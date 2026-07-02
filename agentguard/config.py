"""配置加载模块"""

import yaml
from pathlib import Path
from dataclasses import dataclass, field
from typing import List


@dataclass
class ArxivConfig:
    max_results: int = 200
    sort_by: str = "SubmittedDate"
    days_back: int = 1


@dataclass
class StorageConfig:
    papers_file: str = "data/papers.json"
    readme_file: str = "README.md"
    seen_file: str = "data/seen_ids.json"


@dataclass
class ReadmeConfig:
    page_size: int = 50
    show_abstract: bool = True
    abstract_max_length: int = 200


@dataclass
class CategoryDef:
    name: str
    description: str
    description_en: str = ""
    keywords: List[str] = field(default_factory=list)


@dataclass
class KeywordConfig:
    agent_keywords: List[str] = field(default_factory=list)
    security_keywords: List[str] = field(default_factory=list)
    llm_keywords: List[str] = field(default_factory=list)
    categories: List[CategoryDef] = field(default_factory=list)


@dataclass
class Config:
    arxiv: ArxivConfig = field(default_factory=ArxivConfig)
    storage: StorageConfig = field(default_factory=StorageConfig)
    readme: ReadmeConfig = field(default_factory=ReadmeConfig)
    keywords: KeywordConfig = field(default_factory=KeywordConfig)
    project_root: str = ""


def load_config(config_dir: str = "config") -> Config:
    """加载配置文件"""
    config_dir = Path(config_dir)
    project_root = config_dir.parent.resolve()

    # 加载 settings.yaml
    settings_path = config_dir / "settings.yaml"
    settings = {}
    if settings_path.exists():
        with open(settings_path, "r", encoding="utf-8") as f:
            settings = yaml.safe_load(f) or {}

    # 加载 keywords.yaml
    keywords_path = config_dir / "keywords.yaml"
    keywords_data = {}
    if keywords_path.exists():
        with open(keywords_path, "r", encoding="utf-8") as f:
            keywords_data = yaml.safe_load(f) or {}

    # 构建 Config 对象
    arxiv_data = settings.get("arxiv", {})
    storage_data = settings.get("storage", {})
    readme_data = settings.get("readme", {})

    categories = [
        CategoryDef(
            name=cat.get("name", ""),
            description=cat.get("description", ""),
            description_en=cat.get("description_en", ""),
            keywords=cat.get("keywords", []),
        )
        for cat in keywords_data.get("categories", [])
    ]

    config = Config(
        arxiv=ArxivConfig(
            max_results=arxiv_data.get("max_results", 200),
            sort_by=arxiv_data.get("sort_by", "SubmittedDate"),
            days_back=arxiv_data.get("days_back", 1),
        ),
        storage=StorageConfig(
            papers_file=str(project_root / storage_data.get("papers_file", "data/papers.json")),
            readme_file=str(project_root / storage_data.get("readme_file", "README.md")),
            seen_file=str(project_root / storage_data.get("seen_file", "data/seen_ids.json")),
        ),
        readme=ReadmeConfig(
            page_size=readme_data.get("page_size", 50),
            show_abstract=readme_data.get("show_abstract", True),
            abstract_max_length=readme_data.get("abstract_max_length", 200),
        ),
        keywords=KeywordConfig(
            agent_keywords=keywords_data.get("agent_keywords", []),
            security_keywords=keywords_data.get("security_keywords", []),
            llm_keywords=keywords_data.get("llm_keywords", []),
            categories=categories,
        ),
        project_root=str(project_root),
    )

    return config
