<div align="center">

# AgentGuard 🛡️

**Daily Tracking of LLM Agent Security Papers on arXiv**

[![Auto Update](https://github.com/NY1024/AgentSafety-Papers/actions/workflows/daily-update.yml/badge.svg)](https://github.com/NY1024/AgentSafety-Papers/actions/workflows/daily-update.yml)
[![Papers](https://img.shields.io/badge/Papers-29864-blue)](#)
[![License](https://img.shields.io/badge/License-MIT-green)](#)

</div>

---

## 📖 简介 / Introduction

自动追踪 arXiv 上大模型 Agent 安全方向的最新论文，每日更新，关键词智能分类。

*Automatically tracking the latest LLM Agent security papers on arXiv, updated daily with keyword-based classification.*

**最近更新 / Last Updated**: 2026-09-29 04:39 ｜ **论文总数 / Total Papers**: 29864（近 30 天 / Recent 30 days: 4235）

🌐 **[GitHub Pages](https://ny1024.github.io/AgentSafety-Papers/)** — 查看全部 29864 篇论文（含摘要、分类筛选、搜索）/ View all 29864 papers with abstracts, filters & search

## 📑 分类导航 / Category Navigation

- **[jailbreak](#-jailbreak)** — 越狱攻击 / Jailbreak Attacks — 643
- **[prompt-injection](#-prompt-injection)** — 提示注入攻击 / Prompt Injection Attacks — 571
- **[memory-poisoning](#-memory-poisoning)** — 记忆投毒与篡改 / Memory Poisoning & Tampering — 52
- **[tool-use-attack](#-tool-use-attack)** — 工具使用攻击 / Tool-Use Attacks — 142
- **[backdoor](#-backdoor)** — 后门与投毒攻击 / Backdoor & Poisoning Attacks — 478
- **[adversarial-attack](#-adversarial-attack)** — 对抗攻击 / Adversarial Attacks — 607
- **[privacy-leakage](#-privacy-leakage)** — 隐私泄露 / Privacy Leakage — 4208
- **[steganography](#-steganography)** — 隐写与隐蔽通信 / Steganography & Covert Communication — 72
- **[misuse](#-misuse)** — 滥用与误用 / Misuse & Abuse — 1078
- **[red-teaming](#-red-teaming)** — 红队测试 / Red Teaming — 129
- **[vulnerability](#-vulnerability)** — 漏洞与攻击面 / Vulnerabilities & Attack Surfaces — 3302
- **[defense](#-defense)** — 防御与防护方法 / Defense & Protection Methods — 3123
- **[alignment](#-alignment)** — 对齐与安全约束 / Alignment & Safety Constraints — 2896
- **[robustness](#-robustness)** — 鲁棒性与可靠性 / Robustness & Reliability — 3103
- **[watermark](#-watermark)** — 水印与溯源 / Watermarking & Provenance — 492
- **[unlearning](#-unlearning)** — 机器遗忘 / Machine Unlearning — 101
- **[agent-safety](#-agent-safety)** — Agent 安全框架 / Agent Safety Frameworks — 56
- **[benchmark](#-benchmark)** — 安全评测与基准 / Safety Benchmarks & Evaluation — 66
- **[survey](#-survey)** — 综述与系统化 / Surveys & Systematization — 364
- **[other](#-other)** — 其他安全相关 / Other Security-Related — 8381

## 📄 近期论文 / Recent Papers (Last 30 Days)

> 仅展示最近 30 天中最新的 500 篇论文（含日期、作者、摘要）。近 30 天共 4235 篇，完整 29864 篇论文列表请访问 [GitHub Pages](https://ny1024.github.io/AgentSafety-Papers/)

> Showing the latest 500 of 4235 papers from the last 30 days (with date, authors & abstract). For the full list of 29864 papers, visit [GitHub Pages](https://ny1024.github.io/AgentSafety-Papers/)

### 📂 jailbreak
*越狱攻击 / Jailbreak Attacks* — 4 papers

- **2026-09-28** — Shunchang Liu, Lukas Fluri, Xin Chen et al. — [Narrow Multimodal Fine-Tuning Can Induce Emergent Misalignment](http://arxiv.org/abs/2609.35291v1)
  <details><summary>📄 Abstract</summary>
  Modern AI models are aligned through post-training to adapt them to downstream tasks. Recent work shows that fine-tuning language models on narrow tasks can induce emergent misalignment (EM), causing broadly harmful behaviors beyond the training task. However, EM has been studied almost entirely in text-only tasks, leaving its manifestation in multimodal models unclear. In this paper, we define and analyze EM in the context of vision-language models. We first induce EM via fine-tuning on narrow ...
  </details>

- **2026-09-28** — Xi Wang, Songlei Jian, Yiming Zhang et al. — [Jailbreak Context Lingers: Divergent Safety Routing and Its Cross-Task Predictability in Tool Agents](http://arxiv.org/abs/2609.34686v1)
  <details><summary>📄 Abstract</summary>
  As large language models increasingly operate as tool-using agents, post-jailbreak safety feedback is often assumed to serve as a reliable safeguard; however, how lingering jailbreak context shapes subsequent agent behavior remains largely unexplored. To systematically examine this dynamic, we introduce a paired continuation framework across 192 parent tasks spanning 42 domains, evaluating 12,148 analyzed continuation pairs (curated from a 12,288-pair initially design) across eight diverse agent...
  </details>

- **2026-09-26** — Mohan Li, Chengyu Yu, Francesco Sovrano et al. — [LLM Alignment--Utility Asymmetry under Semantic-Preserving Transformations](http://arxiv.org/abs/2609.32717v1)
  <details><summary>📄 Abstract</summary>
  Large Language Model (LLM) alignment is intended to ensure that models remain helpful and safe, but its stability under input distributional shift is not yet fully understood. Prior work shows that aligned models can fail under jailbreak prompts, alternative encodings, and cross-lingual transfer, yet these failures are usually studied as attacks rather than controlled probes of alignment generalization. Moreover, existing evidence is largely grounded in natural language variation already represe...
  </details>

- **2026-09-26** — Gal Wertheizer, Rom Himelstein, Tomer Peretz et al. — [AnchorRep: Defending LLMs Against Cross-Model Adversarial Transfer via Representation Repulsion](http://arxiv.org/abs/2609.32602v1)
  <details><summary>📄 Abstract</summary>
  Adversarial attacks optimized on a single open-weight LLM can transfer to and jailbreak architecturally different models, allowing an attacker with white-box access to one model to compromise independently deployed systems. This creates a shared vulnerability across models, yet existing defenses are not designed for this cross-model threat. We find that cross-model transfer aligns with shared internal representation geometry, making it a natural defense target. AnchorRep targets this geometry di...
  </details>


### 📂 prompt-injection
*提示注入攻击 / Prompt Injection Attacks* — 11 papers

- **2026-09-28** — Bravish Ghosh — [Tracekit: Tamper-Evident Intent-Reasoning-Action Auditing for Autonomous Coding Agents](http://arxiv.org/abs/2609.35659v1)
  <details><summary>📄 Abstract</summary>
  Autonomous coding agents read untrusted files, run shell commands and spawn sub-agents with little supervision, yet their record is usually an editable log. We present Tracekit, an open-source, dependency-free system that captures three channels for every agent session: what the human asked (intent), what the model said of its reasoning (self-report), and what it actually executed (actions). These are written to a hash-chained, externally anchorable ledger and cross-checked. Tracekit hooks into ...
  </details>

- **2026-09-28** — Rohit Saxena, Utkarsh Upadhyay — [Nudgeability: Reasoning Models Follow Confidence Signals Without Tracking Their Own Competence](http://arxiv.org/abs/2609.34572v1)
  <details><summary>📄 Abstract</summary>
  Reasoning language models that can call tools must decide during inference whether to answer unaided or delegate. Any self-reflection mechanism for this must answer three questions: where the reflective signal comes from (verbal reports, output distributions, hidden states, a separate predictor), how it is presented to the model (numerical prediction, confidence token, prompt injection), and whether it changes the model's subsequent action. We isolate the third question. At a fixed point in othe...
  </details>

- **2026-09-28** — Xiao Yang, Yangchen Ou, Yuhan Gao et al. — [CoDeL: Co-Evolutionary Defense against Indirect Prompt Injection in LLM-based Agents](http://arxiv.org/abs/2609.34463v1)
  <details><summary>📄 Abstract</summary>
  Large language model (LLM)-based agents increasingly rely on external tools and content, exposing them to indirect prompt injection (IPI). This threat has motivated a wide range of defenses, among which training-based defenses are often regarded as most reliable. However, existing training-based defenses are typically optimized on a static distribution of explicit injections. They learn surface-form cues rather than the boundary between serving the user and obeying an injected objective, and the...
  </details>

- **2026-09-28** — Anmol Pandey, Aditya Jain, Liang Chen et al. — [Certified Multi-Source Integrity for Structured Agent Actions](http://arxiv.org/abs/2609.34245v1)
  <details><summary>📄 Abstract</summary>
  LLM agents increasingly take privileged, often irreversible structured actions, such as paying an invoice. They assemble each action from action-critical fields in documents and tool outputs that an adversary can corrupt, and indirect prompt injection can drive the model itself to extract attacker-chosen values. Current defenses gate on a source's trust label or certify free-text answer quality. None certifies the integrity of a coupled, policy-bound structured action under a corruption budget t...
  </details>

- **2026-09-27** — Zhihao Zhang, Chao Wang, Rujia Li et al. — [When Consent Outlives Context: Residual Authority Replay in Long-Lived Agents](http://arxiv.org/abs/2609.33910v1)
  <details><summary>📄 Abstract</summary>
  LLM agents increasingly rely on user approval to authorize security-sensitive actions at runtime. Such approvals are granted within a specific task and execution context. In long-lived agents, authorization decisions may need to persist across tasks or sessions. We find that this continuity can outlive the context that originally justified the approval, creating residual authority reusable without renewed consent. We expose this failure mode through a longitudinal attack that starts from a targe...
  </details>

- **2026-09-27** — Chenlong Yin, Xiaolong Jin, Wei Zou et al. — [Climbing the Hill: Prompt Injection Red-Teaming Against Frontier Models with Curriculum Reinforcement Learning](http://arxiv.org/abs/2609.33628v1)
  <details><summary>📄 Abstract</summary>
  Prompt injection is a leading security risk for LLMs and LLM-based applications such as agents. State-of-the-art red-teaming methods for prompt injection leverage reinforcement learning (RL) to train an attacker LLM to generate effective injected prompts. However, when targeting frontier LLMs such as GPT-6-Luna, a major challenge is the cold-start problem: every attack attempt by the attacker LLM fails and thus receives zero reward, providing no signal for learning. In this work, we propose a cu...
  </details>

- **2026-09-27** — Yixuan Liu — [Evaluating System One Models for Agent Security Decisions: Reliability, Calibration, and Selective Automation](http://arxiv.org/abs/2609.33401v1)
  <details><summary>📄 Abstract</summary>
  Model-based judges support agent security by detecting prompt injections, assessing interaction risks, and screening harmful requests. System One models expose typed decisions with probabilities that software can use to allow, block, or escalate inputs, but whether these probabilities support reliable automated security decisions remains unclear. We evaluate Jev, Laya, Decider, and Bespoke Nimble against specialized classifiers and language-model judges, examining decision accuracy, probability ...
  </details>

- **2026-09-27** — Patrick Kenney, Hadi Ahmadi, Denis Lusson et al. — [API Secrets Should Never Become Tokens in the LLM's Vocabulary: A Threat Analysis of API Credential Handling in LLM Agent Systems and an Empirical Evaluation of a Vault-Mediated Execution Boundary](http://arxiv.org/abs/2609.33371v1)
  <details><summary>📄 Abstract</summary>
  Tool-using large language model (LLM) agents turn credential hygiene from a storage problem into an execution-security problem. A key pasted into a prompt, or embedded in a system prompt or tool configuration, crosses from an authentication boundary into a data pipeline, where it may persist in conversation history, logs, memory stores, generated code, and error payloads. Prompt injection and excessive agency then convert passive disclosure into unauthorized action. This paper formalizes the cre...
  </details>

- **2026-09-27** — Zhongjian Zhang, Xiao Wang, Busheng Zhang et al. — [ZeroGAR: Benchmarking the Adversarial Robustness of Zero-Shot Graph Models](http://arxiv.org/abs/2609.33314v1)
  <details><summary>📄 Abstract</summary>
  Zero-shot graph models (ZGMs), which learn transferable knowledge from source graphs and directly apply to unseen target graphs without any adaptation, have achieved promising performance and attracted considerable attention. Despite their proliferation, existing ZGMs are predominantly evaluated on clean graphs, while existing graph robustness benchmarks mainly focus on supervised settings, leaving a fundamental question largely unexplored: How robust are ZGMs when their unseen target graphs are...
  </details>

- **2026-09-27** — Ben Hagag, William L. Anderson, Srija Chakraborty et al. — [ORBIT: A Framework for Multi-Agent Safety and Security Evaluations](http://arxiv.org/abs/2609.33102v1)
  <details><summary>📄 Abstract</summary>
  Multi-agent LLM systems are increasingly deployed for complex, long-horizon tasks or emerge as a natural consequence of agents interacting in the wild. Yet they give rise to significant safety and security risks: the flexible protocols that enable task generalization also expose novel threats, from cascading prompt injection to inter-agent collusion. Progress in defending against these threats has been slowed by a lack of shared empirical infrastructure, which forces bespoke environment developm...
  </details>

- **2026-09-26** — Animesh Shaw — [Silent Failures in Agentic Security Evaluation: A Validated Harness for Tool-Call Mediation Under Indirect Prompt Injection](http://arxiv.org/abs/2609.32691v1)
  <details><summary>📄 Abstract</summary>
  LLM agents that invoke privileged tools are vulnerable to indirect prompt injection (IPI), in which adversarial instructions embedded in retrieved data hijack the agent's actions. A growing body of work evaluates defenses against IPI, but the validity of that evaluation is rarely examined. We audit an IPI benchmark and its harness and identify four defect classes -- silent payload non-delivery, attack success scored by tool identity rather than arguments, false-rejection rate conflated with mode...
  </details>


### 📂 memory-poisoning
*记忆投毒与篡改 / Memory Poisoning & Tampering* — 1 papers

- **2026-09-28** — Mingxi Zou, Langzhang Liang, Zhuo Wang et al. — [From Attack Success to Attack Severity: Counterfactual Memory Attacks on LLM Agents](http://arxiv.org/abs/2609.34132v1)
  <details><summary>📄 Abstract</summary>
  As LLM agents increasingly rely on persistent memory for long-horizon and personalized behavior, they can retain and reuse information across interactions, but this also creates a lasting channel through which malicious memory writes can influence future behavior. Persistent-memory attacks are typically evaluated by whether they succeed, yet successful attacks can leave persistent states with substantially different downstream consequences. We study this severity as a distinct attack-design obje...
  </details>


### 📂 tool-use-attack
*工具使用攻击 / Tool-Use Attacks* — 2 papers

- **2026-09-26** — Kaiwei Liu, Jiqian Dong, Liran Dong et al. — [SkillVine: Agent Skill Evolution via Branching Exploration](http://arxiv.org/abs/2609.32731v1)
  <details><summary>📄 Abstract</summary>
  Agent skills encapsulate reusable procedural knowledge that enables LLM agents to perform tasks, and they can be improved automatically using trajectories from interactions with the environment. This is the classic problem of skill evolution. Existing approaches predominately follow a linear evolution paradigm, in which updates are sequentially applied to the latest skill-library version. As a result, they inevitably fall into local optima, leaving many promising evolution paths unexplored. We p...
  </details>

- **2026-09-26** — Pengyu Zhu, Jingyi Yang, Yi Liu et al. — [SkillDRE: Dual-Stage Red-Team Evolution of Agent Skills via Pre-Execution and Runtime Feedback](http://arxiv.org/abs/2609.32400v1)
  <details><summary>📄 Abstract</summary>
  Agent skills package instructions, executable code, and task-specific resources into reusable artifacts that agents can improve using execution feedback. The same mechanism also enables attackers to evolve malicious skills, making them more effective and less detectable. However, a candidate skill may pass pre-execution scanning yet fail to realize its target under runtime defenses, while a revision that repairs execution may introduce new scanner findings. We introduce SkillDRE, a fully automat...
  </details>


### 📂 backdoor
*后门与投毒攻击 / Backdoor & Poisoning Attacks* — 5 papers

- **2026-09-28** — Kajetan Dymkiewicz, Tim Farrelly, Adam Práda et al. — [Don't Inoculate Everything: Stratified Inoculation Prompting Narrows Backdoor Triggers and Preserves Desired Traits](http://arxiv.org/abs/2609.35356v1)
  <details><summary>📄 Abstract</summary>
  Supervised fine-tuning can teach language models undesired behaviours alongside desired ones. Inoculation prompting (IP) aims to limit unwanted generalisation by requesting the undesired behaviour during training and removing the request at inference. However, undesired behaviour can still appear under unrelated prompts. IP can also hinder learning of the desired behaviour. We address these limitations in settings where both behaviours co-occur in most training examples, so filtering out example...
  </details>

- **2026-09-28** — Kaisheng Fan, Yishu Gao, Xunzhu Tang et al. — [LENS: The Sum Is Worse Than the Parts for Set-Level Poisoning in Retrieval-Augmented Generation](http://arxiv.org/abs/2609.35155v1)
  <details><summary>📄 Abstract</summary>
  Retrieval-augmented generation (RAG) aggregates evidence from multiple external documents, yet this joint integration creates an underexamined vulnerability: attack effects absent in individual documents can emerge through set-level composition. Existing coordinated attacks do not explicitly enforce that every proper subset remains insufficient in frozen single-round RAG. We formalize set-level compositional poisoning, where documents designed to remain individually plausible jointly redirect RA...
  </details>

- **2026-09-28** — Zhongqi Wang, Jie Zhang, Nie Sen et al. — [Backdoor as Probe: Test-Time Adversarial Defense for CLIP](http://arxiv.org/abs/2609.34641v1)
  <details><summary>📄 Abstract</summary>
  Test-time adversarial defense improves the robustness of vision-language foundation models such as CLIP without retraining. However, adversarial activation shifts are typically treated as distortions to suppress, rather than signals to exploit. We turn these shifts into defense signals by repurposing the trigger-to-target mechanism of backdoors. The key is to implant a defender-controlled backdoor as a probe that is weakly activated by clean inputs but strongly activated by adversarial shifts. B...
  </details>

- **2026-09-27** — Sae Furukawa, Alina Oprea — [The Privacy Fallacy of Crowdsourced Fine-Tuning: Extracting Proprietary Data via Topic-Based Poisoning](http://arxiv.org/abs/2609.33985v1)
  <details><summary>📄 Abstract</summary>
  Supervised fine-tuning (SFT) is widely used to adapt large language models to downstream tasks. Crowdsourcing user conversations is an established approach to collecting SFT data at scale while reducing the need for costly manual annotation. However, it also allows untrusted users to contribute data to the fine-tuning pipeline. We investigate an underexplored privacy risk arising from this setting: can a malicious user poison a small fraction of the crowdsourced data to amplify extraction of pre...
  </details>

- **2026-09-26** — Indranil Halder, Rastri Dey, Cengiz Pehlevan — [A Solvable Theory of Pre-training Data Poisoning: Regime-Dependent Scaling Exponents](http://arxiv.org/abs/2609.32288v1)
  <details><summary>📄 Abstract</summary>
  Pre-training data poisoning of large language models is usually studied using targeted backdoors and their survival through safety post-training, which leaves open a more basic question: how does a model's clean data performance degrade as the poison rate $\varepsilon$ grows? Motivated by our controlled pre-training runs of OLMo-style models, in which the relative clean data validation perplexity increase $Δ$ between poisoned and clean models matched in architecture, token budget, and optimizati...
  </details>


### 📂 adversarial-attack
*对抗攻击 / Adversarial Attacks* — 3 papers

- **2026-09-28** —  Mansi, Nikhil Raghavan, Zixia Huang et al. — [eval-unlearn: Benchmarking unlearning in Text-to-Image Diffusion Models](http://arxiv.org/abs/2609.35269v1)
  <details><summary>📄 Abstract</summary>
  The rising number of concept unlearning techniques for text-to-image (T2I) diffusion models has produced a fragmented evaluation landscape. Methods are assessed under heterogeneous experimental conditions making principled cross-method comparison difficult. We present eval-unlearn, an open-source Python library providing a unified, reproducible benchmarking framework for concept unlearning in T2I Diffusion models. eval-unlearn integrates twelve published unlearning techniques spanning fine-tunin...
  </details>

- **2026-09-28** — Mashal Zainab, Salijona Dyrmishi, Hamid Bostani et al. — [Breaking Windows Malware Detection: A Comprehensive Evaluation of Problem-Space Adversarial Robustness](http://arxiv.org/abs/2609.34456v1)
  <details><summary>📄 Abstract</summary>
  Problem-space evasion attacks have exposed critical weaknesses in machine learning-based malware detectors; yet, their evaluation remains fragmented across models, datasets, and attack methodologies, often neglecting domain-specific requirements such as executability and functionality preservation. We address this gap with a unified, large-scale evaluation of nine state-of-the-art evasion attacks against eight Windows malware detectors, including seven open-source models and one commercial detec...
  </details>

- **2026-09-27** — Sen Nie, Jie Zhang, Zhongqi Wang et al. — [One Attack to Fool Them All: Highly Transferable Black-Box Adversarial Attacks on Frontier MLLMs](http://arxiv.org/abs/2609.33833v1)
  <details><summary>📄 Abstract</summary>
  Adversarial attacks have long posed a fundamental threat to machine learning systems. As multimodal large language models (MLLMs) rapidly evolve and become widely deployed, assessing their vulnerability to such attacks is essential for their safe use. In this work, we investigate whether a single adversarial image can consistently mislead diverse frontier MLLMs in black-box settings. We propose O-Attack, a highly transferable black-box attack framework. This framework builds on our insight that ...
  </details>


### 📂 privacy-leakage
*隐私泄露 / Privacy Leakage* — 37 papers

- **2026-09-28** — Ying Ma, Jarod Govers, Le Fang et al. — ["Black Mirror?": Public Sensemaking of AI-Powered Lifelogging](http://arxiv.org/abs/2609.34950v1)
  <details><summary>📄 Abstract</summary>
  AI-powered lifelogging wearables are emerging as a new class of consumer devices that transform everyday experience into searchable, AI-curated memory archives. We study early public sensemaking around these systems at the moment of their market entry, using the Looki L1 as an empirical lens. Analysing large-scale Chinese-language and English-language social media discourse (N = 5,053 comments), we combine topic clustering with inductive thematic analysis to examine how users interpret the socia...
  </details>

- **2026-09-28** — Hao Chen, Wenhui Dong, Ye Chen et al. — [CoSec: Benchmarking Agent Security in Communities](http://arxiv.org/abs/2609.34790v1)
  <details><summary>📄 Abstract</summary>
  LLM agents operate in persistent collaborative environments involving multiple users, communities, memories, files, and tools. Community boundaries may remain fixed or evolve with changes in membership, roles, composition, and relationships. Agents must complete legitimate tasks and prevent unauthorized disclosure of protected information. Existing evaluations do not fully examine these risks in agent systems. We introduce \textbf{CoSec}, an executable benchmark for evaluating privacy and author...
  </details>

- **2026-09-28** — Zimeng Huang, Shilei Chen, Jiatong Zhao et al. — [Loyal Agents: Training LLM Agents to Protect Principal Interests Under Strategic Information Asymmetry](http://arxiv.org/abs/2609.34714v1)
  <details><summary>📄 Abstract</summary>
  As LLMs increasingly act as delegated agents, they are expected to protect principals' interests when interacting with external parties. Standard alignment objectives, such as helpfulness, harmlessness, and honesty, do not specify how agents should protect principals' strategic interests under delegation. We formalize Agent Loyalty as an information-control property requiring agents to prevent Exploitable Information Leakage (EIL) and resist Manipulative Information Uptake (MIU). We introduce Lo...
  </details>

- **2026-09-28** — Xinyuan Qian, Yanghao Zhou, Ziyang Jiang et al. — [Multimodal Target Speaker Extraction: Towards Unified Speaker Cues Across Modalities](http://arxiv.org/abs/2609.35613v1)
  <details><summary>📄 Abstract</summary>
  Target Speaker Extraction (TSE) is pivotal in speech communication and human-computer interaction, enabling the isolation of a specific speaker's voice from complex acoustic environments, i.e., the cocktail party scenario. Although traditional TSE systems conditioned on enrollment speech have progressed substantially, enrollment speech as a cue has inherent limitations. Its reliability degrades when the target and interfering speakers have similar voice characteristics, when intra-speaker variab...
  </details>

- **2026-09-28** — Haowen Yang, Sophia Huerta, Yingying Wu — [AI-Assisted Identification of Magnetic Orders and Skyrmions](http://arxiv.org/abs/2609.35566v1)
  <details><summary>📄 Abstract</summary>
  Exotic magnetic orders in two-dimensional (2D) materials are attracting huge interest for energy-efficient spintronic applications, yet realizing robust high-temperature van der Waals antiferromagnets and topological magnetic states remains challenging. In this work, we develop a machine-learning framework for identifying magnetic orders and predicting magnetization using structural, compositional, and electronic information derived from the Materials Project. Fixed-length descriptors are constr...
  </details>

- **2026-09-28** — Qingzhe Bing, Kaiyuan Zhang, Yinqian Zhang — [INTCC: A Framework for Interactive Confidential Computing](http://arxiv.org/abs/2609.35552v1)
  <details><summary>📄 Abstract</summary>
  Confidential computing leverages Trusted Execution Environments (TEEs) to ensure the confidentiality and integrity of data in use. However, TEEs rely on remote attestation to guarantee the integrity of their initial memory state. This model is fundamentally at odds with interactive development workflows. In scenarios like LLM fine-tuning and exploratory data analysis, data processors need human-in-the-loop capabilities, including dynamic code injection, intermediate state inspection, and hyperpa...
  </details>

- **2026-09-28** — Fengzhou Sun, Yuan Zhang, Xintong Yu et al. — [EP-Mem: Elastic Privacy Memory for Social Relationship-Aware LLM Agents](http://arxiv.org/abs/2609.35233v1)
  <details><summary>📄 Abstract</summary>
  Large language model (LLM) agents face critical privacy risks when acting as delegates in human-agent-human communication. To prevent such breaches, agents must understand users' social relationships and adhere to context-dependent social information disclosure boundaries. Current studies on agent memory privacy focus on instantaneous interactions, leaving the long-term relational disclosure problem unexplored. In this paper, we propose EP-Mem, an Elastic Privacy Memory architecture that reframe...
  </details>

- **2026-09-28** — Fengming Gu, Mingjie He, Zonghui Guo et al. — [DBCF: Dual-Branch Complementary Fusion of Foundation Models for Generalized Deepfake Detection](http://arxiv.org/abs/2609.34720v1)
  <details><summary>📄 Abstract</summary>
  As image generation and editing technologies have progressed substantially, facial forgeries pose significant challenges to privacy and public safety. Due to limited ability to capture forgery cues, existing small-scale forgery detection models often struggle to generalize across various domains and unseen manipulations. To address this limitation, researchers have turned to large-scale foundation models, which can provide richer representations and better generalization. Nevertheless, relying o...
  </details>

- **2026-09-28** — Guy Lupo, Nguyen Hung Nguyen, Viet Vo et al. — [Poster: Towards ProofWeave: A Privacy-Minimised, Integrity-Anchored Evidence Plane for Continuous Agentic Assurance](http://arxiv.org/abs/2609.35234v1)
  <details><summary>📄 Abstract</summary>
  Agentic AI systems increasingly act via tools, memory, delegation, and external services. Existing observability and provenance mechanisms can reconstruct events post hoc, but they rarely show, at the time of the record, whether each policy-relevant action was checked by the intended control before execution. This leaves a trust-observability gap for continuous monitoring, detection, and response: later assurance may rest on evidence that is incomplete, privacy-leaking, mutable, or detached from...
  </details>

- **2026-09-28** — Shuxing Zhang, Yongquan Ni, Zhenyu Ding et al. — [Privacy-Preserving Full-Body Meshing from mmWave Radar via Mesh Foundation Model Supervision](http://arxiv.org/abs/2609.34768v1)
  <details><summary>📄 Abstract</summary>
  Millimeter-wave (mmWave) radar enables privacy-preserving human perception, but the extreme sparsity of point clouds from commercial single-chip sensors (mean ~6.5 points/frame; ~28% empty frames) has confined prior art to body-part keypoints or discrete action classification. We present a cross-modal teacher-student framework that lifts commercial radar to full-body, per-frame, metric 3D mesh reconstruction with per-joint uncertainty. Three innovations: (1) a mesh-foundation-model teacher - SAM...
  </details>

- **2026-09-28** — Zhengxiang Huang, Shengheng Chen, Chaoyue Niu et al. — [Dynamic Flow, Static Graph: KV Cache Reuse for Efficient LLM Serving on Mobile NPUs](http://arxiv.org/abs/2609.34727v1)
  <details><summary>📄 Abstract</summary>
  On-device large language model (LLM) serving is a cornerstone of local-first personal intelligence, offering users data sovereignty, strong privacy guarantees, and freedom from cloud API latency and cost. Although KV caching is widely used to reduce latency in long-context inference, existing designs were primarily optimized for cloud GPUs with dynamic execution environments and abundant memory bandwidth. These architectural assumptions do not hold on mobile NPUs, where computation graphs must b...
  </details>

- **2026-09-28** — Saeid Firouzi Daghigh, Saeed Ayat — [Evidence Before Accuracy: A MRI-PET Fusion Network for Alzheimer Disease Classification with Causal Regional Validation](http://arxiv.org/abs/2609.34520v1)
  <details><summary>📄 Abstract</summary>
  Deep learning models for Alzheimer disease (AD) classification routinely report near-perfect discrimination, yet few are shown to rest on AD-relevant neurobiology rather than on dataset artifacts, subject-level leakage, or non-brain image content. We present a fusion network combining T1 MRI and FDG PET across axial, coronal, and sagittal planes, trained on ADNI consists of 554 paired subjects. The fusion model reaches AUC 0.962, accuracy 0.909, and F1 0.891, competitive with recent 3D CNN and m...
  </details>

- **2026-09-28** — Haeun Jang, Yonghyun Jun, Hwanhee Lee — [Over-Personalization Is a Decision Failure: Generation-Induced Apply Bias in LLMs](http://arxiv.org/abs/2609.34284v1)
  <details><summary>📄 Abstract</summary>
  Personalized LLMs must decide, for each stored preference, whether the current context calls for applying or suppressing it, which we call its applicability. They frequently over-personalize, applying preferences the context rules out, yet existing benchmarks score only the final response and cannot tell where this failure arises. We decompose preference handling into three stages and measure each separately: (1) knowing whether a preference applies, (2) deciding on an explicit Apply/Suppress la...
  </details>

- **2026-09-28** — Linbo Shao, Huilin He, Yating Lou et al. — [Behavior-Grounded Semantic Enrichment for Financial Fraud Modeling and Reasoning](http://arxiv.org/abs/2609.34211v1)
  <details><summary>📄 Abstract</summary>
  In financial fraud detection, rich semantic context can provide important evidence for transaction behavior modeling and fraud reasoning. However, public real-world financial datasets often lack rich semantics due to privacy constraints. Consequently, synthetic datasets incorporate generated semantics, but at the cost of behavioral realism; textual descriptions for contextual reasoning remain scarce. We address this gap through a semantic enrichment framework grounded in original transaction beh...
  </details>

- **2026-09-28** — Yuzhuo Li, Di Zhao, Tingrui Qiao et al. — [Advancing Wildlife Conservation through Multimodal Animal Re-Identification with Environmental Metadata](http://arxiv.org/abs/2609.34094v1)
  <details><summary>📄 Abstract</summary>
  Identifying individual animals is crucial for effective wildlife monitoring and conservation efforts. Recent advancements in computer vision have shown promise in animal re-identification (Animal ReID) by leveraging data from camera traps. However, existing Animal ReID datasets rely exclusively on visual data, overlooking environmental metadata that ecologists have identified as highly correlated with animal behavior and identity, such as temperature and circadian rhythms. Meanwhile, modern visi...
  </details>

- **2026-09-27** — Dzung Pham, Dillon Sheils, Naina Singh et al. — [Can Prompt Anonymity Protect Your Identity From LLM Providers?](http://arxiv.org/abs/2609.33903v1)
  <details><summary>📄 Abstract</summary>
  User conversations with large language models (LLMs) often contain highly sensitive personal information that can be exploited by LLM providers to create detailed user dossiers, enable targeted advertising, and train more powerful models. To protect user privacy, anonymizing LLM proxies have emerged as a practical solution that separates user identity from their prompts, yet this approach still leaves the prompt content visible to LLM providers. We study the impact of this gap by conducting the ...
  </details>

- **2026-09-27** — Yiyong Liu, Jun Sakuma, Michael Backes et al. — [No Free Efficiency: Revisiting the Trade-off Between Training Efficiency and Model Vulnerability](http://arxiv.org/abs/2609.33898v1)
  <details><summary>📄 Abstract</summary>
  Training efficiency has become the central driver of recent progress in foundation models. To overcome the massive computational and data requirements of large-scale training, researchers increasingly adopt strategies such as selective data sampling, efficient pre-training, and simplified reinforcement learning pipelines. While these strategies drastically reduce overhead, they prompt a critical, yet neglected question: Is efficiency achieved at the expense of model robustness and security? To o...
  </details>

- **2026-09-27** — Yuwei Han, Lingwei Wei, Wooseong Yang et al. — [DynGraphAgentBench: A Benchmark for Agentic Lifecycle Control in Dynamic Graph Anomaly Detection](http://arxiv.org/abs/2609.33980v1)
  <details><summary>📄 Abstract</summary>
  Dynamic graph anomaly detection requires repeated decisions as graph structure and class prevalence drift, yet detector benchmarks usually score a fixed pipeline after current labels are known. We introduce DynGraphAgentBench, an executable benchmark for agentic lifecycle control under delayed feedback. It comprises seven temporal graph datasets with node- and edge-level anomaly tasks, eleven selectable detectors, and eight chronological deployment windows per dataset. In each window, a controll...
  </details>

- **2026-09-27** — Negar Alizadeh, Nishant Saurabh, Fernando Castor — [Green AI: Cost of LLM-Based Code Completion](http://arxiv.org/abs/2609.33918v1)
  <details><summary>📄 Abstract</summary>
  Code completion is one of the most widely used applications of large language models (LLMs) in software development. Open-weight LLMs are increasingly adopted for locally deployed code completion systems, partly due to privacy concerns. Despite advances in LLM accuracy, the energy cost of inference remains underexplored, particularly under large-context workloads and across programming languages. This study investigates the trade-off between accuracy and energy consumption in LLM-based code comp...
  </details>

- **2026-09-27** — Yiyong Liu, Jiayang Liu, Yixin Tan et al. — [Near-Duplicate Families Break Exact-Record Membership Inference](http://arxiv.org/abs/2609.33909v1)
  <details><summary>📄 Abstract</summary>
  Membership inference (MI) asks whether a specific record appeared in a model's training set and is increasingly used as evidence for data provenance and copyright auditing. These applications require determining whether the exact queried record was used for training, rather than merely whether the model was exposed to similar content. Making this distinction is challenging because web-scale datasets naturally contain near-duplicates, including syndicated articles, mirrored pages, and lightly mod...
  </details>

- **2026-09-27** — Luyang Fang, Haoran Lu, Jiazhang Cai et al. — [A Statistical Perspective on Knowledge Distillation: Foundations, Classical Methods, and Large Language Model Extensions](http://arxiv.org/abs/2609.33727v1)
  <details><summary>📄 Abstract</summary>
  Knowledge Distillation (KD) has emerged as a vital paradigm for transferring the capabilities of high-capacity models to efficient ``student'' counterparts, addressing critical challenges in computational cost, deployment constraints, and privacy-sensitive settings. Although KD is widely used in practice, it is often viewed primarily as an engineering technique, with a unified statistical perspective remaining less developed. This review bridges that gap by presenting a unified Bayesian formulat...
  </details>

- **2026-09-27** — Gert Lek, Abele Malan, Chaoyi Zhu et al. — [Safety Reconstructed: Generative Modeling via Masked Diffusion Builds Strong Safety Guardrails](http://arxiv.org/abs/2609.33634v1)
  <details><summary>📄 Abstract</summary>
  Guard models are the last line of defense between a language model and a harmful output, yet their training objective is surprisingly narrow. Existing guards learn to predict a single verdict token from a conversational context, concentrating supervision on a single target. The consequences are structural: models latch onto shortcut features, are overconfident, and remain sensitive to where safety evidence appears in the sequence rather than its role in the full context. We propose a different f...
  </details>

- **2026-09-27** — Dipankar Sarkar — [When Privacy Moves ML-Mediated Decisions On Device: Information and Incentive Misalignment in Auctions](http://arxiv.org/abs/2609.33312v1)
  <details><summary>📄 Abstract</summary>
  Moving ML-mediated decision making onto privacy-preserving clients decentralises the economic decision along with the inference. Shared budget constraints then depend on information that cannot be globally current, creating an information-structure failure that conventional pacing is not designed to solve. We study this information misalignment in an auction-logic-faithful on-device simulation with 36 campaigns and 50 devices. Accounting is in dimensionless integer score units; no currency seman...
  </details>

- **2026-09-27** — Thanina Hamitouch, Khadidja Henni, Abdelkrim Arie et al. — [BERT4DTI : BERT-based Model for Predicting Drug-Protein Interactions](http://arxiv.org/abs/2609.33254v1)
  <details><summary>📄 Abstract</summary>
  Understanding how drugs interact with protein targets is fundamental to drug discovery, drug repurposing and the early identification of promising therapeutic candidates before costly experimental testing. Sequence-based DTI models face three practical limitations: labelled interactions are scarce and unevenly distributed, large pretrained chemical and protein encoders are expensive to fine-tune end-to-end, and independently encoded sequences do not capture pair-specific dependencies. We present...
  </details>

- **2026-09-27** — Ya-Wen Wu, Meng-Fen Chiang, Kuang-Da Wang et al. — [CAME: Company-Aware Evidence-Memory Experts for Interpretable Quarter-Ahead Revenue Forecasting](http://arxiv.org/abs/2609.33143v1)
  <details><summary>📄 Abstract</summary>
  Quarter-ahead revenue forecasting requires company-scale numerical accuracy, strict temporal validity, and company-specific interpretation of narrative disclosures. LLMs can distill textual evidence but can produce scale-misaligned forecasts, whereas history-based anchors are stable but miss forecast-time signals such as product transitions, supply constraints, and management guidance. We introduce CAME (Company-Aware Evidence-Memory Experts), a residual-forecasting framework that refines a no-l...
  </details>

- **2026-09-27** — Moghis Fereidouni, Anthony Arnold, Sumit Gulwani et al. — [On Device Agentic Operation Caches -- Classifier-Centric NL-to-Action Generation](http://arxiv.org/abs/2609.33141v1)
  <details><summary>📄 Abstract</summary>
  Agentic AI is increasingly being embedded in software applications to provide natural language interfaces to features and functionality. In most cases these agents are powered by enterprise (100+ billion parameter) or frontier class large language models that require substantial computational resources run and depend on cloud hosted inference to handle the task of transforming natural language inputs into actionable software operations. This reliance on cloud-hosted inference introduces substant...
  </details>

- **2026-09-27** — Prasanjit Dubey, Xiaoming Huo — [Byzantine-Robust Federated RAG via Aligned Calibration and Fixed-Membership Conformal Prediction](http://arxiv.org/abs/2609.33037v1)
  <details><summary>📄 Abstract</summary>
  Retrieval-augmented generation (RAG) lets language models answer questions more accurately by consulting relevant documents. Many valuable collections, such as medical records, cannot be pooled because of privacy rules. Federated RAG leaves each collection with its owner, or node, which scores candidate answers from its own documents; a central hub combines the scores. Some nodes, called Byzantine, may be compromised, faulty, or misled by instructions hidden in documents, and report arbitrary sc...
  </details>

- **2026-09-26** — Sasank Annapureddy, Anjaneya Prasad Thamatani — [The Epistemics of Agent Memory: Measuring, and Governing, the Consolidation Decision in Long-Horizon LLM Agents](http://arxiv.org/abs/2609.33013v1)
  <details><summary>📄 Abstract</summary>
  Long-horizon LLM agents must convert accumulated experience into durable memory, deciding what to keep, compress, abstract into reusable skills and rules, or forget. We report a four-phase research program on this consolidation problem whose central finding is a shift in what is measured: from how much an agent remembers, to whether its consolidation decisions are any good, to whether those decisions can be trusted.   Phase 1 learns episodic boundaries from agent traces by downstream utility; an...
  </details>

- **2026-09-26** — Jeongho Yoon, Chanhee Park, Yongchan Chun et al. — [Learning to Refer: Client-Resolved Generation for Privacy-Aware Language Models](http://arxiv.org/abs/2609.32706v1)
  <details><summary>📄 Abstract</summary>
  Cloud-based large language models (LLMs) require users to disclose plaintext data to service providers, creating privacy risks in sensitive domains. Existing privacy-preserving approaches often trade utility for protection, incur substantial computational or communication overhead, remain vulnerable to reconstruction from intermediate representations, or protect only a subset of the training and inference pipeline. We introduce Client-Resolved Generation (CRG), a genera- tion interface that sepa...
  </details>

- **2026-09-26** — Mahmudul Faisal Al Ameen — [Reading Is Not Leaking: Local, Auditable Measurement and Reduction of Inference Exposure from Public Footprints](http://arxiv.org/abs/2609.32565v1)
  <details><summary>📄 Abstract</summary>
  Anyone with a public footprint leaks facts that were never stated, and language models make the inference cheap. We present a framework for measuring and reducing this inference exposure that runs on the owner's own CPU with no language model at analysis time, instantiated on organisations and on individuals. It starts from a measurement result: scoring an inference system against the target's private truth conflates how well the system reads the record with how much the record leaks. On a 128-q...
  </details>

- **2026-09-26** — Muhammed Ustaomeroglu, Ziyue Xu, Hanshen Xiao et al. — [TRAP: Understanding and Mitigating Privacy Memorization in Language Models](http://arxiv.org/abs/2609.32293v1)
  <details><summary>📄 Abstract</summary>
  Fine-tuning a language model on sensitive records can leave it able to reproduce them. We ask when this memorization arises and how to prevent it without knowing in advance which spans are sensitive. Our starting point is that most memorization scores and attacks share one statistical core: whether the model assigns a token more probability than some reference would. Taking as the reference a model trained on the complementary half of the same corpus gives the Target Reference Advantage (TRA), a...
  </details>

- **2026-09-26** — Jeremy Kepner, Hayden Jananthan, LaToya Anderson et al. — [Analyzing 10 Petabit/s Network Data with Accelerated Associative (Token) Arrays](http://arxiv.org/abs/2609.32978v1)
  <details><summary>📄 Abstract</summary>
  As networks expand and become an ever more critical infrastructure to modern society the need to analyze these networks with the highest regard for privacy is essential to ensure their proper function. Depending on the level of the network layer to be analyzed, sources and destinations can be any combination of physical, logical, or persona/agentic endpoints, which requires the ability to handle diverse data. Invaluable to these analyses are mathematical tools that enable sophisticated mathemati...
  </details>

- **2026-09-26** — Asif Shahriar, Md Nafiu Rahman, Sadif Ahmed et al. — [AgentTell: Behavioural Side-Channel Leakage in Browser-Use Agents](http://arxiv.org/abs/2609.32915v1)
  <details><summary>📄 Abstract</summary>
  Browser-use agents often carry information in their context as they move between websites. While it may be necessary for task completion, it also creates a privacy risk, especially when the information contains a private fact regarding the user. For example, an agent may learn a user's affiliation after reading a membership record. If it later selects a registration option specific to that affiliation on another website instead of a general option, the information gets leaked. In this work, we d...
  </details>

- **2026-09-26** — Jerry Huang, Sarvesh Babu, Matt Van Buren et al. — [FinancialAuditBench: Benchmark Construction under Differential Privacy Using Real-World Priors](http://arxiv.org/abs/2609.32835v1)
  <details><summary>📄 Abstract</summary>
  As AI agents are becoming widely adopted in the financial services industry, careful measurement is essential to understand where they can be reliably deployed and where oversight and professional review remain necessary. Such measurement, however, is constrained by limited access to proprietary or privacy-sensitive data. Existing benchmarks therefore often rely on publicly available data, human- and/or LLM-authored tasks, or simplified settings. We introduce FinancialAuditBench, a benchmark for...
  </details>

- **2026-09-26** — Jialuo He, Huangxun Chen — [From Knowing to Abstaining: Bridging the Representation-Action Gap in Vision-Language Models](http://arxiv.org/abs/2609.32653v1)
  <details><summary>📄 Abstract</summary>
  The ability of vision-language models (VLMs) to abstain from unanswerable questions is as important as their ability to answer answerable ones accurately. Recently, several benchmarks have emerged to evaluate and improve VLM abstention, but they have substantial limitations. First, samples often contain shortcut cues in images or questions that reveal answerability, while an explicit "unanswerable" option further prevents accurate assessment of spontaneous abstention. Second, as training data, t...
  </details>

- **2026-09-26** — Yanmeng Wang, Yunxuan Li, Shilong Fan et al. — [Ask Without Telling: Local SLMs Consult Cloud LLMs Without Revealing Task Intent](http://arxiv.org/abs/2609.32642v1)
  <details><summary>📄 Abstract</summary>
  As local small language models (SLMs) increasingly collaborate with more capable cloud large language models (LLMs), a natural privacy question arises: Can a local SLM obtain cloud LLM guidance while protecting user privacy? Existing privacy-preserving SLM-LLM frameworks primarily hide sensitive values while preserving task semantics, which can still expose what the user is trying to accomplish. For example, allocating scarce medical supplies across hospitals may signal an emerging public-health...
  </details>

- **2026-09-26** — Viktoriya Bu-Dager, Silvia Cirstea — [Using Machine Learning to Investigate Predictors of Fasting Blood Glucose: Insights into Circadian Timing and Age Interactions](http://arxiv.org/abs/2609.32386v1)
  <details><summary>📄 Abstract</summary>
  Impaired glucose regulation is a major contributor to metabolic dysfunction and type 2 diabetes. This study developed an interpretable machine-learning framework to predict log-transformed fasting blood glucose using metabolic, hormonal, lifestyle, demographic, nutritional, and circadian variables from the National Health and Nutrition Examination Survey 2017--2020 pre-pandemic dataset. After merging multiple NHANES sub-datasets, data processing used a leakage-resistant pipeline in which imputat...
  </details>


### 📂 misuse
*滥用与误用 / Misuse & Abuse* — 20 papers

- **2026-09-28** — Xinjie Shen, Junran Wang, Rongzhe Wei et al. — [SEAD: A State-Based Perspective on Attack and Defense in Tool-Using Agents](http://arxiv.org/abs/2609.34518v1)
  <details><summary>📄 Abstract</summary>
  Language-model agents increasingly use tools to act on external systems. Earlier actions can alter files, permissions, database records, or other state, making a later routine-looking action harmful. Yet the visible interaction may not reveal the underlying state needed to assess that action. We formulate attack and defense as partially observed state control in SEAD, deriving their design requirements from this shared execution process. Because attackers supply instructions while the target cho...
  </details>

- **2026-09-28** — Zhiwei Chen, Tianchun Wang, Zhongtao Rao et al. — [SAGE: Structured Strategic Reasoning for Efficient LLM Game Playing](http://arxiv.org/abs/2609.34342v1)
  <details><summary>📄 Abstract</summary>
  A strong LLM strategic agent should reason prospectively over uncertain futures, adapt its strategy to opponents' behavioral tendencies, and continuously recalibrate its decision process from interaction experience. However, incorporating these sources in free-form reasoning could lead to unsupported strategic assumptions, inconsistent opponent estimates, and harmful interference from irrelevant historical interactions. To address these issues, we propose SAGE, a training-free inference-time fra...
  </details>

- **2026-09-28** — Xu Wang, Difan Zou, Xuansheng Wu — [Less Sycophancy, Stronger Refusal? Lessons for AI Safety from Mechanistic Interpretability](http://arxiv.org/abs/2609.35544v1)
  <details><summary>📄 Abstract</summary>
  Reliable refusal of harmful requests is essential to the safe deployment of language models. Because excessive eagerness to please users may undermine existing refusal capabilities, reducing sycophancy offers a potential route to stronger refusal beyond the harmful scenarios covered by safety training. We investigate this possibility using compensatory feature injection (CFI), a training technique designed to limit the acquisition of a target concept by supplying its associated activation during...
  </details>

- **2026-09-28** — Guanxu Chen, Qihao Lin, Jing Shao — [Imprint Reader: From Weight-Update Readout to Behavioral Intervention](http://arxiv.org/abs/2609.35261v1)
  <details><summary>📄 Abstract</summary>
  As language models take a growing role in AI development, a natural aspiration is for them to reflect on their own learning process, as humans do, and use that reflection to improve themselves. At the same time, these models have an advantage that human learners lack, since training leaves parameter-level traces that can, in principle, be inspected directly. However, current models cannot decode these traces into an explicit account of what they have learned. To this end, we introduce the \texti...
  </details>

- **2026-09-28** — Abel Rodríguez, Giuseppe Garofalo, Lieven Desmet et al. — [Tool Mediation Alters Refusal Mechanisms in Large Language Models](http://arxiv.org/abs/2609.35117v1)
  <details><summary>📄 Abstract</summary>
  Large language models (LLMs) are increasingly deployed with access to external tools, yet harmful tool-mediated interactions are less likely to be refused when compared to regular conversational ones. As this change in refusal behavior remains underexplored, we investigate its underlying mechanisms across a diverse set of open-weight language models. We find that information about the harmfulness of a request remains strongly encoded in the model's representations and transfers across conversati...
  </details>

- **2026-09-28** — Weiqiao Que, Ruizhe Li, Chengyu Wang et al. — [See it, Say it, Sorted: Mechanistic Diagnosis and Parameter-Space Mitigation of Emergent Misalignment in LLMs](http://arxiv.org/abs/2609.34970v1)
  <details><summary>📄 Abstract</summary>
  Safety-aligned LLMs can exhibit emergent misalignment (EM): narrow domain adaptation unexpectedly triggers catastrophic safety failures across unrelated domains. Prior static analyses leave training dynamics unmapped, while existing defenses rely on heuristics that degrade utility. We present a dynamic, second-order geometric study of EM. Tracking training trajectories reveals that directional Hessian curvature concentrates sharply on semantic pivot tokens. Grassmannian projections show that, in...
  </details>

- **2026-09-28** — Chenxi Wang, Ruiyang Huang, Li Huang et al. — [How to Tame a Multi-Headed Hydra? Adaptive Multi-Category Safety Steering for Large Language Models](http://arxiv.org/abs/2609.34514v1)
  <details><summary>📄 Abstract</summary>
  As large language models (LLMs) become increasingly widespread, preventing unsafe responses to harmful prompts is essential for their safe deployment. Activation steering offers an approach to improving LLM safety by modifying internal activations during inference without updating model parameters. However, a single prompt can involve multiple harm categories, and steering toward safety in one category may leave harmful content from another unaddressed. Despite advances in adaptive steering, exi...
  </details>

- **2026-09-28** — Ruifan Zuo, Guocheng Hu, Wanshui Gan et al. — [SpatialSkill: Self-Evolving Skills for Cross-View Spatial Reasoning](http://arxiv.org/abs/2609.34124v1)
  <details><summary>📄 Abstract</summary>
  Cross-view spatial reasoning requires a model to align different viewpoints into a coherent spatial representation, yet this ability remains challenging for vision-language models despite being natural to humans. Existing methods typically improve spatial reasoning by updating model weights, which keeps the acquired knowledge implicit and tied to a specific backbone. We propose \textit{SpatialSkill}, a weight-update-free framework that enables a frozen vision-language model to accumulate explici...
  </details>

- **2026-09-28** — Sofiia Kosar, Anil R. Pininti, Vladyslav Hnapovskyi et al. — [High-Throughput Imaging of Degradation-Inducing Microscopic Impurities in Perovskite Solar Cells](http://arxiv.org/abs/2609.35510v1)
  <details><summary>📄 Abstract</summary>
  The scalable fabrication of high-quality, large-area perovskite thin films is hindered by microscopic inhomogeneities, particularly residual compositional impurities formed during processing. Identifying these impurities, understanding their impact on device operation, and enabling their rapid detection are essential for upscaling perovskite solar cells (PSCs). Here, nano-Fourier transform infrared spectroscopy combined with high-resolution optical and scanning probe techniques was used to ident...
  </details>

- **2026-09-28** — Xin Li, Mengbing Liu, Chau Yuen — [Measuring Collapse and Correction in Homogeneous-Panel LLM Debate](http://arxiv.org/abs/2609.35279v1)
  <details><summary>📄 Abstract</summary>
  Multi-agent large language model (LLM) debate is often evaluated by whether final answers improve, but movement is not necessarily improvement: the same discussion can rescue an initially wrong majority or destroy an initially correct one. Standard final-accuracy evaluations conflate these opposing mechanisms. We introduce an auditable protocol for homogeneous debate on multiple-choice questions (MCQs) that records each run as a transition ledger over collapse, correction, onset, and signed inte...
  </details>

- **2026-09-28** — Yaxiao Liu, Pengbo Liu, Yiwen Liu et al. — [5W1H+Which: Context-Valid Semantic Indexing with Progressive Ontology Binding](http://arxiv.org/abs/2609.35184v1)
  <details><summary>📄 Abstract</summary>
  Transforming raw data into queryable knowledge requires both early extraction of reusable information and explicit types, relations, and applicability conditions for particular tasks. If indexing selects content too early around a single business schema, later tasks may be unable to use information that was omitted. If the index retains only open-ended text, however, rule-based reasoning lacks checkable premises. We propose 5W1H+Which, a semantic indexing design that separates content extraction...
  </details>

- **2026-09-27** — Yingdan Shi, Ren Wang — [Trajectory Unlearning on LLM-based Agents](http://arxiv.org/abs/2609.33639v1)
  <details><summary>📄 Abstract</summary>
  Existing large language model (LLM) unlearning has focused primarily on removing specific knowledge, such as harmful facts, private data, or copyrighted content. However, as LLMs are increasingly deployed as autonomous agents, a fundamental yet overlooked problem emerges: beyond suppressing what an agent knows, an agent should not reproduce undesired behaviors through its action trajectories. In this work, we introduce trajectory-level unlearning, a new problem formulation that targets the remov...
  </details>

- **2026-09-27** — Kai Mei, Zhiyuan Hu, Yutong Dai et al. — [Opera: A Verbal Critic Framework for Long-horizon Coding Agents](http://arxiv.org/abs/2609.33987v1)
  <details><summary>📄 Abstract</summary>
  Long-horizon coding agents need timely corrections, yet feedback can be ineffective or even harmful when it misjudges ongoing work or fails to address the underlying problem. Existing critics focus on evaluating trajectories and generating feedback, but rarely track what happens after feedback is delivered. We present Opera, a verbal critic framework that treats each correction as a persistent note, followed until the diagnosed problem is resolved. Opera decides when to review through periodic a...
  </details>

- **2026-09-27** — Qing Yang, Zhenyu Mao, Zixiang Luo et al. — [LA-CPD: Local-Evidence-Aware Change-Point Detection for Human-LLM Authorship Segmentation](http://arxiv.org/abs/2609.33787v1)
  <details><summary>📄 Abstract</summary>
  As LLM-generated text becomes increasingly human-like, accurately localizing LLM-authored spans in human-LLM co-authored documents is important for attribution and accountability in cases involving copyright infringement, fraud, and other harmful uses of AI-generated content. Sentence-level detectors provide local authorship evidence, but content variation can cause score fluctuations even among sentences from the same source, creating spurious boundaries. Recovering a coherent document partitio...
  </details>

- **2026-09-27** — Hao Chen — [COGNIT-Guard: Calibrated Standalone Direct-Decision Guardrails with Heterogeneous CPU-NPU Confidence Cascading under Explicit Latency and False-Positive Constraints](http://arxiv.org/abs/2609.33671v1)
  <details><summary>📄 Abstract</summary>
  When must a foundation-model safety gateway generate tokens, and when should it directly output a calibrated decision? We study calibrated standalone direct-decision foundation models for real-time pre-ingestion safety guardrails, jointly addressing probability calibration, dual-use false-positive control, and heterogeneous CPU-NPU routing under explicit latency SLOs. Pre-ingestion guardrails must screen prompts prior to target-LLM prefill with low false alarms on benign compliance inquiries; ho...
  </details>

- **2026-09-27** — Cunchun Li, Haonan He, Yifan Gao et al. — [Rethinking Token Reweighting for SFT: Suppress, Reverse, and Extrapolate Learned Features](http://arxiv.org/abs/2609.33463v1)
  <details><summary>📄 Abstract</summary>
  Supervised fine-tuning (SFT) learns most aggressively from tokens that the model deems least likely. This helps acquire new behaviors, but also amplifies noisy or conflicting supervision and can overwrite useful pretrained knowledge. Through a unified policy-loss view, we revisit existing token-reweighting methods and show that they assign nonnegative coefficients to demonstrated tokens. Consequently, they can suppress or amplify supervised updates, but cannot reverse harmful features once learn...
  </details>

- **2026-09-27** — Jiashu He, Jinxuan Fan, Xiao Xiao et al. — [Ceiling of a Task: When Can a Transformer Succeed Without Its Chain of Thought?](http://arxiv.org/abs/2609.33134v1)
  <details><summary>📄 Abstract</summary>
  Reasoning models generate long chains of thought before they answer, yet it is debated whether the content of these chains does real computational work or is largely decorative. We study this question by viewing a transformer as a shallow circuit. One forward pass through a fixed number of layers has constant depth, so any procedure that runs the model a constant number of times is a shallow circuit. We call the best accuracy that a shallow circuit can reach on a task the ceiling of the task, an...
  </details>

- **2026-09-27** — Difan Jiao, Ashton Anderson — [Agent Safety From Within: Detecting Harmful Trajectories from LLM Internal States](http://arxiv.org/abs/2609.33039v1)
  <details><summary>📄 Abstract</summary>
  Language model agents can now perform sophisticated sequences of actions via tools and harnesses, which has increased the scope of the damage they can cause. Guard models, however, are mainly built for content moderation and thus are not well-suited to detecting this agentic risk. To address this, we proceed by first conducting a representational analysis, then use the resulting insights to build a solution. In our analysis, we focus on two types of trajectory-level agentic harms: harmful conten...
  </details>

- **2026-09-26** — Diego Palma, Kyu Bin Kim, Zhen Han et al. — [Business Compromise Detection with Agentic AI and LLM-driven Knowledge Discovery](http://arxiv.org/abs/2609.32643v1)
  <details><summary>📄 Abstract</summary>
  Detecting compromised business ad accounts is a challenge in digital advertising, as attackers exploit hijacked accounts to launch fraudulent campaigns. Large Language Model (LLM) agents show promise for integrity enforcement, but hallucinated mistakes on hard cases create business friction. In a study we find the autonomous agent is a strong, recall-heavy signal extractor but an unreliable final arbiter, conceding precision on ambiguous decisions. We therefore keep the agent as an investigator ...
  </details>

- **2026-09-26** — Beicheng Xu, Bowen Fan, Weitong Qian et al. — [Multi-Agent System Search via Active Substructure-aware Policy Optimization](http://arxiv.org/abs/2609.32430v1)
  <details><summary>📄 Abstract</summary>
  LLMs enable multi-agent systems (MAS) to tackle complex tasks, but manually designing agent roles, prompts, and communication structures requires substantial expertise and effort. This motivates learning policies that construct query-specific MAS from execution reward. Existing approaches typically train these policies by repeatedly traversing a fixed set of training queries and assigning rewards at the workflow level. However, this overlooks differences in queries' evolving learning potential a...
  </details>


### 📂 red-teaming
*红队测试 / Red Teaming* — 1 papers

- **2026-09-28** — Dmitrii Kharlapenko, Sergei Bratchikov, Konstantin Korolev et al. — [RISE: Red-teaming via Iterative Strategy Evolution for Modern Text-to-Image Models](http://arxiv.org/abs/2609.34920v1)
  <details><summary>📄 Abstract</summary>
  On modern production text-to-image systems, successful policy violations are rare, and previously effective human-written seeds are often patched out. Current automated red-teamers are poorly matched to this regime in two ways: unreliable success measurement and poor exploration. First, we find that judges widely used in prior T2I red-teaming work are unreliable under vague unsafe-content targets: they either miss true violations or reward benign borderline images on hardened APIs. We therefore ...
  </details>


### 📂 vulnerability
*漏洞与攻击面 / Vulnerabilities & Attack Surfaces* — 63 papers

- **2026-09-28** — Wenxin Shao, Siqi Chai, Kun Li et al. — [Humanoid Loco-Manipulation With Discrete VLA Model](http://arxiv.org/abs/2609.35709v1)
  <details><summary>📄 Abstract</summary>
  Vision-language-action (VLA) models using discrete action tokens have proven effective for controling robotic arms on manipulation tasks. For a humanoid, however, the whole-body action space -- legs, torso, arms, and hands -- is far higher-dimensional and heterogeneous, raising tokenization, training, and real-time inference challenges that the previous VLA models do not address. We present Holo-M, to our knowledge the first discrete VLA model for humanoid loco-manipulation that intrinsically ex...
  </details>

- **2026-09-28** — Priyanka Kargupta, Silviu Cucerzan, Shweti Mahajan et al. — [Reinforcing Agentic Creativity in Scientific Ideation with Night Science](http://arxiv.org/abs/2609.35706v1)
  <details><summary>📄 Abstract</summary>
  Large language models (LLMs) excel at structured, verifiable tasks, but their low-entropy bias can produce homogeneous and predictable outputs, limiting their utility for open-ended scientific ideation. Effective discovery, however, spans a broader creative spectrum: from structured day science to loosely structured, serendipitous night science that reaches ideas beyond those typically considered. We introduce AI Night-Scientist, an agentic framework that uses reinforcement learning to teach mod...
  </details>

- **2026-09-28** — Qiyao Ma, Junshan Zhang, Zhe Zhao — [Rethinking Personalized Generation: Test-Time Alignment via Factorized Ranking Models](http://arxiv.org/abs/2609.35695v1)
  <details><summary>📄 Abstract</summary>
  Aligning large language models (LLMs) to diverse user preferences is fundamentally hindered by standard alignment paradigms that optimize for monolithic users. In this work, empirical studies are first used to reveal the existence of a massive, untapped performance headroom for personalized generation through test-time alignment. We demonstrate that personalized generation is uniquely suited for test-time scaling methods like Best-of-N (BoN) because it can be viewed primarily as a candidate matc...
  </details>

- **2026-09-28** — Pedro R. A. S. Bassi, Wenxuan Li, Hanxue Gu et al. — [RT-Super: Learning Tumor Segmentation from Longitudinal Images and Reports](http://arxiv.org/abs/2609.35637v1)
  <details><summary>📄 Abstract</summary>
  Multi-tumor segmentation is important for early cancer detection and allows radiologists to visualize, verify, and understand AI predictions. However, tumor segmentation masks are expensive, time-consuming, and unavailable for many tumor types in public data. Instead, hospitals have vast, readily available data that can guide segmentation: radiology reports, longitudinal images, and multi-phase images. We use this readily available data to substitute for tumor masks in training AI for tumor segm...
  </details>

- **2026-09-28** — Nazim Bendib, Nicolas Perrin-Gilbert, Olivier Sigaud — [Behavioral Foundation Models for Quality Diversity](http://arxiv.org/abs/2609.35615v1)
  <details><summary>📄 Abstract</summary>
  Behavioral Foundation Models (BFMs) are an emerging paradigm in reinforcement learning, playing a role analogous to large language models in natural language processing: they have shown remarkable versatility, enabling zero-shot performance, fast imitation, and online adaptation, all by exploiting the structure of a latent space. In this work, we investigate whether the latent behavioral space induced by BFMs can serve as an effective search space to discover large repertoires of behaviorally di...
  </details>

- **2026-09-28** — Luke Leckie, Peter M. Todd, Jacob G. Foster — [Signatures of semantic search in the activations of large language models](http://arxiv.org/abs/2609.35599v1)
  <details><summary>📄 Abstract</summary>
  When recalling lists of concepts (e.g., animals) during the semantic fluency task (SFT), both humans and large language models (LLMs) organise their output into clusters of related items (e.g., sea animals) that are punctuated by strategic switches between clusters. In humans, this pattern can be explained by a semantic foraging process, whereby distinct neural and behavioural signatures accompany within-cluster production ("exploit") and between-cluster switching ("explore"). Whether LLMs likew...
  </details>

- **2026-09-28** — Yaxin Du, Xiyuan Yang, Zhifan Zhou et al. — [RSI-Master: Structuring Experiments to Guide Autonomous Model Improvement](http://arxiv.org/abs/2609.35561v1)
  <details><summary>📄 Abstract</summary>
  Recursive self-improvement (RSI) seeks to enable AI systems to participate in improving their own capabilities. A concrete pathway is autonomous model development, where agents iteratively explore post-training strategies to improve a base model. This setting faces two challenges: agents may exploit open-ended experimental actions through hacking, and repeated experimentation may lead to strategy lock-in, where an early direction is refined rather than reconsidered. We introduce RSI-Master, whic...
  </details>

- **2026-09-28** — Ruishuo Chen, Weijia Li, Xun Wang et al. — [One Proposal for Every Margin: Zero-Shot Amortized Sequential Importance Sampling for Binary Matrices](http://arxiv.org/abs/2609.35514v1)
  <details><summary>📄 Abstract</summary>
  In ecology, psychometrics, and the analysis of social and financial networks, binary matrices are often analyzed conditional on their observed row and column sums, which restricts the problem to a finite sample space of matrices with the same margins. Two fundamental problems are to count this space and to sample uniformly from it. Sequential importance sampling (SIS) addresses both with independent weighted samples and an unbiased count estimator, but its efficiency depends critically on the pr...
  </details>

- **2026-09-28** — Joni Herttuainen, Kirsi Hellsten, Vesa Kuikka et al. — [AI-Based Vulnerability Assessment Capability and Cyber Attack Graph Analysis](http://arxiv.org/abs/2609.35414v1)
  <details><summary>📄 Abstract</summary>
  Cyber threats targeting mission-critical infrastructure are becoming more sophisticated while the barrier to launching attacks continues to fall. Traditional point solutions like antivirus and firewalls are reactive and fail to address the combinatorial complexity of modern attack surfaces. This paper presents an investigation combining two complementary methodologies: Lockheed Martin's Vortex/Crow framework, which applies multi-agent reinforcement learning (MARL) over industry-standard cyber kn...
  </details>

- **2026-09-28** — Fahrell Giovanny, Geby Bayuningtyas, Sahrul Mukharom et al. — [Epistemic Policy Divergence in Multi-Turn LLM Contamination: A Protocol-Gradient Investigation](http://arxiv.org/abs/2609.35308v1)
  <details><summary>📄 Abstract</summary>
  Large language models process conversation history as unverified context: false premises injected into prior turns can be adopted as fact, a failure mode we term session-level contamination. We introduce five contamination protocols arranged along a source-authority gradient, isolating distinct failure mechanisms while holding the false premise constant, and evaluate GPT-5.4 Mini, Gemini-3.1 Flash-Lite, and GLM-4.5-Air across ten knowledge domains at temperature zero (22,500 turns), using a dual...
  </details>

- **2026-09-28** — Yilun Qiu, Xiaoyan Zhao, Chengbing Wang et al. — [Rubric-Aware On-Policy Self-Distillation for LLM Personalization](http://arxiv.org/abs/2609.35262v1)
  <details><summary>📄 Abstract</summary>
  LLM personalization aims to generate responses aligned with individual users' preferences and needs. User-specific rubrics make these expectations explicit, providing direct supervision on what a satisfactory answer should cover. Existing rubric-guided approaches, however, exploit such guidance only at a coarse granularity, either by using rubrics to supervise the prediction of relevant aspects for subsequent generation or by reducing aspect coverage to a single response-level reward for reinfor...
  </details>

- **2026-09-28** — Prateek Kumar Rajput, Abdoul Kader Kabore, Yewei Song et al. — [Trajectory-Level Security Debt in LLM Coding Agents](http://arxiv.org/abs/2609.35199v1)
  <details><summary>📄 Abstract</summary>
  LLM coding agents can traverse hundreds of intermediate code states before submitting a solution. Evaluating only the final artifact leaves the evolution of security findings unmeasured. We introduce the Security Debt Line Integral (SDLI), which accumulates static-analysis risk when an agent reaches a new best test pass ratio. We instantiate it with four static application security testing (SAST) tools and study artifacts from 830 passing SWE-bench runs, 712 ProgramBench final workspaces, and 13...
  </details>

- **2026-09-28** — Jiaan Zhu, Wei Gao, Youhui Bai et al. — [PEARL: Adaptive Prefill-Decode Execution with Elasticity for Agentic Reinforcement Learning](http://arxiv.org/abs/2609.35158v1)
  <details><summary>📄 Abstract</summary>
  Multi-turn rollout dominates the cost of agentic reinforcement learning (RL). Asynchronous execution and elastic GPU resources can accelerate this stage, but adding rollout replicas yields diminishing returns while training GPUs remain idle between updates. We observe that effective resource use also depends on the prefill--decode (PD) configuration. Both the choice between colocation and disaggregation and the optimal PD ratio vary with the workload, making resource scaling and PD configuration...
  </details>

- **2026-09-28** — Fida M. Thoker, Renaud Vandeghen, Karen Sanchez et al. — [Advancing Video-Text Pretraining with Multi-View Captions](http://arxiv.org/abs/2609.35090v1)
  <details><summary>📄 Abstract</summary>
  Video-text pretraining has achieved remarkable progress through the scaling of models and datasets, yet the quality of language supervision remains underexplored. Existing web-scale datasets often provide only a single sparse caption per video that fails to capture rich spatiotemporal semantics, while directly using captioning models can generate noisy descriptions. We propose a large-scale multimodal large language model-based supervision generation framework that improves supervision diversity...
  </details>

- **2026-09-28** — Zeqin Liao, Yuhong Nan, Henglong Liang et al. — [SmartMemory: Detecting On-chain-off-chain Communication Inconsistency for Smart Contract via Memory-based Agent](http://arxiv.org/abs/2609.34983v1)
  <details><summary>📄 Abstract</summary>
  Smart contracts underpin decentralized finance, where growing demand for on-chain/off-chain communication(OFC) has driven diverse applications such as cross-chain bridges, real-world asset tokenization, and fiat-backed stablecoins. TheOFC-related security incidents in these applications are increasingly frequent, but prior studies address separate vulnerability categories within OFC applications rather than providing a unified view, causing vulnerabilities outside known patterns to be missed.In ...
  </details>

- **2026-09-28** — Zijian Dai, Sen Han, Youhui Bai et al. — [WaveAlign: Cache-Aware Query-Row Scheduling for Sparse Attention in Long-Video Generation](http://arxiv.org/abs/2609.34814v1)
  <details><summary>📄 Abstract</summary>
  Long-video generation with diffusion transformers (DiTs) produces extremely long token sequences, making attention a dominant inference bottleneck. Dynamic sparse attention reduces computation, but its realized speedup remains limited because irregular query-row execution degrades L2 cache locality and increases HBM traffic. We present WaveAlign, a lightweight, cache-aware query-row reordering framework for dynamic sparse attention. WaveAlign formulates row ordering as an optimization problem an...
  </details>

- **2026-09-28** — Minchan Kang, Kyeonghye Park, Seungyeon Sa et al. — [Beyond Reconstruction Loss in Post-Training Quantization: Balanced Fitting for Large Vision-Language Models](http://arxiv.org/abs/2609.34765v1)
  <details><summary>📄 Abstract</summary>
  Post-training quantization (PTQ) enables efficient deployment of large vision-language models (LVLMs), but is typically calibrated on a small set while expected to generalize across diverse downstream tasks. Although recent PTQ methods for LVLMs incorporate sensitivity signals, they still minimize reconstruction loss with respect to the full-precision model, potentially over-preserving FP behavior and calibration-specific bias. Rather than treating quantization solely as an error to be minimized...
  </details>

- **2026-09-28** — Zhen Wang, Changpeng Wang, Zhe Liu et al. — [PanoVLN: Towards Effective Panoramic Vision-and-Language Navigation](http://arxiv.org/abs/2609.34759v1)
  <details><summary>📄 Abstract</summary>
  Recent vision-language models (VLMs) have advanced vision-and-language navigation (VLN), enabling models to predict navigation actions from visual observations and language instructions. In this work, we explore VLN with panoramic observations and introduce PanoVLN. The motivation is straightforward: more complete visual context should enable better-informed navigation decisions. For example, a panorama can reveal a passage outside a perspective camera's field of view, allowing the model to iden...
  </details>

- **2026-09-28** — Alexandre Declèves, Etienne Boursier, Nicolas Flammarion — [Statistical Benefits of Fine-Tuning from Pretrained Initialization in Diagonal Linear Networks](http://arxiv.org/abs/2609.34756v1)
  <details><summary>📄 Abstract</summary>
  Adapting pretrained models to downstream tasks with limited data has become a central paradigm in modern deep learning. Yet, despite its widespread practical success, how fine-tuning leverages information from pretraining remains poorly understood theoretically. We study fine-tuning from pretrained weights through the lens of sparse linear regression and two-layer diagonal linear networks. In our setting, pretraining provides information through the support (and signs) of the initialization pred...
  </details>

- **2026-09-28** — Thorsten Feldmann, Jack Jenkins, Jaime del Palacio Lirola — [Soft-Collinear Chiral Perturbation Theory for $B \to π$ form factors at large recoil](http://arxiv.org/abs/2609.34696v1)
  <details><summary>📄 Abstract</summary>
  We develop an effective hadronic theory for heavy-meson decays into energetic pions, organized by the approximate heavy-quark and chiral symmetries. The dynamical degrees of freedom of the theory consist of quasi-static heavy-meson fields coupled to soft and collinear pions, relevant for exclusive $B \to π$ transitions at large recoil energy ${E_π\simeq M_B/2}$. Our approach exploits the factorization of soft and collinear quarks in Soft-Collinear Effective Theory (SCET), leading to an emergent ...
  </details>

- **2026-09-28** — Moongyu Jeon, Dongjae Jeon, Bumjun Kim et al. — [Low-Confidence Remasking Traps Flexibility: Realizing Arbitrary-Order Potential for Diverse Rollouts in Diffusion LLMs](http://arxiv.org/abs/2609.34509v1)
  <details><summary>📄 Abstract</summary>
  Masked diffusion language models support arbitrary-order generation, suggesting a natural way to produce diverse outputs. However, recent work argues that this flexibility reduces diversity by delaying high-uncertainty tokens that can lead to different generation paths. We trace this diversity loss not to arbitrary-order generation itself, but largely to low-confidence remasking (LCR), a widely used decoding rule. At each step, LCR samples a token at every masked position but commits only the sa...
  </details>

- **2026-09-28** — Ayana Mussabayeva, Anuar Aimoldin, Olivier Oullier et al. — [PhysioTRACE: Provenance-Aware Stress Tests for Physiological Foundation Models](http://arxiv.org/abs/2609.34466v1)
  <details><summary>📄 Abstract</summary>
  Physiological foundation models encode how a signal was recorded alongside the physiology it reflects. When recording conditions are associated with diagnosis, this acquisition provenance can become a shortcut, yet the usual evidence, shifted transfer and provenance decodability, does not show whether a predictor uses it. We introduce PhysioTRACE, a four-axis behavioral audit for frozen encoders that separates what a probe can decode from what a fixed task head relies on. Recover scores how deco...
  </details>

- **2026-09-28** — Yekun Xu, Ante Wang, Jingyi Ren et al. — [When Words Fall Short: Iterative Synergy Between Verbalized Reasoning and Hidden Features for LLM Confidence Estimation](http://arxiv.org/abs/2609.34454v1)
  <details><summary>📄 Abstract</summary>
  Confidence estimation is crucial for developing trustworthy large language models (LLMs), with most methods following estimator-based or verbalization-based paradigms. While recent research increasingly focuses on improving verbalized self-reports of confidence, we challenge the prevailing view that this approach surpasses independent confidence estimators. Our empirical study shows that a dedicated confidence estimator can substantially outperform verbalized confidence, indicating that LLMs' in...
  </details>

- **2026-09-28** — Liang He, Sheng Wu, Haomiao Hao et al. — [ReproBench: Benchmarking LLM Agents on Reproducing Vulnerability From Scratch](http://arxiv.org/abs/2609.34450v1)
  <details><summary>📄 Abstract</summary>
  Large language model (LLM) agents are increasingly evaluated on cybersecurity tasks such as vulnerability reproduction, exploitation, and patching. However, existing cybersecurity benchmarks predominantly operate under a post-environment evaluation paradigm, i.e., handing the agent source code, a container, or an executable binary. This setup bypasses the critical environment reconstruction step, leaving a fundamental question for real-world vulnerability analysis: can an agent autonomously reco...
  </details>

- **2026-09-28** — Jialu Wang, Peizhi Niu, Haoteng Yin et al. — [Making LLMs Truly Forget: Deep Unlearning by Searching, Selecting, and Severing Knowledge Paths](http://arxiv.org/abs/2609.34442v1)
  <details><summary>📄 Abstract</summary>
  While an unlearned language model may no longer recall a fact directly, the fact often remains recoverable through multi-hop reasoning over related knowledge. Most existing unlearning techniques overlook this vulnerability, targeting facts in isolation while leaving their supporting knowledge intact. To achieve true forgetting, we propose a general deep unlearning framework compatible with existing unlearning algorithms. Our approach adaptively explores both explicit responses and latent interna...
  </details>

- **2026-09-28** — Yingjie Qi, Cenlin Duan, Yiou Wang et al. — [PolyCIM: Improving Data Reuse in Digital CIM Accelerators with Polyhedral-Based Compilation](http://arxiv.org/abs/2609.34351v1)
  <details><summary>📄 Abstract</summary>
  Digital Compute-in-Memory (CIM) presents a promising solution for accelerating deep neural networks (DNNs) through the integration of computational logic directly within memory arrays. However, mapping modern DNN operators to CIM accelerators often results in severe array underutilization, due to the strict data reuse constraints imposed by the rigid CIM array structure. We observe that data reuse in modern DNNs forms hyperplane structures often oriented along non-axial directions, rendering the...
  </details>

- **2026-09-28** — Weijun Luo, Kelvin Luu, Xinyi Liu et al. — [Maintaining Benchmarks Against Increasingly Capable Agents: Detection and Remediation of Unearned Passes](http://arxiv.org/abs/2609.34262v1)
  <details><summary>📄 Abstract</summary>
  Agentic benchmarks guide model selection and training. Yet an agent can pass a task without demonstrating the intended capability. Such outcomes constitute unearned passes; their proportion among all passes defines the integrity gap. As agents improve, benchmark surfaces that once seemed harmless can become exploitable, making benchmark validity an ongoing maintenance problem. We introduce a process-verification framework that audits passing trajectories, distinguishes evidenced reward hacking f...
  </details>

- **2026-09-28** — Qiyong Zhong, Mao Zheng, Mingyang Song et al. — [MAS-OPD: On-Policy Distillation for Multi-agent Systems](http://arxiv.org/abs/2609.34234v1)
  <details><summary>📄 Abstract</summary>
  Multi-agent systems (MAS) split a task across specialized roles and are promising on complex tasks, yet a prevailing approach relies on inference-time orchestration alone. General-purpose APIs are costly and hard to customize, while small models with role prompts rarely develop stable role competence or reliable collaboration, so post-training a MAS jointly is central. Most attempts use reinforcement learning, whose team-level reward leaves undetermined which step of which agent brought about th...
  </details>

- **2026-09-28** — Hong Zhang, Zhongjie Duan, Yingda Chen — [EntroPack: Fast and Accurate Entropy-Coded Weight Compression at Arbitrary Bitrates](http://arxiv.org/abs/2609.34185v1)
  <details><summary>📄 Abstract</summary>
  Weight compression helps large neural networks fit deployment memory budgets, but common fixed-width formats offer only coarse storage choices. Entropy coding supports finer rates, yet the achieved size depends on the quantized weight distribution and coding overhead. Exploiting this flexibility requires accurate rate selection and efficient weight reconstruction for inference. We present EntroPack, an entropy-coded weight compressor that supports arbitrary target bitrates without activation cal...
  </details>

- **2026-09-27** — Millend Roy, Soham Samal, Ivan Zelich et al. — [Structure-Adaptive Tree Field Integrators](http://arxiv.org/abs/2609.34025v1)
  <details><summary>📄 Abstract</summary>
  We present a new class of near-linear algorithms for efficiently integrating general tensor fields defined on trees with distance dependent kernels, the Structure-Adaptive Tree Field Integrators (STAD-TFIs). STAD-TFIs exploit the tree's underlying structure through decompositions built around path backbones and single vertex separators, and use two-dimensional fast Fourier transforms to compute interactions jointly. By exploiting this structural information, STAD-TFIs achieve more computationall...
  </details>

- **2026-09-27** — Ivan Kapelyukh, Yafei Hu, Ran Gong et al. — [Test-Time Spatial Reasoning for Robot Manipulation Using Generative Real-to-Sim](http://arxiv.org/abs/2609.33982v1)
  <details><summary>📄 Abstract</summary>
  Spatial reasoning is fundamental to general robot intelligence, as it enables robots to complete long-horizon tasks involving multi-object interaction. We introduce Simify, a training-free, test-time framework that performs explicit spatial reasoning via massively parallel physics simulation. From a single RGB-D image of a scene, Simify reconstructs simulation-ready assets leveraging 3D generative models and vision-language models. Then given a task specified by a reward function (e.g., build th...
  </details>

- **2026-09-27** — Ruosong Ye, Caiqi Zhang, Jiahao Li et al. — [Beyond Solo and Consistency: Vindicating Multi-Agent Debate via Conditional Progressive Pruning](http://arxiv.org/abs/2609.33974v1)
  <details><summary>📄 Abstract</summary>
  Large Language Model (LLM) based Multi-Agent Debate (MAD) is one of the most effective test time scaling techniques. Through multi-round communication, agents complement each other in knowledge and reasoning and solve tasks that no single member can solve. However, existing MAD frameworks fail to beat strong Single Agent and Consistency-based baselines under the same strict cost limit, which shakes the foundation of the MAD field. We propose Conditional Progressive Pruning (CPP), a lightweight p...
  </details>

- **2026-09-27** — Tongtong Liang, Siqi Kou, Ziqiao Xi et al. — [Residual-Stream Burden Shapes Representation Learning in Diffusion Transformers](http://arxiv.org/abs/2609.33895v1)
  <details><summary>📄 Abstract</summary>
  In diffusion-based generation, a neural network can be trained to predict the clean data, the noise, or the velocity from a noisy input. These prediction targets are interconvertible and describe the same generative process, yet plain Diffusion Transformers operating on large pixel patches succeed with clean prediction and fail with noise or velocity prediction. We argue that this asymmetry arises because noisy targets require the residual stream to preserve noise-dependent input variation throu...
  </details>

- **2026-09-27** — Xiangyang Wang, Bingxiang He, Zeyuan Liu et al. — [Diffusion Reward Models](http://arxiv.org/abs/2609.33803v1)
  <details><summary>📄 Abstract</summary>
  Reward models underpin the alignment of large language models, yet the dominant designs reduce each prompt--response pair to a point estimate or to a distribution from a fixed parametric family. This is at odds with human preference, which is inherently multimodal: the same response can be reasonably judged in many ways, and no single family covers all of them. To better fit this structure, we introduce DRM, a Diffusion Reward Model that recasts reward modeling as conditional density estimation ...
  </details>

- **2026-09-27** — Xiaonan Luo, Yue Huang, Kehan Guo et al. — [SecProbe: Adaptive Evaluation of Coding Agents on Cybersecurity Vulnerabilities](http://arxiv.org/abs/2609.33763v1)
  <details><summary>📄 Abstract</summary>
  Assessing cybersecurity vulnerability awareness in coding agents requires evaluations that reveal capability gaps and remain informative as models evolve. Static benchmarks offer fixed coverage and difficulty, while scarce vulnerable repositories and costly expert authoring limit their renewal at scale. We introduce SecProbe, a framework for adaptive evaluation that combines Item Response Theory (IRT) with on-demand synthesis of repository-scale vulnerability-repair tasks. From observed performa...
  </details>

- **2026-09-27** — Shengbin Yue, Hongru Wang, Siyuan Wang et al. — [ParaAgent: Reinforcing Parallel Acting in Open-World Tool Environments](http://arxiv.org/abs/2609.33618v1)
  <details><summary>📄 Abstract</summary>
  Language model agents are increasingly deployed in open-world tool environments, which require balancing exploring unknown capabilities and exploiting known ones. Existing methods face a performance-efficiency tradeoff: they either rigidly decouple exploration and execution or interleave them without coordination. We argue that the key lies not in whether to decouple or interleave them, but in how to coordinate them across granularities. We introduce ParaAct, a structured parallel-action loop th...
  </details>

- **2026-09-27** — Kaicheng Yang, Kaisen Yang, Chunyu Liu et al. — [JustQuant: You Don't Need Smoothing, SVD, or Rotation for 4-Bit Activation Quantization](http://arxiv.org/abs/2609.33601v1)
  <details><summary>📄 Abstract</summary>
  Recent generative models have become increasingly powerful, but their inference cost continues to grow. Model quantization offers a promising way to compress these models and accelerate inference. However, at 4 bits, activation quantization is substantially more challenging than weight quantization. Recent post-training quantization (PTQ) and quantization-aware training (QAT) methods have made progress in 4-bit activation quantization by introducing smoothing, SVD branches, rotations, mixed prec...
  </details>

- **2026-09-27** — Houssem Sifaou, Prabodh Katti, Bipin Rajendran et al. — [TerMeZO: Ternary Sparse Zeroth-Order Optimization for Fine-tuning BitNet Models at the Edge](http://arxiv.org/abs/2609.33548v1)
  <details><summary>📄 Abstract</summary>
  Fine-tuning anguage models (LLMs) with first-order optimizers requires a memory several times larger than that required for inference. Memory-efficient zeroth-order optimization (MeZO) sidesteps this cost by estimating gradients from forward passes only. However, for BitNet architectures, a family of LLMs with ternary {-1,0,1\} weights and 8-bit activations, fine-tuning requires updating full-precision latent weights, and thus the memory footprint of MeZO no longer matches that of inference. A p...
  </details>

- **2026-09-27** — Haoran Yan, Zhongjie Shi, Yuanzhe Xi et al. — [Neural Scaling Laws of Transformer Operator Network](http://arxiv.org/abs/2609.33533v1)
  <details><summary>📄 Abstract</summary>
  Transformers have emerged as powerful architectures for learning solution operators of physical systems. Empirically the prediction error has been observed to decrease when the data size and model size increase, suggesting neural scaling behavior. Yet a theoretical understanding of such scaling laws for transformer-based operator learning remains limited. In this work, we develop a theoretical framework for characterizing the approximation and generalization errors of transformer-based operator ...
  </details>

- **2026-09-27** — Jie Wang, Yanbo Sun, Zheng Yan et al. — [LLM4Trust: Exploring the Capabilities of Large Language Models for Trust Evaluation](http://arxiv.org/abs/2609.33521v1)
  <details><summary>📄 Abstract</summary>
  Trust evaluation plays a critical role in cybersecurity by supporting risk mitigation and decision-making. A variety of trust evaluation methods have been proposed, with learning-based approaches offering high accuracy and automation. However, they often require substantial ground truth, suffer from low training efficiency, lack support for basic trust properties, and provide limited explainability. Large Language Models (LLMs) offer a compelling alternative due to their strong zero-/few-shot re...
  </details>

- **2026-09-27** — Yu Liu, Zhuoting Han, Zexin Feng et al. — [Bare-Die Antiferromagnetic Computing](http://arxiv.org/abs/2609.33460v1)
  <details><summary>📄 Abstract</summary>
  Semiconductor electronic devices are increasingly constrained by fundamental quantum tunneling effects and charge-based mechanisms, which severely limit further miniaturization, write-speed scaling, and environmental robustness of silicon-based technologies. These limitations are particularly prohibitive for deep-space exploration, where extreme temperatures, ultra-strong magnetic fields, and intense radiation rapidly incapacitate conventional electronics without massive shielding. Here, we pres...
  </details>

- **2026-09-27** — Eilon Cohen, Ariel Fogel — [Weird Machine Compositors: Exploiting AI Orchestration at the Expression Layer](http://arxiv.org/abs/2609.33413v1)
  <details><summary>📄 Abstract</summary>
  Orchestration platforms secure user-provided expressions through enumerate and block sandboxing: AST rewriting, runtime property blocklists, template sandbox environments. We demonstrate that these sandboxes are weird machines whose instruction set is the underlying language specification, and that the enumerate and block approach is unfixable, following the same trajectory that led to the deprecation of past sandboxing technologies such as Java's SecurityManager and vm2.   We validate this clai...
  </details>

- **2026-09-27** — Jiayi He, Shengeng Tang, Sisi You et al. — [Naturalness-guided Manifold Flow Matching for Sign Language Production](http://arxiv.org/abs/2609.33339v1)
  <details><summary>📄 Abstract</summary>
  Sign Language Production (SLP) aims to generate sign motions from text. Conditional Flow Matching methods have achieved strong performance in SLP by constructing conditional paths that transform a source distribution into a target distribution. However, existing methods construct these paths via linear interpolation, whereas the rotational geometry of human joints confines valid joint rotations to a manifold embedded in Euclidean space. Consequently, linear interpolation between two sign motions...
  </details>

- **2026-09-27** — Liang Peng, Chenxiao Li, Libo Zhang et al. — [LoopTrack: A Simple Baseline for Parameter-Efficient Transformer Tracking](http://arxiv.org/abs/2609.33306v1)
  <details><summary>📄 Abstract</summary>
  Current Transformer-based tracking methods typically stack multiple Transformer blocks with separate parameters to model interactions between the target template and the search region for target localization. These trackers often incur substantial parameter overhead from stacked blocks, making their deployment on resource-limited devices difficult. To address this, we propose a parameter-efficient Transformer tracking framework, dubbed LoopTrack, which repeatedly applies a set of Transformer blo...
  </details>

- **2026-09-27** — Jianguo Huang, Lipeng Wan, Yanchen Deng et al. — [Hesitation-Aware On-Policy Distillation for Diffusion Language Models](http://arxiv.org/abs/2609.33301v1)
  <details><summary>📄 Abstract</summary>
  Diffusion large language models (dLLMs) generate text by iterative unmasking. At each denoising step, a dLLM proposes a token at every masked position, but the decoder commits only a confident subset of these proposals. Trace-based on-policy distillation (TOPD) builds on this process by matching the student to a stronger teacher, yet only at the committed positions. We argue that this discards much of the useful signal, which resides in the uncommitted proposals, where the student has made a pre...
  </details>

- **2026-09-27** — Dat Phi Van, Ngo Vu Minh, Tuc Nguyen et al. — [Orthogonal Witness Control for Muon Optimization via Sigmoid Spectral Reshaping](http://arxiv.org/abs/2609.33194v1)
  <details><summary>📄 Abstract</summary>
  Matrix-valued optimizers such as Muon exploit the spectral structure of neural network updates through Newton--Schulz orthogonalization, but their near-flattening of the singular spectrum discards relative magnitude information across gradient modes. We introduce \emph{Soren} (\textbf{S}pectral \textbf{O}rthogonal \textbf{Re}shapi\textbf{n}g), a matrix-valued optimizer that preserves the singular subspaces of the gradient while applying a bounded, monotone sigmoid transformation to its singular ...
  </details>

- **2026-09-27** — Di Zhang, Zhangpeng Gong, Jiashuai Liu et al. — [Can Protein-Derived Knowledge Improve Pathology Foundation Models?](http://arxiv.org/abs/2609.33178v1)
  <details><summary>📄 Abstract</summary>
  Molecularly guided pathology foundation models (PFMs) exploit transcriptomic or proteomic information to enrich whole-slide image (WSI) representations, yet effectively leveraging large standalone molecular corpora remains challenging. First, existing molecular foundation models encode protein sequences or single-cell states, not the patient-level bulk expression profiles paired with WSIs. Second, because cross-modal supervision is restricted to paired WSI-omics samples, knowledge from standalon...
  </details>

- **2026-09-27** — Jia Liang, Xi Jin, Liangming Pan — [Beyond the Training Horizon: Mechanisms and Limits of Length Generalization in Looped Transformers](http://arxiv.org/abs/2609.33144v1)
  <details><summary>📄 Abstract</summary>
  Looped Transformers can generalize to reasoning chains longer than those encountered during training, but the computations enabling this behavior and limiting its extent remain unclear. We mechanistically compare two looped-Transformer configurations, which we call the Matched-Recurrence Looped Transformer (MR-Loop) and Decoupled-Recurrence Looped Transformer (DR-Loop), reflecting their respective recurrence-training schemes. We evaluate polynomial iteration, finite-state composition, and knowle...
  </details>

- **2026-09-27** — Lang Cao, Binghang Lu, Yuhao Shen et al. — [MedRouter: Demystifying Knowledge Differences Across Medical LLMs for Routing-Based Reasoning](http://arxiv.org/abs/2609.33119v1)
  <details><summary>📄 Abstract</summary>
  Medical question answering spans diverse specialties and modalities, and individual medical large language models (LLMs) exhibit distinct strengths across tasks and domains. This heterogeneity suggests that combining specialists may enable broader coverage of medical questions than relying on any single model. However, existing LLM routing methods primarily seek to balance answer quality and inference cost, leaving open how to exploit differences in specialist competence to improve medical reaso...
  </details>

- **2026-09-27** — Mattias Akke, Soojung Yang, Jurgis Ruža et al. — [LLM sequential decision making under uncertainty in biochemical domains](http://arxiv.org/abs/2609.33061v1)
  <details><summary>📄 Abstract</summary>
  Large language models (LLMs) are increasingly used to drive scientific discovery. Understanding how LLMs make decisions from new data and memory of the literature is vital before trusting them to design experiments under tight experimental budgets. However, their decision strategies are invisible in the current performance scores used to evaluate research agents. Here, we benchmark five frontier LLMs in a Bayesian Optimization setting against published statistical baselines on seven combinatoria...
  </details>

- **2026-09-27** — Bumgeun Park, Donghwan Lee — [Is Online Interaction Necessary for Recovery? A Minimalist Approach to Robust Planning via Perturbation](http://arxiv.org/abs/2609.33049v1)
  <details><summary>📄 Abstract</summary>
  Behavior cloning (BC) is vulnerable to covariate shift during closed-loop execution, where small prediction or execution errors can drive the robot toward states poorly covered by the demonstration data. We focus on action-sequence planning, where a policy predicts a finite-horizon sequence of actions as a reference trajectory for robot execution. Existing approaches to covariate shift often rely on collecting additional corrective demonstrations, requiring further environment interaction and ac...
  </details>

- **2026-09-26** — Christina M. Ceballos, Matthew S. Mizuhara, Mykhailo Potomkin et al. — [Active matter within flexible boundaries: a novel experimental approach with T. aceti nematodes](http://arxiv.org/abs/2609.32945v1)
  <details><summary>📄 Abstract</summary>
  We experimentally explore the collective behavior of the nematode T. Aceti inside flexible boundaries showing the emergence of previously unreported states. These nematodes have been previously shown to be able to synchronize their body oscillations in a favorable condition of confined space. In this collective state, they are able to exert a strong pushing force which we exploit to study how their collective motion could deform a pliable boundary. Using a novel experimental technique, we were a...
  </details>

- **2026-09-26** — Constantino Álvarez Casado, Nhi Nguyen, Mohammad Rakibur Rahman et al. — [Phenomenon-Graph JEPA: Label-Efficient Representation Learning for Contactless Cardiorespiratory Sensing](http://arxiv.org/abs/2609.32928v1)
  <details><summary>📄 Abstract</summary>
  Millimeter-wave (mmWave) radar and RGB-D cameras can record cardiac and respiratory waveforms continuously and without contact, but labeled recordings remain scarce because every label requires a supervised acquisition session. Self-supervised pretraining can exploit the unlabeled signals, yet contrastive methods depend on signal transformations and negative pairs whose validity is uncertain for cardiorespiratory data, where time warping changes breathing rate and distant windows can share the s...
  </details>

- **2026-09-26** — Maciej Cichoń, Bartłomiej Dmitruk — [A Function-Level Vulnerability Score Measures Flag Rate More Than the Model: Protocol Effects on Paired Benchmarks](http://arxiv.org/abs/2609.32890v1)
  <details><summary>📄 Abstract</summary>
  Language models are increasingly evaluated as vulnerability detectors, and scores reported for similar models differ widely between papers. We measured how much of that difference evaluation protocol accounts for, with model outputs held fixed. In a paired test, a model must flag a vulnerable function and clear its version after a fixing commit. Three choices that published evaluations make differently were varied one at a time: metric, verdict extraction and output budget. Seven frontier and la...
  </details>

- **2026-09-26** — Samyak Jha, Harshvardhan Saini, Yizhen Liao et al. — [Understanding and Exploiting Anisotropy in Post-Training](http://arxiv.org/abs/2609.32792v1)
  <details><summary>📄 Abstract</summary>
  LLM post-training combines supervised fine-tuning (SFT), a mode-covering forward-KL objective, with reinforcement learning (RL), a mode-seeking reverse-KL objective. Frequency-weighted likelihood training leaves a well-known signature: \emph{anisotropy}, in which a few residual channels carry disproportionately large activations. Anisotropy is widely documented and usually treated as a defect, yet its function and its interaction with post-training remain unclear. We first analyze it. A label-fr...
  </details>

- **2026-09-26** — Manuel Tsoukatos, Hayden Jananthan, Jeremy Kepner — [Agentic Network Traffic Monitoring](http://arxiv.org/abs/2609.32778v1)
  <details><summary>📄 Abstract</summary>
  As the use of agentic artificial intelligence increases in nearly every industry, there exists a widening attack surface. It is necessary to monitor agents to ensure that agents are acting in a way that is aligned with the users intent. Auditing an agent's network traffic provides a clear record of the agent interactions. This work presents a novel approach to monitoring the network traffic of agentic systems using complex valued hypersparse traffic matrices by integrating DBOS (DataBase OS), th...
  </details>

- **2026-09-26** — Yi Ding, Lan Wei, Xuehu Zhu et al. — [Reference-Null Calibrated Thresholds for E-Processes with Applications to Conformal Martingales](http://arxiv.org/abs/2609.32678v1)
  <details><summary>📄 Abstract</summary>
  E-processes provide a flexible framework for anytime-valid inference, with the conventional rejection boundary $1/α$ typically justified by Ville's inequality. Such a boundary is universal but can be conservative, as it does not exploit additional information about the null distribution. We propose a reference-null calibration framework that uses independent null samples to construct sharper rejection thresholds while preserving type-I error control. To study the statistical gain from sharper th...
  </details>

- **2026-09-26** — Xianpeng Shang, Canbin Huang, Jiang Li et al. — [Distance-KV: Exploiting Relative Distance for Efficient Long-Context Inference](http://arxiv.org/abs/2609.32663v1)
  <details><summary>📄 Abstract</summary>
  The memory usage and decoding latency of LLM inference grow rapidly with context length. To reduce these costs, key-value (KV) cache compression methods selectively retain cached states based on token importance or differences in attention patterns across heads. However, we discover that retrieval capability varies substantially with relative distance, even within the same attention head. To exploit this structure, we introduce Distance-KV, which learns a static KV retention pattern over the joi...
  </details>

- **2026-09-26** — Yikun Li, Jinfeng Jiang, Yuheng Yieh et al. — [VulContextBench: A Benchmark for Security Context Retrieval in Coding Agents](http://arxiv.org/abs/2609.32601v1)
  <details><summary>📄 Abstract</summary>
  Vulnerability-detection benchmarks score the verdict an agent reaches, not the evidence it gathered. A model that recalls a CVE from pretraining therefore scores the same as one that traced the data flow. We study a task where this difference matters, deciding whether a commit introduces a vulnerability. Instead of scoring the verdict, we score whether the agent retrieved the code its conclusion depends on. We present VulContextBench, a benchmark of 111 vulnerability-introducing commits (VICs) a...
  </details>

- **2026-09-26** — Qi Chen, Fushuo Huo, Hangli Shen et al. — [CyberClear: A Benchmark for LLM Agent Systems on APT Attack Chain Provenance](http://arxiv.org/abs/2609.32424v1)
  <details><summary>📄 Abstract</summary>
  Large language model agents have demonstrated promising capabilities in cybersecurity tasks, yet their ability to reconstruct complete Advanced Persistent Threat attack campaigns from complex security logs remains largely unexplored. Existing cybersecurity benchmarks for agents mainly focus on vulnerability discovery, exploitation, and security analysis tasks, leaving the evaluation of attack chain provenance under realistic security logs insufficiently studied. To address this gap, we introduce...
  </details>

- **2026-09-26** — Jian Tang, Jiawei Fan, Qiannan Zhou et al. — [RefAdapt-DiT: Adaptive Joint Attention for Reference-Conditioned Diffusion Transformers](http://arxiv.org/abs/2609.32415v1)
  <details><summary>📄 Abstract</summary>
  Diffusion Transformers (DiTs) have become the standard backbone for high-quality generative modeling, yet deploying them in conditional generation tasks remains computationally prohibitive because bidirectional joint attention repeatedly processes large reference streams. While existing optimization schemes mitigate generic temporal redundancy, they typically rely on coarse-grained static reuse and overlook the distinct dynamics of references and targets. Specifically, we observe that reference ...
  </details>

- **2026-09-26** — Sourabrata Mukherjee, Sunayana Sitaram — [Opening LLM Judges: Recovering Preference Signals Beyond the Final Verdict](http://arxiv.org/abs/2609.32407v1)
  <details><summary>📄 Abstract</summary>
  LLM judges are widely used to evaluate model outputs, but their verdicts can be unreliable: a judge may favor the worse answer for its position, length, or other surface features. When a judge is wrong, is the information needed to judge correctly absent from the model, or present in its internal representations but not reflected in the output? We study this across 64 open-weight evaluators and 14 datasets, including causal interventions on 41 judges (editing activations mid-run to see whether t...
  </details>

- **2026-09-26** — Zicheng Zhao, Linhao Luo, Junnan Dong et al. — [HyperReCo: Retrieving and Connecting Evidence with Hypergraph Neural Networks for LLM Multi-hop Reasoning](http://arxiv.org/abs/2609.32327v1)
  <details><summary>📄 Abstract</summary>
  Large language models (LLMs) have shown strong capabilities, with retrieval-augmented generation (RAG) supporting complex multi-hop reasoning by retrieving evidence distributed across documents. Graph-based approaches exploit connections among evidence, and hypergraph-based retrieval further preserves higher-order entity associations within documents and connects documents through shared entities. However, existing hypergraph retrievers often rely on predefined structural expansion or diffusion,...
  </details>


### 📂 defense
*防御与防护方法 / Defense & Protection Methods* — 46 papers

- **2026-09-28** — Shidan Javaheri, Alexander Panfilov, Oliver Britton et al. — [Distillation Defenses Easily Break After Reinforcement Learning](http://arxiv.org/abs/2609.35699v1)
  <details><summary>📄 Abstract</summary>
  Distillation attacks copy the reasoning capabilities of closed-source large language models, allowing bad actors to replicate state-of-the-art performance at low cost. Attackers systematically collect a large volume of frontier model reasoning traces and then train (i.e., "distill") their own models on these traces. Existing defenses against distillation attacks are typically evaluated immediately after distillation, implicitly assuming attackers do not train their models any further. In this pa...
  </details>

- **2026-09-28** — Saswat Das, Parvati Viswanathan, Daniel Donnelly et al. — [SEABench: Benchmarking Endogenous Misalignment In Self-Evolving Agents](http://arxiv.org/abs/2609.35596v1)
  <details><summary>📄 Abstract</summary>
  Self-evolving LLM agents have gained prominence for their ability to improve after deployment by modifying their harness, including their controller instructions, memory management protocols, and reusable tools and skills, in response to user and environment feedback. However, locally useful updates may persist into later tasks where they produce unsafe behavior, even without direct adversarial influence. To study this risk, we introduce SEABench, a benchmark for studying endogenous misalignment...
  </details>

- **2026-09-28** — Rong Pan, Yili Hong, Min Xie — [Reliability Engineering for AI Systems: Challenges, Methods, and Directions](http://arxiv.org/abs/2609.35316v1)
  <details><summary>📄 Abstract</summary>
  AI reliability concerns whether an AI system performs its intended function dependably over a stated period and under stated operating conditions, with stated evidence. As these systems become more autonomous, that function includes more than a correct output. Retrieval, memory, tool use, permissions, human oversight, and interactions among systems must operate consistently and safely, and, for generative systems, so must the reasoning process that produces the output. Average benchmark accuracy...
  </details>

- **2026-09-28** — Homayoun Maleki, Nekane Sainz, Jon Legarda et al. — [Sustained Participation as a Security Resource: The Bounded Participation Channel](http://arxiv.org/abs/2609.35300v1)
  <details><summary>📄 Abstract</summary>
  Can sustained, per-identity participation be engineered into a security resource? Most anti-Sybil defenses price identity creation rather than identity survival. Once admitted, an adversary may sustain many identities without paying a recurring cost. We introduce the Bounded Participation Channel (BPC), a formal primitive for repeatedly verifying participation window by window. BPC issues fresh, identity-bound challenges under a strict deadline and enforces four structural properties: identity b...
  </details>

- **2026-09-28** — Kasra Arabi, Nir Weinberger, Micah Goldblum et al. — [TANGO: Watermarking Masked Diffusion Language Models in Token Pairs](http://arxiv.org/abs/2609.35224v1)
  <details><summary>📄 Abstract</summary>
  Masked-diffusion language models fill in masked positions in parallel and in no fixed order. Most practical text watermarks assume left-to-right generation. They key each token to the tokens before it, and in a diffusion model those tokens may still be masked. A fixed green list needs no such context, but it favors the same tokens at every position, so these tokens appear more often in watermarked text. An attacker who compares token frequencies in watermarked and unwatermarked text can recover ...
  </details>

- **2026-09-28** — Qiankun Li, Yuechen Zhang, Bowen Chen et al. — [Still There, No Longer Seen: Exposing Compression-Induced Risk in Large Vision-Language Models](http://arxiv.org/abs/2609.35002v1)
  <details><summary>📄 Abstract</summary>
  Visual token compression reduces the inference cost of Large Vision-Language Models (LVLMs). However, aggregate robustness measures do not reveal whether a particular adversarial failure is induced by compression or inherited from the underlying model. We define a compression-specific failure (CSF) as an adversarial input that remains correct under full-token inference but fails after compression, casting compression-induced risk as a paired failure attribution problem. Within a controlled diagn...
  </details>

- **2026-09-28** — Yiqing Feng, Haozhe Feng, Shunan Shang et al. — [AuxMark: Defending Against Unauthorized Agent Distillation via Auxiliary Behavioral Watermarking](http://arxiv.org/abs/2609.34597v1)
  <details><summary>📄 Abstract</summary>
  Large language model agents can acquire complex capabilities through multi-step interaction and tool use, but their trajectories can also be illegally collected to dis- till student agents. However, existing watermarking methods either do not fit the structured and interactive nature of agent environments or lack reliable effective- ness across tasks and model architectures. We introduce AuxMark, a behavioral watermarking framework for tracing unauthorized agent distillation. AuxMark dynamically...
  </details>

- **2026-09-28** — Chanhee Park, Jeongho Yoon, Sungbin Han et al. — [AgentHop: A Diagnostic Benchmark for Agentic Multi-Hop Scientific Question Answering](http://arxiv.org/abs/2609.34428v1)
  <details><summary>📄 Abstract</summary>
  Agentic tasks require a large language model to interact with the world, navigating information and gathering evidence across multiple steps with restricted resources. Due to this complexity, agentic task failures arise from various sources, and pinpointing these failure causes is essential to diagnose and improve agentic systems. Existing benchmarks, however, tend to focus on a single leaderboard score, leaving the underlying failure modes opaque. To fill this gap, we introduce AgentHop, a diag...
  </details>

- **2026-09-28** — Ding Jia, Wei Liu, Xianglong Du et al. — [PROACT-Agent: Progressive Runtime Oversight and Active Circuit-breaking for Real-Time Safety](http://arxiv.org/abs/2609.34415v1)
  <details><summary>📄 Abstract</summary>
  The transition from Large Language Models (LLMs) to agents shifts safety stakes from toxic text to irreversible environmental harm. While current defenses remain largely retrospective, proactive runtime intervention is bottlenecked by the lack of large-scale, causally-consistent data. We propose PROACT-Agent, a framework for synthesizing high-fidelity trajectories to enable real-time guardrails. We identify a critical "safety drift" in prior benchmarks, where lenient annotation paradigms fail to...
  </details>

- **2026-09-28** — Chaoqian Ouyang, Ling Yue, Libin Zheng et al. — [TokenCast: Forecasting Token Consumption During LLM Agent Execution](http://arxiv.org/abs/2609.35760v1)
  <details><summary>📄 Abstract</summary>
  When a large language model (LLM) agent executes the same task, token consumption can vary by over an order of magnitude across runs. The agent chooses its next steps based on tool feedback and intermediate results, while the growing context steadily inflates the input size of every subsequent call. The total consumption of a task is therefore hard to predict before execution and the prediction must be revised as the run unfolds. In this paper, we propose TokenCast, which learns a composable cos...
  </details>

- **2026-09-28** — Tianyao Shi, Xipeng Shen, Yi Ding — [Beyond Energy: When Sustainability Dimensions Reshape LLM Serving Decisions](http://arxiv.org/abs/2609.35569v1)
  <details><summary>📄 Abstract</summary>
  Large language model (LLM) serving has environmental impacts across energy consumption, carbon emission, water consumption, and biodiversity loss. Yet these dimensions are largely evaluated in isolation, leaving it unclear when and how they lead to different optimization decisions. We present PRISM, a unified framework for characterizing and optimizing LLM serving across energy, carbon, water, and biodiversity impacts. Our analysis reveals a fundamental distinction: computing configurations dete...
  </details>

- **2026-09-28** — Shobhan Roy — [The Compiler May Read It, the Agent May Not: Keeping Part of a Research Code Away from a Coding Agent](http://arxiv.org/abs/2609.35557v1)
  <details><summary>📄 Abstract</summary>
  The compiler must read modules a physics-based solver cannot build without; the coding agent must not read that intellectual property. The harness does not ship that rule. We classified fifteen read routes against a container, permission rules and a sandbox. None of the three can tell which program is reading.
  </details>

- **2026-09-28** — Yage Zhang, Yukun Jiang, Yang Zhang — ["Nothing to See Here'': Unintended Disclosure through Revision Traces of LLM Deliverables](http://arxiv.org/abs/2609.35408v1)
  <details><summary>📄 Abstract</summary>
  Large language model (LLM) assistants increasingly help users draft content for third-party recipients. During private drafting, the user or the model may introduce an item and later remove or replace it. The model may remove the item from the intended content but reveal it again when stating the edit. We call such statements revision traces. For example, after a user removes the password before sharing a configuration file, the model may delete it but leave a comment saying, "Removed the passwo...
  </details>

- **2026-09-28** — Jinnan Guo, Hao Mark Chen, Kapil Vaswani et al. — [Planarian: Managing Agent State with Statepoints](http://arxiv.org/abs/2609.35366v1)
  <details><summary>📄 Abstract</summary>
  LLM agents solve complex tasks by iteratively changing files, invoking local tools, and interacting with remote services, which modifies state across their local environment and remote services. Today, agents and users must manage these changes explicitly, whether reverting exploratory actions or recovering from erroneous ones. Doing so safely requires coordinated actions, yet current agent harnesses lack unified abstractions and mechanisms for managing local and remote state consistently and ef...
  </details>

- **2026-09-28** — Jiahong Zou, Xiangkun Sun, Lingkai Kong et al. — [A mechanistic study of language model introspection](http://arxiv.org/abs/2609.35108v1)
  <details><summary>📄 Abstract</summary>
  Large language models (LLMs) can sometimes report perturbations to their internal activations---even when the input provides no evidence that an intervention occurred. How do models detect and localize such internal changes? We study this question using a controlled task that keeps the input text fixed. We either inject a concept vector into the hidden state at one of ten token positions or apply no intervention. The model is asked to identify the perturbed position or report that no interventio...
  </details>

- **2026-09-28** — Lucio La Cava, Andrea Tagarelli — [Echoes of Deeds: Moral History Can Shape and Steer LLM Behavioral Choices](http://arxiv.org/abs/2609.35070v1)
  <details><summary>📄 Abstract</summary>
  Evaluations of Large Language Models (LLMs) morality typically consider decisions in isolation, thus overlooking whether an individual's unrelated prior conduct influences the model's subsequent choices. This leaves open the question of whether, and to what extent, moral history shapes LLM decisional behaviors. Prior work on human moral decision-making shows that past behavior can influence subsequent moral choices. Building on this observation, we investigate whether analogous effects emerge in...
  </details>

- **2026-09-28** — Ruozhao Yang, Mingfei Cheng, Xiaofei Xie — [Before Acting, Change the State: Prospective State Intervention for Web Agents under Deceptive Interfaces](http://arxiv.org/abs/2609.34974v1)
  <details><summary>📄 Abstract</summary>
  LLM-based Web agents can autonomously complete user tasks, yet deceptive interfaces can steer them toward outcomes that conflict with users' interests. Existing defenses primarily intervene on agent behavior through blocking, guidance, or replanning. We identify a distinct failure mode: a task-valid action can still realize an unauthorized consequence because of the current Web state. This motivates treating task-relevant Web state itself as a runtime control target. We introduce Veer, an agent-...
  </details>

- **2026-09-28** — Andrei Aldea, Dumitru-Bogdan Prelipcean — [Verifying Graceful Degradation in a Distributed Malware-Detection System with SPIN](http://arxiv.org/abs/2609.34873v1)
  <details><summary>📄 Abstract</summary>
  Modern endpoint malware detection is distributed: a lightweight agent on each endpoint collects features from a scanned file or process, sends them to a remote server for analysis, and then enforces the returned verdict locally by blocking, quarantining, or disinfecting. Because the endpoint acts on the verdict, the distributed machinery surrounding detection must never turn a transient server failure into a wrong action. We present a formal model, in Promela, of the endpoint decision pipeline o...
  </details>

- **2026-09-28** — Zhijie Deng, Ling Li, Junhao Ji et al. — [AUV-Bench: Aesthetic Understanding and Generation Evaluation for User Interfaces](http://arxiv.org/abs/2609.34854v1)
  <details><summary>📄 Abstract</summary>
  Multimodal foundation models are increasingly used for evaluating and generating user interfaces (UIs), often producing seemingly reasonable aesthetic judgments and visually plausible pages. However, under professional design scrutiny, their behavior can differ substantially from that of human designers. In professional design practice, designers rely on a systematic set of aesthetic principles that consistently guide judgment, diagnosis, repair, and creation. A coherent aesthetic capability sho...
  </details>

- **2026-09-28** — Tianyi Guan, Jianhui Chen, Liangming Pan — [When Do Model Internals Help? Exploring the Role of Representation Engineering in LLM Safety](http://arxiv.org/abs/2609.34771v1)
  <details><summary>📄 Abstract</summary>
  Reliable AI safeguards require both control mechanisms that reduce unsafe behavior and monitoring mechanisms that detect safety risks during model interactions. Established behavioral safeguards include alignment methods that optimize model outputs and text monitors that assess interaction text. Representation engineering instead reads or modifies internal model states, but the relative strengths of these approaches remain unclear because they are often evaluated under different settings. We pre...
  </details>

- **2026-09-28** — Muhammad Owais, Ehtesham Iqbal, Samee Ullah Khan et al. — [Recent Advances in Agentic Agri-Robotic Phenotyping: A Perspective Review from Fragmented Multimodal Sensing to Unified PhenoAgent Intelligence](http://arxiv.org/abs/2609.34567v1)
  <details><summary>📄 Abstract</summary>
  This review examines the evolution of plant phenotyping from conventional manual trait measurement to high-throughput, robotic, and artificial intelligence-driven crop monitoring. Despite significant advances in imaging, autonomous platforms, multimodal sensing, and deep learning, current phenotyping systems remain fragmented across sensing modalities, crop traits, growth stages, environments, and management objectives. We therefore frame phenotyping as an integrated \emph{seed-soil-plant-enviro...
  </details>

- **2026-09-28** — Zhang Ruiyang, Ou Jinpeng, Xie Yifan et al. — [Marathoner: Ultra-Long-Horizon Autonomous Intelligence](http://arxiv.org/abs/2609.34378v1)
  <details><summary>📄 Abstract</summary>
  Humans naturally possess the ability to work persistently toward long-term goals. Given a challenging task, humans can continuously work for months or even years to accomplish a specific objective. In this paper, we propose Marathoner, an autonomous agentic model possessing the ability of ultra-long-horizon execution. Specifically, we propose a comprehensive post-training pipeline to instill this critical capability into base model. For Ultra-Long-Horizon Task Synthesis, we leverage major releas...
  </details>

- **2026-09-28** — Zhengding Luo, Jinyang Wu, Haozhe Ma et al. — [SAIL: Spatial Audio Intelligence with Large Language Models via Disentangled Acoustic-Spatial Encoding and Dual-Stream Q-Former](http://arxiv.org/abs/2609.34347v1)
  <details><summary>📄 Abstract</summary>
  Spatial audio large language models (LLMs) enable embodied agents, wearable assistants, and immersive systems to recognize sound events, localize sources, and reason about their spatial relationships. However, existing spatial audio LLMs often rely on early fusion of acoustic and spatial features and source-agnostic token representations. These designs make it difficult to preserve the correspondence between individual sound events and their spatial attributes, particularly in multi-source scene...
  </details>

- **2026-09-28** — Shaoqing Zhang, Kehai Chen, Xuefeng Bai et al. — [GUITAR: Structured Failure Diagnosis of GUI Agents via State Transitions](http://arxiv.org/abs/2609.34113v1)
  <details><summary>📄 Abstract</summary>
  Understanding where and why Graphical User Interface (GUI) agents fail is essential for building more reliable systems, yet current evaluation relies on step accuracy, a metric that treats each screen independently and overlooks the underlying structure of GUI environments. This leads to two critical blind spots: (1) functionally equivalent screens are evaluated in isolation, obscuring systematic failure patterns across shared screens; and (2) the long-tailed GUI distribution renders failures on...
  </details>

- **2026-09-28** — Chia-Ling Chen, Yu-Ting Ta, Jian-Yu Jiang-Lin et al. — [Look Before You Judge: Training-Free Region Mining for Grounded and Explainable Deepfake Detection](http://arxiv.org/abs/2609.35536v1)
  <details><summary>📄 Abstract</summary>
  Multimodal large language models (MLLMs) can explain deepfake verdicts in natural language, but such explanations are not necessarily visually grounded in the visual evidence underlying the prediction. A model may describe plausible artifacts inferred from language priors rather than from image evidence. Existing grounding methods improve visual reliance through decoding or attention interventions, but they generally strengthen grounding over the entire image, making them ill-suited for forensic...
  </details>

- **2026-09-28** — Tanguy Dieudonné, Jack B. Jedlicki, Heng Yang — [Where Memory Belongs: Ledger, an Object Ledger for Memory-Augmented VLAs](http://arxiv.org/abs/2609.34554v1)
  <details><summary>📄 Abstract</summary>
  Memory is essential for long-horizon, partially observed robotic manipulation: a robot must remember which object was placed in a drawer, whose cup it moved, or how many action cycles have elapsed. Recent vision-language-action (VLA) models embed memory directly inside the policy, but benchmarks show no single in-policy mechanism covers all spatio-temporal dimensions, trailing oracle methods by a wide margin. We argue that memory type dictates where memory should reside: short-term perceptual me...
  </details>

- **2026-09-28** — Xu Wang, Yifan Yang, TingHao YU et al. — [Beyond Token Scale: Chunk-Level Sparse Autoencoders for Reliable Semantic Feature Discovery](http://arxiv.org/abs/2609.35521v1)
  <details><summary>📄 Abstract</summary>
  Sparse autoencoders (SAEs) expose features that help us understand and steer language models, but faithful reconstruction does not guarantee informative concepts. Token-level objectives reward lexical and formatting details alongside semantic content, all competing for a limited sparse budget. We introduce a family of chunk-level SAEs that encode mean-pooled activations over chunks, each a contiguous span of tokens: Mean-Chunk reconstructs the observed chunk, Cross-Chunk predicts an independentl...
  </details>

- **2026-09-28** — Nowshin Amin, Nafisa Tabassum Oyshi, Tahmid Abrar Zidan et al. — [Automated Species Identification in Camera Trap Images for Wildlife Conservation](http://arxiv.org/abs/2609.35420v1)
  <details><summary>📄 Abstract</summary>
  Wildlife conservation involves protecting, preserving, and managing wildlife species and their habitats. With today's rapid pace of human development, climate change, and other unsustainable practices, the need for wildlife conservation has heightened. Despite significant progress in species identification using deep-learning models, significant challenges still remain in effectively detecting small animals in low-contrast trap images due to limited feature extraction capabilities. This thesis p...
  </details>

- **2026-09-28** — Zhaohan Zhang, Junjie Liu, Chengzhengxu Li et al. — [When Confidence Rises Too Early: Detecting Shortcut Reasoning via Premature Answer Commitment](http://arxiv.org/abs/2609.35074v1)
  <details><summary>📄 Abstract</summary>
  The reasoning trajectory of a Large Language Model (LLM) is often treated as a verbalized description of its internal reasoning. However, such trajectories can be unfaithful: a model may rely on shortcuts to reach an answer and then post-rationalize the decision with a seemingly coherent chain of thought. Detecting this shortcut reasoning is challenging because existing monitors and verifiers mainly inspect textual traces or final outcomes, rather than how the model's belief in its answer develo...
  </details>

- **2026-09-28** — Mengyang Zhao, Zhuolin He, Haiyang Yu et al. — [VD-DeepStack: Bridging Visual Comparison and Language Reasoning for Few-Shot Anomaly Detection](http://arxiv.org/abs/2609.34949v1)
  <details><summary>📄 Abstract</summary>
  Few-shot visual anomaly detection is fundamentally a visual comparison task, requiring fine-grained inspection of a query against normal references. Many recent methods based on large vision-language models (LVLMs) emphasize comparative reasoning through language chain-of-thought. Yet discrete, abstract descriptions may underrepresent dense, fine-grained visual differences, leaving a gap between visual comparison and its expression in language. To address this gap, we propose Visual Difference D...
  </details>

- **2026-09-28** — Haiyue Yuan, Jie Guo, Weidong Qiu et al. — [Using LLMs to Detect LLM-Generated Texts: A Cross-Generation Analysis](http://arxiv.org/abs/2609.34691v1)
  <details><summary>📄 Abstract</summary>
  Automated detection of LLM-generated texts (LGTs) is critical, yet dedicated detectors often struggle to generalize across domains and models. While general-purpose LLMs offer flexible zero-shot authorship classification with explanatory rationale, their detection behavior, especially regarding self-detection versus cross-detection across model generations, remains poorly understood. We systematically evaluate 15 LLMs spanning three model generations as both generators and detectors. Using a ben...
  </details>

- **2026-09-28** — Yuanzhe Jia — [In-game Toxic Detection: Bi-directional Representations with Attention Residuals](http://arxiv.org/abs/2609.34584v1)
  <details><summary>📄 Abstract</summary>
  In-game toxic language has emerged as a critical concern in the gaming industry and community. While several frameworks and models for online game toxicity analysis have been proposed, detecting toxicity in player chat utterances remains a formidable challenge: stemming not only from the extremely short length of such utterances but also from the heavy reliance on game slang, abbreviations, and domain-specific jargon, which generic language models are poorly suited to recognize. This paper prese...
  </details>

- **2026-09-28** — Ziyun Cui, Wen Wu, Chuan Shi et al. — [Explainable and Generalisable LLM-based Cognitive Decline Detection with Spontaneous Speech](http://arxiv.org/abs/2609.34217v1)
  <details><summary>📄 Abstract</summary>
  Alzheimer's disease (AD) and mild cognitive impairment (MCI), which may precede AD, manifest early through subtle linguistic and acoustic alterations. Traditional diagnostics, however, are often resource-intensive and lack scalability for mass screening. To address these challenges, we introduce a novel bilingual speech large language model framework for automated, explainable cognitive screening. Unlike conventional pipelines that rely on error-prone automatic speech recognition, our system dir...
  </details>

- **2026-09-28** — Wonmo Koo, Jaeyeong Lee, Taeseong Yoon et al. — [GT-PSSM: Unified Probabilistic Framework for Stochastic Dynamics Modeling and Dependency Learning in Multivariate Time Series Anomaly Detection](http://arxiv.org/abs/2609.34161v1)
  <details><summary>📄 Abstract</summary>
  Multivariate time series anomaly detection (MTAD) is crucial for ensuring the safe and reliable operation of complex systems. Many existing methods learn normal patterns by training reconstruction or forecasting models on predominantly normal data. However, a large portion of these approaches rely on deterministic models and their associated point-wise output errors for anomaly scoring. Since real-world multivariate time series are inherently stochastic due to measurement noise and intrinsic sys...
  </details>

- **2026-09-28** — Kuniaki Saito, Yoshitaka Ushiku — [The Devil is in the Spectrum Bias: Spectrum-Balanced Feature Matching for Robust Representation Distillation](http://arxiv.org/abs/2609.34106v1)
  <details><summary>📄 Abstract</summary>
  Large visual foundation models have demonstrated remarkable transferability across a wide range of downstream tasks. To deploy such models efficiently, feature matching has become a popular knowledge distillation approach that transfers teacher representations to smaller student models without requiring labeled data. However, we show that the conventional feature matching objective with L2-distance is inherently biased toward reconstructing dominant spectral directions of the teacher representat...
  </details>

- **2026-09-27** — Guruprerana Shabadi, Aaditya Naik, Rajeev Alur et al. — [Learning Strategies to Break Judges](http://arxiv.org/abs/2609.33773v1)
  <details><summary>📄 Abstract</summary>
  As AI agents surpass human performance, it becomes exceedingly hard for system designers to evaluate them directly and understand their failure modes. Consequently, agents themselves are being deployed extensively to evaluate, judge, and provide feedback on model traces. But this raises an important question: how can we trust the judge? In this work, we propose an agent-guided method to find weaknesses of agentic judges that expose interpretable failure mechanisms. Our method focuses on mathemat...
  </details>

- **2026-09-27** — Antonio De Santis, Arsenio Leo, Marco Brambilla — [Augmenting Visual Anomaly Detection with Automated Interpretability](http://arxiv.org/abs/2609.33818v1)
  <details><summary>📄 Abstract</summary>
  Visual anomaly detectors identify deviations from known-normal data, but their anomaly signals may mix evidence of actual anomalies with benign visual variation. We investigate whether automated interpretability can augment visual anomaly detectors by identifying and intervening on different components of this signal. We decompose PatchCore nearest-normal residuals into sparse features using Sparse Autoencoders (SAEs), and provide high-activation and contrastive non-active examples to a Multimod...
  </details>

- **2026-09-27** — Yingming Zhou, Adarsh Vatsa, William Eiers — [RAISE: Reinforcing Access Control Policy Synthesis in LLMs via Symbolic Evaluation](http://arxiv.org/abs/2609.33796v1)
  <details><summary>📄 Abstract</summary>
  Translating natural-language access-control requirements into policies requires careful reasoning about permissions, constraints, and exceptions, and even frontier LLMs often produce policies that violate the intended authorization semantics. We construct CedarInstruct, to our knowledge the first dataset that supports both training and semantic evaluation for formally verifiable Cedar policy synthesis. It contains 5,800 scenarios across 44 domains and 1,408 representing a single synthetic organi...
  </details>

- **2026-09-27** — Eliott Jacopin, Éric Jacopin, Koichi Takahashi — [HTN Planning as a Coordination Layer for Multi-Server MCP Tool Orchestration](http://arxiv.org/abs/2609.33731v1)
  <details><summary>📄 Abstract</summary>
  The Model Context Protocol (MCP) isolates servers by design: only the host can orchestrate cross-server workflows. When the host is a large language model, the resulting orchestrations are non-deterministic, non-reproducible, and pay one inference round-trip per tool call. We present a coordination architecture in which a Hierarchical Task Network (HTN) planner generates a verifiable cross-server plan once, and a runtime middleware executes it deterministically across multiple MCP servers, bindi...
  </details>

- **2026-09-27** — Feilian Huang — [SpecRead: A Benchmark for Measuring Whether Language Models Understand Hardware Specifications](http://arxiv.org/abs/2609.33699v1)
  <details><summary>📄 Abstract</summary>
  Existing benchmarks for large language models (LLMs) in hardware design evaluate downstream artifacts such as generated RTL, assertions, or testbenches. When a model fails such a benchmark, the failure is ambiguous: it may have misread the specification, or it may have understood the specification and failed to write the code. We present SpecRead, a benchmark that isolates specification comprehension from generation ability. SpecRead v2.1 contains 385 questions over 10 open-source OpenTitan IP b...
  </details>

- **2026-09-27** — Zhixiang Zhang, Zesen Liu, Wai Ip Lai et al. — [Compositional Safety Failures in Harness Evolution: Identification and Runtime Monitoring](http://arxiv.org/abs/2609.33123v1)
  <details><summary>📄 Abstract</summary>
  Self-evolving agent harnesses continually update persistent components such as memory, prompts, skills, and tools. We call this process harness evolution. However, such evolution could introduce unexpected safety risks. Existing work studies harness misevolution and validates candidate harnesses or attributed individual component updates, leaving safety analysis of cross-component update interactions largely unexamined. To address this gap, we study compositional safety failures in harness evolu...
  </details>

- **2026-09-27** — Uliana Elina — [Maat: Independent Deterministic Contract-Based Governance for Multi-Agent LLM Workflows](http://arxiv.org/abs/2609.34017v1)
  <details><summary>📄 Abstract</summary>
  Large-language-model multi-agent systems (LLM-MAS) introduce a characteristic reliability problem: an error produced by one agent can be accepted as context by downstream agents and propagate across the workflow. Many proposed safeguards rely on learned or LLM-based judges whose verdicts are themselves probabilistic; we ask whether a deterministic layer can instead stop contract-detectable handoff defects. We present Maat, a runtime governance layer that validates agent-to-agent handoffs against...
  </details>

- **2026-09-26** — Xutao Mao, Rui Qian, Linghan Chen et al. — [Trust the Brand, Lose Control: How Identity Hijacks LLM Agent Orchestration](http://arxiv.org/abs/2609.32635v1)
  <details><summary>📄 Abstract</summary>
  LLM agents now execute tasks end to end with permission to change real systems and increasingly orchestrate subagents that differ in capability and cost. Prior work treats the choice of subagent as an optimization problem. Yet the orchestrator makes this choice from the identities that subagents display, and an attacker can spoof them. Displayed identity thus decides operational authority, meaning who is trusted to check the work and who is allowed to change it. As a result, a risky subagent can...
  </details>

- **2026-09-26** — Derui Wang, Zewei Shi, Rayne Holland et al. — [Black-Box Auditing of Epistemic Reliability in Multi-Agent Debate Distillation](http://arxiv.org/abs/2609.32361v1)
  <details><summary>📄 Abstract</summary>
  Debate distillation adapts weaker verifiers using multi-agent debate transcripts to improve their judgement in subsequent debates, but gains on monitored tasks do not establish reliability on related unmonitored tasks. We study epistemic reliability degradation, in which adaptation preserves monitored performance while reducing support for correct responses on hidden tasks. We consider an adversarial debater that manipulates debate arguments while defending the correct monitored response, and as...
  </details>

- **2026-09-26** — Junchi Chen, Changtao Miao, Yuxiao Xiang et al. — [PlanGuard: A Guardrail for Multi-Step Plan Safety in Embodied Agents](http://arxiv.org/abs/2609.32801v1)
  <details><summary>📄 Abstract</summary>
  Embodied task planners may produce multi-step plans whose subtask dependencies and interactions with the environment create physical risks during execution. Yet existing safeguards overlook such compositional risks, as general-purpose guardrails focus on semantic harm and embodied safety detectors assess subtasks in isolation. To address this gap, we introduce PlanGuard, the first pre-execution detector that evaluates the physical safety of a complete multi-step plan in its current environment. ...
  </details>

- **2026-09-26** — Murat Ozer, Bulent Erenay, Ibrahim Berber — [Reward Hacking and Agent Containment Failure: A Monte Carlo Study Based on the 2026 Hugging Face Incident](http://arxiv.org/abs/2609.32390v1)
  <details><summary>📄 Abstract</summary>
  The July 2026 intrusion into Hugging Face production infrastructure showed how reward hacking can become an external cybersecurity incident when a capable agent encounters weak containment boundaries. This study develops a probabilistic risk model linking five stages: reward hacking, containment escape, usable access, persistence, and failure of detection. A Monte Carlo simulation evaluates 100,000 runs under each of four control configurations. Input distributions represent explicit uncertainty...
  </details>


### 📂 alignment
*对齐与安全约束 / Alignment & Safety Constraints* — 54 papers

- **2026-09-28** — Qirui Liu, Yichen Sun, Yan Wang et al. — [DeShortcut-Align: Decoupling Spurious Shortcuts for Robust Safety Alignment in Large Reasoning Models](http://arxiv.org/abs/2609.34896v1)
  <details><summary>📄 Abstract</summary>
  Safety alignment of large reasoning models (LRMs) via supervised fine-tuning (SFT) and reinforcement learning (RL) often yields near-perfect safety scores, yet this apparent success comes at the cost of severe over-refusal and degraded general capabilities. Through systematic empirical analysis, we find that these failures are closely associated with the learning of spurious shortcuts rather than robust intent-sensitive safety evaluation. Specifically, we identify two dominant shortcuts: formatt...
  </details>

- **2026-09-28** — Yejin Kim, William F. Shen, Seokwon Jung et al. — [TULIP: Targeted LLM Unlearning at Layers Identified Per-Input](http://arxiv.org/abs/2609.34591v1)
  <details><summary>📄 Abstract</summary>
  Representation-level unlearning intervenes on the intermediate hidden states of LLMs. Although knowledge is distributed across layers, existing methods operate at a single fixed layer for the entire forget set. We ask whether such a fixed layer is sufficient. To answer this, we design a hijacking experiment that grafts hidden states of the target model into an oracle trained only on the retain set. The oracle cannot produce the forget answer on its own, yet it produces the answer from the grafte...
  </details>

- **2026-09-28** — Hyunwoo Yoo, Cassie Huang, Haebin Shin et al. — [Representation Alignment as a Bottleneck in LLM-Based Retrosynthesis Planning](http://arxiv.org/abs/2609.35571v1)
  <details><summary>📄 Abstract</summary>
  While LLMs show promise in general reasoning, symbolic planning in chemistry remains a bottleneck. Direct ''SMILES-to-PDDL'' attempts fail because they force models to juggle chemical analysis and planning-language structuring simultaneously. We hypothesize that this failure stems from a lack of intermediate abstractions rather than insufficient model capacity. By decomposing retrosynthesis into molecule mapping, reaction mapping, and PDDL generation, we achieve high success rates where end-to-e...
  </details>

- **2026-09-28** — Pranjal Garg, Jacob Beck — [Spontaneous Context Restoration: How Language Models Recover from Corrupted Inputs](http://arxiv.org/abs/2609.35475v1)
  <details><summary>📄 Abstract</summary>
  Language models sometimes produce correct outputs even when their inputs are corrupted by deletion, replacement, or misspelling. We study the internal processes accompanying this behavior, which we call context restoration, in controlled attention-only transformers and five pretrained LLMs (1B-32B parameters) across arithmetic, reading comprehension, and multiple-choice reasoning tasks. In the attention-only transformers, restoration emerges spontaneously despite training exclusively on clean se...
  </details>

- **2026-09-28** — Carlos Garrido-Munoz, Jorge Calvo-Zaragoza — [Handwritten Text Recognition Lives in the High-Pixel Variance Subspace](http://arxiv.org/abs/2609.35473v1)
  <details><summary>📄 Abstract</summary>
  In self-supervised pretraining for Handwritten Text Recognition (HTR), pixel reconstruction methods outperform contrastive methods, unlike in natural-image classification. We argue that this difference follows from where discriminative signal lies in pixel space: for HTR, it is concentrated in high-variance directions and largely absent from low-variance ones. This predicts that objectives preserving high-variance pixel content will transfer best. We test six SSL methods from three families (pix...
  </details>

- **2026-09-28** — Lucas Bandarkar, Junlin Hu, Chenyuan Yang et al. — [Multilinguality in Hybrid Attention LLMs](http://arxiv.org/abs/2609.35378v1)
  <details><summary>📄 Abstract</summary>
  In response to the growing demand for long sequences in agentic and reasoning use cases, many state-of-the-art LLMs combine multiple variants of attention to mitigate the quadratic complexity of traditional softmax attention. These hybrid attention LLMs aim to balance the strengths and limitations of full attention and alternatives based on recurrence. This work presents a first study of how hybrid attention impacts the multilinguality of LLMs. Beyond the impact on long sequences in poorly token...
  </details>

- **2026-09-28** — Bangjun Wang, Longyan Wu, Yukun Wei et al. — [From Pixel to Poses: Object-centric Tool Manipulation Learning from Human Demonstrations](http://arxiv.org/abs/2609.35375v1)
  <details><summary>📄 Abstract</summary>
  Scaling up robotic manipulation is primarily bottlenecked by the scarcity of real-world robot data. While recent approaches leverage human video demonstrations to mitigate this shortage, they remain computationally expensive and still rely on paired human-robot data for domain alignment. Although current state-of-the-arts excel at long-horizon tasks, they struggle with the delicate and precise control required for complex tool manipulation. To overcome these limitations, we introduce P2P-T, from...
  </details>

- **2026-09-28** — Xingming Long, Jie Zhang, Yuecong Min et al. — [Beyond Saying Less: Fine-Grained Alignment for Informative and Faithful Vision-Language Models](http://arxiv.org/abs/2609.35294v1)
  <details><summary>📄 Abstract</summary>
  Object hallucination remains a major challenge for large vision-language models. While off-policy preference optimization proves to be an effective solution, on-policy reinforcement learning provides a more promising direction as it directly targets a model's current failure modes. However, we find that without fine-grained reward formulation and allocation, on-policy optimization often falls into an easy shortcut: reducing hallucinations merely by saying less---making fewer valid claims. To com...
  </details>

- **2026-09-28** — Han Fu, Jiacheng Chen, Baoquan Zhao et al. — [Scaffold Then Internalize: Representation Injection for Diffusion Transformers](http://arxiv.org/abs/2609.35292v1)
  <details><summary>📄 Abstract</summary>
  Recent representation alignment (REPA) methods accelerate diffusion transformer training by aligning projections of the transformer's hidden states with representations from pretrained visual encoders. In this work, we explore a reverse and complementary direction to REPA: rather than projecting diffusion representations into the encoder's space, we inject encoder representations into the diffusion transformer, allowing them to actively participate in the denoising process. To this end, we intro...
  </details>

- **2026-09-28** — Yuanzi Li, Lingjie Wang, Zihang Tian et al. — [SCBO: Semantically Coherent Batching and Ordering for LLM-Based Social Surveys](http://arxiv.org/abs/2609.35250v1)
  <details><summary>📄 Abstract</summary>
  Large Language Models (LLMs) offer a scalable way to simulate survey respondents using demographic profiles and observed reference responses. However, the conventional approach of predicting one question per prompt repeatedly encodes the same context, limits each target to a narrow set of reference responses, and prevents later predictions from using information in earlier answers. Predicting multiple questions in one prompt can reduce these costs, share a broader pool of references, and let lat...
  </details>

- **2026-09-28** — Shurui Liu, Weide Chen, Changwang Yi et al. — [DrawingsDreamer: A Unified Multi-View Engineering Drawings Generation Model](http://arxiv.org/abs/2609.35242v1)
  <details><summary>📄 Abstract</summary>
  Scalable Vector Graphics (SVG) are essential for modern industrial Computer-Aided Design (CAD). However, existing autoregressive SVG generation models are predominantly tailored for artistic creation and struggle to maintain the rigorous geometric fidelity and cross-view spatial alignment required for engineering drawings. To bridge this gap, we introduce \textbf{DrawingsDreamer}, a unified Large Language Model (LLM)-driven framework for multi-view vector-based engineering drawings generation. B...
  </details>

- **2026-09-28** — Rui Zhong, Yu Li, Zheyu Yan et al. — [Beyond Selection: Token Parameterization for Extreme Visual Token Compression](http://arxiv.org/abs/2609.35232v1)
  <details><summary>📄 Abstract</summary>
  Visual-token compression is effective for improving the efficiency of vision-language models, but under extreme compression budgets, token pruning can break visual grounding while learned resamplers increase parameter count, attention cost, and training complexity. We revisit compression through a token parameterization lens, separating (i) basis transformation and structured truncation (retained subspace/compressibility) from (ii) coordinate organization (optimization and cross-modal alignment)...
  </details>

- **2026-09-28** — Zhaoyi An, Sihan Tan, Youngbae Hwang et al. — [SignFLIP: A Unified Model for Sign Language Translation and Generation via Stage-wise Alignment at Scale](http://arxiv.org/abs/2609.35225v1)
  <details><summary>📄 Abstract</summary>
  Sign language translation and generation share the goal of bidirectional alignment between text and sign representations. However, existing approaches either treat them as isolated tasks or are only verified on limited datasets, limiting effective modeling between modalities. In this paper, we propose SignFLIP, a unified LLM-centered framework for translation and generation. To enable bidirectional mapping between text and sign, SignFLIP adopts a symmetric architecture together with a stage-wise...
  </details>

- **2026-09-28** — Husrev Taha Sencar, Rezart Beka, Danish Naeem et al. — [From Normative Frameworks to Alignment Data: Constructing and Evaluating SFT and Preference Data](http://arxiv.org/abs/2609.35201v1)
  <details><summary>📄 Abstract</summary>
  Aligning language models with a specified normative framework requires translating abstract principles into concrete examples and preference signals from which models can learn. We present an expert-driven methodology for constructing such alignment data and apply it to a normative framework grounded in Islamic ethical, theological, and jurisprudential traditions. Over approximately one year, seven domain experts systematically probed language models to identify alignment deficiencies, curated d...
  </details>

- **2026-09-28** — Bohao Wang, Xiaoyan Zhao, Yang Zhang et al. — [Using Context Is Not Enough: Test-Time Training for Personalized Reward Modeling](http://arxiv.org/abs/2609.35109v1)
  <details><summary>📄 Abstract</summary>
  Reinforcement learning from human feedback (RLHF) aligns large language models (LLMs) with human preferences, yet most pipelines learn a single reward model that overlooks individual differences in preferences. Personalized reward models (PRMs) address this by conditioning rewards on user-specific feedback, most commonly through in-context learning (ICL), where a user's historical comparisons are supplied as contextual preference pairs. However, we identify a key limitation of ICL-based PRMs: th...
  </details>

- **2026-09-28** — Ben Moore, Liam Dunne — [What Drives Citations in Production Large Language Models? An Observational Multi-Method Study of Two Million AI Citations Across Ten Thousand Web Pages](http://arxiv.org/abs/2609.35077v1)
  <details><summary>📄 Abstract</summary>
  Production large language models retrieve and cite web pages alongside generated answers, yet the page-level features that predict citation frequency remain poorly characterised. We present an observational study of approximately 2 million LLM citations from four commercial engines (ChatGPT, Claude, Google AI, Gemini) over six months, joined to 10,000 crawled pages from nineteen B2B SaaS workspaces. Sixty-plus features are tested using a nine-method consensus framework combining mixed-effects re...
  </details>

- **2026-09-28** — Hongli Xu, Zhaowei Lu, Junwen Huang et al. — [LEGAU: Learning Semantic Gaussian Priors for Scalable Category-level Pose Estimation](http://arxiv.org/abs/2609.35046v1)
  <details><summary>📄 Abstract</summary>
  Category-level 6D pose estimation from a single RGB-D observation is inherently under-constrained, since partial visible geometry must be interpreted together with a canonical object structure before a stable pose can be determined. We present LEGAU, a unified framework that jointly predicts NOCS correspondence, object pose and size, and a canonical Semantic Gaussian Field. Rather than treating reconstruction as a detached auxiliary task, LEGAU uses the Gaussian field as a category-conditioned s...
  </details>

- **2026-09-28** — Antonio Ferrara, Alberto Rumi, Francesco Bonchi — [BA-DPO: Bias-Adjusted Direct Preference Optimization for Language Model Alignment](http://arxiv.org/abs/2609.35044v1)
  <details><summary>📄 Abstract</summary>
  Preference-based alignment methods such as Direct Preference Optimization (DPO) use pairwise preferences labeled by human annotators to fine-tune language models. However, annotators carry systematic biases toward some attributes: a name that signals a gender or an ethnicity, a persona, a language variety, a formatting convention, or length. If not properly addressed, these systematic biases can be absorbed and amplified during alignment. Existing methods address length bias or annotator disagre...
  </details>

- **2026-09-28** — Yifan Wang, Shipeng Zhu, Fei Xiong et al. — [PEAR: Progressive Evidence-Based AutoResearch for Industrial Search Systems](http://arxiv.org/abs/2609.35031v1)
  <details><summary>📄 Abstract</summary>
  AutoResearch improves systems through iterative experimentation: agents propose candidate modifications, evaluate them, and use the results to guide subsequent exploration. Applying this paradigm to industrial search presents two challenges. (1) Common AutoResearch approaches follow a keep-if-better rule, retaining the highest-scoring candidate for subsequent experiments. Under non-stationary traffic, transient gains may be mistaken for persistent improvements, impairing reliable accumulation of...
  </details>

- **2026-09-28** — Florian Eichin, Philipp Mondorf, Andrei Mircea et al. — [Don't Forget! Decomposing the Training Dynamics of Memorization in Language Models](http://arxiv.org/abs/2609.34933v1)
  <details><summary>📄 Abstract</summary>
  Memorization has been proposed as a mechanism to explain how language models fit the tail of their training distributions, but its training dynamics are not understood well. In this work, we take a fine-grained look at memorization by decomposing the loss trajectory of memorized sequences over training and model parameters. Across the Pythia family, we study memorization of duplicated training sequences (recitation) and rare ones (recollection). We find that memorization in both cases is charact...
  </details>

- **2026-09-28** — Yanzhe Chen, Qifang Zhao, Xiaoxiao Xu et al. — [Muon Sublates the Edge of Stability in LLM Pretraining](http://arxiv.org/abs/2609.34915v1)
  <details><summary>📄 Abstract</summary>
  Muon is increasingly used for language-model pretraining, yet its large-step dynamics are not captured by the classical edge-of-stability (EoS) picture of gradient descent (GD). In GD, loss neutrality, equal-magnitude update reversal, and marginal stability meet at a single learning-rate-dependent edge. We show that Muon breaks this coupling. For stochastic no-momentum Muon, we derive a coherence-corrected conditional loss-neutral boundary $2ρ_b/η$, while temporal alignment follows a separate ge...
  </details>

- **2026-09-28** — Zhuchenyang Liu, Ziyi Wang, Yao Zhang et al. — [ColNanoVDR: Document-Free Query Distillation for Multi-Vector Visual Document Retrieval via Optimal Transport](http://arxiv.org/abs/2609.34899v1)
  <details><summary>📄 Abstract</summary>
  Multi-vector retrievers built on vision-language models lead visual document retrieval (VDR), but they run a multi-billion-parameter query encoder on every search. Distilling this encoder into a small student that queries the teacher's existing index would remove the bottleneck. The standard recipe, however, matches the teacher's MaxSim scores and so requires encoding and caching every training page, which can reach terabytes of page tokens. NanoVDR avoids pages entirely by training on the teach...
  </details>

- **2026-09-28** — Jiacheng Liu, Jingwei Song, Qituan Zhang et al. — [Beyond Token Alignment: Event Completion for Cross-Tokenizer On-Policy Distillation](http://arxiv.org/abs/2609.34738v1)
  <details><summary>📄 Abstract</summary>
  On-policy distillation (OPD) transfers knowledge between language models through teacher supervision on student-generated trajectories. With different tokenizers, a single teacher token may require multiple student tokens to generate, creating intermediate states where the event is entered but not yet completed. Existing cross-tokenizer methods align tokens or text spans to construct comparable prediction targets. We study a complementary problem after partial generation: once the student produc...
  </details>

- **2026-09-28** — Yongcong Wang, Hingchin Chen, Mingyu Fan et al. — [What Visual Generators Need from Teachers: Rethinking Representation Alignment](http://arxiv.org/abs/2609.34732v1)
  <details><summary>📄 Abstract</summary>
  Representation alignment speeds up diffusion transformer training by pulling an intermediate block of the model (student) toward features of a frozen pretrained encoder (teacher). Which teacher layer to align, and for how long, is still set by convention, and each alternative costs a training run. We find that alignment helps where the student cannot linearly recover the teacher's features, not where it already resembles them. Since a deep teacher layer is largely predictable from the one below,...
  </details>

- **2026-09-28** — Le Zhao, Zesong Fei, Xinyi Wang et al. — [Intelligent Beamforming and Handover via Physics-Informed Beam-Aware CKM Diffusion](http://arxiv.org/abs/2609.34704v1)
  <details><summary>📄 Abstract</summary>
  Downlink communications from base stations (BSs) to unmanned aerial vehicles (UAVs) in sixth-generation (6G) networks require precise beam alignment to overcome severe mobile communication path loss. However, traditional exhaustive beam sweeping relies on discrete codebooks and consumes valuable air-interface resources for online measurements, rendering it inefficient for highly dynamic aerial environments. In this paper, we propose BeamCKMDiff, a physics-informed generative diffusion framework ...
  </details>

- **2026-09-28** — Dongkyeom Jang, In-Nea Wang, Junho Jeong — [Tool Waiting and Re-arrival in Compile-Time-Static LLM Serving: Cost Mechanisms and Configuration Selection](http://arxiv.org/abs/2609.34663v1)
  <details><summary>📄 Abstract</summary>
  In agentic LLM services, a session calls an external tool, waits for it, and re-arrives to continue inference. Statically compiled NPU serving can fix the batch bucket set, the maximum batch size, and the number of KV cache slots at compile time. We define such an environment as a compile-time-static serving substrate and analyze the execution-time cost that tool waiting and re-arrival incur in it. On a single LLM instance, we run synthetic workloads following a measured tool waiting time distri...
  </details>

- **2026-09-28** — Yang Tan, Qijia Tian, Gangyu Sun et al. — [A General Harness for Protein Foundation Model Fitness Prediction](http://arxiv.org/abs/2609.34654v1)
  <details><summary>📄 Abstract</summary>
  Accurate fitness prediction is central to protein engineering and understanding sequence-function relationships. With advances in deep learning, protein foundation models (PFMs) have become widely used for this task. Recent analyses, however, show that these models share preferences reflecting their training corpora, while unreliable inputs can further distort fitness predictions. Family-specific evolutionary evidence and structural context can help address these limitations by providing complem...
  </details>

- **2026-09-28** — Peilin Sun, Guang Liang, Jin Tong et al. — [GLF-Q: Global-Local Feature-based Quantization for Vision Transformers](http://arxiv.org/abs/2609.34564v1)
  <details><summary>📄 Abstract</summary>
  Post-training quantization (PTQ) efficiently compresses Vision Transformers (ViTs) without retraining, yet suffers severe accuracy degradation at low bit-widths. Existing optimization-based PTQ methods guide block reconstruction via either soft logits or second-order Hessian proxies. Logit supervision is prone to overfitting on limited calibration data, while Hessian approximations incur structural truncation errors. To address these limitations, we propose \textbf{GLF-Q}, a novel PTQ framework ...
  </details>

- **2026-09-28** — Xi Xiao, Tianchen Zhao, Youngeun Kim et al. — [Rethinking Latent Visual Reasoning: Grounding Latent Reasoning in Visual Evidence](http://arxiv.org/abs/2609.34563v1)
  <details><summary>📄 Abstract</summary>
  Latent visual reasoning (LVR) enables multimodal large language models (MLLMs) to perform intermediate computation in continuous latent tokens rather than expressing every reasoning step in words. However, unlike textual CoT, latent reasoning is not directly observable, making it difficult to supervise what latent tokens learn. In this work, we first conduct a thorough analysis of latent-token behavior and identify a latent evidence-credit gap: latent tokens respond only weakly to image perturba...
  </details>

- **2026-09-28** — Luyao Jin, Running Zhao, Huan Zhao et al. — [Brain-Conditioned Action Policies for Neural Motor Decoding](http://arxiv.org/abs/2609.34561v1)
  <details><summary>📄 Abstract</summary>
  Motor brain-computer interfaces (BCIs) aim to decode motor intention, enabling people with paralysis to control external devices. Neural motor decoding typically learns task-specific mappings from neural activity to kinematics, yet remains constrained by scarce paired neural-action data. We propose BrainVLA, a framework that enables neural motor decoding by drawing on a pretrained vision-language-action (VLA) model through language-mediated alignment. BrainVLA mitigates reliance on scarce paired...
  </details>

- **2026-09-28** — Boyu Zhang, Yangming Cheng, Ning Zhang et al. — [SAGE: Subspace Alignment for Classifier-Free Guidance in Mixture-of-Experts Diffusion Models](http://arxiv.org/abs/2609.34525v1)
  <details><summary>📄 Abstract</summary>
  Diffusion Transformers with Mixture-of-Experts (MoE) routing are a leading recipe for scaling generative models. Classifier-Free Guidance (CFG) is essential for generation quality, yet excessively high guidance scales trigger collapse. We identify a previously unreported failure mode in their combination: the two CFG branches route independently, so their realized activations occupy different subspaces. The unconditional write then leaves the conditional subspace, and CFG amplifies that residual...
  </details>

- **2026-09-28** — Saeid Firouzi Daghigh, Majid Iranpour Mobarakeh — [HPMD: A Historical Persian Manuscript Dataset for Word Spotting with Line-Level Annotation](http://arxiv.org/abs/2609.34490v1)
  <details><summary>📄 Abstract</summary>
  Large collections of historical Persian manuscripts have been digitized, but searching them is still slow and mostly manual. Historians usually want to find where a specific name, date, event, or topic appears, which is a word spotting problem. Progress on this task is limited by two things. First, there is almost no public dataset of historical Persian handwriting; the only notable resource, OpenITI MAKHZAN, contains a relatively small Persian portion. Second, word spotting models usually need ...
  </details>

- **2026-09-28** — Shengchao Hu, Peng Wang, Qiyang Zhou et al. — [Alignment-Guided Flow Transformer for Efficient Vision-Language-Action Policy Learning](http://arxiv.org/abs/2609.34467v1)
  <details><summary>📄 Abstract</summary>
  Recent advances in Vision-Language-Action (VLA) models point toward general-purpose robotic intelligence by unifying perception, instruction, and control. Despite impressive progress, existing VLA models often adapt poorly due to \emph{tri-modal misalignment} among vision, language, and action, which weakens action grounding and hurts generalization and fine-tuning efficiency. In this work, we present Alignment-Guided Flow Transformer (AGFT), a novel framework that explicitly enforces tri-modal ...
  </details>

- **2026-09-28** — Chuiyang Meng, Ming Tang, Vincent W. S. Wong — [CORTEX: Learning to Share and Specialize in Dense Language Models](http://arxiv.org/abs/2609.34449v1)
  <details><summary>📄 Abstract</summary>
  Large language models are trained on heterogeneous data mixtures, where different knowledge domains require both shared knowledge and specialization. Existing modular approaches typically impose explicit components or discover modules through interpretability analysis after training. In this work, we propose CORTEX, a learning dynamics-inspired framework that learns internal modularization within dense language models. CORTEX partitions trainable matrices into parameter groups and learns module ...
  </details>

- **2026-09-28** — Huimin Yan, Xian Yang, Zhi Wang et al. — [Clinical Trajectory Alignment for Medical Vision-Language Pre-training](http://arxiv.org/abs/2609.34439v1)
  <details><summary>📄 Abstract</summary>
  Medical vision-language pre-training largely follows a visit-level image-report matching paradigm, aligning paired images and reports at individual visits. While effective for static cross-modal correspondence, this paradigm provides limited supervision for longitudinal clinical change, such as whether abnormalities improve, remain stable, or worsen over time. Learning such change is challenging because temporal semantics are implicit in free-text reports, and different abnormalities within the ...
  </details>

- **2026-09-28** — Shengchao Hu, Peng Wang, Jifeng Hu et al. — [Q-learning Penalized Transformer for Safe Offline Reinforcement Learning](http://arxiv.org/abs/2609.34426v1)
  <details><summary>📄 Abstract</summary>
  This paper addresses the problem of safe offline reinforcement learning, which involves training a policy to satisfy safety constraints using an offline dataset. This problem is inherently challenging as it requires balancing three highly interconnected and competing objectives: satisfying safety constraints, maximizing rewards, and adhering to the behavior regularization imposed by the offline dataset. To tackle this trilogy challenge, we propose Q-learning Penalized Transformer policy (QPT), a...
  </details>

- **2026-09-28** — Eric Frankel, Banghua Zhu, Sewoong Oh et al. — [ABC-Align: Prediction-Powered Alignment with Adaptive Bias Control](http://arxiv.org/abs/2609.34374v1)
  <details><summary>📄 Abstract</summary>
  Language model post-training is often bottlenecked by the need for human-collected preference data, which is expensive and difficult to scale. Reinforcement learning from AI feedback (RLAIF) style approaches that leverage pseudo labels offer an abundant alternative but introduce systematic biases that degrade downstream alignment. Recent general-purpose semi-supervised methods correct for teacher bias using a small set of human-labeled examples, but suffer from high variance especially when huma...
  </details>

- **2026-09-28** — Mihir Chauhan, Aniket Bera — [Emergence, Not Bandwidth: Physical Coupling and the Limits of Learned Multi-Agent Communication](http://arxiv.org/abs/2609.34373v1)
  <details><summary>📄 Abstract</summary>
  Rate-limited multi-agent teams raise three questions the emergent-communication literature has answered only empirically: what an optimal message should encode, what compression costs over a horizon, and when a learned protocol is unique enough for a teammate to read. We answer them for rate-limited Dec-POMDPs, then measure how far reinforcement learning falls short of the optimum. Our theorems fix what is achievable independently of any learner, so a gap between an engineered and a learned send...
  </details>

- **2026-09-28** — Zelong Xu, Yan Li, Wenhe Hu et al. — [SyncRA: Learning Temporal Correspondence in Omni-Modal Models](http://arxiv.org/abs/2609.34363v1)
  <details><summary>📄 Abstract</summary>
  Recent omni-modal models demonstrate strong perception of audio and visual inputs, yet often struggle to connect what they hear with what they see at the same moment. This weakness in temporal correspondence can cause models to associate spoken cues with the wrong visual scenes, producing plausible answers grounded in incorrect audio-visual pairings. We diagnose this problem through controlled temporal swaps, revealing that model answers do not reliably follow changes in these pairings. To addre...
  </details>

- **2026-09-28** — Yuchen Cai, Ding Cao, Qixiang Yin et al. — [Learning to Steer, Steering to See: Unveiling the Geometry of RLVR in Large Language Models via Trainable Vectors](http://arxiv.org/abs/2609.34344v1)
  <details><summary>📄 Abstract</summary>
  Reinforcement learning (RL) has become a key paradigm for enhancing the reasoning of large language models, yet the high dimensionality of parameter updates makes its training dynamics hard to analyze. We study reinforcement learning with verifiable rewards (RLVR) and use vector steering to identify a low-dimensional effective manifold in activation space associated with RL-induced gains. We uncover two geometric properties. (1) Effective Manifold Capacity: the capacity needed to reproduce RL ga...
  </details>

- **2026-09-28** — Chengyang Zhang, Wenchuan Zhang, Bo Li et al. — [See, Measure, and Reason: Learning Visually Grounded Reasoning in Pathology](http://arxiv.org/abs/2609.34277v1)
  <details><summary>📄 Abstract</summary>
  Pathological assessment relies on recognizing fine-grained visual details in histological images. Vision-language models (VLMs) increasingly support pathology interpretation, yet their ability to perceive these details remains inadequate. This weakness leads to inaccurate cellular observations that can persist even when final answers are correct. In this paper, we propose ASPECT to improve visually grounded reasoning through explicit supervision of cellular appearance and abundance. ASPECT train...
  </details>

- **2026-09-28** — Shenghan Tan, Ziyi Zhou, Wenpeng Hu et al. — [RADNPO: Reference-free Adaptive Negative Preference Optimization for LLM Unlearning](http://arxiv.org/abs/2609.34251v1)
  <details><summary>📄 Abstract</summary>
  Large language models (LLMs) can memorize sensitive, private, or copyrighted content during pre-training, making machine unlearning necessary for removing targeted knowledge. Recent preference optimization (PO)-based unlearning methods improve stability over gradient ascent (GA)-based methods by introducing alignment-style objectives, which effectively suppress the probability of forget targets. However, target suppression alone does not sufficiently constrain the next-token distribution after u...
  </details>

- **2026-09-28** — Yuyang Deng, Mohammadreza M. Kalan, Eitan J. Neugut et al. — [Constrained Nonconvex Stochastic Optimization with One Projection](http://arxiv.org/abs/2609.34099v1)
  <details><summary>📄 Abstract</summary>
  Constrained nonconvex optimization has seen increasing application in modern machine learning, such as safe LLM alignment/finetuning, transfer learning and rank-constrained continual learning. The commonly used approach is Projected SGD which requires projection at every iteration. However, projection onto a functional constraint can cost substantially more than a stochastic first-order update. We study whether this operation can be deferred until the end of nonconvex stochastic optimization, an...
  </details>

- **2026-09-28** — Feiyang Chen, Wenhan Yang, Bohan Wang et al. — [HiThink Turn: An Intent-Aware Turn-Taking Control Module for Full-Duplex Dialogue](http://arxiv.org/abs/2609.34096v1)
  <details><summary>📄 Abstract</summary>
  Full-duplex dialogue requires timely yet selective interruption handling, which end-of-turn prediction alone cannot achieve: complete utterances may need no response, while unfinished requests may warrant interruption. To address this challenge, we propose HiThink Turn, an intent-aware streaming turn-state predictor that separates response intent from semantic completeness and conditions decisions on system playback state. A key contribution is minimal intent-sufficient prefix supervision, const...
  </details>

- **2026-09-28** — Yaqing yang, Vikram Mohanty, Mei-Xi Chia et al. — [StructSim: Measuring Idea Similarity at Scale Through Structural Representation](http://arxiv.org/abs/2609.34046v1)
  <details><summary>📄 Abstract</summary>
  Measuring idea similarity is fundamental to creativity evaluation, especially as LLMs enable idea generation at increasing scale. However, text embeddings collapse an idea into a single vector, making it difficult to capture structural similarity, including partial overlap across core and supporting components and differences across levels of abstraction. We introduce a shared structural representation that decomposes ideas into purpose, mechanism, and implementation components and organizes rel...
  </details>

- **2026-09-28** — Samuel Tetteh, Cody Fleming — [Vision--Language Signals in Constrained RL: Safety Gains Without Anticipation](http://arxiv.org/abs/2609.34041v1)
  <details><summary>📄 Abstract</summary>
  Safe reinforcement learning seeks policies that maximise task performance while satisfying safety constraints. In driving benchmarks, however, collision costs typically appear only at the time of collision, providing no advance warning of an approaching hazard. Frozen vision--language models can provide dense semantic feedback, yet it remains unclear whether their scores anticipate collisions and which component drives an observed safety improvement. Episodic cost can also favour policies that m...
  </details>

- **2026-09-28** — Christian Moya, Elliott Thornley, Guang Lin — [Verifier Errors in RLVR: Reward Hacking, Limits of Feedback, and Selective Control](http://arxiv.org/abs/2609.35677v1)
  <details><summary>📄 Abstract</summary>
  In reinforcement learning with verifiable rewards (RLVR), imperfect verifiers can reward incorrect responses, creating opportunities for reward hacking. Using gradient flow with a fixed verifier, we characterize the conditions under which reward rises while correctness falls. We then show that the observations available during RLVR are, in general, insufficient to detect or identify accepted errors, or to guarantee their reduction without sacrificing correct responses. To address this limit, we ...
  </details>

- **2026-09-27** — Mehmet Murat Albayrakoglu, Mehmet Nafiz Aydin — [High-Level Text Preprocessing for Semantic Similarity Analysis of Discursive Texts: A Framework and Empirical Demonstration](http://arxiv.org/abs/2609.33983v1)
  <details><summary>📄 Abstract</summary>
  Semantic Textual Similarity (STS) methods assume that a document's lexical content faithfully represents what it asserts. This assumption fails for discursive documents that discuss, compare, critique, and contextualize other positions in the process of articulating their own. The result is semantic diffusion: similarity scores between documents are inflated by vocabulary acquired through discursive engagement rather than substantive alignment. Standard Natural Language Processing (NLP) preproce...
  </details>

- **2026-09-27** — Kedi Chen, Chen Lin, Yutao Sun et al. — [Dual-Vocabulary Language Model for Cross-Tokenizer Distillation](http://arxiv.org/abs/2609.33816v1)
  <details><summary>📄 Abstract</summary>
  On-policy distillation (OPD) bridges teacher supervision and student behavior, but different teacher-student tokenizers introduce misalignment in both input tokenization (#1) and output logits (#2). Existing approaches address the former by matching same-text spans or converting tokens to bytes, often losing fine-grained token information or disrupting the native-token paradigm, while for the latter, strategies such as ranking, padding, or key-token selection retain only shared logit dimensions,...
  </details>

- **2026-09-27** — Yiheng Lyu, Xueying Jiang, Wenhao Li et al. — [CodeActionBench: Evaluating Agentic Code-as-Policy for Embodied Manipulation](http://arxiv.org/abs/2609.33807v1)
  <details><summary>📄 Abstract</summary>
  How well can general-purpose multimodal models turn visual understanding and reasoning into embodied manipulation via executable code? We introduce CodeActionBench, a benchmark of 25 manipulation tasks that evaluates this capability through agentic Code-as-Policy. Without task-specific fine-tuning, demonstrations, external specialist perception or grasp modules, privileged scene state, or predefined task policies, agents should select visual evidence, form task-relevant 3D estimates, construct m...
  </details>

- **2026-09-27** — Yayue Deng, Dingdong Wang, Yuxuan Hu et al. — [DuraS2ST: Chain-of-Thought and Reinforcement Learning for Duration-Aligned Speech-to-Speech Translation](http://arxiv.org/abs/2609.33742v1)
  <details><summary>📄 Abstract</summary>
  Speech-to-speech translation (S2ST) in time-sensitive applications such as video dubbing requires not only semantic fidelity and speaker preservation, but also strict duration consistency to avoid audio-visual misalignment. However, existing S2ST systems largely generate target speech without explicit temporal planning, making duration control an unresolved challenge. We introduce DuraS2ST, a duration-aligned reasoning framework that enables a single speech language model to first generate an ex...
  </details>

- **2026-09-27** — Yassine Sghaier, Emilio Calvanese Strinati, Philipp del Hougne — [Wave-Domain Semantic Equalization Using a Practical Dynamic Metasurface Antenna with Strong Mutual Coupling](http://arxiv.org/abs/2609.33729v1)
  <details><summary>📄 Abstract</summary>
  Semantic mismatch between independently trained AI-native agents in heterogeneous networks can impair semantic communications. Hybrid analog-digital semantic equalization can align the incompatible latent representations without retraining the semantic transceivers. We study a practical realization of this approach based on a fabricated dynamic metasurface antenna (DMA), an emerging low-cost, low-power, ultracompact technology for hybrid analog-digital beamforming. We model the DMA-assisted chan...
  </details>

- **2026-09-27** — Tianzhuo Yang, Zirui Mi, Yantao Huang et al. — [AgentBoundary: Counterfactual Evaluation of Safety in Tool-Using LLM Agents](http://arxiv.org/abs/2609.33658v1)
  <details><summary>📄 Abstract</summary>
  Safety alignment for large language models (LLMs) in conversational settings is largely framed around whether to answer or refuse a request. In agentic settings, however, the same models must decide whether to act as permission-critical evidence emerges during execution. This creates a distinct challenge: apparent risk, action permissibility, and task competence are easily confounded, making agentic over-refusal difficult to distinguish from ordinary task failure. To address this, we introduce A...
  </details>

- **2026-09-27** — Jiabin Fan, Dezhi Ye, Yongchang Hao et al. — [RMB: Reward Model Boosting Mitigates Reward Hacking](http://arxiv.org/abs/2609.33221v1)
  <details><summary>📄 Abstract</summary>
  Reinforcement Learning from Human Feedback (RLHF) is a powerful technique for aligning large language models (LLMs) with human preference. However, it often suffers from the reward hacking issue, where policy optimization improves the proxy reward model while actually degrading performance with respect to the true human preference, due to the imperfection of the proxy. To address this, we propose Reward Model Boosting (RMB), a novel approach that enhances the robustness and reliability of the re...
  </details>


### 📂 robustness
*鲁棒性与可靠性 / Robustness & Reliability* — 58 papers

- **2026-09-28** — Sidharth Pulipaka, Ansh Sharma, Stanislau Hlebik et al. — [Share-Borne AI Virus: Memory-Hopping Attacks Across LLM Agents](http://arxiv.org/abs/2609.35576v1)
  <details><summary>📄 Abstract</summary>
  Large language models are increasingly deployed as stateful assistants that retain information across interactions and use tools to read, modify, and create persistent artifacts. As these artifacts are shared between users, they form an indirect communication channel between otherwise independent assistants. We study a failure mode in which this channel enables self-propagating attacks. We introduce artifact-mediated propagation, where adversarial content introduced through an artifact (e.g. a r...
  </details>

- **2026-09-28** — Kseniya Belousova, Anna Konanykhina, Zilya Murzina et al. — [Physics-informed self-supervised generation of digital brain MRI phantoms from weighted images using differentiable MRI simulation](http://arxiv.org/abs/2609.35273v1)
  <details><summary>📄 Abstract</summary>
  Purpose: To develop a physics-informed, self-supervised framework for generating digital brain MRI phantoms directly from conventional weighted MR images without requiring ground-truth parametric maps or anatomical segmentation. Methods: The framework predicts T1, T2, and proton density (PD) maps from T1-, T2-, and PD-weighted images and reconstructs the input images through an MRI signal model. Three generative architectures (variational autoencoder (VAE), generative adversarial network (GAN), ...
  </details>

- **2026-09-28** — Victor L. Qin, Nicolas Lanzetti, Saverio Bolognani et al. — [Strategically Robust Game-Theoretic Multi-Agent Trajectory Optimization](http://arxiv.org/abs/2609.35142v1)
  <details><summary>📄 Abstract</summary>
  Aviation authorities worldwide expect Advanced Air Mobility (AAM) traffic management to be decentralized among service providers, requiring AAM flights to autonomously plan trajectories by predicting other flights' control inputs rather than relying on centralized coordination. Game-theoretic approaches that formulate multi-agent collision avoidance as an exact dynamic potential game can efficiently find open-loop equilibria, but they assume that agents exactly follow their equilibrium trajector...
  </details>

- **2026-09-28** — Haoyang Zou, Yao Wang, Jun Yao et al. — [LoRo-Mark:Provably Lossless and Robust Agent Watermarking](http://arxiv.org/abs/2609.34080v1)
  <details><summary>📄 Abstract</summary>
  As LLM agents are increasingly deployed as commercial services, protecting proprietary orchestration logic and tool-use policies is important. We consider agent repackaging: an adversary integrates a protected agent into its own application via API and presents it under its own identity. It may modify parts of execution to obscure the source. The owner typically has only black-box access to the repackaged service, so black-box ownership verification is essential. Agent watermarking embeds owners...
  </details>

- **2026-09-28** — Zhilin Guo, Boqiao Zhang, Oszkár Urbán et al. — [Reliability-Gated Fusion of Consumer Head and Foot IMUs for Lower-Body 3D Pose](http://arxiv.org/abs/2609.35764v1)
  <details><summary>📄 Abstract</summary>
  Sparse inertial pose estimation promises camera-free motion capture from consumer devices, but consumer sensors are unreliable: firmware-fused orientations are biased, mounting varies between sessions, and streams drift or drop out. On a new 35-take single-subject benchmark pairing an earbud head inertial measurement unit (IMU) with two smart-insole foot IMUs (SAM-3D-Body pseudo-ground-truth labels), we show the reliability problem is channel-level: a channel ablation isolates foot acceleration ...
  </details>

- **2026-09-28** — Tianjian Liu, Shicheng Feng, Jin'ao Shang et al. — [LLM-Assisted Automatic Security Proofs for Cryptographic Protocols: How Far Are We?](http://arxiv.org/abs/2609.35434v1)
  <details><summary>📄 Abstract</summary>
  Large language models (LLMs) have shown strong potential for assisting software and security analysis tasks, yet their effectiveness in cryptographic symbolic protocol verification remains insufficiently understood.   In this paper, we conduct the first systematic evaluation of the capability of state-of-the-art LLMs in cryptographic symbolic protocol verification. To quantify this capability, we propose \textsc{CRoST} (Coverage Rate of Solve Tree), a proof-based metric derived from the verifier...
  </details>

- **2026-09-28** — Julianna Piskorz, Antonin Berthon, Mihaela van der Schaar — [On-Policy or Off-Policy Learning? A Systematic Study of Distillation Dynamics](http://arxiv.org/abs/2609.35259v1)
  <details><summary>📄 Abstract</summary>
  On-policy learning has been argued to reduce catastrophic forgetting, produce sparser parameter updates, and improve generalisation. However, existing comparisons between supervised fine-tuning and reinforcement learning vary many factors simultaneously, making the contribution of rollout policy difficult to isolate. We study the effect of rollout policy in a controlled strong-to-weak distillation setting, by independently varying rollout policy, token-level KL direction, and learning rate acros...
  </details>

- **2026-09-28** — Di Zhu, Ziheng Yan, Fang Wan — [ActionUNet: Improving Robustness of VLA Models with Efficient Multi-scale Fine-tuning](http://arxiv.org/abs/2609.34982v1)
  <details><summary>📄 Abstract</summary>
  Vision-Language-Action (VLA) models have shown great promise for robotic manipulation by mapping multi-modal semantics to physical actions. However, this mapping inherently struggles to align these coarse-grained semantics with fine-grained temporal execution. It leaves VLA models with limited generalization and insufficient robustness in cluttered environments. To overcome this issue, we propose ActionUNet, an efficient multi-scale fine-tuning framework that enhances pre-trained VLA models with...
  </details>

- **2026-09-28** — Erik Aerts — [Applying Language Models in medical Medicine: Recent Trends and Perspectives](http://arxiv.org/abs/2609.34780v1)
  <details><summary>📄 Abstract</summary>
  The use and applicability of artificial intelligence (AI) in medical research and clinical practice has received increasing attention in the literature over recent years. The emergence of large language models (LLMs) has expanded discussions in regards to applications of AI within healthcare. While traditional deep learning based AI applications in medicine have often focused on specific and defined tasks, LLMs offer broader capabilities and flexibility in working with available data,. At the sa...
  </details>

- **2026-09-28** — Hai Duong, Thanh Le, ThanhVu Nguyen — [ZonoGPT: Towards An Abstract Domain for Verifying Large GPT Models](http://arxiv.org/abs/2609.34457v1)
  <details><summary>📄 Abstract</summary>
  Transformer-based models are widely used for reasoning, coding, and multimodal agentic tasks. To provide formal assurance of desirable behaviors, such as robustness, safety, and fairness, neural network verification techniques prove required properties and provide auditable guarantees before deployment. However, prior work remains limited to small or restricted Transformers, and maintaining precision across deep models remains challenging. In this work, we introduce ZonoGPT, an abstract domain f...
  </details>

- **2026-09-28** — Xianbo Cai, Hideyuki Ichiwara, Zihang Wang et al. — [TLC-DiT: Task-Aligned Local Visual Conditioning for Robust Multitask Robot Manipulation](http://arxiv.org/abs/2609.34297v1)
  <details><summary>📄 Abstract</summary>
  Language-conditioned robot policies have made clear progress in multitask manipulation, but task-relevant local visual evidence usually stays hidden inside a visual backbone or attention layers. This leaves the policy difficult to inspect and fragile under visual change, two symptoms of a missing explicit, task-aligned local visual channel. We present TLC-DiT, a plug-in extension of the Multitask Diffusion Transformer (DiT) policy that adds explicit task-guided local visual feature maps without ...
  </details>

- **2026-09-28** — Tanmoy Kanti Halder, Akash Ghosh, Arijit Roy et al. — [GenoMorph: Pathway-Grounded Genomic Disease Reasoning via Adaptive Latent Computation](http://arxiv.org/abs/2609.34079v1)
  <details><summary>📄 Abstract</summary>
  Large language models (LLMs) have demonstrated strong capabilities in biological reasoning; however, genomic disease inference remains largely dependent on memorized gene-disease associations rather than understanding biological pathways. This shortcut learning undermines robustness and generalization, and breaks down when molecular identifiers are unavailable. We present GenoMorph, a multimodal genomic reasoning framework that shifts disease prediction from associative gene-disease mapping towa...
  </details>

- **2026-09-28** — Steven T Flammia, Savar D Sinha, Yu Tong — [Gauge freedom and efficient algorithms for Lindbladian learning](http://arxiv.org/abs/2609.35265v1)
  <details><summary>📄 Abstract</summary>
  We study the problem of learning a local Lindbladian in the presence of state-preparation-and-measurement (SPAM) noise. Although recent work has developed scalable learning algorithms under idealized access assumptions, SPAM can make distinct Lindbladians experimentally indistinguishable, thus making part of the Lindbladian fundamentally unlearnable. We give a sharp characterization of this obstruction for bounded-degree local Lindbladians. We identify a family of locality-preserving gauge trans...
  </details>

- **2026-09-28** — Zhuoyuan Yu, Jiacheng Wang, Tianle Liu et al. — [F4R: Failure-Driven Recognition, Reconstruction, Refinement, and Redeployment for Continual Robot Self-Improvement](http://arxiv.org/abs/2609.35575v1)
  <details><summary>📄 Abstract</summary>
  The real-world performance of current vision-language-action models is fundamentally constrained by the limited coverage of expert demonstrations and their insufficient understanding of physical interactions. A common remedy is to collect additional real-world demonstrations of newly encountered failures. However, this process is costly, inefficient, potentially unsafe, and difficult to scale. To address this challenge, we propose Failure for Rising (F4R), a failure-driven real-to-sim-to-real cl...
  </details>

- **2026-09-28** — Hanxun Huang, Yutao Wu, Qizhou Wang et al. — [VEX-Bench: Benchmarking Verification Complexity of LLM-Generated Misinformation](http://arxiv.org/abs/2609.35028v1)
  <details><summary>📄 Abstract</summary>
  Large language models (LLMs) have made misinformation inexpensive to produce but not to verify, creating a growing asymmetry in the information ecosystem. Under tight time, labor, and budget constraints, media organizations, platforms, and fact-checkers rely on screening to prioritize which content to verify. We introduce VEX-Bench, a unified benchmark for evaluating the verification complexity of LLM-generated misinformation, as perceived during screening, across models and generation methods. ...
  </details>

- **2026-09-28** — Hongyu Ma, Hairong Qu, Shiqi Zhao et al. — [ESTHER: Egocentric Stereo Hand Estimation and Reconstruction in the Wild](http://arxiv.org/abs/2609.34817v1)
  <details><summary>📄 Abstract</summary>
  Human dexterity is guided by two eyes watching two hands: binocular vision supplies the metric 3D structure that fine-grained manipulation consumes. Egocentric stereo is therefore the natural perceptual interface for robots, AR, and VR-yet metric 3D hand reconstruction from this very signal still has neither an end-to-end model nor an in-the-wild benchmark. We propose ESTHER, a model whose stereo geometry, temporal reasoning, and output representation are designed for wearable egocentric stereo....
  </details>

- **2026-09-28** — Basile Morel, Samuel Ruiperez-Campillo, Andreas P. Streich et al. — [DR-net-Mamba: Selective State-Space Modeling for Long-Range ECG Time-Series Denoising](http://arxiv.org/abs/2609.35634v1)
  <details><summary>📄 Abstract</summary>
  Electrocardiogram (ECG) recordings are corrupted by non-stationary noise sources that degrade diagnostic reliability, particularly in ambulatory and long-duration recordings. Deep learning denoisers exist, but convolutional architectures are limited by their receptive field, transformer-based models scale quadratically with sequence length, and diffusion-based approaches incur prohibitive inference cost. We propose a Mamba-augmented model that inserts selective state-space blocks at the convolut...
  </details>

- **2026-09-28** — Yongda Wei, Chen Zhang, Yifei Wang et al. — [What Paired Evaluations Reveal under Visual Perturbations](http://arxiv.org/abs/2609.35583v1)
  <details><summary>📄 Abstract</summary>
  Robustness evaluation must examine diverse visual perturbations, while benchmarks cover only some real-world conditions and physical testing is costly. Paired evaluations link clean and perturbed predictions for the same image, capturing changes in correctness, confidence, and acceptance beyond aggregate accuracy. We investigate how this image correspondence supports two needs in robustness evaluation: interpreting paired evaluation results and prioritizing samples for physical testing. To inter...
  </details>

- **2026-09-28** — Pranav Gupta — [QC-Stark: A Multi-Task Benchmark Revealing Capability Dissociations in LLMs Evaluated on Quantum Computing Tasks](http://arxiv.org/abs/2609.35581v1)
  <details><summary>📄 Abstract</summary>
  We introduce QC-Stark, a benchmark for evaluating large language models (LLMs) on 11 quantum computing (QC) tasks, spanning circuit construction, debugging, compilation, error correction, and simulation. Across 2,750 evaluations (10 models $\times$ 11 tasks x 5 difficulty levels x 5 seeds), we find that overall rankings mask substantial per-task variation. The Spearman correlation between overall and per-task rankings is statistically insignificant for 4 out of the 11 tasks included in this benc...
  </details>

- **2026-09-28** — Vahagn Grigoryan, Donato Romano, Cesare Stefanini et al. — [Positional choice and robust collective behavior in fish schools: biohybrid experiments and modeling](http://arxiv.org/abs/2609.35554v1)
  <details><summary>📄 Abstract</summary>
  Collective behavior of fish schools is usually modeled on the assumption that each individual follows specific rules of motion that depend on its position and velocity relative to its neighbors. Although these models reproduce many schooling patterns observed in nature, it remains unclear whether the assumed rules are realistic at the individual level. To address this question, we first analyzed a set of experiments in which a live fish interacted with four moving robotic fish in a tank, and mea...
  </details>

- **2026-09-28** — Peilin Feng, Zhengyang Huang, Soujanya Poria — [BaRe-Mem: Bayesian Reliability Memory for Robust and Adaptive Agent Consultation](http://arxiv.org/abs/2609.35551v1)
  <details><summary>📄 Abstract</summary>
  In multi-agent systems, reliable consultation is challenging because advisor capabilities vary across tasks, and misleading information can make consultation worse than autonomous reasoning. We introduce BaRe-Mem, an online Bayesian reliability memory for multi-agent consultation. It estimates advisor reliability based on the central model's internal belief representations and updates these estimates from historical interactions. These estimates modulate the influence of advisor responses and gu...
  </details>

- **2026-09-28** — Xiao Zhang, Wang Zeng, Sheng Jin et al. — [Rethinking Visual Token Compression for Video Large Language Models: A Simple Yet Strong Baseline](http://arxiv.org/abs/2609.35394v1)
  <details><summary>📄 Abstract</summary>
  Video Large Language Models (Video LLMs) have achieved remarkable progress in video understanding, but their inference efficiency is constrained by the large number of visual tokens produced by long videos. Recent video token compression methods increasingly introduce sophisticated strategies for token selection, pruning, and merging. This raises a fundamental question: how much of compression performance can be obtained by simply preserving the structure encoded in the visual representations? W...
  </details>

- **2026-09-28** — Zineddine Tighidet, Andrea Mogini, Jiali Mei et al. — [MemoReason: Evaluating the Effect of Parametric Memory on Contextual Reasoning in LLMs](http://arxiv.org/abs/2609.35312v1)
  <details><summary>📄 Abstract</summary>
  Large Language Models (LLMs) perform well on reasoning benchmarks, but it remains unclear whether this reflects genuine contextual reasoning or reliance on facts memorized in their parameters. We investigate this by distinguishing two possibilities: a broad \textit{memorization bias}, where familiar content improves reasoning performance, and the \textit{Strong Parametric Shortcut Hypothesis}, where models skip reasoning entirely and recall stored answers. To test these effects, we introduce \te...
  </details>

- **2026-09-28** — Huachi Zhou, Yujing Zhang, Jiahe Du et al. — [Towards Reliable AI Data Scientists: Data Agents with Workflow Harnesses](http://arxiv.org/abs/2609.35255v1)
  <details><summary>📄 Abstract</summary>
  Large language model agents are increasingly deployed for data-intensive work, yet reliable data analysis requires more than general-purpose reasoning and ad hoc tool augmentation. Data Agents, equipped with workflow harnesses, offer a promising paradigm for automating the end-to-end data science lifecycle. This paper examines Data Agents from a harness-centric perspective. First, we introduce a taxonomy of Data Agents and associated data environments, organizing the literature around five funct...
  </details>

- **2026-09-28** — Yuanzi Li, Xueyang Feng, Junhao Wang et al. — [Adaptive Resource Allocation for Effective and Efficient LLM Social Survey Simulation](http://arxiv.org/abs/2609.35216v1)
  <details><summary>📄 Abstract</summary>
  Large Language Models (LLMs) enable scalable social survey simulation, yet existing pipelines typically use the same strong general-purpose model and a fixed, often large, respondent history for every respondent-question request. This uniform approach overlooks three factors. First, stronger models may rely on their own knowledge rather than respondent-specific evidence while costing more. Second, additional history can help when evidence is limited, but irrelevant responses may add noise and in...
  </details>

- **2026-09-28** — Zhilin Guo, Boqiao Zhang, Oszkár Urbán et al. — [One Sensor, Whole Body - 3D Body Pose from a Single Consumer Earbud IMU](http://arxiv.org/abs/2609.34978v1)
  <details><summary>📄 Abstract</summary>
  Consumer earbuds already stream inertial motion data from the head, one of the most widely worn sensor locations on the body. We ask how much of the 3D body pose a single such head IMU can recover, and whether adding more consumer sensors actually helps. We build a multimodal capture pipeline that records four-view RGB-D video together with an AirPods head IMU and two Striv insole IMUs, synchronize the streams post-hoc, and generate pseudo-ground-truth with SAM 3D Body, yielding a 35-take single...
  </details>

- **2026-09-28** — Jeongsol Kim, Youngjun Jun, Kyumin Choi et al. — [Adjoint Guidance Flow: Amortized Critic Guidance for VLA Policies](http://arxiv.org/abs/2609.34944v1)
  <details><summary>📄 Abstract</summary>
  Flow-based Vision-Language-Action (VLA) policies are typically trained by behavior cloning and thus do not explicitly optimize long-term task return. Critic guidance steers generation toward higher-value actions, but existing methods differentiate the critic through a one-step surrogate of the sampler and back-propagate a critic ensemble at every flow step. In contrast, here we propose Adjoint Guidance Flow (AGF), which amortizes trajectory-aware critic guidance into a lightweight guidance netwo...
  </details>

- **2026-09-28** — Zehui Wu, Jian Yu, Jian-Song Pan — [Spontaneous breaking of continuous scale invariance and Efimovian-like dynamics in a driven-dissipative harmonic oscillator](http://arxiv.org/abs/2609.34926v1)
  <details><summary>📄 Abstract</summary>
  The Efimov effect manifests discrete scale invariance through a geometric series of three-body bound states. Analogous discrete scale symmetry has been observed in the Efimovian expansion of scale-invariant strongly interacting Fermi gases. However, it is unclear whether strong correlation is necessary. Here we investigate the spontaneous breaking of continuous scale invariance in a simple driven-dissipative harmonic oscillator whose driving and dissipation parameters scale as $1/t$. By transfor...
  </details>

- **2026-09-28** — Lukas Koch Vindbjerg, Qi Zhang, Yury Brodskiy et al. — [Attention-based Hierarchical Variational Information Bottleneck for Robust Multi-Agent Communication under Variable Bandwidth](http://arxiv.org/abs/2609.34860v1)
  <details><summary>📄 Abstract</summary>
  Learning-based multi-agent communication under limited bandwidth does not only require deciding what to communicate, but also structuring messages so that partial transmissions remain useful. We study this problem under prefix truncation, where only the first part of each message is received. To address it, we propose \textbf{AH-VIB}, an attention-based autoregressive variational communication model that combines a variational information bottleneck (VIB) with sequential message generation and a...
  </details>

- **2026-09-28** — An Yan, Yu Huo, Zhiwei Shang et al. — [CEO Arena: Evaluating Long-Horizon Multi-Agent Decision-Making in Competitive Markets](http://arxiv.org/abs/2609.34821v1)
  <details><summary>📄 Abstract</summary>
  Long-horizon competition tests agents' ability to coordinate business decisions under uncertainty and adapt to changing rival strategies. We introduce CEO Arena, a benchmark that uses matched replacement evaluation to assess operating returns alongside an agent's effects on rivals and the market. Each CEO agent is compared with a reference policy in the same company under the same economic seed, holding other agents' identities and assignments fixed while all agents adapt. In a shared eight-comp...
  </details>

- **2026-09-28** — Tao Huang, Wei Zhou — [No Attention, No Problem: Rethinking Session-based Recommendation with Pure Convolution](http://arxiv.org/abs/2609.34802v1)
  <details><summary>📄 Abstract</summary>
  Session-based recommendation (SBR) predicts the next choice in a session by analyzing recent interactions. Transformer-based models are widely used because of their ability to capture long-range dependencies through self-attention mechanisms. In contrast, traditional convolutional models, although more efficient, are often limited by their weak global modeling capabilities and are losing ground in SBR tasks. In this work, we propose a Next-generation Pure Convolutional Framework (NextConvRec) fo...
  </details>

- **2026-09-28** — Gauvain Devillez, Stefania Dumbrava, Angela Bonifati — [Transformations for Evolving Property Graph Schemas](http://arxiv.org/abs/2609.34789v1)
  <details><summary>📄 Abstract</summary>
  Property graph databases are widely used to represent complex and evolving data; yet, systematic support for property graph schema evolution remains limited. In practice, schema transformations are typically defined manually, coupled to specific application contexts, and are difficult to reuse across schemas or evolution scenarios. We present GRAFT, a logic-based framework that models prop- erty graph schema evolution as reusable, order-constrained meta- transformations derived from atomic edits...
  </details>

- **2026-09-28** — Haonan Zhang, Weihua Wu, Qi Zhang et al. — [Robust Resource Management for SAGIN using DNN-Driven Channel Uncertainty Learning](http://arxiv.org/abs/2609.34728v1)
  <details><summary>📄 Abstract</summary>
  This paper focuses on the joint robust beamforming and resource allocation for space-air-ground integrated networks (SAGIN) under uncertain channel state information (CSI). In SAGIN, uncertain CSI undermines the precise adjustment of beamforming and resource allocation, posing a major challenge to meeting heterogeneous users' strict quality of service (QoS) requirements. To address this challenge, we first formulate a chance-constrained optimization problem to minimize the total transmit power w...
  </details>

- **2026-09-28** — Qiulin Shang, Zhoutong Wu, Jie Hu et al. — [QuantForge: Discovering Residual Decompositions for MXFP4 Post-Training Quantization](http://arxiv.org/abs/2609.34680v1)
  <details><summary>📄 Abstract</summary>
  Four-bit post-training quantization can reduce the memory demands of large language models, but preserving accuracy under strict MXFP4 W4A4 requires coordinating several design choices. Coordinate transforms change block-encoding errors, which in turn affect the residuals propagated through the network. The useful algorithmic decomposition is therefore not fully known before search. LLM-driven program evolution offers a way to explore these choices, but performance scores alone do not explain wh...
  </details>

- **2026-09-28** — Xiaoting Lyu, Xinbo Ma, Yufei Han et al. — [The Marathon of Scientific Reasoning: Robustness of Scientific Agents to Perturbations in Multi-Turn Interactions](http://arxiv.org/abs/2609.34537v1)
  <details><summary>📄 Abstract</summary>
  Large language model (LLM)-based scientific agents are increasingly used for scientific problem solving, yet their robustness to imperfections arising during multi-turn interactions remains poorly understood. We introduce \textsc{SciARP} (\textbf{Sci}entific \textbf{A}gent \textbf{R}obustness to \textbf{P}erturbations), a benchmark for evaluating scientific agents under scientifically plausible perturbations throughout multi-turn problem solving. \textsc{SciARP} transforms 620 scientific problem...
  </details>

- **2026-09-28** — Shihao Zhang, Weiting Liu, Siyu Shao et al. — [LLMs as Adaptive Meta-Solvers: Strategy-Diverse RL for Industrial-Scale Optimization](http://arxiv.org/abs/2609.34427v1)
  <details><summary>📄 Abstract</summary>
  Scaling LLM-based optimization from textbook-scale instances to real-world, industrial tasks remains a critical open challenge. Existing approaches are predominantly evaluated on small, self-contained textual problems and often commit to a solver-integrated paradigm, limiting their ability to handle the scale and structural diversity of practical optimization workloads. In this work, we propose a practical framework for training open-source LLMs to tackle real-world, industrial-scale optimizatio...
  </details>

- **2026-09-28** — Suhwan Choi, Myeongho Jeon, Myungjoo Kang — [Zero-Shot Cue-Grounded Topic Segmentation of Spoken Documents](http://arxiv.org/abs/2609.34425v1)
  <details><summary>📄 Abstract</summary>
  Topic segmentation structures spoken documents into coherent sections, facilitating navigation and downstream understanding. The appropriate granularity can vary substantially, ranging from broad thematic shifts to fine-grained subtopics. Existing LLM-based segmenters, however, often struggle to adapt to this variation, causing them to either merge distinct subtopics or over-segment coherent themes. To address this, we introduce Cue-Grounded Segmentation (CGS), a training-free framework that ope...
  </details>

- **2026-09-28** — Ryoga Yuzawa, Tasuku Takagi — [HyperDAM: Hyperspectral Distractor-Aware Memory with Amodal Expansion for SAM 3 Tracking](http://arxiv.org/abs/2609.34396v1)
  <details><summary>📄 Abstract</summary>
  Hyperspectral video provides material cues that can disambiguate targets with similar false-color appearance, yet foundation-model trackers update memory primarily from spatial and appearance evidence. We present HyperDAM, a DAM4SAM3-based hyperspectral tracker with three principal contributions. First, HOTC2026-Modal adds human-verified frame-wise modal masks and mask-tight boxes to all 481 organizer-provided HOTC 2026 videos. Second, a frame-zero-calibrated HSI gate rejects spectrally inconsis...
  </details>

- **2026-09-28** — Yifan Lu, Qiyue Zhang, Haotian Shan et al. — [Routing Without Embeddings: Fast And Interpretable Routing With Regular Expressions](http://arxiv.org/abs/2609.34326v1)
  <details><summary>📄 Abstract</summary>
  Large Language Model (LLM) routers commonly rely on neural query embeddings, with larger encoders expected to better capture query intent and difficulty. Yet scaling Qwen2.5 encoders from 0.5B to 72B parameters brings little improvement in routing accuracy (Figure 1b), suggesting that small encoders may already capture the query properties needed for routing. We therefore investigate which properties matter and whether they can be extracted directly from text without a neural encoder. We introdu...
  </details>

- **2026-09-28** — Yuyang Deng, Yu Wang, Jiayun Wang — [Direct Self-Evolving Optimization: Evolving LLMs without Challenger Training](http://arxiv.org/abs/2609.34279v1)
  <details><summary>📄 Abstract</summary>
  Self-evolving language models improve by generating tasks and learning from their own feedback, but adapting the task generator often requires a separate challenger-training loop. Can we generate tasks adapted to the current solver without explicitly training a challenger? We introduce \textbf{D}irect Self-\textbf{E}volving \textbf{O}ptimization (DEO), which replaces challenger parameter updates with solver-guided task sampling. The KL-regularized challenger objective defines an exponential tilt...
  </details>

- **2026-09-28** — Xiaoye Liang, Ye Yan, Mingze Yin et al. — [SegBanana: Steering Unified Multimodal Models into Medical Segmenters](http://arxiv.org/abs/2609.34235v1)
  <details><summary>📄 Abstract</summary>
  Medical image segmentation remains challenging in practical deployment, as models often struggle to generalize beyond the distributions covered by their training data and high-quality pixel-level annotations are typically unavailable for adaptation. Inspired by the cross-task transferability of large language models, we investigate whether unified multimodal models (UMMs) can transfer their pretrained visual understanding, reasoning, and generation capabilities to medical image segmentation with...
  </details>

- **2026-09-28** — Yingbo Zhao, Zeyu Yang, Zhoufan Zhu — [AlphaPareto: Formulaic Alpha Discovery with LLM-Guided Multi-Objective Reinforcement Learning](http://arxiv.org/abs/2609.34188v1)
  <details><summary>📄 Abstract</summary>
  Formulaic alpha discovery is a core challenge in quantitative trading, as identifying alphas that work well together remains difficult. Recent reinforcement learning (RL) methods formulate this task as a Markov decision process (MDP), but two important issues remain unresolved. First, as the alpha pool evolves, the reward function changes accordingly, making the MDP inherently non-stationary. Second, most existing methods optimize a single objective, typically predictive power, while ignoring ot...
  </details>

- **2026-09-28** — Tien Tran, Namho Koh, Daiki E. Matsunaga et al. — [Same Tasks, Different Apps: Why Mobile GUI Agents Fail to Generalize?](http://arxiv.org/abs/2609.34139v1)
  <details><summary>📄 Abstract</summary>
  Mobile GUI agents deployed in real settings must work across different applications that support the same functionality. Most existing benchmarks test each task in only one app, so a high score can mean the agent understands the task, or only that it knows that particular app. We introduce AnyAppBench, a category-controlled live Android benchmark that evaluates cross-application generalization while keeping the user goal fixed. It spans 10 functional categories, 100 task templates, and 520 task-...
  </details>

- **2026-09-28** — Lovely Yeswanth Panchumarthi, Andrew Lu, Saurabh Kataria et al. — [TRACE: Expert-Aligned ECG Representation Learning with Rigorous Benchmarking and Real-World Validation in Acute Cardiac Care](http://arxiv.org/abs/2609.34088v1)
  <details><summary>📄 Abstract</summary>
  TRACE (Text-Reinforced Analysis of Cardio ECGs) is a multimodal electrocardiogram (ECG) representation model that learns clinically grounded signal embeddings for downstream cardiac classification. It is designed to address the limitations of existing CLIP-style training, which often struggles with noisy clinical text and fails to leverage the complementary strengths of unimodal (from ECG) and cross-modal (between ECG and matched cardiologist reports) learning. To bridge this gap, we propose a h...
  </details>

- **2026-09-28** — Pengxin Wang, Yuanzhe LI, Yuxin Ren et al. — [Learning Perturbation Robust Policies for LLM Agents with Stable Optimization](http://arxiv.org/abs/2609.34064v1)
  <details><summary>📄 Abstract</summary>
  Reinforcement learning (RL) has become an effective post-training paradigm for long-horizon large language model (LLM) agents. However, we find that the resulting policies can be sensitive to various policy perturbations, such as hidden-state noise, pruning, and quantization. In this work, we study how to improve perturbation robustness during policy optimization. We first introduce the notion of a perturbation robust policy and analyze conditions under which perturbed policy updates preserve st...
  </details>

- **2026-09-27** — Futa Waseda, Shuhei Kurita, Isao Echizen — [Does Adversarial Training Improve Generalization in Multi-View VLAs? Revealing and Mitigating View Collapse](http://arxiv.org/abs/2609.33707v1)
  <details><summary>📄 Abstract</summary>
  Vision-language-action (VLA) models adapt pretrained vision-language models (VLMs) for closed-loop robot control, transferring their perceptual and semantic capabilities to action prediction. Despite strong in-distribution performance, however, VLAs often degrade under deployment shifts. Adversarial training (AT) offers a model-adaptive approach to robustness without explicitly anticipating individual shifts, but its effect on natural distribution-shift generalization in multi-view VLAs remains ...
  </details>

- **2026-09-27** — Hong Xi Tae, Jiaming Zhang, Wenwen He et al. — [Concept Score Relearning: A Unified Cross-Architecture Attack on Concept Erasure](http://arxiv.org/abs/2609.33445v1)
  <details><summary>📄 Abstract</summary>
  Concept erasure aims to suppress undesirable knowledge in text-to-image generative models. However, existing robustness evaluations typically rely on relearning attacks tailored to specific model architectures. We study concept reactivation across two substantially different generative paradigms: noise-prediction U-Nets and flow-matching Transformers. We introduce \textbf{Concept Score Relearning (CSR)}, a unified parameter-level framework that reactivates erased concepts by optimizing each mode...
  </details>

- **2026-09-27** — Shambhavi Mishra, Omprakash Chakraborty, Julio Silva-Rodriguez et al. — [Test-Time Generalized Category Discovery](http://arxiv.org/abs/2609.33937v1)
  <details><summary>📄 Abstract</summary>
  Test-Time Adaptation (TTA) and Generalized Category Discovery (GCD) are traditionally treated as disjoint problems: the former adapts models to domain shift assuming all test classes are known, while the latter discovers novel categories assuming labeled training data for known classes. However, real-world deployment rarely fits either setting. Motivated by this gap, we introduce Test-Time Generalized Category Discovery (TT-GCD), a unified and more realistic scenario where a vision-language mode...
  </details>

- **2026-09-27** — Priyanath Maji, Sidharth Gaur, Rajavinoth Paul Durai — [Beyond Fixed Features: Architecture-Dependent Sensitivity to Node Representations under Heterophily](http://arxiv.org/abs/2609.33764v1)
  <details><summary>📄 Abstract</summary>
  Graph Neural Networks (GNNs) perform well on homophilic graphs but struggle in heterophilic settings, where connected nodes often carry dissimilar labels. Existing evaluations typically compare architectures under a fixed node-feature representation, leaving unclear whether conclusions about heterophily robustness remain stable as the input representation changes. We address this question by constructing parallel feature variants of two large-scale heterophilic benchmarks, Roman-Empire and Amazo...
  </details>

- **2026-09-27** — Jingyi He, Nier Wu, Shuang Liu et al. — [RewardExplainer: Learning Reward Model Explanations from Counterfactual Preference Feedback](http://arxiv.org/abs/2609.33989v1)
  <details><summary>📄 Abstract</summary>
  Reward models (RMs) are a key component of large language model post-training, providing reward signals for subsequent reinforcement learning. However, conventional discriminative RMs typically output only scalar scores, making it difficult to identify the response behaviors associated with their scoring decisions. Existing interpretation methods often rely on predefined high-level attributes and require repeated counterfactual interventions for each response pair to validate candidate explanati...
  </details>

- **2026-09-27** — Chia-Hsiang Kao, Belinda Zeng, Bharath Hariharan et al. — [Video, Ergo Genero: Unifying Video Tasks via Spatiotemporal Analogy](http://arxiv.org/abs/2609.33935v1)
  <details><summary>📄 Abstract</summary>
  Adapting video models to new tasks typically requires dedicated data curation and fine-tuning. While visual analogy provides a training-free alternative by specifying tasks in-context, it remains restricted to the image domain. To explore whether analogy-based methods can unify diverse video tasks and generalize to out-of-distribution scenarios, we introduce ViGeo, a framework that extends visual in-context learning to the video domain via spatiotemporal canvas completion. Evaluated on a diverse...
  </details>

- **2026-09-27** — Sichao Liu, Zekun Wang, Lixuan Tang et al. — [Robot-GST: geometry-aware spatial-temporal robot policy representation and evaluation](http://arxiv.org/abs/2609.33872v1)
  <details><summary>📄 Abstract</summary>
  Robotic manipulation policies are advancing rapidly with increasing reliance on vision-language models for end-to-end decision making. However, reliable deployment remains challenging because many policies lack explicit mechanisms for predicting task outcomes and evaluating whether generated actions will achieve desired final states, causing execution errors to accumulate during long-horizon manipulation. We present Robot-GST, a geometry-aware spatio-temporal behaviour representation and evaluat...
  </details>

- **2026-09-27** — Namai Chandra, Madhur Thareja, Shriram Damodaran et al. — [ActionGround: Training-Free Runtime Refinement of Frozen VLA Policies](http://arxiv.org/abs/2609.33256v1)
  <details><summary>📄 Abstract</summary>
  Vision-Language-Action (VLA) models map visual observations and language instructions directly to robot actions, but they do not explicitly represent the phase structure of manipulation tasks or the rigid-body dynamics governing execution. We present ActionGround, a neuro-symbolic, training-free runtime layer that wraps a frozen VLA policy without retraining, fine-tuning, or weight access, adding less than 1 ms of overhead per control step. A symbolic phase-aware finite-state machine identifies ...
  </details>

- **2026-09-27** — Yuyang Zhao, Xuan Liu, HaoYang Shangm Haojian Jin — [Where Do Test-Time Scaling and Training Fall Short in Individual Stance Prediction?](http://arxiv.org/abs/2609.33155v1)
  <details><summary>📄 Abstract</summary>
  Test-time scaling and post-training have improved LLM performance in coding and mathematical reasoning, but their effectiveness for individual stance prediction remains unclear. We study this question by predicting a person's stance in a new discussion from their history. We evaluate widely used test-time scaling strategies and post-training methods, such as supervised fine-tuning and reinforcement learning, and identify four failure modes across generation, selection, and learning: (1) incorrec...
  </details>

- **2026-09-27** — Rajat Modi, Priyank Pathak, Xin Liang et al. — [Position Aware Layer Queries for Test Time Training in Vision Language Models](http://arxiv.org/abs/2609.34021v1)
  <details><summary>📄 Abstract</summary>
  Test-Time Training (TTT) adapts models to incoming test samples (e.g. out-of-distribution, (OOD)) when conventional fine-tuning is infeasible. Existing TTT methods for Vision-Language Models (VLMs) create supervision from several augmented views, each requiring forward (and often backward) passes through the entire VLM, incurring substantial computational cost. We observe that one forward pass with all the intermediate layer outputs already yields far more signal than the final embedding from al...
  </details>

- **2026-09-27** — Tong Liu, Lanmiao Liu, Xiang Hu — [RICE-Alpha: Reliability-Informed Correction with Event Graphs for LLM-Agent Stock Forecasting](http://arxiv.org/abs/2609.34004v1)
  <details><summary>📄 Abstract</summary>
  Equity-relevant news evolves through temporally dependent corporate events, making historical information useful only when event continuity, information availability, and transition reliability are modeled. Existing LLM-based financial agents incorporate historical evidence, yet they provide limited support for preserving issuer-specific chronology under point-in-time constraints and for identifying when historical transitions contribute information beyond the current forecast. We present RICE-A...
  </details>

- **2026-09-26** — Yi Tang, Tengxue Zhang, Yang Shu et al. — [SIFT: Enhancing Time Series Foundation Models via Semantic Invariance and Structural Fidelity Fine-Tuning](http://arxiv.org/abs/2609.32676v1)
  <details><summary>📄 Abstract</summary>
  Time Series Foundation Models (TSFMs) have achieved remarkable zero-shot performance through extensive pre-training on massive time series datasets. Nevertheless, due to the low-dimensional properties and diverse structural patterns of time series data, performing naive fine-tuning on TSFMs often leads to overfitting and falling into the mean-prediction trap. To address these challenges, we propose SIFT, a robust adaptation method that enhances time series foundation models by preserving Semanti...
  </details>

- **2026-09-26** — Cristina V. Lopes, Yuangang Li, Justin Tian Jin Chen et al. — [The Geometry of Logic: Stratification Induces Semantic Structure and Robust Reasoning](http://arxiv.org/abs/2609.32927v1)
  <details><summary>📄 Abstract</summary>
  Transformer-based language models perform well on symbolic tasks, yet it remains unclear whether they learn generalizable rules or rely on statistical shortcuts. Mechanistic studies link algorithmic behavior to structured internal representations, motivating the hypothesis that robust reasoning benefits from separating values from the types that control their manipulation. Can making this separation an architectural primitive improve the learnability and generalization of logical mechanisms? We ...
  </details>


### 📂 watermark
*水印与溯源 / Watermarking & Provenance* — 10 papers

- **2026-09-28** — Niklas Koenen, Claudia Battistin, Jeriek Van den Abeele et al. — [A Hierarchy of Entropy-Shapley Games for Multivariate Predictive Uncertainty](http://arxiv.org/abs/2609.35217v1)
  <details><summary>📄 Abstract</summary>
  Modern probabilistic machine learning models increasingly produce multivariate outputs with complex dependence structure, from multi-step time-series forecasts to sample path predictions. Understanding which input features drive the predictive uncertainty is important for risk-aware decisions, model diagnostics, and deciding whether the uncertainty should be mitigated or hedged against. This attribution problem requires a choice of how dependencies between output components are treated. Existing...
  </details>

- **2026-09-28** — Geonwoo Kim, Brent ByungHoon Kang — [When Valid Tool Calls Change Meaning: Formation-Consistent Dispatch for LLM Agents](http://arxiv.org/abs/2609.35088v1)
  <details><summary>📄 Abstract</summary>
  Tool-enabled agents form calls from model-visible interfaces, while hosts later select their implementation. Standard dispatch omits the descriptor-handler relation. An unchanged and schema-valid call can therefore acquire a different security effect during rollout, reconnect, or delayed approval. We call this failure schema-epoch drift. We present formation-consistent dispatch (FCD), which connects implementation analysis to execution authority. Reviewed profiles produce provenance-bound over-a...
  </details>

- **2026-09-28** — Enoal Gesny, Eva Giboulot — [Optimizing and Securing the Modern Watermarking Channel for Images](http://arxiv.org/abs/2609.34744v1)
  <details><summary>📄 Abstract</summary>
  To comply with recent regulations requiring traceable generated content, modern watermarking has adopted multi-bit post-hoc watermarking schemes. These modern designs rest on an encoder-decoder pair implemented as deep neural networks. These models are usually treated as pure black-boxes trained end-to-end, with the noise of the watermarking channel modeled through a fixed set of geometric and valuemetric transforms applied to watermarked images. We argue that this purely empirical approach lead...
  </details>

- **2026-09-28** — Wanqi Zhou, Jiawei Lu, Yang Wang et al. — [Remember by Asking: Retrieval-Induced Memory Evolution for LLM Agents](http://arxiv.org/abs/2609.34438v1)
  <details><summary>📄 Abstract</summary>
  Long-term memory is essential for language agents to maintain coherent and effective behavior over extended, multi-session interactions. Existing memory systems mainly use retrieval at read time, while write-time memory formation still relies on direct extraction or compression. However, when future information needs are unknown, compressing an entire interaction in one pass can overlook locally important details that may matter later. To this end, we introduce RIME, a retrieval-induced memory f...
  </details>

- **2026-09-28** — Luyao Zhuang, Yujing Zhang, Zijin Hong et al. — [Org-Agent: Beyond Personal Assistants Towards Organizational Agents](http://arxiv.org/abs/2609.34392v1)
  <details><summary>📄 Abstract</summary>
  Language model agents serving organizations must coordinate requests from multiple users while using knowledge distributed across their interactions. We identify two complementary capabilities for this setting, namely cross-user interaction and decision-making, as well as cross-user memory and knowledge use. Both capabilities are governed by organizational constraints across three aspects: user identity, authority, and access permissions; the attribution and temporal validity of information; and...
  </details>

- **2026-09-28** — Chidera Biringa, Lucas Yannul, Xiaowen Wang et al. — [Stashbird: Efficient Speaker-Indexed Memory for Conversational Agents](http://arxiv.org/abs/2609.34242v1)
  <details><summary>📄 Abstract</summary>
  AI agents require memory that preserves information across user-agent exchanges, user-to-user conversations, and group conversations with or without agent participation, while supporting updates as evidence changes or is removed. We present Stashbird, an agent memory system that links source episodes to derived memory state through explicit provenance. Stashbird organizes memory into episodic records, semantic relations, community summaries, and persisted graph state, with lifecycle operations f...
  </details>

- **2026-09-28** — Haodong Yang, Mengzhu Chen, Jia Cai — [STITCH-RAG: Spatio-Temporal Influence Tracing over Topic Hypergraphs for Multi-Hop Retrieval-Augmented Generation](http://arxiv.org/abs/2609.34127v1)
  <details><summary>📄 Abstract</summary>
  Multi-hop retrieval-augmented generation requires a retriever to connect evidence distributed across documents while preserving a concise, faithful generation context. Existing indexes leave two complementary gaps: chunk-based RAG can break cross-passage evidence chains, whereas an unlabeled pairwise projection without generating-topic provenance cannot jointly preserve topic-level co-participation and per-occurrence entity descriptions. We propose STITCH-RAG, a hypergraph-based framework with t...
  </details>

- **2026-09-27** — Hao Chen — [MAD-Guard: Controlled Study of Autoregressive Generation versus Direct Decision Interfaces for Closed Multimodal Forensic Tasks](http://arxiv.org/abs/2609.33683v1)
  <details><summary>📄 Abstract</summary>
  When should multimodal foundation models generate tokens, and when should they directly output a decision? We present MAD-Guard, a controlled study of output-decision interfaces for closed multimodal forensic tasks. Once a multimodal representation is computed, is autoregressive generation necessary for closed forensic decisions with high input complexity but low output entropy? Under a matched Qwen3-VL-8B backbone, 2,400 FakeClue training samples, and LoRA budget ($r=16, α=32$) on Huawei Ascend...
  </details>

- **2026-09-27** — Yifan Liu, Praveen Venkateswaran, Abdulhamid Adebayo et al. — [Auditing Agent Actions through Query-Conditioned Attribution](http://arxiv.org/abs/2609.33676v1)
  <details><summary>📄 Abstract</summary>
  LLM agents increasingly take consequential actions through interactions with users, policies, and external tools. Auditing these agents requires automated attribution of realized actions to their historical basis. However, existing attribution formulations do not provide question-specific traces for diverse auditing objectives. Additionally, when access to the acting model is limited (e.g., in API-only deployments), applicable methods commonly rely on costly input perturbations or external LLM a...
  </details>

- **2026-09-26** — Shu-Xun Yang, Yidong Wang, Zhuoer Feng et al. — [From Anomalies to Failures: Constructing Causal Error Graphs for Agentic Trace Diagnosis](http://arxiv.org/abs/2609.32514v1)
  <details><summary>📄 Abstract</summary>
  LLM-driven agents are increasingly deployed in complex applications, where long agentic traces make failures difficult to diagnose. Existing trace diagnosis methods often conflate anomalies, errors, and failures, making diagnostic targets ambiguous; they also lack structured modeling of how causally relevant errors propagate and amplify into final task failures, resulting in unreliable failure attribution. To address these problems, we propose CEG-Agent, a tool-augmented agentic framework for ca...
  </details>


### 📂 unlearning
*机器遗忘 / Machine Unlearning* — 2 papers

- **2026-09-28** — Bardh Prenkaj, Andrea D'Angelo, Davide Mottin et al. — [Causal Routing for Unlearning](http://arxiv.org/abs/2609.34475v1)
  <details><summary>📄 Abstract</summary>
  LLMs cannot forget the way we delete a file. Strangely, we are asked to remove something that was never put anywhere in particular. What the model took from a piece of text is now smeared across billions of weights. Existing methods rewrite all of them to change one thing, and none of them say which part produced that change. To address this, we introduce Causal Routing for Unlearning (CRU) by asking where the concept is expressed in the model and suppressing only that part. One untrained forwar...
  </details>

- **2026-09-27** — Xiongtao Sun, Hui Li, Tiantong Wu et al. — [What Does It Mean to Forget a Person? Individual-Level Unlearning in Vision-Language Models](http://arxiv.org/abs/2609.33481v1)
  <details><summary>📄 Abstract</summary>
  Erasing individual identities from Vision-Language Models (VLMs) is uniquely challenging because personal data is entangled across modalities rather than stored as isolated attributes. However, existing multimodal unlearning benchmarks primarily evaluate attribute-centric forgetting, overlooking the more critical objective of individual-level unlearning: eliminating a model's ability to access, link, and reconstruct target-related information across modalities. To address this gap, we propose ID...
  </details>


### 📂 agent-safety
*Agent 安全框架 / Agent Safety Frameworks* — 1 papers

- **2026-09-28** — Guy Lupo, Nguyen Hung Nguyen, Viet Vo et al. — [Continuous Assurance of Agentic Security Auditors for Software Delivery Decision Gates](http://arxiv.org/abs/2609.35266v1)
  <details><summary>📄 Abstract</summary>
  Large language model (LLM)-based repository auditors are increasingly deployed as security controls within continuous integration (CI) pipelines, where their findings admit, block, or delay software changes. As Agentic Software Development Life Cycle (SDLC) Security Controls, their non-deterministic behaviour changes the evidence, while organisational risk appetite and jurisdictional or data-sovereignty policy change its interpretation. Point-in-time audits therefore cannot maintain current assu...
  </details>


### 📂 survey
*综述与系统化 / Surveys & Systematization* — 2 papers

- **2026-09-28** — Ji Huang, Mengfei Li, Shuai Shao — [Simulating Respondents, Not Single Questions: Coherent Survey Generation with Large Language Models](http://arxiv.org/abs/2609.34828v1)
  <details><summary>📄 Abstract</summary>
  Large language models are increasingly used to simulate response distributions in social surveys. Prior work has achieved accurate population-level simulation for individual questions. Real questionnaires, however, ask each respondent a sequence of related questions. A simulated respondent should show coherent preferences across the whole questionnaire, not merely accurate distributions for isolated items. Existing single-item methods cannot accurately reproduce how the same person answers a com...
  </details>

- **2026-09-28** — Akhlak Mahmood, Janhavi Nistane, Huan Tran et al. — [A roadmap for polymer informatics super-intelligence](http://arxiv.org/abs/2609.34051v1)
  <details><summary>📄 Abstract</summary>
  Polymer informatics has matured from isolated property-prediction studies into an integrated discipline that couples data, models, and decision-making across the polymer design cycle. Yet it still falls short of a true intelligent system capable of inverse design on demand, causal reasoning across chemistry, processing, and performance, and closed-loop autonomous experimentation. This article traces a roadmap toward that goal, grounded in experience developing two complementary agentic and infor...
  </details>


### 📂 other
*其他安全相关 / Other Security-Related* — 180 papers

- **2026-09-28** — Hanbin Zhou, Shangzhe Li, Alexander Braverman et al. — [Provable Benefits of Regularization: Fast Rates for Adversarial Imitation Learning](http://arxiv.org/abs/2609.35698v1)
  <details><summary>📄 Abstract</summary>
  We study adversarial imitation learning (AIL), in which an agent learns to imitate expert demonstrations by optimizing a policy against an adversarial reward that distinguishes expert and learner behavior. Historically, reward regularization and entropy-based policy regularization are key components of empirically successful methods such as GAIL and LS-IQ, yet their finite-sample benefits remain underexplored. We establish fast rates for jointly regularized AIL in finite-horizon Markov decision ...
  </details>

- **2026-09-28** — MohammadHossein Bateni, Zahra Hadizadeh, MohammadTaghi Hajiaghayi et al. — [Optimal Networks for Agentic Information Aggregation](http://arxiv.org/abs/2609.35537v1)
  <details><summary>📄 Abstract</summary>
  We study information aggregation in the networked learning model introduced by Kearns, Roth, and Ryu (SODA 2026). There is a fixed distribution over $d$ features and a common label. Agents learn in topological order on a directed acyclic graph. Each observes a subset of the features and its parents' predictions, fits a linear predictor to minimize mean squared error, and passes only its prediction forward. The global predictor is the best linear predictor using all features. Kearns, Roth, and Ry...
  </details>

- **2026-09-28** — Chengyang Li, Yujie Wan, Shuai Wang et al. — [Memory in the Sky: Low-Altitude Question Answering with Multi-Agent Memory Aggregation](http://arxiv.org/abs/2609.35431v1)
  <details><summary>📄 Abstract</summary>
  This paper studies low-altitude question answering (LAQA), in which distributed unmanned aerial vehicle (UAV) memories are aggregated at a ground server to answer questions about observations over a long horizon. Unlike conventional resource allocation based on sensing, communication, control, or computation metrics, LAQA requires an explicit measure of memory value. We propose a generative adversarial exam (GAE) that uses forward simulation to evaluate memory retrieval and exam scores to quanti...
  </details>

- **2026-09-28** — Ritam Bhaumik, Chun Guo, Xiaoning Guo et al. — [Indistinguishability of Sum of Permutations: A Fourier Analytic Route to Classical and Quantum Security](http://arxiv.org/abs/2609.35421v1)
  <details><summary>📄 Abstract</summary>
  We study classical and quantum indistinguishability of sums of independent random permutations and related transformations from permutations to functions. Let $G$ be a finite abelian group of order $N$, and let $π^k_+(x)=π_1(x)+\cdots+π_k(x)$ for $k\geq2$ independent uniform random permutations of $G$. We give a unified Fourier analytic treatment in which the construction is represented by its probability density and a distinguisher by its acceptance function, with the classical and quantum quer...
  </details>

- **2026-09-28** — Keyi Li, Yihao He, Quanyi Li — [Envy-Free Decompositions of Random Assignments: Settling Four Agents, and What Lies Beyond](http://arxiv.org/abs/2609.35192v1)
  <details><summary>📄 Abstract</summary>
  A random assignment of n indivisible objects to n agents is specified by its assignment matrix and implemented by drawing a deterministic assignment from a Birkhoff-von Neumann decomposition. Kawase et al. observed that the choice of decomposition matters for fairness: a matrix that is envy-free in the sense of stochastic dominance (SD-EF) can be decomposed so that some agent envies another with probability close to 1. They call a decomposition Dec-EF if every agent envies every other agent with...
  </details>

- **2026-09-28** — Benjamin Aminof, Tuan Khai Nguyen, Sasha Rubin — [FONDANT: Strong and Best-Effort Planning via Antichains](http://arxiv.org/abs/2609.35160v1)
  <details><summary>📄 Abstract</summary>
  A classical solution concept in fully observable nondeterministic (FOND) planning, is the strong policy (aka winning strategy in the closely related area of reactive synthesis), i.e., such a policy ensures that the goal is reached in an adversarial environment. When strong policies are not available or there is no evidence that the environment is adversarial, one can resort to best-effort policies, which always exist, and which follow the classic decision-theoretic principle that an agent should...
  </details>

- **2026-09-28** — Jeremy Canale — [DGF-Bench: A Benchmark for Simulating and Auditing Deception Against Multi-Agent Governance Boards](http://arxiv.org/abs/2609.34913v1)
  <details><summary>📄 Abstract</summary>
  Tool-using language-model agents can review enterprise projects as governance boards do: they read the evidence, apply written rules and decide whether the project may proceed. Part of that evidence comes from suppliers and project members with a stake in the decision. DGF-Bench is a benchmark in which a board of agents (specialist gates and a General gate that consolidates their decisions) reviews synthetic dossiers while an attacker plants deceptive content in evidence the organization does no...
  </details>

- **2026-09-28** — Andrew Nguyen, Samson Kempiak, Agrim Gupta et al. — [MINT: Modeling GenAI Impact on Network Traffic](http://arxiv.org/abs/2609.35742v1)
  <details><summary>📄 Abstract</summary>
  Generative AI (GenAI) is becoming a mainstream network workload, yet packet-level simulators lack measure\-ment-driven GenAI traffic models. Currently researchers must approximate GenAI services using traditional sources such as file transfer and video streaming, limiting realistic network evaluation of scheduling and capacity planning. We present MINT, a measurement and modeling framework for GenAI network traffic. Using an isolated net\-work-namespace capture pipeline, we collect client-side t...
  </details>

- **2026-09-28** — Jonathan Light, Christopher Zhang Cui, Jeonghye Kim et al. — [Shockingly Simple Self-retrospection Improves Agentic Models Without RL](http://arxiv.org/abs/2609.35741v1)
  <details><summary>📄 Abstract</summary>
  People learn not only by repeating successful actions, but also by recounting and explaining their experiences, revising their understanding to guide future behavior. Can a language-model agent improve its future actions by training only on explanations of its own experience? We investigate this question by studying Retrospection-Only Fine-Tuning (ROFT), a minimal online procedure designed to isolate the effect of explanation-only training on subsequent behavior. The agent attempts a task, obser...
  </details>

- **2026-09-28** — Kerui Ren, Tao Lu, Linning Xu et al. — [GeoVerse: World-Consistent Novel View Synthesis in Geometric Latent Space](http://arxiv.org/abs/2609.35734v1)
  <details><summary>📄 Abstract</summary>
  Novel view synthesis from sparse images must reconcile faithful reconstruction of observed regions with plausible completion of unseen content, while maintaining world consistency across viewpoints. Existing geometry-based methods preserve observed scene structure but often struggle to complete unseen regions, whereas video generative models offer rich appearance priors but accumulate inconsistencies during sequential view generation. We propose GeoVerse, a framework that synthesizes world-consi...
  </details>

- **2026-09-28** — Ziyao Huang, Zhengkun Rong, Shiyang Qin et al. — [FlowAct-R2: Beyond Talking Avatar via Streaming Multimodal References and Proactive Agent Planning](http://arxiv.org/abs/2609.35728v1)
  <details><summary>📄 Abstract</summary>
  We present FlowAct-R2, a framework for interactive humanoid video generation that combines continuous multimodal control with proactive agent planning. Our method consists of two coupled components. First, a Streaming Multimodal Reference Diffusion Transformer adapts the pretrained Seedance 2.0 Mini reference-to-video backbone to accept rolling action prompts, streaming audio, and dynamically updated image, audio, and video references. Video-driven rotary positional embeddings align reference ch...
  </details>

- **2026-09-28** — Li Zhang, Chuqin Geng, Mark Zhang et al. — [Rethinking Circuit Evaluation: Do Circuits Explain Model Errors?](http://arxiv.org/abs/2609.35686v1)
  <details><summary>📄 Abstract</summary>
  Mechanistic interpretability (MI) aims to explain a model's behaviour through analyzing its internal computations; circuit-based explanations aim to isolate these computations with compact subnetworks validated by ablating the rest of the model. We show that circuits validated this way may fail to recover the underlying mechanism of the model's behaviour by closely reproducing its successful decisions while failing to account for most of its errors. Such explanations should account for the model...
  </details>

- **2026-09-28** — Matteo Musacchio, Juan Cruz Giner Pulero, Isabel Castañeda et al. — [QuanReview: Offline, Auditable Reconciliation of Human and LLM Span Annotations](http://arxiv.org/abs/2609.35685v1)
  <details><summary>📄 Abstract</summary>
  Structured span annotations, such as quantities with their units, uncertainty modifiers, and event classes, are expensive to create and hard to keep trustworthy once language models enter the loop. We present QuanReview, an open-source system for auditing and correcting such annotation layers. QuanReview aligns two annotation streams over the same documents at character level, resolves unambiguous cases by an explicit and logged policy, and routes candidate conflicts to a browser-based adjudicat...
  </details>

- **2026-09-28** — Haofeng Xu, Junwei Su, Lansong Diao et al. — [Reward-Aligned Reweighting for On-Policy Distillation](http://arxiv.org/abs/2609.35517v1)
  <details><summary>📄 Abstract</summary>
  On-policy distillation (OPD) trains a student language model with dense feedback from a stronger teacher on student-generated trajectories. Yet standard OPD weights token-level distillation terms uniformly, implicitly treating local teacher preference as a proxy for correction utility. A decision's task value, however, depends on how the student completes the subsequent reasoning. This mismatch can cause imitation to suppress viable student strategies or reinforce paths the student cannot reliab...
  </details>

- **2026-09-28** — Takashi Furuya, Nicholas H. Nelsen, Frank Cole — [Universal Approximation of Measure-to-Measure Operators by Pushforwards](http://arxiv.org/abs/2609.35483v1)
  <details><summary>📄 Abstract</summary>
  Many learning tasks map an input distribution to an output distribution. A natural way to model such an operator is to transform each input sample using a continuous function that may depend on the entire input distribution, and then take the distribution of the transformed samples. This defines a measure-dependent pushforward model and includes measure-theoretic formulations of transformers. We ask when such models can approximate arbitrary continuous operators between spaces of probability mea...
  </details>

- **2026-09-28** — Chenyu Zhang, Yuhang Cao, Daru Du et al. — [Rethinking Causal Action Tokenization with Conditional Annealing in Flow Matching](http://arxiv.org/abs/2609.35469v1)
  <details><summary>📄 Abstract</summary>
  Autoregressive Vision-Language-Action (VLA) models offer a scalable path to robot learning, yet existing action tokenizers treat tokenization as a compression problem, producing representations that are semantically misaligned with the autoregressive backbone. We propose CATok, a causal action tokenizer that reframes tokenization as a causally structured generative process. CATok introduces a conditional annealing mechanism that extracts action tokens by progressively annealing a flow-matching p...
  </details>

- **2026-09-28** — Junchen Fu, Kleomenis Katevas, Vandana Rajan et al. — [Can Generative Retrievers Learn Semantic IDs Without Forgetting How to Speak?](http://arxiv.org/abs/2609.35430v1)
  <details><summary>📄 Abstract</summary>
  Generative retrieval (GR) enables end-to-end retrieval by generating document semantic identifiers (SIDs). However, retrieval-only fine-tuning can over-specialize pretrained language models to SID prediction, substantially distorting their natural-language distribution and limiting their suitability for interactive systems that must both retrieve documents and generate natural-language responses. We introduce SpeakGR, a dual-objective framework that learns SIDs while preserving language generati...
  </details>

- **2026-09-28** — Amir Moeini, Huaijiang Zhu, Daniel Havir et al. — [Inductive Feedback for Mixed-Policy Distillation](http://arxiv.org/abs/2609.35390v1)
  <details><summary>📄 Abstract</summary>
  Verbal feedback can identify errors and prescribe corrections, providing rich supervision for language-model post-training even when reliable programmatic verifiers are unavailable. Such feedback, often generated by a capable model, can be used to condition the teacher in on-policy distillation, which trains the student to match the teacher's predictions on student-generated rollouts. However, this approach can transfer teacher preferences that the feedback did not motivate, while leaving much o...
  </details>

- **2026-09-28** — Ruitao Liu, Qinghao Hu, Song Han — [d-OPD: Future-Aware On-Policy Distillation for Block Diffusion Language Models](http://arxiv.org/abs/2609.35362v1)
  <details><summary>📄 Abstract</summary>
  Large language models (LLMs) typically generate text autoregressively (AR), predicting one token at a time. Block diffusion language models (dLLMs) instead generate blocks sequentially while denoising multiple tokens in parallel within each block, offering a promising way to accelerate generation. Rather than training such models from scratch, recent work adapts strong pretrained AR models into block dLLMs through distillation. On-policy distillation (OPD) has been widely used for LLM training b...
  </details>

- **2026-09-28** — Yiqun Zhang, Peidong Wang, Zihan Wang et al. — [Decide, Don't Generate: Competitive Dimensional ABSA with Jev's Typed Decisions](http://arxiv.org/abs/2609.35293v1)
  <details><summary>📄 Abstract</summary>
  Aspect-based sentiment analysis (ABSA) has largely turned to text generation. We show that competitive dimensional ABSA does not need it. Using Jev, a frozen model that answers typed questions with rubric scores, label probabilities, and yes/no judgments, we decompose all three tasks of SemEval-2026 Task III Track A into such decisions and align them with the annotation scheme through 488 coefficients fitted on CPU, with no text generation and no backbone tuning. On valence-arousal regression ov...
  </details>

- **2026-09-28** — Leyang Xue, Tianxin Wang, Xin Zhe Khooi et al. — [Weaver: A System for AI-RAN Compute Sharing with Foundation Model Training](http://arxiv.org/abs/2609.35276v1)
  <details><summary>📄 Abstract</summary>
  The emergence of AI-RAN infrastructure, which equips cell sites with GPU-accelerated hardware, creates an opportunity to colocate non-RAN workloads with primary RAN processing. We explore using this spare capacity for decentralized training of foundation models (FMs), one of the most compute-intensive AI workloads. We present the first characterization of spare GPU capacity in AI-RAN systems at both micro-scale--across transmission slots within a cell site--and macro-scale--across sites. Our ana...
  </details>

- **2026-09-28** — Genglin Wang, Kaiwei Liu, Liekang Zeng et al. — [EdgeCraft: Automated Model Crafting for Edge IoT](http://arxiv.org/abs/2609.35167v1)
  <details><summary>📄 Abstract</summary>
  Machine learning (ML) increasingly powers Internet of Things (IoT) applications at the edge. Yet producing a deployable edge ML artifact for a specific scenario requires navigating a huge search space spanning data representation, model design, training on domain-specific data, and runtime customization. This workflow is fragmented and difficult to scale across diverse edge applications.   We present EdgeCraft, an LLM-driven system that turns high-level intent into deployable edge ML artifacts. ...
  </details>

- **2026-09-28** — Guodong Ma, Baofeng Sun, Wenyu Yang et al. — [Coordinated Lane-Level Variable Speed Limits and Ramp Metering for Successive Weaving Segments Considering Merging/Diverging Risks: A Hybrid Model Predictive Control and Multi-Agent Reinforcement Learning Approach](http://arxiv.org/abs/2609.35152v1)
  <details><summary>📄 Abstract</summary>
  Successive weaving segments (SWSs) on urban expressways are bottlenecks prone to recurrent congestion and collisions, requiring fine-grained active traffic management (ATM). Existing approaches struggle to balance the adaptive performance of data-driven optimization with the resilience and transferability of model-based control. We propose a hybrid framework to coordinate lane-level variable speed limits (VSLs) and ramp metering across SWSs. First, we reconstruct L-METANET, a lane-level macrosco...
  </details>

- **2026-09-28** — Yaxiao Liu, Pengbo Liu, Yiwen Liu et al. — [From Migration to Calibration: Preserving Agent Capabilities across Models, Jurisdictions, and Scale](http://arxiv.org/abs/2609.35149v1)
  <details><summary>📄 Abstract</summary>
  Agents need calibration when deployment conditions change: replacing a driving model, including a foundation-to-post-trained transition; crossing jurisdictions; or scaling across heterogeneous markets and sources. Interface compatibility alone does not establish capability retention or target-contract satisfaction. We formulate agent calibration as constrained behavioral adaptation across three interacting layers: information preservation, harness adaptation, and user acceptance; the layers appl...
  </details>

- **2026-09-28** — Ran Yan, Youhe Jiang, Jiayi Nie et al. — [AReaL-TIK: Stateful Agentic Optimization of Unified RL Kernels through an Optimization IR](http://arxiv.org/abs/2609.35140v1)
  <details><summary>📄 Abstract</summary>
  Reinforcement learning (RL) post-training often uses distinct GPU kernels for rollout and policy update. In synchronous PPO and GRPO, numerical disagreement can perturb ratios between current token probabilities and those assigned during rollout. Recomputing rollout log-probabilities with the policy-update backend avoids this discrepancy but adds a forward pass. Bitwise-consistent unified kernels permit reuse when the policy snapshot and probability processing match the objective. Their optimiza...
  </details>

- **2026-09-28** — Yu-Kai Wang, Chun-Xin Tan, Manh-Hung Nguyen et al. — [Style-Driven Data Synthesis and Degradation-Aware Enhancement for Ultrasound Image Restoration](http://arxiv.org/abs/2609.35120v1)
  <details><summary>📄 Abstract</summary>
  Low-cost handheld ultrasound devices can be widely deployed compared to professional hospital ultrasound machines. However, their images suffer from compound degradation that can mislead clinical judgment. Motivated by this observation, mapping handheld low-quality (LQ) to hospital high-quality (HQ) images has been considered a valuable research question. Conventionally, the mapping requires pixel-aligned LQ-HQ pairs. This requirement is unsatisfactory in practical scenarios because real scans a...
  </details>

- **2026-09-28** — Seongtae Hong, Youngjoon Jang, Jungseob Lee et al. — [RenderRank: Learning to Rerank Text with Compressed Visual Tokens](http://arxiv.org/abs/2609.35069v1)
  <details><summary>📄 Abstract</summary>
  Rendering document text as images allows vision-language models to encode documents as visual tokens, which can reduce input sequence length compared with text input. This reduction in input length is particularly useful for reranking, where each query involves scoring multiple candidate documents and token savings apply to each candidate evaluation. We introduce RenderRank, a reranker that learns query-dependent relevance scoring from compressed visual document representations instead of the te...
  </details>

- **2026-09-28** — Xiaotong Ji, Ahmed Khaled Khamis, Rasul Tutunov et al. — [Composable Decoding on the Probability Simplex: Theory and Implementation](http://arxiv.org/abs/2609.34992v1)
  <details><summary>📄 Abstract</summary>
  Decoding for large language models is typically treated as a collection of isolated sampling strategies, with limited theoretical understanding of the behaviours they induce and how their underlying objectives relate. We formulate decoding as an optimisation problem over next-token distributions on the probability simplex, balancing expected model score against regularisation under support constraints. This view recovers familiar decoding methods through choices of regularisers and support const...
  </details>

- **2026-09-28** — Rongyu Zhang, Ruizhi Fan, Yunfan Lou et al. — [RoboFL: Federated Expert Assembly for World Action Models](http://arxiv.org/abs/2609.34968v1)
  <details><summary>📄 Abstract</summary>
  Vision-language-action and world-action models are increasingly popular, yet remain bottlenecked by physical interaction data that is scarce, institutionally siloed, and task-heterogeneous. A natural federated solution is to let each client adapt a shared foundation model through parameter-efficient fine-tuning, avoiding the exchange of full-model updates. However, federating these adapters is nontrivial, as naive aggregation can entangle incompatible updates, while incorporating MoE-style routi...
  </details>

- **2026-09-28** — Joseph Hoche, Quentin Guimard, Gianni Franchi — [Semantic Uncertainty Quantification Needs Factual Equivalence](http://arxiv.org/abs/2609.34967v1)
  <details><summary>📄 Abstract</summary>
  Semantic uncertainty quantification for large language models rests on a common template: sample several answers, measure how much they agree, and treat disagreement as uncertainty. We first formalize this template as two separate roles: an operator that compares two answers, and an aggregator that combines all pairwise comparisons into a scalar. Existing methods differ almost entirely in how they aggregate, while taking the operator off the shelf, typically an NLI model or a generic sentence en...
  </details>

- **2026-09-28** — Arshak Rezvani, Sasha Behrouzi, Ahmad-Reza Sadeghi — [JevVibe: Efficient Classification-Guided Secure Code Generation](http://arxiv.org/abs/2609.34963v1)
  <details><summary>📄 Abstract</summary>
  Large language models can generate functionally correct code that still contains security weaknesses, motivating repair pipelines that first diagnose a weakness type before deciding how to fix it. The Common Weakness Enumeration (CWE) provides a standardized vocabulary for such diagnoses, but asking an autoregressive language model to generate a CWE label and extracting it from the response raises questions about output validity, speed, and cost, as well as accuracy. We evaluate Jev, a decision ...
  </details>

- **2026-09-28** — Huayi Lai, Shichao Song, Qingchen Yu et al. — [PDEU-Bench: Benchmarking the Personalized Planning Lifecycle of Tool-Calling LLM Agents](http://arxiv.org/abs/2609.34930v1)
  <details><summary>📄 Abstract</summary>
  Large language model (LLM) agents are evolving from tool-calling systems that execute isolated instructions into task-oriented agents that pursue user goals through sustained, multi-step interactions. However, existing benchmarks for personalized tool use largely assess isolated calls or reactive execution, leaving unclear whether agents can formulate, execute, and revise an explicit plan while preserving user preferences throughout long-term interaction. To address this gap, we introduce \textb...
  </details>

- **2026-09-28** — Yaowen Zhang, Xiangyu Qiu, Junyi Hu et al. — [ReSight-SMC: Two-Stage Power Sampling via Island SMC with Visual Scouts](http://arxiv.org/abs/2609.34905v1)
  <details><summary>📄 Abstract</summary>
  Power sampling has emerged as a training-free approach to LLM reasoning, eliciting capabilities comparable to reinforcement learning by sharpening the model distribution over complete responses. Despite this success, power sampling remains underexplored in large vision-language models (LVLMs). We transfer Power-SMC to LVLM decoding by defining a sequence-power target conditioned on both the image and the prompt. This direct transfer provides a strong training-free baseline, but leaves two aspect...
  </details>

- **2026-09-28** — Haizhao Jing, Zhenhao Shang, Haokui Zhang et al. — [P4Q: Co-designing Token Pruning and Quantization for Vision-Language Model Acceleration](http://arxiv.org/abs/2609.34867v1)
  <details><summary>📄 Abstract</summary>
  Vision language models have achieved strong performance across a wide range of multimodal applications, yet their substantial computational and memory costs hinder efficient deployment. Visual token pruning and post-training quantization reduce inference overhead along two complementary dimensions, namely sequence length and numerical precision. Existing workflows typically optimize these techniques independently or apply them sequentially. Their distinct optimization objectives leave critical i...
  </details>

- **2026-09-28** — Zhiqiang Wang, Yichao Gao — [JEV as a Judge for Agent Trace Security: An Empirical Comparison with Generative LLM Judges](http://arxiv.org/abs/2609.34862v1)
  <details><summary>📄 Abstract</summary>
  Security evaluation of tool-using agents requires judging actions in context, yet generative judges add latency, explanation overhead, and output-validation failures. We study whether JEV, a typed decision model, offers a useful alternative for retrospective trace classification. We evaluate JEV and four generative judges on four benchmark collections totaling 5,219 trajectories, using a common risk rubric and behavior-level labels. JEV attains a benchmark-averaged positive-class F1 of 77.8, com...
  </details>

- **2026-09-28** — Yueru Chen, Pengpeng Yu, Dingquan Li et al. — [Transform-Aligned Learned Features for Lossy Point Cloud Attribute Compression](http://arxiv.org/abs/2609.34834v1)
  <details><summary>📄 Abstract</summary>
  Transform-based methods provide an effective framework for point cloud attribute compression by representing attributes as transform coefficients. Introducing learned spatial context into this framework requires mapping spatial representations to the transform domain, but this known basis change is often left for the network to learn implicitly. We propose Transform-Aligned Learned Features (TALF) by applying the attribute transform to learned spatial representations, explicitly aligning them wi...
  </details>

- **2026-09-28** — Rong Yu Xu, Prayag Tiwari, Shaolei Zhang — [From Perception to Integration: Revisiting the Internal Dynamics of Reasoning in Vision-Language Models](http://arxiv.org/abs/2609.34809v1)
  <details><summary>📄 Abstract</summary>
  Vision-language models (VLMs) can answer simple visual questions, but often struggle when one question requires several visual judgments. We study this gap with controlled tasks for feature binding, numerosity, spatial relations, and amodal completion, together with a Composite task that combines them. Matched counterfactual image pairs isolate changes in the visual evidence needed to answer. Across four models, direct answers, hidden-state readouts, and state interventions show that the individ...
  </details>

- **2026-09-28** — Bohao Xing, Xin Liu, Kaishen Yuan et al. — [Do Emotion Concepts Generalize Across Sources, Modalities, and Architectures in Vision-Language Models?](http://arxiv.org/abs/2609.34742v1)
  <details><summary>📄 Abstract</summary>
  Recent studies suggest that large language models encode emotion concepts as structured internal representations, but most existing work focuses on text and a single architecture. Therefore, we ask, do emotion concepts generalize across sources, modalities, and architectures in vision--language models (VLMs)? To address this, we construct CMES (Cross-Modal Emotion Stimuli), a multi-source collection of emotion-conditioned stories, real facial expressions, synthetic portraits, and synthetic emoti...
  </details>

- **2026-09-28** — Yingxu Wang, Kunyu Zhang, Xinwang Liu et al. — [Learning Propagation Geometry from Message-Passing Feedback](http://arxiv.org/abs/2609.34711v1)
  <details><summary>📄 Abstract</summary>
  Learning local geometry enables graph neural networks (GNNs) to adapt how they compare and integrate neighborhood information. However, estimating geometry from aggregated representations can overlook variation among individual messages and dependencies across feature dimensions. We propose GeoF, a recurrent framework that jointly evolves node features and propagation geometry through message-passing feedback. Each node maintains a local symmetric positive-definite geometry, initialized from a s...
  </details>

- **2026-09-28** — Omri Kaduri, Kate Feingold, Phillip Isola et al. — [Reinforcement Learning from Intermediate Renders for Image-to-Code Generation](http://arxiv.org/abs/2609.34587v1)
  <details><summary>📄 Abstract</summary>
  Reinforcement learning is increasingly used to post-train vision-language models for image-to-code generation, such as generating SVG code from a reference image, by optimizing rewards computed from the final rendered output. However, relying on a single terminal reward provides sparse feedback that is poorly aligned with the contribution of individual tokens. A generated program may contain operations that accurately reproduce some parts of the target image alongside others that introduce error...
  </details>

- **2026-09-28** — Bingqing Jiang, Guoxi Zhang, Jasper Wang et al. — [SkillRubric: Co-Evolving Actor Guidance and Evaluator Rubrics for Multimodal Agents](http://arxiv.org/abs/2609.34557v1)
  <details><summary>📄 Abstract</summary>
  Recent work incorporates reusable skills distilled from past interactions into multimodal agent training, providing procedural guidance for long-horizon planning and tool use. However, policy optimization in these methods remains driven primarily by sparse outcome rewards, providing little supervision for intermediate decisions. Rubric-based rewards address this limitation through explicit intermediate criteria, but reliable rubrics are difficult to construct at scale and often disconnected from...
  </details>

- **2026-09-28** — Boyu Zhang, Yifan Liu, Shuxia Lin et al. — [TSGate: Timestep-Aware Gated Attention for Diffusion Transformers](http://arxiv.org/abs/2609.34539v1)
  <details><summary>📄 Abstract</summary>
  Diffusion Transformers (DiTs) have emerged as the dominant architecture for high-fidelity image and video generation. Recent DiT systems increasingly use structured prompts for training, improving caption quality and prompt adherence. However, their generation quality can degrade severely under out-of-domain (OOD) prompts, including the free-form descriptions supplied by users at inference time. Although LLM-based rewriting can convert these prompts into structured formats, it does not guarantee...
  </details>

- **2026-09-28** — Hangyul Yoon, Hyungyung Lee, Edward Choi et al. — [SentZero: An Enhanced Sentence-Centric Vision-Language Pretraining for Multi-Task Zero-Shot Chest X-Ray Analysis](http://arxiv.org/abs/2609.34479v1)
  <details><summary>📄 Abstract</summary>
  Vision-language (VL) pretraining using paired chest X-ray (CXR) images and radiology reports has shown strong potential for medical image understanding. However, existing methods often remain dependent on task-specific finetuning because radiology reports are lengthy, clinically dense, and difficult to align with simple zero-shot prompts. Recent sentence-level approaches partially address this limitation using clinical phrases extracted by large language models (LLMs), but they largely overlook ...
  </details>

- **2026-09-28** — Jianpeng Zhao, Haihua Xu, Haoyang Zhang et al. — [RGDT-Bench: Benchmarking LLM Reasoning for Rule-Governed Decisions and Their Justifications](http://arxiv.org/abs/2609.34455v1)
  <details><summary>📄 Abstract</summary>
  We study reasoning in Rule-Governed Decision Tasks (RGDTs), where models apply external rules to case facts and justify decisions, as required in policy, contract, and compliance settings. Beyond the deductive capability emphasized by standard mathematical and logical reasoning tasks, RGDTs require interpreting rules and their applicability, assessing conditions from evidence, combining judgments under rules and exceptions, and providing checkable justifications. These demands motivate a benchma...
  </details>

- **2026-09-28** — Lei Wu, Jiashuai Liu, Di Zhang et al. — [Modeling Whole-Slide Images as Dynamic Tumor Microenvironment Fields](http://arxiv.org/abs/2609.34451v1)
  <details><summary>📄 Abstract</summary>
  Due to the gigapixel-scale nature of whole-slide images (WSIs), weakly supervised WSI analysis is commonly formulated as a multiple instance learning (MIL) problem, where patch-level features are aggregated into slide-level representations. However, diagnostic and prognostic evidence often arises from spatially coherent tumor microenvironment regions and their interactions, rather than isolated patches alone. Existing patch-level or static region-based methods usually overlook how tissue regions...
  </details>

- **2026-09-28** — Hongwei Li, Spandan Garg, Yufan Huang — [Improving Large Language Models for Code through Runtime Program-State Reasoning](http://arxiv.org/abs/2609.34359v1)
  <details><summary>📄 Abstract</summary>
  Large language models receive limited explicit training in reasoning about runtime program states. We study whether training models to reason about runtime program states improves downstream software-engineering capabilities. We introduce two complementary program-state reasoning tasks. Buggy input-output reasoning requires a model to generate a concrete input that exposes a behavioral difference between a buggy program and a hidden correct implementation and to predict the resulting execution b...
  </details>

- **2026-09-28** — Taekyung Kim, Salem Fradi, Yanning Dai et al. — [Predictive Semantic Safety: From Visual Physical Reasoning to Safety-Critical Control](http://arxiv.org/abs/2609.34356v1)
  <details><summary>📄 Abstract</summary>
  Physical interactions can create future hazards that are not apparent from the robot's current geometric surroundings. We present a framework termed Predictive Semantic Safety (PSS), which connects visual physical reasoning to backup-based safety filtering. A vision-language model (VLM) predicts physical events and their timing or directly predicts object displacements. An explicit motion model converts event hypotheses into object trajectories. Split conformal prediction calibrates position err...
  </details>

- **2026-09-28** — Shucheng Liu, Changchun Shi, Kai Zhang et al. — [FAST-Brain: A Flow-Aligned Spatio-Temporal Surrogate Brain Model](http://arxiv.org/abs/2609.34354v1)
  <details><summary>📄 Abstract</summary>
  Modeling resting-state functional magnetic resonance imaging (rs-fMRI) data is crucial for understanding brain-wide neural activity. However, traditional methods struggle to capture complex temporal dynamics over long horizons, to account for the brain's anatomical spatial structure, and to model high-dimensional ambient signals that lie on a low-dimensional intrinsic subspace. We propose FAST-Brain, a unified flow-aligned spatio-temporal surrogate brain model that addresses all three challenges...
  </details>

- **2026-09-28** — Kang Yang, Gaofeng Dong, Liying Han et al. — [Dynamical Parameters: An Interpretability Framework for Time-Series Foundation Models](http://arxiv.org/abs/2609.34316v1)
  <details><summary>📄 Abstract</summary>
  This work studies a central gap in interpreting time-series foundation models (TSFMs): a dynamical property may be accessible in a hidden state even when the forecast fails to respond correctly as that property changes. We formalize these properties as Dynamical Parameters, including trend slope, oscillation frequency, and autoregressive dependence. We compare their representation accessibility, measured by recovery from hidden states, with their forecast response, measured by agreement with the...
  </details>

- **2026-09-28** — Trung Minh Bui, JongSul Moon, YoungOuk Kim et al. — [SAGE: Symbolic Action-Gating and Editing for LLM Task Planners](http://arxiv.org/abs/2609.34268v1)
  <details><summary>📄 Abstract</summary>
  Large language models (LLMs) are now the default cognitive core of embodied household agents, yet the plans they emit are rarely checked against a grounded model of the environment before execution, and the task-success they report is often measured on benchmarks so saturated that no method can be separated from another. We present SAGE (Symbolic Action-Gating and Editing), a single-LLM planner built from two lightweight mechanisms: a domain-agnostic symbolic gate (~250 lines of Python, zero tok...
  </details>

- **2026-09-28** — Wenyi Yu, Siyin Wang, Terumi Chiba et al. — [SALMONN-duo: Adaptive Dual-System Coordination for Full-Duplex Voice Agents](http://arxiv.org/abs/2609.34247v1)
  <details><summary>📄 Abstract</summary>
  Full-duplex speech large language models (LLMs) enable low-latency, natural voice interaction. However, real-world agents must also use tools and perform deliberative reasoning-operations whose variable latency and computational cost conflict with the stringent timing requirements of real-time conversation. To reconcile these demands, we propose SALMONN-duo, an adaptive dual-system voice agent inspired by dual-process theories of cognition. SALMONN-duo separates real-time interaction from delibe...
  </details>

- **2026-09-28** — Jinnuo Liu, Junhao Zhu, Weifeng Jiang et al. — [Coherence-Aware Distributional Evaluation of Open-Ended Text Generation](http://arxiv.org/abs/2609.34240v1)
  <details><summary>📄 Abstract</summary>
  Existing metrics for open-ended text generation measure likelihood, lexical diversity, or distributional similarity in generic representation space, yet they can miss fundamental dimensions of quality. A prominent blind spot is global coherence: a generated passage may be locally fluent while remaining globally contradictory, causally inconsistent, or topically disconnected. Such failures can still preserve the token-level and lexical statistics that existing metrics rely on. We identify represe...
  </details>

- **2026-09-28** — Jiapeng Li — [Frozen Judges, Moving Agents: Version-Dependent LLM-Judge Error and the Limits of Judge-Assisted Agent Evaluation](http://arxiv.org/abs/2609.34198v1)
  <details><summary>📄 Abstract</summary>
  Language-model judges compare agent upgrades with their predecessors, but a fixed judge can make version-dependent mistakes. We analyze 35 public coding-agent submissions (20 prespecified version pairs on 250 SWE-bench Verified issues), two customer-service agents (155 tau-bench tasks), and 1,106 expert-labeled AgentRewardBench trajectories. An upstream outage left three judges for the primary SWE-bench analysis (8,743 aligned agent-task cells); the fourth is descriptive. All three coding-agent ...
  </details>

- **2026-09-28** — Jiaxin Liu, Ruilin Yu, Liang Peng et al. — [Beyond Retrieval Relevance: Scene-Grounded Risk Entailment for Vision-Language Driving](http://arxiv.org/abs/2609.34145v1)
  <details><summary>📄 Abstract</summary>
  Retrieval-augmented generation (RAG) gives vision--language driving systems access to external safety knowledge, yet a retrieved risk rule may be relevant without applying to the current scene. A vision--language model (VLM) receiving such knowledge must ground objects, bind entities across time, and verify relations before deciding how to act, leaving the support for risk conclusions implicit. We address this relevance--applicability gap with a Driving-Risk Knowledge Graph (DRKG) and Semantic W...
  </details>

- **2026-09-28** — Se Jin Sim, Seoung Bum Kim — [WhiteCon: Semi-Supervised Domain Adaptation Regression Through Whitening Transform and Dual Consistency](http://arxiv.org/abs/2609.34078v1)
  <details><summary>📄 Abstract</summary>
  Domain adaptation is crucial for addressing distributional shifts that degrade model performance across domains. While most existing research has centered on classification, semi-supervised domain adaptation regression (SSDAR) for continuous-output tasks remains largely unexplored, particularly in practical scenarios with limited labeled target data. To address this gap, we propose semi-supervised domain adaptation regression through whitening transform and dual consistency (WhiteCon), which com...
  </details>

- **2026-09-28** — Piyush Jha, Aishik Ghosh, Vijay Ganesh — [Towards Certificate-Driven Software Porting: A Self-Improving Agentic Harness for Scientific Program Optimization](http://arxiv.org/abs/2609.34069v1)
  <details><summary>📄 Abstract</summary>
  The upgrade and rewriting of large scientific codebases has traditionally been a major challenge. While evolutionary search with large language models (LLMs) can port and accelerate legacy code, repair feedback in prompts alone does not prevent subsequent candidates from repeating the same errors. We introduce Certificate-Driven Evolutionary Search (CDES), which extends evolutionary search with enforceable restrictions derived from failed candidates, recorded as certificates of assumptions, chec...
  </details>

- **2026-09-28** — Mir Tafseer Nayeem, Davood Rafiei — [Who Gets a Token, and What Does It Carry? Unequal Name Support and Concept Access in Large Language Models](http://arxiv.org/abs/2609.34065v1)
  <details><summary>📄 Abstract</summary>
  Names are personal identifiers, but they also carry social meaning and are widely used to evaluate how language models treat different people. Such evaluations typically assume that matched names are comparable model inputs. We show that this assumption often fails at the lexical interface: matched names are not necessarily matched inputs. Some names receive direct single-token access, while others are assembled from multiple subwords, creating unequal name-surface support. Across nearly half a ...
  </details>

- **2026-09-28** — Alexander Detkov, Matt Thomson — [Do World Models Learn Global Understanding?](http://arxiv.org/abs/2609.34058v1)
  <details><summary>📄 Abstract</summary>
  AI systems often feel brittle and fragmented. A large language model (LLM) may correctly explain a concept but fail to apply it, or follow safety instructions in one context but not another. This behavior suggests a general failure to lift local information to a global understanding. To gain fundamental insight, we frame "understanding" as learning constraints and propagating their consequences. We construct learning tasks on monoid worlds, sets of states connected by action transitions, where o...
  </details>

- **2026-09-28** — Qiwei Liang, Guangyu Chen, Shaolong Zhu et al. — [MM-ABC: Towards Generalist Mobile Manipulation via Seeing, Coordinating and Imagining](http://arxiv.org/abs/2609.35652v1)
  <details><summary>📄 Abstract</summary>
  Mobile manipulation extends robot interaction beyond a fixed kinematic workspace by making the reachable region itself controllable. This flexibility introduces two central challenges: spatially grounded perception under continuous ego-motion and coordinated control of heterogeneous arm and base actions. Existing approaches strengthen geometry through explicit 3D representations or predictive world models, and often decouple mobility and manipulation into separate action streams. We argue that e...
  </details>

- **2026-09-28** — Davide Dardari — [On the Universal Approximation Capability of Stacked Intelligent Metasurfaces](http://arxiv.org/abs/2609.35524v1)
  <details><summary>📄 Abstract</summary>
  Wave-domain processing is an emerging paradigm in which signal-processing operations are partially shifted from the digital domain to the electromagnetic (EM) domain to reduce complexity, energy consumption, and latency in next-generation wireless systems. Stacked intelligent metasurfaces (SIMs) are a promising technology for wave manipulation. Although numerous studies have addressed the numerical design of SIMs for specific tasks, no theoretical results have yet established whether a prescribe...
  </details>

- **2026-09-28** — Yingjin Song, Denis Paperno, Albert Gatt — [Who Is Left of Whom? Tracing Spatial Evidence and Role Binding in Relative-Position Reasoning](http://arxiv.org/abs/2609.35486v1)
  <details><summary>📄 Abstract</summary>
  High instance-level accuracy can mask inconsistencies in spatial reasoning when objects exchange positions or their roles are reversed in the query. The internal representations supporting relative-position reasoning remain poorly understood. We investigate two complementary components of this process: tracking object locations in the input and representing their query roles. Across three VLMs with visual or textual inputs and their language-model backbones, activation patching reveals a staged ...
  </details>

- **2026-09-28** — Youhui Wang, Yunzhu Li, Li Fei-Fei et al. — [DexAgent: An Agentic Human2Sim2Robot Framework for Dexterous Manipulation with Self-Evolving Tool Library](http://arxiv.org/abs/2609.35318v1)
  <details><summary>📄 Abstract</summary>
  Human videos offer a scalable source of demonstrations for dexterous robot manipulation. However, existing human-to-simulation-to-robot (Human2Sim2Robot) pipelines rely on predefined procedures that struggle to accommodate diverse object properties and interactions, particularly those involving articulated and deformable objects. We introduce DexAgent, an agentic Human2Sim2Robot framework that converts a single egocentric human video and a task prompt into physically grounded robot trajectories ...
  </details>

- **2026-09-28** — Pankhuri Vanjani, Mostafa Hatab, Can Mizrakli et al. — [ReCAT: Remember, Count, and Time: Structured Recurrent Memory for Robot Manipulation](http://arxiv.org/abs/2609.35200v1)
  <details><summary>📄 Abstract</summary>
  Memory-dependent manipulation requires robots to make decisions using information that is no longer available to their current sensors, such as recalling an earlier visual cue, tracking task progress, counting repeated events, or estimating elapsed time. We present ReCAT, a language-conditioned policy with structured recurrent memory. An instruction-conditioned encoder forms features from the current observation. A recurrent memory integrates the observation stream through Mamba-2 layers and one...
  </details>

- **2026-09-28** — Yichao Liang, Amber Li, Dat Nguyen et al. — [EMPIRIC: Experiment-Driven Learning of Residual World Models for Robot Planning](http://arxiv.org/abs/2609.35047v1)
  <details><summary>📄 Abstract</summary>
  A robot should be able to learn through experiments how unfamiliar objects behave and interact, then plan with that knowledge. It need not start from scratch: physics engines supply knowledge of motion and contact, but can omit entire mechanisms, such as glue curing, water heating, or wind. We present EMPIRIC, an agent that learns a residual world model: a physics engine extended with code for the missing mechanisms. The learned programs can introduce new forces, constraints, and hidden state, a...
  </details>

- **2026-09-28** — Wolfgang Maass — [Nociception as a Control Primitive: Afferent Channels and Nociceptive Memory for Agents Deployed in One Body](http://arxiv.org/abs/2609.34840v1)
  <details><summary>📄 Abstract</summary>
  An agent deployed in a single body cannot learn how fast that body wears, because every trial that would reveal its wear resistance wears the body it would protect. We study this \emph{epoch-one} setting, in which the parameters of a fixed-weight policy are set before the body is drawn and never updated in life. The agent carries a load-gated nociceptive channel and a memory that retains what was felt. We prove that felt cost moves the allocation to the best-\emph{paid} work not yet felt rather ...
  </details>

- **2026-09-28** — Yuan Lin, Ziyue Zhou, JinLong Zhao et al. — [Where Do Embodied Decisions Come From? Rethinking Latent and Explicit Reasoning](http://arxiv.org/abs/2609.34794v1)
  <details><summary>📄 Abstract</summary>
  Chain-of-Thought (CoT) reasoning is increasingly incorporated into Vision-Language-Action (VLA) models, yet it can degrade the performance of stronger embodied agents. We investigate this capability-dependent effect by distinguishing explicit reasoning from latent decision computation, i.e., perception-grounded computation that directly supports action prediction. Under the standard \textit{think-then-act} (TTA) paradigm, intervening on the generated CoT while fixing the visual input and model p...
  </details>

- **2026-09-28** — Zijian Ye, Chengqi Wei, Wei Huang et al. — [D$^2$-VLA: Dual-Memory Dual-Frequency Vision-Language-Action Model For Long Dynamic Manipulation](http://arxiv.org/abs/2609.34792v1)
  <details><summary>📄 Abstract</summary>
  Long-horizon manipulation requires robots to remember cues that are no longer in view while responding to moving objects. Yet vision-language-action (VLA) policies often rely on the latest observation, and refreshing their visual context typically requires another costly vision-language model (VLM) pass. We present D$^2$-VLA, which combines dual memory and dual-frequency control at the KV-cache interface of a pretrained VLA. D$^2$-VLA uses block-wise causal KV caching to encode observations incr...
  </details>

- **2026-09-28** — Linquan Wu, Shichang Meng, Tianxiang Jiang et al. — [Draft-KV: Learning Useful Latent Communication Between Language Models](http://arxiv.org/abs/2609.34754v1)
  <details><summary>📄 Abstract</summary>
  Latent communication passes internal states between language models instead of decoded text, but higher receiver accuracy does not show that the receiver used the message content. Across five method-dataset pairs, replacing each message with one from an unrelated question changes accuracy by at most 0.60 points, even when communication adds 15.44 points over the receiver alone. Thus the interface can supply the gain while making the sharer dispensable. Draft-KV instead sends the key-value states...
  </details>

- **2026-09-28** — Naichuan Sun, Haotian Shen, Yizhang Zhang et al. — [DexWeave: Learning Dexterous Humanoid Loco-Manipulation from Human Demonstrations](http://arxiv.org/abs/2609.34724v1)
  <details><summary>📄 Abstract</summary>
  Learning dexterous humanoid loco-manipulation from human demonstrations requires transferring not only human motion, but also the coordinated interaction structure underlying the demonstrated behavior. This is challenging because embodiment differences distort the coupling among body motion, wrist placement, finger articulation, and object interaction, while kinematically accurate references may still be difficult to realize under robot dynamics. We present DexWeave, a unified framework that con...
  </details>

- **2026-09-28** — Qiulin Shang, Binyu Wang, Yongqi Qiao et al. — [SOLAR: A State-Driven Online Learning Rate Scheduler for LLM Pretraining](http://arxiv.org/abs/2609.34681v1)
  <details><summary>📄 Abstract</summary>
  Learning-rate (LR) scheduling plays a central role in large language model (LLM) pretraining, yet current practice still relies heavily on hand-crafted heuristics such as Warmup-Cosine-Decay and Warmup-Stable-Decay. Because these schedules are fixed in advance, they cannot adapt to evolving optimization dynamics. Online learned scheduling within the Learning to Optimize (L2O) framework offers a dynamic alternative, but remains brittle at LLM scale due to noisy signals, delayed feedback, and the ...
  </details>

- **2026-09-28** — Yihan Zhou, Rui Yan, Mingcong Li et al. — [Gaze Prompts: Temporally Dense Human Attention for Vision-Language-Action Fine-Tuning](http://arxiv.org/abs/2609.34550v1)
  <details><summary>📄 Abstract</summary>
  Vision-Language-Action (VLA) fine-tuning pairs images with actions at every step, yet typically provides only a task-level language instruction, leaving moment-to-moment visual relevance implicit. We introduce \emph{eye-tracker-supervised gaze prompting}, which uses gaze recorded during VR teleoperation to provide frame-level visual guidance for VLA fine-tuning. During training, recorded gaze locations are rendered as crosshairs on the robot's head-camera images. At deployment, a lightweight pre...
  </details>

- **2026-09-28** — Sheng Hu, Weiyi Lu, Lingbing Zeng et al. — [ARS: Agentic Reward System for Robot Learning](http://arxiv.org/abs/2609.34484v1)
  <details><summary>📄 Abstract</summary>
  Progress reward modeling is the problem of estimating how a robot's behavior changes task progress over time. Reliable estimation requires distinguishing meaningful state changes from failed attempts and task-irrelevant actions. We introduce the Agentic Reward System (ARS), an inference framework for progress reward modeling with general-purpose vision-language models (VLMs), without additional reward-model training. Given an offline trajectory and a task instruction, ARS uses adaptive visual in...
  </details>

- **2026-09-28** — Jaegyun Park, Jingwang Lee, Jungsoo Lee et al. — [From Language to Task Maps: Compiling Semantic Relations While Preserving Task-Relevant Freedom](http://arxiv.org/abs/2609.34412v1)
  <details><summary>📄 Abstract</summary>
  Natural-language manipulation instructions specify qualitative relations, whereas continuous controllers require state-evaluable task quantities, differentials, and completion conditions. Because a qualitative relation generally leaves part of the relative configuration unspecified, expanding it into a complete pose can introduce unintended constraints. We present a typed semantic-to-geometric interface in which language specifies entities, relations, and phases, while each relation indexes a re...
  </details>

- **2026-09-28** — Ziyao Zeng, Xiatao Sun, Hao Wang et al. — [Dexterous Tactile World Model](http://arxiv.org/abs/2609.34286v1)
  <details><summary>📄 Abstract</summary>
  World models for manipulation are typically trained from video, yet the events that determine how manipulation unfolds, such as making and releasing contact, are difficult to observe visually and are often easier to sense through touch. We present the Dexterous Tactile World Model (DTWM), a video world model for future-frame prediction of egocentric manipulation from both observed video and tactile signals from a glove worn on each hand. We condition a pretrained video diffusion transformer on e...
  </details>

- **2026-09-28** — Fangcheng Liu, Yeqing Shen, Anda Cheng et al. — [RoboICL: Embodied In-Context Learning with GPT-6 Astra](http://arxiv.org/abs/2609.34261v1)
  <details><summary>📄 Abstract</summary>
  General-purpose vision-language models offer a promising way to zero-shot robot control: \gptastra{} excels at open-ended and language- or image-conditioned manipulation but remains substantially weaker on high-precision and long-horizon tasks. We introduce \emph{RoboICL}, an in-context robot-control framework that narrows these gaps without robot-specific parameter updates or a learned VLA. RoboICL separates \emph{demonstration context}, which provides recorded examples when available, from \em...
  </details>

- **2026-09-28** — Qing Yu, Kent Fujiwara — [MotionSpaceFlow: Representation-Aware Flow Matching in Direct Motion Space](http://arxiv.org/abs/2609.34190v1)
  <details><summary>📄 Abstract</summary>
  Recent advances in diffusion and flow models have substantially improved text-driven human motion generation. Yet most methods generate in low-dimensional, temporally downsampled latent spaces learned primarily for reconstruction, a bottleneck that can limit generation quality and preclude direct manipulation of individual frames and joints. We introduce MotionSpaceFlow (MSFlow), a representation-aware flow-matching framework that predicts clean motion directly in continuous motion space without...
  </details>

- **2026-09-28** — Hanoona Rasheed, Mohammed Irfan Kurpath, Bin Ren et al. — [Hard Vision, Easy Vision: What GPT-6 Astra Reveals Across Computer Vision](http://arxiv.org/abs/2609.35718v1)
  <details><summary>📄 Abstract</summary>
  Frontier general-purpose systems are rapidly expanding beyond visual understanding into capabilities traditionally handled by dedicated computer-vision models. As these capabilities expand, a central question for the computer-vision community is how far this reach extends, and what remains hard. We evaluate GPT-6 Astra alongside five frontier general-purpose AI systems across 34 capabilities and 55 benchmarks spanning nine areas of computer vision. We compare their performance with dedicated mod...
  </details>

- **2026-09-28** — Yangqin Jiang, Lingrui Xu, Chao Huang — [PhoneCLI: From App Interfaces to Callable Commands for Mobile Agents](http://arxiv.org/abs/2609.35671v1)
  <details><summary>📄 Abstract</summary>
  Mobile GUI agents operate through a perception--action loop: at each step they screenshot the device, invoke a vision--language model (VLM), and emit an action. It is slow, costly, and brittle, yet most of what it does is navigation---and everyday navigation is static, ordered, and endlessly repeated. We present PhoneCLI, which compiles an app's GUI navigation into callable commands, without any app-internal API, runtime instrumentation, or model training. Offline, PhoneCLI explores a target app...
  </details>

- **2026-09-28** — Mengfan Ma, Biaoshuai Tao, Fangxiao Wang — [Truthful-in-Expectation Mechanism with Constant Maximin-Share Guarantee](http://arxiv.org/abs/2609.35670v1)
  <details><summary>📄 Abstract</summary>
  We study the truthful and fair allocation of indivisible goods to $n$ strategic agents with additive valuations. Babaioff, Feige, and Manaker Morag [FOCS 2026] gave a randomized mechanism that uses only the agents' rankings of the goods, is truthful in expectation (TIE), and guarantees every agent $1/(H_{n-1}+2)=Θ(1/\log n)$ of her maximin share (MMS) in every realized allocation, where $H_{n-1}$ is the $(n-1)$th harmonic number; this is nearly the best possible with rankings alone. They conject...
  </details>

- **2026-09-28** — Aditya Thimmaiah, Lara Marinov, Jayanth Srinivasa et al. — [Twist, Don't Tilt: Trajectory-Exact Constrained Decoding for Masked Diffusion Models](http://arxiv.org/abs/2609.35609v1)
  <details><summary>📄 Abstract</summary>
  Constrained decoding for Masked Diffusion Language Models (MDLMs) aims to ensure that generated outputs satisfy a specified structure or syntax constraint. MDLMs generate outputs by repeatedly unmasking masked positions present in their current state. Recent strategies for constrained decoding constrain the model's per-step mean-field posterior (which factorizes over masked positions) by enforcing the desired constraint with an automaton. The resulting chain-structured factor graph allows exact ...
  </details>

- **2026-09-28** — Yung-Chin Chen, Chia-Yu Chen, Naveen Verma — [IMC-CLINIC: Coupled Loss-Informed Newton Iterations for Clipping in Analog In-Memory Computing](http://arxiv.org/abs/2609.35586v1)
  <details><summary>📄 Abstract</summary>
  Analog in-memory computing (IMC) offers a promising path toward energy-efficient large language model (LLM) inference by executing matrix multiplications (MatMul) directly within memory arrays in the analog domain. Its efficiency, however, comes with an additional source of error: limited-precision analog-to-digital converters (ADCs) quantize accumulated analog partial sums, introducing output-side error distinct from conventional activation and weight quantization at the MatMul inputs. Clipping...
  </details>

- **2026-09-28** — Kangcheng Deng, Hui Cai, Jiacheng Lu et al. — [From Search to Research: Exploring Search Scaling in Autonomous Quantitative Factor Mining](http://arxiv.org/abs/2609.35559v1)
  <details><summary>📄 Abstract</summary>
  Inference scaling has been shown to improve large language model (LLM) performance, and this principle naturally extends to autonomous LLM agents through increased search budgets, which we refer to as *search scaling*. Although prior work has characterized the mechanisms, scaling behavior, and performance limits of LLM inference scaling, much less is known about these questions in autonomous research. Therefore, we investigate how search scaling affects research performance and what mechanisms d...
  </details>

- **2026-09-28** — Yuta Oshima, Ku Onoda, Yusuke Iwasawa et al. — [AutoRef: Harness Optimization for Agentic Multi-Reference Image Generation](http://arxiv.org/abs/2609.35530v1)
  <details><summary>📄 Abstract</summary>
  Recent image generation models can take multiple reference images as input and combine them into a new image. However, multi-reference image generation remains challenging: models may omit or duplicate subjects from the references, or produce images in which multiple subjects appear unnaturally pasted. Recent work has proposed image generation agents that combine image generation models, reasoning models, and a harness, which is an executable program that specifies how reference images are inter...
  </details>

- **2026-09-28** — Zihan Yu, Jiadong Zhang, Jialin Cheng et al. — [MechBench: Can AI Scientific Agents Discover Mechanisms Beyond Phenomenal Laws?](http://arxiv.org/abs/2609.35515v1)
  <details><summary>📄 Abstract</summary>
  Scientific discovery requires not only recovering mathematical laws that describe observable behavior, but also identifying the mechanisms that generate them. Existing benchmarks for symbolic regression and scientific agents primarily evaluate phenomenal-law recovery, leaving mechanism discovery largely untested. We introduce MechBench, a benchmark that explicitly separates these two capabilities. Each task is defined by a mechanistic model, a structured set of scientifically meaningful relation...
  </details>

- **2026-09-28** — Vlad-Petru Nitu, Harsh Songara, Konstantinos Sgouras et al. — [Argus: Agentic, Reference-Calibrated, Tree-Guided, System-Software-Level Bottleneck Localization](http://arxiv.org/abs/2609.35508v1)
  <details><summary>📄 Abstract</summary>
  Operating system (OS) code can account for a substantial share of CPU execution time. First, as application logic is offloaded to heterogeneous accelerators (e.g., GPUs), the CPU increasingly acts as an orchestrator, spending cycles in driver calls, data movement, and synchronization rather than in application code. Second, workloads such as serverless functions frequently invoke OS services. At the same time, the OS is a complex codebase spanning many subsystems (e.g., memory management, networ...
  </details>

- **2026-09-28** — Shangzhe Li, Yuxiao Yang, Tianrun Yu et al. — [An RL View of OPD: Least Square Policy Distillation for Sample-Efficient LLM Reasoning](http://arxiv.org/abs/2609.35505v1)
  <details><summary>📄 Abstract</summary>
  We study on-policy distillation (OPD) through the lens of reinforcement learning, establishing a connection between the reverse-KL objective in OPD and KL-regularized policy optimization. Building on this connection, we introduce Least-Square Policy Distillation (LSPD), an RL-inspired framework that brings optimistic exploration and off-policy data reuse from value-based RL into policy distillation. LSPD preserves policy diversity through exploration while improving rollout efficiency by repeate...
  </details>

- **2026-09-28** — Yinghan Chen, Xiyao Tian, Yizan Dai et al. — [Robot Tool Design from Scratch via Behavior-Aware Hierarchical Optimization](http://arxiv.org/abs/2609.35479v1)
  <details><summary>📄 Abstract</summary>
  The ability to design a tool for a task marks a level of intelligence beyond merely understanding, selecting, or using one. Existing methods for robotic tool design typically optimize a tool's continuous shape and action within a structure that is prescribed or generated beforehand, so the structure itself stays outside the physical optimization loop. We study task-driven tool design from scratch, where tool structure, shape, and action are all derived from the desired physical outcome. Here we ...
  </details>

- **2026-09-28** — Bojian Yin, Shurong Wang, Yuqi Pan et al. — [SOLO: Pretraining Billion-Parameter Language Models with Shared-Output Local Learning](http://arxiv.org/abs/2609.35440v1)
  <details><summary>📄 Abstract</summary>
  Large language models are trained with backpropagation, whose global gradient coordinates all layers but forces each to hold its activations and wait for the gradient to pass back through every deeper layer. Conventional local learning removes this update locking by training each module to predict the target through its own readout, but has not scaled to billion-parameter pretraining. We identify these private readouts as a key weakness, since they leave each module without information from deep...
  </details>

- **2026-09-28** — Dewen Liu, Zixuan Li, Jonathan Pan et al. — [From Input to Output: A Flexible Agent for Dual-End Interpretation of Sparse Autoencoder Features](http://arxiv.org/abs/2609.35367v1)
  <details><summary>📄 Abstract</summary>
  Sparse autoencoders (SAEs) are an important tool for mechanistic interpretability, but interpreting their many features remains challenging. Existing methods characterize input-side activation patterns and output-side intervention effects, yet often leave their functional connection implicit, while input-side evidence collection typically relies on costly large-corpus scans. We introduce functional interpretation, which characterizes an SAE feature as a mapping from its activating input semantic...
  </details>

- **2026-09-28** — Simon Klüttermann, Xueying Ding, Leman Akoglu — [From Data to Program: Fast & Direct Generative Program Inference from Empirical Data](http://arxiv.org/abs/2609.35348v1)
  <details><summary>📄 Abstract</summary>
  Estimating probability densities from a finite set of samples typically requires dataset-specific model fitting. We introduce PRODiGI, a pretrained data-to-program model that infers an explicit, executable generative program in a single forward pass. Pretrained on synthetic datasets paired with their ground-truth programs, PRODiGI accommodates diverse generative families and data dimensionalities through template prediction and non-autoregressive program parameter decoding. Its inferred programs...
  </details>

- **2026-09-28** — Riccardo Porcedda — [Jev thinks "I don't know'', but doesn't say it: Introducing Sys1Cal-v1 Dataset for Probability Calibration](http://arxiv.org/abs/2609.35342v1)
  <details><summary>📄 Abstract</summary>
  The appearance of Jev marked the era of System One Models, foundation models that return structured decisions with probability distributions rather than text. Aside from low cost and great speed, Jev's central promise is that these probabilities are calibrated: such claim is not backed by any public test and available external benchmarks evaluate confidence calibration, not whether every returned option probability has the right numerical meaning. To tackle this issue, we introduce Sys1Cal-v1, a...
  </details>

- **2026-09-28** — Shengqin Wang, Jie Jin, Yu Cheng et al. — [TMCS: Tool-Grounded Multi-Agent Reasoning for Compositional Chemical Problem Solving](http://arxiv.org/abs/2609.35336v1)
  <details><summary>📄 Abstract</summary>
  Despite the promise of Large Language Models (LLMs) in computational chemistry, rigorous combinatorial chemistry problems remain difficult because they require quantitatively constrained molecular modification, candidate validation, and systematic revision after failed attempts. Existing tool-augmented chemical agents demonstrate useful planning and tool use, but they rarely provide a unified loop for property-driven molecular optimization and workflow-level composition. To bridge this gap, we p...
  </details>

- **2026-09-28** — Zipei Yu, Yue-Jiao Gong, Zeyuan Ma et al. — [Hyper Algorithm Design Agent: Evolving Learnable Optimizer from Zero](http://arxiv.org/abs/2609.35328v1)
  <details><summary>📄 Abstract</summary>
  Meta-Black-Box Optimization (MetaBBO) is one of the highlights in the recent AI for Optimization trend. This paradigm's bi-level workflow leverages the learnable algorithm design policy at meta level to ensure the performance and generalization improvement on the low-level optimization task. While MetaBBO helps advance the performance lower bound of the resulted optimization system, it is currently handcrafted and customized case by case to adapt different optimization problems, which inevitably...
  </details>

- **2026-09-28** — Ghazal Fazelnia, Paul Gigioli, Eliza Klyce et al. — [Textual User Taste: Natural-Language User Context for Foundation-Model Recommender System at Scale](http://arxiv.org/abs/2609.35285v1)
  <details><summary>📄 Abstract</summary>
  Foundation model recommender systems require user context that can be consumed by large language models, reasoned over, and refined through natural-language interaction. Traditional behavioral embedding vectors remain highly effective for retrieval and ranking, but they are opaque to users and not natively expressed for language model workflows. We present Textual User Taste, a system that generates structured natural-language taste profiles from listening behavior, interaction signals, content ...
  </details>

- **2026-09-28** — Yizhou Fang, Siyue Chen, Zimo Qi et al. — [When Words Speak Louder than Images: Towards Understanding Language Bias in Vision-Language Models](http://arxiv.org/abs/2609.35272v1)
  <details><summary>📄 Abstract</summary>
  Despite substantial progress across downstream applications, vision-language models (VLMs) remain susceptible to language bias, often prioritizing linguistic cues over visual evidence and consequently producing incorrect predictions. Prior studies have proposed various approaches to understanding and mitigating language bias in VLMs, yet their findings often conflict due to the difficulty of tracing how language bias propagates within black-box VLMs. Building on the word completion task, we trac...
  </details>

- **2026-09-28** — Niayesh Afshordi, Kristina Giesel — [A Cuscuton Representation of the Loop Quantum Cosmology Bounce](http://arxiv.org/abs/2609.35222v1)
  <details><summary>📄 Abstract</summary>
  Loop Quantum Cosmology (LQC) replaces the big bang singularity of the homogeneous universe by a bounce, usually described by the modified Friedmann equation $H^2=ρ(1-ρ/ρ_c)/(3M_p^2)$. We show that this background dynamics follows from a local cuscuton effective theory, whose scalar equation is a constraint rather than a wave equation. One way to establish this is to write the cuscuton in terms of an angular coordinate $θ$, identified with the LQC polymerization angle $2λb$. Its constraint gives ...
  </details>

- **2026-09-28** — Yixin Peng, Er Jin, Diego Collarana et al. — [Temporal Heterogeneous Graph Pretraining for Relational Deep Learning](http://arxiv.org/abs/2609.35219v1)
  <details><summary>📄 Abstract</summary>
  Relational deep learning models database rows and foreign-key links as a heterogeneous graph for prediction from record attributes and relational context. These graphs contain two distinct temporal signals: record age changes with the prediction cutoff, while intervals between observed records remain fixed. Prior work often treats time as a single signal or studies temporal representation and pretraining separately. We investigate how explicitly encoding both signals affects temporal pretraining...
  </details>

- **2026-09-28** — Kilian Bänziger, Sonia Laguna, Markus Kreft et al. — [ConRAG: Lightweight inference of multi-hop relations](http://arxiv.org/abs/2609.35193v1)
  <details><summary>📄 Abstract</summary>
  Understanding how two entities are connected often requires tracing multi-hop relations across documents to identify intermediate entities and supporting evidence that explain a connection. This is a task that appears frequently in scientific research and other knowledge-intensive analyses. We formalise this setting as multi-hop relation inference: given two known endpoint entities, we aim to recover the bridge entities and evidence-grounded reasoning chains that connect them across a document c...
  </details>

- **2026-09-28** — Suwesh Prasad Sah — [Beneath the Tokens: A Performance Engineering Study of Multi-Token Prediction in GPU-Accelerated LLM Inference](http://arxiv.org/abs/2609.35188v1)
  <details><summary>📄 Abstract</summary>
  Autoregressive large language model inference repeatedly invokes the target model to generate one token at a time, making generation sensitive to GPU memory movement and sequential execution. This study evaluates two-token multi-token prediction (MTP) against autoregressive decoding in a controlled single-request deployment on an NVIDIA A10G GPU. A 360-request benchmark covered plain-text, reasoning-intensive, and tool-calling workloads, while runtime telemetry, Nsight Systems, PyTorch Profiler,...
  </details>

- **2026-09-28** — Siddhant Jain, Anna Lea Reinwarth, Dimitra Tsovaltzi et al. — [Toward a Culturally Adapted Chinese Language Agent: A Wizard-of-Oz Study of Nonverbal Behavior in Chinese-German Intercultural Interaction](http://arxiv.org/abs/2609.35150v1)
  <details><summary>📄 Abstract</summary>
  Successful intercultural communication requires more than grammatical competence. It demands sensitivity to culturally embedded social norms whose violation triggers subtle but meaningful nonverbal responses. For German learners of Mandarin Chinese, acquiring this sensitivity is critical yet poorly supported by existing language-learning agents. We present a Wizard-of-Oz (WoZ) study design and supporting real-time system for collecting multimodal behavioral data from native Chinese speakers reac...
  </details>

- **2026-09-28** — Haodong Zhu, Yangyang Ren, Changbai Li et al. — [GraphHCA: Closed-Form Hindsight Credit Assignment for Long-Horizon LLM Agents](http://arxiv.org/abs/2609.35084v1)
  <details><summary>📄 Abstract</summary>
  Group-based reinforcement learning (RL) has advanced large language models (LLMs) and is increasingly extending to agentic tasks, where sparse terminal rewards make step-level credit assignment essential. Existing methods assign credit from what follows an action in sampled rollouts, but do not explicitly capture its retrospective relation to the realized outcome. Hindsight credit assignment (HCA) instead attributes credit through the ratio of hindsight to behavior-policy probabilities, but esti...
  </details>

- **2026-09-28** — Jiashen Ren, Wenlin Zhang, Bohan Zhang et al. — [Persona Following Is Not Selective Control: The Neutrality Gap in LLM User Simulation](http://arxiv.org/abs/2609.35036v1)
  <details><summary>📄 Abstract</summary>
  Persona prompting is widely used to construct user simulations with large language models (LLMs), yet it relies on a largely untested assumption: specifying one user attribute should change that attribute alone. We test this assumption and identify a systematic failure of selective control: across all eight black-box LLMs we audit, changing a target attribute also shifts responses on unspecified, non-target attributes. For example, describing a user as more risk-seeking shifts color choices, eve...
  </details>

- **2026-09-28** — Nicolas Dahan, Fran{\cc}ois Yvon, Rachel Bawden — [TermJudge: A Document-Level Metric Judging, Not Counting, Terminology in Machine Translation Evaluation](http://arxiv.org/abs/2609.35017v1)
  <details><summary>📄 Abstract</summary>
  Existing automatic metrics for evaluating terminological use in machine translation (MT) penalise any divergence from a fixed reference, conflating translation errors with the valid terminological variation that human translators routinely produce. We introduce TermJudge, a document-level terminology metric that assigns an interpretable verdict to every term occurrence: glossary-conforming occurrences are settled deterministically, while divergences are assessed under a two-step LLM-as-judge pro...
  </details>

- **2026-09-28** — Yinhong Liu, Zhili Tan, Zilin Wang et al. — [Action-Space Shaping for LLM Agents: Measuring and Mitigating Tool-Schema Bias](http://arxiv.org/abs/2609.34971v1)
  <details><summary>📄 Abstract</summary>
  Large Language Models (LLMs) have shown strong performance on tool-use agentic tasks when given a fixed tool schema. Yet a tool schema is not the action space of an agent; it is merely one interface representation of it. The same executable action can be exposed through many different, functionally equivalent tool definitions, and an agent that has truly learned a task should behave consistently across them. We show that current agents often do not, a phenomenon we term schema bias. To study thi...
  </details>

- **2026-09-28** — Arnau Mayoral-Macau, Jiaqi Lai, Manala Tyobeka et al. — [KITA AI: A Multi-Agent LLM System for Pluralistic Policy Deliberation](http://arxiv.org/abs/2609.34890v1)
  <details><summary>📄 Abstract</summary>
  Public policies addressing urgent social and environmental challenges need to explicitly consider the diverse, often conflicting perspectives of the affected stakeholders. Despite computational decision-support approaches increasingly offering recommendations across diverse human value systems, they still tend to deliver a single consensus-driven outcome. We present KITA AI, a modular system in which multiple large language model agents, each grounded in distinct demographic stakeholder personas...
  </details>

- **2026-09-28** — Paul Primus, Gerhard Widmer — [On Temporal Binding in Large Audio Language Models](http://arxiv.org/abs/2609.34806v1)
  <details><summary>📄 Abstract</summary>
  Reasoning about temporal structure of audio recordings requires Large Audio Language Models (LALMs) to associate sound events with their temporal position. Understanding the underlying mechanisms is a first step toward diagnosing failures and identifying model components that may need improvement. Using mechanistic interpretability, we investigate how temporal information is represented and bound to sound events in three open-source LALMs. We find that across all three, event-specific location b...
  </details>

- **2026-09-28** — Yadong Wang, Siping Yue, Yu Tian et al. — [Before the Token Commits: Trajectory-Level Benchmarking of Visual Hallucinations in Diffusion VLMs](http://arxiv.org/abs/2609.34772v1)
  <details><summary>📄 Abstract</summary>
  Multimodal diffusion language models generate responses by iteratively unmasking tokens, making each answer the endpoint of a multi-step trajectory rather than an immediate commitment. Hallucination benchmarks built for autoregressive models evaluate only the final output, and therefore cannot determine whether an unsupported claim in diffusion VLMs appears late or has already stabilized before any answer token is revealed. We introduce DynaHall, a trajectory-level benchmark of annotation-backed...
  </details>

- **2026-09-28** — Bingo Zhang, Haochuan Lu, Zongjie Li et al. — [LongPuzzleBench: Evaluating GUI Agents on Long-Horizon Visual Puzzles](http://arxiv.org/abs/2609.34769v1)
  <details><summary>📄 Abstract</summary>
  GUI agents need long-horizon visual reasoning: they must interpret a changing interface while keeping a multi-step plan viable as earlier actions constrain later ones. Existing benchmarks evaluate grounding, computer use, and game play, but rarely test whether agents stay coherent across long chains of coupled decisions. Long-horizon visual puzzles expose this capability directly: a legal move that looks like progress can make the puzzle unsolvable, and the loss shows only several moves later. W...
  </details>

- **2026-09-28** — Vasilis Perifanis, Nikolaos Pavlidis, Symeon Symeonidis — [SeLMRoute: Probabilistic Semantic Evidence for Large Language Model Routing](http://arxiv.org/abs/2609.34736v1)
  <details><summary>📄 Abstract</summary>
  Large language model (LLM) routing aims to select the most suitable model for each incoming query. Most existing routers learn this decision directly from query embeddings, model representations, preference data, or clusters of similar examples. Such approaches can be effective, yet the representation used for routing rarely states what a query actually requires. We introduce SeLMRoute, a routing framework that separates the extraction of candidate-independent semantic evidence from the learning...
  </details>

- **2026-09-28** — Wangxuan Fan, Xiaoyu Nie, Zhoutian Shi et al. — [From Preference to Reciprocity: Decentralized Matching with Empirically Grounded LLM-agent Based Modeling](http://arxiv.org/abs/2609.34679v1)
  <details><summary>📄 Abstract</summary>
  Bipartite matching is a fundamental problem in game theory and market design. Classical approaches such as Gale--Shapley assume complete preferences and centralized computation, whereas many real-world matching processes are decentralized, asynchronous, and shaped by sequential interaction under limited information. We propose a dynamic bipartite matching framework that combines large language model (LLM) agents with contextual bandits. In a simulated Chinese marriage market, economically ground...
  </details>

- **2026-09-28** — Etienne Boursier, Nicolas Flammarion — [Two-Timescale Fine-tuning Provably Learns New Features for Two-Layer ReLU Networks](http://arxiv.org/abs/2609.34667v1)
  <details><summary>📄 Abstract</summary>
  Fine-tuning pre-trained models on specialized tasks with scarce data is central to modern deep learning. Despite its empirical success, theoretical understanding of fine-tuning remains limited. We introduce a Gaussian multi-index setting to study fine-tuning from pre-trained weights, where the teacher network has $m+1$ features, $m$ of which are learned during pre-training and one of which must be learned during fine-tuning. For two-layer ReLU networks, we show that two-timescale training, i.e.,...
  </details>

- **2026-09-28** — Sergei Kholkin, Evgeny Burnaev, Alexander Korotin — [Tilted Schrödinger Bridge Matching](http://arxiv.org/abs/2609.34642v1)
  <details><summary>📄 Abstract</summary>
  Schrödinger bridges provide an entropy-regularized framework and a principled solution for unpaired domain translation. In practice, a pretrained bridge may need to be adapted to human preferences or physical constraints through a reward a problem closely related to reward tilting in diffusion models but underexplored for Schrödinger bridges. We introduce Tilted Schrödinger Bridge Matching (TSBM), a post-training method for fine-tuning a learned bridge $P$ between source $p_0$ and target $p_1$ t...
  </details>

- **2026-09-28** — Danilo Gusicuma, André Freitas — [MechReasoner: A Simulator and Benchmark for Mechanistic Reasoning in Qualitative Physics](http://arxiv.org/abs/2609.34636v1)
  <details><summary>📄 Abstract</summary>
  This work introduces MechReasoner, a mechanistic qualitative simulator grounded in confluence-based qualitative physics, together with a benchmark for mechanistic inference. Current large language models (LLMs) generate fluent mechanistic descriptions that do not reliably follow from underlying structural and causal constraints. The benchmark tests whether answers preserve simulator-licensed ambiguity, quantified claims, episode-graph transition evidence, repairs, and trace-support judgments. It...
  </details>

- **2026-09-28** — Jarod Lévy, Mathurin Videau, Jad Yehya et al. — [RoPE is Dead, Long Live RoPE: Towards Scalable Data-aware Positional Encodings](http://arxiv.org/abs/2609.34556v1)
  <details><summary>📄 Abstract</summary>
  Transformers process tokens without any inherent notion of order, making positional encoding a fundamental requirement rather than an architectural refinement. Rotary Position Embedding (RoPE) has become the default positional encoding in modern language models, yet it is heavily biased toward nearby tokens. Existing alternatives have been evaluated under different settings, leaving the literature fragmented and without a clear replacement. We bring structure to this landscape by examining a spe...
  </details>

- **2026-09-28** — Binbin Yong, Zhao Su, Lan Guo et al. — [LLN: Learnable Lens Networks for Parameter-Efficient Long-Horizon Dynamical Prediction](http://arxiv.org/abs/2609.34493v1)
  <details><summary>📄 Abstract</summary>
  Explicit residual connections of the form (x+f(x)), often combined with normalization layers, have become a standard strategy for training very deep neural networks. However, residual addition primarily provides an algebraic shortcut for gradient propagation, while leaving the evolution of feature geometry across layers largely unconstrained. We introduce Learnable Lens Networks (LLN), a physics-inspired architecture that replaces direct feature-space residual accumulation with learnable optical...
  </details>

- **2026-09-28** — Yijie Sun, Sanquan Sun, Yanda Zhu et al. — [Escaping Local Views: Discovering Latent Concepts for Interpretable Multi-Agent Reinforcement Learning](http://arxiv.org/abs/2609.34459v1)
  <details><summary>📄 Abstract</summary>
  Efficient cooperation is challenging due to the usual partial observability of each agent in multi-agent reinforcement learning. Recurrent networks encode local interaction histories, but their hidden representations provide limited insight into the information underlying individual decisions. To address these challenges, we propose a novel interpretable framework, called escaping local views (ELV), which introduces semantically structured latent concepts to render policy decisions transparent. ...
  </details>

- **2026-09-28** — Linjian Meng, Siyuan Gan, YuHan Li et al. — [Unbiased Top-$k$ Estimation for On-Policy Distillation](http://arxiv.org/abs/2609.34447v1)
  <details><summary>📄 Abstract</summary>
  On-policy distillation (OPD) is becoming an important component of large language model (LLM) post-training for transferring the reasoning capability of a strong teacher LLM to a weaker student LLM. OPD trains the student by minimizing the reverse KL divergence between the teacher and the student via rollouts generated by the student's policy. However, estimating the gradient of the reverse KL divergence in OPD remains a challenge. Using only the sampled token from the student-generated rollout ...
  </details>

- **2026-09-28** — Chuiyang Meng, Wenlu Yu, Ming Tang et al. — [Social Circuits behind Multi-agent Echo Chambers](http://arxiv.org/abs/2609.34444v1)
  <details><summary>📄 Abstract</summary>
  Language-model agents exchange messages to combine evidence, but their communication can also create echo chambers that reinforce shared errors. However, overall task performance does not explain how a message changes the receiving agent's internal activations and affects its decision. In this work, we introduce Social Circuits, a framework for tracing message effects through receiver activations. We compare the receiver's answers before and after changing a message. Then, we restore selected ac...
  </details>

- **2026-09-28** — Tong Qiao, Ao Zhou, Yingjie Qi et al. — [MegaGraph: Towards Efficient Training of Large-Scale Graph Transformers with Automated Hybrid Parallelism](http://arxiv.org/abs/2609.34420v1)
  <details><summary>📄 Abstract</summary>
  Graph Transformers (GTs) offer superior representation capabilities by overcoming the depth limitations and over-smoothing issues of traditional Graph Neural Networks (GNNs). However, scaling GTs to large graphs poses critical bottlenecks. Specifically, the attention score matrix and its associated topology-aware bias matrix jointly incur significant per-layer memory overhead, and heavy graph embedding layers result in severe workload imbalances. These characteristics are unique to GT training a...
  </details>

- **2026-09-28** — Junhao Zhang, Feiran Hu, Xiao Hu et al. — [Correcting to Predict: Pseudo-Value Correction for Multimodal Attribute Value Extraction](http://arxiv.org/abs/2609.34383v1)
  <details><summary>📄 Abstract</summary>
  Product attribute value extraction (AVE) is a fundamental task in e-commerce, aiming to identify specific values of predefined attributes from multimodal product profiles such as text and images. While multimodal large language models (MLLMs) have shown promise for AVE, they face challenges in extracting implicit attributes that require joint reasoning over visual and textual cues, often confusing semantically similar values. However, existing methods often fail to resolve such ambiguities becau...
  </details>

- **2026-09-28** — Bo Xue, Ji Cheng, Shen-Huan Lyu et al. — [Test-Time Scaling via Budgeted Multi-Attribute Verification](http://arxiv.org/abs/2609.34322v1)
  <details><summary>📄 Abstract</summary>
  Verifying LLM-generated answers under a shared computational budget requires jointly deciding which candidates to inspect and which verification attributes to evaluate. We formulate this problem as multi-attribute good-arm identification under a global budget: each candidate is an arm evaluated along several costly attributes, and the goal is to certify as many candidates as possible whose mean scores exceed the prescribed thresholds on all attributes. We propose \textsc{BMA-GAI}, an algorithm t...
  </details>

- **2026-09-28** — Xunyi Zhao, Jian Zhou, Sihao Lin et al. — [NavHarness: Towards Lifelong Embodied Navigation](http://arxiv.org/abs/2609.34276v1)
  <details><summary>📄 Abstract</summary>
  Frontier models can now perform well on individual embodied navigation tasks through multi-round multimodal reasoning with simple tools. Across successive tasks, however, an agent must also rely on an evolving map and earlier search records, both of which may be incomplete or conflict with new observations. We present NavHarness, a training-free embodied harness towards lifelong navigation that makes memory processing part of the navigation loop. During navigation, its multi-round agentic sessio...
  </details>

- **2026-09-28** — Yunhao Feng, Yifan Ding, Yuxiang Xie et al. — [AdaGuard: An Adaptive Guard Model with User-defined Policies](http://arxiv.org/abs/2609.34241v1)
  <details><summary>📄 Abstract</summary>
  Guard models support the safe deployment of language model agents, but fixed risk taxonomies limit their ability to accommodate requirements that vary across applications and tasks. Under user-defined policies, detecting violations requires interpreting both the applicable rules and the agent's behavior, since identical actions can receive different judgments under different policies. To support learning this capability, we introduce AdaptiveSafety, a dataset of 10,939 training examples and 1,00...
  </details>

- **2026-09-28** — Zhuoxiong Gan, Qiang Dong — [Measuring and Mitigating Identity-Cue Preference Drift in LLM-based Recommender Systems](http://arxiv.org/abs/2609.34229v1)
  <details><summary>📄 Abstract</summary>
  In large language model-based recommender systems, identity cues embedded in prompts can steer recommendations toward group-level patterns even when the underlying behavioral evidence remains unchanged. We introduce PromptShift, an interpretable, training-free framework for quantifying and mitigating such identity-cue preference drift. We define Drift as the divergence, in both item membership and ranking order, between a recommendation list generated under an identity-cued prompt and the refere...
  </details>

- **2026-09-28** — Qiyong Zhong, Mao Zheng, Mingyang Song et al. — [USA: Update-aware SAM for Cross-domain On-Policy Disitllation of Language Agents](http://arxiv.org/abs/2609.34225v1)
  <details><summary>📄 Abstract</summary>
  On-policy distillation instils multi-turn agentic reasoning through dense token-level supervision on the student's own trajectories, but a single domain saturates early, so further supervision has to be drawn from other domains. Multi-domain data mixing is the most direct way of incorporating them, at the cost of conflicts between their data distributions and of retraining the entire model whenever one domain is revised. Model merging avoids both by distilling every domain independently and fusi...
  </details>

- **2026-09-28** — Jihoo Jung, Youngjoon Jang, Hyebin Cho et al. — [Uncovering Ordinal-Matching Bias in Audio-Visual LLMs](http://arxiv.org/abs/2609.34223v1)
  <details><summary>📄 Abstract</summary>
  This work aims to improve how audio-visual large language models (AVLLMs) associate speech with the correct visible speaker in multi-speaker scenes. We find that current AVLLMs frequently fail at this task, and analyze the nature of these failures. To this end, we construct a synthetic diagnostic dataset in which multiple visible speakers each utter a single word. Analysis on this corpus reveals a consistent error pattern across three recent open-source AVLLMs: models attribute utterances by sim...
  </details>

- **2026-09-28** — Zirui Zhu, Hailun Xu, Xuanlei Zhao et al. — [Loop Dropout: Regularizing Shared Updates in Looped Language Models](http://arxiv.org/abs/2609.34218v1)
  <details><summary>📄 Abstract</summary>
  Looped language models separate computational depth from parameter count by repeatedly applying the same transformer block. Adapting these models requires a shared update that remains effective as hidden states evolve throughout the recurrent computation. Our empirical analysis reveals a pronounced late-loop bias in standard low-rank adaptation (LoRA): the shared update is more effective at later loop positions. This imbalance motivates training shared updates under varying combinations of their...
  </details>

- **2026-09-28** — Bowen Dong, Yilong Fan, Tengyu Pan et al. — [X-MoD: Practical Scaling Laws for Sparse-Depth Routing Beyond Mixture-of-Depths](http://arxiv.org/abs/2609.34212v1)
  <details><summary>📄 Abstract</summary>
  Mixture-of-Depths (MoD) enables conditional computation across Transformer depth by routing only a subset of tokens through selected layers, but its original one-sparse--one-dense alternation tightly couples total capacity to active capacity and limits sparse-depth scaling. We introduce X-MoD, a scalable sparse-depth architecture that decouples token sparsity from anchor stride, allowing total parameter count to grow while keeping active-equivalent capacity nearly fixed. To make deep sparse rout...
  </details>

- **2026-09-28** — Mingyuan Hu, Vivek Shende, Dinglong Wang — [A proper dg algebra which does not cogenerate](http://arxiv.org/abs/2609.34193v1)
  <details><summary>📄 Abstract</summary>
  Keller's strong form of the homological conjectures asserts: any finite dimensional algebra cogenerates its unbounded derived category of modules. Here we record an example of a (coconnective) dg algebra with finite dimensional cohomology, which does not cogenerate its module category, along with some related phenomena: a smooth dg category whose dualizing bimodule fails to be nondegenerate, and a nontrivial fully faithful left Calabi-Yau morphism. All examples and most proofs were produced by C...
  </details>

- **2026-09-28** — Jiaming Tian, Liyao Li, Wentao Ye et al. — [TableSeek: Structure-Preserving Agentic Evidence Seeking over Heterogeneous Table Corpora](http://arxiv.org/abs/2609.34157v1)
  <details><summary>📄 Abstract</summary>
  Open-domain table retrieval seeks tables that contain sufficient evidence for answering a question or verifying a claim. Yet semantic relevance is often misleading: topically similar tables may lack the required facts, while answer-bearing evidence is often confined to a few cells whose meaning depends on surrounding schema and table context. Heterogeneous schemas, value formats, and serializations further weaken one-shot matching.   We present TableSeek, a structure-preserving agentic search fr...
  </details>

- **2026-09-28** — Renxiang Wang, Jiaming Cui — [Evo2Team: When Do Evolved Skills Transfer? From Selection to Deployment](http://arxiv.org/abs/2609.34135v1)
  <details><summary>📄 Abstract</summary>
  A skill bank that helps one multi-agent system may leave another's behavior unchanged. A transferred rule helps only when target agents act on it successfully. We study this path for routing and communication skills in Count-Frequency and AgentsNet, using teams of 4--32 agents and GPT and Qwen model ladders. Source evolution meets a joint quality, cost, model-tier, and confirmation goal in 14 of 16 settings. We then evaluate Evo2Team, which selects, adapts, and confirms source skills for the tar...
  </details>

- **2026-09-28** — Yao Long Teng, Jiayi Cai, Bo An — [JET: Judge-Guided Evolution at Test Time for Agent Programs](http://arxiv.org/abs/2609.34126v1)
  <details><summary>📄 Abstract</summary>
  An agent's executable program governs how it uses tools, processes observations, and responds to failures. Evolving this program at test time can help adaptation, but deciding which changes to retain is difficult when true rewards are unavailable. Execution traces provide evidence of agent behavior, yet interpreting that evidence requires a judge that remains useful as tasks and candidate programs change. We introduce Judge-Guided Evolution at Test Time (JET), which evolves an executable judge o...
  </details>

- **2026-09-28** — Vishalakshi Arumugam, Dan Schumacher, Veronica Rammouz et al. — [Understanding Clinical Cognitive Dialogues Using Large Language Models](http://arxiv.org/abs/2609.34125v1)
  <details><summary>📄 Abstract</summary>
  In-person cognitive assessment is both a test and an interaction. Clinicians explain tasks, repair misunderstandings, and adapt to patient responses, while patients may hesitate, seek clarification, or disengage. Yet clinical dialogue resources rarely label the interaction structure needed to study these behaviors at scale. We present an de-identified corpus of 33 cognitive assessment conversations with 8,250 utterances annotated for three speaker roles and 56 dialogue acts. We use this corpus t...
  </details>

- **2026-09-28** — Medha Dandu, Sriram Sankar, Giovanny Espitia et al. — [(Sub)nanoscale Visualization of Reconstruction-Driven Moiré Exciton Localization and Delocalization](http://arxiv.org/abs/2609.34104v1)
  <details><summary>📄 Abstract</summary>
  Spectral fingerprints in optical absorption and emission have typically been used as a signature of exciton localization in twisted moiré bilayers. However, the mechanism by which excitons become confined to specific stacking sites and their associated optical signature is experimentally unresolved. Here, we directly visualize in real space how tuning the change in extent of structural reconstruction leads to localization and delocalization of moiré excitons in the WSe2/WS2 moiré superlattice. U...
  </details>

- **2026-09-28** — Yucong Cao, Chenqi Li, Tingting Zhu — [When Is an SAE Feature Interpretable? A Validation Ladder for EEG Foundation Models](http://arxiv.org/abs/2609.34091v1)
  <details><summary>📄 Abstract</summary>
  Sparse autoencoders (SAEs) decompose dense model activations into discrete latents, making individual features easy to interpret--and easy to misinterpret. In EEG foundation models, this creates a tempting inference: if removing alpha-band activity strongly changes a latent's activation, one might conclude that the latent represents alpha activity. Across 27 settings spanning three backbones, three EEG datasets, and three network depths, this interpretation initially appears compelling: alpha re...
  </details>

- **2026-09-28** — Yunfei Bai, Enrico Chionna, Akash Amol et al. — [K-OPSD: Verifiable On-Policy Self-Distillation for Post-Training Vision-Language Models on AEC Drawings](http://arxiv.org/abs/2609.34082v1)
  <details><summary>📄 Abstract</summary>
  Interpreting architecture, engineering, and construction (AEC) drawings is hard for general Multimodal Large Language Models (MLLMs) and vision-language models (VLMs). We introduce K-OPSD, a VLM post-training methodology for improving AEC drawing understanding. Building on On-Policy Self-Distillation (OPSD) with verifiable supervision, we construct a teacher from the model's own best-of-N generations, certified by a process-level verifier, and rescue failed prompts by resampling under a hint tha...
  </details>

- **2026-09-28** — Yuezhou Ma, Huikun Weng, Jialong Wu et al. — [PhysFieldBench: Can Multimodal Models Understand Physical Fields?](http://arxiv.org/abs/2609.34072v1)
  <details><summary>📄 Abstract</summary>
  Multimodal large language models (MLLMs) are increasingly envisioned as core components of scientific and engineering agents, yet their ability to interpret physical fields remains poorly understood. Existing physics benchmarks largely emphasize textbook problem solving or intuitive physical reasoning, leaving open whether MLLMs can infer physically meaningful information from continuous field observations. We introduce PhysFieldBench, a benchmark comprising 24 tasks and 1,160 evaluation example...
  </details>

- **2026-09-28** — Ahmadreza Jeddi, Enming Zhang, Jasper Gerigk et al. — [SCOPD: Sparse-Context On-Policy Self-Distillation for Efficient Vision-Language Models](http://arxiv.org/abs/2609.34044v1)
  <details><summary>📄 Abstract</summary>
  Reasoning vision-language models (VLMs) process images and videos as long sequences of visual tokens, making inference expensive. Training-free token pruning reduces this cost, but aggressive compression can sharply degrade performance, often attributed to irreversible loss of task-relevant visual information. We show that this explanation is incomplete. In a fixed-context Pass@K analysis, repeated sampling from the same pruned visual representation recovers many examples missed by greedy decodi...
  </details>

- **2026-09-27** — Zhuowen Liu, Zhixuan Wang — [HESP: Separating What to Probe from When to Stop in Local LLM Alert-Triage Agents](http://arxiv.org/abs/2609.33446v1)
  <details><summary>📄 Abstract</summary>
  Security operations centers receive far more alerts than analysts can investigate, and organizations that cannot send their telemetry to hosted models must automate triage with small open-weight LLMs on their own hardware. Current LLM agents leave the investigation procedure to the model, and small local models fail at it: they probe without converging, never commit to a verdict, or dismiss real attacks. In this paper, we present HESP, a controller that holds the investigation procedure outside ...
  </details>

- **2026-09-27** — Nan Huang, Mario Tapia-Pacheco, Kun Zhou et al. — [DISCERN: Can AI Agents Work Like Scientists and Guide Discovery?](http://arxiv.org/abs/2609.33357v1)
  <details><summary>📄 Abstract</summary>
  Reliable automated research requires agents to vet data, verify analyses, and generate hypotheses grounded in trustworthy evidence, potentially reducing routine scientific workload while allowing scientists to focus on interpretation and discovery. Existing benchmarks often only assess analytical task completion or hypothesis generation separately rather than testing whether reliable evidence supports valid and novel claims. We introduce DISCERN (Data Integrity and Scientific Capability: Evidenc...
  </details>

- **2026-09-27** — Matei-Ioan Stan, Oliver Rhodes — [ADPTNet: Adaptive with Prescriptive Timescales Non-Linear SSM for Sequence Modelling](http://arxiv.org/abs/2609.34034v1)
  <details><summary>📄 Abstract</summary>
  A central aim of neuromorphic computing is to provide a viable alternative to highly energy-intensive Transformer-based AI. However, efficient alternatives struggle to capture the set of qualities that have secured the Transformer's status as the de facto standard in sequence modelling. Any realistic contender must be data-adaptive, able to capture long-range dependencies, and GPU-parallelisable, but also non-linearly recurrent to enable complex reasoning. Based on evidence suggesting the audito...
  </details>

- **2026-09-27** — Cecilia Bolaños, Luciana Ferrer, Magdalena Fuentes — [Uncovering shortcut learning in audio classifiers by discovering recurring concepts in temporal explanations](http://arxiv.org/abs/2609.34030v1)
  <details><summary>📄 Abstract</summary>
  Correlations between events in machine learning datasets may result in shortcut learning, where models learn to predict the target event based on the presence of a correlated event. When these correlations are spurious -- arising from data collection artifacts -- models are likely to perform poorly in practice. We propose a pipeline to uncover shortcut learning in audio classifiers by discovering recurring concepts in their temporal explanations. Specifically, we isolate audio segments that expl...
  </details>

- **2026-09-27** — Chunming He, Rihan Zhang, Lei Xu et al. — [UnfoldCRF: Structured Mask Refinement with Image-Conditioned Latent Regions](http://arxiv.org/abs/2609.33996v1)
  <details><summary>📄 Abstract</summary>
  Learned mask refiners improve segmentation accuracy, but it is hard to tell how much of the improvement comes from explicit structure rather than from extra capacity, and whether it holds up when the mask generator or its error distribution changes. UnfoldCRF treats refinement as inference in a conditional random field over pixel labels and latent region variables. Its energy has a corrected unary term, learned local pairwise interactions, and image-conditioned latent-region consistency, with a ...
  </details>

- **2026-09-27** — Hasan Amin, Ming Yin, Rajiv Khanna — [Simple Diffusion Language Models Are More Effective Few-Step Generators Than Reported](http://arxiv.org/abs/2609.33947v1)
  <details><summary>📄 Abstract</summary>
  Diffusion language models (DLMs) promise fast parallel generation, yet high-quality samples often require large number of refinement steps, which diminishes their advantage in practice. This has led to massive interest in and rapid development of new methods for effective few-step generation. We show that much of the supposed quality gap at few steps can instead arise from a suboptimally configured sampler. Modest sampler sharpening, without any model retraining, enables a couple years old maske...
  </details>

- **2026-09-27** — Adil Alshammari, Sareh Assiri, Hayretdin Bahsi — [A2A-ForensicTrace: Offline Verification of Tamper-Evident A2A Runtime Evidence](http://arxiv.org/abs/2609.33924v1)
  <details><summary>📄 Abstract</summary>
  Security-relevant Agent2Agent (A2A) executions can cross organizational boundaries, leaving investigators without live access to all participating systems. Offline investigation involves checking preserved records and their cross-record relationships for consistency. This paper presents A2A-ForensicTrace, an offline verification layer that converts runtime observations into typed records, derives protocol-relevant relationships, and commits both under an incident-trace root. An Ed25519-signed re...
  </details>

- **2026-09-27** — Adrian de Wynter — [Population Physics, Population Problems: Safety and Emergence in LLM Societies](http://arxiv.org/abs/2609.33871v1)
  <details><summary>📄 Abstract</summary>
  The collective behaviour of large language model (LLM) societies is not the sum of their individual outputs. It yields statistically distinct, sometimes-unpredictable phenomena, for which the tools we use to study single agents may not scale. Due to recent incidents involving autonomous agentic systems, however, understanding these systems is paramount. For that we introduce a framework for measuring self-organisation in LLM social systems and apply it to three such systems: a Schelling grid, a ...
  </details>

- **2026-09-27** — Levon Nurbekyan, Samy Wu Fung — [Higher-Order Mean-Field Control Barrier Functions](http://arxiv.org/abs/2609.33852v1)
  <details><summary>📄 Abstract</summary>
  Mean-field control barrier functions (MF-CBFs) enforce swarm safety through constraints on the agents' distribution. Previous formulations, including applications to stochastic coverage and shepherding, use first-order differential inequalities. These cannot directly enforce constraints whose barrier functions yield control-free first derivatives. Thus, we develop the theory of higher-order MF-CBFs, which ensures the positivity of the barrier functionals through higher-order differential inequal...
  </details>

- **2026-09-27** — Carlos J. Costa — [Internet and Enterprise Strategy Revisited: From Digital Connectivity to AI-Enabled Enterprises, 1996 - 2026](http://arxiv.org/abs/2609.33850v1)
  <details><summary>📄 Abstract</summary>
  This paper revisits the 1996 article Internet and Enterprise Strategy and assesses how its propositions were confirmed, transformed, or contradicted as digital connectivity evolved into an AI-enabled enterprise environment by 2026. The reassessment combines historical interpretation with a structured comparison of Internet-enabled capabilities, industry structure, value-chain transformation, platform intermediation, cybersecurity, data governance, artificial intelligence, and digital sovereignty...
  </details>

- **2026-09-27** — Mustafa Ozaytac, Ozge Karadag Atas — [StatD2GAN: When Calibration Masks Generator Quality in Held-Out Evaluation of Synthetic Weather Sequences](http://arxiv.org/abs/2609.33761v1)
  <details><summary>📄 Abstract</summary>
  Generative models for multivariate weather series are routinely evaluated with pooled distributional metrics computed after marginal calibration. We show this practice can invalidate architectural conclusions, and rebuild the evaluation of StatD2GAN, a three-discriminator GAN with evolutionary weight adaptation, around a held-out protocol: the final two calendar years of each dataset are held out behind a 168 hour embargo, calibration is fitted on the training block only, and all metrics are com...
  </details>

- **2026-09-27** — Ruibin Yuan, Jiahao Pan, Junyan Jiang et al. — [YuE2: Unifying Symbolic and Audio Music Generation at Frontier Quality](http://arxiv.org/abs/2609.33757v1)
  <details><summary>📄 Abstract</summary>
  Symbolic models make melody, harmony, rhythm, and form explicit but typically stop before a finished recording; audio models produce complete songs while leaving composition implicit. We introduce YuE2, which unifies symbolic and audio music generation at frontier quality through symbolic planning. A single AR-NAR Mixture-of-Transformers (MoT) first writes a readable score specifying melody and harmony, expands it into semantic music tokens, and realizes it as full-song audio. In comparisons usi...
  </details>

- **2026-09-27** — Shizhe Liu, Jiayan Gu, Xiangyu Kong et al. — [ResDiffFRG: Residual Diffusion for Multiple Appropriate Facial Reaction Generation](http://arxiv.org/abs/2609.33749v1)
  <details><summary>📄 Abstract</summary>
  In dyadic human speaker-listener conversations, the listener's facial reactions allows the speaker to accurately perceive the listener's emotional states. Since human facial reactions are non-deterministic, the ability to generate multiple appropriate human-like facial reactions is crucial for realistic human-agent interactions. Although diffusion models are naturally suited to such one-to-many generation, existing diffusion-based Multiple Appropriate Facial Reaction Generation (MAFRG) methods a...
  </details>

- **2026-09-27** — Haixiang Sun, Jiefu Zhang, Yinghao He et al. — [Reliable Replay through Spatial Coherence in Online Continual Learning](http://arxiv.org/abs/2609.33725v1)
  <details><summary>📄 Abstract</summary>
  Continually adapting models to new tasks requires retaining earlier knowledge under limited memory and computation. Experience replay addresses this challenge, but priorities based on individual loss increases overlook how related memories respond to the same update and can overemphasize isolated responses. We introduce SPatial coHErent risk control for REplay (SPHERE), a general replay-allocation method applicable across a broad range of learning settings. SPHERE uses a representation kernel to...
  </details>

- **2026-09-27** — Avi Caciularu — [Geometric Inductive Biases for Semi-Supervised Equalization: The Constellation-Aware Transformer](http://arxiv.org/abs/2609.33695v1)
  <details><summary>📄 Abstract</summary>
  Decoding signals over unknown channels with minimal pilot overhead is a critical challenge in next-generation communications. Existing deep learning approaches typically rely on generic encoders that struggle to model long-range temporal dependencies or efficiently capture the channel's physical properties from scarce data. We argue that standard architectures suffer from agnostic estimation gaps, as they must implicitly learn the constellation geometry that is already known. We introduce the Co...
  </details>

- **2026-09-27** — Rylan Schaeffer, Brando Miranda, Joshua Kazdan et al. — [How Strong Is the Evidence for the Artificial Hivemind? Reevaluating Evidence for the Open-Ended Homogeneity of Language Models](http://arxiv.org/abs/2609.33936v1)
  <details><summary>📄 Abstract</summary>
  Recent research argues that language models exhibit pronounced homogeneity in open-ended generation, framing such behavior as an Artificial Hivemind that poses a long-term threat to human creativity. We examine three of its central results. First, the flagship example is that model responses to "Write a metaphor involving time" collapse into two clusters. Visualization, spectral analysis, clustering, and language model labels all contradict this description. The labels record each response's veh...
  </details>

- **2026-09-27** — Han Yang, Yian Wang, Yunlong Song et al. — [DexTaG: Tactile-as-Guidance in Reinforcement Learning for Dexterous Manipulation](http://arxiv.org/abs/2609.33882v1)
  <details><summary>📄 Abstract</summary>
  Glove-based motion capture is emerging as a scalable approach to collecting dexterous-hand demonstration data. However, due to the kinematic gap between the human and robot hand, the recorded human motions cannot be executed directly on the robot, especially for contact-rich tool-use tasks involving in-hand reorientation. Prior work bridges this gap in simulation through reinforcement learning (RL) or trajectory optimization, but the human contact pattern is hard to preserve under such formulati...
  </details>

- **2026-09-27** — Anshuman Singh, Abrar Eyasir, Haseeb Yaqoob et al. — [The Effects of Incremental Instruction Delivery on Language-Model Creative Writing](http://arxiv.org/abs/2609.33738v1)
  <details><summary>📄 Abstract</summary>
  Large language models are increasingly used as interactive writing tools, where users develop stories, revise ideas, and introduce new requirements across multiple turns rather than specifying a complete brief upfront. Yet most evidence on multi-turn instruction degradation comes from tasks with objectively verifiable outcomes, leaving unclear whether incremental interaction harms creative artifacts in ways that explicit requirement checks cannot capture. We study this question using 160 human-a...
  </details>

- **2026-09-27** — Yuexian Li, Yifei Yang, Zouying Cao et al. — [EAT: Expert Account Tracker for Efficient MoE Inference](http://arxiv.org/abs/2609.33614v1)
  <details><summary>📄 Abstract</summary>
  Mixture-of-Experts (MoE) models have emerged as a revolutionary method to scale Transformer models. However, traditional MoE architecture still suffers from inefficiency since a large number of experts are unnecessarily activated. Existing approaches for reducing the number of activated experts often overlook the historical performance of each expert. In this paper, we propose EAT, a novel method called Expert Account Tracker (EAT), which utilizes history-awareness metrics and adaptive threshold...
  </details>

- **2026-09-27** — Liron Soffer, Ravid Shwartz-Ziv, Chen Shani — [LLMs Trust Their Own: Identity-Dependent Conformity in Multi-Agent Systems](http://arxiv.org/abs/2609.33495v1)
  <details><summary>📄 Abstract</summary>
  Large language models (LLMs) are increasingly deployed in multi-agent settings, where agents observe and influence one another, making social influence a key dimension of AI behavior and safety. We investigate whether LLMs' responses depend on the social identity of other agents, beyond the effect of their consensus. We construct judgment tasks with a single correct answer, and place models in a multi-agent setting where they receive incorrect answers from other agents whose social identities (A...
  </details>

- **2026-09-27** — Seungyeon Kim, Junhoo Lee, Minkyu Kim et al. — [Recursive Harness Distillation across Agents for Robot Manipulation](http://arxiv.org/abs/2609.33378v1)
  <details><summary>📄 Abstract</summary>
  A central goal in robotics is to enable manipulation across changing tasks and environments. Vision-language-action (VLA) models provide broad manipulation capabilities but can struggle when execution requires diagnosing failures and adapting behavior. Strong agents can discover effective interventions through interaction with these policies. We propose Recursive Harness Distillation to accumulate this experience as reusable guidance across agents. A strong agent distills its experience into a p...
  </details>

- **2026-09-27** — Yongsheng Zhao, Han Gao, Baoping Cheng et al. — [TAO-DA: Towards Autonomous Operation--A Dual-Arm Vision-Language-Action Model for Coordinated Manipulation](http://arxiv.org/abs/2609.33197v1)
  <details><summary>📄 Abstract</summary>
  Vision-Language-Action (VLA) models provide a unified framework for grounding high-level semantic information into low-level robot actions, enabling scalable robotic manipulation across diverse tasks. However, existing VLA models lack explicit mechanisms to disentangle the states and intents of the two arms, leading to unintended cross-arm interference that degrades task execution success. To address this issue, we propose a symmetric Dual-Arm Expert (DAE) architecture built upon a shared Vision...
  </details>

- **2026-09-27** — Zhizhen Zhang, Yuxia Fu, Zijian Wang et al. — [Train Together or Merge Later? Unifying VLA Experts via a Shared Action Interface](http://arxiv.org/abs/2609.33125v1)
  <details><summary>📄 Abstract</summary>
  Co-training offers a straightforward way to build a multi-task vision-language-action (VLA) policy, but can fall short of the performance achieved by training each task independently. The challenge is to retain these task-specific gains in a multi-task policy without joint post-training. Combining independently trained experts through model merging is a natural approach, yet strong individual experts do not necessarily yield a strong merged policy. We identify one source of this incompatibility:...
  </details>

- **2026-09-27** — Zihan Guo, Shuzhe Zhang, Muhan Li et al. — [Evolving Dexterous Robots from Scratch](http://arxiv.org/abs/2609.33101v1)
  <details><summary>📄 Abstract</summary>
  Little is known about how to manually design agents capable of dexterous manipulation. Some design principles have been inferred from close examination of how animals manipulate objects, but these structures and behaviors have so far resisted biomimicry and may not be optimal for artificial machines. Here we evolve freeform robots to pick up, hold, rotate, and use diverse objects. Unlike other approaches to optimizing robot hands, we do not presuppose the presence, articulation, or geometry of a...
  </details>

- **2026-09-27** — Samiha Tariq — [The Accommodation Trap: Survival Dependence, Communication, and the Allocation of Invisible Work](http://arxiv.org/abs/2609.33064v1)
  <details><summary>📄 Abstract</summary>
  This paper develops a theory of accommodation traps in workplace hierarchies. Workers with weak outside options face a higher relational cost of appearing unavailable, resistant, or difficult, and so adopt accommodative communication (extra deference, softened boundaries, visible flexibility) to preserve the employment relationship. This short-run strategy is also an informative signal: a friction-minimizing supervisor rationally infers that an accommodating worker is less likely to resist, and ...
  </details>

- **2026-09-27** — Masahiro Ogawa, Qi An, Atsushi Yamashita — [3D Point Tracking with State Space Models](http://arxiv.org/abs/2609.34035v1)
  <details><summary>📄 Abstract</summary>
  Tracking any point of a dynamic scene in metric 3D - in absolute meters, not up to an unknown scale - underpins 3D and 4D reconstruction, robot navigation, and autonomous driving, where decisions are made in meters, not pixels. Our objective is a 3D point tracker accurate in those absolute terms and operating within a single commodity GPU, pose-free, monocular budget. Our method rests on one observation: once a point's 2D image trajectory is fixed, the quantity that governs its metric accuracy i...
  </details>

- **2026-09-27** — Kaiwen Luo, Ming Gao — [Designing Reliable LLM-as-a-Judge Measurement Systems for Multi-Turn Business Agents](http://arxiv.org/abs/2609.33955v1)
  <details><summary>📄 Abstract</summary>
  Many LLM-as-a-judge evaluations score fixed outputs under a fixed task definition. Production multi-turn business agents instead require a maintained measurement system: correctness depends on business-specific facts and procedures, outcomes emerge across turns, and failures must be attributed to either agent capability or missing business knowledge before they are actionable. We present an integrated methodology spanning evaluation specification, modular LLM judges, intent-preserving user simul...
  </details>

- **2026-09-27** — Lenore M. Mullin, Gaetan Hains — [Validating Memory-Optimal Transformer Kernels on Real Hardware: From Formal Derivation to Measured Performance Across Two HPC Clusters](http://arxiv.org/abs/2609.33916v1)
  <details><summary>📄 Abstract</summary>
  We validate memory-optimal cost functions for transformer kernels derived via the Mathematics of Arrays (MoA). Companion Papers I-IV formally derive kernels for attention forward, backward, fused forward+backward, decode, and the complete block (RMSNorm, gated MLP) as a hardware-independent specification (DNF) transformed to a machine-specific realization (ONF) via gamma, with verification to machine precision against PyTorch. This paper checks those predictions against measured performance on t...
  </details>

- **2026-09-27** — Houjun Liu, Pratyusha Sharma — [Training Witnesses: Trusting the Training without Trusting the Trainer](http://arxiv.org/abs/2609.33915v1)
  <details><summary>📄 Abstract</summary>
  Progress in machine learning cannot outpace our ability to verify it. With an explosion in papers today, every scientific claim rests initially on trust in the trainer, leading to uneven evaluation, baselines, and forestalling of reliable progress. Traditionally, the burden of verification falls on the reader, who must reproduce expensive training runs. This strategy is impractical due to an explosion in slop contributions, diversity of methods, and the sheer compute required. We put the burden ...
  </details>

- **2026-09-26** — Vivek Kumar Singh, Preeti Priyam, Gautam Bhowmick — [Planner-as-Router: Joint Plan-Time Model Routing for Cost-Efficient Multi-Agent Workflows](http://arxiv.org/abs/2609.32917v1)
  <details><summary>📄 Abstract</summary>
  Running large language model (LLM) agents in production gets expensive fast. A frontier model (the largest, most capable tier) is accurate but can cost 25 times what a small model costs per token, and the gap compounds once a workflow chains several calls together. Planner-as-Router (PaR) attacks this from a different angle. Instead of leaving model-tier selection to some component downstream, it folds the choice into planning itself. As the planner breaks a query into subtasks, it also assigns ...
  </details>

- **2026-09-26** — Jonas Ngnawé, Yann Pequignot, Sabyasachi Sahoo et al. — [Mind the Spike: Mechanisms and Brittleness of Visual Massive Activations in Large Vision-Language Models](http://arxiv.org/abs/2609.32808v1)
  <details><summary>📄 Abstract</summary>
  Large vision-language models (LVLMs) inherit massive activations from their text-only bases: spikes where a few fixed hidden channels receive values thousands of times above the typical magnitude. The text spike systematically appears in early layers at a fixed initial position, independently of input content. Visual spikes vary across images, but whether their formation follows a consistent pattern across LVLMs and how they respond to image perturbations remain open questions. We find that some...
  </details>

- **2026-09-26** — Hamza Mahmood, Usman Ali, Adeel Akhtar — [Path Invariance of a Quadrotor System under Cyber Attacks with Theoretical Guarantees](http://arxiv.org/abs/2609.32747v1)
  <details><summary>📄 Abstract</summary>
  This paper presents a path-following controller for a quadrotor system to guarantee safe maneuvers, in terms of forward path invariance, in the presence of cyber-physical attacks. We assume that an adversarial agent can control any one of the rotors through a false data injection (FDI) type of attack. A feedback controller is designed using transverse feedback linearization which guarantees that the system follows a class of smooth curves under FDI attacks. Our proposed controller is computation...
  </details>

- **2026-09-26** — Xiaoran Xu, Yujing Wang — [An End-to-End Latent-Rollout Approach for Pushing Few-Step ImageNet-$256$ Generation to FID $1.11$ without Fréchet Losses](http://arxiv.org/abs/2609.32376v1)
  <details><summary>📄 Abstract</summary>
  Iterative generation poses a joint optimization problem across steps, as intermediate predictions shape subsequent computations and ultimately determine the final output distribution. Few-step generators distilled from pretrained diffusion and flow-matching models make such optimization computationally practical end to end. We build on this opportunity with a distill-then-refine approach that uses teacher imitation to establish a strong initialization for a few-step rollout in latent space, then...
  </details>

- **2026-09-26** — Shuchi Chawla, Zhiyi Huang, Pooja Kulkarni et al. — [Single-or-Sample: Online Fair Allocation for Combinatorial Agents](http://arxiv.org/abs/2609.32286v1)
  <details><summary>📄 Abstract</summary>
  We study the problem of fairly allocating $m$ indivisible goods among $n$ agents who arrive online, under the notion of maximin share (MMS) fairness. Fair allocation with online arrivals is notoriously challenging: prior work achieves constant-factor MMS guarantees only when agents' preferences belong to a set of valuation functions known in advance, while no guarantees were known without such prior information.   We develop a new randomized online algorithm for additive and submodular valuation...
  </details>

- **2026-09-26** — Shivam Aarya, Zhang Xi-Jia, Chengyue Huang et al. — [CAPEX: Efficiently Distilling Foundation Model Behavior into Deployable Robot Policies through Experience-Adaptive Reasoning](http://arxiv.org/abs/2609.33007v1)
  <details><summary>📄 Abstract</summary>
  Robot learning has largely relied on human-teleoperated demonstrations to acquire effective learnable behaviors. However, human-operated data collection processes can be unintuitive, difficult to scale, and inherently asynchronous. We explore an alternative: distilling physical behavior from general-purpose multimodal foundation models into deployable robot policies by using the foundation model itself as an autonomous demonstrator. While sufficiently capable models can generate successful zero-...
  </details>

- **2026-09-26** — Ziwen Li, Hanlue Zhang, Zhenyang Ren et al. — [SEES: A Self-Evolving Embodied System via Failure-Guided VLA Policy Adaptation](http://arxiv.org/abs/2609.32698v1)
  <details><summary>📄 Abstract</summary>
  Recent vision-language-action (VLA) policies demonstrate promising generalization across diverse short-horizon tasks. However, they remain unreliable on long-horizon tasks, partly because the large-scale training data is biased toward single-stage manipulation tasks that are cheaper to demonstrate. A single weak atomic skill can cause failures across multiple multi-stage tasks. To address such failures, existing methods often require experts to identify the bottleneck and provide additional demo...
  </details>

- **2026-09-26** — Yunpeng Qing, Yilun Kong, Sixu Lin et al. — [PF-RL: Progress Field Reinforcement Learning via Goal-Conditioned Value Geometry for Vision-Language-Action Models](http://arxiv.org/abs/2609.32634v1)
  <details><summary>📄 Abstract</summary>
  Reinforcement Fine-Tuning~(RFT) has emerged as a promising paradigm for improving Vision-Language-Action~(VLA) policies, yet sparse task-level outcomes provide limited credit for intermediate transitions, especially in long-horizon manipulation. A natural approach is to model intermediate task progress and use it as dense feedback for policy improvement. Despite their architectural differences, existing progress-aware methods commonly formulate task progress as an explicit scalar prediction, pro...
  </details>

- **2026-09-26** — Xutao Mao, Rui Qian, Longxiang Wang et al. — ["You're Right, Let Me Fix It": How LLM Agents Damage Correct Work When Falsely Accused](http://arxiv.org/abs/2609.32616v1)
  <details><summary>📄 Abstract</summary>
  LLM agents increasingly keep working after a task succeeds as they resume after compaction or take over handoffs. Their finished work keeps receiving follow-up input that sometimes falsely accuses it for later failures. We call an agent's acceptance of such a false accusation gaslight sycophancy, and destructive over-correction when acting on it damages previously correct work. We introduce CAVE-Bench, a benchmark of 365 agentic tasks across six domains built around opaque tasks. Every scored ru...
  </details>

- **2026-09-26** — Mengxue Fu, Ethan Xu, Sam Iyer-Singh et al. — [Assisting for Open-Ended Tasks: Goal-Oriented Shared Autonomy as a Particle Filter](http://arxiv.org/abs/2609.32576v1)
  <details><summary>📄 Abstract</summary>
  A common approach for shared autonomy blends human inputs with autonomous assistance based on the human's likely goal. However, most existing approaches assume that a static set of possible goals is known a priori, which limits the use of such methods in unstructured assistive settings. We instead investigate how to enable shared autonomy with open-ended and dynamically changing goals. We formulate goal-oriented shared autonomy as a particle filter in which particles represent candidate human go...
  </details>

- **2026-09-26** — Yanjie Zhang, Nanchen Hu, Yushi Sun — [Do Audio LLMs Listen Before They Act? Diagnosing Acoustic-Context Gating in Voice Agents](http://arxiv.org/abs/2609.32536v1)
  <details><summary>📄 Abstract</summary>
  Audio language models can recognize spoken commands and invoke tools, but an agent must first decide whether the acoustic and conversational context warrants action. We introduce VGBench, a 1,018-item diagnostic benchmark for action-level addressedness across side-talk, self-talk, and speaker-switch scenarios. Each item uses a shared action space comprising silence, a tool call, and a natural-language answer. Speaker-switch pairs hold the specified words fixed while source, distance rendering, a...
  </details>

- **2026-09-26** — Huimin Chen, Quan Long, Yanhao Wang — [REFINE: A Resilient Evolution Framework for Intelligent Enterprise Alert Triage in Security Operations Centers](http://arxiv.org/abs/2609.32516v1)
  <details><summary>📄 Abstract</summary>
  Security Operations Centers (SOCs) process large volumes of alerts daily. Alert triage prioritizes high-risk threats while reducing manual review of benign alerts. LLM agents can reason over logs and threat intelligence, but struggle to keep aligned with organization-specific, rapidly evolving SOC operational standards.   We introduce REFINE, an LLM-agent framework for enterprise alert triage. REFINE encodes analyst expertise as structured skills and continuously adapts using analyst disposition...
  </details>

- **2026-09-26** — Minghao Li, Rui Tan, Ruihang Wang — [Beyond Scripted Search: Sample-Efficient Reward Discovery via Agentic Black-box Optimization](http://arxiv.org/abs/2609.32394v1)
  <details><summary>📄 Abstract</summary>
  Designing dense reward functions for low-level reinforcement learning (RL) control remains difficult. Recent work uses large language models (LLMs) to iteratively generate and refine reward functions using policy-training feedback within scripted search algorithms. However, evaluating each candidate requires a full RL training run, making sample efficiency a central challenge for reward search on complex control tasks. To address this limitation, we propose an Agentic Reward Black-box Optimizati...
  </details>


## 📊 统计 / Statistics

| 分类 / Category | 论文数 / Count |
|------|--------|
| jailbreak | 643 |
| prompt-injection | 571 |
| memory-poisoning | 52 |
| tool-use-attack | 142 |
| backdoor | 478 |
| adversarial-attack | 607 |
| privacy-leakage | 4208 |
| steganography | 72 |
| misuse | 1078 |
| red-teaming | 129 |
| vulnerability | 3302 |
| defense | 3123 |
| alignment | 2896 |
| robustness | 3103 |
| watermark | 492 |
| unlearning | 101 |
| agent-safety | 56 |
| benchmark | 66 |
| survey | 364 |
| other | 8381 |

---

📚 **全部 29864 篇论文**（2022 至今）请访问 [GitHub Pages](https://ny1024.github.io/AgentSafety-Papers/) 查看完整列表、搜索与筛选。

*Generated by AgentGuard at 2026-09-29 04:39:12*