"""README 生成模块"""

from datetime import datetime, timedelta
from typing import List
from .config import Config
from .scraper import Paper


def _format_authors(authors: List[str], max_n: int = 3) -> str:
    """格式化作者列表，最多显示 max_n 人，超出用 et al."""
    if not authors:
        return "Unknown"
    if len(authors) <= max_n:
        return ", ".join(authors)
    return ", ".join(authors[:max_n]) + " et al."


def _escape_md(text: str) -> str:
    """转义 Markdown 特殊字符（用于标题等）"""
    for ch in ('|',):
        text = text.replace(ch, f'\\{ch}')
    return text


def generate_readme(papers: List[Paper], config: Config) -> str:
    """生成 README.md 内容

    策略：
    - README 只展示最近 30 天论文，含日期、作者、可折叠摘要
    - 完整论文列表引导到 GitHub Pages
    """
    lines = []

    now = datetime.now()
    cutoff = (now - timedelta(days=30)).strftime("%Y-%m-%d")
    recent_papers = [p for p in papers if p.published >= cutoff]
    recent_papers.sort(key=lambda p: p.published, reverse=True)

    # GitHub README 渲染限制 ~512KB，限制展示数量
    MAX_DISPLAY = 500
    total_recent = len(recent_papers)
    show_papers = recent_papers[:MAX_DISPLAY]
    capped = total_recent > MAX_DISPLAY

    # ---- 头部 ----
    lines.append('<div align="center">')
    lines.append("")
    lines.append("# AgentGuard 🛡️")
    lines.append("")
    lines.append("**Daily Tracking of LLM Agent Security Papers on arXiv**")
    lines.append("")
    lines.append("[![Auto Update](https://github.com/NY1024/AgentSafety-Papers/actions/workflows/daily-update.yml/badge.svg)](https://github.com/NY1024/AgentSafety-Papers/actions/workflows/daily-update.yml)")
    lines.append(f"[![Papers](https://img.shields.io/badge/Papers-{len(papers)}-blue)](#)")
    lines.append("[![License](https://img.shields.io/badge/License-MIT-green)](#)")
    lines.append("")
    lines.append("</div>")
    lines.append("")
    lines.append("---")
    lines.append("")

    # ---- 简介 ----
    lines.append("## 📖 简介 / Introduction")
    lines.append("")
    lines.append("自动追踪 arXiv 上大模型 Agent 安全方向的最新论文，每日更新，关键词智能分类。")
    lines.append("")
    lines.append("*Automatically tracking the latest LLM Agent security papers on arXiv, updated daily with keyword-based classification.*")
    lines.append("")
    lines.append(f"**最近更新 / Last Updated**: {now.strftime('%Y-%m-%d %H:%M')} ｜ **论文总数 / Total Papers**: {len(papers)}（近 30 天 / Recent 30 days: {total_recent}）")
    lines.append("")
    lines.append(f"🌐 **[GitHub Pages](https://ny1024.github.io/AgentSafety-Papers/)** — 查看全部 {len(papers)} 篇论文（含摘要、分类筛选、搜索）/ View all {len(papers)} papers with abstracts, filters & search")
    lines.append("")

    # ---- 分类导航 ----
    lines.append("## 📑 分类导航 / Category Navigation")
    lines.append("")
    category_counts = {}
    for p in papers:
        cat = p.category or "other"
        category_counts[cat] = category_counts.get(cat, 0) + 1

    for cat_def in config.keywords.categories:
        count = category_counts.get(cat_def.name, 0)
        if count > 0:
            anchor = cat_def.name.lower()
            desc = f"{cat_def.description} / {cat_def.description_en}" if cat_def.description_en else cat_def.description
            lines.append(f"- **[{cat_def.name}](#-{anchor})** — {desc} — {count}")
    lines.append("")

    # ---- 近 30 天论文 ----
    lines.append(f"## 📄 近期论文 / Recent Papers (Last 30 Days)")
    lines.append("")
    if capped:
        lines.append(f"> 仅展示最近 30 天中最新的 {MAX_DISPLAY} 篇论文（含日期、作者、摘要）。近 30 天共 {total_recent} 篇，完整 {len(papers)} 篇论文列表请访问 [GitHub Pages](https://ny1024.github.io/AgentSafety-Papers/)")
        lines.append("")
        lines.append(f"> Showing the latest {MAX_DISPLAY} of {total_recent} papers from the last 30 days (with date, authors & abstract). For the full list of {len(papers)} papers, visit [GitHub Pages](https://ny1024.github.io/AgentSafety-Papers/)")
    else:
        lines.append(f"> 仅展示最近 30 天的论文（含日期、作者、摘要）。完整 {len(papers)} 篇论文列表请访问 [GitHub Pages](https://ny1024.github.io/AgentSafety-Papers/)")
        lines.append("")
        lines.append(f"> Showing only papers from the last 30 days (with date, authors & abstract). For the full list of {len(papers)} papers, visit [GitHub Pages](https://ny1024.github.io/AgentSafety-Papers/)")
    lines.append("")

    if not show_papers:
        lines.append("*最近 30 天暂无新论文 / No new papers in the last 30 days.*")
        lines.append("")
    else:
        for cat_def in config.keywords.categories:
            cat_papers = [p for p in show_papers if (p.category or "other") == cat_def.name]
            if not cat_papers:
                continue
            cat_papers.sort(key=lambda p: p.published, reverse=True)

            desc = f"{cat_def.description} / {cat_def.description_en}" if cat_def.description_en else cat_def.description
            lines.append(f"### 📂 {cat_def.name}")
            lines.append(f"*{desc}* — {len(cat_papers)} papers")
            lines.append("")

            for p in cat_papers:
                title = _escape_md(p.title.strip())
                authors = _format_authors(p.authors)
                abstract = p.abstract.strip() if p.abstract else "No abstract available."
                # 截断过长摘要
                if len(abstract) > 500:
                    abstract = abstract[:500] + "..."

                lines.append(f"- **{p.published}** — {authors} — [{title}]({p.abs_url})")
                lines.append(f"  <details><summary>📄 Abstract</summary>")
                lines.append(f"  {abstract}")
                lines.append(f"  </details>")
                lines.append("")

            lines.append("")

    # ---- 统计 ----
    if category_counts:
        lines.append("## 📊 统计 / Statistics")
        lines.append("")
        lines.append("| 分类 / Category | 论文数 / Count |")
        lines.append("|------|--------|")
        for cat_def in config.keywords.categories:
            count = category_counts.get(cat_def.name, 0)
            if count > 0:
                lines.append(f"| {cat_def.name} | {count} |")
        lines.append("")

    # ---- 页脚 ----
    lines.append("---")
    lines.append("")
    lines.append(f"📚 **全部 {len(papers)} 篇论文**（2022 至今）请访问 [GitHub Pages](https://ny1024.github.io/AgentSafety-Papers/) 查看完整列表、搜索与筛选。")
    lines.append("")
    lines.append(f"*Generated by AgentGuard at {now.strftime('%Y-%m-%d %H:%M:%S')}*")

    return "\n".join(lines)
