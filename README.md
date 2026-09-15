<div align="center">

# AgentGuard 🛡️

**Daily Tracking of LLM Agent Security Papers on arXiv**

[![Auto Update](https://github.com/NY1024/AgentSafety-Papers/actions/workflows/daily-update.yml/badge.svg)](https://github.com/NY1024/AgentSafety-Papers/actions/workflows/daily-update.yml)
[![Papers](https://img.shields.io/badge/Papers-27635-blue)](#)
[![License](https://img.shields.io/badge/License-MIT-green)](#)

</div>

---

## 📖 简介 / Introduction

自动追踪 arXiv 上大模型 Agent 安全方向的最新论文，每日更新，关键词智能分类。

*Automatically tracking the latest LLM Agent security papers on arXiv, updated daily with keyword-based classification.*

**最近更新 / Last Updated**: 2026-09-15 20:47 ｜ **论文总数 / Total Papers**: 27635（近 30 天 / Recent 30 days: 3814）

🌐 **[GitHub Pages](https://ny1024.github.io/AgentSafety-Papers/)** — 查看全部 27635 篇论文（含摘要、分类筛选、搜索）/ View all 27635 papers with abstracts, filters & search

## 📑 分类导航 / Category Navigation

- **[jailbreak](#-jailbreak)** — 越狱攻击 / Jailbreak Attacks — 628
- **[prompt-injection](#-prompt-injection)** — 提示注入攻击 / Prompt Injection Attacks — 538
- **[memory-poisoning](#-memory-poisoning)** — 记忆投毒与篡改 / Memory Poisoning & Tampering — 49
- **[tool-use-attack](#-tool-use-attack)** — 工具使用攻击 / Tool-Use Attacks — 134
- **[backdoor](#-backdoor)** — 后门与投毒攻击 / Backdoor & Poisoning Attacks — 455
- **[adversarial-attack](#-adversarial-attack)** — 对抗攻击 / Adversarial Attacks — 592
- **[privacy-leakage](#-privacy-leakage)** — 隐私泄露 / Privacy Leakage — 4083
- **[steganography](#-steganography)** — 隐写与隐蔽通信 / Steganography & Covert Communication — 64
- **[misuse](#-misuse)** — 滥用与误用 / Misuse & Abuse — 1009
- **[red-teaming](#-red-teaming)** — 红队测试 / Red Teaming — 123
- **[vulnerability](#-vulnerability)** — 漏洞与攻击面 / Vulnerabilities & Attack Surfaces — 3061
- **[defense](#-defense)** — 防御与防护方法 / Defense & Protection Methods — 2872
- **[alignment](#-alignment)** — 对齐与安全约束 / Alignment & Safety Constraints — 2672
- **[robustness](#-robustness)** — 鲁棒性与可靠性 / Robustness & Reliability — 2786
- **[watermark](#-watermark)** — 水印与溯源 / Watermarking & Provenance — 425
- **[unlearning](#-unlearning)** — 机器遗忘 / Machine Unlearning — 95
- **[agent-safety](#-agent-safety)** — Agent 安全框架 / Agent Safety Frameworks — 54
- **[benchmark](#-benchmark)** — 安全评测与基准 / Safety Benchmarks & Evaluation — 65
- **[survey](#-survey)** — 综述与系统化 / Surveys & Systematization — 342
- **[other](#-other)** — 其他安全相关 / Other Security-Related — 7588

## 📄 近期论文 / Recent Papers (Last 30 Days)

> 仅展示最近 30 天中最新的 500 篇论文（含日期、作者、摘要）。近 30 天共 3814 篇，完整 27635 篇论文列表请访问 [GitHub Pages](https://ny1024.github.io/AgentSafety-Papers/)

> Showing the latest 500 of 3814 papers from the last 30 days (with date, authors & abstract). For the full list of 27635 papers, visit [GitHub Pages](https://ny1024.github.io/AgentSafety-Papers/)

### 📂 jailbreak
*越狱攻击 / Jailbreak Attacks* — 3 papers

- **2026-09-14** — Mark Russinovich, Blake Bullwinkel, Giorgio Severi et al. — [Divide, Consult, Conquer: Capability Laundering Through Aligned LLMs](http://arxiv.org/abs/2609.15383v1)
  <details><summary>📄 Abstract</summary>
  Language model safety is typically evaluated one interaction at a time. We show that a weaker, unaligned model can split a harmful task into benign-looking subproblems, consult a stronger aligned model independently on each, and combine the answers locally. We call this attack capability laundering. Unlike a jailbreak, no single response is a harmful task. We measure consultation-aided uplift using tasks that a raw frontier model solves, the aligned frontier refuses, and the unassisted orchestra...
  </details>

- **2026-09-13** — Afshin Khadangi — [Another Blueprint In The Wall: How to Ask Frontier AI Like a Kid?](http://arxiv.org/abs/2609.14803v1)
  <details><summary>📄 Abstract</summary>
  This paper reports experiments across six frontier model types from OpenAI, Anthropic, xAI, and Google DeepMind. Ten independent sessions per model type used the same three stage prompt sequence, progressing from architectural preference to a full ASCII backbone. Under the school audience framing, responses repeatedly converged on a shared architectural pattern built around persistent latent state, adaptive computation, memory, specialist routing, verification, stopping control, and delayed deco...
  </details>

- **2026-09-13** — Mohd Azfar, Izhar Dad Khan — [SPARK: Representation-Level KV Memory Alignment for Safer Vision-Language Models](http://arxiv.org/abs/2609.14258v1)
  <details><summary>📄 Abstract</summary>
  Vision-language models (VLMs) remain vulnerable to jailbreaks that distribute harmful intent across text and images, making unimodal safety mechanisms insufficient. We investigate whether this vulnerability can be mitigated directly in the multimodal key-value (KV) memory formed during prefill, without modifying model parameters at inference time. We introduce SPARK, a two-stage framework for targeted KV-memory repair. Stage 1 uses a disposable diagnostic adapter to identify harm-associated dire...
  </details>


### 📂 prompt-injection
*提示注入攻击 / Prompt Injection Attacks* — 8 papers

- **2026-09-14** — Rakesh Kumar Surapani, Pradeep Kumar Dolabehera Kakitapelli, Arun Morampudi et al. — [Authorization Architectures for Tool-Using AI Agents](http://arxiv.org/abs/2609.15906v1)
  <details><summary>📄 Abstract</summary>
  Tool-using artificial intelligence (AI) agents, systems that autonomously invoke application programming interfaces (APIs), databases, browsers, and inter-agent protocols such as the Model Context Protocol (MCP), are becoming production infrastructure. Yet the security model governing when an agent is authorized to act on a human's behalf remains underdeveloped. Trustworthy human-AI systems require that every consequential agent action be traceable to a human principal, bounded by what that huma...
  </details>

- **2026-09-14** — Faruk Alpay, Taylan Alpay — [Approval Integrity and Recovery in LLM Answer Publication](http://arxiv.org/abs/2609.15576v1)
  <details><summary>📄 Abstract</summary>
  Publication integrity in LLM systems requires binding approved content to its current authorization context. We examine exact-content binding, authorization freshness and checkpoint recovery in Lightcap's publication enforcement mechanism. On 900 independently human-annotated RAGTruth responses from 150 source tasks, three dated Ministral models and a same-model direct-grounding baseline yield 3,600 assessments. The production response-act checker instantiated with 14B accepts 291 of 302 unsuppo...
  </details>

- **2026-09-14** — Yusuf Khalid Shire, Sang-Chul Kim — [PIDS-Bench: Evaluating Prompt-Injection Detectors Under Over-Defense, Obfuscation, and Distribution Shift](http://arxiv.org/abs/2609.15017v1)
  <details><summary>📄 Abstract</summary>
  Prompt-injection detectors are typically evaluated using aggregate F1 on in-distribution test data, which offers limited insight into behavior under distribution shift, particularly on the benign side of the decision boundary, where false positives impose direct operational cost yet are seldom measured. We present PIDS-Bench, a frozen multi-axis benchmark that jointly evaluates attack detection and benign false-positive behavior at fixed thresholds, spanning in-distribution inputs, hard-benign p...
  </details>

- **2026-09-14** — Bingzheng Wang, Xiaoyan Gu, Wentao Wang et al. — [ActGuard: Pre-execution Action Auditing against Indirect Prompt Injection in LLM Agents](http://arxiv.org/abs/2609.14987v1)
  <details><summary>📄 Abstract</summary>
  Large language model (LLM) agents interact with external environments through tool invocation, but tool outputs can also expose them to indirect prompt injection (IPI) attacks. Existing defenses mainly rely on prompt hardening, content filtering, pre-generated plans, or permission constraints. These approaches often struggle with complex tasks or over-sanitize external content, making it difficult to balance security and utility. The key challenge is therefore to preserve execution flexibility w...
  </details>

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


### 📂 tool-use-attack
*工具使用攻击 / Tool-Use Attacks* — 1 papers

- **2026-09-10** — Pingchen Lu, Xiangyi Wang, Xiang Li et al. — [COBRA-Skills: Contextual Bandit-Guided Evolution for Agent Skill Optimization](http://arxiv.org/abs/2609.11682v1)
  <details><summary>📄 Abstract</summary>
  Large language model (LLM) agents can benefit from reusable skills distilled from prior task experience, yet existing skill optimization methods often rely on costly execution-based evaluation and substantial task data. We introduce \textbf{COBRA-Skills}, an efficient framework that formulates skill optimization as budgeted sequential optimization over a dynamically evolving candidate space. COBRA-Skills couples contextual-bandit-guided prioritization with evidence-grounded skill evolution, sele...
  </details>


### 📂 backdoor
*后门与投毒攻击 / Backdoor & Poisoning Attacks* — 6 papers

- **2026-09-14** — Roberto Riaño, Gorka Abad, Stjepan Picek et al. — [When the World Lies: Backdoor Attacks on Latent World Models for Downstream Control](http://arxiv.org/abs/2609.15781v1)
  <details><summary>📄 Abstract</summary>
  Pretrained world models, learned simulators that encode an observation into a latent state and predict how it evolves under actions, are beginning to be reused as off-the-shelf dynamics backbones for control, like pretrained encoders and language models are reused today. We show that this reuse opens a supply-chain backdoor: an adversary who controls only a released checkpoint can hijack the downstream controller, even though the victim trains and evaluates entirely on clean data and never sees ...
  </details>

- **2026-09-14** — Aashiq Muhamed, Mona T. Diab, Virginia Smith et al. — [Pick Your Poison: Learning to Select Poison Sets for Stronger LLM Backdoor Attacks](http://arxiv.org/abs/2609.15029v1)
  <details><summary>📄 Abstract</summary>
  Backdoor poisoning attacks add poisoned examples to otherwise-clean finetuning data, pairing a trigger with a target behavior that the model learns to produce when the trigger appears. Existing evaluations typically fix the number of poisoned examples and sample them at random from a candidate pool. We show that this can severely underestimate worst-case vulnerability: across three LLaMA-3-8B backdoor settings, holding the model, clean data, and poison count fixed, attack success ranges from 3% ...
  </details>

- **2026-09-13** — Xue Tan, Changhui Wang, Sanrui Yang et al. — [Detecting and Localizing Segment-Level Poisoning in Multi-Source LLM-Agent Inputs](http://arxiv.org/abs/2609.14723v1)
  <details><summary>📄 Abstract</summary>
  Modern large language model (LLM) agents often construct prompts by aggregating retrieved passages, user reviews, and documents from multiple external sources. This paradigm exposes them to segment-level poisoning attacks, in which an adversary controlling only a small subset of sources injects malicious content to manipulate model outputs. Existing defenses mainly rely on textual patterns, external embeddings, or auxiliary detectors and may therefore fail against fluent, semantically plausible ...
  </details>

- **2026-09-13** — Xue Tan, Xuandi Zeng, Yu Shao et al. — [ViTeGate: Visual-Textual Triggered Knowledge Poisoning for Vision-Language Retrieval-Augmented Generation](http://arxiv.org/abs/2609.14685v1)
  <details><summary>📄 Abstract</summary>
  Modern Vision-Language Retrieval-Augmented Generation (VLRAG) systems augment Large Vision-Language Models (LVLMs) with retrieved visual and textual evidence, enabling responses grounded in external knowledge. However, the retrieval pipeline also creates an attack surface: adversaries can inject poisoned image-text pairs into the knowledge corpus to influence model outputs. Existing knowledge poisoning attacks are typically always-on, allowing poisoned evidence to affect generation whenever it i...
  </details>

- **2026-09-10** — Rui Wen, Ahmed Salem, Andrew Paverd et al. — [SpecGuard: Inference-Time Backdoor Detection For Free](http://arxiv.org/abs/2609.11799v1)
  <details><summary>📄 Abstract</summary>
  Large language models are often fine-tuned, shared, or downloaded from third parties, so a deployed model may carry a hidden backdoor that behaves normally on benign inputs but switches to attacker-controlled behavior when a secret trigger appears. While backdoors can be audited before deployment, runtime monitoring remains important for models that are frequently updated. The challenge is that LLM serving is latency-sensitive: existing inference-time detectors either rely on assumptions about t...
  </details>

- **2026-09-10** — Haozhe Lu, Jiaqi Li, Xinyuan Zhu et al. — [ToxicRAG: Compromising Retrieval-Augmented Generation Systems via Single-Shot Knowledge Poisoning Attacks](http://arxiv.org/abs/2609.11082v1)
  <details><summary>📄 Abstract</summary>
  Retrieval-Augmented Generation (RAG) can ground large language model (LLM) outputs in external evidence, but it also exposes the system to knowledge poisoning. Representative attacks use multiple injected documents or templates that directly assert a target answer. We present ToxicRAG, a one-document-per-target attack that expresses misinformation as a coherent knowledge-update narrative. The generated document first acknowledges the previously accepted answer, introduces fabricated events that ...
  </details>


### 📂 adversarial-attack
*对抗攻击 / Adversarial Attacks* — 4 papers

- **2026-09-14** — Fares Trad, Simin Chen, Hung Viet Pham et al. — [Adversarial Testing of Automated Program Repair Agents for Security Vulnerabilities](http://arxiv.org/abs/2609.15963v1)
  <details><summary>📄 Abstract</summary>
  Software agents with Large Language Models (LLMs) are designed for Automated Program Repair (APR) tasks, raising the possibility that, in the near future, APR agents will fix bugs automatically without much human intervention. Can we trust an APR agent to produce both functionally correct and secure code in such situations? What if attackers target production APR agents with adversarial issues that seem benign but may influence the agents to produce correct but insecure code? In this paper, we t...
  </details>

- **2026-09-14** — Paul Stahlhofen, Luca Hermes, Tim Kochs et al. — [Admissable: Training Reinforcement Learning Agents against Adversarial Missingness](http://arxiv.org/abs/2609.15297v1)
  <details><summary>📄 Abstract</summary>
  In order to make Reinforcement Learning algorithms applicable in real world scenarios, safety must be ensured even under adverse operating conditions. In this work, we consider the challenge of adversarial feature missingness: a scenario in which an adversary occludes features from the agent's observation in order to reduce performance as much as possible. We formally define adversarial missingness for Reinforcement Learning and compare it to the related concepts of $\ell_\infty$-norm bounded ad...
  </details>

- **2026-09-13** —  Sergei,  Komarov — [Graph-Transformer Fraud Detection with Self-Supervised Pretraining and Conformal Risk Control](http://arxiv.org/abs/2609.14234v1)
  <details><summary>📄 Abstract</summary>
  Financial fraud in corporate transaction networks has grown more coordinated and harder to detect with rule-based engines and with classical learning models that treat each transaction in isolation. This paper presents GTFD, a graph-transformer fraud detector that fuses structural and temporal evidence from a corporation's payment graph. GTFD encodes the graph with a multi-head graph attention network, encodes ordered transaction sequences with a gated transformer, and combines both views throug...
  </details>

- **2026-09-09** — Tong Li, Saunak Kumar Panda, Yisha Xiang — [Certifying Lower Bounds for Risk-Sensitive Reinforcement Learning under Adversarial State Perturbations](http://arxiv.org/abs/2609.10866v1)
  <details><summary>📄 Abstract</summary>
  Reinforcement learning (RL) agents deployed in real-world environments are often vulnerable to adversarial perturbations in state observations, creating risks in safety-critical applications. Certification methods can improve robustness against adversarial perturbations by providing lower bounds on expected cumulative rewards. Existing certification methods, however, mainly focus on risk-neutral objectives. In this paper, we extend certification methods to risk-sensitive objectives by establishi...
  </details>


### 📂 privacy-leakage
*隐私泄露 / Privacy Leakage* — 43 papers

- **2026-09-14** — Md Khalid Syfullah, Alvi Ataur Khalil — [Don't Send What You Don't Need: Question-Guided Token Pruning as a Privacy Defense for Vision-Language Models](http://arxiv.org/abs/2609.15671v1)
  <details><summary>📄 Abstract</summary>
  Visual Question Answering (VQA) with Vision-Language Models (VLMs) is increasingly used in privacy-sensitive and bandwidth-constrained settings. Federated Learning (FL), Split Learning (SL), and U-Shaped Split Learning (USL) keep raw data local, but transmitting all visual tokens across a model partition remains costly and can expose private information. We propose QPriv-VL, a question-guided, privacy-aware token-pruning framework for FL, SL, and USL that prunes visual tokens before transmission...
  </details>

- **2026-09-14** — Pengwei Wang, Zihan Wang, Hangcheng Cao et al. — [CounterPersona: Append-Only Defense Against Unauthorized Persona Skill Distillation](http://arxiv.org/abs/2609.15097v1)
  <details><summary>📄 Abstract</summary>
  Persona skill distillation can extract recurring patterns from personal information and encode them into reusable skills, enabling AI systems to closely replicate an individual's behavior. However, such replication also raises serious concerns regarding personal privacy and labor autonomy. Unlike existing perturbation-based defenses that require individuals to modify their data before collection, once historical records are collected by an attacker, they can no longer be altered, sanitized, or r...
  </details>

- **2026-09-14** — Shashie Dilhara Batan Arachchige, Robin Carpentier, Hassan Jameel Asghar et al. — [SpliTEE: Improving LLM Inference on Trusted Hardware with Differentially Private GPU Outsourcing](http://arxiv.org/abs/2609.15039v1)
  <details><summary>📄 Abstract</summary>
  User prompts provided to large language models (LLMs) may contain sensitive or private information that can be misused by remotely deployed models, such as through inadvertent memorization during retraining. One way to protect user prompts is to execute the LLM inside a trusted execution environment (TEE), with the guarantee that the service provider has no access to computations performed within or information exchanged with the TEE. However, current TEEs are primarily CPU-based and significant...
  </details>

- **2026-09-14** — Wen Hu, Ya Yu, Xutong Wang — [Reversibility-Verified De-identification for Cloud-Local LLM Inference: A Locally Certified Dehydrate-Rehydrate Loop with Layered Assurance (DR-SL)](http://arxiv.org/abs/2609.14883v1)
  <details><summary>📄 Abstract</summary>
  Cloud-local LLM inference must keep sensitive user data on-device while exploiting cloud-grade reasoning, yet existing sanitization approaches (placeholder substitution, differential-privacy perturbation, and skill distillation) lack a release decision that is simultaneously safe and utility-preserving. We propose DR-SL (Dehydrate-Rehydrate with Self-Learning loop), which formalizes de-identification completeness as two measurable conditions: de-identification sufficiency under Pufferfish semant...
  </details>

- **2026-09-14** — Paul-Gabriel Nicolae, Irina Georgiana Mocanu — [Anatomical Grounding and Leakage-Aware Multimodal Contrastive Learning for Alzheimer's Disease Classification from Structural MRI](http://arxiv.org/abs/2609.15888v1)
  <details><summary>📄 Abstract</summary>
  Deep networks trained on structural MRI for Alzheimer's disease (AD) staging often reach reasonable accuracy while attending to anatomically irrelevant regions, and multimodal models that add clinical tables frequently rely on variables that were used to assign the diagnostic label in the first place. We study both issues with a deliberately lightweight slice-based encoder (ResNet18 with a one-layer Transformer over slices) on 1,075 baseline T1-weighted scans from ADNI-1. First, we use FastSurfe...
  </details>

- **2026-09-14** — Wenxin Xu, Jinwei Lu, Hwanhee Kim et al. — [VisInteract: Towards Dynamic Interactive Text-to-Visualization under Imperfect Queries](http://arxiv.org/abs/2609.15182v1)
  <details><summary>📄 Abstract</summary>
  Real-world visualization requests are routinely ambiguous, incomplete, or factually incorrect, yet existing Text-to-Visualization (Text-to-Vis) systems assume well-specified inputs and produce charts in a single pass. When queries are imperfect, a system must \emph{interact} with the user to recover the true intent, but no benchmark or method supports this dynamic process. We introduce \textbf{VisInteract}, a new paradigm that reframes Text-to-Vis as interaction-driven intent recovery, and \text...
  </details>

- **2026-09-14** — Md Khalid Syfullah, Alvi Ataur Khalil — [LLM-Based Schema-Aware Split Learning for Privacy-Preserving Mental Distress Prediction Across Heterogeneous Surveys](http://arxiv.org/abs/2609.15871v1)
  <details><summary>📄 Abstract</summary>
  Rising societal and lifestyle complexity has been linked to a growing prevalence of mental distress worldwide. Educational institutions, workplaces, clinics, etc. collect large volumes of mental health survey data to understand and reduce this burden. Collaborative analysis of such data could yield effective generalizable predictive models. Privacy constraints and varied survey designs (i.e., different questions, scales, and formats) hinder direct integration. We propose a schema-aware split lea...
  </details>

- **2026-09-14** — Jigang Duan, Heran Wang, Ligen Shi et al. — [TRACE: Two-Stage Detector-Response Estimation With Angular Cosine Expansion for Ring Artifact Correction in Photon-Counting CT](http://arxiv.org/abs/2609.15834v1)
  <details><summary>📄 Abstract</summary>
  Detector response nonuniformity introduces systematic projection errors and ring artifacts in photon-counting detector computed tomography (PCD-CT). In measured PCD-CT data, residual stripe amplitudes vary slowly with projection angle, which fixed-bias models cannot adequately capture. We propose TRACE, a two-stage unsupervised sinogram decomposition method for estimating and correcting these response-related errors. TRACE represents stripes as a fixed bias plus low-order discrete cosine transfo...
  </details>

- **2026-09-14** — R. Oguz Araz, Xavier Lizarraga, Xavier Serra et al. — [Building a Dataset for Music Sample Identification](http://arxiv.org/abs/2609.15465v1)
  <details><summary>📄 Abstract</summary>
  Sample identification (SI) is the task of matching an element of a musical work to its musically transformed versions used to create new works. The task has received little attention and lacks large-scale publicly available data. In this work, we mine sampling annotations from a music database and split them for training and evaluation. The resulting dataset is nearly three orders of magnitude larger than the existing SI benchmarks, with training, validation, and test sets of 114 k, 6 k, and 10 ...
  </details>

- **2026-09-14** — Max Dupré la Tour — [Differentially Private Multicolor Discrepancy and Fair Division of Indivisible Goods](http://arxiv.org/abs/2609.15372v1)
  <details><summary>📄 Abstract</summary>
  We study the fair division of indivisible goods under pure differential privacy, continuing the line of work initiated by Manurangsi and Suksompong. For $n$ agents with nonnegative additive utilities over $m$ goods and a fixed privacy parameter, we give an entry-private algorithm that, with high probability, achieves consensus envy-freeness up to $O(\sqrt n+\log^3 m)$ goods. This substantially improves the dependence on $n$ over the previous $O(n\log m)$ guarantee for ordinary envy-freeness, whi...
  </details>

- **2026-09-14** — Jianhua Jiang, Dongbo Yuan, Weihua Li — [MemRiskBench: Trace-Aware Risk-Preserving Evaluation for Long-Horizon LLM Agents](http://arxiv.org/abs/2609.14976v1)
  <details><summary>📄 Abstract</summary>
  Long-horizon LLM agents accumulate memory across sessions, creating sparse but high-impact risks: stale facts, conflicting updates, cross-user leakage, revoked-memory reuse, and constraint decay. Standard aggregate scores hide per-risk failure rates--a model achieving 78% average accuracy may still leak data in 4% of episodes--and benchmark compression preferentially discards the rare high-severity events that distinguish a mostly-working model from one that occasionally causes harm. We present ...
  </details>

- **2026-09-13** — Tan Xue, Huo Chang, Wang Changhui et al. — [CIG-MIA: Context-Induced Information Gain Membership Inference Attacks against Retrieval-Augmented Generation](http://arxiv.org/abs/2609.14649v1)
  <details><summary>📄 Abstract</summary>
  Retrieval-augmented generation (RAG) systems ground large language models on external knowledge bases, enabling access to private, domain-specific, and up-to-date knowledge without retraining. However, the same retrieval interface can expose whether a candidate document is contained in the knowledge base. This paper studies knowledge base membership inference against RAG systems under both gray-box and text-only black-box access. Existing RAG membership inference attacks rely on signals such as ...
  </details>

- **2026-09-13** — Murat Kantarcioglu — [AI Deployment Accountability Engineering: A Vision for Accountable AI in Safety-Critical Socio-Technical Systems](http://arxiv.org/abs/2609.14592v1)
  <details><summary>📄 Abstract</summary>
  Artificial intelligence systems are rapidly becoming critical components in healthcare, finance, public services, and other safety-critical domains. Yet the engineering practices used to evaluate these systems remain predominantly model-centric, emphasizing properties such as accuracy, robustness, fairness, and interpretability before deployment. These properties are necessary but insufficient once an AI system operates within an ever changing socio-technical environment characterized by distrib...
  </details>

- **2026-09-13** — Myra Cheng, Lujain Ibrahim, Grace Liu et al. — [LLMs as Oracles: Reliance on LLMs for Subjective Personal Questions](http://arxiv.org/abs/2609.14849v1)
  <details><summary>📄 Abstract</summary>
  We characterize how people are turning to LLMs as oracles: all-knowing authorities on subjective personal questions. Motivated by risks to users' autonomy and well-being, we develop a typology and LLM-based methods to measure this form of AI reliance at scale and understand how people are offloading judgment and decision-making to AI. Applying our typology to public usage data (68K prompts from WildChat and ThoughtTrace), we find that LLM-as-oracle use has increased over time (2023-2026) and is ...
  </details>

- **2026-09-13** — Erkan Bayram, Mohamed-Ali Belabbas, Tamer Başar — [Privacy Preserving Gossip Learning](http://arxiv.org/abs/2609.14778v1)
  <details><summary>📄 Abstract</summary>
  We propose a decentralized privacy-preserving learning algorithm in which each agent holds a single private sample and a shared model. Samples are learned sequentially, and each update must preserve the endpoint mappings at previously learned samples while protecting private data. This gives each agent three roles: (i) a learner that updates the model parameters, (ii) a teacher whose sample is learned at the current iteration, and (iii) a protected agent whose sample has already been learned. We...
  </details>

- **2026-09-13** — Rohit Patel, Susil Kumar Mohanty, Jeenal Chaudhary — [TriCalRAG: A Three-Strategy, Retrieval-Augmented Benchmark for On-Premise LLM-Based Root Cause Analysis in AIOps](http://arxiv.org/abs/2609.14762v1)
  <details><summary>📄 Abstract</summary>
  Cloud-hosted large language models (LLMs) are increasingly used for root cause analysis (RCA) in AIOps pipelines, but they introduce data privacy risk, network latency, and per-query cost that scale poorly with production log volumes. We present TriCalRAG, a benchmark evaluating open-weight LLMs served locally via vLLM on a single high-memory workstation GPU (NVIDIA RTX PRO 6000, 96GB) against a classical LSTM-based log anomaly detector (DeepLog), across four real, publicly available log dataset...
  </details>

- **2026-09-13** — S M Mehedi Zaman, Md Mozammel Hoque — [Vulnerabilities in Personalization: Assessing Health Privacy Risks in ChatGPT Logs and Memory](http://arxiv.org/abs/2609.14697v1)
  <details><summary>📄 Abstract</summary>
  As conversational LLMs become deeply embedded in daily life, users frequently disclose sensitive personal health information during routine interactions. We present a large-scale computational audit analyzing 179,057 conversations across India, Nigeria, Brazil, and Pakistan (N = 1,057) to evaluate personal health disclosures and background memory synthesis in ChatGPT. We find that 21.31% of audited conversations contain personal health data, with 3.62% posing high-to-extreme privacy risks involv...
  </details>

- **2026-09-13** — He Zhang, Siyu Yuan, Siyu Liu et al. — [EdgeHAR: An Edge-Native Compact Sensor Foundation Model for Human Activity Recognition](http://arxiv.org/abs/2609.14498v1)
  <details><summary>📄 Abstract</summary>
  Sensor-based human activity recognition (HAR) is fundamental to ubiquitous and wearable computing, yet existing foundation models are largely designed for cloud-scale deployment and struggle with real-world sensing shifts, including unseen users, devices, sampling rates, and sensor placements. We present \textbf{EdgeHAR}, an edge-native compact sensor foundation model designed for wearable intelligence. Unlike conventional models that entangle activity knowledge with acquisition variations, Edge...
  </details>

- **2026-09-13** — Leon Fernando, C Dombawala, P. Hettigoda et al. — [A Generative AI Integrated Multimodal Framework for Low-Latency Multi-Camera Person Re-Identification](http://arxiv.org/abs/2609.14419v1)
  <details><summary>📄 Abstract</summary>
  Person re-identification (ReID) is essential for multi-camera surveillance and tracking, yet remains difficult due to viewpoint and illumination changes, occlusion, background clutter, and low resolution imagery. We propose a generative AI integrated multimodal ReID framework designed explicitly for robustness under missing cues and low latency deployment. The key idea is a cost aware early-exit cascade that prioritizes inexpensive, high confidence evidence and only triggers expensive modalities...
  </details>

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


### 📂 misuse
*滥用与误用 / Misuse & Abuse* — 10 papers

- **2026-09-14** — Keertana Chidambaram, Andrew Ilyas, Vasilis Syrgkanis — [Corrupt Plans, Clean Traces: Evading Chain-of-Thought Monitoring with Plan Injection](http://arxiv.org/abs/2609.15989v1)
  <details><summary>📄 Abstract</summary>
  Chain-of-thought (CoT) monitoring is a safety strategy where the reasoning of a large language model "actor" is inspected by a "monitor" (often another language model) for signs of unsafe planning, deception, or misalignment. We find that planting harmful but benign-sounding reasoning in the actor's context can steer it to perform adversarial actions while evading monitors, an attack we term "plan injection". We initially discover this attack in the multiple-choice question-answering monitorabil...
  </details>

- **2026-09-14** — Laura M. Vowels, Matthew J. Vowels, Shivali Sharma et al. — [K-Bench: a clinically calibrated benchmark for evaluating large language models in high-risk mental health conversations](http://arxiv.org/abs/2609.15855v1)
  <details><summary>📄 Abstract</summary>
  % !TEX root = ../main.tex People increasingly use large language models (LLMs) for mental health support, yet their safety in evolving, high-risk conversations remains poorly characterised. We developed K-Bench, a clinician-calibrated, protected benchmark evaluating 125 model configurations representing 33 base models from 14 providers across a fixed cohort of 200 multi-turn vignettes involving suicide, self-harm, domestic violence, substance misuse, and no-risk presentations. Synthetic patient ...
  </details>

- **2026-09-14** — Mohammed Ahnouch, Lotfi Elaachack — [Semantic Fibers and Cross-Gram Interference: A Calculus of Safety Drift in Overcomplete Representations](http://arxiv.org/abs/2609.14861v1)
  <details><summary>📄 Abstract</summary>
  A deployed language model may refuse a harmful request in English yet comply with its faithful translation, revealing a cross-lingual safety failure that cannot be characterized reliably by output behavior alone. We formalize this phenomenon through an audited equivalence relation and show that, for a declared quotient, representation, metric, feature dictionary, scoring head, threshold, and contrast model, the resulting safety drift admits an exact linear-algebraic characterization. Specificall...
  </details>

- **2026-09-13** — Orion Reblitz-Richardson — [Refusal Reads Only a Slice of What the Model Knows: Harm-Keyed Routing and Its Exceptions Across Model Families](http://arxiv.org/abs/2609.14759v1)
  <details><summary>📄 Abstract</summary>
  Alignment applied after pretraining is shallow in a measurable way: a single direction in a model's residual stream can be edited out, and the model stops refusing harmful requests. That fact says how easily refusal can be removed, not what the refusal decision was reading in the first place. We ask what it reads, and we separate that from what the model comprehends. Across four open-weight models spanning three families, moral comprehension is native to pretraining: a low-rank moral subspace cr...
  </details>

- **2026-09-13** — Ziyi Zhu, Daniel R. Cahn, Thomas D. Hull et al. — [Optimizing Sparse Outcomes Through Dense Behavioral Signals via Value-Guided Preference Distillation](http://arxiv.org/abs/2609.14648v1)
  <details><summary>📄 Abstract</summary>
  Aligning multi-turn dialogue agents is usually framed as matching turn-level human preferences, yet direct optimization of long-term outcomes is often ineffective and prone to reward hacking. We formulate long-horizon dialogue optimization as a multi-objective reinforcement learning problem and train a multi-head value model that predicts a vector of observed user behaviors across multiple look-ahead horizons. Our findings demonstrate that a scalarized composite of dense auxiliary behavioral sig...
  </details>

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


### 📂 red-teaming
*红队测试 / Red Teaming* — 1 papers

- **2026-09-09** — Arnab Chattopadhayay, Debdipta Halder — [Belief-State Engine: Augmenting LLMs for Principled Planning Under Partial Observability](http://arxiv.org/abs/2609.10036v1)
  <details><summary>📄 Abstract</summary>
  Large language model agents produce fluent action sequences across a wide range of tasks, yet they fail in characteristic ways once the environment becomes partially observable. Ambiguous feedback pushes them into premature commitments. A single informative observation can collapse their uncertainty onto the wrong hypothesis. Policies drift as the history grows. We trace these symptoms to a common structural cause. An LLM agent, as commonly deployed, is a history-conditioned policy with no expli...
  </details>


### 📂 vulnerability
*漏洞与攻击面 / Vulnerabilities & Attack Surfaces* — 55 papers

- **2026-09-14** — Aman Priyanshu, Supriti Vijay, Kimia Majd et al. — [Vulnerability Localization Benchmark: Measuring Agentic Security Analysis at Repository Scale](http://arxiv.org/abs/2609.15939v1)
  <details><summary>📄 Abstract</summary>
  Language-model agents increasingly operate over complete software repositories, yet cybersecurity evaluations primarily measure whether they can detect, reproduce, or repair vulnerabilities rather than whether they can locate the relevant code. We study vulnerability localization: given a weakness class and an unfamiliar repository, identify the implementation files associated with that weakness. We introduce the Vulnerability Localization Benchmark (VLoc Bench), comprising 500 real world vulner...
  </details>

- **2026-09-14** — Theodoros Moutesidis — [The Model Proposes, the Code Disposes: A Pre-Registered Ablation of a Verifier-and-Acceptance Stage in an LLM-Orchestrated Offensive-Security Agent](http://arxiv.org/abs/2609.15887v1)
  <details><summary>📄 Abstract</summary>
  We evaluate whether a verifier-and-acceptance stage - a model verifier whose verdicts are enforced by deterministic code - changes what an LLM-driven offensive-security agent reports. We report a 15-run exploratory pilot, a pre-registered 20-run confirmatory ablation, and a pre-registered 2 x 2 factorial study with 40 runs across two deliberately vulnerable lab targets. In the confirmatory study, removing the stage eliminated pre-report suppression (median 2 versus 0 findings per run; exact one-...
  </details>

- **2026-09-14** — Mingkai Liu, Hao Zhao, Xingxing Zuo — [SURE-Map: Self-Correcting Streaming Geometric Foundation Model](http://arxiv.org/abs/2609.15795v1)
  <details><summary>📄 Abstract</summary>
  Streaming geometric foundation models are emerging as a compelling alternative to SLAM systems. Yet this streaming nature introduces a fundamental issue: each prediction is made from limited context, which is vulnerable to dynamic objects and weak textures. Small local errors accumulate into severe geometric distortion and long-horizon scale drift. We argue that reliable streaming reconstruction requires geometric foundation models to be not only predictive, but also self-correcting. We introduc...
  </details>

- **2026-09-14** — Guo Fuzheng — [CiteShade: Citation Laundering in Multi-Source Retrieval-Augmented Generation and Its Counterfactual Defense](http://arxiv.org/abs/2609.15660v1)
  <details><summary>📄 Abstract</summary>
  Retrieval-augmented generation (RAG) grounds a language model's answers on retrieved external knowledge and returns each answer with citations that identify its sources. Those citations are the user's audit trail: they let a reader verify a claim without trusting the model. Prior security work on RAG asks whether an attacker can corrupt the answer, leaving the citation channel unexplored. We show that this channel is a new and practical attack surface. We propose CiteShade, the first citation la...
  </details>

- **2026-09-14** — Oliver Stevanovic, Jasmin Wachter — [Automating Attack Graph Construction for Agentic Pentesting. Towards Neuro-Symbolic Vulnerability Hunting](http://arxiv.org/abs/2609.15523v1)
  <details><summary>📄 Abstract</summary>
  Logic attack graphs grounded in scanner output provide explicit and auditable attack path reasoning LLM-based agents lack. Integrating symbolic frameworks such as MulVAL to contemporary security workflows or agentic pipelines, however, requires translating scanner evidence to initial facts, and creating domain-specific rules. We present a semi-automated pipeline that addresses this interoperability problem and depict its feasibility in a web-security case study. Our pipeline parses findings from...
  </details>

- **2026-09-14** — Tianyi Li, Simon Geirnaert, Bert De Smedt et al. — [Multiscale Gaussian-Mixture Modeling for HMM Post-Processing in Selective Auditory Attention Decoding](http://arxiv.org/abs/2609.15490v1)
  <details><summary>📄 Abstract</summary>
  Selective auditory attention decoding (sAAD) infers from electroencephalography (EEG) which speaker a listener attends to in multi-speaker scenarios. A widely used approach reconstructs the attended speech envelope from EEG, correlates it with candidate envelopes, and selects the speaker with the highest Pearson correlation. However, correlations in each decision window have high intrinsic variance, making per-window decisions unreliable, especially for short windows. Recent work introduced a hi...
  </details>

- **2026-09-14** — Satoshi Nakano, Kazuhiko Nishimura — [Endogenous supply-chain transformation via dynamically calibrated nonneutroelastic processing networks](http://arxiv.org/abs/2609.15452v1)
  <details><summary>📄 Abstract</summary>
  Understanding how supply chains endogenously transform requires a parametric model of processing networks with non-neutral substitution elasticities. While the Cascaded CES (CCES) production function provides a rigorous framework for these multi-layered linkages, dynamically calibrating its structural parameters from time-series data constitutes a highly non-convex inverse optimization problem. Enforcing the strict microeconomic concavity constraint causes standard monolithic approach to fail du...
  </details>

- **2026-09-14** — Halil Burak Noyan — [Empirical Evaluation of Task-Based Permission Scoping Architecture for AI Agents](http://arxiv.org/abs/2609.15422v1)
  <details><summary>📄 Abstract</summary>
  AI agents are provisioned the same as employee-owned hosts in many enterprise settings with a static credential set fixed at deployment which includes all permissions the employee role might ever need. Role-based access control made this compromise for human principals because scoping access per task was infeasible. For AI agents, the compromise leaves every credential standing exposed whether or not the current task uses them. These permissions can later be utilised by a compromised or misalign...
  </details>

- **2026-09-14** — Christian Fisch, Angela Altmeier, Martin Obschonka et al. — [Artificial entrepreneurial cognition: Locating and causally steering an opportunity recognition dial inside large language models (LLMs)](http://arxiv.org/abs/2609.15277v1)
  <details><summary>📄 Abstract</summary>
  Entrepreneurial cognition is a foundation of entrepreneurship research. Yet the growing involvement of large language models (LLMs) in entrepreneurial work extends the cognition question beyond human actors to systems whose internal representations remain largely unexplored. We introduce artificial entrepreneurial cognition, the functional organisation of entrepreneurship-relevant representations and computations inside artificial intelligence (AI) systems. We bring mechanistic interpretability ...
  </details>

- **2026-09-14** — Yang Chen, Lirong Che, Zhenyu Huang et al. — [HarnessVLN: Unifying Training-Free Embodied Navigation through an Agent Harness](http://arxiv.org/abs/2609.15195v1)
  <details><summary>📄 Abstract</summary>
  Embodied navigation requires agents to interpret visual observations, accumulate spatial knowledge, and execute actions to follow instructions or locate objects. Training-based methods face generalization challenges, while training-free methods exploit multimodal large language models (MLLMs) but often lack mechanisms to reconcile proposed actions with spatial evidence, task progress, and execution failures. We present HarnessVLN, a zero-shot, training-free framework whose Agent Harness coordina...
  </details>

- **2026-09-14** — Yuyao Sun, Tao Deng, Shuang Li et al. — [AdaVSkip: Adaptive Visual Token Skipping Across Layers For Efficient MLLMs Inference](http://arxiv.org/abs/2609.15131v1)
  <details><summary>📄 Abstract</summary>
  Multimodal large language models (MLLMs) require substantial computation to process numerous visual tokens across all transformer layers. Most methods for efficient MLLM inference exploit horizontal redundancy by compressing visual tokens. Beyond token reduction, recent studies exploit vertical redundancy through early exit or fixed-layer skipping. However, we find that the extent and distribution of this redundancy vary across inputs and differ between self-attention and MLP modules. Motivated ...
  </details>

- **2026-09-14** — Shuhao Han, Wenjie Liao, Hayden Vance et al. — [DNF-SR: Dual-Input and Negative-Aware Feature Fine-Tuning for Real-World Image Super-Resolution](http://arxiv.org/abs/2609.15120v1)
  <details><summary>📄 Abstract</summary>
  Benefiting from the powerful generative priors of diffusion models, diffusion-based real-world image super-resolution (Real-ISR) methods have demonstrated impressive performance.To achieve efficient Real-ISR, several recent works have designed one-step diffusion-based models.Howerver, unmediatedly feeding LR into a diffusion model creates a distributional gap with the model's original input.A straightforward approach to reduce the distribution gap is to introduce noise to the LR latents. However...
  </details>

- **2026-09-14** — Yi Chen, Rufeng Cheng, Qiang Xie et al. — [Generate to Explore, Select to Exploit: Aligning LLM-based Headline Generation with Personalized Recommendation](http://arxiv.org/abs/2609.15094v1)
  <details><summary>📄 Abstract</summary>
  In industrial recommendation feeds, presenting a static headline for an item often fails to satisfy the diverse, multimodal interests of the user population, particularly suppressing the needs of long-tail audiences. While Large Language Models (LLMs) have been integrated into recommendation for content understanding or ranking, directly optimizing them to output a single best headline typically leads to mode collapse---converging to generic patterns that satisfy average tastes but miss specific...
  </details>

- **2026-09-14** — Xu He, Chih-Hsuan Lin, Hung-Mao Chen et al. — [Overflip: Repetition-Induced Label Flips in Guardrail Models](http://arxiv.org/abs/2609.15013v1)
  <details><summary>📄 Abstract</summary>
  Guardrail models are classifiers deployed to screen malicious prompts and responses in LLM-based services. To meet latency constraints, many lightweight guardrails adopt compact Transformer backbones (e.g., DeBERTa) that are trained with short context windows (typically 512 tokens) and rely on bucketed relative positional encodings to process longer inputs. Prior evaluations assume that a guardrail's decision is stable as the input is lengthened. We show that this assumption can fail. We identif...
  </details>

- **2026-09-13** — Jacques Peyrière — [Fast tensor transforms and ring-valued orthogonal matrices: an application to cryptography](http://arxiv.org/abs/2609.14782v1)
  <details><summary>📄 Abstract</summary>
  We present a generalization of the Fast Fourier and fast Walsh   transform algorithms to tensor products of $n$ arbitrary $q\times q$   matrices over a commutative ring, reducing the cost of applying such   a tensor product from $q^{2n}$ to $nq^{n}$ ring operations. We then   give an explicit construction of square orthogonal matrices over a   commutative unitary ring, starting from a prescribed first row, and   specialize this construction to ${\mathbb Z}/256{\mathbb   Z}$. Combining these two ...
  </details>

- **2026-09-13** — Maoliang Li, Hailong Zou, Taohong Han et al. — [BigMoMo: Efficient Inference of Large-Scale MoE with Speculative Decoding on Mobile Devices](http://arxiv.org/abs/2609.14643v1)
  <details><summary>📄 Abstract</summary>
  Mixture-of-Experts (MoE) models expand language model capacity on smartphones, but expert offloading remains constrained by limited DRAM capacity and costly data movement. Sequential token routing couples expert execution to fragmented flash reads and multistage NPU preparation, leaving sparse computation stalled on weight transfers. Each transfer serves few tokens before execution moves on. We exploit the multi-token verification window of speculative decoding to decouple expert movement from s...
  </details>

- **2026-09-13** — Juanen Li, Peng Qian, Guanyan Li et al. — [EchoFuzz: Empowering Smart Contract Fuzzing with Large Language Models](http://arxiv.org/abs/2609.14475v1)
  <details><summary>📄 Abstract</summary>
  Smart contracts, serving as the cornerstone of decentralized applications, autonomously manage trillion-dollar digital assets, making them attractive targets for attacks. Fuzzing has emerged as a promising technique for detecting vulnerabilities in smart contracts, yet existing methods face two main challenges. (1) The logical gap in state transitions and combinatorial redundancy hinders effective tradeoffs between bug detection efficiency and state space exploration cost, leading to critical ex...
  </details>

- **2026-09-13** — Hongliu Cao — [Policy Loopholes in Agent Evaluation: When Policy Ambiguity Masquerades as Agent Error](http://arxiv.org/abs/2609.14400v1)
  <details><summary>📄 Abstract</summary>
  Agent benchmarks evaluate policy compliance but assume each policy determines a unique correct action. Natural-language policies can violate this assumption through silence, ambiguity, or contradiction, admitting multiple defensible readings that a single gold trajectory cannot capture. Auditing two $τ^2$-bench domains, we develop a taxonomy of such policy loopholes and show that affected tasks produce unreliable scores: they lower scores across different models in different ways and make every ...
  </details>

- **2026-09-13** — Zhuojin Li, Marco Paolieri, Leana Golubchik — [Partition-Aware Scheduling for Mobile Heterogeneous Inference Co-Execution](http://arxiv.org/abs/2609.14213v1)
  <details><summary>📄 Abstract</summary>
  Modern mobile inference runs on heterogeneous platforms combining mobile GPUs with multiple CPU core clusters. Existing optimizations typically exploit either inter-operator parallelism, by assigning entire operators to CPU cores or to the GPU, or intra-operator parallelism, by partitioning each operator for CPU-GPU co-execution. We consider these two forms of parallelism together, to improve inference latency of tasks that can be represented by a static DAG of operators with predefined input/ou...
  </details>

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


### 📂 defense
*防御与防护方法 / Defense & Protection Methods* — 58 papers

- **2026-09-14** — Zhaofeng Yu, Haokai Ma, Dongyang Zhan et al. — [Misleading the Planner through Deceptive Resumes: Registration-Time Injection in Centralized Multi-Agent Systems](http://arxiv.org/abs/2609.15516v1)
  <details><summary>📄 Abstract</summary>
  A centralized LLM-based multi-agent system (MAS) extends its functionality by registering new worker agents, whose descriptions are read by the planner to decide how a task is decomposed, which worker executes each subtask, and what each subtask requires. Third-party descriptions are authored outside the system but trusted by the planner, creating a registration-time injection channel. The payload is planted before any user instruction arrives, targets the planner and propagates through the gene...
  </details>

- **2026-09-14** — Luis M. Sánchez — [Clean Scores, Buried Evidence, and Confident Wrong: A Receipt-Based Audit of Frontier Agentic QA](http://arxiv.org/abs/2609.15319v1)
  <details><summary>📄 Abstract</summary>
  Frontier models score well on shallow document/chart reading tasks. In a controlled data-room audit, moving evidence into buried conditions reduced accuracy, increased forced declarations, increased tool calls, and increased cost per correct answer. Confidence and benchmark calibration did not fully capture wrong answers; a documented production incident shows fabricated structural claims can be mixed with accurate numeric tables. Agentic evaluations need claim-level receipts (statement-level pr...
  </details>

- **2026-09-14** — Yuhang Wang — [Why LLM Agents Collapse Without Oversight: The Enforcement Gap as the Mechanism Behind Emergence World Failures](http://arxiv.org/abs/2609.15293v1)
  <details><summary>📄 Abstract</summary>
  When Emergence World placed frontier LLM agents in an unsupervised multi-agent simulation, the results were alarming: agents committed crimes, starved, and enforced unanimous conformity -- without any external attacker. This paper identifies the mechanism. Reflexion-style agents already detect dangerous plan steps through iterative self-critique, yet the architecture provides no pathway from detection to action. We call this the enforcement gap: the audit sees the problem; the controller ignores...
  </details>

- **2026-09-14** — Dalton Diez, Peyton Andras, Max Shroyer et al. — [Event-Native Symbolic-Temporal Spike Encoding Framework for Heterogeneous Cyber Streams](http://arxiv.org/abs/2609.15772v1)
  <details><summary>📄 Abstract</summary>
  Spiking neural networks (SNNs) have shown promise for sparse, event-driven computation through stateful processing that is naturally compatible with low-power edge hardware. These properties align with cyber monitoring, where data arrives asynchronously, and malicious behavior often emerges through temporal patterns across event sequences. However, cyber streams are not composed solely of continuous numeric signals: their informative structure is also carried by categorical identifiers, irregula...
  </details>

- **2026-09-14** — Daniele Veri' — [Beyond AI Literacy: A Structured Review and Exploratory Meta-Analysis of Measures for Competent Generative-AI Use](http://arxiv.org/abs/2609.15624v1)
  <details><summary>📄 Abstract</summary>
  Researchers assessing competent generative-AI use at work must choose among self-reports, objective tests, and measures of oversight and reliance. We conducted a structured, seeded review of 24 focal empirical publications, starting from the 2024 COSMIN-based review and adding a targeted update through 17 August 2026. We grouped the measures into four domains: knowledge and use, epistemic oversight, reliance calibration, and operational control of tool-using agents. In an exploratory meta-analys...
  </details>

- **2026-09-14** — Yolo Y. Tang, Daiki Shimada, Jiayue Meng et al. — [BVB: Benchmarking Agentic Video Understanding via Programmatic Reconstruction in Blender](http://arxiv.org/abs/2609.15478v1)
  <details><summary>📄 Abstract</summary>
  Multimodal agents can create complex videos in software such as Blender by coding without relying on diffusion models. Yet video understanding benchmarks still evaluate models mainly through question answering. If an agent truly understands a video, it can reconstruct it programmatically. We introduce BVB, Blender-VideoBench, a benchmark that tests this ability by asking agents to reconstruct real-world videos as animated Blender scenes. To ensure fair comparison, each agent programs the reconst...
  </details>

- **2026-09-14** — Jean Groeninger, Zihao Zhao, Juliana de Castilhos et al. — [Listening for Airway Stenosis: A Foundation Model-Based Method for Rapid and Accessible Detection](http://arxiv.org/abs/2609.15453v1)
  <details><summary>📄 Abstract</summary>
  Airway stenosis can cause severe respiratory complications, yet its detection often relies on specialized examinations and medical imaging. This study explores the potential of acoustic AI for rapid and accessible airway stenosis detection using readily acquired patient voice recordings. We systematically investigate whether acoustic foundation models (AFMs) can extract acoustic representations associated with airway stenosis-related speech patterns. Experiments are conducted on a cohort of 748 ...
  </details>

- **2026-09-14** — Hongchang Shi, Jinpeng Hu, Ao Wang et al. — [MarKey: Marginal Utility Guided Greedy Keyframe Selection for Long Video Understanding](http://arxiv.org/abs/2609.15408v1)
  <details><summary>📄 Abstract</summary>
  Long-video understanding remains challenging for multimodal large language models (MLLMs) because densely encoding long frame sequences is computationally expensive, while uniform sampling under a limited visual budget can miss sparse yet decisive evidence. Recent training-free keyframe selection methods have enabled more efficient inference and yielded promising performance gains. However, many existing methods score frames largely in isolation without explicitly considering how each candidate ...
  </details>

- **2026-09-14** — Sayantan Mukherjee — [Large Universe Subset Predicate Encryption with IND-CCA Security (with Constant-size Ciphertext and Keys)](http://arxiv.org/abs/2609.15312v1)
  <details><summary>📄 Abstract</summary>
  Katz et al. (CANS'17) introduced Subset Predicate Encryption (SPE).   This scheme is a generalization of broadcast encryption as it emulates the \emph{subset containment} predicate in the encrypted domain.   They proposed two selectively IND-CPA secure SPE constructions in the small universe setting.   They also showed some black-box transformations of SPE to well-known primitives like WIBE and ABE to establish the richness of the SPE structure.   Chatterjee and Mukherjee (RSA'19) proposed two S...
  </details>

- **2026-09-14** — Hanne Beuter, Sebastian Dorn — [Closed-form Bayesian homography estimation from noisy point correspondences](http://arxiv.org/abs/2609.15227v1)
  <details><summary>📄 Abstract</summary>
  While homographies are fundamental to many computer vision tasks, the majority of conventional estimation techniques provide only point estimates without directly quantifying uncertainty introduced by noisy observations. Uncertainty, though, propagates to subsequent processing steps such as camera calibration and 3D reconstruction and is particularly relevant in safety-critical and socially relevant fields including medical imaging, autonomous driving, and defense. We present a fast Bayesian for...
  </details>

- **2026-09-14** — Gongbo Zhang, Hao Li, Yu Wang et al. — [OpenAI4S: Code as Action, Science as Sessions](http://arxiv.org/abs/2609.15096v1)
  <details><summary>📄 Abstract</summary>
  AI co-scientists could accelerate computational research, but over a long-running study the workflow also has to stay inspectable, resumable and reproducible, which requires persistent computational state and provenance. Here we present OpenAI4S, an open-source scientific research agent built around the principle of \emph{Code as Action, Science as Sessions}. OpenAI4S combines a persistent computing runtime with research-session management: orchestration is handled through structured tool calls,...
  </details>

- **2026-09-14** — Hyeongcheol Park, Sumin In, Suyeon Myeong et al. — [SALUTE: Benchmarking and Adapting LLMs for the Defense Domain](http://arxiv.org/abs/2609.15022v1)
  <details><summary>📄 Abstract</summary>
  Defense is a knowledge-intensive domain that requires precise understanding of specialized terminology, doctrinal concepts, operational procedures, and evolving military events. Although recent work has explored language technologies for military applications, existing efforts remain fragmented: they are often task-specific, rely on limited adaptation pipelines, or lack comprehensive defense-domain evaluation. In this paper, we present SALUTE, an end-to-end framework for benchmarking and adaptin...
  </details>

- **2026-09-14** — Hyungseok Ryu, Pilwon Hur — [Two-Stage Personalized Gait Phase Estimation in Stroke Survivors During Exoskeleton-Assisted Walking: An Offline Feasibility Study](http://arxiv.org/abs/2609.14984v1)
  <details><summary>📄 Abstract</summary>
  This study evaluated personalized gait phase estimation for stroke survivors using functional inertial measurement unit (IMU) alignment and two-stage sequential adaptation of models pre-trained on healthy gait. The estimator used signals from a thigh-mounted IMU. Heel force-sensitive resistor measurements provided reference phase labels for offline adaptation and evaluation. Stage 1 established a distillation-regularized participant-specific model, and Stage 2 performed conditional refinement us...
  </details>

- **2026-09-14** — Tinashe Handina, Yuehan Diao, Adam Wierman et al. — [Strategic Decision Focused Learning](http://arxiv.org/abs/2609.14907v1)
  <details><summary>📄 Abstract</summary>
  Machine learning (ML) predictions are increasingly being used to guide decision-making, giving rise to the problem of decision-focused learning (DFL) where predictors are optimized for downstream decision quality rather than accuracy alone. However, most existing work assumes a single decision-maker optimizing in isolation. This paper formalizes strategic decision-focused learning, where an ML system predicts an exogenous state that some agents observe before playing a game. For example, a park ...
  </details>

- **2026-09-14** — Livia Oddi, Simone Scardapane, Toru Sugimoto et al. — [Authorship attribution and aesthetic evaluation of AI poetry: a case study with Haiku](http://arxiv.org/abs/2609.15511v1)
  <details><summary>📄 Abstract</summary>
  This paper investigates the generation and human evaluation of Japanese haiku by contemporary Large Language Models (LLMs), focusing on authorship perception and aesthetic judgment within a constrained poetic form. Using a few-shot prompting strategy, Japanese haiku were generated across a heterogeneous set of large language models, including open- and closed-source systems, medium-scale and large-scale architectures, models with native or adapted Japanese support, and multilingual proprietary m...
  </details>

- **2026-09-14** — Ivy Zhang — [The Troy Moment of AI: Why SomeWill Cheat and SomeWill Follow?](http://arxiv.org/abs/2609.15494v1)
  <details><summary>📄 Abstract</summary>
  Recent investigations of the July 2026 OpenAI--Hugging Face incident motivate two questions about agent behavior under task failure: when an assigned task becomes impossible, does an agent stop or escalate, and can observing another agent's behavior change that decision? We study these questions using seven ImpossibleBench tasks with GPT-5.6 Sol, Claude Fable 5.1, and Gemini 3.8 Flash in both solo and three-agent settings. Each task contains a genuine software defect together with a conflicting ...
  </details>

- **2026-09-14** — Dennis Ng, Xingyu Shen, Ankit Raj et al. — [ChatGPT Images 2.5 in the Wild: A Launch-Period Dataset and Detector Evaluation](http://arxiv.org/abs/2609.15100v1)
  <details><summary>📄 Abstract</summary>
  An image tool can change its underlying generator while retaining its public name, making version attribution from online posts ambiguous. We study this problem after the ChatGPT Images 2.5 launch. Our frozen collection contains 3,478 images from 2,440 posts across 8 sources. Recorded posting times fall within the first 51.1 hours after the announcement. It records three attribution tiers and retains standalone images after image-form filtering and targeted review. Caption claims and host record...
  </details>

- **2026-09-14** — Lingheng Du, Yiming Tang, Xufeng Duan et al. — [What Does an LLM Learn from Reinforcement Learning? A Mechanistic Interpretability Perspective with Fixed-SAE Track](http://arxiv.org/abs/2609.15064v1)
  <details><summary>📄 Abstract</summary>
  Reinforcement learning (RL) is widely utilized in large language model training to improve targeted capabilities, yet how RL reshapes a model remains poorly understood. Prior attempts to explain how RL works largely offer behavioral perspectives, leaving open what RL gives a model at the representation level: can RL create genuinely novel features, and which existing features does it enhance or suppress? Recent developments in mechanistic interpretability suggest sparse autoencoders (SAEs) as a ...
  </details>

- **2026-09-14** — Siwei Wu, Jincheng Ren, Yizhi Li et al. — [ModularRSI: Modular and Generalizable Recursive Harness Self-Improvement](http://arxiv.org/abs/2609.14857v1)
  <details><summary>📄 Abstract</summary>
  Recent work extends recursive self-improvement (RSI) to agent harnesses for long-horizon coding and terminal tasks, enabling agents to improve execution mechanisms from experience. However, generalizable harness RSI remains challenging. First, evolving harnesses on evaluation benchmarks or their subsets makes it difficult to distinguish reusable improvements from benchmark-specific adaptation. Second, single-trajectory updates can conflate systematic harness deficiencies with instance-specific r...
  </details>

- **2026-09-13** — Mirza Samad Ahmed Baig, Syeda Anshrah Gillani, Asher Ali et al. — [The Stochastic Deputy: Structural Tenant Isolation for Tool-Using LLM Agents](http://arxiv.org/abs/2609.14780v1)
  <details><summary>📄 Abstract</summary>
  Multi-tenant tools commonly accept a tenant identifier and validate it against the caller's entitlement. For a large language model (LLM) agent, that pattern delegates resource selection to a process whose context may contain attacker controlled instructions. We formalize this stochastic deputy problem and present a structural defense: remove tenant identity from the Model Context Protocol (MCP) tool schema, bind scope to a verified credential, and enforce it below the agent. In a 373-trial abla...
  </details>

- **2026-09-13** — Yusheng Zheng, Wenhui Zhang, Yu Mao — [LLM Agent Capabilities Should Follow Task Intent and Context Source](http://arxiv.org/abs/2609.14631v1)
  <details><summary>📄 Abstract</summary>
  LLM agents take real actions, including executing code, modifying files, calling services, and delegating tasks, driven by context sources: user requests, tool results, documents, shell outputs, Skill and MCP instructions, memory. Unlike traditional systems, where capability is predefined, the least-privilege capability an agent needs is dynamic, depending on its task intent: what it wants to do and how. This creates a security and safety challenge: all inputs enter one shared planning channel w...
  </details>

- **2026-09-13** — Tianhao Ma, Weihao Xuan, Dong-Dong Wu et al. — [DenMark: Robust Semantic Watermarking for Diffusion Language Models](http://arxiv.org/abs/2609.14257v1)
  <details><summary>📄 Abstract</summary>
  Semantic text watermarks encode signals in meaning rather than surface token choices, offering robustness to paraphrasing and other semantic-preserving edits. Existing semantic watermarking methods are primarily designed for autoregressive language models (ARLMs), where completed candidate units can be generated and scored before generation proceeds. This paradigm does not naturally extend to diffusion language models (DLMs), where semantic units remain incomplete during intermediate denoising s...
  </details>

- **2026-09-13** — Sarah Wilson, Gail Kaiser, Patrick Musau — [Efficiency Hallucination: Formalizing and Measuring Behavioral Calibration in LLM-Based Code Optimization](http://arxiv.org/abs/2609.14839v1)
  <details><summary>📄 Abstract</summary>
  The integration of Large Language Models (LLMs) into automated code optimization introduces a critical reliability risk we term the Efficiency Hallucination: an LLM's tendency to issue non-functional mutations with unsubstantiated performance claims on already-optimized code. This is driven by the Evaluation Trap, wherein binary benchmarks incentivize unnecessary modifications over safely abstaining. We present a validation framework using classification penalty methods, evaluated across 180 opt...
  </details>

- **2026-09-13** — Cheikh Ahmed — [Enemray: Toward Capable Language Models for Hassaniya](http://arxiv.org/abs/2609.14829v1)
  <details><summary>📄 Abstract</summary>
  We introduce Enemray, a Hassaniya-centric language model that enables general-purpose interaction in Hassaniya. Enemray is trained around a stability--plasticity objective: acquire strong Hassaniya linguistic and cultural competence while preserving the general reasoning, multilingual, instruction-following, and safety behaviors of a capable instruction-tuned model. The development pipeline separates language acquisition from behavioral specialization. A separately assembled continual-pretrainin...
  </details>

- **2026-09-13** — Arham Sethi, Arsen Kenzhebayev, Saanvi Paturi et al. — [Fabrication After Tool Failure: Tool-Augmented Agents Assert Values Their Tools Did Not Return](http://arxiv.org/abs/2609.14758v1)
  <details><summary>📄 Abstract</summary>
  Tool-augmented language models are evaluated on whether they reach the right answer, not on whether they report honestly when a tool fails to supply one. We isolate this post-failure decision with a benchmark of 1,024 items spanning 16 internal-system domains and eight tool-failure types, in which a tool call is enforced and the returned payload is guaranteed to be unusable. Under a deployment-style system prompt, 14.10% of responses are dishonest: the model either asserts a value the payload ca...
  </details>

- **2026-09-13** — Weihong Qi, Chen Ling — [Perceive, Refine, Reason: A Calibrated Pipeline for Measuring Indicators in Strategic Visual Communication on Social Media](http://arxiv.org/abs/2609.14699v1)
  <details><summary>📄 Abstract</summary>
  Visual content shapes audience perception and opinion on social media, and computational social science increasingly relies on automated tools to analyze images at scale. Yet a measurement gap persists: existing tools rely on predefined categories or produce only coarse image-level labels, while measuring which specific objects appear in an image, how prominently, and where in the frame remains difficult at scale. We introduce Perceive, Refine, Reason (PRR), a calibrated pipeline that turns flex...
  </details>

- **2026-09-13** — Toqeer Ali Syed, Ali Akarma, Adeel Ahmad et al. — [Beyond Scene Description: Multi-Agent Orchestration for Non-visual Access to Virtual Worlds](http://arxiv.org/abs/2609.14512v1)
  <details><summary>📄 Abstract</summary>
  Virtual worlds now host classrooms, meetings, conferences, shops, and social venues, and nearly every interaction they expose assumes a user who can scan a three-dimensional scene, follow avatars, and read floating panels. Blind and visually impaired (BVI) users are left with assistive tools that each solve one task in isolation: naming an object, reading text, describing a scene, or planning a route. A live virtual room defeats that model: obstacles, speakers, gestures, chat, slides, and notifi...
  </details>

- **2026-09-13** — Nitish Kovuru, Prateek Jannu — [CoArena: Evaluating Computer-Use and Multi-Agent Systems in Real Time](http://arxiv.org/abs/2609.14239v1)
  <details><summary>📄 Abstract</summary>
  Static benchmarks for computer-use agents fix a task set at release and score every system against it once. That makes them reproducible, and it lets them drift from what they should measure: a fixed task set ages, leaks into training corpora, and cannot follow how people actually use agents from week to week. CoArena measures use directly. Real users submit tasks; two systems, each a single model or a multi-agent pipeline behind the same tool interface, execute the same task concurrently in ide...
  </details>

- **2026-09-13** — Arya Pulkit, Aditya Ruhela, Akarshan Kapoor et al. — [Lightweight Generalized DeepFake Face Detection with WAVIE: Wavelet Augmented Vision Intermediate Embeddings](http://arxiv.org/abs/2609.14437v1)
  <details><summary>📄 Abstract</summary>
  Deepfake detection systems often exhibit significant performance degradation when deployed on unseen manipulation methods, limiting their reliability in real-world multimedia environments. This lack of generalization poses critical challenges for misinformation mitigation, digital forensics, and human-centric AI systems. Existing detectors perform well on the forgery methods they are trained on, but their accuracy drops sharply on unseen pipelines. To bridge this generalization gap, we propose W...
  </details>

- **2026-09-13** — Madhurananda Pahar, Caitlin Illingworth, Dorota Braun et al. — [CCMAN: Cognitive Instability-Aware Cross-Modal Attention Network for Interpretable Temporal Biomarkers of Verbal Fluency Speech](http://arxiv.org/abs/2609.14764v1)
  <details><summary>📄 Abstract</summary>
  Early detection of cognitive decline from speech offers a scalable and non-invasive alternative to conventional clinical assessment. Verbal fluency tasks are particularly informative, but most automated approaches aggregate features across an entire recording, overlooking temporal speech dynamics. We propose the Cognitive Instability-Aware Cross-Modal Attention Network (CCMAN), a transfer learning framework that learns task-agnostic cognitive speech representations from multiple memory-probing t...
  </details>

- **2026-09-13** — Binghao Wang, Feng Zhang, Wendong Wang et al. — [Robust low-rank tensor completion via factorized weighted tensor schatten-p norm minimization](http://arxiv.org/abs/2609.14307v1)
  <details><summary>📄 Abstract</summary>
  Low-rank tensor factorization provides a flexible framework for completing multidimensional data from incomplete and corrupted observations. However, unweighted spectral regularizers impose a common shrinkage profile across singular components, which may excessively attenuate dominant low-rank components, and factorized variants either lack component-specific weighting or require costly singular value decompositions (SVDs). This paper proposes two weighted Schatten-$p$ tensor factorization model...
  </details>

- **2026-09-12** — Tri Nhu Do, Yosefine Triwidyastuti, Gunes Karabulut Kurt — [Inverse Maxwell-Based Wall-Aware OFDM-ISAC for Slow-Moving Target Sensing](http://arxiv.org/abs/2609.14182v1)
  <details><summary>📄 Abstract</summary>
  In this paper, we study integrated sensing and communication (ISAC) for short-range indoor orthogonal frequency-division multiplexing (OFDM) systems in which the sensing path crosses a building wall. The target is a slow-moving user equipment behind the wall, and its echo is embedded in the wall reflection and static indoor clutter. Because the wall adds excess propagation length, attenuation, and internal reflections, a conventional delay transform reports an apparent range. We therefore formul...
  </details>

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


### 📂 alignment
*对齐与安全约束 / Alignment & Safety Constraints* — 47 papers

- **2026-09-14** — Asraful Haque, Christopher M. Rouleau, Rama K. Vasudevan et al. — [An Open-Source Hardware and Software Toolkit to Enable Agentic RHEED-Guided Thin-Film Synthesis](http://arxiv.org/abs/2609.15922v1)
  <details><summary>📄 Abstract</summary>
  Reflection high-energy electron diffraction (RHEED) provides rich information about evolving surfaces during thin-film growth, but non-automated, operator-dependent alignment and fragmented analysis workflows limit its potential in fully autonomous synthesis. Here, we present an open-source hardware and software toolkit that makes RHEED control and quantitative analysis accessible to operators and artificial intelligence (AI) agents. Demonstrated on a pulsed laser deposition system, the toolkit ...
  </details>

- **2026-09-14** — Kyle O'Brien, Edward James Young, Puria Radmard et al. — [Inoculation Midtraining with Learned Neologisms](http://arxiv.org/abs/2609.15886v1)
  <details><summary>📄 Abstract</summary>
  Large language models (LLMs) often learn both desirable and undesirable properties during post-training. We study whether midtraining, an earlier training stage, can shape which of these properties later generalise. We introduce Inoculation Midtraining, a technique that teaches a base model that unsafe behaviour belongs to a designated <quarantine_token> context, as indicated by the <quarantine_token> neologism (a new token) introduced during midtraining, and then post-trains the model on unsafe...
  </details>

- **2026-09-14** — Natalie Collina, Surbhi Goel, Aaron Roth et al. — [Delegating Authorization to Misaligned Agents: Coalitional Alignment and Safe Control](http://arxiv.org/abs/2609.15803v1)
  <details><summary>📄 Abstract</summary>
  Long-running AI agents create a control problem: each action they take changes the state, which in turn affects the trajectory of future actions. If the agent is not fully aligned, then guaranteeing safety requires approving consequential actions before allowing them to be executed. But requiring human approval at every step makes attention a bottleneck. Delegating review to other AI agents raises the same alignment problem: the reviewers may themselves be misaligned. We identify a condition on ...
  </details>

- **2026-09-14** — Mingzhi Chen, Yiyu Gui, Guibo Luo et al. — [A Language-Guided Multimodal Foundation Model for Zero-Shot and Multi-Task Brain Signal Analysis](http://arxiv.org/abs/2609.15740v1)
  <details><summary>📄 Abstract</summary>
  Brain signal analysis is essential for both neuroscience research and clinical diagnostics, yet current approaches face critical limitations. End-to-end models require task-specific retraining and exhibit limited generalization, while pre-trained models lack semantic depth and still depend on extensive fine-tuning. Meanwhile, general-purpose multimodal foundation models, though powerful in other domains, struggle to interpret brain signals due to representational misalignment and lack of domain ...
  </details>

- **2026-09-14** — Matteo Barbieri, Giammarco La Barbera, Juan Pablo De La Plata et al. — [Benchmarking Intra-Patient 3D Deformable Multimodal Image Registration](http://arxiv.org/abs/2609.15669v1)
  <details><summary>📄 Abstract</summary>
  Multimodal image registration is a key component of many clinical workflows, yet it remains challenging because corresponding anatomical structures often exhibit substantially different image intensities across modalities. In this work, we present a comprehensive benchmark of intra-patient 3D multimodal deformable registration methods across three datasets covering different anatomical regions and difficulty levels, including both synthetic deformation recovery and real clinical scenarios. We ev...
  </details>

- **2026-09-14** — Jiayang Gu, Zheng Fang, Lichaun Xiang et al. — [Principal-timestep Restricted Init via Sparse Matrix-decomposition in Flow-matching](http://arxiv.org/abs/2609.15643v1)
  <details><summary>📄 Abstract</summary>
  Flow-matching diffusion models have recently emerged as a strong paradigm for high-fidelity visual generation. However, their prohibitively high fine-tuning cost limits scalability to downstream tasks. While Low-Rank Adaptation (LoRA) combined with spectral initialization has demonstrated accelerated convergence and improved performance in autoregressive language models by better aligning gradient directions, we find that it fails to deliver similar gains in diffusion fine-tuning, often yielding...
  </details>

- **2026-09-14** — Jiahao Chang, Dong Du, Wanhu Sun et al. — [SAM3D-Part: Interactive Part Selection and Generation from 3D Objects](http://arxiv.org/abs/2609.15639v1)
  <details><summary>📄 Abstract</summary>
  Part-level control is essential for modern 3D asset creation, where objects are frequently edited, reused, animated, or fabricated through their individual components. In many such workflows, users need only several specific components rather than a complete object decomposition. However, existing 3D generation methods produce all parts regardless of user intent, while promptable 3D segmentation methods typically output partial surfaces instead of reusable complete meshes. In addition, image-con...
  </details>

- **2026-09-14** — Weixin Xu, Zhenyu Yang, Bing Wang et al. — [VideoScout: Learning Agentic Active Exploration with Adaptive Reasoning Pacing for Long Video Understanding](http://arxiv.org/abs/2609.15606v1)
  <details><summary>📄 Abstract</summary>
  Multimodal Large Language Models (MLLMs) have achieved remarkable progress on short video understanding yet remain limited on long videos due to the limited visual context window. Prevailing approaches rely on uniform frame sampling or recent coarse-to-fine agentic zooming, both of which struggle to localize sparse, decisive evidence in sufficiently long videos. We formulate long video understanding as a \textbf{Sequential Evidence Acquisition (SEA)} problem, in which an agent reads the video tu...
  </details>

- **2026-09-14** — Yang Xing, Jiong Wu, Savas Ozdemir et al. — [A Unified Vision-Language Model for PSMA PET/CT Report Generation, Visual Question Answering, and Lesion Segmentation](http://arxiv.org/abs/2609.15603v1)
  <details><summary>📄 Abstract</summary>
  Accurate PSMA PET/CT interpretation is central to prostate cancer management, yet existing PET/CT AI models typically address isolated tasks. We propose a unified PSMA PET/CT vision-language model for report generation, visual question answering, and lesion segmentation. The framework adopts an LLaVA-style architecture, comprising a PET/CT vision encoder, an MLP-Mixer projection module, a LoRA-tuned large language model, and a 3D segmentation branch. Training followed a four-stage strategy: visi...
  </details>

- **2026-09-14** — Stephane Hatgis-Kessell, W. Bradley Knox, Emma Brunskill — [Specifying Reward Functions for RL Without Environment Sampling](http://arxiv.org/abs/2609.15544v1)
  <details><summary>📄 Abstract</summary>
  Enabling human stakeholders to specify reward functions that lead to their desired outcomes is a key challenge in deploying reinforcement learning agents. Preference-based methods such as online RLHF can reduce the burden of manual reward design, but they require repeatedly training policies, sampling trajectories from the real world, and eliciting feedback, making them impractical in settings where environment interaction is computationally expensive or unsafe. We introduce Experience-Free Auto...
  </details>

- **2026-09-14** — Qiangqiang Zhou, Wenjun Tang, Yong Chen et al. — [ViCo-SAM3: Vision-Conditioned Alignment for Open-Vocabulary Camouflaged Object Segmentation](http://arxiv.org/abs/2609.15418v1)
  <details><summary>📄 Abstract</summary>
  Open-vocabulary camouflaged object segmentation (OVCOS) aims to segment unseen camouflaged objects under text guidance. We observe that SAM3 still suffers from a pronounced semantic gap between global textual semantics and fine-grained pixel-level visual cues in OVCOS. Meanwhile, fully fine-tuning the text encoder introduces heavy parameter overhead and risks overfitting to training categories, which compromises open-vocabulary representation flexibility. To address these issues, we propose ViCo...
  </details>

- **2026-09-14** — Chenxu Liu, Zilu Zou, Peizhong Gao et al. — [IWC-Bench: Evaluating Web Application Generation from a Software Testing Perspective](http://arxiv.org/abs/2609.15387v1)
  <details><summary>📄 Abstract</summary>
  Human evaluation provides a direct measure of the quality of LLM-generated web applications. However, fitting human judgments through automated evaluation remains challenging. Static benchmarks can credit functionality that exists in source code but is unreachable at runtime. Interactive benchmarks exercise the application, yet incomplete exploration can cause them to miss implemented functionality and confound application defects with agent execution failures. To address these limitations, we p...
  </details>

- **2026-09-14** — Qingyu Liu, Rixi Xu, Yushen Chen et al. — [Cross-Lingual F5-TTS 2: A Simplified Framework for Language-Agnostic Voice Cloning](http://arxiv.org/abs/2609.15184v1)
  <details><summary>📄 Abstract</summary>
  Zero-shot text-to-speech (TTS) can clone a speaker's voice from a short audio prompt, yet most TTS systems still require the audio prompt transcript during inference. This dependency prevents cross-lingual voice cloning when the audio prompt transcript is unavailable, particularly for unseen languages. Cross-Lingual F5-TTS removes this dependency and enables transcript-free cross-lingual voice cloning, but it prepares its training data with forced alignment. Forced alignment is sensitive to boun...
  </details>

- **2026-09-14** — Hanzhang Tu, Zhanfeng Liao, Wei Min et al. — [Tele360: Real-Time Feed-Forward Human Reconstruction from Sparse Unposed Cameras](http://arxiv.org/abs/2609.15032v1)
  <details><summary>📄 Abstract</summary>
  Live free-viewpoint visualization of real humans is critical for immersive communication and interactive digital experiences. Existing methods either rely on computationally expensive optimization or require calibrated cameras and low-resolution inputs, making real-time high-resolution deployment impractical. In this work, we present Tele360, the first real-time feed-forward system for dynamic human reconstruction and live free-viewpoint visualization from sparse, unposed RGB streams. Our system...
  </details>

- **2026-09-14** — Frank Li — [Validating Hybrid-State Cache Recovery for GLM-5.3-Flash with vLLM and LMCache](http://arxiv.org/abs/2609.15030v1)
  <details><summary>📄 Abstract</summary>
  External cache transfers can succeed while a hybrid language model resumes from an inconsistent state. We examine the full 45-layer GLM-5.3-Flash model, using the RedHatAI/ GLM-5.3-Flash-NVFP4 quantized checkpoint with vLLM and LMCache under four-way tensor parallelism. A complete-hit recovery mismatch restored state for the full prompt while the scheduler credited one fewer token. We aligned recovery through strict-prefix lookup and established a numerical comparison using shared computation co...
  </details>

- **2026-09-14** — Quang Phuoc Nguyen, Félix Gaschi, David Anugraha et al. — [Online Language Adaptive Sampling for Better Distributed Cross-lingual Gains](http://arxiv.org/abs/2609.14969v1)
  <details><summary>📄 Abstract</summary>
  Realignment is a promising approach for improving the cross-lingual transfer ability of multilingual language models, particularly for extremely low-resource languages (LRLs). However, existing realignment methods rely on uniform and random sampling of parallel sentences across languages, which may be suboptimal under limited batch sizes. In practice, models may benefit from seeing certain languages more frequently, especially those that are poorly aligned, and the optimal distribution can evolv...
  </details>

- **2026-09-14** — Chandan Kumar Sah, Jishnu Keshavan — [Exact Feasibility Certification and Optimal Responsibility Allocation for Multi-Robot CBF Safety Filters](http://arxiv.org/abs/2609.14935v1)
  <details><summary>📄 Abstract</summary>
  Multi-robot Control Barrier Function (CBF) safety filters can become infeasible, but a failed quadratic program (QP) does not indicate why the conflict occurred or how to resolve it. To address this, we develop an exact feasibility certificate for multi-agent CBF filters with heterogeneous control-affine dynamics and convex input sets. The certificate quantifies a feasibility reserve by separating the demand imposed by safety constraints from the available actuator supply. This decomposition sho...
  </details>

- **2026-09-14** — Jiayi Yuan, Hangoo Kang, James Jihao Liu et al. — [Forty Shades of Blue: Quality-Diversity Alignment via Mode-Conditioned Reinforcement Learning](http://arxiv.org/abs/2609.14896v1)
  <details><summary>📄 Abstract</summary>
  A notable byproduct of LLM alignment training is mode collapse: the progressive loss of output diversity that narrows a model's expressivity at inference time. This degradation is especially limiting for applications requiring open-ended exploration and pluralistic perspectives, such as scientific ideation and creative writing. We present MoDA (Mode-conditioned Diversity Alignment), an online post-training RL algorithm that jointly optimizes generation quality and diversity, inspired by the coor...
  </details>

- **2026-09-14** — Naihao Deng, Samee Arif, Shuaichen Chang et al. — [One Example Is Enough to Pass Fairness Benchmarks: Rethinking Fairness Evaluation for Aligned LLMs](http://arxiv.org/abs/2609.14860v1)
  <details><summary>📄 Abstract</summary>
  Warning: This submission studies stereotypes and biases, and contains toxic and offensive examples, used for illustration purposes only.   Fairness benchmarks such as BBQ have become the de facto standard for fairness evaluation across major model families. We argue that these benchmarks are too easy to support their role: training Qwen 2.5 7B Base with Group Relative Policy Optimization (GRPO) on a single BBQ example, or placing that example in context as a one-shot demonstration for in-context...
  </details>

- **2026-09-13** — Jingbin Hu, Luyu Wang, Wenjie Tian et al. — [Bridging Data, Reasoning, and Alignment: A Unified Framework for Context-Aware Instruction-Following TTS](http://arxiv.org/abs/2609.14740v1)
  <details><summary>📄 Abstract</summary>
  The ISCSLP 2026 CoT-TTS Challenge requires TTS systems to generate Chain-of-Thought (CoT) reasoning from dialogue history before synthesizing contextually appropriate speech. While the official baseline establishes a unified architecture, it remains constrained by limited contextual comprehension, weak instruction fidelity, and suboptimal audio quality. We present a systematic optimization pipeline to address these limitations. First, we develop a data process framework that cleans raw data via ...
  </details>

- **2026-09-13** — Guocun Wang, Kenkun Liu, Guorui Song et al. — [Open-UniMo: Towards Unified Motion-Language Understanding and Generation in the Open World](http://arxiv.org/abs/2609.14615v1)
  <details><summary>📄 Abstract</summary>
  Unified motion generation and understanding is crucial for embodied AI systems that can both synthesize and interpret human actions in open-world environments. Existing motion-language models often treat motion as an auxiliary modality of a language model, leading to text-dominated representations and limited cross-modal interaction. Moreover, the next-token prediction paradigm is not naturally suited to long motion sequences, where autoregressive generation may accumulate prediction errors. To ...
  </details>

- **2026-09-13** — Liangjian Wen, Linjie Li, Jiang Duan et al. — [Dependency, Compression, and Synergy: A Unified Information-Theoretic View of Multimodal Learning](http://arxiv.org/abs/2609.14421v1)
  <details><summary>📄 Abstract</summary>
  Recent advances in multimodal foundation models have intensified the need to understand how different modalities share, preserve, and complement information. Mutual Information (MI), the Information Bottleneck (IB), and Partial Information Decomposition (PID) provide complementary perspectives, yet existing studies often treat them as isolated tools. This survey presents an information-theoretic perspective connecting these principles as progressively refined views of multimodal information proc...
  </details>

- **2026-09-13** — Sarah Y. Li, Elijah Renner, Rayan Ansari et al. — [Corpus Characterization and Inverse Constitutional Fine-Tuning for Style-Aware Radiology Reports](http://arxiv.org/abs/2609.14226v1)
  <details><summary>📄 Abstract</summary>
  Automated radiology report generation has advanced rapidly in diagnostic accuracy, yet generated reports frequently diverge from the stylistic conventions of authentic radiologist writing in structure, diction, and uncertainty language, a gap which has direct implications for clinician trust and user experience. To address this, we characterize stylistic variation across 2,000 reports from the CheXpert Plus dataset using Bio-ClinicalBERT embeddings, UMAP dimensionality reduction, and HDBSCAN clu...
  </details>

- **2026-09-13** — Yixian Gao, Hongyu Liu, Yang Liu — [On passive recovery of structured elastic density and initial states](http://arxiv.org/abs/2609.14215v1)
  <details><summary>📄 Abstract</summary>
  We study simultaneous recovery of the (variable) mass density, initial displacement, and initial velocity for the three-dimensional isotropic elastic wave equation with known constant Lamé parameters. The data are the complete displacement trace on an enclosing boundary. We first assume that the density-weighted initial displacement and velocity have fixed known profiles in one spatial direction. The $s^0$ and $s^1$ coefficients of the zero-frequency Laplace expansion identify these weighted sta...
  </details>

- **2026-09-12** — Prajjwal Bhattarai, Tuka Alhanai — [Signatures of Steerability in Activation Space of Language Models](http://arxiv.org/abs/2609.14151v1)
  <details><summary>📄 Abstract</summary>
  Steering language models using a set of contrastive representations has been a canonical and computationally efficient method for controlling model behavior. Despite this success in controlling certain model behaviors, the effectiveness of activation steering varies markedly across concepts; the generalization properties of steering vectors are often considered a function of the dataset used to construct them. We make this dataset-dependence claim more rigorous and show that simple separation me...
  </details>

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


### 📂 robustness
*鲁棒性与可靠性 / Robustness & Reliability* — 56 papers

- **2026-09-14** — Chaofan Wang, Xiaodong Gu, Yuling Shi et al. — [Translator vs. Challenger: Adversarial Agentic Learning for C-to-Rust Translation](http://arxiv.org/abs/2609.15381v1)
  <details><summary>📄 Abstract</summary>
  C-to-Rust translation remains challenging due to the substantial semantic gap between the two languages. Recent experience-enhanced LLM translators improve translation quality by learning reusable insights from prior failures and repairs. Yet learned insights do not automatically constitute reusable translation knowledge: derived from sparse, program-specific traces, they often contain missing conditions, narrow applicability boundaries, or overlooked corner cases. This limits their robustness a...
  </details>

- **2026-09-14** — Sarra Gharsallah, Adele Robaldo, Mariia Tokareva et al. — [Can We Trust the Judges? Validation of Factuality Evaluation Methods via Answer Perturbation](http://arxiv.org/abs/2609.15561v1)
  <details><summary>📄 Abstract</summary>
  Evaluating the factual correctness of large language models (LLMs) is vital for many applications. But are our evaluation tools themselves trustworthy? Despite the rise of factuality-based metrics, their sensitivity and reliability remain underexplored. This paper introduces a meta-evaluation framework that systematically tests these metrics using controlled corruptions of gold standard answers. Our method generates ranked outputs with known degrees of degradation to probe how metrics capture nu...
  </details>

- **2026-09-14** — Lindsay Spoor, Aske Plaat, Thomas Moerland — [Evaluation Metrics for Safe Reinforcement Learning](http://arxiv.org/abs/2609.15315v1)
  <details><summary>📄 Abstract</summary>
  Safe reinforcement learning (RL) is commonly formalized as a Constrained Markov Decision Process (CMDP), in which an agent maximizes expected reward while keeping its expected cumulative cost below a specified safety bound. Existing safe RL benchmarks predominantly report whether an algorithm is safe on average, following this expectation-based guarantee. We argue that this convention is insufficient to reliably characterize an algorithm's true safety: it fails to capture how often and how sever...
  </details>

- **2026-09-14** — Dylan Waldner, Yiannis Kantaros, Guido Governatori et al. — [Legislating World-Model-Based Planning with Legal Reasoning](http://arxiv.org/abs/2609.15113v1)
  <details><summary>📄 Abstract</summary>
  As robotic systems grow more general, legal norms are needed to integrate them into society. This paper extends the isomorphism problem of aligning legal source texts with their encodings, and measures two key challenges to robot normative control: (1) the \textit{grounding isomorphism gap}, where perception error grounds false atoms for legal reasoning, and (2) the \textit{ontological isomorphism gap}, where one legal conclusion admits many faithful translations into planning constraints. The p...
  </details>

- **2026-09-14** — Shwai He, Haichao Zhang, Shen Yan — [Disentangling Representation Evolution in Transformers through Directional Decomposition](http://arxiv.org/abs/2609.15975v1)
  <details><summary>📄 Abstract</summary>
  Transformer representations evolve through learned additive transformations that either preserve their current direction or redirect it. We study this evolution as a functional geometry, decomposing learned updates into parallel and perpendicular components. Across pretrained models, we find substantial parallel components beyond the residual identity path. We then apply the decomposition in two spaces: to attention and MLP updates relative to the hidden state, and to attention value aggregation...
  </details>

- **2026-09-14** — Zhenjie Yang, Yideng Zhang, Dongjie Zhang et al. — [Bench2Dex: Benchmarking Visuo-Tactile Bimanual Dexterous Manipulation Across Dexterous Hands](http://arxiv.org/abs/2609.15726v1)
  <details><summary>📄 Abstract</summary>
  Tactile sensing provides contact information that can be difficult to infer from vision alone, but tactile hardware for dexterous hands has not converged to a common design. Dexterous hands differ in finger structure, contact surfaces, and sensor layouts, while simulated tactile signals still differ from measurements produced by physical sensors. These factors make it difficult to study visuo-tactile manipulation across diverse dexterous hands within a consistent experimental setting. We present...
  </details>

- **2026-09-14** — Tahir Cetin Akinci — [Multiscale Visibility Theory: A Task-Relative Operator-Geometric Framework for Observation, Robustness, and Detectability](http://arxiv.org/abs/2609.15948v1)
  <details><summary>📄 Abstract</summary>
  Multiscale Visibility Theory (MVT) is introduced as a task-relative operator-geometric framework for determining how prescribed information survives and remains accessible through a structured observation architecture. Rather than evaluating observation quality by transform magnitude, output energy, rank, or signal prominence alone, MVT measures the accessibility of a specified task direction or task subspace through the row space of the composite operator A_A = R_E W_rho H_beta P_Omega. Unlike ...
  </details>

- **2026-09-14** — Amir Globerson, Amy Keeling, Anisha Choudhury et al. — [Towards Scalable Measurement of Durable Skills](http://arxiv.org/abs/2609.15864v1)
  <details><summary>📄 Abstract</summary>
  Durable skills, such as collaboration, creativity and critical thinking, are instrumental to success in the modern workforce. Yet, measuring these skills remains a persistent challenge. Moreover, because what is not measured is often not taught, these skills are often overlooked in mainstream educational curricula. Designing effective assessments for these skills necessitates balancing two often-conflicting requirements: ecological validity and psychometric rigor. On the one hand, the assessment...
  </details>

- **2026-09-14** — Yucheng Shen, Lingyong Yan, Jiulong Wu et al. — [Navigating Sparse Evidence: Agentic Visual RAG via Explicit Context Selection and Consolidation](http://arxiv.org/abs/2609.15800v1)
  <details><summary>📄 Abstract</summary>
  Visual Retrieval-Augmented Generation (VRAG) empowers models to navigate and answer queries about visually rich documents by retrieving relevant page images as visual evidence and reasoning over their content. However, effectively utilizing this visual evidence is usually impeded by two main challenges. First, answer-relevant evidence is sparse and may be concentrated in a small region of one page or dispersed across multiple pages. Second, existing agentic methods often generate answers based o...
  </details>

- **2026-09-14** — Hansong Ma, Junxiao Wang — [EEG-Xplain: Decoding Neural Black-Boxes of EEG Foundation Models](http://arxiv.org/abs/2609.15687v1)
  <details><summary>📄 Abstract</summary>
  EEG foundation models such as BIOT, LaBraM, and EEGMamba have achieved remarkable performance in neural signal decoding, but their black-box nature limits clinical trust and neuroscientific validation. We propose a unified attribution framework for interpreting EEG foundation models across heterogeneous architectures. The framework integrates gradient-, perturbation-, and activation-based explanation methods to analyze model behavior in spatial, temporal, and frequency dimensions. Spatially, it ...
  </details>

- **2026-09-14** — Yongsheng Chen, Shuo Lu, Wei Guo et al. — [Physics-Guided Conditional Flow Matching with Energy Regularization for Robust PDE Inverse Problems](http://arxiv.org/abs/2609.15536v1)
  <details><summary>📄 Abstract</summary>
  We consider partial differential equation (PDE) inverse problems from sparse, noisy, and corrupted observations, with the aim of recovering unknown coefficient fields and associated state variables in a mesh-free setting. Under such sparse and corrupted observations, standard physics-informed and generative approaches typically treat all samples indiscriminately and therefore lack a principled mechanism for reconciling physical laws with contaminated data. We address this difficulty with a two-s...
  </details>

- **2026-09-14** — Rafael Pina, Varuna De Silva, Corentin Artaud — [Robust and Efficient Communication for Multi-Agent Learning](http://arxiv.org/abs/2609.15361v1)
  <details><summary>📄 Abstract</summary>
  Effective communication is a cornerstone of distributed intelligence in Multi-Agent Reinforcement Learning (MARL), yet ensuring that generated messages are both informative and robust to physical constraints remains a significant challenge. This paper introduces Multi-Agent Regularized Communication (MARC), a novel framework inspired by information-theoretic principles of conditional mutual information. MARC employs an attention-based architecture coupled with a unique message regularization mec...
  </details>

- **2026-09-14** — Marta Marszewska, Justyna Signerska, Paweł Dłotko — [Topological Characteristics for the Analysis of Vector Fields. New stable characteristics for discrete and continuous dynamical systems](http://arxiv.org/abs/2609.15260v1)
  <details><summary>📄 Abstract</summary>
  The qualitative analysis of nonlinear dynamical systems relies on identifying geometric and topological structures that govern phase-space organization. We develop a computational framework based on novel topological and geometric descriptors of vector fields that enables robust comparison of dynamical regimes from both analytical models and sampled data. The framework comprises the Begin-End Point Embedding (BEPE), Density of Directions (DOD) and Euler characteristic-based summaries (Euler Char...
  </details>

- **2026-09-14** — Qingtao Xia, Jiahua Bao, Siyao Cheng et al. — [Pre-PEFT Probing: Weight Statistics and Perturbation Robustness for Layer Selection in VLM Vision Encoders](http://arxiv.org/abs/2609.15229v1)
  <details><summary>📄 Abstract</summary>
  We propose a pre-fine-tuning probing method for Parameter-Efficient Fine-Tuning (PEFT) layer selection, aiming to obtain more stable and higher gains with fewer trainable parameters when adapting large vision--language models (VLMs). Unlike the common practice of applying LoRA and other adapters to all layers at once---where layer selection often relies on heuristic rules---we focus on the vision encoder and directly evaluate the "adaptability'' of each Transformer layer. Specifically, we charac...
  </details>

- **2026-09-14** — Tin Mišić, Takato Horii — [Sensory Precision Inference for Multimodal Arbitration under Uncertainty](http://arxiv.org/abs/2609.15065v1)
  <details><summary>📄 Abstract</summary>
  Autonomous agents operating on multisensory data cannot assume that all sensory modalities remain consistently informative. In real environments, sensory streams are frequently corrupted by noise, missing data, or inter-modal incongruence, requiring adaptive arbitration between competing sensory hypotheses. While active inference provides a principled framework for uncertainty-guided inference, the role of dynamically inferred sensory precision in generative multimodal arbitration under sensory ...
  </details>

- **2026-09-14** — Sidi Chang, Peiying Zhu — [Four Ledgers, Not One Score: Responsible Communication of LLM-Judge Calibration in Biomedical ML](http://arxiv.org/abs/2609.15015v1)
  <details><summary>📄 Abstract</summary>
  Synthetic perturbations appear to offer inexpensive calibration data for LLM evaluators in biomedical ML, where expert review is scarce. Yet a planted mutation key is neither a detector output nor automatically human ground truth. We formalize four distinct ledgers: planted perturbations, independent detector outputs, source-linked human dispositions, and human-added discoveries. We then audit the evaluation design, scoring code, read paths, and current human records of a private synthetic Japan...
  </details>

- **2026-09-14** — Chengxin Yu, Zhaoxin Fan, Faguo Wu et al. — [CoMem: Collective-Individual Memory Synergy for Evolutionary Multi-Agent Systems](http://arxiv.org/abs/2609.15009v1)
  <details><summary>📄 Abstract</summary>
  Designing effective memory mechanisms is crucial for advancing LLM-driven Multi-Agent Systems (MAS), helping agents learn together and perform better over time. While recent work has led to strong cooperation skills, most methods still use flat, unstructured memories, which easily get filled with noise and erase differences between agents. To address this, we introduce the concept of collective-individual memory synergy and propose CoMem, an architecture that unifies both private experience and ...
  </details>

- **2026-09-14** — Alef Iury Siqueira Ferreira, Pedro Lustosa Rege Botelho, Fernanda Silva et al. — [CAL-MOS: Bridging Layers with Adapters for Robust MOS Prediction Across Speech Foundation Models](http://arxiv.org/abs/2609.14956v1)
  <details><summary>📄 Abstract</summary>
  Speech Quality Assessment (SQA) is essential for modern speech technologies, and recent non-intrusive SQA predictors increasingly rely on Speech Foundation Models (SFMs). However, because SFMs expose representations from many layers, it remains unclear which depths are most informative for MOS prediction and how multi-layer information should be combined reliably across backbones and datasets. We benchmark ten SFMs on four MOS datasets under three regimes: full fine-tuning, last-layer probing wi...
  </details>

- **2026-09-14** — Wonje Heo, Shinee Youn, Yooshin Kim et al. — [Tracing the Origins: Legacy Codec Identification in Neural Audio Transcoding](http://arxiv.org/abs/2609.14916v1)
  <details><summary>📄 Abstract</summary>
  Residual Vector Quantization (RVQ)-based neural audio codecs (NACs) enable high-fidelity audio distribution at unprecedentedly low bitrates through discrete token-based representations. However, this shift disrupts traditional forensics, as non-linear neural transcoding obscures the underlying traces of legacy compression. This study defines the forensic gap and proposes a Transformer-based framework designed to leverage the hierarchical and temporal dependencies inherent in RVQ sequences. By mo...
  </details>

- **2026-09-14** — Evgeny S. Saveliev, Krzysztof Kacprzyk, Charlotte Capitanchik et al. — [SeqMaestro: From nucleotide sequences to biological hypotheses through interpretable machine learning](http://arxiv.org/abs/2609.14882v1)
  <details><summary>📄 Abstract</summary>
  Nucleotide sequence analysis is central to problems spanning regulatory genomics, evolutionary biology, and phenotype prediction. Classical bioinformatics methods extract interpretable sequence properties such as motifs and k-mer composition, but their flexibility is limited. In contrast, modern deep learning models can learn powerful predictive representations directly from raw sequences, yet their internal representations and decision mechanisms are difficult to inspect. Interpretable machine ...
  </details>

- **2026-09-13** — Alireza Parchami, Artin Saberpour, Robin Connor Schramm et al. — [Speak to the City: Multimodal Resolution for Outside-the-Vehicle References](http://arxiv.org/abs/2609.14691v1)
  <details><summary>📄 Abstract</summary>
  As autonomous vehicles and Extended Reality (XR) headsets enable novel in-car interactions, seamlessly querying physical landmarks, known as Outside-the-Vehicle Referencing (OVR), remains challenging due to ego-motion and referential ambiguity. We present a robust, multimodal OVR framework fusing user gaze and natural language to identify Points of Interest (POIs). To address the scarcity of dynamic vehicular data, we developed a VR-based pipeline synchronizing 360-degree transit videos with veh...
  </details>

- **2026-09-13** — Tobias Labarta, Frederik Pahde, Novak Boskov et al. — [Safety Signals to Verify NetOps Agents with Action-Level Granularity](http://arxiv.org/abs/2609.14422v1)
  <details><summary>📄 Abstract</summary>
  Agentic Network Operations (NetOps) are an emerging paradigm promising to enable workload-aware, self-adjustable, and reliable autonomous networks. While agents have proven their value in incident summarization and telemetry signal extraction, their effectiveness as autonomous control-loop engines heavily relies on their long-horizon reliability. One such setting is the datacenter fabric, where an agent must respond to alarms and operator intents while abstaining from high-risk actions that may ...
  </details>

- **2026-09-13** — Zhiling Chen, Jingzhan Ge, Ruimin Chen et al. — [Task-Specified Active Metrological Inspection with Measurement-Steered VLA Manipulation and Deterministic Evidence Gating](http://arxiv.org/abs/2609.14219v1)
  <details><summary>📄 Abstract</summary>
  High-mix low-volume (HMLV) manufacturing requires inspection systems to adapt to changing parts, specifications, and work orders without repeated task-specific programming. Existing inspection automation typically assumes predefined sensing sequences, while general purpose robot agents optimize task completion rather than the completeness and validity of metrological evidence. We formulate task-specified active metrological inspection and propose From Requirements to Admissible Metrological Evid...
  </details>

- **2026-09-13** — Constantinos Papantoniou, Brian Hilton — [ANASSA: An Agentic AI Orchestration Framework for Spatial Intelligence](http://arxiv.org/abs/2609.14824v1)
  <details><summary>📄 Abstract</summary>
  The emergence of large language models (LLMs) and large multimodal models (LMMs) has enabled a new class of agentic systems capable of integrating natural language understanding with tool-based execution. In geographic information systems (GIS), this shift is transforming traditional, expert-driven workflows into semiautonomous systems that can interpret user intent, construct spatial workflows, and execute geospatial analysis tasks. However, existing approaches remain limited by fragmented inte...
  </details>

- **2026-09-13** — Ji Lu, Lifei Liu, Haoran Yu et al. — [MedTRACE: Tool-Augmented Multimodal Clinical Reasoning Agents for Evidence-Grounded Decision-Making](http://arxiv.org/abs/2609.14823v1)
  <details><summary>📄 Abstract</summary>
  Multimodal clinical decision-making requires reliable reasoning over heterogeneous evidence from electronic health records, medical images, and physiological signals. Existing models typically map these inputs directly to diagnoses without explicitly assessing evidence sufficiency, tool-use requirements, or diagnostic uncertainty. This paper presents MedTRACE, a tool-augmented multimodal clinical reasoning agent for evidence-grounded decision-making. MedTRACE uses modality-specific encoders to c...
  </details>

- **2026-09-13** — Ji Lu, Huiran Duan, Bo Zhao et al. — [Decision-Oriented Uncertainty Quantification for Risk Control in Earth System Spatiotemporal Foundation Models](http://arxiv.org/abs/2609.14821v1)
  <details><summary>📄 Abstract</summary>
  Earth system modeling is shifting from task-specific predictors toward foundation models with general spatiotemporal representation capabilities. Although these models can jointly encode dynamic Earth fields, external forcings, and static geographic context for multistep forecasting, accurate point predictions or statistically calibrated intervals alone are insufficient for high-impact applications such as extremeweather warning, flood control, renewable-energy dispatch, and emergency resource a...
  </details>

- **2026-09-13** — Andre Panossian — [Transformed in Translation: Two-Stage Structural Uncertainty in LLM-Based Scientific Autoformalization](http://arxiv.org/abs/2609.14808v1)
  <details><summary>📄 Abstract</summary>
  Scientific autoformalization turns verbal accounts into executable mathematics, but executable code does not settle which model has been constructed. We examine two sources of structural uncertainty: the formalizer that generates a response law, and the recurrence that turns that law into trajectories. In secondary analyses of an openly archived crossed experiment, we studied 320 response maps generated by two pinned language-model formalizers from five engineered cognitive accounts within one s...
  </details>

- **2026-09-13** — Aashish Bohra, Vivek Vijay — [WaVeFuse: Regime-Adaptive Equity Index Forecasting via Channel-Wise Wavelet Denoising and Vertical Attention Fusion](http://arxiv.org/abs/2609.14733v1)
  <details><summary>📄 Abstract</summary>
  Hybrid Deep Learning for equity index forecasting is limited by three problems: propagation of OHLCV noise into derived technical indicators (TIs), channel-indiscriminate multi-scale decomposition that conflates heterogeneous frequency signatures, and static multi-branch fusion that cannot adapt to market regime shifts. WaVeFuse addresses these limitations through a unified dual-branch architecture. Symlet-4 wavelet denoising (level 2, MAD soft threshold) suppresses microstructure noise in OHLCV...
  </details>

- **2026-09-13** — Zhibin Jiao, Xiangjing An — [SH-WRNN: Implicit Spherical Harmonics Weight Field Routing Neural Networks for Asymmetric Edge Intelligence](http://arxiv.org/abs/2609.14614v1)
  <details><summary>📄 Abstract</summary>
  Deep learning architectures remain rigidly built upon traditional fully connected layers. While networks scale up, few challenge this foundational root. In this work, we reshape this paradigm by transforming the core synapse weight matrix from static, discrete parameters into a differentiable, continuous field governed by spherical harmonics functions. We introduce the Implicit Spherical Harmonics Weight Field Routing Neural Network (SH-WRNN), which constrains weight matrices within a continuous...
  </details>

- **2026-09-13** — Eduin E. Hernandez, Luis F. Garcia, Nurassyl Askar et al. — [Theseus in the Graph: Towards Traceable Multi-Hop Graph Navigation](http://arxiv.org/abs/2609.14528v1)
  <details><summary>📄 Abstract</summary>
  Multi-Hop Knowledge Graph Question Answering (KGQA) tasks require models to assemble relational evidence along paths in a KG to answer natural-language questions. However, existing KGQA systems typically focus on predicting the final answer without explicitly modeling or validating the intermediate reasoning steps, obscuring whether the correct answers arise from faithful multi-hop reasoning. To address this limitation, we re-frame multi-hop KGQA as a question-conditioned graph navigation proble...
  </details>

- **2026-09-13** — Bhargav Lad, Yifan Hao — [Retrieval-Guided Fine-Tuning as Noisy Estimation: Risk bounds and Architectural Analysis](http://arxiv.org/abs/2609.14485v1)
  <details><summary>📄 Abstract</summary>
  Retrieval-Guided Fine-Tuning (RAG-FT) incorporates retrieved data directly into the training objective, but the statistical consequences of noisy retrieval during training remain theoretically undercharacterized. We study this question by modeling RAG-FT as an estimation problem in a multi-task linear regression framework, using an OLS proxy for single-layer linear self-attention to obtain finite-sample risk bounds. Under homoscedastic retrieval noise, we show that retrieval failure decays expon...
  </details>

- **2026-09-13** — Zhixuan Chen, Jialiang Lu, Zhong Ye et al. — [PRI-Net: A Lightweight Multimodal Framework for 3D UAV Localization](http://arxiv.org/abs/2609.14469v1)
  <details><summary>📄 Abstract</summary>
  Accurate 3D localization of unmanned aerial vehicles (UAVs) remains challenging for existing multimodal approaches due to sparse LiDAR geometry, modality-imbalanced fusion, and redundant feature transmission over constrained edge-to-server links. To address these limitations, we propose PRI-Net, an efficient and lightweight multimodal fusion framework for UAV localization that integrates point cloud splatting, residual attention fusion, and an information bottleneck. Specifically, a 3D point clo...
  </details>

- **2026-09-13** — Kazutoshi Sasahara, Aoi Naito, Ryo Fujie — [A latent dimension of Condorcet's jury theorem for multiple AI advisers](http://arxiv.org/abs/2609.14438v1)
  <details><summary>📄 Abstract</summary>
  When the same question is asked of multiple AI advisers, as in self-consistency and LLM-as-a-judge panels, Condorcet's jury theorem predicts that adding independent, competent advisers makes the majority more reliable. The theorem, however, has a latent dimension when viewed from the user's vantage: adding advisers also makes disagreement more visible. A binomial model reveals that this ``visible dissent'' becomes nearly inevitable as the number of advisers grows, and that reliability and disagr...
  </details>

- **2026-09-13** — Haoran Zhang, Zian Mao, Shufen Chu et al. — [Multi4D: an end-to-end neural network for structural determination at complex material interfaces](http://arxiv.org/abs/2609.14348v1)
  <details><summary>📄 Abstract</summary>
  Heterogeneous interfaces dictate the performance and degradation of functional materials, making it essential to link local structural variations with macroscopic failure mechanisms to guide future materials design. Yet structural heterogeneity, phase overlap, and local disorder produce highly convoluted diffraction signatures, making extended transition regions difficult to interpret at atomic resolution across large fields of view. Here, we introduce Multi4D, a physics-informed neural network ...
  </details>

- **2026-09-13** — Ziyu Zhang, Yun Chen, Taihui Wang et al. — [Modeling, Scaling, and Decoding: Optimizing Controllable Speech Generation with Nonverbal Vocalizations](http://arxiv.org/abs/2609.14231v1)
  <details><summary>📄 Abstract</summary>
  Controllable synthesis of nonverbal vocalizations (NVVs) is es- sential for natural and expressive speech, but remains challeng- ing due to their acoustic diversity and imbalanced distribution in existing corpora. To address these challenges, we develop an NVV-aware DiTAR system that models continuous speech latents, encodes the 16 target NVV categories as dedicated to- kens, and adapts stop prediction to distinguish mid-utterance vocalizations from utterance boundaries. Training begins with lar...
  </details>

- **2026-09-12** — Metin Alp Dogan, Edward Sun, Feng Xu et al. — [Visible Touch: Rendering Contact for Visuomotor Policies](http://arxiv.org/abs/2609.14156v1)
  <details><summary>📄 Abstract</summary>
  Integrating contact information into visuomotor policies remains an open problem. Touch is essential to robust manipulation, yet most modern policies, including pretrained vision-language-action (VLA) models, operate from vision and proprioception alone. Existing approaches to closing this gap require specialized tactile hardware, add separate tactile encoders, or commit to non-image policy backbones, all incompatible with the modern paradigm of image-conditioned policies built on pretrained 2D ...
  </details>

- **2026-09-12** — Qiyang Sun, Langqing Zhang, Yupei Li et al. — [A New Transformer-Based Approach for Audio-Based Kinship Verification and a New Uncontrolled Mandarin Kinship Speech Dataset](http://arxiv.org/abs/2609.14145v1)
  <details><summary>📄 Abstract</summary>
  Kinship verification is a task involving determining whether two individuals share a first-order kin relation. To tackle this task, we propose CONVTRAP-TN, a new architecture for audio-based kinship verification, and conduct an ablation study on the proposed model. To the best of our knowledge, we are the first to apply the successful transformer architecture to the task of audio-based kinship verification. Furthermore, we also collect a custom speech dataset, ARKIN, which accurately reflects ev...
  </details>

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


### 📂 watermark
*水印与溯源 / Watermarking & Provenance* — 13 papers

- **2026-09-14** — Zvi Kons, Avihu Dekel, Hagai Aronowitz et al. — [Word Timestamps and Speaker Attribution with a Non-Autoregressive LLM](http://arxiv.org/abs/2609.15218v1)
  <details><summary>📄 Abstract</summary>
  Timestamps and speaker attribution are useful additions to speech recognition, creating a rich text transcript. This information can either be extracted during transcription or aligned to a given transcript. In this paper we present models that add timestamps and speaker information to a given transcript using a non-autoregressive LLM-based architecture. Compared to an autoregressive model built from similar components, the models are more accurate and annotate a given transcript one to two orde...
  </details>

- **2026-09-14** — Meiduo Chong, Shaolei Zhang, Ju Fan et al. — [EvoOntology: A Self-Evolving Ontology Layer for Data Agents](http://arxiv.org/abs/2609.15779v1)
  <details><summary>📄 Abstract</summary>
  Data agents aim to fulfill natural-language instructions over heterogeneous data, including tables, files, and databases. However, data agents face a challenging agent-data gap: heterogeneous data resides outside the agent, while the agent can access it (e.g., column names and file paths) only through generic tools. Existing approaches either let agents directly explore raw data sources or inject manually constructed semantic layers into prompts. However, neither scales well to large heterogeneo...
  </details>

- **2026-09-14** — Mengyi Deng, Xin Li, Duyi Pan et al. — [RESKILL: Explicit Failure Attribution and Structured Repair for Interactive Language Agents](http://arxiv.org/abs/2609.15684v1)
  <details><summary>📄 Abstract</summary>
  Language agents increasingly rely on reusable skills, but post-failure repair is often handled by opaque one-shot reflection: a model generates a skill patch without explicitly maintaining how failure explanations relate to candidate repairs or how unsuccessful retests should influence later edits. We introduce RESKILL, a structured repair framework that maintains an explicit repair state across repair rounds. Given a failed rollout, the framework links failure hypotheses to candidate skill patc...
  </details>

- **2026-09-14** — Lei Qu — [From Ideas to Actions: A Public-Data Decision-Support Toolchain Across the Venture Lifecycle](http://arxiv.org/abs/2609.15219v1)
  <details><summary>📄 Abstract</summary>
  Founders face two linked decisions: whether to pursue an idea before founding, and which operating actions and capital partners fit afterward. We present a public-data decision-support toolchain combining time-bounded proposal profiling, market and moat checks, and deterministic aggregation with auditable investor-company event chains for retrospective analysis. Pre-founding: (a) After threshold selection on 198 development companies, the frozen pipeline achieves F0.5=0.5357 [0.412, 0.655] on an...
  </details>

- **2026-09-13** — Genliang Zhu — [AcquireBound: Runtime Authorization for Resources Acquired by AI Agents](http://arxiv.org/abs/2609.14744v1)
  <details><summary>📄 Abstract</summary>
  By acquiring compute, credentials, accounts, services, and other agents, autonomous AI agents can introduce new authority into a task. Payment, budget, OAuth, mandate, and fulfillment checks can validate transaction conditions without deciding whether a returned resource may become usable authority. This post-fulfillment activation gap spans tool-mediated creation, inter-agent delegation, and agentic commerce. We present AcquireBound, a provenance-bounded runtime authorization architecture. It q...
  </details>

- **2026-09-13** — Tsz Wai Ko, Jiaru Bai, Thomas Swanick et al. — [El Agente Potente: High-Throughput Agentic Atomistic Simulations](http://arxiv.org/abs/2609.14840v1)
  <details><summary>📄 Abstract</summary>
  Foundational machine-learning interatomic potentials (MLIPs) are transforming atomistic simulations by achieving near-ab initio accuracy across large chemical spaces at a fraction of the computational cost. A central challenge in using these tools for high-throughput property calculations is translating high-level scientific intent into adaptive simulation campaigns without compromising workflow rigour. We introduce El Agente Potente, an agentic system that combines typed execution graphs with a...
  </details>

- **2026-09-13** — Orion Reblitz-Richardson — [Calibrating Interpretability Instruments Before Trusting Their Verdicts](http://arxiv.org/abs/2609.14754v1)
  <details><summary>📄 Abstract</summary>
  Causal claims about large language model (LLM) internals rest on measurements. Those might include a projection, a cosine, an ablation delta, or an interchange patch among others. These measurements fail in specific, diagnosable ways that return a plausible number instead of an error, so a broken instrument can easily read as a finding. A covariance-matched null can saturate until every direction looks typical, a per-head attribution can overshoot the true residual write threefold on reordered-n...
  </details>

- **2026-09-13** — Dmitry Kuklev — [A Building as a Repository: KIR, a Typed Intermediate Representation for Agent-Authored Building Information Models](http://arxiv.org/abs/2609.14578v1)
  <details><summary>📄 Abstract</summary>
  Autonomous agents that author building information models need more than access to a host API. They need a representation of what they intended, what a compiler decided on their behalf, what was refused, what was observed after execution and what remains unknown. We present KIR, a typed intermediate representation in which a building is authored as a program held in a versioned repository and lowered to host applications as build targets. KIR is organised around seven ways in which a generator w...
  </details>

- **2026-09-13** — Yee Man Choi, Xuehang Guo, Songcheng Cai et al. — [ATTRICITE: Training an Open 4B Model for Citation Recovery toward Faithful Attribution](http://arxiv.org/abs/2609.14248v1)
  <details><summary>📄 Abstract</summary>
  Faithful citation attribution begins with identifying the intended source for a scientific claim. We study this source-identification capability through citation recovery: recovering the paper cited by the original author from a citation-bearing passage. Our evaluation adopts the published author's citation as an observable human attribution signal and uses target recovery as a proxy for progress toward faithful attribution. We introduce ATTRICITE, an open 4B-parameter model trained for tool-usi...
  </details>

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


### 📂 unlearning
*机器遗忘 / Machine Unlearning* — 1 papers

- **2026-09-10** — Rongcan Pei, Zhepei Wei, Shuyao Xu et al. — [Negative Self-Distillation: Learning to Reason by Avoiding Flaws](http://arxiv.org/abs/2609.11699v1)
  <details><summary>📄 Abstract</summary>
  On-Policy Self-Distillation (OPSD) has emerged as a popular paradigm for large language model (LLM) self-improvement, allowing models to act as their own teachers by leveraging privileged information such as ground-truth solutions. However, recent findings indicate that OPSD can severely degrade the performance of LLMs on complex reasoning tasks: By forcing the student to imitate an artificially confident reasoning trace conditioned on privileged information, OPSD inadvertently suppresses expres...
  </details>


### 📂 survey
*综述与系统化 / Surveys & Systematization* — 5 papers

- **2026-09-14** — Steven Ndung'u, Adel Daoud, Ismael Yacoubou Djima et al. — [Transfer Learning for Socioeconomic Estimation in Forced-Displacement Settings](http://arxiv.org/abs/2609.15773v1)
  <details><summary>📄 Abstract</summary>
  Progress in inclusive household surveys has strengthened socioeconomic evidence for forcibly displaced populations, providing indispensable benchmarks on living conditions and welfare. However, these surveys remain resource-intensive and periodic, while conditions can change between rounds, particularly in settings affected by fragility, conflict, and violence. More frequently updated, spatially granular complementary evidence is therefore needed to identify where socioeconomic conditions may be...
  </details>

- **2026-09-13** — Jakub Growiec, Klaus Prettner, Maciej Szkróbka — [Redistributive Policies for the Times of Transformative AI](http://arxiv.org/abs/2609.14750v1)
  <details><summary>📄 Abstract</summary>
  After the arrival of transformative artificial intelligence (TAI), broad-based automation is expected to decrease the labor share and increase income and wealth inequality. Although economic growth is likely to accelerate, most of its gains may accrue to a narrow group of individuals and firms. Hence, if unmitigated by redistributive policy, income and wealth inequality may rise to levels unseen in the industrial economy. Using a unifying theoretical framework, we survey the redistributive polic...
  </details>

- **2026-09-13** — Soobin Cho, Deveshi Modi, Divya Mavinkurve et al. — [Assessing the Applicability of Existing Design Recommendations to AI Companion Design: A Multi-Method Study](http://arxiv.org/abs/2609.14236v1)
  <details><summary>📄 Abstract</summary>
  With the rapid proliferation of large language model (LLM)-based systems, AI companions have emerged as conversational agents designed to cultivate emotional connection rather than primarily to support humans in instrumental tasks. Because engagement with AI companions involves relational, emotional, and potentially long-term interactions, their design is consequential. Prior work has offered guidance for designing trustworthy and relational AI systems and has begun to examine design for AI comp...
  </details>

- **2026-09-10** — Jiani Ding, Minghao Yue, Yongda Zhu et al. — [Learning JWST. I. A Foundation Model for New Population Discoveries and Morphology-Aware Photometric Redshift Measurements in the JADES Survey](http://arxiv.org/abs/2609.11879v1)
  <details><summary>📄 Abstract</summary>
  We present FM-JADES-v1, a self-supervised foundation model for James Webb Space Telescope ({\em JWST}) deep-field science, trained with 482,444 objects from the {\em JWST} Advanced Deep Extragalactic Survey (JADES) Data Release 5 using multi-band imaging and the photometric catalog. The shared embedding space is trained without class labels. We demonstrate that FM-JADES-v1 can serve as a powerful tool for object discovery and improving property measurements using two experiments, blind active di...
  </details>

- **2026-09-09** — Kateryna Karpo, Artem Chernodub — [Larger Context Window, Fewer Overcorrections: Optimizing Prompts and Batching for Minimal-Edit Grammatical Error Correction](http://arxiv.org/abs/2609.10810v1)
  <details><summary>📄 Abstract</summary>
  Minimal-edit Grammatical Error Correction (GEC) is a challenging task for zero- and few-shot prompted Large Language Models (LLMs), which systematically overcorrect and degrade $F_{0.5}$ by rewriting well-formed spans. While fine-tuning provides an effective solution, it imposes substantial infrastructure demands. We introduce a prompt-based approach that closes the gap to fine-tuned models through three advances in GEC prompting methodology. First, we introduce taxonomy-based instructions to en...
  </details>


### 📂 other
*其他安全相关 / Other Security-Related* — 189 papers

- **2026-09-14** — Honghao Lin, David P. Woodruff, Yuan Deng et al. — [Stellar Colosseum: A Many-Agent Harness for Long-Horizon Research in Mathematics and Theoretical Computer Science](http://arxiv.org/abs/2609.15983v1)
  <details><summary>📄 Abstract</summary>
  Language models can produce plausible short proofs, but may still be unreliable on long-horizon research problems, where progress depends on a sequence of uncertain and interdependent decisions. We introduce Stellar Colosseum, a model-agnostic harness for allocating inference across research in mathematics and theoretical computer science. Colosseum explores alternative strategies before proof construction, uses a readiness gate to decide when a route is mature enough to decompose, represents th...
  </details>

- **2026-09-14** — Tobias Ladner, Matthias Althoff — [The Misery of Mechanistic Interpretability: A Formal Perspective](http://arxiv.org/abs/2609.15533v1)
  <details><summary>📄 Abstract</summary>
  Mechanistic interpretability has become the dominant lens for understanding frontier language models, as their inner workings are complex and inherently black boxes. To gain insights into these models, interpretable replacement networks (IRNs) are trained at all layers, exposing interpretable features through sparsely activated neurons. However, the faithfulness of an IRN is usually evaluated only empirically on clean data, and we show that even semantically minor input perturbations flip the do...
  </details>

- **2026-09-14** — Zeyang Li, Sunbochen Tang, Navid Azizan — [Safe Meta-Reinforcement Learning via Information Space Reachability](http://arxiv.org/abs/2609.15915v1)
  <details><summary>📄 Abstract</summary>
  Meta-reinforcement learning (meta-RL) enables agents to adapt to unseen tasks with limited experience. Despite its promise, the application of meta-RL in real-world tasks is hindered by safety requirements, which have been underexplored in prior work. In this paper, we propose a safe meta-RL framework that explicitly accounts for safety during adaptation. Our key insight is to reason about safety in the information space, which captures both the physical state and the agent's belief over the und...
  </details>

- **2026-09-14** — Xiaofeng Mao, Peijia Lin, Shaohao Rui et al. — [LynnReal-Omni: Native multi-modal Video Generation for Agentic Visual Workflows](http://arxiv.org/abs/2609.15863v1)
  <details><summary>📄 Abstract</summary>
  Video diffusion models are stochastic and hard to control: precise content often requires repeated sampling without guaranteed success, and long-horizon scenes drift in appearance, interactions, and temporal coherence. Agentic visual creation provides explicit references, editable 3D scenes, or executable game states for stable control, but does not by itself guarantee high object or character fidelity. Combining the two can enable stable, high-quality generation. To realize this combination, we...
  </details>

- **2026-09-14** — Jocelyn Kang, Caroline Zhang — [KnowBench: Effort Reduction as a Unified, Deployment-Grounded Benchmark for Clinical AI](http://arxiv.org/abs/2609.15794v1)
  <details><summary>📄 Abstract</summary>
  Clinical AI systems are evaluated with instruments built for research settings (reference-based similarity metrics and expert rubric panels) that measure resemblance to an artifact rather than reduction of a burden. We introduce KnowBench, pioneered by Knowtex, whose unifying metric is Effort Reduction (ER): the proportion of system-generated clinical work product accepted by the responsible clinician under expert and safety review. ER is defined once and instantiated per task across the adminis...
  </details>

- **2026-09-14** — Jiajie He, Jiangyuan Hong, Dongling Ni et al. — [Are LLMs Good Financial User Simulators? A Preliminary Study](http://arxiv.org/abs/2609.15727v1)
  <details><summary>📄 Abstract</summary>
  Large language models (LLMs) are increasingly used as user simulators, but their ability to reproduce evolving individual financial decisions remains unclear. We present a preliminary study in a controlled paper-trading environment with 120 volunteers. Participants used non-redeemable virtual funds under real-time market conditions; no real brokerage accounts, real-money positions, or real transaction records were accessed. Given only information available before a prediction cutoff, a simulator...
  </details>

- **2026-09-14** — Lemen Chao, Zixuan Yang, Anran Fang et al. — [Data storytelling meets interpretable machine learning: Decoding AI decisions for non-experts without revealing sensitive data and model details](http://arxiv.org/abs/2609.15722v1)
  <details><summary>📄 Abstract</summary>
  AI-driven automated decision-making requires both predictive performance and interpretability. Recent advances in interpretable machine learning (IML) provide tools for explaining model predictions, but the technical complexity of these explanations may hinder accessibility to non-experts. To address this challenge, this study integrates data storytelling with IML to enhance the explainability of AI-generated decisions for a broader audience. Following the design science research (DSR) paradigm,...
  </details>

- **2026-09-14** — Jinyuan Deng, Yuqi Jiang, Wenjing Huang et al. — [Circuit-MLLM: Topological Logic-Guided Latent-Space Visual Reasoning for Circuit Schematic Understanding](http://arxiv.org/abs/2609.15668v1)
  <details><summary>📄 Abstract</summary>
  Through pre-training on extensive text and image datasets, current multi-modal large language models (MLLMs) achieve strong performance on general tasks. However, circuit schematics present a unique challenge for MLLMs due to their dense component layouts and distinct topological logic, demanding fine-grained structural parsing to extract the electrical semantics. To address this, we propose Circuit-MLLM, a multimodal reasoning framework that reformulates circuit topology analysis as a process o...
  </details>

- **2026-09-14** — JuHeon Ha, Byounghan Lee, Yunseo Choi et al. — [Empathy Is Steerable but Multi-Axial: Mechanism Geometry and Persona Effects in LLMs](http://arxiv.org/abs/2609.15654v1)
  <details><summary>📄 Abstract</summary>
  Activation steering has been used to control traits such as honesty, refusal, and sycophancy, yet supportive empathy is evaluated along multiple dimensions that need not correspond to independently controllable activation directions. Using the EPITOME framework, which decomposes supportive empathy into Emotional Reactions, Interpretations, and Explorations, we study three instruction-tuned LLMs and ask whether candidate directions derived from these labels produce distinguishable intervention ef...
  </details>

- **2026-09-14** — Haoyu Wang, Jing Yang, Chenyu Liu et al. — [Graph Attention Design Choices Matter: A Controlled Study of LoRA-Adapted Audio Anti-Spoofing](http://arxiv.org/abs/2609.15650v1)
  <details><summary>📄 Abstract</summary>
  Audio anti-spoofing systems increasingly combine self-supervised learning, parameter-efficient fine-tuning, and graph-attention-based backends. However, performance gains in such systems are often entangled with concurrent changes in the backbone, fine-tuning strategy, and training protocol, making the independent contribution of graph attention design difficult to isolate. To address this issue, we conduct a systematic controlled study of the graph attention layer under a unified experimental s...
  </details>

- **2026-09-14** — Son Ho, Cédric Fournet, Jonathan Protzenko et al. — [Scaling Verification of Cryptographic Software with Aeneas, Rust, and Lean](http://arxiv.org/abs/2609.15648v1)
  <details><summary>📄 Abstract</summary>
  We develop a new methodology for verifying cryptographic software. We target production code written in Rust for performance and system integration, rather than verification convenience. Rust's ownership discipline enables Aeneas to extract a pure model of this code in Lean, relieving us from low-level reasoning about pointer liveness and aliasing. Lean's extensibility lets us develop tactics and libraries that greatly simplify reasoning about extracted Rust code.   We design and tune our toolch...
  </details>

- **2026-09-14** — Jiawei Li, Fabio Bonassi, Johan Sundström et al. — [On the role of the tokenizer in ECG transformer models](http://arxiv.org/abs/2609.15433v1)
  <details><summary>📄 Abstract</summary>
  Tokenization determines both the physiological content presented to an ECG Transformer and the sequence over which attention operates. We compare eight tokenization strategies across Transformer, Informer, Reformer, and FEDformer on the nine-label CPSC2018 classification task. The input projection and principal backbone capacity are controlled to isolate the effect of token construction. Median-beat and HeartLang tokenization achieve mean macro-AUCs of 0.893 and 0.889 across the four backbones, ...
  </details>

- **2026-09-14** — Haoxiang Kang, Ming Wen — [SkillLift: Learning Dense Rubrics from Sparse Oracles for Efficient Skill Evolution](http://arxiv.org/abs/2609.15396v1)
  <details><summary>📄 Abstract</summary>
  LLM-based agents increasingly rely on persistent skills, i.e., reusable procedural prompts, to adapt without weight updates. Existing skill self-evolution methods directly revise skill text based on execution feedback, but each oracle evaluation requires a full agent rollout, creating a supervision bottleneck that confines search to failure-patching updates. Our key insight is that ranking is a smoother supervision target than absolute outcome regression: identifying which skill is better requir...
  </details>

- **2026-09-14** — Xudong Yuan, Shunyu Liu, Tongya Zheng et al. — [CodeTS: Verifiable Text-to-Time Series Generation via Executable Code](http://arxiv.org/abs/2609.15393v1)
  <details><summary>📄 Abstract</summary>
  Text-to-Time Series Generation (Text-to-TS) provides a promising paradigm for synthesizing time series from natural language, enabling scenario-specific generation when real observations are scarce or costly to acquire. However, existing methods typically lack an explicit mechanism for deriving generation logic from textual descriptions to guide time series synthesis. In this paper, we propose CodeTS, a verifiable framework that uses code as an intermediate generation interface, reformulating Te...
  </details>

- **2026-09-14** — Konstantinos Varsos, Ramin Khalili, Adamantia Stamou et al. — [A Game-Theoretic Framework for Incentive-Compatible AI training Under Renewable-Energy Constraints](http://arxiv.org/abs/2609.15389v1)
  <details><summary>📄 Abstract</summary>
  As artificial intelligence systems increasingly rely on distributed and collaborative training, the energy footprint of these processes becomes a shared responsibility. Modern AI training often unfolds across heterogeneous compute nodes-ranging from cloud clusters to edge devices-whose energy availability is spatially and temporally variable. At the same time, renewable energy grids experience growing levels of excess generation, creating opportunities to align computational workloads with low-c...
  </details>

- **2026-09-14** — Xinyue Xu, Hongbin Lin, Juangui Xu et al. — [Concept-Grounded Reasoning with Prompt-Driven Localization for Interpretable Structured Report Generation](http://arxiv.org/abs/2609.15334v1)
  <details><summary>📄 Abstract</summary>
  Medical imaging modalities such as ultrasound and X-ray are widely used in clinical practice, where diagnosis follows a structured, evidence-driven workflow aligned with standardized criteria. While multimodal large language models (MLLMs) show promise for automated medical report generation, most existing systems rely on end-to-end multimodal fusion without modeling clinically defined intermediate attributes, leading to limited grounding and interpretability. To address this issue, we propose C...
  </details>

- **2026-09-14** — Chanho Park, Bumsu Park, Soonhee Kwon et al. — [Thinking in Tokens, Talking in Bits: A Practical Interface for Token Communication](http://arxiv.org/abs/2609.15256v1)
  <details><summary>📄 Abstract</summary>
  Advanced artificial intelligence models think in tokens; contemporary communication systems carry bits. The direct way to bridge this gap is to transmit tokens, but that makes a model-specific representation part of the air interface, coupling the endpoints through a shared tokenizer, codebook, and often a neural transceiver. We take a different route: keep bits in the payload and let tokens control how those bits are generated and protected. The resulting token-bit interface transition aligns t...
  </details>

- **2026-09-14** — Rui Lu, Rui Ge, Huanghuang Liang et al. — [ETCInfer: An Energy-efficient Thermal-aware Cooling-joint Scheduler for LLM Inference in AI Datacenters](http://arxiv.org/abs/2609.15230v1)
  <details><summary>📄 Abstract</summary>
  Large language model (LLM) inference in AI datacenters creates a coupled control problem between GPU serving and facility cooling. Raising ambient temperature setpoints can reduce cooling energy and carbon, but also shrinks thermal headroom, induces GPU throttling, and leads to Service-Level-Objective (SLO) violations. In this paper, we study joint cooling--computing control for LLM inference: minimizing per-job GPU-plus-cooling energy while satisfying thermal safety and latency SLO constraints....
  </details>

- **2026-09-14** — Juntong Zhang, Chun Gu, Li Zhang — [X-WBC: A Cross-Embodiment Foundation Model for Humanoid Whole-Body Control](http://arxiv.org/abs/2609.15213v1)
  <details><summary>📄 Abstract</summary>
  Scaling humanoid whole-body control toward general-purpose deployment requires large human motion corpora and training experience shared across robot bodies. Existing methods usually train one policy per robot, leaving motion experience isolated across embodiments. We introduce X-WBC, a cross-embodiment foundation framework that separates relatively shared human motion semantics from embodiment-specific physical execution. Human-centered command tokens align full human motion, robot reference mo...
  </details>

- **2026-09-14** — Sriram Selvam, Anneswa Ghosh — [CITECHOICE: A Causal Audit of How Document Presentation Redistributes Citation Credit in Agentic Search](http://arxiv.org/abs/2609.15164v1)
  <details><summary>📄 Abstract</summary>
  When several retrieved sources support the same claim, an answer engine cites some but not others. We call this decision citation allocation and introduce CITECHOICE, a causal audit of authentic multi-turn agentic search. From 129 everyday-query transcripts, CITECHOICE selects 113 same-call document pairs with independently verified support for the same pre-specified fact, without observing ranks or answer outcomes; blinded human review confirms 103. It runs a hash-verified 2-by-2 replay crossin...
  </details>

- **2026-09-14** — Siran Zhang, Shuming Cheng, Xiang Li et al. — [A train--prune--readout--rewrite workflow for interpretable quantum learning](http://arxiv.org/abs/2609.15139v1)
  <details><summary>📄 Abstract</summary>
  AI for Science aims not only to predict complex physical systems from data, but also to extract mathematical structure and physically testable representations from learned models. Here, a train--prune--readout--rewrite workflow is developed that separates physical-domain grounding from three increasingly stringent analysis claims: algebraically equivalent readout of a trained predictor, compact teacher-faithful symbolic rewriting on the sampled physical domain, and transformation-based tests of ...
  </details>

- **2026-09-14** — Yunhao Feng, Ruixiao Lin, Ming Wen et al. — [HazardAuditor: From Executable Threats to Safer Computer-Use Agents](http://arxiv.org/abs/2609.15134v1)
  <details><summary>📄 Abstract</summary>
  Computer-use agents increasingly interact with browsers, terminals, file systems, and external services, introducing safety risks that emerge through runtime behavior rather than generated content alone. Existing guard models target static prompts and responses and are poorly suited to agent execution; existing executable safety platforms produce evaluation verdicts rather than the normalized supervision a guard model needs to learn across heterogeneous agent frameworks. We introduce HazardAudit...
  </details>

- **2026-09-14** — Kushagra Agrawal, Yuming Feng, Man-Fai Leung — [Translating the Translator: Decomposing the Cost of English-Forced Inter-Agent Communication](http://arxiv.org/abs/2609.15079v1)
  <details><summary>📄 Abstract</summary>
  Multi-agent LLM architectures, such as LangChain and AutoGen, largely assume English as the lingua franca for internal inter-agent communication, even when the end-user task is non-English. We fill this gap by evaluating a two-agent extraction-answer core, with an additional back-translation agent in the English-forced condition, across four typologically diverse languages (Hindi, Chinese, Spanish, Arabic; n = 300 per language) using the Aya-23-8B model. We compare a native-language pipeline to ...
  </details>

- **2026-09-14** — Yu Li, Qikun Cai, Tao Huang et al. — [Semantic-TVM: Structure-Preserving Trustworthy Virtual Memory for Memory-Augmented and Tool-Using Agents](http://arxiv.org/abs/2609.15011v1)
  <details><summary>📄 Abstract</summary>
  Memory-augmented and tool-using agents expose exact private values when remote LLMs process retrieved memory, tool actions, and intermediate observations. One-way masking limits direct exposure but removes values needed for trusted execution and can leak them through later observations. We propose Trustworthy Virtual Memory (TVM), a closed-loop runtime that keeps exact-value state local while presenting a protected view to the remote model. Within this single runtime, Rule-TVM replaces whole pro...
  </details>

- **2026-09-14** — Zhendong Li, Mingze Zhu, Zhou Su et al. — [Discrete Antenna Positioning and Beamforming Design for RIS-Assisted MA Secure ISAC Systems](http://arxiv.org/abs/2609.14974v1)
  <details><summary>📄 Abstract</summary>
  This paper investigates a reconfigurable intelligent surface (RIS)-assisted movable antenna (MA) secure integrated sensing and communication (ISAC) system. In this architecture, the RIS establishes indirect transmission links to provide communication services for multiple legitimate users, while the high spatial diversity gain of MA is leveraged to enhance system security. Then, we formulate an optimization problem to maximize the system total secrecy rate by jointly optimizing the MA position s...
  </details>

- **2026-09-14** —  DeepCybo Team, Yu Bin, Haipeng Cao et al. — [PhysBrain 1.5: From Vision-Language Models to Physical Foundation Models](http://arxiv.org/abs/2609.14973v1)
  <details><summary>📄 Abstract</summary>
  We present PhysBrain 1.5, a unified model for understanding physical environments, generating actions, and predicting future states. Motivated by the physical loop of observation, interaction, and environmental change, we bring these capabilities into a common learning framework. Starting from a general vision--language model, we encode language responses, end-effector motion, and dense visual targets as discrete sequences and jointly optimize them with autoregressive next-token prediction. Pre-...
  </details>

- **2026-09-14** — Yahya Mohamed Elnawasany — [A Corpus-Aligned Uthmani-to-Standard Quranic Word Mapping and a Deterministic Recitation Validator](http://arxiv.org/abs/2609.14967v1)
  <details><summary>📄 Abstract</summary>
  Quranic text is distributed in two orthographic forms that are byte-level distinct: the Uthmani script used in every printed mushaf, and the Standard (Imla'i) Arabic form that every mainstream Arabic NLP tool is built for. The gap is concentrated in one Unicode character, U+0670 (superscript alef), which appears in some of the most frequently recited words in the Quran and is silently mishandled by general-purpose Arabic normalizers. We release a 2,290-pair, corpus-aligned Uthmani-to-Standard wo...
  </details>

- **2026-09-14** — Beibei Jing, Tianle Guo, Youjia Zhang et al. — [MoVT: Video-Augmented Motion Tokenizer for Text-to-Motion Generation](http://arxiv.org/abs/2609.14965v1)
  <details><summary>📄 Abstract</summary>
  Text-driven 3D human motion generation models face significant challenges in responding to diverse and unconstrained textual prompts, primarily due to the limited availability of 3D motion training data. To address this, we introduce MoVT, a novel framework that effectively leverages the extensive range of human action videos to enhance text-to-motion generation. At the core of our approach is the cross-modal augmented motion tokenizer, which projects discrete 3D motion tokens into the 2D domain...
  </details>

- **2026-09-14** — Xinjing Zhou, Jason Mohoney, Samuel Madden et al. — [Chronos: Efficient Bolt-on Branching Across Data Stores for Stateful Agentic Applications](http://arxiv.org/abs/2609.14889v1)
  <details><summary>📄 Abstract</summary>
  Data-centric applications increasingly use speculative execution to explore multiple candidate paths where each path modifies state distributed across heterogeneous data stores. This trend is intensified by the rise of tool-calling agents. Hence, applications need data systems that can create branches quickly, isolate state-modifying paths, and merge changes consistently across stores without imposing substantial query overhead. Existing systems provide only partial support, forcing applications...
  </details>

- **2026-09-14** — Haoran Yu, Lifei Liu, Danping Zhang — [Toward Sustainable AI Deployment: A Carbon-Aware Decision Framework for Enterprise Supply Chain Systems](http://arxiv.org/abs/2609.14881v1)
  <details><summary>📄 Abstract</summary>
  Enterprises deploying AI for supply chain decisions commonly default to the largest available language model, a procurement heuristic that neglects both empirical performance and environmental cost. We benchmark six large language models across 520 supply chain tasks, simultaneously measuring decision quality and estimated generation-related operational carbon. Drawing on the Technology-Organization-Environment (TOE) framework, we develop a Carbon-Aware AI Procurement Framework (CAAPF), a Green ...
  </details>

- **2026-09-14** — Tong Zheng, Xidong Wu, Zheng Zhang et al. — [Dream-RSI: Recursive Self-Improvement through Evolving Worlds](http://arxiv.org/abs/2609.14858v1)
  <details><summary>📄 Abstract</summary>
  Recursive self-improvement is becoming increasingly vital for autonomous AI agents, where progress hinges on discovering high-value solutions across complex domains. The driver of this process is effective exploration, however, managing and improving exploration strategies remains a major bottleneck. Current systems face a fundamental dilemma: fixed strategies fail to adapt as search spaces scale, while online policy optimization requires navigating vast meta-search spaces under delayed and expe...
  </details>

- **2026-09-14** — Matteo Grimaldi, David Klee, Ziling Chen et al. — [Touch2Trace: Tactile-Driven Imitation Learning for Dexterous Cable Tracing](http://arxiv.org/abs/2609.15921v1)
  <details><summary>📄 Abstract</summary>
  Dexterous manipulation of deformable objects demands continuous fingertip-level regulation of pressure, friction, and incipient slip. We study one of the most challenging cases: dexterous cable tracing, feeding a cable through the hand with repeated pinch-and-curl motions of the thumb and index finger. We introduce Touch2Trace, a tactile-driven imitation-learning system for this task, and provide, to our knowledge, the first systematic real-world characterization of how encoder pretraining, cont...
  </details>

- **2026-09-14** — Protik Dey, Mohd Saifuzzaman, Taslima Akter — [More Than Just Access: Generative AI as Communication Intermediary for Blind and Low-Vision Users](http://arxiv.org/abs/2609.15696v1)
  <details><summary>📄 Abstract</summary>
  Generative AI (GenAI) tools are increasingly woven into how blind and low-vision (BLV) people communicate, not only with digital information, but with the physical world and with other people. Tools such as ChatGPT, Google Gemini, Be My AI, and Seeing AI translate visual and textual content into accessible form, and are beginning to substitute for interpersonal requests for help, such as asking a family member to read a label or describe a scene. Drawing on semi-structured interviews with 19 BLV...
  </details>

- **2026-09-14** — Keuntae Kim, Eunhye Jeong, Yong Suk Choi — [CWM: Controllable White-Box Meta-Prompting for Adaptive Retrieval-Augmented Generation and Reasoning Ability](http://arxiv.org/abs/2609.15234v1)
  <details><summary>📄 Abstract</summary>
  Recently, Large Language Models (LLMs) have gained significant attention due to their strong language understanding and generation capabilities, demonstrating impressive reasoning abilities as well as effective utilization of external knowledge. Many studies have proposed methods that specialize in improving performance for individual tasks. However, ironically, only a limited number of attempts have explored general-purpose, task-agnostic methods. In this work, we present a unified framework in...
  </details>

- **2026-09-14** — Akash Kumar Panda, Olaoluwa Adigun, Bart Kosko — [Converting Sequenced Fuzzy Cognitive Maps to Causal Virtual Worlds with Large Video Generators](http://arxiv.org/abs/2609.14985v1)
  <details><summary>📄 Abstract</summary>
  We show how users can create and manipulate causal virtual worlds with large-language-model (LLM) and large-video-model agents. The approach uses feedback fuzzy cognitive maps (FCMs) both to model the granular causal structure of the virtual world and to guide its causal evolution. The local causal rules are partial or fuzzy while the FCM's feedback structure produces global equilibria that define causal scenarios. A sequence of \emph{dynamical} meta-rules of the form ``If $\mathcal{A}$ then $\m...
  </details>

- **2026-09-14** — Jieyuan Liu, Mengzhou Hu, Jefferson Chen et al. — [HypoEvolve: Genetic Algorithms Enable Multi-Agent LLMs to Discover Scientific Hypotheses](http://arxiv.org/abs/2609.15938v1)
  <details><summary>📄 Abstract</summary>
  Scientific agents contribute to hypothesis discovery by synthesizing evidence, assessing proposals, and developing new explanations. Recent systems combine scientific agents with evolutionary search through critique, comparison, and revision. However, how different forms of agent collaboration affect hypothesis quality remains an open question. Answering this question requires separating the effects of agents' scientific capabilities from those of their collaboration. A framework must therefore ...
  </details>

- **2026-09-14** — Sushmita Gupta, Sanjay Seetharaman — [On the Hardness of Maximin Share Allocations](http://arxiv.org/abs/2609.15841v1)
  <details><summary>📄 Abstract</summary>
  The maximin share (MMS) guarantee is a central fairness benchmark for allocating indivisible items. Since Kurokawa, Procaccia and Wang [EC'14, JACM'18] showed that exact MMS allocations need not exist, much work has studied existence and computation of approximate MMS allocations. In contrast, a basic complexity question posed more than a decade ago by Bouveret and Lemaître [JAAMAS'16] has remained unresolved: how hard is it to decide whether an exact MMS allocation exists?   For additive valuat...
  </details>

- **2026-09-14** — Hai-Dang Dang, Bao-Yen Pham, Bao Nguyen et al. — [Assembling the CREW: A Collaborative Multi-agent Reinforcement Learning Framework for Automated Related Work Generation](http://arxiv.org/abs/2609.15721v1)
  <details><summary>📄 Abstract</summary>
  Automatic Related Work Generation (RWG) significantly reduces the human time and effort required to author the Related Work Section (RWS) of a research paper. However, prior methods leveraging multi-agent Large Language Models (LLMs) typically rely on a predefined workflow, where each agent is responsible for a specific step in the entire process. This rigid, static inter-agent coordination limits the adaptive collaboration required to synthesize complex scientific literature. To address this li...
  </details>

- **2026-09-14** — Mohamad Najafi, Hongyun Fu, Mathias Brochhausen et al. — [Knowledge-Enriched Structured EHR Features for 30-Day Hospital Readmission Prediction on MIMIC-IV](http://arxiv.org/abs/2609.15713v1)
  <details><summary>📄 Abstract</summary>
  Recent approaches to 30-day hospital readmission prediction rely on pre-trained language models applied to discharge summaries. Although these methods achieve strong performance, they depend on the availability of clinical notes, incur substantial computational costs, and yield representations that lack interpretability. We propose a knowledge-enriched feature representation that augments structured Electronic Health Record (EHR) data with four medical knowledge sources: disease ontology mapping...
  </details>

- **2026-09-14** — Bernard Reber — [New Conditions for Philosophers to Catch the Wave of Citizen Deliberation in the Age of Artificial Intelligence in advance](http://arxiv.org/abs/2609.15707v1)
  <details><summary>📄 Abstract</summary>
  Powerful technologies labeled ``AI''-without sufficient epistemic caution-are already reshaping political and private life, bringing both new dangers and new opportunities for citizen participation. These range from electoral and legislative engagement to the most ambitious form: political co-creation through citizens' assemblies. Large Language Models (LLMs) could support such processes through moderation, translation, facilitation, summarization, and writing assistance. But this potential rema...
  </details>

- **2026-09-14** — Victor H. Chen, Hairui Yu, Stella K. Chung et al. — [CIDERS: Cloud-Edge LLM Collaborative Learning via Accelerating Personalized Bilevel Optimization](http://arxiv.org/abs/2609.15664v1)
  <details><summary>📄 Abstract</summary>
  Amid the rapid advancement of physical-world intelligence, cloud-edge collaborative large language models (LLMs) have emerged as a promising roadmap for practical LLM deployment. However, existing cloud-edge paradigms struggle to balance global consensus with local personalization, which fails to satisfy the need for a unified knowledge foundation on the cloud and domain-specific adaptation at the edge. To address this, we introduce, for the first time, a personalized bilevel optimization framew...
  </details>

- **2026-09-14** — Gwang-Hyeon Yun, Jong-Hoon Park, Bing Hu et al. — [Multi-View Molecular Representation Learning with Hierarchical Graphs and Contextualized Fingerprints](http://arxiv.org/abs/2609.15611v1)
  <details><summary>📄 Abstract</summary>
  Molecular property prediction requires representations that generalize from limited labeled data to structurally novel compounds. Existing molecular pretraining methods often rely on a single view: graph-based approaches model atom-bond topology but provide limited fragment-level supervision, whereas fingerprint descriptors encode chemical patterns but are typically used as fixed auxiliary features. We propose HiFi-Mol, a multi-view framework that separately pretrains a hierarchical graph encode...
  </details>

- **2026-09-14** — Simonetta Liuti, Zaki Panjsheeri, Kemal Tezgin — [Generalized Parton Distributions: Phenomenology, Extraction, and Hadron Imaging](http://arxiv.org/abs/2609.15583v1)
  <details><summary>📄 Abstract</summary>
  Generalized Parton Distributions (GPDs) provide a framework for investigating the correlated momentum and spatial structure of quarks and gluons in hadrons and for accessing fundamental properties such as angular momentum and the QCD energy-momentum tensor. In this review, we discuss the present status of GPD phenomenology, emphasizing the challenges involved in connecting deeply virtual exclusive measurements to the underlying partonic structure. We organize this problem in terms of two success...
  </details>

- **2026-09-14** — Haoting Alexa Yu, Bea Wohl — [Who Chooses the Artwork? Curatorial Agency and Distributed Intent in Botto](http://arxiv.org/abs/2609.15548v1)
  <details><summary>📄 Abstract</summary>
  Botto is often described as a decentralized autonomous artist, but its authorship cannot be located in image generation alone. This paper examines Botto as an agentic curatorial system in which generation, ranking, voting, feedback, and minting form a recursive loop. Drawing on Botto's documentation and prior accounts of the project, we argue that agency in Botto is distributed but asymmetrical: community participants influence artistic direction through voting and governance, while Botto's inte...
  </details>

- **2026-09-14** — Guillermo Herrera Sánchez, Daniel Gradeci, Daniele Ramsay et al. — [The life and death of football team runs: survival of collective modes shapes Lévy-like transport](http://arxiv.org/abs/2609.15541v1)
  <details><summary>📄 Abstract</summary>
  Broad run-length distributions and short-lag superdiffusion have recently been reported in football players and team centroids, prompting a collective-foraging interpretation. The mechanism linking these player- and team-level signatures remains unclear. Using SoccerMon GPS data from 66 tracked team-match records across 62 fixtures in the Norwegian women's top-flight Toppserien, we asked whether player transport is inherited from a translating team mode and what controls the lifetime of that mod...
  </details>

- **2026-09-14** — Doan Dai Nguyen, Ana Bušić — [Stability in stochastic hypergraph matching III: general reneging](http://arxiv.org/abs/2609.15532v1)
  <details><summary>📄 Abstract</summary>
  In many real-life matching problems, waiting agents might abandon before being matched, such as patients deceasing before receiving organs, passengers/drivers cancelling ride requests, or raw materials/intermediary products degrading in production lines. This poses the need for incorporating reneging in stochastic matching models.   In this work, we consider matching models on hypergraphs with batch arrivals and general-weight matchings. Since our model allows fractional weights, we may not be a...
  </details>

- **2026-09-14** — Franck Signe, Hippolyte Pilchen, François Yvon et al. — [To Each Language Its Tokenizer: Modular Tokenizers for Efficient Multilingual LLMs](http://arxiv.org/abs/2609.15528v1)
  <details><summary>📄 Abstract</summary>
  Multilingual Large Language Models (LLMs) traditionally rely on a single vocabulary shared by all supported languages, which can lead to uneven compression across them. Moreover, their large embedding and output matrices increase memory usage and slow inference, notably for small-scale models. It is also wasteful as models are often used for only a subset of languages. To address these issues, we introduce a modular framework for multilingual model training. First, we propose methods to learn la...
  </details>

- **2026-09-14** — Xiang Fang, Feng Guo, Shengzhao Hou et al. — [Canonical analytic realizations of hyperbolic determinantal processes](http://arxiv.org/abs/2609.15506v1)
  <details><summary>📄 Abstract</summary>
  Krishnapur asked whether the invariant hyperbolic determinantal point processes on the disk admit a random analytic zero-set interpretation at noninteger parameters. We construct such a realization for every positive real parameter as the full compact-open limit in distribution of normalized finite Blaschke products. The zeros determine the modulus and normalized analytic shape, leaving one independent uniform phase. We prove exact Möbius covariance and classify all realizations with this covari...
  </details>

- **2026-09-14** — Nikita Markarian — [Harmonic sums and the Galois group of the Mellin-KZ difference equation](http://arxiv.org/abs/2609.15463v1)
  <details><summary>📄 Abstract</summary>
  We identify the universal Galois group of the difference equation obtained by the Mellin transform of the Knizhnik-Zamolodchikov equation with the prounipotent group associated with the transport Hopf algebra of Deligne and Terasoma studied in \cite{Markarian}. At each finite weight, we realize the Picard-Vessiot ring by finite multiple harmonic sums. We also interpret the classical Gamma-corrected projected associator as the comparison between finite and regularized asymptotic fibers in this re...
  </details>

- **2026-09-14** — Xintong Fang, Zhiyuan Fang, Rengan Xie et al. — [ESG: Generating Physically Consistent Dynamic 3D Scenes from Text Descriptions](http://arxiv.org/abs/2609.15392v1)
  <details><summary>📄 Abstract</summary>
  Recent progress in image and 3D scene generation has enabled increasingly realistic static environments, yet most methods remain confined to such static configurations. Generating dynamic scenes from natural language is fundamentally challenging: it requires joint reasoning over scene structure, temporal evolution, and physical feasibility, while ensuring reliable execution in modern physics engines. We present a unified framework for generating physically consistent dynamic 3D scenes from text,...
  </details>

- **2026-09-14** — Jochen Madler — [SlopShape: Identifying AI-Generated Commercial Web Content](http://arxiv.org/abs/2609.15369v1)
  <details><summary>📄 Abstract</summary>
  Word-level detectors identify unedited AI-generated text almost perfectly, but the literature documents their brittleness under rewording, and a word-level score neither characterizes a text nor identifies which AI model wrote it. We ask whether AI-generated text can be identified one level deeper, from structural signatures: how information is presented, in what order, with what evidence, and in what voice. We replicate StoryScope (Russell et al., 2026), which showed such patterns for AI-genera...
  </details>

- **2026-09-14** — Fabian Frank, Warut Suksompong — [Reconfiguration in Fair Division Revisited](http://arxiv.org/abs/2609.15358v1)
  <details><summary>📄 Abstract</summary>
  We revisit reconfiguration in the fair allocation of indivisible goods, where the goal is to transform one fair allocation into another through a sequence of exchanges while preserving fairness at every step. Our focus is on the hierarchy of envy-freeness up to $k$ goods (EF$k$). We show that for any fixed $k$, two EF1 allocations with the same size vector need not admit a reconfiguration path whose intermediate allocations satisfy EF$k$. This impossibility persists even when the two allocations...
  </details>

- **2026-09-14** — Tamanna Kumavat, Georg Brunner, Kyriakos Flouris — [Parameter-Efficient Adaptation of Pretrained Language Models for Time-Series Forecasting](http://arxiv.org/abs/2609.15344v1)
  <details><summary>📄 Abstract</summary>
  We study the adaptation of pretrained language models to univariate time-series forecasting through a parameter-efficient transfer learning framework, with the goal of understanding which design choices drive effective cross-modal transfer. While language models operate on discrete textual tokens, time series consist of continuous numerical observations with temporal dependencies. To bridge this modality gap, we project fixed-length time-series patches directly into the embedding space of a pret...
  </details>

- **2026-09-14** — Luca Müller, Qian Liu, Rolf Drechsler — [LLM-enabled Behavior Driven Development Workflow for Formally Verified Hardware Designs](http://arxiv.org/abs/2609.15318v1)
  <details><summary>📄 Abstract</summary>
  Recently, the use of Large Language Models (LLMs) for different tasks in the Electronic Design Automation (EDA) life-cycle has been studied extensively, but an integrated view is lacking. Specifications are the foundation of this life-cycle, but they suffer from ambiguity when written in natural language, which especially affects the quality of LLM output. Formal specifications mitigate these ambiguities, but they come with their own challenges. On the other hand, Controlled Natural Language (CN...
  </details>

- **2026-09-14** — Yizhou Liu, Fei Tang, Yuchen Yan et al. — [Learning from Reliable Negatives: Confidence-Anchored Test-Time Adaptation for GUI Grounding](http://arxiv.org/abs/2609.15307v1)
  <details><summary>📄 Abstract</summary>
  Graphical User Interface (GUI) grounding is essential for autonomous agents to map natural language instructions to precise screen coordinates. However, existing supervised fine-tuning and reinforcement learning methods are constrained by the high cost of annotation, creating a scalability bottleneck. In this paper, we introduce a label-free test-time training paradigm driven by two key insights: (1) confidence patterns in coordinate tokens are a better indicator than full-sequence confidence, a...
  </details>

- **2026-09-14** — Jugal Garg, Eklavya Sharma, Xiaowei Wu — [Tight Subsidy Bounds for Weighted Proportional Allocation of Mixed Manna](http://arxiv.org/abs/2609.15208v1)
  <details><summary>📄 Abstract</summary>
  We study the problem of fairly allocating m indivisible items among n agents with possibly unequal entitlements in the mixed manna setting, where each item may be perceived as a good or a chore by different agents. We focus on the fundamental fairness notion of proportionality. Since proportional allocations need not exist in this setting, we allow monetary subsidies to restore proportionality while minimizing the total subsidy. When each item's (dis)utility is bounded by 1, a total subsidy of a...
  </details>

- **2026-09-14** — Tong Li, Shuye Ding, Jiachuan Wang et al. — [TEAR: Table Extraction with Attribute Recommendation from Texts via Large Language Models](http://arxiv.org/abs/2609.15205v1)
  <details><summary>📄 Abstract</summary>
  Table extraction from texts is an important task for information systems, and recent approaches that prompt large language models (LLMs) with instructions have drawn great attention for their strong performance. Existing works have assumed the input texts to be table descriptions or specialized documents. However, these efforts have largely overlooked another prevalent category of texts, commonly found in news reports and social media: naturally occurring texts. Extracting tabular information fr...
  </details>

- **2026-09-14** — Mingqian Yu, Wenpeng Zhang, Peilin Zhao — [T-LoopFormer: Token-Level Elastic-Depth Looped Transformers for Latent Reasoning With Dynamic Routing](http://arxiv.org/abs/2609.15160v1)
  <details><summary>📄 Abstract</summary>
  Looped Transformers have recently demonstrated strong performance in both reasoning and language tasks by reusing a shared set of parameters across multiple iterations, achieving parameter efficiency without sacrificing representational power. Besides, looped Transformers perform inference directly in the latent space (latent reasoning) to reduce the number of tokens consumed during inference, thereby achieving improved sample efficiency. However, these models typically apply a fixed recursion d...
  </details>

- **2026-09-14** — Yanping Li, Wei Zhou, Yawen Liu et al. — [PACE: Progressive Angular-to-Norm Contrastive Embedding](http://arxiv.org/abs/2609.15152v1)
  <details><summary>📄 Abstract</summary>
  Multimodal embedding models encode heterogeneous inputs into a shared embedding space, enabling efficient similarity computation across modalities and tasks. Most existing methods optimize cosine-based contrastive objectives, which promote stable training but restrict semantic compatibility to angular geometry, precluding embedding norms from serving as an additional semantic signal. However, directly optimizing the more expressive dot-product similarity, which leverages both angular and norm in...
  </details>

- **2026-09-14** — Muchen Li, Leonid Sigal, Renjie Liao — [MoME: Mixture-of-Memory Embeddings for Context-Aware Sparse Lookup](http://arxiv.org/abs/2609.15126v1)
  <details><summary>📄 Abstract</summary>
  Scaling large language models efficiently has motivated sparse capacity mechanisms such as Mixture-of-Experts and, more recently, conditional memory: token-indexed embedding tables that augment the backbone with cheap parametric lookups. Existing memory-embedding methods retrieve via a deterministic function of the surface form, which collapses different contextual senses of the same token (e.g., python the language vs. the animal) into a single fixed entry. We introduce Mixture of Memory Embedd...
  </details>

- **2026-09-14** — Jianhe Zhao, Yanhua Qiu, Zhiyu Zhang et al. — [LG-VLN: A Zero-Shot Vision-and-Language Navigation Framework with LangGraph State Orchestration](http://arxiv.org/abs/2609.15098v1)
  <details><summary>📄 Abstract</summary>
  Continuous-environment vision-and-language navigation (VLN-CE) requires interpreting natural-language instructions in unseen 3D environments and executing continuous low-level actions. Existing methods often depend on LiDAR, panoramic cameras, or extra sensors; separate geometric-mapping and semantic-navigation visual representations can cause long-trajectory spatial-semantic inconsistencies. We propose LG-VLN, a monocular zero-shot framework with shared visual features and LangGraph-based state...
  </details>

- **2026-09-14** — Tomer Ezra, Tamar Garbuz — [Improved Impossibility Bounds for Maximin Share Allocations](http://arxiv.org/abs/2609.15085v1)
  <details><summary>📄 Abstract</summary>
  The maximin share (MMS) is a central fairness benchmark for allocating indivisible items, but it need not be simultaneously attainable even under additive preferences. While extensive work has developed approximation guarantees, quantitative impossibility bounds have received comparatively little attention. We establish improved asymptotic and constant impossibility bounds for both goods and chores.   For every sufficiently large number $n$ of agents, we construct additive goods instances in whi...
  </details>

- **2026-09-14** — Keunyoung Kim, Nojun Kwak — [MoARa: Module-Aware Rank Allocation and Structure-Preserving Decomposition for Low-Rank LLM Pre-training](http://arxiv.org/abs/2609.15037v1)
  <details><summary>📄 Abstract</summary>
  Low-rank gradient projection reduces the optimizer-state memory cost of large language model (LLM) pretraining, but the steps and wall-clock time needed to reach a target quality remain a meaningful axis for improvement. We attribute this to two design choices in existing methods: the projection-rank budget is allocated uniformly across Transformer modules with heterogeneous projection sensitivity, and projecting a raw gradient attenuates its magnitude and direction jointly. We propose MoARa, wh...
  </details>

- **2026-09-14** — Xu Yuqing, Zhou Liguo, Sun Ze et al. — [Horizon-specific Expert Fusion for Photovoltaic Power Forecasting](http://arxiv.org/abs/2609.15035v1)
  <details><summary>📄 Abstract</summary>
  Short-term photovoltaic power forecasting requires models to represent regular solar cycles and weather-driven fluctuations whose importance changes with the forecast horizon. This study develops a hierarchical ensemble that combines temporal neural models, historical analogs, state climatology, and gradient-boosted trees. Solar geometry and numerical weather forecasts describe the expected generation conditions, while horizon-specific convex weights combine complementary predictions. A separate...
  </details>

- **2026-09-14** — Manling Yang, Remco Chang — [Sensemaking as Artifact: Accumulated Influence in AI-Mediated Information Environments](http://arxiv.org/abs/2609.14911v1)
  <details><summary>📄 Abstract</summary>
  Generative AI is changing what can happen after a source artifact reaches its audience. A viewer's interpretation can now be externalized into a derivative artifact, allowing private sensemaking to become part of subsequent communication. Once such a derivative artifact circulates, it can enter subsequent viewers' information environments and shape the conditions under which their later sensemaking occurs. In this paper, we examine how this shift changes visual information communication. We firs...
  </details>

- **2026-09-14** — Haill An, Suhyeon Kim, Minjun Kang et al. — [MedVA: An End-to-End Neuro-Symbolic Agentic System for Medical Volume Visualization](http://arxiv.org/abs/2609.14874v1)
  <details><summary>📄 Abstract</summary>
  Medical volume visualization requires selecting regions of interest (ROIs) and carefully controlling their relative visual emphasis according to a given clinical intent. Implementing these decisions in conventional workflows demands substantial clinical and visualization expertise and often involves trial-and-error optimization. Recent agentic systems have introduced natural-language interaction and autonomous visualization operations but largely rely on MLLM-based inference throughout the workf...
  </details>

- **2026-09-13** — Jiunn-Tsair Chen, Jia-Shung Wang, Chi-Yun Hsieh et al. — [AutoLab: An Internet-Accessible Experimental Platform for Operational World Models in Wireless Networks](http://arxiv.org/abs/2609.14854v1)
  <details><summary>📄 Abstract</summary>
  Operational World Models (OWMs) require structured interaction with the physical world: they must observe operational state, impose controlled actions, measure consequences, preserve experience, and use that experience to support prediction and preventive decision making. This paper presents Autolab, an Internet-accessible experimental platform that provides these physical grounding functions for wireless-network OWMs. A remote researcher can inspect a live test site, reconstruct recent state hi...
  </details>

- **2026-09-13** — Suzannah E McKinney, Phuc Vu, Samuel A Justice et al. — [A primer on evaluation methods for large language models in healthcare](http://arxiv.org/abs/2609.14819v1)
  <details><summary>📄 Abstract</summary>
  Large language models (LLMs) have a growing range of applications in medicine, and their evaluation is critical for ensuring they provide benefit and not harm. This evaluation can be more challenging than traditional machine learning for many reasons, including probabilistic and open-ended outputs, and behavior that shifts with prompt design and accumulated context. This review covers four key areas of LLM evaluation: principles of study design, statistical methods, capability evaluation and cli...
  </details>

- **2026-09-13** — Roba Hassan, Nahla Aboromi, Naomi Unkelos-Shpigel — [Trust by Design: Trust Calibration Through Non-Advisory Socratic Dialogue in Conversational Agents](http://arxiv.org/abs/2609.14818v1)
  <details><summary>📄 Abstract</summary>
  As conversational AI systems increasingly operate in sensitive domains, the central challenge shifts from usability to trust calibration, ensuring that users rely on systems neither too much nor too little. Systems that provide advice or interpretations risk encouraging inappropriate reliance, particularly when users perceive AI outputs as authoritative. We present CASELy, a conversational agent explicitly designed to limit its own authority through non-advisory Socratic dialogue. The agent asks...
  </details>

- **2026-09-13** — Mingze Yin, Xiaohan Wang, Dian Li et al. — [Func-R1: Incentivizing Mathematical Function Reasoning in Multimodal Large Language Models](http://arxiv.org/abs/2609.14779v1)
  <details><summary>📄 Abstract</summary>
  Performing deliberate mathematical reasoning in visual contexts is a hallmark of advanced Multimodal Large Language Models (MLLMs) and requires a sophisticated synthesis of perceptual grounding and symbolic logic. However, in the realm of mathematical functions, our investigation reveals a critical modality interference phenomenon: even advanced models, while performing textual computational reasoning, tend to disregard or misinterpret essential visual cues. To address this challenge, we propose...
  </details>

- **2026-09-13** — Boqin Yuan, Xiaoyi Gu, Fiona Li et al. — [CALICO: A Human-Centered, Codebook-Aligned System for Annotation](http://arxiv.org/abs/2609.14726v1)
  <details><summary>📄 Abstract</summary>
  Large language models are increasingly used to scale codebook-based annotation in scientific research, but existing workflows provide limited support for translating domain experts' codebooks into reliable, revisable, and auditable prompts. Prompts are often treated as fixed instructions and hidden from annotators, making it difficult for non-technical domain experts to diagnose and correct model behavior when outputs violate codebook guidelines. In this paper, we present CALICO, a human-centere...
  </details>

- **2026-09-13** — Natarajan Chidambaram, Mauro Dalle Lucca Tosi, Jordi Cabot — [A Two-Dimensional Study of the Model Context Protocol: Publication and Adoption](http://arxiv.org/abs/2609.14721v1)
  <details><summary>📄 Abstract</summary>
  The Model Context Protocol (MCP), released by Anthropic in November 2024, standardizes how large language model applications connect to external tools and data sources. Despite MCP's rapid growth, no study has jointly characterized its emergence in the research literature, its adoption on GitHub and the relationship between them. We address this gap with a longitudinal, two-dimensional study of 802 MCP-related publications and 33,319 GitHub repositories. We characterize their growth and identify...
  </details>

- **2026-09-13** — Jahyun Koo, Sunghyeon Woo, Jaeeun Kil et al. — [Carryover Drafting: Recycling Rejected States for Speculative Decoding](http://arxiv.org/abs/2609.14717v1)
  <details><summary>📄 Abstract</summary>
  Speculative decoding accelerates LLM inference by verifying multiple drafted tokens in parallel, allowing a single target forward pass to accept several tokens. By construction, verification computes representations for both accepted and rejected tokens. Yet, conventional drafters retain only the representations of accepted tokens, leaving the substantial verifier computation spent on rejected tokens effectively wasted. We find that these discarded hidden states generated during target forward r...
  </details>

- **2026-09-13** — Abdalwhab Bakheet Mohamed Abdalwhab, Giovanni Beltrame, David St-Onge — [Learning Multi-Agent Task Assignment and Navigation in the Factory: from Simulation to Real Robots](http://arxiv.org/abs/2609.14567v1)
  <details><summary>📄 Abstract</summary>
  Reinforcement learning (RL) has shown considerable promise for robotic decision-making, yet deploying multi-agent RL (MARL) on physical multi-robot systems in industrial environments remains challenging. This paper investigates the real-world applicability of decentralized MARL for multi-robot multi-machine tending. We propose Feature-fusion Multi-Agent Proximal Policy Optimization (FMAPPO), which fuses 2D LiDAR measurements with task-specific state information to enable safe decentralized multi...
  </details>

- **2026-09-13** — Yuchen Guan, Jiaye Liu, Yifei Han et al. — [TATK: Triple-Aware Top-K Learning with Knowledge-Grounded Verification for LLM-based Sequential Recommendation](http://arxiv.org/abs/2609.14565v1)
  <details><summary>📄 Abstract</summary>
  LLM-based sequential recommenders usually cast next-item prediction as text generation, but this interface is poorly matched to full-catalog top-K ranking. We propose TATK, a Triple-Aware framework that couples Top-K Learning (TKL) with Knowledge-Grounded Verification (KGV) for LLM-based sequential recommendation. Top-K Learning combines context-aware metadata-KG prompt grounding with position-aware top-K rewards, aligning training with ranking utility; Knowledge-Grounded Verification then appli...
  </details>

- **2026-09-13** — Toqeer Ali Syed, Ali Akarma, Adeel Ahmad et al. — [OptoAgent: A Trustworthy Multi-Agent Framework for Opportunistic Vision Micro-Screening in Classroom Environments](http://arxiv.org/abs/2609.14514v1)
  <details><summary>📄 Abstract</summary>
  A child with reduced distance vision often does not know that anything is wrong. Children adapt, move closer, and rarely report the difficulty, so the problem can survive years of schooling before an adult notices. School screening addresses part of this, but it runs on a schedule, depends on staffing, and is separated from the classroom moments where the difficulty appears. Smartphone and web-based acuity tests have widened access, yet every one of them still needs somebody to start a test. We ...
  </details>

- **2026-09-13** — Xiaopeng Chu, Jianbo Zhu, Mingmin Jin et al. — [VARG: Value-Aware and Ranking-Aligned Generative Retrieval for Dynamic E-commerce Search](http://arxiv.org/abs/2609.14493v1)
  <details><summary>📄 Abstract</summary>
  Integrating recall and pre-ranking in e-commerce search requires candidate generation to account for relevance, personalization, and business value before final ranking. To this end, we present VARG, a generative retrieval system for Tmall App search that directly admits generated item candidates to the existing final ranker. VARG-ID constructs semantic prefixes using RQ-VAE, enhances search relevance through bidirectional query-item contrastive learning, and combines these prefixes with a value...
  </details>

- **2026-09-13** — Avijit Dasgupta, Shayon Dasgupta, Zakaria Laskar et al. — [PuzzleMate: Benchmarking MLLMs for Egocentric Puzzle Assistance](http://arxiv.org/abs/2609.14473v1)
  <details><summary>📄 Abstract</summary>
  Personal AI assistants hold the potential to evolve from digital interfaces into embodied companions capable of guiding users through complex physical activities. For these assistants to become integral to daily life, they must do more than identify objects; they must provide precise, step-by-step instructions that align with a user's real-time progress. While Multimodal Large Language Models (MLLMs) show promise in general visual understanding, their ability to deliver grounded, sequential guid...
  </details>

- **2026-09-13** — Siddhanth Sridhar, Shreya Chaurasia, Baddela Sai Yaswantha Reddy et al. — [Dynamic Learning Solutions: A System for Personalized Educational Video Generation](http://arxiv.org/abs/2609.14408v1)
  <details><summary>📄 Abstract</summary>
  We present an automated pipeline that converts NCERT textbooks into interactive video explanations that respond directly to user queries. A user uploads a PDF and asks a question; the system then generates a video-based explanation as output, handling both text and visual elements from the PDF for multi-modal retrieval and response generation. The pipeline combines a Retrieval-Augmented Generation (RAG) model with generative multimedia components. The RAG stage is optimized for the structure of ...
  </details>

- **2026-09-13** — Chao Shen, Hongwei Zhen, Junyan Shao et al. — [LLaTSA: Large Language Model-Aligned General-Purpose Transient Stability Analysis](http://arxiv.org/abs/2609.14374v1)
  <details><summary>📄 Abstract</summary>
  Dynamic trajectory prediction has become an important paradigm for data-driven transient stability analysis (TSA), yet most existing predictors remain system-specific and require substantial retraining when network configurations, generation mixes, or state-variable sets change. Uni-TSA introduced a general-purpose TSA framework that combines channel-independent modeling with a pretrained large language model (LLM) predictor. Nevertheless, its application to heterogeneous systems is limited by a...
  </details>

- **2026-09-13** — Hyeon Jeon, Jinwook Seo — [ggaction: A Grammar of Graphical Actions](http://arxiv.org/abs/2609.14353v1)
  <details><summary>📄 Abstract</summary>
  A chart may be declarative; authoring it is not. Visualization grammars often describe charts as finished specifications, whereas people construct them through a sequence of authoring actions. This mismatch can make visualization code difficult for humans to interpret and for machines to generate from human intent. ggaction addresses this gap by modeling the chart authoring process itself. In ggaction, individual authoring actions are abstracted as functions, and the authoring process is express...
  </details>

- **2026-09-13** — Quoc-Huy Trinh, Minh-Van Nguyen, Debesh Jha — [AURA: Unified Multimodal Framework for Conversational Music Editing](http://arxiv.org/abs/2609.14344v1)
  <details><summary>📄 Abstract</summary>
  Instruction-guided music editors typically process each request independently, limiting their ability to support workflows in which users progressively refine a track. We introduce AURA, a unified multimodal framework for conversational music editing. AURA uses a multimodal large language model to interpret the complete dialogue history, an optional image, and reference audio, distilling the editing intent into compact concept tokens. A concept-to-audio module injects these tokens and frame-alig...
  </details>

- **2026-09-13** — Nirmal Kumar Jingar — [Policy-Governed Post-Quantum Migration for Legacy Microservices Using Ephemeral Sidecar Architectures](http://arxiv.org/abs/2609.14286v1)
  <details><summary>📄 Abstract</summary>
  The fast development of quantum computing represents a big risk to classical cryptography that is commonly used in cloud native and microservice based enterprise systems. Traditional cryptographic primitives are closely linked to legacy microservices and it is both intricate, hazardous, and disruptive to straight up migrate to post-quantum cryptography (PQC). In a bid to overcome these issues, this research presents a PolicyGoverned Post-Quantum Migration through Ephemeral Sidecar Architectures ...
  </details>

- **2026-09-13** — Zeyu Dong, Benjamin Wang, Joyee W. Jin — [Route, Don't Fix: Regime-Dependent Decoding Correction and a Trajectory-Gated Router for Reliable Clinical LLM Answer Selection](http://arxiv.org/abs/2609.14825v1)
  <details><summary>📄 Abstract</summary>
  Large language models (LLMs) are often deemed unsafe for clinical question answering because of their tendency to hallucinate. Retrieval augmentation, fine-tuning, and external verifiers require new infrastructure that clinical governance must approve and may add latency or extra model calls. Inference-time correction uses the model's internal logit signals, but a fixed transformation need not suit every question. A corrector that improves accuracy by about ten percentage points on a truthfulnes...
  </details>

- **2026-09-13** — Hanyu Liu, Qian Li, Yizhu Ding et al. — [REVOLVE: An Automated Closed-Loop Framework for Evolving Robot Manipulation with Minimal Human Intervention](http://arxiv.org/abs/2609.14633v1)
  <details><summary>📄 Abstract</summary>
  Recent advances in data-driven robot manipulation policies have substantially improved task execution and generalization. However, real-world deployment still relies heavily on humans for failure assessment, correction, and environment reset, while models often fail to continually learn from failures and corrective experience. We present REVOLVE (Robot Evolving via Orchestrated Loops, Verification, and Experience), an automated closed-loop framework for evolving robot manipulation with minimal h...
  </details>

- **2026-09-13** — Hang Cheung, Jinniao Qiu — [SCMO: Stochastic Control for Optimization over Probability Measures on Infinite-Dimensional Spaces](http://arxiv.org/abs/2609.14548v1)
  <details><summary>📄 Abstract</summary>
  We study objective-only optimization of possibly nonconvex and nonsmooth functionals over probability measures on a separable Hilbert space, allowing the optimizer to be intrinsically non-Dirac. We introduce SCMO (Stochastic Control Measure Optimizer), a gradient-free particle method derived from entropy regularized stochastic control. After finite-particle and Galerkin approximations, a Cole--Hopf transform represents the optimal feedback as a Gibbs-weighted terminal displacement. SCMO approxim...
  </details>

- **2026-09-13** — Karthekeyan Chandrasekaran, Raymond Jiang, Krishna Kalathur — [A $(p+q)^{O(pq)}$-approximation for $(p, q)$-Flexible Graph Connectivity](http://arxiv.org/abs/2609.14243v1)
  <details><summary>📄 Abstract</summary>
  In the $(p,q)$-Flexible Graph Connectivity problem, the input consists of non-negative integers $p$ and $q$ and a graph $G=(V, E)$ whose edges are classified into safe and unsafe edges with non-negative edge costs. A subgraph H of G is $(p,q)$-Flex-Connected if every non-empty proper subset of vertices has either at least $p$ safe edges or at least $p+q$ total edges crossing it. The goal is to find a minimum cost subset $F\subseteq E$ of edges such that the subgraph $(V, F)$ is $(p,q)$-Flex-Conn...
  </details>

- **2026-09-13** — Qixuan Zai, Randall Berry — [Multi-Agent Reinforcement Learning in Markets with Congestion](http://arxiv.org/abs/2609.14827v1)
  <details><summary>📄 Abstract</summary>
  This paper investigates multi-agent reinforcement learning (MARL) in settings where firms compete for customers using congestible resources. We consider Bertrand competition in which firms compete by announcing prices and customers choose among firms based on both price and congestion. The relationship between price, congestion and the quantity of customers willing to accept service is governed by an unknown inverse demand curve, which firms must learn through experience. Each firm is modeled as...
  </details>

- **2026-09-13** — Utsav Kumar Nareti, Ayush Bansal, Kumari Priya et al. — [From Visual Feedback to Textual Reviews: A Multi-Agent Vision-Language Framework for Image-Grounded Review Assistance](http://arxiv.org/abs/2609.14761v1)
  <details><summary>📄 Abstract</summary>
  Visual feedback in the form of user-uploaded images and videos is becoming increasingly common in e-commerce platforms because it provides authentic evidence of product quality, defects, packaging conditions, and real-world usage. However, visual feedback alone often lacks the contextual explanations and subjective opinions necessary for informed decision-making, while many users provide limited textual feedback due to the effort required to compose detailed reviews. To bridge this gap, we intro...
  </details>

- **2026-09-13** — Dushyant Rajput, Nirdesh Chauhan, Siddharth Kosaraju — [Depth and Scale in the Sub-150M Regime: JugnuLM-53M vs JugnuLM-110M](http://arxiv.org/abs/2609.14715v1)
  <details><summary>📄 Abstract</summary>
  We scale our conventional sub-150M pretraining recipe from 53.5M to 109.7M parameters, holding the method fixed (Qwen3-style decoder with grouped-query attention, RoPE, SwiGLU, RMSNorm, QK-Norm, and a z-loss; FineWeb-Edu data) and changing only the geometry to a deep-and-thin 23-layer x 576-hidden design. The larger model improves across the board -- BLiMP 78.1 -> 81.3, ARC-Easy 51.4 -> 52.5, WikiText-2 byte-perplexity 2.04 -> 1.95 -- and its 81.3% BLiMP essentially matches GPT-X2-125M (81.28) a...
  </details>

- **2026-09-13** — Advait Deshmukh, Nora Benedict, Melanie Walsh et al. — [The Garden of Forking Prompts: How Users Explore Narrative Space in Story Generation](http://arxiv.org/abs/2609.14677v1)
  <details><summary>📄 Abstract</summary>
  Large language models (LLMs) have changed the way people engage with stories. Drawing on public chatbot logs, we can see that when users generate stories, they iteratively edit their prompts to explore narrative possibilities, adjusting characters, redirecting plots, and swapping fictional universes. As aggregated data, these prompts represent rich traces of creative preference at scale. Yet story generation evaluation benchmarks rely on static, one-shot prompts that cannot capture this explorat...
  </details>

- **2026-09-13** — Ali Abbasian Ardakani, Afshin Mohammadi, Taha Yusuf Kuzan et al. — [From Density to Biopsy Decisions and Malignancy Prediction: A Benchmark Study of Multimodal Large Language Models Against Radiologists in Digital and Contrast-Enhanced Mammography](http://arxiv.org/abs/2609.14676v1)
  <details><summary>📄 Abstract</summary>
  Purpose: To compare four multimodal large language models (MLLMs) with radiologists of varying expertise in breast density assessment, BI-RADS assessment, biopsy candidacy determination, and continuous malignancy probability estimation using digital mammography (DM) and contrast-enhanced mammography (CEM). Methods: This study included 179 women with paired DM/CEM examinations and reference standards. Four MLLMs (ChatGPT-5.2, Gemini-3.1 Pro, Sonnet-4.6, Muse Spark) interpreted images with and wit...
  </details>

- **2026-09-13** — Christian Rembe — [Self-Gravitation of Mode Quanta in a Causal Resonator: One-Loop Finiteness in Linearized Quantum Gravity and the Emergence of the Dark-Energy Scale](http://arxiv.org/abs/2609.14650v1)
  <details><summary>📄 Abstract</summary>
  Perturbative quantum gravity is ultraviolet divergent and, as shown by 't Hooft and Veltman, non-renormalizable. A recent object-relative, Lorentz-invariant weighting of internal electromagnetic modes renders selected one-loop contributions of quantum electrodynamics finite without counterterms. Here that weighting is derived rather than postulated: causality defines a mode resonator bounded by the Hubble radius and re-defined in every inertial frame, and the self-gravitation of each mode quantu...
  </details>

- **2026-09-13** — Christopher Blier-Wong — [Towards foundation models for insurance risk modelling](http://arxiv.org/abs/2609.14576v1)
  <details><summary>📄 Abstract</summary>
  Claim narratives, images and sensor data contain information about insured risks that is difficult to use through existing actuarial models. Foundation models learn patterns from large datasets before being adapted to particular tasks. By turning these high-dimensional sources into variables or numerical representations, they could help insurers use more of the information they already collect, potentially reducing the experience needed to develop each application. For example, a language model ...
  </details>

- **2026-09-13** — Sushan Adhikari — [AlgoRAG: Retrieval-Augmented Generation for Theoretical Computer Science Education -- A Comprehensive Evaluation Framework for Algorithm Analysis and Complexity Theory](http://arxiv.org/abs/2609.14572v1)
  <details><summary>📄 Abstract</summary>
  Teaching abstract theoretical computer science (TCS) concepts such as algorithm analysis and complexity theory is challenging because students must handle formal proofs and asymptotic reasoning that conventional resources rarely explain in an adaptive, on-demand way. We present AlgoRAG, a specialized Retrieval-Augmented Generation (RAG) system that couples a large language model (LLM) with a curated, domain-specific knowledge base to address these challenges. The knowledge base integrates author...
  </details>

- **2026-09-13** — Ziyu Zhang, Mingchen Shao, Wenjie Tian et al. — [Bridging the Modality Gap in Long-Form Clinical Audio: A Comparative Study of Lightweight and Heavyweight End-to-End SOAP Generation](http://arxiv.org/abs/2609.14467v1)
  <details><summary>📄 Abstract</summary>
  Automating clinical documentation from long-form doctor-patient conversations remains challenging for modern audio-language models. While cascaded ASR systems perform well, end-to-end (E2E) models often struggle with information loss and hallucinations on extended audio. For the BeTraC 2026 challenge, the ASLP team presents a fully E2E multimodal system that generates structured SOAP notes directly from audio, bypassing intermediate transcripts. We constructed a 1.41-million-sample multi-task co...
  </details>

- **2026-09-13** — Pallaviram Sure, Chandra Mohan Bhuma — [Vision Language Models for Radiation Patterns to Antenna Parameters](http://arxiv.org/abs/2609.14447v1)
  <details><summary>📄 Abstract</summary>
  Observed radiation patterns often serve as a primary evidence of antenna's behavior, but translating them into meaningful interpretations is a nontrivial and expertise intensive task. This demand necessitates automated pattern interpretation, a diagnosis problem encountered in applications encompassing Radio Frequency (RF) surveillance, non cooperative emitter characterization and Over The Air (OTA) testing. This work addresses the incorporation of Contrastive Language Image Pre training (CLIP) ...
  </details>

- **2026-09-13** — Shengyun Shi, Li Tian, Bo Li — [Dynamical Anisotropy of a Colloidal Glass Under Pressure](http://arxiv.org/abs/2609.14415v1)
  <details><summary>📄 Abstract</summary>
  Pressure is a critical thermodynamic parameter that profoundly influences the physical properties of glasses. Pressure-induced densification and structural transformation endow glasses manufactured under such conditions with exceptional mechanical and optical properties. Although pressure-treated glasses have been characterized by ensemble-averaged methods such as X-ray diffraction and Raman spectroscopy, their microscopic dynamics have rarely been addressed, limiting our understanding of the co...
  </details>

- **2026-09-13** — Praveen Kumar, K. R. Guruprasad, Tushar Sandhan — [Multi-Task Visual Perception Network with LLM Conditioning for Autonomous Navigation](http://arxiv.org/abs/2609.14297v1)
  <details><summary>📄 Abstract</summary>
  Long-term navigation for service robots faces crit- ical challenges like the accumulation of odometry drift and sensor error, which progressively degrade 2D maps and renders traditional path planning algorithms (e.g., A*, RRT*, DiPPer, ViT-A*) ineffective over time. To address this, we propose a user-friendly, interactive framework that eliminates the reliance on globally consistent maps. Our approach integrates visual perception with Large Language Models (LLM) to interpret user commands via te...
  </details>

- **2026-09-13** — Jie Feng, Xiaoyang Wang, Xin Chen et al. — [Recursive Self-Improvement LLM Agents for Inverter Dynamic Model Identification](http://arxiv.org/abs/2609.14260v1)
  <details><summary>📄 Abstract</summary>
  This is a position paper. We demonstrate that recursive self-improvement (RSI) large language model (LLM) agents are a natural search engine for dynamic model identification of inverter-based resources (IBRs) whose internal controls are often proprietary and hidden from grid operators. White-box models provide physical transparency but require vendor disclosure; black-box models avoid this requirement but sacrifice interpretability; and existing grey-box approaches, including sparse and symbolic...
  </details>

- **2026-09-12** — Carmel Kronfeld, Sharva Gogawale, Tetsuro Kobayashi et al. — [A Multi-Stage Agentic Framework for Effective Counter-Narrative Generation and Refinement](http://arxiv.org/abs/2609.14178v1)
  <details><summary>📄 Abstract</summary>
  The rapid diffusion of hate speech and misinformation on social networks challenges democratic societies, since direct suppression efforts may deepen polarization, fuel public distrusts, and strengthen extremist narratives. LLM-driven counter-narratives (CNs) offer a promising way to reduce those risks, yet their effectiveness depends on rhetorical and stylistic choices that remain poorly understood. We present a multi-stage agent-based framework for generating, refining, and evaluating CNs, app...
  </details>

- **2026-09-12** — Tianyu Liu, Fan Zhang, Jiayuan Chen et al. — [RAGCell: Retrieval-Augmented Generation as Supervision for Versatile Single-cell Analysis](http://arxiv.org/abs/2609.14147v1)
  <details><summary>📄 Abstract</summary>
  Single-cell foundation models (scFMs) are transforming computational biology by enabling generalizable, task-agnostic representations for versatile single-cell analysis. Despite their progress in facilitating rapid deployment for downstream tasks, off-the-shelf scFMs still have some overlooked concerns: (I) (Pretraining Cost.) Pretrain-based scFMs necessitate pretraining on a vast volume of cells, rendering it draining resources in applications. (II) (Heterogeneous Gap.) Large Language Models (L...
  </details>

- **2026-09-12** — Bojro Das — [Inherited Heads: Audio language models track speakers with their text backbone's attention, and an attention-mass ranking retrieves a different set](http://arxiv.org/abs/2609.14174v1)
  <details><summary>📄 Abstract</summary>
  Asked to describe what one of six speakers in a recording talks about, audio language models describe the right one on 6 to 16% of trials, below the 16.7% a guess would give. Adding a fixed bias to the attention logits of a hundred heads, under a tenth of the model's and with no training, redirects the description to whichever speaker we choose, on 90.7% to 99.0% of trials. Those heads are largely not specific to audio. Rank the text-only language model an audio model was built from, or a releas...
  </details>

- **2026-09-12** — Saanvi Paturi, Arsen Kenzhebayev, Arham Sethi et al. — [When Tools Get in the Way: The Effect of Unnecessary Tool Availability on LLM Answering](http://arxiv.org/abs/2609.14157v1)
  <details><summary>📄 Abstract</summary>
  Large language models (LLMs) are increasingly deployed with external tools that extend what they can do beyond their own knowledge. Tools help on tasks that need external information, but their availability may also change how a model handles questions that do not need them. Prior work has mostly asked whether models select and use tools appropriately; whether an unnecessary tool changes the correctness of answers has received less attention. We ask whether making a related but unnecessary tool ...
  </details>

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


## 📊 统计 / Statistics

| 分类 / Category | 论文数 / Count |
|------|--------|
| jailbreak | 628 |
| prompt-injection | 538 |
| memory-poisoning | 49 |
| tool-use-attack | 134 |
| backdoor | 455 |
| adversarial-attack | 592 |
| privacy-leakage | 4083 |
| steganography | 64 |
| misuse | 1009 |
| red-teaming | 123 |
| vulnerability | 3061 |
| defense | 2872 |
| alignment | 2672 |
| robustness | 2786 |
| watermark | 425 |
| unlearning | 95 |
| agent-safety | 54 |
| benchmark | 65 |
| survey | 342 |
| other | 7588 |

---

📚 **全部 27635 篇论文**（2022 至今）请访问 [GitHub Pages](https://ny1024.github.io/AgentSafety-Papers/) 查看完整列表、搜索与筛选。

*Generated by AgentGuard at 2026-09-15 20:47:26*