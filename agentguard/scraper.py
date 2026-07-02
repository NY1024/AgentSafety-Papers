"""arXiv 论文爬取模块"""

import arxiv
from datetime import datetime, timedelta
from dataclasses import dataclass, field
from typing import List
from .config import Config


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
    # LLM 生成的字段（后续填充）
    category: str = ""
    summary_zh: str = ""
    has_code: bool = False
    code_url: str = ""


def build_query(config: Config) -> str:
    """根据关键词配置构建 arXiv 查询字符串"""
    kw = config.keywords

    # 构建 agent 关键词组
    agent_terms = " OR ".join(f'abs:"{k}"' for k in kw.agent_keywords)

    # 构建安全关键词组
    security_terms = " OR ".join(f'abs:"{k}"' for k in kw.security_keywords)

    query = f"({agent_terms}) AND ({security_terms})"
    return query


def fetch_papers(config: Config) -> List[Paper]:
    """从 arXiv 爬取论文"""
    query = build_query(config)

    sort_map = {
        "SubmittedDate": arxiv.SortCriterion.SubmittedDate,
        "Relevance": arxiv.SortCriterion.Relevance,
        "LastUpdatedDate": arxiv.SortCriterion.LastUpdatedDate,
    }
    sort_by = sort_map.get(config.arxiv.sort_by, arxiv.SortCriterion.SubmittedDate)

    search = arxiv.Search(
        query=query,
        max_results=config.arxiv.max_results,
        sort_by=sort_by,
    )

    client = arxiv.Client()
    papers: List[Paper] = []
    cutoff_date = None
    if config.arxiv.days_back > 0:
        cutoff_date = datetime.now() - timedelta(days=config.arxiv.days_back)

    for result in client.results(search):
        published = result.published
        if cutoff_date and published.replace(tzinfo=None) < cutoff_date:
            continue

        paper = Paper(
            arxiv_id=result.entry_id.split("/abs/")[-1],
            title=result.title.replace("\n", " ").strip(),
            authors=[a.name for a in result.authors],
            abstract=result.summary.replace("\n", " ").strip(),
            published=published.strftime("%Y-%m-%d"),
            updated=result.updated.strftime("%Y-%m-%d"),
            primary_category=result.primary_category,
            pdf_url=result.pdf_url,
            abs_url=result.entry_id,
        )
        papers.append(paper)

    return papers
