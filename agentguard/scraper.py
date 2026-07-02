"""arXiv 论文爬取模块 - 多组子查询策略，最大化召回"""

import arxiv
import time
import logging
from datetime import datetime, timedelta
from dataclasses import dataclass, field
from typing import List, Tuple
from .config import Config

log = logging.getLogger("agentguard")


@dataclass
class Paper:
    """论文数据结构"""
    arxiv_id: str
    title: str
    authors: List[str]
    abstract: str
    published: str  # ISO 日期字符串
    updated: str
    primary_category: str
    pdf_url: str
    abs_url: str
    # 分类字段
    category: str = ""
    summary_zh: str = ""
    has_code: bool = False
    code_url: str = ""


def build_queries(config: Config) -> List[Tuple[str, str]]:
    """构建多组子查询，每组聚焦不同安全主题，避免 URL 过长
    
    策略: 将安全关键词分成 5 组，每组与 agent+llm 关键词组合，
    形成 5 个子查询，分别搜索后合并去重。
    """
    kw = config.keywords

    # Agent + LLM 核心关键词（abs: 搜索摘要）
    agent_core_kws = kw.agent_keywords[:20]  # 取前 20 个核心词
    agent_terms = " OR ".join(f'abs:"{k}"' for k in agent_core_kws)

    llm_terms = " OR ".join(f'abs:"{k}"' for k in kw.llm_keywords[:15])
    
    agent_llm = f"({agent_terms}) OR ({llm_terms})"

    # 安全关键词分成 5 组（每组 ~15-20 个词），避免 URL 过长
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


def fetch_papers(config: Config) -> List[Paper]:
    """从 arXiv 爬取论文（多组子查询，合并去重）"""
    queries = build_queries(config)
    log.info(f"🔍 构建 {len(queries)} 组子查询")

    sort_map = {
        "SubmittedDate": arxiv.SortCriterion.SubmittedDate,
        "Relevance": arxiv.SortCriterion.Relevance,
        "LastUpdatedDate": arxiv.SortCriterion.LastUpdatedDate,
    }
    sort_by = sort_map.get(config.arxiv.sort_by, arxiv.SortCriterion.SubmittedDate)

    cutoff_date = None
    if config.arxiv.days_back > 0:
        cutoff_date = datetime.now() - timedelta(days=config.arxiv.days_back)

    # 每组查询的最大结果数
    per_query_max = config.arxiv.max_results

    client = arxiv.Client()
    all_papers: List[Paper] = []
    seen_ids = set()

    for group_name, query in queries:
        log.info(f"  📄 查询组 [{group_name}] (query length: {len(query)} chars)")
        try:
            search = arxiv.Search(
                query=query,
                max_results=per_query_max,
                sort_by=sort_by,
            )

            group_count = 0
            for result in client.results(search):
                published = result.published
                if cutoff_date and published.replace(tzinfo=None) < cutoff_date:
                    continue

                arxiv_id = result.entry_id.split("/abs/")[-1]
                if arxiv_id in seen_ids:
                    continue
                seen_ids.add(arxiv_id)

                paper = Paper(
                    arxiv_id=arxiv_id,
                    title=result.title.replace("\n", " ").strip(),
                    authors=[a.name for a in result.authors],
                    abstract=result.summary.replace("\n", " ").strip(),
                    published=published.strftime("%Y-%m-%d"),
                    updated=result.updated.strftime("%Y-%m-%d"),
                    primary_category=result.primary_category,
                    pdf_url=result.pdf_url,
                    abs_url=result.entry_id,
                )
                all_papers.append(paper)
                group_count += 1

            log.info(f"  ✅ [{group_name}] 获取 {group_count} 篇新论文")
        except Exception as e:
            log.warning(f"  ⚠️ [{group_name}] 查询失败: {e}")

        # arXiv 限速：每组查询间隔 3 秒
        time.sleep(3)

    log.info(f"📊 多组查询完成，共获取 {len(all_papers)} 篇去重论文")
    return all_papers
