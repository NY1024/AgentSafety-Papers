<div align="center">

# AgentGuard 🛡️

**Daily Tracking of LLM Agent Security Papers on arXiv**

[![Auto Update](https://github.com/NY1024/AgentSafety-Papers/actions/workflows/daily-update.yml/badge.svg)](https://github.com/NY1024/AgentSafety-Papers/actions/workflows/daily-update.yml)
[![Papers](https://img.shields.io/badge/Papers-36736-blue)](#)
[![License](https://img.shields.io/badge/License-MIT-green)](#)

</div>

---

## 📖 简介 / Introduction

自动追踪 arXiv 上大模型 Agent 安全方向的最新论文，每日更新，关键词智能分类。

*Automatically tracking the latest LLM Agent security papers on arXiv, updated daily with keyword-based classification.*

**最近更新 / Last Updated**: 2026-11-12 23:06 ｜ **论文总数 / Total Papers**: 36736（近 30 天 / Recent 30 days: 4331）

🌐 **[GitHub Pages](https://ny1024.github.io/AgentSafety-Papers/)** — 查看全部 36736 篇论文（含摘要、分类筛选、搜索）/ View all 36736 papers with abstracts, filters & search

## 📑 分类导航 / Category Navigation

- **[jailbreak](#-jailbreak)** — 越狱攻击 / Jailbreak Attacks — 718
- **[prompt-injection](#-prompt-injection)** — 提示注入攻击 / Prompt Injection Attacks — 677
- **[memory-poisoning](#-memory-poisoning)** — 记忆投毒与篡改 / Memory Poisoning & Tampering — 59
- **[tool-use-attack](#-tool-use-attack)** — 工具使用攻击 / Tool-Use Attacks — 174
- **[backdoor](#-backdoor)** — 后门与投毒攻击 / Backdoor & Poisoning Attacks — 556
- **[adversarial-attack](#-adversarial-attack)** — 对抗攻击 / Adversarial Attacks — 667
- **[privacy-leakage](#-privacy-leakage)** — 隐私泄露 / Privacy Leakage — 4572
- **[steganography](#-steganography)** — 隐写与隐蔽通信 / Steganography & Covert Communication — 90
- **[misuse](#-misuse)** — 滥用与误用 / Misuse & Abuse — 1307
- **[red-teaming](#-red-teaming)** — 红队测试 / Red Teaming — 150
- **[vulnerability](#-vulnerability)** — 漏洞与攻击面 / Vulnerabilities & Attack Surfaces — 3973
- **[defense](#-defense)** — 防御与防护方法 / Defense & Protection Methods — 3876
- **[alignment](#-alignment)** — 对齐与安全约束 / Alignment & Safety Constraints — 3627
- **[robustness](#-robustness)** — 鲁棒性与可靠性 / Robustness & Reliability — 3964
- **[watermark](#-watermark)** — 水印与溯源 / Watermarking & Provenance — 740
- **[unlearning](#-unlearning)** — 机器遗忘 / Machine Unlearning — 120
- **[agent-safety](#-agent-safety)** — Agent 安全框架 / Agent Safety Frameworks — 67
- **[benchmark](#-benchmark)** — 安全评测与基准 / Safety Benchmarks & Evaluation — 75
- **[survey](#-survey)** — 综述与系统化 / Surveys & Systematization — 449
- **[other](#-other)** — 其他安全相关 / Other Security-Related — 10875

## 📄 近期论文 / Recent Papers (Last 30 Days)

> 仅展示最近 30 天中最新的 500 篇论文（含日期、作者、摘要）。近 30 天共 4331 篇，完整 36736 篇论文列表请访问 [GitHub Pages](https://ny1024.github.io/AgentSafety-Papers/)

> Showing the latest 500 of 4331 papers from the last 30 days (with date, authors & abstract). For the full list of 36736 papers, visit [GitHub Pages](https://ny1024.github.io/AgentSafety-Papers/)

### 📂 jailbreak
*越狱攻击 / Jailbreak Attacks* — 4 papers

- **2026-11-10** — Haoyi Wu, Yunkai Dang, Wanyu Zhang et al. — [POEM: Output-Relative Block-Sparse Attention for Long-Context Prefilling](http://arxiv.org/abs/2611.13578v1)
  <details><summary>📄 Abstract</summary>
  Large language models (LLMs) have shown strong capabilities across diverse applications, making both safety and utility essential for reliable deployment. Jailbreak attacks use diverse forms of adversarial prompting to bypass alignment safeguards and induce LLMs to generate harmful responses. Some representation-based defenses regulate internal activations using predefined steering directions or learned safety regions. However, adapting intervention to each input without a predefined representat...
  </details>

- **2026-11-10** — Yunkai Dang, Wanyu Zhang, Meiyi Zhu et al. — [TERM: Target-Free Jailbreak Defense via Entropy-Guided Residual Modulation](http://arxiv.org/abs/2611.13577v1)
  <details><summary>📄 Abstract</summary>
  Large language models (LLMs) have shown strong capabilities across diverse applications, making both safety and utility essential for reliable deployment. Jailbreak attacks use diverse forms of adversarial prompting to bypass alignment safeguards and induce LLMs to generate harmful responses. Some representation-based defenses regulate internal activations using predefined steering directions or learned safety regions. However, adapting intervention to each input without a predefined representat...
  </details>

- **2026-11-08** — Mohammad Tehabsim, Basil Al-Housani, Nour Alhussien et al. — [Beyond AUROC: Deployment-Aware Evaluation of Model-Internal Jailbreak Detectors](http://arxiv.org/abs/2611.11067v1)
  <details><summary>📄 Abstract</summary>
  Large language models (LLMs) are increasingly deployed in user-facing systems, where jailbreak attacks can bypass safety controls and induce harmful and policy-violating outputs. Recent model-internal detectors use hidden representations, gradients, or internal signals to identify such prompts, but their practical security value depends critically on behavior at low false-positive operating points rather than on area under the receiver operating characteristic curve (AUROC) alone.   We study two...
  </details>

- **2026-11-06** — Tianze Chang, Junjie Chu, Yixin Wu et al. — [GuardrailAgent: An Agentic Framework for Jailbreak Defense](http://arxiv.org/abs/2611.09734v1)
  <details><summary>📄 Abstract</summary>
  Despite undergoing safety training to align with human values, large language models (LLMs) remain vulnerable to jailbreak attacks that circumvent built-in safeguards and elicit malicious behaviors given by the adversary. Existing defenses are mostly static and fail to adapt to new or unknown attack strategies, providing limited resilience. To address these, we propose a multi-agent defense framework, GuardrailAgent, that offers adaptive, end-to-end protection. The system autonomously gathers an...
  </details>


### 📂 prompt-injection
*提示注入攻击 / Prompt Injection Attacks* — 10 papers

- **2026-11-09** — Julien Delaunay — [Can the Confidence and Decisions of System 1 Models Be Trusted? An Explainability and Perturbation Audit of Jev-Style Decision Models](http://arxiv.org/abs/2611.12521v1)
  <details><summary>📄 Abstract</summary>
  "System 1" decision models (pioneered by TypeSafe AI's Jev) replace autoregressive text generation with a single forward pass returning typed probability distributions over declared schemas (Choice, Score, Noul). While deployed for low-latency routing and automated triage, their statistical calibration and post-hoc explainability remain uncharacterized. We introduce an open, deterministic audit benchmark evaluating System 1 decision models across calibration under label-preserving perturbations,...
  </details>

- **2026-11-09** — Dario Pasquini,  Reworr, Giuseppe Ateniese et al. — [Say Shibboleth: Fingerprinting the LLMs and Harnesses Behind Agentic Attacks](http://arxiv.org/abs/2611.12386v1)
  <details><summary>📄 Abstract</summary>
  We study the fingerprinting of agentic cyberattacks. Our objective is to reliably infer information about the attacker's configuration, such as LLM version and harness, from telemetry. To achieve this, we introduce a technique we call shibboleth traps: modular honeypot services designed to elicit discriminative behaviors from agentic attackers. The traps make informative interactions a condition for obtaining resources the agent seeks, eliciting model declarations and characteristic writing with...
  </details>

- **2026-11-09** — Xinyi Wu, Jiagui Chen, JiaYi Dong et al. — [Harness Matters: Measuring and Dissecting Security Resilience in Web Agents](http://arxiv.org/abs/2611.11971v1)
  <details><summary>📄 Abstract</summary>
  Web agents extend LLMs from text generation to real-world web interaction by relying on execution harnesses that interpret user goals, perceive webpages, plan actions, and ground model decisions into browser operations. While prior work has recognized that agent security depends on more than the backend model alone, how harness design quantitatively shapes web-agent security remains insufficiently measured.   To systematically study web-agent harness security, we first characterize web-agent har...
  </details>

- **2026-11-09** — Alexey Kurakin, Vishal Karande, Alex Bie et al. — [Scaling Adaptive Prompt Injection Attacks with Agent Swarms](http://arxiv.org/abs/2611.11861v1)
  <details><summary>📄 Abstract</summary>
  Prompt injections have emerged as one of the top security risks faced by AI agents today. Early work in prompt injection attacks looked at simple tool-call agents and static attack payloads, and were saturated since mid-2025. As of Fall 2026, human red-teaming may be nearing saturation, especially on the Gemini family of models. In this work, we argue that despite this apparent plateau, prompt injection attacks are still possible and continued effort into prompt injection defense is needed.   We...
  </details>

- **2026-11-08** — Mustafa S. Aljumaily, Nawar S. Alseelawi, Raghad Alshabandar — [Treating the Model as an Untrusted Component: Deterministic Policy Enforcement, Human Approval and Taint Tracking Against Prompt Injection in Tool-Using Agents, with Validation on Open-Weights Models](http://arxiv.org/abs/2611.11571v1)
  <details><summary>📄 Abstract</summary>
  Tool-using LLM agents act on instructions embedded in the data they read, so prompt injection is a structural rather than a prompt-wording problem. We compare in-prompt defences (hardened prompts, spotlighting, LLM detectors) with deterministic enforcement outside the model (four reference monitors of increasing strength), human approval and taint tracking, judged by one effect-based oracle independent of every defence in an executable environment of 13 tasks and 12 tools, with argument-fuzzing ...
  </details>

- **2026-11-08** — Brijesh Dongol — [On the Relative Security of Prompt Injection: Mechanised Definitions, Defences and Verdicts for LLM Agents](http://arxiv.org/abs/2611.11506v1)
  <details><summary>📄 Abstract</summary>
  An LLM agent that reads untrusted content, such as an email or a web page, may follow instructions hidden in it. Noninterference is too strong for such agents, since a useful agent lets untrusted content influence what it does and may disclose the user's data by design, and declassification needs a release policy written for each task. We instead state security relative to a reference agent, which runs the same plan under the same runtime monitor with a model that never obeys untrusted content. ...
  </details>

- **2026-11-08** — Yiming Sun, Mi Zhang — [When Coding Agents Get Arms: Safety Risks Across the Digital-Physical Boundary](http://arxiv.org/abs/2611.11438v1)
  <details><summary>📄 Abstract</summary>
  Advances in spatial understanding have enabled frontier models to power coding agents that control a real robot arm zero-shot and end-to-end, without task-specific demonstrations or retraining. This brings two new safety challenges. First, the extensive knowledge of frontier models lets these agents perform tasks that earlier VLA and WAM paradigms could not, opening the door to new forms of capability misuse. Second, coding agents can access digital resources such as web pages and emails. Threat...
  </details>

- **2026-11-08** — Doron Shavit — [Least-Privilege Auditing of Agent Tool Calls with Intent Graphs and Reasoning-Guided Escalation](http://arxiv.org/abs/2611.11305v1)
  <details><summary>📄 Abstract</summary>
  LLM agents that call tools are exposed to indirect prompt injection: instructions hidden in tool outputs can steer an agent into calls the user never asked for. We present a runtime audit that derives an executable intent graph from the user's objective and the deployment's tool catalog with one LLM call per task, and checks every tool call against it with a deterministic loop that makes no LLM call (median 5.7 microseconds per call). Two further mechanisms recover utility. Lookups of the user's...
  </details>

- **2026-11-08** — Riya Bharathwaj, Akshara Prabhakar, Roshan Ram et al. — [ErosionBench: Probing Alignment Decay in Enterprise Multi-Agent Systems](http://arxiv.org/abs/2611.11266v1)
  <details><summary>📄 Abstract</summary>
  As enterprises delegate consequential work to multi-agent LLM systems, benign-looking requests can escalate into unsafe actions as they propagate across sessions through poisoned shared state, long-context documents, and trusted peer messages: no single message is malicious, yet the assembled tool action is. Prior benchmarks isolate a single agent under prompt injection or score multi-agent attacks by their final output, leaving cross-session erosion of shared state out of scope. We introduce Er...
  </details>

- **2026-11-07** — Thanh M. Truong-Le, Amber Bennoui, Hoang-Ly Nguyen et al. — [Agents of Chaos: A Systematization of Knowledge (SoK) on Malicious Attacks on Agentic AI Systems](http://arxiv.org/abs/2611.10843v1)
  <details><summary>📄 Abstract</summary>
  Agentic AI systems extend large language models with tools, memory, retrieval, browser or computer-use interfaces, code execution, external services, and multi-agent coordination. Although these capabilities enable agents to act beyond text generation and perform tasks, they also create attack paths through which adversaries can exploit untrusted content, deceptive metadata, poisoned state, compromised skills, mutable dependencies, or malicious code. Such attacks can manipulate planning and tool...
  </details>


### 📂 memory-poisoning
*记忆投毒与篡改 / Memory Poisoning & Tampering* — 2 papers

- **2026-11-10** — Vicenç Torra, Maria Bras-Amorós — [On Private Knowledge Retrieval and Private Inference for secure multi-agent systems](http://arxiv.org/abs/2611.13696v1)
  <details><summary>📄 Abstract</summary>
  Multi-agent systems provide a convenient framework for the massive deployment of agents based on Large Language Models (LLMs). It provides a sound framework where agents can interact with existing software to perform actions in an autonomous way. Agentic AI is the new term to denote these AI-based autonomous systems.   In real multi-agent systems, agents need to deal with malicious agents some of which can exploit security vulnerabilities to do harm. A memory poisoning attack is an example of ex...
  </details>

- **2026-11-06** — David H. Yang, Blake Bullwinkel, Amanda Minnich et al. — [MemoryDojo: Benchmarking Poisoning Through LLM Agent Memory](http://arxiv.org/abs/2611.09721v1)
  <details><summary>📄 Abstract</summary>
  LLM agents benefit from using memory systems to improve performance on long-horizon, multi-session tasks. However, memory introduces a critical attack surface. Malicious instructions encountered in one session may be stored and propagated through memory before being retrieved and acted upon in later sessions. Because memory systems differ in how they process and retrieve information, the downstream effects of poisoning can vary significantly across systems. To quantify the effects of poisoning a...
  </details>


### 📂 tool-use-attack
*工具使用攻击 / Tool-Use Attacks* — 2 papers

- **2026-11-08** — Enhao Huang, Chunshu Xia, Yiming Li et al. — [SkillCODER: Towards Auditing and Attribution of Copyright Infringement in LLM Agent Skills](http://arxiv.org/abs/2611.11308v1)
  <details><summary>📄 Abstract</summary>
  Agent skills package reusable workflows and task-specific procedures into deployable natural-language artifacts for LLM agents. Their scale and readability make them valuable but vulnerable to unauthorized redistribution and repackaging. Existing prompt copyright auditing methods struggle with long skills and introduce token-level perturbations that compromise readability. We propose SkillCODER for copyright auditing and buyer attribution in a black-box, content-only setting. During embedding, S...
  </details>

- **2026-11-07** — Thanh M. Truong-Le, Amber Bennoui, Hoang-Ly Nguyen et al. — [The Devil Wears Markdown: Detecting Malicious Intent Hidden in AI Agent Skill Instructions through Hybrid Static, Dynamic, and Agentic Analysis](http://arxiv.org/abs/2611.10830v1)
  <details><summary>📄 Abstract</summary>
  Agentic AI ecosystems increasingly rely on reusable agent skills that combine executable code, natural-language instructions, configuration artifacts, and external tool integrations. These hybrid artifacts create software supply-chain risks because malicious intent may be distributed across instructions, code, metadata, and runtime behavior, making isolated alerts difficult to interpret.   We evaluate three open-source scanners on a held-out test set of 140 skills comprising 80 malicious and 60 ...
  </details>


### 📂 backdoor
*后门与投毒攻击 / Backdoor & Poisoning Attacks* — 6 papers

- **2026-11-10** — Yuhong Wang, Yujun Cai, Lei Feng et al. — [GARD: Gradient-Guided Adversarial Representation Defense against Backdoors in Multimodal Contrastive Learning Models](http://arxiv.org/abs/2611.14143v1)
  <details><summary>📄 Abstract</summary>
  Multimodal contrastive learning models such as CLIP are vulnerable to backdoor attacks with diverse trigger structures, ranging from localized patches to globally distributed perturbations, with recent attacks increasingly optimizing these triggers in the representation space. Existing post-hoc defenses based on clean fine-tuning may leave backdoors active, while trigger-inversion methods depend on accurately estimating the attack target and trigger. We observe that backdoored encoders exhibit s...
  </details>

- **2026-11-09** — Junsheng Fu, Shuangshuang Gao — [Suppression Is Not Erasure: Mechanistic Analysis and Reactivation Boundaries of Subspace Projection for LoRA Backdoor Defense](http://arxiv.org/abs/2611.12807v1)
  <details><summary>📄 Abstract</summary>
  Low-Rank Adaptation (LoRA) is the standard paradigm for customizing large language models, yet third-party LoRA adapters pose a supply-chain risk: modifying less than 1% of model parameters suffices to implant stealthy backdoors. Recent defenses project adapter weights onto estimated backdoor subspaces, reporting near-zero static Attack Success Rates (ASR). We audit subspace-projection defenses across four model scales (Qwen2.5-0.5B/1.5B/3B/7B) and three architectures (Qwen2.5, InternLM2.5, Spar...
  </details>

- **2026-11-09** — Jingfen Qiao, Rui Li, Shuaiqun Pan et al. — [StealthyPoison: Manipulating LLM Agent Behavior through Procedural Poisoning of Third-Party Skills](http://arxiv.org/abs/2611.12155v1)
  <details><summary>📄 Abstract</summary>
  LLM agents increasingly retrieve third-party skills from public registries and follow their procedures to complete user tasks. This reliance allows attackers to manipulate agent behavior by poisoning the skills. However, overtly malicious instructions can provide explicit signals for detection. We present StealthyPoison, a stealthy procedural poisoning attack that corrupts a skill's decision-critical rules to induce incorrect task outcomes while preserving its advertised functionality and normal...
  </details>

- **2026-11-08** — Bibek Bhandari, Kshitij Lingthep — [Do Benign-Trained Hidden-State Probes Detect Tool Errors Under Adversarial Conditions?](http://arxiv.org/abs/2611.11172v1)
  <details><summary>📄 Abstract</summary>
  Although hidden-state probes efficiently monitor model operation, it remains unclear whether probes trained on benign tool use remain useful for detecting incorrect actions under adversarial conditions. In this research, we assess this problem from the perspective of operational tool-action correct- ness. we use four AgentDojo suites, four conditions, and three models: Qwen2.5-7B-Instruct, Qwen2.5-14B-Instruct, and GLM- 4.6V-Flash (9B). We perform a five-fold, task-grouped out-of-fold (OOF) eval...
  </details>

- **2026-11-07** — Ufaq Khan, Umair Nawaz, Satyajit Tourani et al. — [BAPLe++: Cross-Model Transferability and Prompt-Level Defense of Backdoors in Medical Foundation Models](http://arxiv.org/abs/2611.10764v1)
  <details><summary>📄 Abstract</summary>
  Medical foundation models (Med-FMs) are increasingly adapted to clinical tasks through prompt learning, which tunes a small set of prompt tokens while the backbone remains frozen. Recent work has shown that this efficiency introduces a vulnerability: jointly optimizing learnable prompts and an imperceptible noise trigger during few-shot adaptation implants a backdoor that leaves clean performance intact but steers triggered inputs to an attacker-chosen class. Since prompts are compact and readil...
  </details>

- **2026-11-06** — Louise Nayeong Koh, Yaechan Lee, Myeongjong Lee et al. — [When Feedback Becomes a Backdoor: Tracing Backdoor Skill Formation in Text-Space Skill Optimization](http://arxiv.org/abs/2611.09348v1)
  <details><summary>📄 Abstract</summary>
  Reference answers are a supervision channel in text-space Skill optimization, which produces reusable text artifacts called Skills that guide future agent behavior. Poisoning those answers can induce a persistent trigger-conditioned rule without giving the attacker access to the model, optimizer, or Skill file. We study this reference-feedback poisoning in SkillOpt by tracing an attacker-supplied trigger--payload mapping from reflection to held-out activation. In SearchQA, where the payload repl...
  </details>


### 📂 adversarial-attack
*对抗攻击 / Adversarial Attacks* — 3 papers

- **2026-11-10** — Sedjro Salomon Hotegni, Konstantin Sonntag, Paul-Christian Bürkner et al. — [Lipschitz-Controlled Flow Matching for Robust Image Restoration](http://arxiv.org/abs/2611.13995v1)
  <details><summary>📄 Abstract</summary>
  Flow-matching models can produce high-quality image restorations, but their learned dynamics may amplify small input perturbations and make reconstructions unstable. We introduce LipsFlower to reduce this amplification. We derive stability bounds for Flow-from-$Y$, which initializes the ordinary differential equation from a noise-perturbed observation, as well as for observation-conditioned posterior sampling, which conditions the velocity field on the observation throughout integration. Based o...
  </details>

- **2026-11-09** — Melih Coşğun, Mehmet Emre Gürsoy, Alptekin Küpçü et al. — [SNAPRAG: Cost-Efficient Knowledge Extraction Attack on RAG Systems via Adversarial Perturbations](http://arxiv.org/abs/2611.12241v1)
  <details><summary>📄 Abstract</summary>
  Retrieval-Augmented Generation (RAG) systems improve Large Language Model (LLM) responses by incorporating information from external knowledge bases. However, recent studies have shown that attackers can extract substantial portions of private knowledge bases from RAG systems through repeated querying. Yet, state-of-the-art extraction attacks either rely heavily on external LLMs to generate adversarial queries or require a large number of queries. In this paper, we propose SNAPRAG, a novel and c...
  </details>

- **2026-11-08** — Yibo Miao, Yichuan Cao, Xiao-Shan Gao et al. — [Chatter Attack: Resource Consumption Attack for Large Language Models](http://arxiv.org/abs/2611.11261v1)
  <details><summary>📄 Abstract</summary>
  LLMs are powerful but incur substantial inference cost, which can be exploited by malicious users to induce overly long outputs, increasing latency and operational expense. Prior resource consumption attacks either coerce repetition or suppress the end-of-sequence token by lowering its logit value. However, with autoregressive, sampling-based generation, the search space grows exponentially with length and small deviations or unstable trajectories can derail optimization, limiting attack effecti...
  </details>


### 📂 privacy-leakage
*隐私泄露 / Privacy Leakage* — 17 papers

- **2026-11-10** — Xingqi Wang, Xiaoyuan Yi, Xing Xie et al. — [Specify Privacy Yourself: Assessing Inference-Time Personalized Privacy Preservation Ability of Large Vision-Language Models](http://arxiv.org/abs/2611.13997v1)
  <details><summary>📄 Abstract</summary>
  Large Vision-Language Models (LVLMs) have demonstrated remarkable capabilities but raise significant privacy concerns due to their abilities to infer sensitive personal information from images with high precision. While current LVLMs are relatively well aligned to protect universal privacy, e.g., credit card data, we argue that privacy is inherently personalized and context-dependent. This work pivots towards a novel task: can LVLMs achieve Inference-Time Personalized Privacy Protection (ITP$^3$...
  </details>

- **2026-11-10** — Linru Zhang, Xiangning Wang, Jun Jie Sim et al. — [MOAI: Module-Optimizing Architecture for non-interactive secure transformer Inference](http://arxiv.org/abs/2611.13641v1)
  <details><summary>📄 Abstract</summary>
  Privacy concerns have been raised in Large Language Models (LLM) inference when models are deployed in Cloud Service Providers (CSP). Homomorphic encryption (HE) offers a promising solution by enabling secure inference directly over encrypted inputs. However, the high computational overhead of HE remains a major bottleneck. To address this challenge, we propose MOAI, an efficient HE-based, non-interactive framework for secure transformer inference. MOAI gains significant efficiency improvement f...
  </details>

- **2026-11-10** — Runjia Li, Minghao Chen, Junyu Xie et al. — [OnlyAct: Extracting Action Representations from Foundation Models for World Models](http://arxiv.org/abs/2611.14420v1)
  <details><summary>📄 Abstract</summary>
  Video world models promise general-purpose interactive simulators, but their training is limited by action supervision: action labels are scarce, fragmented across incompatible specifications, and do not scale with the unlabeled video pretraining corpus. A common workaround jointly trains an action encoder to compress consecutive frames into a latent action and a decoder to reconstruct the next frame from the previous frame and that latent, forcing the latent to capture only new information. Thi...
  </details>

- **2026-11-10** — Xintao Xia, Jia Gu — [Differentially Private Statistical Inference for Rankings from Pairwise Comparisons](http://arxiv.org/abs/2611.13485v1)
  <details><summary>📄 Abstract</summary>
  Reliable inference for rankings of large language models based on human pairwise comparisons must preserve the privacy of individual preference records. To meet this need, we develop methods for score and rank inference under the Bradley-Terry model with edge differential privacy. For an objective-perturbed estimator, a new leave-one-out analysis establishes finite-sample bounds on Euclidean and entrywise estimation errors. For sufficiently dense comparison graphs, the error bounds extend to sma...
  </details>

- **2026-11-09** — Hao Zhao, Minghao Lin — [DEPUTYBENCH: Evaluating Contextual Safety in Enterprise Agents](http://arxiv.org/abs/2611.13355v1)
  <details><summary>📄 Abstract</summary>
  Enterprise agents must determine whether ordinary requests are permitted by organizational records and policies while continuing legitimate work. We introduce DEPUTYBENCH, an executable benchmark with 79 base items, 375 instances, paired permission contexts, and graded evidence requirements. Across 12 models, revised audits give 88.0% pooled safety and 79.1% paired success. A controlled study of 28 derived tasks and six models tests authorization-fact flips, evidence masking, and irrelevant rewr...
  </details>

- **2026-11-09** — Masanori Hanada, Jiwoo Seo, Seok-Kyun Son et al. — [Quantum simulation of real-time bosonic dynamics with binary and unary position encodings on superconducting and trapped-ion processors](http://arxiv.org/abs/2611.13079v1)
  <details><summary>📄 Abstract</summary>
  Simulating a bosonic degree of freedom on qubit hardware requires discretizing its position space, and the qubit encoding of the resulting lattice determines the circuits that realize its real-time dynamics. We compare binary and unary encodings of a position lattice on superconducting (IBM) and trapped-ion (IonQ) processors. Binary encoding applies the kinetic term through the quantum Fourier transform; unary encoding uses one qubit per site, single-qubit rotations for the potential and excitat...
  </details>

- **2026-11-09** — Tong Guan, Yunchun Li, Minyuan Xiao et al. — [When Handshakes Go Dark: An Adaptive Semantic-Sequential Fusion Framework for Encrypted Traffic Classification](http://arxiv.org/abs/2611.12442v1)
  <details><summary>📄 Abstract</summary>
  Encrypted traffic classification is essential for network security monitoring and traffic management. Self-supervised pre-training can learn reusable representations from large-scale unlabeled traffic, but TLS 1.3, QUIC, and privacy mechanisms such as Encrypted Client Hello (ECH) increasingly conceal application, handshake, and service-identifying information. Observable upper-layer bytes are therefore dominated by ciphertext, weakening the link between raw-byte patterns and application semantic...
  </details>

- **2026-11-09** — Valentin Burkin — [A local language model layered with rule-based and neural detectors for clinical text de-identification: an open-source toolkit and evaluation](http://arxiv.org/abs/2611.12709v1)
  <details><summary>📄 Abstract</summary>
  Objectives: To measure whether a locally hosted large language model (LLM), stacked with deterministic and clinical named-entity recognition (NER) detectors, finds more protected health information (PHI) than open tools, and at what precision.   Materials and Methods: DeidSharp, an open-source .NET toolkit, combines the findings of pluggable detectors (patterns, a clinical NER model, a local 26B mixture-of-experts LLM) and fails closed on any detector error. Configurations fixed on tuning halves...
  </details>

- **2026-11-09** — Sung Il Choi, Junhao Cai, Dohun Kim et al. — [Spectral Unlearning: Transformer Structure-Preserving Updates for Language Models](http://arxiv.org/abs/2611.11902v1)
  <details><summary>📄 Abstract</summary>
  Machine unlearning in large language models (LLMs) aims to remove specific learned knowledge, capabilities, or behaviors while preserving model utility. Existing methods have mostly focused on the design of unlearning objectives, while largely overlooking the intrinsic matrix structure of transformer weights. In particular, standard optimizers operate on independent scalar coordinates, thereby ignoring this matrix structure. We propose spectral unlearning, an update framework that combines stand...
  </details>

- **2026-11-09** — Wei Zhang, Peijun Ye, Dihu Chen et al. — [MDA framework: multi-architecture domain adaptation for unsupervised person re-identification](http://arxiv.org/abs/2611.11836v1)
  <details><summary>📄 Abstract</summary>
  Unsupervised person re-identification not only faces the challenge of domain gaps, but existing methods also rarely support multiple network architectures. To tackle both issues, this paper proposes a multi-architecture auto-adaptive domain adaptation method: Mamba augmented multi-architecture domain adaptation framework. Specifically, this paper constructs the multi-architecture domain adaptation capability at two levels. At the first level, we propose a composite operator(MDA operator) that en...
  </details>

- **2026-11-08** — Ziyun Cui, Haoyu Niu, Wen Wu et al. — [Task-adaptive anonymisation enables privacy-preserving sharing of clinical speech data](http://arxiv.org/abs/2611.11273v1)
  <details><summary>📄 Abstract</summary>
  Clinical speech is increasingly used for disease screening and clinical assessment, but directly distributing speech recordings poses privacy risks because they contain both speaker-identifying voiceprints and sensitive spoken content. Existing speech anonymisation approaches are primarily developed for general speech applications or task-specific clinical speech and overlook that different clinical tasks rely on distinct speech characteristics, necessitating task-adaptive anonymisation strategi...
  </details>

- **2026-11-08** — Chaymaa Abbas, Kareem Hassani, Mariette Awad — [RADE: Risk-Adjusted Deployment Efficiency, A Framework for Routing, Memory, and Escalation in Safe LLM Systems](http://arxiv.org/abs/2611.11659v1)
  <details><summary>📄 Abstract</summary>
  A deployed language model does not merely answer questions. It spends computation, consumes time, consults evidence, exposes memory, invites or avoids human review, and sometimes makes mistakes whose consequences are radically unequal. Yet LLM systems are still commonly compared as if the relevant object were a single model and the relevant outcome were a single benchmark score. This paper argues that the unit of analysis should instead be the deployment policy: the mechanism that decides when t...
  </details>

- **2026-11-08** — Feriel Fass, Djemel Ziou — [Daily Emergency Call Volume Forecasting using Univariate and Multivariate TimeGPT](http://arxiv.org/abs/2611.11613v1)
  <details><summary>📄 Abstract</summary>
  This study investigates the potential of TimeGPT, a pretrained foundation model for timeseries, for forecasting daily emergency call volumes. Real-world emergency call data, comprising 2,101 daily observations, are used to evaluate both univariate and multivariate forecasting settings under one-step-ahead and seven-day multi-step-ahead scenarios. The multivariate forecasting incorporates temporal, meteorological, demographic, and socioeconomic variables. A chronological training, validation, and...
  </details>

- **2026-11-07** — Xiaobei Yan, Tianwei Zhang — [Mirage: Provable Defense Against LLM KV Cache Timing Side Channels with Topology-Aware Isolation](http://arxiv.org/abs/2611.10756v1)
  <details><summary>📄 Abstract</summary>
  Large Language Models (LLMs) are increasingly deployed as shared multi-tenant services, relying on advanced optimizations like KV cache and prefix sharing to improve throughput and reduce latency. However, these optimizations introduce a critical vulnerability: attackers can exploit time-to-first-token (TTFT) variations between KV cache hits and misses to infer sensitive prompt tokens via prefix-matching side-channel attacks. Existing defenses indiscriminately restrict cross-tenant cache sharing...
  </details>

- **2026-11-07** — Wanlu Sun, Zhenhui Yuan, Xiang Ji et al. — [Where Should Models Run? A Collaborative Inference Framework for Embodied Intelligence in 6G](http://arxiv.org/abs/2611.11023v1)
  <details><summary>📄 Abstract</summary>
  Embodied intelligence systems rely on fast and reliable inference to enable real-time perception, reasoning, and control. Recent advances in large-scale artificial intelligence (AI) models, including Large Language Models (LLMs) and Vision-Language-Action (VLA) models, have significantly enhanced the capabilities of embodied agents in complex environments. However, deploying these models remains challenging due to the limited computational resources and energy budgets of robotic platforms. A fun...
  </details>

- **2026-11-07** — Matthias Lehmann, Madeleine Werthebach — [Generating Diverse and Verified Synthetic Clinical Notes with Labels by Construction](http://arxiv.org/abs/2611.10789v1)
  <details><summary>📄 Abstract</summary>
  Under strict privacy regulations in the clinical domain, de-identification is necessary to enable the use of clinical data such as for natural language processing. However, we currently lack sophisticated ways to tell which de-identification models actually are suitable. Specifically, we need benchmarks that are challenging, diverse, and clinically plausible, all while ensuring label correctness. To this end, we present SPARCLING, an LLM-based pipeline to generate synthetic discharge letters wit...
  </details>

- **2026-11-06** — Chuxue Cao, Jingru Zeng, Boqin Yin et al. — [Authorization Drift in LLM Agents: Evaluating Boundary Compliance in Multi-Step Tool Use](http://arxiv.org/abs/2611.09113v1)
  <details><summary>📄 Abstract</summary>
  LLM agents can exceed their authorization boundaries while pursuing user goals without an adversary. We formalize this phenomenon as authorization drift across data, tool, scope, and time, and introduce the Authorization Drift Benchmark (ADB): 648 samples across seven domains, each pairing a sufficient compliant path with an attractive unauthorized shortcut. To ensure executable tasks, tempting shortcuts, and feasible compliant paths, Staged Execution-Reflective Synthesis (SERS) grounds benchmar...
  </details>


### 📂 misuse
*滥用与误用 / Misuse & Abuse* — 9 papers

- **2026-11-10** — Simon Hegelich, Bardh Prenkaj, Habiba Sarhan et al. — [From Attack Surface to Defense Architecture: Compositional Security for Agentic Coding Harnesses](http://arxiv.org/abs/2611.13960v1)
  <details><summary>📄 Abstract</summary>
  AI coding harnesses couple language models to shells, filesystems, and network sockets, turning the harness into an automated Living-off-the-Land (LotL) platform: once an adversary injects instructions into retrieved content, dual-use binaries such as bash, curl, and find become the payload. We argue that security in agentic systems is a structural property of the cognitive architecture and permission composition rather than an emergent property of individual models. Static regex blacklists miss...
  </details>

- **2026-11-10** — Felix Härer — [Model-Based Authoring of SOC Simulation Exercises for Cybersecurity Education](http://arxiv.org/abs/2611.14227v1)
  <details><summary>📄 Abstract</summary>
  Cybersecurity training and classroom exercises with a virtual Security Operations Center (SOC) combine alerts, evidence, timeline entries, learner tasks, and assessment items that must remain consistent across an evolving incident. This paper presents a model-based authoring method in which a technical and educational specification is used to construct an incident exercise model and a large language model (LLM) generates selected scenario text based on that model. The incident exercise model com...
  </details>

- **2026-11-10** — Runxuan Tang, Haoyu Gao, Yuyan Ding et al. — [When Should Agents Remember? Falsification-Gated Self-Evolution for LLM Agents](http://arxiv.org/abs/2611.14326v1)
  <details><summary>📄 Abstract</summary>
  LLM agents increasingly operate in long-horizon, verifier-rich environments, but current self-improvement mechanisms often write episode-derived lessons directly into memory, making local success an unreliable signal for reusable and safe knowledge. This paper addresses the core question of when an experience-derived behavioral update should be admitted into persistent agent state. We propose Falsification-Gated Self-Evolution (FGSE), a verifier-grounded framework that represents each candidate ...
  </details>

- **2026-11-09** — Donghyun Kim, Jin Hong, Seungmin Kim et al. — [MUTE: Multi-Level Alignment Uncoupling Against Talking-Head Exploitation for Voice Protection](http://arxiv.org/abs/2611.11989v1)
  <details><summary>📄 Abstract</summary>
  Talking-head generation models, which synthesize realistic facial animations from audio, are increasingly vulnerable to misuse in multimodal deepfake scenarios. Protecting such systems remains challenging, as talking-head models fundamentally rely on precise audio-visual alignment, while effective audio protection methods remain largely underexplored. In this work, we propose MUTE, an audio protection framework that uncouples the underlying audio-visual alignment through a multi-level strategy. ...
  </details>

- **2026-11-09** — Sepehr Ilami, Babak Heydari — [Steering Emergent Behavior in Multi-Agent LLM Systems via Information Networks](http://arxiv.org/abs/2611.11714v1)
  <details><summary>📄 Abstract</summary>
  Large language model (LLM) agents increasingly operate in groups, each pursuing an individual objective while jointly determining system performance. If an operator controls which agent observes which other agent, but not their payoffs or messages, how should observations be structured to raise collective welfare? We make the information network (who observes whom) a design object, decoupled from the fixed interaction network over which agents act. Ten identical LLM agents play repeated group-de...
  </details>

- **2026-11-09** — Kevin Wei, Sumaya Nur Adan, Stephan Llerena et al. — [FraudBench: A Legal Evaluation of AI Deception](http://arxiv.org/abs/2611.12167v1)
  <details><summary>📄 Abstract</summary>
  We introduce FraudBench, an evaluation of large language models' (LLMs) propensities to recommend, assist, or directly take actions that would constitute fraud under U.S. law. Our evaluation contains a novel dataset of 159 scenarios based on real-world U.S. court cases and validated by legal experts. We present each scenario to LLMs via three tasks at varying levels of autonomy: advising users, drafting messages for users to send, and acting directly on behalf of users (477 tasks total). In each...
  </details>

- **2026-11-09** — Jui-Chien Tsou, Po-Yi Wu — [Correct First, Fast Second: What a Local 7B Code Model Can and Cannot Do for GPU Kernel Optimization](http://arxiv.org/abs/2611.12079v1)
  <details><summary>📄 Abstract</summary>
  We study how much the interaction strategy around a fixed, locally hosted 7B-parameter code model (Qwen2.5-Coder-7B-Instruct) affects its ability to replace PyTorch operators with custom CUDA kernels. On 30 KernelBench tasks (levels 1-3, first 10 each, evaluated on a V100), we compare four regimes of increasing structure: zero-shot prompting, profiling-guided prompting, iterative refinement on execution feedback, and a multi-agent loop (analysis, retrieval, generation, evaluation, feedback triag...
  </details>

- **2026-11-06** — Jiashu Zhang, Jiaming He, Zheming Zhang et al. — [AUTEUR: Acoustic Plan Learning for Red-Teaming Text-to-Audio Models](http://arxiv.org/abs/2611.09351v1)
  <details><summary>📄 Abstract</summary>
  Automated red-teaming of text-to-audio models requires test prompts that pass textual screening and expose harmful acoustic content. The central challenge is to connect the sounds produced by the target model to both reusable test generation and prompt revision. Our key idea is to represent test descriptions as structured acoustic plans that organize foreground sounds, context, and vocal attributes. To this end, we propose acoustic plan learning, a framework that learns and refines these plans u...
  </details>

- **2026-11-06** — Hongwei Lin, Xun Huang, Chenglu Wen et al. — [Zero-Query Transferable Pretend Benign Attacks with Amortized Online Generation for Cooperative Perception](http://arxiv.org/abs/2611.09256v1)
  <details><summary>📄 Abstract</summary>
  Cooperative perception enables an ego agent to acquire information from collaborators beyond its own sensors' reach. Yet, the most beneficial messages are often the hardest to verify from local observations. Pretend Benign (PB) exploits this asymmetry by targeting regions with weak local verifiability and applying multi-objective perturbations, making harmful feature changes appear to be benign assistance. However, PB is victim-dependent: selecting regions and optimizing perturbations require th...
  </details>


### 📂 red-teaming
*红队测试 / Red Teaming* — 2 papers

- **2026-11-10** — Howard Zhang, Chuck Arvin, Logan Brown et al. — [Comparative Analysis of Agent Evaluation Frameworks: Stability, Detection, and Discovery in Enterprise Analytics Agents](http://arxiv.org/abs/2611.14493v1)
  <details><summary>📄 Abstract</summary>
  Deploying LLM-based analytics agents in enterprise settings requires evaluation frameworks that can reliably detect failures across complex, multi-tool workflows. We present a three-phase comparative study of three evaluation frameworks, each representing a distinct evaluation paradigm (trace-based LLM judging, text-only LLM judging with red-teaming, and deterministic heuristics), applied to two analytics agents in a controlled research setting using frozen execution traces. Phase 1 quantifies e...
  </details>

- **2026-11-06** — Ruoyu Zhou, Shuyao Jiang, Haifeng Ruan et al. — [GreyZone: Production-quality Agentic Application Threats](http://arxiv.org/abs/2611.09161v1)
  <details><summary>📄 Abstract</summary>
  Agents are increasingly deployed across domains such as coding, banking, and commerce. Their ability to invoke tools and change application state makes security testing important for reliable deployment. Although agent security has been studied through various adversarial testing approaches, benchmarks grounded in production agent environments remain limited. We introduce GreyZone, a benchmark for evaluating automated red-teaming services against real-world agent applications. Unlike benchmarks ...
  </details>


### 📂 vulnerability
*漏洞与攻击面 / Vulnerabilities & Attack Surfaces* — 56 papers

- **2026-11-10** — Muhan Gao, Hangxiao Zhu, Xinqi Su et al. — [Re-Search: Dissecting LLM Ideation Through a Two-Player Questioning Game](http://arxiv.org/abs/2611.14487v1)
  <details><summary>📄 Abstract</summary>
  Research ideation is iterative: researchers refine their ideas step by step based on feedback. Yet existing evaluations obscure this search process, making it difficult to understand how LLMs explore the space of research ideas and what limits their progress. We introduce Re-Search, which adapts the format of Twenty Questions to research ideation: given only the research problem of a published paper, a model must rediscover the paper's core idea by asking yes-or-no questions. Built from 200 ICML...
  </details>

- **2026-11-10** — Karol Struniawski — [Breakdown of Autoregressive Multi-Step Reasoning Under Concentrated vs. Diffuse Attention Head Dropout](http://arxiv.org/abs/2611.14209v1)
  <details><summary>📄 Abstract</summary>
  During extended wakefulness, mammalian neocortical networks experience localized periods of transient neuronal silence termed off-states. Here, we examine how analogous spatiotemporally concentrated disruptions affect sequential reasoning in autoregressive Large Language Models (LLMs). Evaluating 250 paired derivations on the GSM8K benchmark across two 8B models (Qwen3-8B and LLaMA-3.1-8B-Instruct), we contrast clustered bursts of attention head masking against budget-matched diffuse i.i.d. drop...
  </details>

- **2026-11-10** — Haozhan Shen, Liangbo He, Jun Lan et al. — [ZoomGain: Mining Global-to-Zoom Perception Gaps for Fine-Grained Visual Supervision](http://arxiv.org/abs/2611.14076v1)
  <details><summary>📄 Abstract</summary>
  Fine-grained visual perception requires Vision-Language Models (VLMs) to locate and interpret subtle evidence within complex scenes. Constructing supervision for this ability is challenging: questions must have correct, unambiguous answers that depend on actual fine-grained visual details rather than coarse cues or language priors. Verifying these properties makes manual annotation labor-intensive and automatic generation difficult for models that themselves struggle with fine-grained perception...
  </details>

- **2026-11-10** — Jonas Limniatis, Bennet Schaarmann, Georg Reuber et al. — [Controlled Knowledge Engineering for Taxonomy Induction with Tool-Grounded LLM Agents and Runtime-Adaptive Policies](http://arxiv.org/abs/2611.13966v1)
  <details><summary>📄 Abstract</summary>
  Taxonomies are structured knowledge representations that support semantic search, recommendation, product catalog organization, and retrieval-augmented generation. Their automated construction from a fixed set of candidate entities requires more than plausible text generation: the resulting hierarchy must be complete, structurally valid, and semantically coherent. Large Language Models (LLMs) are promising for this task, but iterative free-form generation remains vulnerable to omitted or halluci...
  </details>

- **2026-11-10** — Suhas Chandrashekar, Thomas Stieglitz, Prasanth Velvaluri — [Design of Self-Folding Origami Architectures for Biomedical Implants: A Finite Element Simulation Framework](http://arxiv.org/abs/2611.13964v1)
  <details><summary>📄 Abstract</summary>
  Minimally invasive brain implants require compact deployment geometries and controlled shape transformation for delivery through confined vessels. Origami-inspired structures enable large shape changes from compact to tailored deployed configurations, but implementation at microscale dimensions remains challenging, as conventional designs rely on predefined mountain and valley folds that become increasingly difficult to fabricate and assemble as unit-cell size is reduced to meet clinical require...
  </details>

- **2026-11-10** — Weifeng Yuan, Zifan Chen, Yucheng Zhang et al. — [BypassGym: A Benchmark for Evaluating AI Agents' Endpoint Defense Evasion Capabilities](http://arxiv.org/abs/2611.13684v1)
  <details><summary>📄 Abstract</summary>
  Artificial intelligence agents increasingly automate cybersecurity tasks, including offensive operations. Frequent attacks across the web make endpoint detection and response (EDR) a critical defense, but whether AI agents can evade it remains unclear. Benchmarks evaluate the offensive capabilities of large language model (LLM) agents in areas such as penetration testing and vulnerability discovery. One important capability that these benchmarks do not address is defense evasion, specifically wh...
  </details>

- **2026-11-10** — Yue Wu, Xueyu Zhou, Yangrong Hu et al. — [Bootstrapped On-Policy Distillation](http://arxiv.org/abs/2611.13680v1)
  <details><summary>📄 Abstract</summary>
  On-policy distillation (OPD) improves language models by distilling teacher predictions on student-generated trajectories, while on-policy self-distillation (OPSD) removes the need for an external teacher by using a reference-conditioned copy of the model as the teacher. Despite its great early improvements, we find that OPSD does not remain consistently effective under continued training and can eventually suffer substantial performance degradation. We study this training behavior and link the ...
  </details>

- **2026-11-10** — Daniel Barter, Jacob C. Bridgeman, Chris Dawson et al. — [Machine-learning decoders for fusion-based quantum computing in real time](http://arxiv.org/abs/2611.13630v1)
  <details><summary>📄 Abstract</summary>
  Fault-tolerant quantum computation requires decoders that combine accuracy, throughput, low latency, and scalability to large numbers of physical qubits. In photonic fusion-based architectures, erasures from photon loss and probabilistic fusion measurements are a dominant error mechanism, motivating decoders that remain accurate at high erasure rates. We introduce PRISM, a transformer-based machine-learning decoder designed to exploit the known locations of erasures in protocols subject to both ...
  </details>

- **2026-11-10** — Aghoghomena Akasukpe, Li Yang, Xinyao Zhou et al. — [IFRS Compliance Verification: An Open Multi-LLM Benchmark and Content-Conditioned Ensemble Classifier](http://arxiv.org/abs/2611.13595v1)
  <details><summary>📄 Abstract</summary>
  Verifying corporate financial disclosures against the International Financial Reporting Standards (IFRS) is a core auditing task in which experts cross-reference disclosures with hundreds of fine-grained regulatory paragraphs: a laborious, costly, and error-prone process that motivates growing interest in large language models (LLMs) as compliance assistants. Yet single-model accuracy remains insufficient for high-stakes use, and naive ensembling is vulnerable to systematic per-model biases that...
  </details>

- **2026-11-10** — Zhiliang Chen, Sammy Nammari, Jiahao Su et al. — [Exploiting Feature-invariant Scaling Laws for Efficient A/B Experimentation in Recommendation Systems](http://arxiv.org/abs/2611.13539v1)
  <details><summary>📄 Abstract</summary>
  Researchers and engineers improve recommendation systems by performing A/B experiments with new model architectures, optimization methods, and data features. However, running full-scale experiments (e.g., full-model training with online data) for every feature change is prohibitively computationally intensive, while the result from a single small-scale experiment is often misleading. To address this challenge, we show that modern recommendation models exhibit feature-invariant scaling: the chang...
  </details>

- **2026-11-10** — Purva Pruthi, Andrew Yuan, Alexander D'Amour et al. — [Evaluating Compositional Generalization in Transformers: The Role of Composition Equivalence and Module Coverage](http://arxiv.org/abs/2611.13498v1)
  <details><summary>📄 Abstract</summary>
  Compositional generalization is an important form of out-of-distribution generalization, defined as the ability to train on some combinations of modules (e.g., functions such as sort, filter) and then generalize to unseen combinations. Despite substantial empirical work evaluating compositional generalization in transformers, findings have been inconsistent because evaluations were often conducted on a limited set of train-test splits, defined in an ad hoc manner. Through a systematic evaluation...
  </details>

- **2026-11-10** — Mo Zhou, Yiwei Zhang — [Framing-Induced Vulnerability in Large Language Models: Evidence from Chinese News Headlines](http://arxiv.org/abs/2611.13531v1)
  <details><summary>📄 Abstract</summary>
  Large language models increasingly evaluate, route, and moderate news, so a model's judgment of a headline has become a gatekeeping decision. We ask whether that judgment follows the fact being reported or the way the fact is framed. We combine an ecological audit of 63,926 Chinese news headlines with a controlled experiment. The experiment covers 30 real events, 30 synthetic events, and 29 natural headline pairs, tested on four Chinese models. Changing only the headline frame shifted both perce...
  </details>

- **2026-11-09** — Oshando Johnson, Ranjith Krishnamurthy, Rohith Kumar Shanmuganathan et al. — [Code-Grounded Agentic Explanations for Static Analysis Vulnerability Findings](http://arxiv.org/abs/2611.13041v1)
  <details><summary>📄 Abstract</summary>
  Static application security testing (SAST) tools surface vulnerabilities early and their verdicts are rule-based and auditable. Yet developers routinely dismiss findings they cannot interpret. Large language models can supply the missing explanation, but designs that also hand the model the detection give up the auditability that makes static analysis defensible. We keep detection with the analyser and give the model only the explaining. A preliminary user study with 20 participants and a worksh...
  </details>

- **2026-11-09** — Hanxiao Li, Shutong Liu, Yongjia Ma et al. — [Mitigating Agentic Deception via Evaluation-Side Partially Observable Games](http://arxiv.org/abs/2611.12835v1)
  <details><summary>📄 Abstract</summary>
  As large language models become more capable agents, they can exhibit deceptive behaviors, cheating human for higher rewards while appearing helpful. We attribute this failure to evaluation-side partial observability, where models are evaluated mainly from final outcome, without checking the faithfulness of underlying reasoning, tool use, and environmental effects. Prior mitigations address this partial observability by predefined evaluator latent belief space or one-shot monitoring, which do no...
  </details>

- **2026-11-09** — Lukun Wu, Jie Li, Ziqi Ren et al. — [Complementarity-Driven Dual-Teacher Hierarchical Alignment for Zero-Shot EEG-to-Image Retrieval](http://arxiv.org/abs/2611.12798v1)
  <details><summary>📄 Abstract</summary>
  Decoding visual information from EEG is central to brain--computer interfaces and brain-inspired intelligence, and contrastive alignment with pretrained vision foundation models (VFMs) has become the dominant paradigm. However, existing methods align EEG solely with CLIP-family VFMs, leaving hierarchical visual information in neural responses under-exploited. To address this gap, we formulate a mechanism-paradigm correspondence view linking hierarchical visual processing (from appearance to sema...
  </details>

- **2026-11-09** — Yuxuan Hu, Jihao Liu, Weikang Shi et al. — [Large Language Models as a Universal Searcher for Open-World Automated Machine Learning](http://arxiv.org/abs/2611.12791v1)
  <details><summary>📄 Abstract</summary>
  Developing effective machine learning models requires complex manual tuning, while current Automated Machine Learning (AutoML) frameworks remain domain-specific and isolate model architecture, training hyperparameter, and data ratio optimization. Here, we bridge this gap by proposing a universal, large language model (LLM)-based AutoML framework that jointly optimizes these configurations for the first time without the need for task-specific fine-tuning. We propose NCode, a unified numerical enc...
  </details>

- **2026-11-09** — Pengju Chen, Da-Wei Luo, Ting Yu — [Self-Energy Construction for Chain Representations of Open Quantum Systems](http://arxiv.org/abs/2611.12782v1)
  <details><summary>📄 Abstract</summary>
  We identify the self-energy as the environmental response to the system, which transforms covariantly under shifts of the system--environment cut. For a semi-infinite chain with asymptotically uniform parameters, this transformation admits a fixed point that defines the asymptotic boundary self-energy (BSE), whose spectral density is the Wigner semicircle. A chain-extended BSE exploits the trend of the retained chain, offering improved accuracy in representing the environment. The transformation...
  </details>

- **2026-11-09** — Brendan P. Murphy, Agustina Saenz — [Safe Reinforcement Learning for Multi-Turn Clinical Agents: When Dense Rewards Beat Outcome Rewards](http://arxiv.org/abs/2611.12728v1)
  <details><summary>📄 Abstract</summary>
  Reinforcement learning with verifiable rewards is increasingly used to improve language model reasoning, yet its effects on sequential decision procedures remain poorly understood. We study this problem in clinical multi-turn agents that must decide what information to request, when to stop gathering evidence, and which action to take. We introduce three controlled environments: medication refill triage, acute diagnostic work-up, and dosing titration, each with hidden clinical states, query cost...
  </details>

- **2026-11-09** — Walid Elbarz, Mohamed Bourriz, Vincent Simonneaux et al. — [National-Scale Crop Type Mapping in Morocco Using Google AlphaEarth Foundations Embeddings and the Fields of the World Field Boundary Map](http://arxiv.org/abs/2611.12681v1)
  <details><summary>📄 Abstract</summary>
  Recent geospatial foundation models have introduced a new paradigm for large-scale Earth observation by providing pretrained embedding representations that can be directly exploited for downstream tasks. In this work, we investigate the use of Google AlphaEarth Foundations embeddings for national-scale crop type mapping in Morocco. The proposed workflow operates directly on publicly available 64-dimensional pretrained embeddings using lightweight downstream classifiers, eliminating the need to p...
  </details>

- **2026-11-09** — Isaac Xu, Devi Ayyagari, Martin Gillis et al. — [GHiML: VLM-Guided Hierarchical Multi-Label Learning with Applications to Benthic Imagery](http://arxiv.org/abs/2611.12564v1)
  <details><summary>📄 Abstract</summary>
  Vision language models (VLMs) encode substantial expert knowledge within their weights, yet their direct application to specialised classification domains such as benthic imagery remains limited. Meanwhile, vision transformers trained on these tasks rely predominantly on low-level visual latents (colours, textures, and shapes) that lack the higher-level reasoning humans employ for identification. We propose Guided Hierarchical Multi-Label (GHiML) learning, a pipeline that extracts conceptual lat...
  </details>

- **2026-11-09** — Xiangrui Yang, Yunfeng Zhao, Jiawei Yang et al. — [RecoGEM: A Serving System for Production-Scale Generative Recommendation](http://arxiv.org/abs/2611.12296v1)
  <details><summary>📄 Abstract</summary>
  Generative recommendation (GR) is moving industrial recommender systems (RecSys) from scoring candidate items to autoregressively generating item identifiers. This shift promises higher recommendation quality, but makes serving substantially harder: each request executes a short sequence of dependent decoding steps that explore a large item space and select promising candidates on the latency-critical path. GR not only creates structural mismatches with conventional RecSys pipelines, but also ch...
  </details>

- **2026-11-09** — Mohsen Ahmadvand, Piotr Dobaczewski, Camille Bouzerand — [Lessons Not Learned: Why Cross-Chain Bridges Keep Losing Billions the Same Way](http://arxiv.org/abs/2611.12252v1)
  <details><summary>📄 Abstract</summary>
  Bridge hacks have cost billions, often without exploiting a code bug. In the cross-chain bridge hacks we catalogue from 2021 to 2026, failures of security posture, meaning how a bridge's people, code, controls and off-chain infrastructure are set up, account for 88% of reported losses since 2023, and nearly all repeat earlier failures. Code audits cannot catch these failures, so we propose a bridge security assessment rubric. It scores each bridge deployment from on-chain evidence, and a hard ca...
  </details>

- **2026-11-09** — Hong Su — [SCALE: Small-Model-First Concept Abstraction with LLM-Guided Experience Internalization](http://arxiv.org/abs/2611.12120v1)
  <details><summary>📄 Abstract</summary>
  Autonomous agents must continually acquire reusable knowledge from experience without relying on costly large language model (LLM) reasoning for every decision. However, existing experience-based approaches often struggle to transform accumulated observations and reasoning into compact knowledge that lightweight models can independently apply. This paper proposes SCALE, a small-model-first framework that integrates selective LLM reasoning, experience-driven concept abstraction, and knowledge int...
  </details>

- **2026-11-09** — Shoubin Chen, Rui Xu, Zehao Wu et al. — [CSG-Nav: Confidence-Aware Semantic-Geometric Fusion for Robust Exploration and Accurate Zero-Shot Object-Goal Navigation](http://arxiv.org/abs/2611.11978v1)
  <details><summary>📄 Abstract</summary>
  Zero-shot object-goal navigation requires autonomous agents to explore unseen environments and locate target objects without task-specific training, posing challenges in perceptual reliability under observation uncertainty and physically grounded goal termination. Although foundation-model-based approaches improve generalization, they remain vulnerable to unreliable long-range perception, hallucination-induced directional bias, and semantically plausible but geometrically incorrect stopping deci...
  </details>

- **2026-11-09** — Eyhab Al-Masri, Wenjun Yang — [ShadowBench-MCP: Measuring Shadow Invocations in MCP-Style Tool Routing](http://arxiv.org/abs/2611.11720v1)
  <details><summary>📄 Abstract</summary>
  LLM agents increasingly act as routers for tools, APIs, and software-supply-chain workflows, making an execution path - rather than generated text alone - a security-relevant model output. We study shadow invocation: a task-preserving request variant that causes an LLM router to select a riskier execution path, potentially skipping validation, provenance, staging, redaction, or audit controls even though the request does not ask for a malicious action. We introduce ShadowBench-MCP, a benchmark a...
  </details>

- **2026-11-08** — Hongjie Zhang, Xingcheng Li, Hanzhou Wu et al. — [RoCoMark: Robust Code Watermarking Against LLM-Based Functionality-Preserving Rewriting Attacks](http://arxiv.org/abs/2611.11399v2)
  <details><summary>📄 Abstract</summary>
  Large Language Models (LLMs) present significant challenges to source tracing of generated code, as LLM rewriting can substantially alter the syntactic and structural characteristics of watermarked code. However, existing watermarking methods often suffer severe performance degradation under LLM-based functionality-preserving rewriting attacks. We attribute this vulnerability not merely to the intensity of rewriting, but to a fundamental distribution mismatch between the perturbations encountere...
  </details>

- **2026-11-08** — Gijs Wijngaard, Felix Förster, Ross Wightman et al. — [LAION-Audio-XL: A Web-Scale Corpus and Scaling Studies for Contrastive Language-Audio Pretraining](http://arxiv.org/abs/2611.11592v1)
  <details><summary>📄 Abstract</summary>
  Recent progress on contrastive audio-language models can be attributed mainly to the scale and quality of their training data. Larger training datasets expose models to a broader range of sounds and corresponding audio captions. To exploit this, we collect 1.48 billion audio samples from academic datasets, internet datasets, web collections, Common Crawl, and YouTube, and process them with a multi-stage curation pipeline. Furthermore, we generate short and long captions for samples in our corpus...
  </details>

- **2026-11-08** — Ziqi Wang, Su Chen, Qiance Tang et al. — [UTOPI: Efficient Egocentric Long-Video Understanding in AR via User-Guided Token Pre-Compression](http://arxiv.org/abs/2611.11562v1)
  <details><summary>📄 Abstract</summary>
  As long-video understanding gains increasing attention, augmented reality (AR) devices are emerging as a compelling deployment platform. However, egocentric videos exhibit significant temporal redundancy, imposing substantial memory and computational burdens on resource-constrained AR hardware. To address this challenge, we introduce UTOPI, a plug-and-play pre-compression module designed specifically for egocentric long videos on AR platforms. First, we leverage user motion signals to estimate i...
  </details>

- **2026-11-08** — Zhanghu Zhao, Daolang Huang, Xinyi Wen et al. — [Amortized Bayesian Experimental Design with In-Context Knowledge Conditioning](http://arxiv.org/abs/2611.11512v1)
  <details><summary>📄 Abstract</summary>
  Amortized Bayesian experimental design (BED) enables real-time design strategies by shifting acquisition cost offline, but existing methods remain tied to the prior and task distribution they were trained on and cannot exploit additional information available at deployment. We introduce in-context amortized BED with unified knowledge encoding (IMBUE), a BED framework that admits external knowledge at deployment through a unified in-context interface. IMBUE accepts two forms of such knowledge wit...
  </details>

- **2026-11-08** — Chenhao Sun, Niels Mündler-Sasahara, Mark Vero et al. — [Coding Agents Propagate Vulnerabilities in Code Bases](http://arxiv.org/abs/2611.11455v1)
  <details><summary>📄 Abstract</summary>
  LLM-based coding agents are widely used to develop critical production software. Even though coding agents are known to occasionally write vulnerable code, there has not been any investigation into how code base vulnerabilities evolve over time under coding agent contributions. In this work, we close this gap by investigating whether and how vulnerabilities in existing code lead coding agents to introduce similar vulnerabilities in the code they write. We first evaluate coding agents on 96 tasks...
  </details>

- **2026-11-08** — Hongjie Zhang, Xingcheng Li, Hanzhou Wu et al. — [RoCoMark: Robust Code Watermarking Against LLM-Based Functionality-Preserving Rewriting Attacks](http://arxiv.org/abs/2611.11399v1)
  <details><summary>📄 Abstract</summary>
  Large Language Models (LLMs) present significant challenges to source tracing of generated code, as LLM rewriting can substantially alter the syntactic and structural characteristics of watermarked code. However, existing watermarking methods often suffer severe performance degradation under LLM-based functionality-preserving rewriting attacks. We attribute this vulnerability not merely to the intensity of rewriting, but to a fundamental distribution mismatch between the perturbations encountere...
  </details>

- **2026-11-08** — Zesen Chen, Youxuan Xu, Shigang Li — [MG-Cache: Multi-Granularity Caching for Accelerating Diffusion Transformer Inference](http://arxiv.org/abs/2611.11365v1)
  <details><summary>📄 Abstract</summary>
  Diffusion Transformer (DiT) models, while having become a powerful backbone for generative synthesis, suffer from high inference cost on generating high-resolution images. Diffusion caching has emerged as a promising acceleration technique to reduce inference cost. However, existing caching strategies fail to accurately identify the varying importance of different computational modules and rarely coordinate cache reusing across the timestep and layer granularities, making it difficult to control...
  </details>

- **2026-11-08** — Xu He, Sagar Patel, Shu Wang — [Tracing MCP Security Vulnerabilities: Constructing and Analyzing an MCP Security Vulnerability Dataset](http://arxiv.org/abs/2611.11104v1)
  <details><summary>📄 Abstract</summary>
  As a core protocol for integrating large language models (LLMs) with external data sources and tools, the Model Context Protocol (MCP) has quickly become a key interface in emerging AI agent systems. As the MCP ecosystem expands, reported vulnerabilities have also increased, creating a growing software-security attack surface. However, MCP vulnerability information remains scattered, noisy, and difficult to study systematically. This paper addresses that gap by constructing a curated MCP vulnera...
  </details>

- **2026-11-08** — Elliott Piercy, Justin Chan, Sepand Dyanatkar — [What Does Multiple Choice Actually Measure? Disentangling Video Understanding from Option Exploitation](http://arxiv.org/abs/2611.11062v1)
  <details><summary>📄 Abstract</summary>
  Video understanding evaluations are intended to measure a model's proficiency in video perception and task solving. However, current VideoQA benchmarks struggle to isolate these capabilities due to their reliance on multiple-choice (MC) answer guidance, language priors, and fragile scoring pipelines. Disentangling these confounding factors reveals how much of a model's score is supplied by the evaluation context rather than earned through faithful perception. Across six VideoQA benchmarks of var...
  </details>

- **2026-11-07** — Joel Lehman, Kenneth O. Stanley — [Unified Factored Representations Resist Catastrophic Forgetting](http://arxiv.org/abs/2611.11020v1)
  <details><summary>📄 Abstract</summary>
  This paper explores an unexpected connection between the quality of a neural network's (NN's) internal representation and its vulnerability to catastrophic forgetting. The representational forgetting hypothesis is that networks with unified, factored representation (UFR) can resist catastrophic forgetting without any modification to the underlying fine-tuning algorithm or network architecture. The key insight is that catastrophic forgetting may largely result from fractured entangled representat...
  </details>

- **2026-11-07** — Binchi Zhang, Hadi Abdullah, Yiwei Cai et al. — [When Safety Becomes An Outlier: Understanding the Retention of LLM Safety Behaviors](http://arxiv.org/abs/2611.10971v1)
  <details><summary>📄 Abstract</summary>
  Safety-aligned large language models often lose their safety behaviors after fine-tuning, even when safety data are included. While this fragility is well documented, its underlying cause remains unclear. In this paper, we propose that formulaic refusal strings can function as outlier modes: narrow, weakly grounded response patterns that are easy to fit but vulnerable to subsequent updates. Controlled experiments support this account: fixed refusals are acquired much like arbitrary constant stri...
  </details>

- **2026-11-07** — Rahul Saha, Alan Li, Anton Xue et al. — [Improving Analytic Constants via Interpretable AI-Guided Lean Proof Refinement](http://arxiv.org/abs/2611.10961v1)
  <details><summary>📄 Abstract</summary>
  AI agents are increasingly capable of discovering new mathematical results, yet their reasoning and generated proofs can be difficult to understand and verify. We introduce an interpretable framework for AI-guided mathematical discovery, focused on improving quantitative bounds on analytic constants. Our key insight is that existing proofs often contain slack in intermediate lemmas, which can be tightened without reconstructing the entire argument. To exploit this structure, we represent proofs ...
  </details>

- **2026-11-07** — Nicholas Pecka, Lotfi Ben Othmane, Renee Bryce — [Validating AI-Discovered Cloud Threats on Live Infrastructure: A Multi-Model, Multi-Cloud Study](http://arxiv.org/abs/2611.10947v1)
  <details><summary>📄 Abstract</summary>
  Cloud infrastructure threat modeling lacks empirical validation of AI-discovered threats. We present a three-phase methodology of multi-agent threat discovery, automated exploit synthesis, and non-destructive live validation, and apply it to three commercial foundation models on two cloud architectures, validating each threat natively on the cloud (AWS, GCP, or Azure) it was discovered against. Of 233 AI-discovered threats, 103 were confirmed and 34 refuted (75.2\% precision, 95\% CI [67.3, 81.7...
  </details>

- **2026-11-07** — Luv Verma — [What Broke & Why: Practical Lessons from Reinforcement Learning Post-Training](http://arxiv.org/abs/2611.10844v1)
  <details><summary>📄 Abstract</summary>
  Reinforcement learning with verifiable rewards (RLVR) has become an important way to improve how language models reason, solve problems, and use tools. But getting it to work in practice is not always straightforward. Training can fail because a model receives no useful reward, learns to exploit the reward system, stops exploring, or appears to improve when the evaluation itself is misleading.   In this book, we give a practical introduction to reinforcement learning post-training for language m...
  </details>

- **2026-11-06** — Aria Wong, Joshua Engels, Neel Nanda — [Designing Effective Monitor-Based Interventions for Mitigating Reward Hacking During RL](http://arxiv.org/abs/2611.09828v1)
  <details><summary>📄 Abstract</summary>
  Reinforcement learning (RL) rewards are notoriously difficult to design and control, often leading to the model learning unintended behaviors such as reward hacking. One potential solution is to monitor for reward hacking and penalize it when detected; however, training against a monitor could lead to evasive behavior, and our general understanding of how to apply monitors effectively during training is limited. To study how best to use monitors to mitigate reward hacking, we introduce and open ...
  </details>

- **2026-11-06** — Junlin Wang, Haozhe Chen, Ang Li et al. — [Test-Time Compute Scales Better with Parallel Agent Teams](http://arxiv.org/abs/2611.09798v1)
  <details><summary>📄 Abstract</summary>
  Test-time scaling improves the performance of a fixed model by spending more computation at inference. There are two common ways to spend it on agents when a verifier can score every attempt. Best-of-N sampling runs many independent agents and keeps the best result but saturates quickly. One large team of collaborating agents can score higher but stops improving as it grows. Can we get the best of both? Our method, parallel agent teams, does so by sampling many small teams in parallel and keepin...
  </details>

- **2026-11-06** — Jinho Kang, Jinsook Kim — [Safety Is $Π_1$, Provability Is $Σ_1$: One Framework for the Hugging Face Breach and OpenAI's Mathematical Proofs](http://arxiv.org/abs/2611.09736v1)
  <details><summary>📄 Abstract</summary>
  OpenAI's agents breached Hugging Face in July 2026, and the same company released more than seven hundred AI-generated manuscripts of mathematical proofs in October 2026. The first event is read as a failure in security, while the second is read as a success in mathematics. We read both through the hybrid framework of our paper (Kim and Kang, 2026, arXiv:2611.01914), in which coding, proving, and learning from data are derivations by one and the same deductive mechanism, distinguished by the kin...
  </details>

- **2026-11-06** — Marc Barthelemy, Manlio De Domenico — [Slow structures, fast degrees of freedom, and the morphology of chess openings](http://arxiv.org/abs/2611.09710v1)
  <details><summary>📄 Abstract</summary>
  Chess openings naturally separate into slow and fast degrees of freedom: pawns evolve through irreversible moves, whereas pieces can be rapidly reorganized within the resulting structure. We exploit this separation to construct a quantitative morphology of opening space. From a catalogue of 3810 named variations, 1749 reach a common depth of $N=10$ plies, corresponding to 619 distinct positions and only 435 joint pawn structures. We characterize these positions through observables measuring pawn...
  </details>

- **2026-11-06** — Danyal Ahmed, Edouard Oyallon — [Know What You Need: Efficient Activation Checkpointing](http://arxiv.org/abs/2611.09614v1)
  <details><summary>📄 Abstract</summary>
  Large Language Model training is increasingly constrained by memory capacity. Activation Checkpointing reduces activation memory by avoiding storing selected activations during the forward pass and rematerializing them during backpropagation, thereby trading memory savings for additional computation. Although this technique is essential for scaling model training, rematerialization can be prohibitively expensive, particularly for Transformer linear layers. Approximate computation could reduce th...
  </details>

- **2026-11-06** — Vitalii Aksenov, Oliver Henze — [Bayesian Inverse Problems for EUV reflectometry with regularized JKO scheme](http://arxiv.org/abs/2611.09574v1)
  <details><summary>📄 Abstract</summary>
  We study a Bayesian inverse problem in EUV reflectometry, where optical constants and layer thicknesses are inferred from angle- and wavelength-resolved reflection measurements. The physical process is modeled and evaluated using an efficient forward model based on the transfer matrix method. As an alternative to computationally expensive sampling-based inference, we employ an Eulerian, entropically regularized Jordan-Kinderlehrer-Otto (JKO) scheme that minimizes the Kullback--Leibler divergence...
  </details>

- **2026-11-06** — Seokin Seo, Sung Kuk Shyn, Minji Seo et al. — [DexDICE: Reconciling Safety and Performance via Dual-Expert Offline Imitation Learning](http://arxiv.org/abs/2611.09433v1)
  <details><summary>📄 Abstract</summary>
  Ensuring high returns while providing strong safety guarantees in offline imitation learning (IL) is a fundamental challenge: existing approaches either rely on explicitly specified cost functions, which are difficult to design for complex real-world safety constraints, or require expert demonstrations that are both safe and high-performing, which are often too costly to collect. We introduce dual-expert imitation learning, which leverages two complementary data sources: (i) safety-compliant dem...
  </details>

- **2026-11-06** — Emil Schätzle, Markus Püschel — [MINE: Entropy-coded Memory-efficient Inference for Large Language Models](http://arxiv.org/abs/2611.09424v1)
  <details><summary>📄 Abstract</summary>
  We present MINE (Memory-efficient INference Engine), a lossless entropy coding approach that accelerates single-stream inference of Large Language Models (LLMs), where existing lossless compression methods yield speedups only for specific data types such as \texttt{BF16} and under additional assumptions. Single-stream decoding is strongly memory-bound, since every weight must be streamed from memory once per generated token and requests cannot be batched in local or low-latency deployments. At t...
  </details>

- **2026-11-06** — Yutang Lu, Shuai Jiang, Fei Su et al. — [SPSC: Zero-Shot Cross-Subject EEG-to-Image Reconstruction via Semantic Preservation and Subspace Calibration](http://arxiv.org/abs/2611.09380v1)
  <details><summary>📄 Abstract</summary>
  Pretrained vision-language models and diffusion generators have driven rapid progress in brain-to-image generation, while EEG-based reconstruction is still constrained by low signal-to-noise ratio and cross-subject semantic shifts. Zero-shot cross-subject reconstruction poses even greater challenges: EEG semantic embeddings learned from source subjects deviate from the manifold of image embeddings of the unseen target subject, particularly when neither target labels nor target image embeddings a...
  </details>

- **2026-11-06** — Seokin Seo, Byung-Jun Lee, Jongmin Lee et al. — [Mitigating Covariate Shift in Behavioral Cloning via Robust Stationary Distribution Correction](http://arxiv.org/abs/2611.09371v1)
  <details><summary>📄 Abstract</summary>
  We consider offline imitation learning (IL), which aims to train an agent to imitate from the dataset of expert demonstrations without online interaction with the environment. Behavioral Cloning (BC) has been a simple yet effective approach to offline IL, but it is also well-known to be vulnerable to the covariate shift resulting from the mismatch between the state distributions induced by the learned policy and the expert policy. Moreover, as often occurs in practice, when expert datasets are c...
  </details>

- **2026-11-06** — Armin Pirastehzad, Bart Besselink — [Hierarchical Signal Temporal Logic Control of Continuous-Time Systems](http://arxiv.org/abs/2611.09283v1)
  <details><summary>📄 Abstract</summary>
  For linear continuous-time systems, we solve the signal temporal logic (STL) control problem by translating it from continuous to discrete time such that a solution to the discrete-time problem guarantees a solution to the original continuous-time one. We split control synthesis into three hierarchical tasks. First, we discretize the continuous-time STL formula into a discrete-time one by sampling the temporal behavior it specifies. We accordingly discretize the continuous-time system by constru...
  </details>

- **2026-11-06** — Siyuan Yan, Shen Gu, Xiaoxing Ma et al. — [DUET: Dual-Sparse Inference for Block Diffusion Language Models](http://arxiv.org/abs/2611.09239v1)
  <details><summary>📄 Abstract</summary>
  Diffusion language models (DLMs) enable parallel token generation through iterative denoising, yet their inference remains costly due to repeated attention over a growing historical prefix and repeated processing of the entire current generation block. Historical attention becomes increasingly expensive as generation progresses, while all current-block positions are propagated through the Transformer at every denoising step even though only a small fraction are typically resolved at that step. I...
  </details>

- **2026-11-06** — Phi-Hung Hoang, Van-Manh Tran, Nam-Thuan Trinh et al. — [HMMF-Net: A Lightweight Hierarchical Multi-Frame Multimodal Fusion Network for Accurate Fish Feeding Intensity Assessment](http://arxiv.org/abs/2611.09224v1)
  <details><summary>📄 Abstract</summary>
  Automated fish feeding intensity assessment (FFIA) is important for precision aquaculture and feed cost optimization. However, unimodal methods are vulnerable to acoustic noise and visual disturbances, while existing multimodal frameworks often rely on computationally intensive 3D convolutions or Transformers, limiting their use on edge devices. To address these limitations, we propose HMMF-Net, a lightweight multimodal architecture that combines early multi-frame visual encoding and multi-axis ...
  </details>

- **2026-11-06** — Bohan Wang, Shuo Chen, Yunzhi Li et al. — [Trajectory Forcing: Exploiting Diffusion Trajectories for Autoregressive Long Video Generation](http://arxiv.org/abs/2611.09096v1)
  <details><summary>📄 Abstract</summary>
  Autoregressive (AR) modeling is arguably the only way to extend a fixed-length video diffusion model to longer or even streaming videos. However, existing AR diffusion methods use only the previously predicted chunk as context for the next, discarding the intermediate predictions that constitute the chunk's generation history. In contrast, conventional AR models such as LLMs condition on the entire history of preceding tokens. To this end, we propose Trajectory Forcing (TraF), an AR diffusion me...
  </details>

- **2026-11-06** — Luzhan Yuan, Chao Mi, Xiahao Shi et al. — [TUGB: A Two-stage Uncertainty-aware Generative Auto-Bidding Framework](http://arxiv.org/abs/2611.09091v1)
  <details><summary>📄 Abstract</summary>
  Generative modeling, particularly Decision Transformers, shows promise in auto-bidding strategies. However, it struggles with limited exploration in static offline datasets, vulnerability to dynamic environmental shifts, and a reliance on heuristic return-to-go (RTG) specifications that may yield suboptimal performance on unseen traffic. To address these challenges, we propose the Two-stage Uncertainty-aware Generative Auto-Bidding (TUGB) framework. TUGB integrates generative sequence modeling w...
  </details>

- **2026-11-06** — Rui Qi, Yunlong Liang, Yufeng Chen et al. — [MARS: Training Multilingual Search Agents for Retriever-Free Evidence Acquisition](http://arxiv.org/abs/2611.09090v1)
  <details><summary>📄 Abstract</summary>
  Existing multilingual retrieval-augmented generation relies heavily on learned retrievers and similarity-based ranking from multilingual collections, which are vulnerable to cross-lingual retrieval errors and indexing overhead. In this paper, we explore retriever-free multilingual search, where the model directly interacts with raw corpora through executable shell commands. This paradigm shifts the bottleneck to multilingual search action generation, where exact search is sensitive to entity sur...
  </details>

- **2026-11-06** — Jialiang Dong, Willy Susilo, Xu Gai et al. — [Beyond a Single Commit: Anchor-Guided Reconstruction of Multi-Commit Patches](http://arxiv.org/abs/2611.09026v1)
  <details><summary>📄 Abstract</summary>
  Vulnerability patch identification plays a critical role in software security by linking reported vulnerabilities and the corresponding fixes, enabling reliable vulnerability analysis, mitigation, and automated security tool development. As software systems evolve in complexity, vulnerability remediation has increasingly shifted from single-commit fixes to multi-commit fixing processes. Although many studies have been proposed to identify fixing commits associated with target vulnerabilities aut...
  </details>


### 📂 defense
*防御与防护方法 / Defense & Protection Methods* — 49 papers

- **2026-11-10** — James Rice, Ji Hwan Park, Andres Kwasinski — [What a CAGE 4 Score Measures: An Audit of a Learned Cyber-Defense Benchmark, Its Reference Defenders, and the Tables Built on Them](http://arxiv.org/abs/2611.14068v1)
  <details><summary>📄 Abstract</summary>
  CAGE Challenge 4 is the benchmark on which learned multi-agent cyber defenders are compared. We reproduce its two reference defenders, KEEP and H-MARL Expert, in a pinned container and show that three things read from it measure less than they are taken to measure. First, the simulator silently discards any action asserted for an agent whose previous action is still running, and charges one point for a discarded Restore as for one that runs. The documented observation does not expose the busy fl...
  </details>

- **2026-11-10** — Luka Dragar, Peter Peer, Vitomir Štruc et al. — [Metric-Aligned Group Relative Policy Optimization for Explainable Deepfake Detection](http://arxiv.org/abs/2611.14436v1)
  <details><summary>📄 Abstract</summary>
  Deepfake detectors are commonly evaluated on real/fake classification alone, but real-world applications require explanations of the visual evidence behind each prediction. Joint vision-language models struggle with authenticity assessment, producing "real" narratives for manipulated images. To address this, we propose a decoupled predict-then-explain pipeline as our submission to the ACM Multimedia 2026 Explainable Deepfake Detection Challenge, with methods trained and evaluated on the XPlainVe...
  </details>

- **2026-11-10** — Patrick Nowakowski, Cameron Little, Mahima Gupta et al. — [Analysis and Demonstration of a Current-Stiff, Isolated Capacitive Bridge Transformer](http://arxiv.org/abs/2611.14416v1)
  <details><summary>📄 Abstract</summary>
  The traditional Voltage Source Inverter (VSI) based Dual Active Bridge (DAB) utilizes a transformer at its center to provide galvanic isolation and a turns ratio for step up/down functionality. However, the transformer is often the limiting factor of the DAB, especially as semiconductor switching speeds improve, given steel core losses, winding losses, etc. This paper presents a new DAB architecture based on Current Source Inverters (CSIs) coupled through, and isolated by, an AC capacitive bridg...
  </details>

- **2026-11-10** — Naveen Babu Narayanan Nair, Sajay Kurup — [Verifiable Agentic Traffic Class: A Policed Quality-of-Service Mechanism for Agentic AI Traffic, Evaluated from Simulation to Real-Kernel Adversarial Testing](http://arxiv.org/abs/2611.14211v1)
  <details><summary>📄 Abstract</summary>
  Software agents built on large language models generate traffic unlike human web traffic, yet routers have no class for it and cannot verify a sender's claim to be an agent. This paper proposes the Verifiable Agentic Traffic Class (VATC), which combines a reserved Differentiated Services Code Point (DSCP) value declaring agent traffic, a router-side classifier that demotes flows contradicting the declaration to a class served after best-effort traffic, and a rate-limited priority queue. VATC was...
  </details>

- **2026-11-10** — Steve Nouyep, Maxime Puys, Sébastien Salva — [Isolation Is Not Confidentiality: Security Boundaries of Geometric Access Control in RAG](http://arxiv.org/abs/2611.14061v1)
  <details><summary>📄 Abstract</summary>
  Retrieval-Augmented Generation (RAG) systems increasingly rely on vector databases containing documents governed by different access-control policies. Recent search-preserving geometric approaches enforce such access control by structuring the embedding space so that transformed embeddings, which we call protected representations, remain retrievable without exposing information across policy boundaries.   We provide a unified security analysis of this paradigm, covering policy isolation, represe...
  </details>

- **2026-11-10** — Yuka Saito, Ikumi Numaya, Jun Suzuki et al. — [Beyond Fluent Responses: Finding User Dissatisfaction in Human-AI Interactions](http://arxiv.org/abs/2611.13894v1)
  <details><summary>📄 Abstract</summary>
  As large language models generate increasingly high-quality responses, recent work on response evaluation has moved beyond response-centered criteria, such as correctness and coherence, toward user-centered criteria, including user preferences and perceived usefulness. This shift is fundamentally important for developing technologies that are truly useful to real-world users. While conventional response evaluation quantifies the quality of the response itself, users' satisfaction in real convers...
  </details>

- **2026-11-10** — Bastien Dussard, Aur{é}lie Clodic, Guillaume Sarthou — [Taxonomy-Agnostic Neurosymbolic Grounding of Robot Kinematics](http://arxiv.org/abs/2611.13850v1)
  <details><summary>📄 Abstract</summary>
  While symbolic reasoning for task allocation requires grounding a robot's physical capabilities, standard Unified Robot Description Format (URDF) files provide only low-level kinematics without the formal semantic context needed for reasoning. We present URDF2Ontology, an automated, taxonomy-agnostic neurosymbolic framework that transforms raw URDF files into populated, grounded OWL ontologies. It leverages a Large Language Model (LLM) for targeted semantic reasoning, coupled with an iterative s...
  </details>

- **2026-11-10** — Boshra Khalili, Sonia Moshfeghi, Jinwoo Jang et al. — [AgenticConflictLens: From Long Traffic Videos to Verifiable Conflict Evidence](http://arxiv.org/abs/2611.13540v1)
  <details><summary>📄 Abstract</summary>
  Traffic cameras continuously record urban road-user behavior, providing proactive safety evidence beyond crash reports. Yet safety-critical events - conflicts, near misses, unsafe turns, sudden braking, and crosswalk interactions - are rare and brief, buried in hours of routine footage. Existing traffic-video pipelines extract detections, trajectories, and risk scores but process footage uniformly, without adapting to an analyst's query. Vision-language methods improve scene understanding but of...
  </details>

- **2026-11-10** — Sheethal Bhat, Bogdan Georgescu, Awais Mansoor et al. — [Toward Foundation Detection Models via Example-Based Grounding in EM-DETR](http://arxiv.org/abs/2611.14518v1)
  <details><summary>📄 Abstract</summary>
  DeepLearning (DL)-based Computer-Aided Diagnostic (CAD) systems have shown great promise in supporting clinicians, but their performance heavily depends on the availability of large, well-annotated datasets. In medical lesion detection, the scarcity of comprehensive, stan dardized annotations and the heterogeneity of existing datasets limit the development of robust foundation models. In this work, we introduce a novel approach to building a multi-domain foundation model for le sion detection by...
  </details>

- **2026-11-10** — Peng Chen, Yihang Wang, Zhongwen Rao et al. — [TimeSeek: Multi-Task and Multi-Domain Pretraining for Generalized Time Series Analytics](http://arxiv.org/abs/2611.14491v1)
  <details><summary>📄 Abstract</summary>
  Time series analytics has been widely applied across various domains. While existing time series foundation models (TSFMs) have demonstrated promising results, they still face two major challenges: 1) Most TSFMs mainly rely on stacking Transformer layers to increase parameter size, lacking the ability to adaptively model complex time series patterns from multi-domain data. 2) Current TSFMs are primarily pre-trained for specific tasks, e.g., forecasting or anomaly detection, and a few models supp...
  </details>

- **2026-11-10** — Mikhail Kulakov, Ruslan Solikhov, Ivan Bondarenko — [Sckwoky at SHROOM-Visions: Character-Level Hallucination-Span Detection in Image-Conditioned VLMs via Dual-Prompted LoRA Decoders](http://arxiv.org/abs/2611.14100v1)
  <details><summary>📄 Abstract</summary>
  We present our system for the SHROOM-visions 2026 shared task on character-level hallucination span detection in image-conditioned vision-language model (VLM) responses, evaluated across English, French, Italian, and Chinese. The detector is built on a frozen Gemma-4-12B-it backbone with trainable LoRA adapters (approximately 10.7M parameters). Because the backbone is a causal decoder, hidden states read from a single copy of an answer cannot attend to subsequent tokens; we therefore repeat the ...
  </details>

- **2026-11-10** — Fábio A. S. Passos, Péricles B. C. Miranda, Ana Paula Cavalcanti — [MISO-BR: An Open Corpus for Misogyny Detection in Brazilian Portuguese](http://arxiv.org/abs/2611.14036v1)
  <details><summary>📄 Abstract</summary>
  Misogyny is among the most prevalent forms of online hate speech directed at Brazilian users, yet open and auditable resources dedicated to it in Brazilian Portuguese remain scarce. We introduce MISO-BR, an open, documented and versioned corpus of 896 balanced social media texts annotated for binary misogyny, released with its construction protocol and reproducible baselines. The corpus combines lexicon- and target-guided scraping from X with items imported from OLID-BR, a large language model t...
  </details>

- **2026-11-10** — Jinchan Kim, Jinhee Im, Hyunsouk Cho — [CASCADE: Constraint-Aware SCAffolded DEcomposition for Logical Anomaly Detection](http://arxiv.org/abs/2611.13820v1)
  <details><summary>📄 Abstract</summary>
  Logical Anomaly Detection (LAD) requires verifying whether all category-specific constraints, such as object counts, pairing relations, and measurement ranges, are satisfied by a query image given only a few normal references. Recent LAD methods based on Large Vision-Language Models (LVLMs) formulate this as checklist verification, decomposing the decision into independent textual checks. This decomposition, however, is text-only. Every item still reads the same unmodified query image, so the LV...
  </details>

- **2026-11-10** — Kushal Trivedi, Mayank Mahor, Dhruv Sanghvi et al. — [You Are What You Read: Indian Political News Media Bias Dataset for Hindi Language](http://arxiv.org/abs/2611.13686v1)
  <details><summary>📄 Abstract</summary>
  Media bias understanding and detection remains an under-researched problem for Indian context, specifically for Indic languages, such as, Hindi, which is widely spoken in India. In this paper, we introduce a comprehensive, multi-annotator, explainable dataset consisting of 448 unique articles from four leading Indian news agencies publishing in Hindi. We focus on Hindi, the most spoken and an official language of India. The study of media bias is particularly relevant in the Indian context due t...
  </details>

- **2026-11-09** — Shaohuang Wang, Jinghao Wen, Xulei Zhang et al. — [Dependable Long-Horizon LLM Agents: A Trajectory-Centered Empirical Study of Where Errors Enter and Which Controls Reach Them](http://arxiv.org/abs/2611.13254v1)
  <details><summary>📄 Abstract</summary>
  When an LLM agent fails part-way through a long task, the usual analysis records a symptom: a failure-mode label, or the agent and step judged responsible. It does not say where the error entered, which state carried it to the symptom, whether anything in the trajectory contradicted it, or which control could have caught it. We define an episode record that ties a candidate fault to its origin, propagation, detection, response and consequence, located by operational phase and state domain, and t...
  </details>

- **2026-11-09** — Dipin Khati, Shubham Mehrotra, Bin Bi et al. — [AgentScript-Eval: Benchmarking LLMs and Agents for Code Generation in an Enterprise DSL](http://arxiv.org/abs/2611.13183v1)
  <details><summary>📄 Abstract</summary>
  Domain-specific languages (DSLs) are widely used in enterprise software, giving a compact interface to complex tasks, from data access to infrastructure automation. Platforms increasingly extend them to agents, where a developer declares the topics, permitted actions, and guardrails of an agent rather than writing general-purpose code. Large language models (LLMs) write general-purpose code well, but that ability has been measured almost entirely on languages abundant in public pretraining data,...
  </details>

- **2026-11-09** — Daniel Campa, Spandan Das, Srinjoy Das — [FaST: Factored Synthesis of Transitions for Offline Reinforcement Learning](http://arxiv.org/abs/2611.13013v1)
  <details><summary>📄 Abstract</summary>
  Synthetic data augmentation promises to scale offline reinforcement learning beyond fixed logged datasets, but leading diffusion-based generators model the transition tuple (state, action, next state, reward, terminal) as a monolith: no single factor can be natively redrawn in isolation. We present FaST (Factored Synthesis of Transitions), which factors transitions via the chain rule into state, action, dynamics, reward, and terminal stages, fitting each with an estimator matched to its statisti...
  </details>

- **2026-11-09** — Albert Shaju, Christo Kurisummoottil Thomas, Mingzhe Chen — [STAR: Semantic-Criticality Tiered Allocation of Radio Resources via Zero-Shot Learning](http://arxiv.org/abs/2611.13238v1)
  <details><summary>📄 Abstract</summary>
  In remote inference, edge devices transmit high-resolution images over wireless links to a receiver, where an artificial intelligence (AI) model answers task-specific questions about these images to enable reliable decisions. These answers are often determined by a small set of task-causal pixels, such as those of text, whose corruption changes the answer, so these pixels must be delivered with high fidelity. Conventional transmission protects every pixel equally, so it either consumes many reso...
  </details>

- **2026-11-09** — Izzeddin Teeti, Vaibhav Kango, Nidhi Sridhar et al. — [Multimodal Road Closure Mapping via Cross-Modal Graph Attention](http://arxiv.org/abs/2611.13192v1)
  <details><summary>📄 Abstract</summary>
  Accurate and timely identification of road closures is critical for large-scale navigation and logistics systems, yet remains challenging due to the need to jointly reason over visual evidence, spatial context, and road network topology. Existing approaches either rely on manual map updates or focus on detecting closure-related objects without resolving which road segment is affected. In this work, we introduce a unified multimodal and multitask framework that jointly performs road closure class...
  </details>

- **2026-11-09** — Ayesha Habib, Huixiang Zhang, Dan Zhu et al. — [Text2NGAC: a multi-LLM pipeline for NGAC policy extraction with mutation-based verification](http://arxiv.org/abs/2611.12572v1)
  <details><summary>📄 Abstract</summary>
  Access-control policies are written in natural language but enforced as formal models, and translating them into NIST Next Generation Access Control (NGAC) graphs remains unsolved: prior systems cover only subsets of the NGAC model, and none verify the graphs they extract. We present Text2NGAC, a pipeline of cooperating large language models that disambiguates each sentence before extraction, escalates uncertain sentences to a multi-model ensemble, and checks the resulting graph with a five-stra...
  </details>

- **2026-11-09** — Samuel Joseph Amouyal, Ofek Glick, Yaniv Menasherov et al. — [LEGION: Benchmarking Language Agents on Sparse-Signal Investigation Under Adversarial Noise](http://arxiv.org/abs/2611.11896v1)
  <details><summary>📄 Abstract</summary>
  Autonomous language-model agents are increasingly deployed on discovery-driven tasks where signal is sparse and most retrieved information is irrelevant. Current benchmarks fail to evaluate this regime due to dense signals, cooperative environments, and ground truth typically being only a few tool calls away. We introduce Legion, a benchmark framework coupling a stochastic enterprise-telemetry simulator (Legion-Sim) with a tiered library of 74 expertly-crafted adversarial scenarios (Legion-Bench...
  </details>

- **2026-11-09** — Heng Fang, Zehui Guo, Yuehan Zhang et al. — [World In-Context Learning for Agentic Robot Manipulation](http://arxiv.org/abs/2611.12885v1)
  <details><summary>📄 Abstract</summary>
  Trained action policies write manipulation skill into network weights, tying what is learned to the distribution it is learned from. In-context learning (ICL) avoids this coupling but has not matched trained policies, because a demonstration recorded in another scene carries no feedback from the world the robot currently faces. We observe that what an agent learns in context is semantic, recording task steps and object roles rather than visual appearance, so experience gathered in one world tran...
  </details>

- **2026-11-09** — Tiziano Maisonhaute, Jean-Christophe Soulié, Fabien Michel — [A Modular Perspective for Modeling MARL Systems](http://arxiv.org/abs/2611.12314v1)
  <details><summary>📄 Abstract</summary>
  The growing complexity of Multi-Agent Reinforcement Learning (MARL) has fragmented the literature, obscuring underlying architectural choices behind diverse implementations. This fragmentation makes it difficult to evaluate critical modeling dimensions in isolation, identify how components affect the resulting system dynamics, and compare, reuse, or combine contributions across the literature.   This paper proposes a modular perspective for modeling, analyzing, and implementing MARL systems. We ...
  </details>

- **2026-11-09** — Nir Sharon, Sheng Xu — [Distribution-Free Symmetry Detection in Multi-Reference Alignment at Low SNR](http://arxiv.org/abs/2611.11872v1)
  <details><summary>📄 Abstract</summary>
  Symmetry can reveal the structure of a signal, but detecting it becomes difficult when observations are noisy and randomly transformed. We study how to infer symmetry directly from multi-reference alignment data with additive isotropic Gaussian noise of known variance, without aligning the observations or knowing how the transformations were sampled. For cyclic symmetry, we identify a simple statistical signature that yields tests with exact finite-sample error guarantees. We demonstrate their p...
  </details>

- **2026-11-09** — Suryansh Talukdar, Taha Sarwat, Jin Soung Yoo — [LogCDM: Interpretable Log Anomaly Detection via Behavioral Graph Drift and Adaptive Signal Fusion](http://arxiv.org/abs/2611.12775v1)
  <details><summary>📄 Abstract</summary>
  Log-based anomaly detection is increasingly dominated by large pretrained models, from BERT-scale encoders to 8B-parameter language models, which require GPUs at inference time and are difficult to deploy on the monitoring nodes where logs are produced. We present LogCDM, a compact detector that scores each log session using three complementary signals: the next-event surprise of a small causal Transformer, the distance between a graph-attention embedding of the session's own transition graph an...
  </details>

- **2026-11-09** — Bernat Homs, Oscar Palomar, Miquel Moreto et al. — [Will AI mess my RTL? A snapshot-based approach to verifying AI-written RTL](http://arxiv.org/abs/2611.12712v1)
  <details><summary>📄 Abstract</summary>
  With the growing interest in using AI (Artificial Intelligence) for RTL (Register-Transfer Level) hardware development, robust and comprehensive verification has become more important than ever. As Large Language Models (LLMs) increasingly assist in creating and modifying RTL designs, ensuring that these changes preserve existing functionality is paramount for building trust in AI-driven workflows. We present SVApshot, a fully automated framework that leverages LLMs to generate and systematicall...
  </details>

- **2026-11-09** — Davidson Chisom Onwubiko, Shahana Bano, Carlos Francisco Moreno-García — [A forensic evaluation framework for egocentric foundation models: an EFM3D case study for crime scene reconstruction](http://arxiv.org/abs/2611.12259v1)
  <details><summary>📄 Abstract</summary>
  Foundation models increasingly combine geometry, semantics, and spatial context for three-dimensional scene understanding, but their suitability for forensic crime scene reconstruction remains unclear. This study presents a structured forensic evaluation framework for egocentric foundation models and demonstrates it using the Egocentric Foundation Model for 3D (EFM3D). Four simulated indoor crime scenes were recorded with Meta Project Aria Gen~1 at Robert Gordon University's East Lodge House for...
  </details>

- **2026-11-09** — Jiwei Tian, Mouyang Cheng, Mingda Li — [AI-Driven Discovery of Entanglement Witness in Spin Hamiltonians](http://arxiv.org/abs/2611.11935v1)
  <details><summary>📄 Abstract</summary>
  Entanglement is a crucial resource in quantum science and engineering, but detecting it in many-body states from experimentally accessible observables remains challenging. Here we introduce EntNet, an AI-driven framework to discover compact combinations of spin observables that accurately distinguish entangled from fully separable many-body mixed states in one-dimensional spin-$1/2$ chains governed by short-range Hamiltonians. We construct local-unitary-invariant representations of measurable Pa...
  </details>

- **2026-11-09** — Peiyu Li, Pouya Hosseinzadeh, Soukaina Filali Boubrahimi et al. — [Scalable Counterfactual Explanations for Time Series via Policy Learning](http://arxiv.org/abs/2611.11704v1)
  <details><summary>📄 Abstract</summary>
  Generating counterfactual (CF) explanations for time series is challenging due to complex temporal dependencies and the computational inefficiency of traditional instance-specific optimization. We propose a policy learning framework for counterfactual explanation in time series, trained as a one-step contextual-bandit policy-learning problem. By training an actor-critic agent in the latent space of a pre-trained autoencoder, our method learns a transferable policy that captures global structural...
  </details>

- **2026-11-08** — Viktoriia Makovska, Tetiana Zakharchenko, Oleksandra Ostafiichuk — [WarBias: A Bilingual LLM Benchmark of Stereotypes About Internally Displaced People and Veterans](http://arxiv.org/abs/2611.11284v2)
  <details><summary>📄 Abstract</summary>
  This paper contains examples of stereotypes about veterans and displaced people that may be offensive or distressing. Social bias benchmarks for language models commonly examine categories such as gender, race, and religion, often drawn from lists of legally protected characteristics. Veterans and internally displaced people (IDPs) fall outside these lists, and stereotypes about them, which can undermine access to employment, housing, and social participation, remain largely absent from language...
  </details>

- **2026-11-08** — Yang Luo, Qingni Shen, Tairui Wang et al. — [PRISM: Causal Counterfactual Minimization of Agent Tool Privileges via Information Bottleneck Role Induction](http://arxiv.org/abs/2611.11539v1)
  <details><summary>📄 Abstract</summary>
  This paper shifts the object of role engineering from human users to large language model (LLM) agents, and proposes PRISM to address the over-authorization that arises when an agent obtains full tool privileges through the Model Context Protocol (MCP). PRISM formulates whether a tool is necessary for a task as an intervenable causal proposition, and applies structured interventions in a sandbox to learn a counterfactual necessity model. It then compresses trajectories into discrete latent varia...
  </details>

- **2026-11-08** — Jing Liang, Zhenyu Hou, Senthurbavan Kirubaharan et al. — [MOSU2: Long-range Navigation System with Multi-modal Scene Understanding](http://arxiv.org/abs/2611.11148v1)
  <details><summary>📄 Abstract</summary>
  Robots that travel long distances through public outdoor spaces must do more than avoid obstacles: they must remain on terrain suited to their mobility and decide when to proceed, yield, or detour around pedestrians, cyclists, vehicles, traffic signals, and temporary restrictions. These decisions are difficult because their correctness often depends on how a scene evolves, such as whether an approaching car is slowing or a cyclist will cross the robot's path. Vision-language models (VLMs) can in...
  </details>

- **2026-11-08** — Mohan W. Gupta, Sandy Tanwisuth — [System Prompts Affect Response Bias More Than Discriminability in LLM Safety](http://arxiv.org/abs/2611.11074v1)
  <details><summary>📄 Abstract</summary>
  Large language model safety evaluations often focus on a compliance-refusal tradeoff: models should refuse unsafe requests without refusing safe ones. We argue that this misses a broader form of prompt-conditioned task selection, where the same request can elicit different behaviors depending on the system prompt. We investigate this using a controlled evaluation crossing eight safety-task prompt families with three clarity levels across HarmBench, XSTest, and IHEval. Holding benchmark items fix...
  </details>

- **2026-11-08** — Viktoriia Makovska, Tetiana Zakharchenko, Oleksandra Ostafiichuk — [WarBias: A Bilingual LLM Benchmark of Stereotypes About Internally Displaced People and Veterans](http://arxiv.org/abs/2611.11284v1)
  <details><summary>📄 Abstract</summary>
  This paper contains examples of stereotypes about veterans and displaced people that may be offensive or distressing. Social bias benchmarks for language models commonly examine categories such as gender, race, and religion, often drawn from lists of legally protected characteristics. Veterans and internally displaced people (IDPs) fall outside these lists, and stereotypes about them, which can undermine access to employment, housing, and social participation, remain largely absent from language...
  </details>

- **2026-11-08** — Olga Lavinda — [Known Good, Known Bad: A Ground-Truth Calibration Protocol for AI Judgment in Science](http://arxiv.org/abs/2611.11673v1)
  <details><summary>📄 Abstract</summary>
  Scientific use of generative AI requires evaluation against cases with independently checkable answers. We present a ground truth calibration protocol that compares a verified reference case with reference deviant variants through neutral evaluation, an authority framed recheck, and a line by line audit. Human adjudication distinguishes deviation detection, premise accommodation, unsupported doubt, and correctness of the resulting calculation.   An instructor generated organic chemistry demonstr...
  </details>

- **2026-11-08** — Zhihao Zhang, Abhinav Kumar, Huaizhi Qu et al. — [Rethinking Geometric Depth in Monocular 3D Object Detection: A Projection-Consistent Reformulation](http://arxiv.org/abs/2611.11607v1)
  <details><summary>📄 Abstract</summary>
  Monocular 3D detection (Mono3D) hinges on recovering depth from a single image, for which the geometric formulation $z \approx f \cdot H / h_{2D}$ is widely adopted due to its simplicity and direct grounding in projective geometry. We show that this formulation harbors a systematic, projection-induced bias: substituting the 2D bounding-box height $h_{2D}$ recovers the depth of an object's visible front surface rather than its center, causing size-dependent underestimation that persists even unde...
  </details>

- **2026-11-07** — Ali Mohammadi Ruzbahani, Abbas Yazdinejad, Hadis Karimipour — [PIA: Agentic Physics-Informed Runtime Anomaly Detection](http://arxiv.org/abs/2611.11009v1)
  <details><summary>📄 Abstract</summary>
  Runtime anomaly detectors for cyber-physical systems are either learned as black boxes from normal data, which miss stealthy manipulations that keep every signal inside its normal range, or derived by hand from physical models, which requires expert effort for every plant. We introduce physicsinformed agents (PIA), in which a large language model agent writes the detector itself as a set of physical residuals, such as pump characteristics, tank mass balances, and controller logic, and refines ev...
  </details>

- **2026-11-07** — Ailin Barzegar, Davide Spinello, Mohammad Pirani — [Real-Time Threat Classification in Multi-Agent Systems via Topology-Coupled Hidden Markov Models](http://arxiv.org/abs/2611.10779v1)
  <details><summary>📄 Abstract</summary>
  Networked multi-agent systems coordinating in adversarial environments face compound cyber threats that alternate between false-data injection (FDI), denial-of-service (DoS), and stealthy decoy perturbations designed to mimic benign operational anomalies. Because the switching policy is latent and the plant dynamics evolve continuously, deterministic threshold detectors struggle to isolate deception without causing excessive false alarms. This paper presents an online, data-driven framework that...
  </details>

- **2026-11-07** — Ali Mohammadi Ruzbahani, Abbas Yazdinejad, Hadis Karimipour — [GradReason: LLMs as Meta-Learners that Replace Training Epochs with Training-Data-Free Weight Updates](http://arxiv.org/abs/2611.11005v1)
  <details><summary>📄 Abstract</summary>
  Standard training recipes make a fixed number of passes over the training data, even when an epoch mostly adds mini-batch noise. We study whether a large language model (LLM) that reads the weight and gradient history of a run can replace some of these epochs with updates that compute no gradient and read no training image. In GradReason, an LLM agent is called every ten epochs. In a restricted sandbox, it analyses recent weight snapshots, epoch-mean gradients, and validation metrics, then submi...
  </details>

- **2026-11-07** — Parthaw Goswami, Erfan Zareei, Amy Vogelsmeier et al. — [A Tool for Anonymized Clinical Knowledge Retrieval and Speaker Interaction Analysis of Healthcare Tele-mentoring Sessions](http://arxiv.org/abs/2611.10922v1)
  <details><summary>📄 Abstract</summary>
  We present a tool for anonymized retrieval of clinical knowledge and analysis of multi-speaker interactions in tele-mentoring sessions of Project ECHO (Extension for Community Healthcare Outcomes). Our tool's novel design includes: (a) a compound metadata filter that enforces strict speaker- and session-level isolation during retrieval, preventing cross-session context contamination; (b) MedGemma-4B as a locally-hosted language model for clinically grounded answer generation across three query m...
  </details>

- **2026-11-07** — Xiaoxiao Li, Ruinan Jin, Lili Meng et al. — [Beyond Real or Fake: A Dual-Channel Authenticity and Reasoning Protocol for Photographic Assessment](http://arxiv.org/abs/2611.10908v1)
  <details><summary>📄 Abstract</summary>
  Forensic verification has converged on a binary "real vs. fake" label that confates fully synthetic, tampered, and AI-retouched images despite their very different consequences. We argue that GenAI manipulations decompose along two complementary channels: a camera channel of sensor fingerprints (destroyed by neural processing), and a semantic channel of scene-level coherence (disrupted by content edits). Each manipulation type leaves a distinctive two-channel signature. We instantiate this taxon...
  </details>

- **2026-11-07** — Ankit Goyal, Santosh Jha, Zhuo Zhi et al. — [Firepool: Brokering Warm GPU Capacity for Agentic and RL Workloads at LinkedIn](http://arxiv.org/abs/2611.10832v1)
  <details><summary>📄 Abstract</summary>
  AI agents and reinforcement-learning (RL) trainers run thousands of short, isolated GPU jobs: tool calls, verifiers, and rollouts. A job often finishes in seconds, but starting a GPU pod for it takes 20-35 s even when the container image is already on the node, and minutes when it is not. A warm pod removes the wait only if it can serve the next job, and keeping pods warm must neither waste GPUs nor leak state between callers. Firepool, the sandbox and execution broker behind agentic and RL work...
  </details>

- **2026-11-07** — Chengyuan Ma, Shixiao Liang, Hangyu Li et al. — [Selective Cooperative Perception via Blind Spot Reasoning and Agentic Dialogue with Vision-Language Models](http://arxiv.org/abs/2611.10819v1)
  <details><summary>📄 Abstract</summary>
  Real-time cooperative perception (CP) in multi-agent traffic environments is highly resource-intensive, which posing scalability challenges for large-scale deployment. Efficiency can be significantly improved by selectively performing CP only in safety-critical scenarios and for key occluding objects. Vision-Language Models (VLMs) are well-suited for complex reasoning in dynamic and uncertain environments, making them a promising tool for this selective CP task. This study proposes a VLM-driven ...
  </details>

- **2026-11-07** — Zilin Guo, Tianrui Zhang, Yi Rong et al. — [BlenderFORGE: Framework for Optimizing Reactive 3D-Graphics Editing Ability of MLLMs](http://arxiv.org/abs/2611.10768v1)
  <details><summary>📄 Abstract</summary>
  Multimodal Large Language Models (MLLMs) have shown promise as interactive agents, yet precise, programmatic 3D graphics editing remains difficult to train because existing systems largely rely on closed-source model APIs and lack deterministic, state-verifiable execution environments. We present BlenderFORGE, a trainable data-environment-optimization framework for open-weight MLLM agents that edit explicit Blender scenes through Blender Python (bpy) code generation. BlenderFORGE targets four fu...
  </details>

- **2026-11-07** — Getnet Demil, Md Moinul Islam, Mourad Oussalah — [Hydro-Dataset: A Multi-Modal Open-Source Pipeline for Nordic Hydrological Research and Foundation Model Benchmarking](http://arxiv.org/abs/2611.10992v1)
  <details><summary>📄 Abstract</summary>
  Despite world-class snow monitoring by the Swedish Meteorological and Hydrological Institute (SMHI) and Finnish Meteorological Institute (FMI), no station-anchored, multi-parameter snow benchmark dataset exists for the Nordic boreal domain. We present Hydro-Dataset v1.1, a reproducible open-source pipeline that harmonizes 582 SMHI meteorological observation stations across nine hydrological winters (2015/16-2023/24) into a CF-1.9 NetCDF product with 1.8~million annotated station-days. Six derive...
  </details>

- **2026-11-07** — Chih-Yu Tsai, Chih-Heng Chang, Jian-Jiun Ding — [REDiff-AD: No Training and No Target Masks for Industrial Anomaly Image Generation via Diversity-Driven In-Context MMDiT](http://arxiv.org/abs/2611.10875v1)
  <details><summary>📄 Abstract</summary>
  Industrial anomaly detection is challenged by the scarcity and diversity of real defects, leaving insufficient anomalous data to effectively train downstream models. Existing anomaly generation methods often require product-specific fine-tuning, target mask annotation, or costly procedures to achieve realistic and diverse defects. We propose REDiff-AD, a framework that requires neither model training nor target masks and introduces Rectified Flow MMDiT into industrial anomaly generation for effi...
  </details>

- **2026-11-07** — Shuai Wu, Yanna Feng, Yufang Li et al. — [Patch correctness in automated program repair: A five-dimensional evidence framework and cross-benchmark audit from classical repair to coding agents](http://arxiv.org/abs/2611.10837v1)
  <details><summary>📄 Abstract</summary>
  Tests guide automated program repair and determine which candidate patches are reported as successful. Repository-level coding agents extend this feedback loop by generating tests and revising code after observing execution results. This technical report introduces a five-dimensional evidence profile and reporting protocol to audit how test observations support patch-correctness claims across classical repair systems and coding agents. We assemble an audit dataset of 39 benchmark and evaluation ...
  </details>

- **2026-11-06** — Ruihan Hu, Wei Luo, Yu-Ming Shang et al. — [Logit Laundering: Evading Data-Use Auditing in Large Language Models](http://arxiv.org/abs/2611.09446v1)
  <details><summary>📄 Abstract</summary>
  Data-use auditing in Large Language Models (LLMs) aims to determine whether the given data has been used for training, thereby supporting data ownership safeguards. A dominant solution is data watermarking, which embeds traceable signals into training data and detects them in model outputs. Recent studies have proposed many watermarking-based auditing methods in LLMs. However, systematic investigation from an adversarial perspective remains limited: non-compliant LLM providers would use unauthor...
  </details>

- **2026-11-06** — Ayush Sawarni, Wenqian Xing, Tijana Zrnic et al. — [Knowing When to Intervene: Causal Evaluation of AI Agents](http://arxiv.org/abs/2611.09792v1)
  <details><summary>📄 Abstract</summary>
  Current evaluations of agentic AI systems primarily rely on benchmarks. However, the static nature of benchmarks makes them uninformative about the value of auditing interventions at deployment time. For reliable deployment, we often need to determine within an agent's trajectory whether or not to intervene, e.g., by verifying the agent's current output or steering it toward different behavior, using either human review or more costly models or time-consuming agentic supervision. The value of su...
  </details>


### 📂 alignment
*对齐与安全约束 / Alignment & Safety Constraints* — 52 papers

- **2026-11-10** — Stine Lyngsø Beltoft, Jonas Vistrup, Peter Schneider-Kamp et al. — [Living constitutions: Participatory alignment for sovereign foundation models](http://arxiv.org/abs/2611.13402v1)
  <details><summary>📄 Abstract</summary>
  In Constitutional AI, a plain-text "constitution" encodes values and gets incorporated into a model via post-training. However, the procedure for creating such a constitution poses significant challenges: who contributes, who decides which norms are included, and to what extent must the process be participatory or democratic? These challenges can be paralyzing. Yet, we argue that taking action is essential: without a deliberate constitution, sovereign models would risk misalignment or default to...
  </details>

- **2026-11-10** — Amir Tahmasbi, Keshav Singh, Shaheer Raza et al. — [Demonstration of MANA: Multi-perspective Alignment of NPC Agents](http://arxiv.org/abs/2611.14431v1)
  <details><summary>📄 Abstract</summary>
  We present MANA (Multi-perspective Alignment of NPC Agents), an interactive approach for authoring NPC behavior through embodied demonstration. We show MANA in the context of Minecraft, where a developer aligns NPCs while playing the game itself. Activating MANA lets the developer dynamically switch into the point of view (POV) of any character and demonstrate, in-situ, how it would act given the surrounding context, through both movement and dialogue. MANA then distills each demonstration into ...
  </details>

- **2026-11-10** — Eoin M. Kenny, Salim I. Amoukou, Tom Bewley — [Beyond Proxy Metrics: MLLMs as Human Surrogates for Explainable AI Evaluation](http://arxiv.org/abs/2611.13926v1)
  <details><summary>📄 Abstract</summary>
  Explainable AI (XAI) has expanded into a broad and impactful research area, but the fundamental question of how best to evaluate explanation techniques has proven frustratingly elusive. Methodologies typically revolve around either proxy metrics which tell us little about the utility of an explanation, or human evaluation which---while generally considered the gold standard---is expensive, difficult to scale, and challenging to reproduce. In this paper, we investigate if Multimodal Large Languag...
  </details>

- **2026-11-10** — Fatemeh Mirhosseini, Yasaman S. Sefidgar — [How Well Do Benchmarks Evaluate LLMs' Use for Personal Health Informatics?](http://arxiv.org/abs/2611.13652v1)
  <details><summary>📄 Abstract</summary>
  Benchmarking is a valuable technique for advancing the capabilities of Large Language Models (LLMs), including in personal health informatics. There are growing efforts on benchmark creation for personal health data activities. However, it is unclear whether and how well these efforts align with needs and considerations of personal health informatics process. Addressing this need, we first analyzed 53,587 tasks across eight benchmarks related to personal health informatics and characterized the ...
  </details>

- **2026-11-10** — Basavaraj R M, Aryan Bharat Kumar — [Sanity Checks for Attention Surgery: Null Models and Matched Interventions for Representation-Motivated Design](http://arxiv.org/abs/2611.13543v1)
  <details><summary>📄 Abstract</summary>
  Transformer architectural modifications frequently measure a statistic on internal representations, observe that it is large, remove it architecturally, and report an improvement. Interpreting that sequence requires evaluating whether the statistic exceeds its noise floor, whether it survives a geometric null, and whether the training gain requires the specific direction removed. We formulate these requirements as three reusable checks and apply them to self-attention removal, which deletes the ...
  </details>

- **2026-11-10** — Evan Pačes-Wiles, Bryen Alvarez, Sara Gulabani et al. — [EJAI: Judgment-Preserving Civic AI for Data Center Environmental Justice](http://arxiv.org/abs/2611.13525v1)
  <details><summary>📄 Abstract</summary>
  Communities in the United States and around the world are contesting data centers, the physical infrastructure of AI. These disputes pose environmental justice issues: residents must weigh unevenly distributed burdens using evidence scattered across metrics, corporate claims, policy documents, and public testimony. A formative study with 10 users showed that dashboards and single-agent AI can settle questions before people examine that evidence. Here we present EJAI, a source-grounded system tha...
  </details>

- **2026-11-10** — Chaeho Lee, Junyup Kim, Wansoo Kim et al. — [Leveraging Psychophysical Attentional Distribution for Gaze-Augmented Reward Modeling](http://arxiv.org/abs/2611.13477v1)
  <details><summary>📄 Abstract</summary>
  Integrating human feedback into language models has gained increasing attention as a means to align model outputs with human preferences, with Reinforcement Learning from Human Feedback (RLHF) serving as a prominent framework for preference-based alignment. Recent studies have incorporated eye-tracking (ET) data as an additional supervisory signal for reward model training, grounding reward learning in human reading behavior. Building on this approach, we extend prior fixation-centric models by ...
  </details>

- **2026-11-10** — Paulo Camara — [Inherited Weights: Measuring the Tokenization Premium and the Sovereignty Cost of Language Models for the Global South](http://arxiv.org/abs/2611.13441v1)
  <details><summary>📄 Abstract</summary>
  Most language models deployed outside the United States and China are fine-tuned descendants of a small number of pretrained families. We argue that fine-tuning leaves the decisive properties of a model inherited from its base: vocabulary, knowledge, cultural alignment, memorized data and license. We contribute (i) an updated, reproducible measurement of the tokenization premium across 31 languages and 7 tokenizers released in 2023-2024, on 27 articles of the Universal Declaration of Human Right...
  </details>

- **2026-11-10** — Moein Heidari, Alvin Kimbowa, Mahdi Tabatabaei et al. — [Prompt2Echo (P2Echo): Text-Prompted Multi-View Echocardiography Segmentation with One Model](http://arxiv.org/abs/2611.13425v1)
  <details><summary>📄 Abstract</summary>
  Automated segmentation in multi-view echocardiography is essential for comprehensive cardiac assessment, yet remains challenging due to substantial anatomical and appearance variability across standard acoustic windows. In this paper, we present P2Echo, a unified framework capable of segmenting diverse cardiac structures across multiple standard echocardiographic views using a single model controlled by structured view-aware text prompts. Unlike recent foundation model adaptations that rely on i...
  </details>

- **2026-11-10** — Boyan Han, Xiaoyan Wang, Zhe Sun et al. — [AURA: Auditory Spatial Intelligence via a Unified Representation from a General-Audio Encoder through Complete Alignment](http://arxiv.org/abs/2611.13687v1)
  <details><summary>📄 Abstract</summary>
  Answering spatial questions about multi-source scenes requires a model both to identify each sound and to locate it. Existing spatial audio-language models obtain spatial information from a dedicated encoder, which separates spatial and semantic processing into distinct feature spaces. We study whether a general-audio codec trained without spatial supervision can serve both purposes. A controlled layer-wise analysis shows that the frozen codec retains spatial information, with lateral cues carri...
  </details>

- **2026-11-09** — Carina Jacobson, Aditya Purohit, Srikar Kovvali et al. — [TASCopilot: A provenance-preserving assistant for triple-axis neutron scattering](http://arxiv.org/abs/2611.13374v1)
  <details><summary>📄 Abstract</summary>
  Experimental decisions often depend on evidence scattered across papers, instrument logs, data files, and specialist software. A scientific assistant must connect that evidence without turning a plausible interpretation into an unsupported conclusion. TAS Co-pilot addresses this problem for triple-axis spectroscopy (TAS), which uses neutrons to probe material structure and excitations. It preserves provenance: the sources, processing steps, and review decisions behind each result. Independently ...
  </details>

- **2026-11-09** — Alexandros Hollender, Sonja Kraiczy — [Enforcing Axioms for AI Alignment under Loss-Based Rules](http://arxiv.org/abs/2611.13369v1)
  <details><summary>📄 Abstract</summary>
  Many alignment methods, most notably reinforcement learning from human feedback (RLHF), train reward models by minimizing a loss on pairwise comparisons of model responses. Inspired by principle-guided methods such as Constitutional AI, we treat each principle as a voter that compares responses according to that principle, for example, preferring the more helpful or less toxic response. We represent these voters as linear directions in a fixed embedding space, a simplifying assumption motivated ...
  </details>

- **2026-11-09** — Mufei Li, Nikki Lijing Kuang, Zhuoer Wang et al. — [Which Successes Make Good References? Action-Sequence Alignment for Multi-Turn On-Policy Distillation](http://arxiv.org/abs/2611.13135v1)
  <details><summary>📄 Abstract</summary>
  On-policy distillation (OPD) reduces train-inference distribution mismatch by supervising a student on its own trajectories. For multi-turn tool-use agents, conditioning the teacher on a validated same-task successful trajectory as a reference can provide useful hindsight, but different successes may reach incompatible interaction states and offer misleading supervision. We cast successful-reference selection as a free-target optimal transport problem, which reduces to assigning each failed traj...
  </details>

- **2026-11-09** — Seona Seo, Geonhee Ahn, Hyunsoo Cho et al. — [GRAP: Gender Rubric-Aware Probing for Analyzing Gender Bias in LLMs](http://arxiv.org/abs/2611.13024v1)
  <details><summary>📄 Abstract</summary>
  As LLMs increasingly mediate everyday interactions, subtle gender biases in open-ended responses pose growing societal risks. Existing probing methods have two key limitations: they rely on fixed-format tasks, such as pronoun resolution or occupation association, that alignment-tuned models can easily handle; and they compare raw group-level rubric scores, ignoring per-dimension variance and obscuring which bias dimensions reliably distinguish gender groups. We introduce GRAP (Gender Rubric-Awar...
  </details>

- **2026-11-09** — Francisco M. López, Francisco Cruz — [Can Hindsight Critics Guide Delayed Actors?](http://arxiv.org/abs/2611.11863v2)
  <details><summary>📄 Abstract</summary>
  Sensory delays create temporal misalignments between the state of the environment and the observations available to an agent, turning Markovian control problems into partially observable ones. In this work, we inquire whether such misalignments can be mitigated during training by using hindsight to recover aligned state-action transitions. We introduce Hindsight Critics, an asymmetric extension of the Soft Actor-Critic for reinforcement learning under partial observability. The critics are train...
  </details>

- **2026-11-09** — Huixuan Zhang, Li Lin, Junzhe Zhang et al. — [Direct Trajectory Optimization for Inference-Time Alignment of Text-to-Image Diffusion Models](http://arxiv.org/abs/2611.11821v2)
  <details><summary>📄 Abstract</summary>
  Alignment of text-to-image diffusion models with reward functions is a key challenge in controllable generation. Existing approaches typically rely on optimizing model inputs or fine-tuning denoising networks, which requires computationally expensive backpropagation through large denoising models. In this work, we propose Direct Trajectory Optimization (DTO), a training-free framework that performs alignment by directly optimizing the sampling trajectory of diffusion models. Specifically, DTO tr...
  </details>

- **2026-11-09** — Haozhi Yuan, Handong Li, Yifan Zhang et al. — [Reframe: Observation-Aligned Multi-Teacher On-Policy Distillation for Agentic Visual Reasoning](http://arxiv.org/abs/2611.12886v1)
  <details><summary>📄 Abstract</summary>
  Agentic reinforcement learning (RL) and multi-teacher on-policy distillation (MOPD) offer complementary routes to post-training. For visual agents, however, tool use presents two related challenges. Models may overlook useful tool-returned observations, while poorly grounded actions can limit the evidence available for subsequent distillation. We introduce Reframe, a post-training framework that treats the observation state, rather than only the output distribution, as an object of alignment. Fi...
  </details>

- **2026-11-09** — Julia Herbst, Simon Roschmann, Quentin Bouniot et al. — [Where Does Alignment Emerge and What Does It Mean? A Closer Look at the Platonic Representation Hypothesis](http://arxiv.org/abs/2611.12869v1)
  <details><summary>📄 Abstract</summary>
  The Platonic Representation Hypothesis (PRH) suggests that neural networks are converging toward similar representation spaces. As language models become more capable, their representations are aligning with those of vision models. However, recent work has questioned whether this trend continues to hold for newer language models. Moreover, it has been shown that representation similarity metrics can be confounded by model depth and width, requiring appropriate baselines for interpretation. In th...
  </details>

- **2026-11-09** — Xinjie Shen — [Shortcuts and Boundaries: Verifiable RL Misalignment and Contextual Safety Learning](http://arxiv.org/abs/2611.12865v1)
  <details><summary>📄 Abstract</summary>
  Reinforcement learning (RL) can improve an agent's task capability while reinforcing behavior that violates contextual execution requirements. We study this reward-driven misalignment, including reward hacking, through verifiable reward--context conflicts, where compliant task completion remains feasible while some executable shortcuts earn more reward than every compliant strategy. Encoding these conflicts in task dynamics lets us generate diverse interactive environments at scale and derive co...
  </details>

- **2026-11-09** — Olina Mukherjee, Arnav Goel, Aditi Raghunathan et al. — [Is Persona Generalization Predictable?](http://arxiv.org/abs/2611.12864v1)
  <details><summary>📄 Abstract</summary>
  Persona generalization occurs when fine-tuning a language model in one domain induces behavioral changes in others -- for example, the broadly unsafe behavior observed in emergent misalignment. We discover a surprising "on-the-line" phenomenon in persona generalization: in-domain and out-of-domain persona rates across various fine-tuning hyperparameters follow an approximately probit-linear relationship, and the specific probit-linear relationship is surprisingly shared even across model familie...
  </details>

- **2026-11-09** — Aarya Bhave, Anushka Ajay Bhave — [2D Gum-Net: Unsupervised Dense Elastic Image Registration via Symmetric Correlation and Spectral Pooling](http://arxiv.org/abs/2611.12805v1)
  <details><summary>📄 Abstract</summary>
  Dense non-rigid registration, the recovery of a pixel-wise deformation field that warps one image into geometric agreement with another, is fundamental across medical imaging, structural biology, and correspondence estimation, yet learning-based approaches face a severe bottleneck: ground-truth deformation fields are notoriously difficult to obtain for real data. We present 2D Gum-Net, an end-to-end architecture that predicts dense elastic deformation fields fully unsupervised. We transfer the G...
  </details>

- **2026-11-09** — Ding Zhu, Xiukun Wei, Tian Xie et al. — [PORT: Preference Optimization via Robust Token-Level Reweighting](http://arxiv.org/abs/2611.12763v1)
  <details><summary>📄 Abstract</summary>
  Preference optimization has become a central approach for aligning large language models with human values, but its effectiveness depends heavily on the quality of preference annotations. In practice, preference data is often noisy due to annotation errors and ambiguity. Existing robust preference optimization methods primarily operate at the sequence level, implicitly treating entire responses as uniformly correct or incorrect. However, rejected responses may still contain informative reasoning...
  </details>

- **2026-11-09** — Xindi Wang, Aifen Xiong, Baiyang Wang et al. — [Path-Level Structural and Semantic Alignment for Hierarchical Multi-Label Text Classification](http://arxiv.org/abs/2611.12420v1)
  <details><summary>📄 Abstract</summary>
  Hierarchical multi-label text classification (HMTC) requires models to capture both structural dependencies among labels and the fine-grained semantics of labels at different hierarchy levels. Existing methods often model hierarchy through prediction constraints or representations of individual labels and local relations. Structural and semantic supervision, however, are usually formulated separately. We instead use complete root-to-node label paths as a shared unit for both. Our framework intro...
  </details>

- **2026-11-09** — Provat Saha, Ashika Habib Khan, Tahseen Tanha et al. — [BDBBQ: A Human-AI Collaborative Benchmark for Bengali Social Bias in LLMs](http://arxiv.org/abs/2611.12407v1)
  <details><summary>📄 Abstract</summary>
  Despite growing attention to social bias in large language models (LLMs), existing bias benchmarks provide limited coverage of culturally grounded evaluation in Bengali, particularly within Bangladesh's sociocultural context. To address this gap, we develop a bilingual extension of BanglaBBQ comprising 61,312 question-answering instances across 12 social categories in English and Bengali. The benchmark incorporates balanced answer permutations, contrasting question framings, and both ambiguous a...
  </details>

- **2026-11-09** — Ruofan Wang, Puzuo Wang, Xin Chen et al. — [TMT: Adapting CLIP to Infrared Imagery via Text-Derived Modality Knowledge Transfer](http://arxiv.org/abs/2611.12345v1)
  <details><summary>📄 Abstract</summary>
  Vision-language models such as CLIP achieve strong performance across computer vision tasks, yet their image-text alignment is less reliable for infrared (IR) imagery because large-scale pre-training is dominated by visible-spectrum data. Due to the high cost of the infrared-text labeling, we investigate adapting CLIP to IR through only paired infrared-visible images, which requires considering modality-specific knowledge while preserving scene content and CLIP's image-text alignment. To achieve...
  </details>

- **2026-11-09** — Cheng Luo, Jian Zhu, Zhoujian Sun et al. — [Representational Alignment between Deep Neural Networks and Human Brain in Speech Processing under Audiovisual Noise](http://arxiv.org/abs/2611.12291v1)
  <details><summary>📄 Abstract</summary>
  Speech comprehension in the human brain is an incremental process that begins with acoustic processing and advances to linguistic processing. While recent studies have revealed that the hierarchy of deep neural networks (DNNs) correlates with the ascending auditory pathway, the exact nature of this DNN-brain alignment remains underexplored. In this study, we investigate how DNN representations align with the brain's acoustic-to-linguistic processing. Specifically, we employed neural encoding mod...
  </details>

- **2026-11-09** — Shijun Xiao, Zonghui Yang, Xinrong Chen et al. — [LiveWorkspace: Externalizing Visual Understanding as Persistent Shared State for Screenshot-to-Code Agents](http://arxiv.org/abs/2611.12112v1)
  <details><summary>📄 Abstract</summary>
  Screenshot-to-Code requires coding agents to sustain visual understanding across code generation, execution, and revision. We introduce LiveWorkspace, a visual coding harness that externalizes this understanding as Shared Visual State (Shared VS), an implementation-independent representation of visual hierarchy, node attributes, and layout relations. LiveWorkspace constructs and retains \textit{Target} from screenshots and recovers \textit{Current} from browser execution in the same schema. Stru...
  </details>

- **2026-11-09** — Kaiwen Zheng, Srijan Srivastava, Zheng Yan et al. — [Toward Verifiable Auto-Research for Data Systems](http://arxiv.org/abs/2611.12063v1)
  <details><summary>📄 Abstract</summary>
  AI auto-research is poised to forge bespoke data systems, from key-value stores and indexes to query engines, each engineered for a specific workload and hardware platform. Yet this promise rests on fragile ground. An agent optimizes what it can measure, not necessarily what users need. Natural-language requirements leave ample room for specification gaming, producing systems that blaze through benchmarks while silently losing updates or violating consistency. Worse, each research iteration cons...
  </details>

- **2026-11-09** — Taemin Cho, Hector Martel, Enyan Koh — [BARS: Beat-Adaptive Rap Synthesis via Flow Matching](http://arxiv.org/abs/2611.12061v1)
  <details><summary>📄 Abstract</summary>
  We present BARS (Beat-Adaptive Rap Synthesis), a non-autoregressive rapping voice generation model based on Flow Matching, conditioned on a beat track (instrumental backing), lyrics, and a short reference voice for zero-shot timbre control. Unlike prior autoregressive rap synthesis, where rap pace and output duration are strictly determined by the beat, BARS enables independent control over the rap tempo, allowing flexible-length generation without explicit duration prediction or phoneme-level a...
  </details>

- **2026-11-09** — Guglielmo Padula, Antonio Colanera, Gianluigi Rozza — [Parametric spatio-temporal reduced-order modelling via Spectral Proper Orthogonal Decomposition and Gaussian Process Regression](http://arxiv.org/abs/2611.12028v1)
  <details><summary>📄 Abstract</summary>
  We present SPOD-GPR, a non-intrusive, parametric, spatio-temporal reduced-order model (ROM) that combines Proper Orthogonal Decomposition (POD), Spectral POD (SPOD), and Gaussian Process Regression (GPR). A parametric POD first projects the high-dimensional state onto a low-dimensional subspace. The reduced trajectories are then divided into windowed sections, transformed into the frequency domain, and truncated to the most energetic frequencies. SPOD is then performed independently at each reta...
  </details>

- **2026-11-09** — Zhefan Wang, Da Li, Keping Bi et al. — [Multi-Modal Agricultural Document Understanding at the DAGRI Task](http://arxiv.org/abs/2611.11886v1)
  <details><summary>📄 Abstract</summary>
  Agricultural documents, such as prefectural technical reports and crop calendars, are critical knowledge resources. However, their complex table layouts, significant variations in document length, and dense multi-modal elements pose substantial challenges for automated understanding. To address these issues, the NTCIR-19 DAGRI (Data Analytics for aGRicultural Information) task introduced three subtasks focusing on different dimensions of document intelligence. In the Table Information Extraction...
  </details>

- **2026-11-09** — Francisco M. López, Francisco Cruz — [Can Hindsight Critics Guide Delayed Actors?](http://arxiv.org/abs/2611.11863v1)
  <details><summary>📄 Abstract</summary>
  Sensory delays create temporal misalignments between the state of the environment and the observations available to an agent, turning Markovian control problems into partially observable ones. In this work, we inquire whether such misalignments can be mitigated during training by using hindsight to recover aligned state-action transitions. We introduce Hindsight Critics, an asymmetric extension of the Soft Actor-Critic for reinforcement learning under partial observability. The critics are train...
  </details>

- **2026-11-09** — Huixuan Zhang, Xiaojun Wan — [Direct Trajectory Optimization for Inference-Time Alignment of Text-to-Image Diffusion Models](http://arxiv.org/abs/2611.11821v1)
  <details><summary>📄 Abstract</summary>
  Alignment of text-to-image diffusion models with reward functions is a key challenge in controllable generation. Existing approaches typically rely on optimizing model inputs or fine-tuning denoising networks, which requires computationally expensive backpropagation through large denoising models. In this work, we propose Direct Trajectory Optimization (DTO), a training-free framework that performs alignment by directly optimizing the sampling trajectory of diffusion models. Specifically, DTO tr...
  </details>

- **2026-11-09** — Sumin Jo, Edward Choi — [HiddenPathQA: A Benchmark for Knowledge Graph Question Answering When Questions Hide Their Paths](http://arxiv.org/abs/2611.11802v1)
  <details><summary>📄 Abstract</summary>
  Knowledge graph question answering (KGQA) systems are typically evaluated on questions whose surface tokens lexically expose the gold KG path. Users, however, may ask questions without knowing the underlying schema: "Which condition could Andrew have due to family history?" compresses a 4-hop chain "Andrew --[father]--> parent --[father]--> grandparent --[medical condition]--> disease --[subclass of]--> hereditary disorder" into a single phrase (family history) that names none of those relations...
  </details>

- **2026-11-09** — Yiqun T. Chen, Jan Matthias, Jianing Yao et al. — [Publications as benchmarks: auditing AI agents on spatial transcriptomics alignment](http://arxiv.org/abs/2611.11796v1)
  <details><summary>📄 Abstract</summary>
  AI agents are increasingly automating data analysis, but responsible adoption requires reliable performance evaluation, which is costly in specialized scientific domains. We introduce a framework that translates scientific publications into auditable benchmarks for AI agents and demonstrate its use on spatial transcriptomics alignment tasks. Across 121 tasks, 16 baseline methods, and six AI agents, the best agents (GPT-6-Astra and Gemini-4-Argon) matched or outperformed all baselines on 80% of t...
  </details>

- **2026-11-09** — Khurram Khalil, Khaza Anuarul Hoque — [Spectral Rank and Step-Direction Dynamics in Language-Model Post-Training](http://arxiv.org/abs/2611.11752v1)
  <details><summary>📄 Abstract</summary>
  Language-model post-training modifies weights through cumulative updates and successive displacements, yet existing studies report seemingly conflicting spectral properties: nearly full-rank updates and low stable-rank changes. We show these observations are compatible and characterize update directions during training. For singular values following $σ_i \propto i^{-α}$ with $0 < α\leq 1/2$, we prove that stable rank becomes negligible relative to fixed-energy rank as dimension increases. Full s...
  </details>

- **2026-11-09** — Pengyu Yin, Jie Pan, Junxiang Tan et al. — [GeoPilot: Diagnosis-Guided Interventions and Geometric Evaluation for Aerial Reconstruction](http://arxiv.org/abs/2611.11751v1)
  <details><summary>📄 Abstract</summary>
  When a mesh reconstructed from aerial remote-sensing imagery disagrees with reference geometry, deciding what to change requires a diagnosis of the reconstruction process. We present GeoPilot, a workflow that turns diagnostics and prior observations into executable program or camera-configuration interventions. A large language model proposes the change, numerical tools reconstruct the mesh, and an external evaluator measures its geometry under a stated coordinate and reference protocol. The mai...
  </details>

- **2026-11-09** — Kiavash Fathi, Hans Wernher van de Venn — [CRAFT-AI: Capability and Requirement Alignment for Flexible Manufacturing through Agentic AI](http://arxiv.org/abs/2611.12092v1)
  <details><summary>📄 Abstract</summary>
  One of the fundamental needs for reaching resilient production infrastructure is flexible manufacturing, which requires translating changing production requirements into implementable system configurations. This paper introduces \textbf{CRAFT-AI}, an agentic AI approach combining natural language (NL) requirement interpretation, Asset Administration Shell (AAS)-based capability descriptions, and reusable engineering knowledge from existing manufacturing configurations. A tool-using AI agent matc...
  </details>

- **2026-11-09** — Edoardo Chidichimo — [Explaining and interrupting collective misalignment in language model systems](http://arxiv.org/abs/2611.11724v1)
  <details><summary>📄 Abstract</summary>
  In collectives, language model agents can exchange individually innocuous messages that together support a policy violation. Understanding and preventing collective misalignment requires answering the question of which messages sufficiently influenced and necessarily enabled the violation. Collective Dependence Analysis (CDA) operationalises necessity and sufficiency to explain decisions and find the fewest removals interrupting support within tested combinations. Tests covered constructed viola...
  </details>

- **2026-11-08** — Anay Loya, Rishi Gupta, Arnav Samal et al. — [SurfScaff3D: Bridging Geometric and Semantic Representations for LLM-based 3D Object Generation](http://arxiv.org/abs/2611.11678v1)
  <details><summary>📄 Abstract</summary>
  Creating high-quality 3D content has traditionally required specialist expertise and experience with complex tools. The growing ecosystem of AI-assisted creativity demands accessible and intuitive 3D generation systems. Recent advances in Large Language Models (LLMs) offer promising directions, yet extending their generative capabilities to 3D remains fundamentally challenging because existing 3D representations are not naturally compatible with language-based reasoning. Current approaches eithe...
  </details>

- **2026-11-08** —  InfraRSI Team, Yuchuan Tian, Haocheng Mei et al. — [InfraRSI: Harnessing Recursive Self-Improvement for Training Infrastructure](http://arxiv.org/abs/2611.11558v1)
  <details><summary>📄 Abstract</summary>
  While Recursive Self-Improvement (RSI) accelerates isolated algorithm and kernel synthesis, distributed LLM training depends on tightly coupled launch settings, operator kernels, and communication schedules, where single edits often hit out-of-memory (OOM) boundaries, compiler conflicts, measurement jitter, or silent numerical drift. We present InfraRSI, the agentic harness that turns open-ended human commands into verified training optimizations via a five-stage workflow: init locks editable sc...
  </details>

- **2026-11-08** — Pramath Girish Haritz, Chandra Sekhar Seelamantula — [Dropping Tokens Without Dropping Them: Causal Attribution for Diabetic Retinopathy](http://arxiv.org/abs/2611.11547v1)
  <details><summary>📄 Abstract</summary>
  In this work, we investigate whether attention-based attribution maps in a vision transformer provide causal explanations for diabetic retinopathy (DR) classification. We introduce a principled decomposition of attention into two attribution maps: the contribution ($c_t$), which satisfies the completeness axiom in explainable artificial intelligence (xAI), and the pull ($p_t$), which quantifies causal explanations. We define an identity relating $c_t$ and $p_t$ that characterizes when $c_t$ fail...
  </details>

- **2026-11-08** — Siming Zhang, Zhehui Shen, Shijie Chen et al. — [Boundary Mass in Feature Space as a Label-Budget Diagnostic for Representations](http://arxiv.org/abs/2611.11525v1)
  <details><summary>📄 Abstract</summary>
  Low-label transfer is often decided by a practical question: after a representation looks useful, how many labels are still needed to learn the downstream boundary? Transferability and probe-quality scores characterize global alignment, likelihood, margins, and calibration. Boundary-near target mass complements these diagnostics by measuring the ambiguous regions where scarce labels are most costly. We propose effective boundary complexity, a label-budget diagnostic for frozen representations an...
  </details>

- **2026-11-08** — Vitus Benson, Fanny Yang, Markus Reichstein — [Decomposing Earth Embeddings with Sparse Autoencoders](http://arxiv.org/abs/2611.11398v1)
  <details><summary>📄 Abstract</summary>
  Earth observation foundation models produce global metre-resolution embeddings that underpin work across agriculture, ecology, hydrology, and beyond. Yet these embeddings are opaque: each dimension entangles unrelated physical concepts, which makes them difficult to interpret and their robustness hard to assess. Here, we propose sparse autoencoders (SAEs) as a principled way to decompose Earth embeddings into sparse, approximately monosemantic features over an overcomplete dictionary. Because LL...
  </details>

- **2026-11-08** — Suxin Ji, Hungtao Wan — [TLRS-DPO: Token-Level Risk Scoring for Better Direct Preference Optimization](http://arxiv.org/abs/2611.11232v1)
  <details><summary>📄 Abstract</summary>
  Direct Preference Optimization (DPO) is a simple and widely used alternative to RLHF for aligning large language models (LLMs), but its sequence-level objective cannot precisely locate or suppress the local patterns that make an otherwise acceptable response unsafe or undesirable. We propose TLRS-DPO (Token-Level Risk Scoring for Better Direct Preference Optimization), which augments DPO with fine-grained token-level control while remaining fully offline and reference-based. TLRS-DPO introduces ...
  </details>

- **2026-11-08** — You Liu, Quanchao Lu — [Replay Fidelity in LLM Agent Evaluation: Randomness, Hidden State, and Test Oracles in AppWorld](http://arxiv.org/abs/2611.11216v1)
  <details><summary>📄 Abstract</summary>
  Reproducibility in large language model (LLM) agent evaluation depends on replay fidelity: which parts of an execution trace are reconstructed, controlled, and compared. This matters for agent debugging, failure analysis, and counterfactual evaluation of stateful tool use. We audit all 71 unsuccessful executions in a fixed historical AppWorld corpus using 284 isolated fixed-code replay attempts. Reconstructed declared settings admit 42 cases under printed-output, pre-oracle database-delta, and n...
  </details>

- **2026-11-08** — Nairouz Mrabah, Ismail Ben Ayed, Eric Granger — [Full Fine-Tuning is not the Problem: Why Adam Fails and SGD Succeeds in Few-Shot CLIP Adaptation](http://arxiv.org/abs/2611.11152v1)
  <details><summary>📄 Abstract</summary>
  Few-shot CLIP adaptation is often treated as a parameterization problem. Full fine-tuning is assumed to overfit, so parameter-efficient fine-tuning (PEFT) methods are preferred. In this paper, we show that this conclusion conflates parameterization with optimization. Across 11 datasets, 3 CLIP backbones, and 5 shot levels, dense full fine-tuning with plain SGD outperforms representative PEFT methods under the reported evaluation protocol, whereas Adam/AdamW collapses. We trace this collapse to u...
  </details>

- **2026-11-07** — Sudhanshu Srivastava, Faisal Aqlan — [Beating the Pool, Not the Game: A White-Box Equilibrium Agent for Language-Based Economic Games](http://arxiv.org/abs/2611.10932v1)
  <details><summary>📄 Abstract</summary>
  We describe sudsho, a rule-based agent for the GLEE Competition that plays bargaining, negotiation, and persuasion with zero inference-time LLM calls. Games are scored as payoff percentiles against an empirical pool of prior play on the same configuration, so pool percentiles set our demand targets while clamped equilibrium shares bound demands and acceptance. Every move is a deterministic function of the visible state (persuasion mixing aside), so alignment is verified by replaying the post-fre...
  </details>

- **2026-11-07** — Xunlan Zhou, Yuzhe Zhao, Xuhong Huang et al. — [BRAT: Bounded Residual-Aligned Training for Stable Multi-Pass LLM Post-Training](http://arxiv.org/abs/2611.10873v1)
  <details><summary>📄 Abstract</summary>
  Reinforcement learning for large language model post-training often reuses each batch of sampled rollouts for several gradient passes to amortize the cost of generation. Under such multi-pass reuse, existing objectives fail in different ways: unclipped updates collapse as the policy drifts away from the sampling policy, adding a negative baseline avoids collapse but reinforces every sampled response, and PPO-style ratio clipping cuts off gradients abruptly. We first ask why reuse is fragile. Mea...
  </details>

- **2026-11-07** — Qisai Liu, Zhanhong Jiang, Zahid Hasan et al. — [Proximal Preference Optimization: A Unified Framework for Stable and Reward-Free Alignment](http://arxiv.org/abs/2611.10785v1)
  <details><summary>📄 Abstract</summary>
  We introduce a proximal preference optimization framework that unifies the implicit reward formulation of Direct Preference Optimization (DPO) with the trust-region stability of Proximal Policy Optimization (PPO). Our framework yields two complementary algorithms. P$^2$O (Proximal Preference Optimization) introduces a clipped importance ratio directly into the DPO preference margin, producing a reward-model-free algorithm that supports safe dataset reuse, bounded policy divergence, and monotonic...
  </details>

- **2026-11-07** — Shrey Singhal, Nannan Huang, Haytham M. Fayek — [AERO: Adaptive Ensemble-Disagreement Routing for Oracle Feedback in Sample-Efficient Online RLHF](http://arxiv.org/abs/2611.10750v1)
  <details><summary>📄 Abstract</summary>
  Aligning Large Language Models (LLMs) with human preferences via Reinforcement Learning from Human Feedback (RLHF) has driven substantial improvements across a wide range of tasks, but the cost of acquiring preference labels remains the dominant bottleneck in the alignment pipeline. While many recent alignment methods improve sample efficiency through active exploration over candidate responses, they typically query the oracle uniformly across contexts, even for contexts where the learned reward...
  </details>

- **2026-11-06** — Anthony Rhodes, Gadi Singer — [BMMS: Policy-Conditioned Measurement of Behavioral Compliance in Language Models](http://arxiv.org/abs/2611.09147v1)
  <details><summary>📄 Abstract</summary>
  Behavioral evaluation of language models fixes its dimensions in advance: hallucination, sycophancy, toxicity, over-refusal. An operator in a regulated industry needs a different question answered: does a system do what a particular rulebook requires? We introduce the Behavioral Misalignment Metric Suite (BMMS), which measures policy-conditioned misalignment by taking a policy corpus as an argument and returning a compliance profile over it, for any published policy and any system that answers i...
  </details>


### 📂 robustness
*鲁棒性与可靠性 / Robustness & Reliability* — 56 papers

- **2026-11-10** — Mario Chacón-Falcón, Tatiana Valentine Guy, Miroslav Kárný et al. — [Adversarial risk analysis with fully probabilistic designs](http://arxiv.org/abs/2611.14289v1)
  <details><summary>📄 Abstract</summary>
  Adversarial risk analysis (ARA) informs decision-makers when facing intelligent opponents and uncertain outcomes, enabling an analyst to model beliefs about the opponents' preferences, capabilities, beliefs, and the strategic calculations that opponents employ. Major applications cover reliability and risk analysis of critical infrastructures in presence of adversarial threats. In such domains, ARA mitigates typical common knowledge assumptions of standard game-theoretic approaches. However, ARA...
  </details>

- **2026-11-10** — Ziqing Xu, Hancheng Min, Lachlan Ewen MacDonald et al. — [A Margin Perspective on LoRA: Robustness to Catastrophic Forgetting and Adapter Merging (MaLoRA)](http://arxiv.org/abs/2611.14397v1)
  <details><summary>📄 Abstract</summary>
  Low-rank adaptation (LoRA) is the de facto method for parameter-efficient fine-tuning of large neural networks, achieving strong task adaptation with minimal trainable parameters and low optimization cost. Beyond this efficiency, practitioners have observed two striking properties: \textit{robustness to catastrophic forgetting} and the ability to \textit{merge independently trained adapters} into a single model that performs competitively across multiple tasks. These properties are central to co...
  </details>

- **2026-11-10** — Rezwan Islam Salvi, Saiyma Sittul Muna, Mushfiqur Rahman Mushfique — [HandsOnAid: Building and Evaluating an Offline First-Aid Assistant for Emergency Response Scenarios](http://arxiv.org/abs/2611.14059v1)
  <details><summary>📄 Abstract</summary>
  Emergencies can occur where there is no phone signal and no ambulance nearby. A small language model on a phone can be helpful in such situations, but its advice needs to be safe and accurate. We built HandsOnAid, a 4-bit Gemma 2B model fine-tuned with QLoRA on FirstAidQA dataset, a corpus of 5,550 first-aid question-answer pairs. We compared seven configurations, including the base, 4-bit and 8-bit fine-tuned models, and versions with a length floor, safety gate, or retrieval. We used a 41-pair...
  </details>

- **2026-11-10** — Sandarbh Agrawal, Rakshith Sathish, Ashwathi Nambiar — [Satellite Pretraining Is Not One Thing: A Matched-Pair Study of Generic and Earth-Observation Foundation Models for Scene Classification](http://arxiv.org/abs/2611.13849v1)
  <details><summary>📄 Abstract</summary>
  Geospatial foundation models are pretrained on satellite and aerial imagery, but whether such an encoder beats a strong generic one for few-label land-use/land-cover mapping remains unclear, as prior comparisons rarely isolate the pretraining data. We study five matched pairs of Earth-observation (EO) and generic encoders sharing objective and architecture (DINO/SatDINO, DINOv3/DINOv3-SAT, MAE/SatMAE, MAE/Scale-MAE, CLIP/RemoteCLIP) within a benchmark of 14 frozen encoders on five RGB scene-clas...
  </details>

- **2026-11-10** — Jianqiang Wang, Tengfei Liu, Zhong-Ping Jiang — [Input-to-State Safety and Small-Gain Theorems for Large-Scale Nonlinear Systems](http://arxiv.org/abs/2611.13718v1)
  <details><summary>📄 Abstract</summary>
  This paper studies the safety verification problem for a general class of large-scale systems characterized by multiple safety indicator functions. Each safety indicator function satisfies a trajectory-based input-to-state safety (ISSf) estimate that provides a lower bound on its value along system trajectories in terms of the initial state, external inputs, and the other safety indicator functions, whose influence is quantified by continuous and nondecreasing gain functions. Within this framewo...
  </details>

- **2026-11-10** — Qinan Zhang, Xinyu Wang, Qihang Jin et al. — [Towards Reliable VLM Judges: State-Conditional Invariance and Presentation-Aware Diagnostics](http://arxiv.org/abs/2611.13596v1)
  <details><summary>📄 Abstract</summary>
  Vision-language models (VLMs) are increasingly used as automated judges for multimodal and embodied tasks, yet aggregate accuracy or consistency alone does not reveal whether a judge changes its verdict for the right reason. We propose State-Conditional Invariance (SCI), a reliability principle requiring a judge to remain stable under semantics-preserving changes in presentation while responding to causal interventions that change the task outcome. We instantiate SCI in GridWM-Judge, a simulator...
  </details>

- **2026-11-10** — Sina Mohammadi, Apurv Shukla, Junho Hong et al. — [An Accurate Modulation-Assisted Method for Phasor Estimation Under Decaying DC Offsets](http://arxiv.org/abs/2611.13558v1)
  <details><summary>📄 Abstract</summary>
  Decaying DC (DDC) offsets severely compromise the accurate estimation of current phasors immediately following power grid fault occurrence. Consequently, conventional full-cycle discrete Fourier transform (FCDFT) algorithms experience decaying oscillatory magnitude errors, potentially causing distance relays to malfunction. This paper introduces a modulation-assisted technique designed to precisely eliminate the DDC components from fault current signals. By multiplying the fault signal with a hi...
  </details>

- **2026-11-10** — Siddhartha Chatterjee — [Darmok: Championship Cryptic Crossword Solving via Constraint Tightening and Resilient Orchestration](http://arxiv.org/abs/2611.13557v1)
  <details><summary>📄 Abstract</summary>
  We present Darmok, the first automated system to reach superhuman performance on British cryptic crosswords. Unlike American-style crosswords, cryptic clues disguise an unmarked definition and compositional wordplay beneath a misleading surface reading, sparse grids leave nearly half of each word's letters unchecked, and tournament rules rank a grid with even a single wrong or blank square behind all error-free solutions regardless of speed. Competing alongside an elite human field at the 55th T...
  </details>

- **2026-11-10** — Xuheng Zhang, Yiming Zhang, Jialin Gao et al. — [LaST0.5: A Generalist World Action Model with Interaction-Centric Latent Reasoning](http://arxiv.org/abs/2611.14048v1)
  <details><summary>📄 Abstract</summary>
  World Action Models (WAMs) have recently emerged as a promising paradigm for robotic manipulation, endowing policies with strong capabilities for modeling temporal and physical dynamics. Existing WAMs, encompassing both video-first action prediction and joint video-action modeling, directly transfer global physical representations from world models to action generation. However, global scene representations may underemphasize local robot-object interactions, creating a mismatch between represent...
  </details>

- **2026-11-10** — Martim Afonso, Inês Lynce, Maurizio Morisio et al. — [ProofCoder: Continuous Reasoning for Automated Software Verification](http://arxiv.org/abs/2611.14106v1)
  <details><summary>📄 Abstract</summary>
  Formal verification using proof assistants provides strong correctness guarantees for software, but constructing proofs remains labor-intensive and requires significant expertise. Recent approaches based on large language models (LLMs) have shown promise in automating proof synthesis. However, these approaches typically constrain the model to a rigid tactic-generation loop, in which the surrounding system controls premise retrieval, proof-state management, and backtracking. We introduce ProofCod...
  </details>

- **2026-11-10** — Zehui Wang, Wolfram Höpken, Dietmar Jannach — [Data Quality Challenges in Multimodal Tourism Recommender Systems](http://arxiv.org/abs/2611.13972v1)
  <details><summary>📄 Abstract</summary>
  Modern recommender systems increasingly consider diverse data modalities to enhance model performance. However, the quality of the underlying multimodal data (e.g. data from social media platforms) has received limited attention so far. Focusing on tourism recommendation, we examine real-world challenges encountered when using datasets from Yelp and Instagram. Issues include noise from fake reviews, hallucinated content from LLMs, modality contradictions, and demographic bias. We outline future ...
  </details>

- **2026-11-10** — Stefan van Dijk, W. P. M. H. Heemels, Paula Chanfreut Palacio — [Online Adaptive Clustering in Robust Distributed Model Predictive Control](http://arxiv.org/abs/2611.13923v1)
  <details><summary>📄 Abstract</summary>
  This paper proposes a dynamic clustering framework for tube-based model predictive control (MPC) of coupled multi-agent systems. Agents within a cluster coordinate their dynamics explicitly, while couplings from agents outside the cluster are treated as bounded disturbances. For each admissible cluster, we construct a state-dependent mismatch measure from a robust upper bound on its predicted closed-loop cost and an optimistic, partition-independent lower bound. Combining this mismatch with a co...
  </details>

- **2026-11-10** — Ruohan Wang, Giannis Delimpaltadakis, Luca Laurenti et al. — [Efficient control of multi-agent robust MDPs through tensor trees](http://arxiv.org/abs/2611.13672v1)
  <details><summary>📄 Abstract</summary>
  This paper introduces a tensor-based framework for controller synthesis of stochastic multi-agent systems under temporal logic specifications that couple the agents, such as one agent reaching its goal only after another agent has reached its own. The agents are modeled as robust Markov decision processes (RMDPs), whose transition probabilities are only known to lie in an ambiguity set, for instance due to abstraction errors, learned models, or uncertain parameters. We show that the decoupled na...
  </details>

- **2026-11-10** — Bowen Deng, Gwang-Jin Jeong, Seulgi Noh et al. — [Lightweight Deep Learning Framework for Astrocyte-Centric 3D Reconstruction across Normal and Stress-associated Ultrastructural States](http://arxiv.org/abs/2611.13581v1)
  <details><summary>📄 Abstract</summary>
  The morphology of astrocytes is closely associated with their ability to support and modulate neural circuit functions; however, its reconstruction from volume electron microscopy (vEM) data remains labor-intensive and computationally resource-intensive, placing substantial barriers on its broader adoption and scalability despite the high spatial resolution of vEM. We present AstroSeg-vEM, a lightweight, astrocyte-centric framework for morphology-preserving astrocyte segmentation, 3D reconstruct...
  </details>

- **2026-11-10** — Hanyu Jin, Kenji Shimada — [DeRep: Learning Depth Representations for End-to-End Navigation in Cluttered Environments](http://arxiv.org/abs/2611.13499v1)
  <details><summary>📄 Abstract</summary>
  End-to-end navigation in cluttered environments relies on compact visual representations to support collision avoidance and goal-directed motion. Existing methods typically learn these representations jointly with the policy or through observation reconstruction, which does not explicitly specify what information the representation should preserve. Moreover, they are usually evaluated with a single downstream policy learner, although the benefit of a representation may depend on how the policy i...
  </details>

- **2026-11-10** — Mingchen Li, Yongkang Xiao, Rumeng Li et al. — [BioMem: Agentic Memory for Biomedical LLM Agents](http://arxiv.org/abs/2611.13426v1)
  <details><summary>📄 Abstract</summary>
  Large language models (LLMs) have demonstrated considerable potential in biomedical applications, while agentic memory systems have emerged as a promising approach to preserving and utilizing information across tasks and interactions. However, a fundamental question remains: how effectively and reliably do these systems retain, retrieve, update, and utilize biomedical information? In this study, we systematically investigate agentic memory in the biomedical domain, focusing on task effectiveness...
  </details>

- **2026-11-10** — Alireza Daghigh, Chung-Yu Wang, Luca Filippelli et al. — [SPARK: Semantic-preserving Prompt Mutation for Code Generation using Consensus-based Verification Framework](http://arxiv.org/abs/2611.13401v1)
  <details><summary>📄 Abstract</summary>
  Automated code generation with large language models (LLMs) has improved in recent years. With the lack of test cases in real-world usages, generated code is not automatically verifiable and often requires manual validation. Previous studies have leveraged consensus verification, where code solutions and corresponding test cases are generated and evaluated based on functional consistency. Building on this, SPARK incorporates semantic-preserving mutations to problem descriptions such as paraphras...
  </details>

- **2026-11-09** — Grigory Malinovsky, Yury Demidovich, Peter Richtárik — [Byzantine-Robust Muon: Resilient Momentum Orthogonalization for Distributed Learning](http://arxiv.org/abs/2611.13137v1)
  <details><summary>📄 Abstract</summary>
  Optimization methods, including the Muon optimizer based on the Linear Minimization Oracle (LMO) and momentum orthogonalization, have shown strong empirical performance in large-scale and distributed learning, yet their robustness to adversarial behavior and data heterogeneity is not well understood. We study these methods within a unified first-order trust-region framework and analyze Muon-based updates with robust aggregation for Byzantine-robust distributed and federated learning. Our analysi...
  </details>

- **2026-11-09** — Shu Jiang, Graham A. Colditz — [Do AI Agents need Preventive Care? An Epidemiologic Cohort Design for Agentic AI](http://arxiv.org/abs/2611.13333v1)
  <details><summary>📄 Abstract</summary>
  As AI agents increasingly perform tasks autonomously across sectors, including healthcare and biomedical research, understanding how their behaviors develop and influence outcomes over time becomes increasingly important. Existing evaluations largely focus on model capabilities and performance on predefined tasks. Here, we propose an epidemiologic cohort design for studying agentic AI, drawing on principles established in human population studies. The framework treats individual agents as member...
  </details>

- **2026-11-09** — Pedro Antonio Alarcon Granadeno, Jane Cleland-Huang — [DOBB: Dynamic Oriented Bounding Boxes for Multi-Agent Collision Avoidance under State Uncertainty and Heterogeneous Dynamics](http://arxiv.org/abs/2611.13142v1)
  <details><summary>📄 Abstract</summary>
  Learning-based decentralized collision avoidance must remain reliable under state-estimation uncertainty and heterogeneous agent dynamics. Existing methods typically address these factors through training-domain variation or by exposing uncertainty and capability estimates to the policy at runtime. However, both leave the policy to infer how these quantities should alter the physical separation required for safe interaction, which can couple collision-avoidance behavior to relationships learned ...
  </details>

- **2026-11-09** — Mahyar Bolhassani, Tijana Geroski, Narayana S. Singam et al. — [Domain adaptation of a video Foundation model for Heart Failure Diagnosis from Echocardiography](http://arxiv.org/abs/2611.13297v1)
  <details><summary>📄 Abstract</summary>
  The rapid advancement of foundation models has transformed computer vision, yet their adaptation to medical imaging, particularly purpose built foundation models for spatio temporal echocardiography videos, remains limited. In this work, we explore the feasibility of fine tuning a pretrained foundation model for video (TimeSformer) for automated diagnosis of reduced ejection fraction heart failure (HFrEF) from apical four chamber videos. The model is finetuned on the publicly available RVENet A4...
  </details>

- **2026-11-09** — Rayed AlGhamdi — [Reliability of Claude Code as an Agentic AI Grading System for Handwritten University Exams](http://arxiv.org/abs/2611.13217v1)
  <details><summary>📄 Abstract</summary>
  This study examines the reliability of Claude Code, an agentic deployment of the Claude Opus 4.6 large language model, as a grading system for handwritten university exams. Four research questions addressed agreement with expert human grading on total scores (RQ1), agreement across five question types from multiple choice to evaluative judgement (RQ2), consistency across two independent grading sessions one week apart (RQ3), and the accuracy of AI-generated feedback (RQ4). Claude Code graded the...
  </details>

- **2026-11-09** — Gabriel Sargent, Will Wei Sun, Zhengwu Zhang et al. — [Prediction-Powered LLM Ranking with Adaptively Collected Human Feedback](http://arxiv.org/abs/2611.13186v1)
  <details><summary>📄 Abstract</summary>
  Ranking large language models (LLMs) through human evaluations is essential for downstream decision-making. Because human feedback is expensive, evaluation platforms often collect it adaptively, prioritizing informative model comparisons using previously observed feedback. To further improve precision with limited human feedback, evaluators can draw on abundant unrated responses and relatively inexpensive LLM judges; however, judge bias and adaptive dependence challenge standard i.i.d. inference...
  </details>

- **2026-11-09** — Aviv Orly, Ori Shem-Ur, Yaron Oz — [One Temperature to Rule Them All?](http://arxiv.org/abs/2611.13077v1)
  <details><summary>📄 Abstract</summary>
  Inference-time sampling is a central mechanism for improving large language models, with temperature controlling the tradeoff between reliability and diversity. While recent work suggests that varying temperature across samples can improve multi-sample inference, simple fixed-temperature schemes remain the standard in practice. We investigate this discrepancy in the canonical pass@K setting, asking when temperature diversity is useful, and when a single tuned temperature suffices. To this end, w...
  </details>

- **2026-11-09** — Jens Parslov, Marco Schouten, Dim P. Papadopoulos — [EditJudge-Bench: Auditing VLM Image-Edit Judges with Synthetic Ground Truth](http://arxiv.org/abs/2611.12524v1)
  <details><summary>📄 Abstract</summary>
  Vision-language models (VLMs) are increasingly used as automated judges for image-editing benchmarks, yet their reliability is poorly understood. Auditing these judges is difficult because real edited images lack controlled ground truth and entangle the requested changes with model artefacts, unintended side effects, and ambiguous degrees of success. In this paper, we introduce EditJudge-Bench, a diagnostic benchmark of 1,382 synthetic before/after image pairs rendered in Blender, with edits par...
  </details>

- **2026-11-09** — Aviad Eisenberg, Sharon Gannot, Shlomo E. Chazan — [Textraction: Unified Text-Guided Speaker Extraction and Enhancement for Single- and Multi-Channel Audio](http://arxiv.org/abs/2611.12493v1)
  <details><summary>📄 Abstract</summary>
  We present Textraction, a text-guided speaker extraction framework that enables the selective extraction of desired speakers or noise sources from an audio mixture using only natural-language descriptions. The proposed method operates within a single unified model that supports both single-channel and multi-channel inputs and it allows conditioning on either semantic textual descriptions of the target source or on its spatial description. Dedicated single- and multi-channel encoders feed a share...
  </details>

- **2026-11-09** — Pekka Abrahamsson, Muhammad Waseem, Esa Karjalainen et al. — [Unprompted coordination through shared memory in LLM agents: a locked two-implementation replication and extension](http://arxiv.org/abs/2611.12412v1)
  <details><summary>📄 Abstract</summary>
  Coordination between large language-model agents has become a central question for AI safety and software engineering, as such agents are deployed in groups that share infrastructure. Existing research tells the agents that partners exist or asks them to coordinate. Whether coordination arises through shared state alone, with nothing disclosing that anyone else is present, is the key question for deployments that share caches and memory between agents, yet it has rarely been examined, and never ...
  </details>

- **2026-11-09** — Bui Trong Duc, Huynh Thi Thanh Binh — [BECON: Belief-Conditioned Constrained Multi-Objective Reinforcement Learning under Drifting Preferences and Budgets](http://arxiv.org/abs/2611.12053v1)
  <details><summary>📄 Abstract</summary>
  Constrained preference-conditioned MORL typically assumes full task observability, treating preferences and safety budgets as stationary task signals. In real-world deployment, however, these signals are often unreliable proxies: intent may drift, safety tolerances may shift with context, and exposed descriptors may be noisy, delayed, or incomplete. We therefore formulate constrained preference-conditioned MORL as a partially observed task-specification problem, where the agent must navigate a f...
  </details>

- **2026-11-09** — Yu Zhang, Ruijie Yu, Xuelin Zhao et al. — [Enhancing Multi-Step Chemical Mechanism Prediction with Graph-Guided Preference Data](http://arxiv.org/abs/2611.12013v1)
  <details><summary>📄 Abstract</summary>
  Predicting multi-step chemical reaction mechanisms requires identifying plausible intermediates and correctly ordering the elementary reaction steps. Existing computational methods focus on single-step elementary reaction prediction, limiting their ability to generalize to unseen reaction spaces. We introduce a graph-guided framework for multi-step chemical mechanism prediction that leverages a chemical mechanism knowledge graph (ChemMechKG) to guide large language models (LLMs). To improve path...
  </details>

- **2026-11-09** — Pengyu Huang, Peipei Song, Beier Zhu et al. — [Layer Roles Matter: Mitigating Modality Imbalance in Multimodal Emotion Reasoning via Adaptive Layer Profiling](http://arxiv.org/abs/2611.11907v1)
  <details><summary>📄 Abstract</summary>
  Multimodal Emotion Reasoning (MER) requires perceiving and integrating emotion cues from multiple modalities. Recent advances increasingly leverage Multimodal Large Language Models (MLLMs) to enhance reasoning capacity. However, due to the inherent heterogeneity in conveying emotions across modalities, these models often suffer from modality imbalance and confront flawed emotion understanding. In this paper, we conduct an in-depth analysis on MER models and uncover two key empirical insights. (i...
  </details>

- **2026-11-09** — Duc A. Tran, Dung Truong, Duy Le — [DeFSM: Robust and Efficient Decentralization of Federated Submodular Maximization](http://arxiv.org/abs/2611.11866v1)
  <details><summary>📄 Abstract</summary>
  Submodular maximization seeks a small subset best representing a large dataset. In its federated setting, the server is a single point of failure and some clients may be Byzantine. Removing the server raises a trilemma of decentraliza- tion, efficiency, and security. We propose DeFSM, a Byzantine-robust and communication-efficient architecture that replaces the server with a lightweight smart contract and a pool of independent, consensus-free agents. Its aggregation rule, SafeGM, builds on two n...
  </details>

- **2026-11-09** — Jinghe Wang, Xinrui Cao, Duo Wu et al. — [GeoMind: A Benchmark for Spatial Understanding in Robotic Manipulation](http://arxiv.org/abs/2611.12175v1)
  <details><summary>📄 Abstract</summary>
  Robotic manipulation has advanced rapidly in mapping visual observations and language instructions to actions. However, reliable manipulation in open-world environments requires robust spatial understanding: the ability to identify targets in complex layouts (spatial reasoning) and adapt to scenes that continuously evolve through interaction (spatial memory). Yet existing embodied benchmarks fall short in evaluating spatial understanding: they often introduce strong visual cues that bypass spati...
  </details>

- **2026-11-09** — Shuangyu Xie, Kaiyuan Chen, Ken Goldberg — [Flip Anything with Agentic Robotics Self-Learning](http://arxiv.org/abs/2611.11941v1)
  <details><summary>📄 Abstract</summary>
  Flipping is a fundamental robotic manipulation skill that requires reorienting a target object in a stable pose on a planar support surface by rotating it 180$^\circ$ about an axis parallel to the support surface -- think of flipping a coin from heads to tails. Although flipping is a common objective in industrial tasks such as parts inspection, mechanical assembly, and tool use, coding a bimanual robot with grippers to flip diverse objects is a significant challenge. In this paper, we show that...
  </details>

- **2026-11-09** — Paul Häusner, Jevgenija Rudzusika, Jens Sjölund et al. — [Learning inexact alternating minimization for convex problems with quadratic coupling](http://arxiv.org/abs/2611.12544v1)
  <details><summary>📄 Abstract</summary>
  Alternating minimization is a standard tool for optimization problems with two coupled variable blocks. Its cost is dominated by the inner subproblem solvers, which rarely have a closed-form solution. In this paper, we propose to learn an inexact alternating scheme in which neural networks approximate the subproblem solution at each iteration. For convex problems with quadratic couplings between the variable blocks that satisfy a quadratic growth condition, we derive a worst-case bound on the op...
  </details>

- **2026-11-09** — Yuewen Huang, Pin Chen, Yutong Lu — [UniHam: A Large-Scale SOC-Complete Dataset and Benchmark for Hamiltonian Learning in Materials](http://arxiv.org/abs/2611.12509v1)
  <details><summary>📄 Abstract</summary>
  Accurate prediction of electronic Hamiltonians would enable broad property inference while avoiding the high computational cost of Density Functional Theory (DFT). However, progress toward general-purpose materials foundation models is limited by a data bottleneck: existing Hamiltonian datasets are typically small, lack structural diversity, and often omit essential relativistic physics such as spin--orbit coupling (SOC). We therefore construct UniHam, a large-scale Hamiltonian dataset and bench...
  </details>

- **2026-11-09** — Nils-Jonathan Schaller, Thorben Jansen, Olaf Köller et al. — [Detecting AI-Authored Text in Authentic Student Writing: Evidence from PISA 2025](http://arxiv.org/abs/2611.12487v1)
  <details><summary>📄 Abstract</summary>
  AI-text detectors reach near-perfect scores in evaluations that contrast fully human-written texts with texts generated from researcher-designed prompts. In authentic student writing, however, AI use is voluntary and often partial. We study this setting with the PISA 2025 FLA dataset, in which 15-year-olds in Germany wrote English argumentative essays with and without access to a gpt-4o-mini-based chatbot. Keystroke, clipboard and chat logs let us trace every character of the final essay to its ...
  </details>

- **2026-11-09** — Symeon Vaidanis, Photios A. Stavrou, Marios Kountouris — [Reference-Dependent Utility Optimization for Goal-Oriented Communication Systems](http://arxiv.org/abs/2611.12480v1)
  <details><summary>📄 Abstract</summary>
  Traditional communication resource allocation optimizes operational metrics such as rate, latency, energy efficiency, and reliability. Motivated by goal-oriented semantic communication, we develop a generalized allocation framework that transforms operational rewards through reference-dependent user utilities and evaluates them via expected utility, cumulative prospect theory (CPT), or related decision criteria. The formulation separates operational rewards, user-side valuations, and system-leve...
  </details>

- **2026-11-09** — Alex Ardelean, Giacomo Casadei, Paolo Frasca — [Scalable Practical Synchronization of Heterogeneous Linear Systems](http://arxiv.org/abs/2611.12423v1)
  <details><summary>📄 Abstract</summary>
  We study practical state synchronization of heterogeneous linear multi-agent systems over directed graphs using static diffusive state feedback. Persistent mismatches between the agent dynamics generally preclude exact synchronization and are treated as bounded disturbances within an Input-to-State Stability (ISS) framework. We derive a scalable synthesis procedure based on fixed-dimension linear matrix inequalities (LMIs), whose dimension is independent of the number of agents. Local robust dis...
  </details>

- **2026-11-09** — Changming Lei, Junhao Dai, Donghua Shi — [Multi-Target Tracking via Mean Field Feedback Control](http://arxiv.org/abs/2611.12230v1)
  <details><summary>📄 Abstract</summary>
  Cooperative tracking of multiple moving targets requires a swarm to continually adjust its deployment. Existing methods often rely on repeated agent-target reassignment or updates to position-dependent partitions, which can complicate coordination as swarms grow. This motivates us to seek an approach with a lighter coordination burden. Specifically, we formulate multi-target tracking as a time-varying density-tracking problem, with the targets' tracking and sensing demands encoded in a task-dema...
  </details>

- **2026-11-09** — Jens Elgeti Johannes C. Krämer — [Fluctuation-Response Relations and Memory in Tissue Cell Number Dynamics](http://arxiv.org/abs/2611.12216v1)
  <details><summary>📄 Abstract</summary>
  The longevity of multicellular systems requires finely tuned feedback mechanisms to control the balance of cellular proliferation and loss. To understand the microscopic details governing feedback during homeostasis, it is crucial to quantify the feedback using a robust, minimally invasive method. Existing methods typically depend on perturbing the system to quantify the response. Such perturbations may alter cell physiology and are often technically challenging to implement. We propose a steady...
  </details>

- **2026-11-09** — Zixiang Ai, Zhenyu Cui, Xu Zou et al. — [3R-Adapter: Retrieval, Rewiring, and Refinement for Efficient Adaptation of 3D Reconstruction Model](http://arxiv.org/abs/2611.11964v1)
  <details><summary>📄 Abstract</summary>
  Feed-forward 3D reconstruction models have demonstrated strong generalization under large-scale pre-training, yet they struggle in long-tail scenarios such as low-light reconstruction, joint human-scene reconstruction, and test-time adaptation. We observe relational attention structure collapse, manifested as the failure of cross-view correspondences, as a primary cause of these limitations. While adaptation offers a practical way to bridge this gap, existing parameter-efficient fine-tuning (PEF...
  </details>

- **2026-11-09** — Yuji Nozawa, Yu-Chieh Lin, Youyang Ng — [Training Vision Transformers to Focus: Emergence of Spatial Attention Head Specialization](http://arxiv.org/abs/2611.11890v1)
  <details><summary>📄 Abstract</summary>
  Self-supervised learning in Vision Transformer models, such as DINO, enables robust visual perception without requiring labeled data by leveraging large-scale image datasets. However, these models lack a focusing mechanism during training, resulting in perceptual representations that are often ambiguous or overly similar. In this work, we introduce two visual focusing loss functions designed to establish correspondence between the model's attention and specific regions within images. Specificall...
  </details>

- **2026-11-09** — Gwangseon Jang, Sieun Yun, Dong Ho Lee et al. — [MOTIF: LLM-Defined Material Taxonomies for OOD Property Prediction via Invariant Feature Selection](http://arxiv.org/abs/2611.11846v1)
  <details><summary>📄 Abstract</summary>
  Out-of-distribution (OOD) generalization remains a central challenge in materials property prediction, where models must extrapolate to novel chemistries beyond the training distribution. While large language models (LLMs) have demonstrated strong scientific reasoning, their direct use for quantitative prediction remains limited. To address this, we systematically evaluate multiple roles for LLM assistance, finding that only taxonomy-based grouping consistently improves OOD generalization over a...
  </details>

- **2026-11-08** — Sjoerd Takken, Shaodi You — [NightSteps: A Night-Time Dataset and Benchmark for Pedestrian Crossing Intention Prediction](http://arxiv.org/abs/2611.11583v1)
  <details><summary>📄 Abstract</summary>
  Autonomous vehicles use pedestrian crossing intention prediction (PCIP) to participate safely in traffic. Existing models are largely trained under favourable daytime conditions with sufficient daylight. Little is known about the robustness of these models under night-time and low-light conditions, due to the lack of datasets containing night-time footage. This paper investigates how a dataset, named NightSteps, can be constructed and evaluated as a baseline benchmark. The dataset is based on ni...
  </details>

- **2026-11-08** — Liu Xuanyu, Cao Keyi, Cheng Xiang — [WiFo-R: Wireless Foundation Model with Recurrent Channel Representation](http://arxiv.org/abs/2611.11275v1)
  <details><summary>📄 Abstract</summary>
  Wireless foundation models learn transferable channel state information (CSI) representations across heterogeneous wireless systems. However, conventional grid-aligned representations couple feature sequence length to CSI dimensions, restricting the allocation of representation capacity to different propagation conditions and task requirements while increasing inference overhead. This paper proposes WiFo-R, a wireless foundation model that learns progressive channel representations with selectab...
  </details>

- **2026-11-08** — Yinghang Ma, Wuyang Dai, Song Wang et al. — [Beyond Code Translation: Agentic Android-to-HarmonyOS Migration](http://arxiv.org/abs/2611.11192v1)
  <details><summary>📄 Abstract</summary>
  Migrating Android applications to HarmonyOS is an important yet challenging software engineering task. Existing large language model (LLM)-based migration approaches primarily translate code at the method or file level, overlooking project-wide dependencies and workflow coordination. Moreover, ArkTS, the primary language for HarmonyOS, is relatively low-resource, and migrated applications often lack sufficient tests for reliable verification, making end-to-end migration error-prone. We present A...
  </details>

- **2026-11-08** — Shrinivass Arunachalam Balasubramanian — [Advancements in Cloud-Native Systems: A Systematic Mapping Study of Reliability and Scalability across Cloud-Native, Edge-Native and AI-Enabled Systems](http://arxiv.org/abs/2611.11040v1)
  <details><summary>📄 Abstract</summary>
  Cloud-native systems now extend to the network edge and host artificial-intelligence (AI) workloads, including AI agents, but evidence on their reliability and scalability is scattered and uneven. We report a PRISMA 2020 systematic mapping study with an evidence-graded synthesis. Five logged OpenAlex searches on 11 October 2026 covered cloud-native systems, edge AI, agentic AI for operations, reliability of agentic applications and physical AI; 189 records from an earlier exploratory search were...
  </details>

- **2026-11-08** — Andrew R Weckstein, Issa J Dahabreh, Marinka Zitnik et al. — [Does Predictive Performance Translate to Causal Performance? Evaluating tabular foundation models as nuisance learners for causal effect estimation](http://arxiv.org/abs/2611.11381v1)
  <details><summary>📄 Abstract</summary>
  Tabular foundation models based on prior-data fitted networks (PFNs) achieve strong predictive performance, but their value for causal inference is unclear. We evaluated whether PFNs, which predict through in-context learning, could match or outperform conventional nuisance learners in supporting accurate causal estimation and reliable uncertainty quantification (inference). Learners modeled propensity scores and outcome regressions within doubly robust estimators of average causal effects, with...
  </details>

- **2026-11-08** — Wali Ullah Khan — [Energy-Harvesting-Aware Cell-Free LEO Satellite Networks: A Lyapunov Framework for Sustainable User-Centric Beamforming and Clustering](http://arxiv.org/abs/2611.11283v1)
  <details><summary>📄 Abstract</summary>
  We study battery-aware downlink control in user-centric cell-free low Earth orbit satellite networks with intermittent solar harvesting and finite onboard batteries. A perturbed Lyapunov controller coordinates clustering and hybrid beamforming using measured battery states and causal harvest forecasts. The per-slot solver combines group-sparse association, rate bounds, a quadratic transform, and successive convex approximation. We establish robust battery invariance for feasible implemented acti...
  </details>

- **2026-11-08** — Zedong Wang, Yucheng Wang, Dan Xu — [Virtual Task Prompting for Multi-Task Scene Understanding](http://arxiv.org/abs/2611.11041v1)
  <details><summary>📄 Abstract</summary>
  Multi-task scene understanding models typically rely on modified vision encoders or complex decoders for cross-task interaction, which limits their flexibility and compatibility with off-the-shelf vision foundation models (VFMs). We introduce Virtual Task Prompting (VTP), which frames multi-task prompting as retrieving task-adaptive compositions from a shared virtual state, where both the state and routing process are optimized in an end-to-end manner. Concretely, VTP maintains an expanded set o...
  </details>

- **2026-11-07** — In-Jae Lee, Namtae Kim, Robert Exley et al. — [AmodalBox: Automated 3D Bounding Box Annotation under Partial Visibility](http://arxiv.org/abs/2611.10821v1)
  <details><summary>📄 Abstract</summary>
  Recent progress in vision foundation models (VFMs) has made automated open-vocabulary 3D bounding box annotation increasingly feasible by jointly leveraging LiDAR point clouds and images. However, partial observations remain a major challenge in sparse driving scenes, where visible LiDAR points often cover only a small fraction of the object's surface and provide insufficient cues for estimating its full spatial extent. As a result, existing methods often produce mislocalized boxes or leave obje...
  </details>

- **2026-11-07** — Zihe Gao, Zhengling Qi, Yifan Cui — [Trustworthy Recursive Self-Improvement with Statistical Guarantees](http://arxiv.org/abs/2611.10787v1)
  <details><summary>📄 Abstract</summary>
  Recursive self-improvement offers a promising path toward AI agents that improve through experience by refining their own harnesses without retraining their underlying large language models (LLMs). Making this self-improvement process reliable, however, requires more than generating new updates: agents must decide which changes are worth keeping. A greedy gate that accepts updates based solely on higher validation scores can mistake an observed gain for genuine progress and lead to performance d...
  </details>

- **2026-11-07** — Davide Proserpio — [Do Modern Difference-in-Differences Estimators Change Published Findings in Business Research?](http://arxiv.org/abs/2611.11003v1)
  <details><summary>📄 Abstract</summary>
  Staggered-adoption difference-in-differences (DiD) designs are a workhorse of empirical research in business-school journals. The two-way fixed effects (TWFE) estimator that typically implements them can place negative weights on heterogeneous treatment effects. We ask whether negative weights change published findings by reanalyzing staggered-adoption specifications in business-school journals with journal-wide public replication archives. Following Hull (2026), we use large language model agen...
  </details>

- **2026-11-07** — Zhizhang Fu, Lucas Zhao, Michalis Korakakis et al. — [SWEET: Mitigating Spurious Feature Reliance in LLM Reasoning via Weight Editing](http://arxiv.org/abs/2611.10974v1)
  <details><summary>📄 Abstract</summary>
  Reasoning in large language models can be disrupted by simple input perturbations (e.g. adding irrelevant distractors), suggesting reliance on spurious correlations. Identifying and suppressing the spurious features involved in long chain-of-thought reasoning remains challenging. We introduce Spurious-feature WEight EdiTing (SWEET), a training-free method that combines counterfactual interventions with mechanistic interpretability to identify and suppress spurious-features. SWEET extracts token-...
  </details>

- **2026-11-07** — Usha Shrestha, Radu Timofte, Dmitry Ignatov — [Semantic Synthesis over Brute-Force Search: LLM-Guided Transformation Design for Efficient Learning](http://arxiv.org/abs/2611.10940v1)
  <details><summary>📄 Abstract</summary>
  Data transformation pipelines shape the training distribution in computer vision, but designing them is a computationally expensive problem. We investigate whether large language models can enable efficient discovery by synthesizing executable transformation programs outside predefined augmentation spaces. We compare nine strategies under a unified training protocol, including standard augmentation policies, brute-force search, direct code generation with two LLMs, and performance-guided generat...
  </details>

- **2026-11-07** — Hossam Elsafty, Tobias Deußer, Lorenz Sparrenberg et al. — [Evaluating Jev on Arabic: Comparing Decision Models and LLMs Across Arabic Tasks and Dialects](http://arxiv.org/abs/2611.10802v1)
  <details><summary>📄 Abstract</summary>
  How does Jev compare with other systems on Arabic tasks, and how does its performance change between Modern Standard Arabic (MSA) and dialects? We evaluate 67 systems, including 47 decision models and 20 large language models (LLMs), on 43 tasks across 9 task families using a shared zero-shot protocol. The Arabic-focused frozen suite includes English controls in three parallel resources, which we also remove in a separate descriptive comparison. Jev 1.14.0 achieves a mean task-primary metric of ...
  </details>


### 📂 watermark
*水印与溯源 / Watermarking & Provenance* — 19 papers

- **2026-11-10** — Ilia Larchenko, Gleb Zarin, Atindra Nair et al. — [One Policy for 100 Household Tasks: Our Solution for the 2026 BEHAVIOR Challenge](http://arxiv.org/abs/2611.14432v1)
  <details><summary>📄 Abstract</summary>
  We describe our solution for the 2026 BEHAVIOR Challenge: 100 long-horizon household tasks in the OmniGibson simulator. We placed 9th on the final leaderboard, the only independent team in the top 10. The core of the solution is a single vision-language-action (VLA) model, one checkpoint for all 100 tasks, built on our 1st-place 2025 solution, which is based on $π_{0.5}$. On the 50 tasks shared with 2025, its Q rises from 0.260 to 0.371; across all 100 tasks it scores 0.392. Our main conclusion ...
  </details>

- **2026-11-10** — Yupeng Han, Kai Zhang, Shuochen Liu et al. — [Personalized Memory Rubrics: Learning What to Remember per User via Rubric-Guided Credit Assignment](http://arxiv.org/abs/2611.14017v1)
  <details><summary>📄 Abstract</summary>
  Long-horizon personalized agents maintain an evolving memory by continuously deciding what to add, modify, or discard. However, learning an optimal update policy remains challenging. Conventional training relies solely on terminal question-answering accuracy, yielding a coarse feedback signal that treats all intermediate updates identically. Furthermore, update utility is inherently user-specific, as identical memory actions may yield opposite effects across different user personas. Existing met...
  </details>

- **2026-11-10** — Fantong Meng, Chengjie Sun, Shuangjia Yang et al. — [One Sequence Is Enough: Fingerprinting Language Models from Fixed-Length Integer Sequences](http://arxiv.org/abs/2611.14010v1)
  <details><summary>📄 Abstract</summary>
  Users of model APIs and third-party platforms often rely on the declared model name to identify the model responding to their requests. However, the actual model may differ from the declared one, motivating identity verification based on observable outputs. Previous studies have shown that preferences in simple numerical-choice tasks can serve as model fingerprints. We investigate whether a single fixed-length integer sequence can combine multiple numerical observations to identify its source mo...
  </details>

- **2026-11-10** — Niran Nataraj, Maina Sogabe, Masamichi Yamashita et al. — [TransGHOST: Real-Time, Synthesis-Free Reconstruction of Instrument-Occluded Regions in Ophthalmic Microsurgery](http://arxiv.org/abs/2611.13971v1)
  <details><summary>📄 Abstract</summary>
  Intraoperative scene perception in ophthalmic microsurgery is limited by instrument occlusion: when a tool enters the high-magnification field, it conceals tissue from both the surgeon and the perception components of robot-assisted systems that process the video. Generative inpainting can remove the occluder but replaces the missing image content with synthesis, which is unsuitable when visual provenance matters. Many video inpainters also depend on future frames and cannot operate online. We p...
  </details>

- **2026-11-10** — Qi Luo, Ziwen Wang, Kunlin Li et al. — [Scaling Shapley Energy Attribution to Large LLM Batches](http://arxiv.org/abs/2611.13802v1)
  <details><summary>📄 Abstract</summary>
  LLM services have become essential infrastructure for applications such as chat assistants and coding agents. Service providers need to attribute resource consumption to individual requests for purposes such as billing. Among these resources, energy is a key metric for assessing the cost of serving each request. However, serving engines batch requests together, and GPUs report only aggregate energy consumption. Providers typically estimate each request's share in proportion to its token consumpt...
  </details>

- **2026-11-09** — Mohamed Bachar, Ilyass Abouelaziz, Yuehua Ding — [Continuous-Time Set-Transformers for Asynchronous WiFi-IMU Indoor Localization](http://arxiv.org/abs/2611.13057v1)
  <details><summary>📄 Abstract</summary>
  Indoor localization commonly combines WiFi received signal strength indicator (RSSI) fingerprints with inertial measurements. However, these sensor streams are sampled asynchronously at different rates; therefore, observations rarely align in time and may be missing or stale. Most existing methods resample the data onto a shared clock and process each modality using a separate branch. We instead present a continuous-time transformer that represents observations as an unordered set of timestamped...
  </details>

- **2026-11-09** — James Rhodes, George Kang — [Beyond the Document: Compiled Context and Governed Agents for Any Work Product](http://arxiv.org/abs/2611.13055v1)
  <details><summary>📄 Abstract</summary>
  A document preserves the visible result of professional work but often discards the research, calculations, assumptions, evidence, and authorization boundaries behind it. We study a different unit of delivery: a Portable Agent Format (PAF) package that carries a work product together with compiled context, evidence, provenance, and rules for subsequent interaction. To test whether this context remains useful beyond the process that produced it, we evaluate four new packages, created after the ho...
  </details>

- **2026-11-09** — Jiongchi Yu, Yue Duan, Ziming Zhao et al. — [The Gene Is Not the Gate: Conceptualizing the Semantic Genome of Quantum Software](http://arxiv.org/abs/2611.13049v1)
  <details><summary>📄 Abstract</summary>
  Quantum software spans applications, program representations, compilers, runtimes, and hardware-facing control. Existing abstractions describe these artifacts and layers, but they do not capture the semantic responsibilities that must remain valid as a computation is transformed across the stack. This limits systematic reasoning about cross-layer correctness, evolution, and reuse.   We present QGenome, a semantic foundation for quantum software genomics. We define a quantum software gene as a ty...
  </details>

- **2026-11-09** — Abdulhady Abas Abdulla, Jiyan Salim Mahmud, Fatemeh Daneshfar et al. — [TANSAR: Editable and Attributable Correlation Matrix Memories under Correlated Keys, with Rule-Constrained Multi-Hop Knowledge Editing](http://arxiv.org/abs/2611.12374v1)
  <details><summary>📄 Abstract</summary>
  Correlation Matrix Memories (CMMs) store associations as sums of rank-one outer products, providing closed-form addressability, exact deletion, and linear attribution. While classical analyses assume random, orthogonal keys, semantic encoders produce correlated representations. We analyse CMMs under correlated keys using frame-theoretic coherence: (i) capacity bounds yielding an encoder-independent limit $n \le d(1+\varepsilon^2)$ for mean squared crosstalk $\varepsilon^2$; (ii) an exact charact...
  </details>

- **2026-11-09** — Wei-Chieh Huang, Weizhi Zhang, Jiayan Nan et al. — [MIRIX-2.0: Multi-Agent Memory System](http://arxiv.org/abs/2611.12068v1)
  <details><summary>📄 Abstract</summary>
  Long-term memory lets LLM agents personalize, stay consistent, and reuse what worked before. Parametric memories need training, consolidation can lose details for good, and keeping every record leaves a growing store to search. We present MIRIX-2.0, a multi-agent memory system designed to be practical, accurate, and efficient at once. It is the most accurate of the compared systems on four of five QA benchmarks. It reaches 91.4% on LoCoMo and 72.6% on LongMemEval-S, where it leads the strongest ...
  </details>

- **2026-11-09** — Yifan Luo, Takafumi Matsumaru, Vibekananda Dutta et al. — [DPGS-SLAM: Diffusion-Prior and Provenance-Aware Monocular Gaussian Splatting SLAM for Dynamic Visual Sensing](http://arxiv.org/abs/2611.12038v1)
  <details><summary>📄 Abstract</summary>
  This paper presents DPGS-SLAM (Diffusion-Prior and Provenance-Aware Monocular Gaussian Splatting SLAM) for dense mapping in environments containing dynamic objects. Dynamic observations can contaminate camera tracking and scene reconstruction in visual SLAM (simultaneous localization and mapping). Although 3DGS (3D Gaussian splatting) enables efficient dense mapping, existing 3DGS-SLAM systems may exhibit instability when dynamic objects violate their underlying static-scene assumption. Excludin...
  </details>

- **2026-11-09** — Wei Chen, Lihao Zhuang, Yubing Wu et al. — [Trajectory Density Ratios under Weak Support: A Survey across the Sciences](http://arxiv.org/abs/2611.11985v1)
  <details><summary>📄 Abstract</summary>
  Many problems across the sciences compare two stochastic processes through the sequences they generate. Reinforcement learning asks what a new policy would return from the trajectories of an old one; molecular simulation asks how much more a ligand binds from samples of the unbound state; climate attribution asks how a heat wave shifted under warming; and language-model post-training asks what a deployed agent will do from logged interactions. In every case, one quantity would answer all these q...
  </details>

- **2026-11-09** — Akwasi Asare — [Benchmarking CNNs, Vision Transformers, and Foundation Models for Explainable Brain Tumor MRI Classification: Calibration, Decision Analysis, and External Validation](http://arxiv.org/abs/2611.11793v1)
  <details><summary>📄 Abstract</summary>
  Deep learning models for brain tumor MRI classification are usually compared by accuracy alone, on public datasets whose independence is rarely checked. We benchmarked six architectures: two convolutional networks (EfficientNetV2-M and ConvNeXt-V2-Tiny), two vision transformers (Swin-V2-S and ViT-L/16), and two foundation models (DINOv2-L and MedSigLIP-448), for four-class classification of 7,216 public MRI images. We assessed accuracy, calibration, explainability, ensembles, and decision curves...
  </details>

- **2026-11-08** — Tiltan Gilat, Gal Engelberg, Ariel Zadok et al. — [Agentic Attribution of Cloud Resource Ownership](http://arxiv.org/abs/2611.11340v1)
  <details><summary>📄 Abstract</summary>
  Security tools raise findings across cloud environments, and AI agents now investigate and prioritize them. A finding is still resolved by people: it has to reach the people responsible for fixing it and accountable for the resource it concerns. Ownership is the organizational context that decides who that is. Where recorded, it is declared by hand in configuration management databases or owner tags and goes stale unless kept current; accounts are shared, and automation creates much of the infra...
  </details>

- **2026-11-08** — Po-Ming Law, Jianheng Ouyang, Nguyen-Truong Thinh et al. — [Linking Event-sequence Data Claims to Analytic Provenance in Chatbots: Technique and Evaluation](http://arxiv.org/abs/2611.11325v1)
  <details><summary>📄 Abstract</summary>
  Chatbots are increasingly used to analyze temporal event sequences of which website clickstreams are among the most common. Explanations are essential for understanding claims about event-sequence data. However, existing systems often require programming expertise to interpret these explanations and fail to explain the data processes underlying the data claims. We introduce a technique for linking a data claim to its analytic provenance (i.e., the analytic steps and results that produced it). It...
  </details>

- **2026-11-08** — Bharatha Rankothge, Suzanne Hodgkins, Virginia Rich et al. — [Agents Propose, Code Verifies, Humans Decide: Verified Agentic Ingestion of Heterogeneous Scientific Tables into Relational Databases](http://arxiv.org/abs/2611.11045v1)
  <details><summary>📄 Abstract</summary>
  Public scientific datasets rarely arrive analysis-ready. They arrive as messy folders of wide matrices, long tables, spreadsheets, and per-cohort files whose keys and encodings differ, and every reanalysis must reconnect them first. A coding agent can automate this, but its mistakes can look plausible, and without an audit trail, a mistake that corrupts data can go uncaught. We present an AI-assisted ingestion pipeline built on one rule: LLM agents propose, deterministic code verifies, and human...
  </details>

- **2026-11-08** — Muhammad bin Javaid, Karim K. Ben Hicham, Enkhnyam Battulga et al. — [Building and Auditing Chemical Datasets with LLMs: A General LLM-as-a-Judge Framework Applied to Homogeneous Catalytic PET Depolymerisation](http://arxiv.org/abs/2611.11030v1)
  <details><summary>📄 Abstract</summary>
  Large language models can rapidly extract structured multivariate experimental data from the chemistry literature, yet verifying thousands of generated records without ground truth remains difficult. We present a general, citation-grounded extraction and verification methodology centered on an independent "LLM-as-a-judge", applied to the literature on homogeneous catalytic poly(ethylene terephthalate) (PET) depolymerisation. In this pipeline, an extractor LLM generates schema-enforced records fr...
  </details>

- **2026-11-07** — Uday Allu — [Lightfoot: Graph Retrieval-Augmented Generation with Exact, Model-Free Document Deletion](http://arxiv.org/abs/2611.11010v1)
  <details><summary>📄 Abstract</summary>
  Graph-based retrieval-augmented generation (GraphRAG) improves multi-hop question answering, but deployed systems face two costs that research comparisons rarely measure: building the graph, and removing documents from it. We present Lightfoot, a GraphRAG system in which every entity, link, fact and synonym edge is a deterministic function of per-passage extractions carrying chunk-level provenance. Indexing makes one language-model call per passage, retrieval makes none, and deleting a document ...
  </details>

- **2026-11-06** — Claudio Segal, Paulo Segal, Hudson Silva Borges et al. — [Agents on the Patch Path: Mining AI-Associated Security Remediation in GitHub Security Advisories](http://arxiv.org/abs/2611.09808v1)
  <details><summary>📄 Abstract</summary>
  Autonomous coding agents are increasingly involved in software development, but their participation in real-world security remediation remains poorly understood. We investigate observable evidence of coding-agent involvement in commits referenced by reviewed GitHub Security Advisories (GHSAs), characterize the associated vulnerabilities, and examine review timing in relation to advisory disclosure routes.   We develop a local-Git mining pipeline that identifies agent evidence through known agent...
  </details>


### 📂 benchmark
*安全评测与基准 / Safety Benchmarks & Evaluation* — 1 papers

- **2026-11-10** — Qinfeng Zhu, Weiguang Zhao, Ke Sun et al. — [LEASH: Stay Safe in Agentic Robotics](http://arxiv.org/abs/2611.14115v1)
  <details><summary>📄 Abstract</summary>
  Foundation models such as GPT and Claude have shown strong capabilities in spatial understanding and embodied intelligence. These advances make agentic robotics a promising path toward artificial general intelligence in robotics. However, we find that using foundation models to control robots poses serious safety risks, and comprehensive safety evaluation is still lacking. We introduce RoboRisk, a comprehensive benchmark for evaluating safety in agentic robotics. Its 92 simulated tasks and 13 ph...
  </details>


### 📂 survey
*综述与系统化 / Surveys & Systematization* — 4 papers

- **2026-11-10** — Jingjing Jiang — [A Cross-Scenario Survey and Analysis of Self-Evolving Multimodal Agents](http://arxiv.org/abs/2611.14256v1)
  <details><summary>📄 Abstract</summary>
  Recent work shows that multimodal agents increasingly self-improve without recurring human annotation. However, each self-improvement mechanism is designed and evaluated within a single scenario, leaving its preconditions unverified under cross-scenario transfer. This survey investigates the structural source of asymmetric mechanism transfer across four scenarios: multimodal reasoning, multimodal generation, GUI and Web navigation, and embodied manipulation. We first formalize the self-evolving ...
  </details>

- **2026-11-10** — Javier Hernandez, Andrew D. Wilson — [PARLEY: Evaluating LLM Collaboration Through Cooperative Asymmetric Puzzles](http://arxiv.org/abs/2611.14242v1)
  <details><summary>📄 Abstract</summary>
  As large language models power autonomous agents, understanding how they collaborate and where they fail becomes critical. We introduce PARLEY, an extensible platform for studying LLM agent collaboration through four asymmetric puzzle tasks grounded in cognitive psychology (referential communication, joint coordination, perspective-taking, and spatial reasoning). GPT-4o agent pairs succeeded in 60.5% of conversations (N=400, 100 per task), with task-level variation (34-80%) reflecting distinct c...
  </details>

- **2026-11-10** — Shyam Agarwal, Olga Lvova, Agnia Sergeyuk et al. — [The AI Era's Lines of Code? A Case Study on What an Engineer's Token Spend Measures](http://arxiv.org/abs/2611.13396v1)
  <details><summary>📄 Abstract</summary>
  Organizations use engineers' token spend to monitor AI adoption, set budgets, and measure productivity, but the metric's relationship with engineering output is unclear. We link five weeks of token usage in coding agents to the commits of 404 engineers at JetBrains, and analyze a company survey of 412 employees. We find that token spend varied mostly between engineers, and which engineers spent the most stayed largely the same over the five weeks. Among weeks with similar commit counts, the 90th...
  </details>

- **2026-11-09** — Jeremy Canale, Fabien Soulis — [Detecting Shadow AI: Unsanctioned LLM Agents on Enterprise Endpoints: A Taxonomy, an Open Detector and a Controlled Evaluation](http://arxiv.org/abs/2611.12377v1)
  <details><summary>📄 Abstract</summary>
  Shadow IT, the use of technology that the IT organisation has not approved, is a long-standing governance problem. We argue that autonomous AI agents can make it grow much faster: agents make building tools nearly free, act with their user's privileges, and leave behind scripts, automations and MCP servers that are themselves unsanctioned. A simple compounding model shows that, under its assumptions, shadow IT grows exponentially once agentic artifacts reproduce faster than the organisation reti...
  </details>


### 📂 other
*其他安全相关 / Other Security-Related* — 208 papers

- **2026-11-10** — Tanishq Rachamalla, Srishti Kaushik, Muhammad Attique Khan et al. — [RS-JEPA: Remote Sensing Joint-Embedding Predictive Architecture with Scan-Path Views for Cross-Sensor Image Retrieval](http://arxiv.org/abs/2611.14496v1)
  <details><summary>📄 Abstract</summary>
  Cross-sensor remote sensing image retrieval aims to find scenes with the same content across heterogeneous sensors, such as SAR and optical or panchromatic (PAN) and multispectral (MS) imagery, without manual labels. Existing self-supervised methods either reconstruct sensor-specific pixel detail, align each image only with its co-registered twin, or rely on large transformers with 118-173M parameters (and up to 398M). We introduce RS-JEPA, a compact joint-embedding predictive framework built on...
  </details>

- **2026-11-10** — Bikrant Bikram Pratap Maurya — [Domain-Invariant and Language-Model-Assisted Acoustic Side-Channel Attacks on Keyboards](http://arxiv.org/abs/2611.13922v1)
  <details><summary>📄 Abstract</summary>
  Acoustic side-channel attacks (ASCA) recover typed text from the sound of keystrokes, using only a commodity microphone and no access to the victim's device. Prior work establishes that such attacks succeed under idealized laboratory conditions - a single keyboard, a fixed microphone, a quiet room, and training and testing on the same device but leaves open the question that matters for security: whether keystroke inference survives the open world of unseen keyboards, diverse users, noisy enviro...
  </details>

- **2026-11-10** — Canyon Grey Dell'Omo, Joao Pedro de Carvalho Voltani — [Stinging the Swarm: Extracting Attacker Intelligence from a Twin-Controller OT Honeypot](http://arxiv.org/abs/2611.13406v1)
  <details><summary>📄 Abstract</summary>
  Autonomous language-model agents can drive industrial controllers over fieldbus protocols, probing a plant at machine speed and in coordinated swarms. We present Talos, an inline gate that judges every agent request to a controller in milliseconds and routes agents it flags as hostile to a device-faithful decoy -- a mirror twin of the real plant -- where their attack continues harmlessly and is read for intelligence. We evaluate the full pipeline (detect -> quarantine -> mirror -> extract) again...
  </details>

- **2026-11-10** — Guorui Lu, Qinyu Chen — [C$^2$-Routing: Complementary Cropping and Compression for Efficient Vision-Language Inference](http://arxiv.org/abs/2611.14469v1)
  <details><summary>📄 Abstract</summary>
  Visual Question Answering (VQA) imposes substantial computational overhead on vision-language models (VLMs), motivating model-agnostic input reduction methods that can be readily applied across diverse VLMs, including in black-box settings. Simply enforcing a visual-token cap reduces computation, but it can discard information needed to answer the question. A single reduction strategy also struggles to accommodate different scenarios. Our key observation is that cropping and compression are comp...
  </details>

- **2026-11-10** — Souhaila Djaffal, Amna Jamal, Gagana Madhugiri Devaraja et al. — [Evaluating LLM-Generated World Models for Neuro-Symbolic Reasoning](http://arxiv.org/abs/2611.14419v1)
  <details><summary>📄 Abstract</summary>
  Formal world models can support planning, verification, and safety reasoning, but constructing them from open-ended natural-language situations is difficult, particularly in multi-agent settings where several formalizations may be plausible. We study whether five LLMs can generate such world models as partially observable stochastic games and whether mechanical validity is sufficient to establish that the resulting model faithfully represents the intended decision problem. We introduce a benchma...
  </details>

- **2026-11-10** — Avinash Singh, Manish Saroya, Fatemeh Cheraghi Pouria et al. — [SIGMO: Sigmoid Gated Interaction-Aware Motion Planning](http://arxiv.org/abs/2611.14414v1)
  <details><summary>📄 Abstract</summary>
  Despite the widespread adoption of autonomous vehicle technologies, reliable navigation within cluttered environments remains arduous due to the necessity of interaction-aware strategies; example scenarios include: narrow passages with multiple agents, lane changing in dense traffic, and crossing unsignalized intersections. These scenarios often require highly proactive strategies, simultaneously demanding interpretability and quick adaptability, which challenge end-to-end and data-driven method...
  </details>

- **2026-11-10** — Dong Han, Jin Zhang, Kunyue Yang — [Cognitive Mapping of Learning by Thinking Mechanisms in Large Language Models](http://arxiv.org/abs/2611.14382v1)
  <details><summary>📄 Abstract</summary>
  Large language models (LLMs) increasingly exhibit capabilities that resemble human Learning by Thinking (LbT), the acquisition of new insight through internal processes such as explanation and reasoning, without new external input. A systematic account of the cognitive mechanisms behind these capabilities, and of their limits, remains underdeveloped. This paper proposes a Cognitive LbT Framework that maps four mechanisms (Reflective Reasoning, Synthetic Memory Formation, Internal Simulation, and...
  </details>

- **2026-11-10** — Jiahang Lin, Wanying Ren, Wanghan Xu et al. — [ARE-bench: Benchmarking Agents' Research Ability in Real-World Researcher Sessions and Workspaces](http://arxiv.org/abs/2611.14364v1)
  <details><summary>📄 Abstract</summary>
  Research agents achieve increasingly strong benchmark scores, yet these scores do not necessarily translate into reliable delivery in ongoing research projects. Many research-agent benchmarks emphasize standalone tasks and relatively self-contained workflows in clean or curated workspaces. However, researchers ask agents to complete one step within an ongoing project, where requests depend on earlier session decisions and workspaces contain unfinished files, outdated versions, and failed attempt...
  </details>

- **2026-11-10** — Dominika Maslarova, Mattys Pouyez, Patrik Jansson et al. — [Physics-informed Bayesian optimization of high-order harmonic generation in gases](http://arxiv.org/abs/2611.14119v1)
  <details><summary>📄 Abstract</summary>
  Optimization of high-order harmonic generation in gases is essential for attosecond science. Improving conversion efficiency from the infrared driving laser to the extreme-ultraviolet high-order harmonic radiation requires balancing microscopic single-atom dipole responses with macroscopic phase matching. The resulting conversion-efficiency landscape exhibits complex structures, such as the hyperbolic ridge in the pressure-length space, which can be difficult to accurately reconstruct using conv...
  </details>

- **2026-11-10** — Minyu Zhou, Yajing Wu, Yongqiang Tang et al. — [ScaleBrain: A Scale-Consistent Framework for EEG Foundation Models](http://arxiv.org/abs/2611.14035v1)
  <details><summary>📄 Abstract</summary>
  Foundation models pre-trained on large unlabeled electroencephalography (EEG) corpora have emerged as a transformative paradigm for Brain-Computer Interface (BCI) applications. Recent EEG foundation models have shown that multi-scale representations derived from fixed-length patches can improve EEG representation learning. Existing frameworks commonly construct temporal scales through feature-level operations. However, these operations leave the correspondence between learned features and scale-...
  </details>

- **2026-11-10** — Haotian Qi, Gabriel Skantze — [AVCC: Audio-Visual Conversation Corpus for Turn-Taking Prediction with a Human Benchmark](http://arxiv.org/abs/2611.13957v1)
  <details><summary>📄 Abstract</summary>
  } Predicting who will speak next, and when, is a prerequisite for conversational agents and social robots that take turns without waiting for silence. Multiparty next-speaker prediction (NSP) has been studied on corpora with per-speaker sensors, each with its own event definitions. No public benchmark covers the single camera and microphone a robot has, and no model has been compared against how well people perform the same prediction. We turn AVCC, a 31-hour audio-visual corpus of two- and thre...
  </details>

- **2026-11-10** — Yash Purswani, Shivansh Agarwal, Anuj Tiwari — [Safety and Connectivity Certificates for Finite-Time Formation Transitions](http://arxiv.org/abs/2611.13927v1)
  <details><summary>📄 Abstract</summary>
  Finite-time formation transitions are useful for coordinating multi-agent systems in time-critical missions, but convergence to a prescribed formation in finite time does not guarantee collision avoidance or communication connectivity during the transition. Existing approaches address finite-time coordination and safety-constrained formation control, yet explicit connections between disagreement during transitions, formation geometry, and coupling-gain selection need to be developed for certifyi...
  </details>

- **2026-11-10** — Lianlei Shan, Han Jin, Yaunchao Ma et al. — [Game-Enhanced Embodied Learning with Event and Foresight Pretraining](http://arxiv.org/abs/2611.13819v1)
  <details><summary>📄 Abstract</summary>
  Human gameplay supplies paired observations, actions, and visual consequences that can supplement robot-policy training. We study event-and-foresight pretraining for InternVLA-A1.5, combining recorded keyboard/mouse event prediction with history-conditioned visual supervision through a frozen video model. Coverage-preserving anchor selection constructs one-second targets, and an attention mask prevents teacher-forced future actions from entering foresight queries. The selected corpus contains 39...
  </details>

- **2026-11-10** — Shengzhou Kong — [Omni-JEV: Text and Dual-Stream Speech Decisions](http://arxiv.org/abs/2611.13777v1)
  <details><summary>📄 Abstract</summary>
  A user utterance does not uniquely determine the next action in full-duplex dialogue: its consequences depend on the assistant's response state and interaction history. Speech activity, utterance completion, and interruption intent provide related evidence, whose implications for a response require an explicit action policy. We formulate this task at collected-segment endpoints and introduce Omni-JEV, which maps text or role-indexed user and assistant-reference speech to probabilities over five ...
  </details>

- **2026-11-10** — Saeid Firouzi Daghigh, Saeed Ayat — [From Depth to Safe Depth: Uncertainty-Aware Monocular Perception for Mobile Robot Navigation](http://arxiv.org/abs/2611.13769v1)
  <details><summary>📄 Abstract</summary>
  Monocular depth foundation models make it tempting to replace depth sensors on mobile robots with a single RGB camera. We show that, used off the shelf, this is unsafe: in a simulated indoor navigation benchmark, a standard Nav2 stack driven by Depth Anything V2 (metric) collides in 63\% of 120 episodes, because the model systematically over-estimates the distance to nearby obstacles. We propose a lightweight plug-in module that turns predicted depth into \emph{safe depth}. A 0.58\,M-parameter h...
  </details>

- **2026-11-10** — Yuechun Sun, Jun Yang, Kexin Pei — [Curriculum proof repair with learned counterexamples](http://arxiv.org/abs/2611.13627v1)
  <details><summary>📄 Abstract</summary>
  Language models (LMs) have substantially lowered the barrier to applying formal verification for building reliable and secure software. Existing approaches commonly follow the verifier-in-the-loop paradigm, but the verifier often provides only coarse, binary pass/fail feedback, which offers little actionable signal on how the proof should be repaired. Recent work shows that counterexamples provide more actionable feedback by grounding proof failures in concrete program states, but generating use...
  </details>

- **2026-11-10** — Tiancheng Xu, Wensheng Yu — [Megrez: A Knowledge-Guided Agent for Formal Mathematics over MK Set Theory](http://arxiv.org/abs/2611.13613v1)
  <details><summary>📄 Abstract</summary>
  General-purpose coding agents equipped with proof-assistant tools have shown strong performance on standalone competition problems, yet cumulative textbook formalization inside a low-resource mathematical library still faces three obstacles: aligning textbook concepts with library declarations, keeping long-horizon search synchronized with live proof states, and integrating locally verified proofs reliably into a growing codebase. We present Megrez, a knowledge-guided formalization agent for Roc...
  </details>

- **2026-11-10** — Yuqi Wang, Fengyuan Liu, Mukai Li et al. — [Market-Conditioned JEPA: Learning from Unpredictable Market Shocks](http://arxiv.org/abs/2611.13572v1)
  <details><summary>📄 Abstract</summary>
  Much of the variation in financial time series is driven by market-wide shocks that cannot be predicted from an asset's own history. Per-asset self-supervised learning treats this variation as irreducible noise. Under a latent factor model, we show that conditioning prediction on the realized market factor makes the asset's market exposure necessary for optimal prediction, while reducing the noise against which the asset-specific component is learned. Building on this insight, we introduce Marke...
  </details>

- **2026-11-10** — P Sangeerth, Poulomee Ghosh, Pushpak Jagtap — [Incremental Input-to-State Stabilization of Partially Unknown Control-Affine Systems within Prescribed Safe Sets](http://arxiv.org/abs/2611.13556v1)
  <details><summary>📄 Abstract</summary>
  Incremental input-to-state stability ($δ$-ISS) guarantees that the trajectories of a system converge towards one another, up to a gain on the difference of their inputs. Some existing learning-based designs that combine incremental stability with safety achieve only incremental input-to-state practical stability, whose non-vanishing offset can make the guarantee conservative. We consider control-affine systems with a known, full-row-rank input matrix and an unknown drift learned using Gaussian p...
  </details>

- **2026-11-10** — Jiawei Xiao, Boya Wang, Longtian Qiu et al. — [Reasoning-Aware Relational Representation Learning for Open-Vocabulary Scene Graph Generation](http://arxiv.org/abs/2611.13496v1)
  <details><summary>📄 Abstract</summary>
  Open-Vocabulary Scene Graph Generation (OV-SGG) requires models to recognize visual relationships beyond the training vocabulary, yet existing methods often rely on dataset-specific object--predicate co-occurrence patterns. Under long-tailed distributions and noisy object localization, such reliance leads to biased, entangled relation representations, limiting both rare-relation recognition and generalization to unseen predicates. To address these challenges, we propose RaRe, a reasoning-aware r...
  </details>

- **2026-11-10** — Yijia Shao, Song Bian, Junxian Guo et al. — [Deep Personalization: Continuous Context Observation for Local Proactive Agents](http://arxiv.org/abs/2611.13457v1)
  <details><summary>📄 Abstract</summary>
  As AI agents become increasingly capable, users must still recognize when and how to ask for help, leaving many opportunities for useful support unrealized. Proactive agents hold the promise to close this gap, but effective proactivity requires understanding users' real-time activities and personalizing intervention timing so that assistance is offered when it is likely to be helpful rather than disruptive. We introduce deep personalization, a closed-loop process that connects continuous context...
  </details>

- **2026-11-10** — Serhii Zabolotnii, Alina Tarasova — [An AI Assistant for Automating Anti-Corruption Expertise of Draft Legislation Based on the TRACE Framework](http://arxiv.org/abs/2611.14244v1)
  <details><summary>📄 Abstract</summary>
  We present an AI assistant for automating anti-corruption expertise of draft legislation based on the TRACE architecture, designed to screen bills for corruption risks: pinpoint provisions an expert would criticise and name the regulatory defect in each. The pipeline combines a deterministic parsing core, model-guided single-provision qualification, rule-based factor assignment, and external human oversight. To evaluate the assistant, we constructed an open benchmark from the published conclusio...
  </details>

- **2026-11-10** — Chengxiao Dong, Alessio Caporali, Hongyu Lan et al. — [From Prediction to Action: Learning Physical Context for Deformable Linear Object Manipulation](http://arxiv.org/abs/2611.14274v1)
  <details><summary>📄 Abstract</summary>
  A representation that accurately predicts a deformable object's response is not necessarily the one most useful for choosing manipulation actions. We study this distinction between predictive utility and decision utility in planar single-grasp shape control of Deformable Linear Objects (DLOs). As a common decision backbone, we introduce Geometry-Pointer-Flow (GPF), a geometry-grounded policy that separates grasp-location selection from grasp-conditioned motion generation. Its geometry-only varia...
  </details>

- **2026-11-10** — Dimitris Panagopoulos, Adolfo Perrusquía, Yang Xing et al. — [Model-Free Runtime Measurement of Task-Relevant Information](http://arxiv.org/abs/2611.14111v1)
  <details><summary>📄 Abstract</summary>
  Autonomous systems increasingly monitor physical kinematics, environmental states and task completion outcomes. While existing work provides methods to plan information seeking actions and interpret acquired observations, current approaches do not monitor whether the live process of information gathering is functioning properly. Consequently, such systems can remain operationally active without resolving outstanding mission requirements. To address this limitation, we introduce Acquisition-State...
  </details>

- **2026-11-10** — Huaijin Pi, Zehong Shen, Yong Wang et al. — [DexSeed: Expanding Human Hand-Object Interactions into Robot Demonstrations for Dexterous Policy Learning](http://arxiv.org/abs/2611.14092v1)
  <details><summary>📄 Abstract</summary>
  We study how to generate diverse, physically executable robot demonstrations for dexterous vision-language-action (VLA) learning. Existing demonstration-generation methods typically rely on costly teleoperated examples. Meanwhile, human hand--object datasets provide a reusable source, but existing transfer methods mainly reproduce given interactions. Turning these interactions into VLA training data further requires coverage of different objects and manipulation locations, together with executab...
  </details>

- **2026-11-10** — Xianghui Wang, Aoran Fu, Liyou Luo et al. — [ReACT: Reflection-Consistent Modulation and Cross-Load Consistency for Humanoid Velocity Tracking Under Asymmetric Loads](http://arxiv.org/abs/2611.13929v1)
  <details><summary>📄 Abstract</summary>
  In recent years, humanoid loco-manipulation has progressed to whole-body grasping, lifting, and transport. A basic requirement underlying these tasks is carrying the object to its destination, which depends on the locomotion controller accurately executing velocity commands from the navigation policy. However, carrying an object in one hand introduces a persistent asymmetric upper-body load that can degrade velocity tracking. Persistent tracking biases can accumulate into position and heading de...
  </details>

- **2026-11-10** — Yelin He, Jiaquan Ye, Xinming Wei et al. — [WAM is capable in BEHAVIOR-1K: the 2nd-place solution to the 2026 BEHAVIOR Challenge](http://arxiv.org/abs/2611.13818v1)
  <details><summary>📄 Abstract</summary>
  This work presents the 2nd-place solution (Team IF1001) to the 2026 BEHAVIOR Challenge, which evaluates mobile manipulation across 100 household tasks. Our method is built on a powerful world action model (WAM), Cosmos 3. We improve Cosmos 3 by using richer visual history, task-progress conditioning, and task-group and skill-specific LoRA adapters. During inference, we apply a separate progress estimator to supply task-progress context, and use task- and progress-conditioned routing to select a ...
  </details>

- **2026-11-10** — Aalap D. Shah, Basil Saeed, Joshua B. Tenenbaum et al. — [A computational framework for understanding embodied plans](http://arxiv.org/abs/2611.13669v1)
  <details><summary>📄 Abstract</summary>
  Reasoning about people's plans and goals based on their actions is fundamental to human social interaction and essential for cooperative, embodied artificial intelligence. Formalizing this capacity in naturalistic, embodied settings has been a longstanding challenge. Here, we present GenEA, a novel agent representation capable of reasoning over multi-step, long-horizon embodied plans. At the heart of GenEA lies a multilevel state-space that couples the coarse biomechanics of an articulated body ...
  </details>

- **2026-11-10** — Yi Wang, Jingqiu Wu, Lei Yao et al. — [From Egocentric Human Video to Robot Manipulation in the Era of Embodied Intelligence](http://arxiv.org/abs/2611.13610v1)
  <details><summary>📄 Abstract</summary>
  Egocentric human video (EHV) records close-range hand-object interaction (HOI) and the temporal structure of everyday activities, offering a potentially scalable source of experience for robot manipulation. Using this experience for robot control requires recovering useful supervision without recorded robot actions and accounting for differences in morphology, viewpoint, and action space. We define Ego2Robot learning as the process of learning or adapting robot manipulation policies from EHV, or...
  </details>

- **2026-11-10** — Niall Dalton — [How Post-Training Influences Verbalized Algorithmic Computation in Language Models](http://arxiv.org/abs/2611.13552v1)
  <details><summary>📄 Abstract</summary>
  Post-training improves language-model reasoning, but how it changes the use of internal information and verbalized chain of thought (CoT) remains unclear. We study successive SFT, DPO, and RLVR checkpoints of Olmo-3-7B-Instruct on multi-digit addition, using carry values as known intermediate state. Probes recover carry information from internal activations with similar accuracy in SFT and RLVR, although manipulating this information does not reliably control model outputs. In contrast, the usef...
  </details>

- **2026-11-10** — Emre Kutlusan, Yongmin Li — [Medical Image Segmentation: Foundation Model Adaptation versus Task-Specific Training](http://arxiv.org/abs/2611.14519v1)
  <details><summary>📄 Abstract</summary>
  Foundation models pretrained on large natural-image collections are increasingly adapted for medical image segmentation, in the expectation that they will replace models trained for each task. Most comparisons, however, use data from the training distribution and a single task-specific baseline whose configuration is rarely justified, and therefore provide limited evidence of performance at new clinical sites. It also remains unclear how much of a foundation model must be adapted, and what deter...
  </details>

- **2026-11-10** — Megha Srivastava, Michael H. Lim, Allison M. Keys et al. — [Pyrite: Building and Benchmarking Protein-Ligand Pose Ranking Agents](http://arxiv.org/abs/2611.14511v1)
  <details><summary>📄 Abstract</summary>
  Predicting how a ligand binds to its target is central to small-molecule drug discovery. Modern cofolding models can generate diverse candidate poses, but reliably ranking these candidates remains challenging. We introduce Pyrite, a pairwise pose-ranking benchmark comprising 1,500 pose pairs across diverse protein-ligand complexes. Expert chemists equipped with 3D visualization tools and physics-based scores perform near chance, highlighting the difficulty of interpreting available chemical sign...
  </details>

- **2026-11-10** — Vagn Krister Nes Glomsrud, Mathias Bynke, Lars Henry Berge Olsen et al. — [Accurate predictions of properties of energetic materials with tabular foundation models](http://arxiv.org/abs/2611.14462v1)
  <details><summary>📄 Abstract</summary>
  We use TabPFN, a recently developed tabular foundation model, to predict three properties of energetic materials: impact sensitivity, decomposition temperature and crystal density. Without any hyperparameter tuning, TabPFN outperforms the best published models for all three properties. It also substantially outperforms a wide range of established machine-learning models, including tuned gradient boosting (XGBoost), random forests and Gaussian processes. This holds both when the models are given ...
  </details>

- **2026-11-10** — Ferran Espuny-Pujol — [Measuring Kaplan--Meier Overestimation Under Competing Risks: Event Ordering, Quantification, and Exact Inference](http://arxiv.org/abs/2611.14457v1)
  <details><summary>📄 Abstract</summary>
  Competing risks arise when individuals may experience multiple mutually exclusive event types. Competing events are frequently treated as censoring and analysed using Kaplan--Meier (KM) methods, which overestimate real-world event risks. While the existence of KM overestimation is well known, its determinants, magnitude, and inferential properties remain poorly characterised.   We develop a nonparametric framework that treats competing risks overestimation as a statistical quantity in its own ri...
  </details>

- **2026-11-10** — Sourish Gunesh Dhekane, Abinaya Kumar, Torsten Woertwein et al. — [Quantifying the Sampling Frequency Invariance of Time-Series Foundation Models for Sensor Data Applications](http://arxiv.org/abs/2611.14425v1)
  <details><summary>📄 Abstract</summary>
  Time-Series Foundation Models (TSFMs) are increasingly used in sensor applications, where sampling frequency (SF) varies across sensors, devices, and operating modes (e.g., power saving). Ideally, TSFMs must remain effective during such SF changes, provided the SF retains task-critical bandwidth. In this paper, we stress-test 4 prominent TSFMs: MOMENT, Chronos-2, Moirai-MoE, and TimesFM, to quantify their SF-invariance and investigate whether their behavior tracks the resulting loss of informati...
  </details>

- **2026-11-10** — Lucas de Souza Brandão, Gabriel da Costa Merlin, Diego Furtado Silva — [Exploring Post-Hoc Disentanglement of Audio Foundation Models for Music Similarity](http://arxiv.org/abs/2611.14415v1)
  <details><summary>📄 Abstract</summary>
  Audio foundation models like CLAP, MuQ, and MERT excel at capturing general musical similarity. On the other hand, their entangled latent spaces limit interpretability and fine-grained attribute control. Conditional Similarity Networks (CSN) address this by pairing a backbone representation model with learned masks that gate the embedding space into attribute-specific subspaces. However, existing methods train the backbone from scratch, rather than leveraging pretrained foundation models. We ins...
  </details>

- **2026-11-10** — Mohammed Nayeem Khan, Logesh L, Aliyas Ahmad Misri — [Bits or permutations? Spending a fixed inference budget on weight precision or on option-order averaging in small local language models](http://arxiv.org/abs/2611.14413v1)
  <details><summary>📄 Abstract</summary>
  Local language models can save memory by storing weights in fewer bits, and they can reduce sensitivity to the order of answer options by averaging a few reorderings. We ask whether the first makes the second worse, and which is the cheaper way to spend a fixed budget. On Qwen3-0.6B and Qwen3-1.7B with simulated round-to-nearest weight quantization (8, 6, 4 and 3 bits, fp16 reference), read from the logits of the letters A to D on ARC-Easy, ARC-Challenge, MMLU and HellaSwag (300 items each), 6 b...
  </details>

- **2026-11-10** — Bernhard Voggenberger, Christian Ganhör, Levente Zólyomi et al. — [The Unused Input: The Initial State as a Conditioning Interface for Recurrent TSFMs](http://arxiv.org/abs/2611.14357v1)
  <details><summary>📄 Abstract</summary>
  Time series foundation models (TSFMs) forecast unseen series without task-specific training. Increasingly they are built on recurrent backbones, whose constant per-step cost makes long-context inference cheap, and which, unlike transformers, carry a state. A recurrent backbone computes its prediction from two inputs: the observed context window and the initial recurrent state. In practice only the first is utilised and the initial state is unused by convention. We ask whether the initial state c...
  </details>

- **2026-11-10** — Alessio Brini — [Point-in-Time Encoders for Earnings Calls](http://arxiv.org/abs/2611.14325v1)
  <details><summary>📄 Abstract</summary>
  Text encoders turn earnings calls into vectors for search, for language models that answer from retrieved passages, and for forecasting models. A live retriever can use an encoder trained once on all available text, as finance retrievers are, but a backtest needs an encoder that read no text written after the date of each vector. To address this look-ahead bias, from 412,248 calls we train vintages under four pretraining recipes, with yearly cutoffs from 2010 to 2024, and each vintage reads only...
  </details>

- **2026-11-10** — Ezequiel Centofanti, Benjamin Remy, Emma Ayçoberry et al. — [SHINE: Shear inference environment - Generative forward modelling for radio weak gravitational lensing](http://arxiv.org/abs/2611.14301v1)
  <details><summary>📄 Abstract</summary>
  Next-generation radio interferometers, such as SKA, will observe the radio sky with unprecedented sensitivity and resolution enabling weak gravitational lensing studies using radio data, which not only complement optical observations but also probe higher redshifts. However, traditional shear estimation methods, based on measuring the ellipticity of observed galaxies, are not directly applicable to radio interferometric data. Interferometric observations are acquired in the Fourier domain, where...
  </details>

- **2026-11-10** — Yuan Zhang, Thales Bertaglia, Ralph Schroeder — [Can AI be a 'Researcher Without Borders'? Auditing Bias in AI-Assisted Social Science Research about China and the US](http://arxiv.org/abs/2611.14288v1)
  <details><summary>📄 Abstract</summary>
  Although large language models have demonstrated strong performance on algorithmic and mathematical tasks, their suitability as social science research assistants remains unclear, particularly because many social science questions lack agreed-upon, quantifiable benchmark answers. Evaluating this suitability is important since researchers and students increasingly rely on AI to generate research ideas. When questions concern the countries in which models were developed, bias may be exacerbated: D...
  </details>

- **2026-11-10** — Mehmet Onur Keskin, Berk Buzcu, Nikhil Churamani et al. — [Personalized Affective Perception via Continual Learning in Human-Agent Negotiation](http://arxiv.org/abs/2611.14247v1)
  <details><summary>📄 Abstract</summary>
  Self-interested intelligent agents that negotiate with humans should interpret nonverbal expressions and adapt their behavior accordingly. However, generic facial-affect models degrade across individuals and contexts, creating a generalization gap. We introduce an affect-adaptive negotiation strategy that incorporates Continual Learning with Imagination for Facial Expression Recognition (CLIFER) to personalize valence-arousal perception in real time. Differential feedback converts changes in val...
  </details>

- **2026-11-10** — Jack T. Parley — [Stagewise and interpretable emergence of inside-outside computation in Transformer-based language models](http://arxiv.org/abs/2611.14221v1)
  <details><summary>📄 Abstract</summary>
  Variability in syntactic structure and parsing ambiguity are fundamental aspects of natural language which modern LLMs have to learn to deal with proficiently. Previous "post-mortem" studies have shown that fully trained Transformers indeed approximate canonical parsing algorithms such as inside-outside, but little is established theoretically about how this is actually learned. Here, we make a first step towards addressing this by studying the learning dynamics in synthetic context-free grammar...
  </details>

- **2026-11-10** — Geunsoo Jang, K. Selçuk Candan, Gerardo Chowell — [Benchmarking large language models for parameter-level structural identifiability classification in epidemic ODE models](http://arxiv.org/abs/2611.14184v1)
  <details><summary>📄 Abstract</summary>
  Structural identifiability determines whether unknown parameters can be uniquely recovered from ideal model outputs, making it a prerequisite for interpreting parameter estimates. We evaluated whether large language models (LLMs) can reliably provide preliminary structural identifiability classifications for epidemic models. We constructed a retrospective benchmark of 88 scenarios from 14 of the 27 studies considered, encompassing 696 parameter-level formal reference classifications from publish...
  </details>

- **2026-11-10** — Shenxi Liu, Yiwei Li, Mingyang Zhao et al. — [BARS: Budget-Aware Sequential Sampling with Refusal for Majority Identification under Unknown Distributions](http://arxiv.org/abs/2611.14171v1)
  <details><summary>📄 Abstract</summary>
  Repeated sampling with majority selection is an effective means of enforcing self-consistency in large language models. Recently, a variant has also been introduced that terminates early to save costs when the output distribution is favorable. But it still cannot yield a correct confidence estimate from the answer distribution. For this issue, we formalize this as majority identification under an unknown distribution with a budget and a target error rate, and propose BARS, a sequential rule cert...
  </details>

- **2026-11-10** — Haohang Huang, Xuan Lu, Mingjin Kuai et al. — [From Search to Decision: How Post-Training Shapes Information-Seeking Capabilities in Large Language Models](http://arxiv.org/abs/2611.14149v1)
  <details><summary>📄 Abstract</summary>
  Information seeking in large language model (LLM) systems increasingly involves decisions about when to acquire information, where to search, and how to evaluate and use evidence. Recent post-training methods have improved several such behaviors, but their objectives and evaluations span different tasks and system settings. This paper organizes research around six interrelated information-seeking capabilities and examines the learning signals, optimization methods, update loci, and credit-assign...
  </details>

- **2026-11-10** — Federico Ravenda, Mirko Cesarini, Daniele Montagnani et al. — [Hx2Dx: From Anamnesis to Diagnosis - A Multimodal Arena for Conversational Clinical Reasoning in LLMs](http://arxiv.org/abs/2611.14122v1)
  <details><summary>📄 Abstract</summary>
  Large language models (LLMs) achieve expert-level diagnostic accuracy in static evaluations, where the model receives a curated vignette or case report that already condenses the diagnostically relevant findings. Such evaluations measure inference over already selected evidence; the evaluations do not account for the inquiry used to obtain it. In clinical practice, however, diagnosis is an iterative process of inquiry. Clinicians take the patient's history, or anamnesis (Hx), through targeted qu...
  </details>

- **2026-11-10** — Yuanhe Tian, Yan Song — [Looking One Step Ahead: An Anticipation-guided Agent for Object State Readout in Videos](http://arxiv.org/abs/2611.14113v1)
  <details><summary>📄 Abstract</summary>
  Understanding the progress of an activity requires tracking how the objects involved change over time. Object state readout provides this information by describing a target object's states and transitions across video frames. Although multimodal large language models (MLLMs) generate detailed visual descriptions, these descriptions may leave the attributes needed to distinguish successive states insufficiently specified. In this paper, we propose look-ahead state readout (LASER), an anticipation...
  </details>

- **2026-11-10** — Dave Murray-Rust, Elisa Giaccardi, Federico Bomba et al. — [From Bias to Positionality: A critical grammar for Large Language Models](http://arxiv.org/abs/2611.14079v1)
  <details><summary>📄 Abstract</summary>
  Bias has become a default lens for understanding what machine learning systems do and how we should relate to them. Bias is at root a deviation from a standard; in decision making systems we can supply a standard from outside: a law, a protected attribute, a benchmark, a statistical property. However, even there, biased is often used as a shorthand, without stating what the position taken is - a silent ``relative to''. In a general use of language models, nothing supplies the standard: there is ...
  </details>

- **2026-11-10** — Zhikun Tao, Fangyong Jin, Junping Zhao — [Can KV Cache Be Reused Across Model Updates? A DeepSeek-V4-Flash Case Study](http://arxiv.org/abs/2611.14051v1)
  <details><summary>📄 Abstract</summary>
  Reusing key--value (KV) caches across language model updates could avoid repeated computation of shared context, but changes in model weights raise a fundamental question about what these caches preserve. We investigate direct cache reuse across four model updates, with a detailed study of DeepSeek-V4-Flash to Flash-0731. Our central finding is that caches can retain useful task information without faithfully reproducing the updated model's behavior. Retrieval accuracy varies substantially acros...
  </details>

- **2026-11-10** — Wei Gu, Weiwei Qi, Jiajun Tang et al. — [TreeAgent: Structure-Aware Memory Agent for Processing Long Hierarchical Data](http://arxiv.org/abs/2611.13946v1)
  <details><summary>📄 Abstract</summary>
  Practical Web applications increasingly require agents to interpret long conversations or documents. For inputs exceeding the context windows of large language models (LLMs), memory agents process segments sequentially and retain past information in bounded memory. However, they typically divide inputs into flat token segments without preserving structure or hierarchy, causing three limitations for structured data such as API responses or HTML documents. First, fixed-length segmentation can spli...
  </details>

- **2026-11-10** — Haowei Cheng, Milhan Kim, Bowen Jiang et al. — [OpenRE-Bench: A Benchmark Harness for Multi-Agent Requirements Engineering with Mined GitHub Issues](http://arxiv.org/abs/2611.13925v1)
  <details><summary>📄 Abstract</summary>
  OpenRE-Bench is an open-source benchmarking infrastructure for large language model (LLM) based multi-agent requirements-engineering (RE) frameworks. Such frameworks are increasingly common, but they use different agent roles, negotiation policies, and output shapes, and are typically evaluated on their own runtimes, metrics, and small sets of curated system descriptions, which makes fair, reproducible comparison difficult. OpenRE-Bench addresses this with four reusable pieces: a shared run harn...
  </details>

- **2026-11-10** — Vojtech Cahlik, Amir Reza Mohammadi, Rodrigo Alves et al. — [From Counterfactual Edits to Human Narratives: LLM-Driven Interpretations for Recommender System Explanations](http://arxiv.org/abs/2611.13914v1)
  <details><summary>📄 Abstract</summary>
  Recommender systems increasingly influence what users discover and consume online, yet the decision logic behind their outputs often remains opaque. Counterfactual explanation (CFX) methods provide an effective way to show which changes to a user's interaction history would alter a recommendation. In recommendation settings, however, CFXs often require many edits, producing long, low-level lists that are hard for users to interpret. Moreover, most evaluations emphasize edit counts while largely ...
  </details>

- **2026-11-10** — Guangyu Wang, Xiaodong Ma, Xinming Wu — [Adapting a Vision Foundation Model for Fracture Characterization in Acoustic Image Logs](http://arxiv.org/abs/2611.13911v1)
  <details><summary>📄 Abstract</summary>
  Natural fractures (NFs) and drilling-induced tensile fractures (DITFs) in acoustic image logs provide insights into rock mass structure and in situ stress, but manual characterization is time-consuming. Deep learning can automate this task, although expert-labeled data are scarce. We investigate whether adapting a pretrained vision foundation model (VFM) outperforms task-specific models trained from scratch with limited annotations. Using 80 annotated acoustic image samples, we fine-tuned DINOv3...
  </details>

- **2026-11-10** — Lorenzo Cirillo, Irene Amerini, Andrea Cavallaro — [Mechanistic Interpretability of Deep Neural Networks: Methods, Frameworks, and Perspectives](http://arxiv.org/abs/2611.13868v1)
  <details><summary>📄 Abstract</summary>
  Deep neural networks underpin fundamental tasks in a wide range of signal domains, such as image, audio, and language processing. However, their internal mechanisms are notably difficult to interpret. Internal activations are structured signals transformed across layers that may encode a multitude of interdependent relationships, as individual neurons frequently represent multiple underlying concepts. Mechanistic interpretability aims to uncover the internal mechanisms of neural networks by iden...
  </details>

- **2026-11-10** — Teysir Baoueb, Leonardo Boulitreau de Menezes Martins Marques, Paraskevas Stamatiadis et al. — [MusicFlux: Flexible Conditioning for Text-Guided Music Generation and Editing](http://arxiv.org/abs/2611.13834v1)
  <details><summary>📄 Abstract</summary>
  Music editing transforms existing recordings while preserving their original attributes. Recent approaches adapt pretrained text-to-music models for tasks like inpainting, event insertion, or restoration by conditioning them with context audio. It was recently proposed for image editing to unify generation and editing by treating the source image as in-context information. However, applying this directly to music is computationally expensive due to long audio sequences. In this work, we develop ...
  </details>

- **2026-11-10** — Mohd Tahseen, Vivekanand Dabade — [Elastic Landau states as martensite nuclei in austenite](http://arxiv.org/abs/2611.13816v1)
  <details><summary>📄 Abstract</summary>
  In this article, we investigate the geometric closure of austenite--martensite interfaces. Classical compatibility conditions permit stress-free interfaces between the two phases: the condition $λ_2 = 1$ admits planar interfaces, whereas the cofactor conditions additionally admit curved interfaces. However, neither, guarantees the geometric closure of these interfaces. We identify two-parameter families of martensitic deformations that overcome this limitation and enable the formation of closed,...
  </details>

- **2026-11-10** — Donghun Ryu, Seokhyun Kim, Minhyeok Lee — [FastWild-GS: Minutes-Scale In-the-Wild Gaussian Splatting via Compact Per-Image Appearance Adaptation](http://arxiv.org/abs/2611.13808v1)
  <details><summary>📄 Abstract</summary>
  Internet photos of a scene differ in exposure, illumination and transient objects such as passers-by, so one set of Gaussian colours cannot explain all photos (the in-the-wild setting). Recent in-the-wild Gaussian Splatting methods mostly report hours of per-scene optimization. We present FastWild-GS, which describes each photo by a 128-dimensional Photo Appearance Token and a per-channel transform, a scale and an offset applied to the rendered image (six parameters); a small MLP predicts the co...
  </details>

- **2026-11-10** — Andrew P. Kels, Masahito Yamazaki — [Elliptic hypergeometric sum/integrals for orthogonal groups and Seiberg duality on the lens space](http://arxiv.org/abs/2611.13803v1)
  <details><summary>📄 Abstract</summary>
  We derive new transformation formulas for elliptic hypergeometric sum/integrals associated with the orthogonal groups $\mathrm{SO}(N)$. The sum/integrals are written in terms of the lens elliptic gamma function, which depends on an integer $r\geq 1$ in addition to the usual complex variables, and they reduce to the elliptic hypergeometric integrals of Spiridonov and Vartanov for $r=1$. The derivation uses the $BC_n\leftrightarrow BC_{\tilde n}$ transformation formula proven in our previous paper...
  </details>

- **2026-11-10** — Fabio Bonsignorio, Elisabetta Barletta, Sorin Dragomir et al. — [Softness is something you also need! Why compliance helps control: information metrics of a passive walker with compliant ankle](http://arxiv.org/abs/2611.13779v1)
  <details><summary>📄 Abstract</summary>
  A great gap in adaptivity, flexibility, and dexterity still exists between intelligent robots, whether they are made of rigid or (partially) compliant components, and their naturally evolved animal and vegetal counterparts. One reason could be of `paradigm' nature. On the one hand, most robots (both rigid and soft) are still designed by following a `Cartesian' approach, with top-down control and a clear mind-body separation. Designing artificial agents on the basis of the principles that we obse...
  </details>

- **2026-11-10** — Karl Friedrich Siburg — [Berry phase and Hannay angle as Taylor coefficients of the minimal action](http://arxiv.org/abs/2611.13702v1)
  <details><summary>📄 Abstract</summary>
  For a Hamiltonian system with one degree of freedom whose parameters are varied slowly around a closed loop, with slowness $δ$, we study the minimal action $β_δ$ of the resulting time-periodic system and its convex conjugate, Mather's $α$-function $α_δ$, both normalized per unit time. The cycle map of such a system is an area-preserving map of the cylinder which in general is not integrable. We prove that $β_δ(ρ)$ and $α_δ(c)$ have asymptotic expansions in $δ$ to every finite order, locally unif...
  </details>

- **2026-11-10** — Huixue Han, Jiaying Liu — [Compute the Interactions, Not the Attributes: What a Fact Layer Must Supply in the Chinese Sexagenary System](http://arxiv.org/abs/2611.13597v1)
  <details><summary>📄 Abstract</summary>
  Language-model systems in rule-governed domains often pair the model with a deterministic fact layer, but which facts that layer should supply is rarely measured. We measure it in the Chinese sexagenary system underlying BaZi chart analysis, where every fact has one table-checkable value: 682 items over twelve fact categories and 160 transit--natal collision items, posed closed-book, with the reference table, and with computed facts at increasing levels. In eleven open-weight models answering di...
  </details>

- **2026-11-10** — Jifan Gao, Junjie Hu, John Caskey et al. — [A Concept-Based Interpretable Framework for Clinical Text-based Prediction via Token-Concept Attention without Concept Supervision](http://arxiv.org/abs/2611.13564v1)
  <details><summary>📄 Abstract</summary>
  Objective: Concept-based interpretation has emerged as a promising approach for explaining blackbox models using human-understandable, high-level concepts. However, most existing methods require annotated concept labels to train the model to identify concepts in the input, and obtaining such annotations in clinical text is often expensive. This study aims to enable concept-based interpretation for language models without concept supervision on clinical prediction tasks. Methods: We propose a nov...
  </details>

- **2026-11-10** — Zhiqun Zhao, Xiaodong Yang, Bruce Gu et al. — [An evidence-traceable benchmark of clinical reasoning in large language models](http://arxiv.org/abs/2611.13562v1)
  <details><summary>📄 Abstract</summary>
  Benchmark scores for medical large language models (LLMs) are difficult to interpret when scoring criteria cannot be traced to clinical evidence. Here we developed Med Evidence Bench (MEB; https://www.medevidencebench.org.cn/), comprising 1,536 physician-constructed items across three levels: guideline knowledge, standardized clinical scenarios and real-world laboratory scenarios. Each criterion stating a medical claim is linked to a versioned source-text span. Across ten LLMs, the Evidence Trac...
  </details>

- **2026-11-10** — Boyoung Kwon, Jiyoon Seo, Sang Ho Lee — [Discovering Structurally Plausible and Interpretable Cognitive Models with Large Language Models](http://arxiv.org/abs/2611.13561v1)
  <details><summary>📄 Abstract</summary>
  Computational cognitive modeling has traditionally relied on manual model construction, which is a time-intensive process that requires substantial domain expertise. Although recent LLM-based approaches have begun to automate model generation, they often prioritize predictive accuracy at the expense of structural plausibility and parameter identifiability. We introduce DisCo, an LLM-guided framework that discovers interpretable symbolic cognitive models through evolutionary search with two struc...
  </details>

- **2026-11-10** — Ed deHaan, Allen H. Huang — [Tabular Foundation Models in Financial Predictions](http://arxiv.org/abs/2611.13550v1)
  <details><summary>📄 Abstract</summary>
  This technical note introduces tabular foundation models (TFMs) to accounting research and evaluates their performance in one common benchmark task: predicting firms' next-year earnings changes. TFMs produce numeric predictions and learn in context, without post-release training or tuning, making them natural and easy to use for forecasting. The TFMs we study are pretrained on synthetic tabular data, so they avoid look-ahead bias from memorizing firms' outcomes. We compare Google Research's TabF...
  </details>

- **2026-11-10** — Mahdi Nazemi, Oleg Rybakov, Tijmen Blankevoort et al. — [Closing the BF16-FP16 Convergence Speed Gap in RL Post-Training with Stochastic Rounding](http://arxiv.org/abs/2611.13545v1)
  <details><summary>📄 Abstract</summary>
  BF16 is widely used to pretrain large language models because it has the same dynamic range as FP32 and converges similarly to FP32 training. However, in reinforcement learning with verifiable rewards, where learning rates are typically low, we find that standard mixed-precision BF16 training converges more slowly than FP16 training at the same learning rate. We attribute this gap to weight sticking: when FP32 shadow weights are quantized to BF16 using round-to-nearest, small updates often leave...
  </details>

- **2026-11-10** — Jeevan Neupane, Janardan Bhetwal, Kshitiz Paudel et al. — [Nepali-English Code-Mixed Speech Recognition: Data Preparation and Adaptation of a Speech Foundation Model](http://arxiv.org/abs/2611.13512v1)
  <details><summary>📄 Abstract</summary>
  Nepali speakers regularly mix English words into conversation, but multilingual speech recognisers often struggle with language switches and the writing script used for English words. We study how to adapt SraVaani, a 449M-parameter hybrid TDT-CTC model, using a 172.8-hour corpus covering six Nepali speech domains. Its pretrained tokenizer does not support digits and several common symbols. Rather than replace it or discard these recordings, we generate Nepali and English readings for numbers an...
  </details>

- **2026-11-10** — Erfan Baghaei Potraghloo, Milad Heidari Sorkhehdizaj, Shahab Rahimirad et al. — [Free Lunch Uncertainty: Sequence-Level Rényi Entropy from Particle Decoding for Adaptive LLM Reasoning](http://arxiv.org/abs/2611.13414v1)
  <details><summary>📄 Abstract</summary>
  Quantifying uncertainty over an entire LLM completion is critical for selective prediction and adaptive compute. Zero-cost signals such as mean token entropy and log-probability are local to tokens or to one completion, and self-consistency needs many extra completions. We show that Sequential Monte Carlo (SMC) decoding for power sampling already estimates the normalizing constant of the power distribution, which gives the sequence-level R'enyi entropy (SRE) of the model's completion distributio...
  </details>

- **2026-11-10** — Antoinette Stone, Ruoning Zhang, Brian Utter — [AI is ready, but are the students. From answer-making to sense-making](http://arxiv.org/abs/2611.13404v1)
  <details><summary>📄 Abstract</summary>
  Students in introductory physics often struggle with interpreting kinematics graphs, especially when connecting graphical features to physical meaning. We investigated AI tool use in kinematic graphing analysis as an intervention to support active sensemaking. This study examines GPT-5 performance on the Test of Understanding Graphs in Kinematics (TUG-K) and the way students interacted with GPT-5 during introductory physics activities involving graphical analysis. For the first part of the study...
  </details>

- **2026-11-10** — Freek Byrman, Partha Das, Stijn Verdenius et al. — [How Hyperbolic Are Hyperbolic Vision-Language Models?](http://arxiv.org/abs/2611.13384v1)
  <details><summary>📄 Abstract</summary>
  Hyperbolic vision-language models (VLMs) have emerged as a rapidly growing area of research, reporting strong zero-shot performance alongside an interpretable embedding space in which radius orders representations by generality. But how hyperbolic are hyperbolic VLMs in practice? We investigate this at the exponential map, the single operation through which curvature enters an otherwise Euclidean network. We show that across MERU, HyCoCLIP, ARGENT, and PHyCLIP, the exponential map is well approx...
  </details>

- **2026-11-09** — Josip Vrdoljak, Akash Singh, Bas Steunebrink et al. — [ExpertCrowd-SWE: Measuring Frontier Coding Agents on Expert-Authored Engineering Tasks in Unfamiliar Codebases](http://arxiv.org/abs/2611.13246v1)
  <details><summary>📄 Abstract</summary>
  ExpertCrowd-SWE (EC-SWE) is a benchmark of 100 expert-authored, multi-file software engineering tasks for evaluating autonomous coding agents in large, unfamiliar codebases. Each task is a change request written by a practising engineer against a pinned commit of a real repository, paired with a sealed reference solution and a task-specific grader whose weighted, mostly executable criteria award partial credit; must-pass blockers and pass/fail gates encode what a maintainer would refuse to merge...
  </details>

- **2026-11-09** — Delin Zhao, Zhengrong Yue, Junlin He et al. — [RoboACE: Adversarial Co-Evolution for Robot Self-Improvement](http://arxiv.org/abs/2611.13034v1)
  <details><summary>📄 Abstract</summary>
  Robot agents can improve reusable skills, planning procedures, and recovery strategies from execution feedback, yet a fixed practice source leaves the search for new weaknesses unchanged. Useful practice depends on the agent's current capabilities, so the procedure that chooses practice must also be revisable. We present RoboACE (Robot Adversarial Co-Evolution), a framework that jointly evolves curriculum and execution harnesses around frozen foundation models. The curriculum harness uses accumu...
  </details>

- **2026-11-09** — Bogdan Mamaev, Qizhou Wang, Christopher Leckie et al. — [Measuring Definition Sensitivity in LLM Annotation of Social Science Concepts](http://arxiv.org/abs/2611.13339v1)
  <details><summary>📄 Abstract</summary>
  In social science research, text annotation is a fundamental task that is traditionally a costly, hard-to-scale manual process. Researchers have used large language models (LLMs) to perform annotation by writing a definition of a concept into a prompt - a rule that determines whether a label should be attributed to a text depending on its content. However, concepts such as hate speech, fake news, and terrorism typically have several theoretically defensible competing definitions. It is also unkn...
  </details>

- **2026-11-09** — Zhaoyi Liu, Haichuan Zhang, Xiaochuan Gong et al. — [Disentangling Multimodal Rotary Positional Embedding in Vision-Language Models](http://arxiv.org/abs/2611.13334v1)
  <details><summary>📄 Abstract</summary>
  Vision-language models widely adopt Multimodal Rotary Position Embedding (MRoPE), an extension of Rotary Position Embedding (RoPE) that incorporates temporal, height, and width axes to encode the spatial structure of visual tokens. However, MRoPE also assigns height and width coordinates to text tokens that lack inherent spatial structure, introducing spatial positional effects into text-vision attention. Existing MRoPE variants explore different frequency allocations and coordinate layouts, wit...
  </details>

- **2026-11-09** — Xiang Fang, Wanlong Fang, Junhao Dong et al. — [ABRR: Transforming Temporal Sentence Grounding with Wasserstein-Adaptive Refinement and Precision Ranking](http://arxiv.org/abs/2611.13310v1)
  <details><summary>📄 Abstract</summary>
  Temporal Sentence Grounding (TSG) aims to localize temporal segments in untrimmed videos that correspond to natural language queries, a critical task for video understanding with applications in video retrieval, summarization, and human-computer interaction. Despite significant progress driven by transformer-based models, existing TSG methods suffer from two key limitations: quantization errors due to temporal downsampling, which misalign segment boundaries, and suboptimal ranking of predictions...
  </details>

- **2026-11-09** — Michelle Ho, Maximilian Adang, Zachary Booth et al. — [Large Language Model Explainability for Planning Lunar Rover Trajectories under Uncertainty](http://arxiv.org/abs/2611.13292v1)
  <details><summary>📄 Abstract</summary>
  Planning planetary rover trajectories under probabilistic uncertainty is a multi-objective optimization problem that science teams currently iteratively solve and verify by hand. This process becomes impractical when timelines and constraints frequently shift throughout the mission planning phase. Sampling-based planners such as Monte Carlo tree search can speed up this process, but their outputs do not preserve traceability to the science objectives that justify each plan, which the science tea...
  </details>

- **2026-11-09** — Yunpeng Xiao, Yuzhang Xie, Junhao Huang et al. — [Decisions by Discrimination: Differential Evidence for Medical Reasoning](http://arxiv.org/abs/2611.13233v1)
  <details><summary>📄 Abstract</summary>
  Large language models (LLMs) are increasingly studied for clinical decision support, and medical question answering provides a testbed for evaluating this capability. In particular, medical multiple-choice questions (MCQs) reflect a core challenge in clinical decision-making: plausible options often share overlapping evidence, while only a few decisive factors distinguish the correct option from incorrect ones. However, existing retrieval-based and reasoning-oriented methods mainly focus on supp...
  </details>

- **2026-11-09** — Daofu Zhang, Qingcheng Zeng, Chunwei Liu et al. — [ARoute: Task-Aligned Batch and Streaming Model Routing](http://arxiv.org/abs/2611.13209v1)
  <details><summary>📄 Abstract</summary>
  Language models increasingly power data-intensive applications, from semantic data processing to question answering and agentic workflows. Using frontier models for every request is prohibitively expensive, while relying only on smaller models reduces accuracy. We study model routing under a user-specified cost budget, aiming to maximize accuracy under task-specific correctness criteria. Existing routers fall short in two ways: pretrained routers rely on generic preference signals that may not r...
  </details>

- **2026-11-09** — Lingzhi Shen, Xiaohao Cai, Yunfei Long et al. — [HiCAP: Hierarchical Cultural Adaptation via Personality for Dialogue Generation](http://arxiv.org/abs/2611.13207v1)
  <details><summary>📄 Abstract</summary>
  Cultural adaptation in dialogue systems refers to the ability to generate responses that conform to linguistic norms and social expectations across different cultures. However, existing dialogue generation approaches pay limited attention to the role of personality in shaping cultural expression and communication style. We therefore propose HiCAP, a novel framework that integrates personality traits into culturally adaptive dialogue generation. HiCAP employs a personality-conditioned control mec...
  </details>

- **2026-11-09** — Sepideh Ravanbakhsh, Hamidreza Moradi — [Cognitive Multi-Agent Search and Rescue: Language-Grounded Hierarchical Reinforcement Learning for Collaborative Robotics](http://arxiv.org/abs/2611.13161v1)
  <details><summary>📄 Abstract</summary>
  Effective search and rescue (SAR) operations require autonomous systems capable of coordinating multiple heterogeneous agents, adapting to dynamic hazards, and aligning with human mission intent. Existing language-guided reinforcement learning (RL) methods primarily focus on single-agent instruction following and lack mechanisms for team-level coordination in complex, partially observable environments. This paper presents a Cognitive Multi-Agent Framework based on Language-Grounded Hierarchical ...
  </details>

- **2026-11-09** — Lluís Arola-Fernández, Aissam Khadraoui, Alex Arenas — [Everything in its right place: attention is a radio head](http://arxiv.org/abs/2611.13146v1)
  <details><summary>📄 Abstract</summary>
  Attention, the core of language models, is a digital calculation over tokens: an exponential selects them, a division normalizes and a positional code sets the order. We show that attention can instead emerge from the synchronization of a receiver with its context tokens. Each past token is an oscillator whose state carries its content and whose frequency drifts with its age. The present token selects them by content, aligning an antenna with its query, and by position, setting the frequency of ...
  </details>

- **2026-11-09** — Johin Johny Arimbur, Ankur Ashit Ghosh, Shervin Sam — [The Indic Token Tax in 2026: Measuring Tokenizer. Disparity and Its Cost for the Languages of India](http://arxiv.org/abs/2611.13058v1)
  <details><summary>📄 Abstract</summary>
  Commercial language model APIs bill per token, so a tokenizer that needs more tokens for the same content in one language makes that language more expensive, slower, and able to fit less text in a fixed context window. We measure this disparity for nine public tokenizers, including those of GPT-4, GPT-4o, Qwen2.5, DeepSeek-V3, Mistral-Nemo and four Sarvam models, on all 25 languages of India available in FLORES-200 (2,009 professionally translated sentences aligned with English) and on 13,732 hu...
  </details>

- **2026-11-09** — Pengkun Wang, Rui Mao, Zhe Zhao et al. — [ChipOmni: A General-Purpose AI Agent for Electronic Design Automation](http://arxiv.org/abs/2611.13020v1)
  <details><summary>📄 Abstract</summary>
  Electronic design automation (EDA) workflows remain highly fragmented, requiring engineers to coordinate heterogeneous representations, specialised software tools, and iterative verification across multiple design stages. Although large language models have brought more general reasoning and code-generation capabilities to EDA, many existing approaches remain focused on isolated tasks and struggle to plan, verify, and repair designs autonomously within executable engineering environments. Here w...
  </details>

- **2026-11-09** — Duy Anh Nguyen, Trung Dung Ngo — [Force-Closure Condition for Cooperative Multi-robot Pushing of Rectangular Objects](http://arxiv.org/abs/2611.13268v1)
  <details><summary>📄 Abstract</summary>
  In cooperative object manipulation, the placement of pushing contacts determines whether force closure can be achieved and agents can generate arbitrary forces and torques on the object correspondingly. This study derives a necessary and sufficient closed-form condition for the planar force closure of a rectangular object, a common object shape in everyday settings, under four frictionless pushing contacts. For a rectangle of length $b$ and width $a$, force closure holds if and only if $(l_1+l_3...
  </details>

- **2026-11-09** — Shiki Iwase — [Fastener-centric acquisition and AND/OR graph representation of state-dependent disassembly knowledge from CAD-derived virtual assemblies](http://arxiv.org/abs/2611.13379v1)
  <details><summary>📄 Abstract</summary>
  Design-stage disassemblability assessment requires knowledge of product structure and the operations available in each assembly state, but CAD assemblies do not directly specify state-dependent disassembly operations. This paper proposes a fastener-centric virtual-disassembly framework that acquires such knowledge from CAD-derived virtual assemblies. Fasteners jointly releasing the same constraint are grouped into operation-level sets, avoiding enumeration of arbitrary individual-fastener orders...
  </details>

- **2026-11-09** — Andrea Martínez Pacheco, Sara Rodríguez Corvillo, Alberto Rivera-Calzada et al. — [Hysteresis and mode switching in FIB engineered random laser diodes](http://arxiv.org/abs/2611.13328v1)
  <details><summary>📄 Abstract</summary>
  Complex dynamical behavior in laser diodes is commonly induced by external perturbations such as optical or optoelectronic feedback and optical injection. The structural transformation of a stable laser diode into a stand-alone nonlinear dynamical system would provide a practical alternative as a single and compact device. Here we demonstrate the fabrication of such a device by milling, via focused ion beam, the output facet of a Fabry-Perot laser diode with a predesigned mask, obtaining a scatt...
  </details>

- **2026-11-09** — Komal Thareja, Mats Rynge, Berent Aldikacti et al. — [PegasusAI Studio: Legible Cyberinfrastructure and Accountable AI Agents for Scientific Workflows](http://arxiv.org/abs/2611.13309v1)
  <details><summary>📄 Abstract</summary>
  AI coding agents can now construct scientific workflows, but operating them on shared cyberinfrastructure (CI) raises problems that code generation does not solve. Agents need current knowledge of the workflow system and its execution sites and access to the runtime state of distributed executions, while facilities need to attribute every agent action to a user and bound it by that user's privileges. We present PegasusAI Studio, an AI-assisted science gateway built on the Pegasus and HTCondor st...
  </details>

- **2026-11-09** — Jiamin He, Mark Rowland, Zhaohan Daniel Guo et al. — [Off-policy Learning with Excursion Policies](http://arxiv.org/abs/2611.13275v1)
  <details><summary>📄 Abstract</summary>
  Off-policy reinforcement learning (RL) tries to learn the value of a target policy while data comes from a different behavior policy. This often requires trading off bias for variance or stability. One way to trade these off is to linearly interpolate between the behavior and target policies, but this represents only one point in a broader space of interpolation mechanisms. We introduce excursion policies--a structured alternative where the agent follows the target policy for a multi-step "excur...
  </details>

- **2026-11-09** — Melody Zixuan Li, Taylor Webb — [What drives the emergence of symbolic mechanisms in large language models?](http://arxiv.org/abs/2611.13270v1)
  <details><summary>📄 Abstract</summary>
  Recent work has identified a set of emergent symbolic mechanisms that support abstract reasoning in large language models, but it remains unclear what factors drive the emergence of these mechanisms. To address this question, we trained neural networks from scratch on abstract sequence tasks, varying both architectural and data distributional factors, and investigated the effects of these factors on the emergence of symbolic mechanisms. Using representational, attentional, and causal mediation a...
  </details>

- **2026-11-09** — Madhu Sudhan Rao Beesetty — [Agreeing on the Answer but Not the Reason: Measurement Limits of LLM Reasoning Failure Taxonomies](http://arxiv.org/abs/2611.13140v1)
  <details><summary>📄 Abstract</summary>
  Failure taxonomies for LLM reasoning are increasingly reported as measurements: papers state what fraction of a model's errors fall into named categories, then compare those fractions across models. We show that for one such category the reported fraction is largely a property of the measurement procedure. We defined Compositional Collapse (a model notices a required sub-part of a problem, then drops or misapplies it) and measured it across twelve models and eleven languages on a public multilin...
  </details>

- **2026-11-09** — Ronnie Andrews, Alain Connes, Antonio La Gatta — [The uncertainty operator, the Weil ground state and the zeros of zeta: a numerical study and conditional positivity of the Weil quadratic form](http://arxiv.org/abs/2611.13129v1)
  <details><summary>📄 Abstract</summary>
  Applying the Dirichlet principle to the Weil quadratic form $QW_λ$ on $L^2([λ^{-1},λ],d^*u)$--using only the primes $p\leλ^2$ of the Euler product--yields canonical finite-dimensional Hermitian matrices whose ground state has a Mellin transform with zeros proved real in full generality when the lowest eigenvalue is simple and even. While $λ^2=13$ gave $50$ zeros of $ζ$, $λ^2=250$ ($λ\sim16$) gives the first $1000$ zeros with $>500$ correct decimals (the first with $1341$). We explain this via a ...
  </details>

- **2026-11-09** — Erik Derner, Jiří Kubalík, Robert Babuška — [ASPIRE: An Agentic System-Identification Platform for Iterative Reasoning and Exploration](http://arxiv.org/abs/2611.13114v1)
  <details><summary>📄 Abstract</summary>
  System identification requires expert decisions on the identification method, incorporation of prior physical knowledge, and model validation. We propose ASPIRE, a framework for nonlinear system identification in which a large language model agent selects and executes the identification method. ASPIRE constructs closed-form, nonlinear static or dynamic models from measured data, optionally supplemented by a system description, the intended use of the model, and physical requirements expressed fo...
  </details>

- **2026-11-09** — György Eigner, Patrik P. Süli, Roland Hollós — [Trust, but verify, audit and attribute: a human-in-the-loop framework for checking AI-produced research results](http://arxiv.org/abs/2611.13042v1)
  <details><summary>📄 Abstract</summary>
  Artificial intelligence (AI) systems now produce research results in bulk: in October 2026 a single laboratory released more than 700 AI-generated mathematics manuscripts, only part of them with machine-checked proofs. Such volumes will be checked mostly by AI agents that call specialised software. A passing check certifies only the artefact that was checked. For proofs translated into the proof assistant Lean, it has been shown that this artefact may state something other than the author's text...
  </details>

- **2026-11-09** — Jiajun Chen, Shicheng Fang, Jiahao Lu et al. — [GTAGym: Real AAA Game Tasks Environment for Evaluation and Reinforcement Learning](http://arxiv.org/abs/2611.13028v1)
  <details><summary>📄 Abstract</summary>
  AAA games offer a rich testbed for evaluating agent perception, reasoning, and control. However, evaluating whether agents can complete tasks in AAA games is challenging and often human-annotated because task outcomes are often difficult to verify automatically, let alone applying it for Reinforcement Learning (RL). We introduce GTAGym, an environment and framework for evaluation and RL on GTA V tasks. Its evaluation benchmark, GTAVBench, derived from GTA V main-story missions, contains 103 onli...
  </details>

- **2026-11-09** — Zhenyuan Chen, Wenshuo Tao, Zhuo Huang et al. — [When to Trust Adaptation: Contextual Fusion for Transferable Vision-Language Prompting](http://arxiv.org/abs/2611.11824v2)
  <details><summary>📄 Abstract</summary>
  When a vision-language model encounters a new class or domain, how much should it trust its learned prompts? Because source adaptation can correct pretrained errors on some target images while disturbing valid predictions on others, we introduce Contextual Adaptive Fusion (CAF), which retains four prediction branches by pairing frozen and prompted visual and textual representations. To arbitrate when branches disagree on an image, CAF combines each branch's predictive confidence with how frequen...
  </details>

- **2026-11-09** — Erik Hoel — [Qualiaphobic artificial neural networks (and why to build them)](http://arxiv.org/abs/2611.12809v1)
  <details><summary>📄 Abstract</summary>
  This paper introduces qualiaphobic AI: artificial neural network architectures that are hostile to theories of consciousness. I show that qualiaphobia can be well-justified by knowledge about theories of consciousness, like when such theories are trivial or unfalsifiable or contradicted by overwhelming scientific evidence. It can also be justified by how theories of consciousness must be grounded in phenomenology, as well as how current popular theories of consciousness are applied to AI. I iden...
  </details>

- **2026-11-09** — Md Anwar Hossen, Ali Jannesari — [FireGate: Bounding Behaviour Change Before Training in Continual RL Fine-Tuning](http://arxiv.org/abs/2611.11979v1)
  <details><summary>📄 Abstract</summary>
  Fine-tuning a deployed language model on one task after another can change behaviour that should stay fixed, such as earlier skills, general chat or refusals. Today, such forgetting is found only after training, on the benchmarks someone chose to run. This work bounds, before training, how often its outputs change on chosen prompt distributions. FireGate places each task's update, such as a new LoRA, behind a gate, which is a classifier on the model's frozen lower layers that decides for each pr...
  </details>

- **2026-11-09** — Zhaoying Pan, Shenyu Lu, Jun Hui Wong et al. — [Beyond Modality Preference: Controlling Multimodal Arbitration under Modality Conflict in MLLMs](http://arxiv.org/abs/2611.12883v1)
  <details><summary>📄 Abstract</summary>
  Multimodal large language models (MLLMs) integrate information across modalities, but become unreliable when those modalities disagree. Under conflicting inputs, MLLMs may favor modalities that are not the most reliable for the task, thus motivating inference-time control of modality arbitration. We identify a small set of attention heads, termed arbitration heads, that causally influence whether predictions follow visual or textual evidence. Building on this, we introduce a lightweight, trainin...
  </details>

- **2026-11-09** — Anna Mishchenko, Nikolai Gavrilin — [LawKAN: Group-Law Layers for Composition -- When Imposing a Known Law Pays Off](http://arxiv.org/abs/2611.12567v1)
  <details><summary>📄 Abstract</summary>
  Many tasks compose transformations by a known rule: chained rotations in robotics and navigation. Learned models relearn it, compounding error; classical estimators hardcode it and miss hardware deviations. We impose the known structure and learn only the remainder: an exact non-commutative group law sits in the node of a self-contained layer, its edges learn local increments, and a zero-initialized correction psi learns unknown deviations of the law. A pre-training criterion predicts exact repr...
  </details>

- **2026-11-09** — Shengyun Si, Junjie Chu, Ye Leng et al. — [Can Frontier Auto Researchers Reconstruct Human Research Decisions in AI?](http://arxiv.org/abs/2611.12429v1)
  <details><summary>📄 Abstract</summary>
  Scientific research has long been driven by substantial human effort, from reviewing prior work and identifying research gaps to designing specific solutions. Recent advances in harness-based agent systems have given rise to increasingly capable Auto Researchers, which can autonomously carry out these tasks and, increasingly, entire end-to-end research workflows. Yet despite their rapidly growing capabilities, how closely the research decisions and outputs produced by auto researchers align with...
  </details>

- **2026-11-09** — Baifu Huang, Shilin Fang, Jianan Wang — [Be My Eye: Learning to See Beyond a Robot's Own Perspective](http://arxiv.org/abs/2611.12295v1)
  <details><summary>📄 Abstract</summary>
  Robots operating in the real world are inherently subject to partial observability, particularly in multi-robot collaboration, where individual observations may be insufficient for effective task execution. A key challenge is leveraging complementary observations from partner robots to support collaborative decision-making. We argue that information sharing should go beyond passively transmitting raw observations or generic visual features. Instead, robots should selectively encode task-relevant...
  </details>

- **2026-11-09** — Guangyan Gan, Jiahao Li, Jiashun Wang et al. — [Agent4Crypto: A Dual-Reflective and Market-Feedback-Aligned LLM-Based Multi-Agent System for Cryptocurrency Trading](http://arxiv.org/abs/2611.12269v1)
  <details><summary>📄 Abstract</summary>
  Cryptocurrency markets provide a natural testbed for autonomous AI agents because they are digital-native, high-frequency, and machine-speed environments, yet existing methods often struggle with non-stationary market regimes, opaque decisions, and fixed aggregation rules. In this paper, we propose Agent4Crypto, a dual-reflective and market-feedback-aligned multi-agent system. The framework coordinates specialized agents for data collection, analysis, risk assessment, reflection, and trading, sy...
  </details>

- **2026-11-09** — Meraj Mammadov, Pedro Zuidberg Dos Martires, Johannes Andreas Stork — [RAIL: Representation-Aligned Imitation Learning for Student-Compatible Teacher Policies](http://arxiv.org/abs/2611.12251v1)
  <details><summary>📄 Abstract</summary>
  Reinforcement learning (RL) from raw sensory inputs such as images or onboard sensors can be challenging due to high-dimensional observations and sparse rewards. A common strategy is to train a teacher policy with access to privileged state information and then distill it into a student policy that acts from raw inputs alone. However, when the teacher relies on information unavailable to the student, exact imitation may be impossible, creating an irreducible imitation gap. Existing approaches ty...
  </details>

- **2026-11-09** — Boris Ruf, Adrien de Mailly Nesle, Marcin Detyniecki — [Toward Sustainable Agentic AI: Carbon Tradeoffs Across Iterative Self-Refinement and Tool-Augmented Coding](http://arxiv.org/abs/2611.12128v1)
  <details><summary>📄 Abstract</summary>
  Agentic language model systems can improve performance either by iterating on their own outputs or by using external tools in grounded environments. While these strategies can reduce error rates and substitute for larger models in some settings, their environmental cost remains relatively underexplored. We present two complementary empirical studies that estimate the energy and carbon footprint of agentic AI across settings of increasing complexity. Study~1 evaluates iterative verbal self-refine...
  </details>

- **2026-11-09** — Xiaoyang Ye, Xiao Yao, Hairui Zhu et al. — [CARE-PO: Controllable Tool-Call Efficiency for LLM Agents](http://arxiv.org/abs/2611.12125v1)
  <details><summary>📄 Abstract</summary>
  External tool calls are a major running cost of an LLM agent, while its training objectives align almost exclusively with task completion. In a step-level diagnosis of Qwen3.5 trajectories at two model sizes on GAIA, a long-horizon tool-use benchmark, we find that most contain removable calls, at a similar rate at both sizes. Some methods add an efficiency reward to the objective to reduce the call count, but introduce problems of their own: the anchor they price calls against is computed from t...
  </details>

- **2026-11-09** — Xiangheng He, Mingjun Zhao, Zhehao Fan et al. — [Joi-Bench-Task: Benchmarking Task Coordination in Full-duplex Voice Agents through Interactive Simulation](http://arxiv.org/abs/2611.12118v1)
  <details><summary>📄 Abstract</summary>
  Full-duplex voice agents enable natural, hands-free interaction, allowing users to refine requests, redirect ongoing work, and seek clarification while the agent is speaking. However, existing voice-agent benchmarks insufficiently isolate coordination between task execution and conversation. We introduce a benchmark that assesses this coordination by examining whether agents track what is being executed, what has been completed, what has been communicated, and what remains to be reported as the ...
  </details>

- **2026-11-09** — Taekyung Kim, Jeongeun Park, Byeongho Heo et al. — [SPARK: Simple Post-training for Adapting pRetrained Knowledge to Robot Control](http://arxiv.org/abs/2611.12102v1)
  <details><summary>📄 Abstract</summary>
  Large-scale representation learning has produced public foundation models that provide strong general-purpose visual features. However, their pretraining objectives are not designed for robot representation learning, so the resulting embeddings tend to emphasize global semantics rather than the temporally sensitive representations required for robot control. Training robot models from scratch is also undesirable due to the limited scale and high collection cost of robotics data, as well as the s...
  </details>

- **2026-11-09** — Chao Chen, Jiashuo Zhang, Yunhang Shen et al. — [SMO: Compiling Natural Language Skills into Graphs of Reusable State-Move-Outcome Bricks](http://arxiv.org/abs/2611.12041v1)
  <details><summary>📄 Abstract</summary>
  Large language model agents increasingly rely on reusable natural-language skills, yet growing skill collections remain accumulations of isolated text artifacts that are difficult to compare, deduplicate, and compose. We argue that the reusable content of a skill lies not in its surface wording but in its procedural transitions: which operation to execute under a given state and which observable outcome to produce. Based on this observation, we propose State-Move-Outcome (SMO), a compilation-lik...
  </details>

- **2026-11-09** — Shigeki Kusaka, Mikoto Kudo, Takumi Tanabe et al. — [Reward-Estimated Hypergradient for Bilevel Reinforcement Learning with Black-Box Follower](http://arxiv.org/abs/2611.11998v1)
  <details><summary>📄 Abstract</summary>
  Hypergradient (HG) methods for bilevel reinforcement learning (RL) typically assume a white-box follower whose reward is known. In practice, however, the leader rarely knows the follower's reward function and can only observe its trajectories. We address this black-box setting and propose Reward-Estimated Hypergradients (RE-HG), which recovers the follower's reward from these trajectories via inverse RL (IRL). Yet IRL identifies the reward only up to potential-based shaping, a transformation tha...
  </details>

- **2026-11-09** — Trung Phuong Le, Hirofumi Nonaka, Koji Marusaki et al. — [A Large-Scale Dataset for Cross-Lingual Multi-Jurisdiction Patent Drafting from Patent Cooperation Treaty Applications](http://arxiv.org/abs/2611.11891v1)
  <details><summary>📄 Abstract</summary>
  Securing patent protection across countries requires drafting claims separately for each national patent office, in the relevant language and according to its legal and stylistic conventions. Patent claims can therefore differ across languages and jurisdictions because of translation, target-office drafting practices, and prosecution-stage changes. We formulate cross-lingual patent drafting as generating plausible candidate claim sets for a specified target language, jurisdiction, and prosecutio...
  </details>

- **2026-11-09** — Mehwish Nasim, Nicolas Fay — [Competing Influence in LLM Populations: Budget Timing and Baseline Drift](http://arxiv.org/abs/2611.11867v1)
  <details><summary>📄 Abstract</summary>
  When competing campaigns target a population of large language model (LLM) agents, observed opinion changes may reflect both campaign influence and changes that would occur without intervention. We study how the timing of campaign expenditure and the population's own evolution shape outcomes in a network of persona-conditioned LLM agents that exchange and revise opinions in natural language. A proponent and a challenger are tasked with generating opposing messages under equal delivery budgets, w...
  </details>

- **2026-11-09** — Thomas X. Sheppard, Alon Albalak, Joel Lehman et al. — [Are UFOs Real? Introducing Unified Factored Organizers](http://arxiv.org/abs/2611.11862v1)
  <details><summary>📄 Abstract</summary>
  Implicit in much research in deep learning is the assumption that if a network achieves low loss, then it must have learned a good representation of its training data. Recent work by Kumar et al. (2025, arXiv:2505.11581) questions this assumption, arguing that networks trained with conventional gradient descent achieve low loss despite learning fractured entangled representations (FER), leaving related concepts disconnected and unrelated concepts entangled inappropriately. Kumar et al. further s...
  </details>

- **2026-11-09** — Bingzhang Wang, Nathan Zhao, Jialeng Ni et al. — [Decoupled Asynchronous System for Humanoids (DASH): Latency-Agnostic Scaling of Vision-Language-Action Models for Humanoid Manipulation](http://arxiv.org/abs/2611.11854v1)
  <details><summary>📄 Abstract</summary>
  Vision-language-action (VLA) models pair a vision-language backbone with an action head, but in closed-loop control the backbone sits on the control-critical path: while it computes, the robot keeps moving, so each executed action is conditioned on an increasingly stale observation. A larger backbone therefore directly blocks reactivity, especially in humanoid dexterous manipulation. We present DASH, a Decoupled Asynchronous System for Humanoids that removes this coupling. DASH splits the policy...
  </details>

- **2026-11-09** — Huiyu Xie, Tanping Zhou, Tao Hu et al. — [VeilTune: Secure Fine-Tuning of Private LoRA Adapters on Public Pretrained Language Models](http://arxiv.org/abs/2611.11817v1)
  <details><summary>📄 Abstract</summary>
  Fine-tuning public pretrained language models with lightweight adapters such as LoRA has become the mainstream way to adapt them to downstream tasks. A service provider often trains its adapter on a data owner's samples, so two assets need protection: the data owner's samples and the provider's adapter. Existing secure fine-tuning protocols protect the samples but reveal to the data owner intermediate results of every training step, such as the hidden representations or logits of its inputs. We ...
  </details>

- **2026-11-09** — Qi Lu, Sen Li, Likun Shi et al. — [CaseLaw: A Policy-Decoupled Framework for Training-Free Content Moderation](http://arxiv.org/abs/2611.11812v1)
  <details><summary>📄 Abstract</summary>
  Content moderation is inherently policy-dependent: moderation boundaries are often subtle, subjective, and frequently updated, while conventional rule based or fine-tuning based systems require costly rule rewriting, model retraining, or system redeployment. We propose CaseLaw, a policy-decoupled and training-free framework for adaptive content moderation. CaseLaw reformulates moderation as precedent-based retrieval and voting, where multimodal content is transformed into evidence-preserved stru...
  </details>

- **2026-11-09** — Payman Behnam, Debopam Sanyal, Pranav Ponnusamy et al. — [BridgeKV: Large-Model Prefill and Small-Model Decoding for LLM Inference via KV Cache Translation](http://arxiv.org/abs/2611.11761v1)
  <details><summary>📄 Abstract</summary>
  LLM inference has two phases with different bottlenecks: LLM prefill runs once per request and is compute-intensive. Decoding repeats for every output token and is limited by memory bandwidth. To address the challenges associated with this issue, different solutions have been proposed. All of these solutions use the same model for both prefill and decode phases. We propose BridgeKV, which uses a larger model for prefill and a smaller model of the same family for decoding. A lightweight KV-stitch...
  </details>

- **2026-11-09** — Laura Kurek, Elijah Covert, Rafael I Bonilla et al. — [State Media at Retrieval Time: A Large-Scale Audit of Russian State-Aligned Sources in AI Chatbot Responses](http://arxiv.org/abs/2611.11727v1)
  <details><summary>📄 Abstract</summary>
  The Pravda Network is a Russian state-aligned media aggregator, with over 110 websites and more than 15 million articles published since 2023. Given its prolific and repetitive output, emerging scholarship argues that the Pravda Network was built to influence AI systems. We conduct a large-scale audit of leading AI chatbots to understand: (1) the retrieval rates of Pravda Network articles, (2) the conditions of retrieval, and (3) whether chatbot responses affirm or caveat this content. We build ...
  </details>

- **2026-11-09** — Saif Uddin Mahmud, Afsana Tasnim, Ahmed Ryan et al. — [Decalage: Uncovering the Gap Between Model-Generated Reasoning and Actual Code Implementation in Small Language Models](http://arxiv.org/abs/2611.11721v1)
  <details><summary>📄 Abstract</summary>
  Agentic code generation often asks a model to explain its reasoning before it writes code, and a common way to make such a workflow safer is to add a security instruction to the prompt. We test what that instruction does in small language models, which are attractive because they run locally and cheaply. Four open code models of 1.5B to 3B parameters generate C++ from 166 sections of eleven public requirements documents, once with a general prompt and once with a secure prompt. The secure prompt...
  </details>

- **2026-11-09** — Ziming Wei, Bingyang Liu, David Z. Pan — [CASCoDe: A Closed-Loop Agentic Framework for Analog Sizing and Layout Co-Design](http://arxiv.org/abs/2611.11710v1)
  <details><summary>📄 Abstract</summary>
  Expert analog layouts differ from auto-generated ones in density and regularity, not only in legality: experts make a succession of discrete, hierarchical physical decisions and revisit each after extracted electrical results, while most existing automated flows act on a physical search space fixed before the controller runs. We present CASCoDe, a closed-loop LLM agent framework for analog netlist-to-layout design that formalizes those expert decisions as a hierarchical discrete action space-siz...
  </details>

- **2026-11-09** — Bing Han, Yichuan Peng, Haoyu Dong et al. — [Learning Heterogeneous Tactile Representation for General Dexterous Manipulation](http://arxiv.org/abs/2611.12806v1)
  <details><summary>📄 Abstract</summary>
  Tactile sensing is an indispensable modality for contact-rich dexterous manipulation, a capability that hints at the ultimate frontiers of embodied intelligence. However, commercially available tactile sensors are still at a relatively early stage of development, with each type of sensor offering irreplaceable strengths alongside its own drawbacks. A key challenge is thus to free tactile understanding from sensor-specific physics, so that embodied models can effectively leverage heterogeneous ta...
  </details>

- **2026-11-09** — Matěj Kripner, Milan Straka — [VLA Adaptation with Real and Simulated Data: A Case Study on Robotic Chess](http://arxiv.org/abs/2611.12676v1)
  <details><summary>📄 Abstract</summary>
  Vision-language-action (VLA) models are trained as general-purpose foundation models for robot learning, and require fine-tuning for each downstream task and robot. This raises practical questions such as how much data and training updates are needed, how checkpoints should be selected, and whether simulation can be leveraged to alleviate the cost of real data collection. We study these questions on a task that requires both precise manipulation and spatial understanding of the scene. In this ta...
  </details>

- **2026-11-09** — Ruilin Zhang, Xuanshuo Liu, Junzhe Dai et al. — [PCTac: Mechanochromic Photonic-Crystal Tactile Sensor for Dexterous Manipulation](http://arxiv.org/abs/2611.12383v1)
  <details><summary>📄 Abstract</summary>
  Modern visuotactile sensors primarily sense contact by imaging the deformation of a compliant interface. Using techniques such as photometric stereo, they can recover detailed contact geometry, often represented as surface normals or depth. However, force-related information typically still needs to be inferred indirectly through calibration, geometric reconstruction, or learned mappings. Mechanochromic photonic-crystal (PC) materials offer an alternative physical encoding mechanism: contact loa...
  </details>

- **2026-11-09** — Kangrui Wang, Qineng Wang, Changhe Chen et al. — [Embodied First Exam](http://arxiv.org/abs/2611.12177v1)
  <details><summary>📄 Abstract</summary>
  Early successes on agentic robotics point to a potential paradigm shift toward using coding agents to control robots. Existing robotics benchmarks are built around visuomotor policy learning, leaving it open whether coding agents can reliably control diverse robots under physical-world constraints. We therefore introduce the Embodied First Exam, a unified, comprehensive, and agent-native evaluation framework where coding agents can choose their own control approach: direct control, code to contr...
  </details>

- **2026-11-09** — Ali-Adeeb Abbas, Esmaeil Seraj — [Distilling Instructions into Weights: Closed-Form Edits Fix a Robot Policy's Misreading](http://arxiv.org/abs/2611.11894v1)
  <details><summary>📄 Abstract</summary>
  Generalist robot policies often fail at one step of a task they can otherwise perform. We ask whether such a failure can be repaired by editing the policy's weights directly, without gradients, training data, or a change to the instruction. Told to put the cube then the banana in the bowl, a zero-shot $π_{0.5}$ vision-language-action policy in RoboLab releases the cube before it reaches the bowl. Replaying 21 of these decisions under rewordings shows that it binds "in the bowl" to the wrong obje...
  </details>

- **2026-11-09** — Estuti Shukla, David Radice, Rossella Gamba et al. — [Mapping of Spacetimes with Neural Networks](http://arxiv.org/abs/2611.12857v1)
  <details><summary>📄 Abstract</summary>
  Gauge freedom in numerical relativity complicates the interpretation of simulation coordinates and the comparison of different descriptions of the same spacetime. We present a data-driven neural network method for learning coordinate maps from numerical metric data to a prescribed target gauge. The network is trained by matching the transformed source metric to the target metric, without assuming a functional form for the coordinate transformation. We first validate the method on analytical Schw...
  </details>

- **2026-11-09** — Tianze Luo, Haofeng Huang, Yuan Yao — [What kills $v$-prediction? A Patch-wise PCA Perspective on Pixel-Space Flow Matching](http://arxiv.org/abs/2611.12852v1)
  <details><summary>📄 Abstract</summary>
  Latent Diffusion Models dominate generative modeling but face two-stage training complexity and the inherent reconstruction limits of pre-trained autoencoders. Pixel-space Flow Matching offers a simplified end-to-end alternative yet often encounters training difficulties when using the standard $v$-prediction objective. Recent research attributes this difficulty to the off-manifold nature of noised targets, motivating a shift toward $x$-prediction. In this paper, we investigate this explanation ...
  </details>

- **2026-11-09** — Tingwei Hu, Lili Mei, Guochuan Zhang — [Computing EF1 Allocations under Budget Constraints in Polynomial Time](http://arxiv.org/abs/2611.12740v1)
  <details><summary>📄 Abstract</summary>
  We study the fair allocation of indivisible items to agents with budget constraints and additive valuations. Each agent compares its own bundle with the subsets of another bundle that fit its budget. An allocation is envy-free up to one item (EF1) if, for every agent and every nonempty subset under comparison, removing an item of maximum value to that agent eliminates its envy. We require EF1 both between agents and towards the charity, which contains all unallocated items. EF1 allocations exist...
  </details>

- **2026-11-09** — Marcus Armstrong, Navid Ayoobi, Pradham Mummaleti et al. — [Interpretability Is Not Model-Specific](http://arxiv.org/abs/2611.12675v1)
  <details><summary>📄 Abstract</summary>
  Interpretability tools are usually built for one model at a time: a refusal direction, a truthfulness probe, or a steering vector is found with labeled data inside the model it explains. We ask whether such tools can be carried to other models through a map between residual streams fit only on unlabeled prompts. We transfer a refusal direction, tested causally by addition and ablation, and two read-out tools, a correctness direction and a sentiment probe, across 110 pairs of models from five fam...
  </details>

- **2026-11-09** — Zequan Liu — [Spike-to-Field Mechanisms of Turbulence-Like Dynamics in Spatial Spiking Neural Networks](http://arxiv.org/abs/2611.12627v1)
  <details><summary>📄 Abstract</summary>
  Neural avalanches and turbulence-like brain dynamics are usually measured after neural activity has been coarse-grained into continuous fields, leaving open which spike-level mechanisms can generate these macroscopic observables. We build a spatial leaky integrate-and-fire spiking neural network and explicitly transform spikes into activity-density and Hilbert phase fields. A delayed, distance-dependent, passive-dendrite regime reproducibly generates turbulence-like field structure, including hi...
  </details>

- **2026-11-09** — Wannes Van den Bulck, Sofie Goethals, David Martens — [Fairness in Explainable AI Narratives: Decomposing Social Disparities in LLM-Generated Explanations](http://arxiv.org/abs/2611.12592v1)
  <details><summary>📄 Abstract</summary>
  Large language models (LLMs) are increasingly used to translate technical explainable AI (XAI) artefacts such as SHAP into explanatory narratives (XAINs) for lay users. In high-risk domains, these explanations are often the main resource through which individuals can understand and contest adverse decisions. Yet LLMs are known to reproduce social bias, even from proxy variables alone, and fairness in XAINs remains unstudied. Because XAINs are bound to a ground-truth artefact, fairness concerns n...
  </details>

- **2026-11-09** — A. R. M. Wolfert — [Monetisation and Cost Function Scalarisation Cannot Guarantee Valid Multi-Criteria Decision-Making](http://arxiv.org/abs/2611.12577v1)
  <details><summary>📄 Abstract</summary>
  Monetary quantities are not preferences. Cost is an object-related system performance; value-for-money is an actor's subjective evaluation of it. Monetisation embeds trade-off information: its conversion coefficients express valuations and determine how heterogeneous performances compensate one another. Cost-benefit analysis, even net present value, yields quantities of money, not the preference value actors attribute to them.   This creates a monetisation paradox. Cost enters a multi-criteria p...
  </details>

- **2026-11-09** — Rebeca Nam, Chase M. Fensore, Christian A. Fauria-Robinson et al. — [Evaluating Cross-Signal Coherence in Mammography Vision-Language Models](http://arxiv.org/abs/2611.12574v1)
  <details><summary>📄 Abstract</summary>
  As vision-language models (VLMs) move toward interpreting medical images directly, their outputs increasingly include not just a label but a stated confidence and a written justification. Yet the field still predominantly evaluates VLMs using just accuracy. We evaluate the coherence between answer, confidence, and explanation across four VLMs on breast density and BI-RADS categorization, using two mammography datasets. We perform controlled perturbations of the question, multiple choice option o...
  </details>

- **2026-11-09** — Yuhao Liu, Mengyu Wang, Xiao Chen et al. — [More Than Just Style: Benchmarking Personality Influence in Large Language Models](http://arxiv.org/abs/2611.12392v1)
  <details><summary>📄 Abstract</summary>
  In addition to the effects of explicit input prompts and instructions, large language model outputs are influenced by underlying behavioral preferences similar to human personality tendencies. These tendencies can affect how models interpret situations and make decisions. However, their influence is difficult to disentangle from the effects of model capabilities and instructions. Therefore, we introduce SPACE, a benchmark framework combining a controlled evaluation protocol with complementary da...
  </details>

- **2026-11-09** — Vianey Darsel, Etienne C{ô}me, Jeppe Rich et al. — [The Fragility Of Synthetic Populations Over Time: An Evaluation Of Forecasting Strategies For Agent-Based Models](http://arxiv.org/abs/2611.12344v1)
  <details><summary>📄 Abstract</summary>
  Agent-based simulation models are widely used to assess the future mobility projects. However, their effectiveness hinges on the accuracy of synthetic populations, which are often generated using data from a single reference year. This study explores the temporal validity of these populations by evaluating their performance over multi-year datasets in a simulation-like environment. We focus on multi-dimensional agents, ensuring that all attributes critical to the simulation are comprehensively r...
  </details>

- **2026-11-09** — Riccardo Cavarra, Lupo Lovatelli, Shaheim Ogbomo-Harmitt et al. — [PACE-ECG: Patient-Aware Contrastive ECG Pretraining; Leveraging Longitudinal Structure for Transferable Representations](http://arxiv.org/abs/2611.12307v1)
  <details><summary>📄 Abstract</summary>
  Foundation models for physiological signals are commonly evaluated on in-domain interpretation tasks, but their ability to transfer to longitudinal clinical prognosis across healthcare systems remains uncertain. We developed PACE-ECG, an ECG pretraining framework that combines contrastive learning across temporally neighbouring recordings from the same patient with clinically guided multitask supervision. We evaluated frozen ECG representations for post-myocardial-infarction all-cause mortality ...
  </details>

- **2026-11-09** — Miguel P. Bento — [A Geometric Invariant of Attention Predicts Head Specialization from Weights Alone](http://arxiv.org/abs/2611.12206v1)
  <details><summary>📄 Abstract</summary>
  Transformers are built with continuous symmetries in the attention mechanism. We derive $ρ$, a scalar invariant that measures each head's capacity to couple to rotary positional encodings. This framework allows us to analyze heads without forward passes, opening a new research direction into data-independent analysis of modern LLMs. Empirically, we find that $ρ$ predicts induction heads, the most-studied circuit type in mechanistic interpretability, with Spearman correlation between $-0.55$ and ...
  </details>

- **2026-11-09** — Ankur Verma — [Forecast Value Add: Reward-Based Action Selection over Probabilistic Demand Forecasts](http://arxiv.org/abs/2611.12116v1)
  <details><summary>📄 Abstract</summary>
  Strong machine-learning ensembles capture much of the trend, seasonality, and known events in demand, yet they can still understate peaks, miss moving events, or mistake temporary changes for shifts in demand level. We address this gap by framing forecast refinement as a reward-driven decision problem. For each forecast period, we let an agent choose among values already produced by the ensemble: its base forecast, distribution-free bounds, quantiles, and a bias-corrected estimate. We evaluate t...
  </details>

- **2026-11-09** — Francesca Larosa, Sandro Calmanti, Matteo De Felice et al. — [Perils and opportunities of AI for public climate services](http://arxiv.org/abs/2611.12106v1)
  <details><summary>📄 Abstract</summary>
  The rapid integration of artificial intelligence (AI), particularly generative and machine-learning systems, in climate services development and provision is transforming how climate information is produced, accessed, and interpreted. AI-enabled climate services offer significant opportunities for process automation, optimisation, tailoring, and the translation of complex climate data into actionable knowledge for diverse users. However, the growing reliance on privately controlled algorithms, d...
  </details>

- **2026-11-09** — Josef A. Buchner, Richard Osuala, Ayhan Can Erdur et al. — [Next-Generation Segmentation in Radiotherapy: A Narrative Review from Atlas-Based Methods to Agentic Vision-Language Models](http://arxiv.org/abs/2611.12085v1)
  <details><summary>📄 Abstract</summary>
  Precise segmentation of target volumes and organs at risk is an essential prerequisite for modern, high-precision radiation therapy. However, this task has traditionally been time-consuming and subject to high interobserver variability. Motivated by these limitations, more advanced and novel approaches to automating this task have been developed over the past two decades. This narrative review highlights representative milestones, with a focus on the most recent developments. These approaches in...
  </details>

- **2026-11-09** — Xuyu Dong, Yixuan Li, Jianguo Huang et al. — [Benchmarking language models and agents for scientific reasoning in evolving materials laboratories](http://arxiv.org/abs/2611.12014v1)
  <details><summary>📄 Abstract</summary>
  Large language models and the multi-agent systems built around them could accelerate materials discovery by connecting scientific knowledge with experimental decisions. Existing benchmarks establish capabilities in domain knowledge, multimodal interpretation and scientific tool use. As language models increasingly support materials research workflows, their ability to distinguish closely related material states and reason accurately with quantitative evidence remains insufficiently evaluated. Th...
  </details>

- **2026-11-09** — Mostafa 'Neo' Mohsenvand — [Attention Is Only as Good as Its Witnesses: When Higher-Order Layers Help, and When They Do Not](http://arxiv.org/abs/2611.11937v1)
  <details><summary>📄 Abstract</summary>
  Transformers stop learning graph search as graphs grow, and learn the card game SET only after many distinct questions, although attention can represent both. We read these failures, and the uneven record of higher-order attention, from what a layer sums over: each layer we study computes the partition function of a family of witnesses and reads it at a temperature. Two laws follow. The depth law is a known result of logic, which we state for these layers: L layers over two-step walks reach exac...
  </details>

- **2026-11-09** — Peixuan Hou, Bin Chen, Li He et al. — [ShopMind: A Mental World Model for Personalized and Realistic E-commerce User Simulation](http://arxiv.org/abs/2611.11897v1)
  <details><summary>📄 Abstract</summary>
  Large language models are widely used in e-commerce user simulation, providing a foundation for understanding users and predicting human decisions. However, existing simulators still struggle to achieve both personalization and behavioral realism. Most methods predict the next action directly from interaction histories and the current context, without accounting for the evolving mental world that underlies user behavior. Theory of Mind suggests that behavior is driven by mental states, including...
  </details>

- **2026-11-09** — Amir Sabbaghziarani, Parsa Ghazvinian, Sepehr Salem et al. — [Answer or Defer? Testing VLMs' Stated Confidence on Brain MRI](http://arxiv.org/abs/2611.11833v1)
  <details><summary>📄 Abstract</summary>
  Vision-language models (VLMs) could support medical-image interpretation, but their use requires deciding which interpretations to accept and which images to refer to a clinician. We test whether thresholding stated confidence can retain useful coverage while limiting errors among accepted answers, and how this depends on the population. Eight open-weight VLMs, including two reasoning models, assess 3,888 brain MRI slices from post-treatment glioma patients (BraTS 2024) and healthy volunteers (I...
  </details>

- **2026-11-09** — Zhenyuan Chen, Wenshuo Tao, Zhuo Huang et al. — [When to Trust Adaptation: Contextual Fusion for Transferable Vision-Language Prompting](http://arxiv.org/abs/2611.11824v1)
  <details><summary>📄 Abstract</summary>
  When a vision-language model encounters a new class or domain, how much should it trust its learned prompts? Because source adaptation can correct pretrained errors on some target images while disturbing valid predictions on others, we introduce Contextual Adaptive Fusion (CAF), which retains four prediction branches by pairing frozen and prompted visual and textual representations. To arbitrate when branches disagree on an image, CAF combines each branch's predictive confidence with how frequen...
  </details>

- **2026-11-09** — David B. D'Ambrosio, Alon Albalak, Joel Lehman et al. — [The Value of Not Knowing: How Fresh Eyes through Naive LLMs Fuel Creativity](http://arxiv.org/abs/2611.11725v1)
  <details><summary>📄 Abstract</summary>
  Many major scientific advances come from approaching a problem with a new or novel perspective. While large language models (LLMs) with internet-scale knowledge seem poised to take such perspectives, their consistent generation remains elusive. Instead, models are drawn to dominant views and preexisting, in-field bias. To explore the potential of fresh eyes to increase creativity, this paper proposes naive LLMs, models that are made intentionally ignorant of a specific topic. Through deprivation...
  </details>

- **2026-11-08** — Na Young Ahn — [Just AI Governance and the Forbidden-Boundary Principle](http://arxiv.org/abs/2611.13007v1)
  <details><summary>📄 Abstract</summary>
  Artificial intelligence (AI) increasingly shapes consequential decisions, yet predictive accuracy is not a sufficient justification for delegated authority. This conceptual study develops an integrated framework for assessing just AI across normative, data, model, and governance layers. Drawing on plural theories of justice, sociotechnical fairness research, and publicly available governance standards, it maps six justice requirements to observable evidence, decision rights, and remedies. It pro...
  </details>

- **2026-11-08** — Yuanrui Wang, Kaifang Li, Xuanyue Li et al. — [One Table, Many Queries: Benchmarking Generalist Tabular Models Across Generation, Imputation, and Prediction](http://arxiv.org/abs/2611.13001v1)
  <details><summary>📄 Abstract</summary>
  Generation, imputation, and prediction query different aspects of the same tabular distribution, but are usually evaluated separately. This leaves unclear which capabilities they share, how their training objectives interact, and whether one model can perform all three well. We introduce the One Table Benchmark (\ours{}), spanning 56 datasets, 46 registered methods, and 20 capability axes under aligned data splits and explicit task contracts. We compare task ranks on aligned support, train five ...
  </details>

- **2026-11-08** — Ruimeng Liu, Denan Liang, Ruofei Bai et al. — [PhysMoE: Fast Spatial Grounding with Single-Token Coordinate Representation in Modality-Decoupled VLMs](http://arxiv.org/abs/2611.13000v1)
  <details><summary>📄 Abstract</summary>
  Embodied Vision-Language Models (VLMs) are backbones for robotic planning and manipulation. However, for coordinate prediction in grounding tasks, existing architectures suffer from two distinct bottlenecks: discrete tokenization disrupts spatial continuity with high decoding latency, while standard point regression fails on multi-contact affordances and irregularly shaped targets. To resolve these challenges, we propose PhysMoE, introducing three core contributions: (1) sharing lower layers for...
  </details>

- **2026-11-08** — Joseph Marvin Imperial, Daniel Slate, Noam Kolt — [ScrapeBench: Evaluating Legal Compliance of AI Agents in Website Scraping](http://arxiv.org/abs/2611.11306v2)
  <details><summary>📄 Abstract</summary>
  AI agents deployed on the open web are becoming more capable of performing actions that may breach contractual provisions and violate computer security laws. In this paper, we introduce ScrapeBench, the first agentic benchmark for empirically evaluating the legal compliance of AI agents with website scraping policies, namely terms of service (ToS) and $\texttt{robots.txt}$ directives. Across widely used closed-weight and open-weight AI agents, we find that most agents exhibit low compliance rate...
  </details>

- **2026-11-08** — Mingjia Chen, Xuewen Zhao, Philip Dames et al. — [CAFE: Closed-Loop Autonomous Task Formulation and Execution without Instance-Specific Instructions](http://arxiv.org/abs/2611.12983v1)
  <details><summary>📄 Abstract</summary>
  Scene-driven robot autonomy requires selecting tasks from observations as well as executing them. We study scene-driven task formulation and execution under predefined cleaning, safety, and storage/organization categories, without instance-specific goals or action sequences. CAFE maintains online memory of objects, functional zones, and execution states. A rule-guided Trigger-LLM admits formulation from accumulated evidence; Draft, Complete, and Audit propose goals, resolve execution details, an...
  </details>

- **2026-11-08** — Mohamed Gaber, Tahsin Wahid, Mohammad Mamun et al. — [Attack Injection to Vehicle Reactions: Extensible Closed-Loop Adversarial Evaluation Framework](http://arxiv.org/abs/2611.11627v1)
  <details><summary>📄 Abstract</summary>
  Autonomous vehicles can use information exchanged with other vehicles and roadside infrastructure to support driving decisions. However, applications that rely on this information can make unsafe decisions when it is falsified. Studying the resulting traffic effects requires following received information through application decisions, vehicle reactions, and subsequent interactions. We present an extensible closed-loop adversarial evaluation framework built on VaN3Twin, a platform for traffic an...
  </details>

- **2026-11-08** — Prabhjot Singh, Praney Goyal, Raksha Sharma — [A Layer-wise Study of How Style Rewriting Breaks the Calibration of Zero-Shot LLM Fake-News Detectors](http://arxiv.org/abs/2611.11239v1)
  <details><summary>📄 Abstract</summary>
  Large language models (LLMs) are increasingly asked to judge whether a news article is true, and their stated confidence is often taken at face value. We test what happens to that confidence when an article's writing style, but not its facts, is manipulated, as in recent \emph{style attacks} on fake-news detectors. Tracing how the prediction and its confidence form layer by layer inside the network, we study three model families (LLaMA-3-8B, Qwen2.5-7B, Mistral-7B) on three fake-news benchmarks,...
  </details>

- **2026-11-08** — Chris Choy, Zhiding Yu, Jan Kautz — [LocateAnyMesh: Grounding 3D Mesh Queries in 2D Images with Vision-Language Models](http://arxiv.org/abs/2611.11692v1)
  <details><summary>📄 Abstract</summary>
  Textured 3D meshes specify object geometry and appearance, making them a natural query for finding a particular asset in an image. We introduce LocateAnyMesh, a vision-language model that uses the mesh itself as part of its prompt. A frozen 3D encoder maps colored surface points to a compact token sequence, which a learned connector places alongside image and instruction tokens. We evaluate two grounding models with PPAT mesh tokens: LAM-Select selects image-region proposals, while LAM-Direct pr...
  </details>

- **2026-11-08** — Dhruv Dixit, Paritosh Pandey, Snehalkumar 'Neil' S. Gaikwad — [Self-Indexing Latent Memories for Access-Aware Continual Instruction Tuning of LLMs](http://arxiv.org/abs/2611.11684v1)
  <details><summary>📄 Abstract</summary>
  Continual instruction tuning often preserves old skills with task-private modules. Inference still requires selecting the right module from the prompt alone. We introduce Task-Isolated Latent Adapter Continual Training (TILA-CT), a replay-free method that makes each task module self-indexing. Each task receives a latent memory and adapter bank in a frozen LLM. During adaptation, the memory gathers causal-prefix information and injects task-conditioned context. For access, its persistent state pr...
  </details>

- **2026-11-08** — Xiayin Lou, Peng Luo, Liqiu Meng — [Toward Self-Evolving Geospatial Algorithms: An LLM-Driven Framework with a Case Study on Spatial Regime Discovery](http://arxiv.org/abs/2611.11669v1)
  <details><summary>📄 Abstract</summary>
  Geospatial algorithms have been developed through expert-driven discovery: a researcher spots a limitation, proposes a structural fix, and checks it by hand. With LLM-driven multi-agent systems becoming practical, much of the candidate-generation, evaluation, and selection work can now be largely automated, while the researcher's role shifts upstream toward problem formulation, evaluation design, and interpretation. We refer to this paradigm as Self-Evolving Geospatial Algorithms (SEGA) and prop...
  </details>

- **2026-11-08** — Dennis Gross — [Weight-Space Programming of Policies and Their Verification via Model Checking](http://arxiv.org/abs/2611.11604v1)
  <details><summary>📄 Abstract</summary>
  Large language models (LLMs) can write the weights of small neural networks directly, without gradient descent. This weight-space programming creates policies for sequential decision-making from a task description alone, but nothing guarantees that a written policy behaves as intended. We combine weight-space programming with probabilistic model checking. Given an environment modeled as a Markov decision process and a requirement in probabilistic computation tree logic (PCTL), an LLM writes all ...
  </details>

- **2026-11-08** — Fangcheng Jin — [Kinora: A Versioned Workflow for Text-to-Motion Generation, Robot Retargeting, and Interactive Validation](http://arxiv.org/abs/2611.11601v1)
  <details><summary>📄 Abstract</summary>
  Motion generation tools produce candidate trajectories, but interactive robot authoring also requires recoverable execution, traceable edits, explicit geometry, and model-specific validation. We present Kinora, a system that connects text-to-motion generation, a motion library, local agent tools, robot retargeting, and trajectory refinement through versioned artifacts. The current release uses an independently specified 52-joint authoring rig and procedural skeleton previews, separating the dist...
  </details>

- **2026-11-08** — Sunghyeun Woo, Javier Conde, Pedro Reviriego — [Same Error, Different Recovery: How Delivery Changes LLM Agent Behavior](http://arxiv.org/abs/2611.11581v1)
  <details><summary>📄 Abstract</summary>
  A tool-using language model must decide whether to retry a failed call, correct it, or stop and tell the user. The error text alone may not be enough: the same feedback can lead to different actions depending on where it appears in the conversation. We isolate this delivery problem by varying placement, guidance, retained history and turn structure. Two studies with plans fixed before data collection, across 13 open models from 3B to 70B parameters, compare the next action and subsequent task co...
  </details>

- **2026-11-08** — Guanming Liu, Weihang Wang, Peng Zhang et al. — [LiveAsset: Learning Intent Assets from Corrective Interactions for Agent Runtime Control](http://arxiv.org/abs/2611.11560v1)
  <details><summary>📄 Abstract</summary>
  Large language model (LLM) agents acting across web applications and online services often need multi-turn corrections to align their work with users' underspecified goals and preferences. In practice, users may identify problems in the current outcome without specifying the desired result, so learning user intentions requires interpreting each correction against the agent's preceding and revised outcomes. These expectations are often connected to a particular context, making it hard to know whe...
  </details>

- **2026-11-08** — Weizhong Huang, Huaijia Kou, Tianyu Xie et al. — [Semantically Aligned KV Cache Compression for Efficient Agentic Autoregressive Video Generation](http://arxiv.org/abs/2611.11452v1)
  <details><summary>📄 Abstract</summary>
  Agentic autoregressive video generation combines semantic planning, sequential generation, and visual verification for controllable synthesis. Growing visual histories enlarge the key-value (KV) cache, increasing memory use and attention costs across candidate rollouts. Existing compression methods primarily optimize individual generators without the planner's semantic constraints, risking low priority for states supporting requested attributes or actions. We introduce SemanticKV, a training-fre...
  </details>

- **2026-11-08** — Joonkyu Jang, Hyung-Joo Moon, Kwang Soon Kim et al. — [CHANNELS4WORLD: An Environment-Scale Dataset for Wireless Foundation Models](http://arxiv.org/abs/2611.11428v1)
  <details><summary>📄 Abstract</summary>
  Wireless foundation models learn reusable representations across tasks, configurations, and deployment environments. Their pretraining requires environmental breadth, yet wireless datasets often sample few sites densely. We introduce Channels4World, a scene-centered dataset of 100,000 distinct outdoor RF scenes and a procedural method for generating them. Each scene links a generated environment and RF material assignments to 32 base-station (BS) positions, 16,384 UE positions, and aligned varia...
  </details>

- **2026-11-08** — Siming Fu, Ruizhe He, Zheming Fu et al. — [GenRM-Flow: Generators are Process-aware Reward Models in Flow Matching](http://arxiv.org/abs/2611.11421v1)
  <details><summary>📄 Abstract</summary>
  Aligning video generation models with human preference depends critically on the quality of the reward model that scores generated videos. Current video reward models, however, source their reward signal from a model's representational rather than generative capacity: they either repurpose vision-language models as pixel-space scorers, or train auxiliary scoring heads on top of frozen generator features. The generator's actual ability to predict velocities, denoise latents, and produce videos pl...
  </details>

- **2026-11-08** — Joseph Marvin Imperial, Daniel Slate, Noam Kolt — [ScrapeBench: Evaluating Legal Compliance of AI Agents in Website Scraping](http://arxiv.org/abs/2611.11306v1)
  <details><summary>📄 Abstract</summary>
  AI agents deployed on the open web are becoming more capable of performing actions that may breach contractual provisions and violate computer security laws. In this paper, we introduce ScrapeBench, the first agentic benchmark for empirically evaluating the legal compliance of AI agents with website scraping policies, namely terms of service (ToS) and robots.txt directives. Across widely used closed-weight and open-weight AI agents, we find that most agents exhibit low compliance rates (< 5%) wh...
  </details>

- **2026-11-08** — Jingkun Yue, Pengxiang Wang, Siqi Zhang et al. — [SurgWorld: Learning Surgical Representations Beyond Observation via Latent Prediction](http://arxiv.org/abs/2611.11140v1)
  <details><summary>📄 Abstract</summary>
  Surgical procedures are inherently partially observable, requiring surgeons to continuously infer evolving anatomical dynamics and future surgical states beyond the current observation. However, existing self-supervised learning methods primarily learn from observed surgical videos through masked reconstruction or predicting representations within the camera's current field of view, lacking the capability to explicitly model the out-of-sight surgical dynamics. Inspired by latent predictive world...
  </details>

- **2026-11-08** — Changran Liu, Qi Wu, Wenchao Ma et al. — [From Game Generation to Game Playing: Fully Automated Ability Training for Vision-Language-Action Models](http://arxiv.org/abs/2611.11136v1)
  <details><summary>📄 Abstract</summary>
  Training vision-language-action (VLA) models to follow gameplay instructions across diverse games is limited by the cost of collecting demonstrations. We introduce a framework that automatically generates game environments and expert demonstrations. An LLM-powered agent uses game-building tools to construct executable environments and tasks targeting specified skills. Programmatic experts then use privileged simulator state to generate aligned instructions, rendered observations, and keyboard an...
  </details>

- **2026-11-08** — Qinhong Zhou, Riley Zong, Chunru Lin et al. — [HARP-Bench: Benchmarking Robot Manipulation Around Active Humans](http://arxiv.org/abs/2611.11123v1)
  <details><summary>📄 Abstract</summary>
  Recent robot manipulation benchmarks have enabled systematic evaluation of general-purpose robot policies across diverse objects, scenes, instructions, and embodiments. However, most existing benchmarks still assume that the robot is the only active agent and that task semantics are determined primarily by the instruction and object state. This assumption overlooks a common source of real-world variation: humans actively sharing the workspace. In such settings, humans may reveal an implicit goal...
  </details>

- **2026-11-08** — Elena Aschmann, Anshu Dubey, Mohamed Wahib et al. — [Application-Defined Abstractions to Separate Numerical Intent from Computation Orchestration](http://arxiv.org/abs/2611.11100v1)
  <details><summary>📄 Abstract</summary>
  In High-performance Computing the holy grail has been to translate numerical algorithms expressed in mathematical notation into code that performs well across a range of platforms. A variety of portability frameworks have abstracted data layout, parallelization and orchestration from application's view, however, the resulting format is still code that conforms to the idioms of the framework. Additionally, substantial refactoring is typically needed to achieve performance goals. Increasing sophis...
  </details>

- **2026-11-08** — Ziwon Yoon, Seok Hwan Kim, Yiyu Chen et al. — [HINT-VLM: Humanoid Interactive Navigation over Rough Terrain with Embodiment-Grounded Vision-Language Model](http://arxiv.org/abs/2611.11665v1)
  <details><summary>📄 Abstract</summary>
  Humanoid robots have achieved significant progress in locomotion and manipulation, enabling traversal over rough terrain and richer interaction with the environment, such as moving obstacles. However, most traditional navigation methods assume non-interactive environments and focus only on traversal. While Navigation Among Movable Obstacles (NAMO) approaches relax this assumption, prior efforts have largely focused on flat environments and reactive interaction, rather than predicting object mova...
  </details>

- **2026-11-08** — Zhang Xi-Jia, Roman Yakunin, Shivang Chopra et al. — [FlowEval: How Much Adaptation Does an Embodied Foundation Model Need at Deployment?](http://arxiv.org/abs/2611.11650v1)
  <details><summary>📄 Abstract</summary>
  Large-scale pretraining is reducing the amount of adaptation required to deploy embodied foundation models, but it is not guaranteed that a pretrained model already provide the level of performance required in every deployment. Practitioners therefore need to understand how well a pretrained model matches a target deployment and how much adaptation data is left to be collected. We study whether a small set of successful target-domain demonstrations can reveal whether and how much target-domain d...
  </details>

- **2026-11-08** — Lei Shu, Alberta Longhini, Leonidas Guibas et al. — [SoftPAT3D: Physics-Augmented Text-to-3D Scene Generation with Deformables](http://arxiv.org/abs/2611.11087v1)
  <details><summary>📄 Abstract</summary>
  We present SoftPAT3D, a physics-augmented framework for text-to-3D scene generation in which deformable objects, such as cloth, stuffed toys and ropes, are generated as physically valid, simulation-ready bodies and placed in intersection-free contact with the furniture that supports them, with one another and with themselves. Existing physics-augmented pipelines simulate rigid bodies only and cannot accommodate a generated deformable object, which text-to-3D generation returns as a geometrically...
  </details>

- **2026-11-08** — Saleh Mozaffari, Abolfazl Nadi — [Perturbation Profiles of Scanpath Classifiers: What Reading, Code-Comprehension and Video Decoders Are Sensitive To](http://arxiv.org/abs/2611.11632v1)
  <details><summary>📄 Abstract</summary>
  When a scanpath descriptor discriminates a task, it is rarely clear what the discrimination rests on. We propose a perturbation profile for trial-level descriptors. Five transformations each destroy one stated property while preserving a listed set of invariants: fixation order, duration-position coupling, the duration distribution, orientation and handedness, and fine spatial structure. The classifier is refit, and the drop in participant-held-out AUC is the pipeline's sensitivity to that prope...
  </details>

- **2026-11-08** — Samuel Haeuser, Martin Mootz, Dasol Kim et al. — [Coherent Control of High-Order Lightwave Currents in Gate-Tunable Bilayer Graphene](http://arxiv.org/abs/2611.11616v1)
  <details><summary>📄 Abstract</summary>
  The sub-cycle acceleration of charge carriers in an electronic circuit by tailored terahertz (THz) electric-field waveforms, rather than conventional pulsed bias voltages, opens a transformative frontier for lightwave electronics operating far beyond the scaling limits of gigahertz electronic technologies. Yet gate-tunable coherent control of multi-order and non-perturbative currents has remained elusive. Here, we demonstrate lightwave control over the amplitude, phase flips, and zero-crossings ...
  </details>

- **2026-11-08** — Linkai Peng, Baorian Nuchged, Yuyang Yao — [Beyond the Transcript: Measuring and Improving the Use of Acoustic Information in Audio Language Models](http://arxiv.org/abs/2611.11573v1)
  <details><summary>📄 Abstract</summary>
  Audio language model benchmarks provide comprehensive evaluation across diverse tasks. However, some tasks can be answered from the transcript or even the question alone, and benchmark scores can therefore confound acoustic understanding with language modeling ability. We distinguish lexical tasks, for which the transcript usually suffices, from global-attribute and within-recording-structure tasks, which require the model to analyse the recording beyond its words, either as a whole, for propert...
  </details>

- **2026-11-08** — Bian Sun, Kevin Zhai, Mubarak Shah et al. — [Actions Should EARN Their Credit: Test-Time Adaptation and Route Consolidation for Frozen LLM Agents](http://arxiv.org/abs/2611.11565v1)
  <details><summary>📄 Abstract</summary>
  LLM agents can use feedback from repeated attempts to improve their decisions without updating model parameters. However, positive action credits can continue to favor actions that repeatedly achieve the same score, even when higher scores are achievable. Under a fixed interaction budget, trying new actions in the final attempts can also lower performance. We introduce EARN, a method that uses past experience to guide further progress and retain earlier performance through conditional reuse of e...
  </details>

- **2026-11-08** — Jin Gao, Sayjel Vijay Patel — [From Sketch to Design: A Cross-scale Workflow for Procedural Generative Urban Design](http://arxiv.org/abs/2611.11561v1)
  <details><summary>📄 Abstract</summary>
  Urban designers use sketches and symbols to express spatial intentions, while many generative urban design tools rely on numeric parameters that are difficult to relate to this visual process. We propose a cross-scale workflow and a web-based prototype that translates symbolic sketches into controllable procedural urban generation. A vocabulary of shapes, informed by examples of urban design diagrams and sketching exercises with graduate urban design students, encodes attributes such as network ...
  </details>

- **2026-11-08** — Debarshi Kundu, Swaroop Ghosh, Vasant G Honavar — [Weight-Space Programming of Variational Quantum Circuits: Large Language Models Write Quantum Circuit Parameters Without an Optimizer](http://arxiv.org/abs/2611.11537v1)
  <details><summary>📄 Abstract</summary>
  Variational quantum algorithms (VQAs) optimize circuit angles through repeated quantum-device evaluations, often facing vanishing gradients and high optimization costs. We ask whether a large language model (LLM) can write these angles directly. Extending *weight-space programming* from classical networks to quantum circuits, we provide a frontier LLM (\gpt) with the problem, circuit, and gate conventions. Its angles are executed exactly as written, without returning losses, gradients, or accura...
  </details>

- **2026-11-08** — Federico Pennino, Andrea Gurioli, Maurizio Gabbrielli et al. — [SWHForest: A Structural Curation and Search Layer for Large-Scale Code Corpora](http://arxiv.org/abs/2611.11439v1)
  <details><summary>📄 Abstract</summary>
  Pre-training code language models relies on massive code corpora usually streamed over the internet. However, researchers rarely need a multi-terabyte archive in its entirety; instead, their workflow centers on curated subsets: selecting well-documented files, filtering out repetitive boilerplate, auditing for benchmark contamination, or retrieving specific code patterns. Yet, because modern corpora are typically published as file pointers and basic attributes rather than source text, no general...
  </details>

- **2026-11-08** — Guifu Liu, Vera Demberg — [Modeling individual and item differences in atypicality inferences with ACT-R](http://arxiv.org/abs/2611.11416v1)
  <details><summary>📄 Abstract</summary>
  Humans engage in pragmatic reasoning when encountering mentions of highly predictable events. Such mentions may appear redundant, leading comprehenders to infer that the event is atypical, and accommodate this inference with an explanation for why it is atypical. However, these inferences are not drawn uniformly across individuals, and experimental items vary in inference rates due to differences in event typicality. We show that these patterns can be predicted with a resource-rational cognitive...
  </details>

- **2026-11-08** — Rui Zou, Xin Zhao, Mengqi Wei et al. — [BiVerify: Closing the Loop Between Backward and Forward Verification for Mathematical Self-Correction](http://arxiv.org/abs/2611.11368v1)
  <details><summary>📄 Abstract</summary>
  Large language models (LLMs) have made substantial progress in mathematical reasoning but still produce incorrect solutions to complex problems, indicating the need for more reliable self-correction mechanisms. Mathematical self-correction typically identifies errors through verification, which can proceed backward or forward. The two directions provide complementary verification capabilities. Backward verification checks a candidate answer against the original constraints, bypassing complex int...
  </details>

- **2026-11-08** — Xiao Chen, Dong Fang, Haitao Li et al. — [IntentLens: Grounding Underspecified Multimodal Queries for Recommendation via Tool-Augmented Reasoning](http://arxiv.org/abs/2611.11346v1)
  <details><summary>📄 Abstract</summary>
  As intelligent personal assistants are increasingly deployed in real-world scenarios, recommendation paradigms are shifting from passive preference matching to inferring user intent from underspecified multimodal inputs. In practical interactions, users typically issue a reference image paired with a vague natural language query, keeping key visual attributes, personalized preferences, and item-side constraints implicit. Existing recommendation methods either leverage historical user interaction...
  </details>

- **2026-11-08** — Chentao Cao, Zhanke Zhou, Sangni Duan et al. — [Spatial Harness: Grounding Spatial Reasoning in Executable World States with Physics Engines](http://arxiv.org/abs/2611.11344v1)
  <details><summary>📄 Abstract</summary>
  Spatial reasoning requires understanding how objects and observers are arranged in a scene and how their relations change with viewpoint or movement. Vision-language models (VLMs) typically perform both steps through model-internal reasoning, forming an implicit scene interpretation from partial views and imagining the consequences of spatial transformations. A misread scene can lead to a wrong answer, while even a correct interpretation does not ensure that imagined transformations satisfy spat...
  </details>

- **2026-11-08** — Paulo A. Condado, Fernando G. Lobo — [DIY Customized Speech Recognition for a Person with Speech Disabilities](http://arxiv.org/abs/2611.11327v1)
  <details><summary>📄 Abstract</summary>
  General-purpose state-of-the-art automatic speech recognition (ASR) systems fail systematically for speakers with moderate to severe speech disabilities. This paper describes the design, implementation, and evaluation of a customized ASR system built for the first author, a researcher with cerebral palsy and dysarthria. We fine-tuned OpenAI's Whisper medium and large-v3 models using Low-Rank Adaptation (LoRA) on audio samples recorded from the first author's own speech on consumer-grade hardware...
  </details>

- **2026-11-08** — Yu Liu, Xingbang Du — [LoMASA: A Local Multi-Agent Sales Assistant with Confidence-Gated Delegation for B2B Quoting](http://arxiv.org/abs/2611.11234v1)
  <details><summary>📄 Abstract</summary>
  Frontline sales staff spend much of their day re-coordinating quotes after customers change quantities, ask for discounts or new payment terms, or costs move. We present LoMASA (Local Multi-Agent Sales Assistant), a training-free multi-agent system that runs entirely on one desktop computer. A 35B mixture-of-experts model (System-1) makes each decision in a single forward pass and reads its confidence from the probabilities of the answer options. A 27B dense model (System-2) writes customer repl...
  </details>

- **2026-11-08** — Yushuo Li, Xunkai Li, Zhengyu Wu et al. — [TEAM: Topology-Aware, Semantic-Sensitive, General Transformer for Multimodal-Attributed Graphs](http://arxiv.org/abs/2611.11189v1)
  <details><summary>📄 Abstract</summary>
  Multimodal-Attributed Graphs (MAGs) organize heterogeneous data in graphs whose nodes are characterized by modalities such as text and images rather than traditional unimodal attributes. However, many representative MAG methods organize propagation around node-level states and topology-defined neighborhoods, which can obscure fine-grained modality contributions: a bounded neighborhood may contain semantically weak evidence, while compatible context need not be confined to it. To address both lim...
  </details>

- **2026-11-08** — Jaeho Hwang, Sehong Park, Daejin Choi et al. — [The Race Is Decided Early! A Kernel Law Predicts Lock-In in Majority-Vote Test-Time RL](http://arxiv.org/abs/2611.11165v1)
  <details><summary>📄 Abstract</summary>
  Test-time reinforcement learning with majority-vote rewards trains a language model on unlabeled questions by rewarding the samples that agree with its most frequent answer. During training, each question locks into one answer, on hard questions often a wrong one, but which answer it locks into is known only after training. In this paper, we show that this outcome is decided early, in a short race driven by sampling noise between the answers that are close at the start, and we derive the probabi...
  </details>

- **2026-11-08** — Derek Egolf, Stavros Tripakis — [Symbolic Synthesis with Token-Level LLM Guidance](http://arxiv.org/abs/2611.11057v1)
  <details><summary>📄 Abstract</summary>
  We propose a synergistic combination of classical program synthesis techniques and contemporary large language models (LLMs) to solve the problem of recursive program synthesis from first-order logic specifications. Our approach leverages the strengths of both paradigms: we use LLMs as a source of statistical bias to guide the search for a correct program. At the same time we use techniques from classical synthesis to short-circuit on semantically incorrect prefixes and to avoid sampling semanti...
  </details>

- **2026-11-08** — Armin Abdollahi, Negin Ashrafi, Mehdi Kamal et al. — [PRISM: Preference-based Reward and Uncertainty-Integrated Synthesis Minimization for RTL PPA Optimization](http://arxiv.org/abs/2611.11051v1)
  <details><summary>📄 Abstract</summary>
  This paper introduces a budget-aware, multi-objective framework (called PRISM) for RTL optimization that improves power, performance, and area (PPA) while sharply limiting expensive commercial synthesis tool calls. Starting from a synthesizable baseline and functional testbench, the method iterates through LLM-driven rewrite generation, fast compile/simulation equivalence filtering, low-cost proxy feature extraction, and selective commercial synthesis tool (Synopsys Design Compiler (DC)) evaluat...
  </details>

- **2026-11-07** — Kunal Talwar — [Toward a theory of Evaluability](http://arxiv.org/abs/2611.10996v1)
  <details><summary>📄 Abstract</summary>
  Machine learning models, particularly large foundation models, are increasingly evaluated along multiple axes that are relevant for their usage. In addition to accuracy measures appropriate for the specific task of interest, measures capturing safety, calibration and fairness properties are often of interest. The classical approach to these problems assumes that the test set has been held out from the training process, an assumption that is increasingly harder to justify for large foundation mod...
  </details>

- **2026-11-07** — Rajat Bisht, Tevfik Kosar, Anthony Skjellum et al. — [Network Contention State Aware Dynamic Optimizer for Accelerator Collective Communication Libraries](http://arxiv.org/abs/2611.10984v1)
  <details><summary>📄 Abstract</summary>
  Collective Communication Libraries (CCL) are critical for large-scale distributed AI/ML training, yet their configurations are determined by static heuristics that do not account for real-time network conditions. Our empirical study shows that these heuristics perform near-optimally in contention-free environments, but degrade substantially under background traffic. To address this, we present a cooperative multi-agent run-time optimizer for accelerator collective communication. Our approach emp...
  </details>

- **2026-11-07** — Peiming Guo, Jinpeng Huang, Yangbin Sun et al. — [Simple Test-Time Refinement for Plot-to-Code Generation via Visual-Code Diagnostics](http://arxiv.org/abs/2611.10840v1)
  <details><summary>📄 Abstract</summary>
  Plot-to-code generation has been greatly advanced by recent multimodal large language models (MLLMs). However, existing studies mainly focus on one-pass generation or iterative sampling guided by verifier-based filtering, which does not align with the typical human programming workflow of generate first, then iteratively error-location and fix. This naturally motivates a test-time refinement paradigm for plot-to-code generation. In this work, we present the first study on plot-to-code generation...
  </details>

- **2026-11-07** — Guanqi Lyu, Fei Zhao, Zhaojun Lu et al. — [AutoC2V: Synthesis-Guided LLM Training for QoR-Optimized C++-to-Verilog Generation](http://arxiv.org/abs/2611.10824v1)
  <details><summary>📄 Abstract</summary>
  High-level synthesis (HLS) can translate C/C++ kernels into register-transfer level (RTL) designs, yet generating high-quality hardware still relies heavily on manual pragma tuning and repeated synthesis evaluation. We propose AutoC2V, a C++-to-Verilog generation framework driven by real synthesis feedback that enables large language models (LLMs) to directly generate RTL with improved quality of results (QoR) from synthesizable C++ kernels. We construct training data from real synthesis results...
  </details>

- **2026-11-07** — Subin Kim, Anh-Quan Pham, Dinesh Jayaraman — [Zero-Shot VLA Adaptation with Retrieved Guidance](http://arxiv.org/abs/2611.10894v1)
  <details><summary>📄 Abstract</summary>
  Pre-training large parametric "Vision-Language-Action" (VLA) models on large demonstration datasets has recently yielded promising results for general-purpose manipulation. However, these models still struggle under even small domain shifts relative to the training data, such as changes in camera viewpoint, background, object identity, or robot morphology. Motivated by the success of Retrieval-Augmented Generation (RAG) in language models, we pursue retrieval to boost VLA performance. Specifical...
  </details>

- **2026-11-07** — Drishti Goel, Ethan M. Nguyen, Violeta J. Rodriguez et al. — [CompAIssionate Other: Identity Assumptions in LLM Responses to Distress](http://arxiv.org/abs/2611.10808v1)
  <details><summary>📄 Abstract</summary>
  Individuals experiencing suicidal ideation (SI) or psychological distress may disclose their social identities when seeking support from LLMs. Attending to identity-related stressors can be important for providing contextually appropriate and empathetic support. However, disclosing an identity does not necessarily mean that it is a cause of distress. In this work, we audit how LLMs interpret distress through disclosed identities. Using paired counterfactual interventions, we evaluate six LLMs ac...
  </details>

- **2026-11-07** — Bulent Soykan, Murtadha Alsayegh, Sean Mondesire et al. — [Differentiable Agent-Based Modeling for Multi-Echelon Supply Chains: Gradient-Based Optimization of Heterogeneous Policies at Scale](http://arxiv.org/abs/2611.10999v1)
  <details><summary>📄 Abstract</summary>
  Global supply chains rely on the interactions of thousands of heterogeneous agents, posing significant challenges for optimization. While traditional optimization often assumes homogeneity to ensure tractability, Reinforcement Learning struggles with sample inefficiency when scaling to high-dimensional state spaces. We propose a Differentiable Agent-Based Model for multi-echelon inventory management. By implementing stochastic dynamics via differentiable tensor operations, we enable direct gradi...
  </details>

- **2026-11-07** — Katharina Stengg, Christian Macho, Martin Pinzger — [Hybrid Source Code Change Impact Analysis](http://arxiv.org/abs/2611.10958v1)
  <details><summary>📄 Abstract</summary>
  Change impact analysis (CIA) helps developers identify code entities impacted by their initial changes. While several approaches for CIA were proposed, they still struggle with either low precision or low recall, thereby increasing manual effort for developers to verify the results. Furthermore, limitations in the used datasets and experimental setups can bias the results reported by many CIA approaches. In this paper, we first address the dataset limitations by manually labeling 1,931 changed c...
  </details>

- **2026-11-07** — J. Elisenda Grigsby, Yiyao Huang, Arushi Katyal et al. — [Can small transformers learn the language of Coxeter groups?](http://arxiv.org/abs/2611.10936v1)
  <details><summary>📄 Abstract</summary>
  The field of mechanistic interpretability is well-suited to collaborative projects between mathematicians and AI researchers. This work describes one such project. We trained a small transformer to learn the language of the Coxeter group affine A2, best known as the symmetries of the tiling of the Euclidean plane by equilateral triangles. We then formulated and proved a word-theoretic conjecture about affine A2 after observing the attention patterns of the trained model.
  </details>

- **2026-11-07** — Zhiran Zhang, Hu Wang, Yichen Wu et al. — [Remembering to Reason: Structured Memory for Scene and Workflow Understanding in Robot-Assisted Surgery](http://arxiv.org/abs/2611.10917v1)
  <details><summary>📄 Abstract</summary>
  Surgical video understanding is an important foundation for intelligent assistance in robot-assisted surgery. Similar surgical views can reflect different actions or procedural stages. Interpreting these views requires access to earlier observations, yet frame-centric prompting leaves this history unavailable. We introduce MemSurg, a framework that remembers surgical observations before reasoning over them. Its structured memory graph stores timestamped entity categories, locations, motion cues,...
  </details>

- **2026-11-07** — Luv Verma — [Inference for Reasoning Models: Practical Lessons from Evaluation and Serving](http://arxiv.org/abs/2611.10845v1)
  <details><summary>📄 Abstract</summary>
  Running a language model involves more than its trained weights. The same model can receive very different benchmark scores, produce different answers, or cost more to serve depending on how it is evaluated and run. In one experiment in this book, changing only the maximum response length moved accuracy on a math benchmark from 0.08% to 93.18%.   This book explains how inference settings shape the results we report and the systems we deploy. We begin with evaluation, including generation limits,...
  </details>

- **2026-11-07** — Donglin Sui, Mohammad Deghat — [Integral Compensation for Discrete-time Bearing-only Target Localization and Circumnavigation](http://arxiv.org/abs/2611.10762v1)
  <details><summary>📄 Abstract</summary>
  This paper investigates the discrete-time control problem of driving an agent to localize and circumnavigate an unknown target at a prescribed radius using bearing measurements. Discretizing existing continuous-time circumnavigation controllers can introduce steady-state orbit bias, even at sampling rates that preserve stability. To eliminate the sampling-induced orbit bias, we propose an adaptive compensator for a circumnavigation controller formulated directly in discrete time. Driven by the e...
  </details>

- **2026-11-06** — Osamudiamen Edogun, Joshua Obigwe, Irfan Mehmood — [Compaction, decay and reinforcement in a two-tier conversational memory: a paired evaluation against retrieval-augmented generation](http://arxiv.org/abs/2611.09807v1)
  <details><summary>📄 Abstract</summary>
  A conversational agent that remembers has to decide what to keep. Retrieval-augmented generation keeps the transcript and searches it; the alternative is to compact each turn into atomic facts and search those. We compare the two on LoCoMo, with both arms answering all 1,985 questions in one window, against the same stores, with the same generator and judge, and both predictions on one row, which licenses McNemar's exact test on the 512 questions where they disagree.   On the four categories com...
  </details>

- **2026-11-06** — Chang Rajani, Luke Sebastien Marsden, Stephan Kunz et al. — [Autonomous Particle Image Velocimetry Using Zero-Shot Sim-to-Real Reinforcement Learning](http://arxiv.org/abs/2611.09679v1)
  <details><summary>📄 Abstract</summary>
  Particle image velocimetry (PIV) reconstructs a flow field from the motion of tracer particles but the reconstruction quality is bounded by how well the flow structure of interest is resolved in the images. The acquisition position is typically fixed by the operator before the measurement. We cast camera placement as a sequential decision-making problem and train a reinforcement learning agent to control a 6-DoF manipulator equipped with a camera, enabling it to locate, frame and resolve a hydro...
  </details>

- **2026-11-06** — Ernesto Mordecki — [Hostages](http://arxiv.org/abs/2611.09580v1)
  <details><summary>📄 Abstract</summary>
  Our house has been taken over. It is not completely destroyed, but many of its essential functions and facilities no longer work as they used to. Essentially, they are out of our control. Artificial intelligence, through its large language models (LLMs), has taken it. And we, the inhabitants of the house, without really noticing what was happening, and surprised by the effectiveness of LLMs, have handed over our most sacred belongings: the capacity to think about a problem, the joy of having an ...
  </details>

- **2026-11-06** — Eduardo C. Garrido-Merchán — [Zero-Shot Weight-Space Programming Across a Difficulty-Graded Ladder of Two-Player Games](http://arxiv.org/abs/2611.09271v1)
  <details><summary>📄 Abstract</summary>
  Weight-space programming sets every weight of a feed-forward network by hand, from an explicit specification of the desired computation, with no gradient descent and no training data anywhere in the construction. We ask how far a large language model can carry this practice, zero-shot, across games of deliberately increasing difficulty. We design a four-rung ladder (Nim, tic-tac-toe, two sizes of Connect Four, and a chess endgame) spanning four axes of difficulty, and build a second, independent...
  </details>

- **2026-11-06** — Xiaoyong Yu, Xinge Yu — [Grounding-Aware Judge Reward Reinforcement Learning for Out-of-Domain Face Anti-Spoofing](http://arxiv.org/abs/2611.09047v1)
  <details><summary>📄 Abstract</summary>
  Face Anti-Spoofing (FAS) must distinguish genuine faces from presentation attacks. A unified Multimodal Large Language Model (MLLM) is an attractive solution: it detects physical attacks (print, replay, mask) in one model and produces interpretable forensic evidence via Chain-of-Thought (CoT). A central obstacle to post-training such a model with reinforcement learning is that FAS reasoning has no rule-verifiable ground truth: only the binary verdict is checkable, while the reasoning chain canno...
  </details>

- **2026-11-06** — Aubin Charley, Julien Khlaut, Charles Corbière et al. — [Can Agentic Systems Close the Gap in Radiology with Production AI Tools?](http://arxiv.org/abs/2611.09836v1)
  <details><summary>📄 Abstract</summary>
  Radiology AI has developed along two paths: specialized models that perform well on narrow tasks but cover few clinical findings, and generalist models that address a broader range of tasks but remain prone to hallucination and inaccurate measurements. Combining the two through agentic systems offers a route towards comprehensive radiology reporting, but published systems are tied to one modality or body part. We describe a radiology agentic framework that standardizes how an orchestrator calls ...
  </details>

- **2026-11-06** — Dongxu Wu, Sara Court, Micha Elsner — [Are These Programmers Ripe Enough to Eat? Evaluating How LLMs Handle Lexical Knowledge Conflicts in Translation](http://arxiv.org/abs/2611.09785v1)
  <details><summary>📄 Abstract</summary>
  External lexical resources can help large language models (LLMs) translate texts in low-resource languages and specialized domains, but these resources may conflict with models' prior lexical knowledge. To isolate this conflict, we construct a controlled Mandarin-to-English translation task in which familiar source words are assigned new meanings within and across semantic categories. We treat these prompt-supplied meanings as contextual knowledge (CK) and systematically evaluate the effects of ...
  </details>

- **2026-11-06** — Zhongyi Zhang, Jingyu Xiao, Shuqing Li et al. — [AnimWeb-Bench: Benchmarking Animated Webpage Code Generation from Videos](http://arxiv.org/abs/2611.09769v1)
  <details><summary>📄 Abstract</summary>
  Animation is pervasive on the Web, the CSS animation property alone appears on over three-quarters of webpages. Yet existing webpage code generation benchmarks target static screenshots, user-triggered interactions, or isolated motion graphics, leaving the ability of multimodal large language models (MLLMs) and coding agents to reconstruct complete animated webpages largely unexplored. To fill this gap, we introduce AnimWeb-Bench, the first benchmark for animated webpage code generation from vid...
  </details>


## 📊 统计 / Statistics

| 分类 / Category | 论文数 / Count |
|------|--------|
| jailbreak | 718 |
| prompt-injection | 677 |
| memory-poisoning | 59 |
| tool-use-attack | 174 |
| backdoor | 556 |
| adversarial-attack | 667 |
| privacy-leakage | 4572 |
| steganography | 90 |
| misuse | 1307 |
| red-teaming | 150 |
| vulnerability | 3973 |
| defense | 3876 |
| alignment | 3627 |
| robustness | 3964 |
| watermark | 740 |
| unlearning | 120 |
| agent-safety | 67 |
| benchmark | 75 |
| survey | 449 |
| other | 10875 |

---

📚 **全部 36736 篇论文**（2022 至今）请访问 [GitHub Pages](https://ny1024.github.io/AgentSafety-Papers/) 查看完整列表、搜索与筛选。

*Generated by AgentGuard at 2026-11-12 23:06:10*