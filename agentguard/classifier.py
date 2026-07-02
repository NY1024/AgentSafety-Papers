"""论文分类模块 - 基于关键词规则分类，优先级制"""

import logging
from .config import Config
from .scraper import Paper

log = logging.getLogger("agentguard")


def classify(paper: Paper, config: Config) -> str:
    """基于关键词规则对论文进行分类。
    
    策略：按 categories 列表顺序（优先级从高到低）遍历，
    返回第一个命中关键词的类别。列表中靠前的类别更具体，优先级更高。
    """
    text = (paper.title + " " + paper.abstract).lower()
    for cat in config.keywords.categories:
        if not cat.keywords:
            continue
        for kw in cat.keywords:
            if kw.lower() in text:
                return cat.name
    return "other"


def batch_classify(papers, config: Config) -> list:
    """批量分类论文"""
    for i, paper in enumerate(papers):
        paper.category = classify(paper, config)
        log.info(f"  [{i+1}/{len(papers)}] {paper.arxiv_id} → {paper.category}")
    return papers
