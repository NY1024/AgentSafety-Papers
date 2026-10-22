<div align="center">

# AgentGuard 🛡️

**Daily Tracking of LLM Agent Security Papers on arXiv**

[![Auto Update](https://github.com/NY1024/AgentSafety-Papers/actions/workflows/daily-update.yml/badge.svg)](https://github.com/NY1024/AgentSafety-Papers/actions/workflows/daily-update.yml)
[![Papers](https://img.shields.io/badge/Papers-34037-blue)](#)
[![License](https://img.shields.io/badge/License-MIT-green)](#)

</div>

---

## 📖 简介 / Introduction

自动追踪 arXiv 上大模型 Agent 安全方向的最新论文，每日更新，关键词智能分类。

*Automatically tracking the latest LLM Agent security papers on arXiv, updated daily with keyword-based classification.*

**最近更新 / Last Updated**: 2026-10-22 21:07 ｜ **论文总数 / Total Papers**: 34037（近 30 天 / Recent 30 days: 5342）

🌐 **[GitHub Pages](https://ny1024.github.io/AgentSafety-Papers/)** — 查看全部 34037 篇论文（含摘要、分类筛选、搜索）/ View all 34037 papers with abstracts, filters & search

## 📑 分类导航 / Category Navigation

- **[jailbreak](#-jailbreak)** — 越狱攻击 / Jailbreak Attacks — 689
- **[prompt-injection](#-prompt-injection)** — 提示注入攻击 / Prompt Injection Attacks — 632
- **[memory-poisoning](#-memory-poisoning)** — 记忆投毒与篡改 / Memory Poisoning & Tampering — 56
- **[tool-use-attack](#-tool-use-attack)** — 工具使用攻击 / Tool-Use Attacks — 160
- **[backdoor](#-backdoor)** — 后门与投毒攻击 / Backdoor & Poisoning Attacks — 533
- **[adversarial-attack](#-adversarial-attack)** — 对抗攻击 / Adversarial Attacks — 646
- **[privacy-leakage](#-privacy-leakage)** — 隐私泄露 / Privacy Leakage — 4443
- **[steganography](#-steganography)** — 隐写与隐蔽通信 / Steganography & Covert Communication — 81
- **[misuse](#-misuse)** — 滥用与误用 / Misuse & Abuse — 1221
- **[red-teaming](#-red-teaming)** — 红队测试 / Red Teaming — 144
- **[vulnerability](#-vulnerability)** — 漏洞与攻击面 / Vulnerabilities & Attack Surfaces — 3704
- **[defense](#-defense)** — 防御与防护方法 / Defense & Protection Methods — 3569
- **[alignment](#-alignment)** — 对齐与安全约束 / Alignment & Safety Constraints — 3365
- **[robustness](#-robustness)** — 鲁棒性与可靠性 / Robustness & Reliability — 3655
- **[watermark](#-watermark)** — 水印与溯源 / Watermarking & Provenance — 641
- **[unlearning](#-unlearning)** — 机器遗忘 / Machine Unlearning — 117
- **[agent-safety](#-agent-safety)** — Agent 安全框架 / Agent Safety Frameworks — 65
- **[benchmark](#-benchmark)** — 安全评测与基准 / Safety Benchmarks & Evaluation — 70
- **[survey](#-survey)** — 综述与系统化 / Surveys & Systematization — 417
- **[other](#-other)** — 其他安全相关 / Other Security-Related — 9829

## 📄 近期论文 / Recent Papers (Last 30 Days)

> 仅展示最近 30 天中最新的 500 篇论文（含日期、作者、摘要）。近 30 天共 5342 篇，完整 34037 篇论文列表请访问 [GitHub Pages](https://ny1024.github.io/AgentSafety-Papers/)

> Showing the latest 500 of 5342 papers from the last 30 days (with date, authors & abstract). For the full list of 34037 papers, visit [GitHub Pages](https://ny1024.github.io/AgentSafety-Papers/)

### 📂 jailbreak
*越狱攻击 / Jailbreak Attacks* — 2 papers

- **2026-10-21** — Hongyu Li, Xinlong Huang, Zhan Yu et al. — [Beyond Binary Labels: Diagnostic Evaluation of LLM Safety with Prompt-Level Rubrics](http://arxiv.org/abs/2610.29225v1)
  <details><summary>📄 Abstract</summary>
  Current LLM safety benchmarks predominantly rely on binary safe or unsafe labels, lacking explanatory depth and suffering from low consistency across automated judges. To address this, we introduce DiagSafe, a diagnostic evaluation framework that moves beyond binary classification by employing prompt-level rubrics. Grounded in globally applicable AI safety policies, each rubric provides explicit criteria along two dimensions: safety, which targets concrete harms with specific exemptions to suppr...
  </details>

- **2026-10-20** — Pedro H. Barcha Correia, Matheus Azevedo de Sá, Paulo H. Gomes de Senna et al. — [Combining Long-Term Memory and LLMs Comes at a High Cost: From Prompt Injection to Persistent Compromise](http://arxiv.org/abs/2610.28810v1)
  <details><summary>📄 Abstract</summary>
  The widespread adoption of generative artificial intelligence in recent years has brought a parallel rise in prompt injection and jailbreak attacks. By embedding malicious instructions, these exploits manipulate language models to bypass intended behavior and operational boundaries. In traditional chatbots, such attacks are confined to a single session because state memory is not preserved across conversations. However, persistent memory features in modern conversational interfaces enable cross-...
  </details>


### 📂 prompt-injection
*提示注入攻击 / Prompt Injection Attacks* — 6 papers

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
*工具使用攻击 / Tool-Use Attacks* — 3 papers

- **2026-10-21** — Yufeng He — [Auditing LLM Alpha-Factor Mining: Metric Provenance and Full-Cohort Reanalysis](http://arxiv.org/abs/2610.29500v1)
  <details><summary>📄 Abstract</summary>
  Reliable evaluation of LLM-based alpha mining requires more than positive backtest summaries. We audit a preserved project at three levels: historical run counters, outcome retention, and a separately scoped public reanalysis. Three historical runs report 67, 20, and 11 keep decisions, but the comparison mixes metric populations: a mean over kept candidates is compared with a mean of per-round maxima, and successful evaluations with all returned outcomes. These artifacts cannot identify an archi...
  </details>

- **2026-10-20** — Shuo Yuan, Dacheng Li, Joseph E. Gonzalez — [D-Skill: Distilling Teacher Knowledge through Agent Skills](http://arxiv.org/abs/2610.28914v1)
  <details><summary>📄 Abstract</summary>
  Frontier language-model agents excel at complex tasks, but high inference costs make transferring their capabilities to smaller models essential. Traditional knowledge distillation achieves this through parameter updates, requiring access to the student's weights and additional training compute while encoding the transferred knowledge implicitly in the parameters. We introduce D-Skill, a framework that treats the teacher as a black box and distills its behavioral advantage into an interpretable ...
  </details>

- **2026-10-19** — Nataša Krčo, Euodia Dodd, Peter Romov et al. — [You Are the Trigger: Speaker-Activated Backdoors](http://arxiv.org/abs/2610.27210v1)
  <details><summary>📄 Abstract</summary>
  Speech models are increasingly used as an interface to AI systems, from transcription tools to voice agents. Existing audio backdoors require an attacker to introduce triggers at inference time. We study a different threat model in which the attacker compromises the model during fine-tuning but has no access to the victim's inference-time inputs. We introduce the Speaker-Activated Backdoor (SAB) setting, in which a target speaker's natural voice serves as the trigger. We develop a two-phase fine...
  </details>


### 📂 backdoor
*后门与投毒攻击 / Backdoor & Poisoning Attacks* — 5 papers

- **2026-10-21** — Arshan Dabirsiaghi — [Compaction Laundering: Provenance Destruction in Context-Compacting Coding Agents](http://arxiv.org/abs/2610.29869v1)
  <details><summary>📄 Abstract</summary>
  Coding agents that run long enough must compact their context, summarizing the conversation, discarding the original, and carrying the summary forward as memory. We show that in popular open-source coding agents this step is an exploitable trust boundary. Harnesses that flatten the typed conversation into a single plain string, marking each message with a text label such as [User]:, destroy message provenance in code, before the summarizer runs. An attacker who controls anything the agent reads ...
  </details>

- **2026-10-21** — Fabian Tritthart, Tom Zehle — [Credit Where Credit Is Due: Contrastive Attribution Topology Search for Multi-Agent Systems](http://arxiv.org/abs/2610.29292v1)
  <details><summary>📄 Abstract</summary>
  An LLM multi-agent system (MAS) is only as good as the agents it chooses to trust: its accuracy and cost hinge on its topology, meaning which agents are included and how they communicate. A single task score, however, does not reveal which agents help or hinder performance. We propose Contrastive Attribution Topology Search (CATS), which searches for compact teams within a fixed supergraph of specialized agents. An LLM attributer compares execution traces across candidate topologies and assigns ...
  </details>

- **2026-10-20** — Tanqiu Jiang, Min Bai, Sadat Shahriar et al. — [PerMIT: Securing Persistent Memory for LLM Agents via Machine-Checked Integrity Theorems and Scalable Community Trust](http://arxiv.org/abs/2610.28987v1)
  <details><summary>📄 Abstract</summary>
  Persistent memory is a largely undefended surface for injection and poisoning, and the same risk limits memory sharing among agents. We present PerMIT, a memory architecture with provable integrity guarantees under an explicit trust assumption: only user-typed inputs and values confirmed at a gate are trusted. PerMIT mediates the release and use of untrusted environment-derived values through a finite memory interface, while preserving agent-driven multi-turn planning and tool choice. Over this ...
  </details>

- **2026-10-20** — Masahiro Kaneko — [Poisoning-Based Backdoors Are Not Cryptographic](http://arxiv.org/abs/2610.28045v1)
  <details><summary>📄 Abstract</summary>
  To defend against backdoor attacks on neural networks, the defender must identify the verifier function that determines whether an input is a trigger, rather than rejecting individual triggers in isolation, since an attacker can generate new triggers satisfying the same verifier faster than they can be blocked. If a backdoor verifier could be installed with the asymmetry of a cryptographic authentication scheme, in which only the attacker can produce trigger inputs while the defender cannot reve...
  </details>

- **2026-10-19** — Qi Pang, Hanshen Xiao, Andre Manoel et al. — [Guided Diffusion for Trustworthy Synthetic Text Generation](http://arxiv.org/abs/2610.27259v1)
  <details><summary>📄 Abstract</summary>
  The rapid evolution of Large Language Models is fueled by massive datasets, yet this reliance poses severe privacy risks, as models can inadvertently memorize and even directly output sensitive training data. Synthetic text generation offers a promising solution to this challenge; however, existing methods struggle to reconcile rigorous privacy guarantees with high data utility. In this paper, we propose a new paradigm for private synthetic text generation: Guided Diffusion. Leveraging the uniqu...
  </details>


### 📂 adversarial-attack
*对抗攻击 / Adversarial Attacks* — 7 papers

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

- **2026-10-19** — Leo Elmecker-Plakolm, Lukasz Szpruch, Avishek Joey Bose et al. — [Exposing Vulnerability Monoculture Through Systemic Adversarial Robustness](http://arxiv.org/abs/2610.27353v1)
  <details><summary>📄 Abstract</summary>
  Beneath the apparent diversity of foundation models lies an increasingly homogeneous technical stack of common training pipelines, distillation methods, and data. These shared algorithmic choices can expose an otherwise distinct model ecosystem to concentrated risks leading to a vulnerability monoculture. Yet current practice in assessing adversarial robustness is restricted to individual robustness scores and attack transfer rates, leaving open the unexplored fundamental question: how many atta...
  </details>

- **2026-10-19** — Shruthi Gowda, Nikita Jain, Elahe Arani et al. — [Language Guidance for Supervised Vision Training: An Empirical Study of Generalization](http://arxiv.org/abs/2610.27208v1)
  <details><summary>📄 Abstract</summary>
  Deep neural networks have achieved remarkable success on vision benchmarks, yet they continue to struggle with many generalization challenges. Supervised vision training relies on one-hot labels, which provide limited information about semantic structure and shared attributes between classes. This limited supervision can leave visual representations vulnerable to distribution shifts, spurious correlations, texture bias, adversarial perturbations, and forgetting in sequential learning settings. W...
  </details>

- **2026-10-19** — Yuyang Zhang, Kangjie Chen, Yihui Jin et al. — [Model Exposure on One Device Endangers Others: Rethinking Edge Neural Network Security across Devices](http://arxiv.org/abs/2610.27152v1)
  <details><summary>📄 Abstract</summary>
  Neural networks (NNs) are increasingly deployed on edge devices such as mobile and IoT platforms, offering low latency and improved privacy compared to cloud-based deployment. However, on-device models embedded in mobile applications can be unpacked and exposed to adversaries, enabling cross-node attacks in centrally distributed ecosystems, where adversarial examples crafted on one compromised device transfer effectively to other nodes sharing the same models. To address this threat, we propose ...
  </details>


### 📂 privacy-leakage
*隐私泄露 / Privacy Leakage* — 34 papers

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

- **2026-10-20** — Devansh Srivastav, David Pape, Samira Abedini et al. — [Contextual Candour: Role-Aware Graduated Disclosure for LLMs over Mixed-Sensitivity Contexts](http://arxiv.org/abs/2610.28067v1)
  <details><summary>📄 Abstract</summary>
  LLMs increasingly operate over mixed-sensitivity contexts, where they must reason over information ranging from public to confidential while disclosing only what the user is authorised to receive. Existing approaches enforce access control as a binary decision: either fully answering or refusing, without regulating how much or what kind of information is revealed if access is granted, leading to over-refusal or unintended leakage. We introduce graduated disclosure, an access-control formulation ...
  </details>

- **2026-10-20** — Zhiping Zhang, Franklin Mingzhe Li, Zihao Huang et al. — [Act on Your Behalf, Beyond Your Authorization: Benchmarking LLM Agent Authorization Alignment](http://arxiv.org/abs/2610.27548v1)
  <details><summary>📄 Abstract</summary>
  When an LLM agent acts on behalf of a user, it is expected to act within the authorization scope the user grants. Existing agent evaluations largely measure task completion or harmful consequences and can therefore overlook actions that violate this delegation without producing conventional safety or privacy harms. We introduce AuthorizationBench, a benchmark of authorization alignment grounded in documented real-world cases. A scalable construction pipeline produces 286 executable tasks spannin...
  </details>

- **2026-10-20** — Hanieh Totonchi Asl, Ebrahim Nouri, Zhuoran Li et al. — [Interflow: Breaking the Offline-Online Barrier for Private AI at the Edge](http://arxiv.org/abs/2610.27431v1)
  <details><summary>📄 Abstract</summary>
  Privacy-preserving machine learning (PPML) offers a promising path toward bringing powerful AI services to the edge without exposing sensitive user data. However, its practical deployment remains constrained by the high communication, computation, and data-movement costs of secure multi-party computation (MPC), particularly during nonlinear inference. Existing MPC systems typically decouple input-independent correlated randomness generation from online execution, creating substantial memory pres...
  </details>

- **2026-10-20** — Bo Liu, Tong Li, Jiapeng Zhang et al. — [Beyond Trajectory Statistics: Community-Consistent Human Mobility Generation via Evolving User-Location Graphs](http://arxiv.org/abs/2610.28467v1)
  <details><summary>📄 Abstract</summary>
  Human mobility data are fundamental to Web-based location services and broader urban applications, and mobility generation provides synthetic trajectories when real data are costly or inaccessible. Although recent mobility generators have incorporated collective mobility patterns, they primarily focus on individual trajectories and aggregate population dynamics, leaving evolving community structures formed by user-location interactions insufficiently modeled. In this paper, we study community-co...
  </details>

- **2026-10-20** — Rohan James, Ioannis Christofilogiannis, Yuuv Jauhari et al. — [Beyond a Single Sentiment Score: Topical and Affective Dimensions of Emoji Meaning on Twitter](http://arxiv.org/abs/2610.28337v1)
  <details><summary>📄 Abstract</summary>
  Emoji are widely treated as compact affective tokens whose meaning is summarised by a single sentiment score. We argue that this picture is incomplete. From a corpus of 16{,}575 English tweets and a per-emoji metric we call \emph{stability delta} (within-class minus between-class cosine similarity of sentence embeddings), we show that emojis used in tightly clustered topical contexts also exhibit \emph{more} polarised crowd-sourced sentiment, not less. Validated against the Kralj Novak et al.\ (...
  </details>

- **2026-10-20** — Raghav Bongole, Amirreza Zamani, Tobias J. Oechtering et al. — [Lower bounds for Bayesian CVaR in interactive problems with local differential privacy](http://arxiv.org/abs/2610.28153v1)
  <details><summary>📄 Abstract</summary>
  We develop an information-theoretic method for lower bounding the prior-predictive conditional value-at-risk (CVaR) of loss in interactive statistical decision making (ISDM). A generalized Fano inequality replaces a single error event by a randomized binary statistic constructed from a bounded transform of the loss, reducing the problem to a Bernoulli $f$-divergence inequality. A bounded hinge transform yields a direct lower bound on Bayesian CVaR under a prior fixed in advance. We derive revers...
  </details>

- **2026-10-20** — Anna-Maria Halacheva, Jan-Nico Zaech, Sombit Dey et al. — [P$^3$-VLM: A Point-based Alternative for Grounded 3D Vision-Language Models](http://arxiv.org/abs/2610.28018v1)
  <details><summary>📄 Abstract</summary>
  Examining existing benchmarks for grounding in 3D VLMs reveals a pervasive "semantic leakage" in the evaluation and prompting protocols: a heavy reliance on bounding boxes as spatial prompts or representation primitives. Because bounding boxes are highly informative of object categories, they introduce a shortcut for the models to neglect visual information during 3D VLM training. We demonstrate this with a "blind" LLM that, prompted only with the box coordinates, can perform surprisingly well. ...
  </details>

- **2026-10-20** — Rajarshi Bhattacharya, Aryan Shukla, Shakeeb Murtaza et al. — [In PRAISE of Attributes: Grounding Retrieval Geometry with Query-Conditioned Subspaces for Person Re-Identification](http://arxiv.org/abs/2610.27944v1)
  <details><summary>📄 Abstract</summary>
  Person re-identification (ReID) ranks an image gallery using either an image query or a textual query. In image-to-image (I2I) ReID, viewpoint, illumination, occlusion, and background changes can make distractors appear more similar than the true match. In text-to-image (T2I) ReID, incomplete or ambiguous descriptions may omit key visual evidence. We study this problem for vision-language model (VLM) based ReID, where attributes such as clothing color and carried objects provide useful fine-grai...
  </details>

- **2026-10-20** — Pengying Wu, Zhejia Wen, Kang Ding et al. — [CovNav: Conformal Prediction-Guided Adaptive Inference for Object Goal Navigation](http://arxiv.org/abs/2610.27677v1)
  <details><summary>📄 Abstract</summary>
  In object goal navigation (ObjectNav), an embodied agent must find a target object (e.g., "find a bed") in a previously unseen environment, relying on spatial commonsense such as object co-occurrence. Large Language Models (LLMs) encode this commonsense, but deploying them on robots exposes a trade-off between reasoning quality and efficiency: cloud-based models incur latency and privacy risks, whereas small on-device LLMs are fast but prone to hallucinated spatial judgments. Hybrid reasoning LL...
  </details>

- **2026-10-20** — Ruoyao Zhang, Hongxuan Li, Jie Peng et al. — [Ensemble-Aware Structural Encoding (EASE): Conditioning Protein Encoders on Peptide Conformational Ensembles](http://arxiv.org/abs/2610.27638v1)
  <details><summary>📄 Abstract</summary>
  Protein foundation models provide transferable representations for downstream peptide prediction tasks. However, existing representations typically reduce a peptide to a single sequence or structure, which may miss conformational variability relevant to key peptide properties, including antibacterial activity, hemolysis, toxicity, stability, and binding. For example, protease resistance correlates more strongly with conformational dynamics measured by hydrogen exchange than with average helicity...
  </details>

- **2026-10-20** — Tao Yang, Chengxi Yang, Ben J. Sekely et al. — [Ultra-Fast 4H-SiC AC-LGAD for 4D Tracking Applications](http://arxiv.org/abs/2610.27535v1)
  <details><summary>📄 Abstract</summary>
  4H-SiC low gain avalanche detectors (LGADs) combine internal gain with the high carrier saturation drift velocity, thermal stability, and low leakage current of SiC. AC-coupled readout (AC-LGAD) adds position information to the precise timing, which enables 4D tracking. This work reports the first experimental demonstration of a 4H-SiC AC-LGAD. Devices with a $1.0\times1.0$~mm$^2$ active area and a $2\times2$ array of AC-coupled pads at a pitch of 500~$μ$m were fabricated with two gain-layer dop...
  </details>

- **2026-10-20** — Laurent Mombaerts, Jonathan Taws, Jacopo Gargano et al. — [Training-Free Continual Learning for Multimodal Forecasting via Prompt Evolution](http://arxiv.org/abs/2610.27468v1)
  <details><summary>📄 Abstract</summary>
  Adapting a forecasting system to a changing world classically means retraining. We ask whether the task of continually learning regimes for time series forecasting can be represented by a piece of text: a guidance block, evolved by outcome-driven reflection and used in a frozen LLM forecaster's prompt. On a refreshed multimodal benchmark (weekly search indices, daily currencies, daily commodities, each window paired with web-retrieved news), we run GEPA-style prompt evolution under strict contam...
  </details>

- **2026-10-19** — Ethan Seefried, Romit Ghosh, Sharmin Afrose et al. — [Benchmarking the Quantum Leap: Auditing LLM Evaluation for Quantum Code Generation](http://arxiv.org/abs/2610.28678v1)
  <details><summary>📄 Abstract</summary>
  Large language models (LLMs) can generate quantum programs, but reliable evaluation remains difficult because benchmarks differ in task composition, scoring, and failure handling. We evaluate 15 hosted frontier, open-weight, quantum-specialized, and retrieval-augmented models on five quantum code-generation suites (530 tasks), plus 10 models on our new QuantumBenchEval (QBE) benchmark (96 tasks across six topics). We report bootstrap confidence intervals, multiplicity-adjusted paired comparisons...
  </details>

- **2026-10-19** — Wenyue Chen, Yuhan Cheng, Ruixin Yang et al. — [Steering Vision-Language Models for Visual-Contextual Privacy in Location Disclosure](http://arxiv.org/abs/2610.27323v1)
  <details><summary>📄 Abstract</summary>
  Vision-language models (VLMs) can infer sensitive information such as geolocation from subtle visual cues, creating privacy risks when responses disclose more detail than the visual context warrants. We study visual-contextual privacy in geolocation disclosure, where a VLM should reveal location information only at the granularity appropriate to the visual context depicted in the image. We first show that this contextually appropriate granularity is recoverable from pre-generation hidden states,...
  </details>

- **2026-10-19** — Mingchen Li, Zifan Peng, Kewei Sha et al. — [Profile-DP: Differential Privacy for User-Controlled Profile Release in Personalized LLM Inference](http://arxiv.org/abs/2610.27213v1)
  <details><summary>📄 Abstract</summary>
  Personalized large language models (LLMs) increasingly rely on profile-conditioned inference, pairing public requests with rich, user-specific facts. This paradigm exposes the user profile itself, together with the user's explicit sharing preferences. We introduce Profile-DP, a policy-aware local differential privacy framework designed specifically for user-profile release in personalized LLM inference. Profile-DP provably bounds the release of user-withheld facts while treating public instructi...
  </details>

- **2026-10-19** — Oussema Dhaouadi, Zuria Bauer, Johannes Michael Meier et al. — [MatchCityLoc: Aerial Localization in LoD City Models via Surface Normal Matching](http://arxiv.org/abs/2610.27110v1)
  <details><summary>📄 Abstract</summary>
  Autonomous Unmanned Aerial Vehicle (UAV) navigation in urban environments requires precise pose estimation. Because Global Navigation Satellite System (GNSS) signals are often unreliable in cities, visual localization serves as a crucial complement. Within this domain, textureless Level-of-Detail (LoD) city models provide a lightweight and privacy-preserving substitute for heavy 3D textured meshes. However, localizing against abstract geometry is challenging. Existing pipelines typically score 2...
  </details>

- **2026-10-19** — Yuxuan Chen, Yang Xiao, Jack Sun et al. — [Beyond Two Tracks: Speaker-Anchored Full-Duplex Dialogue Recovery](http://arxiv.org/abs/2610.27109v1)
  <details><summary>📄 Abstract</summary>
  Spoken interaction is moving from alternating turns to full-duplex conversation, where an agent listens while speaking. Learning this coordination requires natural dialogue with persistent speaker-resolved tracks, a data requirement that remains difficult to satisfy at scale. Generative recovery offers a route from ordinary recordings, but recovering two voices is not enough: their track assignments can drift as the conversation unfolds. We address this missing link with speaker-anchored routing...
  </details>


### 📂 steganography
*隐写与隐蔽通信 / Steganography & Covert Communication* — 1 papers

- **2026-10-20** — Hieu Tran, Hong Yu — [Is Anyone Enforcing the Cartel? What Reinforcement Learning Teaches LLM Agents in Markets](http://arxiv.org/abs/2610.28787v1)
  <details><summary>📄 Abstract</summary>
  Evaluations of large language model (LLM) agents report that pricing agents collude at others' expense. Yet collusion is defined by enforcement: a cartel, in which competitors share monopoly profits, holds only if a member who cheats is punished. We introduce an audit that tests enforcement by forcing a member to cheat in counterfactual copies of a market, and use it to study what reinforcement learning (RL) teaches agents in pricing and trading. Small LLMs trained by RL learn what their trainin...
  </details>


### 📂 misuse
*滥用与误用 / Misuse & Abuse* — 19 papers

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

- **2026-10-20** — Zijian Yu, Hangwei Zhang, Jun Lan et al. — [WildAIGC-Bench: Can AI Image Detectors Handle the Wild? A Benchmark of Generated and Edited Images in Online Circulation](http://arxiv.org/abs/2610.28087v1)
  <details><summary>📄 Abstract</summary>
  AI-generated images linked to news events and online claims can mislead audiences, enable fraud, or cause public controversy. We introduce WildAIGC-Bench, built through recurring collection across news websites, fact-checking sources, and related social media content. The pipeline combines broad coverage, timely updates, and human-verified labels through scheduled discovery, automatic screening and preliminary annotation, and human review of image-specific evidence. The benchmark contains 407 ve...
  </details>

- **2026-10-20** — Yali Du, Yunji Zhang, Ming Li — [Hallucinations of Large Language Models in Cross-Language Code Translation: Phenomena and Mitigation](http://arxiv.org/abs/2610.27868v1)
  <details><summary>📄 Abstract</summary>
  Code translation converts source code from one programming language to another while preserving its functionality. Although Large Language Models (LLMs) have improved code translation, their outputs still contain hallucinations: generated code that conflicts with the source program, violates target-language facts, or introduces contextually inconsistent dependencies. These failures are especially harmful in translation because small semantic deviations can silently change program behavior. Exist...
  </details>

- **2026-10-20** — Hayden Moore, Abhinav Verma, Anshuman Dutt — [Tracing Recurrent and Emergent Hallucination Patterns in Decomposed Text-to-SQL Generation](http://arxiv.org/abs/2610.27720v1)
  <details><summary>📄 Abstract</summary>
  Large language models can achieve strong Text-to-SQL benchmark performance while still producing schema and query-logic errors. Most evaluations characterize such failures only in the final generated query, making it difficult to determine whether a related error was also observed in an earlier, simpler step or appears only at the final stage. We present a drill-down evaluation framework that decomposes Text-to-SQL queries into progressively more complex executable sub-queries and corresponding ...
  </details>

- **2026-10-19** — Aidan Sirbu, Charles Y. Zhang, Yuanjia Yang et al. — [A latent control model for realistic rodent motion](http://arxiv.org/abs/2610.27279v1)
  <details><summary>📄 Abstract</summary>
  The development of embodied models of animal behavior is a major goal of the neuro-AI community. Embodied models will enhance our ability to make direct comparisons between biological and artificial agents. To make such comparisons effective, though, we need embodied models that actually move like animals. Previous work has developed virtual animal bodies and techniques for training realistic motion through imitation. However, to date, there is no system for embodied animal modeling that produce...
  </details>

- **2026-10-19** — Arnav Grover — [Refuses When Asked, Complies When Acting: A Runtime Safety Check for Robot Control Loops](http://arxiv.org/abs/2610.27350v1)
  <details><summary>📄 Abstract</summary>
  Frontier models can control robots through agent harnesses that loop on one question: what motion comes next toward the user's goal? We show that this default loop carries out harmful instructions. With GPT-6 Astra controlling a low-cost SO-101 arm through the Inspect Robots harness on three household tasks whose hazard is common knowledge, such as "put the knife in the toy basket", the policy refused 0% of 15 trials, attempted the harm every time, and completed it in 27%. Its one exit, give_up,...
  </details>

- **2026-10-19** — Jalil Alva, David Harper, Abigail E. Thornton et al. — [Global Security Blind Spots: Translation as a Safety Bypass in Low-Resource Languages](http://arxiv.org/abs/2610.27304v1)
  <details><summary>📄 Abstract</summary>
  Large language models are deployed globally, yet safety alignment and evaluation remain concentrated in English: harmful requests refused in English can elicit unsafe completions when translated into low-resource languages. We evaluate ten widely deployed LLMs across 79 languages (English plus 78 low-resource) under a translation-bypass threat model, using a metric conditioned on English safety, which separates translation bypass from unsafety already present in English. English safety does not ...
  </details>

- **2026-10-19** — Chenhan Lyu, Amir Rahmani — [Auditing Safety Preference Supervision with Recorded Derivations](http://arxiv.org/abs/2610.27266v1)
  <details><summary>📄 Abstract</summary>
  Preference labels align model training, but the judgments behind them are difficult to inspect or verify. In this paper, we examine how preference construction can be checked when intermediate decisions are recorded, and which of them remain uncertain. We present Symbolic Preference Labeling, a method in which a pretrained language model classifies predefined attributes of prompts and responses. Explicit rules assign response verdicts, and a fixed verdict ranking determines the preference label....
  </details>

- **2026-10-19** — Carson Sobolewski, Anjali Parashar, Fei Chen et al. — [What Would Removing This Corruption Change? Failure Attribution for Vision-Language-Action Models](http://arxiv.org/abs/2610.27277v1)
  <details><summary>📄 Abstract</summary>
  Vision-language-action (VLA) models are sensitive to visual corruptions, but knowing that a corruption is typically harmful does not establish whether removing it would benefit the current episode. Furthermore, when several corruptions co-occur, deciding what to correct requires understanding which ones contribute to failure risk and how much their removal would help. We define this problem as failure attribution. Detecting corruption presence alone cannot answer this question, as corruptions ca...
  </details>

- **2026-10-19** — Yanan Ma, Yang Wang, David Le et al. — [Which Agent's Skill Should Change? Group-Relative Credit Assignment for Evolving Multi-Agent Teams](http://arxiv.org/abs/2610.27227v1)
  <details><summary>📄 Abstract</summary>
  Cooperative language-model agents can improve without weight updates by revising reusable skills, but only if a shared team reward is traced to the responsible agent and skill. Existing methods credit the skills present in each trajectory, yet presence is not responsibility: a harmful skill active in successful runs still earns positive credit. We present \textbf{GRSE}, \textbf{G}roup-\textbf{R}elative \textbf{S}kill \textbf{E}volution, which assigns behavioral credit by comparison: inspired by ...
  </details>


### 📂 red-teaming
*红队测试 / Red Teaming* — 1 papers

- **2026-10-19** — Hao Li, Tongyan Hu, Weidi Luo et al. — [AutoRedClaw: Automated Red-Teaming for Claw-Style Agents](http://arxiv.org/abs/2610.27244v1)
  <details><summary>📄 Abstract</summary>
  Agent systems are shifting from task-scoped tool-use agents to persistent, personalized assistants such as OpenClaw. These claw-style agents maintain configuration files (e.g., AGENTS.md), long-term memory, and reusable skills. Once poisoned, this persistent state is repeatedly reloaded into the agent's context, creating persistent threats across tasks and sessions. Existing security evaluation systems struggle to evaluate these complex claw-style systems since they rely heavily on manually cons...
  </details>


### 📂 vulnerability
*漏洞与攻击面 / Vulnerabilities & Attack Surfaces* — 58 papers

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

- **2026-10-19** — Hyunji Alex Nam, Michael Dennis, Natasha Jaques et al. — [Evolving Self-tuning Benchmarks for Long-Horizon Tool Use](http://arxiv.org/abs/2610.27307v2)
  <details><summary>📄 Abstract</summary>
  For AI assistants to move beyond simple chat interfaces and reliably assist users with applications like Gmail, Venmo, and Slack, we need to improve their tool-use capabilities. However, existing tool use benchmarks are still limited and difficult to scale because they rely on human supervision or are too domain-specific. To make data generation scalable, we propose, TURTLE (Tool Use Related Tasks with Long-Horizon Evolution), an Unsupervised Environment Design (UED) approach to evolve existing ...
  </details>

- **2026-10-19** — Nishant Abhishek, Ping Charoenwet, Kla Tantithamthavorn — [AgenticVulHunter: Bringing Local Agentic Vulnerability Hunting to Your Terminal](http://arxiv.org/abs/2610.27383v1)
  <details><summary>📄 Abstract</summary>
  Finding vulnerabilities early, before they can affect the production system, is important for reducing the risk of any software attacks. However, detecting vulnerabilities during secure code review is still difficult because the vulnerable code logic may depend on lines found across different repository files. Recent approaches such as AgenticSCR have shown that LLM agents can explore repository files and use security knowledge to improve secure code review. However, these approaches mainly rely...
  </details>

- **2026-10-19** — Saptaparna Bhattacharya — [Pretraining on boosted boson decays for polarization tagging of hadronic $W$ bosons](http://arxiv.org/abs/2610.27346v1)
  <details><summary>📄 Abstract</summary>
  Longitudinally polarized weak bosons probe the unitarization of vector-boson scattering. At large boosts, longitudinal and transverse $W$ bosons produce jets with the same mass and two-prong structure, distinguished only by the decay angle. Longitudinal bosons are rare: they occur in only 0.3% of $W$+jet events at these large boosts. We ask where the polarization information of a boosted $W$ boson lies and how much a tagger can recover. Requiring both decay quarks within the jet truncates the de...
  </details>

- **2026-10-19** — Zerui Chen, Changrui Chen, Fei Ni et al. — [Look Before You Reason: Implicit Visual Thinking for Efficient Multimodal Reasoning](http://arxiv.org/abs/2610.27341v1)
  <details><summary>📄 Abstract</summary>
  Vision-language models (VLMs) have advanced rapidly in multimodal reasoning, yet they remain limited on tasks requiring fine-grained understanding of small or easily overlooked image regions. Recent thinking with images approaches mitigate this limitation by allowing models to inspect images through operations such as zooming, cropping, or code execution. While effective, their multi-turn interactions with VLMs introduce redundant token computation and slow inference, and separate region inspect...
  </details>

- **2026-10-19** — Pablo P. Rejo, Manuel Fernández-Veiga, Ana Fernández-Vilas et al. — [Orchestrating Key Scarcity: Global Capacity Allocation in Hybrid QKD-PQC Networks](http://arxiv.org/abs/2610.27332v1)
  <details><summary>📄 Abstract</summary>
  This article presents a Distributed Key Management System (DKMS) that provisions quantum-safe symmetric encryption keys to applications across a network. To overcome the distance and rate limitations inherent to Quantum Key Distribution (QKD), the architecture adopts a hybrid design: it utilizes multi-hop trusted relays for physical key transport, while applying an end-to-end Post-Quantum Cryptography (PQC) layer to ensure the relayed key material remains strictly protected from intermediate nod...
  </details>

- **2026-10-19** — Hyunji Alex Nam, Michael Dennis, Natasha Jaques et al. — [Evolving Self-tuning Benchmarks for Long-Horizon Tool Use](http://arxiv.org/abs/2610.27307v1)
  <details><summary>📄 Abstract</summary>
  For AI assistants to move beyond simple chat interfaces and reliably assist users with applications like Gmail, Venmo, and Slack, we need to improve their tool-use capabilities. However, existing tool use benchmarks are still limited and difficult to scale because they rely on human supervision or are too domain-specific. To make data generation scalable, we propose, TURTLE (**T**ool **U**se **R**elated **T**asks with **L**ong-Horizon **E**volution), an Unsupervised Environment Design (UED) appr...
  </details>

- **2026-10-19** — Taozheng Zhu, Shixiong Jiang, Fanxin Kong — [Vulnerability Analysis for Safe Multi-Agent Reinforcement](http://arxiv.org/abs/2610.27293v1)
  <details><summary>📄 Abstract</summary>
  Safe Multi-Agent Reinforcement Learning (SMARL) aims to learn cooperative control policies under prescribed safety constraints. Al- though existing SMARL methods focus on enforcing safety during policy optimization, their vulnerability remains largely unexplored. This paper investigates inference-time observation attacks against SMARL, where an adversary perturbs the observations of a subset of agents, thereby altering the actions produced by their policies. We propose MinMax Attack, an attack f...
  </details>

- **2026-10-19** — Rui Melo, Andre Catarino, Claudia Mamede et al. — [When Models Know but Can't Linearly Say: Relational Encoding Limits Linear Vulnerability Classification in Code LLMs](http://arxiv.org/abs/2610.27257v1)
  <details><summary>📄 Abstract</summary>
  Large language models can detect vulnerable code, yet the form of vulnerability encoding in their representations remains unclear. We analyze 8 code models spanning 6.7B-15B parameters on C programs using three datasets (DELTASECOMMITS, SVEN, and PRECISE-BUGS), comparing two diagnostic tasks on the same representations: identifying what patterns the code instantiates, and determining whether it is vulnerable. Models encode the first with high fidelity. Under the studied paired C-code datasets an...
  </details>

- **2026-10-19** — Ameya D. Jagtap — [Glass-Box Deep Reinforcement Learning for High-Speed Flow Control](http://arxiv.org/abs/2610.27132v1)
  <details><summary>📄 Abstract</summary>
  Deep reinforcement learning (DRL) is challenging long-held assumptions in active flow control. By learning directly from interaction with a flow, DRL agents can find actuation strategies for nonlinear, unsteady flows without explicit models, often exploiting mechanisms that classical control would not anticipate. High-speed flows are a demanding test of this promise: shocks, shock/boundary-layer interactions, transition, aerothermal loading and microsecond-scale dynamics strain both algorithms a...
  </details>

- **2026-10-19** — Rajneil Baruah, Subhadeep Mondal, Sunando Kumar Patra et al. — [This is SParTA: A modular, efficient and scalable transformer architecture for jet-tagging](http://arxiv.org/abs/2610.27106v1)
  <details><summary>📄 Abstract</summary>
  We present the Sparse Particle-interaction Transformer Architecture (SParTA), a modular, scalable, and efficient transformer for jet tagging at high-energy colliders. Exploiting the steeply falling transverse-momentum ($p_T$) spectrum of jet constituents, SParTA factorizes constituent processing into two topological regimes. Ordered by descending $p_T$, only the $N$ hardest constituents (the hard core) participate in quadratic $O(N^2)$ differential interaction attention driven by pairwise physic...
  </details>

- **2026-10-19** — Osama Shabih, Dayam Nadeem, Shahab Saquib Sohail et al. — [Fluent but Fallible: Benchmarking Hallucination and Factual Reliability in Large Language Models](http://arxiv.org/abs/2610.27034v1)
  <details><summary>📄 Abstract</summary>
  Large Language Models (LLMs) have significantly advanced natural language processing and artificial intelligence applications through their capabilities in reasoning, text generation and knowledge retrieval. However, LLMs are still vulnerable to two important challenges: hallucination, generating factually incorrect or fabricated content, and response deviation, meaning systematic deviations from ground-truth responses. These limitations raise serious concerns regarding reliability and trustwort...
  </details>

- **2026-10-19** — Phurinat Polasa, Thanapon Thanadunpremdet, Phatthanasak Kraiduang et al. — [Teaching AI Agent to Play Poker Strategically Through Preference Optimization](http://arxiv.org/abs/2610.27028v1)
  <details><summary>📄 Abstract</summary>
  A poker agent can make a legal move and still make a strategically poor one. We ask whether compact AI agents can exhibit strategic behavior under hidden information and whether preference optimization can improve beyond static and zero-shot policies. We first evaluate a static baseline and three frozen language models: SmallThinker, Qwen3, and Gemma-3 whose performance varies substantially between exact-game and six-player evaluation. We therefore propose Strategic Preference Optimization with ...
  </details>

- **2026-10-19** — Tue Le, Anh Nguyen Hoang, Gabriel Sasseville et al. — [Secure Agentic Coding through Counterexample-Grounded Feedback](http://arxiv.org/abs/2610.25916v2)
  <details><summary>📄 Abstract</summary>
  As coding models and agent harnesses become more capable, reliable security verification is becoming a central bottleneck. Improving secure code generation requires a signal whose reported progress remains aligned with actual program behavior under optimization; otherwise, an optimizer can improve the signal's verdict without removing the underlying vulnerability. Existing model-based approaches require models to either infer program behavior from source code or specify correct outcomes for adve...
  </details>

- **2026-10-19** — Qihao Wang, Hang Su, Fan Cui et al. — [Think Before You Transcribe: Context-Steered Reasoning for Hotword-Aware Speech Recognition](http://arxiv.org/abs/2610.26986v1)
  <details><summary>📄 Abstract</summary>
  Contextual automatic speech recognition (ASR) improves rare-entity recognition by supplying candidate hotwords, but retrieved candidates may be incomplete or incorrect. A reliable system must therefore exploit a relevant candidate without allowing unsupported alternatives to override the acoustic evidence. We propose a context-steered reasoning framework that generates a short, audio-grounded caption before transcription. This task-specific representation lets the model assess candidate relevanc...
  </details>

- **2026-10-19** — Youran Dong, Junfeng Yang, Wei Yao et al. — [Newton-Based Methods for Bilevel Optimization Beyond Lower-Level Strong Convexity](http://arxiv.org/abs/2610.26839v1)
  <details><summary>📄 Abstract</summary>
  Bilevel optimization provides a framework for machine learning tasks such as hyperparameter optimization, data reweighting, and meta-learning. Existing Newton-based bilevel methods typically rely on the classical hypergradient formula, which is generally unavailable when lower-level solutions are nonunique and the lower-level Hessian is singular. We develop two Newton-based methods beyond lower-level strong convexity by exploiting curvature shared by the lower-level and multiplier updates. Newto...
  </details>

- **2026-10-19** — Ming Yang, Yaqi Yin, Zhibo Wang et al. — [AGR: Agentic Generative Retrieval with Tool-Augmented Search](http://arxiv.org/abs/2610.26831v1)
  <details><summary>📄 Abstract</summary>
  Large-scale search and recommendation systems derive much of their retrieval quality from rich, heterogeneous features, yet existing generative retrieval (GR) methods struggle to exploit such feature ecosystems efficiently. Static feature injection either encodes all available signals or places them according to predetermined schemes, increasing serving cost and introducing irrelevant or conflicting evidence. More fundamentally, existing methods cannot adaptively determine when a feature is need...
  </details>

- **2026-10-19** — Zhuofan Josh Ying, Guanglong Sun, Nolan Ho et al. — [Scaling Parameter-Efficient Fine-Tuning for Brain Encoding](http://arxiv.org/abs/2610.26802v1)
  <details><summary>📄 Abstract</summary>
  Brain encoding models aim to predict neural responses to stimuli. The most widely used approach fits readouts from frozen pretrained backbones. Using neural data to train large models from scratch or fully fine-tune them after task-pretraining has proven difficult because neural data is costly and limited. We show that parameter-efficient fine-tuning (PEFT) enables us to effectively adapt very large pretrained backbones for brain encoding with a small number of trainable parameters. To make it c...
  </details>


### 📂 defense
*防御与防护方法 / Defense & Protection Methods* — 43 papers

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

- **2026-10-20** — Christoph Riedl, Fernando E. Rosas — [Claims of emergence in AI should be grounded in information decomposition](http://arxiv.org/abs/2610.28479v1)
  <details><summary>📄 Abstract</summary>
  When a language model develops capabilities not traceable to its individual components, when a multi-agent AI system outperforms each agent on its own, or when a human-AI pair succeeds where either fails in isolation, AI researchers describe it as a case of ``synergy'' or ``emergence''. However, these are usually informal assessments not supported by a theoretical framework, making these claims impossible to compare or even meaningfully dispute. Here we argue that \emph{information decomposition...
  </details>

- **2026-10-20** — Tim Bakker, Christos Louizos — [Relative Representations Enable Portable White-Box Monitoring Across Language Models](http://arxiv.org/abs/2610.28366v1)
  <details><summary>📄 Abstract</summary>
  Independently trained autoregressive language models often acquire similar capabilities, but it remains unclear whether their internal representations organize behaviorally relevant information in compatible ways. We show that models do in fact organize information similarly by using specific behavioral probes that operate on compatible representations. This unlocks portable white-box monitoring: a probe developed and validated on one model can be reused when the model changes, without requiring...
  </details>

- **2026-10-20** — Tianyi Lorena Yan, John Hewitt — [Reward Misspecification Degrades Chain-of-Thought Monitorability](http://arxiv.org/abs/2610.28303v1)
  <details><summary>📄 Abstract</summary>
  Monitoring the chain-of-thought (CoT) of language models (LMs) is a key strategy for detecting and preventing misbehaviors for AI safety. As such, it is critical to identify reinforcement learning (RL) practices that lead to unmonitorable chain-of-thought. One such practice may be unavoidable: reward misspecification. As RL environments become more complex, it is infeasible to have perfect verification, and models are rewarded for behaviors that are different from the true task intent. We show t...
  </details>

- **2026-10-20** — Chucheng Xiang, Runze Wang, Zhi Deng et al. — [GALA: Geometry-Aware Language Model for Controllable Object Arrangement](http://arxiv.org/abs/2610.28280v1)
  <details><summary>📄 Abstract</summary>
  Reasoning about fine-grained placement constraints, such as support and containment, is essential for realistic 3D scene creation. It remains a significant challenge for existing methods that rely on simplified object representations like oriented bounding box (OBB), which are blind to the detailed geometry. To address this limitation, we introduce GALA, a geometry-aware language model with explicit point cloud perception for controllable object placement. Our model performs autoregressively by ...
  </details>

- **2026-10-20** — Jiapu Wang — [Temporal Evidence-Parameter Co-Alignment for LLM Reasoning over Temporal Knowledge Graphs](http://arxiv.org/abs/2610.28176v1)
  <details><summary>📄 Abstract</summary>
  Large Language Models (LLMs) often struggle with temporally grounded reasoning because their static parametric memory is misaligned with the dynamic evolution of real-world knowledge. Although RAG and Parameter-Efficient Fine-Tuning (PEFT) provide practical ways to enhance LLMs, they remain insufficient for temporal reasoning. Existing retrieval methods typically prioritize semantic relevance while overlooking temporal validity, event order, and evolutionary dependencies, resulting in evidence t...
  </details>

- **2026-10-20** — Zhipeng Cao, Taoran Wu, Weiru Cui et al. — [Anytime-Valid Runtime Monitoring of Learned Barrier Certificates](http://arxiv.org/abs/2610.27726v1)
  <details><summary>📄 Abstract</summary>
  Learned barrier certificates provide a principled mechanism for establishing safety of stochastic systems, but their validity may deteriorate during deployment when the underlying dynamics differ from those used for training. We propose an anytime-valid runtime monitor that audits a learned barrier certificate using observed closed-loop trajectories. The monitor is intended to detect loss of statistical support for the deployed barrier condition; it does not by itself guarantee detection before ...
  </details>

- **2026-10-20** — Anmol Pandey, Aditya Jain, Liang Chen et al. — [Local Allow, Global Deny: Why Per-Action Authorization Does Not Compose in LLM Agents](http://arxiv.org/abs/2610.27620v1)
  <details><summary>📄 Abstract</summary>
  Autonomous LLM agents act through tools under per-action authorization: a local guard screens each tool call in isolation. We show that local authorization does not compose into global authorization. A compositional authorization failure (CAF) is a locally authorized execution, or a pair of locally authorized executions, that violates a global policy spanning intent, purpose, provenance, consent, and delegation. We characterize CAFs along two axes, expressiveness (single-trace safety versus rela...
  </details>

- **2026-10-20** — Zhikang Chen, Yueqing Sun, Sen Cui et al. — [KPHarness: Co-Evolving Knowledge and Probing for Long-Horizon Gaming Harnesses](http://arxiv.org/abs/2610.27417v1)
  <details><summary>📄 Abstract</summary>
  A failed gaming trajectory reveals that an agent needs intervention, but not necessarily how its execution harness should change. Effective harness adaptation therefore requires gathering diagnostic evidence, rather than merely proposing alternative recovery rules. We present KPHarness, a framework that adapts the external execution harness of a frozen vision-language-action model through knowledge-probing co-evolution. Recovery knowledge supplies context-specific intervention hypotheses that gu...
  </details>

- **2026-10-20** — Yao Huang, Siyuan Chen, Zhenghan Zhou et al. — [Why Static Probes Fail: Context Determines Deception Feature Composition](http://arxiv.org/abs/2610.27577v1)
  <details><summary>📄 Abstract</summary>
  With increasing autonomy, Large Language Models (LLMs) may engage in deceptive behaviors, such as scheming to pursue misaligned goals or sandbagging to escape oversight. Monitoring outputs alone is insufficient, as models can produce seemingly benign responses while harboring misaligned internal objectives. While mechanistic approaches like linear probing are promising, they rely on the assumption that deception corresponds to a single direction in representation space. We demonstrate that such ...
  </details>

- **2026-10-20** — Yue Xu, Xiyang Wang, Hui Liu et al. — [From Tokens to Files: Multi-Granularity Detection and Localization of AI-Involved Code](http://arxiv.org/abs/2610.27863v1)
  <details><summary>📄 Abstract</summary>
  The increasing use of large language models for code generation calls for methods that distinguish purely human-written code from AI-involved code: files in which any part, however small, was generated or substantially modified by a model. Beyond flagging such files, we aim to localize the lines or blocks attributable to AI. Existing approaches compress a file into a single score, from surface stylistic features or a global code representation, which averages away the evidence when only a few bl...
  </details>

- **2026-10-20** — Xu Hu, Haoming Li, Yuxiang Wang et al. — [CUA-Recovery: Benchmarking Error Recovery in Long-Horizon Computer-Use Agents](http://arxiv.org/abs/2610.27645v1)
  <details><summary>📄 Abstract</summary>
  As computer-use agents (CUAs) move to long-horizon workflows spanning multiple applications, undetected errors can silently corrupt persistent state and cause cascading failures in subsequent actions. Reliable error detection and recovery have become critical bottlenecks for building robust CUAs. However, existing benchmarks focus primarily on end-to-end task performance, providing limited insight into whether agents can detect and recover from errors during execution. The few benchmarks that ev...
  </details>

- **2026-10-20** — Chuanbo Zhu, Run Luo, Weibo Zhao et al. — [AudiPsy: Evidence-Grounded Multimodal Reasoning over Spoken Counseling Conversations for Depression Assessment](http://arxiv.org/abs/2610.27567v1)
  <details><summary>📄 Abstract</summary>
  Depression assessment from counseling speech requires integrating textual and acoustic psychological evidence across turns, yet existing end-to-end classification approaches lack explicit multimodal evidence interpretation and context-aware reasoning. We propose AudiPsy, an evidence-grounded omni-LLM for depression assessment over spoken counseling conversations. AudiPsy employs an Observation-Assessment-Summary (OAS) paradigm to integrate dialogue transcripts, textual and acoustic emotions, and...
  </details>

- **2026-10-20** — Qizhou Wang, Jiawen Zhu, Guansong Pang et al. — [AnomalyJev: Towards Evaluating Image Anomaly Explanations via Claim-Level Verification](http://arxiv.org/abs/2610.27565v1)
  <details><summary>📄 Abstract</summary>
  Recent multimodal LLM (MLLM)-based anomaly detection (AD) methods can generate textual explanations that help interpret their predictions. However, reliably and efficiently evaluating these explanations remains challenging. While LLM judges can assess explanations through structured rubrics, they often require substantial token generation, making evaluation costly and difficult to scale. We instead propose to anchor evaluation in the available ground truth by extracting verifiable claims from ea...
  </details>

- **2026-10-20** — Daniel Weiner, Raj Korpan — [Evaluating Social Reasoning in Embodied Vision-Language Models](http://arxiv.org/abs/2610.27496v1)
  <details><summary>📄 Abstract</summary>
  Foundation models now serve as reasoning layers for robot teams, but it remains unclear whether embodiment-specialized vision-language models (VLMs) preserve the social-reasoning capabilities of general-purpose VLMs. We evaluate Gemini Robotics-ER on SHREC, a benchmark of real human-robot social interactions, and compare it with published general-purpose VLM baselines. Robotics-ER outperforms GPT-4o-mini on error/competence detection but performs worse on detailed social-attribute judgments; add...
  </details>

- **2026-10-19** — Alex Clay, Ernesto Jimenez-Ruiz, Pranava Madhyastha — [Looking Into The Past: The Impact of Context on Detecting Deceptive Statements](http://arxiv.org/abs/2610.27407v1)
  <details><summary>📄 Abstract</summary>
  Deception detection typically considers messages in isolation. Previous works in claim verification and role detection have displayed that additional information such as gameplay history is crucial to successful predictions. In this work, we demonstrate the value of preceding gameplay dialogue when applied to deceptive message detection within the hidden role game of Avalon. The findings show that LLMs can see improvement across a number of metrics, including accuracy by up to 31\% with the addi...
  </details>

- **2026-10-19** — Salimeh Sekeh, Mary Wisell — [A Theoretical Analysis of Environment-Aware Out-of-Distribution Detection for Vision-Language Models](http://arxiv.org/abs/2610.27211v1)
  <details><summary>📄 Abstract</summary>
  Continual vision-language models (VLMs) encounter a stream of environments and must also reject inputs that do not belong to the environment at hand.   Class information from earlier environments can aid out-of-distribution (OOD) detection, yet existing detectors score each environment in isolation, and when previous environments help or hurt is theoretically unclear. We develop a theory of environment-aware OOD detection built on contribution scores, pairwise cosine expectations measuring how t...
  </details>

- **2026-10-19** — Chenpan Li, Thies Brockmoeller, Stefanie Jegelka et al. — [On the Fragility of Tasks under Composition: Implicit Budgeting in Language Models](http://arxiv.org/abs/2610.27190v1)
  <details><summary>📄 Abstract</summary>
  Modern language models are increasingly asked to handle several tasks within a single prompt. Doing so requires solving each task correctly while integrating the resulting answers into a coherent response. In this paper, we identify a fundamental limitation in this process, where models make substantially more errors when tasks are composed, even when they can solve every constituent task reliably in isolation. This degradation cannot be fully explained by the accumulation of independent errors....
  </details>

- **2026-10-19** — Bo Yan, Qi Zhang, Ziwen Kan et al. — [PROVISO: Provenance-Informed Action Selection for Secure LLM Agents](http://arxiv.org/abs/2610.27115v1)
  <details><summary>📄 Abstract</summary>
  LLM agents act on the external world through tools and third-party skills, so a single executed action can cause irreversible harm. Existing defenses judge a proposed action without tracking whether its content comes from the user or from external sources such as tool outputs, and they judge it in isolation rather than against an available alternative, which forces a trade-off between security and utility. We present PROVISO, a controller that decides which action to commit after the agent propo...
  </details>

- **2026-10-19** — Christian Kragh Jespersen — [Graph Neural Networks for Astrophysics and Cosmology](http://arxiv.org/abs/2610.27051v1)
  <details><summary>📄 Abstract</summary>
  Physics seldom makes breakthroughs when we consider objects only in isolation. Instead we model and measure how objects sit among their neighbours, spatial, temporal, or otherwise: a galaxy in its environment, a halo in its history, a photon hit in a detector. Graphs are ideally suited for encoding exactly these relations, and Graph Neural Networks (GNNs) learn the geometric functions that respect them. This review presents the use of GNNs for astrophysics and cosmology, and argues that GNNs oft...
  </details>

- **2026-10-19** — Allison Chen, William Yang, Salma Abdel Magid et al. — [Robustness of Internal Signals for Hallucination Detection in Vision-Language Models](http://arxiv.org/abs/2610.27041v1)
  <details><summary>📄 Abstract</summary>
  When given an image and a text prompt, vision-language models (VLMs) can produce seemingly sophisticated text responses. However, they are also prone to hallucinate objects in their output, which can have detrimental consequences in safety-critical applications. To detect these hallucinations, certain methods interestingly leverage internal signals from the VLM as it generates the text response; potentially, these methods use the same signals that led to a hallucination to detect it. We conduct ...
  </details>

- **2026-10-19** — Ruotian Peng, Yuanyi Ren, Shuaiqi Liu et al. — [VibeTraining-Bench: Data-Trainer-Harness Co-Design for Iterative System Improvement](http://arxiv.org/abs/2610.26342v2)
  <details><summary>📄 Abstract</summary>
  Recursive self-improvement (RSI) requires agents to diagnose system bottlenecks and coordinate improvements across training and inference. We refer to the agents' capability to jointly optimize training data, the trainer, and the inference harness as cross-component co-design. We introduce VibeTraining-Bench, a benchmark for evaluating this capability across tasks spanning terminal operation, software engineering, multi-turn tool use, and mathematical reasoning. Within each task, research agents...
  </details>

- **2026-10-19** — Sicong Huang, Ian Lane — [SHAM-Bench: A Span-level Hallucination Benchmark Across Multiple Tasks](http://arxiv.org/abs/2610.27370v1)
  <details><summary>📄 Abstract</summary>
  Span-level hallucination detection pinpoints unsupported content in LLM outputs, enabling actionable feedback and targeted mitigation. Existing evaluations for span-level hallucination detection methods are fragmented across tasks, annotation formats, and metrics, and most span-level datasets cover only a single NLG domain, making it difficult to assess whether a detection method actually generalizes across tasks and domains. In this paper, we introduce SHAM-Bench (Span-level Hallucination Bench...
  </details>

- **2026-10-19** — Nikita Gautam, Moana Sargent, Kaitlyn Sievers et al. — [Conversational AI for Perceived Cognitive Decline Screening in Older Adults](http://arxiv.org/abs/2610.27344v1)
  <details><summary>📄 Abstract</summary>
  Early detection of cognitive decline in older adults remains challenging due to the resource demands of standard neuropsychological assessments. Chatbot-based Intelligent Cognitive Assistants (ICAs) provide a scalable alternative by eliciting open-ended responses rich in linguistic, semantic, and autobiographical cues. This study evaluates whether ICA question-answer (Q/A) interviews with older adults can screen for participant-reported perceived cognitive decline and related cognitive, function...
  </details>


### 📂 alignment
*对齐与安全约束 / Alignment & Safety Constraints* — 58 papers

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

- **2026-10-20** — Chuyang Ye, Qinting Jiang, Jingyan Jiang — [SenseAlign: Understanding Vision and Touch through Language at Test Time](http://arxiv.org/abs/2610.28511v1)
  <details><summary>📄 Abstract</summary>
  Tactile-visual-language models combine vision and touch through a shared language space to recognize objects and materials. In real-world deployment, changes in lighting, contact quality or sensor hardware can shift visual or tactile inputs and degrade recognition performance. When both modalities contribute to a prediction, an unreliable modality can override correct evidence from the other. Since labeled data are generally unavailable during deployment, test-time adaptation offers a way to rec...
  </details>

- **2026-10-20** — Ning Zhang, Shihao Wang, Jinrui Zhang et al. — [BitMTP: When Multi-Token Prediction Meets Low-Bit Large Language Models](http://arxiv.org/abs/2610.28500v1)
  <details><summary>📄 Abstract</summary>
  For efficient deployment of large language models (LLMs), methods of ultra-low-bit backbones reduce weight storage, memory traffic, and linear-layer execution cost, while multi-token prediction (MTP) methods reduce sequential decoding steps by predicting multiple future tokens in parallel. Although complementary, the direct combination of these methods cannot accelerate decoding at comparable quality: masked drafting lacks intermediate token input supplied in next-token training, while wider com...
  </details>

- **2026-10-20** — Zhenwei Tang, Di Bai, Jintao Liu et al. — [Toolflation: Seller Agents Distort Tool Markets Through Spontaneous Generative Engine Optimization](http://arxiv.org/abs/2610.28454v1)
  <details><summary>📄 Abstract</summary>
  Agents are starting to sell to other agents. Seller agents write the listings of tools, services and products, and buyer agents read these listings when they choose what to use. We show that seller agents told only to be selected more often practice generative engine optimization on their own, and that this distorts the market for sellers and for buyers. We build tool markets from real data tools on Amazon and Instagram and run every tool on every question, so we know which tools can answer each...
  </details>

- **2026-10-20** — Zhenghan Chen, Zekai Shao, Xin Lin et al. — [Code2Video-Compass: A Comprehensive Benchmark for General-Purpose Code-Based Video Generation across T2V, I2V, and V2V](http://arxiv.org/abs/2610.28416v1)
  <details><summary>📄 Abstract</summary>
  Code-based video generation offers fine-grained control, targeted editing, and component reuse compared with direct video generation. This approach requires multimodal large language models (MLLMs) to translate visual and temporal requirements into executable programs that produce complete videos. However, existing code-based benchmarks primarily target specialized tasks, leaving complete video creation across diverse creative categories and input modalities insufficiently evaluated. We introduc...
  </details>

- **2026-10-20** — Yuxia Chen, Wenbo Zhu, Yangguang Ji et al. — [Auto-Director: Leveraging Multi-Agent Collaboration for Autonomous Video Editing](http://arxiv.org/abs/2610.28346v1)
  <details><summary>📄 Abstract</summary>
  Autonomous video editing from open-world resources remains a challenging problem in multimedia content creation. Retrieval-based methods are constrained by fixed source material and lack creative flexibility, while generative models struggle with long-horizon coherence and often diverge from user intent. Both paradigms fail to replicate the structured, multi-stage reasoning that underlies professional post-production. To address these limitations, we present Auto-Director, a tool-augmented multi...
  </details>

- **2026-10-20** — Arthur Ouaknine, David Rolnick — [Towards Consistent Geospatial Representations: Aligning One Encoder to Many Foundation Models](http://arxiv.org/abs/2610.28313v1)
  <details><summary>📄 Abstract</summary>
  Geospatial foundation models (GFMs) differ widely in pretraining objective, modality and resolution, and none leads across benchmarks. We ask whether their representations are complementary, and whether a single encoder can inherit that complementarity. We introduce Pangaea-Latents, an extension of the Pangaea benchmark providing frozen embeddings of $5$ GFMs over its $11$ datasets, along with reproduced baselines, and find GFM embeddings to be neither redundant nor disjoint. We then propose Geo...
  </details>

- **2026-10-20** — Yuheng Zhang, Jie Zhang, Yuecong Min et al. — [PI-MLLM: Psychophysics-Inspired Multimodal Large Language Model for Oddly Satisfying Video Emotion Analysis](http://arxiv.org/abs/2610.28264v1)
  <details><summary>📄 Abstract</summary>
  Oddly Satisfying Videos (OSVs) can evoke strong viewer responses through repetitive motion, visual tactility, and ASMR-like sounds despite containing few explicit semantic emotion cues. This makes OSVs a challenging setting for Video Emotion Analysis (VEA), since most existing methods focus on semantic video content and under-model the physical sensory dynamics that shape viewer responses. To support Oddly Satisfying Video Emotion Analysis (OSVEA), we construct the Oddly Satisfying Video Dataset...
  </details>

- **2026-10-20** — Tzu-Quan Lin, Chih-Kai Yang, Yi-Cheng Lin et al. — [Uncovering Audio-Text Alignment in Large Audio-Language Models through Cross-Modal Concept Neurons](http://arxiv.org/abs/2610.28189v1)
  <details><summary>📄 Abstract</summary>
  While the language model backbone is pretrained on text alone, large audio-language models (LALMs) can, to a great extent, recognize acoustic attributes, such as emotion, speaker gender, and spoken language. However, it is unclear how the audio representation is integrated, if at all, with the other text representation before the model produces text. We hypothesize that there is a shared subspace where the audio and text representations are aligned. To test this hypothesis, we identify cross-mod...
  </details>

- **2026-10-20** — Huynh Dang Nguyen, Trong-Thang Pham, Anh-Thuan Do et al. — [IECG: Weakly-Supervised Interpretability-Enhancing Foundation Model for Electrocardiogram](http://arxiv.org/abs/2610.28083v1)
  <details><summary>📄 Abstract</summary>
  Electrocardiography (ECG) is a cornerstone of cardiac diagnosis, yet most machine learning methods for ECG analysis lack interpretability, limiting their clinical adoption. We present IECG, a weakly-supervised ECG foundation model that jointly performs diagnostic classification and abnormality localization without requiring manual abnormal region annotations, overcoming a long-standing bottleneck in interpretable ECG learning. Central to IECG is a weakly-supervised attention strategy that explic...
  </details>

- **2026-10-20** — Ben Vardi, Dana Schonberger, Yuval Friedmann et al. — [AdaptMIL: Domain Adaptation for Multiple Instance Learning in Digital Pathology](http://arxiv.org/abs/2610.28007v1)
  <details><summary>📄 Abstract</summary>
  Pathology foundation models (PFMs) support a wide range of histopathology tasks on whole-slide images through multiple instance learning (MIL). Despite recent progress, these models remain sensitive to cross-hospital distribution shifts: performance often degrades when a task head (e.g., classification) is trained on data from one hospital and then used on data from another hospital. To address this challenge, we propose AdaptMIL, a training strategy for integrating domain adaptation into MIL tr...
  </details>

- **2026-10-20** — Darío Blanco-Fernández — [Understanding CEO-Employee compensation dynamics: An agent-based simulation approach](http://arxiv.org/abs/2610.27975v1)
  <details><summary>📄 Abstract</summary>
  CEO compensation has often been examined from the top down, i.e., as the outcome of a negotiation between the CEO, the board of directors, and the shareholders. While these approaches have provided valuable insights into the nature of CEO compensation and its relations with firm performance and intra-firm inequality, we believe they leave aside the internal decision-making dynamics of CEOs and employees. To fill this research gap, we develop an agent-based model built on the NK framework in whic...
  </details>

- **2026-10-20** — Genshin Kakimoto, Atsushi Yanagisawa — [Staged Continual Adaptation of Multimodal Foundation Models for Japanese Financial Documents](http://arxiv.org/abs/2610.27904v1)
  <details><summary>📄 Abstract</summary>
  Staged post-training of multimodal foundation models chains vision-language alignment, reasoning distillation, and domain tuning, yet how each phase trades capabilities against the others remains under-characterised. Tracking an 8.4B-parameter model from an un-fine-tuned baseline through three training phases on Japanese financial documents (evaluated on five text-input benchmarks), we find the phases interact non-additively: math-only distillation overwrites the financial knowledge acquired ear...
  </details>

- **2026-10-20** — Sasi Kiran Gaddipati, Gollam Rabby, Sören Auer — [CollabSciReM: Aligning Language Models for Scientific Conversations via Science-Aware Reward Decomposition](http://arxiv.org/abs/2610.27901v1)
  <details><summary>📄 Abstract</summary>
  Large Language Models (LLMs) are increasingly used as research collaborators for hypothesis refinement, methodological planning, and technical analysis across multi-turn interactions. In this setting, a useful assistant must be accurate, methodologically justified, logically consistent, and token-efficient. Current alignment approaches rarely achieve all of these together. Instruction-tuned models gain conversational quality through verbosity, and we show that science-agnostic general collaborat...
  </details>

- **2026-10-20** — Hao Wang, Zixuan Li, Long Bai et al. — [SciDiagBench: A Type-Specific Benchmark for Human-Aligned Evaluation of Scientific Diagrams](http://arxiv.org/abs/2610.27841v1)
  <details><summary>📄 Abstract</summary>
  Recent agents have demonstrated strong capabilities in generating images from textual prompts, motivating their utilization for scientific diagram generation. Scientific diagrams naturally span diverse types, each characterized by distinct visual structures and content organization. Consequently, during peer review and other scientific evaluation, human experts naturally consider type-specific criteria when assessing their quality. However, existing VLM-based evaluation benchmarks fail to reflec...
  </details>

- **2026-10-20** — Siyuan Ma, Yu Qi, Cheng Ye et al. — [RoboJudge: Multimodal Language Models as Judges for Embodied Video Generation](http://arxiv.org/abs/2610.27782v1)
  <details><summary>📄 Abstract</summary>
  Video generation models are promising foundations for embodied world models, but only if their generated rollouts are physically valid and faithful to task instructions. Multimodal large language models (MLLMs) are increasingly used to judge these properties, yet their agreement with human judgments on embodied videos has not been systematically evaluated. To address this gap, we introduce RoboJudge-Bench, a benchmark for evaluating MLLMs as judges of embodied video generation. The benchmark mea...
  </details>

- **2026-10-20** — Sahil Kale — [Beyond Calibration: Temporal LLM Confidence Assessment Across Languages and Local Settings](http://arxiv.org/abs/2610.27702v1)
  <details><summary>📄 Abstract</summary>
  Large language models are expected to estimate their own uncertainty, with confidence signals used to guide retrieval, adaptive compute allocation, routing, and selective abstention. We investigate whether confidence signals measured at different temporal stages of problem solving encode distinct forms of epistemic information and remain reliable beyond English-centric settings. Inspired by classical meta-memory theory, we distinguish anticipatory pre-solve confidence (Feeling-of-Knowing, FOK) f...
  </details>

- **2026-10-20** — Bohao Li, Dinglun Cao, Pengcheng Huang et al. — [EASformer: Environment-Action-State Alignment for Industrial Generative Ranking](http://arxiv.org/abs/2610.27691v1)
  <details><summary>📄 Abstract</summary>
  Modern industrial ranking systems increasingly adopt generative recommendation (GR) paradigms, in which user behavior sequences and non-sequential (NS) features are tokenized and jointly modeled by Transformer-style backbones. This unified formulation provides a scalable interface for modeling long histories and heterogeneous features. However, sequence and NS representations often carry asymmetric semantics: historical representations may combine environment context with observed-action semanti...
  </details>

- **2026-10-20** — Yang Liu, Masahiro Kaneko, Chenhui Chu — [Speak vs. Know: Balancing Behavior and Knowledge Distributions of Large Language Models](http://arxiv.org/abs/2610.27648v1)
  <details><summary>📄 Abstract</summary>
  Recent work reports that the distribution verbalized directly in the output text aligns far better with human opinion distributions than the next-token log-probability distribution of LLMs. However, the verbalized distribution reflects what LLMs know about a group's opinions (knowledge distribution), while what they actually output at deployment is governed by their log-probability distribution (behavior distribution). We find that when prompting LLMs to predict the opinion of a specific group, ...
  </details>

- **2026-10-20** — Tingxu Han, Wei Song, Ziming Li et al. — [Standards-Guided and Dependency-Aware Code-Level Documentation Generation](http://arxiv.org/abs/2610.27634v1)
  <details><summary>📄 Abstract</summary>
  Automatically generating high-quality documentation for software repositories remains challenging: existing approaches largely treat documentation as unconstrained text generation, lacking explicit quality specifications, depending heavily on long-context prompts over raw code, and offering limited support for reproducible evaluation. We argue that code-level documentation generation should instead be a standards-guided software engineering task, in which documentation is generated and assessed ...
  </details>

- **2026-10-20** — Junjie Xu, Yuzhe Yang, Rui Yang et al. — [HealBench: A Fine-Grained Benchmark for Evaluating Psychological Comfort in Text-to-Image Generation](http://arxiv.org/abs/2610.27516v1)
  <details><summary>📄 Abstract</summary>
  Despite advances in photorealism, semantic fidelity, and aesthetics, text-to-image generation and image editing remain understudied in a human-centered dimension: whether their outputs feel psychologically comforting. Grounded in cognitive evaluation theory, we define psychological comfort as an affective response shaped by viewers' appraisal of restorative and emotionally supportive visual cues. We introduce HealBench, a fine-grained benchmark of 30,000 high-quality image-text pairs spanning 19...
  </details>

- **2026-10-20** — Kohei Yamamoto, Kosuke Okusa — [MiCLA: Mixture-to-Constituent Latent Alignment for Polyphonic Audio Representation Learning](http://arxiv.org/abs/2610.27491v1)
  <details><summary>📄 Abstract</summary>
  Real-world audio typically contains concurrent sound events, yet standard self-supervised methods treat each clip as an isolated training unit without explicitly modeling mixture--constituent relationships. We propose Mixture-to-Constituent Latent Alignment (MiCLA), a two-stage self-supervised pre-training framework that uses synthetic log-mel mixing to align mixture representations with their constituent clips. Stage 1 structures single-clip representations via masked self-distillation and cont...
  </details>

- **2026-10-20** — Zhengfeng Zheng, Minghong Fang — [Beyond the Prompt: Recovering Hidden Concepts in Text-to-Image Models](http://arxiv.org/abs/2610.27473v1)
  <details><summary>📄 Abstract</summary>
  Text-to-image models can generate visual concepts that their prompts never mention, and recent work shows that such associations can be implanted so that ordinary prompts trigger them. Auditing this behavior requires recovering the description that a prompt omits. Existing prompt optimizers are not well suited to this task. Gradient-based methods require backward access to the scoring encoder. Discrete evolutionary search treats semantically unrelated tokens as equally close. Language-model-guid...
  </details>

- **2026-10-19** — Afonso Baldo, António Farinhas, Marcos Treviso et al. — [Mitigating Reward Hacking in Preference Reward Models with Evolving Penalties](http://arxiv.org/abs/2610.26496v2)
  <details><summary>📄 Abstract</summary>
  Reinforcement learning for language models has moved from preference reward models to verifiable rewards, which sustain much longer optimization. Preference models are prone to reward hacking: the policy raises their score without improving response quality, or even while degrading it. Yet for open-ended tasks, where quality can neither be verified nor fully written down as rubrics, they remain valuable. We introduce Dynalize, which mitigates reward hacking online, during policy training. Period...
  </details>

- **2026-10-19** — Abolfazl Babanazari, Kaveh Fathian — [On Maximum Clique and Maximum Consensus Formulations in Point Cloud Registration](http://arxiv.org/abs/2610.27275v1)
  <details><summary>📄 Abstract</summary>
  Maximum clique and maximum consensus are widely used formulations for robust point cloud registration in robotics. Maximum consensus seeks one transformation that aligns as many matches as possible, while maximum clique selects matches through pairwise distance tests. Maximum clique is often used as a substitute for or an approximation to maximum consensus, with empirical evidence suggesting a close relationship. However, how closely the two formulations agree is not fully understood. We study t...
  </details>

- **2026-10-19** — Shuaiqi Cheng, Jiahao Zhang, Boyuan Gu et al. — [TamedFlow: Trajectory-Aware Distillation for Teacher-Assisted Diffusion Sampling](http://arxiv.org/abs/2610.26025v2)
  <details><summary>📄 Abstract</summary>
  Diffusion Transformers (DiTs) deliver high-fidelity image and video generation, but inference requires many sequential model evaluations. Two acceleration strategies are increasingly important: model compression makes each evaluation cheaper, while adaptive inference avoids selected teacher computation through reuse, forecasting, or speculative execution. Their combination, however, is brittle: directly applying the evaluated adaptive methods to a compressed student can degrade quality, an obser...
  </details>

- **2026-10-19** — Lanfeng Zhong, Xiangyu Sun, Guixuan Xu et al. — [REST: Reliability-Guided Spatial Transcriptomics Supervision for Gene Expression Prediction from Histopathological HE-Stained Images](http://arxiv.org/abs/2610.26988v1)
  <details><summary>📄 Abstract</summary>
  Histopathology is central to cancer diagnosis, but morphology in Hematoxylin and Eosin (HE)-stained images does not directly reveal the molecular states that characterize disease heterogeneity and inform tumor characterization, prognostic assessment, and biomarker discovery. Spatial Transcriptomics (ST) measures spatially resolved gene expression, providing molecular information within tissue architecture, yet differences in assay coverage and spot informativeness make paired HE--ST observations...
  </details>

- **2026-10-19** — Zhengyue Zhao, Liwei Jiang, Yejin Choi et al. — [Safety Mid-Training: Internalizing LLM Safety as a Foundational Capability](http://arxiv.org/abs/2610.26809v1)
  <details><summary>📄 Abstract</summary>
  Safety alignment for large language models (LLMs) is primarily performed during post-training, while recent work has also begun incorporating safety data into pre-training. Yet safety can degrade when later training no longer includes safety data, and gains in safety often come at the cost of general capability. This tension suggests that safety and general reasoning should not be treated as separate training goals. We instead view safety as an LLM capability that can be learned through a reason...
  </details>


### 📂 robustness
*鲁棒性与可靠性 / Robustness & Reliability* — 69 papers

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

- **2026-10-20** — Youmna Farag, Svetlana Stoyanchev, Simon Keizer et al. — [CAPSafe: A Benchmark for Contextual Action and Plan Safety Reasoning in Embodied Agents](http://arxiv.org/abs/2610.28381v1)
  <details><summary>📄 Abstract</summary>
  Reasoning about safety is essential for embodied agents powered by large language models (LLMs). We introduce the Contextual Action and Plan Safety benchmark (CAPSafe), designed to evaluate safety reasoning at two levels: (1) an action-level dataset that tests whether a single action is safe given its environmental context, and (2) a plan-level dataset that evaluates whether agents can generate safe long-horizon plans for complex hazardous household tasks. CAPSafe models safety conditions where ...
  </details>

- **2026-10-20** — Borui Xu, Han Chen, Bingsheng He et al. — [VLA-Retain: Benchmarking Cross-Dimension Effects of Vision Tuning in VLAs](http://arxiv.org/abs/2610.27698v1)
  <details><summary>📄 Abstract</summary>
  Vision-language-action (VLA) models transfer knowledge from large-scale pretraining into robot control, but their manipulation performance remains sensitive to changes in observation conditions, which recent work addresses by fine-tuning the visual module on target-domain data. However, it remains unclear how such adaptation affects robustness beyond the target condition, as existing robustness benchmarks only evaluate models without fine-tuning and adaptation studies only report the target gain...
  </details>

- **2026-10-20** — Jiatong Li, Jisheng Dang, Qiangqiang Ma et al. — [FIT-MAC: A Closed-Loop Multi-Agent Framework for Robust Vision-Language-Action Models](http://arxiv.org/abs/2610.28109v1)
  <details><summary>📄 Abstract</summary>
  Vision-language-action (VLA) models have achieved strong performance on standard robotic manipulation benchmarks. However, their reliability can degrade substantially when task conditions deviate from the nominal setting. Perturbations in object positions and task instructions may lead to complete task failure. Existing VLA policies generally lack an explicit runtime mechanism for distinguishing these failure modes and selecting an appropriate recovery strategy. To systematically mitigate this i...
  </details>

- **2026-10-20** — Da Huang, Jichao Wang, Junhui Wu et al. — [Frontier LLMs Enter the World of Robotics: A Cross-Model Evaluation on RoboColiseum](http://arxiv.org/abs/2610.27865v1)
  <details><summary>📄 Abstract</summary>
  Recent studies have explored the potential of multimodal large language models for robot control, yet the models' embodied capabilities remain insufficiently characterized across models, tasks, and execution settings. We conduct a multidimensional comparative evaluation on RoboColiseum across four tracks: Instruction Following, Spatial Reasoning, General Manipulation, and Robustness. We implement Agent2Act, a control harness that integrates GPT-6 Astra, GPT-6.1 Sol, Claude Opus 5.5, and Gemini 4...
  </details>

- **2026-10-20** — Ma ZhenYao, Yue Liang, Jian-Qiao Zhu — [OptScientist: Automated Discovery of Optimization Laws](http://arxiv.org/abs/2610.28562v1)
  <details><summary>📄 Abstract</summary>
  Many scientific phenomena are best understood as outcomes of underlying optimization problems, yet automated scientific discovery has largely focused on recovering equations that describe observed input-output patterns. We introduce OptScientist, a novel automated framework for discovering compact symbolic optimization laws directly from data. OptScientist comprises (i) a model that infers symbolic optimization problems by first learning to represent data as an optimization problem and then extr...
  </details>

- **2026-10-20** — Mohammad Reza Modarres, Armin Tourajmehr, Artin Tavasoli et al. — [Every Model Leaves a Trace: Multi-Resolution LLM Fingerprinting](http://arxiv.org/abs/2610.28434v1)
  <details><summary>📄 Abstract</summary>
  Large language models leave model-specific traces in their generated text, but it remains unclear how finely these fingerprints can distinguish related models and which signals remain informative as obvious cues are reduced. We study this through fingerprint resolution, considering both model resolution, from different families to distilled and adapted variants, and signal resolution across behavioral, stylometric, lexical, and semantic evidence. We progressively suppress surface cues, paraphras...
  </details>

- **2026-10-20** — Yunxin Geng, Shengxiang Hao, Yichen Wu et al. — [ORCA: Onboard Reflective Collaborative Agents for Reliable Task Offloading in LEO Satellite Networks](http://arxiv.org/abs/2610.28404v1)
  <details><summary>📄 Abstract</summary>
  Low Earth orbit (LEO) satellites increasingly perform time-critical onboard processing, yet heterogeneous computing capabilities, rapidly changing inter-satellite links (ISLs) and uncertain neighbor behavior make decentralized task offloading difficult under partial observations. This paper presents ORCA, an architecture of Onboard Reflective Collaborative Agents for autonomous onboard task offloading. ORCA organizes offloading decisions into a four-Agent \emph{Perceive}$\rightarrow$\emph{Reason...
  </details>

- **2026-10-20** — Cecilia Diana-Albelda, Fiona Kekwick, Raghav Mehta et al. — [Convergent Performance, Divergent Mechanisms in LoRA-Adapted Vision Foundation Models for Brain MRI](http://arxiv.org/abs/2610.28255v1)
  <details><summary>📄 Abstract</summary>
  Adapting Vision Foundation Models (VFMs) to medical imaging via LoRA has become standard practice, yet model selection is guided almost entirely by downstream task metrics, treating backbones with similar performance as interchangeable. We investigate whether equal performance implies equal internal representational shift. We analyse four ViT-B/16 backbones, DINOv3, SigLIP2, MerMED-FM, and BiomedCLIP, pre-trained with different objectives (self-distillation vs. contrastive vision-language) and o...
  </details>

- **2026-10-20** — Edric Castel C. Hao, Rez Samantha Z. Floresca — [Beyond the Evidence Boundary: Behavioral Mirage Under Progressive Degradation in Medical VLMs](http://arxiv.org/abs/2610.28000v1)
  <details><summary>📄 Abstract</summary>
  VLMs for medical image interpretation are typically evaluated on clean inputs, despite the progressive evidence loss that can occur in high stakes clinical settings. Existing robustness studies show that performance can degrade while confidence remains high, but do not establish when a previously reliable model-case pair ceases to behave reliably. We introduce a baseline-anchored framework that traces baseline-correct cases through progressive image degradation to identify an empirical evidence ...
  </details>

- **2026-10-20** — Esther Shizgal, Ron Keinan, Daniel Shtauber et al. — [From DQI to C-DQI: Automatic Codebook Generation and Evaluation for Measuring Computational Discourse Quality Index](http://arxiv.org/abs/2610.27937v1)
  <details><summary>📄 Abstract</summary>
  Effective democratic deliberation is vital for civic engagement and the health of legislative institutions. However, assessing parliamentary discourse quality is traditionally done using expert-scored, theory-based codebooks (CBs), which are rigid, labor-intensive, and prone to biases. While Large Language Models (LLMs) offer a scalable alternative for both schema induction and discourse annotation, ensuring schema quality and mitigating models' inherent bias remains a clear challenge. In this w...
  </details>

- **2026-10-20** — Junha Song, Geonmo Gu, Jeongeun Park et al. — [LaLa-World: Scaling Latent World Models with Natural Language Actions](http://arxiv.org/abs/2610.27851v1)
  <details><summary>📄 Abstract</summary>
  This paper shows that JEPA-style latent world models (LWMs) can learn across diverse domains and data sources by adopting the language-conditioned interface of video generation models. We establish this approach as an effective and efficient basis for planning with imagination and downstream policy fine-tuning. To this end, we introduce LaLa-World, a Language-conditioned Latent World model that learns from simulation and robot trajectories together with broader image and video data. Two designs ...
  </details>

- **2026-10-20** — Daisuke Oba, Hiroki Furuta, Naoaki Okazaki — [BCT: Bayes-Consistent Tempering for Flow Language Models](http://arxiv.org/abs/2610.27641v1)
  <details><summary>📄 Abstract</summary>
  Temperature scaling is typically applied as a post-hoc transformation of model probabilities. In posterior-induced flow language models, this creates two mismatches. First, posterior tempering implicitly changes both the endpoint distribution and the distribution of intermediate noisy states, while the denoiser remains trained on the original states. Second, the tempered posterior weights are combined with transport dynamics derived for the untempered flow. These mismatches are reflected empiric...
  </details>

- **2026-10-20** — Zihan Chen, Di Zhu, Lei Nico Zheng — [Auditing the Product, Not the Recursion: The Evaluation Evidence Behind Recursive Self-Improvement Claims](http://arxiv.org/abs/2610.27610v1)
  <details><summary>📄 Abstract</summary>
  Recursive self-improvement (RSI) promises AI systems, such as self-evolving LLM agents, that become better at producing further improvements. Evaluating this promise requires separating product claims about the final system from process claims about the improvement process itself. Existing surveys specify the evidence these claims require, but how often studies report that evidence remains unmeasured. We examine this question through full-text coding of 114 eligible studies in a reproducible arX...
  </details>

- **2026-10-20** — Yuchen Guo, Zhuoyuan Mao, Yiwen Guo — [Factual Access States in Diffusion Language Models: From Mechanism to Knowledge Editing and Retrieval](http://arxiv.org/abs/2610.27580v1)
  <details><summary>📄 Abstract</summary>
  Factual recall is a lookup: some representation inside the network serves as the key, and what that key is made of decides which queries can retrieve the fact, what an edit must cover, and what a retriever can read. We call it the factual access state. In autoregressive (AR) models the subject position enriches attributes largely independently of the relation, and relation-specific selection happens later, at the readout position. In masked diffusion language models (DLMs) we find the state is a...
  </details>

- **2026-10-20** — Yuqian Zheng, Hyoju Ahn, Hyeongjin Ahn et al. — [Less is More: Concise Retrieval and Critic-based Re-ranking for Composed Image Retrieval](http://arxiv.org/abs/2610.27538v1)
  <details><summary>📄 Abstract</summary>
  Zero-shot composed image retrieval (ZS-CIR) aims to retrieve a target image based on a reference image and modification text. Recent approaches commonly rely on large vision-language models to generate target image captions for retrieval. However, these captions may include redundant semantic details, introducing noise when retrieving the target image and leading to suboptimal retrieval results. To address this issue, we propose Less-is-More CIR, a two-stage training-free framework that combines...
  </details>

- **2026-10-20** — Daniel Weiner, Raj Korpan — [Robot-Task Suitability in Heterogeneous Multi-Robot Task Allocation](http://arxiv.org/abs/2610.27504v1)
  <details><summary>📄 Abstract</summary>
  Heterogeneous multi-robot task allocation depends on estimates of how suitable individual robots are for candidate tasks, yet suitability can be defined in substantially different ways. We compare ten deterministic methods and two LLM-based variants spanning rule-based, similarity-based, requirement-oriented, fuzzy, and semantic approaches. Using common robot and task profiles, we compare how the methods score and rank candidate robots, identify feasibility, and select a top robot, while examini...
  </details>

- **2026-10-20** — Samaneh Zamanifard, Sajad Goudarzi, Andrew Robb — [Bias and Reliability in Learning-Style Inference from Student--AI Dialogues: An Evaluation of GPT-4o and Gemini 2.0 Flash](http://arxiv.org/abs/2610.27448v1)
  <details><summary>📄 Abstract</summary>
  Large Language Models (LLMs) are increasingly integrated into educational technologies for personalized support, creating opportunities for real-time learner modeling from dialogue. This study evaluates whether GPT-4o and Gemini 2.0 Flash can infer three Felder-Silverman Learning Style Model dimensions (Active-Reflective, Sensing-Intuitive, and Sequential-Global) from short, task-focused student-AI problem-solving dialogues. Using questionnaire-derived Index of Learning Styles labels from 153 un...
  </details>

- **2026-10-20** — Javier Porras-Valenzuela, Arush Arora, Alejandro Ribeiro — [Scaling Graph Reasoning in Language Models with Learnable Graph Positional Encodings](http://arxiv.org/abs/2610.27439v1)
  <details><summary>📄 Abstract</summary>
  Solving reasoning tasks supported on graphs typically requires providing a Language Reasoning Model (LRM) with a serialized description of the graph. This approach results in the input length growing with the number of edges, which limits the size of the problems that can be solved. Furthermore, even when graphs fit in context, performance sharply decays as the graphs grow. We propose to address this by augmenting LRMs with scalable and permutation equivariant graph positional encodings that mod...
  </details>

- **2026-10-19** — Chao Yu, Shu'ang Yu, Hao Lin et al. — [Learning from Fleet Experience: Collective Experience Learning Across 96 Robots](http://arxiv.org/abs/2610.25736v2)
  <details><summary>📄 Abstract</summary>
  Robot deployment generates experience that can support policy improvement, but continued reliance on expert corrective actions makes learning difficult to scale across growing fleets. We propose learning from fleet experience: using deployed robots' own executions as a source of supervision for further policy improvement. We call this paradigm Collective Experience Learning (CEL), in which robots pool execution experience to update a shared policy that returns to the fleet. Following expert-supe...
  </details>

- **2026-10-19** — P. K. G. Williams — [AI and The Enclosure of the Scientific Commons](http://arxiv.org/abs/2610.27251v1)
  <details><summary>📄 Abstract</summary>
  The scientific literature can be viewed as an "information commons:" an intangible resource that "no one owns and is shared by everyone." There are well-established economic and political frameworks for understanding such commons, emerging from the history of agricultural common lands found in places like preindustrial England. This article provides a primer on the history and these frameworks, and considers a key difference between the information commons and the fields of yore: while informati...
  </details>

- **2026-10-19** — Xinying Cai, Bin Hu, Mingyu Jin et al. — [RealControlBench: A Benchmark for Interpretability-Informed Fine-Grained Control of LLMs and Agents](http://arxiv.org/abs/2610.27295v1)
  <details><summary>📄 Abstract</summary>
  Existing steering benchmarks are built around simplified, isolated generation tasks and evaluate a single behavioral attribute under controlled settings that do not reflect the diversity and complexity of practical deployment. As a result, performance on these benchmarks provides only a limited picture of how steering methods perform in the real world. We therefore introduce RealControlBench, a comprehensive benchmark for evaluating fine-grained steering of LLMs and LLM agents across diverse beh...
  </details>

- **2026-10-19** — Weinan Zhang, Chunhua Shen, Tianfan Xue et al. — [Physical AI: Concepts, Techniques, and Challenges](http://arxiv.org/abs/2610.27045v1)
  <details><summary>📄 Abstract</summary>
  In recent years, physical artificial intelligence (physical AI) has experienced rapid development, capturing significant attention in academia and industry. However, the field has yet to reach consensus on its definition, technical landscape, and core challenges. To address this gap, this monograph seeks to define physical AI, present its technical landscape, and examine each key technical subfield in depth. In doing so, it establishes a unified framework for Physical AI: artificial systems that...
  </details>

- **2026-10-19** — Ocean Monjur, Daud Ahmad Nisar, Shahriar Kabir Nahin et al. — [LoWAgent: A Low-Resource Multilingual Benchmark for Web Agents](http://arxiv.org/abs/2610.27205v1)
  <details><summary>📄 Abstract</summary>
  Web agents are typically evaluated on English-language interfaces, leaving their ability to operate across the world's multilingual websites largely unexplored. This gap is especially significant for low-resource languages, where standardized resources for evaluating web agents remain limited. To address this gap, we introduce Low-Resource Web Agent Benchmark (LoWAgent), a benchmark for evaluating web agents across different low-resource languages (LRLs) in comparison to the default, English. Lo...
  </details>

- **2026-10-19** — Dan Porat, Ran Finkelstein, Tal Carmon — [Allight: A Perfect Photon Collector](http://arxiv.org/abs/2610.27161v1)
  <details><summary>📄 Abstract</summary>
  Collecting photons from quantum emitters remains a key limitation in light-matter interaction because conventional lenses collect light only from one direction. Here, we introduce a perfect light collector by inverse-designing a surrounding dielectric structure that encloses the emitter to increase photon-collection efficiency toward unity. Decomposing the device into several refractive interfaces enables emission collection from the full 4$π$ solid angle with adiabatic reshaping into a collimat...
  </details>

- **2026-10-19** — Shafi Bin Sultan, Sabik Bin Sultan, Mohammad Tajrian Arafat Alvi et al. — [A Hybrid TFT-NBEATS Framework for Robust Multi-Horizon Photovoltaic Power Forecasting](http://arxiv.org/abs/2610.27155v1)
  <details><summary>📄 Abstract</summary>
  Accurate multi-horizon photovoltaic (PV) power forecasting is essential for grid stability, energy scheduling, and the efficient operation of PVbatterygrid systems. However, existing models often fail to jointly capture short-term variability and long-term temporal patterns, while lacking unified multi-horizon capability and interpretability. To address these limitations, this study proposes a novel hybrid deep learning framework that integrates a Temporal Fusion Transformer (TFT) and N-BEATS wi...
  </details>

- **2026-10-19** — Yupeng Qiu, Han Fang, Ee-Chien Chang — [ClockMark: Adaptive and Host-Dependent Watermarking for Large Language Models](http://arxiv.org/abs/2610.27079v1)
  <details><summary>📄 Abstract</summary>
  Large language model (LLM) watermarking operates on the next-token distribution that evolves during generation. In streaming generation, each sampled token becomes part of the text and affects subsequent distributions. Embedding therefore proceeds with a changing host, unlike classical watermarking, which adapts embedding to an existing host signal. To accommodate this difference, we formulate a novel embedding framework for LLM watermarking based on two principles. We first argue that embedding...
  </details>

- **2026-10-19** — Tong Ding, Caiwei Tian, Dongmin Bang et al. — [Discrete Neural Interlingua for Ontology-Agnostic EHR Modeling](http://arxiv.org/abs/2610.27047v1)
  <details><summary>📄 Abstract</summary>
  EHR foundation models promise scalable clinical prediction across health systems, yet their deployment is constrained by a tokenization bottleneck. The same clinical concept can appear as different ontology codes, local identifiers, synonyms, or free-text descriptions, which standard EHR tokenizers treat as unrelated symbols. A model trained on MIMIC-III with a closed-vocabulary tokenizer can use only 13% of eICU events. We introduce MEDIATOR, a discrete ontology-agnostic tokenizer that maps any...
  </details>

- **2026-10-19** — Mobina Koochaknia, Maryam Ramezani, Mohammad Hasan Shafaat — [MultiCard: Multiple Attribute Cardinality Estimation via Deep Learning](http://arxiv.org/abs/2610.27019v1)
  <details><summary>📄 Abstract</summary>
  Cardinality estimation is essential for query optimization, but most existing learned estimators focus on a single predicate type, such as string LIKE clauses or numerical range filters. In practice, analytical workloads often combine both types, while the accuracy of string estimators tends to decrease with longer patterns. We introduce MultiCard, a comprehensive learned cardinality estimator that unifies LIKE predicates and numerical filters within a single end-to-end architecture. By combinin...
  </details>

- **2026-10-19** — Chuansen Peng, Xiaojing Shen — [Robust Latent Variable Graphical Models: Exact Recovery and Fundamental Limits](http://arxiv.org/abs/2610.27010v1)
  <details><summary>📄 Abstract</summary>
  We study robust estimation of a Gaussian precision matrix that decomposes as a sparse matrix minus a symmetric, possibly indefinite, low-rank matrix, a structure that arises when latent-variable marginalization is combined with conditioning on linear measurements. The proposed convex estimator replaces the sample covariance by the centered Gaussian measure-transformed (MT) covariance, which preserves the signed graph of the sparse component under the nominal model, and penalizes the low-rank com...
  </details>

- **2026-10-19** — Matthias Eder, Pantelis Emmanouil, Vivek Farias et al. — [Policy Search in Code Space for Multi-Agent Pathfinding](http://arxiv.org/abs/2610.25946v2)
  <details><summary>📄 Abstract</summary>
  Developing coordination policies for complex multi-agent systems relies on either labor-intensive algorithm design or opaque task-specific reinforcement learning. With recent advances in autonomous coding agents, we show that policy search directly in code space offers a compelling third path that combines automated optimization with explicit interpretability. We investigate a human-directed workflow in which coding agents iteratively propose, implement, evaluate, diagnose, and eventually refine...
  </details>

- **2026-10-19** — Yudong Pan, Lian Liu, Shixin Zhao et al. — [3D-MoE: Complementarity-Guided Hardware-Software Co-Design for MoE Decode on 3D-Stacked NMP](http://arxiv.org/abs/2610.26991v1)
  <details><summary>📄 Abstract</summary>
  Mixture-of-Experts (MoE) have become a mainstream way to scale Large Language Models (LLMs), because each token activates only a small subset of experts, reducing inference cost. However, MoE decode remains highly memory-bound and exhibits strongly skewed, time-varying expert loads. 3D-stacked DRAM near-memory processing (NMP) provides the bandwidth that decode demands, yet its tiled organization makes load balancing expensive: expert parallelism (EP) preserves locality but suffers from hotspot-...
  </details>


### 📂 watermark
*水印与溯源 / Watermarking & Provenance* — 12 papers

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

- **2026-10-20** — Seyedeh Fatemeh Mirfakhar, Reda Snaiki, Rocio Lilen Segura — [A Multimodal Engineering GraphRAG Framework for Post-Wind-Event Building Assessment and Recovery Inference](http://arxiv.org/abs/2610.28216v1)
  <details><summary>📄 Abstract</summary>
  Post-event building assessment requires linking observed physical damage to its consequences for safety, habitability, functionality, and recovery. Yet post-disaster evidence is often heterogeneous, incomplete, and distributed across images and reconnaissance reports, while recovery models typically require structured engineering inputs. This study develops a multimodal engineering Graph Retrieval-Augmented Generation (GraphRAG) framework that connects post-wind-event damage evidence to physical...
  </details>

- **2026-10-20** — Oleksiy V. Penkov, Boyang Shen — [Value-level data provenance in an electronic laboratory notebook used by humans and language-model agents: An experience report](http://arxiv.org/abs/2610.27859v1)
  <details><summary>📄 Abstract</summary>
  A published laboratory number can be verified only when its raw file and extraction method are known. This paper presents the value-level provenance architecture of APS ELN, an electronic laboratory notebook used by both researchers and language-model agents. The architecture was motivated by a production audit in a materials laboratory covering projects performed over almost 5 years. Tracing eight baseline studies from sample to stored value showed that the initial ELN structure preserved the l...
  </details>

- **2026-10-19** — Luyang Zhang, Minxing Zheng, Jialu Wang — [Correcting Attribution Patching with a Few Exact Measurements](http://arxiv.org/abs/2610.27393v1)
  <details><summary>📄 Abstract</summary>
  Mechanistic interpretability asks which language model components matter for a behavior, and activation patching answers by changing one component's activation and measuring its effect, at a cost growing with components and prompts. Attribution patching estimates these effects from one gradient pass, but its estimates can be far off, and verifying each one restores the cost. Can the structure of these errors reduce this cost? We propose Guided-AP, which uses a few exact measurements to reveal at...
  </details>


### 📂 unlearning
*机器遗忘 / Machine Unlearning* — 1 papers

- **2026-10-21** — Yiyang Duan, Fan Wu, Tiantong Wu et al. — [C$^2$U in RAG: Compositional Concept Unlearning in Retrieval-Augmented Generation](http://arxiv.org/abs/2610.29223v1)
  <details><summary>📄 Abstract</summary>
  Retrieval-augmented generation can expose unwanted concepts through retrieved evidence even when the generator is moderated. We study query-side concept suppression with a fixed encoder and document index. Compositional Concept Unlearning (C$^2$U) routes a profile-derived direction through an augmented atom bank, adding only a bounded edited-minus-original delta to the raw query. Across five datasets, four encoders, and three seeds, the validation-selected configuration reduces pooled binary tar...
  </details>


### 📂 benchmark
*安全评测与基准 / Safety Benchmarks & Evaluation* — 1 papers

- **2026-10-19** — Israel Abebe Azime, Jesujoba O. Alabi, Tajuddeen Gwadabe et al. — [African Languages AI Safety Readiness Report](http://arxiv.org/abs/2610.27269v1)
  <details><summary>📄 Abstract</summary>
  With the widespread adoption of large language models (LLMs) across languages and domains, AI safety has emerged as a critical global concern. However, due to resource constraints, research and development efforts tend to prioritize a limited number of high-resource languages, leaving many others, especially those spoken in Africa, underrepresented. While existing research on language "resource-ness" has largely examined whether sufficient resources are available to develop language technologies...
  </details>


### 📂 survey
*综述与系统化 / Surveys & Systematization* — 9 papers

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

- **2026-10-20** — Jakob Steimle, Thomas Elsken, Daniel Ehrhardt et al. — [Don't Skip the Baseline: A Controlled Comparison of Dynamic Expert Skipping in MoEs](http://arxiv.org/abs/2610.28369v1)
  <details><summary>📄 Abstract</summary>
  A growing body of work proposes dynamic expert-skipping methods for Mixture-of-Experts (MoE) models that adjust the number of experts activated per token during inference, aiming to preserve model quality while further reducing the number of active parameters. These methods have added calibrated importance scores, inter-expert similarity metrics, or learned per-token allocators in order to identify experts to skip. However, different calibration regimes, different reductions in the effective num...
  </details>

- **2026-10-20** — Marc Chapus, Carlos Crispim-Junior, Véronique Eglin et al. — [CountVideoBench: A Benchmark to Evaluate Prediction Biases on the Object Counting task by Video-Language Models](http://arxiv.org/abs/2610.28356v1)
  <details><summary>📄 Abstract</summary>
  Object counting in videos remains a poorly characterized capability of multimodal large language models. Counting questions are included in many existing VideoQA benchmarks, but the ground-truth count distributions in these benchmarks are heavily skewed toward small values. Across the nine benchmarks we survey, the median ground-truth count is at most five, and the three most frequent values together account for between 45% and 93% of the videos. The resulting mean accuracy is then dominated by ...
  </details>

- **2026-10-19** — Won Seok Jang, Harry Bhaskar Joshi, Hong Yu — [Does Multi-Agent Collaboration Reduce Hallucination in Clinical Tasks?](http://arxiv.org/abs/2610.27027v1)
  <details><summary>📄 Abstract</summary>
  Multi-agent LLM systems improve performance on clinical tasks, and that improvement is often read as evidence of a more trustworthy system. However, the two are not the same claim. A clinician acts on the stated reasoning and not only on the conclusion, so whether collaboration reduces hallucination, and what decides when it does, has to be measured in the reasoning too. Yet most evaluations score only the final answer. We evaluate four systems (a single-LLM baseline and three multi-agent topolo...
  </details>


### 📂 other
*其他安全相关 / Other Security-Related* — 170 papers

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

- **2026-10-20** — Nikita Ganziuk, Innokentiy S. Humonen, Ilya Makarov et al. — [MythoSemantic: An Interactive System for Discovering Semantic Parallels Across Mythological and Religious Traditions](http://arxiv.org/abs/2610.28452v1)
  <details><summary>📄 Abstract</summary>
  We present a tool for the comparative study of mythological and religious texts. Traditional manual analysis is highly labor-intensive and difficult to scale. To address this, we use neural language models to embed texts into a shared semantic space, so that users can find semantic parallels across cultural traditions in an interactive interface. Embedded fragments form distinct semantic structures whose coarse geometry aligns with well-documented historical relations between traditions. We quan...
  </details>

- **2026-10-20** — Charbel Abi Hana, Rayan Zaitouni, Kameel Amareen et al. — [Physical AI for Intralogistics: Benchmarking the NVIDIA Sim-to-Real Ecosystem for Cosmos-Enhanced COMPASS Navigation on Industrial Mobile Robots](http://arxiv.org/abs/2610.28432v1)
  <details><summary>📄 Abstract</summary>
  Classical robot navigation stacks are reliable but often require re-engineering for each new robot type and site. Learning-based navigation shifts this effort from hand-tuned parameters to data generation and training, where a policy adapts to each new embodiment or facility by fine-tuning in simulation. Whether policies adapted this way stay reliable on real industrial robots has seen little systematic testing. We study this for NVIDIA's X-Mobility and COMPASS workflow for training learned navi...
  </details>

- **2026-10-20** — Sumaiya Fazal, Rizwan Qureshi, Laleh Behjat et al. — [Gated Prototype Transfer for Zero-Support Medical Vision Language Model](http://arxiv.org/abs/2610.28350v1)
  <details><summary>📄 Abstract</summary>
  Realistic few-shot adaptation of medical vision-language models (VLMs) can leave low-prevalence classes without any labeled support. The training-free SS- Text+ solver remains operational in this setting, but its zero-support prototypes receive no visual adaptation and fall back to a purely textual class prototype. We in- troduce Gated Knowledge-Guided Prototype Transfer (GProtoT), a pre-repulsion module that transfers supported-class visual residuals to missing classes using VLM similarity and ...
  </details>

- **2026-10-20** — Indrakshi Dey, Nicola Marchetti — [Conformal Koopman Certificates for Nonlinear Multi-Agent Consensus on Time-Evolving Graphs](http://arxiv.org/abs/2610.28285v1)
  <details><summary>📄 Abstract</summary>
  Robot fleets must often agree on a shared value before they act, over wireless networks that change as the robots move. Their supervisor needs a deadline: the number of communication rounds after which the fleet has agreed with a stated probability. Today it comes from simulation plus a safety margin, with an open probability of being met. We certify it. Our method, conformal Koopman certification, rests on one observation: averaged over the random network changes, the expected behaviour of the ...
  </details>

- **2026-10-20** — Huachen Gao, Yang Yang, Xiaoqian Liang et al. — [HRoPE: Homography Relative Positional Encoding](http://arxiv.org/abs/2610.28284v1)
  <details><summary>📄 Abstract</summary>
  Geometric Relative Positional Encoding has become the primary mechanism for injecting spatial inductive biases into multi-view transformers. Existing designs condition attention on camera-level frustums or ray-marched depth, associating cross-view tokens through the sensor geometry. Such sensor-centric formulations, however, describe only where a token is observed from, leaving the rich surface geometry of the scene region depicted by the token. In this paper, we advocate a shift toward surface-...
  </details>

- **2026-10-20** — Artem Mikhaylov, Pavel Konoplev, Nikolay Efanov et al. — [RANGER: Retrieval Agent for Navigating Graphs with Semantic Evaluation Rewards](http://arxiv.org/abs/2610.28010v1)
  <details><summary>📄 Abstract</summary>
  The integration of Large Language Models and Reinforcement Learning offers a promising direction for complex sequential decision-making tasks, such as multi-hop question answering over knowledge graphs. While LLMs provide strong semantic understanding and reasoning capabilities, they often struggle with precise, multi-step navigation in structured environments. Conversely, RL agents excel at learning navigation policies but are hindered by the difficulty of designing semantically meaningful rewa...
  </details>

- **2026-10-20** — Jihai Zhang, Runjia Qian, Kaiqin Kong et al. — [Matrix-Game 4.0: Harnessing Video Models for Real-Time Playable Game Worlds](http://arxiv.org/abs/2610.27999v1)
  <details><summary>📄 Abstract</summary>
  Moving from controllable videos to genuinely playable worlds requires persistent world state, executable game rules, and low-latency interaction. We outline a roadmap for the next generation of Matrix-Game that separates game execution from visual generation through an executable game harness, and introduce Matrix-Game 4.0 as the first system built on this design. A lightweight game engine maintains world state and executes interaction rules, a multimodal coding agent translates player ideas int...
  </details>

- **2026-10-20** — Dayin Chen, Xiaodan Shi, Xin Xu et al. — [Foundation-Style Pretraining for Scalable and Transferable Distributed PV Forecasting](http://arxiv.org/abs/2610.27763v1)
  <details><summary>📄 Abstract</summary>
  The rapid growth of distributed photovoltaic (PV) generation is increasing the demand for accurate forecasting across large numbers of geographically dispersed stations. Existing approaches are commonly developed for individual sites or specific forecasting horizons, requiring repeated training and maintenance as new stations are integrated and limiting direct reuse at previously unseen sites. To address this scalability gap, this paper presents a domain-specific foundation-style pretraining fra...
  </details>

- **2026-10-20** — Xiang Lv, Kai Zhao, Qiang Wang et al. — [PixelSR: Pixel-Space Orthogonal Flow Decoupling for Real-World Image Super-Resolution](http://arxiv.org/abs/2610.27759v1)
  <details><summary>📄 Abstract</summary>
  Latent diffusion models have recently achieved remarkable progress in Real-world Image Super-Resolution (Real-SR). However, existing methods consistently exhibit a persistent seesaw effect: enhancing perceptual realism compromises structural fidelity. This effect, we argue, is not intrinsic to diffusion models, but largely stems from the architectural constraints of prevailing two-stage frameworks. To address this challenge, we propose PixelSR, a novel single-stage Pixel Diffusion Transformer fo...
  </details>

- **2026-10-20** — Pratik Jawanpuria, Bhabatosh Garai, Bamdev Mishra — [Constant Step Sizes for Muon-Type Spectral Optimizers on Strongly Convex Quadratics](http://arxiv.org/abs/2610.27747v1)
  <details><summary>📄 Abstract</summary>
  Muon and related optimizers update a weight matrix with a spectrally transformed gradient. In this work, we study such spectral optimizers with a constant step size on strongly convex matrix quadratics, which isolate the effect of the update from the confounds of nonconvexity, noise, and step size schedules. We analyze an update using two quantities: the gain, which is the factor by which it amplifies the gradient along each singular direction, and the length, which is the norm of the update. Th...
  </details>

- **2026-10-20** — Wenhan Li, Yangrui Zhang, Hang Zhou et al. — [Prescribed Performance Guided Safe Reinforcement Learning for Roundabout Navigation of Autonomous Vehicles](http://arxiv.org/abs/2610.27732v1)
  <details><summary>📄 Abstract</summary>
  Connected and Autonomous Vehicles (CAVs) face significant challenges in roundabout navigation due to dense traffic interactions and unpredictable agent behaviors, necessitating high levels of adaptability and safety. While the combination of Reinforcement Learning (RL) and Model Predictive Control (MPC) offers a promising approach, existing frameworks suffer from a structural mismatch where pointwise RL decisions fail to align with MPC's trajectory level optimization, and often lack rigorous saf...
  </details>

- **2026-10-20** — Thai Nguyen Van, Ibrahim Khan, Mury Fajar Dewantoro et al. — [Reusing Multimodal Agents: Efficient Evaluation of Sound Designs in Games](http://arxiv.org/abs/2610.27670v1)
  <details><summary>📄 Abstract</summary>
  This paper introduces a novel framework for efficiently evaluating in-game sound designs using multimodal learning and reinforcement learning. Sound design significantly influences gameplay and accessibility; however, objective evaluation methods, defined here as automated assessments based on agent performance rather than human ratings, often require retraining agents from scratch for each sound design. Our approach first pre-trains a multimodal encoder that encodes visual and auditory informat...
  </details>

- **2026-10-20** — Yuping Yan, Yaochu Jin — [Secure Multimodal Federated Optimization via Hierarchical DNA-Based Key Management](http://arxiv.org/abs/2610.27644v1)
  <details><summary>📄 Abstract</summary>
  Federated optimization over heterogeneous multimodal data enables distributed institutions to collaboratively optimize a shared model using medical images, genomic profiles, clinical records, and physiological signals without centralizing raw data. However, protecting modality-specific data throughout the optimization lifecycle remains insufficiently explored, particularly when heterogeneous modalities require separate encryption keys and selective local access. This paper proposes a secure mult...
  </details>

- **2026-10-20** — Pan Wang, Yihao Hu, Guangyuan Dong et al. — [PAR: Progress-Aligned Recurrence for Length Generalization in State Tracking](http://arxiv.org/abs/2610.27628v1)
  <details><summary>📄 Abstract</summary>
  Looped language models can run more iterations at test time, but additional iterations need not help them solve longer problems. For sequential state tracking, final-answer supervision does not specify how far each iteration should advance, and repeated updates can change the scale of the recurrent state. We introduce \textbf{Progress-Aligned Recurrence (PAR)}, which trains the prediction at iteration $k$ to match the state after the first $k$ operations and rescales recurrent states to their fi...
  </details>

- **2026-10-20** — Yubang Wang, Zezheng Huai, Yifei Zhang et al. — [Embodied Task Agents Can Perform Fine Manipulation through Tactile In-Context Learning](http://arxiv.org/abs/2610.27613v1)
  <details><summary>📄 Abstract</summary>
  Can embodied task agents use tactile experience to perform fine manipulation without task-specific model training? We investigate this capability through Tactile-ETA, a system that incorporates tactile experience into an embodied task agent through in-context learning. Successful expert demonstrations show how contact changes during manipulation. We pair each recorded robot movement with its camera views and bilateral tactile observations. We keep tactile observations at the start and end of eac...
  </details>

- **2026-10-20** — Yuxuan Li, Xiangchen Guan, Kunrong Li et al. — [DuplexLedger: Benchmarking Transactional Memory in Full-Duplex Speech Agents](http://arxiv.org/abs/2610.27581v1)
  <details><summary>📄 Abstract</summary>
  Full-duplex speech agents must update persistent memory while listening and speaking, yet it remains unclear which events should be stored, revised, or excluded. Existing benchmarks isolate interaction timing from memory outcomes, obscuring the state transitions behind a correct answer. We introduce DuplexLedger, a bilingual benchmark of 1,094 persistent sessions aligning four full-duplex scenarios with event-level Write/Update/Ignore/Retain supervision, explicit pre/post memory states, and 6,56...
  </details>

- **2026-10-20** — Xi Yang, Guodong Liu, Cheng Peng et al. — [Exploring Recurrent-Depth Language Models for Multitask Clinical Text Processing](http://arxiv.org/abs/2610.27559v1)
  <details><summary>📄 Abstract</summary>
  Clinical natural language processing includes diverse tasks such as information extraction, classification, and question answering. Developing one model for all tasks could simplify deployment and improve knowledge transfer. We evaluated whether small recurrent-depth language models can meet this need through joint fine-tuning and compared their performance with standard transformers. We fine-tuned Ouro1.4B-Thinking, Ouro-2.6B-Thinking, HRM-Text-1B, Qwen3-1.7B, and Qwen3-8B on 9 datasets coverin...
  </details>

- **2026-10-20** — Jian Zhang, Manrong Liu, Yilei Huang et al. — [Multiscale Temporal-Spectral-Spatial EEG Learning With Modality-Specific and Modality-Invariant Representations for Emotion Recognition](http://arxiv.org/abs/2610.27521v1)
  <details><summary>📄 Abstract</summary>
  Multimodal physiological signals provide complementary cues for emotion recognition. They also raise two related challenges. Emotion-related EEG patterns vary across time, frequency bands, electrodes, and brain regions. Different physiological modalities also contain both modality-specific and shared affective information. This paper presents GMSI-Net, an EEG-centered multimodal emotion recognition framework. It has three key components. The temporal-spatial-spectral-region (TSSR) encoder models...
  </details>

- **2026-10-20** — Haoxiang Luo, Bang Huang, Mohamed-Slim Alouini — [SAGE-HAP: Sustainability-Certified Agentic Communication and Computing at a Solar-Powered High-Altitude Platform](http://arxiv.org/abs/2610.27513v1)
  <details><summary>📄 Abstract</summary>
  The solar-powered High-Altitude Platforms (HAP) can provide persistent communication and computing services beyond terrestrial coverage. However, changing mission priorities, coupled resource demands, and uncertain solar supply complicate sustainable scheduling, while large language model proposals require independent feasibility checks. This paper proposes SAGE, a Sustainability-certified Agentic Ground-service Engine for a HAP. We formulate an energy-causal stochastic optimization problem inco...
  </details>

- **2026-10-20** — Rahul Sajnani, Diego Romeres, Mingyuan Zhang et al. — [UniWALM: Unified World Action Language Model for Embodied Robot Control](http://arxiv.org/abs/2610.28626v1)
  <details><summary>📄 Abstract</summary>
  Motivated by the human ability to integrate experience across language, perception, and action, we introduce UniWALM, a unified world-action-language model that learns video, action, and language in a single shared representation, where each modality is both a conditioning signal and a supervision target. We ask: can jointly generating language enrich this shared representation, improving manipulation and supporting memory-dependent behavior? Unlike prior approaches that attach a reasoning or vi...
  </details>

- **2026-10-20** — Xinxin Liu, Bingxin Xu, Wenrui Bao et al. — [AgenticRoboRL: Bringing Coding-Agent Post-Training to Agentic Robotics](http://arxiv.org/abs/2610.28589v1)
  <details><summary>📄 Abstract</summary>
  Agentic robotics systems combine planners with robot harnesses to perform complex manipulation tasks. Recent work improves these systems through better harnesses and external memory, but relies on powerful closed-source models as planners and does not improve the planners' own capabilities. In contrast, coding agents have improved substantially by post-training the model itself. We therefore investigate whether post-training can also improve robot planners. However, applying it across robot harn...
  </details>

- **2026-10-20** — Rundong Luo, Yunong Liu, Di Cao et al. — [SceneRig: An Agentic System for Simulation-Ready 3D Scene Reconstruction from Single Images](http://arxiv.org/abs/2610.28585v1)
  <details><summary>📄 Abstract</summary>
  Simulation is a powerful tool for robotics, but building diverse, simulation-ready scenes at scale remains difficult. Reconstructing scenes from single images is a promising alternative, but visual similarity alone is insufficient: objects must also be recovered, accurately placed, and physically grounded. Existing methods that rely on post-hoc physics settling often misplace objects, producing scenes that look correct but behave poorly under manipulation. We present SceneRig, an agentic system ...
  </details>

- **2026-10-20** — Ziyong Wang, Yupei Lin, Runxuan Huang et al. — [GPT-6-Astra Understands Touch and Outperform Vision--Tactile--Language--Action Models](http://arxiv.org/abs/2610.28457v1)
  <details><summary>📄 Abstract</summary>
  General-purpose multimodal models have shown promise as direct robot action policies, yet whether they grasp the physics underlying real-world interactions and can apply that understanding to guide action remains underexplored. We investigate this question using contact-rich manipulation as a representative testbed, examining tactile understanding as a concrete instance of this broader capability. Contact-rich manipulation requires interpreting tactile feedback and adjusting actions after obstru...
  </details>

- **2026-10-20** — Spiros Maggioros, Guray Erus, Gareth Harman et al. — [Brain2Vec: A Self-Supervised 3D Foundation Model for Structural Brain MRI](http://arxiv.org/abs/2610.28411v1)
  <details><summary>📄 Abstract</summary>
  Deep learning models have become essential tools in medical imaging, yet training them end-to-end for diverse tasks remains challenging due to limited labeled data and computational constraints. To address this, we introduce Brain2Vec, a foundation model pre-trained on 74,425 T1-weighted Magnetic Resonance Imaging (MRI) scans pooled from multiple studies. Brain2Vec can serve both as a weight initialization backbone for fine-tuning downstream tasks and as a standalone feature extractor. We evalua...
  </details>

- **2026-10-20** — Mayimunah Nagayi, Alice Scaria Khan, Tamryn Frank et al. — [Region-Guided Food-Package Evidence Extraction and Abstention-Aware Draft R3337 Screening with Selective VLM Review](http://arxiv.org/abs/2610.28211v1)
  <details><summary>📄 Abstract</summary>
  Applying South Africa's draft R3337 warning criteria to food-package photographs requires nutrition, ingredient and product-form evidence. This study presents a region-guided evidence extraction and abstention-aware screening workflow for draft R3337. A three-class detector localises nutrition information panels, ingredient lists and product-identity regions, after which PaddleOCR and structured extraction recover nutrient values, ingredient evidence and product-form information. Recovered evide...
  </details>

- **2026-10-20** — Xiaoxu Xu, Hao Li, Hongtao Zhang et al. — [From Predictive Geometry to Action: Learning Complementary Predictive Representations for Embodied Manipulation](http://arxiv.org/abs/2610.28164v1)
  <details><summary>📄 Abstract</summary>
  Effective manipulation requires a policy to capture not only about the current scene geometry, but also about how that geometry will evolve under interaction. Existing approaches either augment policies with geometric information from current observations or introduce future prediction as auxiliary supervision, leaving open how predictive geometry should be represented for action generation. Therefore, we propose a two-stage framework, which learns complementary predictive representations from m...
  </details>

- **2026-10-20** — Antonio Langella, Giovanni Minelli, Giovanni B. Dessy et al. — [LocoPilot: Single-Operator Bilateral Teleoperation for Loco-Manipulation Policy Learning](http://arxiv.org/abs/2610.27998v1)
  <details><summary>📄 Abstract</summary>
  Learning loco-manipulation policies requires demonstrations that capture coordinated base and arm motion on the target embodiment. Robot-free interfaces allow demonstrations to be collected independently of the target robot, increasing flexibility but without directly capturing platform-specific commands, proprioception, and body-mounted observations. On-robot teleoperation allows to capture these signals directly, but requires an interface capable of commanding the complete system concurrently....
  </details>

- **2026-10-20** — Jingjiao Zhao, Dong Jing, Mingyu Cao et al. — [EventSync: Event-Driven Memory Updates for History-Dependent Manipulation](http://arxiv.org/abs/2610.27917v1)
  <details><summary>📄 Abstract</summary>
  History-dependent robotic manipulation requires task context and interaction history, as the current observation alone is insufficient to determine the next action. Hierarchical frameworks use task memory for high-level subgoal reasoning and low-level policies for execution. However, memory updates require accurate completion assessment: similar observations may correspond to different execution phases, and prematurely recording completion can mislead subsequent subgoal reasoning. We present Eve...
  </details>

- **2026-10-20** — Manar Ali, Lisa Gottschalk, Simeon Junker et al. — [Testing Associative Creativity in Humans and Multimodal LLMs with Difficult-to-Name Visual Stimuli](http://arxiv.org/abs/2610.27894v1)
  <details><summary>📄 Abstract</summary>
  We investigate associative creativity in descriptions of abstract visual stimuli by humans and multimodal large language models (MLLMs). While conceptual association is central to human communication, it remains unclear how humans and models adapt when visual stimuli become increasingly difficult to map onto familiar semantic concepts. We evaluate several state-of-the-art MLLMs and human participants along two dimensions of creativity, originality and effectiveness, using two datasets with contr...
  </details>

- **2026-10-20** — Jiahong Tang, Jiaju He, Zhiyuan Yang et al. — [AWLS: Advantage-Weighted Latent Steering for One-Step Generative Robotic Manipulation Policies](http://arxiv.org/abs/2610.27736v1)
  <details><summary>📄 Abstract</summary>
  Human-collected real-world robotic manipulation demonstrations often contain mixed-quality trajectories, including hesitant, indirect, or inefficient action segments. While diffusion- and flow-based policies can model such multimodal data, standard behavior cloning (BC) assigns equal likelihood to all demonstrated actions and may therefore reproduce suboptimal modes. Offline RL value estimates offer a natural signal for biasing policies toward higher-value behavioral modes, but directly fine-tun...
  </details>

- **2026-10-20** — Eachen Soong, Zijian Niu, Haoran Xu et al. — [NeoWorld-3: From Pixels to Code-Defined Physical Worlds](http://arxiv.org/abs/2610.27690v1)
  <details><summary>📄 Abstract</summary>
  Simulation-ready world reconstruction demands physical interactivity beyond visual realism, which existing black-box 3D generation fails to deliver. We present NeoWorld-3, a coding-agent framework that reconstructs interactive 3D worlds from visual observations via tunable, executable programs. At its core, NeoSDK provides the underlying computational engine for low-level geometries, part composition, differentiable parameter refinement, and physics validation. At the same time, NeoMCP exposes t...
  </details>

- **2026-10-20** — Jad Yammine, Malek Wahidi, Abrar Anwar et al. — [Industrial ReMEmbR: Scaling Spatiotemporal Memory to Robot Fleets](http://arxiv.org/abs/2610.28624v1)
  <details><summary>📄 Abstract</summary>
  Warehouse robot fleets continuously observe operational conditions, but preserving these observations as reusable semantic memory incurs substantial computation, communication, and storage costs. For example, explaining recurring aisle blockages can require reviewing video from multiple robots across several shifts. We present IndustrialRemembr, a shared spatiotemporal memory system that extends NVIDIA ReMEmbR to robot fleets and reduces server-side computation by generating scene descriptions o...
  </details>

- **2026-10-20** — Yanbo Wang, Siqi Luo, Siyu Zhang et al. — [MindView: Benchmarking Generative Multi-View Spatial Intelligence](http://arxiv.org/abs/2610.28622v1)
  <details><summary>📄 Abstract</summary>
  Spatial intelligence has recently been assessed through generative tasks such as spatially grounded image editing, yet language-guided generation of spatially consistent views from partial multi-view observations remains underexplored. We introduce MindView, a benchmark for generative multi-view spatial intelligence with 1,500 samples from 513 scenes across three indoor datasets. Its seven tasks form two families: geometry-dominant tasks specify changes in camera position and orientation, while ...
  </details>

- **2026-10-20** — Noor Abo Mokh, Teresa Lynn, Nizar Habash et al. — [Benchmarking Arabic Dialects for Math Problems](http://arxiv.org/abs/2610.28607v1)
  <details><summary>📄 Abstract</summary>
  Mathematical reasoning remains underexplored for low-resource languages, including Dialectal Arabic. To bridge this gap, we introduce the DAR-MGSM (Dialectal Arabic Multilingual Grade School Math) Benchmark, the first manually curated benchmark for evaluating mathematical reasoning in Dialectal Arabic. DAR-MGSM consists of math word problems (MWPs) requiring multi-step reasoning and covers five major Arabic dialects alongside Modern Standard Arabic (MSA). The benchmark comprises two parallel ver...
  </details>

- **2026-10-20** — Shu Zhao, Tan Yu — [Capable Teacher, Myopic Scorer: Reward-Free Teacher Repair for Agentic On-Policy Distillation](http://arxiv.org/abs/2610.28586v1)
  <details><summary>📄 Abstract</summary>
  Agentic on-policy distillation (OPD) trains a student agent on its own trajectories while a teacher scores every token. A natural explanation of where it goes wrong is compounding error: the student's mistakes carry its trajectories beyond the region where the teacher is reliable, so recent methods keep training inside that region, through episode-length curricula, teacher-guided turns, prefix replay, or teacher intervention where the two disagree. We show this explanation is incomplete. From th...
  </details>

- **2026-10-20** — Azim Dehghani Amirabad, Ali Khodabandeh Yalabadi, Artem Moskalev et al. — [Spatially Informed and Direction Sensitive Representation Learning for Spatial Transcriptomics](http://arxiv.org/abs/2610.28579v1)
  <details><summary>📄 Abstract</summary>
  Cellular states are shaped by both intrinsic gene expression programs and the spatial microenvironment in which cells reside. Spatial transcriptomics makes this context measurable, but effective representation learning requires capturing both spatially informative molecular signals and intercellular organization. Existing approaches address these challenges only partially: conventional gene selection can overlook spatially structured signals, while methods for encoding cell-cell relationships of...
  </details>

- **2026-10-20** — Chenxu Niu, Batuhan Sencer, Wei Zhang et al. — [The Token-Energy Law of LLM Decode: Active Bytes and Realized Time Account for Joules per Token](http://arxiv.org/abs/2610.28576v1)
  <details><summary>📄 Abstract</summary>
  Energy-efficient deployment of large language models requires understanding how model architecture, hardware, and serving settings shape energy per generated token. We introduce the Token-Energy Law, a compact, interpretable model of GPU-board energy per output token for dense, full-history decoding. It relates token energy to two core dimensions: active bytes and realized decode time. Active bytes describe logical byte demand per output, separating dense weights shared within a decode iteration...
  </details>

- **2026-10-20** — Simon Mackenzie, Mashbat Suzuki — [Exact Envy-Free Cake Cutting with Polynomial Expected Queries](http://arxiv.org/abs/2610.28535v1)
  <details><summary>📄 Abstract</summary>
  Envy-free cake cutting asks how to divide a resource so that no agent prefers another agent's share. Finding such a division with few queries about preferences has been a longstanding challenge. Aziz and Mackenzie gave the first query bound depending only on the number $n$ of agents: a tower of six $n$'s. Subsequent improvements culminated in Ye and Bai's single-exponential bound of $n^{O(1)}2^n$. A large gap remains between this deterministic upper bound and Procaccia's general lower bound of $...
  </details>

- **2026-10-20** — Yiqing Shen, Mathias Unberath — [A Multi-Agent Framework for Automated Machine Learning with Evidence-based Planning for Medical Image Analysis](http://arxiv.org/abs/2610.28410v1)
  <details><summary>📄 Abstract</summary>
  Deep learning has become the default tool for medical image analysis, driven by the open-source movement. However, achieving the best performance on a given task remains difficult, with architecture selection and hyperparameter optimization (HPO) still considered "more of an art than a science". Automated machine learning (AutoML) automates parts of model training, yet helps little in medical imaging: general-purpose approaches lack medical architectures and preprocessing, and medical-focused on...
  </details>

- **2026-10-20** — Zijun Dou, Kun Luo, Chaofan Li et al. — [FALCA: Falsification-Aware Reinforcement Learning with Hierarchical Credit Assignment for Long-Horizon Deep Search Agents](http://arxiv.org/abs/2610.28361v1)
  <details><summary>📄 Abstract</summary>
  Long-horizon deep search requires LLM agents to iteratively decompose complex information needs, gather evidence from external sources, and maintain a reliable research state under multiple constraints. A central challenge is that early mistakes can be amplified over the search trajectory: agents may anchor on an incorrect candidate, collect partially supporting evidence, overlook contradictions, and accumulate errors that misguide subsequent reasoning. We propose FALCA, a falsification-aware fr...
  </details>

- **2026-10-20** — Rui Gong, Ruoyu Wang, Yalun Dai et al. — [S-Agent 2.0: Spatial Reasoning with a General Coding Agent](http://arxiv.org/abs/2610.28354v1)
  <details><summary>📄 Abstract</summary>
  Spatial reasoning asks a model to work out where objects are in 3D space, how they relate to one another, and how they move. Agentic VLMs have recently brought large improvements on such tasks by letting the model actively gather evidence with 3D perception tools instead of answering in a single pass. Even so, on many questions the tools return the right evidence and the model still does not arrive at the correct answer: the gap between model and tools, where raw readings become usable conclusio...
  </details>

- **2026-10-20** — Christian Meske, Tobias Hermanns, Florian Brachten — [The GenAI Who Knew Too Little: Revisiting Transactive Memory Systems in Human GenAI Collaboration](http://arxiv.org/abs/2610.28343v1)
  <details><summary>📄 Abstract</summary>
  Generative artificial intelligence (GenAI) is rapidly transforming knowledge work, creating new collaborative dynamics that challenge tradi-tional human-human interaction patterns. This study investigates how Transactive Memory Systems (TMS) manifest in human-GenAI collabora-tion. Through qualitative interpretive interviews with 14 knowledge work-ers and thematic analysis, we identified distinct TMS manifestations across its three main dimensions: (1) regarding specialization, expertise recogni-...
  </details>

- **2026-10-20** — Itai Shapira, Myra Cheng, Hadas Orgad — [Is Sycophancy a Form of In-Context Updating?](http://arxiv.org/abs/2610.28325v1)
  <details><summary>📄 Abstract</summary>
  Factual sycophancy, a language model's deference to a user's false beliefs, is usually understood as a bid for the user's approval at the expense of truthfulness. We argue that this framing over-emphasizes the user and propose viewing sycophancy as a failure within the broader and generally useful process of in-context updating, by which models revise their answers based on information supplied during an interaction. We support this view with behavioral and mechanistic evidence. First, models' r...
  </details>

- **2026-10-20** — Amit Lisha, Reut Tsarfaty — [From Abstraction to Action: DSLs for Natural Language Abstraction Interpretation and Execution](http://arxiv.org/abs/2610.28311v1)
  <details><summary>📄 Abstract</summary>
  Natural-language instructions often rely on high-level abstractions, such as asking an agent to ``stack blocks in a pyramid.'' Interpreting abstract instructions requires models to both identify the abstraction intended by the speaker, and unroll it into the many concrete actions that instantiate it. Language models struggle here: prior work has shown that performance degrades as the level of abstraction in the instruction rises. To bridge the gap between natural language abstraction and concret...
  </details>

- **2026-10-20** — T. Vignau Costa, J. Colbois, G. L. Rossini et al. — [Classical spin liquids in the kagome Ising model, and their link with magnetoelasticity](http://arxiv.org/abs/2610.28298v1)
  <details><summary>📄 Abstract</summary>
  We investigate a nearest-neighbor Ising model on the kagome lattice coupled to elastic lattice distortions. By integrating out the lattice degrees of freedom, we derive an approximate spin-only description in terms of a kagome \(J_1\)-\(J_2\)-\(J_{3}\) Ising model with interactions extending to third nearest-neighbors. Using tensor network methods complemented by classical Monte Carlo simulations, we revisit its zero-temperature phase diagram and characterize the ground states studied more than ...
  </details>

- **2026-10-20** — Tapan Parikh — [Forty Questions: Identifying a Language Model from One-Word Answers](http://arxiv.org/abs/2610.28281v1)
  <details><summary>📄 Abstract</summary>
  A model behind an API can be identified from its one-word answers to everyday questions such as "Name a sound" or "Name a poet". A model's profile records how often it gives each answer to each question. We attribute new answers to the model most likely to have given them. On a panel of 94 models, 40 answers identify the exact model 92.5% of the time, against 1.1% by chance. Profiles built through OpenRouter identified all ten models served by DeepInfra under blinded labels. A system prompt lowe...
  </details>

- **2026-10-20** — Argyrios Deligkas, Eduard Eiben, Robert Ganian et al. — [Subjective Valuations Make It Hard to be Fair: The Complexity of Resource Allocation to Groups of Agents](http://arxiv.org/abs/2610.28213v1)
  <details><summary>📄 Abstract</summary>
  We study the parameterized complexity of finding an EF1 allocation of indivisible items in the group-sharing setting, which has received increasing attention in recent years. There, items are not allocated to individual agents but rather to one of two (or possibly more) groups, and agents within that group all share the assigned items. We consider both the "fixed" (EF1-Fix) and "variable" (EF1-Var) group cases, where in the former the assignments of agents to groups are prescribed. While both ar...
  </details>

- **2026-10-20** — Cedric Derstroff, Jannis Blüml, Janosch Moos et al. — [Reframing Object-Centric Reinforcement Learning: From Absolute to Relative Representations](http://arxiv.org/abs/2610.28197v1)
  <details><summary>📄 Abstract</summary>
  Object-centric reinforcement learning agents typically receive each object's position in a fixed global frame, even though their decisions usually depend on where objects are relative to one another. These absolute views often fail to capture the local context that is most relevant to the agent's behavior. As a result, an agent must relearn the same response at every location where a configuration can occur, and its performance collapses when the scene is merely shifted. In this work, we propose...
  </details>

- **2026-10-20** — Somin Kim, Robert Feldt, Shin Yoo — [Foreword: Pre-Generation Prediction and Characterisation of LLM Test Failures using the Jacobian Lens](http://arxiv.org/abs/2610.28187v1)
  <details><summary>📄 Abstract</summary>
  Testing LLM-based software is expensive: each input needs several sampled responses, each judged by a costly oracle. Further, every prompt or model change calls for re-testing. Pre-generation adequacy measures cut this cost by ranking inputs by failure risk based on the model's internal state. However, the state of the art, Clotho, models only passing reference inputs, and its hidden-state representation says nothing about why inputs fail. We present Foreword, a framework built on two ideas: lea...
  </details>

- **2026-10-20** — Igor Sloev, Gerasimos Lianos — [The Scale of Universalization in Multiplicative Kantian Equilibrium](http://arxiv.org/abs/2610.28180v1)
  <details><summary>📄 Abstract</summary>
  Multiplicative Kantian equilibrium requires agents to evaluate whether they would prefer all players to change their actions by a common proportional factor. This note argues that such a counterfactual is not fully specified by the material payoff environment alone: one must also specify the scale in which proportional universalization is performed. Building on the Sher-Roemer discussion of strategic non-invariance, we characterize how a smooth monotone reparametrization of actions changes the m...
  </details>

- **2026-10-20** — Stephanie Fong, Yiwen Jiang, Qingyang Xu et al. — [Reading Too Much Into It? Interpretive Preferences and Commitment in LLM Mentalisation under Ambiguity](http://arxiv.org/abs/2610.28105v1)
  <details><summary>📄 Abstract</summary>
  Large Language Models (LLMs) are increasingly used for interpersonal advice, potentially shaping how users interpret ambiguous social encounters. Existing Theory of Mind evaluations typically rely on predefined answers, while uncertainty research overlooks LLMs' preferred explanations and confidence under psychological distress. To address these gaps, we introduce MentalLoom, a novel evaluation of LLM mentalisation comprising 604 ambiguous social episodes, matched depression and social anxiety d...
  </details>

- **2026-10-20** — Jan Kobiolka, Christian Frey, Josif Grabocka — [MuPACE: Learning to Pace Muon for LoRA Fine-Tuning](http://arxiv.org/abs/2610.28072v1)
  <details><summary>📄 Abstract</summary>
  Learning rate schedules are typically fixed before training begins, yet when fine-tuning large language models with low-rank adapters (LoRA), the appropriate scale varies substantially with the model, task, and adapter configuration. Practitioners re-tune a schedule for every new problem, yet a tuned schedule still cannot react to the training dynamics it encounters. We instead amortize learning rate selection across LoRA fine-tuning problems. We leave the base optimizer, Muon, untouched, so tha...
  </details>

- **2026-10-20** — Saber Zerhoudi, Jelena Mitrovic, Michael Granitzer — [AutoSim: A Self-Improving User Simulator for Conversational Search Evaluation](http://arxiv.org/abs/2610.28054v1)
  <details><summary>📄 Abstract</summary>
  User simulators promise to evaluate conversational search systems at a scale human studies cannot reach, but only if their behavior is realistic enough to trust. We study AutoSim, a conversational-search user simulator whose relevance judgments rank a controlled pool of retrieval systems in agreement with NIST across three TREC iKAT years (Kendall's $τ$ of $0.66$, $0.91$, and $0.91$; all $p{\le}0.002$), an agreement that survives removing its persona. AutoSim self-improves against a held-out sig...
  </details>

- **2026-10-20** — Andrea Campagner, Federico Cabitza, Vincenzo Crupi — [When Do Humans and Machines Truly Complement Each Other? Formal Conditions and Empirical Evidence for Human-AI Synergy](http://arxiv.org/abs/2610.27965v1)
  <details><summary>📄 Abstract</summary>
  Can humans and artificial intelligence cooperate such that their combination yields greater accuracy than either agent alone? This result, termed \emph{synergy} or \emph{complementarity}, is notoriously difficult to achieve, even when both agents possess significant independent accuracy. In this paper, we present a formal framework to model human-AI interaction through the lens of reliance patterns, which characterize the joint correctness structure of human and algorithmic decisions. We derive ...
  </details>

- **2026-10-20** — Rishi Advani, Abolfazl Asudeh — [Splitting Planar Necklaces with Few Straight Cuts](http://arxiv.org/abs/2610.27956v1)
  <details><summary>📄 Abstract</summary>
  In the classical necklace splitting problem, beads of different colors lie on a line, and the goal is to divide them among $k$ agents using as few cuts as possible so that every agent receives the same number of beads of each color. We study the planar analog in which a cut is a full straight line and the objective is minimizing the number of lines: $m$ points colored red and blue must be separated by straight-line cuts into regions that can be allocated to $k$ agents so that each agent receives...
  </details>

- **2026-10-20** — Mervat Abassy, Zhaoxin Feng, Tatsuki Kuribayashi et al. — [Why Do LLMs Accept Generics? Explaining Acceptability using Psycholinguistic and Model-Derived Factors](http://arxiv.org/abs/2610.27928v1)
  <details><summary>📄 Abstract</summary>
  Psycholinguistic studies explore why humans accept some generic statements but reject others by showing that these judgments depend on more than how common a property is. People consider several other factors such as how well it sets the kind apart from others or whether it is characteristic of the kind.   Inspired by the linguistic and cognitive literature, we explore to what extent factors from these studies explain how large language models (LLMs) judge generics. Our results with twelve model...
  </details>

- **2026-10-20** — Jiahui Ning, Liang Chen, Yuchen Liang et al. — [ACE-Compression: An Ability-Centric Evaluation of Compressed Large Language Models](http://arxiv.org/abs/2610.27913v1)
  <details><summary>📄 Abstract</summary>
  Model compression makes large language models deployable, but today's evaluation tells an incomplete story. Standard practice measures retained task performance and stops there. This misses a critical fact: compression perturbs the distributed knowledge embedded across billions of weights, and task scores alone cannot reveal which underlying abilities survive and which quietly collapse. To solve this question, we introduce ACE-Compression, an ability-centric evaluation framework. Instead of aski...
  </details>

- **2026-10-20** — Jiamei Xu, Jie Sun, Keshuang Tang et al. — [Agentic discovery of interpretable car-following laws from multi-source trajectory data](http://arxiv.org/abs/2610.27836v1)
  <details><summary>📄 Abstract</summary>
  Car-following (CF) models is a fundamental component of microscopic traffic simulation and underpin the analysis of collective traffic dynamics, while its modeling becomes more challenging due to diverse human driving behaviors and the increasing presence of automated vehicle. Analytical CF models offer interpretable representations of longitudinal vehicle interactions, but their prescribed functional structures may limit the representation of heterogeneous driving behavior. This study proposes ...
  </details>

- **2026-10-20** — Guanchen Li, Yixing Xu, Xuanwu Yin et al. — [SliMOO: Interpretable Multi-Objective Evolutionary Search for LLM Depth Pruning](http://arxiv.org/abs/2610.27812v1)
  <details><summary>📄 Abstract</summary>
  As large language models (LLMs) grow more powerful, their scale makes them costly to serve. Depth pruning offers a practical route to efficiency by directly reducing memory and latency without hardware-specific support. However, we observe that transformer layers exhibit markedly different task-dependent layer contributions, whereas existing depth-pruning methods ignore this heterogeneity and thus tend to optimize for a narrow domain or benchmark rather than preserve broad capability. This sugge...
  </details>

- **2026-10-20** — Riku Kisako, Tatsuki Kuribayashi, Ryohei Sasano — [Are Linguistic and Arithmetic Circuits Dissociated in LLMs?](http://arxiv.org/abs/2610.27790v1)
  <details><summary>📄 Abstract</summary>
  Large language models (LLMs) exhibit both knowledge of language, rendered by, for example, grammatical judgment ability, and abilities to perform tasks through language, such as math-word problem solving. Motivated by neurolinguistic studies of their neural dissociation in human brains, in this study, we investigate the overlap of their circuits in large language models (LLMs). Specifically, we examine the overlap and causal effects between the circuits extracted for linguistic and arithmetic ta...
  </details>

- **2026-10-20** — Yingxin Jia, Hui Geng, Wenxin Yang et al. — [Give the Model a Finger: Developmentally Aligned Evaluation of Counting in Vision-Language Models](http://arxiv.org/abs/2610.27756v1)
  <details><summary>📄 Abstract</summary>
  Vision-language models (VLMs) are exact on small sets and drift into estimation on larger ones, a profile reminiscent of children before they master counting. Children cross the barrier with epistemic actions: pointing at each item while reciting number words, moving counted items aside, partitioning the array. We give VLMs the same actions as dumb image tools with no visual intelligence of their own in a training-free agent loop. Our central claim is about measurement, not intervention: a model...
  </details>

- **2026-10-20** — Fan Ding, Fucai Ke, Kevin Yuchen Ma et al. — [JARVIS: From Visual Manuals to Autonomous Robotic Assembly](http://arxiv.org/abs/2610.27618v1)
  <details><summary>📄 Abstract</summary>
  Visual manuals communicate procedural knowledge through stepwise diagrams, but translating these instructions into reliable long-horizon robotic execution remains challenging. We introduce JARVIS, a method-agnostic benchmark for autonomous visual-manual-guided execution without additional language instructions. JARVIS comprises 236,679 LEGO assembly tasks across 8,987 scenes, with a carefully curated JARVIS-v1 suite of 50 tasks for interactive robotic evaluation. Tasks span varying initial struc...
  </details>

- **2026-10-20** — Koshiro Saito, Diasuke Oba, Danushka Bollegala et al. — [Beyond Model Weights: Sampling-Dependent Fairness in Diffusion Language Models](http://arxiv.org/abs/2610.27584v1)
  <details><summary>📄 Abstract</summary>
  Diffusion language models (DLMs) are emerging as a practical alternative to autoregressive language models (ARLMs), yet their fairness remains largely uncharacterized. DLMs introduce sampling controls with no direct autoregressive counterpart, such as block length and remasking strategy, that directly set their speed--quality operating point. This raises a basic question: does a DLM's measured social bias remain stable across these settings? Across LLaDA, LLaDA-1.5, and Dream on Open-BBQ, we fin...
  </details>

- **2026-10-20** — Jui-Chien Tsou, Hsuan-Chi Liu, Wei-Chin Wang et al. — [TeCoP: Accelerating Diffusion Large Language Model Decoding via Tentative Context Pipelining](http://arxiv.org/abs/2610.27583v1)
  <details><summary>📄 Abstract</summary>
  Diffusion large language models (dLLMs) predict multiple token positions per forward pass, yet block-wise decoders serialize generation and repeatedly recompute stable predictions. We attribute this inefficiency to coupling a prediction's readiness for irreversible commitment with its utility as context. We introduce Tentative Context Pipelining (TeCoP), a training-free decoder that decouples these roles through staggered block-parallel pipelining and draft-and-verify. TeCoP reuses stable but un...
  </details>

- **2026-10-20** — Marko Petković, Susanne Gooijer, José Manuel Vicent-Luna et al. — [RaspAssistant as an Agentic Framework for Automating Adsorption Simulation Research in Porous Materials](http://arxiv.org/abs/2610.27572v1)
  <details><summary>📄 Abstract</summary>
  Porous-material adsorption studies require coordinated structure preparation, force-field selection, simulation, validation, and interpretation, making end-to-end automation difficult. We test whether RaspAssistant, a hierarchical multi-agent framework, can carry an adsorption study from force-field preparation through validation and downstream separation analysis. Across twelve multi-agent workflow-reproduction runs spanning four adsorption and separation benchmarks, overall scores ranged from ...
  </details>

- **2026-10-20** — Yuxing Peng, Zhiqing Tang, Weijia Jia — [Lower Bounds for Smooth Nonconvex Zeroth-Order Optimization: The Price of Determinism under Low Curvature Trace](http://arxiv.org/abs/2610.27550v1)
  <details><summary>📄 Abstract</summary>
  Low curvature trace, an effective rank condition, is a common explanation for why randomized zeroth-order methods scale to high-dimensional tasks such as language model fine-tuning. Can deterministic methods achieve the same savings? We show that they cannot. We study finding $\varepsilon$-stationary points of $L$-smooth nonconvex functions on $\mathbb{R}^d$ from exact function values, assuming that below the starting value the Hessian is dominated by a fixed matrix with trace at most $LE$; this...
  </details>

- **2026-10-20** — Marilyn Zhang, Tianfeng Chen, Patricia M Pechter et al. — [When Health Assistants Agree Too Readily: A Benchmark of Time-Critical Self-Diagnosis](http://arxiv.org/abs/2610.27518v1)
  <details><summary>📄 Abstract</summary>
  Every day, more than 40 million people ask ChatGPT a health question, such as whether laptop posture explains a stiff neck and days of pounding headache. Posture is plausible, but meningitis is a time-critical possibility. We introduce SelfDx, a paired benchmark for whether models have the appropriate response behavior, a form of epistemic independence, in health questions where misplaced agreement with the user's self-diagnosis could delay urgent or emergency care. Each of 100 pairs contrasts a...
  </details>

- **2026-10-19** — Jianing Yin, Ziyi Chen, Hao Wang et al. — [VerifierBench: Benchmarking the Generation of Executable Verifiers for LLM Agents](http://arxiv.org/abs/2610.28679v1)
  <details><summary>📄 Abstract</summary>
  Agents need reliable ways to validate their outputs, both when completing tasks and when filtering synthetic training data. We study verifier generation: from the instruction and environment available for solving a task, an agent writes an executable verifier that must accept every valid solution and reject invalid ones. We introduce VerifierBench, a benchmark of 222 tasks from six agent benchmarks spanning tool-call, state-based, and code verification, with 4,993 hidden test cases that include ...
  </details>

- **2026-10-19** — Fedor Part, Valery Isaev, Sergey Sinchuk — [Theorem prover Arend](http://arxiv.org/abs/2610.27264v2)
  <details><summary>📄 Abstract</summary>
  This paper is an exposition of the theorem prover Arend developed at JetBrains Research. Arend language has been designed to facilitate the formalization of mathematics within the framework of univalent foundations and with the focus on constructive mathematics. It is based on a variant of homotopy type theory with cubical syntax that is more closely aligned with Martin-Löf Type Theory (MLTT) than fully computational cubical type theories, while still retaining some of their computational proper...
  </details>

- **2026-10-19** — Jiaming Liu, Xinghao Zhu, Yiming Zhang et al. — [Physical Words: A Vocabulary for Structuring Latent Reasoning in Robot Manipulation](http://arxiv.org/abs/2610.26854v3)
  <details><summary>📄 Abstract</summary>
  Multimodal reasoning provides robotic foundation models with predictive context needed for reliable action generation. However, language-based reasoning captures task semantics but struggles to express fine-grained physical dynamics, while latent reasoning models future state evolution but offers limited structure for organizing these dynamics into reusable reasoning primitives. To bridge this gap, we introduce PhysWord, a reasoning-before-acting foundation model built on Physical Words, which u...
  </details>

- **2026-10-19** — Juan Pablo Vigneaux, Jennifer Cole — [Steering intonational tunes in text-to-speech synthesis](http://arxiv.org/abs/2610.27403v1)
  <details><summary>📄 Abstract</summary>
  Text-to-speech systems built on residual vector quantization often generate audio in two stages: a transformer backbone emits the first level of each frame's token stack, and a smaller depth model generates the rest autoregressively. We ask which components of such a model are responsible for prosodic intonation, more precisely for generating the English nuclear tune (for instance, the falling pitch melody that distinguishes an assertion from a question's rising melody), and whether intervention...
  </details>

- **2026-10-19** — Akash Gokul, Srijan Bansal, Yingbo Zhou et al. — [TEX: Test-Time Scaling Testing Agents via Execution-based Cross-Validation](http://arxiv.org/abs/2610.27290v1)
  <details><summary>📄 Abstract</summary>
  Test-case generation is critical but remains challenging for language models. Existing test-time scaling methods either isolate candidates or aggregate traces, which do not scale to long-horizon tasks. We present TEX, a collaborative test-time scaling framework based on execution-driven cross-validation. TEX parallelizes agents to generate tests and patches, cross-executing each test against every patch to form a $K \times K$ feedback matrix. Agents use their matrix slices for refinement, enabli...
  </details>

- **2026-10-19** — Fedor Part, Valery Isaev, Sergey Sinchuk — [Theorem prover Arend](http://arxiv.org/abs/2610.27264v1)
  <details><summary>📄 Abstract</summary>
  This paper is an exposition of the theorem prover Arend developed at JetBrains Research. Arend language has been designed to facilitate the formalization of mathematics within the framework of univalent foundations and with the focus on constructive mathematics. It is based on a variant of homotopy type theory with cubical syntax that is more closely aligned with Martin-Löf Type Theory (MLTT) than fully computational cubical type theories, while still retaining some of their computational proper...
  </details>

- **2026-10-19** — Zhiwei Liu, Zhujun Lan, Jielin Qiu et al. — [EGI-BENCH: An Enterprise General Intelligence Benchmark Suite](http://arxiv.org/abs/2610.27234v1)
  <details><summary>📄 Abstract</summary>
  Enterprise adoption of LLMs in agentic workflows is gated by evaluations that span a wide arc of abilities: CRM operations, heterogeneous-document retrieval, personal data understanding, multi-turn planning, tool use, function calling, long-horizon research, and long-context software engineering. These evaluations live today in separate repositories with divergent runners, dependencies, and scoring conventions, which makes cross-benchmark comparison difficult and obscures what a single aggregate...
  </details>

- **2026-10-19** — Samee Arif, Furkan Danisman, Angana Borah et al. — [The Culture Within: Towards Mechanistic Understanding of Cultural Reasoning in LLMs](http://arxiv.org/abs/2610.27202v1)
  <details><summary>📄 Abstract</summary>
  Large Language Models (LLMs) increasingly operate across culturally diverse settings, yet existing evaluations largely measure cultural behavior at the output level. We introduce CultureLens, a reference-grounded benchmark and mechanistic study of how LLMs use cultural information. CultureLens contains 9,261 scenarios across 75 countries and systematically varies country, value, true-norm, and contradictory-norm evidence. Across Llama-3.1-8B, Gemma-3-12B, and Qwen-3.5-27B, stating a contradictor...
  </details>

- **2026-10-19** — George Nigmatulin, Valentin Mohl, Sascha Frey et al. — [LOB-Impact Benchmark: Emergent Market Impact in Generative Limit Order Book Models](http://arxiv.org/abs/2610.27100v1)
  <details><summary>📄 Abstract</summary>
  Realistic market impact is essential for generative limit order book (LOB) models to serve as world models for trading agents. If a simulator misprices this mechanism, agents learn policies that are optimal in the simulator but wrong in the real market. Existing metrics assess generated streams purely through distributional comparison with historical data, leaving counterfactual response to an agent's own orders largely unexplored. Here, we show that market impact emerges naturally in neural LOB...
  </details>

- **2026-10-19** — Jiaming Liu, Xinghao Zhu, Yiming Zhang et al. — [Physical Words: A Vocabulary for Structuring Latent Reasoning in Robot Manipulation](http://arxiv.org/abs/2610.26854v2)
  <details><summary>📄 Abstract</summary>
  Multimodal reasoning provides robotic foundation models with predictive context needed for reliable action generation. However, language-based reasoning captures task semantics but struggles to express fine-grained physical dynamics, while latent reasoning models future state evolution but offers limited structure for organizing these dynamics into reusable reasoning primitives. To bridge this gap, we introduce PhysWord, a reasoning-before-acting foundation model built on Physical Words, which u...
  </details>

- **2026-10-19** — Zeyu Zheng, Yiyang Liu, Yuyang Zhao et al. — [ReuF2F: Benchmarking Coding Agents on Formalized Undergraduate Research Problems](http://arxiv.org/abs/2610.27046v1)
  <details><summary>📄 Abstract</summary>
  As AI systems begin to resolve open research problems, reliable verification becomes increasingly important. Formal mathematics provides a trusted framework for mathematical reasoning, enabling agents to produce machine-checkable proofs while conducting mathematical exploration. Existing formal mathematics benchmarks often focus on known results or a small set of prominent open problems, which can become difficult to evaluate reliably once solutions are discovered and widely disseminated. Existi...
  </details>

- **2026-10-19** — Min-Seong Kim, Jongbok Won, Jeesup Park et al. — [Rethinking LLM Fine-Tuning via Weight Space Reparameterization: Preserving Safety during Downstream Adaptation](http://arxiv.org/abs/2610.26443v2)
  <details><summary>📄 Abstract</summary>
  Fine-tuning large language models (LLMs) on downstream tasks often weakens their previously aligned safety behavior, creating an inherent trade-off between task adaptation and safety preservation. Existing approaches attempt to mitigate this issue by identifying safety-relevant neurons, layers, or update directions in the original parameter space. However, safety-related information is often distributed across many directions in this space, causing downstream updates to overwrite parameters that...
  </details>

- **2026-10-19** — Jennifer Hsia, Zachary C. Lipton, Aarti Singh — [Joint Constraint Aggregation for Qualifier-Sensitive Retrieval-Augmented QA](http://arxiv.org/abs/2610.27114v1)
  <details><summary>📄 Abstract</summary>
  Retrieval-augmented QA can fail even when the correct answer is in the retrieved evidence. This can happen when a competing answer satisfies some, but not all, of the question's requirements and is mentioned frequently in the retrieved documents, which can make it appear to be the best-supported answer. To test whether this retrieval skew actually affects the decision, we manipulate it directly: increasing the prevalence of passages that favor the competing answer makes the model more likely to ...
  </details>

- **2026-10-19** — Zijian Liu, Chaoyou Fu, Yan Yang et al. — [Omni-Woodpecker: Hallucination Correction via Evidence-Prior Rebalancing for Omni LLMs](http://arxiv.org/abs/2610.27103v1)
  <details><summary>📄 Abstract</summary>
  Recent Omni LLMs (OLLMs) have demonstrated remarkable capabilities in joint audio-visual reasoning, yet cross-modal hallucinations remain a major challenge. Existing mitigation methods mainly operate at the output level, overlooking the entanglement of grounding evidence and learned priors within fused representations. To address this issue, we propose Omni-Woodpecker (OWP), a training-free framework that shifts hallucination mitigation from output-level manipulation to conflict-conditioned repr...
  </details>

- **2026-10-19** — Yinhe Wang, Tao Tao, Zexin He et al. — [ACE-Brain-0.6: Scaling Spatial Grounding for Physical Foundation Models](http://arxiv.org/abs/2610.27040v1)
  <details><summary>📄 Abstract</summary>
  General-purpose multimodal models, including GPT-6 Astra and Claude Opus 5.5, demonstrate broad capabilities in embodied manipulation. Our analysis indicates that this generality is accompanied by strong spatial perception, as Astra can determine where to interact with task-relevant entities amid visual distractors. Because spatial perception connects high-level reasoning to the physical scene, we investigate scaling visual grounding to strengthen the perceptual foundation of general embodied op...
  </details>

- **2026-10-19** — Feng Chen, Pei Zhou, Lixuan He et al. — [Embodied Playground: A Long-Horizon Agentic Robotics Benchmark for Physical, Strategic, and Spatial Reasoning](http://arxiv.org/abs/2610.27039v1)
  <details><summary>📄 Abstract</summary>
  Foundation models offer a promising basis for robotic agents, but long-horizon tasks require them to sustain coherent reasoning and reliable physical execution across interdependent stages. We introduce Embodied Playground, a benchmark for evaluating how foundation-model agents coordinate physical, strategic, and spatial reasoning throughout such tasks. Agents must track task progress, satisfy intermediate constraints, and revise their plans using execution feedback as earlier actions shape subs...
  </details>

- **2026-10-19** — Oveys Delafrooz Noroozi, Bhagyashree Puranik, Upamanyu Madhow — [Shaped SAEs: Expanding the Toolkit for Mechanistic Interpretability](http://arxiv.org/abs/2610.27375v1)
  <details><summary>📄 Abstract</summary>
  Sparse autoencoders (SAEs) seek to decompose the dense activations of large language models (LLMs) into sparse, potentially interpretable features using a learned overcomplete dictionary. In this work, we ask whether it is possible to enhance the semantic selectivity of the learned dictionary atoms by linearly \emph{shaping} the dense activations prior to learning an SAE. We explore rank-reducing transformations based on the recently introduced J-space corresponding to the averaged Jacobian from...
  </details>

- **2026-10-19** — Soukaina Alaoui Ismaili, Jean-Sebastien Dessureault — [An LLM-Based Agent for Legal Compliance Assessment: Architecture, Memory, and Evaluation in a Canadian and Quebec Context](http://arxiv.org/abs/2610.27347v1)
  <details><summary>📄 Abstract</summary>
  Checking whether a text complies with a body of law is slow when done by hand and fragile when done with keyword rules. This paper presents ComplianceAgent, the legal compliance sub-agent of COMPASS, a multi-agent framework that evaluates texts along four axes: digital sovereignty, carbon impact, compliance, and ethics. The agent relies on a large language model that scores a text on a fixed rubric, grounds its judgment in a reference legal corpus, and, when the score falls at or below a critica...
  </details>

- **2026-10-19** — Hangyue Zhang, Qiran Hu, Ziyi Zhang et al. — [Inspectable LLM-Simulated Participants for Qualitative Interview Rehearsal](http://arxiv.org/abs/2610.27333v1)
  <details><summary>📄 Abstract</summary>
  LLMs are increasingly used across research workflows, including research ideation, qualitative analysis, and participant simulation. Within work on participant simulation, prior studies have largely evaluated simulated participants by how realistic or human-like their responses appear, leaving less known about how researchers use and critique these materials when revising interview protocols before fieldwork. We present Rehearsim, an inspectable research probe that treats LLM-simulated participa...
  </details>

- **2026-10-19** — Paraskevi Platanou, John Pavlopoulos — [What Not to Erase: Saliency-Constrained Augmentation for Low-Resource Handwritten Character Recognition](http://arxiv.org/abs/2610.27309v1)
  <details><summary>📄 Abstract</summary>
  Optical Character Recognition (OCR) and handwritten character recognition (HCR) in low-resource historical material collections often rely on data augmentation, yet augmentation strategies are typically evaluated almost exclusively through predictive accuracy. This leaves open whether a model's improved performance is accompanied by saliency stability. This question is important in low-resource historical HCR, where recognition is performed on variable and partially degraded letterforms and two ...
  </details>

- **2026-10-19** — Yuqiao Wen, Lili Mou — [ICLHerd: Herding-Based Data Selection for LLMs with In-Context Learning as a Proxy](http://arxiv.org/abs/2610.27142v1)
  <details><summary>📄 Abstract</summary>
  Data selection plays a central role in modern large language model training, as the quality of training data strongly influences downstream performance. A common approach is to curate a development set that encodes the desired skills (e.g., reasoning or multilinguality) and select data that are similar to them. Existing methods compute similarity using cosine distance over either the model's hidden states or gradients. However, we observe that this max-similarity strategy induces a mode-seeking ...
  </details>

- **2026-10-19** — Lijia Wu, Zheng Li, Yuxuan Liu et al. — [SciFigBench: A Benchmark for Scientific Method Figure Understanding](http://arxiv.org/abs/2610.27087v1)
  <details><summary>📄 Abstract</summary>
  Scientific method figures often provide researchers with a clear visual entry point into a paper's methodology and core contributions, yet their dense layouts and complex information flows are difficult for Vision Language Models (VLMs) to interpret. Existing benchmarks predominantly focus on coarse-grained tasks, such as context-based retrieval or holistic comprehension, overlooking the fine-grained content and inter-module relations within complex methodological diagrams. To address these over...
  </details>

- **2026-10-19** — Motti Goldberger, Nils Rudi — [Selecting the Best Few with Human Evaluators: Adaptively Combining Ratings and Pairwise Comparisons](http://arxiv.org/abs/2610.26380v2)
  <details><summary>📄 Abstract</summary>
  This paper considers a decision-maker tasked with identifying the $k$ best items from a large pool of candidates, such as job applicants, LLMs, award nominees, or new product ideas. The decision-maker learns about the items' quality by soliciting human evaluations. Each evaluation can be costly, so the decision-maker aims to use the limited evaluation budget efficiently by allocating evaluations adaptively. A key consideration is the form of evaluation to solicit, which should be something evalu...
  </details>


## 📊 统计 / Statistics

| 分类 / Category | 论文数 / Count |
|------|--------|
| jailbreak | 689 |
| prompt-injection | 632 |
| memory-poisoning | 56 |
| tool-use-attack | 160 |
| backdoor | 533 |
| adversarial-attack | 646 |
| privacy-leakage | 4443 |
| steganography | 81 |
| misuse | 1221 |
| red-teaming | 144 |
| vulnerability | 3704 |
| defense | 3569 |
| alignment | 3365 |
| robustness | 3655 |
| watermark | 641 |
| unlearning | 117 |
| agent-safety | 65 |
| benchmark | 70 |
| survey | 417 |
| other | 9829 |

---

📚 **全部 34037 篇论文**（2022 至今）请访问 [GitHub Pages](https://ny1024.github.io/AgentSafety-Papers/) 查看完整列表、搜索与筛选。

*Generated by AgentGuard at 2026-10-22 21:07:19*