"""一次性脚本：用requests直接调arXiv API，跳过已有2000篇，抓取下一批2000篇"""

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

# Atom XML namespace
NS = {"atom": "http://www.w3.org/2005/Atom"}


def build_simple_query(config):
    """构建简化查询 - 减少关键词数量避免URL过长"""
    kw = config.keywords
    # 只用核心关键词，避免URL过长导致500错误
    agent_terms = " OR ".join(f'abs:"{k}"' for k in kw.agent_keywords[:6])
    security_terms = " OR ".join(f'abs:"{k}"' for k in kw.security_keywords[:15])
    return f"({agent_terms}) AND ({security_terms})"


def fetch_page(query, start, max_results=100):
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
    """解析arXiv API返回的XML"""
    root = ET.fromstring(xml_text)
    papers = []
    for entry in root.findall("atom:entry", NS):
        try:
            entry_id = entry.find("atom:id", NS).text
            arxiv_id = entry_id.split("/abs/")[-1]
            title = entry.find("atom:title", NS).text.replace("\n", " ").strip()
            summary = entry.find("atom:summary", NS).text.replace("\n", " ").strip()
            published = entry.find("atom:published", NS).text
            updated = entry.find("atom:updated", NS).text
            authors = [a.find("atom:name", NS).text for a in entry.findall("atom:author", NS)]

            # PDF URL
            pdf_url = ""
            abs_url = entry_id
            for link in entry.findall("atom:link", NS):
                if link.get("title") == "pdf":
                    pdf_url = link.get("href")

            # Primary category
            primary_cat = ""
            for cat in entry.findall("{http://arxiv.org/schemas/atom}primary_category"):
                primary_cat = cat.get("term", "")
                break

            paper = Paper(
                arxiv_id=arxiv_id,
                title=title,
                authors=authors,
                abstract=summary,
                published=datetime.fromisoformat(published.replace("Z", "+00:00")).strftime("%Y-%m-%d"),
                updated=datetime.fromisoformat(updated.replace("Z", "+00:00")).strftime("%Y-%m-%d"),
                primary_category=primary_cat,
                pdf_url=pdf_url,
                abs_url=abs_url,
            )
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

    # 2. 构建简化查询
    query = build_simple_query(config)
    log.info(f"🔍 使用简化查询")

    # 3. 动态计算起始位置（跳过已有论文数）
    START = len(existing_papers)
    TOTAL = 2000  # 每次抓2000篇
    PAGE_SIZE = 100
    all_new_papers = []

    for offset in range(START, START + TOTAL, PAGE_SIZE):
        log.info(f"📄 抓取第 {offset}-{offset+PAGE_SIZE} 篇...")
        xml_text = fetch_page(query, offset, PAGE_SIZE)
        if not xml_text:
            log.error(f"  ❌ 获取失败，跳过")
            time.sleep(3)
            continue

        page_papers = parse_results(xml_text)
        if not page_papers:
            log.info(f"  ⛔ 没有更多结果")
            break

        all_new_papers.extend(page_papers)
        log.info(f"  ✅ 获取 {len(page_papers)} 篇，累计 {len(all_new_papers)} 篇")
        time.sleep(3)  # arXiv限速：3秒/次

    log.info(f"📄 共获取 {len(all_new_papers)} 篇论文")

    # 4. 过滤已有
    fresh_papers = [p for p in all_new_papers if p.arxiv_id not in seen_ids]
    log.info(f"🆕 去重后新增 {len(fresh_papers)} 篇")

    if not fresh_papers:
        log.info("✅ 没有新论文")
        return

    # 5. 分类
    log.info("🏷️ 开始分类...")
    fresh_papers = batch_classify(fresh_papers, config)
    classified = sum(1 for p in fresh_papers if p.category)
    log.info(f"✅ 分类完成: {classified}/{len(fresh_papers)}")

    # 6. 合并保存
    all_papers = fresh_papers + existing_papers
    all_papers.sort(key=lambda p: p.published, reverse=True)

    save_papers(all_papers, config)
    log.info(f"💾 论文数据已保存 ({len(all_papers)} 篇)")

    for p in fresh_papers:
        seen_ids.add(p.arxiv_id)
    save_seen_ids(seen_ids, config)

    # 7. 生成 README
    log.info("📝 生成 README.md...")
    readme_content = generate_readme(all_papers, config)
    save_readme(readme_content, config)
    log.info("✅ README.md 已生成")

    # 统计
    dates = sorted([p.published for p in all_papers])
    log.info(f"🎉 完成！本次新增 {len(fresh_papers)} 篇，总计 {len(all_papers)} 篇")
    log.info(f"📅 日期范围: {dates[0]} ~ {dates[-1]}")

    # 8. 同步到 docs 目录（GitHub Pages）
    import shutil
    docs_dir = Path(__file__).parent / "docs"
    shutil.copy(config.storage.papers_file, docs_dir / "papers.json")
    shutil.copy(config.storage.papers_file, docs_dir / "data" / "papers.json")
    log.info("✅ 已同步 papers.json 到 docs/ 目录")

    # 9. Git 提交推送（自动同步 README + 数据到 GitHub）
    import subprocess
    log.info("📤 提交并推送到 GitHub...")
    try:
        subprocess.run(["git", "add", "-A"], check=True, cwd=str(Path(__file__).parent))
        commit_msg = f"feat: batch fetch {len(fresh_papers)} papers (total {len(all_papers)}, {dates[0]} ~ {dates[-1]})"
        subprocess.run(["git", "commit", "-m", commit_msg], check=True, cwd=str(Path(__file__).parent))
        subprocess.run(["git", "push", "origin", "main"], check=True, cwd=str(Path(__file__).parent))
        log.info("✅ 已推送到 GitHub")
    except subprocess.CalledProcessError as e:
        log.error(f"❌ Git 推送失败: {e}")
        log.error("请手动执行 git push")

    # 10. 触发 GitHub Actions 重新部署 Pages
    log.info("🚀 触发 GitHub Pages 重新部署...")
    try:
        token = subprocess.check_output(
            ["security", "find-internet-password", "-s", "github.com", "-w"],
            stderr=subprocess.DEVNULL
        ).decode().strip()
        repo = "NY1024/AgentSafety-Papers"
        resp = requests.post(
            f"https://api.github.com/repos/{repo}/actions/workflows/daily-update.yml/dispatches",
            headers={"Authorization": f"token {token}", "Accept": "application/vnd.github.v3+json"},
            json={"ref": "main"},
            timeout=10,
        )
        if resp.status_code == 204:
            log.info("✅ 已触发 Pages 重新部署（1-2 分钟后生效）")
        else:
            log.warning(f"⚠️ 触发部署返回 HTTP {resp.status_code}")
    except Exception as e:
        log.warning(f"⚠️ 触发部署失败: {e}")
        log.warning("Pages 将在下次每日自动更新时同步")


if __name__ == "__main__":
    main()
