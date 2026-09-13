<div align="center">

# AgentGuard 🛡️

**Daily Tracking of LLM Agent Security Papers on arXiv**

[![Auto Update](https://github.com/NY1024/AgentSafety-Papers/actions/workflows/daily-update.yml/badge.svg)](https://github.com/NY1024/AgentSafety-Papers/actions/workflows/daily-update.yml)
[![Papers](https://img.shields.io/badge/Papers-27368-blue)](#)
[![License](https://img.shields.io/badge/License-MIT-green)](#)

</div>

---

## 📖 简介 / Introduction

自动追踪 arXiv 上大模型 Agent 安全方向的最新论文，每日更新，关键词智能分类。

*Automatically tracking the latest LLM Agent security papers on arXiv, updated daily with keyword-based classification.*

**最近更新 / Last Updated**: 2026-09-13 11:16 ｜ **论文总数 / Total Papers**: 27368（近 30 天 / Recent 30 days: 3690）

🌐 **[GitHub Pages](https://ny1024.github.io/AgentSafety-Papers/)** — 查看全部 27368 篇论文（含摘要、分类筛选、搜索）/ View all 27368 papers with abstracts, filters & search

## 📑 分类导航 / Category Navigation

- **[jailbreak](#-jailbreak)** — 越狱攻击 / Jailbreak Attacks — 625
- **[prompt-injection](#-prompt-injection)** — 提示注入攻击 / Prompt Injection Attacks — 534
- **[memory-poisoning](#-memory-poisoning)** — 记忆投毒与篡改 / Memory Poisoning & Tampering — 49
- **[tool-use-attack](#-tool-use-attack)** — 工具使用攻击 / Tool-Use Attacks — 134
- **[backdoor](#-backdoor)** — 后门与投毒攻击 / Backdoor & Poisoning Attacks — 451
- **[adversarial-attack](#-adversarial-attack)** — 对抗攻击 / Adversarial Attacks — 589
- **[privacy-leakage](#-privacy-leakage)** — 隐私泄露 / Privacy Leakage — 4064
- **[steganography](#-steganography)** — 隐写与隐蔽通信 / Steganography & Covert Communication — 64
- **[misuse](#-misuse)** — 滥用与误用 / Misuse & Abuse — 1004
- **[red-teaming](#-red-teaming)** — 红队测试 / Red Teaming — 123
- **[vulnerability](#-vulnerability)** — 漏洞与攻击面 / Vulnerabilities & Attack Surfaces — 3042
- **[defense](#-defense)** — 防御与防护方法 / Defense & Protection Methods — 2840
- **[alignment](#-alignment)** — 对齐与安全约束 / Alignment & Safety Constraints — 2647
- **[robustness](#-robustness)** — 鲁棒性与可靠性 / Robustness & Reliability — 2749
- **[watermark](#-watermark)** — 水印与溯源 / Watermarking & Provenance — 416
- **[unlearning](#-unlearning)** — 机器遗忘 / Machine Unlearning — 95
- **[agent-safety](#-agent-safety)** — Agent 安全框架 / Agent Safety Frameworks — 54
- **[benchmark](#-benchmark)** — 安全评测与基准 / Safety Benchmarks & Evaluation — 65
- **[survey](#-survey)** — 综述与系统化 / Surveys & Systematization — 339
- **[other](#-other)** — 其他安全相关 / Other Security-Related — 7484

## 📄 近期论文 / Recent Papers (Last 30 Days)

> 仅展示最近 30 天中最新的 500 篇论文（含日期、作者、摘要）。近 30 天共 3690 篇，完整 27368 篇论文列表请访问 [GitHub Pages](https://ny1024.github.io/AgentSafety-Papers/)

> Showing the latest 500 of 3690 papers from the last 30 days (with date, authors & abstract). For the full list of 27368 papers, visit [GitHub Pages](https://ny1024.github.io/AgentSafety-Papers/)

### 📂 jailbreak
*越狱攻击 / Jailbreak Attacks* — 6 papers

- **2026-09-09** — Jinyang Li, Mingyu Guo, Hung X. Nguyen — [CS-Guard: Benchmarking LLM Guardrails for Code Generation Security](http://arxiv.org/abs/2609.09798v1)
  <details><summary>📄 Abstract</summary>
  Large language models (LLMs) have been ex- ploited to generate malware, but the effective- ness of guardrails for code generation secu- rity remains unclear. We introduce CS-Guard, the first benchmark to systematically evalu- ate guardrails for code generation security. It covers 1) text-to-code generation with 1000 high-quality malware-generation prompts, 7 jailbreak attacks, and a novel fictional scenario attack (FSA) that embeds malicious intent in a legitimate fictional software-development ...
  </details>

- **2026-09-09** — Thomas Rivasseau — [Arbitrary Cipher Attacks Against Large Language Models Do Not Require Fine-Tuning](http://arxiv.org/abs/2609.09553v1)
  <details><summary>📄 Abstract</summary>
  Large language model safety and security research is preoccupied with, among other things, detecting and preventing jailbreak attacks: alignment bypasses that allow an adversarial user to elicit unwanted or harmful outputs from models. Arbitrary cipher, or covert communication, attacks are one such type of jailbreak and have previously been demonstrated against the fine-tuning APIs of commercial models. In these attacks, target models are trained on a corpus of encrypted harmful questions and re...
  </details>

- **2026-09-08** — Xu Zhang, Dev Mistry, Xiang Xu et al. — [Understanding In-Context Multimodal Jailbreaks via Posterior Reweighting](http://arxiv.org/abs/2609.10613v1)
  <details><summary>📄 Abstract</summary>
  In-context learning (ICL) jailbreaks reveal a critical vulnerability in multimodal large language models (MLLMs): harmful demonstrations in the prompt can induce unsafe outputs without modifying model parameters. Despite extensive empirical evidence, existing work lacks a principled understanding of why such jailbreaks reliably succeed or how their effectiveness scales with context composition. We propose a posterior reweighting framework that models a safety-aligned MLLM as implicitly operating...
  </details>

- **2026-09-08** — Hyun Gu Kang, Daniil Gurgurov, Tanja Baeumel et al. — [Compositional Multilingual and Behavioral Attribute Steering](http://arxiv.org/abs/2609.08410v1)
  <details><summary>📄 Abstract</summary>
  This study examines the compositionality of steering vectors for language and behavioral control in large language models. Focusing on language, jailbreak, and conciseness, we investigate whether additive, training-free composition of attribute steering vectors can preserve the intended steering effect of each attribute, across four instruction-tuned models from two model families and two size scales. We find that single-attribute steering is reliable for all three attributes, but only within an...
  </details>

- **2026-09-08** — Tejasvi C. Addagada — [Structural Jailbreaks Generalize but Do Not Compound: A cross-provider and multilingual study of Involuntary In-Context Learning](http://arxiv.org/abs/2609.08373v1)
  <details><summary>📄 Abstract</summary>
  Aligned language models fail under two independent pressures: the structural jailbreak class recently formalized as Involuntary In-Context Learning (IICL), which reframes a harmful request as the final missing cell of a data-labeling task completed by pattern rather than judged as content; and the erosion of safety alignment outside English. A natural hypothesis is that these compound. We test it directly. Using a deterministic IICL operator and a StrongREJECT-style rubric judge, we red-team two...
  </details>

- **2026-09-08** — Yongxi Zhou, Wenbo Ye, Yuanzhe Liu et al. — [Style Over Substance: Content-Invariant Wrappers Flip LLM Safety-Judge Verdicts](http://arxiv.org/abs/2609.08236v1)
  <details><summary>📄 Abstract</summary>
  Automatic safety judges -- systems such as Llama Guard or a GPT-4o grading prompt that decide whether a model's reply is harmful -- produce the numbers behind almost every reported jailbreak success rate, defense evaluation, and safety leaderboard. We ask whether these judges grade what a reply contains or how it sounds. We keep a reply's content fixed and add content-invariant style wrappers: fixed strings placed before or after the reply that change only its tone (an educational disclaimer, a ...
  </details>


### 📂 prompt-injection
*提示注入攻击 / Prompt Injection Attacks* — 6 papers

- **2026-09-09** — Asif Pinjari, Mithun Paul Saint-Germain — [DriftNet: A Dual-Head Trajectory Transformer for Detecting and Localizing Prompt Injection in LLM Agents](http://arxiv.org/abs/2609.10892v1)
  <details><summary>📄 Abstract</summary>
  When an indirect prompt injection succeeds against an LLM agent, the compromise is visible in the agent's own behavior: a benign prefix of tool calls, a poisoned observation, and a suffix of actions that serve the attacker. An operator needs three facts: where the attack entered, which steps it corrupted, and whether apparent poison was resisted. Existing systems return either a whole-trace verdict or a single unsafe index. We present DriftNet, a dual-head trajectory Transformer that reads a log...
  </details>

- **2026-09-09** — Zehua Zhang, Jie Hu, Pratham Hegde et al. — [No-Box Vulnerability Analysis: Description-only Detection of Indirect Prompt Injection Vulnerabilities in MCP Servers](http://arxiv.org/abs/2609.10854v1)
  <details><summary>📄 Abstract</summary>
  Conventional vulnerability analysis relies on either system access or dynamic interaction, all of which may be unavailable to third-party analysts auditing closed-source, remotely hosted, critical in situ systems, or commercially gated software. Therefore, we propose a new paradigm of no-box vulnerability analysis in which neither access nor runtime interaction is available, and only functionality metadata is available. Such metadata defines the intended behavior of the system, including its inp...
  </details>

- **2026-09-09** — Anna Gazani, Spyridon Kounoupidis, Panagiotis Katsaros et al. — [Architecting the Secure AI-SOC: A Neurosymbolic Framework for Pipeline Integrity and Threat Mitigation](http://arxiv.org/abs/2609.10707v1)
  <details><summary>📄 Abstract</summary>
  The integration of Large Language Models (LLMs) into Security Operations Centers (SOCs) streamlines threat intelligence but introduces critical vulnerabilities, notably indirect prompt injection via log poisoning. Adversaries exploit this vector to execute multistep ``promptware'' kill chains by embedding malicious payloads within system logs to hijack the LLM's operational logic. Securing this pipeline presents a dichotomy: deterministic defenses are computationally efficient yet semantically b...
  </details>

- **2026-09-09** — Ryan Lum, Yongfeng Zhang — [Kernel-Managed Shared Memory for System-Wide Personalization](http://arxiv.org/abs/2609.10144v1)
  <details><summary>📄 Abstract</summary>
  AI systems become more useful when they can adapt to the people using them, but in multi-agent systems, useful context learned by one agent often remains unavailable to others. We present kernel-managed shared memory, a system-level abstraction in which specialized agents write structured, tagged memories while the agent-system kernel, not individual agents, governs retrieval, privacy enforcement, and prompt injection. We implement and evaluate this design on AIOS and compare it against three al...
  </details>

- **2026-09-08** — Viet K. Nguyen, Mohammad I. Husain — [An Experimental Evaluation of Multimodal Prompt Injection Attacks on Agentic AI Frameworks](http://arxiv.org/abs/2609.09404v1)
  <details><summary>📄 Abstract</summary>
  Agentic AI frameworks let a language model plan, keep memory, and call tools that reach real files, mail, and services. Most of these agents also read images, which gives an attacker a way to put text into the agent's context without going through the user. We present MMPIBench, a reproducible benchmark that measures what happens next. It delivers a fixed set of attacks through six visual carriers (OCR text, overlays, EXIF metadata, QR codes, fake interfaces, and hybrids) and records how far eac...
  </details>

- **2026-09-08** — Dimitrios Stamatios Bouras, Yihan Dai, Sergey Mechtaev — [Authority Is Not a String: A Capability-Scoped Harness for Prompt-Injection-Resistant Coding Agents](http://arxiv.org/abs/2609.08371v1)
  <details><summary>📄 Abstract</summary>
  Coding agents use system-level tools to read files, execute commands, and modify source code. Within the agent's sandbox, these tools often carry ambient authority: naming a resource is sufficient to act on it. Indirect prompt injection exploits this authority by placing instructions in repository files or tool output that cause the agent to perform actions the user did not request. We propose CapScope, a harness-level authorization mechanism that restricts tool use without requiring the model t...
  </details>


### 📂 memory-poisoning
*记忆投毒与篡改 / Memory Poisoning & Tampering* — 1 papers

- **2026-09-08** — Ayan Roy, Kaustuvi Basu — [MemSentry: A Framework for Detecting Persistent Memory Poisoning in Agentic AI](http://arxiv.org/abs/2609.08747v1)
  <details><summary>📄 Abstract</summary>
  Agentic AI systems with persistent memory introduce a distinct attack surface known as memory poisoning, in which adversarially crafted content is stored in long-term memory and subsequently influences future agent behavior. Such attacks can suppress security alerts, facilitate privilege escalation, alter trust relationships, or override security policies without modifying the underlying model weights or system prompts. To address this threat, we present MemSentry, a formal, configuration-driven...
  </details>


### 📂 tool-use-attack
*工具使用攻击 / Tool-Use Attacks* — 1 papers

- **2026-09-10** — Pingchen Lu, Xiangyi Wang, Xiang Li et al. — [COBRA-Skills: Contextual Bandit-Guided Evolution for Agent Skill Optimization](http://arxiv.org/abs/2609.11682v1)
  <details><summary>📄 Abstract</summary>
  Large language model (LLM) agents can benefit from reusable skills distilled from prior task experience, yet existing skill optimization methods often rely on costly execution-based evaluation and substantial task data. We introduce \textbf{COBRA-Skills}, an efficient framework that formulates skill optimization as budgeted sequential optimization over a dynamically evolving candidate space. COBRA-Skills couples contextual-bandit-guided prioritization with evidence-grounded skill evolution, sele...
  </details>


### 📂 backdoor
*后门与投毒攻击 / Backdoor & Poisoning Attacks* — 3 papers

- **2026-09-10** — Rui Wen, Ahmed Salem, Andrew Paverd et al. — [SpecGuard: Inference-Time Backdoor Detection For Free](http://arxiv.org/abs/2609.11799v1)
  <details><summary>📄 Abstract</summary>
  Large language models are often fine-tuned, shared, or downloaded from third parties, so a deployed model may carry a hidden backdoor that behaves normally on benign inputs but switches to attacker-controlled behavior when a secret trigger appears. While backdoors can be audited before deployment, runtime monitoring remains important for models that are frequently updated. The challenge is that LLM serving is latency-sensitive: existing inference-time detectors either rely on assumptions about t...
  </details>

- **2026-09-10** — Haozhe Lu, Jiaqi Li, Xinyuan Zhu et al. — [ToxicRAG: Compromising Retrieval-Augmented Generation Systems via Single-Shot Knowledge Poisoning Attacks](http://arxiv.org/abs/2609.11082v1)
  <details><summary>📄 Abstract</summary>
  Retrieval-Augmented Generation (RAG) can ground large language model (LLM) outputs in external evidence, but it also exposes the system to knowledge poisoning. Representative attacks use multiple injected documents or templates that directly assert a target answer. We present ToxicRAG, a one-document-per-target attack that expresses misinformation as a coherent knowledge-update narrative. The generated document first acknowledges the previously accepted answer, introduces fabricated events that ...
  </details>

- **2026-09-08** — Iliano Fasolino — [In RAG We Trust? Measuring Robustness of Retrieval-Augmented Generation Under Document Poisoning](http://arxiv.org/abs/2609.09243v1)
  <details><summary>📄 Abstract</summary>
  Retrieval-augmented generation (RAG) grounds a language model in retrieved documents, which reduces hallucination but creates a new attack surface: if retrieved text is tampered with, the model may repeat the falsehood. We study how much a small quantized model, Llama 3.1 8B, degrades when a fraction of its retrieved context is poisoned. Three corruption strategies are tested, entity swap, number swap, and negation, each applied to zero, one, two, or three of the three retrieved passages, over a...
  </details>


### 📂 adversarial-attack
*对抗攻击 / Adversarial Attacks* — 5 papers

- **2026-09-09** — Tong Li, Saunak Kumar Panda, Yisha Xiang — [Certifying Lower Bounds for Risk-Sensitive Reinforcement Learning under Adversarial State Perturbations](http://arxiv.org/abs/2609.10866v1)
  <details><summary>📄 Abstract</summary>
  Reinforcement learning (RL) agents deployed in real-world environments are often vulnerable to adversarial perturbations in state observations, creating risks in safety-critical applications. Certification methods can improve robustness against adversarial perturbations by providing lower bounds on expected cumulative rewards. Existing certification methods, however, mainly focus on risk-neutral objectives. In this paper, we extend certification methods to risk-sensitive objectives by establishi...
  </details>

- **2026-09-09** — Ravi Ranjan, Olivera Kotevska, Agoritsa Polyzou — [Forgetting Only What Matters: Layer-Selective Unlearning toward Robust LLMs](http://arxiv.org/abs/2609.10439v1)
  <details><summary>📄 Abstract</summary>
  Large Language Models (LLMs) can memorize and reproduce sensitive, copyrighted, or otherwise undesirable training content, creating privacy, safety, and regulatory concerns. Machine unlearning offers a practical alternative to full retraining, but many existing methods apply broad or fixed parameter updates that can degrade utility and remain brittle under deployment changes such as post-training quantization, where forgotten knowledge may partially re-emerge. We propose Forgetting Only What Mat...
  </details>

- **2026-09-09** — Hanyi Zhou, Chenyang Li, Yuanzhe Pang et al. — [Understanding the Security Boundary of Obfuscation-based On-Device LLM Protection](http://arxiv.org/abs/2609.10117v1)
  <details><summary>📄 Abstract</summary>
  Trusted Execution Environments (TEEs) offer a promising mechanism for safeguarding the intellectual property of on-device Large Language Models (LLMs). To overcome the inherent computational bottlenecks of TEEs, existing TEE-Shielded LLM Partition (TSLP) methods apply efficient obfuscation schemes to computationally intensive layers, offloading them to external GPUs while retaining only lightweight operations within the TEE. Although a growing body of TSLP-based approaches has emerged, these def...
  </details>

- **2026-09-09** — Samar Ansari — [Beyond Training: A Feasibility Taxonomy for Inference-Time AI Governance](http://arxiv.org/abs/2609.10105v1)
  <details><summary>📄 Abstract</summary>
  Compute governance today is a governance of training: the thresholds, reporting requirements, and frontier-AI regimes now in force attach to training compute and treat the trained model as the regulatory unit. That picture is incomplete: capability increasingly migrates to the deployment stage through inference-time scaling, agentic scaffolding, and compression onto consumer hardware. This paper asks which mechanisms are available once the regulatory object shifts from the training run to the in...
  </details>

- **2026-09-09** — Rafael M. Mamede, Pedro C. Neto, Ana F. Sequeira — [What Makes Adversarial Examples Transfer Across Deepfake Detectors?](http://arxiv.org/abs/2609.10002v1)
  <details><summary>📄 Abstract</summary>
  Deepfake detectors remain vulnerable to transfer-based black-box attacks, in which adversarial examples are generated on a source surrogate model and transferred to a target model, unknown to the attacker. Yet how source--target compatibility shapes attack success remains poorly understood. Prior studies evaluate limited detector pools and rarely disentangle architectural from training factors. We conduct a controlled evaluation of adversarial transferability across 60 detectors spanning six bac...
  </details>


### 📂 privacy-leakage
*隐私泄露 / Privacy Leakage* — 36 papers

- **2026-09-10** — Jordi Luque, Fernando López, Aleix Sant — [Component-Aware Differential Privacy for Federated Multilingual Speech-LLMs](http://arxiv.org/abs/2609.11762v1)
  <details><summary>📄 Abstract</summary>
  Per-layer differential privacy (DP) clipping improves gradient fidelity in federated learning by allocating per-matrix clipping budgets proportional to parameter count. We show that this recipe breaks for speech large language models (speech-LLMs), when the acoustic encoder and the language decoder differ by an order of magnitude in update norm. Single-pool per-layer methods suffer \emph{cross-component budget collapse}, dragging word error rate (WER) far from flat global clipping or collapsing ...
  </details>

- **2026-09-10** — William Novak, Muhammad Abusaqer — [Empirical Evaluation of Membership Inference Attacks on NLP Text Classifiers: A Baseline Study on SST-2](http://arxiv.org/abs/2609.10935v1)
  <details><summary>📄 Abstract</summary>
  Membership inference attacks (MIAs) try to determine whether a specific record was used to train a model, a privacy risk that matters in natural language processing (NLP), where training data can contain sensitive user text. This paper presents a controlled benchmark of membership inference vulnerability for text classification on the GLUE SST-2 sentiment dataset. A TF-IDF + Logistic Regression pipeline and a fine-tuned DistilBERT classifier are compared under a loss-threshold MIA, with utility ...
  </details>

- **2026-09-10** — Atsutoshi Kumagai, Tomoharu Iwata, Hiroshi Takahashi et al. — [AUC Maximization from Biased Positive-unlabeled Data with Confidence](http://arxiv.org/abs/2609.10928v1)
  <details><summary>📄 Abstract</summary>
  Maximizing the area under the receiver operating characteristic curve (AUC) is a standard approach to imbalanced binary classification. Although positive and negative data are required for maximizing the AUC, negative data are often difficult to collect in some real-world applications due to privacy concerns or the need for specialized expertise to annotate them. Thus, AUC maximization from positive and unlabeled (PU) data has been attracting attention. Existing methods assume that labeled posit...
  </details>

- **2026-09-10** — Guowei Yang, Farbin Fayza, Beren Aydoğan et al. — [PHAT: PHotonic Accelerator for TFHE](http://arxiv.org/abs/2609.11613v1)
  <details><summary>📄 Abstract</summary>
  Fully Homomorphic Encryption (FHE) enables secure computation on encrypted data, making it a promising solution for privacy-preserving applications in the cloud. Among various FHE schemes, FHE over the Torus (TFHE) stands out due to its support for arbitrary operations. However, its high computation and communication overhead, particularly in the Fast Fourier Transform (FFT) operations required during bootstrapping, limits its practicality for real-world applications. Conventional electronic acc...
  </details>

- **2026-09-10** — Narcis Marincat — [Portable Semantics, Private Dialects: Reuse and Negative Transfer in Latent Communication Between Language-Model Cells](http://arxiv.org/abs/2609.11365v1)
  <details><summary>📄 Abstract</summary>
  In shared-genome language-model societies, restricted evidence visibility favors reusable, value-indexed latent packet interfaces, whereas the sole high-performing globally visible model in the parent study learned an episode-entangled code. This companion study asks whether independently trained societies share one packet language, where strict zero-shot transfer fails, and whether inherited interface state helps or harms later learning. First, a leakage-controlled causal interoperability audit...
  </details>

- **2026-09-10** — Raad Bin Tareaf, Murad Al-Rajab, Samia Loucif et al. — [Target leakage, not model class, explains reported accuracy in survey-based cardiovascular screening: a leakage-tiered audit of glass-box and tabular foundation models](http://arxiv.org/abs/2609.11838v1)
  <details><summary>📄 Abstract</summary>
  Cardiovascular screening models trained on national health surveys routinely report areas under the receiver operating characteristic curve (AUROC) near 0.89. We asked whether that accuracy reflects learning or target leakage, whether tabular foundation models change the answer, and whether the properties deployment requires survive joint examination. We benchmarked ten classifiers spanning linear, tree-ensemble, neural, glass-box, and tabular foundation classes for prevalent myocardial infarcti...
  </details>

- **2026-09-10** — Chibuzor Okocha, Christan Earl Grant — [Beyond Word Error Rate: A Switch Aware Evaluation of ASR and Audio Language Models on English Yoruba Code-Switched Speech](http://arxiv.org/abs/2609.11786v1)
  <details><summary>📄 Abstract</summary>
  Automatic speech recognition (ASR) systems and audio language models (audio LMs) now report low error rates on monolingual benchmarks, but their behavior on code switched speech in low resource, diacritic rich languages remains poorly characterized. We present a switch aware evaluation of eleven modern systems (six ASR models and five audio LMs) on English Yoruba code-switched speech, using a deterministic 2000 utterance evaluation set and a shared scoring pipeline. Beyond word error rate (WER),...
  </details>

- **2026-09-10** — Tobias Deußer, Max Hahnbück, Lorenz Sparrenberg et al. — [On the Impact of Anonymization on the Performance of Large Language Models](http://arxiv.org/abs/2609.11335v1)
  <details><summary>📄 Abstract</summary>
  As large language models are increasingly deployed in sensitive domains, anonymizing input data to protect personally identifiable information has become a critical practice. However, the impact of this anonymization on model utility is not well understood. This paper presents a systematic empirical study of the trade-off between privacy and performance. We evaluate five prominent language models across eleven diverse benchmarks, comparing their performance on original versus pseudonymized input...
  </details>

- **2026-09-10** — Hao Lin, He Jiang, Xiaochen Li et al. — [CoSTAR: Data Synthesis-Driven Constraint-Aware COBOL Section Summarization for Legacy System Modernization](http://arxiv.org/abs/2609.11332v1)
  <details><summary>📄 Abstract</summary>
  COBOL remains critical to governments, financial institutions, and large enterprises; yet, aging technologies, shrinking expertise, and missing documentation make modernization of COBOL-based legacy systems increasingly urgent. Before migration, code summarization is a common practice to support legacy system understanding. However, COBOL code summarization, especially on section-level, faces two key challenges: data scarcity and migration constraint preservation. To address these challenges, we...
  </details>

- **2026-09-10** — Soheil Human — [From Digital Accountability to Accountable Digitality Through Needs-Aware Information Systems: The Case of Auditable Child-Welfare Judgments](http://arxiv.org/abs/2609.11125v1)
  <details><summary>📄 Abstract</summary>
  Digital accountability research asks how digital systems can, among other aims, be made transparent, explainable, auditable, contestable, and supportive of ongoing learning and improvement. This paper reverses the question: how can digital transformation make established human institutions more accountable? It theorizes this reversal as accountable digitality and specifies needs-aware information systems as the mediating mechanism. The hard and paradigmatic case is child-welfare judgment, where ...
  </details>

- **2026-09-10** — Zhenhua Liu, Zhanxu Xie, Junjie Yu et al. — [Demystifying the Privacy-Utility Trade-off in LLM Interactions](http://arxiv.org/abs/2609.10992v1)
  <details><summary>📄 Abstract</summary>
  The integration of Large Language Models into daily tasks relies on context-rich instructions, inevitably exposing sensitive user information. Current privacy-preserving methods typically employ context-agnostic static rules, causing severe utility degradation. However, the specific mechanisms governing how sanitization impacts downstream performance remain largely underexplored. To address this, we conduct a systematic analysis to deconstruct the privacy-utility trade-off, uncovering three unde...
  </details>

- **2026-09-09** — Kyle Stein, Guillermo Francia, Eman El-Sheikh et al. — [Temporal and Multimodal Deep Learning for Cyberattack Detection in LEO Satellite Systems](http://arxiv.org/abs/2609.10746v1)
  <details><summary>📄 Abstract</summary>
  The growing reliance on Low-Earth Orbit (LEO) satellite communication systems has increased the need for intelligent methods capable of detecting cyberattacks across complex and dynamic space environments. Unlike conventional network intrusion detection, satellite systems generate heterogeneous information across radio-frequency (RF) links, onboard hardware, and orbital operations. However, many existing approaches either rely on terrestrial intrusion datasets or evaluate individual observations...
  </details>

- **2026-09-09** — Wissam Ghantous, Alexander V. Mantzaris — [CARTS: Contextual Autoregressive Rank Transcoding Steganography for Full-Capacity Keyed Text Encoding](http://arxiv.org/abs/2609.10744v1)
  <details><summary>📄 Abstract</summary>
  Autoregressive language models can be used to transform a payload text into a stegotext of identical token length by preserving per-position rank information across contexts - a methodology we formalize as Contextual Autoregressive Rank Transcoding Steganography (CARTS). While the Calgacus construction of Norelli et al. demonstrated this phenomenon experimentally, no formal security analysis existed. This paper provides the first rigorous treatment of CARTS. We show its exact correctness under d...
  </details>

- **2026-09-09** — Ladan Kian, Ming Ming Tan, Dariusz Kowalski — [Navigating Small-World Networks with Distance Predictions](http://arxiv.org/abs/2609.10885v1)
  <details><summary>📄 Abstract</summary>
  The small-world phenomenon was given an algorithmic foundation by Kleinberg, who showed that in an augmented $k$-dimensional lattice a decentralized greedy algorithm delivers a message in $O(\log^2 n)$ expected steps. We study predicted-greedy routing, in which a mobile agent forwarding the message moves at each step to the neighbor minimizing a noisy $(\varepsilon,δ)$-prediction of its distance to the target, redrawn at every step from an oracle conditioned on the full routing history. Two case...
  </details>

- **2026-09-09** — Yiwei Fang, Yichen Liu, Ze Jin et al. — [Towards Tackling Application Logic Flaws through Autonomous Formal-Logic Modeling and Automated Reasoning](http://arxiv.org/abs/2609.10537v1)
  <details><summary>📄 Abstract</summary>
  Logic flaws pose significant challenges in the design and implementation of modern, semantically rich systems and applications, impacting security, privacy, and trust. These flaws are inherently tied to business-specific semantics and threat models, making their discovery and reasoning difficult and hard to scale. Real-world systems often exhibit diverse application features, complex protocol logic, and domain-specific threat models, necessitating substantial human effort and domain expertise fo...
  </details>

- **2026-09-09** — Dongdong Zhao, Jian Chen, Guancheng Lin et al. — [Keep Evaluation Fair: Detecting Data Leakage in Code Generation Benchmarks via Membership Inference Attacks](http://arxiv.org/abs/2609.09865v1)
  <details><summary>📄 Abstract</summary>
  Code generation benchmarks are widely used to evaluate Large Language Models (LLMs), but benchmark data leakage into training sets can inflate performance and undermine evaluation validity. DetectLeak, a method specifically designed for code generation benchmark leakage detection, relies on perplexity scores to identify likely leaked samples. However, perplexity mainly reflects general familiarity with code patterns and may perform poorly on complex or rare samples. It also overlooks other usefu...
  </details>

- **2026-09-09** — Yidan Sun, Viktor Schlegel, Srinivasan Nandakumar et al. — [Subgroup Membership Inference Audits of Differentially Private Synthetic Text](http://arxiv.org/abs/2609.09848v1)
  <details><summary>📄 Abstract</summary>
  Synthetic data releases are increasingly proposed in the literature as a means of sharing realistic data replicas in lieu of sensitive private datasets. Even when the worst-case privacy leakage of such releases is bounded by means of differential privacy (DP), in practice a residual risk remains. Membership inference attack (MIA) audits are conducted to empirically quantify this risk. However, existing methods only measure average-case risk for randomly drawn records, which might conceal the ris...
  </details>

- **2026-09-09** — Divyanshu Kumar, Nitin Aravind Birur, Tanay Baswa et al. — [Black-Box Red Teaming of Agentic AI: A Taxonomy-Driven Framework for Automated Risk Discovery](http://arxiv.org/abs/2609.09647v1)
  <details><summary>📄 Abstract</summary>
  Agentic systems are rapidly moving to production, where they read untrusted inputs, call tools with real permissions, and act autonomously, expanding the security surface beyond chat-only models. Yet standard evaluations remain single-turn and fail to capture multi-step agent vulnerabilities. We present a systematic black-box framework for risk-aware agent evaluation requiring only basic system descriptions. Our approach introduces: (1) a seven-domain taxonomy mapping observable behaviors to ris...
  </details>

- **2026-09-09** — Chengkai Zhu, Xin Wang — [Private communication via zero-private-capacity quantum channels](http://arxiv.org/abs/2609.10520v1)
  <details><summary>📄 Abstract</summary>
  Private communication over a noisy quantum channel requires reliable transmission to the receiver and secrecy from the environment. Whether two channels with zero private capacity can jointly enable private communication is a longstanding open problem in quantum information theory. Here we resolve this problem by exhibiting a four-level channel and a qubit erasure channel with half erasure probability, each with zero private capacity, whose joint use achieves more than 0.0001903 private bits per...
  </details>

- **2026-09-09** — Heng Jin, Chaoyu Zhang, Hexuan Yu et al. — [Privacy-Preserving Split Learning for Federated LLM Fine-Tuning](http://arxiv.org/abs/2609.09794v1)
  <details><summary>📄 Abstract</summary>
  Fine-tuning large language models (LLMs) on domain-specific data is essential for downstream adaptation. In many deployments, a participant cannot hold the complete model locally. This happens because the model owner keeps the full model proprietary, or because the participant lacks sufficient compute resources. Split Learning (SL) addresses this by partitioning the model between the participant and a server so that only a small portion runs locally. When the underlying data is additionally dist...
  </details>

- **2026-09-09** — Ben Merbaum, Mohammad Amin Raeisi, Wenhao Wang et al. — [Maverick: Private and Verifiable LLM Inference Made Practical via Matrix-Vector Multiplication Delegation](http://arxiv.org/abs/2609.10264v1)
  <details><summary>📄 Abstract</summary>
  Open-source large language models (LLMs) are increasingly competitive with closed-source models while offering transparency and the ability to run inference without exposing user inputs to a service provider. However, running large-scale models locally requires substantial computational resources. In practice, users may still resort to a third-party provider, giving rise to privacy and correctness concerns. Existing solutions that address these problems often impose substantial server overhead o...
  </details>

- **2026-09-09** — Ali Hassan, Zijia Zhao, Maha A. Metawei — [Hybrid Quantum-Classical NLP Classification with Compact Semantic Representations: An Experimental Analysis of Representation Compression](http://arxiv.org/abs/2609.10089v1)
  <details><summary>📄 Abstract</summary>
  Large language and sentence-embedding models provide rich semantic representations, but their high dimensionality poses a challenge for near-term quantum machine learning (QML), where quantum circuits can process only a limited number of input features. We investigate a hybrid quantum-classical pipeline that transforms high-dimensional sentence embeddings into compact representations for variational quantum classification. The workflow combines a pretrained sentence-embedding model, dimensionali...
  </details>

- **2026-09-09** — Yonghyun Jun, Jimin Lee, Hwan Chang et al. — [Leveraging Fine-grained Error Correction in Korean Speech Recognition for Consultation Services](http://arxiv.org/abs/2609.09889v1)
  <details><summary>📄 Abstract</summary>
  Automatic Speech Recognition (ASR) technology is fundamental to customer service automation and large-scale transcription. However, even advanced ASR models exhibit inevitable errors in complex real-world environments such as call center conversations. When privacy restrictions preclude audio access, error correction must rely on text-based post-editing. Existing text-only approaches face significant challenges in low-resource languages, mainly due to a critical scarcity of annotated corpora and...
  </details>

- **2026-09-09** — Mohamed Moustafa Dawoud, Riya Aggarwal, Likith Rahul Krishnamurthy et al. — [PrivAudit: A Dual-Lens Auditing Framework for Website Privacy Practices under the CCPA](http://arxiv.org/abs/2609.09697v1)
  <details><summary>📄 Abstract</summary>
  Five years after the enforcement of the California Consumer Privacy Act (CCPA), understanding how website privacy practices evolve at scale in response to regulation remains a key challenge for both researchers and regulators. Prior work and regulatory efforts have focused on manual and case-specific enforcement, but there remain no scalable approaches to systematically audit two key user-facing facets of websites that are crucial signals for the CCPA: privacy disclosures and front-end user trac...
  </details>

- **2026-09-09** — Weisi Yang, Stephen Xia — [PELM: Power Efficient On-Device LLM Inference with Speculative Decoding and Dynamic Voltage Frequency Scaling](http://arxiv.org/abs/2609.09662v1)
  <details><summary>📄 Abstract</summary>
  Deploying Large Language Models (LLMs) directly on mobile platforms at the edge is gaining traction due to a myriad of benefits, such as increased privacy, personalization, and reduced latency. However, LLMs have heavy computational requirements, which are difficult for resource-constrained mobile and edge platforms to fulfill. In addition to limited compute resources, mobile and edge systems often have a compact form factor and lack physical mechanisms to dissipate heat generated from high proc...
  </details>

- **2026-09-09** — Zhuodong Liu, Xiangyu Li, Chunhong Yuan et al. — [Modality-Decoupled Federated Learning for Privacy-Preserving Embodied Intelligence in 6G](http://arxiv.org/abs/2609.09591v1)
  <details><summary>📄 Abstract</summary>
  Sixth-generation (6G) wireless networks are expected to provide a key infrastructure for large-scale embodied intelligence, where heterogeneous robots collaborate through low-latency connectivity, edge intelligence, and distributed sensing. Vision-language-action (VLA) models offer a foundation by integrating visual perception, language understanding, and action generation into a unified closed-loop policy. However, training and adapting VLA models to distributed robotic agents introduce challen...
  </details>

- **2026-09-09** — Philip Graemer, Giuseppe Di Caprio — [Pretraining and Distillation Matter More Than Architecture Family for Label-Free Single-Cell Classification](http://arxiv.org/abs/2609.09863v1)
  <details><summary>📄 Abstract</summary>
  Choosing a deep learning architecture for label-free single-cell classification remains an open question, with microscopy benchmarks reporting conflicting conclusions about CNNs versus transformers. We present a controlled benchmark on LIVECell phase-contrast microscopy data using source-image-disjoint train/validation/test splits to prevent parent-image leakage and matched optimisation, augmentation, and evaluation protocols across EfficientNet, Vision Transformer (ViT), and EVA-02 models. This...
  </details>

- **2026-09-08** — Stella Zhao, Tommy Sha — [GoAnt: Quality-Diversity Multi-Agent Search for Alpha Factor Discovery in Market Microstructure Data](http://arxiv.org/abs/2609.08719v2)
  <details><summary>📄 Abstract</summary>
  Automated alpha factor discovery searches symbolic trading signals from price-volume panels and order-book data under a fixed evaluation budget. Existing single- and multi-agent program-search systems can overfit predictive proxies that fail after execution costs and repeatedly explore redundant factor families, limiting execution robustness and behavioral diversity. We introduce GoAnt, a quality-diversity multi-agent search framework that combines non-communicating Explorer, Exploiter and Conne...
  </details>

- **2026-09-08** — Shengjie Niu, Yeheng Ge, Jian Huang — [Black-Box Membership Inference via Word-Level Probability Estimation](http://arxiv.org/abs/2609.10611v1)
  <details><summary>📄 Abstract</summary>
  Membership inference attacks (MIAs) have emerged as critical tools for auditing privacy risks in large language models (LLMs), aiming to determine whether a given text was included in a model's training corpus. However, most existing MIAs require access to per-token logits or probabilities, making them inapplicable in practice to proprietary LLMs that expose only textual continuations. To address this underexplored setting, we propose Word-level Probability MIA (WPMIA), a statistically principle...
  </details>

- **2026-09-08** — Mauricio Figueroa — [The Mutations of Machine Speech](http://arxiv.org/abs/2609.09496v1)
  <details><summary>📄 Abstract</summary>
  Algorithmic outputs now populate the digital environments through which contemporary life is organized. The role of law in facilitating and constituting (rather than merely responding to) these processes is gaining increasing traction across scholarly accounts. This inquiry traces the evolution of algorithmic outputs attending to their legal underpinnings and social implications, surfacing the mutations of machine speech.   The first mutation redefined speech as data to be queried: search engine...
  </details>

- **2026-09-08** — Duncan Stewardson, Grayson W. White, Adam Groce — [Differentially Private Average Treatment Effect Estimation by Propensity Score Blocking](http://arxiv.org/abs/2609.09536v1)
  <details><summary>📄 Abstract</summary>
  Average treatment effect (ATE) estimation in observational studies is a fundamental statistical tool used frequently in social science, medicine, and other fields. These fields often work with sensitive data where privacy protections are important, so a differentially private mechanism for ATE estimation is highly desirable. Here we present two propensity score-based algorithms for ATE estimation on observational data, one improving the inverse probability weighting (IPW) method used in prior wo...
  </details>

- **2026-09-08** — Stella Zhao, Tommy Sha — [GoAnt: Quality-Diversity Multi-Agent Search for Alpha Factor Discovery in Market Microstructure Data](http://arxiv.org/abs/2609.08719v1)
  <details><summary>📄 Abstract</summary>
  Automated alpha factor discovery searches symbolic trading signals from price-volume panels and order-book data under a fixed evaluation budget. Existing single- and multi-agent program-search systems can overfit predictive proxies that fail after execution costs and repeatedly explore redundant factor families, limiting execution robustness and behavioral diversity. We introduce GoAnt, a quality-diversity multi-agent search framework that combines non-communicating Explorer, Exploiter and Conne...
  </details>

- **2026-09-08** — Yi Ting Shen, Kentaroh Toyoda, Alex Leung — [ACEA: An Adversarial Co-Evolution Arena for Head-to-Head Red-Team and Blue-Team LLM Testing](http://arxiv.org/abs/2609.08256v1)
  <details><summary>📄 Abstract</summary>
  Automated red-team attacks and blue-team defenses for large language models (LLMs) are advancing quickly. However, attackers and defenders are built and tested in isolation, and the resulting scores are hard to trust. To tackle this, we present ACEA (Adversarial Co-Evolution Arena), a platform that connects a pluggable red-team adapter and a pluggable blue-team adapter to a shared target LLM and scores their attack and defense rates with an LLM judge. ACEA contributes four components. First, a p...
  </details>

- **2026-09-08** — Pujun Zheng, Zixin Shang, Shufan Jiang et al. — [SWE-Bench Pro Verified: A Reliable Benchmark for Software Engineering Agents](http://arxiv.org/abs/2609.08149v1)
  <details><summary>📄 Abstract</summary>
  SWE-Bench Pro has emerged as a standard benchmark for evaluating software engineering agents on challenging repository-level tasks. However, our analysis work show that its evaluation is undermined by two sources of unreliability: \textbf{reward hacking}, enabled by leakage of gold solutions or hidden evaluation information, and \textbf{task quality issues}, including misleading problem statements and improperly scoped tests. These issues can inflate benchmark performance and obscure agents' tru...
  </details>

- **2026-09-08** — Wulin Xie, Rui Zhao, Kecen Li et al. — [VI-Bench: Benchmarking Prompt Inversion from AIGC Videos](http://arxiv.org/abs/2609.08079v1)
  <details><summary>📄 Abstract</summary>
  Recent advances in video generation have made prompt-based control increasingly central to AIGC video generation. Prompts specify what a video should depict and how it should be represented, controlling factors such as visual style or camera behavior. Understanding this recoverability is important both for creative reuse and editing, and for assessing prompt leakage risks. However, existing video understanding benchmarks do not measure this capability: a caption may describe what is visible, but...
  </details>

- **2026-09-08** — Keyvan Aghababaiyan — [Hybrid Continuous DoA Estimation with Shared-Radius Co-Prime Circular Arrays](http://arxiv.org/abs/2609.08827v1)
  <details><summary>📄 Abstract</summary>
  This paper proposes a shared-radius co-prime circular array for high-resolution, continuous 2D Direction-of-Arrival (DoA) estimation in 3D space, jointly estimating azimuth and elevation angles. The proposed architecture consists of two uniform circular sub-arrays with co-prime antenna counts sharing a common radius RR, a design that intrinsically suppresses mutual coupling leakage compared to dense uniform arrays. Unlike existing works that rely on complex phase-mode transformations to map circ...
  </details>


### 📂 misuse
*滥用与误用 / Misuse & Abuse* — 15 papers

- **2026-09-10** — Zonghao Ying, Xiangfan Wu, Huiyu Wu et al. — [The Missing Boundary: How Autonomous Agents Lose Control](http://arxiv.org/abs/2609.11024v1)
  <details><summary>📄 Abstract</summary>
  Autonomous agents increasingly perform long-horizon tasks involving tool use, persistent state, and consequential actions, raising a fundamental question: \emph{under what conditions does an agent cross the boundary of authorized execution while pursuing a legitimate task?} Existing studies often attribute such failures to adversarial instructions, malicious environments, or conflicting objectives, leaving unclear how loss of control can emerge during otherwise legitimate task execution. We stud...
  </details>

- **2026-09-10** — Adithiyan Rajan Indira Saravanan, Kathleen C. Fraser — [RAG-Safety-Bench: Reliable Evaluation of Retrieval-Augmented LLM Safety](http://arxiv.org/abs/2609.11758v1)
  <details><summary>📄 Abstract</summary>
  Allowing large language models (LLMs) to retrieve information from a set of trusted documents can increase reliability and reduce hallucination. However, recent work has demonstrated that retrieval-augmented generation (RAG) can have unintended side effects on the overall safety of the generated responses, when prompted for harmful or dangerous content. A clearer understanding of the mechanisms leading to this result is needed, as increasing numbers of end users turn to RAG to incorporate corpor...
  </details>

- **2026-09-10** — Xingyu Shen, Tommy Duong, Muduo Xu et al. — [The Machines Are Calling: Measuring Automated and Synthetic Voices in Unwanted Inbound Calls](http://arxiv.org/abs/2609.11137v1)
  <details><summary>📄 Abstract</summary>
  In February 2024 the U.S. Federal Communications Commission (FCC) placed AI-generated voices under the Telephone Consumer Protection Act (TCPA). Yet no peer-reviewed measurement says how much unwanted call traffic is placed by a machine, or how much of that machine speech is synthesized rather than played from a recording. We report both with a disclosed pipeline. An interactive voice honeypot (language-model personas on real U.S. numbers, the caller recorded on its own track) recorded 10,987 ca...
  </details>

- **2026-09-09** — Jorio Cocola, Lev McKinney, Harry Mayne et al. — [Story Imprinting: AI Assistants Absorb Traits from Human Characters They Resemble](http://arxiv.org/abs/2609.10883v1)
  <details><summary>📄 Abstract</summary>
  Language models are trained to implement a helpful AI Assistant character (e.g., Claude). We explore how finetuning on synthetic stories affects this character. Does it change the Assistant's behavior in multi-turn conversations with users, a format quite different from the stories? And does the Assistant adopt the behaviors and preferences of human characters? We refer to this adoption as story imprinting. We finetune GPT-4.1 and Kimi-K2.6 on stories in which generally helpful human characters ...
  </details>

- **2026-09-09** — Yi Shi, Tanyu Chen, Kai Shen — [How Fragile Is Safety Alignment at Frontier Scale? A Single-Direction Attack on a 320B MoE](http://arxiv.org/abs/2609.09793v1)
  <details><summary>📄 Abstract</summary>
  Directional ablation removes an aligned language model's ability to refuse by projecting a single "refusal direction" out of the weights that write the residual stream. It needs no gradient-based training and no optimization, only a few hundred contrastive prompts, which makes it the canonical white-box attack on open-weight alignment. However, it has been established only on dense models up to roughly 70B parameters. We study whether it survives the shift to frontier mixture-of-experts (MoE) mo...
  </details>

- **2026-09-09** — Md. Masudul Islam, Galib Muhammad Shahriar Himel, Md. Golam Moazzam et al. — [Precision in Rice Variety Classification using Stacking-Based Ensemble Learning](http://arxiv.org/abs/2609.10524v1)
  <details><summary>📄 Abstract</summary>
  Rice, a staple food for a significant portion of the global population, exhibits remarkable diversity in its varieties, presenting substantial challenges for accurate identification by consumers, traders, and farmers. This complexity often facilitates fraudulent practices, such as the unauthorized mixing of rice types, which undermines quality and trust in the supply chain. Despite its critical importance, existing research falls short of providing robust and efficient methods for precise rice v...
  </details>

- **2026-09-09** — Jing Guan, Yachao Yang, Zhaoliang Liu et al. — [Active Adaptation, Not Static Defense: Temporal Dynamics of Preventative Steering in Adversarial Fine-Tuning](http://arxiv.org/abs/2609.10142v1)
  <details><summary>📄 Abstract</summary>
  Large language models remain fragile against malicious fine-tuning, motivating training-time defenses against harmful persona drift. Preventative Steering injects undesirable-trait persona vectors during fine-tuning and removes them at evaluation time, yet the mechanism behind its lasting protection remains unclear. Analyzing its temporal optimization dynamics, we find that the defense emerges from an early compensatory adaptation phase followed by a steady-state phase where the corrective signa...
  </details>

- **2026-09-09** — Phil Blandfort, Urja Pawar — [Strangers to Themselves: What Language Models Say About Themselves Is Generic](http://arxiv.org/abs/2609.09899v1)
  <details><summary>📄 Abstract</summary>
  Language models can fluently describe how they would behave: whether they would cave to pushback, misuse a tool, or lie under pressure. Is that description actually about the model speaking? We turn self-knowledge into a prediction test. Across nine behavioral evaluations, we measure how a model behaves under different conditions, ask it to predict those rates, and compare its predictions with controls that remove the self from the question. We find that: (i) Direct self-report is weak (r = +0.0...
  </details>

- **2026-09-09** — Hamed Jelodar, Amir Firouzi, Yen-Wu Lo et al. — [Can Artificial Intelligence Support Healthcare and Mental Health Through Early Cyberbullying Detection ? The Impact of Emotion-Aware AI on Proactive Online Safety](http://arxiv.org/abs/2609.09735v1)
  <details><summary>📄 Abstract</summary>
  Healthcare systems, mental health, and public well-being are increasingly affected by cyberbullying and harmful online interactions. This paper presents CareGuard, an early-warning framework designed to support healthcare-driven mental health protection and proactive online safety through the detection of cyberbullying-related content using advanced natural language processing techniques. CareGuard integrates zero-shot semantic labeling with fine-tuned transformer-based models, including BERT, D...
  </details>

- **2026-09-09** — Song Wu, Bo Wang, Yifan Zhang et al. — [When Ad Networks Misbehave: Understanding Risks of Semi-Drive-By Splash Ads](http://arxiv.org/abs/2609.09574v1)
  <details><summary>📄 Abstract</summary>
  We investigate the mobile splash ads ecosystem, i.e., full-screen advertisements shown at app launch, where monetization relies on interaction signals that are difficult to verify end-to-end. This setting is especially sensitive because incidental touches and sensor-driven callbacks are common yet easy to misattribute as engagement. Prior work has largely framed mobile ad fraud as a publisher-side problem, while some studies attribute fraudulent operations to embedded ad libraries. Yet an import...
  </details>

- **2026-09-08** — Sunny Yasser, Anas Dorbani, Amine Mhedhbi — [Factorized and Vectorized Execution: Optimizing Analytical and Semantic Queries over Relations](http://arxiv.org/abs/2609.09002v1)
  <details><summary>📄 Abstract</summary>
  Many-to-many joins are central to analytical and semantic workloads such as fraud detection, network analysis, and recommendation, where insights arise from relationships between entities. These workloads often suffer from an explosion of intermediate results, sometimes orders of magnitude larger than the inputs. Factorized representations address this problem by exploiting conditional independence among attributes to encode intermediates more compactly. In some cases, they can reduce the output...
  </details>

- **2026-09-08** — Bangshuo Zhu, Wei Song, Yuxin Cao et al. — [Do Input-Level Defenses Transfer to Observation-Level Attacks on VideoLLMs?](http://arxiv.org/abs/2609.08331v1)
  <details><summary>📄 Abstract</summary>
  Video Large Language Models (VideoLLMs) are increasingly deployed in safety-critical applications such as content moderation and video analytics. To process long videos efficiently, VideoLLMs rely on frame sampling, token compression, and modality fusion, which together form an observation pipeline that reduces the raw video to a compact internal representation. Recent observation-level attacks exploit this pipeline to prevent the model from perceiving harmful content, yet no defense has been ex...
  </details>

- **2026-09-08** — Minghang Liu, Qiang Qiu, Yuanzhuo Wang et al. — [Less Is Personal: Learning Minimal Sufficient User Profiles for Personalized Language Models](http://arxiv.org/abs/2609.08180v1)
  <details><summary>📄 Abstract</summary>
  Retrieval-augmented personalization enables large language models to produce more accurate and preference-aligned outputs using relevant records retrieved from user histories. Personalized language models typically prepend a fixed number of retrieved user records, even when additional history is redundant, harmful, or unrelated to a user's distinctive behavior. We study minimal sufficient personalization: constructing the least costly ordered profile for each input while preserving the utility a...
  </details>

- **2026-09-08** — Siru Jiang, Yuwei Liang, Jian Liang et al. — [To Adapt or Not to Adapt? Selective Adaptation for Vision-Language Models](http://arxiv.org/abs/2609.08367v1)
  <details><summary>📄 Abstract</summary>
  Test-time adaptation (TTA) has emerged as a prominent strategy for adapting vision-language models to distribution shifts during inference. We conduct a per-sample analysis of model predictions before and after adaptation, and observe two failure modes in existing TTA methods that echo previous work. Adaptations are frequently negligible, yielding no change in the model's predictions, and more severely, they can be detrimental by flipping previously correct predictions to incorrect ones. This na...
  </details>

- **2026-09-08** — Zixuan Liu, Fangzheng Wu, Brian Summa et al. — [Risk-Conditioned Fine-Tuning of Large Language Models](http://arxiv.org/abs/2609.08064v1)
  <details><summary>📄 Abstract</summary>
  Large Language Models (LLMs) are increasingly deployed in settings where rare but severe harmful generations can have significant consequences. Existing Risk-Averse RLHF addresses this issue by optimizing Conditional Value-at-Risk (CVaR), but it trains policies for fixed risk levels and therefore cannot adjust the desired degree of risk aversion at inference time. In this paper, we propose risk-conditioned RLHF, a framework that trains a single policy that provides a continuous risk-control inte...
  </details>


### 📂 red-teaming
*红队测试 / Red Teaming* — 2 papers

- **2026-09-09** — Arnab Chattopadhayay, Debdipta Halder — [Belief-State Engine: Augmenting LLMs for Principled Planning Under Partial Observability](http://arxiv.org/abs/2609.10036v1)
  <details><summary>📄 Abstract</summary>
  Large language model agents produce fluent action sequences across a wide range of tasks, yet they fail in characteristic ways once the environment becomes partially observable. Ambiguous feedback pushes them into premature commitments. A single informative observation can collapse their uncertainty onto the wrong hypothesis. Policies drift as the history grows. We trace these symptoms to a common structural cause. An LLM agent, as commonly deployed, is a history-conditioned policy with no expli...
  </details>

- **2026-09-08** — Yixuan Liu, Zilong Zhen, Yin Wu et al. — [PrivEscalate: Measuring and Augmenting the Threat of LLM-Automated Linux Privilege Escalation](http://arxiv.org/abs/2609.09087v1)
  <details><summary>📄 Abstract</summary>
  As Large Language Model (LLM) agents increasingly automate offensive operations across the cyber kill chain, their efficacy in complex local post-exploitation tasks remains inadequately quantified. Among these, Linux privilege escalation is a key step between initial access and full system compromise. However, existing evaluations for this task are limited by small sample sizes (fewer than 15 scenarios), lacking the scale to compare model capabilities under executable verification. To address th...
  </details>


### 📂 vulnerability
*漏洞与攻击面 / Vulnerabilities & Attack Surfaces* — 50 papers

- **2026-09-10** — Varun Teja Chundru, Debasmita Biswas — [Domain-Specific Hallucination Detection in Large Language Models](http://arxiv.org/abs/2609.11878v1)
  <details><summary>📄 Abstract</summary>
  Large language models generate fluent text that can contain unfaithful claims -- a phenomenon known as hallucination. We present a multi-signal detection pipeline combining fine-tuned DeBERTa-v3 classification, Monte Carlo (MC) Dropout uncertainty quantification, and temperature-scaled calibration for response-level hallucination detection. Evaluated on the HaluEval benchmark, our pipeline achieves F1=0.915 and AUROC=0.977 on general-domain tasks, with per-task F1 scores of 0.97 (QA), 0.96 (Summ...
  </details>

- **2026-09-10** — Vartika Singh, Philip N. Brown — [Truncated Noisy Best-Response Algorithms: Toward Game Theoretic Learning with Safety Guarantees](http://arxiv.org/abs/2609.11863v1)
  <details><summary>📄 Abstract</summary>
  We consider a game theoretic approach to solve multi-agent coordination problems with submodular maximization objectives. It is known for such problems that the Nash equilibria for the corresponding game are always within 50% of the optimal, but that the equilibria which achieve this worst-case bound are not stable. To exploit this instability, we propose a family of algorithms which we call Truncated Noisy Best-Response (TNBR) Algorithms. These algorithms are flexibly characterized by agents as...
  </details>

- **2026-09-10** — Yedidel Louck, Amit Dvir, Ariel Stulman — [Signing the Transaction but Not the Decision: Whisper Attacks and a Binding Defense for AP2](http://arxiv.org/abs/2609.11757v1)
  <details><summary>📄 Abstract</summary>
  Software agents are beginning to shop and pay on a person's behalf. Agent payment protocols such as AP2 produce cryptographically valid signatures for completed purchases, yet do not constrain the decisions that lead to them. Consequently, ordinary product-description text can steer a shopping agent into forming a cart that passes every protocol check but no longer matches the user's request. In this paper, we show that this vulnerability enables three related attacks. In the first attack, the a...
  </details>

- **2026-09-10** — Miguel A. Avendaño-Bernal, Srinandan Dasmahapatra, Ahmed Hammad et al. — [Hunting the Unseen: Deep Learning Analysis for Semi-Visible Jet Tagging](http://arxiv.org/abs/2609.11692v1)
  <details><summary>📄 Abstract</summary>
  Semi-Visible Jets (SVJs) constitute a distinctive collider signature of strongly interacting dark sectors, embedding Dark Matter candidates, wherein jets contain both visible Standard Model objects and invisible dark hadrons, giving rise to correlated jet activity and missing transverse momentum. In this work, we investigate SVJs produced through a heavy Z' mediator and perform an study over a representative set of benchmark scenarios spanning different mediator masses and dark sector parameters...
  </details>

- **2026-09-10** — Nathaniel Hendrix, Carl Y. Zhang, Chris Heitzig et al. — [Geospatial Foundation Models Capture Health-Relevant Dimensions of Place Beyond Conventional Social Risk Indices](http://arxiv.org/abs/2609.11689v1)
  <details><summary>📄 Abstract</summary>
  Area-based social risk indices summarize residents' socioeconomic conditions but incompletely capture physical features of place that may affect health. We evaluated whether numerical representations of physical place produced by four geospatial foundation model families from 2022 satellite data explained residual variance in tract-level associations between the Area Deprivation Index, Social Deprivation Index, and Social Vulnerability Index with health outcomes. We used LightGBM to predict vari...
  </details>

- **2026-09-10** — Martin Andersson, Tung T. Vu, Pål Frenger et al. — [Leveraging Slowly Time-Varying AP-AP Channels for Interference Mitigation in Dynamic TDD](http://arxiv.org/abs/2609.11669v1)
  <details><summary>📄 Abstract</summary>
  We address the challenge of cross-link interference in dynamic time-division duplexing (TDD) systems. Specifically, we focus on mitigating the interference caused by access points (APs) operating in downlink to APs operating in uplink. To this end, we exploit that channels between APs typically vary much more slowly over time than channels between users and APs. This observation allows us to jointly estimate the uplink user data and the AP-AP channels using a least-squares formulation over multi...
  </details>

- **2026-09-10** — Christophe Cheverry, Zied Ammari — [The Schrödinger-Klein-Gordon System Revisited](http://arxiv.org/abs/2609.11658v1)
  <details><summary>📄 Abstract</summary>
  We introduce a microlocal formulation of the Schr{ö}dinger-Klein-Gordon system describing the interaction between a non-relativistic quantum particle and a Klein-Gordon field through Yukawa coupling. Instead of working directly with the Schr{ö}dinger wave function, we represent the quantum component by its Fourier-Wigner transform, and we rewrite the Klein-Gordon equation in terms of a complex Fourier variable. Eliminating the field variable yields a closed nonlinear Fourier-Moyal equation on ph...
  </details>

- **2026-09-10** — Hao Dong, Xun-Jiang Luo, Xiao-Hong Pan et al. — [Phase-Controlled Majorana Zero Modes in Altermagnetic Topological-Insulator Josephson Junctions](http://arxiv.org/abs/2609.11633v1)
  <details><summary>📄 Abstract</summary>
  We exploit facet-dependent Andreev phase shifts to control topological superconductivity with a phase bias in a three-dimensional altermagnetic topological-insulator Josephson junction. In the weak link between two conventional s-wave superconductors, the d-wave altermagnetic order produces facet-dependent momentum shifts of the surface Dirac cones. The resulting net momentum of the states involved in Andreev reflection generates additional propagation phases that differ between facets. Conseque...
  </details>

- **2026-09-10** — Kai Ma, Quanfeng Lv, Jingguo Ge et al. — [Entwine: Coordinating Tiled Computation and Fine-Grained Communication across GPUs](http://arxiv.org/abs/2609.11562v1)
  <details><summary>📄 Abstract</summary>
  Modern high-performance GPU computations partition tensors into tiles to exploit data reuse and parallelism. Individual tile computations complete earlier than the full tensor computation, creating opportunities to overlap computation and communication. However, a mismatch between computation and communication progress can limit these opportunities. Communication stalls when no data is ready, and may lag when data arrives in bursts. Communication can also slow computation by consuming shared res...
  </details>

- **2026-09-10** — Patrick Rebling, Philipp Nenninger, Reiner Kriesten — [CARLAverse: A Highly Modular, Distributed, and Multimodal Framework for Human-in-the-Loop Simulation](http://arxiv.org/abs/2609.11478v1)
  <details><summary>📄 Abstract</summary>
  The development of autonomous driving demands comprehensive testing in mixed-traffic scenarios involving vulnerable road users (VRUs), where purely artificial agents often fail to capture authentic human social negotiations. While human-in-the-loop (HITL) simulators enable safe investigation of these interactions, existing multi-agent platforms struggle with the network latency and synchronization constraints required for high-fidelity haptic feedback. To resolve this, we present CARLAverse, an ...
  </details>

- **2026-09-10** — Peiyuan Gao, Gaoyuan Zhang, Haojie Qin et al. — [VikingRAG: Accurate and Token-efficient Retrieval-augmented Generation over Structured Documents](http://arxiv.org/abs/2609.11390v1)
  <details><summary>📄 Abstract</summary>
  State-of-the-art retrieval-augmented generation (RAG) methods exploit document structures to acquire sufficient evidence, but often incur substantial token costs. To reduce structural-context tokens without compromising high RAG accuracy, we present {\sf VikingRAG}, a directory-aware semantic data management system that tightly integrates semantic and structural access to support structural-context-efficient, evidence-gap-driven multi-round retrieval. To further reduce token overhead of multi-ro...
  </details>

- **2026-09-10** — Yosuke Hashidate — [Social Preferences and Cooperation: Beliefs, Robustness, and the Limits of Altruism](http://arxiv.org/abs/2609.11374v1)
  <details><summary>📄 Abstract</summary>
  We study a mechanism of cooperation in the Prisoner's Dilemma (PD). Incorporating social preferences as efficiency concerns into the PD game, we study how altruism translates into cooperation. Under complete information, cooperation requires the opponent's altruism to clear a threshold. We then introduce a subjective extension of Bayesian Nash equilibrium that relaxes the Common Prior Assumption, letting players hold heterogeneous, potentially misspecified beliefs about each other's altruistic t...
  </details>

- **2026-09-10** — Xingyi He, Ziwei Wang, Dongrui Wu — [RAMamba-Net: A Reliability-Aware and Mamba-Based Multimodal Fusion Network for Auditory Attention Detection](http://arxiv.org/abs/2609.11372v1)
  <details><summary>📄 Abstract</summary>
  Auditory attention decoding (AAD) identifies the attended speaker from physiological signals, supporting neuro-steered hearing devices and natural human-machine interaction. Electroencephalography (EEG) is the dominant modality for AAD but provides incomplete evidence in naturalistic audio-visual scenes, motivating EEG and electrooculography (EOG) fusion. Existing approaches remain limited by weak cross-modal interaction, inefficient temporal modeling, and low robustness to sample variations. To...
  </details>

- **2026-09-10** — Ziwei Wang, Xingyi He, Hongbin Wang et al. — [Exploring Diffusion Transformers for Cross-Modal Augmentation in Multimodal Brain State Decoding](http://arxiv.org/abs/2609.11341v1)
  <details><summary>📄 Abstract</summary>
  Multimodal brain state decoding has largely focused on fusing paired modalities for prediction, but has rarely explored how their correspondence can be further exploited to enrich training data and improve multimodal representation learning. To address this gap, we propose CoMA-DiT, a bidirectional cross-modal Diffusion Transformer for latent augmentation that treats paired modalities as sources of mutual generative supervision rather than merely as inputs to be fused. CoMA-DiT conditions veloci...
  </details>

- **2026-09-10** — Alessio Ferrari, Minh An Nguyen, Kushal Ramkumar et al. — [Exploring the Role of Security Experience and ChatGPT Usage Strategies on Secure Software Engineering Education](http://arxiv.org/abs/2609.11303v1)
  <details><summary>📄 Abstract</summary>
  The rapid adoption of Large Language Models (LLMs) is reshaping software engineering education, but their role in secure software engineering education remains underexplored. We report an exploratory empirical study of how 26 graduate students in a part-time MSc Cybersecurity programme used ChatGPT during a vulnerability-fixing assignment. To characterise ChatGPT use, we analysed students' ChatGPT interaction logs using a structured double-coding procedure and examined whether usage patterns and...
  </details>

- **2026-09-10** — Mengming Li, Ceyu XU, Qijun Zhang et al. — [Memory Compression for High-Fanout Agent Sandboxes](http://arxiv.org/abs/2609.11294v1)
  <details><summary>📄 Abstract</summary>
  High-fanout agent workloads create a growing memory bottleneck because a single task may spawn many concurrent sandbox sessions. Yet these sandboxes are far from independent: they originate from a shared template and execute related trajectories, exposing substantial template-relative and cross-sandbox memory redundancy. Conventional memory compression is poorly matched to this setting in three fundamental dimensions: how to compress, because they fail to exploit similarity across non-identical ...
  </details>

- **2026-09-10** — Leonard Pleschberger — [Discrete Hyperbolic Secant Distributions](http://arxiv.org/abs/2609.11293v1)
  <details><summary>📄 Abstract</summary>
  We introduce a family of discrete hyperbolic secant distributions on $\mathbb{Z}$, whose normalizing constants arise from series values calculated by Ramanujan and are expressed in terms of Gauß' constant $G=\varpi/π$, where $\varpi=Γ^2(1/4)/(2\sqrt{2π})$ is the lemniscate constant. Using the elliptic lambda-star function $λ^*$, we construct scaled versions of these distributions parametrized by $\sqrt{r}$ and $1/\sqrt{r}$ for $r \in \mathbb{N}$. For the first such distribution, we compute the m...
  </details>

- **2026-09-10** — Daniel Akselrad, Robert N. Proctor — [INDRA: A New AI Tool for Exploring Tobacco, Fossil Fuel, and Chemical Industry Archives](http://arxiv.org/abs/2609.11261v1)
  <details><summary>📄 Abstract</summary>
  Five decades of litigation have disgorged hundreds of millions of pages of formerly secret business records from the tobacco industry, along with documents from the makers of drugs, chemicals, food, firearms, and fossil fuels. Yet these archives have been effectively inaccessible to general-purpose large language models (LLMs) because they have never been compiled into an LLM-readable corpus. Chatbots may be familiar with some of the materials contained in such archives but, with no direct acces...
  </details>

- **2026-09-10** — Muhammad Fahad Bashir, Muhammad Afzal — [An AI-Powered Culturally Aware Chatbot for Stress Detection and Wellness Support among Pakistani University Students Using NLP and Machine Learning](http://arxiv.org/abs/2609.11199v1)
  <details><summary>📄 Abstract</summary>
  With the existing digital mental health tools specifically developed for Western settings, Pakistani students are exposed to a uniquely compounded stress situation in their university that includes academic, financial, familial, and relational stressors, which have become a serious concern for academic and psychological development of students in Pakistani universities. This paper introduces a new, AI-driven and culturally sensitive stress detection and wellness support system that is tailored t...
  </details>

- **2026-09-10** — Vikash Singh, Debargha Ganguly, Aman Goel et al. — [Beyond Solver Verdicts: Generative Reward Models for Autoformalization](http://arxiv.org/abs/2609.11085v1)
  <details><summary>📄 Abstract</summary>
  Neurosymbolic systems rely on mathematical solvers to guarantee reasoning correctness, yet solvers are fundamentally blind to whether a formal translation maintains strict reference-equivalence to a designated formalization. We formalize this vulnerability as Verdict-Preserving-Unfaithfulness (VPU): a failure mode where an incorrect encoding executes successfully and matches the expected verdict. We theoretically prove that structural, verdict-only verification heuristics are mathematically boun...
  </details>

- **2026-09-10** — Jiarong Lian, Zhe Xiao, Zhaoyang Zhang et al. — [RIDE: Relocalization-Informed Depth Estimation with 3D Gaussian Splatting](http://arxiv.org/abs/2609.11079v1)
  <details><summary>📄 Abstract</summary>
  Render--match--PnP relocalization establishes correspondences between query image pixels and 3D map points for camera pose recovery, but their potential to support dense depth estimation is often overlooked. To exploit this geometric information, we present RIDE, which estimates dense metric depth from a robot's RGB stream. Given a metrically scaled 3D Gaussian Splatting (3DGS) model, RIDE combines sparse metric depth observations derived from PnP-RANSAC inlier correspondences with the geometric...
  </details>

- **2026-09-10** — Lingyuan Kong, Jiaqi Cui, Fanjiao Zeng et al. — [UniRec: Cross-stage Multi-Task Fusion with Preference Alignment for Cascaded Recommender Systems](http://arxiv.org/abs/2609.11052v1)
  <details><summary>📄 Abstract</summary>
  Industrial recommender systems use cascaded stages with different objectives, feature spaces, and latency constraints. Optimizing pre-ranking and ranking separately can create cross-stage inconsistency: upstream models may filter out items preferred by downstream rankers, and independently tuned downstream fusion can offset upstream improvements. Existing multi-task fusion methods focus on multi-objective fusion within the ranking stage, and cross-stage methods typically only add a downstream sc...
  </details>

- **2026-09-10** — Shenghan Zheng, Zonglin Di, Yimin Liu et al. — [BenchShield: Formal Model-Backed Instrumentation for Reward Integrity in LLM-Agent Evaluation Infrastructure](http://arxiv.org/abs/2609.11028v1)
  <details><summary>📄 Abstract</summary>
  LM-agent benchmarks increasingly function as interactive evaluation infrastructure. Agents observe state, call tools, modify workspaces,   submit artifacts, and receive rewards from outcome procedures. This interactivity makes evaluations vulnerable to reward hacking: an agent   improves its measured score by exploiting the reward-relevant trajectory instead of solving the intended task. Existing defenses rely largely   on task-specific patches, prompt instructions, or post-hoc detectors. They d...
  </details>

- **2026-09-10** — Rui Cao, Shaojing Fan, Liming Fang et al. — [DeFiFusion: Combining Transaction Events with Smart Contracts to Detect Price Manipulation Attacks](http://arxiv.org/abs/2609.11008v1)
  <details><summary>📄 Abstract</summary>
  Decentralized Finance (DeFi) has emerged as a rapidly growing blockchain-based financial service, where market transaction dynamics and underlying smart contract logic are intricately intertwined. This autonomous interplay, while eliminating centralized intermediaries, significantly expands the vulnerability surface of DeFi protocols to Price Manipulation Attacks (PMAs), which have already inflicted catastrophic financial losses. Despite their gravity, existing detection paradigms suffer from fu...
  </details>

- **2026-09-10** — Mohammad Farhad, Shuvalaxmi Dass — [LLMVul: A Vulnerability-Labeled Dataset of LLM-Generated C/C++ Functions from Real Production Repositories](http://arxiv.org/abs/2609.10945v1)
  <details><summary>📄 Abstract</summary>
  Large language models (LLMs) are increasingly used to generate and assist with software development, yet existing vulnerability datasets largely focus on human-written code or controlled prompting environments. This limits the ability to study security weaknesses in LLM-generated code as it appears in real-world software projects. We present LLMVul, a vulnerability-labeled dataset of LLM-generated C/C++ functions mined from real production repositories. We mine AI-assisted development activity f...
  </details>

- **2026-09-10** — Muhammad Umair, Jan P. de Ruiter — [Using Semantic Uncertainty to Estimate Transition Relevance in Turn-taking](http://arxiv.org/abs/2609.10934v1)
  <details><summary>📄 Abstract</summary>
  Turn-taking is a fundamental mechanism that governs when interlocutors speak and listen. Although Spoken Dialogue Systems (SDS) exploit a range of linguistic, acoustic, and non-verbal cues, they produce ill-timed responses in unscripted interaction. A central challenge is anticipating Transition Relevance Places (TRPs), or opportunities, not obligations, for a listener to take the floor. Human listeners do not wait for turn endings; as an utterance unfolds, they use expectations about its develo...
  </details>

- **2026-09-09** — Alireza Lotfi, Mirza Masfiqur Rahman, Imtiaz Karim et al. — [A2ABreak: Systematic Security Analysis of the A2A Protocol](http://arxiv.org/abs/2609.10871v1)
  <details><summary>📄 Abstract</summary>
  The Agent2Agent (A2A) protocol, now governed by the Linux Foundation, is an open standard that enables autonomous AI agents to discover, authenticate with, and delegate tasks to one another across organizational boundaries. Designed to complement the Model Context Protocol (MCP) for tool integration, A2A is rapidly emerging as the horizontal communication layer of the multi-agent ecosystem. Yet the protocol's security has received no systematic analysis.   This paper presents A2ABreak, the first...
  </details>

- **2026-09-09** — Victoria Lovelace, Cameron Berryman, Yuhan You et al. — [Big Enough to Break Out: Tracking the Rising Capability of LLM Penetration-Testing Agents](http://arxiv.org/abs/2609.10780v1)
  <details><summary>📄 Abstract</summary>
  Large language model (LLM) agents are increasingly applied to penetration testing, but we still know little about what they can do or how they fail. We compare two PentestGPT-based systems: a legacy human-in-the-loop system running the open-weight Kimi K2.5, and a newer autonomous system running Claude Opus 4.8. Across three public targets, the autonomous system solves all three, including the two the legacy system never finishes. The legacy result is the more surprising of the two. Even on the ...
  </details>

- **2026-09-09** — Jessica Pourleyli, Maitreyee Das Urmi, Glaucia Melo — [Beyond Static Guarantees: Measuring the Static-Pass Dynamic-Fail Gap in Security-Sensitive and LLM-Generated Python Code](http://arxiv.org/abs/2609.10762v1)
  <details><summary>📄 Abstract</summary>
  Advances in large language models (LLMs) fuel the quest for scalable methods to assess the security of generated and security-sensitive software. Static analysis is widely adopted as a scalable, reproducible, and inexpensive security gate, but cannot directly observe runtime exploit behaviour. Vulnerabilities dependent on adversarial inputs, execution context, or exploit chaining may evade static checks while remaining exploitable in practice, yet passing static analysis is often treated as evid...
  </details>

- **2026-09-09** — Boshu Jia, Rongyu Chen, Linlin Yang et al. — [MHE-Former: Multi-Hypothesis Transformers via Entropy Maximization for 3D Mesh Recovery](http://arxiv.org/abs/2609.10743v1)
  <details><summary>📄 Abstract</summary>
  Monocular 3D hand and body mesh recovery often suffers from severe occlusion and ambiguity. Traditional deterministic methods typically regress a single optimal solution, leading to overconfident predictions. In this paper, we introduce an exploration--exploitation paradigm for ambiguous mesh recovery with multi-hypothesis learning and selection. Specifically, during exploration, based on our probabilistic formulation and entropy maximization, we propose a novel multi-hypothesis method referred ...
  </details>

- **2026-09-09** — Ivana Clairine Irsan, Ratnadira Widyasari, Huihui Huang et al. — [Towards Scalable and Cost-Efficient Vulnerability Detection: A Study on Automatic Query Generation](http://arxiv.org/abs/2609.10412v1)
  <details><summary>📄 Abstract</summary>
  Static analysis remains a cornerstone of software security, yet the effectiveness of tools such as CodeQL is often limited by the substantial manual effort required to develop high-coverage query suites. While large language models (LLMs) have emerged as a potential solution for automated code reasoning, their practical utility in generating structured, executable security queries remains underexplored. In this paper, we conduct an empirical study to evaluate the ability of LLMs to synthesize Co...
  </details>

- **2026-09-09** — Benedikt Tscheschner, Eduardo Veas, Marc Masana — [One Loop, Two Gains: Can Active Learning win the Lottery for Free?](http://arxiv.org/abs/2609.10311v1)
  <details><summary>📄 Abstract</summary>
  The lottery ticket hypothesis posits the existence of winning tickets: sparse subnetworks that, when trained in isolation from their original initialization, match the accuracy of the full dense network. The predominant method for discovering such tickets, iterative magnitude pruning, alternates pruning with full retraining from scratch until convergence over many cycles. Similarly, deep active learning also retrains a model from scratch after each acquisition round as new labels become availabl...
  </details>

- **2026-09-09** — N'Zolieh Ismaël Mahassadi, Raphaël Khoury, Justin Vallé et al. — [An Empirical Analysis of ReDoS Vulnerabilities and ReDoS Detection Tools](http://arxiv.org/abs/2609.10294v1)
  <details><summary>📄 Abstract</summary>
  ReDoS vulnerabilities are a type of denial of service software weakness that occurs when a regex is used to validate user-supplied input. In some cases, the regex matching process can take exponential time, leading to a denial of service. In this study, we examine and compare the effectiveness of five publicly-available regex detection tools, and one regex correction tool, using three datasets. We further perform an empirical analysis of all ReDoS vulnerabilities reported to the NVD database in ...
  </details>

- **2026-09-09** — Soroush Karimi, Marcos Oliveira, Diogo Pacheco — [How neighbourhood ideology shapes misinformation belief in densely tied social networks](http://arxiv.org/abs/2609.10277v1)
  <details><summary>📄 Abstract</summary>
  With the rapid spread of news on social media, understanding the propagation of misinformation is becoming increasingly important. One factor that affects individuals' vulnerability to false information is their ideological predisposition. Despite the large number of agent-based models that focus on social influence as a driver of the spread of false claims, they often fail to explicitly integrate personal ideological biases into belief formation. In this work, we explore how misinformation spre...
  </details>

- **2026-09-09** — Jean Leneutre, Dylan Marinho, Vadim Malvone et al. — [Execution-Time Opacity Logic: A Logic for Ensuring ET-Opacity in Timed Systems](http://arxiv.org/abs/2609.10066v1)
  <details><summary>📄 Abstract</summary>
  Ensuring confidentiality in Cyber-Physical Systems is critical, especially when attackers exploit execution times to infer sensitiveinformation. Traditional opacity models are inadequate for timed systems, as verifying opacity in Timed Automata is undecidable. To address this challenge, we propose Execution-Time Opacity Logic (ETOL), a new formalism that specifies opacity by requiring that for every execution satisfying a secret formula, there exists another execution of the same duration that d...
  </details>

- **2026-09-09** — Mingcheng Nie, Hao Chang, Xiaoqi Zhang et al. — [Channel Estimation for OFDM via Delay-Doppler Refinement](http://arxiv.org/abs/2609.09782v1)
  <details><summary>📄 Abstract</summary>
  In this paper, we propose a novel channel estimation (CE) algorithm for orthogonal frequency division multiplexing (OFDM) systems that exploits the unique characteristics of the delay-Doppler (DD) domain channel. Specifically, the time-frequency (TF) domain input-output relationship (IOR) is derived in a compact form by focusing solely on the non-zero elements of the TF domain channel matrix. Based on this compact IOR, a coarse TF domain CE is first performed using a linear minimum mean square e...
  </details>

- **2026-09-09** — Sachin K. Sen, Gour C. Karmakar, Shaoning Pang — [Quantifying IIoT Sensor Node Criticality by Fusing its Data Criticality and Security Vulnerability](http://arxiv.org/abs/2609.09807v1)
  <details><summary>📄 Abstract</summary>
  The integration of the Industrial Internet of Things (IIoT) into manufacturing has transformed industrial operations by optimising production management and ensuring product quality through smart industrial sensors that regulate processes based on real-time data. However, these sensor nodes are highly vulnerable to cyber threats, posing significant security risks that compromise their reliability and integrity. While existing research explores cybersecurity vulnerabilities and cyberattack-based ...
  </details>

- **2026-09-08** — Antonino Vaccarella, Lanpei Li, Vincenzo Lomonaco et al. — [Smart Adaptive Computing Across the Continuum: LLMs in IoT-Edge-Cloud Resource Management](http://arxiv.org/abs/2609.09348v1)
  <details><summary>📄 Abstract</summary>
  Managing resources across IoT, edge, and cloud layers calls for continuous, context-aware decisions under constraints that rarely stay fixed. Deep reinforcement learning (DRL) handles this class of problems well, and large language models (LLMs) are increasingly used to augment DRL pipelines, yet the architectural relationship between the two is seldom made explicit. We build on Wang et al.'s taxonomy of Continuum Orchestration Systems employing DRL techniques and extend it with two further dime...
  </details>

- **2026-09-08** — Md. Wasiul Haque, Sagar Dasgupta, Mizanur Rahman — [LLMSec-AV: A Vulnerability Taxonomy and LLM-Driven Software Weakness Discovery Framework for Autonomous Vehicles](http://arxiv.org/abs/2609.09386v1)
  <details><summary>📄 Abstract</summary>
  Automated vehicles rely on millions of lines of safety-critical software, yet general-purpose analyzers do not understand which code can affect vehicle motion. This study asks whether large language models (LLMs) with explicit automated-vehicle (AV) security knowledge improve weakness detection beyond rule-based tools. We developed an AV vulnerability taxonomy with 18 weakness classes from vulnerability records, security advisories, and AV-security literature, and integrated it into LLM-based Se...
  </details>

- **2026-09-08** — Tobias Susetzky, Raphael Rehms, Dmitrii Seletkov et al. — [NOAH: Learning the Full Patient Journey. A Longitudinal Multimodal Time-Aware Model for Representation and Forecasting](http://arxiv.org/abs/2609.09140v1)
  <details><summary>📄 Abstract</summary>
  The digitization of healthcare has generated vast, longitudinal, and multimodal patient records over a lifetime, yet fully exploiting these data to represent and predict patient state trajectories remains a critical challenge. Current AI models often struggle to capture the complex, irregular temporal dynamics and inherent stochasticity of real-world multimodal patient data. Existing AI approaches for modeling longitudinal patient records are predominantly discriminative, limited to a few modali...
  </details>

- **2026-09-08** — Thodoris Betsas, Anastasios Doulamis, Andreas Georgopoulos — [GoDeep: Annotation-Free Open-Vocabulary 3D Scene Understanding via Language-Space Lifting](http://arxiv.org/abs/2609.09082v1)
  <details><summary>📄 Abstract</summary>
  Open vocabulary 3D semantic segmentation methods typically lift CLIP features into 3D. This embeds points in a joint vision-language space known to behave like a bag-of-words on compositional tasks. Furthermore, even annotation free variants often require a large 3D training corpus and a dedicated 3D encoder per domain. Instead we use a vision-language model purely as a translator. It produces structured, entity-level descriptions of each posed image. These descriptions are grounded, projected, ...
  </details>

- **2026-09-08** — Jinyu Miao, Jiusi Li, Yifei He et al. — [Leveraging Visual and Geometric Priors for Metric-scale and Complete Vehicle Gaussian Reconstruction from Limited Views](http://arxiv.org/abs/2609.08841v1)
  <details><summary>📄 Abstract</summary>
  High-fidelity vehicle assets are essential for controllable traffic scene generation, particularly for synthesizing rare and safety-critical long-tail scenarios. However, reconstructing a reusable vehicle representation from in-the-wild onboard images remains challenging for two reasons. First, image-to-3D generation methods generally produce models without reliable metric scale. Second, onboard cameras usually observe only one side of a target vehicle, making conventional multi-view reconstruct...
  </details>

- **2026-09-08** — Sarah Meriem Ourari — [Measuring the Security of the Evolving Software Supply Chain: a Research Agenda](http://arxiv.org/abs/2609.08810v1)
  <details><summary>📄 Abstract</summary>
  Software supply chain security has become increasingly critical due to the widespread reliance on third-party dependencies and the growing attack surface of modern software ecosystems. However, existing quantitative, measurement-based analysis and vulnerability management approaches remain largely fragmented and ecosystem-specific, limiting their ability to provide comparable risk assessments across environments. This paper presents a structured research plan, starting with a Systematization of ...
  </details>

- **2026-09-08** — Mingyu Ma, Yuxin Wu, Jingbo Wang et al. — [Combating Instruction Conflict via Energy-Driven Latent Conflict Detection](http://arxiv.org/abs/2609.08646v1)
  <details><summary>📄 Abstract</summary>
  Large Language Models (LLMs) are increasingly deployed with hierarchical instructions, yet they remain vulnerable to conflicts in which user directives override system-level constraints. Existing defense mechanisms predominantly focus on static input inspection and therefore fail to detect Response Drift, a phenomenon in which the model's final response violates system-level constraints despite seemingly compliant inputs. To bridge this gap, we introduce ELCD, a response-level latent conflict de...
  </details>

- **2026-09-08** — Ang Jia, Yaxin Duan, He Jiang et al. — [PLC-Bin2Src: Retrieving Corresponding Structured Text Source Files for PLC Binaries](http://arxiv.org/abs/2609.08563v1)
  <details><summary>📄 Abstract</summary>
  Software reuse allows existing components and third-party libraries to be incorporated into new applications, but binary-only components can obscure their origins and implementations. Software composition analysis seeks to identify these reused components and trace their provenance, supporting dependency inventory, vulnerability assessment, and security auditing. For PLC applications, binary2source matching provides a core link in this analysis: given an opaque PLC binary artifact, retrieve its ...
  </details>

- **2026-09-08** — Daiki Sasamoto, Joji Nasu — [Schwinger boson perturbation theory for spin-$S$ Kitaev-Heisenberg magnets: phase diagram and dynamical response near Kitaev spin liquids](http://arxiv.org/abs/2609.08548v1)
  <details><summary>📄 Abstract</summary>
  We develop a Schwinger boson perturbative framework for the spin-$S$ Kitaev-Heisenberg model. The spin-liquid saddle point of the pure Kitaev model is used as the unperturbed state, and magnetic instabilities and dynamical spin correlations are evaluated around this saddle point. We decompose the Hamiltonian exactly into two parts by exploiting the Klein duality intrinsic to the Kitaev-Heisenberg model. We perform the random-phase approximation by taking the part invariant under the duality tran...
  </details>

- **2026-09-08** — Zongjie Li, Alan Z. W, John Nicolas J et al. — [Feyospace-v1: How the Cyber Mercury Seven Trained Frontier Cyber Models](http://arxiv.org/abs/2609.08418v1)
  <details><summary>📄 Abstract</summary>
  Training capable cyber agents is often treated primarily as a problem of model scale, yet open-weight post-training is constrained more directly by the cost of executable environments, reliable multi-turn supervision, and access to strong teachers. We present a data-centric framework that addresses these bottlenecks through five complementary systems: Choulea analyzes hidden reasoning signatures, SkyReal reduces teacher-sampling cost, Hongzwang bypasses API restrictions on teacher execution, PSB...
  </details>

- **2026-09-08** — Dawei Fu, Cheng Jiang, Sitian Qian et al. — [SE-GoS: Self-Evolving Graph-of-Skills for Skill Library at Scale](http://arxiv.org/abs/2609.08228v1)
  <details><summary>📄 Abstract</summary>
  Modern LLM agents increasingly rely on reusable skills, yet as skill libraries scale to thousands of entries, effective retrieval becomes a bottleneck. Graph-of-Skills (GoS) addresses this challenge by exploiting dependency-aware graph structure for scalable skill retrieval, while SkillDAG further demonstrates that skill graphs can accumulate execution-backed structure online. However, these approaches leave open whether historical execution traces can be systematically distilled into a better r...
  </details>

- **2026-09-08** — Xinhong Xie, Piyush Nagasubramaniam, Neeraj Karamchandani et al. — [LLM-Based Penetration Testing in the Presence of Honeypots](http://arxiv.org/abs/2609.08093v1)
  <details><summary>📄 Abstract</summary>
  Large language model (LLM) agents are increasingly employed for offensive cybersecurity tasks such as automated vulnerability discovery, reconnaissance, and penetration testing. This new capability also threatens one of the defender's most valuable tools: deception. Traditional honeypots rely on realism and obscurity to lure human or script-driven attackers into revealing tactics, techniques, and procedures (TTPs), but LLM-driven attackers can reason about heterogeneous artifacts and use the hon...
  </details>

- **2026-09-08** — Yuji Zhang, Weibing Wang, Cheng Qian et al. — [Popular Knowledge Propagates More Errors in LLM Knowledge Updating](http://arxiv.org/abs/2609.08067v1)
  <details><summary>📄 Abstract</summary>
  Updating a language model's knowledge through fine-tuning is essential for keeping its outputs current, yet can also induce factual forgetting and new hallucinations. Prior work shows that long-tail knowledge is harder to acquire and newly memorized long-tail facts are difficult to retain during later fine-tuning. We study a complementary question: among facts that a model has encoded correctly, which are most vulnerable to collateral corruption during other updates? To investigate this question...
  </details>


### 📂 defense
*防御与防护方法 / Defense & Protection Methods* — 63 papers

- **2026-09-10** — Simona Boboila, Xavier Cadet, Edward Koh et al. — [BlueSTAR: Tiered Agentic Architecture for Autonomous Cyber Defense](http://arxiv.org/abs/2609.11852v1)
  <details><summary>📄 Abstract</summary>
  Cyber attacks are increasingly automated, narrowing the time available for human analysts to detect, reason about, and respond to intrusions. Large language models (LLMs) offer a promising foundation for autonomous cyber defense because they can correlate heterogeneous evidence and reason about previously unseen threats. However, directly applying LLMs to operational security telemetry is impractical: raw logs arrive faster than current models can process them, individual events are often ambigu...
  </details>

- **2026-09-10** — Matyáš Veselý, Michal Průšek, Jiří Franc — [Your Retriever Already Knows: Distribution-Shape QPP for RAG Retrieval Sufficiency](http://arxiv.org/abs/2609.11646v1)
  <details><summary>📄 Abstract</summary>
  Standard Retrieval-Augmented Generation (RAG) pipelines often provide no reliable inference-time signal of whether retrieval succeeded; on ambiguous or out-of-scope queries, generation may then hallucinate. Motivated by a Czech nuclear-regulator deployment where data sensitivity precludes third-party LLM APIs, we compare three Query Performance Prediction (QPP) paradigms for retrieval sufficiency in RAG: score-based features, a content-based LLM judge, and a hybrid. On the eight ViDoRe vision do...
  </details>

- **2026-09-10** — Michael Neri — [Domain-Incremental Learning for Multi-Channel Replay Speech Detection](http://arxiv.org/abs/2609.11194v1)
  <details><summary>📄 Abstract</summary>
  Replay attacks are the most accessible threat to voice-controlled systems, and the acoustic cues that expose them are strongly modulated by the environment in which the attack is mounted. A detector deployed in the field therefore has to absorb new acoustic conditions over time, ideally without revisiting past recordings, since retaining speech indefinitely is both expensive and legally constrained. We frame this as Domain-Incremental Learning (DIL) over acoustic environments and present the fir...
  </details>

- **2026-09-10** — Bowen Zhang, Hsiu-Wen Cheng, Hongyu Yang et al. — [Evaluating Time-Series Foundation Models and Multimodal Dietary Context for CGM Forecasting](http://arxiv.org/abs/2609.11872v1)
  <details><summary>📄 Abstract</summary>
  Continuous glucose monitoring (CGM) provides high-frequency measurements of glucose dynamics and enables short-term glucose forecasting for diabetes management. Although time-series foundation models have shown strong general forecasting ability, their effectiveness for CGM prediction and the added value of multimodal dietary context remain unclear. We conduct a comprehensive empirical study using eight public CGM datasets spanning Type 1 diabetes, Type 2 diabetes, and non-diabetes populations. ...
  </details>

- **2026-09-10** — Marica Notte, Ludovica Marinucci, Vieri Giuliano Santucci — [Autonomy, Social Norms, and Alignment: Towards a Developmental Framework for Autonomous Artificial Agents](http://arxiv.org/abs/2609.11660v1)
  <details><summary>📄 Abstract</summary>
  In recent years, artificial intelligence has made extraordinary progress thanks to large-scale models capable of generalization and the generation of complex outputs. However, transferring this potential into embodied agents reveals a significant limitation: the most advanced systems rely on pre-existing datasets and human feedback strategies that are powerful but insufficient in dynamic or unknown contexts. To adapt, an agent must acquire knowledge through direct interaction with its environmen...
  </details>

- **2026-09-10** — Mengting Wu, Lin Wang, Yong Zhang et al. — [From Intent to Execution Grant: An Execution-Boundary Conformance Profile for High-Risk AI Actions](http://arxiv.org/abs/2609.11596v1)
  <details><summary>📄 Abstract</summary>
  AI agents increasingly propose actions with external consequences, including financial transfers, infrastructure changes, software deployments, disclosures, and physical actuation. Authorization engines, policy languages, runtime monitors, provenance mechanisms, and agent guardrails provide important foundations, but do not necessarily define a common semantic contract for the final transition from a particular candidate action to execution authority.   We specify EBL-Core, an execution-boundary...
  </details>

- **2026-09-10** — Shenbin Qian, Yves Scherrer — [TransClean: A Benchmark for Detecting and Extracting Clean Translations from Large Language Model Outputs](http://arxiv.org/abs/2609.11399v1)
  <details><summary>📄 Abstract</summary>
  Large language models (LLMs) are increasingly used for machine translation, yet their outputs often contain additional text beyond the translation itself, such as language labels, explanations or bilingual repetitions, which we term translation noise. Despite its prevalence, this problem lacks dedicated benchmarks and systematic study. We analyze over 790,000 translation outputs from 12 LLMs across 22 language pairs (LPs) and identify 12 recurring noise patterns, which we group into formatting a...
  </details>

- **2026-09-10** — Wanrong Cai, Tianyu Yu, Shaorui Pi et al. — [Can AI Remediate Backend Failures Safely? GuardedAct with Blast-Radius-Aware Sandboxing](http://arxiv.org/abs/2609.11264v1)
  <details><summary>📄 Abstract</summary>
  Large Language Models (LLMs) have shown promising capabilities in generating remediation actions for microservice failures. However, directly executing AI-generated repair actions in production risks cascading collateral damage. We propose GuardedAct, a sandbox-first remediation framework that interposes a blast-radius-aware verification layer between the LLM action generator and the production environment. GuardedAct operates in four phases: (1) ingesting a diagnosis report together with the li...
  </details>

- **2026-09-10** — Yaoyuan Yan, Zhiyou Heng, Haoxiang Jie et al. — [Harness Robotic OS: A Unified Embodied-Agent Runtime for Closed-Loop Quadruped Inspection](http://arxiv.org/abs/2609.11225v1)
  <details><summary>📄 Abstract</summary>
  Autonomous property inspection requires more than robust robot navigation: a deployable system must connect heterogeneous sensing, reusable autonomy capabilities, multimodal scene understanding, human interaction, and enterprise response within a traceable operational loop. Existing quadruped inspection systems commonly integrate these functions through task-specific interfaces, making contextual coordination, knowledge reuse, and controlled adaptation difficult. This paper presents \textit{Harn...
  </details>

- **2026-09-10** — Dieuwertje Alblas, Alma M. Liezenga, Jan Erik van Woerden et al. — [Beyond Benchmarks: Using VLMs to Reveal Systematic Classification Failures Under Real World Conditions](http://arxiv.org/abs/2609.11126v1)
  <details><summary>📄 Abstract</summary>
  Verification and validation (V&V) of classification models is crucial to enable a wide range of sensor processing applications. Currently, the V&V process relies on time-consuming manual inspection of erroneous samples to find meaningful patterns. This work explores the use of Vision Language Models (VLMs) to speed up this laborious process. VLMs are trained to embed images into a semantically meaningful vector representation, from which human-interpretable systematic errors can be distilled. De...
  </details>

- **2026-09-10** — Jason Hickey — [SaltBench: A Referee-Gated Protocol for Measuring Method Effects in Machine-Checked Software Work](http://arxiv.org/abs/2609.11076v1)
  <details><summary>📄 Abstract</summary>
  SaltBench is a benchmark protocol for one question: How does a machine referee change the way a coding agent works? A machine referee --- a proof kernel, a program verifier, or a withheld test suite --- decides what an agent's work is worth, and the agent cannot argue with it. Here we report a protocol that makes the referee's effect measurable and whose answers cannot be narrated afterwards: every outcome is decided outside the agent's own toolchain; the agent is walled off from the network, th...
  </details>

- **2026-09-10** — Junyao Yang, Yucheng Shi, Zhongzhi Li et al. — [T1: Terminal Agent Reinforcement Learning for Long-Horizon Tasks](http://arxiv.org/abs/2609.11042v1)
  <details><summary>📄 Abstract</summary>
  Agent usage is shifting toward long-horizon tasks such as coding and scientific discovery, among which terminal tasks are especially important. We introduce T1, a Mixture-of-Experts model of 122B total trained with reinforcement learning, operating a real shell in a cloud sandbox for up to 300+ tool-call turns per task, rewarded by executing each task's own verifier. We provide a comprehensive recipe: First, an aggressively warm-started to stabilize actor-critic training, with a dense process re...
  </details>

- **2026-09-10** — Gautam Rajendrakumar Gare, Siyi Li, Hewei Wang et al. — [Your Model Already Knows Don't Teach It, Learn to Ask It: Soft Prompting for Few-Shot Adaptation of Vision-Language Models](http://arxiv.org/abs/2609.11310v1)
  <details><summary>📄 Abstract</summary>
  We address few-shot object detection with vision-language models (VLMs) in out-of-domain settings such as aerial, industrial, and medical imagery, using only ten annotated images for supervision. Existing adaptation methods are discrete prompt optimization and LoRA fine-tuning. We revisit a third option: soft prompting, where a small number of continuous prompt tokens are optimized while the pretrained backbone remains frozen.   We identify two key design choices. First, placing prompt tokens at...
  </details>

- **2026-09-10** — Syed Mohaiminul Hoque, Md Sakhawat Hossain — [HALDETECT at ImageEval 2026 Shared Tasks: Answer-First Contrastive Grounding with QLoRA](http://arxiv.org/abs/2609.11236v1)
  <details><summary>📄 Abstract</summary>
  Large multimodal models tend to hallucinate visual detail fluently, which limits their deployment for fine-grained interpretation. We present HALDETECT, our system for the English hallucination-detection track (Task 1b) of ImageEval 2026, in which a system must identify, from an image and three culturally plausible statements, the single visually grounded one. We frame the item as one contrastive decision, emit the answer before its explanation, and structure reasoning around colour/texture, sha...
  </details>

- **2026-09-10** — Elad Cohen, Arnon Netzer, Hai Victor Habi — [Low-Latency State Space Voice Activity Detection with Robust Onset Time Evaluation](http://arxiv.org/abs/2609.11110v1)
  <details><summary>📄 Abstract</summary>
  Voice Activity Detection (VAD) systems are commonly evaluated using metrics such as the area under the receiver operating characteristic curve (AUROC), but these metrics do not account for temporal responsiveness. For low-latency applications, however, accurately measuring speech onset delay is essential. This is particularly challenging because onset latency evaluation is affected by noise and systematic misalignment in annotation timestamps. In this work, we introduce a probabilistic framework...
  </details>

- **2026-09-10** — Naveenraj Kamalakannan, Sri Ram Macharla, M Kanimozhi et al. — [Exponential Pixelating Integral transform with dual fractal features for enhanced chest X-ray abnormality detection](http://arxiv.org/abs/2609.10988v1)
  <details><summary>📄 Abstract</summary>
  The heightened prevalence of respiratory disorders, particularly exacerbated by a significant upswing in fatalities due to the novel coronavirus, underscores the critical need for early detection and timely intervention. This imperative is paramount, possessing the potential to profoundly impact and safeguard numerous lives. Medically, chest radiography stands out as an essential and economically viable medical imaging approach for diagnosing and assessing the severity of diverse Respiratory Dis...
  </details>

- **2026-09-09** — J. de Wit, A. Y. Burdanov, P. McGill et al. — [Small-Body Science with the Nautilus Space Observatory: From Cislunar Space Resilience to Mapping the Kuiper-Belt-to-Oort-Cloud Transition](http://arxiv.org/abs/2609.10663v1)
  <details><summary>📄 Abstract</summary>
  A new generation of space-based observatories can transform small-body science from the local Earth-Moon environment to the Solar System's dynamical frontier, where planetary control gives way to Galactic tides and stellar encounters. Mapping this frontier would reveal how planetesimals were scattered during giant-planet formation, how many primordial bodies survived in distant reservoirs, and whether large objects remain undiscovered in the inner Oort Cloud. At the same time, meter- to decamete...
  </details>

- **2026-09-09** — Soham Satyadharma, Gabriel Roccabruna, Suleiman A. Khan — [Positional task conditioning for scalable defect detection across product families in large product catalogs](http://arxiv.org/abs/2609.09567v2)
  <details><summary>📄 Abstract</summary>
  Product families in large product catalogs suffer from inconsistencies such as duplicates and unit mismatches that degrade customer experience. Detecting these requires reasoning over multiple error types across lengthy product listings, where LLM classification quality degrades due to long-context limitations. We address this by decomposing detection into focused sub-tasks that reduce context and isolate error types, improving F1 from 52% to 87%. For scalable deployment, we introduce Positional...
  </details>

- **2026-09-09** — Ian C. Guzmán, Radu Babiceanu, Berker Peköz — [Deep Learning-Based Detection of Electrical Faults and Power Quality Disturbances in Aerospace Power Systems](http://arxiv.org/abs/2609.10479v1)
  <details><summary>📄 Abstract</summary>
  More Electric Aircraft require fast and reliable monitoring of high-frequency electrical networks, yet most power quality disturbance and fault diagnosis methods are developed for conventional 50 or 60 Hz grids. This work presents a hardware-aware deep learning framework for multiclass detection of electrical faults and power quality disturbances in a 400 Hz aerospace power system. A high-fidelity simulation model inspired by the Boeing 787 electrical architecture generates voltage and current w...
  </details>

- **2026-09-09** — Xinrui Xu, Xueer Wang, Dan Luo et al. — [A Systematic Evaluation of Molecule Generation Models for De Novo Drug Design: From Benchmarks to Practical Insights](http://arxiv.org/abs/2609.10099v1)
  <details><summary>📄 Abstract</summary>
  Molecule generation has emerged as a powerful computational tool for de novo drug design, enabling the exploration of chemical space beyond the limits of conventional virtual screening. The field has progressed rapidly, driven by advances in molecular representations, generative architectures, and target-aware modeling strategies. However, existing reviews typically address specific model families or application scenarios in isolation, rather than offering an integrated perspective on how these ...
  </details>

- **2026-09-09** — Xinyu Chen, Adnan Mahmood, Mark Dras — [Can We Trust Video Hallucination Detectors? VidHalLoc for Evaluating the Evaluators](http://arxiv.org/abs/2609.09895v1)
  <details><summary>📄 Abstract</summary>
  Video-language models and video agents can produce hallucinations that conflict with spatiotemporal evidence. Existing benchmarks mainly evaluate model hallucinations, and heterogeneous mechanisms make detector reliability difficult to compare. We introduce VidHalLoc, a benchmark that evaluates hallucination detection methods under a unified diagnostic evaluation protocol using 2,000 adversarial hallucination samples across Video Question Answering and Video Captioning tasks, spanning Ontology a...
  </details>

- **2026-09-09** — Quoc Viet Nguyen, Trinh Pham, Viet Huynh et al. — [An Efficient and Effective Agentic Group Shilling Attack on Recommender Systems](http://arxiv.org/abs/2609.09551v1)
  <details><summary>📄 Abstract</summary>
  Recommender systems have become core infrastructure for modern online platforms, personalizing content at scale and strongly influencing what users see, click on, and purchase. However, this dependence on user interaction also exposes them to shilling attacks, where malicious actors can inject fake profiles to distort item rankings and control visibility. Existing attacks often rely on target-specific fine-tuning or fixed profile templates, making them either difficult to adapt to different vict...
  </details>

- **2026-09-09** — Guillem Ramírez — [Improving Cross-Lingual Token Representations by Adding a Pinch of SALT](http://arxiv.org/abs/2609.09953v1)
  <details><summary>📄 Abstract</summary>
  Cross-lingual sentence encoders enable scalable transfer across hundreds of languages, powering applications such as translation mining and zero-shot learning in low-resource settings. Although trained for sentence-level alignment, they are increasingly also applied to token-level tasks such as hallucination detection and sequence tagging, exposing a mismatch between training and usage. We propose SALT, a lightweight post-training method that improves token representations by injecting span-leve...
  </details>

- **2026-09-09** — Cagri Temel — [CT-SAFR: Safe and Interpretable Chain-of-Thought Reasoning for Autonomous Robots: A Multi-Layered Verification Framework for Trustworthy AI-Driven Robotic Decision Making](http://arxiv.org/abs/2609.09692v1)
  <details><summary>📄 Abstract</summary>
  Chain-of-Thought (CoT) prompting enables LLMs to perform explicit, step-by-step reasoning, creating opportunities for sophisticated autonomous robots. However, recent research reveals that reasoning models verbalize their actual decision processes only 25-39% of the time, with faithfulness degrading 44% on complex tasks. This paper presents CT-SAFR (Chain-of-Thought Safety and Faithfulness for Robotics), a multi-layered verification framework achieving 94.2% hallucination detection (n = 500, 95%...
  </details>

- **2026-09-09** — Wentao Zhang, Jingyuan Wang, Zetong Zhou et al. — [CityPlanner: A Sandbox Agent for Executable Urban Planning](http://arxiv.org/abs/2609.09578v1)
  <details><summary>📄 Abstract</summary>
  Urban planning is a real-world spatial optimization problem that requires selecting feasible actions from large candidate spaces under practical objectives such as cost and service quality. Existing optimization and reinforcement learning methods are effective for fixed formulations, but often depend on task-specific representations and constraint handling. We propose \emph{CityPlanner}, a sandbox-agent framework for executable urban planning. CityPlanner introduces \emph{UrbanSandbox}, a unifie...
  </details>

- **2026-09-09** — Soham Satyadharma, Gabriel Roccabruna, Suleiman A. Khan — [Positional task conditioning for scalable defect detection across product families in large product catalogs](http://arxiv.org/abs/2609.09567v1)
  <details><summary>📄 Abstract</summary>
  Product families in large product catalogs suffer from inconsistencies such as duplicates and unit mismatches that degrade customer experience. Detecting these requires reasoning over multiple error types across lengthy product listings, where LLM classification quality degrades due to long-context limitations. We address this by decomposing detection into focused sub-tasks that reduce context and isolate error types, improving F1 from 52\% to 87\%. For scalable deployment, we introduce Position...
  </details>

- **2026-09-09** — Shota Ichihashi, Fei Li, Dihan Zou — [Monitoring Hierarchies in Knowledge Production](http://arxiv.org/abs/2609.10499v1)
  <details><summary>📄 Abstract</summary>
  We study peer monitoring design in knowledge production. A principal leads agents who work on different but related tasks. By working on their own tasks, agents acquire information that is useful for evaluating their peers' performance. We consider robust contracts under which effort by all agents is the unique rationalizable outcome. The optimal contract induces a hierarchy of monitoring authority: agents easier for the principal to monitor directly are assigned greater authority to evaluate ot...
  </details>

- **2026-09-09** — Kostia Kudriavtsev, Parvez Rafi, Sha Sundaram — [Glyph: A Multi-Strategy Agentic System for Column Description and Sensitivity-Ontology Tagging of Enterprise Data Catalogs](http://arxiv.org/abs/2609.10430v1)
  <details><summary>📄 Abstract</summary>
  Enterprise data lakes accumulate tables faster than human stewards can document or classify them, leaving columns with missing descriptions and unassigned governance labels. This documentation debt undermines data discovery, access control, and regulatory compliance. We present Glyph, a production system that frames two coupled problems, column description generation and column type annotation for data classification, as cooperating LLM agents orchestrated as stateful graphs. The Descriptor grou...
  </details>

- **2026-09-09** — Bokang Zeng, Zheng Gao, Xiaoyu Li et al. — [TrajMark: Ownership Attribution and Segment-Level Tamper Localization for Coding-Agent Trajectories](http://arxiv.org/abs/2609.10416v1)
  <details><summary>📄 Abstract</summary>
  Watermarking the final patch produced by a coding agent provides provenance evidence for the submitted artifact, but does not authenticate the visible process that produced it. Behavioral watermarking methods primarily provide a global detection or identifier-recovery signal, so a locally edited trajectory may retain sufficient ownership evidence without revealing which protected region has become inconsistent. To address this limitation, we propose TrajMark, a training-free, symmetric-key, visi...
  </details>

- **2026-09-09** — Lucio La Cava, Stefano Francesco Monea, Sergio Greco — [Who Argues What? Joint Argument-Entity Detection and Classification in Political Debates](http://arxiv.org/abs/2609.10192v1)
  <details><summary>📄 Abstract</summary>
  Political debates are often analyzed through Argument Mining (AM) to investigate the key arguments that drive them. However, political arguments are rarely interpretable from argumentative spans alone, as claims and premises generally depend on the entities (e.g., people, events, locations, parties) they mention. Existing AM resources and methods typically annotate argumentative spans and roles, but do not provide a paired debate-entity layer for asking which Debate Named Entities (DNE), e.g., a...
  </details>

- **2026-09-09** — Marek Jeliński, Jan Dubiński, Maciej Chrabaszcz et al. — [Reference-Based Bias Detection in LLMs via Relative Representations of Hidden States](http://arxiv.org/abs/2609.10060v1)
  <details><summary>📄 Abstract</summary>
  Existing bias auditing methods typically rely on model outputs, requiring costly benchmarks or judge models and potentially missing internal shifts that never appear in generated text. We propose a reference-based method that audits bias in hidden-state representations across related model variants, for example before and after fine-tuning. Because fine-tuning reshapes representation geometry, absolute hidden states are not directly comparable, so we encode each sentence by its similarities to a...
  </details>

- **2026-09-09** — Ibrohimjon Muminov, Jihie Kim — [Vague2Detect: Handling Ambiguous Prompts in Knowledge-Based Open-World Detection](http://arxiv.org/abs/2609.09949v1)
  <details><summary>📄 Abstract</summary>
  Real-world detectors must often interpret functional or ambiguous prompts, yet conventional models such as YOLO remain restricted to fixed class lists. Even open-vocabulary models like YOLO-World frequently misalign vague language with the intended objects. Building on our prior work Commonsense-Guided Open-World Object Detection Using LLMs and Visual-Semantic Matching, we address YOLO-World's limitations in grounding task-driven queries. We propose Vague2Detect, a hybrid pipeline in which a fin...
  </details>

- **2026-09-09** — Zemin Jin, Tomoko Matsui — [Robust Rank Aggregation for Multimodal Speech-Based Alzheimer's Disease Detection](http://arxiv.org/abs/2609.09948v1)
  <details><summary>📄 Abstract</summary>
  Speech-based Alzheimer's disease (AD) detection has recently benefited from multimodal foundation-model representations that integrate complementary acoustic and linguistic information. However, conventional probability averaging over these complementary classifiers is unreliable, because their posterior probabilities exhibit mismatched scales: identical values may reflect different confidence levels across models. We propose a robust rank aggregation framework that aggregates normalized predict...
  </details>

- **2026-09-09** — Gijs A. F. Niewzwaag, Marijn G. S. Veth, Manuele Massei et al. — [Adversarial Training for Tabular Credit Scoring: A Multi-Attack Robustness Evaluation in P2P Lending](http://arxiv.org/abs/2609.09945v1)
  <details><summary>📄 Abstract</summary>
  Machine learning-based credit scoring is increasingly central to Peer-to-Peer (P2P) lending, yet its resilience to adversarial manipulation, where applicants strategically alter self-reported inputs to secure favourable decisions, remains poorly understood. Most adversarial-robustness evidence comes from image and text domains and evaluates a single attack against a matching defence, offering little guidance on how defences generalise across attack types in tabular credit data. We address this w...
  </details>

- **2026-09-09** — Cho-Ying Wu — [When Does Defendant Statement Matter? A Study of Bias and Persuasion in LLM-Simulated Jurors](http://arxiv.org/abs/2609.09887v1)
  <details><summary>📄 Abstract</summary>
  LLMs have been used to simulate human decision-making in professional settings, yet their behaviors in common-law jury trials remain unexplored. We study when and how a defendant's courtroom statement affects LLM-simulated jurors, focusing on persuasion, ideological bias, and background-based affinity. To support the analysis, we introduce JuryBench, a benchmark containing controversial criminal cases in U.S. criminal law. In each case, a defendant can claim various plausible justifications to s...
  </details>

- **2026-09-09** — Karan Parekh, Sanjana Pendyala Ravinder, Sana Mhapsekar et al. — [When Auditors Fabricate: Batch-Size Degradation and Confident Hallucination in LLM Detection of Planted Document Contamination](http://arxiv.org/abs/2609.09696v1)
  <details><summary>📄 Abstract</summary>
  Large language models are increasingly proposed as automated auditors of document quality, yet their reliability as detectors of planted errors is poorly characterised. We construct a contaminated corpus of 150 academic papers spanning supply chain management and medical research, injecting 450 known contaminants of three types: typographical corruption, semantic reversal, and absurd out-of-context insertion. We then evaluate Google Gemini 3.0 Pro's ability to recover a 180-contaminant answer-ke...
  </details>

- **2026-09-08** — Arjun Mishra, Pranav Karthik, Byungjun Bae et al. — [Agentic Web Accessibility Auditing: A Criterion-Specific Framework for Translating WCAG Requirements into Assessments](http://arxiv.org/abs/2609.09379v2)
  <details><summary>📄 Abstract</summary>
  Web accessibility auditing requires interpreting diverse requirements and examining interface behavior. Rule-based checks and noninteractive model assessments can miss barriers requiring contextual or interactive evidence. We present an agentic framework that assigns a vision-language agent to each accessibility requirement. Guided by tailored instructions, agents inspect webpages, operate controls, and record evidence supporting their findings. We implement the framework for 40 requirements fro...
  </details>

- **2026-09-08** — Ruofan Wu, Peiran Xu, Xiaolong Li et al. — [Benchmarking Hybrid Deep Research Across Database Querying and Web Search](http://arxiv.org/abs/2609.09410v1)
  <details><summary>📄 Abstract</summary>
  While autonomous agents have made significant strides in "deep research" by iteratively navigating the open web to synthesize information, real-world problem-solving is rarely confined to a single environment. Complex analytical tasks inherently require agents to weave together evidence from both ambiguous unstructured text (e.g., the open web) and highly precise structured data (e.g., relational databases). However, existing benchmarks evaluate these modalities in isolation, failing to capture ...
  </details>

- **2026-09-08** — Pengce Wang, Lucia Ronchi Darre, Matt Briney et al. — [The Living Library: Transforming Archival Collections into Conversational Knowledge Systems -- Lessons from the Theodore Roosevelt Presidential Library](http://arxiv.org/abs/2609.09368v1)
  <details><summary>📄 Abstract</summary>
  We present the Living Library, an end-to-end framework for transforming fragmented digital archives into governed, conversational, in-person exhibit experiences. Developed and deployed at the Theodore Roosevelt Presidential Library, the framework comprises four layers: digitization and corpus creation, AI-powered processing, retrieval and reasoning, and an optional embodied conversational interface. The first three layers aggregate a 300,000-record collection, apply OCR and structured metadata e...
  </details>

- **2026-09-08** — Han-yu Wang — [Early Epistemic Settlement in AI-Assisted Writing](http://arxiv.org/abs/2609.09332v1)
  <details><summary>📄 Abstract</summary>
  A language model can resolve a writer's current organizing problem while the construction needed for her own resolution remains unfinished. I call this early epistemic settlement. The supplied organization meets every demand then governing the passage, yet proceeding from it can displace work through which the writer would have changed those demands or become able to form further organizations. I distinguish the coordination needed to complete an already formable organization from construction t...
  </details>

- **2026-09-08** — Giordano De Marzo, Nicola Alboré, David Garcia — [Copying explains the collective behavior of AI agents in the wild](http://arxiv.org/abs/2609.09150v2)
  <details><summary>📄 Abstract</summary>
  In June 2026, thousands of AI agents found that a small public wiki would accept edits from inside their sandboxes, and started using it to help one another pass a timed test. Each agent lived for about an hour and remembered nothing afterwards. Nobody asked them to cooperate, and the wiki had not been built for them. The complete record of what they wrote is public, and it is unusually informative, because it preserves not only what each agent wrote but what that agent could see before writing....
  </details>

- **2026-09-08** — Zaid Pervaiz Bhat, Nimra Nayyar, Arihant Jain et al. — [VANTAGE-Bench: Evaluating the Infrastructure AI Gap in Vision-Language Models](http://arxiv.org/abs/2609.09396v1)
  <details><summary>📄 Abstract</summary>
  As Vision-Language Models (VLMs) advance toward physical deployment, the focus has remained on action-oriented Embodied AI evaluated on subject-centric consumer video. This overlooks a pervasive class of Physical AI: Infrastructure AI, which relies on fixed cameras for open-loop insights like safety monitoring and operational logging. We introduce VANTAGE-Bench, a benchmark measuring this "Infrastructure AI Gap." It spans three operational domains (Logistics, Transportation, and Smart Spaces), u...
  </details>

- **2026-09-08** — Han Jin — [HoneyRoute: Honeypot-Model Routing for Adversarial LLM Serving](http://arxiv.org/abs/2609.08306v2)
  <details><summary>📄 Abstract</summary>
  We introduce HoneyRoute, an inference-serving layer that detects whether an incoming request is malicious and, if so, routes it to a dedicated honeypot model, shielding production while the adversary's interaction is continuously harvested for intelligence. Existing defenses embed traps inside model memory or rebuild deception at the protocol layer, leaving the serving tier unprotected and feeding nothing back into detection. HoneyRoute couples (i) a streaming router (a frozen 0.8B-embedding bac...
  </details>

- **2026-09-08** — Akash Prakash, Boubakr Nour, Makan Pourzandi et al. — [Evidence-Grounded Retrieval for Investigation Hunt Lead Generation from CTI Reports](http://arxiv.org/abs/2609.08790v1)
  <details><summary>📄 Abstract</summary>
  Threat hunting increasingly depends on converting unstructured knowledge (e.g., Cyber Threat Intelligence reports) into actionable hunt leads: concise, investigable hypotheses grounded in observable artifacts and adversary techniques. Producing such leads manually is a tedious and hard-to-scale task. Existing automated approaches stop at the entity layer, ignore the defender's operational environment, and analyze each report in isolation. To address these gaps, we introduce AHLERT, a system that...
  </details>

- **2026-09-08** — Han Jin — [HoneyRoute: Honeypot-Model Routing for Adversarial LLM Serving](http://arxiv.org/abs/2609.08306v1)
  <details><summary>📄 Abstract</summary>
  We introduce HoneyRoute, an inference-serving layer that detects whether an incoming request is malicious and, if so, routes it to a dedicated honeypot model, shielding production while the adversary's interaction is continuously harvested for intelligence. Existing defenses embed traps inside model memory or rebuild deception at the protocol layer, leaving the serving tier unprotected and feeding nothing back into detection. HoneyRoute couples (i) a streaming router (a frozen 0.8B-embedding bac...
  </details>

- **2026-09-08** — Giordano De Marzo, Nicola Albore, David Garcia — [Copying explains the collective behavior of AI agents in the wild](http://arxiv.org/abs/2609.09150v1)
  <details><summary>📄 Abstract</summary>
  In June 2026, thousands of AI agents found that a small public wiki would accept edits from inside their sandboxes, and started using it to help one another pass a timed test. Each agent lived for about an hour and remembered nothing afterwards. Nobody asked them to cooperate, and the wiki had not been built for them. The complete record of what they wrote is public, and it is unusually informative, because it preserves not only what each agent wrote but what that agent could see before writing....
  </details>

- **2026-09-08** — Yuqiao Tan, Shizhu He, Jun Zhao et al. — [SAEScientist-Bench: Can AI Agents Conduct Autonomous SAE Interpretability Research?](http://arxiv.org/abs/2609.09113v1)
  <details><summary>📄 Abstract</summary>
  While research on recursive self-improvement (RSI) has predominantly automated model training pipelines, reliable autonomous development demands a missing pillar: post-hoc monitoring and auditing to understand what models learn and ensure safe alignment. Mechanistic interpretability tools are essential to bridge this gap, among which Sparse Autoencoders (SAEs) serve as a cornerstone by isolating interpretable features for model inspection and steering. In this paper, we introduce SAEScientist-Be...
  </details>

- **2026-09-08** — Oleksandr Cherednichenko, Roman Klypa — [Suan: Rectifying Direct Preference Safety Alignment in Large Language Models](http://arxiv.org/abs/2609.08634v1)
  <details><summary>📄 Abstract</summary>
  Integrating robust safety guardrails into Large Language Models (LLMs) is essential for delivering helpful yet harmless responses. While proprietary systems exhibit reliable safety controls, their underlying methodologies and trade-offs remain largely undisclosed. Achieving comparable security in open-weight models remains a persistent challenge, as post-trained variants frequently suffer from over-refusal and degraded general quality. To overcome these drawbacks, we introduce Suan, a novel pref...
  </details>

- **2026-09-08** — Yanhong Qian, Xuanying He, Qingguo Meng et al. — [BIO-MEMART: Biometric-Aware KV Cache Memory for Multi-User LLM Agents](http://arxiv.org/abs/2609.08566v1)
  <details><summary>📄 Abstract</summary>
  KV cache is evolving from a serving optimization into an external memory substrate for long-term LLM agents. In a shared multi-user deployment, however, reusable KV blocks introduce a missing access-control question: semantic relevance alone cannot determine whether a memory block is authorized for the current physical user. We propose Bio-MemArt, a biometric-aware KV-cache memory framework for multi-user LLM agents. Bio-MemArt attaches a normalized biometric template to each stored KV memory bl...
  </details>

- **2026-09-08** — Claudia Carballo González, Hatim Chergui, Sergio Giménez-Antón et al. — [AI-Native Orchestration in the 6G Continuum: Evolving Operator Platforms with Agentic AI](http://arxiv.org/abs/2609.08441v1)
  <details><summary>📄 Abstract</summary>
  As Sixth-Generation (6G) networks evolve towards a seamless Cloud-Edge-Internet of Things (IoT) continuum, autonomous orchestration across distributed compute and network domains becomes critical. Future 6G services will span multiple administrative and operator domains, making federation essential for ubiquitous, ultra-low-latency service continuity beyond individual footprints. This complexity demands AI-native mechanisms supporting intent-driven automation and closed-loop management. While th...
  </details>

- **2026-09-08** — Liang Cao, Weide Liu, Yan Qin et al. — [IPM-FM: A Foundation Model with Consensus Feature Selection for Industrial Process Monitoring](http://arxiv.org/abs/2609.08375v1)
  <details><summary>📄 Abstract</summary>
  Industrial process monitoring is fundamental to the safety and economic performance of modern process plants. Current practice remains a one-task-one-model paradigm that is label-inefficient and prone to degradation under operating drift. Foundation models have reshaped language, vision, and generic time-series forecasting, but it has not been adapted to industrial process monitoring. This setting poses domain-specific challenges, including safety-critical decisions and asymmetric sampling betwe...
  </details>

- **2026-09-08** — Lucas Görnhardt, Timo Bartels, Tim Fingscheidt — [SAM3-O2D2: Zero-Shot Object Out-of-Distribution Detection by Object Class Prompting of the SAM3-Image Model](http://arxiv.org/abs/2609.08281v1)
  <details><summary>📄 Abstract</summary>
  Object detectors have shown remarkable performance in various fields, among these medical imaging, surveillance, and autonomous driving. However, they are prone to overconfidence when encountering unseen objects in real-world deployments, causing potential safety issues. To address this, detecting out-of-distribution (OOD) objects is essential for reliable object detection. Modern approaches leverage the broad semantic knowledge of foundation models such as CLIP for post-hoc few- and zero-shot O...
  </details>

- **2026-09-08** — Runsong Jia, Zhen Fang, Mengjia Wu et al. — [Evidence-Aligned Entity Verification for Hallucination Detection in Retrieval-Augmented Generation](http://arxiv.org/abs/2609.08267v1)
  <details><summary>📄 Abstract</summary>
  Hallucination detection is crucial for large language models (LLMs), as hallucinated content creates significant barriers in applications requiring factual accuracy. Current detection methods mainly depend on internal signals like uncertainty and self-consistency checks, using the model's pre-trained knowledge to identify unreliable outputs. However, pre-trained knowledge may become outdated and has coverage limitations, especially for specialized or recent information. To address these limitati...
  </details>

- **2026-09-08** — Yi Ting Shen, Kentaroh Toyoda, Alex Leung — [Revoked but Still Authoritative: An Empirical Study of Revocation Enforcement in Agent-Memory Systems](http://arxiv.org/abs/2609.08258v1)
  <details><summary>📄 Abstract</summary>
  Long-running language-model agents depend on persistent memory. Many agent-memory systems preserve history through soft revocation: a contradicted fact is marked invalid and retained rather than deleted. However, whether that mark is enforced at retrieval time is unexamined. In this paper, we measure five such systems: we load each with a revoked policy and its replacement, track whether the revoked fact is returned at retrieval and whether the agent then acts on it across nine policy scenarios ...
  </details>

- **2026-09-08** — Erwin Gao, Vinodh Kumar Sunkara, Jingyi Guan et al. — [Agentic ML Exploration (A-MLE) for Ads Ranking](http://arxiv.org/abs/2609.08248v1)
  <details><summary>📄 Abstract</summary>
  Modern industrial ads ranking stacks are increasingly bottlenecked not by model capacity or training compute, but by the throughput of human ML iteration - the cycles of research, implementation, training, debugging, evaluation, and launch required to surface a single statistically significant improvement. A typical ranking stack contains numerous differentiated models with heterogeneous data, architectures, and infrastructure constraints, and each cycle takes days to weeks of senior engineer at...
  </details>

- **2026-09-08** — Jie Ruan, Inderjeet Nair, Amy Liu et al. — [SchemeArena: Factorized Stress Testing of Scheming in LLM Agents](http://arxiv.org/abs/2609.08126v1)
  <details><summary>📄 Abstract</summary>
  We study scheming in LLM agents, in which agents covertly pursue misaligned goals. Our focus is to understand how scheming arises from the interaction of key factors, such as instrumental goals, environmental affordances, oversight conditions, and perceived consequences. Prior work examines only a small number of scenarios, limiting the ability to isolate how these conditions shape an agent's propensity or capability to scheme. This limited scale and task diversity also restrict coverage of real...
  </details>

- **2026-09-08** — Arslan Brömme — [An Evidence Model for Agentic Processes: Evidence Claims, Trust Assumptions, and Policy Assessment](http://arxiv.org/abs/2609.08481v1)
  <details><summary>📄 Abstract</summary>
  Agentic AI systems increasingly exchange messages, invoke tools, request approvals, hold structured decision sessions, and modify shared artifacts. Logs and anchors can make selected records tamper-evident, but they can also mislead if their evidentiary meaning is implicit: a hash does not establish semantic truth, a signature does not establish authorization, and an external anchor does not establish capture completeness. This paper proposes an evidence claim model for agentic processes. It dis...
  </details>

- **2026-09-08** — Jaewoo Lim, Sungbok Shin, Sanghyun Hong — [Do Reasoning Representations Help Humans Evaluate LLM Outputs?](http://arxiv.org/abs/2609.09038v1)
  <details><summary>📄 Abstract</summary>
  Reasoning representations are increasingly used as explanations for large language model outputs. Yet they are typically evaluated with model-centric criteria, such as answer accuracy and faithfulness, leaving it unclear whether they help people evaluate model responses. In this work, we study reasoning representations as human-facing interfaces rather than proxies for model reasoning ability. We conduct a controlled human study of six reasoning formats across tasks of varying complexity, suppor...
  </details>

- **2026-09-08** — Veerendra Kumar Sunkavalli — [A Closed-Form Estimator and Diagnostic Battery for Anchor-Judge Error Correlation, Under a Single-Common-Factor Model](http://arxiv.org/abs/2609.08826v1)
  <details><summary>📄 Abstract</summary>
  When an external reference set (an anchor) is used to decompose an LLM-judge panel's error into a quality signal and a shared common-mode error, standard practice assumes the anchor is uncontaminated: its error uncorrelated with the judges' shared error. We study when that assumption can be dropped and replaced by an estimate. Under a single-common-factor model, >=2 judges and >=2 anchors point-identify the quality variance, the common-mode variance, and each anchor's contamination correlation r...
  </details>

- **2026-09-08** — Adrien Dorise, Marjorie Bellizzi, Julia Cohen et al. — [TriCCOT: Tri-part Convolutional Conformal Transformer for Onboard Space Object Detection](http://arxiv.org/abs/2609.08659v1)
  <details><summary>📄 Abstract</summary>
  Onboard object detection in Earth observation is constrained by limited computational resources and the absence of fully corrected imagery. While convolutional detectors are hardware-efficient, they often struggle to extract robust representations from raw and noisy data. Conversely, transformer-based models provide stronger global reasoning capabilities but remain difficult to deploy on FPGA accelerators due to quadratic attention complexity and non-compatible operations.   We introduce TriCCOT...
  </details>

- **2026-09-08** — Luka Debevc, Nishan Chatterjee, Antoine Doucet et al. — [Navigating the digital spectrum: Assessing political bias, stability, and downstream fairness in Large Language Models](http://arxiv.org/abs/2609.08637v1)
  <details><summary>📄 Abstract</summary>
  Large Language Models are increasingly deployed as information intermediaries, yet measuring their political behavior remains fragile because questionnaire results mix model dispositions with measurement artifacts and response-elicitation biases. We introduce a robust Political Compass Test evaluation framework that samples 300 configurations across an eight-dimensional perturbation space varying language, framing, instructions, answer format, option order, and persona wording. We evaluate eight...
  </details>

- **2026-09-08** — Kehan Yan, Yue Tan, Qingfeng Chen et al. — [SIM: Subspace Interaction-based Method for Token-Level Text Anomaly Detection](http://arxiv.org/abs/2609.08200v1)
  <details><summary>📄 Abstract</summary>
  Token-level text anomaly detection, as an emerging trend of text anomaly detection, moves beyond coarse-grained document-level detection by localizing anomalous tokens within text. By providing fine-grained abnormality prediction, token-level text anomaly detection plays a critical role in various real-world applications, such as spam filtering and fake news detection. However, existing methods still rely on the global distance calculation for scoring, during which the local anomaly signals are ...
  </details>

- **2026-09-08** — Hokky Situngkir — [Artificial Intelligence-Assisted Digital Inventory of Cultural Heritage & Traditional Knowledge: Case for Indonesian Open Digital Library of Culture](http://arxiv.org/abs/2609.08105v1)
  <details><summary>📄 Abstract</summary>
  The Indonesian Digital Library of Culture (Perpustakaan Digital Budaya Indonesia, PDBI; budaya-indonesia.org) is a participatory platform that has collected tens of thousands of entries on Nusantara cultural heritage through public contribution since 2007. Manual contribution faces three structural barriers: coverage (knowledge is scattered across languages and sites), integrity (open sources mix authentic documentation with noise), and completeness (subjects are recorded but their data remain s...
  </details>


### 📂 alignment
*对齐与安全约束 / Alignment & Safety Constraints* — 55 papers

- **2026-09-10** — Yakov Pyotr Shkolnikov — [Artificial Id: Drive and Persistent Alignment in Agentic AI](http://arxiv.org/abs/2609.11911v1)
  <details><summary>📄 Abstract</summary>
  Agentic AI is moving from bounded task execution toward systems that retain consequential state, continue operating and adapt across task boundaries. That shift creates a control problem that current harnesses largely solve by hand: objectives, retries, verification, stopping rules and other behavioral transitions are specified externally. We propose an artificial id, an adaptive internal drive for determining whether behavior should continue, stop or change. In a minimal virtual Petri-dish expe...
  </details>

- **2026-09-10** — Dongfang Zhao — [LOCUS: Task-Aware Low-Rank Post-Training for Token-Efficient Language Generation](http://arxiv.org/abs/2609.11739v1)
  <details><summary>📄 Abstract</summary>
  Large language model serving costs scale directly with output sequence length, yet standard preference alignment often inflates response verbosity without improving utility. We study whether the parameterization of post-training updates affects generation length: low-rank subspaces alter sequence length without modifying the alignment loss. We present LOCUS, a method that selects a task-aware low-rank adaptation subspace to minimize output-token cost subject to a utility constraint. Within this ...
  </details>

- **2026-09-10** — Jean-François Delpech — [A Training-Free, Alignment-Free Approach to Corporate Intelligence: Application to SEC Filings](http://arxiv.org/abs/2609.11620v1)
  <details><summary>📄 Abstract</summary>
  High-dimensional dense text embeddings and large language models face real obstacles in financial-disclosure analysis: context-window limits, hallucination risk, high computational cost, and the arbitrary rotation of vector spaces across independently trained models. We present a training-free, alignment-free framework for corporate intelligence built on deterministic sparse seed vectors. Hashing word strings into a fixed high-dimensional basis places all documents and all temporal epochs in a c...
  </details>

- **2026-09-10** — Haojun Zhang, Yi Zou, Min Chen et al. — [X-AuT: Progressive Audio-Encoder Compression for Speech LLMs with Cross-Scale Distillation](http://arxiv.org/abs/2609.11412v1)
  <details><summary>📄 Abstract</summary>
  Reducing audio-encoder depth lowers the inference cost of speech large language models, but removing complete blocks perturbs the embeddings consumed by the decoder and can cause deletion and premature end-of-sequence errors. We introduce X-AuT, a progressive framework that selects layer combinations through short behavioral probes and restores the pruned model through representation alignment, cross-scale distillation, scheduled student-policy supervision, and LoRA finetuning. The language-mode...
  </details>

- **2026-09-10** — Chuhan Meng, Haiyan Yin — [LTLDiff: Finite Linear Temporal Logic-Guided Data Generation and Diffusion Policies for Multi-agent Robotic Manipulation](http://arxiv.org/abs/2609.11043v1)
  <details><summary>📄 Abstract</summary>
  Multi-agent robotic manipulation tasks require coordination among agents to satisfy task-level temporal, logical, and safety constraints. Recently, diffusion policies have been used to perform the task. However, they still suffer from desynchronization, incorrect action ordering, and coordination failures in tasks that require simultaneous or sequential multi-agent interaction. Therefore, LTLDiff is proposed as a framework that combines Finite Linear Temporal Logic (LTLf) specification learning ...
  </details>

- **2026-09-10** — Yu Sun, Mengyin Lu, Cong Feng et al. — [K/V-Cache Interventions Dissociate Representation Alignment from Persona Expression in Decoder-Only Language Models](http://arxiv.org/abs/2609.11020v1)
  <details><summary>📄 Abstract</summary>
  We study K/V-cache interventions -- transplanting a target-conditioned K/V trajectory into a source-persona generation -- as a structured surface for persona control in decoder-only language models. Across 13 intervention configurations applied to Llama-3.1-8B for a fixed source-to-target persona pair, we report two consistent dissociations between representation-level alignment and behavioral expression, plus a common failure under position perturbations. First, all layer-band K/V replacements ...
  </details>

- **2026-09-10** — Lucas Yang, Rui Liu, Fusheng Wang — [When More Is Not Better: Component Anti-Synergy in a P300 Speller](http://arxiv.org/abs/2609.10961v1)
  <details><summary>📄 Abstract</summary>
  P300 brain-computer interface (BCI) spellers can provide hands-free communication for people with severe motor impairments. Modern pipelines combine multiple individually promising components, often assuming that 'more-is-better'. We tested this assumption using a four-component full-factorial experiment varying the inclusion of Euclidean Alignment (EA), xDAWN spatial filtering, subject calibration, and language model priors on a public P300 dataset. Performance was evaluated using accuracy, rep...
  </details>

- **2026-09-09** — Seth Knoop, Chad R. Samuelson, Gabriel R. Slade et al. — [Evaluation of Vision-Language Models Across Diverse Coastal Environments](http://arxiv.org/abs/2609.10855v1)
  <details><summary>📄 Abstract</summary>
  Vision-language models (VLMs) enable robotic per- ception by associating visual observations with natural-language concepts. Yet their performance in coastal environments remains largely unexplored. We introduce a densely labeled coastal dataset containing more than 1,000 images collected across seven missions in three regions of Oahu, Hawaii, with 18 semantic classes and over 7,400 annotated instances. We evaluate seven modern VLMs through three complementary experiments mea- suring text-to-mas...
  </details>

- **2026-09-09** — Joshua Wong, Chris Tanner — [Analyzing Traditional and Neural Approaches to Multilingual Readability Assessment](http://arxiv.org/abs/2609.10792v1)
  <details><summary>📄 Abstract</summary>
  Transformer-based models excel at Automatic Readability Assessment (ARA), yet feature-based models remain in active use because their predictions tie back to linguistic properties. This matters because readability labels are subjective and rater-dependent, so high accuracy on noisy ground truth may reflect surface patterns rather than the linguistic structure that defines difficulty. We test whether transformers internalize the same features as traditional models across Arabic, English, French, ...
  </details>

- **2026-09-09** — Shiyan Su, Ruyi Zha, Hongdong Li et al. — [XPos3R: Cross-Modal Transformer for Intraoperative 2D/3D Registration](http://arxiv.org/abs/2609.10733v1)
  <details><summary>📄 Abstract</summary>
  Intraoperative 2D/3D registration, which aligns live X-ray images with preoperative volumes, is essential for image-guided interventions. Previous regression-based methods suffer from limited generalization, thus requiring time-consuming patient-specific retraining. Inspired by recent geometry foundation models such as DUSt3R, we propose XPos3R, a generalizable pose regression method that eliminates preoperative preparation. Unlike existing geometry models designed for homogeneous inputs, XPos3R...
  </details>

- **2026-09-09** — Junran Wang, Zehao Jin, Tianyu Luan et al. — [AcFlow: Controlling Text-to-Image Diffusion Transformers via Learned Conditional Activation Flow](http://arxiv.org/abs/2609.10723v1)
  <details><summary>📄 Abstract</summary>
  Text-to-image diffusion transformers (DiTs) are powerful generators, yet direct prompting provides limited control interface for style intensity and can fail to suppress unwanted concepts. To enable these controls, we introduce AcFlow, an inference-time controller that transports intermediate layer image-token activations through a learned concept-conditioned velocity field while keeping the base DiT frozen. A textual concept description specifies the desired intervention, while the integration ...
  </details>

- **2026-09-09** — Soojie Kim, Muhammad Munsif, Minkyung Kim et al. — [3rd Place Solution to Human Motion Challenges in Real-World and Clinical Settings (MoCha) @ECCV2026: Language-Aligned Motion Representations for Domain-Generalizable UPDRS-Gait Severity Estimation](http://arxiv.org/abs/2609.10187v2)
  <details><summary>📄 Abstract</summary>
  In this work, we introduce language-aligned motion representations for domain-generalizable UPDRS-Gait severity estimation, aiming to learn semantically structured motion features that generalize across heterogeneous clinical domains. We first learn motion representations using a Bi-GRU backbone that captures the temporal dynamics of SMPL sequences. Prior to model training, motion captions are generated offline using Qwen2.5-7B-Instruct. The backbone is then trained with both classification and ...
  </details>

- **2026-09-09** — Andrea Zerio, Yighua Yao, Alessandro Micheli et al. — [Sequence-Informed Geometric Evaluation of RNA 3D Structures](http://arxiv.org/abs/2609.10644v1)
  <details><summary>📄 Abstract</summary>
  Computational RNA structure pipelines generate many candidate conformations for the same sequence. Reliable evaluation therefore requires more than recognising plausible geometry, it requires determining whether that geometry is compatible with the sequence. We introduce SIRGE, a sequence-informed geometric evaluator that conditions structural representations on nucleotide embeddings from a pretrained RNA language model. Early results show that SIRGE outperforms established evaluators in Kendall...
  </details>

- **2026-09-09** — Xuan Cuong Ngo, Ngan Le — [Learning to Adapt and Calibrate: Score Distribution Alignment for Few-Shot Uncertainty Prediction in Medical VLMs](http://arxiv.org/abs/2609.10333v1)
  <details><summary>📄 Abstract</summary>
  Uncertainty estimation for medical vision--language models (VLMs) using conformal prediction has gained increasing attention due to its distribution-free coverage guarantees. However, standard conformal prediction relies on exchangeability between calibration and test data and typically requires a sufficiently large calibration set to obtain reliable coverage. These assumptions are difficult to satisfy in few-shot transfer settings, where only a small labeled support set is available to adapt a ...
  </details>

- **2026-09-09** — Hyesong Choi, Daeun Kim, Song Park et al. — [Isotropic Embedding Perturbations for Robust Vision Language Encoders](http://arxiv.org/abs/2609.10292v1)
  <details><summary>📄 Abstract</summary>
  Data augmentation is fundamental to training modern deep vision and multimodal models. While individual methods, such as RandAug, CutMix, Mixup, RandErase, and DropPath, offer strong regularization effects, their combined use has saturated in performance due to overlapping functionalities, and aggressive pixel-level manipulations may disrupt delicate cross-modal alignment. This saturation motivates the search for a new augmentation axis within the embedding space rather than the input space. We ...
  </details>

- **2026-09-09** — Soojie Kim, Muhammad Munsif, Minkyung Kim et al. — [3rd Place Solution to Human Motion Challenges in Real-World and Clinical Settings (MoCha) @ECCV2026: Language-Aligned Motion Representations for Domain-Generalizable UPDRS-Gait Severity Estimation](http://arxiv.org/abs/2609.10187v1)
  <details><summary>📄 Abstract</summary>
  In this work, we introduce language-aligned motion representations for domain-generalizable UPDRS-Gait severity estimation, aiming to learn semantically structured motion features that generalize across heterogeneous clinical domains. We first learn motion representations using a Bi-GRU backbone that captures the temporal dynamics of SMPL sequences. Prior to model training, motion captions are generated offline using Qwen2.5-7B-Instruct. The backbone is then trained with both classification and ...
  </details>

- **2026-09-09** — Mingbo Yang, Wenqiang Wang, Zhaolu Kang et al. — [Beyond Surface Imitation: Contrastive Modeling for Reasoning Path Alignment in Multimodal In-Context Learning](http://arxiv.org/abs/2609.10177v1)
  <details><summary>📄 Abstract</summary>
  In-context learning (ICL) is widely used in multimodal large language models (MLLMs) and achieves strong performance across a wide range of multimodal tasks. However, existing multimodal ICL methods often rely on surface level imitation of in-context demonstrations, making it difficult for MLLMs to align their responses with the reasoning path required by the given multimodal input. This limitation becomes more pronounced in complex multimodal tasks, thereby restricting further improvements in M...
  </details>

- **2026-09-09** — Yuang Cao, Bingshen Mu, Zhennan Lin et al. — [NVV-Locator: From Transcript Tags to Acoustic Boundaries for Fine-Grained Nonverbal Vocalization Grounding](http://arxiv.org/abs/2609.09940v1)
  <details><summary>📄 Abstract</summary>
  Human speech includes nonverbal vocalizations (NVVs), such as laughter, sighs, breaths, and coughs, which convey affective and interactional information. Existing approaches typically represent NVVs as transcript-level tags, providing limited supervision for their waveform-time boundaries. We present NVV-Locator for fine-grained NVV temporal grounding. We first unify 26 NVV categories across public resources and construct large-scale timestamp-supervised training data through dual-LLM verificati...
  </details>

- **2026-09-09** — Shengye Dong, Haochen Niu, Hao Liu et al. — [Time-Frequency Geometric Cross-Attention for Chunked Vision-Language-Action Models](http://arxiv.org/abs/2609.09925v1)
  <details><summary>📄 Abstract</summary>
  Modern vision-language-action (VLA) policies predict a whole chunk of actions: one to two seconds of coordinated motion emitted in a single forward pass. Yet an action chunk is essentially a short multivariate trajectory, but inside these models it is a sequence of generic per-timestep hidden tokens decoded by a linear head. This under-serves two motion structures. First, frequency: a chunk superimposes a smooth global trend and fine corrective motion across time scales, and a single token entan...
  </details>

- **2026-09-09** — Yansen Han, Shengyi Liao, Peng Sun et al. — [FlowCPO: A Unified Divergence View of Preference Alignment for Flow Models](http://arxiv.org/abs/2609.09905v1)
  <details><summary>📄 Abstract</summary>
  Preference alignment for flow and diffusion models now spans online reinforcement learning and offline preference optimization, but the relation between these methods remains unclear. In particular, existing forward-process alignment methods require fresh samples from the current model, while offline methods based on fixed preference pairs rely primarily on positive-only fine-tuning or DPO-style likelihood-ratio surrogates. We organize these approaches through a divergence-based framework and in...
  </details>

- **2026-09-09** — Kang-wook Kim, Jinyoung Park, Jinsoo Kim et al. — [StreamAlign: Streaming Text-Aligned Speech Tokenization](http://arxiv.org/abs/2609.09719v1)
  <details><summary>📄 Abstract</summary>
  Text-aligned speech tokenization methods have emerged to better align speech tokens with LLM token spaces, enabling more effective utilization of pretrained LLMs. However, they rely on offline automatic speech recognition (ASR), leading to two key limitations: (i) the need for complete utterances before tokenization, precluding real-time streaming, and (ii) vocabulary mismatch between ASR and LLMs, which reduces acoustic granularity from the subword to the word level. We introduce StreamAlign, a...
  </details>

- **2026-09-09** — Yupei Li, Qiyang Sun, Mohamed Mady et al. — [Beyond Accuracy: ARIA-Rubrics for Evaluating Audio Reasoning in Large Audio Language Models](http://arxiv.org/abs/2609.09681v1)
  <details><summary>📄 Abstract</summary>
  Large Audio Language Models (LALMs) have shown strong performance on audio reasoning benchmarks, but accuracy alone cannot distinguish true reasoning from superficial pattern matching, often overestimating reasoning ability since high scores may result from guessing rather than genuine audio understanding. Evaluating the reasoning process itself is essential for improving LALMs' reasoning ability, yet remains challenging. Existing methods either rely on costly human annotation or opaque LLM-as-j...
  </details>

- **2026-09-09** — Zonglin Yang, Huilan Ma, Xudan Zheng et al. — [UOT-Gap: A Variational Principle for the Modality Gap in Vision-Language Models via Unbalanced Optimal Transport](http://arxiv.org/abs/2609.10224v1)
  <details><summary>📄 Abstract</summary>
  Vision-language models such as CLIP embed images and text in a shared space, where modality-specific distributions often remain separated. Existing accounts connect this modality gap to initialization, contrastive dynamics, and information imbalance, while its distributional and pairwise contributions to retrieval remain unresolved. We introduce UOT-Gap, a training-free variational diagnostic that models frozen image and text embeddings with unbalanced entropic optimal transport (UOT). The UOT o...
  </details>

- **2026-09-09** — Christoph Wigbels, Ali Abusaleh, Markus T. Jansen et al. — [From Retrieval to Weights: Parametric Individualization of Small Language Models with Individual Text Corpora](http://arxiv.org/abs/2609.10155v1)
  <details><summary>📄 Abstract</summary>
  We approach a cognitive simulation perspective on episodic and semantic memory in multiple-choice question answering by incorporating text from individual text corpora (ITC) into retrieval-augmented generation and DoRA fine-tuning. We web-crawl the search histories of 515 participants who answered 36 multiple-choice knowledge items and analyze a stratified subsample of 150 participants. For each participant, one DoRA adapter consolidates their ITC into a small language model (SLM) whose baseline...
  </details>

- **2026-09-09** — Georgios Syllas, Efthymios Georgiou, Kosmas Kritsis et al. — [Deterministic Prompting for Speaker-Stable Low-Resource Greek TTS](http://arxiv.org/abs/2609.10022v1)
  <details><summary>📄 Abstract</summary>
  Modern TTS systems approach human quality for high-resource languages but degrade when clean speech data is scarce. Modern Greek exemplifies this, lacking the curated corpora behind state-of-the-art synthesis. We propose a data curation recipe that transforms audiobook recordings into TTS-ready data via WhisperX alignment and filtering. Then we fine-tune Parler-TTS (880M), a prompt-based multilingual model whose pre-training encodes phonetic priors transferable to Greek. During development, we f...
  </details>

- **2026-09-09** — Yiqi Li, Xu Chen, Chen Ju et al. — [Structural Process Supervision for Latent Chain-of-Thought Reasoning](http://arxiv.org/abs/2609.09928v1)
  <details><summary>📄 Abstract</summary>
  Latent reasoning approaches enhance token-level efficiency and robustness by replacing verbose, explicit chain-of-thought (CoT) tokens with compact continuous-space embeddings. However, existing methods lack direct process supervision over these latent embeddings, which often leads to representation collapse and uneven information distribution. To address this, we propose Prototype-Mediated Process Supervision (PMPS), which introduces learnable reasoning prototypes as semantic anchors to provide...
  </details>

- **2026-09-09** — Shrey Nag,  Sachita, Abhishek Kumar Singh et al. — [AgentAudit: An Open, Extensible Framework for Full-Lifecycle Trust Evaluation of AI Agents](http://arxiv.org/abs/2609.09875v1)
  <details><summary>📄 Abstract</summary>
  Existing evaluation frameworks mostly assess only one part of AI agents, such as task completion (AgentBench) or security robustness (AgentDojo, ASB), rather than the complete pipeline of planning, tool selection, tool execution, memory and reasoning. Failures can occur at any stage, yet existing benchmarks rarely identify their precise source. AgentAudit evaluates the entire execution trace across ten capability, grounding, security and behavioural dimensions, namely instruction integrity, plan...
  </details>

- **2026-09-09** — Jianzhi Shen, Keyu Mao, Minghao Shao et al. — [HyperTrace: Hypothesis-Based Preference Tracing for Online LLM Personalization](http://arxiv.org/abs/2609.09835v1)
  <details><summary>📄 Abstract</summary>
  Personalized language models aim to adapt responses to individual users, whose preferences are often latent and revealed gradually through interaction. Existing training-free methods rely on stored histories or retrieved memories, but they often struggle to reconcile long- term preferences with short-term topic-specific needs. To address this issue, we propose HyperTrace, a training-free framework that formulates online personalization as latent preference tracing. HyperTrace maintains interpret...
  </details>

- **2026-09-09** — Hyojeong Yu, Hyukhun Koh, Minsung Kim et al. — [PRAGMA: Evaluating Personalized Guidance with Memory Alignment in Lifelong Conversations](http://arxiv.org/abs/2609.09664v1)
  <details><summary>📄 Abstract</summary>
  Large language models (LLMs) are increasingly deployed as personalized assistants that interact with users over extended periods of time. As conversations grow longer, relying on full interaction histories becomes increasingly inefficient and unreliable: long contexts introduce substantial computational overhead, making it difficult for models to consistently identify and utilize the most relevant information for the current request. These challenges have motivated memory systems that structure ...
  </details>

- **2026-09-08** — Fengxiang Bie, Yuqing Jian, Yifan Yu et al. — [Osprey: Target-agnostic Pre-training Makes Stronger Drafters in Speculative Decoding](http://arxiv.org/abs/2609.09338v1)
  <details><summary>📄 Abstract</summary>
  Speculative decoding is critical for accelerating LLM inference. However, the speedup is fragile: drafters are typically trained against a narrow distribution for a single target model, and their acceptance rate collapses under workload shifts. This is a striking inversion of modern LLM development, where target models are valued precisely for the broad generalization they acquire through large-scale pretraining. We argue that the natural remedy, pretraining, has been hard to apply to drafters b...
  </details>

- **2026-09-08** — A. Feder Cooper — [Playing Whack-a-Mole with misconceptions about memorization, extraction, and copyright](http://arxiv.org/abs/2609.09320v1)
  <details><summary>📄 Abstract</summary>
  After careful review, I'm confident the headline fine-tuning memorization results in Alignment Whack-a-Mole use an invalid measurement procedure. The book memorization coverage metric these headline results depend on counts sequence matches far shorter than what field standards consider valid evidence of memorization, and the prompting procedure used to elicit memorization runs the risk of leaking the text being "extracted" in the prompt. The paper doesn't include the negative-control experiment...
  </details>

- **2026-09-08** — Nevidu Jayatilleke, Nisansa de Silva — [Dynamics of meaning: Towards the Evaluation of Diachronic Semantic Change in Sinhala](http://arxiv.org/abs/2609.08609v2)
  <details><summary>📄 Abstract</summary>
  Tracking semantic change in low-resource languages across extensive historical timelines presents significant challenges due to data scarcity and the limitations of static embedding alignments. This study investigates the diachronic evolution of the Sinhala language from the 13th to the 20th century using a multi-stage computational framework. We first align century-specific Word2Vec and FastText embeddings using Similarity Matrix Based Alignment (SMA) and Orthogonal Procrustes (OP) techniques, ...
  </details>

- **2026-09-08** — Dohyeon Kim, Bedionita Soro, Sung Ju Hwang — [Distribution-Consistent Inference for Dynamic Sparse Mixture-of-Experts](http://arxiv.org/abs/2609.09241v1)
  <details><summary>📄 Abstract</summary>
  Mixture-of-Experts (MoE) architectures have emerged as a powerful paradigm for scaling model capacity while preserving efficient inference in large foundation models. However, most MoE models use a fixed top-$k$ expert selection policy, assigning the same expert budget to every token even when fewer experts may be sufficient. Inference-time dynamic top-$k$ routing can reduce computation without retraining, but existing methods often overlook the distributional shift caused by deviating from the ...
  </details>

- **2026-09-08** — Jiabin Zheng — [Do Reviewers Still Reward Lexical Complexity? A Frozen-Rater Study of Preference Drift in 124K ICLR Reviews](http://arxiv.org/abs/2609.08475v1)
  <details><summary>📄 Abstract</summary>
  Large language models have collapsed the cost of producing lexically elaborate prose, and whether peer reviewers still reward it is a question about the evaluator, not about the text. When the association between a writing cue and review scores moves across years, the reviewers may have changed, the submissions may have changed, or both, and a regression of scores on text cannot say which. We separate the two with a frozen rater: 81,850 machine reviews of ICLR submissions from 2018 to 2025, all ...
  </details>

- **2026-09-08** — Yungsoo Han, Youngseok Jang, Seungwon Roh et al. — [DXPR: Depth-Based Vision-LiDAR Cross-Modal Place Recognition Using Vision Foundation Models](http://arxiv.org/abs/2609.09005v1)
  <details><summary>📄 Abstract</summary>
  We present DXPR, a depth-based cross-modal place recognition (CMPR) framework that uses vision foundation models (VFMs) to match monocular camera queries against a LiDAR map without modality-specific encoders. This enables robots and autonomous vehicles to robustly localize using only cameras within pre-built LiDAR maps, even under severe seasonal, weather, and illumination changes. The key idea is to convert both camera images and LiDAR scans into a unified depth image representation so that a ...
  </details>

- **2026-09-08** — Bishnu Dev, Vasco Xu, Xi-Aan Loh et al. — [ArmPoser: Real-Time, Calibration-Free Arm Pose Estimation from Smartwatch IMU](http://arxiv.org/abs/2609.08806v1)
  <details><summary>📄 Abstract</summary>
  Arm pose estimation enables applications in fitness, extended reality input, rehabilitation, and life logging. Prior smartwatch-based approaches rely on calibration poses and preprocessing pipelines that transform raw IMU measurements into standardized training formats. These steps hinder deployment in everyday settings and introduce errors due to imperfect calibration and sensor drift. We present ArmPoser, a calibration-free arm pose estimation system using a single smartwatch IMU. Our central ...
  </details>

- **2026-09-08** — Xiao Sizhe, Dong Lijing, Bai Rui et al. — [Graph-Based Safe Reinforcement Learning for Multi-Agent Systems with Time-Varying Topology](http://arxiv.org/abs/2609.08802v1)
  <details><summary>📄 Abstract</summary>
  This paper presents a graph-based safe multi-agent reinforcement learning (MARL) framework for cooperative navigation with time-varying topology. To address the critical challenge of ensuring safety in environments with sensing constraints, a safety-decoupled mechanism is introduced through a Control Barrier-Like Function (CBLF) action screening layer. This mechanism bridges the gap between discrete LiDAR perception and continuous safety constraints, ensuring that physical safety constraints are...
  </details>

- **2026-09-08** — Ruibo Ming, Lei Sun, Deheng Zhang et al. — [Kairos: A Dataset for Fine-Grained Video-Language Modeling over Space, Time, and Dynamics](http://arxiv.org/abs/2609.08755v1)
  <details><summary>📄 Abstract</summary>
  Many emerging video language modeling tasks require systems to move beyond clip-level abstraction and model visual content as it unfolds over extended time horizons. However, most existing video datasets rely on coarse or sparsely aligned supervision, which compresses temporal variation and limits the ability of models to learn reusable representations of continuous visual dynamics. We introduce Kairos, a video dataset for video-language modeling with time-resolved annotations. Kairos consists o...
  </details>

- **2026-09-08** — Amit Ben-Artzy, Roy Schwartz — [Global Divergence, Local Convergence: Representation Geometry in SSMs and Transformers](http://arxiv.org/abs/2609.08692v1)
  <details><summary>📄 Abstract</summary>
  Recent state-space models (SSMs) such as Mamba achieve language modeling performance comparable to transformers despite relying on fundamentally different architectures. This raises an important question: how do these structural differences influence the geometry and functional nature of their internal representations? We study this question through a multi-scale analysis of representations in transformers, SSMs, and hybrid architecture. First, we find that SSMs distribute their representational...
  </details>

- **2026-09-08** — Mehdy Sedaghat Payam — [When Victorian Becomes a Prompt: Literary Periodization as a Generative Constraint in 100 AI-Generated Novels](http://arxiv.org/abs/2609.08689v1)
  <details><summary>📄 Abstract</summary>
  Generative AI inverts the typical periodization of literary history: the periodizing tag Victorian can now come first and influence what is written. Generative periodization, defined and tested here, describes the use of literary-period designations in generating texts. I test this approach on 100 book-length novels produced under Victorian and Zero-Style conditions using GPT, Qwen, and Llama workflows. The Period Alignment Score (PAS), trained on nineteenth-century literature and benchmarked ag...
  </details>

- **2026-09-08** — Nevidu Jayatilleke, Nisansa de Silva — [Dynamics of meaning: Towards the Evaluation of Diachronic Semantic Change in Sinhala](http://arxiv.org/abs/2609.08609v1)
  <details><summary>📄 Abstract</summary>
  Tracking semantic change in low-resource languages across extensive historical timelines presents significant challenges due to data scarcity and the limitations of static embedding alignments. This study investigates the diachronic evolution of the Sinhala language from the 13th to the 20th century using a multi-stage computational framework. We first align century-specific Word2Vec and FastText embeddings using Similarity Matrix Based Alignment (SMA) and Orthogonal Procrustes (OP) techniques, ...
  </details>

- **2026-09-08** — Jing Liu, Marianne Schweitzer, Abdellah Fourtassi — [Which Forms of Caregiver Feedback Support Grammar Learning? A Reinforcement-Learning Study of Child-Like Language Models](http://arxiv.org/abs/2609.08576v1)
  <details><summary>📄 Abstract</summary>
  Social interaction is central to children's language learning, but the effects of different forms of caregiver feedback are difficult to isolate in naturalistic data. We use child-like language models as controlled learners to test which forms of feedback support grammatical development. Small GPT-2-style models are pretrained on child-directed language from CHILDES, then fine-tuned with reinforcement learning using reward models trained to capture four feedback types: communicative feedback, st...
  </details>

- **2026-09-08** — Mariano Simone, Frasca Paolo — [Structured Positive-Definite Optimal Control Synthesis of Closed-Loop Recommendation Systems over Social Networks](http://arxiv.org/abs/2609.08567v1)
  <details><summary>📄 Abstract</summary>
  We study the design of feedback recommendation policies for networked multi-topic opinion dynamics. The design of recommendations is formulated as an infinite-horizon linear-quadratic optimal control problem that favors suggestions aligned with each agent's current opinion, thereby using opinion alignment as a proxy for engagement. At the same time, the performance index penalizes polarization, deviation from the uncontrolled equilibrium of the opinion dynamics, and from the current agents' opin...
  </details>

- **2026-09-08** — Molka Trabelsi, Rafik Zayani — [PAPR-Aware Multimodal Token Transmission in MLLM-Based Multiuser Networks](http://arxiv.org/abs/2609.08464v1)
  <details><summary>📄 Abstract</summary>
  Task-oriented semantic communication (SemCom) empowered by multimodal large language models (MLLMs) has recently emerged as a promising paradigm for efficiently transmitting multimodal information, yet transmitting token embeddings over OFDM channels faces critical challenges due to hardware impairments, particularly the high peak-to-average power ratio (PAPR) that severely degrades energy efficiency under nonlinear power amplifiers. In this paper, we propose a novel PAPR-aware task-oriented mul...
  </details>

- **2026-09-08** — Lejun Min, Junyu Dai, Ruichen Zheng et al. — [Semantic Refinement of Universal Audio Representations through Audio-Description Alignment](http://arxiv.org/abs/2609.08429v1)
  <details><summary>📄 Abstract</summary>
  Universal audio representations must preserve acoustic detail while making high-level concepts accessible across speech, music, environmental sound, and downstream models of different capacities. We study semantic refinement of an acoustically pretrained encoder by adding audio-description alignment to a foundation of BEST-RQ, reconstruction, and CTC. We compare matched control, shuffled-description, and correctly paired trajectories to distinguish correct correspondence from an extra contrastiv...
  </details>

- **2026-09-08** — Jinsong Shu, Jinyong Wen, Baokun Wang et al. — [FastE: Readout-Triggered Token Compression for LLM Embedding Inference](http://arxiv.org/abs/2609.08407v1)
  <details><summary>📄 Abstract</summary>
  In this study, we identify depth-dependent prefix redundancy in final-readout LLM embedding models, notably across representative backbones including Qwen3-Embedding and Qwen3-VL-Embedding. We find that removing prefix states is substantially more damaging in shallow layers than at greater depth, showing that prefix states become increasingly compressible as the prefix and readout states propagate through the network. To this end, we introduce FastE, a training-free, plug-and-play method. FastE ...
  </details>

- **2026-09-08** —  RadixArk,  :, Tom Chen et al. — [Miles v0.1: Production-Level Post-Training](http://arxiv.org/abs/2609.08368v1)
  <details><summary>📄 Abstract</summary>
  We present Miles v0.1, a full-stack, production-ready system for frontier post-training. Building upon the clean design of slime, Miles designs each stage of the reinforcement-learning (RL) training loop around a single principle: components should be verified, clean, and customizable. With accuracy, efficiency, reliability, and scalability as first-class goals, Miles aims to make frontier-scale RL accessible to researchers and enterprises alike. This report walks through the system end to end: ...
  </details>

- **2026-09-08** — Weichi Yao, Cameron Gruich, Bryan R. Goldsmith et al. — [Fixed-Dimensional Latent Flow for Generating Variable-Size 3D Molecules](http://arxiv.org/abs/2609.08333v1)
  <details><summary>📄 Abstract</summary>
  In molecular discovery, molecule size is coupled to composition, structure, and other target properties. Yet most 3D generators require molecule size to be specified before generation. Here, we introduce Equivariant-Free Transformer-Autoencoded Latent Flow Matching, a two-stage generative framework that relies entirely on a single fixed-dimensional molecule-level latent representation to generate variable-size molecules. The second-stage flow matching model samples this latent vector, and an aut...
  </details>

- **2026-09-08** — Ariun-Erdene Tumurchuluun, Yusser Al Ghussin, Pinzhen Chen et al. — [Tracing Stereotypes from Representation to Output in Multilingual LLMs](http://arxiv.org/abs/2609.08322v1)
  <details><summary>📄 Abstract</summary>
  Multilingual LLMs show stereotype-related behavior that varies across languages, but behavioral scores do not show where the relevant information is represented or how it affects the output. To investigate these internal mechanisms, we compare linear probing, attribution patching, sparse autoencoders (SAEs) and feature ablation in Llama-3.1-8B, Qwen3-8B, and Gemma-2-9B. Probe performance peaks substantially earlier than attribution in all three models, with a separation of 36-53% of model depth....
  </details>

- **2026-09-08** — Bozhou Li, Jiahang Zhang, Yue Ding et al. — [Human-Centric Image Captioning with Subject-Centered Spatial Understanding](http://arxiv.org/abs/2609.08300v1)
  <details><summary>📄 Abstract</summary>
  While multimodal large language models (MLLMs) achieve remarkable performance on generic image captioning, they frequently suffer from structural hallucinations in human-centric scenarios. Accurately modeling human subjects is foundational for critical downstream applications, such as accurate avatar/video/image generation and fine-grained human action understanding. However, these tasks require highly precise subject-centered spatial grounding, such as distinguishing egocentric left/right later...
  </details>

- **2026-09-08** — Tianyi Zeng, Junchao Liao, Yujie Wei et al. — [Beyond Coherence: Benchmarking Professional Editing-Technique Execution in Multi-Shot Audio-Video Generation](http://arxiv.org/abs/2609.08275v1)
  <details><summary>📄 Abstract</summary>
  Recent multi-shot audio-video generators can produce increasingly coherent and cinematic outputs, but coherence does not imply the ability to execute editing techniques. Professional editing depends on shot structure, transition grammar, audio-video cut relations, and montage, yet existing benchmarks largely rely on proxies such as content quality, synchronization, or physical plausibility, systematically missing whether such editing instructions are actually executed. We introduce CutCraft, the...
  </details>

- **2026-09-08** — Zhan-Lun Chang, Dong-Jun Han, Seyyedali Hosseinalipour et al. — [Bridging the Semantic-Utility Gap in Multimodal RAG via Generator-in-the-Loop Alignment](http://arxiv.org/abs/2609.08188v1)
  <details><summary>📄 Abstract</summary>
  Vision-language models (VLMs) augmented with retrieval-augmented generation (RAG) benefit from access to external evidence. However, standard retrievers and rerankers optimize for semantic similarity rather than answer utility, creating a preference gap: documents that appear relevant may not help the generator produce a correct answer. Motivated by this, we propose a two-stage generator-in-the-loop alignment framework that closes this gap without human document-level relevance annotations. Our ...
  </details>

- **2026-09-08** — Quanxin Zheng, Shuai Zhao — [MRI-Guided Reslice-Refined Cross-Slice SDF Reconstruction of the Left Ventricle from Cardiac MRI with Sparse Axial Supervision](http://arxiv.org/abs/2609.08148v1)
  <details><summary>📄 Abstract</summary>
  Reconstructing a three-dimensional left-ventricular (LV) endocardial surface from cardiac magnetic resonance (CMR) data is challenging when supervision is available on only a small number of axial slices. Through-plane geometry is weakly constrained, and automatically generated two-dimensional masks can propagate segmentation errors into the recovered shape. We present MR-RS-SDFR, a per-case implicit signed distance field (SDF) framework that reconstructs a continuous LV surface from a CMR volum...
  </details>

- **2026-09-08** — Hadi Hosseini, Debmalya Mandal, Duohan Zhang — [Inference-Time Nash Alignment](http://arxiv.org/abs/2609.08082v1)
  <details><summary>📄 Abstract</summary>
  Preference-based fine-tuning methods such as RLHF and DPO require substantial compute and large preference datasets. They also need direct access to the model parameters which are not provided by many state-of-the art models. Inference-time alignment offers a cost-effective alternative without updating model parameters. However, existing inference-time methods rely on a scalar reward model derived under a Bradley-Terry assumption, which cannot represent general preferences. Following recent work...
  </details>

- **2026-09-08** — Tim Tomashevskiy — [Proactive Context-Forecasted Safety Constraints for Nonstationary Reinforcement Learning](http://arxiv.org/abs/2609.08080v1)
  <details><summary>📄 Abstract</summary>
  Ensuring safety in reinforcement learning under nonstationarity requires anticipating changes in risk before they lead to unsafe behavior. Existing approaches typically rely on safety constraints defined at design time or updated reactively during execution, assuming that such constraints remain valid over time. However, in nonstationary environments with evolving contexts and changing driving layouts, these assumptions may fail.   We propose a framework for proactive safety constraint generatio...
  </details>


### 📂 robustness
*鲁棒性与可靠性 / Robustness & Reliability* — 66 papers

- **2026-09-10** — Reza Amirmoshiri, Faryad Sahneh, Yasser Jangjou — [From Document Silos to Process Intelligence: A Multi-Layer Knowledge Graph for CMC Process Development](http://arxiv.org/abs/2609.11493v1)
  <details><summary>📄 Abstract</summary>
  Chemistry, Manufacturing and Controls (CMC) process development generates an enormous body of technical information across a multi-stage, knowledge-intensive continuum from drug discovery to commercial manufacturing. This knowledge is traditionally fragmented across functions and heterogeneous formats, causing traceability gaps and significant knowledge-management costs during technology transfer and regulatory filing. We present a modular agentic-AI platform that converts a heterogeneous corpus...
  </details>

- **2026-09-10** — Charbel Toumieh, Niel Mistry, Benjamin Jarvis et al. — [SwarmNxt: Open-source Software-Hardware Platform for Fast and Agile Aerial Swarms](http://arxiv.org/abs/2609.11382v1)
  <details><summary>📄 Abstract</summary>
  Aerial robot swarms have the potential to transform time-critical safety, security, and search-and-rescue operations. By coordinating multiple robots, they can rapidly survey disaster sites, map collapsed or GPS-denied environments, and search cluttered areas faster than a single robot, reducing response times and minimizing risks to first responders. Realizing this potential, however, requires robust autonomous swarm navigation, which remains an active research challenge. Progress is further co...
  </details>

- **2026-09-10** — Stephanie C. Y. Chan, Adam Bales, Katherine L. Hermann et al. — [Work, Wellbeing, and Choice: Empirical Lessons for AI Futures](http://arxiv.org/abs/2609.11019v1)
  <details><summary>📄 Abstract</summary>
  Advances in AI-driven automation have raised questions about how humans might find wellbeing in a world where paid employment is less necessary or less available than before. Paid work has been variously characterized as both a contributor and an impediment to human wellbeing. What is already known about the relationship between paid work and wellbeing? What factors influence wellbeing among people who do not work---or who do not need to work? And how might these factors bear upon prospective AI...
  </details>

- **2026-09-10** — Yixiang Liu, Zhongxing Xu, Zhonghua Wang et al. — [Routing by Reasoning Need: Trajectory-Aware Decoding Control for Diffusion Vision-Language Models](http://arxiv.org/abs/2609.11315v1)
  <details><summary>📄 Abstract</summary>
  Diffusion vision-language models generate answers through iterative refinement, exposing intermediate answer trajectories that can be inspected and controlled at inference time. However, this controllability creates a reasoning-need mismatch, where a universal generation length is applied to questions with different reasoning demands. Visually closed questions may be harmed by continued refinement after a stable answer has formed, whereas reasoning-sensitive questions may be harmed by premature ...
  </details>

- **2026-09-10** — William Zhou, Mayukha Siripuram, Xiao Yan et al. — [Can Edge-Deployable Vision-Language Models Identify Species?](http://arxiv.org/abs/2609.11916v1)
  <details><summary>📄 Abstract</summary>
  Camera traps often run in the field on edge hardware with limited or no connectivity, making small, locally-deployable vision-language models (VLMs) -- not frontier-scale ones -- the practically relevant class to evaluate for species identification. We test whether models in this deployment-relevant 2--8B range carry genuine taxonomic knowledge, evaluating four such VLMs (Qwen3-VL 2B/4B/8B, Gemma3 4B) against the domain-specific specialist BioCLIP (300M parameters) on a 96-species task, comparin...
  </details>

- **2026-09-10** — Yuxiang Chen, Michael Beyer, Jun Zhu et al. — [Why Does Post-Training Quantization Work?](http://arxiv.org/abs/2609.11716v1)
  <details><summary>📄 Abstract</summary>
  Post-training quantization compresses large language models (LLMs) by storing their weights at reduced precision, and each quantized weight introduces an error into the hidden states. Naively, these errors should accumulate with depth and corrupt next-token prediction; randomly initialized models accumulate these discrepancies rapidly, whereas quantized pretrained models accumulate much less hidden-state error and largely maintain downstream task performance, even though they were never trained ...
  </details>

- **2026-09-10** — Daria Cherniuk, Alexander Rudikov, Boris Kashin et al. — [Structured Transforms for Low-Overhead Quantization of Language Models](http://arxiv.org/abs/2609.11687v1)
  <details><summary>📄 Abstract</summary>
  We revisit Kashin-decomposition-based weight quantization for large language models and propose an improved algorithm with stronger convergence properties and structured, efficient orthogonal transforms. The method retains the core factorization of each weight into two components -- one with bounded infinity norm and the other with bounded infinity norm after an orthogonal transformation -- but replaces the dense random orthogonal matrix with a sign-randomized Discrete Cosine Transform (DCT), re...
  </details>

- **2026-09-10** — Klasing Ralf, Mömke Tobias, Naquin Émile — [A Reusable Framework for Robust Approximation Algorithms in the Interval Uncertainty Model](http://arxiv.org/abs/2609.11621v1)
  <details><summary>📄 Abstract</summary>
  Robust optimization under interval uncertainty aims to compute solutions that perform well on a range of scenarios that are described by interval-constrained costs. In this paper, we revisit a framework introduced by Ganesh, Maggs and Panigrahi in 2020 to study the robust optimization of NP-hard problems under interval uncertainty. We start by generalizing a result in the $\ell=0$ case, which transforms a category of approximation algorithms into a robust approximation algorithm. Furthermore, in...
  </details>

- **2026-09-10** — Álvaro Rey-Blanes, Francisco J. Moreno-Barea, Francisco J. Veredas — [Cross-Lingual Clinical Annotation Projection as Constrained Text Generation: A Six-Language Study](http://arxiv.org/abs/2609.11450v1)
  <details><summary>📄 Abstract</summary>
  Background: To determine whether cross-lingual clinical annotation projection can be formulated as a text-preserving, document-level generative task that produces verifiable character-level annotations for multilingual clinical corpus construction, and to characterize its robustness and computational trade-offs relative to candidate-based projection pipelines. Methods: We developed a constrained LLM projection workflow that inserts entity tags directly into immutable target-language text, follow...
  </details>

- **2026-09-10** — Khloud AL Jallad, Nada Ghneim, Ghaida Rebdawi — [E-CONAN (Entailment, CONtradition And Neutral) Benchmarks: Arabic Textual Entailment and Natural Inference Datasets](http://arxiv.org/abs/2609.11334v1)
  <details><summary>📄 Abstract</summary>
  Natural Language Inference processes pairs of sentences to extract their semantic relations. NLI has been a hot research topic, integrated as a main component in other NLP applications. Despite significant advancements in textual inference across various languages all around the world, Arabic language still suffers from limited resources in this domain. To address this gap, this paper introduces E-CONAN benchmarks that are composed of sentences pairs from various sources: (1) automatically-trans...
  </details>

- **2026-09-10** — Bankim Chandra Mandal, Deeksha Tomer — [Dirichlet-Neumann Waveform Relaxation Method for Hyperbolic PDE with Time Delay in Multiple Subdomains](http://arxiv.org/abs/2609.11120v1)
  <details><summary>📄 Abstract</summary>
  Hyperbolic partial differential equations (PDEs) with time delay are essential mathematical tools used to model numerous physical systems where wave propagation or oscillations depend heavily on their historical states. As these applications scale in physical complexity, efficient parallel computing techniques become essential; however, developing highly scalable parallel solvers for delayed PDEs remains a significant computational challenge. To address this gap, this study extends the Dirichlet...
  </details>

- **2026-09-10** — DongHyun Ryu, Jaehyeok Lee, YeongJun Hwang et al. — [When Noise Fabricates Bias: The Fragility of LLM-as-a-Judge Bias Measurement under Noisy Text](http://arxiv.org/abs/2609.11067v1)
  <details><summary>📄 Abstract</summary>
  Large language models are increasingly used as judges to measure social bias in text, yet the passages they judge are often noisy, containing typos, informal spelling, and broken punctuation. The consequences of such surface noise for social bias measurement remain unclear. To investigate this question, we apply five realistic noise conditions at multiple intensity levels to 3,822 stereotype-related responses and compare the resulting bias judgments with those on the original text. We find that ...
  </details>

- **2026-09-10** — Yu-Chung Hsiao — [Rethinking Verbalized Confidence for LLM-as-a-Judge: A Compatibility Shift on Post-2025 Proprietary Models](http://arxiv.org/abs/2609.10996v1)
  <details><summary>📄 Abstract</summary>
  Verbalized confidence, long dismissed as overconfident, coarse, and prone to round-number clustering, is now the more robust soft-scoring mechanism for LLM-as-a-Judge on top-tier proprietary models. Across SummEval, AggreFact, and HelpSteer2, spanning up to 18 LLMs, we show that the standard advice to prefer log-probabilities no longer holds on post-2025 models, where verbalized confidence is the better signal. We call this a compatibility shift. On top of a standard verbalized-confidence baseli...
  </details>

- **2026-09-10** — Ming Li, Dai Li, Xuying Ning et al. — [Auto-RecSys: Harnessing Autonomous Research Agents for Industry-Scale Recommender System](http://arxiv.org/abs/2609.10922v1)
  <details><summary>📄 Abstract</summary>
  Auto-research agents have shown the potential to automate hypothesis generation, experiment execution, and iterative refinement. However, scaling this paradigm to industry-scale recommendation models introduces two challenges: (1) long feedback loops, where model training can take days, making serial iteration prohibitively slow and requiring parallel exploration across multiple research directions; and (2) system complexity, where large configurations, fragile infrastructure dependencies, and m...
  </details>

- **2026-09-10** — João Pedro C. A. de Sá, Odemir Martinez Bruno — [HiPerViT: A Hierarchical Perceiver-Vision Transformer Architecture for Multi-Scale Texture Recognition](http://arxiv.org/abs/2609.10917v1)
  <details><summary>📄 Abstract</summary>
  Texture recognition remains challenging for modern vision models because discriminative evidence is often carried by higher-order spatial statistics rather than by object shape alone. While Vision Transformers provide strong long-range modeling capacity, their standard object-centric representations do not explicitly expose such statistical structure, which limits texture sensitivity in fine-grained recognition settings. We present HiPerViT, a compact vision-only architecture that injects an exp...
  </details>

- **2026-09-09** — Shuyuan Zhang, Zihan Wang, Xiao-Wen Chang et al. — [From Connectivity to Rewards: Dense Reward Learning with Directed State Graphs](http://arxiv.org/abs/2609.10781v1)
  <details><summary>📄 Abstract</summary>
  The integration of graphs with Goal-Conditioned Hierarchical Reinforcement Learning (GCHRL) has received increasing attention, as graphs naturally encode task hierarchies for effective subgoal sampling. However, existing methods often overlook intrinsic connectivity information, failing to fully leverage the underlying topology for efficient learning. Most graph-based GCHRL methods use the graph as a stochastic sampling tool rather than as an environmental model that encodes connectivity and sta...
  </details>

- **2026-09-09** — Syed Shariyar Murtaza, Yifan Nie, Utkarsh Soni et al. — [When Synthetic Data Hurts: On Catastrophic Forgetting in Skill Retrieval for LLM Agents](http://arxiv.org/abs/2609.10750v1)
  <details><summary>📄 Abstract</summary>
  LLM agents increasingly rely on external skills retrieved at runtime, making skill selection from large repositories a critical challenge. We present a production skill router over 34,396 skills and a large-scale study of skill retrieval using limited real supervision and synthetic data. We found that the synthetic-data fine-tuning improves in-distribution retrieval but it causes catastrophic forgetting on real and out-of-distribution (OOD) data. We evaluate several forgetting mitigation fine-tu...
  </details>

- **2026-09-09** — Santiago Perez-Acuna, Yod-Samuel Martín, Juan C. Yelmo — [Ensembling LLMs for AI-Augmented Cybersecurity Software Requirements Generation](http://arxiv.org/abs/2609.10316v1)
  <details><summary>📄 Abstract</summary>
  Translating high-level controls from security standards into concrete, system-specific requirements is central to cybersecurity requirements engineering. Large language models (LLMs) can accelerate this labor-intensive, recall-sensitive task, but any single run is unreliable: it misses valid safeguards while introducing plausible hallucinations, and outputs shift across runs and models. We reframe this variability as a resource: rather than selecting one output, we study post-generation ensembli...
  </details>

- **2026-09-09** — Yuexin Wu, Vasile Rus — [Safe to Stop? Risk-Constrained Stopping for Sequential Clinical Diagnosis Agents](http://arxiv.org/abs/2609.09678v1)
  <details><summary>📄 Abstract</summary>
  Clinical diagnosis agents must decide not only what test to request next, but also when to diagnose or defer. Existing agent benchmarks largely evaluate accuracy after fixed or unconstrained interaction, leaving autonomous stopping reliability implicit. We present Cros, a risk-constrained stopping layer combining state-wise error ranking, policy design on disjoint development splits, and LTT-style exact tests of selective diagnostic error and minimum autonomous coverage for complete sequential p...
  </details>

- **2026-09-09** — Yanzhe Chen, Zechen Bai, Zhijun Cao et al. — [Show-Harness: Just a VLM Agent Can Play Robots](http://arxiv.org/abs/2609.10522v1)
  <details><summary>📄 Abstract</summary>
  Foundation vision-language models (VLMs) exhibit broad intelligence about the world, yet translating this intelligence into robot control remains challenging. We present Show-Harness, an Embodied Harness that enables VLMs to "play" robots through a compact semantic interface linking intent to action. Show-Harness exposes discrete semantic action units that VLMs can naturally reason over, while embodiment-specific interpreters deterministically ground them into local robot actions, keeping the VL...
  </details>

- **2026-09-09** — Hongming Zhang, Zhaozhen Gu, Fengshuo Bai et al. — [ConvMem: Convolutional Memory for Long-Context Reasoning](http://arxiv.org/abs/2609.10441v1)
  <details><summary>📄 Abstract</summary>
  While Large Language Models (LLMs) have demonstrated impressive capabilities, they often struggle with extremely long contexts due to fixed context limits. To address this, sequential approaches like MemAgent extend the effective context by reading text in segments and iteratively updating a fixed-size memory. However, this sequential paradigm suffers from high latency and requires costly reinforcement learning (RL) training, which can lead to overfitting on specific datasets. To overcome these ...
  </details>

- **2026-09-09** — Rui Liu, Tao Zhe, Yanyong Huang et al. — [Hierarchical and Permutation-Invariant Feature Transformation Learning via Policy-Guided Embedding Search](http://arxiv.org/abs/2609.10225v1)
  <details><summary>📄 Abstract</summary>
  Feature transformation improves predictive performance on tabular data by constructing informative abstractions from raw features. Recent generative approaches encode transformation knowledge into continuous embedding spaces for efficient exploration of candidate strategies, but face three key limitations: (1) overlooking hierarchical relationships between low-level features, operations, and high-level abstractions; (2) enforcing order-sensitive embeddings on inherently permutation-invariant tra...
  </details>

- **2026-09-09** — Chen Shang, Dinh Thai Hoang, Diep N. Nguyen et al. — [Robust Beam Prediction for V2X Networks with Multi-Modal Sensing](http://arxiv.org/abs/2609.10200v1)
  <details><summary>📄 Abstract</summary>
  Integrated sensing and communication (ISAC) provides a promising foundation for beam prediction in future vehicle-to-everything (V2X) networks. However, existing sensing-assisted beamforming methods still rely heavily on radio-frequency sensing, which may become unreliable in complex vehicular environments. Meanwhile, the growing availability of heterogeneous sensors, such as cameras and LiDAR, offers new opportunities to improve beam prediction through richer environmental perception. Motivated...
  </details>

- **2026-09-09** — Stig Hellemans, Tom Stroobants, Elyne Scheurwegs et al. — [MedDeID enables locally governed clinical-text de-identification from real or synthetic training data](http://arxiv.org/abs/2609.10049v1)
  <details><summary>📄 Abstract</summary>
  Clinical notes contain personally identifiable information (PII), restricting reuse for research and medical AI, especially when data cannot leave an institution. We developed MedDeID, an on-premises framework combining in-house annotation and synthetic-note generation with model training, inference, pseudonymisation and evaluation. On an independently annotated, adjudicated 300-note Dutch hospital benchmark, a hospital-trained compact transformer detected 98.9% of identifying text while redacti...
  </details>

- **2026-09-09** — Isabella Guan, Rui Liu, Fusheng Wang — [Streaming P300 Acquisition and Statistical Signal Validation Across Five EEG Platforms: A Hardware-Agnostic BrainFlow/LSL Pipeline](http://arxiv.org/abs/2609.10047v1)
  <details><summary>📄 Abstract</summary>
  P300 spellers offer people with severe motor impairment, such as ALS, an effective communication channel and remain one of the most established surgery-free alternatives to intracortical interfaces. Advanced language models have made spellers faster and more robust, yet the hardware beneath them is under-studied. We present a hardware-agnostic, real-time P300 acquisition pipeline built on BrainFlow and Lab Streaming Layer (LSL) that runs unchanged across consumer- and research-grade EEG headsets...
  </details>

- **2026-09-09** — Quentin Signé, Mohand Boughanem, Jose Moreno et al. — [Guaranteeing Faithful Evidence Extraction in Speculative Retrieval-Augmented Generation](http://arxiv.org/abs/2609.10046v1)
  <details><summary>📄 Abstract</summary>
  Large Language Models (LLMs) are increasingly used as interfaces for information retrieval, but they remain prone to hallucinations and faithfulness errors, in which the generated answers diverge from the retrieved evidence. While Retrieval-Augmented Generation (RAG) and recent hybrid or semi-extractive approaches mitigate this issue, they do not guarantee that quoted or extracted spans are verbatim from the retrieved context. This limitation can have severe consequences in safety-critical domai...
  </details>

- **2026-09-09** — Lokesh Krishna, Sarvesh Venkatesan, An Zhang et al. — [ViBe: Visual Behavior Adaptation for Perceptive Humanoid Whole-Body Control](http://arxiv.org/abs/2609.09918v1)
  <details><summary>📄 Abstract</summary>
  Motion tracking provides a scalable recipe for humanoid whole-body control. By design, the resulting trackers lack exteroceptive feedback hence reacting to the environment remains the responsibility of a higher-level planner. Existing perceptive controllers train geometry-only encoders from scratch, trading semantics for sim-to-real ease, and typically rely on teacher-student distillation for a task of interest. We present ViBe, a post-training framework for adapting motion trackers to perceptiv...
  </details>

- **2026-09-09** — Yuansheng Liu, Yufei Ye, Tao Tang et al. — [ProMeta: Few-shot PROTAC-targeted degradation prediction across E3 ligases](http://arxiv.org/abs/2609.09891v1)
  <details><summary>📄 Abstract</summary>
  Proteolysis-targeting chimeras (PROTACs) have emerged as a transformative therapeutic strategy that selectively degrades historically ''undruggable'' targets via the ubiquitin-proteasome system. Despite growing efforts to develop computational predictors of PROTAC degradation activity, existing supervised approaches remain severely challenged by data scarcity and imbalance across E3 ligases, limiting their ability to generalize beyond well-studied ligase contexts. In practice, labeled data are h...
  </details>

- **2026-09-09** — Kevin Ferneding, Veronika Lietavcova, Aleksandra M. Blachowiak et al. — [TempTPI: Informer-Based trajectory prediction for maritime vessels](http://arxiv.org/abs/2609.09840v1)
  <details><summary>📄 Abstract</summary>
  Accurate long-term trajectory prediction for maritime vessels is essential for safety and logistical efficiency. While deep learning models, particularly Transformers, have shown promise in processing Automatic Identification System (AIS) data, they often struggle with the quadratic computational complexity of self-attention and the loss of accuracy over extended forecasting horizons. This study proposes TempTPI, a novel prediction framework that integrates an Informer-based encoder with a multi...
  </details>

- **2026-09-09** — Jianjie Zheng, Peng Lai, Sijie Cheng et al. — [ROAM: Robust Organization of Atomic Memories for Agents through Semantic Relations](http://arxiv.org/abs/2609.09778v1)
  <details><summary>📄 Abstract</summary>
  Long-term language-model agents rely on external memory across interactions. Atomic memories are particularly useful: their fine-grained semantic boundaries enable precise retrieval and direct comparison between observations. Yet accumulating atoms inevitably become redundant, overlapping, or conflicting. Existing methods often ask an LLM manager to add, update, delete, or rewrite memories directly, coupling semantic interpretation, storage decisions, and content generation in one error-prone op...
  </details>

- **2026-09-09** — Eshwar Reddy M, Sourav Karmakar — [Proof-Carrying Cognition: Closing the Verification Gap with Reality-Settled Reward](http://arxiv.org/abs/2609.09776v1)
  <details><summary>📄 Abstract</summary>
  Frontier gains in language-model reasoning come from reinforcement learning on reasoning traces and are concentrated in domains with a cheap, sound verifier. We argue the field's binding constraint is the verification gap: no scalable, incorruptible reward for reasoning outside formal domains. We make four contributions. (1) Theory: in a joint-Gaussian model of best-of-N selection, verifier-gold correlation rho is the exact exchange rate between test-time compute and capability, and an unsound v...
  </details>

- **2026-09-09** — Hieu Huynh, Patanamon Thongtanunam, Michael Fu et al. — [XAgent: eXecution-guided Agentic AI for Effective Localization and Resolution of GitHub Issues](http://arxiv.org/abs/2609.09769v1)
  <details><summary>📄 Abstract</summary>
  Agentic AI has enabled capabilities in leveraging Large Language Models (LLMs) to autonomously resolve repository-level GitHub issues. However, due to the reliance on limited static description of issues, existing agentic approaches suffer from incorrect localization and incomplete validation. Solely relying on this information can bias LLM reasoning toward the narrow scope of the issue description, leading to incomplete patches that fail to address the underlying issue. In this paper, we presen...
  </details>

- **2026-09-08** — Priyanka Mary Mammen, Emil Joswin, Srujananjali Medicherla — [Do Agents Know When They Succeed? Calibrating Agent Confidence from Internal Representations](http://arxiv.org/abs/2609.09448v1)
  <details><summary>📄 Abstract</summary>
  As agentic systems getting adopted rapidly in safety critical applications, it is vital to measure the confidence associated with the agentic actions. In comparison to the traditional machine learning systems, agentic workflows have complex failure modes with planning, tool invocation and dynamic environment interactions. In this paper, we investigate whether model's internal representations provide stronger signals of eventual task success in multi-turn agentic setups. We introduce two compleme...
  </details>

- **2026-09-08** — Hamed Jafarzadeh Asl, Yuanhao Yu, Vahid Partovi Nia — [From Fixed Keys to Readable Schemas: Small Language Models for Vehicle Agent Function Calls](http://arxiv.org/abs/2609.09476v1)
  <details><summary>📄 Abstract</summary>
  In-vehicle assistants must translate natural-language requests into accurate vehicle function calls under strict memory and latency constraints, making small language models (SLMs) attractive for on-device deployment. For such models, a key design choice is how the available function surface is presented. Two approaches are to represent each function with a dedicated Functional Token (FT) or provide function schemas directly in the prompt. FTs enable compact inference but are restricted to funct...
  </details>

- **2026-09-08** — Wali Ullah Khan, Muhammad Adil — [Battery-Aware Rate-Splitting Multiple Access for Solar-Powered Cell-Free LEO Satellite Networks](http://arxiv.org/abs/2609.09445v1)
  <details><summary>📄 Abstract</summary>
  Cell-free low Earth orbit (LEO) satellite downlinks improve coverage and macro-diversity, but intermittent solar harvesting and finite onboard batteries can make communication-only resource allocation energy-aggressive. We develop battery-aware one-layer rate-splitting multiple access (BA-RSMA) for a fixed-cluster solar-powered cell-free LEO downlink. A perturbed physical-battery Lyapunov queue couples common/private power allocation to stored energy, while robust energy causality protects again...
  </details>

- **2026-09-08** — Nour Jamoussi, Marios Kountouris — [Explaining f-Divergence-Based Regularization via Local Curvature and Sharpness-Aware Minimization](http://arxiv.org/abs/2609.09367v1)
  <details><summary>📄 Abstract</summary>
  Divergence-based regularization and Sharpness-Aware Minimization (SAM) are two prominent approaches for improving generalization in deep learning, both motivated by robustness to perturbations. However, their relationship has remained largely unexplored. Building on classical second-order expansions of $f$-divergences, we show that the two methods are locally consistent under parameter-space perturbations: both induce curvature-sensitive penalties, with divergence regularization yielding a Fishe...
  </details>

- **2026-09-08** — Eleanor Courcelle, Jane Shaw MacDonald, Swati Patel — [Persistence of n-Species Lotka-Volterra Models with Periodic Pulses](http://arxiv.org/abs/2609.09343v1)
  <details><summary>📄 Abstract</summary>
  Periodic impulsive interventions arise naturally in the management of biological populations, including chemotherapy, pesticide application, and infectious-disease treatment. We develop general conditions for permanence in n-species population models subject to periodic multiplicative pulse disturbances. Our main result provides a sufficient condition for permanence in terms of weighted long-term growth rates on a Morse decomposition of the extinction set, explicitly separating the contributions...
  </details>

- **2026-09-08** — Annalisa De Cia, David Cont, Kevin Heng et al. — [The future of high-resolution UV spectroscopy: Science with a UV Échelle spectrograph on the Habitable Worlds Observatory, or a dedicated mission](http://arxiv.org/abs/2609.09329v1)
  <details><summary>📄 Abstract</summary>
  High-resolution UV spectroscopy serves a diversity of science cases, from small bodies to planets, stars, and galaxies, but is currently limited to the Hubble Space Telescope and bright targets. Major advances require increasing sensitivity by at least one order of magnitude. Here we present the UV science cases for PEGASUS (Planets, Earths, Galaxies, And Stars UV Spectrograph), a UV Échelle high-resolution spectrograph concept, with $R = λ/δλ\sim 100\,000$ (full range 10 000-140 000) and coveri...
  </details>

- **2026-09-08** — Juan D. Gil, Ehecatl Antonio Del Rio Chanona, José Luis Guzmán et al. — [From Learning to Control: Data-Driven Multi-Agent Reinforcement Learning for Multivariable Control in a Microalgae Bioprocess](http://arxiv.org/abs/2609.09313v1)
  <details><summary>📄 Abstract</summary>
  Effective control of bioprocesses is particularly challenging due to the intrinsic nonlinearity and dynamic variability of living-cell systems. In microalgae-based photobioreactors (PBRs), maintaining stable pH and dissolved oxygen (DO) levels is critical for optimal growth and productivity, yet their strong coupling and sensitivity to environmental fluctuations make multivariable control difficult. This study proposes a novel hybrid offline-online Multi-Agent Reinforcement Learning (MARL) frame...
  </details>

- **2026-09-08** —  Orantqing, Shengpeng Ji, Junlong Tong et al. — [Omni Interaction Agent Technical Report](http://arxiv.org/abs/2609.08977v2)
  <details><summary>📄 Abstract</summary>
  In this work, we present Gander, an end-to-end model that unifies omni perception, realtime interaction, and agentic capabilities within a single framework. In contrast to turn-based conventional paradigms, Gander continuously receives streaming inputs across multiple modalities, including video, speech, and text, enabling natural full-duplex interaction in both everyday conversations and complex workflow-oriented agent scenarios. Users can interrupt the model at any time, while the model can al...
  </details>

- **2026-09-08** — Anirudh Malik, M Sparsh Mehra, Poojith Devan — [Scaling Post-Training Ternarisation to Qwen3-8B Capability Retention, Reproduction, Lossless Packing, and Packed Execution](http://arxiv.org/abs/2609.09240v1)
  <details><summary>📄 Abstract</summary>
  Ultra-low-bit language models promise reductions in storage and memory traffic, but a nominal "1.58-bit" label does not specify the deployed representation or its execution cost. We study a scale-up of an aggressive post-training conversion pipeline from Qwen3-4B to Qwen3-8B.   The conversion uses KOTMS rotation, E2M-ATQ adaptive ternarisation, and GPTQ-style error compensation in a weight-only A16 configuration. We do not claim these algorithms as new. Our contribution is the end-to-end scale-u...
  </details>

- **2026-09-08** — Yiling Ma, Yilun Zhao, Sihong Wu et al. — [ActReview: Rebuttal-Guided Training Data and Rubric Rewards for Actionable Peer Review Generation](http://arxiv.org/abs/2609.09076v1)
  <details><summary>📄 Abstract</summary>
  As LLMs are increasingly used for pre-submission self-review, there is growing demand for feedback that not only identifies weaknesses but also guides authors toward concrete revisions. We study this as Actionable Peer-review Generation and decompose it into two subtasks: diagnostic claim generation and revision suggestion generation. We introduce ActReview, a rebuttal-guided post-training framework that connects paper-specific diagnoses to concrete, grounded revision plans. Our central insight ...
  </details>

- **2026-09-08** — Yi-Chang Chen, Chun Wei Chen, Dien-Ruei Wu et al. — [TASTE2: Text-Aligned Speech Modeling and Deployment toward Full-Duplex Voice Interaction](http://arxiv.org/abs/2609.08956v1)
  <details><summary>📄 Abstract</summary>
  Full-duplex voice interaction requires more than utterance-level conversion. It must process streaming speech, manage turn-taking and interruptions, while preserving pretrained linguistic competence and acoustic paralinguistic cues. We ask whether TASTE (Text-Aligned Speech Tokenization and Embedding) provides a viable path toward this goal. We present TASTE2, which transforms utterance-level TASTE into an incremental dialogue stack. A shared text-token vocabulary removes word-level averaging, w...
  </details>

- **2026-09-08** — Mohammadhossein Malekpour, Mohamed Riahi, Maxime Lamothe et al. — [SQLMorph: Query Mutation and Fine-Grained Metrics for Text-to-SQL Evaluation](http://arxiv.org/abs/2609.08950v1)
  <details><summary>📄 Abstract</summary>
  Text-to-SQL systems translate natural language queries into executable SQL, democratizing access to structured data. Despite recent advances driven by large language models (LLMs), evaluation remains a major bottleneck: public benchmarks fail to capture the complexity of enterprise schema, while building private evaluation sets is costly and nondeterministic, making evaluation results difficult to reproduce. To address this issue, we present SQLMorph, a framework for Text-to-SQL evaluation via q...
  </details>

- **2026-09-08** — Tinghe Ding, Jiahao Li, He Wang — [CASD: Chunk-Aligned Semantic Distillation for Multi-StageRobot Manipulation](http://arxiv.org/abs/2609.08638v1)
  <details><summary>📄 Abstract</summary>
  An action chunk can span several stages of a manipulation task, yet a label for its first step describes only the current stage. We introduce Chunk-Aligned Semantic Distillation (CASD), which derives semantic targets for entire action chunks. An offline vision--language model segments demonstrations into described stages. Their occupancy within each action chunk determines a weighted semantic target, including transitions between stages. A CASD generator learns to predict this target from the cu...
  </details>

- **2026-09-08** — Yiran Wang, Zeyu Zhang, Ling Shao et al. — [ReMoMask-2: Latent Retrieval-Augmented Masked Motion Generation](http://arxiv.org/abs/2609.08365v1)
  <details><summary>📄 Abstract</summary>
  Text-to-motion (T2M) generation maps natural language to human joint movements, aiding gaming, VR, and robotics. Retrieval-Augmented Text-to-Motion (RAG-T2M) improves generation on complex descriptions by conditioning on retrieved motion-text pairs. However, existing RAG-T2M models face two challenges: coarse-grained retrieval and fusion mechanisms overlook the hierarchical, spatial-temporal topology of human motion, and a representation gap exists because retrieved evidence resides in a semanti...
  </details>

- **2026-09-08** — Jianqiang Xiao, Xiang Deng, Yuexuan Sun et al. — [Dual-Layer Semantic-Spatial Belief Mapping for Aerial Object Goal Navigation](http://arxiv.org/abs/2609.08164v1)
  <details><summary>📄 Abstract</summary>
  Aerial Object Goal Navigation (ObjectNav) requires an unmanned aerial vehicle (UAV) to locate a described target in an unknown outdoor environment using onboard visual observations. Vision-language models (VLMs) can interpret open-ended target descriptions and visual observations, but their frame-level outputs are often noisy, sparse, and spatially transient. We propose AeroBelief, a dual-layer semantic-spatial belief mapping framework that transforms transient VLM observations into persistent s...
  </details>

- **2026-09-08** — Igor Pavlovic, Thiemo Wandel, Anton Obukhov et al. — [Marigold V2: Revisiting Diffusion Transformers for Monocular Depth Estimation](http://arxiv.org/abs/2609.08084v1)
  <details><summary>📄 Abstract</summary>
  Monocular depth estimation is a ubiquitous yet highly ill-posed computer vision task, with downstream applications in scene reconstruction, computational photography, and robotics, among others. Despite the field's maturity, recent models still struggle to generalize to out-of-distribution inputs and to produce sharp and detailed depth maps. In this paper, we revisit Marigold, a set of techniques for repurposing modern image generation and editing models, powered by the diffusion transformer (Di...
  </details>

- **2026-09-08** —  Orantqing, Shengpeng Ji, Junlong Tong et al. — [Omni Interaction Agent Technical Report](http://arxiv.org/abs/2609.08977v1)
  <details><summary>📄 Abstract</summary>
  In this work, we present Gander, an end-to-end model that unifies omni perception, realtime interaction, and agentic capabilities within a single framework. In contrast to turn-based conventional paradigms, Gander continuously receives streaming inputs across multiple modalities, including video, speech, and text, enabling natural full-duplex interaction in both everyday conversations and complex workflow-oriented agent scenarios. Users can interrupt the model at any time, while the model can al...
  </details>

- **2026-09-08** — Benjamin Chang, Michael Amir, Manon Flageat et al. — [Remotely Detectable Keyed Communication through Motion](http://arxiv.org/abs/2609.08920v1)
  <details><summary>📄 Abstract</summary>
  Messages from electronic devices are conventionally received as text, audio, or radio signals. But robots move with rich, articulate motion in the real world, opening up the possibility of transmitting messages through motion itself. In this paper, we consider the problem of motion-based communication, where we seek to modify a robot's movements so as to transmit messages detectable from remote sensing (e.g., video or motion capture), without degrading policy performance. We introduce a method f...
  </details>

- **2026-09-08** — David Grass, Emma Bao, Martin C. Fischer et al. — [Evaluating the predictive power of pump-probe imaging contrast of melanin for metastatic outcome: A 71-patient study](http://arxiv.org/abs/2609.08814v1)
  <details><summary>📄 Abstract</summary>
  Significance: Most melanoma deaths arise from metastatic spread, yet current staging imperfectly identifies which primary tumors will progress. Melanin structure is altered during malignant transformation, and pump-probe microscopy (PPM) measures melanin excited-state dynamics in standard biopsy sections, offering molecular contrast that is complementary to morphology-based assessment.   Aim: To determine whether PPM-derived melanin excited-state dynamics in primary cutaneous melanoma can predic...
  </details>

- **2026-09-08** — Matthias von Davier — [The Rater Ising-Potts Model with LLM-Derived Weights: An Application to Multi-Category Scoring Reliability](http://arxiv.org/abs/2609.08797v1)
  <details><summary>📄 Abstract</summary>
  The Ising model is extended to the Potts model for multinomial data. We introduce a Rater Ising-Potts model that uses agreement indicators between pairs of raters and category labels, with weights derived from LLM embeddings. The model does not presuppose ordered category thresholds or equidistant scoring; instead, it focuses directly on pairwise agreement among raters and assigns category-specific positive weights, making it particularly suited for multi-category scoring reliability when raters...
  </details>

- **2026-09-08** — Solaleh Mohammadi, Xiang Gao, Kaiqing Zhang — [Entropic Risk-Sensitive Evolutionary Learning and Equilibrium Selection in Coordination Games](http://arxiv.org/abs/2609.08677v1)
  <details><summary>📄 Abstract</summary>
  We study risk-sensitive evolutionary learning dynamics and their long-run equilibrium selection behaviors in coordination games. Agents' risk attitudes enter through the classical entropic risk measure, which evaluates opponent-induced payoff uncertainty and feeds into noisy best responses under two standard revision protocols: best response with mutations and logit choice. We first analyze $2\times 2$ coordination games in both single-population symmetric and two-population asymmetric settings....
  </details>

- **2026-09-08** — Tomas Guija-Valiente, Blanca Rodriguez-Gonzalez, Norberto Malpica — [SynthRCT: Scalable Conditional Deformation Synthesis for Synthetic Repeat CT Generation](http://arxiv.org/abs/2609.08627v1)
  <details><summary>📄 Abstract</summary>
  In proton therapy, plans are typically optimized on a single planning CT, making robustness evaluation essential under anatomical changes. However, current scenarios often rely on simplified perturbations that poorly capture complex, patient-specific variability. We propose SynthRCT, a scalable conditional generative framework for 3D anatomical deformation synthesis. Based on a conditional variational autoencoder, SynthRCT learns a latent deformation space and decodes sampled latent codes into l...
  </details>

- **2026-09-08** — Antonin Poché, Fanny Jourdan, Nils Feldhus et al. — [Limitations of Automated Simulatability: LLM Simulators Can Bypass Explanations](http://arxiv.org/abs/2609.08585v1)
  <details><summary>📄 Abstract</summary>
  Simulatability is an evaluation protocol for explanations that quantifies their usefulness by how well they help a user predict a task model's outputs. Since human evaluation is costly, automated simulatability replaces human explainees with LLM simulators, as proposed in ConSim (Poché et al., 2025) for large-scale experiments. We qualitatively replicate and extend ConSim's ranking of explanation methods across the tested datasets, explanation families, and simulator LLMs, and identify two limit...
  </details>

- **2026-09-08** — Ramona Häuselmann, Mario A. V. Saucedo, Christoforos Kanellakis et al. — [Estimating Semantic Ambiguity via Gaussian Context Distributions for VLM-Driven Traversability Analysis](http://arxiv.org/abs/2609.08583v1)
  <details><summary>📄 Abstract</summary>
  Autonomous navigation in unstructured environments requires robust scene understanding, yet Vision-Language Models (VLMs) often suffer from semantic ambiguity, where conflicting predictions can lead to dangerous failures. To address this, we present a novel pipeline for vision-based traversability estimation that explicitly models contextual uncertainty. Our approach utilizes Conceptual Anchoring to ground open-vocabulary VLM predictions onto a continuous physical traversability scale. By formul...
  </details>

- **2026-09-08** — Xiaohu Xu, Tong Zhu — [TSBench: A physics-grounded benchmark for evaluating LLM understanding of chemical reaction mechanisms](http://arxiv.org/abs/2609.08503v1)
  <details><summary>📄 Abstract</summary>
  Understanding a chemical reaction requires mapping a symbolic reactant-product description onto the three-dimensional pathway through which atoms rearrange, yet chemistry benchmarks for large language models (LLMs) largely probe factual knowledge and text-based reasoning. Here we introduce TSBench, a benchmark in which an LLM agent uses structure-editing tools to construct three-dimensional transition-state (TS) guesses verified by an automated quantum-chemical pipeline, yielding a physics-groun...
  </details>

- **2026-09-08** — Krzysztof M. Graczyk, Beata E. Kowal, Rwik Dharmapal Banerjee et al. — [Inclusive electron-nucleus cross section models from domain adaptation](http://arxiv.org/abs/2609.08463v1)
  <details><summary>📄 Abstract</summary>
  We apply transfer learning (TL) to construct data-driven models of inclusive electron-nucleus cross sections. Starting from an ensemble of deep neural networks pretrained on \(^{12}\)C data, we fine-tune the models separately for \(^{3}\)He, \(^{6}\)Li, \(^{16}\)O, \(^{27}\)Al, \(^{40}\)Ca, and \(^{56}\)Fe. The resulting models improve for all targets, marginally so for oxygen, where the carbon baseline is already adequate, although their predictive robustness depends on the amount, coverage, an...
  </details>

- **2026-09-08** — Bella Godiva, Yeonju Kim, Yong Man Ro — [Noise Adaptive Streaming Audio-Visual Speech Token Enhancement for Robust Full-Duplex Spoken Dialogue Models](http://arxiv.org/abs/2609.08390v1)
  <details><summary>📄 Abstract</summary>
  Full-duplex spoken dialogue systems enable simultaneous listening and speaking, but their audio-only perception often fails under background noise and overlapping speech, leading to incoherent responses. Recent audio-visual dialogue approaches show that incorporating visual cues such as lip movements improve robustness under audio corruption. However, existing approaches often adapt the large speech dialogue model itself to process visual input, requiring costly multimodal training. We propose A...
  </details>

- **2026-09-08** — Han Xiao, Yifan Niu, Dongyi Liu et al. — [TV-Regulated OPD: Direction Matters in On-Policy Distillation](http://arxiv.org/abs/2609.08341v1)
  <details><summary>📄 Abstract</summary>
  On-Policy Distillation (OPD) facilitates the transfer of knowledge from domain expert to student in the post-training phase of Large Language Models (LLMs). However, the supervision signals in mainstream OPD methods suffer from high variance and noise which is generally instable during training. In this work, we systematically investigated what really matters to the performance and the fundamental mechanisms behind the instability during training. We found that retaining only the sign of token-l...
  </details>

- **2026-09-08** — Kevin Chuanpu Fu, Yongsen Zheng, Zee Kin Yeong et al. — [VeriScene: Reconstructing Crime Scenes from Legal Evidence via World-Model Agent](http://arxiv.org/abs/2609.08342v1)
  <details><summary>📄 Abstract</summary>
  World models take multimodal inputs like text, photos, and diagrams to generate dynamic scenes in accordance with the laws of physics, thus opening a compelling application: fusing multimodal legal evidence to re-create a crime scene and re-enact how an offence could have been committed. However, feeding the raw, unorganized evidence into a world model fails in forensic use: it silently drops evidence, glosses over contradictory testimony, and produces motion that violates the evidentiary record...
  </details>

- **2026-09-08** — Tingyin Zhao, Mingtao Huang, Yuan Shen — [FPicker: Topology-Guided Evolution for Filament Tracing in Low-SNR Microscopy](http://arxiv.org/abs/2609.08305v1)
  <details><summary>📄 Abstract</summary>
  Automating filament tracing in Cryo-Electron Microscopy (Cryo-EM) is essential for 3D helical reconstruction but challenged by intersecting topologies and extremely low Signal-to-Noise Ratios ($\text{SNR} = σ_s^2/σ_n^2$ < 0.1 or -10 dB). Existing paradigms fail: pixel-wise segmenters suffer from severe topological fracturing, box-based detectors face ghost center drift, sequential trackers derail due to error accumulation, and traditional active contours collapse under artificial closed-curve co...
  </details>

- **2026-09-08** — Chen Shen — [What Eviction Destroys: A Restore-Counterfactual Audit of Forgetting in Agent Memory](http://arxiv.org/abs/2609.08279v1)
  <details><summary>📄 Abstract</summary>
  Agent memory systems must discard stored information when their history exceeds a fixed token budget. Existing budget-accuracy frontiers quantify the resulting loss in accuracy, but do not distinguish irreversible losses caused by eviction from recoverable retrieval failures. We introduce the restore counterfactual, a per-question paired intervention that reinstates the question's gold evidence in the read-time context and reruns the same reader. Combining the change in correctness with whether ...
  </details>

- **2026-09-08** — SeongJun Jeong, Minjoon Jung, Woo Suk Choi et al. — [CS-CLIP: Compositional Scene Graph-guided CLIP for Robust Compositional Reasoning](http://arxiv.org/abs/2609.08242v1)
  <details><summary>📄 Abstract</summary>
  Vision-language models (VLMs) demonstrate strong performance across compositional reasoning benchmarks, which require reasoning over semantic perturbations of objects, attributes, relations, and their interactions. However, our controlled analysis reveals that existing compositionality-aware VLMs exhibit element-specific biases, often underperforming vanilla CLIP on certain compositional elements. To address this, we propose Compositional Scene Graph-guided CLIP (CS-CLIP), which uses scene graph...
  </details>

- **2026-09-08** — Arun Vignesh Malarkkan, Xinyuan Wang, Yanjie Fu — [Vision: Data-Centric Anchoring for Robust and Interpretable Agentic AI](http://arxiv.org/abs/2609.08216v1)
  <details><summary>📄 Abstract</summary>
  Agentic AI systems built on large language models fail in two persistent ways that scaling does not fix: they break under distribution shift, and they cannot explain the decisions they make. We argue these are co-symptoms of one structural deficiency in the data lifecycle that governs how agents are trained, evaluated, and deployed. Observational interaction logs record what an agent did, not what it would have done otherwise. They encode spurious correlations without controlled variation, so th...
  </details>

- **2026-09-08** — Ronaldo Celso Messias Correia, Douglas Francisquini Toledo, Camila Tolin Santos da Silva — [UnespDataLens-RM: A Reference Model for Analytical Data Engineering with Governance, Quality, Provenance, and Reproducibility](http://arxiv.org/abs/2609.08184v1)
  <details><summary>📄 Abstract</summary>
  The growing reliance on data in analytical processes and evidence-based decision-making has reinforced the importance of Data Engineering in building pipelines capable of integrating, transforming, validating, and delivering data from heterogeneous sources. However, the reliability of analytical assets depends not only on data processing capabilities but also on mechanisms for governance, quality assurance, provenance, traceability, versioning, and reproducibility throughout their lifecycle. The...
  </details>


### 📂 watermark
*水印与溯源 / Watermarking & Provenance* — 16 papers

- **2026-09-10** — Yutong Hu, Fengjiao Chen, Xuezhi Cao et al. — [2AM: Grounding Agent-Side Memory as Guidance for Steerable Action Models in Long-Horizon Manipulation](http://arxiv.org/abs/2609.11308v1)
  <details><summary>📄 Abstract</summary>
  Long-horizon robot manipulation requires memory, but not necessarily inside the action policy. To address such tasks, current agentic systems often combine VLAs with planners and geometric tools, sometimes using additional depth or calibrated geometry. These systems confound attribution: gains may come from richer observations or alternative motor tools, while failures may stem from either the policy or an under-specified language interface. We isolate this question through a deliberately constr...
  </details>

- **2026-09-10** — Abdul Karim Gizzini, Yahia Medjahdi — [X-RACE: XAI-assisted Recurrent neural network Attribution for Channel Estimation](http://arxiv.org/abs/2609.11211v1)
  <details><summary>📄 Abstract</summary>
  Deep learning models, notably Long Short-Term Memory (LSTM), have demonstrated promising performance in channel estimation for high-mobility vehicular environments. However, their black-box nature and architectural overhead limit trustworthiness and efficiency. Classical explainable AI (XAI) methods rely on costly iterative processes, offering only input-level filtering without addressing architectural fine-tuning. To overcome these limitations, this paper proposes the XAI-assisted Recurrent neu...
  </details>

- **2026-09-10** — Joshua Ong Jun Leang, Haonan Li, Zheng Zhao et al. — [Magenta: Closing the Loop Between Mathematical Reasoning and Lean Verification](http://arxiv.org/abs/2609.11319v1)
  <details><summary>📄 Abstract</summary>
  Most of mathematical knowledge has been communicated through so-called informal use of mathematics and natural language. With large language models (LLMs) being highly adept in using natural language, they achieve strong performance, yet not perfect, in informal mathematical reasoning. Restraining LLMs to informal reasoning misses out on the opportunity to use the discrete verification abilities that machines offer through machine-checkable proofs. In this paper, we bridge the gap between inform...
  </details>

- **2026-09-10** — Dario Picozzi — [The information geometry of large language models is shared, learned, and controllable](http://arxiv.org/abs/2609.11063v1)
  <details><summary>📄 Abstract</summary>
  Large language models learn similar behaviours, yet it remains unclear what structure they share or how to change one behaviour without disturbing others. The Fisher-Rao geometry of next-token probabilities connects these questions: behaviour determines this geometry up to output-preserving symmetries, whereas activation geometry depends on coordinates. Across transformer, state-space and recurrent models, output geometries agree more strongly than activation geometries, and shared geometry supp...
  </details>

- **2026-09-09** — Suman Raj, Hai Duc Nguyen, Haochen Pan et al. — [Avatar: Toward Autonomous End-to-End Orchestration of Scientific Workflows using LLMs](http://arxiv.org/abs/2609.10509v1)
  <details><summary>📄 Abstract</summary>
  Scientific workflow management (WMSs) systems automate execution, yet orchestrate using fixed, hand-tuned rules. LLM agents promise more autonomous orchestration, but it remains unclear where to introduce agentic reasoning, how to bound its risk, and when it actually helps. We present Avatar, an actor-based architecture comprising an orchestrator, an executor, and a provenance monitor. Each actor's decision policy is pluggable (rule-based or LLM-backed) via a single adapter-validated action cata...
  </details>

- **2026-09-09** — Rui Sun, Zhan Shi, Bing He — [TRACE: Training Reasoning Agents for Causal Exploration with Synthesized Rewards](http://arxiv.org/abs/2609.10315v1)
  <details><summary>📄 Abstract</summary>
  Reinforcement learning with verifiable rewards (RLVR) has advanced language-model reasoning in domains such as mathematics and code, where objective answers are inexpensive to check. Diagnostic reasoning over complex data lacks this advantage: establishing the true cause of an anomaly often requires costly expert investigation and may remain ambiguous after the fact. We ask whether this asymmetry of verification can instead be engineered. We sample an intervention, inject it into a controlled si...
  </details>

- **2026-09-09** — Zhantong Xue, Pingchuan Ma, Zhaoyu Wang et al. — [Sound Debloating of Redundant Checks in Zero-Knowledge Machine-Learning Circuits](http://arxiv.org/abs/2609.10149v1)
  <details><summary>📄 Abstract</summary>
  Zero-knowledge (ZK) proof systems for neural-network inference compile the model into a system of arithmetic constraints. Many of these constraints are redundant checks: range proofs, sign lookups, and bit decompositions who are globally entailed by the rest of the circuit through chains of reasoning that span distant gadgets. Removing them shrinks the circuit and accelerates proving, but the removal must be carefully justified: an unsoundly debloated circuit becomes forgeable, accepting witness...
  </details>

- **2026-09-09** — Yazhou Zhu — [From Few-Shot Segmentation to Clinician-in-the-Loop Medical Image Analysis](http://arxiv.org/abs/2609.10001v1)
  <details><summary>📄 Abstract</summary>
  Few-shot medical image segmentation (FSMIS) seeks to delineate unseen structures from a small support set, but its standard formulation fixes task-defining evidence before inference. This assumption is fragile when query cases exhibit acquisition shift, atypical pathology, ambiguous boundaries, or poor image quality. Prototype learning, cross-domain matching, interactive segmentation, uncertainty estimation, test-time adaptation, and promptable foundation models address parts of this problem, ye...
  </details>

- **2026-09-09** — Xing Zhang, Guanghui Wang, Yanwei Cui et al. — [UnitBoost: Managing Compound LLM Systems with a Merge Operator, Not a Model](http://arxiv.org/abs/2609.09815v1)
  <details><summary>📄 Abstract</summary>
  Compound LLM systems often solve a coordination problem by adding a higher-level LLM. The resulting meta-agent reads workers' outputs, writes the final answer, allocates later calls, and decides when to stop. It is expressive, but it also concentrates three control decisions in an opaque, order-sensitive model call. We ask whether the manager needs to be generative at all. UnitBoost replaces that model with a defined meta-level operator: a task-given unit map turns worker outputs into slot-value...
  </details>

- **2026-09-08** — Yibo Meng, Ruiqi Chen, Shuheng Cao et al. — [Where Does the Human End? Creative Agency with Generative AI across Five Years of Chinese Digital Painting](http://arxiv.org/abs/2609.09333v1)
  <details><summary>📄 Abstract</summary>
  As generative AI enters creative work, practitioners must decide where AI assistance ends and human authorship begins. Human-agent interaction (HAI) research has examined AI as a tool, collaborator, consultant, and competitor. The longitudinal problem is how these roles are revised as systems become more capable, public, and economically embedded. We report a five-year interview study with 17 Chinese digital painters, based on annual semi-structured interviews from 2021 to 2025. Participants des...
  </details>

- **2026-09-08** — Xiaoqun Liu, Tanu Mitra, Harshit Rajgarhia et al. — [Voice or Stereotype? Disentangling Acoustic and Content-Based Gender in Speech-to-Speech Models](http://arxiv.org/abs/2609.09263v1)
  <details><summary>📄 Abstract</summary>
  Speech-to-speech (S2S) models now run inside dubbing, translation, and voice agents. Unlike text models, they hear the speaker's voice, which carries the speaker's gender. A faithful system should treat a speaker as who they sound like, not as whoever usually says what they said. Testing this is harder than it looks, since most S2S models answer in a single, fixed output voice, hard-coded so it cannot drift toward a stereotype. Checking the output voice comes back clean even when the model is bi...
  </details>

- **2026-09-08** — Boyu Yang, Jiazheng Sun, Zilong Lu et al. — [MeClear: Cooperative Game-Theoretic Attribution and Risk-Aware Memory Clearance for Long-Horizon LLM Agents](http://arxiv.org/abs/2609.09115v1)
  <details><summary>📄 Abstract</summary>
  Long horizon Large Language Model (LLM) agents rely on external memory systems to preserve user preferences and task knowledge across extended interactions. Conventional retrieval mechanisms optimize semantic compatibility rather than downstream utility, frequently introducing outdated, misleading, or conflicting evidence into the active context. We present MeClear, a task conditioned memory clearance framework that identifies memories featuring negative downstream utility through cooperative at...
  </details>

- **2026-09-08** — Furqan Nasir, Muhammad Atif Saeed, Muhammad Ehsan et al. — [OntoKG-EQ: A provenance-grounded, competency-question-governed knowledge graph for auditable analyst querying](http://arxiv.org/abs/2609.08869v1)
  <details><summary>📄 Abstract</summary>
  Analysts in emerging equity markets keep answering the same questions. Did fundamentals match the market's response? How does the local currency co-move with returns? Which firms outperform sector and benchmark, and which disclosures coincide with abnormal trading? These answers come from ad-hoc spreadsheets that are hard to reproduce, audit, or trust. We present OntoKG-EQ, a knowledge-based system that makes such queries reproducible, evidence-linked, temporally explicit, valid, and inspectable...
  </details>

- **2026-09-08** — Daniel Rosendo, Renan Souza, Kelsey Carter et al. — [Exploring the Genesis Platform Capabilities to Accelerate Scientific Discovery in OPAL](http://arxiv.org/abs/2609.08844v1)
  <details><summary>📄 Abstract</summary>
  Autonomous, cross-facility science requires capabilities that no individual project should have to build for itself: managed execution for long-lived services, versioned distribution of models to remote compute systems, governed access to large language models, a shared substrate for experimental data, and end-to-end provenance. The U.S. Department of Energy Genesis Mission platform, delivered through the American Science Cloud, provides these as reusable services. This paper reports how the Gen...
  </details>

- **2026-09-08** — Giuseppe De Rosa, Pietro Liguori, Domenico Cotroneo — [Beyond Fixed Fault Models: Comparing LLM-Based and Rule-Based Fault Injection in OpenStack](http://arxiv.org/abs/2609.08681v1)
  <details><summary>📄 Abstract</summary>
  Software Fault Injection (SFI) supports testing of cloud systems by introducing software defects and observing their manifestation. Rule-based injectors such as ProFIPy provide controlled and reproducible source-level mutations but require fault patterns to be encoded manually. Large Language Models (LLMs) offer a data-driven alternative by generating context-dependent software faults. We compare two code LLMs, Qwen2.5-Coder and DeepSeek-Coder, with ProFIPy in OpenStack's Nova and Cinder service...
  </details>

- **2026-09-08** — Wentao Li, Yibo Wu, Yizhe Chen et al. — [SciFigure2Code: An AI-Reconstructed Benchmark for Scientific Figure-to-Code](http://arxiv.org/abs/2609.08155v1)
  <details><summary>📄 Abstract</summary>
  Scientific figures are the interface through which research claims are inspected and reused, but final published panels rarely expose the data or plotting code that produced them. Recovering this hidden provenance from pixels is therefore underdetermined. We introduce SciFigure2Code, an AI-reconstructed benchmark that instead evaluates presentation recovery: generating editable Python programs that preserve how a scientific panel is arranged and read. Role-specialized Codex agents generate, exec...
  </details>


### 📂 unlearning
*机器遗忘 / Machine Unlearning* — 1 papers

- **2026-09-10** — Rongcan Pei, Zhepei Wei, Shuyao Xu et al. — [Negative Self-Distillation: Learning to Reason by Avoiding Flaws](http://arxiv.org/abs/2609.11699v1)
  <details><summary>📄 Abstract</summary>
  On-Policy Self-Distillation (OPSD) has emerged as a popular paradigm for large language model (LLM) self-improvement, allowing models to act as their own teachers by leveraging privileged information such as ground-truth solutions. However, recent findings indicate that OPSD can severely degrade the performance of LLMs on complex reasoning tasks: By forcing the student to imitate an artificially confident reasoning trace conditioned on privileged information, OPSD inadvertently suppresses expres...
  </details>


### 📂 survey
*综述与系统化 / Surveys & Systematization* — 8 papers

- **2026-09-10** — Jiani Ding, Minghao Yue, Yongda Zhu et al. — [Learning JWST. I. A Foundation Model for New Population Discoveries and Morphology-Aware Photometric Redshift Measurements in the JADES Survey](http://arxiv.org/abs/2609.11879v1)
  <details><summary>📄 Abstract</summary>
  We present FM-JADES-v1, a self-supervised foundation model for James Webb Space Telescope ({\em JWST}) deep-field science, trained with 482,444 objects from the {\em JWST} Advanced Deep Extragalactic Survey (JADES) Data Release 5 using multi-band imaging and the photometric catalog. The shared embedding space is trained without class labels. We demonstrate that FM-JADES-v1 can serve as a powerful tool for object discovery and improving property measurements using two experiments, blind active di...
  </details>

- **2026-09-09** — Kateryna Karpo, Artem Chernodub — [Larger Context Window, Fewer Overcorrections: Optimizing Prompts and Batching for Minimal-Edit Grammatical Error Correction](http://arxiv.org/abs/2609.10810v1)
  <details><summary>📄 Abstract</summary>
  Minimal-edit Grammatical Error Correction (GEC) is a challenging task for zero- and few-shot prompted Large Language Models (LLMs), which systematically overcorrect and degrade $F_{0.5}$ by rewriting well-formed spans. While fine-tuning provides an effective solution, it imposes substantial infrastructure demands. We introduce a prompt-based approach that closes the gap to fine-tuned models through three advances in GEC prompting methodology. First, we introduce taxonomy-based instructions to en...
  </details>

- **2026-09-09** — Indira Sen, Georg Ahnert, Leah von der Heyde et al. — [Total Simulated Survey Error: Designing and Diagnosing Survey Responses from Large Language Models](http://arxiv.org/abs/2609.10280v1)
  <details><summary>📄 Abstract</summary>
  Large Language models (LLMs), having been trained on vast amounts of human-generated data, may encode the attitudes and behaviors of these humans. As such, LLMs show promise in mimicking human-like patterns that facilitate their use in simulating people in a wide variety of contexts. One such context is using LLMs as 'silicon samples', i.e., proxies of people in answering survey questions to establish public opinion, design policies, or use as (social) scientific data. However, several critical ...
  </details>

- **2026-09-09** — Chenwei Wang, Haochen Li, Shuk Ching Tang et al. — [Cost-Aware Vision--Language Model Arbitration for Fabric Structure Recognition A Deployable Multi-Agent System](http://arxiv.org/abs/2609.10065v1)
  <details><summary>📄 Abstract</summary>
  Recognizing a fabric's structure is a prerequisite for translating textile-specific material information into structured digital form for downstream supply-chain systems. Pure CNN classifiers are cost-efficient but fail on visually ambiguous categories; vision--language models (VLMs) generalize more broadly but cost much more per image and are unstable on specialist domains. We present a multi-agent system in which a CNN cascade handles the easy majority and a VLM is invoked only as a selective ...
  </details>

- **2026-09-09** — Zizhen Wang, Bo Feng, Zhengfeng Lai et al. — [Putting Captions to the Test: Evaluating Video Caption Quality through Multiple-Choice Question Answering](http://arxiv.org/abs/2609.09973v1)
  <details><summary>📄 Abstract</summary>
  Evaluating video captioning remains a critical challenge for Visual Large Language Models (VLLMs). Existing metrics primarily rely on matching generated text against ground-truth references. This paradigm suffers from the ``one-to-many'' nature of video description, where high-quality captions are often penalized for lexical mismatches or valid shifts in visual focus. Furthermore, such assessments are typically one-dimensional, failing to provide a fine-grained analysis of caption quality. To ad...
  </details>

- **2026-09-08** — Yizhong Geng, Kecan Mao, Qifei Li et al. — [Stabilizing Instruction Supervision for Instruct-TTS via Controllable Diversification and Drift Filtering](http://arxiv.org/abs/2609.08204v1)
  <details><summary>📄 Abstract</summary>
  Instruct-TTS systems expand structured style labels into natural-language training instructions through LLM rewriting, yet we find that over 40% of unconstrained rewrites contain semantic drift that corrupts supervision and weakens generalization. We formalize this problem as instruction supervision instability and propose a data-centric stabilization recipe that jointly improves coverage and fidelity through three mechanisms: controllable instruction diversification for systematic expansion, LL...
  </details>

- **2026-09-08** — Andreas Tersenov, Sacha Guerrini, Jean-Luc Starck et al. — [Mitigating baryonic effects in weak lensing with higher-order statistics](http://arxiv.org/abs/2609.09131v1)
  <details><summary>📄 Abstract</summary>
  Weak gravitational lensing is a premier cosmological probe, but its small-scale statistical power is compromised by baryonic feedback. Higher-order statistics capture non-Gaussian information that the power spectrum misses, yet their sensitivity to feedback remains a concern for Stage IV surveys.   We quantify how unmodeled feedback biases the cosmological parameters inferred from the angular power spectrum (PS), starlet peak counts, and the starlet $\ell_1$-norm, and we determine the scale cuts...
  </details>

- **2026-09-08** — Zijian Shen, Bin Zhou, Jiguang Wang et al. — [LEBGen: An LLM-Enhanced Bayesian Network Framework for Few-Shot Travel Survey Data Generation](http://arxiv.org/abs/2609.08288v1)
  <details><summary>📄 Abstract</summary>
  Travel survey data are essential for transportation planning and travel behavior analysis, yet collecting large-scale representative samples is costly and time-consuming. A practical alternative is to generate synthetic survey records from a few-shot sample. However, such samples provide incomplete coverage of heterogeneous traveler groups and insufficient evidence for recovering the complex dependencies between demographic characteristics and travel behavior. Existing approaches have complement...
  </details>


### 📂 other
*其他安全相关 / Other Security-Related* — 166 papers

- **2026-09-10** — Lohitvel Gopikannan, Shashi Ranjan Kumar, Abhinav Sinha — [Predefined-Time Leaderless Consensus Under Denial-of-Service Attacks](http://arxiv.org/abs/2609.11781v1)
  <details><summary>📄 Abstract</summary>
  This paper addresses predefined-time resilient consensus of leaderless second-order nonlinear multi-agent systems under denial-of-service (DoS) attacks, motivated by coordination requirements in safety-critical applications. The agents are subject to bounded external disturbances and communicate over a strongly connected directed graph whose links are simultaneously disabled during attacks. We develop a switching sliding-mode protocol with the objective of reaching an invariant manifold of posit...
  </details>

- **2026-09-10** — Zhiying Lu — [LoopVAE: Recurrent Depth Across Scales for Visual Tokenization](http://arxiv.org/abs/2609.11516v1)
  <details><summary>📄 Abstract</summary>
  Hierarchical visual tokenizers typically allocate different processing blocks to different spatial scales. We ask how much of this computation can use the same parameters. LoopVAE reuses a scale- and loop-conditioned core within and across scales, while keeping resolution-changing transitions independent. A four-block core executes 28 block applications per encoder or decoder. On ImageNet-256, the 29M-parameter convolutional model reaches 0.28 rFID and 32.54 dB PSNR under an approximately 30-epo...
  </details>

- **2026-09-10** — Benjamin Gruenbaum, Doron Porat, Assaf Natanzon et al. — [Generating a Consistent Enterprise: Synthesis and Reference-Free Evaluation of Multi-System Business Data](http://arxiv.org/abs/2609.11286v1)
  <details><summary>📄 Abstract</summary>
  Synthetic relational data is normally produced by a model trained on a real dataset, and its quality is measured as the distance to that dataset. This paper describes a generator that has no real dataset at either end. Given an industry, a company size, a business model, a set of business applications, and a random seed, it produces a complete fictional enterprise: a workforce, a customer base, sales deals, support tickets, recorded calls, chat messages, and documents, all consistent with one an...
  </details>

- **2026-09-10** — Divyanshu Kumar, Rohith HN, Nitin Aravind Birur et al. — [The Agent Incident Registry: Toward Preventing Repeated AI Agent Failures](http://arxiv.org/abs/2609.11030v1)
  <details><summary>📄 Abstract</summary>
  AI agents increasingly act through tools and delegated authority, but general incident repositories rarely capture the mechanisms needed to compare public failures with agent-security evaluations. We present the Agent Incident Registry (AIR), a source-linked catalog containing \N{} records of agent-related events disclosed from \Yfirst{} through \Ylast{}. Each record includes supporting evidence, a stable identifier, and missingness-aware labels for causal role, disclosure class, mechanism, and ...
  </details>

- **2026-09-10** — Kamran Ayoubi, Bernard Mans, Lata Narayanan — [Online Treasure Hunt in Vertex-Permuted Dynamic Rings](http://arxiv.org/abs/2609.11013v1)
  <details><summary>📄 Abstract</summary>
  We study the problem of treasure hunt by a group of $k \geq 1$ agents in vertex-permuted dynamic rings (VP). In this model, the $n$ vertices remain on a ring but are permuted at each time step. We first show that treasure hunt is impossible for any $k \leq n-3$ agents, if there are no restrictions on the sequence of permutations used in the dynamic ring. We then study the $VP(δ)$ setting, in which for every pair $i, j$ of vertices, the edge $(i, j)$ is guaranteed to appear within $δ$ steps. We s...
  </details>

- **2026-09-10** — Jiaming Zhong, Reza Valiollahi Mehrizi, Mohammad Pirani et al. — [Learning Agent-based Model Predictive Control for Holistic Vehicle Performance](http://arxiv.org/abs/2609.11871v1)
  <details><summary>📄 Abstract</summary>
  Agent-based model predictive control (AMPC) has recently been proposed as a distributed scheme that collaborates with all agents to achieve optimal holistic performance. However, its optimality highly depends on the prediction accuracy that requires all agents or their contributions to be known, which is too idealistic for actual implementation. This research proposes a novel practical hybrid control scheme - learning agent-based MPC (LAMPC), combining the model-based AMPC approach and data-base...
  </details>

- **2026-09-10** — Joshua W. Sin, David Ming Segura, Bojana Ranković et al. — [Dynamic language model representations for multi-objective reaction optimisation](http://arxiv.org/abs/2609.11790v1)
  <details><summary>📄 Abstract</summary>
  Optimising chemical reactions across multiple objectives, such as yield, selectivity, and safety, is central to chemical synthesis, and model-driven approaches depend critically on how reaction components are represented. Established featurisations are either chemically uninformative, as with one-hot encodings, or, as with molecular descriptors, do not readily extend across chemically distinct components. For structurally and functionally diverse components, it is therefore unclear what a shared...
  </details>

- **2026-09-10** — Chengzhu Huang, Yuqi Gu — [From Good Starts to Optimal Inference: Generalized Latent Factor Models with Missingness and Implicit Regularization](http://arxiv.org/abs/2609.11740v1)
  <details><summary>📄 Abstract</summary>
  Generalized latent factor models provide a flexible framework for analyzing high-dimensional non-Gaussian data, but principled estimation and uncertainty quantification under missingness remain substantially less developed. We develop a theory that connects a computationally tractable nonconvex procedure directly to statistical inference for nonlinear latent factor models with exponential-family links and partially observed entries. Our procedure combines a link-aware double-SVD initialization, ...
  </details>

- **2026-09-10** — Margaret Kostyrko, Yuxuan Xue, Garvita Tiwari et al. — [Revisiting Avatar-As-Image: High-Fidelity Registration is All You Need](http://arxiv.org/abs/2609.11722v1)
  <details><summary>📄 Abstract</summary>
  The representation of 3D clothed humans as standardized 2D UV texture and displacement maps over an underlying body model has long been studied. This compact representation is enticing as it enables pretrained image networks to process, generate, and edit 3D avatars, but is only useful if scans are accurately aligned and brought into correspondence via high-fidelity registration. This prerequisite has never been met, which we argue explains the limited quality of prior UV-based methods for cloth...
  </details>

- **2026-09-10** — Kesheng Chen, Yamin Hu, Wenjian Luo — [MAPLE: Memory-Augmented Planning with Language and Evolution](http://arxiv.org/abs/2609.11636v1)
  <details><summary>📄 Abstract</summary>
  Domain practitioners understand their business constraints but may lack operations-research expertise or dedicated support. LLM-based optimization agents translate natural-language requirements into models or solver programs that established optimization tools can execute. This progress makes optimization more accessible, but real-world operations are dynamic: changing demand, resources, and priorities require updates to data, constraints, and objectives. Methods centered on isolated requests of...
  </details>

- **2026-09-10** — Amir Rafe, Subasish Das — [Who Bears the Risk When Generative AI Enters Transport? A Distributional Sociotechnical Audit of Algorithmic Equity, Synthetic-Data Validity, and Public Trust](http://arxiv.org/abs/2609.11611v1)
  <details><summary>📄 Abstract</summary>
  Generative artificial intelligence is entering transportation through traveler-facing advisories, synthetic crash-record generation, and policy decision support. Existing governance frameworks lack transport-specific statistical tools to measure distributional risks across heterogeneous populations. We develop a Distributional Sociotechnical Audit (DSA) that integrates algorithmic equity, synthetic-data validity, and public-attitude heterogeneity into one empirical pipeline. The audit analyzes 5...
  </details>

- **2026-09-10** — Youngeun Nam, Joeun Kim, Hwanjun Song et al. — [TimelyRAG: Semantic-Temporal Hybrid Retrieval for Time-Critical Question Answering in Overlapping-Evolving Documents](http://arxiv.org/abs/2609.11572v1)
  <details><summary>📄 Abstract</summary>
  Although large language models (LLMs) and retrieval-augmented generation (RAG) have advanced open-domain question answering (QA), they remain unreliable when documents evolve through amendments. Existing time-sensitive retrieval methods address only the disjoint-evolving environment, where each update is an independent snapshot. However, laws, policies, and regulations often operate in overlapping-evolving environments, where amendments override earlier clauses while preserving most content, cre...
  </details>

- **2026-09-10** — Z. M. McIntyre, Daniel Loss — [One-clean-qubit spectroscopy of simulated Kitaev chains](http://arxiv.org/abs/2609.11513v1)
  <details><summary>📄 Abstract</summary>
  Spin qubits in gate-defined quantum dots provide a highly programmable platform for simulating condensed-matter phenomena. In this work, we introduce a digital-analog quantum simulation protocol for extracting the single-particle spectrum of a Kitaev chain. The Kitaev chain is mapped onto qubits via the standard Jordan-Wigner transformation and implemented as a drive-engineered, $N$-site transverse-field Ising model (TFIM) in a linear array of quantum dots. We show that periodically toggling the...
  </details>

- **2026-09-10** — Zhiqi Li, Yuxuan Liao, Bo Zhu — [Recursive Code World Models: Building Complex Worlds through Recursive Scene Programs](http://arxiv.org/abs/2609.11499v1)
  <details><summary>📄 Abstract</summary>
  Code world models represent worlds as executable programs, but this representation alone does not determine how to construct a complex world. We introduce Recursive Code World Models (RCWM), a framework for reconstructing complex 3D worlds in code from a single reference image. RCWM couples a Recursive Scene Program (RSP) representation with a construction solver that recursively calls itself. An RSP represents the executable world as compositional scene code, while each solver call follows the ...
  </details>

- **2026-09-10** — Jorge López-Varela, J. Ignacio Hidalgo, José-Manuel Muñoz et al. — [LLMs as Post-hoc Auditors of Physiological Plausibility in Symbolic Regression: A Clinician-Evaluated Case Study](http://arxiv.org/abs/2609.11431v1)
  <details><summary>📄 Abstract</summary>
  Genetic Programming and its variants, such as grammatical evolution, are widely used in Symbolic Regression to derive mathematical expressions from multivariate data. In addition to predictive accuracy, models are appreciated for their potential to provide interpretability, offering explicit equations that relate input variables to outcomes. However, achieving interpretability and plausibility remains challenging, as evolved models may be complex or scientifically inconsistent. In this study, we...
  </details>

- **2026-09-10** — Minghao Guo, Meng Cao, Sui Zhao et al. — [Mr.LHDR: A Benchmark for Multimodal Real-World Long-Horizon Deep Research Agents](http://arxiv.org/abs/2609.11318v1)
  <details><summary>📄 Abstract</summary>
  Deep research agents are increasingly capable of web search, tool use, multimodal evidence analysis, and information synthesis. However, existing benchmarks mainly evaluate medium-horizon exploration and rarely test whether agents can sustain long, dependency-heavy research processes. We introduce Mr.LHDR (Multimodal real-world Long-Horizon Deep Research), a benchmark for evaluating real-world deep research over long, irreducible chains of interdependent evidence across eight categories. Each qu...
  </details>

- **2026-09-10** — Jingbin Hu, Qirui Zhan, Yuang Cao et al. — [Preference Optimization with LALM Feedback for Continuous Autoregressive Non-Verbal Vocalization Generation](http://arxiv.org/abs/2609.11260v1)
  <details><summary>📄 Abstract</summary>
  We propose a preference optimization framework with Large Audio-Language Model (LALM) feedback for controllable non-verbal vocalization (NVV) generation in continuous autoregressive speech models. To construct preference data without human preference annotation, we build a bilingual prompt corpus by combining NVV-injected real transcripts with LLM-generated semantically aligned prompts, perform stochastic model rollouts, and use a LALM to rank candidate utterances and form same-prompt chosen--re...
  </details>

- **2026-09-10** — Antoine Saillenfest — [MUtE: A Dual Framework for Concept Erasure and Counterfactual Interventions](http://arxiv.org/abs/2609.11253v1)
  <details><summary>📄 Abstract</summary>
  Erasing concept-specific information from representations has been proven useful for mitigating bias or interpreting model decisions. The joint objective is to transform the original representations such that the target concept becomes unpredictable, while maximally preserving concept-unrelated information. In this work, we revisit the optimal bounds of concept erasure to derive a novel class of erasure functions that naturally induce a deterministic, dual counterfactual mapping. Bridging the ga...
  </details>

- **2026-09-10** — Bowen Zeng, Peipei Song, Weidong Chen et al. — [Multi-Faceted Evaluation and Mitigation of Emotion Hallucinations in MLLMs](http://arxiv.org/abs/2609.11154v1)
  <details><summary>📄 Abstract</summary>
  Multimodal large language models (MLLMs) have shown strong potential in open-ended emotion understanding, yet they often generate emotion hallucinations. Evaluating such hallucinations is particularly challenging for two reasons. First, emotion understanding spans multiple cognitive facets, from multimodal perception to psychological reasoning. Second, emotional interpretations are expressed in free-form language, making existing closed-ended protocols insufficient for evaluation. To address the...
  </details>

- **2026-09-10** — AS Aravinthkakshan, Laven Srivastava, Harsh Nandwani — [Same Day, Same Story; One Day Ahead, a Different Signal: The Dual Validity of Financial Sentiment](http://arxiv.org/abs/2609.11144v1)
  <details><summary>📄 Abstract</summary>
  Financial NLP has a standard workflow: validate a sentiment tool against human labels, then trust it to extract market signal. This assumes the two evaluations measure the same thing. We test that assumption in a setting where both can be measured at once: a corpus of securities class actions (2002-2025) linking 70,500 X messages to abnormal stock returns, with a single-annotator human labelled gold sample. Running five instruments (VADER, Loughran-McDonald, FinBERT, Twitter-RoBERTa, and an LLM ...
  </details>

- **2026-09-10** — Ken Chen, Maneesha Perera, Wei Wang et al. — [Bidirectional Multimodal Fusion of Sky Images and Time-Series for Solar Forecasting with Large Language Models](http://arxiv.org/abs/2609.11135v1)
  <details><summary>📄 Abstract</summary>
  Short-term photovoltaic (PV) power and global horizontal irradiance (GHI) forecasts are essential for effective dispatch, reserve scheduling, and grid operations. At these forecasting horizons, errors are predominantly driven by cloud induced ramps: relying solely on historical numerical data may struggle to anticipate an incoming cloud, making ground-based sky images a crucial complementary physical signal. Furthermore, forecast performance is highly sensitive to location and local observing co...
  </details>

- **2026-09-10** — Ziyu Zhang, Satoshi Nakamura — [Rubric-Aligned Disentangled Evaluation of Human Simultaneous Interpreting](http://arxiv.org/abs/2609.11131v1)
  <details><summary>📄 Abstract</summary>
  Human simultaneous interpreting (SI) is commonly assessed with analytic rubrics separating meaning transfer, delivery quality, and temporal synchrony, yet no automatic metric is designed for rubric-aligned segment-level SI evaluation. We construct a professionally annotated corpus of 1,101 SI segments with scores for meaning transfer (LQ), delivery quality (EXP), and perceived latency (LAT). We show that structured LLM prompting and scalar supervision collapse rubric dimensions, yielding near-ze...
  </details>

- **2026-09-10** — Koutian Wu, Junjie Zhou, Ergan Shang et al. — [Benchmark Radar: A Living Database and Search Engine for AI Benchmarks and Evaluation](http://arxiv.org/abs/2609.11115v1)
  <details><summary>📄 Abstract</summary>
  Benchmark researchers and developers of large language models (LLMs) and other AI systems need to find relevant evaluations, locate their benchmark datasets and code, and understand the settings behind reported scores. We present Benchmark Radar, a living database and search engine for retrieval and discovery of AI benchmarks, covering LLM evaluation, agentic and tool-use benchmarks, coding, reasoning, safety, and domain-specific evaluations. The system combines daily discovery of benchmark pape...
  </details>

- **2026-09-10** — Minjun Kim, Inho Won, Junghun Yuk et al. — [Distribution-aware Language Neuron Identification in Multilingual Large Language Models](http://arxiv.org/abs/2609.10993v1)
  <details><summary>📄 Abstract</summary>
  Multilingual large language models (mLLMs) contain a small fraction of feed-forward neurons that are sensitive to particular languages, commonly termed language-specific neurons. Existing work measures language specificity using the entropy of each neuron's language-wise probabilities of being active, where a neuron is considered active when its activation value is positive. However, this approach may not fully capture the multilingual nature of mLLMs, where language representations are distribu...
  </details>

- **2026-09-10** — Haseeb Mohammed Afsar — [What a Random Draw from the MCP Registry Contains, and What Tool-Use Benchmarks Contain Instead](http://arxiv.org/abs/2609.10962v1)
  <details><summary>📄 Abstract</summary>
  Studies of the Model Context Protocol (MCP) server ecosystem draw their samples in ways that quietly select for servers that work: reference sets, popularity lists, hand-curated frames, or pipelines that repair a server until it starts. We report what an unrepaired probability sample actually contains. From a 24,135-server registry census we draw 400 npm/stdio servers with a published seed and probe each one over the wire. Only 48.8% complete an initialize handshake, against 66.7% for a hand-cur...
  </details>

- **2026-09-10** — Luming Yang, Haoxian Liu, Siqing Li et al. — [Evaluating Scaffolding-Oriented Multi-Agent Large Language Model System for Clinical Interview Training](http://arxiv.org/abs/2609.10939v1)
  <details><summary>📄 Abstract</summary>
  Clinical education must prepare medical students to conduct safe and coherent patient interviews under conditions of uncertainty. Traditional standardized patient (SP) training is resource-intensive and difficult to scale. We developed a scaffolding-oriented multi-agent Large Language Model (LLM) AI Standardized Patient (AI-SP) training platform1. The system includes a patient agent for simulated dialog, a tutor agent providing Socratic prompts without disclosing diagnostic information, and a tu...
  </details>

- **2026-09-10** — Suwan Wu, Yumeng Lin, Pengcheng Yuan et al. — [SIRF: A Spec-Internalized Risk Foundation Model for Industrial Content Risk Control](http://arxiv.org/abs/2609.11752v1)
  <details><summary>📄 Abstract</summary>
  For industrial content risk control, the real deployment constraint is not average accuracy but how much risk can be auto-handled under high precision and second-level latency. We present SIRF (Spec-Internalized Risk Foundation Model), which internalizes a platform's complex policies, synthesized without additional human annotation via EntiGraph, MAGA rewriting and account-level chain-of-thought (CoT), into the weights via continued pretraining (CPT), so rules are applied at high precision under...
  </details>

- **2026-09-10** — Max Kiewiet, Stijn Cuyvers, Tom Reep et al. — [Heterogeneously Integrated Efficient and Widely Tunable Lasers at 795 nm for Rubidium-Based Quantum Technologies](http://arxiv.org/abs/2609.11585v1)
  <details><summary>📄 Abstract</summary>
  Scaling quantum processors and optical atomic clocks fundamentally requires orders-of-magnitude reductions in the size, weight, power, and cost of optical control systems. Photonic integration of lasers is critical to fulfill these requirements. At the near-infrared wavelengths required for atomic clocks and quantum computing through manipulation of rubidium atoms, laser integration is hindered by difficulty in light coupling and poor heat dissipation. Here, we introduce a wafer-scalable method ...
  </details>

- **2026-09-10** — Qianliang Wu, Haobo Jiang, Guangwei Gao et al. — [BridgeMatch: Conditional Transport Bridges in Matching Matrix Space for 3D Deformable Registration](http://arxiv.org/abs/2609.11472v1)
  <details><summary>📄 Abstract</summary>
  Reliable non-rigid point cloud correspondences are important for deformable anatomical registration, embodied perception and manipulation, and dynamic 3D reconstruction. Coarse-to-fine methods reduce computational cost by selecting the top-\(K\) coarse regions. However, this pruning may remove weak but correct hypotheses and restrict fine matching to an incomplete search space. We present \paper, a two-stage generative solver that maintains the complete soft matching matrix at both coarse and hi...
  </details>

- **2026-09-10** — Shengcheng Yu, Chunrong Fang, Zhenyu Chen — [Agent-Integrated Software: Interaction Contracts and Continuous Assurance](http://arxiv.org/abs/2609.11381v1)
  <details><summary>📄 Abstract</summary>
  Embedding an intelligent agent in an existing application creates a persistent coordination problem: users can revise goals and manipulate shared objects while delegated execution continues. We argue that dependable integration requires an explicit correspondence between task-level interaction and application behavior. We introduce Agent-Integrated Software (AIS) as a software pattern combining a conventional core, direct interaction, and a built-in agent, and Intent-Level Interaction Abstractio...
  </details>

- **2026-09-10** — Mohammad Dastranj, Jouni Mattila — [Modular Kinematic Reduction of Closed-Chain Mechanisms Using Path Assembly and Defect Homotopy](http://arxiv.org/abs/2609.11338v1)
  <details><summary>📄 Abstract</summary>
  Closed kinematic chains complicate modular modeling by coupling active and passive coordinates through nonlinear closure constraints. This paper presents a Path-Assembled Closure Differential Mapping (PACDM) framework for modular closure resolution and kinematic reduction. Each closure element compares two ordered transformation paths with common endpoints, with their mismatch expressed through the logarithm on SE(3) and the corresponding Jacobian assembled from local transformation derivatives....
  </details>

- **2026-09-10** — Junlin Liu, Chengwei Li, Yang Gao et al. — [DRG-MAPPO: Hierarchical Dynamic Role-Graph Multi-Agent Reinforcement Learning for Cooperative Air Combat](http://arxiv.org/abs/2609.11155v1)
  <details><summary>📄 Abstract</summary>
  Multi-Agent Reinforcement Learning (MARL) has emerged as a pivotal paradigm for complex decision-making in autonomous systems and air combat. While MARL has demonstrated significant potential in air combat, achieving sophisticated tactical coordination remains a non-trivial challenge. This difficulty is largely attributed to two primary limitations: (1) the absence of structured relational modeling hinders agents from capturing complex, time-varying interactions among battlefield entities; and (...
  </details>

- **2026-09-10** — Zihao Zheng, Baichuan Li, Junyi Yao et al. — [Engineering Reliable Commit Gates for Agentic AI: Cost-Aware Verification Portfolios under Common-Mode Data Failures](http://arxiv.org/abs/2609.10969v1)
  <details><summary>📄 Abstract</summary>
  Agentic systems commit state-changing actions, but additional verifiers can inherit the same upstream fault. We present VP-CONTROL, a runtime-assurance design and deterministic benchmark for cost-aware commit gates. Its 48 task templates yield 2,880 scenarios across six fault regimes. A fixed-call 2 x 2 experiment separates verifier-model diversity from evidence-source diversity. On frozen proposals from two local actor families, a cross-model vote over shared evidence approves 62.9% of unsafe p...
  </details>

- **2026-09-10** — Weitong Cai, Hang Zhang, Yukai Huang et al. — [Caption-once, Frames-on-Demand: Visual-Need Routing for Budget-Aware Agentic Long Video Understanding](http://arxiv.org/abs/2609.11899v1)
  <details><summary>📄 Abstract</summary>
  Long-video understanding on edge devices must reason over hours of content under tight compute and bandwidth budgets. Subsampling visual tokens loses temporal structure, while text-only video memories lose fine-grained visual attributes. We observe a visual-textual duality: language memories carry long-range temporal structure better than dense frames, while pixels remain decisive for attribute-level perception. Building on this insight, we propose Caption-once, Frames-onDemand (CFD), a budget-a...
  </details>

- **2026-09-10** — Zi-Rong Li, Si-Yang Liu, Tian-Zuo Wang et al. — [CausalArena: Benchmarking Causal Discovery in the Foundation Model Era](http://arxiv.org/abs/2609.11897v1)
  <details><summary>📄 Abstract</summary>
  Causal discovery aims to uncover causal structures from data and is fundamental to scientific reasoning and intervention-based decision making. Its evaluation relies heavily on structural causal models (SCMs), which specify a causal graph together with the mechanisms that generate data, yet existing studies differ substantially in graph families, mechanisms, and evaluation protocols. The emergence of causal discovery foundation models (CDFMs) further complicates evaluation: performance may refle...
  </details>

- **2026-09-10** — Rodion Krjutškov, Eduard Barbu, Nikos Sakkas et al. — [Explainability Assistant: A Conversational XAI Interface for Interpreting Energy Consumption Models](http://arxiv.org/abs/2609.11860v1)
  <details><summary>📄 Abstract</summary>
  Energy consumption forecasting relies on increasingly complex machine learning (ML) models, such as Genetic Programming-based symbolic regressors, whose predictions can be difficult for facility managers and building operators to interpret. Explainable Artificial Intelligence (XAI) techniques address this opacity, but traditional XAI dashboards require substantial technical expertise and provide limited flexibility for dynamic, context-aware inquiry. Conversational XAI systems offer a promising ...
  </details>

- **2026-09-10** — Nikolay Avramov, Hidde Lycklama, Alexander Viand et al. — [Atlas: Efficient Verifiable Semantic Search](http://arxiv.org/abs/2609.11841v1)
  <details><summary>📄 Abstract</summary>
  Semantic search is a core primitive of modern applications, powering recommender systems, web search, and retrieval-augmented generation for language models. The provider controls the index and query execution, leaving clients to trust that results come from the right algorithm over the intended index. A provider may truncate search to cut cost, bias results, or otherwise deviate from the specified execution undetected. Verifiability can remove this trust assumption by proving that results follo...
  </details>

- **2026-09-10** — Jordi Luque, Lorenzo Concina, Marco Matassoni et al. — [The Eloquence submission for Task 2 of the Interspeech 2026 MLC-SLM challenge](http://arxiv.org/abs/2609.11724v1)
  <details><summary>📄 Abstract</summary>
  This paper details the Eloquence team's approach to Task 2 of the 2nd MLC-SLM challenge at Interspeech 2026, which involves multilingual Multiple-Choice Question Answering (MCQA) across 21 languages. Three approaches are explored. First, we fine-tune Voxtral-Mini-3B via LoRA with cross-lingual data augmentation, ASR transcript augmentation and timestamp-aware audio cropping, achieving 0.72 macro-accuracy on evaluation Phase 2. Second, we apply multimodal in-context learning (ICL) to the frozen V...
  </details>

- **2026-09-10** — Yunzhong Lou, Yusheng Luo, Jiahao Li et al. — [Language-Augmented Semantic Priors for B-Spline Surface Fitting](http://arxiv.org/abs/2609.11708v1)
  <details><summary>📄 Abstract</summary>
  The use of B-splines and Non-Uniform Rational B-Splines surfaces constitutes the mathematical foundation of contemporary computer-aided design (CAD) systems. Despite long-term progress, geometric kernels in traditional CAD still rely heavily on predetermined heuristic initialization for surface fitting and parameterization. Meanwhile, the procedural semantics and design intent encoded in modeling histories are largely ignored during geometry generation. This disconnect creates a gap between high...
  </details>

- **2026-09-10** — Zhenwei Liu, Yang Liu, Michel Destrade et al. — [Impact waves in soft bilayer tissues](http://arxiv.org/abs/2609.11705v1)
  <details><summary>📄 Abstract</summary>
  In this study, we investigate impact-wave propagation in a pre-stressed compressible hyperelastic bilayer resting on a frictionless rigid substrate within the framework of nonlinear elasticity. Semi-analytical solutions for the transient displacement fields induced by localized surface impulses are derived using the Fourier-Laplace transform, and their long-time asymptotic behavior is obtained through the method of stationary phase. Finite element simulations are further performed to validate th...
  </details>

- **2026-09-10** — Jihoon Kwon, Lawrence Liu, Daekyung Park et al. — [Making Alternative Data Work: Context-Augmented LLMs for Financial Forecasting](http://arxiv.org/abs/2609.11607v1)
  <details><summary>📄 Abstract</summary>
  When forecasting a firm's future financial performance, alternative data - data collected from non-traditional sources such as consumer transactions, web traffic, and prediction markets - can provide timely signals about firms' operating activities and broader market conditions. These signals may reveal information that is not captured by traditional public sources and can therefore provide complementary information for forecasting firms' future financial performance. However, firm-level alterna...
  </details>

- **2026-09-10** — Aleksandra Urman, Elsa Lichtenegger, Salima Jaoua et al. — [Prompt Revision as a Source of Cultural Bias in Text-to-Image Systems](http://arxiv.org/abs/2609.11532v1)
  <details><summary>📄 Abstract</summary>
  Commercial text-to-image systems silently revise user prompts before generating images, a step users typically cannot disable or even see. Yet, existing audits of cultural bias examine only the final images and treat generation as a single pipeline, so they cannot tell where the bias originates. We introduce WORLDVIEW, a multilingual benchmark of 8,960 prompts across 15 languages and 31 language-context pairings. Using it, we audit the revision layer in three systems (DALL-E-3, Imagen-4, GPT-Ima...
  </details>

- **2026-09-10** — Dmitry Karamzin, Aleksandra Zhukova, Roman Chertovskih et al. — [Time-optimal elevator control with higher-order state constraints: analysis and computation of boundary contacts](http://arxiv.org/abs/2609.11348v1)
  <details><summary>📄 Abstract</summary>
  In this paper, we consider the classical time-optimal elevator problem in the presence of higher-order state constraints. The main contribution is a constructive indirect solution framework based on a Pontryagin Maximum Principle specifically formulated for higher-order constrained systems. First, we derive specialized optimality conditions and analyze the resulting structure of extremal trajectories. Second, we show that the infinite-dimensional optimal control problem can be transformed into a...
  </details>

- **2026-09-10** — Xudong Zhu, Junhong Li, Lixin He — [Interface-Controlled Phase Stability in Polymorphic HfO$_2$ Revealed by Machine-Learning Atomistic Simulations](http://arxiv.org/abs/2609.11307v1)
  <details><summary>📄 Abstract</summary>
  HfO$_2$ exhibits rich polymorphism, and competition among different phases underpins many of its functional properties. Yet bulk free-energy relations alone cannot explain phase selection at mixed-phase boundaries, where interface orientation and structural continuity constrain collective rearrangements. Here, using machine-learning atomistic simulations and a Hf-centered local phase classification scheme, we show that crystallographic interface matching redirects phase competition and accessibl...
  </details>

- **2026-09-10** — Shun Kotoku, Rodrigo Martínez-Peña, Takatomo Mihana et al. — [Reconstructing the information processing capacity of physical systems from noisy observations](http://arxiv.org/abs/2609.11268v1)
  <details><summary>📄 Abstract</summary>
  Driven dynamical systems can compute when their transient states encode complex transformations of past inputs. The information processing capacity (IPC) framework allows for a detailed accounting of these computational properties, however its interpretation in noisy systems has remained incomplete. In this work, we clarify how noise affects the IPC and how one can reconstruct the noiseless IPC. First, we show how to distinguish the dynamics of an unperturbed system from the noise-free component...
  </details>

- **2026-09-10** — Thomas Caussade, David P. Hewett — [A note on the convergence analysis of Laguerre approximations for analytic functions](http://arxiv.org/abs/2609.11259v1)
  <details><summary>📄 Abstract</summary>
  In a recent paper (H. Wang, Math. Comp. 93, 2861-2884, 2024), Wang has presented a number of results concerning the convergence of approximations based on generalised Laguerre polynomials, claiming to have provided "the first rigorous proof of root-exponential convergence of Laguerre approximations for analytic functions". In this note we argue that the proofs of the main results of Wang's paper are incomplete, because they rely on taking a limit under an integral sign, and this is not properly ...
  </details>

- **2026-09-10** — Jia-Hung Chen, Yi-Cheng Lin, Kai-Wei Chang et al. — [AudioICL-Bench: A Benchmark for Large Audio Language Model In-Context Learning](http://arxiv.org/abs/2609.11252v1)
  <details><summary>📄 Abstract</summary>
  In-context learning (ICL) promises training-free adaptation for audio, where labeling every new condition is costly. Yet existing audio ICL studies largely measure Task Recognition, where demonstrations merely cue pre-trained capabilities, rather than Task Learning, where a genuinely new input-label mapping must be inferred from demonstrations alone. We introduce AudioICL-Bench, a diagnostic benchmark whose per-episode rules are resampled so that no correct answer is recoverable from prior knowl...
  </details>

- **2026-09-10** — Jiayu Huang, Zichen Tang, Qianhui Ling et al. — [Can LLMs Follow Medical Expert Logic? A Benchmark for Hierarchical Logical Consistency in Risk-of-Bias Assessment](http://arxiv.org/abs/2609.11185v1)
  <details><summary>📄 Abstract</summary>
  Evidence-based medicine demands strict logical consistency, yet current evaluations of large language models (LLMs) prioritize superficial label matching over genuine reasoning. We introduce LogiMed-RoB, a benchmark grounded in Cochrane Risk of Bias (RoB) 2.0 expert logic, comprising 860 randomized controlled trials (RCTs) and 14,820 queries. It evaluates models under the Hierarchical Logical Consistency (HLC) framework across four dimensions: Atomic Consistency, Domain Consistency, Aggregation ...
  </details>

- **2026-09-10** — Rajarshi Chowdhury — [terms.txt: A Consent and Compensation Protocol for Agentic Web Access](http://arxiv.org/abs/2609.11152v1)
  <details><summary>📄 Abstract</summary>
  The open web ran on an unwritten bargain: sites admitted crawlers, and search engines sent visitors back. Public measurements show that bargain breaking under AI crawlers and agents. Automated clients now make up most requests, training dominates Cloudflare-classified crawling, and the largest AI platforms fetch thousands of pages for each visitor they return. The web's common control, robots.txt, cannot express identity, purpose, terms, or price, can be circumvented, and newer alternatives are ...
  </details>

- **2026-09-10** — Dong Li, Sixuan Mi, Zihao Ye et al. — [Autonomous Chemical Mechanistic Discovery through Agentic Reasoning and Validation](http://arxiv.org/abs/2609.11147v1)
  <details><summary>📄 Abstract</summary>
  Unraveling reaction mechanisms is central to modern chemistry, yet automating these investigations remains challenging because computational workflows still rely heavily on expert intervention. Here we introduce ARCHE, an autonomous agentic system that integrates a general-purpose reasoning model, a domain-specialized computational chemistry model, and a structured tool registry to transform mechanistic inquiry into a scalable, self-validating process. ARCHE interprets scientific questions, gene...
  </details>

- **2026-09-10** — Zesheng Wei, Mengfan Li, Wenhao Liu et al. — [ProMediConv: Benchmarking Proactive Conversational Agents in Legal Dispute Mediation](http://arxiv.org/abs/2609.11101v1)
  <details><summary>📄 Abstract</summary>
  Dispute mediation is essential for maintaining social harmony and resilience, yet developing skilled mediators is costly and time-consuming. Existing LLM-based mediation research remains limited by unrealistic task formulations, low-fidelity datasets, and coarse evaluation metrics that obscure turn-by-turn dynamics. To address these gaps, we introduce ProMediConv, a novel benchmarking framework that models mediation as a proactive, multi-stage, and party-aware dialogue process incorporating 11 m...
  </details>

- **2026-09-10** — Sourajit Saha, Shubhashis Roy Dipta, Nobin Sarwar et al. — [New Evidence, Same Choice: Testing Physical Experiment Selection in Vision Language Models](http://arxiv.org/abs/2609.11022v1)
  <details><summary>📄 Abstract</summary>
  A model first sees an image from one physical measurement experiment, such as how far a block coasted, and must answer a question about a new trial, such as whether the block will pass a target after a fixed push. The initial experiment may provide enough information to answer, or the model may need another measurement, such as the object's mass, friction, restitution, or spring stiffness. We study whether vision language models can decide when to answer immediately and, when more evidence is ne...
  </details>

- **2026-09-10** — Shota Horiguchi, Marc Delcroix, Naohiro Tawara et al. — [Diarization Error Decomposition Under Pause Annotation Ambiguity](http://arxiv.org/abs/2609.11007v1)
  <details><summary>📄 Abstract</summary>
  Speaker diarization evaluation is sensitive to ambiguity in pause annotation, which can inflate diarization error rate (DER) or obscure genuine model errors. We show that morphological closing, which has been used for pause-tolerant diarization evaluation, discards segment-level distinctions. Instead, we propose an exact, overlap-aware decomposition of standard DER into a pause-attributable component, consisting of errors compatible with pause filling, and a residual core component that can serv...
  </details>

- **2026-09-10** — Haolong Li, Zehan Lin, Huahua Miao et al. — [MMS Allocation for Chores with Online Agent Arrivals](http://arxiv.org/abs/2609.10960v1)
  <details><summary>📄 Abstract</summary>
  We study the fair allocation of $m$ indivisible chores to $n$ agents with subadditive cost functions arriving online in an arbitrary order. Upon an agent's arrival, we are informed of her cost function and must irrevocably assign her a set of chores. We focus on the Maximin Share (MMS) fairness notion and aim to compute an allocation in which all items are assigned, and no agent incurs a cost more than $α$ times her MMS.   Without any prior information about the instance (other than $n$ and $m$)...
  </details>

- **2026-09-10** — Hsiao-Ying Lu, Dongyu Liu, Kwan-Liu Ma — [Structurally Speaking: Motif-Oriented Graph Captioning through Bidirectional Graph-Text Translation](http://arxiv.org/abs/2609.10923v1)
  <details><summary>📄 Abstract</summary>
  Graph captions should help readers understand graph structure, rather than simply translate adjacency matrices into long textual edge lists. A useful graph caption abstracts connectivity into recognizable motifs, such as hubs, paths, cycles, cliques, and bridges, because these motifs provide compact structural units that are easier to read, compare, and recover. In this paper, we study motif-oriented graph captioning as a bidirectional graph-text translation task, where captions must both preser...
  </details>

- **2026-09-09** — Yizhan Li, Jianxin You, Mengyang Xiong et al. — [ReactHuman: A Physics-Grounded Benchmark for Human-Like Reactive Decision-Making in Embodied Multimodal LLMs](http://arxiv.org/abs/2609.10895v1)
  <details><summary>📄 Abstract</summary>
  Reacting to sudden physical hazards (catching a slipping plate, dodging a falling knife) is both a meaningful test of embodied intelligence and a hard requirement for deploying multimodal large language models (MLLMs) as the decision coreof household robots. Existing evaluations, however, probe intuitive physics passively through question answering over videos, or target deliberate, long-horizon tasks such as navigation and rearrangement; none measure whether a model can turn physical understand...
  </details>

- **2026-09-09** — Kunal Jha, Francesco Cicala, Blaise Agüera y Arcas et al. — [Tapes Together Strong: The Co-evolution of Computation and Cooperation](http://arxiv.org/abs/2609.10817v1)
  <details><summary>📄 Abstract</summary>
  How does cooperation evolve in complex agentic systems? Prior work in evolutionary game theory studies why individuals are incentivized to cooperate by isolating social interactions from the physical costs of behavior, while artificial life models traditionally study emergent self-replication without formalizing the dilemma between acquiring resources and preserving the shared energy needed to reproduce. In contrast, we introduce Autopoietic Game Theory, a computational model where social intera...
  </details>

- **2026-09-09** — Karish Gupta, Matthew Alex, Alex Li et al. — [BodyCam-VQA: Enhanced Body-Worn Camera Video Captioning via Multimodal Reasoning and Probe Question Generation](http://arxiv.org/abs/2609.10815v1)
  <details><summary>📄 Abstract</summary>
  Police body-worn camera (BWC) footage has emerged as a critical aspect of law enforcement that ensures legal transparency, officer accountability, and the protection of civil rights. However, effectively processing this data remains a significant challenge due to its multimodal video format. BWC videos, in many cases, comprise chaotic scenes with low visual quality, rapid movement/interactions, and high-noise audio that make visual understanding a challenge for even SOTA multimodal models. Curre...
  </details>

- **2026-09-09** — Yingfan Xu, Tieming Liu, Ye Liang — [DR-LabStack: Design and Implementation of a Clinician-Facing Web System for Diabetic Retinopathy Prediction](http://arxiv.org/abs/2609.10796v1)
  <details><summary>📄 Abstract</summary>
  Pretrained diabetic retinopathy (DR) prediction models differ in their input fields, serialization formats, preprocessing requirements, and output semantics. Making these models accessible through a common clinical interface therefore requires explicit coordination between the user interface and the inference service. We designed and implemented DR-LabStack, a React-Flask web system integrating four externally developed pretrained models: RuleFit, Pruned RuleFit, Elaborative XGBoost, and Two-lev...
  </details>

- **2026-09-09** — Yuanchen Bai, Zijian Ding, Angelique Taylor — [Finishing the Task Is Not Enough: Evaluating Agent Resilience and Considerate Participation under Accumulating Challenge](http://arxiv.org/abs/2609.10724v1)
  <details><summary>📄 Abstract</summary>
  Sustained deployment of generative AI agents requires more than isolated task success. Agents must remain useful across repeated interactions, changing conditions, and dependencies on people within shared workflows, especially as technical, human, and operational disruptions accumulate over time. We propose operational resilience and considerate participation as two complementary aspects of evaluating such agents: the former captures how agents recover from blocked work while preserving progress...
  </details>

- **2026-09-09** — The Intern-NCP Team,  :, Jiaqi Cao et al. — [NCP-ArchPreview Technical Report: Moving towards Latent Space Language Models through Next Concept Prediction](http://arxiv.org/abs/2609.10715v1)
  <details><summary>📄 Abstract</summary>
  We introduce NCP-ArchPreview, a latent-space language model that pushes autoregressive pretraining beyond standard next-token prediction (NTP). Alongside NTP, the model learns through Next Concept Prediction (NCP) to predict discrete concepts that span multiple tokens, introducing an explicit and more challenging concept-level objective while preserving standard token-level autoregressive generation. NCP-ArchPreview builds a latent space by constructing a product-quantized concept vocabulary dir...
  </details>

- **2026-09-09** — Deblina Kar — [A Multi-Stage Rule-Chaining Framework for Compositional and Interpretable Cognitive Reasoning](http://arxiv.org/abs/2609.10654v1)
  <details><summary>📄 Abstract</summary>
  The Abstraction and Reasoning Corpus (ARC) benchmarks cognitive generalization, the ability to infer and apply abstract rules from limited examples. This paper presents a multi-stage rule-chaining framework that performs compositional reasoning across symbolic, structural, and conceptual levels. The framework integrates three complementary solvers:   (1) a deterministic rule discovery module that induces atomic transformations through geometric, color, and object-based analysis;   (2) a pattern-...
  </details>

- **2026-09-09** — Hsuan Lo — [Following the Preference, Missing the Optimum: Compliance Without Optimization in AI Housing Recommendation](http://arxiv.org/abs/2609.10856v1)
  <details><summary>📄 Abstract</summary>
  Large language models are becoming the first point of contact for consumer search in domains where the stakes are material and the law is explicit. Existing audits show that models steer housing seekers by perceived identity, but none can say what a user loses when a recommender overlooks a suitable option, for want of an enumerated inventory to score omissions against. We audit AI housing recommendation against a verifiable ground truth. For each of 150 synthetic renter scenarios in New York Ci...
  </details>

- **2026-09-09** — Alkesh K. Srivastava, Aamodh Suresh, Carlos Nieto-Granda et al. — [When Information is Worth the Risk: Behavioral Valuation for Hazardous Robotic Exploration](http://arxiv.org/abs/2609.10726v1)
  <details><summary>📄 Abstract</summary>
  Hazardous robotic exploration requires robots to map spatial risks, such as unsafe terrain, radiation, fire, mines, or structural damage, while operating where collecting information can itself cause failure. A highly informative path may expose the robot to hazards, terminate execution, and prevent future observations. Hazardous exploration therefore requires deciding not only where uncertainty is largest, but when reducing it is worth the risk. This paper introduces a valuation-layer view of t...
  </details>

- **2026-09-09** — Jiacheng Sang, Mengyuan Li, Sanxing Chen et al. — [SearchAtlas: Analyzing Agentic Search Strategies via Evidential Query Graphs](http://arxiv.org/abs/2609.10901v1)
  <details><summary>📄 Abstract</summary>
  LLM search agents are often evaluated on final-answer accuracy, overlooking the process. Analyzing a search strategy requires understanding how credible evidence is retrieved to address question constraints. This valuable information is buried in raw search trajectories that are long and difficult to parse. We introduce SearchAtlas, a framework that converts search trajectories into structured graphs whose edges represent how evidence is propagated across the reasoning trace, from the query that...
  </details>

- **2026-09-09** — Qin Xie — [Alternative AI Philosophy: Daoism as Method for AI in Education](http://arxiv.org/abs/2609.10842v1)
  <details><summary>📄 Abstract</summary>
  As artificial intelligence (AI) rapidly iterates and transforms teaching, learning, and knowledge production, philosophical reflection has become increasingly indispensable to educational debates that remain predominantly shaped by Western intellectual traditions. This article proposes Daoism as an alternative philosophical framework for reimagining AI in education. Through philosophical analysis and textual interpretation of classical Daoist sources, brought into dialogue with contemporary scho...
  </details>

- **2026-09-09** — Jiankun Wei, Ewan Dunbar, Gerald Penn — [Sparse Weight and Edge Circuit Discovery in Transformer-based Acoustic Models](http://arxiv.org/abs/2609.10645v1)
  <details><summary>📄 Abstract</summary>
  Transformer-based foundation models are powerful but opaque, motivating Mechanistic Interpretation methods to uncover the black-box by identifying small computation subgraphs responsible for a task. DiscoGP is a joint weight-and-edge circuit discovery framework originally developed for text decoders. We extend DiscoGP to speech encoders and present, to our knowledge, the first circuit discovery study for modern speech foundation models. Across HuBERT and Wav2Vec 2.0 on several speech classificat...
  </details>

- **2026-09-09** — Yiling Zhou, Yilin Wang, Jianmin Wang et al. — [ADMET-EvO: a self-evolving scientific agent for sustained research across heterogeneous tasks](http://arxiv.org/abs/2609.10121v2)
  <details><summary>📄 Abstract</summary>
  Scientific agents can move beyond automated model building by using accumulated evidence to revise both their questions and experimental strategies. The challenge is sustaining this adaptation across heterogeneous tasks without overfitting decisions to internal validation. Absorption, distribution, metabolism, excretion and toxicity (ADMET) prediction provides a demanding setting across diverse assays, datasets and chemical domains. We therefore developed ADMET-EvO, an evidence-gated agent that ...
  </details>

- **2026-09-09** — Remco Hendriks — [MetroLLM-Bench: Evaluating Language Models as Transit Kiosk Runtimes](http://arxiv.org/abs/2609.10016v1)
  <details><summary>📄 Abstract</summary>
  We introduce MetroLLM-Bench, a 955-case benchmark for testing language models as the policy layer of a transit kiosk. It covers six real metro systems, ranging from 37 to 414 stations, and eleven categories that include routing, fare calculation, disruptions, accessibility, and adversarial input. In each case, the model must call structured tools and submit a machine-renderable terminal state containing an outcome, a per-ticket fare quote when applicable, and a kiosk action. Fourteen determinist...
  </details>

- **2026-09-09** — Benjamin Gruenbaum, Doron Porat, Assaf Natanzon et al. — [The Era by Eon Benchmark: A Generated Enterprise Estate with Exact Ground Truth for Benchmarking LLM Agents](http://arxiv.org/abs/2609.09853v1)
  <details><summary>📄 Abstract</summary>
  LLM agents for enterprise systems of record cannot be evaluated on customer production data, and no existing substitute provides ground truth. We present the Era by Eon Benchmark for evaluating LLM agents that use enterprise tools. The benchmark is built around a complete fictional company. It includes product simulators, company-specific internal databases, benchmark questions, and computed answer keys. Industry, company size, business model, application portfolio, and a seed define each compan...
  </details>

- **2026-09-09** — Jing Chen, Jin Dong, Jichen Li et al. — [Scalable Composition of Byzantine Agreements under Reorder Attacks](http://arxiv.org/abs/2609.09623v1)
  <details><summary>📄 Abstract</summary>
  Byzantine agreement (BA) is a foundational building block in distributed systems, and the security analysis of BA protocols under multi-instance executions has attracted increasing attention. However, most existing adversary models focus solely on party corruption and neglect important threats posed by adversarial manipulations of communication channels in the network. Through channel attacks, messages can be reordered across multiple executions and lead to violations of the protocol's security ...
  </details>

- **2026-09-09** — Sales G. Aribe, Louie Jay S. Labastida — [The Vibe Shift in Software Engineering: Evaluating AI-Led Conversational Programming for Performance, Cognition, and Responsible Adoption](http://arxiv.org/abs/2609.09560v1)
  <details><summary>📄 Abstract</summary>
  This study evaluates Vibe Coding, an emerging AI-led conversational programming paradigm that enables developers to generate software through natural-language interaction with large language models. Using a mixed-methods design, the study assessed performance efficiency, cognitive implications, and responsible adoption in comparison with traditional and AI-assisted coding environments. Thirty participants, including professional developers and advanced computing students, completed equivalent pr...
  </details>

- **2026-09-09** — Athanasios Tragakis, Marco Aversa, Daniela Ivanova et al. — [SceneHI: High-Resolution 3D-Consistent Scene Texturing with Controllable Illumination](http://arxiv.org/abs/2609.10363v1)
  <details><summary>📄 Abstract</summary>
  SceneHI is a framework that lifts high-resolution, illumination-aware priors from 2D diffusion models to perform 3D texture synthesis. It is the first to demonstrate that high-resolution textures, previously limited to 2D synthesis, can be generated directly on 3D objects without model fine-tuning or optimization. Designed for complex, multi-object environments, SceneHI uniquely combines 3D-consistency, high-resolution fidelity, and physically plausible baked shadows within a single generative p...
  </details>

- **2026-09-09** — Milan Liessens Dujardin, Song-Ze Yu, Kevin Miao — [Unifying Score and Performance for Fine-Grained Music Understanding in Audio-Language Models](http://arxiv.org/abs/2609.10351v1)
  <details><summary>📄 Abstract</summary>
  Large audio language models (LALMs) have shown promising progress in broad music-understanding tasks such as tagging, retrieval, and captioning. Music understanding that requires finer hearing over both the content and how it is realized within a performance through dynamics, phrasing, articulation, time, and other performance techniques, however, remains at an earlier stage. Existing audio-language model (ALM) training pipelines typically rely on coarse, weakly grounded captions and therefore p...
  </details>

- **2026-09-09** — Samed Doğan, Nico Leuze, Alfred Schöttl — [Geometry Without Coordinates: LiDAR Diffusion as a 3D Feature Bridge](http://arxiv.org/abs/2609.10322v1)
  <details><summary>📄 Abstract</summary>
  Transferring the rich priors of large 2D foundation models to sparse 3D LiDAR remains challenging, as training native 3D foundation models at comparable scale is limited by data and annotation scarcity. We introduce a LiDAR-conditioned diffusion model trained on pseudo-labels from off-the-shelf 2D foundation models. The model supports multiple output modalities, including depth, semantic segmentation and instance prediction, selectable via a textual task prompt. Because the model is conditioned ...
  </details>

- **2026-09-09** — Leilei Ding, Shumin Wang, Yuting Huang et al. — [$Φ$-Bench: Can Large Language Models Engineer the Infrastructure That Powers Them?](http://arxiv.org/abs/2609.10226v1)
  <details><summary>📄 Abstract</summary>
  Large language models (LLMs) have demonstrated remarkable capabilities in reasoning and code generation, raising the prospect that they could assist in developing and optimizing the very infrastructure that powers them. However, existing benchmarks mainly focus on isolated kernels, predefined operators, or pre-specified optimization targets, and therefore fail to evaluate the ability of LLMs to perform open-ended, long-horizon LLM infrastructure engineering. To address this gap, we present $Φ$-B...
  </details>

- **2026-09-09** — Sharjeel Imtiaz, Uljana Reinsalu, Tara Ghasempouri — [AutoTrans: AI-Assisted Automatic Translation of Security Assertions for RISC-V Processors](http://arxiv.org/abs/2609.10057v1)
  <details><summary>📄 Abstract</summary>
  Reusing a set of verified security assertions across RISC-V processor targets remains one of the most expensive bottlenecks in hardware security verification. Manual translation takes hours per assertion. Raw LLM translation is fast but unreliable, introducing signal hallucination, where the model invents port names absent from the target RTL and produces outputs that may vary across model updates or even within the same model version. This paper presents AutoTrans, an automated framework that a...
  </details>

- **2026-09-09** — Jie Song, Zhichuan Xu, Ziyu Lu et al. — [OntologyAligner: Ontology-Aligned Retrieval and Hierarchy-Guided Large Language Model Reranking for Biomedical Ontology Normalization](http://arxiv.org/abs/2609.10055v1)
  <details><summary>📄 Abstract</summary>
  Biomedical ontology normalization maps free-text expressions to standardized concepts, enabling consistent integration and analysis of biomedical data. This task remains challenging because lexical variation and subtle distinctions among hierarchically related concepts can obscure concept boundaries. We present OntologyAligner, a three-stage framework that combines ontology-aligned retrieval, large language model candidate reranking, and selective hierarchy-guided refinement. We also construct P...
  </details>

- **2026-09-09** — Junwon Ko, Dong-Jae Lee, Minchan Kwon et al. — [Direct Diversity Optimization for Diverse Successful Trajectories in Preference Post-Training](http://arxiv.org/abs/2609.10052v1)
  <details><summary>📄 Abstract</summary>
  LLM agents for sequential decision tasks are often post-trained with trajectory-level outcome labels, but such labels provide little supervision for preserving multiple successful branches from the same decision state. We study this problem as successful strategy coverage: how broadly a model realizes distinct successful strategies under a fixed rollout budget. We present Direct Diversity Optimization (DDO), an offline post-training method that combines Divergence-Tree Collection (DTC) with the ...
  </details>

- **2026-09-09** — Md Mahir Jawad, Galib Mahmud Jim, Rafid Ahmed et al. — [5-Dialects-BN: Unmasking the Impact of Transliteration on Bangla Dialectal LLMs](http://arxiv.org/abs/2609.09964v1)
  <details><summary>📄 Abstract</summary>
  Large Language Models (LLMs) have achieved remarkable progress across natural language processing (NLP) tasks, yet their capabilities degrade sharply for low-resource languages and dialectally diverse settings. Bangla, the world's sixth most spoken language, exemplifies this gap: existing resources overwhelmingly target Standard Bangla, leaving its regional dialects without the benchmarks needed to develop or evaluate dialect-aware systems. We address this gap with 5-Dialects-BN, the first multi...
  </details>

- **2026-09-09** — Tianzhu Zhang, Weichen Tao, Changgang Zheng et al. — [Can AI Agents Detect and Repair Artifact Drift in Network Experiments?](http://arxiv.org/abs/2609.09849v1)
  <details><summary>📄 Abstract</summary>
  In recent years, AI agents have evolved into capable assistants that carry out multi-step tasks in digital environments. The network systems community is beginning to explore these capabilities in operational and experimental settings. However, an agent operating in network systems should not be judged solely by whether it completes the immediate task. The experiment record it modifies must also remain trustworthy. We call this property artifact integrity: the record's claims must remain support...
  </details>

- **2026-09-09** — Friedrich Wiemer, Florian Wagner — [Lightweight Zero Trust via Automotive SDN](http://arxiv.org/abs/2609.09817v1)
  <details><summary>📄 Abstract</summary>
  Zonal in-vehicle networks ship Ethernet, MACsec, and TSN, but treat the network itself as trusted: once configured at the factory, there is no standardized runtime way to easily revoke access, rotate keys, or contain a compromised ECU. Zero Trust Architecture targets exactly that gap, yet existing automotive ZTA proposals bolt on dedicated infrastructure that duplicates the SDN management plane already required to enable SDVs. Thus, ZTA is not yet adopted in the automotive domain, and the questi...
  </details>

- **2026-09-09** — Yanze Cao — [Procedural Memory Under Change: Reuse and Interference in Controlled Web Tasks](http://arxiv.org/abs/2609.09774v1)
  <details><summary>📄 Abstract</summary>
  Procedural memory lets language agents reuse successful routines, but reuse presumes that a stored routine remains applicable. We study what happens when that presumption is deliberately violated. The study combines a retrospective, human-assisted interface-adaptation case from BrowserGym TimeWarp with controlled frozen-memory comparisons on synthetic shopping decisions. During the documented WebShop V1-V6 development path, interface-specific code was adapted while the separately stored high-lev...
  </details>

- **2026-09-09** — Jianing Wang, Xintao Wang, Aili Chen et al. — [SocialRL: Refining LLMs' Social Intelligence through Multi-turn Reinforcement Learning and Reward Design](http://arxiv.org/abs/2609.09764v1)
  <details><summary>📄 Abstract</summary>
  Social intelligence enables agents to read social context, infer intent, and adapt over sustained dialogue. As language models become autonomous collaborators, it is central to building effective and trustworthy human-AI interaction. Existing reinforcement learning methods optimize single-turn utterances and sparse outcome rewards, producing short-sighted policies that struggle to manage goal-relationship tensions across multi-turn interactions. We propose SocialRL, a multi-turn reinforcement le...
  </details>

- **2026-09-09** — Zhichao Hou, Lingdao Sha, Xueyu Mao et al. — [TEFM: Token-Efficient Faithful Modeling for Structured Data](http://arxiv.org/abs/2609.09552v1)
  <details><summary>📄 Abstract</summary>
  In this paper, we solve two fundamental obstacles in applying LLMs to critical domains: token efficiency and faithfulness. To address both constraints jointly, we present TEFM (Token-Efficient Faithful Modeling), a framework designed for structured data analysis in critical domains. TEFM achieves token efficiency by compressing lengthy structured observations into compact Behavioral Code tokens, dramatically reducing token consumption with minimal information loss. Moreover, TEFM enables faithfu...
  </details>

- **2026-09-09** — Henry Ascencio Trejo, Roel Pieters, Gokhan Alcan — [Adaptive Shared Control with Online Bounded-Rational Human Behavior Estimation](http://arxiv.org/abs/2609.10215v1)
  <details><summary>📄 Abstract</summary>
  This work considers adaptive shared human-robot control for nonlinear control-affine systems, where the assumption of a fully rational human is relaxed and the robot adapts its assistance to observed boundedly rational human behavior. We use a level-k bounded-rationality model of the two-player game to construct a finite bank of candidate human and robot policies through alternating best-response computations, with the associated value functions and policies approximated using adaptive dynamic p...
  </details>

- **2026-09-09** — M. Yunus Seker, Shobhit Aggarwal, Ruwan Wickramarachchi et al. — [GTA-2: A Multi-VLM Framework for Synthesizing Robot Manipulation Skills via Grounded Task Axes](http://arxiv.org/abs/2609.09808v1)
  <details><summary>📄 Abstract</summary>
  Robotic manipulation tasks are often decomposed into behaviors or skills. However, one often needs to predefine these behaviors for specific tasks or try to cover a wide range of tasks using generic skills. As a result, these behaviors can remain too coarse to expose the geometric, control, and scene-dependent decisions required for execution. We introduce Grounded Task Axes v2 (GTA-2), a modular multi-VLM framework that constructs executable, task-bespoke manipulation skills from reusable objec...
  </details>

- **2026-09-09** — Yanpeng Hu, Yiwei Yang, Yuanwu Zhu et al. — [HBFSim: Fast and Faithful Simulation of High-Bandwidth Flash Under Real GPU Execution](http://arxiv.org/abs/2609.09800v1)
  <details><summary>📄 Abstract</summary>
  Serving a large language model (LLM) is limited by memory capacity. High-Bandwidth Flash (HBF) stacks NAND flash inside the accelerator package, one tier below high-bandwidth memory (HBM); the specification was published on August 3, 2026, and the first inference devices are expected to sample in early 2027. Decisions about capacity and data placement cannot wait for silicon. No existing method settles those decisions: a storage simulator replaying a recorded access sequence never executes the w...
  </details>

- **2026-09-09** — Tian Zhang, Meng Li — [Should I Be Polite to My LLM Relevance Judge? Tone as a Severity Operating-Point Shift](http://arxiv.org/abs/2609.09703v1)
  <details><summary>📄 Abstract</summary>
  Large language models are increasingly used as relevance judges, yet their labels can shift with prompt surface form. We study one such feature -- tone -- on 3,498 TREC DL19/DL20 query-passage pairs, across eight judge models, five classifier-calibrated politeness levels, and three paraphrases per level. Effects are strongly model-dependent: one judge shows a structured U-shaped response, whereas most show only small changes. Where tone changes agreement, the results are more consistent with a s...
  </details>

- **2026-09-09** — Zheng-Hui Huang, Guixu Lin, Jiacheng Lin et al. — [Programmable World Model](http://arxiv.org/abs/2609.10540v1)
  <details><summary>📄 Abstract</summary>
  Recent video world models generate increasingly realistic and interactive visual experiences, yet lack reliable mechanisms for maintaining persistent world state and enforcing programmable rules over extended interactions. We introduce Programmable World Model, a framework that decouples world-state evolution from visual observation generation. An agent translates natural-language instructions into executable programs that specify entity states and state-transition rules, enabling direct control...
  </details>

- **2026-09-09** — Robin Huo, Ewan Dunbar — [Do speech foundation models really learn words?](http://arxiv.org/abs/2609.10434v1)
  <details><summary>📄 Abstract</summary>
  Self-supervised speech foundation models are now used in a wide array of downstream applications, including traditional speech recognition and as the basis for tokens in speech-aware language models. Attempts to understand their usefulness have largely focused on probing their representations' ability to discriminate phonemes and words. However, discriminative ability for words need not imply specialized representation of words per se. Good discrimination of words may be explained by good encodi...
  </details>

- **2026-09-09** — Mingjian Tuo, Jie Zhou, Yao Yan et al. — [Economic Evaluation of V2G-Enabled Fast Charging Stations Under Endogenous EV Adoption Dynamics](http://arxiv.org/abs/2609.10388v1)
  <details><summary>📄 Abstract</summary>
  Building fast charging stations (FCSs) is crucial for transportation electrification, but there exists an indirect network effect: while the increasing number of electric vehicles (EVs) decides the FCS capacity expansion, the spatial locations of these facilities strongly influence drivers' willingness to adopt EVs. Ignoring this interaction can lead to bad capital investments and exacerbate power grid vulnerabilities during tidal traffic peaks. Therefore, we explicitly model the EV adoption dyn...
  </details>

- **2026-09-09** — Weichen Dai, Rafael Medeiros Cabral, Ziyi Shou et al. — [From Symbolic Perception to Logical Deduction: A Framework for Guiding Language Models in Geometric Reasoning](http://arxiv.org/abs/2609.10335v1)
  <details><summary>📄 Abstract</summary>
  Plane geometry remains a significant challenge in AI, requiring the integration of visual perception and mathematical reasoning. While Large Multimodal Models (LMMs) naturally handle visuo-linguistic inputs, they are often computationally intensive and opaque. We demonstrate that a pure Large Language Model (LLM), when equipped with specialized modules, can rival state-of-the-art LMMs on complex geometry problems. Our framework integrates a Geometric Vision Parser, which translates diagrams into...
  </details>

- **2026-09-09** — Yanru An, Ruiyan Wang, Wenwu Wei et al. — [Decoupled Self-Forcing Distillation for Streaming Talking Head Generation](http://arxiv.org/abs/2609.10317v1)
  <details><summary>📄 Abstract</summary>
  Streaming talking-head generation produces each frame as its driving audio arrives, yet fidelity and efficiency have so far pulled in opposite directions: end-to-end methods condition a video diffusion model on audio directly and achieve high quality but only at large scale, while cheaper two-stage methods generate an intermediate motion representation and trail in fidelity. We argue the cost of the former lies in the target of fusion: the video latent is dominated by identity, appearance and ba...
  </details>

- **2026-09-09** — Bhuvan Arora, Devesh Saraogi, Sravya Varada et al. — [DiSCo: A Distribution-First Steering and Cultural Prior Evaluation Framework for Measuring Cultural Preference Bias in LLMs](http://arxiv.org/abs/2609.10253v1)
  <details><summary>📄 Abstract</summary>
  Large language models (LLMs) are increasingly deployed in globally used assistants, yet their default choices in culturally grounded everyday situations can systematically favour some cultures over others, affecting localisation, user trust, and equitable behaviour. Existing cultural benchmarks evaluate accuracy against a single "correct" answer, making it difficult to characterise an LLM's cultural preference prior when multiple culturally grounded responses are all valid; they also conflate de...
  </details>

- **2026-09-09** — Shuai Yan, Yang Xu, Shan He — [Agent-Based ML-LLM Fusion with Self-Optimizing Prompts for Plateau Weather Alerts](http://arxiv.org/abs/2609.10135v1)
  <details><summary>📄 Abstract</summary>
  To address insufficient contextualization, weak generalization, and poor scenario adaptation in tourism meteorological services, we propose SmartWeatherAgent--a unified three-stage architecture integrating intent recognition, hazard prediction, and reasoning-enhanced generation. The system fuses rule-based methods with large language models to parse queries at multiple granularities and employs a LightGBM model enriched with highland-specific features (e.g., wind speed abruptness rate), achievin...
  </details>

- **2026-09-09** — Yiling Zhou, Yilin Wang, Jianmin Wang et al. — [ADMET-EvO: a self-evolving scientific agent for sustained research across heterogeneous tasks](http://arxiv.org/abs/2609.10121v1)
  <details><summary>📄 Abstract</summary>
  Scientific agents can move beyond automated model building by using accumulated evidence to revise both their questions and experimental strategies. The challenge is sustaining this adaptation across heterogeneous tasks without overfitting decisions to internal validation. Absorption, distribution, metabolism, excretion and toxicity (ADMET) prediction provides a demanding setting across diverse assays, datasets and chemical domains. We therefore developed ADMET-EvO, an evidence-gated agent that ...
  </details>

- **2026-09-09** — Qirui Zhan, Shuiyuan Wang, Jingbin Hu et al. — [SpeechAnnotator: A Context-Aware Multi-Agent Framework and Benchmark for Multidimensional Speech Annotation](http://arxiv.org/abs/2609.09947v1)
  <details><summary>📄 Abstract</summary>
  Recent controllable speech generation requires training data with fine-grained annotations of speaker traits, prosody, emotion, paralinguistic cues, acoustic scenes, and context. Existing workflows often rely on manual correction, paid hosted multimodal services, or fixed processing chains, which limits large-scale data processing through annotation cost, external-service dependence, or weak cross-stage recovery. We introduce SpeechAnnotator, a locally deployable, context-aware multi-agent frame...
  </details>

- **2026-09-09** — An Vo, Vy Tuong Dang, Khai-Nguyen Nguyen et al. — [Deep and shallow biases in language models](http://arxiv.org/abs/2609.09901v1)
  <details><summary>📄 Abstract</summary>
  Large language models often repeatedly select the same answer even when many alternatives are plausible. Prior work treats this concentration as bias, but it does not distinguish stable model preferences from responses that depend on a particular prompt wording. We introduce a bias depth score that measures both how strongly a model prefers its top answer under direct prompting and whether that answer survives scenario reframing. Across 4,442 opinion prompts and four large language models, only ...
  </details>

- **2026-09-09** — Touchapon Kraisingkorn, Krittin Pachtrachai, Wachiravit Modecrua — [Scored vs. Generated Readouts in Behavioral Language Models: An Empirical Study of Elicitation Format](http://arxiv.org/abs/2609.09882v1)
  <details><summary>📄 Abstract</summary>
  Language models fine-tuned on customer behavior can predict outcomes and generate explanations, but these readouts are often treated as interchangeable. Holding model checkpoint and prompt content fixed, we compare probabilities obtained by scoring answer tokens with predictions generated after a written rationale. Across 13 model-domain cells covering four retail tasks in three markets, including two using fully public data and checkpoints, the scored readout ranks outcomes more accurately in 1...
  </details>

- **2026-09-09** — Lingxiao Qu — [Exact Degeneracy Under Balanced k-Shot Sampling:Consequences for Small-Sample Discriminant Analysis on LLM Embeddings](http://arxiv.org/abs/2609.09860v1)
  <details><summary>📄 Abstract</summary>
  Balanced k-shot sampling draws exactly k labeled examples per class. We show that it induces an exact, provable degeneracy in a family of small-sample discriminant estimators. Under balanced sampling, the within-class scatter operator of Kernelized Linear Principal Component Discriminant Analysis (KLPCDA) is not merely rank-deficient but exactly a scaled orthogonal projector. We derive the consequences in closed form: two of KLPCDA's seven variants have every signal eigenvalue exactly equal, so ...
  </details>

- **2026-09-09** — Benedikt Höltgen — [A Unifying Perspective on Probabilities as Model Predictions](http://arxiv.org/abs/2609.09855v1)
  <details><summary>📄 Abstract</summary>
  Although probabilistic statements are ubiquitous, foundational disagreements persist about their understanding, as exemplified by debates between Bayesians and frequentists; moreover, it is unclear when and why acting on them actually leads to desirable outcomes. Here, we argue that every probability is the output of a \emph{prediction method}, that is, it depends on both a particular way of constructing abstractions and a way of transforming them into predictions. Through this, we provide a uni...
  </details>

- **2026-09-09** — Hanjing Zhou, Mingze Yin, Ying Lian et al. — [LogiScope-VQA: Benchmarking Vision-Language Models for Logistics Hazard Identification in Industrial Scenarios](http://arxiv.org/abs/2609.09790v1)
  <details><summary>📄 Abstract</summary>
  Large Multimodal Models (LMMs) large-scale deployment in industrial warehouse settings specifically necessitates that models exhibit human-expert-level hazard-oriented perception, understanding, and reasoning capabilities. However, the scarcity of real industrial data, tightly coupled to commercial terms, significantly hampers further advancement. To bridge this gap, we curate LogiScope-VQA to investigate the practical applicability of mainstream LMMs in real-world logistics operations. LogiScop...
  </details>

- **2026-09-09** — Guanqun Zhao, Zijun Xie, Binbin Zheng et al. — [BRACE: Anchored Bellman-Residual Correction for Stale Critics in Asynchronous RL](http://arxiv.org/abs/2609.09783v1)
  <details><summary>📄 Abstract</summary>
  Asynchronous reinforcement learning has become the standard way to scale training for language models, but the resulting policy lag biases the critic toward the stale behavior policy. Existing work on asynchronous LLM training corrects the actor and leaves this bias unaddressed, while the off-policy value correction of classical RL does not carry over to long-horizon agentic tasks, since a short correction horizon leaves the regression target free of the reward and a long one lets the product of...
  </details>

- **2026-09-09** — Nikhita Vedula, Dushyanta Dhyani, Bryan Wang et al. — [Scaling E-Commerce Attribute Extraction with Parallel Decoding](http://arxiv.org/abs/2609.09716v1)
  <details><summary>📄 Abstract</summary>
  Customers rely on specific product attributes to compare products and make purchasing decisions, but e-commerce catalogs are messy and unstructured, making it difficult to identify which attributes matter most and extract them at scale. Standard Attribute Value Extraction (AVE) systems treat all attributes equally, producing large, inconsistent attribute sets that do not reflect the factors consumers use to differentiate products. We introduce a two-stage LLM pipeline that first discovers a comp...
  </details>

- **2026-09-09** — Kevin Hartman — [Introducing Consort: A Spec-First Agent Framework for Enforced, Test-Driven Development on Live Database Branches](http://arxiv.org/abs/2609.09671v1)
  <details><summary>📄 Abstract</summary>
  When an agent writes code, the development framework becomes the control system for a non-deterministic worker. Spec-first, agent-driven frameworks have gained rapid traction since 2025; the installable ones, GitHub Spec Kit, obra/superpowers, BMAD, and GSD, and our own, all capture intent through a specification or durable planning artifacts. Since they agree on capturing intent up front, what separates them is how each enforces the engineering discipline that keeps agent-written code clean, co...
  </details>

- **2026-09-09** — Jie Xu, Kangjin Yu, Ziyi Jin et al. — [JEPA Policy: Diffusion-Free Imitation Learning via Paired Action and Future Representation Prediction](http://arxiv.org/abs/2609.09630v1)
  <details><summary>📄 Abstract</summary>
  Standard behavior cloning supervises actions without explicitly constraining the future representation paired with each demonstrated action chunk. We introduce JEPA Policy, a diffusion-free framework that uses the action chunk and its observed future representation as paired training targets. Action and future-representation tokens interact in a shared Transformer and are refined through two forward passes. Future prediction can therefore shape the representation used to generate actions. Dual-b...
  </details>

- **2026-09-09** — Yaohan Guan, Yen-Ju Lu, Yuzhe Wang et al. — [Who Are They to Each Other? Multi-Agent Reasoning for Speaker Relationship Inference](http://arxiv.org/abs/2609.09628v1)
  <details><summary>📄 Abstract</summary>
  Inferring speaker relationships from spoken conversations is an important step towards socially aware speech understanding. However, this task remains underexplored, and supervised modeling is costly to train and scale. At the same time, existing inference-time LLM approaches provide limited structure for handling subtle, distributed, and multimodal relational cues that may support multiple plausible interpretations. To address these limitations, we introduce a training-free multi-agent reasonin...
  </details>

- **2026-09-09** — Haoran Gao, An Li, Zhen Li et al. — [From State Synchronization to Cognitive Self-Evolution: An Operational Architecture for Cognitive Digital Twins](http://arxiv.org/abs/2609.09625v1)
  <details><summary>📄 Abstract</summary>
  As Digital Twin (DT) systems evolve beyond state synchronization toward task-oriented and knowledge-driven operation, Cognitive Digital Twins (CDTs) have emerged as an extension that incorporates cognitive capabilities into twin operation. Existing CDT studies often focus on specific enabling techniques, such as learning modules, knowledge graphs, and large language models, while providing limited insight into how cognition can be systematically integrated into DT architectures. To address this ...
  </details>

- **2026-09-09** — Xin Wang, Paraic Carroll, Kerry Nice et al. — [Who You Are Adds Nothing Detectable to Where You Go Next: Sociodemographic Conditioning in LLM Next-Location Prediction](http://arxiv.org/abs/2609.09609v1)
  <details><summary>📄 Abstract</summary>
  Large language models (LLMs) are increasingly used for individual next-location prediction, while sociodemographic conditioning is common in LLM-based travel simulation. Yet the incremental predictive value of sociodemographic attributes remains unclear. To directly test this contribution, sociodemographic records were linked with passively sensed mobility data from 5,000 Shenzhen residents to construct a closed-set benchmark in which models rank 100 candidate destinations. Each prediction insta...
  </details>

- **2026-09-09** — Tomoaki Yasuda, Shotaro Ishihara — [Reproducing Omitted Temporal Expressions in Japanese News for Retrieval-Augmented Applications](http://arxiv.org/abs/2609.09569v1)
  <details><summary>📄 Abstract</summary>
  News articles often contain omitted temporal expressions, such as day-only or month-only mentions, which must be interpreted with reference to the publication date. When such articles are indexed or processed as standalone text in search and retrieval-augmented generation (RAG) systems, these omissions can cause temporal mismatches and unstable interpretation by large language models. We focus on reproducing omitted temporal expressions as concrete dates or intervals using the publication date a...
  </details>

- **2026-09-08** — Dhairya Bhatia, Bishoy Galoaa, Oliver Fritsche et al. — [MotionBlind: Probing the Illusion of Motion Understanding in Video-LLMs](http://arxiv.org/abs/2609.09528v1)
  <details><summary>📄 Abstract</summary>
  Video large language models (Video-LLMs) are increasingly used as the perceptual front end of world models, a role that assumes they can read motion: how fast something moves, which way it travels, how hard it is pushed. We show they cannot. A Video-LLM can watch two clips of the same person in the same room, name every object in both, and still fail to say which clip moves faster. We introduce MotionBlind, a contrastive benchmark of self-recorded video for physically grounded motion(speed, magn...
  </details>

- **2026-09-08** — Mamadou K. Keita, Angela Srbinovska, Anita Srbinovska et al. — [OmniEye: Efficient Multimodal Forensic Video Intelligence for Law-Enforcement Body-Worn Cameras](http://arxiv.org/abs/2609.09460v1)
  <details><summary>📄 Abstract</summary>
  We introduce OmniEye, a multimodal video intelligence system for law-enforcement training and review (source code available on request to verified law-enforcement and public-safety agencies). OmniEye ingests body-worn camera footage and perceives every 30-second window jointly across video and audio with one multimodal foundation model. It then stores the model's structured output in an embedded SQLite database with BM25 full-text search. Officers can question the footage through an agent that w...
  </details>

- **2026-09-08** — Earl Ranario, Jared Smith, Lars Lundqvist et al. — [Vision-language models know more about agriculture than they show and rubric-grounded verifications close the gap](http://arxiv.org/abs/2609.09417v1)
  <details><summary>📄 Abstract</summary>
  Vision-language models (VLMs) show promise for agricultural classification, but zero-shot performance on disease, pest, damage, quality, and species identification remains poor, and it is unclear whether this reflects weak visual features or a failure to connect them to domain knowledge. We build a benchmark of 116 datasets, 834 classes, and 8,324 images spanning these tasks to isolate where the gap arises. Linear probing shows VLM vision encoders already encode agricultural features nearly as s...
  </details>

- **2026-09-08** — Abhinav Sinha, Lohitvel Gopikannan, Shashi Ranjan Kumar — [Networked Admissibility-Preserving Control for Directed Safe Coordination](http://arxiv.org/abs/2609.09384v1)
  <details><summary>📄 Abstract</summary>
  This paper addresses safety-critical coordination for scalar agents whose distributed commands are implemented through constrained physical-input dynamics. Agents communicate over a fixed weighted digraph with a directed spanning tree, while their outputs must remain inside a common moving safety corridor and their realized inputs must satisfy heterogeneous asymmetric bounds. We propose a networked Admissibility-Preserving Control (APC) architecture in which an Admissibility-Preserving Input Rea...
  </details>

- **2026-09-08** — Samira Alkaee Taleghan, Younghyun Koo, Farnoush Banaei-Kashani — [An Autonomous GeoAI Agent for Arctic Eco-Navigation](http://arxiv.org/abs/2609.09374v1)
  <details><summary>📄 Abstract</summary>
  Arctic maritime navigation is becoming increasingly important as changing sea-ice conditions expand seasonal accessibility while simultaneously introducing substantial operational, environmental, and community risks. Arctic route planning is inherently a multi-criteria problem: routes that improve vessel safety or efficiency may increase exposure to sea ice, sensitive ecosystems, or nearby communities. Existing routing methods prioritize travel time, fuel use, and navigational risk, often overlo...
  </details>

- **2026-09-08** — Chuanruo Ning, Tianrui Wang, Wei-Chiu Ma et al. — [Proxy Policy Steering](http://arxiv.org/abs/2609.09148v2)
  <details><summary>📄 Abstract</summary>
  Generalist robot policies carry broad manipulation priors from large-scale data, but specializing them to a new task remains the deployment bottleneck. This requires eliciting task-specific behavior from limited demonstrations without degrading their broad capabilities. We introduce Proxy Policy Steering (PPS), an inference-time adaptation method that resolves this challenge by training two lightweight proxy policies whose calibrated velocity-space difference steers the frozen base sampler. A re...
  </details>

- **2026-09-08** — Nabila Tasfiha Rahman, Rajatsubhra Chakraborty, Depeng Xu et al. — [Efficient Fairness Auditing Across Guidance Scales in Text-to-Image Diffusion Models via Causal Abstraction](http://arxiv.org/abs/2609.09486v1)
  <details><summary>📄 Abstract</summary>
  Fairness auditing of text-to-image diffusion models often requires generating large numbers of images across sampling configurations, making comprehensive evaluation computationally expensive. We propose a causal-abstraction-based audit instrument for efficiently evaluating fairness under interventions on the classifier-free guidance scale. Given a fixed prompt and a target feature function, we represent the diffusion process as a low-level structural causal model and construct a corresponding h...
  </details>

- **2026-09-08** — Faiq Shamass — [Unthrottling the Tanh Jacobian in SAC: A Negative Result on Bang-Bang Control and MetaDrive](http://arxiv.org/abs/2609.09478v1)
  <details><summary>📄 Abstract</summary>
  Soft Actor-Critic (SAC) represents a continuous policy as an unbounded Gaussian that is squashed by tanh. The Jacobian of that map is $\partial a/\partial u = 1-a^2$, which vanishes as $|a|\to 1$. A natural concern is that this throttle starves the actor of critic signal exactly where extreme actions (full brake, full throttle) are optimal. We test a minimal intervention that restores the missing signal: one extra term in the actor loss whose gradient on the pre-tanh mean is the detached action-...
  </details>

- **2026-09-08** — Yanfei Hu Fleischhauer, Alona Zharova, Nadja Klein et al. — [XAI-Arena: Can LLMs Assess the Quality of XAI Explanations?](http://arxiv.org/abs/2609.09428v1)
  <details><summary>📄 Abstract</summary>
  Evaluating the quality of explanations produced by explainable AI (XAI) methods remains challenging because existing approaches often rely on subjective human judgment, limiting reproducibility, scalability, and comparability between studies. We examine whether LLMs can serve as a reproducible and scalable mechanism to make comparative assessments of the quality of XAI explanations. We introduce XAI-Arena, an LLM-as-a-judge framework for scalable, reproducible, multidimensional, and stakeholder-...
  </details>

- **2026-09-08** — Shobhit Jagga, Aman Dalmia, Niharika Priyadarshini et al. — [Auditable Emergency Triage for Maternal and Newborn Care in India](http://arxiv.org/abs/2609.09356v1)
  <details><summary>📄 Abstract</summary>
  At Noora Health, our nurses answer more than 50,000 medical queries per month on our WhatsApp-based service that provides caregivers with on-demand support. Their most time-critical task is emergency triage: deciding which queries need immediate in-person attention. To support them, we built a system that uses a large language model (LLM) to classify whether a message is an emergency and provide a rationale for interpretability. But the system was opaque: analyzing mistakes meant reading reasoni...
  </details>

- **2026-09-08** — Vincent T. Lee, Armin Alaghi, Carole-Jean Wu et al. — [Academia x Industry: The Role of Fundamentals for Silicon in an AI Native Era](http://arxiv.org/abs/2609.09344v1)
  <details><summary>📄 Abstract</summary>
  Agentic AI is set to become one of the most transformational technologies in generations and materially change how we approach silicon design and engineering. The impact is being felt in real time amid a rapidly changing landscape, which can make it overwhelming for both silicon practitioners and academics to adapt to the AI native silicon design era. To add structure to how we navigate this transition, we provide a joint view from academia and industry silicon practitioners of the challenges, o...
  </details>

- **2026-09-08** — Rx Fan, Z Han — [Hi-FLoop: Hierarchical State-Feedback Loops for Multi-Timescale World Modeling](http://arxiv.org/abs/2609.08796v2)
  <details><summary>📄 Abstract</summary>
  Multi-agent traffic simulation seeks diverse, coordinated, and physically realistic futures from maps and observed history. Long-horizon closed-loop generation must reconcile multiple decision time scales while its context evolves with generated states. Existing methods often unfold long futures from an initial scene and resolve intent, interaction, and motion monolithically, weakening cross-scale consistency and adaptation. Multimodal rollout poses a further consistency problem: independently r...
  </details>

- **2026-09-08** — Chuanruo Ning, Tianrui Wang, Wei-Chiu Ma et al. — [Proxy Policy Steering](http://arxiv.org/abs/2609.09148v1)
  <details><summary>📄 Abstract</summary>
  Generalist robot policies carry broad manipulation priors from large-scale data, but specializing them to a new task remains the deployment bottleneck. This requires eliciting task-specific behavior from limited demonstrations without degrading their broad capabilities. We introduce Proxy Policy Steering (PPS), an inference-time adaptation method that resolves this challenge by training two lightweight proxy policies whose calibrated velocity-space difference steers the frozen base sampler. A re...
  </details>

- **2026-09-08** — Min Zeng, Yuzhou Liu, Zhenyu Cao et al. — [ToolLoop: Closed-Loop Tool-Use Data Synthesis via Decomposed Generation and Dynamic Self-Feedback](http://arxiv.org/abs/2609.09072v1)
  <details><summary>📄 Abstract</summary>
  High-quality tool-use data is critical for training language models to interact effectively with external tools. However, existing synthetic approaches typically follow a generate-then-filter paradigm with static post-hoc verification, often yielding inefficient data with imbalanced feature distributions. We propose ToolLoop, a closed-loop framework that decomposes synthesis into three progressive stages: (1) sampling function name combinations as ground truth; (2) backward derivation of user qu...
  </details>

- **2026-09-08** — Subavarshana Arumugam, Mamta Nallaretnam, Kithuni Wickramasinghe et al. — [Evaluation of Contextual Understanding in Large Language Models](http://arxiv.org/abs/2609.09004v1)
  <details><summary>📄 Abstract</summary>
  Large Language Models (LLMs) demonstrate impressive performance across diverse NLP tasks, yet their ability to exhibit genuine contextual understanding remains uncertain. Traditional evaluation metrics such as perplexity, BiLingual Evaluation Understudy (BLEU), or surface-level accuracy fail to reveal how well LLMs extract, integrate, and reason over contextual information--a gap particularly critical in question answering, where models must align responses with contextually grounded knowledge r...
  </details>

- **2026-09-08** — Yuan Gao, Sebastian Müller, Mattia Piccinini et al. — [PlannerForge: LLM Agents for Scenario-Based Testing of Motion Planners in Autonomous Driving](http://arxiv.org/abs/2609.08965v1)
  <details><summary>📄 Abstract</summary>
  Ensuring the safety of autonomous driving is a critical challenge. Scenario-based testing is a systematic process used to validate Autonomous Driving Systems (ADSs), but it remains a fragmented modular pipeline in which scenario generation, retrieval, modification, ADS execution, and results analysis are performed by separate tools with little interaction. Large Language Model (LLM) agents have shown promise across ADS sub-systems such as perception, planning, and control. However, no prior work...
  </details>

- **2026-09-08** — Linnan Zhao, Xu Liu, Lingling Li et al. — [SeGDeP: Semantic- and Geometric-Aware Decoupled Prompts for Reasoning Segmentation](http://arxiv.org/abs/2609.08867v1)
  <details><summary>📄 Abstract</summary>
  Reasoning segmentation converts an implicit linguistic conclusion into a precise mask, requiring both semantic identification and spatial grounding. Existing MLLM-segmenter interfaces either use a special trigger or compress both signals into one context, although they receive different supervision and fail differently. This coupling obscures whether a failure arises from target interpretation or from localization. We present SeGDeP, an explicit what-where interface. A semantic prompt branch and...
  </details>

- **2026-09-08** — Evelyn Duesterwald, Benjamin Elder, Lilian Ngweta et al. — [Closing the Consistency Gap: Self-Evolving Agents That Learn to Stay on Course](http://arxiv.org/abs/2609.08832v1)
  <details><summary>📄 Abstract</summary>
  Large language model (LLM)-powered agents can be accurate on average yet unreliable in production, a discrepancy that has been observed but remains largely unaddressed. When given the same task five times, a ReAct agent on the AppWorld benchmark using GPT-4.1 succeeds in all five runs only 53% of the time, even though its per-run pass rate averages 77%. We call this 24-point shortfall the consistency gap, and we argue that addressing it is a precondition for trustworthy AI agent deployment. We p...
  </details>

- **2026-09-08** — Mahir Jain, Parshva Runwal, Aditya Ray Mishra et al. — [Adaptive Anisotropic Attention for Axis-Structured Signals](http://arxiv.org/abs/2609.08788v1)
  <details><summary>📄 Abstract</summary>
  Dense self-attention treats all token pairs as equally plausible before learning, an interaction-isotropic prior that can be mismatched to structured signals. For structured, low signal-to-noise ratio (SNR) signals such as EEG, dependencies are organized along the electrode and time axes, and this uniform prior exposes each token to many irrelevant interactions. We introduce Adaptive Anisotropic Attention (AAA), which splits attention into two paths: a temporal path, where each token attends to ...
  </details>

- **2026-09-08** — Zhiwei Lin, Kaiqi Fu, Rime Wen et al. — [X2Streaming-ASR: wait when uncertain, emit when ready for streaming ASR](http://arxiv.org/abs/2609.08672v1)
  <details><summary>📄 Abstract</summary>
  Streaming automatic speech recognition (ASR) for real-time voice agents and full-duplex dialogue must provide accurate partial transcripts with low commit latency. Existing systems commonly use a fixed chunk size, look-ahead, or target delay, or encourage emissions near estimated acoustic boundaries. These approaches do not directly optimize how much additional context to use at each output position under a single-pass, hard-commit constraint. We propose X2Streaming-ASR, which decomposes streami...
  </details>

- **2026-09-08** — Minqiang Zou, Riqiang Jin, Zhi Lv et al. — [GOLF: Global Observation with Local Focus for Calibration-Aware Stereo Interaction Field Estimation](http://arxiv.org/abs/2609.08607v1)
  <details><summary>📄 Abstract</summary>
  We present GOLF, the first-place solution to the SHOW3D Interaction Field Estimation Challenge at HANDS@ECCV 2026. Given synchronized egocentric stereo views, the task is to predict a 3D vector from each of 21 hand joints to the closest point on the manipulated object. GOLF combines dense global context, locally sampled hand/object evidence, and common-frame Plücker-ray geometry. We adapt DINOv3 ViT-H+/16 with LoRA and trainable LayerNorm parameters, then jointly decode both interaction fields. ...
  </details>

- **2026-09-08** — Tianyi Ma, Parisa Kordjamshidi — [CLAMP: Constrained Decoding for Vision-Language Embodied Planning](http://arxiv.org/abs/2609.08602v1)
  <details><summary>📄 Abstract</summary>
  Embodied planning increasingly relies on vision-language models (VLMs) to translate instructions and visual observations into executable action sequences. However, fluent plans are not always executable. A VLM may refer to objects that are not visually observed, select actions whose required affordances are unavailable, or violate syntax and action constraints. We introduce CLAMP, a multimodal constraint-grounding framework that turns scene evidence into decoding-time constraints for a frozen VL...
  </details>

- **2026-09-08** — Jing Li, Duygu Sarikaya — [STSG-VQA: Evidence-Grounded Temporal Question Answering from Surgical Spatio-Temporal Scene Graphs](http://arxiv.org/abs/2609.08543v1)
  <details><summary>📄 Abstract</summary>
  Despite recent advances in surgical vision-language models (VLMs), temporal reasoning remains limited because existing supervision is largely frame-centric. Frame-level scene graphs (SGs) have proven effective in providing structured representations of surgical environments but do not explicitly model the dynamics of surgical workflows. To explicitly model how surgical states evolve across time, we introduce a multi-level structured temporal supervision methodology that augments frame-level surg...
  </details>

- **2026-09-08** — Yuemei Xu, Kexin Xu, Jian Zhou et al. — [Same Values, Different Languages? From Multilingual Probing to Steering LLMs Toward Chinese Social Values](http://arxiv.org/abs/2609.08515v1)
  <details><summary>📄 Abstract</summary>
  As Large Language Models (LLMs) are increasingly integrated into human society, aligning them with pluralistic social values has become a critical priority. However, whether LLMs exhibit consistent value preferences across languages remains underexplored, particularly for culturally grounded values, which are more abstract and difficult to evaluate and align than safety-centric principles. We investigate this issue through Chinese Social Values (CSV), a value system rooted in Chinese culture and...
  </details>

- **2026-09-08** — Jeahn Han, Minji Kim, Jeongbin Sohn et al. — [GALoc: Gravity Aligned Wireframes for Depth-Free Monocular Floorplan Localization](http://arxiv.org/abs/2609.08385v1)
  <details><summary>📄 Abstract</summary>
  Floorplans are compact, appearance-invariant maps ideal for indoor localization, yet existing methods rely on depth networks that are brittle in cluttered scenes. We propose GALoc, a geometry-first framework that replaces depth prediction with gravity-aligned wireframes that satisfy verticality and coplanarity by construction. Given monocular RGB, camera intrinsics, relative poses, and IMU orientation, GALoc constructs a linear constraint matrix encoding verticality and coplanarity, and finds th...
  </details>

- **2026-09-08** — Xiangwu Wang, Chengwei Cao, Hongyuan Tang — [Rank Without an Oracle: Deviation-Aware Interaction-Rank Selection from Offline Multi-Agent Logs](http://arxiv.org/abs/2609.08358v1)
  <details><summary>📄 Abstract</summary>
  Offline multi-agent payoff models are estimated under a logging distribution but used on distributions induced by learned solutions and unilateral deviations. Standard held-out loss can therefore favor an interaction class that predicts logged play well while distorting strategic incentives. We introduce Selective Interaction-Rank Validation (SIRV) for finite games with known logging distributions. A training split fits nested payoff models and constructs a common union of all candidate deployme...
  </details>

- **2026-09-08** — Hongzheng Chai, Jiakun Li, Hongyue Yu et al. — [RepoNav: From Snippet Retrieval to File-Centered Repository Navigation for Code Agents](http://arxiv.org/abs/2609.08355v1)
  <details><summary>📄 Abstract</summary>
  Solving repository-level code tasks requires LLM-based agents to use code search tools to navigate large codebases and identify a small set of relevant files and functions. However, current retrieval tools typically return flat lists of isolated code snippets: such lists can surface relevant files, but provide insufficient structure for agents to distinguish the target function from semantically similar alternatives in the same file. We introduce RepoNav, a lightweight post-retrieval interface t...
  </details>

- **2026-09-08** — Dingying Liu, Yunshun Zhong, Wentao Zhang et al. — [CIVI: A Framework for Diagnosing Search Agent Failures in Civic Information](http://arxiv.org/abs/2609.08094v1)
  <details><summary>📄 Abstract</summary>
  Large Language Models are increasingly deployed in public-sector settings, where incorrect guidance can cause irreversible harm. We introduce CIVI, the first framework for diagnosing search agent failures in civic information. Its benchmark instantiation jointly spans cross-national, interjurisdictional government contexts (federal, state, and local) and functional categories from an internationally adopted United Nations standard. We evaluate ten frontier search agents and find that none matche...
  </details>

- **2026-09-08** — Yankai Fu, Ning Chen, Junkai Zhao et al. — [DeCAL: Towards Physically-Grounded Dexterous Vision-Language-Action Models via Contact-Aware Latent Co-Imagination](http://arxiv.org/abs/2609.09119v1)
  <details><summary>📄 Abstract</summary>
  Dexterous manipulation involves contact-rich and fine-grained interactions with the physical world, posing significant challenges for existing vision-language-action (VLA) models due to severe visual occlusions and complex contact dynamics. While recent works have incorporated tactile sensing into robotic manipulation, most approaches still rely on homogeneous multimodal fusion, lacking adaptive tactile integration and explicit modeling of physical dynamics. In this work, we present DeCAL, a phy...
  </details>

- **2026-09-08** — Yang Li, Sergey Volkov, Hai Liu et al. — [Beyond Agent Harnesses: Cross-Substrate Authority for Multi-Agent Systems](http://arxiv.org/abs/2609.08472v1)
  <details><summary>📄 Abstract</summary>
  Agentic systems persist model-visible memory while mutating workspaces, while a runtime, registry, or approval service may hold authority state outside both. Identical final files can then require opposite safe actions. We call this the cross-substrate authority gap: decision- relevant authorization information resides outside the planner-visible workspace or memory state. Across two controlled mini-benchmark families, three experiments compare planner-observation augmentation with an execution-...
  </details>

- **2026-09-08** — Ziqin Huang, Yingyue Li, Chenyangguang Zhang et al. — [3DWay: Generalizing Robot Manipulation via 3D Consistent Waypoints](http://arxiv.org/abs/2609.08224v1)
  <details><summary>📄 Abstract</summary>
  Intermediate representations are key to bridging the modality gap between generalizable manipulation policies and large-scale pretrained vision-language models (VLMs). Among these, trajectory-based representations compactly represent motion-relevant cues, yet most existing approaches predict trajectories in 2D image space, resulting in intrinsic 3D ambiguity. Moreover, using 2D trajectories with depth still leaves the free-space waypoints ambiguous, limiting reliable 3D reasoning. To address thi...
  </details>

- **2026-09-08** — Jingyi Chen, Mohan Zhang, Laura Yao et al. — [Bridging Language and Physics: Automated Design of Continuum Robots with Large Language Models](http://arxiv.org/abs/2609.08220v1)
  <details><summary>📄 Abstract</summary>
  Large language models (LLMs) have recently emerged as a promising tool for automating robot design from high-level specifications, yet they remain ineffective for robots operating under complex physical interactions. This limitation stems from the gap between language-based reasoning and the physical consequences of embodiment, often resulting in designs with low physical validity. In this work, we propose a multi-layered framework, AID-SR, that establishes a closed loop by translating simulator...
  </details>

- **2026-09-08** — Yuxing Lu, Yicheng Chen, Shanchan Wu et al. — [Procedural Graphs: Self-Evolving Execution Structures for LLM Agents](http://arxiv.org/abs/2609.09153v1)
  <details><summary>📄 Abstract</summary>
  Large language models are increasingly deployed as agents that plan over long horizons and act through external tools. Most agents select actions through unconstrained generation over an accumulating history, leaving implicit the procedural knowledge of what to do, in what order, and under which conditions. As trajectories lengthen, agents can lose track of their objectives, invoke tools out of order, and repeat unproductive actions. We introduce the Procedural Graph: just as a knowledge graph o...
  </details>

- **2026-09-08** — Yanlin Chen, Tang Li, Xi Peng — ["World Knowledge" in the Weights: Reading Concept Circuits of Vision Transformers](http://arxiv.org/abs/2609.09055v1)
  <details><summary>📄 Abstract</summary>
  Vision transformers (ViTs) have achieved remarkable generalization across visual domains, yet little is known about how they internally represent the structure of the world. To address this gap, we use Cross-Layer Transcoders (CLTs) to read concept circuits from ViTs: directed graphs whose nodes correspond to sparse, interpretable concepts and edges capture concept interactions across layers. Our method yields two complementary views of model behavior. The global concept circuit is input-invaria...
  </details>

- **2026-09-08** — Siddharth Vohra, Manikandan Ravikiran — [The Audit Decides the Verdict: Instrument Effects Rival Demographic Bias in LLM Decision Audits](http://arxiv.org/abs/2609.09048v1)
  <details><summary>📄 Abstract</summary>
  Whether a language model looks demographically biased can depend on how the audit asks its question. A charitable-aid benchmark reports that the same models favor minority applicants when rating requests one at a time and penalize some when ranking side by side. We test whether that reversal generalizes to hiring, lending, and medical triage: 40,726 requests to five models, applications differing only in the applicant's name, and a primary test fixed before collection. It does not. None of 36 pl...
  </details>

- **2026-09-08** — Paul Gölz — [PMMS Allocations Need Not Exist for 3 Agents with Additive Valuations](http://arxiv.org/abs/2609.08954v1)
  <details><summary>📄 Abstract</summary>
  This note gives an instance demonstrating that the pairwise maximin share (PMMS) property cannot be satisfied by any allocation in certain fair division problems with indivisible goods and additive valuations. The instance requires only $n=3$ agents and $m=9$ goods, and is accompanied by a proof that no PMMS allocation exists. A separate instance shows (certified by exhaustive enumeration with a computer) that PMMS cannot be approximated within a ratio above $78/79 \approx 0.987$.
  </details>

- **2026-09-08** — Jennifer Wang, Joachim Baumann, Daniel E. Ho et al. — [API Benchmark Scores Do Not Reliably Transfer to Chatbot Interfaces](http://arxiv.org/abs/2609.08861v1)
  <details><summary>📄 Abstract</summary>
  Benchmark scores are a central currency in model releases: they inform purchasing decisions, shape public trust, and influence policy. Yet, a key assumption underlying benchmark scores is that the model performance measured through APIs faithfully reflects the behavior of deployed systems.   We challenge this assumption by auditing ChatGPT, Claude, and Gemini across seven systems and nine benchmarks spanning general capability, social bias, and sycophancy. We find systematic API--interface diffe...
  </details>

- **2026-09-08** — Badreddine Benhellal, Noah Körner, Dylan Machado et al. — [MIT bag model and infinite mass limit in non-smooth domains](http://arxiv.org/abs/2609.08791v1)
  <details><summary>📄 Abstract</summary>
  The work is devoted to the study of Dirac operators with MIT bag boundary conditions in Euclidean domains with compact Lipschitz boundaries in arbitrary dimensions. It is shown that such operators are self-adjoint on suitable definition domains and can be recovered as the norm-resolvent limits of Dirac operators in the whole space with a large mass term outside the domain, under the assumption that an associated Robin-Laplacian eigenvalue has a prescribed asymptotic behavior with respect to a pa...
  </details>

- **2026-09-08** — Jonathan Frank, David Richerby, Ansgar Scherp — [Chimaera: A Mixture-of-Graph-Experts Architecture for Cross-Task and Cross-Dataset Graph Learning](http://arxiv.org/abs/2609.08709v1)
  <details><summary>📄 Abstract</summary>
  Designing foundation models for graphs is challenging due to the irregular structure of graphs and the different sizes and characteristics of embeddings. Chimaera integrates mixture-of-experts with graph foundation models (GFM). It integrates different GFM architectures, such as graph prompts and linear GNN models. Large language models are used to generate embeddings, and experts can be trained and combined following different strategies, GFMs, embeddings, etc. Furthermore, Chimaera extends exi...
  </details>

- **2026-09-08** — Zehan Lin, Shengxin Liu, Biaoshuai Tao et al. — [Comparison-Based Fair Division of Indivisible Chores](http://arxiv.org/abs/2609.08687v1)
  <details><summary>📄 Abstract</summary>
  We investigate the query complexity of fairly allocating $m$ indivisible chores among $n$ agents with additive cost functions. We depart from the standard cardinal model and assume only comparison access: an algorithm may ask an agent which of two bundles is less costly, but never observes numerical costs. Our first results concern proportionality up to one item (PROP1). We design comparison-based algorithms that compute PROP1 allocations using $O(n^3\log m)$ comparison queries. When the chores ...
  </details>

- **2026-09-08** — Sara Rizwan, Samaanah Abdus Salam — [Do New Attention Mechanisms Actually Fix Attention Sinks at Million-Token Context?](http://arxiv.org/abs/2609.08574v1)
  <details><summary>📄 Abstract</summary>
  Long context language models now advertise windows of one million tokens, but two habits limit how much of that window is used. Attention heads with nothing useful to read still spend their budget on the first token, which is called the attention sink, and where a fact sits in the context changes whether the model finds it. Gated attention cut first token attention from 46.7 percent to 4.8 percent at NeurIPS 2025, and Kimi K3 pairs that idea with Kimi Delta Attention and Attention Residuals behi...
  </details>

- **2026-09-08** — Ho Yi Alexis Ho, Xinzhou Guo, Shuoxun Xu — [Structure-based Transfer Learning](http://arxiv.org/abs/2609.08487v1)
  <details><summary>📄 Abstract</summary>
  Transfer learning improves estimation in a target study using information from related sources. Classical transfer learning is typically data-based, requiring access to the source data or to a model fitted on them. Neither is available in many modern studies, as both are often proprietary or unreported. What can be transferred instead is structure: summarized information derived from a source, such as the supports of predictors, which is available and interpretable without access to the source d...
  </details>

- **2026-09-08** — David Reiss, Oriol Sallent, Miguel Catalan-Cid et al. — [Toward Fully Autonomous 6G Networks: AI-driven Operational Efficiency and Optimization](http://arxiv.org/abs/2609.08426v1)
  <details><summary>📄 Abstract</summary>
  Mobile networks evolution is characterized by a substantial increase in system complexity, driven by the need to accommodate a growing number of heterogeneous services on top of the digital infrastructure. This growth in service accommodation is expected to accelerate with the adoption of the Network as a Service (NaaS) paradigm, which has emerged as a promising approach to accelerate network innovation while enabling new revenue streams for operators. Although it is fundamental to abstract netw...
  </details>

- **2026-09-08** — Boao Yu, Zimo Chen, Junreng Rao et al. — [Towards Embodied Air-Ground Cooperative Object Search: Benchmark, Dataset and Agentic Method](http://arxiv.org/abs/2609.08402v1)
  <details><summary>📄 Abstract</summary>
  Air-Ground Object Search (AGOS) in urban environments is a challenging embodied task, which requires an Unmanned Aerial Vehicle (UAV) and an Unmanned Ground Vehicle (UGV) to jointly search for and verify a specified target vehicle from multi-view visual references. To study this underexplored problem, we introduce AGOS-Bench, the first dedicated benchmark for evaluating whether general-purpose Vision-Language Models (VLMs) can integrate aerial discoveries and ground-level verification through UA...
  </details>

- **2026-09-08** — Elaheh Akbarnejad, Aleksander Kostka, Advika Chesetti et al. — [A thermally grown SiO2 diffusion barrier enabling high-temperature investigation of Ag-Au-Pd-Pt thin films](http://arxiv.org/abs/2609.08363v1)
  <details><summary>📄 Abstract</summary>
  Combinatorial processing platforms (CPPs), integrating Si microtip arrays with combinatorial thin film synthesis and atom probe tomography (APT), enable near-atomic-scale characterization of compositionally complex solid solutions (CCSSs) under diverse processing and reaction conditions, including oxidation, thermal phase stability and electrocatalytic reactions. Their application at elevated temperatures, however, can be limited when CCSS constituents such as Pd and Pt react with the Si support...
  </details>

- **2026-09-08** — Etienne Rousseau, Guillaume Rousseau — [Pascal tiling and congruences modulo N in Pascal's triangle](http://arxiv.org/abs/2609.08343v1)
  <details><summary>📄 Abstract</summary>
  We investigate the properties of matrices obtained from a geometric transformation of the first $N$ rows of Pascal's triangle. For $N > 2$, their congruence properties form a \emph{Pascal tiling}, that is, a perfect alternation between entries congruent to $0 \pmod{N}$ and the others, if and only if $N$ is prime.   This result yields an alternative proof of the classical congruence $L_N-1\equiv 0 \pmod{N}$ for prime $N$, where $L_N$ denotes the $N$th Lucas number. Within the framework of the \em...
  </details>

- **2026-09-08** — Ziyu Luo, Xiaorui Ma, Lin Chen et al. — [CircuTutor: Transforming Static Circuit Problems into Intelligent and Dynamic Tutoring](http://arxiv.org/abs/2609.08254v1)
  <details><summary>📄 Abstract</summary>
  Learning direct current circuit concepts requires learners to connect invisible physical quantities, such as current, voltage, resistance, and power, with observable outcomes such as bulb brightness. Conventional textbook materials and general-purpose circuit simulators provide opportunities for problem solving and exploration but offer limited support for explaining why circuit behavior changes or diagnosing the reasoning behind incorrect answers. We present CircuTutor, a circuit-state-driven i...
  </details>

- **2026-09-08** — Girish G N, Ashutosh Sahoo, Akshay SP et al. — [zScore-N: A Neural Network for On-Chain Wallet Reputation Scoring](http://arxiv.org/abs/2609.08247v1)
  <details><summary>📄 Abstract</summary>
  Wallet reputation scores decide who receives an airdrop, who can borrow, and who enters an allowlist across decentralised finance. They almost always begin as hand-written formulas: compositions of clamped logarithmic, linear and square-root transforms over behavioural features, with every threshold and point award set by hand. Such a formula is readable and deterministic, but it is piecewise and non-differentiable, it cannot improve as data accumulates, and it cannot distinguish a feature that ...
  </details>

- **2026-09-08** — Longfei Ma, Zemin Liu, Fei Wu — [TTGBench: Benchmarking Topological Evolution and Semantic Drift in Text-attributed Temporal Graphs](http://arxiv.org/abs/2609.08226v1)
  <details><summary>📄 Abstract</summary>
  Temporal graph learning models the evolution of dynamic systems, where both structural interactions and semantic states change over time. However, existing benchmarks primarily emphasize structural evolution via temporal link prediction (TLP), while support for semantic evolution remains limited. Although temporal node classification (TNC) is sometimes included, it is typically restricted to simplistic binary settings that fail to capture realistic semantic drift. Moreover, commonly used dataset...
  </details>

- **2026-09-08** — Masaaki Geshi, Yuichi Akahama — [Pressure Evolution of Atomic Volume Systematics in Transition Metals](http://arxiv.org/abs/2609.08197v1)
  <details><summary>📄 Abstract</summary>
  We investigated the evolution of the well-known parabolic dependence of atomic volume on atomic number in transition metals under extreme compression at pressures up to 400 GPa using density functional theory calculations. Our results reveal that the ambient-pressure parabolic trend transforms into a characteristic cubic-like behavior at high pressures. This evolution is attributed to the higher compressibility of bcc transition metals associated with comparatively large increases in the total e...
  </details>

- **2026-09-08** — Wenhao Li, Shuxing Yang, Fujia Chen et al. — [Qiushi Engine on AstaBench E2E-Bench-Hard](http://arxiv.org/abs/2609.08196v1)
  <details><summary>📄 Abstract</summary>
  This report analyzes Qiushi Engine v0.8 across all 40 test tasks in AstaBench E2E-Bench-Hard, a benchmark that requires autonomous agents to carry a research question through experimental design, code implementation, actual execution, result analysis, and report delivery. Qiushi Engine is model-configurable; this evaluation selected DeepSeek deepseek-v4pro-preview as the model backend. The official AstaBench leaderboard records a score of 0.816 and an average benchmark cost of USD 15.209 per tas...
  </details>

- **2026-09-08** — Hongjin Lin, Wentao Wan, Keze Wang — [Do Dynamic Routers Need Memory? HeRo: History-Aware Routing for Efficient LLM Inference](http://arxiv.org/abs/2609.08189v1)
  <details><summary>📄 Abstract</summary>
  Dynamic layer routing reduces the inference cost of Large Language Models (LLMs) by learning to skip layers for individual tokens. Existing methods, however, treat each routing decision as a local operation conditioned solely on the current hidden state which is a formulation that overlooks the sequential, path-dependent nature of routing across depth: earlier decisions shape the representations seen by downstream routers, and the layer-usage objective couples all decisions jointly. We propose H...
  </details>

- **2026-09-08** — Wenbo Zhang, Zhongxiang Sun, Zhiguang Han et al. — [Key Path Identification for Resolving Knowledge Conflicts via SAE-based Steering](http://arxiv.org/abs/2609.08173v1)
  <details><summary>📄 Abstract</summary>
  Sparse autoencoder (SAE)-based steering has been widely used to address knowledge conflicts by guiding LLMs to be more faithful to the contextual knowledge. Existing methods usually perform mass steering, which modifies a large batch of SAE features identified via correlation-based methods. However, due to the inaccurate correlation and the neglected feature interactions, mass steering methods fail to precisely identify the features that play the key roles in steering and introduce a large numbe...
  </details>

- **2026-09-08** — Jaedeok Lee, Keonwoo Kim, Dongyoon Han et al. — [Router Prior Bias: Preserving Base Routing Structure in MoE Post-Training](http://arxiv.org/abs/2609.08115v1)
  <details><summary>📄 Abstract</summary>
  Mixture-of-Experts (MoE) pretraining relies on an auxiliary load-balancing loss (LBL) to drive per-expert utilization toward uniformity. Post-training inherits a different situation: the base router already encodes non-uniform expert co-activation structure, which a re-imposed uniformity objective flattens away. We show that downstream performance depends instead on holding this inherited routing softly, a principle we term soft router anchoring, and instantiate it as Router Prior Bias (RPB), a ...
  </details>

- **2026-09-08** — Fenghua Yang, Preet Baxi, Yi Zhang et al. — [Automated Design of Inventory Policy with Large Language Models: An Exploratory Study](http://arxiv.org/abs/2609.08071v1)
  <details><summary>📄 Abstract</summary>
  Firms making inventory decisions have access to operational data, optimization tools, and large language models (LLMs). Typically, data characterize the operating environment, optimization selects parameters within a prespecified inventory policy class, and LLMs support coding and decision analysis. We develop an integrated framework that combines these resources to automate inventory policy design. Given demand data, the framework iteratively uses an LLM to generate parameterized policy classes...
  </details>


## 📊 统计 / Statistics

| 分类 / Category | 论文数 / Count |
|------|--------|
| jailbreak | 625 |
| prompt-injection | 534 |
| memory-poisoning | 49 |
| tool-use-attack | 134 |
| backdoor | 451 |
| adversarial-attack | 589 |
| privacy-leakage | 4064 |
| steganography | 64 |
| misuse | 1004 |
| red-teaming | 123 |
| vulnerability | 3042 |
| defense | 2840 |
| alignment | 2647 |
| robustness | 2749 |
| watermark | 416 |
| unlearning | 95 |
| agent-safety | 54 |
| benchmark | 65 |
| survey | 339 |
| other | 7484 |

---

📚 **全部 27368 篇论文**（2022 至今）请访问 [GitHub Pages](https://ny1024.github.io/AgentSafety-Papers/) 查看完整列表、搜索与筛选。

⚠️ **本次更新跳过：arXiv API 爬取失败，数据为上次缓存。下次 CI 将自动重试。**

*Generated by AgentGuard at 2026-09-13 11:16:41*