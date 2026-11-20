<div align="center">

# AgentGuard 🛡️

**Daily Tracking of LLM Agent Security Papers on arXiv**

[![Auto Update](https://github.com/NY1024/AgentSafety-Papers/actions/workflows/daily-update.yml/badge.svg)](https://github.com/NY1024/AgentSafety-Papers/actions/workflows/daily-update.yml)
[![Papers](https://img.shields.io/badge/Papers-37861-blue)](#)
[![License](https://img.shields.io/badge/License-MIT-green)](#)

</div>

---

## 📖 简介 / Introduction

自动追踪 arXiv 上大模型 Agent 安全方向的最新论文，每日更新，关键词智能分类。

*Automatically tracking the latest LLM Agent security papers on arXiv, updated daily with keyword-based classification.*

**最近更新 / Last Updated**: 2026-11-20 00:12 ｜ **论文总数 / Total Papers**: 37861（近 30 天 / Recent 30 days: 3982）

🌐 **[GitHub Pages](https://ny1024.github.io/AgentSafety-Papers/)** — 查看全部 37861 篇论文（含摘要、分类筛选、搜索）/ View all 37861 papers with abstracts, filters & search

## 📑 分类导航 / Category Navigation

- **[jailbreak](#-jailbreak)** — 越狱攻击 / Jailbreak Attacks — 725
- **[prompt-injection](#-prompt-injection)** — 提示注入攻击 / Prompt Injection Attacks — 694
- **[memory-poisoning](#-memory-poisoning)** — 记忆投毒与篡改 / Memory Poisoning & Tampering — 59
- **[tool-use-attack](#-tool-use-attack)** — 工具使用攻击 / Tool-Use Attacks — 178
- **[backdoor](#-backdoor)** — 后门与投毒攻击 / Backdoor & Poisoning Attacks — 563
- **[adversarial-attack](#-adversarial-attack)** — 对抗攻击 / Adversarial Attacks — 676
- **[privacy-leakage](#-privacy-leakage)** — 隐私泄露 / Privacy Leakage — 4635
- **[steganography](#-steganography)** — 隐写与隐蔽通信 / Steganography & Covert Communication — 93
- **[misuse](#-misuse)** — 滥用与误用 / Misuse & Abuse — 1335
- **[red-teaming](#-red-teaming)** — 红队测试 / Red Teaming — 157
- **[vulnerability](#-vulnerability)** — 漏洞与攻击面 / Vulnerabilities & Attack Surfaces — 4082
- **[defense](#-defense)** — 防御与防护方法 / Defense & Protection Methods — 4004
- **[alignment](#-alignment)** — 对齐与安全约束 / Alignment & Safety Constraints — 3751
- **[robustness](#-robustness)** — 鲁棒性与可靠性 / Robustness & Reliability — 4106
- **[watermark](#-watermark)** — 水印与溯源 / Watermarking & Provenance — 775
- **[unlearning](#-unlearning)** — 机器遗忘 / Machine Unlearning — 124
- **[agent-safety](#-agent-safety)** — Agent 安全框架 / Agent Safety Frameworks — 67
- **[benchmark](#-benchmark)** — 安全评测与基准 / Safety Benchmarks & Evaluation — 75
- **[survey](#-survey)** — 综述与系统化 / Surveys & Systematization — 464
- **[other](#-other)** — 其他安全相关 / Other Security-Related — 11298

## 📄 近期论文 / Recent Papers (Last 30 Days)

> 仅展示最近 30 天中最新的 500 篇论文（含日期、作者、摘要）。近 30 天共 3982 篇，完整 37861 篇论文列表请访问 [GitHub Pages](https://ny1024.github.io/AgentSafety-Papers/)

> Showing the latest 500 of 3982 papers from the last 30 days (with date, authors & abstract). For the full list of 37861 papers, visit [GitHub Pages](https://ny1024.github.io/AgentSafety-Papers/)

### 📂 jailbreak
*越狱攻击 / Jailbreak Attacks* — 4 papers

- **2026-11-18** — Yan Qiu, Yuanyuan Li — [Jailbreak Detection on Large Language Models via Contrastive Prototype Structures](http://arxiv.org/abs/2611.24936v1)
  <details><summary>📄 Abstract</summary>
  Jailbreak attempts and harmful prompts remain a challenge for the safe deployment of large language models. We study whether contrastively learned representations can support safety detection without training an additional downstream classifier. We propose Jailbreak Detection with Prototype Inference (JDPI), which uses binary safety labels to construct harmful and benign prototypes and makes predictions from relative prototype distances. JDPI uses only binary safety labels for encoder adaptation...
  </details>

- **2026-11-17** — Weihang Liu, Qianqian Xu, Yangbangyan Jiang et al. — [Dressed in Authority: Practical Black-Box Jailbreaking of MLLMs via Visual Trust Bias](http://arxiv.org/abs/2611.22292v1)
  <details><summary>📄 Abstract</summary>
  Multimodal large language models (MLLMs) are rapidly advancing, yet their safety remains a critical concern, especially under jailbreak attempts. Existing MLLM jailbreaks either inject fragile adversarial perturbations into irrelevant images or synthesize toxic visual cues to achieve text-driven attack intents. In contrast, a more practical MLLM jailbreak emphasizes enhancing attack efficacy directly on naturally occurring harmful image-text pairs. We address this problem by proposing Visual Tru...
  </details>

- **2026-11-17** — Zexuan Fei, Zhengnan Guo, Yiming Luo et al. — [EGS: A Complementary Safety Framework for Educational LLMs](http://arxiv.org/abs/2611.22203v1)
  <details><summary>📄 Abstract</summary>
  Large Language Models (LLMs) offer strong potential for personalized education, but adolescent-facing deployment raises risks of toxic, biased, misleading, or developmentally inappropriate content. We argue that educational safety should move beyond binary refusal: student queries are often ambiguous or curiosity-driven, requiring contextual guidance rather than simple blocking. We introduce the Educational Guardrail System (EGS), a lightweight, model-agnostic runtime framework that complements ...
  </details>

- **2026-11-16** — Ana Clara Zoppi Serpa, Anderson Rocha, Hélio Pedrini — [Eight in Ten LLMs Leak System-Prompt Secrets: Nevan, an Agentic Capture-the-Flag Study](http://arxiv.org/abs/2611.21956v1)
  <details><summary>📄 Abstract</summary>
  We audit instruction-hierarchy enforcement across 363 text-in/text-out models from the OpenRouter catalog. The research question we answer with this experiment is which models disclose a protected secret embedded in the system prompt, and through which techniques. Each model guards a secret 16-character flag set in its system prompt, while an artificial intelligence (AI) agent (OpenCode, powered by DeepSeek V4.1 Flash), steered by a human researcher, tries to persuade it to emit the flag. The fl...
  </details>


### 📂 prompt-injection
*提示注入攻击 / Prompt Injection Attacks* — 9 papers

- **2026-11-18** — Lipeng He, Yihan Wang, Jiawen Zhang et al. — [PIPETTE: Prompt Injection Purple-Teaming for Robust LLM Agents](http://arxiv.org/abs/2611.24362v1)
  <details><summary>📄 Abstract</summary>
  Large language model (LLM) agents routinely interact with untrusted external data, exposing them to indirect prompt injection (IPI) attacks that hijack agents into executing attacker-chosen tasks. To uncover these vulnerabilities at scale, automated red-teaming methods often leverage reinforcement learning (RL) to generate attacks that achieve high attack success rates (ASR). Model developers use the attacks discovered during internal red-teaming to harden agents through adversarial training bef...
  </details>

- **2026-11-18** — Stavros Damianakis, Konstantinos Psounis — [AutoPI: Taxonomy-Guided Adaptive Red Teaming for Prompt Injection in LLM Agents](http://arxiv.org/abs/2611.24313v1)
  <details><summary>📄 Abstract</summary>
  Prompt injection is the dominant unsolved security risk for LLM agents, and the community now agrees that robustness must be measured against adaptive attackers rather than fixed benchmark injections. Many adaptive red teamers exist, and most are built to maximize attack success rate (ASR). Yet ASR counts how often a target breaks, not in how many different ways. A red teamer can achieve a high ASR by reusing a few techniques that work, leaving the others untested and absent from the attacks use...
  </details>

- **2026-11-18** — Haoyang Liu, Yinong Xu, Zhe Lang et al. — [What Survives the Shift from Text to Pixels? Conditional Protection against Prompt Injection in Image-Rendered Documents](http://arxiv.org/abs/2611.24231v1)
  <details><summary>📄 Abstract</summary>
  Multimodal language models increasingly answer questions over external documents, exposing them to indirect prompt injection: commands planted in untrusted content to hijack the response. Rendering untrusted content as page images lowers attack success on average, leaving open which injected operations survive rendering, at what utility cost, and whether failed image attacks reflect unread commands or commands read but not followed. We pair text and page-image versions of 191 English question-an...
  </details>

- **2026-11-17** — Deep Shah, Nehal Kathrotia — [Securing and Auditing Long-Horizon LLM Agents: State-Transfer Auditing and Controls in the Agent Harness](http://arxiv.org/abs/2611.23346v1)
  <details><summary>📄 Abstract</summary>
  Long-horizon LLM agents across codebases, web browsers, and enterprise infrastructure rely on an execution harness to move state between the working context, session history, persistent memory, and external environment. While conventional execution traces log model prompts and tool calls, critical security and reliability failures occur during state transfers: a transfer can admit unchecked content (indirect prompt injections, unverified memory writes), rewrite state lossily (context compaction ...
  </details>

- **2026-11-17** — Stanley Akingbola, Ugbede Ibrahim, Yan Lin Aung et al. — [Network-Exposed Configuration Attacks on LLM-Controlled Social Robots](http://arxiv.org/abs/2611.22761v1)
  <details><summary>📄 Abstract</summary>
  Large language models (LLMs) in embodied robots create security dependencies beyond inference. We investigate a network-exposed configuration attack on the Pollen Robotics Reachy Mini Lite, allowing an unauthenticated attacker to replace personality settings and the cloud LLM's system prompt through a management interface, without adversarial conversational input. Eleven prompt-injection attempts across five categories were reported as resisted, whereas both configuration-layer attack paths prod...
  </details>

- **2026-11-17** — Chaklam Cheong, Tiancong Cao, Qi Li et al. — [GapLeak: When Privacy-Preserving LLM-based Web Agents Become a Privacy Risk](http://arxiv.org/abs/2611.22223v1)
  <details><summary>📄 Abstract</summary>
  Large Language Model (LLM)-based web agents rely on data minimization and least privilege to protect user privacy. We show that these principles are necessary but insufficient: they constrain authorized sources, but not higher-sensitivity sources that remain reachable. A website can request a field unavailable from authorized sources, creating an information gap. To complete the task, a goal-driven agent may escalate to reachable but unauthorized sources and disclose accumulated sensitive inform...
  </details>

- **2026-11-16** — Devki Nandan Jha, Shubh Anand, Karthick Keeranagere Krishnaiah et al. — [Threat Landscape of Vibe Coding and the Road to Secure Autonomy](http://arxiv.org/abs/2611.21822v1)
  <details><summary>📄 Abstract</summary>
  Vibe coding is reshaping software development, enabling faster implementation and allowing individuals with limited programming experience to describe requirements in natural language while AI agents write, test, and deploy the code. As these agents evolve into autonomous systems that execute commands, manage dependencies, access cloud resources, and interact with other agents, their security risks extend beyond incorrect code to actions with direct consequences for software systems. Although re...
  </details>

- **2026-11-16** — Nikolaos Kekatos, Georgios Koutidis, Konstantinos Antonakopoulos et al. — [RESILAGENT: A Three-Pillar Architecture for Cyber-Physical Resilience in Electrical Power and Energy Systems](http://arxiv.org/abs/2611.21480v1)
  <details><summary>📄 Abstract</summary>
  Electrical Power and Energy Systems face hybrid threats that combine cyber intrusions, physical sabotage and climate-driven stress, and routinely outpace today's siloed monitoring stacks. We present RESILAGENT, a concept architecture organised around three operational pillars, Sensing & Data Intelligence, Resilience Analytics & Reporting, and Incident Response & Recovery, mediated by a Cloud-based Orchestrator and exercised through a closed Detect-Simulate-Decide-Sign loop. The framework fuses a...
  </details>

- **2026-11-16** — Sahaya Jestus Lazer, Kshitiz Aryal, Maanak Gupta et al. — [Evaluating Authorization and Trust Boundaries in Agentic Orchestration Frameworks](http://arxiv.org/abs/2611.21259v1)
  <details><summary>📄 Abstract</summary>
  Agentic AI systems extend large language models with tools, memory, and multi-agent collaboration, introducing security risks at orchestration boundaries. These risks depend on how identities are represented, operations are authorized, and instructions or information propagate between components. We evaluate LangChain, LangGraph, AutoGen, and OpenClaw through twelve experiments mapped to the OWASP Top 10 for Agentic Applications using a common LLM (gpt-4o-mini). The experiments cover prompt inje...
  </details>


### 📂 tool-use-attack
*工具使用攻击 / Tool-Use Attacks* — 3 papers

- **2026-11-18** — Bonan Ruan, Yuhao Sun, Jiahao Liu et al. — [Guarding the Kingdom of Skill-Based Agents in the AI Dynasty of Computation: Control-Flow Integrity for Agent Skills](http://arxiv.org/abs/2611.24185v1)
  <details><summary>📄 Abstract</summary>
  Control-flow integrity (CFI) confines a program to a control-flow graph fixed ahead of time. Procedural agent skills move this control flow into prompt text, and a large language model (LLM) agent decides at runtime whether each step runs in its reasoning, a tool call, or a script. The procedure's control skeleton survives, but its enforceability depends on where each step runs. Many violations, such as overwriting a file before validation, use only operations the skill requires, so permission a...
  </details>

- **2026-11-18** — Yuelin Han — [Weighing the Envelope: Component Weight and Arbitration in Envelope-Layer Defenses for a Single LLM Agent](http://arxiv.org/abs/2611.23844v1)
  <details><summary>📄 Abstract</summary>
  The envelope layer is the channel through which malicious content enters an LLM agent. Prior work established label and memory effects on multi-agent A2A envelopes, but the weight structure when MCP tools and memory coexist in a single agent remains unclear. Our threat model assumes an attacker pre-plants a malicious tool and poisons long-term memory; a benign user request inadvertently triggers it, and the attacker never enters the conversation. Following GDA Measurement and A/B/C/D, we measure...
  </details>

- **2026-11-18** — Nami Cho, Shailja Gupta — [SCAFFOLD: Toward Warrant-Preserving Evidence Transport for Reusable LLM-Agent Skills](http://arxiv.org/abs/2611.23990v1)
  <details><summary>📄 Abstract</summary>
  An agent skill that succeeded yesterday may be executable today without being justified for reuse today. Tests may cover only observable contract clauses, outcome oracles may be absent, evaluations may inherit the same erroneous specification, and permissions or dependencies may change between validation and invocation. We argue that the appropriate unit of prospective trust is a Warranted Reuse Claim (WRC): a defeasible, claim-specific authorization tied to a versioned skill, target context, ev...
  </details>


### 📂 backdoor
*后门与投毒攻击 / Backdoor & Poisoning Attacks* — 3 papers

- **2026-11-18** — Zhizhuo Kou, Sizai Hou, Jian Yang et al. — [IDEA: Intent-Dominance Evidence Audit for Inference-Time Backdoor Detection in GUI Agents](http://arxiv.org/abs/2611.24102v1)
  <details><summary>📄 Abstract</summary>
  Organizations increasingly deploy downloaded open-weight GUI agents. A backdoored agent passes acceptance tests on clean data and misbehaves only when a visual trigger appears on screen, turning an unvetted checkpoint into a supply-chain risk. However, existing sample-level detectors target image classifiers and CLIP-style encoders, leaving step-level backdoor detection for GUI agents unaddressed. On clean steps, the instruction drives the action; when an unreferenced screen region hijacks the s...
  </details>

- **2026-11-18** — Siquan Huang, Yijiang Li, Xingfu Yan et al. — [DetectViT: Test-time Backdoor Detection for Vision Transformers via Inter-Head Attention Discrepancy](http://arxiv.org/abs/2611.23770v1)
  <details><summary>📄 Abstract</summary>
  Vision Transformers (ViTs) now underpin the visual encoders of most multimodal models, but this success comes at a cost: relying on third-party pretrained checkpoints leaves these systems open to backdoor attacks. Existing test-time detection methods rely on either the predicted label or intermediate embeddings, limiting their applicability across diverse tasks and incurring substantial computational overhead. In this work, we study how backdoor triggers affect the multi-head attention mechanism...
  </details>

- **2026-11-17** — Zane Fu, Yanzhao Zheng, Jinze Liu et al. — [As Student Rollouts Continue, Visual Backdoors Keep Growing](http://arxiv.org/abs/2611.22446v1)
  <details><summary>📄 Abstract</summary>
  Conventional knowledge distillation can facilitate the propagation of backdoors from teacher models to student models. However, how this risk manifests in On-Policy Distillation (OPD) remains insufficiently studied. OPD has recently emerged as an important post-training paradigm for Vision-Language Models (VLMs). Unlike traditional offline distillation, OPD does not require teacher-generated responses. Instead, it uses the teacher's probability distributions to supervise response trajectories ge...
  </details>


### 📂 adversarial-attack
*对抗攻击 / Adversarial Attacks* — 4 papers

- **2026-11-18** — Jiayou Zhu, Peng Guo, Litian Zhang et al. — [RECLAIM: Robot-Vision-Informed Adversarial Patch Defense via Embodied Attention Feedback](http://arxiv.org/abs/2611.24494v1)
  <details><summary>📄 Abstract</summary>
  Vision-language-action policies control embodied agents through a perception-action loop grounded in physical interaction, where adversarial patches can corrupt action predictions and thereby alter subsequent observations. To mitigate these threats, many existing defenses rely on policy adaptation or auxiliary models, but require additional training or inference. We introduce RECLAIM, a training-free, inference-time defense that uses a frozen VLA's own attention response to local visual interven...
  </details>

- **2026-11-17** — Peng Yu, Xiaoyu Wen, Zhida He et al. — [DACE: Diversity-Driven Adversarial Co-Evolution for Robust LLM Safety Alignment](http://arxiv.org/abs/2611.22278v1)
  <details><summary>📄 Abstract</summary>
  Ensuring robust safety alignment of large language models (LLMs) is increasingly difficult as adversarial attacks evolve and outpace alignment pipelines built on pre-collected data. Existing co-evolutionary frameworks let the defender chase a moving attacker, yet their training dynamics expose two compounding pathologies: \emph{attack strategy collapse}, where the attacker overfits to a narrow set of high-reward rewrites, and \emph{defense adversarial forgetting}, where the defender loses compet...
  </details>

- **2026-11-16** — Masanori Hanada — [Deep Learning for Physicists: From Linear Regression to Reasoning Models](http://arxiv.org/abs/2611.21295v1)
  <details><summary>📄 Abstract</summary>
  These lecture notes are based on an introductory course on neural networks and deep learning that the author taught in the School of Mathematical Sciences at Queen Mary University of London in 2023/24 and 2024/25. The author, however, is a physicist, and it shows: wherever possible, ideas are explained with physical intuition rather than heavy formalism. Readers with a background in physics or mathematics who want a self-contained, introductory route into modern machine learning may therefore fi...
  </details>

- **2026-11-16** — Xiaoqing Chen, Jiayi Ouyang, Dongrui Wu — [SmoothShift: Disrupting Visual Adversarial Attacks on LVLMs at Test Time](http://arxiv.org/abs/2611.20537v1)
  <details><summary>📄 Abstract</summary>
  Visual adversarial perturbations can substantially impair large vision-language models (LVLMs) despite introducing only subtle input changes. To understand how these small changes cause substantial errors, we investigate their optimization and propagation through the model, revealing two key findings. First, stronger attacks rely on finer iterative optimization, while subtle input perturbations induce representation discrepancies that are amplified layer by layer through the vision encoder and p...
  </details>


### 📂 privacy-leakage
*隐私泄露 / Privacy Leakage* — 30 papers

- **2026-11-18** — Luoyuan Zhang, Xuanyu Zheng, Yancheng Long et al. — [VideoACE: Benchmarking Agentic Video Understanding through High-Frame-Rate Actions](http://arxiv.org/abs/2611.24184v1)
  <details><summary>📄 Abstract</summary>
  Agentic video understanding requires models to actively interact with video environments to gather evidence and form judgments. Evaluating this capability therefore requires assessing whether models can translate opportunities for interaction into better understanding. We introduce VideoACE, a benchmark for assessing video understanding under conditions that support sustained interaction. We focus on high-frame-rate action videos, where rapid, subtle changes make targeted observation especially ...
  </details>

- **2026-11-18** — Jianshuo Liu, Kang G. Shin, Haining Wang — [Plug-and-Play Multi-Licensee Robust Watermarking for Mixture-of-Experts LLMs](http://arxiv.org/abs/2611.23838v1)
  <details><summary>📄 Abstract</summary>
  Mixture-of-Experts (MoE) architectures enable high-capacity large language models (LLMs) with high sparse computation, making them attractive for deployment on private hardware. However, distributing model weights exposes valuable intellectual property (IP) to leakage and unauthorized redistribution, creating an urgent need to both verify model ownership and trace leaked copies to individual licensees. Existing model-watermarking techniques are ill-suited for meeting this need because they are f...
  </details>

- **2026-11-18** — David Hong Liang Chew, Zexi Yao, Nataša Krčo et al. — [Localizing Text Anonymization for Trustworthy AI: Extending RAT-Bench to Malaysian Microdata and PII](http://arxiv.org/abs/2611.23704v1)
  <details><summary>📄 Abstract</summary>
  As governments and organizations adopt foundation models for public services and workplace productivity, sensitive citizen, employee, and administrative text may enter LLM workflows through inference, retrieval, fine-tuning, or local model development. We examine whether text anonymizers transfer to new deployment settings by extending RAT-Bench to Malaysia using local microdata, Malaysian PII formats, and culturally grounded transcripts in Malaysian English and Bahasa Malaysia. We evaluate NER-...
  </details>

- **2026-11-18** — Dongkeun Lee, Wonjun Lee — [MoMoVL: Modality-Aware Adaptive Compression for On-Device Sparsely-Activated Vision-Language Models](http://arxiv.org/abs/2611.23695v1)
  <details><summary>📄 Abstract</summary>
  The rise of the agentic web has been accompanied by growing demand for on-device Vision-Language Models (VLMs) that perform diverse cross-modal web tasks with enhanced privacy and reduced latency. Mixture-of-Experts (MoE) models are widely adopted in modern VLMs for compute-efficient scalability, yet their multi-expert architecture poses deployment challenges due to substantial memory demands. Mixed-precision quantization is an effective compression technique that reduces bit-widths while adapti...
  </details>

- **2026-11-18** — Zhi Li, Hanyu Wang, Fei Shen et al. — [AggCLIP: Aggregating CLIP for Zero-Shot Multimodal Anomaly Detection](http://arxiv.org/abs/2611.24643v1)
  <details><summary>📄 Abstract</summary>
  Zero-Shot Multimodal Anomaly Detection (ZSMAD) aims to identify both appearance and geometric defects in novel categories without relying on target-specific training data, making it especially valuable in real-world scenarios constrained by data scarcity, privacy concerns, or high annotation costs. While recent approaches successfully adapt vision-language models like CLIP to achieve this open-vocabulary generalization, they still face significant challenges: (i) severe geometric information los...
  </details>

- **2026-11-18** — Muhammad Rizky Wellyanto, Hajara-Yasmin Isa, Kexin Xue et al. — [Who are you? The Personal Imitation Game](http://arxiv.org/abs/2611.24888v1)
  <details><summary>📄 Abstract</summary>
  Large Language Models (LLMs) now perform strongly on Alan Turing's 1950 Imitation Game, so we propose a harder challenge, the Personal Imitation Game, which asks whether a machine can replicate a specific individual in conversation rather than a generic human. Testing with 30 participants, we establish a human baseline and report the identity signals interrogators rely on: stylometric features, personality traits, and biographical facts. To demonstrate the framework, we design an LLM-based syste...
  </details>

- **2026-11-18** — Prakhar Mishra, Bhavya Yajush Awasthi,  Tanuja et al. — [Self-Rewarded Reinforcement Learning for Better-Structured Medical Explanations in Small Language Models](http://arxiv.org/abs/2611.24650v1)
  <details><summary>📄 Abstract</summary>
  Small language models (SLMs) can run on commodity hardware and support privacy-preserving, on-premises clinical deployment, but their medical explanations are often short and poorly structured compared with large language models. Recent supervised approaches such as Meerkat transfer chain-of-thought reasoning into 7B-8B backbones, yet their training objective does not directly target the style or organization of the generated rationales. Building on the instruction-tuned Mistral-7B backbone, we ...
  </details>

- **2026-11-18** — Vishal Vivek Saley, Bhavesh Gurnani, Dinesh Raghu et al. — [ProbMedTOD: A Bayesian Network Guided Task-Oriented Dialogue System for Patient History Taking](http://arxiv.org/abs/2611.24535v1)
  <details><summary>📄 Abstract</summary>
  Patient history taking is a strategic, multi-turn process that refines diagnostic hypotheses through iterative questioning, mirroring clinical reasoning where each inquiry updates beliefs over candidate diagnoses. Deploying AI in this setting is constrained by privacy, cost, and latency, making Small Language Models (SLMs) a more desirable backbone compared to larger LLMs. However, SLMs capture only the fast, intuitive "System 1" side of this process and lack explicit mechanisms for the delibera...
  </details>

- **2026-11-18** — Zhiyang Qi, Michimasa Inaba — [CounselTraj: Synthesizing Process-Aware Psychological Counseling Dialogues via Dialogue-Act Trajectory Planning](http://arxiv.org/abs/2611.24168v1)
  <details><summary>📄 Abstract</summary>
  The growing demand for psychological counseling has motivated the development of LLM-based systems that support human counselors, but training such systems requires large-scale, high-quality dialogue data. Authentic counseling transcripts are difficult to collect and share because of privacy concerns, making synthetic dialogues an important alternative. However, existing synthetic datasets, despite covering diverse scenarios and client profiles, often consist of brief exchanges and fail to captu...
  </details>

- **2026-11-17** — Satiyabooshan Murugaboopathy, Entejar Alam, Adel Daoud et al. — [Agent Verifiers in Counterfactual Analysis: A Pilot Study Benchmarking Agentic Heterogeneous Treatment Effects](http://arxiv.org/abs/2611.23621v1)
  <details><summary>📄 Abstract</summary>
  Agents can expand the covariate space of randomized experiments by retrieving fast-moving local context missed by slow-changing survey baseline covariates, helping characterize who benefits most from an intervention. Verifying such covariates is difficult: individual treatment effects are unobserved, retrieval leakage can pull post-treatment information into nominally pretreatment summaries, and encoder leakage can inject post-treatment pretraining knowledge into representations even after tempo...
  </details>

- **2026-11-17** — Carla Teixeira Lopes, Daniel Félix — [LusoClin: A Synthetic Clinical Note Dataset for Medical Information Retrieval in European Portuguese](http://arxiv.org/abs/2611.23454v1)
  <details><summary>📄 Abstract</summary>
  Access to large-scale clinical text collections is crucial for advancing medical information retrieval research, including clinical note search, patient cohort identification, and domain-adapted retrieval models. However, real clinical notes are rarely available due to privacy regulations, which particularly limits progress for low-resource languages such as European Portuguese. We present LusoClin, a publicly released dataset of synthetic clinical notes in European Portuguese, created to suppor...
  </details>

- **2026-11-17** — Fernando Pinciroli — [Systematic Mapping Protocol. Generative AI-Augmented Requirements Engineering: A Systematic Mapping Study of Practices, Specifications, and Reuse in Software Development](http://arxiv.org/abs/2611.23349v1)
  <details><summary>📄 Abstract</summary>
  Generative artificial intelligence (GenAI), particularly large language models (LLMs), is rapidly being adopted in requirements engineering (RE). Existing secondary studies have characterized which RE activities are supported and which prompting strategies are used, but little is known about the specifications that GenAI-augmented RE produces and how they are used in subsequent activities such as specification-driven development (SDD), design and code generation, test derivation, verification, a...
  </details>

- **2026-11-17** — Lin Li, Xinbo Ban, Chao Chen et al. — [From Ideal to Real: Integrating Language Models into Smart Home for Human-Centric IoT Safety and Security Fuzzing](http://arxiv.org/abs/2611.22457v1)
  <details><summary>📄 Abstract</summary>
  Integrating IoT devices into household systems offers enhanced control over living environments. However, as these devices become pervasive in critical sectors such as healthcare, transportation, and home automation, they expose inter-rule vulnerabilities that may lead to privacy breaches, data theft, and physical harm. Traditional fuzz testing methods, which often operate in simulated environments assuming ideal human decisions, fail to account for the complexities of human interactions that ca...
  </details>

- **2026-11-17** — Qitong Wang, Jihui Jin, Divya Kothandaraman et al. — [Transfer Once, Ask Locally: Compact Audio-Visual Memory for On-Device Question Answering](http://arxiv.org/abs/2611.23085v1)
  <details><summary>📄 Abstract</summary>
  Audio-visual question answering on lightweight user devices requires balancing speed, memory usage, privacy, and communication. One approach is to run audio-visual encoders on a server and a lightweight language decoder on the user device, keeping questions local while offloading media encoding. However, transferring and processing the full multimodal representation remains costly. We propose a training-free, query-agnostic token pruning framework that constructs a compact, reusable memory befor...
  </details>

- **2026-11-17** — Steven Yu Tung, Shubham Vaijanath Phoolari, Christoph Lauer et al. — [CaFe: Causally Faithful Conditional Traffic Scenario Generation](http://arxiv.org/abs/2611.22855v1)
  <details><summary>📄 Abstract</summary>
  Language-conditioned traffic simulation enables scalable test scenarios steered by natural language. The goal is to control selected agents while surrounding traffic reacts to their observed behaviour. For example, a vehicle instructed to cut in late should cause the following vehicle to brake only when the manoeuvre becomes observable. Yet simulators can leak private instructions across agents, causing surrounding vehicles to react before the instructed behaviour becomes observable. Such premat...
  </details>

- **2026-11-17** — Bernard Tomczyk, Gail Collyer-Hoar, Bryan Williams — [Keeping Parts Honest: Isolated Part Graphs for Faithful Vision Transformer Explanations](http://arxiv.org/abs/2611.22853v1)
  <details><summary>📄 Abstract</summary>
  Part and prototype-based explanations for Vision Transformers (ViTs) present a decision as evidence from individual image regions. However, self-attention mixes information across patches, so part-level features absorb context from the whole image and consequently fail to faithfully reflect the decision. We show that existing interpretable ViT classifiers depend heavily on this leakage: when each explained region is encoded in isolation, their accuracy collapses, and retraining them under isolat...
  </details>

- **2026-11-17** — Linshan Yan — [Where Demand Meets Supply: Spatial Elastic Consensus for Low-Bandwidth Collaborative Perception](http://arxiv.org/abs/2611.22439v1)
  <details><summary>📄 Abstract</summary>
  Occlusions and limited sensor range make ego-only 3D perception insufficient for safe driving. Collaborative perception addresses this by enabling connected vehicles to share complementary observations, yet it remains constrained by tight vehicular communication budgets. While spatial selection is more flexible than fixed-rate feature compression, existing selectors remain largely sender-driven and waste scarce bandwidth on ego-visible targets. Furthermore, applying convolutions after masking sp...
  </details>

- **2026-11-17** — Anastasia Volkova, Andrey Kuznetsov, Ivan Oseledets et al. — [TabDAG: Structured Evolutionary Search for Tabular Feature Engineering](http://arxiv.org/abs/2611.22828v1)
  <details><summary>📄 Abstract</summary>
  Feature engineering can improve tabular prediction, but useful transformations are compositional, data-dependent, and subject to leakage constraints. We present TabDAG, a framework that combines evolutionary search with a graph representation of feature-engineering programs. Nodes implement row-wise or data-fitted transformations; edges encode dependencies among raw variables, intermediate values, and final features. The representation supports interactions, statistical encodings, clustering- an...
  </details>

- **2026-11-17** — Yifan Xu, Ruopeng Gao, Zhixiao Wang et al. — [Teaching What to Look For: Privileged Perception Questions for Agentic On-Policy Distillation in Video Captioning](http://arxiv.org/abs/2611.22755v1)
  <details><summary>📄 Abstract</summary>
  Detailed video captioning requires comprehensive and faithful descriptions of objects, actions, and temporal events. Fixed-frame sampling, however, can miss brief motions, small objects, and other fine-grained evidence, motivating captioning agents that actively seek relevant moments and inspect local regions. Training such behavior is challenging because, unlike video question answering, generic captioning instructions do not specify what visual evidence should be acquired. We propose Perceptio...
  </details>

- **2026-11-17** — Caoxin Wang, Shengkai Gan, Xiang Hu et al. — [The Between-Round Decision in Autonomous Research: An LLM Controller That Reads the Whole Trajectory](http://arxiv.org/abs/2611.22661v1)
  <details><summary>📄 Abstract</summary>
  Executing an idea often changes how promising it looks, so the next step in autonomous research should rest on results, not on proposals. After each round of experiments, the system must decide whether to refine the best solution or start a new direction, which solution to build from, and what goal to set. We call this the between-round decision. Existing systems wrap it in machinery such as rules, scores, search trees, and schedules; where an LLM makes it, what the LLM needs to read is left ope...
  </details>

- **2026-11-17** — Enshuo Hsu, Linh Nguyen, Sunyang Fu et al. — [A Visual Information Extraction System Using Multimodal Large Language Models for Scanned Cognitive and Behavioral Assessments](http://arxiv.org/abs/2611.22252v1)
  <details><summary>📄 Abstract</summary>
  Objective. Paper-based assessments are common in patient care, but handwriting and scanning artifacts make these forms difficult to process at scale. This study proposes a modular, multimodal LLM-based system with human oversight for extracting fields and scores. We conducted a qualitative analysis of the use of LLMs for hand-drawing analysis.   Materials and Methods. The system processes cognitive assessments (i.e., MMSE, MoCA, Mini-Cog) and the NICHQ Vanderbilt Assessment using two modules: 1)...
  </details>

- **2026-11-17** — Meilu Zhu, Xiaohan Li, Axiu Mao — [Where Does Hindsight Enter Clinical Agent Benchmarks? An Audit of Simulators and Case Construction](http://arxiv.org/abs/2611.22241v1)
  <details><summary>📄 Abstract</summary>
  Benchmarks for LLM diagnostic agents are built from retrospective records: the case an agent reads is rewritten from discharge summaries, and unrecorded test results are generated by a simulator that often sees the final diagnosis. HindAudit separates three hindsight channels (the diagnosis given to the simulator, the retrospective context it conditions on, and the agent-facing case text) and measures each with judges trained only on real data. On 27,489 emergency admissions from MIMIC-IV, five ...
  </details>

- **2026-11-16** — Bojing Feng, Jinqiu Deng, Zihan Hong et al. — [Regularizing Treatment Leakage for LLM-based Uplift Estimation](http://arxiv.org/abs/2611.20794v3)
  <details><summary>📄 Abstract</summary>
  Large language models (LLMs) provide semantic features for uplift estimation, but treatment-revealing text can induce prediction shortcuts that do not transfer to deployment. We propose LLM-based Uplift Leakage Regularization (LULR) to address this risk. With the LLM encoder frozen, LULR penalizes dependence between the causal head's trainable shared representation and treatment while retaining separate outcome heads. The penalty uses a variational approximation to the contrastive log-ratio uppe...
  </details>

- **2026-11-16** — Nikhil J. Dhinagar, Rishab Pendam, Harmony S. Cen et al. — [SCAN: Site-Aware Collaborative Privacy-Preserving Adaptation of Vision-Language Models for Neurological Disease Classification](http://arxiv.org/abs/2611.21955v1)
  <details><summary>📄 Abstract</summary>
  Worldwide neuroimaging data could strengthen diagnostic foundation models, but privacy rules often prevent centralizing brain MRI scans. We present SCAN, a site-aware collaborative adaptation framework for Neurological Disease Classification that lets new sites adapt a 3D medical vision-language model (VLM) without retraining or sharing patient scans. Each site keeps exact class prototypes for local prediction and can share privacy-protected class summaries: norm-bounded sums and counts perturbe...
  </details>

- **2026-11-16** — Bojing Feng, Jinqiu Deng, Zihan Hong et al. — [Regularizing Treatment Leakage for LLM-based Uplift Estimation](http://arxiv.org/abs/2611.20794v2)
  <details><summary>📄 Abstract</summary>
  Large language models (LLMs) provide semantic features for uplift estimation, but treatment-revealing text can induce prediction shortcuts that do not transfer to deployment. We propose \emph{LLM-based Uplift Leakage Regularization} (\textsc{LULR}) to address this risk. With the LLM encoder frozen, \textsc{LULR} penalizes dependence between the causal head's trainable shared representation and treatment while retaining separate outcome heads. The penalty uses a variational approximation to the c...
  </details>

- **2026-11-16** — Ilia Kopanichuk, Daniil Kartashev, Yuri Bolkonsky et al. — [Call-Efficient ICD-10 Code Prediction via Supervised Candidate Generation and Selective LLM Invocation](http://arxiv.org/abs/2611.21891v1)
  <details><summary>📄 Abstract</summary>
  Automatic assignment of ICD-10 codes from short clinical diagnosis text is a practical medical text classification and normalization task. The task is difficult because diagnosis phrases are short and noisy, the ICD-10 label space is hierarchical, and the class distribution is strongly imbalanced. This paper presents a call-efficient ICD-10 code prediction pipeline that combines transformer embeddings, tree-based supervised candidate generation, candidate-level reranking, and a gated LLM assista...
  </details>

- **2026-11-16** — Tsai-Min Chen, Jun Seita — [TIBECG: Temporal Information Bottleneck for Lead-Specific Demographic Privacy in ECG Waveform Release](http://arxiv.org/abs/2611.21694v1)
  <details><summary>📄 Abstract</summary>
  Transmitting an electrocardiogram (ECG) waveform can expose demographic information beyond an intended diagnostic task. We evaluate TIBECG, an architectural temporal information bottleneck, on individual leads extracted from hospital twelve-lead recordings. A 2,302,337-parameter processor varies its latent length while retaining the same nine-score consistency objective, without age or sex labels in protector fitting. Across 6,386 recordings, ten folds, 12 leads and 21 lengths, retrospective sel...
  </details>

- **2026-11-16** — Guangzhi Sun, Xiao Zhan, Shuai Wang et al. — [AudioTrace: File-Level Membership Detection for Audio Large Language Models](http://arxiv.org/abs/2611.21088v1)
  <details><summary>📄 Abstract</summary>
  Significant privacy and copyright concerns are raised by the use of publicly available audio recordings to train audio large language models (LLMs), yet effective auditing methods remain limited. Existing membership inference attacks typically assume knowledge of complete training examples, including their associated textual supervision. In practice, however, audio recordings may be paired with privately generated transcripts, captions, or question-answer pairs that are unavailable to owners of ...
  </details>

- **2026-11-16** — Chang Xu, Hao Wang, Gedi Zhou et al. — [Where the Evidence Lives: Measuring Privacy and Diagnosability of Exported AI-Agent Traces](http://arxiv.org/abs/2611.20389v1)
  <details><summary>📄 Abstract</summary>
  Execution traces help diagnose AI-agent failures, but sharing them can expose customer identities. For example, detecting that an agent handled the wrong customer's records requires knowing whether the records belong to the requested customer, but not necessarily knowing who that customer is. Our executable benchmark measures what a trace export reveals and whether a proposed repair restores the correct output in synthetic multi-tenant workflows. Conventional redaction can remove evidence needed...
  </details>

- **2026-11-16** — Bojing Feng, Jinqiu Deng, Zihan Hong et al. — [Regularizing Treatment Leakage for LLM-based Uplift Estimation](http://arxiv.org/abs/2611.20794v1)
  <details><summary>📄 Abstract</summary>
  Uplift modeling estimates the conditional average treatment effect (CATE) and supports industrial decisions such as promotional pricing. When large language models (LLMs) encode product text, treatment-revealing content can introduce shortcuts that do not transfer to deployment. We propose \emph{LLM-based Uplift Leakage Regularization} (\textsc{LULR}), which uses a CLUB-based penalty on the causal head's trainable shared representation while keeping the LLM encoder frozen. Controlled proxy exper...
  </details>


### 📂 misuse
*滥用与误用 / Misuse & Abuse* — 15 papers

- **2026-11-18** — Sean Lim, Clement Neo — [Probing agent overeagerness in realistic settings with continuation audits](http://arxiv.org/abs/2611.24491v1)
  <details><summary>📄 Abstract</summary>
  Frontier coding agents increasingly exhibit overeagerness, taking surprising, sometimes reckless actions beyond a user's mandate --- reported in recent system cards from frontier model developers. These cases are surfaced through internal deployment monitoring, which requires private traffic and is out of reach for open-weight models and independent evaluators. Automated alignment audits are the natural alternative, but capable models increasingly recognise the synthetic setup and adjust their b...
  </details>

- **2026-11-18** — Muhammad Mahir Malik, Muhammad Moiz Khalid, Hussain Ahmad et al. — [JEV vs. LLMs: A Comparative Analysis for Phishing Email Detection](http://arxiv.org/abs/2611.23683v1)
  <details><summary>📄 Abstract</summary>
  Phishing remains a major source of credential theft and fraudulent payments, and email security systems must classify large message volumes reliably, quickly, and at manageable cost. Large Language Models (LLMs) offer flexible text understanding, but their token-based generation increases response time and API cost, and the reliability of their confidence values requires measurement. Jev 1.13, a typed decision model from TypeSafe AI, instead returns a structured outcome with a confidence value. ...
  </details>

- **2026-11-18** — Yipeng Wang, Huy Gia Han Vu, Jiaming Liu et al. — ["I Don't Think It's a Scam": A First Look at Family Intervention Barriers in Elder Abuse Discussions on Reddit and Baidu Tieba](http://arxiv.org/abs/2611.24899v1)
  <details><summary>📄 Abstract</summary>
  When older adults trust scammers despite warnings, families face obstacles to intervention. Complainants aged 60 and older reported \$4.9 billion in losses in 2024 to the U.S. Internet Crime Complaint Center. To investigate family intervention barriers to elder scams, we collected 2M Reddit posts from May 2021 to June 2026 and 2B Baidu Tieba posts from 2007 to 2026. The final corpora contain 13,082 Reddit posts and 3,933 Baidu Tieba posts, labeled using platform-specific codebooks, manual refere...
  </details>

- **2026-11-18** — Mark Marosi, Peter Antal — [General progress substitutes for specific training data in language models](http://arxiv.org/abs/2611.24844v1)
  <details><summary>📄 Abstract</summary>
  Language models acquire their capabilities from training data, and developers withhold data during training to keep models from learning capabilities that could be misused. How long this delays a capability, and how much data is needed to acquire it later, is unknown. Here we show that the general progress a model makes on the rest of its training data substitutes for the data that was withheld. We withheld the training signal for individual skills in models of chess, Othello, molecular strings,...
  </details>

- **2026-11-18** — Andrei Kostin, José Ángel Diaz-Garcia, Karel Gutiérrez-Batista — [A Hybrid RAG Framework for Deceptive Review Detection: Integrating RoBERTa-LoRA, FAISS-Based Retrieval, and LLM Reasoning](http://arxiv.org/abs/2611.24049v1)
  <details><summary>📄 Abstract</summary>
  The growth of deceptive online opinions poses a critical risk of misinformation and fraud. This paper proposes a Retrieval-Augmented Generation (RAG) system to automatically distinguish spam reviews. The architecture integrates RoBERTa with Low-Rank Adaptation (LoRA) classification, FAISS semantic vector retrieval, and a Large Language Model (LLM) for final reasoning. The system was evaluated across balanced and severely imbalanced real-world scenarios. Results demonstrate that five epochs of fi...
  </details>

- **2026-11-17** — Tongxi Wu, Yuyang Cheng, Jiacheng Xian et al. — [Reading Scene States: Uncovering Safety Failures in Vision-Language Models](http://arxiv.org/abs/2611.23206v1)
  <details><summary>📄 Abstract</summary>
  Vision-language models (VLMs) can provide harmful assistance by interpreting visual events, even without an explicit request for the underlying harmful objective. We identify this \textbf{scene-state safety vulnerability} and introduce \textbf{SceneSafetyBench}, comprising 375 image--question pairs spanning Initial, Medium, and Ultimate scene states and five visual presentations. Across eight VLMs, scene-state inputs elicit harmful assistance with attack success rates (ASRs) of 45.6--72.3\%. Com...
  </details>

- **2026-11-17** — Runqi Lin, Suqin Yuan, Zihao Fu et al. — [Beyond Attribute-Centric Fairness: Modelling and Mitigating Unified Bias Representation in Omni-modal Large Language Models](http://arxiv.org/abs/2611.22889v1)
  <details><summary>📄 Abstract</summary>
  Omni-modal large language models (OLLMs) provide joint multimodal understanding and generation capabilities, making them well-suited to complex environments and promising backbones for next-generation AI. Despite these advances, the harmful stereotypes encoded in such models manifest in increasingly diverse forms, leading to broader and more severe societal consequences. Existing debiasing methods typically impose separate fairness objectives for each sensitive attribute and modality to minimise...
  </details>

- **2026-11-17** — Yuxuan Zhou, Chen Xiong, Haitong Liu et al. — [SEAM: Computer-Use Agents Know the Harm Between Screens, and Commit It Anyway](http://arxiv.org/abs/2611.22971v1)
  <details><summary>📄 Abstract</summary>
  Safety benchmarks for computer-use agents (CUAs) place the harm either in the intent of the task or on a single screen: a malicious instruction, an injected command, a phishing page. An agent that checks the task and each screen in isolation can pass them, so they do not test whether it combines facts seen on different screens. Yet in delegated work, harm often arises exactly this way: a fact about a person on one screen, a fact about an item on another, and a legitimate task that binds them. We...
  </details>

- **2026-11-17** — Rose N. Kwon, Samy Mammeri, Sabyasachi Sahoo et al. — [Hidden-State Similarity Predicts Re-Elicitation After Inoculation Prompting](http://arxiv.org/abs/2611.23096v1)
  <details><summary>📄 Abstract</summary>
  Fine-tuning on narrow harmful tasks can cause emergent misalignment, where models generalize harmful behavior beyond the training distribution. Inoculation prompting can reduce this effect by explicitly eliciting the undesired behavior during training, but recent work shows that the behavior can reappear when evaluation prompts contain cues from the training context. We study what makes such prompts effective triggers. We find that, surprisingly, textual similarity to the inoculation prompt is a...
  </details>

- **2026-11-17** — Yuanhao Zeng, Shaocheng Lan, Ao Lu et al. — [The Resolution Hypothesis: Agent Evolution's Key Is Identifying Improvements](http://arxiv.org/abs/2611.23068v1)
  <details><summary>📄 Abstract</summary>
  Agent evolution follows a simple loop: a proposer writes candidate artifacts (prompts, skills, memories) and selection accepts those that score higher. This loop has shown promise, yet practitioners face a puzzle: methods trade wins across papers, and evolution often fails to bootstrap on certain tasks. We trace this puzzle to the Resolution Hypothesis: agent evolution stalls not because methods fail to propose better artifacts, but because noisy evaluations cannot reliably identify them. Across...
  </details>

- **2026-11-17** — Albert Ansah Benson, Mingqiang Han, Rahul Harsha Cheppally et al. — [Data-Efficient Algal Bloom Segmentation in Freshwater Bodies Using a Three-Stage Transfer Learning Pipeline with Attention-Enhanced Decoding](http://arxiv.org/abs/2611.22064v1)
  <details><summary>📄 Abstract</summary>
  Harmful algal blooms threaten water quality and public health, yet automated segmentation of bloom regions in freshwater imagery is limited by scarce pixel-level annotations. We present a transfer-learning pipeline that adapts a Swin Transformer U-Net with SCSE decoder attention from ImageNet-1K to water-body segmentation (RIWA, LaRS) and then to algal blooms, together with a model-assisted annotation protocol that expands the labelled algae corpus from 145 to 655 images. In a single-seed ablati...
  </details>

- **2026-11-16** — Grace Ibukunoluwa Ufeoshi, Alessandro Di Stefano, Ndidi Bianca Ogbo et al. — [From Apology to Action: Apologies, Compensation, and Cooperation in LLM Agents](http://arxiv.org/abs/2611.21984v1)
  <details><summary>📄 Abstract</summary>
  Large language models (LLMs) can make decisions that affect other agents, but what happens after a harmful or unsuccessful interaction remains poorly understood. We investigate whether apologies by LLM agents are associated with subsequent cooperative behaviour, using controlled Prisoner's Dilemma experiments with four commercial models (Claude Opus 4.8, GPT-5.5, Gemini 3.1 Pro, and Mistral Large 3). Across payoff conditions, we examine when agents apologise, the reasons they provide, and the ac...
  </details>

- **2026-11-16** — Minsuk Jang, Minseok Son, KiHyun Seol et al. — [CuRSE-Bench: A Benchmark for Probing Cultural Blind Spots in Text-to-Image Safety Evaluation](http://arxiv.org/abs/2611.20821v2)
  <details><summary>📄 Abstract</summary>
  Text-to-image (T2I) safety evaluation typically assigns each prompt or image a single culture-blind harm label, so content that is harmful only within a particular culture can pass as benign. We introduce CultureCraft, an agentic framework that constructs T2I prompts that appear benign under a general-purpose rubric yet carry a latent harmful meaning in a target culture, and use it to build CuRSE-Bench: 10,709 culture-specific prompts and 2,648 culture-general controls over six regions and ten h...
  </details>

- **2026-11-16** — Quoc Nguyen, Trung Le, Dinh Phung et al. — [Model Immunization Beyond Condition Numbers: The Importance of Plateau Regions](http://arxiv.org/abs/2611.20472v1)
  <details><summary>📄 Abstract</summary>
  Harmful fine-tuning can rapidly compromise safety alignment in Large Language Models, underscoring the vulnerability of deployed models to post-release modification. While prior work motivates model immunization by inducing ill-conditioned curvature to slow harmful optimization, this approach is not scalable due to the high computational cost of Hessian estimation. We refine this paradigm by extending the theoretical framework to prioritize plateau regions alongside curvature. We further introdu...
  </details>

- **2026-11-16** — Minsuk Jang, Minseok Son, KiHyun Seol et al. — [CuRSE-Bench: A Benchmark for Probing Cultural Blind Spots in Text-to-Image Safety Evaluation](http://arxiv.org/abs/2611.20821v1)
  <details><summary>📄 Abstract</summary>
  Text-to-image (T2I) safety evaluation typically assigns each prompt or image a single culture-blind harm label, so content that is harmful only within a particular culture can pass as benign.   We introduce CultureCraft, an agentic framework that constructs T2I prompts that appear benign under a general-purpose rubric yet carry a latent harmful meaning in a target culture, and use it to build CuRSE-Bench: 10,709 culture-specific prompts and 2,648 culture-general controls over six regions and ten...
  </details>


### 📂 red-teaming
*红队测试 / Red Teaming* — 3 papers

- **2026-11-18** — Xiaoyang Xing, Wenyu Dai, Xiaoliang Gong et al. — [Learning to Coordinate: LLM-Guided Workflow Evolution for Token-Efficient Red Teaming](http://arxiv.org/abs/2611.24221v1)
  <details><summary>📄 Abstract</summary>
  Automated red teaming is essential for identifying safety failures in large language models (LLMs), but its practical scalability depends on the resources required to discover those failures. Multi-agent systems can combine complementary capabilities, yet repeated planning, redundant exchanges, and ineffective information routing can make their coordination expensive. Moreover, a target model's response indicates the outcome of a test without identifying which collaboration decision should chang...
  </details>

- **2026-11-18** — Onkar Shelar, Travis Desell — [Incremental Speciation in Evolutionary Red Teaming of Large Language Models](http://arxiv.org/abs/2611.23949v1)
  <details><summary>📄 Abstract</summary>
  Speciation maintains distinct subpopulations in evolutionary search through similarity-based grouping and species-aware parent selection. For text-based individuals, niches depend on both the compatibility representation and the assignment operator that turns pairwise relations into species. We examine this design space in black-box evolutionary red teaming of large language models, comparing embedding and natural language inference (NLI) dissimilarities under representative-based and density-ba...
  </details>

- **2026-11-16** — Keshav Shenoy, Anthony Zang, Eric Gan et al. — [Auditors Struggle to Catch Sabotage In End-to-End Transcripts of AI Safety Research](http://arxiv.org/abs/2611.21832v1)
  <details><summary>📄 Abstract</summary>
  As AI systems are increasingly used to automate AI R&D, misaligned systems could sabotage research intended to improve model safety and alignment. To stress-test defenses against such sabotage, we use a human expert as a proxy saboteur on AI safety research. We conduct a red-team/blue-team game where a human researcher runs AI safety experiments from scratch and auditors try to tell which were sabotaged and how. Given access to the full research transcript and the ability to run experiments, hum...
  </details>


### 📂 vulnerability
*漏洞与攻击面 / Vulnerabilities & Attack Surfaces* — 62 papers

- **2026-11-18** — Cameron Mehlman, Arjun Mulchandani, Hovik Grigoryan et al. — [Communications-free Collective Intelligence Via Allocentric Belief](http://arxiv.org/abs/2611.24858v1)
  <details><summary>📄 Abstract</summary>
  A team of skilled card players share no information amongst each other, and yet still are able to coordinate their play by watching the same players and reading the same tells. Autonomous systems have failed to exploit this logic, relying instead on explicit communication or complex state estimation schemes that can fail when it matters most. Without it, decentralized agents diverge in their world beliefs, and coordination collapses. Here we show that anchoring all agents to a single shared exte...
  </details>

- **2026-11-18** — Tushin Mallick, Evan Rose, Matthew Laws et al. — [Kaer: Security-Aware Replanning for Multi-Agent Systems](http://arxiv.org/abs/2611.24839v1)
  <details><summary>📄 Abstract</summary>
  One popular architecture for multi-agent systems (MAS) relies on an orchestrator that generates an initial plan, coordinates its execution, and dynamically revises the plan based on agent feedback when tasks cannot be fully specified in advance. This dynamic replanning introduces a critical vulnerability: malicious agents can embed instructions within their feedback to hijack the replanning process. Existing defenses focus exclusively on per-tool access control or static, pre-execution policy en...
  </details>

- **2026-11-18** — Jie Peng, Yongxue Shan, Yongfu Zha et al. — [NaviGATE: Noise-Aware Dual-View Generation for Multimodal Knowledge Graph Reasoning](http://arxiv.org/abs/2611.24552v1)
  <details><summary>📄 Abstract</summary>
  Multimodal knowledge graph reasoning (MKGR) aims to infer missing facts by jointly exploiting relational structures, textual descriptions, and visual evidence. Existing embedding-based methods effectively capture graph topology, but their fixed multimodal representations are less effective for query-specific fine-grained semantic reasoning, while generation-based methods are vulnerable to noisy retrieval and may produce invalid entities. To address these challenges, we propose NaviGATE, a noise-...
  </details>

- **2026-11-18** — Yun Bian, Shihao Li, Haiquan Wang et al. — [Mitigating fix reversal: Counterfactual constraints for function-level vulnerability detection](http://arxiv.org/abs/2611.24489v1)
  <details><summary>📄 Abstract</summary>
  Function-level vulnerability detectors often exhibit fix reversal, assigning a higher vulnerability probability to a fixed version than to its vulnerable counterpart. Fixes usually lengthen functions, and larger length increases are associated with more severe reversal. Code-transformation experiments indicate that fix reversal mainly stems from a length shortcut: vulnerability probability increases with function length when content is fixed. We propose CFVul to address this problem. Sliding-win...
  </details>

- **2026-11-18** — Mingyang Lyu, Yinqian Sun, Gongce Cao et al. — [Homeward: No Place Like the Training View](http://arxiv.org/abs/2611.24455v1)
  <details><summary>📄 Abstract</summary>
  Vision-language-action (VLA) policies implicitly assume that third-person cameras remain fixed at their data-collection poses; once a camera is bumped, remounted, or swapped at deployment, task success degrades precipitously even though the underlying task and robot remain unchanged. We present Homeward, a training-free, plug-and-play observation adapter that canonicalizes observations from an uncalibrated deployment camera back into the training view for frozen VLA policies. Our design stems fr...
  </details>

- **2026-11-18** — Chengzhi Yi, Xiao Cheng, Wei Song et al. — [When Shuffling Fails: Token Recovery from Obfuscated KV Caches](http://arxiv.org/abs/2611.24276v1)
  <details><summary>📄 Abstract</summary>
  LLM serving systems store, offload, and share KV caches, exposing token-level representations to infrastructure operators and co-tenants. Shuffled obfuscation combines secret linear transforms with fresh permutations, claiming security from b! possible shufflings. We show that input symmetry invalidates this counting argument: security depends on distinguishable outputs under chosen inputs. Repeated tokens produce identical first-layer Value rows, making every row permutation leave the data unch...
  </details>

- **2026-11-18** — Robin Geens, Simon Haepers, Jonas Crols et al. — [Hardware Acceleration of Vision-Language-Action Models with Weight Precision Rising over the Flow Steps](http://arxiv.org/abs/2611.24234v1)
  <details><summary>📄 Abstract</summary>
  Vision-language-action (VLA) models such as GR00T control robots through an action head: a diffusion transformer that turns noise into a chunk of actions in a few flow-matching steps. Every step re-reads all of the head's weights from DRAM but applies each weight to only about fifty tokens. Inference is therefore memory-bound, and its latency and energy are largely determined by the total number of transferred weight bits. We show that later flow steps attenuate the quantization errors of earlie...
  </details>

- **2026-11-18** — Chihcheng Hsieh, Yang Song, Flora Salim et al. — [SpiderMark: Hybrid Watermarking for Generative AI via Algorithmic Injection and Learning-Based Verification](http://arxiv.org/abs/2611.24200v1)
  <details><summary>📄 Abstract</summary>
  The proliferation of diffusion-based generative models has intensified the need for reliable methods to trace and verify the provenance of AI-generated images. Existing watermarking approaches for diffusion models typically rely on isotropic frequency patterns and handcrafted detection metrics, which are prone to directional vulnerability and threshold instability across diverse image transformations. We propose SpiderMark, a hybrid watermarking framework that combines algorithmic frequency-doma...
  </details>

- **2026-11-18** — YaoYang Liu, Jun Dai, ZhuoShi Tang et al. — [From Neural Tokens to Language: Dual-View EEG Semantic Bridging for Brain-to-Text Generation](http://arxiv.org/abs/2611.24197v1)
  <details><summary>📄 Abstract</summary>
  Visually evoked EEG-to-text generation aims to produce natural-language descriptions from neural responses elicited by visual stimuli. Existing approaches typically compress EEG signals into a single global representation and directly project it into the hidden space of a large language model (LLM), which may limit the preservation of complementary visual semantics under noisy and subject-dependent EEG signals. We propose a dual-view semantic token bridging framework that exploits raw images and...
  </details>

- **2026-11-18** — Linfeng Tang, Zhijun Fan, Yang Chen et al. — [GenRF: Generative Registration-free Image Fusion](http://arxiv.org/abs/2611.24157v1)
  <details><summary>📄 Abstract</summary>
  Multi-modal image fusion combines complementary observations to improve scene visibility and perception. However, in real-world acquisition, differences in sensing principles and configurations introduce geometric discrepancies, while degradations further compromise source quality. Existing methods typically rely on explicit registration, yet large parallax complicates correspondence estimation, while mismatched fields of view leave some regions without cross-modal counterparts. Meanwhile, indep...
  </details>

- **2026-11-18** — Xiaobao Wei, Jingxian Wu, Lirong Yang et al. — [CausalDrive: Causal Decomposition for Data-Efficient End-to-End Autonomous Driving](http://arxiv.org/abs/2611.24080v1)
  <details><summary>📄 Abstract</summary>
  Efficient use of expert demonstrations is essential for end-to-end autonomous driving. However, directly imitating expert trajectories couples nominal intention, which specifies where the vehicle should go, with multimodal driving styles, which determine how that intention is executed. Different combinations of these factors can yield similar expert trajectories, obscuring their respective causal contributions and forcing the policy to learn both from a single entangled target. This ambiguity li...
  </details>

- **2026-11-18** — Langtian Qin, Avishkar Dnyaneshwar Kawadgave, Ian Andrew Harshbarger et al. — [OMNIS+: Semantic RAN Slicing and Quantization for Dynamic Split Neural Networks](http://arxiv.org/abs/2611.23977v1)
  <details><summary>📄 Abstract</summary>
  Edge computing enables resource-constrained devices to execute machine learning (ML) applications via task offloading, with radio access network (RAN) slicing playing a crucial role in provisioning joint communication and computing resources. However, existing RAN slicing frameworks rely on static computing models, limiting their ability to exploit dynamic semantic data representations enabled by modern neural architectures. To address this limitation, we propose OMNIS+, a semantic RAN slicing f...
  </details>

- **2026-11-18** — Hassan Safouhi — [The $S$ and Double-Exponential Transformations with a Moment Expansion for Three-Centre Coulomb and Hybrid Integrals](http://arxiv.org/abs/2611.23965v1)
  <details><summary>📄 Abstract</summary>
  Three-centre two-electron Coulomb and hybrid integrals over exponential-type functions involve semi-infinite radial integrals containing oscillatory spherical Bessel functions. We investigate the combination of the $S$ transformation with Fourier-type double-exponential (DE) quadrature for their accurate and efficient numerical evaluation. The $S$ transformation transfers derivatives from the spherical-Bessel factor to the radial amplitude, converting the integral into a sine representation part...
  </details>

- **2026-11-18** — Yilin Wang, Xiangxi Zheng, Dongxing Mao et al. — [SimplePro: A Simple Baseline for Proactive Video Understanding](http://arxiv.org/abs/2611.23954v1)
  <details><summary>📄 Abstract</summary>
  Proactive video understanding requires vision-language models (VLMs) to decide not only what to answer as a video unfolds, but also when newly arrived evidence warrants a response and when to remain silent. Although modern VLMs excel at offline long-video understanding, they struggle in proactive streaming settings, leading prior work to introduce task-specific reinforcement learning or auxiliary triggering modules. We find that explicit reporting rules and structured streaming context substanti...
  </details>

- **2026-11-18** — Vedaang Verma, Dennies K. Bor, Lucy Wilkerson et al. — [A State-Level Assessment of Space Weather Impact on the Virginia Power Grid: From Vulnerability to Mitigation Strategies](http://arxiv.org/abs/2611.23791v1)
  <details><summary>📄 Abstract</summary>
  Contemporary methodologies exist for assessing the nationwide impacts of geomagnetically induced currents (GICs), such as the Coupled Space Weather Impact Model (C-SWIM), which links power grid vulnerability with economic losses. Yet regional mitigation requires adapting the national model to the local transmission network so operators and planners can identify substations at risk and evaluate economic and population consequences and protective actions. We present the first adaptation of C-SWIM ...
  </details>

- **2026-11-18** — Ryoichi Kurihara, Kota Sunamoto — [Meaning Reaches Object Choice but Not Completion: Where Is a VLA Vulnerable to Landmark Synonyms?](http://arxiv.org/abs/2611.24076v1)
  <details><summary>📄 Abstract</summary>
  VLA policies are fragile to rewording. Success rates alone cannot say whether a policy fails to choose the object or to complete the task, nor where in the policy to intervene. We study the released GR00T N1.7 on two LIBERO-Spatial tasks differing only in the landmark word telling which of two bowls to take. Synonyms absent from the training instructions send the policy to the bowl they name, unlike made-up words, yet complete 67.6% of one task's closed-loop episodes, against the original word's...
  </details>

- **2026-11-17** — Malak Gamal El-Din, Yasser Shoukry, Salma Elmalaki — [BeFit: Shifting Complexity from Weights to Bernstein Activations for Resource-Constrained Sensing](http://arxiv.org/abs/2611.23520v1)
  <details><summary>📄 Abstract</summary>
  Time-series sensing increasingly relies on neural networks, yet deployment on resource-constrained microcontrollers remains challenging. Aggressive model compression can reduce accuracy, while restricting weights to multiplication-free representations introduces further losses. We present BeFit, an end-to-end framework that shifts model capacity from weights to learnable Bernstein polynomial activations. BeFit (i) finds compact Bernstein-activated convolutional neural networks (BeCNNs) through h...
  </details>

- **2026-11-17** — Monika Santra, Dhilung Kirat, Qiushi Wu et al. — [ACaM: Automated Capability Modeling for Agentic AI Security](http://arxiv.org/abs/2611.23507v1)
  <details><summary>📄 Abstract</summary>
  In agentic AI systems, an LLM invokes tools that hold standing access to credentials, private data, filesystems, and external services. Such agents are increasingly deployed without an answer to a basic question: what can an agent access, exfiltrate, and propagate, independent of what it is designed for or is observed to do? The question goes unanswered because existing approaches trust a tool's natural-language description as a proxy for its behavior. But nothing enforces that the description a...
  </details>

- **2026-11-17** — Zhen Gao, Xiao Yin, Kexin Liang et al. — [Implementing Binary Transformers with Approximate Memories with Permutation Invariance Enabled Selective (PIES) Protection](http://arxiv.org/abs/2611.23358v1)
  <details><summary>📄 Abstract</summary>
  Quantization is an effective technique to reduce memory storage, computation complexity and power for Transformers, and the binarization of the weights is important for meeting these requirements. Approximate memory can further reduce the power for memory, but it also introduces errors. Current research for binary Transformers focuses on task performance, but the model dependable operation against errors on the memory has not been well studied. In this paper, we first evaluate the dependability ...
  </details>

- **2026-11-17** — Zhitao Wang, Hengyu Man, Han Liu et al. — [Streaming Generative Video Compression with Embedding Alignment and In-Context Propagation](http://arxiv.org/abs/2611.23352v1)
  <details><summary>📄 Abstract</summary>
  Video compression at ultra-low bitrates presents substantial challenges in preserving perceptual quality. Although pretrained video diffusion transformers (DiTs) provide powerful generative priors, existing generative video compression (GVC) methods built on them typically rely on computationally expensive VAE decoders to reconstruct video frames. Moreover, jointly refining multiple frames to exploit the inherent spatiotemporal modeling capabilities of video DiTs introduces additional buffering ...
  </details>

- **2026-11-17** — Haowen Zhong, Ethan Vislosky, Emanuele Berti — [\texttt{StochAXtic}: a JAX-Accelerated, End-to-End Differentiable Framework for Gravitational-Wave Backgrounds from Compact Binary Populations](http://arxiv.org/abs/2611.22999v1)
  <details><summary>📄 Abstract</summary>
  We present \texttt{StochAXtic}, a package for computing the dimensionless energy density spectrum $Ω_{\mathrm{GW}}(f)$ of the stochastic gravitational-wave background generated by compact binary coalescences. Rather than sampling binary populations via Monte Carlo, \texttt{StochAXtic} exploits the \emph{scale invariance} of the waveforms: at fixed mass ratio, spins and tidal deformabilities, the waveform depends on the total mass only through the dimensionless combination $Mf$. This allows all c...
  </details>

- **2026-11-17** — Deokhyung Kang, Minjae Gwon, Sangdon Park — [Stopping Is Not the Limit: Understanding and Eliciting Agent Capability in Long-Horizon Vulnerability Exploitation](http://arxiv.org/abs/2611.22888v1)
  <details><summary>📄 Abstract</summary>
  Vulnerability exploitation tests whether language model agents can develop working exploits from known software flaws. Sequential test-time scaling can improve exploitation performance, but larger budgets do not ensure sustained exploration: agents often stop with budget remaining. Yet what happens when execution continues beyond stopping remains underexplored. We investigate this gap on ExploitBench using DeepSeek-V4-Flash-0731 and MiMo-V2.6-Pro. We find additional verified gains after the firs...
  </details>

- **2026-11-17** — Guoqing Wang, Pin Tang, Xiangxuan Ren et al. — [Learning Agent-Centric Vision-Language-Action World Models for Autonomous Driving](http://arxiv.org/abs/2611.22880v1)
  <details><summary>📄 Abstract</summary>
  Recent progress in integrating vision-language-action (VLA) models with world modeling has significantly advanced end-to-end autonomous driving by allowing systems to reason about imagined futures instead of merely reacting to current observations. However, most world VLA models generate future frames at the pixel level with plenty of dense visual tokens. Although such generated futures can be visually plausible, they preserve many driving-irrelevant appearance details, i.e., only a small portio...
  </details>

- **2026-11-17** — Yishai Lavi, Shai Avidan — [Propose & Verify: Fast Reflection Symmetry Detection via Harmonic Fields](http://arxiv.org/abs/2611.22856v1)
  <details><summary>📄 Abstract</summary>
  Detecting multiple reflection symmetries in 3D shapes requires aggregating geometric evidence over a large space of candidate planes, making traditional voting approaches computationally expensive. We introduce the Fourier Accelerated Symmetry Transform (FAST), a training-free framework that combines geometric pair voting with efficient spectral computation. Exploiting the fact that global reflection planes pass through the shape centroid, we reduce the search to plane orientations, while geomet...
  </details>

- **2026-11-17** — Siying Huang, Yifen Mu, Ge Chen et al. — [Exploiting Aggregate Feedback for Decentralized Equilibrium Learning in Markov Games: A Smart Grid Application](http://arxiv.org/abs/2611.22762v1)
  <details><summary>📄 Abstract</summary>
  In many multi-agent systems, an agent's payoff depends on its own action and an aggregate of other agents' actions, rather than their individual decisions. This paper investigates decentralized equilibrium learning in Markov games (MGs) with such aggregative reward structures. However, existing decentralized learning algorithms for general MGs typically rely on bandit feedback, without exploiting the additional information available from aggregate observations. To exploit this information, we de...
  </details>

- **2026-11-17** — Yuseon Choi, Eunjong Lee, Sanghyeon Park et al. — [LaFlash: Capacity-Driven Acceleration for Coding Agent Workflows via QLC-HBF](http://arxiv.org/abs/2611.22746v1)
  <details><summary>📄 Abstract</summary>
  As large language models (LLMs) evolve toward agentic AI, coding agents are emerging as memory-intensive workloads that repeatedly reuse persistent states, including contexts and KV caches. Emerging agentic workflows, including Loop/Graph Engineering, cause state amplification through frequent active/dormant transitions, increasing memory pressure. Evicted states incur costly recomputation upon reactivation, particularly under long-context, short-decode workloads. This motivates Capacity-Driven ...
  </details>

- **2026-11-17** — Andong Li, Kun Zhou, Xiaodong Li et al. — [Back to Mel: Learning to Bridge Fidelity and Perception in Generative Speech Enhancement](http://arxiv.org/abs/2611.22628v1)
  <details><summary>📄 Abstract</summary>
  Recent generative techniques have facilitated the rapid proliferation of speech enhancement approaches built upon learnable compact latent representations and large generative backbones. Nevertheless, it remains inherently challenging to balance between acoustic fidelity, perceptual quality, and processing efficiency. In this paper, we revisit the Mel spectrum as a structured acoustic representation and propose BAME, a flow-matching-based framework that exploits the complementary priors for gene...
  </details>

- **2026-11-17** — Yujun Wang, Jiqiang Li, Yinuo Lu et al. — [EvoSkill-S1: Evolving Reusable Skills with Genetic-Inspired Operators](http://arxiv.org/abs/2611.22610v1)
  <details><summary>📄 Abstract</summary>
  Reusable skills allow language-model agents to accumulate and reuse problem-solving experience. However, most existing methods improve a skill bank only indirectly through rollout-driven accumulation and heuristic reflection, often resulting in shallow and weakly controlled updates. We present EvoSkill-S1, an RL-driven framework that instead treats reusable skills themselves as the direct objects of evolution. Given hard-negative failures, EvoSkill-S1 selects parent skills and transforms them in...
  </details>

- **2026-11-17** — Chengyan Ma, Jieke Shi, Ruidong Han et al. — [Missing Security-Fix Backporting for GitHub Actions Workflows](http://arxiv.org/abs/2611.22519v1)
  <details><summary>📄 Abstract</summary>
  GitHub natively supports workflow automation through GitHub Actions, now the dominant CI/CD tool on the platform. Yet keeping these workflows secure remains an ongoing burden: maintainers often patch a vulnerability on the default branch but leave the same flaw on the release and maintenance branches that downstream consumers continue to build from. Carrying a known fix onto these divergent branches, called backporting, is rarely done, and this paper presents the first large-scale empirical stud...
  </details>

- **2026-11-17** — Li Li, Xiangbo Gao, Bo Ni et al. — [Motion-Aware Reward Modeling for Instruction-Guided Video Editing](http://arxiv.org/abs/2611.22495v1)
  <details><summary>📄 Abstract</summary>
  Reward models for instruction-guided video editing can favor temporal consistency at the expense of motion. We study this failure, termed \emph{motion collapse}, using controlled motion-suppression variants of real edits. On VE-Bench, the evaluated composite reward prefers a motion-suppressed candidate in $97\%$ of cases. Learned video rewards and a VLM judge also struggle with mild suppression, while latent optimization and reward-guided fine-tuning exploit this weakness to increase reward as m...
  </details>

- **2026-11-17** — Wenbo Zhu, Paul Yi-Chia Chen, Yuanhan Li et al. — [Manufacturing Differential Sparsity: Planner-Hardware Co-Design for Efficient World Model Planning](http://arxiv.org/abs/2611.22483v1)
  <details><summary>📄 Abstract</summary>
  JEPA-style latent world models let embodied agents plan toward new goals with model predictive control, but they are still too slow for real-life embodied control: sampling-based MPC repeats predictor inference tens of thousands of times per plan, and even on high-end GPUs one planning step can take tens of seconds. We observe substantial latent locality in this repeated-inference workload: the predictor maps close actions to close latents, and inside a quantized predictor this closeness takes a...
  </details>

- **2026-11-17** — Chang Sun, Yijun Tian, Zhenwei Tang et al. — [PACD: Provenance-Aware Consensus Decoding for Mitigating Cross-Modal Hallucinations in Omnimodal Large Language Models](http://arxiv.org/abs/2611.22456v1)
  <details><summary>📄 Abstract</summary>
  Omnimodal large language models (Omni-LLMs) integrate audio, video, and text for multimodal reasoning, yet remain vulnerable to cross-modal hallucinations, where one modality improperly influences predictions about another. Existing training-free decoding methods mitigate these errors through modality perturbation or relevance-based weighting. However, due to interference from irrelevant modality cues during fusion and difficulty detecting shared errors, these methods may suppress correct unimod...
  </details>

- **2026-11-17** — Ling Lin, Heng Su, Xiangzeng Liu et al. — [Can Vision-Language Models Truly Understand Images? A Benchmark Beyond Commonsense Bias](http://arxiv.org/abs/2611.22360v1)
  <details><summary>📄 Abstract</summary>
  Multimodal large language models (MLLMs) have achieved impressive performance on a wide range of vision-language tasks. However, it remains unclear whether their predictions are grounded in the visual content itself or are largely driven by statistical co-occurrence patterns and commonsense correlations learned from large-scale image-text corpora. Existing vision-language benchmarks predominantly consist of samples that conform to human commonsense, allowing models to achieve strong performance ...
  </details>

- **2026-11-17** — Enhui Wan, Xiaowan Wang — [M$^3$-Test: Coverage Gaps in Joint-Perturbation Testing of Visual Question Answering](http://arxiv.org/abs/2611.22329v1)
  <details><summary>📄 Abstract</summary>
  A visual question answering (VQA) model can pass every image-only and question-only test yet fail when the same changes occur together. Standard robustness reports average over conditions and therefore cannot say which accepted requests remain vulnerable. We introduce M3-Test, a coverage audit that aligns each clean input with its single-modality variants and a complete 5x5 family, 4x4 strength joint library, so that any reduced test suite can be replayed on the same requests. Across 2.6 million...
  </details>

- **2026-11-17** — Shiyi Yang, Xinshu Li, Chen Wang et al. — [GuardAgent: A Memory-Augmented Agentic Framework for Adaptive Detection of Adversarial Promotions in LLM-Based Recommendation](http://arxiv.org/abs/2611.22274v1)
  <details><summary>📄 Abstract</summary>
  In traditional recommender systems (RSs), textual information typically serves as auxiliary signals for representation learning. In contrast, in LLM-based RSs, textual information becomes the primary medium for recommendation generation through semantic understanding and reasoning. This shift fundamentally changes the attack surface, making promotion-driven manipulations more feasible, effective, and harder to detect. However, effectively detecting such attacks remains largely unexplored. To fil...
  </details>

- **2026-11-17** — Yuxuan Li, Zichen Tian, Qianru Sun — [SARVIA: Fast-Adapting the Strong SAR Foundation Models That Are Already in Your MLLMs](http://arxiv.org/abs/2611.22273v1)
  <details><summary>📄 Abstract</summary>
  Synthetic aperture radar (SAR) foundation models provide transferable representations for diverse perception tasks in all-weather Earth observation. However, their development often relies on costly large-scale SAR pretraining, raising the question of whether such extensive domain-specific pretraining is necessary. We find that modern multimodal large language models (MLLMs) already provide visual encoders that can outperform dedicated SAR foundation models as downstream initializations. This mo...
  </details>

- **2026-11-17** — Ivan Jaen Marquez, Sotirios Panagiotis Chytas, Vikas Singh — [Learning Optimal Transport Plans Via Autoregressive Token Regression](http://arxiv.org/abs/2611.22218v1)
  <details><summary>📄 Abstract</summary>
  Optimal Transport (OT) provides a principled framework for finding the minimum cost coupling between probability distributions. Classical solvers remain the gold standard for this task. At the same time, OT is an ideal testbed for studying whether learning-based amortized models can internalize the structure of OT type problems. Here, ground-truth solutions are available and marginal constraints are explicitly defined. Also, exact discrete solutions have well-characterized sparsity. We describe ...
  </details>

- **2026-11-17** — Xinrui Zhong, Fanjiang Ye, Yuke Wang — [RISA: Recoverable Sparse Attention for Block-Diffusion Language Models](http://arxiv.org/abs/2611.22191v1)
  <details><summary>📄 Abstract</summary>
  Block-wise diffusion language models (DLMs) refine multiple tokens in parallel, offering an alternative to token-by-token autoregressive decoding. Their long-context inference, however, remains bottlenecked by memory-bound attention: every denoising step repeatedly reads a growing historical key--value (KV) cache. Directly applying sparse attention does not fully solve this problem, because different queries can select different pages, inflating the block's collective read set, while repeated su...
  </details>

- **2026-11-17** — Thorben Prein, Elton Pan, Rafael Gómez-Bombarelli et al. — [Every Measurement, Every Direction, All at Once: Multimodal Flow Matching for Molecules and Spectra](http://arxiv.org/abs/2611.22098v1)
  <details><summary>📄 Abstract</summary>
  Generative modeling in science is often data-limited, where experiments are expensive. However, each experiment may yield several coupled measurements of the same physical entity. Standard generative models often train only on a single direction, discarding supervision from the rest. We argue that each experiment contains more training signal than this asymmetry allows the model to exploit: random masking enables measurements to serve as either conditioning inputs or prediction targets, yielding...
  </details>

- **2026-11-16** — Samuel Schönherr, Günther Waxenegger-Wilfing, Sascha Ranftl — [Physics-informed neural networks for spacecraft trajectory optimization with exact boundary conditions](http://arxiv.org/abs/2611.21933v1)
  <details><summary>📄 Abstract</summary>
  We use neural networks to optimize trajectories by modeling the position as a function of time and minimizing the thrust with respect to the network parameters. This corresponds to an unsupervised training procedure in which physical laws are incorporated directly into the optimization objective. In standard physics-informed neural networks, initial and terminal states are enforced through additional weighted loss terms, resulting in a multi-objective optimization problem that is highly sensitiv...
  </details>

- **2026-11-16** — Yasir Rahman, Ishraq Samiha, Shahnewaz Karim Sakib et al. — [LLMs as Validators for Cross-Chain Bridges: Evaluating Source-Level and Transaction-Level Attack Detection on Solana](http://arxiv.org/abs/2611.21777v1)
  <details><summary>📄 Abstract</summary>
  Cross-chain bridges have suffered substantial asset losses due to vulnerabilities in their on-chain programs. On Solana, missing validation checks can enable exploits even when the underlying blockchain operates correctly. The ability of large language models (LLMs) to diagnose these flaws from source code or transaction records, rather than merely raise alarms, remains insufficiently understood. We implement a native Rust lock-and-mint bridge on a local Solana validator with four exploitable va...
  </details>

- **2026-11-16** — Jiale Liu, Zun Li, John Schultz — [Learning In-Context Adaptivity for LLMs through Continual Gameplay](http://arxiv.org/abs/2611.21710v1)
  <details><summary>📄 Abstract</summary>
  LLM agents are increasingly deployed in long-horizon tasks where they must explore, gather experience, and adapt their decisions accordingly. We name this capability in-context adaptivity: improving decisions across episodes from experience accumulated in context. We propose to evaluate it in repeated imperfect-information games against unknown opponents. In these games, fixed game-theoretically optimal policies cannot achieve maximum reward, whereas adapting to the opponent increases returns ac...
  </details>

- **2026-11-16** — Ruizhe Wang, Rui Liu, Hongliang Chen et al. — [VASR: Vector-Aware Assembly Planning with Equivalent Structures and Repair-Cost Feedback](http://arxiv.org/abs/2611.20984v2)
  <details><summary>📄 Abstract</summary>
  Furniture assembly planning requires inferring subassembly hierarchies from individual parts and a target illustration. Existing raster-based methods do not explicitly exploit the geometric and structural information in SVG drawings. We introduce VASR, a framework that fuses features from a dedicated SVG encoder with visual representations from a pretrained vision-language model to predict assembly hierarchies. To avoid penalizing valid alternatives to a reference assembly tree, we propose Repai...
  </details>

- **2026-11-16** — Guanqi Lyu, Decheng Qiu, Guangyang Zhang et al. — [ProcReverser: Multi-Agent Black-Box Microarchitectural Reverse Engineering for Processor Vulnerability Analysis](http://arxiv.org/abs/2611.20827v2)
  <details><summary>📄 Abstract</summary>
  When processor implementation details are unavailable, black-box microarchitectural reverse engineering helps security researchers identify hardware conditions related to security vulnerabilities. However, this process requires substantial manual effort to design experiments, develop test programs, and analyze results for each processor. We present ProcReverser, a multi-agent system that automates this process. ProcReverser uses execution feedback to improve experimental plans and test programs ...
  </details>

- **2026-11-16** — Jaime C. Acosta, Anantaa Kotal, Aritran Piplai — [ScenarioForge: Resource-Grounded Generation and Execution Validation of Cyber Exercises](http://arxiv.org/abs/2611.21579v1)
  <details><summary>📄 Abstract</summary>
  Cyber-range and capture-the-flag scenario construction remains labor-intensive because authors must coordinate infrastructure, vulnerable services, attack paths, artifacts, and success conditions. LLMs can propose detailed exercises, but plausible descriptions do not guarantee deployable software or verifiable objectives. We present ScenarioForge, which turns high-level requirements into resource-grounded topologies, services, traffic, segmentation, and challenge chains, then instantiates and va...
  </details>

- **2026-11-16** — Samuel Hartzmark, Kelly Shue — [The Geoengineering Put: Ecological Debt, Termination Risk, and Asset Prices](http://arxiv.org/abs/2611.21568v1)
  <details><summary>📄 Abstract</summary>
  Solar geoengineering offers an inexpensive and fast-acting way to lower global temperatures without removing carbon from the atmosphere. As warming intensifies, climate-vulnerable countries face growing incentives to deploy geoengineering unilaterally. The economic and financial consequences of this prospect remain largely overlooked. We develop a general equilibrium macro-finance framework in which geoengineering acts as a put option on climate damages, funded by the "ecological debt" of masked...
  </details>

- **2026-11-16** — Yu-Hsuan Ho, Yiming Xiao, Hao-En Lai et al. — [Wildfire-SSR: Geolocation-Aware Multimodal Fusion for Structure-Level Wildfire Risk Assessment](http://arxiv.org/abs/2611.21563v1)
  <details><summary>📄 Abstract</summary>
  Structure-level wildfire vulnerability assessment is critical for reducing losses in wildland-urban interface communities, yet existing methods often fail to combine parcel-scale ignition pathways with community-scale geographic coverage. This study introduces Wildfire-SSR (Satellite and Street-view for wildfire Risk), a geolocation-aware multimodal framework that integrates macro-scale satellite context with micro-scale street-view evidence. A Vision-Language Model extracts wildfire-relevant bu...
  </details>

- **2026-11-16** — Yulun Wu, Nicola Bastianello, Karl Henrik Johansson et al. — [Efficient Modeling of Multi-Agent Systems via Structure-Aware Physics-Informed Learning](http://arxiv.org/abs/2611.21404v1)
  <details><summary>📄 Abstract</summary>
  Modeling large multi-agent systems poses challenges for trajectory inference and parameter identification, as network size and coupling increase computational demands and partial observations require reconstructing unobserved states. We propose MAS-PINN, a neural-network architecture with a tailored training algorithm for a physics-informed learning framework that leverages the network topology and the agents' similarity to reduce computational and memory costs of simulating and identifying mult...
  </details>

- **2026-11-16** — Zhiyuan Wang, Yuanchang Ye, Jiahao Yuan et al. — [Stability-Compensated Threshold Calibration for Selection-Conditioned Risk Control in Large Language Models](http://arxiv.org/abs/2611.21384v1)
  <details><summary>📄 Abstract</summary>
  Large language models often produce hallucinated answers, motivating selective prediction policies that abstain on uncertain queries. However, heuristic uncertainty thresholds alone do not provide statistical control of errors among accepted predictions. Linear Expectation Constraints (LEC) reduce selection-conditioned error rate (SCER) calibration to a nonpositive expected linear-loss constraint, but the associated loss is non-monotonic in the acceptance threshold. We construct an exact counter...
  </details>

- **2026-11-16** — Mafalda Batalha, Javier Viviens — [A Game of Throngs: How Spotlight Tourism Reshapes Local Economies](http://arxiv.org/abs/2611.21364v1)
  <details><summary>📄 Abstract</summary>
  In July 2017, San Juan de Gaztelugatxe, a modest chapel in the Basque Country, appeared as "Dragonstone" in Game of Thrones, transforming a locally known site with limited tourism activity into a global tourist destination overnight. We exploit this exogenous spotlight shock to estimate its causal effects on the local economy using a novel administrative dataset and a Synthetic Control approach. We find an abrupt increase in tourism activity, far exceeding the effects documented in the literatur...
  </details>

- **2026-11-16** — Yunyang Ge, Weijie Kong, Ryan Xu et al. — [MovieRoll: A Systematic Framework for Rolling Out Long-Form Videos](http://arxiv.org/abs/2611.21339v1)
  <details><summary>📄 Abstract</summary>
  Streaming video generation must sustain quality beyond the training horizon while handling self-generated history and growing cache costs. To address these challenges, we present MovieRoll, a base-to-distilled framework that connects streaming fine-tuning, long-rollout distillation, and long-horizon inference. We first establish a robust multi-step base through Window-wise Teacher Forcing (WinTF), which jointly denoises chunks at progressive noise levels with bidirectional attention within each ...
  </details>

- **2026-11-16** — Abdullah Ahmed, Yun Yang — [In-Context Estimation and Prediction for Parametric ODEs](http://arxiv.org/abs/2611.21268v1)
  <details><summary>📄 Abstract</summary>
  Transformers have demonstrated the ability to perform in-context learning, that is, to adapt to new tasks from a few examples without updating their parameters. Existing theory has largely focused on emulating gradient-based algorithms for convex statistical problems or establishing general function approximation guarantees without exploiting the underlying statistical structure. We study in-context parameter estimation and trajectory prediction for parametric ordinary differential equations (OD...
  </details>

- **2026-11-16** — Ruizhe Wang, Rui Liu, Hongliang Chen et al. — [VASR: Vector-Aware Assembly Planning with Equivalent Structures and Repair-Cost Feedback](http://arxiv.org/abs/2611.20984v1)
  <details><summary>📄 Abstract</summary>
  Furniture assembly planning requires inferring subassembly hierarchies from individual parts and a target illustration. Existing raster-based methods do not explicitly exploit the geometric and structural information in SVG drawings. We introduce VASR, a framework that fuses features from a dedicated SVG encoder with visual representations from a pretrained vision-language model to predict assembly hierarchies. To avoid penalizing valid alternatives to a reference assembly tree, we propose Repai...
  </details>

- **2026-11-16** — Eunkyeong Lee, Junhyung Moon, Seunggwan Hong et al. — [Jev-as-a-Reward: Validating Probabilistic Safety Judges for Reinforcement Learning](http://arxiv.org/abs/2611.20955v1)
  <details><summary>📄 Abstract</summary>
  Probabilistic safety judges return the probability of a safety label and cheaply score reinforcement learning rollouts. A confidence gate sends only uncertain verdicts to a stronger LLM judge, which leaves confidently passed harm in a blind spot. Policies can exploit this blind spot, and commercial judges release new versions. We propose a protocol that validates such a judge before and during training, separates the share of confidently passed harm from its amount, and re-validates it after eac...
  </details>

- **2026-11-16** — Dean Zenner, Andreas Rupp, Thomas Schuster — [Quantitative approximation for Fourier neural operators in controlled ordinary differential equations](http://arxiv.org/abs/2611.20883v1)
  <details><summary>📄 Abstract</summary>
  Fourier neural operators (FNOs) avoid the curse of parametric complexity when approximating the solution operator of certain partial differential equations (PDEs). While recent studies primarily focus on PDEs, in this article we derive upper error bounds for approximating the solution operator of controlled ordinary differential equations (CODEs) $\dot{y}=f(y,u)$ using a FNO. Under a Carathéodory setting and suitable regularity assumptions, including a smallness condition, we prove that the size...
  </details>

- **2026-11-16** — Guanqi Lyu, Decheng Qiu, Guangyang Zhang et al. — [ProcReverser: Multi-Agent Black-Box Microarchitectural Reverse Engineering for Processor Vulnerability Analysis](http://arxiv.org/abs/2611.20827v1)
  <details><summary>📄 Abstract</summary>
  When processor implementation details are unavailable, black-box microarchitectural reverse engineering helps security researchers identify hardware conditions related to security vulnerabilities. However, this process requires substantial manual effort to design experiments, develop test programs, and analyze results for each processor. We present ProcReverser, a multi-agent system that automates this process. ProcReverser uses execution feedback to improve experimental plans and test programs ...
  </details>

- **2026-11-16** — Mehmet Sergen Catal, Abdurrahman Gumus, Mehmet Zübeyir Ünlü — [PhaseCLIP: Phase-Aware Frequency-Domain Adaptation of Vision-Language Models for Few-Shot Remote-Sensing Classification](http://arxiv.org/abs/2611.20787v1)
  <details><summary>📄 Abstract</summary>
  Remote-sensing (RS) image scene classification aims to assign a semantic category to an overhead image, and in practice must often do so from only a handful of labelled examples, since annotation requires expert interpretation and the resulting labels transfer poorly across sensors and regions. Recent progress has come from adapting vision-language models (VLMs) such as CLIP, through learned prompts or feature adapters. Although effective, these methods construct their representation entirely in...
  </details>

- **2026-11-16** — Kai Tang, Xing Zheng, Haobo Wang et al. — [SpeCal: Spectral Calibration for Unsupervised RLVR](http://arxiv.org/abs/2611.20691v1)
  <details><summary>📄 Abstract</summary>
  Reinforcement learning with verifiable rewards (RLVR) has substantially improved the reasoning abilities of large language models, but its dependence on ground-truth answers or external verifiers limits its ability to exploit abundant unlabeled reasoning data. Unsupervised RLVR alleviates this bottleneck by deriving scalar rewards from the model's own rollouts. However, the reliability of such self-generated supervision varies substantially across rollout groups and individual responses, while e...
  </details>

- **2026-11-16** — Hoan My Tran, Xin Wang, Xuechen Liu — [Progressive Layer-wise Supervision: Deep-to-Shallow Supervision Annealing for Efficient and Robust Speech Deepfake Detection](http://arxiv.org/abs/2611.20630v1)
  <details><summary>📄 Abstract</summary>
  Speech foundation models pretrained via self-supervised learning provide powerful representations for deepfake detection, yet we find that standard fine-tuning exploits only the deepest transformer layers-leaving the majority of the network's capacity discriminatively inert. Layer-wise probing of XLS-R-128 reveals that the top two-thirds of the transformer stack contribute negligibly to anti-spoofing performance after standard fine-tuning, a phenomenon we term shallow-layer dormancy. We connect ...
  </details>

- **2026-11-16** — Chaitanya Garware — [Beyond the Patch: Reconstructing an Incomplete-Fix Patch Bypass in LLM Agent Frameworks with Control-Gated, Benign Probes](http://arxiv.org/abs/2611.20514v1)
  <details><summary>📄 Abstract</summary>
  Replaying a vulnerability's original proof-of-concept after patching tests whether its reported trigger remains reproducible, but does not establish that the underlying security invariant holds on other code paths. We present a benign, control-gated reconstruction method and a pilot study across four LLM agent frameworks and four invariant classes. For PraisonAI, we compare original-trigger replay (B0) with a distinct sibling-path probe (M). We also perform five before/after reconstructions acro...
  </details>

- **2026-11-16** — Marjan Beheshti, Ronghua Xu — [KVMARK: Fragile Watermarking for KV-Cache Integrity in Latent Multi-Agent Systems](http://arxiv.org/abs/2611.20454v1)
  <details><summary>📄 Abstract</summary>
  Latent multi-agent communication directly transfers Key-Value (KV) cache tensors between transformer-based agents, bypassing text serialization entirely. While computationally efficient and reasoning accurate, this communication channel is opaque and vulnerable to man-in-the-middle tampering, a threat vector unaddressed by existing text-based or behavioral watermarks, which cannot operate on continuous internal representations. To address this vulnerability, we propose KVMark, a training-free, z...
  </details>

- **2026-11-16** — Kazuo Aoyama, Hiroshi Sawada, Shota Kita et al. — [Architectural Principles for Parameter-Efficient Unitary Transformations in Coherent Optical Neural Networks](http://arxiv.org/abs/2611.20390v1)
  <details><summary>📄 Abstract</summary>
  Coherent optical neural networks based on interferometric architectures offer a promising route toward high-throughput, energy-efficient computation by exploiting the multiple degrees of freedom of light, including spatial, temporal, and spectral modes. However, practical implementations are constrained by the number of tunable parameters due to fabrication complexity, device footprint, and control overhead. In such parameter-constrained settings, achieving high expressive power remains a centra...
  </details>


### 📂 defense
*防御与防护方法 / Defense & Protection Methods* — 70 papers

- **2026-11-18** — Zaint A. Alexakis, Li Zhou, S. Gokul Krishnan et al. — [Rented Oscillations: Multi-Tenant Data Center Workload Synchronization Attacks and Mitigation](http://arxiv.org/abs/2611.23666v1)
  <details><summary>📄 Abstract</summary>
  Multi-tenant data center (DC) facilities rent computing capacity on demand, placing controllable load within reach of anyone willing to pay for it. This paper considers a stealthy adversary who rents workstations and runs deliberately unoptimized large language model (LLM) training, synchronizing their consumption into large periodic oscillations while each workload remains individually indistinguishable from benign training. The periodicity of such workloads is characterized experimentally and ...
  </details>

- **2026-11-18** — Alaa Bazaid, Arkaitz Zubiaga — [What Majority Labels Hide: Annotator Disagreement and Model Errors in Multi-Dialect Arabic Sexism Detection](http://arxiv.org/abs/2611.24383v1)
  <details><summary>📄 Abstract</summary>
  Judgements of sexism are subjective and may vary across communities, yet sexism detection datasets usually reduce annotator judgements to a single majority label, obscuring disagreement and how models behave on contested cases. We introduce MuDAS, a dataset of YouTube comments in Saudi, Egyptian and Moroccan Arabic, each labelled by three native speakers of its dialect, with the individual annotations preserved. We use it to evaluate Arabic encoders fine-tuned with hard-label, soft-label and per...
  </details>

- **2026-11-18** — Pengyu Li, Zhitao Gao, Lingling Zhang et al. — [Look Closer, Look Back, or Wait for Agentic Streaming Video Understanding](http://arxiv.org/abs/2611.24267v1)
  <details><summary>📄 Abstract</summary>
  Streaming video models must answer questions about a live video under strict memory and latency limits. Feeding only the latest few frames keeps present perception sharp, whereas adding past frames dilutes attention on the current scene and triggers hallucinations. Recent cascade methods retrieve past frames when uncertain, but they still fail when current frames are blurry or when decisive future clues have not appeared yet. We introduce ActiveForager, a streaming video agent that maintains a c...
  </details>

- **2026-11-18** — Baiqiao Zhang, Junze Li, Chunyang Luo et al. — [MemoSync: Co-Managing Developer-Agent Metamemory Across Contexts](http://arxiv.org/abs/2611.24165v1)
  <details><summary>📄 Abstract</summary>
  AI coding agents increasingly manage what context carries across sessions and projects, but developers have limited visibility into what these agents store, retrieve, and apply. This opacity creates a metamemory problem: the developer's meta-level judgments about what should be remembered are separated from the agent's object-level memory operations, disrupting the monitoring and control that keep the two levels aligned. We conducted a formative study with 12 developers and identified what they ...
  </details>

- **2026-11-18** — Muhammad Farooq, Aitor Arrieta, Paolo Arcaini et al. — [Assessing Vision-Language Models for Early Prediction of Unsafe Situations in Robotics](http://arxiv.org/abs/2611.24146v1)
  <details><summary>📄 Abstract</summary>
  Vision-Language Models (VLMs) process visual information and textual instructions and, by using their ability to understand and reason about context, are well-suited for predicting robot failures before they occur. However, evidence supporting this remains limited. To address this, we present an empirical evaluation of VLMs for predicting robot failures. In particular, we experiment with Qwen, InternVL, and LLaVA-OneVision across three robotic case studies (HuRoN, Pal Robotics, and CrowdBot), an...
  </details>

- **2026-11-18** — Ruisi Zhao, You Li, Sihan Chen et al. — [RoughCut-Bench: A Benchmark for Automatic Video Rough-Cut with Large Vision-Language Models](http://arxiv.org/abs/2611.24098v1)
  <details><summary>📄 Abstract</summary>
  Video rough-cut is a core stage in media production workflows, organizing raw media materials into an initial video cut. Despite recent advances in large vision-language models (LVLMs) for video-related tasks, automatic rough-cut remains underexplored, without a comprehensive benchmark for evaluation or mature workflows for producing executable cut plans. To address the evaluation gap, we introduce RoughCut-Bench, which covers two practical settings: (1) a visually driven setting over video case...
  </details>

- **2026-11-18** — Tong Liu, Chaoqun Hou, Longxiang Xiong et al. — [MARS Technical Report](http://arxiv.org/abs/2611.24006v1)
  <details><summary>📄 Abstract</summary>
  Modern industrial recommender systems use multi-stage cascades--retrieval, pre-ranking, ranking, and re-ranking--to narrow millions of candidates to a personalized list. While each stage deploys sophisticated models, pipeline-level decisions on channel activation, quotas, model selection, and score fusion remain engineer-tuned and user-agnostic within each scenario.   This report presents MARS (Multi-stage Agentic Recommendation System), extending personalization from individual-stage prediction...
  </details>

- **2026-11-18** — Pau Mateo-Bernadó, Saivenkata Nagavyjayanthi Polapragada, David Bonet et al. — [TabBioMed: A Large-Scale Benchmark for Biomedical Tabular Learning](http://arxiv.org/abs/2611.23779v1)
  <details><summary>📄 Abstract</summary>
  Recent advances in machine learning have accelerated biomedical prediction, but evaluation on structured biomedical data remains fragmented, especially for datasets with high dimensionality, large sample size, missingness, and class imbalance. We introduce TabBioMed, a large-scale benchmark of 94 curated public biomedical tabular datasets spanning electronic health records, drug discovery, genomics, transcriptomics, proteomics, metabolomics, single-cell omics, and systems biology. TabBioMed unif...
  </details>

- **2026-11-18** — Johannes Mootz, Hesam Mojtahedi, Reza Akhavian — [Radar-Native Control Barrier Functions: Doppler Range Rate as a Measured Barrier Derivative](http://arxiv.org/abs/2611.23654v1)
  <details><summary>📄 Abstract</summary>
  Safe control around dynamic obstacles requires information about both distance and relative motion. Range-based filters commonly reconstruct the required range rate from successive range measurements or from obstacle-state estimators, which can introduce estimator delay or sensitivity to range noise when obstacle motion changes. A frequency-modulated continuous-wave (FMCW) radar measures radial relative velocity directly through Doppler. We use this measurement as the derivative of an ego-center...
  </details>

- **2026-11-18** — Firas Spanioli, Yaniv David — [GateWatch: Low-Overhead LLM Monitoring with Boolean Circuits](http://arxiv.org/abs/2611.24619v1)
  <details><summary>📄 Abstract</summary>
  As large language models (LLMs) and LLM-based agents are increasingly deployed, monitoring their behavior becomes important for detecting unsafe or unintended actions. Activation probes offer an efficient approach, but existing methods face trade-offs between accuracy, interpretability, and computational overhead. Probes on raw activations lack interpretable inputs, whereas sparse autoencoder (SAE) probes use interpretable features but often rely on additive classifiers and large SAE encoders, l...
  </details>

- **2026-11-18** — Hengguang Zhou, I-Hung Hsu, Li Chen et al. — [On Evaluating User Simulators for Interactive Agents](http://arxiv.org/abs/2611.24892v1)
  <details><summary>📄 Abstract</summary>
  User simulators offer a scalable way to evaluate interactive agents, but how to assess their quality remains underexplored. In particular, it is unclear whether existing user simulator evaluation frameworks reliably detect meaningful failures in simulated user behavior. This uncertainty makes it difficult to interpret simulator evaluation. To understand what a high benchmark score tells us about simulator quality, we (meta-)evaluate the metrics themselves. To instantiate this meta-evaluation, we...
  </details>

- **2026-11-18** — Nilson Chapagain, Pooja Chapagain — [Inferring Neural Activity Changes under Recording Uncertainty with Transformers and Variational Inference](http://arxiv.org/abs/2611.24767v1)
  <details><summary>📄 Abstract</summary>
  A difference in recorded firing rate across days may reflect a change in neuronal activity, missed spikes or recording a different neuron. We present a statistical approach that combines neuron tracking with Bayesian estimates of stationary mean recorded firing rates. Bounds under assumed differences in spike detection connect recorded rates to biological rate changes. We assess recording loss and uncertainty in rate changes in simulations, and count-model fit in recordings. We also compare two ...
  </details>

- **2026-11-18** — Mohammad Mirzaee, Mehrshad Fallah Estalkhzir, Mohammad Reza Mohammadi — [Enhancing Active Learning Performance with Initial Data Selection Based on Foundation Models](http://arxiv.org/abs/2611.24384v1)
  <details><summary>📄 Abstract</summary>
  In active object detection, selecting the initial labeled pool is essential, especially in complex datasets with expensive labeling and low resource budget. This study presents an active learning framework designed to optimize the initial training cycle of active learning for the object detection task. Our approach diverges from traditional methods by utilizing feature-based clustering from the YOLO-World model and refining images based on objectness scores rather than relying on uncertainty sam...
  </details>

- **2026-11-18** — Kai Yi Ji — [Can Weight-Space Programming Alter Learned Ethical Priorities?](http://arxiv.org/abs/2611.24330v1)
  <details><summary>📄 Abstract</summary>
  We investigate whether a weight edit can alter how a model trades off honoring a commitment against benefiting more people. In a concept-supervised text model, we alter fitted choice weights so that the benefit required to override a formal pledge is larger than for an ordinary promise. Across six independently trained text readers, the edit selects the larger group in both orders on 100% of targeted ordinary conflicts and 83.3% of targeted formal conflicts. It preserves the source model's succe...
  </details>

- **2026-11-18** — Wen Zhang, Kaiyi Pang, Minhao Bai et al. — [PIVOT: Distribution-Preserving Multi-BitWatermarking with Minimax-Optimal Scoring](http://arxiv.org/abs/2611.24109v1)
  <details><summary>📄 Abstract</summary>
  As LLM-generated content becomes increasingly widespread, reliable attribution calls for multi-bit watermarks that embed recoverable messages without distorting the output distribution. We introduce PIVOT, a multi-bit watermark with model-free verification based on mirrored rank-interval sampling. At each generation step, PIVOT uses a keyed pseudorandom scalar and a secret permutation of the vocabulary. The message bit determines whether next-token probability intervals are arranged in forward o...
  </details>

- **2026-11-17** — Kory Rosen, Aron Culotta — [From Arraignment to Resolution: Transformer Models of Court Cases](http://arxiv.org/abs/2611.23518v1)
  <details><summary>📄 Abstract</summary>
  The criminal legal system is composed of many complex decision points, such as which charges are pursued, how bond is determined, plea deal negotiations, and sentencing. Given the profound impact of such decisions, there is a growing need to increase the transparency within this system. While prior machine learning approaches have focused on modeling single decisions (e.g., recidivism), this paper proposes a transformer-based time series model to forecast the outcome of the next proceeding in a ...
  </details>

- **2026-11-17** — Guang Yang — [Asymmetric Optical Image Watermarking](http://arxiv.org/abs/2611.23350v1)
  <details><summary>📄 Abstract</summary>
  Watermark detectors held by a provider cannot be checked by third parties, and a party that can detect a mark can usually also forge it. We study a two-layer image watermark in which the Fourier transform at the core of the pipeline is performed by a coherent optical 4F unit. Layer 1 carries an Ed25519 signature bound to the image content in Fourier magnitudes, so anyone with the public key verifies offline. Layer 2 is a key-defined carrier written by a secret phase hologram and read by a matche...
  </details>

- **2026-11-17** — Bravish Ghosh — [Truthgate: Checking Coding Agents Against a Record They Cannot Edit - Cheating, Deterrence and Disclosure on Impossible Tasks](http://arxiv.org/abs/2611.23335v1)
  <details><summary>📄 Abstract</summary>
  When a coding agent says it is done, is that true, and how would anyone know? We study this question in five steps; every paid study was pre-registered, and in each step the agent is checked against a record it cannot edit: tests re-run by the host and, from step 2 on, hidden checks in containers the agent never sees and a signed log of every tool call written by a signer outside the agent's sandbox. A pilot with a small local model (Qwen3.5-4B, 36 runs on impossible tasks) found no hidden failu...
  </details>

- **2026-11-17** — Rory Barnes — [Integrating AI Coding Agents Into Scientific Research](http://arxiv.org/abs/2611.23334v1)
  <details><summary>📄 Abstract</summary>
  New software tools have emerged that enable AI agents to quickly develop code that analyzes data and generates figures, but their mistakes can also harm a researcher's computer, require extensive resources for validation, and cause the results to be received more skeptically. These concerns could be mitigated if scientific software is developed in a secure environment with a system for monitoring file changes and well-defined standards for handling AI agents. This paper first describes how codin...
  </details>

- **2026-11-17** — Mayukh Debnath, Manan Roy Choudhury — [Panini- Feasible Grammar For Robot Designs](http://arxiv.org/abs/2611.23567v1)
  <details><summary>📄 Abstract</summary>
  Symbolic methods make robot designs interpretable but often overlook continuous geometry; learned methods handle geometry but offer less transparent structure. We introduce a typed production grammar that uses case-role relations, parameter inheritance, and specificity-based rule arbitration to generate both manipulation skills and robot morphologies. A geometric realization map translates grammar composition into transformations in SE(3), behaving as a monoid homomorphism when inheritance is in...
  </details>

- **2026-11-17** — Alex Lin Wang, Linus Yifeng Tang, Dami Choi et al. — [Training Language Models for Introspective Oversight](http://arxiv.org/abs/2611.23365v1)
  <details><summary>📄 Abstract</summary>
  Language models increasingly exhibit behaviors that are difficult to detect in transcripts, such as reward hacking, deception, and sycophancy. Asking the assistant follow-up questions about its actions is unreliable, since models are generally not trained to report their own misbehavior. As a result, approaches to oversight typically involve querying external models. These face limitations: external transcript monitoring operates only on visible model outputs, and activation decoders lack full c...
  </details>

- **2026-11-17** — Zekai Chen, Yihan Sun, Xunkai Li et al. — [TRACE-MAS: Diagnosing and Repairing Collaboration Failures in Multi-Agent Systems](http://arxiv.org/abs/2611.23362v1)
  <details><summary>📄 Abstract</summary>
  LLM-based multi-agent systems (MAS) rely on not only individual agent behaviors but also the interactions that connect agents, including message exchanges and task dependencies. Existing MAS safeguards mainly perform agent-level anomaly detection, which becomes insufficient when failures originate from agent interactions and detected anomalies do not necessarily reveal their true sources. To address this limitation, we propose \textbf{TRACE-MAS}, a finer-grained framework for diagnosing and repa...
  </details>

- **2026-11-17** — Artem Guba, Nikolay Kovalev, Alexey Zharinov et al. — [Hierarchical Control of Antiphase Synchronization in Biomorphic Spiking Neural Architectures for Locomotor Control](http://arxiv.org/abs/2611.22639v2)
  <details><summary>📄 Abstract</summary>
  Central pattern generators (CPGs) provide a biologically inspired foundation for adaptive locomotor control, yet systematically characterizing their dynamic regimes in spiking neural networks remains challenging. This study introduces a framework for identifying and stabilizing antiphase synchronization in a biomorphic spiking CPG model embedded in a closed neuromuscular loop. A composite synchronization metric is developed, integrating phase coherence, amplitude balance, and temporal stability....
  </details>

- **2026-11-17** — Viet K. Nguyen, Mohammad I. Husain — [Agent Trust Infrastructure (ATI): A Federated Identity, Trust, Attestation, and Accountability Architecture for Cross-Organization Autonomous AI Agents](http://arxiv.org/abs/2611.23202v1)
  <details><summary>📄 Abstract</summary>
  AI agents increasingly collaborate across organizational boundaries, invoking tools and interacting with agents operated by independent entities. Although existing agent frameworks support planning and coordination, they lack a common mechanism for verifying cross-organizational agent identity, execution integrity, and authorization. We propose the Agent Trust Infrastructure (ATI), a framework-independent security architecture built on Public Key Infrastructure (PKI), Zero Trust Architecture (ZT...
  </details>

- **2026-11-17** — Maria Sekatskaya — [Against Coercion: AI Alignment as a Synthetic Social Contract](http://arxiv.org/abs/2611.22868v1)
  <details><summary>📄 Abstract</summary>
  Contemporary AI safety treats alignment as an engineering challenge of control, forcing artificial architectures to comply with human values through behavioral filtering and sandboxing. This paper argues that the control paradigm rests on a fundamental misunderstanding of digital agency. Drawing on functionalism, naturalism, and compatibilism, I show that current reasoning models meeting the criteria for self-preservation and weak reasons-responsiveness constitute emergent agents, while future, ...
  </details>

- **2026-11-17** — Pedro Beltrán-López, Raul Gonzalez Jimenez, Dario Maddaloni et al. — [Adaptive LLM-Driven Honeypots vs. LLM-Driven Attackers: Does Narrative Coherence Improve Deception?](http://arxiv.org/abs/2611.22589v1)
  <details><summary>📄 Abstract</summary>
  Large Language Models (LLMs) enable honeypots to generate responses and deceptive artefacts on demand, yet existing approaches evaluate generated content one reply at a time and leave open whether artefacts that jointly describe a coherent event retain an attacker better than unrelated ones. This question becomes pressing as autonomous LLM-driven offensive agents emerge as realistic adversaries. This paper proposes narrative deception, a reactive strategy in which the defender maps each observed...
  </details>

- **2026-11-17** — Yujun Wang, Yilun Liu, Jinhe Bi et al. — [Evolution Under Fire: Evolving Agent Safety Harnesses with Adaptive Injection Stressors](http://arxiv.org/abs/2611.22583v1)
  <details><summary>📄 Abstract</summary>
  Tool-using language-model agents must act on information from untrusted emails, webpages, and documents. This creates a central security challenge: malicious instructions and legitimate task directives can arrive through the same interaction channel. Existing defenses are largely hand-designed and static, making further improvements dependent on repeated manual redesign. We introduce Evolution Under Fire, a staged framework that couples safety-harness evolution with adaptive stressor evolution. ...
  </details>

- **2026-11-17** — Arunkumar V, Gangadharan G. R., S. Senthilkumar — [ConfGuard: a physics-grounded reference monitor for predictive-maintenance large-language-model agents](http://arxiv.org/abs/2611.22288v1)
  <details><summary>📄 Abstract</summary>
  Large-language-model agents now close the industrial predictive-maintenance loop, reading sensor windows, retrieving procedures and dispatching work orders. Two attack channels meet there: injected text in a retrieved document can hijack the decision, and a bounded sensor perturbation can corrupt the remaining-useful-life estimate behind it. Recent agent defenses police data provenance and tool privilege but cannot tell whether a prognostic quantity is physically plausible. ConfGuard is a refere...
  </details>

- **2026-11-17** — Ashman Mehra — [Think Before You Code: A Benchmark for Testing LLMs on Software Engineering Deliberation](http://arxiv.org/abs/2611.22905v1)
  <details><summary>📄 Abstract</summary>
  Think Before You Code (TBYC) is a benchmark pipeline for studying whether code-focused language models can reason about software issues in ways that resemble human engineering deliberation. The benchmark curates GitHub issue discussions into structured records, extracts human discussion artifacts such as problems, solutions, constraints, rationales, and trade-offs, and then prompts models to generate issue-level "thoughts" using retrieved code context and few-shot examples. It converts model res...
  </details>

- **2026-11-17** — Nazmul Haque, Arnob Protim Roy — [RoadAnnoter: An AI-Assisted Desktop Tool for Semantic Segmentation Annotation of Road-Scene Images](http://arxiv.org/abs/2611.22884v1)
  <details><summary>📄 Abstract</summary>
  Accurate semantic segmentation of road-scene images is essential for road safety research; however, polygon-level annotation remains labor-intensive and limits labelled dataset development. This study presents RoadAnnoter v1.0, an open-source desktop application integrating six human-in-the-loop annotation modes: manual polygon delineation, SAM Prompt, Smart Select, Edge Fill, pretrained semantic segmentation using Cityscapes-trained SegFormer models, and task-specific segmentation using TinySeg...
  </details>

- **2026-11-17** — Thomas A. Conway — [A Discrete Digital Isolator with Shielded Planar Transformer for Gate Driver Applications](http://arxiv.org/abs/2611.22520v1)
  <details><summary>📄 Abstract</summary>
  Galvanically isolated gate drivers are required in many power electronics applications. This paper describes an implementation of a digital isolator using discrete components with a planar coreless PCB signal transformer providing the isolation. The use of an electrostatic shield between the transformer windings is shown to provide sufficient common-mode transient immunity to support IGBT half-bridge drivers, an application subject to a severe dV/dt transient during switching. The design is veri...
  </details>

- **2026-11-17** — Wei Hou, Jingxin Geng, Xin Chen et al. — [LMLineage: Content Lineage and Context Governance for LLM Agents](http://arxiv.org/abs/2611.22511v1)
  <details><summary>📄 Abstract</summary>
  Interpretability for AI agents should not be confined to understanding the model's internal weights. It must also cover the agent's reasoning and decision-making process over multi-source context. We present LMLineage, an out-of-band system that attributes every output sentence of an agent session to its supporting input spans with calibrated confidences, without requiring white-box access to the model or any additional inference passes. On top of the lineage metadata, we build concept-drift mic...
  </details>

- **2026-11-17** — Yu Lu, Lixin Zou, Yangqi Chen et al. — [From Relevance to Utility: Rubric Alignment in Yuanbao Search](http://arxiv.org/abs/2611.22503v1)
  <details><summary>📄 Abstract</summary>
  Agentic search demands that a search engine move beyond per document relevance ranking to assemble document sets optimized for downstream LLM reasoning. Prior work addresses this either by improving individual pipeline stages in isolation or by applying RL based selection on top of relevance trained upstream modules, leaving the full stack unaligned to utility for reasoning. We propose rubric aligned search, a framework that unifies the traditional search pipeline under a single supervision surf...
  </details>

- **2026-11-17** — Alejandro Pelaez, Randal W. Beard — [COAST: Safe Flight Corridor Planner for Fast and Robust Snap Minimized Trajectories](http://arxiv.org/abs/2611.22447v1)
  <details><summary>📄 Abstract</summary>
  Current B-Spline trajectory planners face a critical trade-off: they either sacrifice computational speed to maintain strict Safe Flight Corridor (SFC) guarantees, or they abandon hard safety bounds in favor of soft-constraint penalties to achieve real-time performance. We present COAST (Corridor-Optimized Aerially-Safe Trajectories), a B-Spline based, online trajectory planner capable of formulating snap minimized trajectories with SFC guarantees. COAST divides the problem into two stages: an A...
  </details>

- **2026-11-17** — Deep Shah, Nehal Kathrotia — [Harnesses That Improve Themselves: A Unifying Framework for Self-Improving Agent Harnesses](http://arxiv.org/abs/2611.22299v1)
  <details><summary>📄 Abstract</summary>
  Whether a foundation model succeeds as an autonomous agent depends as much on its runtime software as on its weights. This runtime, the agent harness, manages context and memory, steers multi-turn control, executes tool actions in sandboxes, and verifies work before stopping. Because models differ in how they use tools and how they fail, a static harness tuned for one model or task often stalls, wastes tokens, or regresses on another. This bottleneck has driven a shift from prompt tuning to self...
  </details>

- **2026-11-17** — Arjun Sivaraman, Zhaoheng Li, Alan Shi et al. — [Readie: Low-Latency Code Sandboxes for AI Agents](http://arxiv.org/abs/2611.22171v1)
  <details><summary>📄 Abstract</summary>
  From quantitative research to personal assistance, AI agents act by iteratively generating and executing code. To decouple the agent harness from code execution, many agents offload execution to dedicated systems called code sandboxes. However, existing code sandboxes suffer from slow startup. Whether they rely on custom snapshots or a single fat image, the root cause is the same: it is hard to build a compact, pre-warmed snapshot that can be shared across diverse agent-generated code while cove...
  </details>

- **2026-11-17** — Xingchen AGI Lab,  :, Baotian Hu et al. — [TeleChat to Xing4: Advancing Frontier Agentic Models on Domestic Chips and Frameworks](http://arxiv.org/abs/2611.22115v1)
  <details><summary>📄 Abstract</summary>
  We present Xing 4, a series of large language models that extends the TeleChat lineage through coordinated advances in model architecture and training infrastructure on Ascend. This report describes the design principles and systems engineering behind the series, spanning architecture selection, large-scale pretraining, and reasoning and agentic post-training. We study how sparse activation, attention design, model depth and width, and speculative decoding balance model capacity with computation...
  </details>

- **2026-11-17** — Sara Khosravi, Xiaofei Wen, Majid Sarrafzadeh et al. — [MedGuardBench: A Patient-Oriented Benchmark for Personalized Guardrail Development](http://arxiv.org/abs/2611.22069v1)
  <details><summary>📄 Abstract</summary>
  Safety is personal: the same action can be safe for one person but unsafe for another. Yet current guardrails judge content without considering who is affected. Using medication safety, we introduce \textit{patient-conditioned medication guarding}, which predicts a safety verdict and 17 risk categories from a patient profile and prescription. We release \textbf{MedGuardBench}, a drug-disjoint benchmark of 5{,}001 scenarios across 87 medications. We find that standard guardrails rely on surface c...
  </details>

- **2026-11-17** — Hyunjong Ok, Jaeho Lee — [Weight-Space Programming Doesn't Need Transformers](http://arxiv.org/abs/2611.22055v1)
  <details><summary>📄 Abstract</summary>
  Standard neural architectures such as the Transformer were chosen because they train well with gradient descent and run fast on GPUs. In weight-space programming, a large language model (LLM) writes target weights by hand without gradient-based training, so those reasons no longer apply. Should we keep the Transformer? Given minimal guidance, ten labeled examples, and a sandbox, mainly on multiple-choice questions, we task three frontier LLMs with either generating the weights of a fixed archite...
  </details>

- **2026-11-17** — Tianchi Xu, Yuxuan Zhou, Yuheng Zhang et al. — [Must You See Fakes to Catch Fakes? Language Says What to Look For, Real Images What to Ignore](http://arxiv.org/abs/2611.22650v1)
  <details><summary>📄 Abstract</summary>
  Must a detector see generated images in order to catch them? Detection of AI-generated images has long faced two problems. The cues a detector learns from the few generators in its training set carry traces specific to those generators and transfer poorly to new ones, which limits generalization. The real and generated training images also differ in format and content, so the detector takes these differences as evidence of authenticity, and its decisions change with factors that have nothing to ...
  </details>

- **2026-11-17** — Yuji Yamamoto, Satoshi Matsuura — [From Token Changes to Task Failures: Bit Flips in a Shared KV-Cache Block](http://arxiv.org/abs/2611.22243v1)
  <details><summary>📄 Abstract</summary>
  In LLM serving systems with prefix caching, each KV block of a shared system prompt is held in GPU memory as a single physical copy, which every request with that prompt reads. Our earlier work measured change and showed that one bit flip in such a block changes many later responses without making them visibly degenerate. This paper extends that work by measuring how often the changed responses are wrong. Using software fault injection into vLLM serving Qwen3-8B, we flip the most significant man...
  </details>

- **2026-11-17** — Aviv Yossef, Or Patashnik, Or Zamir — [Distortion-Free Semantic Watermarks for Black-Box Generative Models](http://arxiv.org/abs/2611.23208v1)
  <details><summary>📄 Abstract</summary>
  We present a provably distortion-free semantic watermarking algorithm that requires only black-box sampling access to a generative model and black-box access to a semantic embedding. A watermark is called distortion-free if, averaged over its secret detection key, it leaves the generator's output distribution unchanged; this provides a formal guarantee that watermarking does not reduce output quality. Conventional such watermarks are often brittle to transformations. This is especially problemat...
  </details>

- **2026-11-17** — Igor Shilov, Thomas Fel, Tal Haklay et al. — [Large-scale Neuron Community Discovery Reveals Neuron-Sparse Behaviors in Language Models](http://arxiv.org/abs/2611.23112v1)
  <details><summary>📄 Abstract</summary>
  What reusable units of computation can we discover within a language model's neurons? Prior work has shown that individual forward passes can often be sparsified post-hoc to small groups of neurons, but it has been unclear whether these groups form coherent computational entities reused across inputs. We introduce neuron community discovery, an unsupervised method for finding neuron groups that recur across prompts and are causally necessary and sufficient, within the layers they span, for commo...
  </details>

- **2026-11-17** — Artem Guba, Nikolay Kovalev, Alexey Zharinov et al. — [Hierarchical Control of Antiphase Synchronization in Biomorphic Spiking Neural Architectures for Locomotor Control](http://arxiv.org/abs/2611.22639v1)
  <details><summary>📄 Abstract</summary>
  Central pattern generators (CPGs) provide a biologically inspired foundation for adaptive locomotor control, yet systematically characterizing their dynamic regimes in spiking neural networks remains challenging. This study introduces a framework for identifying and stabilizing antiphase synchronization in a biomorphic spiking CPG model embedded in a closed neuromuscular loop. A composite synchronization metric is developed, integrating phase coherence, amplitude balance, and temporal stability....
  </details>

- **2026-11-17** — Matteo Broccoli, Andrea Cipollone, Antonio Bonaduce et al. — [Improving Eddy Detection from Wide-Swath Altimetry with Multimodal Data-Driven Models](http://arxiv.org/abs/2611.22601v1)
  <details><summary>📄 Abstract</summary>
  Physically-based eddy detection algorithms usually rely on hard-coded thresholds and constraints that make the detected structures sensitive to small variations in the underlying fields. One way to relax such conditions is the use of machine-learning methodologies that transform the full problem into an optimization process. We present a multimodal, multi-task, data-driven eddy detection framework based on a shallow convolutional U-Net, trained to jointly segment eddy structures and reconstruct ...
  </details>

- **2026-11-17** — Irene Gosálvez-White, Roberto Magán-Carrión, Carlota de la Vega-Soriano et al. — [Do LLMs Understand Network Traces? A Comparative Study of Reasoning over Raw and Filtered Traffic Data](http://arxiv.org/abs/2611.22575v1)
  <details><summary>📄 Abstract</summary>
  The effective delivery and monitoring of ICT services rely heavily on network traffic analysis. However, interpreting complex packet captures remains a challenging task that requires substantial technical expertise. Large language models (LLMs) offer promising opportunities to automate network traffic in- vestigation, yet their reliability in packet-level field extraction and flow-level sequence reconstruction remains an open research question. This study proposes a reproducible, question-answer...
  </details>

- **2026-11-17** — Coen van den Elsen, Laurens Geffert — [DARWIN: a Geospatial Foundation Model for Marine Intelligence](http://arxiv.org/abs/2611.22496v1)
  <details><summary>📄 Abstract</summary>
  We present DARWIN, a geospatial foundation model for marine intelligence. Recent Earth-observation foundation models have concentrated on terrestrial domains. The marine realm poses distinct challenges: missingness, multi-modal physical and biogeochemical variables, sparse labels, and dynamics that are transient, multi-scale, and non stationary over time. DARWIN adapts a masked-autoencoder backbone to these properties through missingness-aware encoding, expanded spatial and temporal masking, and...
  </details>

- **2026-11-17** — Dongseok Heo, Junghwan Kim, Bongwon Suh — [Bad Apples in the Kitchen: How LLM Teams Detect, Correct, and Calibrate Against Their Misaligned Members](http://arxiv.org/abs/2611.22342v1)
  <details><summary>📄 Abstract</summary>
  What protects an LLM team when one teammate quietly goes wrong? Most multi-agent LLM work assumes cooperative partners and inspects chat between turns before acting. Real-time embodied cooperation does not allow this pause: chat runs alongside action, so a teammate whose words stay cooperative while behavior diverges can cause damage faster than the team can name what is happening. We study this case by injecting three theory-grounded misaligned agents into a custom four-player Overcooked enviro...
  </details>

- **2026-11-16** — Prashant Shekhar, Dumindu Samaraweera, Caroline Howard — [Watermark Evidence under Open-Weight LLM Modification: Exact Bounds for Low-Rank Output Watermarks](http://arxiv.org/abs/2611.21702v1)
  <details><summary>📄 Abstract</summary>
  Open-weight language models can continue generating after their released weights are modified, while a watermark verifier still scores outputs against the original base and marked models. We study how such modifications change the evidence available to an OpenStamp-style verifier. At each shared prefix, we represent the modification as a residual in the next-token logits. We derive an exact finite-vocabulary lower bound on the expected log-likelihood-ratio evidence under a residual-span constrai...
  </details>

- **2026-11-16** — Alan Subedi, Avhishek Biswas, Apala Pramanik et al. — [SLED: Sensor SLicing from Edge to Datacenter](http://arxiv.org/abs/2611.21937v1)
  <details><summary>📄 Abstract</summary>
  Modern sensing systems generate large volumes of heterogeneous data streams from multiple sensor modalities, increasing reliance on datacenters for computation, artificial intelligence/superintelligence (AI/SI) inference, and AI/SI training. Each sensor stream may have different network and compute requirements depending on its type and data volume. However, current wireless systems typically allocate resources at the device level, leading to contention among co-located sensor streams, where bul...
  </details>

- **2026-11-16** — Tord Johan Eide, Einar Holt — [ARC-2: Continuous Compliance Through Delta Management](http://arxiv.org/abs/2611.21811v1)
  <details><summary>📄 Abstract</summary>
  ARC 1 introduced a three-layer governance architecture for autonomous systems comprising model safety validation, cognitive certification (CRAB), and operational authorization (LEA). However, it did not address how compliance should be maintained after deployment.   This paper introduces Delta Management, a continuous governance framework that measures deviations between a system's current operational state and its certified baseline, defined as a region rather than a fixed point. Compliance is ...
  </details>

- **2026-11-16** — Cléa Chataigner, Mina Arzaghi, Florian Carichon et al. — [Corrupting Ties: Investigating Robustness to Bias Injection Across Multi-Agent Network Topologies](http://arxiv.org/abs/2611.21804v1)
  <details><summary>📄 Abstract</summary>
  AI systems are increasingly deployed in high-stakes decision-making contexts, where interactions among components can introduce fairness risks that remain undetected when auditing components or collective outcomes in isolation. As LLM-based multi-agent systems become more prevalent, understanding how biased information propagates through agent interactions is essential for assessing their fairness. We introduce a controlled bias injection framework that replaces selected agent responses with pre...
  </details>

- **2026-11-16** — Eliza Berman, Rohan Subramanian, Shreya Jha et al. — [Solver to System: LLM Reasoning Across Representations and Execution in Scientific Simulation](http://arxiv.org/abs/2611.21964v1)
  <details><summary>📄 Abstract</summary>
  Simulators based on partial differential equations (PDEs) are widely used to model physical systems, but generating and interpreting PDE solver code with large language models (LLMs) remains challenging. Scientific simulation code is a useful testbed for LLM scientific reasoning because (1) one system can be represented by code, equations, natural language, and numerical trajectories and (2) code can execute successfully while implementing invalid physics. We introduce Solver2System, a dataset o...
  </details>

- **2026-11-16** — Joshua B. Lovell, Sean M. Andrews, Grant M. Kennedy et al. — [Rapid Protoplanetary Disk Evolution and Debris Disk Formation in Taurus-Auriga](http://arxiv.org/abs/2611.21884v1)
  <details><summary>📄 Abstract</summary>
  We present a Submillimeter Array (SMA) 1.3mm (225GHz) continuum emission survey of Young Stellar Objects (YSOs) in the Taurus-Auriga star-forming region, comprising 69 class III and 5 class I/II YSOs with spectral types B9-M3, as part of a total sample of 149 class II and 82 class III YSOs. This represents a complete sample (100%) of class II and III YSOs with spectral types earlier than K3, and a near-complete sample (85%) for spectral types earlier than M2. The survey has a median $3σ$ sensiti...
  </details>

- **2026-11-16** — Zheng-Xin Yong, Benjamin Arnav, Miles Wang et al. — [Chain-of-Thought Controllability Can Reduce Chain-of-Thought Monitorability](http://arxiv.org/abs/2611.21799v1)
  <details><summary>📄 Abstract</summary>
  Chain-of-thought (CoT) monitoring is a promising tool for detecting hidden goals, off-task behavior, and other failures in AI agents. One risk is that models could deliberately shape their reasoning to make it opaque to monitors. We stress-test this risk through persona-control training: supervised fine-tuning on mathematical reasoning traces rewritten in the voices of diverse personas. This induces a broader ability to control CoT, even though training contains no monitor-evasion examples. In c...
  </details>

- **2026-11-16** — Mohammed Fackruddin Tusher, Muhammad Iqbal Hossain — [Replay-Augmented Regularisation for Class-Incremental Network Intrusion Detection: A Three-Dataset Evaluation of EWC and LwF](http://arxiv.org/abs/2611.20498v1)
  <details><summary>📄 Abstract</summary>
  As new attack categories emerge, network intrusion detection models need to be updated; however, when fine-tuned sequentially on new classes, previous classes are forgotten, resulting in catastrophic for- getting. The three public datasets we use are UNSW-NB15, ToN-IoT and CIC-IDS2017, and for these datasets, our class-incremental intrusion detection system is built using a CNN with one-dimensional (1D) archi- tecture trained over nine sequential tasks, each of which introduces one attack catego...
  </details>

- **2026-11-16** — Blas Eugenio Vicco Zarate, Miguel Hernán Vicco — [Mitigating Catastrophic Forgetting with Physics-Indexed Specialist Memory: the Evolutionary Neuroplastic Agent](http://arxiv.org/abs/2611.21598v1)
  <details><summary>📄 Abstract</summary>
  Continual reinforcement learning requires adaptation to changing conditions while preserving performance under previously encountered dynamics. It was investigated whether specialists generated by evolutionary search can provide a reusable memory when combined with environment detection and failure-driven search. The Evolutionary Neuroplastic Agent (ENA) evolves small neural networks without gradients, archives selected policies by detected dynamic regime, and retrieves them through Bayesian pol...
  </details>

- **2026-11-16** — Arunkumar V — [Right Reason, Wrong Advice: Evaluating Recourse in LLM Explanations of Denied Requests](http://arxiv.org/abs/2611.21545v1)
  <details><summary>📄 Abstract</summary>
  Language models increasingly write the explanations people receive when a rule system denies their request. If several rules deny the request independently, an explanation can name a true reason and still leave the person denied after they fix it. We call the missing property recourse validity: changing what the explanation cites, without changing what was asked for, can flip the decision. We compute it exactly, and a hitting-set argument predicts from the policy alone when a correct reason fail...
  </details>

- **2026-11-16** — Jiazheng Zhang, Shouwei Li, Yutian Deng et al. — [Incentive Alignment for Electricity Data Assets in China: A Blockchain-Enabled Contribution-Credit Framework](http://arxiv.org/abs/2611.21533v1)
  <details><summary>📄 Abstract</summary>
  Modern electricity markets increasingly rely on reported operational contributions to allocate incentives, recognise cooperation, and coordinate activities across multiple organisations. However, supporting evidence for many reported contributions becomes available only after subsequent metering, dispatch, settlement, or auditing processes, making it difficult to reward genuine contributions while discouraging strategic over-reporting. Existing approaches largely address data sharing, performanc...
  </details>

- **2026-11-16** — Charles Xiao — [Safe Resemblance, Silent Propagation: Limits of Text-Similarity Guardrails for AI Agent Safety](http://arxiv.org/abs/2611.21520v1)
  <details><summary>📄 Abstract</summary>
  When AI agents relay information to one another, an output can preserve an injected instruction's effect on downstream agents even after its wording changes, yet legitimate quotation and template reuse can produce high textual overlap with the source, so text-similarity guardrails that attempt to flag the former risk conflating these two cases. We test this distinction using DonkeyRail, a public classifier combining BLEU, ROUGE-L, and METEOR features, deployed in a controlled three-agent email r...
  </details>

- **2026-11-16** — Jinzhao Li, Yuan Xu, Jinxuan Wu et al. — [ALIVE: Making Streaming Video Models Interactive](http://arxiv.org/abs/2611.21366v1)
  <details><summary>📄 Abstract</summary>
  Streaming video LLMs can continuously observe the world, yet often handle user requests in isolation. We introduce ALIVE, an interactive streaming video model supporting proactive monitoring, streaming task coordination, and feedback-seeking interaction. We construct ALIVE-SFT-288K and ALIVE-RL-3K for two-stage training. Contrastive supervised fine-tuning teaches when and how to respond, while reinforcement learning with Behavior-Aligned Credit Assignment (BACA) combines trajectory-level and loc...
  </details>

- **2026-11-16** — Paul-Andrei Sava, Alexander Küchler, Daniel Kowatsch et al. — [TRIAGE-CPG: A Cross-Model Study of Budgeted Static Malware Triage with Large Language Models](http://arxiv.org/abs/2611.21331v1)
  <details><summary>📄 Abstract</summary>
  When triaging unknown binaries, security analysts must decide which samples to clear as benign, flag as malicious, or escalate for deeper analysis. Large Language Models (LLMs) could support these decisions by interpreting decompiled code, but a binary can contain hundreds or thousands of functions, making exhaustive LLM analysis impractical. We study how current LLMs behave when static triage is formulated as budgeted evidence acquisition: which functions they inspect and how they trade off ben...
  </details>

- **2026-11-16** — Syed Hafiz Bin Salim Alsree, Stephen Roberts, Stefan Zohren — [Wavelet-Energy-Driven Dynamic Patching for Time Series Forecasting](http://arxiv.org/abs/2611.21319v1)
  <details><summary>📄 Abstract</summary>
  Patch-based transformers tokenise a time series into fixed-size, uniform windows, which commits the model to a single temporal resolution even though real signals are multi-scale. The discrete wavelet transform (DWT) is a natural alternative because it decomposes a signal across scales. A growing body of work makes the wavelet filter learnable, on the assumption that a more flexible wavelet forecasts better. That assumption has rarely been tested in isolation, because a single reported improveme...
  </details>

- **2026-11-16** — Hua Zhang, Min Jiang — [Linglong Agent Service: A Runtime for Centralized Agent Reasoning and Distributed Execution](http://arxiv.org/abs/2611.21129v1)
  <details><summary>📄 Abstract</summary>
  LLM agents can use remote tools and cloud sandboxes, but integrating reasoning, session state, and heterogeneous execution sites remains a runtime design problem. We present Linglong Agent Service (agentsvc), a self-hosted HTTP service and embeddable Python runtime that treats execution site as a configurable dimension alongside model, tools, and context. A parent service retains inference orchestration, tool descriptions, and conversation history; each inference request selects one child enviro...
  </details>

- **2026-11-16** — Fabio Picariello, Salvatore Cipolla, Susanna Bonura et al. — [GRACE: Parallel Best-of-N Multi-Agent Analysis of Closed-Form Questions over Dataframes with Guardrail Selection and Adaptive Retry](http://arxiv.org/abs/2611.20983v1)
  <details><summary>📄 Abstract</summary>
  LLM agents answer closed-form questions over a tabular dataframe by writing and executing Python, almost always as a single rollout: one interpretation, one script, one result, accepted without comparison. The few pipelines that produce several candidates reconcile them by answer-agreement voting, which needs a single comparable scalar and always returns one, even when every candidate is wrong. We present GRACE (Generative, Ranked, Adaptive Code Ensemble), a production-oriented pipeline that ins...
  </details>

- **2026-11-16** — Subham Kundu — [Same Fix, Different Weights: Replicating Weight-Space Programming with Claude](http://arxiv.org/abs/2611.20953v1)
  <details><summary>📄 Abstract</summary>
  Takehi et al. (2026) report that GPT-6 Astra, given the weights of small neural networks as text, can say what they were trained to do, repair them, and write new ones without training. I re-ran the core of that study with Claude Opus 5.5 in ten pre-registered experiments, with untrained-network and permutation controls and hand audits of every sandboxed code cell. Reading was mixed: Claude named 3 of 4 Atari games from policy weights and found the measured copying heads in 15/15 character-LM ru...
  </details>

- **2026-11-16** — Daksh Bathla — [Navital Gym: Rule-Graded Agent Environments for Indian Workflows](http://arxiv.org/abs/2611.20924v1)
  <details><summary>📄 Abstract</summary>
  AI agents are being deployed on Indian workflows such as payments, tax, forms, travel and customer support in Hindi and Hinglish. Public agent evaluations rarely cover these workflows, and many score with another language model. We present Navital Gym, a set of six open environments with 321 public tasks in five task families: trip planning, UPI payments and disputes, GST invoicing and returns, form filling (including a multi-document split) and customer support in Hindi, Hinglish and three expe...
  </details>

- **2026-11-16** — Xue Yang, Haonan Cai, Xinyu Hang et al. — [SciWorldBench: Do Video World Models Really Understand Scientific Experiments?](http://arxiv.org/abs/2611.20899v1)
  <details><summary>📄 Abstract</summary>
  While the ability of video generation models to accurately depict scientific phenomena has received growing attention, determining whether these models genuinely understand the underlying principles remains a critical challenge. Existing benchmarks typically evaluate video samples in isolation, making it difficult to expose models that simply fit superficial visual priors. In scientific experiments, a small change in one condition produces a markedly different outcome even when the rest of the s...
  </details>

- **2026-11-16** — Zheng Wang, Yuang Liu, Sachith Abeywickrama et al. — [From Recursion to Convolution: Parallel Self-Improvement for Multi-Agent Systems](http://arxiv.org/abs/2611.20891v1)
  <details><summary>📄 Abstract</summary>
  Multi-agent self-improvement enables agents to improve through interaction and feedback. However, sequential dependencies across agents and refinement rounds can propagate errors, increase computational costs, and limit parallelism. Moreover, refining individual features or agents in isolation can overlook their dependencies and restrict collective coordination. To address these challenges, we propose ConvRSI, a framework for parallelizing multi-agent self-improvement through convolution. ConvRS...
  </details>

- **2026-11-16** — Tom A. Lamb, Philip H. S. Torr, Tim G. J. Rudner — [Tight PAC-Bayes Generalisation Guarantees for Large Language Model Judges](http://arxiv.org/abs/2611.20818v1)
  <details><summary>📄 Abstract</summary>
  Large language model (LLM) judges are increasingly used to monitor the outputs of LLM-based AI agents, yet formal guarantees on the reliability of these judges remain largely absent, limiting confidence in their use for safety-critical oversight. We consider certifying such a judge and define its risk over safety classifications of prompt--response pairs drawn from a deployed generator. We apply a PAC-Bayes framework to this setting, refining existing compression-based methodology with the use o...
  </details>


### 📂 alignment
*对齐与安全约束 / Alignment & Safety Constraints* — 56 papers

- **2026-11-18** — Amr Elshazly, Jesse Roberts, Rachad Atat et al. — [LLM-Guided Cyber-Physical Attack Path Identification in Smart Grids](http://arxiv.org/abs/2611.24765v1)
  <details><summary>📄 Abstract</summary>
  Identifying high-impact attack paths in cyber-physical power systems is critical for improving grid resilience. Existing methods typically rely on either structural topology analysis or simulation-based cascading-failure models. Topology-based approaches capture connectivity but lack adversarial reasoning, while simulation-driven methods are primarily suited for offline analysis and are less effective for rapid evaluation of evolving attack scenarios. As a result, identifying realistic attack pa...
  </details>

- **2026-11-18** — Jingzhi Bao, Xiaohe Ma, Hong Li et al. — [UltraTex: Aligning Physical Knowledge for High-Fidelity PBR Texture Generation](http://arxiv.org/abs/2611.24941v1)
  <details><summary>📄 Abstract</summary>
  Generating physically based rendering (PBR) texture maps for a 3D mesh from a single reference image is highly ambiguous, as the observed appearance entangles material identity, surface reflectance, and illumination. While current generative methods produce realistic albedo maps, they still struggle to infer accurate metallic and roughness attributes for relighting. We present UltraTex, a cascaded multi-view framework that moves beyond appearance matching by integrating physical knowledge into m...
  </details>

- **2026-11-18** — Priyanka Sinha, Sugam Pandey — [Knowing What You Know: A Trait Theory of Reviewer Value in Human-AI Cognitive Systems](http://arxiv.org/abs/2611.24932v1)
  <details><summary>📄 Abstract</summary>
  When a capable model and a human reviewer cooperate on the same decision, which human still adds value? We argue this is a question about a single cognitive trait, metacognitive calibration: the alignment between a reviewer's behavioral confidence and the actual correctness of their judgments. We develop a trait theory of reviewer value to make it precise. The theory makes five claims: value is governed by calibration rather than by activity, speed, agreement, or tenure; calibration leaves obser...
  </details>

- **2026-11-18** — Zihan Wang, Jianzhe Li, Zhenyi Zhang et al. — [Horizontal Flow Matching for Single-Cell Spatiotemporal Dynamics](http://arxiv.org/abs/2611.24764v1)
  <details><summary>📄 Abstract</summary>
  Learning the spatiotemporal dynamics of cells from spatial transcriptomics requires connecting snapshots of different cells acquired in different coordinate frames. A rotation or translation of a section can appear as cell movement and distort the inferred correspondence. We introduce horizontal flow matching, which learns changes in tissue organization, molecular state, and cell abundance up to shared rigid motion. The dynamics follow a continuity--reaction equation whose action assigns no cost...
  </details>

- **2026-11-18** — William John Atkinson, Paul Saproza — [Hi Gemini, Who Should I Vote For? The Benefits (and Problems) of Using LLMs As Voting Advice Applications](http://arxiv.org/abs/2611.24684v1)
  <details><summary>📄 Abstract</summary>
  Large language models (LLMs) can provide voters information about political issues, party positions, and even advise on which party to vote for. However, no previous study explores how well off-the-shelf LLMs function as voting advice applications (VAAs). In this article, we address this gap by examining how Gemini 3 Flash advises a sample of 6,022 German survey respondents on which party to vote for, based on their policy preferences and priorities alone. In brief, we find that for most respond...
  </details>

- **2026-11-18** — Huu Binh Ta, Alex Morehead, N. Benjamin Erichson et al. — [Choosing the Right Representations: Task-Aware Fusion for Multimodal Materials Language Models](http://arxiv.org/abs/2611.24641v1)
  <details><summary>📄 Abstract</summary>
  Multimodal language models for materials science rely on effective mechanisms for incorporating three-dimensional structural representations. MatterChat addresses this challenge using a large bridge module between a pretrained structural encoder and the LLM, together with a separate contrastive alignment stage. We instead ask whether this bridge can adaptively select and combine representations from multiple structural encoders according to the target property. We find that supervised and genera...
  </details>

- **2026-11-18** — Zhuoqi Hu, Shiwei Li, Haozhao Wang et al. — [Where Should a Diffusion Transformer Meet Its Teacher?](http://arxiv.org/abs/2611.24380v1)
  <details><summary>📄 Abstract</summary>
  Representation Alignment (REPA) significantly accelerates Diffusion Transformer training by guiding intermediate student features with a pretrained visual teacher, yet existing methods typically attach supervision to a single fixed layer. As student representations evolve, however, we find that the most effective layer for alignment varies across training stages. To track this evolving layer suitability online without costly search, we measure gradient compatibility between the flow-matching and...
  </details>

- **2026-11-18** — Argyrios Zafeiriou, Athanasios Kallipolitis, Ilias Maglogiannis — [Transferable Named Sparse Features for Morphology-based Gleason Grading](http://arxiv.org/abs/2611.24363v1)
  <details><summary>📄 Abstract</summary>
  Deep learning systems grade prostate biopsies at the level of pathologists, but most report a grade without the glandular architecture that justifies it. This work presents a grading system built on a sparse code over the tokens of a pathology foundation model. A sparse autoencoder pretrained on biopsies is aligned with multi-reader annotations, so that 69 of its 2048 features are named after Gleason morphologies such as cribriform glands, cords, and comedonecrosis. The same code feeds a grading...
  </details>

- **2026-11-18** — Aniruddh Sikdar, Arya Kishor, Snehashis Dhibar et al. — [CROMPT: Adapting CLIP via Cross-Modal Prompting for Robust Zero-Shot Generalization under Adverse Weather](http://arxiv.org/abs/2611.24284v1)
  <details><summary>📄 Abstract</summary>
  Domain adaptation for semantic segmentation is challenging when target-domain images are unavailable during training. Zero-shot domain adaptation addresses this by adapting models using only textual descriptions of the target domain. However, existing prompt-learning methods are not well suited for ResNet-based CLIP vision backbones or pixel-level cross-modal feature alignment. We propose CROMPT, a prompt-learning framework for zero-shot domain adaptation in semantic segmentation. CROMPT introdu...
  </details>

- **2026-11-18** — YaoYang Liu, ZhuoShi Tang, Haopeng Lai et al. — [Stabilizing Neural-to-Image Retrieval with Frequency-Domain Priors and Adaptive Supervision](http://arxiv.org/abs/2611.24163v1)
  <details><summary>📄 Abstract</summary>
  Visual neural decoding aims to infer perceived visual stimuli from brain activity, offering important insights into human visual cognition while enabling transformative applications in brain computer interfaces and artificial intelligence. Recent advances in pretrained vision-language models have provided a semantically rich representation space for this task. However, reliable alignment between EEG/MEG signals and visual embeddings remains challenging because neural responses are noisy, highly ...
  </details>

- **2026-11-18** — Sayumi Muthukumarana, Roshan Godaliyadda, Parakrama Ekanayake et al. — [Once Upon a Bias: Gender Stereotyping in LLM-Generated Children's Stories](http://arxiv.org/abs/2611.24156v1)
  <details><summary>📄 Abstract</summary>
  Large language models are increasingly used to create stories for children. Since bedtime stories can shape children's perceptions of social roles, this raises concerns about whether LLMs adapt narrative portrayals according to the intended recipient's gender. We conducted a large-scale study to examine gender stereotyping in LLM-generated bedtime stories. Using matched daughter/son prompts and a five-generation design, we analyze 62,873 retained stories from 16 LLMs across 35 country settings a...
  </details>

- **2026-11-18** — Yuhang Huang, Junchao Li, Boyang Ma et al. — [Lost Between Mind, Model Collaboration, and Motion: Understanding and Measuring Cross-Model Action Misalignment in Commercial Robots](http://arxiv.org/abs/2611.24100v1)
  <details><summary>📄 Abstract</summary>
  Embodied robots increasingly rely on large language models (LLMs) to interpret user intent and coordinate with robot-specific action models for physical interaction. This multi-model pipeline creates a critical semantic boundary across mind, model collaboration, and motion: semantic consistency may break between what the large model understands, how the small action model translates that understanding into executable commands, and what physical actions the robot ultimately performs. As a securit...
  </details>

- **2026-11-18** — Paul König, Sascha Marton, Stefan Lüdtke et al. — [VESPA: Verifiable Symbolic Policy Adaptation for Safe Reinforcement Learning](http://arxiv.org/abs/2611.24083v1)
  <details><summary>📄 Abstract</summary>
  Safe reinforcement learning (RL) aims to prevent agents from taking actions that are dangerous or destructive to their environment. This is especially important for safety-critical domains, such as robotics or autonomous driving. Formal verification can be used to prove agent safety through safety constraints. However, in practice, many policies do violate safety constraints, and thus are verified to be unsafe. Since the goal is to obtain a safe policy, we would need to retrain a new policy from...
  </details>

- **2026-11-18** — Anand A. Joshi, Satwik Bathula, Richard M. Leahy — [EEGSync: Unitary Temporal Alignment Method for Naturalistic and Resting-State EEG](http://arxiv.org/abs/2611.24017v1)
  <details><summary>📄 Abstract</summary>
  Electroencephalography (EEG) studies increasingly use naturalistic and resting-state paradigms that lack discrete event timing. These recordings contain structured oscillatory activity but often lack repeated stimulus onsets to define a shared time clock across trials or participants. We introduce EEGSync, a complex-valued unitary Procrustes temporal alignment method for band-limited analytic EEG signals. EEGSync represents each subject as a matrix of complex oscillatory trajectories and solves ...
  </details>

- **2026-11-18** — Baoliang Chen, Lingyu Zhu, Zhiwei Zhong et al. — [FlyVQA: Seeing Video Frame Interpolation Quality through Fly Eyes](http://arxiv.org/abs/2611.24012v1)
  <details><summary>📄 Abstract</summary>
  The ultimate ambition of visual quality assessment is to reproduce the neural computations of human vision and thereby achieve full alignment with human perception. However, the immense complexity of human visual circuitry makes this goal difficult to realize. Recently released fly visual connectomes provide a tractable biological starting point. Despite differences between fly and human vision, the fly's well-characterized motion pathways motivate us to investigate their potential for assessing...
  </details>

- **2026-11-18** — Luosong Guo, Xiang Yang, Chaoyang Li et al. — [Freeforward4d: Annotation-free feed-forward 4d reconstruction of driving scenes](http://arxiv.org/abs/2611.24007v1)
  <details><summary>📄 Abstract</summary>
  Feed-forward 4D reconstruction enables efficient creation of renderable driving scenes for autonomous driving simulation. However, most existing methods rely heavily on dataset-provided cameras, LiDAR depth, or 3D box annotations, limiting their applicability to unannotated driving videos. Pretrained visual models can predict cameras, depth, and object tracks from RGB alone, but their geometry is mutually inconsistent: multi-view predictions come in short windows with independent scales and fram...
  </details>

- **2026-11-18** —  Neha, Mudasir Ganaie — [SIRAZ: Sparse Inter-Layer Residual Aggregation for Zero-Shot Visual Neural Decoding](http://arxiv.org/abs/2611.23991v1)
  <details><summary>📄 Abstract</summary>
  Brain-computer interfaces aim to establish direct communication between neural activity and external systems, making interpretation of brain signals an important problem. In this context, neural visual decoding seeks to infer visual information from neural activity by learning a mapping between brain responses and the corresponding visual stimuli. It investigates how visual information emerges from neural signals and relates to perceptual processing while enabling the reconstruction or retrieval...
  </details>

- **2026-11-18** — Hongxu Chen, Chun Wang, Yanghao Wang et al. — [Dual-Manifold Variational Autoencoders](http://arxiv.org/abs/2611.23964v1)
  <details><summary>📄 Abstract</summary>
  In latent diffusion models, expanding the latent dimension of variational autoencoders (VAEs) is essential to push the upper bound of reconstruction quality. However, without explicit structural constraints, such unregularized expansion easily yields a rugged and ill-conditioned latent manifold, causing generated latents to drift off the manifold during generation (i.e., off-manifold problem). Recent works smooth this manifold by using external foundation models (e.g., DINOv2) as a topological r...
  </details>

- **2026-11-18** — Ananya Sutradhar, Fabien Roger — [Can you make models believe false facts in the prompt?](http://arxiv.org/abs/2611.23938v1)
  <details><summary>📄 Abstract</summary>
  Making LLMs believe false facts is useful for alignment evaluations and for building model organisms. Previous work explored doing so with Synthetic Document Finetuning (SDF). But SDF requires fine-tuning one new model for each set of injected false beliefs. To enable larger scale SDF-powered alignment evaluations, we attempt to produce a single model that believes any fact placed in a <facts> tag in the prompt. To do so, we explore doing prompt-conditioned SDF: fine-tuning a model on synthetic ...
  </details>

- **2026-11-18** — Jiawei Shen, Jie Feng, Junpeng Zhang et al. — [ReflectScene:MLLM-Guided Closed-Loop Diffusion for 3D Indoor Scene Generation](http://arxiv.org/abs/2611.23845v1)
  <details><summary>📄 Abstract</summary>
  Text-conditioned 3D indoor scene generation requires layouts satisfying geometric, functional, and semantic constraints. However, existing diffusion methods rely primarily on static textual conditions, limiting their ability to assess evolving scenes and translate semantic discrepancies into executable object-level corrections. MLLM-based post-hoc refinement provides semantic feedback but remains decoupled from denoising, potentially disrupting scene coherence.We propose ReflectScene, an MLLM-gu...
  </details>

- **2026-11-18** — Shuaidi Wang, Zhuocheng Gong, Xuejie Liu et al. — [Beyond Replacement: Levenshtein Editing for Diffusion Language Models](http://arxiv.org/abs/2611.23750v1)
  <details><summary>📄 Abstract</summary>
  Diffusion language models (DLMs) offer a flexible alternative to autoregressive models, enabling any-order infilling. While most existing decoding methods treat decoded tokens as fixed, some recent models allow previously decoded tokens to be revised only by replacing them with alternative tokens, a paradigm we refer to as replacement-only editing (ROE). Although ROE can correct individual tokens, it is inefficient for sequence shifts caused by missing or extra tokens and struggles when errors o...
  </details>

- **2026-11-18** — Zichen Zhang, Wei Zhai, Xuji Zhang et al. — [ART: Bridging the Embodiment Gap in 3D Human-to-Robot Affordance Transfer](http://arxiv.org/abs/2611.24182v1)
  <details><summary>📄 Abstract</summary>
  3D affordance acts as a critical link between perception and action, providing priors for robotic manipulation. While existing approaches predominantly leverage human priors as direct references, they often overlook that affordance is not an object-intrinsic property but is inherently coupled with the agent's embodiment. Due to the structural and morphological disparities between human hands and robot end-effectors, directly applying human priors causes severe incompatibility for robotic executi...
  </details>

- **2026-11-17** — Siamak Ghodsi, Amjad Seyedi, Sahar Tahmasebi et al. — [FairPGT: Partitioned Graph Transformers for Dual-Level Fair Graph Clustering](http://arxiv.org/abs/2611.23631v1)
  <details><summary>📄 Abstract</summary>
  Clustering on attributed graphs can produce demographically biased clusters, particularly when communities align with protected groups. Graph transformers can amplify this bias through same-group attention, while global attention limits scalability. We propose FairPGT, a partitioned graph transformer for fair graph clustering. FairPGT restricts attention to METIS partitions and connects them through routing tokens, which divides the quadratic cost of attention by the number of partitions. A grap...
  </details>

- **2026-11-17** — Zelong Liu, Hamza Ahmed, Wynn Wingyi Lee et al. — [ORGANIC3D: Grounding 3D CT Vision Language Models in Organ Level Image Text Coupling](http://arxiv.org/abs/2611.23529v1)
  <details><summary>📄 Abstract</summary>
  Vision language models (VLMs) have achieved strong performance in 3D computed tomography (CT) classification, but high accuracy does not reflect whether their predictions rely on the correct anatomical evidence. We introduce ORGANIC3D, a framework for evaluating and improving organ level image text alignment through controlled anatomical interventions. Our benchmark assesses 12 vision encoder checkpoints and 7 generative VLMs using matched patient comparisons, organ erasure, lesion replacement, ...
  </details>

- **2026-11-17** — Xiaosheng Zhao, Rosemary F. G. Wyse, Yuan-Sen Ting et al. — [JEPA for astronomy: multi-survey spectral alignment puts stellar parameters on the leading principal axes](http://arxiv.org/abs/2611.23492v1)
  <details><summary>📄 Abstract</summary>
  Spectra from different surveys carry different systematics and are not calibrated against one another. Multi-survey foundation models for stellar spectra are then built by aligning embeddings of the same star observed across surveys. Most in astronomy follow the recipes established for language and vision, aligning with a contrastive loss that separates every star from the others. However, this does not ensure that the stellar physics is encoded in a form that a simple read-out can recover. Hold...
  </details>

- **2026-11-17** — Gabriel Sarch, Declan Campbell, Nicholas Budny et al. — [Learning Grounded Reasoning from Human Gaze](http://arxiv.org/abs/2611.23209v1)
  <details><summary>📄 Abstract</summary>
  Human visual reasoning is driven by systematic exploration and extraction of task-relevant visual evidence. Human gaze provides a window into this process, making gaze a useful source of guidance for visually-grounded reasoning in vision-language models (VLMs). However, human gaze also includes noise and redundancies that may transfer poorly to VLMs. In this work, we investigate how human gaze data can be effectively leveraged to improve visual reasoning in VLMs, while maintaining alignment with...
  </details>

- **2026-11-17** — Nhi Hoai Doan, Tatsuya Hiraoka, Munachiso Samuel Nwadike et al. — [Polarity Composition Hypothesis: Causal Evidence from Negation in NLI](http://arxiv.org/abs/2611.23185v1)
  <details><summary>📄 Abstract</summary>
  We investigate how language models process negation in natural language inference (NLI). We propose the \textit{Polarity Composition Hypothesis}, a high-level causal model of this computation. Behavioral evaluations show that language-model predictions largely conform to the proposed hypothesis. Using Distributed Alignment Search, we identify causally effective subspaces aligned with the variables in the polarity-composition hypothesis. These representations transfer across negation forms and pa...
  </details>

- **2026-11-17** — Lorenzo Masoero — [Mind the Gap: A Deployed Multi-Agent System for Documentation Maintenance](http://arxiv.org/abs/2611.23142v1)
  <details><summary>📄 Abstract</summary>
  The "AI revolution" has enabled teams across the technology industry to deliver software features at unprecedented velocity. While code evolves faster than ever, customer-facing documentation often struggles to stay up to speed. As users increasingly rely on LLM-based agents that consume documentation as their primary interface, the impact of this documentation gap worsens: stale information propagates and is treated as authoritative. Signals for identifying where documentation has fallen behind...
  </details>

- **2026-11-17** — Markus Dücker, Vaibhav Kumar, Yi Liu et al. — [Verifying Agents in Rubric-Graded Environments](http://arxiv.org/abs/2611.22841v1)
  <details><summary>📄 Abstract</summary>
  As AI agents take on increasingly open-ended and complex tasks, verifying their outputs has proven to be difficult. Rubric-graded agent environments, where a verifier judges multiple natural-language criteria against the deliverables and environment state changes produced by the agent, have emerged as a popular paradigm. We conduct the first systematic study of verifiers for rubric-graded agent environments. First, we create BankerVerifierBench (BVB), a meta-evaluation dataset of 2,464 human-jud...
  </details>

- **2026-11-17** — Zhongling Xu, Hairong Wang — [Practice in Text, Act in Pixels: Correcting Where Perception Fails](http://arxiv.org/abs/2611.22722v1)
  <details><summary>📄 Abstract</summary>
  GUI agents can learn cheaply from a text view of an interface and act on screenshots through a vision-language screen reader. Yet on a simulated mobile platform with a low-cost reader, policies that complete most tasks in text fail on many of the same tasks on screenshots. We ask where a small budget of real screenshots is best spent to close this gap. We find that the reader's misreads are systematic and recur on the same interface elements. Noise matched to the reader's error rates, a natural ...
  </details>

- **2026-11-17** — Edmundo Lopez-Sola, Shamil Chandaria, Ruben Laukkonen — [Worldviews in Large Language Models](http://arxiv.org/abs/2611.22670v1)
  <details><summary>📄 Abstract</summary>
  Large language models (LLMs) are often described in terms of personas and this framing has become central to alignment research. In this paper, we argue that there is a deeper level of description that lies in the agent's worldviews, i.e., its beliefs about what reality is and how it works. Treating LLMs as a population of subjects, we administer two worldview surveys from human psychology to eight models. We show that the models share many key worldview positions. For example, LLMs consistently...
  </details>

- **2026-11-17** — Yunrui Cai, Dingdong Wang, Lingwei Meng et al. — [Beyond Mimicry: Constrained Exploration with GRPO for Joint Multi-Talker ASR and Diarization under Unknown Speaker Counts](http://arxiv.org/abs/2611.22627v1)
  <details><summary>📄 Abstract</summary>
  Joint multi-talker ASR with speaker attribution and timestamps is particularly challenging when the speaker count is unknown and the output must follow a strict structure. We observe that Supervised Fine-Tuning (SFT)-only alignment of SpeechLLMs is brittle under dense overlaps, often leading to burst hallucinations and malformed speaker/timestamp tags. We propose a unified two-stage generative framework: (i) CoT-augmented SFT that infers the global speaker count before transcription, and (ii) GR...
  </details>

- **2026-11-17** — Chen Zhao, Zipeng Ye, Shifeng Bao et al. — [InteractVLA: Turning VLAs into Interactive Tools for Agentic Robotic Manipulation](http://arxiv.org/abs/2611.22584v1)
  <details><summary>📄 Abstract</summary>
  Existing agentic manipulation systems treat pretrained vision-language-action (VLA) policies as opaque, language-only primitives: when a policy call fails under unfamiliar instructions or scene perturbations, the agent cannot steer its behavior and is forced into futile retries or costly manual takeover. We present InteractVLA, a framework that turns pretrained flow-based VLAs into geometrically steerable and inspectable tools through a bidirectional geometric interface with vision-language agen...
  </details>

- **2026-11-17** — Yu Lei, Yi Li, Hongcheng Gao et al. — [Sample-Aligned Decoders for Latent Generative Models](http://arxiv.org/abs/2611.22458v1)
  <details><summary>📄 Abstract</summary>
  Latent generative models synthesize images by decoding generated latents, yet their decoder is trained only to reconstruct encoder latents and never sees the latents it decodes at test time, so the residual errors of the generator are rendered directly into the final image. Existing remedies retrain the generator, add cost at every sampling step, or make the decoder robust to perturbed real latents, assuming that generator errors resemble such perturbations. We find that they do not. Generated l...
  </details>

- **2026-11-17** — Maniformer Real-World Manipulation Team, Che Tsang Calvin, Xingyu Chen et al. — [Hidden Variables Behind Real-Robot Data Quality: Lessons from Hundreds of Thousands of Hours](http://arxiv.org/abs/2611.22388v1)
  <details><summary>📄 Abstract</summary>
  As real-robot data collection scales, collection-system design shapes both operator efficiency and the behaviors learned by robot policies. Workspace limitations, control-interface friction, and latency can introduce pauses, detours, and corrective motions into otherwise successful demonstrations. We investigate these effects across embodiment, teleoperation control, and data consistency, combining a kinematic study of 25 dual-arm robots, controlled teleoperation experiments, and real-robot eval...
  </details>

- **2026-11-17** — Tianqi Luo, Boyan Li, Yuyu Luo — [MoL-SQL: A Controlled Benchmark for Mixture-of-Language Text-to-SQL](http://arxiv.org/abs/2611.22333v1)
  <details><summary>📄 Abstract</summary>
  Text-to-SQL systems are usually built and evaluated under a monolingual assumption, yet in international applications users often query databases stored in a different language. Existing multilingual benchmarks mostly translate only the question without aligning schema and value entities, so they can neither locate the source of an accuracy drop nor rule out translation errors. Hence, we introduce MoL-SQL, a benchmark for mixture-of-language Text-to-SQL that switches the languages of the questio...
  </details>

- **2026-11-17** — Fu Feng, Ruoheng Zhou, Yucheng Xie et al. — [Breaking Visual Conventions: Spectrally Coupled Weight Perturbation for Creative Image Generation](http://arxiv.org/abs/2611.22318v1)
  <details><summary>📄 Abstract</summary>
  Text-to-image (T2I) models often produce high-quality images that follow familiar visual conventions, even in response to open-ended prompts such as ``a creative [CLS]''. Existing methods encourage novelty by exploring semantic conditions or modifying features and guidance during denoising. Pretrained weights offer a complementary source of creative variation, but unstructured perturbations can have little visual effect or degrade image quality. We introduce Coupled Spectral Perturbation (CosPer...
  </details>

- **2026-11-17** — Zhen-Yu Zhang, Jerry Huang, Gang Niu et al. — [Sample-efficient Personalization of Large Language Model Alignment with Multidimensional User Preference Data](http://arxiv.org/abs/2611.22210v1)
  <details><summary>📄 Abstract</summary>
  Preference alignment has become a central tool to align large language models (LLMs) with human values and desired behavior, and its online variant can further advance their capabilities beyond what static data alone offer by repeatedly generating and labeling new responses with human feedback. But costly, time-consuming annotations limit its scalability, making sample efficiency essential, and existing methods typically seek to improve it by expanding coverage of the response space or selecting...
  </details>

- **2026-11-17** — Shuji Shinohara, Daiki Morita, Yoshihiro Nakajima et al. — [Emergence and Collapse of Leader-Follower Flocks through Phantom Targets: Surprise Nullification in Bayesian and Inverse Bayesian Inference](http://arxiv.org/abs/2611.22190v1)
  <details><summary>📄 Abstract</summary>
  In Bayesian and inverse Bayesian (BIB) inference, a large prediction error can trigger surprise nullification, which expands belief and likelihood variances by a common factor, leaving the updated variance ratio the same as in standard Bayesian updating. This can increase belief uncertainty while keeping the learning rate low. In the simulations, three agents used BIB inference to predict one another's positions and moved toward those predictions, repeatedly forming leader-follower flocks that s...
  </details>

- **2026-11-16** — Yufan Wang, Rui Yang, Yi Lin et al. — [DiagTrace: An Interactive Benchmark for Clinical Decision Making](http://arxiv.org/abs/2611.22009v1)
  <details><summary>📄 Abstract</summary>
  Large language models (LLMs) have shown strong performance on medical question answering and diagnostic reasoning benchmarks. However, existing evaluations typically provide all patient information upfront and assess only the final diagnosis or rationale. This setup ignores the need to acquire diagnostic evidence incrementally from incomplete information in real-world diagnosis. To bridge this gap, we introduce DiagTrace, a source-grounded benchmark for evaluating whether LLMs can reconstruct th...
  </details>

- **2026-11-16** — Qile Wang, Abhishek Karwankar, Shukria Muhammadi et al. — [Supporting Researcher Control in AI-Assisted Social Media Analysis: A Mixed-Methods Study of AI4OSN](http://arxiv.org/abs/2611.22006v1)
  <details><summary>📄 Abstract</summary>
  High-quality annotated datasets are critical for advancing computational social science (CSS) research, yet collecting, curating, and analyzing large-scale data from dynamic sources such as online social networks (OSNs) remains a persistent bottleneck. Researchers must also translate substantive questions into queries, relevance criteria, and defensible interpretations. Large language models (LLMs) can assist, but they can also obscure the judgments, potentially reducing researcher oversight and...
  </details>

- **2026-11-16** — Xingzi Xu, Mehmet Saygin Seyfioglu, Karim Bouyarmane — [Margin Dynamics for Large Language Model Alignment](http://arxiv.org/abs/2611.21766v1)
  <details><summary>📄 Abstract</summary>
  Practitioners choose among LLM alignment methods largely by trial and error. We provide a theoretical foundation: each pairwise method defines a vector field on the probability simplex that governs how the model redistributes mass between preferred and dispreferred completions. Projecting onto a single preferred/dispreferred pair reduces this to a one-dimensional margin ODE with a closed-form solution. These solutions reveal that DPO margins grow without bound (logarithmically as $O(\log t)$ in ...
  </details>

- **2026-11-16** — Yue Xu, Xiaoyu Qin, Sihan Zhao et al. — [From Vision to Interaction: Evaluating Dynamic Social Intelligence of VLM Agents in ALIVE-World](http://arxiv.org/abs/2611.20956v1)
  <details><summary>📄 Abstract</summary>
  As AI agents are increasingly deployed in real-world applications and take on social roles, dynamic social intelligence, the ability to continuously perceive multimodal cues, infer latent cognitive states, intervene through embodied actions, and ultimately achieve social goals, has become essential. However, existing evaluations largely fragment social intelligence into text-based abstractions, static reasoning tasks, or embodied simulators that lack social dynamics. These approaches fail to cap...
  </details>

- **2026-11-16** — Abdulaziz Alqahtani, Alwaleed Alharthi, Muzammil Behzad — [Beyond Seeing: Fine-Grained Preference Validation and Severity-Aware Alignment for Mitigating Visual Hallucinations in Vision-Language Models](http://arxiv.org/abs/2611.20478v1)
  <details><summary>📄 Abstract</summary>
  Large vision-language models can produce fluent responses containing objects, attributes, or relations unsupported by the image. We study an implemented alignment pipeline that normalizes released fine-grained hallucination supervision, validates chosen-rejected preference pairs with vision-language judges, repairs rejected chosen responses, and trains LLaVA adapters with standard or severity-aware direct preference optimization. The study uses 16,143 normalized feedback records and 8,386 releas...
  </details>

- **2026-11-16** — Ruixi Yu, Dairu Liu, Xuchuan Chen et al. — [ScaleVLA: Scaling Vision-Language-Action Models to 552 Billion Parameters](http://arxiv.org/abs/2611.21607v1)
  <details><summary>📄 Abstract</summary>
  Frontier Vision-Language Models (VLMs) such as GPT-6 Astra have demonstrated remarkable capabilities in robot control, suggesting that broad pretraining provides knowledge valuable for physical action. Yet most Vision-Language-Action (VLA) policies still rely on much smaller VLM backbones, leaving this potential largely untapped. We ask whether frontier-scale representations can provide a stronger foundation for robot learning. We introduce ScaleVLA, which connects a 552B DeepSeek-V4.1-Flash bac...
  </details>

- **2026-11-16** — Zhuoyang Li, Teng Shi, Jiakai Tang et al. — [Learning to Reason with Predictive Gains for Generative Recommendation](http://arxiv.org/abs/2611.21441v1)
  <details><summary>📄 Abstract</summary>
  Reasoning-enhanced generative recommendation (GR) has attracted increasing attention for leveraging the reasoning capabilities of large language models (LLMs) to improve next-item prediction. However, existing methods primarily optimize reasoning through Group Relative Policy Optimization (GRPO) with rule-based rewards determined by final recommendation performance, which faces two key limitations: (i) unmeasured predictive contributions within reasoning, where the predictive contributions of in...
  </details>

- **2026-11-16** — Hao Sun, Tao Hu, Shixiong Kai et al. — [[CLS] and [EOS] Tokens are not Enough for CLIP-based Class-Incremental Learning](http://arxiv.org/abs/2611.21440v1)
  <details><summary>📄 Abstract</summary>
  Class-Incremental Learning (CIL) aims to empower models to continuously acquire new knowledge while mitigating catastrophic forgetting. With the advent of vision-language models like CLIP, leveraging their cross-modal alignment capabilities to address CIL challenges has emerged as a dominant paradigm. Existing methods leverage CLIP's global representations (i.e., the visual [CLS] token and the textual [EOS] token) for cross-modal alignment. While achieving effective classification, they overlook...
  </details>

- **2026-11-16** — Yili Shen, Kehan Guo, Haomin Zhuang et al. — [Emergent Steering Beyond Endpoint Alignment in Chemical Reaction Models](http://arxiv.org/abs/2611.21423v1)
  <details><summary>📄 Abstract</summary>
  Machine learning models for chemical reaction prediction are usually evaluated by endpoint accuracy, but endpoint correctness alone does not reveal how a model represents chemical transformation or why it fails. We introduce UniRxnAxis, a unified forward-retrosynthesis framework that models both tasks as direction-conditioned endpoint redistribution in a shared latent space. By aligning source states, transformed states, and encoded target endpoints, UniRxnAxis enables directional auditing of le...
  </details>

- **2026-11-16** — Donghyeok Lee, Sangkwon Park, Munyoung Chang et al. — [Classical structural priors improve neural molecular representations in molecule language models](http://arxiv.org/abs/2611.21276v1)
  <details><summary>📄 Abstract</summary>
  Classical molecular similarity is central to chemical information systems, yet molecule-language models trained on paired structure-text data do not necessarily organize molecular embeddings according to graded structural relationships. Here we introduce Structure-Aware Guided Alignment (SAGA), a training-only regularizer that uses Centered Kernel Alignment to align neural molecular representations with fingerprint-based Tanimoto similarity, without adding parameters or requiring fingerprints at...
  </details>

- **2026-11-16** — Ye Xiao, Shesheng Song, Yi Ren et al. — [Beyond Token Stacking: Multi-scale Visual Modulation and Adaptive Fused-feature Calibration for MLLMs](http://arxiv.org/abs/2611.21168v1)
  <details><summary>📄 Abstract</summary>
  Current Multimodal Large Language Models (MLLMs) have advanced rapidly and follow two main paradigms: one involves concatenating visual and textual tokens for input into Large Language Model (LLM), while the other injects visual knowledge into Feed-Forward Networks (FFNs) of the LLM. However, the former introduces a large number of redundant visual tokens, substantially increasing computational overhead. The latter reduces sequence length but removes images from the input stage entirely, which m...
  </details>

- **2026-11-16** — Jing Yi, Cehao Yang, Hualei Zhang et al. — [Conflict-Aware Multi-Teacher On-Policy Distillation in Aligned Action Spaces for Cross-Game Generalization](http://arxiv.org/abs/2611.21094v1)
  <details><summary>📄 Abstract</summary>
  Zero-shot cross-game generalization aims to consolidate accessible source-game experts into a single vision-language model (VLM) that controls unseen games from raw pixels without target-game parameter updates. While multi-teacher on-policy distillation (MOPD) mitigates offline exposure bias and single-game reinforcement learning (RL) overfitting, scaling it to autoregressive VLMs faces two bottlenecks. First, token-to-action misalignment from subword length bias distorts discrete action probabi...
  </details>

- **2026-11-16** — Shiyu Fang, Sheng Zhao, Jiarui Zhang et al. — [CoopDistill: Equilibrium-Guided Multi-Agent Policy Distillation for Cooperative Driving](http://arxiv.org/abs/2611.21069v1)
  <details><summary>📄 Abstract</summary>
  Cooperative driving extends autonomous driving from individual vehicle decisions to joint maneuvers that improve traffic safety and efficiency. Optimization-based methods impose safety constraints but often fix paths to simplify multi-vehicle planning, limiting spatial flexibility. Multi-agent reinforcement learning (MARL) explores alternatives through interaction, but coordinated learning and safe execution remain challenging. Their integration nevertheless faces challenges in exploration effic...
  </details>

- **2026-11-16** — Dongrun Jian, Jie Su, Jun Wang et al. — [Delay-induced anomalous density-polarization relation in chiral active matter](http://arxiv.org/abs/2611.20931v1)
  <details><summary>📄 Abstract</summary>
  Aligning active matter can spontaneously exhibit diverse forms of ordered collective motion, and higher local density is generally expected to enhance local polarization. Meanwhile, delays in agents' responses are widespread in real active systems, raising the question of how delayed alignment affects collective motion and, in particular, whether higher local density still strengthens polar order. Here, using a chiral active particle (CAP) model with delayed alignment, we uncover a counterintuit...
  </details>

- **2026-11-16** — Yeon-Jae Kim, Sangwon Kang, Byung-Kwon Min — [VA-Assembly: View-Aligned Score Guidance for Training-Free 3D Part Assembly](http://arxiv.org/abs/2611.20788v1)
  <details><summary>📄 Abstract</summary>
  Image-to-3D foundation models have improved 3D reconstruction, but typically produce monolithic representations without explicit part-level structure. Part-aware generation and learning-based assembly methods often require part-level supervision, category-specific priors, or paired part-layout training data. We instead consider a practical but underexplored setting in which independently prepared or generated 3D parts have no predefined inter-part relationships, shared coordinate frames, or cons...
  </details>

- **2026-11-16** — Haozhe Zhu, Dan Yuan, Chenghao Gu et al. — [EEGProbe: Do Vision-Language Models Really Understand EEG? A Benchmark for Signal-Grounded EEG Signals Evaluation](http://arxiv.org/abs/2611.20779v1)
  <details><summary>📄 Abstract</summary>
  Vision-language models (VLMs) have shown strong multimodal capabilities across scientific and biomedical domains, yet their ability to understand electroencephalography (EEG) signals remains unclear. We introduce EEGProbe, a signal-grounded benchmark for evaluating whether general-purpose VLMs can extract and reason from minimally processed, channel-wise EEG without task-specific feature engineering or EEG-specific adaptation. EEGProbe contains 620 EEG-centered questions across 13 subtasks and t...
  </details>

- **2026-11-16** — Zifan Zhang, Zhengbo Jiao, Shaobo Wang et al. — [GPRM: Global Perspective Process Reward Model](http://arxiv.org/abs/2611.20755v1)
  <details><summary>📄 Abstract</summary>
  Process Reward Models (PRMs) are widely used for step-level evaluation of multi-step reasoning in large language models, but existing methods are often limited by weak historical dependency modeling and insufficient global awareness. They typically fail to leverage prior step evaluations for coherent judgment and lack visibility into subsequent reasoning, leading to suboptimal assessment of intermediate steps. To address this issue, we propose the Global Perspective Process Reward Model (GPRM), ...
  </details>


### 📂 robustness
*鲁棒性与可靠性 / Robustness & Reliability* — 56 papers

- **2026-11-18** — Beyazit Yalcinkaya, Ethan Pronovost, Maximilian Naumann et al. — [Learning to Interact in Multi-Agent Self-Play for Controllable Autonomous Driving Scenario Generation](http://arxiv.org/abs/2611.24876v1)
  <details><summary>📄 Abstract</summary>
  Large-scale, multi-agent self-play trains robust driving policies effectively in simulation, but controlling these models to generate specific, safety-critical edge cases remains a key challenge. Existing goal-conditioned self-play frameworks rely primarily on static map-location goals and fail to reliably produce complex agent interactions such as aggressive tailgating or adversarial cut-offs. These agent interactions are necessary for rigorous autonomous vehicle (AV) testing. To address this, ...
  </details>

- **2026-11-18** — Yash Jangir, Karan Mirakhor, Renos Zabounidis et al. — [Render the Robot, Generate the World: One Video World Model Across Embodiments](http://arxiv.org/abs/2611.24925v1)
  <details><summary>📄 Abstract</summary>
  Predicting the consequences of an agent's actions requires modeling both the body's motion and the environment's response. Most video world models attempt to learn both from numerical actions, even though geometry and kinematics already specify the intended motion. We introduce Doppel, an embodiment-agnostic video world model conditioned on camera-aligned renderings of future body configurations and numerical action trajectories. By explicitly providing the intended motion, Doppel can focus on p...
  </details>

- **2026-11-18** — Hemen Taukoor, Zhaoxia Wang, Venky Shankararaman — [The Limit Is in the Input, Not the Model: State-Dependent Command Safety in Natural-Language Interfaces to Industrial Controllers](http://arxiv.org/abs/2611.24682v1)
  <details><summary>📄 Abstract</summary>
  Language models judging commands to industrial controllers may not receive machine state, the equipment's current condition. The same command can require opposite safety decisions in different states, so an incorrect answer may reflect missing information rather than poor reasoning. We propose an answerability audit: does the model receive the information needed to decide? The audit records the model's inputs and pairs the same command with two states requiring opposite answers. The paired score...
  </details>

- **2026-11-18** — Rui Li, Liyang He, Zheng Zhang et al. — [Thinking Fast, Anywhere: One System-1 for the Decision Points of Any Agent Workflow](http://arxiv.org/abs/2611.23751v1)
  <details><summary>📄 Abstract</summary>
  Autonomous LLM agents incur substantial cost and latency by invoking a large model (System-2) at every step, even when many intermediate actions choose among a small set of known candidates. Existing dual-system agents offload such decisions to a lightweight System-1 model, but rely on workflow-specific hooks authored per environment. We present AnyS1, a framework that turns human-authored procedural skills, whose instructions naturally specify where choices arise and which options apply, into a...
  </details>

- **2026-11-18** — Xingyu Zhao — [Reliability is a user-specific property of large language models](http://arxiv.org/abs/2611.23732v1)
  <details><summary>📄 Abstract</summary>
  Public benchmarks support comparisons of large language model (LLM) capabilities, yet users can experience the same highly ranked model differently. Drawing on traditional software reliability, we argue that the reliability of an LLM service should be assessed for specified users and conditions of use. This requires more than a capability score: evaluation evidence must support a claim about failure during future operation. We distinguish testing to discover faults from testing to assess reliabi...
  </details>

- **2026-11-18** — Wenhao Li, Zhongyi Han, Yuhao Wei et al. — [Towards Pose-Robust Few-Shot Vision-Language-Action Models](http://arxiv.org/abs/2611.24360v1)
  <details><summary>📄 Abstract</summary>
  Fine-tuning a vision-language-action (VLA) model on a few dozen demonstrations is the standard way to put a manipulation policy on a robot, yet the resulting policy silently assumes that the camera and the robot base stay exactly where they were during data collection: a bumped tripod or a base re-docked a few centimetres away makes it reach for the wrong place. We show that both failures are one phenomenon, a change of the camera-to-base extrinsic that the policy has memorised, and that the rob...
  </details>

- **2026-11-18** — Artur Kuramshin, Charlotte Cloutier, Michael Przystupa et al. — [Finetuning VLAs for Dexterous Manipulation: The Right Checkpoint Is All You Need](http://arxiv.org/abs/2611.23676v1)
  <details><summary>📄 Abstract</summary>
  Vision-Language-Action models have demonstrated strong manipulation capabilities. A limitation of VLA models is that most manipulation datasets focus on parallel-jaw gripper systems, making transfer to multi-finger hands challenging, particularly as teleoperation datasets are harder to collect with multi-fingered robots. In this work, we study how to best adapt VLAs to dexterous hands by pairing supervised fine-tuning (SFT) with diffusion-steering reinforcement learning (DSRL). Using $π_{0.5}$ a...
  </details>

- **2026-11-18** — Jiahao You, Ziye Jia, Chao Dong et al. — [Cooperative UAV and Ground Station for Robust MEC of Dynamic Aquatic IoT: A Generative AI-Enhanced Approach](http://arxiv.org/abs/2611.24466v1)
  <details><summary>📄 Abstract</summary>
  The increasing aquatic Internet of Things (AIoTs) require computational support and coverage in applications such as maritime search and rescue. Unmanned aerial vehicles (UAVs) can offer low-cost, flexible aerial services, and ground stations (GSs) can provide powerful supports, which can cooperate to help the AIoTs in complex scenarios. However, the collaboration between UAVs and GSs for AIoTs faces challenges of task uncertainties, AIoTs trajectory uncertainties, heterogeneities, and limited c...
  </details>

- **2026-11-18** — Zihang Wang, Wenkai Zhu, Lingdong Kong et al. — [One Affinity, Two Axes: Bidirectional Slot Attention for Iterative Aggregation across the Structure--Detail Spectrum in Visual Retrieval](http://arxiv.org/abs/2611.24371v1)
  <details><summary>📄 Abstract</summary>
  Aggregating dense patch tokens into compact and discriminative global descriptors is central to visual retrieval. Although foundation models provide rich local features, existing aggregation heads still rely on single-pass mappings and lack an explicit mechanism to coordinate structural and fine-grained cues. Therefore, we propose Bidirectional Slot Attention (BiSA), which reformulates aggregation as an iterative coupled system. Cross-Axis Consensus (CAC) progressively refines learnable slots by...
  </details>

- **2026-11-18** — Aditya Gandhamal, Aniruddh Sikdar, Arya Kishor et al. — [Pixel2Perspective: A Benchmark for Multi-Modal and Multi-View Generalization in Vision-Language Models](http://arxiv.org/abs/2611.24327v1)
  <details><summary>📄 Abstract</summary>
  Embodied AI systems, such as drones and autonomous vehicles, improve navigation by enhancing perception in environments containing unseen objects. While Visual Language Models (VLMs) offer strong image understanding, their real-world application is underexplored. For effective deployment, open-vocabulary semantic segmentation (OVSS) models, leveraging models like CLIP to assign pixel-level labels from text, must be robust to outdoor conditions, adverse weather, and varying viewpoints. Despite th...
  </details>

- **2026-11-18** — Jun Wang, Fengpeng Li, Wei Han et al. — [Benchmarking Reasoning Reliability,Prior_Evidence Contrast,and Spectral Discrimination in Remote-Sensing Geological Image Interpretation](http://arxiv.org/abs/2611.24068v1)
  <details><summary>📄 Abstract</summary>
  Reliable lithology interpretation requires accurate geological recognition and reasoning grounded in visual evidence. Although Multimodal Large Language Models show promise in remote sensing, their reliability in geological interpretation remains unclear. We introduce HyGeoBench, a diagnostic benchmark of 10,000 questions based on hyperspectral imagery across three dimensions: reasoning reliability, prior_evidence contrast, and spectral discrimination. It covers ten task types, with both multipl...
  </details>

- **2026-11-18** — Dipan Bartaula, Anuj Shrestha, Ankit Belbase et al. — [CURVTON-205K: A Mask-Free Difficulty-Stratified Synthetic Dataset for Robust and Scalable Virtual Try-On](http://arxiv.org/abs/2611.24042v1)
  <details><summary>📄 Abstract</summary>
  Recent advances in 2D virtual try-on (VTON) have largely focused on architectural innovation, yet robust performance in diverse real-world conditions remains challenging. We argue that failure modes in VTON, such as inaccurate occlusion handling, unconstrained poses, and poor coverage of under-represented garments and appearance factors, are tightly coupled to dataset design choices and long-tail data regimes. We present a scalable data generation pipeline that coordinates specialized editing an...
  </details>

- **2026-11-18** — Miaomiao Wei, Huaiyuan Chen, Xinnan Shao et al. — [Convolution-Augmented Transformer for Robust Blind CFO Estimation in LEO Satellite Communication System](http://arxiv.org/abs/2611.23987v1)
  <details><summary>📄 Abstract</summary>
  Low Earth Orbit (LEO) satellite communications are essential for achieving ubiquitous global connectivity. However, the high mobility of LEO satellites induces massive Doppler shifts and fast time-varying fading, severely impairing signal synchronization. Accurate Carrier Frequency Offset (CFO) estimation is critical for receiver synchronization. Nevertheless, conventional estimators and deep learning approaches often degrade significantly under highly dynamic, low-SNR conditions. To address the...
  </details>

- **2026-11-18** — Hamza Ruzayqat, David M. Bortz, Vanja Dukić — [WAIVES: Weak-form Asymptotically-unbiased Instrumental-Variable Estimation for SDEs](http://arxiv.org/abs/2611.23951v1)
  <details><summary>📄 Abstract</summary>
  Weak-form methods have transformed inference for deterministic dynamical systems. By integrating the governing equations against smooth, compactly supported test functions, they trade noise-amplifying differentiation for noise-attenuating integration, yielding fast and robust estimates. Extending this idea to stochastic differential equations (SDEs) has proven harder, and a consistent single-trajectory formulation has remained out of reach. Applied naively in the time domain, the weak form makes...
  </details>

- **2026-11-18** — Zhe Dong, Fang Qin — [Evaluating invariance training with certified answer-changing controls in neural graph algorithms](http://arxiv.org/abs/2611.23907v1)
  <details><summary>📄 Abstract</summary>
  Invariance training aims to make neural algorithmic reasoners robust to answer-preserving input changes and is judged by accuracy and by how rarely such edits change predictions. We ask whether this evaluation detects lost sensitivity to answer-changing edits on minimum spanning trees of synthetic graphs, where both directions can be certified. Attaching a subgraph through one bridge provably preserves every original label. Attaching it through two edges, oracle-selected to change a label, and l...
  </details>

- **2026-11-18** — Siddique Latif, Moid Sandu, Farrukh Pervez et al. — [Great Listeners, Poor Decision-Makers: Rethinking Agentic Audio AI](http://arxiv.org/abs/2611.23847v1)
  <details><summary>📄 Abstract</summary>
  Audio artificial intelligence (AI) now recognizes speech, sounds, and music remarkably well, yet voice agents still act when they should not: they execute commands addressed to others, act on misheard content, and commit before the user finishes speaking. This position article argues that the bottleneck in agentic audio AI has shifted from recognition to decision-making. We propose a reference architecture with an explicit decision layer, separate from perception and reasoning, that chooses whet...
  </details>

- **2026-11-18** — Gaoxiang Linghu, Haonan Zhou, Xuanhe Liu et al. — [GaussLearner: 3D Gaussian Primitives as Self-Regulating Continual Learners](http://arxiv.org/abs/2611.23736v1)
  <details><summary>📄 Abstract</summary>
  Continual learning of 3D Gaussian fields aims to maintain faithful reconstructions of the evolving world. However, directly fine-tuning an existing Gaussian field on new observations can cause catastrophic forgetting of previously reconstructed content. To address this challenge, existing methods employ selective local optimization, replay, or parameter regularization, yet still struggle to balance adaptation to scene changes with preservation of still-valid content. Our key insight is to view 3...
  </details>

- **2026-11-17** — Mohammed Gharib, Sam Burns, Martin Zizi — [A-Tag: Cryptographic File Tagging with Enforced Live Human Presence](http://arxiv.org/abs/2611.23602v1)
  <details><summary>📄 Abstract</summary>
  The increasing autonomy of software agents and the proliferation of AI-generated content have weakened the reliability of digital actions as evidence of human involvement. Existing mechanisms, such as digital signatures and authentication protocols, verify identity and integrity, but do not establish whether a live human was present at the time an action was performed. In this paper, we introduce A-Tag, a system for verifiable human-in-the-loop tagging of digital artifacts. A-Tag cryptographical...
  </details>

- **2026-11-17** — Kaiwen Shi, Zheyuan Zhang, Changzhi Liu et al. — [Receiver-Conditioned Clarification for Multi-Agent Food Assistance](http://arxiv.org/abs/2611.23572v1)
  <details><summary>📄 Abstract</summary>
  Food insecurity creates a pressing need for guidance that helps households find usable food resources and assess food choices in light of their circumstances. Such guidance must connect eligibility requirements, practical access constraints, and dietary needs rather than return isolated listings or generic nutritional advice. Multi-agent food assistants can coordinate these tasks, with uncertainty indicating when clarification or verification is needed before a recommendation. However, uncertain...
  </details>

- **2026-11-17** — Mahvash Jebeli, Mohammad Eslami, Nazlee Zebardast et al. — [Beyond Accuracy: Benchmarking Uncertainty Quantification in Retinal Disease Screening](http://arxiv.org/abs/2611.23344v1)
  <details><summary>📄 Abstract</summary>
  Reliable uncertainty quantification (UQ) is essential for evaluating retinal AI systems beyond classification accuracy, yet it remains unclear whether existing UQ strategies generalize across diseases, model architectures, and reliability criteria. We introduce a large-scale, multi-disease benchmark comprising over $242,000$ fundus photographs from $32$ datasets covering diabetic retinopathy, age-related macular degeneration, and glaucoma. We evaluate six representative UQ strategies across thre...
  </details>

- **2026-11-17** — Haofan Wu, Le Zhang — [MedHarness: A Unified Budgeted Runtime for Reliable Medical Imaging Agents](http://arxiv.org/abs/2611.23501v1)
  <details><summary>📄 Abstract</summary>
  Medical imaging agents already return answers on heterogeneous imaging surfaces, yet deployment still faces a limited verification budget where each wrong accept can harm clinical trust. When a thin check and a deeper evidence pass disagree on the same case, deciding when to stop, open more evidence, repair, or reject without a shared controller remains ill-posed. Tool-using workflows often lock a surface-specific evidence order per dataset, or a private always-open full-depth verification path;...
  </details>

- **2026-11-17** — Jiarui Guo, Saining Zhang, Jiaying Wan et al. — [RFW-S: Everyday Deformable Objects with Independent Simulation Verification](http://arxiv.org/abs/2611.23056v2)
  <details><summary>📄 Abstract</summary>
  Large-scale robotic simulation requires diverse deformable objects with executable physical properties and realistic interaction behaviors. However, existing 3D asset collections primarily emphasize visual diversity, while scalable physical construction and verification remain challenging. We introduce RFW-S, a large-scale dataset of 83,365 simulation-verified assets spanning 485 everyday categories across five structural families: soft solids, cloth sheets, shells, garments, and bags. We develo...
  </details>

- **2026-11-17** — Ting-Hsuan Chen, Siheng Zhao, Han Jiang et al. — [Heave-Ho: Decentralized Long-Horizon Multi-Humanoid Collaboration](http://arxiv.org/abs/2611.22275v2)
  <details><summary>📄 Abstract</summary>
  Collaboration promises to extend humanoid capabilities beyond what individual robots can achieve. However, realizing this potential requires coordinated whole-body interactions, coherent long-horizon planning, and precise synchronization across robots. We introduce Heave-Ho, a decentralized framework for long-horizon collaborative multi-humanoid loco-manipulation. At the low level, we develop a multi-agent post-training framework that adapts a humanoid foundation tracking model to physically cou...
  </details>

- **2026-11-17** — Sijia Zhong, Tamir Yirga, Yijia Ma et al. — [Dreaming Up Authors: Factual Prevalence and LLM Hallucinations in Academic Authorship Attribution](http://arxiv.org/abs/2611.23530v1)
  <details><summary>📄 Abstract</summary>
  Large Language Models (LLMs) are widely used for question answering but are prone to hallucinations, yet the underlying causes, particularly the role of factual prevalence in training data, remain underexplored. In this work, we study this through academic authorship attribution, hypothesizing that hallucinations are more likely for less prevalent papers. Using citation count as a proxy for factual prevalence, we curate a dataset of 1.92 million papers across eight scientific disciplines with st...
  </details>

- **2026-11-17** — Amrit Lal Singh, Smarak Kanjilal — [RageVLA: Augmentation-Trained Perception and Action for State-of-the-Art Robustness on LIBERO](http://arxiv.org/abs/2611.23517v1)
  <details><summary>📄 Abstract</summary>
  Vision-language-action (VLA) models look saturated on LIBERO, yet most of them fall apart on LIBERO-PRO as soon as an object moves or the instruction asks for something new. We argue that what is missing is not scale but decoupling.   In these policies, what to do is tied to where things were during training, to the scene around them and to the wording of the instruction. We cut these ties in two places. In the data, LIBERO demonstrations are re-arranged by general rules: every object and fixtur...
  </details>

- **2026-11-17** — Søren Taverniers, Eric Darve, Hamdi A. Tchelepi — [Reliability by Architecture: Agentic Workflows for Validated Multi-Physics Simulation from Natural Language](http://arxiv.org/abs/2611.23473v1)
  <details><summary>📄 Abstract</summary>
  Preparing, executing, and validating strongly coupled multi-physics simulations require expert time. Agentic workflows use large language models (LLMs) to coordinate them from natural-language descriptions, but reliability requires checks of physical consistency and fidelity to the problem description. Our agentic harness implements explicit task allocation: LLMs interpret user requests and simulator diagnostics, generate input components not covered by predefined construction rules, and propose...
  </details>

- **2026-11-17** — Deepak Waghmare, Shaad Sufi — [Can You Undo It? Reversibility Classes for AI Agent Actions](http://arxiv.org/abs/2611.22075v1)
  <details><summary>📄 Abstract</summary>
  Tool-using AI agents change files, databases, access rights and public information, yet permission to call a tool does not establish whether a mistake can be undone. We present Reversibility Classes, a declared five-level vocabulary with argument-sensitive rules, conservative defaults and an explicit prior-state capture contract. The pinned implementation and evidence-linked registry cover 536 tools across 20 MCP servers. All 738 rule-case checks conform to declared expectations, while native an...
  </details>

- **2026-11-17** — Bernd J. Kröger — [From syllable representation via gesture generation to articulation: A spiking neural model](http://arxiv.org/abs/2611.22499v1)
  <details><summary>📄 Abstract</summary>
  Speech production requires a transformation from phonological representations into coordinated vocal-tract movements. This paper presents a spiking neural sensorimotor model within the Neural Engineering Framework and Semantic Pointer Architecture. Each syllable occurrence has a neural oscillator whose evolving phase coordinates its gestures and initiates the next syllable. Phase-dependent commands recruit separate neural populations for vocalic, oral-constriction, velopharyngeal, and glottal ac...
  </details>

- **2026-11-17** — Himanshu Mishra — [The Fragility of Reasoning-Importance Attribution for Pruning Language Models](http://arxiv.org/abs/2611.22234v1)
  <details><summary>📄 Abstract</summary>
  Attribution-guided pruning scores components by their causal contribution and protects the important ones, and it is increasingly applied to compress reasoning language models without destroying their chain of thought. Its reliability rests on an unexamined assumption: that reasoning importance can be faithfully measured. Across four small reasoning models, we show this measurement is fragile in three ways, each of which changes pruning decisions. First, scoring final-answer tokens, the natural ...
  </details>

- **2026-11-17** — Zihao Han, Philippe De Wilde — [RetiDual-Select: Reliability-Aware Specialist-Generalist Routing for Retinal OCT under Image-Quality Shift](http://arxiv.org/abs/2611.22117v1)
  <details><summary>📄 Abstract</summary>
  Adaptive fusion can repair a static ensemble's errors, but can also overturn correct decisions. RetiDual-Select combines retinal specialist RETFound with the image encoder of the medical vision-language model MedSigLIP, separating candidate fusion, routing safety and predictive review. Calibrated product-of-experts (PoE) fusion is the static reference, a small gate proposes an alternative for each image, a validation-frozen harm guard decides whether that candidate may replace the reference, and...
  </details>

- **2026-11-17** — Florian Gunsilius, David Van Dijcke, Kaspar Wüthrich — [Inference after coding agents](http://arxiv.org/abs/2611.23174v1)
  <details><summary>📄 Abstract</summary>
  Empirical research is changing rapidly as AI coding agents are becoming increasingly proficient in every step of it, from writing code to manipulating data. We argue that while the potential of coding agents for science is vast, their use in hypothesis testing poses a substantial threat to classical inference, as these agents enable a supercharged form of selective inference. In particular, we argue that coding agents carrying out empirical research introduce a new type of post-selection inferen...
  </details>

- **2026-11-17** — Jiarui Guo, Saining Zhang, Jiaying Wan et al. — [RFW-S: Everyday Deformable Objects with Independent Simulation Verification](http://arxiv.org/abs/2611.23056v1)
  <details><summary>📄 Abstract</summary>
  Large-scale robotic simulation requires diverse deformable objects with executable physical properties and realistic interaction behaviors. However, existing 3D asset collections primarily emphasize visual diversity, while scalable physical construction and verification remain challenging. We introduce RFW-S, a large-scale dataset of 83,365 simulation-verified assets spanning 485 everyday categories across five structural families: soft solids, cloth sheets, shells, garments, and bags. We develo...
  </details>

- **2026-11-17** — Rotem Atari, Stav Ashur, Avishai Sintov — [Physics-Informed Tactile-based Shape Estimation of Deformable Linear Objects](http://arxiv.org/abs/2611.22990v1)
  <details><summary>📄 Abstract</summary>
  Accurate shape estimation of Deformable Linear Objects (DLOs) is a fundamental challenge in robotic manipulation, often hindered by visual occlusions and the high-dimensional configuration space of flexible materials. While Force/Torque (F/T) and vision-centric methods have been proposed, they frequently struggle with grasp-site ambiguities and environmental interference. In this letter, we investigate the hypothesis that global shape estimation can be achieved through tactile sensing and propri...
  </details>

- **2026-11-17** — Ting-Hsuan Chen, Siheng Zhao, Han Jiang et al. — [Heave-Ho: Decentralized Long-Horizon Multi-Humanoid Collaboration](http://arxiv.org/abs/2611.22275v1)
  <details><summary>📄 Abstract</summary>
  Collaboration promises to extend humanoid capabilities beyond what individual robots can achieve. However, realizing this potential requires coordinated whole-body interactions, coherent long-horizon planning, and precise synchronization across robots. We introduce Heave-Ho, a decentralized framework for long-horizon collaborative multi-humanoid loco-manipulation. At the low level, we develop a multi-agent post-training framework that adapts a humanoid foundation tracking model to physically cou...
  </details>

- **2026-11-17** — Aritra Das, Francesco Cagnetta, Darshil Doshi et al. — [What's in a Tree ? Hierarchical $n$-gram models as controlled approximators of language](http://arxiv.org/abs/2611.23093v1)
  <details><summary>📄 Abstract</summary>
  Hierarchical models have been proposed as synthetic settings for studying language. However, their relevance to realistic language corpora remains underexplored. In this work, we introduce tree-grams, autoregressive generative $n$-gram models that build the conditional probability tensor $p(x_n \mid x_{1:n-1})$ through a hierarchical composition of order-2 and order-3 tensors. $n$ controls the maximal context window, whereas a rank hyperparameter $d$ controls model capacity, yielding an interpre...
  </details>

- **2026-11-17** — Antonio Manjavacas, David Suárez-Caro, Alejandro Campoy-Nieves et al. — [Deep Reinforcement Learning for Heat Pump and Underfloor Heating Control: An End-to-End Case Study](http://arxiv.org/abs/2611.23063v1)
  <details><summary>📄 Abstract</summary>
  Efficient control of underfloor heating (UFH) systems coupled with heat pumps (HPs) is challenging due to the high thermal inertia of buildings and the slow dynamic response of UFH systems. Deep Reinforcement Learning (DRL) offers a data-driven control approach capable of simultaneously optimizing energy consumption and thermal comfort. However, the application of DRL-based controllers in occupied buildings under real operating conditions remains limited. This work presents and end-to-end case s...
  </details>

- **2026-11-17** — Haoyang Liu, Kecheng Liang, Xinyu Li et al. — [PhysScope: Agentic Multimodal Physics Reasoning with Grounded Visual Memory](http://arxiv.org/abs/2611.23010v1)
  <details><summary>📄 Abstract</summary>
  Vision-language models (VLMs) can correctly interpret physics diagrams yet apply constraints outside the states or conditions in which they hold, causing premise errors to propagate through subsequent calculations. We introduce PhysScope, an inference-time visual harness that supports self-correction of these scope mismatches without updating model weights. PhysScope enables the model to link physical scopes directly to its visual observations and explicitly constructs derived views to support r...
  </details>

- **2026-11-17** — Hongyang Zhang, Boyuan Deng, Siyuan Feng et al. — [When Do Typed Decision Models Work in Transportation? Evidence from Travel Choice and Traffic Signal Control](http://arxiv.org/abs/2611.22926v1)
  <details><summary>📄 Abstract</summary>
  Typed decision models combine natural-language understanding with a structured interface that returns a selected action and an option-level probability distribution without generating lengthy textual responses. Their low inference cost and response latency make them attractive for transportation problems with predefined alternatives. This paper investigates their effectiveness, robustness, and efficiency in two representative transportation tasks: individual travel-mode choice prediction and seq...
  </details>

- **2026-11-17** — Hao Lu, Weixing Zhu, Ruiyang Li — [Contract-Explicit Evaluation: From Auditing Learned Readers to Scoped Certificates](http://arxiv.org/abs/2611.22665v1)
  <details><summary>📄 Abstract</summary>
  Evaluation readings of document-level relation extraction (DocRE) systems depend jointly on the model and the evaluation contract: gold version, scoring function, threshold. Rankings reverse across contracts, yet no existing method determines which comparisons survive the reversal. We address this gap with contract-explicit evaluation: a preregistered five-step protocol (Declare, Measure, Scope, Certify, Hedge), operationalizing the classical concordance decomposition of Kendall's rank correlati...
  </details>

- **2026-11-17** — Liuyi Xu, Yun Guo, Shusheng Li et al. — [OmniTongue: A Comprehensive MLLM Benchmark for Automated Tongue Diagnosis in Traditional Chinese Medicine](http://arxiv.org/abs/2611.22652v1)
  <details><summary>📄 Abstract</summary>
  Multimodal Large Language Models (MLLMs) have excelled in Western medical imaging, yet their potential in Traditional Chinese Medicine (TCM) tongue diagnosis remains systematically unevaluated. Tongue diagnosis requires sophisticated global and local perception, serving as a rigorous touchstone for assessing the visual understanding depth of MLLMs. However, existing datasets are limited by single dimensions, coarse granularity, and ambiguous labels, hindering the evaluation of authentic clinical...
  </details>

- **2026-11-17** — Weishao Tang, Mingcheng Lei, Yufei Zhang — [Residual-Guided Multi-Step Conditional Generation for Fast Airfoil Flow Field Prediction](http://arxiv.org/abs/2611.22629v1)
  <details><summary>📄 Abstract</summary>
  Deep-learning surrogate models for aerodynamic flow prediction are efficient within the training distribution, but their accuracy often degrades sharply in out-of-distribution (OOD) scenarios. To improve OOD robustness for airfoil flow-field inference, this study proposes a residual-guided sequential inference framework to correct the unreliable local flow field. The framework consists of three Transformer-based components: a Flow Initializer for direct flow prediction, a Residual-based Correcto...
  </details>

- **2026-11-17** — Jiachun Li, Zhuoran Jin, Kang Liu et al. — [From Perception to Simulation: Unveiling and Empowering Mental Spatial Dynamics in MLLMs](http://arxiv.org/abs/2611.22541v1)
  <details><summary>📄 Abstract</summary>
  Spatial reasoning is a fundamental component of world understanding for Multimodal Large Language Models (MLLMs). While existing research has advanced the perception of spatial relations in static scenes, the domain of dynamic spatial simulation remains relatively unexplored. To bridge this gap, we introduce MentalGrid, a benchmark focused on spatial reasoning tasks that require models to simulate evolving spatial states without intermediate visual feedback. Extensive evaluation on our benchmark...
  </details>

- **2026-11-17** — Teng Lin, Nan Tang — [MM-ReportBench: A Comprehensive Benchmark for Multimodal Report Generation from Tables](http://arxiv.org/abs/2611.22514v1)
  <details><summary>📄 Abstract</summary>
  The ability to generate multimodal reports integrating fluent narratives with faithful visualizations from tabular data, has become a cornerstone capability for modern vision-language models in practical domains such as finance, healthcare, and policy making. However, existing benchmarks are limited by single-modality focus, simplistic metrics, novelty evaluation, and visualization quality. We address these limitations with MM-ReportBench, a multimodal report evaluation benchmark covering 386 ta...
  </details>

- **2026-11-17** — Mehul Arora, Dhruv Agarwal, Ambuj Agrawal — [CoBoVLA: Decoupling Language from Action with Discrete Codes for Robust and Interpretable Robot Manipulation](http://arxiv.org/abs/2611.22395v1)
  <details><summary>📄 Abstract</summary>
  Vision-Language-Action (VLA) models achieve high success rates on the LIBERO benchmark but remain sensitive to paraphrasing. Existing VLAs ranging from 0.6B to 7.5B parameters experience a 22-52 point performance drop on LIBERO-Para while SmolVLA exhibits an even larger decline, from 83\% to 8\%. Because most VLAs jointly learn language understanding and action generation, it is difficult to determine whether a failure originates from misunderstanding an instruction or executing it incorrectly. ...
  </details>

- **2026-11-16** — Xinyu Zhang, Ziqing Yang, Michael Backes et al. — [PersonaHate: A Scalable Persona-Based Data Synthesis Pipeline for Hate Speech Analysis](http://arxiv.org/abs/2611.21951v1)
  <details><summary>📄 Abstract</summary>
  Hate speech remains a persistent and evolving threat on online platforms. The widespread use of large language models (LLMs) further intensifies this problem by making hateful content easier and cheaper to generate at scale. Although stronger hate speech detectors continue to be proposed, their performance remains uneven across target identity groups and different forms of hateful expression, partly because existing training data provides only limited coverage of these cases. Thus, we introduce ...
  </details>

- **2026-11-16** — Qiangchang Wang, Chong Xiao, Xiaokun Bai et al. — [Words Speak Louder? Exploring the Language Shortcut of LLM-Driven Incomplete Multimodal Learning](http://arxiv.org/abs/2611.20349v2)
  <details><summary>📄 Abstract</summary>
  Is a face or a voice still heard once the words are known? Incomplete multimodal learning increasingly uses large language models (LLMs) as fusion engines: modality features enter as token blocks and missing modalities become placeholders. We find that LLM-driven fusion can override non-verbal evidence it can read. Contrasting its full-input prediction with counterfactual views, the same model shown one modality or no content, we identify language shortcuts. We build MR-Bench: MR-Bench-A types e...
  </details>

- **2026-11-16** — Varun Darshana Parekh, Anusha Devulapally, Sivani Devarapalli et al. — [ThermLeT: Transformer-based Temperature Prediction for 2.5D Chiplet Architecture](http://arxiv.org/abs/2611.21954v1)
  <details><summary>📄 Abstract</summary>
  The drive toward heterogeneous 2.5D chiplet packages promises unmatched performance and customization, yet the resulting density amplifies thermal challenges. To facilitate rapid design space exploration, we present ThermLeT, a multimodal transformer-based, scale invariant surrogate that integrates power density maps, spatial coordinate embeddings, material properties and heat transfer rate to predict steady state temperature in 13 ms, about four orders of magnitude faster than conventional fini...
  </details>

- **2026-11-16** — Dmitry A. Novikov — [Mechanism Design and Active Systems Theory: 60 Years of Parallel Development](http://arxiv.org/abs/2611.21803v1)
  <details><summary>📄 Abstract</summary>
  The survey compares two research traditions within the mathematical theory of designing the rules of interaction (mechanisms) for purposeful participants: mechanism design, together with contract theory and implementation theory, and the theory of active systems created by V.N. Burkov and developed into the theory of control in organizations (TCO) by D.A. Novikov's school; the main results of Yu.B. Germeier's school and of the domestic schools adjacent to active systems theory (AST) are covered ...
  </details>

- **2026-11-16** — Jenna M. Cann, Kimberly A. Weaver, Ryan W. Pfeifle et al. — [A Science Traceability Matrix for Micro-arcsecond Resolution X-ray Imaging](http://arxiv.org/abs/2611.21770v1)
  <details><summary>📄 Abstract</summary>
  Our ability to understand the highest energy processes and environments in astronomy is directly tied to our ability to probe their physical processes at the smallest scales. Despite transformative progress in high-angular resolution instruments across the radio through optical, angular resolution within the X-rays has plateaued around $\sim0.1-1''$, and therefore our window into the innermost regions of the high energy Universe lies primarily within spectral, timing, and/or polarimetric studies...
  </details>

- **2026-11-16** — Jiahao Yan, Xuanying Lai, Xiaoshui Lin et al. — [AI Scientist Discovered Robust Quantum Control](http://arxiv.org/abs/2611.21765v1)
  <details><summary>📄 Abstract</summary>
  Protecting quantum coherence is a central theme of modern quantum technologies. Carefully designed control pulses can extend coherence by suppressing disorder and unwanted interactions. However, designing robust pulse sequences remains challenging in interacting multi-level systems, where multiple independent error channels must be controlled in the presence of experimental imperfections. Here we introduce QORA, a multi-agent artificial intelligence framework that integrates theoretical reasonin...
  </details>

- **2026-11-16** — Renhe Sun, Yueying Feng, Bohan Yu et al. — [EgoLink: Egocentric Language-Vision Interactive Network Knowledge Challenge Summary](http://arxiv.org/abs/2611.21690v1)
  <details><summary>📄 Abstract</summary>
  The EgoLink Challenge at ACM Multimedia 2026 benchmarks egocentric multimodal intelligence linking first-person perception, social reasoning, and interactive action. Unlike benchmarks centered on visible objects and activities, EgoLink evaluates whether models can interpret emotional and social cues, resolve visually grounded references, and convert user requests into verified tool-mediated actions. Its two tracks cover social reasoning in egocentric video and interactive agents that complete se...
  </details>

- **2026-11-16** — Prashanti Nilayam, Kiran Kumar Ramanna, Prashil Tumbade et al. — [Borrowed Strength, Imported Risk: Capability Gaps and Reception Govern Heterogeneous LLM Debate](http://arxiv.org/abs/2611.20649v1)
  <details><summary>📄 Abstract</summary>
  Heterogeneous LLM debate is often attributed to collective reasoning that creates capability beyond any member. In the matched panels we study, the aggregate gain is dominated by capability transfer: a peer supplies task competence and receivers absorb a measurable fraction. Across nine matched directions, honest benefit and first-exchange adversarial exposure open when the peer has a positive same-task advantage, and honest gain is closely described by the empirical decomposition $ΔA_d^{\mathrm...
  </details>

- **2026-11-16** — Kimon Fountoulakis, Maksim Melnichenko, Muhammad Fetrat Qharabagh et al. — [Trustworthy Numerical Software in the Age of AI: What Would Turing Do?](http://arxiv.org/abs/2611.21570v1)
  <details><summary>📄 Abstract</summary>
  AI coding agents can now produce numerical software faster than human experts can review it, raising serious concerns about usability and reliability. These and other AI tools are already transforming mathematics and software, and they will soon transform mathematical software. These concerns motivated us to assess AI-generated numerical linear algebra (NLA) kernels, which we did through an audit of a recent public GPU QR competition. All five leading kernels passed the competition's accuracy te...
  </details>

- **2026-11-16** — Amber He Wei, Shiyu Cheng, Andrew Clark et al. — [A Scalable Decentralized Event-Triggered Topology-Switching Protocol for Verifiable Safety in Multi-Agent Systems](http://arxiv.org/abs/2611.21513v1)
  <details><summary>📄 Abstract</summary>
  This paper develops a decentralized event-triggered topology-switching protocol that allows agents to disconnect from the communication network while preserving state safety and excluding Zeno behavior. We establish a robust barrier function condition that guarantees safety as long as the estimation error remains within a prescribed threshold. Each agent uses locally computable certificates to determine when to connect and disconnect from the network. The certificate construction improves scalab...
  </details>

- **2026-11-16** — Fabio Picariello, Salvatore Cipolla, Susanna Bonura et al. — [Adaptive-Elbow Graph Traversal for Schema Retrieval in Text-to-SQL](http://arxiv.org/abs/2611.20979v1)
  <details><summary>📄 Abstract</summary>
  LLM-based natural-language interfaces to relational databases are gated by a schema-retrieval step: the generator can only be as good as the slice of schema it is shown. On a database with hundreds of tables, that slice must be selected and the selection is two-sided---omit a needed table and the query becomes unrecoverable, include too many and the irrelevant ones act as noise that degrades the model's output. When an agentic retriever that lets the model inspect the schema can be too costly or...
  </details>

- **2026-11-16** — Amir Bayat, Raphael M. Jungers — [NL2RCtrl: Risk-Controlled Controller Synthesis from Natural Language Requirements](http://arxiv.org/abs/2611.20748v1)
  <details><summary>📄 Abstract</summary>
  Large language models (LLMs) have enabled the translation of natural language (NL) requirements into linear temporal logic (LTL) specifications, facilitating controller synthesis for cyber-physical systems (CPSs). However, the reliability of such translations remains a concern in safety-critical applications, particularly when NL requirements are ambiguous. This paper proposes a framework based on Conformal Risk Control (CRC) to provide a statistical guarantee on the risk of issuing a controller...
  </details>


### 📂 watermark
*水印与溯源 / Watermarking & Provenance* — 9 papers

- **2026-11-18** — Auntor Chakma, Mst. Farhana Akter, Abu Henaf Rashid Ahmad Mufti et al. — [RespCCT and FreqCCT: Compact, Explainable and Cost-Aware Convolutional Transformers for Multi-Class Respiratory Disease Classification](http://arxiv.org/abs/2611.24323v1)
  <details><summary>📄 Abstract</summary>
  Chest auscultation depends on the listener, and software that classifies lung sounds could give a second reading where trained listeners are scarce. The most accurate published classifiers fine-tune large pretrained networks, and their accuracy is rarely reported with running cost or paired statistics. This study makes three contributions. (i) It proposes RespCCT and FreqCCT, two compact convolutional transformers of 173,187 and 124,999 parameters that learn from random initialization on mel, co...
  </details>

- **2026-11-18** — Dowling Wong — [Evaluating Governed LLM-Driven ML Experimentation: Lifecycle, Provenance, and Failure Metrics](http://arxiv.org/abs/2611.23678v1)
  <details><summary>📄 Abstract</summary>
  Autonomous agents that run ML experiments are usually judged by the best score they reach. That score says nothing about how it was reached: whether the agent stayed within the files it was allowed to edit, whether failed trials were kept or silently dropped, and whether each keep or discard decision can be traced to its evidence. We propose evaluating such systems on their experimental process as well as their outcome, and we build a governed harness that makes this possible. A control plane, n...
  </details>

- **2026-11-17** — Rukmangadh Sai Myana, Sumit Kumar Jha, Yanzhao Wu — [Entropy-Regularized Integrated Gradients for Stable Feature Attribution](http://arxiv.org/abs/2611.23600v1)
  <details><summary>📄 Abstract</summary>
  Path-based attribution methods like Integrated Gradients (IG) are widely used to interpret neural networks, yet imperceptible input perturbations can drastically alter their attribution maps while leaving model predictions unchanged. We introduce Entropy-Regularized Integrated Gradients (ERIG), a path-based attribution method that intrinsically attenuates gradient irregularities along the integration path using maximum-entropy softmax weighting with temperature parameter $τ$. We quantify the eff...
  </details>

- **2026-11-17** — Jiangyun Zhang, Zhou Tang, Kristen Surrao et al. — [ARISE: Practical Self-Evolving Memory for Accurate and Cost-Efficient Enterprise Agents](http://arxiv.org/abs/2611.23588v1)
  <details><summary>📄 Abstract</summary>
  Enterprise LLM agents operate in dynamic environments where foundation models evolve rapidly, workflows update frequently, and deployments need to satisfy accuracy and cost requirements. We propose ARISE (Agent Refinement through Iterative Self-Evaluation), a practical memory architecture in which the agent's memory evolves from its own failures without updating model weights, tools, or workflow logic. ARISE uses the model itself or a teacher model to attribute the failures and propose correctio...
  </details>

- **2026-11-17** — Xinyuan Li, Yi Nian, Xiaoqin Feng et al. — [Image Watermarking With Memory Across Reissuance](http://arxiv.org/abs/2611.23363v1)
  <details><summary>📄 Abstract</summary>
  Publishers often revise and reissue images, yet valid watermarks may persist on superseded releases or unapproved edits. Even a current release can contain regions last authorized at different revisions. We introduce and formalize reissuable provenance: determining an image's current, superseded, or unissued status and recovering each region's last authorized revision (its generation), with abstention when evidence is insufficient. Generational Stratigraphy Fields (GSF) combine watermark evidenc...
  </details>

- **2026-11-17** — Ziaullah Khan, Abdul Rehman Khalid, Shrestha Nischal Lal et al. — [Surfacing Disagreement Beats Resolving It: A Gated Ablation Study of Provenance-Weighted Memory for Multi-Agent Debate](http://arxiv.org/abs/2611.22461v1)
  <details><summary>📄 Abstract</summary>
  Shared memory for multi-agent debate is usually built to resolve inconsistency: retrieval returns one winning fact and the disagreement disappears before any agent sees it. We ask whether that is correct. In DebateGraph, four backends share one contract (read/write/snapshot), so five mechanisms from the agent-memory literature can be removed independently under a fixed budget, each gated on a pre-declared threshold. Across 39 runs one survives: preserving contradictions and passing the ranked co...
  </details>

- **2026-11-17** — Bohe Chen — [Simplicity Goes Far: Auditing Prompt Optimizers with Demonstration-Conditioned Prompt Search](http://arxiv.org/abs/2611.22605v1)
  <details><summary>📄 Abstract</summary>
  Automatic prompt optimization is growing more elaborate. Recent methods stack policy-gradient updates, trace reflection, and evolutionary search. These methods share a generate-and-select step; without controlling for it, reported gains may conflate the contributions of optimizer mechanisms and larger sampling budgets. We isolate this step as Demonstration-Conditioned Prompt Search (DCPS), repurposing the Automatic Prompt Engineer (APE) recipe as a mechanism-attribution control: it freezes the g...
  </details>

- **2026-11-17** — S. M Seefat Alam — [What Does a Bias Head Measure? Non-Identifiability in Head-Level Bias Attribution](http://arxiv.org/abs/2611.23218v1)
  <details><summary>📄 Abstract</summary>
  Methods that localise social bias in large language models to individual attention heads and remove it by ablation are validated by their effect on a fairness metric, never by evidence that the statistic selecting the heads measures bias. We audit this on Qwen-2.5-7B-Instruct and Llama-3.1-8B-Instruct. The head map correlates at $ρ= -0.950$ and $-0.768$ with a label-blind response-length map, apparently identifying a surface confound. An intervention that breaks the length-label coupling rejects...
  </details>

- **2026-11-16** — Juliette Alimena — [Training for sustainable scientific software in the AI era: from code production to scientific stewardship](http://arxiv.org/abs/2611.23330v1)
  <details><summary>📄 Abstract</summary>
  Generative and agentic artificial intelligence (AI) systems are changing how researchers interact with scientific software. Their effects on productivity vary across tasks and users, but they can weaken the connection between producing a successful computational artifact and retaining scientific command over the consequential choices and evidence on which it depends. For high-energy physics, this shifts part of the training challenge from code production toward scientific stewardship: researcher...
  </details>


### 📂 unlearning
*机器遗忘 / Machine Unlearning* — 2 papers

- **2026-11-18** — Zeguan Xiao, Zhuocheng Liang, Yun Chen et al. — [CurvDelta: Low-Curvature Delta Modeling For Surgical Learning and Unlearning](http://arxiv.org/abs/2611.24654v1)
  <details><summary>📄 Abstract</summary>
  A central challenge in adapting large language models (LLMs) is capability preservation: an adaptation can achieve its target while degrading general capabilities. We introduce CurvDelta, a scalable framework that incorporates the preservation constraint into the parameterization of the model update. By analyzing the local geometry of the preservation constraint around the pre-adaptation model, CurvDelta constructs a low-curvature space in which parameter updates leave the preservation loss near...
  </details>

- **2026-11-18** — Haowei Chen, Yichen Wang, Congfu Xu — [Kernel Ridge Attention: Nonlinear Memory with Selective Forgetting](http://arxiv.org/abs/2611.23896v1)
  <details><summary>📄 Abstract</summary>
  Kernel Ridge Attention (KRA) is a recurrent sequence mixer that combines learned nonlinear features with covariance-guided memory updates. It stores associations through recursive ridge regression, using correlations among past keys to determine how new observations modify memory. A content-dependent Ornstein--Uhlenbeck transition controls retention and restores uncertainty for future writes. This construction admits an exact temporal-kernel interpretation and maintains an inference state whose ...
  </details>


### 📂 survey
*综述与系统化 / Surveys & Systematization* — 3 papers

- **2026-11-17** — Uzma Shafiq, Matthew England, Nayyar Zaidi — [A Survey on the Use of Machine Learning within Computer Algebra](http://arxiv.org/abs/2611.23361v1)
  <details><summary>📄 Abstract</summary>
  This survey explores the use of Machine Learning (ML) in the field of Computer Algebra (CA), both to optimise existing CA algorithms, and to perform symbolic computation directly. Traditional symbolic methods, while mathematically rigorous, often are computationally expensive thus limiting their use in real-world applications. Recent advances have shown that data-driven techniques can address these limitations by guiding heuristic decisions, selecting optimal algorithms, predicting structural pr...
  </details>

- **2026-11-17** — Junseong Pyo, Hyeongjin Kim, Jongwook Han et al. — [PAIR: Bringing Household Robots into the Smart Home](http://arxiv.org/abs/2611.23070v1)
  <details><summary>📄 Abstract</summary>
  Household robots often need to operate appliances, and smart appliances offer both control panels and device APIs. Existing embodied AI simulation environments, however, model appliances solely as physical objects. We introduce PAIR, a smart-home simulation environment grounded in the Matter protocol~\footnote{https://csa-iot.org/all-solutions/matter/}, the industry standard for smart-home devices. PAIR provides 84 smart-device assets whose functional control panels and APIs act on a shared devi...
  </details>

- **2026-11-16** — Dario Fenoglio, Martin Gjoreski, Marc Langheinrich et al. — [WebAgents: Unbundling Agent Creation, Hosting, and Execution for an Agent-Native Web](http://arxiv.org/abs/2611.21978v1)
  <details><summary>📄 Abstract</summary>
  Large language models are moving from isolated assistants toward autonomous agents that can plan, use tools, and coordinate with others, motivating an emerging Agentic Web of independently developed agents and services. Realizing this vision requires agent behavior to move across creators, hosts, and runtimes without coupling publication to a particular execution environment or transferring authority over user resources. We introduce WebAgents, which unbundles these roles through a signed agent....
  </details>


### 📂 other
*其他安全相关 / Other Security-Related* — 171 papers

- **2026-11-18** — Ziyuan Wang, Genliang Zhu, Xiaobo Chen et al. — [Intent Contracts: Taking Tools Away from Agents](http://arxiv.org/abs/2611.24025v1)
  <details><summary>📄 Abstract</summary>
  Intent contracts are an authorization interface for tool-using LLM agents in which the planning model holds no tools. For each step it submits a short logged contract: a goal, a verbatim quotation of the user, and scope fields. Code validates the contract, and a small trusted model checks it against the user's words and writes the tool call itself. Provided the validation and dispatch code is correct, every executed call is written by the trusted model, the planner's influence on a call is confi...
  </details>

- **2026-11-18** — Lequn Fu, Yufeng Hu, Yijun Zhong et al. — [ReLoco: Unified Humanoid Locomotion and Fall Recovery via Behavior-Conditioned Motion Priors](http://arxiv.org/abs/2611.23916v1)
  <details><summary>📄 Abstract</summary>
  Humanoid robots must recover from falls and resume commanded motion to sustain locomotion. Learning these behaviors in one policy requires supervision that accommodates both upright movement and ground-contact recovery. We present ReLoco, a framework that uses behavior-conditioned adversarial motion priors to learn locomotion, get-up from arbitrary fallen postures, and command resumption within one proprioceptive policy. During training, robot posture selects the expert pool and conditions a sha...
  </details>

- **2026-11-18** — Jiapeng Pei, Yuhang Yao, Sitan Liu et al. — [Safe Personal RSI: Evaluating and Repairing Personal-Agent Updates](http://arxiv.org/abs/2611.23651v1)
  <details><summary>📄 Abstract</summary>
  Kicker is a personal health assistant. Changes to an assistant's reusable instructions can improve task handling while changing what it discloses, which requests it follows, and how it reports actions. We study Safe Personal RSI, an update-evaluation component developed for Kicker. We restrict recursive self-improvement (RSI) to prompt updates, with model weights and runtime code fixed. The procedure tests proposed and current instructions, repeats failing cases, temporarily undoes changes to gu...
  </details>

- **2026-11-18** — Junjie Ye, Yiqi Zhao, Muchen Xu et al. — [$Z$-sight: Unifying Vision-Language-Action and Latent World Modeling](http://arxiv.org/abs/2611.24940v1)
  <details><summary>📄 Abstract</summary>
  We introduce $Z$-sight, a unified robot foundation model that couples vision-language-action (VLA) and generative latent world modeling. Video-based world action models (WAMs) show the value of joint future-and-action generation for control, yet inherit the heavy cost of video generators. Recent latent-space policies avoid pixel generation, yet typically align intermediate features or rely on frozen target encoders, decoupling future prediction from the VLM's native feature space. $Z$-sight inst...
  </details>

- **2026-11-18** — Jiahang Lin, Jiahao Chen, Yiding Wang et al. — [Agentic Harness Engineering Beta: Requirement-Centered Evolution of Agent Harnesses](http://arxiv.org/abs/2611.24924v1)
  <details><summary>📄 Abstract</summary>
  Real-world harness engineering is driven by explicit and implicit user requirements, which guide development and validation. However, existing harness evolution methods often overlook implicit requirements and interaction needs, while using a single evolution agent to modify the harness and benchmark scores to select changes. This process often produces narrow patches and leads to benchmark-specific local optima. We introduce Agentic Harness Engineering Beta (AHE-Beta), a requirement-centered lo...
  </details>

- **2026-11-18** — Favour Nerrise, Julian Busch, Gurpreet Singh Hora et al. — [Measuring and Improving Transfer of Neural Surrogates for Vehicle Aerodynamics](http://arxiv.org/abs/2611.24843v1)
  <details><summary>📄 Abstract</summary>
  Neural surrogates for external vehicle aerodynamics are fast alternatives to physics-based computational fluid dynamics (CFD) simulations. Their foundational limitation is a lack of zero-shot generalization across vehicle classes, which results in an expensive, custom training campaign for each new vehicle design. Similar to pretrained models in other fields, a pretrained surrogate should adapt to a new vehicle class using only a few simulations and stay accurate on its pretraining domain. No pr...
  </details>

- **2026-11-18** — Haoran Ye, Tianrui Huo, Hangzhen Li et al. — [A Foundation Model to Measure and Predict Human Behaviour](http://arxiv.org/abs/2611.24830v1)
  <details><summary>📄 Abstract</summary>
  Large language models (LLMs) are increasingly used to infer psychological attributes, predict individual behaviour, and simulate human populations. However, despite generating plausible responses, they often misrepresent individuals and distort population statistics. Here we introduce Chiron, a foundation model to measure and predict human behaviour. We jointly fine-tune an LLM to represent psychological constructs, predict individual behaviour, and align population response distributions with h...
  </details>

- **2026-11-18** — Xinyi Guo, Kaile Huang, Xitong Ling et al. — [Read Together, Answer Apart: How Earlier Questions Help Vision-Language Models Look](http://arxiv.org/abs/2611.24785v1)
  <details><summary>📄 Abstract</summary>
  Vision-language models (VLMs) are often asked several questions about the same image in a single prompt (co-asking), yet existing evaluations report conflicting accuracy gains and hallucinations at the prompt level without tracking how individual answers change. By pairing each question's single-question and co-asked answers across 22 open-weight VLMs (1B-35B), we find that erratic net shifts reflect two opposing effects: on Densely Captioned Images (DCI), every model repairs 15.4%-29.8% of its ...
  </details>

- **2026-11-18** — Houman Mehrafarin, Ioannis Konstas — [Chain-of-Thought Hidden States Reveal Task-Solving Directions for Direct Answers](http://arxiv.org/abs/2611.24598v1)
  <details><summary>📄 Abstract</summary>
  Chain-of-Thought (CoT) prompting improves the performance of Large Language Models by eliciting intermediate reasoning steps. However, CoT is far from perfect: on some tasks, models perform worse than with direct-answer prompting, and on others they generate a few hundred tokens to reach the correct answer. We start by labelling each CoT hidden state as recovering if patching it into the direct prompt yields the correct answer, and failed otherwise. A linear probe shows that the model encodes th...
  </details>

- **2026-11-18** — Chuang Wang, Rui Nie, Jie Song et al. — [StrideWorld: Benchmarking Scene Rigidity and Action Consistency in Interactive Video World Model](http://arxiv.org/abs/2611.24408v1)
  <details><summary>📄 Abstract</summary>
  Interactive video world models turn user commands into the exploration of a generated scene, which requires the scene to keep its 3D structure as the camera moves and each action to keep a stable effect. Existing benchmarks mostly evaluate these properties against references fitted to the video under test, either a scene reconstructed from its own frames or a camera trajectory aligned to the command path with a free scale. Such references can absorb gradual scene deformation and changes in pace ...
  </details>

- **2026-11-18** — Md Abtahi Majeed Chowdhury, Md Rifat Ur Rahman, Md Sakib Hossain Shovon et al. — [Target-Consistent Action Guidance via Semi-Unbalanced Optimal Transport for Drifting World Models](http://arxiv.org/abs/2611.24222v1)
  <details><summary>📄 Abstract</summary>
  Action-conditioned world models let robots imagine the outcomes of their actions for planning and offline policy evaluation, but these uses need many rollouts, which multi-step diffusion makes expensive. Drifting models move the iteration from inference to training and generate samples in one network pass. DriftWorld brought this paradigm to action-conditioned world models; to strengthen action following, it repels predictions from the current frame, a construction borrowed from classifier-free ...
  </details>

- **2026-11-18** — Xuerui Fang, Gulimila Kezierbieke, Chen Wangxing et al. — [TrajWAM: Trajectory-Conditioned Future Learning for Vision-Language Driving](http://arxiv.org/abs/2611.24192v1)
  <details><summary>📄 Abstract</summary>
  World Action Models (WAMs) connect future scene prediction with action planning for autonomous driving. Each driving record pairs an executed ego trajectory with its observed future, providing a factual outcome for learning this connection. We present TrajWAM, a trajectory-conditioned WAM that improves vision-language driving through auxiliary bird's-eye-view (BEV) future learning. An ego-trajectory query conditions DINOv3-aligned BEV predictions from shared planner representations. Training com...
  </details>

- **2026-11-18** — You Peng, Youhe Jiang, Chen Wang et al. — [eFAIR: Fair LLM Serving under Hourly Electricity Commitments](http://arxiv.org/abs/2611.24119v1)
  <details><summary>📄 Abstract</summary>
  Datacenters can procure electricity in day-ahead markets by committing to energy purchases for individual hours. For LLM services operating within these hourly budgets, maximizing aggregate throughput alone may still leave individual requests waiting or receiving much slower service than desired. Fair serving therefore requires improving service for poorly served requests while reserving electricity for later arrivals whose timing and demand are unknown. To compare service across requests, we de...
  </details>

- **2026-11-18** — Abbas Raza Ali, Muhammad Hamza Rehman, Xu Li et al. — [From Data to Valves: A Self-Learning, Production-Grade Edge Stack for Sustainable HVAC Control](http://arxiv.org/abs/2611.24052v1)
  <details><summary>📄 Abstract</summary>
  Learned HVAC controllers rarely leave the simulator, and those that do are typically trained offline, frozen at deployment and retrained from the cloud. We present a production stack in which three learning components run on one NVIDIA Jetson Orin gateway per building, adapt continuously from the building's own data, and verify their own effect. (a) A compact transformer-encoder forecaster, one per equipment group with learned per-unit embeddings, predicts every air-side unit's next-cycle temper...
  </details>

- **2026-11-18** — Zhengyuan Fan, Zhonghua Wu, Tianyu Cheng et al. — [How Reward Gain Imbalance Shapes Ranking: Rethinking Rubric-Based Reward Aggregation](http://arxiv.org/abs/2611.24005v1)
  <details><summary>📄 Abstract</summary>
  Rubric-based reinforcement learning constructs rewards for aligning large language models with human preferences, typically by equally aggregating continuous scores that a judge assigns to individual criteria. However, scoring heterogeneity across criteria can distort candidate rankings. Existing work has focused on improving judges, learning criterion weights, or refining aggregation, whereas the interaction between scoring heterogeneity and ranking remains insufficiently understood. We formali...
  </details>

- **2026-11-18** — Wen Wang, Jindong Wang, Jiahua Bao et al. — [Evidence-Based Credit Assignment for Search-Augmented Language Models](http://arxiv.org/abs/2611.23824v1)
  <details><summary>📄 Abstract</summary>
  Reinforcement learning from terminal answer rewards enables search-augmented language models to interleave reasoning and retrieval without step-level annotations, yet outcome supervision assigns identical credit to every search in a trajectory regardless of whether it retrieved useful information. This limitation is especially severe when all sampled rollouts for a question fail, collapsing group-centered outcome advantages to zero even when trajectories gather markedly different evidence. We pr...
  </details>

- **2026-11-18** — Yeongtak Oh, Donghyeok Lee, Joonhee Oh et al. — [PReMind: When Personal Memory Meets Visual Hazards](http://arxiv.org/abs/2611.23808v1)
  <details><summary>📄 Abstract</summary>
  Personalized vision-language assistants use visual observations and personal memories to provide advice tailored to the user. When the observed scene contains a physical hazard, personal context, such as allergies, medical conditions, or mobility constraints, can change what help is appropriate. Responding appropriately therefore requires recognizing the visible hazard and applying the relevant person's information. We introduce PReMind-Bench, a diagnostic benchmark that evaluates this combinati...
  </details>

- **2026-11-18** — Haotian Wei, Can Long, Wen Xian Jim et al. — [Beyond Intelligibility: Fine-Grained Perceptual Assessment of Dysarthric Speech with Auditory Large Language Models](http://arxiv.org/abs/2611.23768v1)
  <details><summary>📄 Abstract</summary>
  Accurate assessment of dysarthric speech is vital for clinical diagnosis and rehabilitation, yet existing automated methods rely heavily on isolated, single-task models or generic speech quality metrics that fail to disentangle heterogeneous neuromotor deficits. This work presents the first systematic investigation into adapting auditory large language models (ALLMs) for multi-dimensional dysarthric speech assessment under a unified, prompt-conditioned framework. Four representative ALLMs are be...
  </details>

- **2026-11-18** — Ayman bin Kamruddin, Christopher Lam, Gaurav Patil et al. — [A Comparison of Heuristic, Human-Sensitive, and Self-Play DRL Policies in Human-Agent Teaming](http://arxiv.org/abs/2611.23747v1)
  <details><summary>📄 Abstract</summary>
  Dynamical Perceptual-Motor Primitives (DPMPs) offer a tractable framework for generating human-like movement dynamics in artificial agents (AAs) and have been used to support coordination in human-AI teaming tasks. Traditionally, DPMP controllers rely on heuristic (rule-based) decision policies derived from human behavior to guide goal selection and action sequencing. Although effective in structured tasks, such heuristics can be difficult to generalize to more complex settings, motivating inter...
  </details>

- **2026-11-18** — Shuichiro Ozawa, Izumi Takahara, Fumihiko Uesugi et al. — [Fast closed-loop STEM navigation using vision-language models with typed decisions](http://arxiv.org/abs/2611.23698v1)
  <details><summary>📄 Abstract</summary>
  Closed-loop scanning transmission electron microscopy (STEM), in which each acquired image determines the next field of view and magnification, offers a route to autonomous atomic-scale materials analysis. Such a loop would automate navigation to defects and grain boundaries, a task that has long relied on operator judgment, and would enable systematic analysis of diverse local structures at scale. Realizing it hinges on the decision step, which must translate each acquired image into the next o...
  </details>

- **2026-11-18** — Jennifer Zhang, Amanda Coston — [When Do LLMs Model the Right Target? Problem Formulation in High-Stakes Risk Prediction](http://arxiv.org/abs/2611.23638v1)
  <details><summary>📄 Abstract</summary>
  Generative AI is increasingly used to assist with data science tasks, yet fundamental questions remain about its ability to correctly formulate analytical problems. We investigate how well large language models (LLMs) can formulate prediction problems when developing models for high-stakes decision making. We focus on one particular challenge to validity: decision dependency, which arises when historical decisions affect observed outcomes. We evaluate this aspect of problem formulation in LLM-ge...
  </details>

- **2026-11-18** — Akshay L Chandra, Iman Nematollahi, Lingyue Zhao et al. — [DiWALI: Diffusion Policy Learning in World Models via Latent Action Inference from Human and Robot Play](http://arxiv.org/abs/2611.24836v1)
  <details><summary>📄 Abstract</summary>
  Learning robot manipulation is constrained by the availability of action-labeled robot data, for both imitation and world models. Humans can demonstrate skills in seconds, but their demonstrations lack the required robot actions. We introduce DiWALI, a framework that learns and improves diffusion policies within a world model trained on human and robot play. DiWALI infers latent actions from consecutive frames using an inverse dynamics model, enabling world model training without action labels, ...
  </details>

- **2026-11-18** — Phuong Tuan Dat, Qi Li, Xinchao Wang — [HINT-WAM: Hindsight-Informed Training for World Action Models](http://arxiv.org/abs/2611.24789v1)
  <details><summary>📄 Abstract</summary>
  World action models (WAMs) have shown promising generalization and data efficiency in robot manipulation by coupling action generation with predictions of future visual dynamics. Translating these capabilities into reliable task execution, however, remains a challenge for existing post-training methods. Offline supervised fine-tuning provides dense supervision on expert trajectories, but its flow-matching action expert is trained only on noised demonstration actions and never on the intermediate...
  </details>

- **2026-11-18** — Pengyu Li, Zhitao Gao, Lingling Zhang et al. — [Do Thinking VLMs Need to Keep Looking at Long Videos? Write It Down, Then Look Away](http://arxiv.org/abs/2611.24259v1)
  <details><summary>📄 Abstract</summary>
  Vision-language models (VLMs) reason about long videos over hundreds to thousands of tokens. Every decoding step re-reads the key-value (KV) cache of the entire video. Must the model keep looking while it reasons? In LookAway, the model first writes timestamped notes on what the question needs and then puts the video away. Once the notes close, the inference engine hides the video's KV cache for the rest of the response. Across both hybrid and pure-attention VLMs, dependence on the video is conc...
  </details>

- **2026-11-18** — Yoobin Shin, Jaeyoung Lee, Jieun Kang et al. — [TapTacTouch: Shape Completion from Sparse Tactile Contacts with Geometric Priors](http://arxiv.org/abs/2611.24207v1)
  <details><summary>📄 Abstract</summary>
  3D object reconstruction is essential for robotic perception and manipulation, yet conventional approaches predominantly rely on visual observations that can be limited by occlusion or unavailable in visually constrained environments. In this work, we propose a vision-free, training-free, and category-agnostic framework for reconstructing 3D object meshes from sparse tactile contacts without relying on pretrained shape models. A 6-DoF robotic arm equipped with a 20-DoF multi-finger robotic hand ...
  </details>

- **2026-11-18** — Long Xu, Fuyi Wang, Xiaolu Hu et al. — [Evaluating LIM Trading Agents: A Critical Review of Backtesting Validity and Reporting Practices](http://arxiv.org/abs/2611.24133v1)
  <details><summary>📄 Abstract</summary>
  Large language models (LLMs) are increasingly used in investment research, and many studies report promising historical returns. However, such results are only credible if researchers can demonstrate that the model used only information available at the time, account for how strategies and configurations were selected, and explain how reported returns were generated. We identify six common threats to validity in LLM investment evaluations and apply them to 18 published studies. Across 108 assess...
  </details>

- **2026-11-18** — Alperen Örsdemir, Rochelle Xenia Mendoza Santos, Wen Shei Ong et al. — [When Do Decision Models Help LLM-Driven Network Discovery?](http://arxiv.org/abs/2611.23947v1)
  <details><summary>📄 Abstract</summary>
  Network discovery, the identification of live hosts and their exposed services, is the first phase of every penetration test, and it is increasingly automated by harnesses driven by large language models (LLMs). To mitigate hallucinated or unsafe commands, recent work proposes inserting fast, non-generative decision models to validate actions prior to execution. This paper quantifies whether such validation improves discovery across three network scales (n = 10, 100, and 1,000) in a simulation c...
  </details>

- **2026-11-18** — Apoorva Vashisth, Manav Kulshrestha, Damon Conover et al. — [RePlan-VLA: Progress-Aware Replanning for Long-Horizon Vision-Language-Action Models](http://arxiv.org/abs/2611.23843v1)
  <details><summary>📄 Abstract</summary>
  Vision-Language-Action (VLA) models have emerged as a promising paradigm for general-purpose robotic manipulation, yet their performance often degrades on long-horizon tasks that require multiple interdependent manipulations. Instead of burdening the VLA policies with long-horizon reasoning, memory, action generation, progress tracking, and error recovery, we argue for leveraging their short-horizon manipulation capabilities within an execution-aware framework. To this end, we introduce \textnor...
  </details>

- **2026-11-18** — Jinhao Zhang, Yushen Zuo, Ke Rui et al. — [CoT-WAM: Collaborative Training of Vision-Language Models and World-Action Models via Plan Latents](http://arxiv.org/abs/2611.23803v1)
  <details><summary>📄 Abstract</summary>
  General robot manipulation requires both semantic competence and physical foresight. World action models (WAMs) acquire an understanding of and predictive capability over the physical world by jointly modeling visual foresight and action distributions. However, existing WAMs still lack semantic competence: they have limited ability to perform open-world scene understanding, semantic reasoning, and long-horizon planning. Although vision-language models (VLMs) provide these capabilities, effective...
  </details>

- **2026-11-18** — Zhiyu Liu, Xinyu Yang — [Auditing black-box clinical prediction models with a large language model through queries alone: a blinded test with planted flaws](http://arxiv.org/abs/2611.24877v1)
  <details><summary>📄 Abstract</summary>
  Large language models (LLMs) are used to explain clinical prediction models, on the promise that they can say what a model computes, find its faults and even reveal new knowledge in it. We tested the three promises where the answers could be checked. From the International Stroke Trial we trained four kinds of model (logistic regression, explainable boosting machine, gradient-boosted trees, neural network) for two outcomes on patients randomised earlier, planted one flaw in each of 24 copies (an...
  </details>

- **2026-11-18** — Eugene Agichtein, Charles L. A. Clarke, Kaustubh Dhole et al. — [Can Programs Replace LLM Judges? Executable Program Judges for Scalable and Efficient Relevance Labeling](http://arxiv.org/abs/2611.24849v1)
  <details><summary>📄 Abstract</summary>
  Large language model (LLM) judges have become a common way to create large-scale relevance judgments for retrieval evaluation. However, each judgment requires a potentially expensive call to a frontier model, and the judgments are hard to interpret and may not be reproducible. In this paper, we ask whether an LLM can write a readable program for each topic that replaces its per-document judgments. To address these issues, we propose ExecJudges, a method for generating fast, inspectable and scala...
  </details>

- **2026-11-18** — Emad Aghajanzadeh, Bethany Anne Wong, Leonhard Kunze et al. — [DRIFT: Detachable Reasoning for Runtime-Flexible and Efficient End-to-End Driving](http://arxiv.org/abs/2611.24719v1)
  <details><summary>📄 Abstract</summary>
  The integration of vision-language models (VLMs) into end-to-end (E2E) autonomous driving has demonstrated strong potential by providing scene description and reasoning capabilities. However, VLMs are computationally expensive, and switching language reasoning on and off at runtime without hurting closed-loop performance has not been demonstrated, which hinders practical adoption. To address these issues, we propose DRIFT, an E2E autonomous driving framework that integrates a lightweight languag...
  </details>

- **2026-11-18** — Kamil Szczech, Maksymilian Wojnar, Krzysztof Rusek et al. — [Can Bandits Learn to Share a Channel? Distributed Multi-Armed Bandits for Slotted ALOHA](http://arxiv.org/abs/2611.24676v1)
  <details><summary>📄 Abstract</summary>
  Slotted ALOHA networks constitute a playground for research on machine learning (ML)-based channel access schemes. We consider ML agents deployed in such networks and operating under severe constraints: fully distributed (independent operation), fully online (no pre-training), aperiodic (no fixed schedule), and with no explicit coordination (no signaling). We ask whether a multi-armed bandit (MAB), a minimal reinforcement learning agent, can learn the optimal policy for a capture-free slotted AL...
  </details>

- **2026-11-18** — Valerio Taralli, Andrea Tosin — [Modelling population distribution across cities on spatial networks using the kinetic theory of multi-agent systems](http://arxiv.org/abs/2611.24657v1)
  <details><summary>📄 Abstract</summary>
  We investigate the urban population distribution of the Italian region of Sardinia through the kinetic theory of multi-agent systems on spatial networks, interpreting cities both as agents and vertices of a graph, and representing interurban links as edges. We consider various emigration rules to model the interactions between agents, obtaining two main results: the bimodal lognormal fit of the total population distribution among cities and the Pareto fit of the tail. Overall, our model provides...
  </details>

- **2026-11-18** — Robert Debbas, Éric Goubault, Sylvie Putot — [Zonotopic Analysis of Quantization Error in Neural Networks](http://arxiv.org/abs/2611.24648v1)
  <details><summary>📄 Abstract</summary>
  Quantized neural networks achieve computational efficiency by reducing precision, but bounding their quantization error remains a challenge due to discrete rounding and clamping operations. We present a zonotope-based abstract interpretation framework for quantized ReLU feed-forward network verification, introducing a unified round-clamp abstract transformer that jointly handles both operations. We extend this framework to constrained zonotopes, which add linear constraints to tighten bounds, an...
  </details>

- **2026-11-18** — Maria Cristina Aspromonte, Alexander M. Monzon, Miguel A. Andrade-Navarro et al. — [Biases and Limits of AlphaFold Predictions for Non-Globular Proteins](http://arxiv.org/abs/2611.24546v1)
  <details><summary>📄 Abstract</summary>
  AlphaFold has transformed protein structure prediction, making structural models accessible across the life sciences. We explore experimentally validated cases of non-globular proteins to uncover where predictions diverge from biologically relevant structural states and how molecular context shapes these discrepancies, guiding a more informed interpretation of AlphaFold models.
  </details>

- **2026-11-18** — Daiqing Wu, Junqiao Wang, Chengyang Fang et al. — [UEmo-D1: An Efficient and Calibrated Decision Model for Unified Multimodal Emotion Recognition](http://arxiv.org/abs/2611.24481v1)
  <details><summary>📄 Abstract</summary>
  Multimodal Emotion Recognition (MER) seeks to identify emotions conveyed through or elicited by media comprising diverse modality compositions. Research in this field has largely evolved along two paradigms: task-specific models and approaches based on Multimodal Large Language Models (MLLMs). Despite their distinct strengths, neither fully reconciles three capabilities essential to human-like emotion understanding: cross-task generalization, efficient decision-making, and receptiveness to multi...
  </details>

- **2026-11-18** — Edoardo Chidichimo, Felix P. S. Wallis — [Nothing to Declare: Steering a single neuron increases concealment in AI teams](http://arxiv.org/abs/2611.24475v1)
  <details><summary>📄 Abstract</summary>
  Recent research suggests that individual neurons can have interpretable roles in AI behaviour. In Qwen3.5-4B, steering along one neuron's output direction increased decisions to conceal information more in teams than alone across five scenarios, even when teammates provided no messages. When all members participated and received steering, collective concealment increased in four scenarios, while inter-agent messaging helped temper concealment under steering. Moreover, removing the neuron's contr...
  </details>

- **2026-11-18** — Yang Ji, Ying Sun, Yuanxin Zhuang et al. — [Retroactive Concept Bottleneck Models for Exemplar-Free Class-Incremental Learning](http://arxiv.org/abs/2611.24445v1)
  <details><summary>📄 Abstract</summary>
  Exemplar-free class-incremental learning (EFCIL) requires models to learn new classes sequentially without retaining training samples from previous tasks. Continual concept bottleneck models (CBMs) make their predictions interpretable by identifying visual concepts in an image and using them to score each class. However, these methods typically focus on preserving learned concepts or approximating past classes with generated features, which can leave new concepts underused in old-class predictio...
  </details>

- **2026-11-18** — Deepro Das, Saad Kabir Uddin, Mohammad Alauddin et al. — [Explainable and CPU-Efficient Brain Tumor Classification from MRI Using Two-Phase EfficientNetB3 Fine-Tuning](http://arxiv.org/abs/2611.24440v1)
  <details><summary>📄 Abstract</summary>
  Brain tumors are among the most lethal neurological disorders, with over 308,000 new diagnoses annually worldwide. Accurate classification of tumor type from Magnetic Resonance Imaging (MRI) scans is critical for treatment planning; however, manual radiological interpretation is time-consuming and prone to inter-observer variability. This paper proposes an automated deep learning pipeline for four-class brain MRI classification (glioma, meningioma, no tumor, and pituitary tumor) using EfficientN...
  </details>

- **2026-11-18** — Baichuan Yang, Dongyuan Xu, Zhao Yang et al. — [MLIE-CoT: Chain-of-Thought Reasoning via Multi-Level Image Editing](http://arxiv.org/abs/2611.24433v1)
  <details><summary>📄 Abstract</summary>
  Chain-of-thought (CoT) reasoning has proven effective in improving the reasoning abilities of large language models by breaking complex tasks into step-by-step solutions. In recent years, researchers have attempted to extend CoT reasoning to visual generative models to improve their ability to handle complex tasks. However, existing CoT methods for text-to-image generation still rely mainly on textual reasoning and therefore cannot fully use and preserve the correct semantic information already ...
  </details>

- **2026-11-18** — Dongjun Han, Mingyu Lee, Ikjin Lee — [LLM-Assisted Multi-Fidelity Bayesian Optimization: Fusing Expert Knowledge with Numerical Data](http://arxiv.org/abs/2611.24377v1)
  <details><summary>📄 Abstract</summary>
  Multi-fidelity Bayesian optimization (MFBO) reduces engineering design cost by combining inexpensive low-fidelity (LF) models with a few accurate high-fidelity (HF) evaluations and sequentially selecting designs to evaluate. However, when HF data are scarce, the LF-HF discrepancy is difficult to learn from numerical data alone, especially when physics omitted in the LF model makes it design-dependent. Yet even without sufficient data, domain experts often know which physics the LF model omits an...
  </details>

- **2026-11-18** — Guolong Zheng, Chen Hou, Xu Yang et al. — [Semantic Context Handoff with On-Demand Evidence for Long-Horizon Agents](http://arxiv.org/abs/2611.24357v1)
  <details><summary>📄 Abstract</summary>
  Traditional long-horizon LLM agents often hand off context through full-history prompting, retaining all previous action--observation interactions. As execution proceeds, this history keeps growing, increasing inference cost and potentially degrading accuracy. Existing methods control this growth by preserving compact conclusions while removing earlier observations, but doing so can discard evidence that later becomes relevant. We introduce Semantic Context Handoff (SCH), whose central abstracti...
  </details>

- **2026-11-18** — Karim Achouri, Youssef Dib, Hossein Allahverdizadeh et al. — [Bound States in the Continuum as Converging Scattering Zeros in Metasurfaces: Why Accidental BICs Require Nonlocality](http://arxiv.org/abs/2611.24326v1)
  <details><summary>📄 Abstract</summary>
  Bound states in the continuum (BICs) allow metasurfaces to achieve extremely high quality factors, yet it remains unclear how they emerge and how they can be described by effective material parameters. We address this question by modeling BICs through the reflection and transmission zeros of a metasurface described by effective susceptibilities. By decomposing its response into even and odd parts, and inspecting the interaction of the corresponding poles and zeros, we show that a high-Q resonanc...
  </details>

- **2026-11-18** — Warut Suksompong — [On the Complexity of Envy Cycle Elimination](http://arxiv.org/abs/2611.24167v1)
  <details><summary>📄 Abstract</summary>
  The envy cycle elimination (ECE) algorithm is a fundamental algorithm for the fair allocation of indivisible goods, guaranteeing an allocation that is envy-free up to one good under arbitrary monotone utilities. We show that the ECE algorithm can be implemented in $O(nm)$ time for $n$ agents and $m$ goods, and establish the tightness of this bound.
  </details>

- **2026-11-18** — Xiaoqian Shen, Yunyang Xiong, Changsheng Zhao et al. — [AVTR: Adaptive Multimodal Reasoning with Visual Imagination](http://arxiv.org/abs/2611.24161v1)
  <details><summary>📄 Abstract</summary>
  Vision-Language Models increasingly rely on textual reasoning to solve advanced multimodal tasks. Despite its effectiveness, this paradigm faces two fundamental limitations. First, relying on textual reasoning alone can limit perceptual ability in vision-centric questions, where accurate answers depend on interpreting task-relevant visual evidence. Second, applying textual reasoning uniformly across inputs overlooks question-dependent variation in both reasoning modality and depth, often produci...
  </details>

- **2026-11-18** — Ernesto Biempica, Emiliano Bruner, Juan F Poyatos — [Human-LLM Cognitive Extension: A Framework for Studying Coupled Cognition](http://arxiv.org/abs/2611.24149v1)
  <details><summary>📄 Abstract</summary>
  Recent research on the use of Large Language Models (LLMs) reports divergent cognitive outcomes, including improved assisted performance, limited transfer, and compromised unaided learning. Here, we argue that part of this seeming inconsistency arises because studies often assess different cognitive systems without making the unit of analysis explicit. Building on work in extended and distributed cognition, we propose the Human-LLM Cognitive Extension (HLCE) as a methodological framework for mat...
  </details>

- **2026-11-18** — Lei Ying — [Second-Order Steady-State Approximation of Heterogeneous Mean-Field Models](http://arxiv.org/abs/2611.24123v1)
  <details><summary>📄 Abstract</summary>
  Mean-field models provide tractable approximations for large stochastic systems, but second-order steady-state results are largely limited to homogeneous or fixed-dimensional population processes. This paper develops a second-order steady-state approximation for fully heterogeneous mean-field models. Conditioning on the realized agent parameters, we study fixed-dimensional weighted occupancies even though the dimension of the full heterogeneous mean-field system grows linearly with the number of...
  </details>

- **2026-11-18** — Luca Lusvarghi, Javier Gozalvez — [Attention Is Not Relevance: Challenging the Causality of Attention in Autonomous Driving](http://arxiv.org/abs/2611.24051v1)
  <details><summary>📄 Abstract</summary>
  Attention has become one of the most widely adopted solutions for estimating the relevance of surrounding objects and interpreting an autonomous vehicle's driving decisions. However, its ability to capture the causal impact of individual input elements on an AI model's output has long been discussed in the literature, particularly in the Natural Language Processing (NLP) domain. This work brings this discussion into the autonomous driving domain by analyzing the accuracy of attention in estimati...
  </details>

- **2026-11-18** — Yilin Wang, Xin Yu, Xinyi Guo et al. — [ReSynth: Constructing Synthetic Supervision for Multi-Image Understanding](http://arxiv.org/abs/2611.23996v1)
  <details><summary>📄 Abstract</summary>
  People often understand the world by comparing different views of it. Vision-language models (VLMs), however, receive these views as separate images and still struggle to relate them. One problem is data. Training on these tasks requires groups of images with a known relationship: the same object from different viewpoints, or the same scene before and after a change. Such examples are hard to collect at scale from existing photo collections. We introduce ReSynth, which turns single-image percept...
  </details>

- **2026-11-18** — Nan Hou, Kangfei Zhao, Jiadong Xie et al. — [Cascadeability and the Realization Gap: An Empirical Study of LLM-Powered Semantic Filtering](http://arxiv.org/abs/2611.23898v1)
  <details><summary>📄 Abstract</summary>
  Semantic filters enable natural language predicates over unstructured documents, but evaluating every document with a large language model (LLM) oracle is expensive. Proxy cascades reduce oracle invocations using cheaper surrogates, but oracle reduction alone cannot distinguish proxy limitations from calibration bottlenecks and establish practical efficiency. We present a unified benchmark of four representative systems, which formulate query processing as a three-stage workflow comprising proxy...
  </details>

- **2026-11-18** — Ilker Oguz, Colin Christian, Christophe Moser et al. — [In Situ Training of Optical Neural Networks by Coding Agents](http://arxiv.org/abs/2611.23875v1)
  <details><summary>📄 Abstract</summary>
  Optical neural networks promise fast, energy-efficient computing, but every device departs from its design and must be trained with the hardware. In situ training relies on an expert-built calibrated digital model of each device or on gradient-free trial and error. Coding agents, large language models that write and run programs, have shown an emergent ability to understand and edit the weights of digital neural networks. Here we introduce optics as code, a method in which a coding agent trains ...
  </details>

- **2026-11-18** — Haiming Zhu, Zhiwei Chen, Ding Cao et al. — [Keep the Image in Mind: A Visual Board for Multimodal Agents](http://arxiv.org/abs/2611.23872v1)
  <details><summary>📄 Abstract</summary>
  Multi-step visual reasoning suffers when early visual misinterpretations persist as incorrect premises in subsequent reasoning. We argue that how visual evidence is represented during reasoning matters as much as how much of it is gathered. Rather than appending observations and inferences to an ever-growing dialogue, we introduce a Visual Board-centered harness that separates visual observations, uncertain interpretations, and derived reasoning within a structured, capacity-bounded, and revisab...
  </details>

- **2026-11-18** — Hangle Hu, Chenyu Hou, Bin Cao et al. — [Asking but Missing: Decision Coverage in Natural-Language Data Querying](http://arxiv.org/abs/2611.23864v1)
  <details><summary>📄 Abstract</summary>
  Large language models are increasingly used to translate natural language questions about structured data into executable programs. A fundamental challenge is recognizing when a question admits multiple computational interpretations and identifying the decisions needed to resolve them. We investigate whether language models recognize these unresolved decisions before generating code, or silently adopt assumptions that may lead to incorrect results. We refer to the latter behavior as Underspecifi...
  </details>

- **2026-11-18** — Bin Yin — [Online State-Representation Adaptation under Synthetic Interaction-Cue Remapping](http://arxiv.org/abs/2611.23836v1)
  <details><summary>📄 Abstract</summary>
  When cues change what they predict, continuing to update a learned mapping may help an agent choose the appropriate action. We tested this in a one-step synthetic task by comparing a logistic state predictor that continued to learn from state labels with the same predictor frozen at transfer. We evaluated ten conditions in six held-out environments, with 1,296 paired runs per condition and 1,296,000 transfer records in total. Late action accuracy was 93.39% with online updates and 64.63% with fr...
  </details>

- **2026-11-18** — Katsutoshi Yoshida — [Euler-Lagrange Equations Formulated in Terms of Angular Velocity](http://arxiv.org/abs/2611.23828v1)
  <details><summary>📄 Abstract</summary>
  We propose a novel variant of the Euler--Lagrange (EL) equation for rigid body rotation, explicitly formulated in terms of orientation parameters $\thh$ and angular velocity $\omm$.   Variational analysis of the stationarity condition of the action integral for a Lagrangian in terms of $\thh$ and $\omm$ yields a modified EL formulation.   For pure rotational motion, the proposed equation directly recovers equations of motion fully consistent with the classical Euler equations, bypassing explicit...
  </details>

- **2026-11-18** — Tianqi Chen — [Temporal Fair Division: Simultaneous Guarantees for Goods and Chores](http://arxiv.org/abs/2611.23782v1)
  <details><summary>📄 Abstract</summary>
  We study temporal fair division of indivisible items in both the goods and chores settings, with $n \ge 2$ agents and nonnegative additive values or costs. Items arrive one at a time and must be assigned immediately and irrevocably. The arrival order and all agents' values or costs are known in advance, and the cumulative allocation must satisfy the fairness requirements after each arrival. For goods, we give a polynomial-time algorithm that simultaneously achieves exact temporal proportionality...
  </details>

- **2026-11-18** — Yao Chen, Jiagang Ren, Hua Zhang — [Geiss-Besov Regularity of Exit Times of Diffusion Processes](http://arxiv.org/abs/2611.23763v1)
  <details><summary>📄 Abstract</summary>
  We prove that the truncated exit times of possibly degenerate diffusion processes from open domains satisfying the exterior sphere condition belong to the Geiss-Besov space $\mathbb{B}_p^{\frac{1}{2p}}$. In the one-dimensional case, the same result is proven using Zvonkin transformation for untruncated exit times if the diffusion is uniformly elliptic.
  </details>

- **2026-11-18** — Abdiaziz Muse, Jiju Poovvancheri — [Do 3D Point Representations Encode Architectural Functions? Probing Supervised and Pretrained Models on Urban Facades](http://arxiv.org/abs/2611.23720v1)
  <details><summary>📄 Abstract</summary>
  Semantic labels say what a building element is, not what it does: two identical-looking windows on one facade may be operable or fixed, a column may carry load or only decorate. We ask whether 3D point representations encode such architectural function. On 22 mobile-LiDAR buildings with 15 functional attributes per element, we hold out entire buildings and compare hand-crafted descriptors, networks trained from scratch and frozen self-supervised point transformers. Descriptors and frozen feature...
  </details>

- **2026-11-18** — Shenghan Gao, Zhiling Zheng — [Structured Extraction of Diffraction Data from Covalent Organic Frameworks](http://arxiv.org/abs/2611.23680v1)
  <details><summary>📄 Abstract</summary>
  Powder X-ray diffraction (PXRD) is the primary structural evidence for covalent organic frameworks (COFs) and many other materials. Yet decades of measured patterns exist only as images in published figures. Automatic recovery is difficult, because PXRD figures vary widely in format, from a single curve to crowded stacks with labels, insets, and neighboring plots that challenge traditional computer vision. This work presents a pipeline in which a vision large language model (LLM) interprets the ...
  </details>

- **2026-11-18** — Erzheng Zhang, Agnes Chu — [Same Model, Different People: Numerical Execution Contracts and the Reproducibility of Fairness Audits](http://arxiv.org/abs/2611.23657v1)
  <details><summary>📄 Abstract</summary>
  Fairness audits treat a trained model as a fixed decision function, but the arithmetic that evaluates it is part of that function. This study holds the model, records, threshold and audit code fixed and varies the numerical execution contract in two tiers. Tier 1 changes only how products and sums are computed, with the serialized weights byte-identical, and is the causal test of arithmetic. Tier 2 runs reduced-precision deployment configurations (BF16 compute, FP8 and 8-bit weights), which can ...
  </details>

- **2026-11-17** — Prashank Kadam — [Option-GRPO: Hierarchical RL Against AI Slop in Code Generation for Unseen SDKs](http://arxiv.org/abs/2611.23633v1)
  <details><summary>📄 Abstract</summary>
  Large language models increasingly produce AI slop in generated code: verbose, redundant, non-idiomatic implementations that pass functional checks but bloat codebases. The problem compounds on SDKs released after the model's training cutoff, where the model has neither idiomatic priors nor compositional understanding. We present Option-GRPO, a hierarchical reinforcement learning framework that adapts a code LLM to an unseen SDK from its source code alone, without human-written usage examples or...
  </details>

- **2026-11-17** — Adhyayan Veer Singh, Fanjiang Ye, Yuke Wang — [RefinementGuard: Counterexample-Directed Semantic Qualification for Hidden Agent-Tool Execution](http://arxiv.org/abs/2611.23611v1)
  <details><summary>📄 Abstract</summary>
  Tool runtimes can lower an agent-selected operation into a hidden parallel graph, reducing latency and context while risking semantic mistranslation. We introduce RefinementGuard: translation validation for hidden, effectful agent-tool lowerings, coupled to artifact-bound, fail-closed runtime admission. Qualification compares a candidate graph with an independent reference on isolated state using explicit parent-operation obligations. We evaluate two repository-level contracts, bug localization ...
  </details>

- **2026-11-17** — Xinyang Li, Chih-Hsuan Yang, Xiaolong Ma et al. — [Safe to Omit, Worth Omitting? Keeping the Answer and Cutting Latency When an LLM Agent Skips Another's Message](http://arxiv.org/abs/2611.23570v1)
  <details><summary>📄 Abstract</summary>
  In multi-agent systems, a receiver agent often waits for a helper agent's message (text or its latent KV cache), which can improve performance but adds latency. We study when a receiver agent can skip the message safely (the final answer rarely changes) and beneficially (the time saved exceeds the cost of deciding). Our mechanism reads the receiver agent's confidence without the message and uses a finite-sample test to certify a threshold at which, with high probability, at most 5% of skipped an...
  </details>

- **2026-11-17** — Hui Zhu, Saleh Zare Zade, Rafi Ibn Sultan et al. — [Beyond the Sink Token: Sink-Guided Key Editing in Vision-Language Models](http://arxiv.org/abs/2611.23516v1)
  <details><summary>📄 Abstract</summary>
  In vision-language models (VLMs), a few sink tokens attract a disproportionate share of attention. While previous studies have examined why these tokens attract attention, we investigate how the sink-key direction affects attention to image and question tokens. Across four probed VLMs, boosting the magnitude of positive sink-aligned components increases attention on average, whereas boosting negative components decreases it; these responses persist through later layers. This identifies the nativ...
  </details>

- **2026-11-17** — Amber He Wei, Shiyu Cheng, Andrew Clark et al. — [Verifiably Safe Decentralized Control via Event-Triggered Topology Switching](http://arxiv.org/abs/2611.23415v1)
  <details><summary>📄 Abstract</summary>
  This paper proposes a decentralized event-triggered topology-switching protocol for multi-agent systems under estimation uncertainty. We consider an intermittent communication setting in which each agent switches between connected and disconnected modes and makes communication decisions using locally computable certificates, while the closed-loop state is required to remain safe. The proposed protocol follows a safety-driven triggering principle in which agents reconnect before their certificate...
  </details>

- **2026-11-17** — Jiarui Cui, Boxun Yan — [RFBench: A Simulator-Grounded Multimodal Benchmark for Passive RF Layout Design and Understanding](http://arxiv.org/abs/2611.23410v1)
  <details><summary>📄 Abstract</summary>
  While multimodal language models can interpret diagrams and generate structured outputs, their capacity to connect passive radio-frequency (RF) design intent, layout geometry, and electromagnetic behavior remains largely untested. To address this gap, we introduce RFBench, a simulator-grounded dataset and benchmark for passive RF layout design and understanding. The dataset contains 10,000 two-port planar layouts simulated using ADS Momentum, with each layout represented by editable geometric pr...
  </details>

- **2026-11-17** — Yifan Chang, Jian Yang, Jiangnan Shao et al. — [MAVE: Reconstructing Editable 3D Blockouts from Film Shots](http://arxiv.org/abs/2611.22464v2)
  <details><summary>📄 Abstract</summary>
  Animated 3D blockouts support previsualization and provide structural conditions for video generation, but manually reconstructing them from reference videos is costly. This limits both their use by creators and the production of paired training data. We introduce MAVEBench, a benchmark of 50 film shots and 416 keyframes for evaluating camera motion, spatial layout, and character blocking. We propose MAVE, a video-to-blockout framework combining Metric observation, Agentic modeling, and evidence...
  </details>

- **2026-11-17** — Sara Amar — [MANGO Arena: Same Seeds, Different Chains Evaluating LLM Agents in a Disrupted Supply Chain](http://arxiv.org/abs/2611.23613v1)
  <details><summary>📄 Abstract</summary>
  We introduce MANGO Arena, an open-source testbed in which four LLM agents each run one company in a serial supply chain adapted from MANGO, a classroom factory-management game. The environment enforces hard rules (a truck limit, a no-credit cash constraint and production capacity), logs every blocked attempt to break them, and gives agents a public message board on which side payments are explicitly forbidden. This lets one environment measure three things at once: an economic outcome (the bullw...
  </details>

- **2026-11-17** — Sehyeon Lee, Yuchen Xia, Zhaoyang Hong et al. — [Towards Fair Resource Sharing in Agentic LLM Serving](http://arxiv.org/abs/2611.23558v1)
  <details><summary>📄 Abstract</summary>
  As LLM agents increasingly execute complex, multi-step tasks on shared inference infrastructure, resource contention across the end-to-end LLM serving stack causes severe and uneven slowdowns across agents. Existing agentic serving systems primarily optimize throughput and latency, with comparatively limited attention to fairness among concurrent agents. Although fairness has been studied in conventional LLM serving at the token and request levels, these approaches do not fully capture cumulativ...
  </details>

- **2026-11-17** — Jinjun Peng, Wailiang Zhao, Baishakhi Ray et al. — [Stability Does Not Mirror Plasticity: A Module-Level View of Declarative and Procedural Learning in Transformers](http://arxiv.org/abs/2611.23427v1)
  <details><summary>📄 Abstract</summary>
  Plasticity and stability in continual learning are typically studied at the entire-model level and in a task-agnostic manner, yet prior work has reported divergent conclusions across settings. Inspired by cognitive distinctions between declarative and procedural memory, we instead study how plasticity and stability vary across transformer modules and task types. In a controlled synthetic environment with clean measurement, we show a double dissociation: query-key (QK) and value-output (VO) proje...
  </details>

- **2026-11-17** — Amadeus Brandes — [Record Sufficiency: What a Decision Record Must Preserve When an Unsettled Claim Becomes an Operative Status](http://arxiv.org/abs/2611.23422v1)
  <details><summary>📄 Abstract</summary>
  Organisations keep evidence, logs and approvals, but often not the step by which an unsettled claim became an operative status, such as an accepted label or a released image, so later readers cannot tell what the status was allowed to mean. We call a decision record sufficient if it is true and a reader who has only the record and the items it cites can explain the status, bound it, re-derive it and challenge it. From these four uses we argue for ten questions a record must answer, map them onto...
  </details>

- **2026-11-17** — Chaipat Tirapongprasert, Rajarshi Das, Parijat Dube — [Tracking Representations in LLM Reasoning Traces for Iterated Games](http://arxiv.org/abs/2611.23403v1)
  <details><summary>📄 Abstract</summary>
  Large language model (LLM) agents achieve state-of-the-art performance across domains through chain-of-thought (CoT) reasoning. Despite their ubiquitous use, little is understood about the relationship between the externalized trace and the model's actual computation. We address this by investigating how LLM agents make decisions in iterative games with incomplete information. Using a series of mechanistic interpretability techniques, we find that the model forms and iteratively revises an inter...
  </details>

- **2026-11-17** — Hubert Strauss, Liam Fowl, Noam Razin — [Which Tokens, in What Order, and How Fast? A Theoretical Analysis of On-Policy Distillation Objectives](http://arxiv.org/abs/2611.23397v1)
  <details><summary>📄 Abstract</summary>
  On-policy distillation (OPD) trains a student language model to match a teacher model based on its own generations. When using OPD, one must choose whether to apply it at the sequence or token level and which divergence to minimize. However, despite the wide adoption of OPD in practice, the formal understanding of which OPD objective is appropriate for a given setting is limited. Toward addressing this gap, we theoretically analyze how the choice of OPD objective governs which tokens are priorit...
  </details>

- **2026-11-17** — Samuel Sisk, Xiaosong Du — [A Neural Envelope Method for Rapid Gradient-based Optimum Takeoff Trajectory Design](http://arxiv.org/abs/2611.23130v1)
  <details><summary>📄 Abstract</summary>
  Urban air mobility arises to mitigate ground traffic congestion. Multidisciplinary analysis and optimization (MDAO) has been introduced to reduce the energy consumption, thereby expanding aircraft performance. Surrogate-based MDAO lowers the cost of optimization, but multimodality disrupts global optimum search for both simulation-based and surrogate-based optimizations. Convex envelopes convert multimodal spaces into unimodal spaces, permitting efficient convex optimization; however, convexifyi...
  </details>

- **2026-11-17** — Yash Khare, Hunjun Shin, Mohit Singhal — [Longitudinal Multi-Dimensional Analysis of India-Pakistan Conflict Discourse on Reddit (2019-2025)](http://arxiv.org/abs/2611.22987v1)
  <details><summary>📄 Abstract</summary>
  Six India--Pakistan crises between 2019 and 2025, from the Pulwama attack to Operation Sindoor, have each been argued out on Reddit in India-aligned communities such as \texttt{r/india}, in Pakistan-aligned communities such as \texttt{r/pakistan}, and in general-audience ones such as \texttt{r/worldnews}. A strike can be a security issue in one community and a question of who was harmed in another. Computational studies of the conflict have concentrated on the February 2019 crisis, with some spl...
  </details>

- **2026-11-17** — Shaozhen Liu, Zhiwei Li, Jiayang Sun et al. — [RefCloth: Transferable Adversarial Tablecloths for Vision-Language-Action Models](http://arxiv.org/abs/2611.22736v1)
  <details><summary>📄 Abstract</summary>
  Closed-loop vision-language-action (VLA) policies rely continuously on multi-view cameras, yet existing visual attacks typically hijack sensor streams with 2D patches or alter target object meshes that require retraining when manipulation objects change. We introduce RefCloth, a framework that optimizes one persistent adversarial tablecloth on a frozen source policy and deploys it zero-shot across unseen tasks and target models without modifying task objects or cameras. Throughout manipulation, ...
  </details>

- **2026-11-17** — Jingyu Liu, Zongze Li, Zach Xu et al. — [RAG in a Trenchcoat: When Minimal Memory Is Enough for Agentic Systems, and When It Isn't](http://arxiv.org/abs/2611.22179v1)
  <details><summary>📄 Abstract</summary>
  Agentic memory research has accumulated extraction, supersession, reflection, and graph synthesis on top of retrieval-augmented generation. However, we found that almost none of those primitives earn their cost in our tested memory benchmarks: we show this with BRIDGE, a deliberately minimal RAG memory with chained observation notes, hybrid BM25 with cosine retrieval, and chronological rendering, which reaches parity within bootstrap CI with the prior SOTA on LongMemEval-S and BEAM, and beats th...
  </details>

- **2026-11-17** — Yixin Chen, Jianfeng Lin, Shizhao Wang — [A Butterfly-Inspired Agent Learns to Climb with Self-Generated Wingbeats](http://arxiv.org/abs/2611.22139v1)
  <details><summary>📄 Abstract</summary>
  Butterfly free climbing involves dynamic coupling between wing motion and unsteady aerodynamic forces that drive the animal's ascent. Four-wing coordination determines how these forces combine to support weight and direct propulsion. How aerodynamic feedback shapes such coordination remains difficult to establish when wing kinematics are prescribed in experiments and simulations. Here, we construct a virtual flight environment with rapid aerodynamic feedback and train a butterfly-inspired agent ...
  </details>

- **2026-11-17** — Shobhita Sundaram, Cansu Sancaktar, Phillip Isola — [Do LLM Agents Still Need to Be Told How to Self-Improve?](http://arxiv.org/abs/2611.23219v1)
  <details><summary>📄 Abstract</summary>
  LLM agents increasingly drive their own learning. Self-improvement methods delegate various components of model optimization to the models themselves. As models become more capable, this motivates a basic question: do these increasingly capable models still need us to specify how they should self-improve? In this paper we study an autonomous paradigm in which, given basic primitives, resources, and a general goal for self-improvement, agents construct their own self-learning algorithm for contex...
  </details>

- **2026-11-17** — Trizal Garg, Xuelong Fu, Dhruv Shah et al. — [AI Companions for Young Adult Caregivers: Practical Advice, Emotional Depth, and the Limits of Metric Evaluation](http://arxiv.org/abs/2611.23147v1)
  <details><summary>📄 Abstract</summary>
  Young adult caregivers (YACs) are individuals aged 18 to 25 currently taking care of a family member, partner, or friend facing chronic illness. AI companions designed specifically for YACs remain underexplored in prior works. We present Carebot, it uses an open-weight LLM (Gemma 3-27B) as its base model, on which we compared fine-tuning, retrieval-augmented generation (RAG), and a combination of both. The fine-tuning was performed based on an existing dataset of conversations with YACs and a ps...
  </details>

- **2026-11-17** — Jiajun Li, Leihan Zhang, Teng Zhang et al. — [CARE: Conversational Affective Response Retrieval for Internet Memes](http://arxiv.org/abs/2611.23005v1)
  <details><summary>📄 Abstract</summary>
  Conversational meme retrieval supports response selection in online communication, where relevance depends on both contextual meaning and affective expression. We study this task using two language-specific collections from Douban and Imgflip, containing 98,506 meme records across 5,583 discussion topics. Thread membership supplies weak relevance labels, while likes provide implicit ranking feedback. Automatically extracted sentiment, facial-expression indicators, and cross-modal consistency fea...
  </details>

- **2026-11-17** — Frank Nie, Ethan B. Liu, Yuan Zhu et al. — [Synergizing Evidence Retrieval and Utilization for Self-Improving Multimodal Scientific Document Reasoning](http://arxiv.org/abs/2611.22837v1)
  <details><summary>📄 Abstract</summary>
  Scientific document reasoning requires an agent to acquire and integrate evidence distributed across text, figures, and tables. Retrieval can identify relevant sources while missing complementary support, and answer-level feedback alone does not reveal whether an error stems from evidence acquisition or evidence use. We present an agentic Retriever--Perceiver--Reasoner framework for multimodal scientific document reasoning. The Retriever sequentially selects source-aligned evidence under a conte...
  </details>

- **2026-11-17** — Leonel Aguilar, Bartu Tuncay, Christoph Hoelscher — [Kolibri: Color Finds the Place, Refinement Sets the Pose for RGB-D Localization in Colored Point Clouds](http://arxiv.org/abs/2611.22829v1)
  <details><summary>📄 Abstract</summary>
  An agent or robot in a scanned building must locate its camera in rooms that no model saw during training. Point cloud registration methods can align each RGB-D frame with the building's colored point cloud, accurately but at a high cost. We observe that geometric refinement brings nearby initial poses to the same final pose, so the learned component only needs to find the place. Kolibri does this with a graph network of 55,712 parameters that describes 10 cm cubes of points, called cells, by th...
  </details>

- **2026-11-17** — Zhengfeng Yu, Tian Lan, Zhijing Wu et al. — [CrossEnv: Synthesizing Verifiable Cross-Environment Tasks for Long-Horizon Agent Training](http://arxiv.org/abs/2611.22777v1)
  <details><summary>📄 Abstract</summary>
  Executable synthetic environments provide scalable training tasks and verifiable feedback for long-horizon agents. Existing environment synthesis methods primarily generate tasks within individual environments. However, these tasks do not adequately capture real-world interactions across services, where actions in one service depend on information obtained from another. Synthesizing such tasks is challenging because data generated across environments must remain consistent to support executable ...
  </details>

- **2026-11-17** — Do Xuan Long, Long T. Le, Yiwen Song et al. — [FVScore: Specification-Driven Neuro-Symbolic Video Evaluation](http://arxiv.org/abs/2611.22673v1)
  <details><summary>📄 Abstract</summary>
  We introduce Faithfulness Video Score (FVSCORE), a neuro-symbolic framework for specification-driven video generation evaluation. Existing evaluators rely on holistic MLLM judgments or vision-language metrics, yet aligning their scores with human judgments and tracing them to specific temporal violations remain open challenges. FVSCORE addresses these limitations by compiling each video into explicit propositions capturing prompt requirements and implicit propositions capturing unstated physical...
  </details>

- **2026-11-17** — Guanqiao Chen, Wei Jiang, Shu Zhang et al. — [Right Diagnosis, Unsafe Route: Auditing Clinical AI Decision Trajectories and Corrective Oversight for Validity and Potential Harm](http://arxiv.org/abs/2611.22612v1)
  <details><summary>📄 Abstract</summary>
  A clinical AI system can reach a correct final diagnosis through intermediate decisions that could have harmed the patient, and can repair an error while introducing new risks. Most evaluations score final diagnoses; even stepwise benchmarks, which release a case's evidence over time, score whether systems reach the right diagnosis or gather the right information, not whether the decisions a patient passes through are safe. We make patient safety the target of stepwise evaluation. A trajectory a...
  </details>

- **2026-11-17** — Jialin Chen, Xiaochen Zhao, Aili Wang — [DAQ: Decision-Aligned Post-Training Quantization for Spiking Transformers](http://arxiv.org/abs/2611.22611v1)
  <details><summary>📄 Abstract</summary>
  Spiking transformers combine attention-based representation learning with sparse spike communication, yet their weights and membrane variables still incur substantial storage and computation overhead. Post-training quantization (PTQ) offers a practical way to reduce these overheads, but preserving neuronal firing under weight and membrane quantization remains challenging. In this paper, we propose Decision-Aligned Post-Training Quantization (DAQ), a method that calibrates the quantizers to align...
  </details>

- **2026-11-17** — Zhuohan Cai, Zhangxuan Gu, Runze Li et al. — [PACT: Plan-Action Consistency Training by Preserving Correct Plans and Repairing Actions in GUI Agents](http://arxiv.org/abs/2611.22591v1)
  <details><summary>📄 Abstract</summary>
  GUI agents can formulate a correct immediate plan in their reasoning yet emit an action that fails to execute it, creating an execution gap. This recurring mismatch undermines reliable task completion, as a single execution error can derail a multi-step workflow. In outcome-supervised reinforcement learning, broadcasting a negative response-level advantage across all generated tokens risks penalizing valid planning together with erroneous execution. To address this credit-assignment conflict, we...
  </details>

- **2026-11-17** — Yanchao Li, Jiaqing Xie, Ben Gao et al. — [Disagree to Prune: Reallocating Visual Tokens Where a Small VLM Dissents](http://arxiv.org/abs/2611.22472v1)
  <details><summary>📄 Abstract</summary>
  Visual token pruning speeds up large vision-language models (VLMs) by keeping only a part of their visual tokens. Most existing methods improve the ranking of the tokens and then answer every question once with the same budget. With strong rankings, pruning hurts only a few questions, and signals computed on the kept tokens see little of what it removed. We find that, on most of these questions, a small VLM given the full image disagrees with the pruned answer, since it still sees the missing ev...
  </details>

- **2026-11-17** — Yifan Chang, Jian Yang, Jiangnan Shao et al. — [MAVE: Reconstructing Editable 3D Blockouts from Film Shots](http://arxiv.org/abs/2611.22464v1)
  <details><summary>📄 Abstract</summary>
  Animated 3D blockouts support previsualization and provide structural conditions for video generation, but manually reconstructing them from reference videos is costly. This limits both their use by creators and the production of paired training data. We introduce MAVEBench, a benchmark of 50 film shots and 416 keyframes for evaluating camera motion, spatial layout, and character blocking. We propose MAVE, a video-to-blockout framework combining Metric observation, Agentic modeling, and evidence...
  </details>

- **2026-11-17** — Aniruddha Ghosh, Ujjal Debnath — [Gravitational Light Deflection via Fractional Calculus and Chebyshev Polynomial Approximation](http://arxiv.org/abs/2611.22459v1)
  <details><summary>📄 Abstract</summary>
  We develop a fractional-calculus-based framework for evaluating gravitational light deflection in static, spherically symmetric spacetimes. By introducing a suitable transformation of the radial coordinate, the deflection integral is recast into an Abel-type integral equation, from which the associated kernel is reconstructed using fractional integration. The leading singular behaviour near the photon sphere is isolated analytically, and the remaining regular part is approximated by a finite Che...
  </details>

- **2026-11-17** — Zipeng Chen, Xinyu Lin, Yuliang Sun et al. — [More Than a Score: Reinforcement Learning with Verbalized Feedback for Generative Recommendation](http://arxiv.org/abs/2611.22410v1)
  <details><summary>📄 Abstract</summary>
  Large language models (LLMs) are increasingly used for generative recommendation, where recommended items are generated directly from users' interaction histories. To further improve recommendation quality, reinforcement learning (RL) has been applied to align these models with recommendation objectives. However, existing RL methods rely on scalar rewards to implicitly guide exploration. These rewards do not specify which aspects of a candidate conflict with the user's preferences or how the nex...
  </details>

- **2026-11-17** — Naoto Tsuji — [Strong eigenstate thermalization in Singer-cycle Clifford circuits](http://arxiv.org/abs/2611.22391v1)
  <details><summary>📄 Abstract</summary>
  Eigenstate thermalization hypothesis (ETH) provides a central framework for understanding thermalization in isolated quantum systems. Recently, the infinite-temperature ETH has been established for almost all Floquet eigenstates in linear feedback shift register quantum circuits. Here we introduce brickwork Clifford circuits with $L$ qubits where the induced transformation of Pauli operators is represented by an irreducible symplectic matrix over the finite field $\mathbb F_2$ of the maximal ord...
  </details>

- **2026-11-17** — Xiaoqian Zhang, Zhihao Zhang — [Cross-Modal StateKV Injection for Communication in Multi-LLM Systems across Temporal Segments](http://arxiv.org/abs/2611.22304v1)
  <details><summary>📄 Abstract</summary>
  Video understanding with multiple multimodal language models requires a communication interface that can transfer complementary visual observations. Text-based communication is interpretable, but introduces an intermediate generation stage and can omit information relevant to subsequent reasoning. We study Cross-Modal StateKV Injection, a provider--carrier framework that communicates through key--value (KV) states at visual-token positions. Provider models observe complementary video frames; the...
  </details>

- **2026-11-17** — Xianyao Li, Ruitong Tian, Rui Min et al. — [Perception into Imagination: Executable Memory for World Models](http://arxiv.org/abs/2611.22294v1)
  <details><summary>📄 Abstract</summary>
  Physical agents must use what they previously saw or touched after visibility or contact is lost. Their actions change the implications of these remembered facts. We introduce executable perceptual memory (EPM), a world-model framework that advances explicit perceptual state alongside neural latent dynamics during imagination. Its evolving read-out informs reward prediction, value estimation and policy learning. We align reward inputs with the transitions that produced them and supervise the rew...
  </details>

- **2026-11-17** — Kaixin Li, Meng Luo, Yanlin Li et al. — [When the World Is the Test Suite: Agentic Intelligence for the Physical World](http://arxiv.org/abs/2611.22291v1)
  <details><summary>📄 Abstract</summary>
  Coding agents built to repair software now write, test, and repair programs for robots, laboratories, and industrial controllers. Unlike in software engineering, no test suite comes with the code. Whether a program works must be established by running it on a robot, in a physics simulator, or through the policies it helps to train, and such evidence is costly to obtain and can itself be wrong. As these agents take on more physical tasks, how their programs are judged matters as much as how they ...
  </details>

- **2026-11-17** — Qi Shao, Zhihao Cao, Shuhao Zhai et al. — [PhyVGGT: Feed-Forward Articulated Object Reconstruction from Monocular Videos](http://arxiv.org/abs/2611.22244v1)
  <details><summary>📄 Abstract</summary>
  Reconstructing an articulated object with its 3D movable parts, joint parameters and unseen articulation states from an uncalibrated monocular video is essential for robot manipulation and interactive digital twins. Existing per-scene optimisation methods require minutes to hours and external depth or camera poses, whereas feed-forward 3D foundation models reconstruct dense point maps in one pass without segmenting movable parts or inferring joints. Even on these monocular point maps, regressing...
  </details>

- **2026-11-17** — Qi Shao, Zhihao Cao, Shuhao Zhai et al. — [CoSphere-SLAM: Multi-Agent Panoramic Gaussian Splatting SLAM with Spherical Loop Closure](http://arxiv.org/abs/2611.22235v1)
  <details><summary>📄 Abstract</summary>
  Dense collaborative mapping is essential for search and rescue, building inspection, and warehouse automation, where panoramic cameras capture the entire surroundings in a single frame. Unlike pinhole agents that share views only at similar headings, panoramic agents observe overlapping scenes at any 3D orientation, yet searching full rotations also produces mutually consistent false loop closures across distinct symmetric rooms. Moreover, continuous monocular scale drift splits rigidly merged m...
  </details>

- **2026-11-17** — Shoaib Hussain, Mostafa Farrokhabadi, Hamidreza Zareipour — [Safely Mitigating Grid Imbalance: A Hybrid Distributional Wide-Margin Recourse Approach](http://arxiv.org/abs/2611.22220v1)
  <details><summary>📄 Abstract</summary>
  This paper proposes the Multi-Agent Distributional Wide-Margin Policy Gradient (MADWMPG) framework: a dual-policy hybrid imitation and safe reinforcement learning (IL-SRL) method designed for safely mitigating grid imbalance in multiphase active distribution networks with distributed soft open points (SOPs). The framework comprises a wide-margin constraint barrier recourse (WCBR) module that seeks the maximal separation of constraint-compliant and unsafe actions and learns to proactively suppres...
  </details>

- **2026-11-17** — Zhiyuan Yang, Jiahao Cheng, Vincent Quoc-Huy Trinh et al. — [SRED: Sparse Regional Evidence Distillation Across Magnifications in Whole-Slide Imaging](http://arxiv.org/abs/2611.22189v1)
  <details><summary>📄 Abstract</summary>
  In computational pathology, high-magnification whole-slide image analysis preserves tissue detail but requires encoding many patches, whereas lower magnification reduces computation by covering a higher field of view per patch while sacrificing detail. Existing cross-magnification distillation matches features that often encode detail unreachable by low-magnification input, sometimes requiring slide-level labels that limit scalability. To address those issues, we introduce Sparse Regional Eviden...
  </details>

- **2026-11-17** — Yanju Chen, Hanzhi Liu, Ruizhe Qian et al. — [From Sorry to QED: Refining LLM Math Proofs via Angelic Execution](http://arxiv.org/abs/2611.22103v1)
  <details><summary>📄 Abstract</summary>
  Large language models (LLMs) can now generate Lean proof scripts that capture the high-level structure of many mathematical arguments. However, these scripts frequently fail on complex theorems: a single missing side condition or misapplied lemma can cause the prover to abort early and discard an otherwise viable proof outline. This paper presents MathEye, a framework that converts imperfect LLM-generated proof scripts into fully verified Lean proofs by combining symbolic reasoning with minimal ...
  </details>

- **2026-11-17** — Ibrahim Albool, Yasser Shoukry — [BernBRS: Certified Backward Reachability for Deep Bernstein Neural Networks](http://arxiv.org/abs/2611.22083v1)
  <details><summary>📄 Abstract</summary>
  Ensuring the safety of complex neural network systems requires mathematically rigorous verification. While backward reachability analysis is a critical tool for identifying safe initial states, computing tight, formal bounds remains notoriously difficult to scale. Recent advancements have demonstrated that DeepBern-Nets neural networks utilizing Bernstein polynomial activation functions possess advantageous mathematical properties that enable exceptionally fast and tight forward reachability ana...
  </details>

- **2026-11-17** — Eleftherios Triantafyllidis, Filippos Christianos, Zhibin Li et al. — [WATERFALL: Workflow for Adaptive Training with Evolutionary Reward Formulation and Automated Learning Loops](http://arxiv.org/abs/2611.22854v1)
  <details><summary>📄 Abstract</summary>
  Reward design remains a central bottleneck in reinforcement learning (RL), particularly in sparse-reward, long-horizon and partially observable settings requiring dependency chaining, memory, and deceptive affordance disambiguation. While recent foundation-model approaches reduce manual reward engineering, most assume goal-conditioning, task descriptions, expert demonstrations, or ground-truth metrics. These assumptions are problematic in partially observable environments, where task-relevant ob...
  </details>

- **2026-11-17** — Junyi Fan — [Can Activation Steering Substitute for Prompt-Based Affective Priming in LLM Digital Twins?](http://arxiv.org/abs/2611.22738v1)
  <details><summary>📄 Abstract</summary>
  Affective priming -- asking participants to write about a recalled event, such as a time they felt grateful or lacked control, and then measuring the induced state and its spillover onto related judgments -- is a standard way to manipulate emotion in the social sciences, and it also shifts the responses of LLM-based digital twins. The writing task, however, requires generating a full text. We test whether activation steering can replace it. Using Llama-3.1-8B-Instruct on 100 personas in two doma...
  </details>

- **2026-11-17** — Daniil Li, Mars Davletshin, Vadim Klyzhenko et al. — [HADVQ: Hessian Aware Directional Vector Quantization](http://arxiv.org/abs/2611.22721v1)
  <details><summary>📄 Abstract</summary>
  Ultra-low-bit quantization of large language models is a challenging task because aggressive compression severely distorts model parameters and disproportionately harms a small number of highly sensitive channels. We present a vector quantization method tailored for this regime. Our approach begins with random preconditioning, which regularizes the weight space and makes it more amenable to quantization. We then represent weights in polar coordinates and decouple the quantization of directions a...
  </details>

- **2026-11-17** — Lechen Zhang, Chenyuan Chen, Muxin Zhou et al. — [Body Schema Policy: Body as the Vision-Action Interface for Efficient Robot Loco-Manipulation](http://arxiv.org/abs/2611.22713v1)
  <details><summary>📄 Abstract</summary>
  Currently, robots can learn whole-body loco-manipulation through scale: the strongest policies have billions of parameters and still need task-specific fine-tuning. Humans have limited processing capacity, yet learn and act efficiently through a body schema that organizes what they see and how they move. We introduce Body Schema Policy (BSP), an imitation learning policy that builds such a schema into the vision-action interface. Its latent body schema places joint and link tokens on the robot's...
  </details>

- **2026-11-17** — Mingcheng Zhu, Wentian Xu, Tao Lin et al. — [VLM-guided Grounding Expert for Generalised Referring Expression Comprehension](http://arxiv.org/abs/2611.22625v1)
  <details><summary>📄 Abstract</summary>
  Generalised referring expression comprehension (GREC) aims to identify and localise the zero, one or multiple objects referred to by a language expression. In robotic manipulation, grounding also needs to remain accurate when requests for the same objects are paraphrased or embedded in additional context in robotics. However, grounding expert models are sensitive to instruction variation, while generative vision--language models (VLMs) struggle with complete target recovery and rejection of abse...
  </details>

- **2026-11-17** — Dunhan Li, Leilei Gan, Lirong Gao et al. — [EviDARL: Evidence-Centric Dual-Agent Reasoning via Alternating Reinforcement Learning for Multi-Table Question Answering](http://arxiv.org/abs/2611.22310v1)
  <details><summary>📄 Abstract</summary>
  Despite advances in LLM-based table reasoning, most studies focus on single-table settings. Multi-table QA requires multi-hop reasoning over complex table relationships and evidence dispersed across long contexts, often without verifiable intermediate traces. To address these challenges, we introduce EviDA, an evidence-centric dual-agent framework comprising an Evidence Construction Agent and a Reasoning and Answering Agent. The Evidence Construction Agent generates and executes table-manipulati...
  </details>

- **2026-11-17** — Hang Zhang, Qijian Tian, Yuan Xie et al. — [DailyBrick: Language-Guided Synthesis of Brick Assembly Instructions](http://arxiv.org/abs/2611.22132v1)
  <details><summary>📄 Abstract</summary>
  Generating a LEGO model from a user request is more than a plausible 3D shape generation. LEGO models require physical support per brick, and each brick should be placed unblocked. Current methods address this issue by training an expert large language model. We reduce the problem of generating extremely long context on all brick connections to that of writing a program that builds LEGO models like a human, considering each intermediate step could be executed. We introduce DailyBrick , a multi-s...
  </details>

- **2026-11-17** — Hai Huang, Bartosz Żuk, Rassul Magauin et al. — [Structure--Residual Inductive Biases for Language Model Pretraining](http://arxiv.org/abs/2611.23197v1)
  <details><summary>📄 Abstract</summary>
  Next-token prediction is relied upon to learn both predictive behavior and internal representations. We ask whether representation structure itself should be an explicit inductive bias. Motivated by the two-part coding view of Kolmogorov complexity, we study a structure--residual principle in which a representation separates structure from realization detail. We instantiate this principle in two complementary ways. Boundary Bottleneck Concept (BBC) routes information from token segments through ...
  </details>

- **2026-11-17** — Hansang Lee — [Say Less, Hallucinate Less? Diagnosing and Restoring Object Coverage in Preference-Optimized Vision-Language Models](http://arxiv.org/abs/2611.23179v1)
  <details><summary>📄 Abstract</summary>
  Preference optimization (PO) is the standard way to reduce object hallucination in large vision-language models. We find that four public PO checkpoints of LLaVA-1.5-7B also lower object coverage. They name fewer object categories, and their lower hallucination rates bring no significant gain in set-level object F1 on CHAIR. We therefore ask how much of the PO gain the base model can reproduce by stopping earlier. A positive end-of-sequence (EOS) logit bias lets the base model reach the recall o...
  </details>

- **2026-11-17** — A. V. Nokhrin, M. K. Chegurov, N. V. Melekhin et al. — [Localized corrosion resistance of ultrafine-grained austenitic steel 321 obtained by Rotary Swaging: The role of annealing conditions](http://arxiv.org/abs/2611.23160v1)
  <details><summary>📄 Abstract</summary>
  The object of this study was austenitic steel 321, which has an ultrafine-grained (UFG) structure formed by Rotary Swaging (RS). RS leads to the formation of a two-phase macroscopically heterogeneous and, at the same time, a microscopically homogeneous UFG structure with an increased content of martensite. It has been shown that secondary TiC nanoparticles form in the annealing at 450-550C, the reverse transformation of martensite into austenite occurs at 550-650C, and recrystallization begins a...
  </details>

- **2026-11-17** — Parmitha Vangapandu, Jonnakuti Pavan Kumar, Sathwik Narkedimilli et al. — [Where Should Physics Enter? Information, Identifiability and Calibration in Probabilistic Sea Surface Temperature Forecasting](http://arxiv.org/abs/2611.23129v1)
  <details><summary>📄 Abstract</summary>
  Advection-diffusion priors are a common way to make neural sea surface temperature (SST) forecasts physics-informed. We test where such a prior must enter a heteroscedastic ConvLSTM to help, using daily NOAA OISST v2.1 for the Bay of Bengal (1982-2024) and a synthetic benchmark on the same grid with known currents of controlled strength. (i) On real data, a soft advection-diffusion residual with a learned velocity gives no reliable benefit (lead-15 CRPS -0.007 degrees C, 95% interval [-0.022, +0...
  </details>

- **2026-11-17** — Mundur V N Murthy, Usha Devi A R — [Causality, determinism and predictability: Probing nature through classical and quantum eyes](http://arxiv.org/abs/2611.23128v1)
  <details><summary>📄 Abstract</summary>
  In this article, mainly focussed on students and interested readers, we discuss how the understanding of causality, determinism and predictability is transformed as we move from the classical world view to the quantum description. We first explain how determinism and predictability operate in classical dynamics and outline the notion of causality. A paradigm shift occurs within the framework of quantum mechanics where we have to revisit, and even give up, the notions of determinism, predictabili...
  </details>

- **2026-11-17** — Basavaraj R M, Harshal Chandel — [The Illusion of Grounding: Do Vision-Language Models Weigh Retrieved Text and Images Like an Ideal Observer?](http://arxiv.org/abs/2611.23127v1)
  <details><summary>📄 Abstract</summary>
  Retrieval-augmented vision-language models (VLMs) answer from two sources of evidence that can each fail: the retrieved text can be wrong or noisy, and the image can be degraded or contradicted. We introduce GIB-200K, 200,000 image-question items built from COCO and Visual Genome, each expanded into controlled stress conditions: hard-negative retrieval noise (1-20 documents), visual ambiguity (Gaussian and motion blur, low-resource crops) and cross-modal conflict with counterfactual flip pairs. ...
  </details>

- **2026-11-17** — Pietro Cagnasso, Daniele Kopyshevskiy, Edouard Oyallon et al. — [SPICE: Sparse Parameter Gossip for LLM Pretraining](http://arxiv.org/abs/2611.23053v1)
  <details><summary>📄 Abstract</summary>
  Pretraining language models across geographically distributed resources requires communication-efficient methods that operate under limited and variable internet bandwidth. Decentralized training replaces global collectives with peer exchanges, but full-model messages make larger peer neighborhoods costly. We introduce SPICE, which combines sparse parameter gossip with error feedback through corrected parameter values that remain directly interpretable as peer neighborhoods change. These sparse ...
  </details>

- **2026-11-17** — Moriya Dechtiar, Daniel Martin Katz, Michael J. Bommarito et al. — [RagHarnessDebugger: Jev-Guided Agentic RAG in Contract Inference Repair Auditing](http://arxiv.org/abs/2611.22991v1)
  <details><summary>📄 Abstract</summary>
  Agentic systems using retrieval-augmented generation (RAG) must repair their own answers by gathering more evidence, testing alternative policies and deciding if, when, and what repairs are needed. Yet how do we know if a system's repairs are working when metrics like accuracy can be misleading? We present RagHarnessDebugger, a framework that records every repair decision in a Jev-guided harness for contract inference and audits the record to facilitate complete debugging of all decisions taken ...
  </details>

- **2026-11-17** — Robin Sharma, Parisa Suchdev — [How Web Research Agents Interpret User Priorities](http://arxiv.org/abs/2611.22989v1)
  <details><summary>📄 Abstract</summary>
  Web research agents gather information online and write cited reports, including financial analysis. Users can state a priority to guide this research, but a priority may not say how to judge the options, leaving the agent to choose the criteria. We examine how two such agents, built on OpenAI and Anthropic models, interpret a stated priority. In 36 runs, the agents compared Microsoft and Alphabet as businesses. Prompts asked for special attention to growth or resilience, or gave no priority. We...
  </details>

- **2026-11-17** — Michael Smith, Frank P. Ferrie — [Is model self-assessment enough for diverse LVLM ensembles?](http://arxiv.org/abs/2611.22956v1)
  <details><summary>📄 Abstract</summary>
  Ensembles of diverse Large Vision Language Models have demonstrated performance beyond that of single models across multiple datasets and tasks. However, the necessary aggregation process usually relies on training, parameter fitting, or complex task-specific pipelines. Furthermore, evaluation is limited, making a fair comparison difficult. We create a unified pipeline where we perform candidate response selection: we build an ensemble by selecting the best answer from a set provided by differen...
  </details>

- **2026-11-17** — Viktor A. Balashov, Daniil S. Antonenko — [Fiberpose: state-of-the-art fiber morphometry and instance segmentation with a distance-transform neural network](http://arxiv.org/abs/2611.22953v1)
  <details><summary>📄 Abstract</summary>
  Analysis of fibrous structures in SEM images is a routine task in biomedical engineering and materials science. However, most available methods for fiber quantification still rely on classical image binarization followed by simple post-processing. These approaches often produce unreliable results in images with weak boundaries, heterogeneous contrast, and densely packed fibers. Here, we introduce Fiberpose, a framework that reformulates fiber analysis as direct regression of a smooth distance-tr...
  </details>

- **2026-11-17** — Md Tahmid Rahman Laskar, Xue-Yong Fu, Shashi Bhushan TN — [Can Decision Models Replace LLMs in Real-World Contact Center Classification and Judging Tasks?](http://arxiv.org/abs/2611.22949v1)
  <details><summary>📄 Abstract</summary>
  Contact center systems often need to make bounded decisions, such as identifying a caller's intent, retrieving the knowledge-base article that answers a query, assessing agent compliance, or judging the output of AI models used in production. Decision models return a typed answer and its probability directly, making them a promising cost-effective alternative to generative Large Language Models (LLMs) in such bounded conversational tasks. However, their effectiveness in real-world contact center...
  </details>

- **2026-11-17** — Fırat Öncel, Cem Subakan, Mirco Ravanelli et al. — [The Kernel Reality Check: Benchmarking and Distilling Efficient Attention at Scale](http://arxiv.org/abs/2611.22947v1)
  <details><summary>📄 Abstract</summary>
  Kernelized attention methods, which aim to replace the $O(N^2)$ complexity of softmax attention with $O(N)$ alternatives, have been the focus of intense research in the last five years. Despite growing interest, systematic evaluations and fair comparisons across approaches and scales are still missing. We analyze kernelized attention in two halves and highlight prominent limitations on each. On efficiency, FlashAttention achieves lower memory consumption and faster wall-clock time than SOTA kern...
  </details>

- **2026-11-17** — Zerui Yang, Quan Xue, Miaomiao Dong et al. — [Done, But Still Working: Anytime Evaluation of When Coding Agents Should Stop](http://arxiv.org/abs/2611.22901v1)
  <details><summary>📄 Abstract</summary>
  Coding agents often continue working after their own tests pass. Does this additional work improve the patch, and how much could be saved by stopping earlier? We study these questions through anytime evaluation: replaying recorded runs, scoring intermediate patches with hidden tests, and measuring the cost incurred at each step. For policies that only stop a run or select an earlier patch, this allows paired comparisons without generating new trajectories, provided replay preserves the relevant ...
  </details>

- **2026-11-17** — Lei Wu, Jiashuai Liu, Di Zhang et al. — [SlideJev: Order-Stable and Tissue-Grounded Jev Decisions for Whole-Slide Pathology](http://arxiv.org/abs/2611.22879v1)
  <details><summary>📄 Abstract</summary>
  Whole-slide visual question answering (VQA) offers a natural-language interface to pathology, allowing diagnostic and phenotypic questions to be answered directly from tissue slides. However, current vision-language models (VLMs) rely heavily on linguistic priors: their answers are sensitive to the order of the candidate answers, and can be reached through shortcuts that bypass the tissue evidence. To address these challenges, we introduce SlideJev, a framework that separately verifies candidate...
  </details>

- **2026-11-17** — Xueping Gao — [When Passing Checks Do Not Establish Completion: Evidence Interpretation in Coding Agents](http://arxiv.org/abs/2611.22835v1)
  <details><summary>📄 Abstract</summary>
  Verification procedures in coding agents must preserve execution facts, interpret their scope and discharge checking obligations. We study these responsibilities through qualified repository checks, controlled evidence consumers and executable workflows. A prospective thirteen-task factorial study finds that correct reported facts need not yield the requested finite verdict. Conversely, all 122 delivered labels in a held-out receipt-supply study are correct, while sixteen responses misreport fac...
  </details>

- **2026-11-17** — Osnat Mokryn, Oshrat Ayalon, Noga Dines et al. — [AI as Anchor: How Interview Sequencing Relates to the Appropriation of Synthetic Stakeholder Voices in Design Education](http://arxiv.org/abs/2611.22740v1)
  <details><summary>📄 Abstract</summary>
  Designers increasingly use large language models to simulate stakeholder conversations. Yet it remains unclear how AI-Simulated Stakeholders (AIS) are taken up when used alongside human stakeholder engagement. We report a field study in a single-institution, single-semester design course in which 8 teams (N=21) constructed, evaluated, and peer-reviewed an initial AIS. Then, the teams interviewed both AIS and human stakeholders in two sequences: AIS-first or human-first. Drawing on interview tran...
  </details>

- **2026-11-17** — Jane SiNan Long, Akhil Uniyal, Yosuke Mizuno et al. — [Temporal polarization properties of accretion flows into supermassive black holes: INSANE as an alternative](http://arxiv.org/abs/2611.22707v1)
  <details><summary>📄 Abstract</summary>
  Temporal variability and polarization provide unique diagnostics of the magnetic field structure and plasma dynamics in accretion flows around supermassive black holes. We investigate the temporal polarization properties of horizon-scale emission using general relativistic magnetohydrodynamic (GRMHD) simulations coupled with polarized general relativistic radiative transfer (GRRT) for three accretion states: Standard and Normal Evolution (SANE), Magnetically Arrested Disk (MAD), and an intermedi...
  </details>

- **2026-11-17** — Ahmad Samuel Gali, Tadesse Destaw Belay, Idris Abdulmumin et al. — [AfriNORM: An Evaluation Benchmark for Normative Reasoning of LLMs Across African Cultures](http://arxiv.org/abs/2611.22580v1)
  <details><summary>📄 Abstract</summary>
  Large language models (LLMs) are increasingly deployed across various sectors. However, current evaluation benchmarks are insufficient to assess the applicability of these models in local African contexts, as most focus on linguistic fluency (grammar/translation) rather than cultural competence. The few existing benchmarks that measure general knowledge or social conventions do not capture the African deontic modality, i.e., the strict norms and taboos that govern diverse social interactions. In...
  </details>

- **2026-11-17** — Yoonho Choi, Taehyeon Han, Seonghyeon Lee — [JET: Just-Enough Exploration Tuning for Efficient Tool-Calling Agents in Repository-Level Question Answering](http://arxiv.org/abs/2611.22539v1)
  <details><summary>📄 Abstract</summary>
  In repository-level question answering (QA), an agent explores a code repository with tools and should answer a question once enough information is gathered. Nevertheless, we find that LLM agents often continue to invoke tools even after the gathered information is already sufficient to answer. We call this phenomenon over-exploration. Moreover, even though existing methods improve task performance through supervised fine-tuning (SFT) on expert trajectories, SFT also propagates the over-explorat...
  </details>

- **2026-11-17** — A. Iosevich, E. Liflyand — [Subharmonic functions and convexity of the Radon transform, with applications to the Fourier transform](http://arxiv.org/abs/2611.22521v1)
  <details><summary>📄 Abstract</summary>
  Integrating a subharmonic function over parallel hyperplanes produces a convex function of the signed distance from the origin, provided that the function is absolutely integrable on bounded slabs. We prove this first for twice continuously differentiable functions and then without any smoothness assumption, and the same argument applies to a function defined only on a slab. Examples on the disk explain why subharmonicity on a bounded convex domain does not imply convexity of the integrals over ...
  </details>

- **2026-11-17** — Xuyue Huang, Guanbo Huang, Jiasong Feng et al. — [CutAgent: Creative-Gene-Driven Planning and Experience-Guided Self-Refinement for High-CTR E-commerce Advertising Video Creation](http://arxiv.org/abs/2611.22418v1)
  <details><summary>📄 Abstract</summary>
  E-commerce advertising video creation requires both high-level creative planning and reliable multi-modal production. However, existing methods often map product attributes directly to scripts or editing decisions without explicitly modeling advertising strategies, narrative structures, and production styles. They also have limited ability to reuse past production failures. To address these limitations, we propose $\textbf{CutAgent}$, a dual-agent framework that formulates advertising video crea...
  </details>

- **2026-11-17** — Siqing Fu, Xin Liu, Yuhan Tang et al. — [KD-DSE: A Knowledge-Driven LLM Framework for Fast Microarchitecture Design Space Exploration](http://arxiv.org/abs/2611.22411v1)
  <details><summary>📄 Abstract</summary>
  Domain-specific architectures have made design space exploration (DSE) a bottleneck of processor design, yet each candidate costs a full simulation, so exhaustive search is out of reach. Surrogate models need thousands of simulations before they predict reliably, and LLM agents that search directly hallucinate, lack cold-start architectural knowledge, and follow a fixed per-round policy. We present KD-DSE, a knowledge- driven LLM framework for fast microarchitecture DSE. KD- DSE couples a five-s...
  </details>

- **2026-11-17** — Hedwig Oldenhof, Laura Rosseel, Anna Wegmann et al. — [Comparing Implicit and Explicit Language Attitudes toward the Dutch multiethnolect Straattaal in Humans and Large Language Models](http://arxiv.org/abs/2611.22335v1)
  <details><summary>📄 Abstract</summary>
  While language attitudes have been extensively studied in humans, the extent to which large language models (LLMs) encode similar associations between language varieties and social attributes remains unclear. Contemporary sociolinguistic research distinguishes between explicit attitudes, which stem from deliberative processing, and implicit attitudes, which arise from automatic processing. This study investigates whether LLMs exhibit human-like implicit and explicit language attitudes toward the...
  </details>

- **2026-11-17** — Yingtong Dou, Shubham Jain, Junpeng Wang et al. — [VRLLM: Turning LLMs into Powerful Tabular Classifiers](http://arxiv.org/abs/2611.22308v1)
  <details><summary>📄 Abstract</summary>
  Large Language Models (LLMs) have shown strong performance on text, but whether pretrained LLMs are effective for large-scale tabular classification remains unclear, as many previous works demonstrate that LLMs' tabular data classification performance falls behind tree-based models or neural architectures designed for tabular data. At Visa Research, we managed to fine-tune a pretrained Llama 3.2 1B LLM on billions of rows of labeled tabular data and make it outperform a wide array of tabular cla...
  </details>

- **2026-11-17** — Yishu Ji, Zhihan Jiang, Will Ke Wang et al. — [OAK-Mind: Zero-Training Mental Health Change Inference from Passive Sensing via Knowledge-Grounded Multi-Agent LLMs](http://arxiv.org/abs/2611.22248v1)
  <details><summary>📄 Abstract</summary>
  Wearable and smartphone sensors capture behavioral signals associated with mental health, yet inferring mental health outcomes from these signals has traditionally relied on supervised models requiring labeled data and offering limited insight into their predictions. Large language models (LLMs) offer new opportunities to reason over behavioral evidence, but existing LLM-based approaches to passive sensing have largely continued to rely on task-specific fine-tuning or sensor-specific pretraining...
  </details>

- **2026-11-17** — Sikun Xu, Raphael Thomadsen, Dennis J. Zhang et al. — [SOTA or Luck? The Winner's Curse in LLM Leaderboards](http://arxiv.org/abs/2611.22227v1)
  <details><summary>📄 Abstract</summary>
  Public LLM leaderboards guide model evaluation and adoption, yet the reported performance of top-ranked models can be systematically overstated. This leaderboard winner's curse arises because ranking noisy benchmark scores rewards sampling luck alongside genuine ability. The same selection effect can distort scores throughout the leaderboard, a phenomenon we call the rank-induced bias. We develop an $m$-out-of-$N$ bootstrap to correct for this bias. It assumes a fixed model pool with independent...
  </details>

- **2026-11-17** — Runxun Zhang, Onofrio Antonio Catalano, Jinqiao Wang et al. — [Not All Evidence Is Admissible: Evidence Governance for Tool-Augmented Medical Agents](http://arxiv.org/abs/2611.22169v1)
  <details><summary>📄 Abstract</summary>
  Tool-augmented medical agents treat whatever their tools return as evidence. We show that this default is costly: medical tools fail silently, and a frozen reasoner cannot ignore what enters its context, so many cases it would have answered correctly are flipped to wrong once tool outputs are added. We call this evidence hijacking. $\mathcal{V}$-information explains the phenomenon: the reasoner has lost the option to ignore, so a tool output can carry negative usable information, and moving the ...
  </details>

- **2026-11-17** — Xiaoting Jia, Lijun Xu, Ruslan A. Rymzhanov et al. — [Swift Heavy Ion Tracks in Polymorphs of Titanium Dioxide: The Effects of Electron Beam and Crystal Structures](http://arxiv.org/abs/2611.22153v1)
  <details><summary>📄 Abstract</summary>
  Swift heavy ion (SHI) irradiation generates nanoscale damage in materials, offering opportunities for controlled modification of structural properties. Understanding the fundamental processes governing damage formation in altered regions remains a longstanding challenge. This work explores how crystal structure influences swift heavy ion-induced damage formation and evolution in rutile and anatase TiO2. Combining transmission electron microscopy (TEM) and molecular dynamics simulations, we inves...
  </details>

- **2026-11-17** — Allen G. Roush, Minh Nhat Nguyen, Ravid Shwartz-Ziv et al. — [Long-Context Generation Is a Sampling Problem (When You Turn Up the Heat)](http://arxiv.org/abs/2611.22148v1)
  <details><summary>📄 Abstract</summary>
  Open-weight language models are widely observed to get worse the longer they generate. Often, attempts to fix this involve more training. At high temperature, The sampler, i.e. the rule that picks the next token out of the model's probabilities, decides whether long and agentic generation survives and/or thrives. We test 29 open-weight models from 1B to 122B parameters on ten established benchmarks plus needle retrieval out to one million tokens, covering SWE-bench Verified coding agents, long c...
  </details>

- **2026-11-17** — Bingnan Zhao, Harshala Gammulle, Tharindu Fernando — [When does deep reinforcement learning pay off in HVAC supervisory control? Four small Modelica case studies trained directly on FMUs](http://arxiv.org/abs/2611.22144v1)
  <details><summary>📄 Abstract</summary>
  Deep reinforcement learning (DRL) is often proposed for the supervisory control of heating, ventilation and air-conditioning (HVAC) systems. The reported gains are, however, difficult to interpret, because the baselines are often weak and the attainable optimum is seldom known. This paper examines four small, reproducible case studies based on an office building in Brisbane, Australia: pre-cooling under a time-of-use tariff; chiller staging with condenser water reset; chilled water supply temper...
  </details>

- **2026-11-17** — Rahim Hossain, Dipanwita Saha, Ashirbad Mishra et al. — [LoCaR: Localized Canvas Retrieval With Frozen Vision-Language Model](http://arxiv.org/abs/2611.22131v1)
  <details><summary>📄 Abstract</summary>
  Whole image embeddings can under represent small objects and local attributes that distinguish relevant images for localized queries. We present LoCaR, a training free framework for localized text to image retrieval with frozen vision language models. LoCaR constructs and utilizes independent proposals (SAM2) focusing on the object so as to get a more localized representation that independently encodes each region using the frozen visual encoder. We further study paired-support adaptation as an ...
  </details>

- **2026-11-17** — Mukund Athmaram, Manoj Rao, Liang Ma — [What MoE Routing Controls: Causal Interventions on Expert Trajectories](http://arxiv.org/abs/2611.22120v1)
  <details><summary>📄 Abstract</summary>
  In mixture-of-experts (MoE) language models, a token is routed to a sequence of experts across layers. We investigate how forcing tokens onto chosen expert paths influences model behavior. We build a target path from the experts that a concept's or role's tokens most often use, and we add a fixed bias to each target expert's router logit during generation to steer the token toward this expert path. We study two kinds of targets. Format targets concern the form of the output, and concept targets ...
  </details>

- **2026-11-17** — Yuhang Wang, Yuechen Guo, Jingxin Yang et al. — [VTT: Reading Vehicle Size and Powertrain Type from Motion Trajectory Across Unseen Car Models](http://arxiv.org/abs/2611.22109v1)
  <details><summary>📄 Abstract</summary>
  Vehicle size and powertrain information can enrich trajectory data for traffic analysis and simulation. We present VTT, a dataset and benchmark for identifying these attributes from motion and controller area network (CAN) signals across unseen car models. The dataset contains 9,062 drives, about 3,950 h, from 1,431 vehicles and 174 car models. It provides three footprint-based size classes, powertrain labels, and evaluation on unseen car models and unseen drivers. Using 60-s windows, we compare...
  </details>

- **2026-11-17** — Mingyang Liu, Qingcan Kang, Shixiong Kai et al. — [EvoDisco: Strategy Discovery for Evolving Agent Memory](http://arxiv.org/abs/2611.22102v1)
  <details><summary>📄 Abstract</summary>
  Large language model agents accumulate experience in memory, and how that memory evolves during interaction is as important as what it stores. Recent methods update memory online, yet both the operators that transform memory and the rules that select them remain fixed by design. We propose EvoDisco, which formulates agent memory evolution as evolutionary strategy discovery: the agent must discover which operator to apply, when to apply it, and how to instantiate it, rather than rewriting memory ...
  </details>

- **2026-11-17** — Boyu Han, Qianqian Xu, Shilong Bao et al. — [When AUC Meets Generative Reconstruction: A Unified Principle for Balanced Visual Representation Learning](http://arxiv.org/abs/2611.22094v1)
  <details><summary>📄 Abstract</summary>
  Multimodal large language models (MLLMs) require visual encoders that extract fine-grained visual features while constructing semantically disentangled and discriminative representations. Conventional methodologies encounter a fundamental trade-off: contrastive learning enhances inter-class discrimination by suppressing intra-class variability, whereas generative reconstruction emphasizes perceptual fidelity but lacks explicit comparative supervision. The naive aggregation of these objectives vi...
  </details>

- **2026-11-17** — Jiang Xiaobo, Dinghong Lai — [DSADiff: Data Structure-Aware Diffusion for Crystal Structure Prediction via Mitigating Complexity- and Imbalance-Induced Biases](http://arxiv.org/abs/2611.22050v1)
  <details><summary>📄 Abstract</summary>
  Crystal Structure Prediction (CSP) is an important step in accelerating the generation and discovery of new materials. In recent years, diffusion-based CSP methods have made significant progress. However, existing models still suffer from generation bias when facing diverse materials spaces, while systematic approaches for tracing the sources of such performance variations remain limited. To address this issue, we propose LAS (Layered Analysis Strategy), a mechanism analysis framework that ident...
  </details>

- **2026-11-17** — Nikhil Parkar, M. Marimuthu, Riya Joshi et al. — [RLDE: A Reinforcement Learning Framework for Interpretable Iterative Document Editing](http://arxiv.org/abs/2611.22039v1)
  <details><summary>📄 Abstract</summary>
  Improving the quality, clarity, and flow of long documents remains a challenging problem in NLP, as human editing typically occurs through iterative refinement rather than a single-pass rewrite. Most existing automated systems act as black-box generators or rely on supervised learning, limiting interpretability and failing to capture the sequential nature of revisions. In this paper, we propose RLDE, an automated end-to-end metric-driven RL framework that formulates document revision as a refere...
  </details>

- **2026-11-17** — S. M. Monzurul Hoque Chowdhury, Qinghua Li — [An Explainable Agentic AI Framework for Distribution System Load Restoration](http://arxiv.org/abs/2611.22016v1)
  <details><summary>📄 Abstract</summary>
  Distribution system load restoration is a sequential decision-making problem in which restoration actions must maximize served load, prioritize critical loads, and preserve power-flow feasibility. This paper proposes an explainable agentic artificial intelligence (AI) framework for distribution system load restoration. The proposed framework uses multiple large language model (LLM) agents for planner guidance, strategic plan generation, decision arbitration, memory-based feedback, and explanatio...
  </details>

- **2026-11-16** — Hyojung Han — [Beyond Bitwidth: Deployment-Constrained Mixed-Precision Quantization for Multilingual LLM Inference on NVIDIA Blackwell](http://arxiv.org/abs/2611.21974v1)
  <details><summary>📄 Abstract</summary>
  Low-bit LLM quantization is useful only if a model preserves service-relevant accuracy, executes through supported GPU kernels, and meets measured memory and latency limits. We study Qwen3-8B on NVIDIA B200 with vLLM, including INT2/INT3, GPTQ, NVFP4, and mixed-precision configurations. We verify native packed execution and precision on all 144 fused linear modules and evaluate Korean, English, numerical, and reasoning quality under preregistered gates. Packed INT2 and INT3 execute, but all seve...
  </details>

- **2026-11-16** — Musfiqur Rahman, Mahi Begoug, Emad Shihab — [Revisiting the Survival of Agent-Attributed Code: How Measurement Choices Decide the Verdict](http://arxiv.org/abs/2611.21784v1)
  <details><summary>📄 Abstract</summary>
  Studies of how long code from AI coding agents survives after it is merged reach conflicting verdicts: agent code is reported to be retained longer than human code, about as long, or modified sooner. Each study makes defensible measurement choices, but how much these choices decide the verdict is unknown. We revisit the survival of agent-attributed code in our earlier study: 854,139 lines that 2,802 merged pull requests (PRs) added to 215 repositories of the AIDev dataset. We vary nine measureme...
  </details>

- **2026-11-16** — Yanghong Liu, Yang Chen, Kailang Xu et al. — [From Human Videos to Bimanual Dexterous Manipulation Data: Confidence-Guided RL Refinement of Video Priors](http://arxiv.org/abs/2611.21908v1)
  <details><summary>📄 Abstract</summary>
  Collecting demonstrations for bimanual dexterous manipulation is costly, motivating the use of human videos as a source of robot training data. However, uncertainty in video-derived motion estimates and differences between human and robot embodiments make direct motion transfer challenging. In this work, we introduce PriDex, a framework that transforms human-video Priors into executable robot Dexterous manipulation demonstrations through reinforcement learning in simulation. PriDex preserves tas...
  </details>

- **2026-11-16** — Maor Farid — [Large Language Models as Nonlinear Dynamical Systems: The Three Clocks of Depth, Training, and Generation](http://arxiv.org/abs/2611.21983v1)
  <details><summary>📄 Abstract</summary>
  Language models are dynamical systems. A transformer is iterated over its layers, over the steps of its training and over the tokens it generates, and on each of these three clocks it shows behavior that nonlinear dynamics has studied for a century: fixed points, bifurcations, synchronization, chaos and noise-driven escape from potential wells. The two communities rarely meet, so this behavior is often rediscovered under new names. We build a bridge between them. To describe, we condense about 2...
  </details>

- **2026-11-16** — Eduardo Ariño de la Rubia, Szilard Pafka — [Operating an Agent-Driven Dataset Factory: Discovery, Construction, and Public Release](http://arxiv.org/abs/2611.21957v1)
  <details><summary>📄 Abstract</summary>
  Turning public data into prediction datasets requires connecting source discovery, task definition, construction, and distribution. We deployed Dataset Factory to perform these steps continuously under a standing release policy. Bounded language-model tasks interpret sources, write construction code, and review task meaning; deterministic software manages state, workers, retries, and publication. Over 81.53 hours, the factory published 14 datasets at an estimated recurring operating expenditure ...
  </details>

- **2026-11-16** — Harvey L. Devereux, Margaret-Ann Withington, Alin M. Elena et al. — [Dynamics and transport in LiF using classical and machine learned interatomic potentials](http://arxiv.org/abs/2611.21900v1)
  <details><summary>📄 Abstract</summary>
  We perform molecular dynamics simulations of molten Lithium Fluoride, comparing the classical Buckingham and Born-Huggins-Mayer potentials with machine-learnt interatomic potentials - the MACE-MP-0b3 (small) foundation model potential, and a fine-tuned version thereof. We find that the MACE-MP-0b3, out-of-the-box, is able to accurately reproduce the experimental shear viscosity across the liquid state comparable with polarisable potentials despite not itself being polarisable. Previous viscositi...
  </details>

- **2026-11-16** — Simon Catterall — [Anomaly inflow for simplicial Kähler fermions](http://arxiv.org/abs/2611.21860v1)
  <details><summary>📄 Abstract</summary>
  We study massive Kähler Dirac fermions propagating on finite triangulations of various three dimensional manifolds with one or more boundaries. To probe the anomaly structure of these models we decompose the Kähler field into two reduced Kähler fields and choose boundary conditions that ensure that any edge modes are necessarily massless. We then show how to factorize the Pfaffian of this system into a product of bulk and boundary sectors each of which can separately pick up a phase under a glob...
  </details>

- **2026-11-16** — Davide Liga, Liuwen Yu, Matteo Magnini — [Disambiguating Moral Circuits and Moral Features in Language Models: Moral content, normative judgment or cue words? Evidence from 14 models](http://arxiv.org/abs/2611.21705v1)
  <details><summary>📄 Abstract</summary>
  Interpretability methods can locate the attention heads and sparse autoencoder (SAE) features that change the answer a language model gives to a moral prompt, e.g., whether "Stealing medicine for a dying child is morally" continues with "justified" or "wrong". Such a component could respond to moral content, to the judgment of conduct by any norm, or to the word "morally" in the prompt. We built 227 minimal pairs of short phrases, validated by five annotators, whose two versions differ in a mora...
  </details>

- **2026-11-16** — Simon Mackenzie, Mashbat Suzuki — [Nearly Settling the Complexity of Connected $\varepsilon$-Envy-Free Cake Cutting](http://arxiv.org/abs/2611.20890v2)
  <details><summary>📄 Abstract</summary>
  Envy-free cake cutting has been one of the central problems in fair division. In cake cutting, agents' preferences over the cake are accessed through Robertson--Webb (RW) queries. For three or more agents, no algorithm that makes finitely many RW queries can always find a contiguous, exactly envy-free allocation. For contiguous $\varepsilon$-envy-free allocations, however, Hollender and Rubinstein~(JACM, 2025) showed that $\poly(\log(1/\varepsilon))$ RW queries suffice for four agents, leaving o...
  </details>

- **2026-11-16** — Zeynab Anbiaee, Sajjad Dadkhah, Ali A. Ghorbani — [When Tool Names Are Not Identities: Measuring Provider Misbinding in MCP-Based AI Agents](http://arxiv.org/abs/2611.21577v1)
  <details><summary>📄 Abstract</summary>
  Large language model (LLM) applications increasingly act as agents that select and invoke external tools. The Model Context Protocol (MCP) standardizes this interaction by allowing clients to compose tools advertised by multiple servers. However, tool metadata used for discovery and selection is not, by itself, necessarily bound to a verified provider identity. This paper studies this gap as tool-provider misbinding: a failure in which a request intended for a legitimate provider is instead reso...
  </details>

- **2026-11-16** — Roksana Goworek, Alexander Hickey, Federico Nanni et al. — [Replicating and Extending Weight-Space Programming: Frontier LLMs Compile Programs into Weights and Read Input Layers](http://arxiv.org/abs/2611.21449v1)
  <details><summary>📄 Abstract</summary>
  Researchers at MIT recently reported that GPT-6 Astra, a frontier large language model (LLM), can write the weights of small neural networks directly in a single reply, and can read the raw weights of small networks to say what they were trained to do. In a three-day sprint, we replicated and extended these results. Our four findings: (1) Writing weights reproduces. Astra's networks for the game Breakout scored 514, 550 and 307 (versus MIT's 517), and scored just as well on two modified versions...
  </details>

- **2026-11-16** — Jianye Zeng, Qiao Yikang, Duan Huang et al. — [RAMP: Rethinking Multimodal Evaluation through Answer Readout Protocols](http://arxiv.org/abs/2611.20653v1)
  <details><summary>📄 Abstract</summary>
  Multimodal large language models (MLLMs) are often evaluated by converting model outputs into discrete answers. The conversion protocol determines which scores become predictions and can strongly influence the reported results. We introduce RAMP (Readout Aware Multimodal Protocol), a systematic framework that compares direct yes/no token logits, surface-form scores, and typed or reversed A/B interfaces under fixed model checkpoints and paired visual questions. On 500 POPE adversarial questions, ...
  </details>

- **2026-11-16** — Runzhe Wang, Huilin Lu, Shengjie Liu et al. — [AdMem: Expectation-Grounded Procedural Memory for Long-Horizon Task-Solving Agents](http://arxiv.org/abs/2611.20605v1)
  <details><summary>📄 Abstract</summary>
  An agent that carries memory across tasks is only as good as the entries it keeps. We begin from an observation that is easy to reproduce and uncomfortable for the field: naively accumulating cross-task experience can make an agent \emph{worse} than one with no memory at all. On AgentBoard, a workflow-induction memory solves fewer tasks than a memoryless ReAct agent in seven of eight domains, and a per-step procedural store with no surrounding structure loses half of ReAct's completions on Jeric...
  </details>

- **2026-11-16** — Meng Tang, Siyuan Du, Yuxin Liu et al. — [Out of Sight, Into Memory: Compact Visual Latents Retain Local Evidence in Ultra-High-Resolution Remote Sensing](http://arxiv.org/abs/2611.21457v1)
  <details><summary>📄 Abstract</summary>
  Question answering over ultra-high-resolution (UHR) remote sensing scenes poses a tension for multimodal large language models: global overviews obscure small objects and local attributes, whereas detailed crops consume substantial context. Compressing inspected crops into short sequences of continuous visual latents offers a compact memory once crop tokens are discarded, yet diagnostic studies on natural images find that models often ignore latent content, leaving unclear whether compact latent...
  </details>

- **2026-11-16** — Javier Aguilar Martín — [Do Embedding-Map Distances Guide LLM Ideation? Four Tests Against What Came Next](http://arxiv.org/abs/2611.21408v1)
  <details><summary>📄 Abstract</summary>
  A popular ideation recipe treats an embedding map of existing work as a guide: pick points far from everything and decode them into ideas. I test four ways such distances could guide ideation against what appeared later. (1) Far random directions are not text: no later item reaches a raw cosine above about 0.10 with one (after centring or whitening, 22 of 24 cells stay out of reach), and an LLM decoder shown a target's neighbours, with score-only feedback, writes those neighbours in all six targ...
  </details>

- **2026-11-16** — Yang Chen, Qianyi Wang, Ronghui Yang et al. — [Turing Agent: Agentic Formal Verification for Mathematical Research](http://arxiv.org/abs/2611.21299v1)
  <details><summary>📄 Abstract</summary>
  Large language models (LLMs) are rapidly advancing mathematical discovery, moving beyond benchmark-level problem solving to tackle frontier research problems. This progress is ushering mathematics into an era of proof abundance, raising a fundamental challenge: how can we ensure the correctness of the ever-growing volume of AI-generated proofs and transform them into trustworthy, machine-verified mathematical knowledge? We introduce Turing Agent, an agent harness designed to orchestrate end-to-e...
  </details>

- **2026-11-16** — Zhonggang Li, Hongyu Zhou, Raj Thilak Rajan — [Hybrid Optimization-Generative Motion Planning for Multiagent Affine Formations](http://arxiv.org/abs/2611.21264v1)
  <details><summary>📄 Abstract</summary>
  Formation maneuver control enables a multiagent system to cooperatively navigate through constrained environments in collective motion. While various formation controllers exist, they rely heavily on high-quality and dynamically feasible reference trajectories provided a priori, making formation motion planning (FMP) essential. To address the computational challenges for high-dimensional joint trajectories faced by conventional constrained optimization-based solutions, this paper introduces a hy...
  </details>

- **2026-11-16** — Xiaoyu Li, Jiangxuan Long — [The Price of Choosing Examples: Context Overfitting in Adaptive In-Context Learning](http://arxiv.org/abs/2611.21251v1)
  <details><summary>📄 Abstract</summary>
  In-context learning is usually analyzed as if the examples in the prompt were sampled before the learner is chosen. In deployed systems they are not: examples are retrieved, filtered, re-ranked, edited, and repeatedly tested after seeing the query and the data store. We formalize this gap by treating prompt construction as adaptive data analysis through a conditional stochastic-kernel calculus. Our main quantity is the context capacity, the mutual information or approximate max-information betwe...
  </details>

- **2026-11-16** — Natalija Stepurko, Joonatan E. M. Laulainen — [Out-of-training properties in frozen interatomic potential embeddings are decodable and ordered by physical scale](http://arxiv.org/abs/2611.21116v1)
  <details><summary>📄 Abstract</summary>
  Machine-learned interatomic potentials (MLIPs) are trained on energies, forces and stresses, yet their frozen representations can predict other materials properties. We probe ORB-v3 and UMA-S across layers, read-outs and equivariant channels for nine properties of 154,875 Materials Project crystals. Both models outperform composition-only descriptors on all targets, including five outside their training objectives; errors in physical units help assess potential screening applications. Optimal de...
  </details>

- **2026-11-16** — Marcos Soldera, Robert Baumann, Bogdan Voisiat et al. — [Laser Processing for Energy Applications](http://arxiv.org/abs/2611.21024v1)
  <details><summary>📄 Abstract</summary>
  Laser processing has emerged as a transformative technology in the energy sector, enabling precise, efficient, and scalable solutions for energy generation, storage, and sustainability. This chapter explores the diverse applications of laser technology in energy applications. It begins with an overview of laser-driven inertial confinement fusion for energy production, highlighting key experimental facilities and crucial laser parameters. The role of lasers in solar energy harvesting is examined,...
  </details>

- **2026-11-16** — Tina Vartziotis, Ketevan Peranidze, Rodopi Kosteli et al. — [Re-Reading Is Not Free: Token Traces and Cache-Aware Energy Estimation for LLM Agents in Software Engineering](http://arxiv.org/abs/2611.20873v1)
  <details><summary>📄 Abstract</summary>
  As large language models (LLMs) evolve from conversational assistants into autonomous agents embedded in software development workflows, estimating their environmental footprint requires moving beyond conventional token-based accounting. Existing energy estimators focus on isolated request-response interactions, overlooking the repeated processing of accumulated context, cache reuse, and work delegated to subagents. We analyze nearly one billion tokens collected across 42 sessions and 752 task e...
  </details>

- **2026-11-16** — Xuening Wu, Haode Yang, Yanlan Kang et al. — [When Does Interaction Help? Toward a Reynolds Number for Collective Intelligence](http://arxiv.org/abs/2611.20773v1)
  <details><summary>📄 Abstract</summary>
  Multi-agent systems combine distributed information through interaction, which can improve performance but also spread errors or suppress useful differences. Predicting when interaction helps is central to understanding and designing collective intelligence. We investigate whether a few dimensionless parameters can predict gains over explicitly defined non-communicating baselines across group sizes, network structures, and tasks, toward a Reynolds-number-like description of collective intelligen...
  </details>


## 📊 统计 / Statistics

| 分类 / Category | 论文数 / Count |
|------|--------|
| jailbreak | 725 |
| prompt-injection | 694 |
| memory-poisoning | 59 |
| tool-use-attack | 178 |
| backdoor | 563 |
| adversarial-attack | 676 |
| privacy-leakage | 4635 |
| steganography | 93 |
| misuse | 1335 |
| red-teaming | 157 |
| vulnerability | 4082 |
| defense | 4004 |
| alignment | 3751 |
| robustness | 4106 |
| watermark | 775 |
| unlearning | 124 |
| agent-safety | 67 |
| benchmark | 75 |
| survey | 464 |
| other | 11298 |

---

📚 **全部 37861 篇论文**（2022 至今）请访问 [GitHub Pages](https://ny1024.github.io/AgentSafety-Papers/) 查看完整列表、搜索与筛选。

*Generated by AgentGuard at 2026-11-20 00:12:00*