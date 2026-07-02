"""数据存储模块"""

import json
from pathlib import Path
from typing import List, Set
from .config import Config
from .scraper import Paper


def load_seen_ids(config: Config) -> Set[str]:
    """加载已处理论文 ID 集合"""
    seen_path = Path(config.storage.seen_file)
    if not seen_path.exists():
        return set()
    with open(seen_path, "r", encoding="utf-8") as f:
        return set(json.load(f))


def save_seen_ids(seen: Set[str], config: Config):
    """保存已处理论文 ID"""
    seen_path = Path(config.storage.seen_file)
    seen_path.parent.mkdir(parents=True, exist_ok=True)
    with open(seen_path, "w", encoding="utf-8") as f:
        json.dump(sorted(list(seen)), f, ensure_ascii=False, indent=2)


def load_papers(config: Config) -> List[Paper]:
    """加载已存储的论文列表"""
    papers_path = Path(config.storage.papers_file)
    if not papers_path.exists():
        return []
    with open(papers_path, "r", encoding="utf-8") as f:
        data = json.load(f)
    return [Paper(**item) for item in data]


def save_papers(papers: List[Paper], config: Config):
    """保存论文列表"""
    papers_path = Path(config.storage.papers_file)
    papers_path.parent.mkdir(parents=True, exist_ok=True)
    data = [paper.__dict__ for paper in papers]
    with open(papers_path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)


def save_readme(content: str, config: Config):
    """保存 README 文件"""
    readme_path = Path(config.storage.readme_file)
    with open(readme_path, "w", encoding="utf-8") as f:
        f.write(content)
