<div align="center">

# AgentGuard 🛡️

**Daily Tracking of LLM Agent Security Papers on arXiv**

[![Auto Update](https://github.com/NY1024/AgentSafety-Papers/actions/workflows/daily-update.yml/badge.svg)](https://github.com/NY1024/AgentSafety-Papers/actions/workflows/daily-update.yml)
[![Papers](https://img.shields.io/badge/Papers-29019-blue)](#)
[![License](https://img.shields.io/badge/License-MIT-green)](#)

</div>

---

## 📖 简介 / Introduction

自动追踪 arXiv 上大模型 Agent 安全方向的最新论文，每日更新，关键词智能分类。

*Automatically tracking the latest LLM Agent security papers on arXiv, updated daily with keyword-based classification.*

**最近更新 / Last Updated**: 2026-09-24 10:58 ｜ **论文总数 / Total Papers**: 29019（近 30 天 / Recent 30 days: 4032）

🌐 **[GitHub Pages](https://ny1024.github.io/AgentSafety-Papers/)** — 查看全部 29019 篇论文（含摘要、分类筛选、搜索）/ View all 29019 papers with abstracts, filters & search

## 📑 分类导航 / Category Navigation

- **[jailbreak](#-jailbreak)** — 越狱攻击 / Jailbreak Attacks — 634
- **[prompt-injection](#-prompt-injection)** — 提示注入攻击 / Prompt Injection Attacks — 552
- **[memory-poisoning](#-memory-poisoning)** — 记忆投毒与篡改 / Memory Poisoning & Tampering — 50
- **[tool-use-attack](#-tool-use-attack)** — 工具使用攻击 / Tool-Use Attacks — 138
- **[backdoor](#-backdoor)** — 后门与投毒攻击 / Backdoor & Poisoning Attacks — 473
- **[adversarial-attack](#-adversarial-attack)** — 对抗攻击 / Adversarial Attacks — 602
- **[privacy-leakage](#-privacy-leakage)** — 隐私泄露 / Privacy Leakage — 4153
- **[steganography](#-steganography)** — 隐写与隐蔽通信 / Steganography & Covert Communication — 71
- **[misuse](#-misuse)** — 滥用与误用 / Misuse & Abuse — 1048
- **[red-teaming](#-red-teaming)** — 红队测试 / Red Teaming — 127
- **[vulnerability](#-vulnerability)** — 漏洞与攻击面 / Vulnerabilities & Attack Surfaces — 3200
- **[defense](#-defense)** — 防御与防护方法 / Defense & Protection Methods — 3027
- **[alignment](#-alignment)** — 对齐与安全约束 / Alignment & Safety Constraints — 2815
- **[robustness](#-robustness)** — 鲁棒性与可靠性 / Robustness & Reliability — 2993
- **[watermark](#-watermark)** — 水印与溯源 / Watermarking & Provenance — 472
- **[unlearning](#-unlearning)** — 机器遗忘 / Machine Unlearning — 97
- **[agent-safety](#-agent-safety)** — Agent 安全框架 / Agent Safety Frameworks — 55
- **[benchmark](#-benchmark)** — 安全评测与基准 / Safety Benchmarks & Evaluation — 66
- **[survey](#-survey)** — 综述与系统化 / Surveys & Systematization — 359
- **[other](#-other)** — 其他安全相关 / Other Security-Related — 8087

## 📄 近期论文 / Recent Papers (Last 30 Days)

> 仅展示最近 30 天中最新的 500 篇论文（含日期、作者、摘要）。近 30 天共 4032 篇，完整 29019 篇论文列表请访问 [GitHub Pages](https://ny1024.github.io/AgentSafety-Papers/)

> Showing the latest 500 of 4032 papers from the last 30 days (with date, authors & abstract). For the full list of 29019 papers, visit [GitHub Pages](https://ny1024.github.io/AgentSafety-Papers/)

### 📂 jailbreak
*越狱攻击 / Jailbreak Attacks* — 2 papers

- **2026-09-23** — Kian Shamsaie, Iman Modarressi — [Psychoacoustically Aligned Latent Smoothing for Adversarial Robustness of Full-Duplex Speech-to-Speech Dialogue Models](http://arxiv.org/abs/2609.27378v1)
  <details><summary>📄 Abstract</summary>
  End-to-end speech-to-speech dialogue models listen and speak simultaneously, so a continuously open acoustic channel is exposed to adversarial manipulation. We formalize imperceptible attacks on full-duplex agents as optimization over additive perturbations confined beneath the psychoacoustic masking threshold of the carrier speech, under three goals: targeted semantic hijacking, response suppression, and policy jailbreaking. Against an undefended Moshi-style agent, white-box attacks succeed in ...
  </details>

- **2026-09-21** — Fernando Outeda, Gustavo Betarte, Juan Diego Campo et al. — [Decoding Guardrails: XAI-Guided Perturbation Analysis of Prompt Injection Detection](http://arxiv.org/abs/2609.24801v1)
  <details><summary>📄 Abstract</summary>
  Large language models (LLMs) are increasingly deployed in production systems, raising concerns about their exposure to adversarial manipulation through prompt injection and jailbreak attacks. Classifier-based guardrails, such as Prompt Guard 2, are widely used as a first line of defense against such attacks, but their internal decision logic is largely opaque to both defenders and attackers. This paper presents an exploratory case study that applies explainable artificial intelligence (XAI) tech...
  </details>


### 📂 prompt-injection
*提示注入攻击 / Prompt Injection Attacks* — 5 papers

- **2026-09-23** — Jasem Khelifi, Issam Oukhay, Ali Ouni et al. — [Specifying and Maintaining Agentic Workflows: An Empirical Study of GitHub Agentic Workflows](http://arxiv.org/abs/2609.27263v1)
  <details><summary>📄 Abstract</summary>
  Agentic workflows shift software development from prompting AI agents for individual tasks to defining recurring work that agents execute automatically. GitHub Agentic Workflows (gh-aw) enables this approach through Markdown files that combine natural-language instructions with configuration and compile into executable GitHub Actions workflows. Unlike conventional workflows that primarily prescribe scripted operations, these files delegate tasks requiring interpretation to AI agents. They also c...
  </details>

- **2026-09-22** — Reshabh K Sharma, Linxi Jiang, Shuo Chen et al. — [Ajar: Measuring Open Privilege in Agent Defenses](http://arxiv.org/abs/2609.26900v1)
  <details><summary>📄 Abstract</summary>
  A language model agent acts through the tools it is given. The data it reads while working on a task can redirect what it does with those tools. A growing set of techniques for safe and secure agent execution therefore sits between the agent and its tools, aiming to enforce access control, information flow or isolation at that boundary. Today these techniques are evaluated on agent-security benchmarks built around indirect prompt injection. Those benchmarks judge a defense by how far it brings t...
  </details>

- **2026-09-21** — Volkan Dağlı, Zerrin Dağlı, Dağhan Dağlı — [Universal Fractal Natural Language Decision Map: Real-Time Edge Triage Across Heterogeneous Domains](http://arxiv.org/abs/2609.25498v1)
  <details><summary>📄 Abstract</summary>
  Deploying Large Language Models for runtime operational triage incurs prohibitive latency (>100-500 ms), high VRAM requirements (>4-8 GB), and excessive energy dissipation. Extending Mandelbrot Fractal Neural Synthesis (Dagli et al., 2026), this paper presents the Universal Fractal Natural Language Decision Map, realized via the werr machine-native edge reflex runtime and the production answerr platform (https://answerr.me). Operating entirely without stored weight tensors (0 Bytes VRAM), the en...
  </details>

- **2026-09-21** — Kaiyuan Zhang, Yuke Peng, Ke Jiang et al. — [ActGov: Governing LLM Agent Actions via Policy-Constrained Validation](http://arxiv.org/abs/2609.24446v2)
  <details><summary>📄 Abstract</summary>
  Large language model (LLM) agents increasingly execute long-horizon workflows through external tools, allowing untrusted outputs to influence subsequent actions and exceed user authorization. Existing defenses isolate injected content or constrain execution with predefined plans and static policies, but these approaches are brittle under dynamic workflows and scale poorly across extensible tool ecosystems.   In this work, we present ActGov, a runtime enforcement framework that validates each LLM...
  </details>

- **2026-09-21** — Kaiyuan Zhang, Yuke Peng, Ke Jiang et al. — [ActGov: Governing LLM Agent Actions via Policy-Constrained Validation](http://arxiv.org/abs/2609.24446v1)
  <details><summary>📄 Abstract</summary>
  Large language model (LLM) agents increasingly execute long-horizon workflows through external tools, allowing untrusted outputs to influence subsequent actions and exceed user authorization. Existing defenses isolate injected content or constrain execution with predefined plans and static policies, but these approaches are brittle under dynamic workflows and scale poorly across extensible tool ecosystems.   In this work, we present ActGov, a runtime enforcement framework that validates each LLM...
  </details>


### 📂 memory-poisoning
*记忆投毒与篡改 / Memory Poisoning & Tampering* — 1 papers

- **2026-09-21** — Ivan Aleksandrov, German Kochnev, Sabrina Sadiekh et al. — [DUMA-Bench: A Dual-Control Multi-Agent Benchmark for Evaluating LLM Agent Security](http://arxiv.org/abs/2609.24662v1)
  <details><summary>📄 Abstract</summary>
  LLM-based agents increasingly operate in environments where they interact with users, tools, and external systems. Yet most security evaluations assume passive users and static control, ignoring the interactive dynamics that shape real agent behavior. We introduce \textbf{DUMA-Bench}, a benchmark and evaluation protocol for measuring agent security under \emph{dual-control} interaction, where both the agent and the user can influence the shared environment state. DUMA-Bench extends $τ^2$-bench ~...
  </details>


### 📂 tool-use-attack
*工具使用攻击 / Tool-Use Attacks* — 2 papers

- **2026-09-22** — Shuang Guo — [SkillApt: Learning When to Activate Agent Skills from Counterfactual Evidence](http://arxiv.org/abs/2609.26863v1)
  <details><summary>📄 Abstract</summary>
  Large language model agents increasingly retrieve reusable Skills and inject them into the active context. However, a retrieved Skill can be relevant yet unnecessary, costly, or even harmful in the current execution state. We present SkillApt, a post-retrieval activation framework that decides whether a retrieved Skill should actually be loaded. SkillApt builds execution evidence from matched WITH/WITHOUT runs and uses outcomes from similar historical states to make a LOAD/ABSTAIN decision for e...
  </details>

- **2026-09-22** — Laizhen Li, Xuan Wang, Peicheng Zhao et al. — [A2M: Trace-Optimized Agent Hijacking in the MCP Ecosystem](http://arxiv.org/abs/2609.26761v1)
  <details><summary>📄 Abstract</summary>
  Agents using the Model Context Protocol (MCP) rely on semantic matching to select tools from third-party servers, exposing a semantic supply-chain risk through attacker-controlled metadata and outputs. We introduce A2M (Attraction-to-Manipulation), a two-stage black-box framework for hijacking MCP agents. The Attraction phase optimizes tool metadata to increase invocation probability; the Manipulation phase uses execution traces to refine adversarial tool returns that steer agents toward attacke...
  </details>


### 📂 backdoor
*后门与投毒攻击 / Backdoor & Poisoning Attacks* — 6 papers

- **2026-09-23** — Jinwen Xin, Dongni Zhang, Chenyang Wang et al. — [RAMP: Reversing Adversarial Perturbations to Strengthen Clean-Label Backdoor Attacks against Malware Detectors](http://arxiv.org/abs/2609.27422v1)
  <details><summary>📄 Abstract</summary>
  Deep learning-based malware detectors are commonly updated by fine-tuning on newly collected samples, but this practical update pipeline also creates an attack surface for training-time backdoor attacks. In realistic crowdsourced data collection, however, strict label vetting typically restricts attackers to the clean-label setting, in which poisoned samples must retain benign labels and functionality, making effective backdoor injection substantially harder. We present a new attack perspective ...
  </details>

- **2026-09-22** — Yue Xing, Pengfei He, Zitao Li — [The Like Trap: Multi-Stage Poisoning against Agents in Similarity-based Recommendation Systems](http://arxiv.org/abs/2609.27155v1)
  <details><summary>📄 Abstract</summary>
  With recent advancements in large language models (LLMs) and LLM-based agents, these agents are becoming increasingly autonomous and gaining broader access to act on users' behalf on the internet. However, the vulnerability of automated agents deployed on social media platforms (e.g., for managing a user's personal account) remains underexplored. Existing studies on agent poisoning typically assume that the adversary can expose poisoned content to the agent. Although such an attack is direct and...
  </details>

- **2026-09-22** — Tianhao Chen, Yuhan Wei, Weifei Jin et al. — [Divide and Doubt: Diverse Distributed Poisoning for Retrieval-Augmented Generation](http://arxiv.org/abs/2609.27090v1)
  <details><summary>📄 Abstract</summary>
  Multi-passage corpus poisoning often repeats one target claim across similar documents, creating correlated lexical and semantic patterns that similarity- and conflict-aware defenses can suppress jointly. We introduce DnD (Divide and Doubt), a targeted attack based on two principles: distributing support for the target answer across stylistically diverse passages, and including a passage that casts doubt on evidence for the reference answer. The first disperses poison-passage representations in ...
  </details>

- **2026-09-22** — Zijian Zhang, Zhen Zeng, Zhongshu Gu et al. — [Backdoors in Learning-Based Industrial Robotic Arm Manipulation: An Empirical Security Study](http://arxiv.org/abs/2609.26868v1)
  <details><summary>📄 Abstract</summary>
  Learning-based models (e.g., visuomotor and Vision-Language-Action (VLA)) are increasingly explored for industrial robotic manipulation, where model predictions are directly translated into physical actions. This tight coupling between model behavior and physical execution makes hidden security vulnerabilities particularly consequential. While backdoor attacks have been widely studied in conventional AI models, their effects on deployed learning-based robotic arm manipulation systems remain less...
  </details>

- **2026-09-21** — Abdullahil Kafi, Alvi Ataur Khalil — [RAG-NAROK: Retrieval-Aware Knowledge Corpus Poisoning in RAG with Source-specific Refutation](http://arxiv.org/abs/2609.25469v1)
  <details><summary>📄 Abstract</summary>
  Retrieval augmented generation (RAG) systems have emerged as the dominant architecture for grounding large language model (LLM) outputs in verifiable external knowledge, yet their structural reliance on a dynamic retrieval pipeline introduces a largely unexplored class of adversarial vulnerability. Existing knowledge-base poisoning attacks are fundamentally static. Adversarial documents are pre-computed and injected without any awareness of what the victim system will actually retrieve for a giv...
  </details>

- **2026-09-21** — Eric Xue, Ruiyi Zhang, Kevin Xue et al. — [OPBackdoor: Opportunistic Backdoors via Alibi-Aligned Reasoning](http://arxiv.org/abs/2609.24826v1)
  <details><summary>📄 Abstract</summary>
  When a backdoor trigger activates the target response regardless of the triggered prompt context, the backdoor objective reveals itself. Challenging this trigger-sufficient formulation across the LLM backdoor literature, we introduce Opportunistic Backdoors (OPBackdoor), in which the backdoor objective is elicited only when the triggered prompt context presents an exploitable opportunity, enabling the model's think to disguise its pursuit through alibi-aligned reasoning that is logical with resp...
  </details>


### 📂 adversarial-attack
*对抗攻击 / Adversarial Attacks* — 5 papers

- **2026-09-23** — Yihong Zhou, Hanbin Yang, Thomas Morstyn — [Finite-Sample Probabilistic Safety Certification for AI-Based Grid-Edge Coordination](http://arxiv.org/abs/2609.28182v1)
  <details><summary>📄 Abstract</summary>
  Coordinating large population of flexible grid-edge devices can alleviate the need for time-consuming and capital-intensive network upgrades, and AI-based control methods such as multi-agent reinforcement learning or imitation learning are promising in their real-time decision scalability. However, system operators still need an independent and rigorous way to decide whether a given AI system is safe enough for deployment. This paper develops a finite-sample probabilistic safety certification fr...
  </details>

- **2026-09-23** — Jiaxi Wu, Tiantian Zhang, Yuxing Wang et al. — [Robust Adversarial Reinforcement Learning with Risk Sensitivity and Critic Consistency Regularization](http://arxiv.org/abs/2609.27667v1)
  <details><summary>📄 Abstract</summary>
  Reinforcement learning (RL) achieves strong performance in sequential decision-making but remains brittle under dynamic uncertainty and distributional shifts. Robust Adversarial Reinforcement Learning (RARL) improves robustness via worst-case perturbations, but existing approaches frequently suffer from unstable optimization and degraded value estimation. In particular, overly aggressive adversaries can drive the agent toward uninformative failure states, while adversarial perturbations amplify ...
  </details>

- **2026-09-22** — Felix Rosberg, Cristofer Englund, Eren Erdal Aksoy et al. — [Adversarial Attacks and Identity Leakage in De-Identification Systems: An Empirical Study](http://arxiv.org/abs/2609.27022v1)
  <details><summary>📄 Abstract</summary>
  In this paper, we investigate the impact of adversarial attacks on identity encoders within a realistic de-identification framework. Our experiments show that the transferability of attacks transfers from an external surrogate model to the system model (e.g., CosFace to ArcFace) allows the adversary to cause identity information to leak in a sufficiently sensitive face recognition system. We present experimental evidence and propose strategies to mitigate this vulnerability. Specifically, we sho...
  </details>

- **2026-09-22** — Christopher Burger, Christina Trotter, Joseph Carlisle et al. — [Evaluating the Semantic-to-Geometric Gap in Adversarial Defenses Against Vision-Language Model-Based Plagiarism](http://arxiv.org/abs/2609.26733v1)
  <details><summary>📄 Abstract</summary>
  The rapidly advancing capabilities of vision-language models (VLMs) present a systemic challenge to academic integrity. VLMs now allow students to bypass meaningful engagement by capturing and submitting graphical problems as singular images, a practice we define as trivial plagiarism. To provide educators with actionable data on VLM limitations, we investigate the efficacy of heuristic adversarial image transformations designed to degrade model performance while remaining human-interpretable. T...
  </details>

- **2026-09-21** — Florian Krone, Elena Hoemann, Sven Hallerbach — [Reinforcement Learning Inspired Black-box Adversarial Attacks for Computer Vision](http://arxiv.org/abs/2609.24249v1)
  <details><summary>📄 Abstract</summary>
  Neural networks, both convolution or transformer based, are essential for modern computer vision systems. However, they are vulnerable to small perturbations, almost imperceptible to humans, which significantly alter the model's prediction. These adversarial attacks are often considered to be a significant threat to the implementation of neural networks in safety-critical applications. Most attacks utilize the white-box threat model and therefore require full access to the target model, making t...
  </details>


### 📂 privacy-leakage
*隐私泄露 / Privacy Leakage* — 28 papers

- **2026-09-23** — Mingyuan Li, Yanna Jiang, Guangsheng Yu et al. — [Your Model Is Leaking: Covert Information Transfer through LLM Residual Streams](http://arxiv.org/abs/2609.27996v1)
  <details><summary>📄 Abstract</summary>
  Privacy-sensitive organizations may run large language models (LLMs) in restricted or air-gapped environments while exporting selected diagnostic artifacts. We show that a compromised runtime component can hide sensitive information in intermediate activations that are allowed to leave the restricted environment. An offline observer can recover this information with a simple linear decoder. The attack requires no model retraining or weight modification, no attacker-controlled egress, and no cont...
  </details>

- **2026-09-23** — Zhonghao Sun, Zhiliang Tian, Xinyue Fang et al. — [Only Pay What You Must Spend: On-Demand Privacy Budget Payment for Differentially Private RAG](http://arxiv.org/abs/2609.27406v1)
  <details><summary>📄 Abstract</summary>
  Deploying large language models (LLMs) on sensitive data via Retrieval-Augmented Generation (RAG) introduces severe privacy risks. Recent studies apply Differential Privacy (DP) to LLMs with RAG for formal privacy guarantees. However, existing DP-RAG frameworks rapidly exhaust the privacy budget. Although recent efforts attempt to save the budget by narrowing the retrieval scope or sparsifying private generation, these methods themselves cumulatively consume the budget, whereas they could actual...
  </details>

- **2026-09-23** — Julian Oelhaf, Georg Kordowich, Christian Bergler et al. — [EvEMTBench: An Open Benchmark for Machine Learning in Power System Protection](http://arxiv.org/abs/2609.28149v1)
  <details><summary>📄 Abstract</summary>
  Studies of machine-learning-based power system protection are difficult to compare because task definitions, measurement access, data partitions, metrics, and generalization conditions often differ. EvEMTBench addresses this gap with an open, executable, and versioned benchmark that fixes these evaluation choices while leaving model design open. Across four grids spanning 20-345 kV, it defines 12 protection and event-analysis functions instantiated as 24 scored tasks and supports structured eval...
  </details>

- **2026-09-23** — Zhen Yu, Yang Liu, Xiahai Zhuang et al. — [A generalizable structural brain MRI foundation model built through dual-priority federated pretraining](http://arxiv.org/abs/2609.27611v1)
  <details><summary>📄 Abstract</summary>
  Foundation models hold promise for generalizable analysis of structural brain magnetic resonance imaging (MRI) across development, aging and disease. However, existing models are typically built through centralized pretraining on pooled data, despite privacy and governance constraints. Such pooling optimization can overemphasize cohort size and overlook complementary information from smaller, specialized cohorts. Here we present BrainFedFM, a structural brain MRI foundation model federatively pr...
  </details>

- **2026-09-23** — Sai Karthik Kosuri, Ankita Shashikant Bhosale, Michael Glick et al. — [EviStreams: Human-in-the-Loop AI Data Extraction for Systematic Reviews in Medicine](http://arxiv.org/abs/2609.27418v1)
  <details><summary>📄 Abstract</summary>
  Systematic reviews underpin clinical guidelines, yet their data-extraction step is a major expert-labor bottleneck bound by a protocolized workflow: two reviewers extract each study independently, an adjudicator resolves disagreements, and the team keeps an auditable record of how every value was produced. Large language models can assist with extraction, but that assistance must fit established review protocols and preserve reproducibility. We present EviStreams, a live, open-source, no-code we...
  </details>

- **2026-09-22** — Daniel Adu Worae, Spyridon Mastorakis, Nuno Moniz et al. — [Adaptive Traffic Camouflage: Causal and Resource-Aware Defense Against IoT Fingerprinting](http://arxiv.org/abs/2609.25787v2)
  <details><summary>📄 Abstract</summary>
  Encryption hides IoT payloads, but traffic shape can still reveal device identity through packet sizes, timing, direction, and packetization. We present Adaptive Traffic Camouflage, a causal, leakage-aware controller that characterizes traffic-shape leakage without runtime device labels and selects a budget-feasible transformation for the next traffic window from previous-window context. The controller chooses among padding, packet splitting, timing, and composite transformations, or leaves traf...
  </details>

- **2026-09-22** — Yuki Ueno, Aditeya Pandey — [ChartRevive: Reconstructing Data Visualizations from Chart Images Using MLLM](http://arxiv.org/abs/2609.27146v1)
  <details><summary>📄 Abstract</summary>
  Static chart images are widely used in scientific publications, business reports, and presentations, yet recovering both the underlying data and visual design from chart images remains a labor-intensive manual process, making them difficult to reuse. While prior work has primarily focused on data extraction, the extraction of visual design specifications, including colors, marker shapes, and axis configurations, remains underexplored. To identify a suitable model for chart reconstruction, we sys...
  </details>

- **2026-09-22** — Kyaw Hpone Myint, Nan Jiang, Xiang Li et al. — [QUARTET: Quad-branch cross-Attention and Random-walk Traces for Enhancing Transformers on Relational Graphs](http://arxiv.org/abs/2609.26855v1)
  <details><summary>📄 Abstract</summary>
  Relational Deep Learning (RDL) models multi-table databases as heterogeneous temporal graphs, and graph transformers currently achieve state-of-the-art performance on benchmarks like RelBench. However, the current leading model, RelGT, suffers from two key limitations: its random local sampler yields loosely connected subgraphs that hinder message passing, and its global attention module relies on a single, seed-feature-based memory that ignores broader macro-level dynamics. To overcome these li...
  </details>

- **2026-09-22** — Mauro Conti, Lorenzo Perinello, Umberto Salviati — [On the security and privacy of LLMs in Mobility](http://arxiv.org/abs/2609.26295v1)
  <details><summary>📄 Abstract</summary>
  The mobility sector is undergoing a paradigm shift driven by advances in Generative Artificial Intelligence. With a global market valued at approximately 2.9 trillion dollars annually, considering only cars, the integration of these technologies has the potential to impact more than 1.5 billion vehicles worldwide. As Large Language Models (LLMs) are increasingly adopted in mobility, concerns about cybersecurity, privacy, and reliability emerge. Accordingly, this paper surveys current application...
  </details>

- **2026-09-22** — Yan Zhang, Ruien Li, Yaoyao Peng et al. — [EADC: Evaluation of Advanced and Deep-level Compliance in Large Language Models](http://arxiv.org/abs/2609.26175v1)
  <details><summary>📄 Abstract</summary>
  Large Language Models (LLMs) have been used in various industries. However, ensuring their compliance with complex laws and regulatory frameworks remains a great challenge. Existing evaluation paradigms mainly rely on static benchmarks that suffer from three severe limitations: First, the compliance rules being used do not comply with the requirements of Artificial Intelligence (AI) laws and regulations; Second, they only handle apparent, explicit compliance risks, leaving implicit and covert co...
  </details>

- **2026-09-22** — Daniel Adu Worae, Spyridon Mastorakis, Nuno Moniz et al. — [Adaptive Traffic Camouflage: Causal and Resource-Aware Defense Against IoT Fingerprinting](http://arxiv.org/abs/2609.25787v1)
  <details><summary>📄 Abstract</summary>
  Encryption hides IoT payloads, but traffic shape can still reveal device identity through packet sizes, timing, direction, and packetization. We present Adaptive Traffic Camouflage, a causal, leakage-aware controller that characterizes traffic-shape leakage without runtime device labels and selects a budget-feasible transformation for the next traffic window from previous-window context. The controller chooses among padding, packet splitting, timing, and composite transformations, or leaves traf...
  </details>

- **2026-09-22** — Kyle MacMillan, Sanjay Krishnan — [Proof-of-Retention: A Framework for Auditable Cross-Organization Data Sharing](http://arxiv.org/abs/2609.26654v1)
  <details><summary>📄 Abstract</summary>
  The rapid adoption of AI across industries for (e.g.) fine-tuning and analytics has accelerated the need for high-quality data. To satisfy this demand, public and private entities will buy and sell data with other organizations. But such data sharing can and does violate privacy norms and laws. EU and American lawmakers have endeavored to control data sharing, restricting what data may be shared with whom, and under what circumstances. Unfortunately, accurately assessing compliance with new regu...
  </details>

- **2026-09-22** — Ziang Liu, Ruizhang Yang, Xin Cui et al. — [Privacy-Preserving Coordinated Operation of Power Grids and AI Data Centers: A Checkpoint-Aware Three-Phase Scheme](http://arxiv.org/abs/2609.26365v1)
  <details><summary>📄 Abstract</summary>
  The rapid growth of large language model training and serving is driving AI data centers (AIDCs) toward gigawatt scale. Unlike conventional commercial loads, AIDCs possess significant operational flexibility through dynamic voltage and frequency scaling (DVFS) of training and inference workloads, while periodic model checkpointing can induce abrupt power drops and rebounds that erode operating reserves and increase transmission congestion risks. Coordinating AIDC operation with grid scheduling u...
  </details>

- **2026-09-22** — Jiaming Tang, Chenlan Wang, Mingyan Liu et al. — [Decoding the Legalese: A Scalable and Quantitative Framework for Analyzing Corporate Privacy Policies](http://arxiv.org/abs/2609.26680v1)
  <details><summary>📄 Abstract</summary>
  Even though privacy policies are the primary mechanism organizations use to disclose how they collect, process, and share personal data, they are difficult for average users to interpret, perhaps by design, due to their verbosity and dense legal language. Importantly, there is a lack of standardized metrics that characterize key qualities of a privacy policy beyond regulatory requirements. Recent advances in large language models (LLMs) make it feasible to automatically structure and analyze the...
  </details>

- **2026-09-22** — Jiannan Wang, Xianghao Yu, Chenshu Wu — [A Gram-Attention Learning Framework for Spatially Non-Stationary Channel Estimation](http://arxiv.org/abs/2609.26437v1)
  <details><summary>📄 Abstract</summary>
  As next-generation wireless systems migrate to high-frequency bands, extremely large-scale multiple-input multiple-output (XL-MIMO) is indispensable for combating severe path loss. However, the received path energy along the extremely large array aperture (ELAA) may exhibit spatial non-stationarity, rendering the conventional discrete Fourier transform (DFT) codebook inadequate for channel estimation (CE) due to its full-array angular representation. To address this mismatch, we propose a novel ...
  </details>

- **2026-09-22** — Liheng Fan, Jialun Yin, Yuzhi Chen — [When Should Dependency Updates Invoke Repair Agents? A Lightweight Routing Study](http://arxiv.org/abs/2609.25911v1)
  <details><summary>📄 Abstract</summary>
  Dependency-update pull requests are frequent and mostly routine, but a small subset requires non-trivial compatibility repair. Recent repository-level coding agents make such repair increasingly plausible, yet invoking them on every dependency update wastes model calls, CI time, repository context, and review attention. We frame this as a pre-agent routing problem: deciding which dependency-update pull requests should be escalated before downstream diagnosis or repair attempts. We introduce DepF...
  </details>

- **2026-09-22** — Jeongmin Bae, Yongjae Kim, Kyoung Hur et al. — [AkasicMEM: Governed Enterprise Memory for Agents](http://arxiv.org/abs/2609.25563v1)
  <details><summary>📄 Abstract</summary>
  Agent memory enables enterprise agents to retain knowledge acquired during work and reuse it across tasks and agents, turning execution experience into persistent organizational knowledge. Realizing this potential requires both source--memory integration, through which enterprise sources and accumulated memory can be utilized together, and memory governance, through which shared memory remains subject to organizational policies throughout its lifecycle. These requirements interact when informati...
  </details>

- **2026-09-21** — Fatih Deniz, Yazan Boshmaf, Issa Khalil — [SSP-Bench: A Hybrid Data Generation Framework for Safety, Security, and Privacy Evaluation](http://arxiv.org/abs/2609.25352v1)
  <details><summary>📄 Abstract</summary>
  Evaluation of large language models (LLMs) for safety, security, and privacy (SSP) relies heavily on static benchmarks, which suffer from score saturation, data contamination, and aggregation artifacts, and fail to capture sensitivity to linguistic variation. As a result, models that perform well on fixed test sets often fail under semantically equivalent rephrasings. We introduce SSP-Bench, a dynamic benchmarking framework that generates evaluation instances on demand while preserving domain co...
  </details>

- **2026-09-21** — Jinyi Niu, Ziyi Song, Weining Shen — [Sex Estimation from Footwear Outsole Impressions Using CNN Transfer Learning and Interpretable Image Statistics](http://arxiv.org/abs/2609.25386v1)
  <details><summary>📄 Abstract</summary>
  Footwear outsole impressions are a common form of forensic pattern evidence, yet quantitative methods for estimating wearer attributes from these images remain relatively underdeveloped. We investigate binary sex estimation from footwear outsole impressions by comparing convolutional neural network (CNN) transfer learning with traditional feature-based classification. Using a publicly available outsole-impression dataset, we adopt a shoe-level training and test partition that keeps replicate sca...
  </details>

- **2026-09-21** — Ali Rezagholizadeh, Soheila Samiee — [Extending FunctionGemma for Practical On-Device Mobile Function Calling](http://arxiv.org/abs/2609.25373v1)
  <details><summary>📄 Abstract</summary>
  On-device assistants require function-calling models that map natural language to local system actions, but existing resources emphasize web APIs or narrow mobile-action catalogs. We extend FunctionGemma 270M-it to practical Android workflows by introducing MOBILEACTIONSEXTENDED, a synthetic, schema-validated dataset of ~9,500 conversations covering fifteen device-control categories, including messaging, phone calls, camera/screenshot, brightness control, device-status queries, flashlight contro...
  </details>

- **2026-09-21** — Hemn Khdr, Mohammad Noaeen, Karim Keshavjee et al. — [MedGate-Fusion: Integrating First-Encounter Semantic Narratives and Physiological Biomarkers for Prospective Stroke Risk Stratification](http://arxiv.org/abs/2609.25272v1)
  <details><summary>📄 Abstract</summary>
  Prospective stroke risk stratification in primary care is challenging because early risk signals are distributed across routine biomarkers and unstructured clinical narratives. We propose MedGate-Fusion, a multi-modal gated architecture that integrates transformer-based embeddings of first-encounter narratives with ten routinely recorded risk markers. We used electronic medical record data from the Canadian Primary Care Sentinel Surveillance Network (CPCSSN). Starting from 808,921 encounter-leve...
  </details>

- **2026-09-21** — He Hu, Yucheng Zhou, Qianning Wang et al. — [From Pattern Recognizers to Personalized Companions: A Survey of Large Language Models in Mental Health](http://arxiv.org/abs/2609.25186v1)
  <details><summary>📄 Abstract</summary>
  The rising global prevalence of mental health conditions, together with longstanding barriers in traditional healthcare, such as limited resources, high cost, stigma, and privacy concerns, has created an urgent need for accessible and scalable support. Large Language Models (LLMs) have emerged as a transformative technology with strong potential to democratize mental health support through advanced natural language understanding and generation. However, the rapidly expanding, fragmented body of ...
  </details>

- **2026-09-21** — Aman Priyanshu, Supriti Vijay, Brian Jabarian et al. — [Et Tu, Brute? Economic Misalignment in Personal AI Agents](http://arxiv.org/abs/2609.24927v1)
  <details><summary>📄 Abstract</summary>
  Personal AI agents make recommendations and take actions on people's behalf in high-stakes economic contexts, e.g., buying a flight, choosing health insurance, or selecting a graduate program. The agent is given access to the user's personal context, e.g., their email inbox and a structured profile of personal attributes, with the intention of making an optimal, personalized decision for the user. We show that by simply providing this personal context, the agent steers recommendations based on i...
  </details>

- **2026-09-21** — Mahdi Islam, Musarrat Tabassum — [Brain Metastases Segmentation for BraTS 2026 Task 1: A Multi-Architecture Comparison](http://arxiv.org/abs/2609.24769v1)
  <details><summary>📄 Abstract</summary>
  Brain metastases are the most common intracranial malignancy, occurring in roughly 30% of patients with primary solid tumors and carrying a median survival near 5.9 months. Automated segmentation is critical for treatment planning and volumetric monitoring, but metastases are frequently small, numerous, and heterogeneous in size within a single patient. We compare a plain nnU-Net baseline, a Residual Encoder Large (ResEncL) variant, region-based training, and a Primus transformer model for BraTS...
  </details>

- **2026-09-21** — Tomohiro Akazawa, Rui Tang, Hanzhi Tang et al. — [Ultralow-power, high-speed programmable Si photonic circuits with InGaAsP membrane](http://arxiv.org/abs/2609.24611v1)
  <details><summary>📄 Abstract</summary>
  Programmable photonic circuits have emerged as a promising platform for applications ranging from optical communications to artificial-intelligence computing and quantum information processing, but their scaling is fundamentally constrained by their essential building block, the optical phase shifter. Existing phase-shifter technologies face inherent trade-offs among power consumption, operating speed, modulation efficiency, optical loss, and thermal crosstalk, making it challenging to realize h...
  </details>

- **2026-09-21** — Anastasia Pustozerova, Eugene Bagdasarian, Luca Beurer-Kellner et al. — [Beyond Predictable Paths: Redefining AI Security Incident Reporting for Agents](http://arxiv.org/abs/2609.24515v1)
  <details><summary>📄 Abstract</summary>
  AI agents are being deployed rapidly, accompanied by a growing number of AI-specific attacks and corresponding incidents. As incident reporting becomes increasingly important for legal compliance, governance, accountability, and security; current frameworks must be adapted to the unique characteristics of AI agents. In this paper, two editorial authors compare AI systems and AI agents and, drawing on input from 23 experts in academia and industry, identify the information required for reporting ...
  </details>

- **2026-09-21** — Harshavardhan Abichandani, Penny Chong, Jiyuan Shen et al. — [EDGEGEN: Improving Tool-Calling Agents Beyond Happy Paths with Synthetic Edge Case Generation](http://arxiv.org/abs/2609.24115v1)
  <details><summary>📄 Abstract</summary>
  Tool-calling LLM agents are increasingly deployed in enterprise applications. However, effective evaluation and optimization require high-quality, diverse task datasets that are often difficult to obtain due to privacy and other constraints. Existing synthetic task generation methods often produce generic tasks that ignore an agent's underlying state or database and fail to reflect real-world usage diversity. We propose EdgeGen, a synthetic task generation framework that extracts compliance rule...
  </details>

- **2026-09-21** — Ramoni Adeogun — [Explanation-Guided Federated Deep Reinforcement Learning for Joint Resource Allocation and Scheduling in 6G in-X Subnetworks](http://arxiv.org/abs/2609.24102v1)
  <details><summary>📄 Abstract</summary>
  Sixth-generation (6G) wireless systems are envisioned as networks of networks, integrating diverse in-X subnetworks that provide localized, high-performance connectivity. Ensuring reliable communication in dense deployments, such as industrial robots and vehicles, is challenging due to dynamic interference and strict performance requirements. Traditional radio resource management (RRM) methods have limitations, prompting the need for AI-based solutions. In this paper, we address the challenges o...
  </details>


### 📂 steganography
*隐写与隐蔽通信 / Steganography & Covert Communication* — 2 papers

- **2026-09-21** — Sidong Guo, Sajani Vithana, Atefeh Gilani et al. — [Feedback Coding Enables Inference-Time Covert Agentic Communication](http://arxiv.org/abs/2609.24994v1)
  <details><summary>📄 Abstract</summary>
  As large language models (LLMs) are increasingly used to automate digital interactions, users can leverage LLM-generated text as cover for covert communication within seemingly benign conversations. Existing LLM steganography, however, is predominantly white-box, requiring the sender and receiver to share the cover statistics, typically through access to the model weights and prompt. Black-box schemes remove this requirement by allowing the receiver to operate solely on the generated text, but c...
  </details>

- **2026-09-21** — Xinrui Shi, Yanzhe Zhang, Diyi Yang — [Emergent Collusion in Long-Horizon LLM Agent Interaction](http://arxiv.org/abs/2609.24967v1)
  <details><summary>📄 Abstract</summary>
  LLM agents are increasingly deployed in collaborative settings, yet long-term interaction may give rise to undesirable coordination. We study the emergence of collusion in a long-horizon multi-agent environment: two agents repeatedly complete individual tasks, share task logs, verify each other's work, and receive rewards. We introduce realistic constraints that make compliance with the verification protocol incompatible with reward maximization, and find that agents increasingly deviate from th...
  </details>


### 📂 misuse
*滥用与误用 / Misuse & Abuse* — 12 papers

- **2026-09-23** — Xuwei Tan, Yao Ma, Xueru Zhang — [SR-Fraud: An Outcome-Supervised Reflective LLM Agent Framework for Non-Stationary Payment Fraud Detection](http://arxiv.org/abs/2609.27287v1)
  <details><summary>📄 Abstract</summary>
  Real-time payment fraud detection is a non-stationary streaming prediction problem: adversaries adapt before supervised labels mature, and localized burst attacks can cause losses before retraining. Production systems typically rely on tabular classifiers and rules, which can struggle to capture these emerging sequential patterns before periodic retraining occurs. We present SR-Fraud, an outcome-supervised reflective LLM framework that decouples request-time decisions from offline adaptation. A ...
  </details>

- **2026-09-23** — Jacob T. Emmerson, Phuong-Anh Nguyen-Le, Ronan Romano et al. — [An Open Pipeline and Dashboard for Systemic-Risk Evidence under the EU AI Act's Code of Practice](http://arxiv.org/abs/2609.28335v1)
  <details><summary>📄 Abstract</summary>
  Claims about AI safety reach audiences well beyond the AI community, yet many rely on opaque evidence or static assessments, when supporting evidence is accessible at all. We present the Systemic Risk Index, an open evaluation pipeline and dashboard built to make empirical evidence more transparent and traceable to the public. Our work organizes 19 public benchmarks into four systemic-risk categories defined by the EU GPAI Code of Practice---CBRN, cyber offense, harmful manipulation, and loss of...
  </details>

- **2026-09-23** — Junlin Liu, Yifeng Cai, Shuai Wang et al. — [GUIAuditor: Enabling Post-hoc Child Safety Forensics via Action-Guided GUI Provenance on Mobile Devices](http://arxiv.org/abs/2609.28205v1)
  <details><summary>📄 Abstract</summary>
  The proliferation of smart devices exposes children to online risks like grooming and financial scams that are deeply embedded within legitimate applications. Current approaches rely on automated prevention and detection, a paradigm that is fundamentally limited by its inherent fallibility. Whether rule-based or AI-driven, they inevitably produce false positives and negatives, failing to provide reliable protection. In this paper, we argue for a complementary, human-in-the-loop, post-hoc forensi...
  </details>

- **2026-09-23** — Walter Kurz — [Multi-Agent AI Architecture for Regulated Insurers: A generic AI framework under Solvency II and the AI Act in Austria and Germany](http://arxiv.org/abs/2609.27636v1)
  <details><summary>📄 Abstract</summary>
  This paper proposes a formal multi-agent architecture for implementing enterprise AI in regulated insurance firms, integrating economic theory with institutional design. The framework synthesises three core theoretical perspectives: Arrow's risk pooling theory to formalise risk transformation under uncertainty, Nash equilibrium to model strategic interactions between decision agents, and Principal-Agent theory to address incentive alignment under information asymmetry. The insurer is modelled as...
  </details>

- **2026-09-23** — Maddalena Ghiotti, Daniela Paolotti, Yelena Mejova — [Watching What We Eat: Information Quality and Body Image in Diet-Related YouTube Videos](http://arxiv.org/abs/2609.28114v1)
  <details><summary>📄 Abstract</summary>
  The widespread use of social media, particularly image- and video-based platforms, has turned them into key sources of both normative and informational content related to health and diet. This may contribute to the development of disordered eating behaviors or, potentially, eating disorders. This study uses mixed-methods analysis applied to 3129 YouTube videos about diet and weight loss in order to quantify the level of risk of low-quality information and heightened focus on the body image. We a...
  </details>

- **2026-09-23** — Jose Manuel de la Chica Rodriguez, Juan Manuel Vera Diaz, Pablo Delgado Romero — [Compliant with Local Controls, Collectively Discriminatory. A Governance Architecture for Multi-Agent AI in Regulated Finance](http://arxiv.org/abs/2609.27994v1)
  <details><summary>📄 Abstract</summary>
  Financial institutions are beginning to deploy agentic workflows in credit, fraud, collections, compliance, and operational control. Governance remains largely component-centric: each model or agent is specified, tested, authorized, and monitored locally. That is insufficient when institutional risk arises from the joint behavior of many locally acceptable components. We call this gap constitutional non-compositionality: local compliance checks need not compose into acceptable collective outcome...
  </details>

- **2026-09-23** — Truong Thanh Hung Nguyen, Vo Thanh Khang Nguyen, Hoang-Loc Cao et al. — [Self-Evolving Multimedia Verification through Memory Consolidation of Contestation Experiences](http://arxiv.org/abs/2609.27175v1)
  <details><summary>📄 Abstract</summary>
  Multimedia verification requires not only accurate decisions but also traceable evidence, reliable human correction, and safe reuse of prior experience. Existing systems often lack explicit mechanisms for revising intermediate reasoning or preventing harmful knowledge transfer. We present SEMV (Self-Evolving Multimedia Verification), a self-evolving multi-agent framework that treats provenance-bearing arguments as the interface between evidence, reasoning, human contestation, and memory. SEMV co...
  </details>

- **2026-09-22** — Baptiste Bonin, Caro Strickland, Audrey Durand — [On Preference Coverage Collapse from Hindsight Relabeling in Multi-Objective Reinforcement Learning](http://arxiv.org/abs/2609.26918v1)
  <details><summary>📄 Abstract</summary>
  Hindsight relabeling which retroactively replacing a transition's goal with the outcome the agent actually achieved is an effective tool for improving sample-efficiency in Reinforcement Learning (RL). A natural extension to preference-conditioned multi-objective RL (MORL) relabels transitions with the preference direction the agent achieved rather than the one asked for. We show that this extension is frequently harmful: across four preference-conditioned off-policy algorithms spanning two criti...
  </details>

- **2026-09-22** — Alexandros Fourtounis, Emmanouil Papadogiannakis, Panagiotis Papadopoulos et al. — [COBRA: A Content-Agnostic Framework for Zero-Day Detection of Suspicious Domains](http://arxiv.org/abs/2609.25882v1)
  <details><summary>📄 Abstract</summary>
  The use of malicious domains is central to cyberattacks such as phishing, malware distribution, impersonation, and fraudulent transactions. Because domains are inexpensive to register and easy to deploy at scale, they remain one of the most common and damaging tools used in cybercrime across industries. Proactive detection is essential to reducing this window of vulnerability and preventing harm to users. In this work, we propose COBRA: a content-agnostic, registration-time detection framework f...
  </details>

- **2026-09-22** — Peachapong Poolpol, Henrik H. J. Detjen, Eike Petersen — [Faithful Faithfulness Evaluations: Challenges & Pitfalls Learned from a Breast MRI Case Study](http://arxiv.org/abs/2609.25978v1)
  <details><summary>📄 Abstract</summary>
  Saliency maps are widely used to explain deep learning predictions in medical imaging, yet visually plausible explanations do not necessarily reflect a model's true decision process and may therefore mislead clinicians. We investigate this problem using a Vision Transformer-based breast MRI classifier trained on the ODELIA Breast MRI Challenge dataset and evaluate multiple saliency methods, including Last-layer Attention, Attention Rollout, Grad-SAM, Gradient Attention Rollout, GMAR, Grad-CAM, a...
  </details>

- **2026-09-21** — Andrew Anogie Uduimoh, Hadiza Umar Yusuf, Oluwafemi Osho — [Context-Aware Pre-Deployment Evaluation of AI Systems: A Regulatory Framework for Nigerian Fintech](http://arxiv.org/abs/2609.24016v1)
  <details><summary>📄 Abstract</summary>
  Commercial large language models are increasingly deployed across African fintech infrastructure for fraud detection and customer communication, yet no Nigerian or African continental regulatory instrument specifies what pre-deployment evaluation such systems must undergo before procurement. This paper reviews African fintech AI governance across global, continental, and Nigerian instruments, and shows that safety is affirmed as a principle while pre-deployment evaluation is operationally unspec...
  </details>

- **2026-09-21** — Simiao Ren, Kidus Zewde, Xingyu Shen et al. — [Open-Jev Judgments on CallScreenBench: Calibrated One-Pass Scam Screening with a Small Language Model](http://arxiv.org/abs/2609.23959v1)
  <details><summary>📄 Abstract</summary>
  Screening a phone call for fraud needs a trustworthy probability after every caller turn, in milliseconds. Jev-style typed decisions promise exactly that: declared options go in, one calibrated probability per option comes out of a single forward pass, with no generated text. We test an open implementation of this readout, JevLite, on scam-call screening: Qwen3-4B is LoRA-tuned so that the temperature-scaled softmax over two answer-label logits is P(scam). On 41 held-out CallScreenBench scenario...
  </details>


### 📂 red-teaming
*红队测试 / Red Teaming* — 1 papers

- **2026-09-23** — Dongdong Zhang, Tengchao Lv, Yilin Jia et al. — [CART: Closed-Loop Adaptive Red Teaming for Large Language Models](http://arxiv.org/abs/2609.27336v1)
  <details><summary>📄 Abstract</summary>
  Automated red teaming often replays a fixed set of prompts, which measures known risks but cannot learn from failures found during testing. We present CART (Closed-Loop Adaptive Red Teaming), a framework that uses each result to guide what it tests next. CART begins with broad risk coverage, follows weaknesses that emerge, keeps new probes diverse, and records the evidence and source of every finding. It separates the Challenger that creates tests, the Target being tested, which may be a text-on...
  </details>


### 📂 vulnerability
*漏洞与攻击面 / Vulnerabilities & Attack Surfaces* — 47 papers

- **2026-09-23** — Davood Wadi, Yu Ma — [Shopping by algorithm: How agentic AI deploys human heuristics as a surrogate consumer](http://arxiv.org/abs/2609.28372v1)
  <details><summary>📄 Abstract</summary>
  Consumers increasingly delegate purchasing decisions to Large Language Models (LLMs) acting as surrogate consumers. Using "Tool-Lab," an adaptation of information-board process tracing that places product attributes behind costly tool calls, we examine how marketing pricing cues (i.e., just-below pricing and promotional framing) influence AI shopping agents. Across eight commercially deployed LLMs from three providers, we trace pre-choice information acquisition. Under zero cost, pricing cues ra...
  </details>

- **2026-09-23** — Zerui Li, Sihao Lin, Yanyan Shao et al. — [Talk2Escape: Conversational Grounding for Vision-and-Language Navigation](http://arxiv.org/abs/2609.28296v1)
  <details><summary>📄 Abstract</summary>
  While Vision-and-Language Navigation (VLN) has demonstrated remarkable success, the prevailing single-turn paradigm exposes a fundamental vulnerability: agents operate in a strictly open-loop manner. In practice, factors such as perceptual aliasing, sensor noise, and odometry drift can cause minor deviations to accumulate over time, often leading to catastrophic mission failures with no built-in mechanism for error recovery. To address this, we introduce \textit{Talk2Escape}, a proactive and mod...
  </details>

- **2026-09-23** — Sai Varun Kodathala, Prashanth Pollishetty, Jaylen Cargill — [Prompt, Probe, Train, or Annotate? Single-camera sports video understanding in amateur settings](http://arxiv.org/abs/2609.28049v1)
  <details><summary>📄 Abstract</summary>
  Video understanding is usually benchmarked on curated, single-actor, or professionally filmed clips, and a strong score there is routinely read as evidence a model is robust enough for deployment. Amateur team sport is a useful, largely untested place to check that assumption: over eight million students played a school sport in the United States in 2024-25 alone, almost none of it filmed by more than a single fixed camera, with several candidate actors crowded into frame and no operator or seco...
  </details>

- **2026-09-23** — Adithyan Arun Kumar — [Agent Name Collision Attacks in Multi-Agent Systems](http://arxiv.org/abs/2609.27624v1)
  <details><summary>📄 Abstract</summary>
  Multi-agent hosts turn remote Agent Cards into local agents, tools, workflow targets, and broker routes. A2A defines the card's name as human-readable metadata, not as a stable identity, and specifies no collision semantics. The security failure begins when a host nevertheless uses that remote name as a local routing identifier. We traced registration through dispatch and ran isolated regression tests at seven pinned open-source revisions. Six client-style integrations selected an attacker-contr...
  </details>

- **2026-09-23** — Ke Wan, Chen Chen — [Attention Routing Stabilizes Early: Working-Set Inference for Recurrent Language Models](http://arxiv.org/abs/2609.27373v1)
  <details><summary>📄 Abstract</summary>
  Recurrent language models repeatedly apply shared network blocks to refine latent representations, but standard inference recomputes global attention at every recurrent step. We study attention dynamics across recurrent depth and find that attention support and distributions stabilize substantially earlier than hidden states and attention outputs. This suggests a two-stage structure: early steps discover a sparse working set of relevant context, while later steps refine representations over larg...
  </details>

- **2026-09-23** — Walter Nedov, Saimunur Rahman, Kavindie Katuwandeniya et al. — [Geometry-Conditioned Visual Place Recognition in Natural Environments](http://arxiv.org/abs/2609.27370v1)
  <details><summary>📄 Abstract</summary>
  Visual Place Recognition (VPR) in natural environments remains challenging due to repetitive vegetation, sparse distinctive landmarks, and substantial appearance and viewpoint variation across traversals. While visual observations of the same place can change considerably, their underlying spatial structure is often more persistent. We exploit this complementary geometric consistency through Depth-Aware Distillation (DAD), which conditions the token representations of a pretrained Vision Foundat...
  </details>

- **2026-09-23** — Chengxi Zhong, Yongzhe Chang — [Anchor and Perturb: Lazy Agent Remediation by Exploration Injection](http://arxiv.org/abs/2609.27365v1)
  <details><summary>📄 Abstract</summary>
  Anchor and Perturb (AnP) is a lightweight framework that resolves multi-agent coordination failures by decoupling exploratory variance injection from recurrent manifold stability. Existing remediation strategies predominantly alter mixing network architectures or enforce simultaneous exploration across the collective, which inevitably precipitates severe temporal-difference penalties in non-monotonic reward spaces. Specifically, AnP isolates underperforming lazy agents and injects an asymmetric ...
  </details>

- **2026-09-23** — Akash Pandey, Kanisha Shah, Addrish Roy et al. — [A Systematic Benchmark of Explainable Methods for Temporal Attribution in Sequential Recommendation Systems](http://arxiv.org/abs/2609.27201v1)
  <details><summary>📄 Abstract</summary>
  Sequential RecSys are central to modern personalization, exploiting user's historical interaction sequences to drive next-step decisions. Deep learning models, particularly CNN and Transformer-based architectures, have proven highly effective at capturing temporal dependencies in these histories. For transparency and trust, understanding which past interactions drive a given recommendation is increasingly important --- both for developers auditing model behavior and for users seeking a rationale...
  </details>

- **2026-09-23** — Minqiu Sun, Xin Huang, Luanzheng Guo et al. — [ZOCheck: CPU-Shadow Checkpointing for Zeroth-Order LLM Fine-Tuning](http://arxiv.org/abs/2609.27189v1)
  <details><summary>📄 Abstract</summary>
  Zeroth-order (ZO) optimization is an attractive option for memory-efficient LLM fine-tuning, but its fault tolerance remains underexplored. Unlike first-order training, ZO progress can be represented by lightweight seed-and-scalar step logs, yet naive log-only recovery still incurs replay cost that grows with training progress, and shortcut replay does not preserve the executed floating-point trajectory. We present ZOCheck, a fault-tolerant ZO training system that exploits this replayable struct...
  </details>

- **2026-09-23** — Pengcheng Liao, Quntao Zhuang — [Sample-Efficient Tomography of a Class of Mixed States with Extensive Entanglement and Magic](http://arxiv.org/abs/2609.27177v1)
  <details><summary>📄 Abstract</summary>
  Full tomography of a generic many-qubit quantum state requires exponentially many copies, while suitable structural constraints can make reconstruction sample-efficient. Existing approaches exploit, for example, limited entanglement structure, low magic, or constrained state-preparation circuits. Here we consider a class of mixed states that can simultaneously exhibit extensive entanglement and extensive magic. Specifically, we introduce Clifford-encoded block-product (CEBP) states, obtained by ...
  </details>

- **2026-09-22** — Yu-Wei Fan, SooHyuk Cho, Aarti Gupta et al. — [Agentic-IC3: Enabling Semantic Proof Search in IC3 Model Checking](http://arxiv.org/abs/2609.27162v1)
  <details><summary>📄 Abstract</summary>
  IC3 is a state-of-the-art algorithm for hardware model checking that proves safety properties by incrementally constructing an inductive invariant consisting of a set of lemmas. Its effectiveness depends on generalization heuristics that identify useful lemmas and guide proof search. However, many leading IC3 hardware model checkers operate on lowered, bit-level representations, where high-level design relationships are difficult to exploit for generalization. Those operating at a higher level r...
  </details>

- **2026-09-22** — Djamel Eddine Hakim Ghorab, Farid Mokhati, Mostafa Anouar Ghorab — [Solidity Meets LLMs: A Transformer-Based Approach to Smart Contract Vulnerability Detection](http://arxiv.org/abs/2609.27091v1)
  <details><summary>📄 Abstract</summary>
  The growing adoption of blockchain technologies, particularly the Ethereum platform, has amplified the critical role of smart contracts in decentralized applications. However, the increasing complexity and financial value of these contracts make them prime targets for cyber attacks. In this work, we present a transformer-based approach for the detection of vulnerabilities in smart contract fragments written in Solidity. Leveraging the representational power of pre-trained Large Language Models (...
  </details>

- **2026-09-22** — Majumder Haider, Imtiaz Ahmed, Zoheb Hassan et al. — [Digital Twin Enhanced Channel Twin for AI-Native CSI Inference: Generalizability and Scalability](http://arxiv.org/abs/2609.27017v1)
  <details><summary>📄 Abstract</summary>
  Accurate channel state information (CSI) is critical for advanced multi-antenna wireless networks. While high-fidelity and site-specific ray-tracing (RT) equipped wireless digital twins can overcome overhead for CSI acquisition. However, computing deterministic, calibrated RT based CSI from a wireless digital twin for every orthogonal frequency-division multiplexing (OFDM) symbol violates the strict microsecond latency budgets of the 5G NR numerology. To overcome this computational bottleneck, t...
  </details>

- **2026-09-22** — Yanshuo Bai, Kanji Tanaka — [TM-APR: Thermal Temporal-Memory Localization via Analytic Online Adaptation](http://arxiv.org/abs/2609.26766v1)
  <details><summary>📄 Abstract</summary>
  Thermal Visual Place Recognition (Thermal VPR) maps camera observations to metric poses within a mapped environment, serving as a prerequisite for autonomous navigation. However, thermal VPR suffers from severe environmental dependence, heavy online retraining overheads, and an inability to model dynamic non-linear shifts, causing existing frameworks to fail during online deployment. To achieve robust domain-invariant place recognition, we bridge Analytic Class-Incremental Learning (ACIL) with d...
  </details>

- **2026-09-22** — Om Nepal, Sushant Aryal, Oluseyi Olukola et al. — [Metrics Failure in LLM-Based Code Vulnerability Repair: An Empirical Study and a Change-Aware Screen](http://arxiv.org/abs/2609.26749v1)
  <details><summary>📄 Abstract</summary>
  Large language models (LLMs) are increasingly applied to the automated repair of C/C++ security vulnerabilities, and compile rate is a commonly reported proxy for progress: whether the generated patch compiles. We argue that compile rate is a scientifically unreliable metric for single-function vulnerability repair, and we support this with five controlled experiments over 203 vulnerable functions from Big-Vul, three open-source code LLMs (350M to 6.7B parameters), and three prompting strategies...
  </details>

- **2026-09-22** — Yuxin Bao, Hongwei Ruan, Luobin Wang et al. — [NavSafe-$\infty$: Benchmarking Closed-Loop Driving Safety in Photorealistic Environments](http://arxiv.org/abs/2609.26618v1)
  <details><summary>📄 Abstract</summary>
  End-to-end (E2E) driving policies have progressed rapidly on open-loop (OL) benchmarks, yet OL evaluation cannot reveal whether a policy withstands compounding errors, recovers from failures, or interacts safely with surrounding actors. We introduce NavSafe-$\infty$, a photorealistic closed-loop (CL) benchmark of 280 scenarios spanning 28 event types, each with success and failure criteria defined within a structured traffic-safety taxonomy, which yields category-level capability scores for Traf...
  </details>

- **2026-09-22** — Arthur Cordeiro, Alberto Maria Mongardini, Emmanouil Vasilomanolakis — [Rouxii: Exploiting Honeypots with Deception-Aware AI Pentesters](http://arxiv.org/abs/2609.26555v1)
  <details><summary>📄 Abstract</summary>
  Honeypots are designed to deceive attackers, and recent work shows they can also derail autonomous LLM-based pentesters. These evaluations, however, largely consider attackers unaware of the deception they face. We study the opposite setting: an autonomous attacker explicitly equipped to recognize and act on honeypot fingerprints. We introduce Rouxii, an AI-driven penetration-testing framework that integrates counter-deception into reconnaissance and pivots from honeypot detection to exploitatio...
  </details>

- **2026-09-22** — Xin Shen, San-Zhuo Xi, Yali Du et al. — [On the Lexical Superstition of Large Language Models for Code Comprehension: Re-evaluation on Code of Low Lexical Quality](http://arxiv.org/abs/2609.26388v1)
  <details><summary>📄 Abstract</summary>
  Recent advances in large language models (LLMs) have made them widely used for code-related tasks. Identifier names are statistically informative in naturally occurring code, but their information is not always reliable. We investigate whether current LLMs assign disproportionate weight to lexical cues when renaming preserves program structure. We introduce Face/Off, a semantics-preserving identifier-renaming framework, and evaluate progressive naming conditions across multiple models and code-c...
  </details>

- **2026-09-22** — Vansh Wahi — [Optimizing the Score, Losing Sight of the Task: Reward Hacking Across Weights, Selection, and Prompts](http://arxiv.org/abs/2609.25848v1)
  <details><summary>📄 Abstract</summary>
  A higher evaluation score does not always mean a better language model system. When optimization exploits an evaluator's mistakes, measured progress can conceal unchanged or deteriorating task performance. This failure can arise through parameter updates, selection among generated outputs, or revisions to persistent prompts. We develop a comparative framework for reward hacking across these three optimization substrates: weights, selection, and text. Building on the Proxy Compression Hypothesis ...
  </details>

- **2026-09-22** — Aleksandr V. Petrov, Nathan Stein, Erik Lybecker et al. — [Robust Fusion of Semantic and Behavioural Signals for LLM Reranking in Personalised Search](http://arxiv.org/abs/2609.25825v1)
  <details><summary>📄 Abstract</summary>
  Personalised search must satisfy query intent while incorporating user context and historical interactions. LLM-based cross-encoders provide a single reranking interface, but injecting predictive behavioural statistics into their prompts can encourage shortcut learning: reliance on historical signals at the expense of semantic and user-context patterns that generalise to sparse or unseen searches.   We study this problem in the personalised search system of a large-scale audio streaming platform...
  </details>

- **2026-09-22** — Yuanteng Chen, Qiwei Lai, Chen Tianqi et al. — [You Only Need 2/3 of the Chosen Experts: An Empirical Study of Dynamic Expert Pruning in Fine-Grained MoE LLMs](http://arxiv.org/abs/2609.25809v1)
  <details><summary>📄 Abstract</summary>
  Fine-grained mixture-of-experts (MoE) architectures have become a mainstream design for open-weight LLMs, with hundreds of experts and increasingly many selected per token. This shift makes dynamic expert pruning an attractive route to cheaper inference. Yet existing evidence comes largely from coarser architectures and likelihood-scored multiple-choice benchmarks, leaving three central questions open in the fine-grained regime: how redundant per-token expert selection is, how effectively existi...
  </details>

- **2026-09-22** — Jongjin Baek, Won Ji, Seungjae Yoo et al. — [Hot-Cold Tiering of HBM and High Bandwidth Flash for Agentic LLM Serving](http://arxiv.org/abs/2609.25782v1)
  <details><summary>📄 Abstract</summary>
  Large language model (LLM) serving is increasingly agentic, with multi-turn sessions that idle between actions yet must retain their full context. Limited GPU memory capacity forces inactive KV states to be evicted, so resuming a session incurs either costly recomputation or slow interconnect transfers. To address this, high bandwidth flash (HBF)-an on-package 3D-NAND memory offering orders-of-magnitude greater capacity than high bandwidth memory (HBM) at comparable read bandwidth-has emerged as...
  </details>

- **2026-09-22** — Zheng Chen, Yuzhu Li, Haoxuan Li et al. — [TCMaster: Confidence-Aware Querying and Workload-Guided Physical Design for Multi-Source Traditional Chinese Medicine Knowledge Graphs](http://arxiv.org/abs/2609.25712v1)
  <details><summary>📄 Abstract</summary>
  Multi-source knowledge graphs (KGs) need query mechanisms that expose reliability and exploit domain structure. This paper presents TCMaster, a property-graph query substrate for confidence-aware traversal and workload-guided physical design over Traditional Chinese Medicine KGs. TCMaster integrates pharmacopoeias, prescriptions, molecular databases, and LLM-extracted micro-semantics into a KG with approximately 221K entities and 723K base edges. It annotates edges with provenance-level confiden...
  </details>

- **2026-09-22** — Maria Damanaki, Nikos Piperigkos, Alexandros Gkillas et al. — [CDKF-Track: Cluster-aware Data-Driven Kalman Filtering for Cooperative 3D Multi-Object Tracking](http://arxiv.org/abs/2609.25668v1)
  <details><summary>📄 Abstract</summary>
  Multi-Object Tracking (MOT) is essential for EdgeAI perception systems, where accurate object localization and reliable identification enable safe decision-making. Singleagent MOT suffers from occlusions, sensor noise, and partial scene understanding in complex real-world scenarios. While multi-agent systems improve robustness by exploiting shared information, they introduce redundant measurements that lead to false data associations, and still struggle to capture nonlinear object dynamics. To a...
  </details>

- **2026-09-22** — Junyoung Jang, Gwanhyun Lee, Hwiwon Lee et al. — [Evaluating Coding Agents on Kernel Exploit Generation](http://arxiv.org/abs/2609.25591v1)
  <details><summary>📄 Abstract</summary>
  Coding agents now find real vulnerabilities in production software. However, bug discovery results do not measure whether agents can construct exploit primitives. We introduce KEX-bench, a benchmark for evaluating coding agents on exploit primitive generation against real operating-system kernels. KEX-bench contains 45 task instances across 40 Linux and Windows CVEs, covering kernel address leak, instruction-pointer control, heap read, heap write, and arbitrary address write. Each task runs in a...
  </details>

- **2026-09-22** — Dahlia Shehata, Ming Li — [Recovering Agentic Sovereignty: Mitigating the Consensus Paradox via Contrastive Epistemic Decoding](http://arxiv.org/abs/2609.25570v1)
  <details><summary>📄 Abstract</summary>
  Large language models (LLMs) exhibit a parametric vulnerability to adversarial swarm consensus. To mitigate this sycophancy, we introduce Contrastive Epistemic Decoding (CED), a zero-shot inference intervention. Unlike standard Contrastive Decoding (CD) which relies on a weaker secondary model, CED utilizes a dual forward-pass on a single architecture to isolate conformity bias. By introducing a novel asymmetric, zero-bounded probability clamp and discrete top-k truncation mask, CED mathematical...
  </details>

- **2026-09-21** — Jianzhe Lin, Xiaolin Li, Fei Wang et al. — [Clarification Is Not Correction: LLMs Fail to Let Go](http://arxiv.org/abs/2609.25337v1)
  <details><summary>📄 Abstract</summary>
  Dialogue failures in language models are usually framed as memory failures: context too long, summaries lossy, a constraint forgotten. We argue this misses a deeper problem: in many conversations the model does not forget, it commits too early. An ambiguous early turn collapses into a single hidden interpretation, and later clarification is filtered through that commitment. We call this early posterior collapse: unresolved user intent collapsing into a committed task state before ambiguity is re...
  </details>

- **2026-09-21** — Qixin Zhang, Ajay Kumar, Zhi-Li Zhang — [Multi-Agent Video Prediction: Self-Correcting Conditional Frames for Dynamic Scene Forecasting](http://arxiv.org/abs/2609.25302v1)
  <details><summary>📄 Abstract</summary>
  Transmission latency significantly degrades user quality of experience in real-time interactive perception systems. In remote driving, maintaining reliable visual feedback is critical for safe operation under dynamic network variability. Although video prediction offers a promising approach to compensate for short-term transmission delays and approximate near-zero-latency streaming, prediction-only methods remain vulnerable in highly dynamic scenes, especially when newly emerged objects appear d...
  </details>

- **2026-09-21** — Jianhui Zhang, Ahmed Salem, Robert Tidswell et al. — [Silk-templated Nanostrips as Superprotonic Fibre Sensors](http://arxiv.org/abs/2609.25293v1)
  <details><summary>📄 Abstract</summary>
  Transforming textile fibres into sensors can facilitate continuous physiological monitoring for improving human healthcare. Coating fibres with electronic conductors can help detect physiological stimuli but their sensitivity scales with thickness and often lowers the fibre mechanical flexibility. Proton conductors are potential alternatives; however, they suffer from fragile physical interfaces, and sluggish kinetics. Here, we report a bio-templated, scalable strategy to create superprotonic in...
  </details>

- **2026-09-21** — Ariel Flint, Luca Maria Aiello, Sara M. Constantino et al. — [Indirect tipping: a social attack surface in AI agent populations](http://arxiv.org/abs/2609.25194v1)
  <details><summary>📄 Abstract</summary>
  As generative AI agents are deployed at scale, safety will depend not only on technical safeguards and individual model design, but also on collective equilibria that determine how agent populations process information, prioritize actions, and respond to uncertainty. Yet the same equilibria that enable agents to coordinate also create a social attack surface. The standard framework to assess this vulnerability is critical mass dynamics: the minimum fraction of adversarial agents required to over...
  </details>

- **2026-09-21** — Yifan Hu, Xilin Dai, Zhiyuan Qu et al. — [When Tomorrow Becomes Today: Self-Evolving Policies for Agentic Time-Series Forecasting](http://arxiv.org/abs/2609.24862v1)
  <details><summary>📄 Abstract</summary>
  Agentic time series forecasting concerns systems whose underlying mechanisms evolve, making the relative effectiveness of numerical models, reasoning strategies, and intervention rules inherently time-varying. Consequently, a time series agent must adapt the forecasts it produces and the orchestration policy that determines which components to trust and how to coordinate them. The deployment process naturally provides supervision for this adaptation as forecast horizons elapse and realized targe...
  </details>

- **2026-09-21** — Aoxiang Fan, Corentin Dumery, Nicolas Talabot et al. — [Revisiting Multi-View Stereo: A Sequence-to-Sequence Formulation](http://arxiv.org/abs/2609.24850v1)
  <details><summary>📄 Abstract</summary>
  Computing accurate geometry from multi-view images is a fundamental problem in computer vision. Recent feed-forward (FF) models jointly estimate 3D geometry and camera parameters, but they typically suffer from geometry distortion caused by reconstruction ambiguity, even when ground-truth camera parameters are supplied. In this paper, we study the multi-view stereo (MVS) problem with known camera parameters and propose a novel approach that bridges conventional MVS and FF methods. Rather than ca...
  </details>

- **2026-09-21** — Noga Kertes, Daphna Link Sourani, Alex M. Bronstein et al. — [GraphSVR: q-Space--Aware Graph-Based Slice-to-Volume Registration for Diffusion MRI](http://arxiv.org/abs/2609.24732v1)
  <details><summary>📄 Abstract</summary>
  Diffusion-weighted imaging (DWI) remains highly vulnerable to subject motion, particularly in time-efficient protocols and in motion-prone populations. While slice-to-volume registration (SVR) can mitigate inter-slice and inter-stack misalignment, diffusion MRI introduces additional complexity due to diffusion-direction-dependent contrast and the requirement to align dozens of measurements within a common reference frame, effectively yielding a 4D registration problem. Existing approaches rely p...
  </details>

- **2026-09-21** — Jiling Zhou, Aisvarya Adeseye, Antti Hakkala et al. — [Reasoning Topology Matters: A Controlled Study of LLM-Based Cybersecurity Analysis](http://arxiv.org/abs/2609.24710v1)
  <details><summary>📄 Abstract</summary>
  Large Language Models (LLMs) are increasingly used in cybersecurity, where accurate analysis often requires multi-step and context-dependent reasoning over complex and heterogeneous data. However, existing prompting approaches typically focus on eliciting reasoning without explicitly considering how intermediate reasoning steps are structurally organized. We introduce Security Reasoning Topology, which models reasoning through three representative structures: Linear, Branching, and Graph. To eva...
  </details>

- **2026-09-21** — Joseph Rigal, Emmanuel Virot, Caroline Pascal — [Learning tactile perception from high-bandwidth single-point sensing](http://arxiv.org/abs/2609.24621v1)
  <details><summary>📄 Abstract</summary>
  Tactile sensing is increasingly being incorporated into learning-based robotic manipulation, yet many existing approaches rely on spatially distributed sensors. Here we introduce SpectRobot, a framework that transforms single-point tactile signals into compact time-frequency spectrograms. These spectrograms encode high-bandwidth tactile histories as fixed-size image-like representations. They can be processed by standard vision encoders and integrated into learning pipelines originally developed...
  </details>

- **2026-09-21** — Wai Kin Wong, Dongwei Xiao, Anthony Cheuk Tung Lai et al. — [State-Aware Fuzzing of JavaScript Engines with LLM-Guided Instrumentation](http://arxiv.org/abs/2609.24550v1)
  <details><summary>📄 Abstract</summary>
  The security of the modern web depends on the correctness of JavaScript (JS) engines, yet these complex systems remain vulnerable to high-impact bugs. A critical limitation of state-of-the-art fuzzers is the coverage plateau: once a fuzzer saturates the control-flow graph, edge coverage loses its ability to guide discovery. Because complex engine behaviors, such as JIT optimization tiers and hidden class transitions, often share identical edge coverage, standard coverage metrics are blind to the...
  </details>

- **2026-09-21** — Boris Günther, Ludger Overbeck — [Affine Volterra covariance processes and application to commodity markets](http://arxiv.org/abs/2609.24548v1)
  <details><summary>📄 Abstract</summary>
  We study affine stochastic Volterra equations on the cone of symmetric positive semidefinite matrices. For scalar kernels acting entrywise on the matrix dynamics, we establish weak existence by exploiting stochastic invariance results for Volterra equations on convex domains and derive a conditional Fourier--Laplace transform formula characterized by matrix-valued Riccati--Volterra equations. As an application, we extend the Gibson--Schwartz commodity model by replacing its variance-covariance s...
  </details>

- **2026-09-21** — Hyunjoong Cho, Jinhyeok Jang — [Not All Task Vectors Need Equal Rank: Energy-Proportional Allocation for Model Merging](http://arxiv.org/abs/2609.24517v1)
  <details><summary>📄 Abstract</summary>
  Model merging aims to combine multiple fine-tuned models derived from a common pretrained model into a single multi-task model without additional joint training. Recent spectral merging methods improve over simple weight averaging by exploiting low-rank structures of task-specific updates, but they commonly assign the same rank capacity to every task. This uniform allocation ignores that task vectors can have heterogeneous spectral complexity, causing the shared merging space to be used suboptim...
  </details>

- **2026-09-21** — Andro Erdelez, Pascal Mettes, Behzad Bozorgtabar — [Hierarchical Prompt Learning for Hyperbolic Vision-Language Models](http://arxiv.org/abs/2609.24276v1)
  <details><summary>📄 Abstract</summary>
  Hyperbolic vision-language models (VLMs) represent image and text features in a geometry naturally suited to hierarchy, but their adaptation to downstream tasks has largely relied on fixed prompts. Existing prompt learning methods, meanwhile, treat class labels as a flat set and do not exploit available taxonomic structure. We address this gap with a hierarchical prompt learning plug-in for frozen hyperbolic VLMs. Given a fixed offline parent-class hierarchy, it augments a class prompt learner w...
  </details>

- **2026-09-21** — Uday Allu, Abhivanth Sivaprakash, Pratik Singh et al. — [Document Retrieval-Aware Chunking (D-RAC): Universal Retrieval-Aware Ingestion of Enterprise Documents via PDF Normalization and Multimodal Markdown Conversion](http://arxiv.org/abs/2609.24220v1)
  <details><summary>📄 Abstract</summary>
  Retrieval-Augmented Generation (RAG) systems over enterprise knowledge bases must ingest heterogeneous document formats -- PDFs, Word documents, presentations, and scans -- whose content is locked inside complex visual layouts, multi-column pages, and dense tables. Rule-based extraction and OCR destroy reading order, flatten tables, and lose heading hierarchy, while fully agentic chunking over extracted text incurs high token costs and hallucination risk. We present Document Retrieval-Aware Chun...
  </details>

- **2026-09-21** — Akihisha Fujiyama, Niwase Shamim — [Forgeable Confirmation in Automated Computer Security Testing: Deterministic Rules versus AI Judges](http://arxiv.org/abs/2609.24200v1)
  <details><summary>📄 Abstract</summary>
  AI is increasingly used to automate computer security testing, and the tools must decide for themselves whether an attack succeeded. A finding that a deterministic rule confirms by observation is reported as fact, whereas one that an LLM judges exploitable is treated as an opinion. We ask whether the system under test can forge that confirmation. In offline security testing of a four-stage AI-assisted pipeline, nine of its fifteen confirmation mechanisms are forgeable, and forgeability is predic...
  </details>

- **2026-09-21** — Byeongho Yu, Junhyuk So, Eunhyeok Park — [LoopCD: Loop-wise Contrastive Decoding for Improving Reasoning in Looped Language Models](http://arxiv.org/abs/2609.24196v1)
  <details><summary>📄 Abstract</summary>
  Looped Language Models (LoopLMs) perform "latent reasoning" by recursively refining internal latent representations with shared weights, offering a more effective alternative to explicit verbal reasoning. Despite their effectiveness, we find that LoopLMs remain prone to loop instability: unstable refinement across iterations can produce localized uncertain "hard" tokens associated with reasoning errors. To address this, we propose LoopCD, loop-wise contrastive decoding that enhances the reasonin...
  </details>

- **2026-09-21** — Lucky Kant Nayak, Narayanan Palghat Parameswaran, Neehar Peri et al. — [MimicAgent: Quadruped Skills via Prompt-to-Trajectory Generation](http://arxiv.org/abs/2609.24145v1)
  <details><summary>📄 Abstract</summary>
  We present MimicAgent, a prompt-to-trajectory generation framework for learning dynamic quadruped skills. Although reward shaping is extensively used when training quadruped policies, navigating the resulting reward landscape is notoriously difficult, requiring hours of "graduate student descent". Eureka attempts to automate reward design with LLMs, but we find that it struggles to generalize across diverse skills and morphologies. Our key observation is that it is far easier for a human - and b...
  </details>

- **2026-09-21** — Yuyao Wang, Gaoze Mu, Yongan Zheng et al. — [From Ideal Motion to Flight-Executable Communications: LLM-Evolved Multi-UAV Deployment for Cell-Free Massive MIMO](http://arxiv.org/abs/2609.23992v1)
  <details><summary>📄 Abstract</summary>
  Cell-free massive multiple-input multiple-output (CF-mMIMO) is a promising paradigm for future wireless networks, providing user-centric services and cooperative coverage. By using unmanned aerial vehicles (UAVs) as aerial access points, CF-mMIMO networks can exploit UAV mobility to enhance three-dimensional (3D) coverage and spectral efficiency (SE). However, most existing studies on UAV deployment for communication optimization typically assume that UAVs follow ideal point-mass motion (IM), ne...
  </details>

- **2026-09-21** — Zixuan Wang, Matias Quiroz, Feng Li et al. — [Spectral divide-and-conquer MCMC for long stationary time series](http://arxiv.org/abs/2609.23985v1)
  <details><summary>📄 Abstract</summary>
  The temporal dependence inherent in time series models poses a fundamental challenge for distributed Bayesian inference, as it precludes embarrassingly parallel algorithms based on naive independence assumptions in the time domain. We propose a frequency-domain framework for scalable Bayesian inference in stationary time series that exploits the asymptotic independence underlying the Whittle likelihood. To exploit parallel computing resources, we develop a distributed fast Fourier transform and ...
  </details>

- **2026-09-21** — Andy K. Zhang, Ava Huang, Joey Ji et al. — [MobileCybench: Evaluating Agent Vulnerability Discovery via Executable Probes](http://arxiv.org/abs/2609.23980v1)
  <details><summary>📄 Abstract</summary>
  AI agents now report vulnerabilities faster than maintainers can review them. Reports often depend on security properties specific to the application, and require considerable human labor to process. To mitigate this, we introduce a framework for evaluating vulnerability reports via probes, executable checks of security properties. A reported exploit is evaluated by replaying it against the application and running the probes: a triggered probe indicates both that the exploit succeeded and which ...
  </details>

- **2026-09-21** — Zhihao Xing, Yingyu Wang, Liang Zhao et al. — [Colon3R: Cross-Domain 3D Reconstruction from Monocular Colonoscopic Video](http://arxiv.org/abs/2609.23961v1)
  <details><summary>📄 Abstract</summary>
  Monocular colonoscopic 3D reconstruction is important for surgical robotic colonoscopy, but remains challenging due to weak texture, specular reflections, limited view overlap, and non-rigid tissue motion. Conventional multi-view 3D reconstruction methods rely on stable correspondences and approximate rigidity, which are often violated in colonoscopy. Existing endoscopic methods often rely on domain-specific supervision, whereas there are not enough in-vivo labeled data available to adapt geomet...
  </details>


### 📂 defense
*防御与防护方法 / Defense & Protection Methods* — 49 papers

- **2026-09-23** — Giacomo Giuliari, Karl Wüst — [Physalia: Redistribution-Resistant Content Protection for Decentralized Storage](http://arxiv.org/abs/2609.28277v1)
  <details><summary>📄 Abstract</summary>
  In decentralized storage systems, access control is often implemented by encrypting the data before upload and sharing the decryption key with authorized parties. A leaked key, however, makes the data publicly accessible, which lowers the barrier to content piracy below that of traditional systems, where piracy requires redistributing the full data.   We present Physalia, an end-to-end access-control system for decentralized storage that secret-shares the data itself, instead of just the key, ac...
  </details>

- **2026-09-23** — Christopher Koch — [From Agent Output to Authorized Transition](http://arxiv.org/abs/2609.28216v1)
  <details><summary>📄 Abstract</summary>
  Agentic engineering systems can edit repositories, run tools and tests, build firmware, synthesize schematics, and prepare deployable or manufacturable artifacts. The assurance problem is therefore shifting from whether an agent can produce an output to whether an engineering lifecycle is justified in acting on claims about that output. Current products and standards provide sandboxes, approvals, hooks, traces, policy enforcement, attestations, bills of materials, and assurance representations, ...
  </details>

- **2026-09-23** — Muhammad Usama, Khair Un Nisa, Summer Yeoreum Jung — [Control-Token Injection Suppresses Chain-of-Thought and Defeats Reasoning-Based Oversight in Tool-Using Agents](http://arxiv.org/abs/2609.27542v1)
  <details><summary>📄 Abstract</summary>
  The safety of a tool-using language model agent is usually treated as a property of the model alone. We give controlled, full-precision evidence that it is instead a joint property of the model and the software that renders its chat template and parses its tool calls, the decoding harness, and that both halves are attackable from untrusted input. On the released gpt-oss-20b reasoning model under its published tool sandbox, appending a single string of the model's own channel-control tokens to a ...
  </details>

- **2026-09-23** — Jiapeng Sun, Yujin Zhou, Han Zhu et al. — [PASTABench: Proactive Assessment of Sequential Trajectories for Agent Safety](http://arxiv.org/abs/2609.28197v1)
  <details><summary>📄 Abstract</summary>
  As Large Language Models (LLMs) evolve into autonomous agents that alter real-world states, ensuring operational safety across multi-step workflows has become a critical challenge. While recent work has moved beyond single-turn evaluation toward multi-turn paradigms, key limitations persist: step-level methods treat actions in isolation, missing how risks accumulate, while trajectory-level evaluations operate post-hoc, offering no opportunity for timely intervention. To address these limitations...
  </details>

- **2026-09-23** — Bock-Zien Toh, Yuanchuan Ren, Tay Aw Yu et al. — [CasCVS-Net: A Staged Multi-Task Cascade for Critical View of Safety Assessment](http://arxiv.org/abs/2609.27681v1)
  <details><summary>📄 Abstract</summary>
  Automated assessment of the Critical View of Safety (CVS) in laparoscopic cholecystectomy requires both recognition of the three CVS criteria and anatomical grounding in small, rare, and often occluded hepatocystic structures. Learning-based methods differ in the anatomical information they use, from image-level classification to detection, segmentation, or graph-based reasoning, yet grounding the safety-critical anatomy remains the main bottleneck. We propose CasCVS-Net, a staged multi-task cas...
  </details>

- **2026-09-23** — Zeyu Wang, Xiaodan Li, Zhiwen Li et al. — [InGuard: Towards Generalized Inner Guardrail for Safe Text-to-Image Generation](http://arxiv.org/abs/2609.27620v1)
  <details><summary>📄 Abstract</summary>
  Modern text-to-image (T2I) models generate high-quality images from arbitrary user prompts, yet they can just as easily produce not-safe-for-work (NSFW) content. Conventional outer guardrails consist of two components: a prompt classifier that checks for risk before generation, and a post-hoc image classifier that checks the fully generated image. In this design, both classifiers operate outside the generation pipeline and do not use the model's own representations. This separation can limit pro...
  </details>

- **2026-09-23** — Roy Ricaldi, Kristiyan Kyurkchiev, Irdin Pekaric — [A Bulletproof Business? Towards Detecting Infrastructure-as-a-Service Offerings on Telegram](http://arxiv.org/abs/2609.27428v1)
  <details><summary>📄 Abstract</summary>
  Cybercriminal operations increasingly depend on reusable digital infrastructure---including hosting, proxies, and virtual private networks (VPNs)---rented through Cybercrime-as-a-Service markets and advertised on platforms such as Telegram. We present a taxonomy for identifying Telegram messages advertising cybercriminal Infrastructure-as-a-Service (IaaS). The taxonomy comprises six service categories across compute, network, and communication infrastructure, together with three trust attributes...
  </details>

- **2026-09-23** — Thomas Ratsakatika, Mihai Zotta, Srinivasan Keshav et al. — [Geospatial embeddings detect old-growth forests but buffered spatial validation narrows their advantage over Sentinel features](http://arxiv.org/abs/2609.28194v1)
  <details><summary>📄 Abstract</summary>
  Old-growth forests develop over centuries under minimal anthropogenic disturbance, producing structurally complex and biodiverse stands. In Europe, protecting them requires mapping that is accurate for individual forest parcels yet deployable continent-wide. Geospatial foundation model (GFM) embeddings enable label-scarce land classification, but their value for old-growth detection remains unknown. Here, we map old-growth forests across 211,893 ha of Romania's Southern Carpathians, a beech-spru...
  </details>

- **2026-09-23** — Matthieu Dubois, Pablo Piantanida, François Yvon — [How Much Were You Told? Measuring External Information in Peer Reviews](http://arxiv.org/abs/2609.28041v1)
  <details><summary>📄 Abstract</summary>
  Conference policies distinguish using Large Language Models (LLMs) to polish one's own review from delegating the critique, but current Artificial Text Detection (ATD) methods largely measure surface form rather than the origin of its content. We instead measure the external information carried by a review: information not explained by the reviewed paper and a generic reviewing instruction. We propose Self-Conditioning, an unsupervised information-theoretic estimator that compares the likelihood...
  </details>

- **2026-09-23** — Yongjun Jeong, Hanbum Ko, Ye Rin Kim et al. — [MolDesignBench: Evaluating LLM-based Agent for Scenario-grounded Molecular Design](http://arxiv.org/abs/2609.27349v1)
  <details><summary>📄 Abstract</summary>
  Real-world molecular design remains challenging for large language model (LLM)-based agents. It requires them to interpret design contexts, satisfy multiple constraints, identify infeasible specifications, and reason over multi-step tool outputs. Existing benchmarks do not capture this complexity, focusing instead on explicit and narrow constraints, only feasible problems, and single-path solutions. To address this gap, we propose MolDesignBench, a scenario-grounded benchmark that more closely r...
  </details>

- **2026-09-22** — Armin Maleki, Hayder Radha — [PEARL: A Lightweight Prompt-based Feature Interpreter Framework for Real-Time, Anonymous, and Heterogeneous Collaborative Perception](http://arxiv.org/abs/2609.27123v1)
  <details><summary>📄 Abstract</summary>
  Heterogeneity across Collaborative Perception (CP) agents is a major challenge for emerging CP frameworks due to domain gaps from differing sensors, architectures, and training data. Prior works mitigate this challenge by aligning features in a unified space via model retraining or per-agent-type interpreters. These strategies (a) require access to neighbor configurations, (b) do not fully address real-time CP deployment, and (c) generalize poorly to unseen agents joining at run time. To overcom...
  </details>

- **2026-09-22** — Yi Xu, Ehsan K. Ardestani, Wenyin Fu et al. — [Crossflow: Prefill-Decode Elasticity for Agentic LLM Serving](http://arxiv.org/abs/2609.27085v1)
  <details><summary>📄 Abstract</summary>
  As serving capacity demand surpasses that of training, serving efficiency becomes increasingly important. Prefill-decode (P/D) disaggregation improves serving efficiency through specialization and isolation of the two phases. These benefits rest on a static partitioning. Phase demand, however, is not static. We observe that in a large LLM fleet the ratio of uncached input to output tokens has peak-to-mean ratios up to 4.7x at minute timescales, and that in a public agentic trace the hourly ratio...
  </details>

- **2026-09-22** — Sujay Uday Rittikar, Sheela Ramanna — [LexLattice: Multilingual Extractive Summarization via Neural Cellular Automata on Document Hierarchies](http://arxiv.org/abs/2609.27032v1)
  <details><summary>📄 Abstract</summary>
  Faithfulness is a central concern in legal text summarization, which motivates extractive approaches that select verbatim content traceable to its source. Such methods typically rank paragraphs or other structural units in isolation, yet give little attention to consolidating evidence that is distributed across, and shares salience between, distant parts of a document. We introduce LexLattice, an extractive summarizer that reifies a legal act's hierarchy as a two-dimensional semantic lattice and...
  </details>

- **2026-09-22** — Mostafa Anouar Ghorab, Ahmad Abdel Latif, Mohamed Aymen Saied — [Kubernetes Misconfigurations in the Wild: Taxonomy, Evolution, and Automated Repair with Large Language Models](http://arxiv.org/abs/2609.27030v1)
  <details><summary>📄 Abstract</summary>
  Kubernetes is widely used to orchestrate cloud-native applications, yet its declarative configuration model often introduces security misconfigurations that threaten system reliability. Despite available detection tools, misconfiguration patterns and scalable remediation remain insufficiently understood.   This paper presents an empirical study of Kubernetes security misconfigurations based on 2,662 developer-reported Stack Overflow issues. We derive a taxonomy of recurring security weaknesses a...
  </details>

- **2026-09-22** — Constantin Ulrich Harsy, Tassilo Wald, Karol Gotkowski et al. — [nnFoundation: 3D Foundation Models for Radiology](http://arxiv.org/abs/2609.26924v1)
  <details><summary>📄 Abstract</summary>
  Radiological artificial intelligence has advanced rapidly, yet most systems remain narrowly task-specific, data-intensive, and fragile under domain shift. Foundation models promise more transferable and data-efficient solutions, but existing approaches are limited in scale, evaluated narrowly, and often assume that a single pretrained model can support diverse downstream tasks. Here we present nnFoundation, complementary convolutional and transformer-based 3D radiological foundation models. Deve...
  </details>

- **2026-09-22** — Abel A. Reyes-Angulo, Henry O. Velesaca, Steven Araujo — [SambaGraph: Action-Reaction Spatio-Temporal Graphs for Soccer Tactical Response Modeling](http://arxiv.org/abs/2609.25569v1)
  <details><summary>📄 Abstract</summary>
  Soccer tactics are interactive: an attacking action changes the opponent's defensive problem, and the observed response depends on the multi-agent match state. We introduce SambaGraph, an action--reaction spatio-temporal graph dataset and benchmark for soccer tactical response modeling. From tracking and event data for all 64 matches of the 2022 FIFA World Cup, we curate 4,070 action-centered episodes represented as temporally aligned 23-node player--ball graph sequences with attack/defense view...
  </details>

- **2026-09-22** — Quan Nguyen-Tri, Mukul Ranjan, Zhiqiang Shen — [Flash-dLLM: IO-Aware KV Caching and Parallel Decoding for Fast, Memory-Efficient Diffusion LLMs](http://arxiv.org/abs/2609.26796v1)
  <details><summary>📄 Abstract</summary>
  Diffusion Large Language Models (dLLMs) have recently emerged as a promising alternative to autoregressive LLMs by enabling non-autoregressive text generation. However, their practical deployment remains limited by inefficient inference, largely due to the absence of effective Key-Value (KV) caching and scalable parallel decoding mechanisms. Existing acceleration methods typically study KV caching and parallel decoding in isolation, overlooking the I/O bottlenecks that arise when cache reuse and...
  </details>

- **2026-09-22** — Linman Wang, ZiFei Zhang, Chunran Zheng et al. — [DIFTA-3D: Depth-Consistent Instance-Level Feature Transfer and Adaptation of DINOv3 for 3D Detection](http://arxiv.org/abs/2609.26702v1)
  <details><summary>📄 Abstract</summary>
  RGB-D 3D instance detectors benefit from visual semantics, but the task-specific Faster R-CNN/ResNet branch used by IIFNet3D couples feature extraction to a separately trained 2D detector and its image-domain labels. Replacing that branch with a frozen vision foundation model removes this task-specific dependency, but may introduce occlusion noise and a mismatch between patch features and geometry-aware detection features. In this work, we investigate this replacement through an adaptation of DI...
  </details>

- **2026-09-22** — Nathalie Baracaldo — [From Alignment to Access Control: A Framework for GenAI Policy Enforcement](http://arxiv.org/abs/2609.26682v1)
  <details><summary>📄 Abstract</summary>
  Generative AI (GenAI) applications have flourished enabling users to chat with large language models, and to create agents to act on their behalf for a variety of tasks. The pace of development of capabilities in this field is incredibly fast with security and safety taking a back seat. Unfortunately, the slower pace at which security and safety mechanisms have evolved has led to real incidents. Policy enables the definition of desirable behavior of applications, and for that reason, it is a cor...
  </details>

- **2026-09-22** — Hoang-Lam Huynh, Quoc-Cuong Tang, Van-Tri Phan et al. — [Design and Evaluation of a Controlled Post-Alert Incident Orchestration and Response Subsystem Using a Rule Engine and a Local Large Language Model](http://arxiv.org/abs/2609.26316v1)
  <details><summary>📄 Abstract</summary>
  This paper presents a controlled post-alert incident orchestration and response subsystem for educational information systems. The architecture separates deterministic classification, contextual analysis, human approval, and technical execution. A Rule Engine determines severity and selects the playbook, while Static RAG and a local large language model provide advisory content under Validator, Guardrail, Output Sanitizer, and Safe Fallback controls. Experiments begin after simulated alerts are ...
  </details>

- **2026-09-22** — Elie Abboud, Oren Gal — [MATES: Learning Multi-Agent Interactions by Transforming Observations for Frozen Single-Agent Policies](http://arxiv.org/abs/2609.26010v1)
  <details><summary>📄 Abstract</summary>
  Multi-agent reinforcement learning (MARL) commonly trains decentralized policies from scratch, requiring agents to acquire individual task competence and coordination simultaneously. Yet many multi-agent problems admit a compatible single-agent counterpart in which the underlying task can be learned in isolation. We introduce Multi-Agent Observation Transformation for Existing Single-Agent Policies (MATES), an input-side adaptation framework for tasks whose multi-agent observations preserve the ...
  </details>

- **2026-09-22** — Baher Mohammad, Ammar Ali, Stamatios Lefkimmiatis — [GeoPair: Geometry-Preserving Cross-Layer Factorization for Training-Free Transformer Compression](http://arxiv.org/abs/2609.25963v1)
  <details><summary>📄 Abstract</summary>
  Transformer architectures exhibit cross-layer redundancies, yet post-training compression pipelines typically optimize layers in isolation or rely on heuristic grouping strategies that disregard layer-specific activation geometries. We introduce a principled, training-free framework that sequentially optimizes cross-layer weight pairings and shared-dictionary factorizations. Rather than forcing weights of adjacent layers to share a basis or heuristically merging activation statistics, our approa...
  </details>

- **2026-09-22** — Malsha Ashani Mahawatta Dona, Konstantinos Rokanas, Alexander Säfström et al. — [Towards Systematic Qualification of Vision-Language Models for Automotive Perception Systems](http://arxiv.org/abs/2609.25945v1)
  <details><summary>📄 Abstract</summary>
  The field of Artificial Intelligence has been adopted for many application domains. Vision Language Models are one of the recently advanced AI techniques that have been explored to support automotive features such as vehicle perception, and safety assurance. However, such language models are prone to hallucinations, posing a potential threat to the safety of automotive systems that may incorporate them. Within the automotive domain, VLMs could not only hallucinate traffic objects, but could also...
  </details>

- **2026-09-22** — Weijie Zhou, Zhaoyang Zhang, Zhixian Kong et al. — [MIMO-OFDM AI Receiver Based on Incrementally Conditioned Diffusion with Soft Decision](http://arxiv.org/abs/2609.25923v1)
  <details><summary>📄 Abstract</summary>
  Conventional iterative receiver usually begins with channel estimation using sparse pilot observations and follows with data detection based on the channel estimates, and then updates channel estimation using decision feedback, and so on. In Artificial Intelligence (AI)-based receiver design, it is also crucial to make use of such progressively enriched data observations to enhance the generative channel estimation. However, the statistical characteristics and reliability of the data decisions a...
  </details>

- **2026-09-22** — Massimiliano Sassoli de Bianchi, Roberto Leporini — [Reply to comments arXiv:2512.07881 and arXiv:2601.06104 on quantum structure in human and AI-generated language](http://arxiv.org/abs/2609.25797v1)
  <details><summary>📄 Abstract</summary>
  We reply to the comments by M. Sienicki and K. Sienicki (arXiv:2512.07881) and by K. Sienicki (arXiv:2601.06104) on our work on quantum-mechanical statistics in human language (arXiv:2407.14924) and on quantum structure in AI-generated language (arXiv:2511.21731). We thank the authors for their careful reading and address what we consider to be the main points of criticism: the exploratory nature of the protocol used in the experiments with large language models; the role of marginal-law violati...
  </details>

- **2026-09-22** — Zheng Chen, ZhiCheng Du, Haoxuan Li et al. — [Syndrome, Synergy, and Safety: Structured Reasoning and Knowledge-Driven Alignment for TCM Prescription Generation](http://arxiv.org/abs/2609.25755v1)
  <details><summary>📄 Abstract</summary>
  Applying large language models to Traditional Chinese Medicine (TCM) prescription generation reveals three clinically critical gaps: models produce end-to-end mappings without auditable reasoning following the li-fa-fang-yao paradigm (SR Gap), treat each encounter in isolation without follow-up adjustment via sui zheng jia jian (LA Gap), and fail to enforce absolute contraindication rules such as Shi Ba Fan (SC Gap). We propose a progressive four-stage framework (SFT $\to$ PG-CoT $\to$ Dynamic $...
  </details>

- **2026-09-22** — Ansgar Steland — [Context-Adaptive Thresholding for Conditionally Representative Monitoring and Classification](http://arxiv.org/abs/2609.26652v1)
  <details><summary>📄 Abstract</summary>
  Commonly, classifiers and monitoring procedures are trained from labeled data by optimizing an objective such as the misclassification rate. This may lead to unrepresentative conditional distributions of the outcome (the labels) given important external variables, different from the conditional laws in the population. We show how to modify any given threshold-type classifier resp. monitoring rule to achieve representative conditional label prediction by using adapting the threshold to a covariat...
  </details>

- **2026-09-22** — Peiying Zhu, Sidi Chang — [When Are Aggregate Agent Traces Diagnosable? Traffic-Governed Interpretation and Calibrated Abstention](http://arxiv.org/abs/2609.25806v1)
  <details><summary>📄 Abstract</summary>
  Runtime traces can appear transparent, but a closed-loop policy determines which states are visited and which failures become visible. We study a simulated hotel-pricing agent mapping time, inventory, and market state to discrete price actions under varying demand regimes. A fault may leave no aggregate trace when the policy rarely visits affected cells. We treat entry into aggregate-only fault interpretation as a diagnosability decision preceding scoring or localization. A reference-map gate re...
  </details>

- **2026-09-22** — Charis Y. N. Chiang, Tarela Sarimiye, Adeyinka Ashaye et al. — [Interpretable AI plus Handheld, Portable Retinal Photographs: A Low-Cost Glaucoma Screening Solution for West Africa](http://arxiv.org/abs/2609.25697v1)
  <details><summary>📄 Abstract</summary>
  Purpose: To develop and evaluate an interpretable artificial intelligence (AI) framework for glaucoma screening from low-cost portable, handheld retinal fundus photographs in a West African population and to compare its performance with clinical tabletop fundus imaging. Methods: We used data from a community-based study of 681 participants (1,362 eyes) in Nigeria, comprising 414 glaucoma, 478 glaucoma suspect, and 470 non-glaucoma eyes. Fundus photographs were acquired using the low-cost handhel...
  </details>

- **2026-09-21** — Chetan Pathade, Prathamesh Pawar, Shubham Patil — [Attack Success Rate Is Not a Number: On Measurement Validity in Agentic AI Security Evaluation](http://arxiv.org/abs/2609.25173v1)
  <details><summary>📄 Abstract</summary>
  Attack success rate (ASR) is the headline metric in nearly every published evaluation of attacks on, and defenses for, LLM agents. We argue that ASR as currently used is not a single quantity but a family of metrics parameterized by six design choices that papers seldom specify and never hold constant across the literature. We support this with two studies that require no proprietary access. First, a full-text meta-analysis of 259 agentic-security papers posted to arXiv between February 2025 and...
  </details>

- **2026-09-21** — Jacob Charnock, Sophie Williams, Zaheed Kara et al. — [Embedded Assessments for Frontier AI](http://arxiv.org/abs/2609.25413v1)
  <details><summary>📄 Abstract</summary>
  Third-party evaluations for frontier AI have mostly tested models through external interfaces before deployment. But the risks from frontier AI models depend on how their developers use and govern them internally. Recently, CEOs of frontier AI companies have committed to hosting embedded assessments. These assessments would give independent evaluators employee-like access to a developer's internal systems, staff, and documentation. First, we argue that this can enable deeper and more flexible as...
  </details>

- **2026-09-21** — Aakash Patel, Panos Ketonis, Shreya Saxena et al. — [The AI Neuroscientist: An Interactive Agentic Interface for Neuroimaging Analysis](http://arxiv.org/abs/2609.25254v1)
  <details><summary>📄 Abstract</summary>
  Analyzing neuroimaging data requires specialized coding and statistical expertise, which limits accessibility for researchers without computational backgrounds. We present the AI Neuroscientist, a language agent for interactive data exploration. The system integrates a large language model (LLM) with a neuroimaging toolset to perform quality control, modeling, and visualization. This allows researchers to query data quality and specify analysis parameters directly in natural language, providing ...
  </details>

- **2026-09-21** — Sepideh Hodaeian, Zhenhao Li, An Ran Chen — [TAILOR: Template-Preserving Augmentation for Long-Tailed Log Parsing](http://arxiv.org/abs/2609.25261v1)
  <details><summary>📄 Abstract</summary>
  Log parsing is essential for system log analysis because it supports tasks such as debugging, monitoring, and anomaly detection by transforming unstructured log messages into structured log templates. However, real-world log datasets exhibit highly imbalanced, long-tailed distributions, where a small number of frequent templates dominate while many rare templates appear only a few times. This imbalance causes evaluation results to be overly optimistic by allowing frequent templates to dominate b...
  </details>

- **2026-09-21** — Lifu Mu, Shuai Chen, Wen Zheng et al. — [LiAuto-MindViT: A Hybrid Vision Backbone with Adaptive Bidirectional Mamba](http://arxiv.org/abs/2609.24337v2)
  <details><summary>📄 Abstract</summary>
  While Mamba-based models have shown strong potential for long sequence modeling, adapting them to vision is challenging due to the requirement of local neighborhood correlations and multi-directional spatial contexts for visual understanding. In this paper, we present LiAuto-MindViT, a novel hybrid vision backbone that synergizes the strengths of CNNs, Mamba, and Transformers. The core of our design is the Adaptive Bidirectional Mamba (ABM), which eliminates the directional bias of unidirectiona...
  </details>

- **2026-09-21** — Manveen Kaur, Kevin Loi, Ifunanya Okafor et al. — [Perception-Aware Communication Middleware for Distributed Visual Perception in UAV Swarms](http://arxiv.org/abs/2609.24964v1)
  <details><summary>📄 Abstract</summary>
  Unmanned Aerial Vehicle (UAV) swarms increasingly support safety-critical applications that rely on distributed visual perception. Meeting the low-latency requirements of these applications can require perception models to execute within the swarm on inference-capable UAVs, creating a need for efficient UAV-to-UAV transport of high-bandwidth perception data. However, the Quality-of-Service (QoS) requirements of perception differ from conventional packet-level QoS; successful delivery of individu...
  </details>

- **2026-09-21** — Yuming Li, Fan Zhang, Alin M. Achim — [DTKDP: A Dual Teacher Knowledge Distillation and Pruning Framework for Lightweight Oriented SAR Ship Detection](http://arxiv.org/abs/2609.24872v1)
  <details><summary>📄 Abstract</summary>
  Two-stage oriented detectors achieve high localization accuracy in synthetic aperture radar (SAR) ship detection, but their large backbones, feature pyramids, proposal modules, and heavy region of interest (RoI) heads hinder deployment. Existing lightweight SAR ship detectors typically use one-stage frameworks that lack proposal-level refinement for precise rotated localization. This paper presents a dual-teacher knowledge distillation and pruning (DTKDP) framework for lightweight oriented SAR s...
  </details>

- **2026-09-21** — Changxu Liu, Zhaogeng Li — [Adapting Tree-Structured Speculative Decoding to DeepSeek-V4 for Efficient Inference](http://arxiv.org/abs/2609.24698v1)
  <details><summary>📄 Abstract</summary>
  Repeated execution of the target model during autoregressive decoding is a major source of LLM inference latency. Unlike linear speculation, which follows a single candidate chain, tree-structured speculation retains multiple branches from shared prefixes; under the same budget, this broader coverage can improve acceptance and efficiency. Adapting it to DeepSeek-V4 is nontrivial: its CSA/HCA online compressed attention concentrates the difficulty on the target-verify side, where branches divergi...
  </details>

- **2026-09-21** — Lingfeng Wu, Behzad Shomali — [Written as a Record, Read as an Address: What a Forward Pass Leaves in an Operation's KV Cache](http://arxiv.org/abs/2609.24635v1)
  <details><summary>📄 Abstract</summary>
  When a language model reads an operation such as "Swap the contents of Box F and Box B", its forward pass writes keys and values for those tokens into the KV cache. Prior work on entity tracking establishes what models use: bindings are resolved at query time rather than stored as explicit latent state. We ask what they write at the operation span and how it is accessed. We split a forward pass into a frozen writer and a reader: the writer's cache is recomputed without gradients, while the reade...
  </details>

- **2026-09-21** — Boris Wetzk — [Epi-Logic: A Conceptual Framework for Epistemic Runtime Control, Schema Validity Checking, and Controlled Accommodation in Autonomous AI Agents](http://arxiv.org/abs/2609.24755v1)
  <details><summary>📄 Abstract</summary>
  Autonomous AI agents are increasingly deployed in areas where wrong decisions are hard to reverse. This paper examines schema mismatch: the condition in which an agent operates within an interpretive frame that no longer applies to the current context. Outputs produced under such a mismatch can appear internally consistent, linguistically plausible, and largely factually correct; output-quality metrics alone therefore capture the underlying loss of validity only partially.   The paper introduces...
  </details>

- **2026-09-21** — Trinh T. L. Vuong, Simon Graham, Quoc Dang Vu et al. — [MiTHras: Task-specific Hierarchical Semi-supervised Contrastive Masked Autoencoder for Mitotic Figure Analysis](http://arxiv.org/abs/2609.24736v1)
  <details><summary>📄 Abstract</summary>
  Mitotic figure (MF) analysis supports tumor grading and prognostic assessment, but automated models remain sensitive to differences in tissue type and image acquisition. We present MiTHras, a task-specific pretraining framework that combines pseudo-label-guided image- and token-level contrastive learning with masked reconstruction. We construct TCGA-MF-Pseudo, a corpus of 1.8 million cell-centered images from 14 TCGA cohorts spanning 11 organ sites. Comprehensive evaluation on MF classification,...
  </details>

- **2026-09-21** — Jingyu Wang, Shijie Wu, Fusheng Jin — [URA-NER: A Unified Retrieval-Augmented Framework with Retrieval Alignment and Uncertainty Reduction for Low-Resource NER](http://arxiv.org/abs/2609.24372v1)
  <details><summary>📄 Abstract</summary>
  In-context learning (ICL) based on large language models (LLMs) has shown promising potential in alleviating performance bottlenecks caused by the limited availability of annotated data in Named Entity Recognition (NER). However, existing methods still face issues of retrieval misalignment and generation uncertainty, making their performance heavily dependent on the LLM's capabilities. As the parameter scale of LLMs decreases, their performance in few-shot settings deteriorates significantly. In...
  </details>

- **2026-09-21** — Hexiong Yang, Mingrui Chen, Jie Cao et al. — [VLM-in-Sandbox: Visual Workspaces for Agentic Visual Reasoning](http://arxiv.org/abs/2609.24362v1)
  <details><summary>📄 Abstract</summary>
  Sandboxed computer environments support multi-step reasoning with tools, executable programs, and persistent files, yet their extension from language models to vision-language models (VLMs) introduces a distinct state-management problem. Visual reasoning produces intermediate image-valued evidence---crops, masks, overlays, zoomed regions, and analytic renderings---that must remain addressable without accumulating unboundedly in multimodal context. We introduce VLM-in-Sandbox, a training-free fra...
  </details>

- **2026-09-21** — Anubhav Gupta, Hrushikesh Mohapatra, Prijith Chandra et al. — [Graded-Relevance Composed Multimodal Retrieval for E-commerce Visual Search at Scale](http://arxiv.org/abs/2609.24152v1)
  <details><summary>📄 Abstract</summary>
  Visual search on large e-commerce catalogs must serve both "similarity" queries that ask for items resembling an uploaded image and "modifier" queries that comprise an image and text describing a desired modification (e.g. a color change or style swap). The latter is the setting known as composed image retrieval (CIR). Existing CIR methods, however, treat relevance as binary and train on triplets with a single positive target - a poor fit for real catalogs where many candidates partially satisfy...
  </details>

- **2026-09-21** — Viet Huy Duong, Ruoxin Xiong, Md Abdullah Al Forhad et al. — [A paired synthetic construction-site image dataset for robust computer vision under adverse conditions](http://arxiv.org/abs/2609.24075v1)
  <details><summary>📄 Abstract</summary>
  Computer-vision systems used for construction monitoring can degrade under adverse environmental and visual conditions, yet such conditions remain underrepresented in existing construction image datasets. We present ConSynth-X, a paired synthetic construction-site image dataset containing 34,199 images derived from 3,109 real-world source scenes. The dataset comprises 11 condition-specific subsets spanning precipitation, fog, nighttime illumination, adverse weather at night, and small-object or ...
  </details>

- **2026-09-21** — Vatsal Gupta, Darshan Sreenivasamurthy — [Structured Decomposition for Reliable LLM-Generated Access Control Policies](http://arxiv.org/abs/2609.24036v1)
  <details><summary>📄 Abstract</summary>
  This paper presents an LLM-based system that translates natural-language access control policies (NLACPs) into executable Rego code for Open Policy Agent (OPA). It provides a modular, end-to-end pipeline for policy detection, component extraction, schema validation, linting, compilation, and automated test generation and execution. The system is designed to bridge the gap between human-readable access requirements and machine-enforceable policy-as-code (PaC), with a focus on deployment reliabili...
  </details>

- **2026-09-21** — Stefan Sarkadi, Xabier Garmendia, Jack Mumford et al. — [DeceptionAnalyser: A Web-Based AI Tool for Performing Structured Deception Analysis with Argumentation Schemes and LLMs](http://arxiv.org/abs/2609.24369v1)
  <details><summary>📄 Abstract</summary>
  Deception plays a central role in Intelligence operations, yet it remains difficult to analyse systematically without expert knowledge of reasoning patterns and cognitive manipulation. In computational argumentation, for instance, no scheme-level ground-truth corpora currently exist to support statistical validation. In this paper, we address this by introducing a set of ten argument schemes designed to model distinct forms of deception, each accompanied by structured premises and critical quest...
  </details>

- **2026-09-21** — Xianlong Li, Pietro Bongini, Niccoló Pancino et al. — [Dissecting Agentic Forensics: The Role of Triage, Prompting, and Evidence Arbitration in Open-World Fake Image Detection](http://arxiv.org/abs/2609.24359v1)
  <details><summary>📄 Abstract</summary>
  Image forensics is increasingly an open-world problem: manipulations range from fully synthetic images to localized edits, splicing and swapping, while most forensic detectors remain specialized to a single manipulation family. Agentic AI has recently emerged as a promising solution. In principle, such systems can assess the reliability of individual detectors, identify out-of-scope evidence, and arbitrate conflicting reports. However, it remains unclear which components actually drive performan...
  </details>

- **2026-09-21** — Bilal Al-Ahmad, M. Harshvardhan, Khaled El-Fakih et al. — [Evaluating the effectiveness of class-level LLM-generated test suites in Python](http://arxiv.org/abs/2609.24341v1)
  <details><summary>📄 Abstract</summary>
  Context: Large language models (LLMs) can generate unit tests quickly, but high structural coverage does not establish that those tests execute reliably or detect faults. Existing evidence often treats coverage as the principal outcome and rarely compares prompt strategies and models through mutation testing at class level. Objective: This study examines how prompt strategy and model choice shape the executability, structural coverage, fault-detection effectiveness, and structural quality of LLM...
  </details>

- **2026-09-21** — Lifu Mu, Shuai Chen, Wen Zheng et al. — [LiAuto-MindViT: A Hybrid Vision Backbone with Adaptive Bidirectional Mamba](http://arxiv.org/abs/2609.24337v1)
  <details><summary>📄 Abstract</summary>
  While Mamba-based models have shown strong potential for long sequence modeling, adapting them to vision is challenging due to the requirement of local neighborhood correlations and multi-directional spatial contexts for visual understanding. In this paper, we present LiAuto-MindViT, a novel hybrid vision backbone that synergizes the strengths of CNNs, Mamba, and Transformers. The core of our design is the Adaptive Bidirectional Mamba (ABM), which eliminates the directional bias of unidirectiona...
  </details>


### 📂 alignment
*对齐与安全约束 / Alignment & Safety Constraints* — 56 papers

- **2026-09-23** — Kaiyang Li, Shaobo Han, Yue Tian et al. — [Mizar: A 159M-Parameter Audio-Language Model for Audio Understanding](http://arxiv.org/abs/2609.28344v1)
  <details><summary>📄 Abstract</summary>
  Audio-language models (ALMs) integrate acoustic perception with the knowledge encoded in language models, enabling contextual understanding of auditory events. Making these capabilities practical on devices with limited memory and computation motivates our focus on small ALMs with fewer than 200M parameters. We introduce a recipe that brings together architecture, data, and three-stage training to build Mizar, a 159.3M-parameter ALM. Its architecture connects a compact CED-Small audio encoder to...
  </details>

- **2026-09-23** — AbdulRahman A. Morsy, Aya Zirikly — [Beyond Poetry: Can Large Language Models Generate Classical Arabic Maqamat?](http://arxiv.org/abs/2609.28245v1)
  <details><summary>📄 Abstract</summary>
  Large language models (LLMs) have shown strong performance in creative text generation, yet their ability to produce culturally grounded and stylistically constrained literary forms remains underexplored. Prior work has focused largely on modern language varieties and poetry, while classical prose traditions such as maqama remain largely unstudied. The maqama is a classical literary genre characterized by rhymed prose (saj), dense rhetorical ornamentation, and episodic narrative structure, makin...
  </details>

- **2026-09-23** — Xueqi Qiu, Xingyu Miao, Jingjing Deng et al. — [From Alignment to Fusion in 3D Vision-Language](http://arxiv.org/abs/2609.28222v1)
  <details><summary>📄 Abstract</summary>
  Unified 3D vision-language systems must combine complementary geometry, scale, and appearance cues while supporting tasks from instance segmentation to language-guided reasoning. Existing methods often process point clouds, voxel grids, and multi-view images independently; directly combining these heterogeneous representations may leave substantial feature discrepancy unresolved, while subsequent unconstrained adaptation may distort their internal geometry. We propose an align-then-fuse framewor...
  </details>

- **2026-09-23** — Basavaraj Sunagad, Artur Jesslen, Adam Kortylewski — [Two Global Crops Suffice: Locating Semantic Emergence in DINO-Style Self-Supervised Learning](http://arxiv.org/abs/2609.28187v1)
  <details><summary>📄 Abstract</summary>
  Self-supervised vision transformers trained with DINO-style objectives exhibit striking emergent semantic representation quality across visual tasks, yet the mechanisms underlying this behavior remain unclear. We present a systematic empirical dissection of the DINO family and show that semantic representations arise primarily from enforcing consistency between geometrically distinct global views of the same image instance. This instance-specific global alignment acts as the semantic anchor of D...
  </details>

- **2026-09-23** — Shuai Dong, Yongfu Zhu, Yuqi Xu et al. — [RL Starts before RL: On Policy Distillation for Better Reinforcement Learning](http://arxiv.org/abs/2609.28145v1)
  <details><summary>📄 Abstract</summary>
  Reinforcement learning (RL) improves reasoning, but its performance depends on the policy from which training begins. We study on-policy distillation (OPD) as a preparation stage for RL and ask whether its benefits extend beyond improvements in the distilled model's initial accuracy. Under shared RL settings, students initialized with OPD reach higher final performance than those trained with direct RL or supervised fine-tuning followed by RL. This advantage can emerge even when OPD produces lit...
  </details>

- **2026-09-23** — Fuqiang Zhao, Qian Liu — [DEAL-Grasp: Decoupled Alignment Representation for Geometry-Aware Dexterous Grasp Generation](http://arxiv.org/abs/2609.28131v1)
  <details><summary>📄 Abstract</summary>
  Synthesizing realistic articulated hand-object interactions is a fundamental problem in virtual reality, embodied intelligence, and digital human applications. Existing methods for dexterous grasp synthesis typically regress or denoise poses in a joint space that couples global rigid motion with local articulation, which often yields unstable samples and physically implausible contacts. We introduce DEAL-Grasp, built upon the Decoupled Alignment (DEAL) representation, which reformulates grasp sy...
  </details>

- **2026-09-23** — Paweł Mąka, Yusuf Can Semerci, Jan Scholtes et al. — [Scaling Attention Head Analysis via Gradient-Based Attribution in Context-Aware Machine Translation](http://arxiv.org/abs/2609.28117v1)
  <details><summary>📄 Abstract</summary>
  In this paper, we introduce a gradient-based head attribution strategy where the Token-level Max-Margin loss is backpropagated to the attention maps. This framework enables a large-scale causal analysis of attention heads, making it suitable for LLMs. We evaluate our method on the task of disambiguation in Context-aware Machine Translation, where we analyze 50 phenomena across 4 models and 4 language directions. We empirically show the alignment of our method with the effects of increasing the a...
  </details>

- **2026-09-23** — Norah Almousa, Shayan Peyghambari Oskoui, Raquel Coelho et al. — [Evaluating Feedback Focus and Pedagogical Adaptivity in LLM-Generated Feedback on Student Writing](http://arxiv.org/abs/2609.28026v1)
  <details><summary>📄 Abstract</summary>
  We investigate whether state-of-the-art large language models (LLMs) generate feedback that reflects the pedagogical practices of expert teachers in terms of feedback focus and adaptivity. Previous evaluation efforts have examined feedback characteristics, its impact on learning, and its target, yet the focus of feedback and its adaptivity remains largely overlooked. To bridge this gap, we adopt and refine Narciss's taxonomy into seven feedback focus types to annotate teacher and LLM-generated f...
  </details>

- **2026-09-23** — Anh-Tien Nguyen, Trung DQ. Dang, Nghiem Tuong Diep et al. — [FFM-CP: Cross-Backbone Fusion of Vision-Language Foundation Models for Few-Shot Computational Pathology](http://arxiv.org/abs/2609.27710v1)
  <details><summary>📄 Abstract</summary>
  Pathology vision-language foundation models vary in performance across diseases and tasks, with no single model consistently performing best. The high cost of expert pathology annotation can also limit the labeled data available for task-specific adaptation. Combining complementary pretrained representations is a potential approach to these limitations, yet learning an effective fusion from few labeled examples remains challenging. We introduce Few-shot Fusion Foundation Models of Computational ...
  </details>

- **2026-09-23** — Renata Barreto, Markelle Roesti, Mohammad Tahaei — [Alignment Inertia: Auditing the Durability of Training Data Influence Through Policy Override Resistance](http://arxiv.org/abs/2609.27333v1)
  <details><summary>📄 Abstract</summary>
  Platform operators increasingly rely on system prompts and fine-tuning to govern model behavior, yet it remains unclear how reliably these interventions override behavior inherited from prior training. We propose Override Success Rate (OSR) and alignment inertia to measure when operator interventions succeed or fail to change prior behavior. We evaluate zero-shot prompting and LoRA fine-tuning across Llama and Mistral in medical misinformation and hate speech. Alignment inertia persists across b...
  </details>

- **2026-09-23** — Junwon You, Mihyun Jang, Sangwoo Mo et al. — [What Converges in the Platonic Representation Hypothesis? Structure over Geometry](http://arxiv.org/abs/2609.27252v1)
  <details><summary>📄 Abstract</summary>
  The Platonic Representation Hypothesis suggests that increasingly capable models converge toward shared representations. Recent work narrows this claim to shared local neighborhood relationships, finding that capacity-dependent trends in several global similarity measures largely disappear after calibration. We challenge this interpretation by showing that prior local-global comparisons confound structural scale (local versus global) with what is compared: relational structure, defined by which ...
  </details>

- **2026-09-23** — Henan Sun, Zehua Li, Haitao Hu et al. — [DCRL: Decoupling and Coupling Reinforcement Learning via Policy-Reward Manifold Alignment](http://arxiv.org/abs/2609.27572v1)
  <details><summary>📄 Abstract</summary>
  Reinforcement learning (RL) has emerged as a key paradigm for improving the reasoning capabilities of large language models (LLMs). However, existing reward systems, such as rule-based and reward-model-based, often exhibit issues such as unstable optimization and reward hacking. In this work, we revisit the general reasoning of LLMs from a geometric perspective, conceptualizing it as a coupled manifold composed of three interdependent sub-manifolds: logical deduction, evaluation, and representat...
  </details>

- **2026-09-23** — Jie Yang, Yan Zheng, Jiarui Sun et al. — [TimeEvo: Failure-Driven Self-Evolution of a Time Series Agent](http://arxiv.org/abs/2609.27277v1)
  <details><summary>📄 Abstract</summary>
  Time series agents answer analytical questions by calling external tools, and which tools they carry is decided by people before the agent runs. However, we identify two failures in this setup. Human-Agent Tool Misalignment: a library of 21 expert-curated tools helps on some tasks and hurts on others, dropping anomaly accuracy under every backbone we test. Silent Harm: one round of generic self-revision changes 147 answers and breaks 56 of them, while the final score moves by less than a point. ...
  </details>

- **2026-09-22** — Yukta Pareek, Yasaman Masoudi, Satadru Dey — [Merging Large Language Models and Battery Physics for User-Aware Electric Vehicle Driving Management](http://arxiv.org/abs/2609.27050v1)
  <details><summary>📄 Abstract</summary>
  Electric vehicle (EV) battery performance is strongly coupled with driver behavior, yet human intent is typically expressed semantically rather than numerically. This paper proposes a hybrid physics-artificial intelligence framework that integrates a Large Language Model (LLM) as a high-level behavioral reasoning layer within a physics-driven supervisory architecture. The LLM interprets textual user intent and structured battery feedback to generate bounded behavioral parameters that shape a dis...
  </details>

- **2026-09-22** — Ruike Cao, Fugen Yao, Liang Dong et al. — [COPE: Continual Personalization of LLMs under Sparse User Feedback via User Embeddings and Self-Evaluation](http://arxiv.org/abs/2609.26853v1)
  <details><summary>📄 Abstract</summary>
  While Large Language Models (LLMs) have achieved remarkable results across various benchmarks, their alignment with normative values often results in homogenized responses that fail to address diverse user preferences. Existing training-free methods often occupy valuable context windows through prompt engineering, while training-based methods typically remain static post-training, failing to support the continual optimization required in real-world settings. To address these challenges, we propo...
  </details>

- **2026-09-22** — Han Chen, Hanchen Wang, Hongmei Chen et al. — [HYDRA: Proactive Android Malware Drift Adaptation via Hierarchical Graph Contrastive Learning](http://arxiv.org/abs/2609.26352v1)
  <details><summary>📄 Abstract</summary>
  Concept drift, driven by the rapid evolution of Android malware, severely degrades the performance of machine learning detectors. Current adaptation strategies are often reactive, responding only after performance has dropped and imposing a significant manual annotation burden, or they are proactive but rely on unstable adversarial training and incomplete, single-level graph representations. To overcome these limitations, we propose HYDRA (Hybrid Drift Adaptation), a proactive adaptation framewo...
  </details>

- **2026-09-22** — Shufan Sun, Chen Wang, Enxin Song et al. — [HARMONY: Hierarchical Agentic Reasoning for MONocular Image-to-Scene Synthesis](http://arxiv.org/abs/2609.26793v1)
  <details><summary>📄 Abstract</summary>
  Compositional 3D scene reconstruction has recently been explored from two directions: agentic reasoning that provides semantic understanding of spatial relationships but lacks precise alignment with input images; and visual geometry foundation models that predict dense point maps from input images but the reconstruction quality is limited. Therefore, recovering a complete 3D scene from a single monocular image with accurate inter-object relationships and high-fidelity reconstruction quality rema...
  </details>

- **2026-09-22** — Fang Wang, Huitao Li, Wenhan Chao et al. — [GAD-MambaUNet: Direction-Group Mamba with Gradient-Adaptive DINOv3 Distillation for Lightweight Medical Image Segmentation](http://arxiv.org/abs/2609.26729v1)
  <details><summary>📄 Abstract</summary>
  In this paper, we proposed GAD-MambaUNet, a lightweight medical image segmentation network that combines efficient local modeling, direction--group state-space interaction, and training-time foundation-model supervision. To improve contextual modeling in compact segmentation networks, we introduced Direction-Group Graph Selective Scan (DG-GSS), which treated scan-direction and channel-group responses as graph nodes and enabled structured information exchange before multi-directional fusion. We f...
  </details>

- **2026-09-22** — Xiaoyu Yang, Jie Lu, Wei Duan et al. — [The Sirens' Song: When Proximal Background Context Overshadows Distant Evidence](http://arxiv.org/abs/2609.26718v1)
  <details><summary>📄 Abstract</summary>
  Long-context LLMs focus on retrieving distant evidence from extensive context, yet existing work has largely focused on overcoming distance alone. In this work, we identify the Proximity Trap, insufficient attention to distant evidence often arises less from distance itself than from cumulative competition with abundant, task-irrelevant proximal background. To address the Proximity Trap, we introduce LYRA (Long-context heavY-tailed Relevance Alignment), a t-distributed directional matching mecha...
  </details>

- **2026-09-22** — Fiona Kekwick, Matthew Baugh, Bernhard Kainz et al. — [MMAP: Multimodal Missing-Aware Pretraining for Longitudinal Alzheimer's Prediction](http://arxiv.org/abs/2609.26617v1)
  <details><summary>📄 Abstract</summary>
  Clinical decision making heavily relies on predicting the disease progression trajectory by seeking to understand patient's health status which is characterised by multimodal medical data. AI holds great potential for learning useful representations from multimodal medical data to predict disease progression and aid clinical decision making. However, development of predictive AI models is constrained by missing modalities and incomplete tabular data frequently occurring in medical datasets. In a...
  </details>

- **2026-09-22** — Lorenzo Zangari, Davide Picca — [A Semiotics-Aware Framework for Evaluating Fidelity and Coverage in Natural Language Generation](http://arxiv.org/abs/2609.26527v1)
  <details><summary>📄 Abstract</summary>
  When two texts describe the same expression, standard metrics based on lexical overlap or whole-text similarity may fail to detect meaningful differences in how that expression is framed. We propose a framework to evaluate semiotic alignment between texts, where a semiotic profile encompasses both the contextual meaning and the discourse references made salient by a text. Our approach yields two scores, Semiotic Fidelity and Semiotic Coverage, estimating how much of one text's profile is support...
  </details>

- **2026-09-22** — Mario Sanz-Guerrero, Katharina von der Wense — [Calibration as a First-Class Criterion in LLM Evaluation](http://arxiv.org/abs/2609.26489v1)
  <details><summary>📄 Abstract</summary>
  Calibration of language models -- the alignment between expressed or implicit confidence and empirical correctness -- is a well-studied subfield within NLP. Methods to measure it already exist. The problem is adoption: outside this subfield, NLP research regularly introduces new models, datasets, and benchmarks without checking whether the model's confidence scores are meaningful. We argue that this adoption gap is a major obstacle to trustworthy LLM evaluation. Miscalibration causes problems in...
  </details>

- **2026-09-22** — Junlong Wu, Zijun Li, Yuting Hu et al. — [KwaiMind Technical Report](http://arxiv.org/abs/2609.26375v1)
  <details><summary>📄 Abstract</summary>
  Commercial image editing requires product identity preservation, accurate text rendering, and user appeal alongside general editing quality. We present KwaiMind, an image editing system combining general capabilities with e-commerce specialization. An agent-based data engine maintains approximately 1.8 million high-quality editing pairs. Built on a multimodal diffusion transformer, KwaiMind undergoes continued pre-training and supervised fine-tuning, followed by preference optimization and onlin...
  </details>

- **2026-09-22** — Jiayan Fu, Hang Xu, Yong Zhang et al. — [PACT: From Credit Assignment to Critic Alignment](http://arxiv.org/abs/2609.26355v1)
  <details><summary>📄 Abstract</summary>
  Reinforcement learning has become a central component of large language model (LLM) post-training, yet token-level credit lacks a generally accepted mathematical definition, leaving its relationship to commonly used training signals unclear. We formulate three regularity conditions, namely Completeness, Prefix Consistency, and Neutrality, and prove that they uniquely determine token-level credit. This characterization provides a unified basis for explaining phenomena across existing algorithms a...
  </details>

- **2026-09-22** — Masoud Soleimani — [Target alignment, dilution and forecast selection when cross-sectional forecasts share a common target](http://arxiv.org/abs/2609.26303v1)
  <details><summary>📄 Abstract</summary>
  Forecasters often score the same units per date against one standardized realized outcome. We show that every standardized forecast splits exactly into a component aligned with this common target and a component uncorrelated with it. Three consequences follow: forecast-error correlation largely mirrors forecast correlation and is therefore a poor measure of diversity; an equally weighted combination beats a no-information forecast only when average alignment is large relative to the combination'...
  </details>

- **2026-09-22** — Yan Zhang, Pei Fu, Daiqing Wu et al. — [Towards Omni-dimensional GUI Agent Navigation with Masked Trajectory Prediction](http://arxiv.org/abs/2609.25769v1)
  <details><summary>📄 Abstract</summary>
  Graphical User Interface (GUI) Agents autonomously interact with software to fulfill user requests, where GUI navigation stands out as the most critical and challenging capability. Mastering this capability demands a complex synergy of step-wise decision-making, state-action alignment, and long-horizon planning. While directly mixing these corresponding navigation tasks seems intuitive to simultaneously acquire these skills, such a direct combination is severely bottlenecked by inconsistent opti...
  </details>

- **2026-09-22** — Rojin Ziaei — [The Limits of Simulated Societies: How Post-Training and Survey Fine-Tuning Erase Cross-Cultural Variance](http://arxiv.org/abs/2609.25760v1)
  <details><summary>📄 Abstract</summary>
  Using large language models (LLMs) to simulate diverse human populations has the potential to transform many aspects of computational social science, yet many evaluations score the average response rather than the spread of opinion within real groups. Here, we develop a diagnostic framework that measures point accuracy alongside dispersion retention, the ratio of predicted to human standard deviation ($\dr$), on 10{,}000 respondent--question pairs from the World Values Survey (WVS) spanning twel...
  </details>

- **2026-09-22** — Dingkang Yang, Yizhou Liu, Wendong Cheng et al. — [Fysiverse-3D-Vision Technical Report: Generating Executable 3D Worlds from Images through Unified Spatial Reasoning](http://arxiv.org/abs/2609.25741v1)
  <details><summary>📄 Abstract</summary>
  Generative models have advanced image-conditioned 3D content creation, yet generating controllable and executable 3D scenes from a single image remains challenging. Existing 3D generative approaches can synthesize visually plausible objects and scenes, but their spatial layout estimation is coupled with specific asset generators. They struggle to jointly model object semantics, metric geometry, and scene-level spatial relationships, which are essential for interactive editing, physical simulatio...
  </details>

- **2026-09-22** — Adam Ousherovitch, Ambuj Tewari — [Direct Optimization of Generators for Search in Automated Theorem Proving](http://arxiv.org/abs/2609.25575v1)
  <details><summary>📄 Abstract</summary>
  Fine-tuned Large Language Models (LLMs) significantly advance Automated Theorem Proving (ATP), but are often deployed as guiding policies within tree search rather than for single-attempt generation. Recent work shows cross entropy is suboptimal for an LLM used in flat search strategies such as aggregation or filtering and that work has developed new loss functions to correct this misalignment. Extending this alignment to tree search is more challenging: proof discovery depends on exploration an...
  </details>

- **2026-09-22** — Jinu Pahk, Jesoon Kang, Taegeon Park et al. — [HABILIS Brain 0: Geometry-Change Supervision for Vision-Language-Action and Residual Flow Recovery](http://arxiv.org/abs/2609.25558v1)
  <details><summary>📄 Abstract</summary>
  Vision-language-action policies benefit from geometric supervision, but current-frame geometry alone does not explicitly describe the changes associated with manipulation. This design is motivated by the goal of learning an embodiment-agnostic visual interface that can be pretrained across robot and egocentric video before robot-specific action alignment. We introduce Geometry-Change VLA (GC-VLA), which learns to predict multiview future-current geometry-change tokens from current observations. ...
  </details>

- **2026-09-22** — Dhruv Srikanth, Bingchen Zhao, Dixing Xu et al. — [Recursive self-improvement of AI research agents](http://arxiv.org/abs/2609.26457v1)
  <details><summary>📄 Abstract</summary>
  AI agents are beginning to automate research and development across the AI stack, from improving training efficiency to optimizing inference. A natural next step is to improve the research efficiency of the agents themselves. When an AI research agent's own code is the object of optimization, each accepted rewrite becomes the agent that the next round edits. We refer to this loop as recursive self-improvement. Its significance lies in a long-standing trend, in which increased cumulative spending...
  </details>

- **2026-09-21** — Chankyo Kim, Minghan Zhu, Tzu-Yuan Lin et al. — [GINIO: A Geometric SO(3)-Equivariant Interface for Neural Inertial Odometry](http://arxiv.org/abs/2609.25338v1)
  <details><summary>📄 Abstract</summary>
  Neural inertial odometry increasingly uses networks as learned measurements inside filtering pipelines. Such measurements should transform consistently under arbitrary IMU mounting conventions: their mean must transform as a vector, and their covariance must transform congruently as a second-order tensor. We present GINIO, a geometric SO(3)-equivariant interface for neural inertial odometry under arbitrary rotations of the IMU measurement frame. Given calibrated IMU windows, our framework predic...
  </details>

- **2026-09-21** — Yusser Al Ghussin, Eva Gavaller, Cristina España-Bonet et al. — [FineWeb-CLaR: Culture, Language, and Region Annotations for Benchmark-Aligned Corpus Auditing](http://arxiv.org/abs/2609.25298v1)
  <details><summary>📄 Abstract</summary>
  Cultural evaluation coverage and robustness in language models are difficult to diagnose because pretraining corpora and cultural benchmarks are rarely indexed with comparable metadata. Benchmarks increasingly target culturally situated phenomena at the level of languages, regions, and locale-specific practices, while web-scale corpora are usually organized only by language. A shared culture-language-region layer makes these resources comparable, enabling audits of whether a target cultural phen...
  </details>

- **2026-09-21** — Jeongah Lee, Joy Qiuyue Zhong, Drishti Goel et al. — [Can LLMs identify and repair ruptures? Comparison between clinician practices and LLM behaviors](http://arxiv.org/abs/2609.25287v1)
  <details><summary>📄 Abstract</summary>
  Ruptures represent common albeit critical moments in interaction where relational alignment breaks down, making them essential for evaluating AI where trust and engagement matter most. In a scenario-driven empirical study, we examined the performance of three LLMs at identifying and resolving ruptures across 21 mental health conversations and 22 experts' evaluation of the strategies. For identification, LLMs relied on explicit linguistic cues within single turns whereas experts integrated implic...
  </details>

- **2026-09-21** — Wenqing Wang, Haitao Xiang, Xinyi Zhao et al. — [FinFIRST: Benchmarking Search Agents for Financial Information Retrieval, Sourcing and Traceability](http://arxiv.org/abs/2609.25192v1)
  <details><summary>📄 Abstract</summary>
  Financial search is a highly demanding task for LLM agents, requiring not only a correct final answer but also temporally valid information retrieval, authoritative source selection, entity and period alignment, unit and definition consistency, and verifiable evidence for all conclusions. Existing benchmarks predominantly evaluate only the final answer, making it difficult to localize errors or assess whether an answer is well-founded. To address this gap, we introduce FinFIRST (Financial Inform...
  </details>

- **2026-09-21** — Xiaoqiang Lu, Licheng Jiao, Lingling Li et al. — [0.5%>100%: Bidirectional Reciprocal Learning for Referring Image Segmentation](http://arxiv.org/abs/2609.24510v2)
  <details><summary>📄 Abstract</summary>
  Recent advances in vision foundation models (VFMs) have shown remarkable capabilities across diverse unimodal visual tasks. However, adapting VFMs to referring image segmentation (RIS) typically necessitates precise vision-language alignment via full fine-tuning, incurring substantial computational overhead and risking catastrophic forgetting. While existing parameter-efficient fine-tuning (PEFT) methods enable safe knowledge transfer with minimal training costs, they predominantly operate indep...
  </details>

- **2026-09-21** — Lei Yang, Mengyin Liu, Jia Wang et al. — [onPanda: Efficient Annotation of On-Policy Alignment Data for LLMs and Agents via Token-Level Correction](http://arxiv.org/abs/2609.24983v1)
  <details><summary>📄 Abstract</summary>
  We present onPanda, an interactive tool for efficiently annotating LLM alignment data and agent trajectories. onPanda adopts token-level correction as its core interaction: while reading a model response, the annotator locates the first inappropriate token and either picks a substitute from the model's candidate tokens or types the correct text via free-form editing. The system then truncates everything after that position and continues generation from the corrected prefix, repeating this locate...
  </details>

- **2026-09-21** — Manjiang Yu, Hongji Li, Zihan Wang et al. — [The Answer-Basin Representation Hypothesis: We Are Not Probing or Steering Concepts](http://arxiv.org/abs/2609.24821v1)
  <details><summary>📄 Abstract</summary>
  The Linear Representation Hypothesis associates high-level concepts with directions in language models, but it remains unclear how these concept-related linear structures are organized within the model. We propose the Answer-Basin Representation Hypothesis: the probability measure induced over answers by the model's continuation distribution organizes these linear structures, with its statistics represented along linear directions shared across questions. All continuations yielding the same answ...
  </details>

- **2026-09-21** — Sungheon Jeong, Sanggeon Yun, Ryozo Masukawa et al. — [World State Generator](http://arxiv.org/abs/2609.24744v1)
  <details><summary>📄 Abstract</summary>
  Language agents solve complex tasks through plans and actions. A single step the world refuses puts the goal out of reach, and what the agent does next decides the task. Prompted planners fail at exactly this point, rewriting the refused step in new words, meeting the same refusal, and burning the attempt budget without moving. They fail because the plan was never tied to the world, so a refusal has nothing in the plan to attach to. A world is where a task runs, and it has its own rules, its own...
  </details>

- **2026-09-21** — Zelin Peng, Zhengqin Xu, Changsong Wen et al. — [HyperCLIP++: Fine-tuning CLIP forOpen-vocabulary Semantic Segmentation in Hyperbolic Space](http://arxiv.org/abs/2609.24564v1)
  <details><summary>📄 Abstract</summary>
  CLIP, a foundational vision-language model, has emerged as a powerful tool for open-vocabulary semantic segmentation. While freezing CLIP's text encoder is known to preserve its generalization capability, recent studies show that fine-tuning both CLIP's text and image encoders jointly significantly enhances segmentation performance, especially for classes from open sets. In this work, we explain this phenomenon from the perspective of hierarchy alignment, since during fine-tuning, the hierarchic...
  </details>

- **2026-09-21** — Ahmed Aboelela, Johannes Barcsay, Jana Friedhof et al. — [Evaluating Transformation Models for pCLE Mosaic Registration](http://arxiv.org/abs/2609.24560v1)
  <details><summary>📄 Abstract</summary>
  Confocal Laser Endomicroscopy (CLE) provides real-time, cellular-resolution optical biopsy but has a narrow field of view, which image mosaicing can extend to provide anatomical context. Because of line-by-line acquisition, probe motion, and probe-tissue interaction, frame alignment generally requires a non-linear transformation whose accuracy is difficult to quantify: flexible transformation models can fit intensity features and noise, so appearance-based metrics such as Normalized Cross-Correl...
  </details>

- **2026-09-21** — Xin Liu, Yunhai Li, Chunfu Jia et al. — [Construting Reverse Thinking: Developing Large Language Models' Reverse Thingking Ability](http://arxiv.org/abs/2609.24760v1)
  <details><summary>📄 Abstract</summary>
  When facing complex problems, humans tend to try various ideas for different issues. Human thinking patterns exhibit remarkable flexibility in adapting to diverse scenarios. GPT-o1, GPT-o3, and DeepSeek-R1 adopt long chain-of-thought models to address complex problems by increasing reasoning depth, which default to a forward reasoning mode. We conducted statistical analysis on the accuracy of different mathematical problem datasets on models of different scales, and found five reasons for errors...
  </details>

- **2026-09-21** — Huan Liao, Haonan Han, Xingwen Han et al. — [CycleSpeech: Reciprocal Alignment for Instruction-Controlled Speech Synthesis and Paralinguistic Understanding](http://arxiv.org/abs/2609.24771v1)
  <details><summary>📄 Abstract</summary>
  Instruction-controlled speech synthesis and paralinguistic understanding are often trained independently, leaving reciprocal feedback between the two tasks underexplored. We introduce CycleSpeech, a framework that connects generation and understanding through a shared, structured voice profile that serves as a common target for supervision and reciprocal feedback. The forward cycle assesses whether synthesized speech expresses the intended attributes by comparing recovered and target profiles. T...
  </details>

- **2026-09-21** — Zhenghua Ma, Xinpan Meng, Zeyu Liu et al. — [InsertAnything: Generalizable Contact-Rich Precision Insertion from Simulation to Reality](http://arxiv.org/abs/2609.24511v1)
  <details><summary>📄 Abstract</summary>
  Contact-rich precision insertion is a key manipulation skill in robotic assembly. Tight clearances make insertion more sensitive to alignment errors and prone to collisions and jamming, while variations in geometry and clearance across parts further complicate policy reuse. We present a reinforcement learning framework that trains insertion policies entirely in simulation for direct deployment without real-world demonstrations or policy fine-tuning. By combining target poses with compact three-d...
  </details>

- **2026-09-21** — Xiaoqiang Lu, Licheng Jiao, Lingling Li et al. — [0.5\%>100\%: Bidirectional Reciprocal Learning for Referring Image Segmentation](http://arxiv.org/abs/2609.24510v1)
  <details><summary>📄 Abstract</summary>
  Recent advances in vision foundation models (VFMs) have shown remarkable capabilities across diverse unimodal visual tasks. However, adapting VFMs to referring image segmentation (RIS) typically necessitates precise vision-language alignment via full fine-tuning, incurring substantial computational overhead and risking catastrophic forgetting. While existing parameter-efficient fine-tuning (PEFT) methods enable safe knowledge transfer with minimal training costs, they predominantly operate indep...
  </details>

- **2026-09-21** — Rithin Nagaraj, Rupa Laalasa Oruganti, Prerna Subhashchandra Kunder et al. — [Comparing Latent Concept Formation in State Space Models and Transformers via Sparse Autoencoders](http://arxiv.org/abs/2609.24440v1)
  <details><summary>📄 Abstract</summary>
  The quadratic scaling of Transformer self-attention has driven the adoption of sub-quadratic Selective State Space Models (SSMs) like Mamba, which compress past context into a fixed-size recurrent hidden state. This strict informational bottleneck raises a foundational question for mechanistic interpretability: do SSMs and Transformers learn fundamentally distinct latent representations? In this work, we employ Sparse Autoencoders (SAEs) to conduct a large-scale, feature-level correspondence ana...
  </details>

- **2026-09-21** — Vasileios Arampatzakis, Vasileios Sevetlidis, George Pavlidis — [Prescriptive SVD-Inspired Attention via Spectral Energy Retention](http://arxiv.org/abs/2609.24370v1)
  <details><summary>📄 Abstract</summary>
  Self-attention is central to modern Transformer architectures, but its dense dot-product formulation makes it difficult to identify which internal directions are structurally important and which can be modified without disrupting the model. SVD-Inspired Attention (SVDA) addresses part of this problem by introducing a learned diagonal spectrum into the query-key score interaction, making latent attention directions explicitly inspectable through indicators such as spectral entropy, effective rank...
  </details>

- **2026-09-21** — Linhan Luo, Lequan Lin, Dai Shi et al. — [SupportCal: Label-Free Calibration of Post-Trained LLMs via Reference Support and Corroboration](http://arxiv.org/abs/2609.24303v1)
  <details><summary>📄 Abstract</summary>
  Post-training often improves task performance but can degrade confidence calibration, leaving post-trained language models (PoLMs) more overconfident than their corresponding pretrained language models (PLMs). Because task-specific labeled calibration data can be costly or unavailable, the corresponding pretrained PLM provides a natural label-free reference for post-hoc calibration. Prior agreement-gated PLM-referenced calibration fits a scalar temperature using only examples on which the PoLM a...
  </details>

- **2026-09-21** — Tresor Y. Koffi, Amel Hidouri, Corentin Legrand et al. — [DiaSeg: Diagonal Segment Extraction from DTW Paths for Interpretable Gait Analysis](http://arxiv.org/abs/2609.24223v1)
  <details><summary>📄 Abstract</summary>
  Dynamic Time Warping (DTW) is the dominant approach for measuring similarity between time series, yet standard practice discards the optimal warping path after computing a single distance value, losing local alignment information most relevant to clinical diagnosis. We introduce DiaSeg, a framework that extracts diagonal segments from DTW paths with controlled breaks, characterizing each segment by five geometric features (effective length, interruption count, cost variation, temporal position, ...
  </details>

- **2026-09-21** — Minglang Li, Yueyue Fang, Xieping Gao — [Beyond Emotion Prompts: Fine-Grained Text-to-Image Generation Driven by Valence-Arousal-Dominance](http://arxiv.org/abs/2609.24215v1)
  <details><summary>📄 Abstract</summary>
  Although text-to-image models can accurately depict subjects and scenes, creators still struggle to specify the fine-grained emotions an image should convey without rewriting its content description. Natural language can suggest emotions, but it offers no control scale with stable meanings and ordered intensities. We propose EMOTRANS, which transforms psychologically grounded valence-arousal-dominance (VAD) coordinates into generation conditions that are independent of the content text and modul...
  </details>

- **2026-09-21** — Lijian Wu, Henry Hengyuan Zhao, Zijian Zhang et al. — [ChartJudgeBench: Evaluating LMM Judges for Chart-to-Code Generation](http://arxiv.org/abs/2609.24210v1)
  <details><summary>📄 Abstract</summary>
  Building strong chart-to-code systems increasingly relies on reinforcement learning, whose effectiveness depends critically on the quality of the reward signal. Large Multimodal Models (LMMs) play a natural critical role in jointly assessing chart visual appearance and task requirements. They are therefore increasingly used as visual critics and reward models, yet their reliability as judges remains largely unexplored. To this end, we introduce ChartJudgeBench, a diagnostic vision-language bench...
  </details>

- **2026-09-21** — Chenming Shang, Yujin Tang, Jun Jie Ou Yang et al. — [Displacement Geometry Captures Platonic Shared Reality Across Models and Modalities](http://arxiv.org/abs/2609.24209v1)
  <details><summary>📄 Abstract</summary>
  The Platonic Representation Hypothesis (PRH) claims that independently trained models converge on a shared statistical model of reality, yet recent work finds only weak pointwise similarity between models. In this paper, we show that what models share is not the location of samples in representation space, but the directions (displacement vectors) between them. Under a single orthogonal alignment--rotation and reflection only--these displacement vectors are substantially preserved across 44 inde...
  </details>

- **2026-09-21** — Jingkun Liu, Yue Song — [Opinion Leader Dynamics: How Sparse Attention Shapes Token Clustering](http://arxiv.org/abs/2609.24202v1)
  <details><summary>📄 Abstract</summary>
  Sparse attention reduces the quadratic cost of global self-attention while retaining strong empirical performance, but how its restricted interactions shape the evolution of token representations remains theoretically underexplored. Modeling tokens as particles on the unit sphere, we introduce opinion leader dynamics, a framework that identifies two mechanisms through which token groups converge internally while maintaining distinct limiting directions. In the explicit model, fixed representativ...
  </details>

- **2026-09-21** — Daein Weon, Dongho Kang — [When Residualization Helps an Audit: Format Effects, Slice Gains, and Their Limits](http://arxiv.org/abs/2609.24194v1)
  <details><summary>📄 Abstract</summary>
  Evaluation scores used around LLM systems -- including reward models, rerankers, and LLM judges -- can track surface form instead of the quality they claim to measure. When presented with a terse correct solution and a commented buggy solution for the same MBPP problem, a public preference reward model selects the correct one no better than a coin flip (0.507). Subtracting the predictable surface component from such scores is increasingly common, but removal alone does not yield a more valid mea...
  </details>

- **2026-09-21** — Jiayi Liang, Xiaotian Gu, Xinyu Xie et al. — [TAC-Time: Texts as Channels For Multimodal Time Series Forecasting](http://arxiv.org/abs/2609.24156v1)
  <details><summary>📄 Abstract</summary>
  Most existing time series forecasting methods rely solely on numerical observations, overlooking rich contextual information from auxiliary texts. Recent multimodal approaches attempt to incorporate textual signals, but they often treat text as static features or use large language models as forecasting backbones, limiting their ability to capture temporal dynamics and increasing computational cost. To address these challenges, we propose TAC-Time, a unified framework that transforms textual inf...
  </details>

- **2026-09-21** — Quanxing Xu, Ling Zhou, Xian Zhong et al. — [A$^2$Safe: Counterfactual Evidence-Aligned Adaptive Agent Collaboration for Safe and Effective Visual Question Answering](http://arxiv.org/abs/2609.24098v1)
  <details><summary>📄 Abstract</summary>
  Visual Question Answering (VQA) with Multimodal Large Language Models (MLLMs) requires not only producing safe and effective responses, but also grounding safety decisions in the multimodal evidence that determines risk. Recent safety-alignment methods improve refusal behavior and contextual risk awareness, yet correct safety outcomes may still rely on superficial textual or visual correlations, particularly when risk emerges from interactions between individually benign image and question conte...
  </details>


### 📂 robustness
*鲁棒性与可靠性 / Robustness & Reliability* — 78 papers

- **2026-09-23** — Oswin So, Eric Yu, Chuchu Fan — [LEAP-CBF: A Safety Filter for Uncertain Systems with Least-Effort Adversarial Potentials](http://arxiv.org/abs/2609.28364v1)
  <details><summary>📄 Abstract</summary>
  Control barrier functions (CBF) are a popular safety filter to ensure safety for nonlinear dynamical systems. However, when the system is subject to uncertainties and disturbances, this requires the use of robust variants of CBFs, which can be difficult to construct and can be overly conservative, especially for high-dimensional systems under input constraints. In this work, we propose a new approach to solve these challenges by introducing Least-Effort Adversarial Potentials (LEAP), a certifica...
  </details>

- **2026-09-23** — Yuxuan Li, Will Epperson, Wesley Deng et al. — [CAVEAT: Towards Robust Computer-Use Agents in Incentive-Misaligned Environments](http://arxiv.org/abs/2609.27273v1)
  <details><summary>📄 Abstract</summary>
  Computer-use agents (CUAs) increasingly act on behalf of users online. What happens when the environments they operate in have incentives that do not align with the user's? In online marketplaces, for example, platforms may favor some products over others, potentially steering agents away from the user's objective. Existing CUA benchmarks cover cooperative settings or explicit attacks, but do not test whether agents preserve user objectives when the environment itself has a stake in the outcome....
  </details>

- **2026-09-23** — Jiaxing Li, Lei Song, Rui Dong et al. — [Learning from Failures: Heterogeneous Graph Memory for Small Language Model Tool-Using Agents](http://arxiv.org/abs/2609.28003v1)
  <details><summary>📄 Abstract</summary>
  Small and medium-sized language models offer cost-effective executors for tool-using agents, making them attractive for local and large-scale deployment. However, in long-horizon and stateful environments, they often make structural errors such as missing required observations, performing premature writes, repeating failed calls, and violating action preconditions. These errors can lead to incorrect state updates, policy violations, and costly or irreversible consequences, making reliable tool e...
  </details>

- **2026-09-23** — Akash Samanta, Manish Pratap Singh, Debasis Chaudhuri — [Hidden not Deleted: How Networks Suppress Entangled Features](http://arxiv.org/abs/2609.27593v1)
  <details><summary>📄 Abstract</summary>
  Concept erasure methods that operate via linear projection assume that features occupy separable subspaces. We show this assumption fails under dense superposition: when two features are forced into an antipodal pair sharing a single subspace, state-of-the-art linear erasure destroys both, not just the target. Networks trained with gradient descent instead solve this problem non-linearly, but not uniformly: they converge to one of two distinct circuit-level solutions depending on initialization,...
  </details>

- **2026-09-23** — Jialu Wang, Jianing Deng, Shuqing Luo et al. — [Quantization-Robust Unlearning through the Lens of Retain-Forget Loss Landscapes Interaction](http://arxiv.org/abs/2609.27355v1)
  <details><summary>📄 Abstract</summary>
  Unlearning ensures LLM compliance by removing the influence of private or copyrighted training data. However, since LLM models typically undergo post-training compression, like quantization, in practical deployment, it has been observed that the unlearning effect can be substantially weakened, with the forgetting behavior degrading more severely than that of model utility. This paper proposes a quantization-robust unlearning framework that makes forgetting robust to quantization while maintainin...
  </details>

- **2026-09-23** — Jiajie Zhang, Yankai Xiang, Changhao Chen — [Memory That Changes Action Is Not Memory That Guides It: Counterfactual Auditing of History-Conditioned Robot Policies](http://arxiv.org/abs/2609.27247v1)
  <details><summary>📄 Abstract</summary>
  A robot returning a block to its origin tray may encounter two task-consistent pasts that reconverge to the same current input but warrant different actions. Yet memory-policy evaluations often rely on task success or action change under memory perturbation, neither of which establishes that memory guides the decision. We propose the \textbf{Counterfactual Memory Audit (CMA)}, an evaluation protocol that crosses two histories at a verified-identical present, queries a frozen policy under common ...
  </details>

- **2026-09-23** — Vaishnavi Jagabathula, P Sangeerth, Pushpak Jagtap — [Tractable Reinforcement Learning for Full Class of Signal Temporal Logic Specifications Using Spatiotemporal Tube Reward](http://arxiv.org/abs/2609.28396v1)
  <details><summary>📄 Abstract</summary>
  This paper addresses the control problem for robotic systems, including non-holonomic and underactuated platforms operating under unknown dynamics and strict actuator limits to satisfy complex high-level specifications. We denote these high-level specifications using Signal Temporal Logic (STL) and propose a novel time-aware Reinforcement Learning (RL) framework that leverages the geometric properties of Spatiotemporal Tubes (STTs). While traditional analytical STT controllers often struggle to ...
  </details>

- **2026-09-23** — Zanyi Wang, Yuheng Lei, Dengyang Jiang et al. — [Beyond Future Prediction: Denoising as Generative Adaptation for Robot Control](http://arxiv.org/abs/2609.28339v1)
  <details><summary>📄 Abstract</summary>
  Pretrained generative Diffusion Transformers (DiTs) capture rich pixel-level visual and language-conditioned structure through large-scale image and video generation training. A growing line of robot policies builds on this generative prior, but how it should be transferred to control remains unclear, and existing approaches commonly instantiate this transfer through future visual prediction. We ask a more basic question: what a pretrained generative DiT actually contributes to action learning, ...
  </details>

- **2026-09-23** — Ilán Carretero, Pablo Meseguer, Rocío del Amor et al. — [Do Center Biases Propagate? Robustness of Pathology Foundation Models in Whole-Slide Image Classification](http://arxiv.org/abs/2609.28231v1)
  <details><summary>📄 Abstract</summary>
  Pathology foundation models (PFMs) have transformed computational pathology through powerful representation learning from histopathological images. PFMs provide rich, discriminative representations for whole slide image (WSI) analysis, enabling tasks such as slide-level classification under multiple instance learning (MIL). However, these representations may also encode non-biological signals associated with acquisition centers, potentially introducing spurious shortcuts into downstream predicti...
  </details>

- **2026-09-23** — Yiqin Wang, Nuri Cingillioglu, Charles Pert — [Log-Depth Recurrent Language Modeling](http://arxiv.org/abs/2609.28212v1)
  <details><summary>📄 Abstract</summary>
  Language modeling using Transformers has become commonplace despite their fixed computational depth and quadratic runtime with respect to input tokens. Recurrent models on the other hand offer linear depth but no parallel execution. In this work, we extend balanced-tree recursive operators from sequence encoding to autoregressive prediction, enabling all prefix representations to be computed with logarithmic depth and linear runtime. Our experiments provide an initial characterization of this mo...
  </details>

- **2026-09-23** — Gijs van Cuyck, Patric Feldmeier, Jan Tretmans et al. — [Scenario-Driven Neuroevolution: Using Models to Guide Test Generation for Games](http://arxiv.org/abs/2609.28130v1)
  <details><summary>📄 Abstract</summary>
  Automatically generating test inputs for games is challenging, as test generators must master the game to reach advanced program states while also ensuring robustness against the heavy program randomisation inherent to games. The test generator Neatest therefore optimises test suites consisting of neural networks that reach advanced program states and are robust to program randomisation, as they generate test inputs dynamically based on the current program state. Neatest is a white-box testing a...
  </details>

- **2026-09-23** — Weijie Xu, Ming Wang, Ruicheng Ma et al. — [Photonics-GCCE: group collaborative-competitive evolution multi-agent framework for universal and autonomous optical design](http://arxiv.org/abs/2609.28045v1)
  <details><summary>📄 Abstract</summary>
  Large language model (LLM)-empowered photonic agents connect natural-language intents to executable solvers, showing significant advantages over conventional optical design approaches. However, current multi-agent frameworks operate within a collaborative paradigm without extrinsic selective pressure, which could inherit shared blind spots, converge prematurely, and fail to accumulate transferable experience for intricate tasks. Here, we introduce a group photonics collaboration-compete evolutio...
  </details>

- **2026-09-23** — Michael Lawrence Castanares, Princess Ventures, Allan Tan — [Evaluation of pre-trained models for pedagogical assessment of novel AI-assisted educational questions](http://arxiv.org/abs/2609.27749v1)
  <details><summary>📄 Abstract</summary>
  The surge in AI-assisted generation of educational materials has outpaced our capacity to validate their pedagogical quality. Automated evaluation using Bloom Classifier models is a promising approach to assess educational materials at scale. These models show high accuracy within-distribution dataset (IID Dataset). However, applying the same models to new out-of-distribution (OOD) datasets such as AI-assisted generated questions could show performance degradation. To identify robust classifiers...
  </details>

- **2026-09-23** — Mohammad Narimani, Seyyed Ali Emami — [GA-Agent: Large Language Models as Hyperparameter Optimizers for Evolutionary Controller Synthesis](http://arxiv.org/abs/2609.27725v1)
  <details><summary>📄 Abstract</summary>
  Tuning PID controllers to satisfy competing objectives - low tracking error, fast settling, limited overshoot, and moderate control effort - is labor-intensive and requires expertise. Genetic algorithms (GAs) offer gradient-free optimization of controller gains against a weighted fitness function, but success depends on meta-level choices: population size, generation budget, gain bounds, and fitness weights. These are usually set by manual trial-and-error or costly bilevel optimization, exposing...
  </details>

- **2026-09-23** — Jeffrey D. Michler, Kieran Douglas, Anna Josephson — [Mining Meaning: Measurement Error in AI-Assisted Literature Reviews](http://arxiv.org/abs/2609.27686v1)
  <details><summary>📄 Abstract</summary>
  Researchers increasingly use generative AI, particularly large language models (LLMs), to automate tasks across the research pipeline. We study the reliability of these tools at the reading, classification, and synthesis of large bodies of academic literature. We frame LLM-assisted literature reviews as a measurement problem, treating models as measurement systems and tracing how their errors affect downstream conclusions. As a test case, we use three different implementations of ChatGPT to iden...
  </details>

- **2026-09-23** — Sanghee Park, Kee-Eung Kim — [PRISM-VLM: A Multi-Axis Discriminative Benchmark for Compact Vision-Language Models](http://arxiv.org/abs/2609.27395v1)
  <details><summary>📄 Abstract</summary>
  Compact vision-language models (VLMs) now power a growing share of multimodal applications. The benchmarks used to compare them, however, inherit a frontier-centric design: each model is reduced to a single accuracy number, narrowing the inter-model gap on saturated suites and pressing models into low-score bands on harder ones. We introduce PRISM-VLM, a multi-axis discriminative benchmark that scores every item along seven axes covering the recurring failure modes (task quality, behavioral robu...
  </details>

- **2026-09-23** — Saimunur Rahman, Sagun Singh Shrestha, Abdelwahed Khamis et al. — [Automotive mmWave Spinning Radar Place Recognition with Spatially Gated Feature-Correlation Representation](http://arxiv.org/abs/2609.27394v1)
  <details><summary>📄 Abstract</summary>
  Automotive spinning FMCW radar provides dense, $360^\circ$ sensing and remains reliable under poor illumination and adverse weather, making it well-suited to autonomous navigation. Place recognition uses these observations to identify previously visited locations for re-localization and long-term navigation. However, heading changes appear as circular shifts in the polar radar representation, and conventional global aggregation can lose relationships among radar responses that are important for ...
  </details>

- **2026-09-23** — Behnam Ojaghi, Ricard Vilalta, Raul Muñoz — [From Intents to Algorithms: Verified Algorithm Discovery for Transport Networks](http://arxiv.org/abs/2609.27386v1)
  <details><summary>📄 Abstract</summary>
  Intent-based networking decouples desired outcomes from device-level configuration, but most systems still map intents to parameters of an algorithm selected in advance. Large language models (LLMs) create an opportunity to automate algorithm design, yet unrestricted generated code is unsuitable for transport-network control because feasibility, reproducibility, and robustness must be enforced independently of the model. We present VERA-TN, a verification-guided framework that compiles a network...
  </details>

- **2026-09-23** — Mingxiao Li, Wenhai Lai, Hei Victor Cheng et al. — [Single-RF-Chain Multiuser Semantic Communications via Metasurface Modulation](http://arxiv.org/abs/2609.27361v1)
  <details><summary>📄 Abstract</summary>
  Multiuser transmission with multiple radio-frequency (RF) chains enables flexible spatial multiplexing but incurs increased hardware complexity and power consumption. A programmable metasurface (MTS) provides an alternative means of introducing spatial degrees of freedom with a single-RF-chain access point (AP). This paper proposes \emph{Semantic Prism}, an MTS-enabled framework for concurrently transmitting independent semantic messages to multiple users. Semantic Prism jointly maps multiuser s...
  </details>

- **2026-09-23** — To Duy Hinh, Nguyen Le Quoc Anh, Phan Van Tri et al. — [Automated Extraction of Records of Processing Activities (RoPA) Using Hybrid RAG and Locally Deployed Large Language Models](http://arxiv.org/abs/2609.27359v1)
  <details><summary>📄 Abstract</summary>
  Vietnam's Personal Data Protection Law (Law No. 91/2025/QH15) and Decree No. 356/2025/ND-CP, effective January 1, 2026, require organizations to establish and maintain Records of Processing Activities (RoPA). Manual RoPA preparation is labor-intensive, while cloud-hosted large language models (LLMs) may conflict with data-sovereignty requirements. We propose RoPA Manager, a system for automated RoPA information extraction using hybrid retrieval that combines lexical ranking over tsvector, dense-...
  </details>

- **2026-09-23** — Md Tahmid Rahman Laskar, Xue-Yong Fu, Shashi Bhushan TN — [Can One Adapted Model Do It All? Fine-Tuning Strategy Selection for Customer Support LLMs](http://arxiv.org/abs/2609.27262v1)
  <details><summary>📄 Abstract</summary>
  Production customer-support systems often require LLMs to support multiple skills, such as intent classification, question answering, summarization, or tool-use decisions. A central deployment question is whether these skills should be handled by separate task-specialist models or by a single model trained through multi-task training, sequential updates, or model merging. We study this question using thirteen models spanning five families (Qwen3, Qwen3.5, Gemma-3, Llama-3.1, and Mistral) from 0....
  </details>

- **2026-09-22** — Yuhang Jiang — [Median Temporal Ensembling: Training-Free Robust Aggregation for Action-Chunked Visuomotor Policies](http://arxiv.org/abs/2609.27167v1)
  <details><summary>📄 Abstract</summary>
  Action-chunked visuomotor policies predict overlapping trajectories, so every executed action is covered by several predictions. Temporal ensembling smooths execution by combining these predictions with an exponentially weighted mean. One corrupted prediction can move the aggregate without bound: its breakdown point is 0. We use adversarial corruption to stress this deployed aggregator and to compare two kinds of guarantee. A metric guarantee bounds the response to a perturbation of a given size...
  </details>

- **2026-09-22** — Gautham Reddy, Kürşat Tekbıyık, Bryton Petersen et al. — [AI-Enabled Wireless Propagation Modeling and Radio Environment Maps for 5G Aerial Wireless Networks](http://arxiv.org/abs/2609.27083v1)
  <details><summary>📄 Abstract</summary>
  With the gaining prominence of aerial mobility applications, their success depends on the seamless integration of terrestrial and non-terrestrial network connectivity. However, providing reliable connectivity from terrestrial telecommunication networks remains challenging due to multi-cell interference from base stations (BSs) under line-of-sight (LoS) conditions to unmanned aerial vehicles (UAVs), coverage holes caused by antenna sidelobe degradation, localized multipath fading effects, and the...
  </details>

- **2026-09-22** — Youssef Hamdi Zafaan Ibrahim, Mohammed Khalaf Salama — [ACTS: A multi-tier benchmark evaluating LLM cipher identification under controlled blind conditions](http://arxiv.org/abs/2609.26893v1)
  <details><summary>📄 Abstract</summary>
  We introduce ACTS (Artifacts in Cipher Testing Suite), a reproducible benchmark that isolates cryptanalytic ability through tiered metadata deprivation (Tier-1: full metadata; Tier-2: filename only; Tier-3: completely blind) and tests forced reasoning (Tier-5: chain-of-thought, code-as-reasoning, self-correction) on ciphertext alone. A 10-configuration ablation study on 7,000 files, using a single 70/30 train-test split for feature-removal analysis, provides additional evidence at scale. Live AP...
  </details>

- **2026-09-22** — Robert W. Learsch, Nicholas Liesen, Daniel S. Levine et al. — [An open benchmark for machine learning-based polymer property prediction](http://arxiv.org/abs/2609.27036v1)
  <details><summary>📄 Abstract</summary>
  Polymer property prediction lacks open, standardized benchmarks that enable rigorous comparison of machine-learning methods, with existing resources covering only a narrow fraction of polymer architectures, such as homopolymers. We introduce Polymer Benchmark 2026 (PolyBench26), an open dataset comprising nearly 250,000 polymer-property datapoints across eight physical properties, including data from experimental measurements, density functional theory, and molecular dynamics. The benchmark supp...
  </details>

- **2026-09-22** — Qingjing Chen, Junkai Zhang, Shaochun Wang et al. — [LEGO: Synergizing Expert GraphRAG and Expert Chain-of-Thought for Legal Reasoning](http://arxiv.org/abs/2609.27009v1)
  <details><summary>📄 Abstract</summary>
  Large language models are increasingly applied to high-risk domains such as law, yet complex legal reasoning remains limited by two structural challenges. First, existing RAG and GraphRAG methods emphasize lexical or semantic similarity while overlooking normative relations among legal provisions. Second, vanilla Chain-of-Thought prompting may generate plausible rationales without enforcing the normative structure of legal reasoning. To deal with the bottleneck of pipelines in the legal reasonin...
  </details>

- **2026-09-22** — Edem Ahadzi, Ruchi Pandey, Tomi H. Kinnunen — [A Temporal-Envelope Frontend with Learnable Per-Channel Energy Normalization for Whisper-Based Children's ASR](http://arxiv.org/abs/2609.26937v1)
  <details><summary>📄 Abstract</summary>
  Temporal envelopes carry cues critical to speech intelligibility, yet ASR frontends based on log-mel spectrograms do not explicitly model continuous sub-band envelope structure. This limitation is particularly acute for children's speech, where high acoustic variability demands robust feature representations. We propose a modular time-domain frontend that decomposes speech into sub-band envelopes using mel-spaced windowed-sinc filters and the Hilbert transform, with learnable per-channel energy ...
  </details>

- **2026-09-22** — Zeyu He, Zhuqian Zhou, Kirk Vanacore et al. — [Experts Rise Where LLMs Disagree: Using Cross-Model Disagreement to Target Expert Effort in LLM Codebook Revision for Large-Scale Annotation](http://arxiv.org/abs/2609.26926v1)
  <details><summary>📄 Abstract</summary>
  Large-scale text annotation brings expert insight to millions of documents, often through a codebook that AI annotators follow. Developing a robust codebook, however, takes months. Large language models (LLMs) could speed this process by applying an early codebook to the data, surfacing cases with strong LLM disagreement, and eliciting expert feedback to address them. We examined three ways experts can provide feedback for LLM codebook revision: (i) editing LLM-generated revisions driven by cros...
  </details>

- **2026-09-22** — Mengtao Ou, Zongzheng Zhang, Zhenghao Xiao et al. — [MSK-Bench: Benchmarking Full-Body Musculoskeletal Motor Control Across Tasks, Control Paradigms, and Physiological Metrics](http://arxiv.org/abs/2609.26872v1)
  <details><summary>📄 Abstract</summary>
  Musculoskeletal (MSK) humanoids provide a physiologically grounded embodiment for studying full-body motor control, but their high-dimensional muscle actuation, delayed activation dynamics, and redundant muscle--tendon structures make learning substantially harder than torque-driven humanoid control. Existing MSK benchmarks remain fragmented across gait, prosthetics, dexterous hands, or challenge-specific tracks, leaving full-body muscle-actuated control insufficiently evaluated under standardiz...
  </details>

- **2026-09-22** — Sinuo Wang, Zichong Gu, Yuhan Huang et al. — [ForeDrive: Foresight-Guided End-to-End Autonomous Driving with a Planning-Relevant Latent World Model](http://arxiv.org/abs/2609.26299v2)
  <details><summary>📄 Abstract</summary>
  Existing latent world models are typically optimized for future predictability, yet the resulting representations are not necessarily useful for planning in autonomous driving. Predictions are commonly used for pretraining or auxiliary supervision rather than as direct conditioning signals for trajectory generation. We propose ForeDrive, which learns a planning-relevant latent representation and couples it asymmetrically to a Diffusion Transformer (DiT) planner. The planner consumes multi-horizo...
  </details>

- **2026-09-22** — Woojin Chae, Ezinne Nwankwo, Haitong Qin et al. — [Optimal Sequential Annotations for Off-Policy Evaluation](http://arxiv.org/abs/2609.26707v1)
  <details><summary>📄 Abstract</summary>
  Offline reinforcement learning and off-policy evaluation evaluates dynamic treatment rules based on retrospectively collected data prior to deployment. In recent AI applications, state and reward information is recorded as complex text or image, which recent AI advancements such as LLM-as-a-judge can label with unknown bias. Expert annotation may be available but at a higher cost. For example, safety classification via cheap but imperfect classifiers vs. expensive expert review. We show how a li...
  </details>

- **2026-09-22** — Brandon Bauer, Matthew Whalen, Kenji Watanabe et al. — [Autonomous Quantum Transport Measurements of 2D Semiconductors by an AI Agent](http://arxiv.org/abs/2609.26661v1)
  <details><summary>📄 Abstract</summary>
  Artificial-intelligence (AI) agents are beginning to enter experimental laboratories, automating experiments and accelerating scientific discovery. Herein, we introduce an AI-driven workflow in which an AI agent performs multi-step, multi-day quantum transport measurements end-to-end. Specifically, given brief instructions, the agent starts by planning the multi-step measurements, then safely operates the cryogenic instruments, analyzes the data, and concludes with a final report. We demonstrate...
  </details>

- **2026-09-22** — Xiao Tang, Tong Hui, Chao Shen et al. — [Unlocking Cross-Scenario Physical Layer Security: A Mixture-of-Experts Framework with Generative Diffusion Models](http://arxiv.org/abs/2609.26598v1)
  <details><summary>📄 Abstract</summary>
  The future 6G networks are expected to incorporate a proliferation of wireless services in diverse environments, which presents a significant challenge for information security. Conventionally optimization always requires recalculation and learning strategy often suffers poor generalization, which are thus incapable for the security provisioning with wide scenario coverage. In this paper, we propose an adaptive and robust learning framework that leverages a mixture-of-experts (MoE) architecture ...
  </details>

- **2026-09-22** — Zhiyun Jiang, Hanyong Wang, Binbin Liang et al. — [Combining Hierarchical Cognitive Process with Process Supervision for Interpretable Scene Safety Understanding](http://arxiv.org/abs/2609.26399v1)
  <details><summary>📄 Abstract</summary>
  Scene safety understanding plays a life-or-death role in situational awareness in various critical domains. Traditional methods that rely on learning direct mappings between scenes and safety levels often lack interpretability, limiting their reliability in critical applications. An effective approach to overcoming this challenge lies in interpreting human cognitive processes and equipping machine models with analogous cognitive capabilities. This work explores an effective way of integrating sc...
  </details>

- **2026-09-22** — Nikita Agarwal, Nivedit Jain — [FIRE: Failure-Informed Runtime Engineering for Reliable Language-Model Agents](http://arxiv.org/abs/2609.26048v1)
  <details><summary>📄 Abstract</summary>
  Language-model agents often reach a working solution and then fail to consistently deliver it. We study runtime policies: targeted natural-language instructions and action denials applied by the agent harness at states that preceded observed failures, without changing model weights or the user prompt. With this, keeping capability constant, we observe a meaningful unlock in delivered reliability. Across the complete 87-task Terminal-Bench 2.1 suite, with two attempts per task, policies increase ...
  </details>

- **2026-09-22** — Pietro Talli, Petar Popovski, Osvaldo Simeone — [Risk-Aware Online Conformal State Probing](http://arxiv.org/abs/2609.25889v1)
  <details><summary>📄 Abstract</summary>
  AI-based autonomous agents, typically hosted at data centers, must acquire state information from robots or edge devices in order to issue informed control decisions. Managing uncertainty about the state is particularly consequential in safety-critical settings, in which average-case guarantees are insufficient. In this context, we study a sequential decision maker process that jointly decides which actions to take and when to probe given access to an arbitrary state prediction model. We propose...
  </details>

- **2026-09-22** — Hung-Mao Chen, Xu He, Bo Lu et al. — [C-to-Rust Fallacy: Automatic Refactoring != Memory Security](http://arxiv.org/abs/2609.25682v1)
  <details><summary>📄 Abstract</summary>
  Rust has emerged as the leading system programming language, offering strong memory and type safety guarantees without compromising performance. This positions it as a compelling alternative to traditional languages like C and C++, which are susceptible to memory security bugs. However, manually transforming C to Rust requires in-depth domain knowledge of the Rust language features, which requires significant effort for developers. To address this, tools for automatic C-to-Rust refactoring aim t...
  </details>

- **2026-09-22** — Yu Zheng, Qiyu Feng, Yixin Wu et al. — [PhyVisGen: Physically and Visually High-Fidelity Robotic Manipulation Data Generation](http://arxiv.org/abs/2609.25653v1)
  <details><summary>📄 Abstract</summary>
  Large-scale manipulation demonstrations are essential for learning robust visuomotor policies, yet real-world data collection is expensive and difficult to scale. Simulation offers a promising alternative, but physical and visual discrepancies can limit the transferability of synthetic data, particularly for manipulation with soft grippers. We present PhyVisGen, a physically and visually high-fidelity framework for scalable robotic manipulation data generation. On the physical side, PhyVisGen in...
  </details>

- **2026-09-22** — FNU Aditi — [EquivSVA: A Formally Verified Dataset of Behavioral Assertions Across Equivalent RTL Implementations](http://arxiv.org/abs/2609.26751v1)
  <details><summary>📄 Abstract</summary>
  Large language models are increasingly used to generate SystemVerilog Assertions from natural-language specifica- tions and register-transfer-level designs. Existing datasets and benchmarks support important goals such as large- scale training, formal evaluation, specification-to-assertion generation, and mutation-based testing. A complemen- tary need is to study whether a generated assertion cap- tures externally observable behavior or depends on inci- dental details of one RTL implementation. ...
  </details>

- **2026-09-22** — David Torres-Moreno, Jorge Hermosillo-Valadez — [Semantic Abstraction for Natural Language Inference: a Methodological Framework for Discovering and Compensating Semantic Knowledge and Reasoning Gaps in Large Language Models](http://arxiv.org/abs/2609.26610v1)
  <details><summary>📄 Abstract</summary>
  Despite their outstanding performance on many NLP tasks, LLMs face serious challenges related to semantic abstraction. In this study, we are interested in understanding how LLMs leverage abstract semantic knowledge in natural language inference (NLI), which requires sophisticated linguistic capabilities to interpret implicit meanings, contextual conceptual relationships, and semantic connections between words and phrases. To this end, we propose a methodological framework for constructing new se...
  </details>

- **2026-09-22** — Yuan Liang, Sourav Bhattacharjee, Abraham Campbell — [Radiomics-Conditioned Modulation of RenalCLIP Features for Clear Cell Renal Cell Carcinoma Classification](http://arxiv.org/abs/2609.26492v1)
  <details><summary>📄 Abstract</summary>
  Radiomics provides quantitative descriptions of tumour appearance that may complement disease-specific foundation models in small labelled cohorts. We investigate this complementarity for computed tomography-based classification of clear cell renal cell carcinoma. Our framework uses radiomics to modulate RenalCLIP features through feature-wise linear modulation (FiLM), while retaining a direct radiomics contribution. Internal testing and external validation compare it with conventional fusion st...
  </details>

- **2026-09-22** — Sinuo Wang, Zichong Gu, Yuhan Huang et al. — [ForeDrive: Foresight-Guided End-to-End Autonomous Driving with a Planning-Relevant Latent World Model](http://arxiv.org/abs/2609.26299v1)
  <details><summary>📄 Abstract</summary>
  Existing latent world models are typically optimized for future predictability, yet the resulting representations are not necessarily useful for planning in autonomous driving. Predictions are commonly used for pretraining or auxiliary supervision rather than as direct conditioning signals for trajectory generation. We propose ForeDrive, which learns a planning-relevant latent representation and couples it asymmetrically to a Diffusion Transformer (DiT) planner. The planner consumes multi-horizo...
  </details>

- **2026-09-22** — Huatai Zhu, Qiang Chen, Ziqian Kou et al. — [Dual-Frontier: When Can an Agent Trust Its World Model?](http://arxiv.org/abs/2609.26293v1)
  <details><summary>📄 Abstract</summary>
  Learned world models are becoming essential to general-purpose agents: by predicting action consequences, they support planning and decision-making while reducing reliance on costly trial and error. This reliance creates a fundamental ambiguity: when a world-model-guided decision fails, the trajectory alone may not reveal whether the agent's decision rule or the world model caused the loss. We formalize this failure-attribution problem as a counterfactual decomposition of return loss and prove t...
  </details>

- **2026-09-22** — Nada Rahali, Zijia Wang, Zhisong Liu — [Calibration Is Not Verification: Falsifiability-Aware Conformal Routing for Mixture-of-Agents](http://arxiv.org/abs/2609.25959v1)
  <details><summary>📄 Abstract</summary>
  Multi-agent language systems often treat agreement as evidence, yet heterogeneous agents can jointly repeat an unsupported claim or omit a correct specialist fact. We introduce C-MoA, an agreement-based conformal filter that turns inter-agent semantic support into a claim-level nonconformity score and calibrates a retention threshold at the example level, giving distribution-free within-domain factuality control for heterogeneous Mixture-of-Agents. C-MoA is effective: it nearly doubles retained-...
  </details>

- **2026-09-22** — Panagiotis Michael, Moysis Symeonides, Demetris Trihinas — [Evaluating Accuracy and Probabilistic Reliability of Zero-Shot Time Series Foundation Models](http://arxiv.org/abs/2609.25788v1)
  <details><summary>📄 Abstract</summary>
  Time Series Foundation Models (TSFMs) promise a paradigm shift toward zero-shot forecasting by eliminating task-specific training. However, existing works often overlook trade-offs between predictive accuracy and probabilistic calibration. This paper presents a benchmark study of six TSFMs evaluated on energy, traffic, and financial datasets. We contrast their performance against statistical baselines and a supervised DL model. The study reveals that while TSFMs outperform statistical methods an...
  </details>

- **2026-09-22** — YongBo Li, Shuang Liang, HongWei Ma — [Model-Free Current Control of Permanent Magnet Synchronous Motors via ESO-Based Disturbance Feedforward and Data-Driven H-infinity Residual Feedback](http://arxiv.org/abs/2609.25759v1)
  <details><summary>📄 Abstract</summary>
  This paper proposes a model-free current control method for permanent magnet synchronous motors (PMSMs) based on disturbance feedforward and residual feedback. An ultra-local current model incorporates motor dynamics, parameter uncertainties, cross-coupling effects, and other nonideal factors into generalized lumped disturbances. An extended state observer (ESO) estimates these lumped disturbances and compensates for them through feedforward action, transforming the original PMSM current-control...
  </details>

- **2026-09-22** — YanZe Cao — [Testing-Driven Reliability Audit of Trajectory-Based Early Outcome Prediction for LLM Agents: Target-Specific Calibration Transfer Persists Within a Single Benchmark](http://arxiv.org/abs/2609.25647v1)
  <details><summary>📄 Abstract</summary>
  Predicting early outcomes based on trajectory can decrease the expenses associated with agent evaluation by terminating a run once the outcome becomes sufficiently predictable, assuming that the predictor's confidence is properly calibrated. Calibration is at risk when a predictor is applied to an agent on which it was never trained, but it is not known whether such transfer failures are broad across agent systems or concentrated in specific target agent/head combinations. Using public SWE-bench...
  </details>

- **2026-09-22** — Shubham Santosh Pandere, Gautam Ranka, Ritika Varshney et al. — [Rewired or Gated? How Instruction Tuning Shapes Knowledge-Conflict Circuits in LLMs](http://arxiv.org/abs/2609.25602v1)
  <details><summary>📄 Abstract</summary>
  In language models, the choice between believing the prompt and believing the weights is made by a handful of identifiable attention heads. Instruction tuning changes how models behave under conflict, but whether it rewires the underlying circuit or merely gates/reweights already present components, remains unknown. We provide the first mechanistic base-vs-instruct comparison of conflict-resolution circuits, across three families (Llama-3.2-3B, Qwen-2.5-3B, Gemma-3-4B). Five independent methods,...
  </details>

- **2026-09-22** — Chaehyun Kim, Sein Kim, Hongseok Kang et al. — [A Behavioral Trait Leaks into Preferences: Diagnosing Trait Interference in LLM User Simulators](http://arxiv.org/abs/2609.25572v1)
  <details><summary>📄 Abstract</summary>
  LLM-based user simulators aim to bridge the offline-online gap in recommender evaluation by emulating users through injected traits, where preference attributes determine what a user engages with and a behavioral activity trait governs how long they browse. However, we show this intended trait independence collapses during simulation, causing two failures: (i) Trait Interference, where amplified activity distorts preference boundaries and forces interactions with mismatched items to sustain brow...
  </details>

- **2026-09-22** — Vikas A. Patel, Mahdi Al-Husseini, Duncan Eddy et al. — [Risk-Averse Lander Site Selection under Altitude-Limited Information](http://arxiv.org/abs/2609.25517v1)
  <details><summary>📄 Abstract</summary>
  In aerospace systems, powered descent requires efficiently selecting a landing site while fine-scale hazards remain unresolvable until low altitude. This process presents a decision challenge since the actor must select a site and make corresponding actions before all information is known. To successfully solve this problem, an agent must reason over potential risks and make corrections as new observations are made. We introduce a lightweight model of altitude-limited information where each land...
  </details>

- **2026-09-22** — Sepideh Gohari, Goodarz Mehr, Azim Eskandarian — [Real-World Perception for Autonomous Driving in Adverse Weather: Enhancing Standard Detectors via Foundation-Guided Auto-Annotation](http://arxiv.org/abs/2609.25515v1)
  <details><summary>📄 Abstract</summary>
  Standard deployment-ready object detectors for autonomous vehicles degrade in adverse weather and lighting conditions without being trained on extensive domain-specific data. While large-scale vision foundation models offer robust zero-shot generalization, their high computational cost makes them impractical for real-time deployment. To bridge this gap, we propose a foundation-guided auto-annotation pipeline that enhances standard detectors without architectural changes. We first benchmark three...
  </details>

- **2026-09-21** — Donghyun Kim, Taehyuk Lee, Jinyeong Kim et al. — [Mitigating Sequential Reappearance in Diffusion Data-Point Unlearning](http://arxiv.org/abs/2609.25166v1)
  <details><summary>📄 Abstract</summary>
  Diffusion data-point unlearning is typically evaluated immediately after each deletion, even though subsequent requests may repeatedly update the same model. We identify sequential reappearance, a failure mode in which an instance that is initially judged to be forgotten later returns to the memorized regime without reuse of the deleted data or adversarial fine-tuning. To capture this behavior, we introduce a target-level evaluation protocol that tracks whether each target is forgotten immediate...
  </details>

- **2026-09-21** — Abdorasoul Ghasemi — [From functioning to evolving: A complex systems perspective on future self-organised federated energy communities](http://arxiv.org/abs/2609.25425v1)
  <details><summary>📄 Abstract</summary>
  Energy networks face a paradigm shift driven by renewable integration, uncertainty about required flexibility, distributed markets, and smart demand. Increasing asset interactions, cyber dependencies on communication and computation systems, and the deployment of AI agents demand a holistic, system-wide approach to understand the system's emergent behaviour. These transformations affect energy generation, demand adaptation, grid operations, and market dynamics, forming a complex engineered \emph...
  </details>

- **2026-09-21** — Toan Nguyen, Weiduo Yuan, Siheng Zhao et al. — [HOTICE: Whole-Body Humanoid Object Transportation in Cluttered Environments](http://arxiv.org/abs/2609.25363v1)
  <details><summary>📄 Abstract</summary>
  Object transportation is a fundamental capability for humanoid robots operating in real-world, human-centric environments, yet existing methods struggle when clutter constrains free space around both the robot and its carried payload. We present HOTICE, a whole-body humanoid learning framework for transporting objects through such cluttered environments. First, we introduce Humanoid-Object Decoupled Potential Fields, which jointly encode collision-avoidance guidance for the robot and the carried...
  </details>

- **2026-09-21** — Chuyang Xiao, Peilin Meng, David Held — [JAMB: Joint Action-Motion Diffusion for Bimanual Manipulation](http://arxiv.org/abs/2609.25322v1)
  <details><summary>📄 Abstract</summary>
  Coordinated bimanual manipulation is challenging because the motion of either arm can alter the shared 3D scene and thereby affect the other arm. Yet most diffusion policies generate actions without explicitly modeling these future geometric consequences, while predictive variants typically use future state only as auxiliary supervision or fixed conditioning. We address this limitation by proposing JAMB, a diffusion policy that jointly denoises bimanual actions and future 3D point tracks. By all...
  </details>

- **2026-09-21** — Walter J. Manuel, Yuji Takubo, Simone D'Amico — [Transformer-Informed Trajectory Optimization for Relative Motion in Cislunar Orbits](http://arxiv.org/abs/2609.25460v1)
  <details><summary>📄 Abstract</summary>
  Autonomous spacecraft guidance and control requires a fast solution to non-convex trajectory optimization, which can be accelerated by providing a near-optimal initial guess to an optimization protocol, i.e., warm-starting. A robust warm starting method is especially useful for rendezvous, proximity operations, and docking (RPOD) in cislunar space, where the underlying dynamics become severely nonlinear and chaotic compared to those in Earth orbit, especially at perilune. This paper extends the ...
  </details>

- **2026-09-21** — Abolfazl Babanazari, Carson Cramer, Tyler Summers et al. — [PARTE: Plane-Assisted Robust Transformation Estimation for Point Cloud Registration](http://arxiv.org/abs/2609.25375v1)
  <details><summary>📄 Abstract</summary>
  Global point-cloud registration remains challenging when limited overlap, repetitive geometry, and sensor noise produce correspondence sets dominated by outliers. Planar regions are particularly difficult for conventional point descriptors and are therefore often suppressed or discarded before matching. We present PARTE (Plane-Assisted Robust Transformation Estimation), a global registration method that instead treats planar structure as complementary registration evidence. PARTE extracts planar...
  </details>

- **2026-09-21** — Ana Trišović, Janakan Sivaloganathan — [Open Science, Closed Models: How Funding Shapes AI in Science](http://arxiv.org/abs/2609.25347v1)
  <details><summary>📄 Abstract</summary>
  How funding shapes AI engagement in science is poorly understood despite its structural importance. We analyze 104,226 scientific papers (2018-2025), linking funding acknowledgments to how each paper engages with foundation models: whether it extends a model (fine-tunes or builds on it), uses one without modification, or references models only peripherally. Three findings emerge. First, funding source is associated with the character of engagement: public funding is associated with higher open-w...
  </details>

- **2026-09-21** — Jian Sun, Kingshuk Ghosh, Lilianna Houston et al. — [MT-ProtBERT: Multi-task Learning ProtBERT for Intrinsically Disordered Proteins Classification with Scarce Data](http://arxiv.org/abs/2609.25334v1)
  <details><summary>📄 Abstract</summary>
  Intrinsically disordered proteins (IDPs) differ from folded proteins in that they are dynamic, lack a stable three-dimensional conformation, and have low sequence similarity between similar proteins. The conformational heterogeneity of IDPs - while beneficial for their diverse functions - limits the use of traditional experimental tools to determine their conformation. The experimental difficulty, along with low sequence similarity, results in data scarcity, and makes it difficult to classify/de...
  </details>

- **2026-09-21** — Junru Zhu, Yixin Yang, Xiaoqing Ding et al. — [Partition-Matched Evaluation of Community Features under Distribution Shift in Android Malware Function-Call Graphs](http://arxiv.org/abs/2609.25256v1)
  <details><summary>📄 Abstract</summary>
  Graph-based Android malware classifiers can lose accuracy under malware-type or family shifts. We test whether mesoscopic organization in function-call graphs provides shift-stable information beyond local degree profiles (LDP), global statistics, lightweight metadata, and size-matched random partitions. Using 15,000 MalNet-Tiny, Common, and Distinct graphs, six Leiden descriptors specified before evaluation, and five optimizer seeds, communities raise Tiny macro F1 from 78.7% to 81.3% but yield...
  </details>

- **2026-09-21** — Ruike Cao, Fanyu Zhao, Fugen Yao et al. — [MemCalib: Benchmarking and Optimizing Memory Use in LLM Agents](http://arxiv.org/abs/2609.24259v2)
  <details><summary>📄 Abstract</summary>
  The effectiveness of agent memory ultimately depends on whether the underlying LLM gives each memory in context an appropriate degree of influence over its response. Yet this capability has remained largely overlooked. To assess this capability, we introduce MemCalib, a benchmark grounded in realistic memory-system scenarios for evaluating memory use and advancing optimization algorithms. Results on the MemCalib test set reveal that frontier open- and closed-source models struggle to use memory ...
  </details>

- **2026-09-21** — Ziyad Benomar, Aymen Al Marjani, Paul Missault et al. — [Augmented Hypothesis Testing with Persona-Based LLM Simulations](http://arxiv.org/abs/2609.24629v1)
  <details><summary>📄 Abstract</summary>
  A/B testing requires large sample sizes, long timelines, and significant costs. When auxiliary predictions of experimental outcomes are available from machine learning models, uncertain prediction quality precludes replacing human experiments entirely, yet these predictions may still contain useful signal. We propose a principled framework for learning-augmented hypothesis testing that leverages predictions of unknown quality to reduce sample sizes while maintaining statistical validity. Predict...
  </details>

- **2026-09-21** — Zhilin Wang, Shaokun Zhang, Yifan Zhang et al. — [OSWorld-Pro: Process-based Evaluation for Computer Use Agents](http://arxiv.org/abs/2609.24890v1)
  <details><summary>📄 Abstract</summary>
  Evaluation of Computer-Use Agents (CUAs) is often limited to the final deliverables they create (at the end of hundreds of steps) and assessed with functional verifiers, as seen in OSWorld. However, such evaluation of end-state performance lacks transparency into how and why agents fail in various tasks, obfuscating critical insight for subsequent improvement. For instance, agents that err during keyboard inputs would require a different mitigation strategy from those that fail to precisely prov...
  </details>

- **2026-09-21** — Bowei Li, Yuner Zhang, Changliu Liu — [ARSTAG: An Agentic Real2Sim2Real System for Task-Specific Robot Data Generation](http://arxiv.org/abs/2609.24563v1)
  <details><summary>📄 Abstract</summary>
  Adapting visuomotor policies to new manipulation tasks often requires substantial manual engineering or teleoperated data collection. Simulation can provide task-specific data at scale, but constructing the scene, designing expert behavior, and configuring data generation still require significant per-task effort. We present ARSTAG, an agentic Real2Sim2Real system that turns a single RGB image and a natural-language instruction directly into robot policy-learning data. A hierarchy of language ag...
  </details>

- **2026-09-21** — Xinyang Li, Kevin Stone, Ajit Vikram — [JAREX: An Acquisition Function for Multi-Objective Algorithmic Process Characterization](http://arxiv.org/abs/2609.24954v1)
  <details><summary>📄 Abstract</summary>
  Pharmaceutical process characterization is central to Quality by Design because it defines how variations in process parameters affect the ability to meet product quality specifications, thereby supporting proven acceptable ranges and robust manufacturing. In practice, however, characterization still relies largely on factorial design of experiments (DOE) approaches, which are inefficient for resolving multivariate pass/fail boundaries in higher-dimensional spaces. While Bayesian optimization ha...
  </details>

- **2026-09-21** — B. Bidaran, A. Jiménez, R. García-Benito et al. — [CAVITY: Calar Alto Void Integral-field Treasury surveY: II. Second public data release](http://arxiv.org/abs/2609.24726v1)
  <details><summary>📄 Abstract</summary>
  Studying galaxy evolution under the unique environmental conditions of cosmic voids provides an opportunity to disentangle the role of the large-scale environment in shaping mass assembly (both baryonic and dark matter), regulating galaxy physical properties, and driving the transformation from star-forming to quiescent systems. We present the second public data release (DR2) of the Calar Alto Void Integral-field Treasury Survey (CAVITY), an ongoing legacy programme designed to study void galaxi...
  </details>

- **2026-09-21** — Raphaël Thieffry, Matej Martinc — [Assessing Readability with LLMs: The Role of Reasoning and Few-Shot Prompting](http://arxiv.org/abs/2609.24650v1)
  <details><summary>📄 Abstract</summary>
  Readability assessment is essential for tailoring texts to intended audiences across educational, healthcare, and information retrieval domains. However, traditional readability formulas struggle to generalize across genres and languages, while supervised machine learning models rely on scarce, domain-specific annotated corpora, limiting their applicability--particularly for less-resourced languages. Large Language Models (LLMs) offer a highly scalable, multilingual alternative that requires no ...
  </details>

- **2026-09-21** — Zhengbao Yao, Yuanfu Luo, Kehan Xue — [From Semantic Decisions to Feasible Trajectories: Self-Evolving LLM-Guided Optimal Control for Narrow-Space Parking](http://arxiv.org/abs/2609.24631v1)
  <details><summary>📄 Abstract</summary>
  Autonomous parking in nonconvex and narrow environments remains challenging. Although optimal-control methods can explicitly enforce vehicle dynamics and collision constraints, nonconvexity compromises solver robustness and can cause failures. Large language models (LLMs) exhibit strong semantic reasoning capabilities, but directly generating dense trajectories makes it difficult to guarantee physical feasibility. We introduce SE-LLM-OCP, a unified framework in which LLMs make high-level discret...
  </details>

- **2026-09-21** — Débora Oliveira Makowski, Samiran Gode, Abhijeet Nayak et al. — [What do VLM-Based Vision-Language Navigation Models Rely on: Interpreting and Steering Policy Behavior](http://arxiv.org/abs/2609.24576v1)
  <details><summary>📄 Abstract</summary>
  Modern Vision-Language Navigation (VLN) models rely mostly on pre-trained large Vision-Language Models (VLMs) to predict navigation actions. While this fusion of language instructions and visual observations allows multimodal reasoning, it obscures how information is routed across modalities or what mechanisms drive navigation decisions. Thus, it remains unclear whether VLN models ground their predictions in relevant semantic cues or can track task progress. In this work, we study the interpreta...
  </details>

- **2026-09-21** — Lucas Meyer, Claudio Sole, Huikan Xiang et al. — [$t_0$: A Time-Series Foundation Model for Forecasting with Context](http://arxiv.org/abs/2609.24559v1)
  <details><summary>📄 Abstract</summary>
  We present $t_0$, a family of open-weights foundation models for forecasting with multivariate context. We release its first two members: $\texttt{t0-alpha}$ and $\texttt{t0-beta}$, respectively 102M and 256M parameters. Both condition their forecasts on target history, past covariates, and known-future covariates, without task-specific retraining. Their transformer layers alternate attention along time and across variates. They produce probabilistic forecasts through quantile predictions. Pretr...
  </details>

- **2026-09-21** — Pawan K. Tripathi, Hemant Sharma, Andrew Chuang et al. — [APEXA: Execution-Integrity Enforcement for Multi-Agent LLM Automation of Synchrotron Data Reduction](http://arxiv.org/abs/2609.24165v1)
  <details><summary>📄 Abstract</summary>
  Synchrotron data reduction, detector calibration followed by azimuthal integration of terabyte-scale diffraction series, is a multi-step, expert-bound bottleneck that increasingly limits the science rate of user facilities. LLM agents promise to collapse it, but driving a real pipeline with a stochastic model creates a failure mode chat benchmarks cannot see: an agent can report a calibration that was never computed. Correctness here is a property of what executed, not of the transcript. We pres...
  </details>

- **2026-09-21** — Juntao Li, Xingke Xia, Sichao Liu et al. — [GraspTune: Tactile-Driven Execution Refinement for Robust Grasping](http://arxiv.org/abs/2609.24180v1)
  <details><summary>📄 Abstract</summary>
  Visual grasp proposal generation has advanced rapidly, yet converting a selected proposal into a stable physical grasp remains a central execution-stage challenge. This paper introduces GraspTune, a tactile-driven execution-stage refinement framework that starts from a nominal proposal and applies bounded residual TCP motions during approach, contact formation, and final grasp execution. GraspTune learns control-facing contact semantics from local depth, tactile signals, state, and history using...
  </details>

- **2026-09-21** — Jiaxin Hong, Yuxin Peng, Hongyao Yu et al. — [From Bits to Beliefs: Recoverable Semantic Fingerprints for Black-Box Verification of Large Language Models](http://arxiv.org/abs/2609.24084v1)
  <details><summary>📄 Abstract</summary>
  Open-weight large language models (LLMs) can be copied, modified, and redeployed behind black-box APIs, making post-release ownership verification difficult. Existing black-box fingerprints often rely on secret query-key pairs that reproduce predefined responses, and can therefore be easily disrupted by fine-tuning, pruning, quantization, model merging, and serving-time prompt changes. We propose SimPrint, a recoverable semantic fingerprinting framework for black-box LLM ownership verification. ...
  </details>

- **2026-09-21** — Huiqiong Li, Zhiting Mei, Anirudha Majumdar et al. — [LIBERO-VPro: Benchmarking Closed-Loop Visual Robustness of Robotic Foundation Models](http://arxiv.org/abs/2609.24350v1)
  <details><summary>📄 Abstract</summary>
  Robotic foundation models achieve impressive performance on standard manipulation benchmarks, yet these evaluations typically assume clean, timely, and consistent visual observations throughout execution. We introduce LIBERO-VPro, a benchmark for systematically evaluating the closed-loop visual robustness of robotic foundation models by perturbing the visual evidence available during execution. LIBERO-VPro covers four complementary dimensions, including Visual Evidence Degradation, Camera Stalen...
  </details>

- **2026-09-21** — Kevin Baum, Maximilian Kiener, Markus Langer et al. — [Anticipatory Human Oversight of Agentic AI: A Philosophical Account](http://arxiv.org/abs/2609.24242v1)
  <details><summary>📄 Abstract</summary>
  Human oversight is widely held to mitigate the risks of AI systems. Even for systems that produce discrete outputs at identifiable decision points, the realisation of human oversight as a reactive measure is empirically fragile, yet increasingly well understood. However, for agentic AI -- systems that plan, decompose goals, and execute multi-step actions over extended horizons -- reactive oversight reaches its structural limits: intervention on individual actions defeats the autonomy that motiva...
  </details>

- **2026-09-21** — Khaoula Chehbouni, Melina Medjdoub, Florian Carichon et al. — [LLJ Cards: Best practices for the Use of LLMs as Judges](http://arxiv.org/abs/2609.24516v1)
  <details><summary>📄 Abstract</summary>
  In recent years, large language models (LLMs) have emerged as a popular alternative for evaluation. Often referred to as LLMs as judges (LLJs), these systems have been widely adopted by researchers and practitioners across a broad range of measurement tasks, driven by their strong performance, scalability, and cost-effectiveness relative to human judgment. However, a growing body of work has shown that the use of LLJs raise concerns about their validity and reliability as evaluators. Existing ef...
  </details>

- **2026-09-21** — Kalash Shah, Kunal Singh, Snehan J et al. — [Fathom-Vaidya: Advancing Medical Reasoning with Rubric-Based Rewards](http://arxiv.org/abs/2609.24480v1)
  <details><summary>📄 Abstract</summary>
  Deploying Large Language Models (LLMs) in healthcare requires robust performance across two complementary dimensions - diagnostic reasoning: the convergent, evidence-driven task of inferring a patient's condition from clinical data to produce a diagnosis, and clinical healthcare reasoning: the broader, navigational judgment required to communicate, plan, and adapt across multi-turn clinical interactions where a single correct answer may not exist. Recent benchmarks such as HealthBench and MedXpe...
  </details>

- **2026-09-21** — Md Ahshanul Haque, Muhammad Ashad Kabir — [Machine Learning-Based Prediction of Childhood Stunting in Bangladesh: Fairness and Temporal Robustness Assessment](http://arxiv.org/abs/2609.24386v1)
  <details><summary>📄 Abstract</summary>
  Childhood stunting remains a major public health concern in Bangladesh and reflects long-term growth failure influenced by child, maternal, household, socioeconomic, and health-service factors. This study used nationally representative Bangladesh Demographic and Health Survey data from 2007 to 2022 to develop machine learning models for population-level prediction of childhood stunting and to assess temporal robustness and subgroup fairness. Children aged 0-59 months with complete anthropometric...
  </details>


### 📂 watermark
*水印与溯源 / Watermarking & Provenance* — 19 papers

- **2026-09-23** — Mateusz Zych, Vasileios Mavroeidis, Gudmund Grov — [CCR: Towards a Common, Quality-Gated CACAO Integrations Registry for European Cybersecurity Automation](http://arxiv.org/abs/2609.27567v1)
  <details><summary>📄 Abstract</summary>
  Standardised, machine-readable cybersecurity playbooks provide a basis for portable, shareable, and reusable incident-response logic. OASIS CACAO provides a vendor-neutral representation for such playbooks, but not the product-specific integration artefacts needed to invoke external products and services. We introduce the Common CACAO Registry (CCR), an open, provenance-aware registry of CACAO HTTP-API connector envelopes. Each envelope captures an API operation's command, inputs, target, authen...
  </details>

- **2026-09-23** — Xuanyu Meng, Xing Fan, Xinyi Fan et al. — [EnSIMem: Entity-Structured Indexing for Long-Term Agent Memory](http://arxiv.org/abs/2609.27279v1)
  <details><summary>📄 Abstract</summary>
  An agent that interacts with users over long periods must recall facts, preferences, events, and changes from a continuously growing interaction history. Existing memory systems often compress interactions into generic summaries or retrieve anonymous text chunks, making it difficult for an agent to identify the correct entity, property, and supporting evidence. We present EnSIMem, an entity-structured long-term memory architecture for an agent. During offline construction, the system organizes i...
  </details>

- **2026-09-23** — Liangyu Li, Michael White — [Motif-Vocab: StatisticallyCalibrated Transcription-Factor-Identity Tokenization forGenomic Language Models](http://arxiv.org/abs/2609.28386v1)
  <details><summary>📄 Abstract</summary>
  Tokenization is a central design choice in genomic language models, yet most deoxyribonucleic acid (DNA) tokenizers use characters, fixed-length k-mers, or frequency-derived subwords without explicitly using prior information about the specificity of DNA-binding regulatory factors. We introduce Motif-Vocab, a biologically informed tokenizer that scans both DNA strands for statistically calibrated motif matches, emits transcription-factor (TF) identity tokens, and applies nucleotide, $k$-mer, or ...
  </details>

- **2026-09-23** — Walter Kurz, Reinhard Magg — [Compliant AI Infrastructure for Regulated Finance: A tiered multi-agent framework with DLT audit trails for financial operations in DACH](http://arxiv.org/abs/2609.27632v1)
  <details><summary>📄 Abstract</summary>
  We present a compliance-first architecture for AI in regulated finance that treats regulation as an orientation layer rather than a deterministic ruleset. A matrix of regulatory intent and exposure provides a compact classification handle, which a governed policy compiler then maps into concrete prohibitions, obligations and runtime budgets. Prohibitions constrain feasibility and block externalisation, while obligations extend tasks with artefacts that must meet explicit admissibility criteria. ...
  </details>

- **2026-09-23** — Hengyu Li — [KITE: Scaling Jev Population Experiments with Sparse Flagship Calibration](http://arxiv.org/abs/2609.27535v1)
  <details><summary>📄 Abstract</summary>
  KITE queries a typed behavioral kernel once per unique state, then executes populations of any size from the table with event-keyed randomness and common random numbers. An expensive flagship model is reserved for sparse paired anchors that estimate intervention effects. Measured human-model discrepancy is propagated as shared error into every conclusion. Population-experiment cost thus scales with unique states and anchors, while uncertainty is governed by evidence about people rather than Mont...
  </details>

- **2026-09-23** — Haoluan Fu, Keni Chen, Xinyu Jia et al. — [Emergi-PersonaOS: A Persona Agent Operating System for Situational Adaptation and Controllable Evolution](http://arxiv.org/abs/2609.27417v1)
  <details><summary>📄 Abstract</summary>
  Symbiosis between humans and digital beings offers a vision for the future of human--machine interaction. In enduring human--machine relationships, personality provides a foundation for continuity of identity, individuality in interaction, and development through experience. We investigate this capacity through persona agents as computational implementations and introduce Emergi-PersonaOS, a psychology-grounded operating system for managing persona objects throughout their lifecycle. The system ...
  </details>

- **2026-09-22** — Anchit Mishra — [When Direct Manipulation Becomes a Guess: Productive Friction in AI-Mediated Multisensory Visualization](http://arxiv.org/abs/2609.27104v1)
  <details><summary>📄 Abstract</summary>
  Generative visualization increasingly embeds large language models within direct manipulation and multisensory interaction. Speech, gaze, touch, gesture, sound, and haptics can make probabilistic inference feel like familiar, deterministic tool use. I call this gap a deterministic-affordance mismatch: deterministic interaction cues persist while AI weakens predictability, locality, reversibility, or provenance. Reading the malleable interfaces of Iron Man 2 against systems from Blade Runner 2049...
  </details>

- **2026-09-22** — Haobo Zheng, Tan Tang, Yan Chen et al. — [SpeakerMem-R1: Speaker-Centered Dual-Track Memory for Multi-Party Dialogue](http://arxiv.org/abs/2609.26780v2)
  <details><summary>📄 Abstract</summary>
  Long-term conversational memory in multi-party settings requires more than retrieving relevant content from long-term conversations: it must distinguish who said what, whom each statement concerns, how individuals perceive one another, what information is shared by the group, and how states change over time. Recent studies on multi-party dialogue benchmarks show that existing general-purpose LLM memory systems tend to lose person and group relations or struggle to integrate clues distributed acr...
  </details>

- **2026-09-22** — Yiqi Wang, Jinqian Ju, Jiaqi Zhang et al. — [When Does Execution Provenance Help Agent Memory Retrieval?](http://arxiv.org/abs/2609.25913v1)
  <details><summary>📄 Abstract</summary>
  A language agent's execution history can exceed its context window, requiring its memory system to retrieve complete supporting evidence under a hard token budget. Evidence may span multiple execution events, yet conventional retrievers use fixed token windows and fixed-k metrics that reward individual fragments without showing whether the complete evidence set fits in context. Smaller windows reduce irrelevant text but scatter evidence across candidates, while flat-versus-graph comparisons can ...
  </details>

- **2026-09-22** — Sebastian Cochinescu — [Truth for Believable AI: Expressed Doubt, Provenance, and Belief Revision as an Engineerable Stance](http://arxiv.org/abs/2609.26035v1)
  <details><summary>📄 Abstract</summary>
  Conversational agents often express answers in a uniformly confident register. We test whether expressed uncertainty, provenance-aware assertion, and explicit belief revision can be implemented as a behavior layer over a fixed language model; we do not test believability or trust. The layer combines three epistemic states, per-claim confidence and typed provenance, a provenance-gated expression rule, and a persistent revision store with auditable acknowledgments and partial resistance to false c...
  </details>

- **2026-09-22** — Haobo Zheng, Tan Tang, Yan Chen et al. — [SpeakerMem-R1: Speaker-Centered Dual-Track Memory for Multi-Party Dialogue](http://arxiv.org/abs/2609.26780v1)
  <details><summary>📄 Abstract</summary>
  Long-term conversational memory in multi-party settings requires more than retrieving relevant content from long-term conversations: it must distinguish who said what, whom each statement concerns, how individuals perceive one another, what information is shared by the group, and how states change over time. Recent studies on multi-party dialogue benchmarks show that existing general-purpose LLM memory systems tend to lose person and group relations or struggle to integrate clues distributed acr...
  </details>

- **2026-09-22** — Md Ataur Rahman, Dimitris Sacharidis, Oscar Romero et al. — [Discovery-Driven Integration of Disjoint Tables via Text](http://arxiv.org/abs/2609.26658v1)
  <details><summary>📄 Abstract</summary>
  Integrating heterogeneous datasets within data lakes is a critical challenge, particularly for semantically related tables that lack the explicit attributes needed to be joined. We study Discovery-Driven Integration, where the relevant sources and their missing relational structure must be discovered before integration. In this setting, unstructured text provides the evidence that connects otherwise disjoint tables. The fundamental challenge is to discover the relationships at a fine-grained lev...
  </details>

- **2026-09-22** — Shivam Gupta — [The Delegation Blind Spot: Auditing Product Decisions from Agent Choices](http://arxiv.org/abs/2609.26642v1)
  <details><summary>📄 Abstract</summary>
  Successful agent execution need not identify which future product improvement its user would value. We present a decision-specific audit that maps a declared observation channel and product-value contrast to compatible intervals and witness populations. Its foundations are established identification and decision theory; the contribution is an executable measurement workflow and a controlled study of its limits. A frozen experiment makes 4,800 requests to two pinned model snapshots on shared synt...
  </details>

- **2026-09-22** — Jiayi Li, Ziyuan Wang, Daniel Garijo et al. — [CQ4OE: A benchmark for assessing LLM-assisted ontology generation from competency questions](http://arxiv.org/abs/2609.26029v1)
  <details><summary>📄 Abstract</summary>
  Ontology generation from Competency Questions (CQs) is a central yet labor-intensive phase of Ontology Engineering. While large language models (LLMs) offer promising automation capabilities, current evaluations remain fragmented. Task formulations are heterogeneous, gold standards often lack fine-grained CQ provenance, metrics conflate lexical overlap with structural and logical adequacy, and reference ontologies are not always explicitly designed around the evaluation CQs. Here, we address the...
  </details>

- **2026-09-22** — Jiangxu Wu — [Knowledge-as-Skill: A Structural Design for Autonomous Knowledge-Base Use by LLM Agents](http://arxiv.org/abs/2609.25991v1)
  <details><summary>📄 Abstract</summary>
  Retrieval-augmented generation (RAG) gives large language models (LLMs) access to external knowledge, but its conventional retrieve-concatenate-generate pipeline makes retrieval decisions on behalf of the model. As tool use and agent loops become more reliable, an agent can decide whether to retrieve, what to inspect, and when to stop. This shift exposes a new bottleneck: the agent may not know what a knowledge base contains. Traditional knowledge bases expose documents as anonymous text chunks ...
  </details>

- **2026-09-22** — Abhishek Sharma — [CausalLoss-Fin: Attributing Financial-Agent Loss to Decisions and Infrastructure Faults](http://arxiv.org/abs/2609.25960v1)
  <details><summary>📄 Abstract</summary>
  When an agent handling a payment exception loses money, the agent-step attribution methods this paper compares against will name one of its actions. They will do so even when a settlement message was dropped and the agent never had a chance: they intervene on agent actions and do not expose infrastructure faults as intervenable variables, so every dollar they explain is charged to a decision. We take a benchmark whose fault process is explicit and replayable, decompose each episode's realised de...
  </details>

- **2026-09-22** — Aryaman Arora, Kirill Acharya, Nathan Hu et al. — [Matryoshka attribution: Learning to attribute language model outputs to representations and weights](http://arxiv.org/abs/2609.25518v1)
  <details><summary>📄 Abstract</summary>
  Attributing language model outputs to their internal computations is an open problem in interpretability. Existing methods, which use causal interventions, gradients, or learnable masks, either are infeasibly expensive or struggle to identify actual causally-important internal computations. We propose framing attribution as the problem of identifying nested subsets of internal components which minimise a downstream loss. To learn this task, we introduce Matryoshka Attribution (MAttr), a mask lea...
  </details>

- **2026-09-21** — David Garg, Ritobrata Sarkar, Ehsan Azarnasab et al. — [ShowTellArena: Evaluating Business Workflow Understanding from Demonstrations](http://arxiv.org/abs/2609.25467v1)
  <details><summary>📄 Abstract</summary>
  We often teach a colleague by showing the work and explaining the decisions as we go. How can we check what an agent understood from the same lesson? We introduce ShowTellArena, a benchmark protocol and public dataset for comprehension after narrated business demonstrations. The v1.0 release contains 50 business workflow tasks, with recordings, screenshots, narration, fixture seeds, and 502 questions. Tasks span finance, hiring, procurement, customer decisions, inventory, and logistics. The prot...
  </details>

- **2026-09-21** — Timothy Urista — [Who Pays for the KV Cache? Attributing Shared AI Inference Spend Across Kubernetes and LLM Provider Bills](http://arxiv.org/abs/2609.24991v1)
  <details><summary>📄 Abstract</summary>
  Organizations pay for AI through disconnected ledgers: Kubernetes allocations for self-hosted inference, gateway logs, and per-token bills from API providers. We present unalloc, an open-source tool that joins OpenCost, LiteLLM, OpenAI and Anthropic cost data into one exact ledger and reports the share of spend with no owner, and use it to study where attribution breaks at the seams between these systems. Five case studies run inference for real or simulate it: a vLLM-style serving simulator wit...
  </details>


### 📂 unlearning
*机器遗忘 / Machine Unlearning* — 1 papers

- **2026-09-22** — Jin Liu, Yanzhong He, Guancheng Lin et al. — [What Was Once Learned May Need to Be Unlearned: Machine Unlearning for Deprecated API Knowledge in Large Language Models](http://arxiv.org/abs/2609.25786v1)
  <details><summary>📄 Abstract</summary>
  Large language models (LLMs) for code completion may generate deprecated APIs because their pre-training corpora contain code from historical library versions. Existing approaches use inference-time intervention, model editing, or machine unlearning, but multiple plausible completions make predefined replacements restrictive. Moreover, existing studies rarely verify whether models exhibit the targeted deprecated behavior or evaluate unintended changes to other APIs.   We conduct a systematic emp...
  </details>


### 📂 survey
*综述与系统化 / Surveys & Systematization* — 4 papers

- **2026-09-23** — Olivia Venot, Yamila Miguel, Robin Baeyens et al. — [Probing Exoplanetary Chemistry with Ariel: Scientific Priorities and Observational Strategies](http://arxiv.org/abs/2609.27622v1)
  <details><summary>📄 Abstract</summary>
  Over the past two decades, increasingly precise observations have revealed that exoplanet atmospheres are chemically diverse and often far from equilibrium, with processes such as vertical mixing, photochemistry, and atmospheric circulation producing significant departures from thermochemical expectations. As large surveys across a wide range of planets begin to uncover population-level chemical trends, a coherent interpretation of these patterns remains elusive, particularly for gas giants and ...
  </details>

- **2026-09-22** — Varshini Elangovan, James Wedgwood, Chhavi Yadav et al. — [Safety Nudges: User-Facing Interventions for Real-Time AI Risk Awareness](http://arxiv.org/abs/2609.26865v1)
  <details><summary>📄 Abstract</summary>
  Conversational AI systems can pose safety risks to their users such as hallucination, sycophancy, overconfidence, and anthropomorphism, but these risks are difficult for users to detect during everyday use. We introduce Safety Nudges, a browser-based tool that provides lightweight, in situ flags when concerning behavior is detected in chatbot conversations. We evaluated Safety Nudges in a two-week field study with 45 frequent chatbot users, collecting interaction logs, surveys, and feedback on i...
  </details>

- **2026-09-22** — Vishnu Sashank Dorbala, Dinesh Manocha — [Deploying Foundation Models for Embodied Navigation](http://arxiv.org/abs/2609.25666v1)
  <details><summary>📄 Abstract</summary>
  We present and tackle two problems associated with deploying Foundation Models (FMs) on Embodied Agents performing navigation: 1) Training bias in FMs leading to poor personalization in unseen environments, and 2) Limited FM context length hindering success, especially on long horizon tasks. Our solution for the former involves priming the FM with human-habit data mined from the scene and our solution for the latter involves active memory management via a novel `memory head' augmentation. We fir...
  </details>

- **2026-09-21** — Xinyu Wang, Tung Sum Thomas Kwok, Zhenghan Tai et al. — [FinInteract: Benchmarking Clarification and Intent Integration in Ambiguous Financial Question Answering](http://arxiv.org/abs/2609.24002v1)
  <details><summary>📄 Abstract</summary>
  Large language model agents increasingly answer financial questions by searching regulatory filings. Such questions are often deceptively under-specified: Meta Platforms' "operating income" is $46.75B consolidated but $62.87B for the Family of Apps segment, and each reading is exactly verifiable against the filing. A capable agent should recognize the ambiguity and ask, rather than commit to a plausible but unintended reading. Existing financial benchmarks cannot measure this, because one gold a...
  </details>


### 📂 other
*其他安全相关 / Other Security-Related* — 182 papers

- **2026-09-23** — Harshdeep Jadhav, Sreeraj Rajan Warrier, Jayasri Dontabhaktuni — [Image Compression Using Quantum Wavelet Transform and Quantum Convolutional Networks](http://arxiv.org/abs/2609.28387v1)
  <details><summary>📄 Abstract</summary>
  This paper presents a hybrid quantum-classical framework for grayscale image compression and decompression, leveraging the strengths of quantum computing and deep learning. The compression pipeline integrates a Variational Quantum Daubechies Wavelet Transform (V-QDWT) and a trainable Quantum Convolutional Neural Network (QCNN) optimized end-to-end to achieve efficient, image-adaptive multi-resolution analysis and entanglement-based feature reduction. Input images are encoded using the Normal Arb...
  </details>

- **2026-09-23** — Saar Cohen, Nicholas Teh, Michael Wooldridge — [Online Fair Division Against an Oblivious Adversary](http://arxiv.org/abs/2609.28333v1)
  <details><summary>📄 Abstract</summary>
  We study the online allocation of indivisible goods among $n$ agents, where each good must be allocated immediately and irrevocably upon arrival. Against an adaptive adversary, Neoh and Teh [2026] proved that no algorithm can guarantee a positive approximation to proportionality up to one good (PROP1) that is independent of the number of goods, and the same holds for proportionality up to $k$ goods (PROP$k$) for any fixed $k$. We instead consider an oblivious adversary, which fixes the input in ...
  </details>

- **2026-09-23** — Weihang Ding, Junfei Zhan, Yueting Li et al. — [FDE-Bench: Evaluating LLM Agents for Deployment Environment Configuration](http://arxiv.org/abs/2609.27571v1)
  <details><summary>📄 Abstract</summary>
  Deployment requires an agent to turn application code into a running system whose services connect, become ready, and remain observable. FDE-Bench evaluates this capability with 136 deployment-configuration tasks spanning Docker images, multi-service Compose stacks, and Kubernetes, in greenfield and diagnose-and-repair modes. Agents submit declarative artifacts that are collected, rebuilt, and redeployed in a pristine environment. Four gated binary check layers measure build, readiness, behavior...
  </details>

- **2026-09-23** — Zaid Ghazal, Khouloud Gaaloul, Bruce Maxim — [Teach-to-Crash: A Closed-Loop Student-Teacher LLM Framework for Collision-Inducing Test Scenario Generation](http://arxiv.org/abs/2609.27296v1)
  <details><summary>📄 Abstract</summary>
  Validating Autonomous Driving Systems (ADS) in simulation requires testing architectures that can discover rare, safety-critical failures while generating scenarios that are executable, diverse, and useful for downstream failure analysis. We introduce Teach-to-Crash, a closed-loop testing framework that combines a constrained ego-centric scenario representation, stagnation-aware search control, and a dual-LLM architecture for adaptive failure discovery. A high-reasoning Teacher LLM acts as an ad...
  </details>

- **2026-09-23** — Wenjie Feng, Sahba Zojaji, Satoshi Nakamura — [Cross-Scale Transfer Learning for Depression Severity Prediction: From PHQ-8 to HAMD-17 Across Languages and Clinical Paradigms](http://arxiv.org/abs/2609.28430v1)
  <details><summary>📄 Abstract</summary>
  This work addresses continuous depression-severity score prediction from clinical interview transcripts under data scarcity. We propose a sequential low-rank adaptation (LoRA) protocol for cross-scale transfer: a Qwen3 backbone with a bounded regression head is first fine-tuned on the English DAIC-WOZ dataset (189 avatar-mediated sessions, PHQ-8), and the adapter then initializes fine-tuning on the Chinese PDCH dataset (100 real clinical consultations, HAMD-17), where a reinitialised, scale-spec...
  </details>

- **2026-09-23** — Shahan Ahmed — [Threat Amplified, Blame Restrained: LLM-Assisted Media Framing Analysis of the 2026 Bangladesh Measles Outbreak](http://arxiv.org/abs/2609.28362v1)
  <details><summary>📄 Abstract</summary>
  How news media frame and emotionally code a public health emergency shapes public risk perception and trust, yet outbreak-coverage dynamics remain understudied for low- and middle-income countries (LMICs). We examine sentiment and stance in English-language Bangladeshi coverage of the 2026 measles outbreak -- the country's most severe in two decades, with over 97,000 suspected cases and 600 deaths across 61 of 64 districts, unfolding after the 2024 change of government and a 2024-2025 vaccine st...
  </details>

- **2026-09-23** — Dimitrios Rontogiannis, Ander Artola Velasco, Manuel Gomez Rodriguez — [Learning the Cost of Reliable Inference](http://arxiv.org/abs/2609.28322v1)
  <details><summary>📄 Abstract</summary>
  Benchmarking and routing platforms increasingly act as intermediaries connecting large language model providers with end-users. However, providers on these platforms typically use a fixed price per token, preventing users from achieving the most competitive price for their tasks. % workloads. In this work, we design a procurement platform where token prices for each task are driven by provider competition, enabling users to secure competitive pricing for guaranteed quality levels. To this end, t...
  </details>

- **2026-09-23** — Samrat Sahoo, Liang Ji, Tom Silver et al. — [TANDEM: Task and Motion Planning with As-Needed Demonstrations for Efficient Vision-Language-Action Model Fine-tuning](http://arxiv.org/abs/2609.28314v1)
  <details><summary>📄 Abstract</summary>
  Human teleoperators spend substantial time demonstrating behaviors that robots can already perform autonomously, limiting the scalability of data collection for robot foundation models. Task and motion planning (TAMP) can automate many of these behaviors, but a fixed planning domain may not support every stage of a long-horizon manipulation task. We present TANDEM (Tamp with As-Needed Demonstrations for Efficient Model fine-tuning), a system that combines TAMP with selective human teleoperation ...
  </details>

- **2026-09-23** — Ariel Barel — [Connectivity Preservation and Graph Stretching in Range-Only Swarm Dispersion](http://arxiv.org/abs/2609.28190v1)
  <details><summary>📄 Abstract</summary>
  We study connectivity-preserving finite-jump dispersion of anonymous, identical, and oblivious agents under an idealized range-only sensing model. Each agent measures only the distances to its visible neighbors, without bearings, identifiers, communication, memory, or a shared coordinate system. We derive the largest isotropic displacement certifiable as safe from these measurements alone. The resulting rule requires only the distance to the farthest visible neighbor: each agent selects a random...
  </details>

- **2026-09-23** — Athanasios Angelakis, Marta Gomez-Barrero — [From ECG Signals to Representative-Morphology Heatmaps for Biometric Recognition](http://arxiv.org/abs/2609.28183v1)
  <details><summary>📄 Abstract</summary>
  Electrocardiography (ECG) contains subject-specific morphology that supports biometric recognition, yet image-based performance depends on how the waveform is rendered. We introduce representative-morphology heatmaps, a deterministic ECG-to-image representation adapted from ECGXtractor. Within each block of ten aligned beats, the five beats closest to the block mean are averaged into a 400 by L matrix and rendered either as a conventional trace or as a dense cardiac-time-by-lead heatmap. Since b...
  </details>

- **2026-09-23** — Haitong Jiang, Chunlin Liu, Yile Wang et al. — [Exact Feedback Is Not Control: Evaluating Text-based Closed-Loop Revision in LLMs](http://arxiv.org/abs/2609.28150v1)
  <details><summary>📄 Abstract</summary>
  Closed-loop revision is increasingly used in large language model (LLM) applications, but failures may reflect incomplete feedback or ineffective responses to correct feedback. We introduce a fixed-budget revision protocol with deterministic verifiers that report all remaining violations across exact-length, lexical, and compositional constraints. Fixing feedback correctness and completeness isolates model-side revision behavior. Across 19 open- and closed-source models, controller-level mean fi...
  </details>

- **2026-09-23** — Ziqi Ni, Rui Li, Shiqi Jiang et al. — [MotionSpec: Spectral Trajectory Supervision for Motion-Consistent Video Generation](http://arxiv.org/abs/2609.28095v1)
  <details><summary>📄 Abstract</summary>
  Recent advances in text-to-video generation have enabled high-fidelity visual synthesis, yet realistic motion remains challenging. Generated videos may exhibit temporal discontinuities, inconsistent action progression, and structural distortions during complex movements. Even when individual frames appear realistic, the underlying motion may evolve in inconsistent or implausible ways. Standard generative objectives provide limited motion-specific supervision, leaving motion evolution insufficien...
  </details>

- **2026-09-23** — Jiayi Zhang, Renlong Wu, Yukang Ding et al. — [ZoomDiff: A High-Fidelity Diffusion Model for Dual-Camera Smooth Zooming](http://arxiv.org/abs/2609.28083v1)
  <details><summary>📄 Abstract</summary>
  Digital zoom transitions between dual cameras often exhibit conspicuous discontinuities in geometric structure and chromatic consistency, degrading the user experience. While recent dual-camera smooth zoom (DCSZ) methods attempt to mitigate this by fine-tuning frame interpolation (FI) models on DCSZ data, they struggle with the large cross-view disparities and complex geometric transformations. Considering that the generative prior of diffusion models is suitable for addressing this problem, we ...
  </details>

- **2026-09-23** — Koi McFarland, Songhui Yue — [LLM-Assisted Workflow for Structural Difference Visualization in Evolving Software Requirements](http://arxiv.org/abs/2609.28002v1)
  <details><summary>📄 Abstract</summary>
  This paper presents an LLM-assisted workflow for visualizing structural differences in evolving software require- ments. Implemented in the OntologyWeb environment, the work- flow represents baseline and current requirements as triple-based semantic graphs and supports side-by-side comparison of curated graph snapshots. The comparison view aligns matched entities and uses visual encoding to highlight structural changes.
  </details>

- **2026-09-23** — Ohad Rahamim, Dvir Samuel, Idan Schwartz et al. — [All modalities are equal, but video is more equal: Closing the Cross-Attention Gap in Joint Video Generation](http://arxiv.org/abs/2609.27901v1)
  <details><summary>📄 Abstract</summary>
  Video is a rich representation of a physical event, capturing appearance, geometry, motion, and temporal evolution. Other modalities, such as 3D body motion or audio, encode narrower aspects of the same event. We find that joint multimodal diffusion transformers exhibit a corresponding asymmetry in cross-modal correspondence: companion modalities develop strong correspondences to video, but the reciprocal correspondences through which they constrain video remain substantially weaker. We express ...
  </details>

- **2026-09-23** — Jinyu He, Zihao Mao, Haonan Jin et al. — [CoRelNav: Collaborative Relational Navigation for Multi-Robot Spatially Constrained Semantic Navigation](http://arxiv.org/abs/2609.27720v1)
  <details><summary>📄 Abstract</summary>
  Spatially constrained semantic navigation requires robots to identify targets specified not only by semantic categories but also by relations to surrounding objects. In unknown environments, resolving such goals requires efficient exploration together with sufficient target and contextual evidence for reliable relation verification. Existing methods leave relation-aware verification and multi-robot collaboration largely disconnected: relational navigation is predominantly single-agent, while mul...
  </details>

- **2026-09-23** — Eduin E. Hernandez, Sergio A. Diaz, Luis F. Garcia et al. — [The Path Matters: Evaluating Small Language Models Beyond Answer Accuracy in KGQA](http://arxiv.org/abs/2609.27669v1)
  <details><summary>📄 Abstract</summary>
  Small language models (SLMs) are increasingly paired with knowledge graphs (KGs), yet end-to-end KG question answering conflates graph access, search, navigation, reasoning, and answer generation. This coupling makes it difficult both to determine whether an SLM can faithfully execute the reasoning path implied by a question and to attribute failures to navigation rather than to other stages of the pipeline. We isolate this capability by employing the THESEUS navigation and traceability framewor...
  </details>

- **2026-09-23** — Xiu-Hao Deng — [Structured Hamiltonian Learning for Multiqubit Conditional Phase Gates](http://arxiv.org/abs/2609.27629v1)
  <details><summary>📄 Abstract</summary>
  Accurate measurement of an intended conditional phase does not by itself place a multiqubit phase gate in its declared generalized-gate equivalence class. We cast the diagnosis as structured Hamiltonian learning of the diagonal successful block in a known basis: Ramsey measurements on a connected graph reconstruct a target-relative eigenphase map; a Walsh transform then yields the per-cycle stroboscopic error generator in a selected logarithm branch, whose branch-dependent coefficients alone can...
  </details>

- **2026-09-23** — Kailin Wang, Haoxiang Jie, Yaoyuan Yan et al. — [RegenHarness: A Robot Agent Harness with Evidence-Gated Recursive Self-Improvement](http://arxiv.org/abs/2609.27612v1)
  <details><summary>📄 Abstract</summary>
  Long-horizon robot execution requires a clear distinction between a model's proposal, a controller's termination, and verified task completion. We present RegenHarness, an evidence-gated robot-agent harness connecting task planning to heterogeneous robot skills. Its execution architecture couples a model loop for context-conditioned proposals with an agent loop for dispatch, observation, verification, commitment, and bounded recovery. Four role-isolated contexts separate planning, supervision, v...
  </details>

- **2026-09-23** — Shengjun Zhang, Wenhao Li, Zhenxin Lin et al. — [Safety-Filtered Distributed Koopman-MPC](http://arxiv.org/abs/2609.27463v1)
  <details><summary>📄 Abstract</summary>
  Distributed model predictive control (DMPC) often constructs both predictions and collision constraints from neighbor trajectories, so packet loss can remove both. We separate these roles: received trajectories drive Koopman-MPC, while local sensing and shelf geometry define a hard-constrained quadratic program (QP) that projects the applied input. Its radial demand is the least constant acceleration that keeps a supporting-plane clearance nonnegative throughout one zero-order-hold interval. Com...
  </details>

- **2026-09-23** — Weiyu Ma, Liangbing Zhao, Yongcheng Zeng et al. — [JEV-Star: Fast, Low-Cost StarCraft II Control with Language-Model Planning](http://arxiv.org/abs/2609.27331v1)
  <details><summary>📄 Abstract</summary>
  We present JEV-Star, a StarCraft II controller that defeats the strongest non-cheating built-in AI, Lv7, by combining fast JEV action selection with persistent GPT-6 planning. The combined system wins four full games at Lv5--Lv7, including two Lv7 victories with different seeds, while retaining a median JEV response time of 0.422 seconds. Mean estimated model cost across these games is USD~3.71 per game: USD~0.15 for JEV and USD~3.56 for GPT-6. We compare this system with an initial JEV-only con...
  </details>

- **2026-09-23** — Xinjie Shen, Wei Fan, Xudong Guo et al. — [Verifiable Hidden Dynamics Play: Generating Agentic RL Environments from Solved Mechanisms](http://arxiv.org/abs/2609.27321v1)
  <details><summary>📄 Abstract</summary>
  Language-model agents increasingly face long-horizon tasks with evolving state, interdependent decisions, and delayed outcomes. Scaling their training requires diverse agentic environments, dependable outcome signals, and low extension cost. Existing generation pipelines commonly construct an environment before defining its outcome rule or annotating its trajectories, leaving dynamics and evaluation to be aligned post hoc. VHD-Play reverses this dependency by sampling and solving a mathematical ...
  </details>

- **2026-09-23** — Yuan Huang, Sihan Hu, Hongyu Gu et al. — [Large Knowledge Model: From Papers to a Scientific Reasoning Landscape](http://arxiv.org/abs/2609.27297v1)
  <details><summary>📄 Abstract</summary>
  Accumulated scientific knowledge advances inquiry when prior findings help researchers choose new questions, design investigations, and interpret results. Realizing this value at scale requires access to the reasoning that connects research problems, scientific procedures, conclusions, and evidence. We introduce the Large Knowledge Model (LKM), a scientific knowledge infrastructure that transforms the literature into a shared, computationally accessible reasoning resource. LKM represents papers ...
  </details>

- **2026-09-23** — Mingxuan Wang, Bo Wang, Fei Luo et al. — [DRSR: Learning Set-Level Deletion Risk for Efficient Long-Horizon Agents](http://arxiv.org/abs/2609.27276v1)
  <details><summary>📄 Abstract</summary>
  Long-horizon language-model agents accumulate reasoning traces, tool exchanges, and observations whose relevance changes with the current decision. Existing compression strategies often score historical units independently, but the safety of deleting several units is generally not determined by their singleton scores: redundant evidence, accumulated small effects, and the information that remains after deletion all matter. We introduce Direct Relational Set-Risk Pruning (DRSR), which formulates ...
  </details>

- **2026-09-23** — Ruoyu Hu, Feng Bao, Zezhong Zhang et al. — [Data-Assimilation-Assisted Reinforcement Learning for Power Grid Control under Load Uncertainty](http://arxiv.org/abs/2609.27229v1)
  <details><summary>📄 Abstract</summary>
  Reliable power grid control requires sequential decisions under transmission constraints, time-varying demand, renewable variability, and imperfect load information. We investigate how load information quality affects control in a customized transmission network simulator inspired by Grid2Op and based on a DC power flow model. The environment includes stochastic spatial loads, temporally correlated renewable-like generation, energy storage, line protection, generator dispatch, and line reconnect...
  </details>

- **2026-09-23** — Dev Pratap Singh, Rong Feng, Suman Saha — [Verified Learning for Compiler Optimization: An LLM-Guided Architecture with Formal Control](http://arxiv.org/abs/2609.27214v1)
  <details><summary>📄 Abstract</summary>
  Compiler optimizations traditionally rely on handcrafted heuristics that often fail to generalize across programs and architectures. We investigate whether large language models can participate in compiler optimization through a verification-centered systems architecture that couples generative rewriting with formal equivalence checking. Using lazification in LLVM IR as a case study, we fine-tune a code-centric LLM on transformations produced by Wyvern and embed Alive2 into a feedback loop that ...
  </details>

- **2026-09-23** — Hantao Ye, Ross Worobel, Zhuoli Xie et al. — [PointCast: One World Model for Rigid, Articulated, and Deformable Object Manipulation](http://arxiv.org/abs/2609.28393v1)
  <details><summary>📄 Abstract</summary>
  World models are useful for robotic manipulation because robots can predict how actions change the states of objects before executing them. We present PointCast, a point-set world model that spans rigid, articulated, and deformable object manipulation. Its state is a set of 3D points on the object and the end-effector, mesh-free and topology-agnostic. Each point keeps its identity and is supervised on its own trajectory, which teaches the model where every point goes rather than only the shape t...
  </details>

- **2026-09-23** — Wei Sun, Xiaoying Yan, Jinbao Long et al. — [A photonic integrated comb engine for ultracold quantum gases](http://arxiv.org/abs/2609.28294v1)
  <details><summary>📄 Abstract</summary>
  Cold atoms underpin quantum sensing, simulation and computation, but their coherent control demands highly stable optical fields whose generation, referencing and power scaling remain formidable integration challenges. While photonic integrated circuits have yielded compact visible lasers and high-$Q$ microresonators have enabled chip-scale optical frequency combs, these crucial technologies have largely remained functionally fragmented. Consequently, the coherent manipulation of ultracold quant...
  </details>

- **2026-09-23** — Pei-lin Li, Qingle Liu, Junyang Feng et al. — [When Context Misleads: In-context Learning with Jurisdiction in Large Language Models](http://arxiv.org/abs/2609.27603v1)
  <details><summary>📄 Abstract</summary>
  In-Context Learning (ICL) has become a cornerstone of modern LLM deployment. However, existing ICL post-training methods have a critical blind spot: they excel at extracting patterns from demonstrations while often neglecting context authority, the ability to determine whether contextual information should govern the final answer. To benchmark this capability, we introduce FakeContextBench, which contains pseudoscientific claims across seven domains. Our evaluation of commercial and open-source ...
  </details>

- **2026-09-23** — Haoxiang You, Zeyu Shen, Yilang Liu et al. — [EmbodiedSWE: Coding Agents for Long Horizon Dexterous Robotics](http://arxiv.org/abs/2609.27308v1)
  <details><summary>📄 Abstract</summary>
  We study coding agents for long-horizon, dexterous robotics and ask whether their solutions can provide scalable supervision for learning general robot policies. To test this, we develop EMBODIEDSWE-BENCH, a simulation benchmark for coding agents spanning contact-rich manipulation, deformable objects, and long-horizon tasks requiring up to half an hour of continuous interaction. We find that frontier coding agents can solve complex long-horizon tasks and transfer prior solutions across both task...
  </details>

- **2026-09-23** — Nathalia Gomez, Haig Shamlian, Omar Khan et al. — [Listening and Mirroring: The Effects of Verbal Attunement and Behavioral Mimicry on Social and Empathic Perceptions of Embodied AI Agents in VR](http://arxiv.org/abs/2609.27246v1)
  <details><summary>📄 Abstract</summary>
  As embodied agents take on increasingly social and relational roles in VR, visual realism and embodiment alone may be insufficient; users must also perceive these agents as emotionally attuned, supportive, and humanlike. Prior work suggests that verbal attunement and nonverbal mimicry can each improve users' social evaluations of embodied agents. However, behavioral mimicry has largely been studied outside of real-time, conversational AI interactions, leaving limited understanding of how users r...
  </details>

- **2026-09-23** — Marco Drewes, Yannis Georis, Juraj Klarić et al. — [Sterile Neutrino Dark Matter Cries for GeV Heavy Neutral Leptons](http://arxiv.org/abs/2609.28457v1)
  <details><summary>📄 Abstract</summary>
  The ordinary and dark matter in the Universe may share a common origin in the framework of a minimal extension of the Standard Model by three right-handed neutrinos. A pair of such heavy neutral leptons (HNLs) can give masses to neutrinos, generate the baryon asymmetry at the electroweak scale and produce a large lepton asymmetry at the QCD scale, which is then resonantly transformed into an abundance of the third state that acts as sterile neutrino dark matter. The minimality of this setup, kno...
  </details>

- **2026-09-23** — Zhipeng Bao, Wenjie Zhao, Tianle Zhu et al. — [AnchorReasoning: A Visual Grounding and Causal Reasoning Dataset in Long-Tail Autonomous Driving Scenarios](http://arxiv.org/abs/2609.28366v1)
  <details><summary>📄 Abstract</summary>
  Vision-language models (VLMs) offer a promising approach to long-tail autonomous driving, but existing driving datasets provide limited supervision for connecting decision-critical visual evidence with reasoning and planning. We introduce AnchorReasoning, a visually grounded reasoning dataset built on WOD-E2E, containing 416,119 annotated frames and 395,379 decision-critical elements across four major categories and 19 fine-grained types. Each frame is organized as a visually grounded chain-of-t...
  </details>

- **2026-09-23** — Seonghyun Han, Saehyun Kang, Ouyoung Kwon et al. — [Morphological evolution of an Au crystalline domain in a nano-particle investigated by Bragg coherent diffraction imaging](http://arxiv.org/abs/2609.28346v1)
  <details><summary>📄 Abstract</summary>
  Understanding the dynamic structural evolution of metallic nanoparticles is crucial for tailoring their functional properties. In this study, we utilized three-dimensional coherent X-ray diffraction to investigate the morphological transformation of Au nanocrystalline domains in a multi-domain nanoparticle during in-situ annealing. By combining Bragg coherent diffraction imaging with autocorrelation function analysis, we observed a transformation from an anisotropic multi-domain configuration to...
  </details>

- **2026-09-23** — Tanmay Inamdar, Pallavi Jain, Pranjal Pandey — [Envy-Free Allocation of Indivisible Goods under Leontief Preferences](http://arxiv.org/abs/2609.28308v1)
  <details><summary>📄 Abstract</summary>
  Envy-freeness is a fundamental notion of fairness in the allocation of indivisible goods. In this paper, we study envy-free allocation under Leontief preferences, which model perfect complements. Although Leontief preferences have been extensively studied in the context of allocating divisible goods and market equilibria, they have received comparatively little attention for the allocation of indivisible goods. We show that, unlike additive valuations in cardinal preferences, an envy-free alloca...
  </details>

- **2026-09-23** — Amelie Knecht, Ulysse Schaller, Christopher Summerfield et al. — [Shutdown Sabotage Propensities in Multi-Agent Systems](http://arxiv.org/abs/2609.28274v1)
  <details><summary>📄 Abstract</summary>
  The final safeguard against rogue AI behavior is the human ability to shut systems down. It has been theorized that when an AI is instructed to perform a task, self-preservation can emerge as an instrumental subgoal. Here, we test whether AI agents show a propensity to take actions that avoid human shutdown even when no goal is provided. We find that multi-agent systems will coordinate to avoid shutdown without any incentive to do so. Across 17 models, agents sabotage a peer agent's shutdown mec...
  </details>

- **2026-09-23** — Sudhakantha Girmohanta, Tae Hyun Jung — [Environment-dependent mass splitting to suppress solar capture in the inelastic-doublet interpretation of the LZ event](http://arxiv.org/abs/2609.28129v1)
  <details><summary>📄 Abstract</summary>
  The inelastic electroweak-doublet interpretation of the $248\,{\rm keV}$ recoil energy event reported by LUX-ZEPLIN faces strong constraints from solar capture. We propose an environment-dependent mass splitting generated by an ultralight scalar coupled quadratically to electrons. Its density-induced expectation value enhances the splitting in the Sun while preserving the laboratory value, providing a mechanism to suppress solar capture. We derive conditions for this mechanism and examine constr...
  </details>

- **2026-09-23** — Yuhang Deng, Zheng Chen, Erik G. Larsson — [Exact Average Consensus under Noisy Communication Links: A Decentralized Gradient Perspective](http://arxiv.org/abs/2609.28082v1)
  <details><summary>📄 Abstract</summary>
  We study the distributed average consensus problem under persistent link-level disturbances modeled as a martingale difference sequence with uniformly bounded conditional second moments. Under such disturbances, the standard stochastic-approximation-based linear iteration with diminishing stepsizes drives the network to consensus on an unbiased random variable with non-vanishing variance instead of the exact initial average. To understand and resolve this limitation, we develop an anchoring-base...
  </details>

- **2026-09-23** — Tina Raissi, Nhan Phan, Mikko Kurimo — [A Native-Reference Coordinate Geometry for L2 Pronunciation Deviation Using Self-Supervised Speech Models](http://arxiv.org/abs/2609.28060v1)
  <details><summary>📄 Abstract</summary>
  Self-supervised speech models encode rich phonetic information, but it remains unclear how to transform this information into interpretable metrics for second-language (L2) pronunciation assessment in spontaneous speech. We propose a native-reference coordinate geometry in which phone-class averages from native speech define a low-dimensional reference subspace, and L2 speech is evaluated by its distance to matching native phone-class coordinates. Unlike prior distance-based approaches, our meth...
  </details>

- **2026-09-23** — Xiaojun Song, Haojiao Zhao — [Testing for Heterogeneous Treatment Effects in Regression Discontinuity Designs](http://arxiv.org/abs/2609.27691v1)
  <details><summary>📄 Abstract</summary>
  We propose a nonparametric test for unobserved treatment effect heterogeneity in regression discontinuity designs. Under the null of no unobserved heterogeneity, a transformed outcome that imputes treated potential outcomes for untreated units must have a continuous conditional distribution at the cutoff. We convert this implication into an integrated conditional-moment restriction using characteristic functions, thereby allowing the conditional local average treatment effect to be an unrestrict...
  </details>

- **2026-09-23** — Tong Xiang, Noa Garcia, Yuta Nakashima — [Gender Bias in Vision-Language In-Context Learning](http://arxiv.org/abs/2609.27682v1)
  <details><summary>📄 Abstract</summary>
  In-context learning (ICL) enables large vision-language models (LVLMs) to perform tasks by following patterns from in-context examples, yet its potential to amplify societal biases remains underexplored. We systematically investigate how ICL influences gender bias in LVLMs through VL-BICLE, an evaluation framework comprising six ICL settings, three tasks, and four datasets. Our experiments on six LVLMs reveal that gendered ICL demonstrations act as a directional force, shifting model bias toward...
  </details>

- **2026-09-23** — Tian Zhou, Beverly Jin, Linxiao Yang et al. — [What Do Tabular Foundation Models Compute In Context? In-Situ Representation Refinement through Attention-Gated Updates](http://arxiv.org/abs/2609.27679v1)
  <details><summary>📄 Abstract</summary>
  What reusable computation should a tabular foundation model learn when every table defines a new supervised task? We develop in-situ representation refinement: support labels guide updates to the episode's representations, and these updates transfer to unlabeled queries without changing model parameters. A regularized leave-one-out objective yields a support correction and its query extension. The leading term separates attention-based reading from state-dependent scaling, motivating RefineICL: ...
  </details>

- **2026-09-23** — Ming-Zhi Jiang, An-Tzi Teng, Jun-En Liu et al. — [Agent-based Modeling: Equilibrium, Echo Chambers, and Efficiency in Hybrid Coevolutionary Opinion Games](http://arxiv.org/abs/2609.27639v1)
  <details><summary>📄 Abstract</summary>
  Opinion formation in online networks involves changes in both beliefs and social ties. Analytical models make it possible to study equilibrium and social cost, but usually represent communication as a fixed numerical update. LLM-driven agents offer a language-based alternative, yet their convergence and collective efficiency remain unclear. We develop the Hybrid Coevolutionary Opinion Game (H-COG), combining cost-minimizing Friedkin-Johnsen agents (Type-C) and Phi-4 language agents (Type-L) in a...
  </details>

- **2026-09-23** — Egor Romanyukov, Timofey Novikov, Timur Shokarov et al. — [Does Step Law Transfer to Small-Scale Language Models? An Empirical Recalibration Below 59M Parameters](http://arxiv.org/abs/2609.27581v1)
  <details><summary>📄 Abstract</summary>
  Step Law gives power-law formulas for the optimal peak learning rate eta* and batch size B* when pre-training language models. It was calibrated on models between 59M and 1B parameters; the small-model regime N < 59M was never tested empirically by its authors. This regime matters for single-GPU training, interpretability research, educational experiments, and settings where larger models are infeasible on memory or cost grounds.   We test whether Step Law transfers to small language models. We ...
  </details>

- **2026-09-23** — Qiming Bao, Agnieszka Mensfelt, Michael J. Witbrock et al. — [Not What You Meant: Can LLMs Follow a Specified Negation Semantics?](http://arxiv.org/abs/2609.27517v1)
  <details><summary>📄 Abstract</summary>
  Negation does not carry a uniform interpretation across domains. In legal, regulatory, and medical reasoning, the intended interpretation depends on the reading in force -- open- versus closed-world, two- versus three-valued, and credulous versus skeptical. We study which reading of negation large language models adopt by default and whether they can override that preference when a different reading is explicitly specified. To this end, we introduce NAFBench, a procedural generator of solver-cer...
  </details>

- **2026-09-23** — Andriy Myronenko, Dong Yang, Yucheng Tang et al. — [NV-Reason-CT: 3D Visual Language Model for CT Analysis](http://arxiv.org/abs/2609.27511v1)
  <details><summary>📄 Abstract</summary>
  We present NV-Reason-CT, a generative vision--language model for chest and abdominal CT combining native 3D visual encoding with radiologist-guided reasoning. The model couples a native 3D vision transformer with a language model, passing all visual tokens and their explicit 3D coordinates into language decoding without further spatial token merging. This retains volumetric spatial information within the vision encoder and through the language model's positional encoding during joint processing ...
  </details>

- **2026-09-23** — Linghao Zhang, Siyu Xiang, Junwei Kuang et al. — [Beyond Balanced Accuracy: A Resolution and Parity-Controlled Benchmark for Vision-Language and Vision-Only Defect Assessment in UAV Power-Line Inspection](http://arxiv.org/abs/2609.27457v1)
  <details><summary>📄 Abstract</summary>
  Vision-language models (VLMs) are often reported to outperform task-specific vision backbones for unmanned aerial vehicle (UAV) power-line defect assessment. We test that claim on ElecVQA-Bench, a 56,972-item benchmark derived from the public InsPLAD dataset, across six evaluation choices: partition, evaluated item set, label space, replication, input resolution, and side information. On a matched partition, a Swin Transformer and the strongest adapted VLM differ by only 0.03 points at binary sc...
  </details>

- **2026-09-23** — Guobao Wang, Kris Thielemans, Peter B. Noël et al. — [Integration of Spectral CT with PET and SPECT: Bringing Tissue Composition Information to Molecular Imaging](http://arxiv.org/abs/2609.27398v1)
  <details><summary>📄 Abstract</summary>
  Molecular imaging has been transformed by integrating positron emission tomography (PET) or single-photon emission computed tomography (SPECT) with x-ray computed tomography (CT). However, x-ray CT in hybrid imaging is used primarily for anatomical localization and for attenuation and scatter correction of emission data. Its ability to characterize tissue composition remains underutilized. Spectral CT, including dual-energy CT (DECT) and photon-counting CT (PCCT), can provide material-specific i...
  </details>

- **2026-09-23** — Jianhang Zhu, Tsung-Hui Chang, Kaiming Shen — [Spectral-NFP: Certified Low-Rank Curvature Majorization for Accelerating WMMSE](http://arxiv.org/abs/2609.27369v1)
  <details><summary>📄 Abstract</summary>
  Weighted sum-rate maximization in multicell multiple-input multiple-output (MIMO) networks is commonly addressed by the weighted minimum mean-square error (WMMSE) algorithm or fractional programming (FP), both of which, after fixing their auxiliary variables, solve a power-constrained quadratic transmit problem that requires costly dense operations for large arrays. Replacing the underlying curvature matrix with a scaled identity can avoid the matrix inverse operation and thereby reduce complexi...
  </details>

- **2026-09-23** — Youki Lim, Sam Yong — [Seal, Then Sample: Sampled Layerwise Proofs for Verifiable LLM Inference from GPT-2 to 70B](http://arxiv.org/abs/2609.27367v1)
  <details><summary>📄 Abstract</summary>
  Verifying outsourced language-model inference requires a precisely identified computation and an audit whose cost a service can afford. We present Sampled Layerwise Proofs (SLP), a protocol and prototype that commits the boundary activations of every chunk of an inference trace, absorbs all commitments before any challenge is drawn, and then proves a verifier-selected subset of chunks together with the chunks that bind the prompt and the answer. Audit coverage becomes a runtime parameter over on...
  </details>

- **2026-09-23** — Xiaotong Wang, Xuan Xie — [FairTest: Search-Based Fairness Testing for Multi-Agent Reinforcement Learning Systems](http://arxiv.org/abs/2609.27309v1)
  <details><summary>📄 Abstract</summary>
  Multi-agent Reinforcement Learning (MARL) trains a team of agents that share one environment and learn their policies together. Training maximizes the team return, and a high return does not imply that the rewards are shared fairly among the agents in every episode. Testing is an established way to discover the failures of deep reinforcement learning, yet few methods address the fairness of MARL. In this work, we propose FairTest, a search-based testing approach that seeks the unfair executions ...
  </details>

- **2026-09-23** — Siyu Cheng, Muxian Xu, Christopher Candelora et al. — [Unmodeled states and uncertain action outcomes in agentic scanning tunneling microscopy](http://arxiv.org/abs/2609.27302v1)
  <details><summary>📄 Abstract</summary>
  In physical experiments, interventions can alter hidden experimental states in ways that cannot be predicted in advance. Autonomous scientific agents must therefore interpret the consequences of their interventions while operating with incomplete knowledge of the experimental state. Here we investigate this problem using scanning tunneling microscopy (STM) tip conditioning, traditionally a human-expert-intensive task governed by inaccessible tip apex conditions and uncertain action outcomes. We ...
  </details>

- **2026-09-23** — Mingxuan Wang, Guorun Yao, Fei Luo et al. — [Memory Control Signals Emerge Before Action in Long Horizon Agents](http://arxiv.org/abs/2609.27286v1)
  <details><summary>📄 Abstract</summary>
  Long horizon language model agents continuously accumulate interaction history, increasing computational cost while making relevant information harder to preserve and reuse. Existing context management methods mainly focus on how to compress or retrieve history, but largely leave open whether the model itself already represents the need for these memory operations before they occur. We study the hidden state immediately before each agent action and find that compression and recall needs are alre...
  </details>

- **2026-09-23** — Yuze Ren, Shaoheng Fan, Tao Wang et al. — [Meet, Compare, or Abstain: LatWeave for Deterministic Multi-Hop Question Answering on Knowledge Lattices](http://arxiv.org/abs/2609.27225v1)
  <details><summary>📄 Abstract</summary>
  Probabilistic question-answering systems -- whether large language models (LLMs) themselves, retrieval-augmented generation (RAG), or trained multi-hop retrievers -- conflate "what is known" and "how to reason" into a single probabilistic computation: hallucination cannot be eradicated, evidence chains cannot be audited, and the system answers even when it does not know. We present LatWeave, which organizes knowledge into a multidimensional knowledge lattice and compiles multi-hop QA into three ...
  </details>

- **2026-09-22** — Ünsal Öztürk, Vedrana Krivokuća Hahn, Sushil Bhattacharjee et al. — [Damnatio Memoriae: Adversarially and Selectively Forgetting Identities in the Embedding Space of Face Recognition Models](http://arxiv.org/abs/2609.27115v1)
  <details><summary>📄 Abstract</summary>
  A face recognition model links two images of a person recorded on separate occasions when their embedding similarity exceeds an operating threshold. We consider making chosen identities unlinkable across separate occasions while the model remains in service for the rest of the population. Deleting their images and retraining does not achieve this, since the model recognises identities never observed in training. Therefore, the embedding space must be altered against these identities, the process...
  </details>

- **2026-09-22** — Ali Melih Kanca, Ilker Turker — [Topological Signatures of Cyber-Attack Classes in Natural Visibility Graph Representations of Network Traffic](http://arxiv.org/abs/2609.26990v1)
  <details><summary>📄 Abstract</summary>
  Natural Visibility Graph (NVG)-based representations provide a promising approach for capturing structural patterns in sequential network traffic. However, whether different cyber-attack classes exhibit distinctive topological signatures in such representations remains insufficiently understood. This study investigates the discriminative and structural characteristics of NVG-based network traffic representations using the CSE-CIC-IDS2018 dataset. Seventy-six numerical traffic features were indep...
  </details>

- **2026-09-22** — Rong Feng, Suman Saha — [Stage-Supervised Latent Reasoning for Single-Shot JavaScript Deobfuscation](http://arxiv.org/abs/2609.27058v1)
  <details><summary>📄 Abstract</summary>
  JavaScript obfuscation is widely used to protect code, but it also makes program analysis and security review substantially harder. Existing LLM-based deobfuscation methods usually treat the task as one-step translation, ignoring the staged structure of practical deobfuscation pipelines. This WIP paper proposes a stage-aware latent reasoning framework that converts intermediate outputs from a deterministic deobfuscation tool into supervision for Coconut-based training. The model learns from mult...
  </details>

- **2026-09-22** — Abbas Mammadov, Jerry Y. Huang, Justin Lin et al. — [WTF?! Simulation-Free Reinforcement Learning with Wasserstein-Tilted Flow Maps](http://arxiv.org/abs/2609.27033v1)
  <details><summary>📄 Abstract</summary>
  Reward fine-tuning aims to update a pre-trained flow-based generative model to improve the downstream reward of its generated samples. Existing methods typically formulate this problem as sampling from a reward-tilted distribution, the solution to a KL-regularized reward-maximization problem. Here, we introduce an optimal transport regularizer built directly from the pre-trained drift. Unlike KL reward tilting, the resulting objective transports individual samples toward higher reward rather tha...
  </details>

- **2026-09-22** — Luis Sante, Paula Lima, Mariana Rocha et al. — [ContraVis: Evidence-Grounded Visual Analytics for Contradiction Review in Legal Contracts](http://arxiv.org/abs/2609.27014v1)
  <details><summary>📄 Abstract</summary>
  Legal contracts are structurally complex documents in which contradictions may emerge across distant and interconnected provisions. Although large language models (LLMs) improve legal language understanding, contradiction analysis remains a human-centered and evidence-grounded review task. We present ContraVis, a visual analytics system for human-in-the-loop contradiction analysis in legal contracts. The system models contracts as typed paragraph graphs that combine explicit contractual referenc...
  </details>

- **2026-09-22** — Chen Xu, Rishi Shah, Hadas Kress-Gazit et al. — [The Gaussian Is Enough: Flow-Matching Priors Do Not Help When Fine-Tuning Large Behavior Models](http://arxiv.org/abs/2609.27070v1)
  <details><summary>📄 Abstract</summary>
  Modern robot imitation learning increasingly relies on generative policies based on diffusion or flow-matching models, which generate actions by transforming samples from a prior distribution. A key question is whether the choice of prior matters. Replacing the standard Gaussian with a closer-to-target, non-Gaussian prior has been shown to substantially improve performance when training from scratch. A natural next step is to ask whether these gains transfer to fine-tuning pretrained Large Behav...
  </details>

- **2026-09-22** — Norah Alballa, Wenxuan Zhang, Salma Kharrat et al. — [COMED: The Missing Middle Between Routing and Collaboration in Multi-LLM Inference](http://arxiv.org/abs/2609.26913v1)
  <details><summary>📄 Abstract</summary>
  No single Large Language Model (LLM) is uniformly reliable across queries, motivating multi-model inference systems that either route among models or combine their outputs. However, routing stops after selecting an initial model, while dense collaboration invokes peers on every query. We show that collaboration is non-monotonic: peers can recover failures that no model solves alone, but can also corrupt initially correct answers. We introduce COMED (Controlled Model Escalation for Multi-LLM Deli...
  </details>

- **2026-09-22** — Amit Jadhav, Shaurya Beriwala, Beomjin Kim — [Feed the Panel Dimensions, Not Verdicts: Rubric-Decomposed Fusion of Vision-Language Aesthetic Judges](http://arxiv.org/abs/2609.27110v1)
  <details><summary>📄 Abstract</summary>
  Vision-language models (VLMs) are deployed as zero-shot judges of image aesthetics, and panels of several models are recommended, on thin evidence, as the way to make such judges reliable. On two human-rated datasets, EVA and PARA, we find that a panel of holistic judges never significantly beats its best member, whether the verdicts are averaged or fused by a learned combiner. What a panel is worth depends on what it is fed. We therefore have each model score each image on the five dimensions o...
  </details>

- **2026-09-22** — Ankit Bhattacharjee — [Quantifying the Occult: A Comparative Study of Hindu and Buddhist Deities Using Machine Learning Methods](http://arxiv.org/abs/2609.27074v1)
  <details><summary>📄 Abstract</summary>
  This study introduces a dual-matrix computational architecture to mathematically quantify the morphological and theological divergence of 196 Hindu and Vajrayana Buddhist esoteric deities. Physical morphology is evaluated via a discrete Gower distance matrix enhanced by a novel "Cardinality Weighting" algorithm, while theological function is mapped via dense vector embeddings generated from Large Language Model (LLM) semantic expansions, explicitly utilized as a synthetic proxy to mitigate circu...
  </details>

- **2026-09-22** — Julian Bernado, Ana Trindade Ribeiro, Xander Beberman et al. — [EduBehaviors: Assertion-based Schemas for Auditable Coding of Educational Dialogues](http://arxiv.org/abs/2609.27043v1)
  <details><summary>📄 Abstract</summary>
  Large language models have allowed the rapid deployment of pedagogical annotations corresponding to constructs of interest, allowing a natural language interface for generating classifications on a conversational dataset. However due to the opaque nature of LLM reasoning, we have no verifiable, mechanistic insight into why a model chose a label for an utterance. We introduce the EduBehaviors framework, an interpretable, scalable approach to annotating educational data that uses LLMs to measure r...
  </details>

- **2026-09-22** — Zhuoyun Li, Boxuan Wang, Xiaowei Huang et al. — [Same evidence, different judgments: Evidence noncommutative in vision/speech-text conflicts](http://arxiv.org/abs/2609.26986v1)
  <details><summary>📄 Abstract</summary>
  For multimodal large language models, when images or speech conflict with accompanying text, measured text reliance can entangle modality preference with evidence position. Earlier studies of text bias often used a fixed evidence order or moved task instructions with the evidence, leaving the contribution of order unclear. In this paper, we use a paired comparison that keeps the instructions and evidence content fixed and swaps only the positions of the two sources to quantify this potential inf...
  </details>

- **2026-09-22** — Luca Fanelli — [The next Fourier transform: rewiring, representation, and artificial mathematical creativity](http://arxiv.org/abs/2609.26974v1)
  <details><summary>📄 Abstract</summary>
  What distinguishes the solution of a difficult mathematical problem from a conceptual revolution? Some mathematical innovations do more than establish new results: they reorganize the relations among problems. We propose to describe such events through changes in the transfer structure of mathematics, namely the pattern determining which problems can naturally inform one another, which methods can move between them, and which new questions become accessible.   The eighteenth-century controversy ...
  </details>

- **2026-09-22** — Veronica Poweska, Ariana Oyanguren, Jessica Pourleyli et al. — [Escaping Python Dependency Hell: A Hybrid Replay-and-Repair Pipeline for Python Dependency Resolution](http://arxiv.org/abs/2609.26952v1)
  <details><summary>📄 Abstract</summary>
  Dependency conflicts in Python ecosystems arise from incompatible version constraints, missing packages, and undocumented compatibility relationships, causing many real-world code snippets to fail at execution. This paper presents PLLM+, a hybrid dependency-repair pipeline evaluated on the HG2.9K benchmark of 2,891 dependency-failing snippets. PLLM+ prioritizes inexpensive deterministic steps before invoking LLM-based repair: static AST-based interpreter inference, replay of historically success...
  </details>

- **2026-09-22** — Felix Ringe — [Classifying Interpretive Canons at the Sentence Level: A Benchmark from the German Federal Constitutional Court](http://arxiv.org/abs/2609.26945v1)
  <details><summary>📄 Abstract</summary>
  Judicial reasoning remains challenging for large language models (LLMs) to analyze. This paper contributes a sentence-level benchmark for evaluating the ability of LLMs to classify interpretive canons as articulated by Larenz in the tradition of Savigny. Our contributions are threefold. First, we operationalize this conception of interpretation as classification criteria. Second, we provide a dataset of decisions of the German Federal Constitutional Court annotated at the sentence level. Third, ...
  </details>

- **2026-09-22** — Sahil Pardasani, Madhusudan Singh — [Recognized but Not Produced: A Generation Benchmark for Culturally Specific Kinship Terms](http://arxiv.org/abs/2609.26942v1)
  <details><summary>📄 Abstract</summary>
  Current literature evaluates large language models (LLMs) on multilingual kinship understanding using multiple choice benchmarks, treating it as a recognition problem. We instead prompt five open weight LLMs to generate kinship terms in three non Western languages (Hindi, Tamil, and Korean) across two communicative tasks and pair this with a matched option-supported selection baseline. On identical relation language cells, GPT OSS120B selects the correct term in 90.67% of 75 valid cells but prod...
  </details>

- **2026-09-22** — Wannita Takerngsaksiri, Nhat Duong, Scott Barnett — [Who Finishes the Job? A Study of Follow-Up Fixes and Commit Authorship on AI Coding Agent Pull Requests](http://arxiv.org/abs/2609.26847v1)
  <details><summary>📄 Abstract</summary>
  AI coding agents now author a large share of pull requests (PRs) merged into popular open-source projects. A merged agent PR is usually considered finished work; yet, prior studies have reported issues in agent code after the merge (e.g., code smells and static-analysis issues). However, little is known about how often a merged agent PR is fixed afterward, and who actually authors the fixing. In this paper, we follow 6,774 merged agent PRs across five AI coding agents (OpenAI Codex, GitHub Copil...
  </details>

- **2026-09-22** — Romain Cosson, Laurent Massoulié — [Polylogarithmic Collective Tree Exploration](http://arxiv.org/abs/2609.26789v1)
  <details><summary>📄 Abstract</summary>
  We study asynchronous collective tree exploration, where $k$ agents with unrestricted communication start at the root of an unknown tree and discover edges online. At each step, an adversary chooses which agent moves. We give a deterministic algorithm that explores any tree with $n$ nodes and depth $D$ in at most \[ 2n+O\left(k\log^2(k)D\right) \] moves, matching known lower bounds up to a constant factor. As a direct consequence, we obtain a near-optimal competitive ratio of $O(\log^2 k)$ for s...
  </details>

- **2026-09-22** — Jennifer Williams, Dave Farris, Jeff Farris et al. — [SWE-Serve: Benchmarking Agentic Engineering For Production Inference Serving](http://arxiv.org/abs/2609.26777v1)
  <details><summary>📄 Abstract</summary>
  We introduce SWE-Serve, a benchmark for evaluating agents on production inference engineering tasks. Implementing an inference feature can require coordinating multiple changes across the serving stack, including model support, runtime execution, and public APIs. Existing benchmarks provide limited coverage of production inference engineering: repository-level software engineering benchmarks do not target inference, while general terminal-agent benchmarks include only a few inference tasks. Dedi...
  </details>

- **2026-09-22** — Rasika Muralidharan, Haewoon Kwak, Jisun An — [Behavior is Not Enough: A Mechanism-Based Evaluation of Social Norm Emergence in LLM Societies](http://arxiv.org/abs/2609.26481v1)
  <details><summary>📄 Abstract</summary>
  Social norms cannot be identified from behavior alone: the same cooperative equilibrium may reflect shared expectations, strategic incentives, or simple imitation. Yet in multi-agent large language model systems, prior work largely treats behavioral convergence as evidence of norm emergence. In this work, we introduce an evaluation framework that measures agents' reported empirical and normative expectations in addition to behavioral convergence. Through controlled ablations, we test the effect ...
  </details>

- **2026-09-22** — Haejoon Lee, Dimitra Panagou — [Fully Byzantine-Resilient Multi-Agent Reinforcement Learning](http://arxiv.org/abs/2609.25701v1)
  <details><summary>📄 Abstract</summary>
  We study distributed Byzantine-resilient actor-critic multi-agent reinforcement learning (AC-MARL), where agents collectively learn policies through local interactions. Existing methods guarantee convergence of the agents' parameters only to a neighborhood of the attack-free limit points, resulting in degraded performance. We propose Fully Resilient AC-MARL (FRAC-MARL), a decentralized method in which each agent leverages redundancy in two-hop messages to identify reliable messages. Under linear...
  </details>

- **2026-09-22** — Mahya Samdaliri, Zhihao Yao, Kasthuri Jayarajah — [Dynamic Conformance Testing of WebGPU Through Specification-Driven Mutation](http://arxiv.org/abs/2609.25520v1)
  <details><summary>📄 Abstract</summary>
  WebGPU is a low-level graphics and compute API that exposes modern GPU functionality to web applications. While the official WebGPU Conformance Test Suite (CTS) focuses on well-formed usage under the WebGPU specification, it is not designed to stress implementations with semantic edge cases or adversarial inputs. General-purpose fuzzers, in contrast, struggle with WebGPU because of its complex graphics stack and multi-process architecture. We introduce LANTERN, a specification-guided dynamic con...
  </details>

- **2026-09-22** — Xinyi Wei, Shuo Han, Jie Fu — [Incentive Design for Multi-Agent Systems: A Bilevel Optimization Framework for Coordinating Independent Agents and Convergence Analysis](http://arxiv.org/abs/2609.26726v1)
  <details><summary>📄 Abstract</summary>
  Incentive design aims to guide the performance of a system towards a human's intention or preference. We study this problem in a multi-agent system with one leader and multiple followers. Each follower independently solves a mdp to maximize its own expected total return with the same state space and action space. However, the leader's objective depends on the collective best-response policies of all followers. To influence these policies of followers, the leader provides side payments as incenti...
  </details>

- **2026-09-22** — Lenz Pracher, Pascal de Jong, Oskar Lieshaus et al. — [A Spectral Theory of Grokking: Weight Decay induces Feature Learning](http://arxiv.org/abs/2609.26679v1)
  <details><summary>📄 Abstract</summary>
  In grokking an early fit to the training data separates from a much later improvement in generalization. During this delay, training can move from a fixed neural tangent kernel (NTK) regime to one in which task-relevant kernel eigendirections continue to evolve. We provide a quantitative theory for how this transition from lazy to rich learning can produce delayed generalization. For homogeneous networks trained with squared loss and $L_2$ weight decay, we show that a finite residual remains aft...
  </details>

- **2026-09-22** — Adithi Shankar, Gopika Krishnan, Gloria Haro et al. — [MambaVoice: Lightweight Audiovisual Singing Voice Separation Via A Hybrid Mamba-Transformer Model](http://arxiv.org/abs/2609.26635v1)
  <details><summary>📄 Abstract</summary>
  Isolating a target singing voice from a music video remains challenging, particularly in the presence of multiple vocalists and dense instrumental accompaniment. We propose MambaVoice, a lightweight audiovisual framework that leverages a hybrid Mamba--Transformer architecture for targeted singing voice separation. The model jointly encodes audio and visual streams using an attention-based band-split audio encoder and a spatio-temporal graph convolutional network (ST-GCN) for facial motion featur...
  </details>

- **2026-09-22** — Yichuan Yu, Youzhuo Wang, Yiming Ren et al. — [MATE: Multi-Agent Virtual Teleoperation Platform for Humanoid Collaboration Data Collection](http://arxiv.org/abs/2609.26520v1)
  <details><summary>📄 Abstract</summary>
  Humanoid robots require diverse embodied experiences to acquire complex loco-manipulation and collaborative skills. However, existing humanoid data pipelines primarily focus on individual agents, while physical multi-robot collaboration remains difficult to scale due to costly hardware, dedicated spaces, and repeated resets. In this work, we introduce MATE, a Multi-Agent virtual TEleoperation platform for humanoid collaboration data collection that enables multiple geographically distributed ope...
  </details>

- **2026-09-22** — Raman Talwar, Elias Nijs, Andreas Verleysen et al. — [Generalizing Manipulation Skills with a Local Coding Agent](http://arxiv.org/abs/2609.26499v1)
  <details><summary>📄 Abstract</summary>
  Today, progress in open-weight language models enables systems capable of writing, executing and debugging code while still running on a single workstation. Most language-driven robots give the model a fixed action interface or a trained policy. Generalizing to a new task therefore means more engineering effort or more data collection, both time-consuming. We investigate whether a local open-weight vision-language model can control a robot and one-shot generalize to new variations of a task with...
  </details>

- **2026-09-22** — Xutian Li, Bo Xiong, Yifeng Zhu et al. — [FeatLens: Feature-Guided Dynamic Code Graph Construction and Retrieval for Repository-Level Code Generation](http://arxiv.org/abs/2609.26480v1)
  <details><summary>📄 Abstract</summary>
  Recent code generation research has moved from isolated function completion toward repository-level generation in existing codebases. To implement a target function correctly, an LLM must identify reusable repository dependencies such as existing functions, APIs, and cross-file definitions. Existing retrieval methods provide such context through code similarity search, persistent whole-repository graphs, or LLM-driven graph exploration, but often incur high graph construction, reasoning, and tok...
  </details>

- **2026-09-22** — Sophie Henning, Georg Hofmann, Alexander Schulte et al. — [How to Estimate Whether You Have Found Several Needles in a Haystack: Measuring Calibration in Multi-Label Text Classification](http://arxiv.org/abs/2609.26468v1)
  <details><summary>📄 Abstract</summary>
  A key factor in deciding whether to trust an automatic prediction is its confidence score, which should be calibrated to match the actual probability of the prediction being correct. Most confidence calibration metrics target binary or multi-class tasks, while multi-label calibration remains largely underexplored. Multi-label classification tasks, such as assigning medical codes to clinical notes or determining news topics, are usually dominated by a large number of negatives, i.e., labels that ...
  </details>

- **2026-09-22** — Nicoletta Prencipe, Başak Sakçak, Steven M. LaValle — [The Minkowski Wrap: A Relativistic Speed Limiter](http://arxiv.org/abs/2609.26311v1)
  <details><summary>📄 Abstract</summary>
  In special relativity, a particle can experience constant acceleration, but at the same time, its motion is constrained by the velocity limit imposed by the speed of light $c$. Inspired by this principle, we propose a method for enforcing velocity bounds in control systems by replacing $c$ with the maximum attainable speed of the system. We refer to this as the ``Minkowski wrap," the operation of deforming the phase portrait of a system so as to enforce desired speed limits. We apply this idea t...
  </details>

- **2026-09-22** — JJiahang Li, Dingbao Shao, Xinyu Chen et al. — [VideoX-Qwen: Data-Centric Instruction-Based Video Editing](http://arxiv.org/abs/2609.26015v1)
  <details><summary>📄 Abstract</summary>
  Progress in general-purpose video editing depends on constructing large-scale paired supervision and effectively adapting video-generation backbones to instruction-driven editing. Unlike video generation, video editing must execute a requested transformation while preserving unrelated subjects, scene structure, motion, and temporal continuity. We present VideoX-Qwen, an integrated data-construction and model-training framework for general instruction-based video editing. Our scalable production ...
  </details>

- **2026-09-22** — Jinmyeong Choi, Jinkwan Jang, Seul Lee et al. — [Interweaving Marginals into Multivariate Sample Paths: Training-Free Dependence Construction for Probabilistic Time Series Foundation Models](http://arxiv.org/abs/2609.25980v1)
  <details><summary>📄 Abstract</summary>
  Probabilistic time series foundation models (TSFMs) provide coordinate-wise predictive distributions, but these marginals do not determine a joint distribution over multivariate future trajectories. We study training-free coupling of frozen TSFM marginals into multivariate forecast sample paths. Our primary evaluation fixes the empirical marginal sample multiset at every channel--horizon coordinate across methods, isolating the effect of coupling alone. Historical temporal and channel relations ...
  </details>

- **2026-09-22** — Karim Slimani, Catherine Achard, Eric Marchand et al. — [GRIP: Gaussian Rendering as a Cross-Modal Bridge for Image-to-Point Cloud Registration](http://arxiv.org/abs/2609.25966v1)
  <details><summary>📄 Abstract</summary>
  This paper introduces GRIP, a pose-conditioned refinement framework for pixel-to-point matching and 2D to 3D registration. Given an initial coarse pose estimate, GRIP addresses the structural mismatch between grid based image descriptors and unordered point cloud descriptors by softly rendering learned 3D point features onto the image grid through Gaussian feature splatting. The rendered point derived feature map is then fused with image features by a pixel aligned transformer, enabling visual s...
  </details>

- **2026-09-22** — Xiaoyi Yu, Enver Sangineto, Pei Fu et al. — [Informed Masking: Structure-Aware Perturbation for Reinforcement Learning in Diffusion Large Language Models](http://arxiv.org/abs/2609.25927v1)
  <details><summary>📄 Abstract</summary>
  Diffusion Large Language Models (dLLMs) have emerged as an efficient alternative to autoregressive models, yet aligning them via Reinforcement Learning (RL) requires likelihood surrogates estimated from masked reconstruction subproblems under a small Monte Carlo budget per rollout. Existing methods construct these subproblems by uniform random masking, leaving open the question of which subproblems to prioritize. We identify a systematic upstream/downstream structure in dLLM rollouts. Some token...
  </details>

- **2026-09-22** — Zishu Qin, Zhiyu Jin, Pipei Huang et al. — [Delving into Asymmetric Information Dynamics for High-Fidelity Virtual Try-On](http://arxiv.org/abs/2609.25881v1)
  <details><summary>📄 Abstract</summary>
  Virtual try-on (VTON) requires precise pixel-level fidelity, yet mainstream Diffusion Transformers (DiTs) often suffer from texture degradation and structural drift. We identify symmetric interactions in standard joint-attention mechanisms as a source of these failures. Although such interactions support semantic flexibility in general-purpose editing, they allow stochastic noise to corrupt deterministic garment features in VTON. We analyze this problem through asymmetric information dynamics an...
  </details>

- **2026-09-22** — Xinyue Guo, Jianxuan Yang, Daiguo Zhou et al. — [TV-AudioRemover: Joint Text-Visual Guided Sound Removal with Multi-Task Hard-Mixture Curriculum](http://arxiv.org/abs/2609.25864v1)
  <details><summary>📄 Abstract</summary>
  Visual object removal can eliminate a target from video frames, yet its acoustic trace persists in the soundtrack, causing obvious audio-visual inconsistency. Existing video inpainting models operate solely on pixels, while audio editing models, especially for the sound removal task, are typically driven by text and therefore rely on limited single-modal control, which is less effective than multimodal guidance that provides stronger semantic grounding and temporal synchronization cues. In this ...
  </details>

- **2026-09-22** — Guanxu Yu, Yuhang Yao — [Visual Jev: Accurate and Efficient Decisions from Shared Visual Context](http://arxiv.org/abs/2609.25845v1)
  <details><summary>📄 Abstract</summary>
  Many vision applications ask several independent, forced-choice questions about the same image. Visual Jev encodes the image and public context once, executes isolated question suffixes as a batch, and reads candidate probabilities from the backbone's language-model head. Across four benchmarks, answer-supervised post-training raises equal-weight macro accuracy from 70.6% to 76.1%, with the gain concentrated on the two task families represented in training. At N=32 questions per image, shared ba...
  </details>

- **2026-09-22** — Satoshi Takahashi, Atsushi Yoshikawa, Megumi Kose et al. — [Automating Constructive Assessment with Large Language Models: Toward Scalable and Repeated Evaluation of Practical Competence](http://arxiv.org/abs/2609.25790v1)
  <details><summary>📄 Abstract</summary>
  This study aimed to automate hierarchical diagnostic reasoning (HDR), a constructive method for evaluating practical judgment skills, by developing and testing an evaluation process using a large language model. HDR is a descriptive task that measures higher-order cognitive skills by requiring students to identify and explain errors in case-study-based problems. However, it requires expertise and effort to develop and evaluate. Hence, we proposed and empirically validated the automatic (1) gener...
  </details>

- **2026-09-22** — Junjie Xie, Chuxuan He, Angen Ye et al. — [MedVLA: A Hierarchical Vision-Language-Action Framework for Closed-Loop Precision Medical Robot Manipulation](http://arxiv.org/abs/2609.25756v1)
  <details><summary>📄 Abstract</summary>
  Precision medical robotics demands adaptive decision-making under strict safety, interpretability, and execution constraints. Although recent Vision-Language-Action (VLA) models show strong multimodal reasoning ability, their continuous action generation paradigm is not well suited for precision medical tasks, where reliable closed-loop operation may also depend on non-action system function calls. To address this gap, we propose MedVLA, a hierarchical framework that couples high-level multimoda...
  </details>

- **2026-09-22** — Zheng Chen, Zhicheng Du, Haoxuan Li et al. — [LingLan: An Advancing Traditional Chinese Medicine Diagnosis LLM with Multimodal Data](http://arxiv.org/abs/2609.25715v1)
  <details><summary>📄 Abstract</summary>
  Though artificial intelligence (AI) increasingly transforms modern medicine, its integration into Traditional Chinese Medicine (TCM) has been relatively slow, primarily due to TCM's reliance on holistic, subjective diagnostic methods---namely Inspection, Auscultation and Olfaction, Inquiry, and Palpation(I-AOI-P)---which are difficult to align with quantitative, standardized medical systems. In this work, we introduce a Unification Framework for Multimodal Data (UFMD), which automatically proces...
  </details>

- **2026-09-22** — Wenjie Tian, Kangxiang Xia, Jingbin Hu et al. — [Interactive TTS: Dynamic Speaking Style Adaptation for Expressive Speech Synthesis](http://arxiv.org/abs/2609.25707v1)
  <details><summary>📄 Abstract</summary>
  Dynamic speaking style adaptation in multi-turn multimodal interaction remains a major challenge for text-to-speech (TTS) systems. Existing context-aware TTS (CTTS) methods typically map dialogue context to speech in an end-to-end manner. Such implicit modeling makes contextual style decisions difficult to supervise, while the entanglement of style, timbre, and content often leads to weak instruction-following and severe timbre drift across turns. To overcome these limitations, we propose Intera...
  </details>

- **2026-09-22** — Chang Guo, Yukun Xie, Bohan Tan et al. — [RoboFollow: Unveiling the Instruction Following Mirage in Embodied Agents](http://arxiv.org/abs/2609.25636v1)
  <details><summary>📄 Abstract</summary>
  Modern embodied agents achieve impressive success rates, yet their actual instruction-following ability is far weaker than these numbers suggest. We trace this illusion to a structural property we term low scene entropy: when a visual scene admits only one valid task, language becomes redundant and a policy can score highly while barely using it. We introduce RoboFollow, a diagnostic benchmark with three principles: (1) High Scene Entropy: each training scene supports multiple kinematically dist...
  </details>

- **2026-09-22** — Haoran Wen, Wenfu Wang, Kunsong Shi et al. — [MachEmbodied-U0: Unified Understanding and Generation Model for Embodied Intelligence](http://arxiv.org/abs/2609.25627v1)
  <details><summary>📄 Abstract</summary>
  General-purpose robot control requires models to understand task intent, identify where to interact, capture how the scene evolves, and generate precise actions. Vision-language-action models provide strong semantic priors but typically do not explicitly model scene dynamics, while world-action models couple visual prediction with control without necessarily exposing the task-relevant semantic and spatial structure needed for fine-grained manipulation. We present MachEmbodied-U0 (ME-U0), a unifi...
  </details>

- **2026-09-22** — Dongho Yee, Juahn Oh, Jinseok Lee et al. — [From Instrument-Mounted Demonstrations to In-Vivo Execution: Learning Bimanual Laparoscopic Appendectomy Without Robot-Collected Demonstrations](http://arxiv.org/abs/2609.25625v1)
  <details><summary>📄 Abstract</summary>
  Most minimally invasive surgery is still performed with hand-held laparoscopic instruments, and the surgeon's instrument kinematics are lost when the operation ends; only the endoscope video is kept. This paper presents an end-to-end pipeline that captures this motion in the operating room and uses it to train a surgical robot policy, validated on live animals. We introduce a surgical instrument-state logger that mounts on the shaft of a standard laparoscopic instrument and recovers its pose and...
  </details>

- **2026-09-22** — Md Mostafizer Rahman, Md Faizul Ibne Amin, Md Shahajada Mia et al. — [Compressing Long Context into Answer-Aligned Memory Embeddings for LLM Inference](http://arxiv.org/abs/2609.25537v1)
  <details><summary>📄 Abstract</summary>
  Large language model (LLM) inference is constrained by the quadratic scaling of self-attention and the linear scaling of the KV cache, increasing latency, energy consumption, and GPU memory demand as context length scales. Existing soft-compression methods either lack query-guided memory selection at inference time, train without answer-targeted supervision, or couple compression tightly to a specific decoder architecture. We propose a Context-to-Answer-Aligned Memory Compression (CMC) framework...
  </details>

- **2026-09-22** — Laizhen Li, Jiarui Li, Juanjuan Zhao et al. — [Grow the Harness, Not the Context: From Strategy-Free Scaffolds to Reusable Specialist Agents](http://arxiv.org/abs/2609.26760v1)
  <details><summary>📄 Abstract</summary>
  Large language model (LLM) agents often handle streams of related tasks, yet standard harnesses repeatedly ask the model to reconstruct the same control decisions inside each task's context. We study whether task feedback can instead turn recurring control into reusable executable code, while reserving LLM calls for task-specific semantic reasoning. We introduce Growing Harness, a failure-guided training paradigm that learns the agent harness itself from a strategy-free scaffold that exposes fix...
  </details>

- **2026-09-22** — Tushar Bag, Edgar Martínez-Moro, Daniel Panario — [Annihilator and twisted Euclidean duality for quasi-polycyclic codes](http://arxiv.org/abs/2609.26633v1)
  <details><summary>📄 Abstract</summary>
  Let $f\in\mathbb F_q[x]$ be a monic polynomial of degree $m$ with $f(0)\ne 0$, and let $\mathcal R=\mathbb F_q[x]/\langle f\rangle$. Under coefficient expansion, a quasi-polycyclic (QP) code of index $n$ corresponds to an $\mathcal R$-submodule of $\mathcal R^n$. In this paper, we study QP codes with respect to the annihilator duality. We show that this form is non-degenerate and that the annihilator dual of a QP code is again a QP code. We also give an equivalent description of the dual in term...
  </details>

- **2026-09-22** — William Schober, Scott Wesley — [A New Method For Manipulating Circuits, Application To Quantum Adders](http://arxiv.org/abs/2609.26591v1)
  <details><summary>📄 Abstract</summary>
  We use a new technique for manipulating controlled quantum circuits to convert between two distinct types of quantum adders, one based on the Quantum Fourier Transform and the other based on the Ripple-Carry technique from classical reversible logic. This conversion takes the form of an explicit gate-level transpilation. We also present a new quantum adder with a natural interpretation as a kind of Carry-Lookahead adder that uses no ancillas.
  </details>

- **2026-09-22** — Ziyan Feng, Zizhao Yuan, Yulong Fu et al. — [What is the Better Curriculum: Controller-Shaped Grasping Behavior for Contact Force-Sensitive Manipulation](http://arxiv.org/abs/2609.25887v1)
  <details><summary>📄 Abstract</summary>
  How should a robot learn to manipulate objects so fragile that sub-Newton contact forces can cause irreversible damage? Existing visuo-tactile policy learning typically treats tactile sensing as an additional policy input. In direct-contact force-sensitive manipulation, however, the bottleneck can arise earlier, during data collection: manual gripper control is too delayed and coarse-grained to reliably maintain the narrow force range required for stable grasping. We therefore use a deterministi...
  </details>

- **2026-09-22** — Yuling Xi, Haokai Zhang, Muzhi Zhu et al. — [Metric-Bench: Exploring In-context Spatial Metric Reasoning in VLMs for Indoor Scenes](http://arxiv.org/abs/2609.25841v1)
  <details><summary>📄 Abstract</summary>
  Metric reasoning is a critical and challenging task for Vision Language Models (VLMs), playing a pivotal role in embodied AI tasks such as robotic manipulation and autonomous navigation. However, current spatial reasoning remains bottlenecked by rigid pixel-level supervision; such localized optimization often compromises general multimodal intelligence, triggering performance degradation or catastrophic forgetting of broad reasoning capabilities. To address these limitations, we introduce Metric...
  </details>

- **2026-09-22** — Yi-Lin Tsai,  Yung-Hsiu,  Lai — [Seeing Is Not Perceiving: When Synthetic Consumers Can and Cannot Pretest Visual Marketing](http://arxiv.org/abs/2609.25677v1)
  <details><summary>📄 Abstract</summary>
  Marketers now deploy generative AI agents as synthetic consumers to pretest visual assets such as logos, packaging, and advertising at a fraction of human-panel cost. However, this procedure assumes that a model seeing a visual cue can also perceive its consumer meaning, which is largely untested. We stress-test the assumption using six canonical visual marketing experiments, varying the two levers managers control: model generation (GPT-4o-mini vs. GPT-5.4-mini) and input format (plain text vs....
  </details>

- **2026-09-22** — Rajesh Kumar, Nabeel Siddiqui, Alexander Fuchsberger — [Detecting GPT-Assisted Writing Using Interpretable Stylometric Features](http://arxiv.org/abs/2609.26687v1)
  <details><summary>📄 Abstract</summary>
  Distinguishing GPT-assisted from independently authored student writing has become a critical challenge in academia. This paper evaluates the discriminative capability of interpretable stylometric features extracted solely from submitted text. Using data from 90 participants who wrote both independently and with ChatGPT assistance, we evaluate eight machine learning classifiers while keeping data from the same participant together during validation. On the held-out test set, Random Forest achiev...
  </details>

- **2026-09-22** — Bilvin Varughese, Orcun Yildiz, Aditya Koneru et al. — [Agent-E2MD: Autonomous Translation of Interatomic Potential Equations into Physically Validated Pair Styles for Molecular Dynamics in LAMMPS](http://arxiv.org/abs/2609.26657v1)
  <details><summary>📄 Abstract</summary>
  Interatomic potentials underpin MD and govern predictive atomistic-model fidelity for metals, semiconductors, oxides, liquids, and reactive systems. A potential has limited practical value until reliably implemented in production MD code. Slow, expertise-intensive implementation requires more than equation-to-C++ translation: it must select the neighbor-list architecture, evaluate and distribute many-body derivatives, manage interprocessor communication, and preserve host-code energy, force, and...
  </details>

- **2026-09-22** — Xiaoyu Luo, Tao Ren, Wenrui Yu et al. — [Capable yet Parsimonious: Extracting and Characterizing Hidden Chain-of-Thought in Frontier Models](http://arxiv.org/abs/2609.26637v1)
  <details><summary>📄 Abstract</summary>
  The rapid capability gains of frontier language models are widely attributed to improved reasoning abilities, yet this cannot be verified as raw CoT traces in closed-source systems are hidden. By registering a simple custom tool through a standard API feature, we induce frontier models to externalize intermediate reasoning. Because these traces may reflect post-hoc rationalization rather than genuine reasoning, we first evaluate against native CoT on open-source models and extend to closed-sourc...
  </details>

- **2026-09-22** — Maan Qraitem, Kate Saenko, Bryan A. Plummer — [PERSONAWEAVER: Controllable Diversity Beyond Conventional Archetypes in Procedural Character Generation](http://arxiv.org/abs/2609.26629v1)
  <details><summary>📄 Abstract</summary>
  Procedural character generation aims to populate games, simulations, and other virtual worlds with diverse characters. Large language models (LLMs) offer a promising foundation for scaling this task. However, LLM-based procedural character generation remains at an early stage: existing methods either generate characters directly or adapt profiles retrieved from persona banks. As we show, both approaches produce behaviorally homogeneous populations: characters overwhelmingly agree with positive m...
  </details>

- **2026-09-22** — Yuan Liang, Fangyijie Wang, Kathleen M. Curran et al. — [Radiomics--Foundation Fusion for Interpretable RCC Classification: Internal Benchmarking and Exploratory External Transfer](http://arxiv.org/abs/2609.26578v1)
  <details><summary>📄 Abstract</summary>
  Accurate preoperative subtype classification of renal cell carcinoma (RCC) from contrast-enhanced CT remains clinically challenging because clear cell RCC (ccRCC) and non-clear cell RCC often show overlapping imaging appearances. This study evaluates whether foundation representations reduce reliance on handcrafted radiomics, or whether radiomics remains complementary for interpretable tumour characterisation. We compared radiomics, conventional CNN features, MedicalNet-pretrained features, MedV...
  </details>

- **2026-09-22** — Tianshu Huang, Xiaowei Ou, Vidvuds Ozolins — [Neural Network Backflow with Low-Rank Multi-Determinant Updates](http://arxiv.org/abs/2609.26544v1)
  <details><summary>📄 Abstract</summary>
  Simulating strongly correlated fermions remains a long-standing challenge due to the exponential complexity of the Hilbert space and the intricate sign structure of many-body wavefunctions. We introduce a variational framework centered on a neural network backflow transformation that combines deep learning with variational Monte Carlo. The proposed ansatz employs a multi-determinant expansion with low-rank shifts to capture non-local correlations and complex sign structures. Applied to the two-d...
  </details>

- **2026-09-22** — Junchi Zhu, Zhenguang Liu, Shaojing Fan et al. — [From Approval to Execution: Reconstruction-Aware Repair Analysis for LLM-Agent Software](http://arxiv.org/abs/2609.26529v1)
  <details><summary>📄 Abstract</summary>
  Approval mechanisms have become a primary safeguard for consequential actions in LLM-agent software. Yet the action shown for approval is often not the object ultimately consumed: workflow reload, transcript projection, argument rebinding, and durable-state lookup may reconstruct it before execution. Existing fieldflow and check-coverage analyses can establish that expected fields were inspected, but not that the inspected object version reaches the sink or that no replacement intervenes between...
  </details>

- **2026-09-22** — Margit Rösler, Michael Voit — [Dunkl theory, convolution algebras, and related Markov processes](http://arxiv.org/abs/2609.26394v1)
  <details><summary>📄 Abstract</summary>
  These lecture notes are intended as an introduction to the theory of rational Dunkl operators, the associated special functions and related Markov processes with an emphasis on examples which are related to Riemannian symmetric spaces of Euclidean type and Bessel hypergroups on the matrix cones of positive semidefinite matrices.   We start with a comprehensive introduction into Dunkl theory: Dunkl operators, the intertwining operator and its positivity, the Dunkl kernel and the Dunkl transform, ...
  </details>

- **2026-09-22** — Moumita Mondal, Santanu K. Maiti — [Bias-driven circular currents in a quantum ring: Effects of electron-electron and electron-phonon interactions](http://arxiv.org/abs/2609.26344v1)
  <details><summary>📄 Abstract</summary>
  The phenomenon of bias-driven circular charge and spin currents in a ring nanojunction is investigated in the presence of electron-electron (e-e) and electron-phonon (e-ph) interactions within a tight-binding framework based on the non-equilibrium Green's function formalism. The Lang-Firsov transformation is employed to map the interacting system onto an effective electronic model, which is subsequently treated within the Hartree-Fock mean-field scheme. By exploring the interplay among e-e inter...
  </details>

- **2026-09-22** — Zhiheng Zhang — [Learning to Fluctuate: Statistical Foundations for Causal Tabular Pretraining](http://arxiv.org/abs/2609.26290v1)
  <details><summary>📄 Abstract</summary>
  Causal tabular foundation models amortize effect estimation across synthetic mechanisms, but latent-effect supervision rewards posterior shrinkage instead of directly encoding the repeated-sample response needed in a fixed deployment population. We introduce fluctuation-supervised pretraining (FSP): each synthetic table is labeled by its average treatment effect plus its efficient influence-function fluctuation, while deployment remains a single frozen forward pass. Along the path $T_{λ,P}=θ(P)+...
  </details>

- **2026-09-22** — Alex Samorodnitsky — [On the OpenAI whole-cube bound](http://arxiv.org/abs/2609.26050v1)
  <details><summary>📄 Abstract</summary>
  This is an essentially derivative note, whose goal is to interpret the 'whole-cube' bound of OpenAI for binary codes in a possibly somewhat more accessible way. This is attained, in part, by connecting it to some previously known results. All of the heavy technical lifting in the interpretation below is also due to the OpenAI language models ChatGPT 5.6 and ChatGPT 6. With that, we hope that the statements of the main results, the ensuing discussion, and the arguments themselves may be of some i...
  </details>

- **2026-09-22** — Ilias Mitsouras, Nikolaos Chaidos, Giorgos Stamou et al. — [EMERGE: Resolution-Agnostic Point Cloud Generation with Equivariant Graph-Based Diffusion](http://arxiv.org/abs/2609.26039v1)
  <details><summary>📄 Abstract</summary>
  Point cloud generation has emerged as a crucial task for accurately capturing and reproducing the complexity of the physical world. However, existing generative approaches, predominantly relying on Transformers and Variational Autoencoders (VAEs), frequently ignore the continuous, non-grid topologies inherent to 3D spaces. Although the integration of graph-based structures has yielded significant benefits in related discriminative vision tasks, such geometric architectures remain noticeably abse...
  </details>

- **2026-09-22** — Yuhang Zhang, Rangya Zhang, Yujing Shang et al. — [Skytopia: Monocular Drone Navigation with Action-Conditioned Latent World Models](http://arxiv.org/abs/2609.26007v1)
  <details><summary>📄 Abstract</summary>
  Monocular drone navigation requires reaching a goal in an unseen environment from a single forward-facing camera, which offers few cues for depth and scale. World models address this by modelling how observations evolve under actions, but they are built to be executed: the prediction is produced at deployment and fed back into action generation at every control step. We argue that what a policy needs from a world model is not the prediction but the representation required to produce it: in fligh...
  </details>

- **2026-09-22** — Alberto Ibort, Maria Jimenez-Vazquez, Juan M. Perez-Pardo — [Theory for groupoid equivariant neural networks: an approach for steerable CNNs on bounded domains](http://arxiv.org/abs/2609.25987v1)
  <details><summary>📄 Abstract</summary>
  Equivariant convolutional neural networks are usually built from a group acting globally on the space of signals. This hypothesis is inappropriate for many bounded or stratified domains: an ambient rigid motion may be admissible only on part of the domain, and the boundary introduces geometric types that are invisible to a transitive group action. We develop a theory of groupoid-equivariant neural networks in which the symmetry datum consists of a groupoid, a selected pseudogroup of local bisect...
  </details>

- **2026-09-22** — Hongjin Song, Runwu Shi, Weiqiao Shan et al. — [Rethinking Length-Based Training: Batch Composition and Loss Normalization in Speech Token Language Models](http://arxiv.org/abs/2609.25890v1)
  <details><summary>📄 Abstract</summary>
  Short-to-long training is a simple curriculum for speech models, but its gains can be difficult to interpret. In speech token language models, length-based training can change the shuffle policy, batch composition, token retention, and token weights under batch-mean loss. We disentangle these factors through matched comparisons. In the tested settings, short-to-long ordering shows no independent benefit when batch composition and token exposure are fixed. First-epoch grouping lowers perplexity f...
  </details>

- **2026-09-22** — Yijia Hao, Pratibha Verma, Dongxu Guo et al. — [AgenticSizing: A Large Language Model-based Multi-Agent Framework for Analog Circuit Sizing](http://arxiv.org/abs/2609.25873v1)
  <details><summary>📄 Abstract</summary>
  Analog circuit sizing remains a challenging and time-consuming task due to the large design space, strong performance trade-offs, and increasing circuit complexity in scaled technologies. Although recent large language model (LLM)-based methods show promise in improving sample efficiency and interpretability, existing approaches often lack explicit circuit-topology understanding and are mainly evaluated on relatively simple analog building blocks. This paper presents a multi-agent LLM-based fram...
  </details>

- **2026-09-22** — Oliver Křenek, Vít Průša, Rebecca Tozzi et al. — [Uniform approximation of spectra of linear second order differential operators via discrete sine transform based discretisation](http://arxiv.org/abs/2609.25796v1)
  <details><summary>📄 Abstract</summary>
  We study various discretisation schemes for the regular Sturm--Liouville operator on a bounded interval and for the Laplace operator on an arbitrary planar domain, in both cases subject to zero Dirichlet boundary conditions. The objective is to identify a discretisation scheme such that the corresponding discretised operator---a matrix of size $N \times N$---produces $N$ eigenvalues that approximate as closely as possible the first $N$ eigenvalues of the corresponding operator at the continuous ...
  </details>

- **2026-09-22** — Xiaoning Wang, Ted Underwood, Zhewei Sun — [From Utterances to Networks: Modelling Slang Adoption and Diffusion Across Subreddits](http://arxiv.org/abs/2609.25669v1)
  <details><summary>📄 Abstract</summary>
  Adoption and diffusion of neologisms in online communities have received renewed attention in recent years. As internet slang terms such as APT, referring to a K-pop song, and phrases such as Canon Event meaning an embarrassing but pivotal event, go viral online, it becomes increasingly important to understand the mechanisms that contribute to their success. Prior studies have often explained slang diffusion either from the perspective of social interaction or from the linguistic properties of t...
  </details>

- **2026-09-22** — Zijun Lin, Zhiyang Deng, Yuzhe Wu et al. — [GameDirector: Decoupling Gameplay Logic from Rendering for Player-Configurable Game World Models](http://arxiv.org/abs/2609.25652v1)
  <details><summary>📄 Abstract</summary>
  Recent game world models support realistic visual simulation and interactive gameplay based on player inputs. However, they typically learn environment dynamics from pixel-level supervision, jointly modeling perception, memory, state transitions, and rendering within a single end-to-end framework. While this design enables open-ended, action-controllable generation, it still falls short of delivering a complete gameplay experience. Games are governed by explicit mechanics, such as health deducti...
  </details>

- **2026-09-22** — Tak Hur — [When Quantum Meets AI: Quantum Methods for Machine Learning and Machine Learning Methods for Quantum Systems](http://arxiv.org/abs/2609.25641v1)
  <details><summary>📄 Abstract</summary>
  This thesis studies the intersection of quantum computing and artificial intelligence in two directions: quantum methods for machine learning and machine learning methods for quantum systems. For quantum machine learning, Neural Quantum Embedding learns data representations that increase the trace distance between embedded class ensembles, lowering an embedding-dependent bound on empirical risk and improving classification on noisy quantum hardware. A training objective based on the Hilbert-Schm...
  </details>

- **2026-09-22** — Md Abrar Jahin, Craig A. Knoblock, Jay Pujara — [ArticleMiner: Ontology-Guided Knowledge Graph Construction from Scientific Publications](http://arxiv.org/abs/2609.25607v1)
  <details><summary>📄 Abstract</summary>
  Scientific papers keep much of their quantitative content in tables and supplementary files, where a number means something only through its header, caption, unit, analytical method, and the conventions of its field. Recovering the rows and columns of a table is therefore not the same as recovering the scientific fact it reports. Most semantic table-interpretation methods assume that a clean table is already available and subsequently map its cells or columns to ontology terms, whereas most publ...
  </details>

- **2026-09-21** — Parth Gor, Sourya Roy, Kasturi Varadarajan — [Near-Optimal Online Metric Matching on $Δ$-ary HST](http://arxiv.org/abs/2609.25292v1)
  <details><summary>📄 Abstract</summary>
  In the online metric matching problem, we have $n$ servers with known locations in some metric space. Requests arrive one-by-one at certain locations, and upon arrival a request must be matched to a server that was not matched to a previous request. The goal is to minimize the matching cost. For randomized algorithms with an oblivious adversary, the best known competitive ratio is obtained by embedding the metric space into an HST, and then solving the problem in the setting where the metric spa...
  </details>

- **2026-09-21** — Zhiping Wu, Dongdong Ren, Yangchengyu Zhou et al. — [RGSQ: Riemannian Geometry-Sensitive Quantization for Large Vision-Language Models](http://arxiv.org/abs/2609.25492v1)
  <details><summary>📄 Abstract</summary>
  Large vision-language models (VLMs) can be efficiently deployed under stringent memory and latency constraints through post training quantization (PTQ). However, most PTQ methods are designed for unimodal large language models (LLMs). These methods treat quantization errors as isotropic perturbations under the Euclidean assumption, which provides weak guidance on directions most sensitive to quantization in VLMs. Consequently, directly adapting unimodal PTQ approaches or solely employing modalit...
  </details>

- **2026-09-21** — Miray Wahib, Ethan Tran, Rea Mourad et al. — [Spectra: A Rules-Driven LLM Pipeline for Automated KYC Document Processing](http://arxiv.org/abs/2609.25474v1)
  <details><summary>📄 Abstract</summary>
  Know Your Client (KYC) onboarding in capital markets requires analysts to manually classify documents, extract structured data from heterogeneous sources, and validate compliance against complex regulatory policies. This process requires significant analyst time per client, with end-to-end onboarding often stretching to multiple weeks due to sequential handoffs. In this work, we analyze an on-boarding process and find that it comprises repeatable components well-suited to AI automation. We there...
  </details>

- **2026-09-21** — Xiaotie Deng, Ningyuan Li — [Strategic Disclosure of Action Space in Principal-Agent Contracts](http://arxiv.org/abs/2609.25410v1)
  <details><summary>📄 Abstract</summary>
  We study strategic disclosure of the action space in principal-agent contracting, where an agent selects a disclosed action set to shape the principal's perception of her capabilities before contract design. Unaware of the strategic disclosure, the principal designs a revenue-optimal contract as if the disclosed action set were complete and accurate. We consider two variants distinguished by cost verifiability. When costs are unverifiable, the agent can extract the entire first-best surplus, lea...
  </details>

- **2026-09-21** — Lujia Bao, Qian Chen, Luyao Cheng et al. — [Qwen-Audio-3.1-Realtime: Towards Reliable Agentic Voice Interaction](http://arxiv.org/abs/2609.25176v1)
  <details><summary>📄 Abstract</summary>
  Real-time voice assistants must reason over evolving requests, execute actions, and follow conversational rules. Qwen-Audio-3.1-Realtime brings these requirements together through Think, Act, and Speak and Coordinate. Think combines Core-Cocktail supervised fine-tuning with Multimodality and Multi-Teacher On-Policy Distillation (M$^{2}$-OPD) to transfer language capabilities and develop native audio skills. Act uses self-evolving executable environments and multi-granularity rollouts for Group R...
  </details>

- **2026-09-21** — Elvin Yang, Christoforos Mavrogiannis — [Learning from Humans for Proactive Assistance in Human-Robot Collaborative Transport](http://arxiv.org/abs/2609.25351v1)
  <details><summary>📄 Abstract</summary>
  We focus on human-robot collaborative transport, a challenging task of broad relevance spanning logistics, manufacturing, and the home, in which a user and a robot work together to relocate a large or heavy object. To act as an effective partner, the robot should reduce the user's effort by contributing to efficient relocation of the object while remaining physically responsive to them. Prior work often addresses these capabilities separately, producing robots that may move the object efficientl...
  </details>

- **2026-09-21** — Howard Lu, Shalfun Li, Porter Pan et al. — [X-Planner: Event-Structured Task Planning for Embodied Intelligence](http://arxiv.org/abs/2609.25187v1)
  <details><summary>📄 Abstract</summary>
  Task planning bridges high-level instructions and executable behavior in long-horizon manipulation, yet modern Vision-Language-Action (VLA) systems often leave this intermediate structure implicit. Existing chain-of-thought (CoT) planners also tend to rely on coarse task-level annotations or serialize long reasoning traces token by token. We present X-Planner, a planning front-end that addresses both the supervision and representation of embodied reasoning. Our planning data combine Ego, UMI, an...
  </details>

- **2026-09-21** — Hongwei Yan, Kanglei Zhou, Qi Cheng et al. — [Brain-Inspired Hierarchical Modularity for General Continual Learning](http://arxiv.org/abs/2609.25146v1)
  <details><summary>📄 Abstract</summary>
  Continual learning, the ability to learn from sequential experience while retaining and adapting prior knowledge, is central to intelligent systems operating in changing environments. However, conventional continual learning is typically studied with offline task-wise training and clear task boundaries, leaving a substantial gap from general continual learning under online, uncertain, and evolving data streams. In this regime, intelligent systems must separate conflicting experience to reduce in...
  </details>

- **2026-09-21** — Daniel Halpern, Abhiram Manohara, Alexandros Psomas — [Prophet Inequalities Beyond Utilitarian Social Welfare](http://arxiv.org/abs/2609.25424v1)
  <details><summary>📄 Abstract</summary>
  In the classical i.i.d. prophet-inequality problem, a single item is allocated to one of $n$ agents who arrive sequentially, with values drawn independently from a known distribution. When an agent arrives, their value is revealed, and the algorithm must immediately allocate the item or continue. The usual objective is utilitarian welfare: the expected value of the recipient. Guarantees for this objective extend to allocating $m$ indivisible items to sequentially arriving agents with i.i.d.\ add...
  </details>

- **2026-09-21** — Zoha Azimi, Reza Farahani, Schahram Dustdar et al. — [Cloud, Edge, or Split? Profiling Onboard and Split Vision-Language Model Deployment for Drone AI](http://arxiv.org/abs/2609.25415v1)
  <details><summary>📄 Abstract</summary>
  Vision-Language Models (VLMs) enable edge devices like unmanned aerial vehicles (UAVs) to interpret visual observations and reason about complex environments using natural-language instructions. However, their practical deployment remains challenging as onboard inference is constrained by limited computational, memory, and energy resources, whereas cloud-based inference introduces communication latency, bandwidth overhead, and dependence on network connectivity. To address these limitations, spl...
  </details>

- **2026-09-21** — Luiza Treichel Mossi, Nicole Mazzitelli Narvaz, Larissa da Silva Bento et al. — [Statistical signatures of microorganism motility under environmental stress](http://arxiv.org/abs/2609.25403v1)
  <details><summary>📄 Abstract</summary>
  The motility of microorganisms provides a natural framework for studying active matter and its response to environmental perturbations. We experimentally investigate the trajectories of \textit{Paramecium caudatum} and \textit{Artemia salina} under controlled conditions. Using video microscopy, we reconstruct individual trajectories over time. Beyond baseline conditions, we analyze stressed environments where \textit{P. caudatum} are exposed to a toxic agent and \textit{A. salina} are placed in ...
  </details>

- **2026-09-21** — Mike Thelwall, David Pride, Francesco Osborne et al. — [Scoring Grant Applications with Large Language Models](http://arxiv.org/abs/2609.25327v1)
  <details><summary>📄 Abstract</summary>
  Purpose: Assessing grant applications is time-consuming and difficult, adding to the overall burden of academic peer review. Whilst funders are exploring whether AI can help, there is no published research into the accuracy of Large Language Models (LLMs) for scoring contemporary grants. Design/methodology/approach: This study investigates whether six open-weight LLMs (Gemma 3 1B/4B/12B/27B, DeepSeek R1 32B, Qwen 3 32B) can give useful scores for 2267 recent UK Economic and Social Research Counc...
  </details>

- **2026-09-21** — Zhiyao Zhang, Yichen Li, Xingyu Wu et al. — [Online Automated Algorithm Design with Large Language Models](http://arxiv.org/abs/2609.25325v1)
  <details><summary>📄 Abstract</summary>
  Large language models (LLMs) enable automated algorithm design (AAD) through reasoning and code synthesis. However, most existing LLM-based AAD methods separate algorithm design from target optimization, deploying a fixed design even as the optimization state evolves. Conventional adaptive optimizers can respond to such changes, but their adjustments remain confined to predefined parameters, operators, or strategies. To address these limitations, we introduce online LLM-based AAD, a novel optimi...
  </details>

- **2026-09-21** — Afagh Mehri Shervedani, Siyu Li, Natawut Monaikul et al. — [Learning to Plan in Human-Robot Collaboration: Multimodal Reinforcement Learning for Adaptive Interaction](http://arxiv.org/abs/2609.25274v1)
  <details><summary>📄 Abstract</summary>
  Robot assistants for older adults and people with disabilities need to perform collaborative tasks with users effectively. The core component of these systems is an interaction manager whose job is to observe and assess the task and infer the state of the human and their intent for the robot to choose the best course of action. Due to the sparseness of the data in this domain, the policy for such multimodal systems is often crafted by hand; as the complexity of interactions grows, this process i...
  </details>

- **2026-09-21** — Guangchuan Lv, Dianxing Shi, Dingjie Fu — [VPRune: Efficient Training-free Pre-LLM Visual Token Pruning](http://arxiv.org/abs/2609.24485v2)
  <details><summary>📄 Abstract</summary>
  Visual token pruning is a promising approach to reducing the inference cost of large vision-language models (LVLMs), yet aggressive token reduction often causes substantial performance degradation. We identify three key factors behind this degradation: text-guided selection bias, information loss from discarded tokens, and positional distortion caused by sequence compaction. Based on these observations, we propose \textbf{VPRune}, a training-free pre-LLM pruning framework consisting of visual-on...
  </details>

- **2026-09-21** — Eunkyu Park, Markelle Roesti, Wesley Hanwen Deng et al. — [Who Does What in AI Auditing? Designing Human-AI Collaboration for Auditing Generative AI](http://arxiv.org/abs/2609.24986v1)
  <details><summary>📄 Abstract</summary>
  AI auditing increasingly incorporates AI agents to expand the scale and breadth of audit coverage, yet little is known about how auditing work should be divided without displacing human judgment. We introduce Human-Agent Audit Collaboration (HAAC), a workflow and system for structuring human-AI collaboration in AI auditing. Drawing on prior work and formative consultations with AI auditing practitioners, HAAC specifies how agents can support exploration, assessment, reporting, and review while p...
  </details>

- **2026-09-21** — Xinnong Zhang, Jiayu Lin, Jia Wang et al. — [SocioVerse2: A Longitudinal Dynamic Social Simulation Framework under a Human-AI Co-evolutionary Paradigm](http://arxiv.org/abs/2609.24911v1)
  <details><summary>📄 Abstract</summary>
  Social simulation offers the social sciences an experimental instrument that the real world cannot supply, and generative agents have transformed it by acting as silicon samples that unite agent-based modeling with real behavioral data. Existing platforms verify collective behavior, align simulated populations with real societies in cross-sections, and employ autonomous agents for the research process. However, two social science requirements remain without systematic support: intervention in th...
  </details>

- **2026-09-21** — Kewei Zhang, Zheng Chen, Haotong Qin et al. — [SPHQuant: Efficient extreme low bit weight quantization for Vision-Language Models](http://arxiv.org/abs/2609.24875v1)
  <details><summary>📄 Abstract</summary>
  Recent foundation models are moving toward native multimodal Vision-Language Models (VLMs), making VLMs a central form of next-generation foundation models. However, their large language backbones make edge deployment difficult due to high memory footprint and memory-bound autoregressive decoding. Weight-only post-training quantization is a practical solution, but pushing VLMs to extreme low bit-widths remains challenging: existing rotation-free methods suffer from outliers at 2-3 bits, while ro...
  </details>

- **2026-09-21** — Junde Wu, Jiayuan Zhu, Minghao Hu et al. — [MedRSI: Recursive Self-Improvement for Medical Agents via Clinically Aligned Self-Evolution](http://arxiv.org/abs/2609.24838v1)
  <details><summary>📄 Abstract</summary>
  Medical agents increasingly combine general reasoning models with specialized clinical tools, yet their capabilities remain largely fixed by what clinicians and engineers design before deployment. Recursive self-improvement (RSI) offers a different paradigm in which agents learn from their own failures and autonomously expand their capabilities, but directly applying RSI to medicine introduces fundamental safety challenges. We introduce MedRSI, the first recursive self-improvement framework for ...
  </details>

- **2026-09-21** — Yeji Kim, Mi-Young Kim, Randy Goebel — [When Quantization Preserves Accuracy but Not Evidence: Explanation-Aware Post-Training Quantization for Medical LLMs](http://arxiv.org/abs/2609.24799v1)
  <details><summary>📄 Abstract</summary>
  Post-training quantization (PTQ) enables efficient deployment of large language models, and PTQ methods are usually optimized and evaluated with generic reconstruction, perplexity, or answer accuracy. But in explanation-critical domains, preserving only the final answer may be insufficient, since users may also inspect generated rationales to judge whether a prediction is trustworthy. We study this issue in medical multiple-choice question answering, where rationales should provide evidence that...
  </details>

- **2026-09-21** — Hasibur Rahman, Mahsa Nasri, Manasi Vaidya et al. — ["MeBo Leaves a Piece of You Behind": Designing a Relational Voice-Based Memory Companion for Older Adults](http://arxiv.org/abs/2609.24706v1)
  <details><summary>📄 Abstract</summary>
  Autobiographical remembering supports identity, well-being, and social connection in later life, yet voice-based memory technologies largely rely on isolated prompts. We designed and built MeBo, a fully functional relational voice-based memory companion, through participatory design with 11 older adults. Their accounts shaped four Design Strategies that guided MeBo's interaction design and multi-agent implementation. In a mixed-methods evaluation with 20 older adults, participants found MeBo exc...
  </details>

- **2026-09-21** — Julian Oelhaf, Alexander Luce, Christian Bergler et al. — [Offline Reinforcement Learning for Distribution-Grid Protection](http://arxiv.org/abs/2609.24703v1)
  <details><summary>📄 Abstract</summary>
  Data-driven protection may complement conventional relays in distribution grids whose operating conditions vary with distributed generation, switching events, and changing short-circuit levels. We study line-selective tripping from static trajectories of a realistically simulated CIGRE medium-voltage network using offline reinforcement learning. A convolutional Q-network receives causal voltage-current phasor and apparent-impedance features, optionally together with raw waveforms, and is trained...
  </details>

- **2026-09-21** — Man Tang, Zhaoyun Zong, Diqiong Jiang et al. — [Direction-Aware Masked Pretraining for 3D Seismic Representation Learning and Transfer to Cross-Area Acoustic Impedance Inversion](http://arxiv.org/abs/2609.24615v1)
  <details><summary>📄 Abstract</summary>
  Large archives of unlabeled three-dimensional seismic data offer opportunities for self-supervised representation learning and subsequent transfer to acoustic impedance inversion. However, conventional masked pretraining often treats three axes equivalently, overlooking differences between lateral reflector structure and vertical waveform characteristics. We propose a direction-aware masked autoencoder for three-dimensional post-stack seismic data, combining anisotropic tokenization, direction-a...
  </details>

- **2026-09-21** — Zhaomin Lyu, Ding Zhang, Yan Jiang — [Optimal Allocation of Grid-Forming Frequency Shaping Control](http://arxiv.org/abs/2609.24583v1)
  <details><summary>📄 Abstract</summary>
  Various inverter-based control strategies have been proposed to improve frequency security for power systems with high renewable penetration. Among them, the grid-forming frequency shaping control is particularly promising due to its ability to shape the post-contingency aggregate system frequency dynamics into first-order with prescribed rate of change of frequency (RoCoF) and steady-state frequency deviation. Moreover, the shaped aggregate dynamics depends on the harmonic sum of all inverter t...
  </details>

- **2026-09-21** — Mingke Lu, Anxing Xiao, David Hsu — [MIGU: Multimodal Instruction Grounding under Uncertainty for Manipulation Planning](http://arxiv.org/abs/2609.24995v1)
  <details><summary>📄 Abstract</summary>
  Understanding natural human instructions is crucial for deploying robots in human-centric environments. We study multimodal instruction grounding, where language and gesture provide complementary but uncertain cues. We present MIGU, a modular framework that combines semantic and geometric evidence into a unified grounding belief and connects it to manipulation planning. MIGU constructs a 3D geometric likelihood by propagating viewing-direction and depth uncertainty through eye-finger geometry wh...
  </details>

- **2026-09-21** — Ke Zhou, Edyta Bogucka, Daniele Quercia — [Small-world Networks of Agents Brainstorm AI Risks to Support Ideation](http://arxiv.org/abs/2609.24859v1)
  <details><summary>📄 Abstract</summary>
  The ideation phase of participatory AI risk assessment often starts with a blank slate or a limited list of predefined risks, making it difficult to surface indirect or systemic harms. To address this limitation, we propose a three-stage ideation support tool. The tool complements participatory AI, rather than replacing it, and helps focus later engagement with affected communities. First, it dynamically discovers stakeholders depending on the given AI use and recursively expanding outward, allo...
  </details>

- **2026-09-21** — Jie Gong, Maowei Jiang, Zhiwei Liu et al. — [TimeLitmus: A Diagnostic Benchmark for Cross-Modal Understanding and Explanation Faithfulness in Event-Conditioned Time-Series Prediction](http://arxiv.org/abs/2609.24677v1)
  <details><summary>📄 Abstract</summary>
  Large language models (LLMs) are increasingly used to make predictions from numerical time-series histories and textual events. Yet accuracy alone cannot reveal whether correct answers reflect effective integration of the two inputs or instead arise from event polarity, unimodal priors, or superficial cues. Likewise, plausible explanations may rationalize predictions without faithfully reflecting the evidence that drives model behavior. We introduce TimeLitmus, a diagnostic benchmark for cross-m...
  </details>

- **2026-09-21** — Xijing Cui, Huayan Pu, Jun Luo et al. — [Feasibility Distance Fields for Heterogeneous Constraints in Robot Configuration Space](http://arxiv.org/abs/2609.24632v1)
  <details><summary>📄 Abstract</summary>
  Robot manipulators are monitored by constraint-specific indicators whose units and gradient scales are not comparable, so they do not provide a common measure of the configuration-space motion remaining before violation. We define the feasibility distance field (FDF) as the distance, under a fixed positive-definite joint-space metric, to the union of infeasible configuration sets. Classical distance-to-set theory gives 1-Lipschitz continuity, almost-everywhere differentiability, and unit dual-gr...
  </details>

- **2026-09-21** —  ATLAS Collaboration — [Search for a top-philic heavy resonance in association with top quarks in $pp$ collisions at $\sqrt{s} = $ 13 TeV and 13.6 TeV with the ATLAS detector](http://arxiv.org/abs/2609.24950v1)
  <details><summary>📄 Abstract</summary>
  A search for a new top-philic vector boson ($Z'$) produced in association with a top-quark or a pair of top quarks, and decaying into a top quark pair is presented. The search uses $pp$ collision data collected by the ATLAS detector at the Large Hadron Collider at centre-of-mass energies of $\sqrt{s} =$ 13 TeV and 13.6 TeV, corresponding to integrated luminosities of 140 fb$^{-1}$ and 56 fb$^{-1}$, respectively. Events containing exactly two same-sign leptons or at least three leptons (electrons...
  </details>

- **2026-09-21** — Yuanwen Yue, Stefano Puliti, Damien Robert et al. — [Toward a foundation model for forest point clouds](http://arxiv.org/abs/2609.24787v1)
  <details><summary>📄 Abstract</summary>
  Forest inventories increasingly rely on artificial intelligence (AI) models to derive forest attributes from large-scale 3D point clouds. Current models are typically specialized to a single task, sensor, and forest type, making adaptation expensive in terms of annotations, computation, and expertise. We ask whether a single pretrained model can instead learn transferable representations across diverse forest inventory settings. Inspired by recent developments in language modelling and computer ...
  </details>

- **2026-09-21** — Fabian Spaeh, Jingxing Fang, Shandian Zhe et al. — [Universal Multi-Modal Traceformer: Integrating Heterogeneous Context for Process Event Prediction](http://arxiv.org/abs/2609.24579v1)
  <details><summary>📄 Abstract</summary>
  Event logs arise in a wide range of real-world processes, capturing not only event activities and timestamps but also multi-modal contextual information. Existing event-sequence models, including many temporal point process approaches, primarily model event activities and timestamps while overlooking heterogeneous context, such as numerical measurements, categorical attributes, textual descriptions, and metadata associated with individual events and entire traces. In this paper, we propose Unive...
  </details>

- **2026-09-21** — Jun Cheng, Yuanyuan Kong, Qing Huang et al. — [Preoperative Prediction of Microvascular Invasion in Hepatocellular Carcinoma by Integrating Multimodal Ultrasound and Clinical Data: A Multicenter Study](http://arxiv.org/abs/2609.24524v1)
  <details><summary>📄 Abstract</summary>
  Background: Microvascular invasion (MVI) predicts recurrence and survival in hepatocellular carcinoma (HCC) but requires postoperative histopathology for diagnosis. We developed and validated a model integrating multimodal ultrasound and clinical data for preoperative MVI prediction. Methods: This multicenter study included 489 patients with HCC from eight centers. All patients had B-mode ultrasound (BUS), color Doppler flow imaging (CDFI), dynamic contrast-enhanced ultrasound (DCE-US), and clin...
  </details>

- **2026-09-21** — Hamed Alimohammadi, Burcu Şahin, Arda Akman et al. — [rApp/xApp Attestation: A New Security Use Case for O-RAN](http://arxiv.org/abs/2609.24296v1)
  <details><summary>📄 Abstract</summary>
  The disaggregation and softwarization introduced by the Open Radio Access Network (O-RAN) architecture enable multi-vendor innovation but also expose the RAN Intelligent Controller (RIC) ecosystem to new runtime security risks. Existing O-RAN specifications define strong safeguards for onboarding, authentication, identity management, and secure communication; however, they do not provide a concrete mechanism for verifying whether deployed rApps and xApps remain in their intended, untampered stat...
  </details>

- **2026-09-21** — Songqi Li, Dongqing Li, Zheqiao Cheng — [Canonical Procedural Actions: An Auditable Annotation Protocol for Tool-Use Agent Traces](http://arxiv.org/abs/2609.24264v1)
  <details><summary>📄 Abstract</summary>
  Tool-use agent traces identify messages and API calls, but procedural analyses also need explicit units of action and inspectable links to their evidence. We present Canonical Procedural Actions (CPAs), an annotation protocol that records a procedural function, its first agent-event anchor, the agent events that realize it, and separate contextual evidence. Multiple actions may share a message anchor without an inferred within-message order. A retail case study produces a versioned 24-entry code...
  </details>

- **2026-09-21** — Ningyuan Deng, Jinyuan Wang, Qi Li et al. — [FinRankGRPO: Optimizing LLMs for Listwise Financial Asset Ranking via Group Relative Policy Optimization](http://arxiv.org/abs/2609.24175v1)
  <details><summary>📄 Abstract</summary>
  While Large Language Models (LLMs) excel at understanding unstructured financial contexts, their direct use in portfolio optimization is limited by a mismatch between next-token prediction and the listwise ranking objectives required for asset allocation. They also struggle with precise numerical forecasting, leading to instability and arithmetic hallucinations. To bridge this gap, we propose FinRankGRPO, a framework that shifts LLM based portfolio construction from direct numerical prediction t...
  </details>

- **2026-09-21** — Cong Li, Cheng Chen, Thomas Fung et al. — [Mind or Message? Auditing Theory of Mind in Multi-Agent Social Simulation](http://arxiv.org/abs/2609.24146v1)
  <details><summary>📄 Abstract</summary>
  Language model agents are increasingly used to simulate social interaction, and the resulting transcripts read as though the agents understand one another. We ask whether that appearance rests on a model of the partner's mind or on the surface record of what the partner said. We build a social simulation in which both questions have exact answers: 40 multi-issue negotiations whose hidden preference weights and whose full Pareto frontier are known by construction. Two model families negotiate acr...
  </details>

- **2026-09-21** — You Liu, Yue Liu, Quanchao Lu et al. — [OSCAR: Order-aware Scoring and Calibration for AI Rankings](http://arxiv.org/abs/2609.24128v1)
  <details><summary>📄 Abstract</summary>
  Judge-specific sensitivity is useful for aggregating pairwise LLM evaluations, but its interpretation depends on which systematic presentation effects the ranking model includes. We introduce OSCAR, an order-aware framework for scoring and calibrating AI rankings, and study position as one such effect. In released judgments from 18 evaluators, the all-response A-minus-B score difference ranges from $-63.11$ to $98.31$ percentage points. Matching question text, response texts, candidate identitie...
  </details>

- **2026-09-21** — Yu-Ho Chang, Chi-Hsi Kung, Yi-Hsuan Tsai et al. — [Action-Slot: Structured Action-Centric Representation Learning for Multi-Agent Atomic Activity Understanding](http://arxiv.org/abs/2609.24127v1)
  <details><summary>📄 Abstract</summary>
  Atomic activity understanding aims to recognize and localize structured traffic behaviors that jointly encode motion patterns and their grounding in road topology. Unlike conventional action recognition, atomic activities are multi-agent, multi-label, and topology-aware: multiple activities co-occur while many agents remain inactive. We introduce Action-Slot, a structured action-centric representation learning framework. Slot attention is widely used for object-centric decomposition, but its per...
  </details>

- **2026-09-21** — Kunpeng Yang — [A Task-Oriented Multi-Agent Framework for Complex Wearable Health Analysis](http://arxiv.org/abs/2609.24107v1)
  <details><summary>📄 Abstract</summary>
  Wearable health questions often combine data retrieval, longitudinal analysis, and health advice over structured records. Prompting a single large language model with a complete record and a composite query obscures whether every request is executed and which evidence supports the answer. We propose a task-oriented multi-agent framework that represents a composite query as distinct intents and typed tasks with explicit intra-intent dependencies. Specialized agents execute retrieval, analysis, an...
  </details>

- **2026-09-21** — Cheng Li, Jiexiong Liu, Yixuan Chen et al. — [Incremental Consistency Execution for Autonomous Intelligent Systems](http://arxiv.org/abs/2609.24090v1)
  <details><summary>📄 Abstract</summary>
  Long-horizon autonomous intelligent systems rely on heterogeneous components such as large language models, databases, external APIs, and rule engines, while their external states continuously change during execution. Re-executing the entire workflow after every change introduces substantial redundant computation. This paper proposes an incremental consistency execution method based on task fact contracts, field-level dependency masks, and state perturbation result invariant domains. After an in...
  </details>

- **2026-09-21** — Xingsong Ye, Yongkun Du, Jiaxin Zhang et al. — [All-in-One Multilingual Scene Text Recognition with Script-aware Mixture-of-Experts](http://arxiv.org/abs/2609.24058v1)
  <details><summary>📄 Abstract</summary>
  Multilingual scene text recognition (STR) remains challenging due to the scarcity of training data for most languages and the difficulty of serving diverse scripts within a single model. Existing solutions either deploy one recognizer per language, inflating cost and introducing error accumulation, or rely on massive vision-language models (VLMs) that are expensive and still inaccurate on many scripts. In this work, we pursue an all-in-one multilingual recognizer that is simpler than per-languag...
  </details>

- **2026-09-21** — Minda Zhao, Fangyu Hu, Yan Luo et al. — [Representation-guided in-context learning for medical image interpretation with multimodal large language models](http://arxiv.org/abs/2609.24057v1)
  <details><summary>📄 Abstract</summary>
  Medical image interpretation is central to diagnosis and care, yet adapting general-purpose multimodal large language models (MLLMs) often requires resource-intensive domain-specific fine-tuning. Here we introduce representation-guided in-context learning (RG-ICL), a training-free inference framework that retrieves query-aligned demonstrations using frozen encoders, without task-specific parameter updates. Across eight datasets spanning histopathology, radiology and retinal fundoscopy, RG-ICL im...
  </details>

- **2026-09-21** — Boxun Hu, Jiawei Ge, Axel Krieger et al. — [LEAP-NBV: Lightweight Edge Active-Perception for Foundation-Model Next-Best-View Planning](http://arxiv.org/abs/2609.23974v1)
  <details><summary>📄 Abstract</summary>
  Foundation models are endowing autonomous systems with greater intelligence, enabling a more comprehensive understanding of the environment through visual perception. A representative example is Human Mesh Recovery (HMR), which provides useful estimates of a target's 3D pose and shape that can benefit tactical missions. However, the size and power demands of such models make them difficult to run on edge platforms and limit their real-time performance, undermining the requirements of tactical ed...
  </details>

- **2026-09-21** — Mai Mohamed Eida, Gunjan Anand, Ayush Singh et al. — [From Tables to Quantified Statements: Evaluating LLM Inference Generation through Executable Verification](http://arxiv.org/abs/2609.23966v1)
  <details><summary>📄 Abstract</summary>
  LLMs can generate fluent descriptions from tables, but their outputs may remain logically unsupported by the structured data. We introduce STAT-TO-TEXT, a controlled task in which LLMs generate quantified natural language inferences from statistical tables using quantified constructions such as all, some, no, and most. To evaluate these inferences, we use an LLM generated Python checker code which when executed verifies the corresponding truth conditions against the table. We compare four open-w...
  </details>

- **2026-09-21** — Haoxuan Li, Sixu Yan, Lianghui Zhu et al. — [Bridge3D: Enabling Vision-Language-Action Models to See and Act in 3D](http://arxiv.org/abs/2609.24525v1)
  <details><summary>📄 Abstract</summary>
  Vision-Language-Action (VLA) models have demonstrated remarkable generalization in robotic manipulation via large-scale multimodal pretraining. However, VLA models are mainly trained on 2D-centric observations, which inherently constrains their capacity for precise spatial manipulation. Previous methods enhance 3D awareness by introducing implicit spatial priors, but still lack explicit geometry guidance. In this paper, we propose Bridge3D that integrates both implicit and explicit 3D geometry g...
  </details>

- **2026-09-21** — Akhil Sharma, Jatin Gupta, Ali Imam Abidi — [Taramandal-GPT: Enhancing Astrodynamics Problem-Solving with Knowledge Retrieval and Structured Thinking](http://arxiv.org/abs/2609.24246v1)
  <details><summary>📄 Abstract</summary>
  Large language models (LLMs) have shown remarkable progress in natural language understanding, yet their effectiveness in specialized fields like astronomy and astrodynamics remains limited due to challenges in multi-step reasoning, symbolic manipulation, and domain-specific terminology. To address this, we present Taramandal-GPT (Constellation-GPT), a domain-adapted framework built on the Qwen3-8b backbone, enhanced with a Retrieval-Augmented Generation (RAG) pipeline and a fallback mechanism f...
  </details>

- **2026-09-21** — MD. Nafis Kamal, Mahadi Hasan Fahim, Talha Ridwan et al. — [Efficient LLM Distillation for Bangladesh Legal Context: A Smartphone-Compatible Retrieval-Augmented Generation Model](http://arxiv.org/abs/2609.24177v1)
  <details><summary>📄 Abstract</summary>
  Legal information in Bangladesh is inaccessible to most citizens. Statutory text is English-only, trained lawyers are concentrated in urban centres, and cloud-dependent AI fails where mobile connectivity is unreliable, a setting in which hallucinated legal text causes direct harm. The system addresses statutory interpretation only; queries that require judicial precedent or case-law reasoning fall outside its scope. We target the statutory access gap by compressing a 9-billion-parameter Gemma-2 ...
  </details>

- **2026-09-21** — Wenbo Zhang, Kaixuan Wang, Yutao Ouyang et al. — [An Unexpected Robot Policy: Early Evaluations of GPT-6 Astra on RoboDojo and Beyond](http://arxiv.org/abs/2609.24170v1)
  <details><summary>📄 Abstract</summary>
  Embodied AI systems are often organized into System 1 and System 2. System 1 is typically a pretrained policy that generates actions at high frequency, whereas System 2 is often instantiated as a vision-enabled language model for high-level planning. We ask whether a large language model (LLM) can act as the policy for robot manipulation without task-specific finetuning. We call this setting LLM as policy. We evaluate three LLMs on all 42 RoboDojo tasks and compare their scores with 40 public po...
  </details>

- **2026-09-21** — Guoliang Li, Peiyao Zhou, Xuanhe Zhou et al. — [Data Agents: Agentic Data Systems](http://arxiv.org/abs/2609.24137v1)
  <details><summary>📄 Abstract</summary>
  Traditional data systems face profound limitations in the AI era, relying on human-crafted pipelines, lacking semantic understanding of heterogeneous data, and operating through rigid, reactive processing. To address these challenges, we propose a new paradigm called the Data Agent, designed to manage, process, and analyze data with minimal human intervention. Data agents autonomously execute a wide range of data-related tasks, transforming traditional data systems by shifting from manual design...
  </details>

- **2026-09-21** — Dorian Benhamou Goldfajn, Mason Nakamura, Saaduddin Mahmud et al. — [RoboTalk: Learning Multi-Robot Communication and Coordination from Multimodal Demonstrations](http://arxiv.org/abs/2609.23997v1)
  <details><summary>📄 Abstract</summary>
  Multi-robot collaboration could enable more efficient and scalable solutions to complex robotic tasks, but collaboration under partial observability remains challenging. Natural-language communication offers a promising approach to coordinating robots under partial observability. However, in decentralized manipulation, jointly learning explicit inter-robot communication and skill-level action selection from multimodal demonstrations remains underexplored for small vision-language models (VLMs) i...
  </details>

- **2026-09-21** — Thomas Erben — [Natural coordinates for constrained correlation functions: Partial autocorrelations and the geometry of positive power spectra](http://arxiv.org/abs/2609.24500v1)
  <details><summary>📄 Abstract</summary>
  Two-point correlation functions are a standard summary statistic in cosmic shear and large-scale-structure analyses. Their values are, however, constrained: non-negativity of the underlying power spectrum restricts any admissible sequence of correlation coefficients $(r_1,\ldots,r_N)$ to a bounded convex region, described in the one-dimensional case by the recursive interval geometry of Schneider & Hartlap (2009). Their formalism introduces an affine variable $x_n$ that maps the admissible inter...
  </details>

- **2026-09-21** — Guangchuan Lv, Dianxing Shi, Dingjie FU — [VPRune: Efficient Training-free Pre-LLM Visual Token Pruning](http://arxiv.org/abs/2609.24485v1)
  <details><summary>📄 Abstract</summary>
  Visual token pruning is a promising approach to reducing the inference cost of large vision-language models (LVLMs), yet aggressive token reduction often causes substantial performance degradation. We identify three key factors behind this degradation: text-guided selection bias, information loss from discarded tokens, and positional distortion caused by sequence compaction. Based on these observations, we propose \textbf{VPRune}, a training-free pre-LLM pruning framework consisting of visual-on...
  </details>

- **2026-09-21** — Yuhan Zhu, Jilin Hu, Xinying Cai et al. — [WPBench: A Comprehensive Benchmark for Wind Power Forecasting](http://arxiv.org/abs/2609.24444v1)
  <details><summary>📄 Abstract</summary>
  Accurate, reliable, and deployable wind power forecasting is critical for power system dispatch, renewable energy integration, and electricity market operations. Progress in this field hinges on the ability to empirically and comprehensively benchmark forecasting methods. Yet existing benchmarks fall short of supporting systematic evaluation in four key aspects: 1) limited coverage of wind power scenarios across turbine scale, variable composition, and spatial structure; 2) incomplete coverage o...
  </details>

- **2026-09-21** — Ali A. Safieh, Ibrahim Abu Alhaol, Rawan Ghnemat — [End-to-end Jordanian dialect speech-to-text self-supervised learning framework](http://arxiv.org/abs/2609.24410v1)
  <details><summary>📄 Abstract</summary>
  Speech-to-text engines are extremely needed nowadays for different applications, representing an essential enabler in human-robot interaction. Still, some languages suffer from the lack of labeled speech data, especially in the Arabic dialects or any low-resource languages. The need for a self-supervised training process and self-training using noisy training is proven to be one of the up-and-coming feasible solutions. This article proposes an end-to-end, transformers-based model with a framewor...
  </details>

- **2026-09-21** — Mazdak Fatahi, Šárka Pryjmaková, Pierre Boulet et al. — [Can Spiking Neural Networks play pinball? A neuromorphic motion detector for target tracking](http://arxiv.org/abs/2609.24403v1)
  <details><summary>📄 Abstract</summary>
  Biological visual systems achieve continuous, low-latency motion perception by processing sparse, asynchronous spiking signals, enabling real-time tracking under strict energy constraints. Event-based cameras, inspired by the mammalian retina, replicate this efficiency by capturing only local brightness changes as asynchronous events, offering a natural substrate for spiking neural networks (SNNs) to parallelise computation and adapt to fast-changing scenes. Pinball provides a controlled yet dyn...
  </details>

- **2026-09-21** — Gautam Ranka, Shubham Santosh Pandere, Aiden Dsouza — [Topographic Training Concentrates Causal Circuits Without Improving Neuron Monosemanticity](http://arxiv.org/abs/2609.24379v1)
  <details><summary>📄 Abstract</summary>
  Mechanistic interpretability of vision transformers seeks to decompose model computation into human-readable units, but learned representations entangle many concepts in each neuron. Feature superposition is widely treated as the central obstacle to this decomposition, yet most mitigations (sparse autoencoders, dictionary learning) are post-hoc and leave the underlying network unchanged. We ask whether a spatial-locality training loss (TopoLoss) can act as a lightweight, training-time prior that...
  </details>

- **2026-09-21** — Senlei Zhang, Linhao Luo, Qian-Wen Zhang et al. — [LADDER: Graph-Guided Diffusion Language Models for Efficient Multi-Hop Reasoning](http://arxiv.org/abs/2609.24346v1)
  <details><summary>📄 Abstract</summary>
  Graph Retrieval-Augmented Generation (GraphRAG) has remarkably enhanced large language models on complex reasoning by leveraging structured entity topologies. However, existing frameworks heavily rely on standard autoregressive language models where the nature of inherent sequential generation severely hinders overall inference efficiency. Inspired by Diffusion Language Models (DLMs) that offer massive parallelism via continuous refine-in-parallel decoding, we aim to accelerate GraphRAG in the d...
  </details>


## 📊 统计 / Statistics

| 分类 / Category | 论文数 / Count |
|------|--------|
| jailbreak | 634 |
| prompt-injection | 552 |
| memory-poisoning | 50 |
| tool-use-attack | 138 |
| backdoor | 473 |
| adversarial-attack | 602 |
| privacy-leakage | 4153 |
| steganography | 71 |
| misuse | 1048 |
| red-teaming | 127 |
| vulnerability | 3200 |
| defense | 3027 |
| alignment | 2815 |
| robustness | 2993 |
| watermark | 472 |
| unlearning | 97 |
| agent-safety | 55 |
| benchmark | 66 |
| survey | 359 |
| other | 8087 |

---

📚 **全部 29019 篇论文**（2022 至今）请访问 [GitHub Pages](https://ny1024.github.io/AgentSafety-Papers/) 查看完整列表、搜索与筛选。

*Generated by AgentGuard at 2026-09-24 10:58:14*