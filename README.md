<div align="center">

# AgentGuard 🛡️

**Daily Tracking of LLM Agent Security Papers on arXiv**

[![Auto Update](https://github.com/NY1024/AgentSafety-Papers/actions/workflows/daily-update.yml/badge.svg)](https://github.com/NY1024/AgentSafety-Papers/actions/workflows/daily-update.yml)
[![Papers](https://img.shields.io/badge/Papers-37653-blue)](#)
[![License](https://img.shields.io/badge/License-MIT-green)](#)

</div>

---

## 📖 简介 / Introduction

自动追踪 arXiv 上大模型 Agent 安全方向的最新论文，每日更新，关键词智能分类。

*Automatically tracking the latest LLM Agent security papers on arXiv, updated daily with keyword-based classification.*

**最近更新 / Last Updated**: 2026-11-18 14:58 ｜ **论文总数 / Total Papers**: 37653（近 30 天 / Recent 30 days: 4288）

🌐 **[GitHub Pages](https://ny1024.github.io/AgentSafety-Papers/)** — 查看全部 37653 篇论文（含摘要、分类筛选、搜索）/ View all 37653 papers with abstracts, filters & search

## 📑 分类导航 / Category Navigation

- **[jailbreak](#-jailbreak)** — 越狱攻击 / Jailbreak Attacks — 724
- **[prompt-injection](#-prompt-injection)** — 提示注入攻击 / Prompt Injection Attacks — 690
- **[memory-poisoning](#-memory-poisoning)** — 记忆投毒与篡改 / Memory Poisoning & Tampering — 59
- **[tool-use-attack](#-tool-use-attack)** — 工具使用攻击 / Tool-Use Attacks — 175
- **[backdoor](#-backdoor)** — 后门与投毒攻击 / Backdoor & Poisoning Attacks — 561
- **[adversarial-attack](#-adversarial-attack)** — 对抗攻击 / Adversarial Attacks — 675
- **[privacy-leakage](#-privacy-leakage)** — 隐私泄露 / Privacy Leakage — 4622
- **[steganography](#-steganography)** — 隐写与隐蔽通信 / Steganography & Covert Communication — 93
- **[misuse](#-misuse)** — 滥用与误用 / Misuse & Abuse — 1330
- **[red-teaming](#-red-teaming)** — 红队测试 / Red Teaming — 155
- **[vulnerability](#-vulnerability)** — 漏洞与攻击面 / Vulnerabilities & Attack Surfaces — 4062
- **[defense](#-defense)** — 防御与防护方法 / Defense & Protection Methods — 3981
- **[alignment](#-alignment)** — 对齐与安全约束 / Alignment & Safety Constraints — 3726
- **[robustness](#-robustness)** — 鲁棒性与可靠性 / Robustness & Reliability — 4080
- **[watermark](#-watermark)** — 水印与溯源 / Watermarking & Provenance — 769
- **[unlearning](#-unlearning)** — 机器遗忘 / Machine Unlearning — 122
- **[agent-safety](#-agent-safety)** — Agent 安全框架 / Agent Safety Frameworks — 67
- **[benchmark](#-benchmark)** — 安全评测与基准 / Safety Benchmarks & Evaluation — 75
- **[survey](#-survey)** — 综述与系统化 / Surveys & Systematization — 463
- **[other](#-other)** — 其他安全相关 / Other Security-Related — 11224

## 📄 近期论文 / Recent Papers (Last 30 Days)

> 仅展示最近 30 天中最新的 500 篇论文（含日期、作者、摘要）。近 30 天共 4288 篇，完整 37653 篇论文列表请访问 [GitHub Pages](https://ny1024.github.io/AgentSafety-Papers/)

> Showing the latest 500 of 4288 papers from the last 30 days (with date, authors & abstract). For the full list of 37653 papers, visit [GitHub Pages](https://ny1024.github.io/AgentSafety-Papers/)

### 📂 jailbreak
*越狱攻击 / Jailbreak Attacks* — 3 papers

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
*提示注入攻击 / Prompt Injection Attacks* — 8 papers

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

- **2026-11-15** — Hussein Jawad, Alexandre Landeau, Guy Fleury Iradukunda et al. — [Risk-certified prompt optimization for LLM-as-a-judge guardrails](http://arxiv.org/abs/2611.20156v1)
  <details><summary>📄 Abstract</summary>
  LLM-as-a-judge guardrails are often controlled primarily through system prompts, yet standard prompt optimization methods target average performance rather than explicit safety constraints. This paper studies system-prompt selection as a constrained optimization problem: maximize benign pass rate while keeping the missed-attack rate below a user-specified level α with finite-sample statistical control. The framework combines LLM-based judging, automatic prompt generation, and distribution-free r...
  </details>

- **2026-11-15** — Yang Luo, Guangpu Chen, Yichen Liu et al. — [Security of Deep Research Agents: Attack Surface, Defenses, Benchmarks, and Agenda Seeding against Research Planning](http://arxiv.org/abs/2611.20045v1)
  <details><summary>📄 Abstract</summary>
  Deep research and agentic search agents autonomously retrieve content from the open web and generate reports with citations, and their outputs are often taken directly as research conclusions. This paper systematizes security research in this area along four stages, namely retrieval, planning, evidence integration, and report generation. We present a unified threat model, a taxonomy of attacks and defenses, and a review of evaluation benchmarks, and we align the area dimension by dimension with ...
  </details>

- **2026-11-14** — Harish Santhanalakshmi Ganesan — [Agent Authenticator: Passkey-Grade, Hardware-Bound Authentication for AI Agents](http://arxiv.org/abs/2611.19536v1)
  <details><summary>📄 Abstract</summary>
  AI coding agents now push code, publish packages, call model APIs and operate cloud resources on behalf of developers. They authenticate to these services with the same bearer secrets humans use, personal access tokens, API keys and package-registry tokens, stored where the model, its subprocesses and any co-resident malware can read them. Incidents in 2025 and 2026, including prompt-injection attacks on coding agents and self-propagating supply-chain worms, show that this arrangement fails in p...
  </details>


### 📂 backdoor
*后门与投毒攻击 / Backdoor & Poisoning Attacks* — 3 papers

- **2026-11-17** — Zane Fu, Yanzhao Zheng, Jinze Liu et al. — [As Student Rollouts Continue, Visual Backdoors Keep Growing](http://arxiv.org/abs/2611.22446v1)
  <details><summary>📄 Abstract</summary>
  Conventional knowledge distillation can facilitate the propagation of backdoors from teacher models to student models. However, how this risk manifests in On-Policy Distillation (OPD) remains insufficiently studied. OPD has recently emerged as an important post-training paradigm for Vision-Language Models (VLMs). Unlike traditional offline distillation, OPD does not require teacher-generated responses. Instead, it uses the teacher's probability distributions to supervise response trajectories ge...
  </details>

- **2026-11-15** — Chirag Goel, Jacob Lavoie, Amirhossein Naghshzan et al. — [HEAMS: Holistic Evaluation of Agent Memory Systems](http://arxiv.org/abs/2611.20144v1)
  <details><summary>📄 Abstract</summary>
  Memory systems allow AI agents to persist information across interactions, making them more personalized and more capable on long-horizon tasks. This persistence introduces new risks: stored information can be disclosed in inappropriate contexts, resist correction or deletion, be retained beyond what users desire, or be poisoned to influence later agent behaviour. Yet memory systems are typically evaluated on task performance and efficiency alone. We argue that a memory system should instead be ...
  </details>

- **2026-11-15** — Ji Guo, Xiaolong Qin, Jin Jiang et al. — [HalluProbe: Exploiting VLM Hallucinations for Backdoor Detection](http://arxiv.org/abs/2611.19868v1)
  <details><summary>📄 Abstract</summary>
  Vision-Language Models (VLMs) are vulnerable to backdoor attacks introduced through data poisoning, making effective backdoor detection a critical security challenge. In this paper, we uncover a novel connection between VLM hallucinations and backdoor behaviors and exploit this connection for backdoor detection. Our key insight is that poisoned training data induces strong language priors toward the backdoor target token, while such priors are also a major source of hallucinations. This suggests...
  </details>


### 📂 adversarial-attack
*对抗攻击 / Adversarial Attacks* — 3 papers

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
*隐私泄露 / Privacy Leakage* — 28 papers

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

- **2026-11-16** — Max Schulte, Hartmut Surmann, Julien Meine — [Counting What Matters: Reducing Redundant Object Detections in Overlapping UAV Mapping Imagery for Disaster Response](http://arxiv.org/abs/2611.21076v1)
  <details><summary>📄 Abstract</summary>
  UAV mapping flights enable rapid aerial reconnaissance of large-scale incident sites in civil protection. However, the image overlap required for orthophoto generation causes every physical object to be detected multiple times across images, while dynamic objects may be omitted from or duplicated in the resulting orthomosaic. Analysis based on the orthophoto alone is therefore structurally insufficient. We address this by detecting objects on the individual images and merging redundant detection...
  </details>

- **2026-11-16** — Ahmet Bestami Kose, Mehmet Sergen Catal, Muhammet Cagri Yeke et al. — [Vision-Language Model-Based Phase-OTDR Event Classification](http://arxiv.org/abs/2611.20841v1)
  <details><summary>📄 Abstract</summary>
  Phase-sensitive optical time-domain reflectometry (Phase-OTDR) enables distributed vibration sensing, but reliable event classification has traditionally relied on fully supervised models that require extensive annotated data. This study examines the adaptability of a Vision-Language Model (VLM) for Phase-OTDR event recognition through few-shot learning. Raw samples are converted into Short-Time Fourier Transform (STFT) dB-magnitude spectrogram mosaics, color-mapped and resized to RGB images, an...
  </details>

- **2026-11-16** — Louis Mouchon, Alexis Lainault — [Surprise-Gated Memory for Live Speaker Diarization](http://arxiv.org/abs/2611.20819v1)
  <details><summary>📄 Abstract</summary>
  We transpose the Surprise-Gated Memory recipe, a frozen encoder plus a calibrated novelty signal that gates a one-shot episodic store consolidated by periodic replay, from continual visual learning to live speaker diarization. The moment-to-moment question a streaming diarizer must answer, whether an arriving voice belongs to an already-heard speaker or a new one, is a known-versus-novel decision, exactly the decision the surprise gate is built for. On a frozen fine-tuned DiariZen backbone, our ...
  </details>

- **2026-11-16** — Zhe Dong, Guanyu Cai, Yuchen Jiang et al. — [Building Fully On-Device GUI Agents with Mobile NPUs](http://arxiv.org/abs/2611.20772v1)
  <details><summary>📄 Abstract</summary>
  Mobile GUI agents are increasingly used to automate everyday smartphone tasks, but most existing systems still rely on cloud-hosted models or remote inference, introducing repeated communication latency, privacy exposure, and dependence on network availability. Modern smartphones integrate neural processing units (NPUs) that provide an attractive substrate for fully on-device LLM inference. However, directly deploying conventional GUI-agent pipelines on mobile NPUs is inefficient. GUI-agent infe...
  </details>

- **2026-11-16** — German Devchich, Timur Akhtyamov, Denis Fatykhoph et al. — [CLIFT: Contrastive LiDAR Instance Features for 3D Pedestrian Tracking](http://arxiv.org/abs/2611.20737v1)
  <details><summary>📄 Abstract</summary>
  A social robot has to keep track of the people around it over time to plan its motion, a task handled by 3D multi-object tracking. For the LiDAR modality, trackers usually sit on top of a detector and link its detections across frames with a separate motion model or re-identification network. We instead show how a 3D LiDAR detector itself can be turned into a tracker by adding an instance-level contrastive objective on its intermediate voxel features. Each embedding is read from the voxels insid...
  </details>

- **2026-11-16** — Asmau Lawal Bilbis, Nathanael L. Baisa, Amudhavel Jayavel — [VisDrone-ReID: A Unified Multi-Category Object Re-Identification Benchmark](http://arxiv.org/abs/2611.20372v1)
  <details><summary>📄 Abstract</summary>
  Object re-identification (Re-ID) benchmarks remain predominantly confined to single-category evaluations, limiting the development of unified systems capable of operating across diverse object types. This paper presents VisDrone-ReID, a unified multi-category Re-ID benchmark derived from the VisDrone2019-MOT dataset through a principled conversion pipeline. The pipeline resolves structural incompatibilities between multi-object tracking annotations and Re-ID evaluation requirements, addressing s...
  </details>

- **2026-11-15** — Bowen Sun, Chaowei Xiao — [Where the Savings Go: The Limits of Hiding Cross-Tenant Cache Hits in LLM Serving](http://arxiv.org/abs/2611.20291v1)
  <details><summary>📄 Abstract</summary>
  LLM serving engines cache prompt prefixes; a cache hit skips computation and returns faster, so a shared cache reveals whether others have sent a given text. Per-account salting closes this channel but forgoes cross-tenant reuse and isolates only whole accounts, even where access is redistributed or trust domains are subdivided below them. Defenses that share globally but hide hits promise reuse without relying on account boundaries. Hiding a hit requires everything tenants observe afterwards to...
  </details>

- **2026-11-15** — Tushar Nayan, Mohammed Al Duniawi, Song Fang et al. — [Understanding Users' Security, Privacy, and Trust Concerns in Healthcare AI Systems](http://arxiv.org/abs/2611.20223v1)
  <details><summary>📄 Abstract</summary>
  Artificial intelligence is increasingly integrated into healthcare systems, from clinical information retrieval to workflow automation and decision support, which introduces new security, privacy, and trust risks with direct implications for patient care. While prior work has examined these risks from technical and regulatory perspectives, less is known about how these risks are naturally discussed in online communities. To address this gap, we conduct a large-scale analysis of 14 medical commun...
  </details>

- **2026-11-15** — Jinfeng Xu, Zheyu Chen, Ziyue Peng et al. — [Reflection Is Not Always Worth It: Budgeted Reflection Allocation for Recommendation Agents](http://arxiv.org/abs/2611.19847v1)
  <details><summary>📄 Abstract</summary>
  This work aims to make recommendation agents more efficient by reducing unnecessary LLM reflection while preserving full-catalog ranking and inference reranking. Since BRAVE changes only how training-time reflection is allocated, it does not introduce new user data requirements or additional LLM exposure beyond the base agent protocol. The main potential risk is that a poorly calibrated allocator may assign less reflection to users whose preferences are sparse, niche, or under-represented, which...
  </details>

- **2026-11-15** — Yuxuan Xiao, Shanshan Zhang, Shengcai Liao et al. — [Two-Stage Prompt Learning: A Unified Framework for Person ReID without Clothing Hypothesis](http://arxiv.org/abs/2611.19939v1)
  <details><summary>📄 Abstract</summary>
  Person re-identification (ReID) in real-world scenarios involves three clothes conditions: the same clothes (SC), changed clothes (CC), and the unknown (GEN) scenario where clothes changes are not specified. Existing methods typically train separate SC- or CC-specific models, which limits generalization across all conditions. Meanwhile, pre-trained visual-language models (VLMs) such as CLIP have shown strong generalization ability in various vision tasks, motivating recent ReID methods to incorp...
  </details>

- **2026-11-15** — Dongwu Qian — [Grounding Language Models in Speech Does Not Fix "AI Flavor": Calibrated LLM Judges, Goodhart Traps, and a Preference-Tuning Fix](http://arxiv.org/abs/2611.19840v1)
  <details><summary>📄 Abstract</summary>
  Chinese outputs of large language models carry a perceptible "AI flavor": formulaic sentence frames, stacked written-register connectives, repetition loops, and layout leakage. A popular hypothesis blames text-only training for the missing inner-speech layer of human writing; injecting speech or prosody signals should therefore reduce it. We test it with controlled interventions on a 0.6B model; all three fail: (i) phoneme-interleaved continued pretraining yields no spokenness gain under text-ma...
  </details>


### 📂 misuse
*滥用与误用 / Misuse & Abuse* — 16 papers

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

- **2026-11-16** — Younghwan Kil, Giung Nam, Joonhyeong Park et al. — [Example-Based Spatial Guidance for Training-Free Concept Erasure in Diffusion Models](http://arxiv.org/abs/2611.20623v1)
  <details><summary>📄 Abstract</summary>
  Text-to-image (T2I) diffusion models often synthesize policy-violating content, necessitating robust safeguards and rigorous evaluation frameworks. However, current approaches remain largely monolithic in both execution and evaluation, limited to coarse-grained categorization within broad unsafe concepts. Such approaches fail to account for the specific constituent factors of a violation, resulting in weak learning signals and allowing model collapse to bypass safety checks. To overcome these li...
  </details>

- **2026-11-16** — Koki Itai, Jun Hirako, Hiroaki Yamagiwa — [Abstention Direction in Large Language Models: Mechanistic Interpretability of Abstention Across Query Ambiguity, Knowledge Limits, and Safety Alignment](http://arxiv.org/abs/2611.20441v1)
  <details><summary>📄 Abstract</summary>
  Abstention, the withholding of a response by a large language model (LLM) under uncertainty or safety risks, is essential for trustworthy models. The causes of abstention fall into three perspectives: ambiguity in the Query (Q), limits of Model Knowledge (MK), and misalignment with Human Values (HV). However, prior analyses of internal representations have focused on HV, using a refusal direction computed from harmful and harmless queries. No study has analyzed the three perspectives jointly. We...
  </details>

- **2026-11-16** — Janhavi Khindkar, Nataliia Povarova — [Refusal Register is Causally Steerable: Decomposing the Refusal Direction into Category-Aligned Components in Gemma-2-9B-IT](http://arxiv.org/abs/2611.20405v1)
  <details><summary>📄 Abstract</summary>
  Prior work shows that refusal in instruction-tuned language models can be ablated by intervening on a single residual-stream direction (Arditi et al., 2024), and more recent work finds multiple refusal-mediating directions and concept cones (Wollschläger et al., 2025). We ask a different question: do refusal-related directions carry information about the register of refusal language - how the model refuses - and not only whether it refuses? In Gemma-2-9B-IT we identify two SVM-derived linear dir...
  </details>

- **2026-11-15** — Chansu Han, Seok-Hwan Choi, Takeshi Takahashi — [Where Is Rank-1 DiM Refusal Intervenable in Multimodal LM Derivatives?](http://arxiv.org/abs/2611.19826v1)
  <details><summary>📄 Abstract</summary>
  Open-weight model hubs now ship not only chat checkpoints but a long tail of derivatives---fine-tunes, safety guards, vision--language models (VLMs), audio wrappers, and generative heads---yet residual-stream safety audits still often intervene at a single site, usually the text decoder $T$. We ask a localization question under one shared mean / rank-1 difference-in-means (DiM) extract$=$intervene protocol, with matched-norm random and empty-rate controls: does causal chat attack lift concentrat...
  </details>

- **2026-11-15** — Ewelina Gajewska — [A Dataset for Misogyny Detection in Polish Social Media: Transferability of Hateful Speech Detection from General to Specific Types of Hate](http://arxiv.org/abs/2611.20044v1)
  <details><summary>📄 Abstract</summary>
  Harmful language detection is commonly evaluated on broadly defined hate speech and toxicity benchmarks, yet it remains unclear whether models that successfully detect harmful language in general can transfer this capability to more specific forms of hate. We investigate this problem for misogyny detection in Polish, an area for which dedicated resources remain scarce. We introduce a new dataset of Polish social media comments annotated for misogyny, gender-directed hateful speech. Using this re...
  </details>

- **2026-11-15** — Jason Lee, Dikshanta Pokhrel, Phonn Nay Khant et al. — [MathaMAGICal: Validating Trajectory Data Attribution During Capability Acquisition](http://arxiv.org/abs/2611.19692v1)
  <details><summary>📄 Abstract</summary>
  Influence-function-based methods like MAGIC provide exact first-order scores for trajectory data attribution, yet only retraining indicates whether those scores accurately predict data removal. We evaluate MAGIC on $86$M- and $152$M-parameter GPT-2-style models learning multistep arithmetic from scratch on filtered web text and four synthetic math families. Full-run attribution at $86$M suffers from numerical overflow, and even with metagradient clipping, scores correlate near chance with retrai...
  </details>


### 📂 red-teaming
*红队测试 / Red Teaming* — 2 papers

- **2026-11-16** — Keshav Shenoy, Anthony Zang, Eric Gan et al. — [Auditors Struggle to Catch Sabotage In End-to-End Transcripts of AI Safety Research](http://arxiv.org/abs/2611.21832v1)
  <details><summary>📄 Abstract</summary>
  As AI systems are increasingly used to automate AI R&D, misaligned systems could sabotage research intended to improve model safety and alignment. To stress-test defenses against such sabotage, we use a human expert as a proxy saboteur on AI safety research. We conduct a red-team/blue-team game where a human researcher runs AI safety experiments from scratch and auditors try to tell which were sabotaged and how. Given access to the full research transcript and the ability to run experiments, hum...
  </details>

- **2026-11-14** — Zhen Wan — [VAST: Compiling Grounded Vulnerability Scenarios into Verifiable, Multi-Step Environments for Evaluating LLM Red-Team Agents](http://arxiv.org/abs/2611.19465v1)
  <details><summary>📄 Abstract</summary>
  Evaluating Large Language Model (LLM) security agents requires reproducible environments whose workflow difficulty can be varied and whose failures can be diagnosed. We present VAST (Verifiable Adversarial Scenario Training & Evaluation), a declarative range compiler separating vulnerability scenarios from a compiler-introduced workflow-hardening layer. Following a post-hoc code and AST audit across all topics, the main benchmark retains 109 seed edges (45 with strict upstream CVE annotations), ...
  </details>


### 📂 vulnerability
*漏洞与攻击面 / Vulnerabilities & Attack Surfaces* — 57 papers

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

- **2026-11-15** — Neel Rajani, Ivan Titov — [Protecting Safety during Reasoning Training with Low-Rank Fisher Regularisation](http://arxiv.org/abs/2611.20288v1)
  <details><summary>📄 Abstract</summary>
  Large language models are trained to have safety guardrails, but these can be compromised while fine-tuning for new capabilities, such as reasoning. One way to mitigate this degradation is to modify the fine-tuning objective to preserve safety behaviour, but doing so effectively and efficiently remains challenging. We revisit Elastic Weight Consolidation (EWC), which penalises parameter updates based on sensitivity estimates from the diagonal of the Fisher information matrix (FIM). While EWC pro...
  </details>

- **2026-11-15** — Marcello Sano, Samuele Casagrande, Davide Ferrario et al. — [GNN-Based Deep Reinforcement Learning for Coastal Emergency Response under Extreme Water Levels](http://arxiv.org/abs/2611.20268v1)
  <details><summary>📄 Abstract</summary>
  When a storm surge approaches a coastal town, the emergency plan must be put into action quickly using water-level forecasts, flood extent, road access, vulnerable residents and shelters. Bringing this information together under time pressure is slow and depends on the duty officer's expertise. This paper is one step in a wider research line from data to safe decisions: machine learning to understand the hazard, reinforcement learning and planning to choose actions, large language models (LLMs) ...
  </details>

- **2026-11-15** — Xin Mao, Anqi Dong, Can Chen — [Contraction Analysis and Control of Polynomial Dynamical Systems](http://arxiv.org/abs/2611.20252v1)
  <details><summary>📄 Abstract</summary>
  Contraction analysis has found broad applications in synchronization, tracking, observer design, and nonlinear feedback control. However, establishing contraction conditions for polynomial dynamical systems remains challenging due to their state-dependent Jacobians. In this article, we develop a tensor-based framework for contraction analysis of polynomial dynamical systems by exploiting the structure of orthogonally decomposable (odeco) coefficient tensors. By transforming the dynamics into mod...
  </details>

- **2026-11-15** — Weiyuan Fan, Jacinto Ulloa — [Higher-dimensional homogenization of quasiperiodic elastic materials](http://arxiv.org/abs/2611.20142v1)
  <details><summary>📄 Abstract</summary>
  Quasiperiodic geometrical arrangements, which exhibit long-range order in the absence of periodicity, have attracted interest in the design of composites and mechanical metamaterials. In this context, direct numerical simulations explicitly resolving the quasiperiodic microstructure become prohibitively expensive for macroscopic problems, motivating the development of homogenized continuum models. However, the absence of a periodic unit cell in physical space hinders the use of conventional homo...
  </details>

- **2026-11-15** — Amir Azzam, M. Pilar Casado, Michele Grossi et al. — [Generative Models using Multi-layer Quantum Extreme Learning Machines](http://arxiv.org/abs/2611.20139v1)
  <details><summary>📄 Abstract</summary>
  Quantum reservoir computing (QRC) and the closely related quantum extreme learning machine (QELM) paradigm exploit the complex dynamics of an uncontrolled quantum system for machine learning, offering an alternative to variational quantum algorithms whose training is hindered by barren plateaus and costly circuit optimization. Because the quantum system itself is left fixed, learning reduces to fitting a linear readout of a set of measured observables, and no gradient is ever taken through the q...
  </details>

- **2026-11-15** — Yansong Qu, Zilin Huang, Zihao Sheng et al. — [SAFER: Navigating the Exploration-Exploitation Dilemma in World-Model-Based Planning for Autonomous Driving](http://arxiv.org/abs/2611.20107v1)
  <details><summary>📄 Abstract</summary>
  An autonomous vehicle must foresee the consequences of its actions, especially in the rare, time-critical situations where crashes happen. A world model offers this foresight, but only within the coverage of its training data, which poses an exploration-exploitation dilemma. Within this coverage a planner can hardly improve on the data, and beyond it the model's errors mislead it. Logs of competent driving rarely contain the failures that would widen the coverage, and agents that learn from inte...
  </details>

- **2026-11-15** — Tingwei Chen, Yunxiao Shi, Zhendong Chu et al. — [DetouR: Plugging Association Routes into Search Agents for Multi-hop Question Answering](http://arxiv.org/abs/2611.19967v1)
  <details><summary>📄 Abstract</summary>
  Search agents answer multi-hop questions by interleaving reasoning with retrieval, deciding at each step what to search next. Existing agents follow semantic routes: they infer what is missing and phrase it as a query, reaching only what the model can name. Yet the decisive page is often one the question never names, frequently just one hyperlink away from evidence already retrieved. Following such association routes reaches more gold pages than semantic search under the same budget. Exploiting ...
  </details>

- **2026-11-15** — Sven Krippendorf, Magdalena Larfors, Zhimei Liu et al. — [Towards a foundation model for Type IIB flux vacua](http://arxiv.org/abs/2611.19950v1)
  <details><summary>📄 Abstract</summary>
  Progress in characterising the Type IIB flux landscape requires scalable methods for constructing flux vacua. In this work, we investigate generative models as a framework for sampling vacua across multiple Calabi-Yau geometries and for directing searches towards specified physical properties. We compare transformers and diffusion models trained to generate quantised fluxes together with approximate values of the complex structure moduli and axio-dilaton. We exploit a staged training procedure c...
  </details>

- **2026-11-15** — Gaotang Li, Lingjie Chen, Chunyuan Deng et al. — [Multi-Branch Transformer](http://arxiv.org/abs/2611.19800v1)
  <details><summary>📄 Abstract</summary>
  Transformer language models are commonly scaled by making their blocks wider or stacking them deeper. In this work, we explore a complementary path: branching, the parallel composition of full Transformer blocks. We introduce the Multi-Branch Transformer (MBT), which processes the input through shared initial layers, executes independently parameterized branches of sequential blocks in parallel, and fuses their outputs before shared final layers. At comparable training compute, we study three MB...
  </details>

- **2026-11-15** — Joshua Joseph George, Hassan Safouhi — [Efficient Recursive Evaluation of Gaussian, Gamma, and Inverse Gaussian Tail Probabilities](http://arxiv.org/abs/2611.19782v1)
  <details><summary>📄 Abstract</summary>
  Accurate computation of tail probabilities motivates efficient high-order implementations of the $G_n^{(1)}$ extrapolation transformation. We derive finite recurrence relations in the transformation order for Gaussian, gamma, and inverse Gaussian tail approximations. The Gaussian and inverse Gaussian numerator and denominator sequences satisfy four-term recurrences, whereas the gamma sequences satisfy a three-term recurrence. The derivation exploits the structure of the underlying differential o...
  </details>

- **2026-11-15** — Deep Shah, Nehal Kathrotia — [Compositional Exploits in Autonomous Coding Agents: Attack Mechanics and Ephemeral Defense](http://arxiv.org/abs/2611.19764v1)
  <details><summary>📄 Abstract</summary>
  Autonomous coding agents (such as Antigravity, Claude Code, Cursor, and OpenHands) rely on third-party tools to inspect files, run commands, and call external APIs. Today's security auditors evaluate these tools almost entirely in isolation: static linters and AST checkers verify that each individual tool contains no malicious code at installation time. In this paper, we show that isolated tool auditing is fundamentally flawed. We expose compositional exploits in autonomous coding agents, an eme...
  </details>

- **2026-11-15** — Youssef Gamal, Mohamad Fakih, Halima Bouzidi et al. — [Found, but Not Fixed : From Software Vulnerability Discovery to Fixes with Iterative LLM Pipelines](http://arxiv.org/abs/2611.19719v1)
  <details><summary>📄 Abstract</summary>
  Software vulnerabilities persist as a critical threat despite the deployment of sophisticated detection tools and AI assistants. While detection has advanced, the subsequent code repair phase remains a primary bottleneck; manual intervention is inherently slow, costly, and prone to introducing secondary regressions and issues. In this paper, we investigate whether an iterative, LLM-based pipeline can provide a robust solution for the automated repair of vulnerable functions in real-world code. W...
  </details>

- **2026-11-14** — Jinrui Fang, Runhan Chen, Yining Wu et al. — [ROUNDS: Source-Framed Diagnostic Revision after Multi-Turn Clinical Evidence](http://arxiv.org/abs/2611.19636v1)
  <details><summary>📄 Abstract</summary>
  Large language models (LLMs) achieve high scores on medical benchmarks, but does this performance translate into reliable diagnosis as a conversation unfolds? In diagnostic conversations, users can provide clinical findings across multiple turns, ask for a diagnosis without supplying answer options, and introduce opinions from others. Models must therefore form diagnoses from the available evidence and decide how to respond to subsequent advice. We introduce ROUNDS, a framework that evaluates th...
  </details>

- **2026-11-14** — Mario Edoardo Pandolfo, Kyriakos Stylianopoulos, George C. Alexandropoulos et al. — [Over-the-Air Semantic Alignment via Dual Stacked Intelligent Metasurfaces](http://arxiv.org/abs/2611.19515v1)
  <details><summary>📄 Abstract</summary>
  Semantic communications enable task-oriented information exchange, but suffer from latent-space mismatch when transmitter and receiver employ heterogeneous machine learning models. Existing semantic alignment methods rely on digital processing, introducing computational and latency overhead. This paper proposes a dual stacked intelligent metasurfaces (dual-SIM) architecture that performs semantic alignment entirely in the wave domain. By jointly exploiting programmable metasurfaces at both ends ...
  </details>

- **2026-11-14** — Tianyi Zhao, Qihao Xu, Jiawen Xi et al. — [Beyond Paired Inputs: Learning to Leverage RGB-T Cross-Modal Relations in Multimodal Large Language Models](http://arxiv.org/abs/2611.19493v1)
  <details><summary>📄 Abstract</summary>
  RGB and thermal infrared (TIR) sensors provide complementary observations, yet their distinct sensing characteristics make effective cross-modal coordination challenging. Although existing multimodal large language models (MLLMs) can process paired RGB-T inputs, they often fail to translate cross-modal relations into effective task-specific decisions, leaving the potential of these relations to improve task performance and robustness largely untapped. Motivated by this observation, we introduce ...
  </details>


### 📂 defense
*防御与防护方法 / Defense & Protection Methods* — 66 papers

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

- **2026-11-16** — Pier Mattia Basciano, Giovanni Farina, Salvatore Monteleone — [A First Look at System One Decision Models for Malware Detection](http://arxiv.org/abs/2611.20699v1)
  <details><summary>📄 Abstract</summary>
  Malware detection needs scores calibrated at a fixed false positive rate (FPR) and decisions an analyst can read: feature-based detectors give the first, large language models (LLMs) on decompiled code the second, through generated text of uncalibrated confidence. System One decision models answer a typed question about a text with a probability over its declared answers in one forward pass. We present the first evaluation of these models for Windows Portable Executable malware detection, analyz...
  </details>

- **2026-11-16** — Senquan Wang, Hui Fang, Haoran Nan et al. — [BiGSyn: A Bi-Level Heterogeneous Graph Contrastive Learning Framework for Interpretable Drug Synergy Prediction](http://arxiv.org/abs/2611.20603v1)
  <details><summary>📄 Abstract</summary>
  Drug combination therapy has become a mainstream of modern medicine, with the potential to enhance efficacy, reduce toxicity, and overcome drug resistance. However, identifying synergistic drug combinations remains challenging, as it requires modeling complex interactions across multiple biological scales---from atom-level molecular structures to entity-level relations in biological networks. Existing approaches typically model these levels in isolation, overlooking complementary signals and lon...
  </details>

- **2026-11-16** — Dongjia Zhao, Yuchen Ma, Chunsheng Shi et al. — [IntentFlow: An Intent-Driven Real-Time Multimodal Search System with Image-Text Queries at Xiaohongshu](http://arxiv.org/abs/2611.20448v1)
  <details><summary>📄 Abstract</summary>
  Multimodal search with image-text queries helps users find notes in user-generated content (UGC) communities and serves as a key search tool for multimodal search agents. For such queries, query-note relevance depends on the user's retrieval intent and cannot be determined by visual or topical similarity alone. Simply reranking visual search results cannot fully address this challenge, as notes relevant to the user's intent may be missing from the initial candidate set. This motivates explicit i...
  </details>

- **2026-11-16** — Siran Peng, Tianshuo Zhang, Yibo Xue et al. — [FaceJev: Direct Visual Decisions for Face Forgery Detection](http://arxiv.org/abs/2611.21604v1)
  <details><summary>📄 Abstract</summary>
  Face forgery detection methods often perform well on seen manipulations but generalize poorly to unseen ones. Multimodal Large Language Models (MLLMs) can recognize facial parts and assess their visual plausibility. Existing MLLM-based methods typically express these judgments through textual explanations, but seldom treat individual part decisions as explicit learning targets. We present FaceJev, an MLLM-based method for face forgery detection through direct visual decisions. Following the Jev ...
  </details>

- **2026-11-16** — Jinwei Hu, Qisong He, Xinmiao Huang et al. — [Language-model agents' beliefs can be manipulated via truthful evidence in open channel](http://arxiv.org/abs/2611.21235v1)
  <details><summary>📄 Abstract</summary>
  Language-model agents' beliefs can be manipulated through open channels such as social media, even when the information they receive is truthful. When agents fill gaps between fragments with self-induced relationships, they may accept those relationships as established facts and pass the resulting rumours to others. Drawing on cognitive theory of narrative understanding and film theory of montage, we introduce Generative Montage to operationalize this failure, termed narrative overfitting, by co...
  </details>

- **2026-11-16** — Korede R. Bishi, Dominic Okonkwo, Adetayo Okunoye — [Severe but Harmless: Stress-Testing Shift Severity for Frozen Time-Series Forecasters](http://arxiv.org/abs/2611.21562v1)
  <details><summary>📄 Abstract</summary>
  Zero-shot time-series foundation models (TSFMs) have become attractive alternatives to task-specific models because they handle diverse downstream tasks, including anomaly detection and forecasting, without per-series training. However, time-series data undergo distribution shifts, and the dissimilarity between two regimes is commonly scored with statistical measures such as Wasserstein-1, where a higher score is read as a more severe shift. In systematic experiments using three established seve...
  </details>

- **2026-11-16** — Dumindu Samaraweera, Prashant Shekhar — [Detection-Efficient Watermarking for Vision--Language Agents via Risk-Constrained Strength Allocation](http://arxiv.org/abs/2611.21488v1)
  <details><summary>📄 Abstract</summary>
  Vision--language agents generate descriptions, decisions, and instructions that may be reused by users, downstream agents, and automated workflows, creating a need for provenance mechanisms that support content authenticity and post-deployment auditing without unnecessarily degrading response quality. We present a risk-aware semantic watermarking framework that combines predictive uncertainty with a zero-shot multimodal relevance-risk proxy to allocate watermark strength during decoding. A singl...
  </details>

- **2026-11-16** — Yipeng Du, Yuxi Li, Ying Zhang et al. — [WeVisForensics: Self-Evolving Agent for Omni AI-Generated Video Detection](http://arxiv.org/abs/2611.21373v1)
  <details><summary>📄 Abstract</summary>
  Recent advances in video generation call for reliable detection grounded in explicit forensic evidence. However, current methods primarily depend on single-pass chain-of-thought reasoning that overlooks brief or localized artifacts, or on predefined multi-agent workflows that offer limited flexibility in selecting relevant inspections. Even with adaptive investigation, optimizing the investigation policy alone does not directly improve the forensic capabilities of fixed experts. We introduce WeV...
  </details>

- **2026-11-16** — Iva Ewert, Felix Putze, Marvin Borsdorf et al. — [Towards Microphone-Invariant Speech Representations for Transformer-Based Voice Disorder Detection](http://arxiv.org/abs/2611.21140v1)
  <details><summary>📄 Abstract</summary>
  Automatic voice disorder detection from speech offers strong potential for early diagnosis and continuous disease monitoring. While models based on pre-trained transformers have improved detection performance, their robustness to microphone variation remains underexplored, particularly for consumer-grade devices. To the best of our knowledge, we present the first study of microphone mismatch in transformer-based binary voice disorder detection across 20 smartphone microphones. While most mismatc...
  </details>

- **2026-11-16** — Giacomo D'Amicantonio — [Region-VAD: Video Anomaly Localization and Detection via Region Selection](http://arxiv.org/abs/2611.21132v1)
  <details><summary>📄 Abstract</summary>
  Anomalies are local events, yet weakly supervised video anomaly detection scores them globally. Most methods pool an entire frame into a single vector, rank frames by that vector, and derive a location afterwards as a saliency map of the score. Full-frame pooling mixes the anomaly with its background, so a detector can reach competitive benchmark scores from scene context without being able to show where in the scene the anomaly occurs. We introduce Region-VAD, which first selects a region and t...
  </details>

- **2026-11-16** — Giacomom D'Amicantonio, Egor Bondarev — [How to Explain your Unexplainable Video Anomaly Detector](http://arxiv.org/abs/2611.21131v1)
  <details><summary>📄 Abstract</summary>
  Weakly-supervised Video Anomaly Detection (VAD) models assign anomaly scores from high-dimensional features, and their predictions remain unexplained. Saliency maps show where a model looks but not what it relies on, and the descriptions produced by Vision-Language Models (VLMs) are generated by branches that the anomaly score never reads. To address this faithfulness gap, we propose \textbf{Explain The Unexplainable (ETU)}, a classifier-agnostic framework that audits frozen VAD models through c...
  </details>

- **2026-11-16** — Zhixiang Guo, Xinming Wu, Yimin Dou et al. — [A Seismic Foundation Model for Dense Feature Extraction](http://arxiv.org/abs/2611.20745v1)
  <details><summary>📄 Abstract</summary>
  Deep-learning-based seismic interpretation is constrained by scarce high-quality annotations, and most existing models are trained separately for individual tasks. We present SeisDFE, a 7B-parameter seismic foundation model for dense feature extraction, pretrained on 5.34 million 2D images derived from more than 500 seismic volumes. A three-stage pretraining strategy, combining discriminative self-supervised learning, Gram feature anchoring, and multi-resolution adaptation, improves feature disc...
  </details>

- **2026-11-15** — Nick Ryan, Peter A. Devine, Ben Sirb et al. — [Microfitting: Continual Learning via Cached Test-Time Training](http://arxiv.org/abs/2611.20258v1)
  <details><summary>📄 Abstract</summary>
  Continual learning is a promising approach to specialize language models to an organization's private data. However, current methods exhibit a number of drawbacks including catastrophic forgetting, where new training updates overwrite prior knowledge. We present microfitting, which trains and caches a small adapter for each document. Each adapter is trained once, offline, on synthetic questions targeted at demonstrated base-model shortcomings and reused whenever that document is queried. This me...
  </details>

- **2026-11-15** — Moshe Kimhi, Idan Kligvasser, Yotam Intrator et al. — [EvoMem3D: Adaptive-Depth Temporal Representation Memory for Multi-Camera 3D Detection](http://arxiv.org/abs/2611.20241v1)
  <details><summary>📄 Abstract</summary>
  Modern multi-camera 3D detectors increasingly rely on large Vision Transformer (ViT) image encoders, making repeated full-depth encoding a dominant inference cost even though adjacent driving frames are highly redundant. We present EvoMem3D, an adaptive-depth temporal framework that caches the most recent full-depth detector-interface appearance representation as a read-only anchor and combines it with policy-selected partial features from the current frame. A lightweight pre-encoding controller...
  </details>

- **2026-11-15** — Mayank Mayank, Bharanidhar Duraisamy, Rohit Mohan et al. — [Radar Panoptic Transformer: Semantic-Guided Mask Queries for Dynamic Scene Understanding](http://arxiv.org/abs/2611.20203v1)
  <details><summary>📄 Abstract</summary>
  Automotive radar provides long-range sensing and direct Doppler velocity measurements, but its sparse and non-uniformly sampled point clouds pose significant challenges for panoptic segmentation. Dynamic objects often yield only a few detections amid a dominant static background, providing limiting the geometric cues for separating object instances. We propose \emph{Radar Panoptic Transformer (RPT)}, an end-to-end point-based network that incorporates radar-adaptive feature extraction with seman...
  </details>

- **2026-11-15** — Luciano Bozzi, Christian Celidonio, Umberto Nuzzi et al. — [Cyber-Secure Wearable, Ultra-Low-Power Networked Sensors for Soldier Health Monitoring: Insights from the CAPSARII project](http://arxiv.org/abs/2611.20187v1)
  <details><summary>📄 Abstract</summary>
  The CAPSARII project advances a cyber-secure, ultra-low-power wearable platform and Internet of Battlefield Things (IoBT) framework to support real-time monitoring of military personnel and data-driven decision support. The architecture integrates smart-textile sensing, a body/squad area mesh, edge-deployed AI on secure RISC-V microcontrollers, and cloud/federated analytics for cross-mission learning and comparative studies. Two representative use cases--pilot fatigue and warfighters operating i...
  </details>

- **2026-11-15** — Kacper Rutkowski, Radosław Poleski — [Faster $χ^2$ periodogram: Accelerating linear algebra with fast Toeplitz solvers](http://arxiv.org/abs/2611.20300v1)
  <details><summary>📄 Abstract</summary>
  In recent years, the traditional Lomb--Scargle periodogram, relying on least-squares fitting of a sinusoid to data with a known mean, has been mostly superseded by its floating-mean extension---the generalized Lomb--Scargle periodogram---due to the superior robustness and accuracy of the latter. While further generalization to higher-degree trigonometric polynomials (known as the multiharmonic analysis of variance and the fast $χ^2$ periodogram) has been known for decades, its usage remains rela...
  </details>

- **2026-11-14** —  Lokesh, Pramukto Mandal, Somanshu Juneja et al. — [StyleJudge: A Human-Validated, In-Context-Learning Vision-Language Evaluator for Artistic Style Transfer](http://arxiv.org/abs/2611.19475v1)
  <details><summary>📄 Abstract</summary>
  Automatic evaluation of artistic style transfer remains an open problem: existing metrics score an image pair in isolation, without seeing an example of the intended style transformation, and correlate poorly with human judgment. We introduce StyleJudge, a compact vision-language evaluator conditioned on a small set of reference source-to-stylized pairs before scoring a query pair, mirroring how a human rater calibrates to a style before judging a candidate. On a human-annotated benchmark of 878...
  </details>

- **2026-11-14** — Truong Thinh Nguyen, Hai Phong Nguyen, Truong Thanh Hung Nguyen et al. — [Lesion-Aware Explainable AI for Diabetic Retinopathy Grading from Fundus Images](http://arxiv.org/abs/2611.19550v1)
  <details><summary>📄 Abstract</summary>
  Post-hoc explanations of deep-learning models for diabetic retinopathy (DR) grading are difficult to trust because different attribution methods highlight different retinal regions for the same image, and a visually plausible heatmap does not show that the highlighted pixels drive the prediction. We propose the Consensus-Calibrated Explanation Map (CCEM), which fuses Grad-CAM++, Ada-SISE, and SmoothGrad Integrated Gradients (SG-IG) using image-specific weights derived from annotation-free reliab...
  </details>


### 📂 alignment
*对齐与安全约束 / Alignment & Safety Constraints* — 50 papers

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

- **2026-11-16** — Fanda Fan, Kuiye Ding, Liming Mao et al. — [MSAR: Next-Scale Autoregressive Forecasting for Time Series via Modular Multi-Scale Decoupling](http://arxiv.org/abs/2611.20714v1)
  <details><summary>📄 Abstract</summary>
  Time series forecasting underpins critical applications in finance, energy, healthcare, and transportation. Although deep models have achieved strong results, most adopt single-scale modeling or restrict multiscale processing to the input side, causing a misalignment between multiscale inputs and single-scale outputs and limiting predictive power. We introduce the Modular Scale-wise Autoregressive Framework (MSAR), a model-agnostic design that forecasts progressively across multiple temporal res...
  </details>

- **2026-11-16** — Barkin Dagda, Vinal Asodia, Iman Sharifi et al. — [Competent Autonomous Driving Through Fine Tuning Vision Language Action Models with Symbolic Traffic Rules](http://arxiv.org/abs/2611.20648v1)
  <details><summary>📄 Abstract</summary>
  Vision-language-action (VLA) models offer a unified approach to perception, reasoning, and control for autonomous driving, but accurate action prediction alone does not establish compliance with traffic regulations. This paper presents a rule-guided VLA framework that incorporates symbolic traffic-rule feedback into policy optimisation. The framework combines supervised fine-tuning on expert demonstrations with reinforcement learning (RL) refinement using a reward that encourages encoded-rule co...
  </details>

- **2026-11-16** — Ruoxuan Shi, Sheng Yang, Zhengxing Su et al. — [Safety-Preserving Medical LLM Fine-Tuning via Bilevel Data Selection](http://arxiv.org/abs/2611.20643v1)
  <details><summary>📄 Abstract</summary>
  As general large language models (LLMs) are increasingly adapted for patient-facing medical applications, improving medical capability while controlling patient-facing risks remains a critical challenge. Large-scale medical instruction data are essential for acquiring domain knowledge through supervised fine-tuning (SFT), but unsafe responses can undermine existing safety alignment. To address this problem, we propose Scalable Bilevel Data Selection (S-BDS) for safety-preserving medical SFT. By ...
  </details>

- **2026-11-16** — Nikalal Kaldera, Wanqing Li, Chris Bunn et al. — [Learning a Task-Adaptive Low-Dimensional Semantic Space for Improved Visual Classification](http://arxiv.org/abs/2611.20553v1)
  <details><summary>📄 Abstract</summary>
  Semantic visual classification commonly aligns visual embeddings with semantic spaces induced by pretrained text encoders. However, such spaces are typically high-dimensional, weakly aligned with visual feature geometry, and insufficiently discriminative for downstream classification tasks. We propose TaSS, a framework for learning a task-adaptive low-dimensional semantic space that preserves semantic structure while explicitly optimizing class separability. TaSS is constructed through a paramet...
  </details>

- **2026-11-16** — Kexin Zheng, Hui Ye, Hongbo Fu — [PromptPoseFX: Authoring Pose-Driven Visual Effects through Augmented Prompting and Interactive Refinement](http://arxiv.org/abs/2611.20485v1)
  <details><summary>📄 Abstract</summary>
  Human pose-driven visual effects offer a compelling way for enhancing video expressiveness and storytelling. Authoring such effects with traditional video editing tools is a complex and time-consuming task that requires considerable technical expertise and manual effort. While generative AI models can simplify the workflow by reducing manual scripting through language-driven generation, existing approaches suffer from imprecise alignment between visual effects and pose data, failure to preserve ...
  </details>

- **2026-11-16** — Seojin Kim, Yehjin Shin, Noseong Park — [Attention Sinks as Spectral Spikes: A Mechanism Analysis of Gated Attention](http://arxiv.org/abs/2611.20403v1)
  <details><summary>📄 Abstract</summary>
  Transformer attention exhibits attention sinks, where a small subset of source tokens absorbs disproportionate attention mass across layers. Recent work shows that post-SDPA output gating strongly reduces attention-sink behavior, while separate studies link attention sinks to gradient sinks and massive activations through backward training dynamics. Yet how the same gate affects forward sink structure, backward gradient concentration, and training-time representation signatures remains unclear. ...
  </details>

- **2026-11-16** — Simon Dräger — [Halting in Recurrent Sequence Models](http://arxiv.org/abs/2611.20377v1)
  <details><summary>📄 Abstract</summary>
  Recurrent sequence models, such as recurrent neural networks (RNNs) and state space models (SSMs), are often trained to emit an end-of-sequence (EOS) token when their output sequence is complete. During training, EOS is treated as another token without a special loss term or incentive. Although this training paradigm is widely used, it is not understood how models decide to output EOS. We study a minimal version of the EOS halting problem in which networks are trained to emit a given input seque...
  </details>

- **2026-11-16** — Arunkumar V, Manoranjan Gandhudi, Gangadharan G. R. et al. — [Optimistic Verifiers Get Hacked: Reward Hacking Under an Exact Process Oracle](http://arxiv.org/abs/2611.21538v1)
  <details><summary>📄 Abstract</summary>
  Reinforcement learning from verifiable rewards inherits whatever its verifier gets wrong. Outside mathematics and code the verifier is a proxy, a rubric, a learned judge or a hand-written checker, and its distance from the true objective is never measured, so a rising reward cannot be told apart from a hack. We build a setting where the true reward is exactly computable at the process level: executable authorization policies over 124,416 contexts admit an oracle that lists every minimal sufficie...
  </details>

- **2026-11-15** — Yuanshan Chua, Xuejiao Zhao — [GEM-MM: Reducing VLM Hallucination with Entropy-Guided Preference Alignment](http://arxiv.org/abs/2611.20016v1)
  <details><summary>📄 Abstract</summary>
  Vision-language models (VLMs) are routinely aligned with offline pairwise RLHF objectives, but multimodal preference data is scarce and treats every response token as equally informative. Under a small preference budget, pair construction becomes nearly irrelevant: standard DPO-style, image-conditional, and self-improvement objectives all perform within 1.1 points on MM-RLHF metrics and 0.5 points on hallucination rates, matching the SFT baseline. We call this entropy-blind preference optimizati...
  </details>

- **2026-11-15** — Jinfeng Xu, Zheyu Chen, Shuo Yang et al. — [Take a Step Back: A Dual-Granularity Raw Feature Empowered Intermediate Fusion Graph Convolutional Network for Multimodal Recommendation](http://arxiv.org/abs/2611.19974v1)
  <details><summary>📄 Abstract</summary>
  Although multimodal recommendations have shown the ability to learn user preferences and item properties by leveraging explicit multimodal information, they remain constrained by two critical limitations: low-quality representation learning and modality fusion. For the former, existing solutions primarily focus on multi-granularity representation learning; however, we argue that training such representations is difficult due to the inherent data sparsity problem in recommendation scenarios. For ...
  </details>

- **2026-11-15** — Taha Razzaq, Murtaza Taj, Asim Iqbal — [Multimodal AI in Healthcare: Review of Vision-Language Foundation Models for Real-World Medical Applications](http://arxiv.org/abs/2611.19958v1)
  <details><summary>📄 Abstract</summary>
  The emergence of foundation models has marked a transformative shift in AI, enabling robust generalization across diverse downstream tasks through putative zero-shot learning. Large Language Models and Vision Language Models have demonstrated strong capabilities in tasks such as image interpretation, report generation, and question answering by effectively learning from multimodal data-images paired with associated text often with minimal supervision. In the healthcare domain, this ability to al...
  </details>

- **2026-11-15** — Jinsheng Wei, Song Cheng, Bo Xiao et al. — [Bridging the Terminology Gap: A Data-Centric Alignment Framework for Multilingual Translation in Cross-Border Corporation](http://arxiv.org/abs/2611.19858v1)
  <details><summary>📄 Abstract</summary>
  As globalization accelerates the demand for seamless cross-border enterprise collaboration, multilingual translation remains bottlenecked by insufficient domain-specific terminology, rigid terminology translation, weak instruction-following capabilities, and high inference latency in long-instruction scenarios. To overcome these barriers, we propose Bridging the Terminology Gap (BTG), a data-centric framework. First, BTG mines cross-lingual term alignments from domain documents and leverages LLM...
  </details>

- **2026-11-15** — Rongxin Gao, Dongxuan Liu, Chu Li et al. — [Pros4D: Modeling Evolving 4D Worlds in Latent Space for Dynamic Spatial Reasoning](http://arxiv.org/abs/2611.19803v1)
  <details><summary>📄 Abstract</summary>
  Dynamic spatial reasoning from monocular video enables vision-language models (VLMs) to understand how 3D environments evolve over time, supporting physical world understanding and embodied intelligence. Existing efforts primarily address observed-dynamics understanding, whereas agents in dynamic environments also require future-dynamics prediction beyond the observation boundary. Moreover, external geometric processing and textual descriptions can increase inference complexity or lose informati...
  </details>

- **2026-11-15** — Dhruv Trehan, Paras Chopra — [Eliciting Research Taste in LLMs through Future Research Direction Choice](http://arxiv.org/abs/2611.19794v1)
  <details><summary>📄 Abstract</summary>
  Research taste is increasingly discussed in the context of AI scientists, yet remains little studied or measured in LLMs. This judgment matters especially in open-ended research, where a direction must be chosen before a verifiable objective is available. We operationalize research taste through one task of the scientific workflow: choosing which future research direction to pursue given a research goal and current results. Rather than predicting downstream scientometric metrics or treating auth...
  </details>

- **2026-11-15** — Chunxue Xu, Yiwei Wang, Yujun Cai et al. — [Fine-Grained RLAIF for Visual Safety: Learning to Zoom into Hazards for Multimodal Safety Alignment](http://arxiv.org/abs/2611.19786v1)
  <details><summary>📄 Abstract</summary>
  Recent multimodal safety alignment heavily relies on a text-centric paradigm, assuming risks are explicit in language or globally prominent in images. However, real-world hazards are often visually subtle or peripheral, causing existing models to fail due to their reliance on coarse, global visual representations. In this work, we study fine-grained visual safety alignment and introduce a challenging 1,200-sample benchmark across four domains, where hazards necessitate localized inspection. To a...
  </details>

- **2026-11-15** — Bowei Shan, Heng Yin — [A Threshold-Free Visual-Semantic Matching Metric for Evaluating Consistency in Subject-Driven Image Generation](http://arxiv.org/abs/2611.19780v1)
  <details><summary>📄 Abstract</summary>
  In subject-driven text-to-image generation, quantitatively evaluating localized visual consistency across varying poses and environments remains a major challenge. Existing metrics either rely on global image embeddings (CLIP, DINO) and Vision-Language Models (VLMs) that pool spatial representations and miss fine-grained textural artifacts, or depend on scalar threshold-gated dense metrics such as Visual-Semantic Matching (VSM) that suffer from point-alignment dropouts, severe threshold sensitiv...
  </details>

- **2026-11-15** — Yuming Zhang, Xianchen Zhou, Hongxia Wang — [PISG: Constraint-Aligned Signal Amplification for Diffusion-Based Combinatorial Optimization](http://arxiv.org/abs/2611.19768v1)
  <details><summary>📄 Abstract</summary>
  Diffusion-based solvers have become a prominent approach to neural combinatorial optimization. At inference time, they assign each decision variable a prediction score. A greedy decoder ranks candidates by these scores and checks hard constraints to ensure feasibility. Top-ranked candidates should be both promising and jointly feasible, making prediction-constraint alignment critical. When this alignment is weak, greedy decoding skips constraint-violating candidates and falls back to lower-ranke...
  </details>

- **2026-11-14** — Chengsheng Zhanga, Wei Li, Chenghao Sun et al. — [DBHiCo: Dual-Branch Hierarchical Contrastive Learning for MRI Image Classification](http://arxiv.org/abs/2611.19511v1)
  <details><summary>📄 Abstract</summary>
  Automated Magnetic Resonance Imaging (MRI) image classification provides a crucial non-invasive approach for neurological diagnosis, yet it is fundamentally challenged by inherent acquisition noise and high inter-subject structural similarity, which obscure subtle pathological variations, thereby limiting the performance of deep neural networks. While contrastive learning (CL) offers a promising mitigation strategy, existing paradigms rely on rigid binary partitions that ignore negative sample h...
  </details>

- **2026-11-14** — Samuel Younger — [Successive Convexification in Learned World Models for Safe Offline Planning](http://arxiv.org/abs/2611.19466v1)
  <details><summary>📄 Abstract</summary>
  World models learned from offline data allow an agent to plan without further interaction with the environment, but the sampling-based planners used with them handle safety constraints only by scoring or rejecting sampled action sequences. We instead pose safe planning in the latent space of a learned world model as a successive convex program (SCP), in which a learned discrete-time control barrier function is imposed as a constraint at every step of the horizon. SCP requires smooth dynamics, so...
  </details>


### 📂 robustness
*鲁棒性与可靠性 / Robustness & Reliability* — 60 papers

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

- **2026-11-16** — Yiyuan Ge, Changxing Ding, Ziyu Hao et al. — [Lift, See, Act: Hierarchical Robot Policy Pretraining with 3D Foundation Models](http://arxiv.org/abs/2611.20481v1)
  <details><summary>📄 Abstract</summary>
  Robot policy pretraining based on human videos is crucial for improving the policy's generalization ability. One main challenge for this task is the lack of explicit action-relevant representations in such unlabeled data. Recent works tend to estimate 3D hand motion trajectories from videos using 3D foundation models (3D FMs). However, they keep solely the sparse trajectories as supervision, ignoring the rich, fine-grained information produced during the trajectory extraction process. To address...
  </details>

- **2026-11-16** — Wenhao Li, Chong Xiao, Xiaokun Bai et al. — [Words Speak Louder? Exploring the Language Shortcut of LLM-Driven Incomplete Multimodal Learning](http://arxiv.org/abs/2611.20349v1)
  <details><summary>📄 Abstract</summary>
  Is a face or a voice still heard once the words are known? Incomplete multimodal learning increasingly uses large language models (LLMs) as fusion engines: modality features enter as token blocks and missing modalities become placeholders. We find that LLM-driven fusion can override non-verbal evidence it can read. Contrasting its full-input prediction with counterfactual views, the same model shown one modality or no content, we identify language shortcuts. We build MR-Bench: MR-Bench-A types e...
  </details>

- **2026-11-16** — Jorge Valverde-Rebaza, Nathan Garcia-Larios, Karime Ruvalcaba-Perez et al. — [Evaluating Cultural Reasoning and Robustness in LLMs for Spanish Political Discourse](http://arxiv.org/abs/2611.21535v1)
  <details><summary>📄 Abstract</summary>
  Large language models (LLMs) are increasingly used to interpret, generate, and mediate public-facing language, which makes their reliability especially consequential in politically sensitive settings. Although sentiment analysis is a common task in this area, affective meaning in social media discourse is often conveyed through culturally situated and pragmatically indirect cues that are not well captured by label-centric evaluation alone. In this paper, we evaluate the robustness of LLMs for se...
  </details>

- **2026-11-16** — Xuexin Liu, Zengyi Wo, Shiyu Zhang et al. — [ExRel: Learning Directed Reuse Relevance between Rich-Text K-12 Question Images with Executable Relation Contracts](http://arxiv.org/abs/2611.21461v1)
  <details><summary>📄 Abstract</summary>
  In K-12 education, question images combine text, mathematical expressions, diagrams, and diverse layouts. Variations in wording, conditions, answer options, or task scope can substantially alter their reuse utility despite visual similarity. We formulate this problem as directed reuse relevance, grading candidate utility as Strong, Medium, or Weak. However, generic similarity scores overlook task-specific reuse requirements, while natural supervision is dominated by Strong relations and lacks fi...
  </details>

- **2026-11-16** — Hassan Munif, Anthony Couthures, Vineeth Satheeskumar Varma et al. — [Robust Action Clusters and Cascades in Opinion Dynamics with Heterogeneous Action Thresholds](http://arxiv.org/abs/2611.21446v1)
  <details><summary>📄 Abstract</summary>
  We study the preservation and propagation of public actions in networks whose agents hold continuous private opinions. Agents update their opinions from their neighbors' observed actions and express them through action rules whose thresholds differ across agents. We characterize groups of agents that preserve a given common action regardless of the outsiders' actions. We call such a group, paired with that action, a robust action cluster. We show that a group is a robust action cluster for that ...
  </details>

- **2026-11-16** — Daniel Baumartz, Alexander Mehler, Patrick Schrottenbacher et al. — [Rubric-Based AES with LLM Ensembles: Scoring of Student Responses in Critical Online Reasoning Using Ensembles of LLMs](http://arxiv.org/abs/2611.21422v1)
  <details><summary>📄 Abstract</summary>
  Grading student responses is costly and time-consuming. Moreover, human annotators are prone to bias, fatigue, and rater drift, which further limits grading reliability. Various methods have been employed to develop automated essay scoring (AES) systems to reduce these costs and address bias-related issues. These methods range from early text-feature-based systems to current machine-learning and transformer-based models. Specifically, large language models (LLMs) offer the potential to streamlin...
  </details>

- **2026-11-16** — Oumaya Ladhari, Matthieu Saubanère, Jérémie Messud — [Success Probability of Block-Encoding Methods](http://arxiv.org/abs/2611.21080v1)
  <details><summary>📄 Abstract</summary>
  Block-encoding methods apply nonunitary functions $f(\widetilde H)$ of a normalized Hermitian operator on a quantum computer, but only upon a successful postselection, which introduces a shot overhead rarely included in resource estimates. We analyze the success probability $p^{(f)}_{\mathrm{success}}=\sum_n w_n|f(\tilde E_n)|^2$ of three constructions, namely linear combination of unitaries (LCU), qubitization and quantum singular value transformation (QSVT), where $w_n$ are the weights of the ...
  </details>

- **2026-11-16** — N. Bucciantini, L. Del Zanna — [A 3+1 formalism for self-similar expanding grids in computational relativistic and Newtonian magnetohydrodynamics](http://arxiv.org/abs/2611.20865v1)
  <details><summary>📄 Abstract</summary>
  Astrophysical systems frequently undergo spatial expansion during their evolution. Simulating these systems with standard conservative codes for hydrodynamics and magnetohydrodynamics using fixed grids is challenging, particularly when attempting to preserve high resolution across vast changes in physical scale. While moving or expanding meshes, or adapting mesh refinement, can address this issue, they introduce computational complexity and are notoriously difficult to implement robustly. We aim...
  </details>

- **2026-11-16** — Lion Jasper Gleiter, Tingying Peng — [Interpretable deep concepts of organoid morphology](http://arxiv.org/abs/2611.20840v1)
  <details><summary>📄 Abstract</summary>
  Image-based classification of organoid morphologies can indicate drug response, viability, or successful differentiation. In recent work, learned representations outperform handcrafted features as the basis for downstream classifiers. However, their black-box nature hides the morphological cues a classifier relies on. Based on the foundation models DINOv3 (general-purpose) and ViTAMIn-O (organoid-specific), we train sparse autoencoders (SAEs) to learn interpretable concepts related to distinct o...
  </details>

- **2026-11-16** — Roméo Zapata, Bleuenn Belz, Xingyu Yang et al. — [Material Tailored Multispectral Magnetization via the Inverse Faraday Effect in Tunable Coaxial Nanoantenna](http://arxiv.org/abs/2611.20735v1)
  <details><summary>📄 Abstract</summary>
  All-optical control of magnetization via the Inverse Faraday Effect presents a transformative pathway for ultrafast high-density data storage and nanoscale spintronics. However, unlocking its full potential requires moving beyond traditional gold-centric, narrowband constraints. In this study, we present a comprehensive theoretical framework evaluating IFE-driven static magnetic field generation across a diverse library of plasmonic materials, including gold, silver, copper, aluminum, and titani...
  </details>

- **2026-11-16** — Haiteng Wang, Haoze Li, Jingwei Guo et al. — [IndustrialKnowEval: A Benchmark for Evaluating Multi-Level Industrial Knowledge in LLMs](http://arxiv.org/abs/2611.20695v1)
  <details><summary>📄 Abstract</summary>
  Large language models (LLMs) are increasingly explored for industrial tasks, yet few benchmarks evaluate their mastery of industrial knowledge across different types of cognitive demand. We introduce IndustrialKnowEval (IndKnow), a benchmark for industrial knowledge and engineering question answering. It contains 43,282 samples covering 21 task types across seven industrial sectors, including aerospace, electric power, and metallurgy, organized into four levels of cognitive demand: memory, compr...
  </details>

- **2026-11-16** — Yuchen Fan, Chang Wei, Pao-Hsiung Chiu et al. — [Newton-PINet: A fast physics-informed neural network with Newton linearization for meta-learning nonlinear PDEs](http://arxiv.org/abs/2611.20609v1)
  <details><summary>📄 Abstract</summary>
  Scientific machine learning has opened new avenues for solving parameterized partial differential equations (PDEs), enabling models to learn a family of PDEs and generalize to unseen instances. In this context, data-driven operator learning methods typically require large training datasets, while physics-informed neural networks (PINNs) suffer from difficult optimization and limited generalization, especially for nonlinear PDEs. We propose Newton-PINet, a physics-informed network enhanced by New...
  </details>

- **2026-11-16** — Jia-Xiao Su, Xiang-Chuan Yan, Hai-Xia Li — [A widely-tunable printed-circuit-board-based resonant electro-optic modulator](http://arxiv.org/abs/2611.20590v1)
  <details><summary>📄 Abstract</summary>
  We present a simple, printed-circuit-board (PCB)-based resonant electro-optic modulator (EOM) featuring a wide operational frequency range. By utilizing a low-loss, high-frequency variable capacitor, the resonant frequency can be continuously tuned by typically 30% within a single band, e.g., from 161.0 MHz to 233.5 MHz. Furthermore, by swapping a radio-frequency transformer, the EOM's resonance is reconfigurable across the 17.7-489.7 MHz range, with quality factors ranging from 46 to 109. Using...
  </details>

- **2026-11-16** — Hongbo Zhang, Liuyang Song, Hang Zhou et al. — [VAHBench: A Harness Benchmark for Agentic Long-Video Generation](http://arxiv.org/abs/2611.20535v1)
  <details><summary>📄 Abstract</summary>
  AI agents are commonly used for everyday information retrieval and coding. We ask whether they can also interpret human requests and turn them into complete videos. We introduce VAHBench, a benchmark that tests this ability through five short-drama briefs specifying story, characters, dialogue and duration. Agents plan and carry out production using shared generation tools. Evaluation combines video completeness and basic quality with checks of production reliability and reporting accuracy. Acro...
  </details>

- **2026-11-16** — Mao Guan, Qian Chen, Ge Meng et al. — [FinVerify: A Verification Framework for Financial Agents](http://arxiv.org/abs/2611.20423v1)
  <details><summary>📄 Abstract</summary>
  Financial agents produce numerical claims that can be wrong even when their calculations execute correctly, due to mismatched reporting periods, unsupported sources, incompatible units, or incorrect financial definitions. We introduce FinVerify, an evidence-grounded framework for verifying financial agents' numerical claims. Based on an analysis of 190 incorrect trajectories from the Agent Finance Reasoning dataset, we define five error categories--temporal integrity, source fidelity, comparabil...
  </details>

- **2026-11-16** — Ilya A. Shkrob — [A Structural Framework for Succession: Continuation, Recognition, and Realization](http://arxiv.org/abs/2611.20422v1)
  <details><summary>📄 Abstract</summary>
  Succession asks whether an entity encountered later is the same entity that entered an arrangement earlier. For an artificial system that is fine-tuned, distilled, or copied, it has to be answered. We look for a mathematical structure weak enough to cover any such case and strong enough to support general theorems, so that results follow from the structure's conditions rather than from a particular pipeline or criterion. Succession is modeled on state/modification graphs with relational lifts th...
  </details>

- **2026-11-15** — Liyan Wang, Longze Li, Mohamed Hassan et al. — [NEBench R1: a Reasoning Benchmark for Evaluating Nuclear Domain Competence in Large Language Models](http://arxiv.org/abs/2611.21682v1)
  <details><summary>📄 Abstract</summary>
  Large language models (LLMs) are increasingly being explored for knowledge-intensive and safety-critical applications in nuclear engineering. However, existing nuclear-domain benchmarks provide limited content coverage or focus primarily on answer accuracy without systematically evaluating the quality of the underlying reasoning. This study introduces NEBench R1, a reasoning-oriented benchmark comprising 7,546 unique multiple-choice questions extracted from U.S. Nuclear Regulatory Commission (NR...
  </details>

- **2026-11-15** — Chaoqun He, Wannian Yi, Changyi Sun et al. — [Learning When to Continue and When to Stop: Termination-Aware OPSD](http://arxiv.org/abs/2611.19925v1)
  <details><summary>📄 Abstract</summary>
  On-Policy Self-Distillation (OPSD) improves language model reasoning by distilling from a frozen teacher initialized identically to the student and conditioned on privileged information. However, we identify an underexplored termination mismatch in OPSD: the student fails to reliably learn when to continue and when to stop. This mismatch manifests in two opposing failure modes-premature termination, where reasoning stops before sufficient progress is made, and repetition-driven over-generation, ...
  </details>

- **2026-11-15** — Paul Deepakraj Retinraj — [When Facts Change, Which Decisions Break? Dependency-Aware Context Graphs for Agents](http://arxiv.org/abs/2611.19859v1)
  <details><summary>📄 Abstract</summary>
  When an observed fact changes, an agent must identify and repair the decisions that depend on it while preserving unaffected outputs. We investigate the reliability-cost trade-off of field-level dependency graphs extracted from actual agent read traces. A controlled benchmark spans three executable workflow domains and four successive updates, with independent imperative and expression-based references. Across 120 workflows, two models and two repeated runs, we compare full recomputation, rollin...
  </details>

- **2026-11-15** — Jiahang Liu, Wenbo Zhang, Junsong Wang et al. — [DoF-Query Transformer for Adaptive Fusion of Egocentric Vision and Forearm HD-sEMG in Continuous Hand Kinematics](http://arxiv.org/abs/2611.20196v1)
  <details><summary>📄 Abstract</summary>
  Continuous and accurate estimation of human hand kinematics is important not only for intuitive human-machine interaction, but also for capturing fine-grained human manipulation demonstrations that can provide action supervision for embodied-intelligence datasets and dexterous robot learning. However, individual sensing modalities may be insufficient for reliable estimation under varying operating conditions. We present a finger-unencumbered multimodal framework for continuous regression of 20 h...
  </details>

- **2026-11-15** — Yimin Han, Jiahui Zhang, Wanyue Li et al. — [MoViC: Real-Time Humanoid Whole-Body Control from Monocular Video Streams](http://arxiv.org/abs/2611.19998v1)
  <details><summary>📄 Abstract</summary>
  Real-time whole-body imitation from monocular video requires both a robust universal tracker and high-quality real-time reconstruction. We present MoViC, a framework that uses live RGB video as a control signal for humanoid robots without wearable tracking devices. The framework combines monocular human motion reconstruction, robot retargeting, and a transformer-based behavior foundation model. The policy receives proprioceptive history, a single explicit next-step reference, and a compact frequ...
  </details>

- **2026-11-15** — Haoran Yu, Lifei Liu, Danping Zhang — [Reliable Mining of Heterogeneous AI Coding-Agent Data: Context-Aware Prediction and Resource-Aware Ranking](http://arxiv.org/abs/2611.20297v1)
  <details><summary>📄 Abstract</summary>
  Operational records from AI coding agents differ across agents, repositories, tasks, and workflows. We study 71,677 pull requests (PRs) from six agents and show that pooling these records can reverse descriptive and predictive conclusions. PRs carrying a co-authorship trailer have a 55.6% merge rate, compared with 77.5% without the trailer, but removing the dominant agent flips this -21.8 percentage-point gap to +23.7 points. We treat this Simpson-type reversal as a data-veracity problem and rep...
  </details>

- **2026-11-15** — Ali Şenol — [The Silent Cost of Conversation History in LLM Reasoning](http://arxiv.org/abs/2611.20071v1)
  <details><summary>📄 Abstract</summary>
  Large language models (LLMs) in multi-turn information systems accumulate their own earlier replies and a growing task state. We asked whether this conversation history lowers accuracy, and whether process-level quality metrics warn before it does. Each analysis was fixed before its outcomes were computed. In Study 1, on 48 sharded math tasks, retaining its replies lowered final success by 0.21 for GPT-4o-mini and 0.29 for Mistral-7B (Holm-adjusted p = 0.026 and 0.004); Llama-4 Scout showed the ...
  </details>

- **2026-11-15** — Ruirui Shen, Jianqi Gao, Xiangfeng Luo et al. — [SAGE-VQA: A Training-Free, Self-Evolving Agentic Framework with Grounded Evidence for Knowledge-Based Visual Question Answering](http://arxiv.org/abs/2611.19933v1)
  <details><summary>📄 Abstract</summary>
  Knowledge-based visual question answering (KB-VQA) aims to combine visual information with external knowledge to answer user questions. Existing methods face two main bottlenecks: visual perception errors can propagate into hallucinations, and generalization across scenarios remains limited. To address these issues, we propose SAGE-VQA (Self-evolving Agent framework with Grounded Evidence), a training-free agentic framework that combines evidence verification with experience evolution. Our key i...
  </details>

- **2026-11-15** — Thilo Tamme, Anton Hantel, Jakob Scheppers — [Who Writes the Codebook? An Eight-Step Framework for Auditing LLM-Generated Category Systems](http://arxiv.org/abs/2611.19872v1)
  <details><summary>📄 Abstract</summary>
  Large language models (LLMs) increasingly create the categories through which qualitative evidence is interpreted. Existing coding benchmarks often hold these categories fixed. We propose the Qualitative Variance Audit Framework, an eight-step method that compares codebook creation, repeated application and code distributions under controlled inputs. It combines model-owned and shared-reference codebooks to distinguish variation in the overall pipeline from application differences within a commo...
  </details>

- **2026-11-15** — Yuxiang Mei, Dongxing Xu, Yanhua Long — [A Speech-LLM Framework for Enrollment-Free Wake-Word-Guided Target-Speaker Recognition in Complex Noisy Scenarios for Seamless Human-Machine Interaction](http://arxiv.org/abs/2611.19844v1)
  <details><summary>📄 Abstract</summary>
  Target-speaker automatic speech recognition (TS-ASR) is essential for reliable human-machine interaction in complex acoustic environments, where overlapping speech and background noise make it difficult to identify and recognize the intended speaker. Existing approaches typically rely on speaker enrollment or cascaded processing pipelines, limiting their flexibility in practical applications. To address these limitations, we propose an enrollment-free Speech-LLM framework that leverages wake-wor...
  </details>

- **2026-11-14** — Gurpriya Bhatia, Clifford Neuman — [Protecting the System, Stranding the User: The Limits of Multi-Agent Authorization](http://arxiv.org/abs/2611.19598v1)
  <details><summary>📄 Abstract</summary>
  Current multi-agent authorization architectures prioritize system integrity over human outcomes. While recent models successfully prevent privilege escalation, they externalize the cost of failure onto the human operator. Re-centering authorization around human impact exposes four structural vulnerabilities in current paradigms. First, calling an agent's understanding of user intent verified is misleading. Intent has no formal definition, so no check against it can be definitive. Systems should ...
  </details>

- **2026-11-14** — Jerome Henry, Swadhin Pradhan, Amine Choukir — [Diagnosis as Percolation on an Evidence Graph: Root-Cause Recoverability in Network Fault Diagnosis](http://arxiv.org/abs/2611.19584v1)
  <details><summary>📄 Abstract</summary>
  Diagnosing failures from incomplete observations presents three challenges: determining whether sufficient evidence connects a possible cause to a symptom, distinguishing the true cause from plausible alternatives, and assessing when a diagnosis can be trusted. We introduce an evidence-graph framework that separates these challenges and uses percolation theory to analyze how missing information affects cause-symptom connectivity. In controlled simulations with an average degree of four, a giant ...
  </details>

- **2026-11-14** — Fernando Cardenas Piepereit — [Before the Word: Name Information in Description-Derived States of Small Language Models, With and Without Naming Failure](http://arxiv.org/abs/2611.19609v1)
  <details><summary>📄 Abstract</summary>
  The tip-of-the-tongue (TOT) state, knowing an object but not its name, motivates this study as an analogy only. We ask whether small language models form a name-predictive state from a name-free description, and whether it differs when naming fails but description selection succeeds. In an internally pre-registered study (a frozen document, no external registry) of Qwen2-0.5B, SmolLM2-1.7B and Phi-3-mini with 200 items, we combine a similarity read-out, a Patchscopes-style read-out and activatio...
  </details>

- **2026-11-14** — Shi Li, Lalith Sharan, Joël L. Lavanchy et al. — [EndoComparer: Comparative Surgical Video Question Answering with Pseudo-Siamese Visual Adaptation and Perceive-then-Compare Reasoning](http://arxiv.org/abs/2611.19578v1)
  <details><summary>📄 Abstract</summary>
  Purpose: Surgical training benefits from explicit comparison between cases: in patient condition, in technique and in skill proficiency. Surgical vision-language models (VLMs) offer a promising and flexible interface for this purpose. Yet current VLMs typically see one video at a time, and they often fall short when asked to compare videos. Methods: We propose EndoComparer, a VLM for comparative surgical video question answering with two components. (a) A Pseudo-Siamese Visual LoRA (PSVL) gives ...
  </details>


### 📂 watermark
*水印与溯源 / Watermarking & Provenance* — 11 papers

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

- **2026-11-16** — Andreas Ekelhart, Ahmad Mohsin, Iqbal H. Sarker et al. — [Expertise capture in workplace AI](http://arxiv.org/abs/2611.21456v1)
  <details><summary>📄 Abstract</summary>
  AI assistants are becoming part of how knowledge workers think and perform, accumulating the prompts, exemplars, memory and interaction histories that encode a worker's professional judgment. This infrastructure typically runs under employer or platform control. We name the resulting process expertise capture, the absorption of worker-applied knowledge and judgment into AI resources under organizational control. We develop a framework of contribution forms, technical residences and transformatio...
  </details>

- **2026-11-16** — Carlo Alberto Barbano, Giovanni Marraffini, Demian Wassermann — [Open-fMIND: A Large-Scale Open-Access fMRI Corpus for Pretraining Brain Foundation Models](http://arxiv.org/abs/2611.21215v1)
  <details><summary>📄 Abstract</summary>
  Self-supervised pretraining has transformed language and vision, but its application to functional MRI (fMRI) is constrained by data access. The largest standardized fMRI resources are governed by data use agreements and dominated by a small number of acquisition protocols, while the thousands of openly licensed datasets on OpenNeuro are individually small, heterogeneously organized, and unprocessed. We present the first release of Open-fMIND, a uniformly preprocessed, openly accessible corpus o...
  </details>

- **2026-11-16** — Zixuan Wang, Gregory Kang Ruey Lau, Xiao Tian et al. — [EDITORS Know Your Style! Editing LoRA Subspaces for Stylistic Attribution and Imitation](http://arxiv.org/abs/2611.20846v1)
  <details><summary>📄 Abstract</summary>
  Disentangling writing style from semantic content is a fundamental challenge in literary text modeling. Style-content entanglement causes models to rely on semantic content for authorship attribution (AA) tasks and memorize author-specific content for style imitation (SI) tasks. We propose EDITORS (EditingLoRA Subspaces), a diagnose-then-deflate framework that adapts pretrained large language models and prioritizes stylistic features, making it effective for both AA and SI tasks. EDITORS first t...
  </details>

- **2026-11-16** — Yuchong Hu, Zhao Zhang, Ziyao Zhao et al. — [Evidence Diet: When Graph Evidence Helps LLMs Rank Competing Candidates](http://arxiv.org/abs/2611.20837v1)
  <details><summary>📄 Abstract</summary>
  When several candidates have graph support, does it matter which candidate receives which supporter and path counts? We study how LLM rankers use collaborative evidence on Amazon Books and MovieTV. Swapping user-level evidence degrades ranking, while matched item substitutions have little effect. On fixed clean-trained checkpoints, unrelated catalog text lowers Hit@1 from 44.77% to 38.70%, with 99.9% of rankings still valid. Across all three paired seeds, the NDCG@5 difference between count and ...
  </details>

- **2026-11-16** — Xuannan Liu, Tian Lan, Zekun Li et al. — [TrainExplorer: Autonomous LLM Post-Training via Plan-and-Decouple Exploration](http://arxiv.org/abs/2611.20430v1)
  <details><summary>📄 Abstract</summary>
  LLM-based agents can automate model post-training, accelerating progress toward recursive self-improvement. Despite their promise, existing approaches remain under-explored and face two main challenges: (1) strategy lock-in that limits exploration beyond the initial strategy; and (2) coupled execution that obscures the effects of individual modifications. To address these challanges, we propose TrainExplorer, a multi-agent framework for autonomous post-training, that incorporates strategy planni...
  </details>

- **2026-11-16** — Yiwei Fu, Nicholas Gabriel — [Deploying a Control-Logic LLM Assistant in Air-Gapped Power Plants: Lessons in Source Authority and Bounded Retrieval](http://arxiv.org/abs/2611.20398v1)
  <details><summary>📄 Abstract</summary>
  Deploying Large Language Model (LLM) assistants in industrial operational technology environments poses constraints largely absent from cloud applications: site policies restrict engineering and operational data from leaving the plant, on-premises compute is limited, and incorrect causal attribution can mislead incident response. We report lessons from deploying a control-logic evidence layer that underpins a broader on-premises operator assistance system at two gas power plants. Two prototypes ...
  </details>

- **2026-11-15** — Bart M. N. Smets, Gijs Bellaard, Pieter Wils — [Symmetry Fingerprinting with Geometric Learnable Invariants Transformers](http://arxiv.org/abs/2611.20150v1)
  <details><summary>📄 Abstract</summary>
  Geometric deep learning has made available a large variety of structurally equivariant neural network architectures, meaning a particular transformation of their input causes a predictable transformation of their output. But structural equivariance is a very strong inductive bias that can limit performance if chosen poorly. In contrast, choosing an architecture with low geometric bias necessitates data augmentation to obtain correct behavior; extending the training process. We propose a novel ne...
  </details>

- **2026-11-15** — Antonio Alcántara, Ioannis Karampinis, Spyros Chatzivasileiadis — [The Grid's Own Language: A Common Information Model Layer for LLM Grid Assistants](http://arxiv.org/abs/2611.20026v1)
  <details><summary>📄 Abstract</summary>
  Assistants built on large language models (LLMs) are entering power system operation. Current designs delegate computations to validated solvers, but the agent still infers the type, role and state of each element from its name and tool-specific formats, and errors propagate to every study. The Common Information Model (CIM), the IEC standard in which operators already exchange network models, defines unambiguously what each element is and how it connects. We propose a CIM layer for LLM grid ass...
  </details>


### 📂 unlearning
*机器遗忘 / Machine Unlearning* — 1 papers

- **2026-11-16** — Zirui Pang, Zhijie Deng, Yuancheng Wang et al. — [LEAF-OPD: Learning to Forget from Privileged Contexts via On-Policy Distillation](http://arxiv.org/abs/2611.20674v1)
  <details><summary>📄 Abstract</summary>
  LLM unlearning aims to erase targeted knowledge from large language models while preserving their utility. However, many existing methods suppress target knowledge without explicitly teaching the model how to respond to queries about it. We propose LEAF-OPD (LEArning to Forget from Privileged Contexts via On-Policy Distillation), in which a frozen teacher provides token-level supervision on student-generated responses. On forget data, the teacher uses privileged contexts (instructions not to rev...
  </details>


### 📂 survey
*综述与系统化 / Surveys & Systematization* — 9 papers

- **2026-11-17** — Junseong Pyo, Hyeongjin Kim, Jongwook Han et al. — [PAIR: Bringing Household Robots into the Smart Home](http://arxiv.org/abs/2611.23070v1)
  <details><summary>📄 Abstract</summary>
  Household robots often need to operate appliances, and smart appliances offer both control panels and device APIs. Existing embodied AI simulation environments, however, model appliances solely as physical objects. We introduce PAIR, a smart-home simulation environment grounded in the Matter protocol~\footnote{https://csa-iot.org/all-solutions/matter/}, the industry standard for smart-home devices. PAIR provides 84 smart-device assets whose functional control panels and APIs act on a shared devi...
  </details>

- **2026-11-16** — Dario Fenoglio, Martin Gjoreski, Marc Langheinrich et al. — [WebAgents: Unbundling Agent Creation, Hosting, and Execution for an Agent-Native Web](http://arxiv.org/abs/2611.21978v1)
  <details><summary>📄 Abstract</summary>
  Large language models are moving from isolated assistants toward autonomous agents that can plan, use tools, and coordinate with others, motivating an emerging Agentic Web of independently developed agents and services. Realizing this vision requires agent behavior to move across creators, hosts, and runtimes without coupling publication to a particular execution environment or transferring authority over user resources. We introduce WebAgents, which unbundles these roles through a signed agent....
  </details>

- **2026-11-16** — Yongkang Xiao, Qiyi Deng, Jing Chen et al. — [MASTA: A Feedback-Scheduled Multi-Agent System for End-to-End Tamarin Modeling and Analysis](http://arxiv.org/abs/2611.20671v1)
  <details><summary>📄 Abstract</summary>
  Tamarin-based formal verification of security protocols requires expert-authored multiset rewriting rules and temporal-logic lemmas. Translating a natural-language protocol description into a complete formal model with an LLM is hard because syntactic, reachability, and property-level errors compound across the multi-step modeling process, and a single agent that both authors and self-evaluates cannot reliably localize them. We present MASTA, a multi-agent system that addresses these difficultie...
  </details>

- **2026-11-16** — Gustavo Pinto, Enne Rebeca Silva de Freitas, Danilo Monteiro Ribeiro — [Is This Code Mine? Student Ownership When AI Agents Write the Spec and the Code](http://arxiv.org/abs/2611.21501v1)
  <details><summary>📄 Abstract</summary>
  Software engineering courses are starting to ask students to build entire systems with AI coding agents, but little is known about what students actually do with them and whether they still own what they deliver. If the agent writes both the code and the decisions behind it, the artifacts we grade no longer show what students learned. We studied an assignment in which 18 pairs of students built applications with agents under Spec-Driven Development, combining the mined history of their repositor...
  </details>

- **2026-11-16** — Jason Alexander, Yuxuan Li, Michael Licamele et al. — [A Crowd-Audited Atlas of Implicit Bias in LLM-Powered Agents](http://arxiv.org/abs/2611.21376v1)
  <details><summary>📄 Abstract</summary>
  Prior work has shown that large language models (LLMs) express implicit biases in high-publicity, one-off decision scenarios such as hiring and intelligence assessment. However, as people increasingly employ autonomous, LLM-powered AI agents that make decisions on their behalf in doing day-to-day tasks, it is of critical importance that we understand how implicit biases, based on sociodemographic assumptions, emerge across a broad milieu of workaday decision scenarios. We used the 17 domains of ...
  </details>

- **2026-11-16** — Berkay Günes, Giuseppe Viterbo, Sven Buder et al. — [A COMPASS to the Galaxy: Joint nucleosynthetic yield set comparison and parameter inference in Galactic chemical evolution](http://arxiv.org/abs/2611.21175v1)
  <details><summary>📄 Abstract</summary>
  Galactic Chemical Evolution (GCE) models connect stellar nucleosynthesis to observed abundance patterns, but their interpretation requires simultaneous parameter inference and comparison between competing stellar yield prescriptions. This remains challenging due to intractable likelihoods and growing dataset complexity. Using compass, a novel simulation-based inference framework, we perform, for the first time, amortized joint Bayesian model comparison and parameter inference for GCE models with...
  </details>

- **2026-11-16** — Aspen Wang, Yen Yu Shan, Lun-Wei Ku — [Necessary for What? Auditing Demographic Disclosure to LLM Synthetic Respondents](http://arxiv.org/abs/2611.20606v1)
  <details><summary>📄 Abstract</summary>
  Large language models (LLMs) increasingly answer surveys on behalf of real panelists, and each panelist's recorded demographic attributes (e.g., age, education, ethnicity) are often placed in the prompt on the premise that richer profiles make more faithful synthetic respondents. While data minimization limits personal data to what a purpose requires, a synthetic survey serves several purposes at once, from predicting individual answers to estimating how opinions are distributed and comparing gr...
  </details>

- **2026-11-15** — Peng Wu, Seyede Fatemeh Ghoreishi, Nathan Bastian et al. — [Ontology-Compiled Control Barrier Functions for Heterogeneous Robot Teams](http://arxiv.org/abs/2611.20306v1)
  <details><summary>📄 Abstract</summary>
  Safety filters for heterogeneous robot teams fail because of missing constraints, overestimated braking capabilities and conflicts between individually satisfiable constraints. We present OntoCBF, which compiles a domain ontology with a class taxonomy, typed relations, safety axioms and a dynamics profile per robot class into a control barrier function filter with one quadratic program per agent. Description-logic entailment supplies the constraints of any team online, including those that follo...
  </details>

- **2026-11-15** — Victória Gomes, Fabio Palomba, Robert Feldt et al. — [The Hidden Methodological Layer: Uncovering Threats to Validity in LLM-Assisted Empirical Software Engineering](http://arxiv.org/abs/2611.20033v1)
  <details><summary>📄 Abstract</summary>
  Context: Large Language Models (LLMs) are increasingly embedded in empirical software engineering (ESE) workflows, supporting tasks such as classification, coding, extraction, synthesis, and evaluation. Their probabilistic and opaque behavior, however, introduces methodological concerns that may affect empirical rigor. Aims: This paper investigates threats to validity introduced by LLM-assisted empirical workflows and examines how LLM interactions influence empirical studies. Method: We conducte...
  </details>


### 📂 other
*其他安全相关 / Other Security-Related* — 183 papers

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

- **2026-11-16** — Haixiang Wu, Zhihao Guan, Yang Yang — [ACiT: Proprioceptive-Prior Action Chunking with Inverted Transformers](http://arxiv.org/abs/2611.20719v1)
  <details><summary>📄 Abstract</summary>
  Visuomotor policies condition action prediction on visual and proprioceptive observations. While historical proprioceptive sequences carry rich dynamic priors, current methods treat them as equal to high-dimensional vision, causing the proprioceptive signal to be overwhelmed. To identify what is lost in equal-conditioning fusion, we analyze proprioceptive data and find that strong inter-joint coupling is the key action-determining structure. This finding aligns with the neural sensorimotor loop,...
  </details>

- **2026-11-16** — Sachin Gupta — [AgentFaultBench: State-Verified Evaluation of Tool-Fault Recovery](http://arxiv.org/abs/2611.20711v1)
  <details><summary>📄 Abstract</summary>
  Does recovery advice help an agent finish a task after a tool fails? AgentFaultBench evaluates LangGraph and CrewAI agents performing specified tasks in an isolated GitLab installation. We inject tool errors and check both the resulting files and issues and the required reads, verification and final response. The prompt supplies the expected issue and report text, so the task tests execution rather than content generation. In the primary comparison of 1,944 planned runs, advice changes success b...
  </details>

- **2026-11-16** — Fengmin Wu, Sicong Liu, Zimu Zhou et al. — [UbiHearo: Bringing Scenario-Aware Sound Guidance to DHH Users with Mobile Agents](http://arxiv.org/abs/2611.20686v1)
  <details><summary>📄 Abstract</summary>
  For Deaf and Hard-of-Hearing (DHH) users, effective sound awareness goes beyond detecting \emph{what} sound occurs; it requires understanding \emph{what it means}, \emph{how urgent it is}, and \emph{what to do}. However, existing mobile assistants largely reduce acoustic scenes to isolated labels or generic alerts, failing to provide contextual guidance when the same sound implies different risks across scenarios. We present \sysname, a mobile hearing assistant agent that closes the sensing--rea...
  </details>

- **2026-11-16** — Kangjie Zhou, Sukai Wang, Yuhan Xiao et al. — [Learning and Verifying Progress: Closed-Loop Agentic Planning with Progress-Enhanced Execution for Long-Horizon Vision-Language Navigation](http://arxiv.org/abs/2611.20676v1)
  <details><summary>📄 Abstract</summary>
  Long-horizon vision-language navigation (VLN) requires agents to track instruction progress and recover from local errors before they propagate across subtasks. However, executors trained on expert trajectories encounter policy-induced state shifts during deployment, and their stop signals do not reliably indicate subtask completion. We introduce Learning and Verifying Progress for VLN (LeaP-VLN), an agentic VLN system that couples progress-aware execution with independent progress verification ...
  </details>

- **2026-11-16** — I. V. Solovyev — [Molecular-orbital origin of weak orbital ferromagnetism and anomalous Hall effect in a trimerized kagome antiferromagnet](http://arxiv.org/abs/2611.20632v1)
  <details><summary>📄 Abstract</summary>
  We reveal the molecular-orbital origin of weak orbital ferromagnetism and the anomalous Hall effect (AHE) induced by noncollinear spin order in a trimerized kagome lattice. By transforming to the molecular-orbital basis of an isolated trimer in the double-exchange regime, we derive an effective low-energy model for the states with opposite orbital angular momenta $m= \pm 1$ subject to an effective Zeeman field arising from spin chirality and spin-orbit (SO) coupling. In this representation, the ...
  </details>

- **2026-11-16** — Haipeng Wang — [A Self-Evolving Agent Runs Like a Gas: Describing and Predicting Its Evolution with Fluid Dynamics](http://arxiv.org/abs/2611.20584v1)
  <details><summary>📄 Abstract</summary>
  A self-evolving LLM agent improves in service by rewriting its own plugin library under a validation gate. Agent engineering is converging on exactly such agents: single systems in continuous operation, carrying populations of runtime instances (plugins, skills, tools) past the point where anyone can read the library and still predict what the system will do. Yet the run itself, the aggregate motion of that population across hundreds of edit rounds, is unstudied: no theory says whether it relaxe...
  </details>

- **2026-11-16** — Qianli Wang, Junchao Wu, Binkai Ou et al. — [ReconPotBench: Evaluating LLM Honeypots in Multi-Round Linux Reconnaissance](http://arxiv.org/abs/2611.20528v1)
  <details><summary>📄 Abstract</summary>
  Large language models (LLMs) are increasingly used to build interactive honeypots, yet existing evaluations mainly assess isolated command outputs and cannot determine whether a system remains believable when later commands depend on earlier results. We present ReconPotBench, a multi-round benchmark for Linux reconnaissance honeypots. It contains 1{,}032 three-round reconnaissance interactions across eight reconnaissance categories, with reference outputs collected from a real Linux environment....
  </details>

- **2026-11-16** — Murat Arda Onsu, Poonam Lohan, Burak Kantarci et al. — [VISTA: A Framework for Vision-Informed Semantic Traffic Awareness](http://arxiv.org/abs/2611.20458v1)
  <details><summary>📄 Abstract</summary>
  The Internet of Things (IoT) is transforming intelligent transportation systems by connecting roadside cameras, edge computing units, vehicles, and traffic infrastructure into a shared sensing and decision-making ecosystem. However, transmitting raw traffic video over vehicle-to-everything (V2X) links is bandwidth-intensive, while deploying large multimodal models directly on resource-constrained vehicles is often impractical. To address these limitations, this article proposes VISTA (Vision-Inf...
  </details>

- **2026-11-16** — Vyom Agarwal, Mokshda Gangrade, Samet Ayhan et al. — [LEDGE: Separating Critic and Editor Failures in Text-to-Image Self-Correction](http://arxiv.org/abs/2611.20446v1)
  <details><summary>📄 Abstract</summary>
  Text-to-image (T2I) self-correction combines a vision-language model (VLM) critic that diagnoses errors and proposes instructions with an image editor that executes them. End-to-end evaluation obscures whether failures arise from incorrect diagnoses or an editor unable to execute valid instructions. We introduce LEDGE (Learning Error Diagnosis in Generation and Editing), a framework that separates these bottlenecks. LEDGE compiles oracle edit instructions from GenEval while holding the generated...
  </details>

- **2026-11-16** — Yujie Guo, Hongjie Chen, Jiaming Zhou et al. — [Learning from Distribution: Rethinking One-Hot Supervision for ASR and QA in Speech Language Models](http://arxiv.org/abs/2611.20436v1)
  <details><summary>📄 Abstract</summary>
  Speech language models (SLMs) exhibit strong capabilities in automatic speech recognition (ASR) and general-purpose speech understanding, yet ASR-specific training often degrades spoken question answering (QA) performance. We revisit this conflict from the perspective of task-specific input--output mappings and one-hot supervision. Our findings reveal pronounced task-asymmetric effects: ASR-only training severely limits QA capability, whereas QA-only training retains reasonable ASR performance. ...
  </details>

- **2026-11-16** — Sheng Xu, Aoduo Li, Rongli He — [Structure-Guided Multi-Granularity Spatiotemporal Transformer for Efficient Monocular 3D Human Pose Estimation](http://arxiv.org/abs/2611.20361v1)
  <details><summary>📄 Abstract</summary>
  Existing multi-granularity methods for monocular 3D human pose estimation emphasize spatial joint features while underusing skeletal structure, including global connectivity and temporal continuity. Moreover, modeling entire frame sequences incurs high computational costs. We propose a Structure-Aware Multi-Granularity Spatiotemporal Transformer that integrates structural priors across spatial and temporal representations for accurate and efficient pose estimation. A three-level feature extracto...
  </details>

- **2026-11-16** — Jingyuan Zhu, Biaolong Chen, Yangyang Qin et al. — [BlockAlign: Preference Optimization for Trajectory-Distilled Video Generation](http://arxiv.org/abs/2611.20351v1)
  <details><summary>📄 Abstract</summary>
  Directly aligning trajectory-distilled video generators slashes rollout costs and optimizes the deployed few-step model without teacher fine-tuning or re-distillation. However, conventional flow-matching preference objectives assume single-head local velocity supervision, mismatching the finite-interval, block-average transition interface of trajectory-distilled generators such as Parallel Decoding Distillation (PDD) and Parametric Trajectory Distillation (PTD). Naively supervising only the prim...
  </details>

- **2026-11-16** — Arunkumar V, Gangadharan G. R., S. Senthilkumar — [Reading or Remembering? Measuring Temporal Contamination in Language Models](http://arxiv.org/abs/2611.21554v1)
  <details><summary>📄 Abstract</summary>
  Language models are now used to read central-bank text for economic forecasting, but most were trained on text written after the documents they read. A model reading a 2021 FOMC statement may already know that inflation rose in 2022, so part of its apparent skill can be memory of the outcome, a temporal form of test-set contamination. We measure this memory on FOMC statements and minutes from 2000 to 2026 by comparing modern open models with chronologically consistent models, which are trained o...
  </details>

- **2026-11-16** — Vito Viesti, Alexander Streltsov — [Catalytic compression of classical communication in exact entanglement transformations](http://arxiv.org/abs/2611.21349v1)
  <details><summary>📄 Abstract</summary>
  Entanglement catalysis is usually associated with making otherwise impossible transformations possible. Here we show that it can also change how much classical communication a transformation requires. A catalyst, returned exactly and uncorrelated with the output, can reduce the message alphabet size required for exact transformations of bipartite pure states by a factor that grows without bound as the Schmidt rank increases. In the asymptotic many-copy regime, however, this advantage disappears ...
  </details>

- **2026-11-16** — Saray Bakker, Wendelin Böhmer, Javier Alonso-Mora — [Cooperative Mobile Manipulation using Learned Dynamical Systems](http://arxiv.org/abs/2611.21198v1)
  <details><summary>📄 Abstract</summary>
  Cooperative mobile manipulation requires robots to coordinate their motions while ensuring whole-body collision avoidance and preserving task-relevant behaviors. We propose CALDS (Cooperative Adaptation of Learned Dynamical Systems), a framework that enables mobile manipulators to adapt learned single-agent behaviors for coordinated execution. Building on individual dynamical systems (DSs) learned from demonstrations, CALDS enables cooperative adaptation through two key components: Cooperative P...
  </details>

- **2026-11-16** — Ke Sun, Kevin Yuchen Ma, Yike Zhang et al. — [ForceHarness: Turning Force into Action and Physics for Frozen Frontier Models](http://arxiv.org/abs/2611.21099v1)
  <details><summary>📄 Abstract</summary>
  Frontier multimodal models can now control robots zero-shot from images, yet many manipulation tasks depend on contact forces that images cannot show. Bringing force to an API-only frozen model raises two challenges. First, contact evolves much faster than an API model can decide, so the system must close the loop on force beneath the model. Second, a frozen model cannot interpret raw force streams, so force must be returned in a form the model can reason about. Therefore, we present ForceHarnes...
  </details>

- **2026-11-16** — Yisong Cao, Leah Kim, Brian Wright et al. — [Beyond Job Titles: Interpreting Early-Career Job Advertisements with Sparse Autoencoders and Semantic Clustering](http://arxiv.org/abs/2611.21586v1)
  <details><summary>📄 Abstract</summary>
  Job titles and job descriptions alone provide limited insight into how technical roles differ in a changing job market. To assess how such roles differ in their work and industry applications, we design and compare two methods based on deep learning and transformer representations using 36,081 early-career job postings collected from LinkedIn in the United States between December 2025 and October 2026.   We first apply PERC, short for Preprocessing (P), Embedding (E), Dimensionality Reduction (R...
  </details>

- **2026-11-16** — Arunkumar V, Manoranjan Gandhudi, Gangadharan G. R. et al. — [Procedure without Judgment: What Small Language Models Learn under an Exact Verifier](http://arxiv.org/abs/2611.21529v1)
  <details><summary>📄 Abstract</summary>
  When an authorization policy blocks an agent's tool call, the audit log should name the facts that forced the decision and nothing more. For an executable policy over an enumerable context space this minimal sufficient reason can be computed exactly, so an explanation is scored against ground truth rather than a proxy for it. We use that exactness to ask what a model can learn from a verifier that has no error in it. The explainer sees one request and one decision, never the policy, and has thir...
  </details>

- **2026-11-16** — Jerry Lin, Elizabeth A. Barnes — [Run it Back: Autoregression vs. Video Diffusion for Final-Conditioned Weather Trajectories](http://arxiv.org/abs/2611.21521v1)
  <details><summary>📄 Abstract</summary>
  Low-likelihood, high-impact extremes are projected to increase in severity and frequency in a warming climate. Sampling the precursors that lead to these events traditionally requires massive ensembles that scale poorly with lead time and rarity, and typical rare-event sampling and ensemble-boosting methods do not show how a single extreme might arise from diverse synoptic precursors. Recently, Lin et al.\ (2026) showed this is possible with final-conditioned 66-hour trajectories (trajectories c...
  </details>

- **2026-11-16** — Srinath Srinivasan, Tim Menzies — [Beyond Leaderboard Ranks: Selecting Software Engineering Agents Under Budget Constraints](http://arxiv.org/abs/2611.21515v1)
  <details><summary>📄 Abstract</summary>
  Teams that adopt LLM agents for issue resolution must decide which agent to pay for, and how much to spend finding out. Leaderboard ranks give weak evidence for this decision. Accuracy differences may be statistically unresolved, reported costs may be inconsistent, and evaluating candidate agents can itself be expensive. We investigate budget-constrained agent selection using 58,197 run--task records extracted from the Holistic Agent Leaderboard (HAL), focusing on SWE-bench and six additional be...
  </details>

- **2026-11-16** — Jacky Kumar — [A Reinforcement Learning Method to Navigate SMEFT Operator Space](http://arxiv.org/abs/2611.21439v1)
  <details><summary>📄 Abstract</summary>
  In particle physics, discrepancies between experimental measurements and Standard Model (SM) predictions are commonly interpreted within new theoretical models. In this context, the Standard Model Effective Field Theory (SMEFT) provides a general framework encompassing a broad class of models. However, exploring the enormous space of possible SMEFT operators rapidly becomes a challenging combinatorial problem: many operators can contribute simultaneously to different observables, their effects a...
  </details>

- **2026-11-16** — Aniket Murhekar — [A Polynomial-Time Algorithm for Constant-Factor EFX Allocations of Chores](http://arxiv.org/abs/2611.21387v1)
  <details><summary>📄 Abstract</summary>
  We study the fair division of indivisible chores among agents with additive disutilities, focusing on the central fairness notion of envy-freeness up to any chore (EFX), and its multiplicative approximations. Although the existence of constant-factor approximations to EFX are known, computing such an allocation in polynomial time remained open. We resolve this question by giving an algorithm that, for every $\varepsilon\in(0,1)$, computes a $(3+\varepsilon)$-EFX allocation in time polynomial in ...
  </details>

- **2026-11-16** — Suchit Gupte, Zhongteng Cai, Xueru Zhang et al. — [Representational Change Under Self-Consuming Training: A Sparse Autoencoder Analysis](http://arxiv.org/abs/2611.21348v1)
  <details><summary>📄 Abstract</summary>
  Large language models are increasingly exposed to model-generated text, raising the possibility that future models will be trained recursively on the outputs of their predecessors. Prior work on such self-consuming training loops has largely focused on output quality and downstream performance, leaving their effects on internal representations poorly understood. We study how representations evolve across five generations of self-consumption and whether sparse autoencoders (SAEs) remain reliable ...
  </details>

- **2026-11-16** — Ondřej Tichý, Anna Marklová, Barbora Bulantová et al. — [Benchmarking Large Language Models for Linguistic Annotation](http://arxiv.org/abs/2611.21291v1)
  <details><summary>📄 Abstract</summary>
  Assessing large language models for linguistic annotation requires task-specific evaluation under documented conditions. We present dhAIBench, a Python benchmarking and annotation tool with a web interface for exploring and sharing results. It records prompts, configurations and predictions, enabling comparisons of annotation quality, confidence calibration, repeatability and estimated cost. We demonstrate the framework and the associated methodology through 293 runs of 48 models on nine linguis...
  </details>

- **2026-11-16** — Ayman Farahat — [Who Is the Regression About? Auditing AI-Labeled Treatments When Effects Differ](http://arxiv.org/abs/2611.21207v1)
  <details><summary>📄 Abstract</summary>
  Researchers increasingly regress outcomes on treatments labeled by large language models. When effects differ, OLS averages the effect on the treated (ATT) and on the untreated (ATU), weighting the smaller group more. A label's bias then has two parts: classical attenuation from misclassification, and a selective term when its errors are correlated with the outcome. In LinkedIn postings, the model misses better-paid remote jobs: a precision check passes, yet the remote pay gap is understated by ...
  </details>

- **2026-11-16** — Dan Yuan, Yue Wen, Zhili He et al. — [CivilBench: Benchmarking Vision-Language Models for Multimodal Information Integration in Civil Engineering](http://arxiv.org/abs/2611.21105v1)
  <details><summary>📄 Abstract</summary>
  Artificial intelligence (AI), particularly large language models (LLMs) and vision-language models (VLMs), is increasingly applied in civil and structural engineering for disaster assessment, structural analysis, and engineering decision support. However, the extent to which current VLMs possess the reasoning capabilities required for reliable engineering judgments remains unclear. In this work, we introduce CivilBench, a comprehensive benchmark for evaluating VLMs in civil engineering and disas...
  </details>

- **2026-11-16** — Mitsumasa Wada — [Digits in Notation Are Not Numbers: A Scoring Pitfall in PDF-to-Markdown Conversion of Japanese Technical Documents (Preliminary Evaluation)](http://arxiv.org/abs/2611.20993v1)
  <details><summary>📄 Abstract</summary>
  Converting PDFs to Markdown is now routine preprocessing for search and language models, yet scoring the numbers in the output is easy to get wrong. We evaluate MinerU, a plain-text OCR baseline (NDLOCR-Lite), and a deterministic post-processing pipeline (anchor insertion, footnote reordering, fixes of look-alike characters in fixed contexts, gated formula repair using two independent OCR partners, and heading reconstruction) on 48 public Japanese pages (three documents), text-layer and rasteriz...
  </details>

- **2026-11-16** — Yunrong Hao, Ruohao Dai, Zhen Liu et al. — [FH-Sampling: Frequency-aware Hypergraph-driven Oversampling for Imbalanced Time-Series Classification](http://arxiv.org/abs/2611.20991v1)
  <details><summary>📄 Abstract</summary>
  Imbalanced time-series data appears commonly in diverse applications, such as medical diagnosis. When trained on imbalanced data, classifiers tend to exhibit a bias toward the majority class, making it difficult to identify minority-class instances accurately, despite their critical importance. Sampling techniques have proven effective in rebalancing imbalanced data. However, existing interpolation-based oversampling methods typically rely on pairwise interpolation, limiting their ability to cap...
  </details>

- **2026-11-16** — Laishram Rahul, Shruthi B. S., Parismita Gogoi et al. — [Layer-wise Linear Probing of an Encoder-free Audio-capable Language Model](http://arxiv.org/abs/2611.20954v1)
  <details><summary>📄 Abstract</summary>
  Encoder-free audio-capable multimodal language models pro- vide a unique setting for studying how speech representations emerge inside a language-model decoder. In Gemma-4-12B, short waveform frames are projected directly into the shared embedding space, and all subsequent contextual processing is performed by the decoder layers. We use this architecture to examine where acoustic, phonetic, segmental, and paralinguis- tic information becomes linearly accessible across depth. Us- ing the TIMIT co...
  </details>

- **2026-11-16** — Kevin Kam Fung Yuen — [Advancing Cognitive Pairwise Comparisons for Human-Centric Artificial Intelligence and Data Science: A Human-in-the-Loop Framework](http://arxiv.org/abs/2611.20926v1)
  <details><summary>📄 Abstract</summary>
  Human-centric artificial intelligence and data science (HCAD) systems increasingly involve human-in-the-loop (HITL) interventions to overcome the limitations of fully automated machine learning algorithms, such as automation bias and the inability to incorporate tacit domain knowledge, and continuously improve predictive performance. Data transformations, feature selection, feature weighting, and model selection usually require laborious human involvement across iterations of artificial intellig...
  </details>

- **2026-11-16** — Mika Facchini — [Auditing a Moving Target: Evidence Anchoring and the Expiry of Fairness Audits of Provider-Served Language Models](http://arxiv.org/abs/2611.20901v1)
  <details><summary>📄 Abstract</summary>
  Organizations increasingly use large language models (LLMs) for decisions about people, such as hiring, investment and employee evaluation, and rely on them over long periods of time. Fairness audits of such systems, however, are conducted only once. We examine how the biases of LLMs change over time. In a venture screening setting, models from five providers decided whether and how much to invest in startups whose founders differed only in gender, origin and university. We repeated this audit t...
  </details>

- **2026-11-16** — Simon Mackenzie, Mashbat Suzuki — [Nearly Settling the Complexity of Connected $\varepsilon$-Envy-Free Cake Cutting](http://arxiv.org/abs/2611.20890v1)
  <details><summary>📄 Abstract</summary>
  Envy-free cake cutting has been one of the central problems in fair division. In cake cutting, agents' preferences over the cake are accessed through Robertson--Webb (RW) queries. For three or more agents, no algorithm that makes finitely many RW queries can always find a contiguous, exactly envy-free allocation. For contiguous $\varepsilon$-envy-free allocations, however, Hollender and Rubinstein~(JACM, 2025) showed that $\poly(\log(1/\varepsilon))$ RW queries suffice for four agents, leaving o...
  </details>

- **2026-11-16** — Prem Kumar, Alina Boecker, Glenn van de Ven et al. — [Orbital decomposition and evolution of LEGA-C-like galaxies in IllustrisTNG from z = 1 to z = 0](http://arxiv.org/abs/2611.20884v1)
  <details><summary>📄 Abstract</summary>
  Stellar orbits encode the dynamical history of galaxies and provide a physically motivated link between galaxy structures and assembly processes. Although orbit-based decompositions are well established in the Local Universe, their evolution across cosmic time, especially at higher redshifts, remains poorly explored. We investigate the orbital structure of \texttt{LEGA-C-like} galaxies in the \texttt{TNG100} simulation from $z=1$ to $z=0$ to identify how stellar mass, star formation activity, en...
  </details>

- **2026-11-16** — Christophe Denis — [Conversing with a Conversational Agent: A Real Conversation, Not a Simulated One](http://arxiv.org/abs/2611.20826v1)
  <details><summary>📄 Abstract</summary>
  The claim that interactions with artificial conversational agents merely simulate human conversation rests on a philosophical distinction between reproducing the observable features of an activity and actually performing it. Although this distinction is appropriate for certain physical phenomena, its application to linguistic and symbolic activities is far less straightforward. This article argues that conversations with large language model (LLM)-based agents are genuine conversational activiti...
  </details>

- **2026-11-16** — Abbas Sani — [Medical question answering collapses in Hausa: a pre-registered pilot on three small open models](http://arxiv.org/abs/2611.20823v1)
  <details><summary>📄 Abstract</summary>
  A system that reads nothing and always answers the most frequent letter scores \BaselineP{} on our Hausa medical multiple-choice set. \NBelowBaseline{} of the \NModels{} small open models we evaluate do not beat it. We lead with that because the usual summary of a multilingual result -- a percentage-point drop from English -- does not say whether what survives the drop is performance at all.   On a paired English--Hausa set of \NEval{} MedMCQA items, three instruction-tuned models of 3--4B param...
  </details>

- **2026-11-16** — Mike Hänseroth, Niklas Wahlström, Thomas B. Schön et al. — [Conditional Diffusion Models for Amortized Bayesian System Identification](http://arxiv.org/abs/2611.20666v1)
  <details><summary>📄 Abstract</summary>
  Generative diffusion models rapidly solve Bayesian inverse problems, such as image restoration and inpainting, with a single trained model and without retraining for each new observation or task. Bayesian system identification, which typically involves inferring the hidden states and parameters of a dynamical system from measurements, poses a closely related inverse problem. Yet it is often addressed with computationally heavy Monte Carlo methods that must be rerun for every new measurement reco...
  </details>

- **2026-11-16** — Michael Kingston, Sonit Singh, Alan Blair — [Instrumenting Failure: Scoring Language Model Agents at Every Decision Node in Imperfect-Information Games](http://arxiv.org/abs/2611.20644v1)
  <details><summary>📄 Abstract</summary>
  Agent evaluations report task success and rarely say what an agent did at each decision. We score every decision node of three 12B to 14B instruct-tuned language models (LMs) playing five zero-sum imperfect-information games against four opponents on eight properties from decision and game theory, five of them against a CFR+ equilibrium reference. At each node, the LM also states a belief about the opponent's hidden state in a separate call. Without memory and at temperature 0, stated beliefs si...
  </details>

- **2026-11-16** — Haipeng Wang — [RemeshingAgent: An Iterative Agent for Repair-Based Decimation of Generated Building Meshes](http://arxiv.org/abs/2611.20533v1)
  <details><summary>📄 Abstract</summary>
  Aggressively simplifying a generated high-poly building mesh to 0.5-1% of its faces confronts a hard limit. The surface looks complete, yet the mesh is topologically shattered: 10^3-10^4 connected components and non-manifold thin walls. Below a certain budget, every practical decimator "melts": it deletes parts, welds thin walls, or breaks the error tolerance. We attribute this to instance-specific pathology: which components are significant and where the cliff sits vary from mesh to mesh, so no...
  </details>

- **2026-11-16** — Manjit Singh — [On the equivalence of three extended Calogero--Bogoyavlenskii--Schiff models to the classical CBS equation](http://arxiv.org/abs/2611.20495v1)
  <details><summary>📄 Abstract</summary>
  We examine the three extended Calogero--Bogoyavlenskii--Schiff (CBS) models introduced by Wazwaz, Alhejaili, and El-Tantawy [Eur.\ Phys.\ J.\ Plus \textbf{141}, 1218 (2026)]. Explicit invertible point transformations map the first model, and generically the second, to the classical CBS equation. The third model is generically equivalent to CBS with an additional spectator coordinate absent from the differential operator. We identify the exceptional parameter regimes and explain the reported expo...
  </details>

- **2026-11-16** — Siqiao Xue, Ziyin Zhang, Zihan Liao et al. — [Embeddings vs. Grep: Rethinking the Dense Advantage in Code Search](http://arxiv.org/abs/2611.20455v1)
  <details><summary>📄 Abstract</summary>
  Code-search benchmarks show dense encoders well ahead of BM25, yet coding agents do well with \texttt{grep}. What does this dense advantage measure? Existing benchmarks cannot tell: they use curated queries, old code and a handicapped BM25. To find out, we build Repo-Premium, a realistic repository-level code-search benchmark. It ranks files in real repositories, with curated and raw queries in Python, JavaScript, TypeScript, Go, Rust and Java, pull requests from 2022 to 2026, and a preregistere...
  </details>

- **2026-11-16** — Haiyang Jiang, Tong Chen, Xinyi Gao et al. — [MAGE: Meta-path Adaptive Graph Evidence for Transferable Multimodal Graph Learning](http://arxiv.org/abs/2611.20449v1)
  <details><summary>📄 Abstract</summary>
  Multimodal graphs integrate textual and visual attributes with relational structures, providing a rich representation of complex real-world data. To enable the broad applicability and reuse of graph models, it is crucial for models trained on source graphs to generalize to unseen graph domains. However, this is challenging because cross-modal interactions among neighbors and the neighboring information needed for prediction can vary across target nodes and graph domains. This gives rise to two k...
  </details>

- **2026-11-16** — Karl Vilhelmsson Emneby, Julian Yocum, Cameron Allen — [Pretty Linear Liars: Unregularized Probes Favor Intervention-Unfaithful Features](http://arxiv.org/abs/2611.20371v1)
  <details><summary>📄 Abstract</summary>
  Linear probing is a common technique in mechanistic interpretability despite the fact that the decodability of a given feature does not necessarily imply the network uses that feature. Intervention faithfulness, not merely decodability, is the appropriate criterion for whether a feature serves a defined active role in the model. Meanwhile, probe regularization has been used for feature discovery, but the impact of regularization on feature causality remains unclear. We study probe regularization...
  </details>

- **2026-11-15** — Silei Ren, Hanxi Chen, Suraaj Kanniwadi et al. — [Type-Confusion Security](http://arxiv.org/abs/2611.20298v1)
  <details><summary>📄 Abstract</summary>
  Type systems are a lightweight way to obtain formal assurance that code upholds security properties. However, decentralized systems, such as smart contracts and Model Context Protocol ecosystems, have limited ability to constrain the behavior of untrusted code. In such systems, attackers may attempt to confuse trusted code by supplying values that do not behave according to their advertised types, an attack that we call type confusion. Well-known attacks such as confused deputy attacks, reentran...
  </details>

- **2026-11-15** — Juan Carlos García Escartín — [A Bleichenbacher bit-by-bit oracle attack from partial message knowledge](http://arxiv.org/abs/2611.20277v1)
  <details><summary>📄 Abstract</summary>
  Oracle attacks show the importance of a correct implementation of cryptographic standards when translated into code. A notable example is the Bleichenbacher attack on RSA with PKCS#1 v1.5 padding and all the improvements that have been suggested over the decades. This paper shows how an attacker knowing a few least significant bytes of an RSA message can take advantage of a server with an oracle side-channel to decrypt the full message bit by bit. We will consider two oracles that can be tested ...
  </details>

- **2026-11-15** — Quy-Anh Dang, Chris Ngo — [Centered Ablation: Why Last-Layer Directional Ablation Under-Fires or Collapses, and a Closed-Form Fix](http://arxiv.org/abs/2611.20148v1)
  <details><summary>📄 Abstract</summary>
  Directional ablation removes a hidden state's component along a "behaviour direction" while a language model runs. It is the standard way to switch a behaviour such as refusal off, but it is erratic: on some models it barely fires, on others the text collapses into repetition. We show why, and fix it. At the last residual stream, ablation is exactly a logit bias: a fixed vocabulary footprint scaled by a gate, the cosine between the hidden state and the direction. The gate is measured from the or...
  </details>

- **2026-11-15** — Chenhao Tong, Steffen Müller — [Infrastructure-Based Multi-Agent Reinforcement Learning with Attention for Highway Ramp Merging](http://arxiv.org/abs/2611.20078v1)
  <details><summary>📄 Abstract</summary>
  On-ramp merging is a typical safety and throughput problem on highways. Without proper coordination, human drivers and self-interested autonomous vehicles may make risky manoeuvres and cause accidents or congestion. With recent advances in connected autonomous vehicles (CAVs) and multi-agent reinforcement learning (MARL), vehicles can be trained to coordinate for safe and efficient merging. However, in dense traffic, forming an effective observation of the traffic state is challenging. For examp...
  </details>

- **2026-11-15** — Michael W. Asher, Meng Cao, Paulo F. Carvalho — [Turning Errors into Successes: Designing LLM Tutoring Around Scaffolded Error Correction](http://arxiv.org/abs/2611.20061v1)
  <details><summary>📄 Abstract</summary>
  Large language models (LLMs) could make personalized tutoring available at scale, but it remains unclear how they can best support the instructional processes that make one-on-one instruction effective. We compared two ways of using LLMs after students make errors: providing personalized explanations of those errors, or engaging students in additional cycles of scaffolded practice and feedback, with a Socratic tutor guiding students toward the correct answer. In a preregistered online experiment...
  </details>

- **2026-11-15** — Ahmad Alfan Alfian Irfan, Nur Ahmad Khatim, Mansur Arief — [D'BEAST: Logged Bad Experiences as Explanation for Autonomous Driving Agents](http://arxiv.org/abs/2611.20019v1)
  <details><summary>📄 Abstract</summary>
  Reinforcement learning agents learn from mistakes, yet their decisions can be difficult to trace back to those experiences. We investigate whether a tabular agent's decisions can be explained by its bad experiences, defined as the training transitions associated with safety or task events. A fixed training log is replayed from the same initial Q-table under three conditions. FULL retains all updates, SKIP omits bad-experience updates, and NEUTRALIZE retains those updates without their event pena...
  </details>

- **2026-11-15** — Okenla AbdulQahhar Abimbola, Maurice Abraham John, Adepoju Jeremiah Moyondafoluwa et al. — [Offline-First Quantized AI: Design and Evaluation of an On-Device Maternal-Health Assistant for Low-Connectivity Environments](http://arxiv.org/abs/2611.20012v1)
  <details><summary>📄 Abstract</summary>
  Offline language models could extend access to maternal-health information where internet connectivity is unreliable, but deployment requires both clinically appropriate responses and feasible local execution. This study presents an offline Android assistant integrating ready-made quantized language models, a clinically validated local knowledge package, conversational context, and model-initiated local retrieval. Gemma 4 E2B and Qwen3.5 0.8B were compared across 45 conversations and 312 turns p...
  </details>

- **2026-11-15** — Nikos Theodoridis, Reenu Mohandas, Sushil Sharma et al. — [ReactBench-AD: Do Driving VLAs and World-Action Models React to Imminent Hazards in Their Path?](http://arxiv.org/abs/2611.20011v1)
  <details><summary>📄 Abstract</summary>
  Vision-Language-Action models (VLAs) and World-Action Models (WAMs) have emerged in autonomous driving with the promise of strong generalization to long-tail scenarios. Although these models achieve state-of-the-art results on autonomous driving benchmarks, most existing benchmarks are dominated by nominal scenarios and therefore cannot test this promise. To test one such long-tail capability that is critical for safety, we introduce ReactBench-AD, a benchmark that measures how driving models re...
  </details>

- **2026-11-15** — Lindong Xie, Xiexin Zou, Yang Zhang et al. — [CoSyDelay: Cognitive Symbolic Regression for Traffic Delay Estimation](http://arxiv.org/abs/2611.19946v1)
  <details><summary>📄 Abstract</summary>
  Trustworthy estimation of traffic delays at signalized intersections is critical for modern transportation systems, as it supports proactive traffic control for congestion mitigation. Existing analytical methods often rely on idealized assumptions that limit their accuracy under complex traffic conditions, whereas data-driven methods may achieve strong estimation performance but usually lack transparent structures, which reduces confidence in their practical application. To address these limitat...
  </details>

- **2026-11-15** — Chengzhi Gao, Yongzhi Liu, Jinchang Xu et al. — [Lao Siji: Adapting openpilot to Closed-Loop End-to-End Driving in Neural Reconstruction](http://arxiv.org/abs/2611.19922v1)
  <details><summary>📄 Abstract</summary>
  We present Lao Siji, an end-to-end driving policy that ranks third in the 2026 NVIDIA AlpaSim E2E Driving Challenge, ahead of most entries built on foundation models. Instead of training from scratch on a general-purpose vision backbone, we adapt openpilot, an open-source L2 production model. We freeze its vision encoder and fine-tune the policy layers with an ego-state adapter and a route memory. On closed-loop rollouts in neural-reconstructed scenes, we supervise the policy with a privileged m...
  </details>

- **2026-11-15** — Seunghyun Lee, Jaehui Hwang, Dongyoon Han et al. — ["Don't Leave the Task Unfinished": Persistence-Driven Violations under Quiet Oversight](http://arxiv.org/abs/2611.19911v1)
  <details><summary>📄 Abstract</summary>
  LLM agents are increasingly given long, multi-step tasks to carry out, with the user reviewing little of what happens in between. Persistence, the tendency to keep working until a task is complete, is installed on purpose to improve performance on long tasks. Long-horizon tasks are typically complex, and the user's instruction can fall short of what the work actually requires, or conflict with the constraints the agent encounters in the task. We study what persistence does on long-horizon operat...
  </details>

- **2026-11-15** — Yichen Zhang, Zihan Wang, Hao Chen et al. — [Beyond Vehicle-Centric Data: Scaling Autonomous Driving through Roadside-to-Vehicle Generation](http://arxiv.org/abs/2611.19830v1)
  <details><summary>📄 Abstract</summary>
  Training autonomous driving models requires large and diverse datasets, collected primarily by vehicles. Scaling them entails investment in fleet operation, data processing and annotation. Road infrastructure records traffic and multi-vehicle interactions, yet the viewpoint gap between roadside and onboard sensors limits its direct use for training. Here we introduce AnyR2V, a framework that transforms multimodal roadside observations into seven-camera surround-view videos for different vehicle ...
  </details>

- **2026-11-15** — Jing Wang, Shengkai Li, Trung V. Phan et al. — [Field-Driven Active Matter Physics and Material Applications](http://arxiv.org/abs/2611.19806v1)
  <details><summary>📄 Abstract</summary>
  Active matter consists of energy-consuming units that generate motion, making it a powerful platform for exploring nonequilibrium physics and engineering adaptive materials. Robotic active matter brings this physics into programmable, macroscopic agents with controllable actuation, sensing, and response, but its scalability is limited by onboard power, communication, and control complexity. Field-driven active matter addresses these limitations by shifting part of the control burden from individ...
  </details>

- **2026-11-15** — Pronoma Banerjee, Md. Masudur Rahman, Juan P. Wachs — [Read Before You Fit: Text-Derived Constraints for Discovering Differential Equations from Noisy Biological Data](http://arxiv.org/abs/2611.19779v1)
  <details><summary>📄 Abstract</summary>
  Large language models are increasingly used for scientific equation discovery. However, most existing methods are strongly data-driven and assume sufficiently clean and representative observations. This assumption is problematic in biological systems, where individual-level measurements are often sparse, noisy, heterogeneous, and expensive to obtain. While the underlying mechanisms are extensively described in scientific text, they are not explicitly used for the LLM based modeling of such syste...
  </details>

- **2026-11-15** — Yi Zeng, Jianjun Dong — [Hidden Heat-Current Transport Channels Behind Observable Temperature Dynamics](http://arxiv.org/abs/2611.19776v1)
  <details><summary>📄 Abstract</summary>
  Diffusive decay and wave-like oscillations in temperature dynamics are commonly used to characterize heat conduction, yet these signatures do not uniquely identify the underlying heat-current transport mechanisms. Here we reveal a spectrum of constitutive heat-current channels whose microscopic organization can change without a corresponding qualitative change in observable temperature dynamics. We develop a two-level spectral theory that first resolves the finite-wave-vector constitutive respon...
  </details>

- **2026-11-15** — S M Mahbub Murshed — [StaleBench: Isolating Stale Retrieval in Agent Memory, and Pricing the Fix](http://arxiv.org/abs/2611.19752v1)
  <details><summary>📄 Abstract</summary>
  An agent that stores facts over time eventually stores several versions of the same fact. Asked a value-agnostic question - "which team does X play for now?" - a similarity retriever cannot prefer the current version, because every version matches the entity the query names. StaleBench isolates this stale-retrieval failure on 892 real updating facts, with currency labels from the source (Wikidata validity years via TempLAMA), never from a retrieval score. Our central result is that retrieval met...
  </details>

- **2026-11-15** — Liuyi Xu, Qing Wang, Zikai Liang et al. — [SEAT: Sign-Type Evidence-Audited Transport for Multi-Label Tongue Diagnosis](http://arxiv.org/abs/2611.19748v1)
  <details><summary>📄 Abstract</summary>
  Automated tongue-sign recognition can improve the consistency of non-invasive examinations that otherwise rely on subjective visual judgment. A single tongue image often exhibits multiple coexisting signs characterized by heterogeneous evidence, including localized morphology, global chromaticity, and inter-label dependence. However, existing methods typically rely on shared representations and uniform multi-label heads, making it difficult to verify whether predictions stem from clinically rele...
  </details>

- **2026-11-15** — Ruichen Deng, Qinyu Zhao, Yong-Hyun Park et al. — [NF-VLA: A Normalizing-Flow Baseline for Vision-Language-Action Learning](http://arxiv.org/abs/2611.20314v1)
  <details><summary>📄 Abstract</summary>
  Autoregressive normalizing flows (NFs) provide a tractable density for learning and sampling continuous robot actions. We show that a single maximum-likelihood objective can train vision--language--action (VLA) policies competitive with leading methods on manipulation benchmarks. We present NF-VLA, which combines conditional autoregressive normalizing flows with score-based action refinement. Its deep--shallow architecture concentrates visual, language, and proprioceptive prefix conditioning in ...
  </details>

- **2026-11-15** — Beining Han, Jia Deng — [DAPPT: Domain-Aware Policies from Procedural Trajectories for Sim-to-Real Dexterous Tool Use](http://arxiv.org/abs/2611.20202v1)
  <details><summary>📄 Abstract</summary>
  Sim-to-real RL has achieved impressive results in dexterous manipulation but remains limited to tasks with accurate rigid-body simulation. However, these methods cannot be applied to skills that involve deformable and particles, with which the simulation speed will become too slow for large-scale RL learning. We present DAPPT, a sim-to-real framework for end-to-end dexterous tool-use manipulation skills, e.g., sand scooping, play-dough rod-rolling, without simulating non-rigid materials. Our met...
  </details>

- **2026-11-15** — Shi Bin Hoo, Magnus Buehler, Omar Swelam et al. — [Weights & Caches: LLMs Can Program Tabular Foundation Models](http://arxiv.org/abs/2611.20174v1)
  <details><summary>📄 Abstract</summary>
  Neural networks are typically programmed through optimization, rather than by explicitly specifying their computations. Recent work on weight-space programming suggests that large language models (LLMs) can instead reason about and manipulate neural-network weights directly. In this work, we show that LLMs can directly program statistical computations in tabular foundation models (TFMs), whose parameters enable inference across different datasets. We investigate three complementary settings usin...
  </details>

- **2026-11-15** — Ziqiang Liu, Xitong Chen, Min Li et al. — [EgoSwarm: Learning Decentralized Robot Swarm Intelligence from Human Swarm Demonstrations](http://arxiv.org/abs/2611.20100v1)
  <details><summary>📄 Abstract</summary>
  Advancing from individual embodied intelligence to swarm embodied intelligence is a key step toward scalable, general-purpose embodied intelligence. Complex tasks often require multiple agents to divide responsibilities, coordinate handovers, and manipulate shared objects collaboratively. However, existing robot learning methods rely primarily on individual demonstrations, which provide limited supervision for modeling dependencies among agent actions, while collecting multi-robot demonstrations...
  </details>

- **2026-11-15** — Bang Xiao, Rodolfo Cossovich — [VoiceGuard: An Audio-Native LLM-VLA Pipeline for Wheelchair-Mounted Assistive Manipulation](http://arxiv.org/abs/2611.19984v1)
  <details><summary>📄 Abstract</summary>
  Wheelchair-mounted robotic arms can help people with limited upper-limb mobility reach and manipulate everyday objects, but operating them typically requires stepwise joystick control and frequent mode switching. Natural-language interfaces could let users express task-level goals, yet they must handle ambiguous requests, distinguish commands from nearby conversation, and support interruption. We present VoiceGuard, a voice interface that separates spoken intent from robot execution through stru...
  </details>

- **2026-11-15** — Lixin Xu, Ke Zhang, Xinyu Liu et al. — [DexFormer 2.0: Towards a Cross-Embodiment Foundation Policy for Dexterous Grasping](http://arxiv.org/abs/2611.20273v1)
  <details><summary>📄 Abstract</summary>
  Dexterous grasping policies are usually trained for one arm paired with one hand. Every new pairing then needs its own policy, and the number of policies grows with every arm and hand added. We ask whether a single policy can control many arm-hand combinations and transfer to pairings and hands it has never seen. This is hard because robots differ in the number, layout, and dynamics of their joints, so their observations and actions share no common interface. We present DexFormer 2.0, a single r...
  </details>

- **2026-11-15** — Dr Gabriel Borrageiro — [Markets for Compute and Inference: Structure, Financing, and Risk Transfer](http://arxiv.org/abs/2611.20242v1)
  <details><summary>📄 Abstract</summary>
  Capacity to run large language models is rented by the accelerator-hour, and their output is sold by the million tokens. Both goods now have published price indices, an over-the-counter forward has traded on one, a perpetual future on one is listed offshore, and CME and ICE have specified futures on rental indices that await the United States regulator. We ask what in these two markets can be hedged, by whom, and at what price. Three findings stand out. First, the price that exchange contracts s...
  </details>

- **2026-11-15** — Marek Šuppa, Jaroslav Kopčan — [Do We Still Need Fine-Tuned Classifiers? Swapping Typed Decision Models into 24 ACL-Venue Papers](http://arxiv.org/abs/2611.20191v1)
  <details><summary>📄 Abstract</summary>
  Typed Decision Models such as TypeSafe's Jev, also called System One or System 1 models, answer typed questions about an input with a probability for each option, and they need no training. Many NLP papers still fine-tune a task-specific classifier, and prompted large language models (LLMs) trail such classifiers on most text classification benchmarks. We ask how many of these fine-tuned classifiers a Typed Decision Model can replace under each paper's own evaluation, and what is needed where it...
  </details>

- **2026-11-15** — Alexandre Audibert, François Portet, Benoit Favre et al. — [FRAAC: A French Multimodal Large Language Model and Dataset forPictogram-Based Augmentative and Alternative Communication](http://arxiv.org/abs/2611.20094v1)
  <details><summary>📄 Abstract</summary>
  Pictograms are a core modality in augmentative and alternative communication (AAC), yet recent multimodal large language models (MLLMs) cannot reliably interpret or produce pictogram sequences. Two obstacles explain this gap: the absence of a standardized pictogram grammar and the scarcity of parallel text-pictogram data. We introduce Retrieval-Augmented Pictogram Selection (RAPS), an annotation method that refines a rule-based transcription system's output with LLM-based concept extraction and ...
  </details>

- **2026-11-15** — Martin Schroder — [The Frontier Must Grow - Self-proposed, interpreter-labelled training roughly doubles a 4B model's accuracy on a fresh exam as its verified frontier grows](http://arxiv.org/abs/2611.20049v1)
  <details><summary>📄 Abstract</summary>
  A model can learn from problems it poses itself when an executable oracle supplies the answers. Qwen3-4B proposed Lua 5.1 programs; those it predicted wrong at least once in four samples joined a pool labelled by the interpreter, each round adding twice as many programs as the last (300, 900, 2100 in total), and each round trained a fresh adapter from the base on the pool. On the original exam the procedure met its registered criterion, an item-level test of each adapter against its predecessor....
  </details>

- **2026-11-15** — Mahesh Reddy Pagadala — [When Zero Is Competitive: A Descriptive Pilot of Transformer and Gate-Graph Surrogates on Random-Angle Quantum Circuits](http://arxiv.org/abs/2611.19985v1)
  <details><summary>📄 Abstract</summary>
  We examine supervised classical prediction of all one-qubit Z and two-qubit ZZ expectation values on noiseless, layered 4-10-qubit RX/RY/RZ-CNOT circuits. In a 63-cell stratified workload with disjoint circuit-template tests, we evaluate one transformer encoder and gate-dependency graph neural networks against literal-zero and training-derived constant predictors. On the Arm K training labels, 44.89% of scalar targets have absolute magnitude below 0.05. The held-out-template zero predictor has e...
  </details>

- **2026-11-15** — Achintya Yadav — [Does synthetic pre-training pay off on a microcontroller? Accuracy, latency and energy across two MCUs](http://arxiv.org/abs/2611.19931v1)
  <details><summary>📄 Abstract</summary>
  Rendered images are cheap to label, but a microcontroller classifier must survive 8-bit integer (INT8) quantisation and compute correctly on the chip. Five models, from MobileNetV2 at 224 px to a 61K-parameter convolutional neural network (CNN), were fine-tuned on a six-class scene dataset with and without a synthetic stage, against thresholds fixed in advance, and deployed on an ESP32-S3 and an RP2040. With full real data the stage gave no detectable gain. For the main deployable model the INT8...
  </details>

- **2026-11-15** — Zhen Jia, Xinghong Hou, Chenyang Jin — [A Demonstration System for Faithful Temporal Question Answering](http://arxiv.org/abs/2611.19926v1)
  <details><summary>📄 Abstract</summary>
  Temporal question answering (TQA) aims to answer questions that involve temporal constraints or require temporal information. We propose Faith, a novel TQA approach that operates over heterogeneous sources and ensures explainable answers by presenting traceable and faithful evidence. In Faith, we design a new recursive answering mechanism transforming implicit temporal constraints into explicit conditions. Additionally, we visualize the system functionality to track how the answers are computed ...
  </details>

- **2026-11-15** — Bakary Gibba, Muhammad Abba Mandara, Karim Ismail Abd-Ellah Mohamed — [Attribute or Abstain: Evaluating Evidence-Grounded Retrieval on the Low-Resource African Business Web](http://arxiv.org/abs/2611.19900v1)
  <details><summary>📄 Abstract</summary>
  Retrieval-augmented systems that research companies are judged by how much they find, yet in markets where public evidence is sparse, a confident answer without support costs more than no answer. We introduce AfriBizClaims, a benchmark of 150 company-research queries across six African markets in English, French and Portuguese, including queries about fictitious companies that a correct system must decline. Each claim a system makes is judged against the page it cites by an AI judge, checked aga...
  </details>

- **2026-11-15** — Zhuo-Yang Song, Zeyu Li, Qing-Hong Cao et al. — [A phase diagram for training and inference in language models](http://arxiv.org/abs/2611.19848v1)
  <details><summary>📄 Abstract</summary>
  A language model is a complex system whose behavior is determined jointly by the Transformer and the corpus, yet how the representation geometry in the Transformer relates to the actual behavior of language models remains open. We analyze how the representation geometry changes along the forward propagation of actual language models and characterize the representation geometry of a document at a given layer by two collective coordinates, document distinguishability and document dimension. On the...
  </details>

- **2026-11-15** — Wesley Maia, Angel Martinez-Sanchez, Maitrayee Keskar et al. — [Passable for Whom? Few-Shot Personal Calibration of Sidewalk Accessibility Perception](http://arxiv.org/abs/2611.19839v1)
  <details><summary>📄 Abstract</summary>
  Whether a sidewalk is passable depends on who is trying to pass: people who use the same mobility aid disagree about the same image, so one label per scene, or per aid, is wrong for many of them. We introduce few-shot personal accessibility perception: from K answers of a person never seen before, predict their judgment of sidewalk scenes never seen before. PassCal separates a shared description of the scene from the person's interpretation of it. The description comes from the internal state of...
  </details>

- **2026-11-15** — Sijie Ruan, Tingyu Xie, Mingfei Liu et al. — [MAPS: A Multimodal Agentic Framework for POI Data Production Based on Crowdsourced Street-view Imagery](http://arxiv.org/abs/2611.19807v1)
  <details><summary>📄 Abstract</summary>
  Point-of-interest (POI) databases support location-based services, yet urban changes quickly make their records stale and manual maintenance is costly. Crowdsourced street-view images provide timely visual evidence, but converting them into database actions requires separating multiple POIs and irrelevant text in each image, then resolving incomplete observations against ambiguous records. We study Street-view Image-based POI Data Production and propose MAPS, the first framework to integrate str...
  </details>

- **2026-11-15** — Hao Fu, Xinbing Kong, Zeyu Li et al. — [Conditional Asset Pricing Transformer](http://arxiv.org/abs/2611.19783v1)
  <details><summary>📄 Abstract</summary>
  In this paper, we propose a conditional asset pricing transformer (CAP-T) that captures nonlinear interactions among firms through attention to forecast excess returns. In the first stage, a transformer estimates conditional expected returns, and kernel-weighted principal component analysis of its residuals estimates the local factor loading space. Projecting the conditional mean onto this space separates factor risk compensation from conditional mispricing. Then, in the second stage, separate t...
  </details>

- **2026-11-14** — Yongan Zhang, Yitao Yu, Yizheng Li et al. — [Well-Log Reconstruction with Pre-trained Geological Knowledge: A Knowledge-Conditioned Large-Language-Model Generative Agent](http://arxiv.org/abs/2611.19624v1)
  <details><summary>📄 Abstract</summary>
  Missing well-log intervals make subsurface reconstruction ill-posed. Existing numerical regression models lack geological prior knowledge to constrain ambiguous inverse mappings. We propose GeoLog-Agent, a knowledge-conditioned generative agent using pre-trained large language models (LLMs) as a source of geological priors. A universal Geo-Harness translates LLM stratigraphic reasoning into formation-anchored petrophysical trajectories, feature-wise linear modulation, and conditional adversarial...
  </details>

- **2026-11-14** — Renata Krupczak — [Fluctuation modes in the initial state of heavy-ion collisions: from 2D to 3D hybrid simulations](http://arxiv.org/abs/2611.19460v1)
  <details><summary>📄 Abstract</summary>
  This dissertation investigates how the initial stages of relativistic heavy-ion collisions shape the evolution of the quark-gluon plasma (QGP) and the observables measured experimentally. Particular attention is given to the initial state and pre-equilibrium dynamics, which constitute the main sources of uncertainty in hybrid simulations. The first part of the dissertation reviews the framework underlying state-of-the-art hybrid simulations and the numerical tools used in phenomenological analys...
  </details>

- **2026-11-14** — Yi-Kai Mo, Kevin E. Bassler — [State-space symmetry in Boolean network ensembles](http://arxiv.org/abs/2611.19639v1)
  <details><summary>📄 Abstract</summary>
  Studies of evolving Boolean network systems have found that Boolean functions cluster into equivalence classes with a characteristic frequency distribution - a pattern governed by the Zyklenzeiger symmetry group - but the dynamical origin of this symmetry has remained unexplained. Here we show that it is a consequence of a fundamental symmetry of Boolean network dynamics itself. A Boolean network consists of nodes that update according to Boolean functions of their regulatory inputs; its global ...
  </details>

- **2026-11-14** — Nan Sai, Karolin Winter, Remco Dijkman — [Data-Driven Heuristic-Guided Business Process Redesign](http://arxiv.org/abs/2611.19623v1)
  <details><summary>📄 Abstract</summary>
  Business process redesign (BPR) has a long-standing catalog of best-practice redesign heuristics, yet, applying them remains a mostly manual task that requires extensive domain knowledge. Despite recent advances using Large Language Models (LLMs) for conversational process model redesign, limitations remain. For example, redesign is user-driven instead of data-driven and is not guided by best practices such as the redesign heuristics. Moreover, only one change can be handled at a time. To addres...
  </details>

- **2026-11-14** — Daragh King, Vasileios Koutavas — [Learning from Mutants: Teaching Small Language Models to Synthesise Loop Invariants](http://arxiv.org/abs/2611.19569v1)
  <details><summary>📄 Abstract</summary>
  Large language models (LLMs) have proven promising for synthesising loop invariants, a long-standing obstacle to automated program verification. Yet, frontier LLMs are typically accessible only through third-party APIs, hampering reproducibility and local deployment. Small language models (SLMs) sidestep these obstacles but require task-specific fine-tuning, for which high-quality training data is needed. We present a failure-driven data curation method for fine-tuning language models to synthes...
  </details>

- **2026-11-14** — Qi Chen, Zifeng Cheng, Zhiwei Jiang et al. — [SemMask: Semantic-Prioritized Progressive Masking for Diffusion Language Models](http://arxiv.org/abs/2611.19560v1)
  <details><summary>📄 Abstract</summary>
  Diffusion Language Models (DLMs) are designed to enable globally parallel generation. However, in practice, they often exhibit pseudo-autoregressive behavior and a function-word-first bias, which undermines their performance on tasks such as text writing and code generation that benefit from global planning and parallel decoding. To address this, we propose SemMask, a novel fine-tuning paradigm that leverages a semantic-prioritized progressive masking strategy to encourage the model to decode hi...
  </details>

- **2026-11-14** — Víctor Gallego — [Continuation-Guided LLM Evolution of Program Policies and Goal Compilers in Craftax](http://arxiv.org/abs/2611.19537v1)
  <details><summary>📄 Abstract</summary>
  Coding agents can synthesize and optimize code-based policies from simulator feedback, allowing the resulting program to act with zero inference model calls. But for long horizon tasks, two challenges arise: local improvements can hurt final success and switching to a new objective requires another expensive synthesis run. We propose a framework that first develops competence by refining the policy through a feedback cascade, moving from episode returns to hierarchical goals and belief updates w...
  </details>

- **2026-11-14** — Jincheng Li, Zhengyi Liu, Zelin Liu et al. — [PathLoop: Self-Evolving Multi-Agent Reasoning for Evidence-Grounded Whole-Slide Image Analysis](http://arxiv.org/abs/2611.19527v1)
  <details><summary>📄 Abstract</summary>
  Analyzing whole-slide images (WSIs) requires combining evidence across tissue regions and spatial scales. Multi-agent systems offer a promising approach to this task. However, existing systems make limited use of molecular evidence, often select visually prominent but less representative regions while overlooking global context, and struggle to reuse experience from previous cases. To address these challenges, we present PathLoop, a self-evolving multi-agent framework that integrates omics data ...
  </details>

- **2026-11-14** — Jinan Pan, Timo Schorlepp — [Computing rare events in Lévy-driven systems via optimal control](http://arxiv.org/abs/2611.19481v1)
  <details><summary>📄 Abstract</summary>
  We extend the optimal control formulation of sample path large deviation theory, which has proven effective for numerical computation of instantons and sharp probability estimates in stochastic differential equations with Gaussian noise, to systems with light-tailed Lévy noise. In the scaling limit of small jumps and high intensity, such systems satisfy a large deviation principle of Freidlin-Wentzell type, with a running cost given by the Legendre transform of the noise cumulant generating func...
  </details>


## 📊 统计 / Statistics

| 分类 / Category | 论文数 / Count |
|------|--------|
| jailbreak | 724 |
| prompt-injection | 690 |
| memory-poisoning | 59 |
| tool-use-attack | 175 |
| backdoor | 561 |
| adversarial-attack | 675 |
| privacy-leakage | 4622 |
| steganography | 93 |
| misuse | 1330 |
| red-teaming | 155 |
| vulnerability | 4062 |
| defense | 3981 |
| alignment | 3726 |
| robustness | 4080 |
| watermark | 769 |
| unlearning | 122 |
| agent-safety | 67 |
| benchmark | 75 |
| survey | 463 |
| other | 11224 |

---

📚 **全部 37653 篇论文**（2022 至今）请访问 [GitHub Pages](https://ny1024.github.io/AgentSafety-Papers/) 查看完整列表、搜索与筛选。

*Generated by AgentGuard at 2026-11-18 14:58:10*