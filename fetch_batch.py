"""批量抓取脚本：使用多组子查询策略，抓取历史论文（2022年至今）"""

import sys
import json
import time
import logging
import requests
import xml.etree.ElementTree as ET
from pathlib import Path
from datetime import datetime

sys.path.insert(0, str(Path(__file__).parent))

from agentguard.config import load_config
from agentguard.scraper import Paper
from agentguard.classifier import batch_classify
from agentguard.storage import load_seen_ids, save_seen_ids, load_papers, save_papers, save_readme
from agentguard.readme_generator import generate_readme

logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] %(message)s", datefmt="%Y-%m-%d %H:%M:%S")
log = logging.getLogger("fetch_batch")

ARXIV_API = "http://export.arxiv.org/api/query"
NS = {"atom": "http://www.w3.org/2005/Atom"}

# 只保留 2022 年以后的论文
CUTOFF_DATE = datetime(2022, 1, 1)


def build_sub_queries(config):
    """构建多组子查询，与 scraper.py 中的策略一致"""
    kw = config.keywords

    # Agent + LLM 核心关键词
    agent_core_kws = kw.agent_keywords[:20]
    agent_terms = " OR ".join(f'abs:"{k}"' for k in agent_core_kws)
    llm_terms = " OR ".join(f'abs:"{k}"' for k in kw.llm_keywords[:15])
    agent_llm = f"({agent_terms}) OR ({llm_terms})"

    security_groups = {
        "attack": [
            "attack", "attacker", "jailbreak", "jail break", "jail-breaking",
            "prompt injection", "prompt-injection", "indirect prompt injection",
            "instruction injection", "adversarial", "adversarial attack",
            "adversarial example", "backdoor", "trojan", "poisoning",
            "data poisoning", "exploit", "vulnerability", "vulnerable",
        ],
        "defense": [
            "defense", "defence", "defend", "guardrail", "guard rail",
            "guardrails", "alignment", "safety", "safe AI", "security",
            "trustworthy", "trustworthiness", "sandbox", "isolation",
            "access control", "content filtering", "content filter",
            "constitutional AI", "corrigibility",
        ],
        "privacy": [
            "privacy", "privacy-preserving", "leakage", "data leakage",
            "information leakage", "model extraction", "model stealing",
            "membership inference", "data extraction", "training data extraction",
            "unlearning", "machine unlearning", "re-identification",
            "reidentification", "impersonation",
        ],
        "redteam_misuse": [
            "red team", "red-team", "redteaming", "red teaming",
            "misuse", "abuse", "harmful", "harmful content", "unsafe",
            "threat", "threat model", "social engineering", "phishing",
            "fraud", "scam", "weaponization", "dual-use", "deception",
            "manipulation", "reward hacking",
        ],
        "robust_misc": [
            "robustness", "watermark", "watermarking", "fingerprinting",
            "steganography", "steganographic", "covert", "collusion",
            "specification gaming", "goal misgeneralization", "deceptive alignment",
            "bias", "fairness", "toxicity", "interpretability", "explainability",
            "anomaly detection", "intrusion detection", "malware", "ransomware",
            "supply chain", "circumvent", "bypass", "evasion", "tampering",
            "forgery", "provenance", "attribution", "forensics",
        ],
    }

    queries = []
    for group_name, sec_kws in security_groups.items():
        sec_terms = " OR ".join(f'abs:"{k}"' for k in sec_kws)
        q = f"({agent_llm}) AND ({sec_terms})"
        queries.append((group_name, q))

    return queries


def fetch_page(query, start, max_results=200):
    """获取单页结果"""
    params = {
        "search_query": query,
        "start": start,
        "max_results": max_results,
        "sortBy": "submittedDate",
        "sortOrder": "descending",
    }
    for attempt in range(5):
        try:
            resp = requests.get(ARXIV_API, params=params, timeout=30)
            if resp.status_code == 200:
                return resp.text
            elif resp.status_code == 429:
                wait = 10 * (attempt + 1)
                log.warning(f"  ⏳ 429 限速，等待 {wait}s...")
                time.sleep(wait)
            else:
                log.warning(f"  ⚠️ HTTP {resp.status_code}, 重试 {attempt+1}/5")
                time.sleep(5)
        except Exception as e:
            log.warning(f"  ⚠️ 请求异常: {e}, 重试 {attempt+1}/5")
            time.sleep(5)
    return None


def parse_results(xml_text):
    """解析 arXiv API 返回的 XML"""
    root = ET.fromstring(xml_text)
    papers = []
    for entry in root.findall("atom:entry", NS):
        try:
            entry_id = entry.find("atom:id", NS).text
            arxiv_id = entry_id.split("/abs/")[-1]
            title = entry.find("atom:title", NS).text.replace("\n", " ").strip()
            summary = entry.find("atom:summary", NS).text.replace("\n", " ").strip()
            published_str = entry.find("atom:published", NS).text
            updated_str = entry.find("atom:updated", NS).text
            authors = [a.find("atom:name", NS).text for a in entry.findall("atom:author", NS)]

            pdf_url = ""
            abs_url = entry_id
            for link in entry.findall("atom:link", NS):
                if link.get("title") == "pdf":
                    pdf_url = link.get("href")

            primary_cat = ""
            for cat in entry.findall("{http://arxiv.org/schemas/atom}primary_category"):
                primary_cat = cat.get("term", "")
                break

            published_dt = datetime.fromisoformat(published_str.replace("Z", "+00:00"))
            updated_dt = datetime.fromisoformat(updated_str.replace("Z", "+00:00"))

            paper = Paper(
                arxiv_id=arxiv_id,
                title=title,
                authors=authors,
                abstract=summary,
                published=published_dt.strftime("%Y-%m-%d"),
                updated=updated_dt.strftime("%Y-%m-%d"),
                primary_category=primary_cat,
                pdf_url=pdf_url,
                abs_url=abs_url,
            )
            # 附带 datetime 用于过滤
            paper._published_dt = published_dt.replace(tzinfo=None)
            papers.append(paper)
        except Exception as e:
            log.warning(f"  ⚠️ 解析论文失败: {e}")
    return papers


def main():
    config = load_config(config_dir=str(Path(__file__).parent / "config"))

    # 1. 加载已有数据
    existing_papers = load_papers(config)
    seen_ids = load_seen_ids(config)
    log.info(f"📚 已有论文 {len(existing_papers)} 篇")

    # 已有论文的 ID 集合，用于去重
    existing_ids = {p.arxiv_id for p in existing_papers}
    batch_seen = set()  # 本次批量抓取内去重

    # 2. 构建多组子查询
    queries = build_sub_queries(config)
    log.info(f"🔍 构建 {len(queries)} 组子查询")

    all_new_papers = []
    TOTAL_PER_GROUP = 4000  # 每组最多抓 4000 篇
    PAGE_SIZE = 200

    for group_name, query in queries:
        log.info(f"\n{'='*60}")
        log.info(f"📄 查询组 [{group_name}] (query length: {len(query)} chars)")
        group_count = 0
        consecutive_empty = 0

        for offset in range(0, TOTAL_PER_GROUP, PAGE_SIZE):
            log.info(f"  📄 [{group_name}] 抓取第 {offset}-{offset+PAGE_SIZE} 篇...")
            xml_text = fetch_page(query, offset, PAGE_SIZE)
            if not xml_text:
                log.error(f"  ❌ 获取失败，跳过")
                time.sleep(3)
                continue

            page_papers = parse_results(xml_text)
            if not page_papers:
                log.info(f"  ⛔ 没有更多结果")
                break

            # 过滤：2022年后 + 去重
            page_new = []
            for p in page_papers:
                dt = getattr(p, '_published_dt', None)
                if dt and dt < CUTOFF_DATE:
                    consecutive_empty += 1
                    continue
                if p.arxiv_id in existing_ids or p.arxiv_id in batch_seen:
                    continue
                batch_seen.add(p.arxiv_id)
                page_new.append(p)
                consecutive_empty = 0

            all_new_papers.extend(page_new)
            group_count += len(page_new)
            log.info(f"  ✅ 本页 {len(page_new)} 篇新论文，组累计 {group_count} 篇，总累计 {len(all_new_papers)} 篇")

            # 如果连续多页都是老论文（< 2022），提前停止该组
            if consecutive_empty >= PAGE_SIZE * 3:
                log.info(f"  ⛔ 连续 {consecutive_empty} 篇早于 2022 年，停止 [{group_name}]")
                break

            time.sleep(3)  # arXiv 限速

        log.info(f"📊 [{group_name}] 组完成，新增 {group_count} 篇")

    log.info(f"\n{'='*60}")
    log.info(f"📄 全部查询完成，共获取 {len(all_new_papers)} 篇新论文")

    if not all_new_papers:
        log.info("✅ 没有新论文")
        return

    # 3. 分类
    log.info(f"🏷️ 开始分类 {len(all_new_papers)} 篇论文...")
    all_new_papers = batch_classify(all_new_papers, config)
    classified = sum(1 for p in all_new_papers if p.category)
    log.info(f"✅ 分类完成: {classified}/{len(all_new_papers)}")

    # 4. 合并保存
    all_papers = all_new_papers + existing_papers
    all_papers.sort(key=lambda p: p.published, reverse=True)

    # 清除临时字段
    for p in all_papers:
        if hasattr(p, '_published_dt'):
            delattr(p, '_published_dt')

    save_papers(all_papers, config)
    log.info(f"💾 论文数据已保存 ({len(all_papers)} 篇)")

    for p in all_new_papers:
        seen_ids.add(p.arxiv_id)
    save_seen_ids(seen_ids, config)

    # 5. 生成 README
    log.info("📝 生成 README.md...")
    readme_content = generate_readme(all_papers, config)
    save_readme(readme_content, config)
    log.info("✅ README.md 已生成")

    # 统计
    dates = sorted([p.published for p in all_papers])
    log.info(f"🎉 完成！本次新增 {len(all_new_papers)} 篇，总计 {len(all_papers)} 篇")
    log.info(f"📅 日期范围: {dates[0]} ~ {dates[-1]}")

    # 6. 同步到 docs 目录（GitHub Pages）
    import shutil
    docs_dir = Path(__file__).parent / "docs"
    shutil.copy(config.storage.papers_file, docs_dir / "papers.json")
    log.info("✅ 已同步 papers.json 到 docs/ 目录")

    # 7. Git 提交推送（push 后 deploy-pages.yml 会自动触发 Pages 部署）
    import subprocess
    log.info("📤 提交并推送到 GitHub...")
    try:
        subprocess.run(["git", "add", "-A"], check=True, cwd=str(Path(__file__).parent))
        commit_msg = f"feat: batch fetch {len(all_new_papers)} papers (total {len(all_papers)})"
        subprocess.run(["git", "commit", "-m", commit_msg], check=True, cwd=str(Path(__file__).parent))
        subprocess.run(["git", "pull", "--rebase", "origin", "main"], check=True, cwd=str(Path(__file__).parent))
        subprocess.run(["git", "push", "origin", "main"], check=True, cwd=str(Path(__file__).parent))
        log.info("✅ 已推送到 GitHub，Pages 将自动部署")
    except subprocess.CalledProcessError as e:
        log.error(f"❌ Git 操作失败: {e}")
        log.error("请手动执行: git pull --rebase origin main && git push origin main")


if __name__ == "__main__":
    main()
