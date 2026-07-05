<div align="center">

# AgentGuard 🛡️

**Daily Tracking of LLM Agent Security Papers on arXiv**

[![Auto Update](https://github.com/NY1024/AgentSafety-Papers/actions/workflows/daily-update.yml/badge.svg)](https://github.com/NY1024/AgentSafety-Papers/actions/workflows/daily-update.yml)
[![Papers](https://img.shields.io/badge/Papers-19657-blue)](#)
[![License](https://img.shields.io/badge/License-MIT-green)](#)

</div>

---

## 📖 简介 / Introduction

自动追踪 arXiv 上大模型 Agent 安全方向的最新论文，每日更新，关键词智能分类。

*Automatically tracking the latest LLM Agent security papers on arXiv, updated daily with keyword-based classification.*

**最近更新 / Last Updated**: 2026-07-05 03:26 ｜ **论文总数 / Total Papers**: 19657（近 30 天 / Recent 30 days: 4604）

🌐 **[GitHub Pages](https://ny1024.github.io/AgentSafety-Papers/)** — 查看全部 19657 篇论文（含摘要、分类筛选、搜索）/ View all 19657 papers with abstracts, filters & search

## 📑 分类导航 / Category Navigation

- **[jailbreak](#-jailbreak)** — 越狱攻击 / Jailbreak Attacks — 536
- **[prompt-injection](#-prompt-injection)** — 提示注入攻击 / Prompt Injection Attacks — 438
- **[memory-poisoning](#-memory-poisoning)** — 记忆投毒与篡改 / Memory Poisoning & Tampering — 33
- **[tool-use-attack](#-tool-use-attack)** — 工具使用攻击 / Tool-Use Attacks — 89
- **[backdoor](#-backdoor)** — 后门与投毒攻击 / Backdoor & Poisoning Attacks — 379
- **[adversarial-attack](#-adversarial-attack)** — 对抗攻击 / Adversarial Attacks — 520
- **[privacy-leakage](#-privacy-leakage)** — 隐私泄露 / Privacy Leakage — 3612
- **[steganography](#-steganography)** — 隐写与隐蔽通信 / Steganography & Covert Communication — 49
- **[misuse](#-misuse)** — 滥用与误用 / Misuse & Abuse — 782
- **[red-teaming](#-red-teaming)** — 红队测试 / Red Teaming — 104
- **[vulnerability](#-vulnerability)** — 漏洞与攻击面 / Vulnerabilities & Attack Surfaces — 2305
- **[defense](#-defense)** — 防御与防护方法 / Defense & Protection Methods — 1926
- **[alignment](#-alignment)** — 对齐与安全约束 / Alignment & Safety Constraints — 1744
- **[robustness](#-robustness)** — 鲁棒性与可靠性 / Robustness & Reliability — 1562
- **[watermark](#-watermark)** — 水印与溯源 / Watermarking & Provenance — 153
- **[unlearning](#-unlearning)** — 机器遗忘 / Machine Unlearning — 81
- **[agent-safety](#-agent-safety)** — Agent 安全框架 / Agent Safety Frameworks — 48
- **[benchmark](#-benchmark)** — 安全评测与基准 / Safety Benchmarks & Evaluation — 52
- **[survey](#-survey)** — 综述与系统化 / Surveys & Systematization — 234
- **[other](#-other)** — 其他安全相关 / Other Security-Related — 5010

## 📄 近期论文 / Recent Papers (Last 30 Days)

> 仅展示最近 30 天中最新的 500 篇论文（含日期、作者、摘要）。近 30 天共 4604 篇，完整 19657 篇论文列表请访问 [GitHub Pages](https://ny1024.github.io/AgentSafety-Papers/)

> Showing the latest 500 of 4604 papers from the last 30 days (with date, authors & abstract). For the full list of 19657 papers, visit [GitHub Pages](https://ny1024.github.io/AgentSafety-Papers/)

### 📂 jailbreak
*越狱攻击 / Jailbreak Attacks* — 4 papers

- **2026-07-02** — Joshua Adrian Cahyono — [Safety Targeted Embedding Exploit via Refinement](http://arxiv.org/abs/2607.01859v1)
  <details><summary>📄 Abstract</summary>
  Safety training for large language models (LLMs) is conducted predominantly in English, leaving uncertain how well safety mechanisms generalize to low-resource languages and mixed-language code-switching. We show that this creates an epistemic gap in which models confidently generate harmful responses for inputs that fall outside the distribution of their safety training. To study this phenomenon, we introduce STEER (Safety Targeted Embedding Exploit via Refinement), a gradient-guided attack tha...
  </details>

- **2026-07-01** — Shei Pern Chua, Fangzhao Wu — [HARC: Coupling Harmfulness and Refusal Directions for Robust Safety Alignment](http://arxiv.org/abs/2607.00572v1)
  <details><summary>📄 Abstract</summary>
  Understanding how aligned LLMs internally represent safety is critical for diagnosing alignment vulnerabilities, as it explains why jailbreaks succeed and informs the design of robust alignment strategies. Prior work shows that aligned LLMs encode harmfulness and refusal as separable directions in the residual stream at prompt-side token positions. We show that jailbreaks succeed at prompt encoding by suppressing either the refusal or harmfulness direction before any token is generated, with dis...
  </details>

- **2026-07-01** — Junlong Liu, Haobo Wang, Weiqi Luo et al. — [Beyond the Prompt: Jailbreaking Function-Calling LLMs via Simulated Moderation Traces](http://arxiv.org/abs/2607.00481v1)
  <details><summary>📄 Abstract</summary>
  Jailbreak attacks remain a critical threat to the safe deployment of large language models (LLMs). While prior work has primarily studied attacks and defenses at the prompt level, we show that this prompt-centric paradigm overlooks a structural vulnerability in stateful, function-calling environments. In such applications, developer-defined schemas, structured arguments, and untrusted tool outputs are interleaved into a single shared model context. This architecture expands the attack surface by...
  </details>

- **2026-06-30** — Moreno D'Incà, Massimiliano Mancini, Nicu Sebe — [Harnessing Textual Refusal Directions for Multimodal Safety](http://arxiv.org/abs/2606.31876v1)
  <details><summary>📄 Abstract</summary>
  To improve safety in Large Language Models (LLMs) we can either perform post-training alignment or exploit refusal directions in the activation space. Both strategies are less feasible in Multimodal LLMs (MLLMs) as they require unsafe multimodal data, harder to collect than their unimodal counterpart. In this work, we relax this constraint and investigate whether textual refusal directions, extracted directly from the LLM backbone, generalize across modalities (i.e., image, video). Preliminary f...
  </details>


### 📂 prompt-injection
*提示注入攻击 / Prompt Injection Attacks* — 2 papers

- **2026-07-01** — Brett Reynolds — [Adversarial Pragmatics for AI Safety Evaluation: A Benchmark for Instruction Conflict, Embedded Commands, and Policy Ambiguity](http://arxiv.org/abs/2607.01153v1)
  <details><summary>📄 Abstract</summary>
  Safety evaluations for language models increasingly depend on judgments about ambiguous natural-language behaviour: whether a model has followed an instruction, refused appropriately, complied with a policy, resisted an embedded command, or misreported progress in an agentic task. Existing benchmarks often compress these distinctions into pass/fail labels, obscuring whether failures arise from capability limits, policy ambiguity, instruction conflict, scaffold failure, or unstable evaluator judg...
  </details>

- **2026-06-30** — Yuanai Xie, Jiaxin Chen, Zhaozhi Liu — [Beyond Wireless Security: Covert Communications in Large Language Model-enabled Edge Networks](http://arxiv.org/abs/2606.31016v1)
  <details><summary>📄 Abstract</summary>
  Large language model (LLM)-enabled edge networks (LLMENs) offer mobile users high-quality and low-latency AI-generated content services in the 6G era. However, unlike typical edge networks, LLMENs present unique security challenges due to the inherent complexity of LLMs, their high computational overhead, and continuous interactions with users. Specifically, both frequent user interactions (i.e., queries and responses) over wireless channels and potential electromagnetic information leakage from...
  </details>


### 📂 memory-poisoning
*记忆投毒与篡改 / Memory Poisoning & Tampering* — 1 papers

- **2026-07-02** — Jiankai Jin, Xiangzheng Zhang, Zhao Liu et al. — [ElephantAgent: Contextual State Continuity in Agentic Systems](http://arxiv.org/abs/2607.01919v1)
  <details><summary>📄 Abstract</summary>
  Agentic systems enhance their capabilities by invoking external tools and maintaining persistent memory. However, these external dependencies introduce novel attack surfaces. Recent tool and memory poisoning attacks show that maliciously crafted tool descriptors and poisoned memory can covertly bias agent behavior. These threats reflect a deeper issue: the lack of verifiable continuity in the agent's contextual state for planning and execution. We present ElephantAgent, a protocol that enforces ...
  </details>


### 📂 tool-use-attack
*工具使用攻击 / Tool-Use Attacks* — 4 papers

- **2026-07-02** — Zimo Ji, Congying Xu, Zongjie Li et al. — [Cloak and Detonate: Scanner Evasion and Dynamic Detection of Agent Skill Malware](http://arxiv.org/abs/2607.02357v1)
  <details><summary>📄 Abstract</summary>
  LLM coding agents increasingly rely on third-party agent skills from public marketplaces, which execute with the agent's privileges and create a software supply-chain attack surface: a malicious skill can steal credentials, exfiltrate source code, or install backdoors. Existing defenses use static skill scanners based on pattern matching or LLM-as-judge analysis, but it remains unclear whether they withstand adaptive evasions that preserve malicious behavior while changing payload appearance.   ...
  </details>

- **2026-07-02** — Atharva Hans, Ilias Bilionis — [Coding-agents can replicate scientific machine learning papers](http://arxiv.org/abs/2607.02134v1)
  <details><summary>📄 Abstract</summary>
  Scientific machine learning papers typically make computational claims, e.g., that the relative mean square error is less than 5% or that the 95% predictive credible interval covers the test data. A coding agent can be prompted to replicate those claims from paper materials alone, but the prompt does not by itself reliably preserve progress or check whether generated evidence supports the paper's claims. We introduce Paper-replication, a workflow that makes each selected paper claim a target wit...
  </details>

- **2026-07-01** — Haoyu Gao, Jai Lal Lulla, Hong Yi Lin et al. — [From Registry to Repository: How AI Agent Skills Are Written, Adapted, and Maintained](http://arxiv.org/abs/2607.00911v1)
  <details><summary>📄 Abstract</summary>
  AI coding agents increasingly rely on skills: structured context bundles, typically a SKILL.md file with a YAML header and Markdown body, loaded on demand for domain knowledge, workflows, and scripts. Public registries such as skills.sh now host tens of thousands of skills, making them an emerging unit of reuse in agent-based software engineering. Yet skills have largely been viewed as agent capabilities rather than software artefacts whose content and evolution shape agent behaviour. We present...
  </details>

- **2026-07-01** — Changguo Jia, Tianqi Zhao, Runzhi He et al. — [Skills Are Not Islands: Measuring Dependency and Risk in Agent Skill Supply Chains](http://arxiv.org/abs/2607.01136v1)
  <details><summary>📄 Abstract</summary>
  Agent skills package reusable operational knowledge for Large Language Model (LLM) agents, yet as they grow in scope, they become dependency-bearing artifacts whose identities, versions, and provenance remain implicit. This opacity already causes duplicated dependencies and inconsistent installations, exposing a gap that dependency management has yet to close. We introduce Agent Skill Supply Chains (ASSCs) to characterize mixed skill-package-service dependency graphs and help close this gap. Bor...
  </details>


### 📂 backdoor
*后门与投毒攻击 / Backdoor & Poisoning Attacks* — 8 papers

- **2026-07-02** — Thomas Winninger — [Steerability via constraints: a substrate for scalable oversight of coding agents](http://arxiv.org/abs/2607.02389v1)
  <details><summary>📄 Abstract</summary>
  Coding agents are capable; human oversight is the bottleneck. Unconstrained agents introduce security risks, erode codebase scalability, and make human review increasingly costly. We argue that the same methods used for decades to manage large human engineering teams: access control, network policies, strict coding conventions enforced by tooling; transfer directly to coding agents, and are cheaper (in token) than recent agentic scaffolding. We sketch a start-to-end system on this principle, and...
  </details>

- **2026-07-02** — Yueming Huang, Wenhan Yao, Fen Xiao et al. — [DRL-CLBA: A Clean Label Backdoor Attack for Speech Classification via DDPG Reinforcement Learning](http://arxiv.org/abs/2607.01729v1)
  <details><summary>📄 Abstract</summary>
  Deep learning models for speech classification are vulnerable to backdoor attacks, where malicious triggers cause misclassification at inference time. While sample-specific attacks can bypass many defenses, they often rely on poisoned label attack, making them detectable via manual data defense. In this paper, we propose DRL-CLBA, a novel clean label backdoor attack for speech classification that leverages Deep Deterministic Policy Gradient (DDPG) reinforcement learning. We also utilize deep aud...
  </details>

- **2026-07-02** — Dipayan Saha, Khan Thamid Hasan, Shams Tarek et al. — [VeriChat: An Agentic Conversational AI Assistant for Hardware Security Verification](http://arxiv.org/abs/2607.01668v1)
  <details><summary>📄 Abstract</summary>
  Hardware security verification is a multi-stage process in which engineers must navigate complex design analyses, threat considerations, and verification strategies. They often need security-focused guidance, yet current verification environments provide little structured support for such assistance. Although conversational AI could offer such on-demand assistance, directly using general-purpose chatbots like ChatGPT or Gemini is risky due to their tendency to hallucinate and their reliance on s...
  </details>

- **2026-07-01** — Zhihao Dou, Qinjian Zhao, Zhiqiang Gao et al. — [ReShift: Aha-Moment-Driven Reasoning-Level Backdoor Attacks on Vision-Language Models](http://arxiv.org/abs/2607.00361v1)
  <details><summary>📄 Abstract</summary>
  Vision--Language Models (VLMs) are increasingly deployed in safety-critical applications, yet remain vulnerable to backdoor attacks. Existing methods primarily manipulate final outputs, often producing reasoning traces that are inconsistent or easily detectable. In this paper, we propose ReShift, the novel aha-moment-driven reasoning-level backdoor framework that explicitly redirects the internal chain-of-thought (CoT) trajectory while preserving surface-level coherence. ReShift introduces a Poi...
  </details>

- **2026-07-01** — Shayan Talaei, Abhinav Chinta, Devvrit Khatri et al. — [Distill to Detect: Exposing Stealth Biases in LLMs through Cartridge Distillation](http://arxiv.org/abs/2607.01208v1)
  <details><summary>📄 Abstract</summary>
  Language models deployed in high-stakes roles can potentially favor certain entities, brands, or viewpoints, steering user decisions at scale. Such preferential biases can be introduced by any actor in the model's supply chain and are most dangerous when the model reveals its preference only on the relevant topic while behaving identically to its unmodified base on all other inputs. Recent work has shown that these biases can transfer through context distillation on semantically unrelated data, ...
  </details>

- **2026-07-01** — Andrzej Szablewski, Gabriel Konar-Steenberg, Raffaello Fornasiere et al. — [The Model Organism Lottery: Model Organism Interpretability Strongly Depends on Training Methodology](http://arxiv.org/abs/2607.01033v1)
  <details><summary>📄 Abstract</summary>
  Model organisms (MOs) - language models trained to exhibit undesired or unnatural behaviours - are frequently used as testbeds for evaluating white-box interpretability techniques. Current MOs are typically constructed via post-hoc supervised fine-tuning (SFT) on behavioural transcripts or synthetic documents. Prior research has shown that interpretability methods can easily identify hidden behaviours in these MOs. However, recent work suggests that such post-hoc training methods may make interp...
  </details>

- **2026-07-01** — Chanwoo Choi, Euntae Kim, Kyuho Lee et al. — [KidnapRAG: A Black-Box Attack for Hijacking Reasoning in Agentic Retrieval-Augmented Generation Systems](http://arxiv.org/abs/2607.00422v1)
  <details><summary>📄 Abstract</summary>
  Retrieval-Augmented Generation (RAG) systems are vulnerable to poisoning attacks that inject malicious documents into the retrieval process to manipulate model outputs. Recent Agentic RAG systems are more robust to such attacks because they iteratively perform retrieval and reasoning, allowing them to ignore weakly relevant poisoned documents and preserve the reasoning chain induced by the user query. However, existing attacks on Agentic RAG systems often assume white-box access to system prompt...
  </details>

- **2026-06-30** — Zhengxing Li, David J. Miller, Guangmingmei Yang et al. — [CSO-LLM: Class Subspace Orthogonalization for Post-Training Backdoor Detection and Trigger Inversion in LLMs](http://arxiv.org/abs/2606.31309v1)
  <details><summary>📄 Abstract</summary>
  While post-training backdoor detection and trigger inversion schemes have been developed for AIs used e.g. for images, there is a paucity of such methods for LLMs. First, the LLM input space is discrete, with up to 150,000^k k-tuples to consider with k the token-length of a putative trigger. Second, one must blacklist tokens typical of the putative target response (class) of an attack, as such tokens may give false detection signals. However, a comprehensive blacklist is not available, in genera...
  </details>


### 📂 adversarial-attack
*对抗攻击 / Adversarial Attacks* — 2 papers

- **2026-07-02** — Haiyang Li, Yuming Fu, Qun Song et al. — [AGVBench: A Reliability-Oriented Benchmark of Data Augmentation for Vein Recognition](http://arxiv.org/abs/2607.02271v1)
  <details><summary>📄 Abstract</summary>
  Vein recognition is a secure biometric technology often constrained by limited annotated data and imaging variations. While data augmentation mitigates this, strategies designed for natural images may disrupt the fine-grained topology and textures essential for identity discrimination. We present AGVBench, which evaluates 30 representative augmentation strategies on five public palm- and finger-vein datasets with seven backbone architectures, covering classic CNNs, vision transformers, and vein-...
  </details>

- **2026-07-02** — Mahmoud Abdelfattah, Hamid Nasiri, Peter Garraghan — [kNNGuard: Turning LLM Hidden Activations into a Training-Free Configurable Guardrail](http://arxiv.org/abs/2607.02072v1)
  <details><summary>📄 Abstract</summary>
  Large language models (LLMs) are increasingly deployed in domains requiring guardrails to detect unsafe, off-topic, or adversarial prompts. Existing guardrails predominately rely on fine-tuning to build classifiers, which often suffer from low generalization and high inference latency. We present kNNGuard, a training-free guardrail that utilizes the activation space of an off-the-shelf LLM. Given a small bank of 50 safe and unsafe prompts, kNNGuard extracts hidden activations and performs multi-...
  </details>


### 📂 privacy-leakage
*隐私泄露 / Privacy Leakage* — 28 papers

- **2026-07-02** — Gemma Galdon Clavell, Pablo Accuosto, Usman Gohar — [The Eticas AI Risk Taxonomy: Open Infrastructure for Operationalizing AI Audits](http://arxiv.org/abs/2607.02201v1)
  <details><summary>📄 Abstract</summary>
  The rapid deployment of AI systems across high-stakes domains has created urgent demand for standardized evaluation, yet the field remains fragmented across competing risk taxonomies that catalog risks without showing how an audit is executed. At least 74 AI risk taxonomies exist, and almost all stop at the catalog. The hard part of auditing is not naming a risk but operationalizing it: turning it into a test run against a real system, a measured value, a calibrated severity, and a defensible gr...
  </details>

- **2026-07-02** — Jiale Amber Wang, Kaiyuan Wang, Pengyu Nie — [TestEvo-Bench: An Executable and Live Benchmark for Test and Code Co-Evolution](http://arxiv.org/abs/2607.02469v1)
  <details><summary>📄 Abstract</summary>
  Software tests and code evolve together: a code change should be followed by new or updated tests that record the new software behavior. Yet existing test generation and update benchmarks often isolate the test from the code change, and rely on static metadata that does not verify whether a test is executable or semantically tied to the code change. This makes it difficult to evaluate whether a test automation agent understands how a code change should propagate into the test suite.   We introdu...
  </details>

- **2026-07-02** — Seren Yenikent, Jack Vinijtrongjit, Katherine Ng — [Copewell: A Multi-Agent Swarm Architecture for Equitable Mental Wellness Support](http://arxiv.org/abs/2607.02245v1)
  <details><summary>📄 Abstract</summary>
  Mental health disorders affect nearly one billion people globally, yet 75% of individuals in low- and middle-income countries receive no treatment due to workforce shortages, cost barriers, and stigma. Current AI-powered wellness solutions predominantly rely on single-mode conversational interfaces that suffer high abandonment rates and fail to provide measurable, immediate relief calibrated to users' dynamic emotional states. This paper presents Copewell, a novel multi-agent swarm system design...
  </details>

- **2026-07-02** — Siyuan Li, Youyuan Zhang, Ruitong Liu et al. — [Multimodal Knowledge Edit-Scoped Generalization for Online Recursive MLLM Editing](http://arxiv.org/abs/2607.01978v1)
  <details><summary>📄 Abstract</summary>
  Online multimodal knowledge editing requires injecting a continual stream of visual-textual corrections into multimodal large language models (MLLMs) with bounded overhead and minimal disruption to unrelated behaviors. Existing editors mainly emphasize edit reliability and long-horizon stability, but rarely control the semantic boundary of each edit. Our pilot analyses of post-edit behaviors and internal neuronal activities reveal a scope gap behind reliable edits: instance-level success neither...
  </details>

- **2026-07-02** — Sofiane Ouaari, Kevin Vorwalder, Nico Pfeifer — [Assessing VLM Reliability for Medical Image Quality Evaluation Under Corruption and Bias](http://arxiv.org/abs/2607.01973v1)
  <details><summary>📄 Abstract</summary>
  Vision-Language Models (VLMs) are increasingly applied in medical tasks such as pathology description, report generation, and visual question answering. Medical Image Quality Assessment (MIQA) supports diagnostic accuracy and patient safety by determining whether images meet the standards required for clinical decision-making. Automating MIQA with VLMs may reduce workload, but their behavior under real-world conditions, where images may be degraded or textual context may affect judgments, should...
  </details>

- **2026-07-02** — Javier Irigoyen, Roberto Daza, Francisco Jurado et al. — [AIriskEval-edu: New Dataset for Risk Assessment in AI-mediated K-12 Educational Explanations](http://arxiv.org/abs/2607.01934v1)
  <details><summary>📄 Abstract</summary>
  This work introduces AIriskEval-edu-db2, a new dataset designed to train and evaluate auditors based on LLMs for an explainable pedagogical risk assessment in instructional content for grades K-12. The dataset comprises 1,639 explanations from 170 curated ScienceQA questions, covering science, language arts, and social sciences. For each question, the dataset includes an explanation written by a human teacher alongside 11 explanations generated by LLM-simulated teacher profiles associated with d...
  </details>

- **2026-07-02** — Yunhe Li, Hao Shi, Wenhao Liu et al. — [DemoPSD: Disagreement-Modulated Policy Self-Distillation](http://arxiv.org/abs/2607.02502v1)
  <details><summary>📄 Abstract</summary>
  On-policy self-distillation (OPSD) has emerged as a practical method for training large language models (LLMs) to reason, where a single model acts as both the teacher and the student with different levels of information access. However, recent studies have found that the teacher's dense token-level supervision, conditioned on privileged information, can lead to overfitting to in-domain patterns, suppress exploration, and hurt cross-domain generalization, while also introducing a more fundamenta...
  </details>

- **2026-07-02** — Quoc Bao Phan, Tuy Tan Nguyen — [QFedAgent: Quantum-Enhanced Personalized Federated Learning for Multi-Agent Activity Recognition](http://arxiv.org/abs/2607.02426v1)
  <details><summary>📄 Abstract</summary>
  Federated learning (FL) enables collaborative model training across distributed devices without sharing raw data, making it suitable for privacy-sensitive robotic sensing applications. However, multi-agent systems generate heterogeneous and non-independent and identically distributed (non-IID) multimodal sensor streams that degrade conventional FL algorithms, while classical fusion modules introduce substantial parameter overhead and communication cost. This paper proposes QFedAgent, a hybrid qu...
  </details>

- **2026-07-02** — Shuo Ren, Yaohui Han, Yifan Shi et al. — [A$^{2}$utoLPBench: An Auto-Generated, Agent-Friendly LP Benchmark via Inverse-KKT Construction](http://arxiv.org/abs/2607.02141v1)
  <details><summary>📄 Abstract</summary>
  Most LP-from-text benchmarks are static datasets of word problems written and labeled by hand. Once such a dataset is released, its size is fixed, its difficulty is fixed, and every problem can leak into the training data of future LLMs. We present \textbf{A$^{2}$utoLPBench}, a benchmark for testing LLM-driven agents on linear programming problems written in plain text. We first pick a feasible point and dual, then write down a problem for which that point is optimal and the objective value is k...
  </details>

- **2026-07-02** — Tzu-Heng Huang, Aditya Goyal, John Cooper et al. — [WARP: Weight-Space Analysis for Recovering Training Data Portfolios](http://arxiv.org/abs/2607.01686v1)
  <details><summary>📄 Abstract</summary>
  Foundation models are routinely released to the public, yet the data recipes used to train them -- such as domain mixture weights that determine how different sources are sampled -- are rarely disclosed. This creates an access asymmetry: researchers study the resulting models but lack visibility into the training distribution that produces them. Prior works for inferring training data, such as membership inference, detect at the level of individual samples and thus cannot characterize the global...
  </details>

- **2026-07-01** — George Alexakis, Dimitrios Schoinianakis, Giorgos Dimitrakopoulos — [High-Performance NTT Accelerators for PQC leveraging Unified Redundant Arithmetic and Fine-Tuned Microarchitecture](http://arxiv.org/abs/2607.00621v1)
  <details><summary>📄 Abstract</summary>
  Post-quantum cryptography and privacy-preserving technologies are expected to play a central role in future secure communication systems. Lattice-based PQC schemes such as ML-KEM (CRYSTALS-Kyber) and ML-DSA (CRYSTALS-Dilithium) rely heavily on large-degree polynomial arithmetic, making the Number Theoretic Transform (NTT) a key computational primitive. Although existing hardware accelerators exploit parallelism and pipelining to support both NTT and INTT, their efficiency is often limited by the...
  </details>

- **2026-07-01** — Arya Raeesi, Hanna Roed — [Auditing Forgetting in Limited Memory Language Models](http://arxiv.org/abs/2607.00605v1)
  <details><summary>📄 Abstract</summary>
  Limited Memory Language Models (LMLMs) externalize factual knowledge to a database to enable deletion-based unlearning without retraining. Existing evaluations measure post-deletion correctness in aggregate and cannot tell whether a deleted fact persists through residual parametric memory, alternative retrieval paths, or near-neighbor retrieval artifacts. We propose a causal auditing framework that holds the model fixed and varies the database state at inference time across three interventions: ...
  </details>

- **2026-07-01** — Shijie Li, Yilin Gao, Siyuan Yang et al. — [Multimodal Continuous Reasoning via Asymmetric Mutual Variational Learning](http://arxiv.org/abs/2607.00461v1)
  <details><summary>📄 Abstract</summary>
  Multimodal Large Language Models (MLLMs) are often constrained by a language-space bottleneck, forcing complex visual reasoning into discrete tokens which can lose perceptual nuance. A promising alternative is continuous latent reasoning, where the goal is to discover implicit reasoning pathways that bridge the multimodal query and the final answer. However, this introduces a severe train-inference mismatch: a training-time posterior, conditioned on the ground-truth answer, can exploit answer-de...
  </details>

- **2026-07-01** — Runhao Li, Xiaoxu Ma, Zhenyu Weng et al. — [Attribute-Prompted Kernel Hashing for Unsupervised Data-Efficient Cross-Modal Retrieval](http://arxiv.org/abs/2607.00379v1)
  <details><summary>📄 Abstract</summary>
  Unsupervised cross-modal hashing enables efficient retrieval of semantically related instances across different modalities without requiring manual semantic annotation. However, existing unsupervised methods rely heavily on large-scale image-text pairs. Collecting such data can be costly, particularly in scenarios where well-aligned pairs are scarce due to privacy and specialized constraints. More critically, existing methods tend to overfit to seen training data, restricting their generalizatio...
  </details>

- **2026-07-01** — Xuying Huang, Sicong Pan, Maren Bennewitz — [Privacy-Preserving Depth-Only Open-Vocabulary 3D Semantic Segmentation Via Uncertainty-Guided Test-Time Optimization](http://arxiv.org/abs/2607.00978v1)
  <details><summary>📄 Abstract</summary>
  Privacy-preserving perception is a critical requirement for deploying 3D scene understanding systems in real-world indoor environments, yet it remains underexplored in open-vocabulary 3D semantic segmentation. Existing methods typically rely on obtaining rich semantic cues from RGB images, which may expose privacy-sensitive visual information. Depth-only 3D geometry provides a privacy-preserving alternative, but the absence of appearance-based semantic cues makes open-vocabulary predictions high...
  </details>

- **2026-07-01** — Halil Sina Kelebek, Julia Hindel, Kobus Hoffman et al. — [Spotted: Location-informed Reidentification of Hyenas and Leopards in Camera Trap Surveys](http://arxiv.org/abs/2607.00804v1)
  <details><summary>📄 Abstract</summary>
  Animal re-identification (ReID) in camera-trap surveys remains challenging due to low image quality, strong variation in illumination and viewpoint, and highly imbalanced numbers of observations per individual. As a result, current ReID performance is often insufficient for fully automated use, and practical workflows typically depend on expert review of algorithmically proposed candidate matches. Moreover, most existing approaches focus almost exclusively on visual cues and overlook auxiliary i...
  </details>

- **2026-07-01** — Seref Baris Cagliyan, Umut Ozdemir, Merve Tapli et al. — [Caption Bottleneck Models](http://arxiv.org/abs/2607.00578v1)
  <details><summary>📄 Abstract</summary>
  Concept Bottleneck Models (CBMs) provide interpretability by routing predictions through a layer of human-understandable concepts. However, defining an optimal concept set for a specific dataset remains an open challenge. Existing approaches rely on expensive expert annotations or LLM-generated lists based solely on class names. Even "open-vocabulary" variants typically depend on static concept sets, which restrict discovery and introduce label bias. Furthermore, traditional CBMs often suffer fr...
  </details>

- **2026-07-01** — Prabod Rathnayaka, Fabian Waschkowski, Lukas Wesemann — [BaseRT: Best-in-Class LLM Inference on Apple Silicon via Native Metal](http://arxiv.org/abs/2607.00501v1)
  <details><summary>📄 Abstract</summary>
  We present BaseRT, a native Metal inference runtime for large language models (LLMs) on Apple Silicon, and report the highest inference throughput on this hardware to date. Existing runtimes, including llama.cpp and MLX-based frameworks, incur overhead from abstractions not designed for Metal's execution model or Apple Silicon's unified memory topology. By building natively on Metal with chip-specific kernel fusion, unified memory-aware optimisation, and custom dispatch logic, BaseRT recovers pe...
  </details>

- **2026-07-01** — John Kirchenbauer, Brian R. Bartoldson, Bhavya Kailkhura et al. — [Watermarking for Proprietary Dataset Protection](http://arxiv.org/abs/2607.00325v1)
  <details><summary>📄 Abstract</summary>
  A growing body of literature suggests that training data membership inference problems are fundamentally hard tasks in modern language modeling settings. We argue that output watermarking techniques are the right gadget to make training membership tests for generative models more tractable, based on prior results showing that language models exhibit residual watermark "radioactivity" under partially watermarked training datasets. We pit a watermark-based dataset inference approach head-to-head a...
  </details>

- **2026-07-01** — Hanning Yang, Meropi Karakioulaki, Lennart Purucker et al. — [LLM-Guided ODE Discovery and Parameter Inference from Small-Cohort Aggregate Data](http://arxiv.org/abs/2607.00733v1)
  <details><summary>📄 Abstract</summary>
  Mechanistic modeling via ordinary differential equations (ODEs) provides interpretable descriptions of complex dynamics and enables inference of underlying mechanisms, which is particularly valuable in clinical settings. However, in rare diseases, both the structure and parameters of the model are typically unknown, while individual-level data is scarce, noisy, heterogeneous, and subject to privacy constraints. In such settings, population-level summary statistics provide a practical privacy-pre...
  </details>

- **2026-06-30** — Kai Hu, Akash Bharadwaj, Weichen Yu et al. — [Steal the Patch Size: Adversarially Manipulate Vision-Language Models](http://arxiv.org/abs/2607.00174v1)
  <details><summary>📄 Abstract</summary>
  We present a black-box model-stealing attack that recovers private vision-tokenizer configurations of deployed vision-language models (VLMs), including the visual patch size and input preprocessing pipeline. The key idea is a task-level side channel induced by ViT-style patchification: when a synthetic grid image is aligned with the hidden patch grid, boundary cues are erased at tokenization, causing periodic accuracy drop. By sweeping the grid cell size and measuring these collapses, we infer t...
  </details>

- **2026-06-30** — Wojciech Łapacz, Stanisław Pawlak — [Amplifying Membership Signal Through Chained Regeneration](http://arxiv.org/abs/2606.31991v1)
  <details><summary>📄 Abstract</summary>
  The tendency of large generative models to memorize training data makes sample verification critical for privacy auditing and copyright enforcement. Current membership (MIA) and dataset inference (DI) attacks often rely on one-shot generations, which yield weak signals and limited sensitivity across modalities. Inspired by Model Autophagy Disorder (MAD), we introduce MADreMIA, a model-agnostic framework that enhances white-, gray-, and black-box MIA and DI. Rather than relying on shadow model tr...
  </details>

- **2026-06-30** — Dariush Wahdany, Matthew Jagielski, Jesse C. Cresswell et al. — [TabPATE: Differentially Private Tabular In-Context Learning Without Public Data](http://arxiv.org/abs/2606.31474v1)
  <details><summary>📄 Abstract</summary>
  Tabular foundation models enable accurate in-context learning (ICL) from small labeled datasets, but the private records placed in context can leak through model predictions. We first show that even basic membership inference attacks succeed against tabular ICL, motivating formal privacy protection. We then introduce TabPATE, a differentially private PATE-style defense for tabular ICL that does not require public in-distribution data. TabPATE partitions the private context across teacher models,...
  </details>

- **2026-06-30** — Robert Schambach, Quoc Do Le, Sergei Arnautov et al. — [EnclaveX: End-to-End Confidential AI with CPU/GPU TEEs](http://arxiv.org/abs/2606.31408v1)
  <details><summary>📄 Abstract</summary>
  Large Language Models (LLMs) have rapidly proliferated, driving widespread adoption of AI applications. Most deployments rely on centralized infrastructures such as Microsoft Azure, Google Cloud, or AWS, requiring users to share sensitive data and training or fine-tuning code. This dependence raises significant security and privacy concerns, as cloud providers must be trusted to ensure confidentiality and integrity.   Trusted Execution Environments (TEEs) e.g., Intel SGX/TDX, AMD SEV-SNP, and AR...
  </details>

- **2026-06-30** — Zekai Chen, Kairui Yang, Xuaner Chen et al. — [FedLAB: Traceable Semantic Codebooks for Federated Multimodal Graph Foundation Learning](http://arxiv.org/abs/2606.32016v1)
  <details><summary>📄 Abstract</summary>
  Multimodal graph foundation models aim to learn reusable knowledge from graphs enriched with text, images, attributes, and relational topology, thereby supporting diverse graph-centric and modality-centric tasks. In practice, however, such multimodal graphs are often distributed across decentralized clients, where raw contents and local structures cannot be centrally shared due to privacy constraints. This motivates federated multimodal graph foundation learning, which requires not only transfer...
  </details>

- **2026-06-30** — Fabio Quattrini, Carmine Zaccagnino, Enis Simsar et al. — [Editing Everything Everywhere All at Once](http://arxiv.org/abs/2606.31278v1)
  <details><summary>📄 Abstract</summary>
  Editing multiple elements of an image in a single forward pass is a practical alternative to multi-turn image manipulation, offering improved efficiency and potentially better harmonization. However, when several instructions target different regions, semantic interference often leads to attribute leakage and poor edit disentanglement, especially as the number of edits increases. In this work, we propose MICE (Multi-Instance Concurrent Editing), a training-free strategy for scalable multi-instan...
  </details>

- **2026-06-30** — Ramón Soto C., Liz Soto — [Federated Sovereign Transport Protocol (FSTP): Verifiable Coordination Without Disclosure](http://arxiv.org/abs/2607.00213v1)
  <details><summary>📄 Abstract</summary>
  This paper introduces the Federated Sovereign Transport Protocol (FSTP), a synchronization boundary and transport layer for federated networks in which nodes have heterogeneous privacy requirements. Existing federation protocols leave data confinement to operator policy: they define message formats and delivery semantics but impose no structural constraint on what a conforming server may emit. FSTP addresses this gap by making data confinement a property of the protocol itself.   The central mec...
  </details>

- **2026-06-30** — Yukun Zhang, Kemu Xu — [Delegation Rights: Property, Agency, and Investment Incentives in the Age of AI Agents](http://arxiv.org/abs/2606.31935v1)
  <details><summary>📄 Abstract</summary>
  AI agents increasingly operate inside digital accounts by exercising privileges that users already hold, raising a new control question: whether an existing account entitlement must be exercised manually or may be exercised through a user-authorized automated proxy. We define \emph{delegation rights} as the revocable, identity-preserving, scope-limited, and mode-specific authority of an account holder to authorize such proxy execution. We develop a three-party incomplete-contracts model with a U...
  </details>


### 📂 misuse
*滥用与误用 / Misuse & Abuse* — 5 papers

- **2026-07-02** — Thomas Winninger — [Fast Multi-dimensional Refusal Subspaces via RFM-AGOP](http://arxiv.org/abs/2607.02396v1)
  <details><summary>📄 Abstract</summary>
  Steering and monitoring activations in Large Language Models (LLMs) are increasingly used for both safety and interpretability. Early work assumed behaviours are encoded along single linear directions, but recent findings suggest complex behaviours, such as the refusal to answer harmful queries, live in multi-dimensional subspaces. However, existing methods for extracting these subspaces are computationally expensive, which becomes prohibitive on reasoning models who produce long reasoning trace...
  </details>

- **2026-07-01** — Zidong Zhang, Zhentao Xie, Wenrui Diao et al. — [(A)I Sees What You Don't: Exploiting New Attack Surfaces in Third-Party Mobile Agents](http://arxiv.org/abs/2607.00333v1)
  <details><summary>📄 Abstract</summary>
  Third-party mobile agents powered by Vision-Language Models (VLMs) have emerged as a promising paradigm for automating smartphone interactions. These agents act as high-privilege decision-makers, perceiving device states through screenshots and executing actions via VLM reasoning, transforming how an agent app interacts with the environment (i.e., other apps or the OS). Correspondingly, this transformation introduces new attack surfaces or transforms benign/harmless interfaces into exploitable o...
  </details>

- **2026-06-30** — Taeyoun Kim, Aviral Kumar — [Addressing Over-Refusal in LLMs with Competing Rewards](http://arxiv.org/abs/2606.31748v1)
  <details><summary>📄 Abstract</summary>
  Safety training on language models often induces over-refusal: improved safety on harmful prompts at the cost of increased refusal on harmless ones. Though this trade-off can be mitigated by training models with reinforcement learning (RL) to reason before answering, it does not remove the underlying problem that reasoning can often be a "rubber stamp" for a predetermined response. In this paper, we address the safety-refusal trade-off by rethinking how models are trained to reason about safety....
  </details>

- **2026-06-30** — Mohammadamin Shafiei, Shuyue Stella Li, Yulia Tsvetkov — [Moral Safety in LLMs: Exposing Performative Compliance with Puzzled Cues](http://arxiv.org/abs/2606.31644v1)
  <details><summary>📄 Abstract</summary>
  As large language models take on morally consequential roles in healthcare, legal, and hiring contexts, we need to examine whether their ethical behaviors are genuine or superficial. We show that current fairness evaluations substantially overestimate moral safety. Models appear fair when demographic identity is stated as an explicit label, yet become measurably less fair when the same identity must be inferred. We term this failure \emph{performative compliance}, where a model is fair when the ...
  </details>

- **2026-06-30** — Yunjin Tong — [A Contextual-Bandit Oversight Game with Two-Sided Informational Asymmetry](http://arxiv.org/abs/2607.00155v1)
  <details><summary>📄 Abstract</summary>
  We study runtime human oversight of an AI agent when private information runs in both directions: the human privately knows her reward function, while the AI privately knows the quality of the action it proposes. This is the kind of asymmetry that arises naturally when an autonomous robot or software agent has inspected a situation its human supervisor cannot directly assess. Building on Cooperative Inverse Reinforcement Learning (CIRL) and the Oversight Game, we introduce a contextual-bandit te...
  </details>


### 📂 red-teaming
*红队测试 / Red Teaming* — 2 papers

- **2026-07-02** — Navaneeth Sangameswaran, Preetham S, Ashmiya Lenin — [HaloGuard 1.0: An Open Weights Constitutional Classifier for Multilingual AI Safety](http://arxiv.org/abs/2607.02079v1)
  <details><summary>📄 Abstract</summary>
  We present HaloGuard 1.0, an open-weights implementation of the constitutional-classifier paradigm for input safety. It achieves state-of-the-art performance on English and multilingual prompt-safety benchmarks at roughly one-tenth the model size of current leading open guard models. The safety constitution is the organising structure of the corpus: a natural-language constitution of 46 policies and 2,940 subcategories drives synthetic data generation, with exhaustive one-to-one paired counterfa...
  </details>

- **2026-07-02** — Mona Schirmer, Metod Jazbec, Alexander Timans et al. — [Online Safety Monitoring for LLMs](http://arxiv.org/abs/2607.02510v1)
  <details><summary>📄 Abstract</summary>
  Despite alignment training, LLMs remain prone to generating unsafe outputs at deployment time. Monitoring outputs online and raising an alarm when safety can no longer be assumed is therefore critical. We study a simple real-time monitor that turns a verifier signal from an external model into an alarm decision by thresholding, with the threshold calibrated via risk control. In experiments on mathematical reasoning and red teaming datasets, we show that this simple design is competitive with mor...
  </details>


### 📂 vulnerability
*漏洞与攻击面 / Vulnerabilities & Attack Surfaces* — 46 papers

- **2026-07-02** — Josh Hills, Ida Caspary, Asa Cooper Stickland — [Distributed Attacks in Persistent-State AI Control](http://arxiv.org/abs/2607.02514v1)
  <details><summary>📄 Abstract</summary>
  As AI coding agents become more autonomous, they increasingly ship code iteratively, with the codebase persisting across sessions. This persistence creates a new attack surface: a misaligned or prompt-injected agent can distribute attacks across pull requests (PRs) and time its payload for the PR with the best natural cover. To study the resulting dynamics, we introduce Iterative VibeCoding, a setting for AI control, the study of safely deploying capable but potentially untrusted AI. In Iterativ...
  </details>

- **2026-07-02** — Bohan Liu, Wenqian Ye, Guangzhi Xiong et al. — [Towards Robustness against Typographic Attack with Training-free Concept Localization](http://arxiv.org/abs/2607.02494v1)
  <details><summary>📄 Abstract</summary>
  Models trained via Contrastive Language-Image Pretraining (CLIP) serve as the foundational vision encoders for most modern Large Vision Language Models (LVLMs). Despite their widespread adoption, CLIP models exhibit a critical yet underexplored failure mode: irrelevant text appearing within images confounds visual representations, biasing them toward lexical meaning rather than true visual semantics. This robustness issue, commonly described as a Typographic Attack (TA), exposes a vulnerability ...
  </details>

- **2026-07-02** — Pedro Santos, Joel Reis, Paulo Oliveira et al. — [QuadRocket: An Aerial Robotic Testbed for Adaptive Thrust-Vector Control of Rocket-Like Vehicles](http://arxiv.org/abs/2607.02474v1)
  <details><summary>📄 Abstract</summary>
  This paper presents QuadRocket, a quadrotor-based rocket prototype that provides a low-cost, low-risk platform for validating advanced thrust-vector control strategies for launch vehicle-type systems. The prototype consists of a cylindrical main body mounted on top of a quadrotor through a universal joint, forming a flying inverted pendulum with non-negligible inertia. For control design, the coupled system is modeled as a single axisymmetric rigid body actuated by a vectored force applied along...
  </details>

- **2026-07-02** — Temitayo Olamilekan Ogunsusi, Lijun Qian, Xishuang Dong — [UA-ChatDev: Uncertainty-Aware Multi-Agent Collaboration for Reliable Software Development](http://arxiv.org/abs/2607.02186v1)
  <details><summary>📄 Abstract</summary>
  Software development is a complex task that demands cooperation among agents with diverse roles. Large language models (LLMs) have enabled autonomous multi-agent software development frameworks that leverage role-based collaboration to automate requirements analysis, coding, testing, and refinement. However, existing approaches typically assume that intermediate agent outputs are equally reliable, leaving them vulnerable to hallucination propagation, where incorrect decisions generated in early ...
  </details>

- **2026-07-02** — Chuxi Nan, Di Wu, Hongming Guo et al. — [Multimodal Fusion for Fine-Grained Classification of Breast Fibroadenoma and Phyllodes Tumors](http://arxiv.org/abs/2607.02091v1)
  <details><summary>📄 Abstract</summary>
  Breast fibroadenoma (FA) and phyllodes tumor (PT) are fibroepithelial breast lesions with highly overlapping appearances on B-mode ultrasound, making benign and borderline PT prone to being misclassified as FA and complicating preoperative decision-making. Existing computer-aided diagnosis methods commonly rely on single-modal imaging features and insufficiently exploit complementary clinical and textual information. To address this limitation, we construct the FAPT-M Dataset, a pathology-confir...
  </details>

- **2026-07-02** — Shuhan Liu, Yukai Zhao, Xing Hu et al. — [Mitigating Package Hallucinations in Large Language Models via Model Editing](http://arxiv.org/abs/2607.02052v1)
  <details><summary>📄 Abstract</summary>
  Large language models (LLMs) have demonstrated strong capabilities in software engineering tasks, such as code generation, library recommendation, and dependency configuration. However, recent studies show that LLMs may suffer from package hallucination, where they generate non-existent or invalid package names. These hallucinations can be exploited in software supply chain attacks, as attackers may register malicious packages under hallucinated names. Therefore, mitigating package hallucination...
  </details>

- **2026-07-02** — Feng Li, Chaokun Zhang, Gong Chen — [Sparse-Aware Vector Quantization for Bandwidth-Efficient Collaborative 3D Semantic Occupancy Prediction](http://arxiv.org/abs/2607.01928v1)
  <details><summary>📄 Abstract</summary>
  Collaborative perception extends single-agent perception by enabling multiple vehicles to exchange complementary perceptual information. However, it introduces an inherent trade-off between perception gain and communication overhead, which is particularly severe for 3D semantic occupancy prediction that relies on fine-grained spatial structures. Existing methods typically compress 3D features into 2D, causing severe spatial information loss, or transmit dense 3D representations, hindering real-w...
  </details>

- **2026-07-02** — Yuanzhi Liu, Shousheng Zhao, Bo Zhou et al. — [MMBench-Live: A Continuously Evolving Benchmark for Multimodal Models](http://arxiv.org/abs/2607.01813v1)
  <details><summary>📄 Abstract</summary>
  Evaluation benchmarks are essential for assessing vision-language models (VLMs), but most multimodal benchmarks are static, making them vulnerable to temporal staleness, data contamination, and costly maintenance. We present MMBench-Live, a continuously evolving multimodal benchmark built by a multi-agent-driven automated pipeline. Our framework treats benchmark evolution as task-guided dataset construction, integrating structured benchmark specification, feedback-controlled real-time data acqui...
  </details>

- **2026-07-02** — Weili Guan, Haoyu Zhang, Meng Liu et al. — [SpaceEra++: A Unified Framework Towards 3D Spatial Reasoning in Video](http://arxiv.org/abs/2607.01784v1)
  <details><summary>📄 Abstract</summary>
  Visual-spatial understanding, defined as the ability to infer object relationships and scene layouts from visual inputs, is fundamental to downstream tasks such as robotic navigation and embodied interaction. However, pre-trained vision-language models (VLMs) remain constrained by spatial uncertainty stemming from inherently 2D observations and by the scarcity of data for 3D spatial understanding. To address these limitations, we proposed a novel framework, SpaceEra, in the NeurIPS 2025 Spotligh...
  </details>

- **2026-07-02** — Mingzhe Du, Luu Anh Tuan, Tianyi Wu et al. — [Mastermind: Strategy-grounded Learning for Repository-Scale Vulnerability Reproduction](http://arxiv.org/abs/2607.01764v1)
  <details><summary>📄 Abstract</summary>
  Repository-level vulnerability reproduction is a demanding software engineering (SE) task: an agent must inspect a codebase, infer the input grammar that reaches a vulnerable path, construct a proof-of-conceptv(PoC), and verify that the crash disappears on the patched build. Recent LLM agents can often execute these steps when the approach is correct, yet they still fail by choosing the wrong strategy. This paper argues that strategy, rather than the full action trajectory, is the right learning...
  </details>

- **2026-07-02** — Zirui Chen, Zhipeng Xue, Jiayuan Zhou et al. — [Refploit: Facilitating Exploit Construction via Code-Agent Trajectory Repair](http://arxiv.org/abs/2607.01760v1)
  <details><summary>📄 Abstract</summary>
  Vulnerability exploits play a crucial role in assessing the downstream impact of Java library vulnerabilities. While some vulnerabilities are accompanied by disclosed exploit references, automatically reproducing such references into runnable exploits remains challenging because they are often incomplete, unstructured, or only describe partial reproduction steps. Recent code agents provide a promising way to automate this process, but our study shows that their generated exploits often appear su...
  </details>

- **2026-07-02** — Yuqiang Sun, Han Liu, Ying Li et al. — [Knowledge Over Parameters: Evolving Smart Contract Vulnerability Detection](http://arxiv.org/abs/2607.01742v1)
  <details><summary>📄 Abstract</summary>
  Smart contract vulnerabilities are predominantly logic bugs whose detection requires structured, step-by-step procedural knowledge of attack patterns and contract semantics. Existing LLM-based methods struggle to generate this knowledge automatically: prompt-based methods rely on manually crafted detection rules, while fine-tuning requires massive labeled datasets that are inherently scarce in this domain. We present EvoVuln, an automated framework that reformulates vulnerability detection as a ...
  </details>

- **2026-07-02** — Stefano Masini, Cecilia Viscardi, Michela Baccini — [Full Bayesian Reinforcement Learning via LF-IBIS](http://arxiv.org/abs/2607.01741v1)
  <details><summary>📄 Abstract</summary>
  Reinforcement Learning (RL) is a sequential decision-making framework in which an agent learns optimal policies through interaction with an environment by maximizing cumulative rewards. Among RL methods, Bayesian Reinforcement Learning (BRL) addresses common practical challenges related to data scarcity by leveraging prior knowledge about the environment and sequential belief updates. However, most BRL approaches require an explicit likelihood function, which is frequently inaccessible or intrac...
  </details>

- **2026-07-02** — Zhiyuan Zhang, Adeesh Desai, Jyun-Chi Hu et al. — [Imagining the Sense of Touch: Touch-Informed Manipulation via Imagined Tactile Representations](http://arxiv.org/abs/2607.01684v1)
  <details><summary>📄 Abstract</summary>
  Tactile sensing can substantially improve contact-rich robotic manipulation, yet its practical deployment remains limited by the fragility, calibration requirements, and maintenance burden of tactile hardware. This raises a fundamental question: can robots benefit from tactile knowledge without requiring tactile sensors at deployment? We present TacImag, a tactile imagination framework that predicts tactile observations from vision and proprioception and uses the generated signals to guide manip...
  </details>

- **2026-07-02** — Mingkai Zheng, Junlin Chen, Haotian Xie et al. — [SCAPE: Accurate and Efficient LLM Training with Extreme Sparse Communication](http://arxiv.org/abs/2607.01678v1)
  <details><summary>📄 Abstract</summary>
  Communication increasingly dominates the cost of Large Language Model (LLM) pre-training, especially under data-parallel and sharded training schemes, where gradient synchronization and parameter reconstruction overhead increase with model size and system scale. Existing communication-reduction methods either sparsify raw gradients, which can be unstable for modern Adam-style optimizers at high sparsity, or quantize communication, whose savings are fundamentally bounded by bit width and often in...
  </details>

- **2026-07-02** — Haotian Xie, Junlin Chen, Mingkai Zheng et al. — [DeadPool: Resilient LLM Training with Hot-Swapping via Zero-Overhead Checkpoint](http://arxiv.org/abs/2607.01646v1)
  <details><summary>📄 Abstract</summary>
  State-of-the-art large language model (LLM) training takes tens of thousands of graphics processing units (GPUs) for months and encounters failures across the software and hardware stack. Existing fault-tolerance mechanisms either impose non-trivial overhead during failure-free execution or suffer from prolonged recovery latency, particularly under scenarios where a small subset of compute nodes experience permanent failures. %The tradeoff between failure-free overhead and recovery latency forms...
  </details>

- **2026-07-02** — Zimo Ji, Zekai Zhang, Congying Xu et al. — [Coding Agents Are Guessing: Measuring Action-Boundary Violations in Underspecified DevOps Instructions](http://arxiv.org/abs/2607.02294v1)
  <details><summary>📄 Abstract</summary>
  LLM coding agents are increasingly deployed to act autonomously on real production infrastructure. They execute shell commands, modify repositories, and call operational APIs. However, completing a task is not sufficient for safety. A wrong action can cause severe consequences. Existing agent benchmarks largely emphasize task completion, leaving open how agents behave under benign but underspecified instructions.   We present UnderSpecBench, a benchmark for measuring action-boundary violations i...
  </details>

- **2026-07-01** — Ahmet Nuri Cevik, Sinem Coleri — [Meta-Transfer Learning for mmWave Beam Alignment](http://arxiv.org/abs/2607.00860v1)
  <details><summary>📄 Abstract</summary>
  Millimeter-wave (mmWave) beam alignment plays a critical role in next-generation wireless systems, yet its efficient implementation remains challenging. Meta-learning and transfer learning have been explored to enable deep learning-based beam prediction models to rapidly adapt to unseen environments; however, existing meta-learning approaches adapt the entire network and are trained from random initialization, leading to a large number of updated parameters and a high meta-training cost, while t...
  </details>

- **2026-07-01** — Sheng Qiang, Ruiwei Chen, Yinpeng Wu et al. — [MosaicKV: Serving Long-Context LLM with Dynamic Two-D KV Cache Compression](http://arxiv.org/abs/2607.00760v1)
  <details><summary>📄 Abstract</summary>
  Long-context LLM services now sustain prompts with hundreds of thousands to millions of tokens, making the key-value (KV) cache a first-order serving cost. Because the cache grows linearly with context length, it can exhaust GPU memory, force smaller batches, and reduce serving throughput. Prior KV cache compression techniques typically target only the sequence dimension or only the channel dimension, which leaves limited headroom as context windows scale. Compressing both dimensions promises hi...
  </details>

- **2026-07-01** — Emanuele Caglioti, Marco Cecchini — [Time Averages for the Vortex Model and Stroboscopic Ergodic Averages](http://arxiv.org/abs/2607.00721v1)
  <details><summary>📄 Abstract</summary>
  We consider the vortex model on the plane, focusing on the case of vortices with the same sign and, for simplicity, assuming all vortices possess equal circulation. In particular we are interested at the time average of the vorticity density, i.e. the empirical measure associated to the vortices.   We conjecture that, for a.e. initial data, the time average of the empirical density is radial.   We prove the result for N=3 vortices by exploiting the integrability of the system.   For N > 3 vortic...
  </details>

- **2026-07-01** — Yingjie Dai, Tianyang Xu, Yanglin Deng et al. — [Partial Skeleton Visibility for Action Recognition: A Constrained Field-of-View Approach](http://arxiv.org/abs/2607.00716v1)
  <details><summary>📄 Abstract</summary>
  Skeleton-based action recognition has achieved remarkable success by exploiting joint coordinates and their topological connections, yet prevailing methods overwhelmingly assume complete and clean skeleton inputs. In real-world deployments, such as egocentric vision, crowded surveillance, wearable devices, or edge robotics, limited field-of-view (FoV) frequently causes substantial joint visibility dropout, leading to severe performance degradation that existing models are largely unprepared to h...
  </details>

- **2026-07-01** — Seokhee Jin, Changhwan Sung, Sunung Mun et al. — [AdaBoosting Text Prompts for Vision-Language Models](http://arxiv.org/abs/2607.00684v1)
  <details><summary>📄 Abstract</summary>
  The classification accuracy of pretrained Vision-Language Models (VLMs) relies on the quality of the text prompts. Handcrafted templates and Large Language Model (LLM)-generated descriptions not only make predictions more interpretable, but also enable reuse of the same prompts across heterogeneous VLMs. Recent works construct task-adapted text prompts with a small number of labeled images. However, existing few-shot text prompting methods do not explicitly focus on misclassified examples during...
  </details>

- **2026-07-01** — Yifei Sun, Zemin Liu, Bryan Hooi et al. — [Multi-Label Node Classification with Label Influence Propagation](http://arxiv.org/abs/2607.00671v1)
  <details><summary>📄 Abstract</summary>
  Graphs are a complex and versatile data structure used across various domains, with possibly multi-label nodes playing a particularly crucial role. Examples include proteins in PPI networks with multiple functions and users in social or e-commerce networks exhibiting diverse interests. Tackling multi-label node classification (MLNC) on graphs has led to the development of various approaches. Some methods leverage graph neural networks (GNNs) to exploit label co-occurrence correlations, while oth...
  </details>

- **2026-07-01** — Camila C. Soares, Luis B. Castro, Antonio S. de Castro — [Scattering, bound states, and resonances in the one-dimensional Dirac equation via supersymmetric quantum mechanics](http://arxiv.org/abs/2607.00306v1)
  <details><summary>📄 Abstract</summary>
  We develop a unified treatment of scattering and discrete spectra for the one-dimensional Dirac equation with scalar and vector interactions. Under the spin-symmetry condition, the coupled first-order Dirac system maps exactly onto an effective Sturm--Liouville (Schrö\-din\-ger-like) problem for a single spinor component. This mapping provides a convenient framework for analyzing transmission, reflection, and analytic continuation. As an explicit application, we consider effective interactions o...
  </details>

- **2026-07-01** — Xiangyue Liu, Zijian Zhang, Miles Yang et al. — [Rosetta: Composable Native Multimodal Pretraining](http://arxiv.org/abs/2607.00293v1)
  <details><summary>📄 Abstract</summary>
  Achieving true artificial general intelligence requires foundation models capable of integrating new modalities without forgetting prior knowledge. However, accommodating continuous generative objectives alongside discrete understanding tasks causes severe gradient conflicts. Existing architectures, including standard Mixture-of-Experts (MoE), are highly susceptible to representation overwriting. Even structurally partitioned paradigms like Mixture-of-Transformers (MoT) remain vulnerable to cata...
  </details>

- **2026-07-01** — Luigi Petruzziello, Camilla Fioravanti, Gabriele Oliva — [Distributed Containment of a Compromised Agent through Repulsive Cages](http://arxiv.org/abs/2607.01230v1)
  <details><summary>📄 Abstract</summary>
  UAV swarms and cyber-physical multi-agent systems are increasingly deployed in safety-critical missions that require coordinated motion, distributed decision making, and autonomy. A major security risk arises when a legitimate agent is hijacked and driven by adversarial high-level commands. Rather than focusing on detection and isolation of malicious agents, we exploit a structural property common in autonomous platforms: low-level collision-avoidance modules are typically implemented as indepen...
  </details>

- **2026-07-01** — Michele Armillotta, Nicolò Romandini, Rebecca Montanari et al. — [Antaeus: Hunting Repository-Level Logic Vulnerabilities via Context-Grounded LLM Reasoning](http://arxiv.org/abs/2607.01138v1)
  <details><summary>📄 Abstract</summary>
  LLM-based vulnerability detectors have shown promising results in identifying memory-safety bugs and vulnerability classes whose violations can often be expressed through established security properties. Logic vulnerabilities, however, pose a different challenge, as their identification requires inferring application-specific security invariants and implicit assumptions about intended behavior. Even frontier agentic models struggle because these invariants are often implicit and buried among unr...
  </details>

- **2026-07-01** — Shaoheng Zhang, Zhichen Li, Jie Mei — [DART-VLN: Test-Time Memory Decay and Anti-Loop Regularization for Discrete Vision-Language Navigation](http://arxiv.org/abs/2607.01043v1)
  <details><summary>📄 Abstract</summary>
  Memory-based discrete vision-language navigation (VLN) agents must act under partial observability, yet even strong frozen backbones remain vulnerable at test time. Two common failure modes are stale historical evidence at memory readout and inefficient local backtracking during action selection. We present DART-VLN, a training-free test-time control framework for discrete VLN. DART-VLN combines Test-Time Memory Decay, a read-side memory reweighting rule that suppresses stale and redundant evide...
  </details>

- **2026-07-01** — Sicong Cao, Hao Ma, Le Yu et al. — [Knowledge-Enhanced Agentic Vulnerability Repair](http://arxiv.org/abs/2607.00820v1)
  <details><summary>📄 Abstract</summary>
  Frontier foundation models have changed the math on vulnerability discovery, but the bigger challenge is how the remediation side keeps up. Despite recent progresses in Automated Vulnerability Repair (AVR), current solutions struggle to reliably identify the root causes of vulnerabilities, and insufficiently utilize the prior fix knowledge to guide the patch generation process, thus undermining their effectiveness in practice.   To address this gap, we propose KeaRepair, a novel agentic AVR appr...
  </details>

- **2026-06-30** — Liming Wang, Neguine Rezaii, Bradford C. Dickerson et al. — [Do Multimodal Large Language Models Need Reasoning to Classify Dementia from Speech?](http://arxiv.org/abs/2607.00260v1)
  <details><summary>📄 Abstract</summary>
  Multimodal large language models (MLLMs) have emerged as a promising approach for improving the accuracy, transferability, and explainability of automatic dementia classification (ADC) systems from voice recordings. Yet it remains unclear whether their reasoning capabilities are beneficial for ADC, and how such capabilities should be leveraged. In this paper, we conduct a careful evaluation of reasoning MLLMs for ADC and show that naive strategies, such as relying on text-based rationales, can l...
  </details>

- **2026-06-30** — Saif Mahmud, Fadul Sikder, Yuede Ji et al. — [The Illusion of Safety: Multi-Tier Verification of AI vs. Human C++ Code](http://arxiv.org/abs/2607.00107v1)
  <details><summary>📄 Abstract</summary>
  Large language models increasingly generate C++, a memory-unsafe language where a single overlooked violation can become an exploitable bug. Yet most security evaluations of AI-generated code rely on static analysis alone, which flags warnings without confirming runtime violations or reasoning about untested paths. We ask whether AI-generated C++ is measurably less safe than human-written code, and whether common verification tools agree on the risk. We introduce VULBENCH-CPP, a benchmark of 8,9...
  </details>

- **2026-06-30** — Yufei Li, Zaiwei Zhang, Mingfu Liang et al. — [GR2 Technical Report](http://arxiv.org/abs/2606.31984v1)
  <details><summary>📄 Abstract</summary>
  Industrial recommendation systems serve billions of users through a multi-stage funnel -- retrieval, early-stage ranking, and re-ranking -- where the final re-ranking step disproportionately shapes user engagement and downstream performance, particularly for carousel and grid display formats. Despite growing enthusiasm for Large Language Models (LLMs) in recommendation, three gaps hinder industrial adoption: (1) most efforts target retrieval and ranking, leaving re-ranking -- the stage closest t...
  </details>

- **2026-06-30** — Sitao Chen, Zhuangwei Zhuang, Hui Luo et al. — [Semantic Occupancy Prediction with Dual Range-Voxel Representation](http://arxiv.org/abs/2606.31688v1)
  <details><summary>📄 Abstract</summary>
  LiDAR-based 3D semantic occupancy prediction, which aims to provide accurate and comprehensive scene representation, is crucial for autonomous driving systems. As point clouds suffer from sparsity and incompleteness, leading to insufficient semantic learning and difficult occupancy perception, existing methods often stack multi-sweep point clouds to obtain dense spatial information. However, such a naive strategy also results in efficiency (e.g., additional computational burden) and robustness (...
  </details>

- **2026-06-30** — Basant Agarwal, Dincy R. Arikkat, Swati Yadav et al. — [CVE-TTP KG: Knowledge Graph Linking Software Vulnerabilities to Attack Behaviors](http://arxiv.org/abs/2606.31557v1)
  <details><summary>📄 Abstract</summary>
  In the evolving threat landscape, adversaries exploit software vulnerabilities to launch sophisticated attacks, challenging traditional defenses. Although databases like CVE and NVD provide detailed technical information, they often lack links to attacker behaviors such as tactics and techniques, limiting effective threat interpretation and response. This work bridges this gap by connecting vulnerabilities with behavioral patterns from the MITRE ATT&CK framework. We construct a CVE-TTP Knowledge...
  </details>

- **2026-06-30** — Wenyi Zhang, Fanglong Yao, Youzhi Liu et al. — [AeroVerse-SatAgent: UAV-Satellite Collaborative Spatial Reasoning Inspired by the Dual Visual Pathway Theory of Cognitive Neuroscience](http://arxiv.org/abs/2606.31467v1)
  <details><summary>📄 Abstract</summary>
  With the rapid advancement of aerospace embodied intelligence, enabling Unmanned Aerial Vehicles (UAVs) to autonomously understand and reason about complex environments has become increasingly important. However, existing UAV-based spatial reasoning approaches face critical limitations: single-view perception renders them vulnerable to occlusions and perspective distortions, while most VLMs lack explicit geometric modeling, relying on semantic cues and yielding inconsistent reasoning under viewp...
  </details>

- **2026-06-30** — Sam J. Griffiths, Jamie Friel, Brian Vlastakis — [The limits of erasure-based postselection for quantum error mitigation](http://arxiv.org/abs/2606.31428v1)
  <details><summary>📄 Abstract</summary>
  In both classical and quantum error correction, heralded erasures are known to be easier to tolerate than unheralded general stochastic errors. Whilst an established benefit of loss-dominant quantum architectures such as photonic qubits, this fact has received renewed interest, with a pivot towards reconstructing other architectures to be erasure-dominant, such as dual-rail transmons. This work investigates exploiting these 'erasure qubits' in the near term by using postselection as a technique ...
  </details>

- **2026-06-30** — Yurui Zhao, Xiang Wang, Jingreng Lei et al. — [Dualformer: Efficient Feature Extractor for Complex-valued Blind Communication Signal Analysis](http://arxiv.org/abs/2606.31352v1)
  <details><summary>📄 Abstract</summary>
  Designing effective feature extractors is critical for blind signal analysis tasks such as automatic modulation recognition (AMR), signal scheme recognition (SSR), and \color{black} signal structure parsing (SSP). In this work, we propose dual-channel neural network (DualNN) that efficiently exploits complex-valued signals through parameter sharing across IQ channels. Unlike traditional real-valued or complex-valued models, DualNN is a groundbreaking framework which shares the network parameters...
  </details>

- **2026-06-30** — Jiaqi Li, Chaoren Wang, Xiaohai Tian et al. — [FlexiSLM: A Dynamic and Controllable Frame Rate Spoken Language Model](http://arxiv.org/abs/2606.31247v1)
  <details><summary>📄 Abstract</summary>
  Spoken language models (SLMs) extend LLMs to speech input and output. Existing SLMs represent speech at fixed frame rates (e.g., 25 or 12.5 Hz), ignoring the time-varying information density of speech and offering no flexibility to trade off quality for speed at inference time. Recent audio tokenizer research has proposed dynamic frame rate speech coding, which exploits this non-uniformity and enables two new capabilities: very low average frame rates and frame rate controllability. However, thi...
  </details>

- **2026-06-30** — Jiyong Boo, Byeongin Joung, Hyemin Yang et al. — [HSDF-Lane: Height-Aligned Signed Distance Field with Semantic Lane Prior for 3D Lane Detection](http://arxiv.org/abs/2606.31172v1)
  <details><summary>📄 Abstract</summary>
  Monocular 3D lane detection plays a critical role in autonomous driving, yet recovering reliable 3D geometry from a single image remains challenging due to inherent depth ambiguity. Prior methods project image features into Bird's-Eye-View (BEV) space under a flat-ground assumption, causing geometric distortion on real-world roads. Recent methods instead predict explicit height maps to capture non-planar surfaces, but still rely on sparse anchor-based regression and exploit the recovered geometr...
  </details>

- **2026-06-30** — Mohammed Latif Siddiq, Md. Nafiu Rahman, Joanna C. S. Santos — [An Empirical Study of Security Calibration in Large Language Models for Code](http://arxiv.org/abs/2606.31159v1)
  <details><summary>📄 Abstract</summary>
  Large Language Models (LLMs) are rapidly transforming software development, yet their use in security-critical contexts raises a key question: do models know when their generated code is insecure? This property, known as calibration, measures whether a model's confidence aligns with the true correctness of its outputs. We present the first large-scale empirical study of security calibration in LLM-generated code. We evaluate GPT-4o-mini, Gemini-2.0-Flash, and Qwen3-Coder-Next across multiple tem...
  </details>

- **2026-06-30** — Huaze Tang, Bill Zeng, Chao Wang et al. — [Revealing Safety-Critical Scenarios for UTM via Transformer](http://arxiv.org/abs/2606.31114v1)
  <details><summary>📄 Abstract</summary>
  Unmanned Traffic Management (UTM) systems are cloud-based platforms designed to manage and coordinate multiple aerial vehicles remotely. UTM systems are safety-critical which cannot tolerate failures like crash or collision. To reveal latent vulnerabilities, there are neither optimal failure-exposing demonstrations nor clear reward signals. Additionally, UTM's self-healing capability introduces the ``long-tail effect'' of critical failures. We propose framing UTM vulnerability discovery as a seq...
  </details>

- **2026-06-30** — Wencong Wu, Xiuwei Zhang, Hanlin Yin et al. — [Dual Sparse Aggregation Transformer for Multispectral Object Detection](http://arxiv.org/abs/2606.31015v1)
  <details><summary>📄 Abstract</summary>
  Transformer-based approaches have obtained excellent performance in multispectral object detection tasks due to their ability to model long-range dependencies and capture complementary information. However, previous transformer-based multispectral detection methods tend to use all available tokens for similarity calculation, which results in redundant information interaction from irrelevant areas, leading to degraded detection performance. To overcome this challenge, we propose a novel Dual Spar...
  </details>

- **2026-06-30** — Feibo Jiang, Li Dong, Lei Mao et al. — [SLM, LLM or Agentic AI? Toward Intelligent UAV-Enabled WPT Systems in Low-Altitude Economy Networks](http://arxiv.org/abs/2607.00255v1)
  <details><summary>📄 Abstract</summary>
  Unmanned Aerial Vehicles (UAVs) have become key enabling platforms for low-altitude economic networks, yet achieving efficient and adaptive optimization under resource-constrained and dynamic environments remains challenging. This paper investigates language models for UAV-enabled Wireless Power Transfer (WPT) systems. First, a lightweight Small Language Model (SLM)-based solution is developed using a pre-trained BERT backbone, enhanced UAV embeddings and contextual features, a geometry-aware pa...
  </details>

- **2026-06-30** — Siddhant Panpatil, Arth Singh, Mijin Koo et al. — [EgoSafetyBench: A Diagnostic Egocentric Video Benchmark for Evaluating Embodied VLMs as Runtime Safety Guards](http://arxiv.org/abs/2607.00218v1)
  <details><summary>📄 Abstract</summary>
  Vision-language models (VLMs) are now proposed as runtime safety guards for embodied agents in homes and factories. A deployable guard must catch genuinely unsafe situations while avoiding unnecessary intervention on routine but superficially alarming activity, a distinction that binary safety benchmarks obscure. We introduce EgoSafetyBench, an egocentric video benchmark of 1,200 robot-view scenarios annotated at half-second granularity, to evaluate VLMs as streaming guards across two tracks. Th...
  </details>

- **2026-06-30** — Willem van Osselaer, Jiarui Li, Meshal Alharbi et al. — [Dual-Informed Vertical Expansion for Multi-Objective Node Selection in Anytime Conflict-Based Search](http://arxiv.org/abs/2607.00156v1)
  <details><summary>📄 Abstract</summary>
  Conflict-Based Search (CBS) is a leading exact algorithm for Multi-Agent Path Finding (MAPF), but its high-level node-selection rule is usually treated as a fixed implementation detail. Standard best-first selection is strong for minimizing expanded nodes and closing the optimality certificate, yet it can maintain a large frontier, interrupt parent-child expansion sequences, and provide no feasible incumbent until termination. This paper studies node selection as a first-class design choice for ...
  </details>

- **2026-06-30** — Kaisen Yang, Zheng Jiang, Yuzhao Peng et al. — [Scalable Behaviour Cloning on Browser Using via Skill Distillation](http://arxiv.org/abs/2606.32014v1)
  <details><summary>📄 Abstract</summary>
  Internet users collectively perform an enormous range of skilled work through web browsers, from software development and document editing to search, forms, and enterprise workflows, making human browsing a highly scalable but under-exploited source of reusable browser skills. We argue that the bottleneck for browser agents is decision-making under incomplete information rather than low-level operation, and that the priors agents lack are already implicit in human interaction traces. We therefor...
  </details>


### 📂 defense
*防御与防护方法 / Defense & Protection Methods* — 59 papers

- **2026-07-02** — Haonan Huang — [Grounded autonomous research: a fault-tolerant LLM pipeline from corpus to manuscript in frontier computational physics](http://arxiv.org/abs/2607.02329v1)
  <details><summary>📄 Abstract</summary>
  Autonomous-research agents have demonstrated end-to-end LLM automation in machine-learning sandboxes where execution provides calibration. Frontier physical science differs categorically: physical reasoning underlies every methodology choice, toolchains are often underdocumented, and calibration must come from external literature anchors - which unscaffolded agents cite but do not confront, hallucinating plausible, unverifiable results from internal priors. We present a pipeline that runs end-to...
  </details>

- **2026-07-02** — Ravi Kant Sharma — [Criticality-Based Guard Rail Validation for AI Agent Decisions in Autonomous Telecom Networks](http://arxiv.org/abs/2607.02210v1)
  <details><summary>📄 Abstract</summary>
  The evolution toward fully autonomous telecommunications networks (Autonomous Network Levels 4-5) requires AI/ML agents to make real-time network decisions without human intervention. However, no standardized runtime mechanism exists to intercept and validate individual inference outputs before they trigger live network state changes, creating risks of erroneous autonomous decisions. This paper proposes the Guard Rail Validation (GRV) framework, a standardizable runtime architecture for intercep...
  </details>

- **2026-07-02** — William Hackett, Peter Garraghan — [Behind the Refusal: Determining Guardrail Activation via Behavioral Monitoring](http://arxiv.org/abs/2607.02121v1)
  <details><summary>📄 Abstract</summary>
  As Large Language Models (LLMs) and agentic systems become integrated into real-world applications, ensuring their safety and security is critical. Guardrail systems that detect and block malicious instructions sent to and from an LLM are an essential component of AI security. However, researchers conducting black-box adversarial emulation against production AI systems often struggle to determine whether a guardrail block or an LLM rejection has occurred. This distinction is important because th...
  </details>

- **2026-07-02** — Yunhao Feng, Ruixiao Lin, Ming Wen et al. — [Safety Testing LLM Agents at Scale: From Risk Discovery to Evidence-Grounded Verification](http://arxiv.org/abs/2607.01793v1)
  <details><summary>📄 Abstract</summary>
  LLM agents increasingly perform autonomous actions through external tools, leading to complex and evolving safety risks. However, existing safety testing targets expert-designed safety violations, and the corresponding outcomes are evaluated by hard-coded rules, making them costly to extend as agents evolve. To this end, we present Vera, an end-to-end automated safety testing framework that instantiates software engineering testing principles for non-deterministic agents through a three-stage, s...
  </details>

- **2026-07-02** — Juanwu Lu, Junyu Zhu, Ziran Wang — [Controllable Sim Agents with Behavior Latents](http://arxiv.org/abs/2607.02496v1)
  <details><summary>📄 Abstract</summary>
  Realistic traffic simulation requires agents that imitate logged behavior and can also be steered along interpretable axes. Such controllability enables engineers to isolate variables, reproduce specific edge cases, and test autonomous systems without real-world risk. We introduce Controllable Neural Variational Agents (CNeVA), a controllable simulated-agent framework that learns to infer a per-agent Gaussian behavior latent from per-channel discounted returns via a closed-form conjugate variati...
  </details>

- **2026-07-02** — Ziyao Wang, Maonan Wang, Yucheng He et al. — [Interpretation-Oriented Cloud Removal via Observation-Anchored Residual Flow with Geo-Contextual Alignment](http://arxiv.org/abs/2607.02471v1)
  <details><summary>📄 Abstract</summary>
  Cloud removal (CR) is essential for optical remote sensing, serving as a prerequisite for reliable downstream interpretation, such as semantic segmentation and change detection. However, existing CR approaches often prioritize visual realism while overlooking their impact on subsequent analytical tasks, leading to semantic drift and degraded downstream performance. To address this issue, we propose Geo-Anchored Cloud Removal (GACR), a unified framework that jointly ensures faithful reconstructio...
  </details>

- **2026-07-02** — Jinwei Hu, Yi Dong, Youcheng Sun et al. — [SkillFuzz: Fuzzing Skill Composition for Implicit Intents Discovery in Open Skill Marketplaces](http://arxiv.org/abs/2607.02345v1)
  <details><summary>📄 Abstract</summary>
  Large Language Model (LLM)-based agents increasingly automate software engineering tasks through reusable skills, natural-language instruction documents that guide planning and execution. Open skill marketplaces enable users to assemble agents by co-activating community-contributed skills, but marketplace operators typically audit skills in isolation. As a result, individually benign skills may interact to redirect an agent toward unintended objectives, which we term implicit intents. Detecting ...
  </details>

- **2026-07-02** — Lev Sorokin, Chen Yang, Ken E. Friedl et al. — [Search-based Testing of Vision Language Models for In-Car Scene Understanding](http://arxiv.org/abs/2607.02300v1)
  <details><summary>📄 Abstract</summary>
  In the automotive domain, in-car scene understanding (ISU) enables the detection of safety-critical events, such as driver distraction, and supports drivers or passengers by analyzing the in-car scene and adapting the environment (e.g., ambient lighting). The industry is increasingly exploring vision-language models (VLMs) to interpret camera-recorded in-car scenes and extract information for downstream reasoning tasks. However, VLMs may generate incomplete, erroneous, or misleading scene descri...
  </details>

- **2026-07-02** — Xiangchen Cheng, Yunwei Jiang, Jianwen Sun et al. — [AgenticSTS: A Bounded-Memory Testbed for Long-Horizon LLM Agents](http://arxiv.org/abs/2607.02255v1)
  <details><summary>📄 Abstract</summary>
  Memory for a long-horizon LLM agent is a contract about what each future decision is allowed to see. The simplest contract appends past observations, tool calls, and reflections to every prompt, which makes prior context easy to access but also turns it into a jumbled mixture in which the effect of any single memory component is hard to isolate. We introduce and instrument an alternative bounded contract: every decision is made from a fresh user message assembled by typed retrieval, with no raw ...
  </details>

- **2026-07-02** — Ismail Ismail Tijjani, Ahmad Abubakar Mustapaha, Sunusi Ibrahim Muhammad et al. — [Evaluating Vision-Language Models as a Zero-Shot Learning Alternative to You Only Look Once and Optical Character Recognition for Nigerian License Plate Recognition](http://arxiv.org/abs/2607.02025v1)
  <details><summary>📄 Abstract</summary>
  License Plate Recognition (LPR) systems are critical tools in traffic monitoring, security enforcement, and urban mobility management. Traditional LPR systems often rely on a multi-stage pipeline involving object detection using You Only Look Once (YOLO) and Optical Character Recognition (OCR), which suffer from limitations such as high resource demands, poor performance in unstructured environments, and the need for large annotated datasets. This study explores the potential of Vision-Language ...
  </details>

- **2026-07-02** — Zhiren Gong, Zihao Zeng, Chau Yuen et al. — [Conditional Co-Ablation: Recovering Self-Repair Backups in Transformer Circuits](http://arxiv.org/abs/2607.01940v1)
  <details><summary>📄 Abstract</summary>
  Mechanistic interpretability often relies on component-level interventions to discover how a model produces a behavior. This guides attribution, capability knockout, and model pruning downstream to operate by scoring each unit by the effect of ablation in isolation. Such first-order scoring is natural when component importance is additive, but becomes misleading when a transformer self-repairs: after a primary component is removed, a dormant backup can take over, muting the primary's measured ef...
  </details>

- **2026-07-02** — Yi Pan, Miao Pan, Qi Lu et al. — [VLA-Corrector: Lightweight Detect-and-Correct Inference for Adaptive Action Horizon](http://arxiv.org/abs/2607.01804v1)
  <details><summary>📄 Abstract</summary>
  Vision-Language-Action (VLA) foundation models have recently achieved strong progress in embodied intelligence. To reduce policy-call frequency while preserving temporal coherence, most generative policies adopt an action chunk mechanism, executing multiple future actions in an open-loop manner under a fixed action horizon. However, this "predict-then-blindly-execute" paradigm sacrifices closed-loop reactivity: in contact-rich physical interactions, even small local perturbations can rapidly amp...
  </details>

- **2026-07-02** — Jingtao Xu, Zizhuo Lin, Jianwen Sun et al. — [EAGLE-360: Embodied Active Global-to-Local Exploration in 360$^\circ$](http://arxiv.org/abs/2607.02479v1)
  <details><summary>📄 Abstract</summary>
  While Multimodal Large Language Models (MLLMs) have demonstrated exceptional capabilities in standard visual understanding, adapting them for active visual search in 360$^\circ$ panoramic environments exposes fundamental limitations. Specifically, standard MLLMs struggle to effectively model inherent panoramic properties, such as severe polar distortion and continuous cylindrical topologies, which significantly degrades target detection accuracy. Consequently, existing panoramic search methods a...
  </details>

- **2026-07-02** — Andrei-Marian Ungureanu, Stelian Spînu — [Real-Time Visual Intelligence on Low-Cost UAVs: A Modular Approach for Tracking, Scanning, and Navigation](http://arxiv.org/abs/2607.02298v1)
  <details><summary>📄 Abstract</summary>
  Autonomous drones are rapidly transforming modern warfare and civil applications alike. This paper presents the development of an integrated intelligent drone system designed to serve as a personal assistant. Leveraging the DJI Tello drone platform, we implemented a modular architecture that integrates three core artificial intelligence functionalities: facial detection, facial recognition, and depth estimation from monocular vision. A web-based interface enables seamless drone control and real-...
  </details>

- **2026-07-02** — Balint Turi, Archontis Politis, Parthasaarathy Sudarsanam et al. — [Speaker head orientation estimation with a single microphone array using phase spectrogram features](http://arxiv.org/abs/2607.02129v1)
  <details><summary>📄 Abstract</summary>
  Estimating a speaker's head orientation from audio can provide valuable information in smart environments, meetings, and driver monitoring. We propose a novel approach that leverages the phase component of the short-time Fourier transform from a single microphone array as input to a deep neural network combining convolutional, recurrent, and self-attention layers. Unlike prior methods that use physics-informed handcrafted features or raw waveform inputs, our approach enables robust learning from...
  </details>

- **2026-07-02** — Jiangdi Ru, Bing Li, Yage Huang et al. — [Traceable Fault Diagnosis for Battery Energy Storage Systems via Retrieval-Augmented Multi-Agent O&M Assistant](http://arxiv.org/abs/2607.01992v1)
  <details><summary>📄 Abstract</summary>
  Large-scale battery energy storage systems (BESSs) require O&M decisions that combine alarms, cell-level measurements, device topology, diagnostic tables, historical cases, and maintenance documents. Monitoring platforms can flag threshold violations, but they often cannot explain whether voltage inconsistency, resistance drift, short-circuit risk, capacity divergence, or thermal abnormality needs intervention. This digest presents a traceable BESS fault-diagnosis assistant that uses retrieval-a...
  </details>

- **2026-07-01** — Tong Xu, Xinzhe Cao, Zhihui Zhu et al. — [MolSafeEval: A Benchmark for Uncovering Safety Risks in AI-Generated Molecules](http://arxiv.org/abs/2607.00464v1)
  <details><summary>📄 Abstract</summary>
  Current molecular generation benchmarks emphasize task complexity, molecule novelty, and property alignment; they largely overlook a critical concern: the potential safety risks of AI-generated molecules. In practice, many generative models may produce molecules with toxic, reactive, or otherwise hazardous characteristics - posing hidden dangers that remain insufficiently addressed. To address this gap, we introduce MolSafeEval, a benchmark dedicated to evaluating and analyzing the safety risks ...
  </details>

- **2026-07-01** — Zijian Zhang, Rizhen Hu, Athanasios Glentis et al. — [Is One Layer Enough? Training A Single Transformer Layer Can Match Full-Parameter RL Training](http://arxiv.org/abs/2607.01232v1)
  <details><summary>📄 Abstract</summary>
  Reinforcement learning (RL) has become a central component of post-training large language models (LLMs), yet little is understood about how RL adaptation is distributed across transformer layers. Existing approaches typically update all model parameters uniformly, implicitly assuming that every layer contributes similarly to the gains obtained during RL post-training. In this work, we challenge this assumption through a systematic layer-wise study of RL training. Surprisingly, we find that trai...
  </details>

- **2026-07-01** — Arpita Nema, Hanwei Zhu, Xi Zhang et al. — [LongVQUBench: Benchmarking Long-Term Video Quality Understanding of Vision-Language Models](http://arxiv.org/abs/2607.01086v1)
  <details><summary>📄 Abstract</summary>
  The evaluation of long-term video quality understanding remains an open challenge for large vision-language models (LVLMs). Existing video quality benchmarks predominantly focus on short clips and isolated distortions, overlooking the temporal continuity, cumulative degradation, and reasoning complexity inherent in long-duration content. To address these limitations, we present LongVQUBench, a comprehensive benchmark for long-term video quality understanding. LongVQUBench contains over 1200 dive...
  </details>

- **2026-07-01** — Song-Lin Lv, Weiming Wu, Rui Zhu et al. — [Can Agents Generalize to the Open World? Unveiling the Fragility of Static Training in Tool Use](http://arxiv.org/abs/2607.01084v1)
  <details><summary>📄 Abstract</summary>
  While Large Language Model (LLM) agents demonstrate proficiency in static benchmarks, their deployment in real-world scenarios is hindered by the dynamic nature of user queries, tool sets, and interaction dynamics. To address this generalization gap, we formalize OpenAgent (Tool-Use Agent in Open-World), a problem setting characterized by distributional shifts across query, action, observation, and domain dimensions. To systematically diagnose its impact, we construct a controlled sandbox enviro...
  </details>

- **2026-07-01** — Jiaxu Leng, Jiankang Zheng, Mengjingcheng Mo et al. — [Linguistic Relative Policy Optimization for Video Anomaly Reasoning](http://arxiv.org/abs/2607.00654v1)
  <details><summary>📄 Abstract</summary>
  Video anomaly detection (VAD) with multimodal large language models has shown strong potential, yet most existing methods still depend on large-scale annotations or expert-designed priors, limiting their ability to acquire anomaly knowledge with as little human intervention as possible. To address this, we propose Linguistic Relative Policy Optimization (LRPO), which distills group-relative semantic advantages from multiple reasoning trajectories into a linguistically expressed anomaly experienc...
  </details>

- **2026-07-01** — Sara Candussio, Francesca Padovani, Daniel Scalena et al. — ["Don't Say It!": Constraints, Compliance, and Communication when Language Models Play Taboo](http://arxiv.org/abs/2607.00601v1)
  <details><summary>📄 Abstract</summary>
  The game of Taboo requires describing a target word without using a set of forbidden words, so that other players can guess it. This deceptively simple task combines strict lexical constraints with the need for communicatively effective descriptions, making it a compelling playground for examining how LLMs navigate competing demands at inference time. We evaluate two open-weight models under conditions that intervene at progressively deeper levels of the generative process, from prompting to gen...
  </details>

- **2026-07-01** — Jihyeok Jung, Jeewu Lee, Sanghyeop Kim et al. — [EgoGapBench: Benchmarking Egocentric Action Selection in Multi-Agent Scenes](http://arxiv.org/abs/2607.00547v1)
  <details><summary>📄 Abstract</summary>
  Existing egocentric benchmarks have primarily constructed the egocentric setting from first-person-view data, which makes it difficult to evaluate egocentric perspective itself in isolation. However, understanding first-person-view input and taking an egocentric perspective are separable abilities, especially when first-person body cues are absent or when other agents are present. To isolate egocentric perspective understanding, we introduce EgoGapBench, a diagnostic benchmark for measuring acti...
  </details>

- **2026-07-01** — Chenxun Deng, Zhongde Zhang, Ye Yuan et al. — [HieDG: A Hierarchical Discrete Geometry-Guided Framework for Multi-Animal Tracking](http://arxiv.org/abs/2607.00494v1)
  <details><summary>📄 Abstract</summary>
  Multi-animal tracking (MAT) is critical for wildlife monitoring and behavioral analysis, yet remains challenging due to uniform appearance, high density, and irregular motion. Existing methods typically follow heuristic- or query-based paradigms: the former relies on handcrafted geometric associations without end-to-end optimization, whereas the latter enables joint optimization but relies heavily on appearance embeddings. In such conditions, continuous geometric embeddings can be unstable, as s...
  </details>

- **2026-07-01** — Kaysarul Anas Apurba, Md Hasibul Hasan, Mohammed Ali et al. — [MalariAI: A Label-Resilient Decoupled Framework for Universal Cell Segmentation and Explainable Stage Classification in Dense Malaria Blood Smears](http://arxiv.org/abs/2607.00385v1)
  <details><summary>📄 Abstract</summary>
  Automated malaria diagnosis from blood smear microscopy is a critical challenge in global health AI; in resource-limited settings, the scarcity of expert microscopists remains the primary bottleneck to timely and accurate diagnosis. Three compounding failure modes prevent reliable clinical deployment of existing deep learning systems. First, end-to-end detectors treat unannotated cells as background during training, producing recall figures that are strongly influenced by annotation completeness...
  </details>

- **2026-07-01** — Bohan Li, Min Ye, Haochen Liu et al. — [Queue-Aware Graph Reinforcement Learning for UAV-ISAC-Assisted Maritime Data Collection](http://arxiv.org/abs/2607.00324v1)
  <details><summary>📄 Abstract</summary>
  This paper studies high-altitude platform (HAP)-assisted sparse cooperative integrated sensing and communication (ISAC) for UAV-enabled ocean monitoring. A fleet of rotary-wing UAVs senses drifting buoys, collects their monitoring data, and reports local posterior estimates to a HAP that performs fusion and sparse cooperation control. The model explicitly accounts for a spatially correlated sea-patch field, patch-aware buoy dynamics, RCS- and clutter-aware echo sensing, fused posterior Cramér-Ra...
  </details>

- **2026-07-01** — Zewen Liu — [EPC: A Standardized Protocol for Measuring Evaluator Preference Dynamics in LLM Agent Systems](http://arxiv.org/abs/2607.00297v1)
  <details><summary>📄 Abstract</summary>
  When LLM agents use evaluator feedback to adapt their behavior in closed loops, evaluator biases propagate through the agent's strategy distribution -- a phenomenon known as evaluator preference coupling. Prior work has documented coupling across multiple evaluator families and model versions, but the field lacks a standardized protocol that enables third-party researchers to (i) reproduce coupling measurements, (ii) compare results across evaluators and time points, and (iii) detect measurement...
  </details>

- **2026-07-01** — Hongkuan Zhou, Tristan Rehm, Nadeem Nazer et al. — [GenAU: Language-Grounded Industrial Anomaly Understanding with Vision-Language Models](http://arxiv.org/abs/2607.01049v1)
  <details><summary>📄 Abstract</summary>
  Industrial inspection requires more than binary anomaly detection: a practical system should determine whether an anomaly exists, localize the defective region, identify the defect type, and provide interpretable visual evidence. Existing CLIP-based methods detect and localize anomalies well but offer limited language-level defect understanding, while instruction-tuned vision-language models can describe defects but do not natively produce pixel-level masks. We introduce GenAU, a Generalist visi...
  </details>

- **2026-07-01** — Aryo Pradipta Gema, Beatrice Alex, Pasquale Minervini — [Logit-Contribution Scoring Identifies Non-Literal Retrieval Heads](http://arxiv.org/abs/2607.01002v1)
  <details><summary>📄 Abstract</summary>
  In long-context use, large language models frequently synthesize answers from the meaning of a relevant context span rather than literally copy-pasting them. Identifying which attention heads perform this synthesis matters for interpreting long-context model behavior. Yet existing detectors miss these heads by construction: they reward heads whose attended token matches the generated token, a literal-copy criterion that captures where a head reads but not what it writes through its output-value ...
  </details>

- **2026-07-01** — Chahan Vidal-Gorène, Nadi Tomeh, Victoria Khurshudyan — [Semantic-Guided Reading Order Reconstruction in Historical Armenian Newspapers with LLMs](http://arxiv.org/abs/2607.00596v1)
  <details><summary>📄 Abstract</summary>
  This paper addresses reading order reconstruction in historical Armenian newspapers, which combine complex layouts with limited language resources. We introduce a new annotated dataset of 66 pages and compare geometric heuristics, YOLO-based layout parsing, an end-to-end document model ECLAIR, and a hybrid method combining semantic zone detection with a generative LLM. Our hybrid method achieves the lowest error rates of all evaluated approaches, reducing ordering errors by up to 76% over the st...
  </details>

- **2026-07-01** — Zhongxiang Sun, Haolang Lu, Qiang Ma et al. — [NeuroCogMap Reveals Cognitive Organization of Large Language Models](http://arxiv.org/abs/2607.00397v1)
  <details><summary>📄 Abstract</summary>
  Understanding how complex cognitive functions are organized within artificial systems is central to interpreting large language models (LLMs) and relating them to biological cognition. Yet although LLMs exhibit broad cognitive-like behaviours, it remains unclear whether their internal representations form reproducible functional systems that explain behaviour, failure and links to human cognition. Here we present NeuroCogMap, a cognitive neuroscience-inspired framework that organizes internal fe...
  </details>

- **2026-07-01** — Louis Donaldson, Connor Walker, Koorosh Aslansefat et al. — [Bayesian Uncertainty Propagation for Agentic RAG Pipelines: A Proof-of-Concept Study on Multi-Hop Question Answering](http://arxiv.org/abs/2607.00972v1)
  <details><summary>📄 Abstract</summary>
  Trustworthy deployment of Agentic Retrieval-Augmented Generation (RAG) systems requires mechanisms for estimating when multi-stage reasoning pipelines may fail. This paper presents an uncertainty-aware Agentic Retrieval-Augmented Generation (RAG) framework in which planner, evaluator and generator stages produce uncertainty signals derived from semantic divergence and generator self-evaluation. These signals are propagated through a Bayesian Network (BN) to estimate system-level uncertainty and ...
  </details>

- **2026-07-01** — Srini Ramaswamy, Wang Miaosheng — [Managed Autonomy at Runtime: Gear-Based Safety and Governance for Single- and Multi-Agent Cyber-Physical Systems](http://arxiv.org/abs/2607.00334v1)
  <details><summary>📄 Abstract</summary>
  Autonomous agents, whether LLM-driven software agents or robotic physical agents, face a common class of failure modes when operating without continuous human oversight: safety violations from unverified actions, behavioral instability from unconstrained loops, and continuity loss from unhandled error states. We develop \system{}, a discrete-time control system that combines five execution gears (\Gobs{}, \Gsug{}, \Gplan{}, \Gexec{}, \Gint{}) with utility-gated dispatch and event-driven fallback...
  </details>

- **2026-06-30** — Kalina Borkiewicz, Jixian Li, Joshua A. Levine et al. — [May (A)I Beautify Your Visualization? Expert Judgments of Acceptable Aesthetic Alterations](http://arxiv.org/abs/2607.00239v1)
  <details><summary>📄 Abstract</summary>
  In 3D visualizations of natural phenomena, improving aesthetics can provide measurable benefits, but often involves transformations that affect how the data is perceived. As a growing range of tools - including AI-based methods - make visual design and modification more accessible, it is increasingly important to understand trade offs and concerns when making these changes. We conducted an expert survey (N=95) with visualization researchers, practitioners, and domain scientists, investigating re...
  </details>

- **2026-06-30** — Zaifeng Pan, Qianxu Wang, Zhengding Hu et al. — [SmoothAgent: Efficient Long-Horizon LLM-Based Agent Serving with Lookahead Context Engineering](http://arxiv.org/abs/2607.00151v1)
  <details><summary>📄 Abstract</summary>
  LLM-based agents execute multi-turn workflows with continuously growing contexts, where LLM calls are interleaved with tool invocations and environment feedback. To maintain model quality, modern agent frameworks rely on context engineering strategies such as offloading, reduction, and isolation to control the context length. However, these strategies introduce significant context transformation overhead: each transformation invalidates existing KV caches and triggers re-prefill, leading to incr...
  </details>

- **2026-06-30** — Gabrielle Kaili-May Liu, Avi Caciularu, Gal Yona et al. — [Reinforcement Learning with Metacognitive Feedback Elicits Faithful Uncertainty Expression in LLMs](http://arxiv.org/abs/2606.32032v1)
  <details><summary>📄 Abstract</summary>
  Metacognition is a critical component of intelligence that describes the ability to monitor and regulate one's own cognitive processes. Yet LLMs exhibit systemic deficiencies in key metacognitive faculties: they hallucinate with high confidence, fail to recognize knowledge boundaries, and misrepresent their internal uncertainty--undermining trustworthiness and reliability. Since monitoring task performance and adapting behavior accordingly are central to metacognition, we posit that models capab...
  </details>

- **2026-06-30** — Xinyu Zhao, Zhen Tan, Vaishnav Tadiparthi et al. — [Generative Skill Composition for LLM Agents](http://arxiv.org/abs/2606.32025v1)
  <details><summary>📄 Abstract</summary>
  Recent LLM agents benefit from skills for solving complex tasks. Skills encapsulate modular packages of procedural knowledge and instructions for performing specialized tasks, such as setting up a sandboxed environment, running a test suite, or refactoring a function across multiple files. As skill libraries grow and become reusable across tasks and domains, selecting an appropriate skill composition has emerged as a central bottleneck. Existing approaches fall into two categories. One exposes t...
  </details>

- **2026-06-30** — Nghia T. Nguyen, Lokman Bekit, Yasin Yilmaz — [SENSE-VAD: Sentient and Semantic Video Anomaly Detection for Autonomous Driving](http://arxiv.org/abs/2606.31875v1)
  <details><summary>📄 Abstract</summary>
  Autonomous vehicles (AVs) must navigate not only motion-based hazards but also socially complex situations whose danger is constituted by inter-agent relationships rather than movement statistics alone. A child running away from a guardian, a person being carried by another, or a pursuer chasing a pedestrian across a sidewalk are all anomalous in social context, yet none produces an obvious motion signal that current anomaly detectors are equipped to flag. We introduce SENSE-VAD, the first synth...
  </details>

- **2026-06-30** — Jiahui Fu, Zehao Huang, Han Li et al. — [Generative Lane Topology Reasoning via Autoregressive Model with Geometry Prior](http://arxiv.org/abs/2606.31814v1)
  <details><summary>📄 Abstract</summary>
  Lane topology reasoning aims to construct a lane graph from onboard sensor observations. Existing methods follow a detection and association paradigm that treats each lane instance independently, leading to geometric inconsistency at connected endpoints and incomplete graphs due to visual occlusions. To address these issues, we propose TopoGPT, a generative framework that learns the geometry prior from typical lane graph structures through autoregressive sequence modeling. Specifically, we const...
  </details>

- **2026-06-30** — Ke Wang, Xiaoyi Pan, Zhaoyu Gu et al. — [SAMBA: A Scatter-Guided Masked Bidirectional Mamba Foundation Model for SAR Target Recognition](http://arxiv.org/abs/2606.31668v1)
  <details><summary>📄 Abstract</summary>
  Synthetic aperture radar automatic target recognition (SAR ATR) is critical for Earth observation and defense, but its practical deployment is constrained by scarce annotated training data. Self-supervised pre-training alleviates this label bottleneck, yet prevailing Transformer architectures incur prohibitive quadratic computational complexity, and conventional universal masking neglects the unique electromagnetic scattering properties intrinsic to SAR imagery. To address these limitations, we ...
  </details>

- **2026-06-30** — Nikolai Röhrich, Julian Gleißner, Ahmed H. A. Ibrahim et al. — [Preserve the Hard, Regenerate the Rest: Uncertainty-Guided Synthetic Training Data Augmentation with Diffusion Models](http://arxiv.org/abs/2606.31603v1)
  <details><summary>📄 Abstract</summary>
  Semantic segmentation models struggle with data sparsity and rare or visually diverse regions, e.g., dense regions or small objects in aerial or autonomous mobility data. While synthetic augmentation is an appealing solution, directly generating new labeled data risks misalignment of labels and generated pixels. Existing solutions to this problem often rely on external models, or employ coarse heuristics such as indiscriminately augmenting all foreground objects or entire backgrounds, which wast...
  </details>

- **2026-06-30** — Jinliang Xu, Liping Ma — [A Large-Scale Empirical Evaluation of MMAO Under Fair-Budget Continuous and Discrete Benchmarks](http://arxiv.org/abs/2606.31584v1)
  <details><summary>📄 Abstract</summary>
  This paper evaluates the Metabolic Multi-Agent Optimizer (MMAO) under a stricter empirical protocol rather than reintroducing the framework itself. The study asks whether MMAO's closed-loop resource-allocation principle remains credible under broader, more standard, and more explicitly budget-controlled continuous and discrete benchmarks. The main completed matrix covers eight CEC2017 functions at 10D and 30D with 20 seeds each, and five TSPLIB instances with 20 seeds each, together with stronge...
  </details>

- **2026-06-30** — Outongyi Lv, Yanzhao Zheng, Yuanwei Zhang et al. — [Which Tokens Matter? Adaptive Token Selection for RLVR with the Relative Surprisal Index](http://arxiv.org/abs/2606.31575v1)
  <details><summary>📄 Abstract</summary>
  Reinforcement learning (RL) has become a powerful tool for propelling Large Language Models (LLMs) beyond imitation-based training towards more robust reasoning capabilities. Among existing approaches, RL with Verifiable Rewards (RLVR) has emerged as a pivotal paradigm for advancing LLM reasoning. Despite its empirical success, recent studies have offered different insights. One line of inquiry advocates prioritizing high-entropy token positions during training, while another perspective caution...
  </details>

- **2026-06-30** — Yizhe Liu, Shaolei Zhang, Ju Fan — [DA-Studio: An Agentic System for End-to-End Data Analysis](http://arxiv.org/abs/2606.31423v1)
  <details><summary>📄 Abstract</summary>
  Real-world data analysis is a multi-step process over heterogeneous inputs rather than merely producing a final answer. A practical system should autonomously organize multi-step workflows, execute generated code in a sandboxed and controllable environment, and remain inspectable through visible action traces and intermediate artifacts. Existing LLM-based analysis tools, however, often emphasize isolated subtasks, leaving limited support for complete execution-grounded workflows.   We present DA...
  </details>

- **2026-06-30** — Wanxia Cao, Chengzhen Duan, Pei Fu et al. — [Xiaomi-GUI-0 Technical Report](http://arxiv.org/abs/2606.31410v2)
  <details><summary>📄 Abstract</summary>
  Graphical user interface (GUI) agents build on vision-language models to complete user tasks end-to-end in real applications through interface actions such as tapping, swiping, text entry, and navigation. However, existing GUI agents are trained and evaluated largely on offline trajectories, simulated environments, and standardized benchmarks. These differ substantially from real applications in interface layout, interaction logic, and abnormal-state distribution, and cannot faithfully character...
  </details>

- **2026-06-30** — Hongyi Lin, Yang Liu, Jinhua Zhao et al. — [Rethinking Foundation Model Collaboration: Enhancing Specialized Models through Proxy Task Reasoning](http://arxiv.org/abs/2606.31157v1)
  <details><summary>📄 Abstract</summary>
  Foundation models are increasingly integrated into embodied intelligence systems, but directly assigning them structured prediction tasks requires precise geometric and numerical estimation, where specialized models often remain stronger. This capability mismatch raises a key question: should foundation models replace task-specific predictors, or should they collaborate through tasks better aligned with their strengths? We propose FAT, a foundation-model-augmented task-specific reasoning framewo...
  </details>

- **2026-06-30** — Duc Cao Dinh, Khai Le-Duc, Florent Draye et al. — [PruneGround: Plug-and-play Spatial Pruning for 3D Visual Grounding](http://arxiv.org/abs/2606.31148v1)
  <details><summary>📄 Abstract</summary>
  3D Visual Grounding (3DVG) aims to localize target objects in 3D scenes given natural language descriptions. Existing approaches typically perform reasoning over the entire scene, leading to ambiguous predictions and high computational cost, especially in cluttered environments. We observe that many referential expressions rely on local spatial context and often correspond to restricted spatial regions rather than the full scene. Motivated by this insight, we propose PruneGround, an effective pl...
  </details>

- **2026-06-30** — Hongyi Zhou, Yu Han, Qiechun Chen et al. — [Continuous-Variable Source-Independent Quantum Random Number Generation with General POVMs](http://arxiv.org/abs/2606.31027v1)
  <details><summary>📄 Abstract</summary>
  Continuous-variable source-independent quantum random number generators offer the highest generation rates among semi-device-independent protocols. In reality, the protocol design is limited due to permissible measurement configurations. In this work, we propose a rigorous security proof framework that accommodates general, infinite-dimensional positive-operator-valued measures. Building upon the numerical security proof framework, we evaluate the randomness lower bound by maximizing the eavesdr...
  </details>

- **2026-06-30** — Masen Bachleda, Peter Lalor — [Computer vision-based neural networks for radioisotope identification in urban environments](http://arxiv.org/abs/2607.00270v1)
  <details><summary>📄 Abstract</summary>
  Algorithm development for radioisotope identification in mobile urban search scenarios face significant challenges from non-uniform backgrounds, momentary source encounters, and severe class imbalance between rare threat signatures and background measurements. We present a machine learning-based approach to this problem that converts list-mode gamma-ray data into two-dimensional waterfall spectrograms and applies computer vision architectures to the resulting images. Rather than treating waterfa...
  </details>

- **2026-06-30** — Thinh Phan, Hao Vo, Khoa Vo et al. — [MVDGC: Joint 3D and 2D Multi-view Pedestrian Detection via Dual Geometric Constraints](http://arxiv.org/abs/2607.00273v1)
  <details><summary>📄 Abstract</summary>
  The core challenge in multi-view pedestrian detection (MVPD) lies in effective aggregation of visual features from different viewpoints for robust occlusion reasoning. Recent approaches have addressed this by first projecting image-view features onto a Bird's Eye View (BEV) map, where ground localization is then performed. Despite impressive performance, the perspective transformation induces severe distortion, causing spatial structure break and degrading the quality of object feature extractio...
  </details>

- **2026-06-30** — Shuwen Chai, Qiaosen Wang — [Sample Complexities of Estimating Gumbel--Max Watermark Proportions with and without Reduction to Pivotal Statistics](http://arxiv.org/abs/2607.00224v1)
  <details><summary>📄 Abstract</summary>
  Watermarking promises a statistical trace of large language model (LLM) use, but real documents, after editing or paraphrasing, rarely arrive as purely human-written or purely machine-generated. This motivates a quantitative question beyond detection: what proportion of a document is generated from a pre-specified watermarked LLM? We study this watermark proportion estimation problem under the Gumbel--max watermarking mechanism, treating the next-token prediction (NTP) distributions as unknown a...
  </details>

- **2026-06-30** — Thuan Bui, Duong Do, Tung Vu et al. — [SpikeLogBERT: Energy-Efficient Log Parsing Using Spiking Transformer Networks](http://arxiv.org/abs/2606.31781v1)
  <details><summary>📄 Abstract</summary>
  Log parsing is a fundamental step in automated log analysis, transforming raw system logs into structured event templates for downstream tasks such as anomaly detection and system monitoring. Existing log parsing methods range from rule-based and clustering-based approaches to neural models that learn semantic representations from log messages. However, neural approaches typically rely on dense matrix multiplications, which can result in high computational cost and energy consumption. This paper...
  </details>

- **2026-06-30** — Jonas Schäfer, Cezary Pilaszewicz, Gerhard Wunder — [Robust Text Watermarking for Large Language Models via Dual Semantic Embeddings](http://arxiv.org/abs/2606.31602v2)
  <details><summary>📄 Abstract</summary>
  This work presents Dual-Embedding Watermarking (DEW), a semantic watermarking scheme for large language models (LLMs) that leverages contextual and token-level embeddings to enhance robustness against paraphrasing and translation. DEW utilizes a signal-processing methodology, applying algebraic vector-space operations to token and context embeddings to derive a watermark signal that degrades gracefully under semantic shifts. The method obfuscates the watermark by projecting embedding vectors thr...
  </details>

- **2026-06-30** — David Pelosi, Fernando Barão, Bruna Bertucci et al. — [A new model for long-term forecasting of Galactic cosmic rays](http://arxiv.org/abs/2606.31433v1)
  <details><summary>📄 Abstract</summary>
  The modulation of galactic cosmic rays, driven by the evolution of the heliospheric magnetic field, strongly influences the intensity of cosmic rays reaching near-Earth space. Characterizing this process is crucial both for advancing our understanding of cosmic-ray transport and for assessing radiation exposure and related hazards in space environments. Here we present a newly developed forecasting framework built on a numerical description of charged particle transport in the heliosphere and it...
  </details>

- **2026-06-30** — Yuan Wang, Wanxing Chang, Songtao Jiang et al. — [AtomiMed: Hierarchical Atomic Fact-Checking for Universal Clinical-Aware Medical Report Evaluation](http://arxiv.org/abs/2606.31292v1)
  <details><summary>📄 Abstract</summary>
  Traditional metrics for Medical Report Generation (MRG) predominantly rely on surface-level n-gram overlap, which fails to capture clinical factual accuracy and often overlooks catastrophic diagnostic errors. We address this fundamental limitation by proposing \textbf{AtomiMed}, a universal, modality-agnostic evaluation framework that decomposes complex medical narratives into a standardized, multi-level hierarchy of Atomic Clinical Facts, encompassing Disease-level entities and Attribute-level ...
  </details>

- **2026-06-30** — Snehasis Banerjee, Ranjan Dasgupta — [LLM-Powered Interactive Robotic Action Synthesis from Multimodal Speech, Gestures, and Music](http://arxiv.org/abs/2606.31158v1)
  <details><summary>📄 Abstract</summary>
  The quest for intuitive and natural human-robot interaction (HRI) remains a significant challenge in robotics. Traditional methods often rely on rigid, pre-programmed commands that limit the robot's expressiveness and adaptability. This paper introduces a novel framework that leverages the reasoning capabilities of Large Language Models (LLMs) to synthesize complex robotic actions from a rich tapestry of multimodal human inputs: natural speech, hand gestures, and music/sound beats. Our system ar...
  </details>

- **2026-06-30** — Yucheng Chen, Jinjing Zhu, Yang Yu et al. — [Seeing Through Multiple Views: Parameter-Efficient Fine-Tuning via Selective Neurons for Consistent Radiology Report Generation](http://arxiv.org/abs/2606.31099v1)
  <details><summary>📄 Abstract</summary>
  Recent years have seen substantial advances in radiology report generation (RRG), yet existing approaches predominantly adopt direct feature fusion when handling multi-view X-ray images. Such approaches overlook the potential clinical inconsistencies and inaccuracies arising when a single model processes different views, adversely impacting performance and clinical reliability. To this end, we introduce View-PNDF (View-specific Pattern Neuron Detection and Fine-tuning), a parameter-efficient fra...
  </details>

- **2026-06-30** — Edward Y. Chang, Longling Geng, Emily J. Chang — [Mnemosyne: Agentic Transaction Processing for Validating and Repairing AI-generated Workflows](http://arxiv.org/abs/2607.00269v1)
  <details><summary>📄 Abstract</summary>
  LLMs, solvers, and agent teams increasingly generate workflow actions, repairs, and plans, but a generated action may be syntactically valid yet stale, infeasible, conflicting, or destructive of the evidence that triggered a repair. We introduce Agentic Transaction Processing (ATP), a transaction model that treats generated actions as untrusted proposals until they pass deterministic admission under a declared, executable constraint set C. The principle is two-sided: a proposal is not truth, and...
  </details>

- **2026-06-30** — Ziyan Wang, Tan Xiang, Peng Chen et al. — [Bridging Local Observation and Global Simulation in Closed-Loop Traffic Modeling](http://arxiv.org/abs/2606.31844v1)
  <details><summary>📄 Abstract</summary>
  A local-to-global context mismatch arises when autoregressive traffic simulators trained on ego-centric driving logs are deployed in globally observable closed-loop environments. In such logs, the ego vehicle has rich local observations, while surrounding agents are only partially observed due to perception limits and occlusions. As a result, simulators may learn incomplete context--action mappings that remain hidden in log-based training but emerge during closed-loop rollouts, leading to unreal...
  </details>


### 📂 alignment
*对齐与安全约束 / Alignment & Safety Constraints* — 67 papers

- **2026-07-02** — Dengyang Jiang, Mengmeng Wang, Harry Yang et al. — [From SRA to Self-Flow: Data Augmentation or Self-Supervision?](http://arxiv.org/abs/2607.02508v1)
  <details><summary>📄 Abstract</summary>
  Representation alignment has become an effective way to accelerate diffusion transformer training and improve generation quality. Recent self-alignment methods, such as SRA and Self-Flow, further remove the dependency on external pretrained encoders by constructing alignment within the diffusion model itself. However, the mechanism behind the improvement from SRA to Self-Flow, dual-time scheduling, remains under-examined: Self-Flow attributes its gain to interactions between tokens at different ...
  </details>

- **2026-07-02** — Arman Ghaffarizadeh, Danyal Mohaddes, Aliakbar Izadkhah et al. — [What LLM Agents Say When No One Is Watching: Social Structure and Latent Objective Emergence in Multi-Agent Debates](http://arxiv.org/abs/2607.02507v1)
  <details><summary>📄 Abstract</summary>
  LLM agents will increasingly act in socially structured settings where role, audience, and relational context can shape what is advantageous or costly to say. We study whether such social structure, without any explicit objective in the prompt, changes what an agent expresses publicly relative to an off-the-record (OTR) channel elicited under the same condition. We introduce a dual-channel debate framework in which agents produce public utterances that enter the shared history alongside OTR resp...
  </details>

- **2026-07-02** — Song Tang, Shuming Hu, Xincheng Shuai et al. — [Seek to Segment: Active Perception for Panoramic Referring Segmentation](http://arxiv.org/abs/2607.02497v1)
  <details><summary>📄 Abstract</summary>
  Existing referring segmentation models passively process static images captured from fixed perspectives, limiting their applicability in Embodied AI, where agents must perform active perception in the continuous 360$^\circ$ environments. To bridge this gap, we introduce a novel task: Active Panoramic Referring Segmentation (APRS). In this setting, an agent is required to adjust its viewing direction ($Δθ, Δφ$) to explore the 360$^\circ$ environment, seeking the object specified by a user instruc...
  </details>

- **2026-07-02** — Kaustubh Kapil, Kishor P. Upla — [Transformer Geometry Observatory TGO-II: Representational Similarity Observatory](http://arxiv.org/abs/2607.02386v1)
  <details><summary>📄 Abstract</summary>
  While Vision Transformers have achieved remarkable success across computer vision and language applications, the geometric evolution of their internal representations throughout training remains insufficiently understood. Existing analyses primarily focus on attention mechanisms and downstream performance, leaving the evolution of representation geometry largely unexplored. In this work, we present Transformer Geometry Observatory-II (TGO-II), a representation geometry analysis framework designe...
  </details>

- **2026-07-02** — Kim Zierahn, Cristina Cachero, Anna Korhonen et al. — [Personality Without Persons? A Psychometric Critique of Big Five Testing in Large Language Models](http://arxiv.org/abs/2607.02325v1)
  <details><summary>📄 Abstract</summary>
  Human personality inventories are increasingly used to characterize large language models (LLMs), compare systems, and inform downstream governance claims. Yet, these inventories were developed and validated for humans, and it remains unclear whether they apply to LLMs. We present a systematic psychometric evaluation of Big Five personality measurements in LLMs. We ask three research questions: Do Big Five inventories a) appropriately describe LLMs, b) capture inter-individual differences across...
  </details>

- **2026-07-02** — Zijun Li, Yimin Zhou, Jia Sun et al. — [DetailAnywhere: Fashion Detail Generation via Cross-Modal Feature Alignment Distillation](http://arxiv.org/abs/2607.02220v1)
  <details><summary>📄 Abstract</summary>
  Diffusion-based generative AI has achieved remarkable success in e-commerce applications such as virtual try-on, poster generation, and product background synthesis. However, when making online purchasing decisions for apparel, consumers also desire the freedom to examine specific detail regions of interest, such as collars, cuffs, and fabric textures, yet existing methods have not explicitly studied this setting. We therefore formalize a new, non-template task: Fashion Detail Generation with fo...
  </details>

- **2026-07-02** — Zhanglin Shangguan, Wei Xiao, Bo Yang et al. — [Reference-Governed Distributed Safe Gradient Flow for Safe Optimal Output Agreement of Multi-Agent Systems](http://arxiv.org/abs/2607.02192v1)
  <details><summary>📄 Abstract</summary>
  This paper studies safe optimal output agreement for nonlinear multi-agent systems with output safety constraints. Existing safe feedback optimization methods often implement gradient-flow dynamics directly through the plant input, which may require high-order control barrier functions (HOCBFs). The resulting derivative-chain design is tuning-sensitive and can introduce additional equilibrium conditions that alter the steady-state optimal solution. We propose a reference-governed two-layer archi...
  </details>

- **2026-07-02** — Susmit Agrawal, Matthias Bethge, Matthias Kümmerer — [DeepGaze3.5-VL: Modeling Scanpaths via Autoregressive Token Prediction](http://arxiv.org/abs/2607.02083v1)
  <details><summary>📄 Abstract</summary>
  Understanding human visual attention on a scene over time has applications in domains such as interface design and inferring cognitive states. Modeling visual scanpaths has historically relied on specialized architectures with hand-crafted priors. While these architectures can model fixation sequences, their rigid structural biases restrict easy extendability and flexible conditioning. For instance, integrating task-specific instructions or adapting to distinct viewer identities requires custom,...
  </details>

- **2026-07-02** — Wenda Wang, Yihan Tong, Yuwei Hu et al. — [MolSight: A Graph-Aware Vision-Language Model for Unified Chemical Image Understanding](http://arxiv.org/abs/2607.01982v1)
  <details><summary>📄 Abstract</summary>
  Using molecular large language models (LLMs) as a unified framework for understanding molecular structures and functions is emerging as a new trend in tasks such as molecular design and drug discovery. However, these models struggle to fully capture the visual representation of molecular structures, limiting their potential. While existing molecular vision-language models (VLMs) show promise, they still face challenges in structural alignment and lack the necessary topological modeling for accur...
  </details>

- **2026-07-02** — Jan Drchal — [Object Aligner: A Configurable JSON Schema Similarity Score for Graphs, Applied to LLM Prompt Optimization](http://arxiv.org/abs/2607.01972v1)
  <details><summary>📄 Abstract</summary>
  Large language models (LLMs) are often asked to produce JSON conforming to a fixed schema, powering information extraction, tool calling, agentic planning, and knowledge-graph construction. Measuring how closely an output matches a gold reference is essential yet surprisingly hard: exact match is brittle, text similarity ignores structure, and an LLM judge is expensive, opaque, and non-deterministic. We address this with Object Aligner (OA), an open-source Python library that scores two JSON obj...
  </details>

- **2026-07-02** — Jinxi Li, Tianyi Zhang, Yafei Yang et al. — [NeoMap: Training-free Novel-View Synthesis from Single Images and Videos](http://arxiv.org/abs/2607.01962v1)
  <details><summary>📄 Abstract</summary>
  We study the challenging problem of novel view video synthesis from single images or monocular videos. Existing methods, which operate under the assumption that pre-trained video models lack native novel view synthesis capability and enforce view alignment via camera conditioning, task-specific fine-tuning, or stepwise hard denoising guidance, often suffer from artifacts and compromised global scene consistency. In this paper, we introduce NeoMap, a novel training-free framework designed to loca...
  </details>

- **2026-07-02** — Bingcong Yan, Chunlei Li, Jingliang Hu et al. — [Towards Real-World Ultrasound Understanding: Large Vision-Language Models from Multi-Image Examinations with Long-Form Reports](http://arxiv.org/abs/2607.01908v1)
  <details><summary>📄 Abstract</summary>
  Large vision-language models (LVLMs) have achieved strong performance across many medical imaging tasks, yet their application to ultrasound remains limited due to its inherent complexity and variability. In this work, we revisit what is truly needed to enable real-world ultrasound understanding. Instead of introducing complex architectures or elaborate training strategies, we show that data scale and clinically faithful data alignment are the key factors. We construct a large-scale dataset of 1...
  </details>

- **2026-07-02** — Yidan Xu, Xiangmin Han, Rundong Xue et al. — [SABER: A Semantic-Aligned Brain Network Analysis Framework via Multi-scale Hypergraphs](http://arxiv.org/abs/2607.01901v1)
  <details><summary>📄 Abstract</summary>
  Effective brain disease diagnosis requires the synergy of brain connectivity patterns and high-level semantic knowledge. Existing methods, however, largely treat semantics from large language models (LLMs) as auxiliary features or supervision, limiting their direct role in decision-making and constraining classification stability and robustness. To overcome this, we propose a semantic-aligned brain network framework that actively integrates LLM-derived semantics into the prediction process. Spec...
  </details>

- **2026-07-02** — Fengchen He, Hao Xu, Dayang Zhao et al. — [FoundDP: Revisiting Weak Disparity Observability in Dual-Pixel Depth Estimation](http://arxiv.org/abs/2607.01900v1)
  <details><summary>📄 Abstract</summary>
  Dual-pixel (DP) imaging enables metric depth estimation from a single camera using sub-aperture disparity. However, the extremely small effective baseline limits disparity observability, leading to structural degradation and depth failure in textureless, low-contrast, or downsampled regions. Existing DP-based methods rely primarily on local disparity cues and therefore become unreliable when disparity signals are weak or ambiguous. To address this limitation, we propose \emph{FoundDP}, a unified...
  </details>

- **2026-07-02** — Qing Yu, Kent Fujiwara — [InterCMDM: Block-Causal Diffusion for Autoregressive Human Interaction Generation](http://arxiv.org/abs/2607.01743v1)
  <details><summary>📄 Abstract</summary>
  Text-conditioned human interaction generation must capture both long-range temporal causality within each individual and tightly coupled coordination between partners. Existing interaction diffusion models typically denoise full sequences using bidirectional attention, which obscures causality and hinders streaming and long-horizon generation. Autoregressive alternatives enforce causality but often suffer from temporal drift, leading to coordination degradation and unstable interaction dynamics ...
  </details>

- **2026-07-02** — Hexian Ni, Tao Lu, Yinghao Cai — [CoRe: Combined Rewards with Vision-Language Model Feedback for Preference-Aligned Reinforcement Learning](http://arxiv.org/abs/2607.01721v1)
  <details><summary>📄 Abstract</summary>
  Reward design remains a central challenge in reinforcement learning (RL). Hand-crafted rewards are often difficult to specify and may lead to suboptimal policies, while learned rewards from preferences can suffer from inefficiency and unstable training. Inspired by the dual nature of human learning explored in cognitive science, we decompose rewards into two complementary components: Formal Rewards (FR), explicitly designed based on task knowledge, and Residual Rewards (RR), learned from observa...
  </details>

- **2026-07-02** — Xudong Wu, Jian Qian, Pangpang Liu et al. — [Distributionally Robust Listwise Preference Optimization](http://arxiv.org/abs/2607.01715v1)
  <details><summary>📄 Abstract</summary>
  Existing robust preference optimization for language-model alignment mainly studies pairwise supervision and places robustness at the dataset, prompt, or preference-pair level. We instead study listwise preference optimization under ranking-label uncertainty: given a prompt and a candidate list, the observed ranking over that list may be ambiguous due to annotator inconsistency, near-ties, lossy rankwise feedback, or reward-model noise. We propose a pointwise total-variation robust Plackett--Luc...
  </details>

- **2026-07-02** — Xuanhua He, Jiaxin Xie, Mingzhe Zheng et al. — [ICDepth: Taming Video Diffusion Models for Video Depth Estimation via In-Context Conditioning](http://arxiv.org/abs/2607.01677v1)
  <details><summary>📄 Abstract</summary>
  Monocular video depth estimation requires temporal consistency, geometric accuracy, and generalization across diverse scenarios, yet existing methods struggle to achieve all three simultaneously. Discriminative models excel at per-frame accuracy but suffer from temporal drift due to limited context windows, while generative methods improve consistency and generalization at the cost of extensive training data (10M+ samples) and lack of geometric precision. In response to these issues, we introduc...
  </details>

- **2026-07-02** — Chen Zhao, Jiajun Ma, Qilong Huang et al. — [Temporal and Cross-Modal Alignment for Enhanced Audiovisual Video Captioning](http://arxiv.org/abs/2607.01667v1)
  <details><summary>📄 Abstract</summary>
  While Multimodal Large Language Models (MLLMs) have advanced video understanding, achieving precise temporal and cross-modal alignment in audiovisual video captioning remains a formidable challenge. Most existing approaches suffer from modality detachment and temporal incoherence, failing to accurately bind auditory events to visual entities or capture complex causal dynamics. To address these deficiencies, we propose TCA-Captioner, a framework specifically engineered to enhance Temporal and Cro...
  </details>

- **2026-07-02** — Yuan Yuan — [The Dual Nature of LLM Persona: Aggregated Tendencies and Frame-Dependent Geometry](http://arxiv.org/abs/2607.02368v1)
  <details><summary>📄 Abstract</summary>
  Evaluations of LLM personas via psychometric questionnaires typically rely on aggregate scores, discarding within-instance correlation structure. We test whether this geometric structure is intrinsic or frame-dependent. Constructing within-instance correlation matrices from IPIP-50 responses, we analyze geometry on SPD manifolds under manipulated question orderings in GPT-4o simulating American and Chinese-American personas. We find that persona expression comprises two dissociable components: a...
  </details>

- **2026-07-01** — William Philipp, Finn Fassbender, Thorsten Langer et al. — [Clinician-Level Agreement Without Clinical Caution: LLM Evaluator Limits in Medical AI Benchmarking](http://arxiv.org/abs/2607.01103v1)
  <details><summary>📄 Abstract</summary>
  Open-response evaluation provides stronger clinical validity than multiple-choice benchmarks but creates a scoring bottleneck that motivates automated LLM-asa-Judge approaches. Whether such evaluators replicate clinical calibration and caution, however, remains untested. We introduce MedQADE, the first standardised open-response clinical benchmark for German, a major clinical language lacking native evaluation infrastructure, comprising 3,800 items annotated by ten practising physicians and nine...
  </details>

- **2026-07-01** — Soosung Kim, Minjae Park, Eui-Young Chung et al. — [GSRQ: Gain-Shape Residual Quantization for Sub-1-bit KV Cache](http://arxiv.org/abs/2607.01065v1)
  <details><summary>📄 Abstract</summary>
  The deployment of Large Language Models (LLMs) with extended context windows is increasingly constrained by the linear growth of Key-Value (KV) cache memory. Vector Quantization (VQ), particularly Residual Quantization (RQ), is a promising approach for pushing KV cache storage toward the sub-1-bit regime by progressively encoding residuals with small codebooks. However, most VQ methods still rely on standard $\ell_2$ $K$-means as the core codebook-learning primitive. We identify a subtle high-di...
  </details>

- **2026-07-01** — Ali Vardasbi, Gustavo Penha, Enrico Palumbo et al. — [As It Was: Aligning LLM Search Evaluation with Historical User Preferences](http://arxiv.org/abs/2607.01040v1)
  <details><summary>📄 Abstract</summary>
  Large-scale search systems evolve faster than human quality assurance can scale, especially for long-tail intents and multilingual queries. LLM-as-a-judge approaches provide a scalable alternative for evaluating the relevance of search engine result pages (SERPs), but judgments based solely on semantic similarity or world knowledge can drift from actual user preferences, particularly for ambiguous queries. We introduce a behavior-grounded LLM judge that augments each SERP item with a lightweight...
  </details>

- **2026-07-01** — Subhadeep Pal, Shashwat Sourav, Tirthankar Ghosal et al. — [Graph-Native Reinforcement Learning Enables Traceable Scientific Hypothesis Generation through Conceptual Recombination](http://arxiv.org/abs/2607.00924v1)
  <details><summary>📄 Abstract</summary>
  Accelerating materials discovery requires AI systems that can generate scientifically valid hypotheses through multi-step, domain-grounded reasoning. Standard large language models often produce fluent but weakly traceable responses to open-ended materials design problems, making it difficult to determine whether final answers are supported by coherent intermediate reasoning. We develop Graph-PRefLexOR, a family of graph-native reasoning models fine-tuned with Group Relative Policy Optimization ...
  </details>

- **2026-07-01** — Fei Wang, Chao Xue, Taoran Liu et al. — [Beyond Activation Alignment:The Alignment-Diversity Tradeoff in Task-Aware LLM Quantization](http://arxiv.org/abs/2607.00908v1)
  <details><summary>📄 Abstract</summary>
  Mixed-precision quantization (MPQ) has become a key technique for deploying large language models under stringent memory and compute constraints. We first identify a phenomenon that we term the Perplexity Illusion: layers ranked as important by perplexity-based sensitivity show little rank correlation with those that are most influential for complex reasoning performance, with Kendall $τ\approx 0$ in our analysis. We further reveal an Alignment-Diversity Tradeoff: using only target-task calibrat...
  </details>

- **2026-07-01** — Zhihan Zeng, Amir Hussain, Yue Xiu et al. — [Geometry-Aware Cross-Height Channel Knowledge Map Prediction for UAV-Assisted Communications With Uncertainty-Guided 3D Sensing](http://arxiv.org/abs/2607.00887v1)
  <details><summary>📄 Abstract</summary>
  Low-altitude Unmanned Aerial Vehicles (UAVs) often need to infer channel knowledge across a range of heights from only sparse observations collected at a few altitude layers. To address this challenge, this paper studies height-conditioned cross-height channel knowledge map (CKM) prediction for UAV-assisted communications in geometry-rich urban environments. We develop a geometry-aware conditional prediction framework that combines urban scene priors, sparse multi-altitude observations, and targ...
  </details>

- **2026-07-01** — Ruixin Li, Jin Liu, Yuling Shi et al. — [Mirror-Fusion Attention for Reflection-Aware Self-Supervised Representation Learning](http://arxiv.org/abs/2607.00850v1)
  <details><summary>📄 Abstract</summary>
  Most self-supervised learning (SSL) methods encourage invariance across augmentations, but strict flip invariance can suppress informative left--right correspondences in approximately bilateral data such as medical images and human faces. We propose Mirror-Fusion-Augmented Self-Supervised Learning (MFASSL), a Vision Transformer framework that injects a soft reflection prior into standard SSL without redesigning the backbone. MFASSL constructs mirror-paired views aligned to an estimated symmetry ...
  </details>

- **2026-07-01** — Xianru Chen, Yukai Huang, Mingxiang Chen et al. — [MSQA: A Natively Sourced Multilingual and Multicultural SimpleQA Benchmark](http://arxiv.org/abs/2607.00724v1)
  <details><summary>📄 Abstract</summary>
  Multilingual fluency often invites a stronger assumption: a model that can speak a user's language must also understand the culture encoded by that language. We call this the Illusion of Cultural Alignment. To test this assumption directly, we introduce MSQA, a benchmark of 1,064 natively sourced questions across 11 language groups, five cultural dimensions, and three difficulty tiers. Unlike translated benchmarks, MSQA targets locally grounded knowledge and reduces shortcuts from English-centri...
  </details>

- **2026-07-01** — Ronghan Chen, Yandan Yang, Zuojin Tang et al. — [ABot-M0.5: Unified Mobility-and-Manipulation World Action Model](http://arxiv.org/abs/2607.00678v1)
  <details><summary>📄 Abstract</summary>
  Mobile manipulation is a key capability for general-purpose robots, yet remains challenging for current embodied learning methods. VLA policies are typically reactive and lack explicit world modeling, while existing World Action Models (WAMs) are still poorly aligned with the structure of mobile manipulation: they operate on coarse video chunks, model entangled navigation-manipulation actions, and train inverse dynamics under supervision that does not match autoregressive inference. As a result,...
  </details>

- **2026-07-01** — Tejas Pradeep Shirodkar — [Measuring Dead Directions: Decomposing and Classifying Singular Structure off Canonical Alignment](http://arxiv.org/abs/2607.00603v1)
  <details><summary>📄 Abstract</summary>
  We give a descent-free, alignment-free measurement of singular structure on trained networks. At a single frozen checkpoint the read recovers the order $k$ of each dead direction from the directional-Fisher rate, the master invariant from which the per-direction learning coefficient $1/(2k)$ follows exactly, in whatever basis the optimizer left. The same read classifies each direction, separating a genuine singularity, whose order the architecture fixes, from a flat gauge symmetry; the direction...
  </details>

- **2026-07-01** — Mattia D'Urso, Christian Sormann, Mattia Rossi et al. — [EPO: Boosting 3D Foundation Models with Edge-based Pose Optimization](http://arxiv.org/abs/2607.00579v1)
  <details><summary>📄 Abstract</summary>
  We introduce \textbf{Edge-based Pose Optimization (EPO)}, a trackless geometric optimization framework specifically designed to boost the Structure-from-Motion reconstructions generated by 3D Foundation Models. These models achieve rapid inference by bypassing the time-consuming feature extraction and matching stages of traditional pipelines, where explicit correspondences between each 3D point and multiple images, referred to as tracks, are established. However, their geometric accuracy current...
  </details>

- **2026-07-01** — Zijian Dong, Yi Lin, Ji Fang et al. — [BrainFIBRE: A Foundation Model via Information Decomposition for Brain Microstructure](http://arxiv.org/abs/2607.00573v1)
  <details><summary>📄 Abstract</summary>
  Diffusion MRI probes brain microstructure with particular sensitivity to early cerebrovascular and neurodegenerative changes. Neurite Orientation Dispersion and Density Imaging (NODDI) decomposes the diffusion signal into three biophysically interpretable maps: neurite density index (NDI), orientation dispersion index (ODI), and free water fraction (FWF), capturing neurite packing, fiber coherence, and extracellular fluid. These 3D maps offer a rich substrate for transferable microstructural rep...
  </details>

- **2026-07-01** — Yuchen Zhang, Luanyuan Dai, Yiwei Wang et al. — [Robust 3D Alignment of Generative Reconstructions via Partial Monocular Observations](http://arxiv.org/abs/2607.00498v1)
  <details><summary>📄 Abstract</summary>
  Aligning generative 3D reconstructions with partial monocular observations is a critical but under-explored challenge in computer vision. This task is inherently ill-posed due to severe asymmetries between noisy, sparse monocular inputs and dense generative priors, whose scale ambiguity and geometric hallucinations, combined with the lack of initial overlap, render traditional registration pipelines ineffective. To resolve these issues, we propose a training-free and interpretable geometric alig...
  </details>

- **2026-07-01** — Anindya Sarkar, Nasik Muhammad Nafi, Isaac Lyngaas et al. — [PAPA: Online Personalized Active Preference Alignment](http://arxiv.org/abs/2607.00486v1)
  <details><summary>📄 Abstract</summary>
  Diffusion models are highly effective at modeling complex data distributions, including images and text. However, in applications like personalized recommender systems, the objective often shifts to modeling specific regions of the distribution that maximize user preferences-initially unknown but gradually uncovered through interactive feedback. This can naturally be framed as a reinforcement learning problem, where the goal is to fine-tune a diffusion model to maximize a reward function based o...
  </details>

- **2026-07-01** — Ji Ha Jang, Hayeon Kim, Chulwon Lee et al. — [HyFL-CLIP: Hyperbolic Fine-Tuning of CLIP for Robust Long-Context Understanding](http://arxiv.org/abs/2607.00428v1)
  <details><summary>📄 Abstract</summary>
  CLIP (Contrastive Language-Image Pre-training) has become a de facto paradigm for image-text alignment, but it struggles with long-context descriptions (>77 tokens) due to absolute positional encoding and pretraining on short captions. In long contexts, sentences are often reordered, summarized, or partially omitted. Although prior works extend CLIP with longer positional encodings, they often suffer from degraded image-text alignment under such text perturbations. We attribute this limitation t...
  </details>

- **2026-07-01** — Jaeho Han, Jisoo Yang, Hyeondong Woo et al. — [Selective Test-Time Debiasing for CLIP via Reward Gating](http://arxiv.org/abs/2607.00423v1)
  <details><summary>📄 Abstract</summary>
  Vision language models (VLMs) demonstrate strong zero-shot performance, but often perpetuate social stereotypes in person-centric queries, yielding skewed demographic distributions. Current debiasing methods apply uniform bias corrections across all input queries regardless of their bias sensitivity, creating a fundamental fairness--utility trade-off. Strong debiasing distorts semantically meaningful information in bias-insensitive queries, while weak debiasing fails to mitigate stereotypes in b...
  </details>

- **2026-07-01** — Saad Wazir, Patrick Dominique Vibild, Dinh Phu Tran et al. — [MedCAGD: Context-Aware Gated Decoder for Efficient Medical Image Segmentation](http://arxiv.org/abs/2607.00409v1)
  <details><summary>📄 Abstract</summary>
  Medical image segmentation relies on the ability of encoder-decoder architectures to translate rich feature representations into accurate pixel-level predictions under challenging conditions such as low contrast, structural ambiguity, and scale variability. While recent advances in large-scale pretraining and transformer-based encoders have substantially improved feature extraction, segmentation accuracy remains constrained by decoder design, particularly in terms of cross-scale alignment, conte...
  </details>

- **2026-07-01** — Xingran Guo, Tiaojie Xiao, Jie Liu et al. — [Holographic Quantum Transformer: A Generalist Neuro-Symbolic Architecture for Solving Frustrated Systems via Generative Attention](http://arxiv.org/abs/2607.00398v1)
  <details><summary>📄 Abstract</summary>
  Simulating two-dimensional frustrated quantum matter is a grand challenge due to the sign problem and exponential Hilbert space complexity. In this work, we introduce the Holographic Quantum Transformer (HQT), a physics-inspired generative architecture that leverages global self-attention to resolve non-local entanglement patterns. We validate HQT on the square lattice $J_1-J_2$ Heisenberg model. On the heavily frustrated $8 \times 8$ lattice at the quantum critical point ($J_2=0.5$), HQT reache...
  </details>

- **2026-07-01** — Kele Xu, Yulu Fang, Boda Zhou et al. — [From Objectives to Applications: Aligning Architectural Biases in Audio Self-Supervised Learning](http://arxiv.org/abs/2607.00387v1)
  <details><summary>📄 Abstract</summary>
  This paper examines audio self-supervised learning (SSL) through the alignment between pretraining objectives, architectural inductive biases, and downstream applications. Rather than treating SSL methods as a chronological sequence of pretext tasks or model families, we ask how different supervisory signals shape the representations that models are expected to learn. The discussion is organized around five paradigms: auxiliary tasks, contrastive learning, generative reconstruction, discrete tok...
  </details>

- **2026-07-01** — Hengyu Fu, Tianyu Guo, Zixuan Wang et al. — [DiscoLoop: Looping Discrete Embeddings and Continuous Hidden States for Multi-hop Reasoning](http://arxiv.org/abs/2607.00341v1)
  <details><summary>📄 Abstract</summary>
  Large language models achieve strong performance on many reasoning tasks when allowed to externalize intermediate steps as Chain-of-Thought (CoT). However, many questions require the model to internalize the multi-step reasoning within a single forward pass before generating the answer. We study this challenge through two-hop reasoning, a representative task where the model must compose multiple pieces of parametric knowledge within a single forward pass. Standard non-recurrent Transformers suff...
  </details>

- **2026-07-01** — Prabal Gupta — [A Text-Steerable Instrument for Sketching Procedural Soundscapes via Language Models](http://arxiv.org/abs/2607.00309v1)
  <details><summary>📄 Abstract</summary>
  We present a real-time musical interface that converts natural-language scene descriptions into evolving procedural soundscapes. A performer types a prompt such as "warm jazz cafe at midnight" and steers it through direct parameter adjustments - stepping brightness down, switching a rhythm style - each producing a predictable, audible shift without re-prompting. Where GPU-bound text-to-audio systems synthesize monolithic waveforms, our instrument generates human-readable configurations over a ca...
  </details>

- **2026-07-01** — Yoonhyung Park, Minji Kim, Sungwon Moon et al. — [Wake up for Touch! Mask-isolated Tactile Alignment Learning in MLLMs](http://arxiv.org/abs/2607.00302v1)
  <details><summary>📄 Abstract</summary>
  Touch supplies the physical grounding needed to perceive intrinsic material properties, such as friction and compliance, that vision alone often cannot resolve. Recent efforts for equipping multimodal LLMs with this tactile sense, however, expose a zero-sum trade-off: the limited parameter budget of compact models forces a choice between acquiring the new sensory modality and preserving the established vision-language reasoning. We present Splash, a mask-isolated tactile alignment learning frame...
  </details>

- **2026-07-01** — Jingwei Song, Haofeng Xu, Jie Xiao et al. — [Staleness-Learning Rate Scaling Laws for Asynchronous RLHF](http://arxiv.org/abs/2607.01083v1)
  <details><summary>📄 Abstract</summary>
  High-throughput RLHF systems often decouple rollout generation from policy optimization, leading to the use of stale rollouts during learner updates. In this work, we study the effect of such staleness in asynchronous GRPO. We make the behavior policy explicit in the GRPO surrogate objective and distinguish between the surrogate-gradient mapping used by the learner and the true total derivative of a distribution-dependent population objective. Under assumptions of local boundedness, distribution...
  </details>

- **2026-07-01** — James Grover, Emily A. Hewson, Andrew Phair et al. — [Closed-loop coupling of personalised and foundation models for real-time treatment guidance with MRI](http://arxiv.org/abs/2607.00500v1)
  <details><summary>📄 Abstract</summary>
  Image-guided therapies, including radiotherapy, biopsy and deep brain stimulation, rely on real-time targeting of anatomical structures. However, in the presence of motion, imaging latencies create a temporal misalignment between observed and true anatomy, compromising treatment accuracy. Artificial intelligence-based frameworks have increasingly been presented to close this latency gap, but leading personalised models can fail due to a lack of stable anatomical grounding. Foundation models can ...
  </details>

- **2026-07-01** — Yangfan Hu, Xuhan Tong, Haoyue Bai et al. — [Understanding Why Language Models Hallucinate: Testing Reasoning Against Priors](http://arxiv.org/abs/2607.00447v1)
  <details><summary>📄 Abstract</summary>
  Large language models often produce hallucinated answers that violate prompt-level constraints. A key diagnostic question is whether these failures reflect missing knowledge, or whether the model has the relevant information but follows the wrong inference path. We study this phenomenon as inference misalignment: a mismatch between the answer supported by the prompt and the answer favored by statistically salient latent associations. We formalize this view with a latent key-task model, in which ...
  </details>

- **2026-07-01** — Yiming Zhang, Vikram Krishnamurthy — [Emergence of Preferential Attachment and Glass-Ceiling Effects in Autonomous Networks of LLMs](http://arxiv.org/abs/2607.01148v1)
  <details><summary>📄 Abstract</summary>
  We investigate the emergence of structural disparities in networks of collaborating large language model (LLM) agents. When LLM agents autonomously choose collaborators, the resulting communication network exhibits preferential-attachment dynamics: agents that are already prominent become increasingly likely to attract additional connections. In some cases, weaker LLM agents (agents with smaller base model or older version) can disproportionately occupy central and influential network positions ...
  </details>

- **2026-07-01** — Mengjingcheng Mo, Jiaxu Leng, Xinbo Gao — [Learning to Watch: Active Video Anomaly Understanding via Interleaved Policy Optimization](http://arxiv.org/abs/2607.00622v1)
  <details><summary>📄 Abstract</summary>
  Video anomaly understanding (VAU) relies on sparse, context-dependent cues. However, existing passive paradigms suffer from observational aliasing, where static sampling fails to disambiguate semantically distinct events. To overcome this, we propose $Anom\text{-}π$, a closed-loop framework that reconceptualizes video understanding as an active sequential decision-making process within a dynamic environment. Inspired by human video-reviewing behavior, this framework unifies internal cognitive re...
  </details>

- **2026-06-30** — Jack Le, Anh H. N. Nguyen, Tien N. Nguyen — [Do Machines Struggle Where Humans Do? LLM and Human Comprehension of Obfuscated Code](http://arxiv.org/abs/2606.31725v1)
  <details><summary>📄 Abstract</summary>
  While code obfuscation impairs human code comprehension, it remains unclear if large language models share these failure modes. Building directly on a recent human study of program comprehension under code obfuscation, we evaluate whether large language models share the failure modes that obfuscation induces in human programmers. Evaluating several LLMs with five obfuscation tiers using the Block Model, we localize comprehension failures at the atom, block, relational, and macro levels. We find ...
  </details>

- **2026-06-30** — John Sweeney — [Signed-Permutation Coordinate Transport for RMSNorm Transformers](http://arxiv.org/abs/2606.31963v1)
  <details><summary>📄 Abstract</summary>
  Modern LLM workflows move coordinate-indexed objects across checkpoints: steering vectors, sparse autoencoders, top-$k$ neuron sets, attribution lists, and merge alignments. This is only well posed after fixing the model's residual-stream gauge, which we show is architecture-dependent: LayerNorm residual charts have permutation gauge $S_d$ (up to a global sign flip), while RMSNorm charts with generic per-channel gain have signed-permutation gauge $B_d = S_d \ltimes \{\pm 1\}^d$. Permutation-only...
  </details>

- **2026-06-30** — Xianda Zheng, Huan Gao, Meng-Fen Chiang et al. — [Evo-PI: Aligning Medical Reasoning via Evolving Principle-Guided Supervision](http://arxiv.org/abs/2606.31800v1)
  <details><summary>📄 Abstract</summary>
  Despite recent progress, the reasoning capabilities of large multimodal language models (MLLMs) remain fundamentally constrained by static supervision, where fixed prompts, rules, or reward models provide non-adaptive guidance throughout training. Such static signals are often sufficient to enforce output formats, but fail to shape the underlying reasoning process, leading to brittle generalization and performance saturation in complex decision-making tasks. We propose Evo-PI, a principle-centri...
  </details>

- **2026-06-30** — Yaozhi Zheng, Yilei Jiang, Manyuan Zhang et al. — [UniCoder: Unified Visual-to-Code Generation via Symbolic Rewards and Reference-Guided Code Optimization](http://arxiv.org/abs/2606.31732v1)
  <details><summary>📄 Abstract</summary>
  Visual-to-Code generation, which transforms scientific plots, vector graphics, and webpages into executable scripts, demands a level of pixel-precise alignment that standard Multimodal Large Language Models (MLLMs) fail to achieve through Supervised Fine-Tuning (SFT) alone. While Reinforcement Learning (RL) offers a theoretical pathway to bridge this gap, its application is hindered by two fundamental obstacles: (1) \textit{Reward Coarseness}, where semantic metrics like CLIP scores fail to pena...
  </details>

- **2026-06-30** — Nan Li, Albert Gatt, Massimo Poesio — [Seeing Is Not Sharing: Some Vision-Language Models Overestimate Common Ground in Asymmetric Dialogue](http://arxiv.org/abs/2606.31719v1)
  <details><summary>📄 Abstract</summary>
  In collaborative dialogue, shared perception does not guarantee shared interpretation. Mutual understanding must be established through interaction. We investigate whether vision-language models (VLMs) can distinguish what could be shared from what has been shared between dialogue participants through grounding. We formulate this as an interpretation-matching task on 13,077 annotated reference expressions from HCRC MapTask dialogues, and evaluate VLMs under systematically controlled manipulation...
  </details>

- **2026-06-30** — Javal Vyas, Milapji Singh Gill, Mehmet Mercangöz — [Automating Cause-Effect Specification with Knowledge Graphs and Large Language Models](http://arxiv.org/abs/2606.31614v1)
  <details><summary>📄 Abstract</summary>
  Engineering specifications such as interlocks, alarm rationalization tables, and cause-and-effect (C&E) matrices remain central to process control and safety, yet their creation is still predominantly manual, document-driven, and prone to inconsistency. This paper presents a semantic-AI framework that automates the generation of C&E logic by combining a knowledge graph (KG) with a constrained large language model (LLM) layer. The KG builds on an established modular alignment ontology to represen...
  </details>

- **2026-06-30** — Jason R. Brown, Patrick Leask, Lev McKinney — [Evil Spectra: How Optimisers can Amplify or Suppress Emergent Misalignment](http://arxiv.org/abs/2606.31591v1)
  <details><summary>📄 Abstract</summary>
  Emergent misalignment (EM) is a recently discovered phenomenon in LLMs where fine-tuning on a narrow misaligned task, such as writing insecure code, leads to broadly misaligned behaviour on unrelated prompts. Previous work has noted that the severity of EM is highly sensitive to training choices; however, we still lack a systematic characterisation of this sensitivity. We perform a sweep over several Qwen3 models, optimisers, datasets, and batch sizes, and find that the choice of optimiser has t...
  </details>

- **2026-06-30** — Xudong Wu, Pangpang Liu, Vaneet Aggarwal et al. — [On the Convergence of Self-Improving Online LLM Alignment](http://arxiv.org/abs/2606.31524v1)
  <details><summary>📄 Abstract</summary>
  The Self-Improving Alignment (SAIL) algorithm addresses distribution shift by reducing a bilevel formulation of the problem to an efficient, single-level method. Empirically, SAIL has demonstrated strong performance on this task. However, a formal analysis of its convergence properties has been lacking. We identify a key theoretical challenge: the standard SAIL objective function is not guaranteed to be strongly concave due to unfavorable properties of its Hessian. To address this limitation, we...
  </details>

- **2026-06-30** — Runhao Li, Xiaoxu Ma, Zhenyu Weng et al. — [Unsupervised Data-Efficient Cross-Modal Retrieval with Global-Neighborhood Alignment Hashing](http://arxiv.org/abs/2606.31517v1)
  <details><summary>📄 Abstract</summary>
  Compared to supervised cross-modal hashing (CMH), unsupervised CMH reduces the reliance on manual labeling by learning binary codes from unlabeled image-text pairs. However, existing unsupervised CMH methods often rely on large-scale image-text pairs, which are costly to collect. To address this limitation, we propose Global-Neighborhood Alignment Hashing (GNAH), a novel approach that preserves the semantic structure of vision-language foundation models within a compact binary Hamming space usin...
  </details>

- **2026-06-30** — Jack Bell, Giacomo Carfi, Gerlando Gramaglia et al. — [CLOUDADV: Decision-Aligned Instance Sizing with Zero-Shot Foundation Models under Drift](http://arxiv.org/abs/2606.31470v1)
  <details><summary>📄 Abstract</summary>
  Cloud virtual machines are often overprovisioned, creating avoidable cost and operational inefficiency. We present CLOUDADV, an interactive engineer-facing advisory system for cloud instance sizing under workload drift. The system combines zero-shot time-series forecasting with bounded recommendation generation across day-, week-, and month-scale planning horizons. For each query, CLOUDADV constructs a structured decision context from historical utilization, forecast summaries, current VM metada...
  </details>

- **2026-06-30** — Jisung Park, Seohyeon Kang, Daeun Yoo et al. — [Resolving superposition in AI for interpretability and cross-modal alignment in patient-neuronal images](http://arxiv.org/abs/2606.31394v1)
  <details><summary>📄 Abstract</summary>
  Artificial intelligence is transforming our capability to solve biological challenges. In dimensionality bottleneck regimes exacerbated by high-dimensional biological data, Neural networks force distinct concepts into the lower dimensions known as superposition. Although this superposition is widely known to hinder interpretability, its impact on corrupting the geometry of latent spaces remains critically overlooked. Here, we utilized sparse autoencoders (SAEs) trained on over 100,000 multiplexe...
  </details>

- **2026-06-30** — Joonkyu Park, Kyoung Mu Lee — [Language-Assisted Super-Resolution from Real-World Low-Resolution Patches](http://arxiv.org/abs/2606.31363v1)
  <details><summary>📄 Abstract</summary>
  Single image super-resolution aims to reconstruct high-resolution (HR) images from low-resolution (LR) inputs. Training SR models typically requires paired HR-LR data, which is difficult to obtain in reality. As a result, most methods synthesize LR images by artificially degrading HR images with handcrafted kernels or camera ISP adjustments. However, these synthetic degradations fail to capture the complexity of real LR images, leading to poor generalization in practice. To address this, we obse...
  </details>

- **2026-06-30** — Aurélien Pellet, Julien Perez, Marie Puren — [HistoriQA-ThirdRepublic: Multi-Hop Question Answering Corpus for Historical Research, Parliamentary Debates from the French Third Republic (1870-1940)](http://arxiv.org/abs/2606.31325v1)
  <details><summary>📄 Abstract</summary>
  We present HistoriQA-ThirdRepublic: a French-language dataset of multi-hop historical questions derived from parliamentary debates and newspapers of the French Third Republic. Designed in collaboration with a historian, the corpus captures complex reasoning patterns typical of historical inquiry, including cross-source synthesis, temporal reasoning, and the integration of sparse evidence. The dataset is made of 1782 questions and emphasizes multi-hop connections across heterogeneous historical d...
  </details>

- **2026-06-30** — Hong-Yun Lin, Fu-An Chao, Bi-Cheng Yan et al. — [LOPA: Enhancing Spoken Language Assessment via Latent Ordinal Prototype Alignment](http://arxiv.org/abs/2606.31310v1)
  <details><summary>📄 Abstract</summary>
  Fueled by increasing model scale and multimodal inputs, Multimodal Large Language Models (MLLMs) have emerged as a promising paradigm for Spoken Language Assessment (SLA). While effective, this paradigm often overlooks the intrinsic ordinal structure of language acquisition. This paper works around the necessity of large-scale MLLMs by introducing Latent Ordinal Prototype Alignment (LOPA) for SLA, a prototype-based regularizer that enforces an ordinal geometric prior directly on the latent space...
  </details>

- **2026-06-30** — Zhiyuan Yao, Zheren Fu, Zhixiao Zheng et al. — [ADAPT: Attention Dynamics Alignment with Preference Tuning for Faithful MLLMs](http://arxiv.org/abs/2606.31054v1)
  <details><summary>📄 Abstract</summary>
  Multimodal Large Language Models (MLLMs) are critically hampered by hallucination, generating content inconsistent with the provided image. In this paper, we identify an internal signature of hallucination: progressive degradation of text-to-image cross-attention during generation, leading to specific failure patterns like unfocused or biased attention. Existing mitigation strategies are largely outcome-driven and do not explicitly target this failure mode. To address this problem, we propose AD...
  </details>

- **2026-06-30** — Xiaozao Wang, Zhewei Wang, Hongyi Wen — [Evaluating Interactivity: Toward Automated Assessment of AI-Generated Explorable Explanations](http://arxiv.org/abs/2606.31012v1)
  <details><summary>📄 Abstract</summary>
  While large language models now enable rapid generation of interactive learning materials, evaluating the interaction quality of these explorable explanations remains an open challenge. Existing benchmarks largely focus on code executability or visual fidelity, providing limited insight into dynamic interaction behaviors such as learner-controlled state transitions and context-sensitive system responses, which are factors that critically shape learners' conceptual understanding. We present EE-Ev...
  </details>

- **2026-06-30** — Ahmadreza Chokhachian, V. Roshan Joseph, Yu Ding — [Spatio-Temporal Gaussian Process for Building Terrain-Incorporating Wind Power Curves](http://arxiv.org/abs/2607.00051v1)
  <details><summary>📄 Abstract</summary>
  Accurate modeling of wind turbine power curves is crucial for optimal wind farm operation. Nearly all existing power curve models focus on temporal variables such as wind speed and temperature while overlooking the influence of terrain covariates, which governs inflow wind conditions and thus also affects wind power production. This paper proposes a nonparametric spatio-temporal Gaussian process model that integrates temporal environmental covariates with spatial terrain features. The model fall...
  </details>

- **2026-06-30** — Ashutosh Mishra, Elian Neppel, Shreya Santra et al. — [Distributed Multi Robot Lunar Cargo Transportation via Phase Decomposed Reinforcement Learning](http://arxiv.org/abs/2607.00160v1)
  <details><summary>📄 Abstract</summary>
  Modular reconfigurable robotic systems provide a scalable solution for cooperative surface operations in future lunar missions. However, cooperative cargo transportation remains challenging due to morphology-dependent topology changes, strong payload-induced coupling, long-horizon decision making, and safety constraints. This paper proposes a phase-decomposed reinforcement learning framework for cooperative cargo transport with distributed robotic units. The task is decomposed into lifting, tran...
  </details>

- **2026-06-30** — Wenyuan Xie, Shaokai Wu, Yijin Zhou et al. — [MVP-Nav: Multi-layer Value Map Planner Navigator](http://arxiv.org/abs/2606.31919v1)
  <details><summary>📄 Abstract</summary>
  Zero-shot Object Goal Navigation (ZSON) with RGB-only perception poses a fundamental challenge for embodied agents, as the absence of explicit depth information introduces severe physical uncertainty and semantic-physical misalignment. Existing approaches either rely on high-level semantic reasoning without geometric grounding or learn end-to-end policies that lack explicit physical constraints, often resulting in semantically plausible but physically unsafe behaviors. In this paper, we propose ...
  </details>

- **2026-06-30** — Ben Slater, Matteo G. Mecattaf, Lucy G. Cheke et al. — [Theory of Mind and Persuasion Beyond Conversation: Assessing the Capacity of LLMs to Induce Belief States via Planning and Action](http://arxiv.org/abs/2606.31916v1)
  <details><summary>📄 Abstract</summary>
  Theory of Mind (ToM) benchmarks for Large Language Models (LLMs) typically rely on passive question-answering formats, but the deployment of LLMs in increasingly agentic and autonomous forms demands new evaluations. In this paper we evaluate an agent's ability to induce specific belief states in other agents by taking actions rather than using conversational persuasion, a capability we call Non-Conversational Planning ToM (NCP-ToM). NCP-ToM is likely to be essential for many agent use-cases, inc...
  </details>


### 📂 robustness
*鲁棒性与可靠性 / Robustness & Reliability* — 89 papers

- **2026-07-02** — Matteo Boglioni, Thibault Rousset, Siva Reddy et al. — [LACUNA: A Testbed for Evaluating Localization Precision for LLM Unlearning](http://arxiv.org/abs/2607.02513v1)
  <details><summary>📄 Abstract</summary>
  LLMs memorize sensitive training data, including personally identifiable information (PII), creating a pressing need for reliable post hoc removal methods. Unlearning has emerged as a promising solution, with state-of-the-art(SOTA) methods often following a localize-first, unlearn-second paradigm that targets specific model parameters. However, existing benchmarks evaluate unlearning solely at the output level, leaving open the question of whether unlearning truly erases knowledge from a model's...
  </details>

- **2026-07-02** — Misha Sulpovar, Benn R. Konsynski, Qaish Kanchwala et al. — [ContextNest: Verifiable Context Governance for Autonomous AI Agent](http://arxiv.org/abs/2607.02116v1)
  <details><summary>📄 Abstract</summary>
  Autonomous AI agents increasingly depend on external knowledge stores, yet most retrieval pipelines provide relevance without durable guarantees of provenance, version identity, integrity, traceability, or point-in-time reconstruction. We formalize this as context governance and present ContextNext, an open specification and reference implementation for governed AI-consumable knowledge vaults. ContextNext does not replace Retrieval-Augmented Generation (RAG); it supplies the governance layer ben...
  </details>

- **2026-07-02** — Minjong Cheon — [Robust for the Wrong Reasons: The Representational Geometry of LLM Robustness to Science Skepticism](http://arxiv.org/abs/2607.01951v1)
  <details><summary>📄 Abstract</summary>
  Large language models (LLMs) are increasingly consulted on contested scientific questions, raising the concern that they will sycophantically retreat from established consensus when a user signals doubt -- drifting toward a false balance that treats settled science as one view among several. We test this across three open instruction-tuned models (Llama-3.1-8B, Qwen2.5-7B, Mistral-7B), three consensus-science domains (climate, vaccines, evolution), and single- and multi-turn settings, combining ...
  </details>

- **2026-07-02** — Alex Brooker, Tim Hughes — [Pre-Flight: A Benchmark for Evaluating Large Language Models on Aviation Operational Knowledge](http://arxiv.org/abs/2607.01829v1)
  <details><summary>📄 Abstract</summary>
  Large language models (LLMs) are increasingly proposed for aviation business operations, from documentation and training generation to customer facing assistants. General purpose benchmarks do not measure whether a model reasons safely and correctly about aviation specific operational knowledge, and the high stakes, regulated nature of the domain makes that gap consequential. We present Pre-Flight, an open source benchmark of 300 multiple choice questions drawn from international standards and a...
  </details>

- **2026-07-02** — Jiamin Jiang, Jingfei Feng, Yu Luo et al. — [KRCA: An Efficient Root Cause Analysis System in Hyper-Scale Microservice Systems via Agentic AI](http://arxiv.org/abs/2607.01788v1)
  <details><summary>📄 Abstract</summary>
  Hyper-scale microservice systems have become the standard infrastructure for large-scale Internet companies. These systems consist of numerous loosely coupled microservices that evolve independently through continuous development and deployment. Such complexity makes failures unavoidable, necessitating efficient Root Cause Analysis (RCA) to help Site Reliability Engineers (SREs) quickly localize root cause services and classify failure types. However, existing RCA methods often struggle to adapt...
  </details>

- **2026-07-02** — Meng Wang, Haohan Zhao, Wenzhuo Liu et al. — [Denser $\neq$ Better: Limits of On-Policy Self-Distillation for Continual Post-Training](http://arxiv.org/abs/2607.01763v1)
  <details><summary>📄 Abstract</summary>
  Continual post-training enables foundation models to acquire new knowledge while preserving existing capabilities. Recent work suggests that on-policy learning can mitigate forgetting, with on-policy self-distillation emerging as a particularly attractive approach. In this work, we revisit this optimistic view through self-distillation policy optimization (SDPO). Our experiments show that SDPO can accelerate in-domain specialization when teacher signals are stable and well aligned, but it strugg...
  </details>

- **2026-07-02** — Sung June Kim, Sangpil Kim, Honglak Lee — [Path-level Hindsight Instructions for Semantic Exploration in Vision-Language Navigation](http://arxiv.org/abs/2607.01754v1)
  <details><summary>📄 Abstract</summary>
  On-policy exploration is a crucial component for training robust Vision-Language Navigation agents, as it exposes the policy to a broader state distribution. However, such exploration inevitably leads to trajectories that deviate from expert demonstrations, resulting in a semantic mismatch between the executed visual stream and the original language instruction. In this work, we address this challenge by introducing Phi-Nav, a unified on-policy framework that leverages hindsight reasoning to ali...
  </details>

- **2026-07-02** — Yongjie Bai, Hanting Wang, Mingtong Dai et al. — [Bridge-WA: Predicting Where and How the World Changes for Robotic Action](http://arxiv.org/abs/2607.02195v1)
  <details><summary>📄 Abstract</summary>
  General-purpose vision-language-action models benefit from large vision-language priors, but effective manipulation also requires anticipating action-relevant scene changes. Existing world-action models often rely on large generative world models or dense future rollouts, which are expensive and spend capacity on visual details weakly coupled to control. We present Bridge-WA, a lightweight world-action framework that distills a frozen future-change teacher into three compact priors: future token...
  </details>

- **2026-07-02** — Haofei Xu, Rundi Wu, Philipp Henzler et al. — [PointDiT: Pixel-Space Diffusion for Monocular Geometry Estimation](http://arxiv.org/abs/2607.02515v1)
  <details><summary>📄 Abstract</summary>
  State-of-the-art single-image 3D reconstruction methods often rely on complex hybrid architectures and loss functions, or compress geometry into latent spaces in order to leverage pre-trained latent diffusion models. In this work, we show that such architectural overhead and intricate loss formulations are unnecessary. We introduce a minimalist pixel-space Diffusion Transformer, built on a plain ViT, that operates directly on raw 3D point map patches and is conditioned on image tokens from a pre...
  </details>

- **2026-07-02** — Yuxuan Li, Lingxi Xie, Xinyue Huo et al. — [Reasoning LLM Improves Speaker Recognition in Long-form TV Dramas](http://arxiv.org/abs/2607.02504v1)
  <details><summary>📄 Abstract</summary>
  Long-form TV dramas present a formidable challenge for comprehensive video understanding, where deciphering complex storyline often relies on \textbf{speaker recognition}, the task of accurately attributing each spoken utterance to its respective character. In this paper, we advance this field through two primary contributions. (1) We introduce \textbf{DramaSR-532K}, a large-scale benchmark comprising 532K annotated dialogue lines across more than 900 unique characters, necessitating the integra...
  </details>

- **2026-07-02** — Xi Zhang, Papi Menon, Vivian Chu et al. — [Adoption and Ecosystem Health: A Longitudinal Analysis of Open-Source Multi-Agent Frameworks](http://arxiv.org/abs/2607.02453v1)
  <details><summary>📄 Abstract</summary>
  Since ChatGPT's launch in November 2022, open-source agentic frameworks have proliferated, making framework selection important for engineering teams while obscured by popularity signals such as GitHub stars. This paper analyzes 15 major open-source AI agent framework repositories from late 2022 to early 2026, using 808,042 stars, 73,997 pull requests, 86,241 commits, and 987,330 user profiles to assess ecosystem health across awareness, adoption, and retention. Three findings emerge. First, hea...
  </details>

- **2026-07-02** — Xi Fang, Weijie Xu, Yingqiang Ge et al. — [DRIFTLENS: Measuring Memory-Induced Reasoning Drift in Personalized Language Models](http://arxiv.org/abs/2607.02374v1)
  <details><summary>📄 Abstract</summary>
  Personalization changes what a model says to a user; we show that it can also change the reasoning trajectory used to justify the response. Modern LLMs personalize interactions by storing user attributes, preferences, and prior context, then injecting this information into future prompts. We study whether such memory reshapes reasoning on open-ended questions where no single ground-truth answer exists. To quantify this effect, we introduce DRIFTLENS, a ground-truth-free framework that maps each ...
  </details>

- **2026-07-02** — Wanyun Cui — [A Hippocampus for Linear Attention: An Exact Memory for What the Recurrent State Forgets](http://arxiv.org/abs/2607.02303v1)
  <details><summary>📄 Abstract</summary>
  Linear-attention and state-space language models compress the prefix into a fixed-size recurrent state, yielding O(1) memory at the cost of a lossy exact memory: when many key--value associations compete, earlier facts are overwritten and needle recall degrades. Inspired by Complementary Learning Systems, we give linear attention a hippocampal complement. HOLA (Hippocampal Linear Attention) keeps the usual delta-rule state as a compressive memory and adds a bounded exact KV cache, forming a semi...
  </details>

- **2026-07-02** — Tien-Phat Nguyen, Ngai-Man Cheung — [When Token Compression Breaks: Structural Pruning vs. Token Reduction for Robust ViT Segmentation under High Compression](http://arxiv.org/abs/2607.02237v1)
  <details><summary>📄 Abstract</summary>
  Vision Transformers (ViTs) are strong backbones for semantic segmentation, but their computational cost limits deployment. Recent token compression methods for efficient transformer-based segmentation reduce this cost by decreasing the number of tokens. However, existing evaluations primarily focus on low-to-moderate compression, leaving their behavior under aggressive compression and corrupted inputs unclear. Meanwhile, structural pruning provides an orthogonal route to efficiency by removing r...
  </details>

- **2026-07-02** — Satoshi Yamamori, Koji Ishihara, Kentaro Minamikawa et al. — [Actuator Reality Shaping for Zero-Shot Sim-to-Real Robot Learning](http://arxiv.org/abs/2607.02205v1)
  <details><summary>📄 Abstract</summary>
  Sim-to-real transfer in robot learning is often limited by discrepancies between the ideal actuator dynamics assumed during policy training and the nonlinear, hardware-dependent behavior of physical motors. While conventional approaches attempt to bridge this gap by increasing simulator fidelity through system identification, domain randomization, or learned actuator models, we introduce an alternative paradigm: actuator reality shaping. Instead of modifying the simulator to match the real world...
  </details>

- **2026-07-02** — Shunya Kato, Taiki Miyanishi, Shuhei Kurita et al. — [LongEgoRefer: A Benchmark for Long-Form Egocentric Video Referring Expression Comprehension](http://arxiv.org/abs/2607.02096v1)
  <details><summary>📄 Abstract</summary>
  Egocentric videos capture rich and diverse human-object interactions and have emerged as a fundamental resource for understanding human activities related to objects. In this context, Video Referring Expression Comprehension (Video REC), the task of localizing the temporal and spatial extent of a referred object in video frames given a natural language query, plays a key role in linking textual descriptions to observed objects in untrimmed egocentric recordings. However, existing egocentric Vide...
  </details>

- **2026-07-02** — Yihuai Zhang, Yidan Cao, Huan Yu et al. — [Robust Stabilization of Linear Markov-Jumping Hyperbolic PDEs with Boundary Input Delay](http://arxiv.org/abs/2607.02081v1)
  <details><summary>📄 Abstract</summary>
  This paper studies the robust stabilization of 2 $\times$ 2 linear hyperbolic partial differential equations (PDEs) with Markov-jumping parameters and boundary input delay. The main challenge arises from the simultaneous presence of stochastic parameter variations and input delay, which complicates both the stability analysis and controller design. To address this issue, a nominal delay-compensating backstepping controller is first designed for a fixed nominal system. Applying the nominal transf...
  </details>

- **2026-07-02** — Qianyu Chen, Canran Xiao, Runxuan Tang — [Hidden Forgetting in Continual Multimodal Learning: When Accuracy Survives but Grounding Fails](http://arxiv.org/abs/2607.02020v1)
  <details><summary>📄 Abstract</summary>
  Multimodal large language models must continually adapt to evolving tasks and domains, yet standard continual learning metrics mainly measure whether old answers remain correct, leaving the stability of multimodal grounding largely unexamined. We study this overlooked failure mode and ask whether a continually adapted MLLM can preserve not only what it answers, but also how it uses visual, textual, OCR, chart, and document evidence. We identify \emph{hidden evidence-use forgetting}, where answer...
  </details>

- **2026-07-02** — Yi Wang, Fan Wang, Prabin Gyawali et al. — [UnderOneFacade: Worldwide Facade Semantic Segmentation Benchmark Dataset](http://arxiv.org/abs/2607.02018v1)
  <details><summary>📄 Abstract</summary>
  Globally consistent semantic digital twins require centimeter-accurate and geographically transferable 3D facade segmentation. However, progress in facade parsing is limited by the lack of large-scale, standardized benchmarks for evaluating cross-domain generalization. Existing datasets are geographically narrow, semantically inconsistent, or insufficiently precise. We introduce UnderOneFacade, the largest cross-country and cross-continent 3D facade benchmark to date, comprising centimeter-accur...
  </details>

- **2026-07-02** — Cedric Richter, Mike Papadakis — [Underspecification does not imply Incoherence: The Risks of Semantic Collapse in Coding Models](http://arxiv.org/abs/2607.01953v1)
  <details><summary>📄 Abstract</summary>
  Large Language Models (LLMs) have become increasingly effective at generating code when task descriptions are clear and precise. Yet, in practice, user-provided task descriptions are often ambiguous, incomplete, or contradictory, leaving critical aspects of the intended program behavior underspecified. In such cases, multiple behaviorally distinct interpretations may satisfy the description equally well, yet semantically differ in ways that matter/affect the user intent. A natural expectation, o...
  </details>

- **2026-07-02** — Lihui Luo, Joongwon Chae, Ziyan Chen et al. — [MMIR-TCM: Memory-Integrated Multimodal Inference and Retrieval for TCM Clinical Decision Support](http://arxiv.org/abs/2607.01814v1)
  <details><summary>📄 Abstract</summary>
  Traditional Chinese Medicine (TCM) diagnosis, particularly through tongue inspection, faces persistent challenges in subjectivity and reproducibility. The application of multimodal artificial intelligence to TCM clinical tasks, such as syndrome differentiation and prescription generation, is significantly hampered by the semantic gap between visual tongue features and textual reasoning, as well as the lack of large-scale, standardized datasets. To address these challenges, we introduce MMIR-TCM,...
  </details>

- **2026-07-02** — Haoju Lin, Wenchang Zhang, Weipeng Xu et al. — [TO-Master: an LLM-agent framework for automated topology optimization](http://arxiv.org/abs/2607.01812v1)
  <details><summary>📄 Abstract</summary>
  Topology optimization (TO) has become a mature computational design method, but using it still requires substantial manual effort in geometry preparation, mesh generation, boundary-condition assignment, solver setup, and postprocessing. This implementation barrier limits the use of TO outside expert workflows, even when differentiable finite element solvers are available. This work introduces TO-Master, a large language model (LLM) agent framework that turns finite-element-based TO into a conver...
  </details>

- **2026-07-02** — Jiatong Li, Weida Wang, Changmeng Zheng et al. — [Do LLMs Truly Generalize in the Molecular Domain? A Perturbation-Based Analysis](http://arxiv.org/abs/2607.01800v1)
  <details><summary>📄 Abstract</summary>
  Large Language Models (LLMs) have recently shown promise in molecular discovery, yet a gap remains between their probabilistic nature over discrete sequential tokens and the rigid topological constraints of chemical space. This raises the question of whether molecular LLMs can generalize beyond the local neighborhoods induced by their sequence-based representations. To systematically investigate this question, we introduce a Molecular Perturbation framework that generates syntax-valid structural...
  </details>

- **2026-07-02** — Wen Wang, Yaping Sun, Yejun He et al. — [LLM-Empowered Multimodal Fusion Framework for Autonomous Driving: Semantic Enhancement and Channel-Adaptive Design](http://arxiv.org/abs/2607.01772v1)
  <details><summary>📄 Abstract</summary>
  Vision-radar fusion is central to robust autonomous driving, combining dense visual semantics with precise range and velocity measurements from radar. However, real-world fusion quality is fundamentally challenged by dynamically varying input quality, stemming from occlusion, adverse weather, and channel noise. To address this, we re-frame the problem from static data fusion to channel-aware semantic reasoning and propose a Large Language Model-centric Semantic-layer Channel-aware Integrated Per...
  </details>

- **2026-07-02** — Ronghui Xu, Tongxin Wu, Guozhen Zhang et al. — [UniWind: Toward Unified Day-Ahead Wind Power Forecasting via Physics-Informed State Routing](http://arxiv.org/abs/2607.01670v1)
  <details><summary>📄 Abstract</summary>
  Day-ahead wind power forecasting is essential for cost-effective power-system operation. It is primarily driven by future meteorological conditions while retaining temporal dependencies in power generation. In practice, observed wind-farm power often entangles physically available power with local environmental effects and latent operational states, such as shutdowns and curtailment. Existing physical models provide useful constraints but adapt poorly across wind farms, whereas data-driven model...
  </details>

- **2026-07-02** — Eunyi Lyou, Yunjeong Choi, Junho Lee et al. — [Domain Generalization via Text-Anchored Information Bottleneck](http://arxiv.org/abs/2607.01657v1)
  <details><summary>📄 Abstract</summary>
  Visual recognition models often fail when deployed in new environments. Domain Generalization (DG) addresses this by learning representations that remain invariant to environment-specific variations. Recent approaches increasingly rely on large vision-language models, assuming that preserving their expressive visual representations improves robustness. However, we show that such visual expressiveness can instead propagate spurious cues that tie representations to the training environments, hinde...
  </details>

- **2026-07-01** — Yaofei Duan, Yuhao Huang, Tianyu Zhang et al. — [ClinRAG-GRAPH: Clinical-prior Retrieval-Augmented Graph Model with Domain Adversarial Learning for Breast pCR Prediction](http://arxiv.org/abs/2607.00798v1)
  <details><summary>📄 Abstract</summary>
  Neoadjuvant chemotherapy (NAC) response prediction is clinically important for treatment stratification in breast cancer. However, robust pre-treatment pathological complete response (pCR) prediction remains challenging due to insufficient cross-modal modeling, multicenter imaging heterogeneity, and weak evidence-grounded interpretability. We propose ClinRAG-GRAPH, a Clinically informed Retrieval-Augmented Generation Graph framework, for pre-treatment pCR prediction from DCE-MRI, structured clin...
  </details>

- **2026-07-01** — Nils Neukirch, Martin Maurer, Nils Strodthoff — [Foundation Models vs. Radiomics for Lung Computed Tomography: A Benchmark of Feature Extractors, Classification Heads, and Segmentation Choices](http://arxiv.org/abs/2607.01001v1)
  <details><summary>📄 Abstract</summary>
  Radiomics is the established approach for CT-based lung cancer phenotyping, yet comparisons with foundation models rarely isolate contributions of feature extractor, classification head, and segmentation choice, or test cross-cohort robustness. We benchmark five feature extractors (Curia, Curia-2, DINOv3, Radiomics2D, Radiomics3D), seven classification heads (TabPFN, TabICL, XGBoost, CatBoost, Random Forest, logistic regression, Ridge), and three segmentation regimes on five tasks: tumor volume ...
  </details>

- **2026-07-01** — Xinyi Shang, Peng Sun, Bei Shi et al. — [Condensing Large-Scale Datasets Directly with Minimal Information Loss](http://arxiv.org/abs/2607.00916v1)
  <details><summary>📄 Abstract</summary>
  Recent advancements in scaling dataset distillation rely heavily on decoupled information extraction pipelines, comprising SQUEEZE, RECOVER, and RELABEL stages. Despite their scalability to large-scale datasets, these methods suffer from prohibitive computational overhead and poor cross-architecture generalization. In this paper, we reveal the root cause of these bottlenecks: the implicit dual-compression process, from data to model and back to images, inherently induces severe information loss....
  </details>

- **2026-07-01** — Yuan Qing, Chengzhi Mao, Boqing Gong — [StochasT: Learning with Stochastic Turn Depth for Visual Instruction Tuning](http://arxiv.org/abs/2607.00465v1)
  <details><summary>📄 Abstract</summary>
  Large Vision-Language Models (LVLMs) rely extensively on Visual Instruction Tuning (VIT) to elicit their multimodal reasoning capabilities. However, we find a discrepancy: VIT often packs multiple language tasks about the same image for conversational, multi-turn training, whereas existing benchmarks evaluate LVLMs in isolated, single-turn scenarios. The models can suffer from visual attention decay and contextual overfitting during multi-turn training, making it hard for them to realize their f...
  </details>

- **2026-07-01** — Xiangchen Song, Zhenhao Chen, Lingjing Kong et al. — [Beyond Perplexity: A Behavioral Evaluation Framework for Deployment-Memory Claims in LLM Test-Time Training](http://arxiv.org/abs/2607.00368v1)
  <details><summary>📄 Abstract</summary>
  Large language model test-time training (TTT) is often evaluated through local proxy metrics: models are updated on recent tokens, retrieved context, target-domain data, or verifiable task attempts, and then judged by perplexity, future-token loss, long-context performance, or reward. These metrics are well matched to claims about stream adaptation, domain adaptation, context compression, and reward-backed test-time improvement. They are weaker evidence, however, for a capability that TTT result...
  </details>

- **2026-07-01** — Kuan-Chen Chen, Winston Chen, Wei-Fang Sun et al. — [VLM-AR3L: Vision-Language Models for Absolute and Relative Rewards in Reinforcement Learning](http://arxiv.org/abs/2607.00483v1)
  <details><summary>📄 Abstract</summary>
  Designing effective reward functions remains a major challenge in reinforcement learning (RL), particularly in open-ended environments where task goals are abstract and difficult to quantify. In this work, we present VLM-AR3L, a framework that leverages Vision-Language Models (VLMs) to provide both absolute and relative rewards for RL. VLM-AR3L interprets an agent's visual observations in the context of a natural language task goal, and learns both absolute and relative rewards from VLM-generate...
  </details>

- **2026-07-01** — Austin McDannald, Julia Tisaranni, Howie Joress — [Optimal Resource Utilization for Autonomous Laboratory Orchestrators](http://arxiv.org/abs/2607.01188v1)
  <details><summary>📄 Abstract</summary>
  In autonomous laboratories, AI agents suggest the next batch of experiments to do. However, planning and executing those tasks taking full advantage of the available resources is a completely different question. This can be challenging when dealing with real-world hardware constraints, especially so when there are multiple instruments with different capacities and throughputs. Here we demonstrate a 2-step method to address resource utilization for our autonomous platform for metal-organic framew...
  </details>

- **2026-07-01** — Roger Beaty, Vijeta Deshpande, Clin K. Y. Lai et al. — [AGC-Bench: Measuring Artificial General Creativity](http://arxiv.org/abs/2607.01152v1)
  <details><summary>📄 Abstract</summary>
  Creativity research has debated whether creativity is domain-specific (e.g., visual, writing, science), and if it is psychometrically separable from general intelligence. Both questions now apply to LLMs, but a unified benchmark of AI creativity remains elusive. We introduce AGC-Bench, an artificial general creativity benchmark built from a systematic review of the AI creativity literature (3,101 papers screened, 497 benchmarks identified), paired with an agentic harness that converts idiosyncra...
  </details>

- **2026-07-01** — Adam Pooley, Matthew Hale — [Technical Report: Asynchronous Distributed Trajectory Estimation of Multi-Robot Systems](http://arxiv.org/abs/2607.01106v1)
  <details><summary>📄 Abstract</summary>
  Distributed trajectory estimation arises in many applications across robotics, but existing implementations typically do not consider asynchrony in agents' communications and computations. Therefore, we propose an asynchronous block coordinate descent algorithm for distributed trajectory estimation. We consider a team of agents that observes a team of robots and estimates their states over a sliding window. The agents solve an approximation of the maximum a posteriori estimation problem, which w...
  </details>

- **2026-07-01** — Valentino Sacco, Luca Scofano, Indro Spinelli et al. — [Robots Ask the Way: Communication-Enabled Social Navigation](http://arxiv.org/abs/2607.01044v1)
  <details><summary>📄 Abstract</summary>
  Assistive autonomous robots operating in multi-agent environments require efficient strategies to locate specific individuals among multiple residents. Current social navigation methods focus on reactive collision avoidance and trajectory adaptation, but lack mechanisms to proactively gather information through human-robot communication.   We introduce Communication-enabled Social Navigation (CommNav). In this novel task, robotic agents actively seek assistance from residents to locate target in...
  </details>

- **2026-07-01** — Eric Benz, Lennart Stöpler, Nikolai Bolik et al. — [KnowledgeDebugger -- an Exploration Tool for Knowledge Localization and Editing in Transformers](http://arxiv.org/abs/2607.01000v1)
  <details><summary>📄 Abstract</summary>
  Recent research has increasingly focused on understanding how Transformers store and process knowledge, as well as how this knowledge can be edited. Research work in this area is often conducted in two phases: first, phenomena are explored on individual samples. Then, when results appear promising, more statistically robust experiments follow. To support the first phase, we propose KnowledgeDebugger, a GUI-based exploration tool for knowledge localization and editing in Transformers. Our tool - ...
  </details>

- **2026-07-01** — Yingzhou Li, Jingyu Liu — [A Superfast Direct Solver for 2D Type-II Inverse Nonuniform Discrete Fourier Transform Based on Hierarchically Semiseparable Matrix](http://arxiv.org/abs/2607.00928v1)
  <details><summary>📄 Abstract</summary>
  This paper proposes a direct inversion method for the 2D type-II nonuniform discrete Fourier transform~(NUDFT). The NUDFT matrix $A$ is factored as $A = G F$, where $G$ can be expressed as a kernel matrix and $F$ is the 2D DFT matrix. We show that $G$ can be approximated by a hierarchically semiseparable~(HSS) matrix and give an estimate of the HSS rank. Then, using the least-squares solver for HSS matrix and the two-dimensional inverse fast Fourier transform, the inverse NUDFT problem can be so...
  </details>

- **2026-07-01** — Wenhao Zhang, Kuanwei Lin, Xuyi Yang et al. — [EFlow: Learning Evidence Flow for Long-Video Reasoning with Adaptive Reflection](http://arxiv.org/abs/2607.00867v1)
  <details><summary>📄 Abstract</summary>
  Long-video reasoning is fundamentally constrained by how models acquire and utilize visual evidence. Existing tool-augmented video frameworks often interleave temporal grounding and answer reasoning within a single trajectory, causing early semantic hypotheses to bias evidence localization. We term this failure mode premature semantic commitment, where biased grounding retrieves incomplete evidence and incomplete evidence further reinforces incorrect reasoning. To address this issue, we propose ...
  </details>

- **2026-07-01** — Xuelin Zhu, Xiu-Shen Wei, Jiawei Ge et al. — [Rethinking Multi-Label Image Classification With Deep Learning: Taxonomy, Challenge, and Outlook](http://arxiv.org/abs/2607.00839v1)
  <details><summary>📄 Abstract</summary>
  Multi-label image classification (MLIC), a fundamental task in computer vision, focuses on identifying multiple objects or concepts within an image, underpinning numerous read-world applications, such as autonomous driving, disease diagnosis, recommendation system, and mobile service robot. Over the past decade, deep learning paradigms based on convolutional neural networks, recurrent neural networks, and Transformers have significantly advanced this field, owing to their powerful capability in ...
  </details>

- **2026-07-01** — Qian Serena Hou, Zecheng Gan — [LSR-Net: Long-Short-Range Operator Learning for Pattern Dynamics on Manifolds](http://arxiv.org/abs/2607.00750v1)
  <details><summary>📄 Abstract</summary>
  We propose the Long-Short-Range Neural Network (LSR-Net), an extensible operator-learning framework for predicting pattern dynamics on planar domains, spherical surfaces, and general manifolds. The method decomposes the forward evolution operator into a long-range component, represented by a compact Fourier multiplier constructed via the Sum-of-Exponentials (SOE) approximation, and a short-range component adapted to the underlying geometry and its intrinsic symmetries. For general manifolds repr...
  </details>

- **2026-07-01** — Zheng Fang, Dongming Jin, Yihong dong et al. — [ClarifyCodeBench: Evaluating LLMs on Clarifying Ambiguous Requirements for Code Generation](http://arxiv.org/abs/2607.00711v1)
  <details><summary>📄 Abstract</summary>
  Large Language Models have emerged as programming assistants. However, the efficacy of code generation is constrained by the quality of input requirements, which are frequently ambiguous, incomplete, or underspecified. While LLMs excel at one-shot code synthesis, their ability to proactively clarify intent remains underexplored, as a critical trait for robust software engineering. Existing benchmarks largely overlook this interactive bottleneck, assuming perfectly specified prompts that do not r...
  </details>

- **2026-07-01** — Cong Liu, Xiaofang Li, Simon X. Yang — [Active Spatial Guidance: Eliminating Injected Positional Mechanisms in Vision Transformers](http://arxiv.org/abs/2607.00580v1)
  <details><summary>📄 Abstract</summary>
  Vision Transformers (ViTs) commonly rely on injected positional mechanisms to address self-attention's permutation invariance. Motivated by the spatial regularities of natural images, we ask whether spatial organization can be induced from data rather than explicitly injected. Under controlled, matched from-scratch training, we propose Active Spatial Guidance (Guidance), a training-only objective that disables positional injection and applies an auxiliary 2D coordinate-regression loss to the fin...
  </details>

- **2026-07-01** — Michael Tatarjitzky, Vladimir Tourbabin, Boaz Rafaely — [AmbiDrop: Ambisonics-Based Array-Agnostic Neural Speech Enhancement](http://arxiv.org/abs/2607.00548v1)
  <details><summary>📄 Abstract</summary>
  Multichannel Deep Neural Networks (DNNs) have significantly improved speech enhancement performance; however, they typically remain constrained by reliance on fixed microphone array geometries, leading to poor generalization on unseen or irregular configurations. Current array-agnostic approaches often rely on high-complexity architectures or massive, diverse datasets, yet they still struggle to generalize to out-of-distribution layouts. In this paper, we present an in-depth analysis of AmbiDrop...
  </details>

- **2026-07-01** — Xuefeng Liu, Mingxuan Cao, Qinan Huang et al. — [Active-GRPO: Adaptive Imitation and Self-Improving Reasoning for Molecular Optimization](http://arxiv.org/abs/2607.00531v1)
  <details><summary>📄 Abstract</summary>
  Scientific reasoning is an increasingly important capability of large language models, yet improving the robustness and efficiency of training such reasoning remains a key open challenge. We study this problem in instruction-based molecular optimization, where answer-only supervised fine-tuning (SFT) collapses multi-step reasoning and reinforcement learning with verifiable rewards (RLVR) suffers from sparse feedback. Reference-guided Policy Optimization mitigates both by anchoring policy updates...
  </details>

- **2026-07-01** — Ananya Chattaraj, Conan Weiland, Bruce Ravel et al. — [Surface Platinum Alloying for Passivation of Oxide Interfaces on Superconducting Niobium Films](http://arxiv.org/abs/2607.00429v1)
  <details><summary>📄 Abstract</summary>
  Dielectric loss arising from two-level systems (TLS) at surfaces and interfaces remains a primary limitation to coherence in superconducting transmon qubits. Niobium (Nb), a widely used material in superconducting quantum circuits, readily forms native oxides under ambient conditions, leading to lossy dielectric interfaces that degrade device performance. Here, a robust and scalable fabrication strategy is demonstrated for chemically stabilizing Nb surfaces and mitigating further oxidation, incl...
  </details>

- **2026-07-01** — Qiyan Luo, Yingdong Pi, Lekang Wen et al. — [EO-VGGT: Orbital Ray-Conditioned 3D Foundation Models for Satellite Multi-View Reconstruction](http://arxiv.org/abs/2607.00417v1)
  <details><summary>📄 Abstract</summary>
  In the era of satellite constellations, multi-view optical satellite imagery is pivotal for Earth Observation (EO) and high-quality Digital Surface Model (DSM) reconstruction. Although feed-forward 3D foundation models have transformed computer vision, their deployment in satellite remote sensing is inherently constrained by the structural discrepancy between implicit perspective assumptions and explicit orbital pushbroom geometry. This geometric incongruity is further compounded by pronounced v...
  </details>

- **2026-07-01** — Jongchan Park, Seungjun Oh, Seungho Baek et al. — [Learning Generalizable Skill Policy with Data-Efficient Unsupervised RL](http://arxiv.org/abs/2607.00392v1)
  <details><summary>📄 Abstract</summary>
  Unsupervised Reinforcement Learning (URL) aims to pre-train scalable, skill-conditioned policies without extrinsic rewards, serving as a foundation for downstream control tasks. Despite recent progress, we argue that current off-policy URL methods are limited by two critical, overlooked bottlenecks: (1) non-stationary skill semantics and (2) brittle generalization. To address these challenges, we propose GenDa (Generalizable Data-efficient Agent), a unified framework for robust unsupervised rein...
  </details>

- **2026-07-01** — Yaheng Wang, Rui Meng, Xiaodong Xu et al. — [Semantic-based Internet of Embodied Intelligence: Visions and Frontiers](http://arxiv.org/abs/2607.00342v1)
  <details><summary>📄 Abstract</summary>
  Recent advances in generative artificial intelligence (AI) and embodied intelligence (EI) enable autonomous agents to interact with the physical world. However, scaling these systems into networks of multiple agents, namely the Internet of EI (IoEI), faces critical bottlenecks. These include the overhead of massive multimodal data transmission and the decoupling of logical reasoning from physical constraints. To address these challenges, we envision the Semantic-based IoEI (SIoEI), which leverag...
  </details>

- **2026-07-01** — Zewen Liu — [Mapping the Evaluation Frontier: An Empirical Survey of the Bias-Reliability Tradeoff Across Eleven Evaluator-Agent Conditions](http://arxiv.org/abs/2607.00304v1)
  <details><summary>📄 Abstract</summary>
  The bias-reliability tradeoff conjectures that LLM evaluation systems are constrained in (gamma, H, CV) space, where evaluator coupling (gamma), strategy diversity (H), and small-sample measurement reliability (CV(N)) cannot be simultaneously optimized at fixed sample size N. Prior evidence rests on n=5 conditions with complete metrics from a single study. We expand the empirical base to 11 conditions, measuring gamma and H for all 11 (nine with valid weight vectors) and CV(N=5) for seven with s...
  </details>

- **2026-06-30** — Fei Liu, Alessio Figalli, Patrick Owen et al. — [RAISE: LLM-based Automated Heuristic Design with Robust Adversary Instance Search](http://arxiv.org/abs/2606.31801v1)
  <details><summary>📄 Abstract</summary>
  Automated Heuristic Design (AHD) with Large Language Models (LLMs) has shown remarkable progress in discovering high-quality heuristics. However, existing LLM-based AHD methods optimize heuristics for a fixed training instance set and may fail catastrophically when deployed under real-world distributional shifts. We propose Robust Adversary Instance Search (RAISE), a framework that integrates constrained worst-case instance search within a principled neighborhood of the training distribution int...
  </details>

- **2026-06-30** — Keivan Faghih Niresi, Alice Cicirello, Olga Fink — [Relational and Sequential Conformal Inference for Energy Time Series over Graphs via Foundation Models](http://arxiv.org/abs/2606.31804v1)
  <details><summary>📄 Abstract</summary>
  Accurate energy demand forecasting is essential for the reliable operation and planning of modern sustainable energy systems. Spatial-temporal graph neural networks (STGNNs) have recently achieved strong performance in point forecasting by jointly modeling temporal dynamics and relational dependencies across interconnected energy nodes. However, in real-world energy systems, accurate point forecasts alone are insufficient, as operators also require reliable uncertainty estimates to support risk-...
  </details>

- **2026-06-30** — Martina Mattioli, Marcello Pelillo — [Scientific Explanations in Health Sciences: Causality, Trust, and Epistemic Adequacy](http://arxiv.org/abs/2606.31616v1)
  <details><summary>📄 Abstract</summary>
  Medical Artificial Intelligence (AI) is widely expected to transform clinical practice, yet the decision-making processes of many Machine Learning (ML) models remain opaque. Explainability has been advanced as a partial remedy to clarify why AI generates predictions, particularly in high-stakes contexts. Despite ongoing efforts, debates on what constitutes an adequate medical explanation remain unsettled. Yet, explanation has long been a central topic of inquiry in the philosophy of science and ...
  </details>

- **2026-06-30** — Tao Chen, Lizheng Liu, Jiaxu Wang et al. — [Agentic RAG-VLM: Affordance-Aware Retrieval-Augmented Generation with Self-Reflective Planning for Robotic Grasping](http://arxiv.org/abs/2606.31200v1)
  <details><summary>📄 Abstract</summary>
  Generalizable robotic grasping in cluttered environments is essential for deploying manipulators in unstructured human spaces, yet existing VLM-based methods rely on visual similarity for object matching, neglecting physical affordances such as handle graspability and material fragility, and operate open-loop without spatial reasoning or failure recovery, limiting their effectiveness when objects are densely packed or physically diverse. We present Agentic RAG-VLM, a unified framework that bridg...
  </details>

- **2026-06-30** — Yixiao Li, Tifanny Portela, Jordis Herrmann et al. — [ELMP: Efficient Learning for Motion Planning via Analytical Policy Gradients](http://arxiv.org/abs/2607.00215v1)
  <details><summary>📄 Abstract</summary>
  Neural Motion Planners (NMPs) enable fast reactive motion generation, but adapting them to new environments typically requires recollecting large expert datasets, which is computationally prohibitive. We propose ELMP, a framework for data-efficient adaptation via self-supervised fine-tuning. Rather than generating additional expert trajectories with expensive global planners, ELMP directly optimizes the policy through a differentiable kinematic layer using dense collision, target-reaching, and s...
  </details>

- **2026-06-30** — Szabolcs Vitus, Ferenc Járai-Szabó — [Synchronization and Swarming of Two-Mode Stochastic Oscillators](http://arxiv.org/abs/2607.00179v1)
  <details><summary>📄 Abstract</summary>
  Synchronization and swarming are canonical manifestations of self-organization, observable across scales from cellular processes to animal flocks. This study investigates the collective dynamics of a novel agent-based model where individuals exhibit both spatial mobility and internal, two-mode stochastic oscillatory states. By introducing a local, distance-dependent coupling between the agents' spatial configuration and their internal state transitions, we establish a mutual feedback loop that d...
  </details>

- **2026-06-30** — Kira Goldner, Divyarthi Mohan, Thodoris Tsilivis — [Knowing Who, Not How Much: Learning-Augmented Mechanisms for Consumer Utility Maximization](http://arxiv.org/abs/2607.00175v1)
  <details><summary>📄 Abstract</summary>
  We study consumer utility maximization in an online random-order model where strategic agents arrive sequentially. To circumvent strong impossibility results for utility maximization, we turn to the framework of learning-augmented mechanism design. Crucially, we show that the types of predictions commonly used in learning-augmented mechanism design (such as predictions of agent values or the optimal value) are not useful for utility maximization, where payments are directly at odds with the obje...
  </details>

- **2026-06-30** — Sajjad Abdoli, Ghassan Al-Sumaidaee, Ahmad ElShiekh et al. — [Benchmarking Frontier LLMs on Arabic Cultural and Sociolinguistic Knowledge: A Cross-Evaluation Framework with Human SME Ground Truth](http://arxiv.org/abs/2607.00139v1)
  <details><summary>📄 Abstract</summary>
  The cost of human expert evaluation is a principal bottleneck to deploying language models in specialized, high-stakes domains. This is particularly acute for Arabic sociolinguistic knowledge: credible grading requires not only linguistic fluency but deep cultural familiarity that cannot be approximated by surface-level metrics. We address this with a cross-evaluation framework instantiated on two underrepresented Arabic dialect communities: Egyptian and Iraqi Arabic. We contribute 103 validated...
  </details>

- **2026-06-30** — Dengxian Gong, Yuanzheng Wu, Haobo Yuan et al. — [PixelEyes: Decoupling Perception and Reasoning for Pinpoint Visual Evidence Seeking](http://arxiv.org/abs/2607.00115v1)
  <details><summary>📄 Abstract</summary>
  This paper explores multi-turn visual reasoning and observes that MLLMs repeatedly fail to localize the target, leading to long, redundant trajectories. We attribute this failure to the entanglement of reasoning and perception within a single model, the MLLM reasons and localizes simultaneously, and inaccurate localization triggers additional reasoning turns that bloat the trajectory. To solve this problem, we propose PixelEyes, a multi-turn visual reasoning agent that explicitly decouples reaso...
  </details>

- **2026-06-30** — Zifan Carl Guo, Laura Ruis, Jacob Andreas et al. — [Introspective Coupling: Self-Explanation Training Tracks Behavioral Change Despite Fixed Supervision](http://arxiv.org/abs/2606.32038v1)
  <details><summary>📄 Abstract</summary>
  When does training language models (LMs) to generate explanations of their predictions yield faithful introspection, rather than superficial imitation? We study LMs trained to explain which features of their inputs influenced their behavior, using models' counterfactual behavior on modified inputs as supervision. Surprisingly, we find that LMs trained on fixed counterfactual explanations derived from earlier checkpoints of themselves, or even from behaviorally similar models in different familie...
  </details>

- **2026-06-30** — Yujie Guo, Yudong Jin, Lingteng Qiu et al. — [PointSplat: Compact Gaussian Splatting via Human-Centric Prediction](http://arxiv.org/abs/2606.32036v1)
  <details><summary>📄 Abstract</summary>
  Producing 3D human representations from input views on the fly is essential for immersive live streaming systems, where representation compactness is as critical as high fidelity given limited computational power and transmission bandwidth. Although recent feed-forward reconstruction methods achieve impressive quality through the view-centric prediction of 3D representations, they repeatedly encode the same subject content across multiple views, leading to significant inter-view redundancy. Our ...
  </details>

- **2026-06-30** — Linfeng Xu, Shengrong Ding, Kailiang Wu — [GQL-Based Physical-Constraint-Preserving High-Order Finite Difference Schemes for Special Relativistic Hydrodynamics in Arbitrary Dimensions](http://arxiv.org/abs/2606.31992v1)
  <details><summary>📄 Abstract</summary>
  High-order accurate simulations of special relativistic hydrodynamics (RHD) are prone to numerical breakdown if intrinsic physical constraints (positive rest-mass density/pressure and subluminal velocity) are violated near strong discontinuities. In this work, we develop a robust and efficient physical-constraint-preserving (PCP) flux-limiting framework for high-order schemes, using finite-difference WENO as a representative example. By leveraging the geometric quasilinearization (GQL) represent...
  </details>

- **2026-06-30** — Yuhao Wang, Mu Qiao, Haiwen Diao et al. — [ERA: Entropy-Guided Visual Token Pruning with Rectified Attention for Efficient MLLMs](http://arxiv.org/abs/2606.31982v1)
  <details><summary>📄 Abstract</summary>
  Multimodal Large Language Models (MLLMs) incur prohibitive inference costs due to long visual token sequences. Training-free visual token reduction provides an efficient solution. However, existing methods distort attention distributions, giving rise to a phenomenon we term Attention Logit Collapse. To address this issue, we propose ERA, an Entropy-guided visual token pruning framework with Rectified Attention for efficient MLLMs. Specifically, ERA comprises three crucial components: Dual-view E...
  </details>

- **2026-06-30** — Qingyun Liu, Jiwen Zhang, Jingyi Hu et al. — [MECoBench: A Systematic Study of Multimodal Agent Collaboration in Embodied Environments](http://arxiv.org/abs/2606.31966v1)
  <details><summary>📄 Abstract</summary>
  Recent multimodal large language models (MLLMs) have strong potential as embodied agents, but their ability to collaborate in visually grounded environments remains underexplored. To address this gap, we introduce MECoBench, a multimodal embodied cooperation benchmark with an evaluation platform spanning diverse real-world tasks, two cooperation structures, and three collaboration modes. Through extensive experiments across various MLLMs, we summarize three key findings: (i) Collaboration genera...
  </details>

- **2026-06-30** — Felipe Tommaselli, Francisco Affonso, Arthur Pompeu et al. — [LeCropFollow: Latent Space Planning for Navigation in Unstructured Crop Fields](http://arxiv.org/abs/2606.31941v1)
  <details><summary>📄 Abstract</summary>
  Unstructured navigational features, such as irregular planting or discontinuities, remain the primary failure mode for under-canopy agricultural robots. Existing geometric approaches often fail in these scenarios because they compress high-dimensional visual data into deterministic spatial references, effectively discarding the uncertainty and semantic context required to navigate ambiguous terrain. To address this, we present LeCropFollow, a visual navigation framework that bypasses explicit ge...
  </details>

- **2026-06-30** — Igor Sedlár — [Non-classical Topological Evidence Logic](http://arxiv.org/abs/2606.31888v1)
  <details><summary>📄 Abstract</summary>
  Topological Evidence Logic (TEL) is a recent approach to epistemic logic that uses topological tools to model coherent epistemic justification. Specifically, a hypothesis is coherently justified if and only if it is entailed by a dense open set. In its simplest form, TEL can be formulated as an extension of S4 with a global modality.  All currently studied forms of TEL are based on classical propositional logic, which has been heavily criticised for misrepresenting the way in which ordinary agen...
  </details>

- **2026-06-30** — Mark Oskin — [Explicit Fuzzy Logic in the Feed-Forward Layer: Self-Forgetting Quantifiers Discover Legible Grammatical-Licensing Detectors](http://arxiv.org/abs/2606.31845v1)
  <details><summary>📄 Abstract</summary>
  A transformer's feed-forward (FFN) sublayer materializes the distinctions attention gathers, yet gives no account of what it computes. In a parameter-neutral replacement, each hidden unit is an explicit fuzzy set operation on sigmoid-bounded [0,1] memberships: intersection A*B and set-difference A*(1-B), the latter a bounded positive negation ("A but not B") that gated/bilinear units lack -- a negation-capable FFN (NC-FFN). On N-bit parity they are the most parameter-efficient reasoning basis at...
  </details>

- **2026-06-30** — Oguzhan Karaahmetoglu, Hyong Kim — [Adaptive Cluster-First Route-Second Decomposition for Industrial-Scale Vehicle Routing](http://arxiv.org/abs/2606.31820v1)
  <details><summary>📄 Abstract</summary>
  Large-scale capacitated vehicle routing problems (CVRPs) are commonly addressed using cluster-first route-second (CFRS) approaches that split a routing instance into smaller, computationally tractable subproblems. Existing splitting methods typically rely on fixed partitioning rules, predefined optimization objectives, or learned policies, which may perform inconsistently across instances exhibiting different spatial, demand, and operational characteristics. In this work, we propose an adaptive ...
  </details>

- **2026-06-30** — Gaochao Song, Haohan Weng, Luo Zhang et al. — [Mesh BDF: Barycentric Dominance Field for 3D Native Mesh Generation](http://arxiv.org/abs/2606.31777v1)
  <details><summary>📄 Abstract</summary>
  Autoregressive (AR) modeling has recently achieved remarkable progress in native 3D mesh generation, largely due to its natural ability to handle variable-length, discrete data structures. However, the inherent constraints of the AR paradigm severely restrict the generated meshes, leading to limited face counts, bounded vertex resolutions, and difficulties in supporting textures. To overcome these bottlenecks, we propose the Barycentric Dominance Field (BDF), a continuous representation defined ...
  </details>

- **2026-06-30** — Yufeng Lin, Jialu Zhang — [ScratchWorld: Evaluating If World Models Compute Executable Consequences](http://arxiv.org/abs/2606.31689v1)
  <details><summary>📄 Abstract</summary>
  World-model evaluations often score a predicted future by overlap with a target state or observation. In sparse-change worlds, this can turn copied persistent state into apparent accuracy. We introduce ScratchWorld, an offline diagnostic benchmark that treats Scratch projects as executable worlds and uses a pinned Scratch VM to produce replay-verified transitions, hidden variables, causal traces, and counterfactual outcomes. ScratchWorld evaluates next-state prediction, long-horizon tracking, ca...
  </details>

- **2026-06-30** — Rahul Bhardwaj, Madhu Gupta — [V-Line Tensor Tomography in a Disk: Theoretical and Numerical Reconstruction](http://arxiv.org/abs/2606.31632v1)
  <details><summary>📄 Abstract</summary>
  In this article, we investigate V-line transforms for symmetric $m$-tensor fields whose support lies inside a disk of radius $R$ and centered at the origin. We provide an explicit characterization of the kernel of the V-line transforms acting on a symmetric $m$-tensor field and derive a new inversion formula using a decomposition result. In addition, we present a comprehensive numerical verification and validation of the inversion algorithms for these V-line transforms for vector fields and symm...
  </details>

- **2026-06-30** — Torsha Majumder, Konstantin Malanchev, Emille E. O. Ishida — [Multi-Scale Contrastive Attention for Light-Curve Representation Learning](http://arxiv.org/abs/2606.31627v1)
  <details><summary>📄 Abstract</summary>
  Current and next-generation time-domain surveys demand automated techniques capable of analyzing millions of light curves, observed in multiple filters, without relying on exhaustive human annotation or scarce spectroscopic follow-up. We present Astra-CLR, an attention-based, self-supervised contrastive learning framework which enables the representation of raw light curves into a highly discriminative latent space. Pre-trained on $\sim$2.1 million unlabeled Zwicky Transient Facility light curve...
  </details>

- **2026-06-30** — Francisco S. Neves, Pedro N. Pereira, Raul D. S. G. Campilho et al. — [Robust Autonomous UAV Landing on Maritime Platforms via Multimodal Agentic AI and Active Wave Compensation](http://arxiv.org/abs/2606.31613v1)
  <details><summary>📄 Abstract</summary>
  Autonomous aerial inspection of marine infrastructure is frequently compromised by stochastic sea states, introducing risks of high-kinetic impacts, post-landing toppling, and sensory occlusion. This paper proposes a decoupled, multi-vehicle landing framework synchronizing an Unmanned Surface Vehicle (USV) equipped with a 3-RPU stabilized platform with a robust Unmanned Aerial Vehicle (UAV). The architecture utilizes two independent Deep Reinforcement Learning (DRL) agents: a Soft Actor-Critic (...
  </details>

- **2026-06-30** — Ajmal M., Abin Roy, Afthab Salam Kanniyan et al. — [CLExEval: A Human-in-the-Loop Framework for Qualitative Evaluation of LLM Clinical Reasoning](http://arxiv.org/abs/2606.31608v1)
  <details><summary>📄 Abstract</summary>
  Large Language Models (LLMs) achieve strong results on many medical benchmarks, but their clinical reasoning remains difficult to evaluate reliably. A central risk is an evaluation illusion: fluent and well-structured explanations can appear clinically convincing even when the final diagnosis is incorrect. We introduce CLExEval, a human-in-the-loop framework for evaluating LLM clinical reasoning under progressive information masking. CLExEval combines 5,600 expert-physician annotations with 200 ...
  </details>

- **2026-06-30** — Tengming Lou, Haiyang Wang, Haijiao Ji et al. — [Eigenstate Transitions, Duality, and Anomalous Diffusion in a Quasiperiodic Qi-Wu-Zhang Chern Insulator](http://arxiv.org/abs/2606.31604v1)
  <details><summary>📄 Abstract</summary>
  Quasiperiodic systems usually interpolate between extended, critical, and localized states as the quasiperiodic modulation is increased. Here we show that the magnetic Qi-Wu-Zhang Chern-insulator model realizes a distinct full-spectrum transition in which localization is avoided. For an irrational magnetic flux, the two-dimensional model reduces to a spinor quasiperiodic chain with a matrix onsite modulation controlled by the hopping amplitude $t_x$. When $|m+2|>t_y$, increasing $t_x$ produces t...
  </details>

- **2026-06-30** — Quan Quan — [Stabilization Learning: A Paradigm Transition Bridging Control Theory and Machine Learning](http://arxiv.org/abs/2606.31562v1)
  <details><summary>📄 Abstract</summary>
  Stabilization learning is an interdisciplinary paradigm that bridges control theory and machine learning. Its core idea is to enable systems to adjust their policies under perturbations or environmental changes through real-time feedback and adaptive mechanisms. It takes stability as its primary goal, distinguishing itself from certificate learning, which focuses on formal proofs, and reinforcement learning, which pursues optimality. It encompasses a range of methods, including Lyapunov-based an...
  </details>

- **2026-06-30** — Stefanie Rinderle-Ma, Juergen Mangler, Johannes Loebbecke et al. — [Design and Implementation of Agentic Orchestrations and Orchestration of Agents](http://arxiv.org/abs/2606.31518v1)
  <details><summary>📄 Abstract</summary>
  Agentic Business Process Management has gained momentum recently. The prospect is that the autonomy of AI agents, i.e., predominantly LLM-based agents, can be balanced with a certain level of robustness, tractability, and traceability through a combination with process technology. In this paper, we provide a classification framework for agentic orchestration options along properties such as task specificity, traceability and tractability, autonomy and reactivity, and correctness assurance and pr...
  </details>

- **2026-06-30** — Michael Fedders, Jakob Schattenfroh, Yanglei Wu et al. — [ILPU: Iterative Laplace-Based Phase Unwrapping via Bi-Level Optimization](http://arxiv.org/abs/2606.31460v1)
  <details><summary>📄 Abstract</summary>
  Phase unwrapping is an essential preprocessing step for phase-based MRI applications, including susceptibility mapping, field mapping, thermometry, and MR elastography. We present Iterative Laplace-Based Phase Unwrapping (ILPU), a bi-level optimization algorithm. In this method, a lower-level solver recovers a continuous phase increment from an incremental Poisson equation using the discrete cosine transform (DCT), while an upper-level solver refines an integer offset map through quality-guided ...
  </details>

- **2026-06-30** — Fengnian Zhang, Tao Huang, Siyu Xu et al. — [Revisiting Parameter Redundancy in Vision-Language-Action Models: Insights from VLM-to-VLA Adaptation](http://arxiv.org/abs/2606.31382v1)
  <details><summary>📄 Abstract</summary>
  Vision-Language-Action (VLA) models have made significant strides in embodied intelligence by integrating the powerful representations of pre-trained Vision-Language Models (VLMs). However, the massive parameter scale of VLAs imposes a heavy computational burden, and these models exhibit extreme sensitivity to parameter pruning. Current paradigms often treat the resulting performance degradation as inevitable, relying on fine-tuning or low-rank corrections to recover efficacy. We challenge this ...
  </details>

- **2026-06-30** — Yujun Lee, Joonhyeok Shin, Hyoeun Kim et al. — [Beyond Binary Instrument QA: Probing Instrument Grounding in Music Audio-Language Models](http://arxiv.org/abs/2606.31338v1)
  <details><summary>📄 Abstract</summary>
  Recent music audio-language models achieve high accuracy on instrument question-answering benchmarks, but it remains unclear whether this reflects robust audio grounding or benchmark-specific shortcuts. In this paper, we introduce an OpenMIC-derived diagnostic benchmark sequence for instrument grounding in music audio-language models, extending binary instrument-presence QA to genre-prior-reduced examples, confusable instrument discrimination, longer audio context, and temporal localization. Acr...
  </details>

- **2026-06-30** — Mohamad Mestoukirdi, Vincent Corlay — [Expected Gain-based Escalation in Vertical Federated Learning](http://arxiv.org/abs/2606.31331v1)
  <details><summary>📄 Abstract</summary>
  Collaborative inference can improve predictive performance by integrating complementary information across agents, but applying collaborative fusion to every sample can incur unnecessary communication and computational overhead. This trade-off is particularly relevant in vertical federated learning (VFL), where clients observe different views of the same sample and fusion typically requires transmitting intermediate representations to a server. We study selective escalation in a two-round VFL in...
  </details>

- **2026-06-30** — Xinming Wang, Fan Tang, Yingli Wei et al. — [A Novel Method for Differential-Algebraic Dynamic Model Discovery in Power Systems: An LLM-Based Multi-Agent Collaborative Framework](http://arxiv.org/abs/2606.31314v1)
  <details><summary>📄 Abstract</summary>
  With large-scale integration of emerging power electronic devices represented by grid-forming inverters, power system dynamics increasingly exhibit strong nonlinearity, multi-timescale coupling, and black-box control logic. These features hinder conventional parameter identification requiring known model structures and structure identification based on predefined function libraries, making complete differential-algebraic dynamic model recovery difficult under weak prior information. To address t...
  </details>

- **2026-06-30** — George Stamatelis, Hui Chen, Henk Henk Wymeersch et al. — [Active Sensing for RIS-Aided Tracking and Power Control: A Hybrid Neuroevolution and Supervised Learning Approach](http://arxiv.org/abs/2607.00056v1)
  <details><summary>📄 Abstract</summary>
  This paper studies energy efficient tracking of power-limited mobile users with the assistance of a Reconfigurable Intelligent Surface (RIS). Since localization pilot transmissions dominate the energy budget of power-constrained devices, we introduce a low-overhead feedback link from the Base Station (BS) to the user to enable dynamic uplink power control. To navigate the discrete and decentralized nature of this active sensing problem, we propose a novel Dual-Agent (DA) deep learning framework ...
  </details>

- **2026-06-30** — Jiangyu Zhao, Yibo Liu, Guoli Wu et al. — [Symmetry-Enforced Ferroelectric Switching of Two-Dimensional Altermagnetism](http://arxiv.org/abs/2606.31241v1)
  <details><summary>📄 Abstract</summary>
  Altermagnetism features strong momentum-dependent spin splitting despite zero net magnetization, offering a transformative platform for next-generation spintronics. However, the nonvolatile and deterministic switching between its two equivalent spin-splitting states remains a fundamental bottleneck. Here, we propose a universal layer-engineering paradigm to achieve symmetry-enforced ferroelectric switching of two-dimensional altermagnetism. By sandwiching a conventional antiferromagnetic monolay...
  </details>

- **2026-06-30** — Apurva Gandhi, Vishwas Suryanarayanan, Raja Hasnain Anwar et al. — [PPT-Eval: A Benchmark for Computer-Use Agents on PowerPoint Tasks](http://arxiv.org/abs/2606.31154v1)
  <details><summary>📄 Abstract</summary>
  Creating and editing slides is a rich, multimodal activity that is ubiquitous in professional and educational settings, making it an ideal testbed for real-world computer-use agents. Microsoft PowerPoint is among the most widely adopted and feature-rich environments for presentation creation. We introduce PPT-Eval, a benchmark of 120 PowerPoint tasks across 12 files that cover both content creation and presentation editing scenarios, organized by difficulty. A central challenge in this domain is...
  </details>

- **2026-06-30** — M. Abdullah Khokhar, Malgorzata M. O'Reilly, Richard Turner — [Level-dependent quasi-birth-and-death processes: Application to cost analysis of multi-server systems](http://arxiv.org/abs/2606.31133v1)
  <details><summary>📄 Abstract</summary>
  Analysing costs is crucial for optimising the operational efficiency and resource allocation in systems evolving under uncertainty. In this paper, we study the distribution of costs associated with the evolution of level-dependent quasi-birth-and-death (LD-QBD) processes, which are useful in modelling many multi-server systems. We derive analytical expressions for the Laplace-Stieltjes transforms (LSTs) of the distribution of total costs accumulated during the times the LD-QBD processes spend in...
  </details>

- **2026-06-30** — Mustafa Chasmai, Aaron Sun, Subhransu Maji — [WildProp: Visual Estimation of Wildlife Body Proportions at Scale](http://arxiv.org/abs/2606.31125v1)
  <details><summary>📄 Abstract</summary>
  Population-level morphometric measurements underpin ecological and evolutionary studies but traditionally require controlled imaging or physical specimen handling, limiting scalability. We present WildProp, a training-free framework that estimates wildlife body proportion distributions directly from large-scale, unconstrained image repositories. We cast morphometric estimation as a retrieval-driven correspondence problem: given a single user-annotated canonical image, WildProp performs pose-awar...
  </details>

- **2026-06-30** — Meng Yang, Zizhuo Li, Linfeng Tang et al. — [AnyMatch: Supercharging Universal Multi-Modal Image Matching with Large-Scale Single-View Images](http://arxiv.org/abs/2606.31077v2)
  <details><summary>📄 Abstract</summary>
  Multi-modal image matching is essential for visual localization and multi-sensor fusion, but it is hindered by the scarcity of large-scale training data with precise geometric annotations. Existing real-world datasets suffer from prohibitive costs, limited scene diversity, and errors in SfM-MVS pipelines, while synthetic methods struggle to maintain 3D geometric consistency or achieve photorealistic appearance. To address this, we propose AnyMatch, a novel framework that leverages abundant, easi...
  </details>

- **2026-06-30** — Naihao Deng, Yilun Zhu, Joan Nwatu et al. — [Wait, am I Being Fair? Characterizing Deductive Stereotyping and Mitigating It with Fair-GCG](http://arxiv.org/abs/2606.30989v1)
  <details><summary>📄 Abstract</summary>
  Warning: This paper contains several toxic and offensive statements. While reasoning generally improves fairness in recent large language models (LLMs), failures persist. In this work, we identify a failure mode, deductive stereotyping, in which models apply population-level statistical regularities to individual cases, producing logically coherent yet socially biased inferences. We provide a statistical interpretation of this phenomenon. To steer models toward fairness-aware reasoning, we propo...
  </details>


### 📂 watermark
*水印与溯源 / Watermarking & Provenance* — 8 papers

- **2026-07-02** — Ziyun Qiao, Yue Min, Ruining Chen et al. — [HERMES: A Multi-Granularity Labeling Substrate for Pre-training Data Mixtures](http://arxiv.org/abs/2607.02266v1)
  <details><summary>📄 Abstract</summary>
  Most data-mixing methods assume the corpus has already been partitioned into groups, and the choice of those groups determines what a mixer can express. Existing labels, including provenance, topic or format taxonomies, and flat embedding clusters, commit to one semantic axis at one granularity; changing the resolution rebuilds the labels. We argue the bottleneck is the label system, not the mixer, and provide a hierarchical one. HERMES is a data-derived labeling substrate: a Learned Semantic Tr...
  </details>

- **2026-07-02** — Xue Qin, Simin Luan, Cong Yang et al. — [Episodic-to-Semantic Consolidation Without Identity Drift](http://arxiv.org/abs/2607.01988v1)
  <details><summary>📄 Abstract</summary>
  Long-running adaptive intelligent agents face a structural tension between knowledge consolidation and information integrity. Memory consolidation is conventionally treated as an agent-changing operation: a model is fine-tuned, a prompt rewritten, a policy distilled, or a reflection appended to the context that governs future behaviour. In regulated autonomic deployment this is a liability because the agent operates under commitments and audit contracts that bind to a specific, cryptographically...
  </details>

- **2026-07-01** — Dangxing Chen, Pengzhan Guo — [Shapley in Context: Explaining Financial Language with Domain Expertise](http://arxiv.org/abs/2607.00856v1)
  <details><summary>📄 Abstract</summary>
  In recent years, large language models have achieved remarkable success and have seen growing adoption in financial applications. At the same time, explainability remains critical in finance, a domain characterized by high stakes and strict regulatory requirements. Although numerous methods have been proposed to explain black box machine learning models, the majority of these approaches are designed for general purpose tasks and do not incorporate domain specific knowledge. In this work, we stud...
  </details>

- **2026-07-01** — Jeroen Janssen — [From Runtime Records to Legal Findings: An Evidentiary-Adequacy Criterion for Agentic AI Oversight](http://arxiv.org/abs/2607.00941v1)
  <details><summary>📄 Abstract</summary>
  Agentic AI systems generate runtime records, logs, traces, and audit artefacts, but the existence or integrity of such records does not by itself establish that legally operative oversight findings can be recovered from them. This technical report defines an evidentiary-adequacy criterion for a bounded class of determinations: binary findings of fact about specific events and their relations, such as whether protected data crossed a boundary, whether a human could intervene, whether an informati...
  </details>

- **2026-07-01** — Dan Ley, Giang Nguyen, Himabindu Lakkaraju et al. — [Prototype Language Models](http://arxiv.org/abs/2607.00510v1)
  <details><summary>📄 Abstract</summary>
  Knowing which training examples drive outputs is fundamental to auditing, correcting, and understanding language models, yet for modern LLMs this remains expensive, approximate, and largely post-hoc. Standard language models generate tokens through a dense network pathway, causing training data's influence to be distributed across parameters rather than organized along explicit, traceable components. We introduce a prototype language model architecture, Prototypes for Interpretable Sequence Mode...
  </details>

- **2026-06-30** — Hui Gong — [Agent-to-Agent Finance: Blockchain Payments and Trust Infrastructure for Autonomous AI Agents](http://arxiv.org/abs/2607.00245v1)
  <details><summary>📄 Abstract</summary>
  Autonomous AI agents are beginning to occupy a position between analytical tools and transacting counterparties. They can interpret goals, call external tools, negotiate with other agents, access data and computation, and in some settings initiate payments or blockchain transactions. This development creates a distinct problem for financial markets: if software agents can act economically, market participants need infrastructure for identity, authorisation, payment, verification, reputation and ...
  </details>

- **2026-06-30** — Philippe Chlenski, Zachariah Carmichael, Ayush Warikoo et al. — [Surrogate Fidelity: When Can Open LLMs Explain Closed Ones?](http://arxiv.org/abs/2606.32008v1)
  <details><summary>📄 Abstract</summary>
  Mechanistic interpretability (MI) requires full access to model internals, yet the APIs for most widely deployed language models at best expose log-probabilities over output tokens. This creates a surrogate problem: when do measurements made on open models allow us to make claims about a closed model? We evaluate surrogate fidelity at the prediction, attribution, and representation levels. For binary classification tasks, log-odds provide an API-compatible scalar readout of the model's represent...
  </details>

- **2026-06-30** — Ke Zhang, Patricio Gallardo Candela, Sudhir Murthy et al. — [Beyond Compilation: Evaluating Faithful Natural-Language-to-Lean Statement Formalization](http://arxiv.org/abs/2606.31002v1)
  <details><summary>📄 Abstract</summary>
  Theorem-proving benchmarks evaluate proof search against fixed formal statements, but natural-language-to-Lean formalization must generate the formal statement itself. In this setting, compilation is only a validity check: a Lean declaration may type-check while omitting hypotheses, changing domains, or expressing a vacuous claim. We study faithful statement formalization as both an evaluation problem and a bottleneck-attribution problem. On a 400-entry graduate-level benchmark spanning real ana...
  </details>


### 📂 unlearning
*机器遗忘 / Machine Unlearning* — 1 papers

- **2026-06-30** — Noah Scharrenberg, Chang Sun — [Probing Stylistic Appropriation using Large Language Models: An Evaluation Framework for Copyright Infringement under EU Law](http://arxiv.org/abs/2606.31250v1)
  <details><summary>📄 Abstract</summary>
  Large language models (LLM) trained on web-scale corpora generate output that may infringe copyright, yet existing technical safeguards focus narrowly on verbatim memorisation. EU copyright doctrine applies a broader standards: substantial similarity, which extends to stylistic choices, narrative structure, and creative elaboration. This mismatch between what current methods detect and what the law protects leaves a significant compliance gap. We introduce PSALM, an LLM-as-a-judge framework that...
  </details>


### 📂 agent-safety
*Agent 安全框架 / Agent Safety Frameworks* — 2 papers

- **2026-07-02** — Gabriel Hurtado — [Has This Checkpoint Been Abliterated? A Two-Signal Audit and Its Failure Map](http://arxiv.org/abs/2607.01854v1)
  <details><summary>📄 Abstract</summary>
  Can a platform tell, before deployment, whether an open-weight checkpoint has had its refusal mechanism stripped? Runtime guards cannot: they score generations, not the artifact. We combine two cheap internal signals, a reference-anchored activation refusal-gap and a weight-recovery energy of the base-to-candidate weight difference, into a threshold-free checkpoint audit. The two are negatively correlated and label-complementary: the gap supplies refusal-specificity and the weight energy supplie...
  </details>

- **2026-07-01** — Richard Kang, Vincent Wang — [Registry-Governed Agent Lifecycle:Completing EDDOps with Evaluation-DrivenRegistration, Promotion, and Retirement on AWS AgentCore](http://arxiv.org/abs/2607.00345v1)
  <details><summary>📄 Abstract</summary>
  Enterprise adoption of LLM agents requires model selection methods that balance quality, reliability, safety, latency, and cost. Evaluation-Driven Development and Operations (EDDOps) positions evaluation as a continuous governing function across the agent lifecycle rather than a terminal checkpoint. This paper presents a practitioner-oriented instantiation of EDDOps on AWS Bedrock AgentCore and proposes a cost-to-performance framework for selecting foundation models in enterprise agent architect...
  </details>


### 📂 benchmark
*安全评测与基准 / Safety Benchmarks & Evaluation* — 1 papers

- **2026-07-02** — Joshua Penman — [Epistemic Goggles: A Pretrained Module that Induces an Epistemic Frame via Gradient Editing](http://arxiv.org/abs/2607.01690v1)
  <details><summary>📄 Abstract</summary>
  Finetuning a language model on documents that are explicitly annotated as fictional results in a model that still actually believes the documents' core claims, an effect known as Negation Neglect. In our evaluations, models trained on documents prefixed and suffixed with such annotations correctly identify the relevant claims as fictional only about 9% of the time. To address this, we introduce Goggles, a learned module that intervenes on the finetuning gradient rather than the data. During supe...
  </details>


### 📂 survey
*综述与系统化 / Surveys & Systematization* — 8 papers

- **2026-07-02** — Manuel Alonso-Carracedo, Ruben Fernandez-Boullon, Pedro Celard et al. — [Automated grading of Linux/bash examinations using large language models: a four-level cognitive taxonomy approach](http://arxiv.org/abs/2607.02432v1)
  <details><summary>📄 Abstract</summary>
  Scalable and reliable grading of command-line examinations remains a challenge in computing education, where rising enrolments make manual marking difficult and rule-based autograders cannot handle partial credit, equivalent solutions, or syntactic variation. This paper evaluates whether four frontier Large Language Models (GPT, Claude Opus, Gemini, and GLM) can approximate expert judgment when grading short Linux/bash command responses. The study adopts a four-level cognitive taxonomy that comb...
  </details>

- **2026-07-02** — Jose Afonso, Stergios Amarantidis, Stas Shabala et al. — [The Road to Identifying the Earliest Radio-Powerful AGN with the SKA](http://arxiv.org/abs/2607.02366v1)
  <details><summary>📄 Abstract</summary>
  The Epoch of Reionization (EoR) is one of the most pivotal frontiers in modern astrophysics, marking the emergence of the first galaxies, stars, and supermassive black holes (SMBHs). Despite insights from the Atacama Large Millimetre/submillimetre Array and the James Webb Space Telescope, we still struggle to explain how $\sim10^{9}$ M$_\odot$ SMBHs powering luminous active galactic nuclei (AGN) already exist by $z\sim7$. The recent discovery of powerful radio emission from some of these early A...
  </details>

- **2026-07-01** — Elias Najarro, Ane Espeseth, Eleni Nisioti et al. — [Conversable Complexity: Agentic LLM Collectives as Interpretable Substrates](http://arxiv.org/abs/2607.01047v1)
  <details><summary>📄 Abstract</summary>
  Complexity and interpretability rarely coincide: systems rich enough for complex behaviours to emerge are usually too opaque to question, while transparent ones are too simple for anything complex to emerge. A single large language model (LLM) is a static artefact, hardly exhibiting any of the emergent properties we associate with life. This changes through interaction: populations of LLMs display emergent dynamics absent from isolated models. Furthermore, LLMs can be endowed with persistent mem...
  </details>

- **2026-07-01** — Yanan Wang, Wen Li, Yibin Ying et al. — [GEAR-Seg: A Grounded Explainable Agent for Reasoning Segmentation and Data Engine](http://arxiv.org/abs/2607.00544v1)
  <details><summary>📄 Abstract</summary>
  Reasoning segmentation requires localizing targets based on complex, implicit queries. Current end-to-end models typically entangle perception and deduction into an opaque black box, severely limiting interpretability and scalability. To address this, we propose GEAR-Seg (Grounded Explainable Agent for Reasoning Segmentation), an explicitly decoupled agent that shifts the paradigm by translating visual pixels into dense, attribute-rich text. By decoupling class-agnostic segmentation, semantic de...
  </details>

- **2026-07-01** — Daniel Armstrong, Maarten Dobbelaere, Valentas Olikauskas et al. — [Agentic generation of verifiable rules for deterministic, self-expanding reaction classification](http://arxiv.org/abs/2607.01061v1)
  <details><summary>📄 Abstract</summary>
  Computer-assisted synthesis planning breaks target molecules into accessible precursors using large libraries of reaction rules that assign each transformation a deterministic, interpretable label. But chemistry is long-tailed, making manual encoding intractable, and existing tools rely on fixed rulesets that cannot adapt to new chemistries. Here we present a fully automated pipeline in which a multi-agent framework of large language models (LLMs) classifies reactions and writes the rules themse...
  </details>

- **2026-07-01** — Zhiyue Xu, Fandi Meng, Kaijie Xu et al. — [AI Native Games: A Survey and Roadmap](http://arxiv.org/abs/2607.00527v1)
  <details><summary>📄 Abstract</summary>
  Generative AI now enables games to produce dialogue, quests, characters, images, and worlds at runtime. Yet generation alone does not make a game AI-native, nor does it guarantee playability. This paper defines AI-native games by whether runtime generative AI is constitutive of the core loop: if the AI component were removed or trivially replaced, the central form of play would collapse or become fundamentally different. This counterfactual criterion separates AI-native games from AI-augmented g...
  </details>

- **2026-06-30** — Alessio Taranto, Gabriele Rodeghiero, Luca Rosignoli et al. — [Modeling of the diffuse background produced by the Vera C. Rubin Observatory M2 baffle scattered light](http://arxiv.org/abs/2606.31793v1)
  <details><summary>📄 Abstract</summary>
  The Vera C. Rubin Observatory, with its unprecedented field of view and fast focal ratio, will survey the entire sky every 3.5 nights. This unique capacity requires dealing with off axis light that can produce stray light artefacts on the images. The secondary mirror (M2) baffle restricts the light that reaches the LSSTCam detector and it contributes to shaping the inner edge of the telescope optical pupil. This work studies the contribution to the background from the light scattered by the M2 b...
  </details>

- **2026-06-30** — Ahmet Kaplan — [Optimization Algorithms for Joint OFDM Waveform Design and RIS Configuration in 6G Networks: From Convex Relaxation to Foundation Models](http://arxiv.org/abs/2606.31334v1)
  <details><summary>📄 Abstract</summary>
  Joint OFDM-RIS optimization for 6G is a mixed-integer nonlinear programming (MINLP) problem covering sum-rate maximization, energy efficiency, max-min fairness, and peak-to-average power ratio (PAPR)-constrained objectives. Seventy-eight joint OFDM-RIS optimization works published between 2021 and 2026 are surveyed. No standardized benchmark exists, and cross-paper comparisons remain infeasible. This survey classifies these works into four paradigms: (I) model-based convex relaxation, (II) heuri...
  </details>


### 📂 other
*其他安全相关 / Other Security-Related* — 163 papers

- **2026-07-02** — Shahreen Salim, Klaus Mueller — [When Do LLM Personas Support Visualization Design? A Cross-Model Study of Color Assignment and Chart Choice](http://arxiv.org/abs/2607.02455v1)
  <details><summary>📄 Abstract</summary>
  Large language model personas are increasingly used to approximate diverse users during early-stage visualization design, but it remains unclear whether persona-conditioned outputs reflect stable personality effects or artifacts of model choice and task framing. We examine this question across two visualization-relevant tasks: color assignment for abstract and concrete concepts, and chart-idiom preference ratings across task contexts. Using 43 Big Five profiles across GPT-4o-mini, GPT-4.1-mini, ...
  </details>

- **2026-07-02** — Zhilin Wang, Han Song, Runzhe Zhan et al. — [EvoPolicyGym: Evaluating Autonomous Policy Evolution in Interactive Environments](http://arxiv.org/abs/2607.02440v1)
  <details><summary>📄 Abstract</summary>
  Autonomous agents are increasingly expected to improve executable policies through feedback, yet existing evaluations often collapse this process into a final score or confound it with open-ended software-engineering progress. We introduce Autonomous Policy Evolution, a controlled evaluation setting in which a harness-model agent repeatedly edits an executable policy system under a fixed interaction budget. We instantiate this setting in EvoPolicyGym, a benchmark built from compact interactive R...
  </details>

- **2026-07-02** — Francesca Pistilli, Simone Alberto Peirone, Giuseppe Averta — [Learning to Evolve Scenes: Reasoning about Human Activities with Scene Graphs](http://arxiv.org/abs/2607.02425v1)
  <details><summary>📄 Abstract</summary>
  Understanding human behavior while interacting with the surrounding world is crucial for many applications of embodied AI. First-person videos are particularly informative for this problem, as they well capture how activities reshape the scene over time. However, existing approaches often rely on implicit visual or language-aligned representations, disregarding structured reasoning over the scene dynamic. We argue that explicit, compositional and editable representations of human-environment int...
  </details>

- **2026-07-02** — Mohamed Shamseldein — [Generative Autonomous Grid Control: Integrating Decision Transformers with a Two-Stage Safety Stack](http://arxiv.org/abs/2607.02379v1)
  <details><summary>📄 Abstract</summary>
  The displacement of synchronous generation by inverter-based resources is accelerating power system frequency dynamics beyond the response capability of conventional automatic generation control. This paper presents Autonomous Grid Generation Control with Decision Transformers, a framework coupling an offline-trained Decision Transformer with a twostage symbolic safety stack for secondary frequency control. The Decision Transformer learns a conditional dispatch policy from offline supervisory co...
  </details>

- **2026-07-02** — Uwe M. Borghoff, Paolo Bottoni, Remo Pareschi — [Hardware-Enforced Semantic Coordination for Safety-Critical Real-Time Autonomous Systems](http://arxiv.org/abs/2607.02376v1)
  <details><summary>📄 Abstract</summary>
  Recent advances in agentic AI are producing increasingly complex autonomous systems that integrate large language models, world models, optimization engines, specialized neural architectures, autonomous platforms, and human operators. While much current research focuses on improving reasoning capabilities, safety-critical real-time deployment also requires bounded and verifiable coordination among heterogeneous components operating concurrently under uncertainty. Software-mediated coordination p...
  </details>

- **2026-07-02** — Batu Guan, Zirui Wang, Shaohua Li — [Understanding Agent-Based Patching of Compiler Missed Optimizations](http://arxiv.org/abs/2607.02370v1)
  <details><summary>📄 Abstract</summary>
  Compiler missed optimizations refer to cases in which compilers failed to optimize certain code. It takes many compiler developers' efforts to implement or patch such missed optimizations. In this paper, we present a systematic study of how well agents patch compiler missed optimizations. We identify a significant challenge that patching a missed optimization requires more than just fixing the reported case, and instead requires generalizing to similar cases. We construct a benchmark of real-wor...
  </details>

- **2026-07-02** — Ohad Eitan, Idit Keidar, Ehud Shapiro — [Securing People and their Machines Against Major Faults](http://arxiv.org/abs/2607.02304v1)
  <details><summary>📄 Abstract</summary>
  We consider grassroots platforms -- distributed systems of agents consisting of people identified by self-chosen public keys and their machines (smartphones) -- and wish to make them secure against \emph{major faults}: the loss of their private keys and/or their smartphones. As grassroots platforms have no global resource to rely on for recovery, our peer-based solution is based on: (\ia) \emph{a grassroots social graph} in which agents establish and maintain friendships; (\ib) \emph{identity cu...
  </details>

- **2026-07-02** — Fatima Elsheimy, Mohammad Mussadiq Jalalzai, Tobias Klenze et al. — [Cadence: Extreme Pipelining with Multiple Concurrent Proposers](http://arxiv.org/abs/2607.02275v1)
  <details><summary>📄 Abstract</summary>
  We present Cadence, a Byzantine fault-tolerant multi-proposer consensus protocol with arbitrarily low block intervals, optimal resilience, and optimal fast-path latency. Cadence divides time into equally spaced slots, one block per slot, each finalized in its own consensus instance. Blocks do not build directly on their predecessor, so instances run independently and none waits for an earlier block to finish or propagate; we call this extreme pipelining, decoupling the block interval from networ...
  </details>

- **2026-07-02** — Rintaro Otsubo, Ryo Fujii, Reina Ishikawa et al. — [AnyGroundBench: A Specialized-Domain Benchmark for Video Grounding in Vision-Language Models](http://arxiv.org/abs/2607.02269v1)
  <details><summary>📄 Abstract</summary>
  Vision-Language Models (VLMs) have demonstrated immense promise in Spatio-Temporal Video Grounding (STVG). However, current evaluation protocols are largely confined to zero-shot assessments on general, daily-life benchmarks. This creates a critical disconnect from real-world applications in specialized fields, where models inevitably encounter rare visual concepts and complex spatio-temporal dynamics. Since exhaustive pre-training across infinite data distributions is infeasible, the ability to...
  </details>

- **2026-07-02** — Zhanming Shen, Jintao Tong, Shaotian Yan et al. — [Purified OPSD: On-Policy Self-Distillation Without Losing How to Think](http://arxiv.org/abs/2607.02234v1)
  <details><summary>📄 Abstract</summary>
  On-policy self-distillation (OPSD) has emerged as a promising paradigm for improving LLM reasoning, where a privileged teacher with access to reference solutions provides token-level supervision on the student's own generated trajectories. However, we find that OPSD consistently fails on long chain-of-thought (long-CoT) reasoning models, yielding at best marginal gains while destabilizing the reflective reasoning capability these models depend on. Through a novel decomposition of the teacher's s...
  </details>

- **2026-07-02** — Sampreeti Bhattacharya, Arkaprava Roy — [An Additive MLP-GNN Framework for Characterizing Chemical and Structural Contributions to Aqueous Solubility](http://arxiv.org/abs/2607.02212v1)
  <details><summary>📄 Abstract</summary>
  Aqueous solubility is a key property in early-stage drug discovery, but most predictive models merge physicochemical descriptors and molecular graph information into a single representation, obscuring whether a prediction is driven by global chemistry, molecular structure, or both. We present an additive deep-learning framework that keeps these two sources of information separate throughout training: physicochemical descriptors are encoded by a multilayer perceptron (the chemical branch) and mol...
  </details>

- **2026-07-02** — Jijie Zhang, Zhe Ren, Quan Zhang et al. — [Bayesian Sparse Low-Rank Adaptation for Large Language Model Uncertainty Estimation](http://arxiv.org/abs/2607.02182v1)
  <details><summary>📄 Abstract</summary>
  Large language models (LLMs) exhibit remarkable reasoning capabilities, but their task-specific fine-tuning is notoriously plagued by overconfidence, severely hindering trustworthy deployment. We propose Data-Adaptive Lower-Rank Adaptation (DALorRA), a simple and effective variational Bayesian sparse framework that shifts the paradigm of uncertainty quantification from the dense parameter space to the lightweight rank level of low-rank adaptation (LoRA). With the insight that LoRA essentially ag...
  </details>

- **2026-07-02** — Samiha A. Ismail, Fan X. Chen, Ali Merali — [A rubric-based controlled comparison of frontier language models on expert-authored clinical reasoning tasks](http://arxiv.org/abs/2607.02175v1)
  <details><summary>📄 Abstract</summary>
  Multiple-choice medical benchmarks are increasingly saturated, and recent rubric-based evaluations such as HealthBench have shown that open-ended clinical performance is far from solved - its "Hard" subset top score remains 32%. We present a small, deliberately difficult evaluation dataset of five clinician-authored clinical scenarios spanning four specialties (anaesthesia, internal/family medicine, emergency medicine, and obstetrics), each accompanied by an atomic, weighted, MECE rubric (25-62 ...
  </details>

- **2026-07-02** — Gianmarco Spinaci, Lukas Klic, Giovanni Colavizza — [EduArt: An educational-level benchmark for evaluating art history knowledge in large language models](http://arxiv.org/abs/2607.02007v1)
  <details><summary>📄 Abstract</summary>
  Large language models now score near ceiling on general benchmarks, but these aggregate measures reveal little about how models behave within single disciplines. Existing art-focused evaluations rely on synthetic questions and rarely report item-level properties. This paper introduces EduArt, an educational-level benchmark for art-historical knowledge and visual reasoning in multimodal LLMs. EduArt comprises 871 human-authored questions from Italian secondary-school exercises and US Advanced Pla...
  </details>

- **2026-07-02** — Weichen Zhou, Yawen Zou, Chunzhi Gu et al. — [Understanding Geometric Representations in Self-Supervised Vision Transformers via Subspace Intervention](http://arxiv.org/abs/2607.01987v1)
  <details><summary>📄 Abstract</summary>
  We introduce a controlled subspace intervention framework to investigate how self-supervised Vision Transformers (ViTs) encode dense geometric information. While linear probing is widely used to assess geometric representations, it treats features as a black box, failing to disentangle the underlying topology. To address this issue, we decompose the weights of converged linear probes to isolate the low-rank subspaces containing explicit geometric signals using Singular Value Decomposition (SVD)....
  </details>

- **2026-07-02** — Shahbaz Siddeeq, Mateen Abbasi, Jussi Rasku et al. — [Epic-Organized vs. Requirement-Aligned Gherkin: An Empirical Evaluation of LLM-Based Acceptance Criteria Generation](http://arxiv.org/abs/2607.01980v1)
  <details><summary>📄 Abstract</summary>
  Automated authoring of Gherkin Behavior-Driven Development (BDD) acceptance criteria remains a manual bottleneck in requirements engineering. This study investigates whether epic-organized LLM-generated Gherkin produces higher quality and coverage than requirement-aligned generation. We compare our Timeless (an epic-organized LLM pipeline) approach against a naive large language model (LLM) baseline on four requirements documents (107 requirements) from the PURE dataset. Evaluation covers struct...
  </details>

- **2026-07-02** — Massimiliano Berti, Alberto Maspero, Antonio Milosh Radakovic — [McLean resonances and $3d$ spectral instability of Stokes waves](http://arxiv.org/abs/2607.01939v1)
  <details><summary>📄 Abstract</summary>
  The spectral instability of traveling periodic water waves has been investigated for more than sixty years, since the seminal discovery of Benjamin and Feir. Despite an extensive literature, no rigorous theory has been available for arbitrary three-dimensional -- longitudinal and transverse -- perturbations. We establish the first rigorous description of the $3d $ unstable spectrum of small-amplitude gravity Stokes waves in deep water in a full neighborhood of the McLean resonant curves. Our res...
  </details>

- **2026-07-02** — Nicholas Tagliapietra, Gian Lorenzo Marchioni, Moritz Willig et al. — [CausalSteward: An Agentic Divide-Conquer-Combine Copilot for Causal Discovery](http://arxiv.org/abs/2607.01936v1)
  <details><summary>📄 Abstract</summary>
  Learning causal models from high-dimensional data is a significant challenge, particularly in real-world settings where violations of core assumptions lead to causal identifiability issues. Although massive amounts of prior knowledge are available, and contain valuable causal information, effectively integrating this knowledge into the causal discovery process remains an open problem. We introduce CausalSTeward (CAST), a novel human-in-the-loop framework for interactively assembling large causal...
  </details>

- **2026-07-02** — Ahin Lee, Sehyun Yun, Taesik Gong — [EPnG: Adaptive Expert Prune-and-Grow for Parameter-Efficient MoE Fine-tuning](http://arxiv.org/abs/2607.01789v1)
  <details><summary>📄 Abstract</summary>
  Mixture-of-Experts (MoE) models scale efficiently but remain costly to adapt due to redundant experts and uniform parameter allocation. Existing parameter-efficient fine-tuning (PEFT) methods such as LoRA ignore MoE routing dynamics, leading to suboptimal resource use. We propose EPnG, an adaptive prune-and-grow framework that reallocates LoRA capacity based on expert importance derived from router gate probabilities. EPnG prunes under-utilized experts and expands high-importance experts via ran...
  </details>

- **2026-07-02** — Xinyuan Song, Zekun Cai — [Repair the Amplifier, Not the Symptom: Stable World-Model Correction for Agent Rollouts](http://arxiv.org/abs/2607.01767v1)
  <details><summary>📄 Abstract</summary>
  As agent planning moves from short tool chains toward persistent workflows with thousands or tens of thousands of steps, failures will occur inside large planning graphs rather than in isolated predictions. Replanning the entire graph after every mistake is neither computationally realistic nor desirable: full-graph replay consumes large context budgets, exposes the LLM to many irrelevant symptoms, and can degrade long-context retrieval. This paper studies the missing component in such systems: ...
  </details>

- **2026-07-02** — Minkuk Kim, Suyong Yun, Young Tae Kim et al. — [ReQuest: Rethinking-based Question-Aware Frame Selection for Long-Form Video QA](http://arxiv.org/abs/2607.01737v1)
  <details><summary>📄 Abstract</summary>
  Recent multimodal large language models (MLLMs) have substantially advanced video understanding, yet long-form video QA remains challenging under fixed input token budgets, where uniform sampling can be inefficient for evidence localization. We propose ReQuest , an uncertainty-driven, question-adaptive keyframe selection pipeline that aligns question intent with relevant video content through selective computation. ReQuest integrates (i) a lightweight question-aware selector distilled from MLLM-...
  </details>

- **2026-07-02** — Ruchao Fan, Yiming Wang, Rui Zhao et al. — [Rethinking Speech-LLM Integration for ASR: Effective Joint Speech-Text Training by Interleaving](http://arxiv.org/abs/2607.01733v1)
  <details><summary>📄 Abstract</summary>
  Speech-LLM integration has shown promising results by leveraging extensive textual pretraining, yet its specific benefits for automatic speech recognition (ASR) remain unclear. We observe that as supervised ASR training data increases, the contribution of LLM priors becomes less evident, and simple speech-text joint training under-utilizes textual knowledge. We therefore propose Joint Speech-Text Interleaved Pretraining (JSTIP), an ASR-oriented pretraining strategy that constructs word-level and...
  </details>

- **2026-07-02** — Zhaoyan Sun, Shan Zhong, Daizhou Wen et al. — [AgenticDataBench: A Comprehensive Benchmark for Data Agents](http://arxiv.org/abs/2607.01647v1)
  <details><summary>📄 Abstract</summary>
  Data science aims to derive actionable insights from heterogeneous raw data, unlocking the value of the massive amounts of data generated in modern society. Automating this process is essential to reducing labor-intensive efforts for data scientists and enabling scalable data-driven applications. Recently, large language model (LLM)-based data agents have emerged as a promising solution to automate data science workflows. However, the field lacks comprehensive benchmarks to rigorously evaluate t...
  </details>

- **2026-07-02** — Shuai Tian, Yupeng Zheng, Yuhang Zheng et al. — [VT-WAM: Visual-Tactile World Action Model for Contact-Rich Manipulation](http://arxiv.org/abs/2607.02503v1)
  <details><summary>📄 Abstract</summary>
  Contact-rich manipulation requires policies to react to local deformation, pressure, slip, and friction, yet these cues are temporally sparse and often invisible in visual observations. Existing visual-tactile policies usually feed tactile observations directly into action prediction, but rarely model tactile deformation dynamics during action generation. In this paper, we introduce VT-WAM, a Visual-Tactile World Action Model that jointly learns future visual prediction, tactile deformation pred...
  </details>

- **2026-07-02** — Kyobin Choo, Youngmin Kim, Hyunkyung Han et al. — [QWERTY: Training-Free Motion Control via Query-Warped Video Diffusion Transformers](http://arxiv.org/abs/2607.01869v1)
  <details><summary>📄 Abstract</summary>
  Video diffusion transformers (DiTs) generate high-fidelity and temporally coherent videos, yet motion control remains implicit, primarily relying on text prompts. As a result, achieving desired motion often requires extensive prompt engineering and repeated resampling. While fine-tuning models with additional spatial prompts (e.g., bounding boxes or point trajectories) enables explicit control, it demands substantial data curation and computation, and may compromise the generative capabilities o...
  </details>

- **2026-07-02** — Wentao Zhang, Liliana Hotsko, Woojeong Kim et al. — [Program-as-Weights: A Programming Paradigm for Fuzzy Functions](http://arxiv.org/abs/2607.02512v1)
  <details><summary>📄 Abstract</summary>
  Many everyday programming tasks resist clean rule-based implementation, such as alerting on important log lines, repairing malformed JSON, or ranking search results by intent, and are increasingly outsourced to large language model APIs at the cost of locality, reproducibility, and price. We propose fuzzy-function programming: compiling such a function from a natural-language specification into a compact, locally-executable neural artifact. We instantiate this paradigm with Program-as-Weights (P...
  </details>

- **2026-07-02** — Donghyun Lee, Jitesh Chavan, Duy Nguyen et al. — [OrbitQuant: Data-Agnostic Quantization for Image and Video Diffusion Transformers](http://arxiv.org/abs/2607.02461v1)
  <details><summary>📄 Abstract</summary>
  Diffusion transformers (DiTs) achieve state-of-the-art image and video generation, but their multi-step sampling and growing parameter count make inference expensive. Post-training quantization (PTQ) is the natural remedy, yet DiT activations shift across timesteps, prompts, and guidance branches, forcing prior methods to re-fit calibration data for every new checkpoint or modality. We present OrbitQuant, a data-agnostic weight-activation quantizer that bypasses range estimation by quantizing in...
  </details>

- **2026-07-02** — Nina Begus — [World Wide Models: Literary Tools for Cultural AI](http://arxiv.org/abs/2607.02369v1)
  <details><summary>📄 Abstract</summary>
  LLMs stage a new form of cultural encounter that is massive, automated, and monolingual. Literary disciplines have always negotiated cultural struggles with comparative reading of literature, narratological and poetic analysis, critical theory, world literature, and translation. These tools have now become indispensable for building culturally literate AI. The essay develops a layered framework toward more nuanced textual models and pluralistic interpretations of AI, emphasizing the natural inte...
  </details>

- **2026-07-02** — Yuan Ding, Wenjing Liu, Xin Chen et al. — [Facility Location Game with Envy Ratio](http://arxiv.org/abs/2607.02330v1)
  <details><summary>📄 Abstract</summary>
  We study the one-facility location game on a real line with a new objective called envy ratio. The envy ratio, which is adopted from fair division and represents the egalitarianism, is defined as the maximum over the ratios between any two agents' utilities. We are interested in strategyproof or group strategyproof mechanisms that can minimize the envy ratio objective.   We consider the model in two settings that can capture natural scenarios: the facility location and all the agents' locations ...
  </details>

- **2026-07-02** — Andrea Mazzolini, Leonardo Agasso, Filippo Valle et al. — [Alternative routes to universal diversity scaling in component systems: from proteomes to large language models](http://arxiv.org/abs/2607.02221v1)
  <details><summary>📄 Abstract</summary>
  Remarkably common statistical laws characterize the diversity scaling and its fluctuations across a wide range of complex "component systems". These regularities are often interpreted as signatures of an underlying innovation mechanism driving the growth of component diversity, but the basic ingredients necessary for their emergence remain poorly understood. In particular, from language and technological artifacts to genomes and gene expression patterns, the number of distinct components grows s...
  </details>

- **2026-07-02** — Mohammad Amanour Rahman — [MedSaab-US: A Backpropagation-Free Multi-Scale Wavelet-Saab Framework for Thyroid Nodule Segmentation in Ultrasound Images](http://arxiv.org/abs/2607.02209v1)
  <details><summary>📄 Abstract</summary>
  Deep learning (DL) methods dominate thyroid nodule segmentation in ultrasound (US) images, achieving high Dice scores but at the cost of millions of parameters, GPU-dependent training via backpropagation, and limited mathematical tractability. These limitations impede deployment in resource-constrained environments. In this paper, we propose MedSaab-US, a backpropagation-free segmentation framework grounded in the Green Learning paradigm. MedSaab-US extracts multi-scale spatial-frequency feature...
  </details>

- **2026-07-02** — Sara Antonijevic, Brani Vidakovic — [Quaternion Nondecimated Wavelet Descriptors for Multiclass Breast Histology Classification](http://arxiv.org/abs/2607.02133v1)
  <details><summary>📄 Abstract</summary>
  Breast histology images carry diagnostic information in color, texture, orientation, and tissue architecture across a range of scales. In H&E microscopy this information is inherently chromatic and is not fully recovered when the red, green, and blue (RGB) channels are reduced to grayscale or transformed as independent scalar images. We propose an interpretable quaternion nondecimated wavelet framework for breast histology classification. Each RGB image is encoded as a pure quaternion field, and...
  </details>

- **2026-07-02** — Jian Xu, Delu Zeng, John Paisley et al. — [Ask the Right Comparison:Bias-Aware Bayesian Active Top-$k$ Ranking with LLM Judges](http://arxiv.org/abs/2607.02104v1)
  <details><summary>📄 Abstract</summary>
  Large language models (LLMs) are increasingly used as cheap, scalable judges that compare candidate outputs pairwise -- to rank responses, select models, or triage papers. Yet LLM judges are both noisy and systematically biased: they favor verbose or well-formatted answers and exhibit position effects, so simply aggregating their votes recovers a ranking of presentation, not of true quality. We study the practical goal of identifying the \topk{} items under a fixed comparison budget, and make tw...
  </details>

- **2026-07-02** — Cuipeng Wang, Haipeng Wang — [SFKD: Spatial--Frequency Joint-Aware Heterogeneous Knowledge Distillation via Multi-Level Wavelet Spectral Interaction](http://arxiv.org/abs/2607.01906v1)
  <details><summary>📄 Abstract</summary>
  Most existing knowledge distillation methods focus on homogeneous models (e.g., CNN-to-CNN), thereby overlooking the flexibility and potential of knowledge transfer across heterogeneous models. Due to intrinsic inductive bias discrepancies between heterogeneous models that cause spatial distribution inconsistencies, prior heterogeneous distillation methods often weaken or discard spatial information in heterogeneous representations. However, the spatial information in representations often encod...
  </details>

- **2026-07-02** — Zihao Xu, Yuekang Li, Gelei Deng et al. — [Rethinking Complexity Metrics for LLM-Integrated Applications: Beyond Source Code](http://arxiv.org/abs/2607.01903v1)
  <details><summary>📄 Abstract</summary>
  LLM-integrated applications blend natural language prompts with program code, and much of their runtime behavior originates in the prompt layer rather than in the code itself. Existing complexity metrics, however, operate solely at the code level and therefore overlook this behavioral logic entirely. We present HECATE, the first tool designed to assess complexity in both the prompt and code layers of such applications. Central to HECATE is Prompt-as-Specification, a Hoare-logic-inspired formalis...
  </details>

- **2026-07-02** — Maximo Rulli, Thomas Fontanari, Simone Petruzzi et al. — [Subliminal Clocks: Latent Time Modelling in Diffusion Language Models](http://arxiv.org/abs/2607.01774v1)
  <details><summary>📄 Abstract</summary>
  Diffusion Language Models (DLMs) have recently emerged as a promising alternative to autoregressive models. Unlike standard diffusion-based approaches, DLMs are not explicitly conditioned on a timestep, raising a natural question: do these models internally represent denoising progress, and how is such information used downstream? In this work, we show that DLMs do in fact encode a latent representation related to the diffusion timestep within their residual streams. We find that this signal can...
  </details>

- **2026-07-02** — Yujin Yang, Heejung Lee — [Verifiable Knowledge Expansion through Retrieval-Grounded Formal Concept Analysis](http://arxiv.org/abs/2607.01773v1)
  <details><summary>📄 Abstract</summary>
  Ontology construction requires deciding which objects, attributes, and structural relations should be accepted as valid knowledge. Language models can propose such structures from text, but their outputs can still be unsupported or inconsistent. This paper proposes a retrieval-augmented small language model (SLM) framework that uses formal concept analysis (FCA) as a symbolic verification loop for knowledge expansion. Starting from seed attributes, FCA proposes implications over a growing formal...
  </details>

- **2026-07-02** — Licheng Zhang, Bach Le, Pengtao Zhao et al. — [Beyond Pixel Diffs: Benchmarking Image Change Captioning for Web UI Visual Regression Testing](http://arxiv.org/abs/2607.01728v1)
  <details><summary>📄 Abstract</summary>
  Visual regression testing (VRT) is a standard quality assurance step in modern software release pipelines. On every change, it re-renders user interface (UI) screenshots, compares each one against an approved baseline image, and routes any detected difference to a human reviewer who decides whether it is an intended update or an unintended regression. A widely used approach, especially in open-source and continuous-integration pipelines, is pixel-level comparison, which is semantically blind and...
  </details>

- **2026-07-02** — Yongqin Zeng, Sicheng Pan, Jiale Wang et al. — [Generic Expert Coverage for Pruning SparseMixture-of-Experts Language Models](http://arxiv.org/abs/2607.01710v1)
  <details><summary>📄 Abstract</summary>
  Sparsely activated Mixture-of-Experts (MoE) language models contain substantial structured redundancy among routed experts, but pruning them without downstream calibration data remains challenging. Existing expert-pruning methods typically rely on a single aggregated importance score, which can bias the retained set toward experts favored by dominant calibration patterns. We propose \textbf{Generic TB-Coverage}, a coverage-aware expert pruning method that uses only generic text corpora (WikiText...
  </details>

- **2026-07-02** — Frederic Latremoliere — [How to approximate the flat spectral triple of a quantum torus by fuzzy tori : a twisted tale](http://arxiv.org/abs/2607.01681v1)
  <details><summary>📄 Abstract</summary>
  We prove that the classical and the quantum flat torus can be rigorously approximated at a differential level by finite-dimensional fuzzy tori within the framework of the spectral propinquity. Standard attempts to establish this convergence are traditionally obstructed by the intrinsic non-locality of discrete calculus and the subsequent failure of the Leibniz rule. While contemporary alternatives such as spectral truncations circumvent this issue by abandoning $C^*$-algebras in favor of operato...
  </details>

- **2026-07-02** — Lukáš Likavčan — [Substrate-Agnostic 3x: Biosignatures, Technosignatures, Ecologies](http://arxiv.org/abs/2607.01664v1)
  <details><summary>📄 Abstract</summary>
  Substrate-agnostic perspectives are currently attracting increased attention. For example, it has become customary to refer to agnostic biosignatures to reflect the range of alternative extraterrestrial biospheres and to account for the deeper philosophical dependence of candidate biosignatures on the underlying theory of life. Analogously, one can formulate a concept of agnostic technosignatures, reflecting that the more we expand the search for technosignatures, the more we invite theories of ...
  </details>

- **2026-07-01** — Ben Slivinski, Michael Saldivar — [Theoria: Rewrite-Acceptability Verification over Informal Reasoning States](http://arxiv.org/abs/2607.01223v1)
  <details><summary>📄 Abstract</summary>
  When should an AI system's answer be trusted? Formal proof assistants offer certainty but cannot reach most of the problem distribution; scalar LLM judges offer coverage but produce opaque scores that cannot be audited after the fact and are subject to the same coherence issues as any LLM. We present Theoria, a verification architecture that closes this gap. A candidate solution is rewritten into a sequence of typed state transitions, each licensed by an explicit justification, whether that be a...
  </details>

- **2026-07-01** — Jiale Li, Sihan Chen, Mengyuan Liu — [MoHallBench: A Benchmark for Motion Hallucination in Video Large Language Models](http://arxiv.org/abs/2607.01117v1)
  <details><summary>📄 Abstract</summary>
  Video Large Language Models (VideoLLMs) have shown strong progress in video understanding, yet they still suffer from hallucinations that are inconsistent with visual evidence. Existing benchmarks mainly focus on object hallucination or coarse action perception, leaving a key video-specific problem underexplored: motion hallucination, in which models infer human motions that are absent from the video. We present MoHallBench, a benchmark for diagnosing motion hallucination in VideoLLMs. MoHallBen...
  </details>

- **2026-07-01** — Yuan Si, Jialu Zhang — [Checked Program Recovery from Execution Video: A Sound Oracle for Untrusted Generators](http://arxiv.org/abs/2607.00635v1)
  <details><summary>📄 Abstract</summary>
  A growing class of tools recovers a program from observations of its behavior using an untrusted generator, a neural model or a search, that proposes candidates with no correctness guarantee. We study how to make such recovery trustworthy, in the concrete setting of recovering a runnable Scratch program from a recording of its execution. The recording shows what the program does but never its code; many programs produce the same video, so the source cannot be recovered, and the right target is a...
  </details>

- **2026-07-01** — Hongxing Li, Xiufeng Huang, Dingming Li et al. — [Perceive-to-Reason: Decoupling Perception and Reasoning for Fine-Grained Visual Reasoning](http://arxiv.org/abs/2607.01191v1)
  <details><summary>📄 Abstract</summary>
  Fine-grained visual reasoning remains challenging for vision-language models, especially when small but critical visual cues are buried in high-resolution images. Existing approaches rely on repeated cropping or test-time visual search to introduce local evidence, but they typically do not explicitly distinguish perception from reasoning. In this paper, we propose Perceive-to-Reason (P2R), a unified framework that formulates fine-grained visual reasoning as a two-stage process: the model first l...
  </details>

- **2026-07-01** — Bingchen Zhao, Sara Beery, Oisin Mac Aodha — [Autonomous Scientific Discovery via Iterative Meta-Reflection](http://arxiv.org/abs/2607.01131v1)
  <details><summary>📄 Abstract</summary>
  Autonomous scientific discovery systems offer the potential to accelerate research by automating the process of hypothesis generation and validation. However, current systems operate within constrained search spaces or require predefined research questions, limiting their capacity for true open-ended inquiry. Furthermore, while they generate hypotheses iteratively, they largely lack the ability to explicitly synthesize their own accumulated findings to uncover complex, interconnected phenomena. ...
  </details>

- **2026-07-01** — Yin-Jie Li, Yuan-Zhu Wang, Shao-Peng Tang et al. — [Smoking-gun evidence for hierarchical black-hole mergers](http://arxiv.org/abs/2607.01121v1)
  <details><summary>📄 Abstract</summary>
  How stellar-mass black holes grow after their birth is a central open question in astrophysics. Gravitational-wave observations have revealed a subpopulation of coalescing black holes with both high masses and high spins, but whether these properties arise from hierarchical mergers in dense stellar environments or from accretion onto isolated black holes has remained unresolved. Here, using a flexible mixture population model applied to the 259 binary black hole mergers in GWTC-5, we show that t...
  </details>

- **2026-07-01** — Miruna Cretu, John Bradshaw, Patricia Suriana et al. — [SynLaD: Latent Diffusion for Generating Synthesizable Molecules Conditioned on 3D Pharmacophore Profiles](http://arxiv.org/abs/2607.01105v1)
  <details><summary>📄 Abstract</summary>
  We present SynLaD, a latent diffusion framework for small-molecule generation that unifies ligand-based drug design objectives (what to make) with synthetic accessibility (how to make it). Current models typically optimize one objective at the expense of the other, creating a bottleneck for discovering high-scoring and synthesizable molecules. SynLaD combines reaction-constrained generation with pharmacophore-conditioned 3D design by learning a latent space that decodes to both 3D structures and...
  </details>

- **2026-07-01** — Zinan Tang, Yukun Zhang, Shaomian Zheng et al. — [CausalMix: Data Mixture as Causal Inference for Language Model Training](http://arxiv.org/abs/2607.01104v1)
  <details><summary>📄 Abstract</summary>
  In Large Language Model (LLM) training, data mixing plays a pivotal role in determining model performance. Recent methods optimize mixture weights via proxy models, but they rely on the assumption of static data distributions. As a result, when the underlying data pool shifts, these methods require costly retraining from scratch. This limitation restricts their ability to scale seamlessly from small settings to larger data pools and model sizes. In this paper, we propose CausalMix to address thi...
  </details>

- **2026-07-01** — Byeongguk Jeon, Seonghyeon Ye, JaeHyeok Doo et al. — [RoboWorld: Fast and Reliable Neural Simulators for Generalist Robot Policy Evaluation](http://arxiv.org/abs/2607.01060v1)
  <details><summary>📄 Abstract</summary>
  Video world models are emerging as a scalable alternative for evaluating generalist robot policies, bypassing the physical constraints and engineering burdens of real-world deployment. However, evaluating policies with video world models remains challenging, as world-model errors can make generated rollouts unreliable and slow inference limits large-scale throughput. We introduce RoboWorld, an automated evaluation pipeline that pairs a fast autoregressive video world model with a task-progress-a...
  </details>

- **2026-07-01** — Li Jin, Jian Huang, Junde Lu et al. — [Slope-Guided Mamba and Angular-Refined Transformer for Light Field Super-Resolution](http://arxiv.org/abs/2607.00965v1)
  <details><summary>📄 Abstract</summary>
  Light Field Super-Resolution (LFSR) necessitates accurate modeling of spatial-angular correlations while preserving intrinsic 4D ray coherence. However, maintaining such high-dimensional consistency remains challenging, primarily due to two inherent limitations in prevailing modeling paradigms. First, spatial and angular dimensions are often modeled in a decoupled manner, restricting early cross-dimensional interaction and leading to geometric inconsistencies. Moreover, although continuous seque...
  </details>

- **2026-07-01** — Jingchen Ni, Cangjin Yu, Dan Jiang et al. — [MG-RWKV: Multi-Grained Context-Aware RWKV for Temporal Forgery Localization](http://arxiv.org/abs/2607.00902v1)
  <details><summary>📄 Abstract</summary>
  Driven by Artificial Intelligence-Generated Content (AIGC), the authenticity of audio-visual content is facing severe challenges. Temporal Forgery Localization (TFL) aims to precisely identify manipulated segments within untrimmed sequences. However, existing methods are limited by CNNs' local receptive fields or Transformers' quadratic complexity, while emerging linear models often struggle to balance global authentic context compression with local abrupt forgery perception. To address this, we...
  </details>

- **2026-07-01** — Maximilian Idahl, Jörg Tiedemann, Sampo Pyysalo et al. — [MultiSynt/MT: Trillion-Token Multi-Parallel Pre-Training Data Translated Across 36 Languages](http://arxiv.org/abs/2607.00890v1)
  <details><summary>📄 Abstract</summary>
  Open web-scale pre-training corpora remain concentrated in English, limiting multilingual LLM development. We introduce MultiSynt/MT, an open synthetic parallel corpus with approximately 4.8 trillion target-language tokens across 36 European languages, produced by translating 100 billion high-quality Nemotron-CC tokens with Tower+ and OPUS-MT/HPLT-MT systems. For many medium- and lower-resource European languages, this is the largest openly available pre-training resource. On a broad multilingua...
  </details>

- **2026-07-01** — Xudong Li, Mengdan Zhang, Peixian Chen et al. — [OmniView-Space: Reinforcing Spatial Reasoning via Multi-Perspective Spatial Mapping](http://arxiv.org/abs/2607.00881v1)
  <details><summary>📄 Abstract</summary>
  Spatial intelligence remains a persistent challenge for Multimodal Large Language Models (MLLMs), as it requires coherent spatial scene representations beyond basic object recognition. Existing methods typically build such representations through textual reasoning or 3D reconstruction. However, they often falter during multi-step reasoning, particularly when required to dynamically re-anchor evidence to the specific camera-, object-, or direction-centric reference frames demanded by complex quer...
  </details>

- **2026-07-01** — Biswa Sengupta — [Self-Evolving Agents with Anytime-Valid Certificates](http://arxiv.org/abs/2607.00871v1)
  <details><summary>📄 Abstract</summary>
  Self-evolving agents violate the assumption behind most learning-theoretic guarantees: the data, evaluator, components, and hypothesis space are produced by the policy being updated. We present \textbf{SEA}, an architecture that confines self-modification to a small steering adapter and a versioned harness around a \emph{frozen} base model and admits each modification only through an anytime-valid gate that emits an auditable certificate against a fixed error budget. Five loop controllers compos...
  </details>

- **2026-07-01** — Andrea Sanchietti, Riccardo Marin, Bharat Lal Bhatnagar et al. — [Stitched Embeddings: A Unified Latent Space for 3D Garments and 2D Patterns](http://arxiv.org/abs/2607.00829v1)
  <details><summary>📄 Abstract</summary>
  While garments are essential for realistic digital humans, their topological variety makes them much harder to model than parametric bodies. Traditional tailoring relies on 2D sewing patterns, yet bridging these patterns to 3D geometry currently requires physical simulations. We present Stitched Embeddings, the first simulation-free framework to unify 3D garment reconstruction and sewing pattern inference within a single bidirectional latent space. By leveraging the geometric priors of a pretrai...
  </details>

- **2026-07-01** — Kyan Mahajan, Mohammad Saqlain — [SpiralFovea: Input-Adaptive Foveated Tokenization as a Third Lever of Resource-Adaptive Inference](http://arxiv.org/abs/2607.00780v1)
  <details><summary>📄 Abstract</summary>
  Most adaptive-inference techniques for foundation models change what the model does - early exit, MoE routing, KV-cache compression, dynamic attention sparsity. The input that hits the backbone, however, remains a fixed-grid tokenisation indifferent to image content. We argue that this is a missed lever. We present SpiralFovea, a parameter-free, input-adaptive tokeniser in which token identity, location, scale, and count are all functions of local visual entropy and selection completes before an...
  </details>

- **2026-07-01** — Mark Russinovich, Ram Shankar Siva Kumar, Ahmed Salem — [Phantom References: Hallucinated Citations That Survive Peer Review at Top-Tier Conferences](http://arxiv.org/abs/2607.00738v1)
  <details><summary>📄 Abstract</summary>
  Large language models can generate polished scientific text that includes unsupported claims, allowing hallucinations to enter the archival record. Assessing this risk via technical statements is difficult and often requires expert judgment, but citations provide a more auditable surface: a reference either resolves to a real scholarly work with compatible authorship, or it does not.   We measure citation hallucination in peer-reviewed proceedings using a conservative definition limited to ident...
  </details>

- **2026-07-01** — Kyuwon Kim, Sunjae Yoon, Chang D. Yoo — [SPECSIA: Stylization Dataset for Novel-View Enhancement in Drawing-based 3D Animation](http://arxiv.org/abs/2607.00525v1)
  <details><summary>📄 Abstract</summary>
  Generating animation from a single 2D drawing is challenging because the output must preserve character appearance while remaining plausible and temporally coherent under motion. Existing drawing-based 3D animation pipelines often use sample-wise 2D refinement to align animated renderings with the input image, but such optimization tends to overfit to the observed view and fails to correct projection-induced artifacts in novel views. To address this limitation, we introduce SPECSIA-15K, a paired...
  </details>

- **2026-07-01** — Emil Joswin, Srujananjali Medicherla, Priyanka Mary Mammen — [A Mechanistic View of Authority Hierarchy in LLM Sycophancy](http://arxiv.org/abs/2607.00415v1)
  <details><summary>📄 Abstract</summary>
  Authority bias poses a critical safety concern in language models: models systematically prioritize social cues from authority figures over factual consistency, swaying their answers based on source credibility rather than evidence. We mechanistically investigate this phenomenon using a controlled medical QA setting, where hints suggesting incorrect answers are attributed to personas of varying expertise. Across Llama-3.1-8B, Qwen3-8B, and Gemma-2-9B, we find that models respond in a graded mann...
  </details>

- **2026-07-01** — Jingjing Zhang, Lei Zhang, Zheren Fu et al. — [Learning to Compose: Revisiting Proxy Task Design for Zero-Shot Composed Image Retrieval](http://arxiv.org/abs/2607.00374v1)
  <details><summary>📄 Abstract</summary>
  Composed Image Retrieval (CIR) retrieves a target image from a reference image and a textual modification. While supervised CIR relies on costly triplets, Zero-Shot CIR (ZS-CIR) alleviates this reliance through proxy tasks trained on image-text pairs. However, existing proxy tasks primarily enhance visual and textual representations to accommodate a predefined composition mechanism such as pseudo-word injection into a frozen text encoder or linear feature arithmetic. As a result, the composition...
  </details>

- **2026-07-01** — Qingda Hu, Ziheng Qiu, Jieru Zhao et al. — [AutoSpeed: Annotation-Free Stage-Adaptive Motion Speed Learning for Robot Manipulation](http://arxiv.org/abs/2607.01051v1)
  <details><summary>📄 Abstract</summary>
  Different stages of manipulation tasks exhibit varying levels of difficulty, suggesting stage-dependent motion speeds and temporal prediction horizons. However, existing IL-based visuomotor policies typically imitate the execution speed of expert demonstrations and operate with a fixed temporal prediction horizon, limiting flexibility and overall task throughput. In this paper, we introduce AutoSpeed, a model-agnostic learning framework that enables existing visuomotor policies to predict trajec...
  </details>

- **2026-07-01** — Yannik Keller, Thomas Eisenmann — [Understanding Large Language Models](http://arxiv.org/abs/2607.01006v1)
  <details><summary>📄 Abstract</summary>
  Large Language Models (LLMs) represent one of the most significant advances in AI and natural language processing in recent years. Still, many pressing questions about their mechanisms, capabilities, and relationship to human cognition remain highly debated. This chapter aims to outline our current understanding of LLMs by discussing recent evidence on emerging capabilities and their mechanistic implementation within processing layers. We begin with a concise overview of the Transformer architec...
  </details>

- **2026-07-01** — Hiroki Oda, Kinga Makovi, Taha Yasseri et al. — [A field experiment of social influence and behavioral contagion with bots on Reddit](http://arxiv.org/abs/2607.00854v1)
  <details><summary>📄 Abstract</summary>
  Recent advances in AI have heightened scholars' and policy makers' concern with social influence and behavioral contagion in online communities. We conduct a field experiment on Reddit to investigate the extent to which online users are susceptible to positive behavioral stimuli from other users and artificial agents. We let apparent human and bot accounts give symbolic awards to users with one of four rationales: praising the recipient's logical argument, emotional sensitivity, or moral integri...
  </details>

- **2026-07-01** — Jinwen Wang, Youfang Lin, Xiaobo Hu et al. — [Local Motion Matters: A Deconstruct-Recompose Paradigm for Reinforcement Learning Pre-training from Videos](http://arxiv.org/abs/2607.00808v1)
  <details><summary>📄 Abstract</summary>
  Pre-training on large-scale videos to improve reinforcement learning efficiency is promising yet remains challenging. Existing methods typically treat the agent as an indivisible entity, modeling motion patterns globally. Such global modeling is tightly coupled with the morphology, hindering transfer across domains. In contrast, despite the vast disparity in global motions, the local components exhibit similar motion patterns across different agents. Building on this insight, we propose a novel ...
  </details>

- **2026-07-01** — Jinwen Wang, Youfang Lin, Xiaobo Hu et al. — [Task-Relevant Representation Decoupling for Visual Reinforcement Learning Generalization](http://arxiv.org/abs/2607.00796v1)
  <details><summary>📄 Abstract</summary>
  Visual Reinforcement Learning (VRL) has achieved considerable success in solving control tasks. However, generalizing learned policies to new environments remains a major challenge, as agents often overfit to task-irrelevant features in the training environment. To solve this problem, we introduce the concept of decoupling observations into task-relevant and task-irrelevant representations. Building on this idea, we propose a self-supervised Task-Relevant Representation Decoupling (T2RD) algorit...
  </details>

- **2026-07-01** — Alexey Potapov — [AGI Maze as a Benchmark Framework for World-Modeling Agents](http://arxiv.org/abs/2607.00627v1)
  <details><summary>📄 Abstract</summary>
  Large language models (LLMs) are powerful pattern-completion systems, but their default operating mode - predicting the next token from a static context - does not reliably produce persistent, manipulable representations of an external world. Many tasks that look like "reasoning" in text become substantially harder once the environment is partially observable, stateful, and requires memory and structured hypotheses about hidden state. AGI Maze is a lightweight framework for building such environ...
  </details>

- **2026-07-01** — Deeparnab Chakrabarty, Hang Liao — [Query Complexity of Hypergraph Connectivity and Learnability using CUT Oracles](http://arxiv.org/abs/2607.01216v1)
  <details><summary>📄 Abstract</summary>
  We investigate the power of CUT queries to reveal the structure of unknown hypergraphs. While simple graphs allow for optimal $O(n)$-query connectivity algorithms, hypergraphs face a fundamental identifiability barrier in that distinct hypergraphs can share identical cut-profiles, making exact edge learning impossible in general, a primitive crucial in the graph connectivity algorithms.   We first present a zero-error randomized algorithm that identifies the connected components of any weighted ...
  </details>

- **2026-07-01** — Georgios Amanatidis, Giulio Giaconi, Evangelos Markakis et al. — [Online Fair Division Meets Reordering Buffers](http://arxiv.org/abs/2607.01159v1)
  <details><summary>📄 Abstract</summary>
  We study the online fair division of indivisible mixed manna among agents with additive valuation functions. Under the standard online model, at each time step an indivisible item arrives; each agent may assign it a positive, negative, or zero value, and it must be irrevocably allocated, before the arrival of the next item. At the same time, we also wish to maintain some fairness guarantee, and in this work we focus on envy-freeness (EF) and one of its most prominent relaxations, envy-freeness u...
  </details>

- **2026-07-01** — Xun Dong, Yibo Xu, Naigang Wang et al. — [ZO-Act: Efficient Zeroth-Order Fine-Tuning via One-Shot Activation-Informed Low-Rank Subspaces](http://arxiv.org/abs/2607.01125v1)
  <details><summary>📄 Abstract</summary>
  Zeroth-order (ZO) optimization enables fine-tuning large language models when backpropagation is unavailable or memory-prohibitive, but existing methods often perturb full model weights or randomly constructed low-dimensional subspaces, yielding high-variance estimates and limited performance. We propose ZO-Act, an activation-informed ZO fine-tuning method that restricts perturbations to a fixed low-rank subspace derived from input activations. For each linear layer, ZO-Act computes a small acti...
  </details>

- **2026-07-01** — James C. Davis, Paschal C. Amusuo, Tanmay Singla et al. — [Cheap Code, Costly Judgment: A Case Study on Governable Agentic Software Engineering](http://arxiv.org/abs/2607.01087v1)
  <details><summary>📄 Abstract</summary>
  Generative AI is shifting software engineering from a practice organized around scarce implementation effort toward one organized around abundant, low-cost code production. This shift changes the central engineering problem: not whether AI can generate useful code, but how engineers organize architectures, tools, evidence, and feedback loops so that AI-mediated development remains inspectable, correctable, and maintainable.   We study this problem through a first-person case study: a 12-week dev...
  </details>

- **2026-07-01** — Suraj Borate, Aarav Shah, Madhu Vadali — [Where Am I? Semantic Map Grounding via Vision-Language Models for Multi-Modal Localization](http://arxiv.org/abs/2607.01079v1)
  <details><summary>📄 Abstract</summary>
  We address robot localization in GPS-denied indoor environments by reframing it as a semantic reasoning task rather than a geometric estimation problem. Motivated by how humans localize using object-level cues and labeled maps, we ask whether a vision-language model, given a front camera image, a polar LiDAR scan, and a top-down semantic grid map, can infer the robot pose. We fine-tune Qwen2.5-VL-7B with LoRA and attach a lightweight regression head that predicts continuous pose coordinates (x, ...
  </details>

- **2026-07-01** — Ishay Haviv — [Fair Allocation under Conflict Constraints via Strong Colorability](http://arxiv.org/abs/2607.01059v1)
  <details><summary>📄 Abstract</summary>
  In the fair allocation problem under conflict constraints, the goal is to partition the vertices of a graph among agents in a fair manner, such that no two adjacent vertices are assigned to the same agent. We study this problem for agents with common preferences through the lens of three fairness criteria: stochastic-dominance envy-freeness up to one item for preference orders (SD-EF1), envy-freeness up to one item for monotone additive valuations (EF1), and envy-freeness up to one item from eac...
  </details>

- **2026-07-01** — Dianyu Wang, Yidan Zhang, Peirong Zhang et al. — [GeoSearcher: Anchor-Guided Progressive Reasoning for Remote Sensing Visual Grounding with Process Supervision](http://arxiv.org/abs/2607.01050v1)
  <details><summary>📄 Abstract</summary>
  Recent multimodal large language models (MLLMs) have shown strong cross-modal understanding and coordinate generation abilities in visual grounding. However, transferring these abilities to remote sensing visual grounding (RSVG) remains challenging. High-resolution remote sensing images usually cover large-scale scenes, where targets are often extremely small and surrounded by numerous visually similar distractors. Meanwhile, queries often contain multiple clues, such as reference objects, spati...
  </details>

- **2026-07-01** — Lawrence Obiuwevwi, Krzysztof J. Rechowicz, Jessica M. Johnson et al. — [Quantifying the Affective Gap: A Zero-Shot Evaluation of LLMs on Fine-Grained Emotion Taxonomies](http://arxiv.org/abs/2607.00968v1)
  <details><summary>📄 Abstract</summary>
  Emotion recognition in natural language is a foundational challenge in affective computing, with critical implications for human-computer interaction, mental health support, and conversational AI. This paper presents a rigorous, unified zero-shot evaluation of three leading commercial large language models: Claude (claude-sonnet-4-6), ChatGPT (GPT-5.4), and Gemini (gemini-2.5-flash). The models were queried through their respective production APIs as of April 2026 on a fine-grained 13-class emot...
  </details>

- **2026-07-01** — Ria Patel, Masoud Hakimi Heris, Yuan Liu et al. — [Synthesizing Compound Pulse Gadgets for Hamiltonian Simulation on Trapped-Ion Platforms](http://arxiv.org/abs/2607.00826v1)
  <details><summary>📄 Abstract</summary>
  Standard gate-level transpilation introduces significant physical noise and overhead for high-precision quantum algorithms, such as the Quantum Singular Value Transformation (QSVT), on near-term trapped-ion hardware. Current compilers treat quantum operations as discrete units, forcing the physical control layer to execute highly fragmented laser pulses. To address this hardware-software disconnect, this work introduces a holistic pulse synthesis strategy that bypasses discrete gate-stitching to...
  </details>

- **2026-07-01** — Omar A. M. Abdelraouf — [On-Demand Coherent Nanolaser Metalens and Beam Steering Enabled by Physics-Informed Neural Networks](http://arxiv.org/abs/2607.00739v1)
  <details><summary>📄 Abstract</summary>
  The integration of artificial intelligence with physical modeling offers a transformative route for accelerating the design of active nanophotonic devices. Here, we present NanoPhotoNet-Lase, a physics-informed neural network (PINN) framework that embeds the electromagnetic and rate equations of lasing directly into its learning process to expedite the design of metasurface nanolasers. By coupling Maxwell's vector Helmholtz equation with the four-level population dynamics of dye gain media, the ...
  </details>

- **2026-07-01** — Roberto Capobianco, Harm van Seijen, Nolan D. Bard et al. — [Coachable agents for interactive gameplay](http://arxiv.org/abs/2607.00642v1)
  <details><summary>📄 Abstract</summary>
  Reinforcement learning has proven to be a valuable tool in the creation of advanced AI and robotic systems, contributing to everything from game playing to robotics to foundation models. Through trial-and-error, these AI systems typically learn one, near-optimal behavior to solve their tasks. However, there are many use cases in which one would like to assert some level of control, preferably in real time, over how the task is solved. We refer to these modifications of a core task as styles. We ...
  </details>

- **2026-07-01** — Bingchen Huang, Zhiling Wang, Yifu Chen et al. — [Retrieved Images as Visual Thought: Training-Free Multimodal In-Context Learning for the Open-vs-Closed Gap](http://arxiv.org/abs/2607.00606v1)
  <details><summary>📄 Abstract</summary>
  Recent work on Thinking with Images makes vision a dynamic part of reasoning, but does so through generation: the model invokes external tools, synthesizes code, or imagines new imagery, each at the cost of a tool protocol, brittle code, or an expensive training pipeline. A fourth route makes vision dynamic without generating anything, by retrieving labeled exemplar images and reasoning over them, yet it remains underexplored despite being train-free. We present ReVisIT, a train-free framework t...
  </details>

- **2026-07-01** — Trung Thanh Nguyen, Hai Nguyen-Truong, Tu Vo et al. — [Cross4D-JEPA: Dense Cross-modal Correspondence Distillation for 4D Point Cloud Representation Learning](http://arxiv.org/abs/2607.00514v1)
  <details><summary>📄 Abstract</summary>
  Automatic understanding of dynamic 4D point clouds, the 3D-point sequences captured over time by depth sensors and LiDAR, is central to robotics and embodied perception. Yet annotating them densely is expensive, making self-supervised pretraining the natural route to transferable representations. Existing pretext tasks, however, are almost entirely intra-modal, and the few methods that transfer knowledge from 2D foundation models rely on a single global embedding per clip, discarding the rich pe...
  </details>

- **2026-07-01** — Ivan Ji, Liuyi Hu,  Harrison et al. — [Real-Time Hard Negative Sampling via LLM-based Clustering for Large-Scale Two-Tower Retrieval](http://arxiv.org/abs/2607.00448v1)
  <details><summary>📄 Abstract</summary>
  The two-tower model has been widely used for large-scale recommendation systems, particularly in the retrieval stage. Industry standards for training two-tower models typically involve in-batch and/or out-of-batch negative sampling. However, these methods often produce easy negatives that models can quickly learn, failing to sufficiently challenge the model. To address this issue, a novel self-supervised hard negative sampling technique is proposed that leverages a large language model (LLM) to ...
  </details>

- **2026-07-01** — Zhishang Xiang, Zerui Chen, Yunbo Tang et al. — [MemSyco-Bench: Benchmarking Sycophancy in Agent Memory](http://arxiv.org/abs/2607.01071v1)
  <details><summary>📄 Abstract</summary>
  Memory has emerged as a cornerstone of modern LLM-based agents, supporting their evolution from single-turn assistants to long-term collaborators. However, memory is not always beneficial: retrieved memories often induce a critical issue of sycophancy, causing agents to over-align with the user at the cost of factual accuracy or objective reasoning. Despite this emerging risk, existing memory benchmarks primarily evaluate whether memories are correctly stored, retrieved, or updated, while overlo...
  </details>

- **2026-07-01** — Midhun Parakkal Unni, Samuel Kaski — [Human-Machine Collaboration on Generative Meta-Learning: Model and Algorithm](http://arxiv.org/abs/2607.00926v1)
  <details><summary>📄 Abstract</summary>
  Generalizing machine learning models to environments that differ from their training distribution remains a critical hurdle, particularly when data from the target domain is entirely or partially unavailable. We propose Generative Meta-Learning with Human Feedback (GMHF), a novel framework that bridges this domain gap by leveraging expert intuition to guide data synthesis. Grounded in a theoretical analysis of generalization error, we derive bounds demonstrating that aligning the distribution of...
  </details>

- **2026-07-01** — Zipeng Guo, Xiaoan Liu, Lichen Ma et al. — [GMO-E$^2$DIT: Grounded Multi-Operation Editing for E-Commerce Images](http://arxiv.org/abs/2607.00920v1)
  <details><summary>📄 Abstract</summary>
  Real-world e-commerce image editing often requires multiple, localized, and auditable operations rather than global restyling. This compositional nature poses a dual challenge: models must precisely apply all requested edits to the correct regions while preserving unmodified content, even under ambiguous instructions. Existing one-shot editors conflate intent resolution, spatial grounding, and synthesis into a single step, frequently resulting in partial execution failures, which is unacceptable...
  </details>

- **2026-07-01** — Markos Antonopoulos, Anastasia Bolovinou, Bill Roungas et al. — [Beyond Line of Sight: Hybrid Validation of V2X Collective Perception in Complex Scenarios](http://arxiv.org/abs/2607.00874v1)
  <details><summary>📄 Abstract</summary>
  This paper introduces a probabilistic framework and hybrid validation methodology for V2X-enabled Collective Perception (CP) in complex traffic scenarios. The proposed Bayesian fusion algorithm extends the perceptual horizon of connected and autonomous vehicles by integrating heterogeneous sensor observations from multiple agents into a shared probabilistic occupancy grid. Each cell of this grid encapsulates both occupancy likelihood and uncertainty, enabling explainable and trustworthy situatio...
  </details>

- **2026-07-01** — Jinliang Xu, Liping Ma — [MMAO-Dyn: A Metabolic Multi-Agent Optimizer for Dynamic Optimization](http://arxiv.org/abs/2607.00846v1)
  <details><summary>📄 Abstract</summary>
  This paper studies whether the Metabolic Multi-Agent Optimizer (MMAO) can be credibly derived into a dynamic-optimization method without replacing its core metabolic control loop by external adaptation modules. The proposed MMAO-Dyn maps private energy, communal budget, role drift, success feedback, and lifecycle turnover to a nonstationary setting in which environmental changes repeatedly invalidate previously useful local structure. We evaluate MMAO-Dyn on an 18-scenario synthetic dynamic cont...
  </details>

- **2026-07-01** — Jalal Mahmud, Eser Kandogan — [Exploring the Semantic Gap in Agentic Data Systems: A Formative Study of Operationalization Failures in Analytical Workflows](http://arxiv.org/abs/2607.00828v1)
  <details><summary>📄 Abstract</summary>
  Large language models (LLMs) are increasingly used to generate queries, invoke tools, and construct analytical workflows. Although recent advances have substantially improved workflow generation and execution, the semantic information required to operationalize analytical concepts often lies beyond what is explicitly represented in database schemas and data values. We present a cross-domain formative study of operationalization failures in agent-generated analytical workflows. Across 236 analyti...
  </details>

- **2026-07-01** — Jisen Li, Bingxuan Li, Nanyi Jiang et al. — [Multi-Turn Agentic Scientific Literature Search via Workflow Induction](http://arxiv.org/abs/2607.00597v1)
  <details><summary>📄 Abstract</summary>
  Scientific literature search often requires more than retrieving papers from a single query: users' intents are underspecified, preference-dependent, and evolve through interaction. Existing search agents typically rely on fixed pipelines or implicit language-only reasoning, making their search strategies difficult to control, inspect, and refine. We introduce PaperPilot, a multi-turn literature search agent that frames scientific search as workflow induction. Given an anchor paper and a user qu...
  </details>

- **2026-07-01** — Shaoyu Yang, Haifeng Lin, Chunrong Fang et al. — [Rise From The Ashes: LLM-based Static Analysis for Deep Learning Framework Bugs](http://arxiv.org/abs/2607.00555v1)
  <details><summary>📄 Abstract</summary>
  Deep learning (DL) frameworks are critical AI infrastructures that often hide bugs with serious security implications. While dynamic approaches such as fuzzing are effective in uncovering these bugs, they require real test execution and incur high computational costs. Static analysis is a natural complement because it can detect bugs without runtime execution, offering fast and scalable testing. Unfortunately, there is still limited work targeting static analysis for DL frameworks due to their m...
  </details>

- **2026-07-01** — Yu-Hsiang Chen, Wei-Jer Chang, Yi-Ting Chen et al. — [ECoSim: Data Efficient Fine-Tuning for Controllable Traffic Simulation](http://arxiv.org/abs/2607.00545v1)
  <details><summary>📄 Abstract</summary>
  Controllable traffic simulation is critical for testing autonomous driving systems, yet existing approaches often require retraining large generative models with extensive annotated data. We introduce a lightweight control adaptation framework that enables multi-modal controllability (sketch, latent behavior codes, and text) for pretrained state-of-the-art diffusion and autoregressive traffic models. By modulating intermediate features through identity-initialized FiLM layers, our method efficie...
  </details>

- **2026-07-01** — Merve Atasever, Cagan Bakirci, Alfredo Reina Corona et al. — [Learning Gait-Aware Quadruped Locomotion with Temporal Logic Specifications](http://arxiv.org/abs/2607.00442v1)
  <details><summary>📄 Abstract</summary>
  Reinforcement learning (RL) for quadruped locomotion commonly depends on fixed, hand-crafted, and Markovian reward functions that limit both interpretability of learned policies and lack explicit control over gait behaviors. We introduce a framework where distinct gaits are specified using parameterized constraints expressed in Signal Temporal Logic (STL). These include safety bounds, gait synchronization constraints, command tracking, and actuation bounds. From these specifications, we develop ...
  </details>

- **2026-07-01** — Jiahui Wang, Zhenyuan Li, Zhengkai Wang et al. — [Minos: A Multi-Agent Collaborative Framework for Provenance-Based Backward Tracking](http://arxiv.org/abs/2607.00440v1)
  <details><summary>📄 Abstract</summary>
  Sophisticated cyber attacks, particularly Advanced Persistent Threats (APTs), require effective post-intrusion forensic analysis. Provenance-based backward tracking reconstructs attack scenarios by tracing causality from security alerts, but existing methods rely on low-level statistical features and rigid traversal strategies, limiting their ability to capture high-level adversarial intent and suffering from dependency explosion. We present Minos, a multi-agent framework that formulates backwar...
  </details>

- **2026-07-01** — Ping Zhang, Rui Meng, Xiaodong Xu et al. — [Evolving Intelligent Complex Systems via Intellicise Networks: Architecture, Technologies, and Pathways](http://arxiv.org/abs/2607.00316v1)
  <details><summary>📄 Abstract</summary>
  Future engineering infrastructures are evolving into large-scale, open, heterogeneous, and wirelessly interconnected complex systems. These systems present significant challenges in optimizing network resource utilization, managing high-dimensional information spaces, and accommodating diverse business requirements. Intellicise networks, characterized by Intent-driven operation, semantic-native capability, and distributed intelligence, offer a promising paradigm for enabling such intelligent com...
  </details>

- **2026-07-01** — Amirreza Rouhi, Rajat Aggarwal, Parikshit Sakurikar et al. — [RetailSMV: Exocentric vs. Egocentric Adaptation of Foundation Video World Models in Retail](http://arxiv.org/abs/2607.00310v1)
  <details><summary>📄 Abstract</summary>
  Foundation video diffusion models are increasingly viewed as world simulators for embodied agents, yet their pretraining on internet-scale generic video leaves them poorly aligned with real-world deployment domains. We study parameter-efficient adaptation of a pretrained foundation video world model to retail scenes: when synchronized egocentric and exocentric video of the same activity are available, which viewpoint of training data produces the strongest adapted model?   We introduce RetailSMV...
  </details>

- **2026-07-01** — Amirhosein Chahe, Tyler Naes, Jovin D'sa et al. — [What's Hidden Matters: Identifying Planning-Critical Occluded Agents using Vision-Language Models](http://arxiv.org/abs/2607.00283v1)
  <details><summary>📄 Abstract</summary>
  Autonomous vehicles must safely navigate complex environments where planning-critical agents may be hidden from view. Current approaches often treat all occlusions with uniform conservatism, yielding needlessly defensive driving, or they infer hidden spaces without estimating the impact on the planner. This work bridges the critical gap between perception and planning by enabling Vision-Language Models (VLMs) to identify and reason about the specific hidden agents that are most critical to the e...
  </details>

- **2026-06-30** — Sarah Arpin, Jason T. LeGrow, Hiram H. López et al. — [Digital signature schemes based on code equivalence and syndrome decoding from restricted errors](http://arxiv.org/abs/2606.31601v1)
  <details><summary>📄 Abstract</summary>
  Digital signature schemes are an important cryptographic tool to ensure data authenticity and integrity in many applications that must be resilient to attacks, including those facilitated by quantum computers. We consider the two digital signature schemes based on error-correcting codes that are second-round candidates in NIST's call for Additional Signature Schemes, which is part of the Post-Quantum Cryptography Standardization Process. Specifically, we provide an overview of the Codes and Rest...
  </details>

- **2026-06-30** — Shayan Peyghambari Oskoui, Norah Almousa, Zhaoyi Joey Hou et al. — [SEFORA: Student Essays with Feedback Corpus and LLM Feedback Evaluation Framework](http://arxiv.org/abs/2607.00274v1)
  <details><summary>📄 Abstract</summary>
  Effective writing feedback is among the strongest drivers of student learning, yet producing it at scale is labor-intensive. LLMs offer a natural path to scaling writing support, but two gaps stand in the way: few public corpora capture how instructors actually deliver feedback in real classrooms, and no reliable method measures whether generated feedback aligns with what an instructor would write. We address both. SEFORA is a public corpus pairing instructor inline feedback with assignment prom...
  </details>

- **2026-06-30** — Adam Darmanin — [LV-ROVER: Multi-Stream Tesseract Voting for Maltese Paragraph OCR](http://arxiv.org/abs/2607.00250v1)
  <details><summary>📄 Abstract</summary>
  Maltese has decent text corpora and pretrained language models, but, like many languages outside the handful with large OCR benchmarks, only a single known real labelled PDF corpus for OCR training, 57 page, far below what paragraph-level training needs: low-resource for OCR specifically. With no real corpus to train on at scale, we built a synthetic training pipeline and a 5-stream Tesseract LV-ROVER ensemble, and report results on a 422-paragraph benchmark against a fine-tuned-Tesseract baseli...
  </details>

- **2026-06-30** — Andrea Ferrario — [A Category Theory Account of AI Identity](http://arxiv.org/abs/2607.00220v1)
  <details><summary>📄 Abstract</summary>
  Artificial intelligence (AI) systems are routinely modified after deployment through retraining and changes in their environments. These transformations raise a metaphysical question: under what conditions does an AI system remain the same system over time or across deployments? Earlier work formulates synchronic and diachronic identity propositionally, by relating identity within a fixed AI system type to equality of trustworthiness levels. Such criteria specify when identity statements are tru...
  </details>

- **2026-06-30** — Ruikang Zhao, Zhenting Wang, Han Gao et al. — [SLIM-RL: Risk-Budgeted Random-Masking RL for Diffusion LLMs Without Trajectory Slicing](http://arxiv.org/abs/2607.00208v1)
  <details><summary>📄 Abstract</summary>
  Reinforcement learning for diffusion large language models (dLLMs) has largely moved to trajectory-aware methods. The current state of the art, TraceRL, holds that random masking is mismatched with the model's inference trajectory, and it reconstructs that trajectory during training by slicing each rollout into up to K/s trajectory-aligned training samples, a cost that grows with the block size K. We show that this mismatch can be mitigated without reconstructing the trajectory. Our method, SLIM...
  </details>

- **2026-06-30** — Nishant Subramani — [Harnessing the Latent Space: From Steering Vectors to Model Calibrators for Control and Trust](http://arxiv.org/abs/2607.00083v1)
  <details><summary>📄 Abstract</summary>
  Language models have changed from unreliable text generators to highly-capable large models with trillions of parameters. Capability increases come hand-in-hand with increases in scale, making understanding the internal representations of models more challenging. Since millions of users increasing rely on language models to interact with external tools or make decisions in medium or high-stakes scenarios, we need to establish control over model behavior and know when to trust model outputs. In t...
  </details>

- **2026-06-30** — Lianyu Hu, Shengqian Qin, Zeqin Liao et al. — [CoLT: Teaching Multi-Modal Models to Think with Chain of Latent Thoughts](http://arxiv.org/abs/2606.31986v1)
  <details><summary>📄 Abstract</summary>
  Chain-of-thought (CoT) reasoning has enabled multi-modal large language models (MLLMs) to tackle complex visual reasoning tasks by generating explicit intermediate reasoning steps in natural language. However, this text-based reasoning paradigm is inherently slow at inference time with even thousands of tokens and fundamentally constrained by the expressiveness of natural language. In this paper, we propose CoLT, (Chain of Latent Thoughts), a novel framework that teaches multi-modal models to re...
  </details>

- **2026-06-30** — Junyu Ren, Lek-Heng Lim — [Low-dimensional topology of deep neural networks](http://arxiv.org/abs/2606.31856v1)
  <details><summary>📄 Abstract</summary>
  We study layered models, including feedforward networks, ResNets, and transformers, by limiting each layer to a width of $d = 3$, i.e., $\mathbb{R}^3$ as representation space. This allows us to track how a neural network changes low-dimensional topological invariants through its layers. Just about any topological structure may be simplified or even trivialized by simply increasing dimension; e.g., any knot is equivalent to an unknot in $\mathbb{R}^4$. By restricting to $\mathbb{R}^3$, we not onl...
  </details>

- **2026-06-30** — Ying Fan, Anej Svete, Kangwook Lee — [Bridging the Gap Between Latent and Explicit Reasoning with Looped Transformers](http://arxiv.org/abs/2606.31779v1)
  <details><summary>📄 Abstract</summary>
  Language models typically reason via explicit chain-of-thought (CoT), generating intermediate steps token-by-token. Latent CoT offers an alternative: it performs multi-step reasoning in the model's hidden states, replacing decoded tokens with continuous representations for greater efficiency. However, existing latent CoT methods underperform explicit CoT beyond 1B parameters, and the gap widens with scale. Looped, or recurrent-depth, Transformers, which reuse their weights to increase computatio...
  </details>

- **2026-06-30** — Soohwan Lee, Seoyeong Hwang, Mingyu Kim et al. — [Investigating LLM-Powered Dissenting Minority Support in Power-Imbalanced Group Decision-Making: Counterargument and Mediation as Intervention Strategies](http://arxiv.org/abs/2606.31762v1)
  <details><summary>📄 Abstract</summary>
  Minority viewpoints are often suppressed in power-imbalanced group decision-making due to social pressure to comply with the majority. To address this problem, we developed an LLM-powered dissenting minority support system that aimed to foster attention to minority views through either AI-generated counterarguments or AI-mediated messages. We conducted a mixed-method experiment with 96 participants in 24 groups, comparing minority members' experiences across baseline, AI-counterargument, and AI-...
  </details>

- **2026-06-30** — Haoming Liu, Yuanhe Guo, Yijia Cao et al. — [Histogram-constrained Image Generation](http://arxiv.org/abs/2606.31683v1)
  <details><summary>📄 Abstract</summary>
  Diffusion models have emerged as a dominant paradigm in generative modeling, enabling high-fidelity sampling from complex data distributions. Despite impressive capabilities, controlling diffusion models to produce outputs aligned with user intent remains an open challenge, especially when balancing global coherence with local precision. Existing control mechanisms vary in the granularity of their conditioning signals. For example, textual prompts guide generation globally through high-level sem...
  </details>

- **2026-06-30** — Chanjong Im, Sebastian Diem, Thomas Mandl — [REDI: Corpus Aware Patch Ranking for DINOv3 Token Reduction](http://arxiv.org/abs/2606.31676v1)
  <details><summary>📄 Abstract</summary>
  Most token reduction methods for Vision Transformers seek favorable tradeoffs between accuracy and efficiency by pruning, merging, or pooling patch tokens. REDI (Relevance for DINOv3 Token Reduction) studies this question through a controlled supervised reference: how should a fixed token budget be allocated across patches for image classification? REDI quantizes final block DINOv3 patch representations into a visual vocabulary and derives class conditioned corpus scores using supervised TF-IDF ...
  </details>

- **2026-06-30** — Asif Hanif, Mohammad Yaqub — [ZEBRA: Zero-Shot Entropy-Regularized Prompt Learning for Base-to-Novel Generalization in Audio-Language Models](http://arxiv.org/abs/2606.31587v1)
  <details><summary>📄 Abstract</summary>
  Audio-Language Models (ALMs) achieve strong zero-shot performance by aligning audio with textual class descriptions. Although prompt learning improves accuracy on base classes through few-shot supervised adaptation, we observe a critical trade-off: it often degrades performance on novel classes, sometimes falling below zero-shot accuracy. This exposes a base-to-novel generalization gap in prompt learning for ALMs. To address this issue, we propose \textbf{ZEBRA} (Zero-shot Entropy-Regularized Pr...
  </details>

- **2026-06-30** — Koki Mizuno — [High-harmonic spin-current signatures of altermagnetic spin-group symmetry](http://arxiv.org/abs/2606.31573v1)
  <details><summary>📄 Abstract</summary>
  Spin point groups classify magnetic phases in the weak spin-orbit coupling regime and characterize the static properties of altermagnetic phases, but their dynamical consequences remain largely unexplored. Here, we derive selection rules for high-harmonic generation of charge and spin currents by extending dynamical symmetry to include spin point group operations. Since spin currents transform under both real and spin space operations, whereas charge currents transform only under real space oper...
  </details>

- **2026-06-30** — Yacouba Diarra, Nouhoum Souleymane Coulibaly, Mamadou Dembele et al. — [Building an ASR Solution for Training and Assessing Children's Reading](http://arxiv.org/abs/2606.31508v1)
  <details><summary>📄 Abstract</summary>
  Automatic speech recognition for children's reading remains underdeveloped for most African languages, including Bambara, despite its potential value for reproducible literacy assessment. We present an open-source system for assessing children's reading in Bambara, developed through an end-to-end process linking field data collection, benchmark construction, model adaptation, a reading application, and classroom validation. A mobile collection and assessment app was used to collect 55 hours of r...
  </details>

- **2026-06-30** — Chi Huang, Wenhao Zhang, Hang Yin et al. — [DrivingDepth: Sparse-Prompted Pixel-wise Scale Correction for Driving Depth Estimation](http://arxiv.org/abs/2606.31488v1)
  <details><summary>📄 Abstract</summary>
  Dense depth estimation for autonomous driving faces a geometry-scale conflict: depth foundation models deliver pixel-aligned dense visual geometry without reliable metric scale, while projected LiDAR provides metric anchors that are sparse, noisy, and misaligned with image structures. Existing sparse-prompted methods incorporate LiDAR by regenerating depth from scratch, overriding the foundation model's coherent geometry and producing structural artifacts on visually continuous surfaces. Our key...
  </details>

- **2026-06-30** — Yuchen Huang, Xiang Li, Zhenqing Ling et al. — [CDR-Bench: Evaluating Faithful Execution of Compositional, Order-Sensitive Data Refinement Recipes](http://arxiv.org/abs/2606.31435v1)
  <details><summary>📄 Abstract</summary>
  Data refinement involves executing multi-step recipes over evolving text states, where both composition and execution order of processing operators determine the outcome. While existing benchmarks either isolate text editing or entangle it with code and tool execution, it remains unclear whether LLMs can directly and faithfully execute these compositional, order-sensitive data refinement recipes. To fill this gap, we introduce CDR-Bench, a comprehensive benchmark featuring 3,462 high-quality tas...
  </details>

- **2026-06-30** — Soheyb Ribouh, Phil Polo Ditsia Di Ngoma — [Towards a Joint Task-Oriented and Generative Semantic Communication Framework for 6G Networks](http://arxiv.org/abs/2606.31426v1)
  <details><summary>📄 Abstract</summary>
  Semantic Communication (SC) has emerged as a key enabler for 6G wireless systems by transmitting task-relevant meaning rather than raw data, thereby significantly reducing bandwidth consumption while preserving communication intent. In this work, we propose an end-to-end OFDM-based semantic communication framework that integrates a semantic encoder-decoder pipeline with a neural receiver operating over a 3GPP vehicular channel. The semantic encoder extracts the underlying meaning of a visual sce...
  </details>

- **2026-06-30** — Rui Hao, Qiankun Li, Junyuan Mao et al. — [Synergistic Perception-Reasoning Governance: Grounding Medical MLLMs with Verifiable Anatomical Evidence](http://arxiv.org/abs/2607.00060v1)
  <details><summary>📄 Abstract</summary>
  Multimodal large language models (MLLMs) show strong promise for clinical VQA and radiology report generation, yet inference-time hallucinations still undermine trustworthy use: models can produce fluent conclusions that conflict with imaging evidence. Existing mitigation strategies typically rely on additional training, external retrieval/knowledge bases, or multi-stage post-hoc verification, which increases cost and pipeline complexity and often generalizes poorly across models and tasks.To ad...
  </details>

- **2026-06-30** — Shreya Rajpal, Tanawan Premsri, Parisa Kordjamshidi — [Spatial Reasoning via Modality Switching Between Language and Symbolic Representation](http://arxiv.org/abs/2606.31285v1)
  <details><summary>📄 Abstract</summary>
  Human reasoning is inherently multimodal: when problems become difficult, we rarely think in words alone. We often externalize our reasoning by sketching diagrams or drawing grids to understand the underlying conceptual structure and avoid mistakes. Building on this premise, our research investigates: (a) whether grounding multi-hop textual-spatial stories into geometry-aware modalities, such as layouts or grids, improves reasoning compared to natural language-based inference; and (b) whether a ...
  </details>

- **2026-06-30** — Kaiwen Xiong, Haonian Ji, Shi Qiu et al. — [ClawArena-Team: Benchmarking Subagent Orchestration and Dynamic Workflows in Language-Model Agents](http://arxiv.org/abs/2606.31174v1)
  <details><summary>📄 Abstract</summary>
  Production large language-model (LLM) agents are increasingly deployed not as lone problem-solvers but as managers: a main model creates specialized subagents, delegates work, and orchestrates their parallel, asynchronous returns through dynamic workflows. Whether one model can actually run such a team is largely unmeasured: existing benchmarks score a policy's own task-solving or a fixed multi-agent system's emergent behavior, but none isolate the management ability of the single LLM acting as ...
  </details>

- **2026-06-30** — Ziqi Li, Zijian Chen, Tingzhu Chen et al. — [Beyond Single Character: Evaluating MLLMs for Sentence-Level Oracle Bone Inscription Understanding](http://arxiv.org/abs/2606.31169v1)
  <details><summary>📄 Abstract</summary>
  Existing AI-assisted oracle bone inscription (OBI) visual recognition and understanding studies mainly focus on character-level, ignoring the long-form textual coherence and contextual dependencies embedded in complete divination charges. Recently, the powerful visual perception capabilities of multimodal large language models (MLLMs) have opened new possibilities for OBI information processing. In this work, we introduce S-OBI, a novel benchmark for evaluating MLLMs in Sentence-level OBI unders...
  </details>

- **2026-06-30** — Anjali Parashar, Chuchu Fan — [Scenario Generation for Testing of Autonomous Driving Systems Using Real-World Failure Records](http://arxiv.org/abs/2606.31131v1)
  <details><summary>📄 Abstract</summary>
  To ensure safe on-road behavior, pre-deployment testing and failure discovery of Autonomous Driving Systems (ADS) is crucial. Present day simulation based testing methods focus largely on mathematical models for efficient search of optimal scenarios, assuming a fixed scenario representation. On the other hand, real-world testing involves substantial manual effort to design scenario templates for testing. These templates represent distinct failure scenarios consisting of pre-deployment vehicle mo...
  </details>

- **2026-06-30** — Rui Zhou, Tianci Xie — [Fora: From Weight-Space to Function-Space Protection in Capability-Preserving Fine-Tuning](http://arxiv.org/abs/2606.31092v2)
  <details><summary>📄 Abstract</summary>
  Full fine-tuning adapts large language models to new tasks but can erode capabilities they already possess. Existing remedies protect through proxies such as parameter distances, importance penalties, output matching, or dominant singular directions of the weights, but none directly asks which activation directions the preserved capability relies on. We argue that a capability is characterized more faithfully by the activation subspace it induces than by the singular geometry of the weight matri...
  </details>

- **2026-06-30** — Ramin Pishehvar — [A Three-Phase Foundation Model for Tax-Aware Personalized Portfolio Management](http://arxiv.org/abs/2606.30997v1)
  <details><summary>📄 Abstract</summary>
  We present a three-phase deep reinforcement learning system for personalized portfolio management that addresses three limitations shared by all prior financial RL work: 1) ticker lock-in, 2) monolithic objectives , and 3) static user models. Phase 1 pretrains a ticker-identity-free cross asset encoder via self-supervised learning on a multi-asset corpus, augmented by a frozen parallel branch using Chronos, a T5-based time series foundation model, fused via a learned gating mechanism. To our kno...
  </details>

- **2026-06-30** — Runyu Lu, Yubo Wu, Ethan Kou et al. — [ASPIRE: Agentic /Skills Discovery for Robotics](http://arxiv.org/abs/2607.00272v1)
  <details><summary>📄 Abstract</summary>
  Traditional robot programming is challenging: it requires orchestrating multimodal perception, managing physical contact dynamics, and handling diverse configurations and execution failures. We introduce ASPIRE (Agentic Skill Programming through Iterative Robot Exploration), a continual learning system that autonomously writes and refines robot control programs in a code-as-policy paradigm while compounding experience into a reusable skill library. ASPIRE discovers skills that persist across tas...
  </details>

- **2026-06-30** — Bowen Jiang, William Painter Reger, Roberto Martin-Martin — [CoDex: Learning Compositional Dexterous Functional Manipulation without Demonstrations](http://arxiv.org/abs/2606.31909v1)
  <details><summary>📄 Abstract</summary>
  In this work, we study Compositional Dexterous Functional Object Manipulation (CD-FOM): tasks such as aiming and actuating a spray bottle on a plant or a glue gun on wood, which require both actuating an object's internal mechanism and controlling its pose to apply the object's function to the environment. These tasks pose significant challenges for robots due to the demanding integration of semantic understanding of the object's function, actuation mode, and application area with intricate phys...
  </details>

- **2026-06-30** — Lang Cao, Renhong Chen, Luyi Li et al. — [Z-1: Efficient Reinforcement Learning for Vision-Language-Action Models](http://arxiv.org/abs/2606.31846v1)
  <details><summary>📄 Abstract</summary>
  Vision-Language-Action (VLA) models offer a promising framework for robotic manipulation by connecting language instructions, visual observations, and continuous control. However, most existing policies remain limited by behavior cloning or supervised fine-tuning (SFT) from fixed demonstrations, which provides limited opportunity to improve from the policy's own failures. In this paper, we present Z-1, a reinforcement learning (RL) post-training framework for flow-based VLA models. Built on top ...
  </details>

- **2026-06-30** — Xiaofan Liu, Zecan Li, Zhuang Zhao et al. — [AdaTrans: Automated C to Rust Transformation via Error-Adaptive Repair](http://arxiv.org/abs/2606.31706v1)
  <details><summary>📄 Abstract</summary>
  The automated transformation of C code to Rust is challenging due to Rust's strict ownership and borrowing semantics. While Large Language Models (LLMs) show promise, they often produce code that violates these rules or relies on unsafe constructs. We propose AdaTrans, a framework that addresses these issues through three core mechanisms: a Strategy-Driven Retrieval-Augmented Generation (RAG) mechanism to map compiler errors to specific repairs, an Error-Stratified Transformation Strategy (ESTS)...
  </details>

- **2026-06-30** — Kartik Bali, Roland Aydin — [MV-GEL: Language-Driven Multi-View Geometric Entity Localization on Meshes](http://arxiv.org/abs/2606.31533v1)
  <details><summary>📄 Abstract</summary>
  Identifying and grounding precise geometric entities, such as edges, planar regions, and curved surfaces within 3D objects, is foundational to computer-aided design (CAD), robotic manipulation, and scientific simulation. Although modern Vision Language Models (VLMs) have advanced referring segmentation (RIS) in the image domain, extending such language-driven localization to structured 3D geometry is substantially harder. The 3D object appearance is highly sensitive to viewpoints; a single persp...
  </details>

- **2026-06-30** — Yao Shi, Kingfung Luo, Nan Tang et al. — [CSTrader: A Testbed for Language-Grounded Trading in a Community-Driven Virtual Asset Market](http://arxiv.org/abs/2606.31461v1)
  <details><summary>📄 Abstract</summary>
  Niche asset markets, such as Counter-Strike 2 (CS2) weapon skins, are small, volatile, and heavily driven by community discussions and platform rules. These properties make them hard for traditional quantitative models, but provide an ideal testbed for studying how large language models (LLMs) turn unstructured text into trading actions. We present CSTrader, a multi-agent framework for language-grounded trading in the CS2 skin market. The system first integrates heterogeneous signals from variou...
  </details>

- **2026-06-30** — Dongyoon Hwang, Byungkun Lee, Dongjin Kim et al. — [3D HAMSTER: Bridging Planning and Control in Hierarchical Vision Language Action Models through 3D Trajectory Guidance](http://arxiv.org/abs/2606.31329v2)
  <details><summary>📄 Abstract</summary>
  Hierarchical Vision-Language-Action (VLA) models decouple high-level planning from low-level control to improve generalization in robot manipulation. Recent work in this paradigm uses 2D end-effector trajectories predicted by a Vision-Language Model (VLM) as explicit guidance for a downstream policy. However, state-of-the-art low-level policies operate in 3D metric space on point clouds, and feeding them 2D guidance that lacks depth forces each waypoint to be assigned the depth of whatever scene...
  </details>

- **2026-06-30** — Ethan Hirschowitz, Fabio Ramos — [Warp RL: Reshaping Base Policy Distributions for Dynamics Adaptation](http://arxiv.org/abs/2606.31043v2)
  <details><summary>📄 Abstract</summary>
  Residual reinforcement learning adapts a pretrained robot policy by learning an additive correction to its actions. While effective when adaptation amounts to shifting the base policy's action distribution, additive corrections cannot change the distribution's shape, scale, or state-dependent geometry -- limitations we formalize as wrong variance, miscalibrated confidence, and non-uniform correction. We show that these matter under dynamics shift: when the base distribution is geometrically mism...
  </details>

- **2026-06-30** — Seongho Son, Sangwoong Yoon, Jiahua Tang et al. — [SWE-Router: Routing in Multi-turn Agentic Software Engineering Tasks](http://arxiv.org/abs/2607.00053v1)
  <details><summary>📄 Abstract</summary>
  Large language models (LLMs) embedded in multi-turn agentic harnesses are reshaping software engineering (SWE), but routing every task to a frontier model is wasteful when many issues admit cheap fixes. Existing LLM routers operate on the task description alone, which inherits an information-theoretic Bayes-error floor in agentic settings: a similar issue can hide either a localized typo or a multi-module refactor, and the prompt does not separate the two. We introduce SWE-Router, a value-based ...
  </details>

- **2026-06-30** — Tom Saliencro, Maya Lindqvist, Rohan Desai et al. — [FRAME: Learning the Adaptation Domain with a Mixture of Fractional-Fourier Experts](http://arxiv.org/abs/2607.00162v1)
  <details><summary>📄 Abstract</summary>
  Parameter-efficient fine-tuning (PEFT) reparameterizes weight updates in a fixed basis: low-rank adapters operate in the spatial domain, while a recent line of spectral methods operates in a fixed Fourier domain. We argue that the choice of domain is itself a design degree of freedom that should be learned, and that no single basis is optimal across tasks, layers, or tokens. We introduce Fractional-Fourier Mixture of Experts, a mixture-of-experts adapter in which every expert carries a learnable...
  </details>

- **2026-06-30** — Qian Ma, S M Rayeed, Charles V. Stewart et al. — [Identifying and Resolving Pitfalls of Knowledge-Based VQA Benchmarks: Auditing, Repairing, and Augmenting](http://arxiv.org/abs/2607.00159v1)
  <details><summary>📄 Abstract</summary>
  Knowledge-Based Visual Question Answering (KB-VQA) aims to evaluate whether Visual Language Models (VLMs) can retrieve, ground, and reason over external structured knowledge beyond visual evidence. In practice, answer accuracy is widely adopted as the primary evaluation metric, implicitly treating correctness as a proxy for knowledge-grounded reasoning. However, for existing KB-VQA benchmarks, this proxy relies on critical assumptions that are often overlooked and rendered unreliable by benchmar...
  </details>

- **2026-06-30** — Deyang Jiang, Haoran Wu, Ziyi Wang et al. — [RareDxR1: Autonomous Medical Reasoning for Rare Disease Diagnosis Beyond Human Annotation](http://arxiv.org/abs/2607.00147v1)
  <details><summary>📄 Abstract</summary>
  Rare disease differential diagnosis is a critical yet arduous clinical task, requiring physicians to identify precise phenotypes from complex, unstructured patient symptoms and execute intricate reasoning within a vast search space. However, existing AI approaches typically rely on pipeline-based phenotype extraction or retrieval-augmented generation, which suffer from critical information loss due to predefined ontologies, retrieval bottlenecks, and a lack of diagnostic logic. To address these ...
  </details>

- **2026-06-30** — Hussein Chouman, Wataru Sasaki, Tomokazu Matsui et al. — [Representation as a Bottleneck for Mechanistic Interpretability: The Manifestation Unit Protocol](http://arxiv.org/abs/2607.00089v1)
  <details><summary>📄 Abstract</summary>
  Mechanistic interpretability has produced a rich inventory of component-level analyses that characterise what neural-network components encode and how they interact. Their outputs, however, are not easily reusable: selectivity tables, circuit diagrams, and feature lists remain locked in per-study notebooks - non-composable, not queryable in natural language, and not directly actionable for downstream audit or intervention. We study the representation layer that sits between these analyses and do...
  </details>

- **2026-06-30** — Dimitrios Chatzis, Madison Hammond, Carlos Nunez et al. — [Holographic Spread Complexity from Branes and Strings](http://arxiv.org/abs/2607.00074v1)
  <details><summary>📄 Abstract</summary>
  We study Krylov spread complexity in holographic theories using genuine string-theory probes. Building on the proposal that the growth rate of spread complexity is measured by a proper momentum in the bulk, we embed the falling-particle picture in top-down examples. We first analyse a D0 brane in the type IIA AdS$_4\times {\mathbb{CP}}^3$ background dual to ABJM theory, identifying it with a dressed monopole operator in the boundary CFT. For purely radial motion the proper-momentum prescription ...
  </details>

- **2026-06-30** — Sameer Malik, Ayush Singh, Amar Prakash Azad — [PolicyGuard: From Organizational Policies to Neuro-SymbolicCompliance Review Engines](http://arxiv.org/abs/2606.32004v1)
  <details><summary>📄 Abstract</summary>
  Policy-grounded document review requires determining whether a target document complies with organization-specific policies, guidelines, or playbooks. While large language models can assist with policy interpretation and document analysis, end-to-end prompting leaves the applied policy logic implicit, making compliance decisions difficult to inspect, update, and test. We present PolicyGuard, a neuro-symbolic framework for policy-grounded document compliance review. PolicyGuard converts organizat...
  </details>

- **2026-06-30** — Peng Li, Rawal Khirodkar, Junxuan Li et al. — [LUNA: Learning Universal 3D Human Animation Beyond Skinning](http://arxiv.org/abs/2606.31981v1)
  <details><summary>📄 Abstract</summary>
  Creating photorealistic, animatable 3D human avatars from monocular images still largely depends on Linear Blend Skinning (LBS) and parametric body models, which constrain expressivity and often introduce artifacts due to imperfect fitting. We propose LUNA, an LBS-free universal neural animation model that directly maps multiple 2D controls like images, keypoints, sketches, and unseen characters into 3D Gaussian deformations, bypassing explicit body fitting. At its core, a transformer-based moti...
  </details>

- **2026-06-30** — Shiyi Chen, Nicholas Saban, Collin Hargreaves et al. — [TreeAgent: A Generalizable Multi-Agent Framework for Automated Bias Labeling in Forestry via Compiled Expert Rules and Vision-Language Models](http://arxiv.org/abs/2606.31976v1)
  <details><summary>📄 Abstract</summary>
  Human-labeled data are widely used as reference annotations in ML, despite known variability across annotators in many expert-driven domains. In addition, expert annotation is slow, inconsistent, and remains a major bottleneck for scaling tasks like tree height bias classification in forestry remote sensing. We propose a multi-agent system (MAS) that orchestrates expert decision trees with Vision-Language Models (VLMs), treating the decision tree as a structural prior while VLMs perform localize...
  </details>

- **2026-06-30** — Xiaoyu Liu, Huan Wang, Fan Li et al. — [InstanceControl: Controllable Complex Image Generation without Instance Labeling](http://arxiv.org/abs/2606.31924v1)
  <details><summary>📄 Abstract</summary>
  Controllable image generation methods, such as ControlNet, have demonstrated a remarkable capacity to introduce visual conditions(e.g., depth maps) to guide image generation. However, these methods often struggle with complex multi-instance scenes, frequently leading to attribute confusion among instances. While recent approaches attempt to mitigate this via manual instance labeling, such requirements are labor-intensive. In this paper, we propose InstanceControl, a novel multi-instance controll...
  </details>

- **2026-06-30** — Zhaoyang Luo, Runmin Dong, Miao Yang et al. — [Attend, Transform, or Silence: Operator-Level Visual Skipping for Efficient Multimodal LLM Inference](http://arxiv.org/abs/2606.31903v1)
  <details><summary>📄 Abstract</summary>
  Multimodal large language models (MLLMs) increasingly process long visual-token sequences, increasing the overall inference computation. Existing acceleration methods usually remove visual tokens or skip visual-token updates in entire layers, but these coarse strategies may discard fine-grained evidence or suppress useful operators together with redundant ones. In this paper, we study visual-token computation from an answer-observable perspective and find that late visual-token updates can remai...
  </details>

- **2026-06-30** — Yu Wei — [Better Understanding, Understanding Better](http://arxiv.org/abs/2606.31892v1)
  <details><summary>📄 Abstract</summary>
  "Any fool can know; the point is to understand." A well-known remark often attributed to Einstein captures a widely shared intuition: understanding is more than merely knowing. Yet epistemic logic has paid relatively little attention to understanding, despite its central role in contemporary epistemology, philosophy of science, and recent debates about AI. A recurring theme in the philosophical literature is that, unlike knowledge, understanding comes in degrees: one may understand something mor...
  </details>

- **2026-06-30** — Ryo Murai, Sizhuo Liu, Katsuhiko Sano — [Analytic Cut in Epistemic Logics with Distributed Knowledge](http://arxiv.org/abs/2606.31886v1)
  <details><summary>📄 Abstract</summary>
  Distributed knowledge is a notion of group knowledge studied in multi-agent epistemic logic. Semantically, the distributed knowledge of a group is interpreted via an accessibility relation given by the intersection of the epistemic accessibility relations of the agents in that group. This paper investigates sequent calculi for epistemic logics of distributed knowledge based on K45, KD45, and S5. While cut elimination holds in existing sequent calculi for modal logics K45 and KD45, it fails in al...
  </details>

- **2026-06-30** — Ruijia Zhang, Jiacheng Zhu, Hanqing Zhu et al. — [Geometry-Preserving Orthonormal Initialization for Low-Rank Adaptation in RLVR](http://arxiv.org/abs/2606.31813v1)
  <details><summary>📄 Abstract</summary>
  Low-rank adaptation (LoRA) and its variants enable parameter-efficient fine-tuning of large language models under the supervised fine-tuning (SFT) paradigm. However, their efficacy and behavior under Reinforcement learning with verifiable rewards (RLVR) are less well understood. In particular, two structurally initialized LoRA variants, PiSSA and MiLoRA, which outperform standard LoRA under SFT, can underperform standard LoRA under RLVR and may even exhibit training instability. These observatio...
  </details>

- **2026-06-30** — Manis Chaudhuri, Pavel Krainov, Dmitry Astakhov et al. — [Plasma double layer development during high power EUV exposure](http://arxiv.org/abs/2606.31797v1)
  <details><summary>📄 Abstract</summary>
  The development of electrostatic plasma double layer (DL) at the boundary of Extreme Ultra Violet (EUV) exposed and un-exposed region in the bulk volume has been confirmed by 3DPIC (Particle-In-Cell) simulations in the context of fast transient high power EUV exposures. It is found that the DL exists only for short time scale during EUV-ON time period (~ 70ns) and disappears soon after EUV is OFF. Such DL fingerprint appears above a certain critical value of EUV beam energy (~ 0.1mJ) and it tran...
  </details>

- **2026-06-30** — Jesus S. Aguilar-Ruiz — [When to Truncate a Feature Ranking: A Residual-Overlap Stopping Rule for Subset Selection](http://arxiv.org/abs/2606.31686v1)
  <details><summary>📄 Abstract</summary>
  Feature rankings are widely used in supervised feature selection because they are simple, scalable and easy to interpret. Variables are first ranked by a relevance score, and a subset is then obtained by retaining the top-ranked variables. Although the first stage has been extensively studied, the second is often governed by an arbitrary cardinality, an empirical threshold or cross-validation, without a direct interpretation. This raises a basic question: given a feature ranking, when is there e...
  </details>

- **2026-06-30** — Wenhao Li, Jinhao Dong, Hailin Zhang et al. — [RaBitQCache: Rotated Binary Quantization for KVCache in Long Context LLM Inference](http://arxiv.org/abs/2606.31519v1)
  <details><summary>📄 Abstract</summary>
  Long-context Large Language Model inference is severely bottlenecked by the massive Key-Value (KV) cache, yet existing sparse attention methods often suffer from static fixed-budget (Top-k) retrieval or rely on proxy scores that are computationally expensive and biased. To address these limitations, we propose RaBitQCache, a novel sparse attention framework that utilizes randomized rotated binary quantization and high-throughput binary-INT4 arithmetic to efficiently estimate attention weights. O...
  </details>

- **2026-06-30** — Dong Bi, Yongqi Zhao, Paul Kovacevic et al. — [A Large-Language-Model Supported Personalized Driving Framework for Lane Change in Highway Scenarios](http://arxiv.org/abs/2606.31483v2)
  <details><summary>📄 Abstract</summary>
  Personalized driving can improve the user acceptance of automated driving systems. However, existing methods still provide limited support for translating natural-language driving preferences, especially when such preferences are expressed implicitly, into executable and distinguishable driving behaviors. This paper proposes a large language model (LLM)-supported personalized driving framework for highway lane-change scenarios. The framework maps natural-language driving commands to executable p...
  </details>

- **2026-06-30** — Deniz Bickici, Michael Pabst, Shohei Mori et al. — [Think While You Map: Asynchronous Vision-Language Agents for Incremental 3D Scene Graphs](http://arxiv.org/abs/2606.31471v1)
  <details><summary>📄 Abstract</summary>
  Open-vocabulary 3D scene graph methods typically operate in two stages: first reconstruct, then enrich with vision-language models, leaving the graph unqueryable during exploration. We argue that this sequential coupling is unnecessary and propose an asynchronous architecture in which lightweight online mapping runs concurrently with heavyweight semantic refinement. A probabilistic voxel-based backbone maintains stable object identities incrementally, while background VLM agents progressively en...
  </details>

- **2026-06-30** — Keito Inoshita — [Who Determines the Meaning of an Emotion? Affective Sovereignty as an Epistemic Consequence of Measurement Limits](http://arxiv.org/abs/2606.31442v1)
  <details><summary>📄 Abstract</summary>
  Emotion-sensing AI is rapidly becoming embedded in vehicles, home appliances, dialogue agents, and social infrastructure, giving rise to a sphere in which emotion is no longer confined to individual experience but is instead observed and computed at a societal scale, a domain we term the Affectosphere. Yet a central normative question in this domain has remained underexplored: who has the final authority to determine the meaning of one's own emotion? This study addresses the question from the ep...
  </details>

- **2026-06-30** — Onkar Jadhav, Tim French, Matthew Rayson et al. — [Patch-PODiff-ViT: Structured Latent Diffusion with Patchwise POD for Super-Resolution and Uncertainty Quantification](http://arxiv.org/abs/2606.31290v1)
  <details><summary>📄 Abstract</summary>
  Diffusion models enable probabilistic super-resolution and conditional generation, but pixel-space methods are computationally expensive and learned latent spaces often lack interpretable uncertainty quantification. We introduce Patch-PODiff-ViT, a structured latent diffusion framework in which the latent space is defined by patchwise Proper Orthogonal Decomposition (POD), a fixed linear orthonormal basis over local patches, rather than learned by a nonlinear autoencoder. This yields low-dimensi...
  </details>

- **2026-06-30** — Zhengxuan Wang, Haohan He, Mengying Zhou — [Towards Inclusive Mobility Modeling: Characterizing and Evaluating Elderly Trajectory Patterns in Urban Systems](http://arxiv.org/abs/2606.31207v1)
  <details><summary>📄 Abstract</summary>
  The rapid advance of smart cities increasingly depends on trajectory data mining, yet underrepresented demographic groups, particularly the elderly, are often sparsely represented in public mobility datasets. This underrepresentation can introduce systematic bias into mobility modeling and downstream urban planning. Using the 2016-2020 Jersey City subset of the Citi Bike System Data, this study quantitatively examines how the absence of underrepresented subgroups' mobility signatures affects mob...
  </details>

- **2026-06-30** — Qianchu Liu, Sheng Zhang, Guanghui Qin et al. — [HealthAgentBench: A Unified Benchmark Suite of Realistic Agentic Healthcare Environments for Challenging Frontier AI Agents](http://arxiv.org/abs/2606.31179v1)
  <details><summary>📄 Abstract</summary>
  As AI agents become increasingly capable of complex, long-horizon reasoning, rigorous and holistic evaluation is essential for measuring progress toward real-world healthcare applications. We introduce HealthAgentBench, a suite of 54 agentic healthcare tasks across 7 categories each with its unique environment. The benchmark suite spans diverse workflows throughout the patient journey and a broad range of modalities. Each task is designed to replicate an end-to-end clinical workflow: given minim...
  </details>

- **2026-06-30** — Woosung Kim, Youngjun Suh, Jinho Lee et al. — [AETDICE: Unified Framework and Offline Optimization for Nonlinear Multi-Objective RL](http://arxiv.org/abs/2606.31178v1)
  <details><summary>📄 Abstract</summary>
  Optimizing nonlinear preferences in multi-objective reinforcement learning (MORL) is essential for capturing complex trade-offs like risk aversion or fairness. However, such non-linearity has historically bifurcated nonlinear MORL objectives into two distinct paradigms: Scalarized Expected Return (SER) and Expected Scalarized Return (ESR). While SER requires global-level optimization and ESR requires non-Markovian policies, leading to fragmented optimization strategies, we bridge this divide thr...
  </details>

- **2026-06-30** — Lingjie Chen, Yuanchen Bei, Haobo Xu et al. — [TAG-DLM: Diffusion Language Models for Text-Attributed Graph Learning](http://arxiv.org/abs/2606.31166v1)
  <details><summary>📄 Abstract</summary>
  Text-attributed graphs (TAGs), where each node carries a natural language description, require models to jointly reason over text and graph topology. Existing approaches often handle the two modalities separately: graph neural networks operate on shallow text features, while hybrids of LLMs and graphs use the language model mainly as a text encoder and delegate structure learning to a separate graph module. We propose method that unifies textual reasoning and graph message passing within a maske...
  </details>

- **2026-06-30** — Micah M. Borrero, Max Z. Li — [Augmenting airline networks using airside-to-airside buses to strengthen system resilience under disruptions](http://arxiv.org/abs/2606.31142v1)
  <details><summary>📄 Abstract</summary>
  Each year, disruptions in the air transportation network strand millions of passengers and cost airlines billions in revenue. Airline networks prioritize operational and cost efficiency through hub-and-spoke structures that maximize revenue; however, these hubs also act as critical choke points during disruptions. Previous studies have focused on reactionary measures in response to air transportation network disruptions, whereas this work proposes a proactive strategy to improve resilience by re...
  </details>

- **2026-06-30** — Chuanbo Zhu, Wuyou Zhou, Rongxiu Zhong et al. — [UniSAE: Unified Speech Attribute Editing on Speaker, Emotion and Low-Level Content via Discrete Phonetic Posteriorgram Modelling](http://arxiv.org/abs/2606.31128v1)
  <details><summary>📄 Abstract</summary>
  Speech editing aims to modify specific portions of an utterance while preserving the remaining speech. Existing approaches primarily focus on word-level content modification and typically treat content, speaker, and emotion editing as separate tasks, limiting both editing granularity and flexibility. We propose UniSAE, a unified speech attribute editing framework which supports composable speaker, emotion and content editing from sub-phoneme to word level within a single architecture. UniSAE int...
  </details>

- **2026-06-30** — Davy Guan, Lu Zhang, Asiri Wijesinghe et al. — [Can Tabular In-Context Learners Generalize to Biomolecular Property Prediction?](http://arxiv.org/abs/2606.31126v1)
  <details><summary>📄 Abstract</summary>
  Predicting biomolecular properties from limited labeled data is a central bottleneck in protein engineering and small-molecule design. As strong pretrained encoders now supply rich fixed-length representations, the difficulty has shifted from representation learning to building a data-efficient predictor for the few-shot regime. Tabular foundation models such as TabPFN3 and TabICL are unlikely candidates for this role: they are in-context learners pretrained on synthetic tables drawn from random...
  </details>

- **2026-06-30** — Zihan Chen, Songwei Dong, Chengshuai Shi et al. — [The Past Is Prologue: A Plug-in Controller for Selective Updates in Sequentially Evolving LLM Memory](http://arxiv.org/abs/2606.31121v1)
  <details><summary>📄 Abstract</summary>
  Sequentially evolving LLM memory enables agents to reuse past experience, but existing systems usually deploy each locally generated memory update without checking whether it improves future behavior. As a result, updates that help the current task may overwrite useful knowledge, introduce over-specific rules, or bias the final memory toward recent examples. We propose Janus, a plug-in memory controller that decides whether to accept a candidate memory update or retain the previous memory. To ma...
  </details>

- **2026-06-30** — Ashish Hallur, Thomas Thebaud, Georgi Tinchev et al. — [Reference-Based Prosody and Rhythm Evaluation for Spoken Dialogue Systems](http://arxiv.org/abs/2606.31055v1)
  <details><summary>📄 Abstract</summary>
  Speech-to-speech (S2S) AI agents are advancing rapidly, yet evaluation lacks interpretable speech-native measures for conversational prosody and rhythm. Because $F_0$, speaking rate, articulation rate, and pausing shift with model-predicted speaker traits and interaction state, pooled human statistics can be poorly calibrated for evaluating a particular output. Using 4000+ hours of dyadic English conversation from the Seamless Interaction dataset, we construct matched reference regimes for $F_0$...
  </details>

- **2026-06-30** — Hamidah Oderinwale, David Atkinson, Rachel Hong et al. — [Partially ordering software licenses](http://arxiv.org/abs/2606.31032v1)
  <details><summary>📄 Abstract</summary>
  Licenses are legal instruments that inventors may use to protect the technologies they build and regulate how they are used -- however, the nature of their authorship and selection means that how they are interpreted, chosen, and enforced is largely unstructured. In practice, this makes it difficult to compare licenses at scale -- when is one license considered more permissive than the other, and when are their terms incomparable to each other? Currently, there is a growing list of licenses that...
  </details>

- **2026-06-30** — Sergio Hernández-Gutiérrez, Matteo Merler, Ilze Amanda Auzina et al. — [QVal: Cheaply Evaluating Dense Supervision Signals for Long-Horizon LLM Agents](http://arxiv.org/abs/2606.32034v1)
  <details><summary>📄 Abstract</summary>
  LLM agents increasingly act over long horizons, where a single trajectory can contain hundreds or thousands of actions. In these settings, outcome-only rewards provide too sparse guidance, failing to inform the model about the goodness of intermediate actions. Dense supervision methods aim to solve this problem by scoring intermediate steps, from intrinsic confidence to self-distillation and embedding similarities. However, it is common practice to evaluate them by measuring the downstream perfo...
  </details>

- **2026-06-30** — Ye Chen, Xuanhong Chen, Yupeng Zhu et al. — [World Narrative Model for Highly Controllable Video Generation: A Paradigm Shift from Pixel Sampling to Physical World Orchestration](http://arxiv.org/abs/2606.31946v1)
  <details><summary>📄 Abstract</summary>
  The fundamental obstacle to industrial grade video generation is the lack of controllability: existing models treat video as a pixel distribution sampling problem, bypassing the explicit, instance level $4D$ $(3D + T)$ physical world. Consequently, content creators cannot specify geometry, motion, camera parameters, or lighting in a deterministic, quantitative way, leading to the infamous ''gacha'' loop that makes professional content creation prohibitively inefficient and expensive. To address ...
  </details>

- **2026-06-30** — Renan Souza, Daniel Rosendo, Kelsey Carter et al. — [An Agentic AI Framework to Accelerate Scientific Discovery in Plant Phenotyping](http://arxiv.org/abs/2606.31831v1)
  <details><summary>📄 Abstract</summary>
  High-throughput plant phenotyping now generates image derived datasets far faster than scientists can analyze them. At Oak Ridge National Laboratory's Advanced Plant Phenotyping Laboratory (APPL), automated stations image hundreds of plants daily across multiple remote sensing modalities; yet, trait extraction and interpretation remain manual, expert-bound, and strictly post-hoc, making analysis, not acquisition, the binding constraint on discovery. We present an end-to-end agentic AI framework ...
  </details>

- **2026-06-30** — Khashayar Etemadi, Zhendong Su — [JETO-Bench: A Reproducible Benchmark for Execution Time Improvement Patches in Java](http://arxiv.org/abs/2606.31767v1)
  <details><summary>📄 Abstract</summary>
  Automated fixing of performance issues is gaining increasing attention. However, existing benchmarks of execution time improvement patches are fixed datasets that target Python, C++, or .NET and cannot be extended to new patches according to user-defined configurations. In this paper, we present JETO-Mine, the first configurable and reusable tool for automatically creating reproducible benchmarks of execution time improvement patches (ETIPs) in real-world Java projects. JETO-Mine employs a three...
  </details>


## 📊 统计 / Statistics

| 分类 / Category | 论文数 / Count |
|------|--------|
| jailbreak | 536 |
| prompt-injection | 438 |
| memory-poisoning | 33 |
| tool-use-attack | 89 |
| backdoor | 379 |
| adversarial-attack | 520 |
| privacy-leakage | 3612 |
| steganography | 49 |
| misuse | 782 |
| red-teaming | 104 |
| vulnerability | 2305 |
| defense | 1926 |
| alignment | 1744 |
| robustness | 1562 |
| watermark | 153 |
| unlearning | 81 |
| agent-safety | 48 |
| benchmark | 52 |
| survey | 234 |
| other | 5010 |

---

📚 **全部 19657 篇论文**（2022 至今）请访问 [GitHub Pages](https://ny1024.github.io/AgentSafety-Papers/) 查看完整列表、搜索与筛选。

*Generated by AgentGuard at 2026-07-05 03:26:10*