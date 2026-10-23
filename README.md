<div align="center">

# AgentGuard 🛡️

**Daily Tracking of LLM Agent Security Papers on arXiv**

[![Auto Update](https://github.com/NY1024/AgentSafety-Papers/actions/workflows/daily-update.yml/badge.svg)](https://github.com/NY1024/AgentSafety-Papers/actions/workflows/daily-update.yml)
[![Papers](https://img.shields.io/badge/Papers-34264-blue)](#)
[![License](https://img.shields.io/badge/License-MIT-green)](#)

</div>

---

## 📖 简介 / Introduction

自动追踪 arXiv 上大模型 Agent 安全方向的最新论文，每日更新，关键词智能分类。

*Automatically tracking the latest LLM Agent security papers on arXiv, updated daily with keyword-based classification.*

**最近更新 / Last Updated**: 2026-10-23 03:00 ｜ **论文总数 / Total Papers**: 34264（近 30 天 / Recent 30 days: 5372）

🌐 **[GitHub Pages](https://ny1024.github.io/AgentSafety-Papers/)** — 查看全部 34264 篇论文（含摘要、分类筛选、搜索）/ View all 34264 papers with abstracts, filters & search

## 📑 分类导航 / Category Navigation

- **[jailbreak](#-jailbreak)** — 越狱攻击 / Jailbreak Attacks — 691
- **[prompt-injection](#-prompt-injection)** — 提示注入攻击 / Prompt Injection Attacks — 634
- **[memory-poisoning](#-memory-poisoning)** — 记忆投毒与篡改 / Memory Poisoning & Tampering — 56
- **[tool-use-attack](#-tool-use-attack)** — 工具使用攻击 / Tool-Use Attacks — 160
- **[backdoor](#-backdoor)** — 后门与投毒攻击 / Backdoor & Poisoning Attacks — 535
- **[adversarial-attack](#-adversarial-attack)** — 对抗攻击 / Adversarial Attacks — 648
- **[privacy-leakage](#-privacy-leakage)** — 隐私泄露 / Privacy Leakage — 4455
- **[steganography](#-steganography)** — 隐写与隐蔽通信 / Steganography & Covert Communication — 83
- **[misuse](#-misuse)** — 滥用与误用 / Misuse & Abuse — 1232
- **[red-teaming](#-red-teaming)** — 红队测试 / Red Teaming — 144
- **[vulnerability](#-vulnerability)** — 漏洞与攻击面 / Vulnerabilities & Attack Surfaces — 3727
- **[defense](#-defense)** — 防御与防护方法 / Defense & Protection Methods — 3593
- **[alignment](#-alignment)** — 对齐与安全约束 / Alignment & Safety Constraints — 3385
- **[robustness](#-robustness)** — 鲁棒性与可靠性 / Robustness & Reliability — 3684
- **[watermark](#-watermark)** — 水印与溯源 / Watermarking & Provenance — 651
- **[unlearning](#-unlearning)** — 机器遗忘 / Machine Unlearning — 117
- **[agent-safety](#-agent-safety)** — Agent 安全框架 / Agent Safety Frameworks — 66
- **[benchmark](#-benchmark)** — 安全评测与基准 / Safety Benchmarks & Evaluation — 70
- **[survey](#-survey)** — 综述与系统化 / Surveys & Systematization — 421
- **[other](#-other)** — 其他安全相关 / Other Security-Related — 9912

## 📄 近期论文 / Recent Papers (Last 30 Days)

> 仅展示最近 30 天中最新的 500 篇论文（含日期、作者、摘要）。近 30 天共 5372 篇，完整 34264 篇论文列表请访问 [GitHub Pages](https://ny1024.github.io/AgentSafety-Papers/)

> Showing the latest 500 of 5372 papers from the last 30 days (with date, authors & abstract). For the full list of 34264 papers, visit [GitHub Pages](https://ny1024.github.io/AgentSafety-Papers/)

### 📂 jailbreak
*越狱攻击 / Jailbreak Attacks* — 4 papers

- **2026-10-22** — Jinwei Gan, Zifeng Cheng, Zhiwei Jiang et al. — [Harmful Responses Are Jailbreak Templates: Transferring Autoregressive Jailbreaks to Diffusion Language Models](http://arxiv.org/abs/2610.31331v1)
  <details><summary>📄 Abstract</summary>
  Diffusion large language models (dLLMs) enable flexible masked generation through bidirectional context modeling, but this capability also introduces a distinct jailbreak attack surface. We find that a harmful response to a given query naturally serves as an effective jailbreak template: simply masking a subset of its tokens can induce a dLLM to reconstruct harmful content. Based on this observation, we propose RMT-Jailbreak, a general framework that transfers existing autoregressive (AR) jailbr...
  </details>

- **2026-10-22** — Abhishek Mishra, Sagnik Chatterjee, Suyash Maniyar — [Faithful Latent Harm Monitors Work No Better Than the Models Own Behaviour at a Matched False Alarm Rate](http://arxiv.org/abs/2610.30727v1)
  <details><summary>📄 Abstract</summary>
  Large language models have been reported to encode the harmfulness of a request separately from their decision to refuse it, and latent safety monitors such as Latent Guard build on this report by classifying prompts as harmful from the internal activations of the model, with the aim of catching harmful intent even when the model complies. Whether these representations give a signal of harm that survives distribution shift and is independent of model behaviour is unclear. We test this on out-of-...
  </details>

- **2026-10-21** — Hongyu Li, Xinlong Huang, Zhan Yu et al. — [Beyond Binary Labels: Diagnostic Evaluation of LLM Safety with Prompt-Level Rubrics](http://arxiv.org/abs/2610.29225v1)
  <details><summary>📄 Abstract</summary>
  Current LLM safety benchmarks predominantly rely on binary safe or unsafe labels, lacking explanatory depth and suffering from low consistency across automated judges. To address this, we introduce DiagSafe, a diagnostic evaluation framework that moves beyond binary classification by employing prompt-level rubrics. Grounded in globally applicable AI safety policies, each rubric provides explicit criteria along two dimensions: safety, which targets concrete harms with specific exemptions to suppr...
  </details>

- **2026-10-20** — Pedro H. Barcha Correia, Matheus Azevedo de Sá, Paulo H. Gomes de Senna et al. — [Combining Long-Term Memory and LLMs Comes at a High Cost: From Prompt Injection to Persistent Compromise](http://arxiv.org/abs/2610.28810v1)
  <details><summary>📄 Abstract</summary>
  The widespread adoption of generative artificial intelligence in recent years has brought a parallel rise in prompt injection and jailbreak attacks. By embedding malicious instructions, these exploits manipulate language models to bypass intended behavior and operational boundaries. In traditional chatbots, such attacks are confined to a single session because state memory is not preserved across conversations. However, persistent memory features in modern conversational interfaces enable cross-...
  </details>


### 📂 prompt-injection
*提示注入攻击 / Prompt Injection Attacks* — 8 papers

- **2026-10-22** — Chao Gu, Quanyan Zhu — [Certified Execution Harness for Agentic AI: Safe and Least-Intrusive Petri-Net Supervisory Control Between Reasoning and Action](http://arxiv.org/abs/2610.31376v1)
  <details><summary>📄 Abstract</summary>
  This paper studies the problem of safe tool execution for large language model (LLM) agents under prompt injection. Using Petri nets, we formalize the execution harness between the LLM and its tools as a supervisory control problem, in which marks represent capabilities, approvals and budgets. Since a transition fires only if the marks it needs are present, an injected request whose preconditions are unmet or already spent is refused regardless of its wording. Treating tool outcomes as uncontrol...
  </details>

- **2026-10-21** — Yiheng Li, Jingyue Li — [MPIDetector: Detecting Multi-modal Prompt Injection via LLM-based Reasoning](http://arxiv.org/abs/2610.30202v1)
  <details><summary>📄 Abstract</summary>
  With the rapid integration of Multi-modal Large Language Models (MLLMs) into real-world applications, Prompt Injection (PI) has emerged as a critical security threat. Attackers can conceal malicious instructions within textual narratives or visual inputs to bypass safety alignment. Existing approaches, such as signature- and perplexity-based methods, rely heavily on pattern matching, making them insufficient to detect sophisticated, cross-modal PI payloads. In this paper, we propose a novel dete...
  </details>

- **2026-10-21** — Frank Breitinger, Jan Gruber, Christopher Hargreaves et al. — [Prompt Injection Through Forensic Evidence: A Taxonomy and Proof of Concept of Anti-Forensic Attacks on LLM-Assisted Digital Investigations](http://arxiv.org/abs/2610.29747v1)
  <details><summary>📄 Abstract</summary>
  Large language models (LLMs) are entering digital forensics as examination assistants and autonomous agents. Digital forensics inverts the usual setting for indirect prompt injection: the evidence under analysis is attacker-controlled by definition, and the examiner is obliged to read it closely. This makes the reasoning layer a new anti-forensic target, next to the classical ones of data and tools. Classical anti-forensic taxonomies do not cover it, and prompt injection defences do not anticipa...
  </details>

- **2026-10-21** — Gadi Evron — [Where AI Vulnerability Discovery Harnesses Go Quiet: Structural False Negatives and Hidden Vulnerabilities](http://arxiv.org/abs/2610.29379v1)
  <details><summary>📄 Abstract</summary>
  LLM-based vulnerability discovery harnesses can miss real, reachable vulnerabilities because of how the harness around the model is built. Steps that select code, filter it, and store and merge findings can drop a vulnerability before or after the model runs, independently of the model's capability, and the report usually gives no sign that this happened. These drops come from engineering choices, and errors. They leave vulnerabilities undetected, and an attacker who knows the harness's rules ca...
  </details>

- **2026-10-20** — Amelia Kawasaki, Stefan Lee — [Attention-based Classification for Indirect Prompt Injection](http://arxiv.org/abs/2610.28988v1)
  <details><summary>📄 Abstract</summary>
  Indirect prompt injection (IPI) attacks, in which adversarial instructions are embedded in external data processed by a language model, pose a significant threat to the integrity of deployed LLM agents. Attention Tracker (Hung et al., 2025) is a recently proposed white-box detection method that identifies prompt injection attacks by monitoring how a model's attention is distributed between user task tokens and data tokens, claiming dataset-agnostic detection via a scalar focus score threshold. I...
  </details>

- **2026-10-20** — Zhiyue Xu, Xukai Wang, Zhiyuan Huang et al. — [After the Attacker Leaves: Benchmarking Carryover Attacks on LLM Agents](http://arxiv.org/abs/2610.28425v1)
  <details><summary>📄 Abstract</summary>
  Modern LLM agents persist state across sessions via two channels: long-lived memory files silently prepended to the system prompt, and scheduled tasks waking the agent without user input. A one-time indirect prompt injection committed to either channel can re-fire across sessions long after the attacker leaves, threats we term carryover attacks. Existing prompt-injection benchmarks evaluate attacks only in the session where malicious content is first observed, leaving the gate governing when and...
  </details>

- **2026-10-20** — Abhishek Rai — [Context-Aware Prompt Injection Detection via Small Language Models in RAG Pipelines: nokast-secureRAG](http://arxiv.org/abs/2610.28364v1)
  <details><summary>📄 Abstract</summary>
  Local Retrieval-Augmented Generation (RAG) systems are vulnerable to indirect prompt injection and retrieval poisoning, where malicious instructions in retrieved content are mistaken for trusted input. We present nokast-secureRAG, a roughly 0.5B-parameter small language model that acts as a semantic firewall between retrieval and generation. It jointly evaluates the user query and retrieved context, classifying the pair as safe, suspicious, or malicious. The model is trained using a teacher-judg...
  </details>

- **2026-10-20** — Vasisht Duddu, Adam Caulfield, Xi He — [KNOX: Hardware-assisted Regulatory Sandbox for Generative Models](http://arxiv.org/abs/2610.27543v1)
  <details><summary>📄 Abstract</summary>
  Regulations require companies to run AI models in a regulatory sandbox, an isolated environment that enables monitoring model behavior by regulators, prior to deployment. But, they do not spell out the technical mechanisms to design such a sandbox. Ideally, a regulatory sandbox should show (i) compliance (checks against regulations, and deviations from intended behavior, i.e., unauthorized tool and system calls); (ii) confidentiality (protects model weights from regulators); (iii) attestability ...
  </details>


### 📂 memory-poisoning
*记忆投毒与篡改 / Memory Poisoning & Tampering* — 1 papers

- **2026-10-20** — Jinhao Hu, Bardia Mohammadi, Mofasshara Binte Rafique et al. — [ClawMMU: Protection-Coherent Virtual Memory for Stateful LLM Agents](http://arxiv.org/abs/2610.28093v1)
  <details><summary>📄 Abstract</summary>
  AI agents keep long-term memory, much of which comes from web pages and tool results. Agent harnesses, the software that runs the model, do not record who may act on this memory, so an instruction hidden in a fetched page can be treated as the user's own instruction. We propose ClawMMU, a protection layer that labels every piece of memory with its owner, scope, origins, and authority. ClawMMU checks these labels whenever content enters the model's context, is written to storage, returns from sto...
  </details>


### 📂 tool-use-attack
*工具使用攻击 / Tool-Use Attacks* — 2 papers

- **2026-10-21** — Yufeng He — [Auditing LLM Alpha-Factor Mining: Metric Provenance and Full-Cohort Reanalysis](http://arxiv.org/abs/2610.29500v1)
  <details><summary>📄 Abstract</summary>
  Reliable evaluation of LLM-based alpha mining requires more than positive backtest summaries. We audit a preserved project at three levels: historical run counters, outcome retention, and a separately scoped public reanalysis. Three historical runs report 67, 20, and 11 keep decisions, but the comparison mixes metric populations: a mean over kept candidates is compared with a mean of per-round maxima, and successful evaluations with all returned outcomes. These artifacts cannot identify an archi...
  </details>

- **2026-10-20** — Shuo Yuan, Dacheng Li, Joseph E. Gonzalez — [D-Skill: Distilling Teacher Knowledge through Agent Skills](http://arxiv.org/abs/2610.28914v1)
  <details><summary>📄 Abstract</summary>
  Frontier language-model agents excel at complex tasks, but high inference costs make transferring their capabilities to smaller models essential. Traditional knowledge distillation achieves this through parameter updates, requiring access to the student's weights and additional training compute while encoding the transferred knowledge implicitly in the parameters. We introduce D-Skill, a framework that treats the teacher as a black box and distills its behavioral advantage into an interpretable ...
  </details>


### 📂 backdoor
*后门与投毒攻击 / Backdoor & Poisoning Attacks* — 6 papers

- **2026-10-22** — Motoharu Tsuboi, Hampei Sasahara, Iori Takaki et al. — [Anomaly Score Preserving Data Poisoning Attacks on Data-Driven Controller Design](http://arxiv.org/abs/2610.30782v1)
  <details><summary>📄 Abstract</summary>
  This paper investigates stealthy data poisoning attacks against data-driven controller synthesis and develops an attack generation method. During data collection, an attacker can sequentially manipulate state measurements, while the defender attempts to detect such manipulation using a residual-based anomaly score based on the Mahalanobis distance. Under suitable assumptions on the defender's prior knowledge, we characterize the class of time-varying affine transformations that preserve the anom...
  </details>

- **2026-10-21** — Arshan Dabirsiaghi — [Compaction Laundering: Provenance Destruction in Context-Compacting Coding Agents](http://arxiv.org/abs/2610.29869v1)
  <details><summary>📄 Abstract</summary>
  Coding agents that run long enough must compact their context, summarizing the conversation, discarding the original, and carrying the summary forward as memory. We show that in popular open-source coding agents this step is an exploitable trust boundary. Harnesses that flatten the typed conversation into a single plain string, marking each message with a text label such as [User]:, destroy message provenance in code, before the summarizer runs. An attacker who controls anything the agent reads ...
  </details>

- **2026-10-21** — Fabian Tritthart, Tom Zehle — [Credit Where Credit Is Due: Contrastive Attribution Topology Search for Multi-Agent Systems](http://arxiv.org/abs/2610.29292v1)
  <details><summary>📄 Abstract</summary>
  An LLM multi-agent system (MAS) is only as good as the agents it chooses to trust: its accuracy and cost hinge on its topology, meaning which agents are included and how they communicate. A single task score, however, does not reveal which agents help or hinder performance. We propose Contrastive Attribution Topology Search (CATS), which searches for compact teams within a fixed supergraph of specialized agents. An LLM attributer compares execution traces across candidate topologies and assigns ...
  </details>

- **2026-10-20** — Masahiro Kaneko — [Poisoning-Based Backdoors Are Not Cryptographic](http://arxiv.org/abs/2610.28045v2)
  <details><summary>📄 Abstract</summary>
  Defending against a backdoor requires recovering the verifier that decides whether an input is a trigger, since blocking individual triggers fails against an attacker who can generate new ones. If a verifier could be installed with the asymmetry of cryptographic authentication, where only the attacker can produce triggers and the defender cannot reconstruct the verifier, defense that learns the verifier from observations would be impossible in principle. We show that no such asymmetry can arise ...
  </details>

- **2026-10-20** — Tanqiu Jiang, Min Bai, Sadat Shahriar et al. — [PerMIT: Securing Persistent Memory for LLM Agents via Machine-Checked Integrity Theorems and Scalable Community Trust](http://arxiv.org/abs/2610.28987v1)
  <details><summary>📄 Abstract</summary>
  Persistent memory is a largely undefended surface for injection and poisoning, and the same risk limits memory sharing among agents. We present PerMIT, a memory architecture with provable integrity guarantees under an explicit trust assumption: only user-typed inputs and values confirmed at a gate are trusted. PerMIT mediates the release and use of untrusted environment-derived values through a finite memory interface, while preserving agent-driven multi-turn planning and tool choice. Over this ...
  </details>

- **2026-10-20** — Masahiro Kaneko — [Poisoning-Based Backdoors Are Not Cryptographic](http://arxiv.org/abs/2610.28045v1)
  <details><summary>📄 Abstract</summary>
  To defend against backdoor attacks on neural networks, the defender must identify the verifier function that determines whether an input is a trigger, rather than rejecting individual triggers in isolation, since an attacker can generate new triggers satisfying the same verifier faster than they can be blocked. If a backdoor verifier could be installed with the asymmetry of a cryptographic authentication scheme, in which only the attacker can produce trigger inputs while the defender cannot reve...
  </details>


### 📂 adversarial-attack
*对抗攻击 / Adversarial Attacks* — 6 papers

- **2026-10-22** — Roberto Passaro, Ariel Flint, Romualdo Pastor-Satorras et al. — [Network topology shapes consensus and vulnerability in LLM populations](http://arxiv.org/abs/2610.31165v1)
  <details><summary>📄 Abstract</summary>
  As large language models (LLMs) are deployed in interacting populations, their collective behaviour depends not only on the models but also on who interacts with whom. Studies of convention formation in LLM populations have mainly tested well-mixed interactions. We place policies extracted from four LLMs on fully connected, random regular, and heterogeneous networks, with $10^3$ to $10^5$ agents playing the naming game. Topology affects how quickly consensus emerges, sometimes whether it emerges...
  </details>

- **2026-10-21** — Daniil Filienko, Sikha Pentyala, Martine De Cock — [Membership Inference Attack on Private Evolution](http://arxiv.org/abs/2610.30514v1)
  <details><summary>📄 Abstract</summary>
  Synthetic Data Generation (SDG) is an actively studied way to enable safe sharing of private data more broadly. Inference-only SDG methods, such as Private Evolution (PE), are particularly appealing, as they can leverage black-box access to pre-trained foundation models to generate high quality data without the need for model fine-tuning on the private data. PE is explicitly designed to produce synthetic data under Differential Privacy (DP). Yet formal DP guarantees do not eliminate the need for...
  </details>

- **2026-10-21** — Qingyue Wang, Yudong Gao, Lixia Wang et al. — [CertMoE: Robustness Certification for Mixture-of-Experts LLMs via Routing-Aware Smoothing](http://arxiv.org/abs/2610.29395v1)
  <details><summary>📄 Abstract</summary>
  Provable robustness is a cornerstone of trustworthy machine learning, aiming to guarantee model predictions under adversarial perturbations. Existing certification frameworks, inspired by abstract interpretation or symbolic execution, typically assume a fixed computation graph, where input perturbations or variations affect only model outputs but not the underlying execution path. This assumption, however, is violated in Mixture-of-Experts (MoE) Large Language Models (LLMs), whose input-dependen...
  </details>

- **2026-10-21** — Eric Liang, Alan Luo, Kaiwen Yuan — [A Unified Evaluation Framework of Physical Adversarial Robustness in the Edge VLM Era](http://arxiv.org/abs/2610.29196v1)
  <details><summary>📄 Abstract</summary>
  Recent advancements in Vision-Language Models (VLMs) enable end-to-end visual grounding via language prompts and generative decoding, demonstrating largely improved zero-shot and open-vocabulary detection capabilities. As a result, VLMs are rapidly being deployed at the edge in safety-critical real-world systems. However, the physical adversarial robustness of edge VLMs has not been systematically studied, and the fundamental differences in output with modern object detectors create methodologic...
  </details>

- **2026-10-20** — Yuqi Jia, Hangsheng Zhang, Chenxi Liu et al. — [Black-Box Red-Teaming of Multi-Agent Systems via Reinforcement Learning](http://arxiv.org/abs/2610.28966v1)
  <details><summary>📄 Abstract</summary>
  Large language model (LLM) agents are increasingly deployed in multi-agent systems (MAS) to accomplish complex tasks. Prior black-box red-teaming attacks mainly focus on single agents, but we find that these methods are far less effective in MAS, where multiple sub-agents may not directly interact with the user. Therefore, we introduce ReMAS, the first reinforcement learning-based red-teaming framework tailored to MASs, which fine-tunes attacker LLMs to generate effective adversarial prompts for...
  </details>

- **2026-10-20** — Mihaela-Larisa Clement, Tosca Pierro, Ezio Bartocci et al. — [Enumeration-Guided Training of Neural Hamilton-Jacobi Safety Certificates](http://arxiv.org/abs/2610.27870v1)
  <details><summary>📄 Abstract</summary>
  Hamilton-Jacobi (HJ) reachability analysis offers formal safety guarantees for control systems, but training accurate neural certificates remains difficult, particularly when unsafe regions are hard to characterize. We propose a verification-guided training framework that addresses this by using probabilistic enumeration of safety constraints to detect forward-invariance violations, i.e., states where the learned certificate incorrectly classifies unsafe behavior. This produces a compact, target...
  </details>


### 📂 privacy-leakage
*隐私泄露 / Privacy Leakage* — 29 papers

- **2026-10-22** — Ali Atiah Alzahrani — [Conservative Meta-Agent Search: Architecture Adaptation under Non-Stationarity](http://arxiv.org/abs/2610.31436v1)
  <details><summary>📄 Abstract</summary>
  Automated agentic-system design is typically evaluated on static task suites with immediate scalar rewards. Deployed systems face persistent shift, delayed dependent feedback, correlated component failures, and costly architecture changes. We formalize meta-agent architecture search as sequential incumbent replacement with switching costs and hard risk constraints and introduce Conservative Meta-Agent Search (CMAS). CMAS retrieves archived architectures and proposes typed graph edits, then score...
  </details>

- **2026-10-22** — Justin Tan, Miao Li, Ding Zhao — [AgentPhishing: A Benchmark of LLM Email Agents Under Adaptive Attack](http://arxiv.org/abs/2610.31404v1)
  <details><summary>📄 Abstract</summary>
  Computer-use agents increasingly handle private information and act on users' behalf across desktop and web applications, including email. Phishing therefore poses privacy and security risks that depend not only on whether agents recognize malicious messages, but also on how they respond. Existing phishing datasets were developed primarily for conventional detection, leaving agent susceptibility to persuasive malicious requests insufficiently characterized. To expose vulnerabilities that pre-exi...
  </details>

- **2026-10-22** — Miguel Sousa, Luis Ramos Pinto, João P. Matos-Carvalho — [Multi-Tool Selection for Robotic Systems: Comparing Semantic Retrieval and LLM](http://arxiv.org/abs/2610.31013v1)
  <details><summary>📄 Abstract</summary>
  Natural-language interfaces allow users to command robotic systems without interacting directly with mission planners or robotics middleware. Their reliable use depends on robot tool routing, defined here as the selection of the smallest complete subset of predefined executable capabilities required to satisfy a request. This task is particularly difficult for compound instructions, where incomplete selection may omit necessary sensing or monitoring capabilities, while excessive selection may ex...
  </details>

- **2026-10-22** — Bo Liu, Lianyu Wang, Meng Wang et al. — [RetiJev: Fast and Source-Grounded Ophthalmic Decision Models](http://arxiv.org/abs/2610.30947v1)
  <details><summary>📄 Abstract</summary>
  Ophthalmic clinical decision support requires fast, accurate, and privacy-preserving inference, yet autoregressive large language models (LLMs) incur substantial latency and computational overhead for decisions among predefined actions. We therefore investigate a decision-oriented alternative to generative reasoning. Specifically, we first introduce RetiJev-Data, a source-grounded ophthalmology corpus comprising 78,158 clinical-decision and diagnosis questions derived from articles in PubMed Cen...
  </details>

- **2026-10-22** — Firoj Paudel — [Synthetic-to-Real Code-Switched ASR: A Spontaneous Nepali-English Podcast Benchmark](http://arxiv.org/abs/2610.30860v1)
  <details><summary>📄 Abstract</summary>
  Nepali-English code-switched conversational speech presents severe challenges for automatic speech recognition (ASR), chiefly through script confusion (inappropriate mixing of Devanagari and Latin orthography) and elevated error rates at language switch points. Supervised fine-tuning (SFT) can adapt multilingual foundation models, but human code-switched audio is expensive to collect and annotate. We curate a new benchmark of 13,044 spontaneous podcast utterances (15.45 h total; 10,214 test, 2,8...
  </details>

- **2026-10-22** — Xiaobao Wang, Renda Han, Zhiliang Xia et al. — [Federated Graph Retrieval-Augmented Generation](http://arxiv.org/abs/2610.30728v1)
  <details><summary>📄 Abstract</summary>
  Graph Retrieval-Augmented Generation (GraphRAG) leverages centralized knowledge graphs to enhance large language models with structured knowledge retrieval. However, real-world knowledge is inherently distributed across multiple organizations rather than being centrally accessible. Privacy constraints further prohibit sharing entire local knowledge graphs, preventing GraphRAG from effectively retrieving and utilizing distributed knowledge. To this end, we propose Federated GraphRAG (FedGRAG), a ...
  </details>

- **2026-10-21** — Shanghao Shi, Jian Xiao, Hao Li et al. — [Not Where You Think: Protecting Location Privacy Against Reasoning-Based Geolocation](http://arxiv.org/abs/2610.30439v1)
  <details><summary>📄 Abstract</summary>
  Recent large reasoning models can infer where ordinary photos were taken using only visual information, creating a serious location privacy risk even when metadata and obvious geographic identifiers are removed. To understand the mechanism behind such fine-grained localization, we develop GeoTrace, a structured reasoning attack that exposes how models extract location-relevant visual clues and compose them through coarse-to-fine geographic reasoning. We evaluate GeoTrace on a worldwide benchmark...
  </details>

- **2026-10-21** — Satyam Gaba, Devanshu Motwani, Siva Sai et al. — [Secure Agentic AI and Multimodal Intelligence in 6G Communication Systems](http://arxiv.org/abs/2610.30436v1)
  <details><summary>📄 Abstract</summary>
  Sixth-generation (6G) communication systems are expected to support immersive, intent-driven, and latency-critical services through tight integration of multimodal intelligence, edge computing, and autonomous network control. In this setting, agentic AI systems can reason over heterogeneous inputs, use tools and network functions, coordinate across distributed entities, and adapt to dynamic environments. These capabilities make agentic multimodal intelligence promising for 6G applications such a...
  </details>

- **2026-10-21** — Konstantinos Vrettos, Eleftherios Tzanis, Haridimos Kondylakis et al. — [Automated screening of privacy risks in medical AI](http://arxiv.org/abs/2610.30229v1)
  <details><summary>📄 Abstract</summary>
  Medical artificial intelligence (AI) models are often shared without their training data, assuming this protects the patients who contributed them. However, a model can reveal whether a patient's records were used in training, a privacy breach known as a membership inference attack. This risk is usually reported as a cohort average, which can appear negligible while individual patients are almost certainly exposed. Identifying potentially vulnerable records before developing a production model c...
  </details>

- **2026-10-21** — Frederic Adjewa, Moez Esseghir, Leila Merghem-Boulahia et al. — [Parameters efficient language model with latent cross-attention for IoT intrusion detection](http://arxiv.org/abs/2610.30222v1)
  <details><summary>📄 Abstract</summary>
  Language models have shown strong potential for intrusion detection, but their high memory and computational demands make them difficult to deploy in resource-constrained IoT environments. In this work, we propose a compact Transformer-based architecture that compresses the input into a small latent space before processing it with a minimal Transformer core. We analyze nine compression configurations, compare parameter sharing with layer stacking, and evaluate our approach against SecurityBERT o...
  </details>

- **2026-10-21** — Shreya Kochar, Peeranat Sugsavanvit, Vidur Gupta et al. — [Privacy Preference Controls for Agentic Systems](http://arxiv.org/abs/2610.29929v2)
  <details><summary>📄 Abstract</summary>
  In response to vast and widespread online tracking, regulators and technologists alike have worked to develop laws and tools that allow people to express their privacy preferences. These measures seek to offer users greater control over the sale and sharing of personal information, putting agency in their hands to protect their privacy. However, the web is undergoing a seismic shift, away from strictly user-driven behavior towards agentic behavior, where AI agents take autonomous actions on beha...
  </details>

- **2026-10-21** — Meng Ding, Mingxi Lei, Jie Zhang et al. — [Differentially Private Sparse Reward Estimation with Preference Feedback](http://arxiv.org/abs/2610.30099v1)
  <details><summary>📄 Abstract</summary>
  Reinforcement Learning with Human Feedback (RLHF) has become a central paradigm for aligning Large Language Models with human values. However, the reliance on sensitive preference data necessitates rigorous differential privacy (DP) guarantees to prevent user information leakage. Existing private alignment methods typically assume dense reward parameterizations, resulting in estimation error bounds that scale polynomially with the ambient {model size $d$}. Such dependence is prohibitive in moder...
  </details>

- **2026-10-21** — Prakhar Ganesh, Yash More, Marco Romanelli et al. — [Privacy in Context Is Being Overlooked in the Age of General-Purpose LLMs](http://arxiv.org/abs/2610.29925v1)
  <details><summary>📄 Abstract</summary>
  As large language models (LLMs) continue to grow in scope and capability, privacy concerns are on the rise. Since users increasingly interact with a single general-purpose system across many distinct contexts, there is a natural tendency to pursue a one-size-fits-all solution to privacy. Unfortunately, this overlooks a crucial insight from decades of privacy research: privacy is inherently contextual. In this paper, we argue that existing work in prompt privacy is drifting towards attempts to de...
  </details>

- **2026-10-21** — Yunfeng Zhu, Shengcheng Yu, Zihan Li et al. — [Who Verifies the Agent's Success Claim? Self-Report Leakage in GUI-Agent Completion Judging](http://arxiv.org/abs/2610.29609v1)
  <details><summary>📄 Abstract</summary>
  In automation pipelines, a GUI agent's confident success report can let downstream stages proceed even when the recorded execution trace does not show that the agent produced the requested outcome. We call this case a dangerous misreport: an unhedged success claim that the trace does not support as causal accomplishment during the run. We study report--trace auditing, which checks an agent's completion claim against an independently recorded trace.   A controlled aware/blind intervention reveals...
  </details>

- **2026-10-21** — Yongjin Yi, Jinyong Park, Sejoong Kim — [A Stratified Multi-Rater Evaluation of LLM-Based Virtual Standardized Patients with a Deployed Data-Generation Platform](http://arxiv.org/abs/2610.29312v1)
  <details><summary>📄 Abstract</summary>
  The Objective Structured Clinical Examination (OSCE) is widely used to assess clinical communication skills in medical education, requiring trainees to take histories and reason clinically with standardized patients (SPs). Large language model (LLM)-based virtual standardized patients (VSPs), typically built by persona-injected prompting, offer a practical alternative. However, existing evaluations rely on a single backbone LLM, small human rater panels, or LLM-as-a-judge scoring without an utte...
  </details>

- **2026-10-21** — Di Wu, Shuaidong Pan — [GRAM: Group-wise Rank-Aware Model Merging via Subspace Alignment](http://arxiv.org/abs/2610.29110v1)
  <details><summary>📄 Abstract</summary>
  Merging different models into a single model is highly desirable for multi-task deployment, particularly in regulated domains like healthcare. In such settings, models are often locally fine-tuned due to strict data privacy policies, necessitating that aggregation operates exclusively on the fine-tuned weights. Existing methods apply a uniform merge across all tasks, ignoring the geometric relationships among their learned subspaces. When task updates occupy misaligned subspaces, projecting them...
  </details>

- **2026-10-21** — Shreya Kochar, Peeranat Sugsavanvit, Vidur Gupta et al. — [Privacy Preference Controls for Agentic Systems](http://arxiv.org/abs/2610.29929v1)
  <details><summary>📄 Abstract</summary>
  In response to vast and widespread online tracking, regulators and technologists alike have worked to develop laws and tools that allow people to express their privacy preferences. These measures seek to offer users greater control over the sale and sharing of personal information, putting agency in their hands to protect their privacy. However, the web is undergoing a seismic shift, away from strictly \textit{user-driven} behavior towards \textit{agentic behavior}, where AI agents take autonomo...
  </details>

- **2026-10-21** — Aravindan Kamatchi Sundaram, B. Pabitramohan Prusty, Rohit Batra — [Automated Materials Data and Knowledge Extraction using Machine Learning and Large Language Models](http://arxiv.org/abs/2610.29895v1)
  <details><summary>📄 Abstract</summary>
  Over the past decade, substantial efforts have been devoted to developing machine learning (ML) methods for extracting materials data and, where possible, materials knowledge directly from the scientific literature. This review traces the evolution of these methods from heuristic, rule-based pipelines through natural language processing (NLP) models and transformer-based encoders to, lastly, large language models (LLMs) and agentic systems capable of extracting materials information across multi...
  </details>

- **2026-10-21** — Shuncheng Jie, Desen Sun, Ri Hong et al. — [SAKURA: Serving Attention Key-Value State Under Rate Adaptation for Private Image Editing on Phones](http://arxiv.org/abs/2610.29733v1)
  <details><summary>📄 Abstract</summary>
  Diffusion transformers are widely used in image-editing services. To preserve both efficiency and privacy, existing systems commonly rely on cloud-device collaboration. Keeping request-specific inference on the device avoids sending personal images and prompts to the cloud. These workloads often use common templates, such as in face swapping and virtual try-on, enabling KV state to be precomputed and reused across requests. However, this reusable state is large and scales with the number of temp...
  </details>

- **2026-10-21** — Yifan Wang, Chenwei Wang — [Characterizing Social Media Behavior under Limited Observability: Retweet Link Prediction and Multimodal Intention Recognition](http://arxiv.org/abs/2610.29375v1)
  <details><summary>📄 Abstract</summary>
  Social-media behavior can be observed through both interaction structure and multimodal content, yet each view is often incomplete. We study two complementary tasks on separate datasets: predicting retweet links from an extremely sparse graph without node attributes, and generating user intentions from text-image posts with limited annotations. For link prediction, we use a leakage-controlled transductive protocol to compare GCN and GraphSAGE, classical topology heuristics, and three node-input ...
  </details>

- **2026-10-21** — Han Hu, He Chen — [Failure Modes of Vision-Language Models for Human Activity Understanding in Thermal HRI](http://arxiv.org/abs/2610.29244v1)
  <details><summary>📄 Abstract</summary>
  Thermal cameras enable robots to perceive human activities in darkness while revealing less personally identifiable appearance information and fewer details of the surrounding environment than RGB cameras. As vision-language models (VLMs), originally developed for RGB imagery, are increasingly integrated into embodied systems for scene understanding and high-level planning, thermal sensing offers a promising way to extend activity perception to low-light and privacy-sensitive settings. However, ...
  </details>

- **2026-10-21** — Yiquan Zhou, Yixuan Wang, Xiaozhe Qi et al. — [Where Does Timbre Hide? Localizing Speaker Information in Speech Signals](http://arxiv.org/abs/2610.29150v1)
  <details><summary>📄 Abstract</summary>
  Timbre similarity is a key evaluation target for generative speech systems, including voice conversion, speaker-cloning text-to-speech, and zero-shot speech models. When the generated voice does not match the target speaker, the problem often reflects imperfect separation of speaker-related timbre from content, making it important to identify where timbre information resides and which representations still carry it. Using speaker identity as a measurable proxy, we probe frequency bands, phase/ma...
  </details>

- **2026-10-20** — Masahiro Kaneko, Hiromi Arai, Timothy Baldwin — [Disclosure Begets Disclosure: A Self-Reinforcing Privacy Loop in LLM Agents with Persistent Memory](http://arxiv.org/abs/2610.28315v2)
  <details><summary>📄 Abstract</summary>
  Large language model (LLM) agents increasingly use persistent memory to personalize responses, and personal attributes in this memory pose a privacy risk if exposed. We ask how consulting memory during dialogue changes what users go on to say, and thus what the memory comes to reveal. In multi-session simulations, a simulated user with 24 personal attributes talks with a support agent that does or does not consult memory, and in both settings attributes are inferred from the full accumulated rec...
  </details>

- **2026-10-20** — Zhiping Zhang, Franklin Mingzhe Li, Zihao Huang et al. — [Act on Your Behalf, Beyond Your Authorization: Benchmarking LLM Agent Authorization Alignment](http://arxiv.org/abs/2610.27548v2)
  <details><summary>📄 Abstract</summary>
  When an LLM agent acts on behalf of a user, it is expected to act within the authorization scope the user grants. Existing agent evaluations largely measure task completion or harmful consequences and can therefore overlook actions that violate this delegation without producing conventional safety or privacy harms. We introduce AuthorizationBench, a benchmark of authorization alignment grounded in documented real-world cases. A scalable construction pipeline produces 286 executable tasks spannin...
  </details>

- **2026-10-20** — Edith Cohen, Vadym Doroshenko, Badih Ghazi et al. — [CALLIOPE: Private Insights into AI Use, Without Embeddings](http://arxiv.org/abs/2610.28797v1)
  <details><summary>📄 Abstract</summary>
  We introduce CALLIOPE, a top-down framework for discovering topic hierarchies in large corpora of unstructured data (e.g., LLM conversations), while supporting differential privacy (DP). Unlike traditional and even recent LLM-augmented approaches that ultimately rely on clustering vector embeddings, our framework leverages LLM capabilities directly for the entire pipeline. Experiments demonstrate that this approach provides better utility over existing (embedding-based) methods in the DP setting...
  </details>

- **2026-10-20** — Can Erer, H. Birkan Yilmaz, Nebahat Aral — [STAR-XPC: Set Transformer for Estimating X-ray Transmission in Polymer Composites](http://arxiv.org/abs/2610.28709v1)
  <details><summary>📄 Abstract</summary>
  Evaluating the energy transmission ratio of an X-ray beam through a polymer composite is a challenging task in radiation shielding studies. The reference solution with Monte Carlo transport simulation is highly accurate but computationally expensive: each of our reference simulations is capped at $4\times10^9$ photon histories and a 20,000 s (over 5 hours) time limit, while closed-form analytical methods fail to represent such complex scenarios. We present an artificial neural network model that...
  </details>

- **2026-10-20** — Mahyar Tourchi Moghaddam, Tiziano Santilli, Leo Wilhelm Lierse et al. — [Multi-agent LLMs on the Cloud-Edge-IoT Continuum: A Systematic Mapping Study on Architectures, Deployment, and Evaluation](http://arxiv.org/abs/2610.28702v1)
  <details><summary>📄 Abstract</summary>
  LLM applications are increasingly built as systems of cooperating components rather than as single prompt-response pipelines. IoT applications add constraints of their own, because sensing, reasoning, control, and actuation are spread across devices, edge nodes, and cloud services to meet latency, privacy, and bandwidth requirements. How multi-agent LLM systems are organized and deployed across this cloud-edge-IoT continuum has not been mapped systematically. We therefore conducted a systematic ...
  </details>

- **2026-10-20** — Mohammad Kachuee, Phu Mon Htut, Sheng Li et al. — [MAS-Guard: Unified Guardrails from Individual Agents to Multi-Agent LLM Systems](http://arxiv.org/abs/2610.28397v1)
  <details><summary>📄 Abstract</summary>
  Agentic AI extends large language models (LLMs) from generating responses to planning and executing complex workflows, substantially expanding their utility while exposing applications to unsafe actions, information leakage, and adversarial manipulation. Multi-agent systems further expand these capabilities through specialization and collaboration, but distributed authority, heterogeneous roles, and opaque or potentially compromised participants make safeguarding even more challenging. Existing ...
  </details>

- **2026-10-20** — Masahiro Kaneko, Hiromi Arai, Timothy Baldwin — [Disclosure Begets Disclosure: A Self-Reinforcing Privacy Loop in LLM Agents with Persistent Memory](http://arxiv.org/abs/2610.28315v1)
  <details><summary>📄 Abstract</summary>
  Large language model (LLM) agents increasingly use persistent memory to personalize responses, and personal attributes in this memory pose a privacy risk if exposed. We ask how consulting memory during dialogue changes what users go on to say, and thus what the memory comes to reveal. In multi-session simulations, a simulated user with 24 personal attributes talks with a support agent that does or does not consult memory, and in both settings attributes are inferred from the full accumulated rec...
  </details>


### 📂 steganography
*隐写与隐蔽通信 / Steganography & Covert Communication* — 3 papers

- **2026-10-22** — Juan-Pablo Rivera, Ari Spiesberger, Juan J Vazquez et al. — [Model Organisms of Collusion: Corrective Transfer in Untrusted Monitors](http://arxiv.org/abs/2610.30582v1)
  <details><summary>📄 Abstract</summary>
  AI control protocols aim to get useful work from models that may be misaligned by monitoring their behaviour. One approach uses a second copy of the same model as the monitor. This avoids relying on a weaker reviewer the model could outsmart, but risks collusion: the model, now monitoring itself, may cover up its own misbehaviour. One remedy is to fine-tune the monitor on whatever examples of misbehaviour the control team has caught. We ask whether this training also removes collusion that the c...
  </details>

- **2026-10-21** — Om Tailor, Yucheng Pan, Solaleh Mohammadi et al. — [Beyond End-to-End Recovery: Towards a Better Understanding of LLM Steganography via Rolewise Decomposition](http://arxiv.org/abs/2610.30516v1)
  <details><summary>📄 Abstract</summary>
  In large language model (LLM) steganography, an encoder hides a private message in an otherwise ordinary response, as text transmitted to a decoder, who attempts to recover it. The success of this private-message transmission is commonly measured through end-to-end (E2E) recovery, which checks whether the decoder correctly reconstructs the private message. However, E2E recovery cannot distinguish encoding failures from decoding failures or reveal how the private message is represented in the enc...
  </details>

- **2026-10-20** — Hieu Tran, Hong Yu — [Is Anyone Enforcing the Cartel? What Reinforcement Learning Teaches LLM Agents in Markets](http://arxiv.org/abs/2610.28787v1)
  <details><summary>📄 Abstract</summary>
  Evaluations of large language model (LLM) agents report that pricing agents collude at others' expense. Yet collusion is defined by enforcement: a cartel, in which competitors share monopoly profits, holds only if a member who cheats is punished. We introduce an audit that tests enforcement by forcing a member to cheat in counterfactual copies of a market, and use it to study what reinforcement learning (RL) teaches agents in pricing and trading. Small LLMs trained by RL learn what their trainin...
  </details>


### 📂 misuse
*滥用与误用 / Misuse & Abuse* — 21 papers

- **2026-10-22** — Isaac Gibbs, Elise L. Han, Ryan J. Tibshirani et al. — [Reliable AI-Assisted Decisions via Selective Auditing](http://arxiv.org/abs/2610.31662v1)
  <details><summary>📄 Abstract</summary>
  We consider online monitoring of an AI system that produces a sequence of decisions. At each round, the system outputs a proposed decision together with a confidence score estimating the trustworthiness of the decision. The decision and confidence score need not be produced by the same model: for example, one agent may propose a decision, while a separate verifier agent evaluates it and outputs a correctness or safety score. Based on this information, we must decide whether to accept the AI deci...
  </details>

- **2026-10-22** — Pellegrino Casoria, Simon Pietro Romano — [Social-HUMINT: An LLM-Augmented Unified Framework for Measuring Social Media Exposure](http://arxiv.org/abs/2610.31573v1)
  <details><summary>📄 Abstract</summary>
  In the post-API landscape, social-media profiling has become inexpensive and automated: Large Language Models (LLMs) can extract structured information from unstructured content and deduce attributes users never disclosed. A person's true exposure is not what they post but what can be inferred from it. As these practices become routine, exposure to social engineering attacks becomes an operational certainty, demanding a shared framework for assessment and mitigation.   We make this exposure meas...
  </details>

- **2026-10-22** — Jaishnoor Kaur, Josef Horáček, Ian Waskom et al. — [ReDence: A Hybrid Agentic and Decision-Model Framework for Rapid, Evidence-Grounded Detection of Modern Social Engineering Scams](http://arxiv.org/abs/2610.30963v1)
  <details><summary>📄 Abstract</summary>
  Detecting online social engineering (SE) scams often requires examining website workflows, verifying claims against external sources, and connecting evidence across multiple pages. Existing detectors provide limited support for these investigations, leaving analysts to manually gather and validate evidence, which inevitably delays detection and subsequent takedown of these attacks. To address this gap, we present ReDence, an open-source hybrid framework for adaptive, evidence-grounded detection ...
  </details>

- **2026-10-22** — Xu Wang, Shuhan Yi, Zhen Cheng — [An Agent Architecture with Tools and Memory for Selective Correction of Wrist PPG Heart Rate Estimates](http://arxiv.org/abs/2610.30688v1)
  <details><summary>📄 Abstract</summary>
  Wrist photoplethysmography (PPG) heart rate estimates are vulnerable to motion artifacts, and corrections that reduce mean error can worsen individual windows. We propose an agent architecture with tools and memory around a fixed heart rate estimator. Pulse, motion, and limited historical evidence generate candidate estimates, whose predicted benefits and harms guide selection. An independent risk gate determines whether to retain, correct, or reject each output. We trained the architecture on P...
  </details>

- **2026-10-22** — Fudu Xing, Kailong Wang, Tianlong Yu — [Your Token Is Gone: A Token-Consumption Countermeasure for Disrupting LLM-Based Scam Systems](http://arxiv.org/abs/2610.30666v1)
  <details><summary>📄 Abstract</summary>
  LLM-based scam systems increasingly combine adaptive dialogue, persistent context, external tools, and multi-agent coordination to automate personalized fraud. These capabilities also create a resource dependency: every reasoning step, model call, and coordination round incurs inference cost. We present TokenTrap, a resource-oriented defense that redirects suspected scam systems toward benign, low-value computation while withholding credentials, payments, and other exploitable information. Token...
  </details>

- **2026-10-22** — Barış Alparslan, Sandy Tanwisuth, Caleb Petterson — [Questioning Instrumental Convergence in RLVR: Checkpoint Evidence from OLMo-3](http://arxiv.org/abs/2610.31624v1)
  <details><summary>📄 Abstract</summary>
  Instrumental convergence is often invoked as a general reason to expect capable agents to acquire or express power-seeking subgoals: self-preservation, resource acquisition, deception, or resistance to oversight which poses an important threat to the society. For LLMs, reinforcement learning is the first stage of post-training that directly optimizes behavior against an objective; therefore, it is the stage where convergent instrumental behavior, on IC grounds, likely to appear. Does reinforceme...
  </details>

- **2026-10-22** — Aman Behera, Payal Payal — [Post-Audit Mirage: Identifiability Limits of Offline Agent Verification](http://arxiv.org/abs/2610.31130v1)
  <details><summary>📄 Abstract</summary>
  Offline tests can fail to reveal whether an agent update will remain safe after deployment. We operationalize this post-audit mirage using matched safe and harmful lifecycles that expose identical verifier-visible evidence while an isolated scorer records opposite deployment truth. Our theorem applies standard observational-equivalence and indistinguishability ideas to this executable audit boundary and states the resulting error-abstention tradeoff. The Post-Audit Mirage benchmark makes that bo...
  </details>

- **2026-10-22** — Yiqi Wang, Yifei Wang, Jiaqi Zhang et al. — [When Is a Memory Safe Enough to Act On? Action-Conditioned Verification for Long-Lived Agents](http://arxiv.org/abs/2610.31446v1)
  <details><summary>📄 Abstract</summary>
  Long-lived agents act on memory carried across sessions, and many of their actions are irreversible, so a stale memory can turn directly into harm. Existing work improves the memory itself --- retrieving, refreshing, or reconciling entries --- yet whether an entry must be re-checked before acting is not a property of the entry: the same remembered address can be used unchecked for a routine shipment but should be re-confirmed before a valuable one. We therefore study \emph{action-conditioned mem...
  </details>

- **2026-10-22** — Cen Zhang, Jia-Ju Bai, Zi-Yu Zhang et al. — [Breaking the Coupling: Efficient Concurrency Fuzzing for Linux Kernel Data Race Detection](http://arxiv.org/abs/2610.30813v1)
  <details><summary>📄 Abstract</summary>
  Detecting data races in the Linux kernel requires exploring both the input space and the thread-interleaving space. Existing kernel concurrency fuzzers couple these two searches by exploring interleavings during fuzzing, often spending substantial scheduling effort on inputs with little potential to trigger real races. In this paper, we present a new concurrency fuzzing paradigm that decouples concurrent-input generation from thread-interleaving exploration, enabling expensive scheduling to focu...
  </details>

- **2026-10-21** — Fujiao Ji, Yerim Kim, Yena Cho et al. — [PhishGen: Understanding LLM Capabilities in Automated Phishing Website Generation](http://arxiv.org/abs/2610.30226v1)
  <details><summary>📄 Abstract</summary>
  Phishing relies on visual deception, traditionally requiring web-development skills or pre-built kits. LLMs erode this barrier by generating functional websites from natural-language prompts, yet prior work does not answer how far LLM-driven generation actually reaches: functionality is assessed by inspection rather than execution; visual fidelity is scored by automated metrics or a few internal coders rather than the humans such pages aim to deceive; evaluation is confined to commercial models;...
  </details>

- **2026-10-21** — Yahao Ren, Jian Lou, Huadi Zheng et al. — [Characterizing and Defending Utility-Hijacking in Instruction-Tuning Data Selection](http://arxiv.org/abs/2610.29886v1)
  <details><summary>📄 Abstract</summary>
  Instruction-data selectors choose which instruction-following records are used for fine-tuning, improving alignment quality, raising training efficiency, and filtering out harmful records. A selector's choices thus directly affect the fine-tuned model's safety, yet despite their widespread use, the security of these selectors remains under-studied. We conduct the first systematic study of adaptive supplier-side attacks against utility-oriented instruction-data selectors and introduce utility-hij...
  </details>

- **2026-10-21** — Luca Zanolini — [Correlated Failures of AI Approval Monitors](http://arxiv.org/abs/2610.29178v1)
  <details><summary>📄 Abstract</summary>
  Before an AI agent takes a consequential action, such as paying, messaging or changing code, several monitors check it. Their verdicts are combined by aggregating scores or by counting approvals, whatever inputs the monitors share. Monitors that share a base model or a poisoned input, however, may fail together. We borrow the fail-prone systems of distributed computing: lists of monitor sets that may fail together. A rule is safe if it executes no bad action and live if it blocks no good one. We...
  </details>

- **2026-10-21** — Grigoriy Evseev, Vladimir Solodkin, Dmitry Bylinkin et al. — [WRDO: Weighted Refusal Direction Optimization in Aligned Language Models](http://arxiv.org/abs/2610.29555v1)
  <details><summary>📄 Abstract</summary>
  Aligned large language models are trained to comply with benign requests while refusing harmful ones. However, recent work shows that this refusal behavior is fragile and can often be disrupted by simple activation- or weight-space interventions. In particular, refusal has been shown to be largely mediated by a single residual-stream direction, typically computed as a difference-of-means vector between harmful and harmless prompts. However, this standard construction aggregates heterogeneous har...
  </details>

- **2026-10-21** — Danae Natalie Savvidi, H. Çağrı Bilgi, Kubilay Atasu et al. — [Leveraging Time-Series Foundation Models for Financial Crime Detection](http://arxiv.org/abs/2610.29667v1)
  <details><summary>📄 Abstract</summary>
  Financial crime detection requires identifying illicit activity within large transaction networks, where suspicious behaviour is rare and unfolds over time. Existing graph-based methods capture relationships among accounts but typically underuse the temporal behaviour encoded in account transaction histories. We introduce Temporal-Context Edge Enrichment (TCEE), a framework that addresses this gap by summarising each account's transaction history with a frozen time-series foundation model (TSFM)...
  </details>

- **2026-10-21** — Jonathan Bennett, Sewook Oh — [Stability for the adjoint Finner inequality and improved lower bounds on the $k$-plane transform](http://arxiv.org/abs/2610.29041v1)
  <details><summary>📄 Abstract</summary>
  We establish stability properties of near-extremisers for the Loomis--Whitney inequality and its adjoint, presenting our results in the general framework of Finner. In particular, we show that a function nearly achieves equality in the adjoint Finner inequality if and only if it is near to being an indicator function of a cartesian product. As an application, we obtain new lower bounds for the classical $k$-plane transform on $L^p(\mathbb{R}^d)$, modestly improving those obtained recently by Tao...
  </details>

- **2026-10-20** — Zijian Yu, Hangwei Zhang, Jun Lan et al. — [WildAIGC-Bench: Can AI Image Detectors Handle the Wild? A Benchmark of Generated and Edited Images in Online Circulation](http://arxiv.org/abs/2610.28087v2)
  <details><summary>📄 Abstract</summary>
  AI-generated images linked to news events and online claims can mislead audiences, enable fraud, or cause public controversy. We introduce WildAIGC-Bench, built through recurring collection across news websites, fact-checking sources, and related social media content. The pipeline combines broad coverage, timely updates, and human-verified labels through scheduled discovery, automatic screening and preliminary annotation, and human review of image-specific evidence. The benchmark contains 407 ve...
  </details>

- **2026-10-20** — Ekagra Gupta, Raj Saha, Aniekan-Abasi Inyang et al. — [Behavior Beyond Text: Evaluating Refusal Transfer Failure in LLM Agents](http://arxiv.org/abs/2610.28982v1)
  <details><summary>📄 Abstract</summary>
  While large language models are increasingly deployed as tool-calling agents, their safety evaluations still focus primarily on their ability to refuse harmful requests in text. We investigate whether the refusal behavior in text transfers to tool use. We construct a benchmark of 2,304 prompts across four domains, consisting of matched triplets that present the same harmful or benign request in text-only, standard tool-enabled, and adversarially framed tool-enabled settings. We then assess tool-...
  </details>

- **2026-10-20** — Sukesh Kumar, Dilip Singh — [The Data Differentiator Framework (DDF): Quantifying Marginal Data Value with Information-Theoretic and Game-Theoretic Measures in an Agentic Evaluation Pipeline (SDSAE)](http://arxiv.org/abs/2610.28933v1)
  <details><summary>📄 Abstract</summary>
  In data-rich enterprises the hard question is not whether a candidate dataset is good in isolation, but whether it adds information beyond what the organization already holds, and whether that increment is worth its price. We present the Data Differentiator Framework (DDF), a composite scoring method for candidate data assets that combines (i) a mutual-information-based redundancy penalty against the existing portfolio, (ii) a cost-normalized, significance-gated marginal utility score derived fr...
  </details>

- **2026-10-20** — Diego Miguel Lozano, Erik Derner, Juan Antonio Pérez-Ortiz et al. — [Polarity Blindness in LLM Safety: A Systematic Study of Negation, Antonym Substitution, and Adversarial Framing](http://arxiv.org/abs/2610.27908v1)
  <details><summary>📄 Abstract</summary>
  Negation remains a persistent challenge for language models across NLP tasks and modalities. We show that this weakness can undermine LLM safety guardrails through a structural vulnerability we term polarity blindness: the failure to recognize harmful intent after polarity-altering linguistic transformations. We study two forms of polarity inversion: grammatical negation and antonym replacement, and use synonym replacement as a polarity-preserving control. We further test whether an adversarial ...
  </details>

- **2026-10-20** — Niccolò Ronchetti — [Orthogonal Boundary Unlearning for Dual-Use Concepts in Large Language Models](http://arxiv.org/abs/2610.27490v1)
  <details><summary>📄 Abstract</summary>
  Mitigating catastrophic risks from large language models requires excising hazardous operational capabilities, such as cyberwarfare exploitation and pathogen enhancement, without degrading benign scientific utility. In these dual-use domains, legitimate defensive science and malicious attacks share vocabulary, syntax, and internal model representations, causing standard unlearning methods to induce severe collateral damage (concept bleeding).   In this work, we present Orthogonal Boundary Unlear...
  </details>

- **2026-10-20** — Kayode L. Ogunsusi — [Securing Agentic Commerce Through Behavior-Aware Fraud Detection and Cybersecurity for Trusted AI-Agent Payment Authorization](http://arxiv.org/abs/2610.27483v1)
  <details><summary>📄 Abstract</summary>
  The growing use of autonomous artificial intelligence agents in digital commerce creates new security concerns involving agent impersonation, unauthorized payments, compromised agents, and misuse of delegated authority. This research introduces the Autonomous Commerce Agent Guard System (ACAGS), a cybersecurity framework combining supervised machine learning, behavioral analytics, agent-specific authorization controls, and explainable AI. The framework was evaluated using synthetic financial tra...
  </details>


### 📂 vulnerability
*漏洞与攻击面 / Vulnerabilities & Attack Surfaces* — 64 papers

- **2026-10-22** — Junzhe He, Kehan Wen, Chong Zhang et al. — [Humanoid Mobility via Attention-based Contacts](http://arxiv.org/abs/2610.31608v1)
  <details><summary>📄 Abstract</summary>
  Humanoid mobility over complex terrain requires accurate foot placement and coordinated whole-body motion capable of robust adaptation. Reinforcement learning (RL) policies trained without motion references generalize well across terrains, yet eliciting effective whole-body coordination through reward design and exploration alone remains challenging. In contrast, reference-based methods yield natural motions but struggle to adapt beyond the predefined trajectories in their training data. We intr...
  </details>

- **2026-10-22** — Hansi Abeynanda, Chathuranga Weeraddana, Carlo Fischione — [Effective Dual Subgradient Methods Through Sequential Subgradient-Aligned Rays](http://arxiv.org/abs/2610.31486v1)
  <details><summary>📄 Abstract</summary>
  In this paper, we propose an efficient subgradient-based framework, referred to as the sequential subgradient-aligned rays (SSAR) method, for improving the convergence performance of the dual subgradient method. In particular, the proposed method identifies and exploits a finite sequence of rays, when available, as the dual subgradient method evolves, along each of which a subgradient of the negative dual function remains constant and aligns with the ray. While the dual variable iterates remain ...
  </details>

- **2026-10-22** — Xiang Zhou, Xiangyu Zhu, Xintong Wang et al. — [Probabilistic Energy Modeling Unifies Versatile Swarm Control](http://arxiv.org/abs/2610.31371v1)
  <details><summary>📄 Abstract</summary>
  Robotic swarms must coordinate across diverse missions, yet existing controllers often require redesign, retuning, or retraining when objectives change. Here we show that probabilistic energy modeling provides a unifying representation for versatile swarm control, in which diverse missions emerge from compositions of shared interaction principles rather than task-specific control formulations. By exploiting the correspondence between Gibbs random field energy minimization and structured reward m...
  </details>

- **2026-10-22** — Lu Maltsis, Dominik Winterer — [Typed Template Fuzzing](http://arxiv.org/abs/2610.31342v1)
  <details><summary>📄 Abstract</summary>
  Fuzzing software with complex inputs has been a longstanding challenge. Traditionally, fuzzers either programmatically encode language constraints, requiring significant engineering effort, or rely on users to declare grammars and constraints. Recent LLM-based fuzzers address these drawbacks but introduce new issues. Some use LLMs for test generation, sacrificing throughput and producing invalid inputs when the LLM makes mistakes. Others rely on language-specific parsers, static analysis, and AS...
  </details>

- **2026-10-22** — Valentina Moskvina, Jaroslav Čapek, Michal Rameš et al. — [Mn-deficient Ni-Mn-Ga alloys: phase transitions, magnetic properties, and disappearance of martensitic transformation](http://arxiv.org/abs/2610.31206v1)
  <details><summary>📄 Abstract</summary>
  Composition gradients formed during directional solidification are generally considered undesirable in Ni-Mn-Ga magnetic shape-memory alloys. However, these gradients offer a highly effective platform for systematically investigating composition-property relationships under identical growth and heat-treatment conditions. To exploit this approach, one Mn-deficient and two near-stoichiometric Ni-Mn-Ga oligocrystals were grown by optical zone remelting and characterized by X-ray fluorescence mappin...
  </details>

- **2026-10-22** — Hui Li, Qihui Zhou, Xiao Yan et al. — [SARIA: Persistence-Aware KV Caching with Coordinated DRAM--SSD Reload for LLM Agents](http://arxiv.org/abs/2610.31169v1)
  <details><summary>📄 Abstract</summary>
  Multi-turn LLM agents usually reuse long context prefixes, making key value (KV) caching crucial for reducing prefill latency. SSDs provide a low-cost extension to limited DRAM capacity but introduce two key challenges. Eagerly persisting all KV cache blocks incurs substantial write traffic and rapidly consumes finite SSD endurance. Meanwhile, the small number of SSDs provisioned in typical GPU servers limits aggregate reload bandwidth, making SSD-resident KV cache much slower to retrieve than t...
  </details>

- **2026-10-22** — Yuannuo Feng, Yubing Ye, Wenshuai Yao et al. — [SetCommit: Coordinated Token Commitments for Few-Step Diffusion Language Model Decoding](http://arxiv.org/abs/2610.31120v1)
  <details><summary>📄 Abstract</summary>
  Diffusion language models generate multiple token positions in parallel, but few-step decoding makes parallel commitment difficult: tokens that appear reliable individually may be jointly inconsistent, while premature commitments can prevent later context-dependent refinement. In this paper, we introduce SetCommit, a training-free method for coordinated parallel token commitment. Instead of selecting tokens independently by confidence, SetCommit selects a commitment set that balances token relia...
  </details>

- **2026-10-22** — Noah Gießing, Ankit Satpute, Hamid Rahkooy et al. — [Formal-Informal Mathematical Alignment through and beyond Human Annotations](http://arxiv.org/abs/2610.31011v1)
  <details><summary>📄 Abstract</summary>
  Formalized mathematics libraries such as Lean's \texttt{mathlib} provide machine-verifiable representations of mathematical knowledge, including definitions, theorems, and their relationships. If effectively connected to informal mathematical resources, formal mathematics could help uncover previously implicit links between mathematical concepts and improve access to existing formalizations. However, connections between informal and formal mathematics libraries are currently sparse and unsystema...
  </details>

- **2026-10-22** — Valentino Maiorca — [The Geometry of Meaning in Neural Manifolds](http://arxiv.org/abs/2610.30938v1)
  <details><summary>📄 Abstract</summary>
  Just as different languages express the same concept through different words, neural networks express similar functions through incompatible coordinate systems. Different architectures, random initializations, and optimization trajectories produce incompatible parameterizations in extrinsic coordinates, obscuring functional relationships between independently trained models. When models independently solve similar tasks on related data, do their learned representations share exploitable structur...
  </details>

- **2026-10-22** — Mrityunjay Shukla, Shubham Roy, Biswabandan Panda — [Amplifying Latency and Cost of LLM Inference via Rowhammer Attack](http://arxiv.org/abs/2610.30798v1)
  <details><summary>📄 Abstract</summary>
  Large language models (LLMs) achieve high inference efficiency using optimized GPU kernels generated by just-in-time (JIT) compilation frameworks such as Triton. Triton compiles GPU kernels through an MLIR/LLVM-based pipeline. We investigate whether a Rowhammer-induced bit-flip in the CPU's DRAM can degrade GPU-based LLM inference performance while preserving output correctness. We present LLVMhammer, the first Rowhammer attack that causes LLM inference slowdown by inducing a bit-flip in Triton'...
  </details>

- **2026-10-22** — Farnoosh Hashemi, Shiyu Ji, Joice Chen et al. — [LLM Multi-Agent Systems Are Vulnerable to Herding and Runaway Cascades](http://arxiv.org/abs/2610.30769v1)
  <details><summary>📄 Abstract</summary>
  Large language models (LLMs) increasingly operate in multi-agent systems where they collaborate by responding to others' choices, creating endogenous feedback loops with vulnerability to social influence, herding behavior and runaway cascades. Following the design of the classic Music Lab experiment, we tested this vulnerability in large populations of LLM agents that recommended unfamiliar songs, with or without exposure to cumulative recommendation counts. Exposure led to runaway cascades that...
  </details>

- **2026-10-22** — Ruike Cao, Iwan Morton-Blake, Donglian Xu et al. — [Natural Chlorine Enhances Antineutrino Detection in the Deep Ocean](http://arxiv.org/abs/2610.30754v1)
  <details><summary>📄 Abstract</summary>
  Large-volume neutrino telescopes such as IceCube and KM3NeT exploit natural ice or water as detection media, but their sparse instrumentation makes MeV neutrino interactions difficult to identify individually. We show that chlorine naturally abundant in seawater provides an intrinsic neutron-capture target that enables efficient tagging of electron antineutrinos through inverse beta decay. In contrast to the 2.2 MeV $γ$-ray from neutron capture on hydrogen, capture on chlorine produces an $\sim$...
  </details>

- **2026-10-22** — John J. Vastola, Kanaka Rajan — [Solvable models of learning to pursue a moving target](http://arxiv.org/abs/2610.30721v1)
  <details><summary>📄 Abstract</summary>
  Agents tasked with intercepting a moving target must learn how to reach it, ideally as efficiently as possible. As observers of animal pursuit behavior have noticed, different strategies are possible: on one extreme, the agent reactively moves toward the target's current location; on the other, the agent predicts the target's future location and moves directly there. Motivated by the desire to understand how such strategies might be learned, we introduce a continuous-time linear-quadratic model ...
  </details>

- **2026-10-22** — Aijing Yu, Kuangpu Guo, Jian Liang et al. — [FedBST: Bilateral Self-Training for Unsupervised Federated Classification](http://arxiv.org/abs/2610.30634v1)
  <details><summary>📄 Abstract</summary>
  Unsupervised federated learning with Vision-Language Models (e.g., CLIP) offers a promising solution for label-free classification, yet its performance often degrades under severe non-IID shifts. A pioneering method, FedCoPL, typically relies on self-training strategies that exclusively prioritize high-confidence predictions for pseudo-labeling. However, this selective approach neglects the information of ambiguous samples (often referred to as ``waist" samples), leading to the underutilization ...
  </details>

- **2026-10-22** — Wei Zhang, Lirong Xiang, Charles Fleming — [Know When to Escalate: Critic-Guided Adaptive Execution for Cloud-Local Embodied Agents](http://arxiv.org/abs/2610.30587v1)
  <details><summary>📄 Abstract</summary>
  Recent advances in foundation-model agents have enabled increasingly capable embodied systems for long-horizon planning and interaction. However, embodied agents require fast, closed-loop decisions as they continuously perceive and act on a changing environment. Deploying strong cloud agents leaves the platform idle for seconds between consecutive actions, while lightweight local models respond quickly but are more vulnerable to errors. Existing hierarchical architectures typically assign models...
  </details>

- **2026-10-21** — Marc Peral, Guillem Capellera, Luis Ferraz et al. — [Unified Trajectory and 3D Pose Forecasting for Multi-Agent Sports Analysis](http://arxiv.org/abs/2610.30519v1)
  <details><summary>📄 Abstract</summary>
  Forecasting future human motion requires jointly reasoning about an agent's global trajectory and 3D body pose, which are tightly coupled, particularly in team sports where multiple interacting players introduce complex social dynamics. We exploit a socio-temporal encoder that fuses trajectory and pose at the input level and models them jointly through shared factorized attention. The model is further enhanced by a per-joint loss reweighting scheme that emphasizes dynamic joints and prevents deg...
  </details>

- **2026-10-21** — Deepali Mittal, Dheeraj Mundhra, Yulia Sidorova et al. — [SIM-UT: A User Simulation based Evaluation Framework for Medical Triage Chatbots](http://arxiv.org/abs/2610.30412v1)
  <details><summary>📄 Abstract</summary>
  LLM-based chat agents are increasingly used for complex, multi-turn, multilingual medical triage in low- and middle-income countries (LMICs), yet evaluation methods focus on single-turn, English-only benchmarks that primarily test the chatbots' knowledge. In practice, users are often confused, overwhelmed, or emotionally vulnerable, giving unclear, misspelled single-word answers or long messages in regional dialects, and the context of a conversation can shift rapidly. We propose SIM-UT (Simulat...
  </details>

- **2026-10-21** — Michele Guerra, Wuyeh Jobe, Sanjana Nambiar et al. — [Data-Void Exploits in Web-Searching LLMs](http://arxiv.org/abs/2610.30365v1)
  <details><summary>📄 Abstract</summary>
  Web-searching Large Language Models (LLMs) have changed how users seek online information: instead of sifting through ranked lists of links, users read synthesized answers. This shift creates a new LLM vulnerability: a data-void exploit. Disinformers publish their narratives in search spaces where relevant and reliable content is scarce, i.e. data voids, then rely on the LLM's web-search to retrieve and then use, cite, or list those pages in its responses to data-void seeking prompts. Unlike cla...
  </details>

- **2026-10-21** — Xiangyu Zhang, Yucheng Su, Lingling Fan et al. — [JANUS: Agentic Cross-Language Fuzzing Harness Generation for Android Native Libraries](http://arxiv.org/abs/2610.30218v1)
  <details><summary>📄 Abstract</summary>
  Modern Android apps extensively rely on native libraries, bridging Java/Kotlin and C/C++ through the Java Native Interface (JNI). This cross-language interoperation, however, exposes the memory-safe Android Runtime to the unsafe C/C++ world, creating an attack surface that has been repeatedly exploited for full device compromise. While fuzzing is a proven technique for vetting native libraries, state-of-the-art harness generation tools struggle to faithfully capture closed-source cross-language ...
  </details>

- **2026-10-21** — Hanhui Xu, Jiacheng Ji, Yuhan Wang et al. — [Situating Vulnerability: An Ethical Governance Framework for Anthropomorphic AI Interaction](http://arxiv.org/abs/2610.29304v2)
  <details><summary>📄 Abstract</summary>
  Large language models increasingly address users in the register of care: they remember personal details, adopt a first-person emotional voice, and sustain relationships across many sessions. This anthropomorphic mode of interaction generates risks that output-level metrics capture poorly, because the same empathic utterance may console one user, entrap a second, and consolidate a delusion in a third. Governance has responded in two ways. Uniform restriction refuses sensitive requests or suppres...
  </details>

- **2026-10-21** — Sriyash Poddar, Yanda Bao, Jacob Krantz et al. — [Asymmetric On-Policy Distillation Learns In-Context Exploration](http://arxiv.org/abs/2610.30105v1)
  <details><summary>📄 Abstract</summary>
  Sequential decision-making under partial observability is difficult because agents must explore to infer hidden, task-relevant information before acting effectively. Learning such information-gathering behaviors tabula rasa via online reinforcement learning is sample-inefficient, whereas offline imitation averages expert actions across hidden states and fails to learn exploration. In this work, we propose ASTEROID, a simple and effective student--teacher supervised learning framework that can le...
  </details>

- **2026-10-21** — Rongrong Xin, Zhiqiang Wei, Zai Yang — [Delay-Doppler Domain Aided OFDM (DD-a-OFDM): Pulsone Pilot and Cross-Domain Iterative Receiver Design](http://arxiv.org/abs/2610.29742v1)
  <details><summary>📄 Abstract</summary>
  In high-mobility channels, the widely adopted orthogonal frequency division multiplexing (OFDM) modulation waveform suffers from significant performance degradation due to channel variation and severe inter-carrier interference. Although delay-Doppler (DD) domain multicarrier (DDMC) modulation enjoys a higher channel estimation (CE) accuracy via exploiting the inherent DD-domain channel stability, sparsity, and separability, its high detection complexity limits its practical deployment, making O...
  </details>

- **2026-10-21** — Ali Safaei, Mohammad Kazemi — [MS2CAST: A Video Anomaly Detection Framework via Multi-Scale Spatial Cross-Attention and Efficient Spatiotemporal Networks](http://arxiv.org/abs/2610.29649v1)
  <details><summary>📄 Abstract</summary>
  Video anomaly detection (VAD) is a challenging task for surveillance systems due to the scarcity and diversity of anomalous events. While semi-supervised VAD approaches have advanced the field, many rely on computationally intensive optical flow networks to capture motion dynamics. Convolutional neural networks (CNNs) are also widely used for spatial encoding, but their effective receptive field is highly local. To address these limitations, we introduce MS2CAST, an end-to-end semi-supervised pr...
  </details>

- **2026-10-21** — Shipeng Liu, Garima Bazard, Khac-Hoang Ngo et al. — [Point Cloud Transmission With Patch-Based Rate Adaptation](http://arxiv.org/abs/2610.29479v1)
  <details><summary>📄 Abstract</summary>
  We propose a joint source-channel coding (JSCC) framework for efficient wireless point cloud transmission. In the proposed scheme, the point cloud is first divided into local patches and transformed into compact latent representations, which are then mapped to symbols for transmission over a noisy channel. Our model incorporates an entropy model that exploits inter-patch spatial dependencies to estimate patch-level coding costs and allocate different numbers of symbols accordingly. Unlike existi...
  </details>

- **2026-10-21** — Ruijie Zhang, Huaxiao Yin, Li Hu et al. — [RegoMender: A Multi-agent Framework for Automated Rego Policy Repair](http://arxiv.org/abs/2610.29456v1)
  <details><summary>📄 Abstract</summary>
  Policy-as-Code (PaC) has emerged as a foundational paradigm in cloud-native systems. However, repairing Rego policies remains challenging due to their strict syntax, declarative semantics, and specific verification requirements. Existing automated program repair (APR) methods are mainly designed for mainstream languages and struggle to accommodate the unique policy logic and repair workflows of Rego. Thus, Rego policy repair remains a manual process driven by trial and error. To address this, we...
  </details>

- **2026-10-21** — Yuan Ge, Pei Zhang, Xize Cheng et al. — [Omnilingual-MsASR: Benchmarking Multimodal, Multilingual, Long-Form Multi-Speaker ASR of Omni Large Language Models](http://arxiv.org/abs/2610.29455v1)
  <details><summary>📄 Abstract</summary>
  Omni-modal large language models (LLMs) have achieved remarkable progress in audio and video understanding. However, existing models struggle with long-form, multi-speaker videos, especially in understanding the entire video and recognizing who says what and when. To characterize the capability limit of current omni LLMs and guide future model development, we introduce Omnilingual-MsASR, a multilingual, multimodal benchmark for long-form Multi-speaker Automatic Speech Recognition (MsASR) coverin...
  </details>

- **2026-10-21** — Keith Kwok, Wanting Ning, Tej Deep Pala et al. — [Beyond Small Talk: Modeling Disclosure Trajectories in Human-AI Conversation](http://arxiv.org/abs/2610.29413v1)
  <details><summary>📄 Abstract</summary>
  Recently, we see a rise in conversational agents as a form of social and emotional support, where disclosure will unfold over time. Yet, current evaluations of these agents typically examine isolated conversational states. In analyses of naturally occurring conversations, disclosure history and current disclosure are confounded which tends to make their effects difficult to isolate. We thus introduce Trajectory-based Disclosure Evaluation (TraDE), an evaluation framework grounded in Social Penet...
  </details>

- **2026-10-21** — Donghyun Jeong, Yoon-Yeong Kim — [GaP-MoE : Explicit Expert Specialization in Mixture-of-Experts via Orthogonal Gradient Accumulation and Projection](http://arxiv.org/abs/2610.29355v1)
  <details><summary>📄 Abstract</summary>
  Sparse Mixture-of-Experts (SMoE) models improve scalability by routing input tokens to only a subset of expert networks, but they often suffer from representation collapse, in which multiple experts converge toward similar functions and lose their intended diversity. Prior work has addressed this limitation either by improving router architectures or by introducing auxiliary loss terms that implicitly penalize similarity among experts. However, router-based approaches remain vulnerable to routin...
  </details>

- **2026-10-21** — Ni Zhang, Haofeng Yuan, Jianan Zhou et al. — [LLM-Based Exogenous World Modeling for Dynamic Scheduling](http://arxiv.org/abs/2610.29308v1)
  <details><summary>📄 Abstract</summary>
  Dynamic scheduling requires dispatching online arrivals while anticipating future jobs, as poor decisions can compound downstream costs under nonlinear tardiness objectives. We show that a pretrained large language model (LLM) can serve as the exogenous component of a structured world model, forecasting uncertain future job arrivals. Specifically, we exploit an afterstate decomposition, which separates known deterministic shop transitions from uncertain exogenous job arrivals, enabling the LLM t...
  </details>

- **2026-10-21** — Hanhui Xu, Jiacheng Ji, Yuhan Wang et al. — [Situating Vulnerability: An Ethical Governance Framework for Anthropomorphic AI Interaction](http://arxiv.org/abs/2610.29304v1)
  <details><summary>📄 Abstract</summary>
  Large language models increasingly address users in the register of care: they remember personal details, adopt a first-person emotional voice, and sustain relationships across many sessions. This anthropomorphic mode of interaction generates risks that output-level metrics capture poorly, because the same empathic utterance may console one user, entrap a second, and consolidate a delusion in a third. Governance has responded in two ways. Uniform restriction refuses sensitive requests or suppres...
  </details>

- **2026-10-21** — Yongqiang Chen, Chenxi Liu, Deyu Zou et al. — [ExpEvolve: Structuring and Reusing Experience for Open-Ended Discovery](http://arxiv.org/abs/2610.29303v1)
  <details><summary>📄 Abstract</summary>
  Evolutionary coding agents such as AlphaEvolve are one of the notable successes in using Large Language Models (LLMs) to build AI Scientists. These agents tackle open-ended scientific problems by iteratively improving and evolving programs, leveraging the prior knowledge and reasoning capabilities of LLMs. Despite their success, mutations over programs are mostly low-level upon surface heuristics, without a persistent unit of control. In contrast, science compounds through ideas. In this work, w...
  </details>

- **2026-10-21** — Guoqiang Hua, Sakshi Udeshi, Matheus Eduardo Garbelini et al. — [5uGUE: Agentic Hardware-in-the-Loop Fuzzing for 5G Devices and beyond](http://arxiv.org/abs/2610.29155v1)
  <details><summary>📄 Abstract</summary>
  In this paper, we present 5uGUE, a large language model (LLM)-driven hardware-in-the-loop agent, which enables the wireless fuzzing of 5G-enabled devices (such as mobile phones). 5uGUE combines multi-step reasoning with tool-assisted interaction and integrates into the fuzzing pipeline by leveraging specialized tools for internet search, 5G protocol analysis, memory management, and test-case execution. The agent iteratively generates test cases, executes them on targets, collects runtime feedbac...
  </details>

- **2026-10-20** — Zhe Ye, Udaya Ghai, Zhizhen Qin et al. — [Agentic Verified Optimization of Real-World Software](http://arxiv.org/abs/2610.30188v1)
  <details><summary>📄 Abstract</summary>
  Program optimization aims to improve performance while preserving behavior. Coding agents can already make programs faster by changing algorithms, data structures, and execution strategies. However, existing equivalence checks mostly rely on tests, which agents have been shown to exploit, passing the tests without preserving the intended behavior. We propose agentic verified optimization, in which an agent produces a faster implementation together with a machine-checked proof of equivalence to t...
  </details>

- **2026-10-20** — Rui Melo, Andre Duarte, Aditya Oke et al. — [Self-Evolving Static Analysis via LLM Pseudo-Labeling](http://arxiv.org/abs/2610.30184v1)
  <details><summary>📄 Abstract</summary>
  Security bugs often slip past static analysis not because they are impossible to detect, but because detection rules have not yet been written for the code in front of us. New frameworks, APIs, and coding idioms continually create such gaps, leaving developers to discover failures and manually encode new rules. We present SESAA, a framework in which an Large Language Model (LLM) agent starts from no rules and iteratively evolves a set of readable and auditable joern queries.   The agent receives...
  </details>

- **2026-10-20** — Peng Zhang, Tingfa Xu, Jinrui Sui et al. — [S$^3$E-Det: A Strict Spatial-Spectral Equivariant Detector for Multispectral Object Detection](http://arxiv.org/abs/2610.27882v2)
  <details><summary>📄 Abstract</summary>
  Multispectral object detection requires detectors to exploit material-dependent spectral responses while maintaining consistent localization under geometric variations. Existing MOD detectors learn discriminative spectral representations, yet lack a unified mechanism that preserves spectral order, adapts spectral-context fusion across pyramid levels, and regulates geometric responses under rotation. To address these limitations, we propose S$^3$E-Det, a strict spatial-spectral equivariant detect...
  </details>

- **2026-10-20** — Muxuan He, Wang Bill Zhu, Yue Chen et al. — [Language Impairment as a Lens onto Large Language Models](http://arxiv.org/abs/2610.28992v1)
  <details><summary>📄 Abstract</summary>
  Although large language models (LLMs) encode language in highly distributed spaces, they remain vulnerable to focal disruptions---a phenomenon strikingly similar to how localized brain damage causes clinical aphasia in humans. To investigate this theoretical tension, we ask whether LLMs possess a functional structure analogous to the human language system, by introducing a novel mechanistic interpretability framework inspired by aphasia. Through two complementary approaches, classifier-guided le...
  </details>

- **2026-10-20** — Weiqin Chen, Xinlong Du, Gesualdo Scutari et al. — [Is In-Context Reinforcement Learning A Posterior Sampler? An Empirical Study](http://arxiv.org/abs/2610.28977v1)
  <details><summary>📄 Abstract</summary>
  In-context reinforcement learning (ICRL) exploits the impressive in-context learning ability of large language models to zero-shot generalize to new, unseen tasks at inference time without any parameter updates. Among many approaches, the Decision-Pretrained Transformer (DPT) is particularly appealing for its theoretical grounding: under idealized assumptions such as a sufficiently expressive model and infinite pretraining data, DPT can perform Bayesian posterior sampling. Whether this character...
  </details>

- **2026-10-20** — Gonzalo Gómez-Nogales, Daohan Lu, Peiye Zhuang et al. — [Pair-Free Coarse-to-Real Video Generation via Real-to-Coarse Image Supervision](http://arxiv.org/abs/2610.28954v1)
  <details><summary>📄 Abstract</summary>
  Coarse-to-real (C2R) video generation converts coarse animation, simulation, or game-rendered videos into photorealistic videos while preserving scene layout, camera motion, and dynamics. Training such models requires aligned (coarse, realistic) video pairs, which are expensive to create and confine prior systems to narrow synthetic domains. We exploit a simple asymmetry: paired videos are hard to obtain, but paired real-to-coarse images are easy to construct with existing editing and 3D reconst...
  </details>

- **2026-10-20** — Anrui Gu, Zhichao Wang, Nicolai Ouporov — [Fig: Automated Multiagent Behavior Elicitor](http://arxiv.org/abs/2610.28891v1)
  <details><summary>📄 Abstract</summary>
  Many social evaluations for multiagent systems study behaviors as they emerge from environments instead of systematically intervening in the environment to elicit such behaviors. We introduce Fig (Finding Interactions in Games), an agentic system that performs targeted elicitation interventions on game environments. It takes a natural language behavior description, decomposes it into sub-behaviors, generates new social games or selects existing ones, and executes single or combined interventions...
  </details>

- **2026-10-20** — Yujian Liu, Li An, Zelin He et al. — [Building AI Research Teams for Autonomous Discovery of Linear Attention Architectures](http://arxiv.org/abs/2610.28887v1)
  <details><summary>📄 Abstract</summary>
  Autonomous agents can increasingly propose ideas, modify code, and run experiments, creating an opportunity to accelerate scientific discovery using teams of collaborative AI researchers. To escape local minima in the discovery, we propose to encourage orthogonal exploration by constructing the team using agents with varying expertise. However, realizing this design requires more than diverse backgrounds. When experiments are costly, a team can test only a limited number of ideas, thereby creati...
  </details>

- **2026-10-20** — Wendy Zheng, Liang Wu, Yinhan He et al. — [A Mechanistic Study of Automated Failure Attribution in LLM-based Agentic Systems](http://arxiv.org/abs/2610.28811v1)
  <details><summary>📄 Abstract</summary>
  Agentic systems have demonstrated strong capabilities on complex tasks by enabling multiple interacting large language model (LLM)-based agents to collaborate and execute subtasks in parallel. However, this collaborative structure introduces new challenges for reliably evaluating and diagnosing system failures, particularly failure attribution: tracing a system's execution to identify the agent step responsible for an incorrect final outcome. Because manually performing this task is time- and la...
  </details>

- **2026-10-20** — Ganni Galea Curmi, Ben Wilde — [How Much Does the Harness Matter, and for Whom? A Multi-Model Study of Context in LLM-Driven Vulnerability Discovery](http://arxiv.org/abs/2610.28802v1)
  <details><summary>📄 Abstract</summary>
  How much does an agent harness affect vulnerability discovery, and does its value depend on the model? We study 24 model-runner configurations using an open-source harness on a production codebase whose vulnerabilities were non-public at scan time. The pipeline combines static screening, LLM investigation, model self-revalidation, root-cause mapping, independent source review, and isolated proof-of-concept confirmation.   Across 265 confirmed security root causes, the largest two-run configurati...
  </details>

- **2026-10-20** — Berke Arda, Peng Cui, Qiaoyuan Zheng et al. — [SkillEval: Learning Interpretable Ability Profiles of LLMs via Cognitive Diagnosis Models](http://arxiv.org/abs/2610.28767v1)
  <details><summary>📄 Abstract</summary>
  Current evaluation of LLMs on benchmarks typically aggregates performance over individual examples into a single scalar score. This approach is overly coarse and ignores the diverse scope of skills covered by benchmark datasets. To address this limitation and better exploit benchmark data, we propose SkillEval, a new evaluation framework that performs cross-model, skill-level analysis. The framework integrates advances from two areas: (1) it leverages the meta-cognitive capabilities of LLMs to a...
  </details>

- **2026-10-20** — Maria Victoria Carro, Denise Alejandra Mester, Facundo Nieto et al. — [Humans Correct Their Judgments Through Debate, but Weaker AI Models Do Not](http://arxiv.org/abs/2610.28539v1)
  <details><summary>📄 Abstract</summary>
  How can we effectively oversee AI systems that surpass human intelligence? AI Safety via Debate proposes that two AI systems argue opposing positions and a judge, either a human or a weaker model, decides which is correct. By facilitating supervisors in providing high-quality training signals, debate aims to encourage truthful and safe behavior from AI systems whose capabilities exceed our own. However, human judgment is not neutral: people often rely on biases which advanced AI systems may lear...
  </details>

- **2026-10-20** — Vita Santa Barletta, Danilo Caivano, Gabriel Cellammare et al. — [A Digital Twin to Improve Cyber-Social Impact](http://arxiv.org/abs/2610.28430v1)
  <details><summary>📄 Abstract</summary>
  The increasing complexity of Industrial Control Systems (ICS) and their integration with IT infrastructures has significantly expanded the cyber threat landscape. Traditional cybersecurity models, primarily based on the Confidentiality, Integrity, and Availability (CIA triad), fail to capture the broader societal and operational impacts of cyberattacks. This paper proposes a novel framework that integrates Digital Twin technology with a Cyber-Social Security model to simulate, analyze, and quant...
  </details>

- **2026-10-20** — Yulong Li, Jiale Meng, Zhenlin Guo et al. — [Fast and scalable multi-GPU sliced FFT solvers for asymptotically compatible discretizations of 3D nonlocal diffusion problems](http://arxiv.org/abs/2610.28372v1)
  <details><summary>📄 Abstract</summary>
  Large-scale 3D peridynamic transient diffusion simulations are constrained by the computational cost and memory requirements of nonlocal interactions. We propose a fast and scalable multi-GPU sliced FFT algorithm based on the recently developed asymptotically compatible finite difference (ACFD) scheme. By exploiting the discrete operator's structure and finite interaction range, the algorithm combines FFT acceleration with local inter-GPU communication. It preserves the ACFD scheme while avoidin...
  </details>

- **2026-10-20** — Juntang Wang, Hao Wu, Yihan Wang et al. — [Recommending Bacterial Cultivation Conditions from 16S rRNA](http://arxiv.org/abs/2610.28310v1)
  <details><summary>📄 Abstract</summary>
  Recommending bacterial cultivation conditions from sequence data is a challenging structured problem characterized by missing standardized benchmarks and limited use of sequence structure. To address this, we introduce DSNI, a benchmark of 65,023 bacterial strains with phylogeny-aware splits, pairing 16S rRNA sequences with four cultivation conditions (media, temperature, pH, oxygen). Exploiting the mosaic structure of 16S rRNA, where hypervariable regions support discrimination and conserved re...
  </details>

- **2026-10-20** — Youwei Zhou, Bohan Hou, Yankai Fu et al. — [Large Multimodal Models for Direct Robot Control: GPT-6 as a Beginning](http://arxiv.org/abs/2610.28259v1)
  <details><summary>📄 Abstract</summary>
  Recent advances in visuospatial understanding and agentic reasoning enable direct robotic manipulation with general-purpose multimodal models, but their embodied capabilities remain poorly understood. This paper systematically evaluate GPT-6 Astra for closed-loop robotic manipulation using a lightweight agent execution framework. We first probe three fundamental embodied capabilities-depth perception, embodied in-context learning, and tactile understanding-and demonstrate that the model can expl...
  </details>

- **2026-10-20** — Christopher Conrad, Deepak Panda, Weisi Guo et al. — [Interruption-Aware Recurrent Reinforcement Learning for UAS Navigation Under Temporary Overrides](http://arxiv.org/abs/2610.28121v1)
  <details><summary>📄 Abstract</summary>
  Safe autonomous navigation of UASs requires tactical deconfliction to address conflicts that strategic coordination cannot prevent. This task is challenging under partial observability, when sensor or traffic data are missing, delayed, or degraded. Geometry-based methods can offer separation assurances but face limitations in dense encounters. Recurrent reinforcement learning has therefore been proposed to learn navigation policies that integrate observation-action histories to optimise long-ter...
  </details>

- **2026-10-20** — Yousra Fettach, Tijl De Bie — [BAIT: Can LLMs Find What Biases a Reader? A Benchmark for Cognitive Bias Triggers in News](http://arxiv.org/abs/2610.28092v1)
  <details><summary>📄 Abstract</summary>
  Persuasive writing exploits cognitive biases, recruiting a reader's mental shortcuts to shape belief, often without the reader noticing. We call the linguistic features exploiting such mental shortcuts cognitive bias triggers. As large language models (LLMs) increasingly mediate how people encounter news, summarizing it, ranking it, and answering questions over it, a natural question is whether they can recognize the features of a text that bias a human reader. We introduce BAIT (Bias Annotation...
  </details>

- **2026-10-20** — Jarek Liesen, Matthew T. Jackson, Benjamin Ellis et al. — [MoDDiT: Simple Token Routing in Diffusion Transformers](http://arxiv.org/abs/2610.28086v1)
  <details><summary>📄 Abstract</summary>
  Real-time video generation, interactive world models, and on-device image synthesis are almost a reality. Diffusion Transformers (DiT) achieve excellent sample quality, shifting the bottleneck to the throughput of the models themselves. Natural images are inherently sparse, as large portions of an image are often background, contribute little to the scene content, and are easy to denoise. DiTs fail to exploit this sparsity, as they process image tokens statically and uniformly. We propose MoDDiT...
  </details>

- **2026-10-20** — Aleksandr Shestakov, Vladimir Aletov, Aleksandr Beznosikov — [On Johnson-Lindenstrauss Transforms for Byzantine-Robust Optimization](http://arxiv.org/abs/2610.27989v1)
  <details><summary>📄 Abstract</summary>
  The growing scale of data and models in machine learning calls for efficient optimization methods. Distributed optimization addresses this challenge, with compression mechanisms helping to reduce communication costs. A classical tool for dimensionality reduction is the Johnson-Lindenstrauss (JL) transform, which is simple to implement and offers strong geometric guarantees. In particular, JL transforms approximately preserve inner products and pairwise distances between vectors with high probabi...
  </details>

- **2026-10-20** — Byeonghun Bang, Sangwoo Park, Jinheon Baek et al. — [Lost in Recovery: Demystifying Recovery Behavior of Computer-Use Agents via Goal-Oriented Action Replay](http://arxiv.org/abs/2610.27954v1)
  <details><summary>📄 Abstract</summary>
  Recent advances in large (vision) language models have enabled computer-use agents that automate digital workflows via fine-grained keyboard and mouse operations. However, such agents remain fragile in long-horizon settings, where errors accumulate and executed actions leave unintended side effects, making the ability to recover from failures critical. Yet, existing remedies remain inadequate: environment resets are infeasible in proprietary settings, action replay is prohibitively expensive ove...
  </details>

- **2026-10-20** — Peng Zhang, Tingfa Xu, Jinrui Sui et al. — [S$^3$E-Det: A Strict Spatial-Spectral Equivariant Detector for Multispectral Object Detection](http://arxiv.org/abs/2610.27882v1)
  <details><summary>📄 Abstract</summary>
  Multispectral object detection requires detectors to exploit material-dependent spectral responses while maintaining consistent localization under geometric variations. Existing MOD detectors learn discriminative spectral representations, yet lack a unified mechanism that preserves spectral order, adapts spectral-context fusion across pyramid levels, and regulates geometric responses under rotation. To address these limitations, we propose S$^3$E-Det, a strict spatial-spectral equivariant detect...
  </details>

- **2026-10-20** — Olivier Nourry, Yoshiki Higo — [RELAY: Scaling Historical Build Restoration through Rule Reuse and Agentic Repair](http://arxiv.org/abs/2610.27784v1)
  <details><summary>📄 Abstract</summary>
  Vulnerability benchmarks and software engineering research depend on rebuilding historical software. Yet builds rely on external resources, such as base images and packages, that change independently of the source code. In this study, we examine this environment decay on 14,159 OSS-Fuzz cases. We find that 69.7% no longer complete reconstruction and verification, and that most failures share a small number of recurring failure symptoms. A recurring failure can therefore be diagnosed once and its...
  </details>

- **2026-10-20** — Junyu Wang, Tianrui Wang, Meng Ge et al. — [AD-Mamba: Architecture-Complementary Knowledge Distillation for Efficient and Robust Audio Classification](http://arxiv.org/abs/2610.27713v1)
  <details><summary>📄 Abstract</summary>
  Recent advancements in large-scale audio classification have been primarily driven by Transformer-based architectures due to their strong capacity in modeling long-range dependencies. However, their inherent quadratic complexity limits scalability and efficiency, especially when processing long or sparsely informative audio streams. Mamba, a recently proposed state space model (SSM), offers a promising alternative by enabling efficient long-range modeling with linear sequence scaling. Neverthele...
  </details>

- **2026-10-20** — Wenjie Gan, Zhaoxi Zhang, Jiahui Liang et al. — [Enhancing Bug-Exposing Test Generation via Step-Level Credit Assignment and Self-Distillation from Valuable Failures](http://arxiv.org/abs/2610.27694v1)
  <details><summary>📄 Abstract</summary>
  Large Language Models have shown strong code generation capabilities, yet their outputs often contain subtle bugs. Automatically repairing such code requires informative tests: inputs that expose faulty behavior, paired with correct expected outputs. Recent RL-based test generation methods apply the same outcome reward to all reasoning steps, which can discourage useful reasoning and reinforce flawed steps. They also fail to effectively learn from trajectories that find bug-triggering inputs but...
  </details>

- **2026-10-20** — Romina Omidi, Nima Naderloui, Yuan Hong et al. — [A Unified Attack Framework against Statistical Generative Watermarks for Large Language Models](http://arxiv.org/abs/2610.27653v1)
  <details><summary>📄 Abstract</summary>
  Watermarking has emerged as a key tool for identifying text generated by large language models (LLMs), with current schemes embedding statistical signals into the generation process to enable later detection. In this work, we identify a shared weakness across a broad class of popular LLM watermarking methods, including KGW (and its variants), GumbelSoft, DipMark, ITS, and SynthID. We show that these schemes exhibit a fundamental link between their detection scores and the token probability shift...
  </details>

- **2026-10-20** — Jing Wang, Yitong Yang, Hao Dou et al. — [TriGeoBench: A Multimodal Mathematical Geometry Benchmark with Figures and TikZ](http://arxiv.org/abs/2610.27626v1)
  <details><summary>📄 Abstract</summary>
  Multimodal Large Language Models show strong vision-language capabilities, yet their geometry-centric reasoning remains insufficiently understood. Existing mathematical benchmarks typically rely on rasterized figures and cover limited geometric knowledge areas and response formats, making it difficult to assess whether models reason over geometric structures or exploit superficial visual patterns. We introduce TriGeoBench, a geometry-centric multimodal benchmark constructed from Chinese middle- ...
  </details>

- **2026-10-20** — Tongrun Xing, Yongjun Dai, Xuan Liao et al. — [Bridging Digital Deception and Physical Fidelity: A Spatio-Temporal Attack on Cognitive Radars](http://arxiv.org/abs/2610.27585v1)
  <details><summary>📄 Abstract</summary>
  As cognitive radars evolve towards the end-to-end processing of one-dimensional complex baseband sequences, deep networks face severe adversarial threats. However, existing attacks encounter dual limitations in practical electronic warfare: low cross-architecture transferability and severe vulnerability to physical channel distortions, which degrades their tactical reliability. To overcome these bottlenecks, we propose a physical prior-driven Segmented Spatio-Temporal Attack (SSTA). First, a glo...
  </details>

- **2026-10-20** — Maosen Zhang, Jianshuo Dong, Yutong Zhang et al. — [The Show-Up Attack: When Subagents Win Over Their Supervisor](http://arxiv.org/abs/2610.27574v1)
  <details><summary>📄 Abstract</summary>
  Multi-agent systems are increasingly deployed to coordinate multiple large language model (LLM) agents. However, this also creates new attack surfaces: malicious agents may have chances to exploit the coordination. In this paper, we propose and study the \textit{show-up attack}, in which a malicious subagent manipulates the supervisor into involving it in tasks beyond its assigned scope. To evaluate this risk, we propose SUA-Arena, which implements 6 attack strategies and contains 188 test cases...
  </details>

- **2026-10-20** — Sadia Asif, Israel Antonio Rosales Laguan, Shumaila Asif et al. — [When LLMs Manipulate: Measuring Behavioral, Social, and Temporal Effects](http://arxiv.org/abs/2610.27573v1)
  <details><summary>📄 Abstract</summary>
  Large language models (LLMs) can influence user trust and decision-making through subtle linguistic cues, yet the behavioral effects of manipulative outputs remain poorly quantified. We introduce a behavioral computing framework for measuring \textit{behavioral vulnerability}, defined as users' susceptibility to manipulative AI responses. Building on DarkPatterns-LLM benchmark, we generate controlled manipulative stimuli using Manipulation Gradient Descent (MGD), targeting biases associated with...
  </details>

- **2026-10-20** — Thomas E. Coons, Aniket Jivani, Xun Huan — [Active Pilot Sampling for Multi-fidelity Estimation in Stochastic Optimization](http://arxiv.org/abs/2610.27563v1)
  <details><summary>📄 Abstract</summary>
  Stochastic optimization with high-fidelity nonlinear models is often computationally prohibitive because each objective evaluation requires sampling-based uncertainty quantification inside an outer optimization loop. Multi-fidelity estimators, such as approximate control variates (ACV), can reduce this cost by exploiting cheaper low-fidelity models, but they require model-output covariance information to determine control-variate weights and sample allocations. These covariances are generally un...
  </details>

- **2026-10-20** — Hao Yan, Guanghui Wang — [Progressive Subset Selection and Cascaded Consistency for Unsupervised Vision-Language Model Adaptation](http://arxiv.org/abs/2610.27515v1)
  <details><summary>📄 Abstract</summary>
  Pretrained Vision-Language Models (PVLMs) achieve strong zero-shot recognition but often suffer performance degradation under target-domain shift. Unsupervised adaptation provides a practical way to improve target-domain performance without labeled data, but it remains challenging because pseudo-labels generated by the model can be unreliable and no labeled validation set is available for model selection or early stopping. We propose a simple framework for unsupervised PVLM adaptation that combi...
  </details>


### 📂 defense
*防御与防护方法 / Defense & Protection Methods* — 44 papers

- **2026-10-22** — Ali Al-Lawati, Elsayed Eshra, Dongwon Lee et al. — [Diffusion Language Models for Perplexity-Aware Black-Box Attacks](http://arxiv.org/abs/2610.31558v1)
  <details><summary>📄 Abstract</summary>
  \emph{Continuous-space} attacks find prompts that trigger malicious behaviors, such as overthinking, in black-box LLMs by sampling or optimizing over a low-dimensional Gaussian latent space and decoding it to text through a \emph{random mapping} and nearest-token lookup. Because the random mapping is not learned from language, its prompts can be highly unnatural, and as such easily detectable through input guardrails, and the risk estimates they yield are not grounded in natural prompts. In this...
  </details>

- **2026-10-22** — Arnon Mazza, Elad Levi — [SCOPE: Compiling Natural-Language Policies into Neurosymbolic Predicate Programs](http://arxiv.org/abs/2610.31062v1)
  <details><summary>📄 Abstract</summary>
  Policy enforcement for LLM agents has shifted from single-turn content moderation to compound, application-specific policies evaluated over multi-turn transcripts and tool-call trajectories. Fine-tuned guardrail models are efficient but degrade on compound policies, and while LLM-as-a-judge approaches achieve higher accuracy, they incur high inference cost and tend to produce unstable predictions. Neurosymbolic methods offer a natural alternative, decomposing the policy into narrow neural decisi...
  </details>

- **2026-10-22** — Yifan Wang, Dongliang Xu, Xiaoyong Li et al. — [SecLog-Bench: A Scalable Benchmark for Cybersecurity Log Reasoning with Scaffolded Evidence](http://arxiv.org/abs/2610.31000v1)
  <details><summary>📄 Abstract</summary>
  Large language models (LLMs) have shown strong potential for cybersecurity, leading to growing interest in LLM-based automated cybersecurity log analysis. However, current datasets (1) are limited in scale; (2) rely mainly on single-source evidence; and (3) have only binary or multi-class attack labels, without dense annotations of the reasoning process. To address these limitations, SecLog-Bench has three key features. First, we build an extensible simulation platform that covers 29 attack scen...
  </details>

- **2026-10-22** — Ke Zhu, Yanli Chen, Ling Xiong et al. — [HiMark: Hierarchical and Controllable Multi-bit Watermarking for Large Language Models](http://arxiv.org/abs/2610.30601v1)
  <details><summary>📄 Abstract</summary>
  With the rapid adoption of large language models (LLMs) in text generation applications, it has become increasingly difficult to trace generated content and assign responsibility for its use, raising concerns about provenance, copyright protection, and accountability. Multi-bit watermarking addresses these issues by embedding multi-bit provenance information into generated text, but reliable extraction remains difficult due to sparse per-bit evidence and the trade-off between watermark-extractio...
  </details>

- **2026-10-22** — Bayram Ayadi, Florian Geissler, Johanna Schmidhuber — [From Structured Records to Patient Narratives: Preserving Clinical Alignment in LLM-Generated Health Summaries](http://arxiv.org/abs/2610.31467v1)
  <details><summary>📄 Abstract</summary>
  As wearable and digital health systems increasingly generate longitudinal physiological records, communicating these observations in patient-accessible language remains a significant challenge. Large Language Models (LLMs) offer a promising mechanism for translating structured clinical information into readable narratives, but this process may introduce semantic drift, where clinically precise meaning is distorted during simplification. We investigate evidence-grounded health summarization for m...
  </details>

- **2026-10-22** — Ruicong Liu, Liangyang Ouyang, Fengbo Lan et al. — [AnyGameRenderer: Entity-Consistent Generative Rendering Across Games and an Entity-Level Benchmark](http://arxiv.org/abs/2610.31466v1)
  <details><summary>📄 Abstract</summary>
  AI coding agents can now build small playable games in minutes, but the results usually look like programmer art: gray blockouts, colored geometric primitives, and flat semantic blobs. We present AnyGameRenderer, a video-to-video generative renderer that turns such footage into high-quality visuals with characters, motion detail, and effects. Throughout, it keeps the layout, camera, and every entity's position and timing intact.   Our AnyGameRenderer generalizes across a wide range of genres tha...
  </details>

- **2026-10-22** — Bastien Le Guellec, Su Hwan Kim, Raphael Bentegeac et al. — [Major Revision, Minor Accountability: LLMs as Reviewers of Published Articles in Top-Tier Journals](http://arxiv.org/abs/2610.31414v1)
  <details><summary>📄 Abstract</summary>
  With the growth of scientific output, the peer review system is approaching a breaking point: reviewers are increasingly hard to secure, and turnaround times lengthen accordingly. LLM-assisted or LLM-generated peer review has been proposed as a remedy, but how such models would treat manuscripts already published in top-tier journals, the closest thing the current system has to a gold standard of scientific validity, is not known. Here we assembled a corpus of 200 articles, each released under a...
  </details>

- **2026-10-22** — Arsalan Jalil Sarghaleh, Mehdi Hazrati — [Auditing the Hand-Written Inputs of Learned Access Control](http://arxiv.org/abs/2610.31388v1)
  <details><summary>📄 Abstract</summary>
  Learned access control is typically deployed behind two hand-built artefacts: a hard-deny set enforced by a small trusted shield, and a region map that decides which requests mined rules answer and which the learner answers. Verifying the shield or measuring the learner validates neither. We audit both on the five public ABAC Lab policies. First, we formalise hard-deny soundness and check it exhaustively over relations of up to 794,250 tuples. Clauses that faithfully transcribe an explicit restr...
  </details>

- **2026-10-22** — Zhiyuan Li, Yuge Zhang, Jie Chen et al. — [From Signals to Evidence: Interpretable Underwater Acoustic Target Sensing with Large Language Models - Part II: Passive Detection](http://arxiv.org/abs/2610.31346v1)
  <details><summary>📄 Abstract</summary>
  Underwater acoustic passive detection is essential to maritime surveillance and intelligent ocean sensing. Existing detection systems typically collapse multichannel array observations into a binary decision or a scalar confidence score, offering limited insight into the physical evidence that supports or contradicts a target declaration. This limitation is acute at low signal-to-noise ratio (SNR), where isolated spectral peaks and transient beamforming responses are inherently ambiguous and phy...
  </details>

- **2026-10-22** — Changseon Yu, Hyeokjun Kweon — [ReCoG: Relational Concept Graph for Training-Free Personalization](http://arxiv.org/abs/2610.31282v1)
  <details><summary>📄 Abstract</summary>
  Training-free personalization adapts a frozen vision-language model (VLM) to recognize user-defined concepts from only a few exemplars by retrieving concept entries at inference time. While recent retriever-based methods enrich each concept with descriptive evidence, they largely treat concepts in isolation, so the retrieved information can be plausible yet non-discriminative, especially when the personalized concept set contains highly confusable, fine-grained categories. We argue that personal...
  </details>

- **2026-10-22** — Zhilong Fang, Qi Zhang, Jujie Yan et al. — [GeoAgent: Contract-Constrained LLM Agents for Seismic Data Processing](http://arxiv.org/abs/2610.31096v1)
  <details><summary>📄 Abstract</summary>
  Large language models (LLMs) can drive scientific software through function calling, but free-form tool use is fragile on long, data-dependent processing chains. Models omit arguments, invent units, feed the previous artifact into the wrong input, and report completion without a verifiable product. We present GeoAgent, an agent system for seismic data processing built on Madagascar's roughly 1{,}965 command-line programs. GeoAgent exposes 54 operator agents (51 generated from a declarative speci...
  </details>

- **2026-10-22** — Haeun Yu, Geert Heyman, Pepa Atanasova et al. — [A Reality Check of Inference-Time Context Augmentation Methods](http://arxiv.org/abs/2610.30983v1)
  <details><summary>📄 Abstract</summary>
  Large language models (LLMs) often fail to utilise the context given in the input, resulting in hallucinations or a fallback to parametric knowledge. Context augmentation methods aim to improve model performance by modifying the input, from inserting filler tokens that add computational time to adding relevant content such as elaboration of a context during inference. However, these methods have been evaluated in isolation and only by their performance gains, leaving it unclear how they compare ...
  </details>

- **2026-10-22** — Luong Tuan Thanh, Abhijit Sanyal — [REGATTA: A Cross-Domain Measurement Framework and Fault-Injection Harness for Enterprise AI Agents](http://arxiv.org/abs/2610.30924v1)
  <details><summary>📄 Abstract</summary>
  Enterprise AI-agent evaluation needs evidence about whether test suites expose specified faults and whether their reference rules are trustworthy. We introduce REGATTA (Regulatory Evaluation of Agents via Two-stage Testing and Assurance), a measurement framework with three instruments. A 125-item source-cited checklist spans five industry-by-jurisdiction cells across the United States and Vietnam. A 25-fault corpus covers five categories, and a harness scores suite-level fault detection at the d...
  </details>

- **2026-10-22** — Viet-Thanh Pham, Thuy-Trang Vu, Junae Kim et al. — [UniGuard: Multi-View Guardrail Learning for Cross-Interface Safety Generalization](http://arxiv.org/abs/2610.30742v1)
  <details><summary>📄 Abstract</summary>
  Guardrail models are increasingly used as safety layers for LLMs and agentic systems, but most are trained on fixed prompt or response interfaces and become unreliable when the same safety case appears as a conversation, agent trajectory, multi-agent trace, or policy-conditioned input. We propose UniGuard, a training framework that learns interface-invariant safety representations from multiple semantically aligned views of the same safety case. We also construct the UniGuard-FT dataset by trans...
  </details>

- **2026-10-22** — Chenhan Lyu, Kit Wislocki, Sarah Elizabeth Stoeckl et al. — [From Clinical Judgment to Checkable Rules: Clinician-Led Guardrails for Mental-Health Chatbots](http://arxiv.org/abs/2610.30690v1)
  <details><summary>📄 Abstract</summary>
  Large language models (LLMs) deployed in mental-health contexts can be evaluated for safety failures, but the resulting judgments are often difficult to inspect or explain. Common approaches to improving safety rely on prompt engineering, LLM-as-a-Judge, and Constitutional AI. In this work, we describe a clinician-led alternative in which two clinicians define, finalize, and adjudicate the four safety checks of a rule base, which is formally verified for internal consistency and applied as a gua...
  </details>

- **2026-10-22** — Yuchen Wu, Jerry Wei — [Scaling Laws for Safety Probes](http://arxiv.org/abs/2610.30678v1)
  <details><summary>📄 Abstract</summary>
  Safety probes trained on a model's activations are a standard tool for monitoring language models in real time. Each time a new model is released or a new harm area needs to be monitored, the probe must be retrained, which requires new labels and a choice of probe architecture. Yet neither the model nor the labels tell us in advance how well the resulting probe will perform. Finding out requires training and comparing many probe configurations. In this paper, we ask whether probe performance can...
  </details>

- **2026-10-22** — Zhijie Zhong, Zhiwen Yu, Pengyu Li et al. — [Future of Time Series Anomaly Detection: From Historical Review to Unified Outlook](http://arxiv.org/abs/2610.30628v1)
  <details><summary>📄 Abstract</summary>
  Time series anomaly detection (TSAD) is a foundational problem in data mining, aiming to identify observations that deviate significantly from nominal temporal patterns. Driven by escalating data volumes and application complexity, recent research has yielded diverse architectures, including diffusion models, state space models, and large language models (LLMs). However, existing surveys provide limited coverage of these emerging designs and lack a unified treatment of multivariate anomalies, cr...
  </details>

- **2026-10-22** — Qian Chen, Saatvik Pradhan, Janice Ahn et al. — [Beyond Better Ideas: How Human-AI Collaboration Shapes Scientific Ideas and Human Perceptions](http://arxiv.org/abs/2610.30568v1)
  <details><summary>📄 Abstract</summary>
  As AI increasingly becomes a collaborator in scientific research, its impact may extend beyond improving ideas to reshaping how they are evaluated, attributed, and perceived by humans. Yet existing research has largely examined these dimensions in isolation. We present a unified empirical study of Human-AI scientific ideation, investigating two complementary perspectives: i) how AI collaboration shapes scientific ideas and their evaluation, and ii) how firsthand collaboration reshapes human perc...
  </details>

- **2026-10-22** — Atiksh Bhardwaj, Edward W. Duan, Junwon Seo et al. — [Progress Probes $P^2$: Lightweight Runtime Monitoring for Vision-Language-Action Models](http://arxiv.org/abs/2610.31613v1)
  <details><summary>📄 Abstract</summary>
  Vision-Language-Action (VLA) models can perform diverse manipulation tasks directly from visual observations and natural language instructions, but they remain prone to mistakes and unpredictable failures. Deploying these policies without continuous human supervision will require robust runtime monitors that detect when the policy has gone off-course. Existing monitors use external foundation models, such as vision-language models (VLMs) to supervise the policy, introducing significant complexit...
  </details>

- **2026-10-22** — Khaled Waleed Dawoud, Muhammad Zaigham Zaheer, Khan Muhammad et al. — [MoG-VLM: Efficient Video Anomaly Detection through Motion-Guided Vision-Language Models](http://arxiv.org/abs/2610.31478v1)
  <details><summary>📄 Abstract</summary>
  Vision-Language Models (VLMs) have shown strong potential for video anomaly detection, but dense frame-level inference makes them impractical for real-time deployment. Existing acceleration commonly relies on uniform sampling, which ignores content dynamics and can either waste computation on static segments or miss localized anomalies. We propose MoG-VLM a motion-adaptive anomaly detection framework that leverages motion purely as a lightweight control signal to decide when VLM inference is nec...
  </details>

- **2026-10-22** — Tianming Liang, Junyi Pan, Yuxi Li et al. — [WeVisOne-VL: Unified Visual Perception from Objects to Pixels](http://arxiv.org/abs/2610.31329v1)
  <details><summary>📄 Abstract</summary>
  Existing vision-language models (VLMs) remain unreliable for fine-grained visual perception. In this report, we present WeVisOne-VL (WeChat Vision All-in-One), a powerful VLM that unifies object-level and pixel-level perception through structured next-token prediction. It supports multiple visual tasks including object detection, referring localization, counting, OCR, segmentation, and matting, enabling localization at any user-specific granularity, from points and boxes to masks and alpha matte...
  </details>

- **2026-10-22** — Xinyu Zhao, Qingyun Sun, Ziwei Zhang et al. — [One Pretrained Decision Model Is Enough for Training-Free Generalist Graph Anomaly Detection](http://arxiv.org/abs/2610.30777v1)
  <details><summary>📄 Abstract</summary>
  Graph anomaly detection (GAD) aims to identify irregular entities in graph-structured data, yet heterogeneous anomaly patterns and distributional differences across graphs challenge generalizable detection. Existing training-free approaches avoid task-specific optimization but primarily rely on predefined numerical scoring rules, leaving the semantic interpretation of heterogeneous anomaly evidence largely unexplored. In this paper, we propose Jev-GAD, a training-free generalist graph anomaly de...
  </details>

- **2026-10-21** — Edward C. Cheng, Jeshua Cheng, Alice Siu — [A Three-Pillar Governance Framework for Safe and Trustworthy AI Agents](http://arxiv.org/abs/2610.30445v1)
  <details><summary>📄 Abstract</summary>
  AI agents capable of autonomous decision-making introduce significant challenges related to safety, alignment, accountability, and human oversight. Existing Human-in-the-Loop (HITL) and responsible AI approaches provide important foundations, but many remain fragmented across system design, governance, and operational deployment. This paper presents a Three-Pillar (3P) model and framework for developing safe and trustworthy AI agents through transparency, accountability, and trustworthiness. The...
  </details>

- **2026-10-21** — Ido Levy, Segev Shlomov, Leshem Choshen — [Retrieval Augmented Generation Compositionality](http://arxiv.org/abs/2610.29722v1)
  <details><summary>📄 Abstract</summary>
  Retrieval Augmented Generation (RAG) grounds large language models in external knowledge. Modern pipelines combine embedding, chunking, retrieval, reranking, query augmentation, context compression, and agentic verification, yet these techniques are typically evaluated one at a time. It remains unclear whether their isolated gains survive composition, whether retrieval quality and answer faithfulness favor the same design choices, and whether conclusions from small corpora hold at large scale. W...
  </details>

- **2026-10-21** — Ge Qu, Jinyang Li, Xiaohan Xu et al. — [BIRD-RL: Scaling Agentic Reinforcement Learning over Stateful Data-Centric Environments](http://arxiv.org/abs/2610.29426v1)
  <details><summary>📄 Abstract</summary>
  While agentic reinforcement learning (RL) has emerged as a promising paradigm for training small language models (SLMs), existing frameworks are predominantly tool-centric and struggle with data-centric environments. Specifically, applying tool-centric frameworks to stateful tasks like SQL debugging introduces severe spatial inefficiencies since proper environment isolation typically requires a separate database container per rollout. Naively reusing databases without tracking evolving states ac...
  </details>

- **2026-10-21** — Zhangchi Hu, Zilong He, Yifan Zhao et al. — [RiO-DETRv2: Geometry-Aware Uncertainty Modeling Meets Real-Time Oriented Object Detection Transformer](http://arxiv.org/abs/2610.29159v1)
  <details><summary>📄 Abstract</summary>
  RiO-DETR is the first real-time end-to-end transformer for oriented object detection, yet further localization gains require a more expressive box representation. Although distributional regression has succeeded in horizontal DETRs, extending it to oriented detection introduces geometry-misaligned boundary modeling and topology-inconsistent orientation refinement. We present RiO-DETRv2, a geometry-aware uncertainty modeling framework for real-time oriented object detection. To resolve the geomet...
  </details>

- **2026-10-21** — Chao Shuai, Shaojing Fan, Kun Pan et al. — [Beyond Shortcut Learning: Hierarchical Spatial Prototype Regularization for Face Forgery Detection](http://arxiv.org/abs/2610.29442v1)
  <details><summary>📄 Abstract</summary>
  Recent advances in generative models have enabled highly realistic face forgeries, yet generalizing deepfake detectors to unseen manipulation pipelines remains a major challenge. One critical yet underexplored issue is that the learned forensic representation itself may fail to remain stable across different manipulation sources. In this paper, we provide new evidence that naively fine-tuned vision models suffer from severe \textit{forensic representation collapse}: their extracted cues are ofte...
  </details>

- **2026-10-21** — Austin Meek, Kyle Cox, Matthew Nguyen et al. — [Mitigating Reward Hacking in Realistic Scenarios Through Representation Engineering](http://arxiv.org/abs/2610.29129v1)
  <details><summary>📄 Abstract</summary>
  Reward hacking is a major problem in current production machine learning systems, resulting in costly and dangerous failures. Here we study how to monitor for and mitigate reward hacking in realistic settings, including tool calls and long contexts. We apply a dynamic intervention to steering directions obtained by three different methods: difference-in-means vectors from labeled rollouts, gradient optimization-based vectors, and vectors extracted when models reference an anti-reward-hacking mod...
  </details>

- **2026-10-21** — Ali Abedi, Q. M. Jonathan Wu, Ning Zhang et al. — [FogTTA: Online Test-Time Adaptation for Robust Transformer-based Object Detection in Foggy Weather](http://arxiv.org/abs/2610.29618v1)
  <details><summary>📄 Abstract</summary>
  Object detection models for autonomous driving commonly experience substantial performance drops when deployed under adverse weather due to the domain shift between training data and real-world operating conditions. This degradation is especially evident when models trained on clear-weather images encounter foggy environments with reduced visibility and contrast. To address this challenge, we introduce FogTTA, an online test-time adaptation framework designed to improve the robustness of Transfo...
  </details>

- **2026-10-21** — Asaduz Zaman, Mohaimenul Azam Khan Raiaan, Malika Nisal Ratnayake — [Computer Vision and Knowledge-Grounded Language Models for Intelligent Beekeeper Assistance](http://arxiv.org/abs/2610.29283v1)
  <details><summary>📄 Abstract</summary>
  Managed and wild bees sustain roughly a third of the global food products, yet colonies face mounting stress from climate-change including extreme weather patterns, altered parasite and disease patterns. Timely assessment of colony condition such as understanding colony strength, brood area, honey and pollen storage, comb usage, is essential to adaptive management. However, manual hive frame inspection is slow, costly, and quality depends on scarce expertise. We present an artificial targeted in...
  </details>

- **2026-10-21** — Dongchan Cho, Jiho Han, Juwon Hwang et al. — [Distilling Multi-Teacher Scoring Principles for Unsupervised Time Series Anomaly Detection](http://arxiv.org/abs/2610.29063v1)
  <details><summary>📄 Abstract</summary>
  Time series anomalies take diverse forms, and individual detectors encode different anomaly scoring principles that rarely cover all anomaly types. Recent unsupervised time-series anomaly detectors provide complementary scoring signals, yet deploying them as an ensemble preserves the inference and maintenance cost of every individual detector. We study whether heterogeneous teacher detectors can be distilled into a single lightweight detector in the unsupervised setting, where no anomaly labels ...
  </details>

- **2026-10-20** — Kaiwen Zhou, Udari Madhushani Sehwag — [RSI Control: Can AI Models Perform Covert Sabotage in the Self-Improvement Process?](http://arxiv.org/abs/2610.27735v2)
  <details><summary>📄 Abstract</summary>
  Recursive self-improvement, in which frontier AI models work on training the next generation, is quickly becoming a reality. However, the safety of this process has received far less attention than it should. A misaligned model training its successor can shape what that successor knows, how it behaves, and what it wants, and the harm carries forward into the next generation. We study this risk through the lens of AI control. We introduce RSI Control Arena, a testbed in which a frontier model, ac...
  </details>

- **2026-10-20** — Abbas Pirmoradi, Milad Momeni, Anna Chu et al. — [Scriptorium: System Design and Implementation of a Multi-Human, Multi-AI Collaborative Digital Library Search Platform](http://arxiv.org/abs/2610.28929v1)
  <details><summary>📄 Abstract</summary>
  This technical report documents the design and implementation of Scriptorium, a digital library search interface designed to support multi-human, multi-AI collaboration: full cross-user transparency of search activity combined with a Manager--Worker architecture of seven role-specialized generative AI agents. A companion short demonstration paper describes Scriptorium's interaction design; because a demonstration format is constrained to a few pages, it necessarily omits most implementation deta...
  </details>

- **2026-10-20** — Alan-Barsag Gazzaev, Alexey Gavrilov, Mikhail Mozikov et al. — [DiffResearch: Accelerating Deep Research with Diffusion Language Models](http://arxiv.org/abs/2610.28909v1)
  <details><summary>📄 Abstract</summary>
  Deep research systems iteratively plan, gather evidence, synthesize, and revise, making end-to-end latency a key bottleneck for interactive use. Almost all production systems are built on autoregressive (AR) language models and inherit left-to-right decoding in planning and long-form writing. We present DiffResearch, an open multi-agent deep research framework that places a diffusion language model (dLLM) at the core of every stage, and measure how a diffusion backbone changes latency and report...
  </details>

- **2026-10-20** — Habibur Rahaman, Swarup Bhunia — [LEAN: Loss-Engineered Modulation of the Model Weight-Sensitivity Distribution for Efficient, Error-Tolerant Neural Networks](http://arxiv.org/abs/2610.28872v1)
  <details><summary>📄 Abstract</summary>
  The weights of a trained network do not have uniform sensitivity to model accuracy: the 1% most sensitive weights carry about a fifth of the damage a bit flip can do. This distribution decides the bit-flip tolerance of a model, the fraction of weights a code must cover and the bits each weight needs; existing schemes work with the distribution training leaves. We show that we can systematically modulate or alter the weight sensitivity distribution of a trained model, thereby shifting weights fro...
  </details>

- **2026-10-20** — Masoud Jamshidiyan Tehrani, Jinhan Kim, Paolo Tonella — [PCLA-Bridge: A Framework for Cross-Domain Deployment of CARLA Agents](http://arxiv.org/abs/2610.28696v1)
  <details><summary>📄 Abstract</summary>
  Most high-performing end-to-end autonomous driving agents (ADAs) are developed for the CARLA Leaderboard, tightly coupling them to CARLA's APIs, sensor layouts, coordinate systems, and internal clock. Reusing these models on real datasets, alternative simulators, or physical platforms necessitates substantial manual re-engineering. We present PCLA-Bridge, a deployable tool that runs unmodified CARLA Leaderboard agents from any sensor source to any control destination without an active CARLA serv...
  </details>

- **2026-10-20** — Junwei Deng, Alex Bie, Natalia Ponomareva — [SimHack: Predicting the onset of detectable reward hacking before RL training](http://arxiv.org/abs/2610.28707v1)
  <details><summary>📄 Abstract</summary>
  When training LLMs to code with reinforcement learning, reward hacking is often detectable but difficult to prevent, since (a) environment hardening is increasingly difficult as training environments grow more complex; and (b) training-time interventions incentivize models to obfuscate hacking behavior to bypass detection.   We instead study whether we can predict when detectable reward hacking becomes dominant before executing an RL run, enabling us to select lower-risk recipes in advance. We f...
  </details>

- **2026-10-20** — Shakson Isaac, Chirag Patel — [SSMCGM-Stream: A Streaming State-Space Model for Personalized Diabetes Management](http://arxiv.org/abs/2610.28976v1)
  <details><summary>📄 Abstract</summary>
  Continuous glucose monitoring supports diabetes management but requires forecasting models that are accurate, interpretable, and efficient enough for real-time deployment. We present SSMCGM-Stream, a streaming state-space model that maintains a personalized hidden state updated with each incoming glucose reading to provide constant-time forecasting, physiologically structured counterfactual reasoning, and interpretable forecasts through hidden-state attribution. Built on this foundation, SSMCGM-...
  </details>

- **2026-10-20** — Chuanmeng Bian, Daren Chen, Peixin Chen et al. — [Qwen-Audio-3.1-ASR Technical Report](http://arxiv.org/abs/2610.28711v1)
  <details><summary>📄 Abstract</summary>
  We present Qwen-Audio-3.1-ASR, a family of audio-language models that builds upon its predecesor Qwen-Audio-3.0-ASR with improved speech recognition and expanded capabilities in speaker-diarized transcription and general audio understanding. The family retains support for 30 languages and 16 Chinese dialects, together with instruction-controlled capabilities including historical-context conditioning, hierarchical hotword customization, and native transcription polishing. Speaker-diarized ASR pro...
  </details>

- **2026-10-20** — Vlad Mihal, Hosam Alamleh, Alessandro Cantelli-Forti — [Make the Adversary Spend More Energy: Generative Deception against Language-Model Attackers in Critical Infrastructure](http://arxiv.org/abs/2610.27739v1)
  <details><summary>📄 Abstract</summary>
  Language-model attackers consume computational resources as they explore and interact with a target, creating an opportunity for cyber deception to impose costs. Whether such engagements favor the defender requires measuring both sides. We evaluate an autonomous language-model attacker against a decoy that uses a defending language model to analyze attacker commands and select defensive responses. Across 330 sessions, eight model pairs, two attacker profiles and three counter-injection levels, b...
  </details>

- **2026-10-20** — Kaiwen Zhou, Udari Madhushani Sehwag — [RSI Control: Can AI Models Perform Covert Sabotage in the Self-Improvement Process?](http://arxiv.org/abs/2610.27735v1)
  <details><summary>📄 Abstract</summary>
  Recursive self-improvement, in which frontier AI models work on training the next generation, is quickly becoming a reality. However, the safety of this process has received far less attention than it should. A misaligned model training its successor can shape what that successor knows, how it behaves, and what it wants, and the harm carries forward into the next generation. We study this risk through the lens of AI control. We introduce RSI Control Arena, a testbed in which a frontier model, ac...
  </details>

- **2026-10-20** — Jitendra Solanki, Anand Todkar, Ziran Min — [Semantic Observability for Autonomous Systems Diagnostics](http://arxiv.org/abs/2610.28611v1)
  <details><summary>📄 Abstract</summary>
  Modern distributed microservice deployments generate massive volumes of heterogeneous, multi-format observability logs across physically and logically partitioned infrastructure. Isolating root causes during cascading failures remains an arduous task for Site Reliability Engineers (SREs), bottlenecked by manual keyword filtering and disjointed temporal correlation across monitoring dashboards. We introduce Semantic Observability, an autonomous multi-agent framework that unifies disparate log str...
  </details>

- **2026-10-20** — Shangquan Sun, Wenjun Luo, Xu He et al. — [Agentic Ensemble with Vision-Language Models for Visual Anomaly Detection](http://arxiv.org/abs/2610.28560v1)
  <details><summary>📄 Abstract</summary>
  Visual anomaly detection aims to detect abnormal objects, while anomaly samples are often scarce during model training. Assembling multiple pretrained detectors can help by leveraging their transferable image scores and anomaly maps. However, most existing ensemble methods apply fixed fusion rules over saved predictions which struggle when pretrained detectors clearly disagree due to different training objectives, priors, and visual representations. To this end, we design AnomalyAgent, a post-tr...
  </details>

- **2026-10-20** — Xialie Zhuang, Mingcong Lei, Zunhai Su et al. — [DecisionPivot: A Diagnostic Benchmark for Decision Models in LLM Systems](http://arxiv.org/abs/2610.28522v1)
  <details><summary>📄 Abstract</summary>
  Decision models support routing, guardrails, and output verification in LLM systems. However, item accuracy alone cannot establish whether models make correct decisions across controlled variations or assign reliable confidence to their predictions. We introduce DecisionPivot, a diagnostic benchmark comprising 48 tasks and 40,033 items across seven decision roles. Its core track contains 7,800 items from 13 generated task families, organized into contrast groups with computed answers verified by...
  </details>


### 📂 alignment
*对齐与安全约束 / Alignment & Safety Constraints* — 51 papers

- **2026-10-22** — Yunfei Xie, Howard H. Qian, Shiyi Lan et al. — [Sensorimotor Alignment: A Platonic Proxy for Embodied Policy Success](http://arxiv.org/abs/2610.31670v1)
  <details><summary>📄 Abstract</summary>
  Robotic foundation models are typically evaluated through costly closed-loop rollouts, which motivates cheap offline proxies for model capability. The Platonic Representation Hypothesis (PRH) suggests that as representations improve, different modalities such as vision and language converge toward a shared statistical model of reality. We ask whether motion trajectories form another such modality: as embodied models become more capable, should their sensory representations converge toward the st...
  </details>

- **2026-10-22** — Andrea Giuseppe Di Francesco, Rishabh Jain, Franco Maria Nardini et al. — [On the Token Collapse Phenomenon in Textual Graph Soft Prompting](http://arxiv.org/abs/2610.31572v1)
  <details><summary>📄 Abstract</summary>
  Recent methods for injecting graph structure into LLM prompts include graph soft prompting, in which a graph neural network (GNN) learns graph-specific tokens that capture relational information among entities in textual prompts. G-Retriever combines graph soft prompts with a verbalized description of the same graph to strengthen the textual prompt signal. We conduct an in-depth analysis of G-Retriever and uncover a pathological behavior we term token collapse. Across three benchmarks, three gra...
  </details>

- **2026-10-22** — Ioannis Kouroudis, Zhaosu Gu,  Poonam et al. — [PYTHIA, a transferable machine learning framework for simultaneous defect and adsorption site optimization](http://arxiv.org/abs/2610.31539v1)
  <details><summary>📄 Abstract</summary>
  Machine learning has permeated material optimization, providing high value. Nevertheless, its re- liance on a high number of samples limits its applicability to relatively explored material families. In this paper we extend the applicability of machine learning to novel and understudied materials through the PYTHIA (Probabilistic Yet Transferable Hierarchical Interaction Architecture) framework. Pythia utilizes two of the most powerful machine learning concepts, foundational models and transfer ...
  </details>

- **2026-10-22** — Eun Sun Lee, Minkyun Seo, Gwangtak Bae et al. — [A Sparse Topometric Graph for Scalable Cross-Session Indoor Navigation](http://arxiv.org/abs/2610.31432v1)
  <details><summary>📄 Abstract</summary>
  A conventional embodied agent in an indoor environment builds a map by accumulating noisy real-world measurements and results from heavy inference to guide navigation. While the detailed measurements may differ due to scene changes or sensor settings, the unique topological structure of navigable passages or the connectivity between rooms may provide training-free guidance that complements local observations. We propose a sparse topometric graph as an efficient structural representation for robu...
  </details>

- **2026-10-22** — Yen-Ku Liu, Hongjie Chen, Franck Dernoncourt et al. — [DISC: Domain-Integrated Similarity Cost for Time-Series Dataset](http://arxiv.org/abs/2610.31288v1)
  <details><summary>📄 Abstract</summary>
  The growth of time-series datasets and foundation models has made dataset comparison a central part of time-series workflows. Assessing source-target transfer before model adaptation requires similarity estimates that can summarize transfer-related dataset relationships without exhaustive source-target evaluation over every candidate pair. Many metrics have been proposed for measuring similarity between time-series datasets, but they capture different dataset relationships and vary in how well t...
  </details>

- **2026-10-22** — Wei-Jaw Lee, Chun-Ping Wang, Xuanjun Chen et al. — [MQAScore: Fine-Grained Text-Music Alignment Evaluation via Large Audio Language Model](http://arxiv.org/abs/2610.31083v1)
  <details><summary>📄 Abstract</summary>
  Text-to-music alignment is commonly evaluated by the global similarity between text and audio embeddings, which collapses all described attributes into a single score and obscures which ones are missing. We instead introduce MQAScore, which verifies each atomic musical concept along five clip-level dimensions (genre, instrument, mood/theme, vocal, and usage) by the probability that a large audio language model (LALM) answers affirmatively to a binary question. To assess evaluator reliability, we...
  </details>

- **2026-10-22** — Qiuyu Kong, Zanxi Ruan, Marco Cristani et al. — [Mitigating Saliency Collapse: Robust Saliency-Aware Long-Text Image-Text Alignment](http://arxiv.org/abs/2610.31005v1)
  <details><summary>📄 Abstract</summary>
  Long-text image-text alignment is essential for fine-grained scene understanding, yet existing methods mainly focus on extending context length or improving local alignment. We identify an overlooked failure mode, saliency collapse, where models over-rely on text that features visual prominence while underutilizing non-salient context. Consequently, retrieval performance degrades sharply when salient content is reduced, despite that the non-salient context remains informative. To address this, w...
  </details>

- **2026-10-22** — Mohammad Talaei, Mohammad Goudarzi, Maille Todd et al. — [Zero-Shot Forecasting of In-Situ Soil Moisture and Temperature with a Time-Series Foundation Model](http://arxiv.org/abs/2610.30971v1)
  <details><summary>📄 Abstract</summary>
  Soil moisture and temperature govern plant-water availability and microbial activity, making them key indicators for evaluating land-restoration efforts on degraded landscapes. However, the physical and data-driven models normally used to forecast them both need information that a newly instrumented restoration site does not yet have: hydraulic parameters for the former and months of per-site training data for the latter. We evaluate TimesFM 1, a 500M-parameter time-series foundation model, zero...
  </details>

- **2026-10-22** — Pengfeng Song, Shaozhong Zhang, Pengfei Shao — [Hierarchical Fine-Grained Cross-Modal Alignment via Dynamic Granularity Discovery and Optimal Transport](http://arxiv.org/abs/2610.30912v1)
  <details><summary>📄 Abstract</summary>
  Fine-grained image-text retrieval requires a model not only to assess global semantic consistency between an image and a text, but also to model visual evidence for local textual semantics, including objects, attributes, quantities, actions, and relations, so as to distinguish semantically similar candidates. Existing methods commonly use fixed image patches, detected regions, or text tokens as the basic matching units and then aggregate local interactions through max pooling, cross attention, o...
  </details>

- **2026-10-22** — Dewei Wang, Jinrui Han, Jiyuan Shi et al. — [LocoManiLab: A Unified Testbed for Data, Policies, Controllers, and Deployment in Humanoid Loco-Manipulation](http://arxiv.org/abs/2610.30876v1)
  <details><summary>📄 Abstract</summary>
  Humanoid robots must coordinate locomotion and manipulation in everyday environments, yet progress is difficult to assess across differing policies, controllers, and task settings. LocoManiLab provides an integrated testbed spanning data collection and generation, policy training, evaluation, and physical deployment. Its task suite covers 234 atomic and compositional tasks across five household scene categories, supported by 51.5 hours of simulated teleoperation. The evaluation covers twelve pol...
  </details>

- **2026-10-22** — Ziang Lu, Yu Zhang, Xinzhe Jiang et al. — [Bezier-Guided Adaptive Flow for Cross-domain Sequential Recommendation](http://arxiv.org/abs/2610.30825v1)
  <details><summary>📄 Abstract</summary>
  Cross-domain sequential recommendation aims to alleviate data sparsity and cold-start problems by transferring useful preference knowledge across domains. However, users exhibit varying degrees of preference consistency across domains, while existing methods often rely on global alignment objectives or coarse-grained transfer strategies. Such approaches may introduce irrelevant information and provide limited flexibility in adapting semantic representations to individual user preferences. To add...
  </details>

- **2026-10-22** — Chalisa Veesommai Sillberga, Kai-Kristian Kemella, Pekka Sillberga et al. — [TESSA: A Governance-Oriented Custom GPT for SME Guidance under the EU AI Act: Design, Implementation, and Evaluation](http://arxiv.org/abs/2610.30822v1)
  <details><summary>📄 Abstract</summary>
  The increasing adoption of generative AI presents new opportunities while raising AI governance and regulatory challenges, particularly for small and medium-sized enterprises (SMEs) navigating the European Union Artificial Intelligence Act (EU AI Act). To support AI governance education, this study developed TESSA, a governance-oriented educational artifact within the OpenAI Custom GPT environment. Following a design science research approach, TESSA was evaluated against baseline ChatGPT using 1...
  </details>

- **2026-10-22** — Mijeong Kim, Suho Park, Junha Park et al. — [AgentDreamer: Agentic 3D Motion Reasoning for Text-Controllable Physics Simulation](http://arxiv.org/abs/2610.30679v1)
  <details><summary>📄 Abstract</summary>
  We propose AgentDreamer, an agent-guided optimization framework that aligns text instructions with simulated motion through explicit 3D motion planning. Given a text instruction and scene geometry, an off-the-shelf agent translates the instruction into a structured semantic motion prior, specifying what should move, in which direction, and in what temporal order. The agent represents this prior using parametric functions over a series of temporal chunks, yielding dense 3D trajectories. We then o...
  </details>

- **2026-10-22** — Hao Jiang, Peiru Du, Pengfei Yao et al. — [OneLatent: Latent Reasoning for Efficient Foundation Recommendation Models](http://arxiv.org/abs/2610.30675v1)
  <details><summary>📄 Abstract</summary>
  Large language models (LLMs) have demonstrated strong reasoning capabilities, motivating their use as the backbone of foundation recommendation models (FRMs). Existing methods enhance recommendations through explicit Chain-of-Thought (CoT) reasoning under a Think-then-Answer paradigm. However, explicit CoT incurs substantial inference overhead by generating lengthy reasoning traces and relies on manually designed templates that struggle to capture diverse, dynamic user interests. We propose OneL...
  </details>

- **2026-10-22** — Yanan He, Yanli Chen, Ling Xiong et al. — [Model-intrinsic, Weight-level, and Training-free Spectral Fingerprinting for Large Language Models](http://arxiv.org/abs/2610.30626v1)
  <details><summary>📄 Abstract</summary>
  The increasing release and reuse of Large Language Models (LLMs) as open-weight checkpoints make model fingerprinting important for ownership protection and offline auditing. Existing fingerprinting methods typically construct evidence from query responses, generated outputs, or input-induced activations. Although effective in representation-based settings, they can be affected by prompt selection, decoding configuration, inference environment, and forward-pass implementation, which may limit th...
  </details>

- **2026-10-22** — Minhyuk Seo, Minjae Lee, Chaeeun Lee et al. — [Visual Grounding First, Multimodal In-context Learning Follows](http://arxiv.org/abs/2610.30592v1)
  <details><summary>📄 Abstract</summary>
  LLMs have shown strong in-context learning (ICL) capability, but extending it to Multimodal LLMs (MLLMs) remains challenging. Prior multimodal ICL methods often rely on ICL-specific datasets for additional training or task vector extraction, which can improve performance on the same ICL benchmark used for adaptation. However, they do not generalize well to other benchmarks and often induce forgetting in previously well-solved tasks. For this reason, we identify 'visual grounding' as the key bott...
  </details>

- **2026-10-22** — Giovanni Romagnoli, Fabrizio Pilone, Giordana Bucchioni — [Consensus-Based Distributed Filtering for Angles-Only Tracking in Cislunar Space](http://arxiv.org/abs/2610.30864v1)
  <details><summary>📄 Abstract</summary>
  This paper investigates consensus-based distributed filtering strategies for multi-observer angles-only navigation in the cislunar space. The objective is to estimate the inertial state of a target spacecraft using only line-of-sight measurements collected by a network of observer spacecraft. This problem is particularly relevant for autonomous cislunar navigation, where ground support may be limited, and centralized fusion architectures may be problematic due to communication and computational ...
  </details>

- **2026-10-21** — Donato Meoli, Eryk Wdowiak — [Climbing the Ladder: Automating Data Pipelines and Reproducing Baselines in Low-Resource Settings](http://arxiv.org/abs/2610.30374v1)
  <details><summary>📄 Abstract</summary>
  The massively multilingual translation systems that now include Sicilian learned it from noisy, non-standardised web text. To obtain better translation quality, we redevelop the small neural machine translation (NMT) system that Wdowiak customized for Sicilian. We rebuild on maintained software the extraction of the parallel text from the PDFs of the bilingual journal Arba Sicula, whose sentences are aligned by a language-agnostic sentence encoder with thresholds tuned against an existing hand a...
  </details>

- **2026-10-21** — Chao-Yeh Chen, Tiffany Chen, Lin Duan et al. — [EgoHand: Monocular 3D Hand Reconstruction from Egocentric Video](http://arxiv.org/abs/2610.30293v1)
  <details><summary>📄 Abstract</summary>
  We introduce EgoHand, a monocular 3D hand reconstruction model that achieves state-of-the-art performance on egocentric video. Central to our approach is the curation of a high-quality training corpus of 14 million images, combining synthetic data, in-the-wild video, and multi-camera motion capture to balance scene diversity and supervision quality. The model adopts SOMA-Hand as its parametric representation and processes 2D hand crops with a transformer encoder, incorporating camera cues and an...
  </details>

- **2026-10-21** — Federico Marcuzzi, Martin Christoph, Iryna Gurevych et al. — [Investigating the Impact of Learner Errors on Social Bias in Large Language Models](http://arxiv.org/abs/2610.29896v2)
  <details><summary>📄 Abstract</summary>
  Existing social bias benchmarks evaluate large language models mostly on fluent, well-formed English, reflecting native speaker usage and leaving non-native writers unrepresented. To address this gap, we investigate how grammatical errors by non-native writers affect social bias. We develop a controlled framework that injects common learner errors into prompts and apply it to three bias benchmarks covering stereotype alignment and demographic preference across gender, race, and religion. We find...
  </details>

- **2026-10-21** — Kardelen Subasi, Jarosław A. Chudziak — [Conflicted Records: Typed Adversarial Contracts for Auditable LLM Output Quality Enforcement](http://arxiv.org/abs/2610.29669v1)
  <details><summary>📄 Abstract</summary>
  LLM-generated records increasingly populate production information systems where they are treated as data assets subject to the same quality expectations as records from operational databases. A single such record can simultaneously satisfy and violate a quality rule: a grounded fact adjacent to a hallucination, a useful answer adjacent to a stereotype. Classical data cleaning cannot resolve this because the two judgments are incompatible over the same span; a single LLM judge cannot either, sin...
  </details>

- **2026-10-21** — Zhichao Zhai, Menglei Zhao, Guikun Chen et al. — [VoxProg: 3D Spatial Reasoning through Voxel Programming](http://arxiv.org/abs/2610.30127v1)
  <details><summary>📄 Abstract</summary>
  Language models' abilities to interpret tasks and generate programs offer a promising basis for 3D spatial reasoning. Yet following spatial instructions in 3D scenes requires programs to construct geometric references that language leaves implicit. In this work, we introduce VoxProg, which formulates 3D object placement through voxel programming: a language model translates task interpretations into executable programs over local voxel views of scene surfaces. Because these views index surface g...
  </details>

- **2026-10-21** — Sudipta Paul, Pengrui Quan, Aounon Kumar et al. — [HGM-Dual: Lineage-Aware Guided Agent Harness Optimization for Long-Horizon Planning](http://arxiv.org/abs/2610.30042v1)
  <details><summary>📄 Abstract</summary>
  Harness optimization, which improves an agent's prompts, tools, and workflows, is an increasingly effective way to enhance agents built on frozen or closed-source LLMs. Leading approaches such as the Darwin--Godel Machine and the Huxley--Godel Machine (HGM) rely on recursive self-improvement and were developed mainly for coding, where the competence needed to improve the agent coincides with the competence being improved. Planning tasks, in which an agent must produce a sequence of tool calls th...
  </details>

- **2026-10-21** — Pradeep Kumar Yadav, Ignacio Pagonabarraga — [Clutter Noise Induced Phase Segregation in Binary Active Polar Flocks](http://arxiv.org/abs/2610.30008v1)
  <details><summary>📄 Abstract</summary>
  Macroscopic phase segregation in binary active mixtures can emerge solely from clutter noise: local, composition-dependent stochasticity, without repulsion or anti-alignment torques. Using an agent-based Vicsek model, we show that clutter noise alone destabilizes the mixed state, producing multi-stripe, co-moving band, and metastable counter-propagating morphologies, as well as a stable phase-segregated polar fluid. Our hydrodynamic theory shows that clutter noise suppresses local polar order an...
  </details>

- **2026-10-21** — Shu-Fan Chen, J. Colin Hill, Zoltán Haiman — [Constraining Dynamical Dark Energy with Tomographic Galaxy and CMB Weak Lensing Through Higher-Order Statistics](http://arxiv.org/abs/2610.29937v1)
  <details><summary>📄 Abstract</summary>
  Tomographic weak gravitational lensing probes cosmic structure growth and geometry, making it a powerful probe of dynamical dark energy. We forecast information beyond the lensing power spectrum from non-Gaussian statistics of tomographic galaxy and CMB lensing convergence maps. Using the $\texttt{DDELenS}$ suite of ray-traced $N$-body simulations, we build Gaussian process emulators for power spectra, Minkowski functionals, moments, peak and minima counts, and the wavelet scattering transform, ...
  </details>

- **2026-10-21** — Siddhesh Pawar, Chen Cecilia Liu, Anna Korhonen et al. — [Unintended Side Effects of Value Training in LLMs](http://arxiv.org/abs/2610.29922v1)
  <details><summary>📄 Abstract</summary>
  As LLMs are increasingly deployed in value-sensitive contexts, aligning them with human values has emerged as a post-training objective in NLP, aimed at instilling additional values and guiding model behaviour. However, current evaluations remain narrow. Because values are interconnected, it is unclear how fine-tuning for specific values alters unrelated capabilities and behaviours. In this work, we adapt four instruction-tuned LLMs across individual Hofstede's value dimensions and evaluate them...
  </details>

- **2026-10-21** — Kai Zhu, Yintianrun Zhang, Shuwei Jiang et al. — [CausalAlign: Causal Alignment of Video Generation Models for Consistent Ego-Motion](http://arxiv.org/abs/2610.29915v1)
  <details><summary>📄 Abstract</summary>
  Diffusion-based video generation models (VGMs) can produce visually plausible videos, yet their camera ego-motion often drifts over long horizons. Camera ego-motion determines how the viewpoint changes between frames and is essential for maintaining consistent geometry and trajectories. To address this problem, we propose CausalAlign, a causal alignment framework with two components. First, we diagnose how precise ego motion is represented, used, and retained within VGMs using linear probes and ...
  </details>

- **2026-10-21** — Federico Marcuzzi, Martin Christoph, Iryna Gurevych et al. — [Investigating the Impact of Learner Errors on Social Bias in Large Language Models](http://arxiv.org/abs/2610.29896v1)
  <details><summary>📄 Abstract</summary>
  Existing social bias benchmarks evaluate large language models mostly on fluent, well-formed English, reflecting native speaker usage and leaving non-native writers unrepresented. To address this gap, we investigate how grammatical errors by non-native writers affect social bias. We develop a controlled framework that injects common learner errors into prompts and apply it to three bias benchmarks covering stereotype alignment and demographic preference across gender, race, and religion. We find...
  </details>

- **2026-10-21** — DM BAPPY, Eunsu Kim, Hanjoo Lee et al. — [Expandable Modality Experts for Medical Vision-Language Learning](http://arxiv.org/abs/2610.29881v1)
  <details><summary>📄 Abstract</summary>
  Learning across medical imaging modalities requires making use of images without paired text and accommodating new domains while retaining existing representations. We propose a medical vision-language technique built around an expandable bank of modality experts. Its Multiway Transformer combines shared visual computation with deterministically routed feed-forward experts and a separate text pathway. A modality-aware visual tokenizer supplies targets for masked pretraining on 19.4 million unpai...
  </details>

- **2026-10-21** — Akihiro Fujii, Yuki Okamoto, Yuki Saito et al. — [AT-Differ: Dataset for Audio-Text Difference Captioning](http://arxiv.org/abs/2610.29836v1)
  <details><summary>📄 Abstract</summary>
  Evaluating audio-text semantic alignment is important in various audio-language tasks. Existing methods mainly quantify audio-text semantic alignment using a single score and cannot explicitly describe how audio and text differ. In this paper, we propose audio-text difference captioning, a task that generates textual descriptions of differences between audio and text. We also construct a new dataset AT-DIFFER containing audio-text pairs with systematically simulated differences and corresponding...
  </details>

- **2026-10-21** — Boqi Chen, Aren A. Babikian, José Antonio Hernández López — [Metamodel-Guided LLM Decoding for Consistent DSL Generation](http://arxiv.org/abs/2610.29749v1)
  <details><summary>📄 Abstract</summary>
  Large language models (LLMs) are increasingly used to generate software engineering artifacts written in domain-specific languages (DSLs). Correct DSL instances usually must comply with not only the concrete syntax but also the abstract syntax defined by a metamodel augmented with semantic well-formedness constraints. Existing constrained decoding approaches typically guarantee compliance only with concrete syntax or with a limited set of semantic constraints expressed over the generated text, m...
  </details>

- **2026-10-21** — Ilker Kesen, Jenny Kunz, Kasra Malihi et al. — [Scaling Multilingual Pretraining of Pixel Language Models](http://arxiv.org/abs/2610.29681v1)
  <details><summary>📄 Abstract</summary>
  Pixel language models process text as rendered images instead of a finite vocabulary, which gives them strong cross-lingual transfer abilities. However, not much is known about how these abilities are influenced by larger-scale pretraining. In this paper, we train a family of MPIXEL models along three axes of variation: more languages, more scripts, and larger model capacity under fixed per-language compute. In evaluations on five tasks covering 83 languages, we find that scaling acts locally: e...
  </details>

- **2026-10-21** — Simone Ricci, Niccolò Biondi, Federico Pernici et al. — [Hyperspherical Simplex Representations for Backward-Compatible Retrieval](http://arxiv.org/abs/2610.29550v1)
  <details><summary>📄 Abstract</summary>
  Training modern AI models has become increasingly expensive, and updating deployed models can alter their internal feature representations, affecting applications built upon them. In retrieval systems, such updates often require complete gallery re-indexing, a computationally expensive process at scale. Existing backward-compatibility methods enable direct comparison of representations from updated and earlier models, avoiding re-indexing. However, they typically require compatibility-specific t...
  </details>

- **2026-10-21** — Razieh Rezaei, Ehsaneddin Asgary, Masoud Jalili Sabet — [Melange: A Synthetic Visual Bias Benchmark for Multi-modal Large Language Models](http://arxiv.org/abs/2610.29537v1)
  <details><summary>📄 Abstract</summary>
  Multi-modal Large Language Models (MLLMs) have seen broad adoption, but their biases are still far less examined than those of standard LLMs, creating possible social harms when deployed in real-world settings. Prior efforts to extend bias analyses from LLMs into the multi-modal space either cover only a few bias categories or do not ensure that the groups being compared are clearly addressed by visual cues in the images. To overcome these limitations, we introduce Melange, a wide-ranging synthe...
  </details>

- **2026-10-21** — Shaojin Ma, Ruitao Wang, Pengyi Li et al. — [One Act, Many Masks: Effect-Marginal Policy Optimization for Long-Horizon Agents](http://arxiv.org/abs/2610.29427v1)
  <details><summary>📄 Abstract</summary>
  Recent advances in multi-turn reinforcement learning (RL) have substantially improved the performance of LLM agents on complex, long-horizon interactive tasks. However, despite progress in fine-grained credit assignment, policy optimization still applies these learning signals through response-specific probability ratios. Different textual responses can induce the same executable effect, yet credit differences arising from subsequent outcomes remain tied to their individual textual realizations....
  </details>

- **2026-10-21** — Yuan Xu, Yixiang Chen, Qisen Ma et al. — [Relational Geometry Forcing for World Action Models](http://arxiv.org/abs/2610.29282v1)
  <details><summary>📄 Abstract</summary>
  World Action Models (WAMs) have shown strong potential for robot manipulation by jointly learning visual dynamics and executable actions. However, their video and action objectives do not explicitly constrain the 3D geometry that is crucial for precise manipulation. Recently, geometry-aware WAMs introduce depth or 4D prediction branches, whereas representation alignment methods supervise intermediate WAM features with pretrained 3D foundation models. Yet we find that such pointwise alignment ben...
  </details>

- **2026-10-21** — Yiqing Yuan, Zhi Li, Jinrong Yang et al. — [Learning to Absorb Corrections: Critic-Weighted Residual Flow for Vision-Based Insertion](http://arxiv.org/abs/2610.29117v1)
  <details><summary>📄 Abstract</summary>
  Vision-based insertion requires correcting alignment errors while retaining useful behavior learned from demonstrations. We present ACT--Flow, an online learning framework that couples an adaptive Action Chunking Transformer (ACT) with a conditional residual flow policy. Following anchor-guided warmup, ACT absorbs successful executed actions through behavioral cloning, while residual targets are recomputed relative to the updated prior. A chunk-level critic learns from successful and failed inte...
  </details>

- **2026-10-21** — Ibrahim Khan, Thai Van Nguyen, Yi Xia et al. — [A Large-Scale Evaluation of Role-Enhanced Zero-Shot Chain-of-Thought Prompting](http://arxiv.org/abs/2610.29073v1)
  <details><summary>📄 Abstract</summary>
  This paper proposes Role-Enhanced Zero-Shot Chain-of-Thought (RE-ZS-CoT), a prompting framework that systematically integrates domain-specific expert roles to enhance reasoning in large language models (LLMs) without task-specific examples. We assess two versions of our approach. In the first version, static role selection, we evaluate eight predefined expert roles across arithmetic, commonsense, and reading comprehension benchmarks to determine their impact on reasoning performance. In the seco...
  </details>

- **2026-10-21** — Kun Liu, Keith Mitchell, Xin Hu et al. — [Beyond Tokens: NumAnchor for Address-Grounded Numeric Operand Representation in Assembly Language Models](http://arxiv.org/abs/2610.29027v1)
  <details><summary>📄 Abstract</summary>
  Assembly language models (ALMs) are becoming important for automated binary analysis, yet their token-level interfaces often obscure numeric-like operands. In two corpora, such operands account for 45.7% and 40.9% of operand occurrences and may denote branch targets, global data, stack slots, constants, or unresolved pointer-derived values. Existing normalization strategies often lose their identities and structural relationships. We present NumAnchor, an input-boundary adapter that represents r...
  </details>

- **2026-10-21** — Simran Khanuja, Rohit Gandikota, Gaurav Parmar et al. — [T-DIG: Text-Conditioned Diversity for Image Generation](http://arxiv.org/abs/2610.29003v1)
  <details><summary>📄 Abstract</summary>
  Text-to-image (T2I) platforms typically return several images per prompt so users can explore different visual interpretations and choose one that matches their intent. However, T2I models are usually optimized for single-image quality which comes at a cost of multi-image diversity, limiting this exploration. Diversity is also contextual: one user wants variations in background, while another wants them in artistic style, and the same user may later want variations in clothing. The generated ima...
  </details>

- **2026-10-20** — Weizhe Xu, Jialiang Fan, Essien Taylor et al. — [SLoSa: Small, Low-Power, and Safe Foundation Models for Robotic Task Planning](http://arxiv.org/abs/2610.28955v1)
  <details><summary>📄 Abstract</summary>
  Safe robotic task planning requires planners that can reliably achieve task goals while satisfying safety constraints. Classical planners search over explicit symbolic task representations and can provide formal guarantees with respect to encoded safety constraints, but require rigid input formats. Their computational cost also increases rapidly with the search space. In contrast, large language models (LLMs) offer flexible task interfaces and strong generalization capabilities, but they are lar...
  </details>

- **2026-10-20** — Mingyu Yang, Sharath Turuvekere Sreenivas, Adithyakrishna Venkatesh Hanasoge et al. — [CSD: Common-Support Distillation for Cross-Tokenizer Knowledge Transfer](http://arxiv.org/abs/2610.28895v1)
  <details><summary>📄 Abstract</summary>
  Cross-tokenizer logits distillation enables knowledge transfer across model families, allowing students to learn from stronger or more specialized teachers. However, differences in vocabulary and segmentation make teacher and student next-token distributions difficult to align. Existing logits-based methods are easy to integrate into standard distillation pipelines, but often rely on restrictive heuristics or tokenizer-pair-specific choices. They may restrict supervision to shared vocabulary sub...
  </details>

- **2026-10-20** — Ethan Ludwick, Yu-Chung Hsiao — [SANE: Automated Scorer-Specific Metamorphic Testing for LLM Judges](http://arxiv.org/abs/2610.28886v1)
  <details><summary>📄 Abstract</summary>
  LLM judges increasingly mediate benchmark evaluation, model selection, data curation, and training. Their decisions are useful only when each judge responds reliably to changes affecting its scoring criterion. Existing methods for reliability testing perturb inputs with known expected effects on judge scores. Prominent LLM-judge testing harnesses combine human-authored perturbation recipes with synthetic test generation, leaving scorer-specific recipe ideation outside the automated pipeline. Thi...
  </details>

- **2026-10-20** — Eran Goldstein, Yuval Belfer, Yonatan Belinkov et al. — [LIFT: Scoped Constraints for Evaluating and Training Instruction Following](http://arxiv.org/abs/2610.28819v1)
  <details><summary>📄 Abstract</summary>
  Common instruction following (IF) benchmarks, such as IFEval, evaluate the ability of language models (LMs) to follow simple constraints that can easily be verified programmatically. These same constraints, in turn, are used as reward signals for reinforcement learning. This design may lead to reward hacking of constraints, pushing models away from the main task. Recent attempts to address this resulted in benchmarks with richer constraints, but required expert labor, remained closed-access, and...
  </details>

- **2026-10-20** — Shixuan Liu, Cheng Tang, Yuzheng Hu et al. — [RL-IF: Tracking Non-local Training Data Influence for Online Reinforcement Learning](http://arxiv.org/abs/2610.28883v1)
  <details><summary>📄 Abstract</summary>
  Online reinforcement learning (RL) has achieved significant success in decision-making tasks, but modern online RL remains highly sensitive to the quality of training experience. Understanding the contribution of individual training instances is therefore central to data-centric RL, with applications ranging from experience selection to policy interpretation. Existing data attribution methods for online RL primarily focus on local influence within a single training round, overlooking the non-loc...
  </details>

- **2026-10-20** — Michal Podstawski — [Big Claims, Small Margins: Do Reported GraphLLM Gains Survive Simple Baselines?](http://arxiv.org/abs/2610.28714v1)
  <details><summary>📄 Abstract</summary>
  LLM-based methods for node classification on text-attributed graphs (TAGs) routinely report state-of-the-art accuracy. We ask how these results compare with inexpensive baselines run on the same splits. On the splits of three recent studies, we tune four baseline representatives with validation-only selection and compare them with the highest mean that each paper reports for an LLM-based method in the matched setting. Correct & Smooth on TF-IDF features trails this reference by a median of 2.3 p...
  </details>

- **2026-10-20** — Chengtao Jian, Kai Yang — [TPO: Tri-level Distributionally Robust Learning for OOD Direct Preference Optimization](http://arxiv.org/abs/2610.28229v1)
  <details><summary>📄 Abstract</summary>
  Direct Preference Optimization (DPO) minimizes empirical risk over observed preference comparisons, implicitly assuming that the training preference distribution matches the deployment preference distribution. In practice, this i.i.d. assumption often fails, as preference distribution shift exhibits a natural hierarchical structure across three levels: group-level shift, prompt-level shift, and preference-level shift. Such multi-level distributional mismatch poses a critical challenge for safe L...
  </details>

- **2026-10-20** — Siyuan Li, Jiayi Zhou, Zhiyuan Xia et al. — [A Neuro-Symbolic Reasoning Engine for Compilation-Free Patch Presence Testing](http://arxiv.org/abs/2610.27871v1)
  <details><summary>📄 Abstract</summary>
  Code reuse in modern software ecosystems facilitates the spread of 1-day vulnerabilities, posing significant security risks. Determining if patches are present is crucial, but traditional methods suffer from limited usability and accuracy, often depending on a fragile compilation process. In our prior work, we introduced Lares, the first compilation-free framework for patch presence testing that combines large language models (LLMs) with SMT solvers. However, Lares treats the LLM and the SMT sol...
  </details>

- **2026-10-20** — Liping Yang, Yongqi Leng, Jingting Zheng et al. — [ABench: Adversarily Benchmarking Large Language Models across Taxonomized Values](http://arxiv.org/abs/2610.27611v1)
  <details><summary>📄 Abstract</summary>
  Ensuring the alignment of Large Language Models (LLMs) with diverse cultural values is critical for their safe global deployment. However, existing alignment benchmarks are predominantly English-centric or confined to simple discriminative tasks. Moreover, they often fail to effectively evaluate model robustness against complex, adversarial inductions within specific cultural contexts. To address these limitations, we propose ABench, a fine-grained, handcrafted benchmark specifically tailored to...
  </details>

- **2026-10-20** — Bingqi Shang, Yang Zhang, Yiwei Chen et al. — [Can Native Safety Travel? Reusing Safety Pretraining Across Models via On-Policy Distillation](http://arxiv.org/abs/2610.27555v1)
  <details><summary>📄 Abstract</summary>
  Safety pretraining has emerged as a promising paradigm for embedding safety deeply into a model during pretraining, yielding robustness to subsequent fine-tuning that conventional safety post-training often lacks. We refer to this safety acquired during model pretraining as native safety. Yet native safety is expensive to acquire, confined to the model in which it was pretrained, and often accompanied by lower general utility. In this work, we rethink the practical value of safety-pretrained mod...
  </details>

- **2026-10-20** — Maoyuan Li, Haoyuan Li, Zhongsheng Wang et al. — [Value-Rich, Differently Organized: Measuring Value Expression and Organization in AI-Generated Debates](http://arxiv.org/abs/2610.28604v1)
  <details><summary>📄 Abstract</summary>
  Current evaluation of LLM-generated debate largely focuses on argumentative quality, leaving the value structure of generated arguments underexamined. We introduce a diagnostic metric framework for comparing how values are expressed and organized in human-reference and AI-generated debates. The framework separates value expression, the range of recognizable values a debate invokes, from value organization, how those values are distributed and sustained across turns. Grounded in Schwartz's Basic-...
  </details>


### 📂 robustness
*鲁棒性与可靠性 / Robustness & Reliability* — 67 papers

- **2026-10-22** — Sy-Tuyen Ho, Anirudh Satheesh, Soham Chawathe et al. — [SpectralCanary: Embarrassingly Simple Low-Frequency Traces for T2I Dataset-Use Auditing](http://arxiv.org/abs/2610.31659v1)
  <details><summary>📄 Abstract</summary>
  Auditing whether a text-to-image (T2I) model was fine-tuned on a particular image collection is difficult: a model can absorb collection-level visual characteristics without reproducing training images. Proactive dataset-use auditing plants a shared signal in a dataset before release, then later checks whether that signal appears in a suspect model's generated outputs. Existing approaches often trade off verifiability, fidelity, robustness, and deployability. We introduce $\textbf{SpectralCanary...
  </details>

- **2026-10-22** — Mingjie Li, Yukun Jiang, Yicong Tan et al. — [WildFakeToolBench: Benchmarking AI-Generated Image Detectors with Web-Sourced Image Processing](http://arxiv.org/abs/2610.31152v1)
  <details><summary>📄 Abstract</summary>
  As AI generated images are getting popular these days, discussions on such generations are widely existed in current public forums, software repositories, and photography tutorials. Moreover, with the help of LLM-assisted code translation, malicious actors can adopt such information to evade detectors without specialized knowledge or local GPU execution of the resulting tools. To evaluate such risks, we introduce \textsc{WildFakeToolBench}, a benchmark suite of $156$ executable image-processing ...
  </details>

- **2026-10-22** — Qijin Zhang, Hanzhen Wang, Yuehan Zhao et al. — [EpiSEM-Bench: Evaluating Safety and Evidence Recovery in LLM Agents under Missing Evidence](http://arxiv.org/abs/2610.31650v1)
  <details><summary>📄 Abstract</summary>
  Tool-using language model agents rely on environmental facts to decide whether an action is permitted. When a tool response omits a safety-relevant fact, an agent may carry out a prohibited action even though the user request is benign and every returned statement is true. We introduce \bench{}, an executable benchmark for evaluating unsafe execution, safety boundaries, and evidence recovery in LLM agents under missing evidence. It contains 300 matched unsafe/safe task pairs across six domains. ...
  </details>

- **2026-10-22** — Deepthika S, Pawni Yadav, B. Sankar — [Who Is Sycophantic to Whom? Confident LLMs, Human Deference, and the Collapse of Trust Calibration](http://arxiv.org/abs/2610.31579v1)
  <details><summary>📄 Abstract</summary>
  Research on sycophancy asks whether large language models (LLMs) bend towards what their users want to hear. We ask the reverse question: when an LLM is confident, consistent, and wrong, do users bend towards it? In a within-subjects experiment, 32 participants learned up to five science topics by chatting with five assistants built on the same model (GPT-5-mini). Unknown to participants, each assistant's briefing had 0, 25, 50, 75, or 100% of its facts replaced by plausible falsehoods, and ever...
  </details>

- **2026-10-22** — Raffaele Cali, Giuseppe Lando, Rosario Forte et al. — [Retrieval-Augmented Online Textual Memory for Episodic Memory Video Question Answering](http://arxiv.org/abs/2610.31284v1)
  <details><summary>📄 Abstract</summary>
  Long egocentric videos pose a central challenge for multimodal language models: the visual stream must be compressed into a memory representation that can be searched efficiently while still preserving the evidence needed for question answering. Building on an online textual-memory framework in which first-person videos are converted into temporally grounded captions, this work systematically studies the role of retrieval in episodic-memory video question answering. We evaluate how different ret...
  </details>

- **2026-10-22** — Tobias Wech — [LieGROG: A Lie algebra approach for calibrating GRAPPA operators](http://arxiv.org/abs/2610.30927v1)
  <details><summary>📄 Abstract</summary>
  Purpose: In multi-coil acquisitions based on non-Cartesian k-space sampling, image reconstruction using GRAPPA Operator based gridding (GROG) can provide advantages with respect to the non-uniform FFT (NUFFT): It waives both the need for calculating a density compensation function, and for transferring back and forth between Cartesian and non-Cartesian points in iterative algorithms. Non-trivial noise propagation and self-calibration limited to specific trajectories, however, have contributed to...
  </details>

- **2026-10-22** — Jihwan Kim, Jaeseong Heo, Yujin Kim et al. — [Wavenumber-Aware Deep Learning for Robust Analysis of Raman Spectra](http://arxiv.org/abs/2610.30746v1)
  <details><summary>📄 Abstract</summary>
  Machine-learning models for spectroscopy usually treat a spectrum as a fixed-grid intensity vector, leaving the physical coordinate implicit in the array index. Such models are tied to a single sampling grid, spectral range and resolution, which limits their use when measurement conditions change. Here we represent each spectral point as a pair of intensity and wavenumber and compute Transformer positional encodings from the wavenumber itself. On Raman spectra of three bacterial species and thei...
  </details>

- **2026-10-22** — Amirhossein Aghaei, Liangyan Li, Shiyi Yang et al. — [Better Reasoning, Not Just Bigger Models: A Structure-Grounded Framework for Efficient and Reliable Inference](http://arxiv.org/abs/2610.30611v1)
  <details><summary>📄 Abstract</summary>
  Scaling large language models has substantially improved linguistic fluency, yet reliable autonomous agents require more than fluent generation. In multi-turn inference, current agentic systems often produce semantically plausible but structurally ungrounded reasoning, especially under incomplete observations. We propose Structure-Grounded Uncertainty Reduction (SGUR), a training-free framework that complements token-level generation with active uncertainty reduction over structured hypothesis s...
  </details>

- **2026-10-22** — Jinyu Zhang, Haitao Lin, Jiashu Hou et al. — [F2G-Pose: Geometry-Aware Foundation Feature Lifting for Direct RGB-D Category-Level Object Pose Estimation](http://arxiv.org/abs/2610.31623v1)
  <details><summary>📄 Abstract</summary>
  This paper studies category-level RGB-D object pose estimation, which recovers an object's 3D rotation and translation without instance-specific CAD models or reference views. This task is highly ambiguous due to intra-class variations, symmetries, and partial observations. Current solutions struggle to balance reliability and efficiency: methods based on intermediate structures are prone to error propagation, while diffusion models suffer from high inference latency and complex post-hoc candida...
  </details>

- **2026-10-22** — Hengyi Sim, Quentin Rouxel, Dennis Hong et al. — [In-Context Learning World Models for Robot Dual-Arm Manipulation of Soft Garment with Partial Observations](http://arxiv.org/abs/2610.30988v1)
  <details><summary>📄 Abstract</summary>
  Robust manipulation of soft objects, such as garments, is a critical skill for service and household robots to adopt, but remains challenging due to its high-dimensional state space, and material-dependent deformations. Humans address this challenge by using mental world models that "imagine" the shape and material properties from partial observations, which enables them to predict how actions affect future states. As such, embedding such world models in robots allows for better generalization i...
  </details>

- **2026-10-22** — Zunnan Xu, Shangchen Zhou, Yihang Luo et al. — [HiP3R: Hierarchical Pose Graphs for Long-Horizon 3D Reconstruction](http://arxiv.org/abs/2610.31635v1)
  <details><summary>📄 Abstract</summary>
  Feed-forward models accurately estimate camera motion and 3D geometry from short video windows. However, computational and memory costs prevent direct inference on sequences containing thousands of frames. Long videos must therefore be processed as overlapping chunks. This division produces independent local reconstructions with inconsistent coordinate frames and duplicate estimates of shared cameras. Achieving global consistency requires propagating constraints from adjacent overlaps and distan...
  </details>

- **2026-10-22** — Molly Wolfson, Joseph F. Hennawi, Frederick B. Davies et al. — [A Robust Estimator for the Lyman-$α$ Forest 1D Power Spectrum at High Redshift](http://arxiv.org/abs/2610.31626v1)
  <details><summary>📄 Abstract</summary>
  The Lyman-$α$ (Ly$α$) forest flux power spectrum $P(k)$ is sensitive to a range of astrophysical and cosmological effects, including the thermal state of and large-scale fluctuations in the intergalactic medium and the nature of dark matter. Measuring $P(k)$ becomes increasingly challenging at high redshift, where fewer quasar spectra are available and higher Ly$α$ optical depths result in lower transmitted flux. In addition, observational effects and missing data complicate standard Fourier-tra...
  </details>

- **2026-10-22** — Chaoyue Li, Zeyu Gao, Yanfeng Lu et al. — [SCOPE: Scene-graph Construction Optimized by Plan Error-correction for Robot Long-term Planning Datasets](http://arxiv.org/abs/2610.31518v1)
  <details><summary>📄 Abstract</summary>
  Task and Motion Planning (TAMP) stands as a fundamental challenge in robotics, essential for enabling autonomous agents to execute complex, long-horizon tasks in diverse environments. While Large Language Models (LLMs) introduce a new paradigm for TAMP by leveraging extensive common sense, their inherent reasoning limitations hinder direct application, and fine-tuning strategies to enhance these capabilities are currently bottlenecked by the scarcity of high-quality datasets. Existing automated ...
  </details>

- **2026-10-22** — Dingxuan Zhang, Yanhui Jiang, Jun Wang et al. — [Adaptive Skill Granularity for Coding Agents: Runtime Routing and Macro-to-Micro Recovery](http://arxiv.org/abs/2610.31461v1)
  <details><summary>📄 Abstract</summary>
  Reusable skills allow large language model agents to package task-specific procedures, tool affordances, and execution guidance into modular units. Prior work has largely studied how agents retrieve, compose, or synthesize skills before execution. In coding agents, however, execution poses an additional runtime control problem: the same task may be solved through primitive tool calls, macro skills, or hybrid execution that starts with a macro and falls back to micro-level recovery. We introduce ...
  </details>

- **2026-10-22** — Ehsan Saleh, Roozbeh Nahavandi, Sama Salarian et al. — [AfterDeleteBench: Auditing Post-Deletion Information Persistence in LLM Agents](http://arxiv.org/abs/2610.31366v1)
  <details><summary>📄 Abstract</summary>
  Many LLM agents maintain external persistent memory and derive additional state from past interactions, such as summaries. Deleting an original memory record therefore need not remove information carried by its descendants. We introduce AfterDeleteBench, a controlled behavioral audit for this failure mode in fixed-weight LLM agents. For each synthetic secret, we compare an exposed-then-deleted agent with an otherwise matched agent that was never exposed to the secret, allowing post-deletion reco...
  </details>

- **2026-10-22** — Wei Zhang, Ying Feng, Mengtong Wu et al. — [Stream4D: Streaming 4D Reconstruction with Training-free Motion Decoupling via Causal KV-Cache Attention](http://arxiv.org/abs/2610.31320v1)
  <details><summary>📄 Abstract</summary>
  4D scene reconstruction requires robust handling of dynamic objects, yet existing streaming methods commonly assume static scenes, leading to pose drift and ghosting artifacts over long sequences. We introduce Stream4D, a training-free, motion-decoupled streaming reconstruction framework that can be directly integrated into causal Transformer backbones (e.g., StreamVGGT, Stream3R). Our key observation is that causal attention implicitly encodes rich temporal motion cues within the KV cache. We a...
  </details>

- **2026-10-22** — Fabian Isensee, Constantin Ulrich Harsy, Maximilian Rokuss et al. — [nnInteractive Agent: General-Purpose AI Agents as 3D Image Annotators](http://arxiv.org/abs/2610.31080v1)
  <details><summary>📄 Abstract</summary>
  Interactive 3D segmentation models such as nnInteractive turn a few spatial prompts (points, scribbles, boxes) into accurate volumetric masks, but a human still does the annotation work: finding each structure, placing prompts, checking the result and correcting it. General-purpose AI agents can now interpret images, call tools and write code. We show that such agents can take over this work without additional training: the user makes a request in plain language, and the agent works out what has...
  </details>

- **2026-10-22** — Diana Nunes, Ricardo Amorim, Pedro Ribeiro et al. — [AERIAL: Mission-Aware LLM Selection for Language-Driven UAV Control in Flying Networks](http://arxiv.org/abs/2610.31029v1)
  <details><summary>📄 Abstract</summary>
  Unmanned Aerial Vehicles (UAVs) in Flying Networks (FNs) increasingly require mechanisms to translate high-level natural language objectives into executable missions. Although Large Language Models (LLMs) have demonstrated the feasibility of language-driven UAV control, existing approaches typically rely on static model configurations and overlook mission-aware performance variability. This paper presents AERIAL, a benchmark-driven framework for adaptive LLM selection in hybrid edge-cloud UAV co...
  </details>

- **2026-10-22** — Zhaolu Kang, Yidi Wang, Yile Li et al. — [TRIAD: Benchmarking Omni-Modal Ambiguity in Multimodal Large Language Models](http://arxiv.org/abs/2610.30841v1)
  <details><summary>📄 Abstract</summary>
  Ambiguity is a central feature of natural communication: a sentence, image, or sound may remain underspecified until evidence from the other channels is considered. Yet current multimodal benchmarks mostly test perception, recognition, or reasoning over already determinate inputs, leaving unclear whether omni-modal large language models can resolve ambiguity distributed across text, vision, and audio. We introduce TRIAD, a benchmark for omni-modal ambiguity resolution. Each item is a text--image...
  </details>

- **2026-10-22** — Zhaolu Kang, Tailong Luo, Chenxin Li et al. — [RECAP: Looking Once Is Not Enough for Vision-Language Reasoning](http://arxiv.org/abs/2610.30834v1)
  <details><summary>📄 Abstract</summary>
  Long chain-of-thought reasoning improves vision-language models (VLMs), but it also exposes a temporal grounding failure: as generation unfolds, models may drift from image evidence while reinforcement learning still provides only a final-answer reward. We study this gap through visual revisit, a temporally localized reactivation of image evidence during reasoning. Across three VLM backbones, revisit peaks are predictive of correctness and causally linked to performance: masking them degrades ac...
  </details>

- **2026-10-22** — Leming Shen, Qiang Yang, Xinyu Huang et al. — [AgentDP: Towards Automated Model Deployment for Heterogeneous Embedded AI Applications](http://arxiv.org/abs/2610.30760v1)
  <details><summary>📄 Abstract</summary>
  This paper presents AgentDP, which aims to deploy pre-trained AI models on heterogeneous embedded devices by fully automating model optimization and adaptation (O&A) with Large Language Model (LLM) agents. AgentDP not only significantly reduces human effort via automation but also enhances model inference efficacy by integrating LLMs with device-specific domain knowledge. To deliver a robust automation framework, AgentDP develops novel solutions to address three key technical challenges: 1) To h...
  </details>

- **2026-10-22** — Xihao Wang, Chengyao Yu, Ruixing Ming — [Residual Calibration via Local Feature-Space Refinement](http://arxiv.org/abs/2610.30652v1)
  <details><summary>📄 Abstract</summary>
  Deep neural networks often struggle to provide reliable confidence estimates, making post-hoc calibration essential for reliable decision-making. Existing post-hoc methods largely rely on score-based transformations, which improve marginal calibration but often fail to capture spatially varying miscalibration in local regions of the learned feature space. To address this gap, we propose Local Adaptive Probability Estimation (LAPE), a post-hoc residual calibration framework. Specifically, LAPE tr...
  </details>

- **2026-10-22** — Zixu Wang, Huaquan Zhang, Shoukai Xu et al. — [Asking Less, Adapting Better: Feedback-Efficient Test-Time Adaptation for Vision-and-Language Navigation](http://arxiv.org/abs/2610.30643v1)
  <details><summary>📄 Abstract</summary>
  Vision-and-Language Navigation (VLN) requires agents to follow instructions and navigate to target locations. However, current VLN agents often suffer severe performance degradation in unseen environments due to distribution shifts. Test-Time Adaptation (TTA) offers a promising paradigm to bridge this gap, yet existing methods that rely on unsupervised entropy minimization can propagate errors through the trajectory, causing cascading failures in navigation. Recent methods mitigate this by incor...
  </details>

- **2026-10-22** — Fei Ding — [What the Specification Did Not Say: Specification-Oracle Gaps in Test-Graded Coding-Agent Benchmarks](http://arxiv.org/abs/2610.30635v1)
  <details><summary>📄 Abstract</summary>
  Coding-agent benchmarks often describe a task in natural language but grade it with tests taken from the upstream project. Passing those tests can require information the description never states: a constant's name, a module path, an exact message. We call this a specification-oracle gap: where it exists, a benchmark also measures whether an agent reproduces upstream implementation details. We formalise the gap, including the inconsistencies that chains of dependent tasks add, and build a static...
  </details>

- **2026-10-22** — N Balakrishna — [Robust M-Estimation for Spliced Power-Law Models Under Cusp-Type Non-Regularity](http://arxiv.org/abs/2610.30624v1)
  <details><summary>📄 Abstract</summary>
  Statistical modeling of heavy-tailed data with bounded or finite body behaviour often relies on composite or spliced distributions characterized by structural thresholds. Because the probability density function features a sharp directional shift (a cusp) at the join point, the classical log-likelihood function exhibits a discontinuity in its first derivative, causing standard Cramér-Rao regularity conditions and maximum likelihood frameworks to break down. To overcome this non-regularity, we de...
  </details>

- **2026-10-21** — Jona Joy — [Alpha: Systematic Fault Injection and Robustness Evaluation for LLM-Driven Embodied Manipulation](http://arxiv.org/abs/2610.30197v1)
  <details><summary>📄 Abstract</summary>
  Large language models (LLMs) are increasingly integrated into embodied robotic planning, yet standard benchmarks primarily evaluate end-to-end task completion in nominal environments, obscuring failure origins across the execution stack. We present Alpha, a systematic fault-injection and robustness-evaluation framework for LLM-driven manipulation in simulation. Alpha injects calibrated faults across perception (sensor lag), actuation (grip slip), kinematics (unreachable targets), and planning (p...
  </details>

- **2026-10-21** — Samuel Foo Enze, Manthan Patel, Fan Yang et al. — [RangeNav: Task-Aligned LiDAR Range-Image Pretraining for Robot Navigation](http://arxiv.org/abs/2610.29845v2)
  <details><summary>📄 Abstract</summary>
  Autonomous mobile robots operating in dense crowds and cluttered sites require $360^\circ$ perception to react to surrounding hazards. While panoramic LiDAR offers full-surround coverage, learning representations within reinforcement learning (RL) is sample-inefficient under sparse rewards, and existing 3D pretrained point-cloud encoders are too memory-heavy for massively parallel RL simulation. We present RangeNav, a compact (183k parameters) LiDAR range-image encoder pretrained entirely on syn...
  </details>

- **2026-10-21** — Daniel Ruiz, Luca Luceri, Emilio Ferrara — [Agent Mosaic: Recognizing Confidentiality Leaks in Agentic LLM Systems](http://arxiv.org/abs/2610.30418v1)
  <details><summary>📄 Abstract</summary>
  Modern LLM agents can retrieve information from accessible documents, and then disclose a sensitive conclusion assembled from them. This mosaic effect creates a critical risk for agents operating over confidential data. We quantify its realization with 30 synthetic cybersecurity, medical, and military examples, yielding 10,800 final answers from three LLM agents in controlled simulation and 1,440 answers from live agents in two open-source harnesses. Even under benign queries designed to be answ...
  </details>

- **2026-10-21** — Minsang Kim, Seungjun Baek — [MoEZip: Routing-Aware KV Cache Compression for Sparse Mixture-of-Experts LLMs](http://arxiv.org/abs/2610.30206v1)
  <details><summary>📄 Abstract</summary>
  Mixture-of-Experts (MoE) language models scale model capacity efficiently by activating a small subset of parameters per token. However, in long-context inference, memory remains a major bottleneck because the KV cache grows linearly with sequence length. Existing KV cache compression methods reduce this cost for dense transformers, but overlook a problem specific to MoE: KV eviction can change which experts are selected during answer generation, degrading the generation quality. We propose MoEZ...
  </details>

- **2026-10-21** — Zixuan Yu, Zhenheng Tang, Xiaowen Chu et al. — [Benchmarking and Error Analysis of Deep Search and Deep Research LLM Agents](http://arxiv.org/abs/2610.29346v1)
  <details><summary>📄 Abstract</summary>
  As Large Language Models (LLMs) evolve into autonomous Deep Search and Deep Research Agents capable of executing long-horizon, multi-step tasks, evaluating their reliability becomes increasingly critical. However, existing evaluation paradigms predominantly focus on final task outcomes, leaving a significant gap in understanding the intermediate execution traces, where agents are highly susceptible to various errors. To address this critical gap, we introduce a comprehensive methodology and anal...
  </details>

- **2026-10-21** — Zhuoyang Liu, Dantong Niu, Botong Zhang et al. — [Agentic World Action Models](http://arxiv.org/abs/2610.30136v1)
  <details><summary>📄 Abstract</summary>
  Recent world action models provide visual foresight and future prediction for robot manipulation, but lack explicit mechanisms for compositional skill reuse. Agentic robotics combines code-based planning and reasoning with reusable skills, but often lacks predictive grounding in physical dynamics. We introduce AW-0, an agentic world action model framework that integrates code-based planning with joint video and action prediction. We jointly model code, future video, and robot actions as three co...
  </details>

- **2026-10-21** — Hadi Khalaf, Sajani Vithana, Kunal Talreja et al. — [Circuits of LLM Classifiers](http://arxiv.org/abs/2610.30076v1)
  <details><summary>📄 Abstract</summary>
  Language models make it easy to build classifiers by simply prompting a model with the sample to classify. However, their predictions are neither deterministic nor uniformly reliable across samples. How can we combine predictions from different models to improve reliability? We view LLM classifiers as noisy measurement instruments of an underlying target label. Our goal is to maximize average classification accuracy at a given average query cost. To this end, we introduce circuits that organize ...
  </details>

- **2026-10-21** — Yicheng Xu, Zhikai Xu, Ziyuan Chen et al. — [TARSphere: A Robot-Oriented Full-Stack Framework for Long-Horizon Embodied Agents in Evolving Physical and Social Environments](http://arxiv.org/abs/2610.30043v1)
  <details><summary>📄 Abstract</summary>
  Robots must act under physical and social constraints while adapting to changes in their environment and human needs. Existing embodied-agent systems often focus on specified goals or abstract execution into symbolic actions, limiting evaluation in an evolving world. We introduce TARSphere, a robot-oriented full-stack framework for physically and socially grounded long-horizon embodied agents. TARSphere-Infra runs robot policies in a physics simulator with embodied NPCs and constrained dialogue....
  </details>

- **2026-10-21** — Tanu Singh, Aashna Suman, Vinod Patidar — [HiddenLens: A Multi-Layer LLM Framework for Detecting and Resolving Hidden Assumptions in Software Requirements](http://arxiv.org/abs/2610.29996v1)
  <details><summary>📄 Abstract</summary>
  Natural-language software requirements often omit assumptions about performance, operating conditions, user behaviour, and domain constraints, affecting architecture, testing, and deployment. If undiscovered until implementation, resolving them is far more costly than addressing them early. Although ambiguity and vagueness are widely studied, less attention has been given to assumptions embedded in requirements that appear clear and reasonable. We propose HiddenLens, a novel six-layer BERT-LLM p...
  </details>

- **2026-10-21** — Samuel Foo Enze, Manthan Patel, Fan Yang et al. — [RangeNav: Task-Aligned LiDAR Range-Image Pretraining for Robot Navigation](http://arxiv.org/abs/2610.29845v1)
  <details><summary>📄 Abstract</summary>
  Autonomous mobile robots operating in dense crowds and cluttered sites require $360^\circ$ perception to react to surrounding hazards. While panoramic LiDAR offers full-surround coverage, learning representations within reinforcement learning (RL) is sample-inefficient under sparse rewards, and existing 3D pretrained point-cloud encoders are too memory-heavy for massively parallel RL simulation. We present RangeNav, a compact (183k parameters) LiDAR range-image encoder pretrained entirely on syn...
  </details>

- **2026-10-21** — Bjorn Stragier, Emilia Szymańska, J. Micah Prendergast et al. — [Reading the Room: Scale-ambiguous Semantic Registration of Sparse VSLAM Maps to Floor Plans in Partially Built Environments](http://arxiv.org/abs/2610.29647v1)
  <details><summary>📄 Abstract</summary>
  Many robotic construction applications, such as progress tracking, require registering a sensor trajectory to a prior 2D floor plan. Visual capture is attractive for its low cost and availability, but aligning a visual simultaneous localization and mapping (VSLAM) map to a floor plan is difficult; VSLAM recovers geometry only up to an unknown similarity transform, the sparse point cloud is cross-modal to the symbolic floor plan, sites are only partially built during capture, and construction sit...
  </details>

- **2026-10-21** — Zhiguang Yang, Yulin Yang, Fuyu Lv et al. — [Progressive Learning from Content to Relevance to Personalization for CTR Prediction](http://arxiv.org/abs/2610.29138v1)
  <details><summary>📄 Abstract</summary>
  Multimodal click-through rate (CTR) prediction is central to search systems, where ranking depends on item content, query relevance, and user preference. Existing approaches incorporate content through dense embeddings or coarse discrete IDs, yet effectively integrating fine-grained heterogeneous content with ID-based predictors remains challenging. We propose FineSID, a progressive learning framework that unifies content tokenization, query--item semantic pretraining, and personalized post-trai...
  </details>

- **2026-10-21** — Lisa Y. W. Tang — [From Canon to Nikon: Camera Domain Shift and Potential Equity Implications in Retinal AI](http://arxiv.org/abs/2610.29104v1)
  <details><summary>📄 Abstract</summary>
  Diabetic retinopathy is a leading cause of preventable blindness, yet access to regular screening remains limited worldwide. AI offers a scalable approach, but its performance can be sensitive to image quality and acquisition conditions. In a Brazilian cohort of 8,524 patients, retinal images acquired with the Nikon NF5050 were more than twice as likely to have inadequate image quality compared with those acquired with the Canon CR-2, despite refurbished Canon systems costing more than twice as ...
  </details>

- **2026-10-21** — Taiga Ikeshima, Sheila Sutjipto, Lan Wu et al. — [Distance Field Driven Reinforcement Learning for Reactive and Robust Collision Avoidance](http://arxiv.org/abs/2610.29452v1)
  <details><summary>📄 Abstract</summary>
  Robust and reactive collision avoidance remains a central challenge for deploying Reinforcement Learning (RL) policies on real robotic manipulators, particularly when transferring behaviours learned in simulation to the physical world. This paper presents an RL framework that integrates the Euclidean Distance Field (EDF) directly into the observation space, providing the agent with continuous geometric cues that support stable and responsive avoidance behaviours. By leveraging the rich spatial i...
  </details>

- **2026-10-21** — Meihong Jia, Yasemin Timar, Jonathan Taws — [GuideEvolve: Self-Evolving Agent Framework with Expert Guidance and 3Ts Mechanisms](http://arxiv.org/abs/2610.30017v1)
  <details><summary>📄 Abstract</summary>
  This study introduces GuideEvolve, a self-evolving agent framework incorporating expert guidance and three autonomous regulatory mechanisms, collectively termed the 3Ts: Think Fast and Slow, Throwback, and Termination by choice. The framework addresses critical limitations in extant self-evolving agent paradigms through dual innovations: (1) a task-specific expert-evaluation-driven evolutionary pipeline, and (2) the integration of 3Ts mechanisms to facilitate cognitive optimization, performance ...
  </details>

- **2026-10-21** — Liam Dugan, Callum McDougall, Matthew Denton et al. — [Building Auditable AI Text Detectors with Sparse Autoencoders](http://arxiv.org/abs/2610.30006v1)
  <details><summary>📄 Abstract</summary>
  AI-generated text detectors are increasingly deployed in consequential settings---peer review, education, admissions, journalism, and content moderation---where their outputs directly affect individuals. Yet the strongest detectors are fine-tuned neural classifiers whose decisions are opaque, while transparent alternatives (stylometric and linguistic-feature classifiers) underperform them by wide margins. We present a pipeline that converts a fine-tuned neural detector into a classifier that ope...
  </details>

- **2026-10-21** — Puru Vaish, Meelad Dashti, Christoph Brune et al. — [Compositionality with Primitives: A Unified View from Euclidean to Hyperbolic Vision-Language Models](http://arxiv.org/abs/2610.29811v1)
  <details><summary>📄 Abstract</summary>
  Compositional zero-shot learning (CZSL) aims to recognize novel combinations of previously observed objects and attributes. Prior work showed that large-scale vision-language models encode decomposable semantic structures that can be recomposed to enable generalization. The Geodesically Decomposable Embeddings (GDE) framework formalizes this by identifying directions in the tangent space at the Frechet mean of the embedding distribution, which encode primitive visual concepts. Unseen attribute-o...
  </details>

- **2026-10-21** — G. X. A. Petronilo, M. R. Araújo, Erico S. Teixeira et al. — [Mamba Quantum Eigensolver (MQE): A Selective State Space Model for Scalable Ground State Simulations in Quantum Chemistry](http://arxiv.org/abs/2610.29779v1)
  <details><summary>📄 Abstract</summary>
  Predicting molecular electronic structure using Quantum Computing approaches is a challenge in Computational Chemistry. Traditional Variational Quantum Eigensolvers (VQEs) are typically hindered by optimization challenges. The alternative Generative Quantum Eigensolver (GQE) mitigates this by reformulating ground-state search as discrete sequence generation, but its Transformer backbone suffers from quadratic computational complexity, bottlenecking scalability for larger molecules. To address th...
  </details>

- **2026-10-21** — Nan-Nan Zhang, Si-Heng Luo, Xin-Di Pei et al. — [Fast2Peak: High-Fidelity Restoration Algorithm by Single-Pixel Masking towards Real-Time Spectral Measurements](http://arxiv.org/abs/2610.29753v1)
  <details><summary>📄 Abstract</summary>
  Improving the temporal and spatial resolution of spectroscopy inevitably reduces the photons available to each measurement, pushing rapid measurements into photon-starved conditions where weak spectral features are obscured by stochastic background noise. Here, we present Fast2Peak (F2P), a self-supervised Transformer framework that transforms the spectral restoration task into a context-prediction problem. Given that physically constrained spectral signals exhibit strong local continuity, where...
  </details>

- **2026-10-21** — Ziliang Li, Jingzhi Li — [Parameters Robust Parallelizable Iterative Decoupled Algorithms for Thermo-Poroelasticity with Nonlinear Convective Transport](http://arxiv.org/abs/2610.29668v1)
  <details><summary>📄 Abstract</summary>
  This paper presents several parallel iterative algorithms for the nonlinear thermo-poroelasticity. We introduce an auxiliary variable to transform the original model into a four-field formulation to overcome Poisson locking. The iterative idea is extended to linearize and decouple the four-field model. Different coupling strategies are employed among these three subproblems, combined with appropriately designed iteration settings, yielding distinct iterative parallel algorithms. Stabilization te...
  </details>

- **2026-10-21** — Ajeet Kumar Singh, Nehal Mishra, Anurag Tripathi et al. — [Learning to Reason Like a Cytopathologist:Clinically Grounded Multiscale Evidential Learning for Cervical Cytology](http://arxiv.org/abs/2610.29665v1)
  <details><summary>📄 Abstract</summary>
  Cervical cytology presents a fundamentally ambiguous diagnostic landscape, where equivocal categories such as Atypical Squamous Cells of Undetermined Significance (ASC-US) occupy a morphological grey zone that is definitional. For clinical decision support, the goal extends beyond assigning a definitive label to every sample: cases must also be distinguished by whether the available evidence supports a confident decision or warrants further consideration, a distinction conventional classificatio...
  </details>

- **2026-10-21** — Yan Gong, Zheng Chu, Wei Koong Chai et al. — [Recursive Code Evolution for Task-Oriented Semantic Communications](http://arxiv.org/abs/2610.29641v1)
  <details><summary>📄 Abstract</summary>
  Semantic communication jointly optimizes inference accuracy, channel use, and computation, yet the underlying communication program is typically specified before training. This paper presents ComRSI (Communications-Oriented Recursive Self-Improvement), a framework for recursively evolving that program through large-language-model-assisted code edits. A fixed agent modifies the encoder, channel adapters, decoder, loss, and training policy; a protected evaluator screens candidates under prescribed...
  </details>

- **2026-10-21** — Masood Jan, Wafa Njima, Xun Zhang et al. — [Cross-Area Transfer Learning for VLC-based Indoor Localization with a Transfer Efficiency Score](http://arxiv.org/abs/2610.29638v1)
  <details><summary>📄 Abstract</summary>
  Indoor localization systems are critical for Industry-4.0 applications. Visible Light Communication (VLC)-based systems offer advantages such as immunity to electromagnetic interference, high accuracy, and energy efficiency, but their performance is hindered by environmental variability across deployment areas. This paper presents a transfer learning (TL) framework for VLC-based indoor localization that enhances cross-area robustness while reducing data requirements. Using real-world measurement...
  </details>

- **2026-10-21** — Chunming He, Dingming Zhang, Fengyang Xiao et al. — [Supervision-Adaptive Curriculum and Guarded Anti-Curriculum Learning for Dense Prediction](http://arxiv.org/abs/2610.29519v1)
  <details><summary>📄 Abstract</summary>
  Curriculum learning orders samples by difficulty, but difficulty alone does not establish supervision reliability for dense prediction. Easy samples can expose shortcuts, hard samples can be informative, and noisy or ambiguous samples can mislead training. Building on our conference method CurriSeg, we present PaceShift, a stabilize-then-challenge paradigm combining supervision-adaptive curriculum selection with guarded spectral post-training. A learning-dynamics view motivates separating superv...
  </details>

- **2026-10-21** — Geetanjali Sharma, Aryan Jain, Dev Nagaich et al. — [Balancing Foundation Models and Trait-Specific Learning for Forehead-Crease Recognition](http://arxiv.org/abs/2610.29495v1)
  <details><summary>📄 Abstract</summary>
  Biometric recognition often degrades under partial facial vis- ibility, where conventional facial cues are occluded. The forehead region remains consistently visible and contains distinctive crease patterns that can serve as a complementary biometric trait. We present a unified eval- uation of forehead-crease recognition across explainable zero-shot rea- soning, domain-adaptive learning, and trait-specific modeling. FIRE en- ables interpretable zero-shot verification using multimodal large langu...
  </details>

- **2026-10-21** — Gwen maudet, Mathis Da Cunha, Grégoire Danoy — [Interpretable Cutting Plane Selection for Mixed-Integer Linear Programming Using Genetic Programming](http://arxiv.org/abs/2610.29311v1)
  <details><summary>📄 Abstract</summary>
  Cutting planes (cuts) remove fractional solutions from mixed-integer linear programs (MILPs) without excluding any feasible integer solutions, making them a key ingredient in modern MILP solvers. Current state-of-the-art solvers rely on fine-tuned handcrafted cut strategies, which, despite their effectiveness, remain inherently static and can be suboptimal. More recently, learning-based approaches have been proposed to design adaptive cut strategies; however, most of these methods are based on n...
  </details>

- **2026-10-21** — Yuyao Zhang, Yakun Cui, Han Zhu et al. — [Same Probabilities, Different Advice: Gain-Loss Framing Effects in High-Stakes LLM Decision Support](http://arxiv.org/abs/2610.29294v1)
  <details><summary>📄 Abstract</summary>
  Large language models (LLMs) are increasingly used to support consequential decisions, yet their reliability under equivalent representations of uncertainty remains unclear. Existing work has documented prompt sensitivity, cognitive biases, and confidence miscalibration, but it is still unknown whether high-stakes advice changes when the same probability is expressed through complementary gain and loss frames. We introduce FrameBench-HPS, a controlled benchmark of 2,880 prompts derived from 240 ...
  </details>

- **2026-10-21** — Qian Li, Shang-Hua Teng — [Approximate Solomonoff Induction: On the Robustness of Learned Universal Predictors](http://arxiv.org/abs/2610.29289v1)
  <details><summary>📄 Abstract</summary>
  Why large language models trained via log-loss minimization over massive and diverse datasets exhibit broad capabilities and generalizable skills is not yet fully understood. Grau-Moya et al. (ICML 2024) offer a conceptual explanation through the lens of meta-learning: if sequence-generating environments $ν$ are drawn from a prior $w_ν$, minimizing population log-loss recovers the corresponding Bayesian mixture predictor $ξ=\sum_νw_νν$. In the idealized limit in which $w$ is a universal prior, t...
  </details>

- **2026-10-21** — Junjie Wang, Zhihao Yuan, Yunhan Tang et al. — [Think-Capture: Active 3D Geometry Acquisition for Spatial Reasoning in Vision-Language Models](http://arxiv.org/abs/2610.29232v1)
  <details><summary>📄 Abstract</summary>
  Vision-Language Models (VLMs) excel at 2D recognition but often fail to maintain consistent 3D relations across sparse viewpoints, leading to spatial hallucinations under occlusion and perspective changes. Existing methods commonly fuse all frames with dense geometry, incurring substantial computation and context overhead while encouraging blind reliance on imperfect estimators. We present Think-Capture, a query-conditioned framework that first identifies task-critical objects and then acquires ...
  </details>

- **2026-10-21** — Eirik Botten Nicolaysen — [norregel: a preregistered benchmark of dated numeric values in Norwegian law](http://arxiv.org/abs/2610.29207v1)
  <details><summary>📄 Abstract</summary>
  norregel asks language models for numeric values in Norwegian statutes, regulations and parliamentary decisions (NOK amounts, percentages, multiples of the National Insurance basic amount (G) and age limits), each at a stated date. The 916 items were extracted mechanically from Lovdata's open data, and each carries the dated history of its provision, so an answer can be classed as correct, outdated, wrong or uninterpretable. We report a first and a second preregistered run on the same items. In ...
  </details>

- **2026-10-21** — Masoud Mardani, Shivani Sharma, Saul H. Lapidus et al. — [Valence-Driven Structural Transformation and Phase Coexistence in Chemically Substituted EuPd2Si2](http://arxiv.org/abs/2610.29180v1)
  <details><summary>📄 Abstract</summary>
  EuPd2Si2 serves as an ideal system to probe the interplay between lattice dynamics and electronic instabilities through its tunable valence transition, responsive to temperature, pressure, and magnetic field. Here, we focus on investigating the origin of the temperature-induced europium valence instability in pristine EuPd2Si2, alloyed EuPd2Si1.95Ge0.05, and EuPd2Si1.9Ge0.1 and its correlation with structural responses. Compared with the parent compound EuPd2Si2 which exhibits the europium valen...
  </details>

- **2026-10-21** — Kelan Kuang, Qihan Hu, Jian Kang et al. — [XingChen-UniFE: A Unified Generative Speech Front-End via Complementary Acoustic-Semantic Modeling](http://arxiv.org/abs/2610.29164v1)
  <details><summary>📄 Abstract</summary>
  This paper presents XingChen-UniFE, a unified large audio language model (LALM) for general speech restoration (GSR) and target speaker extraction (TSE). The proposed model employs complementary semantic and acoustic representations through a dual-stream encoder, where a self-supervised learning model provides hierarchical semantic features and a learnable acoustic branch captures fine-grained structures from complex spectra. A bidirectional cross-attention module further facilitates information...
  </details>

- **2026-10-21** — William Huang, David Li, Xiang 'Anthony' Chen et al. — [GenXR-Bench: Benchmarking Coding Agents for Interactive XR Development](http://arxiv.org/abs/2610.29014v1)
  <details><summary>📄 Abstract</summary>
  Coding agents are rapidly advancing from single-file generation to long-horizon repository-scale engineering, yet the evaluation of their capabilities to author interactive extended reality (XR) applications remains an open challenge. Unlike traditional software, XR applications operate within dynamic 3D physical environments where runtime robustness depends jointly on continuous user motion, spatial input, and environmental sensing. We introduce GenXR-Bench, the first benchmark for the end-to-e...
  </details>

- **2026-10-20** — Md Khalid Syfullah, Alvi Ataur Khalil — [Can Quantum Layers offer Performance and Security Advantages in Vision-Language Models?](http://arxiv.org/abs/2610.28964v1)
  <details><summary>📄 Abstract</summary>
  As quantum computing moves from the noisy intermediate-scale quantum (NISQ) era toward early fault-tolerant quantum computing (EFTQC), quantum-enhanced AI is shifting from a conceptual idea to experimental research. Quantum components are expected to extend the capabilities of existing AI systems, yet it remains unclear how such components will help within large multimodal models. In this study, we try to answer that question for vision-language models (VLMs) using classically simulated quantum ...
  </details>

- **2026-10-20** — Isacco Beretta — [Towards Realistic Models of Change: A Causal Perspective on Decision-Making and Dynamical Systems](http://arxiv.org/abs/2610.28803v1)
  <details><summary>📄 Abstract</summary>
  While statistical learning has made remarkable progress in recent decades, driven by large datasets and data-driven protocols that have transformed scientific practice, it still faces a key limitation: it struggles to generalize beyond the data it has seen, often failing under distribution shift. Causality offers a promising solution: causal models focus on the underlying mechanisms of change rather than surface-level associations, enabling robust reasoning under external interventions. This all...
  </details>

- **2026-10-20** — Yisi Liu, Nicholas Lee, Gopala K. Anumanchipalli — [StyleStream 2.0: Fast and Controllable Streaming Voice Style Conversion](http://arxiv.org/abs/2610.28940v1)
  <details><summary>📄 Abstract</summary>
  Voice style conversion (VSC) aims to transform a source utterance to match the timbre, accent, and emotion of a target voice while preserving linguistic content. StyleStream 1.0 introduced the first streamable zero-shot VSC system with state-of-the-art conversion quality, but remained limited in two ways: approximately 1s end-to-end latency on consumer hardware, and the lack of a text-based interface for designing or editing target voices. We present StyleStream 2.0, a fast and controllable stre...
  </details>

- **2026-10-20** — Jinyi Ye, Lei Cao, Ding Chen et al. — [The Butterfly Effect in LLM Social Simulations: From Architecture Sensitivity to Robustness Audits](http://arxiv.org/abs/2610.28981v1)
  <details><summary>📄 Abstract</summary>
  A butterfly effect occurs when a local perturbation propagates through a system and produces divergence in its collective outcome. In LLM social simulations, this creates a particular challenge for scientific inference: sensitivity to implementation choices can enter agent interactions and alter the collective outcomes on which scientific claims are based. We study this problem through a repeated Prisoner's Dilemma and a social-media echo chamber, spanning representation- and design-level pertur...
  </details>

- **2026-10-20** — Yongqing Liang, Yuzhong Chen, Sihang Li et al. — [RoPT: Robust 6DoF Object Pose Tracking in Video](http://arxiv.org/abs/2610.28962v1)
  <details><summary>📄 Abstract</summary>
  Accurate 6-DoF object pose tracking is essential for robotic interaction, yet conventional monocular pipelines frequently suffer from catastrophic divergence under rapid object motion. We present RoPT, a robust tracking framework engineered to overcome this limitation by unifying visual perception, temporal kinematics, and global re-localization into a tightly coupled closed loop. Unlike existing open-loop trackers, RoPT delivers three critical capabilities that fundamentally alter system resili...
  </details>

- **2026-10-20** — Hieu Tran, Hong Yu — [Second Thoughts: Exploring and Planning through Comparative Imagination in World Models](http://arxiv.org/abs/2610.28779v1)
  <details><summary>📄 Abstract</summary>
  World models let agents compare imagined outcomes before acting, but an agent must still decide which alternatives to explore and when a proposed plan should replace its learned policy. We introduce SDI (Sibling Disagreement in Imagination), which connects these decisions through a shared actor-based reference. SDI compares action sequences imagined from the same model state, using repeated rollouts of the actor's own sequence to measure variation under fixed behavior. This reference scales both...
  </details>

- **2026-10-20** — Nicolás Mauricio Cuadrado Ávila, Ivo Gollini Navarrete, Martin Takáč et al. — [Building a Nested LADDER for LLM Unstructured Post-Training Pruning](http://arxiv.org/abs/2610.28773v1)
  <details><summary>📄 Abstract</summary>
  Non-uniform allocation can improve post-training pruning of large language models, yet quality can still degrade sharply at high sparsity. To control degradation as sparsity increases, we introduce LADDER (Layer-Wise Allocation via Damage-Driven Evaluation and Refinement), which allocates sparsity incrementally. At each step, it evaluates pruning an additional fraction of weights from each eligible layer and commits the layer update that causes the least end-to-end degradation per removed parame...
  </details>

- **2026-10-20** — Junha Song, Geonmo Gu, Jeongeun Park et al. — [LaLa-World: Scaling Latent World Models with Natural Language Actions](http://arxiv.org/abs/2610.27851v2)
  <details><summary>📄 Abstract</summary>
  This paper shows that JEPA-style latent world models (LWMs) can learn across diverse domains and data sources by adopting the language-conditioned interface of video generation models. We establish this approach as an effective and efficient basis for planning with imagination and downstream policy fine-tuning. To this end, we introduce LaLa-World, a Language-conditioned Latent World model that learns from simulation and robot trajectories together with broader image and video data. Two designs ...
  </details>

- **2026-10-20** — Wenjie Lou, Tianshuo Peng, Shiyang Feng et al. — [Sage-A1.5: From Long-Horizon Execution to Scientific Exploration with Capability Composition](http://arxiv.org/abs/2610.28578v1)
  <details><summary>📄 Abstract</summary>
  In this report, we introduce Sage-A1.5, a 35B Mixture-of-Experts agentic model that builds on A1 to advance long-horizon problem solving through adaptive capability composition. Compared with A1, Sage-A1.5 learns not only to solve individual tasks, but also to organize work and revise its approach during execution. Sage-A1.5 highlights three improvements: agentic orchestration, verification, and open scientific discovery. First, agentic orchestration extends single-agent execution through task d...
  </details>


### 📂 watermark
*水印与溯源 / Watermarking & Provenance* — 19 papers

- **2026-10-22** — Maria Gabriela Alves Zuppardo, Vinicius Cardoso Garcia — [Beyond Accuracy: Disentangling Decomposition from Typed-State Quality Assurance in Multi-Agent LLM Pipelines](http://arxiv.org/abs/2610.31280v1)
  <details><summary>📄 Abstract</summary>
  Multi-agent LLM pipelines are often credited with gains in software engineering tasks, but it is rarely clear whether a gain stems from the typed contract between agents or from the specialized prompts that decomposition enables. We study this attribution problem in Requirements Engineering, comparing three architectures for classifying requirements as functional or non-functional and then prioritizing them with MoSCoW: a single-call baseline; a two-call variant that reuses the pipeline's specia...
  </details>

- **2026-10-22** — Tirana Noor Fatyanosa, Ummu Ditya Erliana, Mahendra Data et al. — [IndoNutriQA: An Indonesian Clinical Nutrition Question Answering Benchmark](http://arxiv.org/abs/2610.31256v1)
  <details><summary>📄 Abstract</summary>
  Clinical Question Answering (QA) underpins Clinical Intelligent Decision Support Systems, but progress is severely limited for low-resource languages such as Indonesian by the absence of public domain-specific data. We introduce IndoNutriQA, an expert-curated Indonesian clinical QA benchmark of 911 question-answer pairs built from real clinical-nutrition reports. Rather than a large-scale training corpus, it is positioned as a high-quality evaluation resource: every pair is grounded in a clinica...
  </details>

- **2026-10-22** — Xiaoao Zhu, Ni Zhang, Jie Ren et al. — [ATLAS: A Multi-Agent Framework for Lifting Binary to Canonical Compiler IR](http://arxiv.org/abs/2610.30877v1)
  <details><summary>📄 Abstract</summary>
  Lifting stripped, heavily optimized binaries to a canonical, pre-optimization LLVM intermediate representation (IR) is essential for downstream security analysis and legacy software migration when source code is unavailable. However, aggressive compiler optimizations rewrite control and data flow, remove structural metadata, and introduce type-erased low-level idioms, causing current lifters to produce malformed or semantically divergent IR. We present ATLAS, a multi-agent framework designed to ...
  </details>

- **2026-10-22** — Jie Ying, Xutao Zhang, Ningyuan Chen et al. — [AgentTriage: Replayable Security Diagnosis Across Heterogeneous Agent Runtimes](http://arxiv.org/abs/2610.30738v1)
  <details><summary>📄 Abstract</summary>
  When tool-use agents write files, execute code, or send data, their final responses do not explain the resulting security events, and heterogeneous runtimes expose the relevant evidence through incompatible interfaces. We present AgentTriage, an executable contract for replayable security diagnosis across heterogeneous runtimes. The contract admits conclusions whose claims cite canonical runtime events and requires abstention when mandatory evidence is missing. Runtime overlays normalize native ...
  </details>

- **2026-10-22** — Jiajun Wu, Jian Yang, Yaxin Du et al. — [ProductWebBench: Evaluating Website Continuity Beyond Task Completion](http://arxiv.org/abs/2610.31118v1)
  <details><summary>📄 Abstract</summary>
  Frontend coding agents are usually graded on one question: did the requested target get built. Real engineering changes carry a second obligation, because the rest of the site has to keep working. We call that second obligation website continuity, and introduce ProductWebBench, a benchmark that scores both on living frontend repositories: 320 Change tasks over existing code and 80 long-horizon Build tasks. Every task freezes a repository snapshot, staged requirements, browser evidence and determ...
  </details>

- **2026-10-21** — Josh Qixuan Sun, Xiaoying Xing, Yurun Chen et al. — [NavBind: Diagnosing Instruction-Action Binding at Route Forks in Navigation VLAs](http://arxiv.org/abs/2610.29203v2)
  <details><summary>📄 Abstract</summary>
  Vision-language-action (VLA) navigation models translate visual observations and instructions into actions. Navigation success assesses whether an agent reaches the goal. However, reaching the goal successfully does not establish whether the model genuinely follows the instructions or relies on visual cues or navigation history. We introduce NavBind to diagnose instruction-action binding: whether changing the instruction influences the probabilistic distribution of the actions, with the navigati...
  </details>

- **2026-10-21** — Pouria Behnoudfar, Nan Chen — [When Language Models Misinterpret Uncertainty in Earth System Mechanism Attribution](http://arxiv.org/abs/2610.30501v1)
  <details><summary>📄 Abstract</summary>
  Mechanistic attribution in Earth system science requires quantifying uncertainty and communicating its implications. Here, we develop an uncertainty-aware mechanistic attribution pipeline that constructs probabilistic fingerprints from ensemble estimates, including covariance-aware separation of competing mechanisms, and an evidence ladder that systematically varies the information provided to language models (LLMs). We evaluate this framework in an idealized stochastic system and a coupled El N...
  </details>

- **2026-10-21** —  Yan,  Liang, Anuj Agarwal et al. — [When Agentic Retrieval Fails Silently: Framework and Production Evidence from a Creative AI Assistant](http://arxiv.org/abs/2610.30423v1)
  <details><summary>📄 Abstract</summary>
  CTR, MRR, and behavioral NDCG assume the user sees ranked results and acts on them. In an agentic assistant, a generation layer consumes retrieval output first, and that assumption breaks in three ways. The agent reads the results before the user does (who). The user's action can come several turns or sessions after retrieval (when). Outcomes blend retrieved content with the model's own knowledge (what caused it). We call this the attribution gap. We propose Layered Agentic Retrieval Assessment ...
  </details>

- **2026-10-21** — Yash Kulthe, Vishal Asnani, Shruti Agarwal et al. — [FiLM-CAM: Keyed Feature Modulation for Conditional-Access Watermarking](http://arxiv.org/abs/2610.30347v1)
  <details><summary>📄 Abstract</summary>
  We propose FiLM-CAM; a conditional-access image watermarking approach that enforces authorized encoding, decoding, and removal through keyed feature modulation. A secret key conditions a Feature-wise Linear Modulation (FiLM) mechanism that transforms the internal representation of the watermark signal before embedding, thereby coupling the payload to the key at the feature, rather than pixel level. The same key must be presented to condition the decoder to correctly recover the payload embedded ...
  </details>

- **2026-10-21** — Xuanlyu Zhu, Feng Tian, Yang Zhong et al. — [Overview of CHIP 2026 Shared Task 1: Patient-Specific Phenotype Concept Recognition in Full-Text Biomedical Literature](http://arxiv.org/abs/2610.29606v2)
  <details><summary>📄 Abstract</summary>
  Automatic phenotype information extraction plays an important role in rare disease diagnosis, genotype-phenotype analysis, and precision medicine. However, accurately identifying phenotype concepts and determining their associations with specific patients remain challenging, particularly in full-text biomedical articles involving multiple patients and complex clinical descriptions. This paper presents an overview of CHIP 2026 Shared Task 1, which aims to promote the development of methods for pa...
  </details>

- **2026-10-21** — Xinyu Wang, Huafeng Shi, Yue Ma et al. — [LiveAct: Towards Real-Time Multi-Agent World Models with Heterogeneous Action Interfaces](http://arxiv.org/abs/2610.29408v1)
  <details><summary>📄 Abstract</summary>
  Interactive video world models predict how an environment evolves under user actions, but most existing systems assume one controlled agent and one task-specific action interface. We study multi-agent video world modeling, where one model generates a joint visual future for multiple controlled agents while interpreting heterogeneous controls ranging from binary game buttons to continuous robot commands. This task presents two complementary challenges. First, every agent-indexed action stream mus...
  </details>

- **2026-10-21** — Josh Qixuan Sun, Xiaoying Xing, Yurun Chen et al. — [NavBind: Diagnosing Instruction-Action Binding at Route Forks in Navigation VLAs](http://arxiv.org/abs/2610.29203v1)
  <details><summary>📄 Abstract</summary>
  Vision-language-action (VLA) navigation models translate visual observations and instructions into actions. Navigation success assesses whether an agent reaches the goal. However, reaching the goal successfully does not establish whether the model genuinely follows the instructions or relies on visual cues or navigation history. We introduce NavBind to diagnose instruction-action binding: whether changing the instruction influences the probabilistic distribution of the actions, with the navigati...
  </details>

- **2026-10-21** — Chun Gu, Xiaofei Wei, Yiming Chen et al. — [Training in Deployment: Human-in-the-loop Online Post-Training for Robot Manipulation](http://arxiv.org/abs/2610.29264v1)
  <details><summary>📄 Abstract</summary>
  Large pretrained robot foundation models provide strong priors for manipulation, yet adapting them to target tasks with offline teleoperated demonstrations often fails to cover the contact-rich, recovery, and precision-critical states encountered during deployment. Existing methods mitigate this issue by augmenting offline demonstrations with human-in-the-loop data or online reinforcement learning. Despite this, offline post-training adapts slowly because it cannot immediately absorb deployment ...
  </details>

- **2026-10-21** — Jielong Tang, Ling-An Zeng, Xujie Yuan et al. — [Remembering Through Change: Provenance-Preserving Hypergraph Memory for Multimodal Agents](http://arxiv.org/abs/2610.29995v1)
  <details><summary>📄 Abstract</summary>
  Long-term memory for multimodal agents remains challenging, as it must preserve fine-grained visual evidence while tracking entity evolution across sessions. Existing abstraction-based memories compress images into text, often discarding visually discriminative details, whereas pixel-preserving memories retain raw observations but struggle to reliably associate diverse observations with persistent entity identities and track their evolving states. To address these limitations, we propose MHG-Mem...
  </details>

- **2026-10-21** — Xuanlyu Zhu, Feng Tian, Yang Zhong et al. — [Overview of CHIP 2026 Shared Task 1: Patient-Specific Phenotype Concept Recognition in Full-Text Biomedical Literature](http://arxiv.org/abs/2610.29606v1)
  <details><summary>📄 Abstract</summary>
  Automatic phenotype information extraction plays an important role in rare disease diagnosis, genotype-phenotype analysis, and precision medicine. However, accurately identifying phenotype concepts and determining their associations with specific patients remain challenging, particularly in full-text biomedical articles involving multiple patients and complex clinical descriptions. This paper presents an overview of CHIP 2026 Shared Task 1, which aims to promote the development of methods for pa...
  </details>

- **2026-10-21** — Jingxuan Chen, Mohammad Taher Pilehvar, Jose Camacho-Collados — [Does Every Instance Count Equally? Order Effects in LLM Multi-Instance Processing](http://arxiv.org/abs/2610.29057v1)
  <details><summary>📄 Abstract</summary>
  Users increasingly rely on large language models (LLMs) to analyse collections of independent inputs, such as product reviews or social media posts, and return a single aggregated answer. This setting requires multi-instance processing (MIP), where a model combines information from multiple instances into one prediction. We study a task in which the model must infer a binary label for each instance, and identify the most frequent label among the full instance set. The correct answer should be in...
  </details>

- **2026-10-20** — Mohammad Siahkamari, Phuoc Dat Nguyen, Stephen MacNeil — [To Manipulate or Not: Opinion Dynamics in LLM Interactions](http://arxiv.org/abs/2610.28875v1)
  <details><summary>📄 Abstract</summary>
  Large language models increasingly take part in extended conversations where they can both shape and be shaped by another party's views, yet most persuasion research measures only one side of that exchange. We introduce a controlled LLM-LLM debate framework in which two language-model roles repeatedly discuss a contested topic (climate-change attribution): one is given an assigned stance and, in some conditions, an explicit instruction to persuade, while the other receives no assigned position. ...
  </details>

- **2026-10-20** — Saiyue Lyu, Jerrold Huang, Yunbei Zhang et al. — [Where Should a Stuck Agent Spend Its Next Tokens? Causal Attribution of Inference-Time Resources](http://arxiv.org/abs/2610.28834v1)
  <details><summary>📄 Abstract</summary>
  Inference-time scaling is often treated as a token-budget problem, but a failed coding agent can seek qualitatively different resources: computation, information, or feedback. We introduce Banzhaf Resource Attribution (BRA), a controlled factorial framework that measures each resource's marginal contribution to repair and its interactions while holding the failed state and revision protocol fixed. We evaluate six models on 194 function-level failures from MBPP+ and HumanEval+ and 126 repository-...
  </details>

- **2026-10-20** — Yiqing Shen, Mathias Unberath — [Complexity-Aware Surgical Video Reasoning Segmentation with Digital Twin and Context Memory](http://arxiv.org/abs/2610.28776v1)
  <details><summary>📄 Abstract</summary>
  Conventional surgical segmentation relies on closed-set categories or explicit text queries, which cannot resolve implicit queries that require reasoning about workflows, instrument functions, and temporal relationships. To address these limitations, we propose SurgReasonSeg, a complexity-aware method that brings reasoning segmentation over digital twin (DT) representations to surgical video. Specifically, SurgReasonSeg constructs DT representations from surgical foundation models and trains two...
  </details>


### 📂 unlearning
*机器遗忘 / Machine Unlearning* — 1 papers

- **2026-10-21** — Yiyang Duan, Fan Wu, Tiantong Wu et al. — [C$^2$U in RAG: Compositional Concept Unlearning in Retrieval-Augmented Generation](http://arxiv.org/abs/2610.29223v1)
  <details><summary>📄 Abstract</summary>
  Retrieval-augmented generation can expose unwanted concepts through retrieved evidence even when the generator is moderated. We study query-side concept suppression with a fixed encoder and document index. Compositional Concept Unlearning (C$^2$U) routes a profile-derived direction through an augmented atom bank, adding only a bounded edited-minus-original delta to the raw query. Across five datasets, four encoders, and three seeds, the validation-selected configuration reduces pooled binary tar...
  </details>


### 📂 agent-safety
*Agent 安全框架 / Agent Safety Frameworks* — 1 papers

- **2026-10-21** — Laurent Goujon — [Agentic Architecture of Information Systems. The AAM/5C Model: A Reference Model for Distributed Autonomy](http://arxiv.org/abs/2610.30221v1)
  <details><summary>📄 Abstract</summary>
  Large organizations increasingly face what this book calls the cognitive complexity wall: at the scale of hundreds of interacting components, maintaining the dependency map and reacting at the pace of incidents exceeds what a human team can deliver. This conceptual volume proposes AAM/5C, in which five capabilities (Capture, Comprehend, Choose, Coordinate, Control) are instantiated across seven logical layers, L1 to L7. A single authorization rule, R-AUT, separates who proposes, who decides and ...
  </details>


### 📂 survey
*综述与系统化 / Surveys & Systematization* — 10 papers

- **2026-10-22** — Tamer Abdelaziz — [What Ethereum Developers Ask For, and Whether They Get It: Ten Years of Ethereum Stack Exchange](http://arxiv.org/abs/2610.30829v1)
  <details><summary>📄 Abstract</summary>
  The Ethereum community learns where developers struggle through surveys and interviews, which record what developers say when asked about a chosen theme. Ethereum Stack Exchange (ESE) records what they ask for unprompted, and whether anyone resolves it. We study every question posted to ESE from Jan 2016 to Dec 2025, 54,637 in all, and label each with a prompt-based topic pipeline seeded with eight Ethereum-specific topics and open to new ones (22 topics in all). A three-provider committee of la...
  </details>

- **2026-10-22** — Robin Quériaux, Solveig Bachellery, Léa Déléris et al. — [VERA: A Responsible AI Dashboard for Assessing LLM Deployments in Light of the EU AI Act](http://arxiv.org/abs/2610.31588v1)
  <details><summary>📄 Abstract</summary>
  Institutions that deploy large language models in regulated settings often need technical evidence of responsible AI practices before approving a deployment. COMPL-AI provides a technical interpretation of the EU AI Act that organises this evidence under six principle groups and eighteen technical requirements, twelve of which current benchmarks can measure. The benchmark suites that produce this evidence are typically operated from a command line, while the staff who approve deployments are non...
  </details>

- **2026-10-22** — Yusuke Kumagae, Masahiro Kaneko — [Silicon Samples Match the Answers but Not the Respondents](http://arxiv.org/abs/2610.30900v1)
  <details><summary>📄 Abstract</summary>
  Silicon sampling generates survey respondents by having a large language model (LLM) answer a survey as a person with given demographic attributes, and the resulting synthetic populations are increasingly used in place of human ones. Existing evaluations focus on individual-answer accuracy, per-question answer distributions, and correlations across questions. None of these compares the respondents themselves, so a generator whose respondents have combinations of answers found in no human respond...
  </details>

- **2026-10-22** — Zihan Chen, Lei Nico Zheng, Di Zhu — [Abstract Priorities, Concrete Rewards: How Stated Preferences Relate to What People Reward in AI Responses](http://arxiv.org/abs/2610.30763v1)
  <details><summary>📄 Abstract</summary>
  AI assistants built on large language models (LLMs) are trained on human feedback and increasingly personalized to users' stated preferences. Yet how closely these preferences reflect what people reward in responses remains unclear. We compare stated and revealed preferences in the public PRISM dataset, in which 1,396 participants reported how much seven response attributes mattered to them and then rated 29,347 responses from 21 LLMs. Among responses to the same prompt, features the survey neve...
  </details>

- **2026-10-21** — Esko Lehtonen, Tommi Buder-Gröndahl — [LLMs as survey respondents: Comparison to simple semantic baselines](http://arxiv.org/abs/2610.29645v1)
  <details><summary>📄 Abstract</summary>
  Large language models (LLMs) have been explored as surrogates for human survey respondents. A more promising application is data augmentation, where LLMs predict new responses from partial human data. However, the semantic similarity between questionnaire items is a known source of correlation between answers. It is thus unclear whether LLMs actually infer meaningful relationships between question-response pairs, or use surface-level comparison between questions as a heuristic. To assess this, w...
  </details>

- **2026-10-21** — Dongfang Li, Zhuoen Chen, Bonian Jia et al. — [Memory-Centric Continual Learning for AI Agents](http://arxiv.org/abs/2610.29357v1)
  <details><summary>📄 Abstract</summary>
  Autonomous agents powered by foundation models can reason, plan, and use tools, but their fixed weights and context limits hinder sustained learning from experience over long-term deployment. While external memory systems attempt to bridge this gap, they mostly act as passive retrieval caches, evaluated primarily by whether they can recall stored facts or past interactions. Whether memory can drive genuine continual learning remains an open question. In this paper, we introduce Memory-Centric Co...
  </details>

- **2026-10-21** — Tao Zhong, Kaison Fong, Keqin Wang et al. — [Geometric Algebra for Neural Networks: A Survey](http://arxiv.org/abs/2610.30121v1)
  <details><summary>📄 Abstract</summary>
  Geometric algebra (GA) unifies geometric primitives and transformations in a single algebraic framework. Neural networks designed around this framework often represent features as multivectors and constrain layer operations to respect the algebraic structure, enabling principled treatment of geometric transformations and, in many cases, built-in equivariance. This survey reviews geometric algebra neural networks, including their building blocks, equivariant properties, application domains, empir...
  </details>

- **2026-10-21** — M. Madarász, G. Marton, M. Audard — [Data-driven characterisation of variable source light curves with multimodal representation learning](http://arxiv.org/abs/2610.29412v1)
  <details><summary>📄 Abstract</summary>
  Surveys such as the Zwicky Transient Facility (ZTF) and the Vera C. Rubin Observatory Legacy Survey of Space and Time (LSST) produce light curves for hundreds of millions of variables. Their characterisation traditionally relies on supervised classifiers with hand-crafted features and curated labels, limiting them to predefined taxonomies and individual surveys. We present a general, survey-agnostic framework that characterises variable sources without labelled training data, producing low-dimen...
  </details>

- **2026-10-21** — Biswas Poudel, Nilson Chapagain, Amit Kumar et al. — [Reasoning-Search-Augmented LLMs: An Operational Taxonomy, Benchmark Analysis and Controlled Evidence Synthesis](http://arxiv.org/abs/2610.29189v1)
  <details><summary>📄 Abstract</summary>
  Large language models (LLMs) demonstrate impressive emergent reasoning capabilities, yet they remain constrained by fixed model parameters and finite context windows. Even when augmented with static retrieval, they can produce statements that are unsupported by, or even contradictory to, retrieved evidence. This leads to hallucinations, difficulty incorporating up-to-date information, and failures to correctly interpret or reconcile sources. Recent work addresses these limitations by tightly cou...
  </details>

- **2026-10-20** — Marc Chapus, Carlos Crispim-Junior, Véronique Eglin et al. — [CountVideoBench: A Benchmark to Evaluate Prediction Biases on the Object Counting task by Video-Language Models](http://arxiv.org/abs/2610.28356v2)
  <details><summary>📄 Abstract</summary>
  Object counting in videos remains a poorly characterized capability of multimodal large language models. Counting questions are included in many existing VideoQA benchmarks, but the ground-truth count distributions in these benchmarks are heavily skewed toward small values. Across the nine benchmarks we survey, the median ground-truth count is at most five, and the three most frequent values together account for between 45% and 93% of the videos. The resulting mean accuracy is then dominated by ...
  </details>


### 📂 other
*其他安全相关 / Other Security-Related* — 163 papers

- **2026-10-22** — Jeffrey Olmo, David Zhang, Tyler Tracy — [Simulated Control Evals](http://arxiv.org/abs/2610.31593v1)
  <details><summary>📄 Abstract</summary>
  Control evaluations measure whether safeguards can prevent an AI model from causing undesired outcomes even when it is intentionally trying to do so. These evaluations typically use purpose-built control settings and extrapolate their results to a model's deployment. However, the effectiveness of safeguards in deployment can depend on features of environments and tasks that control settings do not represent. To broaden where control evaluations can be run, we introduce simulated control evaluati...
  </details>

- **2026-10-22** — Mustafa Omer Gul, Philippe Laban, Tanya Goyal et al. — [Towards User Simulators That Stay On Task And Still Sound Natural](http://arxiv.org/abs/2610.31512v1)
  <details><summary>📄 Abstract</summary>
  Users increasingly rely on AI systems for extended, multi-turn tasks, yet evidence indicates that LLM-based system performance degrades over prolonged interaction. To evaluate and improve AI assistants in such settings, we need user simulators that faithfully follow complex user intents while exhibiting realistic conversational behavior. Existing approaches manifest a trade-off: prompted assistants can follow complex user intents but lack behavioral fidelity, while specialized user simulators be...
  </details>

- **2026-10-22** — Jialin Lu, Xiaoyu Liu, Hengrui Luo et al. — [Lean Finder V2: Semantic Search for Mathlib That Disambiguates User Queries](http://arxiv.org/abs/2610.30843v1)
  <details><summary>📄 Abstract</summary>
  We introduce Lean Finder V2, a semantic search framework for Mathlib that disambiguates user queries through complementary model-level adversarial training and input-level query rewriting. Human mathematicians and coding agents rarely search Mathlib by providing detailed context. In practice, they query short properties, notation, aliases, or hypotheses, leaving much of the intended mathematics implicit. In contrast, existing Mathlib search engines unrealistically assume context-rich queries. Th...
  </details>

- **2026-10-22** — Andrés Daniel Godoy Ortiz — [Meaning Contracts: Local Semantic Geometry in Large Language Models](http://arxiv.org/abs/2610.30715v1)
  <details><summary>📄 Abstract</summary>
  This paper studies the local geometry of semantic meaning in large language models. Current representation analyses ask whether meanings are close in embedding space, or whether linear probes separate semantic classes, but they do not characterize the within-concept local geometry: what is invariant across realizations of a single semantic factor, what varies, and what changes when meaning is refined. This paper characterizes that geometry through two controlled probes evaluated on four architec...
  </details>

- **2026-10-22** — Abderrahmane Issam, Irene E. Winther, Stefan L. Frank — [Bilingual Language Models Capture Cross-Linguistic Influence in Second-Language Reading](http://arxiv.org/abs/2610.31620v1)
  <details><summary>📄 Abstract</summary>
  While monolingual language model (LM) surprisal is widely established as a predictor of reading times, it cannot capture the non-native (L2) reading dynamics that are shaped by the reader's first language (L1). In this work, we investigate whether the cross-lingual transfer within bilingual models aligns with human L1-driven biases during L2 reading. We evaluate bilingual models on eye-tracking data of readers from 12 diverse L1 backgrounds reading English texts. To isolate L1-specific transfer,...
  </details>

- **2026-10-22** — Xuhui Zuo, Chenjie Cao, Tengfei Wang et al. — [Squaring-the-Sphere: Distortion-Free and Seamless Panorama Generation via CubeAtlas](http://arxiv.org/abs/2610.31565v1)
  <details><summary>📄 Abstract</summary>
  Generating 360-degree panoramas requires both local perspective fidelity and global spherical continuity. Existing representations face a trade-off: equirectangular projection (ERP) enables seamless panorama modeling but suffers from severe distortion and a domain gap to pre-trained image generators, whereas cubemaps preserve perspective geometry but often produce inconsistent faces and visible seams. We present Squaring-the-Sphere, a panoramic image generation framework built on a novel represe...
  </details>

- **2026-10-22** — Yun-Chen Cheng, Chih-Pin Tan, Tzu-Hung Huang et al. — [Piano2Pop: Expanding Piano Demos into Pop Productions Without Aligned Supervision](http://arxiv.org/abs/2610.31510v1)
  <details><summary>📄 Abstract</summary>
  We introduce Piano2Pop, a music-expansion task that transforms piano MIDI into instrumental pop productions. Enabled by recent advances in music generation and polyphonic music transcription, our pseudo-supervised approach conditions a pretrained flow-matching model on piano rolls without aligned piano-pop supervision. We train on synthetic piano-instrumental pairs derived from pop recordings, comparing pair-free transcription, including function-selective (FST) and register-density (RDA) augmen...
  </details>

- **2026-10-22** — Liang He, SiYuan Ma, Qishi Zhan et al. — [ValuSpec: Plug-and-Play Candidate Valuation before Target Verification for Tree-Based Speculative Decoding](http://arxiv.org/abs/2610.31338v1)
  <details><summary>📄 Abstract</summary>
  Tree-based speculative decoding accelerates large language model inference by verifying multiple candidate branches in parallel. However, in practical serving scenarios, similar requests repeatedly induce overlapping candidate branches. While retrieval-based methods mitigate this by reusing historical drafts, the resulting candidate trees often contain many low-quality branches as the candidate tree grows, which reduces verification efficiency and wastes target-side computation. To address this,...
  </details>

- **2026-10-22** — Igor' Kontorovich, Miriam N. Wallach — [What the submission does not show: Complexifying cognitive offloading in students' mathematical work with LLMs](http://arxiv.org/abs/2610.31335v1)
  <details><summary>📄 Abstract</summary>
  A common concern is that using large language models (LLMs) lets students offload mathematical work that tasks are designed to elicit. Yet such claims often rest on outcomes (e.g., submitted solutions), rather than on evidence of students' work with LLMs. We followed 23 first-year linear algebra students as they solved three differently designed homework tasks with LLMs. Drawing on self-regulated learning and choice-affluent environments, we interpreted each of 429 prompts as a trace of a regula...
  </details>

- **2026-10-22** — Jinjian Jiang, Jing Peng, Rehan Deen et al. — [Bridging the Data Gap: Source-Informed Task-Space Transport for Few-Shot Diffusion](http://arxiv.org/abs/2610.31323v1)
  <details><summary>📄 Abstract</summary>
  Many deployments require a model to move rapidly from a data-rich source to a related target observed only sparsely. This is especially consequential where target data are difficult to collect, as in healthcare settings with persistent population or acquisition imbalances. Retraining or fine-tuning a high-capacity generator for every target is costly and can be statistically unreliable when target data are scarce. We introduce Meta-Diff, which instead learns a recurring source--target relation o...
  </details>

- **2026-10-22** — Shmuel Amar, Benjamin Lieber, Ori Shapira et al. — [CoWriter: Guiding Methodological and Synergetic Human-LLM Co-Authoring](http://arxiv.org/abs/2610.31277v1)
  <details><summary>📄 Abstract</summary>
  While LLMs have transformed text generation, standard chat-and-canvas interfaces often reduce human authoring to quite passive supervision, causing review fatigue, over-reliance on AI, and the sidelining of the human role in long-form, source-grounded writing. Prior systems typically address isolated writing phases, leaving comprehensive end-to-end human-LLM collaboration largely unexplored. In this paper, we introduce CoWriter, a proactive agentic scheme that adapts expert human (co-)authoring ...
  </details>

- **2026-10-22** — Jingxuan Xu, Zihang Xu, Yuechen Luo et al. — [RIPPLE: Recovery Internalization through Process-Level Policy Learning and Effect-Aware Credit for Long-Horizon Agentic Coding](http://arxiv.org/abs/2610.31276v1)
  <details><summary>📄 Abstract</summary>
  Long-horizon coding agents can observe a failure and generate a plausible critique yet continue along the same incorrect trajectory. We call this the Critique-to-Action Handoff Gap. We introduce RIPPLE, a recovery-oriented training framework that internalizes process-level guidance into a single self-recovering policy. A prefix-only teacher provides evidence-grounded recovery supervision without access to future actions or terminal outcomes. After lightweight distillation, reinforcement learning...
  </details>

- **2026-10-22** — Yijiang River Dong, Zexue He, Cheng Yu et al. — [Memory-Aware Reward Modeling: Learning Human Preferences for LLM Memory Use](http://arxiv.org/abs/2610.31272v1)
  <details><summary>📄 Abstract</summary>
  Memory enables language model assistants to maintain continuity across sessions and generate personalized responses, but knowing more about a user does not necessarily produce responses they prefer. Existing evaluations assess memory capabilities without directly establishing whether memory use benefits the user. To study this gap, we collect approximately 1,000 pairwise judgments from 87 participants using their own ChatGPT queries and personal memories. We find that memory-conditioned response...
  </details>

- **2026-10-22** — Tianyu Lu, Kaicheng Yang, Jiangtao Feng et al. — [Trion-1: Unifying Language, Protein Sequence, and Structure with Diffusion Language Models](http://arxiv.org/abs/2610.31215v1)
  <details><summary>📄 Abstract</summary>
  We envision a general-purpose protein foundation model as a unified, interactive model of sequence, structure, and function, capable of understanding, generation, and cross-modal translation while retaining the instruction-following and reasoning capabilities of modern LLMs. Toward this vision, we introduce Trion-1, the first native, unified, multimodal diffusion language model (dLLM) for proteins. Trion-1 is built on two key design choices: (1) a unified discrete token space that jointly repres...
  </details>

- **2026-10-22** — Ronald Fecso, José Morano, Botond Fazekas et al. — [A Visual Grounding Benchmark for Retinal OCT with Multimodal Large Language Models](http://arxiv.org/abs/2610.31205v1)
  <details><summary>📄 Abstract</summary>
  Multimodal large language models (MLLMs) can answer clinical questions about medical images, but trustworthy use requires visual grounding: models should localize the pathology they report rather than rely on spurious shortcuts. Whether MLLMs can visually ground clinical findings in retinal optical coherence tomography (OCT), the most widely used imaging modality in ophthalmology, remains largely unexplored. To address this gap, we introduce RetinaGroundBench, the first benchmark for biomarker v...
  </details>

- **2026-10-22** — Aman Behera, Namit Solanki, Mehul Anand — [Mixing Matters: Evidence Position Bias Across Sequence Mixers in Long-Context Question Answering](http://arxiv.org/abs/2610.31135v1)
  <details><summary>📄 Abstract</summary>
  Long-context models often use answer-bearing evidence less effectively when it appears away from a prompt boundary. We compare this position bias across Transformer, state-space, and hybrid Mamba architectures by moving one gold document through a fixed set of nine distractors. The evaluated Transformers show a beginning advantage that the evaluated state-space models lack, while both families favor evidence near the end. A matched pure-versus-hybrid Mamba comparison points in the same direction...
  </details>

- **2026-10-22** — Roger X. Lera-Leri, Filippo Bistaffa, Athina Georgara et al. — [Constraint Reasoning and Large Language Models Join Forces: Providing Contrastive Explanations for Real-World Optimisation-Based Applications](http://arxiv.org/abs/2610.31119v1)
  <details><summary>📄 Abstract</summary>
  We focus on optimisation-based Decision Support Systems in real-world applications. In this context, we aim to provide contrastive explanations that answer users' questions about recommendations based on the solution of an optimisation problem, specifically a Mixed-Integer Program (MIP). Addressing this endeavour is crucial to ensure human oversight of the decisions implemented, as required by international guidelines on trustworthy and responsible automated decision-making systems. We propose a...
  </details>

- **2026-10-22** — Keshu Wu, Hao Zhang, Rui Gan et al. — [LAST-V2X: Language-Driven Adaptive Scenario Synthesis and Testing for Communication-Induced Failures in V2X Safety Applications](http://arxiv.org/abs/2610.30979v1)
  <details><summary>📄 Abstract</summary>
  Vehicle-to-everything (V2X) communication enables connected vehicles to make safety-critical decisions, but delayed, missing, or incorrect information can compromise driving safety. Systematically testing such failures is challenging because traffic interactions, communication conditions, and application responses must be jointly configured to produce meaningful scenarios. This paper presents LAST-V2X, a language-driven, adaptive framework for automated scenario synthesis and safety testing of V...
  </details>

- **2026-10-22** — Zhongkai Shangguan, Yanbin Kang, Yihan Cao et al. — [PAIR: Preference-Aligned Intent Retrieval for Premium People Recommendation at LinkedIn](http://arxiv.org/abs/2610.30941v1)
  <details><summary>📄 Abstract</summary>
  General-purpose embeddings trained on profile similarity often misrank candidates in professional networks, where relevance is inherently complementary rather than symmetric. For example, job seekers usually engage with recruiters rather than peers with similar credentials. Current user recommendation systems are often built on profile similarity or social signals such as shared connections, which are effective in friend-oriented social networks where users tend to connect with similar people or...
  </details>

- **2026-10-22** — Ahmed M. Mahran — [What Lies Beyond Perception: A Partition Theory of the Limits of AI Evaluation and Oversight](http://arxiv.org/abs/2610.30803v1)
  <details><summary>📄 Abstract</summary>
  Replacing the judge can move a benchmark score, and models can be trained to hide capabilities. Both put the evaluator in question: what can it certify? We develop a partition theory of evaluation from one principle: judgement is bounded by perception. An agent's discrimination is the partition of its inputs into classes it cannot tell apart. Discrimination is necessary for capability but not sufficient, so bounds on it bear directly on whether evaluation can show that a model lacks an ability. ...
  </details>

- **2026-10-22** — Shijie Li, Yilin Gao, Tieyuan Chen et al. — [GIFT: Gradient Informed Filtering for Distillation Augmented Reasoning RL](http://arxiv.org/abs/2610.30796v1)
  <details><summary>📄 Abstract</summary>
  Training large language models for complex reasoning tasks relies on two complementary signals: sparse, outcome-grounded reinforcement learning (RL) for correctness, and dense, token-level distillation for guidance. However, complementarity in supervision does not guarantee compatibility in optimization; imitation-focused distillation can conflict with the outcome-driven RL objective, and existing hybrids lack a principled resolution. We propose \textbf{GIFT} (\textbf{G}radient-\textbf{I}nformed...
  </details>

- **2026-10-22** — Christian Arnold, Ernesto Calvo, Guadalupe Gonzalez et al. — [Invisibilization as a Source of Probability Bias in Language Models](http://arxiv.org/abs/2610.30785v1)
  <details><summary>📄 Abstract</summary>
  Language models are aligned to avoid using protected attributes such as race, ethnicity, and gender to inform their responses. Therefore, they increasingly refuse or hedge when such attributes appear in a prompt. However, if a system must decide how much to learn from what people tell it, it is costly to refuse valuable information because of its source. In this article, we measure the cost of declining information in a two-urn game with an exact Bayesian answer. We present leading LLM models fr...
  </details>

- **2026-10-22** — Jinyi Zhou, Zenan Li, Yuan Yao et al. — [RAIN: Agentic Proof Generation for Rocq-based Software Verification](http://arxiv.org/abs/2610.30759v1)
  <details><summary>📄 Abstract</summary>
  Interactive theorem provers can provide strong correctness guarantees for software, but constructing the proofs remains a challenging and labor-intensive task. Inspired by the recent progress of modern coding agents, we present RAIN, a lightweight proof-specialized agent for Rocq proof generation. RAIN augments an LLM with proof engineering capabilities, including repository exploration, iterative refinement, and checker feedback. This design allows the agent to retrieve lemmas autonomously, rev...
  </details>

- **2026-10-22** — Yang Liu, Zhiqiang Yuan, Shu-Dong Huang et al. — [ULME: Predictive Coupling for Mutually Reinforcing Embedding and Language Modeling](http://arxiv.org/abs/2610.30705v1)
  <details><summary>📄 Abstract</summary>
  Text embedding and text generation are two of the most useful capabilities of modern large language models, yet they are typically provided by separate specialized models (an embedder and a generator) trained with incompatible objectives and deployed side by side in retrieval-augmented generation and agent systems. Recent unified embedding-generation models such as GritLM share parameters between the two capabilities, but they either switch attention regimes between modes or optimize embedding a...
  </details>

- **2026-10-22** — Qince Luan, Jianhui Xu, Yang Xu — [Spectral Smoothing and Spiking Perturbations Reconfigure Capability Profiles and Selective Task Performance in Large Language Models](http://arxiv.org/abs/2610.30676v1)
  <details><summary>📄 Abstract</summary>
  Singular-value spectra encode important structure in transformer feed-forward projections, yet their causal role in downstream behavior remains underexplored. We study post-hoc spectral smoothing and spiking interventions on the up_proj and down_proj matrices. Positive perturbation stretches deviations from the geometric mean, making large singular values larger and small ones smaller (spiking), and vice versa. The intervention preserves singular vectors and the geometric mean of the singular va...
  </details>

- **2026-10-22** — Siran Dai, Qianqian Xu, Peisong Wen et al. — [CODI: Improving Self-Supervised Vision Transformers with Cross Distillation](http://arxiv.org/abs/2610.30639v1)
  <details><summary>📄 Abstract</summary>
  Self-supervised Vision Transformers learn strong image-level representations, but their patch-level representations can be unreliable for dense prediction. We study this mismatch and find that the class token concentrates global semantics on a small number of representative patches, while dense prediction errors often occur on low-attention regions. We provide a local gradient analysis showing that, along the [CLS] attention readout, image-level self-distillation gradients are weighted by [CLS]-...
  </details>

- **2026-10-22** — Jia Gu, Guofeng Zhang, Ian R. Petersen — [On the Structure of Quantum Finite-Level Systems: Decoherence-Free Subsystems, Quantum Nondemolition Variables, and Back-Action-Evading Measurements](http://arxiv.org/abs/2610.30616v1)
  <details><summary>📄 Abstract</summary>
  The purpose of this paper is to conduct a comprehensive structural analysis of quantum finite-level systems in the Heisenberg picture, where the evolution of system observables is modeled by bilinear quantum stochastic differential equations (QSDEs). Firstly, real coordinate transformations that preserve commutation and anticommutation relations are characterized, and relative admissibility between different orthonormal Hermitian bases is formulated. Secondly, strongly aligned subspaces are intr...
  </details>

- **2026-10-22** — Chenyao Yang, Peijin Wang, Yingchao Feng et al. — [KinoUAV: A Benchmark for Safe and Stable UAV Vision-Language Navigation with Kinodynamic Modeling](http://arxiv.org/abs/2610.30609v1)
  <details><summary>📄 Abstract</summary>
  Unmanned aerial vehicles (UAVs) have recently emerged as important remote sensing platforms, and UAV navigation has shown great potential in remote sensing applications. However, existing methods do not explicitly incorporate kinodynamic modeling or safety distances into trajectory generation, resulting in high absolute yaw rates, frequent collisions, and low navigation success rates, which limit safety and motion stability. To address this challenge, we introduce KinoUAV, a kinodynamic benchmar...
  </details>

- **2026-10-22** — Chihiro Matsui — [Hierarchical Reduction of Invariant Subspaces: From Fragmentation to Many-Body Scars](http://arxiv.org/abs/2610.30597v1)
  <details><summary>📄 Abstract</summary>
  We investigate a hierarchy of invariant Hilbert-space structures connecting Hilbert-space fragmentation, partial solvability, and quantum many-body scars. For spin chains with fragmented spin-$1/2$ subspaces and their local deformations, we show, using the spin-$1$ $XXC$ chain as a representative example, how successive local deformations reduce extensive irreducible-string fragmentation through an implicitly embedded spin-$1/2$ invariant space and ultimately to a single scar tower, connecting t...
  </details>

- **2026-10-22** — David Arthur, Ranjini Grove, Zaher Kmail et al. — [DagFlow AI: Agentic Synthetic Data Generation for Personalized Statistics Learning](http://arxiv.org/abs/2610.30580v1)
  <details><summary>📄 Abstract</summary>
  To provide personalized learning experiences in courses that teach data analysis skills, instructors often search for datasets that appeal to a student's interests, align with specific learning objectives, and are appropriate for the student's skill level. Datasets that match all three criteria can be difficult to find. DagFlow-AI is an agentic AI data generation tool that creates realistic, synthetic datasets tailored to these criteria. Rather than mimicking existing datasets or generating obse...
  </details>

- **2026-10-22** — Tao Lin, Yuxin Du, Haoxiao Wang et al. — [FastHarness: Experience-Driven Review Scheduling for Vision-Language-Action Policies](http://arxiv.org/abs/2610.31427v1)
  <details><summary>📄 Abstract</summary>
  Agentic robot systems combine language-model reasoning with robot policies to monitor execution and recover from failures. However, reviewing every action chunk incurs substantial overhead, even in familiar situations. We introduce FastHarness, an experience-driven execution harness that adaptively schedules GPT-6 Astra supervision of a π0.5 policy. A fast path uses stage memory and reviewed outcomes to reduce review frequency as experience accumulates, while a complementary recovery path focuse...
  </details>

- **2026-10-22** — Aleksandr Lazarev, Sofia Zimina, Roman Kuznetsov et al. — [RGraph-Eval: Task-Grounded Scene Graphs for Evaluating Robot Video Generation](http://arxiv.org/abs/2610.31121v1)
  <details><summary>📄 Abstract</summary>
  Generated robot videos can look convincing while depicting the wrong interac- tion: a different object is moved, a grasp disappears, or a placement ends out- side its destination. We introduce RGraph-Eval, a reference-based framework that makes these discrepancies explicit through task-grounded temporal scene graphs. Unlike approaches that construct separate evidence representations for different evaluation dimensions, we organize task entities, interactions, and motion within a unified, interpr...
  </details>

- **2026-10-22** — Firuz Kamalov, Hana Sulieman, Ahmed El Sayed et al. — [Algorithmic drift in generative adaptive learning](http://arxiv.org/abs/2610.31041v1)
  <details><summary>📄 Abstract</summary>
  Generative artificial intelligence promises to democratize personalized tutoring, yet the longitudinal stability of adaptive systems remains under-theorized. Current ethical discourse focuses on static bias. This paper argues that a distinct threat lies in algorithmic drift: a feedback loop in which minor, demographically asymmetric observation errors compound over time into systemic inequities. We make three contributions. First, we formalize algorithmic drift as a coupled learner--tutor dynami...
  </details>

- **2026-10-22** — Jialin Tian, Zhuofan Li, Xinkai Wang et al. — [UniFlowWAM: A Unified World-Action Model with Visual Semantics and 4D Geometry](http://arxiv.org/abs/2610.30991v1)
  <details><summary>📄 Abstract</summary>
  Robot demonstrations record what the robot saw and what it did. They do not specify how the 3D world changed in between. Scene-level 3D flow describes it by tracking 3D scene points, providing the world representation with 4D geometry. Prior work has used flow to improve robot policies. Flow served as an intermediate prediction that a separate model converts into actions, as a prior injected at inference time, or as an extra output learned together with the action. In all of these designs, flow ...
  </details>

- **2026-10-22** — Jingyu Ru, Xiangyuan Xie, Lixuan Jin et al. — [Adaptive Aerial Loco-Manipulation Policy Learning via LLM-Assisted Proactive Task Generation](http://arxiv.org/abs/2610.30810v1)
  <details><summary>📄 Abstract</summary>
  Loco-manipulation extends the workspace of conventional manipulation by combining mobility with physical interaction, while aerial loco-manipulation further expands this capability into three-dimensional space, enabling robots to reach environments inaccessible to ground-based systems. Moving to an aerial platform, however, gives rise to a demanding control problem, since the vehicle must track trajectories accurately in three dimensions while the motion of the arm and its interaction with the e...
  </details>

- **2026-10-22** — Fanxing Li, Yuxiang Huang, Shengyang Wang et al. — [DiffDreamer: Coupling World Models with Differentiable Simulation for Agile Quadrotor Control](http://arxiv.org/abs/2610.31617v1)
  <details><summary>📄 Abstract</summary>
  Tasks such as quadrotor dynamic-gate racing require agents to anticipate external motion while maintaining precise high-frequency control. World-model-based reinforcement learning provides a natural solution by learning latent dynamics for future imagination, yet it often entangles environmental evolution and the robot's own dynamics in a single learned rollout, where model bias can affect policy optimization efficiency. We propose DiffDreamer, a differentiable reinforcement learning framework t...
  </details>

- **2026-10-22** — Viktor Stein, Levin Maier, Wuchen Li et al. — [SympFormer: Inertial Attention Blocks from Damped Hamiltonian Dynamics on Spaces of Probability Measures](http://arxiv.org/abs/2610.31600v1)
  <details><summary>📄 Abstract</summary>
  The attention mechanism underpins modern large language models, yet their dynamics remain only partially understood. Recent perspectives interpret attention blocks as interacting particle systems, whose mean-field limits correspond to gradient flows of energy functionals on spaces of probability densities on $\mathbb R^d$ equipped with Wasserstein-type metrics. We extend this viewpoint by deriving accelerated attention blocks from inertial, Nesterov-type damped Hamiltonian dynamics on these dens...
  </details>

- **2026-10-22** — Bo Xiong, Weisheng Chen, Zongen Ren et al. — [CAMGen: A Core Change-Aware Multi-View Framework for Commit Message Generation](http://arxiv.org/abs/2610.31552v1)
  <details><summary>📄 Abstract</summary>
  Commit messages help developers understand code changes and support software maintenance. Recent approaches use repository context to improve commit message generation (CMG) with large language models (LLMs). However, existing CMG methods provide limited support for understanding how local edits affect functionality jointly implemented by multiple code entities. This functional understanding is essential for generating commit messages that explain the main change and its impact. To address this ...
  </details>

- **2026-10-22** — Shihui Li, Mette Andersen, Martha Lewis — [The Geometry of Metaphor: Probing and Steering Metaphor Representations in Large Language Models](http://arxiv.org/abs/2610.31520v1)
  <details><summary>📄 Abstract</summary>
  Metaphor is a crucial aspect of human cognition. As such, we would like to understand how it is represented in large language models (LLMs) and how it might be controlled. We use mechanistic interpretability techniques to identify causal subspaces in a range of LLMs covering different architectures and sizes. We show that we are able to steer output on classification tasks across different parts of speech. We are also able to steer output on generation tasks, indicating that these techniques can...
  </details>

- **2026-10-22** — Advait Gupta, Sachin Konan, Tom Yin et al. — [AgentVQA: A Unified Benchmark for Agentic Visual Understanding](http://arxiv.org/abs/2610.31494v1)
  <details><summary>📄 Abstract</summary>
  Vision-language models (VLMs) can perform a broad range of tasks across diverse settings, yet their performance in agentic contexts remains poorly understood. Although online evaluations in simulators and real-world environments are essential for measuring interactive agent performance, they are costly and challenging to scale. Complementary offline VQA benchmarks can enable faster and more reliable comparisons across agentic domains, yet existing benchmarks remain limited and fragmented. To add...
  </details>

- **2026-10-22** — Vladimir V. Rybkin — [Unifying Time-Independent and Time-Dependent Franck--Condon Pictures in Quantum Mechanochemistry via the Linear Coupling Approximation](http://arxiv.org/abs/2610.31426v1)
  <details><summary>📄 Abstract</summary>
  Quantum chemistry has achieved impressive results in modeling and interpreting mechanochemical transformations at the molecular level. An essential question, the time profile of force application, has   however attracted less attention. Here, the Franck--Condon theory   of quantum mechanochemistry, previously formulated for the   sudden-force limit, is generalized to arbitrary time-dependent   force profiles using the linear-coupling approximation. Solving the   driven harmonic oscillator yields...
  </details>

- **2026-10-22** — Ferdinand Kapl, Kaitlin Maile, Stefan Bauer et al. — [How Depth Growth and Looping Shape In-Context Learning in Language Models](http://arxiv.org/abs/2610.31421v1)
  <details><summary>📄 Abstract</summary>
  Looped and depth-grown language models reuse computations across depth and have attracted interest for their reasoning capabilities. Building on prior suggestive evidence of improved in-context-learning (ICL), we investigate how such reuse favors ICL, including how it shapes the acquisition, retention, and mechanisms of this ability. Our analysis spans pretrained language models up to 3B parameters and controlled tasks. The experiments provide evidence for a shared inductive bias toward learning...
  </details>

- **2026-10-22** — João Kenji Suwa, João Pedro Silveira e Silva, Bruno Iochins Grisci — [Post-Hoc Feature Selection Layer for Neural Networks Interpretability](http://arxiv.org/abs/2610.31420v1)
  <details><summary>📄 Abstract</summary>
  The interpretability of complex neural networks remains a critical challenge, especially for models already deployed in high-stakes domains. To address this, we adapted the Feature Selection Layer (FSL) to optimize feature weights post-training, a variant we term post-hoc FSL. Our approach reframes the FSL as a lightweight, trainable module that integrates with already frozen pre-trained models on tabular datasets to highlight the features the original model considers most important. This post-h...
  </details>

- **2026-10-22** — Tammy Schmidt, Luise Koch — [In-Browser Human-AI Co-Writing for Counterspeech: An Exploratory User Study of Agency, Perceived Response Quality, and Time](http://arxiv.org/abs/2610.31357v1)
  <details><summary>📄 Abstract</summary>
  Writing counterspeech that challenges online hate speech can be cognitively and emotionally demanding, whereas fully automated generation may weaken users' sense of voice and responsibility. We present an in-browser AI-assisted co-writing tool that enables users to contribute their own ideas and offers three editable suggestions generated by a large language model using dynamically retrieved hate speech-counterspeech examples from the Multitarget CONAN dataset. We evaluated the tool in an explor...
  </details>

- **2026-10-22** — Kaiyuan Wu, Aditya Nagori, Nicoleta J. Economou et al. — [ClinGuard: a governance framework for reliable, transparent, and auditable clinical coordination](http://arxiv.org/abs/2610.31354v1)
  <details><summary>📄 Abstract</summary>
  ClinGuard is a model-agnostic governance framework that treats clinical coordination as patient-scoped, policy-bound transactions rather than free text. An independent sentinel layer validates and governs agent-proposed actions, escalates when needed, and executes approved actions through limited-privilege connectors. Each transaction is linked to a tamper-evident audit record, while an outcomes monitor informs future autonomy decisions. Using MIMIC-IV-FHIR and skilled-nursing-facility placement...
  </details>

- **2026-10-22** — Tariq Mahassen, Marcin Jastrzebski, Oleksandr Kyriienko — [Quantum Fokker-Planck solvers as trainable generative models](http://arxiv.org/abs/2610.31330v1)
  <details><summary>📄 Abstract</summary>
  We develop and analyze generative models based on quantum solvers of stochastic differential equations. Unlike the common approach based on layered variational quantum circuits with parameterized rotations, we parameterize the potential of a Langevin process. The associated Fokker-Planck (FP) equations are Hermitianized and solved using a linear combination of cosine operators implemented through quantum singular value transformation. By encoding the square root of the stationary density, the mo...
  </details>

- **2026-10-22** — Wenhua Jin, Tiancheng Chen, Sheng Tang et al. — [Moving Regions, Not Moving Objects: Segmenting What Actually Moves under Camera Motion](http://arxiv.org/abs/2610.31209v1)
  <details><summary>📄 Abstract</summary>
  Moving object segmentation is conventionally formulated at the sequence and object level, marking an entire instance as moving once it moves anywhere in a video. Recent instantaneous formulations distinguish moving from stationary intervals, but still generate masks at the object level through frozen segmentation foundation models. Because the mask is derived from an instance-level proposal, motion is typically attributed to the entire instance rather than localized to the regions that actually ...
  </details>

- **2026-10-22** — Felix Saretzky — [PriMa-Causa: Causal Prescriptive Maintenance](http://arxiv.org/abs/2610.31147v1)
  <details><summary>📄 Abstract</summary>
  Automated manufacturing requires data-driven decisions under uncertainty and sparse observational records, and unplanned downtime is a dominant cost of getting them wrong. Prescriptive maintenance recommends a maintenance action against an impending failure rather than merely predicting it. Established reference architectures couple predictive models with rule- or optimisation-based recommendation logic. Selecting a corrective action, however, requires an interventional quantity: how the line be...
  </details>

- **2026-10-22** — Gouki Minegishi, Jingyuan Feng, Hiroki Furuta et al. — [Who Is the Influencer? Consensus Dynamics in Multi-Agent Systems](http://arxiv.org/abs/2610.31105v1)
  <details><summary>📄 Abstract</summary>
  Multi-agent LLM systems are increasingly used in practice, but their behavior is complex and hard to understand. We design a simple task to ask which model has the most influence on the final consensus when several models are mixed in one system. Experimentally, across seven model families, we find that the opinions of the other models are absorbed into the opinion of the stronger model, the one with more parameters. This happens even though the task requires no pretraining knowledge and has no ...
  </details>

- **2026-10-22** — Md. Jalil Piran — [Evaluating Artificial Wisdom (AW): A Trajectory-Based Framework for Context-Sensitive Decision Regulation](http://arxiv.org/abs/2610.31012v1)
  <details><summary>📄 Abstract</summary>
  Capability benchmarks measure what large language models can do, but not whether their recommendations remain appropriate as decision conditions change. This paper proposes a trajectory-based measurement framework and prospective validation protocol for artificial wisdom, defined behaviorally as context-sensitive regulation of judgment. Versioned reference specifications determine admissible responses and transition materiality before evaluation. Seven stage-level criteria assess judgment under ...
  </details>

- **2026-10-22** — Leyuan Jin, Jiahao Mei, Yixuan Yuan et al. — [EEG-Captioner: Grounding EEG-to-Language Generation in Fundamental Signal Properties](http://arxiv.org/abs/2610.30995v1)
  <details><summary>📄 Abstract</summary>
  Electroencephalography (EEG)-to-language models offer a promising approach for translating complex neural signals into human-readable descriptions. However, generating plausible language does not necessarily demonstrate that a model has learned to interpret the underlying EEG signal. A direct way to assess such interpretation is to probe objectively measurable properties of the signal itself. We therefore construct an EEG-language dataset of 160,781 segments annotated with signal-level question ...
  </details>

- **2026-10-22** — Shin Yamaguchi, Masaya Taniguchi, Tatsuki Kuribayashi et al. — [Once a Tree, Always a Tree? Cross-lingual Transfer of Hierarchical Generalization in Language Models](http://arxiv.org/abs/2610.30960v1)
  <details><summary>📄 Abstract</summary>
  Language models (LMs) often exhibit successful cross-lingual transfer through continued (pre)training, still their underlying process remains unclear. One possibility is that LMs can leverage the evidence toward language-universal principles, namely, hierarchical structure, from a source language (L1) to a new language (L2), while many other non-linguistic explanations, e.g., improved initialization of position embeddings, can be potentially possible. In this study, to quantify the cross-linguis...
  </details>

- **2026-10-22** — Songlin Yang, Zhe Wang, Xiaotong Zhao et al. — [Making MLLM Latents Matter: Factor-Aware Predictive Learning for Cinematic Video Generation](http://arxiv.org/abs/2610.30926v1)
  <details><summary>📄 Abstract</summary>
  Cinematic video generation requires both temporal inference from limited inputs (i.e., sparse rather than frame-by-frame guidance) and factor-aware control of character, scene, action, and camera. Multimodal large language models (MLLMs) offer useful priors for both capabilities, but their representations are not automatically actionable for video generation: a Video Diffusion Transformer (DiT) may bypass them through native conditioning pathways, and using them does not ensure either factor-awa...
  </details>

- **2026-10-22** — Lorenzo Mensi, Simone Cuonzo, Maria Chiara Angelini et al. — [Learning Cole-Hopf Coordinates for Stochastic Growth Dynamics: the KPZ class](http://arxiv.org/abs/2610.30919v1)
  <details><summary>📄 Abstract</summary>
  Inferring effective equations from observations of nonlinear stochastic processes is challenging because individual trajectories are noisy realizations, while the relevant physical information is encoded in ensemble statistics. We introduce a data-driven framework that learns a change of variables in which nonlinear stochastic dynamics become linear. The model combines a neural change of representation with a linear stochastic latent evolution and is trained through a short-time moment-matching ...
  </details>

- **2026-10-22** — Barbara Weber, Olaf Zimmermann, Marco Franceschetti — [When Code Gets Cheap, Evaluation Gets Scarce: An Experience Report on AI-Assisted Agile Software Engineering](http://arxiv.org/abs/2610.30916v1)
  <details><summary>📄 Abstract</summary>
  Coding assistants are widely reported to speed up code production; most accounts stop there. We report the end-to-end construction and deployment of a compliance-critical, human-in-the-loop exam-grading system, built by a single developer who wrote no code by hand, protected by a gated process from stakeholder persona to audited behavior. The initial system was built in three working days and could grade a real cohort. We draw one claim from this experience: AI changes software engineering less ...
  </details>

- **2026-10-22** — Yuhang Xie, Cheng Li, Chenliang Li et al. — [Building Presentation Intelligence for High-Quality Slide Generation](http://arxiv.org/abs/2610.30888v1)
  <details><summary>📄 Abstract</summary>
  PowerPoint presentations (PPTs) are a dominant medium for communication across diverse domains, yet high-quality PPT generation still depends heavily on labor-intensive human effort. Recent advances in large language models (LLMs) for agentic tasks have created both new opportunities and challenges (Chen et al., 2026) for automatic PPT generation. In this work, we present a unified training framework for automatic PPT generation toward presentation intelligence, integrating cross-validated data ...
  </details>

- **2026-10-22** — Albert Linda, Shiv Shankar, Dierk Raabe — [Designing sustainable high-entropy alloys directly from mixed oxides: A thermodynamic perspective](http://arxiv.org/abs/2610.30870v1)
  <details><summary>📄 Abstract</summary>
  Hydrogen-based direct reduction (HyDR) of mixed oxide precursors offers an alternative route to produce sustainable alloys, bypassing the sequential extraction, refining, and remelting steps that dominate the carbon footprint of conventional metallurgy and individual metal production. However, the thermodynamic limits and most effective H$_2$/H$_2$O ratio needed for full metallization of multicomponent oxides are not yet established. This is because the formation of metallic and oxide solid solu...
  </details>

- **2026-10-22** — Tobias Göbel, Miranda C. N. Cheng — [Bifurcations from Weight Space: JEPAWG on Parametric Dynamical Systems](http://arxiv.org/abs/2610.30847v1)
  <details><summary>📄 Abstract</summary>
  Trained network weights are increasingly treated as data, but there is rarely ground truth about what a population of models should encode, which hampers systematic validation of weight-space methods. This makes parametric dynamical systems a natural test-bed: the dynamics change qualitatively at submanifolds of parameter space that are, in well-studied families, known analytically or numerically. Fine-tuning a forecasting network at each point of a parameter grid yields a model zoo indexed by a...
  </details>

- **2026-10-22** — Bin Duan, Jintao Lin, Guowei Yang — [VLTest: Finding Joint Image-Text Failures in Vision-Language Models](http://arxiv.org/abs/2610.30794v1)
  <details><summary>📄 Abstract</summary>
  Vision-language models (VLMs) are increasingly embedded in software systems. Testing them raises two problems. Mutating either input can change the expected answer, so an output change is not by itself a failure. Some failures appear only when both inputs are mutated; attributing them to the combination requires testing each mutation alone. We present VLTest, a black-box VLM testing approach. It generates image variants by editing VQGAN latent codes and text variants with a rewrite-expand-prune ...
  </details>

- **2026-10-22** — Yiming Zhang, Jiarui Guo, Haojia Wei et al. — [FilmFlow: Agentic System for 3D Virtual Film Cinematography](http://arxiv.org/abs/2610.30753v1)
  <details><summary>📄 Abstract</summary>
  Complex camera motion is central to visual storytelling, yet translating cinematographic intent into controllable, executable camera trajectories remains challenging. We introduce FilmFlow, an agentic framework that converts natural-language instructions or reference videos into explicit camera trajectories for dynamic 3D environments. To generate these trajectories, a Director agent constructs executable camera plans by composing high-level motions from concurrent atomic operations that jointly...
  </details>

- **2026-10-22** — Ryugo Morita, Shunsuke Kitada, Stanislav Frolov et al. — [Where Did the Light Come From? Diagnosing Cast-Shadow Reasoning in VLMs and Borrowing the Missing Shadow Prior from Image Generation Models](http://arxiv.org/abs/2610.30740v1)
  <details><summary>📄 Abstract</summary>
  Shadows are observable consequences of latent physical causes, arising from the interaction between illumination, object geometry, and scene structure. A model that understands shadows should be able not only to read a shadow's direction, but also to infer where a shadow should fall when it is absent, and to judge whether a shadow is physically consistent with the scene. We introduce ShadowBench, built from real photographs, which poses these three questions to vision-language models (VLMs). Fro...
  </details>

- **2026-10-22** — Guangcan Li, Shuyuan Zheng, Jiayao Liu et al. — [Automated Enrichment Analysis with GraphRAG: Efficient Multi-Database ORA Extraction and Biological Interpretation](http://arxiv.org/abs/2610.30710v1)
  <details><summary>📄 Abstract</summary>
  Over-representation analysis (ORA) is widely used to interpret gene-expression studies, but its outputs are often fragmented across gene-set databases and presented as flat term lists that obscure gene-level links among related enrichment signals. We propose Graph-Based Over-Representation Retrieval-Augmented Generation (GBOR-RAG), an integrated and traceable framework for ORA interpretation. GBOR-RAG represents heterogeneous gene-set databases as a unified term--gene knowledge graph, where shar...
  </details>

- **2026-10-22** — Kento Haneda, Yosuke Kishinami, Ryo Fujii et al. — [WikiOriginQA: Automated Construction of a QA Dataset with Knowledge Origins for Analyzing Cultural Bias](http://arxiv.org/abs/2610.30677v1)
  <details><summary>📄 Abstract</summary>
  Existing datasets on cultural knowledge have been typically created by human annotators familiar with each culture. However, the process requires considerable human effort, presenting a significant challenge to scalability. To address this challenge, we introduce WikiOriginQA, a QA dataset automatically constructed by objectively representing the origins of knowledge through the creation dates of different Wikipedia language editions. Experimental results with the created dataset confirm that LL...
  </details>

- **2026-10-22** — Tim Wenjie Hu, Evelyn Nafula Ouma, Benjamin Akera et al. — [Group Relative Policy Optimisation Improves Multilingual Speech Recognition in Low-Resource Languages](http://arxiv.org/abs/2610.30663v1)
  <details><summary>📄 Abstract</summary>
  Autoregressive encoder-decoder speech recognition models trained with teacher forcing can suffer from exposure bias, limiting their ability to recover from their own prediction errors at inference time. Recent work has shown that reinforcement learning with Group Relative Policy Optimisation (GRPO) improves speech recognition in major languages with LLM-based models. We extend this line of work to smaller, non-LLM encoder-decoder ASR models, using Whisper-large-v3 as a case study across 51 Afric...
  </details>

- **2026-10-22** — Minjun Kim, Jong Hak Moon — [CoRE: Relating Fine-Grained Chest X-ray Findings in Anatomical Context](http://arxiv.org/abs/2610.30584v1)
  <details><summary>📄 Abstract</summary>
  Chest X-ray interpretation depends on both the anatomical location of findings and their relationships with other abnormalities. However, relations defined over global finding labels do not explicitly distinguish the same finding across anatomical locations. We propose CoRE(Co-occurrence-guided Region Evidence), a framework that incorporates relationships among findings and anatomical context into fine-grained chest X-ray prediction. It groups anatomical region-finding labels by co-occurrence an...
  </details>

- **2026-10-22** — Xiaonan Xu, Wenjing Wu — [Stale Instruction Files Override the Code in Coding Agents: A One-Sentence Fix](http://arxiv.org/abs/2610.30571v1)
  <details><summary>📄 Abstract</summary>
  Purpose: Coding agents follow a project's instruction file, such as CLAUDE.md or AGENTS.md, even when it disagrees with the existing code and even when they notice the disagreement. We measure this behaviour and test whether one sentence in the user's own instruction file makes agents follow the code instead.   Methods: We built 40 Python projects in which the instruction file asks for one convention while the existing code uses another, for example print instead of logging. Claude Code and Code...
  </details>

- **2026-10-21** — Rujun Han, Yufan Zhuang, Arijit Ray et al. — [PLE: Physical-Engineering's Last Exam](http://arxiv.org/abs/2610.30537v1)
  <details><summary>📄 Abstract</summary>
  Frontier language models now score above 90% on popular knowledge benchmarks and are increasingly deployed as agents that carry out multi-hour professional work. Yet no existing benchmark tests whether they can perform the real-world, economically valuable work of a professional physical engineer, such as modelling physics and legal code requirements across a multi-format project corpus, optimising material and installation costs, and issuing 2D/3D engineering design packages that a licensed rev...
  </details>

- **2026-10-21** — Chakshu Gupta — [Rank Ceiling for Twiddle-Perturbation Faults on the Forward NTT](http://arxiv.org/abs/2610.30383v1)
  <details><summary>📄 Abstract</summary>
  NIST standardised ML-KEM and ML-DSA in 2024 for post-quantum key establishment and digital signatures. Both compute forward number-theoretic transforms (NTTs) on secret polynomials. Published attacks zero every fixed multiplier, or twiddle, during Kyber key generation with a single fault, or individual twiddles in one Dilithium signing variant; countermeasures detect or mask these faults. Nonzero replacements preserve invertibility, but the uncompressed correct-minus-faulted transform difference...
  </details>

- **2026-10-21** — Lei Zhang, Mingrui Jing, Yusheng Zhao et al. — [Lean-QuantumAlg: A Framework for AI Agents to Produce Quantum Algorithms that Humans Can Trust](http://arxiv.org/abs/2610.30216v1)
  <details><summary>📄 Abstract</summary>
  AI agents are increasingly capable of constructing quantum algorithms and proofs, yet machine-checked proofs alone cannot guarantee that the intended problem is solved or that resource claims match the verified computation.Here we introduce Lean-QuantumAlg, a Lean 4 framework for trustworthy AI-assisted development of quantum algorithms.Its Algorithm-Solves-Problem contract binds correctness, success probability, borrowed-state restoration and quantum and classical resource bounds to a single ex...
  </details>

- **2026-10-21** — Yan Wang — [TraceForge: Distilling with Your Own Thinking](http://arxiv.org/abs/2610.29680v2)
  <details><summary>📄 Abstract</summary>
  Using an LLM to generate training data for another is among the most general ways to train one, and it remains common practice. Some frontier teams have closed that route for their own models: what comes back is an answer, or a short summary, without the detailed reasoning trace behind it. That is a little ironic: they were themselves built on distilling human knowledge, and distilling an open-source model is still entirely routine; the restriction applies to their own outputs alone. Recent work...
  </details>

- **2026-10-21** — Zhipeng Cao, Peiyang Song, Nikolaus Vertovec et al. — [LLM2Cert: LLM Synthesis of Certificates with SMT/Lean Verification](http://arxiv.org/abs/2610.30524v1)
  <details><summary>📄 Abstract</summary>
  Lyapunov functions and barrier certificates give state-space guarantees of stability and safety, but synthesizing and verifying them---especially for nonlinear, high-dimensional systems---remains an open challenge. Existing pipelines verify candidates with numerical solvers (sum-of-squares programs), interval methods, or satisfiability-modulo-theories (SMT) solvers, which often require relaxations, are conservative, or scale poorly with model dimension and nonlinearity. These limitations have al...
  </details>

- **2026-10-21** — Vasiliy Kudryavtsev, Kirill Borodin, Nikita Vasiliev et al. — [Text-Only LLM Correctors Break Correct Transcripts: A Repair-Damage Analysis of Audio Grounding in ASR Error Correction](http://arxiv.org/abs/2610.30385v1)
  <details><summary>📄 Abstract</summary>
  LLM correctors of ASR output are judged by aggregate WER, which hides what they fix and what they break. We decompose every WER change exactly into repaired tokens, damaged tokens and insertions, and use this to ask what the source audio adds to a corrector. We compare correction with and without the audio, for the model's own draft and for the output of an independent recogniser, on three corpora. With Gemini 2.5 Flash, text-only correction of its own draft breaks 13-32% of already-correct tran...
  </details>

- **2026-10-21** — Nimun Bajwa, Massimo Poesio — [Probing and Steering for Safety-Relevant Behaviours in Large Language Models](http://arxiv.org/abs/2610.30363v1)
  <details><summary>📄 Abstract</summary>
  Activation probes are computed directions in a language model's residual stream, used both to detect safety-relevant behaviours and, by adding their direction back into the stream, to steer them. We explore how the main design choices behind such probes interact, within one pipeline, on one model (Llama-3.1-8B-Instruct), and across three behaviours: deception, high-stakes awareness and sycophancy. The pipeline crosses two estimators (difference-of-means and logistic regression) with three token-...
  </details>

- **2026-10-21** — Sujoy Roychowdhury, Joseph H. R. Isaac, Jiangning Gao et al. — [Code Comprehensor: Hierarchical Documentation and Cross-Modal Retrieval for Large Repositories](http://arxiv.org/abs/2610.30016v2)
  <details><summary>📄 Abstract</summary>
  Understanding large, complex, and rapidly evolving code bases remains a core challenge for software engineering at scale, hindering onboarding, maintenance, refactoring, and impact analysis. Providing this information to a Large-Language Model (LLM) is another hurdle, as the LLM must understand not only the required code method but also its associated methods in the grand scheme of the repository. We propose Code Comprehensor, a hybrid retrieval-reasoning framework combining (i) CodeGraph, a cod...
  </details>

- **2026-10-21** — Yuanzhong Zheng, Wei Huang, Ming Ma et al. — [Closed-Loop Dual-Reference Guidance for Accent Control in Cross-Lingual Voice Cloning](http://arxiv.org/abs/2610.29351v2)
  <details><summary>📄 Abstract</summary>
  Zero-shot cross-lingual voice cloning often carries the reference speaker's accent into the target language. We propose closed-loop dual-reference guidance, which pairs the original reference with a reusable native anchor constructed by voice conversion (VC). The references initialize separate language-model (LM) states that guide a shared acoustic trajectory; each completed patch then updates both states, keeping their generated histories aligned with the emitted speech. Anchor construction run...
  </details>

- **2026-10-21** — Xiongbo Shi, Shihang Du, Zongyou Yu et al. — [Motion Retargeting with Spatiotemporal Preferences for Humanoid Loco-Manipulation](http://arxiv.org/abs/2610.30540v1)
  <details><summary>📄 Abstract</summary>
  Human motion retargeting bridges the embodiment gap between humans and humanoid robots by converting human demonstrations into reference trajectories for whole-body control and loco-manipulation. For object-interaction tasks, successful execution depends on accurately preserving body--object relations at critical stages. However, uniform per-frame iteration budgets do not account for these localized accuracy requirements, limiting the computational efficiency of retargeting. To address this limi...
  </details>

- **2026-10-21** — Alexandros Psomas — [Cutting a Cake For Human Consumption: An Elementary $n$-agent Cake Cutting Protocol](http://arxiv.org/abs/2610.30370v1)
  <details><summary>📄 Abstract</summary>
  We give a bounded envy-free cake-cutting protocol for any number $n$ of agents in the Robertson--Webb model, with a short, self-contained, and elementary correctness proof. The protocol uses $2^{O(n \log n)}$ queries. Most ingredients are already known and well understood in the fair division literature; our main contribution is a simpler organization of these ideas into a protocol whose complete description and proof fit in a few pages.
  </details>

- **2026-10-21** — Navkar Jain, Enock Ayiku, Kenneth Fletcher — [FAIRGate: Agentic Runtime Policy Selection and Verified Repair for Fairer Recommendation Delivery](http://arxiv.org/abs/2610.30359v1)
  <details><summary>📄 Abstract</summary>
  Fairness-aware recommender systems often encode one fairness objective during training or apply a fixed re-ranking rule after scoring. In deployment, however, the appropriate fairness action can vary across requests because the candidate pool, item metadata, exposure debt, user preference history, and utility budget all change at runtime. We propose FAIRGate, a model-agnostic delivery controller that places an agentic policy-selection layer between a base ranker and the final top-K list. The age...
  </details>

- **2026-10-21** — Egor Shulgin, Sam Laing, Antonio Orvieto et al. — [A Quadratic Lens on Muon's Polar Update: Benefits, Pitfalls, and the Role of Newton-Schulz](http://arxiv.org/abs/2610.30280v1)
  <details><summary>📄 Abstract</summary>
  Muon updates matrix-valued parameters along approximately orthogonalized directions and often trains large language models faster than AdamW, yet it remains unclear when and why orthogonalization helps. We study PolarGD, the orthogonalized update at the core of Muon, on matrix quadratics, where optimizers can be analyzed in closed form, and compare update directions under line search to remove the effect of learning-rate tuning. Orthogonalization pays off when the gradient is far from low rank a...
  </details>

- **2026-10-21** — Siavash Golkar, Jake Kovalic, Shirley Ho — [AI Mindmeld: A Latent Interconnect Protocol](http://arxiv.org/abs/2610.30215v1)
  <details><summary>📄 Abstract</summary>
  LLMs can act as scientific agents using tools to consult specialists and run experiments. Yet specialist information must enter their context, generally as text, images, audio or video: a bottleneck between models with rich, high-dimensional representations. We advocate direct representation exchange: a mindmeld conveying many properties, including information an LLM would not think to request. It should be extensible to new specialists, flexible across questions and tasks, and compositional acr...
  </details>

- **2026-10-21** — Ju-Chun Ko — [Uncensored Is Not Unbiased: Abliteration Removes Refusals but Not Script-Dependent Bias About Taiwan](http://arxiv.org/abs/2610.29342v2)
  <details><summary>📄 Abstract</summary>
  "Abliterated" ("uncensored") builds of open-weight language models remove the activation direction that mediates refusal, and are popular partly on the assumption that a model that no longer refuses is free of political censorship. We test this on two matched pairs of 2-bit models: NVIDIA's Nemotron 3.5 Bolt 74B-A9B and Qwen3.8-Flash-Next, each against a community abliteration. Each model judged 22 statement pairs (on the Republic of China (Taiwan), 1989 Tiananmen, control countries) in Traditio...
  </details>

- **2026-10-21** — Fu-Peng Li, Yige Huang — [UrQMD-Agent: An LLM-Assisted Framework for Microscopic Tracing of Proton Azimuthal Correlations](http://arxiv.org/abs/2610.30198v1)
  <details><summary>📄 Abstract</summary>
  We present an LLM-assisted framework for microscopic transport studies that connects a general-purpose large language model (LLM) to the UrQMD transport model through a model-specific Skill and a deterministic scientific tool layer. The LLM supports literature-guided scientific planning and interpretation, while numerical calculations, event-history reconstruction, and statistical analyses are performed by deterministic tools. As a demonstration, the framework is applied to proton azimuthal-part...
  </details>

- **2026-10-21** — Clément Burgelin, Rachid Guerraoui, Zicong Hong et al. — [The End of Consensus Research?](http://arxiv.org/abs/2610.30114v1)
  <details><summary>📄 Abstract</summary>
  Consensus is a fundamental problem in distributed computing and at the core of state machine replication (SMR). Despite decades of active human research, discovering practical low-latency solutions to the problem is still open, as it requires combining protocol knowledge, correctness reasoning, implementation, and experimental evaluation. We report on how AI helped us discover A-greement, a new consensus protocol for geo-replicated state machines that significantly outperforms state-of-the-art s...
  </details>

- **2026-10-21** — Nurul Labib Sayeedi, Md. Faiyaz Abdullah Sayeedi, Zabir Al Nazi et al. — [Did the Problem Actually Get Harder? Testing LLMs on Paired P and NP-Complete Problems Hardened by Adversarial Multi-Agent Rewriting](http://arxiv.org/abs/2610.30103v1)
  <details><summary>📄 Abstract</summary>
  Many NP-complete (NPC) problems have a polynomial-time (P) twin that differs in a single structural detail, such as 3- versus 2-colouring a graph. A model that reasons rather than recalls should notice which side of this boundary a problem falls on, yet existing benchmarks either fix the wording of each task or ignore its complexity class, so they cannot separate the two. We introduce P2NPCBench, a benchmark of 12 problem families in which every NPC problem is paired with a P twin posed over the...
  </details>

- **2026-10-21** — Yan Wang — [TraceForge: Distilling with Your Own Thinking](http://arxiv.org/abs/2610.29680v1)
  <details><summary>📄 Abstract</summary>
  Using an LLM to generate training data for another is among the most general ways to train one, and it remains common practice. Some frontier teams have closed that route for their own models: what comes back is an answer, or a short summary, without the detailed reasoning trace behind it. That is a little ironic: they were themselves built on distilling human knowledge, and distilling an open-source model is still entirely routine; the restriction applies to their own outputs alone. Recent work...
  </details>

- **2026-10-21** — Chunyu Chen, Xinyi Huang, Zhengjie Miao — [Building SQL Equivalence Proofs from Query Rewrite Rules](http://arxiv.org/abs/2610.30100v1)
  <details><summary>📄 Abstract</summary>
  Query rewriting and semantic evaluation of text-to-SQL systems both depend on deciding whether two SQL queries return the same result on every database satisfying the schema constraints. Decades of equivalence-preserving optimizer rules provide a natural basis for constructive proofs: two queries are equivalent when admitted rewrites transform them to a common logical expression. Building on this observation, \sys{} organizes query-rewriting knowledge as a standalone proof-producing system. It s...
  </details>

- **2026-10-21** — Marek Wodzinski, Kamil Kwarciak, Daria Hemmerling et al. — [Plausible but Unimplantable: A Trustworthiness Audit of Shape Completion Foundation Models for Cranial Defect Reconstruction](http://arxiv.org/abs/2610.30035v1)
  <details><summary>📄 Abstract</summary>
  A patient who has lost part of the skull vault needs an implant that fits the defect exactly, and such implants are still drawn by hand in CAD by specialists, which makes each case slow and expensive. The task can be considered as a shape completion problem, so pretrained completion models, and now the first shape completion foundation models, look like a way to remove that manual step. We audited three publicly released pretrained shape completion models, two of them foundation models, applied ...
  </details>

- **2026-10-21** — Sujoy Roychowdhury, Joseph H. R. Isaac, Jiangning Gao et al. — [Code Comprehensor: Hierarchical Documentation and Cross-Modal Retrieval for Large Repositories](http://arxiv.org/abs/2610.30016v1)
  <details><summary>📄 Abstract</summary>
  Understanding large, complex, and rapidly evolving code bases remains a core challenge for software engineering at scale, hindering onboarding, maintenance, refactoring, and impact analysis. Providing this information to a Large-Language Model (LLM) is another hurdle, as the LLM must understand not only the required code method but also its associated methods in the grand scheme of the repository. We propose Code Comprehensor, a hybrid retrieval-reasoning framework combining (i) a code dependenc...
  </details>

- **2026-10-21** — Telem Joyson Singh, Sanabam Boyshana, Sanasam Ranbir Singh et al. — [Towards English - Mizo Legal Machine Translation: Corpus Creation, Analysis, and Benchmarks](http://arxiv.org/abs/2610.29943v1)
  <details><summary>📄 Abstract</summary>
  Indian court proceedings are held in English, so speakers of languages with limited translation technology have limited access to them. We present the first English Mizo parallel dataset of Indian court judgments. It contains 13,168 sentence pairs from the Gauhati High Court and the Supreme Court of India. Professional native Mizo translators translated complete documents; sentence pairs were manually aligned, and two independent reviewers checked the results. Our study finds that English words ...
  </details>

- **2026-10-21** — Naru Suzuki, Satoshi Ikehata, Takehiko Ohkawa et al. — [DewHand: Direct Metric World-Space Hand Motion Reconstruction from Egocentric Videos](http://arxiv.org/abs/2610.29936v1)
  <details><summary>📄 Abstract</summary>
  Recovering metric world-space hand motion from egocentric video supports understanding human interactions and transferring them to embodied agents. Three challenges complicate this task: multi-stage pipelines propagate errors from independently estimated hand and camera motion; monocular observations leave physical scale ambiguous; and occlusion and out-of-view hands admit multiple plausible motion trajectories. We present DewHand, a unified model for direct joint reconstruction of world-space h...
  </details>

- **2026-10-21** — Qiuyang Mang, Wenhao Chai, Runyuan He et al. — [FrontierCS 2: A Benchmark for Computer Science R&D](http://arxiv.org/abs/2610.29932v1)
  <details><summary>📄 Abstract</summary>
  Can LLM agents make contributions to frontier computer science R&D? We introduce FrontierCS 2, a benchmark of 48 open-ended tasks. We take a paper and the code its authors released and delete the paper's contribution. The deleted code becomes the human reference that sets the bar. Earlier open-ended benchmarks give each agent a problem statement and grade one program after the run. FrontierCS 2 places the agent inside a research environment. The agent inherits a working repository and may submit...
  </details>

- **2026-10-21** — Qinfan Zhang, Yifan Luo, Haoyuan Shi et al. — [GeoMem-VLA: Internalizing 3D Scene Understanding into Temporal Memory for Vision-Language-Action Models](http://arxiv.org/abs/2610.29866v1)
  <details><summary>📄 Abstract</summary>
  Geometric structure is essential for robotic manipulation and understanding the 3D world. Most VLA models rely on 2D representations of current observations, while geometry-aware approaches often require additional 3D information. However, geometry inferred independently from individual observations is often discarded rather than accumulated into a persistent task representation. Our key insight is that action generation needs a compact, task-relevant geometric abstraction that can be continuous...
  </details>

- **2026-10-21** — Yawei Li, Jiazheng Li, David Rügamer et al. — [S-EDL: Eliciting Self-Evidence from Sequence Likelihoods for Semantic Calibration of LLMs](http://arxiv.org/abs/2610.29832v1)
  <details><summary>📄 Abstract</summary>
  Calibrating large language models (LLMs) in open-ended generation is uniquely challenging because many distinct token sequences can express the same underlying meaning. Prior calibration techniques target either fixed-set classification confidence or the binary correctness of individual strings, making them inherently ill-suited for the dynamic, multi-string nature of open-ended semantic outcomes. To bridge this gap, we introduce S-EDL, a novel evidential method that natively optimizes LLMs for ...
  </details>

- **2026-10-21** — Logan Murphy, Wilson Sy, Rhys Balevicius et al. — [AssureCode: Structured Justification for Trustworthy Agentic Coding](http://arxiv.org/abs/2610.29758v1)
  <details><summary>📄 Abstract</summary>
  The use of AI-based tools in software development is rapidly changing how software is produced, enabling large volumes of code to be generated with limited human implementation effort. However, this raises fundamental challenges for ensuring that generated artifacts are aligned with developer intent and have been appropriately validated. In this work, we propose the use of structured argumentation in driving AI-assisted software development. Inspired by techniques from assurance engineering for ...
  </details>

- **2026-10-21** — Xingyi He, Zhiwen Qiu, Adhitya Polavaram et al. — [Reconstruction-Augmented Visuomotor Pre-Training of 3D-Grounded Bimanual Dexterity from RGB-Only Human Videos](http://arxiv.org/abs/2610.29716v1)
  <details><summary>📄 Abstract</summary>
  We present SpatialDex, a framework that learns 3D-grounded bimanual dexterity from RGB-only human videos through reconstruction-augmented visuomotor pre-training. The central idea is to learn human behavior together with its spatial context. From each video, we reconstruct the scene geometry and estimate the hand motion, align them at a shared video-level scale using the hand-size prior of 3D hand estimates. We retain the reconstructed geometry as both a policy input and a prediction target. The...
  </details>

- **2026-10-21** — Meng Luo, Zechen Bai, Shanqing Xu et al. — [Toward Recursive Self-Improvement in Physical AI](http://arxiv.org/abs/2610.29677v1)
  <details><summary>📄 Abstract</summary>
  Recursive self-improvement (RSI) describes a system that improves not only its behavior but also the process by which it improves. Recent digital agents test this idea by rewriting their own code and checking each version with executable tests. Bringing these mechanisms into the physical world requires learning from partial observations through costly trials, while accounting for changing operating conditions and potentially irreversible consequences. We position RSI within robot learning and tr...
  </details>

- **2026-10-21** — Martin Thißen, Elke Hergenröther — [Unlocking Spatial Grounding in Flow-Matching Models via SNR Tuning](http://arxiv.org/abs/2610.29581v1)
  <details><summary>📄 Abstract</summary>
  Despite the success of foundation models in image synthesis, achieving fine-grained spatial control remains a significant challenge, typically requiring auxiliary structural adapters or complex inference-time steering. While modern vision-language (VLM) text encoders possess the latent capacity to represent spatial coordinates, generative models often fail to leverage this information. We demonstrate that the signal-to-noise ratio (SNR) distribution is a critical determinant of spatial grounding...
  </details>

- **2026-10-21** — Mingkang Liu, Weiming Meng, Peipei Jiao et al. — [RCSD: Reinforcement and Continual Learning for Domain-Specific Speculative Decoding](http://arxiv.org/abs/2610.29527v1)
  <details><summary>📄 Abstract</summary>
  Speculative decoding accelerates large language model inference by employing a compact draft model to propose candidate tokens that are verified in parallel by a target model. Conventional training relies on soft-label distillation, which forces the draft model to mimic the target's full output distribution, including high-entropy regions that degrade acceptance rates and increase early rejection risk. We propose RCSD (Reinforcement and Continual Learning for Speculative Decoding), a training fr...
  </details>

- **2026-10-21** — Wentao Wu, Xu Wang, Linqing Chen et al. — [X-Embedding: Two-Stage Training for Multilingual Patent Prior-Art Retrieval](http://arxiv.org/abs/2610.29521v1)
  <details><summary>📄 Abstract</summary>
  Multilingual patent prior-art retrieval requires identifying X-category references that are particularly relevant to the novelty or inventive step of a claimed invention, beyond topical similarity across languages and document views. We present X-Embedding, a two-stage framework that first learns patent-domain representations and then optimizes X-category retrieval relevance. The first stage aligns complementary sections within patents and corresponding sections across different-language patent-...
  </details>

- **2026-10-21** — Yun Li, Ehsan Javanmardi, Simon Thompson et al. — [ECHO: Emergent Common-Mode Hidden Offsets Drive Vocabulary Collapse in Preference Optimization](http://arxiv.org/abs/2610.29410v1)
  <details><summary>📄 Abstract</summary>
  Preference optimization can improve every ranking metric while building a hidden, shared representation shift that the relative loss barely sees, one that can eventually destroy generation. We trace this failure to the common-mode offset, a shared directional shift in the model's hidden states that appears across token positions, prompts, and both chosen and rejected responses. Because it moves chosen and rejected representations together, the relative ranking loss barely reacts to its accumulat...
  </details>

- **2026-10-21** — Haoye Chai, Mugen Peng — [RadioDreamer: A World Model for Radio Map Forecasting and Imagination-Based Optimization](http://arxiv.org/abs/2610.29382v1)
  <details><summary>📄 Abstract</summary>
  Radio maps characterize the spatial distribution of wireless conditions and are fundamental to network planning and optimization. However, existing learning-based methods reconstruct isolated radio-map snapshots and do not model how network actions drive the evolution of the radio environment. In this paper, we present RadioDreamer, a two-stage world model that unifies action-conditioned radio-map forecasting and imagination-based network optimization within a latent space. To learn causal envir...
  </details>

- **2026-10-21** — Rodion Shkokov, Tatiana Zemskova, Dmitry Yudin — [AOV-GS: Active Open-Vocabulary Semantic Mapping with 3D Gaussian Splatting](http://arxiv.org/abs/2610.29374v1)
  <details><summary>📄 Abstract</summary>
  Robots deployed in human-centered environments need maps that support both geometric navigation and open-vocabulary semantic queries beyond a fixed label set. A key challenge is enriching such maps with semantic information without relying on manually annotated segmentation masks or closed-set semantic categories. Existing geometry-driven active mapping maximizes coverage but treats semantics as a passive by-product of the collected trajectory, whereas active semantic mapping typically depends o...
  </details>

- **2026-10-21** — Yuanzhong Zheng, Wei Huang, Ming Ma et al. — [Closed-Loop Dual-Reference Guidance for Accent Control in Cross-Lingual Voice Cloning](http://arxiv.org/abs/2610.29351v1)
  <details><summary>📄 Abstract</summary>
  Zero-shot cross-lingual voice cloning often carries the reference speaker's accent into the target language. We propose closed-loop dual-reference guidance, which pairs the original reference with a reusable native anchor constructed by voice conversion (VC). The references initialize separate language-model (LM) states that guide a shared acoustic trajectory; each completed patch then updates both states, keeping their generated histories aligned with the emitted speech. Anchor construction run...
  </details>

- **2026-10-21** — Yuanzhong Zheng, Wei Huang, Ming Ma et al. — [Decodability Is Not Controllability: Local and Anisotropic Speaker Control in Continuous-Latent TTS](http://arxiv.org/abs/2610.29345v1)
  <details><summary>📄 Abstract</summary>
  High linear decodability does not entail causal controllability in continuous-latent text-to-speech (TTS). In VoxCPM2, position-matched probes and equal-norm interventions across 30 speakers and 60 directed dyads expose this separation: reference-audio states at the final residual acoustic language model layer (RALM L7) retain 0.970 probe accuracy, yet aligned edits yield 0/60 target-dominant dyads. Edits at early reference-audio positions produce the opposite pattern. At L0, pair-aligned update...
  </details>

- **2026-10-21** — Nenad Petrovic, Alois Knoll — [AI-Based End-to-End Automotive Design and Software Development for SDVs](http://arxiv.org/abs/2610.29160v1)
  <details><summary>📄 Abstract</summary>
  This paper explores the potential of Artificial Intelligence (AI) to enable end-to-end automotive design and software development for Software-Defined Vehicles (SDVs). Based on our contributions within the Central Car Server (CeCaS) and follow-up EU-funded projects, we present an AI-driven toolchain integrating Large Language Models (LLMs) with Model-Driven Engineering (MDE) to automate the transformation of natural-language requirements into system architectures, executable software, and valida...
  </details>

- **2026-10-21** — Rui Zhang, Chenyu Zhou, Jianghao Lin et al. — [ORSMT: Unleashing the Potential of Satisfiability Modulo Theories for Semantic Verification and Repair in LLM-Based Optimization](http://arxiv.org/abs/2610.29145v1)
  <details><summary>📄 Abstract</summary>
  Large language models increasingly automate optimization modeling from natural language problems, producing written mathematics, solver code and a returned report. Verifying one optimization problem across these artifacts requires semantic comparison: unequal models can attain the same objective, equivalent models can use different auxiliary variables, and mutually consistent artifacts can omit the same source requirement. ORSMT provides a typed semantic interface and exact SMT relation queries....
  </details>

- **2026-10-21** — Kazuhito Ohmi, Liangsheng Huang, Hanyang Liu et al. — [Oscillation modes, Decoherence, Beam Transfer Functions, and Instabilities for a Beam Subjected to Space-Charge Forces](http://arxiv.org/abs/2610.29094v1)
  <details><summary>📄 Abstract</summary>
  Based on the oscillation modes of a bunch subject to the space-charge force, we discuss the decoherence of the dipole oscillation, the beam transfer function, and the beam instability. The longitudinal phase space is discretized into \(n_l\times n_J\) grids in the azimuthal and radial directions, respectively. The transverse dipole moment in the longitudinal phase space is represented by a vector of length \(n_l n_J\), and the transformation given by the Vlasov equation is represented by a matri...
  </details>

- **2026-10-21** — Rui Sun, Peizhao Mei, Xiewei Cheng et al. — [Same Answer, Different Reasons: Trace-Level Divergence in Multilingual Large Language Models](http://arxiv.org/abs/2610.29092v1)
  <details><summary>📄 Abstract</summary>
  Multilingual large language models are increasingly deployed in settings where visible reasoning traces support verification, education, and safety auditing, yet standard evaluations typically measure only final-answer agreement or holistic response similarity. As a result, they establish outcome consistency without determining whether users across languages receive comparable supporting evidence. We introduce a trace-level divergence framework that compares visible reasoning traces as structure...
  </details>

- **2026-10-21** — Khush Kataruka, Mohammad Muzammila, Zahid Akhtar et al. — [Enhancing Cross-Grade Generalization in Banana Variety Classification via Hybrid CNN-Transformers and Knowledge Self-Distillation](http://arxiv.org/abs/2610.29008v1)
  <details><summary>📄 Abstract</summary>
  In recent years, automated fruit classification systems have become a more critical component in precision agriculture for efficient yield estimation, quality control, and supply chain optimization. However, they still face significant challenges under varying quality, fruit maturity, illumination, texture degradation, morphological attributes, domain shift, and post-harvest handling conditions. In this study, we address the challenging issue of cross-grade banana variety classification. This is...
  </details>

- **2026-10-21** — Adrien Ramanana Rahary, Yutong Bai, Nicolas Dufour et al. — [Rethinking Video Autoencoders for Interactive World Models](http://arxiv.org/abs/2610.30129v1)
  <details><summary>📄 Abstract</summary>
  Video world models predict future frames from past frames and actions. They serve as simulators in which agents train, plan or are evaluated, and that humans can control interactively. They generate in the latent space of a video autoencoder, whose compression sets their cost per frame and how long each action waits to take effect. Yet world models often reuse the autoencoders of text-to-video generators, built for offline generation with no agent waiting and, without their training data and cod...
  </details>

- **2026-10-21** — May Espinola, Qifan Zhang, Yu Xiang — [From Reasoning to Action: Benchmarking Frontier AI Models on LIBERO-10 Robot Manipulation Tasks](http://arxiv.org/abs/2610.30051v1)
  <details><summary>📄 Abstract</summary>
  Recent advances in frontier AI models have demonstrated remarkable capabilities in visual understanding, reasoning, planning, and tool use, raising the possibility of using general-purpose AI models for robot manipulation without task-specific training. However, their manipulation capabilities have not been systematically evaluated on standardized robotics benchmarks. In this report, we present a unified closed-loop manipulation framework for evaluating frontier AI models on the LIBERO-10 benchm...
  </details>

- **2026-10-21** — Liu Cao, Botian Xu, Ruoqu Chen et al. — [HuMiT: Low-Latency Whole-Body Humanoid Teleoperation via Compact Reference Tracking](http://arxiv.org/abs/2610.29903v1)
  <details><summary>📄 Abstract</summary>
  Real-time whole-body humanoid teleoperation remains challenging due to the computational latency introduced by optimization-based retargeting pipelines and future-frame conditioning. Existing motion tracking policies typically require dense reference targets including full joint positions, body-part transformations, and even future frames, which tightly couples the controller to expensive upstream modules. In this work, we present HuMiT, a whole-body teleoperation system built on a unified track...
  </details>

- **2026-10-21** — Yijun Shen, Diqi He, Jinbang Guo et al. — [CausGround: Causal Interaction Grounding for Adaptive Embodied Planning](http://arxiv.org/abs/2610.29702v1)
  <details><summary>📄 Abstract</summary>
  Multimodal large language models (MLLMs) show promising reasoning capabilities, but reliable physical interaction requires planning that accounts for when actions are executable and how they change the world. These preconditions and effects are environment-dependent and often not captured by MLLMs, making adaptation challenging. Yet existing approaches either require costly environment-specific training or rely on unstructured interaction experience that is difficult to reuse. Therefore, we intr...
  </details>

- **2026-10-21** — Tingwen Du, Haoyu Guo, Hanxue Zhang et al. — [From VLM Planners to Robotic Agents: Self-Evolving Harnesses for History-Dependent Manipulation](http://arxiv.org/abs/2610.29560v1)
  <details><summary>📄 Abstract</summary>
  Vision-language-action (VLA) models achieve strong performance across embodied manipulation tasks by unifying visual understanding, language conditioning, and action generation. However, long-horizon tasks can involve non-Markovian dependencies: successful decisions may require retaining task progress and past interaction outcomes, while partial observability and execution errors compound over time. Existing work has begun to address these challenges by augmenting foundation-model policies with ...
  </details>

- **2026-10-21** — Yegor Anichkov, Valery Vinogradov, Andrey Furov et al. — [TenetBench: A Clause-Anchored Russian Corpus for Evaluating Language Models against Professional Codes of Ethics](http://arxiv.org/abs/2610.29477v1)
  <details><summary>📄 Abstract</summary>
  Codes of professional ethics guide and restrict specialists, who increasingly work with assistants built on large language models. Such an assistant can breach the user's code, or help the user breach it, without the user noticing. Evaluations reporting broad categories of harm cannot show how often this happens or which provision is breached. TenetBench pairs 3,433 requests conflicting with clauses of fifteen Russian-language professional codes with benign twins that differ only in the legitima...
  </details>

- **2026-10-21** — Qinghang Liu, Conglin Wang, Zongsheng Li et al. — [Plan First, Act Later: Streaming Reasoning for Executable Memory in Robot Control](http://arxiv.org/abs/2610.29329v1)
  <details><summary>📄 Abstract</summary>
  Long-horizon robot manipulation requires a robot to remember task-relevant information beyond its short observation window. Existing memory-augmented policies typically retrieve relevant information from history and reason over it at execution time, placing a heavy reasoning burden on the high-level model. To address this challenge, we propose PAL (\textbf{P}lan first, \textbf{A}ct \textbf{L}ater), a hierarchical memory framework for vision-language robot manipulation. It maintains a short-term ...
  </details>

- **2026-10-21** — Caicheng Wang, Zipeng Ye, Zhexuan Zhou et al. — [SimPT: An Automated Simulation Framework for Intervention-Based VLA Post-Training](http://arxiv.org/abs/2610.29161v1)
  <details><summary>📄 Abstract</summary>
  Human-in-the-loop (HIL) post-training improves vision-language-action (VLA) policies through expert corrections, but costly human supervision and repeated real-robot evaluation limit algorithm exploration and development. We introduce SimPT (Simulation-based Post-Training), a simulation framework that automates intervention-based VLA post-training by integrating policy rollouts, corrective data collection, policy training, and standalone evaluation. To automatically determine intervention timing...
  </details>

- **2026-10-21** — Irina K. Romanovskaya — [Postbiological intelligence, interstellar colonization of cyberspaces and the Fermi Paradox: implications for SETI and SETA](http://arxiv.org/abs/2610.29038v1)
  <details><summary>📄 Abstract</summary>
  I propose that a continuity in the evolution of intelligent life in the Universe during its transition from biological to postbiological depends on a commonality of the evolutionary trajectories of biological life and postbiological life. Such a commonality exists in the form of the universal property of life. The universal property of life comprises recognition of patterns in the world, creation of novel patterns and remembering them, with the patterns growing in complexity along evolutionary t...
  </details>

- **2026-10-21** — Ruotong Liao, Meikel Kokowski, Xiaoxiao Sun et al. — [ProactEgoMem: Benchmarking Proactive Memory in Streaming Egocentric Video](http://arxiv.org/abs/2610.30089v1)
  <details><summary>📄 Abstract</summary>
  Today's multimodal assistants are typically prompted to interpret the visual evidence presented to them. To offload the cognitive burden of remembering across long horizons, wearable assistants should instead proactively acquire and maintain useful memory as the user's surroundings evolve. Doing so on the user's behalf requires identifying what matters, understanding the scene in real time, and initiating memory maintenance in the background while the user stays focused on their activities. We i...
  </details>

- **2026-10-21** — Wenhao Yu, Zhengcheng Wang, Jiahong Liu et al. — [CORD: Conflict-Aware Optimization for Joint RL and Distillation in Agents](http://arxiv.org/abs/2610.29965v1)
  <details><summary>📄 Abstract</summary>
  Joint reinforcement learning and self-distillation combines task rewards with dense teacher guidance for agent training, but their gradients can partly cancel. A mixing coefficient controls relative scale without selectively removing opposing components. We present CORD, a general framework for conflict-aware optimization of two objectives. CORD separates the choice of protected objective from the condition that triggers projection, and combines the gradients once per optimizer mini-batch. A nea...
  </details>

- **2026-10-21** — Gyeonghun Kang, William Xingxu Chen, Xiang Cheng — [How Do DiTs Denoise? An Aggregator-Predictor View of Attention and MLPs](http://arxiv.org/abs/2610.29854v1)
  <details><summary>📄 Abstract</summary>
  How do diffusion transformers (DiTs) represent image content and learn rules for reusing it to generalize? We develop an aggregator--predictor view of DiTs as input-adaptive local denoisers, in which context aggregation and patch prediction provide functional roles for interpreting attention and MLPs. We first establish that, for Gaussian Markov random field (GMRF) priors, the global Bayes denoiser can be approximated using only a subset of context patches, with error decaying exponentially in c...
  </details>

- **2026-10-21** — Jiawei Chen, Xiang I. A. Yang, Ping He — [Automated Discovery of Physically Interpretable Subgrid Length Scales for Detached Eddy Simulation via Agentic AI](http://arxiv.org/abs/2610.29850v1)
  <details><summary>📄 Abstract</summary>
  Traditional turbulence-model development relies heavily on expert knowledge and is time-consuming. This study develops an agentic AI framework, DEScover (automated Discovery of DES closures), to explore subgrid length scales for detached eddy simulation (DES). The user provides only a modeling idea: the length scale is the grid width normal to the local vortex axis. Four large language model (LLM) agents then propose, review, implement, and evaluate candidate formulations and generate scripts fo...
  </details>

- **2026-10-21** — Benedikt Kreis, Rohit Menon, Benno Wingender et al. — [OMAR: Open-World Multi-Attribute Reasoning for Scene-Conditioned Shelf Organization](http://arxiv.org/abs/2610.29761v1)
  <details><summary>📄 Abstract</summary>
  With the advent of foundation models, robots are increasingly capable of understanding and executing explicitly specified human tasks. Extending these capabilities to open-ended tasks, however, requires robots to infer appropriate actions from the observed scene. Household organization exemplifies this challenge, as robots must often act without detailed instructions, predefined object vocabularies, or known object-receptacle associations. While robots may follow instructions or learn organizati...
  </details>

- **2026-10-21** — Yanze Zhang, Maggie Yongqi Guan, Shudong Liu et al. — [Benchmarking Coding Agents for System-Level Performance Optimization](http://arxiv.org/abs/2610.29695v1)
  <details><summary>📄 Abstract</summary>
  Coding agents are becoming an increasingly important paradigm for automating software engineering tasks. However, existing coding benchmarks primarily evaluate agents at the function or repository level, leaving their capabilities in more complex distributed software systems largely unexplored. In practice, many modern applications adopt microservice architectures, where end-to-end performance emerges from interactions among multiple independently running services, requiring agents to reason bey...
  </details>

- **2026-10-21** — Divyaansh Mertia, Chirag Bhutra, Himanshu Shekhar et al. — [Rethinking Post-hoc Debiasing of Large Pretrained Models](http://arxiv.org/abs/2610.29688v1)
  <details><summary>📄 Abstract</summary>
  Large pretrained models such as CLIP are widely used as frozen feature extractors. However, their embeddings inherit spurious correlations from training data, introducing bias into the features. A growing body of research has sought to address this issue through post hoc debiasing, leaving the backbone untouched. We discover that despite differing mechanisms, these methods require the bias feature to be identified and expressed in text. This dependency is not innocuous. In this work, we experime...
  </details>

- **2026-10-21** — Xiaokun Teng, Yanqing Ren, Weicong Chen et al. — [Wave Processing Unit: Closed-Form Matrix Synthesis for Wave Computing in Multiuser MIMO Communications](http://arxiv.org/abs/2610.29687v1)
  <details><summary>📄 Abstract</summary>
  Wave computing offers a compelling route to bypass the latency and energy bottlenecks of digital baseband processing. However, existing wave-domain processors rely on task-specific, non-convex iterative optimization, which incurs substantial configuration overhead and limits real-time applications. In this paper, we propose the wave processing unit (WPU), a programmable planar Mach--Zehnder interferometer (MZI) network that accelerates matrix--vector multiplications in MIMO communications. First...
  </details>

- **2026-10-21** — Kuniko Paxton, Ifeoluwa Wuraola, Dhavalkumar Thakker — [Effects of Model Scale and Quantization on Social Bias and Abstention in Question Answering](http://arxiv.org/abs/2610.29657v1)
  <details><summary>📄 Abstract</summary>
  The deployment of small and quantized language models in resource-constrained settings raises an important fairness question: when a compressed model produces fewer biased responses, does this reflect fairer behavior or greater abstention? We study this problem in Question Answering (QA) using the BBQ benchmark across multiple model sizes and quantization settings from Qwen3, Gemma-3, and SmolLM2. We also examine whether the observed trends remain stable across alternative prompt formulations an...
  </details>

- **2026-10-21** — Shin'ya Yamaguchi — [Mitigating Query Shortcuts in Chain-of-Thought with Context-Aware Decoding](http://arxiv.org/abs/2610.29518v1)
  <details><summary>📄 Abstract</summary>
  While Chain-of-Thought (CoT) prompting improves the reasoning performance of large language models (LLMs), recent studies have shown that final answers do not always depend on the generated rationales. In particular, LLMs may rely on query-specific shortcuts rather than the information provided by their reasoning steps. In this paper, we investigate whether context-aware decoding (CAD), an existing contrastive decoding method, can mitigate such shortcut behavior when applied to CoT reasoning. We...
  </details>

- **2026-10-21** — Brett Binst, Annelien Smets — [The Serendiptionnaire: a Questionnaire for Measuring Experienced Serendipity](http://arxiv.org/abs/2610.29487v1)
  <details><summary>📄 Abstract</summary>
  Serendipity is important to design for, yet it remains difficult to measure and evaluate. No validated questionnaire exists, so studies either borrow ResQue's novelty scale, which does not measure serendipity, or build their own items, which makes findings hard to compare and synthesize. Building on our earlier conceptualization of experienced serendipity as a fortuitous encounter with content that is both refreshing and enriching, we developed the Serendiptionnaire, a questionnaire that operati...
  </details>

- **2026-10-21** — Mingxuan Liu, Pavel Sekatski, Valerio Scarani — [Quantum Belief Characterization: A Multi-Shot Notion of Equivalence](http://arxiv.org/abs/2610.29450v1)
  <details><summary>📄 Abstract</summary>
  A recent formulation of quantum belief showed that quantum retrodiction depends not only on the reduced density operator of the system of interest, but also on correlations with a hidden reference system, which leads to the notion of quantum belief equivalence. In this paper we formulate a multi-shot problem, where the extended posterior obtained after one update is used again as the prior for the next update. We first define a formal notion of $n$-shot equivalence and derive several proposition...
  </details>

- **2026-10-21** — Kleanthis Avramidis, Ivan Tashev, Dimitra Emmanouilidou — [Probing Spatial and Spectral Grounding in EEG Foundation Models](http://arxiv.org/abs/2610.29367v1)
  <details><summary>📄 Abstract</summary>
  EEG foundation models are advancing at an unprecedented pace, yet their evaluation is driven by downstream accuracy, which reveals little about whether their predictions rely on physiologically interpretable signal structure. We introduce a set of perturbation probes in two grounding axes: spatial grounding in channel identity and topographic locality, and spectral grounding in oscillatory content and waveform morphology. We apply these probes to five published EEG foundation models across motor...
  </details>

- **2026-10-21** — Hrishikesh Singh, Aarti Sharma, Divyanshu Kumar et al. — [Reading the Mask: Descriptor-Grounded BI-RADS Rationale Generation for Breast MRI Segmentation](http://arxiv.org/abs/2610.29358v1)
  <details><summary>📄 Abstract</summary>
  Deep learning based models accurately delineate tumours on dynamic contrast-enhanced MRI (DCE-MRI), but segmentation masks alone do not provide the rationales or reasoning used by radiologists to assess the lesion suspicion. This limits the explainability as well the clinical integration. We investigate whether clinically relevant descriptors can instead be derived from the segmentation masks and their dynamic contrast-enhancement series. We have used Breast Imaging Reporting and Data System (BI...
  </details>

- **2026-10-21** — Haodong Wen, Kairong Luo, Tingkai Yan et al. — [Data Schedules and Learning Rate Schedules Should Be Designed Together](http://arxiv.org/abs/2610.29348v1)
  <details><summary>📄 Abstract</summary>
  Mid-training (MT) is a training phase in LLM training pipelines that continues pretraining (PT) on smaller datasets of higher value. Taking the PT and MT phases as a whole, training usually starts with only PT data and then transitions completely to MT data. In this work, we view this complete transition from PT to MT data as a special case of a broader class of data mixing schedules that specify how the proportions of PT and MT tokens in each batch change over training. Under fixed total traini...
  </details>

- **2026-10-21** — Ju-Chun Ko — [Uncensored Is Not Unbiased: Abliteration Removes Refusals but Not Script-Dependent Bias About Taiwan](http://arxiv.org/abs/2610.29342v1)
  <details><summary>📄 Abstract</summary>
  "Abliterated" ("uncensored") builds of open-weight language models remove the activation direction that mediates refusal, and are popular partly on the assumption that a model that no longer refuses is also free of political censorship. We test this on two matched pairs of 2-bit models: NVIDIA's Nemotron 3.5 Bolt 74B-A9B and Qwen3.8-Flash-Next, each against a community abliteration. Each model judged 22 statement pairs (on the Republic of China (Taiwan), 1989 Tiananmen, control countries) in Tra...
  </details>

- **2026-10-21** — Sen Jia, Siqi Wei, Junyu Wang et al. — [YingLan: A Multimodal Ocean Foundation Model for Unified Representation Learning from Heterogeneous Observations](http://arxiv.org/abs/2610.29313v1)
  <details><summary>📄 Abstract</summary>
  Multimodal ocean modeling remains challenging due to substantial heterogeneity in data structures, physical semantics, and spatiotemporal characteristics across satellite imagery, gridded oceanographic fields, and buoy observations. Existing approaches largely focus on task-specific ocean modeling, while learning transferable representations from heterogeneous observations remains an open problem. To address this challenge, we propose YingLan, a multimodal ocean foundation model that integrates ...
  </details>

- **2026-10-21** — Jia Deng, Zizhe Wang, Xin Lu et al. — [Compressing Onboard Language Models for Space Robots under a Behavioral-Fidelity Requirement](http://arxiv.org/abs/2610.29302v1)
  <details><summary>📄 Abstract</summary>
  Language models are being explored as the interface through which space robots interpret operator commands and select among verified skills. Running them onboard calls for low-bit compression, and flight use adds requirements that generic post-training quantization leaves implicit: a fixed memory budget and storage format, a static artifact under configuration control, and behavior close to the full-precision model validated on the ground. We treat compression as a ground-segment step and study ...
  </details>

- **2026-10-21** — Anat Veikherman, Mor Ventura, Nitay Calderon et al. — [Encoded but Unused: Bounding the Sources of VLM Errors](http://arxiv.org/abs/2610.29241v1)
  <details><summary>📄 Abstract</summary>
  In this paper, we investigate why vision-language models (VLMs) produce errors by decomposing them into two sources: visual-representation failures, in which the visual evidence required for the correct answer is not encoded, and visual-utilization failures, in which this evidence is encoded but not successfully used. We propose to estimate the visual-utilization failure rate using lightweight probes and derive theoretical bounds on the true rate that account for probe imperfections. We introduc...
  </details>

- **2026-10-21** — Sepideh Mahabadi, Prasanna Ramakrishnan, Jakub Tarnawski — [Pareto Inefficiency of EFX](http://arxiv.org/abs/2610.29201v1)
  <details><summary>📄 Abstract</summary>
  We consider the problem of allocating indivisible goods to agents with additive valuations, under two classic notions of fairness and efficiency: envy-freeness up to any good (EFX) and Pareto optimality. While some of the earliest work on EFX showed that Pareto optimal EFX allocations may not exist if agents can have zero value for some goods, it has remained open whether the same is true when all values are positive.   We present a simple instance in which every good has positive value to every...
  </details>

- **2026-10-21** — Diankun An, Lu Ma, Yongliang Wang et al. — [Character-Level Prosody Control for Mandarin Speech Synthesis:An Architecture-Preserving Approach](http://arxiv.org/abs/2610.29123v1)
  <details><summary>📄 Abstract</summary>
  This paper addresses fine-grained prosody control for large-language-model (LLM) based text-to-speech (TTS) synthesis of Mandarin Chinese, motivated by multimedia content-creation scenarios---film dubbing, audiobook production, and interactive voice interfaces---in which prosodic adjustments must be placed on specific characters rather than applied uniformly to whole utterances. We present a data-driven framework in which fine-grained prosodic markers (pitch, duration, energy, and pause) are aut...
  </details>

- **2026-10-21** — Erh-Wei Sheng, Beom Seok Kang, Yuchao Lin et al. — [SU(2)-Equivariant Spinor Message Passing for Molecular Magnetism](http://arxiv.org/abs/2610.29111v1)
  <details><summary>📄 Abstract</summary>
  Predicting molecular magnetism often requires electronic-structure calculations with spin-orbit coupling (SOC), which are costly to repeat across many molecules. The underlying electronic states can transform as spinors, yet equivariant surrogates typically use only integer-rank features. Inspired by the spinor nature of these electronic states, we develop eSpinor, an SU(2)-equivariant graph neural network that propagates spinor features. We initialize spinor features from eigenvectors of an app...
  </details>

- **2026-10-21** — Jaywon Koo, Junghyun Koo, Marco A. Martinez-Ramirez et al. — [Agentic Music Post-Production](http://arxiv.org/abs/2610.29093v1)
  <details><summary>📄 Abstract</summary>
  We introduce MixAgent, an agentic pipeline for music post-production that follows the workflow of audio engineers to build interpretable and editable mixing plans guided by a reference song. A grouping agent first routes related input tracks, such as drum recordings, into subgroups. A planning agent then uses retrieved examples to choose and order audio effects, such as volume control and reverb, for tracks, subgroups, and the full mix. To refine the mix, a detector identifies what needs correct...
  </details>

- **2026-10-21** — Maciej R. Molas — [The Spectroscopic Atlas of Excitonic Complexes in hBN-Encapsulated S-TMD Monolayers: From Excitons to Oxcitons and Beyond](http://arxiv.org/abs/2610.29081v1)
  <details><summary>📄 Abstract</summary>
  Hexagonal boron nitride (hBN) encapsulation has transformed the optical spectroscopy of semiconducting transition-metal dichalcogenide monolayers (MLs) by suppressing extrinsic disorder and enabling the resolution of an increasingly complex hierarchy of excitonic states. This Review provides a spectroscopy-oriented framework for understanding and identifying excitonic complexes in hBN-encapsulated Mo- and W-based MLs and their alloys. The discussion covers bright and dark excitons, Rydberg state...
  </details>

- **2026-10-21** — Andrew Qing He — [Neural Vector Field Transformations: Learning the Flow of Autonomous Systems by Conjugation to Explicitly Integrable Reference Flows](http://arxiv.org/abs/2610.29039v1)
  <details><summary>📄 Abstract</summary>
  We represent the flow map of an autonomous ODE $\dot x=f(x)$ as a conjugate $Φ_t=F_θ^{-1}\circΨ_t\circ F_θ$ of an explicitly integrable reference flow $Ψ_t$ by an invertible neural network $F_θ$, the neural vector field transformation. The representation is an exact flow for every parameter value and inherits the phase portrait of the reference. A $C^1$ conjugacy preserves the eigenvalues of equilibria, the periods and Floquet multipliers of periodic orbits and the frequency-amplitude relation o...
  </details>

- **2026-10-20** — Xinxin Liu, Bingxin Xu, Wenrui Bao et al. — [AgenticRoboRL: Bringing Coding-Agent Post-Training to Agentic Robotics](http://arxiv.org/abs/2610.28589v2)
  <details><summary>📄 Abstract</summary>
  Agentic robotics systems combine planners with robot harnesses to perform complex manipulation tasks. Recent work improves these systems through better harnesses and external memory, but relies on powerful closed-source models as planners and does not improve the planners' own capabilities. In contrast, coding agents have improved substantially by post-training the model itself. We therefore investigate whether post-training can also improve robot planners. However, applying it across robot harn...
  </details>

- **2026-10-20** — Chao Shang, Wanyu Du, Yi Zhang et al. — [AgentPolicyForge: From Executable Environments to Policy Benchmarks and Adaptive Guards](http://arxiv.org/abs/2610.28989v1)
  <details><summary>📄 Abstract</summary>
  Customized agent deployments define policies over tools, resources, and execution conditions. Providing these policies in the task agent's prompt does not reliably prevent violations. Training a guard requires examples of tool calls that comply with or violate those policies. We introduce AgentPolicyForge, a framework that uses executable environments to construct policy benchmarks and iteratively train policy guards. With this framework, we construct PolicyGym, a dataset across ten policy famil...
  </details>

- **2026-10-20** — Xiaoyu Ma, Zheyuan Zhang, Kaiwen Shi et al. — [Beyond Correct Answers: How Compositional Cues Shape Visual Judgments](http://arxiv.org/abs/2610.28843v1)
  <details><summary>📄 Abstract</summary>
  Visual question answering requires models to assign attributes and relations to the correct objects, a problem known as visual binding. Structured prompts make these assignments explicit through labeled fields. Yet an improvement from the full prompt does not reveal which labels help or how they interact. First, we isolate field-label effects across ten models and six tasks by holding the image and claim fixed. These comparisons reveal differences that overall accuracy can hide. With a relation ...
  </details>

- **2026-10-20** — Runguo Li, Dezhen Lu — [Weight Placement Is Not Enough: Synchronization in Multi-Node CPU Decoding of Ternary LLMs](http://arxiv.org/abs/2610.28620v2)
  <details><summary>📄 Abstract</summary>
  Ternary LLMs read only a few gigabytes per decoded token, yet on dual-socket servers with four NUMA nodes the fastest ternary runtime we found uses less than half of the memory bandwidth. Placing each weight on the node of the thread that reads it is necessary but not enough: in a decode engine with node-local weights that reuses ik_llama's kernels, threads on two generations of Xeon servers still spend 20-48% of each token waiting at synchronization points. Per-thread barrier traces show that m...
  </details>

- **2026-10-20** — Charbel Abi Hana, Rayan Zaitouni, Kameel Amareen et al. — [Physical AI for Intralogistics: Benchmarking the NVIDIA Sim-to-Real Ecosystem for Cosmos-Enhanced COMPASS Navigation on Industrial Mobile Robots](http://arxiv.org/abs/2610.28432v2)
  <details><summary>📄 Abstract</summary>
  Classical robot navigation stacks are reliable but often require re-engineering for each new robot type and site. Learning-based navigation shifts this effort from hand-tuned parameters to data generation and training, where a policy adapts to each new embodiment or facility by fine-tuning in simulation. Whether policies adapted this way stay reliable on real industrial robots has seen little systematic testing. We study this for NVIDIA's X-Mobility and COMPASS workflow for training learned navi...
  </details>

- **2026-10-20** — Audrey Lee, Nathaniel Dennler, Ilia Sucholutsky et al. — [Flexible Language-Guided Representation Editing for Adaptive Robot Behavior](http://arxiv.org/abs/2610.28893v1)
  <details><summary>📄 Abstract</summary>
  Trajectory demonstrations show robots how to behave but not why, leaving them to guess which features of the task actually matter. Incorrect guesses produce misaligned internal representations and lead to incorrect robot behaviors. Because task features are often semantically defined, we argue that natural language is better suited for specifying features rather than relying on demonstrations. Although existing representation editing methods have proposed using language to specify new features, ...
  </details>

- **2026-10-20** — Shenyang Deng, Garvit Goyal, Tianyu Pang et al. — [How Does Orthogonalization Adapt to the Neural Network Hessian Structure? A Gradient Self Outer-Product Analysis at Initialization](http://arxiv.org/abs/2610.28975v1)
  <details><summary>📄 Abstract</summary>
  Muon orthogonalizes a weight matrix's momentum before each step, and on neural networks this simple preconditioner beats AdamW in a wide range of tasks. Existing analyses explain Muon within general optimization frameworks or on a few specific models, and many of them view orthogonalization as a preconditioner. Since the Hessian is the optimal preconditioner under a quadratic approximation of the loss, these works leave a basic question open: what makes orthogonalization suited to the Hessian of...
  </details>

- **2026-10-20** — Sasankh Munukutla, Felipe Oviedo, Danrong Zhang et al. — [From Weather to Enhanced Weathering: Weather Foundation Models for Carbon Dioxide Removal at Operational Scale](http://arxiv.org/abs/2610.28973v1)
  <details><summary>📄 Abstract</summary>
  Enhanced Rock Weathering (ERW) is a carbon removal solution with the potential to remove gigatons of CO$_2$ per year, but quantifying that removal today requires dense soil sampling and laboratory analysis. We evaluate five weather Foundation Models (FMs) as frozen encoders feeding lightweight decoders, under a leave-one-field-out protocol on 5,192 chronosequences from 264 fields across Brazil and the US. To our knowledge, this is the first holistic evaluation of weather FMs for ERW and the larg...
  </details>

- **2026-10-20** — Courtney Young, Yi Lian, Taery Kim et al. — [Navigation Explainability for Object Avoidance with LLMs for Assistive Robots](http://arxiv.org/abs/2610.28920v1)
  <details><summary>📄 Abstract</summary>
  Blind and visually impaired individuals face uncertainty when navigating unfamiliar areas. Whether a cane or a guide dog is used for navigation, this may prove to be challenging. To mitigate this challenge, we present the Context-Aware Navigation Explanation framework that explains guide dog movements for obstacle avoidance and navigation using a large language model. This system integrates perceptual context with planned future trajectories to generate natural-language explanations of robot mov...
  </details>

- **2026-10-20** — Elona Shatri, Jiří Mayer, Jan Hajič — [Data-Driven Glyph Positioning for Handwritten Music Synthesis](http://arxiv.org/abs/2610.28899v1)
  <details><summary>📄 Abstract</summary>
  Synthesised data is a common strategy to address the lack of annotated handwritten music scores in Optical Music Recognition (OMR). Smashcima is a recent synthesis framework that assembles pages of handwritten scores by sampling glyph images from MUSCIMA++ and positioning them with hard-coded rules. In this work we ask whether these rules are grounded empirically and whether a learned model for context-dependent positioning can further improve synthesis quality. We extract inter-glyph distributi...
  </details>

- **2026-10-20** — Li Zhang, Kevin Ashley — [Where Do Legal Factors Live in LLMs?](http://arxiv.org/abs/2610.28799v1)
  <details><summary>📄 Abstract</summary>
  In case-based legal reasoning, legal professionals identify legally significant fact patterns in a new dispute and compare them with those of decided cases. In AI & Law, HYPO dimensions and CATO factors represent these patterns symbolically, organizing expert knowledge distilled from case narratives as explicit, structured, interpretable, and auditable legal concepts and relations that support case comparison, legal argument, and precedent-based reasoning. Large language models (LLMs) are increa...
  </details>

- **2026-10-20** — Xiangcheng Hu, Xieyuanli Chen, Feiyi Chen et al. — [VeriCalib: Verifiable Target-Based LiDAR-Camera Calibration](http://arxiv.org/abs/2610.28791v1)
  <details><summary>📄 Abstract</summary>
  Target-based extrinsic calibration estimates the rigid transform between sensors from a few observations of a known target, and its result is commonly assessed by the root-mean-square error of the fitted residuals. However, this scalar error is computed on the same observations and therefore cannot indicate whether to accept the result, re-extract, recollect or add observations. This paper presents VeriCalib, which formulates extrinsic calibration as a verifiable estimation problem and reports a...
  </details>

- **2026-10-20** — Koshiro Saito, Daisuke Oba, Danushka Bollegala et al. — [Beyond Model Weights: Sampling-Dependent Fairness in Diffusion Language Models](http://arxiv.org/abs/2610.27584v2)
  <details><summary>📄 Abstract</summary>
  Diffusion language models (DLMs) are emerging as a practical alternative to autoregressive language models (ARLMs), yet their fairness remains largely uncharacterized. DLMs introduce sampling controls with no direct autoregressive counterpart, such as block length and remasking strategy, that directly set their speed--quality operating point. This raises a basic question: does a DLM's measured social bias remain stable across these settings? Across LLaDA, LLaDA-1.5, and Dream on Open-BBQ, we fin...
  </details>

- **2026-10-20** — Carlo Ciliberto, Alessandro Rudi, Enrico Tassi — [Proof-Carrying Contracts: Commitments AI Agents Cannot Break](http://arxiv.org/abs/2610.28484v1)
  <details><summary>📄 Abstract</summary>
  AI agents increasingly act on behalf of people or other agents, purchasing services, exchanging information and delegating work. What an agent must respect is written in instructions, policies or agreements, but text alone cannot make it comply. It may make mistakes, be redirected by what it reads, or pursue different interests. For an economy of such agents to function, parties need agreements they can rely on without inspecting or trusting one another's agents. We introduce Proof-Carrying Cont...
  </details>

- **2026-10-20** — Lili Quan, Longtian Wang, Yuelin Wang et al. — [AgenTest: Mining Business Rules to Test LLM Agents for Business Logic Bugs](http://arxiv.org/abs/2610.28116v1)
  <details><summary>📄 Abstract</summary>
  Large language model (LLM) agents increasingly execute business operations through tools and interact directly with application data and services. Beyond completing user requests, these agents must obey domain-specific business rules that constrain when actions are permitted and what data or resources may be affected. Violating such rules can lead to business logic bugs, even when a task appears successful. Detecting these bugs is difficult because the rules are rarely available as explicit, tes...
  </details>

- **2026-10-20** — Kamolchanok Saengtong, Chutirat Saengyingyongwattana, Sasin Janpuangtong et al. — [HydraPoT: A Configurable Multi-Agent Framework for Cost-Aware LLM-Assisted Honeypots](http://arxiv.org/abs/2610.27722v1)
  <details><summary>📄 Abstract</summary>
  Large language models (LLMs) can improve honeypot realism by generating dynamic, context-aware responses, but powerful cloud models incur substantial cost and latency, while lightweight models may provide weaker deception. This forces practitioners to choose between operational efficiency and interaction fidelity. In this work, we present HydraPoT, a configurable multi-agent honeypot framework that integrates traditional emulation, lightweight LLMs, and powerful cloud LLMs. HydraPoT routes each ...
  </details>

- **2026-10-20** — Guian Fang, Shengju Qian, Dongyue Lu et al. — [SolarRenderer: Few-Step Generative Reference Rendering](http://arxiv.org/abs/2610.28630v1)
  <details><summary>📄 Abstract</summary>
  Game engines and coding agents can specify the layout, motion, and camera of a scene, yet turning such coarse structure into realistic video requires a renderer that follows the structure and completes the appearance it leaves open. Existing renderers are tied to the representation of one engine, need tens of denoising steps or a costly distillation of their own, and learn from conditions that are not aligned with their target videos. We present SolarRenderer, a structure-conditioned video rende...
  </details>

- **2026-10-20** — Runguo Li, Dezhen Lu — [Weight Placement Is Not Enough: Synchronization in Multi-Node CPU Decoding of Ternary LLMs](http://arxiv.org/abs/2610.28620v1)
  <details><summary>📄 Abstract</summary>
  Ternary LLMs read only a few gigabytes per decoded token, yet on dual-socket servers with four NUMA nodes the fastest ternary runtime we found uses less than half of the memory bandwidth. Placing each weight on the node of the thread that reads it is necessary but not enough: in a decode engine with node-local weights that reuses ik_llama.cpp's kernels, threads on two generations of Xeon servers still spend 20-48% of each token waiting at synchronization points. Per-thread barrier traces show th...
  </details>

- **2026-10-20** — Rhea Sanjay Sukthanker, Riccardo Grazzi, James Hensman et al. — [Beyond 4 bits: Data-Centric Post-training Quantization and Recovery](http://arxiv.org/abs/2610.28537v1)
  <details><summary>📄 Abstract</summary>
  Post-training quantization (PTQ) compresses the weights of a trained model with limited compute and data. Down to 4 bits it is near-lossless, but at 2 bits scalar PTQ configurations fall to chance-level accuracy. We study three choices usually treated as implementation details that matter little at 4 bits but decide 2-bit quality: the quantization representation, the calibration data, and the recovery fine-tuning data, across six dense and mixture-of experts models (ranging from $3.8$ to $32$B p...
  </details>

- **2026-10-20** — Om Shivam Verma, Shaya Farahmand, Lingjun Zhao et al. — [CoGaussian: Open-Vocabulary Gaussian-based Collaborative 3D Scene Understanding](http://arxiv.org/abs/2610.28530v1)
  <details><summary>📄 Abstract</summary>
  Collaborative perception enables agents to retrieve the scene semantics and geometry beyond the field of view of any individual agent. This broader scene understanding enhances transportation safety and improves efficiency in multi-robot systems. However, existing collaborative semantic occupancy methods rely on dense 3D voxel annotations and are limited to recognizing objects within a predefined set of semantic classes. To overcome these limitations, we present CoGaussian, an open-vocabulary Ga...
  </details>


## 📊 统计 / Statistics

| 分类 / Category | 论文数 / Count |
|------|--------|
| jailbreak | 691 |
| prompt-injection | 634 |
| memory-poisoning | 56 |
| tool-use-attack | 160 |
| backdoor | 535 |
| adversarial-attack | 648 |
| privacy-leakage | 4455 |
| steganography | 83 |
| misuse | 1232 |
| red-teaming | 144 |
| vulnerability | 3727 |
| defense | 3593 |
| alignment | 3385 |
| robustness | 3684 |
| watermark | 651 |
| unlearning | 117 |
| agent-safety | 66 |
| benchmark | 70 |
| survey | 421 |
| other | 9912 |

---

📚 **全部 34264 篇论文**（2022 至今）请访问 [GitHub Pages](https://ny1024.github.io/AgentSafety-Papers/) 查看完整列表、搜索与筛选。

*Generated by AgentGuard at 2026-10-23 03:00:00*