"""AgentGuard 主入口 - 每日自动追踪大模型 Agent 安全论文"""

import sys
import logging
from pathlib import Path

# 将项目根目录加入 path
sys.path.insert(0, str(Path(__file__).parent))

from agentguard.config import load_config
from agentguard.scraper import fetch_papers, Paper
from agentguard.classifier import batch_classify
from agentguard.storage import load_seen_ids, save_seen_ids, load_papers, save_papers, save_readme
from agentguard.readme_generator import generate_readme


def setup_logging():
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s [%(levelname)s] %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
    )


def main():
    setup_logging()
    log = logging.getLogger("agentguard")

    log.info("🚀 AgentGuard 启动 - 开始追踪 Agent 安全论文")

    # 1. 加载配置
    config = load_config(config_dir=str(Path(__file__).parent / "config"))
    log.info(f"📋 配置加载完成 | arXiv max: {config.arxiv.max_results}")

    # 2. 加载已有数据
    seen_ids = load_seen_ids(config)
    existing_papers = load_papers(config)
    log.info(f"📚 已有论文 {len(existing_papers)} 篇，已处理 ID {len(seen_ids)} 个")

    # 3. 爬取新论文
    log.info("🔍 开始从 arXiv 爬取论文...")
    new_papers = []
    fetch_ok = False
    try:
        new_papers = fetch_papers(config)
        fetch_ok = True
    except Exception as e:
        log.error(f"❌ arXiv 爬取失败: {e}")
        log.warning("⚠️ 跳过本次数据更新，使用已有数据生成 README（CI 不会阻塞部署）")

    log.info(f"📄 arXiv 返回 {len(new_papers)} 篇论文")

    # 4. 过滤已处理的论文
    fresh_papers = [p for p in new_papers if p.arxiv_id not in seen_ids]
    log.info(f"🆕 新论文 {len(fresh_papers)} 篇（过滤已处理 {len(new_papers) - len(fresh_papers)} 篇）")

    if not fresh_papers:
        log.info("✅ 没有新论文，跳过分类")
    else:
        # 5. 关键词规则分类
        log.info("🏷️ 开始关键词规则分类...")
        fresh_papers = batch_classify(fresh_papers, config)
        classified = sum(1 for p in fresh_papers if p.category)
        log.info(f"✅ 分类完成: {classified}/{len(fresh_papers)} 篇成功")

    # 6. 合并并保存
    all_papers = fresh_papers + existing_papers
    # 按发布日期降序排序
    all_papers.sort(key=lambda p: p.published, reverse=True)

    save_papers(all_papers, config)
    log.info(f"💾 论文数据已保存 ({len(all_papers)} 篇)")

    # 更新 seen_ids
    if fetch_ok:
        for p in fresh_papers:
            seen_ids.add(p.arxiv_id)
        save_seen_ids(seen_ids, config)

    # 7. 生成 README
    log.info("📝 生成 README.md...")
    readme_content = generate_readme(all_papers, config, fetch_ok=fetch_ok)
    save_readme(readme_content, config)
    log.info(f"✅ README.md 已生成")

    if fetch_ok:
        log.info(f"🎉 完成！本次新增 {len(fresh_papers)} 篇，总计 {len(all_papers)} 篇论文")
    else:
        log.warning(f"⚠️ 本次跳过爬取，使用已有 {len(all_papers)} 篇论文生成 README，等待下次 CI 重试")


if __name__ == "__main__":
    main()
