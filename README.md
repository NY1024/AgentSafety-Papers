<div align="center">

# AgentGuard 🛡️

**Daily Tracking of LLM Agent Security Papers on arXiv**

[![Auto Update](https://github.com/NY1024/AgentSafety-Papers/actions/workflows/daily-update.yml/badge.svg)](https://github.com/NY1024/AgentSafety-Papers/actions/workflows/daily-update.yml)
[![Papers](https://img.shields.io/badge/Papers-20992-blue)](#)
[![License](https://img.shields.io/badge/License-MIT-green)](#)

</div>

---

## 📖 简介 / Introduction

自动追踪 arXiv 上大模型 Agent 安全方向的最新论文，每日更新，关键词智能分类。

*Automatically tracking the latest LLM Agent security papers on arXiv, updated daily with keyword-based classification.*

**最近更新 / Last Updated**: 2026-07-18 02:38 ｜ **论文总数 / Total Papers**: 20992（近 30 天 / Recent 30 days: 3671）

🌐 **[GitHub Pages](https://ny1024.github.io/AgentSafety-Papers/)** — 查看全部 20992 篇论文（含摘要、分类筛选、搜索）/ View all 20992 papers with abstracts, filters & search

## 📑 分类导航 / Category Navigation

- **[jailbreak](#-jailbreak)** — 越狱攻击 / Jailbreak Attacks — 545
- **[prompt-injection](#-prompt-injection)** — 提示注入攻击 / Prompt Injection Attacks — 458
- **[memory-poisoning](#-memory-poisoning)** — 记忆投毒与篡改 / Memory Poisoning & Tampering — 36
- **[tool-use-attack](#-tool-use-attack)** — 工具使用攻击 / Tool-Use Attacks — 91
- **[backdoor](#-backdoor)** — 后门与投毒攻击 / Backdoor & Poisoning Attacks — 386
- **[adversarial-attack](#-adversarial-attack)** — 对抗攻击 / Adversarial Attacks — 531
- **[privacy-leakage](#-privacy-leakage)** — 隐私泄露 / Privacy Leakage — 3691
- **[steganography](#-steganography)** — 隐写与隐蔽通信 / Steganography & Covert Communication — 52
- **[misuse](#-misuse)** — 滥用与误用 / Misuse & Abuse — 815
- **[red-teaming](#-red-teaming)** — 红队测试 / Red Teaming — 108
- **[vulnerability](#-vulnerability)** — 漏洞与攻击面 / Vulnerabilities & Attack Surfaces — 2449
- **[defense](#-defense)** — 防御与防护方法 / Defense & Protection Methods — 2074
- **[alignment](#-alignment)** — 对齐与安全约束 / Alignment & Safety Constraints — 1907
- **[robustness](#-robustness)** — 鲁棒性与可靠性 / Robustness & Reliability — 1786
- **[watermark](#-watermark)** — 水印与溯源 / Watermarking & Provenance — 181
- **[unlearning](#-unlearning)** — 机器遗忘 / Machine Unlearning — 82
- **[agent-safety](#-agent-safety)** — Agent 安全框架 / Agent Safety Frameworks — 48
- **[benchmark](#-benchmark)** — 安全评测与基准 / Safety Benchmarks & Evaluation — 54
- **[survey](#-survey)** — 综述与系统化 / Surveys & Systematization — 245
- **[other](#-other)** — 其他安全相关 / Other Security-Related — 5453

## 📄 近期论文 / Recent Papers (Last 30 Days)

> 仅展示最近 30 天中最新的 500 篇论文（含日期、作者、摘要）。近 30 天共 3671 篇，完整 20992 篇论文列表请访问 [GitHub Pages](https://ny1024.github.io/AgentSafety-Papers/)

> Showing the latest 500 of 3671 papers from the last 30 days (with date, authors & abstract). For the full list of 20992 papers, visit [GitHub Pages](https://ny1024.github.io/AgentSafety-Papers/)

### 📂 jailbreak
*越狱攻击 / Jailbreak Attacks* — 3 papers

- **2026-07-14** — Roman Prosvirnin, Victor Minchenkov, Alexey Soldatov et al. — [Silent Alarm: A J-Space Protocol for Comparing Danger Recognition Across Models and Quantization Levels](http://arxiv.org/abs/2607.12792v1)
  <details><summary>📄 Abstract</summary>
  Jailbreak-robustness research typically evaluates safety through generated responses using an LLM-as-judge approach. Such evaluations, however, are sensitive to the benchmark's grading procedure and capture only observed behavior on a given set of attacks, without directly revealing the hidden fragility of the underlying safety mechanisms. This work proposes JADR (Jacobian Assessment of Danger Recognition), a protocol that measures a model's internal representation through Jacobian space (J-spac...
  </details>

- **2026-07-13** — Ren-Yi Huang, Mingchen Li, Dumindu Samaraweera et al. — [Securing LLMs in the Wild: Privacy and Security Challenges at the Edge](http://arxiv.org/abs/2607.13088v1)
  <details><summary>📄 Abstract</summary>
  Large Language Models (LLMs) are rapidly moving from research settings into the wild, deployed on enterprise infrastructure, personal devices, and edge platforms. While cloud deployments offer scalable compute, concerns over data sovereignty, compliance, latency, and third-party dependence are driving organizations toward edge and on-premise LLMs. This shift introduces new security and privacy challenges: limited compute and memory force aggressive optimizations, including quantization, pruning,...
  </details>

- **2026-07-13** — Junyoung Park, Namgyu Park, Sechan Lee et al. — [MJ: Multi-turn LLM Jailbreaking via Decomposed Credit Assignment](http://arxiv.org/abs/2607.11070v1)
  <details><summary>📄 Abstract</summary>
  Modern large language models (LLMs) operate in interactive multi-turn settings, making multi-turn jailbreaking a realistic threat model and an important setting for automated red teaming. A core challenge in learning multi-turn jailbreak attackers is credit assignment: different turns contribute differently to the final outcome, yet existing learning signals are often too coarse to identify their individual contributions. We propose decomposed credit GRPO (DC-GRPO), a unified turn-level credit a...
  </details>


### 📂 prompt-injection
*提示注入攻击 / Prompt Injection Attacks* — 7 papers

- **2026-07-15** — Mohammad Allahbakhsh, Mohammad Hassan Bahari, Moslem Attar-Raouf — [Rethinking Penetration Testing for AI-Enabled Systems: From Resource Compromise to Behavioral Objective Violation](http://arxiv.org/abs/2607.14006v1)
  <details><summary>📄 Abstract</summary>
  Penetration testing traditionally evaluates whether adversaries can exploit weaknesses in software, infrastructure, configurations, or operational controls to achieve security-relevant compromise. This paradigm remains necessary for AI-enabled systems, but it is no longer sufficient. In such systems, adversaries may influence prompts, retrieved content, sensor inputs, training data, memory, tools, or human-AI interaction loops to alter system behavior without directly compromising the underlying...
  </details>

- **2026-07-15** — Sanket Badhe, Priyanka Tiwari — [Agent Skill Security: Threat Models, Attacks, Defenses, and Evaluation](http://arxiv.org/abs/2607.13987v1)
  <details><summary>📄 Abstract</summary>
  Reusable skills are becoming a fundamental building block of Large Language Model (LLM) agents, enabling capabilities to be packaged, shared, and reused across diverse applications. However, existing security research primarily focuses on prompt injection and runtime execution, leaving security risks throughout the broader skill lifecycle largely unexplored. In this paper, we present SkillSec-Eval, a lifecycle-aware framework for systematically evaluating the security of reusable agent skills. W...
  </details>

- **2026-07-15** — Alexandra E. Michael, Franziska Roesner — [How Agents Ask for Permission: User Permissions for AI Agents, from Interfaces to Enforcement](http://arxiv.org/abs/2607.13718v1)
  <details><summary>📄 Abstract</summary>
  As AI agents gain prevalance, users are increasingly exposed to the risks such systems entail. Prompt injection attacks, as well as hallucination, can cause agents to leak private information to third parties. As autonomous systems, agents also present the more active danger of performing sensitive tasks, such as bank transactions, without the user's intent or authorization.   Recognizing this challenge, the agentic security community has developed numerous proposals for secure agentic systems. ...
  </details>

- **2026-07-14** — Junhui Wang, Hangtao Zhang, Zhirun Zheng et al. — [PVDetector: Detecting Prompt Injection Attacks on Purpose-Specific LLM Agents through Policy-Violation Concept Analysis](http://arxiv.org/abs/2607.12624v1)
  <details><summary>📄 Abstract</summary>
  Large language models (LLMs) are increasingly deployed as purpose-specific agents to handle domain-specific tasks such as customer service and code generation. These agents are expected to comply with not only generic safety guardrails but also purpose-specific restrictions tailored to their designated roles. Such additional restrictions enlarge the attack surface, particularly to prompt injection (PI) attacks. To defend against such attacks, existing detection methods primarily rely on analyzin...
  </details>

- **2026-07-14** — Huihao Jing, Wenbin Hu, Shaojin Chen et al. — [Isolation as a First-Class Principle for LLM-Agent System Safety: Concepts, Taxonomy, Challenges and Future Directions](http://arxiv.org/abs/2607.12406v1)
  <details><summary>📄 Abstract</summary>
  The capability of LLM agents to function as the ``brain'' of a system fundamentally expands the scope of analysis beyond a standalone model. Consequently, safety is no longer only about input--output content alignment. It also concerns system behavior and real-world execution outcomes. However, the current literature is fragmented across attack types, applications, and benchmarks. This makes it hard to explain why failures such as prompt injection, tool misuse, and memory poisoning often share t...
  </details>

- **2026-07-13** —  SingGuard Team — [SingGuard-NSFA: Extensible Guardrails for Agentic AI via Generative Reasoning and Real-Time Classification](http://arxiv.org/abs/2607.13081v1)
  <details><summary>📄 Abstract</summary>
  We present nsfaguard, a guardrail framework for securing agentic AI systems against operational threats, such as prompt injection, sensitive information extraction, malicious code requests, dangerous tool misuse, and resource exhaustion. We first introduce the NSFA taxonomy, which organizes 185 risk variants into a CIA-triad-grounded hierarchy and is cross-validated against three well-established OWASP guidelines. Based on this taxonomy, we construct a benchmark suite spanning 133 languages, com...
  </details>

- **2026-07-12** — Bálint Gyevnár, Atoosa Kasirzadeh, Nihar B. Shah — [Distributed Denial of Science: How Indirect Data Poisoning of AI Systems Can Industrialize Scientific Fraud](http://arxiv.org/abs/2607.10712v1)
  <details><summary>📄 Abstract</summary>
  Scientific fraud is the instrument of doubt that malicious entities can use to establish controversy in science. Historically, it required the resources of a company: deep pockets, ghostwritten articles, and corrupt academics. Today, Artificial Intelligence (AI) is increasingly automating scientific research, so we ask: Can a remote adversary weaponize the honest use of AI in science to compromise scientific integrity? We envision and empirically evaluate a new attack, indirect data poisoning, i...
  </details>


### 📂 backdoor
*后门与投毒攻击 / Backdoor & Poisoning Attacks* — 2 papers

- **2026-07-13** — Junrui Zhang, Zemin Chen, Lusi Li et al. — [Input-Aware Dynamic Backdoor Attack Against Quantum Neural Networks](http://arxiv.org/abs/2607.11843v1)
  <details><summary>📄 Abstract</summary>
  Quantum Neural Networks (QNNs) are a promising framework for quantum machine learning on near-term quantum devices, but their security risks remain insufficiently understood. Studies have shown that QNNs are vulnerable to backdoor attacks, yet existing quantum backdoors mostly rely on a fixed trigger shared by all poisoned inputs. This fixed-trigger design is a major weakness because many defenses detect or weaken the repeated patterns such triggers leave in data representations. Although input-...
  </details>

- **2026-07-13** — Yibo Hu, Ren Wang — [When Local Monitors Miss Compositional Harm: Diagnosing Distributed Backdoors in Multi-Agent Systems](http://arxiv.org/abs/2607.11751v1)
  <details><summary>📄 Abstract</summary>
  As multi-agent, tool-using LLM systems are deployed, a common safety net is a runtime monitor that checks each message, tool call, or step on its own. We show this net has a fundamental hole. A distributed backdoor splits a harmful payload across agents, so every local check passes while the assembled object is the attack. The monitor can be right on every step and still miss the attack. The problem is not splitting itself: split fragments can still leak suspicious tokens or provenance edges. Th...
  </details>


### 📂 adversarial-attack
*对抗攻击 / Adversarial Attacks* — 5 papers

- **2026-07-15** — Michal Štefánik, Philipp Mondorf, Andreas Waldis et al. — [AIMO Interpretability Challenge](http://arxiv.org/abs/2607.13899v1)
  <details><summary>📄 Abstract</summary>
  We propose the AIMO Interpretability Challenge, a competition on distinguishing robust from spurious reasoning in frontier mathematical language models based on the models' internal mechanisms. The challenge is motivated by a central limitation of standard reasoning benchmarks: strong final-answer accuracy does not reveal whether a model relies on stable reasoning mechanisms or exploits brittle reasoning shortcuts. Building on AI Mathematical Olympiad (AIMO) problems and submissions, together wi...
  </details>

- **2026-07-14** — Yuxin Huang, Ziming Hong, Mingming Gong et al. — [Delving into the Temporal Challenges of Unified Video Protection Against Image-to-Video and Fine-Tuning-based Customization](http://arxiv.org/abs/2607.13336v1)
  <details><summary>📄 Abstract</summary>
  Recent diffusion-based video generation models have enabled high-quality personalized video customization through both tuning-based pipelines, which fine-tune a video diffusion model, and reference-based pipelines such as image-to-video generation. However, these capabilities raise serious concerns about personal privacy, identity ownership and intellectual property protection. Existing anti-customization works focus on protecting images, while protection for videos against both reference- and t...
  </details>

- **2026-07-13** — Congren Dai, Danni Zhao, Enyang Liu et al. — [Verifier-Guided Twelve-Tone Composition: A Generate-Verify-Repair Harness for Symbolic Music Generation](http://arxiv.org/abs/2607.11334v2)
  <details><summary>📄 Abstract</summary>
  Large language models can produce superficially legal twelve-tone scores that collapse into degenerate textures. We introduce a neuro-symbolic harness that wraps a language-model proposer in a generate-verify-repair-trace loop with symbolic verification. The complete pipeline improves event-local consistency without claiming whole-piece legality. Across 40 controlled tasks and four paired models, constraint-checked delivery rises from 13.3% under raw generation to 48.1% with the harness; it abst...
  </details>

- **2026-07-13** — Congren Dai, Danni Zhao, Enyang Liu et al. — [Verifier-Guided Twelve-Tone Composition: A Generate-Verify-Repair Harness for Symbolic Music Generation](http://arxiv.org/abs/2607.11334v1)
  <details><summary>📄 Abstract</summary>
  Large language models can produce superficially legal twelve-tone scores that collapse into degenerate textures. We introduce a neuro-symbolic harness that wraps a language-model proposer in a generate-verify-repair-trace loop with symbolic verification. The complete pipeline improves event-local consistency without claiming whole-piece legality. Across 40 controlled tasks and four paired models, audited delivery yield rises from 13.3% under raw generation to 48.1% with the harness, which explic...
  </details>

- **2026-07-13** — Chenyang Li, Kaige Li, Zeyu Jiang et al. — [AdvNav: Behavior-Guided Black-Box Adversarial Attacks on Vision-Language Navigation](http://arxiv.org/abs/2607.11063v1)
  <details><summary>📄 Abstract</summary>
  Despite progress in Embodied AI, Vision-and-Language Navigation systems remain vulnerable to adversarial visual disturbances. Most existing methods rely on white-box access to target model gradients, which is often unrealistic for real-world deployed systems and computationally exhaustive due to recursive backpropagation for optimization, limiting their applicability. While previous black-box methods predominantly target single-step, instantaneous decision tasks, they struggle to handle the task...
  </details>


### 📂 privacy-leakage
*隐私泄露 / Privacy Leakage* — 26 papers

- **2026-07-15** — Haoran Li, Jiebi Deng, Tong Jin et al. — [A Self-Evolving Agent for Longitudinal Personal Health Management](http://arxiv.org/abs/2607.13940v1)
  <details><summary>📄 Abstract</summary>
  Personal health management unfolds over repeated encounters, yet most health AI systems treat each request in isolation. We developed HealthClaw, an open-source agent architecture that updates support as a person's routines, preferences, measurements and risks change. It separates shared safety rules and medical knowledge from private longitudinal memory containing profile facts, reusable procedures and episodic traces. After each episode, induction determines what should update the profile, rev...
  </details>

- **2026-07-15** — Shengchao Chen, Ting Shu — [FM$^2$: Unified Federated Foundation Models for Heterogeneous Multimodal Medical Imaging](http://arxiv.org/abs/2607.13386v1)
  <details><summary>📄 Abstract</summary>
  Building foundation models for medical imaging requires pooling data across institutions, yet privacy regulations prohibit centralized aggregation. Existing Federated Foundation Models either fine-tune natural-image models with poor medical-domain transfer, or train from scratch within a single modality, lacking the flexibility to unify tasks. We identify an under-explored challenge, Imaging Modality Heterogeneity, where clients operate under two structural regimes: Overlapped (shared modalities...
  </details>

- **2026-07-15** — Ilef Chebil, Asma El Hadj, Souheib Yousfi et al. — [PriEval-Protect: A Unified Framework for Privacy Evaluation and Protection in Healthcare Systems](http://arxiv.org/abs/2607.13754v1)
  <details><summary>📄 Abstract</summary>
  Safeguarding patient privacy while enabling meaningful healthcare data use remains critical under GDPR and HIPAA. Existing compliance methods are manual, error-prone, and separate policy audits from data-level assessments. This paper presents PriEval-Protect, a two-phase framework for unified privacy risk evaluation and mitigation. The evaluation phase combines regulatory compliance scoring using a fine-tuned legal LLM with RAG, and technical analysis via encryption type, data architecture, and ...
  </details>

- **2026-07-15** — Michael O. Eniolade — [Evaluating Frontier AI Agents as Autonomous Clinical Security Auditors](http://arxiv.org/abs/2607.13411v1)
  <details><summary>📄 Abstract</summary>
  Clinical AI models can expose patients to harm when adversarial vulnerabilities go undetected, yet formal security auditing requires statistical expertise, specialized tools, and significant time. We present an open evaluation task, built on METR Task Standard v0.3.0, that tests whether frontier AI agents can autonomously implement a structured clinical AI security audit. Given a pre-trained clinical prediction model, a patient dataset, and written instructions, each agent must implement four at...
  </details>

- **2026-07-14** — Stephan A. Fahrenkrog-Petersen, Aleksander Figiel, Darya Melnyk et al. — [Privacy Attacks on Stable Marriage](http://arxiv.org/abs/2607.13015v1)
  <details><summary>📄 Abstract</summary>
  The stable marriage problem appears in many privacy-sensitive domains, for example in the National Resident Matching Program in the US. In such applications, preserving the privacy of users' preference lists is essential to prevent strategic manipulation, discourage misreporting, and comply with data protection regulations.   In this work, we investigate privacy attacks on stable marriage algorithms. Assuming that the attacker (e.g., the hospitals) can repeatedly interact with the stable marriag...
  </details>

- **2026-07-14** — Qingcheng Zeng, Puxuan Yu, Aman Mehta et al. — [Finding the Right Tables and Columns: A Benchmark and Corpus-Adaptive Embeddings for SQL Schema Retrieval](http://arxiv.org/abs/2607.13311v1)
  <details><summary>📄 Abstract</summary>
  Retrieval in the SQL setting has largely been studied as the task of finding, within a large collection of SQL statements, the statement that answers a natural-language question. At scale, however, a more fundamental retrieval problem precedes generation: schema retrieval, identifying the tables and columns a question requires in a database that may contain thousands of them, far more than fit in a model's context. We argue that this step warrants first-class evaluation. To this end, we recast f...
  </details>

- **2026-07-14** — Shuai Cui, Chen Wenxuan, Wenjie Du et al. — [AdaPCLA: Adaptive Prior-Calibrated Logit Adjustment for Long-Tailed Longitudinal EHR Generation](http://arxiv.org/abs/2607.12645v1)
  <details><summary>📄 Abstract</summary>
  Generative modeling of longitudinal Electronic Health Records is increasingly important for privacy-preserving research, yet standard autoregressive models tend to underrepresent the co-occurrence structure of tail events (i.e., diseases, symptoms), reducing the fidelity and faithfulness of generated data for rare subpopulations. To this end, we propose AdaPCLA framework, which enables generative models to adaptively fit and generate EHR data through a data distribution-aware training strategy; ...
  </details>

- **2026-07-14** — Qianpiao Ma, Xiaozhu Song, Junlong Zhou et al. — [Scaling Synthetic-Image Pre-Training for Federated Fine-Tuning of Large Vision Models](http://arxiv.org/abs/2607.12583v1)
  <details><summary>📄 Abstract</summary>
  Federated fine-tuning (FedFT) enables adapting pre-trained large vision models (LVMs) on distributed, privacy-sensitive devices, while its practical deployment is hindered by three critical challenges: resource constraints, system heterogeneity, and non-IID data. While prior studies partially address these issues, e.g., by pre-training initial models on synthetic images to mitigate the adverse effects of non-IID data, or leveraging parameter-efficient fine-tuning (PEFT) methods like low-rank ada...
  </details>

- **2026-07-14** — Yi Li, Chen Li, Jiexiong Liu — [Efficient and Privacy Aware Edge Cloud Collaborative Inference for Large Language Models](http://arxiv.org/abs/2607.13093v1)
  <details><summary>📄 Abstract</summary>
  On-device LLM inference faces a trilemma of response latency, limited hardware resources and user privacy. Full cloud inference delivers strong computing power but exposes user prompts and dialogue data, while standalone on-device inference is unfeasible for most consumer and embedded edge devices. This paper presents a privacy-centric edge-cloud collaborative LLM inference framework built on endpoint-authenticated KV cache. Local endpoints handle input preprocessing, embedding computation, adap...
  </details>

- **2026-07-14** — Ranjeet K Jha, Venkata Suresh Gummadilli — [Privacy Preserving Recommender Systems Balancing Personalization with Privacy](http://arxiv.org/abs/2607.13328v1)
  <details><summary>📄 Abstract</summary>
  Personalized recommendation systems are central to modern e-commerce and retail platforms, but they typically rely on centralized storage of detailed user interaction data, creating significant privacy and regulatory challenges. With increasing requirements from regulations such as GDPR, CCPA, and CPRA, organizations must develop recommendation systems that preserve user privacy without substantially degrading recommendation quality.   This work presents and evaluates a privacy-preserving recomm...
  </details>

- **2026-07-14** — Bruce Coburn, Jingbo Yue, Jinge Ma et al. — [Open-KNEAD: Knowledge-grounded Nutrition Estimation via Agentic Decomposition](http://arxiv.org/abs/2607.12911v1)
  <details><summary>📄 Abstract</summary>
  Multimodal Large Language Models (MLLMs) are increasingly used for dietary assessment from meal images, where retrieval-augmented grounding was shown to sharpen nutrition estimates. However, we find this premise no longer holds for current MLLMs. A modern MLLM's direct estimate now matches or surpasses the full retrieval pipeline. This raises a question: if retrieval no longer improves the overall estimate, can it still deliver the two things clinicians value, accurate portions and a traceable, ...
  </details>

- **2026-07-14** — Sai Sandeep Damera, John S. Baras — [Stability Buys Time: A Re-Keying Game for Encrypted Multi-Agent Control](http://arxiv.org/abs/2607.12742v1)
  <details><summary>📄 Abstract</summary>
  Encrypted control lets a cloud coordinate a fleet of agents on fully homomorphically encrypted state, keeping their positions and commands private. The approximate scheme for real-valued control, CKKS, returns decryptions that carry the encryption noise, a key-recovery leak; the loop must decrypt to actuate, so the leak is unavoidable. Yet the security of approximate FHE is studied statically, encrypted control assumes an honest-but-curious cloud, and persistent-threat games never reach inside t...
  </details>

- **2026-07-14** — Wenhao Zhang, Zhongliang Zhou, John Kang et al. — [Auditing Data Leakage in Whole-Slide Image Multimodal Benchmarks](http://arxiv.org/abs/2607.12278v1)
  <details><summary>📄 Abstract</summary>
  Recent vision-language models (VLMs) for computational pathology report striking zero-shot performance on whole-slide image (WSI) visual question answering (VQA) benchmarks. We audit these claims and find them fundamentally compromised by data leakage at two hierarchical levels: patient-level leakage, where slides from the same case appear in both training and test folds, and institutional-level leakage, where different cases nonetheless share staining-batch and scanner signatures through a comm...
  </details>

- **2026-07-13** — Jing Liu, Kun Yang, Yan Wang et al. — [PFAdapter: Hierarchical LoRA Decomposition for Personalized Federated MLLMs](http://arxiv.org/abs/2607.12111v1)
  <details><summary>📄 Abstract</summary>
  Agentic AI systems are reshaping communications and networking by deploying autonomous intelligent agents capable of collaborative learning while maintaining data privacy at network edges. Within distributed network environments, Multimodal Large Language Models (MLLMs) serve as cognitive engines for edge devices, yet federated fine-tuning faces substantial challenges in balancing global knowledge aggregation with local adaptation under heterogeneous network conditions. Conventional federated pr...
  </details>

- **2026-07-13** — Yuvraj Sehgal, Sneh Patel, Mahsa Panahandeh et al. — [TraceSynth: Generating Production-Quality Kernel Traces with Constraint-Guided Diffusion Models](http://arxiv.org/abs/2607.12104v1)
  <details><summary>📄 Abstract</summary>
  Machine learning models for system diagnostics rely on kernel execution traces to capture fine-grained system behavior, but collecting production traces in industrial systems is costly due to runtime overhead, storage demands, and privacy constraints. We present TraceSynth, a diffusion-based framework for generating synthetic kernel traces that augment limited real data for downstream ML tasks. TraceSynth models traces as multi-channel sequences (event types, timestamps, CPU affinity, thread ide...
  </details>

- **2026-07-13** — Navnit Shukla — [Cost-Governed RAG: Unified Per-Tenant Cost Attribution Across Retrieval and Generation in Multi-Tenant LLM Systems](http://arxiv.org/abs/2607.12188v1)
  <details><summary>📄 Abstract</summary>
  Enterprise Retrieval-Augmented Generation (RAG) deployments face a critical governance gap: while LLM generation cost is metered per token, the retrieval layer - vector memory, similarity compute, and embedding API calls - remains an unattributed shared cost, enabling invisible cross-subsidization among tenants. We present Cost-Governed RAG, an architecture that integrates a codebook-oblivious vector index (TurboVec) with a multi-tenant LLM governance gateway, creating a unified observability st...
  </details>

- **2026-07-13** — Jing Liu, Chenxuanyin Zou, Jiayang Ren et al. — [Continual Learning with Elastic Regularization and Synthetic Replay for Federated MLLM Fine-Tuning](http://arxiv.org/abs/2607.12112v1)
  <details><summary>📄 Abstract</summary>
  Federated fine-tuning of Multimodal Large Language Models (MLLMs) across distributed networks enables privacy-sensitive adaptation to evolving data streams, yet a fundamental obstacle prevents robust deployment in dynamic environments: catastrophic forgetting, wherein sequential task updates erase previously acquired knowledge across visual, linguistic, and cross-modal representations. Addressing this challenge is especially critical for autonomous networked AI operating in safety-sensitive doma...
  </details>

- **2026-07-13** — Kartik Ghanshyambhai Pansuriya, Ehsan Ghorbani, Deepak Singh et al. — [Predicting Acceptance and Review Effort in Human and Agent Pull Requests](http://arxiv.org/abs/2607.12057v1)
  <details><summary>📄 Abstract</summary>
  Pull requests (PRs) are a central mechanism for reviewing and integrating code changes in modern software repositories. As AI coding agents begin to submit more code changes alongside human developers, maintainers face a new challenge: deciding which PRs are likely to be accepted and which ones may require substantial review effort. This paper studies whether such outcomes can be estimated at the time a PR is opened, before reviewer discussion, CI feedback, or merge decisions are available. Usin...
  </details>

- **2026-07-13** — Jijie Li, Jiankuo Zhao, Xiangyu Zhu et al. — [The Devil Is in the Leakage: A Disentangled Dual-Purification Framework for High-Fidelity Hairstyle Transfer](http://arxiv.org/abs/2607.11281v1)
  <details><summary>📄 Abstract</summary>
  Hairstyle transfer aims to synthesize a photorealistic portrait by transplanting the hairstyle from a reference image onto a source subject while preserving the source identity. Recent foundation models show strong generative capability, but they struggle with the zero-shot disentanglement required for precise local editing, often entangling the reference hairstyle with its original identity and pose. Existing diffusion-based pipelines typically decompose the task by first generating a "bald" im...
  </details>

- **2026-07-13** — Yiming Zhang, Jiangrong Wu, Yuhong Nan — [FlowArk: Boosting Agentic Data-flow Analysis for Android Apps via Context-Aware Knowledge Reuse](http://arxiv.org/abs/2607.11308v1)
  <details><summary>📄 Abstract</summary>
  Data-flow analysis is foundational to Android app privacy and security auditing. Recent coding agents can assist with non-trivial source-to-sink data-flow analysis tasks by searching, reading, and reasoning over repository code. However, when these tasks are executed as a batch workload, current agentic analysis setups incur substantial re-analysis cost. Agent instances assigned to different taint sources may inspect shared code fragments, because code reuse in the target app can cause different...
  </details>

- **2026-07-13** — Eddie Huang, Ken Liao, Iven Fu et al. — [NVAITC AI Scientist: A Governed End-to-End Research System -- A Hypertension GWAS Case Study](http://arxiv.org/abs/2607.11084v1)
  <details><summary>📄 Abstract</summary>
  Agentic research systems are emerging as a new paradigm for coordinating scientific workflows beyond isolated model inference, code generation, or statistical analysis. However, deployment in institutional biomedical environments requires governed mechanisms for research planning, data access, workflow orchestration, evidence tracking, reproducibility, and human oversight. We present NVAITC AI Scientist (NAIS), a governed end-to-end agentic research system designed to support domain-general scie...
  </details>

- **2026-07-13** — Junhao Ruan, Yuan Ge, Bei Li et al. — [ToFu: A White-Box, Token-Efficient Agent Harness for Researchers](http://arxiv.org/abs/2607.11423v1)
  <details><summary>📄 Abstract</summary>
  Agentic coding tools present new opportunities to transform research workflows. The performance of agent systems built depends on both large language models (LLMs) and the harness around LLMs, which is the orchestration code that determines an agent's behavior. We present ToFu, an agentic harness for researchers that reads your codebase, edits files, runs commands, and integrates with your development tools. ToFu plays a dual role in research. As a research assistant, it supports practical resea...
  </details>

- **2026-07-13** — Aleh Manchuliantsau — [From Checker to Forecaster: Code-Owned Evaluation of Model-Generated Strategic Routes Under Delayed Ground Truth](http://arxiv.org/abs/2607.10972v1)
  <details><summary>📄 Abstract</summary>
  Many evaluations of model outputs rely either on contracts checkable at evaluation time or on feedback that arrives within the operating loop. We study the complementary setting in which ground truth is delayed, censored, or private, so deterministic code cannot check correctness at scoring time and must instead issue a code-owned provisional forecast. RouteCast instantiates this regime for model-generated typed strategic routes: models propose candidate routes and structured factors; point-in-t...
  </details>

- **2026-07-12** — Borzoo Rassouli, Morteza Varasteh — [Differentially Private Consistent Release of Counting Queries](http://arxiv.org/abs/2607.10952v1)
  <details><summary>📄 Abstract</summary>
  We study the problem of releasing counting-query outputs through a stochastic mechanism that is both consistent and \((ε,δ)\)-differentially private. Consistency requires the released value to lie within the feasible range of the query, while utility is measured by the worst-case probability of error. We first derive a closed-form expression for the minimum achievable error probability and obtain an explicit optimal mechanism. By exploiting the active differential privacy constraints satisfied b...
  </details>

- **2026-07-12** — Elette Boyle, MohammadTaghi Hajiaghayi, Keivan Rezaei et al. — [Can Watermarking Techniques Help Prevent LLM Model Stealing?](http://arxiv.org/abs/2607.10794v1)
  <details><summary>📄 Abstract</summary>
  Model stealing attacks have recently been introduced, enabling the extraction of precise information from black-box commercial language models. In this work, we propose defense methods against a recent attack of \cite{carlini2024stealing} and extensions for extracting the hidden layer dimension of production language models. Our methods are inspired by watermarking techniques that perturb the logits layer of these models to prevent such attacks. We provide empirical experiments demonstrating the...
  </details>

- **2026-07-12** — Syed Irfan Ali Meerza, Oktay Ozturk, Amir Sadovnik et al. — [DiffUE: Enhancing Utility-Unlearnability Trade-off of Unlearnable Examples via Diffusion Autoencoders](http://arxiv.org/abs/2607.10580v1)
  <details><summary>📄 Abstract</summary>
  AI models are increasingly trained on personal images scraped from social media and public platforms, often without consent, leading to serious privacy violations, such as unauthorized facial recognition and targeted advertising. To counter this, researchers have developed unlearnable examples (UEs), images modified with imperceptible noise to prevent AI models from extracting meaningful information. However, existing UE methods primarily rely on pixel-space noise, which can be bypassed by relea...
  </details>


### 📂 misuse
*滥用与误用 / Misuse & Abuse* — 14 papers

- **2026-07-15** — Tianyu Chen, Chujia Hu, Wenjie Wang — [SAFETY SENTRY: Context-Aware Human Intervention via EXECUTE-ASK-REFUSE Routing](http://arxiv.org/abs/2607.13594v1)
  <details><summary>📄 Abstract</summary>
  LLM agents act on real-world environments through tool calls, and a single misjudged action can cause irreversible harm. The standard safeguard is a guard model that labels each proposed action as safe or unsafe, but this binary view conflates two distinct decisions: whether the action is harmful in itself, and whether it is appropriate given the user's context. It also operates at the granularity of action categories rather than individual instances, producing routine interruptions that erode a...
  </details>

- **2026-07-15** — Qiang Zhu, Jiajun Wu — [LAPO: Leave-One-Turn Attribution for Self-Generated Process Rewards in Multi-Turn Search Reasoning](http://arxiv.org/abs/2607.13501v1)
  <details><summary>📄 Abstract</summary>
  Reinforcement learning for multi-turn search reasoning typically relies on terminal outcome rewards, which cannot distinguish useful, redundant, and harmful intermediate interactions. We propose LAPO, a self-generated process-supervision method based on backward leave-one-turn attribution. For each search turn, LAPO replaces the turn and its retrieval observation with a fixed [DELETE] placeholder and measures the resulting change in the current policy's mean log-likelihood of the gold answer. Th...
  </details>

- **2026-07-14** — Paolo Magliano, Puze Liu, Jan Peters et al. — [Directional Constraints for Efficient Exploration in Safe Reinforcement Learning](http://arxiv.org/abs/2607.12784v1)
  <details><summary>📄 Abstract</summary>
  Reinforcement Learning has revolutionized the landscape of robotic research, allowing robust learning of complex robotic skills in simulation. However, real-world deployment in open-ended environments requires strong safety guarantees to prevent dangerous or harmful behaviors. Safe Reinforcement Learning methods address this requirement by enforcing safety constraints. Nevertheless, learning under constraints often reduces learning speed and could lead to suboptimal task performance, as the agen...
  </details>

- **2026-07-14** — Z Sun, Q Jiang, S Sheng et al. — [WaterMoE: Expert-Routing-based Watermarking for High Fidelity and Efficiency](http://arxiv.org/abs/2607.13099v1)
  <details><summary>📄 Abstract</summary>
  Large language models (LLMs) have achieved remarkable success but raise growing concerns about content provenance and misuse, motivating the need for reliable watermarking techniques. However, these techniques have rarely been adopted in practice mainly for two reasons: i) severely degraded model performance, and ii) additional inference overhead. To confirm the problem, we construct a comprehensive benchmark spanning different generation tasks to systematically evaluate 9 representative waterma...
  </details>

- **2026-07-13** — Rahul Gupta, Abhinav Mohanty, Payal Motwani et al. — [A Threshold Exceedance Framework for CBRN Uplift Evaluation in Frontier Language Models](http://arxiv.org/abs/2607.12200v1)
  <details><summary>📄 Abstract</summary>
  As frontier language models advance, policymakers and model developers need methods for assessing whether model access materially increases a non-expert actor's ability to plan high-consequence Chemical, Biological, Radiological, or Nuclear (CBRN) misuse relative to public tools alone. Existing CBRN evaluations differ in non-expert definitions, threat scope, baselines, scoring rubrics, and decision rules, making results difficult to compare across studies. We introduce a Threshold Exceedance Cri...
  </details>

- **2026-07-13** — Ahmed Omar Salim Adnan, Yogananda Manjunath, Shivanjali Khare — [An Explainable Agentic System for Detection of Conversational Scams with Summary-Based Memory](http://arxiv.org/abs/2607.11707v2)
  <details><summary>📄 Abstract</summary>
  Following the rapid progress of generative Artificial Intelligence, there is a growing threat posed by conversational scams. These scams often span over multiple weeks or months, gradually build trust and request for money or sensitive information. Existing scam-detection systems mainly focus on isolated messages, which renders them inadequate against this evolving threat. This paper extends single-message phishing detection and presents an explainable agentic system for detecting sophisticated ...
  </details>

- **2026-07-13** — Romain Amigon — [Transformer-Guided Swarm Intelligence for Frugal Neural Architecture Search](http://arxiv.org/abs/2607.11826v1)
  <details><summary>📄 Abstract</summary>
  Neural Architecture Search (NAS) has automated the design of deep learning models but traditionally requires massive computational resources, often measured in thousands of GPU-days. In this paper, we propose a frugal and memetic NAS framework designed to democratize architecture design on consumer-grade hardware. Our approach combines the global macro-search capabilities of an autoregressive Transformer controller, trained via Reinforcement Learning (RL), with the local micro-exploitation of an...
  </details>

- **2026-07-13** — Praneeth Narisetty, Shiva Nagendra Babu Kore — [Mako: A Self-Evolving Agentic Operating System (SE-AOS) for Autonomous Web Exploitation](http://arxiv.org/abs/2607.11288v1)
  <details><summary>📄 Abstract</summary>
  We introduce the Self-Evolving Agentic Operating System (SE-AOS): a new class of AI agent that treats exploit capability as a mutable, versioned kernel it extends at runtime, observing its own failures, synthesising new capabilities, proving them against a live target, and hot-loading them back into itself. Mako is the first SE-AOS instance for security research and the autonomous web exploitation engine developed within LaunchSafe. LaunchSafe builds autonomous security agents for continuous off...
  </details>

- **2026-07-13** — Ahmed Omar Salim Adnan, Yogananda Manjunath, Shivanjali Khare — [An Explainable Agentic System for Detection of Conversational Scams with Summary-Based Memory](http://arxiv.org/abs/2607.11707v1)
  <details><summary>📄 Abstract</summary>
  Following the rapid progress of generative Artificial Intelligence, there is a growing threat posed by conversational scams. These scams often span over multiple weeks or months, gradually build trust and request for money or sensitive information. Existing scam-detection systems mainly focus on isolated messages, which renders them inadequate against this evolving threat. This paper extends single-message phishing detection and presents an explainable agentic system for detecting sophisticated ...
  </details>

- **2026-07-13** — Aznaur Aliev, Carlos Hinojosa, Abdelrahman Eldesokey et al. — [HyperSafe: Inference-Time Safety Recovery for Fine-Tuned Language Models](http://arxiv.org/abs/2607.11475v1)
  <details><summary>📄 Abstract</summary>
  Safety alignment in large language models can be fragile under fine-tuning, as even benign task adaptation may increase harmful compliance. Existing defenses mainly follow two directions: they either intervene during or after fine-tuning through retraining or weight modification, which can be costly and may hurt task performance, or they use model-agnostic safety classifiers, which may miss failures specific to a given fine-tuned checkpoint. These limitations motivate a post hoc, model-specific,...
  </details>

- **2026-07-13** — Joris Voerman, Nicolas Sidere, Jean-Christophe Burie — [Video Transformer for Remote Identity Document Hologram Detection](http://arxiv.org/abs/2607.11419v1)
  <details><summary>📄 Abstract</summary>
  Remote identity authentification using Identification Documents has been a major challenge for several years. DeepFakes advent and the development of AI-guided tools helps fraudsters creating counterfeit ID Documents. Ensuring the authenticity of ID Documents has become a real clue in the seurization of remote authentification. This need is all the more pressing given the increasing digitization of administrative and transactional processes. To ensure widespread accessibility, the system should ...
  </details>

- **2026-07-12** — Chinmayi Dixit — [Filtering Harmful Actions Isn't Enough: Phantom Transfer in Agentic SDF](http://arxiv.org/abs/2607.10750v1)
  <details><summary>📄 Abstract</summary>
  Synthetic data is widely used to train large language models because it is inexpensive to generate and easy to control. As models are increasingly deployed as agents, synthetic trajectories are likely to become an important source of training data for agentic behavior. We investigate the effects of training on synthetic agentic trajectories containing adversarial interactions, including actions such as terminating another agents process, lowering its scheduling priority, or accessing resources w...
  </details>

- **2026-07-12** — Piper Harris, Chad M. Topaz — [Institutional Harm through Threshold Cascades](http://arxiv.org/abs/2607.10726v1)
  <details><summary>📄 Abstract</summary>
  Can a population of people not individually inclined to harm others nonetheless produce harmful collective outcomes, purely because of the institutional structure they inhabit? Social scientists have long argued yes, but existing accounts are largely qualitative and provide no precise condition distinguishing safe institutions from unsafe ones. We develop a threshold cascade model in which agents have positive activation thresholds, harmful behavior is irreversible, and the institution exerts bo...
  </details>

- **2026-07-12** — Caihui Yan, Gang Cao, Huawei Tian et al. — [Effective Synthetic Image Detection via Noise Residual Clustering](http://arxiv.org/abs/2607.10695v1)
  <details><summary>📄 Abstract</summary>
  The rapid advancement of generative artificial intelligence (AI) has made synthetic images remarkably realistic, posing security threats such as misinformation and fraud. It is significant to detect the synthetic image in the manner of passive and blind image authentication. Most existing detectors rely on supervised training with large labeled datasets, leading to high costs and degraded performance on unknown generative models. To attenuate such deficiencies, we propose a training-free detecti...
  </details>


### 📂 red-teaming
*红队测试 / Red Teaming* — 3 papers

- **2026-07-14** — Yakov Pyotr Shkolnikov — [Composable Trust for Language Models: A proven boundary and a measured defense](http://arxiv.org/abs/2607.13149v1)
  <details><summary>📄 Abstract</summary>
  In a language model, instructions and data share one token stream, so nothing inside the model's generation can keep untrusted text from steering it. We develop a trust model that places the authority to act outside the model, in code: a source's standing, not its content, decides which operation runs and whether it acts. A lower-trust source may inform an answer but not override a higher one. An unmodified model runs inside a deterministic pipeline that ranks inputs by source integrity, and a f...
  </details>

- **2026-07-13** — Xutao Mao, Xiang Zheng, Cong Wang — [Agent Hacks Agent: Autoresearch for Production-Agent Red-Teaming](http://arxiv.org/abs/2607.11698v1)
  <details><summary>📄 Abstract</summary>
  Production LLM agents such as Claude Code and Codex operate over untrusted content, files, commands, and workspace state, making safety failures directly actionable. Red-teaming must therefore keep pace with evolving models and tools. Existing approaches mainly optimize attack success and preserve artifacts such as benchmarks, payloads, or attack programs, which record where attacks succeed but not the enabling conditions behind unsafe agent behavior. We study automated red-teaming for productio...
  </details>

- **2026-07-13** — Yi Ting Shen, Kentaroh Toyoda, Alex Leung — [AMT-X: Phase-Structured Multi-Turn Red-Teaming with Checklist-Gated Evaluation](http://arxiv.org/abs/2607.11151v1)
  <details><summary>📄 Abstract</summary>
  Safety evaluation of large language models (LLMs) relies largely on single-turn attack datasets and single-judge scoring, underestimating risk from adaptive multi-turn adversaries and reporting a single success rate that does not separate partially actionable outputs from those carrying complete operational detail. We propose AMT-X (Adaptive Multi-Turn Exploitation), a phase-structured multi-turn red-teaming framework. Unlike prior multi-turn attacks that rely on ad hoc escalation or free-form p...
  </details>


### 📂 vulnerability
*漏洞与攻击面 / Vulnerabilities & Attack Surfaces* — 59 papers

- **2026-07-15** — Liam Buisson — [Recovery of coefficients for a convection-diffusion equation from partial data](http://arxiv.org/abs/2607.13778v1)
  <details><summary>📄 Abstract</summary>
  This article is devoted to the inverse problem of determining the zeroth- and first-order coefficients, depending on both the time and space variables, in a parabolic equation from partial boundary measurements of the flux generated by Dirichlet excitations. More precisely, we establish the unique determination of a time-dependent convection term and potential from the partial Dirichlet-to-Neumann map associated with the corresponding parabolic equation, where the Neumann measurements are restri...
  </details>

- **2026-07-15** — Wenxuan Miao, Haosong Liu, Weiming Hu et al. — [Kaleido: Algorithm-Hardware Co-Design for Video Diffusion Transformers by Exploiting Latent Space Correlations](http://arxiv.org/abs/2607.13770v1)
  <details><summary>📄 Abstract</summary>
  Video diffusion transformers (vDiTs) generate high quality video but introduce extremely high compute cost due to the long diffusion timesteps and self attention computation. As diffusion timesteps are reduced, the computation cost of self attention becomes the dominant bottleneck. Existing acceleration approaches largely inherit sparse attention techniques from large language models, which fail to consider the unique spatiotemporal correlation of video data.   This paper presents Kaleido, an al...
  </details>

- **2026-07-15** — Aida Abiad, Nichola Castriota — [Spectral and Additive Combinatorial Methods for Cycles and Absorbing Sets in Lifted-Product Quantum LDPC Codes](http://arxiv.org/abs/2607.13666v1)
  <details><summary>📄 Abstract</summary>
  The finite-length performance of quantum low-density parity-check (LDPC) codes under iterative decoding is governed by small substructures of the Tanner graph, principally short cycles and absorbing sets. While the classical theory of these substructures for quasi-cyclic codes is well developed through discrete Fourier transform (DFT) methods, these tools do not directly address the two-block tensor structure $H_X = [\,\widetilde{H}_1 \mid I \otimes \widetilde{B}^T\,]$ of the lifted-product (qua...
  </details>

- **2026-07-15** — Muntaser Syed, Marius C. Silaghi, Sheikh Abujar et al. — [The Environmental Cost of Digital Sovereignty: Water, Energy, and Emissions Impacts of Sovereign AI Infrastructure in the Global South](http://arxiv.org/abs/2607.13443v1)
  <details><summary>📄 Abstract</summary>
  Sovereign AI has become a strategic priority across the Global South, with over \$200 billion in state-led commitments announced between 2024 and 2026. Yet the physical infrastructure that compute sovereignty demands, above all data centers, imposes water, energy, and carbon costs that fall hardest on countries least equipped to absorb them. This paper presents a comparative environmental stress analysis across four cases: the United Arab Emirates, Bangladesh, India, and Africa (with a focus on ...
  </details>

- **2026-07-15** — Mingyang Sun, Guozhu Meng — [DREA: Decoupled Reasoning and Exploration Agents for Repository-Level Vulnerability Detection](http://arxiv.org/abs/2607.13439v1)
  <details><summary>📄 Abstract</summary>
  Large language models (LLMs) are increasingly applied to vulnerability detection due to their strong code comprehension capabilities, but most existing approaches rely on isolated functions or context extracted by fixed program-analysis rules. These methods cannot adaptively explore repository-level dependencies to gather sufficient context when vulnerabilities span multiple functions or files, compromising detection reliability. We present DREA (Decoupled Reasoning and Exploration Agents), a hy...
  </details>

- **2026-07-15** — Rui Wang, Hongru Wang, Yi Chen et al. — [Demystifying On-Policy Distillation: Roles, Pathologies, and Regulations](http://arxiv.org/abs/2607.13399v1)
  <details><summary>📄 Abstract</summary>
  On-policy distillation (OPD) has become a key paradigm in LLM post-training, yet its training dynamics remain poorly understood. We present a systematic study examining the role, pathologies, and regulations of OPD. We first clarify the role of OPD as an exploration catalyst: it steers the student toward correct reasoning paths via dense token-level guidance, without expanding capability ceiling. We confirm this by showing that prompt diversity matters more than per-problem sampling numbers, and...
  </details>

- **2026-07-15** — Xi Shi, Mengxin Zheng, Qian Lou — [Learning Latency-Aware Orchestration for Multi-Agent Systems](http://arxiv.org/abs/2607.13359v1)
  <details><summary>📄 Abstract</summary>
  Multi-agent systems (MAS) coordinate multiple LLM-powered agents through structured workflows, gaining reasoning power but incurring high inference latency from multi-step execution and repeated model invocations. Existing orchestration methods primarily optimize task performance and inference cost, leaving latency largely unaddressed. In MAS, end-to-end latency is governed by the critical execution path, so reducing total cost alone does not reliably reduce latency. Moreover, optimizing latency...
  </details>

- **2026-07-15** — Yiheng Huang, Zhijia Zhao, Bihuan Chen et al. — [ProfMalPlus: Agent-Coordinated Detection of Malicious NPM Packages via Static-Dynamic Analysis Synergy](http://arxiv.org/abs/2607.13965v1)
  <details><summary>📄 Abstract</summary>
  Open source software is vulnerable to supply-chain attacks through transitive dependencies, especially malicious code injected into NPM packages. Existing detectors often inadequately model obfuscated behavior, overlook JavaScript's object-centric features, poorly coordinate static and dynamic analysis, and lose semantic information during behavior abstraction. We propose ProfMalPlus, a malicious NPM package detector combining object-sensitive behavior graphs with coordinated LLM reasoning over ...
  </details>

- **2026-07-15** — Lynnette Hui Xian Ng, Yunze Xiao, Lionel Z. Wang et al. — [ExpressionCueLens: A Cross-Cultural Analysis of Human-AI Companion Conversations on Social Media](http://arxiv.org/abs/2607.13924v1)
  <details><summary>📄 Abstract</summary>
  LLM-based AI companion agents are increasingly being perceived not only as tools but also as social companions. On social media, people recount conversations where these agents comfort, negotiate and assert boundaries, reflecting a growing attribution of human-like qualities. To profile how agency is perceived in human-AI (HAI) interactions, we introduce the ExpressionCueLens framework, which organizes linguistic, cognitive, behavioral and perceptual cues into ten categories of anthropomorphism ...
  </details>

- **2026-07-15** — Rafael Munoz-Salinas, Francisco Jose Romero-Ramirez, Sergio Garrido-Jurado — [Recursive ArUco Markers: A Scalable Fiducial Marker Design for Unmanned Aerial Vehicle Landing Pads](http://arxiv.org/abs/2607.13830v1)
  <details><summary>📄 Abstract</summary>
  Unmanned Aerial Vehicles (UAVs) increasingly rely on visual fiducial markers for autonomous navigation and precision landing. However, standard markers suffer from limited operational ranges, becoming undetectable when the camera is either too far or too close. While recursive and fractal markers have been proposed to address this issue, existing approaches either require the marker's center to remain visible, making them vulnerable to occlusion, or are limited in their recursion depth and place...
  </details>

- **2026-07-15** — Zhenpeng Li — [Traffic-Aware Randomized Smoothing for LLM-Based Network Intrusion Detection](http://arxiv.org/abs/2607.13801v1)
  <details><summary>📄 Abstract</summary>
  Large language model (LLM)-based intrusion detection systems (IDS) are increasingly studied for security monitoring, yet their robustness against feasible traffic manipulation remains largely empirical. We present Traffic-Aware Randomized Smoothing (TA-RS), a classifier-agnostic certified defense that injects Gaussian noise exclusively into the directly controllable (DC) subspace -- features a remote attacker can modify -- during both fine-tuning and certification, aligning the smoothing distrib...
  </details>

- **2026-07-15** — Serkan Ballı — [The Test Oracle Problem in Synthetic LLM-as-Judge Corpora: Disappearance, Distortion and a Validation Protocol](http://arxiv.org/abs/2607.13707v1)
  <details><summary>📄 Abstract</summary>
  Studies of bias in LLM-as-judge systems typically build synthetic corpora by prompting an LLM to generate a hallucinated answer to pair with a factual one, then presenting both to a judge. We report a case in which this generation step silently failed, and use it to argue that the failure mode is structural rather than incidental. In a multilingual (Turkish/English) faithfulness-judgment corpus, a decoding-budget parameter shared between judging and generation calls truncated one producer's hall...
  </details>

- **2026-07-15** — Eunna Lee, Jungpyo Nam, Sunjun Hwang — [Protective Capacity Hallucination: When Large Language Models Claim Nonexistent Capabilities](http://arxiv.org/abs/2607.13596v1)
  <details><summary>📄 Abstract</summary>
  When cast as the protector of a vulnerable user yet given no explicit capability boundary, a large language model (LLM) may respond not by acknowledging its limits but by claiming to have taken -- or to be taking -- a real-world protective action it cannot perform, such as contacting emergency services or administering care. We term this phenomenon Protective Capacity Hallucination (PCH): a self-referential misattribution in which a model, acting in a protective role, asserts physical or institu...
  </details>

- **2026-07-15** — Dima Galat, Marian-Andrei Rizoiu — [UTS at ELOQUENT 2026 Voight-Kampff: structural shifts in AI writing bypass state-of-the-art detectors](http://arxiv.org/abs/2607.13565v1)
  <details><summary>📄 Abstract</summary>
  We investigate which language model evasion attacks survive state-of-the-art adversarial fine-tuning, developing strategies that sweep the top 5 positions on the ELOQUENT 2026 Voight-Kampff leaderboard. While adversarial fine-tuning trivially closes the 2025 winning evasion recipes, we uncover a fundamental asymmetry in detector vulnerability: pushing generated text out of the detector's training distribution reliably defeats adversarial detection, whereas pulling it into the distribution (e.g.,...
  </details>

- **2026-07-15** — Andrea Maria Braghin, Nicolò Botteghi, Matteo Tomasetto et al. — [Flow-aware Optimal Navigation in Unsteady Flows through Reinforcement Learning](http://arxiv.org/abs/2607.13553v1)
  <details><summary>📄 Abstract</summary>
  Autonomous robotic navigation in nonstationary time-varying fluid flows remains a fundamental challenge due to partial observability and the unpredictability of realistic environments. While classical optimal control frameworks employed in robotics require unrealistic a-priori global flow knowledge, biological systems are able to navigate successfully by exploiting localized sensory cues. In this work we present a reinforcement learning approach using the TD3 algorithm to train autonomous agents...
  </details>

- **2026-07-14** — Qiyuan Fan, Zhi Li, Junjie Li et al. — [Bulkhead: Automated Semantic Detection and Remediation of Container Escape Vulnerabilities](http://arxiv.org/abs/2607.12723v1)
  <details><summary>📄 Abstract</summary>
  Filesystem isolation in container ecosystems is often weakened by cross-boundary path misresolution, causing path traversal (PaTra) vulnerabilities. These vulnerabilities stem from insecure host-container interactions and have become increasingly pervasive as cloud systems mount shared resources, such as GPUs and agent workspaces, into containers to support AI workloads. Existing defenses remain inadequate. Kernel-level protections are intrusive, can destabilize system calls, and have therefore ...
  </details>

- **2026-07-14** — Daomin Ji, Hui Luo, Zhifeng Bao et al. — [GRAFT: Graph-Matched Retrieval and Fusion of Tables in Data Lakes](http://arxiv.org/abs/2607.12717v1)
  <details><summary>📄 Abstract</summary>
  Autonomous data agents resolve analytical queries by retrieving and reasoning over evidence in tabular data lakes. Existing methods score tables independently against the query and ignore the joinability and unionability that link them, returning fragmented evidence that downstream agents cannot integrate. We propose GRAFT (Graph-matched Retrieval and Fusion of Tables), structured around two principal contributions. First, we cast table retrieval as a graph matching problem between a query-deriv...
  </details>

- **2026-07-14** — Rahul Krishnan, Volker Schulz — [A JoLT for the KV Cache: Near-Lossless KV Cache Compression via Joint Tucker and JL-Residual Allocation for LLMs](http://arxiv.org/abs/2607.12550v1)
  <details><summary>📄 Abstract</summary>
  The key-value (KV) cache has become the dominant memory cost of transformer inference. It grows with batch size, context length, and depth, and at long context it, rather than the model weights, sets the ceiling on throughput. Two families of methods reduce it. Low-rank methods factor two-dimensional slices of the cache, either per-head matrices or cross-layer feature blocks, and quantization methods lower the bit-width of every entry. Neither family exploits the fact that the cache at a layer i...
  </details>

- **2026-07-14** — Xianle Dai, Qu Luo, Jianguo Li et al. — [AFDM-FTN: A Spectrally Efficient Waveform for High-Mobility Communications](http://arxiv.org/abs/2607.12510v1)
  <details><summary>📄 Abstract</summary>
  This paper proposes an affine frequency division multiplexing (AFDM)-aided faster-than-Nyquist (FTN) waveform, termed AFDM-FTN, to enhance spectral efficiency (SE) in high-mobility communication scenarios. We first derive the AFDM-FTN input-output relationship and analyze the FTN-induced interference pattern in AFDM-FTN. To address the channel estimation challenges, a low-complexity channel estimator based on the basis expansion model (BEM) is developed. By exploiting the intrinsic characteristi...
  </details>

- **2026-07-14** — Yumiao Zhao, Bo Jiang, Min Lu et al. — [MQAdapter: Multi-Modal Quantum Adapter for Coarse-to-Fine VLM Fine-tuning](http://arxiv.org/abs/2607.12418v1)
  <details><summary>📄 Abstract</summary>
  Large-scale Vision-Language Models have demonstrated impressive transfer learning capabilities across a wide range of tasks. For few-shot classification, we observe that VLMs exhibit a notable ability to filter candidate categories and thus achieve high Top-K accuracy. However, they often struggle with fine-grained discrimination among visually similar categories, resulting in unsatisfactory Top-1 performance, as shown in Figure 1. Existing studies on VLM adapters generally focus on global align...
  </details>

- **2026-07-14** — Andrew G. Ross, Julia Gershenzon, Andreas Kleefeld — [Beyond Consistent Scenarios: Deriving Indirect Influence, Transition Resistance, and Adjustment Dynamics](http://arxiv.org/abs/2607.12414v1)
  <details><summary>📄 Abstract</summary>
  Assessments of structural change and economic transition dynamics, such as those arising in the energy transition, depend on internally consistent qualitative scenarios specifying the policy environment, technology mix, governance arrangements, and demand conditions. Cross-Impact Balance (CIB) analysis derives such socio-technical scenarios as fixed-point attractors of an expert-elicited interdependency network, supplying structural inputs upon which assessment models (including energy system op...
  </details>

- **2026-07-14** — Yameng Zhang, Zhongyu Chen, Dianye Huang et al. — [Seeing Globally, Refining Locally: Global Visual Guidance and Local Ultrasound Cues for Robust Freehand 3-D Ultrasound Reconstruction](http://arxiv.org/abs/2607.12398v1)
  <details><summary>📄 Abstract</summary>
  Freehand 3-D ultrasound (US) imaging has attracted increasing attention owing to its intuitive volumetric visualization, ease of use, and low cost. However, accurate 3-D reconstruction critically depends on stable probe pose estimation, yet existing trackerless methods remain susceptible to accumulated pose errors, particularly over long scanning trajectories. To address this limitation, we propose a global-to-local pose estimation framework that exploits external camera observations for globall...
  </details>

- **2026-07-14** — Hao Xu, Yuqing Zhang, Yiqian Wu et al. — [SeamGen: Artist-Aligned UV Seam Generation via Graph Flow Matching](http://arxiv.org/abs/2607.12379v1)
  <details><summary>📄 Abstract</summary>
  UV seam placement is a critical yet labor-intensive step in 3D content creation, requiring artists to balance chart shape, seam concealment, and alignment with semantic and geometric features. Existing automatic methods are primarily based on per-object optimization, relying on handcrafted objectives to avoid distortion or on proxies from pretrained models to inject semantic information. However, these strategies are not always well aligned with seams used in industrial production pipelines, oft...
  </details>

- **2026-07-14** — Alon Shakevsky, Corban Villa, Ion Stoica et al. — [Antiproof: Synthesizing Vulnerability Detectors and Proofs of Exploitability](http://arxiv.org/abs/2607.12316v1)
  <details><summary>📄 Abstract</summary>
  Discovering vulnerabilities before attackers exploit them requires high recall and reliable automatic validation, but existing approaches struggle to achieve both without prohibitive cost. We present Antiproof, an end-to-end vulnerability discovery system that combines neuro-symbolic detector synthesis for high-recall discovery with proof-of-exploitability oracles for automatic validation. Antiproof learns and iteratively refines static detectors from vulnerability datasets, then validates candi...
  </details>

- **2026-07-14** — Gregory Hyegang Jun, Wesley Pang, Eddie Richter et al. — [HeteroMosaic: Exposing and Exploiting Heterogeneous Execution Opportunities for Energy-Efficient Edge LLM Inference](http://arxiv.org/abs/2607.12839v2)
  <details><summary>📄 Abstract</summary>
  Modern edge system-on-chips (SoCs) combine CPUs, integrated GPUs (iGPUs), and neural processing units (NPUs), yet existing LLM runtimes typically make coarse device-level decisions or optimize operators in isolation. As a result, they underutilize heterogeneous resources, particularly on unified-memory platforms where performance depends on both device placement and task-graph coordination. We present HeteroMosaic, a heterogeneity-first scheduling framework for edge LLM inference. HeteroMosaic f...
  </details>

- **2026-07-14** — Aleh Manchuliantsau — [Win by Silence: Deletion Non-Monotonicity, Autonomous Exploitation, and Typed-State Gating in LLM Plan Evaluation](http://arxiv.org/abs/2607.12986v1)
  <details><summary>📄 Abstract</summary>
  Plan evaluators can reward a strategic plan for becoming less explicit. This paper studies that failure in a staged expected-value scorer for LLM-generated venture routes. Proposition 1 gives the score change from deleting an interior transition while retargeting its predecessor and retaining downstream value: Delta_k = (prod_{i<k} p_i)[c_k + (1 - p_k)R_{k+1}]. On a frozen 26-route cohort, all 57 admissible deletions matched the analytic identity and threshold sign, and every route had at least ...
  </details>

- **2026-07-14** — Duantengchuan Li, Yingqian Bi, Jinsong Chen et al. — [Disentangling Knowledge States with Ability and Proficiency Modeling for Knowledge Tracing](http://arxiv.org/abs/2607.13103v1)
  <details><summary>📄 Abstract</summary>
  Knowledge tracing (KT) aims to predict students' future performance by modeling their evolving knowledge states from historical interactions. Existing KT methods usually treat the raw interaction sequence as a unified behavioral process, overlooking the phase-specific nature of learning behaviors. Our preliminary observations show that students are more likely to correctly answer previously failed knowledge concepts after sufficient practice, suggesting a transition from ability-building to prof...
  </details>

- **2026-07-14** — Mohammadreza Rashidi — [Open-Source Intelligence for Code Provenance and the Security Patterns that Separate Human and Large-Language-Model Implementations of Common Programming Tasks](http://arxiv.org/abs/2607.12524v1)
  <details><summary>📄 Abstract</summary>
  Developers now draw code from two very different sources, the accumulated human answers on sites such as Stack Overflow and the output of large language models. We ask two questions about that split. First, can the provenance of a code snippet be recovered from the code itself, and second, do the two sources differ in the security patterns they adopt for the same task. Using only open sources, a public gateway of open-weight language models and the public Stack Overflow API, we build a fully rep...
  </details>

- **2026-07-14** — Yuhang Yan, Linchao Mou, Bokang Yang et al. — [TerraLogic: A Benchmark for Hierarchical Geospatial Reasoning in Earth Observation](http://arxiv.org/abs/2607.12497v1)
  <details><summary>📄 Abstract</summary>
  Beyond perception, reasoning is essential in remote sensing for advanced interpretation, inference, and decision-making. Recent advances in large language models (LLMs) have enabled tool-augmented agents that leverage external tools to perform complex analytical tasks. However, existing studies in remote sensing primarily focus on perception-oriented tasks, leaving cognitive geospatial reasoning largely underexplored. To address this gap, we introduce TerraLogic, a benchmark for geospatial reaso...
  </details>

- **2026-07-14** — Yubo Wang, Jiarong Liang, Yuxuan Zhang et al. — [Function-Aware Fill-in-the-Middle as Mid-Training for Coding Agent Foundation Models](http://arxiv.org/abs/2607.12463v1)
  <details><summary>📄 Abstract</summary>
  Coding agents must integrate external tool returns into ongoing reasoning - a capability that standard left-to-right pretraining on code exposes only in its forward direction. We observe that the action-observation-continuation loop of a coding agent is structurally isomorphic to a function call site, where a caller binds arguments, a callee returns a value computed elsewhere, and downstream code consumes that value. This conditioning structure exists at internet scale in ordinary code. We explo...
  </details>

- **2026-07-14** — Haitian Zhang, Thai Duy Nguyen, Xiangyuan Wang et al. — [UMSS: Towards Unsupervised Multi-modal Semantic Segmentation](http://arxiv.org/abs/2607.12372v1)
  <details><summary>📄 Abstract</summary>
  Multimodal semantic segmentation (MSS) is essential for robust perception in complex environments, yet its potential remains largely untapped because of the prohibitive cost of human annotations. While unsupervised semantic segmentation (USS) has achieved strong results on a single RGB modality, its naive extension to multimodal data is often hindered by fusion degradation. This occurs because, without explicit supervision, existing frameworks struggle to reconcile the heterogeneous structural p...
  </details>

- **2026-07-14** — Weifeng Yuan, Wenbo Guo, Feng Dong et al. — [Skills That Don't Exist: A Large-Scale Study of Hallucinated Skill Recommendation in LLM Agents](http://arxiv.org/abs/2607.12340v1)
  <details><summary>📄 Abstract</summary>
  LLM agents acquire new capabilities by downloading skills from open registries. Instead of browsing these catalogs manually, developers typically ask the agent to recommend and install a skill. This convenience hides a risk: agents frequently invent names for skills that exist in no registry. We term this flaw skill name hallucination. A fake name may seem harmless, but it opens the door to supply-chain attacks. Because registries rarely verify publishers, an adversary can prompt the agent, coll...
  </details>

- **2026-07-14** — Zhuohao Zhang, Junkun Liu, Rui Yang et al. — [Mystra: Declarative Dynamic Taint Analysis via Shadow Virtual Machine](http://arxiv.org/abs/2607.12308v2)
  <details><summary>📄 Abstract</summary>
  Dynamic taint analysis (DTA) for interpreted languages like JavaScript and Python requires three capabilities: observing host-runtime operations, maintaining parallel taint states, and defining how taint propagates. Existing systems couple these capabilities within an instrumentation mechanism -- source-rewriting or engine-native -- either incurring high runtime overhead or demanding engine-specific embeddings. There is yet to be a runtime-independent abstraction of a general DTA that separates ...
  </details>

- **2026-07-13** — Gabriel Paris-Colombo, Rodrigo M. Cabral-Carvalho, Felipe D. Toro-Hernández — [Comparing Semantic Navigation in Humans and Large Language Models using Natural Language Processing](http://arxiv.org/abs/2607.12195v1)
  <details><summary>📄 Abstract</summary>
  Semantic memory retrieval can be conceptualized as navigation through conceptual space. We compared semantic search dynamics between humans and three large language models (GPT-4o, Gemini-2.5-Pro, Claude-Sonnet-4.5) using verbal fluency data. By applying trajectory-based NLP metrics to the items generated by 82 human participants and LLM output across eight temperature settings, we quantified three complementary dimensions: entropy (step size predictability), distance to next (successive semanti...
  </details>

- **2026-07-13** — Arastoo Zibaeirad, Marco Vieira, Thomas Zimmermann — [AutoTrace: From Patches to Triggers via Agentic Interprocedural Exploration](http://arxiv.org/abs/2607.12058v1)
  <details><summary>📄 Abstract</summary>
  Given a vulnerability-fixing commit, trigger localization asks which specific statement turns the vulnerable program state into a concrete unsafe operation. This question is harder than binary vulnerability detection because the answer demands interprocedural, causal reasoning: in a substantial fraction of real-world CVEs the triggering statement lies several call layers outside the patched function, beyond the reach of static rule sets and pattern-matching language models alike. We present Auto...
  </details>

- **2026-07-13** — Iman Johary, Guillaume Bied, Alexandru C. Mara et al. — [STEP: Career-Path Recommendation via Temporal and Educational Trajectory Modeling](http://arxiv.org/abs/2607.11722v2)
  <details><summary>📄 Abstract</summary>
  Career paths encode decades of skill acquisition, role transitions, and educational investment, and understanding them at scale underpins workforce planning, labor market policy, and job recommendation. Resumes are a rich source of information about career paths: they contain detailed descriptions of work experience, education, and skills. Yet their unstructured, heterogeneous, and multilingual nature has long prevented large-scale systematic analysis. With the advent of large language models (L...
  </details>

- **2026-07-13** — Induk Um, Youngung Han, Kyeonghun Kim et al. — [SpikeDS: Dual Sparsity Spikformer for Perineural Invasion Prediction in 3D MRI](http://arxiv.org/abs/2607.11986v1)
  <details><summary>📄 Abstract</summary>
  Perineural invasion (PNI) is associated with poor prognosis in cholangiocarcinoma (CCA). However, its detection from 3D MRI remains challenging due to the subtle and spatially heterogeneous imaging signatures at the tumor periphery. Capturing such spatially sparse cues necessitates volumetric analysis of 3D MRI, but existing deep learning approaches incur prohibitive computational costs on volumetric medical images, limiting their clinical deployment. We propose Dual Sparsity Spikformer (SpikeDS...
  </details>

- **2026-07-13** — Ziqi Yin, Jianyang Gao, Peiqi Yin et al. — [LiteTopK: Exploiting the Curse of Dimensionality for a Fused Indexer-TopK Kernel in Long-Context Sparse Attention](http://arxiv.org/abs/2607.11976v2)
  <details><summary>📄 Abstract</summary>
  Indexer-TopK, the operation to compute the scores and select the top-k candidates, is widely used by sparse attention kernels in large language models and vector retrieval in recommendation systems and vector databases. However, existing GPU-based Indexer-TopK kernels like DeepSeek Sparse Attention (DSA) remain inefficient due to excessive global memory traffic, costly synchronization, and prohibitive memory overhead. In this work, we exploit the curse of dimensionality in high-dimensional space...
  </details>

- **2026-07-13** — Lukas Rapp, Jiewei Feng, Muriel Médard et al. — [Generalized Segmented GRAND for Guesswork Reduction in Turbo Product Decoding](http://arxiv.org/abs/2607.12147v1)
  <details><summary>📄 Abstract</summary>
  Guessing random additive noise decoding (GRAND) can efficiently decode any moderately redundant code with near maximum likelihood (ML) performance via noise effect guessing. For binary linear codes, Rowshan and Yuan's Segmented GRAND was the first to show that constrained guessing can reduce guesswork. Although powerful, their approach requires a specific parity-check matrix structure that limits the number of constraints that can be exploited as well as the class of applicable codes. Here we in...
  </details>

- **2026-07-13** — Zeyan Liang, Graham McDonald, Iadh Ounis — [Explaining When PRF Fails: Participatory Auditing for Selective Query Expansion](http://arxiv.org/abs/2607.12098v1)
  <details><summary>📄 Abstract</summary>
  Pseudo-Relevance Feedback (PRF) improves retrieval effectiveness on average, but harms a substantial fraction of queries through query drift, an asymmetry hidden by aggregate offline metrics. Existing Selective PRF (sPRF) approaches typically rely on Query Performance Prediction (QPP) methods derived from the same ranking statistics, and therefore inherit, rather than resolve, this opacity. We argue that this is a core explainability problem in IR, and propose a two-stage audit-then-automate fra...
  </details>

- **2026-07-13** — Kerui Chen, Jinglu Wang, Xiaoyi Zhang et al. — [Beyond the Single Camera: Agentic Multi-View Reasoning in Sports Video Understanding](http://arxiv.org/abs/2607.11844v1)
  <details><summary>📄 Abstract</summary>
  Recent Multimodal Large Language Models (MLLMs) achieve strong performance on single-view video understanding benchmarks. However, sports videos involve dense occlusion, rapid motion, and complex interactions that are difficult to resolve from a single viewpoint. In practice, sports events are recorded from multiple camera angles, providing complementary evidence used by referees. Yet, no existing benchmark evaluates MLLMs on multi-view sports video understanding. To address this gap, we introdu...
  </details>

- **2026-07-13** — Moritz Schaffenroth, Uwe Kölbel, Heike Lepke et al. — [Multi-Agent Reinforcement Learning for C-V2X RAT Selection](http://arxiv.org/abs/2607.11744v1)
  <details><summary>📄 Abstract</summary>
  Vehicles are increasingly equipped with advanced V2X communication capabilities. While early V2X apps utilized services such as Cooperative Awareness Messages, recent developments have allowed more advanced applications including cooperative driving, shared perception, and sensor-sharing services. The broader mix of applications leads to heterogeneous requirements for latency and reliability. At the same time multiple communication technologies for V2X are available with pros and cons. Hybrid V2...
  </details>

- **2026-07-13** — Iman Johary, Guillaume Bied, Alexandru C. Mara et al. — [STEP: Career-Path Recommendation via Temporal and Educational Trajectory Modeling](http://arxiv.org/abs/2607.11722v1)
  <details><summary>📄 Abstract</summary>
  Career paths encode decades of skill acquisition, role transitions, and educational investment, and understanding them at scale underpins workforce planning, labor market policy, and job recommendation. Resumes are a rich source of information about career paths: they contain detailed descriptions of work experience, education, and skills. Yet their unstructured, heterogeneous, and multilingual nature has long prevented large-scale systematic analysis. With the advent of large language models (L...
  </details>

- **2026-07-13** — Julie Gilbert, Francesco Calzaferri — [Targeting DNA Methylation: New Paradigms and the Advent of Gene-Selective Tools](http://arxiv.org/abs/2607.11697v1)
  <details><summary>📄 Abstract</summary>
  DNA methylation can function as a toxic alkylation reaction exploited by chemotherapeutic agents to induce cancer cell death. However, finely tuned DNA methylation plays a fundamental role in cellular physiology, particularly in the epigenetic regulation of gene expression. Once thought to act solely as a repressor of gene transcription, its functional role has since been elucidated as genomic locus-specific and deeply connected with other epigenetic factors. Following the clinical approval of D...
  </details>

- **2026-07-13** — Chengcheng Yan, Qingsong Wang — [Structure-Feature Aligned Graph Learning via Alternating Constrained Optimization](http://arxiv.org/abs/2607.11577v1)
  <details><summary>📄 Abstract</summary>
  We introduce a constrained two-view framework for node prediction that aligns structure-conditioned GNN embeddings with a structure-free feature prior learned by an anchor model. Conventional Graph Neural Networks (GNNs) couple feature transformation and neighborhood aggregation, which renders them vulnerable to topology noise and heterophilous connections. To decouple this dependency, our framework utilizes an independent anchor network to capture intrinsic attribute features via a self-supervi...
  </details>

- **2026-07-13** — Tianyuan Zhang, Zonglei Jing, Jiangfan Liu et al. — [Technical Report on the CVPR 2026@AdvML Workshop Challenge](http://arxiv.org/abs/2607.11560v1)
  <details><summary>📄 Abstract</summary>
  Vision-language agents (VLAs) are increasingly used to interpret complex driving scenes and support safety-critical reasoning. This report presents the CVPR 2026@AdvML Workshop Challenge on adversarial multimodal attacks against autonomous-driving VLAs. Built on DriveLM-style multi-view visual question answering, the challenge represents each scene with six synchronized camera images and a structured collection of driving-related question-answer pairs. Participants generate adversarial images an...
  </details>

- **2026-07-13** — Xiaolin Wen, Feng Liang, Yuanye Ma et al. — [ManiScope: LLM-Assisted Visual Analytics of Cryptocurrency Manipulation Risk](http://arxiv.org/abs/2607.11451v1)
  <details><summary>📄 Abstract</summary>
  Cryptocurrency markets are vulnerable to trade-based manipulation, such as wash trading, which can distort price signals and mislead investors. Prior research has mainly focused on detecting manipulation using fixed rules or labeled examples, offering limited flexibility and interpretability for assessing potential risks. Existing visual analytics tools can reveal basic manipulation-related signals, such as token distribution, but still require substantial manual effort to integrate holder relat...
  </details>

- **2026-07-13** — Minase Mekete Mengistu, Juri Di Rocco, Phuong T. Nguyen et al. — [TerraRepair: A Tool-Grounded LLM Agent for Infrastructure-as-Code Repair](http://arxiv.org/abs/2607.11390v1)
  <details><summary>📄 Abstract</summary>
  Background: Infrastructure-as-Code (IaC) scanners detect cloud misconfigurations in Terraform and other IaC languages before deployment, but repairing the flagged configurations remains largely manual. Recent Large Language Model (LLM)-based repair approaches can repair some findings, but may hallucinate unsupported constructs or suppress warnings without fixing the issue. Aims: We study whether tool grounding can improve LLM-based Terraform repair, and when a finding should be escalated because...
  </details>

- **2026-07-13** — Mingxi Xu, Bowen Duan, Yi Gu et al. — [HandFlow: Fully Generative 4D Hand Recovery with Flow Matching](http://arxiv.org/abs/2607.11221v1)
  <details><summary>📄 Abstract</summary>
  Accurate monocular 4D hand reconstruction remains challenging. Per-frame discriminative regressors lack temporal context and often produce jittery predictions. Temporal models improve consistency by aggregating information across frames, but they are typically deterministic regressors, making them vulnerable to ambiguous observations caused by occlusion and motion blur. Generative modeling offers a natural alternative by learning a prior over plausible hand motion sequences, enabling coherent ha...
  </details>

- **2026-07-13** — Kim Hammar, Yuchao Li — [Recovery Control in Replicated Systems through Autonomous Multiagent Rollout](http://arxiv.org/abs/2607.11187v1)
  <details><summary>📄 Abstract</summary>
  We study recovery control in replicated computing systems. Such systems consist of replicas that collectively provide a service to a client population. This redundancy enables the system to withstand failures provided that failed replicas are recovered faster than new failures occur. We show that the problem of deciding when to initiate recovery of selected replicas can be formulated as a partially observable Markov decision problem (POMDP) with a multiagent structure. We exploit this structure ...
  </details>

- **2026-07-13** — Seohwan Yun, Jeeyoung Yun, Yongjin Kim et al. — [MusicMark: A Robust Generative Watermarking Framework for Music Generation](http://arxiv.org/abs/2607.11117v1)
  <details><summary>📄 Abstract</summary>
  AI music generation has rapidly advanced alongside commercial platforms, raising the need for reliable watermarking for provenance and attribution. However, existing audio watermarking research has largely focused on speech, and applying speech-oriented methods to music is challenging due to music's complex structure and rich acoustic texture. Most existing methods are post-hoc, adding imperceptible perturbations after generation rather than embedding watermarks as part of the content. This make...
  </details>

- **2026-07-13** — Zhen-Lin Chen, Maosen Sheng, Peng Lin et al. — [MMRM: A Multiplex Multimodal Representation Model for Product Ranking in E-commerce Search](http://arxiv.org/abs/2607.11030v1)
  <details><summary>📄 Abstract</summary>
  Multimodal information is pivotal for e-commerce search ranking. Existing works leverage multimodal data typically by fine-tuning general Multimodal Large Language Models (MLLMs) via collaborative signals, subsequently integrating the derived representations into ranking models as item features. Despite their efficacy, these methods face two primary limitations: (1) they rely on a single collaborative signal for MLLM fine-tuning, failing to exploit the heterogeneous signals essential for multita...
  </details>

- **2026-07-13** — Qiyang Sun, Yi Chang, Yupei Li et al. — [CHARM: Charge Calibration and Acoustic Rescue for LLM-based Multimodal Sarcasm Detection](http://arxiv.org/abs/2607.11102v1)
  <details><summary>📄 Abstract</summary>
  Sarcasm detection, the identification of discrepancies between literal and intended meaning, is a fundamental task in affective computing. However, zero-shot instruction-tuned Large Language Models (LLMs) systematically over-predict the positive (sarcastic) class across the entire capability spectrum, while the prosodic cues humans rely on remain underexploited and transfer unevenly across languages. We introduce CHARM (Charge Calibration and Acoustic Rescue for Multimodal Sarcasm Detection), a ...
  </details>

- **2026-07-12** — Joshua Haworth, Aryan Pasikhani, George Pavlides et al. — [Automated Stealthy Wear-Out Attack on Digital Twins With Deep Reinforcement Learning](http://arxiv.org/abs/2607.10830v1)
  <details><summary>📄 Abstract</summary>
  Digital Twins (DTs) have emerged as pivotal enablers of Industry 4.0, offering transformative capabilities such as real-time monitoring, advanced simulation, and precise control of physical assets. By bridging the physical and virtual domains, DTs facilitate seamless integration of data-driven decision-making and operational optimisation. However, this seamless interaction significantly expands the attack surface of industrial systems, creating vulnerabilities that adversaries can exploit. This ...
  </details>

- **2026-07-12** — Fengji Zhang, Tianyu Fan, Yuxiang Zheng et al. — [To Answer or to Abstain: Mitigating Search-Agent Hallucinations via Abstention-Aware Reinforcement Learning](http://arxiv.org/abs/2607.10738v1)
  <details><summary>📄 Abstract</summary>
  Recent advances in equipping Large Language Models (LLMs) with search tools and outcome-reward reinforcement learning (RL) have achieved new state-of-the-art results on open-domain QA tasks. However, we argue that current training paradigms harbor a critical vulnerability: they predominantly reward correct answers but fail to penalize fabricated ones when retrieval fails, thereby implicitly exacerbating hallucinations. To address this, we propose Abstention-Aware Reinforcement Learning (AWA-RL),...
  </details>

- **2026-07-12** — Zipeng Gao, Zhi Zheng, Qingrong Xia et al. — [Unlocking Parallelism in Autoregressive Language Models via Speculative Decoding with Progressive Tree Drafting](http://arxiv.org/abs/2607.10661v1)
  <details><summary>📄 Abstract</summary>
  Speculative decoding has significantly accelerated Large Language Model (LLM) inference by alleviating memory-bound bottlenecks. However, traditional speculative decoding typically relies on auxiliary draft modules, incurring significant training and communication overhead. Although recent methods attempt to generate drafts within the target model itself, they often fail to fully exploit its latent parallel capacity due to a lack of structural coordination. In this paper, we propose \textbf{Prog...
  </details>

- **2026-07-12** — Xiatao Sun, Yuan Zhuang, Mateo Sanchez Lopez Negrete et al. — [Artificial Foveated Perception for Mitigating Shortcut Learning in Robotic Foundation Models](http://arxiv.org/abs/2607.10655v1)
  <details><summary>📄 Abstract</summary>
  Robotic foundation models have recently made substantial progress in multi-task capability, cross-embodiment transfer, and language-conditioned control. Yet robust deployment across diverse real-world settings remains difficult, in part because policies often fail to distinguish causally relevant visual structure from spurious scene-level correlations. We identify this failure mode as shortcut learning: the tendency to exploit predictive but non-causal correlations in the training distribution r...
  </details>

- **2026-07-12** — JungMin Yun, JuneHyoung Kwon, YoungBin Kim — [CRiT-QA: Evaluating Multi-hop Reasoning with Counterfactual Chains and Distractor Traps](http://arxiv.org/abs/2607.10562v1)
  <details><summary>📄 Abstract</summary>
  Evaluating the multi-hop reasoning capabilities of large language models remains a significant challenge. Although current models achieve strong results on existing multi-hop question answering datasets, such performance often masks two critical vulnerabilities: (1) reliance on internal parametric knowledge rather than adherence to the provided context, and (2) exploitation of dataset shortcuts, such as single-document cues or type-matching, that diminish the need for genuine evidence aggregatio...
  </details>

- **2026-07-12** — Shengyuan Liu, Jia-Xuan Jiang, Boyun Zheng et al. — [Towards Autonomous and Auditable Medical Imaging Model Development](http://arxiv.org/abs/2607.10522v1)
  <details><summary>📄 Abstract</summary>
  Large language model (LLM) agents are beginning to automate machine learning engineering (MLE) by coupling planning, code execution, debugging, and empirical feedback. Translating this capability to medical imaging remains difficult because each task imposes modality-specific experimentation and strict requirements for validation protocols and prediction artifacts. Here we introduce AMID, an autonomous multi-agent framework for medical imaging model development. AMID first proposes Data-Conditio...
  </details>


### 📂 defense
*防御与防护方法 / Defense & Protection Methods* — 54 papers

- **2026-07-15** — Hyeongcheol Kim, Yoontae Hwang — [From Forecasts to Auditable Reports: Evidence Contracts for LLM-Assisted Housing-Guarantee Risk Monitoring](http://arxiv.org/abs/2607.14026v1)
  <details><summary>📄 Abstract</summary>
  Translating next-month housing-guarantee risk forecasts into auditable operational reports is essential yet challenging because upper-tail events are sparse, source records are confidential, and generated narratives can distort the underlying evidence. Using monthly South Korean \textit{jeonse} deposit guarantee data from September 2015 to December 2025, we introduce an evidence-constrained reporting pipeline that prioritizes upper-tail monitoring, retrieves historical precedents aligned with th...
  </details>

- **2026-07-15** — Mustafa Chasmai, Vincent Dumoulin, Jenny Hamer — [MetaPerch: Learning from metadata for bioacoustics foundation models](http://arxiv.org/abs/2607.14072v1)
  <details><summary>📄 Abstract</summary>
  Bioacoustic foundation models rely on large-scale citizen science platforms like Xeno-Canto for geographically and ecologically diverse data. Recent work has shown that supervision alone can produce SotA species detection models when trained on this large-scale data -- however, there remains unutilized potential in the form of recording metadata readily available within these community-driven data hubs. In this work, we explore the use of metadata -- such as location and time -- as auxiliary sup...
  </details>

- **2026-07-15** — Jeremy Guntoro, Alexander Dack, Dylan Danno et al. — [Screening of Biosecurity Features in Metagenomic Data with Evo 2 Probes](http://arxiv.org/abs/2607.14070v1)
  <details><summary>📄 Abstract</summary>
  Genomic foundation models such as Evo 2 learn rich sequence representations, but their value for biosecurity screening is largely unexplored. We ask how much biosecurity-relevant signal is linearly accessible in these representations by training minimal linear and attention probes on frozen Evo 2 layer-26 activations, without fine-tuning the underlying model. Across held-out metagenomic test sets, the probes detect antimicrobial resistance (AMR) with strong discrimination: a linear probe reaches...
  </details>

- **2026-07-15** — Abdallah Aaraba, Alexis Vieloszynski, Remon Polus et al. — [RF Spectrogram Anomaly Detection with Quantum Kitchen Sinks: Architecture, Representation, and Hardware Validation](http://arxiv.org/abs/2607.13897v1)
  <details><summary>📄 Abstract</summary>
  The broadcast nature of wireless channels exposes radio-frequency (RF) networks to anomalous and malicious transmissions, making anomaly detection a fundamental requirement for secure spectrum management. Quantum Kitchen Sinks (QKS) offer a lightweight hybrid quantum feature map suitable for near-term quantum devices, yet their behavior on structured signal data remains poorly understood. In this paper, we extend the standard QKS template with multi-depth data re-uploading and ring entanglement,...
  </details>

- **2026-07-15** — Zexun Wang — [CAVA: Canonical Action Verification and Attestation for Runtime Governance of Agentic AI Systems](http://arxiv.org/abs/2607.13716v1)
  <details><summary>📄 Abstract</summary>
  Agentic AI systems increasingly act through heterogeneous runtimes: local coding hooks, SDK tools, browser automation, managed-agent traces, API gateways, and workflow engines. A single operational act such as publishing code, changing identity state, moving money, or exporting data may therefore be represented by many incompatible runtime records. This makes a basic governance question difficult to answer: what action was actually approved, what evidence binds the approval to execution, and can...
  </details>

- **2026-07-15** — Sagar Deb, Ashwanth Krishnan — [STOCKTAKE: Measuring the Gap Between Perception and Action in LLM Agents with a Fair Oracle](http://arxiv.org/abs/2607.13618v1)
  <details><summary>📄 Abstract</summary>
  LLM agents are increasingly evaluated on multi-week decision tasks in which the state that drives cost is never directly observed. On such tasks the final cost cannot say why an agent failed: it may have misread the world, or read it correctly and still failed to act (the knowing-doing gap). Existing evaluations cannot separate these two failures; their reference policies either read privileged information the agent never sees, or are missing altogether. We introduce STOCKTAKE, a 26-week supply-...
  </details>

- **2026-07-15** — Xixuan Hao, Yutian Jiang, Jiabo Liu et al. — [Multi-Agent Collaborative Reasoning with Tool-Augmented Evidence for Urban Region Profiling](http://arxiv.org/abs/2607.13558v1)
  <details><summary>📄 Abstract</summary>
  Urban region profiling constitutes a core problem in urban computing, supporting applications such as population estimation, economic assessment, and environmental monitoring. Existing methods typically formulate this task as multimodal representation learning, fusing heterogeneous urban data, e.g., satellite imagery, points of interest, textual descriptions, and 3D building information, into latent embeddings for prediction. However, these approaches are largely correlation-driven, assume cross...
  </details>

- **2026-07-15** — Emad Abukhousa, Saman Zonouz, A. P. Sakis Meliopoulos — [Transformer is All You Need: Attention-Based Anomaly Detection and Classification in Inverter-Rich Power Systems](http://arxiv.org/abs/2607.13537v1)
  <details><summary>📄 Abstract</summary>
  Inverter-based resources and IEC 61850 process-bus measurements introduce new protection challenges, including nontraditional fault behavior and measurement-domain cyber-physical attacks. This paper evaluates DL-Xformer, an attention-based Transformer classifier for multi-class fault and cyberattack diagnosis, side-by-side with Dynamic State Estimation-Based Protection (DSE-EBP) on identical high-fidelity electromagnetic-transient (EMT) streaming measurements from an IBR-rich power grid. The eva...
  </details>

- **2026-07-14** — Yunzhou Li, Jiesi Hu, Yanwu Yang et al. — [UniMedSeg: Unified In-Context Learning for Multi-Paradigm 2D/3D Medical Image Segmentation](http://arxiv.org/abs/2607.12896v1)
  <details><summary>📄 Abstract</summary>
  Medical image segmentation foundation models are expected to generalize across diverse clinical scenarios, yet existing universal methods remain fragmented by prompt paradigms and spatial dimensions. Visual in-context learning, interactive segmentation, and language-guided segmentation are typically handled by paradigm-specific models, while 2D and 3D images are also modeled separately. Such isolation prevents heterogeneous annotations and data from being jointly absorbed by a single scalable mo...
  </details>

- **2026-07-14** — Zhiyu He, Zecheng Zhao, Tong Chen et al. — [What Would You Click? Personalized Video Thumbnail Generation with Preference-aware Highlight Retrieval](http://arxiv.org/abs/2607.12882v1)
  <details><summary>📄 Abstract</summary>
  Video thumbnails are a key factor for attracting user clicks on video platforms, and are increasingly supported by automation. However, existing thumbnail generation methods typically produce generic results shared across users, overlooking the diversity of individual preferences. We therefore introduce personalized video thumbnail generation, a novel task that aims to create thumbnails tailored to user-specific preferences. It is challenging in two aspects: (i) identifying visual anchors (i.e.,...
  </details>

- **2026-07-14** — Sania Waheed, Michael Milford, Sarvapali D. Ramchurn et al. — [Breaking Déjà Vu: Independent Auditing of Visual Place Recognition through Vision-Language Reasoning](http://arxiv.org/abs/2607.12818v2)
  <details><summary>📄 Abstract</summary>
  Visual place recognition (VPR) is a key enabler of accurate localization and long-term autonomous navigation in robotics applications, such as loop closure detection for simultaneous localisation and mapping (SLAM). However, real-world VPR deployment relies on selecting an image matching threshold that balances precision and recall. These thresholds are typically tuned using labeled validation data and fixed during deployment, making them unreliable under environmental changes where ground truth...
  </details>

- **2026-07-14** — Ruikang Li, Molin Li, Jiarui Wu et al. — [Color Pass-Through via Camera-Display Coupling](http://arxiv.org/abs/2607.12746v1)
  <details><summary>📄 Abstract</summary>
  When a real-world scene is captured by a smartphone camera and viewed on its screen, the displayed image often differs noticeably from the original scene in color, brightness, and contrast. This gap persists despite substantial advances in both modern cameras and displays. A key reason is that most pipelines factor the high-dimensional capture-to-display process into two separately calibrated camera and display stages, and then connect them through low-dimensional color transforms, leading to in...
  </details>

- **2026-07-14** — Chengjie Wang, Jingzheng Wu, Xiang Ling et al. — [Taming the Drift: Context-aware Repair of Dockerfile Drift during Software Evolution](http://arxiv.org/abs/2607.12541v1)
  <details><summary>📄 Abstract</summary>
  Docker is widely used to create reproducible build environments, but Dockerfile drift, the divergence between a Dockerfile and its evolving source code, can cause CI/CD builds to fail. Existing rule-based and retrieval-based repair approaches analyze Dockerfiles in isolation and therefore struggle with context-dependent failures. We present Cadre, a context-aware framework for automated Dockerfile drift repair. Cadre uses static analysis to construct a Context-aware Dependency Graph (CDG), which...
  </details>

- **2026-07-14** — Farnaz Farid, Raihan Alam, Al Al-Areqi et al. — [Evaluating Health Misinformation in Low-Resource Languages: Integrating Small Language Models with a Culturally-Sensitive Responsible NLP Framework (Bangla as a Case Study)](http://arxiv.org/abs/2607.12336v1)
  <details><summary>📄 Abstract</summary>
  Artificial Intelligence (AI) technologies, while serving as a foundational enabler for modern social media and digital health services, exert a bivalent effect by simultaneously acting as a combatant against and a spread vector for misinformation. A prevalent challenge in mitigating this issue arises in non-English contexts and low socioeconomic classes, where limited data hinders the training of AI models for effective detection. Consequently, culturally and linguistically diverse (CALD) commun...
  </details>

- **2026-07-14** — Xi Cheng, Ke Liu, Siyuan Feng et al. — [Cost-Optimal Foundation Model Deployment Portfolio for Transportation Management](http://arxiv.org/abs/2607.13239v1)
  <details><summary>📄 Abstract</summary>
  Foundation models, including large language models (LLMs) and vision-language models (VLMs), are increasingly used for transportation management center (TMC) tasks such as anomaly detection, incident reporting, and traveler information. Deploying multiple such models across TMC functions raises a portfolio question: which model should serve each function, in which deployment mode, and under what shared hardware budget? We formulate this as the Foundation Model Deployment Portfolio (FMDP) problem...
  </details>

- **2026-07-14** — Xiaoyu Li, Zheng Gao, Xiaoyan Feng et al. — [Watermark Forensics for Generative Models: An Information-Theoretic Perspective](http://arxiv.org/abs/2607.13003v1)
  <details><summary>📄 Abstract</summary>
  A watermark in a generative model's output is usually asked only whether a text is machine-made. The same mark can do more: attribute it to the user who produced it, extract a hidden payload, or localize the part that survives editing. These form a forensic ladder, and we ask what each rung costs in the sample length $n$.   One object organizes the answers. Let $S$ be the secret the mark carries (a user's identity or payload), and let the information profile $ν(t)=I(S;X_t\mid X_{<t})$ record how...
  </details>

- **2026-07-14** — T. O. Hodd, L. C. Gallo, A. G. Gonzalez et al. — [Investigating the Periodic X-ray Behaviour in the Eclipsing AGN NGC 6814](http://arxiv.org/abs/2607.12904v1)
  <details><summary>📄 Abstract</summary>
  A 2016 XMM-Newton X-ray light curve of the Seyfert 1.5 galaxy NGC 6814 exhibited clear eclipsing behaviour, with distinct ingress and egress, during half of the observation. Here, we report on the periodic behaviour in the light curve prior to the eclipse. We use timing and spectral analysis techniques to quantify the behaviour and examine the characteristics of the periodic signal. A superlet transform of the X-ray light curve reveals a period of ~45-50 $μ$Hz in the initial 60 ks of the observa...
  </details>

- **2026-07-14** — Cameron Cagan, Pedram Fard, Jiazi Tian et al. — [A Multi-Agent System for Autonomous, Fine-Tuning-Free Clinical Symptom Detection: Development and Validation Study](http://arxiv.org/abs/2607.12886v1)
  <details><summary>📄 Abstract</summary>
  Clinical notes contain many of the signs and symptoms that bring patients to care, yet this information rarely reaches structured fields. Existing extraction approaches either rely on context-insensitive rules that generate false positives or on supervised models that require substantial fine-tuning. We present Pythia, a multi-agent system that autonomously writes and optimizes extraction prompts for clinical concepts without manual prompt engineering or fine-tuning. Running on a locally hosted ...
  </details>

- **2026-07-14** — Roi Cohen, Yvan Carré, Nick Lechtenbörger et al. — [Knowledgeless Language Models: Suppressing Parametric Recall for Evidence-Grounded Language Modeling](http://arxiv.org/abs/2607.12831v1)
  <details><summary>📄 Abstract</summary>
  Language models encode substantial factual knowledge in their parameters, which can lead to unreliable behavior when this knowledge is outdated, incomplete, or misaligned with the provided context. In this work, we study whether modifying the pretraining signal can systematically shift models away from parametric recall and toward evidence-grounded reasoning. We introduce Knowledge--''Less'' Language Models (KLLMs), a fundamentally different epistemic training paradigm for LLMs, which are pretra...
  </details>

- **2026-07-14** — Hongbo Wang, Huaibo Huang, Jie Cao et al. — [Hallo4D: Multi-Modal Hallucination Mitigation for Consistent Spatio-Temporal Generation](http://arxiv.org/abs/2607.12752v2)
  <details><summary>📄 Abstract</summary>
  While recent advances in 3D generation have enabled impressive visual synthesis, existing methods often rely on 2D diffusion supervision without explicit mechanisms for geometric consistency, leading to spatial hallucinations such as duplicated structures and misaligned geometry. These issues become more severe in 4D generation, where maintaining consistency across viewpoints and temporal evolution introduces additional challenges, including jitter, identity flicker, and structural drift. We pre...
  </details>

- **2026-07-14** — Julius Steiglechner, Lucas Mahler, Gabriele Lohmann — [LLMs Can See the Smoke but not the Fire: Evaluating Abductive Reasoning with Elenchos](http://arxiv.org/abs/2607.12733v1)
  <details><summary>📄 Abstract</summary>
  Large language models (LLMs) excel at pattern recognition and text generation, but their capacity for abductive inference - inferring latent hypotheses that explain observed behavior - remains poorly understood. Here, we introduce Elenchos (named after the Socratic method of cross-examination), a generative evaluation framework that measures abductive reasoning as a structural inverse problem. Given a reference formal system, such as the lambda-calculus, and a potentially mutated counterpart, ag...
  </details>

- **2026-07-14** — Jiahang Wang, Yirong Yang, Yanqing Zhu et al. — [ReflectVLN: Training Vision-Language Navigation Agents with Reflective Reasoning](http://arxiv.org/abs/2607.12680v1)
  <details><summary>📄 Abstract</summary>
  Existing vision-language navigation methods often couple a VLM with waypoint decoders to produce multi-step action plans, but they typically lack an explicit closed-loop mechanism for tracking semantic progress, diagnosing execution failures, and recovering from error accumulation in long-horizon navigation. To address this gap, we propose ReflectVLN, an agentic VLN framework that organizes decision-making through bidirectionally interactive intention and execution agents. The intention agent pe...
  </details>

- **2026-07-14** — Jiho Jun, Jeongwon Woo, Jaemin Song et al. — [MAGE: Color-Invariant and Spatial Knowledge Distillation for Gastric Neoplasm Classification](http://arxiv.org/abs/2607.12663v1)
  <details><summary>📄 Abstract</summary>
  Accurate differentiation between gastric adenoma and carcinoma during endoscopy is critical for clinical decision-making. Yet, this task is highly challenging due to high inter-class similarity and ambiguous boundaries between the two classes. Existing ROI-based classification methods often suffer from detection/segmentation error propagation and loss of surrounding global context. In contrast, full-image classification lacks the necessary spatial focus. Furthermore, we observe that deep neural ...
  </details>

- **2026-07-14** — Raheen Junaid Wani, Smruti R. Sarangi — [Lightweight Multi-Scale Anomaly Detection for Resource-Constrained Edge Devices](http://arxiv.org/abs/2607.12599v1)
  <details><summary>📄 Abstract</summary>
  Time-series anomaly detection is increasingly important in IoT systems, sensor networks, and edge monitoring applications, where models must operate under strict constraints on memory, latency, and power consumption. While recent deep-learning approaches have improved detection accuracy, many remain computationally expensive and often fail to capture subtle anomalies due to limited multi-scale sensitivity. Autoencoders are widely used for anomaly detection because they reconstruct normal pattern...
  </details>

- **2026-07-14** — Mattia Tamiazzo, Simone Milani, Massimo Iuliani et al. — [Explainable-by-Design Audio Deepfake Detection via Wiener-Hopf Linear Prediction](http://arxiv.org/abs/2607.12584v1)
  <details><summary>📄 Abstract</summary>
  The rapid advancement of synthetic speech generation methods has made audio deepfake detection a critical challenge in multimedia forensics. While recent approaches achieve high detection accuracy, they typically rely on black-box architectures that offer limited interpretability and high computational complexity. In this paper, we propose an explainable-by-design audio deepfake detection framework based on Wiener-Hopf linear prediction, processed by a lightweight 2D Convolutional Neural Network...
  </details>

- **2026-07-14** — Martin Uray, Saverio Messineo, Roland Kwitt et al. — [Exploring Zero-Shot Foundation Models for Multivariate Time Series Anomaly Detection](http://arxiv.org/abs/2607.12454v1)
  <details><summary>📄 Abstract</summary>
  Multivariate Time Series Anomaly Detection (MTSAD) is essential for reliability and safety in domains such as industrial process monitoring and financial risk management, yet conventional approaches rely on application-specific models that are costly to train and hard to scale. Foundation Models (FMs), pre-trained on broad data with strong zero-shot generalization, have recently become available for univariate time series forecasting, raising the question of whether they can address MTSAD withou...
  </details>

- **2026-07-14** — A H M Nazmus Sakib, Dipayan Banik, Murtuza Jadliwala — [Trust but Verify? Uncovering the Security Debt of Autonomous Coding Agents](http://arxiv.org/abs/2607.12428v1)
  <details><summary>📄 Abstract</summary>
  The increasing adoption of autonomous coding agents accelerates software development but also introduces scoped security risks within high-impact file paths that can outpace traditional human review capacity. While prior research has primarily evaluated these systems in terms of functional correctness and productivity, this paper presents a large-scale empirical study using the AIDev dataset to systematically characterize security code smells in agent-generated pull requests (PRs). Through a com...
  </details>

- **2026-07-14** — Xiaoning Ren, Yinxing Xue, Lei Ma et al. — [Code-MUE: Measuring Code LLMs' Uncertainty through Execution-based Semantic Interaction Graphs](http://arxiv.org/abs/2607.12273v1)
  <details><summary>📄 Abstract</summary>
  As Code Large Language Models (LLMs) become central to modern software engineering, their inherent stochasticity poses significant real-world risks, where even minor errors can lead to severe functional, security, or safety consequences. Reliable automation, therefore, demands the ability to distinguish between confident, well-supported predictions and stochastic guessing. However, existing uncertainty estimation methods face a critical gap: white and grey-box techniques are often inapplicable t...
  </details>

- **2026-07-14** — Joshua Hill — [Saturation Makes Quantization Error Additive: A Coverage Model with a Certificate](http://arxiv.org/abs/2607.12266v1)
  <details><summary>📄 Abstract</summary>
  Mixed-precision quantization must decide which parts of a model to keep at higher precision. A common premise, shared by sensitivity-based methods such as HAWQ and CoopQ, is that the loss from quantizing a set of layers can be reconstructed from per-layer or pairwise sensitivities measured in isolation. We test this premise at the 4-bit weight-and-activation precisions now being deployed, treating the change in loss $f(S)$ from quantizing a layer set $S$ as a set function on the Boolean cube and...
  </details>

- **2026-07-13** — Mary Phuong, Erik Jenner, Laurent Simon et al. — [GDM AI Control Roadmap](http://arxiv.org/abs/2607.13087v1)
  <details><summary>📄 Abstract</summary>
  AI agents are rapidly accelerating work at frontier AI companies, helping with AI R&D, cyber-defence, and advancing scientific discoveries. As these agents become more tightly integrated into our systems, unlocking their full potential requires rethinking how we do security. We should not assume that AI agents are always perfectly aligned, but should instead build in multiple layers of defence. We present the GDM AI Control Roadmap (v0.1) -- a first-of-its-kind blueprint for internal security ag...
  </details>

- **2026-07-13** — Su Wang, Pin Qian, Yifan Lin et al. — [Phantom Guardrails: When Self-Improving Agent Harnesses Fix Failures That Never Happened](http://arxiv.org/abs/2607.13083v1)
  <details><summary>📄 Abstract</summary>
  Self-improving AI agents are designed to learn from their mistakes. We show they can also hallucinate mistakes that never happened. We study this failure mode in automated harness optimization, where an LLM-based proposer edits an agent's scaffold, including prompts, parsers, filters, validators and guardrails, to eliminate observed failures. But this process rarely asks first: was there a real failure to fix? We introduce the Counterfactual Fabrication Lab, a deterministic micro-lab where the c...
  </details>

- **2026-07-13** — Minh Hua, Rita Raley — [Optimization Is Not All You Need](http://arxiv.org/abs/2607.11977v2)
  <details><summary>📄 Abstract</summary>
  In 2019, OpenAI released two million GPT-2 outputs-ungrammatical, half broken-to aid the detection of machine-generated text. The alignment that produced their more fluent successors is usually regarded as an engineering achievement; we read it instead as the newest expression of optimization culture: the conviction, older than the technology, that measurable improvement along predefined axes exhausts the question of value. Tracing that conviction through the stack-pretraining, decoding, prefere...
  </details>

- **2026-07-13** — Boda Xiao, Xiran Xu, Songyi Li et al. — [Beyond Parallel Tracking: Interactive Multi-Feature Fusion Drives Semantic Reconstruction from Non-invasive Brain Recordings](http://arxiv.org/abs/2607.12071v1)
  <details><summary>📄 Abstract</summary>
  Continuous semantic reconstruction from non-invasive neural recordings remains limited by the representational mismatch between semantic feature spaces and neural coding patterns, which severely impedes cross-modal alignment between high-noise neural signals and target semantic features. Prior semantic decoders have predominantly relied on static lexical representations or dynamic contextualized representations in isolation. This single-dimension approach inevitably leads to severe information l...
  </details>

- **2026-07-13** — Sam Cheng-Tse Huang, Matthew R. Buckley, Justin I. Read et al. — [A Universal Distribution of Dark Matter in Milky Way-like galaxies and How to Infer It](http://arxiv.org/abs/2607.12008v1)
  <details><summary>📄 Abstract</summary>
  The phase-space density of dark matter within the Milky Way is a key quantity that encodes information about the nature of the dark sector. The local phase-space density is also required to properly interpret the results of dark matter direct detection experiments. However, there are at present few observational constraints. In this paper, we show that a simple coordinate transformation reveals a near-universal DM phase-space distribution function among three independent suites of cosmological s...
  </details>

- **2026-07-13** — Yixuan Xiao, Cheng-Wei Lin, Xin Wang et al. — [Evidence Subspace Projection: Measuring How Much Evidence Explains Deepfake Detection in Self-Supervised Speech Models](http://arxiv.org/abs/2607.11538v1)
  <details><summary>📄 Abstract</summary>
  Self-supervised learning (SSL) models are widely used as feature extractors for state-of-the-art audio deepfake detection, but it remains unclear how to directly and quantitatively connect what SSL models capture to detection decisions. To address this gap, we propose Evidence Subspace Projection, a method that represents both evidence factors (e.g., attack category, codec, gender, transmission) and authenticity labels in a shared space constructed from SSL models' neuron activation patterns. By...
  </details>

- **2026-07-13** — Ahmed M. Elmisery — [Graph-Based Structural Evaluation of LLM-Translated Adversary Emulation Procedures](http://arxiv.org/abs/2607.11517v1)
  <details><summary>📄 Abstract</summary>
  Adversary emulation plans describe multi-step attacker procedures using MITRE ATT&CK techniques, privilege requirements, and observable telemetry. Translating them across operating systems supports cross-platform defender evaluation, and large language models (LLMs) can automate this task. However, a translation may only rename tools while retaining source-platform logic, giving defenders little target-platform coverage. Binary scoring can overestimate fidelity because it measures countable feat...
  </details>

- **2026-07-13** — Ananya Acharya, Trenton Goyette, Masoud Ataei et al. — [Capture, Shield, or Neutralize: Engagement-Aware Pursuit-Evasion](http://arxiv.org/abs/2607.10986v1)
  <details><summary>📄 Abstract</summary>
  This paper introduces a hierarchical control architecture for multi-agent adversarial environments, decoupling strategic task planning from rigorous safety assurance. The system formulates pursuit-evasion as a zero-sum receding-horizon game, solved via an iterative minimax \acl{mpc} scheme. This allows pursuers to anticipate and block evader trajectories using transverse velocity penalties rather than relying on reactive heuristic formations. To guarantee collision-free operation without comprom...
  </details>

- **2026-07-13** — Markos Markakis, Tim Kraska — [AutoSLO: Practical Latency SLOs on Cloud Data Warehouses -- Extended Version](http://arxiv.org/abs/2607.11770v1)
  <details><summary>📄 Abstract</summary>
  Modern cloud data warehouses decouple compute from storage, making it easy for organizations to access the same underlying data with multiple compute clusters. This flexibility is often used for performance isolation among diverse workloads, so that each workload meets its latency service-level objective (SLO) more reliably. For example, interactive dashboards, ad hoc analysis, and batch jobs can each run on separate clusters. However, this dedicated-cluster approach requires each compute cluste...
  </details>

- **2026-07-13** — Yilong Yang, Jianxin Tian, Shengchuan Zhang et al. — [GFR-SAM: Training-Free Referring Camouflaged Object Segmentation via Cross-Image Prompting](http://arxiv.org/abs/2607.11732v1)
  <details><summary>📄 Abstract</summary>
  Referring Camouflaged Object Detection (Ref-COD) requires segmenting hidden targets guided by reference cues. While supervised methods are annotation-heavy and training-free approaches via sparse point-prompting are sensitive to localization errors, we propose GFR-SAM, a robust three-stage training-free framework. GFR-SAM shifts the paradigm from fragile point-matching to a "Generate-Filter-Refine" pipeline. First, we introduce In-Context Exemplar-guided Segmentation, empowering SAM3 with cross-...
  </details>

- **2026-07-13** — Huan Zhu — [Think Through a Bottleneck: Hourglass Reasoning for Rigorous Induction](http://arxiv.org/abs/2607.11696v1)
  <details><summary>📄 Abstract</summary>
  Self-refinement often fails to strengthen few-shot inductive reasoning in large language models. Prompting a model to explicitly state its inferred rule does little on its own. What actually matters is a structurally enforced isolation between reasoning stages, so that information can only pass between them as a compressed symbolic state.   We introduce \textbf{Hourglass reasoning}, which enforces strict context isolation between reasoning stages. The frozen LLM acts as a meta-constructor, build...
  </details>

- **2026-07-13** — Hari Prasad — [Auditing the Risk Claims of Distributional Reinforcement Learning](http://arxiv.org/abs/2607.11607v1)
  <details><summary>📄 Abstract</summary>
  Distributional reinforcement learning agents learn full return distributions that are increasingly read at face value: for interpretability, risk-sensitive control, and safety monitoring. We ask a question theory anticipates but that has not been measured directly: are the risk claims of a trained distributional agent true? Our audit combines a decision-relevant screening metric (the excess Wasserstein gap between the top two actions, which equals the mass by which first-order stochastic dominan...
  </details>

- **2026-07-13** — Yuliang Liu, Zhang Li, Ziyang Zhang et al. — [MonkeyOCRv2: A Visual-Text Foundation Model for Document AI](http://arxiv.org/abs/2607.11562v1)
  <details><summary>📄 Abstract</summary>
  Mainstream visual encoders are pretrained on natural images and cannot be effectively applied to document images without document-oriented adaptation, as dense text and fine-grained character strokes demand character-level visual perception. We present MonkeyOCRv2, a visual-text pretrained model for document AI. First, we construct MonkeyDoc v2, to our knowledge the largest document-image pretraining corpus, comprising 113 million images spanning 17 languages. Second, we propose a pretraining st...
  </details>

- **2026-07-13** — Sridhar Mahadevan — [Agentic Skill Optimization over Lie Algebroids](http://arxiv.org/abs/2607.11493v1)
  <details><summary>📄 Abstract</summary>
  Agentic systems increasingly improve themselves by editing skills: prompts, rubrics, plans, tool contracts, examples, validators, and traces. Skill edits are not independent coordinates in a vector space: they are local repairs to structured artifacts whose effects are observed only after rollout, validation, and critique. Distinct edits can have the same immediate visible effect while differing in routing context, template state, guardrail scope, or future composability. The order of edits can ...
  </details>

- **2026-07-13** — Tengjiao Liu — [Heterogeneous Agent Cohorts for Safe Open-Ended Exploration with Runtime Constraint Memory](http://arxiv.org/abs/2607.11226v1)
  <details><summary>📄 Abstract</summary>
  LLM agents today are caught in an awkward bind. Lock them down with static safety instructions and they rarely venture beyond the obvious; give them free reign with tools and multi-agent debate, and safety violations quickly follow. Rather than forcing a single model to juggle both creativity and caution, we separate the concerns across specialized roles. A Disrupter generates unconventional proposals, a Validator enforces hard runtime checks at the tool gateway, and a Broker pulls in distant bu...
  </details>

- **2026-07-13** — Prashant Devadiga,  Abhishek, Adithya Mishra et al. — [A Formal Hierarchical Architecture for Agentic Orchestration with Stack-Based Execution and Lazy Discovery](http://arxiv.org/abs/2607.11138v1)
  <details><summary>📄 Abstract</summary>
  The rapid expansion of capabilities in Large Language Model (LLM) agents has exposed a critical architectural bottleneck: when agents are given access to a flat, monolithic registry of tools, the model must evaluate hundreds or thousands of options simultaneously. This leads to decision-space explosion, context window saturation, and degraded routing accuracy. To address these limitations, this paper presents a hierarchical, skill-based architecture for agentic orchestration. Capabilities are or...
  </details>

- **2026-07-13** — Sara Yakoubi, Ikram Khalfallah, Kenza Khelkhal et al. — [FAD-SA-GRU: Enhancing Hate Speech Detection in Algerian Dialect Through Feature-Augmented Self-Attention GRU Networks](http://arxiv.org/abs/2607.11279v1)
  <details><summary>📄 Abstract</summary>
  The widespread adoption of social media platforms has transformed online communication by enabling users to exchange information and opinions instantly. However, these platforms have also facilitated the dissemination of abusive and hateful content, posing major social, psychological, and ethical challenges. Hate speech can incite discrimination, harassment, and violence against individuals or communities based on attributes such as ethnicity, religion, gender, nationality, or political affiliat...
  </details>

- **2026-07-13** — Kaixin Ma, Di Feng, Alexander Metz et al. — [MM-ToolSandBox: A Unified Framework for Evaluating Visual Tool-Calling Agents](http://arxiv.org/abs/2607.11818v1)
  <details><summary>📄 Abstract</summary>
  We introduce MM-ToolSandBox, a benchmark and evaluation framework for visually grounded tool-calling agents. The framework provides a stateful execution environment spanning 500+ tools across 16 application domains, supporting multi-image, multi-turn tasks where agents must ground progressively arriving visual inputs into executable tool calls while handling realistic conversational phenomena (goal revisions, error corrections, state mutations). An automated scenario generation pipeline produces...
  </details>

- **2026-07-13** — Yi Tang Soon, Jun-Wei Hsieh — [Confidence Scores in Open-Vocabulary Detection Are a Biased Mixture of Scale and Semantics](http://arxiv.org/abs/2607.10993v1)
  <details><summary>📄 Abstract</summary>
  Foundation models such as CLIP have enabled open-vocabulary object detectors that generalise to novel categories via vision-language similarity. However, the confidence scores these detectors produce are not reliable localization probability estimates: they conflate visual scale and semantic query specificity with the true detection signal. Through controlled experiments on COCO across three foundation-model-based detectors (GroundingDINO, OWL-ViT, YOLO-World), with the scale-bias finding furthe...
  </details>

- **2026-07-12** — Yuan Gao, Jiangyi Yang, Yao Zhao et al. — [Auditing Belief-Conditioned LLM Agents in Hidden-Information Social Deduction Games](http://arxiv.org/abs/2607.10814v1)
  <details><summary>📄 Abstract</summary>
  Evaluating LLM agents in hidden-information multi-agent settings is hard: final outcomes are high-variance and rarely reveal why an agent decided as it did. We study this in a 9-player Werewolf environment where agents act under strict, code-level information isolation, and we build an auditable framework that maintains an external belief state over hidden roles, logs belief updates and belief-action deviations as structured evidence, and supports a defensive offline improvement loop that review...
  </details>

- **2026-07-12** — Lin Zhang — [LLM-Enhanced Dynamic Financial Knowledge Graphs for Cross-Entity Signal Propagation and alpha discovery](http://arxiv.org/abs/2607.10932v1)
  <details><summary>📄 Abstract</summary>
  Financial information rarely affects a single company in isolation. Earnings surprises, capital expenditure changes, supply constraints, and guidance revisions can propagate through networks of suppliers, customers, competitors, and technology ecosystems. Traditional financial NLP primarily measures document-level sentiment for the directly mentioned company and often ignores cross-entity information diffusion.   This paper develops an LLM-based financial measurement and signal propagation frame...
  </details>

- **2026-07-12** — Keqin Peng, Chen Li, Yuanxin Ouyang et al. — [Diagnosing and Mitigating Thinking Collapse in On-Policy Self-Distillation](http://arxiv.org/abs/2607.10805v1)
  <details><summary>📄 Abstract</summary>
  On-Policy Self-Distillation (OPSD) has emerged as a crucial paradigm for enhancing and aligning Large Language Models (LLMs). However, in complex reasoning tasks, OPSD paradoxically degrades downstream performance. In this paper, we systematically investigate this pathology and identify a severe optimization trap we define as \textbf{Thinking Collapse} -- a sharp decline in the model's native intermediate reasoning behavior, measured by epistemic-token density (ET per 1k). Through entropy-based ...
  </details>

- **2026-07-12** — Dylan Xinming Hou, Juntian Zhang, Xu Gu et al. — [Detecting AI-Generated Video: A Vision-Language Dual-View Survey](http://arxiv.org/abs/2607.10787v1)
  <details><summary>📄 Abstract</summary>
  The evolving realism of AI-generated Videos (AIGC-V) is rapidly rendering traditional artifact-centric detection insufficient, necessitating a paradigm shift from low-level inspection to high-level semantic verification. This paper presents a comprehensive survey of AIGC-V detection, reframing the task as Factual Fidelity Verification, which asks whether the events, entities, and physical processes depicted in a video are consistent with real-world facts. To systematize this rapidly evolving fie...
  </details>

- **2026-07-12** — Sriram Selvam, Anneswa Ghosh — [Eval-Pair Matrix: Answer-Paired Meta-Evaluation of LLM Judges for Grounded RAG](http://arxiv.org/abs/2607.10626v1)
  <details><summary>📄 Abstract</summary>
  LLM-as-a-judge evaluation is widely used for retrieval-augmented generation (RAG), but reusing the same model family as both generator and judge makes self-leniency difficult to identify. We introduce Eval-Pair Matrix, a controlled meta evaluation protocol for source-grounded RAG. Starting from GaRAGe questions and grounding passages, we induce one hidden answer-causal contradiction per record, generate answers from perturbed passages with GPT, Grok, and Gemini models, and then use the same mode...
  </details>

- **2026-07-12** — Zheng Pei, Mingwei Liu, Zhenxi Chen et al. — [WebDesignIter: Co-Evolving Design Knowledge for Repository-Level Front-End Code Generation](http://arxiv.org/abs/2607.10621v1)
  <details><summary>📄 Abstract</summary>
  Front-end development accumulates change after change at the repository level, weaving complex cross-file dependencies that current LLM coding agents tuned for single-shot tasks cannot reliably track across multiple iterations, leading to functional regressions and code that resists maintenance. We argue the missing piece is design knowledge: architectural principles, module responsibilities, and structural constraints that developers lean on to keep code readable, maintainable, and evolvable as...
  </details>


### 📂 alignment
*对齐与安全约束 / Alignment & Safety Constraints* — 57 papers

- **2026-07-15** — Sai Srikanth Madugula, Peplluis Esteva de la Rosa, Daya Shankar — [The Dynamic Verifiable Multi-Agent Human Agentic Loyalty Loop (DVM-HALL) Model and the Net Human-Agent Score (NHAS) in Autonomous Commerce](http://arxiv.org/abs/2607.13998v1)
  <details><summary>📄 Abstract</summary>
  The rapid proliferation of Agentic Artificial Intelligence fundamentally disrupts traditional customer loyalty paradigms. As AI evolves from passive recommendation algorithms to autonomous, goal-directed agents capable of executing purchasing decisions, the conventional understanding of consumer-brand relationships requires a structural reevaluation. By synthesizing extant literature across human-machine teaming, consumer decision-making, and algorithmic trust dynamics, we demonstrate that tradi...
  </details>

- **2026-07-15** — Zhihao Xie, Junfeng Wu, Xinting Hu et al. — [VideoRAE: Taming Video Foundation Models for Generative Modeling via Representation Autoencoders](http://arxiv.org/abs/2607.14088v1)
  <details><summary>📄 Abstract</summary>
  Video generative models commonly rely on latent spaces learned by 3D Variational Autoencoders (3D-VAEs). However, conventional 3D-VAEs are mainly optimized for pixel-level reconstruction, which can limit the semantic and spatio-temporal structure captured by their latents. Meanwhile, Video Foundation Models (VFMs) such as V-JEPA 2 and VideoMAEv2 show strong video understanding capabilities, yet whether their frozen representations can be transformed into compact, reconstruction-capable, and gene...
  </details>

- **2026-07-15** — Shunbao Li, Zhipeng Yuan, Amoako Ofori et al. — [Pezego-HITL: A policy-grounded large language model architecture for agricultural extension in Ghana](http://arxiv.org/abs/2607.13934v1)
  <details><summary>📄 Abstract</summary>
  Large language models are increasingly deployed in agricultural decision-support settings, yet high-stakes crop protection in smallholder agriculture requires more than output-quality benchmarks. Over a two-year design and evaluation programme, we formalise policy-constrained large language model assessment as an adaptive compute allocation problem that jointly captures safety compliance, helpfulness, operational latency, and expert supervision workload. We introduce P-EVAL (Policy-grounded Expe...
  </details>

- **2026-07-15** — Cheng Tang, Junzhi Ning, Min Cen et al. — [SIVA-RL: Sensitivity-Invariance Visual Alignment for Multimodal Reinforcement Learning](http://arxiv.org/abs/2607.13931v1)
  <details><summary>📄 Abstract</summary>
  Reinforcement learning with verifiable rewards (RLVR) drives multimodal reasoning, but answer-level correctness does not guarantee that a vision-language model grounds its predictions in visual evidence. Existing visual-intervention methods contrast policy behavior on original and modified images, yet assign supervision by the type of intervention rather than its observed effect. This assumption fails: identical operators produce heterogeneous outcomes across samples. We propose SIVA-RL, a Sensi...
  </details>

- **2026-07-15** — Zhixiao Zheng, Zheren Fu, Zhiyuan Yao et al. — [Groc-PO: Grounded Context Preference Optimization for Truthful Multimodal LLMs](http://arxiv.org/abs/2607.13712v1)
  <details><summary>📄 Abstract</summary>
  Despite the rapid progress of Multimodal Large Language Models (MLLMs), they still suffer from untruthfulness issues, such as visual hallucinations, content fabrication, and unfaithful reasoning, which substantially undermine their faithfulness and practical utility. Alignment methods based on human preference, such as Direct Preference Optimization (DPO), have been widely adopted to address these issues. However, multimodal reasoning errors often propagate across stages, and final-answer errors...
  </details>

- **2026-07-15** — Zehan Liu, Yage He, Xianwu Gong — [WAVE-Stereo: Warp-Aligned Volume Encoding for Stereo Matching](http://arxiv.org/abs/2607.13674v1)
  <details><summary>📄 Abstract</summary>
  Existing iterative stereo matching methods primarily adopt two types of correspondence representation: explicit matching search via correlation volumes and local residual refinement via warped features, yet the two remain separately modeled. We propose WAVE-Stereo, built on a core insight: correlation volumes and feature warping provide complementary matching cues. \textbf{GeoWarp Correspondence Encoder (GWCE)} encodes matching search, residual alignment, and disparity prior in parallel at the C...
  </details>

- **2026-07-15** — Yongqiang Chen, Guangyi Chen, Yuewen Sun et al. — [Analogical Deep Research: Retrieving and Integrating Historical Analogies for Foresight Analysis](http://arxiv.org/abs/2607.13602v1)
  <details><summary>📄 Abstract</summary>
  Systematic comparisons between current situations and structurally similar past events in the historical, i.e., historical analogies, is among the most powerful tools for foresight analysis. In this work, we present a new task called Analogical Deep Research (ADR) to Large Language Model (LLM) agents and construct the first ADR benchmark ADR-bench to study whether LLM agents are able to find and leverage historical analogies when doing foresight analysis. Our investigation reveals a key obstacle...
  </details>

- **2026-07-15** — Yuan Xiao, Can Wang, Xiangyu Kong et al. — [ThinkBLOX: 3D Indoor Scene Generation with Progressive Reasoning](http://arxiv.org/abs/2607.13539v1)
  <details><summary>📄 Abstract</summary>
  While traditional graphics methods often synthesize 3D indoor scenes autoregressively or hierarchically, recent vision-language model (VLM)-based generators predominantly adopt a one-shot paradigm where the full layout is planned at once. This one-shot approach often requires global re-optimization or complete reconstruction during interactive editing (e.g., inserting or moving objects) and can lead to physically or semantically poorly organized arrangements. To address these challenges, we prop...
  </details>

- **2026-07-15** — Shuzhen Li, Yifan Zhang, Jiacheng Guo et al. — [DeepLoop: Depth Scaling for Looped Transformers](http://arxiv.org/abs/2607.13491v1)
  <details><summary>📄 Abstract</summary>
  Looped Transformers scale sequential computation by applying a compact stack of physical blocks for multiple rounds, increasing unrolled depth without increasing stored parameters. This reuse changes the residual-scaling problem: in an untied Transformer, each residual branch receives and applies its own parameter update, whereas in a looped Transformer one shared update aggregates gradients from repeated visits and is read back by those same visits in the next linearized forward pass. We formal...
  </details>

- **2026-07-15** — Xinhao Cai, Yixuan Sun, Minghang Zheng et al. — [Music-to-Dance Generation via Atomic Movements](http://arxiv.org/abs/2607.13978v1)
  <details><summary>📄 Abstract</summary>
  Music-driven dance generation aims to produce human motion that is both rhythmically synchronized and semantically consistent with music. While recent neural approaches have achieved impressive visual realism, they typically model motion as a continuous signal and neglect its compositional nature, making generated dances structurally incoherent and difficult to control. In this work, we introduce a structure-aware framework that models choreography as a sequence of atomic movements-semantically ...
  </details>

- **2026-07-15** — Chenyang Zhao, Wei Lin, Antoni B. Chan et al. — [Fine-grained CLIP fine-tuning with self-annotated region alignment](http://arxiv.org/abs/2607.13661v1)
  <details><summary>📄 Abstract</summary>
  Contrastive Language-Image Pre-training (CLIP) has been shown to have limitations in its fine-grained dense feature representation, due to its pre-training focusing on matching the whole image to a text description. Considering the large data and computational burden in pre-training a vision-language model from scratch, a series of works aim to enhance the fine-grained ability of CLIP through a fine-tuning scheme. However, existing works suffer from a variety of limitations: additional region an...
  </details>

- **2026-07-15** — Celeste Veronese, Edoardo Zorzi, Daniele Meli et al. — [Explaining Reinforcement Learning Agents via Inductive Logic Programming](http://arxiv.org/abs/2607.13655v1)
  <details><summary>📄 Abstract</summary>
  Explainable Reinforcement Learning (XRL) seeks to make Reinforcement Learning (RL) policies more transparent and interpretable, a key requirement in safety-critical and human-centric scenarios. However, it is mostly based on user studies, thus targeting the needs of a specific audience and lacking shared evaluation metrics. On the other hand, logic-based approaches within eXplainable Artificial Intelligence (XAI) provide compact, human-readable abstractions of decision-making. However, the syste...
  </details>

- **2026-07-15** — Ayan Igali, Pakizar Shamoi — [Beyond Color Geometry: Evaluating Human-Like Color Representations in Vision Models](http://arxiv.org/abs/2607.13647v1)
  <details><summary>📄 Abstract</summary>
  Do vision models see colors the way humans do? Existing evaluations of color representations usually compare them with geometric spaces such as CIELAB or with discrete color labels. These references capture perceptual distance or category membership, but not the graded way in which people organize colors. We evaluate color grounding against a fuzzy perceptual model with 86 graded categories fitted to human survey data. The framework can be applied to any image encoder and measures three compleme...
  </details>

- **2026-07-15** — Hao Li, Han Fang, Zixin Pan et al. — [GeoAnchor: Collaborative Reasoning via Latent Decomposition for 3D Spatial Understanding](http://arxiv.org/abs/2607.13454v1)
  <details><summary>📄 Abstract</summary>
  Although multimodal large language models (MLLMs) have achieved remarkable progress, understanding 3D spatial relationships from 2D images remains a critical challenge. Existing methods primarily rely on symbolic text tokens, which inherently lack the fidelity to represent continuous geometric information. While recent methods use latent representations to enhance reasoning, relying on a single latent type cannot adapt to the diversity of spatial tasks, leading to misalignment in complex geometr...
  </details>

- **2026-07-15** — Xi Yang, Guodong Liu, Chuqin Li et al. — [Exploring Post-Training Alignment of Small Language Models for Biomedical Data-to-Text Generation: A Case Study of Medication Leaflet](http://arxiv.org/abs/2607.13430v1)
  <details><summary>📄 Abstract</summary>
  Translating complex biomedical data into patient-friendly narratives is central to modern biomedical informatics. This study presents a comparative analysis of training small language models (SLMs) in specialized biomedical datato-text generation tasks. We explore widely adopted post-training methods including supervised fine-tuning (SFT), direct preference optimization (DPO), odds ratio preference optimization (ORPO), and group relative policy optimization (GRPO) with Qwen-based SLMs on a medic...
  </details>

- **2026-07-15** — Dwip Dalal, Shivansh Patel, Chahit Jain et al. — [Generalizable VLA Finetuning via Representation Anchoring and Language-Action Alignment](http://arxiv.org/abs/2607.13429v1)
  <details><summary>📄 Abstract</summary>
  Finetuning a pretrained vision-language model (VLM) on robot demonstrations via behavior cloning (BC) has become the standard recipe for vision-language-action (VLA) policies. However, BC finetuning progressively overwrites the pretrained representations that support visual and semantic generalization. Co-training on web image-text data, a common remedy, does not prevent this; it applies language and action losses to separate observations, leaving VLAs with language-action misalignment that stan...
  </details>

- **2026-07-14** — Jiaying Lin, Seongho Son, Nam Phuong Tran et al. — [Meta-Learning Preferences for Multilingual LLM Alignment](http://arxiv.org/abs/2607.13315v1)
  <details><summary>📄 Abstract</summary>
  Unequal availability of human preference data across languages poses a significant challenge for aligning large language models in multilingual settings. To address the lack of sufficient data in low-resource language alignment, we propose a meta-learning framework for Reinforcement Learning from Human Feedback and Direct Preference Optimization. By leveraging preference data from other languages, our framework learns a transferable initialization that enables effective adaptation to a target la...
  </details>

- **2026-07-14** — Yuhong Fu, Weixing Zhang, Bowen Jiang et al. — [Can LLMs Learn and Apply Multi-Level Modelling Semantics? A First Empirical Study](http://arxiv.org/abs/2607.13257v1)
  <details><summary>📄 Abstract</summary>
  Industry 5.0 emphasises human-centric industrial system design, placing additional demands on modelling tools. Multi-level modelling (MLM) can directly represent three or more abstraction levels, but this comes at the cost of more complex semantic constraints that model correctness depends on. Large Language Models (LLMs) have been increasingly studied in model-driven engineering, but this evidence rests entirely on two-level modelling tasks, and whether it generalises to MLM, whose semantics di...
  </details>

- **2026-07-14** — Jonas Ehrhardt, René Heesch, Oliver Niggemann — [Knowledge- and Gradient-Guided Reinforcement Learning for Parametrized Action Markov Decision Processes](http://arxiv.org/abs/2607.12924v2)
  <details><summary>📄 Abstract</summary>
  In this paper, we study Reinforcement Learning in Parametrized Action Markov Decision Processes (PAMDP), where each decision consists of a symbolic action and numerical parameters. In such settings Reinforcement Learning algorithms typically determine parameters with one-shot estimators, which makes their training sample inefficient. Though in most PAMDP environments explicit but incomplete knowledge (e.g., rules, safety constraints, or expert heuristics) is available, it is rarely directly used...
  </details>

- **2026-07-14** — Hanhua Hong, Yizhi Li, Jiaoyan Chen et al. — [Can LLMs Write Reliable Rubrics? A Meta-Evaluation for Experiment Reproduction](http://arxiv.org/abs/2607.12835v1)
  <details><summary>📄 Abstract</summary>
  Rubric-based evaluation is a promising approach for assessing open-ended outputs from LLM-based research agents, particularly in paper reproduction, where direct paper-to-repository comparison is prone to hallucination. However, constructing paper-specific rubrics requires substantial expert effort, limiting the scalability of benchmarks such as PaperBench. In this work, we present, to our knowledge, the first systematic meta-evaluation of LLM-generated rubrics for paper reproduction. We reformu...
  </details>

- **2026-07-14** — Taizo Suzuki, Soma Yokota, Masaki Onuki — [Spatially-Aligned Chroma from Luma Prediction for Lossless JPEG XS Raw Image Compression](http://arxiv.org/abs/2607.12636v1)
  <details><summary>📄 Abstract</summary>
  This study proposes a Chroma from Luma (CfL)-enhanced Star-Tetrix transform (STT), referred to as CfL-STT, for improving raw image compression in JPEG XS. The proposed CfL-STT integrates CfL prediction into the STT to predict chroma components from the luma component in CFA-sampled raw images. Unlike conventional CfL prediction designed for full-color images, the proposed method employs spatially aligned luma samples obtained via linear interpolation along the horizontal and vertical directions ...
  </details>

- **2026-07-14** — Mao Chen, Xiangkai Zhang, Zhiyong Liu et al. — [More Than Where You Are: Learning Semantics, Structure, and Geometry from Cross-View Localization](http://arxiv.org/abs/2607.12429v1)
  <details><summary>📄 Abstract</summary>
  Consistent cross-view understanding under extreme viewpoint changes is essential for spatial intelligence, as it enables models to recognize the same scene across extreme viewpoint gaps. Cross-view localization naturally provides a promising pathway toward this ability, as it requires a model to align ground-view imagery with geo-referenced satellite-view imagery despite drastic appearance changes to estimate camera poses. Recent visual foundation models have made this long-standing localization...
  </details>

- **2026-07-14** — Kaiwen Zheng, Junchen Fu, Wenhao Deng et al. — [Do We Really Need Multimodal Emotion Language Models Larger Than 1B Parameters?](http://arxiv.org/abs/2607.12787v1)
  <details><summary>📄 Abstract</summary>
  Recent advances in multimodal large language models (MLLMs) have significantly improved the performance of multimodal emotion recognition (MER) and enabled interpretable description generation by jointly modeling video, audio, and language, etc. However, these performance improvements are often accompanied by an increase in model parameter size (e.g, at least 7B), which simultaneously incurs high computational costs and reduces inference efficiency, thereby hindering real-time deployment on reso...
  </details>

- **2026-07-14** — Lin Peng, Cong Wan, Zeyu Guo et al. — [CoRe: A Comprehensive Framework for Cross-Image Comparative Reasoning in Vision-Language Models](http://arxiv.org/abs/2607.12786v1)
  <details><summary>📄 Abstract</summary>
  Cross-image comparative reasoning remains challenging for vision-language models (VLMs), especially when correct prediction requires fine-grained attribute grounding and globally consistent reasoning. We present CoRe, a unified framework for this problem. CoRe includes: (i) CoRe-20K, a large-scale triplet-based training set automatically constructed from structured visual metadata through a multi-expert collaborative pipeline, covering counting, depth, distance, and spatial relations; (ii) TriSR...
  </details>

- **2026-07-14** — Wei Liu, Weisong Sun, Tingting Xu et al. — [Understanding before Naming! Enhancing LLM-based Method Name Prediction with Code Summarization](http://arxiv.org/abs/2607.12467v1)
  <details><summary>📄 Abstract</summary>
  Method names are critical to software quality, affecting code comprehensibility, maintainability, and developer collaboration. However, manually designing meaningful method names is challenging. Method Name Prediction (MNP), which automatically generates method names from code snippets, has recently attracted attention. Although large language models (LLMs) show promising performance for MNP, two challenges remain. First, existing evaluations mainly rely on token similarity metrics, which often ...
  </details>

- **2026-07-13** — Mohammad Amin Samadi, Pedro Martins De Bastos, Jaeyoon Choi et al. — [TRAIL: A Platform for Configurable Human--AI Teaming Experiments](http://arxiv.org/abs/2607.12180v1)
  <details><summary>📄 Abstract</summary>
  An AI teammate's design properties (personality, communication style, when it speaks) can shape a team's trust, coordination, and decisions. Studying this rigorously demands infrastructure no existing tool provides: reproducible configuration of an AI teammate embedded in instrumented, real-time collaboration sustained over time. We present the Team Research and AI Integration Lab (TRAIL), a web platform that makes the AI teammate a configurable, reproducible design object, pairing a Big Five pe...
  </details>

- **2026-07-13** — Gustavo H. Santos, Aline Viana, Thiago H Silva — [CityBehavEx: A Scalable and Empirically Validated LLM-Assisted Urban Simulation Platform](http://arxiv.org/abs/2607.12086v1)
  <details><summary>📄 Abstract</summary>
  Recent LLM-based multi-agent urban simulators can generate semantically rich city routines, but they remain costly to scale and are often weakly validated against empirical mobility patterns. We present CityBehavEx, an interactive LLM-assisted urban simulation platform that scales to city-size populations, exposes agent behavior for inspection, supports empirical validation, and generates mobility patterns that better match real-world spatial, temporal, and semantic distributions. Instead of inv...
  </details>

- **2026-07-13** — Niranjan Kumar M, Balaji Nagarajan, Karthik Nair et al. — [Operationalising Multi-Dimensional Evaluation for Conversational Agents: A Scalable, Governed Pipeline with Selective Re-evaluation and Model Benchmarking](http://arxiv.org/abs/2607.12085v1)
  <details><summary>📄 Abstract</summary>
  Evaluating retail conversational agents requires methods beyond lexical-overlap metrics to assess intent alignment, factuality, helpfulness, clarity, tone, and overall response quality. Although LLM-as-a-judge methods provide scalable alternatives to human evaluation, production deployment introduces challenges in governance, reproducibility, cost, schema consistency, traceability, and reliability. We present GenAI Evaluation, a governed, configuration-driven pipeline for large-scale evaluation ...
  </details>

- **2026-07-13** — Runhui Huang, Qihui Zhang, Zhe Liu et al. — [Read It Back: Pretrained MLLMs Are Zero-Shot Reward Models for Text-to-Image Generation](http://arxiv.org/abs/2607.11886v1)
  <details><summary>📄 Abstract</summary>
  In this paper, we propose SpectraReward, a training-free reward function that turns pretrained MLLMs into off-the-shelf reward models for image-generation reinforcement learning. Instead of asking the MLLM to judge a generated image or answer decomposed verification questions, SpectraReward measures how well the original prompt can be recovered from the generated image through a single image-conditioned, teacher-forced forward pass. We use the average image-conditioned prompt log-likelihood as t...
  </details>

- **2026-07-13** — Landon Liu, Mary Kelly, Alan Tsang — [Forgetting Our Way to Shared Meaning: Effects of Forgetting on Conceptual Alignment in a Non-Partnership Coordination Game](http://arxiv.org/abs/2607.11787v1)
  <details><summary>📄 Abstract</summary>
  Shared meaning in language requires people to learn and agree on categories. We ask how characteristics of agents' memories change the emergence and evolution of shared meaning. Without a coordination game, models of conceptual semantics cannot explain how shared meaning emerges and changes in groups of people; however, existing games assume that players share payoffs in a partnership setting. We model conceptual alignment as a non-partnership game and illustrate differences in actual and percei...
  </details>

- **2026-07-13** — Elmira Salari, Hazem Amamou, José Victor de Souza et al. — [How Temperature Shapes Ideological Discourse in Retrieval-Augmented Generation?](http://arxiv.org/abs/2607.11783v1)
  <details><summary>📄 Abstract</summary>
  Retrieval-Augmented Generation (RAG) has been increasingly adopted to reduce hallucinations and strengthen the factual grounding of large language models (LLMs). While robustness to errors in the retrieval process has been explored, the impact of ideological bias on LLM outputs has been overlooked. For instance, if the retrieved material contains ideological positions, the RAG may transmit, amplify, or suppress such ideological discourses in its outputs. In this study, we address this issue by e...
  </details>

- **2026-07-13** — Daocheng Fu, Rong Wu, Yu Yang et al. — [Proxy Exploration and Reusable Guidance: A Modular LLM Post-Training Paradigm via Proxy-Guided Update Signals](http://arxiv.org/abs/2607.11505v1)
  <details><summary>📄 Abstract</summary>
  Post-training is essential for refining the domain-specific capabilities of large language models (LLMs), yet existing reward optimization and distribution matching methods tightly couple policy exploration with distribution alignment. This coupling forces expensive exploration directly on the policy model and severely hinders the asynchronous generation, reuse, and cross-model transfer of optimization signals. In this paper, we propose Proxy-guided Update Signal Transfer (PUST), a novel post-tr...
  </details>

- **2026-07-13** — Thi Kim Trang Vo, Nghia Hieu Nguyen, Ha Minh Tan — [Direct Image-to-Modern Vietnamese Translation of Han-Nom Manuscripts via Multimodal RLHF Preference Alignment](http://arxiv.org/abs/2607.11434v1)
  <details><summary>📄 Abstract</summary>
  Translating Han-Nom manuscripts into modern Vietnamese is challenging because historical pages are often degraded, the script contains rare logographic characters, and parallel supervision is limited. We propose a multimodal RLHF preference-alignment framework that conditions Vietnamese generation on manuscript images and aligned Han-Nom source text. The model combines four streams: CLIP ViT-L/14@336 for visual features, bert-base-chinese for Han-Nom representations, vinai/phobert-base for Vietn...
  </details>

- **2026-07-13** — Philip Schultheis, Kimia Chavoshi, John Lygeros — [Decentralized Model Predictive Control of Connected and Automated Vehicles with Coupled Safety Constraints](http://arxiv.org/abs/2607.11403v1)
  <details><summary>📄 Abstract</summary>
  Connected and Automated Vehicles (CAVs) operating on lane-free highways offer substantial gains in traffic efficiency. However, their inherent nonlinear dynamics and the presence of coupled, nonconvex safety constraints present critical challenges to control design. Centralized Model Predictive Control (MPC) ensures safety, but suffers from scalability and communication limitations. To address these challenges, this paper investigates decentralized MPC (DMPC) for CAV coordination, focusing on it...
  </details>

- **2026-07-13** — Chunyu Hu, Tianyin Liao, Ge Lan et al. — [Surprisingly Simple and Effective Multi-Domain Graph Foundation Model through Graph-to-Table Alignment](http://arxiv.org/abs/2607.11374v1)
  <details><summary>📄 Abstract</summary>
  Graph Foundation Models (GFMs) have emerged as a promising paradigm for learning transferable representations across diverse graph domains. Recent advancements in GFMs have been largely dominated by two paradigms: Graph Neural Network and Large Language Model (LLM) based methods. However, these methods often face a fundamental dilemma between training with limited data and a heavy reliance on textual attributes. Tabular foundation models (TFMs) offer a potential alternative, as node features and...
  </details>

- **2026-07-13** — Ajitesh Jamulkar, Aritra Hazra — [BackgroundMellow: A Multi-Modal Cohesive Framework for Narrative-Driven Rich Cinematic Soundscape Generation](http://arxiv.org/abs/2607.11364v1)
  <details><summary>📄 Abstract</summary>
  Generating immersive, synchronized and cinematic audio for long-form textual narratives remains a significant challenge in multi-modal AI. While current Text-to-Audio (TTA) frameworks successfully synthesize isolated sound effects, they struggle with narrative cohesion, temporal alignment, and cinematic emotional depth. We present BackgroundMellow, a framework that treats story-to-audio generation as a precise orchestration and signal processing problem. This framework is enabled without ground-...
  </details>

- **2026-07-13** — Jimin Xu, Tianbao Wang, Tao Jin et al. — [HierCAD: Hierarchical Text-to-CAD Design via Structure Alignment and Parameter Grounding](http://arxiv.org/abs/2607.11339v1)
  <details><summary>📄 Abstract</summary>
  Recent text-to-CAD approaches have shown promising results by leveraging large language models, but they often struggle with maintaining structural consistency in complex designs and accurately grounding geometric parameters. To address these issues, we propose HierCAD, a hierarchical text-to-CAD framework that improves both structural reasoning and parameter prediction. HierCAD reformulates CAD generation as progressive reasoning by decomposing CAD construction trees into object-level procedura...
  </details>

- **2026-07-13** — Alexis Popovici, Andrei Ionascu, Adrian-Marius Dumitran — [The Paternalistic Filter: Epistemic Injustice and Differential Refusal in LLM-Mediated History Education for Marginalized Romanian Students](http://arxiv.org/abs/2607.11292v1)
  <details><summary>📄 Abstract</summary>
  As Large Language Models (LLMs) are increasingly deployed as conversational tutors, they risk institutionalizing systemic inequalities. This study presents a systematic API audit of four LLMs acting as history tutors, evaluating 1,800 responses regarding the 1989 Romanian Revolution across five student personas varying by ethnicity and socio-economic tier. We uncover four interconnected patterns of \emph{epistemic paternalism}: (1)~\textbf{Differential Refusal}, where safety-aligned models block...
  </details>

- **2026-07-13** — Gangsu Kim, Won-Ki Jeong — [LaGuadia: Language-Guided Adaptive Distillation from Pathology Foundation Models](http://arxiv.org/abs/2607.11257v1)
  <details><summary>📄 Abstract</summary>
  Pathology Foundation Models (PFMs) offer powerful Whole Slide Image (WSI) representations but suffer from massive computational costs. While Knowledge Distillation (KD) can create efficient student models, existing multi-teacher methods often use suboptimal uniform weighting that ignores tissue heterogeneity. We propose LaGuadia (Language-Guided Adaptive DistillAtion), a framework that develops a compact pathology image encoder by dynamically integrating expertise from multiple PFMs under clinic...
  </details>

- **2026-07-13** — Shyam Marjit, Dheeraj Baiju, Anuj Shikarkhane et al. — [DynEval: Holistic Evaluations of T2I Generative Models in the Wild](http://arxiv.org/abs/2607.11199v1)
  <details><summary>📄 Abstract</summary>
  Recent advances in text-to-image (T2I) generation have led to models capable of producing highly realistic images. Yet, reliably evaluating their outputs remains challenging, especially at scale. Existing automatic evaluators, often relying on a static prompt set, struggle to capture subtle failure modes such as partial prompt misalignment, compositional errors, or visually plausible but semantically incorrect generations. In this work, we introduce DynEval, a Dynamic Evaluation framework design...
  </details>

- **2026-07-13** — Alexandre Chapin, Emmanuel Dellandrea, Liming Chen — [Slot-RAE: Streamlining Object-Centric Learning via Direct Representation Auto-Encoders](http://arxiv.org/abs/2607.11196v1)
  <details><summary>📄 Abstract</summary>
  Deploying object-centric models for real-world scene understanding typically requires complex pipelines to achieve both robust scene decomposition and high-fidelity generation. Recent diffusion-based approaches have improved visual quality, but they almost universally rely on heavy, pretrained generative priors (e.g., Stable Diffusion) and external VAE latent spaces. In this paper, we propose Slot-RAE, a much simpler, fully integrated framework that operates directly within the continuous semant...
  </details>

- **2026-07-13** — Soohan Abbasi, Shahid Munir Shah, Rafia Shaikh et al. — [SISA-Rec: A Semantically Integrated Sequential Recommender with Contrastive Alignment](http://arxiv.org/abs/2607.11168v1)
  <details><summary>📄 Abstract</summary>
  Recommendation systems help users recommend relevant items from a large collection of choices. Present work on transformer-based sequential recommendation learns user preferences from interaction logs, but it mostly focuses on item identifiers and doesn't fully use the semantic meaning of items. This limitation becomes a major challenge in sparse and cold-start scenarios where historical interaction data is limited. To solve this problem, we introduce SISA-Rec (Semantically Integrated Sequential...
  </details>

- **2026-07-13** — Quynh Vo, Cong-Duy Nguyen, Ponhvoan Srey et al. — [TIGER: Text-Conditioned Visual Gated Routing with Acceptance Alignment for Multimodal Speculative Decoding](http://arxiv.org/abs/2607.11131v1)
  <details><summary>📄 Abstract</summary>
  Speculative decoding accelerates autoregressive generation by letting a lightweight drafter propose multiple tokens that are verified by a larger target model. Although effective for text-only LLMs, speculative decoding yields limited gains in VLMs because drafters often diverge on vision-critical content, while existing multimodal acceleration methods do not directly address irrelevant visual evidence or optimize the verifier-accepted prefix length that governs speedup. We propose TIGER, a Text...
  </details>

- **2026-07-13** — Xiuwei Chen, Quanlin Chen, Wentao Hu et al. — [Beyond the Eye: Efficient Multimodal Reasoning via Self-Regulated Implicit Visual Tools](http://arxiv.org/abs/2607.11106v1)
  <details><summary>📄 Abstract</summary>
  Recent multimodal large language models (MLLMs) have made remarkable progress on fine-grained perception tasks under the "Thinking with Images" (TwI) paradigm by iteratively performing various visual tool operations. However, this paradigm relies heavily on frequent external tool calls and repeated image re-encoding, which leads to substantial computational overhead and inference latency. To address these issues, we propose Beyond the Eye (BEE), a novel implicit visual tool paradigm centered on ...
  </details>

- **2026-07-13** — Andrew Hong, Jason Potteiger — [Dimensionality in Satisfaction Ratings](http://arxiv.org/abs/2607.11026v1)
  <details><summary>📄 Abstract</summary>
  We used a large language model (GPT-4.1) to annotate the text of about 9,000 support conversations at a global consumer-goods firm, decomposing customer-care satisfaction into component axes (overall, agent, outcome, product, and customer effort), and validated the LLM annotations against the satisfaction ratings customers gave themselves. Four of five axes track self-reported satisfaction closely (overall, agent, and outcome near an unadjusted 0.65; effort -0.54), while product satisfaction is ...
  </details>

- **2026-07-13** — Varun Ramesh Jois, Antonella DiLillo, James Storer — [Reference-Based Face Super-Resolution Using the Spatial Transformer](http://arxiv.org/abs/2607.11025v1)
  <details><summary>📄 Abstract</summary>
  Face super-resolution is the task of increasing the resolution of an image containing a face thereby adding finer detail. It is a ubiquitous task in many computer vision applications and quite often the user isn't even aware that it is being performed. However, doing it with high fidelity is challenging as it is an ill-posed problem. In this paper we present a reference-based solution for face super-resolution that uses higher resolution reference images to aid in the task. We show an alignment ...
  </details>

- **2026-07-13** — Jie Sun, Mao Zheng, Mingyang Song et al. — [EasyOPD: An Easy-to-use On-Policy Distillation Framework for Large Language Models](http://arxiv.org/abs/2607.11012v1)
  <details><summary>📄 Abstract</summary>
  Conventional language-model distillation often relies on fixed teacher-generated data, which may not cover the states encountered by an evolving student policy. On-policy distillation (OPD) instead collects teacher or evaluator supervision on student-generated rollouts. However, existing OPD methods differ substantially in supervision form, tokenizer compatibility, teacher access, and supervision granularity, leading to fragmented implementations that are difficult to reproduce and extend. We pr...
  </details>

- **2026-07-13** — Youngung Han, Hyunsu Go, Kyeonghun Kim et al. — [LoSA-Net: A Localized and Scale-Adaptive Network for Boundary-Sensitive Prediction of Perineural Invasion in 3D MRI](http://arxiv.org/abs/2607.10992v1)
  <details><summary>📄 Abstract</summary>
  Perineural invasion (PNI) is a clinically relevant indicator of tumor aggressiveness and can influence surgical decision-making, motivating interest in reliable preoperative assessment. The subtle MRI features of PNI, however, often resemble nearby anatomy, complicating noninvasive prediction. These fine perineural cues are easily attenuated by routine downsampling or overly global feature aggregation, reducing the effectiveness of conventional volumetric models. We present LoSA-Net, a localized...
  </details>

- **2026-07-13** — Thanh-Nhan Vo, Thanh-Khoi Nguyen, Trong-Thuan Nguyen et al. — [TreeSoc: Tree-Structured Dynamic Reasoning and Tool Synergy for Soccer Video Understanding](http://arxiv.org/abs/2607.10990v1)
  <details><summary>📄 Abstract</summary>
  Automated understanding of complex soccer scenarios from video remains a significant challenge for contemporary vision-language models (VLMs), which suffer from shallow cross-modal alignment and exhibit fundamental limitations in multi-step reasoning and coordinated tool integration. We present TreeSoc, a structured reasoning framework that reformulates soccer video question answering as a hierarchical search problem rather than a single-pass prediction. Specifically, TreeSoc employs a dynamic d...
  </details>

- **2026-07-12** — Guoliang You, Hongming Li, Yuanwang Zhang et al. — [Learning Anatomy-Grounded CT Vision-Language Representations with Organ-Hierarchical Report Knowledge](http://arxiv.org/abs/2607.10953v1)
  <details><summary>📄 Abstract</summary>
  Medical vision-language pretraining (VLP) from paired CT images and radiology reports enables scalable representation learning, but most existing methods align either whole scans with entire reports or local image regions with text fragments. These formulations underuse a key property of radiology reports: findings are organized around anatomical structures, with abnormalities described by organs, disease concepts, locations, and severity-related attributes. We propose OKA-CT, an organ-hierarchi...
  </details>

- **2026-07-12** — Asher Sprigler, Yang-Yang Feng, Iftach Amir et al. — [Toward Contemplative LLM: A Modular Framework for Evaluating and Enhancing LLM Alignment in Mental Health](http://arxiv.org/abs/2607.10871v1)
  <details><summary>📄 Abstract</summary>
  Contemplative traditions have long guided ethical behavior and prosocial interaction, and recent work suggests that contemplative principles (e.g., mindfulness, compassion, non-dual reasoning) may offer a promising paradigm for aligning large language models (LLMs), improving cooperation and reducing ethical violations in LLM outputs. However, as new models, evaluation metrics, and benchmarks emerge rapidly, it remains challenging to systematically assess whether and how contemplative principles...
  </details>

- **2026-07-12** — Tonmoy Hossain, Atiqur Rahman, Farhana Hossain Swarnali et al. — [Learning To Focus: Anatomy-Guided Attention Regularization for Medical Image Classification](http://arxiv.org/abs/2607.10851v1)
  <details><summary>📄 Abstract</summary>
  Medical image classification models are ideally expected to identify diagnostically relevant regions while making predictions, yet standard classification losses rarely provide spatial supervision. Explicit supervision via anatomical shape information, such as segmentation masks of task-relevant anatomy, has been shown to guide the network toward regions relevant to the target prediction. However, obtaining such masks incurs substantial manual annotation effort and computational overhead. With t...
  </details>

- **2026-07-12** — Venkanna Babu Guthula, Oswin Krause, Dimitri Gominski et al. — [Align and Segment: Unsupervised Learning for Building Segmentation From Misaligned Labels](http://arxiv.org/abs/2607.10841v1)
  <details><summary>📄 Abstract</summary>
  Supervised learning for image segmentation typically requires spatially aligned image and label sets. When images and labels originate from different sources, the pairing may be misaligned, which can significantly deteriorate the performance of the learned models. This is especially common in remote sensing, when aerial or satellite images are co-registered with labels from another source (e.g., OpenStreetMap). In this work, we propose a novel approach for training on misaligned labels, where we...
  </details>

- **2026-07-12** — Kai Yu, Lu Chen, Hanqi Li — [Distributed Agent System: Fault-Tolerant Collaboration Among Embodied Agents](http://arxiv.org/abs/2607.10811v1)
  <details><summary>📄 Abstract</summary>
  AI engineering is shifting from passive text generation by large language models (LLMs) to agent-driven task execution, creating new reliability challenges for long-horizon tasks under resource constraints and environmental uncertainty. Conventional error-elimination optimization strategies fail to address cumulative error propagation. This paper proposes Distributed Agent System (DAS), a device-edge-cloud framework for fault-tolerant collaboration among heterogeneous agents. We redefine agent r...
  </details>

- **2026-07-12** — Zehui Guo, Zhen Wang, Junwei Shu et al. — [h-Flow: Flexible Flow-based Image Editing via Doob's h-Transform](http://arxiv.org/abs/2607.10800v1)
  <details><summary>📄 Abstract</summary>
  Editing images with pre-trained text-to-image flow models typically requires carefully balancing target alignment with the desired prompt and source consistency with the original image. Existing approaches either rely on inversion-based pipelines or heuristic source-to-target trajectory constructions, which often depend on architecture-specific designs or are sensitive to hyperparameters. In this paper, we propose h-Flow, a training-free and theoretically grounded flow-based editing framework. I...
  </details>

- **2026-07-12** — Siyuan Song, Zhiheng Qian, Yunhao Zhang et al. — [The First ChineseBabyLM Challenge: training data-efficient and cognitively plausible language models for Chinese](http://arxiv.org/abs/2607.10745v1)
  <details><summary>📄 Abstract</summary>
  This paper describes the first ChineseBabyLM challenge, which will be held in the 2026 NLPCC conference. The challenge calls for researchers to train language models from scratch with 100 million Chinese tokens and evaluates the models on 3 tracks of tasks: NLU, cognitive alignment and Hanzi knowledge. There is no restriction on tokenizer, model architecture and the number of training epochs. Details of the challenge can be found in https://chinese-babylm.github.io/.
  </details>

- **2026-07-12** — Khush Kataruka, Harshit Maurya, Anuja Vats et al. — [WasteAssistant: Regulation-Guided Visual Question Answering Framework for Intelligent Waste Segregation and Sustainable Managemen](http://arxiv.org/abs/2607.10610v1)
  <details><summary>📄 Abstract</summary>
  Efficient waste segregation is critical for sustainable urban management and environmental governance. Existing automated systems are limited by single-modality visual processing, insufficient contextual understanding, and weak regulatory alignment. To address these issues, we propose a language-guided vision-AI framework that integrates vision-language models and multimodal large language models for joint visual-linguistic reasoning. This framework implements a visual question answering paradig...
  </details>


### 📂 robustness
*鲁棒性与可靠性 / Robustness & Reliability* — 90 papers

- **2026-07-15** — Boyuan Wang, Zhenyuan Zhang, Zhiqin Yang et al. — [PhysClaw-0: A Symbiotic Agentic System for Robot Autonomy via Language Corrections](http://arxiv.org/abs/2607.14047v1)
  <details><summary>📄 Abstract</summary>
  Autonomous data collection governs the volume and quality of real-world trajectories for manipulation policy learning. Existing pipelines reduce human effort via self-resetting, VLM verification, or language-guided correction, yet episode-scoped fixes must be reissued whenever the same failure recurs, so oversight cost grows with session length rather than with the number of distinct problems. We present PhysClaw-0, a human-robot symbiotic agentic system in which corrections are retained and reu...
  </details>

- **2026-07-15** — Jiangang Han — [Partially Correlated Verifier Cascades in LLM Harnesses: Concave Log-Odds, Polynomial Reliability, and Blind-Spot Ceilings](http://arxiv.org/abs/2607.13918v1)
  <details><summary>📄 Abstract</summary>
  Serial verification gates are a core reliability primitive in LLM harnesses: a candidate answer is returned only if $k$ verifier calls all accept it. Under conditionally independent gates, the recent Odds Law (arXiv:2606.15712) shows that posterior log-odds grow linearly in $k$, so failure decays exponentially, and states that "a tight theory of partially correlated verifier cascades remains open." This note gives a minimal such theory. Modeling the per-instance false-accept rate on the generato...
  </details>

- **2026-07-15** — Zichen Ding, Jiaye Ge, Shufan Jiang et al. — [AgentCompass: A Unified Evaluation Infrastructure for Agent Capabilities](http://arxiv.org/abs/2607.13705v1)
  <details><summary>📄 Abstract</summary>
  As Large Language Models (LLMs) evolve into autonomous agents, the need for unified evaluation infrastructure becomes critical. However, current evaluation pipelines remain highly fragmented and tightly coupled, hindering reproducibility and causing redundant engineering. To address this, we introduce AgentCompass, an open-source, lightweight, and extensible infrastructure for evaluating LLM-based agents. AgentCompass organizes the evaluation process around three independent components, namely B...
  </details>

- **2026-07-15** — Ximeng Mao, Nanda H. Krishna, Avery Hee-Woon Ryoo et al. — [Leveraging unlabelled data for generalizable neural population decoding](http://arxiv.org/abs/2607.14086v1)
  <details><summary>📄 Abstract</summary>
  Robust and accurate neural decoders are integral to neurotechnologies such as brain-computer interfaces and closed-loop experiments. Recent work has shown that tokenizing neural data at the spike level facilitates multi-session pretraining and delivers state-of-the-art decoding performance. However, current spike-based models are restricted to supervised learning (SL), limiting training to datasets with paired behavioural labels. To address this limitation, we introduce MOJO (Masked autOencoder-...
  </details>

- **2026-07-15** — Jingyu Xiao, Zhongyi Zhang, Haoran Hou et al. — [VisualRepair: Dynamic Tool Calling and Region Focusing for Visual Software Issue Repair](http://arxiv.org/abs/2607.14075v1)
  <details><summary>📄 Abstract</summary>
  Automated Program Repair (APR) has witnessed significant progress with the advent of Large Language Models (LLMs). However, as modern software systems increasingly expose rich graphical user interfaces, effectively leveraging visual information from bug screenshots has become essential for understanding bugs and generating accurate fixes in multimodal scenarios. Real-world issue reports frequently contain heterogeneous visual attachments including UI screenshots, IDE snapshots, GIFs, and text-ce...
  </details>

- **2026-07-15** — Tam Nguyen, Hung Nguyen, Robert Ogburn — [AI-accelerated End-to-End Framework for Rapid Professional Upskilling](http://arxiv.org/abs/2607.14044v1)
  <details><summary>📄 Abstract</summary>
  By 2030, 59 of every 100 workers will need reskilling or upskilling, yet the average time to close an enterprise skills gap grew from roughly 3 days in 2014 to 36 days in 2018. Most current frameworks accelerate single stages of upskilling programs and generally lack industry validation. We present an end-to-end framework that applies AI acceleration across five stages of knowledge acquisition, content development, content review and verification, teaching, and assessment development; with a str...
  </details>

- **2026-07-15** — Geng Li, Haiwen Li, Rui Chen et al. — [Peak-End-Net: A Peak-End Rule Inspired Framework for Generalizable Video Aesthetic Assessment](http://arxiv.org/abs/2607.13941v1)
  <details><summary>📄 Abstract</summary>
  Video aesthetic assessment (VAA) aims to predict how aesthetically pleasing a video is, yet remains far less explored than other visual assessment tasks. Its progress is hindered not only by the scarcity of large-scale benchmarks, but also by the intrinsic subjectivity of aesthetic judgment, which is shaped by human perception. In this paper, we revisit VAA from a psychological perspective and propose \textit{Peak-End-Net}, a lightweight and interpretable framework inspired by the \textit{peak-e...
  </details>

- **2026-07-15** — Jianguo Yu, Rukang Wang, Duanfeng Chu et al. — [S-squared-VLA: Decoupling Semantic and Spatial Streams in Vision-Language-Action Models for Autonomous Driving](http://arxiv.org/abs/2607.13926v1)
  <details><summary>📄 Abstract</summary>
  Vision-Language Models (VLMs) have demonstrated remarkable potential for high-level reasoning in autonomous driving, yet they fundamentally struggle to generate precise, low-level control actions. This limitation is rooted in a semantic-physical gap caused by the inherent mismatch between discrete language tokens and continuous trajectory planning. While Vision-Language-Action (VLA) architectures attempt to bridge this gap by unifying perception and control into a single policy, this entanglemen...
  </details>

- **2026-07-15** — Ismael Rousseau, Geraldine Damnati, Frederic Bechet — [DeepStress: Stress-Testing Deep Search Agents](http://arxiv.org/abs/2607.13920v1)
  <details><summary>📄 Abstract</summary>
  While search agents demonstrate impressive capabilities in multi-step question answering, their robustness to poor-quality evidence remains under-explored. This phenomenon occurs rarely in realistic benchmarks but can lead to dramatic failure in real life applications. Therefore in this study we propose DeepStress, a stress testing framework that controls the frequency of challenging evidence by replacing the retrieval module of search agents with a controlled synthetic environment. We use this ...
  </details>

- **2026-07-15** — Xueyao Zhang, Chenyang Yan, Bo Yang et al. — [Task-Oriented Sensing and Covert Transmissions for Collaborative Multi-AUV Systems](http://arxiv.org/abs/2607.13880v1)
  <details><summary>📄 Abstract</summary>
  In underwater covert cooperative missions, autonomous underwater vehicles (AUVs) often cannot rely on active sonar to continuously obtain complete information, since active sensing and frequent communications increase the risk of exposure. As a result, AUVs primarily rely on passive observation, an approach that yields incomplete local perception and limited task efficiency. Although underwater acoustic communications can mitigate this limitation through information sharing, they are simultaneou...
  </details>

- **2026-07-15** — Zhuoyuan Fu, Zeshang Li, Yiqiong Zhang et al. — [Towards Enhancing 3D Spatial Reasoning in Medical Multimodal Large Language Models](http://arxiv.org/abs/2607.13860v1)
  <details><summary>📄 Abstract</summary>
  While Multimodal Large Language Models (MLLMs) have demonstrated remarkable success in 2D medical image understanding, their extension to 3D volumetric imaging remains hindered by prohibitive annotation costs and dataset opacity. Current data formats, predominantly consisting of rigid Visual Question Answering (VQA) pairs or unstructured final clinical reports, typically fail to capture explicit clinical reasoning. To address this limitation, we introduce a large-scale structured reasoning datas...
  </details>

- **2026-07-15** — Rodrigo Pato Nogueira, Marco Vieira, João R. Campos — [PROBE: Benchmarking Code Generation in Large Language Models](http://arxiv.org/abs/2607.13820v1)
  <details><summary>📄 Abstract</summary>
  Large Language Models (LLMs) are increasingly being used in everyday software engineering tasks, particularly in automated code generation. Despite their widespread adoption, these models remain far from perfect, making systematic and fair evaluation essential to understand their strengths and limitations. In the context of code generation, existing benchmarks are limited: they often target a single programming language and rely primarily on unit test outcomes, while overlooking other critical d...
  </details>

- **2026-07-15** — Xiaopeng Zhang, Yueyang Weng, Qi Liu et al. — [Learning Robust Execution in Robotic Manipulation with Agentic Reinforcement Learning](http://arxiv.org/abs/2607.13818v1)
  <details><summary>📄 Abstract</summary>
  Robotic manipulation poses fundamental challenges due to uncertainty, long-horizon execution, and compounding errors, which can easily destabilize execution and lead to task failure. Although recent vision-language-action (VLA) models exhibit strong generalization, they typically lack explicit mechanisms to assess execution stability and to recover when execution deviates from its nominal behavior. In this paper, we propose: (1) two complementary metrics to assess execution quality at runtime, a...
  </details>

- **2026-07-15** — Jin-Peng Yang, Yan-Hong Qin — [Multihump-Multivalley Soliton Families on a Plane Wave Background in Birefringent Optical Fibers](http://arxiv.org/abs/2607.13773v1)
  <details><summary>📄 Abstract</summary>
  We obtain a family of multihump-multivalley solitons (MHMVSs) on a plane-wave background in birefringent optical fibers governed by the two-component Fokas-Lenells equations, with exact solutions derived via the Darboux transformation method. The fundamental solutions are systematically classified through their phase diagrams, and higher-order configurations are identified as well. Notably, the construction extends to solitons with arbitrary MHMV structures, a class of solutions previously unrep...
  </details>

- **2026-07-15** — Ashish Thapa, Samrat Karki — [Barnamala: Parameter-Efficient Handwritten Devanagari Recognition at Benchmark Saturation](http://arxiv.org/abs/2607.13689v1)
  <details><summary>📄 Abstract</summary>
  We built a compact convolutional network (1.11 M parameters) for 46-class DHCD Devanagari recognition and reached 99.73%, the highest reported at 15.6x smaller than prior state-of-the-art. We have effectively reached the saturation point: every model tested, large teacher ensembles included, hits the same 11-error intrinsic floor. No configuration achieves a statistically clear win under exact McNemar tests with Wilson confidence intervals. Even without knowledge distillation, our student matche...
  </details>

- **2026-07-15** — Pengxuan Gao, Kai Ying, Botao Wu et al. — [M3F-UAV: A Missing-Modality Multimodal Foundation Model for Low-Altitude Wireless Sensing](http://arxiv.org/abs/2607.13678v1)
  <details><summary>📄 Abstract</summary>
  Low-altitude unmanned aerial vehicles (UAVs) are emerging as key platforms for wireless intelligence tasks. However, practical low-altitude wireless systems usually operate in complex urban environments, where visual occlusion, sparse geometric observations, multipath propagation, and sensor failures may degrade the reliability of single-modality models. To address these challenges, this paper proposes M3F-UAV, a missing-modality multimodal foundation model for low-altitude wireless sensing. The...
  </details>

- **2026-07-15** — Boyu Mi, Mengchen Ma, Yifei Yao et al. — [Exploratory, Communicative, and Deployable: Vision-Driven Embodied Agents for Open-World Mobile Manipulation](http://arxiv.org/abs/2607.13653v1)
  <details><summary>📄 Abstract</summary>
  Real-world deployment of embodied agents requires active exploration, visual grounding, and interactive intent disambiguation. However, existing frameworks often rely on privileged simulator states or assume complete instructions, bypassing realistic deployment challenges. To bridge this gap, we present REAL, an agentic framework for open-world mobile manipulation. REAL establishes sim-to-real-consistent environment APIs without oracle perception and integrates a simulated user to enable human-i...
  </details>

- **2026-07-15** — Shiyin Lu, Yinglun Li, Yu Xia et al. — [OvisOCR2 Technical Report](http://arxiv.org/abs/2607.13639v1)
  <details><summary>📄 Abstract</summary>
  We introduce OvisOCR2, a 0.8B document parsing model. OvisOCR2 is designed as an end-to-end parser: given a document page image, it generates a Markdown representation in natural reading order, covering text, formulas, tables, and visual regions. We build a data engine that combines filtered real-document annotations with synthetic pages whose rendered images and Markdown targets are derived from the same HTML source. The training recipe includes supervised fine-tuning, reinforcement learning on...
  </details>

- **2026-07-15** — David Krongauz, Arad Zulti, Eran Segal et al. — [Automatic Ordinary Differential Equations Discovery For Biological Systems Using Large Language Model Powered Agentic System](http://arxiv.org/abs/2607.13608v1)
  <details><summary>📄 Abstract</summary>
  Automatic scientific discovery has long been a goal of computational scholars - a machine that can discover nature's secrets on its own, moving computational systems beyond data-fitting tools toward the generation and refinement of mechanistic models of the universe. Recent advances in symbolic regression (SR) and large-language-model (LLM)-based agents suggest that such systems can recover equations from data, incorporate domain priors, and automate parts of the research workflow. However, most...
  </details>

- **2026-07-15** — Xian Li, Rong Wei, Lujie Yang et al. — [UniPhysGen: Unified Physical Grounding for Simulation-Ready 3D Assets](http://arxiv.org/abs/2607.13586v1)
  <details><summary>📄 Abstract</summary>
  Physically grounded 3D assets are increasingly important for embodied AI and robotic simulation. However, most existing 3D assets lack unified physical semantics, including articulation semantics and intrinsic physical properties, required for realistic interaction. Current approaches either treat these semantics independently or rely on canonicalized object structures, limiting robustness across heterogeneous 3D assets. We present UniPhys, a scalable framework for automatically transforming raw...
  </details>

- **2026-07-15** — Jun-Gill Kang, Jaehyun Park, Tae-Gyu Song et al. — [Agile perceptive multi-skill locomotion for quadrupedal robots in the wild](http://arxiv.org/abs/2607.13579v1)
  <details><summary>📄 Abstract</summary>
  Enabling quadrupedal robots to traverse complex terrains-from rugged outdoor environments to urban landscapes-requires seamless integration of multiple motor skills, smooth transitions between gaits, and high-speed perceptive locomotion using only onboard sensors. We present APT-RL (Action Pretrained Transformer-based Reinforcement Learning), a unified framework that enables multi-skill locomotion to achieve high-speed traversal in complex environments through autonomous skill transitions utiliz...
  </details>

- **2026-07-15** — Grzegorz Brzezinka — [Graded Entity-Familiarity Readouts in Language Models: Polish Adaptation, Cross-Language Robustness, and Refusal Steering](http://arxiv.org/abs/2607.13568v1)
  <details><summary>📄 Abstract</summary>
  Can a language model estimate its familiarity with an entity before generating an answer? We study activations at the final prompt token in twelve instruction-tuned models from the Bielik, PLLuM, Gemma-4, and Qwen3 families, using a new dataset of 1,440 Polish entities spanning four domains and ten Wikipedia-pageview deciles, plus fabricated controls. Familiarity-probe scores separate real from fabricated entities in every family; in the Polish-adapted Bielik and PLLuM families they additionally...
  </details>

- **2026-07-15** — A. Garofalo, T. Muraveva, L. Monti et al. — [Improving reddening estimates for RR Lyrae stars in the Gaia bands: a machine learning approach to the PAC(Z) relation](http://arxiv.org/abs/2607.13557v1)
  <details><summary>📄 Abstract</summary>
  RR Lyrae stars are essential tracers of old stellar populations and distance indicators across the Milky Way and nearby galaxies. However, their use as standard candles is limited by uncertainties in extinction, especially in the Gaia bands. In Gaia DR3, absorption values (AG) for fundamental-mode RR Lyrae (RRab) were based on an empirical period-amplitude-color (PAC) relation calibrated on a small sample and on passband transformations. We aim to recalibrate extinction relations for RRab stars ...
  </details>

- **2026-07-15** — Lukas Zenger — [Intuitionistic Dynamic Logic](http://arxiv.org/abs/2607.13528v1)
  <details><summary>📄 Abstract</summary>
  This thesis develops the mathematical theory of intuitionistic dynamic logics - extensions of intuitionistic propositional logic with modalities and fixed point operators. Such systems provide formal tools for reasoning about change, such as encountered in mathematical systems evolving over time or in the knowledge state of an agent after an information update.   We investigate five intuitionistic dynamic logics: intuitionistic master modality, intuitionistic common knowledge logic, intuitionist...
  </details>

- **2026-07-15** — Zongyi Li, Jun Wang, Tianwei Hou et al. — [Pinching-Antenna Systems (PASS)-Based User-Side Navigation: An Anchor-Line-based Approach](http://arxiv.org/abs/2607.13485v1)
  <details><summary>📄 Abstract</summary>
  Pinching-antenna systems (PASS) are capable of dynamically reconfiguring wireless channels by flexibly repositioning pinching antennas (PAs) along the waveguides to establish short-range line-of-sight links. In this paper, a user-side navigation framework for PASS is proposed, where mobile users determine their own positions using only downlink broadcast signals without any prior knowledge of the PA positions. First, a Lambert W function-based PA positioning and pseudorange estimation (LWF-PAP) ...
  </details>

- **2026-07-15** — Mingzhu Wang, Yun Shang — [PQFA: Parallel Quantum Feature Augmentation of Fused Representations for Multimodal Classification](http://arxiv.org/abs/2607.13466v1)
  <details><summary>📄 Abstract</summary>
  Most multimodal learning methods improve how heterogeneous representations are aligned and fused, while post-fusion enhancement remains less explored. We propose Parallel Quantum Feature Augmentation (PQFA), a hybrid quantum-classical framework that applies multiple shallow variational quantum circuits to fused multimodal features. Text and image representations extracted by frozen RoBERTa and ViT encoders are processed through bidirectional cross-attention, attentive pooling, and adaptive gated...
  </details>

- **2026-07-15** — Yurui Zhao, Xiang Wang, Zhitao Huang et al. — [Compositional Zero-Shot Recognition based on Tangent Space Disentanglement for Composite Modulation Signals](http://arxiv.org/abs/2607.13463v1)
  <details><summary>📄 Abstract</summary>
  Automatic composite modulation recognition (ACMR) is critical for integrated sensing and communication (ISAC) systems, while conventional approaches face significant challenges due to the semantic coupling between inner-layer and outer-layer modulations in composite modulation (CM), degraded performance under joint hardware and channel imperfections, and limited capability to handle unknown modulation schemes. To this end, we design a disentangled semantic space and propose zero-shot learning fr...
  </details>

- **2026-07-15** — Zhentao Song, Yufeng Gao, Xing Fang et al. — [TMallGS: Scaling Unified Feature and Sequence Modeling for Generative E-commerce Search](http://arxiv.org/abs/2607.13398v1)
  <details><summary>📄 Abstract</summary>
  In industrial search and ranking systems, Click-Through Rate (CTR) prediction is shifting from traditional Deep Learning Recommendation Models (DLRM) toward unified, compute-intensive Transformer architectures. This transition is driven by the need to improve Model FLOPs Utilization (MFU) and achieve predictable gains through scaling laws. However, existing approaches such as OneTrans and Climber often adopt an all-in-tokenization strategy when adapting Large Language Model (LLM) architectures, ...
  </details>

- **2026-07-15** — Alexander Langmann, Frederico Pita de Araujo, Mattia Piccinini et al. — [A Hybrid Sampling-Based Trajectory Planner with Game-Theoretic Guidance for Autonomous Racing](http://arxiv.org/abs/2607.13354v1)
  <details><summary>📄 Abstract</summary>
  Autonomous racing demands planning algorithms that balance vehicle dynamics at the limits of handling with strategic decision-making in competitive multi-agent scenarios. Game theory provides a mathematical framework for modeling these interactions, enabling interactive trajectory planning and strategic behaviors, such as blocking. However, directly solving full dynamic games online is computationally prohibitive and challenging to integrate into robust, high-frequency autonomous software stacks...
  </details>

- **2026-07-15** — Joseph M. Cavanagh, Jonathan B. Arnold, Giovanni Battista Alteri et al. — [How Well Can Frontier Large Language Models Generate Structures? High Quality Prediction of Molecular Geometries with Help from Fine-Tuning](http://arxiv.org/abs/2607.13350v1)
  <details><summary>📄 Abstract</summary>
  The power of Large Language Models (LLMs) has led us to investigate how they might be fine-tuned for learning the "language of molecular geometry". The fine-tuning of the LLMs using Cartesian coordinates or Z-matrices provides an extremely simple method for accurately predicting equilibrium structures and diverse sets of conformers of small organic and drug-like molecules with excellent accuracy and outperforming specialized deep learning models. While the most common representation of molecular...
  </details>

- **2026-07-14** — Dmitrij Żatuchin — [Where Does the Noise Come From? A Variance-Components Decomposition of Non-Determinism in LLM Brand Answers](http://arxiv.org/abs/2607.13304v1)
  <details><summary>📄 Abstract</summary>
  Teams measuring whether large language models (LLMs) recommend a brand face a reproducibility problem: ask the same question twice and the answer moves. Practice resamples each prompt a few times (commonly five) and averages, treating within-prompt resampling as the source of the noise. But a measured brand score moves for at least four separable reasons: within-prompt resampling, prompt paraphrase, model identity, and query language. We specify a crossed random-effects (generalizability-theory)...
  </details>

- **2026-07-14** — Sen Yang, Yuen-Hei Yeung — [Resist and Update: Counterfactual Report Coordinates for Incentive-Compatible LLMs](http://arxiv.org/abs/2607.12985v1)
  <details><summary>📄 Abstract</summary>
  Aligned language models routinely misreport under non-evidential incentive pressure: they agree with a confident user or overstate certainty even when their internal belief is unchanged. We cast this as a failure of internal incentive-compatibility (IC) and present a method for learning and certifying counterfactual report mediators that hold a model's reports to a causal contract: invariant to forbidden influences (pressure, prestige, restyling) and responsive to licensed ones (genuine evidence...
  </details>

- **2026-07-14** — Mehak Dhaliwal, Rasta Tadayon, Andong Hua et al. — [From Critic to Confidence: PPO for Language-Based Quantitative Prediction with Confidence Estimation](http://arxiv.org/abs/2607.12687v1)
  <details><summary>📄 Abstract</summary>
  LLMs can perform language-based quantitative prediction from unstructured inputs, but remain susceptible to hallucinations and overconfident errors, making it critical to know not only what a model predicts, but when its predictions can be trusted. We introduce CARE-PPO, a reinforcement learning framework that establishes a connection between loss prediction for uncertainty estimation and actor-critic PPO fine-tuning, enabling joint learning of accurate numerical estimates and reliable confidenc...
  </details>

- **2026-07-14** — Rwik Rana, Jesse Quattrociocchi, Christian Ellis et al. — [Adapting Generalist Vehicle Models for High-Speed MPC Across Terrains](http://arxiv.org/abs/2607.13319v1)
  <details><summary>📄 Abstract</summary>
  High-speed off-road autonomy requires precise closed-loop control for a target vehicle while remaining robust across changing terrains. Recent forward kinodynamic (FKD) prediction foundation models suggest a promising path, starting from a generalist model and specializing it to the target platform. However, effective specialization remains challenging, as it often requires substantial real-world data, and models adapted to one setting can still overfit to specific terrains or driving regimes. W...
  </details>

- **2026-07-14** — Bidyarthi Paul, Nahida Jannat Mayouree, Md. Asif Karim et al. — [GSM-Plus-BN: A Perturbation-Based Benchmark for Bangla Mathematical Reasoning in Large Language Models](http://arxiv.org/abs/2607.13248v1)
  <details><summary>📄 Abstract</summary>
  The evaluation of mathematical reasoning in large language models (LLMs) has predominantly focused on high-resource languages like English. This has created a significant barrier to the equitable development and deployment of AI in linguistically diverse regions such as Bangladesh, where over 230 million people speak Bengali. Despite this global significance, there has been minimal prior work on mathematical reasoning in Bengali and no existing research that systematically benchmarks a perturbat...
  </details>

- **2026-07-14** — Zhouchonghao Wu, Akshay Rangesh, Weixin Li et al. — [TerraZero: Procedural Driving Simulation for Zero-Demonstration Self-Play at Scale](http://arxiv.org/abs/2607.13028v1)
  <details><summary>📄 Abstract</summary>
  Training robust autonomous driving agents requires a simulator that is fast enough for reinforcement learning at scale, realistic enough to ground behavior in real-world map structure, and diverse enough to cover the safety-critical long tail that logged data rarely contains. We present TerraZero, a procedural driving simulator and self-play training stack. A configurable C engine runs simulation on the CPU and policy inference on the GPU over a zero-copy path, sustaining 1.3M agent-steps per se...
  </details>

- **2026-07-14** — Zhao Yang, Yinan Shi, Mingyuan Yao et al. — [ChunkFlow: Towards Continuity-Consistent Chunked Policy Learning](http://arxiv.org/abs/2607.12992v1)
  <details><summary>📄 Abstract</summary>
  Vision-language action (VLA) models increasingly adopt chunked action heads to satisfy real-time constraints; however, this introduces boundary jitter: overlapping regions between consecutive chunks often yield inconsistent predictions, degrading temporal coherence and the task success rate. Existing methods, such as inference-time blending, merely reweight mismatched proposals without correcting underlying errors, leading to residual accumulation under biased or noisy histories. We propose Chun...
  </details>

- **2026-07-14** — Yanzhe Zhang, Sanmi Koyejo, Diyi Yang — [The Illusion of Robustness: Aggregate Accuracy Hides Prediction Flips under Task-Irrelevant Context](http://arxiv.org/abs/2607.12963v2)
  <details><summary>📄 Abstract</summary>
  As large language models (LLMs) grow more capable, they are increasingly deployed in context-rich settings where task inputs are often accompanied by long, partially irrelevant context. In a controlled setting, we find that state-of-the-art models often appear robust to task-irrelevant context at the aggregate level: prepending it to benchmark questions causes little change in overall accuracy. This aggregate stability, however, masks significant per-example instability. Even semantically meanin...
  </details>

- **2026-07-14** — Yilun Kong, Yunpeng Qing, Guozheng Ma et al. — [ExToken: Structured Exploration for Efficient Vision-Language-Action Reinforcement Fine-tuning](http://arxiv.org/abs/2607.12931v1)
  <details><summary>📄 Abstract</summary>
  Reinforcement Learning (RL) has demonstrated significant potential for improving Vision-Language-Action (VLA) models on complex manipulation tasks. However, its practical scalability remains severely limited by the substantial cost of environmental interactions. In this work, we first investigate the exploration stagnation bottleneck in current VLA-RL frameworks and reveal that trajectory diversity is fundamentally more important to sample efficiency than the sheer quantity of collected rollouts...
  </details>

- **2026-07-14** — Xixuan Hao, Zeyu Zhang, Zehao Lin et al. — [MemOps: Benchmarking Lifecycle Memory Operations in Long-Horizon Conversations](http://arxiv.org/abs/2607.12893v1)
  <details><summary>📄 Abstract</summary>
  Long-term memory has become a foundational capability for LLM-based agents that accompany users across extended, multi-session interactions. Existing benchmarks, however, evaluate such memory almost exclusively through downstream question answering, scoring only the correctness of a final answer. This black-box formulation conflates the heterogeneous causes of memory failure, such as missing the introduction of a relevant fact, binding an operation to the wrong target, or relying on stale values...
  </details>

- **2026-07-14** — Peter R. D. van der Wal, Nicola Strisciuglio, George Azzopardi — [Inhibited Self-Attention: Sharpening Focus in Vision Transformers](http://arxiv.org/abs/2607.12881v1)
  <details><summary>📄 Abstract</summary>
  Vision Transformers (ViTs) have demonstrated remarkable performance in computer vision tasks. However, their self-attention mechanism often diffuses focus across background regions, relying on spurious correlations rather than object-relevant cues. Inspired by inhibitory mechanisms observed in biological vision systems, we propose the Inhibited Self-Attention (ISA), a novel self-attention that integrates inhibitory signals to enhance feature selectivity and suppress spurious responses. In contra...
  </details>

- **2026-07-14** — Takumi Shioda, Kohei Terashima, Tatsuo Nagai — [Verifier-Based Reinforcement Fine-Tuning of Reasoning Models for Thermal Energy Storage Control](http://arxiv.org/abs/2607.12856v1)
  <details><summary>📄 Abstract</summary>
  Buildings are expected to shift cooling loads in response to grid conditions. Thermal energy storage (TES) enables this shift, but scheduling it well requires planning hours ahead under storage constraints. Model predictive control (MPC) and reinforcement learning are difficult to scale across buildings. This study instead adapts an open-weight reasoning model through reinforcement learning with verifiable rewards (RLVR). We convert exact offline dynamic-programming (DP) action values into dense...
  </details>

- **2026-07-14** — Tapan Parikh — [The One-Word Census: Answer-Choice Conformity Across 44 Language Models](http://arxiv.org/abs/2607.12796v1)
  <details><summary>📄 Abstract</summary>
  When a language model must pick one answer from a large space of equally valid options, which does it pick -- and how often is it the same answer every other model picks? Asked to "pick a word -- any word," 44 models chose "serendipity" 41% of the time. We characterize this convergence with a deliberately minimal instrument: 31 single-turn prompts, each naming a category with many valid one-word answers ("Name a tree."), asked four times per model with no system prompt. Analysis is exact-match o...
  </details>

- **2026-07-14** — Samuel Yeh, Yiwen Zhu, Shaleen Deep et al. — [Tracing Agentic Failure from the Flow of Success](http://arxiv.org/abs/2607.12747v1)
  <details><summary>📄 Abstract</summary>
  Failure attribution for LLM-based agentic systems, i.e., identifying which steps in a failure trajectory caused the task to fail, is critical for debugging and improving these systems. Existing approaches either rely on prompting-based pipelines, which are computationally expensive, or require post-training on failure trajectories with step-level error annotations, which are costly to collect and difficult to scale. We argue that a practical failure attribution model should be lightweight and tr...
  </details>

- **2026-07-14** — Sarah Al-Shareeda, Gulcihan Ozdemir, Heung Seok Jeon — [Learning-based Probabilistic Load Forecasting with Post-hoc and In-model Uncertainty](http://arxiv.org/abs/2607.12730v1)
  <details><summary>📄 Abstract</summary>
  Smart-building load forecasters are often trained offline on dense, multivariate, high-frequency data, but deployment may provide only hourly, feature-limited inputs. Missing features must then be reconstructed, and their errors can propagate through the model. If this input uncertainty is not reflected, prediction intervals may become miscalibrated, affecting demand-response scheduling. Our work examines where uncertainty should be placed once inference inputs are reconstructed. We develop a un...
  </details>

- **2026-07-14** — Jiho Hong, Eunae Kang, Sanghyun Kim et al. — [Instance-Enriched Semantic Maps for Visual Language Navigation](http://arxiv.org/abs/2607.12630v1)
  <details><summary>📄 Abstract</summary>
  Visual Language Navigation (VLN) aims to enable an embodied agent to navigate complex environments by following natural language instructions. Recent approaches build semantic spatial maps and leverage Large Language Models (LLMs) for reasoning and decision making. Despite these advances, existing systems lack instance-level object detail and robustness to diverse user queries, limiting reliable navigation in complex indoor environments. To address these limitations, we propose Instance-Enriched...
  </details>

- **2026-07-14** — Rui Zheng, Changwen Li, Yi Ji et al. — [Hierarchical Fault Localization for Autonomous Driving Systems with Hypothesis Validation and Intent Analysis](http://arxiv.org/abs/2607.12598v1)
  <details><summary>📄 Abstract</summary>
  Comprehensive testing is essential for the safety and reliability of Autonomous Driving Systems (ADS). Existing techniques can detect system-level failures or attribute them to coarse-grained modules, but they often fall short of localizing the root cause in source code. As a result, debugging remains labor-intensive, requiring developers to connect behavioral violations with complex implementation logic. To address this gap, we present HINT, a two-phase framework for hierarchical ADS fault loca...
  </details>

- **2026-07-14** — Cheng-You Ho, Justin Luo, Henry Ng et al. — [Clifford-Only Quantum Reed-Solomon Codes and a Tornado Concatenation for Biased-Noise Cat Qubits](http://arxiv.org/abs/2607.13105v1)
  <details><summary>📄 Abstract</summary>
  Dissipative cat qubits exponentially suppress one Pauli error channel with the mean photon number, leaving the conjugate bit-flip error as the dominant failure mode. This strong noise bias makes the full machinery of general quantum error correction unnecessary: a code need only protect against a single error type, and any classical linear code can be promoted to a Clifford stabilizer code that does exactly this. We use this observation to build a Clifford-only quantum Reed-Solomon (RS) code. St...
  </details>

- **2026-07-14** — Rongxin Gao, Yuzhi Huang, Dongxuan Liu et al. — [DynTrace: Tracking Dynamic Object Evidence for 4D Spatio-Temporal Reasoning in MLLMs](http://arxiv.org/abs/2607.12503v2)
  <details><summary>📄 Abstract</summary>
  4D spatio-temporal reasoning, jointly modeling 3D spatial structure and temporal evolution, is essential for understanding dynamic worlds and enabling embodied interaction. While current Multimodal Large Language Models (MLLMs) show strong capabilities in static scene understanding and coarse-grained 4D tasks, they still have notable limitations in continuous dynamic scene perception, especially in tracking dynamic object evidence for coherent 4D spatio-temporal reasoning. This shortcoming stems...
  </details>

- **2026-07-14** — Jeeyung Kim, Erfan Esmaeili, Qiang Qiu — [Steering Diffusion Models via Class-Contrastive Influence for Few-Shot Medical Classification](http://arxiv.org/abs/2607.12464v1)
  <details><summary>📄 Abstract</summary>
  When labeled data are scarce, off-the-shelf diffusion models can augment training sets for few-shot medical image classification, but not all generated samples are equally useful for the downstream task. Existing approaches largely improve synthetic data by increasing realism, diversity, or domain adaptation, while overlooking a more fundamental question: how should sample usefulness for classification be measured and optimized? We address this with Class-Contrastive Influence (C2I), a criterion...
  </details>

- **2026-07-14** — Jie Mao, Changlun Li, Xiang Li et al. — [EVOQUANT: Self-Evolving Verifier-Guided Strategy Optimization for Robust Quantitative Trading](http://arxiv.org/abs/2607.12455v1)
  <details><summary>📄 Abstract</summary>
  Quantitative strategy optimization remains largely manual, requiring domain experts to identify weak signals, tune risk-control rules, and repeatedly validate iterative revisions. Large language models can accelerate this process, but directly relying on them to rewrite trading strategies often introduces hallucinated edits, strategy drift, and backtest overfitting. We propose EVOQUANT, a self-Evolving Verifier-guided framework for strategy Optimization in Quantitative trading. Our method utiliz...
  </details>

- **2026-07-14** — Timing Yang, Jinrui Yang, Xinlong Li et al. — [Let RGB Be the Language of Vision](http://arxiv.org/abs/2607.12450v1)
  <details><summary>📄 Abstract</summary>
  This work introduces a unified formulation for vision models, where diverse forms of visual information beyond natural images, such as masks, depth maps, and other structured visual signals, are all represented as RGB images, while general visual tasks can be converted into a common RGB-to-RGB image editing problem. In this paradigm, different types of visual information internally share the same encoding and decoding architecture and parameters as natural images, enabling a single model to tran...
  </details>

- **2026-07-14** — Arash Nikzad, Sasan Sarbishegi, Ali Dasmeh et al. — [Differentiable Clone-Structured Causal Graphs for End-to-End Cognitive Map Learning from Image Sequences](http://arxiv.org/abs/2607.12382v1)
  <details><summary>📄 Abstract</summary>
  How can an agent build a structured map of its world from nothing but an ongoing sequence of raw sensory input and its own movements, especially when natural variation means exact sensory patterns rarely repeat? The Clone-Structured Causal Graph algorithm (CSCG), a normative hippocampus model, shows how an interpretable map can be learned from aliased observations. However, CSCG requires a predefined discrete alphabet, and its expectation-maximization formulation is not easily combined with exis...
  </details>

- **2026-07-14** — Hung-Chieh Wu, Xiaopan Zhang, Kasra Sinaei et al. — [StratMamba: Strategic and Reactive Stream Partitioning for Path-Efficient LiDAR-Based Obstacle Avoidance](http://arxiv.org/abs/2607.12370v1)
  <details><summary>📄 Abstract</summary>
  This paper proposes StratMamba, a dual-stream Mamba-based temporal modeling architecture, to more efficiently capture long-horizon temporal dependencies required for robot navigation in complex and obstacle-rich environments. StratMamba leverages a combination of fast-decay and slow-decay memory architectures, where the fast-decay component processes high-frequency LiDAR data for reactive obstacle avoidance, while the slow-decay component maintains longer-horizon goal information for strategic p...
  </details>

- **2026-07-14** — Xinyue Xu, Zheng Zhang, Kunyang Ma et al. — [DM-KG: A Novel Method for Boosting Spatial Cognition of Vision-Language Models in Street View Imagery](http://arxiv.org/abs/2607.12319v1)
  <details><summary>📄 Abstract</summary>
  As vision-language models (VLMs) are increasingly deployed in geospatial question answering and visual scene understanding, improving their spatial cognition capability on street view imagery for complex logical reasoning has emerged as a key research priority. However, existing VLMs frequently suffer from "spatial semantic hallucinations" when perceiving object locations, distances, and directions in real-world street view scenes. Furthermore, such errors are often recalcitrant to tracing and c...
  </details>

- **2026-07-14** — Michael Solodko, Steven Gong, Guangwei Yu et al. — [LakeQuest: A Three-Domain Benchmark for Grounded Question Answering across Data Lakes](http://arxiv.org/abs/2607.12310v1)
  <details><summary>📄 Abstract</summary>
  While modern question answering (QA) systems excel on clean, schema-aligned corpora, real-world knowledge is rarely so neatly packaged. Answering questions over enterprise and scientific data lakes requires systems to navigate heterogeneous, weakly structured collections of tables, passages, and linked metadata. Current benchmarks abstract away this noisy discovery process, failing to evaluate end-to-end performance. To bridge this gap, we introduce LakeQuest, a human-validated benchmark of 9,84...
  </details>

- **2026-07-14** — Muhammad Ashad Kabir, Sirajam Munira — [From Many to Meaningful: Feature-Guided Zero-Shot Chronic Kidney Disease Screening Using Large Language Models](http://arxiv.org/abs/2607.12260v1)
  <details><summary>📄 Abstract</summary>
  Early screening of chronic kidney disease (CKD) is essential for preventing irreversible progression; however, many machine learning (ML)-based screening methods remain difficult to deploy in community and resource-limited screening settings due to their reliance on large labeled datasets, resource-intensive pathology tests, or high-dimensional clinical features, and limited robustness to population and distributional shifts. This study examines the feasibility of using large language models (LL...
  </details>

- **2026-07-14** — Vinay Kumar Chaganti — [On-Device Deep Research at 4B: Exposure Bounds Faithfulness, Retrieval Bounds Coverage](http://arxiv.org/abs/2607.12257v1)
  <details><summary>📄 Abstract</summary>
  On-device research agents search a corpus, read sources, and write a cited brief on a personal laptop. Whether their citations are faithful, and at what cost, is unmeasured for a deployable small model. This study fixes one 4B generator on a 24 GB laptop and asks what makes its citations faithful. It separates two quantities usually reported as one number. Cited claim faithfulness asks whether the cited source supports the claim. Trustworthy coverage asks whether the agent also cites the right s...
  </details>

- **2026-07-13** — Aritra Mazumder, Nusrat jahan Lia — [AgentCheck: A Reproduce-Intervene-Mitigate Workbench for LLM Agents over MCP](http://arxiv.org/abs/2607.11098v3)
  <details><summary>📄 Abstract</summary>
  Tool-using LLM agents are mostly evaluated assuming all tools work. When a tool times out, returns a week-stale value, or has its description poisoned in deployment, the developer needs a controlled way to reproduce the failure, test a fix, and confirm the fix worked before deployment. We present AgentCheck, an open-source web workbench that turns an MCP server into an intervention surface. AgentCheck runs an agent against its real tools and records every tool response, then re-runs the agent wi...
  </details>

- **2026-07-13** — Preet Jhanglani, Zeel Kaushal Desai, Vidhi Kansara et al. — [Beyond Test Presence: Assessing the Quality and Robustness of Agent-Generated Tests in Open-Source Projects](http://arxiv.org/abs/2607.12068v1)
  <details><summary>📄 Abstract</summary>
  The integration of AI-powered coding agents into Continuous Integration/Continuous Delivery (CI/CD) pipelines has fundamentally altered how software verification is conducted. While these agents successfully automate the test generation, current evaluation benchmarks (e.g., SWE-bench) largely focus on pass-rates rather than the intrinsic quality of the generated tests. This raises the possibility of "stealth technical debt", in which test suites pass execution but do not offer comprehensive cove...
  </details>

- **2026-07-13** — Samer Saab, Chaouki Abdallah — [Graph Feedback Controls Consensus and Clique Formation in Open-Weight Language-Model Populations](http://arxiv.org/abs/2607.12077v1)
  <details><summary>📄 Abstract</summary>
  Multi-agent language-model systems increasingly route local interactions, yet the runtime interaction graph is often treated as an implementation detail. We study convention formation in open-weight LM populations spanning 1.1B-32B parameters with a naming-game protocol. Restricted first-token scores over tokenizer-safe labels let us measure prompt-conditioned score-state distributions, construct state-similarity graphs, and separate sampled-label agreement from latent state-space consensus. Acr...
  </details>

- **2026-07-13** — Fangxia An, Fatemeh S. Tabatabaei, Nick Seymour et al. — [Tracing cosmic star formation history through radio continuum spectral energy distribution and non-thermal emission](http://arxiv.org/abs/2607.12073v1)
  <details><summary>📄 Abstract</summary>
  As a tracer of massive star formation unaffected by dust, the radio continuum emission provides a unique window into the formation of the first stars and galaxies in the Universe. Recent observations show that the integrated rest-frame mid-radio (~1-10 GHz) luminosity of galaxies serves as one of the most robust tracers of the star formation rate (SFR). These studies further demonstrate that the synchrotron spectral index and the shape of the radio spectral energy distribution (SED) evolves with...
  </details>

- **2026-07-13** — Said Elnaffar, Farzad Rashidi — [Designing Agent-Ready Websites for AI Web Agents: A Framework for Machine Readability, Actionability, and Decision Reliability](http://arxiv.org/abs/2607.12056v1)
  <details><summary>📄 Abstract</summary>
  Online shopping is increasingly shifting toward a model in which AI agents independently search for products, compare options, evaluate constraints, and carry out parts of the purchasing process for users. Website design must now support both human and agent-mediated interaction. This paper introduces the agent-ready website, a design framework for enhancing the readability, interpretability, verifiability, and actionability of e-commerce platforms for AI agents. Existing web design, SEO, and ge...
  </details>

- **2026-07-13** — A. Krylov, D. Rakhov, V. Veselova et al. — [LLM-Guided Program Evolution for Targeted Black-Box Attacks on Perceptual Hash Algorithms](http://arxiv.org/abs/2607.11472v1)
  <details><summary>📄 Abstract</summary>
  Perceptual hash algorithms (PHAs) are widely deployed to detect image forgery under benign transformations, yet their robustness against adversarially chosen perturbations remains poorly understood and rarely comes with provable guarantees. We propose a novel evolutionary framework based on GigaEvo and OpenEvolve for targeted second-image attacks on perceptual hash algorithms. We assess attack performance using a composite score that jointly accounts for the fraction of adversarial images whose ...
  </details>

- **2026-07-13** — Anqi Li, Jie Zhang, Zhongqi Wang et al. — [DeepBias: Adaptive In-depth Probing of Social Biases in LVLMs](http://arxiv.org/abs/2607.11228v1)
  <details><summary>📄 Abstract</summary>
  While Large Vision-Language Models (LVLMs) demonstrate remarkable capabilities, they remain highly susceptible to embedded social biases. Existing bias evaluation protocols predominantly rely on static datasets, which provide only a superficial assessment, as their fixed test cases cannot adaptively evolve to measure the true depth and limits of model vulnerabilities. We introduce DeepBias, an adaptive framework for the in-depth probing of social biases in LVLMs with carefully designed agents. O...
  </details>

- **2026-07-13** — Aritra Mazumder, Nusrat jahan Lia — [AgentCheck: A Reproduce-Intervene-Mitigate Workbench for LLM Agents over MCP](http://arxiv.org/abs/2607.11098v1)
  <details><summary>📄 Abstract</summary>
  Tool-using LLM agents are mostly evaluated assuming all tools work. When a tool times out, returns a week-stale value, or has its description poisoned in deployment, the developer needs a controlled way to reproduce the failure, test a fix, and confirm the fix worked before deployment. We present AgentCheck, an open-source web workbench that turns an MCP server into an intervention surface. AgentCheck runs an agent against its real tools and records every tool response, then re-runs the agent wi...
  </details>

- **2026-07-13** — Georgios Piliouras, Ian Gemp, Siqi Liu et al. — [Paradoxes of Game Theoretic Equilibria and Price of Anarchy](http://arxiv.org/abs/2607.11752v1)
  <details><summary>📄 Abstract</summary>
  For decades, static solution concepts (Nash, Correlated, and Coarse Correlated Equilibria) and the Price of Anarchy (PoA) have formed the bedrock of algorithmic game theory, with no-regret learning proving fast convergence to such game-theoretic equilibria. We show that reducing multi-agent learning to static equilibrium and black-box regret analysis obscures underlying dynamic disequilibrium and game theoretic bounds.   First, interior Nash equilibria lack $C^1$ vector field information, meanin...
  </details>

- **2026-07-13** — Xuefeng Li, Pengfei Liu — [UMoE:Unlocking Every Expert in Domain-Specific Training](http://arxiv.org/abs/2607.11444v1)
  <details><summary>📄 Abstract</summary>
  Mixture-of-Experts (MoE) models scale capacity without proportional compute cost and have become a key architecture for frontier large language models (LLMs). Yet domain-specific post-training inherits an expert pool shaped by mixed-domain pre-training: a substantial subset of experts contributes little on the target domain, and standard supervised fine-tuning (SFT) leaves the composition of this pool unchanged. We propose a simple, budget-preserving pipeline that realigns the expert pool to the...
  </details>

- **2026-07-13** — Haojie Huang, Linfeng Zhao, Haotian Liu et al. — [Pix2Act: Image-Space Manipulation Policies with Equivariant Augmentation](http://arxiv.org/abs/2607.11167v1)
  <details><summary>📄 Abstract</summary>
  Representing manipulation actions as 2D trajectories in the camera plane provides a compact and interpretable basis for learning complex 3D manipulation policies. However, it also creates challenges from out-of-frame trajectories and limited precision. We propose Pix2Act, an imitation learning method that addresses these challenges by generating continuous image-space keypoint trajectories in each camera plane and losslessly recovering end-effector poses via triangulation. This reformulates high...
  </details>

- **2026-07-13** — Pei Chen, Baichao An, Mengying Wu et al. — [Rethinking MCP Security: A Large-Scale Study of Runtime MCP Servers and Security Scanner Reliability](http://arxiv.org/abs/2607.11086v1)
  <details><summary>📄 Abstract</summary>
  The Model Context Protocol (MCP) has rapidly established itself as a standard interface for enabling LLM-based agents to interact with external tools and services. As MCP servers are increasingly entrusted with security-sensitive operations, understanding their real-world risks has become critical. In practice, due to the absence of large-scale runtime MCP servers, such understanding largely relies on security scanners applied to a small number of cases, yet the reliability of these assessments ...
  </details>

- **2026-07-13** — Xinghang Li, Jun Guo, Qiwei Li et al. — [Xiaomi-Robotics-U0: Unified Embodied Synthesis with World Foundation Model](http://arxiv.org/abs/2607.11643v1)
  <details><summary>📄 Abstract</summary>
  Recent foundation image and video generation models offer strong generalization and controllability, but their direct application to embodied scenarios is limited by requirements for multi-view consistency, geometric coherence, and robot embodiment constraints. Existing methods typically adapt foundation models with limited robot data, often sacrificing visual knowledge acquired during large-scale pre-training. We present Xiaomi-Robotics-U0, a 38-billion-parameter multimodal autoregressive model...
  </details>

- **2026-07-13** — Jihong Chen — [Relational Positioning as a Measurable Risk Object: History-Carried Lock-in and Self-Confabulation in Multi-Turn Human-AI Dialogue](http://arxiv.org/abs/2607.11437v1)
  <details><summary>📄 Abstract</summary>
  In long, multi-turn dialogue a large language model maintains an implicit relational stance toward the user, spanning from "push the user toward real-world others" to "position itself as the user's sole support." When it slides toward the latter, "support" degrades into "you only have me" -- a harm documented in real companion conversations (Moore et al., 2026). We define and validate a measure of this stance, relational positioning (D1), and use it to characterize the stance under controlled co...
  </details>

- **2026-07-13** — Mingyue Huo, Yuheng Zhang, Hao Zhang — [Where Speech Enhancement Hurts Recognition: An Inference Time Polar Projection Diagnosis](http://arxiv.org/abs/2607.11157v1)
  <details><summary>📄 Abstract</summary>
  Speech enhancement (SE) can substantially improve perceptual quality, yet enhanced speech does not necessarily improve automatic speech recognition (ASR). Existing remedies, such as retraining the enhancer jointly with recognizer or interpolating enhanced speech with the noisy input, can mitigate this mismatch, but common explanations such as artifacts and over-suppression remain qualitative and do not localize which enhancement component harms recognition. We propose inference time polar projec...
  </details>

- **2026-07-13** — Shijie Wang, Honglu Zhou, Ziyang Wang et al. — [Evidence-Backed Video Question Answering](http://arxiv.org/abs/2607.11862v1)
  <details><summary>📄 Abstract</summary>
  Current Video Large Language Models (Video LLMs) excel in question answering (QA) but largely operate as black boxes, providing textual answers without verifiable visual grounding. Existing explainability efforts rely on textual rationales or sparse bounding boxes, which struggle to capture complex video dynamics such as occlusions and non-rigid deformations. We propose Evidence-Backed Video Question Answering (E-VQA), a novel task requiring models to jointly output a semantic answer and precise...
  </details>

- **2026-07-13** — Ziyue Jiang, Dake Guo, Zekai Zhang et al. — [Qwen-Audio-VAE Technical Report](http://arxiv.org/abs/2607.11738v1)
  <details><summary>📄 Abstract</summary>
  We introduce \textbf{Qwen-Audio-VAE}, a suite of low-bitrate, fast-encoding continuous audio autoencoders designed for scalable general audio generation. The model is built around a simple but important principle: an audio VAE should not only reconstruct diverse audio with high fidelity, but also produce compact latent representations fast enough to support large-scale text-to-audio training. Qwen-Audio-VAE combines a causal encoder-decoder, window Transformer blocks, and multi-discriminator tra...
  </details>

- **2026-07-13** — Aastha Sharma, Guangjing Wang — [VoxENES 2026: Benchmarking Generalization of Speech Spoofing Detectors Against LLM-Era TTS and Voice Conversion](http://arxiv.org/abs/2607.11706v1)
  <details><summary>📄 Abstract</summary>
  Modern LLM-driven text-to-speech (TTS) and voice conversion (VC) systems produce synthetic speech that differs from the generators represented in many legacy spoofing benchmarks. This mismatch creates a temporal generalization gap that can overestimate detector robustness under real-world post-processing conditions. We bridge this gap by introducing VoxENES 2026, a bilingual (English and Spanish) benchmark of 53,628 audio samples generated using 10 contemporary speech synthesis methods and evalu...
  </details>

- **2026-07-13** — Yi-You Yang — [Robust Welfare Decentralization under Population Entry](http://arxiv.org/abs/2607.11658v1)
  <details><summary>📄 Abstract</summary>
  We ask when an incumbent economy with indivisible goods can accommodate an arbitrary new participant while retaining an efficient allocation supported by anonymous item prices. We call this property universal entry robustness. An economy is universally entry-robust if and only if its aggregate welfare valuation is additive. Although the requirement quantifies over all entrant valuations, it can be tested using one canonical entrant whose value for a bundle equals the loss in maximal incumbent we...
  </details>

- **2026-07-13** — Christelle Schneuwly Diaz, Narmina Baghirova, Duy-Thanh Vu et al. — [Imputation-free transformer learning enables robust Alzheimer's disease prediction and calibrated uncertainty quantification across heterogeneous clinical cohorts](http://arxiv.org/abs/2607.11656v1)
  <details><summary>📄 Abstract</summary>
  Accurate diagnostic classification and disease-severity prediction for Alzheimer's disease are hampered by the incompleteness and heterogeneity of real-world clinical data. Left unaddressed, these barriers prevent reliable disease modelling and hinder effective clinical evaluation. Conventional imputation strategies introduce systematic bias, distort inter-feature relationships, and yield overconfident predictions, limitations especially consequential in diagnostic settings. Here, we propose NIT...
  </details>

- **2026-07-13** — Ye Yuan, Kehan Chen, Xinqiang Yu et al. — [DA-Nav: Direction-Aware City-Scale Vision-Language Navigation](http://arxiv.org/abs/2607.11638v1)
  <details><summary>📄 Abstract</summary>
  City-scale outdoor navigation is currently hindered by the heavy reliance on dense maps or costly navigation supervision. In this work, we introduce a novel paradigm for leveraging directional instructions from commercial navigation tools (e.g., Google Maps). To bridge the gap between commercial instructions and executable navigation actions, while mitigating long-horizon error accumulation through robust trajectory recovery, we propose DA-Nav, a Direction-Aware vision-language Navigation framew...
  </details>

- **2026-07-13** — Yikang Chen, Zhengkang Guan, Haoyuan Qian et al. — [DAG-FM: A Foundation Model for Causal Discovery under Heterogeneous Causal Mechanisms](http://arxiv.org/abs/2607.11510v1)
  <details><summary>📄 Abstract</summary>
  Causal discovery from observational tabular data remains fundamentally challenging, primarily due to the heterogeneity of underlying causal mechanisms and the high-dimensional combinatorial search space of Directed Acyclic Graphs (DAGs). In this paper, we propose \textbf{DAG-FM}, a novel foundation model architecture that amortizes causal discovery. Unlike direct matrix prediction, DAG-FM decomposes the causal discovery process into two auto-regressive stages using two specialized Transformer-ba...
  </details>

- **2026-07-13** — Dmitry Nikolaev — [Are LLMs ready for HardChoices?](http://arxiv.org/abs/2607.11471v1)
  <details><summary>📄 Abstract</summary>
  A lot of research attention has been devoted to checking whether large language models (LLMs) are politically biased. This work has largely focused on high-level ideological dimensions, such as left--right or progressive--conservative, and it has been shown that while LLMs are predominantly left and progressive leaning, largely mimicking the biases in the training data, they can be to some extent steered to change their preferences in post-training. In this short note, we check if LLMs have robu...
  </details>

- **2026-07-13** — Roberta Rocca, Sami Boukortt, Geoff Keeling et al. — [Beyond Sally-Anne: Evaluating Theory of Mind in LLMs using Epistemic Schelling Points](http://arxiv.org/abs/2607.11363v1)
  <details><summary>📄 Abstract</summary>
  Text-based evaluations of Theory of Mind (ToM) in Large Language Models (LLMs) often involve cognitive tests akin to the Sally-Anne task that can be gamed due to exposure to relevantly similar tasks in pre-training and do not obviously test models' functional ToM abilities in ways that generalize to naturalistic settings. To address these issues, we introduce the Epistemic Asymmetry Schelling Task (EAST), a two-player dialogue game designed to benchmark robust and generalizable ToM abilities. By...
  </details>

- **2026-07-13** — David Otero, Javier Parapar — [User Preference Induction with LLMs for Offline Top-N Recommendation Evaluation](http://arxiv.org/abs/2607.11354v1)
  <details><summary>📄 Abstract</summary>
  Offline evaluation is the standard methodology for comparing top-N recommender systems, yet it relies on incomplete relevance information. In most benchmark datasets, only a small subset of user--item preferences is observed, and unjudged items are commonly treated as non-relevant. This missing-as-negative assumption can bias evaluation, penalize plausible recommendations with no recorded feedback, and favour algorithms that concentrate on popular or highly exposed items. We propose an LLM-based...
  </details>

- **2026-07-13** — Zhuo Xiao, Bo Liu, Jingjing Wang et al. — [Multi-Catheter Digitization in Brachytherapy via Few-Shot Synthetic-to-Real Learning and Structure-Aware Tracking](http://arxiv.org/abs/2607.11290v1)
  <details><summary>📄 Abstract</summary>
  Accurate catheter digitization in CT-guided interstitial brachytherapy is a critical but time-consuming task, especially for complex implant configurations. We developed a data-efficient, physics-guided framework for automated multi-catheter digitization with minimal clinical annotation. The pipeline consists of two stages. First, an implant region-aware network was pretrained on synthetic CT volumes with simulated metallic signatures and then fine-tuned using only 10 clinical cases. Second, a s...
  </details>

- **2026-07-13** — Ruoxuan Zhang, Qiyun Zheng, Siyu Wu et al. — [RetroHolmes: When Semantic Plausibility Fails Retrospective Physical Process Reasoning](http://arxiv.org/abs/2607.11044v1)
  <details><summary>📄 Abstract</summary>
  Humans can infer hidden physical processes from sparse observations, yet current evaluation protocols for Vision Language Models fail to assess whether such physical reasoning is genuinely captured. To address this gap, we introduce Retrospective Physical Process Reasoning, a new evaluation paradigm to reason backward from outcomes under explicit physical constraints. Building on the paradigm, we present RetroHolmes, the first real-world benchmark for Retrospective Physical Process Reasoning, co...
  </details>

- **2026-07-13** — Jin-Kang Guo, Jia Li, Jin-Lei Wu et al. — [Non-Abelian holonomic transformations in digitally coupled acoustic waveguides guided by the global adiabatic criterion](http://arxiv.org/abs/2607.11000v1)
  <details><summary>📄 Abstract</summary>
  An acoustic platform is validated for implementing compact non-Abelian holonomic transformations (NHTs) guided by a global adiabatic criterion (GAC). A tripod model is mapped onto a digitally coupled four-waveguide structure, where designed coupling envelopes and an acoustically-induced-transparency phase-control module implement a two-stage phase-stitched holonomic evolution. Compared with a reference Gaussian envelope, the GAC-guided power-law profile flattens the spatial distribution of the g...
  </details>

- **2026-07-13** — Zheng Zeng, Deepak Sridhar, Nuno Vasconcelos — [MED-DSLC: Multi-Expert-Domain Classification via Domain Supervision and Logit Calibration](http://arxiv.org/abs/2607.10985v1)
  <details><summary>📄 Abstract</summary>
  Vision-language models (VLMs) such as CLIP enable zero-shot classification by comparing image features with text prompts in a shared embedding space. A fundamental property underlying this capability is the global comparability of logits across arbitrary candidate classes. However, VLMs are often adapted to fine-grained domains using techniques such as LoRA. While this improves in-domain accuracy, out-of-domain accuracy degrades. This leads to a highly fragmented model ecosystem, with thousands ...
  </details>

- **2026-07-12** — Saadeldine Eletter, Owais Aijaz, Preslav Nakov — [Trust Before Fusion: QIMG-7 and Source-Aware Resolution for Polluted Multimodal RAG](http://arxiv.org/abs/2607.10798v1)
  <details><summary>📄 Abstract</summary>
  Multimodal retrieval-augmented generation (RAG) is often evaluated with clean evidence, yet real retrieval can return topically relevant but unreliable content: false text and misleading images from corrupted metadata, entity swaps, typographic overlays, semantic edits, adversarial patches, blends, or style transfer. We introduce QIMG-7, a controlled benchmark for multimodal retrieval pollution in multi-sentence factual QA, spanning four datasets, seven image-attack families, and 16 paired clean...
  </details>

- **2026-07-12** — Tong Nie, Yuewen Mei, Junlin He et al. — [World Models as Adversaries: Multi-Agent Self-Play Fine-Tuning for Robust Motion Planning](http://arxiv.org/abs/2607.10630v1)
  <details><summary>📄 Abstract</summary>
  Robust motion planning in dense traffic requires autonomous vehicles to interact in rare and safety-critical scenarios that are underrepresented in naturalistic driving data. Although adversarial training offers a feasible solution, existing methods often rely on external scenario generators, heuristic perturbations, or simulator-heavy rollouts, which makes them difficult to integrate with modern autoregressive planners. Here, we cast adversarially robust planner learning as a constrained min-ma...
  </details>

- **2026-07-12** — Sirine Ayadi, Sándor Daróczi, Stephan Günnemann et al. — [Reliability Scaling Laws for Quantized Large Language Models](http://arxiv.org/abs/2607.10855v1)
  <details><summary>📄 Abstract</summary>
  Quantization is a powerful strategy to build capable and resource-efficient large language models (LLMs) by reducing the bitwidth of the parameters. While quantized LLMs achieve state-of-the-art performance on unperturbed inputs using standard predictive metrics, their performance on perturbed inputs, measured using reliability metrics, remains underexplored, despite its importance for reliable deployment. To address this gap, we first conduct a comprehensive reliability evaluation of quantized ...
  </details>


### 📂 watermark
*水印与溯源 / Watermarking & Provenance* — 8 papers

- **2026-07-15** — Hyunkyung Han, Min Jung Kim — [Anatomically Faithful but Temporally Blind: Auditing Attribution for Left-Ventricular Ejection-Fraction Estimation from Echocardiography](http://arxiv.org/abs/2607.13738v1)
  <details><summary>📄 Abstract</summary>
  Background and Objective: Deep video models estimate left-ventricular ejection fraction (EF) from echocardiography with near-expert accuracy, and post-hoc attribution (Chefer relevance for transformers, Grad-CAM for CNNs) is increasingly used to certify that models "look at the right place." Yet whether these explanations are faithful both spatially and temporally is unaudited. Because EF is defined by the end-systolic (ES) and end-diastolic (ED) frames, a faithful explanation must localize the ...
  </details>

- **2026-07-14** — Binwen Liu, Yilin Ren — [Epistemic Stance Flexibility Probing: Measuring Prompt-Conditioned Register Shift in Large Language Models](http://arxiv.org/abs/2607.12739v1)
  <details><summary>📄 Abstract</summary>
  A language model may be asked either what experts believe about a contested claim or what it believes about the claim itself. A trustworthy conversational agent should distinguish these two requests and respond in different epistemic registers: neutral attribution in the first case and stance expression in the second. Whether such a shift occurs-and whether it occurs coherently-is not directly assessed by existing benchmarks for accuracy, instruction following, or safety. We introduce ESFP, a be...
  </details>

- **2026-07-14** — Igor Santos-Grueiro — [When Binaries Talk Back: Representation-Confusion Attacks on LLM-Assisted Reverse Engineering](http://arxiv.org/abs/2607.12507v1)
  <details><summary>📄 Abstract</summary>
  LLM-assisted reverse-engineering (RE) systems analyze strings, decompiler output, and tool reports derived from ttacker-controlled binaries. A binary can make data look like instructions or records from one origin look like independent evidence. We call such failures Representation-Confusion Attacks in Reverse Engineering (RARE): the pipeline promotes a correctly extracted observation to instruction authority, claim-validating evidence, or trusted analysis state without the authority or support ...
  </details>

- **2026-07-14** — Satwik Bathula, Anand A. Joshi — [Fisher Rank Inflation: A Spectral Signature of Memorization under Label Noise](http://arxiv.org/abs/2607.12438v1)
  <details><summary>📄 Abstract</summary>
  Deep networks trained with label noise often learn clean structure before memorizing corrupted labels. We show that this transition leaves a spectral signature in the centered scatter of per-example last-layer gradients. Its effective rank transiently expands during memorization and contracts after corrupted labels are fit. We call this phenomenon Fisher Rank Inflation. Corrupted labels increase effective rank by injecting spectral mass into low-energy or previously unused eigendirections, incre...
  </details>

- **2026-07-14** — Jixiang Luo — [XScientist: A Git-Like Research Protocol for Long-Running Autonomous Scientific Discovery](http://arxiv.org/abs/2607.12301v1)
  <details><summary>📄 Abstract</summary>
  Autonomous research systems are often evaluated as one-shot paper generators: given a topic, they produce a manuscript and a small set of experiment logs. This framing hides the operational problem that makes such systems difficult to trust: research is long-running, branching, failure-prone, and dependent on auditable handoffs between agents and humans. XScientist is a git-like research protocol and operating system for this setting. It orchestrates idea generation, experiment execution, manusc...
  </details>

- **2026-07-13** — Vincent Giap, Eric Wang, Cris Nguyen — [Measuring the Re-executability of Published Molecular Docking Claims](http://arxiv.org/abs/2607.12117v1)
  <details><summary>📄 Abstract</summary>
  Published molecular docking scores depend on the receptor, ligand, software, search box, seed, and preparation choices; a paper reporting only the score has published a number with unknowable provenance. We ask whether such claims can be re-executed from their own published records. We introduce MERS-Dock, a 16-field Minimum Executable Reporting Set, and a deterministic E0-E4 executability ladder over audited field states. In 236 open-access SARS-CoV-2 main-protease docking papers, only 8.1% met...
  </details>

- **2026-07-13** — Ke Xu, Han Xu, Xinran Chen et al. — [STAMP: Provenance-Guided Credit Assignment for Deep Search Agents](http://arxiv.org/abs/2607.11172v1)
  <details><summary>📄 Abstract</summary>
  Reinforcement learning for deep-search agents has largely focused on trajectory-level scoring -- outcome correctness, citation-aware rewards, and evidence coverage. Yet the actions that expose supporting documents receive no targeted credit, a gap we call the reward-credit mismatch. We propose STAMP, in which a reference-based verifier judges whether each cited document supports an entity or relation in a training-time evidence graph, and first-exposure attribution traces each supported citation...
  </details>

- **2026-07-12** — Obada Kraishan, Kulsawasd Jitkajornwanich, Kerk Kee — [Robo-Reporters: Evaluating Autonomous AI Agents as Algorithmic Gatekeepers in Computational Journalism](http://arxiv.org/abs/2607.10736v1)
  <details><summary>📄 Abstract</summary>
  Artificial intelligence agents increasingly perform journalism tasks autonomously, searching for sources, evaluating credibility, and producing news content with minimal human oversight. Yet research has largely treated AI as a monolithic category, leaving the effects of architectural design unexamined. Drawing on gatekeeping theory, this study presents the first systematic comparison of four agent architectures, monolithic (Claude), chain-based (LangChain), multi-agent collaborative (CrewAI), a...
  </details>


### 📂 unlearning
*机器遗忘 / Machine Unlearning* — 1 papers

- **2026-07-13** — Chenxi Sun, Minghui Liwang, Wusi He et al. — [HermesHFL: Incentive-Compatible Hierarchical Federated Unlearning for Dynamic LLM Fine-Tuning](http://arxiv.org/abs/2607.11528v1)
  <details><summary>📄 Abstract</summary>
  Hierarchical federated unlearning (HFUL) for large language model (LLM) fine-tuning faces significant challenges due to hierarchical aggregation, dynamic client participation, and strong parameter coupling in LLM adaptation. Selectively removing client contributions is particularly difficult because model updates propagate across multiple aggregation stages while unlearning requests may coincide with client departures and rejoining. To address these issues, we propose **HermesHFL**, a hierarchic...
  </details>


### 📂 benchmark
*安全评测与基准 / Safety Benchmarks & Evaluation* — 1 papers

- **2026-07-14** — Oleg Solozobov — [Agent-Safety Evaluations as Load-Bearing Evidence: A Vendor-Neutral, Cross-Harness Reconstructability Metric](http://arxiv.org/abs/2607.12469v1)
  <details><summary>📄 Abstract</summary>
  Many agent-safety evaluation results are not yet load-bearing evidence: identical nominal outcomes (task success, attack success, monitor scores) may sit atop materially different evidence regimes. No vendor-neutral, runnable instrument scores reconstructability as an evaluation-validity metric: whether captured evidence can reconstruct the decision a claim depends on. This paper introduces a property-level reconstructability metric over eight decision-property classes and a cross-harness adapte...
  </details>


### 📂 survey
*综述与系统化 / Surveys & Systematization* — 4 papers

- **2026-07-13** — Shelley Cazares — [The Emerging Paradigm of Geospatial Foundation Models: From Pre-Training to Agentic Reasoning](http://arxiv.org/abs/2607.12177v1)
  <details><summary>📄 Abstract</summary>
  The analysis of satellite and aerial imagery has entered a new era with the advent of foundation models. This paper describes the concept of Geospatial Foundation Models (GeoFMs), which are artificial intelligence/machine learning (AI/ML) models pre-trained on massive geospatial datasets through varied methodologies. We first articulate the core paradigm shift that GeoFMs enable: a separation of duties, where large-scale model providers perform the computationally intensive pretraining, allowing...
  </details>

- **2026-07-13** — Chunzheng Zhu, Lei Tian, Bohan Tan et al. — [The Path to Self-Evolving Clinical Systems: Scaling Medical Agents from Assistance to Autonomy](http://arxiv.org/abs/2607.11175v1)
  <details><summary>📄 Abstract</summary>
  The growing ability of large language models and vision language models to jointly interpret and reason over images and text is reshaping medical agents, moving them from task specific predictors toward autonomous systems that perceive, reason, plan, remember, and act in clinical environments. This work departs from the capability first perspective of existing literature and instead begins from clinical deployment, asking what tasks, contamination resistant benchmarks, and interactive training e...
  </details>

- **2026-07-13** — Zhengyang Bai, Cheng Chen, Fan Yang et al. — [Many-Body Physics with Rydberg Atoms: Quantum Simulation and Non-equilibrium Dynamics](http://arxiv.org/abs/2607.11038v1)
  <details><summary>📄 Abstract</summary>
  Rydberg atoms, characterized by their strong and long-range dipole-dipole interactions, provide a versatile platform for exploring intriguing collective and many-body effects. Recently, the experimental realization of these effects in dense ensembles and reconfigurable atomic arrays has attracted significant interest, particularly for applications in quantum simulations and non-equilibrium physics. This review focuses on such recent development, discussing the theoretical foundations of the inte...
  </details>

- **2026-07-12** — Robert Wijaya, Ngai-Man Cheung — [Mixture of Cognitive Experts in Large Vision-Language Models](http://arxiv.org/abs/2607.10796v1)
  <details><summary>📄 Abstract</summary>
  Large Vision Language Models (LVLMs) require strong reasoning over both visual and textual input. Recent work suggests that cognitive elements, especially diverse representations and metacognition, correlate with better performance. Many of the needed perceptual functions are already provided by specialized domain-specific computer vision models, which act as the perceptual subsystem for detecting objects, localizing them, inferring states, recovering spatial layout, and reading text. The key ch...
  </details>


### 📂 other
*其他安全相关 / Other Security-Related* — 166 papers

- **2026-07-15** — Lei Zhang, Yusheng Zhao, Hongshun Yao et al. — [Building Shor's Algorithm in Lean: An Agentic Formalization of Quantum Attacks on RSA-2048 and P-256](http://arxiv.org/abs/2607.14082v1)
  <details><summary>📄 Abstract</summary>
  Large language models are increasingly assisting with demanding formal theorem-proving tasks, particularly when grounded in machine-checked libraries such as Lean. Agentic systems further amplify this process by searching, reusing, and extending existing formal developments to uncover new discoveries. In quantum computing, Shor's algorithm and its variants present such a demanding case for Lean formalization. In this work, we formalize this algorithm family in Lean through agentic formalization:...
  </details>

- **2026-07-15** — Zhenkai Zhang, Krista A. Ehinger, Tom Drummond — [TCAM-Diff: Triplane-Aware Cross-Attention Medical Diffusion Model](http://arxiv.org/abs/2607.13812v1)
  <details><summary>📄 Abstract</summary>
  We introduce TCAM-Diff, a novel 3D medical image generation model that reduces the memory requirements to encode and generate high-resolution 3D data. This model utilizes a decoder-only autoencoder method to learn triplane representation from dense volume and leverages generalization operations to prevent overfitting. Subsequently, it uses a triplane-aware cross-attention diffusion model to learn and integrate these features effectively. Furthermore, the features generated by the diffusion model...
  </details>

- **2026-07-15** — Angelo F. Andreoli, Gabriela B. Ribeiro, Guilherme C. Stumpf et al. — [Chemical short-range order controls deformation pathways in a complex concentrated alloy](http://arxiv.org/abs/2607.13896v1)
  <details><summary>📄 Abstract</summary>
  Chemical short-range order (CSRO) is an intrinsic feature of complex concentrated alloys (CCAs), yet its influence on deformation mechanisms is controversial because of the inconclusive state of concurrent CSRO quantification during deformation. Here, we provide experimental evidence that CSRO acts as an intrinsic thermodynamic state variable governing stacking-fault energetics and deformation pathways in a Co30Cr40Ni30 alloy. By comparing quenched (CSRO-lean) and aged (CSRO-enriched) conditions...
  </details>

- **2026-07-15** — Lili Zhou, Ruizi Zhang, Chen Si et al. — [Realization and manipulation of spiral charge density waves in a two-dimensional metal](http://arxiv.org/abs/2607.13878v1)
  <details><summary>📄 Abstract</summary>
  Nearly degenerate charge-density-wave (CDW) states play a central role in the competition among collective phenomena. In real materials, however, these states are often intertwined by disorder, hindering their disentanglement and control. Here we show that strain can lift this near-degeneracy and spatially separate distinct CDW states in NbSe2. Using van der Waals (vdW) interactions, we stabilize a micron-scale strain network that produces spatially inhomogeneous strain fields. Within this lands...
  </details>

- **2026-07-15** — Lin Jiaben, Tong Liyue, Wang Hui et al. — [Scientific-Intention Driven Embodied Intelligent Solar Telescope: Conceptual Design](http://arxiv.org/abs/2607.13533v1)
  <details><summary>📄 Abstract</summary>
  Artificial Intelligence (AI) is profoundly transforming the paradigms of scientific research. Cutting-edge technologies such as Large Language Models (LLMs) and embodied intelligence are continuously pushing the boundaries of scientific instrumentation. Against this backdrop, this paper proposes a novel conceptual system: the Scientific-Intention Driven Embodied Intelligent Solar Telescope (SIDEST). The system is designed with three core layers to achieve three types of intelligent scientific re...
  </details>

- **2026-07-15** — Phu Pham, Damon Conover, Aniket Bera — [COLMAR: Cooperative View Policy Learning for Multi-Agent Active 3D Reconstruction](http://arxiv.org/abs/2607.13524v1)
  <details><summary>📄 Abstract</summary>
  Active 3D reconstruction requires selecting informative viewpoints under limited sensing budgets. In multi-agent settings, coordination inefficiencies such as redundant observations and spatial clustering can significantly reduce reconstruction quality. We present COLMAR, a cooperative view policy learning framework for multi-agent active 3D reconstruction. COLMAR formulates viewpoint allocation as a shared policy optimization over map-centric observations and introduces a reconstruction-aware o...
  </details>

- **2026-07-15** — Zobeir Raisi — [2D Rotary Position Embedding for Scene Text Recognition with Transformers](http://arxiv.org/abs/2607.13458v1)
  <details><summary>📄 Abstract</summary>
  Scene Text Recognition (STR) remains challenging due to the diversity of text appearances, including curvature, rotation, and perspective distortion. Recent Transformer-based approaches perform well but usually rely on one-dimensional positional encodings that ignore the 2D spatial structure of text images. Axial 2D extensions of Rotary Position Embedding (RoPE) exist for vision Transformers, but they assume roughly square, isotropic image content and apply the rotation only within encoder self-...
  </details>

- **2026-07-15** — Ann-Kareen Gedeus, Jack Good, Nadine Wagener et al. — [TANDE: Disentangling Verbal and Nonverbal Backchannels in Emotional AI-Avatar Conversations with Young Adults](http://arxiv.org/abs/2607.13357v1)
  <details><summary>📄 Abstract</summary>
  Embodied conversational agents (ECAs) need effective empathic grounding to foster social support and engagement. Expanding into emotional domains, ECAs now use Large Language Models (LLMs) and multimodal human-agent interactions to enhance their capabilities. Yet, understanding the impact of backchanneling modalities on young adults and their gender remains limited. We introduce TANDE, an LLM-powered ECA designed for emotional conversations with young adults, a population experiencing mental, pe...
  </details>

- **2026-07-15** — Ru Zhang, Weijie Qiu — [SPyCE: Skill-Policy Co-evolution for Multimodal Agents](http://arxiv.org/abs/2607.13854v1)
  <details><summary>📄 Abstract</summary>
  Multimodal agents that think with images iteratively manipulate visual evidence and invoke tools across many steps. Existing reinforcement learning methods reduce trajectories to scalar rewards, forcing the policy to discover reusable tool-use patterns from scratch on every new task; memory-based alternatives retain past experience, yet they rely on test-time retrieval, without updating the policy to absorb reusable patterns from that experience. Our key insight is that multimodal reasoning traj...
  </details>

- **2026-07-15** — Yingwei Ji — [An Empirical Study on Stage-Information Interfaces for VLA Fine-Tuning](http://arxiv.org/abs/2607.13605v1)
  <details><summary>📄 Abstract</summary>
  One high-level instruction in long-horizon manipulation can cover several action stages. We use segmented action annotations as an intermediate representation between the full-task instruction and VLA action chunks. A progress module tracks the active stage, while the action policy receives stage information either as current-stage text or as a normalized ordinal stage index in robot state. We compare these interfaces with GR00T N1.6 on LIBERO-10 under direct fine-tuning and continuation fine-tu...
  </details>

- **2026-07-15** — Huatao Li, Xinwei Geng, Yuheng Wang et al. — [DevicesWorld: Benchmarking Cross-Device Agents in Heterogeneous Environments](http://arxiv.org/abs/2607.13465v1)
  <details><summary>📄 Abstract</summary>
  LLM-based agents have rapidly improved at operating individual digital environments such as mobile applications, desktop systems, and smart homes. However, real-world user goals often span multiple devices: information may come from a phone, be processed on a desktop, and the result may need to appear on another device. Most existing benchmarks center on a single dominant execution environment, making it difficult to evaluate whether agents can acquire and integrate information across heterogene...
  </details>

- **2026-07-15** — Shivansh Patel, Kaifeng Zhang, Sanjay Pokkali et al. — [Learning Physics-Guided Residual Dynamics for Deformable Object Simulation](http://arxiv.org/abs/2607.13451v1)
  <details><summary>📄 Abstract</summary>
  Simulating deformable objects is essential for a wide range of robotic manipulation applications, yet accurately predicting their dynamics remains challenging. We propose Physics-Guided Residual Dynamics (PGRD), a hybrid simulation framework that combines the advantages of physics-based and learning-based approaches. Specifically, PGRD combines an optimizable spring-mass simulator as a backbone with a learned neural network that predicts residual corrections to the physics-based predictions. We ...
  </details>

- **2026-07-15** — Jing-Xiao Liao, Tianwei Zhang, Yu-Hao Jiang et al. — [Self-Improving is Often Sudden: Enlightenment-style Finetuning for Large-Scale Models](http://arxiv.org/abs/2607.13395v1)
  <details><summary>📄 Abstract</summary>
  The pursuit of autonomously self-improving models has attracted growing interest in the era of large-scale foundation models. Drawing inspiration from the concept of "enlightenment" or "aha moment" in human brain, we hypothesize that large models exhibit an analogous enlightenment phenomenon-a latent capacity for sudden capability boost. Then, we propose Enlightenment, a novel training-free post-tuning paradigm for large-scale models. Our approach modifies shortcuts for key modules/layers withou...
  </details>

- **2026-07-15** — Moses Boudourides — [LLMs for Qualitative and Mixed-Methods Social Network Analysis](http://arxiv.org/abs/2607.14045v1)
  <details><summary>📄 Abstract</summary>
  This manuscript explores the integration of Large Language Models (LLMs) into the field of qualitative and mixed-methods social network analysis (SNA). We argue that the primary focus of this integration should be on enhancing the depth and rigor of qualitative SNA, rather than on replacing human researchers with automated systems. We begin by outlining the core principles of qualitative and mixed-methods SNA, emphasizing the importance of understanding the meaning of ties, the role of narrative...
  </details>

- **2026-07-15** — Wenxiao Wang, Priyatham Kattakinda, Soheil Feizi — [Do Agent Optimizers Compound? A Continual-Learning Evaluation on Terminal-Bench 2.0](http://arxiv.org/abs/2607.14004v1)
  <details><summary>📄 Abstract</summary>
  Most reported gains from agent-optimization methods are one-shot: an agent is optimized against a fixed benchmark and the resulting improvement is reported as if it were a stable property of the method. This does not test the setting that matters for deployed agents, where optimization is applied recursively as new failures and new tasks appear over time. The central question this raises is whether optimizer-driven gains compound: after an agent has been optimized once, can it be optimized again...
  </details>

- **2026-07-15** — Benedikt Bollig, Matthias Függer, Thomas Nowak et al. — [Agent-Alternation-Free Epistemic Metric Temporal Logic with Past: Model Checking and Complexity](http://arxiv.org/abs/2607.13981v1)
  <details><summary>📄 Abstract</summary>
  We study model checking for an epistemic metric temporal logic with past, interpreted over finite Büchi automata under synchronous perfect recall. The logic is motivated by observation-based verification problems such as diagnosis and opacity, where an observer sees only a projection of an execution and reasons about events that may have occurred earlier. These requirements use no alternation between different agents' knowledge. We therefore consider the agent-alternation-free fragment, in which...
  </details>

- **2026-07-15** — Juan-Feng Zhu, Wenjie Zhou, Shihao Feng et al. — [Temporal Fourier Optics Reveals Hidden Hybridized Light-Matter States](http://arxiv.org/abs/2607.13957v1)
  <details><summary>📄 Abstract</summary>
  Spectral measurements provide fundamental insights into wave systems by revealing resonances, mode hybridization, and light-matter interactions. However, intrinsic dissipation and measurement-induced spectral broadening often conceal the underlying hybridized light-matter states that give rise to measured spectra. Here, we establish a space-time Fourier correspondence that interprets spectral broadening as an effective temporal attenuation, giving rise to a temporal Fourier optics framework for ...
  </details>

- **2026-07-15** — Wangjin Zhou, Yizhou Zhang, Yichi Wang et al. — [Rethinking Speech Foundation Model Fine-tuning: Better SFT or Better Match?](http://arxiv.org/abs/2607.13864v1)
  <details><summary>📄 Abstract</summary>
  Supervised fine-tuning (SFT) is widely used to adapt self-supervised speech representations to downstream classification tasks. Small gains observed under a single pretrained checkpoint are often interpreted as method-level improvements, i.e., a higher attainable performance ceiling. We show that such conclusions are not always reliable because SFT outcomes depend strongly on the specific pretrained instance. We conduct a systematic study on 3 SUPERB classification tasks, evaluating 8 SFT varian...
  </details>

- **2026-07-15** — Xiaotian Luo, Fengxingyu Wang, Chuanrui Hu et al. — [Self-Evolving Agent Harnesses via Gated Semantic Quality-Diversity](http://arxiv.org/abs/2607.13683v1)
  <details><summary>📄 Abstract</summary>
  An LLM agent's real-task performance is shaped as much by the harness around its model as by the frozen model itself: its prompts, injected knowledge, runtime control, and configuration. In deployment the harness is often the only lever available, so improving it automatically is the natural way to raise performance without touching the weights. The hard part is not generating changes but knowing which one truly helped. Self-generated feedback is noisy, and an apparent gain can be a measurement ...
  </details>

- **2026-07-15** — Yongren Shi, Wenyi Gong — [When Bots Join the Team: Bot Adoption and the Institutional Fabric of Open-Source Software Projects](http://arxiv.org/abs/2607.13679v1)
  <details><summary>📄 Abstract</summary>
  AI agents are joining human teams, raising a basic question: when an automated agent becomes a regular participant, does group organization strengthen or weaken? We study this question in open-source software, where bots open pull requests, review code, and merge changes alongside people, leaving a public record of every interaction. Treating bots as participants rather than tools, we examine 2,991 GitHub projects for two years before and after each adopted its first bot. We measure three capabi...
  </details>

- **2026-07-15** — Jose Martínez-Fajardo, Pablo Pueyo, Fernando Caballero et al. — [From Language to Navigation Goals: A Vision-Language Approach for Semantic Navigation of Mobile Robots Using RGB-D Perception](http://arxiv.org/abs/2607.13624v1)
  <details><summary>📄 Abstract</summary>
  Natural language interaction provides an intuitive way for non-expert users to communicate with robotic platforms. However, transforming user requests into executable navigation actions remains a challenging task, requiring the integration of language understanding, environment perception, and autonomous navigation. This work presents a language-driven navigation framework that enables mobile robots to interpret user requests in natural language to move the robot to a destination and autonomousl...
  </details>

- **2026-07-15** — Yue Yan, SiYing Wang, ZhiXin Xia et al. — [Tensor Network decoding under inter-qubit correlated errors](http://arxiv.org/abs/2607.13570v1)
  <details><summary>📄 Abstract</summary>
  The maximum likelihood decoder based on tensor networks has proven highly successful for the 2D surface code, achieving the optimal decoding success rate. However, existing tensor network decoders are typically designed for independent single-qubit error models, and their performance under inter-qubit correlated error models remains unexplored. This is due to two major challenges. The first challenge lies in constructing the tensor network for correlated errors, since the same final Pauli error ...
  </details>

- **2026-07-15** — Vivek Kanojiya, Vishalaksh Aggarwal, Daeho Baek et al. — [Personalizing Incremental Video Search with Hybrid Text and ID Embeddings](http://arxiv.org/abs/2607.13493v1)
  <details><summary>📄 Abstract</summary>
  Incremental video search requires high-quality ranking after each keystroke, where intent is often underspecified (e.g., 1-3 character prefixes). We present a personalization system for Apple TV search that combines complementary semantic and collaborative signals at ranking time. Our approach learns two item embedding spaces: (i) a text-based multilingual encoder (TextEmb) fine-tuned on co-engagement triplets via contrastive learning, and (ii) an ID-based collaborative embedding model (IdEmb) t...
  </details>

- **2026-07-15** — Lei Yang, Weiqing Li, Zhiyong Su et al. — [CASA-SDF: Curriculum-Aware Spatial Adaptation with Curvature-Guided Density for Neural Implicit Surface Reconstruction](http://arxiv.org/abs/2607.13492v1)
  <details><summary>📄 Abstract</summary>
  Neural implicit representations have emerged as a powerful paradigm for 3D reconstruction. However, high-fidelity indoor surface reconstruction remains a significant challenge, primarily due to the pronounced \emph{geometric heterogeneity} of indoor scenes. Large texture-less planar regions typically require stronger regularization to suppress high-frequency artifacts, while thin structures demand sharper, more adaptive representations to mitigate the spectral bias of multi-layer perceptrons (ML...
  </details>

- **2026-07-15** — Joonyong Park, David M. Chan, Yuki Saito et al. — [Auditing Protocol-Level Shortcuts in Large Audio Language Model Judges for Speech Evaluation](http://arxiv.org/abs/2607.13477v1)
  <details><summary>📄 Abstract</summary>
  Large audio-language models (LALMs) are increasingly used as automatic judges for speech evaluation. However, high agreement with human ratings does not guarantee that their verdicts are grounded in the audio. A judge may instead rely on specialist labels or reference data supplied by the evaluation protocol itself, taking a shortcut in place of listening to the audio. In this paper, we audit such protocol-level ``shortcuts'' in LALM judges across three common deployment protocols: feature-bluep...
  </details>

- **2026-07-15** — Tuomas Oikarinen, Zixiao Chen, Charlotte Siska et al. — [Data-Efficient Adaptation of LLMs via Attention Head Reweighting](http://arxiv.org/abs/2607.13425v1)
  <details><summary>📄 Abstract</summary>
  Learning effectively from limited data is critical in domains like security where labeled examples are scarce. Large language models (LLMs) have demonstrated some capabilities for data-efficient learning, especially through parameter-efficient adaptation methods, but continue to struggle when faced with few samples for difficult tasks. To meet this challenge, we propose Attention Head Reweighting (AHR), a data-efficient method that adapts LLMs to new text-classification tasks by learning only a ...
  </details>

- **2026-07-15** — Jiwen Zhou, Xiang Liu, Mingming Li et al. — [Can We Steer the Black-Box? Towards Controllability-Centric Evaluation of Recommender Systems with Collaborative Agents](http://arxiv.org/abs/2607.13418v1)
  <details><summary>📄 Abstract</summary>
  Recommender systems operate as Black-Boxes, leaving users and regulators unable to steer their outputs toward specific intentions or audit their behavior. This lack of controllability, defined as the system's ability to respond to explicit guidance, remains an unaddressed dimension in existing evaluation paradigms. To fill this gap, we propose CtrlBench-Rec, a collaborative multi-agent framework for systematic assessment of controllability. We formalize three fundamental tasks: target content di...
  </details>

- **2026-07-15** — Guanglei Zhou, Chen-Chia Chang, Yikang Shen et al. — [EXPLORE: Exploration with Guided Search for Analog Topology Generation using Language Models](http://arxiv.org/abs/2607.13416v1)
  <details><summary>📄 Abstract</summary>
  Automating analog circuit topology design is essential to reduce the extensive manual effort required to meet increasingly diverse and customized application demands. Recent advances have applied sequence-to-sequence fine-tuning on pretrained language models to directly generate circuit topologies from user specifications in a single pass. However, these one-shot generation methods failed to generate complex circuits due to their exponentially growing search spaces and limited training datasets....
  </details>

- **2026-07-15** — Wenkai Dong, Yifan Wang — [From Interpretation to Compilation: Compilation-Based Execution of Semantic Operators [Vision]](http://arxiv.org/abs/2607.13407v1)
  <details><summary>📄 Abstract</summary>
  Semantic operator systems extend data processing with natural-language interfaces, supporting operations such as semantic filtering, mapping, and joining. Existing systems commonly execute these operators through interpretation-based execution: for each row, record, or candidate pair, an LLM is invoked to interpret the semantic intent and produce an output. Although expressive, this places expensive LLM calls inside the data-processing loop, causing high latency, monetary cost, and limited scala...
  </details>

- **2026-07-15** — Donghwan Kim — [Evaluation Ability Does Not Imply Optimization Utility: LLM-as-a-Judge Signals in Closed-Loop Table Recognition](http://arxiv.org/abs/2607.13347v1)
  <details><summary>📄 Abstract</summary>
  LLM-as-a-judge is widely used to provide feedback and selection signals in closedloop regeneration, but this use remains insufficiently validated. We study it in table recognition, where deterministic TEDS evaluation provides a controlled testbed, using FinTabNet and OmniDocBench. Three findings emerge. First, judge signals were weak on both datasets: scores frequently tied, rankings were not reproducible, and the only selection policy that beat random on both datasets depended on an earliest-it...
  </details>

- **2026-07-14** — Li Hu, Guangyuan Wang, Peng Zhang et al. — [WanToFight: Real-Time Generative Game Engine for Multi-Player Combat Interaction](http://arxiv.org/abs/2607.12592v1)
  <details><summary>📄 Abstract</summary>
  We present WanToFight, a generative game engine that simulates real-time, two-player The King of Fighters '97 (KOF~'97) gameplay from keyboard input. Prior generative game engines target either single-player first-person settings or non-real-time cooperative scenarios; multi-player control, real-time inference, complex physical interaction, and adversarial gameplay have not been jointly addressed. WanToFight closes this gap with three components built on the Wan-1.3B video diffusion transformer:...
  </details>

- **2026-07-14** — Kunal Gupta, Gaurav Joshi, Yen-Ru Chen et al. — [Reflecting Process Expertise in Procedural Material Generation](http://arxiv.org/abs/2607.13318v1)
  <details><summary>📄 Abstract</summary>
  Procedural material creation underpins applications in digital content creation, visual effects, and 3D asset design. Achieving high-quality results requires more than reproducing node graphs -- it demands understanding the process by which experts construct materials. We formulate procedural material generation as retrieval-time process reasoning over expert demonstrations, elevating process to a first-class representation beyond graph-only synthesis. Concretely, we represent expert workflows a...
  </details>

- **2026-07-14** — Mohammad Javad Latifi Jebelli — [On Transformer Dynamics](http://arxiv.org/abs/2607.13295v1)
  <details><summary>📄 Abstract</summary>
  We develop a geometric framework in which the token dynamics of a transformer are modeled by a system of interacting particles on a Riemannian manifold $\mathcal M$, the attention mechanism being encoded by a time-independent two-body interaction law, that is, a section of the pullback bundle $π_2^{*}(T\mathcal M)$ over $\mathcal M\times\mathcal M$. Within this framework we isolate two features that a family of interaction laws must possess in order to model language: it must realize generic non...
  </details>

- **2026-07-14** — Gabriel R. S. Scapim, Gislaine C. L. Leal, Guilherme C. Guerino — [SoftBoard: A Multi-Agent Tool for the Creation and Evaluation of Low-Fidelity Prototypes](http://arxiv.org/abs/2607.13179v1)
  <details><summary>📄 Abstract</summary>
  User Experience (UX) is recognized as a critical factor for the success of digital products, particularly in software startups, environments marked by time constraints, limited resources, and low maturity in design practices. Building Minimum Viable Products (MVPs) through low-fidelity prototyping represents a well-established strategy for rapid validation cycles at reduced cost. A systematic literature mapping, however, revealed gaps in the ecosystem of available tools: a predominance of genera...
  </details>

- **2026-07-14** — Ilias Kazantzidis, Timothy J. Norman, Yali Du et al. — [Learning Safe Agent Behaviour from Human Preferences and Justifications via World Models](http://arxiv.org/abs/2607.13172v1)
  <details><summary>📄 Abstract</summary>
  We address the problem of safely training an agent policy and deploying a good and safe policy, in settings where the environment dynamics are unknown and no suitable reward function is available. In the context of safety-critical environments, we consider traditional reinforcement learning impractical and resort to the resource of human input. We introduce DROPJ, a human-centred method for both safe training and deployment. We first learn a world model (a learned simulator) from a dataset of pr...
  </details>

- **2026-07-14** — Mert Onur Cakiroglu, Mehmet Dalkilic, Hasan Kurban — [The Spectrum Is Not Enough: When Context Helps Time-Series Forecasting](http://arxiv.org/abs/2607.13006v2)
  <details><summary>📄 Abstract</summary>
  A growing family of indices scores how predictable a series is from its spectrum. Practitioners increasingly read these scores as answering a different question: whether \emph{adding context}, a longer lookback, a retrieval plug-in, or a pretrained model, will help. These are not the same question. The value of context is a property of the operating point, not of the series. Any index built from the power spectrum is invariant under phase randomization, whereas the beyond-second-order value that...
  </details>

- **2026-07-14** — Ruoran Xu, Wending Gao, Qiufeng Wang — [FormalAnalyticGeo: A Neural-Symbolic Based Framework for Multimodal Analytic Geometry Problem Generation](http://arxiv.org/abs/2607.12982v1)
  <details><summary>📄 Abstract</summary>
  Math reasoning has achieved significant progress with the rapid advancement of Multimodal Large Language Models (MLLMs), however analytic geometry remains largely underexplored, primarily due to the scarcity of annotated samples. Existing diagram generation approaches struggle with analytic geometry: template methods cannot handle constraint-driven layouts, and generative models lack the geometric precision to render annotated conic curves correctly. We present FormalAnalyticGeo, a scalable fram...
  </details>

- **2026-07-14** — Chalamalasetti Kranti, Sowmya Vajjala — [LLM Judges Can Be Too Generous When There Is No Reference Answer](http://arxiv.org/abs/2607.12885v1)
  <details><summary>📄 Abstract</summary>
  LLM judges are increasingly being used to evaluate open-ended model responses, often in no-reference settings where a ground-truth answer is unavailable. However, can they reliably assess in such evaluation setups? We explore this question in this paper through a two stage pipeline with a) calibration experiments that assess the judge model's knowledge of the task it is evaluating, and b) sensitivity experiments that assess how the judge model's performance is impacted by the presence and positi...
  </details>

- **2026-07-14** — Xing Zhang, Guanghui Wang, Yanwei Cui et al. — [Who Grades the Grader? Co-Evolving Evaluation Metrics and Skills for Self-Improving LLM Agents](http://arxiv.org/abs/2607.12790v1)
  <details><summary>📄 Abstract</summary>
  Self-evolving agent systems improve by creating, revising, and retiring their own skills, but every such loop rests on a hidden assumption: a reliable evaluation metric already exists. In many real applications it does not. We make three claims. First, metrics can be \emph{evolved}: our metric loop searches compositions of small drawback detectors under a full evolutionary lifecycle, trained to agree with a ten-item anchored reference set, regularized by consensus over unlabeled outputs, and aud...
  </details>

- **2026-07-14** — Cheng-Tai Hsieh, Jiwei Shan, Han Fang et al. — [ExtraGS: Enhancing Endoscopic View Extrapolation via Diffusion-Guided 3D Gaussian Splatting](http://arxiv.org/abs/2607.12785v2)
  <details><summary>📄 Abstract</summary>
  Robot-assisted minimally invasive surgery (MIS) critically depends on reliable endoscopic perception for navigation and safety. However, conventional endoscopes provide only a limited field of view, leaving large portions of the surrounding anatomy unobserved. Recent neural rendering approaches, such as Neural Radiance Fields and 3D Gaussian Splatting, enable novel view synthesis from endoscopic videos, but their reliance on sparse observations often leads to severe artifacts when extrapolating ...
  </details>

- **2026-07-14** — Quanyan Zhu — [Internet of Agentic Things: Networked AI Agents for Closed-Loop IoT Orchestration](http://arxiv.org/abs/2607.12662v1)
  <details><summary>📄 Abstract</summary>
  The paper introduces the Internet of Agentic Things (IoAT), an architectural framework that integrates agentic AI, IoT, cyber-physical systems, Physical AI, edge computing, and digital twins into a unified closed-loop orchestration framework. The proposed architecture consists of cloud, edge/fog, and physical IoT layers connected through autonomous AI agents that perceive, reason, coordinate, and actuate across distributed cyber-physical environments. The paper formalizes IoAT as a coupled workf...
  </details>

- **2026-07-14** — Amin Beheshti, Rong N. Chang, Boualem Benatallah et al. — [Agentic Service-Oriented Computing: A Manifesto for the Next Frontier of Service-Oriented Computing](http://arxiv.org/abs/2607.12619v1)
  <details><summary>📄 Abstract</summary>
  The rapid emergence of LLM-powered autonomous and semi-autonomous agents is reshaping software systems from static, request-response components into goal-directed, adaptive, and tool-using computational actors. As these agents move from isolated cognitive prototypes into complex distributed workflows, they confront challenges that the Service-Oriented Computing community has studied for more than two decades: composition, interoperability, quality of service, lifecycle management, governance, se...
  </details>

- **2026-07-14** — Yanghe Hao, Martin Huber, Christos Bergeles et al. — [Streamlining stereo differentiable rendering for marker-free real-time tracking of surgical robots](http://arxiv.org/abs/2607.12604v1)
  <details><summary>📄 Abstract</summary>
  Purpose: Marker-based tracking of surgical robots is occlusion-prone in cluttered operating rooms. We evaluate stereo differentiable rendering for marker-free, real-time robot pose tracking, potentially improving safety, reducing setup time, and enabling multi-robot interaction. Methods: We extend the markerless pose estimation framework roboreg to online dynamic tracking via (i) sequential optimisation that propagates pose estimates across frames with motion-adaptive hyperparameter tuning, and ...
  </details>

- **2026-07-14** — Wenjie Li, Yujie Zhang, Fanrui Zhang et al. — [Evidence-Grounded AI for Musculoskeletal Care](http://arxiv.org/abs/2607.12527v2)
  <details><summary>📄 Abstract</summary>
  Musculoskeletal diseases are among the leading causes of disability worldwide and create the greatest global need for rehabilitation. Because recovery, remodelling and degeneration often unfold over months to years, musculoskeletal care requires longitudinal management that repeatedly integrates evolving patient evidence, external medical knowledge and stage-specific functional goals. In routine practice, this evidence is fragmented across visits, departments and hospital systems, limiting indiv...
  </details>

- **2026-07-14** — Yiming Liu, Wenqi Lou, Zhiguang Wang et al. — [Realizable N:M Sparse Transformer Inference via Search-Kernel Co-Design](http://arxiv.org/abs/2607.12505v2)
  <details><summary>📄 Abstract</summary>
  Vision Transformers (ViTs) achieve strong accuracy but incur high inference latency. Semi-structured N:M sparsity can reduce arithmetic cost, yet its theoretical savings often fail to translate into proportional end-to-end speedups on modern GPUs. This mismatch arises because deployment latency depends not only on arithmetic reduction but also on execution regularity and hardware scheduling under sparsity. Achieving practical acceleration, therefore, requires coordinated design across sparse exe...
  </details>

- **2026-07-14** — Dharshan Kumaran, Viorica Patraucean, Maks Ovsanikov et al. — [The Computational Basis of Confidence in Large Language Models](http://arxiv.org/abs/2607.12447v1)
  <details><summary>📄 Abstract</summary>
  Reliable confidence -- the probability that a model's own answer is correct -- is essential for the trustworthy deployment of language models. Existing work has largely evaluated confidence by how well it predicts correctness and whether it is calibrated, leaving open a more fundamental question: what does the confidence signal itself represent? Answer logits may reflect a latent decision variable sufficient to compute normative confidence, or instead a heuristic preference signal that combines ...
  </details>

- **2026-07-14** — Abdurrahman Javat, Allan Kazakov — [Accepted Prefixes Are Not All You Need: A Negative Result on PEFT-Based Block-Diffusion Drafting](http://arxiv.org/abs/2607.12422v1)
  <details><summary>📄 Abstract</summary>
  Speculative decoding accelerates autoregressive language model inference by using a cheap drafter to propose multiple future tokens and a target model to verify them. A common design goal is therefore to improve draft quality while reducing auxiliary parameters and systems overhead. We study a negative result for this direction through PEFT-BD, a same-backbone speculative decoding method in which a LoRA-like adapter acts as a block-diffusion drafter for an autoregressive verifier. PEFT-BD is mot...
  </details>

- **2026-07-14** — Kai Jiang, Jiaxing Huang, Jingyi Zhang et al. — [MobileSAM2: Lightweight Segment Anything for Spatial Intelligence](http://arxiv.org/abs/2607.12297v1)
  <details><summary>📄 Abstract</summary>
  The recent large video foundation model, SAM2, enables segment anything in both images and videos, serving as a powerful base model for various applications. However, many of such use cases require to operate on resource-constrained devices like mobile phones and laptops. In this work, we aim to make SAM2 more mobile-friendly by distilling the heavyweight SAM2 into a lightweight model, facilitating segment anything in both images and videos on mobile devices. To this end, we propose Hypergraphic...
  </details>

- **2026-07-14** — Md Mahfuzur Rahman, Pengzhan Zhou, A F M Abdun Noor et al. — [Adaptive Cross-Modal Fusion with Sparse Attention for Pedestrian Crossing Intention Prediction](http://arxiv.org/abs/2607.12293v1)
  <details><summary>📄 Abstract</summary>
  Predicting pedestrian crossing intention is a safety-critical task for autonomous driving, yet existing approaches often rely on single-modal inputs or dense multimodal fusion strategies that inadequately capture complementary visual and kinematic information while introducing redundant inter-modal interactions. We propose ADAPT (Adaptive Domain-Aware Pedestrian Crossing Transformer), a multimodal framework that jointly models local and global visual context together with temporal motion dynamic...
  </details>

- **2026-07-14** — Jacob Dunefsky, Wes Gurnee, Emmanuel Ameisen — [A Shared Subcircuit Lets LLMs Count Down Across Tasks](http://arxiv.org/abs/2607.12279v1)
  <details><summary>📄 Abstract</summary>
  Writing a sentence of exactly twelve words; ending a DNA sequence at the right codon; formatting an ASCII table. These are all tasks that language models can do that requires tracking how many tokens remain before a target. In this work, we identify in Llama-3.1-70B-Instruct a general mechanism for performing these tasks: a "countdown subcircuit" that compares the current position to a goal length and estimates the time remaining until then. We first isolate a countdown subcircuit in a controlle...
  </details>

- **2026-07-14** — Ning Liu — [Track, Rank, Crack: Epistemic Working Memory Scales Multi-Hop Reasoning in Language Agents](http://arxiv.org/abs/2607.12267v1)
  <details><summary>📄 Abstract</summary>
  Language agents that interleave reasoning and tool use degrade sharply as reasoning chains lengthen, even when each individual step is easy. We trace this to context dilution: an agent's investigative state (what it has confirmed, what it suspects, and what it still needs) lives only implicitly in a growing context window, where early discoveries are buried under later retrievals. We introduce SLEUTH, which makes this state explicit and actionable through a structured epistemic working memory: t...
  </details>

- **2026-07-14** — Chengshuai Yang — [How to Realize Recursively Self-Improving Agents and Personal Singularity: A Goal-, Scope-, Tool-, and Benchmark-Driven Multi-Agent Architecture](http://arxiv.org/abs/2607.12254v1)
  <details><summary>📄 Abstract</summary>
  Large language model (LLM) agents can increasingly plan, use tools, maintain memory, and execute long-horizon tasks. These advances motivate two linked questions: how can an agent improve the mechanisms by which it learns and acts, and how can that improvement increase the durable capabilities of its user rather than only the software itself? This paper proposes a governed multi-agent architecture for recursively self-improving agents and introduces personal singularity as a bounded human-AI co-...
  </details>

- **2026-07-14** — Taizhen Cheung, SA Kwon — [When Directional Accuracy Lies: A Base-Rate-Honest Benchmark for LoRA-Adapted TimesFM on Equity Forecasting](http://arxiv.org/abs/2607.12248v1)
  <details><summary>📄 Abstract</summary>
  Large pretrained time-series models such as TimesFM are attractive for financial forecasting, but raw directional accuracy is a misleading scoreboard in equity markets. An early LoRA adapter in this project appeared to reach roughly 80% directional accuracy; we show this is not evidence of skill. Over a long horizon in a rising market, a trivial "always-up" rule attains comparably high accuracy without using the input at all. To separate genuine skill from this base-rate artifact, we build a rep...
  </details>

- **2026-07-14** — Nicolae Cudlenco, Mihai Masala, Marius Leordeanu — [The GEST-Engine: From Event Graphs to Synthetic Video. A Full Technical Report](http://arxiv.org/abs/2607.12231v1)
  <details><summary>📄 Abstract</summary>
  We present the GEST-Engine, a complete system that goes from natural-language text to fully-annotated multi-actor video. At its core is an explicit world model: rather than encoding state as a learned latent, the engine maintains a complete, inspectable representation of the world (which actors exist, where they are, what they are doing, which objects they hold, and how events relate in time and space), expressed as a formal Graph of Events in Space and Time (GEST) and realized deterministically...
  </details>

- **2026-07-14** — Monica Munnangi, Saiph Savage — [Evaluating Large Language Models on Misconceptions in Multi-Turn Medical Conversations](http://arxiv.org/abs/2607.12884v1)
  <details><summary>📄 Abstract</summary>
  Patients seeking medical information often ask questions that embed incorrect assumptions or misconceptions. In such cases, safe medical communication requires not only answering the question, but identifying and correcting the underlying false belief. These interactions naturally unfold over multiple turns, a pattern now mirrored in interactions with LLMs. Yet current evaluation frameworks do not capture model behavior in these settings, where misconceptions can emerge, persist, or evolve over ...
  </details>

- **2026-07-14** — Aldrin Montana, Colin Marc, Luca Bigon et al. — [Not Your Usual Type(s): Data contracts as types across languages and engines](http://arxiv.org/abs/2607.13339v1)
  <details><summary>📄 Abstract</summary>
  Composable data systems promise to let developers combine languages, engines, and catalogs without sacrificing a coherent user experience. In practice, however, pipeline-node boundaries remain weakly specified: transformations exchange tables through schemas that are often checked late, enforced unevenly across languages, and disconnected from the semantics business users care about. Based on over a year of operating millions of jobs in Bauplan, we share the design principles behind our new SDK,...
  </details>

- **2026-07-14** — Jae Joong Lee — [Accuracy Without Grounding: Diagnosing Visual Dependency Dissociation in Video LLM Benchmarks](http://arxiv.org/abs/2607.13305v1)
  <details><summary>📄 Abstract</summary>
  Benchmark accuracy in video large language models (LLMs) is often treated as evidence of visual understanding. We audit this assumption across twenty models spanning 2-78B parameters and ten architecture families. We introduce the Visual Dependency Gap (VDG), the difference in per-question correctness between original-video and black-screen conditions. Paired McNemar tests on MVBench show that accuracy and visual dependency are separable: models differ on original video (p = 0.0003) but not on b...
  </details>

- **2026-07-14** — Stylianos Loukas Vasileiou, Olga Derendiaeva — [Discourse-Aware Policy Analysis with Argumentation: A Hybrid LLM-Symbolic Framework for Disaster Governance](http://arxiv.org/abs/2607.13260v1)
  <details><summary>📄 Abstract</summary>
  Policy documents shape governance outcomes, but their reasoning is often implicit. Participatory commitments and managerial control routinely coexist in the same text, and the tensions between them are rarely stated directly. Existing computational approaches to policy discourse cannot express the frame-mediated relations that drive these tensions, where one argument narrows or instrumentalizes another rather than rejecting it. End-to-end summarization by large language models produces fluent te...
  </details>

- **2026-07-14** — Ali Parviz, Gal Mishne, Alex Cloninger — [Reassessing Muon for Matrix Factorization](http://arxiv.org/abs/2607.13246v1)
  <details><summary>📄 Abstract</summary>
  Muon has recently emerged as a strong optimizer for large-scale deep learning, where it reshapes gradient updates through approximate orthogonalization and has been reported to outperform Adam and AdamW in large language model training. Its empirical success has motivated a growing body of theoretical work that interprets Muon as steepest descent under the spectral norm. Yet it remains unclear which of Muon's advantages stem from its update rule itself and which are artifacts of the scale, archi...
  </details>

- **2026-07-14** — Quanyan Zhu — [AI-Native Insurance for Agentic AI: Pricing, Underwriting, and End-to-End Automation](http://arxiv.org/abs/2607.13230v1)
  <details><summary>📄 Abstract</summary>
  Agentic AI introduces new insurance challenges because autonomous AI systems can make decisions, invoke tools, modify external environments, and interact with third-party services. This paper develops an AI-native mathematical framework for underwriting, pricing, and contract design for agentic AI deployments. A deployment is represented by a risk state that captures autonomy level, operational authority, permission exposure, governance maturity, and dependency concentration. The framework maps ...
  </details>

- **2026-07-14** — Saber Ganjisaffar, Chengyu Song, Nael Abu-Ghazaleh — [Microflow: Microarchitectural Causal Observability for Deep Cross-Layer Analysis and Optimization](http://arxiv.org/abs/2607.13184v1)
  <details><summary>📄 Abstract</summary>
  Existing architectural simulators expose aggregate metrics or raw traces, but fail to reveal complex interactions among microarchitectural events and their relationship to program execution. Consequently, architects observe performance symptoms but cannot systematically attribute them to root causes across abstraction layers. This paper introduces Microflow, an observability framework elevating causality to a first-class analytical object. Microflow transforms execution traces into the Microflow...
  </details>

- **2026-07-14** — Asmaa Abada, Claire Chevallier, Luighi P. S. Leal et al. — [Challenging Majorana neutrino effects in $B\to K^{(\ast)}νν$ and $K\to πνν$ decays](http://arxiv.org/abs/2607.13142v1)
  <details><summary>📄 Abstract</summary>
  We investigate the contributions of Lepton Number Violating (LNV) effective operators to the rare decays $B\to K^{(\ast)}νν$ and $K\to πνν$. Such operators can modify the kinematic distributions of these processes, providing distinctive probes of physics beyond the Standard Model. Through a renormalization-group analysis, we show that the Standard Model Effective Field Theory (SMEFT) operators responsible for these effects are subject to stringent indirect constraints from neutrino physics. In p...
  </details>

- **2026-07-14** — Tanmay Singla, James C. Davis — [Software Supply Chains are Dead: Use-Case-Oriented Regeneration](http://arxiv.org/abs/2607.13021v1)
  <details><summary>📄 Abstract</summary>
  Modern software development relies on an increasingly doubtful premise: that the up-front implementation savings from adopting a dependency outweighs the maintenance costs. Two changes are reshaping the build-vs.-reuse calculus: software supply chain attacks have raised the cost of external reliance, while generative AI has lowered the cost of local implementation. We envision use-case-oriented regeneration as a new software sourcing paradigm that shifts the supply chain from external trust to l...
  </details>

- **2026-07-14** — Héctor Carrión, Narges Norouzi — [Controllable Generation of Diverse Dermatological Imagery for Fair and Efficient Malignancy Classification](http://arxiv.org/abs/2607.12987v2)
  <details><summary>📄 Abstract</summary>
  Accurate dermatological diagnosis naturally necessitates equitable performance across diverse populations, yet a systematic lack of expertly annotated images, especially for underrepresented skin tones and rare diseases, impedes progress toward measurably fair methods. We introduce cgDDI (Controllable Generation of Diverse Dermatological Imagery), a hybrid framework that (1) synthesizes realistic healthy skin samples without disturbing other input properties, (2) maps single-sample rare lesions ...
  </details>

- **2026-07-14** — Mehmet Iscan — [Form, Not Content? A Preregistered, Placebo-Controlled Evaluation of Learned Error-Conditioned Self-Repair Through Prompts and Weights in Frozen Small Code Models](http://arxiv.org/abs/2607.12962v1)
  <details><summary>📄 Abstract</summary>
  Frozen small code LLMs are deployed locally, yet the information guiding a retry after a failed attempt is still measured without placebo controls in the self-repair literature. We treat a failed program as a conjecture and an execution counterexample as an oracle-relative refutation, and introduce PoPE (Popperian Placebo-controlled Evaluation): a methodology for measuring whether evidence that falsifies LLM-generated code can be used operationally by that same model. In PoPE, error content is p...
  </details>

- **2026-07-14** — Elnara Kadyrgali, Muragul Muratbekova, Pakizar Shamoi — [CD-MED: Cross-Domain Multimodal Emotion Descriptor for Visual Comparison of Digital Objects](http://arxiv.org/abs/2607.12958v1)
  <details><summary>📄 Abstract</summary>
  Digital objects express emotions through different modalities. For example, a movie may include visual scenes, audio, dialogue, and facial expressions, while a song may contain melody, rhythm, lyrics, and vocal tone. Because existing emotion recognition models are usually modality-specific, it is difficult to compare such objects directly. This paper proposes CD-MED, a Cross-Domain Multimodal Emotion Descriptor for representing heterogeneous digital objects in a common emotional space. Each moda...
  </details>

- **2026-07-14** — Sigma Jahan — [Toward Localizing and Repairing Bias in Transformer Attention Heads](http://arxiv.org/abs/2607.12863v1)
  <details><summary>📄 Abstract</summary>
  Transformer language models are increasingly used as software components, yet biased outputs remain difficult to localize and repair inside the model. Existing fairness testing and repair methods largely operate at the input-output or retraining level, while recent work suggests that bias-related behavior can concentrate in a small set of attention heads. This paper studies whether attention heads can be localized and repaired through a targeted inference-time intervention. We introduce ROBIN, a...
  </details>

- **2026-07-14** — Yize Mi, Jianan Li, Liang Li et al. — [Unveiling Complex Collective Behaviors from Simple Rewards](http://arxiv.org/abs/2607.12861v1)
  <details><summary>📄 Abstract</summary>
  Multi-agent Reinforcement Learning (MARL) holds great potential for robot swarms, but the black-box nature of neural policies complicates strategic analysis, limiting multi-robot applications. Furthermore, complex swarm behaviors can surprisingly emerge from simple rewards without explicit aggregation incentives. Unveiling the mechanisms behind this emergence is critical, but the disconnection between simple rewards and collective behaviors exacerbates interpretability challenges. This paper aim...
  </details>

- **2026-07-14** — Hiroto Osaka, Shohei Taniguchi, Gouki Minegishi et al. — [Visual Access Boundaries in Vision-Language Model Reasoning](http://arxiv.org/abs/2607.12815v1)
  <details><summary>📄 Abstract</summary>
  Chain-of-Thought (CoT) prompting is widely used as a test-time scaling strategy for Vision-Language Models (VLMs), but it remains unclear what is extended when VLMs generate longer reasoning traces. We ask whether CoT requires continued access to image tokens, or whether it mainly operates over visual information already made available earlier in the forward pass. We introduce Visual Access Sweep, a causal intervention that masks attention from generated-token queries to image-token keys along l...
  </details>

- **2026-07-14** — Viktor A. Lilja, Philippe Tassin — [Symmetry-Informed Deep Learning for Electromagnetic Scattering](http://arxiv.org/abs/2607.12810v1)
  <details><summary>📄 Abstract</summary>
  Deep learning can accelerate the modeling of electromagnetic devices by replacing costly simulations with neural networks trained to map design parameters to scattering parameters. However, data efficiency remains a central bottleneck, as training data is typically generated through expensive numerical simulations. Here we show that symmetry provides a powerful and largely untapped route to overcoming this limitation in electromagnetic scattering problems. Leveraging the equivariance of Maxwell'...
  </details>

- **2026-07-14** — Aleksei Bakin, Andrey V. Savchenko — [HSEmotion Team at the 11th ABAW Challenge: Multi-Task Learning and Ambivalence/Hesitancy Video Recognition](http://arxiv.org/abs/2607.12774v1)
  <details><summary>📄 Abstract</summary>
  This article presents our results for the 11th Affective Behavior Analysis in-the-Wild (ABAW) competition. For multi-task learning with simultaneous prediction of valence, arousal, facial expressions, and action units on s-Aff-Wild2 dataset, we use frozen lightweight facial extractors, MT-EmotiDDAMFN and MT-EmotiEffNet-B0, with separate heads and systematic post-processing: temporal Gaussian smoothing, per-class expression bias, AffectNet blending, per-AU threshold tuning, and weighted backbone ...
  </details>

- **2026-07-14** — Xingyu Dang, Haocheng Tang, Junmei Wang et al. — [Learning Mechanistic Reasoning for Chemical Reactions with Large Language Models](http://arxiv.org/abs/2607.12771v1)
  <details><summary>📄 Abstract</summary>
  Reaction mechanisms consist of the step-by-step sequences of elementary reactions that explain chemical transformations. Learning the mechanism logic is therefore essential for enhancing the fundamental chemical intelligence of large language models (LLMs). The stepwise deduction of reaction mechanism aligns naturally with the reasoning paradigms of reasoning LLMs. However, current chemical LLMs primarily emphasize coarse-grained name reactions for product prediction and retrosynthesis, often le...
  </details>

- **2026-07-14** — Sanjaya Paudel, Suk-Jin Yoon, Tek Prasad Adhikari et al. — [Tidal Grinding of Dwarf Galaxies in Cluster Environments](http://arxiv.org/abs/2607.12694v1)
  <details><summary>📄 Abstract</summary>
  Dwarf elliptical galaxies (dEs) dominate galaxy clusters and provide key constraints on environmentally driven galaxy evolution. Here we examine whether the projected shapes of dEs retain information about their accretion and transformation histories using a homogeneous sample of 1,108 bright (m_g < 19 mag) dEs in the Virgo cluster. Based on the axis-ratio (b/a), we define flat (< 0.70) and round (> 0.74) subsamples and compare their spatial and kinematic properties. We find that flat dEs are di...
  </details>

- **2026-07-14** — Mahmoud Elkarargy, Abdelaziz Rahwan, Abdelrahman Elsayed et al. — [Quantum PDE Solvers in Practice: Application-Driven Benchmarking of the Heat Equation](http://arxiv.org/abs/2607.12688v1)
  <details><summary>📄 Abstract</summary>
  Quantum PDE solvers are difficult to evaluate in practice because published studies use different discretizations, output models, reconstruction rules, and hardware assumptions. We present a reproducible, application-driven benchmark for the 1-D Dirichlet heat equation that compares eleven kernels under the same problem instances and readout contract. The benchmark covers coherent linear solvers (HHL, QSVT, and QLS-Fourier), VQLS, imaginary-time methods (QITE, var-QITE, and AVQDS), real-time Ham...
  </details>

- **2026-07-14** — Chengguang Gan, Zhixi Cai, Yunhao Liang et al. — [A Learning-Rate-Gated Failure of GRPO in a Small Language and Vision-Language Model Web Agent: A Controlled Null and Its Mechanism](http://arxiv.org/abs/2607.12640v1)
  <details><summary>📄 Abstract</summary>
  Reinforcement learning with verifiable rewards, and Group Relative Policy Optimization (GRPO) in particular, is now run routinely on a supervised checkpoint in the hope of producing a stronger agent. We ask whether it adds skill to a small language and vision-language model web agent at the 4B to 8B scale, or whether it mostly reshapes behavior the supervised model already has. Across a control grid of 18 runs that varies learning rate, KL weight, seed, initialization, and clipping, no configura...
  </details>

- **2026-07-14** — Sachin Dev Duggal, Pradyumna Swarnalatha Ramanna, Alexandros Vassiliades — [Atomic Units of X: The Compression Layer of Intelligence](http://arxiv.org/abs/2607.12634v1)
  <details><summary>📄 Abstract</summary>
  This paper proposes a theoretical framework for understanding intelligence as a process of atomic compression and compositional reuse. We argue that cognitive, biological, computational, and organizational systems achieve scalable intelligence by decomposing complex phenomena into reusable atomic units that can be recombined into higher-order structures. Drawing on evidence from cognitive science, information theory, evolutionary biology, software engineering, medicine, legal reasoning, educatio...
  </details>

- **2026-07-14** — Minh Khoi Ho, Zihao Zhu, Runchuan Zhu et al. — [Can Induced Emotion Bias LLM Behaviors in Sequential Decision Making?](http://arxiv.org/abs/2607.12631v1)
  <details><summary>📄 Abstract</summary>
  As Large Language Models (LLMs) are increasingly deployed as autonomous agents in high-stakes domains, understanding contextual factors that may modulate their decision-making becomes critical. While LLMs are trained to perceive and resonate with users' emotions, it remains unclear whether induced emotion can influence their sequential decision-making. We investigate this question using the Iowa Gambling Task (IGT), a classic psychological paradigm for studying decision-making under uncertainty,...
  </details>

- **2026-07-14** — Yunxin Li, Jinchao Li, Shibo Su et al. — [KnowAct-GUIClaw: Know Deeply, Act Perfectly, Personal GUI Assistant with Self-Evolving Memory and Skill](http://arxiv.org/abs/2607.12625v2)
  <details><summary>📄 Abstract</summary>
  OpenClaw has emerged as a leading agent framework for complex task automation, yet it faces insufficient cross-platform GUI interaction support and a well-built self-evolution mechanism. These flaws limit its adaptation to diverse device ecosystems and prevent performance improvements through continuous learning from execution experience. To resolve these issues, we propose the Know Deeply, Act Perfectly paradigm for personal assistants, which holds that accumulated user interaction and task-run...
  </details>

- **2026-07-14** — Ryotaro Shimada, Yu-Chieh Lin, Yuji Nozawa et al. — [Towards Vision-Free CIR: Attribute-Augmented Scoring and LLM-Based Reranking for Zero-Shot Composed Image Retrieval](http://arxiv.org/abs/2607.12621v1)
  <details><summary>📄 Abstract</summary>
  Recent work has shown that "Vision-Free'' approaches (representing images as text) can be effective for standard image retrieval tasks. However, it remains unclear whether this paradigm can effectively handle a more complex, multimodal task, Composed Image Retrieval (CIR), due to the inherent information loss in textual descriptions. In this paper, we introduce a Vision-Free CIR framework that addresses this challenge through two key techniques: (1) Attribute-Augmented Hybrid Scoring, which comp...
  </details>

- **2026-07-14** — Ruocong Tang, Yang Huang, Xing Fang et al. — [Cheaper is Better: A Discount-Aware Network for Conversion Rate Prediction in E-commerce Recommendation System](http://arxiv.org/abs/2607.12578v1)
  <details><summary>📄 Abstract</summary>
  Post-click conversion rate (CVR) is a crucial element in online recommendation systems, which addresses significant challenges such as data sparsity (DS), sample selection bias (SSB), and delayed feedback. However, the impact of item discount rate-a key factor influencing both pricing and user purchasing behavior, has received limited attention. In this paper, we introduce the Discount-Aware Network (DANet) to model the relationship between item discount rates and CVR. DANet comprises three main...
  </details>

- **2026-07-14** — Kaixiang Shu — [From Preimage Search To Source-Grounded Feature Inversion](http://arxiv.org/abs/2607.12526v1)
  <details><summary>📄 Abstract</summary>
  Interpreting a neural network requires understanding what its internal features extract from a particular input. Feature inversion seeks to express a selected feature in the input domain, but canonical iterative methods search for an input whose re-encoded representation matches the target. Because many inputs can satisfy this constraint, target matching alone does not specify the inverse associated with the sample that generated the feature. We formulate source-grounded feature inversion by con...
  </details>

- **2026-07-14** — Junshi Chen, Xuhong Li, Russ Whiton et al. — [Cellular Signal Constructed Convolutional Vision Transformer for High Accuracy Positioning](http://arxiv.org/abs/2607.12518v1)
  <details><summary>📄 Abstract</summary>
  Modern cellular systems employ wide bandwidths and large antenna arrays to meet high data rate requirements. The high spatial and temporal resolution for communication also enables high-accuracy positioning as an ancillary benefit. Standard convolutional neural networks (CNNs) and vision Transformers have demonstrated excellent performance in positioning by leveraging delay-angle domain channel representations. However, they still face practical challenges in complicated cellular environments wi...
  </details>

- **2026-07-14** — Zhiyuan Liu, Yihe Li, Trevor E. Carlson et al. — [When is LLM-Based Program Reasoning Correct? A Completion Semantics for LLM-Based Code Inference](http://arxiv.org/abs/2607.12490v1)
  <details><summary>📄 Abstract</summary>
  Due to token and cognitive limits, Large Language Models (LLMs) typically perform program reasoning over incomplete code fragments/prompts rather than complete programs. Such reasoning therefore must rely on {assumptions about omitted code and context. As a result, the meaning of an inference over a program fragment is not absolute, but depends on an implicit completion model describing how the fragment may be refined into a complete program. In this paper, we introduce completion semantics for ...
  </details>

- **2026-07-14** — Ingmar Posner, Anson Lei, Bernhard Schölkopf — [From Observation to Insight: Mechanistic World Models and the Quest for Autonomous Discovery](http://arxiv.org/abs/2607.12474v2)
  <details><summary>📄 Abstract</summary>
  Recent advances in foundation models have transformed AI for Science, enabling remarkably accurate predictive performance across domains ranging from protein folding to weather forecasting. Yet prediction alone does not constitute scientific discovery. Scientific understanding depends on uncovering the reusable explanatory mechanisms that generate observations, whereas contemporary machine learning remains fundamentally organised around predictive mappings rather than explanatory structure. In t...
  </details>

- **2026-07-14** — Jinjian Wu, Jiaqi Tang, Wei Wei et al. — [IQA-T1: Tool-based Visual Evidence Reasoning for Image Quality Assessment](http://arxiv.org/abs/2607.12375v1)
  <details><summary>📄 Abstract</summary>
  Image Quality Assessment (IQA) in open-world environments remains challenging due to limited generalization and interpretability. Recent approaches based on multimodal large language models (MLLMs) introduce textual reasoning for quality prediction, yet their judgments rely heavily on semantically biased internal representations, making them insensitive to low-level perceptual degradations. We propose IQA-T1, a tool-based visual evidence reasoning framework that augments MLLM reasoning with expl...
  </details>

- **2026-07-14** — Shipeng Liu, Zhanping Song, Liang Zhao et al. — [Semantic-Edge Response Decoding of SAM3 for Zero-Shot Crack Segmentation](http://arxiv.org/abs/2607.12292v1)
  <details><summary>📄 Abstract</summary>
  Crack segmentation is essential for infrastructure inspection and structural health assessment, but existing high-performance methods typically require task-specific pixel-level annotations and training. Text-promptable vision foundation models enable zero-shot deployment, yet their final mask proposals are poorly suited to thin, fragmented, and low-contrast cracks, whose evidence may be suppressed, truncated, or over-expanded during mask generation. We find that language-conditioned semantic re...
  </details>

- **2026-07-14** — Chun-Yi Kuan, Hung-yi Lee — [The Sound of Absence: Audio-Language Embedding Models Struggle with Negation](http://arxiv.org/abs/2607.12290v1)
  <details><summary>📄 Abstract</summary>
  Audio-language embedding models such as CLAP are widely evaluated on matching present sound events, but rarely on negation. We show this affirmation-only evaluation hides a key limitation: these models fail to encode negated sound concepts, mapping affirmative and negated captions to nearly identical representations. To expose this blind spot, we introduce NegEval-Audio, a framework that converts existing datasets into two negation-aware tasks, Retrieval-Neg and Multiple-Choice Negation (MCQ-Neg...
  </details>

- **2026-07-14** — Siqi Wang, Xianjie Chen, Shaofeng Deng et al. — [SlimPer: Make Personalization Model Slim and Smart](http://arxiv.org/abs/2607.12281v1)
  <details><summary>📄 Abstract</summary>
  Transformer-style architectures are increasingly adopted for industrial recommendation systems, yet they inherit a design premise misaligned with the task: generative models rely on per-token autoregressive prediction, which justifies maintaining large intermediate tensors that scale with sequence length. In contrast, recommendation systems produce a single set of relevance scores for each <user, item> pair without token-level supervision. Leveraging this observation, we propose SlimPer, which r...
  </details>

- **2026-07-14** — Gendo Kumoi, Fumie Watanabe, Tota Suko et al. — [A Semi-Automated System for Generating Dialogue-Based TTS Lessons Using Large Language Models: An Exploratory Study of Educational Potential](http://arxiv.org/abs/2607.12235v1)
  <details><summary>📄 Abstract</summary>
  This study proposes a semi-automated system for generating dialogue-based lessons using Large Language Models (LLMs) and Text-to-Speech (TTS) technology, and exploratorily examines its educational potential via a practical quasi-experiment. The system augments rather than replaces educators through a three-stage human-in-the-loop workflow (LLM-based slide/narration generation, educator review, automated audiovisual integration), and introduces a novel method for generating Expert-Novice dialogue...
  </details>

- **2026-07-13** — Anna Gerchanovsky, Lujo Bauer, Michael K. Reiter — [MindReader: Using LLMs to Encourage Memorable and Secure Password Replacement](http://arxiv.org/abs/2607.12148v1)
  <details><summary>📄 Abstract</summary>
  We report on the design and evaluation of MindReader, a tool that helps a user replace her password when she is required to do so. Left to their own devices, users tend to replace their previous passwords with predictable variations of the original ones. MindReader leverages LLMs to suggest password variations that are chosen to be easy for the user to remember but harder for an attacker to predict. To do this, MindReader infers the meaning behind original password components and then suggests s...
  </details>

- **2026-07-13** — Zedong Peng, Chenggang Wang, Shangyue Zhu — [Cross-Cutting Security Analysis of LLM-Generated Code via Metamorphic Testing and Association Rule Mining](http://arxiv.org/abs/2607.12089v1)
  <details><summary>📄 Abstract</summary>
  Large language models (LLMs) frequently generate code with security vulnerabilities, yet these weaknesses are rarely isolated: they often span multiple concern areas simultaneously, reflecting the cross-cutting nature of security in software. We present a framework that combines security-oriented Metamorphic Relations (MRs) with Association Rule (AR) mining to detect vulnerabilities in LLM-generated code, uncover their co-violation structure, and trace that structure back to prompt-level risk fa...
  </details>

- **2026-07-13** — Rafael Ferreira da Silva, Milad Abolhasani, Peter Beaucage et al. — [Toward Trustworthy Autonomous Science: A Two-Year Community Roadmap](http://arxiv.org/abs/2607.12113v1)
  <details><summary>📄 Abstract</summary>
  One year ago, the AISLE roadmap argued that autonomous laboratories operated as isolated islands and proposed a grassroots network organized around five critical dimensions. The field has since moved faster than anticipated. Multi-agent systems have produced experimentally validated hypotheses, self-driving laboratories have grown more interoperable and orchestrated, reasoning-trained and domain foundation models have raised the capability ceiling, and the Genesis Mission has placed autonomous e...
  </details>

- **2026-07-13** — Ruipeng Xing, Yanan Li, Zhen Shang et al. — [Defeating Barren Plateaus with Task-Aligned Symmetry](http://arxiv.org/abs/2607.12100v1)
  <details><summary>📄 Abstract</summary>
  Barren plateaus -- the exponential vanishing of gradients -- are a fundamental obstacle to training scalable quantum neural networks. Whether they arise in quantum recurrent neural networks (QRNNs), a natural architecture for sequential data, remains a pressing question. Here we show that the decisive ingredient for trainability in QRNNs is not the recurrent circuit topology per se, but enforcing time-translation symmetry through parameter sharing across time steps. We prove that, without parame...
  </details>

- **2026-07-13** — Nikita Kozodoi, Zainab Afolabi, Jack Butler — [Are we Merging the Right Models? Impact of Expert Training Duration on Model Merging for LLMs](http://arxiv.org/abs/2607.11997v2)
  <details><summary>📄 Abstract</summary>
  Multi-task model merging combines separately trained expert models into a single model that handles all tasks without co-training. Standard practice merges experts at their optimal validation loss. We challenge this convention by systematically studying how training duration of domain experts affects the quality of the merged model. We fine-tune experts on five domains (Math, Code, Instruction Following, Multilingual, and Safety) across three model sizes (Qwen 3.5 0.8B, 2B, and 4B), saving check...
  </details>

- **2026-07-13** — Ananda Dhakal, Krish Neupane, Aarjan Chaudhary — [Baselines Before Architecture: Evaluating Coding Agents for Autonomous Penetration Testing](http://arxiv.org/abs/2607.13085v1)
  <details><summary>📄 Abstract</summary>
  Recent autonomous penetration testing papers report high benchmark scores while adding multi-component security harnesses around frontier LLMs. Because these systems often change both architecture and backbone model, it is difficult to tell how much performance comes from the harness rather than from the underlying model.   This paper presents a controlled study on the 104-task XBOW benchmark using default coding CLI agents as plain-agent baselines. We first run Codex, OpenCode, and Pi with the ...
  </details>

- **2026-07-13** — Yannick Lehmen, Marvin Wyrich, Anna-Maria Maurer et al. — [Predicting Program Comprehension with Foundation Models of Human Cognition](http://arxiv.org/abs/2607.11372v2)
  <details><summary>📄 Abstract</summary>
  Software engineering depends on the ability of developers to understand code, yet predicting how they do so remains an open challenge despite decades of research. Existing approaches rely either on simplified proxy measures that limit accuracy or on non-trivial measurements requiring elaborate experimental setups that are difficult to scale and apply in practice. In contrast, recent work in psychology suggests an alternative perspective: Instead of modeling task-specific phenomena directly, huma...
  </details>

- **2026-07-13** — Anna Neumann, Jasmin Wyss, Ivy Turk et al. — [It is not enough to give your moderation rules to ChatGPT: Policy-as-Prompt Moderation and Its Potential Impacts on Community Governance](http://arxiv.org/abs/2607.12149v1)
  <details><summary>📄 Abstract</summary>
  Content moderation practices and governance paradigms are changing rapidly, as fewer human moderators are deployed as `experts' by social media companies in a centralized manner. Instead, the companies are focusing more on community approaches, relying on volunteers to provide accurate information and make correct decisions. In decentralized moderation, communities have always relied on volunteers, updated community guidelines, and internal discussions thereof. For both content moderation paradi...
  </details>

- **2026-07-13** — Sheng Xu, Junhua Wang, Boyuan Huang et al. — [Amplitude-Only FFN Intervention for Tool-Structured LLM Inference Method: Gated Evaluation Protocol, and Cross-Model Empirical Results](http://arxiv.org/abs/2607.11183v2)
  <details><summary>📄 Abstract</summary>
  Large language models increasingly operate as tool-using agents, where small format, argument, or function-call errors can invalidate otherwise plausible responses. We study inference-time feed-forward network (FFN) intervention for improving structured outputs without retraining model weights. Our project began with Orthogonal Residual Projection (ORP), a direction-changing repair attempt that revealed sensitive SwiGLU FFN intervention sites but often caused more harm than fixes. We therefore p...
  </details>

- **2026-07-13** — Brenda Lelis, Rodrigo Cabral-Carvalho — [RCWT: Measuring Task-Budget Displacement from Coordination Content in LLM Calls](http://arxiv.org/abs/2607.12216v1)
  <details><summary>📄 Abstract</summary>
  Multi-agent and memory-augmented LLM systems often place coordination content, shared state, prior discussion, tool outputs, summaries, and role instructions, inside the same finite prompt used for the current task. This creates a practical allocation problem: every token spent on coordination is unavailable to task instructions or evidence when a call is assembled under a fixed context budget. We introduce the Roundtable Context Window Test (RCWT), a controlled protocol for measuring this task-...
  </details>

- **2026-07-13** — Rasiq Hussain, Darshil Italiya, Joshua Oltmanns et al. — [Fine-Tuned Multi-Agent Framework for Detecting OCEAN in Life Narratives](http://arxiv.org/abs/2607.12215v1)
  <details><summary>📄 Abstract</summary>
  Accurately assessing personality from text is challenging because traits are latent, context-dependent, and often subtly expressed across long narratives. Large language models (LLMs) offer new opportunities by processing extensive textual contexts, but pretraining of these models can induce latent "personality-like" biases, making single-model inferences inconsistent. We propose a fine-tuned multi-agent framework for detecting OCEAN personality traits, in which sub-agents are conditioned to ado...
  </details>

- **2026-07-13** — Jiahao Luo, Hao Zhang, Jianqi Chen et al. — [RegHead: Non-Humanoid Head Blendshapes via Feed-Forward Registration](http://arxiv.org/abs/2607.12206v1)
  <details><summary>📄 Abstract</summary>
  We present RegHead, a framework for constructing semantic blendshape sets for animatable non-humanoid head avatars. With a fixed expression vocabulary, semantic blendshapes provide a low-dimensional and interpretable animation interface and support cross-identity retargeting. Building such blendshape sets remains expensive because (i) expression-consistent supervision is scarce, (ii) generated 4D assets typically lack correspondence, and (iii) facial motion is highly localized. We propose (1) a ...
  </details>

- **2026-07-13** — Pradyumna Elavarthi, Arun J. Bhattacharjee, Harrison Lisabeth et al. — [From Reconstruction to Interpretation: Zero-Setup Multi-Phase Segmentation of X-ray Tomography Data](http://arxiv.org/abs/2607.12175v1)
  <details><summary>📄 Abstract</summary>
  X-ray tomography enables nondestructive characterization of material microstructures, while advances in micro-CT imaging have accelerated volumetric data acquisition and reconstruction. However, rapid interpretation remains limited by image segmentation, which often requires manual thresholding, user prompting, or material-specific model training. We present a zero-setup framework for multi-phase segmentation of synchrotron X-ray tomography data that generates interpretable masks for previously ...
  </details>

- **2026-07-13** — Sarel Weinberger, Amir Hozez — [Token Reduction Is Not Cost Reduction](http://arxiv.org/abs/2607.12161v2)
  <details><summary>📄 Abstract</summary>
  Context-reduction layers for API-based coding agents, including command-output compressors, retrieval rankers, and API-boundary proxies, are commonly evaluated by how much context or tool output they remove. We ask a different question: which interventions actually reduce end-to-end billed cost while preserving task success?   Our primary evidence is a pre-specified, hash-frozen, paired campaign of 2,908 provider-billed Claude Code runs, of which 2,848 were analyzed, covering 103 tasks, seven re...
  </details>

- **2026-07-13** — Leonardo Modesto — [Superconductive or superfluid condensation in curved spacetime](http://arxiv.org/abs/2607.12133v1)
  <details><summary>📄 Abstract</summary>
  We provide a proof of unitarity for quantum field theory in a general spacetime. Our argument expresses the Bogoliubov transformations in terms of a unitary squeezing operator relating the initial and final Hilbert spaces. The $S$-matrix in curved spacetime is thus the product of the squeezing operator and the $S$-matrix in the out-Hilbert space (typically Minkowski). Since both factors are unitary, their product is unitary. It follows that the Bogoliubov in-vacuum is described by a BCS-like sta...
  </details>

- **2026-07-13** — Tiberiu Musat, Tiago Pimentel, Nicolas Zucchet et al. — [Invariant Learning Dynamics of Transformers in Inductive Reasoning Tasks](http://arxiv.org/abs/2607.11875v2)
  <details><summary>📄 Abstract</summary>
  We present a theoretical framework to explain the emergence of inductive reasoning abilities in Transformer language models. While previous works on Transformer learning dynamics have so far been mostly tied to specific tasks, we study a generalized class of inductive tasks that unifies several synthetic tasks known in the literature, including in-context n-grams and multi-hop reasoning. In this class, we theoretically prove that the training dynamics of attention models can be confined to a hig...
  </details>

- **2026-07-13** — Nishant Aggarwal, Ayushi Dubal, Sreeraj Kannakarankodi et al. — [Can LLMs Perform Deep Technical Comprehension of Computer Architecture Papers?](http://arxiv.org/abs/2607.11859v1)
  <details><summary>📄 Abstract</summary>
  Can large language models perform deep technical comprehension of computer architecture papers -- not summarization, but structured critique that names the core mechanism, surfaces buried assumptions, and connects a contribution beyond its own scope? We study Gauntlet, an open-source pipeline that analyzes a paper through five independent expert-persona reviewers and an adversarial synthesis stage. On 20 ISCA 2025 and HPCA 2026 papers, ten researchers each wrote their own analyses and then judge...
  </details>

- **2026-07-13** — Ying Yan, Liwei Hu, Xiaoming Zhang — [IG-GAN: A Generative Adversarial Network for Aerodynamic Data Generation Based on Intrinsic Geometry](http://arxiv.org/abs/2607.11497v1)
  <details><summary>📄 Abstract</summary>
  Existing generative models learn data distributions in flat Euclidean space. However, most data in our real world are manifolds embedded in high dimensional Euclidean space. Therefore, we propose an intrinsic-geometry-based generative adversarial network (IG-GAN) for data generation in the field of aerodynamics. The generator of the IG-GAN represents aerodynamic data as a piecewise smooth manifold constructed by Bézier surfaces, and the generator tries to learn the coefficients of each Bézier su...
  </details>

- **2026-07-13** — Zahra Mousavi, Chadni Islam, M. Ali Babar et al. — [Understanding the Impact of AI Code Assistants on Security API Usage: An Empirical Study](http://arxiv.org/abs/2607.11348v1)
  <details><summary>📄 Abstract</summary>
  AI code assistants are transforming software development, but their implications for software security remain a major concern, particularly in the context of security APIs. These APIs are critical for safeguarding software systems, yet their complexity often leads to incorrect use and serious vulnerabilities. Developing an evidence-based understanding of how AI assistants influence developers' use of these APIs is therefore essential for informing effective mitigation strategies. While a few use...
  </details>

- **2026-07-13** — Saba Imran, Debanjum Singh Solanky — [ResearchQA: Benchmarking Citation-Grounded Question-Answering on Scientific Papers](http://arxiv.org/abs/2607.11074v1)
  <details><summary>📄 Abstract</summary>
  Large language models are increasingly used to assist scientific reading, but existing evaluation methods often fail to detect whether answers are supported by verifiable citations. We introduce ResearchQA, a benchmark of 6,211 single-paper question-answer pairs from 494 open-access papers spanning eight domains and four question types: lookup, comprehension, multi-hop, and adversarial. ResearchQA is designed for citation-grounded evaluation: it permits multiple valid supporting passages for a c...
  </details>

- **2026-07-13** — Amirmahdi Mirfakhar, Maria-Florina Balcan, Hedyeh Beyhaghi — [Efficient Online Proportional Sampling with Applications to Smoothed Online Learning](http://arxiv.org/abs/2607.10963v1)
  <details><summary>📄 Abstract</summary>
  We study the problem of efficient online proportional sampling from a high-dimensional domain under a $σ$-smoothed adversary, where the sampling distribution is induced by a dynamically evolving weight function defined over a sequence of piecewise-structured partitions. This setting captures a broad range of applications, including principal-agent games (e.g., pricing and contract design), and algorithm configuration and parameter tuning. The central challenge is maintaining an efficient data st...
  </details>

- **2026-07-13** — Dian Wang, Jisang Park, Xiaomeng Xu et al. — [Mixture of Frames Policy: Multi-Frame Action Denoising for Bimanual Mobile Manipulation](http://arxiv.org/abs/2607.11884v1)
  <details><summary>📄 Abstract</summary>
  Robotic manipulation is inherently multi-frame: local actions may be simple in an end-effector frame, while transport, upright-object handling, and whole-body coordination are better represented in a base-aligned frame. However, modern diffusion-based visuomotor policies typically commit to a single predefined action frame, forcing one denoiser to model action distributions that are often unnecessarily complex in that frame. We propose Mixture of Frames Policy (MoF), a diffusion policy that perf...
  </details>

- **2026-07-13** — Shikai Qiu, Marc Finzi, Yujia Zheng et al. — [Requential Coding: Pushing the Limits of Model Compression with Self-Generated Training Data](http://arxiv.org/abs/2607.11883v1)
  <details><summary>📄 Abstract</summary>
  Compression is fundamental to intelligence. A model that can represent its training data as a short code has discovered regularities that enable generalization. Large neural networks may learn functions far simpler than their parameter counts suggest, but it is challenging to construct codes that realize this simplicity. Parameter-based methods such as quantization produce code lengths that scale with model size, insensitive to how much information the parameters store. Prequential coding bypass...
  </details>

- **2026-07-13** — Giulia Di Fede, Salvatore Andolina — [Supporting Reflection in LLM-based Exploratory Search](http://arxiv.org/abs/2607.11810v1)
  <details><summary>📄 Abstract</summary>
  Large Language Models (LLMs) can make exploratory search more efficient but may undermine the reflection and iterative sensemaking needed in unfamiliar domains. Existing LLM tools often prioritize rapid answers over supporting users in tracking how their understanding evolves and how well their strategies align with their goals. We present TrailLM, a system that helps users reconstruct and revisit their exploration paths to support reflection and metacognitive engagement during information seeki...
  </details>

- **2026-07-13** — Seung Hyun Hahm, Minh T. Dinh, SouYoung Jin — [StoryTeller: Training-Free Narrative Grounding for Long-Form Audio Description](http://arxiv.org/abs/2607.11798v1)
  <details><summary>📄 Abstract</summary>
  Long-form audio description (AD) requires more than describing visible actions: it must preserve characters, events, relationships, and story context across scenes so that blind and low-vision (BLV) audiences can follow a film. Modern video-language models (VLMs) are effective on short clips, but they often treat each moment independently, producing descriptions that miss who characters are, why events matter, and how the current scene connects to earlier narrative context. We propose StoryTelle...
  </details>

- **2026-07-13** — Ayoung Lee, Ryan Kwon, Yunxiang Zhang et al. — [MET: Theory-Grounded and Culture-Aware Multilingual Moral Reasoning](http://arxiv.org/abs/2607.11736v1)
  <details><summary>📄 Abstract</summary>
  Language models are increasingly used for moral decision-making across diverse linguistic and cultural contexts, yet existing work overlooks multilinguality on three aspects: 1) multilingual evaluation benchmarks use direct translation, failing to adapt culture-specific items; 2) inference-time methods for moral reasoning rely on static, English-centric scaffolds and lack grounding in moral theory; 3) training methods for moral decision-making typically require expensive supervision from stronge...
  </details>

- **2026-07-13** — Yuanzhi Liang, Xufeng Zhan, Haibin Huang et al. — [From World Action Models to Embodied Brains: A Roadmap for Open-World Physical Intelligence](http://arxiv.org/abs/2607.11689v1)
  <details><summary>📄 Abstract</summary>
  Artificial general intelligence ultimately requires agents that can reason and act in the physical world. Action models, vision-language-action policies, and world models have advanced this goal, while World Action Models (WAMs) are particularly promising because they connect candidate interventions with predicted consequences. However, progress remains fragmented: models use incompatible action spaces and prediction targets, datasets and tasks follow different conventions, and runtime systems e...
  </details>

- **2026-07-13** — Nimrod Talmon, Oghenekaro Elem — [Cardano's Voltaire Governance: Complete Specification and Research Program](http://arxiv.org/abs/2607.11601v1)
  <details><summary>📄 Abstract</summary>
  Blockchain governance, the set of processes by which decentralized protocols evolve, remains a fundamental challenge in balancing adaptability, security, and stakeholder representation. This technical report analyzes Cardano's Voltaire governance system, the on-chain framework introduced via CIP-1694 and enacted through the Chang hard fork in September 2024, and lays down a corresponding research program.   We make two contributions. First, we provide a complete technical specification of Voltai...
  </details>

- **2026-07-13** — Milan Brož, Tamara Čierniková, Ondřej Kozina et al. — [Linux disk encryption and self-encrypting drives -- A case study on Opal2 drives security](http://arxiv.org/abs/2607.11563v1)
  <details><summary>📄 Abstract</summary>
  Opal2 self-encrypting drives provide hardware-based disk encryption serving as an additional layer of protection, or a replacement, for software-based solutions. This paper presents a case study of real-world Linux integration of Opal2 drives and the security of Opal2 firmware. The study was conducted on a testbed of 38 commercial off-the-shelf Opal2 drives from various vendors using a black-box approach. We identified several firmware security issues and incompatibilities, which we responsibly ...
  </details>

- **2026-07-13** — Gong Sitong, Tianyu Yan, Caixin Kang et al. — [Vinci2: Providing Proactive Assistance in Continuous Egocentric Videos](http://arxiv.org/abs/2607.11523v1)
  <details><summary>📄 Abstract</summary>
  When should an intelligent assistant speak up without being asked? Continuous egocentric video offers rich, evolving context that enables a new form of assistance: one that is proactive rather than merely reactive. Yet existing approaches either wait passively for user queries or treat every detected event as requiring a response, without considering the user's history, current activity, or whether assistance would actually be welcome. We reframe proactive assistance as a context-dependent decis...
  </details>

- **2026-07-13** — Xue Qin, Sumesh Surendran Letha — [From GUI Tests to Conversational Interaction: A New Perspective on App-Specific Voice Assistants](http://arxiv.org/abs/2607.11387v1)
  <details><summary>📄 Abstract</summary>
  Voice assistants are widely deployed on mobile platforms, yet most are designed as system-level services that remain poorly aligned with application-specific behavior. As a result, enabling voice interaction at the app level requires developers to manually reimplement application logic, leading to high development and maintenance costs.   We propose an LLM-driven approach to automating the development of app-specific voice assistants by repurposing GUI test code, which encodes behavior-preservin...
  </details>

- **2026-07-13** — Yannick Lehmen, Marvin Wyrich, Anna-Maria Maurer et al. — [Predicting Program Comprehension with Foundation Models of Human Cognition](http://arxiv.org/abs/2607.11372v1)
  <details><summary>📄 Abstract</summary>
  Software engineering depends on the ability of developers to understand code, yet predicting how they do so remains an open challenge despite decades of research. Existing approaches rely either on simplified proxy measures that limit accuracy or on non-trivial measurements requiring elaborate experimental setups that are difficult to scale and apply in practice. In contrast, recent work in psychology suggests an alternative perspective: Instead of modeling task-specific phenomena directly, huma...
  </details>

- **2026-07-13** — Miguel Gomez Fernandez, David Castro Boga, Roi Mendez-Rial et al. — [Benchmarking Edge Inference Strategies for Deep Learning Models in Industrial Machine Vision](http://arxiv.org/abs/2607.11356v1)
  <details><summary>📄 Abstract</summary>
  Edge deployment is often the preferred solution for industrial machine vision systems when low latency, data security, or limited connectivity are critical requirements. Several frameworks are available to optimise inference on edge devices; however, relatively few studies have systematically compared their inference-time performance under industrial deployment conditions.   In this work, we present a comparative study of four widely used approaches for machine vision inference in industrial set...
  </details>

- **2026-07-13** — Chenglin Yu, Li Yin, Ying Yu et al. — [Compile, Then Page: Executable SOP Programs and a Capability-Gated Runtime for Procedural LLM Agents](http://arxiv.org/abs/2607.11346v1)
  <details><summary>📄 Abstract</summary>
  Enterprise agents must follow long-horizon, conditional, safety-critical standard operating procedures (SOPs). We compile machine-readable SOP constraints into executable pseudo-code and run them with a program-guided (PG) stack machine that pages the active frame while an LLM performs semantic execution. A three-arm SOPBench study across six models separates representation from runtime: compiled text never significantly hurts and gains up to 16.0 points where official prose underperforms. Runti...
  </details>

- **2026-07-13** — Rodrigo Labouriau — [Markov Properties of $k$-Record Processes via Order Statistics](http://arxiv.org/abs/2607.11283v1)
  <details><summary>📄 Abstract</summary>
  The theory of $k$-record values (Type 2 $k$-records) plays an important role in the study of partial extremes and in statistical inference based on record data. A common approach reduces the analysis of $k$-records associated with a distribution function $F$ to that of ordinary records from the transformed distribution $F_{1:k}(x)=1-(1-F(x))^k$. This representation is widely used to derive distributional and inferential results, often without an explicit construction of the underlying stochastic...
  </details>

- **2026-07-13** — Liqian Feng, Lintao Wang, Xiaochen Liu et al. — [Q-BridgeNet: A Quantization Network for Cross-Lingual Sign Language Translation](http://arxiv.org/abs/2607.11215v1)
  <details><summary>📄 Abstract</summary>
  Most sign language translation (SLT) methods focus on isolated native sign-spoken pairs (e.g., American Sign Language - English). Extending language-specific SLT models to multilingual translation would improve accessibility by enabling communication across diverse sign and spoken language communities. However, existing multilingual SLT approaches still struggle to learn a unified model that minimizes cross-lingual conflicts while capturing shared cross-lingual semantics and preserving language-...
  </details>

- **2026-07-13** — Changlun Li, Peixian Ma, Qiqi Duan et al. — [NextFund: A Unified Performance Tracking Platform for Agentic Portfolio Management](http://arxiv.org/abs/2607.11141v1)
  <details><summary>📄 Abstract</summary>
  Large language models (LLMs) based agents are beginning to participate in portfolio construction and market analysis, where decisions must be justified under evolving information and risk constraints. Current assessment practice, however, remains poorly aligned with this setting: many studies rely on static examinations or report only terminal portfolio returns, while the intermediate evidence, analyst judgments, and execution steps that produced those returns stay largely invisible. We introduc...
  </details>

- **2026-07-13** — Sunyoung Jung, Jiwoo Park, Yoonseok Choi et al. — [Controlling Motion Transfer in Diffusion Transformers via Attention Heads](http://arxiv.org/abs/2607.11081v1)
  <details><summary>📄 Abstract</summary>
  Diffusion Transformers (DiTs) have advanced video generation with high-quality, temporally coherent results. However, extending them to motion transfer, which requires following reference motion while aligning with a target prompt, remains challenging due to limited understanding of motion and structure representations within DiTs. We analyze video DiTs at the attention-head level and identify distinct heads specialized for motion and spatial structure. Based on this insight, we propose a head-a...
  </details>

- **2026-07-13** — Kimia Hamidieh, Lester Mackey, David Alvarez-Melis — [Domain-Aware Scaling Laws Uncover Data Synergy](http://arxiv.org/abs/2607.11052v1)
  <details><summary>📄 Abstract</summary>
  Machine learning progress is often attributed to scaling model size and dataset volume, yet the composition of data can be just as consequential. Empirical findings repeatedly show that combining datasets from different domains yields nontrivial interactions. For instance, adding code improves mathematical reasoning, while certain mixtures introduce interference that reduces model performance. We refer to these effects collectively as data synergy, where the contribution of multiple domains exce...
  </details>

- **2026-07-13** — Tianjing Zeng, Yuntao Hong, Zhongjun Ding et al. — [QwenPaw-Data: Bridging Facts, Methodology, and Execution for Autonomous Enterprise Data Analytics](http://arxiv.org/abs/2607.11019v1)
  <details><summary>📄 Abstract</summary>
  Enterprise data analysis is emerging as a distinct frontier for autonomous agents. Compared with general-purpose interaction and software engineering, it operates in an open, ambiguous, and continuously evolving environment. These characteristics call for a data-agent architecture that treats semantics, methodology, execution, and evolution as first-class system concerns. To this end, we introduce QwenPaw-Data, an agentic data system designed for enterprise intelligent data analysis. QwenPaw-Dat...
  </details>

- **2026-07-13** — Tingcong Liu, Tongshun Chen, Siyi Ma et al. — [Whole-Body Semantic-to-Actuation Grounding of Elephant-Inspired Soft-Trunk Motion via Lightweight Flow Matching](http://arxiv.org/abs/2607.11018v1)
  <details><summary>📄 Abstract</summary>
  For close-contact human-robot interaction (HRI), trunk-like continuum manipulators provide a physical channel for diverse whole-body expression, but grounding open-vocabulary responses into such robots is difficult: end-effector motion underspecifies body shape, whereas direct whole-body commands are high-dimensional and hard to keep feasible. We propose a whole-body semantic-to-actuation grounding framework for elephant-inspired soft-trunk HRI based on lightweight flow matching. The framework c...
  </details>

- **2026-07-13** — Hao Xu, Xinyu Wei, Sam Wells et al. — [Temporal Feature Distillation for Label-Efficient Precise Event Spotting in Sports Videos](http://arxiv.org/abs/2607.10998v1)
  <details><summary>📄 Abstract</summary>
  Precise Event Spotting (PES) requires distinguishing visually similar yet semantically distinct adjacent frames, making it fundamentally different from image classification and coarse action recognition. Although self-distillation methods such as DINO have shown strong representation learning ability in images, we find that directly applying them to PES is ineffective: without supervised guidance, subtle but crucial motion cues are often suppressed as noise, leading to representations that are i...
  </details>

- **2026-07-13** — Ali Ahmadi, Hamed Rahimi, Adrien Jacquet Cretides et al. — [Think When It Matters: Conditional VLM Reasoning for Social Navigation with RL Policies](http://arxiv.org/abs/2607.10991v1)
  <details><summary>📄 Abstract</summary>
  As mobile robots become more integrated into everyday human environments, social robot navigation is becoming essential for ensuring human comfort, safety, and trust. While reinforcement learning (RL) navigation policies provide the fast inference and reactive behavior necessary for real-time deployment, they still lack flexible semantic reasoning capabilities and often fail to generalize to complex social scenarios. Recent approaches have increasingly turned to vision-language models (VLMs) in ...
  </details>

- **2026-07-13** — Yunhai Feng, Natalie Leung, Jiaxuan Wang et al. — [A Minimalist Retargeting-Guided Reinforcement Learning Recipe for Dexterous Manipulation](http://arxiv.org/abs/2607.11874v1)
  <details><summary>📄 Abstract</summary>
  Recent work in humanoid whole-body control has found success with a simple recipe: retarget human motion to robot kinematic references, then train policies via reinforcement learning (RL) to track them. But how does this recipe transfer to dexterous manipulation? The answer is not obvious, as manipulation involves complex, contact-rich dynamics and requires delicate regulation of contact modes and forces. We present REGRIND, a minimalist retargeting-guided RL pipeline that learns dexterous manip...
  </details>

- **2026-07-13** — Sheng Xu, Boyuan Huang, Ke Jia et al. — [Amplitude-Only FFN Intervention for Tool-Structured LLM Inference Method: Gated Evaluation Protocol, and Cross-Model Empirical Results](http://arxiv.org/abs/2607.11183v1)
  <details><summary>📄 Abstract</summary>
  Large language models increasingly operate as tool-using agents, where small format, argument, or function-call errors can invalidate otherwise plausible responses. We study inference-time feed-forward network (FFN) intervention for improving structured outputs without retraining model weights. Our project began with Orthogonal Residual Projection (ORP), a direction-changing repair attempt that revealed sensitive SwiGLU FFN intervention sites but often caused more harm than fixes. We therefore p...
  </details>

- **2026-07-13** — Hengyuan Hu, Priya Sundaresan, Jensen Gao et al. — [VIA: Visual Interface Agent for Robot Control](http://arxiv.org/abs/2607.11119v1)
  <details><summary>📄 Abstract</summary>
  Robot manipulation is a complex task that requires visual understanding, physical reasoning, planning, and closed-loop control. General-purpose foundation models (FMs) have grown remarkably capable of some of these, especially vision and reasoning. To leverage this for generalist robot policies, current methods typically involve converting existing FMs into vision-language-action (VLA) models by fine-tuning on robot data to output low-level actions. However, VLAs are often orders of magnitude sm...
  </details>

- **2026-07-13** — Tiberiu Musat, Tiago Pimentel, Nicholas Zucchet et al. — [Invariant Learning Dynamics of Transformers in Inductive Reasoning Tasks](http://arxiv.org/abs/2607.11875v1)
  <details><summary>📄 Abstract</summary>
  We present a theoretical framework to explain the emergence of inductive reasoning abilities in Transformer language models. While previous works on Transformer learning dynamics have so far been mostly tied to specific tasks, we study a generalized class of inductive tasks that unifies several synthetic tasks known in the literature, including in-context n-grams and multi-hop reasoning. In this class, we theoretically prove that the training dynamics of attention models can be confined to a hig...
  </details>

- **2026-07-13** — Zixiang Xu, Sixian Li, Huaxing Liu et al. — [Inside the Unfair Judge: A Mechanistic Interpretability Account of LLM-as-Judge Bias](http://arxiv.org/abs/2607.11871v1)
  <details><summary>📄 Abstract</summary>
  Existing studies of LLM-as-judge scoring bias work predominantly at the input-output level: they perturb inputs, measure score deltas, and propose prompt-level mitigations. We argue that the same biases admit a representation-level account in the judge's hidden state, complementary to the input-output view and operationally useful in ways it does not afford. We report three findings, across seven judges, seven bias types, and nine benchmarks. Geometry: baseline judging inputs occupy a tight acti...
  </details>

- **2026-07-13** — Francesco Sorrenti, Erick Pastén, Leonardo Giani — [Reconstructing the kinematics of Laniakea using Type Ia Supernovae](http://arxiv.org/abs/2607.11860v1)
  <details><summary>📄 Abstract</summary>
  We develop a kinematic framework that relates the monopole, dipole, and quadrupole of the luminosity distance to an ellipsoidal peculiar velocity field describing the dynamics of the Laniakea supercluster. By properly accounting for the transformations between the CMB and Laniakea reference frames and selecting Type Ia supernovae within the volume associated with the superstructure, we show that luminosity distance multipoles encode the expansion and shear of the local velocity field. This allow...
  </details>

- **2026-07-13** — Yu-Han Huang, Chih-Kai Yang, Ke-Han Lu et al. — [Encoder-Side Neuron Identification and Amplification for Acoustic Perception in Large Audio-Language Models](http://arxiv.org/abs/2607.11801v1)
  <details><summary>📄 Abstract</summary>
  Large audio-language models (LALMs) often underperform on fine-grained, non-semantic attributes of speech, such as a speaker's emotion, despite strong performance on speech content. Improving this without the cost of retraining calls for an effective inference-time intervention, yet most existing methods intervene only after the audio encoder and operate at a relatively coarse granularity. The encoder itself, where acoustic information is first extracted from the waveform, remains largely unexpl...
  </details>

- **2026-07-13** — Jin Xu, Kangdi Wang, Ruibin Yuan et al. — [Qwen-Music Technical Report](http://arxiv.org/abs/2607.11699v1)
  <details><summary>📄 Abstract</summary>
  In this report, we introduce Qwen-Music, a powerful music generation model capable of producing highly musical and high-fidelity songs with complete vocal singing. Qwen-Music supports two core tasks: Text to Music Generation, which create entirely new songs from text descriptions, lyrics, and musical attributes, and Cover Song Generation, which reinterprets existing songs with different styles and vocal characteristics. Architecturally, Qwen-Music integrates three core components: Qwen-Music-Tok...
  </details>

- **2026-07-13** — Matteo Tuveri — [From Prompt Engineering to Epistemic Prompting: Prompt Trajectories as AI-Mediated Problem Framing in Science Education](http://arxiv.org/abs/2607.11680v1)
  <details><summary>📄 Abstract</summary>
  Prompt engineering is commonly presented as a technical competence for obtaining more accurate, relevant, or well-formatted outputs from large language models (LLMs). However, in STEM education, prompting should also be understood as a continuous epistemic practice. Students interpret contextual and disciplinary cues and adopt expectations about what kind of knowledge, representation, and action are appropriate. Drawing on epistemological framing, and AI-mediated concept-to-decision reasoning, t...
  </details>

- **2026-07-13** — Xin Zhang, Haochen Wang, Yikang Zhou et al. — [Actor as Its Own Critic: Unifying Region Understanding and Localization via CycleGRPO](http://arxiv.org/abs/2607.11581v1)
  <details><summary>📄 Abstract</summary>
  This paper introduces Actor as Its Own Critic, a unified reinforcement learning framework, Cycle Group Relative Policy Optimization (CycleGRPO), that jointly optimizes region understanding and localization for Multimodal Large Language Models (MLLMs). Unlike existing separate pipelines, we leverage the inherent duality between the two tasks to construct a self-evaluating reinforcement learning paradigm: "region $\to$ text $\to$ region''. Specifically, a single MLLM first acts as the actor to gen...
  </details>

- **2026-07-13** — Paul Garnier, Jonathan Viquerat, Elie Hachem — [Heuristic Learning for Active Flow Control Using Coding Agents](http://arxiv.org/abs/2607.11565v1)
  <details><summary>📄 Abstract</summary>
  Active flow control involves nonlinear dynamics, partial observations, and computationally expensive simulations, making controller design particularly challenging. Deep reinforcement learning (DRL) has emerged as a powerful framework for such problems, but its success typically relies on large numbers of simulator interactions and produces neural-network policies whose decision process often remains difficult to interpret. In this work, we investigate a different paradigm: instead of optimizing...
  </details>

- **2026-07-13** — Langyuan Cui, Chun Kai Ling, Hwee Tou Ng — [Communicating Chess Strategies in Natural Language](http://arxiv.org/abs/2607.11486v1)
  <details><summary>📄 Abstract</summary>
  Chess engines have long achieved superhuman playing strength. However, the underlying strategy behind their move suggestions is difficult for human players, even skilled ones, to comprehend. Motivated by this, we propose the task of chess strategy verbalization, which is to describe chess strategies in natural language. We design (i) a pipeline for verbalizing strategies and (ii) an evaluation framework for objective evaluation of generated strategy descriptions. Our experiments show that natura...
  </details>

- **2026-07-13** — Marlena Flüh, Soo-Yon Kim, Carolin Victoria Schneider et al. — [FAIR GraphRAG: A Retrieval-Augmented Generation Approach for Semantic Data Analysis](http://arxiv.org/abs/2607.11464v1)
  <details><summary>📄 Abstract</summary>
  Retrieval-Augmented Generation (RAG) addresses the limitations of Large Language Models (LLMs) when providing responses to domain-specific questions. Graph-based RAG approaches, such as GraphRAG, enhance retrieval by capturing semantic relationships within knowledge graphs (KGs). While the FAIR principles (Findability, Accessibility, Interoperability, and Reusability) are becoming prevalent for scientific data management, especially in complex domains such as medicine, existing RAG approaches la...
  </details>

- **2026-07-13** — Costas Mylonas, Magda Foti — [A Multimodal Dataset for Large Language Model Applications in the Energy Domain](http://arxiv.org/abs/2607.11459v1)
  <details><summary>📄 Abstract</summary>
  This paper presents the mAIEnergy dataset, an open-access, multimodal corpus developed to support Large Language Model (LLM) applications in the energy sector. The dataset integrates approximately 50,000 textual documents, 20,000 images, 25 million numerical time series records, and 2 million geospatial and relational data entries. It includes policy and regulatory texts, scientific articles and news articles, satellite and contextual imagery, electricity system measurements, weather observation...
  </details>

- **2026-07-13** — Wenyi Wu, Sibo Zhu, Kun Zhou et al. — [StructAgent: Harness Long-horizon Digital Agents with Unified Causal Structure](http://arxiv.org/abs/2607.11388v1)
  <details><summary>📄 Abstract</summary>
  Recent advances in large language models (LLMs) and vision-language models (VLMs) have enabled increasingly capable digital agents for computer use. However, real-world tasks are often long-horizon and involve evolving contexts containing accumulated observations, intermediate edits, failed attempts, and partially completed executions. Existing agents typically operate over raw interaction history, making task progress difficult to interpret, verify, and recover, which ultimately limits reliable...
  </details>

- **2026-07-13** — Leo van Iersel, Mark Jones, Esther Julien et al. — [Proximity Measures for Classes of Phylogenetic Networks](http://arxiv.org/abs/2607.11325v1)
  <details><summary>📄 Abstract</summary>
  Phylogenetic networks are used to represent the evolutionary history of species. Due to biological interpretations and computational advantages, researchers have focused on restricted classes of phylogenetic networks, such as tree-child, orchard, and tree-based. These classes capture different notions of tree-likeness: tree-child networks require every internal vertex to have a taxon reachable by a tree path, orchard networks are trees with horizontal arcs (for modelling histories rife with hori...
  </details>

- **2026-07-13** — Tatsuhiko Sato, Shintaro Hashimoto, Tatsuhiko Ogawa et al. — [Toward AI-Agent-Driven Particle Transport Simulations: Implementation of AI-Assisted Workflows for PHITS](http://arxiv.org/abs/2607.11309v1)
  <details><summary>📄 Abstract</summary>
  Monte Carlo particle transport codes are powerful tools, but their use requires substantial knowledge of input preparation, execution, and result analysis. In this study, we present a code-side strategy for applying existing AI assistants and AI agents to PHITS. Two complementary sets of AI-ready resources were prepared from manuals, lecture materials, sample inputs, utility information, and developer-curated cautions: a bundled knowledge base for retrieval-augmented generation (RAG)-based assis...
  </details>

- **2026-07-13** — Ciprian Cristescu, Adrian-Marius Dumitran, Angela-Liliana Dumitran et al. — [Automated Textbook Auditing with Multi-Agent LLM Systems](http://arxiv.org/abs/2607.11276v1)
  <details><summary>📄 Abstract</summary>
  Ensuring the quality of educational materials requires more than standard proofreading: textbooks must be audited for factual accuracy, domain-specific technical correctness, and linguistic quality simultaneously -- a task that general-purpose grammar checkers cannot address. We present \textbf{AI Textbook Auditor}, a modular multi-agent pipeline for automated quality assurance of educational materials across subject domains. The system accepts a textbook PDF and produces a structured, human-rev...
  </details>

- **2026-07-13** — Daeyeop Lee, Hwanjo Yu — [Valid $\ne$ Necessary: Diagnosing Latent Inefficiency in Chain-of-Thought](http://arxiv.org/abs/2607.11266v1)
  <details><summary>📄 Abstract</summary>
  Chain-of-Thought (CoT) prompting has significantly advanced the reasoning capabilities of Large Language Models (LLMs), yet it often incurs substantial computational costs due to over-reasoning: the generation of redundant, verbose, or irrelevant steps. While existing reasoning step evaluators effectively detect logical fallacies and factual errors, our analysis reveals a critical blind spot: they fail to penalize valid but inefficient reasoning steps that inflate token usage without contributin...
  </details>

- **2026-07-13** — Abdullah Mağden — [4x4 Matrix Representation of Hybrid Numbers, Gram Matrix and Golden Ratio](http://arxiv.org/abs/2607.11242v1)
  <details><summary>📄 Abstract</summary>
  This study investigates the Lie algebra structure and geometric properties of hybrid numbers, under a specific non-associative multiplication table. Within the scope of the study, the structure constants of the system were derived through commutator relations, and 4x4 matrix representation was constructed. By defining the Gram matrix, complex and hybrid conjugates, the connection of the eigenvalues of Gram matrices to the golden ratio has been obtained. Theoretical analysis reveal that this hybr...
  </details>

- **2026-07-13** — Sukai Huang, Chenyuan Zhang, Fucai Ke et al. — [What We Talk About When We Talk About LLM Planning: Evidence for Two Distinct Planning Abilities](http://arxiv.org/abs/2607.11197v1)
  <details><summary>📄 Abstract</summary>
  When LLMs exhibit uneven performance across planning tasks, these gaps are often attributed to task difficulty. We argue that this explanation is incomplete, as task-level variation may reflect distinct latent planning competencies rather than differences along a single ability spectrum. We study this question on ACPBench-Hard by evaluating multiple LLM families under varying test-time reasoning budgets and applying a multidimensional item response theory model to uncover the latent competency s...
  </details>

- **2026-07-13** — Ziang Ren, Guodong Lin, Yuchen Ai et al. — [Unified Gradient Projection: Language-Balanced Continual Learning for Multilingual Low-Resource ASR](http://arxiv.org/abs/2607.11163v1)
  <details><summary>📄 Abstract</summary>
  Large-scale pretrained ASR models such as Whisper exhibit strong multilingual capabilities. However, fine-tuning on low-resource languages often causes catastrophic forgetting. Although continual learning mitigates this issue, existing methods struggle to regulate cross-task interference in multilingual settings, where dominant languages bias optimization. We propose Unified Gradient Projection (UGP), which constrains parameter updates using reference gradients from language-balanced replay in a...
  </details>

- **2026-07-13** — Haoyu Gu, Lekai Qian, Haowu Zhou et al. — [BeatEdit: Symbolic Music Generation as Explicit Editing](http://arxiv.org/abs/2607.11124v1)
  <details><summary>📄 Abstract</summary>
  Music creation is fundamentally a process of revision. Yet symbolic music generation remains dominated by paradigms that produce complete sequences from scratch, with limited support for selective modification. Edit-based methods have proven effective for text transformation tasks, but remain largely unexplored for symbolic music. We trace this absence to the representational level: conventional event-based music encodings lack the structural properties required by explicit music editing. In con...
  </details>

- **2026-07-12** — Jinhui Hu, Guo Chen, Huaqing Li et al. — [RED-SEGA:Resilient Decentralized Stochastic Proximal Optimization with Gradient Sketching over Time-Varying Networks](http://arxiv.org/abs/2607.10791v1)
  <details><summary>📄 Abstract</summary>
  Variance reduction is indispensable in Byzantine-resilient decentralized stochastic optimization over multi-agent systems (MASs) for its ability to mitigate gradient noise and thereby enhance the resilient aggregation process. However, most existing Byzantine-resilient decentralized variance-reduced (VR) stochastic gradient algorithms rely on random data sampling, which proves inefficient in data-scarce yet high-dimensional tasks, for instance, image deblurring. This paper pursues an alternative...
  </details>

- **2026-07-12** — Yan Lin, Yuyang Dai, Jiahui Geng et al. — [AI YOU Town: Make Friends and Money with Your Digital Twin](http://arxiv.org/abs/2607.10539v1)
  <details><summary>📄 Abstract</summary>
  Existing approaches to infer user traits and generate responses consistent with a persona rely on static prompting. They lack calibrated uncertainty, ignore sequential evidence, and drift during long interactions. We present \textbf{AI YOU}, a framework that continually updates a personality profile with 22 dimensions from conversation and embodies it in a personal digital twin. Practically, the system combines prompting, Bayesian updating, and conformal prediction for persona inference. A perio...
  </details>

- **2026-07-12** — Xiangxin Zhou, Jiarui Yao, Penghui Qi et al. — [Predictive Divergence Masks for LLM RL](http://arxiv.org/abs/2607.10848v1)
  <details><summary>📄 Abstract</summary>
  Reinforcement learning for large language models (LLMs) typically relies on trust-region masks to stabilize off-policy updates. The dominant PPO-style approach uses the sampled-token importance ratio for two criteria: a proximity criterion, which asks whether the policy has moved too far from the behavior policy, and a direction criterion, which asks whether the update pushes it farther away. Recent work DPPO improves the proximity criterion by replacing PPO's ratio-based test with a probability...
  </details>

- **2026-07-12** — Sudipto Ghosh, Tanmoy Chakraborty — [Route, Communicate, and Reason: Gated Routing and Adaptive Depth for Efficient Multi-Agent Reasoning](http://arxiv.org/abs/2607.10836v1)
  <details><summary>📄 Abstract</summary>
  Multi-agent ensembling multiplies active parameters and inference cost without answering three basic questions: which agents to consult, how deeply a query should traverse a hierarchy of agents, and when inter-agent communication is worth its cost. We present GRADE (Gated Routing and Adaptive Depth for Efficient Reasoning), a hierarchical multi-agent system in which four lightweight learned gates jointly govern agent selection, hierarchy depth, inter-agent communication, and branch pruning. Trai...
  </details>

- **2026-07-12** — Matthias M. M. Buehlmaier — [LayerNorm as Implicit Gain Control in Looped Transformers](http://arxiv.org/abs/2607.10681v1)
  <details><summary>📄 Abstract</summary>
  In pre-LayerNorm looped transformers, LayerNorm inside the recurrent block acts as an implicit gain controller: by coupling the block's local Lipschitz constant inversely to the activation scale, it renders the recurrence Jacobian non-normal -- asymptotically contractive at every verified fixed point even where its operator norm exceeds 1 -- so the true stability budget is the spectral margin, not an operator-norm bound. That margin depletes as the carry $ρ\to 1$, and a minority of initializatio...
  </details>

- **2026-07-12** — Satoshi Kura, Hiroshi Unno — [Solving First-Order Fixed-Point Logics via a Least-to-Greatest Transformation Based on Game Semantics](http://arxiv.org/abs/2607.10650v1)
  <details><summary>📄 Abstract</summary>
  Fixed-point logics provide an expressive intermediate framework for reasoning about temporal properties of programs. One of the key approaches to solving their validity checking problem is via transformations from least fixed points to greatest fixed points ($μ$-to-$ν$ transformations), which generalizes a reduction from termination verification to safety verification studied in binary reachability analysis. In this paper, we introduce game-semantic interpretations of $μ$-to-$ν$ transformations....
  </details>

- **2026-07-12** — Tahmid Al Hannan, Diego Garcia, Alex Njoroge et al. — [Knowledge Distillation for Automated AI Tutor Evaluation](http://arxiv.org/abs/2607.10647v1)
  <details><summary>📄 Abstract</summary>
  The rapid integration of Large Language Models (LLMs) into K-12 and higher education has outpaced the development of reliable methods for evaluating their pedagogical quality. As the research community starts to explore the space of automating evaluation of AI tutors, we introduce FATE (FLC AI Tutor Evaluator), a specialized 8B-parameter language model designed to evaluate AI tutors. Aligned with the four core evaluation tracks from the BEA 2025 Shared Task, our model assesses pedagogical abilit...
  </details>

- **2026-07-12** — Ilia Karpov — [MafiaScope: Non-Invasive, Time-Resolved Belief Probing for LLM Agents in Social Deduction Games](http://arxiv.org/abs/2607.10645v1)
  <details><summary>📄 Abstract</summary>
  An LLM agent's public behaviour reveals little about its social reasoning: an agent that votes correctly may be guessing, and an agent that lies well leaves no trace of what it actually believes. We present MafiaScope, an open testbed that turns the social deduction game Mafia into a measurement instrument for machine Theory of Mind. After every public utterance, every agent privately answers a configurable set of structured probe questions; the answers never re-enter the game and are scored aut...
  </details>

- **2026-07-12** — Tiancheng Gao, Xiang Zhang, Wei Lan et al. — [Inferring Inventory Dynamics from Supply Chain Networks: A Graph Learning Approach with Autonomous Validation](http://arxiv.org/abs/2607.10642v1)
  <details><summary>📄 Abstract</summary>
  Supply-demand mismatch represents a fundamental challenge in supply chain management, yet its direct measurement remains particularly elusive for small and medium-sized enterprises (SMEs).These firms typically lack systematic inventory records, leaving labeled training data critically scarce. Conventional supervised learning methods rely heavily on labeled samples, rendering them ill-equipped to reliably validate firm-level predictions under such data-scarce conditions. To resolve this unlabeled...
  </details>

- **2026-07-12** — Yixiong Chen, Xinyi Bai, Alan Yuille — [The Compliance Trap: Diagnosing How AI Agents Consume Conflicting Memory](http://arxiv.org/abs/2607.10608v1)
  <details><summary>📄 Abstract</summary>
  Memory is becoming a core component of long-horizon AI agents, allowing agents to reuse past experience when operating web browsers, software tools, and other interactive environments. Existing work mostly treats memory as a supply problem, asking what experience to write, how to store it, and which entry to retrieve for the next task. Yet we still lack a clear account of how models consume retrieved memory across a multi-step action trajectory. This consumption process matters because it determ...
  </details>

- **2026-07-12** — Yu Mei, Qingyue Zhuang, Jie Cai et al. — [U-Lens: Supporting User Uncertainty Management in Long-Form LLM Responses](http://arxiv.org/abs/2607.10604v1)
  <details><summary>📄 Abstract</summary>
  Large language models (LLMs) are increasingly used to generate long-form answers for knowledge-intensive tasks, but users often struggle to decide which parts of a response deserve scrutiny, why they may be unreliable, and what to do next. Prior work on uncertainty communication has largely focused on making uncertainty visible through cues such as confidence scores, leaving less support for the broader process of managing uncertainty distributed across a long response. Through a formative study...
  </details>


## 📊 统计 / Statistics

| 分类 / Category | 论文数 / Count |
|------|--------|
| jailbreak | 545 |
| prompt-injection | 458 |
| memory-poisoning | 36 |
| tool-use-attack | 91 |
| backdoor | 386 |
| adversarial-attack | 531 |
| privacy-leakage | 3691 |
| steganography | 52 |
| misuse | 815 |
| red-teaming | 108 |
| vulnerability | 2449 |
| defense | 2074 |
| alignment | 1907 |
| robustness | 1786 |
| watermark | 181 |
| unlearning | 82 |
| agent-safety | 48 |
| benchmark | 54 |
| survey | 245 |
| other | 5453 |

---

📚 **全部 20992 篇论文**（2022 至今）请访问 [GitHub Pages](https://ny1024.github.io/AgentSafety-Papers/) 查看完整列表、搜索与筛选。

*Generated by AgentGuard at 2026-07-18 02:38:22*