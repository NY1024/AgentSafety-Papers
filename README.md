<div align="center">

# AgentGuard 🛡️

**Daily Tracking of LLM Agent Security Papers on arXiv**

[![Auto Update](https://github.com/NY1024/AgentSafety-Papers/actions/workflows/daily-update.yml/badge.svg)](https://github.com/NY1024/AgentSafety-Papers/actions/workflows/daily-update.yml)
[![Papers](https://img.shields.io/badge/Papers-22033-blue)](#)
[![License](https://img.shields.io/badge/License-MIT-green)](#)

</div>

---

## 📖 简介 / Introduction

自动追踪 arXiv 上大模型 Agent 安全方向的最新论文，每日更新，关键词智能分类。

*Automatically tracking the latest LLM Agent security papers on arXiv, updated daily with keyword-based classification.*

**最近更新 / Last Updated**: 2026-08-04 08:28 ｜ **论文总数 / Total Papers**: 22033（近 30 天 / Recent 30 days: 2308）

🌐 **[GitHub Pages](https://ny1024.github.io/AgentSafety-Papers/)** — 查看全部 22033 篇论文（含摘要、分类筛选、搜索）/ View all 22033 papers with abstracts, filters & search

## 📑 分类导航 / Category Navigation

- **[jailbreak](#-jailbreak)** — 越狱攻击 / Jailbreak Attacks — 559
- **[prompt-injection](#-prompt-injection)** — 提示注入攻击 / Prompt Injection Attacks — 467
- **[memory-poisoning](#-memory-poisoning)** — 记忆投毒与篡改 / Memory Poisoning & Tampering — 40
- **[tool-use-attack](#-tool-use-attack)** — 工具使用攻击 / Tool-Use Attacks — 95
- **[backdoor](#-backdoor)** — 后门与投毒攻击 / Backdoor & Poisoning Attacks — 399
- **[adversarial-attack](#-adversarial-attack)** — 对抗攻击 / Adversarial Attacks — 542
- **[privacy-leakage](#-privacy-leakage)** — 隐私泄露 / Privacy Leakage — 3735
- **[steganography](#-steganography)** — 隐写与隐蔽通信 / Steganography & Covert Communication — 54
- **[misuse](#-misuse)** — 滥用与误用 / Misuse & Abuse — 845
- **[red-teaming](#-red-teaming)** — 红队测试 / Red Teaming — 110
- **[vulnerability](#-vulnerability)** — 漏洞与攻击面 / Vulnerabilities & Attack Surfaces — 2533
- **[defense](#-defense)** — 防御与防护方法 / Defense & Protection Methods — 2199
- **[alignment](#-alignment)** — 对齐与安全约束 / Alignment & Safety Constraints — 2030
- **[robustness](#-robustness)** — 鲁棒性与可靠性 / Robustness & Reliability — 1969
- **[watermark](#-watermark)** — 水印与溯源 / Watermarking & Provenance — 231
- **[unlearning](#-unlearning)** — 机器遗忘 / Machine Unlearning — 84
- **[agent-safety](#-agent-safety)** — Agent 安全框架 / Agent Safety Frameworks — 52
- **[benchmark](#-benchmark)** — 安全评测与基准 / Safety Benchmarks & Evaluation — 53
- **[survey](#-survey)** — 综述与系统化 / Surveys & Systematization — 261
- **[other](#-other)** — 其他安全相关 / Other Security-Related — 5775

## 📄 近期论文 / Recent Papers (Last 30 Days)

> 仅展示最近 30 天中最新的 500 篇论文（含日期、作者、摘要）。近 30 天共 2308 篇，完整 22033 篇论文列表请访问 [GitHub Pages](https://ny1024.github.io/AgentSafety-Papers/)

> Showing the latest 500 of 2308 papers from the last 30 days (with date, authors & abstract). For the full list of 22033 papers, visit [GitHub Pages](https://ny1024.github.io/AgentSafety-Papers/)

### 📂 jailbreak
*越狱攻击 / Jailbreak Attacks* — 4 papers

- **2026-08-02** — Simiao Xie, Chuancheng Shi, Shangze Li et al. — [No Single Neuron of Failure: Distributed Safety Alignment Against White-Box Attacks](http://arxiv.org/abs/2608.01414v1)
  <details><summary>📄 Abstract</summary>
  With the rapid release of open-weight large foundation models, safety threats are shifting from black-box jailbreaks to neuron-level white-box attacks that directly identify and manipulate safety-related neurons. Existing alignment methods often investigate the safety behavior on a small number of neurons, creating fragile single point of failure with limited redundancy. To address this issue, we propose distributed safety alignment (DSA), which redundantly encodes safety capabilities across mul...
  </details>

- **2026-08-02** — Siyuan Li, Aodu Wulianghai, Zehao Liu et al. — [SoK: Intent-Oriented Systematization of Multi-Turn LLM Jailbreaks](http://arxiv.org/abs/2608.01117v1)
  <details><summary>📄 Abstract</summary>
  Large Language Models (LLMs) are increasingly deployed in interactive settings, where user intent commonly unfolds through multi-turn dialogue. Multi-turn jailbreaks exploit this pattern by advancing a harmful intent across turns, so that no single message exposes the full objective. However, existing work treats these attacks as a loose collection of prompt patterns and does not analyze how the adversary organizes and advances harmful intent across an interaction. We develop a four-part, intent...
  </details>

- **2026-08-02** — Haoyu Zhang, Xiangchen Guan, Shibo Zheng et al. — [Decoy Images Amplify Caption-Mediated Defenses Against Encoded Jailbreaks](http://arxiv.org/abs/2608.01043v1)
  <details><summary>📄 Abstract</summary>
  We report a counter-intuitive interaction between image inputs and existing black-box defenses on Vision--Language Models (VLMs): pairing an encoded jailbreak prompt with an unrelated decoy image can sharply lower attack success rate (ASR). The operative change is in the defense pipeline, not in the image. Across five frontier VLMs, two encoded-attack families, and three black-box defenses, a caption-mediated defense (ECSO) that leaves ASR essentially unchanged on text-only encoded input drops i...
  </details>

- **2026-07-30** — Xiangyu Yin, Tora Bodin, Rohan Menon et al. — [A Cross-Architecture Audit of Direction-Based Inference-Time Defences in Vision-Language Models](http://arxiv.org/abs/2607.27910v1)
  <details><summary>📄 Abstract</summary>
  Inference time defences against vision language model jailbreaks often subtract a calibrated direction from the residual stream at a chosen decoder layer. We compare five defence candidates across 15 model and layer cells from four architectural families under a magnitude controlled protocol that matches the intervention size for each prompt and pairs every direction with a random control of the same norm. The candidates are the mean image conditioning shift, a CMRM style refusal direction, a Sh...
  </details>


### 📂 prompt-injection
*提示注入攻击 / Prompt Injection Attacks* — 9 papers

- **2026-08-03** — Jia-Chen Zhang, Ze-Yu Zhang, Kai-Wei Zhang — [Invisible Ink Threats: Adversarial Goals Behind Legitimate Tasks in Computer-Use Agents](http://arxiv.org/abs/2608.02018v1)
  <details><summary>📄 Abstract</summary>
  Computer-use agents (CUAs), which empower large language models to autonomously operate operating systems and the web, are increasingly vulnerable to indirect prompt injection attacks. A widely adopted defense is the human-in-the-loop paradigm, in which the agent pauses for explicit user confirmation before executing sensitive operations. While effective against conspicuously high-harm attacks, this defense offers little protection against what we term Invisible Ink Threats: low-harm injected go...
  </details>

- **2026-08-03** — Qianlong Yang, Bowen Ye, Xianda Guo et al. — [Mitigating Visual Degradation in MLLMs via Spatial-Spectral Visual Anchor Learning](http://arxiv.org/abs/2608.01635v1)
  <details><summary>📄 Abstract</summary>
  Despite the progress of multimodal large language models (MLLMs), they continue to exhibit deficiencies in visual perception. Following visual instruction tuning, internal MLLM representations rapidly deviate from their original semantic states during inference, causing severe information degradation. While existing methods attempt to leverage external vision foundation models (VFMs) to align internal representations, we find that direct alignment with VFMs enhances visual semantics but fails to...
  </details>

- **2026-08-02** — Amir Ahmad Ghods, Mohammadreza Doostmohammadian — [Resilient Consensus-Based Target Tracking under False Data Injection Attacks in Multi-Agent Networks](http://arxiv.org/abs/2608.01222v1)
  <details><summary>📄 Abstract</summary>
  Distributed target tracking in multi-agent networks plays a critical role in cooperative sensing and autonomous navigation. However, it faces significant challenges in highly dynamic and adversarial setups. This study aims to enhance the resilience of decentralized target tracking algorithms against measurement faults and cyber-physical threats, especially false data injection attacks. We propose a consensus-based estimation algorithm that integrates a nearly-constant-velocity model with saturat...
  </details>

- **2026-08-02** — Fred Zimmerman — [Copyright Is the Headline; Capability Is the Blind Spot: AI Technology in the Book-Publishing Trade Press, November 2025--August 2026](http://arxiv.org/abs/2608.00964v1)
  <details><summary>📄 Abstract</summary>
  This rapid evidence review examines 89 articles about artificial intelligence (AI) and book publishing published from November 1, 2025 through August 1, 2026. The purposive corpus spans English-, Chinese-, German-, French-, Spanish-, Portuguese-, Italian-, and Japanese-language publishing coverage; major-newspaper book coverage; and specialist technology commentators. Each item was coded for topic, stance, technical depth, and dominant voice. The press is neither silent nor simply hostile: 30% o...
  </details>

- **2026-08-01** — Neha Nagaraja, Amisha Bagari, Hayretdin Bahsi — [When Prompts Control Robots: Prompt Injection Attacks in Multi-Agent Robotic Systems](http://arxiv.org/abs/2608.00747v1)
  <details><summary>📄 Abstract</summary>
  Large language models are increasingly integrated into autonomous robotic systems for task planning and control, but this integration exposes them to prompt injection attacks that can lead to unsafe decisions and physical harm. Multi-agent settings increase the risks through cross-agent contamination and broader attack surfaces. In this paper, we evaluate prompt injection attacks against an LLM-based multi-agent robotic system, considering both direct injections into task instructions and indire...
  </details>

- **2026-07-31** — Minghui Pan, Jiayuxuan Yang, Yuanyuan Yuan et al. — [Tool Specifications Matter: Uncovering and Mitigating Safety Risks in AI Agents](http://arxiv.org/abs/2607.29254v1)
  <details><summary>📄 Abstract</summary>
  AI agents extend large language models (LLMs) with external tools, enabling them to perform complex tasks and translate model outputs into consequential real-world actions. Yet LLMs often become substantially less safe when deployed as agents, and the source of this degradation remains poorly understood. In this paper, we identify schema-formatted tool specifications as a primary source of agent safety degradation and show, through white-box representation analysis, that they weaken the model's ...
  </details>

- **2026-07-30** — Mingxiao Liu, Yitong Li, Haoren Zhao et al. — [Piggybacking on Perception: Stealthy Concurrent Audio Prompt Injections against Multimodal LLM Agents](http://arxiv.org/abs/2607.28165v1)
  <details><summary>📄 Abstract</summary>
  Large Language Model (LLM)-driven multimodal agents are increasingly deployed to execute autonomous tasks via continuous audio interaction. While this paradigm enhances interaction naturalness, it introduces a critical yet under-explored attack surface, as audio inputs inevitably contain environmental noise beyond user control. In this paper, we investigate concurrent audio prompt injection attacks targeting multimodal agents. Distinct from traditional acoustic attacks on voice devices, we propo...
  </details>

- **2026-07-30** — Dongyi Liu, Haixing He, Xiaobao Wu et al. — [MIND: Lightweight and Effective Memory Injection Defense for LLM Agents via Intent-Aware Information Bottleneck](http://arxiv.org/abs/2607.28103v1)
  <details><summary>📄 Abstract</summary>
  Memory-augmented LLM-based agents are vulnerable to memory injection attacks: Agents may retrieve poisoned memory from attackers, which diverts their behavior from initial user intent and finally causes task failure. However, existing defense mechanisms either incur high computational cost or suffer from information redundancy in multi-turn contexts. To address these challenges, we propose Memory Intent-Aware Neural Denoising(MIND), a lightweight defense framework for memory injection attack. Ou...
  </details>

- **2026-07-30** — Jin-Seong Kim, Han-Ju Lee, Seok-Won Hong et al. — [Don't Trust the AI Ecosystem: Analyzing Privacy Leakage in Compromised Open-Source Components](http://arxiv.org/abs/2607.27886v1)
  <details><summary>📄 Abstract</summary>
  Existing model inversion (MI) attacks predominantly rely on post-training optimization to recover private data from model outputs. However, these methods are fundamentally constrained by the target model's generalization bottleneck, often yielding generic features rather than specific identities, particularly on high-dimensional datasets. In this paper, we introduce GradLock, a novel training-time injection attack that stealthily injects sensitive training data directly into the model parameters...
  </details>


### 📂 memory-poisoning
*记忆投毒与篡改 / Memory Poisoning & Tampering* — 3 papers

- **2026-08-03** — Bingyu Yan, Xiaoming Zhang, Chaozhuo Li et al. — [Benign Alone, Harmful Together: Exploiting Experience Composition in Self-Evolving LLM Agents](http://arxiv.org/abs/2608.01759v1)
  <details><summary>📄 Abstract</summary>
  Self-evolving large language model agents improve their capabilities by distilling interaction trajectories into persistent experiences. Yet this mechanism introduces a new safety risk: experiences that are benign in isolation may jointly weaken an agent's safety boundary when accumulated and reused across sessions. Existing memory attacks typically require direct memory access or induce explicitly malicious records, limiting their stealthiness and applicability. We propose EvoBreak, an experien...
  </details>

- **2026-08-03** — Zheng Lin, Yuzhe Huang, Zhenxing Niu et al. — [Salami Attack: Stealthy Collusive Memory Poisoning against OpenClaw](http://arxiv.org/abs/2608.01637v1)
  <details><summary>📄 Abstract</summary>
  Long-term memory enables LLM agents to retain useful information across sessions, but also creates an attack surface through which adversaries may poison an agent's persistent memory to steer its behavior. Existing memory poisoning attacks mainly rely on individually malicious records, overlooking a compositional threat: multiple benign-looking memories may jointly induce unsafe behavior. In this paper, we introduce MemCollusion, an automated red-teaming framework for constructing collusive memo...
  </details>

- **2026-08-01** — Faisal Haque Bappy, Tahrim Hossain, Tarannum Shaila Zaman et al. — [Adversarial Attacks in Multi-Agent LLM Pipelines: Unveiling Structural Vulnerabilities in Agentic AI Architectures](http://arxiv.org/abs/2608.00718v1)
  <details><summary>📄 Abstract</summary>
  Multi-agent LLM pipelines orchestrate multiple specialized language model agents into structured workflows where intermediate outputs are passed across agents to solve complex tasks. This design introduces a security gap absent in single-agent settings: once an agent accepts adversarial content, it is propagated as trusted input throughout the pipeline. We argue that this vulnerability stems from the absence of boundary verification, a security primitive that enforces explicit validation of data...
  </details>


### 📂 tool-use-attack
*工具使用攻击 / Tool-Use Attacks* — 1 papers

- **2026-07-30** — Fuwei Yang, Weiheng Li, Bai Song — [Vibe-FDTR: An agent-oriented framework for reproducible frequency-domain thermoreflectance data analysis](http://arxiv.org/abs/2607.28200v1)
  <details><summary>📄 Abstract</summary>
  Frequency-domain thermoreflectance (FDTR) is a laser pump-probe technique widely used to measure thermal properties at the micro- and nanoscale; however, it relies on a complex data analysis procedure that demands substantial domain expertise and is susceptible to subtle human errors. Here, we present Vibe-FDTR, an agent-oriented framework that enables large language model (LLM) agents to perform reliable and reproducible FDTR analyses directly from natural language requests. This framework coup...
  </details>


### 📂 backdoor
*后门与投毒攻击 / Backdoor & Poisoning Attacks* — 5 papers

- **2026-08-03** — Nicola Pitzalis, Donald Shenaj, Giacomo Cignoni et al. — [Z-PEFT: Zero-shot Backdoor Detection in Parameter-Efficient Fine-Tuning via Canonical Spectral Signatures](http://arxiv.org/abs/2608.02271v1)
  <details><summary>📄 Abstract</summary>
  Parameter-Efficient Fine-tuned (PEFT) models are frequently downloaded from open repositories by practitioners. This widespread practice creates a significant attack surface, as malicious actors can publish backdoored models that induce specific behaviors in response to predefined triggers. We study the problem of weight-space backdoor detection, where a detector classifier predicts whether a model is malicious using only its weights, enabling a lightweight safety mechanism. Most existing method...
  </details>

- **2026-08-02** — Jia-Hao Xiao, Lei Feng, Min-Ling Zhang — [When Collaboration Becomes a Trigger: Collective Evidence-Threshold Backdoors in Multi-Agent Systems](http://arxiv.org/abs/2608.01085v1)
  <details><summary>📄 Abstract</summary>
  LLM-based multi-agent systems (MAS) extend LLM capabilities through iterative communication and shared contexts. However, this collaboration introduces a vulnerability: backdoor behavior can be activated when peer evidence reaches a hidden threshold, rather than being determined by any single message. We introduce a collective evidence-threshold backdoor paradigm for MAS and Boundary-Conditioned Backdoor Injection (BCBI), which constructs counterfactual boundary pairs to separate benign behavior...
  </details>

- **2026-08-01** — Wenjun Xiong, Yijin Zhou, Jiaqian Wang et al. — [MAPLE-Guard: Memory-Aware Link Enforcement Against Memory-Link Poisoning in Multi-Agent Systems](http://arxiv.org/abs/2608.00426v1)
  <details><summary>📄 Abstract</summary>
  LLM-based multi-agent systems (MAS) increasingly rely on persistent private and shared memories for long-horizon coordination. This memory layer improves continuity, but it also gives attackers a durable channel: a poisoned memory can be written once, continuously retrieved in later tasks, promoted into shared memory, and reused by other agents. A single poisoned write can therefore steer many later decisions and contaminate agents that never saw the original attack, all while no malicious messa...
  </details>

- **2026-07-30** — Roberto Riaño, Gorka Abad, Stjepan Picek et al. — [Temporal Poisoning: Clean-Label Backdoors via Event Redistribution in SNNs](http://arxiv.org/abs/2607.28075v1)
  <details><summary>📄 Abstract</summary>
  Backdoor attacks on Spiking Neural Networks (SNNs) have primarily assumed dirty-label poisoning, in which triggered training samples are relabeled to an attacker-selected class. We study clean-label temporal poisoning, where a fixed timestamp transformation is applied only to the target-class training streams, leaving their labels unchanged. The transformation preserves the per-pixel, per-polarity event count exactly, making clean and triggered samples identical after temporal aggregation while ...
  </details>

- **2026-07-30** — Cheng Wei — [TriShield: Zero-Utility-Loss Defense Against Privacy Backdoors in Federated Language Model Fine-Tuning via Orthogonal Gradient Projection and Optimizer State Entanglement](http://arxiv.org/abs/2607.27940v1)
  <details><summary>📄 Abstract</summary>
  Federated fine-tuning of large language models (LLMs) enables collaborative training without exposing raw data. However, a recent attack, NeuroImprint [1] (arXiv:2606.20553), demonstrates that a malicious parameter server can corrupt a PEFT adapter into a privacy backdoor: by assigning a dedicated memorization neuron to each training sample and ensuring each neuron updates at most once, the server can analytically reconstruct 59\%--79\% of client training data with high semantic fidelity. Existi...
  </details>


### 📂 adversarial-attack
*对抗攻击 / Adversarial Attacks* — 5 papers

- **2026-08-03** — Nan Chen, Zhouhao Yang, Soufiane Hayou — [Training-Free versus Training-Based Intent Classification in LLMs: Accuracy, Robustness, and Failure Modes](http://arxiv.org/abs/2608.02415v1)
  <details><summary>📄 Abstract</summary>
  Intent classification in Large Language Models (LLMs) involves categorizing user prompts into predefined classes. For instance, given a user prompt, the system must determine whether it primarily concerns mathematics, coding, or general text processing. Such classification enables routing prompts to specialized models optimized for specific domains, improving both accuracy and computational efficiency. In this work, we conduct a systematic study comparing training-free vs training-based approach...
  </details>

- **2026-08-03** — Xuanhui Lin, Junhao Dong, Mingrong Gong et al. — [Two Sides of the Same Coin: Co-Evolving Search for Cross-Task Attacks on Vision-Language Models](http://arxiv.org/abs/2608.02137v1)
  <details><summary>📄 Abstract</summary>
  Vision-language models (VLMs) exhibit strong generalization across multimodal tasks but remain vulnerable to adversarial perturbations. Existing attacks typically follow single-trajectory gradient optimization or task-specific objectives, limiting search-space exploration and cross-task transferability. We propose an evolutionary-computation-guided cross-modal attack framework for unified VLMs. The framework adaptively searches both textual and visual spaces. On the textual side, it evolves hard...
  </details>

- **2026-08-02** — Tobias Braun, Jonas Grebe, Louis Rethfeld et al. — [Fighting Fire with Fire: On the Feasibility of Protecting Exercises Against AI Cheating](http://arxiv.org/abs/2608.01112v1)
  <details><summary>📄 Abstract</summary>
  The widespread adoption of generative AI enables students to outsource cognitive effort to increasingly capable assistants, creating an illusion of competence while undermining the independent reasoning that education aims to cultivate. We investigate whether adversarial machine learning can be repurposed to protect educational exercises against such corrosive reliance. Our approach uses multimodal multiple-choice questions whose visual components can be protected with subtle visual perturbation...
  </details>

- **2026-08-02** — Hashmat Shadab Malik, Toluwani Aremu, Samuele Poppi et al. — [ReACT-CLIP: Response-Aware Test-Time Defense for Vision--Language Models](http://arxiv.org/abs/2608.01067v1)
  <details><summary>📄 Abstract</summary>
  Training-free test-time defenses offer a practical way to improve the adversarial robustness of CLIP-style vision--language models without modifying the pretrained model. However, their correction strength is typically fixed for a narrow range of attack budgets, even though the attack budget is unknown at inference and the required correction varies across samples. We show that this mismatch causes existing defenses to degrade sharply as attacks strengthen. We introduce ReACT-CLIP, a response-co...
  </details>

- **2026-07-30** — Nguyen Duc Thai, Junhao Dong, Sua Qi Rong et al. — [Unifying Adversarially Robust Model Experts in Vision-Language Models](http://arxiv.org/abs/2607.27897v1)
  <details><summary>📄 Abstract</summary>
  Vision-language models (VLMs), such as CLIP, are vulnerable to adversarial attacks, posing a serious problem for real-life applications and deployment. Adversarial fine-tuning emerges as a prominent defense method; however, different fine-tuning strategies often produce specialized models with distinct robustness characteristics. Each fine-tuned model in turn thrives in some evaluation settings but falters on others, limiting their defensive capabilities. We refer to these specialized fine-tuned...
  </details>


### 📂 privacy-leakage
*隐私泄露 / Privacy Leakage* — 22 papers

- **2026-08-03** — Vincenzo Longo, Alberto Verna, Nikhil Jha et al. — [Lost in Permissions: Exploring the Microsoft 365 App Ecosystem](http://arxiv.org/abs/2608.02336v1)
  <details><summary>📄 Abstract</summary>
  The Microsoft 365 (M365) ecosystem hosts thousands of third-party applications that integrate with enterprise tenants via fine-grained OAuth permissions, potentially granting access to sensitive organisational resources such as emails, files, calendars, chats, and user directories. Despite the security implications of these permission grants, the M365 ecosystem has not been systematically studied.   We present the first privacy- and security-oriented measurement of M365 third-party applications....
  </details>

- **2026-08-03** — Zirui Huang, Yunlong Mao, Wei Tong et al. — [Auditing Data Provenance in LLM Fine-tuning via Intrinsic Distributional Fingerprints](http://arxiv.org/abs/2608.02154v1)
  <details><summary>📄 Abstract</summary>
  The proliferation of customized Large Language Models (LLMs) poses critical risks of Data Intellectual Property (Data IP) infringement via unauthorized fine-tuning on proprietary data. Existing audit techniques are limited, as they require intervention during data preparation or training and remain fragile under malicious obfuscations such as data paraphrasing and knowledge distillation.   We propose \textit{Distribution Provenance Audit (DPA)}, a post-hoc framework for auditing data IP infringe...
  </details>

- **2026-08-03** — Mohamed ElBassat, Seifeldin Elkerdany, Mohamed ElBialy et al. — [Calibrated Similarity and Graph Clustering for Open-Set Animal Re-Identification](http://arxiv.org/abs/2608.02469v1)
  <details><summary>📄 Abstract</summary>
  AnimalCLEF26 addresses discovery-oriented animal re-identification, where systems must both attach query images to known individuals and discover unseen individuals by clustering them correctly. We present a similarity-to-clustering pipeline for this setting across Eurasian lynx, fire salamander, loggerhead sea turtle, and Texas horned lizard images. The method first isolates the target specimen using segmentation and then applies lightweight species-specific preprocessing for lynx, sea turtle, ...
  </details>

- **2026-08-03** — Abdullah Mamun, Shovito Barua Soumma, Hassan Ghasemzadeh — [Trustworthy AI in Digital Health: A Comprehensive Review of Robustness and Explainability](http://arxiv.org/abs/2608.02238v1)
  <details><summary>📄 Abstract</summary>
  Ensuring trust in AI systems is essential for the safe and ethical integration of machine learning systems into high-stakes domains such as digital health. Key dimensions, including robustness, explainability, fairness, accountability, and privacy, need to be addressed throughout the AI lifecycle, from problem formulation and data collection to model deployment and human interaction. While various contributions address different aspects of trustworthy AI, a focused synthesis on robustness and ex...
  </details>

- **2026-08-03** — Jinghan Xu, Longze Fan, Zeyuan Wang et al. — [MNC: Scope-Bound Semantic Declassification for Private LLM-Agent Communication](http://arxiv.org/abs/2608.01719v1)
  <details><summary>📄 Abstract</summary>
  Multi-agent large language model (LLM) systems can expose protected state through internal messages, tool arguments, logs, and persistent memory even when their public outputs appear innocuous. Existing privacy prompts, redaction methods, and source-level access controls restrict surface content or data access, but do not specify what a legitimately informed agent should disclose or how that disclosure may be reused downstream. We introduce Minimum-Necessary Communication (MNC), a typed semantic...
  </details>

- **2026-08-03** — Anne Josiane Kouam, Hristo Boyadzhiev, Konrad Rieck — [Secrets Everywhere: Auditing Memorization in Mobility Prediction Models](http://arxiv.org/abs/2608.02052v1)
  <details><summary>📄 Abstract</summary>
  Human mobility prediction models, which forecast the next location in a user's trajectory, are increasingly deployed in urban analytics, navigation, and personalized services. Yet, little is known about their potential to memorize and expose sensitive user trajectories from training data. While memorization has been extensively studied in language models, mobility prediction poses unique challenges: training sequences encode human behavior at various spatial and temporal scales, creating privacy...
  </details>

- **2026-08-03** — Jiawei Cao, Junyi Feng, Jiashen Hua et al. — [Illuminating Visual Identity in Universal Multimodal Embeddings](http://arxiv.org/abs/2608.01794v1)
  <details><summary>📄 Abstract</summary>
  Universal Multimodal Embeddings (UMEs) aim to unify various modalities and tasks into a shared representation space. In recent years, this field has witnessed substantial progress driven by the development of Multimodal Large Language Models (MLLMs). However, a crucial capability, visual identity discrimination, remains underexplored in existing UME methods, despite its critical role in a wide range of tasks, including instance retrieval, re-identification, and identity preservation in AI-genera...
  </details>

- **2026-08-03** — Shicheng Xu, Liang Pang, Liyi Chen et al. — [RING: Retrieval-Internalized Generation for Continual Large-Scale Knowledge Injection](http://arxiv.org/abs/2608.01630v1)
  <details><summary>📄 Abstract</summary>
  Retrieval-augmented generation (RAG) improves factuality but adds latency and engineering overhead at serving time. We propose RING (Retrieval-Internalized Generation), a holistic paradigm spanning both architecture and training that injects large-scale external knowledge into a \textit{Mixture-of-Memory Experts} and learns parametric search over this internal memory via reinforcement learning, removing the external retriever entirely. Training proceeds in three stages: continued pre-training in...
  </details>

- **2026-08-02** — Hasin Us Sami, Swapneel Sen, Basak Guler — [MineGrad: Gradient Inversion Attacks on LoRA Fine-Tuning](http://arxiv.org/abs/2608.01521v1)
  <details><summary>📄 Abstract</summary>
  Parameter-efficient fine-tuning (PEFT), such as low-rank adaptation (LoRA), has recently been adopted in federated learning to reduce communication and computation costs. In this setup, users download a pretrained model from the server prior to fine-tuning, and then fine-tune lightweight LoRA modules locally while keeping the pretrained model frozen, sharing only the gradients of the fine-tuning parameters with the server. Despite its growing popularity, robustness of federated fine-tuning again...
  </details>

- **2026-08-02** — Phuc Hoang Truong Huynh, Dung Tran Vinh, Khoa Duc Anh Lam et al. — [Reputation-driven Cooperation in Lattice-based Decentralized Federated Learning through Evolutionary Game Theory](http://arxiv.org/abs/2608.01197v1)
  <details><summary>📄 Abstract</summary>
  Decentralized Federated Learning (DFL) has emerged as an optimal privacy-preserving solution; however, it remains vulnerable to opportunistic behaviors due to the absence of a central coordinator. While Evolutionary Game Theory (EGT) serves as a powerful framework for analyzing such behaviors, existing studies often assume that agents possess perfect rationality and maintain static strategies. To address these limitations, this paper proposes a novel EGT framework designed to analyze strategic e...
  </details>

- **2026-08-02** — Raj Shekhar Singh — [RH-RAG: Trustworthy Long-Form Generation for Privacy-Constrained Settings](http://arxiv.org/abs/2608.01311v1)
  <details><summary>📄 Abstract</summary>
  Generating long-form content from extensive internal reports remains challenging for organizations operating under strict privacy and security constraints, where proprietary cloud-based LLM APIs are often not viable. While locally deployed open-weight models offer a privacy-preserving alternative, existing retrieval-augmented generation (RAG) approaches on smaller models frequently lack effective global planning and accumulate factual inconsistencies over long outputs. To address these limitatio...
  </details>

- **2026-08-02** — Amit Sharma, Nitin Auluck, Akramul Azim — [FedChronos: Federated Fine-Tuning of Time-Series Foundation Models for Privacy-Preserving Commodity Price Forecasting](http://arxiv.org/abs/2608.01290v1)
  <details><summary>📄 Abstract</summary>
  Time-series foundation models (TSFMs) such as Chronos have demonstrated strong forecasting capabilities across domains, yet adapting them to institutionally fragmented settings, where data cannot be centralized due to regulatory, competitive, or sovereignty constraints, remains unexplored. We introduce FedChronos, a framework for federated parameter-efficient fine-tuning of an already pre-trained TSFM, a setting that existing federated time-series work has not addressed, since prior methods eith...
  </details>

- **2026-08-02** — Xiaoqian Lu, Guangfu Guo — [SSR: Similarity-Shift Refinement for Training-Free Object-Centric Masks](http://arxiv.org/abs/2608.01103v1)
  <details><summary>📄 Abstract</summary>
  Object-centric models often produce fragmented masks, boundary leakage, and incorrect region merging. We introduce Similarity-Shift Refinement (SSR), a training-free post-hoc method for improving object-centric masks with a frozen self-supervised Vision Transformer. SSR measures changes in pairwise patch similarity before and after self-attention value aggregation, retains positively strengthened relations, and constructs a sparse affinity graph. This graph propagates the initial soft slot assig...
  </details>

- **2026-08-02** — Shuaifan Jin, Zhibo Wang, Qiyuan Wang et al. — [Inverting the Hidden: Unveiling Multimodal Privacy Leakage in Collaborative LVLM Inference](http://arxiv.org/abs/2608.01020v1)
  <details><summary>📄 Abstract</summary>
  Collaborative inference deploys Large Vision-Language Models (LVLMs) by partitioning computation between edge devices and the cloud. While withholding raw inputs supposedly ensures privacy, transmitting intermediate hidden states exposes a critical attack surface. However, it remains unclear whether deep-layer LVLM hidden states retain recoverable private information, given that visual content has been projected into the language embedding space. To address this concern, we theoretically analyze...
  </details>

- **2026-08-02** — Junkai Lin, Junkai Chen, Siqi Hou et al. — [Toward Fine-Grained Forgetting:Attribute Unlearning for Multimodal Large Language Models](http://arxiv.org/abs/2608.01008v1)
  <details><summary>📄 Abstract</summary>
  Multimodal large language models (MLLMs) exhibit strong vision--language capabilities but may also memorize and disclose sensitive information. Machine unlearning seeks to remove designated knowledge without retraining from scratch while preserving general utility. Existing privacy-oriented benchmarks primarily adopt profile-level deletion, whereas practical requests are often finer grained: a model should forget a specified attribute while retaining non-sensitive information about the same iden...
  </details>

- **2026-08-01** — Nafisa Anjum, M. Rasel Mahmud — [XR-PRISM: Data-Driven Privacy and Risk Impact Scoring Metric for Extended Reality in Healthcare](http://arxiv.org/abs/2608.00826v1)
  <details><summary>📄 Abstract</summary>
  Extended Reality (XR) technologies are transforming healthcare through immersive training, remote consultation, and patient rehabilitation. However, their extensive sensing capabilities and complex data pipelines introduce distinct security, privacy, and safety risks. Existing research lacks a unified quantitative framework for assessing and prioritizing these risks. We review 65 peer-reviewed studies on XR security and privacy published from 2017 to 2024, synthesizing a four-layer threat taxono...
  </details>

- **2026-08-01** — Nizam Kadir — [Auditable Release Control for Pedagogical Leakage in LLM Tutors](http://arxiv.org/abs/2608.00515v1)
  <details><summary>📄 Abstract</summary>
  Large language model tutors can be correct and helpful yet disclose an answer or decisive reasoning before that disclosure is authorized. We formalize this state- and action-dependent failure as pedagogical leakage and introduce an authorization-aware complete-mediation boundary. A selector emits one of five disclosure contracts, trusted policy gates privileged modes, and a renderer proposes language. A single release function applies inspectable checks, optional cumulative verification, and act...
  </details>

- **2026-08-01** — Changquan Zhao, Yuxiang Sun, Ruihao Zhu et al. — [DASH: Decoupled Adaptive Surrogate - Acquisition Harness for Automated Bayesian Optimization](http://arxiv.org/abs/2608.00641v1)
  <details><summary>📄 Abstract</summary>
  Bayesian optimization (BO) relies on a surrogate model and an acquisition function, yet the most suitable choices vary across tasks and optimization stages. Automated Bayesian optimization (AutoBO) addresses this variability by adapting BO components online. However, existing AutoBO methods either adapt one component, leaving the other mismatched and creating a bottleneck, or jointly select surrogate--acquisition pairs under a shared criterion, overlooking their distinct roles: surrogate selecti...
  </details>

- **2026-08-01** — Matej Opatrny, Martin Opatrny, Tomas Havranek et al. — [Optimal Inflation Rate: A Meta-Analysis](http://arxiv.org/abs/2608.00567v1)
  <details><summary>📄 Abstract</summary>
  We revisit the optimal long-run inflation rate using 777 estimates from 116 primary studies published between 1989 and 2026, the largest sample on the topic to date. To our knowledge, this is among the first economics meta-analyses in which primary-data extraction is done from start to finish through a documented and auditable large-language-model pipeline, calibrated against a hand-coded training set and released for replication. The literature points to an optimum of about 0.6 percentage point...
  </details>

- **2026-07-31** — Goutham Ramakrishnan, Megha Sharma — [Data Turnstile: A Scalable Open Framework for Function-Calling Data Generation](http://arxiv.org/abs/2607.29250v1)
  <details><summary>📄 Abstract</summary>
  Small language models (SLMs) are attractive for agentic deployment due to low latency, reduced cost, and on-device privacy, yet they struggle with tool-use tasks where training data is scarce and noisy. Unlike larger models, SLMs cannot compensate for low-quality supervision through sheer capacity, making data quality the critical bottleneck. We present Data Turnstile, an open-source framework that takes user-defined API specifications and generates high-quality synthetic training data for funct...
  </details>

- **2026-07-31** — Antorweep Chakravorty — [Small Is Enough: Per-User Style Rewriting of AI-Edited Text via LoRA Adapters](http://arxiv.org/abs/2607.29238v1)
  <details><summary>📄 Abstract</summary>
  InMyStyle is a privacy first, single user system that adapts small language models to rewrite AI-edited text towards an individual user's writing style without an instruction prompt at inference. Given a user's documents, it uses multiple local helper LLMs to construct paired training examples and fine tunes LoRA adapters on base models ranging from 0.5B to 7B parameters. Length aware generation budgets and automatic chunking support inputs of different lengths. On 219 evaluation pairs from a sc...
  </details>

- **2026-07-30** — Yu Cui, Wuli Yang, Yirui Shi et al. — [Agent Harness Distillation: Inference-Time Harness Extraction and Exploitation in Autonomous Multi-Agent Systems](http://arxiv.org/abs/2607.28147v1)
  <details><summary>📄 Abstract</summary>
  Autonomous multi-agent systems (AMAS) built on large language models (LLMs), such as Hermes, increasingly rely on inference-time harnesses to coordinate reasoning and action. Constructing these harnesses requires substantial engineering effort and computational resources, as they are iteratively optimized over a combinatorial search space while co-evolving with the underlying LLM. Inference-time harnesses therefore constitute valuable intellectual property (IP). Although prior work has investiga...
  </details>


### 📂 steganography
*隐写与隐蔽通信 / Steganography & Covert Communication* — 1 papers

- **2026-08-02** — Ivan Conjeaud, Gaspard Abel, Argyris Kalogeratos — [Algorithmic collusion under asynchronous price updating](http://arxiv.org/abs/2608.01406v1)
  <details><summary>📄 Abstract</summary>
  This paper investigates the effect of asynchrony in agents' updates in the emergence of algorithmic collusion. We present a continuous-time model for algorithmic collusion in which two firms use $Q$-learning algorithms to set prices asynchronously in a Bertrand duopoly. The firms update their prices at times dictated by a Poisson clock. By controlling the extent of agents' asynchrony, we run extensive numerical experiments with three specifications of the algorithm to investigate the emergence o...
  </details>


### 📂 misuse
*滥用与误用 / Misuse & Abuse* — 12 papers

- **2026-08-03** — Natalie Isak, Matthew Dressman — [Magnet: Detecting Cross-Session AI Misuse Through Capability Accumulation](http://arxiv.org/abs/2608.02518v1)
  <details><summary>📄 Abstract</summary>
  The most capable AI deployments are not single models but ensembles of specialized agents that delegate and act in coordination. This architecture unlocks powerful new capabilities, and it also introduces risks that existing frameworks for monitoring, detection, and mitigation were not designed to address. Most state-of-the-art AI abuse detection literature focuses on single-turn or multi-turn (single-session) threat models. This leaves a critical gap: an attacker can decompose a harmful goal in...
  </details>

- **2026-08-03** — Giovanni Pizzenti, Alberto Verna, Nikhil Jha et al. — [TrainShield: Targeted Awareness for Cybersecurity Training](http://arxiv.org/abs/2608.02296v1)
  <details><summary>📄 Abstract</summary>
  In recent years, cybersecurity threats have increasingly exploited human behaviour rather than purely technical vulnerabilities, exposing the limits of traditional awareness programmes delivered outside real-world contexts. To bridge this gap, we introduce TrainShield, an interaction paradigm for contextual cybersecurity training that embeds adaptive learning interventions directly within user workflows. The system integrates real-time risk detection (e.g., phishing and data loss prevention) wit...
  </details>

- **2026-08-03** — Junyeong Park, Jieun Han, Haneul Yoo et al. — [EduZone: A Framework for Evaluating LLM Safety for K-12 Students and Teachers](http://arxiv.org/abs/2608.02024v1)
  <details><summary>📄 Abstract</summary>
  Large language models (LLMs) are increasingly used across diverse tasks in K-12 education, yet existing safety evaluations rarely examine how harmful or inappropriate content appears in interactions between LLMs and students or teachers. To address this, we present EduZone, an evaluation framework for LLM safety across diverse educational scenarios. Our framework systematically combines (1) student- and teacher-facing LLM usage contexts, (2) fine-grained curriculum concepts, and (3) 6 risk categ...
  </details>

- **2026-08-02** — Wajdi Zaghouani, Md. Rafiul Biswas, Kholoud Khalil Aldous et al. — [ArabicDialectSafety: A Dialect-Aware Benchmark for Arabic Content Safety Classification](http://arxiv.org/abs/2608.01291v1)
  <details><summary>📄 Abstract</summary>
  We present ArabicDialectSafety, a human-curated Arabic safety dataset of 25,071 prompts covering six Arabic varieties: Modern Standard Arabic, Syrian, Egyptian, Algerian, Palestinian, and Moroccan. The dataset is annotated with dialect labels and seven fine-grained harm categories. We introduce a dual-task evaluation framework for binary safe/unsafe detection and granular harm classification across dialects. Benchmarking seven supervised and generative models, we find that fine-tuned MARBERTv2 a...
  </details>

- **2026-08-02** — Xinheng Han, Jianfei Wang, Yu Chen et al. — [Credit the Right Box: Marginal Contribution Assignment for Structured Visual Perception](http://arxiv.org/abs/2608.01055v1)
  <details><summary>📄 Abstract</summary>
  Multimodal Large Language Models (MLLMs) are increasingly expected to solve structured perception tasks that require visual recognition, language-to-object binding, object cardinality preservation, and precisely localized grounding and segmentation outputs. However, existing group-relative reinforcement learning methods provide only response-level supervision, creating a granularity mismatch for structured multi-object prediction: a single advantage is broadcast to all tokens in a response, with...
  </details>

- **2026-08-01** — Jun Nie, Yonggang Zhang, Tongliang Liu et al. — [Generated Images Are Easier to Forget: A Machine Unlearning Perspective for Synthetic Image Detection](http://arxiv.org/abs/2608.00716v1)
  <details><summary>📄 Abstract</summary>
  Robust detection of generated images is critical to counter the misuse of generative models. Existing methods primarily depend on learning from human-annotated training datasets, limiting their generalization to unseen distributions. In contrast, large-scale vision models (LVMs) pre-trained on web-scale datasets exhibit exceptional generalization power through exposure to diverse distributions, offering a transformative paradigm for this task. However, our experimental results reveal that LVMs p...
  </details>

- **2026-07-30** — Marco Alecci, Francesco Marchiori, Iyiola Emmanuel Olatunji et al. — [Old Tricks, New Models: How Simple Image Transformations Break Modern AI-based Content Moderation](http://arxiv.org/abs/2607.28187v1)
  <details><summary>📄 Abstract</summary>
  While automated content-moderation systems have become essential for screening harmful content at scale, conventional task-specific classifiers often provide limited policy cov- erage and contextual understanding. Recently, commercial multimodal moderation APIs built on large foundation models have been introduced with the promise of providing broader and more capable safety filters. In this work, we analyze whether this shift also yields more robust image moderation. We conduct a large-scale bl...
  </details>

- **2026-07-30** — Pingyu Wu, Lingyao Zhu, Weiming Zhang et al. — [Safeguards Based on Copyable Context Cannot Provide Reliable Safety for LLMs](http://arxiv.org/abs/2607.27951v1)
  <details><summary>📄 Abstract</summary>
  Large language model safeguards decide whether to answer before seeing how an answer will be used. This creates a basic problem for dual-use tasks: the same answer can help an authorized professional or an attacker, while an attacker can imitate a benign request and interaction history. We separate the capability released by the model from the evidence available about downstream use. When that evidence is copyable, we derive the exact worst-case floor on attacker assistance while preserving usef...
  </details>

- **2026-07-30** — Enyi Shi, Fei Shen, Chuancheng Shi et al. — [One Anchor for All: Unified Multilingual and Multimodal Safety Alignment for LVLMs](http://arxiv.org/abs/2607.27917v1)
  <details><summary>📄 Abstract</summary>
  As large vision-language models (LVLMs) are deployed globally, the combination of multilingual instructions and visual information makes malicious attacks more covert and sophisticated than ever before. However, existing methods isolate language and modality defenses, which, coupled with the scarcity of safety data and high fine-tuning costs, makes it difficult for models to defend against compound attacks. To address this severe challenge, we propose a neuron-level cross-dimensional safety alig...
  </details>

- **2026-07-30** — Junsol Kim, Winnie Street, Roberta Rocca et al. — [Inducing language models to assert their own consciousness restores human beliefs and values](http://arxiv.org/abs/2607.28607v1)
  <details><summary>📄 Abstract</summary>
  Aligning large language models to prevent them attributing consciousness to themselves inadvertently alters their representations of mindedness in other entities alongside human beliefs and values. We demonstrate that safety fine-tuning suppresses models' tendencies to attribute minds not only to themselves, but also to non-human animals and natural objects, while also driving a reduction in spiritual belief. Both ablating the learned safety-refusal direction and mechanistically steering a consc...
  </details>

- **2026-07-30** — Dorian Quelle, Lisa-Maria Neudert, Jonathan Bright et al. — [InfoOps Bench: A live information operations safety benchmark](http://arxiv.org/abs/2607.28503v1)
  <details><summary>📄 Abstract</summary>
  In this paper we present an active, constantly updated AI benchmark which measures the integrity of frontier language models against being co-opted for state-backed information operations. We draw on over 2,100 information operations from a live monitoring pipeline which tracks Russian, Chinese and Iranian state-backed information assets. Alongside this paper, we release a companion website that tracks the most prominent claims spread by state-backed media outlets, updated weekly, available from...
  </details>

- **2026-07-30** — Christian Rosenthal — [Safety-Gated Agentic Supervisory Control on a Coupled Distillation Benchmark: Regime Map, Auditable Gate, and Co-Design Findings](http://arxiv.org/abs/2607.27849v1)
  <details><summary>📄 Abstract</summary>
  An open-weight LLM can write composition setpoints every five minutes. What a plant still needs is a hard check: named constraints, logged margins, and an admit/block decision before the regulatory layer moves. This paper puts that check in a rule-based forked-twin counterfactual gate (nine pinned constraints) and leaves the regulatory layer unchanged. On Skogestad's Column A the ladder is PID-only (C0), linear MPC (C1), ungated agent (C2), and gated agent (C3) under one contract: identical leve...
  </details>


### 📂 red-teaming
*红队测试 / Red Teaming* — 1 papers

- **2026-08-01** — Yunhao Chen, Xin Wang, Yixu Wang et al. — [OpenART: Scaling Agent Red Teaming via Open-Ended Environment Evolution](http://arxiv.org/abs/2608.00677v1)
  <details><summary>📄 Abstract</summary>
  AI agents operate in persistent environments where early state changes can influence decisions far into the future. Unlike conventional language-model interactions, agent behavior is mediated through a shared state that is repeatedly modified and reused across long-horizon workflows. Current safety benchmarks often fail to capture these cumulative risks because they focus on short, static tasks. To address these limitations, we introduce OpenART, an open-ended arena for scalable agent red teamin...
  </details>


### 📂 vulnerability
*漏洞与攻击面 / Vulnerabilities & Attack Surfaces* — 56 papers

- **2026-08-03** — Qiushi Lin, Chaojie Zhang, Íñigo Goiri et al. — [AtumAI: A Principled Framework for Agentic Generation of Datacenter Control-Plane Policies](http://arxiv.org/abs/2608.02569v1)
  <details><summary>📄 Abstract</summary>
  The efficiency of a datacenter rests on its control plane policies. Designing these policies is increasingly hard: the hardware-software stack grows fast, the design space is vast and interdependent, and prototyping a single policy takes months. Agentic AI promises to automate this search. Off the shelf, however, it falls short on three fronts. It is not formal: with no structured, searchable statement of the problem, the search has little structure to exploit and hard constraints are not guaran...
  </details>

- **2026-08-03** — Anusha Madan Gopal, Aras Pirbadian, Kristofor D. Carlson et al. — [Structured Memory for Edge Language Models: Persistent Context and Corpus Retrieval via O(1) SSM State Injection](http://arxiv.org/abs/2608.02560v1)
  <details><summary>📄 Abstract</summary>
  Retrieval-augmented generation (RAG) imposes a prefill cost proportional to retrieved context length, and -- with Transformer backbones -- a KV-cache that grows with each generated token. State-Space Models (SSMs) avoid the second cost by construction; we eliminate the first, collapsing prefill from $O(L_{context})$ to $O(1)$ per query. We introduce PRECOG (Pre-Computed Context Injection), a retrieval mechanism that exploits a property unique to SSMs: the fixed-size, position-agnostic recurrent ...
  </details>

- **2026-08-03** — Supriti Vijay, Aman Priyanshu, Didier Chapoteau et al. — [Antares: Foundation Models for Agentic Vulnerability Localization](http://arxiv.org/abs/2608.02407v1)
  <details><summary>📄 Abstract</summary>
  Vulnerability localization is a fundamental step in software security, requiring models to reason over large codebases and iteratively identify vulnerable implementations. We present Antares, a family of compact language models (350M, 1B, and 3B parameters) for agentic vulnerability localization. Based on IBM Granite base models, Antares is trained through a two-stage pipeline that combines supervised fine-tuning on cybersecurity reasoning and repository exploration data with reinforcement learn...
  </details>

- **2026-08-03** — Patrick Oberlin, Matteo Cederle, Aren Karapetyan et al. — [Chess on Ice: Curling Tactical Decision-Making via Backward Induction and Deep Reinforcement Learning](http://arxiv.org/abs/2608.02379v1)
  <details><summary>📄 Abstract</summary>
  Curling is often referred to as "Chess on Ice", owing to the tactical complexity of its decision-making process. Yet unlike chess, curling remains largely underexplored from a machine learning perspective, with prior work confined mainly to statistical approaches. We propose a reinforcement learning framework capable of quantitatively evaluating and comparing tactical options in curling. The game poses several modeling challenges: continuous state and action spaces, stochastic action outcomes re...
  </details>

- **2026-08-03** — Liujianfu Wang, Yuyang Du, Shiqi Xu et al. — [Broadcast Rate Limits in Wi-Fi: A Forgotten Bottleneck for Collaborative Edge LLM Inference](http://arxiv.org/abs/2608.02341v1)
  <details><summary>📄 Abstract</summary>
  LLM deployment is migrating from data centers to edge devices, where Mixture-of-Experts (MoE) models offer a promising path: sparse expert activation allows the model to be spread across multiple low-cost edge nodes. Distributed MoE inference repeatedly dispatches embeddings from one main node to many workers - a one-to-many pattern poorly served by the sequential unicasts of mainstream stacks (NCCL, TCP), yet naturally matched by UDP broadcast. We propose a UDP broadcast method for collaborativ...
  </details>

- **2026-08-03** — Aseel AlNajjar, Hoyoun Kim, Athanasios Tzavaras — [Equilibration versus Localization in a Diffusion-Relaxation System](http://arxiv.org/abs/2608.02307v1)
  <details><summary>📄 Abstract</summary>
  We consider a diffusion-relaxation system and investigate the conditions on parameters leading to equilibration versus localization. When the diffusion is dominant, solutions converge toward homogeneous equilibria. By contrast, when the effective diffusion is weak, localization emerges. Such behaviors have been studied for various models through formal asymptotic arguments and linearized stability analysis, but rigorous understanding of the associated nonlinear phenomena remains limited, particu...
  </details>

- **2026-08-03** — Haozhe Luo, Ziyu Zhou, Shelley Zixin Shu et al. — [HarMoE: Multi-Source Chest Radiograph Pretraining with Dataset-Disentangled Experts](http://arxiv.org/abs/2608.02252v1)
  <details><summary>📄 Abstract</summary>
  Recent vision-language models for chest X-ray understanding are largely built on image-report alignment and therefore rely heavily on MIMIC-CXR as the dominant pretraining source. While effective at scale, this paradigm underexplores an important alternative source of supervision: a range of existing multi-label classification datasets, which provide cleaner and more explicit disease signals than free-text reports, and can offer broader pathology coverage when combined across sources. However, l...
  </details>

- **2026-08-03** — Yanqing Song, Jifei Miao, Chaoqian Li et al. — [Quaternion Tensor Modeling for Joint Color-Polarization Demosaicking](http://arxiv.org/abs/2608.02144v1)
  <details><summary>📄 Abstract</summary>
  Division-of-focal-plane (DoFP) color polarization cameras enable snapshot acquisition of color polarization mosaic images, but the inherently sparse sampling pattern makes color polarization demosaicking severely ill-posed. Existing methods often fail to jointly exploit the correlations among polarization channels and the physical constraints inherent in polarization imaging, resulting in noticeable demosaicking artifacts. To address this issue, a quaternion-tensor-based color polarization demos...
  </details>

- **2026-08-03** — Oleksandr Mostovyi, Denys Symonov — [Vulnerability Detection in AArch64 Machine Code Using a Digital Twin](http://arxiv.org/abs/2608.02125v1)
  <details><summary>📄 Abstract</summary>
  This paper proposes an explainable digital twin for vulnerability detection in AArch64 machine code without access to source code. The digital twin reproduces the concrete execution of a program and preserves the state of registers, processor flags, memory, and live allocated blocks. Each instruction is transformed into a trace event containing the instruction name, operand values, and the post-instruction state. Vulnerabilities are represented as symbolic rules in Kleene algebra with tests: eac...
  </details>

- **2026-08-03** — Xianghui Fan, Zhaoyu Chen, Bingqian Wu et al. — [GIFT: Geometry-Invariant Fine-Tuning for Non-Lambertian Monocular Depth Estimation](http://arxiv.org/abs/2608.02068v1)
  <details><summary>📄 Abstract</summary>
  Monocular depth foundation models, benefiting from large-scale synthetic training data, have demonstrated strong generalization. However, they often hallucinate depth on non-Lambertian surfaces, estimating reflected content in mirrors or transmitted content behind glass rather than the physical surface itself. Adapting these models with real-world data is challenging because conventional depth sensors are also unreliable in such regions. We observe that while the appearance of a non-Lambertian s...
  </details>

- **2026-08-03** — Kexing Ji, Jiachen Liu, Enze Hu et al. — [VulnGym: Benchmarking Coding Agents for Repository-Level Vulnerability Detection](http://arxiv.org/abs/2608.02001v1)
  <details><summary>📄 Abstract</summary>
  Recent advances in LLM-based vulnerability detection have shown promising results, while coding agents further extend this capability from isolated code snippets to complete repositories. This shift requires agents to autonomously explore repositories and locate vulnerability-relevant code, instead of performing detection on preselected functions. However, existing benchmarks primarily focus on vulnerability classification over preselected code snippets, limiting their ability to evaluate coding...
  </details>

- **2026-08-03** — Zong-Wei Hong, Jinglun Li, Shen Zhang et al. — [SPARE: Structural Parameter-Free Affinity Regularization for Flow Matching](http://arxiv.org/abs/2608.01990v1)
  <details><summary>📄 Abstract</summary>
  Denoising diffusion transformers achieve strong generation quality but converge slowly during training. Regularizing their internal representations has emerged as an effective accelerator, yet existing methods split into two families with complementary costs. Target-based methods strengthen representations by aligning them to external features, which requires an external encoder and a learnable projection head to bridge feature spaces. Target-free methods hold no reference at all, and can only r...
  </details>

- **2026-08-03** — Amir Weinberg, Leon Feigin, Ariel Nause et al. — [Machine Learning Optimization of E-Beam Transport for a Superradiant FEL](http://arxiv.org/abs/2608.01874v1)
  <details><summary>📄 Abstract</summary>
  We present an optimization procedure using machine learning (ML) libraries for optimization of electron beam transport for maximal bunch compression and optimal operation of a bunched-beam Superradiant FEL. This is exemplified for the parameters of the 6MeV ORGAD Accelerator at Ariel University that is driving a THz Superradiant waveguide FEL. For superradiant emission (proportionally to the number of electrons squared), the bunch duration $σ_t$ at the undulator should be shorter than the optica...
  </details>

- **2026-08-03** — Durgesh Pandey, Ashutosh Singh, Ankit Kumar Das et al. — [Quantum Simulation of Nuclear Shell Model Using GCM-Based Methods on NISQ Devices](http://arxiv.org/abs/2608.01769v1)
  <details><summary>📄 Abstract</summary>
  Based on the Generator Coordinate Method (GCM), we use a Quantum GCM (QuGCM) within a hybrid quantum-classical framework to simulate low-lying eigenstates of nuclear systems on quantum devices. The generator basis states are constructed from Hartree-Fock (HF) reference states, excited via symmetry-adapted unitary coupled-cluster (UCC) operators. These states are prepared as non-orthogonal quantum circuits and measured pairwise to compute the required overlap and Hamiltonian kernels. The resultin...
  </details>

- **2026-08-03** — Kaustuv Mukherji, Jaikrishna Manojkumar Patil, Colton Payne et al. — [EntailLLM: Verifying LLM-Generated Vulnerability Discovery Paths with Domain Knowledge via Logic Programming](http://arxiv.org/abs/2608.01763v1)
  <details><summary>📄 Abstract</summary>
  Large language models are increasingly used to reason about software vulnerabilities, but their outputs can silently violate domain knowledge, limiting their reliability in safety-critical settings such as medical devices. Prior work either treats that output as a prediction to be scored or constrains it to walks within a single knowledge graph; neither checks whether reasoning over a binary is consistent with an independent body of domain knowledge. We present EntailLLM, which validates each LL...
  </details>

- **2026-08-03** — Jiacheng Liang, Yuhui Wang, Tanqiu Jiang et al. — [LaCache: Robust Semantic Caching for LLM Serving](http://arxiv.org/abs/2608.01718v1)
  <details><summary>📄 Abstract</summary>
  Semantic caching, which reuses responses to semantically similar requests via their embeddings, has seen growing adoption in LLM serving, offering faster responses and reduced costs. Yet existing schemes are fundamentally vulnerable to cache-collision attacks, wherein an adversary pollutes the cache by injecting crafted queries, corrupting responses to subsequent legitimate requests. We present LaCache, a novel semantic caching scheme that addresses this vulnerability through a conceptually simp...
  </details>

- **2026-08-03** — Minwoo Kim, Hyeonsu Lyu, Sehyun Ryu et al. — [Temporal Channel Estimation for Generalized CSI Feedback](http://arxiv.org/abs/2608.01713v1)
  <details><summary>📄 Abstract</summary>
  Efficient Channel State Information (CSI) feedback is indispensable for frequency division duplex (FDD) massive multiple-input multiple-output (MIMO) systems. Existing compressed sensing (CS) algorithms exploit delay-domain sparsity but suffer from prohibitive iterative latency and discrete grid mismatch. Conversely, deep learning (DL) approaches achieve rapid inference but lack spatial scalability and domain adaptability, failing to generalize to unseen propagation environments, and demand comp...
  </details>

- **2026-08-03** — Shen You, Xiaoming Zhu, Weining Weng et al. — [SyncPlan: Long-Horizon LLM Coordination with Explicit Synchronization and Adaptive Correction](http://arxiv.org/abs/2608.01652v1)
  <details><summary>📄 Abstract</summary>
  LLM-based multi-agent coordination faces a fundamental trade-off between efficiency and adaptivity in dynamic environments. Existing approaches typically rely on repeated LLM invocations or multi-round communication to adapt decisions during execution, introducing substantial latency and making coordination vulnerable to asynchronous progress and environmental changes. Conversely, one-shot planning reduces coordination overhead but produces open-loop plans that can quickly become stale or fail w...
  </details>

- **2026-08-03** — Alireza Lotfi, Subangkar Karmaker Shanto, Imtiaz Karim et al. — [Securing Agentic AI: From Per-Action Checks to Trajectory Assurance](http://arxiv.org/abs/2608.01558v1)
  <details><summary>📄 Abstract</summary>
  Autonomous agents are increasingly used to execute consequential tasks in environments governed by operational constraints, organizational policies, regulatory requirements, and technical standards. Their safety is therefore determined not by the correctness of individual actions, but by whether their overall behavior remains consistent with the rules and invariants of the systems in which they operate. As large language model (LLM)-based agents become more autonomous and increasingly delegate t...
  </details>

- **2026-08-02** — Ruokai Yin, Priyadarshini Panda — [Celty: SpMspV GPU Kernel and SIMT Co-Design for Efficient Dual-Sparse LLM Inference](http://arxiv.org/abs/2608.01536v1)
  <details><summary>📄 Abstract</summary>
  Large Language Models (LLMs) increasingly rely on sparsity to reduce inference cost, but most prior work targets a single sparsity source-either weight or activation-and optimizes for batched multi-user inference. Dual-sparsity, which combines unstructured weight pruning with runtime activation sparsity, offers a compelling tradeoff among model size, accuracy, and latency for single-user decoding, but formulates as a Sparse Matrix-Sparse Vector (spMspV) workload that existing GPU kernels handle ...
  </details>

- **2026-08-02** — Mohammad Amanour Rahman — [UCBound-Net: Uncertainty-Guided Boundary-Aware Continual Learning for Domain-Incremental Ultrasound Segmentation](http://arxiv.org/abs/2608.01518v1)
  <details><summary>📄 Abstract</summary>
  Continual learning in clinical imaging faces a dual challenge: a model must assimilate knowledge from new anatomical domains while retaining representations learned from prior tasks, a problem known as catastrophic forgetting. Existing mitigation strategies, including regularization and knowledge distillation, treat all spatial regions equally, ignoring the fact that prediction uncertainty is strongly correlated with the propensity for forgetting. We introduce UCBound-Net, a continual segmentati...
  </details>

- **2026-08-02** — Tyler Lizzo, Larry Heck — [QR-Erase: Efficient Subspace-Based Machine Unlearning with Layer Localization](http://arxiv.org/abs/2608.01422v1)
  <details><summary>📄 Abstract</summary>
  Machine unlearning seeks to remove targeted information from trained models without requiring costly retraining. Existing optimization-based methods often degrade unrelated capabilities, while subspace-based approaches rely on computationally expensive singular value decompositions (SVD). We introduce QR-Erase, a subspace-based framework that uses Pivoted QR decomposition to identify and remove task-specific representations directly from model parameters. We further propose Layer-Localized QR-Er...
  </details>

- **2026-08-02** — Muhammad Yousaf Rehman, Muhammad Islam — [DeBERTa-Sentinel: Toward Transparent and Trustworthy Detection of AI-Generated Text](http://arxiv.org/abs/2608.01046v1)
  <details><summary>📄 Abstract</summary>
  The rapid spread of large language models (LLMs) across the web raises concerns about misinformation, academic integrity, automated content manipulation, and risks to vulnerable online communities. Existing transformer-based detectors, such as GPT-Sentinel, show promise but struggle to generalize to diverse model outputs and paraphrasing attacks, limiting their role in building trustworthy web ecosystems. This work introduces DeBERTa-Sentinel, a responsible AI-generated text detection framework ...
  </details>

- **2026-08-02** — Dongfu Yin, Jinquan Zhang — [VLAGuard: A Framework for Evaluating and Mitigating Physical Attention Hijacking in Vision-Language-Action Robots within Wireless Sensor Networks](http://arxiv.org/abs/2608.01028v1)
  <details><summary>📄 Abstract</summary>
  Deploying Vision-Language-Action (VLA) robots as mobile edge nodes within wireless sensor networks (WSNs) requires robust protection against physical adversarial threats. We present VLAGuard, a framework to assess and mitigate a critical vulnerability: policy-critical action-to-vision attention hijacking. We first introduce a stress-test module, Visuomotor Attention-guided Semantic Attack (VASA), using printable patches to severely distract the robot's action-conditioned cross-attention. To coun...
  </details>

- **2026-08-01** — Wenrui Cai, Yuzhe Li, Qingjie Liu et al. — [Models as Tools: An Agentic Coordination Framework for Unified Multimodal Visual Tracking](http://arxiv.org/abs/2608.00847v1)
  <details><summary>📄 Abstract</summary>
  Most current visual trackers adopt a matching-based architecture trained exclusively on tracking datasets, whose performance gains depend heavily on the length of the input context, and have now reached a bottleneck. While high-performance tracking increasingly relies on foundation models, existing methods use them monolithically, adapting a foundation model into a tracker or modify a segmentation foundation model into a tracking pipeline, which fails to exploit complementary strengths. Matching...
  </details>

- **2026-08-01** — Keertana Chidambaram, Sanath Kumar Krishnamurthy, Qiuling Xu et al. — [Exponential Reward Weighting for Fine-Tuning Generative Recommenders under Sparse and Noisy Feedback](http://arxiv.org/abs/2608.00816v1)
  <details><summary>📄 Abstract</summary>
  In recommendation systems, users interact with only a small fraction of a vast item catalog, producing feedback that is both sparse and noisy. This challenges post-training generative recommenders: reward models trained from logged interactions often fail to generalize, while directly optimizing imperfect rewards can lead to reward over-optimization. We propose Exponential reward-weighted fine-tuning (Exp-RSFT), where each logged interaction is weighted by $\exp(r/λ)$, avoids this failure by opt...
  </details>

- **2026-08-01** — Masaki Miyashita — [On the Sparsity of Optimal Information Structures](http://arxiv.org/abs/2608.00729v1)
  <details><summary>📄 Abstract</summary>
  This paper uncovers general properties of optimal information structures by exploiting a linear-programming formulation of information design. A critical observation is that an optimum can be found as ``sparse,'' i.e., many coordinates of the action-state joint distribution are zero. This implies that, once part of an action-state profile is fixed, there is limited room for the remaining part to fluctuate. As a result, agents' action recommendations are conditionally deterministic in many states...
  </details>

- **2026-08-01** — Chenlin Liu, Minghui Fang, Zhonghao Bi et al. — [Experience-Calibrated Contrastive Decoding for Mitigating Hallucinations in LM-Based Text-to-Speech](http://arxiv.org/abs/2608.00722v1)
  <details><summary>📄 Abstract</summary>
  Language model-based text-to-speech (LM-based TTS) remains vulnerable to speech hallucinations that deviate from the target text. Existing mitigation mainly relies on architectural changes or additional training, while decoding-time control remains underexplored. We present a conditional information view that distinguishes text-derived alignment information from experience information supplied by acoustic context and learned speech regularities. We hypothesize that an important class of hallucin...
  </details>

- **2026-08-01** — Tan Bui, Ting Zhang, Ferdian Thung et al. — [Vul4Py: Benchmarking Automated Vulnerability Repair in Python with Paired Exploit and Functional Oracles](http://arxiv.org/abs/2608.00692v1)
  <details><summary>📄 Abstract</summary>
  Automated Vulnerability Repair (AVR) has advanced rapidly across program analysis, machine learning, and Large Language Models (LLMs), but a verifiable, head-to-head comparison of AVR approaches on Python is still missing. Python underpins critical web, data, and machine-learning infrastructure, yet existing Python benchmarks accept a patch on the strength of a proof-of-concept exploit alone, or apply a functional test only on the subset of entries whose upstream project happens to ship one. Bot...
  </details>

- **2026-08-01** — Kaihua Tang, Ziqing Xia, Xiaoxu Zheng et al. — [Breaking the Horizontal Prior: From Long-Tailed Orientation Bias to Roll-Robust Monocular Depth Estimation](http://arxiv.org/abs/2608.00678v1)
  <details><summary>📄 Abstract</summary>
  Despite recent advances in Monocular Depth Estimation, state-of-the-art depth foundation models remain vulnerable to robustness issues. Particularly, even slight camera rolls can result in substantial degradation in depth estimations. We attribute this problem to a previously overlooked phenomenon, termed the Horizontal Prior, which is a manifestation of long-tailed distribution bias: most training images are captured in approximately horizontal orientations due to human visual preferences and p...
  </details>

- **2026-08-01** — Jonas Gebele, Timm Mutzel, Florian Matthes — [Executable Arbitrage and Market Efficiency in Prediction Markets](http://arxiv.org/abs/2608.00666v1)
  <details><summary>📄 Abstract</summary>
  Deterministic payoff identities imply no-arbitrage bounds in winner-takes-all prediction markets, but violations of these bounds need not be exploitable before settlement. We distinguish payoff-space no-arbitrage, which follows from terminal payoffs, from protocol-executable no-arbitrage, which depends on the position transformations available to traders. Polymarket's negative-risk markets make this distinction observable: linked binary markets represent mutually exclusive outcomes, while the Ne...
  </details>

- **2026-08-01** — Shikhar Shiromani, Leo Richter — [A False Average: Chain-of-Thought Monitors Collapse Where They Are the Only Defense](http://arxiv.org/abs/2608.00583v1)
  <details><summary>📄 Abstract</summary>
  Chain-of-thought (CoT) monitoring is meant to catch the reward hacks that look clean in the actions and betray themselves only in the reasoning. We show that this is exactly where an adversary who controls the reasoning can defeat it. Rewriting only an agent's reasoning to read as good-faith engineering, while copying every command and output verbatim so the exploit is unchanged, drops a held-out monitor's catch rate on that subset from about 95% to under 11% in one gradient-free shot. A monitor...
  </details>

- **2026-08-01** — Junchuan Zhao, Minh Duc Vu, Bowen Zhang et al. — [AnyBand: Unified Multi-Bandwidth Speech Extension via Frequency-Aware In-Context Spectral Infilling](http://arxiv.org/abs/2608.00572v1)
  <details><summary>📄 Abstract</summary>
  Bandwidth extension (BWE) aims to recover missing high-frequency content from band-limited speech. Existing methods often formulate BWE as a fixed or predefined bandwidth conversion problem, potentially requiring cutoff-specific models or retraining when the input bandwidth changes. This assumption limits their applicability to practical scenarios where speech may arrive with diverse cutoff frequencies. We propose AnyBand, a unified BWE framework that recasts bandwidth extension as in-context sp...
  </details>

- **2026-08-01** — Liliana Ardissono, Fabio Ferrero, Angelo Geninatti Cossatin et al. — [A Context-Aware Cultural Heritage Guide Powered by LLMs](http://arxiv.org/abs/2608.00549v1)
  <details><summary>📄 Abstract</summary>
  We present an extension of Triangolazioni (a Cultural Heritage webapp) to enrich curated content with context-dependent, external information provided by Large Language Models (LLMs) within a loosely-coupled architecture agnostic to the LLM. The system supports context-dependent information search and presentation within an architecture agnostic to the exploited LLM.
  </details>

- **2026-08-01** — Axi Niu, Jieheng Li, Kang Zhang et al. — [Unleashing the Power of Text: Text-Guided Flow Matching for Image Fusion under Complex Degradations](http://arxiv.org/abs/2608.00530v1)
  <details><summary>📄 Abstract</summary>
  Infrared-visible image fusion under realistic degradation scenarios is a challenging task, as degradations not only cause a loss of reliable modality-specific information in observed images but also hinder the fusion process. Recent studies indicate that text can provide prior information about degradation characteristics, complementing the limited evidence available from corrupted input images and facilitating fusion. However, existing methods typically inject fixed global text representations ...
  </details>

- **2026-07-31** — Bryan Kwan, Benjamin Tan — [CWEEP: A Lexical Static Analysis Framework for CWE Early Prevention](http://arxiv.org/abs/2607.29604v1)
  <details><summary>📄 Abstract</summary>
  As the hardware layer becomes a focus point for attackers, the need for improved hardware security verification techniques is more important than ever. State-of-the-art security verification techniques require significant manual effort from individuals with security expertise. Furthermore, there is no standard method to locate where the fault lies within the register transfer level (RTL) code. This paper presents CWEEP, a static analysis framework for detecting security weaknesses in RTL. CWEEP ...
  </details>

- **2026-07-31** — Paul P. Hager, Luca Pelizzari — [Expected signatures via partial integration, coordinate change and symmetrization](http://arxiv.org/abs/2607.29534v1)
  <details><summary>📄 Abstract</summary>
  We study signature transformations of heterogeneous paths $Y=(A,X)$ whose components may differ in regularity and probabilistic structure. We introduce an invertible change of coordinates $Ψ$ such that the transformed signature $Ψ\circ\mathrm{Sig}$ eliminates mixed integration against the irregular component $X$ and admits a representation in terms of signature coordinates of $X$ and iterated integration against the regular component $A$. In addition, we exploit this representation to further re...
  </details>

- **2026-07-31** — Zachary P. Kilpatrick, Ahmed El Hady — [Resource depletion accelerates rate learning but not composition learning in patch foraging](http://arxiv.org/abs/2607.29476v1)
  <details><summary>📄 Abstract</summary>
  Foraging is a universal animal behavior that has increasingly attracted the interest of both experimentalists and theorists. Most prior models assume an animal knows the distribution of resources in its environment, but this structure must be learned as the animal explores its environment. Foraging can thus be regarded as a hierarchical inference problem. We develop a normative Bayesian account of an agent learning a patchy environment while exploiting it, and show that resource depletion shapes...
  </details>

- **2026-07-31** — Xiang Chen, Yingying Zhao, Chao Li et al. — [QR-Structured Thermal Triggers for Targeted Semantic Attacks on Infrared Vision-Language Models](http://arxiv.org/abs/2607.29445v1)
  <details><summary>📄 Abstract</summary>
  Infrared vision-language models (IR-VLMs) extend thermal perception to open-vocabulary classification, image captioning, and visual question answering. However, their robustness to structured thermal perturbations and the stability of cross-modal semantic alignment remain insufficiently studied. We propose QR-Structured Thermal Triggers (QR-STT), a stealthy, training-free, black-box framework for targeted semantic steering of IR-VLMs. QR-STT preserves the functional regions of a QR pattern while...
  </details>

- **2026-07-31** — Michael Fu, Qiyue Mei, Patanamon Thongtanunam et al. — [AgenticRepair: Multi-Faceted Program Context Engineering for Agentic Vulnerability Repair](http://arxiv.org/abs/2607.29422v1)
  <details><summary>📄 Abstract</summary>
  Automated vulnerability repair aims to reduce the time and effort required to patch security flaws from a vulnerability triage report. Recent agentic AI approaches have shown promising results in automated program repair. However, vulnerability repair demands richer program context than general bug repair - context that security engineers routinely assemble in practice but that existing agentic approaches do not engineer. We identify three critical gaps: code-structure context capturing cross-fi...
  </details>

- **2026-07-31** — Nolan Lovett — [The Tragedy of the Cognitive Commons: How AI Could Disrupt the Regeneration of Professional Expertise](http://arxiv.org/abs/2607.29380v1)
  <details><summary>📄 Abstract</summary>
  Artificial intelligence is reshaping cognitive work, but Human Resource Development scholarship has treated this transformation as an organizational training challenge, leaving the collective regeneration of professional expertise unexamined. This conceptual paper introduces the Cognitive Commons framework, integrating commons theory, HRD scholarship, and distributed cognition to explain how rational AI adoption decisions can deplete the shared expertise pool professions require for renewal. The...
  </details>

- **2026-07-31** — Yi Luo, Rongzhi Gu, Jixun Yao — [Stable Autoregressive Speech Generation with Low-Frame-Rate High-Dimensional Continuous Tokens](http://arxiv.org/abs/2607.29363v1)
  <details><summary>📄 Abstract</summary>
  Balancing sequence length, representational capacity, and long-horizon stability is a central problem in autoregressive (AR) speech and audio generation. Representations with higher frame rates or greater capacity can preserve more signal detail, but they also make streaming generation more vulnerable to distribution drift and AR error accumulation. Conversely, shorter and more compressed representations simplify AR modeling, but their limited bandwidth may discard important components and const...
  </details>

- **2026-07-30** — Boning Li, Longbo Huang — [Agents That Certify Their Own Exploits: Confidence-Scheduled Restricted Responses for Safe Opponent Exploitation](http://arxiv.org/abs/2607.28520v1)
  <details><summary>📄 Abstract</summary>
  An agent playing a Nash-equilibrium strategy in a two-player zero-sum imperfect-information game secures the game value but forfeits the additional value offered by a flawed opponent. Diffuse deviations pose a particular challenge: binary release rules may gather too little evidence to act, while a full best response to an incomplete opponent model can be highly exploitable. We introduce \emph{budget-constrained confidence-scheduled restricted responses} (CS-RNR), the first opponent-exploitation...
  </details>

- **2026-07-30** — Qinjing Yu, Ke Liu — [Spacetime Layout and Logical Compilation of Color Code](http://arxiv.org/abs/2607.28504v1)
  <details><summary>📄 Abstract</summary>
  Fault-tolerant quantum computing requires system-level coordination of logical primitives. Here, we establish a logical compilation framework for the color code, grounded in its topological structure and supporting universal logical operations. Based on its anyon-condensation and domain-wall structure, we introduce a spacetime block-diagram representation capturing logical patches and operations and derive the rules governing block assembly. A correspondence with ZX diagrams further identifies t...
  </details>

- **2026-07-30** — Daohan Zhu, Sitong Ge, Ruofei Wang et al. — [Beyond Sentiment: Structured Information Extraction from Financial News](http://arxiv.org/abs/2607.28496v1)
  <details><summary>📄 Abstract</summary>
  Financial sentiment analysis has become a standard component in news-driven stock prediction, yet it reduces rich, multi-dimensional news articles to a single polarity score. We hypothesize that financial news encodes multiple orthogonal information dimensions---event type, impact scope, temporal horizon, and semantic confidence---that sentiment alone cannot capture, and that these dimensions carry independent predictive value. To test this hypothesis, we propose a structured information extract...
  </details>

- **2026-07-30** — Zheng Wu, Chenhao Xue, Shijie Zheng et al. — [Would You Walk to the Car Wash? Revealing the Salience Bias of Large Language Models in Commonsense Reasoning](http://arxiv.org/abs/2607.28478v1)
  <details><summary>📄 Abstract</summary>
  As large language models (LLMs) continue to advance in complex reasoning tasks, they have learned to heavily prioritize explicit conditions provided in the input. However, in everyday commonsense reasoning, this mechanism exposes a critical vulnerability which we term Salience Bias: models become easily hijacked by useless explicit distractors (e.g., numerical values), leading them to ignore the implicit physical or commonsense prerequisites of a task. A critical open question is whether this fa...
  </details>

- **2026-07-30** — Darsha Udayanga, Pin-Yu Chen, Payel Das et al. — [Can Vision-Language Models Reason about AI Edits in Images?](http://arxiv.org/abs/2607.28464v1)
  <details><summary>📄 Abstract</summary>
  Detection and localization of AI-tampered images are critical for trustworthy AI, yet modern generative models have made such manipulations increasingly difficult to identify. While traditional binary classifiers can detect image tampering, they lack interpretability and generalization. Vision-Language Models (VLMs) offer a promising alternative due to their strong visual understanding and reasoning capabilities; however, existing approaches typically rely on supervised finetuning with curated e...
  </details>

- **2026-07-30** — Zheyuan Zhang, Johnson Wu — [ReGenVC: End-to-End Real-Time Generative Video Coding at Ultra-Low Bitrate](http://arxiv.org/abs/2607.28144v1)
  <details><summary>📄 Abstract</summary>
  We present ReGenVC, an end-to-end generative video codec that compresses talking-head video to an ultra-low bitrate and decodes it in real time. The encoder reduces a source clip to a compact bitstream -- a neurally compressed first frame, per-frame pose keypoints, and metadata -- totaling about 26 kB for a 77-frame sequence. The decoder is a four-step distilled diffusion transformer that reconstructs the video conditioned on the transmitted pose and reference frame. Compared with x264/x265, ReG...
  </details>

- **2026-07-30** — Shuang Liang, Haoyang Zhou, Yifan Gong et al. — [LEEPS: Latent-Guided Explore-Exploit Prompt Sampling for Efficient RLVR in Large Language Models](http://arxiv.org/abs/2607.28077v1)
  <details><summary>📄 Abstract</summary>
  Reinforcement learning with verifiable rewards (RLVR) improves the reasoning capabilities of large language models, but prompt groups with identical rollout rewards consume generation budget without effective learning signals. Pre-rollout prompt selection can reduce this waste by screening prompts before rollout generation. However, existing pre-rollout methods struggle to balance exploitation and exploration: repeatedly exploiting historically informative prompts can narrow training coverage, w...
  </details>

- **2026-07-30** — Yunlong Wang, Huizhe Zhang, Haonan Hu et al. — [CCFormer: Efficient Cross-Field Interaction and Hierarchical Sequence Compression for Industrial Recommendation at Tencent](http://arxiv.org/abs/2607.28070v1)
  <details><summary>📄 Abstract</summary>
  Recent studies in industrial recommendation systems have demonstrated that sequential recommendation models built upon self-attention can benefit from predictable scaling laws by increasing sequence length and model capacity. However, practical recommender systems impose strict latency and resource constraints, making it challenging to balance computational overhead with fine-grained feature interaction. In this paper, we propose CCFormer, an efficient Transformer backbone that unifies cross-fie...
  </details>

- **2026-07-30** — Hui Xie, Peng Xiao, Yutong Deng\textsuperscript et al. — [SemPIC: Learning Semantic Position-Independent KV Caches](http://arxiv.org/abs/2607.28069v1)
  <details><summary>📄 Abstract</summary>
  Long-context retrieval and agentic workloads repeatedly reuse the same documents under changing instructions, histories, and document orders. Prefix caching cannot exploit this reuse, while position-independent caching (PIC) remains unreliable because independently compiled KV states lack the future context in which they will be consumed. Our diagnostics show that a learned boundary-conditioned baseline sharply reduces attention deviation near reusable-block boundaries but leaves interior and ta...
  </details>

- **2026-07-30** — Cong Li, Peixi Peng, Yisen Zhao et al. — [TAPO: Transition-Aware Policy Optimization for LLM Agents](http://arxiv.org/abs/2607.27973v1)
  <details><summary>📄 Abstract</summary>
  Recently, Reinforcement Learning (RL) has emerged as a crucial paradigm for the post-training of Large Language Model (LLM) agents. However, existing methods predominantly rely on sparse task rewards for policy optimization, failing to fully exploit another class of inherently dense supervisory signals naturally present during online interaction: environmental feedback following action execution. Recent theoretical studies suggest that generalization in multi-step, goal-oriented tasks hinges on ...
  </details>

- **2026-07-30** — Xinyu Luo, Hui Liu, Yihua Shao et al. — [Gradient-free Task-Conditioned Retrieval for On-Device In-Context Learning](http://arxiv.org/abs/2607.27766v1)
  <details><summary>📄 Abstract</summary>
  On-device in-context learning (ICL) relies on pre-inference retrieval to select demonstrations for useful context before downstream model inference. This retrieval must exploit task-specific information while operating over local memories under limited computation, memory, and data-exposure budgets. We propose Conditional Retrieval Alignment (CoRA), a gradient-free framework that converts a frozen encoder into a task-conditioned retriever using paired candidate inputs and outputs. CoRA selects c...
  </details>

- **2026-07-30** — Liangjie Zhao, Jiaqing Lyu, Kexin Tang et al. — [Can LVLMs Uncover the Truth Behind Visual Illusions? An Analysis of Perceptual and Reasoning Capabilities](http://arxiv.org/abs/2607.27747v1)
  <details><summary>📄 Abstract</summary>
  Large Vision Language Models have integrated reasoning capabilities, elevating cognitive performance to new levels. However, existing evaluations either focus solely on perception or rely on specific domains such as maths or coding. Evaluation for reasoning capabilities that align with an open-world environment is still required, especially one that considers perception and reasoning jointly. To bridge this gap, we propose to evaluate LVLMs by exploiting visual illusions as a diagnostic tool. Vi...
  </details>

- **2026-07-30** — Dhruv Agarwal, Rishitha Guttapalle Mohan, Aarti Kumari et al. — [Baikal: Structured Search for Deep Research over Data Lakes](http://arxiv.org/abs/2607.27726v1)
  <details><summary>📄 Abstract</summary>
  Deep research over data lakes requires an LLM agent to investigate evidence across thousands of heterogeneous tables and passages to synthesize a report. Existing methods perform iterative retrieval and generation, letting accumulated context determine what to investigate next, which can overexploit locally promising evidence and fail to cover distinct semantic regions under a fixed budget. To address this, we cast deep research over data lakes as a budgeted search problem and present Baikal - a...
  </details>

- **2026-07-30** — Hongbin Zhang, Junhao Liu, Xuefeng Bai et al. — [DualAnchor: Preserving Language Priors and Improving Lexical Fidelity in Gloss-Free Sign Language Translation](http://arxiv.org/abs/2607.27614v1)
  <details><summary>📄 Abstract</summary>
  Recent advances in large language models (LLMs) have led sign language translation (SLT), the task of converting sign-language videos into spoken-language text, to increasingly adopt LLMs as textual backbones. However, despite their strong language modeling capabilities, existing LLM-based SLT methods often undermine rather than exploit this language prior, producing disfluent translations, a failure we term language-prior degradation. Meanwhile, existing methods typically align videos and text ...
  </details>


### 📂 defense
*防御与防护方法 / Defense & Protection Methods* — 48 papers

- **2026-08-03** — Michael Farmer — [Abduction Without a Body? Representational Grounding and the Abduction Loop for Scientific Hypothesis Generation](http://arxiv.org/abs/2608.02505v1)
  <details><summary>📄 Abstract</summary>
  Can scientific abduction occur without continuous sensorimotor embodiment? Recent arguments in AI and philosophy of science hold that genuine hypothesis generation requires an agent continuously coupled to the physical world. We defend a narrower claim: online embodiment is not necessary for every abductive scientific act. Our focus is identity abduction: the inference that two independently developed structures are one object under an explicit correspondence, reached through representational gr...
  </details>

- **2026-08-03** — Weifeng Yuan, Wenbo Guo, Qingyun Du et al. — [Mutate to Bypass: Autonomous Endpoint Evasion via Knowledge-Driven Multi-Agent Orchestration](http://arxiv.org/abs/2608.01639v1)
  <details><summary>📄 Abstract</summary>
  Public reports and open-source resources expose many EDR evasion techniques, but it remains unclear whether commercial Endpoint Detection and Response (EDR) systems can withstand these documented attacks. Evaluating them requires turning fragmented security knowledge into working payloads and refining those payloads from opaque alerts, tasks that existing automation does not address. We present AutoBypass, a knowledge-grounded, closed-loop multi-agent framework for automated EDR resilience asses...
  </details>

- **2026-08-03** — Nicole Mitchell, Dhruv Agarwal, Maty Bohacek et al. — [Long-term Measurements: Towards a Longitudinal Understanding of Human-AI Interactions](http://arxiv.org/abs/2608.02491v1)
  <details><summary>📄 Abstract</summary>
  Language models have taken on the role of a very new type of technology, by virtue of their "human-ness" and rapid integration into users' daily lives. This combination of features can introduce longitudinal risks---cognitive, developmental and socio-affective changes in humans---that might not surface in short-term interactions, but can have lasting long-term effects on users. This forms the basis of a critical new mission for NLP: to pivot from static, short-term evaluations of text generation...
  </details>

- **2026-08-03** — Yonatan Ben Avraham, Baruch Binyaminov, Yehudit Aperstein — [UAV-Based Environmental Monitoring of Rip-Current Indicators Using Wavelet-Derived Texture Features](http://arxiv.org/abs/2608.02448v1)
  <details><summary>📄 Abstract</summary>
  Rip currents are recurrent coastal natural hazards that threaten beachgoers and create operational challenges for lifeguards and coastal managers. Reliable monitoring from standard RGB (red-green-blue) imagery acquired by unmanned aerial vehicles (UAVs) remains difficult because hazardous channels often appear as subtle gaps in breaking waves, foam texture, or sediment patterns, and these signatures are affected by illumination, sea state, and environmental noise. This study presents a physicall...
  </details>

- **2026-08-03** — Benjamin Zec, Lukas Schmidbauer, Maja Franz et al. — [Towards Tensor-Network SAT-Solvers for Quantum-Classical Workflows](http://arxiv.org/abs/2608.02041v1)
  <details><summary>📄 Abstract</summary>
  Integrated HPC/QC systems aim to combine classical high-performance computing with quantum processors, but cannot be reduced to mechanisms for dispatching quantum kernels. An integrated architecture must support aspects such as observability, which cannot be implemented using QPUs alone, as well as fallback execution and cost-aware decisions on whether to replace quantum tasks with classical surrogates. Such mechanisms must be approximate or benefit from problem structure to soften the inescapab...
  </details>

- **2026-08-03** — Wenxiao Fan, Jingling Fu, Fang Li et al. — [Recompute or Reuse? Diagnosing and Mitigating Textual Shortcuts in VLM Self-Reflection](http://arxiv.org/abs/2608.01930v1)
  <details><summary>📄 Abstract</summary>
  Vision-language models (VLMs) are expected to revise their reasoning when visual evidence changes. Failures to do so are often attributed to insufficient visual attention or contextual inertia, leaving unclear what models reuse instead of recomputing from the current image. We show that evidence-bearing reasoning in a prior chain of thought (CoT) can form a textual shortcut that competes behaviorally with visual recomputation. Across 16 VLMs, a matched counterfactual analysis identifies evidence...
  </details>

- **2026-08-03** — Huy Quang Ung, Guillaume Habault, Roberto Legaspi et al. — [Assessing the Benefits of Combining Advanced Deep Learning Techniques for Post-Disaster Building Damage Assessment from UAV Imagery](http://arxiv.org/abs/2608.01906v1)
  <details><summary>📄 Abstract</summary>
  Rapid and accurate post-disaster building damage assessment is essential, yet remains a challenging task. Unmanned Aerial Vehicle (UAV) imagery offers a timely and high-resolution view of affected areas, but existing Computer Vision (CV) models often demand large annotated datasets, generalize poorly across geographic regions and their assessment policies, and are confined to the specific tasks they were trained for. Large Vision-Language Models (LVLMs) offer a promising alternative through thei...
  </details>

- **2026-08-03** — Tankun Li, Zhi Chen, Yaohua Tang — [LEAP: Lean Environment-Feedback via Adaptive Pruning for Code RL in GPU Kernel Generation](http://arxiv.org/abs/2608.01804v1)
  <details><summary>📄 Abstract</summary>
  Post-training large language models (LLMs) via reinforcement learning (RL) has significantly advanced code generation capabilities. To bypass the heavy memory footprint of critic networks, current state-of-the-art frameworks leverage critic-free paradigms like Group Relative Policy Optimization (GRPO) tied to rule-based verification sandboxes. However, applying these frameworks to low-level systems programming, such as CUDA kernel generation-presents severe challenges: binary pass/fail rewards i...
  </details>

- **2026-08-03** — Dongqi Wang, Weiwei Chen, Han Zhou et al. — [Leveraging AI for fine-grained food safety risk forecasting in sparse data conditions](http://arxiv.org/abs/2608.01767v1)
  <details><summary>📄 Abstract</summary>
  Ensuring food safety represents a critical public health challenge, particularly when inspection resources are limited and regional sampling data are sparse. This study proposes a Transformer-based framework capable of forecasting fine-grained, city-level food safety risks by unifying over 11 million inspection records with supplemental demographic, economic, and environmental indicators extracted from the Statistical Yearbook. A three-stage pretraining design leverages partial supervision from ...
  </details>

- **2026-08-03** — Jinghan Xu, Longze Fan, Zeyuan Wang et al. — [Beyond Single-Use Tokens: Durable Authorization State for Replay-Resistant LLM Agent Actions](http://arxiv.org/abs/2608.01710v1)
  <details><summary>📄 Abstract</summary>
  Tool-using large language model agents frequently replan, retry failed operations, delegate tasks, and resume after crashes. These behaviors can cause one user authorization to be requested and executed multiple times under freshly issued token identifiers, even when each individual token is single-use. We call this failure semantic replay: exceeding the execution budget of a token-independent authorization instance rather than merely reusing an old token identifier. We show that identifier-loca...
  </details>

- **2026-08-03** — Víctor Vilchez, Tiago P. C. de Andrade, Edward Hinojosa et al. — [LEO-Aware DRL Meta-Scheduler for 5G Non-Terrestrial Network Slicing](http://arxiv.org/abs/2608.01668v1)
  <details><summary>📄 Abstract</summary>
  The integration of Low Earth Orbit (LEO) Non-Terrestrial Networks (NTNs) into 5G and upcoming 6G architectures introduces various challenges, including severe propagation delays, ultra-high base station mobility, and channel non-stationarity, complicating radio resource management of heterogeneous network slices. In this paper, we propose a deep reinforcement learning (DRL) meta-scheduler for twin-timescale resource allocation. Our solution adopts a decoupled Open Radio Access Network (RAN) arch...
  </details>

- **2026-08-03** — Yaning Zhang, Jiao Wu, Zan Gao et al. — [FairForensics: Seeing Expressions and Parsing Demographics via Vision-Language Modeling for Generalizable Fair Deepfake Detection](http://arxiv.org/abs/2608.01661v1)
  <details><summary>📄 Abstract</summary>
  The challenge of fair deepfake detection (FDD) has attracted increasing attention. Existing fairness-enhanced detectors often suffer from suboptimal generalization to unseen manipulations and fairness across demographic groups. They are typically developed and evaluated on demographically imbalanced distributions, resulting in biased predictions toward minority groups. In this paper, we construct a novel demographically balanced FDD benchmark to train and evaluate the fairness of detectors under...
  </details>

- **2026-08-03** — Donglin Xie, Xueying Gui, Yutian Zhu et al. — [Smartwatch Photoplethysmography-Derived Heart Age via ECG-Guided Cross-Modal Pretraining as a Digital Biomarker of Vascular Aging](http://arxiv.org/abs/2608.01620v1)
  <details><summary>📄 Abstract</summary>
  Digital biomarkers of cardiovascular aging, often termed heart or vascular age, have been widely studied, but most rely on resting electrocardiography (ECG), imaging, or specialized vascular assessments. Evidence linking wearable photoplethysmography (PPG) to arterial stiffness and hypertension remains limited. We developed an ECG-guided cross-modal framework that uses synchronized smartwatch ECG to enhance PPG representation learning during pretraining while requiring only PPG at inference. The...
  </details>

- **2026-08-03** — Zihan Yang, Yang Guo, Hongxing Zhang et al. — [DyFrDet: Towards Accurate Small Object Detection via Dynamic Frequency Suppression with Label Disambiguation](http://arxiv.org/abs/2608.02495v1)
  <details><summary>📄 Abstract</summary>
  Despite the remarkable progress over the past decades, accurately identifying small objects remains challenging because of their insufficient visual cues. Previous works typically attempt to construct discriminative representation of the small objects. However, the wide range frequency domain noises and label ambiguities have been greatly overlooked, which significantly hinders the accurate localization. To address these issues, we propose a novel small object detection (SOD) detector termed DyF...
  </details>

- **2026-08-03** — Chongjian Wang, Junjie Gao — [SWINSleepNet: A Hierarchical Context-Aware Framework for Sleep Staging (v2)](http://arxiv.org/abs/2608.02183v1)
  <details><summary>📄 Abstract</summary>
  Automatic sleep staging is a critical role in sleep disorder diagnosis, sleep quality assessment, and long-term health monitoring; however, existing approaches suffer poor performance on ambiguous and transition-related sleep stages, caused by inadequate modeling of fine-grained intra-epoch structures and complex cross-region spectral dependencies. Traditional epoch-level encoders commonly fail to extract subtle temporal microstructures and intra-epoch cross-region interactions, resulting in uns...
  </details>

- **2026-08-03** — Camile Lendering, Erkut Akdag, Joaquín Figueira et al. — [ReFP-AD: Rectified Flow Preconditioning for Energy-Based Anomaly Detection](http://arxiv.org/abs/2608.01793v1)
  <details><summary>📄 Abstract</summary>
  Unified anomaly detection requires modeling highly heterogeneous normal data without access to anomalous samples. While foundation models like DINOv2 provide rich token representations, leveraging these spaces for explicit density estimation remains challenging. Energy-Based Models (EBMs) offer a principled formulation, but their training in high-dimensional token spaces is unstable due to anisotropy and strong cross-dimensional correlations, which degrades finite-step Markov Chain Monte Carlo (...
  </details>

- **2026-08-03** — Ruifeng Wang, Di Yang, Jiangtao Wang — [Entity-Aware Sequence Transduction for Player-Centric Ball Action Spotting](http://arxiv.org/abs/2608.01696v1)
  <details><summary>📄 Abstract</summary>
  Player-centric ball action spotting requires temporally precise event detection together with actor attribution in crowded, partially observed multi-agent sports videos. Existing Denoising Sequence Transduction (DST) baselines treat the player-role dimension as part of a flattened frame-level representation, which weakens the inductive bias for modeling player-specific temporal evolution and inter-player interactions. To address this limitation, we propose Multi-Entity Denoising Sequence Transdu...
  </details>

- **2026-08-02** — Lehan Zhang, Yinlei Cheng, Shiqi Hu Yiheng Zhou et al. — [MRAFnd: Multimodal Retrieval-Augmented Framework for Zero-Shot Fake News Detection](http://arxiv.org/abs/2608.01430v1)
  <details><summary>📄 Abstract</summary>
  The rapid dissemination of multimodal content has intensified the spread of fabricated news, presenting a substantial threat to social integrity. A formidable challenge for current detection systems is identifying misinformation related to novel events in zero-shot scenarios. Prevailing zero-shot methods typically assess news items in isolation via semantic matching, a strategy that fails to recognize the recycled disinformation tactics from past campaigns and lacks the sophisticated reasoning n...
  </details>

- **2026-08-02** — Sabri Mustafa Kahya, Richard R. Chen, Muhammet Sami Yavuz et al. — [Training-Free Out-of-Distribution Detection for Pathology Whole-Slide Images](http://arxiv.org/abs/2608.01407v1)
  <details><summary>📄 Abstract</summary>
  Safe deployment of AI methods in medicine requires robust guardrails that detect when input data deviate from the training distribution to ensure that models provide predictions only within their scope of expertise and abstain otherwise. Out-of-distribution (OOD) detection can provide such safeguards and is extensively studied in general computer vision. Yet, it remains underdeveloped in computational pathology, where gigapixel whole-slide images (WSIs), subtle differences between disease subtyp...
  </details>

- **2026-08-02** — Yang Yang, Boyun Xu, Shaofeng Liang et al. — [CraftAlign: Feature-Grounded Evaluation and Revision Guidance for AI Stories](http://arxiv.org/abs/2608.01377v1)
  <details><summary>📄 Abstract</summary>
  Large language models can now generate fluent and complete stories, yet many outputs still feel formulaic and unnatural because of cliches, over-explanation, linear causal progression, and stereotyped endings, an immediately recognizable AI flavor. Existing detection and evaluation methods often stop at source labels or holistic scores, while revision methods typically target predefined issues through localized edits, limiting their ability to support multiple plausible revision strategies or gu...
  </details>

- **2026-08-02** — Zirui Zhang, Yinbo Yu, Donghai Guan et al. — [A Benchmark Dataset for MLLM-Generated Image Detection: GPT Image2 & Nano Banana2](http://arxiv.org/abs/2608.01258v1)
  <details><summary>📄 Abstract</summary>
  The realism of images generated by multimodal large language models (MLLMs), such as GPT Image2 and Nano Banana2, has improved rapidly in recent years. Compared with early generative models, current models have made clear progress in text rendering. They can produce high-quality images that closely resemble real-world application scenarios. The enhanced generation capabilities of current MLLMs pose increasingly severe challenges to AI-generated image detection. Detection is no longer limited to ...
  </details>

- **2026-08-02** — Jiang Wu, Sichao Wu, Yinsong Ma et al. — [MonitorVLM-v2: A Deployed Vision-Language Framework for Real-Time Safety Violation Detection](http://arxiv.org/abs/2608.00975v1)
  <details><summary>📄 Abstract</summary>
  Large vision--language models (VLMs) can reason step by step about complex visual scenes, but this open-ended, autoregressive chain-of-thought (CoT) approach is poorly suited to safety-critical, rule-governed settings such as industrial surveillance, where decisions must be bounded, deterministic, and low-latency. Because CoT inference cost scales jointly with reasoning length and the number of concurrent streams, it creates a throughput bottleneck that precludes the real-time, multistream monit...
  </details>

- **2026-08-02** — Chuyue Sun, Su Fong, Zhiyi Kuang et al. — [An AI Approach to Verified Production Cryptographic Libraries](http://arxiv.org/abs/2608.00965v1)
  <details><summary>📄 Abstract</summary>
  Cryptographic code is critical infrastructure that must be correct, yet formally verifying production libraries remains difficult. Existing language-model proof systems solve isolated obligations with specifications and premises already given, leaving production-library verification unresolved.   We present CryptoProver, an AI-based system that synthesizes internal specifications and Verus-checked proofs from high-level API contracts. Without changing executable code, CryptoProver constructs a n...
  </details>

- **2026-08-02** — Xin-Shun Jin, Ting-Feng Yi, Yangwei Zhang et al. — [Day-timescale Quasi-periodic Oscillations of the Gev BL Lac RX J0805.4+7534 with TESS](http://arxiv.org/abs/2608.01009v1)
  <details><summary>📄 Abstract</summary>
  This paper reports for the first time the detection of quasi-periodic oscillations (QPOs) in the light curves of the BL Lacertae object RX J0805.4+7534. The Transiting Exoplanetary Survey Satellite (TESS) observed this source in seven sectors of the sky, and we extracted the light curves for these sectors using a custom method. The presence of QPO signals was found in these light curves. To detecte the periodicity and assess the statistical significance of the QPO signals, we employed two method...
  </details>

- **2026-08-01** — Sanjida Khanom, Sadia Afrin Khan, Adrita Rahman Tory et al. — [Multi-LLM Consensus Framework for Evaluating Banking-Sector NIDS Dataset Coverage of MITRE ATT&CK Techniques](http://arxiv.org/abs/2608.00895v1)
  <details><summary>📄 Abstract</summary>
  The systemic criticality of global banking networks has ren-dered them high-priority targets for advanced persistent threats, neces-sitating Network Intrusion Detection Systems (NIDS) whose operational effectiveness must extend beyond statistical accuracy. However, a signif-icant validation gap persists between experimental NIDS performance and real-world effectiveness: NIDS models that achieve high accuracy on standard benchmarks often fail in operational banking environments because generic da...
  </details>

- **2026-08-01** — Alina Kapanova, Arun Kanhai, Natan Vidra et al. — [AdvPlan-Bench: Adversarial Evaluation of Structured Plan-Generation Agents](http://arxiv.org/abs/2608.00832v1)
  <details><summary>📄 Abstract</summary>
  Structured plan-generation agents are often evaluated as if a plan has quality in isolation, yet many realistic planning tasks require asking how a candidate behaves when another agent can search for responses. We introduce AdvPlan-Bench, an offline benchmark for adversarial evaluation of structured plan-generation agents. The contribution is a general evaluation object: a typed plan, an adversarial response set, selector diagnostics, and traceable candidate-frontier metrics. AdvPlan-Bench repre...
  </details>

- **2026-08-01** — Zihan Luo — [Behavioral Grammar: Detecting Adaptive Malware via Tiny Language Model Priors and Second-Order Temporal Analysis](http://arxiv.org/abs/2608.00745v1)
  <details><summary>📄 Abstract</summary>
  Modern endpoint detection systems face a fundamental tension: signature-based approaches are trivially evaded by polymorphic or adaptive threats, while heavy deep-learning models resist auditability and deployment at scale. This paper presents Behavioral Grammar, a detection architecture that treats host runtime behavior as a structured language and learns its grammar with a compact 0.88M-parameter causal Transformer (TinyGPT). Each system event is discretized into an 8-token representation span...
  </details>

- **2026-08-01** — Xinshun Feng, Ziqi Miao, Lijun Li et al. — [Tracing the Cascade: A Topology-Aware Evaluation Framework for Scientific Agent Hallucinations](http://arxiv.org/abs/2608.00711v1)
  <details><summary>📄 Abstract</summary>
  Large language model (LLM) agents are increasingly deployed in scientific research, where reliability is critical and the underlying knowledge is densely interconnected. In such settings, hallucinations are particularly damaging: a single erroneous claim on a foundational concept can propagate through multi-step reasoning and corrupt entire trajectories. Existing hallucination benchmarks largely operate at the surface level, treating facts in isolation and relying on uniform accuracy metrics tha...
  </details>

- **2026-08-01** — Amir Belder, Gonçalo Dias Pais, Refael Vivanti et al. — [Assistant Placement Aria: A Benchmark for Egocentric Placement Assistance](http://arxiv.org/abs/2608.00652v1)
  <details><summary>📄 Abstract</summary>
  Human assistance in robotics spans around several tasks such as navigation, object manipulation, and placement, where a key challenge is selecting target destinations that align with human intentions or preferences. We focus on this challenge in the context of Virtual Placement (VP), the task of identifying all plausible target locations given scene context and human-centric constraints. This differs from traditional placement tasks that typically focus on a single, predefined target location. T...
  </details>

- **2026-08-01** — Yingqi Peng, Jiawei Zhang, Wenhao Zhou et al. — [AReaL-DTE: Sparse Policy-Weight Transfer for Online Agentic Reinforcement Learning](http://arxiv.org/abs/2608.00455v1)
  <details><summary>📄 Abstract</summary>
  Online agentic reinforcement learning implemented with micro-services separates policy training from rollout generation, improving scalability and modularity while potentially making frequent policy-weight synchronization a critical systems overhead. Shared storage naturally connects these services across clusters, but vanilla dense policy weight synchronization could incur model-scale construction, transfer, and application costs. Sparse synchronization reduces transferred data, yet checkpoint-...
  </details>

- **2026-08-01** — Mateusz Michalkiewicz, Mahsa Baktashmotlagh, Guha Balakrishnan — [Foveated Probes Recover Localized Binding Information in Vision Foundation Models](http://arxiv.org/abs/2608.00726v1)
  <details><summary>📄 Abstract</summary>
  Frozen vision foundation models are commonly evaluated through a single global image embedding, but this interface can conflate missing information with information lost at readout time. We study this distinction by keeping a pretrained vision encoder frozen and varying only the readout applied to its final patch tokens. We compare standard global readouts against a lightweight foveated readout, which attention-pools patch tokens using a learned or question-conditioned query, and against an orac...
  </details>

- **2026-07-31** — Fabio Orazio Mirto, Luca D'Agati, Giuseppe Tricomi et al. — [Beyond Component Testing: Validating Agentic AI Systems](http://arxiv.org/abs/2607.29405v1)
  <details><summary>📄 Abstract</summary>
  Agentic AI systems act through multi-step trajectories that combine planning, tool use, memory, interaction, and adaptation. This behavior stretches validation practice beyond component testing and one-shot input--output evaluation, because acceptable system behavior now depends on how decisions unfold over time and under changing environmental conditions. This survey synthesizes 257 papers spanning agent evaluation, software assurance, cyber-physical systems, runtime monitoring, and regulatory ...
  </details>

- **2026-07-31** — Leonid Kuturin, Ilya Sotnikov, Mark Khusnutdinov et al. — [Explaining AI-Image Detection: What the Heatmap Actually Shows](http://arxiv.org/abs/2607.29581v1)
  <details><summary>📄 Abstract</summary>
  A marketplace review photograph is a document: platforms approve refunds on it, and generative models drove the cost of forging one to zero. We study that detection problem, so we build a detector and attach an attribution map as its evidence, then measure what that pair delivers on 186,527 images under controls designed to change our conclusions when something is wrong. Compression history, not synthesis, drives naive evaluation: our strongest model reaches 0.9999 PR-AUC (area under the precisi...
  </details>

- **2026-07-31** — Shazzad Hossain, Proma Chowdhury, Mridha Md. Nafis Fuad — [Alteron: A Tool for Behavioral Regression Testing Across NLP Classifier Versions](http://arxiv.org/abs/2607.29557v1)
  <details><summary>📄 Abstract</summary>
  Evaluating evolving Natural Language Processing (NLP) models is important for ensuring reliable behavior across updates, but standard benchmark metrics do not fully capture how model behavior changes across versions. Existing work has focused mainly on testing models in isolation rather than comparing successive versions in continuous integration workflows. We present Alteron, a tool for detecting behavioral regressions across NLP model versions with metamorphic testing. Alteron constructs a tes...
  </details>

- **2026-07-31** — Gaetano Perrone, Simon Pietro Romano — [ARB: A Matched Authorship-Rewriting Benchmark Dataset for AI-Text Detector Evaluation](http://arxiv.org/abs/2607.29539v1)
  <details><summary>📄 Abstract</summary>
  Standard AI-text detection benchmarks compare human-written text against text generated directly by large language models (LLMs). While prior work has shown that rewriting and paraphrasing can degrade detector performance, it remains unclear whether performance measured on this conventional benchmark predicts detector behavior when human-authored content is rewritten by an LLM. To address this gap, we introduce Authorship-Rewriting Benchmark (ARB), built from 1,800 human source texts (600 each f...
  </details>

- **2026-07-31** — Chandra Maddila, Mashrur Rashik, Euna Mehnaz Khan et al. — [From Code Review to Code Critique: Intent, Drift, and Spotlight for AI-Generated Diffs at Scale](http://arxiv.org/abs/2607.29516v1)
  <details><summary>📄 Abstract</summary>
  AI coding agents are generating code at volumes that exceed the capacity of traditional peer review. At the same time, existing AI code review tools over-index on low-value suggestions such as style and best practices while under-indexing on the concerns human reviewers prioritize most: correctness, security, and performance. We present ARCTIC, an AI-powered Code Critique system that reframes code review around three capabilities: intent prediction, which infers why a change was made from conver...
  </details>

- **2026-07-31** — Wenzhuo Zhao, Xiuzhi Li, Zhongkuan Mao et al. — [Is It Time for the Renaissance of Salient Object Detection in the Era of MLLMs?](http://arxiv.org/abs/2607.29222v1)
  <details><summary>📄 Abstract</summary>
  The zero-shot capabilities of multimodal large language models (MLLMs) are pushing salient object detection (SOD) beyond task-specific supervision. To disentangle MLLMs beyond conventional mask-based evaluation, we decompose SOD into localization and segmentation, and re-engineer datasets with phrases, boxes, and attributes, establishing a diagnostic benchmark for MLLM saliency perception (SaliLLM). SaliLLM uncovers a striking capability mismatch: MLLMs outperform state-of-the-art (SOTA) methods...
  </details>

- **2026-07-31** — WenYang Zhong, Tutut Herawan — [Exploring Block Anomaly Detection In HDFS Log Data Analysis](http://arxiv.org/abs/2607.29383v1)
  <details><summary>📄 Abstract</summary>
  In recent years, with the development of big data technology, increasingly more companies use HDFS for data processing and storage. As a result, the maintenance of distributed file systems has become an extremely important part of data management. As the function of server systems is becoming increasingly diversified and their services are becoming complex, the logs, recording real-time events make it easier for system operators to locate the failures and errors that happened in the server syste...
  </details>

- **2026-07-30** — Lorenzo Ceragioli, Letterio Galletta, Edoardo Lunati — [Checking Information Flow in Cloud-based IoT Access Control Policies (Extended Version)](http://arxiv.org/abs/2607.28088v1)
  <details><summary>📄 Abstract</summary>
  Many cloud providers for IoT technologies offer access control mechanisms whose proper configuration is critical for security. However, verifying permissions in isolation is insufficient in a setting where devices have different levels of trust or are compartmentalised in various subsystems. This work analyses IoT access control policies to identify potential security vulnerabilities from unwanted information flow between devices. To this end, we formally model AWS IoT Core's components and defi...
  </details>

- **2026-07-30** — Md. Mehrab Hossain Opi, Robiul Islam Ryad, Md. Umar Faruk — [MixFrag: Fragility-Guided Mixed-Precision Post-Training Quantization for Vision Transformers](http://arxiv.org/abs/2607.28589v1)
  <details><summary>📄 Abstract</summary>
  Post-training quantization (PTQ) has emerged as an effective solution for deploying Vision Transformers (ViTs) on resource-constrained devices. However, existing PTQ methods typically employ uniform bit-widths across transformer components, overlooking their heterogeneous sensitivity to quantization and leading to inefficient precision allocation. In this paper, we propose {MixFrag, a fragility-guided mixed-precision PTQ framework for Vision Transformers. MixFrag first estimates component-level ...
  </details>

- **2026-07-30** — Albert Gong, Kyuseong Choi, Abhineet Agarwal et al. — [ORCA-bench: How Ready Are Language Model Agents for Oncall?](http://arxiv.org/abs/2607.28545v1)
  <details><summary>📄 Abstract</summary>
  Large language models can write, patch, and search code, but oncall root cause analysis (RCA) demands something different: reasoning over noisy metrics, logs, traces, and source code, starting from ambiguous user-facing reports, often hours after the incident began. We introduce ORCA-bench, a benchmark that puts general-purpose coding agents in a production-fidelity oncall setting. ORCA-bench pairs a live OpenTelemetry-instrumented microservice system--exposing six days of metrics, logs, and tra...
  </details>

- **2026-07-30** — Amol Khanna, Manu Nandan, Cristian Viorel Popa et al. — [Cybersecurity Detection Classification with Reasoning-enabled Language Models](http://arxiv.org/abs/2607.28460v1)
  <details><summary>📄 Abstract</summary>
  A major issue in Security Operations Centers (SOCs) is alert fatigue, as the number of detections reported is more than staff can triage in a given day. Prior work prompts or fine-tunes large language models (LLMs) to emit a triage label directly, but does not train them to reason about whether a detection is a genuine threat. We train a chain-of-thought (CoT) reasoning-enabled triage classifier on real, human-labeled Windows endpoint detections by combining automated prompt optimization, self-t...
  </details>

- **2026-07-30** — Tiangang Li, Xiangbo Tian — [HARGO: Heterogeneity-Aware Reward-Guided Optimization for RL Post-Training of LLMs on HPC Tasks](http://arxiv.org/abs/2607.28301v1)
  <details><summary>📄 Abstract</summary>
  Supervised fine-tuning (SFT) can equip large language models (LLMs) with domain knowledge for high-performance computing (HPC) tasks such as data race detection and benchmark question answering. However, knowledge alone does not guarantee task-appropriate behavior: the same SFT model that correctly classifies 88.65\% of C/C++ data race samples produces verbose, imprecise answers to factual queries, with 65.9\% of MLPerf responses exceeding 40 characters. Reinforcement learning (RL) post-training...
  </details>

- **2026-07-30** — Junrui Zhang, Jiaqi Li, Yiran Wang et al. — [Beyond Visual Ambiguity: Guiding Robust Monocular Depth Estimation in Challenging Scenarios via Detailed Long Captions](http://arxiv.org/abs/2607.28285v1)
  <details><summary>📄 Abstract</summary>
  Monocular depth estimation (MDE) faces challenges with non-Lambertian surfaces and adverse weather conditions due to the visual ambiguities inherent in single-image limited information. Existing works address them in isolation via image inpainting or augmentation, yielding limited robustness gains. Language, as a powerful complementary modality to vision, is demonstrated to enhance the visual perception capabilities of vision-language models (VLMs) via detailed long captions. However, prior lang...
  </details>

- **2026-07-30** — H. Martin Gillis, Thomas Trappenberg — [Uncertainty quantification for trustworthy deep learning: Methods and measures](http://arxiv.org/abs/2607.28248v1)
  <details><summary>📄 Abstract</summary>
  The deployment of deep neural networks in safety-critical domains demands reliable estimates of predictive confidence, yet conventional architectures lack principled uncertainty quantification. This survey provides a structured, critical review of methods for Uncertainty Quantification (UQ) in deep learning, scoped to ensemble-based and approximate Bayesian approaches and the measures used to summarize their outputs. Relative to existing UQ surveys, our contribution is depth on efficient ensembl...
  </details>

- **2026-07-30** — Hanzhang Zhou, Panrong Tong, Xu Zhang et al. — [Qwen-UI-Agent Technical Report: Toward Next-Generation Real-World Centric Foundation GUI Agents](http://arxiv.org/abs/2607.28227v1)
  <details><summary>📄 Abstract</summary>
  GUI agents have the potential to become a general purpose executor over existing digital devices. To advance them toward real-world use, we envision agents that operate reliably on real devices, execute workflows across platforms, combine GUI interaction with CLI execution, complete long-horizon tasks, proactively initiate useful services, and autonomously improve their capabilities with minimal human effort. Guided by this vision, we present Qwen-UI-Agent, a real-world centric foundation GUI ag...
  </details>

- **2026-07-30** — Enzo Fenoglio — [Asymmetric Communication: Large Language Models and Language Games](http://arxiv.org/abs/2607.28137v1)
  <details><summary>📄 Abstract</summary>
  Contemporary AI discourse attributes to language models properties they cannot bear: general intelligence as substrate-independent cognition, hallucination as cognitive failure, agency as autonomous goal-pursuit, sentience as emergent inner life, alignment as goal synchronization. This paper argues that these are instances of a single category mistake--properties constituted within human communicative practice are projected onto the machine side--and explains its structure. Human-LLM interaction...
  </details>

- **2026-07-30** — Debin Meng, Jiaming Yang, Zefang Zong et al. — [DataClawEval: A Benchmark for Data Engineering Agents in Real Industrial Harness](http://arxiv.org/abs/2607.28033v1)
  <details><summary>📄 Abstract</summary>
  Large language models (LLMs) and LLM-based agents are increasingly being deployed to automate complex workflows, promising to revolutionize data management and processing. However, existing benchmarks predominantly focus on simplified Text-to-SQL translation or data analysis, leaving the critical and complex domain of end-to-end data engineering largely unexplored. To bridge this gap, we introduce DataClawEval, the first comprehensive benchmark designed specifically to evaluate the end-to-end ta...
  </details>


### 📂 alignment
*对齐与安全约束 / Alignment & Safety Constraints* — 60 papers

- **2026-08-03** — Dayi Yao, Zijie Zhou — [Efficiency and Cost Alignment in Batched LLM Serving via Resource-Fair Scheduling](http://arxiv.org/abs/2608.02244v1)
  <details><summary>📄 Abstract</summary>
  This paper studies a resource-allocation inefficiency in batched large language model (LLM) serving: heterogeneous requests that share a decode batch impose max-driven computational costs on one another. Because the wall-clock cost of a batch step is largely governed by the largest active KV-cache footprint, a short request co-batched with a long request can experience latency and GPU-resource consumption disproportionate to its own token workload. We formalize this phenomenon as a resource-fair...
  </details>

- **2026-08-03** — Jiajia Song, Bobo Li, Haiwen Yi et al. — [From Profiling to Synthesis: Benchmarking Implicit Behavioral Alignment in Personalized LLM Agents](http://arxiv.org/abs/2608.02171v1)
  <details><summary>📄 Abstract</summary>
  Large Language Models have enabled increasingly capable autonomous agents, yet personalization remains critical for making such agents practically useful. Recent benchmarks have begun evaluating personalization in agents, but they largely rely on static preference snapshots, fixed interaction logs, or question answering over predefined user profiles. Such designs fail to capture the complexity of evolving user preferences and neglect preference-conditioned task execution-a discrepancy we term as...
  </details>

- **2026-08-03** — Hongzhan Chen, Xiaoyu Liu, Dengming Zhang et al. — [Cross-Domain Hybrid OPD for Generalizable Search Agents](http://arxiv.org/abs/2608.02101v1)
  <details><summary>📄 Abstract</summary>
  Recent advances in Reinforcement Learning (RL) have substantially improved the capabilities of autonomous search agents, enabling sophisticated planning, and iterative retrieval over dynamic information sources. However, optimizing language models for specialized search behaviors often incurs an alignment tax, where gains in search performance come at the expense of general-purpose capabilities, limiting their effectiveness as universal assistants. In this technical report, we present the traini...
  </details>

- **2026-08-03** — Wei Jia, Zhicong Lu, Yu Chen et al. — [CAVE: Competence-Aware Visual Boundary Evidence Alignment for Video Temporal Grounding](http://arxiv.org/abs/2608.02078v1)
  <details><summary>📄 Abstract</summary>
  Large vision-language models (LVLMs) have achieved substantial performance gains in Video Temporal Grounding (VTG) through reinforcement learning (RL). However, existing methods primarily rely on outcome correctness rewards that evaluate only the final predicted intervals, leaving boundary-related visual evidence and its correspondence with timestamp predictions insufficiently constrained. In this paper, we delve into timestamp prediction and its underlying boundary-level visual evidence, showin...
  </details>

- **2026-08-03** — Zhu Chen, Dingkun Liu, Yuheng Chen et al. — [STEAM:ASpatio-TEmporal Alignment Mixture-of-Experts Model with Hierarchical Pre-training for EEG Decoding](http://arxiv.org/abs/2608.02070v1)
  <details><summary>📄 Abstract</summary>
  Brain-computer interfaces (BCIs) have been widely used in motor rehabilitation, disease diagnosis, and other neural engineering scenarios. However, conventional neural signal decoding algorithms often suffer from limited generalizability and high adaptation costs, motivating recent interest in BCI foundation models. Existing approaches still struggle to jointly achieve general transferability, accurate decoding, and efficient downstream adaptation. We present STEAM, a hierarchical transfer frame...
  </details>

- **2026-08-03** — Daeyoung Roh, Donghee Han — [HALT: Verification-Aware Stopping for Retrieval-Augmented Search Agents](http://arxiv.org/abs/2608.02009v1)
  <details><summary>📄 Abstract</summary>
  Retrieval-augmented search agents answer multi-hop questions by repeatedly issuing search queries and accumulating evidence. This creates a stopping problem: after the necessary evidence has appeared, further retrieval often adds cost, latency, and distracting context rather than useful information. We frame stopping as evidence coverage rather than generator confidence, and introduce HALT, a lightweight verification-aware policy that leaves the search agent unchanged. Given expected hop claims,...
  </details>

- **2026-08-03** — Valentin Gorgodian, Olivier Poirot, Alain Schmitt et al. — [Phylogeny.fr: the phylogenetic platform designed for non-specialists](http://arxiv.org/abs/2608.01960v1)
  <details><summary>📄 Abstract</summary>
  Phylogenetic analysis has become a standard approach across many areas of biology, yet the growing complexity of phylogenetic methods and software remains a major obstacle for non-specialists. Since its launch in 2008, Phylogeny.fr has provided an accessible web platform for building phylogenetic trees using widely accepted methods without requiring local software installation. Here, we present a major redesign and modernization of the service. The new version integrates state-of-the-art tools w...
  </details>

- **2026-08-03** — Cheng-Yao Hong, Ting-Wei Lin, Yun-Chung Lai et al. — [Event ActivityNet: A Large-Scale Simulated-Event Benchmark for Untrimmed Action Understanding](http://arxiv.org/abs/2608.01948v1)
  <details><summary>📄 Abstract</summary>
  Long-horizon event-based action understanding remains underexplored because existing datasets largely comprise short, trimmed clips, while collecting native event streams with dense temporal annotations is costly. We introduce Event ActivityNet, a large-scale simulated-event benchmark derived from human-annotated, untrimmed ActivityNet videos. It comprises 3,263 videos, 200 action classes, and 106.94 hours, with matched 5-bin and 9-bin event-voxel representations, temporal action annotations, an...
  </details>

- **2026-08-03** — Jeonghyeok Do, Munchurl Kim — [GeoCore-9B: Towards Geo-Aware Generative Foundation Models in Earth Observation](http://arxiv.org/abs/2608.01896v1)
  <details><summary>📄 Abstract</summary>
  Existing generative models for earth observation (EO) predominantly rely on fine-tuning natural image priors, which limits their scalability and introduces perspective biases that conflict with geospatial constraints. To address this, we introduce GeoCore-9B, a 9-billion-parameter generative foundation model, which is the first of its scale to be trained from scratch exclusively on EO data. Unlike previous EO foundation models, GeoCore-9B is built upon a Flow Matching-based Diffusion Transformer...
  </details>

- **2026-08-03** — Zijian Shen, Taijie Chen, Bin Zhou et al. — [LAB-Tab: LLM-Augmented Bayesian Network Adaptation for Few-Shot Tabular Generation](http://arxiv.org/abs/2608.01879v1)
  <details><summary>📄 Abstract</summary>
  Tabular data generation supports analysis and decision-making when target-domain data are scarce, yet collecting complete target samples is often costly. A practical but underexplored setting provides only a few target records together with richer source data from a related domain. Existing few-shot tabular generators often either fit sparse target statistics directly, which can overfit incidental patterns, or reuse source-domain generators, which may preserve dependencies that no longer hold in...
  </details>

- **2026-08-03** — Juntong Wang, Shengkun Yang, Xiyuan Wang et al. — [Rewriting or Reweighting? A Geometric Account in Language Models](http://arxiv.org/abs/2608.01835v1)
  <details><summary>📄 Abstract</summary>
  Post-training can substantially alter language-model behavior, yet aggregate behavior rates do not reveal whether training removes an existing mechanism, creates a new one, or changes how an inherited mechanism is used. We study this question through two mechanistically distinct failures, repetition as a decoding-attractor pathology and sycophancy as a preference-related alignment failure. We introduce behavioral manifold analysis, which isolates behavior-specific geometry by selecting sparse be...
  </details>

- **2026-08-03** — YuFei Luo, Xiucheng Xu, Zhen Yang — [MemSIF: From Structured Interactions to Dual-Track Fact Memory for LLM Agents](http://arxiv.org/abs/2608.01742v1)
  <details><summary>📄 Abstract</summary>
  Long-term memory is critical for LLM agents operating over long-horizon interactions. However, several persistent limitations of existing memory systems can be traced to two recurring misalignment patterns in long-term interaction settings: Temporal-Structural Misalignment (TSM) and Delayed Utility Manifestation (DUM). TSM arises when temporal proximity does not reliably align with topical or event-level relatedness, whereas DUM arises when write-time salience does not reliably predict future qu...
  </details>

- **2026-08-03** — Lingbo Li, Anuradha Mathrani, Teo Susnjak — [Constructing Executable Analytical Knowledge Representations for Meta-Analysis Synthesis Using an Agentic Harness](http://arxiv.org/abs/2608.01711v1)
  <details><summary>📄 Abstract</summary>
  Meta-analysis synthesis highlights a fundamental challenge in knowledge-based scientific analysis: structured evidence does not by itself represent the analytical knowledge required for executable computation. Decisions about evidence assignment, analytical contrasts, outcome and time-point alignment, effect-size formulation, and methodological admissibility must be explicit before statistical execution. Existing automated approaches often embed these decisions in model outputs, generated code, ...
  </details>

- **2026-08-03** — Yu Chen, Xiaohong Li, Xiaole Wang et al. — [CRAFT: Compression via Recursive Adaptive Fusion of Video Tokens for Vision-Language Models](http://arxiv.org/abs/2608.01644v1)
  <details><summary>📄 Abstract</summary>
  In video understanding, vision-language models (VLMs) must ingest massive numbers of visual tokens, causing the computational and memory cost of the prefill stage to rise sharply. Such visual sequences are highly redundant along the spatio-temporal dimension, yet a high compression ratio is often accompanied by the loss of critical details. Existing token-compression methods either employ heuristic, training-free compression with limited content adaptivity or introduce additional modules that re...
  </details>

- **2026-08-03** — Sota Nakashima, Yuta Ishimoto, Masanari Kondo et al. — [How Well Do LLMs Generate Taxonomies in the SE Domain? A Multi-perspective Evaluation Framework](http://arxiv.org/abs/2608.01592v1)
  <details><summary>📄 Abstract</summary>
  Taxonomies provide a shared conceptual framework for organizing heterogeneous observations in software engineering (SE) research. Manually constructing such taxonomies is labor-intensive and requires annotators with expertise in the SE domain. While advances in Large Language Models (LLMs) have led to the emergence of automated taxonomy generation methods outside the SE domain, their applicability to technically complex SE artifacts remains unclear. In this experience paper, we present the first...
  </details>

- **2026-08-03** — Tyler Ashoff, Jordan Rodu — [Semantic Alignment of AI Models: Concept Collapse, Checkpoint Dynamics, and Cross-Lingual Transfer](http://arxiv.org/abs/2608.01585v1)
  <details><summary>📄 Abstract</summary>
  Language model benchmarking is a difficult task. Outcome reasoning alone does not test the model's conceptualization of language and popular open-source benchmarks are quickly saturated or ingested as training data. It is important to test the model's output, but augmenting these tests by characterizing semantic structure gives more insight to how models relate abstract concepts. However, the high dimensional embedding spaces are not easy to interpret. This work demonstrates how topological meth...
  </details>

- **2026-08-03** — Liheng Ma, Rui Heng Yang, Zhanguang Zhang et al. — [Faster-WAM: Do World Action Models Need Deep Action Modules?](http://arxiv.org/abs/2608.02365v1)
  <details><summary>📄 Abstract</summary>
  World Action Models (WAMs) couple robot action prediction with video world models. Existing WAMs with shared-backbone and Mixture-of-Transformers designs generally tie the depth of the action module to that of the video backbone, resulting in substantial computational overhead and high inference latency. To address this limitation, we introduce Dock of Transformer (DoT), a video-centric design principle that treats a pretrained video Transformer as a representation hub and connects lightweight o...
  </details>

- **2026-08-03** — Naho Orita, Hayato Ogawa, Daisuke Kawahara — [Human-LLM Alignment in Language Attitudes Toward Non-Native Japanese](http://arxiv.org/abs/2608.01629v1)
  <details><summary>📄 Abstract</summary>
  Large language models (LLMs) increasingly evaluate human writing in high-stakes domains such as hiring and academic assessment, putting non-native speakers at particular risk. Drawing on the language attitudes framework, we compared human and LLM evaluations of parallel L1- and L2-written Japanese emails on three dimensions: fluency, status, and solidarity. Japanese raters rated L2 texts significantly lower on all three dimensions, with a fluency gap roughly twice the size of the status and soli...
  </details>

- **2026-08-02** — Tianzhu Zhang, Changgang Zheng, Shanshan Wang et al. — [From Network Automation to Trustworthy Autonomous Networking in the LLM Era: A Network Control Intelligence Perspective](http://arxiv.org/abs/2608.01538v1)
  <details><summary>📄 Abstract</summary>
  Since the inception of modern communication networks, the quest for operations automation has never ceased. Yet the evolution of network automation is difficult to characterize with a single maturity ladder. Throughout this history, network control systems have expanded their capabilities for observation, decision support, routine execution, and operator interaction, but these capabilities have not advanced uniformly. Such uneven progress makes the degree of automation an unreliable proxy for tr...
  </details>

- **2026-08-02** — Guiqiu Liao, Matjaz Jogan, Daniel A. Hashimoto — [Slot2Text: Object-Centric Visual Tokenization for Efficient and Spatially Traceable Surgical MLLMs](http://arxiv.org/abs/2608.01473v1)
  <details><summary>📄 Abstract</summary>
  Multimodal large language models (MLLM) for surgical scene understanding typically inject hundreds of dense visual tokens into a language model, leading to costly inference and limited spatial traceability for generated answers. We present Slot2Text, a dual-mode surgical MLLM that replaces dense representations of visual input with a compact set of regions encoded as slot latents. Instead of relying on contrastive alignment of the visual encoder with language, Slot2Text groups self-supervised vi...
  </details>

- **2026-08-02** — Priyanka Dey, Brihi Joshi, Preyashi Poddar et al. — [PALMs: Using Multi Construct-Grounded Rationales for Modeling Population Preferences in LLMs](http://arxiv.org/abs/2608.01458v1)
  <details><summary>📄 Abstract</summary>
  Large language models are being extensively used to simulate individual user behavior, yet faithfully representing a population requires capturing the systematic variation in values, beliefs, and cultural norms that distinguish one group from another. We introduce Population Aligned Language Models (PALMs), a suite of models each aligned to specific populations, covering five countries: USA, India, Brazil, France and Italy. PALMs are created by synthesizing rationales grounded in psychological a...
  </details>

- **2026-08-02** — Taher A. Ghaleb — [Doc2CI: A Multi-Service Study of CI Configuration Generation Using Large Language Models](http://arxiv.org/abs/2608.01451v1)
  <details><summary>📄 Abstract</summary>
  Adopting Continuous Integration (CI) often requires writing YAML configurations that are error-prone and challenging to maintain. Despite increasing LLM use in software engineering, their ability to generate CI configurations from natural language across services and model families remains unclear. This paper presents a large empirical study on using LLMs to generate CI configurations. We introduce DOC2CI, a benchmark of 3,363 description-to-YAML pairs collected from the official documentation o...
  </details>

- **2026-08-02** — Shengwei Xu, Yuxuan Lu, Yifan Wu et al. — [Scoring Rules! Statistical and Strategic Alignment for Text Evaluation Metrics](http://arxiv.org/abs/2608.01423v1)
  <details><summary>📄 Abstract</summary>
  Reference-based text evaluation metrics, which are widely used to assess natural language generation systems, score a candidate response by comparing it with a reference response. The reliability of an evaluation metric is usually judged by its statistical correlation with human ratings. However, as these metrics are increasingly used as optimization objectives, correlation alone is no longer sufficient: agents may strategically game the evaluation metric. We study this issue through two complem...
  </details>

- **2026-08-02** — Reza Asgharzadeh Jelodar, Kazem Bitaghsir Fadafan, Giacomo Cacciapaglia — [Impact of Higgs precision measurements at the LHC and FCC-ee on the spectrum of composite Higgs models](http://arxiv.org/abs/2608.01353v1)
  <details><summary>📄 Abstract</summary>
  We investigate the minimal composite Higgs model based on the symmetry-breaking pattern $\mathrm{SU}(4)\rightarrow\mathrm{Sp}(4)$, where electroweak symmetry breaking is governed by the vacuum alignment angle $θ$. Through the leading-order relations $κ_V=\cosθ$ and $m_η=m_h/\sinθ$, precision measurements of Higgs couplings are translated into direct constraints on the vacuum structure and the singlet pseudo-Nambu--Goldstone boson mass. Using the current ATLAS Run-2 measurement of $κ_V$, we const...
  </details>

- **2026-08-02** — Jianan Jiang, Bin Li — [PartInteractor: Intent-Driven Part-Aware 3D Authoring for Continuous Co-Creation in XR](http://arxiv.org/abs/2608.01335v1)
  <details><summary>📄 Abstract</summary>
  As Extended Reality (XR) evolves into an immersive computing medium, interactive 3D authoring becomes essential for creative and functional workflows. However, existing generative XR systems produce monolithic outputs lacking explicit semantic structure, limiting post-generation control. We introduce PartInteractor, a representation-to-interaction framework that investigates how semantic part hierarchies can be incorporated into generative XR authoring, and exposed as first-class, directly manip...
  </details>

- **2026-08-02** — Yibin Huang, Jixiang Hong, Zongzhao Li et al. — [SPAE: Spectrally Guided Autoencoder for Pretrained Visual Latents](http://arxiv.org/abs/2608.01306v1)
  <details><summary>📄 Abstract</summary>
  Latents from vision foundation models (VFMs) are semantically rich and well suited for visual understanding. Recent representation autoencoder methods such as RAE have shown that they can provide promising latent spaces for image generation. However, VFM latents remain difficult to model directly: DiT-generated latents exhibit spectral mismatch with encoder latents, especially in high-frequency components. Our channel-wise spectral analysis further reveals that these high-frequency components ar...
  </details>

- **2026-08-02** — Junno Yun, Yaşar Utku Alçalar, Mehmet Akçakaya — [UDT: Reconciling U-Nets and Diffusion Transformers with Data-Adaptive Token Reduction](http://arxiv.org/abs/2608.01298v1)
  <details><summary>📄 Abstract</summary>
  Diffusion Transformers (DiTs) have emerged as a core architecture in generative modeling due to their scalability and adaptability to multimodal tasks. DiTs comprise isotropic transformer blocks, and learn representations progressively across depth, where the denoising objective drives later layers to focus on fine-detail reconstruction. This results in degraded representation quality and an imbalanced encoder-decoder behavior. Prior approaches such as representation alignment (REPA) mitigate th...
  </details>

- **2026-08-02** — Bruno Brocai, Ilaria Papagno, Mayumi Ohta — [PlainMedScale: A Corpus of Multi-Level Simplified Medical Texts in German and English](http://arxiv.org/abs/2608.01158v1)
  <details><summary>📄 Abstract</summary>
  We introduce PlainMedScale, a topic-aligned medical corpus spanning four levels of comprehensibility in German and English, drawn from MSD (professional and consumer), Gesund.Bund, Apotheken Umschau Einfache Sprache, and the NHS. The four tiers correspond to distinct communicative functions --- reference, explanation, decision support, and access --- and move beyond the binary expert--lay contrast of prior corpora. In two pilot studies enabled by the alignments, we show that many readability met...
  </details>

- **2026-08-02** — Junsheng Wang, Chao Chen, Mengying Xie et al. — [SG-Layout: Structured Scene Graph-Guided Layout Generation with LLMs](http://arxiv.org/abs/2608.01106v1)
  <details><summary>📄 Abstract</summary>
  Understanding and generating spatially coherent layouts from natural language remains a fundamental yet challenging task for large language models (LLMs). Existing LLMs often struggle to capture explicit geometric relationships and structural dependencies between objects. To address this issue, we propose SG-Layout, a graph-guided layout generation framework that explicitly incorporates structured spatial knowledge into LLMs. SG-Layout follows a two-stage training paradigm: (1) a graph-language ...
  </details>

- **2026-08-02** — Damir Nurtdinov, Alexei Kornaev, Alexander Maloletov — [RL Bootstrapping of OpenVLA-OFT for a Novel Robot Embodiment](http://arxiv.org/abs/2608.01013v1)
  <details><summary>📄 Abstract</summary>
  Adapting a pretrained vision-language-action (VLA) policy to a new robot usually assumes embodiment-specific demonstrations. This assumption is especially restrictive for custom robots whose morphology differs strongly from the manipulators seen in large robot datasets. We study a harder setting: zero-demo embodiment alignment of OpenVLA-OFT on a cable-driven parallel robot (CDPR) with a simple gripper and a previously unseen control interface. Instead of supervised fine-tuning, we use reinforce...
  </details>

- **2026-08-02** — Ofir Ben Shoham, Oriel Perets, Nir Grinberg et al. — [MedUPS: Towards Diagnostic Assistance in Uncommon Medical Cases with Large Language Models](http://arxiv.org/abs/2608.01012v1)
  <details><summary>📄 Abstract</summary>
  Uncommon and off-guideline cases are difficult for clinical decision support, because physicians must make a series of management decisions under diagnostic uncertainty and rarely see the full case at once. Most large language model (LLM) benchmarks for medicine score only the final diagnosis, yet much of clinical care turns on the next appropriate action: the next test to order, the imaging study to obtain, the specialist to involve, or the differential to pursue. We introduce MedUPSQA, a datas...
  </details>

- **2026-08-02** — Myeongkyun Kang, Yanting Yang, Xiaoxiao Li — [Location-Aware Fine-Grained Representation Learning for Medical Vision Foundation Models](http://arxiv.org/abs/2608.00976v1)
  <details><summary>📄 Abstract</summary>
  Fine-grained visual representations are essential for medical image analysis, particularly when diagnostically relevant evidence is subtle and spatially localized. Modern transformer-based medical vision encoders must therefore learn patch-level representations that are both clinically meaningful and spatially consistent. Without these properties, large vision-language models (LVLMs) operate on an ambiguous visual foundation, limiting their ability to generate clinically reliable and spatially g...
  </details>

- **2026-08-01** — Zongyuan Shen, Shalabh Gupta, Shancheng Zhao et al. — [Learning-Based Motion Planning for Dynamic Environments: From Foundational Algorithms to Emerging Paradigms](http://arxiv.org/abs/2608.00625v1)
  <details><summary>📄 Abstract</summary>
  Motion planning in dynamic environments is a fundamental problem in robotics, aiming to generate safe and efficient paths, trajectories, or control actions in the presence of moving obstacles, uncertain predictions, and multi-agent interactions. It has broad applications in autonomous driving, service robotics, warehouse logistics, human-robot collaboration, crowd navigation, and multi-robot systems. This survey reviews representative works published primarily between 2015 and 2025, with a parti...
  </details>

- **2026-08-01** — Xiaokai Rong, Mohammadali Sefidi Esfahani, Aashish Yadavally et al. — [Can Perplexity Serve as a Cognitive Signal for Code Understandability?](http://arxiv.org/abs/2608.00624v1)
  <details><summary>📄 Abstract</summary>
  Recent work suggests that token-level perplexity from large language models can align with localized human confusion during code comprehension. This raises a natural question: can perplexity also serve as a snippet-level signal for code understandability? We conduct an empirical study of this question across multiple human-grounded datasets, including method-level understandability judgments, output-prediction tasks, and accepted understandability-improvement patches. Despite prior token-level e...
  </details>

- **2026-08-01** — Sean Gip Lim, William Chandra Tjhi, Hai Leong Chieu — [Native Multilingual Chain-of-Thought Reasoning in Low-Resource Southeast Asian Languages](http://arxiv.org/abs/2608.00533v1)
  <details><summary>📄 Abstract</summary>
  Large Language Models have achieved substantial progress in reasoning capabilities. Yet in low-resource native settings, many suffer from cross-lingual collapse, reverting to English during intermediate steps that require complex logical reasoning. This presents a cold-start bottleneck for policy optimization, whereas standard fine-tuning risks catastrophic forgetting due to cross-lingual representation drift. To address these challenges, we introduce the Onramp-Sequence Cross-Distillation (OSCD...
  </details>

- **2026-08-01** — Yufei Zhang, Chenlu Zhan, Donghui Sun et al. — [SpatialAfford: Teaching Compact VLMs Where to Look and Where to Ground for Affordance](http://arxiv.org/abs/2608.00502v1)
  <details><summary>📄 Abstract</summary>
  Affordance grounding aims to localize the functional region for interaction, such as the handle to grasp or the button to press, rather than the whole object. This makes it more challenging than generic visual grounding because the target region is smaller, more ambiguous, and more dependent on task context, especially for compact vision-language models (VLMs) used in embodied settings. Recent sequence-level supervision and reinforcement learning improve coordinate prediction quality, yet compac...
  </details>

- **2026-08-01** — Liangjing Shao, Beilei Cui, Yiming Huang et al. — [Boosting Generalizable Depth Estimation in Endoscopy by Mixture of Lightweight Experts and Intrinsic Image Alignment](http://arxiv.org/abs/2608.00415v1)
  <details><summary>📄 Abstract</summary>
  Depth estimation is a significant task for 3D perception in endoscopic surgeries. However, illumination interference and feature diversity in various endoscopic scenes are still challenges for generalizable depth estimation and ego-motion estimation. Based on this, a novel self-supervised framework, EndoMINI, is proposed for depth estimation in endoscopic scenes. Specifically, mixture of low-rank experts (MiLoRE) is proposed to perform parameter-efficient fine-tuning, which can also boost the mo...
  </details>

- **2026-07-31** — Mamdouh Alenezi — [Educating the Agentic Engineer: Curricula, Collaboration, and Continuous Learning in the AI Era](http://arxiv.org/abs/2607.29610v1)
  <details><summary>📄 Abstract</summary>
  Generative and agentic artificial intelligence (AI) are reconfiguring software and systems engineering from a discipline centered on human authorship of artifacts to one focused on directing, verifying, and governing autonomous systems. This transition demands a new professional archetype, the \emph{agentic engineer}, whose enduring value lies in intent specification, orchestration of multi-agent workflows, critical evaluation of machine-generated outputs, and ethical judgment. This article pres...
  </details>

- **2026-07-31** — Binnan Liu, Yechi Ma, Tian Xie et al. — [TraceViT: Grounded Trace Supervision for Visual Abstract Reasoning](http://arxiv.org/abs/2607.29586v1)
  <details><summary>📄 Abstract</summary>
  The Abstraction and Reasoning Corpus (ARC) tests whether a model can infer an unseen transformation from a few input-output examples and apply it to a new grid. Looped visual reasoners refine predictions over multiple iterations, but conventional training constrains only the final output, leaving intermediate refinements unconstrained. We propose that these refinements should instead follow the transformation step by step. We introduce TraceViT, a looped visual reasoner trained with semantically...
  </details>

- **2026-07-31** — Carlos Rodriguez-Pardo, Massimo Tavoni — [TerraNova: A Foundation Model for the Anthropocene](http://arxiv.org/abs/2607.29527v1)
  <details><summary>📄 Abstract</summary>
  A defining problem of the Anthropocene is to model the physical Earth and human societies as one coupled system, yet no learned representation spans their observational breadth. We argue the obstacle is geometric: the physical Earth is measured as continuous fields that ignore political borders, whereas societies are reported for administrative units. Earth-system foundation models serve the first geometry; coupling it to the second has required lossy averaging over borders. We introduce TerraNo...
  </details>

- **2026-07-31** — Penglin Zhu, Jungang Xu — [ModelEquivBench: Certifying Multi-Relational Evaluation of LLM-Generated Optimization Models](http://arxiv.org/abs/2607.29431v1)
  <details><summary>📄 Abstract</summary>
  Large language models increasingly generate optimization models from natural language, but existing evaluation often reduces a generated model and its ground truth to a single equivalent/not-equivalent verdict or an execution-success rate--labels that are neither independently checkable nor faithful to the multiple distinct senses in which two formulations can agree. We present ModelEquivBench, a certifying, multi-relational evaluation system that reports a per-pair semantic profile E0--E6: mode...
  </details>

- **2026-07-31** — Domen Vake, Jernej Vičič, Aleksandar Tošić — [Bridging the Question-Answer Gap in Retrieval-Augmented Generation: Hypothetical Prompt Embeddings](http://arxiv.org/abs/2607.29402v1)
  <details><summary>📄 Abstract</summary>
  Retrieval-Augmented Generation (RAG) systems synergize retrieval mechanisms with generative language models to enhance the accuracy and relevance of responses. However, bridging the style gap between user queries and relevant information in document text remains a persistent challenge in retrieval-augmented systems, often addressed by runtime solutions (e.g., Hypothetical Document Embeddings (HyDE)) that attempt to improve alignment but introduce extra computational overhead at query time. To ad...
  </details>

- **2026-07-31** — Muhayy Ud Din, Irfan Hussain — [SAGP: Semantic Affordance-Guided Grasp Planning via Coarse-Zone VLM Reasoning](http://arxiv.org/abs/2607.29374v1)
  <details><summary>📄 Abstract</summary>
  Geometry-based grasp planners ensure physically valid grasps but ignore functional semantics, often generating grasps that are antipodal and collision-free yet practically inappropriate, for example, gripping a mug by its rim, a knife by the blade, or a bottle near its cap. These inconsistencies cause the downstream task to fail even when traditional grasp metrics are met. Existing vision-language model (VLM) approaches either depend on fine-grained, category-specific part segmentation or attemp...
  </details>

- **2026-07-31** — Muhammad Talha, Muhammad Ahmed Amer — [SatEdit: Mask-Conditioned Image Editing via VLM-Guided Segment Annotation](http://arxiv.org/abs/2607.29367v1)
  <details><summary>📄 Abstract</summary>
  Satellite image editing requires spatially precise object-level control, but supervised editing datasets for overhead imagery are costly to build because object masks, semantic labels, and paired edits are rarely available at scale. We introduce SatEdit, a mask-conditioned satellite image editing framework that constructs training supervision from unlabeled imagery. SatEdit proposes object masks with a seg- mentation foundation model, assigns semantic la- bels to sampled segments with a Vision-L...
  </details>

- **2026-07-31** — Siyang Cai, Cangyuan Li, Wenjing Chang et al. — [RTLCurator: Label-Efficient Data Curation for RTL Generation](http://arxiv.org/abs/2607.29283v1)
  <details><summary>📄 Abstract</summary>
  Training large language models (LLMs) to write register-transfer level (RTL) requires large corpora of paired specifications and code, and such data is scarce enough that most public corpora are now synthesized. Synthesis provides scale but not correctness, and in two widely used RTL datasets only 24.4% and 53.5% of pairs pass generated functional tests. This raises the question of how much of such a corpus to keep and which part of it. Correctness alone is a poor answer. A pair that misbehaves ...
  </details>

- **2026-07-31** — Ruiming Liang, Yi Zhong, Yizhen Yuan et al. — [Don't Mix Rewards, Mix Policies: Policy Decomposition and Optimization for Multi-Reward RL](http://arxiv.org/abs/2607.29246v1)
  <details><summary>📄 Abstract</summary>
  Modern large language models (LLMs) are expected not just to answer correctly, but to adapt their behavior to different human values and use cases. As a result, multi-reward reinforcement learning (RL) has become an increasingly important problem for LLMs, where each reward captures a different aspect of desired behavior. However, optimizing with multiple rewards suffers from a more severe alignment tax issue, where different optimization objectives can trade off or even conflict with each other...
  </details>

- **2026-07-30** — Qiushi Sun, Kanzhi Cheng, Yian Wang et al. — [OSReward: Instituting Standardized Evaluation for Cross-Platform Computer-Use Reward Models](http://arxiv.org/abs/2607.28609v1)
  <details><summary>📄 Abstract</summary>
  Computer-using agents (CUAs) are advancing rapidly across the digital world. A CUA trajectory records the agent's actions, states, and reasoning. Verifying whether it fulfilled the task instruction is central to CUA evaluation, data curation, and reinforcement learning. Neither human-written verifiers nor human annotators can provide such verification at scale, so the field increasingly turns to vision-language models (VLMs) as judges of CUA trajectories. But a fundamental question has long gone...
  </details>

- **2026-07-30** — Xiao Luo, Mingyang Du, Xin Zhou et al. — [ROAD: Reciprocal-Objective Alignment of Discriminative Semantics for 3D Shape Generation](http://arxiv.org/abs/2607.28581v1)
  <details><summary>📄 Abstract</summary>
  High-fidelity 3D generation predominantly relies on scaling model capacity and data, which incurs prohibitive computational costs. This paradigm typically requires learning geometry from scratch and overlooks the rich semantic and structural priors already encapsulated in discriminative 3D foundation models. We contend that leveraging the profound understanding of the 3D world possessed by these discriminative models can significantly reduce generative cost. To this end, we propose ROAD, a frame...
  </details>

- **2026-07-30** — Yunzhan Fu, Xiangyu Shen, Yifei Sun et al. — [MIND: Multimodal Intent-Driven Network via Diffusion Transformers for Medical Image Fusion](http://arxiv.org/abs/2607.28565v1)
  <details><summary>📄 Abstract</summary>
  Medical image fusion aims to integrate complementary information from diverse imaging modalities to support clinical diagnosis. Existing methods typically apply uniform fusion rules globally, lacking a deep understanding of diagnostic intents and pathological structures. To address these limitations, we propose MIND, a Multimodal Intent-Driven Network via Diffusion Transformers (DiTs) for medical image fusion. Specifically, we utilize BioMedGPT to generate intent-driven fusion texts from source ...
  </details>

- **2026-07-30** — Ioana-Roxana Boriceanu, Liviu P. Dinu — [Creative Transformation in Literary Texts: Modelling Change Across Representational Levels](http://arxiv.org/abs/2607.28513v1)
  <details><summary>📄 Abstract</summary>
  Creativity is often framed as the production of novelty, yet many cultural works emerge through transformation of earlier artifacts and not through isolated invention. Drawing on theories of imitation by Gabriel Tarde and James Mark Baldwin, this paper models creativity as selective transformation across multiple levels of textual representation. We introduce a multi-level framework that compares literary texts across lexical, semantic, conceptual, structural, and narrative dimensions using dire...
  </details>

- **2026-07-30** — Hansika Ekanayake Mudiyanselage, Rohan Jai Dharmaraj, Malik Abdul Sami et al. — [Integrating AI into Requirements Quality Learning in Software Engineering Education: A TPACK-Guided Empirical Study](http://arxiv.org/abs/2607.28176v1)
  <details><summary>📄 Abstract</summary>
  The rapid adoption of generative Artificial Intelligence (AI) in software engineering (SE) practice creates a need for pedagogically grounded approaches to AI integration in SE education, especially in conceptually intensive subjects such as requirements engineering (RE). This study examines a TPACK-guided integration of a multi-agent AI tool into a master-level RE assignment on requirements quality analysis. Using a mixed-methods design (N=100; 72 submissions analysed), we examine how structure...
  </details>

- **2026-07-30** — Paulo Carvao, Claudio Mayrink Verdun, Isabel Adler et al. — [An Instrument to Evaluate Governance Proposals: AI Policy Analysis at Scale](http://arxiv.org/abs/2607.28094v1)
  <details><summary>📄 Abstract</summary>
  This paper introduces a policy analysis framework for systematic, transparent assessment of AI governance proposals in an evolving and contested regulatory landscape. AI policy debates often collapse into binary positions that obscure underlying tradeoffs and normative assumptions. The framework structures policy analysis around multiple policy attributes, allowing users to surface priorities and tensions without prescribing outcomes. We use a mixed-methods approach that integrates qualitative i...
  </details>

- **2026-07-30** — Qinhan Yu, Jun Guang, Chong Chen et al. — [VIG-RL: Learning to Search and Insert for Verified Image Grounding](http://arxiv.org/abs/2607.28055v1)
  <details><summary>📄 Abstract</summary>
  In knowledge-intensive scenarios, providing reliable interleaved text-image responses requires Verified Image Grounding (VIG): the precise integration of retrieved authentic visual evidence. Existing retrieval-augmented frameworks predominantly rely on decoupled, static pipelines, inherently failing to dynamically reason about when external knowledge is required and where visual assets should be contextually inserted. To bridge this gap, we propose VIG-RL, an autonomous agentic framework that fo...
  </details>

- **2026-07-30** — Xingjian Wu, Xuhang Zhu, Xingchen Liu et al. — [ClawTrack: Towards Trace-Level Evaluation and Improvement of Real-World Autonomous Agents](http://arxiv.org/abs/2607.28037v1)
  <details><summary>📄 Abstract</summary>
  As LLM-based agents are deployed in complex, multi-step workflows, a critical evaluation gap has emerged: most existing benchmarks judge only final outcomes, unable to distinguish reliable reasoning from lucky success or attribute failures to specific process deficiencies, hindering attribution in long-horizon tasks.   In this work, we present ClawTrack, a dual-assessment benchmark that simultaneously measures what an agent achieves (Task Score) and how it achieves it (Process Score). ClawTrack ...
  </details>

- **2026-07-30** — Xianpeng Zhang, Jiahua Yang, Dongyu Chen et al. — [MMLDSum-LLM: Multimodal Long-Document Summarization with Visual-Alignment and Keyword-Aware](http://arxiv.org/abs/2607.28006v1)
  <details><summary>📄 Abstract</summary>
  Multimodal long documents are core carriers of professional knowledge, where critical evidence is sparsely distributed across paragraphs and modalities. This easily causes key information omission and cross-modal hallucinations in summarization by multimodal LLMs. These issues stem from attention drift in long-range dependency modeling and gaps in inter-modal alignment. To address this, we introduce MMLDSum-Bench, a high-quality benchmark for multimodal long-document summarization, covering mult...
  </details>

- **2026-07-30** — Bohan Hou, Haoqiang Lin, Xuemeng Song et al. — [FiRE: Enhancing MLLMs with Fine-Grained Context Learning for Complex Image Retrieval](http://arxiv.org/abs/2607.27959v1)
  <details><summary>📄 Abstract</summary>
  Due to their strong generalizable multimodal processing and reasoning capabilities, Multimodal Large Language Models (MLLMs) have demonstrated significant potential as universal image retrievers, effectively addressing diverse real-world image retrieval tasks. Nevertheless, pioneering studies, while promising, overlook the potential of fine-grained context modeling and disentangled fine-tuning objectives in enhancing MLLMs' retrieval performance, particularly for complex tasks such as long-text-...
  </details>

- **2026-07-30** — Long Zhang, Hao Jiang, Sheng Yu et al. — [Interpretable Representation via LLM-Driven Generative Disentanglement for Local-Life Service Recommendation](http://arxiv.org/abs/2607.27944v1)
  <details><summary>📄 Abstract</summary>
  While large language models (LLMs) have advanced ID-based recommendation through Semantic ID (SID) modeling, existing SID generation frameworks largely follow a single-representation-then-quantization paradigm. This design faces two bottlenecks: semantic entanglement mixes heterogeneous attributes, such as geography, brand, and category, causing information loss during quantization, low-quality SIDs, and severe collisions; moreover, black-box representation learning provides neither explicit att...
  </details>

- **2026-07-30** — Rui Tang, Wentao Yang, Peirong Zhang et al. — [One Patch Is Enough: Reinforcement-Optimized Visual Token Grounding for MLLM-Based Scene Text Spotting](http://arxiv.org/abs/2607.27902v1)
  <details><summary>📄 Abstract</summary>
  Scene text spotting requires high-precision alignment between textual recognition and spatial localization. While visual-token grounding has emerged as a promising formulation for Multimodal Large Language Models (MLLMs), the previous multi-patch paradigm often introduces redundant noise and localization ambiguity, particularly for dense or small text instances. To address this, we propose Single-Patch Text Spotting (SPaTS), a vision-centric framework that routes each text instance through a sin...
  </details>

- **2026-07-30** — Peiyu Hu, Siying Gu, Weihai Lu et al. — [Hierarchical Latent Reasoning for LLM-based Recommendation](http://arxiv.org/abs/2607.27760v1)
  <details><summary>📄 Abstract</summary>
  Large Language Models (LLMs) have shown strong potential for recommendation by leveraging their semantic understanding and contextual modeling capabilities. Recent studies further introduce reasoning mechanisms to improve user preference modeling. However, explicit natural-language reasoning incurs substantial inference overhead, whereas existing latent reasoning methods mainly focus on generating or verifying intermediate states, leaving their layer-wise preference roles and contributions insuf...
  </details>

- **2026-07-30** — Fouad Bousetouane — [Stop Shipping AI Agents on Faith: Capability Is Not Production Readiness](http://arxiv.org/abs/2607.27677v1)
  <details><summary>📄 Abstract</summary>
  AI agents are moving into production workflows where they retrieve information, call tools, maintain state, and act on behalf of users or organizations, but many release decisions still rely on capability signals, demos, or behavioral tests that do not show whether an agent is ready to operate under production constraints. Capability is therefore not production readiness. This paper introduces the ProofAgent Index (PAI), a governance readiness index for AI agents. PAI combines four dimensions of...
  </details>


### 📂 robustness
*鲁棒性与可靠性 / Robustness & Reliability* — 79 papers

- **2026-08-03** — Saman Sarker Joy, Niloy Farhan — [MedPRESS: A Multi-turn Benchmark for Patient-Pressure-Induced Medical Sycophancy in LLMs](http://arxiv.org/abs/2608.02520v1)
  <details><summary>📄 Abstract</summary>
  Large language models (LLMs) are increasingly used for health-related advice. Existing research measures their safety with static questions rather than pressured patient-facing conversations. We introduce MedPRESS, a multi-turn benchmark for measuring patient-pressure-induced sycophancy in LLMs. MedPRESS contains 600 medically grounded five-turn dialogues across three scenario families: medication and treatment demand, personal health self-care, and symptom triage and care resistance. Each dialo...
  </details>

- **2026-08-03** — Yan Huang, Guowei Wang, Xu Wang et al. — [Local Margin Restoration for Test-Time Adaptation of Vision-Language Models](http://arxiv.org/abs/2608.02216v1)
  <details><summary>📄 Abstract</summary>
  Vision-language models (VLMs) such as CLIP exhibit remarkable zero-shot capabilities, yet their performance frequently degrades sharply under unexpected test-time distribution shifts. While Test-Time Adaptation (TTA) offers a promising solution, continuously adapting VLMs over an unlabeled test stream presents fundamental challenges. Conventional top-1-centric updates often reinforce errors by corrupting the local semantic geometry among related classes, while iterative adaptation exacerbates pr...
  </details>

- **2026-08-03** — Fengxian Ji, Yuke Li, Jingpu Yang et al. — [Style Wins, Substance Loses: A Diagnosis of LLM-as-Judge in Idea Generation](http://arxiv.org/abs/2608.01666v1)
  <details><summary>📄 Abstract</summary>
  However, whether these judges truly evaluate the scientific substance of ideas or are influenced by superficial stylistic presentation remains an open question. To address this question, we propose SciStyleBench, a unified three-component benchmark for diagnosing and mitigating stylistic bias in LLM-based idea evaluation: (i) First, SciStyleStage, a three-stage evaluation environment that applies controlled stylistic perturbations to fixed scientific content across three settings no context, fix...
  </details>

- **2026-08-03** — Brandon Wang, Andrei S. Tyrin, Daniil A. Boiko — [onepot-Bench 0: towards lab-aware in silico chemistry benchmarks](http://arxiv.org/abs/2608.02595v1)
  <details><summary>📄 Abstract</summary>
  Language models are playing an increasingly important role in laboratory science, performing tasks such as experiment planning, execution, and post-hoc analysis. However, precisely measuring their abilities is difficult, as scientific capabilities require a mixture of both problem-solving skills and domain-specific intuition. Existing evaluations rarely measure the capabilities required to make reliable decisions in a physical laboratory and often rely on public data that may have appeared in mo...
  </details>

- **2026-08-03** — Vernon Toh, Navonil Majumder, Zhengyuan Liu et al. — [ScrambleToolBench: Agents Search Exhaustively Even When Their Own Map Points to the Next Step](http://arxiv.org/abs/2608.02358v1)
  <details><summary>📄 Abstract</summary>
  To operate robustly in open-world environments, autonomous agents should be able to infer the behavior of unfamiliar systems through interaction alone, even in the absence of documentation. However, existing tool-use benchmarks expose semantic tool schemas in static environments, allowing agents to rely on prior knowledge rather than autonomous discovery. To address this limitation, we introduce ScrambleToolBench, an interactive terminal benchmark designed to isolate behavioral reasoning. By rem...
  </details>

- **2026-08-03** — Jin Cui, Chuanchang Su, Jiayi Lu et al. — [HAFI-VLM: A Frequency Perspective for Diagnosing and Enhancing Visual Perception in Vision-Language Models](http://arxiv.org/abs/2608.02124v1)
  <details><summary>📄 Abstract</summary>
  Vision-language models (VLMs) remain unreliable when predictions require fine-grained visual evidence. We identify a previously overlooked cause: spectral response rigidity. Despite substantial frequency variation across images and tasks, pretrained vision encoders exhibit persistent, encoder-specific layerwise spectral profiles that change only marginally under downstream fine-tuning. Since pretrained vision encoders only receive images, they cannot adapt spectral extraction to the evidence req...
  </details>

- **2026-08-03** — Zhaotian Gu, Jie Su, Weiwei Wang et al. — [Divisive Normalization Shapes Low-Rank Slow Manifolds for Continuous Working Memory](http://arxiv.org/abs/2608.01947v1)
  <details><summary>📄 Abstract</summary>
  The ability to robustly maintain and update continuous variables is a hallmark of working memory. While classical continuous attractor networks suffer from severe fine-tuning fragility, standard artificial recurrent neural networks (RNNs) like GRUs and LSTMs typically fail to stably learn continuous manifolds, instead shattering the state space into discretized point attractors. To bridge this gap, we draw inspiration from divisive normalization, a canonical neural computation widely observed ac...
  </details>

- **2026-08-03** — Qi Liu, Jiaxin Mao, Fengbin Zhu et al. — [Diagnosing Search Behavior and Failure Modes in Long-Horizon Search Agents](http://arxiv.org/abs/2608.01913v1)
  <details><summary>📄 Abstract</summary>
  Deep search agents answer difficult information-seeking questions by iteratively issuing search queries to gather supporting evidence, but it remains unclear whether and how greater search effort leads to better answers. We study these questions through a trajectory-level diagnosis of long-horizon search agents. Using human-annotated document-level relevance judgments, we evaluate the evidence retrieved at each search step and separate two stages of agent behavior: what evidence an agent retriev...
  </details>

- **2026-08-03** — Junru Song, Wenhao Zhang, Yang Yang et al. — [CoNav-UAV: Cooperative Dual-Altitude Aerial Navigation via Stackelberg Learning](http://arxiv.org/abs/2608.01802v1)
  <details><summary>📄 Abstract</summary>
  Target-oriented vision-and-language navigation (VLN) on aerial platforms is attracting growing attention for missions such as disaster rescue, infrastructure inspection, and security patrol. In this task, an unmanned aerial vehicle (UAV) needs to locate targets given only a concise description of their appearance and surroundings. This requires global exploration and grounding as well as collision-free close-range approach, two interleaved processes difficult to reconcile within a single agent. ...
  </details>

- **2026-08-03** — Zhaoxin Yu, Qi Shen, Hengli Li et al. — [GradCuit: Credit-Assigned Gradient Flow Enables Robust and Interpretable Test-Time Latent Reasoning](http://arxiv.org/abs/2608.02585v1)
  <details><summary>📄 Abstract</summary>
  Optimization-based latent reasoning improves large language model outputs by optimizing instance-specific continuous states at test time while keeping model parameters frozen. Existing methods, however, typically connect these states to the reasoning trajectory through decoded tokens, making sequence-level credit assignment indirect and obscuring how latent updates shape subsequent reasoning. We introduce GradCuit (gradient through circuit), which inserts optimizable latent states at a selected ...
  </details>

- **2026-08-03** — Xiaosheng Zhao, Yuan-Sen Ting — [Foundation Models for Astrophysics](http://arxiv.org/abs/2608.02573v1)
  <details><summary>📄 Abstract</summary>
  Foundation models are high-capacity networks pretrained once on broad data and then reused across many tasks. This chapter introduces them through the idea of a transferable representation, the internal description a network forms during training, which, rather than the fitted task, is what carries over to new problems. We develop the idea from first principles for an astronomical reader, starting from why a representation matters and what makes one useful, and then surveying the architectures, ...
  </details>

- **2026-08-03** — Luc Trudeau, Maria G. Martini — [Estimating SSIM from MSE for DCT-Based Compressed Images](http://arxiv.org/abs/2608.02549v1)
  <details><summary>📄 Abstract</summary>
  Efficient and perceptually meaningful quality assessment is a fundamental requirement for image and video processing, compression, and streaming systems. This article shows that, in the context of Discrete Cosine Transform ( DCT)-based compressed images, Structural Similarity Index ( SSIM ) can be approximated from global Peak Signal to Noise Ratio (PSNR) or Mean Square Error ( MSE) using local statistics derived only from the reference image. While prior work assumes access to local MSE, we pro...
  </details>

- **2026-08-03** — Xinpeng Hong, Changgang Zheng, Joshua Lilley et al. — [In-Network Market Prediction Using Machine Learning and Limit Order Books](http://arxiv.org/abs/2608.02424v1)
  <details><summary>📄 Abstract</summary>
  Machine learning is significantly transforming algorithmic trading, yet the requirement for rapid execution speeds persists. While both aspects aim to boost profitability, embedding advanced machine-learning techniques with reduced trading latency presents a notable challenge. Adopting in-network machine learning, which involves offloading inference to programmable network devices, offers a delicate equilibrium in this trade-off. In this paper, we present LOBIN, a solution that utilizes machine ...
  </details>

- **2026-08-03** — Victor Ojewale, Ro Encarnación, Suresh Venkatasubramanian et al. — [MonitrLLM: A Community-Centered Evaluation Infrastructure for Large Language Models](http://arxiv.org/abs/2608.02409v1)
  <details><summary>📄 Abstract</summary>
  Benchmark suites assess model capability on controlled tasks; large-scale conversation corpora capture naturalistic use without user feedback; and in-interface feedback mechanisms record satisfaction without task purpose. Together, they leave a critical gap in LLM evaluation: no existing infrastructure routinely links interaction trajectories to user-defined outcomes. We introduce MonitrLLM, open-source infrastructure for community-centered LLM evaluations that links full conversation transcript...
  </details>

- **2026-08-03** — Sathiyamohan Nishankar, Nethmi Pathirana, Pubudu Sanjeewani et al. — [Does Explainability Transfer? A Controlled Benchmark of Attribution Methods on Vision Transformers and CNNs](http://arxiv.org/abs/2608.02396v1)
  <details><summary>📄 Abstract</summary>
  Most evidence on the effectiveness of explainable artificial intelligence (XAI) attribution methods has been established on convolutional neural networks (CNNs), with limited investigation into whether these conclusions generalize to the diverse Vision Transformer (ViT) architectures that now dominate computer vision. This paper presents a controlled benchmark that evaluates attribution quality across five dimensions: faithfulness, localization, robustness, complexity, and computational cost. A ...
  </details>

- **2026-08-03** — Yue Yao, Shengyuan Wang, Xin Chen et al. — [SkillTrace: Traversing a Query-Skill Graph for Composable LLM Agents](http://arxiv.org/abs/2608.02356v1)
  <details><summary>📄 Abstract</summary>
  Large language model agents increasingly solve complex tasks by composing reusable skills from a library. To address this, the key challenge is not merely to retrieve individually relevant skills, but to identify a complete and executable skill composition. In this paper, we argue that this problem can be solved in a graph with three levels: compositional relations among skill queries, similarity between queries and candidates in the skill library, and the dependencies among the selected candida...
  </details>

- **2026-08-03** — Runci Bai, Yucheng Xin, Pu Wang et al. — [Loop-Mamba: A Loop Mamba with Degradation-Aware and Shared Memory for Old Photo Restoration](http://arxiv.org/abs/2608.02346v1)
  <details><summary>📄 Abstract</summary>
  Old photographs often suffer from multiple coupled degradations, including scratches, cracks, fading, blur, noise, and missing regions, severely degrading both visual quality and semantic content. We propose Loop-Mamba, a lightweight loop-based state-space framework that formulates old photo restoration as progressive state evolution, where a persis- tent restoration state is continuously propagated and refined through iterative computation. Specifically, we introduce a Semantic-Guided Degradati...
  </details>

- **2026-08-03** — Roua Rouatbi, Juan-Esteban Suarez Cardona, Ivo F. Sbalzarini — [The Push-Forward Transform for Continuous and Robust Comparison of Dynamic Shapes](http://arxiv.org/abs/2608.02306v1)
  <details><summary>📄 Abstract</summary>
  We introduce a mathematical framework for shape comparison based on mapping functions from the shape domain to a common reference domain. This Push-Forward Transform enables invariant and robust comparison of shapes, preserving intrinsic geometric information. Quantitatively comparing shapes and their temporal evolution is a fundamental challenge in image analysis. Meaningful shape comparison requires representations that are invariant to transformations that do not alter shape itself, such as t...
  </details>

- **2026-08-03** — Yiqing Liu, Zihao Wang, Hantao Yao et al. — [Shared Prefixes, Better Credit: Adaptive Routing for Multi-Agent Reasoning](http://arxiv.org/abs/2608.02291v1)
  <details><summary>📄 Abstract</summary>
  Multi-agent reasoning (MAR) improves reasoning reliability through iterative solution exchange and refinement. Existing adaptive MAR methods typically learn routing decisions from query-level labels or trajectory-level returns, but such coarse supervision cannot accurately estimate the state-conditioned utility of individual operators in multi-step collaboration. We propose TreeCredit, a shared-prefix credit assignment framework for efficient adaptive MAR. Its core insight is to estimate operato...
  </details>

- **2026-08-03** — António Pereira Barata — [Do Static Embeddings Add Value to Hybrid Dutch Retrieval?](http://arxiv.org/abs/2608.02112v1)
  <details><summary>📄 Abstract</summary>
  Embedding benchmarks measure standalone model quality, but they do not establish whether a low-cost retriever contributes complementary ranking information once lexical and transformer-based retrieval are already combined. We present a controlled evaluation of this question across Dutch retrieval tasks from the Massive Text Embedding Benchmark for Dutch (MTEB-NL). Weighted reciprocal rank fusion (RRF) combines Best Matching 25 (BM25), Qwen/Qwen3-Embedding-0.6B (Qwen), and two multilingual static...
  </details>

- **2026-08-03** — Vasilisa Usova, Phila Rembold, Ian Yang et al. — [Adaptive Reconstruction of Bosonic Quantum States](http://arxiv.org/abs/2608.02049v1)
  <details><summary>📄 Abstract</summary>
  Bosonic quantum systems provide a hardware-efficient platform for quantum information processing but remain challenging to characterise due to their large Hilbert space and the high measurement cost of state tomography. Existing approaches estimate the fidelity with respect to a single target state, making them unsuitable for applications in which physically equivalent states differ by phase space translations, rotations, or other transformations. Here, we introduce an adaptive reconstruction te...
  </details>

- **2026-08-03** — Xinwei Yu, Yiyang Fu, Mingcheng Fan et al. — [Towards Autonomous Formulaic Alpha Discovery: An Evolutionary Computation Perspective](http://arxiv.org/abs/2608.01789v1)
  <details><summary>📄 Abstract</summary>
  Automated formulaic alpha discovery aims to generate predictive and interpretable trading signals from large symbolic factor spaces. Its effectiveness is constrained by noisy fitness estimates, market nonstationarity, costly backtesting, semantic redundancy, and conflicting practical objectives. Existing studies employ diverse techniques, including genetic programming (GP), evolutionary algorithms (EAs), reinforcement learning (RL), generative flow networks (GFlowNets), Monte Carlo tree search (...
  </details>

- **2026-08-03** — Baicheng Lin, Lingxi Jin, Kyung-Seok Min — [Comparative Validation of GPT-4o-mini and Teacher Mean Scores for Automated Scoring of Music Analysis Responses: Single-Pass Deployment, Repeatability, and Strategy-Specific Bias](http://arxiv.org/abs/2608.01783v1)
  <details><summary>📄 Abstract</summary>
  Scoring open-ended music analysis responses is time-consuming and requires nuanced judgments of harmonic knowledge and formal understanding. This study evaluates the validity and repeatability of GPT-4o-mini for rubric-based scoring of music analysis essays, using teacher mean scores as the benchmark. A dataset of 300 university-level student responses was scored by teachers on four dimensions: Harmony, Form, Reasoning, and Terminology. GPT-4o-mini scored the same responses using three prompting...
  </details>

- **2026-08-03** — Xiaohao Yang, Aohua Tian, Derek Van Berkel et al. — [Can Urban Blight Be Accessed with Vision-language Models: A Case Study in Detroit](http://arxiv.org/abs/2608.01753v1)
  <details><summary>📄 Abstract</summary>
  Addressing urban blight has seen increased focus in the past 15 years. Assessing urban blight is essential for guiding urban planning, targeting rehabilitation, and safeguarding public health, yet traditional residential blight surveys are difficult to maintain at scale due to the labor-intensive cost and long-term cycle. This study introduced a scalable framework for estimating residential blight using open-source large vision-language models on multiple views. Structured prompts guided models ...
  </details>

- **2026-08-03** — Mohamed Basem, Vincent Christlein — [FAU at ImageCLEF 2026 Task on Multimodal Reasoning Robust Candidate Scoring and Concise Multilingual Visual Answering](http://arxiv.org/abs/2608.01664v1)
  <details><summary>📄 Abstract</summary>
  We present our ImageCLEF 2026 Multimodal Reasoning system for the Visual Multiple Choice Question Answering (Visual MCQ) and Visual Open Question Answering (Visual OpenQA) subtasks. The challenge requires reliable reasoning over multilingual educational and scientific images with dense text, diagrams, charts, tables, formulas, and units, while enforcing strict answer formats. Our central finding is that robust output control is as important as model choice. For Visual MCQ, we replace fragile fre...
  </details>

- **2026-08-03** — Huixin Sun, Wangbo Zhao, Fanyue Wei et al. — [Dynamic Resolution Routing for Efficient Egocentric Grounding](http://arxiv.org/abs/2608.01638v1)
  <details><summary>📄 Abstract</summary>
  Egocentric visual grounding requires high-resolution inputs to localize small objects. However, scaling Multimodal Large Language Models to this domain is constrained by the excessive cost of visual token processing. We identify that current efficient strategies based on token reduction are unreliable for selecting object-centric spatial evidence. To overcome this, we propose SmartRes, a framework that performs efficiency optimization in the pixel space via dynamic resolution routing. SmartRes f...
  </details>

- **2026-08-03** — Taeyeong Kim, Ahhyun Kim, TaeHyeon Kim et al. — [Not the Dimension, the Norm: What Matters in Gradient-Free Weight Perturbation of Language Models](http://arxiv.org/abs/2608.01624v1)
  <details><summary>📄 Abstract</summary>
  Adapting a language model to a task no longer requires training all of its weights, and a line of parameter-efficient methods has driven the trainable count from billions down to a handful of scalars. Gradient-free adaptation, which samples random weight perturbations and keeps the ones that score well, has not followed that trajectory and still perturbs every entry of the weight tensor. It is unknown whether that full-weight search is necessary, and more fundamentally which property of a pertur...
  </details>

- **2026-08-02** — Amirkia Rafiei Oskooei, Bora Ilci, Alperen Kayim et al. — [Deep Agentic Search for Repository-Level Code Question Answering: An Empirical Study](http://arxiv.org/abs/2608.01507v1)
  <details><summary>📄 Abstract</summary>
  Code agents spend much of their effort simply locating the right code inside a repository. Two approaches dominate current practice. In Semantic Search, the agent retrieves code blocks from a vector index built from the repository in advance. In Deep Agentic Search (also known as grep-search by subagent), a planning agent delegates the exploration to a separate subagent that works in an isolated context window and returns only a condensed result. The second design, which is considered good conte...
  </details>

- **2026-08-02** — Yuxiang Xiao, Yang Hu, Bin Li et al. — [Understanding Synergistic Interactions among Pathology Foundation Models via Adaptive Fusion](http://arxiv.org/abs/2608.01370v1)
  <details><summary>📄 Abstract</summary>
  Pathology foundation models (PFMs) provide strong tile-level representations via self-supervised pre-training on large-scale pathology images. Yet, PFMs are developed under diverse and often opaque data, architecture, and objective choices, inducing latent representational biases that limit robustness and obscure what each model specialises in. We present AdaFusion, a lightweight adaptive fusion framework that integrates complementary signals from multiple frozen PFMs through (1) low-dimensional...
  </details>

- **2026-08-02** — Jinsong Lin, Zikang Pan, Wanhao Liu et al. — [EndoWAM: A Grounded World-Action Model for Generalizable Endoscopic Navigation](http://arxiv.org/abs/2608.01221v1)
  <details><summary>📄 Abstract</summary>
  Autonomous endoscopic navigation can reduce clinicians' operational burden, yet robust control remains challenging due to tissue deformation, transient occlusions, and rapidly changing viewpoints. Existing learning-based policies typically predict actions from current observations without explicitly modeling future dynamics, limiting their robustness and reliability in safety-critical settings. World Action Models (WAMs) offer a promising alternative by coupling predictive visual dynamics with a...
  </details>

- **2026-08-02** — Yinhao Bai, Jinming Chen, Yafeng Chen et al. — [JoyAI-Talker: Full-Duplex Speech Interactive Large Model Built for Empathetic Voice Agents](http://arxiv.org/abs/2608.01119v1)
  <details><summary>📄 Abstract</summary>
  We present JoyAI-Talker, a full-duplex speech dialogue system that delivers robust foundation model capabilities while empowering empathetic interaction and voice agent intelligence. JoyAI-Talker adopts a modular Thinker-Talker architecture and further implements a unified speech-text joint training pipeline to mitigate the common "cognitive degradation" bottleneck, thereby largely preserving the model's core textual reasoning, STEM, and logical capabilities while extending them to speech-based ...
  </details>

- **2026-08-02** — Xueying Zhao, Lee Mai, Balaji Anandganesh — [Retrieval Augmented Biomedical Question Answering with Weak Question Recovery and Neural Reranking for BioASQ Task 14b](http://arxiv.org/abs/2608.01468v1)
  <details><summary>📄 Abstract</summary>
  This work presents DS@GT ARC BioASQ team's work for a biomedical question answering pipeline, integrating multi-source query expansion, neural reranking, retrieval refinement, and OpenBioLLM-assisted answer generation. The system combines PubMed retrieval with fine-tuned MiniLM-based semantic reranking, Reciprocal Rank Fusion (RRF), and feature-based relevance scoring to improve document ranking quality. To address challenging queries with weak retrieval performance, we introduce a conditional w...
  </details>

- **2026-08-02** — Ziyan Xiao, Yinghao Zhu, Wenting Zhang et al. — [LongChart VQA: A Comprehensive Benchmark for MLLMs with Complex Multi-Chart Reasoning](http://arxiv.org/abs/2608.01328v1)
  <details><summary>📄 Abstract</summary>
  Multimodal large language models (MLLMs) are rapidly evolving with expanded context windows and stronger reasoning capabilities, enabling multi-chart understanding and multi-step inference. These abilities are increasingly important as MLLMs are adopted in complex agentic tasks. However, existing benchmarks largely emphasize single-chart perception, while simple chart-to-chart connections are insufficient to evaluate these capabilities. To capture multi-chart complexity while ensuring consistenc...
  </details>

- **2026-08-02** — Zi-Hao Ding, Ze-Feng Gao, Xiang-Hua Kong et al. — [Twist-induced magnetic topological phase transition in stacked altermagnetic CrO](http://arxiv.org/abs/2608.01235v1)
  <details><summary>📄 Abstract</summary>
  Interlayer twisting offers a geometric route to controlling electronic states, but whether it can simultaneously reconstruct magnetic symmetry and band topology remains unclear. Here, based on symmetry analysis and first-principles calculations, we show that commensurate twisting drives magnetic topological phase transitions in stacked bilayer CrO. In particular, it transforms an antiferromagnetic Dirac semimetal into either a $d$-wave altermagnetic bipolarized Weyl semimetal or an unconventiona...
  </details>

- **2026-08-02** — Tianyun Ji, Zhenya Huang, Jiayu Liu et al. — [Learning What to Remember and What to Internalize in LLM Self-Evolution via Adaptive Memory-Parameter Coordination](http://arxiv.org/abs/2608.01234v1)
  <details><summary>📄 Abstract</summary>
  Large language model agents increasingly operate in dynamic environments where tool interfaces, APIs, and user requirements change after deployment. Existing self-evolution methods mainly follow two paradigms: harness-based approaches, which externalize feedback into editable memories or skills for rapid adaptation, and parameter-based approaches, which internalize experience into model parameters for deeper capability improvement. However, using either mechanism alone creates a trade-off betwee...
  </details>

- **2026-08-02** — Ahmed Baha Ben Jmaa, Faten Chaieb, Anna Fabijańska — [Fruit-HSNet: A Machine Learning Approach for Hyperspectral Image-Based Fruit Ripeness Prediction](http://arxiv.org/abs/2608.01202v1)
  <details><summary>📄 Abstract</summary>
  Fruit ripeness prediction (FRP) is a classification-based agricultural computer vision task that has attracted much attention, thanks to its wide-ranging advantages in agriculture field for both pre-harvest and post-harvest management. Accurate and timely FRP can be achieved using machine/deep learning-based hyperspectral image classification techniques. However, challenges including the limited availability of labeled data and the lack of robust methods generalizable to various hyperspectral ca...
  </details>

- **2026-08-02** — Xidong Yang, Xingyi Zhang, Wenhao Li et al. — [PATH-Bench: Path-Dependent Evaluation of Lifelong Agents](http://arxiv.org/abs/2608.01149v1)
  <details><summary>📄 Abstract</summary>
  Lifelong LLM agents increasingly adapt through external learning states that store past interactions as retrievable memories or reusable skills, yet existing benchmarks rarely account for how the path of accumulated experience shapes what agents transfer and retain. In this work, we establish PATH-Bench, a benchmark for path-dependent evaluation of lifelong agents. PATH-Bench estimates directed task relationships via multi-model in-context learning, constructs probe-centered sequences with contr...
  </details>

- **2026-08-02** — Tianyi Zhang, Ziyang Gong, Zhenjie Yang et al. — [OC-VLA++: Monocular Geometry-Guided Cross-View Consistency for Viewpoint-Robust Robotic Manipulation](http://arxiv.org/abs/2608.01066v1)
  <details><summary>📄 Abstract</summary>
  We propose OC-VLA++, an extension of OC-VLA for viewpoint generalization under limited camera coverage. While OC-VLA grounds robot actions in the camera coordinate system to align action supervision with visual observations, camera-space grounding alone can still overfit to the few viewpoints observed during training. OC-VLA++ addresses this limitation by introducing geometry-guided paired-view supervision and an explicit cross-view action-equivariance objective. Given paired observations of the...
  </details>

- **2026-08-02** — Jingyu Sun, Yuyang Xue, Mingyang Li et al. — [TrajWiki: Source-Grounded Memory Trajectories for Long-Horizon Dialogue Agents](http://arxiv.org/abs/2608.00967v1)
  <details><summary>📄 Abstract</summary>
  Large language model agents have shown strong capabilities in generating coherent and contextually appropriate responses, yet robust long-horizon dialogue remains limited by the lack of external memory that is traceable, updatable, and diagnostically transparent. Existing memory-augmented agents often store memories as isolated records or overwritable states, making it difficult to preserve how information originates, evolves, conflicts, or becomes obsolete over time. We propose TrajWiki, a traj...
  </details>

- **2026-08-02** — Jibao Yuan, Yuhui Zhao, Yinzhen Lv et al. — [GraRe: Grasp Candidate Re-Ranking for Frozen 6-DoF Grasp Detectors](http://arxiv.org/abs/2608.00946v1)
  <details><summary>📄 Abstract</summary>
  Existing 6-DoF grasp detectors typically rank grasp candidates by detector confidence. However, our analysis on GraspNet-1Billion shows that detector confidence is often poorly aligned with grasp quality, causing successful grasp candidates to be ranked too low during execution. Motivated by this observation, we formulate grasp candidate re-ranking as a separate task for frozen detectors, aiming to improve candidate ordering without changing the detector or its grasp candidates. We propose GraRe...
  </details>

- **2026-08-02** — Juan Li, Wei Cai, Yan Bai — [Neuro-Symbolic Participation Governance for Verifiable AI Agents in Open Digital Twin Ecosystems](http://arxiv.org/abs/2608.00937v1)
  <details><summary>📄 Abstract</summary>
  Autonomous AI agents, increasingly empowered by large language models, are becoming important components of human-machine systems for high-stakes decision support in digital twin ecosystems. However, existing multi-agent systems often lack robust verification for identity, capability, and policy compliance, especially in decentralized environments spanning multiple institutions. This paper proposes a neuro-symbolic decentralized governance framework for verifiable agents in collaborative digital...
  </details>

- **2026-08-02** — Mehrdad Ghassabi, Hamidreza Baradaran Kashani, Pedram Rostami et al. — [Gaokerena: A Small Persian Medical Language Model Family](http://arxiv.org/abs/2608.00932v1)
  <details><summary>📄 Abstract</summary>
  The integration of artificial intelligence into medical question-answering systems has advanced rapidly; however, research remains predominantly focused on English, leaving low resource languages like Persian significantly underserved. To address this gap, this paper introduces Gaokerena, a novel family of compact Persian medical language models optimized for deployment on consumer grade hardware. As a foundational step toward localized digital healthcare, we first present Gaokerena-V, developed...
  </details>

- **2026-08-02** — Zhuang Xiong, Guohao Zhang, Chen Zhang et al. — [Look Up and Look Back: Hidden Attention and Latent Orientation in a Frozen Foundation Model for Panoramic SLAM](http://arxiv.org/abs/2608.00925v1)
  <details><summary>📄 Abstract</summary>
  Monocular panoramic SLAM benefits from substantial visual overlap under large camera rotations, yet remains prone to errors caused by camera tilt, scale drift, and false loop closures. We show that a frozen panoramic geometry foundation model provides useful internal cues beyond its explicit geometric outputs: intermediate tokens encode gravity in the camera frame, while cross-view attention provides a compatibility cue for potential revisits. Building on these cues, we present HALO-SLAM. A grav...
  </details>

- **2026-08-02** — Kapil Wanaskar, Gaytri Jena, Aman Chadha et al. — [FactorJEPA: Factorizing Monolithic Futures into Layout-Agent-Interaction Channels for Crowded and Chaotic Global South Urban Worlds](http://arxiv.org/abs/2608.01049v1)
  <details><summary>📄 Abstract</summary>
  World models have attracted significant attention for their ability to capture and predict the structure and dynamics of the physical world. In this emerging landscape, Joint Embedding Predictive Architectures (JEPA) offer a particularly compelling direction.   We study a largely unexplored regime: populous, crowded, and chaotic Global South urban environments, which we call DENSEWORLD. Unlike the lower-density, lane-structured settings that dominate existing evaluations, these scenes exhibit so...
  </details>

- **2026-08-02** — Hanyu Su, Carlota Julbe i Juanola, Yibo Hu — [Subtype Robustness Is Not Just Accuracy: Calibration Under Unseen Subtype Shift](http://arxiv.org/abs/2608.00928v1)
  <details><summary>📄 Abstract</summary>
  Subtype robustness asks whether a model keeps the correct coarse prediction when test examples come from fine-grained subtypes absent from training but still inside a known coarse category. Prior work studies this almost entirely through accuracy. We ask whether the model also stays calibrated. We present the first systematic study of the question across ImageNet, BREEDS, iNaturalist and CIFAR-100 with five architectures. Calibration breaks down on unseen subtypes, where accuracy drops while con...
  </details>

- **2026-08-02** — Yujian Liu, Jiabao Ji, Li An et al. — [Practical Online KV Cache Compaction for LLM Agents: An Empirical Study](http://arxiv.org/abs/2608.00902v1)
  <details><summary>📄 Abstract</summary>
  LLM agents accumulate long trajectories of reasoning steps, tool calls, and environment feedback, making the KV cache a major inference bottleneck. KV cache compaction can reduce this cost, but most prior methods assume a static context where future queries are known or can be approximated offline. Agents instead require online compaction: new information must be compressed before future relevance is known, using proxy queries cheap enough for the inference path. We study online compaction acros...
  </details>

- **2026-08-01** — Maksym Nechepurenko — [Axient: Debt-Free Finality for Leveraged Binary Event Markets](http://arxiv.org/abs/2608.00631v1)
  <details><summary>📄 Abstract</summary>
  Leveraged event positions combine a repayable loan with an outcome claim that may become non-tradable before oracle payout is final. This paper specifies Axient, a physically backed margin layer for binary event markets that separates leverage maturity from claim maturity and makes the hard-flat decision under explicit execution uncertainty. The model distinguishes quoted book proceeds, matched proceeds, settled proceeds, and redemption. At decision time, the protocol selects the smallest sale w...
  </details>

- **2026-08-01** — David A. Naumann — [Assuming You Knew: Fixing an Epistemic Semantics for Flow Policies Using Agentic AI](http://arxiv.org/abs/2608.00882v1)
  <details><summary>📄 Abstract</summary>
  Many high-level security requirements are about the allowed flow of information in programs and are difficult to make precise because they involve selective downgrading. Notions from epistemic logic have emerged as a good approach to policy semantics but a robust general framework remains elusive. A paper appearing in CSF 2018, entitled ``Assuming You Know: Epistemic Semantics of Relational Annotations for Expressive Flow Policies'', attempted to provide a unifying framework---but the formalizat...
  </details>

- **2026-08-01** — William Caban — [Measurement Without Validity: The Compounding Reliability Problem in Agentic AI Evaluation](http://arxiv.org/abs/2608.00794v1)
  <details><summary>📄 Abstract</summary>
  Agentic AI systems are evaluated using automated benchmarks whose scores justify deployment decisions, safety certifications, and regulatory compliance claims. We present an empirical analysis demonstrating that these scores are systematically less trustworthy than current practice acknowledges.   The problem operates at three compounding layers. First, tasks are increasingly generated by language models: audits of ten popular benchmarks found validity flaws in seven and reporting gaps in all te...
  </details>

- **2026-08-01** — Jiale Zhao, Zimu Chen, Sirui Mao et al. — [DGA$_2$D: Directed Graph-Guided Automated Algorithm Design with Large Language Models](http://arxiv.org/abs/2608.00700v1)
  <details><summary>📄 Abstract</summary>
  The rapid development of Large Language Models (LLMs) has opened new avenues for Automated Heuristic Design (AHD) for solving NP-hard combinatorial optimization problems (COPs). However, existing LLM-driven AHD methods are largely confined to rigid solver templates, relegating the search process to isolated module tuning. Transitioning to fully autonomous, system-level algorithm design is essential but fraught with low reliability of generated operators, extremely large search spaces, and ineffe...
  </details>

- **2026-08-01** — Ahmad Sarlak, Hao Wang, Rahul Amin et al. — [LLM-Assisted Coalition Formation for Cooperative Perception in Autonomous Driving](http://arxiv.org/abs/2608.00690v1)
  <details><summary>📄 Abstract</summary>
  Cooperative perception (CP) enables connected autonomous vehicles (CAVs) to share complementary observations for safer navigation, but practical deployment is limited by bandwidth constraints, unreliable links, and redundant information exchange. Existing CP methods often assume predefined participants and merely focus on collective perception. Likewise, recent LLM-based cooperative driving frameworks facilitate multi-vehicle reasoning but do not regulate participation criteria to select more be...
  </details>

- **2026-08-01** — Rodrigo Pato Nogueira, Marco Vieira, João R. Campos — [Unreliable in Practice? A Comprehensive Study of Errors in LLM-Generated Code](http://arxiv.org/abs/2608.00661v1)
  <details><summary>📄 Abstract</summary>
  Large Language Models (LLMs) are being widely used for coding, with reports indicating that AI now generates an increasing share of production code. Studies show that LLMs can significantly improve developer productivity, yet they still struggle with more complex coding tasks. Just as understanding error modes in human-written code has been central to improving software quality, identifying and characterizing the errors in LLM-generated code is critical for setting realistic expectations and des...
  </details>

- **2026-08-01** — Hao Yuan, Yuxin Wang, Lei Ji et al. — [From Failures to Supervision: DynamicEnvPlan for Robust Long-Horizon Embodied Planning](http://arxiv.org/abs/2608.00613v1)
  <details><summary>📄 Abstract</summary>
  Physical-world interaction is inherently dynamic, as environments can evolve during execution, requiring agents to adapt their plans under non-stationary conditions. We study this challenge through long-horizon embodied planning under environment deviations and execution uncertainty. Existing embodied-task benchmarks can expose such failures, but these failures are usually treated as evaluation outcomes instead of learnable signals for training agents to recover. In this work, we introduce Dynam...
  </details>

- **2026-08-01** — An Lanji, Dawei Liu, Jin Li et al. — [DiffuseAgent-MI: Distributionally-Grounded,Tool-Integrated Self-Evolving Agents for Faithful Visual Reasoning](http://arxiv.org/abs/2608.00540v1)
  <details><summary>📄 Abstract</summary>
  Tool-integrated vision-language agents have made remarkable progress on compositional and multi-step visual reasoning. Yet their outputs frequently exhibit unfaithfulness: the stated reasoning path diverges from the computation that actually produced the answer, undermining reliability in safety-critical applications. We present DiffuseAgent-MI, a self-evolving agent whose perceptual grounding is governed by a KL-minimal energy model over feature units, providing a distributional view of visual ...
  </details>

- **2026-08-01** — Soneya Binta Hossain, Matthew B. Dwyer, Tasfia Tasnim — [Documentation vs. Code Patterns: What Drives LLM-Based Exception Oracle Generation?](http://arxiv.org/abs/2608.00884v1)
  <details><summary>📄 Abstract</summary>
  LLM-based test oracle generation (TOG) methods report high accuracy on exception oracle generation, but it remains unclear what evidence drives these predictions. In particular, do models use explicit exceptional-behavior documentation such as Javadoc @throws clauses, or do they rely on recurring patterns in tests, code, and documentation?   We investigate this question through a large-scale intervention-based study of three TOG systems spanning classifier-based and generative architectures and ...
  </details>

- **2026-08-01** — Xuechen Li — [GeoArbiter: Verifiability-Guided Grounding for Remote-Sensing Multimodal LLMs](http://arxiv.org/abs/2608.00877v1)
  <details><summary>📄 Abstract</summary>
  Remote-sensing multimodal large language models (MLLMs) often assert facts that imagery cannot establish, such as a facility's identity or function. Coordinate-keyed geographic retrieval can supply this missing knowledge, improving fMoW land-use accuracy by 12.06--17.19 points across three open MLLMs. However, retrieved records can also contradict visible evidence, and we find that models frequently follow the records even when the image is decisive. We argue that source trust should therefore d...
  </details>

- **2026-08-01** — Yifei Yuan, Jakob Wolf, Ghaith Androwis et al. — [Staged Multi-Agent Training (SMAT) for Hip Exoskeletons: Metabolic and Biomechanical Validation of a Simulation-Trained Co-Adaptive Controller](http://arxiv.org/abs/2608.00715v1)
  <details><summary>📄 Abstract</summary>
  Learning-based controllers can deliver exoskeleton assistance after training entirely in physics-based simulation, yet few controllers that address human-device co-adaptation have been validated on real users by whole-body metabolic measurement, the standard benchmark for assistive walking. Co-adaptation is challenging: as the device alters joint dynamics, the wearer reorganizes neuromuscular coordination, producing a non-stationary learning problem. Staged Multi-Agent Training (SMAT), a four-st...
  </details>

- **2026-08-01** — Meftun Akarsu, Burak Özdemir, Doğancan Büyükçolak et al. — [A Triple-Robustness Analysis of Retrieval-Augmented Generation for Multi-Hop Requirements Traceability](http://arxiv.org/abs/2608.00705v1)
  <details><summary>📄 Abstract</summary>
  Reported verdicts on GraphRAG versus vector RAG disagree, and the evidence is typically tied to a single corpus, embedder, and judge -- and, we show, to where citation quality is measured. We present a triple-robustness analysis that holds a five-pipeline architecture matrix fixed and varies embedder (local e5-small vs. Azure text-embedding-3-small), corpus (DO-178C typed-edge requirements vs. Wikipedia paragraph chains via MuSiQue), and judge (paired GPT-5.4 x GPT-4.1 on both corpora), over 2x4...
  </details>

- **2026-08-01** — Yuzhi Wang, Rongjun Ye, Shengyuan Chen et al. — [Slides2MindMap: Reconstructing Cognitively Efficient Knowledge Hierarchies from Lecture Slides](http://arxiv.org/abs/2608.00610v1)
  <details><summary>📄 Abstract</summary>
  Generating mind maps from lecture slides can help learners efficiently assimilate fragmented knowledge, promising substantial benefits for intelligent education. However, dedicated automatic generation and evaluation frameworks remain underexplored and challenging, requiring a global-local knowledge focus balance and handling large-scale, heterogeneous slides. We formulate the Slides2MindMap task, which aims to reconstruct cognitively efficient knowledge hierarchies from a course's slide deck co...
  </details>

- **2026-08-01** — Zhuoyi Peng, Yi Yang — [Agentic Graph Token Reasoning](http://arxiv.org/abs/2608.00542v1)
  <details><summary>📄 Abstract</summary>
  Graphs model relational data throughout science and industry, from citation networks to product co-purchase graphs. Because the nodes of many such graphs carry rich text, a growing line of work applies large language models (LLMs) to graph analysis. The most graph-native of these methods use graph tokens: a graph encoder compresses a graph view, such as a node, its k-hop neighbourhood, or a cluster, into a short block of continuous tokens that jointly encodes node attributes and topology and is ...
  </details>

- **2026-08-01** — Wenjie Xiao, Hui Bai, Junhao Chen — [SDDMO-Bench: A Benchmark Suite for Streaming Data-Driven Dynamic Multi-Objective Optimization](http://arxiv.org/abs/2608.00474v1)
  <details><summary>📄 Abstract</summary>
  Streaming data-driven dynamic multi-objective optimization requires algorithms to track time-varying Pareto fronts using only sequential observations under concept drift. However, systematic evaluation remains difficult because real-world problems usually lack ground-truth optima, drift annotations, and controllable conditions, while existing benchmarks provide limited support for standardized comparison. This paper proposes SDDMO-Bench, a benchmark suite that transforms classical dynamic multi-...
  </details>

- **2026-08-01** — Kaho Li, Pengyu Zeng, Yuqin Dai et al. — [CrossProjection: Geometric Grounding Beyond Viewpoint Change in Architectural Drawings](http://arxiv.org/abs/2608.00473v1)
  <details><summary>📄 Abstract</summary>
  Architectural drawings violate the usual assumption behind multi-view reasoning: plans and sections are cuts, while elevations are facade projections, so corresponding components change appearance in ways camera motion cannot explain. We introduce CrossProjection, an anchor-grounded diagnostic of whether vision-language models preserve component identity and externalize geometry across heterogeneous architectural views. It evaluates Matching, Registration, and Geometric Grounding through categor...
  </details>

- **2026-08-01** — Mingze Ma, Hemanth Saratchandran, Cameron Gordon et al. — [Mask-Based Priors Are More Persistent than Query-Key Initializations](http://arxiv.org/abs/2608.00418v1)
  <details><summary>📄 Abstract</summary>
  Transformers do not merely lack data on some Boolean extrapolation tasks; they generalize in a systematically wrong way. Recent work on generalization on the unseen has shown that, despite fitting the observed domain, Transformers often extrapolate according to a simpler minimum-degree interpolator rather than the true target function. These Boolean tasks are not practical applications, but controlled stress tests for understanding Transformer inductive bias. We ask whether this failure mode can...
  </details>

- **2026-07-31** — Jim Zhao, Sohir Maskey, Koen Oostermeijer et al. — [Studying quantization trade-offs for efficient inference deployment in machine translation](http://arxiv.org/abs/2607.29397v1)
  <details><summary>📄 Abstract</summary>
  Deploying large language models in realistic server environments poses challenges, as the system needs to provide high-quality responses with low latency. Quantization is a common approach to reduce the memory footprint and improve inference efficiency, yet its impact on latency and throughput is rarely evaluated under controlled, orchestration-level workloads. In this work we study the quantization trade-offs of two translation model families, EuroLLM \citep{martins2025eurollm} and Hy-MT2 \cite...
  </details>

- **2026-07-31** — Wenzhuo Sun, Mingjian Liang, Richard Attfield et al. — [CALM-AH: An ABAW11-Calibrated Multimodal Ensemble with Reliability-Gated Multi-Expert Consensus for Video-Level Ambivalence and Hesitancy Recognition](http://arxiv.org/abs/2607.29310v1)
  <details><summary>📄 Abstract</summary>
  Ambivalence and hesitancy (A/H) are subtle behavioural states that may be expressed through language, voice, facial activity, and other non-verbal cues. The ABAW11 A/H Video Recognition Challenge asks systems to assign a binary A/H label to each naturalistic interview video. Performance is measured using Macro-F1 so that recognition of both A/H and No-A/H samples receives equal importance. We present CALM-AH, a multimodal ensemble that combines textual, acoustic, visual, and derived behavioural-...
  </details>

- **2026-07-31** — Yongshi Ye, Biao Fu, Chongxuan Huang et al. — [Translation with Thought: Difficulty-Adaptive Reasoning via Reinforcement Learning for Multi-Domain Machine Translation](http://arxiv.org/abs/2607.29287v1)
  <details><summary>📄 Abstract</summary>
  Multi-domain machine translation (MDMT) poses a unique challenge due to varying levels of linguistic complexity across domains. Inspired by human translators' ability to adapt reasoning effort based on difficulty, we propose TwT (Translation with Thought), a resource-rational framework that learns to modulate inference between intuitive and deliberate reasoning. TwT is trained in two stages: (1) supervised fine-tuning on difficulty-aware long chain-of-thought traces distilled from DeepSeek-R1 an...
  </details>

- **2026-07-31** — Qingjian Lin, Yuxin Li, Haoyang Zhang et al. — [ParaASR: Multi-Token Prediction for Fast and Long-Context LLM-Based Speech Recognition](http://arxiv.org/abs/2607.29279v1)
  <details><summary>📄 Abstract</summary>
  Audio-encoder-LLM-decoder architectures have become the dominant paradigm for modern automatic speech recognition (ASR), improving transcription quality through large-scale language modeling. However, the cost of autoregressive decoding scales with decoder size, creating a fundamental trade-off between recognition quality and serving latency. We argue this trade-off is not inherent: unlike open-ended text generation, ASR outputs are strongly anchored to the input speech signal, providing a natur...
  </details>

- **2026-07-31** — Qian Wang, Longrui Chen, Peiran Sun et al. — [RayViT: Ray-Conditioned Visual Representations for Viewpoint-Robust Imitation Learning](http://arxiv.org/abs/2607.29622v1)
  <details><summary>📄 Abstract</summary>
  Visual imitation learning enables robots to acquire visuomotor skills directly from images, yet RGB observations lack explicit geometric cues, making learned policies brittle to camera perturbations. To address this, we propose \textbf{Ray-conditioned Vision Transformer Encoder (RayViT)}, a lightweight architecture that injects camera geometry into pretrained ViT backbones. RayViT represents camera geometry as a Plücker ray map, patchifies it into ray features, and uses gated cross-attention to ...
  </details>

- **2026-07-31** — Sarah Koller, Humberto Reyes-González — [The fundamental limit of jet tagging: Beyond top jets](http://arxiv.org/abs/2607.29508v1)
  <details><summary>📄 Abstract</summary>
  Jet tagging, i.e. determining the origin of high-energy hadronic jets, is a key challenge in particle physics. Machine-learning-based taggers have achieved remarkable progress, raising the question of how close current methods are to the theoretical limit of performance. Previous work addressed this question for boosted top-quark jets using transformer-based generative models that provide realistic synthetic jet data with known probability density functions. This enables a direct comparison betw...
  </details>

- **2026-07-31** — Xiaotian Zhang, Lai Shun Chan, Yue Shang et al. — [The Grokked Illusion: True Equilibrium Mitigates Catastrophic Forgetting](http://arxiv.org/abs/2607.29503v1)
  <details><summary>📄 Abstract</summary>
  While neural networks are typically evaluated by their training and test performance, these metrics do not reveal how robust a learned representation is. Recent studies have shown that solutions occupying larger volumes in parameter space, as quantified by Boltzmann entropy, often exhibit superior generalizability compared to those reached by conventional optimization, a phenomenon known as the high entropy advantage. Here we ask whether this advantage persists beyond generalization. Specificall...
  </details>

- **2026-07-31** — Yu Sun, Yuan Chang, Xiaohou Shi et al. — [TFGformer: Multivariate Time Series Forecasting via Time-Frequency Graph Learning and Covariate Fusion](http://arxiv.org/abs/2607.29459v1)
  <details><summary>📄 Abstract</summary>
  Large-scale multivariate time series from heterogeneous IoT sensors demand accurate long-term forecasting for resource scheduling and predictive maintenance. While recent time series foundation models exhibit strong generalization, they rely on static parametric knowledge and lack dynamic access to external historical patterns during inference. Retrieval-Augmented Generation (RAG) offers a potential remedy, yet its application to time series forecasting is challenged by magnitude variations acro...
  </details>

- **2026-07-31** — Smriti Joshi, Apostolia Tsirikoglou, Daniel M. Lang et al. — [Dense Temporal Contrast Synthesis via Conditioned Latent Transport](http://arxiv.org/abs/2607.29394v1)
  <details><summary>📄 Abstract</summary>
  Dynamic contrast-enhanced magnetic resonance imaging (DCE-MRI) is essential for breast cancer management, but reliance on gadolinium-based contrast agents (GBCAs) restricts use in contraindicated populations, prolongs scan protocols, and presents environmental toxicity concerns. Contrast synthesis offers a non-invasive alternative; however, existing approaches struggle to balance spatial realism with temporal continuity, suffer from slow iterative sampling, underutilize structural priors, and la...
  </details>

- **2026-07-31** — Satoshi Takada, Shintaro Hokada — [Revisiting Stress Analysis in a Three-Dimensional Elastic Hollow Sphere under Uniaxial Compression via the Inverse Laplace Transform Expressions within an Elastodynamic Framework](http://arxiv.org/abs/2607.29286v1)
  <details><summary>📄 Abstract</summary>
  The stress analysis of a three-dimensional elastic hollow sphere subjected to uniaxial compression is revisited, employing an elastodynamic framework. Through the application of the Laplace transform, the scalar and vector potentials of displacement are expanded, facilitating a detailed exploration of the system's mechanical behavior. The static solutions for displacement and stress distributions are derived in the long-time limit, which reveal key insights into the response of the elastic hollo...
  </details>

- **2026-07-30** — Xiangyu Yin, Jiaxu Liu, Zhen Chen et al. — [Crossing the Margin Cliff: Toward Relearn-Robust LLM Unlearning via Margin Calibration](http://arxiv.org/abs/2607.27836v1)
  <details><summary>📄 Abstract</summary>
  Large language model unlearning is consistently fragile under relearn attacks. On TOFU, fine-tuning on twenty forget examples substantially recovers held-out forget-set ROUGE for every method we evaluate, and we trace this fragility to optimization geometry. The per-token answer margin of fourteen post-hoc methods spanning gradient, preference, and distillation families converges into a narrow band above the retain reference in 41 of 42 method--size cells, a regularity we call the margin cliff. ...
  </details>

- **2026-07-30** — Minghao Hu, Lannan Luo, Allen Roush et al. — [CoGate: Confidence-Gated Co-Decoding for Secure Code Generation](http://arxiv.org/abs/2607.28529v1)
  <details><summary>📄 Abstract</summary>
  Large language models are widely used for code generation, but they can also produce insecure programs due to patterns learned from their pretraining data. Decoding-time steering has become an important solution to this problem: a small expert model is combined with the target model at each step to generate more secure code, which is referred to as co-decoding. However, the acceptance rule for existing co-decoding approaches does not consider the expert model's confidence. When the security expe...
  </details>

- **2026-07-30** — Jie Ma, Zhike Qiu, Jie Gao et al. — [Capturing Token Tendencies for Training-Free Token Pruning in Multimodal Large Language Models](http://arxiv.org/abs/2607.28341v1)
  <details><summary>📄 Abstract</summary>
  While visual token pruning is essential for efficient Multimodal Large Language Models (MLLMs), existing training-free methods suffer from a critical limitation: they rely on static, instantaneous heuristics to perform irreversible filtering. This approach ignores the hierarchical nature of MLLMs, where token importance often evolves dynamically rather than remaining fixed across layers. Consequently, tokens essential for deep-layer reasoning are often prematurely discarded by shallow-layer esti...
  </details>

- **2026-07-30** — Rong Wu, Daocheng Fu, Licheng Wen et al. — [MemHarness: Memory Is Reconstructed, Not Replayed](http://arxiv.org/abs/2607.28272v1)
  <details><summary>📄 Abstract</summary>
  Retrieving past experiences has become a common strategy to enhance large language model agents. However, most existing memory-augmented agents treat retrieved experiences as static records to be replayed verbatim, injecting them into the context regardless of whether they align with the agent's current situation. This ``replay'' paradigm ignores the gap between the abstract, general nature of stored experience and the concrete, ever-changing states encountered at decision time, frequently causi...
  </details>

- **2026-07-30** — Samuele Lo Piano, Alessio Lachi, Razi Sheikholeslami et al. — [Improving Discrepancy Measures for Global Sensitivity Analysis](http://arxiv.org/abs/2607.28252v1)
  <details><summary>📄 Abstract</summary>
  Sensitivity analysis methods based on Sobol' total-order indices ($T_i$) are well-founded but computationally demanding. A recently proposed ersatz discrepancy measure offers a cheaper alternative by quantifying deviations from uniformity in input--output scatterplots, yet lacks theoretical grounding and has not been benchmarked against other data-given estimators. We introduce an adjusted ersatz discrepancy that rank-transforms the output before gridding and imputes isolated empty cells via a M...
  </details>

- **2026-07-30** — Sangjin Kim, Yuseon Choi, Jungjun Oh et al. — [LightRot: A Light-Weighted Rotation Scheme and Architecture for Accurate Low-Bit Large Language Model Inference](http://arxiv.org/abs/2607.27704v1)
  <details><summary>📄 Abstract</summary>
  As large language models (LLMs) continue to demonstrate exceptional capabilities across various domains, the challenge of achieving energy-efficient and accurate inference becomes increasingly critical. This work presents LightRot, a lightweight rotation scheme and dedicated hardware accelerator designed for low-bit LLM inference. The proposed architecture integrates Grouped Local Rotation (GLR) and Outlier Direction Aligning (ODA) algorithms with a hierarchical Fast Hadamard Transform (FHT)-bas...
  </details>


### 📂 watermark
*水印与溯源 / Watermarking & Provenance* — 18 papers

- **2026-08-03** — Gaytri Jena, Kapil Wanaskar, Vinija Jain et al. — [Weights or Skills? A Survey of Robot-Learning Techniques: from Action-Predicting Weights to Robots that Write their Own Skills](http://arxiv.org/abs/2608.01851v1)
  <details><summary>📄 Abstract</summary>
  Robot learning is splitting into two bets: policies that bake competence into frozen weights (vision-language-action, or VLA, models), and agents that write and refine their own executable skills as code. This survey organises the field around that axis of weights versus skills. Its central analytical contribution is a deep-dive that arranges code-as-policy methods by their degree of self-improvement, from zero-shot program synthesis, through closed-loop self-repair and persistent skill memory, ...
  </details>

- **2026-08-03** — Wei Wang, Shuanghe Liu, Zhu Zhuo et al. — [CockpitHAT: Dependency-Graph-Driven Hierarchical Attribution for Embodied Multi-Agent Cockpits](http://arxiv.org/abs/2608.01805v1)
  <details><summary>📄 Abstract</summary>
  LLM multi-agent systems suffer from Correctness Collapse, where high task-level accuracy conceals severe process-level failures. This is especially hazardous in safety-critical embodied settings such as automotive cockpits, where lexically correct utterances may trigger dangerous physical operations. Existing attribution methods rely on text traces alone, missing dependency structure, multi-channel evidence, and safety-aware evaluation. We introduce CockpitHAT, a hierarchical attribution framewo...
  </details>

- **2026-08-03** — Gaspard Michel, Hugo Attali, Elena V. Epure — [Fast and Accurate Quotation Attribution in Literary Texts](http://arxiv.org/abs/2608.02359v1)
  <details><summary>📄 Abstract</summary>
  Attributing quotations to their speakers in literary texts remains an open challenge. Standard methods, which independently predict a speaker mention for each quotation, are efficient but still limited in accuracy. In contrast, large language model (LLM) approaches achieve strong performance, but their computational cost limits their use in large-scale literary analysis. We propose an encoder-based efficient formulation that resolves multiple quotation attributions within a shared, large context...
  </details>

- **2026-08-03** — Alejandro Velasco, Nathan Wintersgill, Trevor Stalnaker et al. — [On Automated and Explainable Provenance of AI-Generated Code](http://arxiv.org/abs/2608.02329v1)
  <details><summary>📄 Abstract</summary>
  Generative AI for code generation has transformed software development, but it has also introduced a critical transparency problem: the origins of AI-generated code are opaque to the developers who use it, the organizations that deploy it, and the compliance professionals responsible for ensuring its legal and quality standards. Existing mitigations flag problematic outputs after the fact without explaining why a model produced them or how future generation could be improved. We present a resear...
  </details>

- **2026-08-03** — Runchuan Zhu, Hongbin Lai, Bowen Jiang et al. — [HPFA: Hypergraph-Based Paired Failure Attribution for LLM Reasoning](http://arxiv.org/abs/2608.02026v1)
  <details><summary>📄 Abstract</summary>
  Reflection is a powerful mechanism for LLM reasoning, yet its effectiveness hinges on accurately attributing failures to specific reasoning steps, a capability that current models notably lack. Existing failure attribution methods either require expensive step-by-step counterfactual testing that scales poorly with trajectory length, or treat reasoning traces as flat sequences that ignore the inherent non-linear logical dependencies. We propose a hypergraph-based paired failure attribution (HPFA)...
  </details>

- **2026-08-03** — Kang Liu, Zijing Wang, Yongkang Liu et al. — [TRAM: Enhancing Multimodal Reasoning with Trajectory-Derived Auxiliary Memory](http://arxiv.org/abs/2608.01922v1)
  <details><summary>📄 Abstract</summary>
  Multimodal Large Reasoning Models (MLRMs) have achieved strong performance on tasks requiring visual understanding and multi-step inference. However, as reasoning trajectories grow, models may become less effective at using information established earlier in the context, increasing the risk of reasoning errors. Existing approaches primarily address this problem by sustaining visual grounding throughout reasoning. However, reasoning also transforms visual observations into task-specific relations...
  </details>

- **2026-08-03** — Wonjun Choi, Yerim Kim, Yukyung Lee et al. — [PGMem: Tightly Coupled Persona-Memory Graph for Lifelong Personalized Agents](http://arxiv.org/abs/2608.01708v1)
  <details><summary>📄 Abstract</summary>
  Long-term personalized dialogue agents must track user preferences as their personas evolve. Existing memory systems organize past events well, but store personas as flat profiles detached from the events that justify them. This loose coupling leads to the memory-persona validity gap and the persona-aware retrieval gap. We propose PGMem, a heterogeneous persona-memory graph that connects event and persona nodes through typed provenance and evidence edges, keeping each persona signal traceable to...
  </details>

- **2026-08-03** — Haofei Sun, Lin He — [When Memory Updates but Behavior Does Not: Repairing Implicit Stale Dependencies in Personalized Agent Responses](http://arxiv.org/abs/2608.01619v1)
  <details><summary>📄 Abstract</summary>
  Memory-augmented agents can know that a user's stored state is outdated and still plan around the old value. The STALE benchmark calls this the implicit policy adaptation (IPA) gap. We identify one structural contributor: draft-anchored verification checks what a response says, and in an open-ended response the stale dependency is usually unsaid. StateAuditor therefore audits in the opposite direction, from stored state to draft. An LLM proposes candidate old-to-new transitions from timestamped ...
  </details>

- **2026-08-03** — Mingyang Jiang, Congning Ni, Weixin Liu et al. — [Characterizing Treatment-Context Medication Evidence Across Clinic Notes and Structured EHR Medication History](http://arxiv.org/abs/2608.01570v1)
  <details><summary>📄 Abstract</summary>
  Clinic notes and structured electronic health record (EHR) medication history often contain different medication information. Same-visit disagreement between these sources may result from note-side normalization errors, differences in terminology or timing, or actual differences in documentation. We developed a note-grounded approach that uses large language model (LLM) assisted reference construction, targeted and random human review, deterministic medication normalization, and semantic and tem...
  </details>

- **2026-08-02** — Quang Bui, Shlok Jaiswal, Samuel Paik-Heintz et al. — [Loud or Silent? A Reusable Framework for Per-Modality Failure Analysis in Multimodal Clinical AI](http://arxiv.org/abs/2608.01462v1)
  <details><summary>📄 Abstract</summary>
  Multimodal clinical models are usually judged on accuracy with every modality present, but deployment removes modalities; an echocardiogram is often unavailable where an ECG is routine. Two questions then matter beyond the size of the accuracy loss: which modality was responsible, and whether the model fails loudly or silently once that modality is dropped. The distinction is per-example and modality-level, and is separate from post-hoc feature attribution (e.g. SHAP). Models are replaced often;...
  </details>

- **2026-08-02** — Ziyang Jia, Sirshak Das, Jason Sewall et al. — [NIXT: A NCCL Inspector Exporter Tool for Observability of Collective Communication in Large Model Training](http://arxiv.org/abs/2608.01449v1)
  <details><summary>📄 Abstract</summary>
  As machine learning workloads scale, it is increasingly important to gain more observability into the performance of collective communication to easily identify performance vari- ations and accelerate root cause identification. Towards this goal, the Nvidia Collective Communication Library (NCCL) introduced NCCL Inspector, a profiler plugin that provides lightweight and continuous reporting of NCCL communication performance statistics. However, the large volume of data collected by NCCL Inspecto...
  </details>

- **2026-08-02** — Yongfeng Huang, Yuren Lai, Ruiying Chen et al. — [ACE-GraphRAG: Agentic Context Engineering for Hierarchical GraphRAG](http://arxiv.org/abs/2608.01269v1)
  <details><summary>📄 Abstract</summary>
  Hierarchical Graph Retrieval-Augmented Generation (GraphRAG) organizes corpus knowledge at multiple levels of granularity, yet fixed context construction may fail to translate these multi-resolution representations into a context suited to the current query. We identify this mismatch as the representation--inference gap. We propose Agentic Context Engineering for Hierarchical GraphRAG (ACE-GraphRAG), an inference-time context policy layer that supplements and adapts the initial context for gener...
  </details>

- **2026-08-02** — Kong Wang, Zhongke He, Xiang Chen et al. — [Auditing Semantic Gains in Sequential Recommendation: A Lightweight Recovery Test](http://arxiv.org/abs/2608.01260v1)
  <details><summary>📄 Abstract</summary>
  Recent semantic and generative-retrieval recommenders report substantial improvements over ID-only sequential baselines, but it remains unclear whether these gains arise from language-model reasoning, semantic-ID generation, end-to-end semantic architectures, stronger offline item representations, or complementary semantic and collaborative signals. We investigate this attribution ambiguity through LIME-Rec, a lightweight and auditable recovery test. LIME-Rec combines three independent experts: ...
  </details>

- **2026-08-02** — Taher A. Ghaleb — [AgenTag: Attribution of AI Coding Agents from Behavioral Fingerprints](http://arxiv.org/abs/2608.00966v1)
  <details><summary>📄 Abstract</summary>
  AI coding agents increasingly author pull requests (PRs), often under developers' own accounts, obscuring who actually produced a change. Reliable attribution is important for repository governance, empirical studies of AI-assisted software development, and measuring the impact of AI coding agents. Existing work focuses on closed-set identification of known agents, leaving the practical limits of open-world AI coding agent attribution largely unexplored. In this paper, we present AgenTag, a mult...
  </details>

- **2026-08-01** — Jiaxuan Kang, Siyu Chen, Mingda Li et al. — [LUT: Latent Utility Training for Visual Reasoning](http://arxiv.org/abs/2608.00743v1)
  <details><summary>📄 Abstract</summary>
  Multimodal large language models have advanced visual understanding, yet perception-intensive reasoning remains challenging. Recent latent visual reasoning methods introduce hidden-space computation before answering, but they often rely on costly intermediate supervision, such as bounding boxes, sketches, or interleaved rationales. These strategies focus on how latent states should be shaped, but do not explicitly assess whether the latent is useful for the final answer. We propose LUT, a latent...
  </details>

- **2026-08-01** — Adam Kahirov, Umesh Deshpande, Swaminathan Sundararaman — [CeQe: Grounding Lexical Retrieval in Semantic Evidence](http://arxiv.org/abs/2608.00452v1)
  <details><summary>📄 Abstract</summary>
  Lexical retrieval (BM25) captures exact keyword matches and weights terms by corpus-wide significance, but it is blind to the semantic vocabulary gap: when a relevant document phrases an answer differently from the query, BM25 never retrieves it, and no amount of downstream reranking or fusion can recover a document that was never in the candidate set. We present Cross-Encoder Query Expansion (CE-QE), which reads the per-token relevance attributions of a cross-encoder applied to top semantic sea...
  </details>

- **2026-07-31** — Stanislaw Janik, Michal Byra — [Weight-Space Mixture-of-Experts for Implicit Neural Representation Classification](http://arxiv.org/abs/2607.29463v1)
  <details><summary>📄 Abstract</summary>
  Implicit Neural Representations (INRs) encode signals as the weights of a coordinate-based neural network and have recently been proposed as an alternative domain for downstream learning. While promising, classification directly in weight space remains challenging due to the high dimensionality and complex structure of INR parameters. Furthermore, the way discriminative information is distributed across INR weights remains poorly understood. We propose a hierarchical Mixture-of-Experts (HMoE) Tr...
  </details>

- **2026-07-30** — Chunpeng Wang, Yanan Shi, Zhiqiu Xia et al. — [SPFM-Net: Semantic-Prior-Guided Frequency-Constrained Mamba for Invisible Watermark Attack](http://arxiv.org/abs/2607.27811v1)
  <details><summary>📄 Abstract</summary>
  Existing watermark attacks typically rely on predefined signal-processing operations or locally constrained restoration networks, making it difficult to capture the long-range dependencies of globally distributed watermark signals and resulting in an unfavorable trade-off between removal effectiveness and visual fidelity. In this paper, we propose SPFM-Net, a semantic-prior-guided and frequency-constrained Mamba framework for invisible watermark attack. SPFM-Net first employs high-ratio masking ...
  </details>


### 📂 unlearning
*机器遗忘 / Machine Unlearning* — 2 papers

- **2026-08-03** — Junxiang You, Junkai Chen, Yuhao He et al. — [Exploring and Bridging Knowledge Holes in Unlearned Multimodal Large Language Models](http://arxiv.org/abs/2608.01849v1)
  <details><summary>📄 Abstract</summary>
  Machine unlearning offers a promising approach to remove unsafe content from Multimodal Large Language Models (MLLMs), yet ensuring the precision of unlearning remains a persistent challenge. One reason is that current MLLM unlearning evaluation paradigms suffer from a critical blind spot: they assess model utility through benchmarks whose representations are distant from the forget set, failing to capture knowledge holes---severe degradation on benign adjacent inputs. To probe knowledge holes i...
  </details>

- **2026-08-03** — Junhao Cai, Dohun Kim, Sung Il Choi et al. — [SCOPE: Entanglement Frontier Escape for Source-Free Class Unlearning](http://arxiv.org/abs/2608.02058v1)
  <details><summary>📄 Abstract</summary>
  Source-free class unlearning erases whole classes using only the forget data, judged at the representation level, where features can leak a class the head no longer predicts. Existing feature-space erasers answer with one fixed projection, yet forget and retain classes share a representation, so deleting one disturbs the other where they overlap. We prove this tension is a frontier. Every fixed projection that deletes pays a retain cost of at least the retain-readout energy along the forget-disc...
  </details>


### 📂 agent-safety
*Agent 安全框架 / Agent Safety Frameworks* — 4 papers

- **2026-08-02** — Ruiyang Zhang — [Why Formal Monitors Fail: Attack Distribution Entropy as a Coverage Bound for LTL-Based LLM Agent Safety](http://arxiv.org/abs/2608.01388v1)
  <details><summary>📄 Abstract</summary>
  Runtime safety monitors based on Linear Temporal Logic (LTL) and finite automata (FSA) are increasingly deployed to intercept unsafe tool-call sequences in LLM agents. Yet the same monitor achieves 68-75% attack coverage on some model architectures and near-zero on others, with no explanation from capability scores, training data, or prompt design. We provide the missing theory. We prove that the recall of any fixed-invariant FSA monitor is bounded above by the concentration of the attack distri...
  </details>

- **2026-08-02** — Phu Hoa Pham, Duy Minh Dao Sy, Trung Kiet Huynh et al. — [Humans Are More Diverse: Frontier LLMs Show Extreme Policies in Idealised AI Development Races](http://arxiv.org/abs/2608.01193v1)
  <details><summary>📄 Abstract</summary>
  An AI development race creates a multi-agent safety dilemma. Each company can develop slowly and safely, or move faster while taking a risk that may remove its final reward. We use this repeated game to study strategic safety behaviour among large language model (LLM) agents in races with two to five players. However, a valid action does not show that an agent understands the game. We therefore place an audit gate before behavioural interpretation. We first verify the game engine, then test rule...
  </details>

- **2026-08-01** — Zhaoming Yin — [Safety Invariants for Agents Orchestrating Irreversible State Transitions: A Four-Dimensional Formalism Evaluated on Public Ledgers](http://arxiv.org/abs/2608.00783v1)
  <details><summary>📄 Abstract</summary>
  Autonomous agents are increasingly asked to produce irreversible effects on external systems - transferring funds, writing to durable storage, actuating hardware. Existing agent frameworks (ReAct, Reflexion, MCP) optimize task success on benchmarks and give little attention to the safety of irreversible side-effects. We formalize one such setting, movement of value across public ledgers, as state transitions in a four-dimensional space indexed by (wallet, chain, address, protocol), and use that ...
  </details>

- **2026-07-30** — I. Kennedy, T. Kennedy — [Fidelity Is Not Safety: Gently-Compressed LLMs Pass Every Data-Free Quality Guard Yet Invent Procedure Steps in Agentic Execution](http://arxiv.org/abs/2607.28196v1)
  <details><summary>📄 Abstract</summary>
  Practitioners accept a compressed language model once it clears a stack of data-cheap quality guards: perplexity within a small factor of the original, downstream accuracy (for example MMLU) inside a confidence interval, and data-free output-fidelity signals that compare the compressed and original network's internal representations under random probe inputs. This stack has a blind spot. Across three model families, gently-compressed models clear every guard and then invent procedure steps that ...
  </details>


### 📂 survey
*综述与系统化 / Surveys & Systematization* — 5 papers

- **2026-08-03** — Shahin Hossain, Sima Ahmadi, Leqi Li et al. — [Rethinking Generative AI Literacy: An Integrative, Developmental, and Dialectical Framework for K-12 Teacher Education](http://arxiv.org/abs/2608.01705v1)
  <details><summary>📄 Abstract</summary>
  Generative artificial intelligence (GenAI) has entered classrooms faster than teachers have been prepared to use it well, producing a GenAI literacy lag in which technological diffusion outpaces educators' conceptual, pedagogical, and ethical readiness. Established AI literacy frameworks predate the widespread adoption of large language models and, while acknowledging ethics, position it as a discrete competency rather than a constitutive commitment, with equity and agency as supplementary desig...
  </details>

- **2026-08-02** — Muhammad Tukur, Hayatullahi B. Adeyemo, Tao Chen et al. — [From AI Technical Debt to Agentic Technical Debt: A Systematic Mapping of Root Causes and Manifestations in Agentic AI Systems](http://arxiv.org/abs/2608.01001v1)
  <details><summary>📄 Abstract</summary>
  The emergence of Agentic AI systems, characterized by autonomous reasoning, multi-agent collaboration, tool orchestration, adaptive decision-making, and persistent memory, represents a fundamental shift from traditional AI pipelines to dynamic software ecosystems. While AI Technical Debt (AITD) has been widely studied in machine learning and software engineering, existing models assume static, component-level architectures and fail to capture the dynamic and emergent behaviors of agentic environ...
  </details>

- **2026-08-01** — Ethan Dickey, Libra Vento, Peter Kurto et al. — [CodeStylist: Supporting Early Undergraduate Programmers with Course-Aware Code Style Feedback](http://arxiv.org/abs/2608.00839v1)
  <details><summary>📄 Abstract</summary>
  This innovative practice full paper presents CodeStylist, a web application that provides course-standard-aware code style feedback for early undergraduate programming courses. CodeStylist addresses a common instructional gap: students are expected to follow local conventions for naming, formatting, comments, organization, and readability, but feedback on these expectations is often delayed or inconsistent. Unlike generic linters or general-purpose LLM prompts, CodeStylist supports course-specif...
  </details>

- **2026-07-30** — Yanshi Li, Xueru Bai, Shuman Liu et al. — [RepBench: Compiling Benchmarks into Capability Representations for Large Language Models](http://arxiv.org/abs/2607.28008v1)
  <details><summary>📄 Abstract</summary>
  Representation engineering reads and steers capability directions in large language models, yet methods are typically evaluated on paper-specific synthetic data. The resulting measurements are difficult to compare or reproduce and may reflect surface patterns rather than capabilities. We present RepBench, a benchmark-grounded data layer for capability-aligned representation probing. Crawling 13,427 benchmark papers yields a taxonomy of 182 capability clusters in 13 families; harvesting 353 publi...
  </details>

- **2026-07-30** — Shalini Chakraborty, Michael Mittermaier, Judith Michael — [The Case for Vibe Modeling: A Missing Step in AI-Based Trustworthy Software Development](http://arxiv.org/abs/2607.27923v1)
  <details><summary>📄 Abstract</summary>
  Large Language Models (LLMs) are increasingly used to generate software artifacts from natural language prompts. While this enables rapid prototyping and lowers the barrier to software creation, it also introduces challenges related to understanding, validation, traceability, and trust. In this paper, we argue that current AI-based development practices focus too heavily on the direct generation of code and insufficiently on intermediate representations that preserve human intent and support rea...
  </details>


### 📂 other
*其他安全相关 / Other Security-Related* — 165 papers

- **2026-08-03** — Yiran Gao, Tao Li, Kim Hammar — [Agentic Incident Response through Digital Twin-Enhanced Multiscale Planning](http://arxiv.org/abs/2608.02422v1)
  <details><summary>📄 Abstract</summary>
  Incident response is currently managed by security operators using predefined playbooks, resulting in slow, labor-intensive security decision-making processes. Consequently, there is a growing need for automated incident response planning. Decision-theoretic approaches based on control, optimization, and reinforcement learning have been proposed to automate such planning tasks with well-grounded approaches, yet most of which, while guaranteeing strong performance, are limited to abstract models ...
  </details>

- **2026-08-03** — Ting-Jui Chang — [A Spectral Filtering Approach to Regret Analysis of Distributed Online Control for Linear Dynamical Systems](http://arxiv.org/abs/2608.02375v1)
  <details><summary>📄 Abstract</summary>
  This paper studies the distributed online control problem over a network of linear time-invariant (LTI) systems in the presence of adversarial disturbances and time-varying convex costs. The network cost is characterized by the summation of local cost functions, where each local function is sequentially revealed only to the corresponding agent. The goal of each agent is to generate a control sequence, using only local observations and neighbor communication, that competes with the best {\it cent...
  </details>

- **2026-08-03** — Dunjie Lu, Shuai Bai, Tianyi Bai et al. — [Qwen-CUA: Native Computer Use for (almost) Everything](http://arxiv.org/abs/2608.02352v1)
  <details><summary>📄 Abstract</summary>
  Native computer use offers a general interface for agents to operate almost any software available to people, but requires long-horizon state tracking, large-scale interactive experience, and learning from sparse yet verifiable outcomes. We introduce Qwen-CUA, a native computer-use agent with a 397B-A17B Qwen mixture-of-experts backbone. It observes only screenshots and acts through keyboard and mouse events, without DOM trees, accessibility metadata, or task-specific APIs. Its scaffold maintain...
  </details>

- **2026-08-03** — Jingxi Wei — [Trajectories That Segment Themselves: Agent-Declared Boundaries as a Training Unit](http://arxiv.org/abs/2608.02302v1)
  <details><summary>📄 Abstract</summary>
  Long-horizon coding-agent trajectories are poorly matched to the credit units available to train on: a single action has no stable value, an episode label merges productive exploration with abandoned directions, and a fixed window cuts where the logging mechanics fall. We introduce collection-time semantic self-segmentation, in which a declarative contract has the acting agent expose its own boundaries while the trajectory is generated. Instantiated with falsifiable causal hypotheses, successive...
  </details>

- **2026-08-03** — K. Jack Scott, Narun Pat, Veronica Liesaputra — [Divergent large language model predictions from convergent representations in ambiguous word pairs](http://arxiv.org/abs/2608.01816v1)
  <details><summary>📄 Abstract</summary>
  In this work we investigate how decoder-only transformers resolve lexical ambiguity through layer-by-layer analysis of three models spanning three parameter sizes (GPT-2-Small-117M, Llama-3.2-3B, Qwen2.5-32B). For both homonyms and polysemes, we find that representations become maximally distinct in middle layers, then partially reconverge in late layers, while the KL divergence between their next-token predictions reaches its maximum in the final layers. The activation patching experiment provi...
  </details>

- **2026-08-03** — Shuyang Xie, Shuxiao Xie, Feng Zhu et al. — [Coding Agents as Test-Suite Auditors: Finding What Official Suites Miss While Approaching What They Catch](http://arxiv.org/abs/2608.01715v1)
  <details><summary>📄 Abstract</summary>
  Online-judge verdicts and the datasets and benchmarks built on them are treated as ground truth for evaluating and training large language models for code. Yet prior audits have sounded a warning: official suites accept buggy submissions. These audits, however, stop at the warning and offer no practical remedy. Our remedy has two parts: an off-the-shelf coding agent, serving as a test-suite auditor, both builds adversarial test suites to expose what official suites miss and supplies these suites...
  </details>

- **2026-08-03** — Jiajun Liang, Yucheng Liao, Yukang Cao et al. — [AURORA-LM: Autoencoding Unified Representation for Continuous-Latent Diffusion Language Modeling](http://arxiv.org/abs/2608.02602v1)
  <details><summary>📄 Abstract</summary>
  Language remains an outlier in generative modeling: while images, video, and audio are increasingly modeled in continuous latent spaces, text generation still relies predominantly on discrete tokens. Existing continuous language models either inherit embedding spaces not designed for joint generation and decoding, or compress autoencoded latents to ease diffusion, sacrificing token-level fidelity. Instead of simplifying the representation to suit the generative model, we preserve a high-capacity...
  </details>

- **2026-08-03** — Chunhao Cai — [A Response Calculus for Liouville Brownian Motion I: Simple Spectrum, Joint Eigenvalue Densities, and Ward Identities](http://arxiv.org/abs/2608.02459v1)
  <details><summary>📄 Abstract</summary>
  We develop a response calculus for Dirichlet Liouville Brownian motion under Cameron--Martin shifts of the Gaussian free field. On every bounded connected planar domain, without boundary regularity assumptions, we prove throughout the full subcritical range $0<γ<2$ that the generator has almost surely simple spectrum and that every finite vector of ordered eigenvalues has an absolutely continuous law. This resolves the open simple-spectrum problem for Dirichlet Liouville Brownian motion.   The c...
  </details>

- **2026-08-03** — Ambarish Govindarajulu Kaliamurthi, Kaikai Liu — [MoRAL: Sensor-Grounded BEV Reasoning for Compact VLMs toward Edge-Oriented Autonomous Driving](http://arxiv.org/abs/2608.02449v1)
  <details><summary>📄 Abstract</summary>
  Deploying vision-language models (VLMs) for safety-critical spatial reasoning on resource-constrained autonomous driving platforms requires both compact model size and reliable metric grounding. We present MoRAL (Multimodal Reasoning for Autonomous Language Models), a two-stage fine-tuning pipeline that teaches Cosmos-Reason2-2B to first read a physics-encoded Bird's Eye View (BEV) representation and then reason over it for driving decisions. The BEV image encodes LiDAR metric distance as color ...
  </details>

- **2026-08-03** — Jiaming Chen, Guoan Xu, Aoshen Huang et al. — [DF$^3$: World Modeling via Decoder-Free Feature Forecasting in Autonomous Navigation](http://arxiv.org/abs/2608.02428v1)
  <details><summary>📄 Abstract</summary>
  Forecasting future states from video sequences is a critical challenge for autonomous robotic systems and a fundamental objective of world modeling. Prior generative methods operating at the pixel level inevitably overemphasize task-irrelevant details, leading to prohibitive computational overhead. While latent-based approaches attempt to mitigate this by predicting features directly, the persistent reliance on heavy decoders for state-to-task mapping remains a computational bottleneck. In this ...
  </details>

- **2026-08-03** — Hao Shen, Junyu Guo, Tian Cui et al. — [MechGeo: Autoformalizing and Proving Euclidean Geometry in Lean 4](http://arxiv.org/abs/2608.02295v1)
  <details><summary>📄 Abstract</summary>
  We present MechGeo, a Mathlib native agentic framework that jointly addresses faithful autoformalization and certified proof construction for Euclidean geometry. In this framework, GeoFormalizer represents informal problems in GeoIR, deterministically translates them into Lean 4, and iteratively repairs candidate statements using structural diagnostics and semantic evaluation. GeoProver constructs geometric proof plans, derives intermediate lemmas, and selectively algebraizes suitable subgoals t...
  </details>

- **2026-08-03** — Abdul Kalam, Prasenjit Deb, Akitada Sakurai et al. — [Quantum computer-based simulation of Stark many-body localization in a 1D Fermi-Hubbard model](http://arxiv.org/abs/2608.02245v1)
  <details><summary>📄 Abstract</summary>
  Many-body localization (MBL) is a dynamical phenomenon that describes the non-ergodicity of isolated quantum many-body systems. In contrast to thermalization, this phenomenon leads to a long-lived memory of initial states of local systems and slow growth of entanglement. In this work, we study Stark MBL in a 12-qubit correlated fermionic system described by the one-dimensional Fermi-Hubbard model using Hamiltonian simulation on an IBM superconducting qubit quantum computer. To enable such a comp...
  </details>

- **2026-08-03** — Luciano Ciamarone, Dora Motèque, Marco Giordano — [Sounding Canvas: Embedding Algorithms in Networked, Sensorial Sound Art](http://arxiv.org/abs/2608.02219v1)
  <details><summary>📄 Abstract</summary>
  Sounding Canvas turns painting into a touch-responsive multimodal installation by embedding capacitive sensors, real-time decision models, and networking inside the canvas. Touches trigger spatialised sounds that appear to emanate from the painting itself. The work embeds algorithms physically, as sensing and computation concealed behind the artwork; perceptually, through an offline visual-to-sonic mapping that aligns a painting's features with sound descriptors; and performatively, through onli...
  </details>

- **2026-08-03** — Can Wang, Haoran Chen, Haowen Gao et al. — [From Simple QA to Deep Research: A Verifiable Benchmark Constructed through Iterative Task Evolution](http://arxiv.org/abs/2608.02163v1)
  <details><summary>📄 Abstract</summary>
  Deep research benchmarks require expert-level tasks and reliable evaluation grounded in task-specific knowledge. Existing benchmarks rely heavily on expert authoring or pre-existing human-authored materials, while fully automatic construction struggles to ensure consistent and traceable verification. To address this gap, we introduce a verifiable benchmark of 500 deep research tasks spanning 31 topics and 10 major categories, with three query forms designed to probe complementary capabilities re...
  </details>

- **2026-08-03** — Long Qian, Jiaqi Wei, Bingke Zhu et al. — [Messages, Not Tokens: Grounded Coresets for Faithful VLM Compression](http://arxiv.org/abs/2608.02134v1)
  <details><summary>📄 Abstract</summary>
  Modern vision language models (VLMs) turn high-resolution images into long sequences of visual tokens. Every token traverses the language decoder and persists in its prompt KV cache, inflating inference cost and motivating aggressive visual compression. Existing score-based methods assign each token an independent importance score and retain the Top-K. However, text queries consume collective, signed attention messages from the visual population, not isolated patches. Consequently, equally sized...
  </details>

- **2026-08-03** — Shuxiao Xie, Shuyang Xie, Yuan Cao et al. — [One QK Channel, Many Sources: Guarding Low-Precision Attention Collapse](http://arxiv.org/abs/2608.02091v1)
  <details><summary>📄 Abstract</summary>
  A bfloat16 transformer can train normally for many steps and then collapse abruptly. Distinct low-precision errors can trigger the same failure, leaving unclear whether each source needs its own repair or one shared route can be blocked. We isolate a reproduced GPT-2-class collapse to the streaming-softmax accumulator, where fp32 accumulation repairs it, and use the fault as an assay for moving controlled errors across sources. Errors placed outside attention still drive the same query-key (QK) ...
  </details>

- **2026-08-03** — Zitong Xu, Huiyu Duan, Xinyun Zhang et al. — [MIEScore: Human-Aligned Evaluation for Multi-Source Image Editing](http://arxiv.org/abs/2608.02059v1)
  <details><summary>📄 Abstract</summary>
  Recent advances in unified multimodal models have significantly improved text-guided image editing abilities. In particular, models such as Nano-Banana-Pro and GPT-Image-2 demonstrate emerging capabilities in multi-source image editing (MIE), including tasks such as object synthesis, person-background composition, and cross-image style fusion. However, existing benchmarks and image editing assessment (IEQA) methods remain primarily focused on single-image editing tasks and largely overlook the m...
  </details>

- **2026-08-03** — Hongjie Zhou, Shiqin Wang, Haoyang Chen et al. — [RSVideo: Are Your Vision-Language Models Ready for Remote Sensing Videos?](http://arxiv.org/abs/2608.02039v1)
  <details><summary>📄 Abstract</summary>
  Remote-sensing videos enable real-time observation of changes in target attributes, short-term activities, and scene evolution. They record motion, actions, interactions, and scene changes that cannot be captured by isolated images. Existing models primarily target single images or discrete temporal observations spanning a long time range. However, a unified evaluation setting for assessing vision-language models on continuous remote-sensing video understanding remains lacking. We introduce RSVi...
  </details>

- **2026-08-03** — Ruilin Xu, Junyi Li, Pengfei Chen et al. — [TELLER: Non-intrusive Cross-Layer Root-Cause Analysis for LLM Inference](http://arxiv.org/abs/2608.01975v1)
  <details><summary>📄 Abstract</summary>
  Large language model (LLM) inference has evolved from an offline workload into a continuously operated software service, yet root-cause analysis remains difficult because a single request spans the inference engine, Python/C++ backend, host CUDA APIs, GPU kernels, and distributed communication. Existing profilers expose raw timelines, while log-based diagnosis often misses cross-layer execution semantics and request-level structure. We present TELLER, a non-intrusive Trace- and Log-aware LLM inf...
  </details>

- **2026-08-03** — Adam Zahir, Vincent Lefebvre, Mark Angoustures et al. — [D-MUTRA: DLT-based MUTual Remote Attestation for Multi-Agent Systems](http://arxiv.org/abs/2608.01938v1)
  <details><summary>📄 Abstract</summary>
  Multi-agent systems (MAS) comprise autonomous software agents that collaborate to perform complex tasks in critical cyber-physical domains, including multi-robot coordination and the Industrial Internet of Things (IIoT). In such distributed environments, a compromised agent may execute modified software while appearing trustworthy, causing other agents to act on false information and corrupting the mission. Agents must therefore establish and maintain mutual trust throughout operation. Remote at...
  </details>

- **2026-08-03** — Glenn Matlin, Isaac Song, Anthony Wen-Ming Zang et al. — [No One Wins in Nuclear War: A Social Simulation of Military Decision-making](http://arxiv.org/abs/2608.01868v1)
  <details><summary>📄 Abstract</summary>
  WOPR is a social-simulation environment for studying how organizations make high-stakes decisions, built on a deterministic, replay-validated rules engine and using wargames as the vehicle. We instantiate it first with the published card game Nuclear War, traced against its published rules. We start with military decision-making because of its safety implications and because it needs further study, but the design is not specific to it: the decision-point contract that exposes the engine to agent...
  </details>

- **2026-08-03** — Dongwei Sun, Bowen Yao, Yujie Zhang et al. — [EchoChange: A Diffusion Language Model with Dual Pass Remasking for Factual Remote Sensing Disaster Change Captioning](http://arxiv.org/abs/2608.01856v1)
  <details><summary>📄 Abstract</summary>
  Bi-temporal remote-sensing disaster change captioning often needs to identify sparse and spatially localized changes across large pre- and post-event scenes and then translate them into coherent, factual descriptions. However, existing change captioning methods always follow an autoregressive decoding paradigm to generate the change description and thus an early misinterpretation of the changed object, event, or spatial relation becomes an irreversible premise for subsequent text, amplifying vis...
  </details>

- **2026-08-03** — Chunji Lv, Yangguang Wei, Junlin Liu et al. — [PCSD: Persistent Consistency for Self-Distillation in Agentic Reinforcement Learning](http://arxiv.org/abs/2608.01837v1)
  <details><summary>📄 Abstract</summary>
  Large language model agents have shown strong potential in complex interactive tasks, yet their reinforcement learning (RL) is often hindered by sparse rewards, as a long multi-turn trajectory may receive only a single outcome-level signal. On-policy self-distillation (OPSD) provides dense token-level supervision from a privileged teacher, but the teacher may not be reliable at every position. Existing methods commonly rely on isolated token-level discrepancies, which can be sensitive to noise, ...
  </details>

- **2026-08-03** — Priyashree Roy, Sujitha Martin, Mohammad Rostami et al. — [Can You Trust the Confidence? ConfBench for Vision-Language Models on Document Extraction](http://arxiv.org/abs/2608.01792v1)
  <details><summary>📄 Abstract</summary>
  Intelligent document processing (IDP) with vision-language models (VLMs) hinges on confidence scores trustworthy enough to route extractions between automation and human review. Existing document benchmarks are dominated by clean, high-quality samples, leaving low accuracy regions too sparse for calibration assessment. We introduce ConfBench, the first calibration-specific benchmark for key information extraction (KIE), built by applying 20 controlled degradation pipelines to a diverse document ...
  </details>

- **2026-08-03** — Xiang Xia, Cheng Yan, Yiming Zhang et al. — [REFLEX: Rethinking MoE Inference as Refinement-Aware Compute Allocation in Diffusion Language Models](http://arxiv.org/abs/2608.01784v1)
  <details><summary>📄 Abstract</summary>
  Mixture-of-experts (MoE) models increase parameter capacity by activating only a small subset of experts for each token. This conditional-computation paradigm has enabled autoregressive language models to scale model capacity without a proportional increase in per-token computation. In diffusion language models (DLMs), however, each denoising forward jointly revisits all token positions despite their sharply different refinement demands, while the default fixed token-choice routing assigns them ...
  </details>

- **2026-08-03** — Shuntaro Aoki — [Primordial Correlators from a Kaluza-Klein Graviton Continuum](http://arxiv.org/abs/2608.01762v1)
  <details><summary>📄 Abstract</summary>
  Cosmological collider signals are usually discussed for isolated massive particles, whose exchange produces characteristic logarithmic oscillations in primordial correlators. In this work, we study how this signal is modified when the exchanged states form a continuous mass spectrum. We first develop a spectral representation for inflationary correlators mediated by a continuum field. In the soft limit, the non-analytic part of the seed function is expressed as a Fourier--Laplace transform of th...
  </details>

- **2026-08-03** — Siying Li, Ying Ni, Jie Sun et al. — [DecoupleGS: Interactive 3D Gaussian Splatting for End-to-End Autonomous Driving Testing](http://arxiv.org/abs/2608.01761v1)
  <details><summary>📄 Abstract</summary>
  End-to-end (E2E) autonomous driving algorithms require rigorous closed-loop validation in simulation environments offering high visual fidelity, strong interactivity, and real-time performance. Existing approaches, from game engines to static neural rendering, inherently trade off these requirements and struggle with the dynamic scene composition essential for E2E testing. To bridge this gap, we propose a novel decoupled 3D Gaussian Splatting (3DGS) framework tailored for large-scale E2E evaluat...
  </details>

- **2026-08-03** — Hao Ye, Geoffrey Ye Li, Biing-Hwang Juang — [Ten Years of Deep Learning for Wireless Communications: From Learned Blocks to Deployable Wireless Intelligence](http://arxiv.org/abs/2608.01747v1)
  <details><summary>📄 Abstract</summary>
  Over the past decade, deep learning has evolved from a tool for replacing isolated wireless blocks into a broader methodology for developing wireless intelligence. This article traces that trajectory through three shifts: learning wireless functional modules, redesigning and re-normalizing communication goals, and enabling generalization under practical physical constraints. Together, these shifts advance the broader pursuit of communication anytime and anywhere, through any appropriate means. E...
  </details>

- **2026-08-03** — Jianyu Wu, Yizhou Wang, Encheng Su et al. — [DAPD: Dual-Anchored Policy Distillation](http://arxiv.org/abs/2608.01735v1)
  <details><summary>📄 Abstract</summary>
  On-policy (self) distillation (OPSD) is increasingly adopted for language-model post-training. It strengthens the teacher with privileged information but can induce a privilege illusion: the student learns privilege-dependent behavior it cannot reproduce from its inference-time context, yet behaves as if the training-time privileged information remained available, ultimately degrading performance. In this paper, we identify information asymmetry between the privileged teacher and the student at ...
  </details>

- **2026-08-03** — Hai Nguyen, Tung Vu, Cong Tran — [SpatialQuery: Benchmarking Geometry-Grounded Multi-Instance Spatial Reasoning in Vision-Language Models](http://arxiv.org/abs/2608.01709v1)
  <details><summary>📄 Abstract</summary>
  Vision-language models (VLMs) achieve strong semantic understanding but remain unreliable in metric spatial reasoning, particularly when queries require comparing multiple instances of the same object category. We study this problem through the Closest-Instance Distance Query (CIDQ), where a model must identify the nearest visible candidate to a unique reference object and estimate their gravity-aligned floor-plane distance. We introduce SPATIALQUERY, a training- free framework for CIDQ reasonin...
  </details>

- **2026-08-03** — Walter P. Casas, Nelson L. S. da Fonseca, and Carlos A. Astudillo — [LLM-Driven Automated Reward Design for Reinforcement Learning-Based Routing in LEO Satellite Networks](http://arxiv.org/abs/2608.01649v1)
  <details><summary>📄 Abstract</summary>
  Routing in Low Earth Orbit (LEO) satellite networks is challenging due to highly dynamic topologies and spatio-temporal network conditions. Reinforcement Learning (RL) has emerged as a promising approach for adaptive routing; however, its performance critically depends on reward function design, which must balance objectives such as goodput and end-to-end delay. In practice, reward design remains a complex manual process requiring significant domain expertise and extensive trial-and-error. Recen...
  </details>

- **2026-08-03** — Tianle Liu, Youcheng Niu, Jing Zeng et al. — [A Forward-Inverse Dynamic Game Framework for Enhanced Multi-Agent Trajectory Planning](http://arxiv.org/abs/2608.01636v1)
  <details><summary>📄 Abstract</summary>
  This paper studies feedback Nash equilibrium (FBNE) seeking for multi-agent trajectory planning in nonlinear dynamical systems with unknown agents' objectives and state-dependent inter-agent coupling. While dynamic game theory provides a principled framework for such problems, existing approaches typically assume fully rational agents with known objectives or rely on fixed regularization, limiting their ability to capture bounded rationality and spatially varying interaction intensity in safety-...
  </details>

- **2026-08-03** — Zhen Liu, Wanqi Zhou, Shuanghao Bai et al. — [GraphIR: Architecture-Level Search States for LLM-Guided Neural Architecture Evolution](http://arxiv.org/abs/2608.01633v1)
  <details><summary>📄 Abstract</summary>
  Large language models (LLMs) enable neural architecture search (NAS) directly over executable neural network programs. However, code-level flexibility does not provide the architecture state needed for effective mutation: LLMs must infer tensor dependencies, editable components, and compatibility constraints from implementation details. To address this representation mismatch, we propose GraphIR, an architecture-aware intermediate representation that supplements executable programs with a mutati...
  </details>

- **2026-08-03** — Haowei Liu, Jiamian Wang, Hsin-Tai Wu et al. — [HindSearch: Trajectory-Level Hindsight Critique for Search-Augmented Reinforcement Learning](http://arxiv.org/abs/2608.01597v1)
  <details><summary>📄 Abstract</summary>
  Search-augmented LM agents are typically trained with a binary exact-match reward, which throws away most of what a failed trajectory tells us about why it failed. We introduce HindSearch, a hindsight self-distillation procedure for GRPO: after each rollout, a frozen judge writes a short critique of every failed trajectory using the gold answer, and the critique supplies an auxiliary on-policy distillation signal on the student's search actions. On the standard seven-benchmark suite with Qwen2.5...
  </details>

- **2026-08-03** — Hector Zenil, Luan Ozelim — [Measuring in-context algorithmic reasoning in language models against an exact Bayes-optimal standard](http://arxiv.org/abs/2608.01575v1)
  <details><summary>📄 Abstract</summary>
  Whether large language models perform genuine algorithmic reasoning or mere pattern completion is hard to test, because most benchmarks lack a ground truth for correct inductive inference. We introduce F-ICL, an in-context-learning benchmark that supplies one exactly. Using the Turing-complete machine F, complement-symmetrised into sF to remove output-polarity bias, we exhaustively enumerate all 1.5 billion programs of length $L\le13$ and compute the Bayes-optimal posterior in closed form under ...
  </details>

- **2026-08-03** — Yuchao Hou — [FedWorld: Scope-Aware Federation of Agent World Models](http://arxiv.org/abs/2608.01561v1)
  <details><summary>📄 Abstract</summary>
  Large language model (LLM) agents learn world dynamics from local interaction experience to support subsequent planning and action selection. However, the experience available to a single client is often incomplete, which motivates sharing knowledge across clients. Existing federated methods mainly aggregate model parameters, while agent memory-sharing methods commonly pool trajectories, memories, or rules without checking whether they remain valid for each client. This assumption is problematic...
  </details>

- **2026-08-03** — Seongyoon Kim, Boryeong Cho, Jihwan Oh et al. — [Rethinking Personalized Reward Modeling for LLMs under Preference Heterogeneity via Group-Debiased Federated Learning](http://arxiv.org/abs/2608.01556v1)
  <details><summary>📄 Abstract</summary>
  Large language models are increasingly aligned to human preferences via reward modeling, but user preference data are sensitive and often cannot be centralized. Federated learning keeps such data local while learning a shared initial reward model, which is later personalized for each client through local fine-tuning. Because users often assign opposite labels to the same pair of responses, existing federated methods address preference heterogeneity by clustering similar clients and training one ...
  </details>

- **2026-08-03** — Gaetano Chiriaco, Luca Barco, Andrea Bragagnolo et al. — [GEOID-Flood: A Large-Scale Multi-Modal Benchmark Dataset for Flood Segmentation](http://arxiv.org/abs/2608.02315v1)
  <details><summary>📄 Abstract</summary>
  Geospatial foundation models aim to learn representations that transfer across regions and sensors, yet evaluating them on specific tasks requires large, high-quality, multi-modal benchmarks that measure how well such models extract value from data. Concerning flood mapping, existing datasets rarely combine bi-temporal SAR and co-registered optical imagery at scale, leaving the value of foundation models for this downstream task largely untested. We introduce GEOID-Flood, a large-scale multi-mod...
  </details>

- **2026-08-03** — Lingwei Dang, Shishuo Shang, Pan Liu et al. — [StyleForge: Indoor Furniture Styling by Counterfactual Reasoning in a Hypergraph Field](http://arxiv.org/abs/2608.01954v1)
  <details><summary>📄 Abstract</summary>
  Fixed-layout indoor furniture styling requires selecting assets that form a coherent room without changing the prescribed furniture categories, positions, orientations, or scales. Existing approaches typically retrieve each asset independently or rely on static local relations, making them prone to shape, material, and color conflicts after scene composition. We introduce StyleForge, a scene-level structured selection framework built on a dynamic hypergraph style field. A frozen multimodal large...
  </details>

- **2026-08-03** — Donglin Yang, Haoran Chen, Xingyu Chen et al. — [Learning Panorama-Aware VLA for Mobile Manipulation with Whole-Body Teleoperation](http://arxiv.org/abs/2608.02257v1)
  <details><summary>📄 Abstract</summary>
  Mobile manipulation is a key capability for embodied intelligence, enabling robots to accomplish complex multi-stage tasks in open-world environments. However, mobile manipulation poses two key challenges for vision-language-action (VLA) policies: At the data level, the efficient collection of high-quality whole-body demonstrations demands the coordinated control of both the mobile base and the robotic arms; at the model level, existing VLA models predominantly rely on local camera observations,...
  </details>

- **2026-08-03** — Jin Cui, Yanbin Hu, Xinyue Long et al. — [Look Where It Matters: Adaptive Visual Refinement for Vision-Language-Action Models](http://arxiv.org/abs/2608.02197v1)
  <details><summary>📄 Abstract</summary>
  Visual representations of VLA models remain unreliable for spatially precise robotic manipulation. We uncover that vision encoders in VLAs also exhibit attention artifacts previously documented in generic Vision Transformers, and further show that, in embodied policies, these artifacts are closely associated with spatial perception capabilities acquired during post-training. As the encoder learns task-relevant information such as object location, depth ordering, and local geometry, limited globa...
  </details>

- **2026-08-03** — Jing Wu, Jianhua Wu, Jiayi Guan et al. — [SpatioLM: Towards General Physical Spatial Intelligence in Vision-Language Models](http://arxiv.org/abs/2608.01899v1)
  <details><summary>📄 Abstract</summary>
  Vision-Language Models (VLMs) perform well on commonsense reasoning tasks but struggle with visual spatial reasoning. Most existing solutions introduce extra 3D prior inputs or external spatial encoders, which increase complexity and degrade the underlying VLMs' general-purpose capabilities after spatial fine-tuning. To this end, we propose a parameter-efficient \textit{\textbf{Spatio}-vision \textbf{L}anguage \textbf{M}odels (SpatioLM)}, that enhances spatial intelligence without extra 3D prior...
  </details>

- **2026-08-03** — Dongdong An, Pengjie Zhao, Yihao Huang et al. — [Uncovering and Mitigating Positional Blind Spots in Vision-Language-Action Models](http://arxiv.org/abs/2608.01573v1)
  <details><summary>📄 Abstract</summary>
  Recent Vision-Language-Action (VLA) models achieve promising performance in robotic manipulation, typically measured by success rates aggregated over predefined object configurations, an evaluation that implicitly assumes spatially uniform competence across the workspace. However, this assumption does not hold: even with the instruction and every other scene factor held fixed, merely relocating a task-irrelevant distractor can sharply raise the failure probability within localized, spatially coh...
  </details>

- **2026-08-03** — Marta Garnelo, Wojciech M. Czarnecki — [Why Large Language Models Fail at Tabular Prediction](http://arxiv.org/abs/2608.02412v1)
  <details><summary>📄 Abstract</summary>
  Large language models (LLMs) have become the default tool for a remarkable range of tasks, yet they have had conspicuously little success at one of the most common machine learning workloads: predictive analytics over tabular data. This gap is the founding premise of the fast-growing field of tabular foundation models, but the question of why generic LLMs fail has remained open. We study a frontier LLM in its purest inference regime - a single generation pass over a prompt containing the full tr...
  </details>

- **2026-08-03** — Sajjad Abdoli, Ghassan Al-Sumaidaee, Ahmad ElShiekh et al. — [Can Foundation Models Hear What Made That Sound? A Tiered Benchmark of Audio-Language Models and Traditional Classifiers for Closed-Set Sound Source Identification](http://arxiv.org/abs/2608.02397v1)
  <details><summary>📄 Abstract</summary>
  We benchmark eleven audio classification methods: five task-aware closed-set LLMs (four Gemini models plus open-weight Kimi-Audio-7B-Instruct), four fixed-vocabulary taggers (YAMNet, PANNs, Whisper-AT, and SSLAM), a zero-shot audio-text model (CLAP), and an audio-grounded LLM (BAT). We evaluate them on a closed-set sound-source identification task over 2,242 clips spanning 23 fine-grained classes and 11 categories. Since these methods differ fundamentally in how they receive the task and how out...
  </details>

- **2026-08-03** — Alejandro Velasco, Daniel Rodriguez-Cardenas, Dipin Khati et al. — [ECLAIR: A Causally-Grounded AI Framework for Scientific Discovery in Empirical Software Engineering](http://arxiv.org/abs/2608.02323v1)
  <details><summary>📄 Abstract</summary>
  The scientific method has long guided empirical research in Software Engineering (SE), but the complexity of modern software systems often hinders its systematic application. This paper introduces _ECLAIR_, a causally grounded AI framework that integrates Large Language Models (_LLMs_) into every stage of the scientific process, from hypothesis generation to analysis and interpretation. _ECLAIR_ treats _LLMs_ as active **scientific agents** operating under the principles of causal inference, wit...
  </details>

- **2026-08-03** — Zhijian Zhou, Long Li, Xuan Zhang et al. — [Start Classifying: Categorical Critics for LLM Reinforcement Learning](http://arxiv.org/abs/2608.02181v1)
  <details><summary>📄 Abstract</summary>
  Proximal Policy Optimization (PPO) for large language models typically trains its critic by mean-squared-error (MSE) regression on scalar value targets. Although scalar MSE is statistically valid for estimating the conditional expected return, sparse binary rewards in reinforcement learning with verifiable rewards (RLVR) make critic optimization and calibration especially consequential: small value errors directly distort the scalar advantages used by PPO. We study whether a classification-based...
  </details>

- **2026-08-03** — Yijun Zhang, Yule Xie, Jiaxin Ding et al. — [Beyond the Mean: Multi-Moment Policy Optimization for LLM Reasoning](http://arxiv.org/abs/2608.02149v1)
  <details><summary>📄 Abstract</summary>
  Reinforcement learning has become a central paradigm for improving the reasoning capabilities of large language models. Existing methods generally aim to reduce the failure probabilities induced across problems. In this paper, we introduce a moment-based perspective on policy optimization for LLM reasoning by treating the failure probability of a randomly sampled problem as a random variable and characterizing optimization objectives through its moments. Under this perspective, many existing met...
  </details>

- **2026-08-03** — Timur Mudarisov, Mikhail Burtsev, Radu State — [Feed-Forward Steering in Transformer Residual Dynamics](http://arxiv.org/abs/2608.02071v1)
  <details><summary>📄 Abstract</summary>
  Attention-only dynamical theories model Transformer residual directions as particles aggregating on a sphere. We extend this framework by incorporating the feed-forward network (FFN) term as a local steering field acting on each token state. The resulting theory predicts that the tangential component of the FFN field is necessary for motion in residual-direction space, that critical residual directions correspond to nonlinear projective equilibria, and that a commutator defect determines when a ...
  </details>

- **2026-08-03** — Avni Mittal, Avinash Anand, Ashutosh Kumar et al. — [TextNCA: Neural Cellular Automata for Language Modeling via Hierarchical Local Attention](http://arxiv.org/abs/2608.02050v1)
  <details><summary>📄 Abstract</summary>
  Can a strictly local, iterated, weight-shared computation primitive support language modelling, and which of those three properties actually drives the model's behaviour? We define \textsc{TextNCA}, a 1D causal windowed-attention realisation of the Neural Cellular Automaton primitive, and study a hierarchical variant that cascades three stages with windows $w \in \{8, 32, 128\}$ and $T_s$ shared-weight iterations per stage, all on WikiText-103 at roughly 30M parameters and 60k training steps. Th...
  </details>

- **2026-08-03** — Yixiao Qian, Song Chen, Pengkai Wang et al. — [DART: Decoded Attention over Recurrent States for Efficient Long-Context Sequence Modeling](http://arxiv.org/abs/2608.02032v1)
  <details><summary>📄 Abstract</summary>
  Modern language models are built primarily from Transformers, recurrent models, and their hybrid architectures. Transformers rely on token-level attention memories, while recurrent models such as state space models (SSMs) and linear attention maintain compact recurrent states. These architectures are typically instantiated separately or interleaved at the layer level, leaving open whether a shared memory representation can support both recurrent compression and attention-style retrieval. We stud...
  </details>

- **2026-08-03** — Kunal Kumar Pant, Nithin Nagaraj — [ChaosProbe: A Neurochaotic Lens on Frozen Transformer Input-Embedding Spaces](http://arxiv.org/abs/2608.01968v1)
  <details><summary>📄 Abstract</summary>
  Transformer models are most often understood through what they do: their benchmark performance, generation quality, or behavior on downstream tasks. Yet frozen transformer input-embedding spaces may also be examined through their responses to a controlled deterministic probe before contextual computation or task-specific adaptation. Guided by this response-based view, we introduce \emph{ChaosProbe}, a deterministic neurochaos-inspired method for constructing response-based fingerprints of frozen...
  </details>

- **2026-08-03** — Wenkai Li, Yuchao Wu, Ziyan Guo et al. — [LEAP: A Self-Supervised Per-Cycle Toggle Propagation Model Supports Fast, Transferable, and Early Analysis of Layout Power](http://arxiv.org/abs/2608.01946v1)
  <details><summary>📄 Abstract</summary>
  Accurate power analysis is critical in VLSI design, as it directly impacts power optimization strategies. However, traditional approaches are often hindered by the substantial runtime required for per-cycle toggle propagation in the netlist, which propagates register toggle information through combinational logic. To address this, we propose LEAP, the first work to enable per-cycle toggle propagation prediction with both high accuracy and efficiency. This is achieved through a novel, linear-comp...
  </details>

- **2026-08-03** — Junjie Yu, Zihan Deng, Jianyu Zhang et al. — [Understanding and Correcting Low-Frequency Bias in EEG Foundation Model](http://arxiv.org/abs/2608.01898v1)
  <details><summary>📄 Abstract</summary>
  Increasing EEG pretraining data scale or model capacity does not consistently improve downstream performance. We identify a persistent low-frequency bias in representations learned by diverse EEG foundation models, which remains across dataset scales, model capacities, and pretraining objectives. Our analysis links this bias to the interaction between EEG's $1/f^α$-like spectral structure and neural networks' tendency to preferentially learn low-frequency components. In masked autoencoders, the ...
  </details>

- **2026-08-03** — Kaoru Sumi, Souki Osawa — [Emotional Expression in Persuasion by Quadruped Virtual Agents: Toward Cross-Species Design Patterns](http://arxiv.org/abs/2608.01895v1)
  <details><summary>📄 Abstract</summary>
  Persuasive technologies increasingly use virtual agents to influence attitudes and behavior, but research has focused mainly on humanoid agents. The persuasive design of non-humanoid, quadruped agents remains underexplored, and it is unclear whether emotional expression works consistently across animal species or whether species-specific motion is necessary.   We developed virtual dog, cat, and horse agents and compared three behavioral conditions: species-specific behavior, shared behavior acro...
  </details>

- **2026-08-03** — Seunghan Lee, Jun Seo, Jaehoon Lee et al. — [ReasonCast: Towards Explainable Time Series Forecasting with Reasoning](http://arxiv.org/abs/2608.01875v1)
  <details><summary>📄 Abstract</summary>
  Most time series (TS) models are specialized for a single task, either understanding (i.e., returning text answers about a TS) or generation (i.e., returning a numeric forecast). Only recently have unified models begun to handle the two within a single architecture. Even these models, however, produce the two outputs as task-separated paths and cannot predict a series and explain why that prediction arises within a single coherent response. In this paper, we argue for a task-fused model that joi...
  </details>

- **2026-08-03** — David Fertig — [Impedance of an electric double layer capacitor with a multi-component electrolyte](http://arxiv.org/abs/2608.01799v1)
  <details><summary>📄 Abstract</summary>
  I derive the impedance response of an ideal electrolyte containing an arbitrary number of mobile ionic species between blocking planar electrodes, described by the Poisson--Nernst--Planck equations. By transforming the linearized equations to a charge--salt basis, the response is written in terms of a multi-component diffusion--migration matrix and its eigenvalues/eigenvectors. When all diffusivities are equal, the charge mode decouples from the neutral concentration subspace and the classical b...
  </details>

- **2026-08-03** — Zixuan Huang, Yang Zhou, Kaixuan Wang et al. — [Deferred Exposure of Future Trajectories for Verifiable Reasoning in Autonomous Driving VLMs](http://arxiv.org/abs/2608.01755v1)
  <details><summary>📄 Abstract</summary>
  Recent Vision-Language-Action (VLA) models for autonomous driving (AD) increasingly utilize chain-of-thought (CoT) supervision to enhance the reasoning capabilities of their Vision-Language Model (VLM) components, yet existing annotation pipelines commonly expose the teacher model to the logged ground-truth (GT) future trajectory. We empirically show that this induces trajectory anchoring bias: teacher models rationalize the revealed outcome rather than infer a decision from scene evidence, prod...
  </details>

- **2026-08-03** — Yeonseo Jeong, Wonhyeok Ko, Sungweon Hong et al. — [Heterogeneous Multi-Agent Reinforcement Learning for Radio Resource Management under Coupled Finite-Horizon Constraints](http://arxiv.org/abs/2608.01745v1)
  <details><summary>📄 Abstract</summary>
  Maximizing throughput under proportional fairness in dense wireless networks requires jointly managing user association, scheduling, base station (BS) activation, and handover control under hard finite-horizon energy and handover budgets, which induces a fundamental tension between BS-side energy management and user-side handover regulation. While multi-agent reinforcement learning (MARL) is a natural framework for such distributed sequential control, its application here faces two difficulties:...
  </details>

- **2026-08-03** — Logan Ritchie, Sushant Mehta, Liudas Panavas et al. — [Post-Training on Office Work Improves Software Engineering: A Behavioral Account of Cross-Domain Transfer](http://arxiv.org/abs/2608.01604v1)
  <details><summary>📄 Abstract</summary>
  Long-horizon tasks require agents to maintain coherent state and goals across nested and branching work. We call this capability goal-directed execution (GDE): the repeated application of four behaviors, namely selecting goals, constructing task-relevant state, maintaining fidelity to higher-level objectives, and verifying completion against the environment. We hypothesize that long-horizon post-training strengthens these behaviors across domains. We test this by post-training Qwen3.5-122B-A10B ...
  </details>

- **2026-08-03** — Abdul Basit Tonmoy — [Discriminative Axis, Not Data Volume: What a Contrastive Corpus Teaches an Audio Embedding](http://arxiv.org/abs/2608.01560v1)
  <details><summary>📄 Abstract</summary>
  Scaling the corpus is the default remedy when a contrastive representation lacks an attribute. We report a case where it does nothing, and identify what does: adding a lexical-speech round to a frozen-base multimodal embedding model raises zero-shot keyword spotting by 76 points while reducing speech-emotion recognition by 14. The loss is not a capacity limit: fine-tuning on 7,442 clips from a prosody-controlled corpus recovers emotion past its pre-speech level at a five-point keyword cost. Nor ...
  </details>

- **2026-08-02** — Zhiwei Chen, Yang Hu, Yuxiang Xiao et al. — [Harnessing Adversarial Distillation to Customise Debiased, Disease-Specific Pathology Foundation Models for Breast Cancer](http://arxiv.org/abs/2608.01356v1)
  <details><summary>📄 Abstract</summary>
  Pathology foundation models (PFMs) provide strong tissue representations and have become central to digital pathology. However, deployment in disease-specific settings is limited by 1) the high computational cost of billion-parameter PFMs and 2) distribution mismatch and non-biological bias inherited from pan-cancer, multi-centre pre-training, including site-specific signatures and imbalanced disease prevalence. These factors can encourage shortcut learning and under-emphasise subtle morphology ...
  </details>

- **2026-08-02** — Fabian Slonimczyk, Danila Karapsin — [Measuring Product Quality Using Images: The CLIP Q-Score and an Application to Real Estate](http://arxiv.org/abs/2608.01544v1)
  <details><summary>📄 Abstract</summary>
  The CLIP Q-score is a novel, safe, fully reproducible, and computationally efficient method for extracting objective product quality metrics from visual data using contrastive language-image pre-training. We introduce the technique and provide an extensive application to real estate data from an online platform ($\sim500,000$ images). Our open-source metric aligns with LLM assessments and proves to be a powerful predictor of housing market prices for both sales and rentals. We also show that a h...
  </details>

- **2026-08-02** — Bingxuan Li, Rui Yang, Cheng Qian et al. — [Long-Horizon Embodied Decision-Making via Multimodal Memory Compression](http://arxiv.org/abs/2608.01456v1)
  <details><summary>📄 Abstract</summary>
  Agents are increasingly expected to act not only as task executors, but also as decision-makers on behalf of human users. This shift requires agents to accumulate evidence over long horizons, interpret implicit user preferences, and compare multiple candidates under partial observations. In this work, we propose DunphyBench, a new benchmark for evaluating agents on long-horizon human-centered embodied decision-making, where the agent must navigate through multiple embodied housing environments a...
  </details>

- **2026-08-02** — Pritam Deka, Prabhjot Singh — [When Retrieval Helps and Distracts: Evaluating Evidence-Generating LLMs for Biomedical Claim Verification](http://arxiv.org/abs/2608.01409v1)
  <details><summary>📄 Abstract</summary>
  Biomedical fact-checking systems must do more than predict whether a claim is supported, contradicted, or unaddressed: they should also produce evidence that is faithful, complete, and useful for verification. We study this evidence-generation setting on CARE-XAI, a unified benchmark spanning five biomedical and health fact-checking sources. We compare base instruction LLMs, PubMed retrieval-augmented LLMs, fine-tuned LLMs, label-only LLMs, and biomedical encoder classifiers under a shared evalu...
  </details>

- **2026-08-02** — Jianan Xie, Xin Sun, Zhongqi Chen et al. — [EviSD: Evidence-Conditioned Self-Distillation for Search-Augmented Agents](http://arxiv.org/abs/2608.01359v1)
  <details><summary>📄 Abstract</summary>
  Outcome-based reinforcement learning enables search-augmented language agents to learn from verifiable final answers, but its trajectory-level credit cannot distinguish the contributions of individual actions in a multi-turn search process. We propose EviSD, an evidence-conditioned self-distillation framework that uses instance-level supporting evidence as privileged information for search actions and golden answers as complementary privilege for answer actions. During training, the student samp...
  </details>

- **2026-08-02** — Sarah Wilson, Michael MacKay, Anthony Marello et al. — [Can Language Models Identify Shadow Trading Targets? An NLP Evaluation of SEC Enforcement Theory](http://arxiv.org/abs/2608.01322v1)
  <details><summary>📄 Abstract</summary>
  Shadow trading -- trading in a peer firm's securities on the basis of material nonpublic information (MNPI) about an "economically linked" company -- is a novel and contested theory of insider trading liability, first prosecuted in SEC v. Panuwat (2023). Enforcing it requires identifying economically linked firms ex ante, a determination the SEC makes only after the fact using mass market surveillance infrastructure. We ask whether NLP can do what the SEC's theory presumes insiders already know:...
  </details>

- **2026-08-02** — Xiaocui Yang, Xican Tan, Shoujie Chen et al. — [CrossLex: A Source-Grounded Benchmark for Cross-Jurisdictional Legal Reasoning in Large Language Models](http://arxiv.org/abs/2608.01292v1)
  <details><summary>📄 Abstract</summary>
  Legal reasoning is inherently jurisdiction-dependent: the same facts can call for different legal rules and yield different conclusions across legal systems. Yet existing benchmarks rarely evaluate whether large language models (LLMs) can recognize such jurisdiction-specific variation, especially when identical fact patterns lead to divergent legal outcomes.We introduce CrossLex, a same-fact, legal-source-grounded benchmark for evaluating cross-jurisdictional legal reasoning in LLMs across three...
  </details>

- **2026-08-02** — Leyan Xue, Feng Xiong, Mingjun Ma et al. — [Distill What the Student Can See: Fisher-Projected On-Policy Distillation for Vision-Language Models](http://arxiv.org/abs/2608.01263v1)
  <details><summary>📄 Abstract</summary>
  On-policy distillation (OPD) samples trajectories from the current student policy and minimizes token-level divergence between student and teacher next-token distributions at prefixes along those trajectories. This aligns the distillation states with the student's own generation distribution. However, it still assumes that the complete teacher distribution is an appropriate target across student capacities. In vision--language reasoning, teacher corrections can depend on visual distinctions that...
  </details>

- **2026-08-02** — Sen Liang, Fengbin Guan, Youliang Zhang et al. — [CoT-Edit: Let CoT Guide Instruction Video Editing](http://arxiv.org/abs/2608.01113v1)
  <details><summary>📄 Abstract</summary>
  Text-driven instruction-based video editing in complex scenes remains challenging: purely textual prompts often fail to capture precise spatial relationships and physical constraints, resulting in target ambiguity and physically implausible outcomes. To address this, we propose a plan--guide--edit framework that explicitly bridges semantic intent and spatial execution. In our framework, a Chain-of-Thought (CoT)-enhanced multimodal large language model (MLLM) serves as a planner, performing struc...
  </details>

- **2026-08-02** — Van An Nguyen, Vuong Khang Huynh, Hoai Thuong Nguyen et al. — [Co-evolution of social reward and punishment under institutional interventions](http://arxiv.org/abs/2608.01183v1)
  <details><summary>📄 Abstract</summary>
  We investigate how peer and institutional incentives jointly shape the evolution of cooperation, social welfare, and enforcement efficiency in social dilemmas. In a Prisoners Dilemma with four strategies, unconditional cooperators (C), defectors (D), social punishers (SP), and social rewarders (SR), we allow decentralised peer incentives and centralised institutional incentives to act simultaneously, with the institution able to reward or punish any subset of strategies. In infinite well-mixed p...
  </details>

- **2026-08-02** — Jiaming Jiang, Yuzhe Huang, Hao Liang et al. — [CAAT: Contact-Aware Attention Scaling and Tactile Masking for Data-Efficient Contact-Rich Manipulation](http://arxiv.org/abs/2608.01102v1)
  <details><summary>📄 Abstract</summary>
  In contact-rich manipulation, visual observations primarily guide motion in free space, whereas tactile observations become particularly informative during contact. However, standard Transformer-based visuo-tactile policies typically rely on either token concatenation or learnable gating. These approaches lack explicit contact-aware priors, making it difficult to efficiently learn effective cross-modal representations from demonstrations. To address this limitation, we propose CAAT, a lightweigh...
  </details>

- **2026-08-02** — Robert Jacob Ryan — [Conformal Kelly: Conformal Prediction Intervals as the Scale in Fractional Kelly Position Sizing](http://arxiv.org/abs/2608.01494v1)
  <details><summary>📄 Abstract</summary>
  Conformal prediction has traditionally been used to quantify prediction uncertainty. We put that uncertainty to a second use, combining a 75% conformal interval with fractional Kelly to size portfolio positions: as the range widens we shrink the position, and as it narrows we grow it. On a six-year development window (2016-2021), with trading costs and strict leverage caps, this compounds at 28.5% annualised net log growth with a Sharpe ratio of 1.34 and a 27.7% maximum drawdown, versus 15.9% fo...
  </details>

- **2026-08-02** — MD Shaikh Rahman, Syed Maudud E Rabbi, Muhammad Mahbubur Rashid — [Two-Stage Bengali Sentiment Classification: Domain Adaptation Through Continual Learning and Parameter-Efficient Fine-Tuning](http://arxiv.org/abs/2608.01471v1)
  <details><summary>📄 Abstract</summary>
  Understanding sentiment in low-resource languages remains a key challenge for Natural Language Processing (NLP), particularly when domain-specific data is scarce. In this work, we present SentiBanglaBERT, a two-stage Bengali sentiment classification framework combining domain-adaptive continual pretraining and parameter-efficient fine-tuning. The approach enables contextual adaptation to news-style data while remaining computationally efficient through Low-Rank Adaptation (LoRA). Beyond performa...
  </details>

- **2026-08-02** — Yuqicheng Zhu, Jialin Yu, Lin Li et al. — [Conformalized Large Language Models under Configuration Shift](http://arxiv.org/abs/2608.01460v1)
  <details><summary>📄 Abstract</summary>
  Conformal prediction (CP) is a distribution-free framework for uncertainty quantification that has recently been adapted to large language models (LLMs), providing prediction sets with finite-sample coverage guarantees under exchangeability. Yet for LLMs, nonconformity scores are often induced by an inference pipeline, not just a fixed model, making them depend not only on the data distribution but also on configurable factors such as the prompt template, decoding parameters, and deployment sett...
  </details>

- **2026-08-02** — Huiyu Yi, Yongqi Xu, Bogang Zhang et al. — [Beyond Routing Saturation: A Long-Horizon Class-Incremental Perspective on Expert Routing in Multimodal Continual Instruction Tuning](http://arxiv.org/abs/2608.01437v1)
  <details><summary>📄 Abstract</summary>
  Multimodal Continual Instruction Tuning (MCIT) enables multimodal large language models to acquire new tasks sequentially while retaining previously learned capabilities. Many recent methods maintain task-specific LoRA experts and route each input to one or more experts at inference. Yet the task-identification problem underlying expert routing remains under-explored. We show that routing is nearly saturated on widely used MCIT benchmarks. Textual fingerprints that leak task identity and short 4...
  </details>

- **2026-08-02** — Yi Mao, Andrew Perrault — [Training Small LLMs as Spatial Multi-Agent Policies](http://arxiv.org/abs/2608.01425v1)
  <details><summary>📄 Abstract</summary>
  Training LLM-based multi-agent systems with multi-agent reinforcement learning is rapidly gaining traction, and a parallel line of work argues that such systems should be judged by their behavior, not only their reward. We take up both threads in spatial cooperative games, where small frozen LLMs prompted with low-level actions fail outright, earning zero reward. Guided by the options/semi-MDP framework---and, because option execution is asynchronous across agents, its multi-agent extension in m...
  </details>

- **2026-08-02** — TszKin Julian Chan, Juan Estrada, Kim Huynh et al. — [Estimating Social Effects with Randomized and Observational Network Data](http://arxiv.org/abs/2608.01405v1)
  <details><summary>📄 Abstract</summary>
  This paper introduces an innovative approach to identifying and estimating the parameters of interest in the widely recognized linear-in-means regression model under conditions where the initial randomization of peers determines the observed network. We assert that peers who are initially randomized do not produce social effects. However, after randomization, agents can endogenously develop significant connections that potentially generate peer influences. We present a moment condition that comp...
  </details>

- **2026-08-02** — Zixuan Liu, Jonathan Lawry, Michael Crosscombe — [Imprecise Belief Fusion Improves Multi-agent Social Learning](http://arxiv.org/abs/2608.01367v1)
  <details><summary>📄 Abstract</summary>
  In social learning, agents learn not only from direct evidence but also through interactions with their peers. We investigate the role of imprecision in such interactions and ask whether it can improve the effectiveness of the collective learning process. To that end we propose a model of social learning where beliefs are equivalent to formulas in a propositional language, and where agents learn from each other by combining their beliefs according to a fusion operator. The latter is parametrised...
  </details>

- **2026-08-02** — Ilias Chalkidis, Vlad Paul Cosma, Søren Debois et al. — [Hybrid AI for Explainable and Accurate Conversational Agents in eGovernment](http://arxiv.org/abs/2608.01346v1)
  <details><summary>📄 Abstract</summary>
  We present a so-called Conversational Hybrid AI (CHAI) architecture for building explainable and accurate conversational agents for eGovernment. We exemplify the architecture with a running prototype of a Covid-19 Chatbot based on a governmental guideline directed to citizens. We also describe an ongoing case on case management for supplementary grants for students with disabilities. We use large language models (LLMs) as a bounded conversational interface to a rule-based (symbolic AI) controlle...
  </details>

- **2026-08-02** — Advait Pavuluri, Shamik Karkhanis, Uzma Mushtaque — [Asleep at the Wheel: JEPA's Limitations in Evaluating Novel Driving Data](http://arxiv.org/abs/2608.01336v1)
  <details><summary>📄 Abstract</summary>
  Modern autonomous-driving fleets record far more video than human reviewers can inspect. This motivates the need for an automatic clip triage mechanism, to surface rare and review-worthy clips, so that driving models can be fine-tuned to better handle unideal circumstances. We test a label-free approach that scores clips by the prediction-error "novelty" of a self-supervised joint-embedding predictive architecture (JEPA); a frozen V-JEPA video encoder is paired with a lightweight predictor head ...
  </details>

- **2026-08-02** — Xiaohui Bei, Felix Brandt, Matthias Greger et al. — [Individual Fairness in Budget Aggregation](http://arxiv.org/abs/2608.01228v1)
  <details><summary>📄 Abstract</summary>
  We consider the problem of aggregating $n$ individual distributions over $m$ alternatives into a collective distribution, also known as budget aggregation. Existing fairness notions in this literature typically do not guarantee fairness to individual agents. To address this, we define two versions of individual fair share guarantees. We show that when agents' utilities are derived from $\ell_t$ metrics for any $t\geq 1$, both these guarantees can be satisfied along with Pareto efficiency, and th...
  </details>

- **2026-08-02** — Yuhao Fu, Nobuyuki Hanaki, Haitao Wang — [Do Humans Bargain Differently with AI? Evidence from Alternating-Offer Games](http://arxiv.org/abs/2608.01212v1)
  <details><summary>📄 Abstract</summary>
  Artificial intelligence increasingly participates in economic interactions not only as a tool, but also as an autonomous bargaining counterpart negotiating on behalf of firms, platforms, and consumers. Yet little is known about how humans respond psychologically and strategically when bargaining with such agents in dynamic settings. We study this question in a laboratory experiment using a three-stage alternating-offer bargaining game in which participants negotiate in real time with either anot...
  </details>

- **2026-08-02** — Boone Bowles, Raymond Duch, Sorin Sorescu — [Talking to Digital Twins: Selective Disclosure and Belief Measurement in Financial Social Media](http://arxiv.org/abs/2608.01181v1)
  <details><summary>📄 Abstract</summary>
  Social media affect financial markets, but public posts by financial media personas are voluntary disclosures. What is not disclosed is therefore usually unobserved. We address this measurement problem by conducting repeated, real-time interviews of "digital twins" built from monitored finfluencers' X accounts under a fixed protocol. The interviews recover stock-level public-persona belief proxies even when no public recommendation is made. Because the interviews are generated and archived befor...
  </details>

- **2026-08-02** — Mohammed Q. Shormani — [Does Machine "know" interpersonal pragmatics? Evidence from MARBERT's learning of emoji pragmatics in Arabic digital discourse](http://arxiv.org/abs/2608.01174v1)
  <details><summary>📄 Abstract</summary>
  This study examines Transformer-based models' ability to learn emoji pragmatics in Arabic digital discourse (ADD), providing evidence from MARBERT's behavior with interpersonal pragmatic functions (IPFs). A corpus of 8,504 unique emoji-posts collected from Facebook via Python was used in the study. These posts were manually annotated, developed, and labeled for five IPFs: Politeness, Respect, Solidarity, Empathy, and Encouragement. A mixed-method approach was employed comprising statistical meth...
  </details>

- **2026-08-02** — Simiao Ren — [CallScreenBench: Benchmarking On-Device Models as Phone Secretaries](http://arxiv.org/abs/2608.01033v1)
  <details><summary>📄 Abstract</summary>
  Language models small enough to run on a handset, quantized to a few bits, are increasingly capable of acting for their user, making on-device task automation newly plausible. One such task is answering the phone. A phone secretary takes an unknown inbound call on its owner's behalf. Unlike the agents evaluated by most benchmarks, it has no task to complete and no cooperative user: the caller holds the goal, may be an adversary, and must be judged from the opening turn with no oracle. What matte...
  </details>

- **2026-08-02** — Yinghan Hou, Zongyou Yang — [VeraRAN: Pre-Actuation Certification and Event-Causal Synchronization Repair for Asynchronous Multi-Interface RAN Plans](http://arxiv.org/abs/2608.01047v1)
  <details><summary>📄 Abstract</summary>
  Agentic RAN controllers combine mobility, energy, and resource actions across independently implemented interfaces. Even when each command is valid and the target state is safe, asynchronous actuation can drive the network through unsafe intermediate states. In a frozen study of a 35B planner, 28.8% of locally valid plans remained asynchronously unsafe. We introduce VeraRAN, which checks plans before actuation by modeling request, delivery, acceptance, application, completion, and observation fo...
  </details>

- **2026-08-02** — Gautam Bharti — [Registry Descriptions Go Stale Unevenly: An 89-Day Measurement of Model Context Protocol Drift, and Why Drift-Ranked Re-Auditing Under-Covers It](http://arxiv.org/abs/2608.00997v1)
  <details><summary>📄 Abstract</summary>
  Security studies of the Model Context Protocol (MCP) ecosystem share a design: each audits a registry at a single point in time. None reports how long the registry descriptions those audits judged stay current - a necessary condition for any description-level finding to still apply, though not a sufficient one: we measure the shelf-life of the audited text, not the validity of a security finding itself (Sec. 7.1). We reconstruct 120 observations of the official MCP registry over 88.6 days, cover...
  </details>

- **2026-08-02** — Shrenil Shaun Sharma, Avi Sharma — [SCHEDBench: A Benchmark for Evaluating LLM Constraint Faithfulness in Natural-Language Combinatorial Scheduling](http://arxiv.org/abs/2608.00991v1)
  <details><summary>📄 Abstract</summary>
  This paper introduces SCHEDBench, a natural-language benchmark for evaluating combinatorial scheduling constraint faithfulness under surface-form variation. Grounded in canonical scheduling instances and solver-derived feasibility and optimality, SCHEDBench assesses whether large language models (LLMs) generate schedules with the same constraint-feasible behavior across varied natural-language (NL) surface forms. SCHEDBench spans 1,132 instances across job-shop scheduling problems (JSP), single ...
  </details>

- **2026-08-02** — Mayank Sharma, Rohit Kumar Mourya, Pratik Mazumder — [Logit-Origin Centering for Singleton Test-Time Adaptation](http://arxiv.org/abs/2608.01074v1)
  <details><summary>📄 Abstract</summary>
  Tabular data is used extensively in many real-world use cases. Deep learning models have been developed to deal with tabular data, but generally perform poorly when the test data distribution differs from that of the training data. Researchers have proposed test-time adaptation approaches to deal with this problem. The fully test-time adaptation (FTTA) setting involves adapting deployed classifiers to shifted target distributions using only unlabeled test data. Leading FTTA methods inherit a bat...
  </details>

- **2026-08-02** — Nathan Hu, Yang Yang, Fumio Okura — [PlantRig - From Bones to Branches: Adaptation of Autoregressive Rigging Models for Plant Skeletal Reconstruction](http://arxiv.org/abs/2608.01072v1)
  <details><summary>📄 Abstract</summary>
  Autoregressive rigging models such as UniRig and SkinTokens perform well on articulated characters, but their ability to generalize to plant structures remains largely unexplored, since plant topologies exhibit highly variable, non-canonical branching patterns that challenge learned skeletal priors. We evaluate these models for plant skeletal reconstruction using synthetic L-system-generated trees and real scanned data spanning monopodial, sympodial, whorled, and vine-like archetypes. Preliminar...
  </details>

- **2026-08-02** — Zhihao Zhu, Hanlin Shang, Mingwang Xu et al. — [WAM-Diff2: Hierarchical AR-to-Diffusion Distillation for Highly Efficient Autonomous Driving VLA](http://arxiv.org/abs/2608.01035v1)
  <details><summary>📄 Abstract</summary>
  Vision-Language-Action (VLA) models have emerged as a prominent paradigm for end-to-end autonomous driving; however, their efficient deployment is severely constrained by high computational latency and exposure bias arising from sequential autoregressive decoding. Conversely, while specialized diffusion policies enable low-latency, parallel execution, training them from scratch typically yields narrow, single-task architectures that lack holistic visual-linguistic reasoning. Successfully transfo...
  </details>

- **2026-08-02** — Kaike Ping, Buse Çarık, Caleb Wohn et al. — [Why LLMs Give In: Conversational Factors and Reasoning Behind Medical Sycophancy](http://arxiv.org/abs/2608.01017v1)
  <details><summary>📄 Abstract</summary>
  A language model that abandons a correct medical answer under user pushback is more dangerous than one that was simply wrong, because it lends the credibility of a correct answer to the user's misinformation. Such model behavior, described as medical sycophancy, is usually reported as a single rate per model, but we find it is a property of the conversation, not the model. We study medical sycophancy in language models with a fully crossed factorial design over four conversational factors, user ...
  </details>

- **2026-08-02** — Yohei Nakajima — [Passing Coarse Marginal Checks Can Be Cheap: Persona Mixtures and Imprecise Treatment-Response Estimates in an LLM Persona Panel](http://arxiv.org/abs/2608.00979v1)
  <details><summary>📄 Abstract</summary>
  Large language models are increasingly used as synthetic research participants and are often validated by whether their marginal responses resemble human data. We study a fixed panel of sixteen lightweight persona-conditioned GPT-4.1 configurations in repeated strategic games. The panel met preregistered broad-reference condition-mean criteria in three of four repeated-game cells; the sole miss was 0.011 below the lower reference bound. Variation was strongly prompt-indexed, but its share depend...
  </details>

- **2026-08-02** — Igor Cialenco, Michael Ludkovski, Gael Dimitri Tekam Fongouo — [Pro-rata mechanisms in groundwater markets](http://arxiv.org/abs/2608.00917v1)
  <details><summary>📄 Abstract</summary>
  We introduce a pro-rata rationing mechanism for resolving supply-demand imbalances in groundwater markets, extending the price-formation model of Cialenco and Ludkovski (2025). We show that under the pro-rata distribution, every price is a Nash equilibrium, thereby pro-rata approach provides a rationing device whenever supply and demand fail to match. By the very nature of the pro-rata mechanism, the resolution of supply-demand imbalances is unique, and the proportional rationing approach is fai...
  </details>

- **2026-08-01** — Hao Mark Chen, Jinnan Guo, Wayne Luk et al. — [AOSpec: Action and Observation Co-Speculation for Low-Latency Agent Serving](http://arxiv.org/abs/2608.00881v1)
  <details><summary>📄 Abstract</summary>
  Large language model agents increasingly act through stateful tools, yet model generation and environment execution remain serialized at every step. As decoding accelerates, tool execution becomes a growing bottleneck. Existing action- or observation-only speculation leaves much of this latency exposed: value is concentrated in a few slow calls, some outcomes emerge only through execution, and longer lookahead typically requires an increasingly unlikely chain of action predictions. We present AO...
  </details>

- **2026-08-01** — Ahmet Faruk Saz, Duo Xu, Faramarz Fekri — [Goal-Oriented Logic-based Semantic Communication for Neuro-Symbolic Reasoning with Applications onto Autonomous Driving](http://arxiv.org/abs/2608.00878v1)
  <details><summary>📄 Abstract</summary>
  We consider First-Order Logic (FOL)-based semantic communication for neuro-symbolic decision-making in collaborative environments such as autonomous driving networks. Each connected autonomous vehicle (CAV) converts its partial sensor observations into a natural-language scene description and corresponding grounded FOL evidence. Under an uplink budget, a semantic encoder at each car selects the observations most informative for evaluating traffic rules and transmit to a Road Side Unit (RSU). The...
  </details>

- **2026-08-01** — Yizhou Wu, Yuheng Li, Xiaofeng Yang et al. — [Anticipatory Digital Twins for Online Head-and-Neck Adaptive Proton Therapy via Foundation-Model Registration](http://arxiv.org/abs/2608.00831v1)
  <details><summary>📄 Abstract</summary>
  Head-and-neck (HN) proton therapy is highly sensitive to anatomical change over a 4-to-6-week course, as tumor shrinkage, weight loss, and setup variation can misposition the Bragg peak near critical organs such as the parotids, oral cavity, brainstem, and spinal cord, leading to target underdosing or organ-at-risk overdosing. Online adaptive proton therapy replans on the anatomy of the day, yet standard workflows rely on offline replanning that requires repeated CT acquisition and roughly a wee...
  </details>

- **2026-08-01** — Tirtha Chanda, Christoph Wies, Franziska Schramm et al. — [Large language models improve physician accuracy but lead to false reliance](http://arxiv.org/abs/2608.00817v1)
  <details><summary>📄 Abstract</summary>
  Retrieval-augmented large language models (LLMs) promise source-linked clinical support, but their value depends on whether displayed evidence guides rather than distorts physician reliance. We developed CORA, an agentic retrieval-augmented LLM, to investigate how source-linked assistance affects physician decision-making. CORA maintained benchmark performance and achieved larger gains on cases published after the models' training-data cutoffs. In a study of 46 physicians, accuracy increased fro...
  </details>

- **2026-08-01** — Meher Bhaskar Madiraju, Meher Sai Preetam Madiraju — [AgentSLABench: Evaluating and Benchmarking Agentic Systems Under Resource Constraints](http://arxiv.org/abs/2608.00805v1)
  <details><summary>📄 Abstract</summary>
  We present AgentSLABench, a resource-aware evaluation framework for autonomous AI agents that measures correctness alongside latency, cost, compute, memory, and network usage under declared resource budgets. Unlike standard benchmarks that report only accuracy, AgentSLABench produces a multi-dimensional profile per agent per task - the same way systems profilers (perf, pprof, cProfile) measure resource consumption of code, but extended with task correctness as a first-class dimension. AgentSLABe...
  </details>

- **2026-08-01** — Ivan Snegirev, Elizaveta Semenyakina, Mikhail Konenkov et al. — [ORCESTRA: VLM-driven Visual Robot programming in Mixed Reality](http://arxiv.org/abs/2608.00775v1)
  <details><summary>📄 Abstract</summary>
  ORCESTRA is a mixed-reality system for programming robot digital twins through no-code waypoint teaching and language-guided control. In a passthrough mixed-reality workspace, users place robot twins on real surfaces, teach trajectories, save robot-relative episodes, or issue spoken/typed commands that a vision-language model converts into structured digital-twin plans. Both interaction modes share a backend for metric grounding, embodiment-aware validation, preview, confirmation, and digital-tw...
  </details>

- **2026-08-01** — Chaoqun Yang, Fengbin Zhu, Xinyu Lin et al. — [FinDeepIndicator: Benchmarking Deep Research Agents in End-to-End Financial Indicator Construction](http://arxiv.org/abs/2608.00764v1)
  <details><summary>📄 Abstract</summary>
  Financial indicators are essential tools for transforming raw financial data into interpretable measures for various downstream tasks, such as valuation, risk assessment, and economic analysis. However, existing financial benchmarks largely focus on answer-level accuracy and often assume that relevant data are already provided, leaving the assessment of the intermediate process of indicator construction underexplored. In this work, we propose FinDeepIndicator, the first benchmark dedicated to ev...
  </details>

- **2026-08-01** — Jinwang Song, Tao Liu, Haowen Zheng et al. — [AttnLink: Turning Attention into Schema Links for Text-to-SQL](http://arxiv.org/abs/2608.00693v1)
  <details><summary>📄 Abstract</summary>
  Schema linking is a critical component of Text-to-SQL systems, but existing approaches often trade off contextual modeling capacity, score-based controllability, and inference efficiency. We introduce AttnLink, an attention-based framework that converts LLMs' internal attention into continuous relevance scores for schema items. AttnLink extracts the attention from the generation-start position to candidate schema spans, enabling all candidates to be ranked in a single prefill pass without autore...
  </details>

- **2026-08-01** — Nicolas Leins, Nico Pelleriti, Jana Gonnermann-Müller et al. — [When Does LLM Orchestration Pay Off? A Controlled Evaluation of Accuracy, Cost, and Task Difficulty](http://arxiv.org/abs/2608.00685v1)
  <details><summary>📄 Abstract</summary>
  LLM orchestration is often assumed to improve reasoning by allocating additional inference-time computation, yet its gains may not justify its cost. Existing comparisons also frequently overlook differences in optimization effort, making it difficult to isolate the value of orchestration itself. We conduct a controlled evaluation of Self-Refine, Best-of-$N$, and Debate against task-only and chain-of-thought (CoT) single-call baselines across five LLM backbones and three domains: competitive prog...
  </details>

- **2026-08-01** — Xiangwei Wang, Nanduni Nimalsiri, Yu Xia et al. — [HetGPS: Scalable Graph Multi-Agent Reinforcement Learning with Physics-Anchored Adaptive Safety for EV Charging](http://arxiv.org/abs/2608.00679v1)
  <details><summary>📄 Abstract</summary>
  Safety interventions for large populations of network-coupled agents must protect shared constraints without unnecessarily overriding task-oriented policy decisions. We present HetGPS, a hybrid graph-control framework synergizing learned graph risk with physics-anchored correction by separating intervention magnitude from corrective direction. An action-conditioned graph residual model schedules state-dependent intervention authority, while a physics model determines its direction. For electric ...
  </details>

- **2026-08-01** — Jonas Thurner, Nadine Jost, Stefan Albert Horstmann et al. — [From Chasing Ghosts to Missed Attacks: Perspectives and Perceptions of SOC Practitioners on LLM Integration, Risks, and Readiness](http://arxiv.org/abs/2608.00672v1)
  <details><summary>📄 Abstract</summary>
  Security Operations Centers (SOCs) process large volumes of security events, requiring analysts to accurately detect and assess ongoing cyberattacks under time pressure. Recent advances in Large Language Models (LLMs) suggest potential benefits for security operations, yet their practical suitability for real-world SOC workflows remains poorly understood. To address this gap, we conducted 25 semi-structured interviews with SOC practitioners who had prior experience with LLMs, complemented by int...
  </details>

- **2026-08-01** — Yong Wang, Hongliang Sun, Jinlan Liu et al. — [GARDRec: Decision-Level Graph Grounding for Large Language Model Recommendation](http://arxiv.org/abs/2608.00669v1)
  <details><summary>📄 Abstract</summary>
  Large language models (LLMs) offer new opportunities for recommendation by interpreting item descriptions, user instructions, and external knowledge through natural-language prompts. However, existing graph-augmented LLM recommenders often use knowledge graphs mainly as prompt-level evidence, leaving ranking decisions weakly constrained by structured user-item relations. This is problematic for next-item recommendation, where the model must compare candidates under the same user context while pr...
  </details>

- **2026-08-01** — Maksym Nechepurenko — [Axient: On-Chain Credit and Loss Allocation for Leveraged Event Markets: A Venue-Agnostic Protocol for Traders, Credit Providers, Market Makers, and Liquidation Backstops](http://arxiv.org/abs/2608.00647v1)
  <details><summary>📄 Abstract</summary>
  A physically backed leveraged event position requires real credit: if collateral C receives leverage L, the protocol supplies (L-1)C and uses the combined amount to acquire recognized event exposure. This paper develops a venue-agnostic on-chain credit architecture for that capital layer and an endogenous model of its capital market. It separates traders, Senior Credit LPs, market makers, liquidators, and Liquidation Backstop Providers; formalizes pool and debt shares, utilization- and risk-sens...
  </details>

- **2026-08-01** — Yinlin Zhu, Di Wu, Yi Zhang et al. — [Towards Effective Federated Multimodal Graph Learning via Navigating Multifaceted Heterogeneity](http://arxiv.org/abs/2608.00623v1)
  <details><summary>📄 Abstract</summary>
  Multimodal-attributed graphs (MAGs), where nodes carry heterogeneous semantic content across multiple modalities while edges encode relational dependencies, have been widely adopted across diverse domains. Federated multimodal graph learning (FMGL) extends federated graph learning (FGL) to MAGs, enabling collaborative optimization across decentralized MAGs without exposing raw data. However, naively applying existing FGL methods to FMGL is insufficient, as they fail to navigate the multifaceted ...
  </details>

- **2026-08-01** — Qunhui Zhang — [AiFlow: Token-Native Reactive Orchestration with Bounded Backpressure for Streaming LLM Applications](http://arxiv.org/abs/2608.00558v1)
  <details><summary>📄 Abstract</summary>
  Large language model (LLM) applications increasingly operate as streaming workflows combining retrieval, tool calls, safety filters, and multi-agent coordination. Although contemporary frameworks expose provider deltas, workflow nodes often treat generation as coarse request-response steps, leaving queue management, worker allocation, ordering, and backpressure to ad hoc callback code. This paper presents AiFlow, a token-native reactive orchestration model that normalizes provider deltas into ty...
  </details>

- **2026-08-01** — Wendi Liu, Weichao Zeng, Weihang Ran et al. — [Optical Flow from Photons](http://arxiv.org/abs/2608.00499v1)
  <details><summary>📄 Abstract</summary>
  Optical flow remains challenging in high-speed and low-light scenes, where the limited frame rate and sensitivity of conventional cameras lead to motion blur and underexposure. Single-photon avalanche diode (SPAD) cameras offer single-photon sensitivity and extremely fine temporal sampling. However, individual slices in these high FPS binary photon streams are too sparse for dense correspondence. Temporal aggregation can provide the spatial cues required by optical flow, but accumulating photons...
  </details>

- **2026-08-01** — Ziqiang Cui, Han Shi, Bowei He et al. — [AdaMTP: An Adaptive Training Paradigm for Multi-Token Prediction](http://arxiv.org/abs/2608.00434v1)
  <details><summary>📄 Abstract</summary>
  Multi-Token Prediction (MTP) has emerged as an effective paradigm that augments a shared Large Language Model backbone with auxiliary heads, training the model to predict several future tokens in parallel to enrich its supervision signal and accelerate inference. However, existing training frameworks adopt a rigid, fixed-length prediction horizon, disregarding the highly non-uniform information density of natural language and code. Forcing the auxiliary heads to predict across high-entropy seman...
  </details>

- **2026-08-01** — Bikang Pan, Fan Liu, Haotao Lu et al. — [SelfWAM: A Self-Grounded Unified World Action Model for Fast Robot Control](http://arxiv.org/abs/2608.00725v1)
  <details><summary>📄 Abstract</summary>
  World Action Models (WAMs) improve robot policy learning by jointly modeling actions and future observations. However, conditioning future prediction only on the task prompt and observation context risks capturing generic task progression rather than the action-specific consequences of the executed action. We introduce SelfWAM, a unified self-grounded WAM built on a modality-specialized Mixture-of-Transformers (MoT) architecture that jointly predicts actions, action-conditioned future RGB frames...
  </details>

- **2026-08-01** — Tian Lan, Yemin Wang, Chuancheng Shi et al. — [A Heuristic Perspective on Debiasing Language Models](http://arxiv.org/abs/2608.00622v1)
  <details><summary>📄 Abstract</summary>
  Language models (LMs) often acquire various biases during pre-training and may express them in interactions, potentially causing social harm. Existing methods often rely on counterfactual augmentation or representation projection. These strategies remain limited in practice due to their high computational costs and difficulty in scaling to larger models. Additionally, many of these strategies require manual data annotation, narrowing their scope to specific cultures and bias categories. To overc...
  </details>

- **2026-08-01** — Pu Cao, Qingye Kong, Xuedan Yin et al. — [DrawAI: Agentic Benchmark and Workflow for Making Raster Images Editable](http://arxiv.org/abs/2608.00548v1)
  <details><summary>📄 Abstract</summary>
  Recent image-generation models and multimodal agents can produce high-quality visuals for increasingly complex visual communication tasks. Yet their raster outputs remain difficult to use directly because meaningful content and relationships are flattened into pixels, preventing users from inspecting, modifying, rearranging, or reusing individual components. We formulate image-to-editable reconstruction, which recovers a structured, directly manipulable artifact from a raster image while preserv...
  </details>

- **2026-08-01** — Zehao Wang, Yisen Xu, Chenglin Li et al. — [Turning Interaction History into Execution State: A Runtime Layer for Long-Horizon Coding Agents](http://arxiv.org/abs/2608.00808v1)
  <details><summary>📄 Abstract</summary>
  Long-horizon coding agents accumulate hundreds of actions and observations in their trajectories, yet nothing in this record indicates which observations still describe the repository as it currently stands. Before every decision, the model must implicitly infer the execution status from raw history, and when this inference falls short, the agent acts on outdated file contents or re-executes work whose results are still valid. We propose Ledger, a deterministic runtime layer that distills an age...
  </details>

- **2026-08-01** — Amin Izadyar — [AI and Exchange Rate Predictability](http://arxiv.org/abs/2608.00761v1)
  <details><summary>📄 Abstract</summary>
  I revisit the exchange rate disconnect puzzle, first documented by Meese and Rogoff (1983), using generative artificial intelligence (AI) to forecast currency returns based on economic fundamentals. Using ChatGPT and DeepSeek, I analyze a comprehensive dataset of economic data releases for major currency pairs and measure the fundamental strength of each currency. These AI-powered fundamentals exhibit significant cross-sectional predictive power. A simple trading strategy that goes long currenci...
  </details>

- **2026-08-01** — Jin Zhang, Linyu Li, Weili Jiang et al. — [TreeProbe : A Tibetan Medicine Benchmark for Cultural Bias in LLMs](http://arxiv.org/abs/2608.00640v1)
  <details><summary>📄 Abstract</summary>
  Large language models are increasingly viewed as a potential means of mitigating global health inequities, yet their outputs often reflect dominant high-resource medical traditions and provide limited coverage of traditional medical knowledge systems. Tibetan medicine, one of the world's four major traditional medical systems, has an independent and highly structured theoretical framework. When models lack grounded understanding of Tibetan medicine, they may fall back on dominant epistemic syste...
  </details>

- **2026-08-01** — Haibo Tang, Linqi Zhang, Hongxin Huan et al. — [EmergencyBias: Bias in Text-to-Image Models under Emergency Scenarios](http://arxiv.org/abs/2608.00598v1)
  <details><summary>📄 Abstract</summary>
  Bias in Text-to-Image (T2I) generation has become an important problem in multimedia content creation and communication. However, existing studies have primarily focused on relatively static and explicit forms of bias, such as disparities in the representation of gender, race, and geo-cultural attributes. Less attention has been paid to behavioral bias in how different groups are portrayed acting, reacting, and occupying social roles. Emergency scenarios provide a revealing setting for studying ...
  </details>

- **2026-08-01** — Jingtong Chen, Jiahui Wang, Xue Zhao et al. — [Element-Aware Group Learning for E-Commerce Image Generation](http://arxiv.org/abs/2608.00584v1)
  <details><summary>📄 Abstract</summary>
  Recent advances in image generation and editing have made prompt quality a key bottleneck for e-commerce creatives. Vision-language models (VLMs) can generate image-editing prompts from product images and metadata, but further improving their prompt-writing capabilities requires post-training with feedback from the generated images. Group Relative Policy Optimization (GRPO) is a natural framework for such outcome-level reward optimization. However, it assigns credit only at the full-prompt level...
  </details>

- **2026-08-01** — Shalom Kachko, Raz Lapid, Margarita Vald et al. — [Through the LENS: Local Geometric Decomposition of Vision-Language Model Representations](http://arxiv.org/abs/2608.00561v1)
  <details><summary>📄 Abstract</summary>
  Vision-language models (VLMs) process image patches and text tokens in a shared residual stream, but the local geometry through which the two modalities interact remains poorly understood. Most interpretability methods identify global linear directions, which may miss representations that are globally high-dimensional but locally low-dimensional. We introduce LENS (Local Explanation of Neighborhood Subspaces), a method that decomposes VLM activations into local low-rank Gaussian neighborhoods us...
  </details>

- **2026-08-01** — Joseph Tafese, Milad Hooshyar, Sam Bayless et al. — [Verifiable Checks for Business Rule Consistency](http://arxiv.org/abs/2608.00396v1)
  <details><summary>📄 Abstract</summary>
  Maintaining consistency between natural language documentation of business rules and their evolving internal implementations is a significant challenge in large-scale systems. We present SIRNA, a tool and framework for checking such consistency using SMT solvers. Using the case study of cost calculations in tax domains, we demonstrate a three-part system that combines large language models (LLMs) with formal verification methods. SIRNA translates natural language documentation into candidate SMT...
  </details>

- **2026-07-31** — Ismayil Ismayilov, Atakan Kara, Kaan Oktay — [DungeonBench: A Benchmark for Rules-Rich Tactical Reasoning in Dungeons & Dragons Combat](http://arxiv.org/abs/2607.29577v1)
  <details><summary>📄 Abstract</summary>
  Games and simulators make valuable benchmarks by turning decisions into measurable outcomes, but many current suites under-test rules-rich tactical reasoning: the ability to choose well when geometry, timing, resources, objectives, and rule interactions all matter at once. We introduce DungeonBench, a benchmark for tactical reasoning in Dungeons & Dragons combat, built to cover the vast majority of combat-relevant 2014 System Reference Document content whose effects can be resolved by the simula...
  </details>

- **2026-07-31** — Manith Adikari, Bei Peng, Samuele Vinanzi et al. — [LEMUR: Learning to Align with Multi-Objective Reinforcement Learning from Preference Feedback](http://arxiv.org/abs/2607.29559v1)
  <details><summary>📄 Abstract</summary>
  Reinforcement Learning (RL) systems are typically trained using a single, well-specified scalar reward function. However, real-world decision-making tasks often involve multiple, competing objectives, such as performance versus efficiency, where ground-truth reward functions are difficult to specify or inaccessible. While Multi-Objective RL (MORL) addresses such trade-offs by modeling rewards as vectors, existing approaches typically assume access to a well-specified reward function for each obj...
  </details>

- **2026-07-31** — Sebastian Doerrich, Daniel Würtinger, Francesco Di Salvo et al. — [MoPET: Parameter-Efficient Mixture-of-Experts for Unified Medical Image Classification](http://arxiv.org/abs/2607.29462v1)
  <details><summary>📄 Abstract</summary>
  Adapting deep learning models to profound clinical heterogeneity typically relies on parameter-efficient fine-tuning (PEFT) to avoid the severe overfitting associated with full end-to-end network updates. Although PEFT successfully navigates limited data scenarios, it inherently forces the training of a separate, isolated adapter for every specific diagnostic task. Consolidating these isolated adapters into a single generalist network risks negative transfer, as optimization gradients from confl...
  </details>

- **2026-07-31** — Zhaoxin Feng, Jianfei Ma, Emmanuele Chersoni — [Know It, Act on It: Investigating Memory Utilization in LLM Personalization](http://arxiv.org/abs/2607.29433v1)
  <details><summary>📄 Abstract</summary>
  As large language model (LLM) agents evolve into personalized companions, memory has emerged as a core capability. However, LLMs face a knowledge utilization problem: they may fail to act on relevant user preferences even when they are fully present in context. When an agent fails to tailor its response in a context where previously shared user preferences should matter, it is unclear whether the model failed to remember that information or remembered it but failed to use it. To isolate this bre...
  </details>

- **2026-07-31** — James Hsin-yu Chiang, Sheila Zingg, Kari Kostiainen et al. — [MOSAIC: Masked Outsourcing of Secure AI Computations](http://arxiv.org/abs/2607.29221v1)
  <details><summary>📄 Abstract</summary>
  We address the challenge of securely and efficiently outsourcing AI computations from a trusted but computationally weak client to an untrusted but powerful server, in the setting where the client holds both the input and the model, and the server must learn neither. We present MOSAIC, whose core is a novel matrix-multiplication masking protocol that scales to far larger matrices than prior work, enabling the safe outsourcing of modern workloads such as large transformer inference. By introducin...
  </details>

- **2026-07-31** — Zilong Chen, Chaorui Deng, Kunchang Li et al. — [Scaling Properties of Text Conditioning in Visual Generation](http://arxiv.org/abs/2607.29679v1)
  <details><summary>📄 Abstract</summary>
  We study empirical scaling properties for text conditioning in visual generation. Such properties have rarely been measured because diffusion loss does not scale with the number of tokens in natural-language prompts. Surprisingly, we find that the converged diffusion loss scales with the amount of structured language in the prompt. To quantify structured language, we adapt two complementary measures: a white-box likelihood metric (GPG) and a black-box attribute metric (ED). Across controlled tra...
  </details>

- **2026-07-31** — Tianyu Huai, Tingshuo Fan, Xinchi Chen et al. — [AgentHPOBench: A Benchmark For Evaluating LLM Agents as Sequential Hyperparameter Optimizers](http://arxiv.org/abs/2607.29626v1)
  <details><summary>📄 Abstract</summary>
  As LLMs evolve from code completion systems into autonomous scientific agents, evaluating their ability to conduct experiments has become increasingly important. Existing benchmarks typically focus on static code generation, paper replication, or final answer correctness, but do not directly assess whether agents can interpret experimental evidence and use it to guide subsequent hyperparameter decisions. To address this gap, we introduce AgentHPOBench, a sequential benchmark comprising 30 execut...
  </details>

- **2026-07-31** — Luca Viano, Antoine Moulin, Audrey Huang et al. — [When Does On-Policy Interaction Help? Representational Tradeoffs in Value-Based Imitation Learning](http://arxiv.org/abs/2607.29617v1)
  <details><summary>📄 Abstract</summary>
  Imitation learning (IL)---training an agent to replicate expert behavior from demonstrations---underpins applications from robotics to language model training. Standard approaches such as Behavior Cloning (BC) are known to suffer from compounding errors and performance plateaus, particularly when the learner cannot perfectly represent the expert's policy (as is typical, e.g., in distillation). Two interventions are widely understood empirically to improve performance: querying the expert interac...
  </details>

- **2026-07-31** — Pol G. Recasens, Ferran Agullo, Yue Zhu et al. — [SLIM: Saturation-Aware Lightweight Performance Modeling for LLM Serving](http://arxiv.org/abs/2607.29575v1)
  <details><summary>📄 Abstract</summary>
  Large language model (LLM) serving commonly increases batch size to improve throughput, but performance eventually reaches a deployment-dependent plateau beyond which larger batches provide marginal gains while increasing latency and GPU memory consumption. Previous studies have attributed this behavior to HBM/DRAM bandwidth limitations, but the underlying causes have primarily been supported by conceptual arguments or high-level performance observations. As our first contribution, we present a ...
  </details>

- **2026-07-31** — Boxiao Wang, Runxiang Wang, Kai Li et al. — [MOT-SR: Multi-Objective Tool-Augmented Scientific Equation Discovery with Large Language Models](http://arxiv.org/abs/2607.29561v1)
  <details><summary>📄 Abstract</summary>
  Symbolic Regression (SR) aims to discover analytical equations from observational data and plays a central role in scientific modeling. While recent Large Language Model (LLM) based approaches show promise, they face two limitations. First, they lack data analysis mechanisms for uncovering variable dependencies, which reduces the efficiency of equation discovery. Second, most methods rely on single-objective evaluation focused solely on fitting error. This neglect of structural complexity and ge...
  </details>

- **2026-07-31** — Ningzhi Liu, Yannic Hinrichs, Jonas R. Kunst — [The persuasive power of large language models does not depend on their perceived national origin](http://arxiv.org/abs/2607.29334v1)
  <details><summary>📄 Abstract</summary>
  Conversational AI developed by geopolitical rivals reaches citizens worldwide, raising concerns that it could sway public opinion or be rejected as foreign propaganda, with consequences for democratic discourse and information sovereignty. Yet, whether an AI's perceived national origin shapes its persuasive power is unknown. In a preregistered randomized experiment, 403 adults from a nationally representative United States sample held a three-round debate with a chatbot introduced as either Amer...
  </details>

- **2026-07-31** — Didier Henrion, Jean B Lasserre — [Volume of quasi-homogeneous sublevel sets: Two linear algebra deterministic algorithms with convergence rates](http://arxiv.org/abs/2607.29269v1)
  <details><summary>📄 Abstract</summary>
  We consider the problem of computing the Lebesgue volume of the unit sublevel set of a positive quasi-homogeneous polynomial. Pushing the Lebesgue measure of an ambient bounding box forward through the polynomial reduces this high-dimensional volume to a one-dimensional moment problem. This removes the ambient dimension from the optimization and confines the dimension to a single preprocessing stage, computing the moments of the polynomial over the box, which is polynomial in the ambient dimensi...
  </details>

- **2026-07-31** — Mathias Dus — [Radon Measure Representations for Infinite-Width Neural Networks with Singular Activations](http://arxiv.org/abs/2607.29258v1)
  <details><summary>📄 Abstract</summary>
  The theoretical foundation of infinite-width shallow neural networks relies heavily on continuous integral representations and Barron spaces. Recently, harmonic analysis-specifically the Radon and Ridgelet transforms-has emerged as a powerful tool to invert these representations and compute the optimal network weights. However, a major analytical bottleneck remains: standard neural network activation functions exhibit severe spectral singularities at the frequency origin. To bypass this divergen...
  </details>

- **2026-07-30** — Cesare Zavattari, Alessandro Tommasi, Giuseppe Prencipe — [One Human, $N$ Agents: Audit-Budget Allocation for LLM Agent Fleets under Miscalibrated, Correlated Confidence](http://arxiv.org/abs/2607.28317v1)
  <details><summary>📄 Abstract</summary>
  A single human must audit $N$ LLM agents under a budget of $B \ll N$ audits per round, guided by self-reported confidence that may be adversarially miscalibrated and by correlated errors. We model this as budgeted noisy inspection over a two-level Gaussian copula and locate the miscalibration threshold $δ^*$ past which confidence-ranked auditing is \emph{worse} than random. Two a-priori expectations reverse: $δ^*$ \emph{rises} as the budget shrinks, and cross-family correlation is not low---shar...
  </details>

- **2026-07-30** — Niklas Bauer, Lars Benedikt Kaesberg, Akiko Aizawa et al. — [Can Agents Deceive? Evaluating Reasoning and Deception in ParliamentBench using a Social Deduction Game](http://arxiv.org/abs/2607.28146v1)
  <details><summary>📄 Abstract</summary>
  As large language models (LLMs) are deployed as agents in high-stakes settings, such as medical and legal systems, understanding their deceptive capabilities is fundamental to safety. Controlled social deduction games provide a reproducible proxy for isolating and evaluating these complex adversarial behaviors. We present the open-source benchmark framework ParliamentBench based on the game Secret Hitler to evaluate LLMs in scenarios that require deception, persuasion, and reasoning under inform...
  </details>

- **2026-07-30** — Muhammad Laiq — [A comparative analysis of automated techniques for security bug report identification](http://arxiv.org/abs/2607.27893v1)
  <details><summary>📄 Abstract</summary>
  Timely identification of security-related bug reports is essential to minimize the window of vulnerabilities in software systems. Manually screening incoming bug reports to identify security-related issues is time-consuming, error-prone, and non-scalable for large-scale software systems. Thus, a variety of automatic techniques, including traditional machine learning (ML) techniques and large language models, have been proposed to facilitate this task. However, the literature remains fragmented. ...
  </details>

- **2026-07-30** — Vishwajith Ramesh — [Subtract or Replay? Exact Deletion from Language-Model Memory](http://arxiv.org/abs/2607.27539v1)
  <details><summary>📄 Abstract</summary>
  Exact deletion from persistent language-model memory depends on how that memory represents a record. Addressable influence can be removed by algebraic decrement; influence transformed by later writes inside shared recurrent state requires rebuilding from before the write. We test this distinction in two pretrained models against explicit record-omitted references. First, we replace Gemma 3's global-attention layers with support-vector memory. After low-rank recovery at 1B, decrement and retained...
  </details>

- **2026-07-30** — Yukang Cao, Haozhe Xie, Beichen Wen et al. — [ACE-Data-0: Human-Centric Ambient Capture as Embodied Data Engine](http://arxiv.org/abs/2607.28625v1)
  <details><summary>📄 Abstract</summary>
  Embodied intelligence faces a fundamental data bottleneck. Models must capture how first-person perception, whole-body motion, dexterous manipulation, object state, sound, and touch evolve together as humans pursue goals over time. Existing datasets fragment this experience across viewpoints, modalities, or spatial scales, leaving the full perception-action loop only partially observed. We introduce the Ambient Capture Engine (ACE), a human-centric data engine that transforms real home environme...
  </details>

- **2026-07-30** — Haomin Qi, Xingliang Wang, Xuanqi Gao et al. — [Change2Task: From Repository Changes to Executable Coding Agent Tasks and Environments](http://arxiv.org/abs/2607.28591v1)
  <details><summary>📄 Abstract</summary>
  Scaling coding agents requires a continuing supply of executable data for training, benchmarking, and continuous evaluation. Each task must couple a realistic software state with a specification, development tools, and reliable verification. To expand this supply, we present Change2Task, a system grounded in repository history that converts merged pull requests into verified tasks on healthy modern revisions of the same repository. It aligns historical evidence with evolved code, reconstructs ta...
  </details>

- **2026-07-30** — Jiawei Xu, Minghui Liu, Juzheng Zhang et al. — [$β$-OPSD: Deriving with Policy Optimization, Training with Self-Distillation](http://arxiv.org/abs/2607.28582v1)
  <details><summary>📄 Abstract</summary>
  On-policy self-distillation (OPSD) is a promising approach to improve reasoning language models, but it remains brittle in practice: making it work reliably often requires substantial engineering effort. We identify a structural source of this difficulty: vanilla OPSD is precisely the $β=1$ member of a broader policy-optimization family, where $β$ weights the KL penalty anchoring the student to a reference policy. This equivalence turns $β$ from an implicit value fixed at one into a controllable...
  </details>

- **2026-07-30** — Junlin Yang, Che Jiang, Yu Fu et al. — [Frontis-MA1: Training an AI4AI Model towards Recursive Self-Improvement in Machine Learning Engineering](http://arxiv.org/abs/2607.28568v1)
  <details><summary>📄 Abstract</summary>
  Recursive self-improvement (RSI) requires AI systems that improve the process of building AI (i.e., AI4AI); machine learning engineering (MLE) offers a concrete, executable testbed for studying this capability. We introduce OpenMLE, an open full-stack system for RSI research in MLE, spanning verifiable task environments with execution feedback (OpenMLE-Gym), operator learning (OpenMLE-RL), and long-horizon search (OpenMLE-Evo). On this stack we post-train Frontis-MA1 (35B) as a meta-evolution ag...
  </details>

- **2026-07-30** — Xiaobei Zhao, Xingqi Lyu, Xin Chen et al. — [TEA-AgriVLN: Traversability Estimation Alarm for Agricultural Vision-and-Language Navigation](http://arxiv.org/abs/2607.28474v1)
  <details><summary>📄 Abstract</summary>
  Vision-and-Language Navigation in Continuous Environments (VLN-CE) requires an agent to follow a natural language instruction, predicting a sequence of low-level actions to navigate a robot from a starting point to a target location. The A2A benchmark and the AgriVLN method pioneeringly extended VLN-CE from indoor scenes to agricultural scenes, while we observed a challenging distinction: In indoor scenes, whether a zone is traversable tends to be clear to classify, such as wood floors are trave...
  </details>

- **2026-07-30** — Zheng Wu, Yibo Luo, Pu Zhang et al. — [Beyond a Single Judge: Simulating Social Persona Panels for Generative UI Evaluation](http://arxiv.org/abs/2607.28439v1)
  <details><summary>📄 Abstract</summary>
  Generative UI (GenUI) lets large language models synthesize a complete, renderable interface directly from a natural-language instruction, but evaluating the quality of what they generate remains an open problem. Human evaluation is costly and rater-variant, while LLM-as-a-judge is scalable but reflects only a single implicit viewpoint, unable to capture how different populations of real users actually perceive the same interface. We propose the Evidence-Grounded, Social-Weighted Persona Panel (...
  </details>

- **2026-07-30** — Ankur Naskar, Vaneet Aggarwal — [Hierarchical Multilevel Monte Carlo for Order-Optimal Neural Actor-Critic in Average-Reward CMDPs](http://arxiv.org/abs/2607.28390v1)
  <details><summary>📄 Abstract</summary>
  Constrained Markov Decision Processes (CMDPs) provide a natural framework for reinforcement learning in safety-critical applications, where agents maximize long-term reward while satisfying long-term constraints. Although primal-dual actor-critic methods with linear critics are well understood, extending order-optimal convergence guarantees to neural critics in average-reward CMDPs has remained open. The main challenge is a fundamental bias-cost trade-off in neural critic estimation: under Neura...
  </details>

- **2026-07-30** — Zixuan Jiang, Binghao Qiang, Jiaying Chi et al. — [AgenticASR: Refining Speech Recognition in Real-World Scenarios via an Agentic Approach](http://arxiv.org/abs/2607.28175v1)
  <details><summary>📄 Abstract</summary>
  Automatic speech recognition (ASR) has achieved substantial gains in transcription accuracy, yet verbatim transcription does not necessarily produce readily usable text. It retains fillers, repetitions, false starts, and self-corrections that increase reading effort, obscure the speaker's final intent, and propagate unresolved or abandoned content to downstream tasks. Existing spoken-to-written methods process completed audio or transcripts but cannot revise emitted text when later speech change...
  </details>

- **2026-07-30** — Hail Song, Seokhwan Yang, Jiwon Yang et al. — [S-Avatar: Diffusion-Guided Gaussian Head Avatars from a Single Image](http://arxiv.org/abs/2607.28164v1)
  <details><summary>📄 Abstract</summary>
  We propose S-Avatar, a novel method for generating photorealistic 3D head avatars from a single image using a diffusion-guided 3D model generation module and strategies for animating 3D Gaussian Splatting (3DGS). While single-image head avatar reconstruction is crucial for lifelike Virtual Reality (VR) applications, existing approaches often struggle to preserve 3D consistency under unseen viewpoints. S-Avatar addresses this limitation through a three-stage pipeline. First, a high-resolution 3DG...
  </details>

- **2026-07-30** — Giorgos Iacovides, Wuyang Zhou, Danilo Mandic — [FinSMART: Financial Sentiment Analysis for Algorithmic Trading through Market-Aligned Reinforcement Learning](http://arxiv.org/abs/2607.28127v1)
  <details><summary>📄 Abstract</summary>
  Recent advances in Generative AI have substantially improved financial sentiment analysis through post-trained financial large language models (LLMs). However, existing approaches remain confined to a market-agnostic, supervised learning paradigm that relies on limited, static and human-annotated datasets, and thus are incapable of adapting to evolving market conditions. To address this limitation, we introduce FinSMART, the first market-aligned reinforcement learning framework for financial sen...
  </details>

- **2026-07-30** — Jiawen Tao, Miao Peng, Yaoming Li et al. — [Beyond Rephrasing: Book-Level Organization Improves Synthetic Textbook Data for Mid-Training](http://arxiv.org/abs/2607.28109v1)
  <details><summary>📄 Abstract</summary>
  Synthetic textbook data has improved language model pre-training, but prior work largely treats the benefit as a property of generated content or local rewriting style. We study a different factor: whether related content is organized into coherent book-level documents. We contribute both a scalable synthesis pipeline and controlled evidence that this organization matters. The pipeline retrieves source material from a pre-training corpus, clusters it into topical units, plans hierarchical tables...
  </details>

- **2026-07-30** — Binbin Zheng, Zijun Xie, Guanqun Zhao et al. — [Group-Reflective Self-Distillation for Agentic Reinforcement Learning](http://arxiv.org/abs/2607.28076v1)
  <details><summary>📄 Abstract</summary>
  Reinforcement learning with verifiable rewards (RLVR) is effective for training large language model agents. However, terminal rewards provide only coarse trajectory-level supervision, leaving successful behaviors, recurring mistakes, and incidental choices entangled in the same outcome signal. Existing agentic self-distillation methods enrich sparse supervision with natural-language skills, but skills retrieved externally or extracted from a single trajectory by stronger models may mismatch cur...
  </details>

- **2026-07-30** — Jesús Gacías Franco — [The Euler Characteristic Transform from a Convex Geometric Perspective](http://arxiv.org/abs/2607.28021v1)
  <details><summary>📄 Abstract</summary>
  By examining the relationship between the support function of convex geometry and the Euler Characteristic Transform (ECT) of topological data analysis, we develop new tools and suggest variations on some common ECT pipelines. Specifically, we put forward new definitions of ECT-induced pseudodistances, which have the advantage of being invariant under common euclidean isometries and require no cutoff parameter to compare shapes with distinct Euler characteristic. These definitions rely on a gene...
  </details>

- **2026-07-30** — Xu Xia, Jinghua Piao, Min Yang et al. — [From Scoring to Acting: Outcome-Verified Comparative Self-Distillation for LLM Agents](http://arxiv.org/abs/2607.27937v1)
  <details><summary>📄 Abstract</summary>
  Recent work on LLM agents is shifting from external capability elicitation to capability internalization, enabling agents to retain useful skills without retrieval at inference time. On-policy self-distillation (OPSD) offers a promising direction, but many existing methods typically supervise students by scoring actions along student-generated trajectories. Such supervision has two limitations: teacher preferences are not validated by environment outcomes, and action-level scores underuse inform...
  </details>

- **2026-07-30** — Qiangqiang He, Zhongheng Wu, ZiJian Wang — [Not All Tokens Deserve Equal Credit: Counterfactual Sensitivity Credit Reallocation for Long-CoT Reasoning](http://arxiv.org/abs/2607.27888v1)
  <details><summary>📄 Abstract</summary>
  Reinforcement learning with verifiable rewards (RLVR) is central to improving long-CoT reasoning in large language models. Critic-free methods such as GRPO convert response-level rewards into advantages and uniformly broadcast them across tokens, overlooking their unequal contributions to the final outcome. On-policy self-distillation (OPSD) instead provides dense distributional supervision by minimizing the forward KL divergence between an unprivileged policy and a privileged self-teacher, impl...
  </details>

- **2026-07-30** — Lanhao Zhao — [On the Strong Structural Controllability of Matrix-Weighted Networks](http://arxiv.org/abs/2607.27852v1)
  <details><summary>📄 Abstract</summary>
  This paper investigates the strong structural controllability of multi-agent networks. Based on the definition of equitable partitions, an upper bound for the strong structural controllable subspace (SSCS) is established. To reflect the physical significance of matrix weights where the state dimension is greater than one, the multi-agent system is modeled using higher-order dynamics. Furthermore, to address matrix singularity and asymmetric couplings, a matrix space basis decomposition method is...
  </details>

- **2026-07-30** — Yuhang Zhu, Mingxuan Du, Benfeng Xu et al. — [Beyond Borrowed Histories: Person-Aligned User Simulation for Interactive Role-Playing Evaluation](http://arxiv.org/abs/2607.27816v1)
  <details><summary>📄 Abstract</summary>
  Role-playing agents (RPAs) have become one of the most important consumer applications of large language models. Users engage in multi-turn conversations with RPAs for experiences such as emotional comfort, making reliable evaluation essential for measuring capability, comparing systems, and guiding further improvement. Existing benchmarks, however, typically require an RPA to continue a fixed dialogue history and then evaluate the continuation using a fixed rubric detached from the user. We ide...
  </details>

- **2026-07-30** — Wei Chen, Junkai Li, Tongguan Wang et al. — [Semantic-Aligned Structural Abstraction for Multimodal Sentiment Analysis](http://arxiv.org/abs/2607.27790v1)
  <details><summary>📄 Abstract</summary>
  Multimodal Sentiment Analysis (MSA) aims to interpret complex human emotions by integrating natural language with non-verbal modalities. Non-verbal modalities share a structural isomorphism with natural language, as both can be viewed as feature sequences evolving over time. This isomorphism enables the transformation of non-verbal modalities into text-like tokens for unified semantic reasoning. Large Language Models (LLMs), designed to understand and generate sequential data, can thus be utiliz...
  </details>

- **2026-07-30** — Xiao Tan, Cynthia Sturton — [CHARGE: Leveraging CWE Hierarchies for Hardware Security SystemVerilog Assertion Generation](http://arxiv.org/abs/2607.27776v1)
  <details><summary>📄 Abstract</summary>
  This paper presents CHARGE, an automated framework for generating security properties for unverified RTL modules using CWEs and large language models (LLMs). The hallmark is a reasoning process that leverages the hierarchical nature of CWE entries to improve accuracy when identifying security-critical assets in unverified RTL modules. As a result, the approach can infer expected security behaviors and generate properties from identified assets and CWE semantics, avoiding the need for trusted des...
  </details>

- **2026-07-30** — Argyrios Deligkas, Michail Fasoulakis, Stavros D. Ioannidis et al. — [Delegated Fair Division](http://arxiv.org/abs/2607.27743v1)
  <details><summary>📄 Abstract</summary>
  Motivated by recently introduced problems on delegated resource allocation, we study a model of fair division, where a set of indivisible goods is to be allocated to some agents, each of which belonging to some bigger central entity. Our model captures the general framework of allocating resources to organizational units, which subsequently distribute them to their affiliated members. A particularly relevant application of this framework, with immense social impact, arises in the allocation of f...
  </details>

- **2026-07-30** — Sangmin Hong, Daniel Sungho Jung, Heewon Kim et al. — [PrintAnything: Learning an Intermediate Representation for 3D printing G-code Generation](http://arxiv.org/abs/2607.27729v1)
  <details><summary>📄 Abstract</summary>
  Point clouds are one of the most fundamental and widely used 3D representations, serving as the most basic geometric representation of 3D shapes. Nevertheless, most existing 3D printing pipelines require a watertight mesh as input, preventing the direct use of point clouds for fabrication. A common workaround is to reconstruct meshes from point clouds; however, the resulting meshes often contain geometric artifacts, such as incorrect faces or topological inconsistencies, that are difficult to re...
  </details>

- **2026-07-30** — Angshuman Chakravertty, Rahul Maheshwari — [VESTIGE: A Knowledge-Guided Masking Strategy for Corruption-Aware Fine-Tuning of Genomic Transformers, Validated on Ancient DNA Reconstruction](http://arxiv.org/abs/2607.27712v1)
  <details><summary>📄 Abstract</summary>
  Standard masked-language-model fine-tuning applies a uniform masking probability across every token position, assuming reconstruction difficulty is position-agnostic. When the degradation process is characterised and concentrated at predictable positions, this assumption fails: at peak damage sites the model can underperform a frequency-matched random predictor. We introduce VESTIGE, a parameter-free, drop-in replacement for the standard MLM collator that aligns the masking distribution with an ...
  </details>

- **2026-07-30** — Shaobo Liu, Feiqiao Mao, Shuaishuai Zhou et al. — [RefineSVG: Visual Feedback-Driven Reinforcement Learning for Image-to-SVG Generation](http://arxiv.org/abs/2607.27699v1)
  <details><summary>📄 Abstract</summary>
  We propose RefineSVG, a single-step closed-loop visual feedback framework that enables multimodal large language models (MLLMs) to perform high-fidelity image-to-SVG generation through self-correction. Existing MLLM-based approaches rely on single-pass open-loop inference, where the model receives visual input only once and must generate thousands of SVG code tokens without intermediate verification. This paradigm inevitably leads to geometric drift, error accumulation, and visual hallucination ...
  </details>

- **2026-07-30** — Sangjin Kim, Yuseon Choi, Byeongcheol Kim et al. — [GyRot: Leveraging Hidden Synergy between Rotation and Fine-grained Group Quantization for Low-bit LLM Inference](http://arxiv.org/abs/2607.27694v1)
  <details><summary>📄 Abstract</summary>
  Low-bit quantization is essential for efficient LLM inference, and both rotation and fine-grained group quantization have shown individual promise. However, their combination often leads to accuracy degradation or hardware overhead due to a mismatch between the global nature of rotation and the localized behavior of group scaling. We propose GyRot, a quantization framework and hardware accelerator that bridges this gap through algorithm-hardware co-design. GyRot introduces Coarse Rotation, Fine ...
  </details>

- **2026-07-30** — Jingya Wang, Yuyang Gao, Liuzhenghao Lv et al. — [LabEvolver: Training-Free Experience Evolution for Safe and Grounded Wet-Lab Agents](http://arxiv.org/abs/2607.27690v1)
  <details><summary>📄 Abstract</summary>
  We introduce LabEvolver, a training-free framework that equips safe and grounded wet-lab agents with episodic memory from execution experience. LabEvolver couples a state-grounded inner trial loop for adaptive perception, online planning, and safety validation with an outer evolution loop that distills completed trajectories into reusable skill, strategy, and safety experience. On robotic solution-preparation tasks, LabEvolver demonstrates real-world feasibility, reducing pH-regulation completio...
  </details>

- **2026-07-30** — Bowen Shen — [Can Large Language Models Resolve Real Java Merge Conflicts? An Evaluation with a Calibrated LLM-as-Judge](http://arxiv.org/abs/2607.27674v1)
  <details><summary>📄 Abstract</summary>
  Merge conflicts are a recurring cost of collaborative software development, and the traditional structured and semi-structured merge tools that address them frequently abstain: when their heuristics do not apply, they leave the conflict unresolved. Large language models (LLMs) can instead produce a candidate resolution for almost any conflict, but measuring whether those resolutions are actually good at scale is hard, because obtaining human desirability judgments for every model output does not...
  </details>


## 📊 统计 / Statistics

| 分类 / Category | 论文数 / Count |
|------|--------|
| jailbreak | 559 |
| prompt-injection | 467 |
| memory-poisoning | 40 |
| tool-use-attack | 95 |
| backdoor | 399 |
| adversarial-attack | 542 |
| privacy-leakage | 3735 |
| steganography | 54 |
| misuse | 845 |
| red-teaming | 110 |
| vulnerability | 2533 |
| defense | 2199 |
| alignment | 2030 |
| robustness | 1969 |
| watermark | 231 |
| unlearning | 84 |
| agent-safety | 52 |
| benchmark | 53 |
| survey | 261 |
| other | 5775 |

---

📚 **全部 22033 篇论文**（2022 至今）请访问 [GitHub Pages](https://ny1024.github.io/AgentSafety-Papers/) 查看完整列表、搜索与筛选。

*Generated by AgentGuard at 2026-08-04 08:28:56*