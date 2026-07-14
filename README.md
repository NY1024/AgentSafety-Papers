<div align="center">

# AgentGuard 🛡️

**Daily Tracking of LLM Agent Security Papers on arXiv**

[![Auto Update](https://github.com/NY1024/AgentSafety-Papers/actions/workflows/daily-update.yml/badge.svg)](https://github.com/NY1024/AgentSafety-Papers/actions/workflows/daily-update.yml)
[![Papers](https://img.shields.io/badge/Papers-20411-blue)](#)
[![License](https://img.shields.io/badge/License-MIT-green)](#)

</div>

---

## 📖 简介 / Introduction

自动追踪 arXiv 上大模型 Agent 安全方向的最新论文，每日更新，关键词智能分类。

*Automatically tracking the latest LLM Agent security papers on arXiv, updated daily with keyword-based classification.*

**最近更新 / Last Updated**: 2026-07-14 02:35 ｜ **论文总数 / Total Papers**: 20411（近 30 天 / Recent 30 days: 3823）

🌐 **[GitHub Pages](https://ny1024.github.io/AgentSafety-Papers/)** — 查看全部 20411 篇论文（含摘要、分类筛选、搜索）/ View all 20411 papers with abstracts, filters & search

## 📑 分类导航 / Category Navigation

- **[jailbreak](#-jailbreak)** — 越狱攻击 / Jailbreak Attacks — 542
- **[prompt-injection](#-prompt-injection)** — 提示注入攻击 / Prompt Injection Attacks — 449
- **[memory-poisoning](#-memory-poisoning)** — 记忆投毒与篡改 / Memory Poisoning & Tampering — 36
- **[tool-use-attack](#-tool-use-attack)** — 工具使用攻击 / Tool-Use Attacks — 91
- **[backdoor](#-backdoor)** — 后门与投毒攻击 / Backdoor & Poisoning Attacks — 384
- **[adversarial-attack](#-adversarial-attack)** — 对抗攻击 / Adversarial Attacks — 525
- **[privacy-leakage](#-privacy-leakage)** — 隐私泄露 / Privacy Leakage — 3662
- **[steganography](#-steganography)** — 隐写与隐蔽通信 / Steganography & Covert Communication — 52
- **[misuse](#-misuse)** — 滥用与误用 / Misuse & Abuse — 798
- **[red-teaming](#-red-teaming)** — 红队测试 / Red Teaming — 105
- **[vulnerability](#-vulnerability)** — 漏洞与攻击面 / Vulnerabilities & Attack Surfaces — 2385
- **[defense](#-defense)** — 防御与防护方法 / Defense & Protection Methods — 2013
- **[alignment](#-alignment)** — 对齐与安全约束 / Alignment & Safety Constraints — 1844
- **[robustness](#-robustness)** — 鲁棒性与可靠性 / Robustness & Reliability — 1677
- **[watermark](#-watermark)** — 水印与溯源 / Watermarking & Provenance — 169
- **[unlearning](#-unlearning)** — 机器遗忘 / Machine Unlearning — 81
- **[agent-safety](#-agent-safety)** — Agent 安全框架 / Agent Safety Frameworks — 48
- **[benchmark](#-benchmark)** — 安全评测与基准 / Safety Benchmarks & Evaluation — 53
- **[survey](#-survey)** — 综述与系统化 / Surveys & Systematization — 239
- **[other](#-other)** — 其他安全相关 / Other Security-Related — 5258

## 📄 近期论文 / Recent Papers (Last 30 Days)

> 仅展示最近 30 天中最新的 500 篇论文（含日期、作者、摘要）。近 30 天共 3823 篇，完整 20411 篇论文列表请访问 [GitHub Pages](https://ny1024.github.io/AgentSafety-Papers/)

> Showing the latest 500 of 3823 papers from the last 30 days (with date, authors & abstract). For the full list of 20411 papers, visit [GitHub Pages](https://ny1024.github.io/AgentSafety-Papers/)

### 📂 jailbreak
*越狱攻击 / Jailbreak Attacks* — 5 papers

- **2026-07-09** — Jennifer Za, Julija Bainiaksina, Nikita Ostrovsky et al. — [Persuasion Attacks Can Decrease Effectiveness of CoT Monitoring](http://arxiv.org/abs/2607.08066v1)
  <details><summary>📄 Abstract</summary>
  Chain-of-thought (CoT) monitoring is a promising safety mechanism for AI agents, based on the premise that visible reasoning traces can surface misaligned or deceptive behavior. While effective in standard scenarios, recent work highlights that LLMs remain vulnerable to persuasion-based jailbreaks, where natural-language arguments override model constraints. We stress-test whether this vulnerability extends to monitoring LLMs: can an adversarial agent persuade its CoT monitor to approve proposed...
  </details>

- **2026-07-08** — Mohamed Amine Merzouk, Nolan Smyth, Damiano Fornasiere et al. — [Efficient Safety Alignment of Language Models via Latent Personality Traits](http://arxiv.org/abs/2607.07918v1)
  <details><summary>📄 Abstract</summary>
  Current safety methods for large language models are known to be vulnerable to adversarial attacks, motivating research into robust alternatives. Latent Adversarial Training (LAT) is among the most effective defenses, but can degrade utility and requires training on large datasets of harmful prompts. We introduce Latent Personality Alignment (LPA), which replaces explicit harm refusal with adversarial training on just 66 harm-agnostic statements drawn from psychometric personality literature. We...
  </details>

- **2026-07-08** — Anupam Wagle, Ifrat Ikhtear Uddin, Chaowei Zhang et al. — [Mechanistic Interpretability of LLM Jailbreaks via Internal Attribution Graphs](http://arxiv.org/abs/2607.07903v1)
  <details><summary>📄 Abstract</summary>
  Large language models (LLMs) exhibit remarkable capabilities but remain highly vulnerable to adversarial prompts and jailbreak attacks. Existing approaches primarily analyze these failures through input-output behaviors or attribution methods, offering limited insight into how adversarial perturbations alter the model's internal reasoning. Consequently, the mechanisms underlying unsafe or incorrect behaviors remain poorly understood. We introduce a mechanistic framework for diagnosing LLM vulner...
  </details>

- **2026-07-08** — Victor Giannakouris, Immanuel Trummer — [Breaking Database Lock-in: Agentic Regeneration of High Performance Storage Readers for Database Bypass](http://arxiv.org/abs/2607.07696v1)
  <details><summary>📄 Abstract</summary>
  Analytical workloads operating on data stored in external database systems face a fundamental bottleneck: data access is guarded entirely by the database driver, like JDBC or ODBC, forcing all reads through query execution and other driver layers that are not designed for bulk columnar analytics. We present Jailbreak, an approach that bypasses the database engine entirely by reading storage files directly and materializing data as in-memory columnar buffers. Jailbreak's key insight is that datab...
  </details>

- **2026-07-08** — Aoxiong Zeng, Yuxin Yang, Xiangquan Yang — [Online Data Selection Is Implicit Alignment](http://arxiv.org/abs/2607.07023v1)
  <details><summary>📄 Abstract</summary>
  Supervised fine-tuning (SFT) is often treated as a capability-adaptation step, while alignment is attributed to later preference optimization or reinforcement learning. This separation is incomplete: when examples are scored and kept online during fine-tuning, the choice of which data to train on already changes the model's behavioral preferences. We study online data selection as an implicit alignment mechanism. Given the same base model, optimizer, and selected-token budget, we compare random,...
  </details>


### 📂 prompt-injection
*提示注入攻击 / Prompt Injection Attacks* — 8 papers

- **2026-07-09** — Hugo García Cuesta, Pablo Mateo Torrejón, Alfonso Sánchez-Macián — [Multi-Agent Firewall Architecture for Privacy Protection of Sensitive Data in Interactions with Language Models](http://arxiv.org/abs/2607.08282v1)
  <details><summary>📄 Abstract</summary>
  While Large Language Models (LLMs) have become essential productivity tools, their integration into workflows without adequate safeguards creates significant risks. This paper proposes an open-source, privacy-focused, user-facing firewall designed to secure both web-based and programmatic LLM interactions. The architecture combines a browser extension and a proxy for total traffic interception across both HTTP(S) and WebSocket communications. At its core, a flexible multi-agent pipeline delivers...
  </details>

- **2026-07-09** — Corban Villa, Alp Eren Ozdarendeli, Sijun Tan et al. — [Prismata: Confining Cross-Site Prompt Injection in Web Agents](http://arxiv.org/abs/2607.08147v1)
  <details><summary>📄 Abstract</summary>
  Autonomous web agents promise to automate everyday browsing tasks, but inherit one of the web's oldest attack surfaces. Cross-Site Scripting proved that mixing trusted and untrusted content is dangerous, even on benign pages. Agents resurface this risk by interpreting natural language as instructions, allowing third-party and user-generated content to hijack the agent via prompt injection. The core challenge is that deriving a task-specific security policy requires reasoning over page structure ...
  </details>

- **2026-07-08** — Phat T. Tran-Truong, Xuan-Bach Le, Minh Nhat Nguyen — [FedMark-FM: Auditable, Risk-Adjusted Data Markets for Federated Foundation-Model Adaptation](http://arxiv.org/abs/2607.07529v1)
  <details><summary>📄 Abstract</summary>
  Federated foundation-model adaptation increasingly relies on heterogeneous private artifacts (retrieval corpora, prompts and demonstrations, LoRA adapters, preference and safety data, and update sketches), yet existing federated-learning incentive mechanisms price clients as homogeneous data or update providers. This assumption poorly matches foundation-model pipelines, where contribution value is heterogeneous, non-IID, pipeline-dependent, privacy-constrained, and vulnerable to strategic behavi...
  </details>

- **2026-07-08** — Aya Spira, Stav Cohen, Elad Feldman et al. — [Beware of Agentic Botnets: Scalable Untargeted Promptware Attacks via Universal and Transferable Adversarial HalluSquatting](http://arxiv.org/abs/2607.07433v1)
  <details><summary>📄 Abstract</summary>
  The growing adoption of agentic LLM applications has introduced a new threat previously named as promptware. While prior work has established that adversaries can exploit direct channels to LLM applications to apply promptware under weak threat models, many applications do not provide any direct channels that could be exploited for prompt injection beyond the Internet. This raises a question: can attackers exploit LLM applications at scale without any direct channels in practical threat models? ...
  </details>

- **2026-07-07** — Sandara Sathsarani Wijethunga, Muneeb Ul Hassan, Nasrin Sohrabi — [FDIFormer:Protocol-Aware Transformer Learning for False Data Injection Attack Detection in Smart Grid Networks](http://arxiv.org/abs/2607.06213v1)
  <details><summary>📄 Abstract</summary>
  Smart grids use communication networks and intelligent electronic devices for reliable, automated power system operation. As these systems become more interconnected, they are increasingly exposed to cyberattacks such as message tampering, false command injection, and denial-of-service attacks. A particularly concerning threat is False Data Injection (FDI), where attackers manipulate communication messages by deleting, modifying, or adding packets. This is especially critical in IEC 61850-based ...
  </details>

- **2026-07-06** — Kristina Nikolić, Egor Zverev, Javier Rando et al. — [Untrusted Content Masking for Web Agents with Security Guarantees](http://arxiv.org/abs/2607.05277v1)
  <details><summary>📄 Abstract</summary>
  Defenses that provide security guarantees against prompt injection attacks rely on strict isolation between trusted instructions and untrusted data. In text-based environments such as tool-use APIs, this separation arises naturally: agents can reason from interface definitions without ever processing untrusted content. Extending these guarantees to web agents faces a fundamental challenge: to perceive and interact with their environment, web agents must first observe the rendered page, which int...
  </details>

- **2026-07-06** — Yechao Zhang, Shiqian Zhao, Jiawen Zhang et al. — [When Claws Remember but Do Not Tell: Stealthy Memory Injection in Persistent Personal Agents](http://arxiv.org/abs/2607.05189v1)
  <details><summary>📄 Abstract</summary>
  Persistent personal agents combine long-term memory with access to users' external environments, enabling personalized foreground assistance and proactive background execution. This integration also creates a new path to compromise: untrusted external content can be silently written into persistent memory and later reused as trusted state. We study this threat as stealth memory injection, in which a remote black-box adversary delivers a single email payload that must induce the agent to write po...
  </details>

- **2026-07-06** — Woohyuk Choi, Juhee Kim, Taehyun Kang et al. — [Agent Data Injection Attacks are Realistic Threats to AI Agents](http://arxiv.org/abs/2607.05120v1)
  <details><summary>📄 Abstract</summary>
  AI agents act on behalf of user prompts, consuming external data and taking actions based on the agent context. Prior research on AI agent security has primarily focused on indirect prompt injection (IPI). Its most well-studied category is instruction injection, where attacker-controlled untrusted data is interpreted as an instruction. In response, many mitigations have been proposed to prevent instruction injection attacks. In this paper, we introduce a new category of IPI, agent data injection...
  </details>


### 📂 memory-poisoning
*记忆投毒与篡改 / Memory Poisoning & Tampering* — 2 papers

- **2026-07-06** — George Torres, Sharad Shrestha, Satyajayant Misra — [When Agents Remember Too Much: Memory Poisoning Attacks on Large Language Model Agents](http://arxiv.org/abs/2607.06595v1)
  <details><summary>📄 Abstract</summary>
  Personal AI agents powered by large language models can reason and act using available tools to access emails, manage calendars, and push code to remote repositories, all with minimal oversight. When augmented with long-term memory, an agent can recall specific details relevant to the current task, reducing the need for large context windows. Currently, long-term memory agents tend to fall into two distinct domains: conversational and action-planning agents. Personal assistant agents sit at the ...
  </details>

- **2026-07-06** — Neeraj Karamchandani, Piyush Nagasubramaniam, Sencun Zhu et al. — [Your Agent's Memories Are Not Its Own: Forged Reasoning Attacks on LLM Agent Memory and Defenses](http://arxiv.org/abs/2607.05029v1)
  <details><summary>📄 Abstract</summary>
  Persistent memory has enabled large language model (LLM) agents to store factual knowledge, prior decisions, reasoning histories, tool usage information, and context. While this has improved the agent's functionality and continuity across tasks, it has also introduced a new attack surface: the agent's own reasoning history. In this paper, we introduce the Forged Amplifying Rationale Memory Attack (FARMA), which poisons an agent's remembered reasoning rather than its factual knowledge. It inserts...
  </details>


### 📂 tool-use-attack
*工具使用攻击 / Tool-Use Attacks* — 2 papers

- **2026-07-07** — Yihua Liu — [Think Before You Grid-Search: Floor-First Triage for LLM Serving](http://arxiv.org/abs/2607.05876v2)
  <details><summary>📄 Abstract</summary>
  LLM serving optimization typically benchmarks many configurations and reaches for heavy profilers when latency targets are missed. We argue for the reverse discipline: estimation is the analytical layer of profiling -- without it, optimization degenerates to grid search. Floor First is a residual-driven triage workflow. Each decode step is modeled as a five-dimensional resource vector (HBM bytes, FLOPs, network bytes, network messages, KV capacity); summing within a resource and maximizing acros...
  </details>

- **2026-07-06** — Zhaoyu Bai, Jiaqi Cai — [PatchOptic for Shared-State LLM Workflows with Projected Views and Verified Structured Updates](http://arxiv.org/abs/2607.05483v1)
  <details><summary>📄 Abstract</summary>
  Agentic workflows often operate over shared, structured state. Because LLM context windows are limited, each model invocation is typically shown only the state fragment needed for the current workflow step, a pattern commonly known as progressive disclosure. Modern systems construct such model-facing views using grep-like keyword search, retrieval-augmented generation (RAG), abstract-syntax-tree (AST) queries, and task-specific agent skills. These methods make the read side manageable, but they ...
  </details>


### 📂 backdoor
*后门与投毒攻击 / Backdoor & Poisoning Attacks* — 5 papers

- **2026-07-09** — Zifan Zhang, Minghong Fang, Dianwei Chen et al. — [Securing Autonomous Vehicle Systems via Twin-Aware Federated Reinforcement Learning](http://arxiv.org/abs/2607.08137v1)
  <details><summary>📄 Abstract</summary>
  Federated reinforcement learning (FRL) is crucial for enabling collaborative learning across multiple agents without sharing raw data, thereby enhancing privacy and scalability in the decision-making process within dynamic vehicular environments. However, poisoning attacks pose a significant threat to the security and reliability of FRL-based systems, particularly in safety-critical autonomous driving, where this vulnerability remains largely unexplored. These attacks can compromise the global c...
  </details>

- **2026-07-09** — Anjun Gao, Yueyang Quan, Zhuqing Liu et al. — [Beware What You Autocomplete: Forensic Attribution of Backdoored Code Completions](http://arxiv.org/abs/2607.08011v1)
  <details><summary>📄 Abstract</summary>
  Large language models have enabled powerful code completion systems that assist developers by predicting subsequent lines of code. However, these models remain vulnerable to backdoor attacks, where malicious fine-tuning data covertly implants unsafe behaviors. Despite advances in defensive techniques, adaptive and sophisticated backdoor attacks still evade detection and mitigation. We present CodeTracer, a forensic framework that traces malicious code completions back to the backdoor fine-tuning...
  </details>

- **2026-07-08** — Oliver Makins, Orazio Angelini, Zohreh Shams et al. — [Multi-Agent AI Control: Distributed Attacks Hamper Per-Instance Monitors](http://arxiv.org/abs/2607.07368v1)
  <details><summary>📄 Abstract</summary>
  AI control is a family of techniques to prevent an AI with malicious goals from subverting its operator's intent. AI Control usually studies a single agent in one trajectory, but real deployments run many agents over shared infrastructure, and the most severe risks (model-weight exfiltration, training-run poisoning) plausibly need several agents acting in concert. We initiate the empirical study of multi-agent AI control, formalising distributed attacks in which several agents jointly aim for a ...
  </details>

- **2026-07-06** — Fabien Polly — [Learning Only What Valid Adapters Can Express: Subspace-Constrained Adaptation Against Fine-Tuning Poisoning](http://arxiv.org/abs/2607.05300v1)
  <details><summary>📄 Abstract</summary>
  Parameter-efficient fine-tuning still leaves a broad space of behavior-changing updates reachable, so a poisoned objective can be represented and optimized. We study an alternative: adaptation constrained to the subspace estimated from a trusted pool of existing task adapters. On flan-t5-large with 196 public LoRA adapters, we show that (1) the functionally relevant content of an adapter lies in a low-dimensional shared subspace, 30 to 38 percent of its weight norm being redundant under the eval...
  </details>

- **2026-07-06** — Yue Pan, Ziheng Zhang, Junxiang Lei et al. — [FORGE: Research-Trajectory Hijacking Attacks on Deep Research Agents](http://arxiv.org/abs/2607.04718v1)
  <details><summary>📄 Abstract</summary>
  Deep research agents decompose open-ended queries into subtasks, retrieve web evidence over multiple rounds, and synthesize long-form reports. This workflow creates a planning-layer poisoning surface: adversarial documents that enter the retrieval pool can steer follow-up questions and turn a local injection into report-level contamination. We present FORGE (Fabricated Orchestrated Reasoning chain for aGent Exploitation), a two-level attack that combines intra-document reasoning fabrication with...
  </details>


### 📂 adversarial-attack
*对抗攻击 / Adversarial Attacks* — 5 papers

- **2026-07-09** — Eugene Ng Yi Sheng, Bingquan Shen — [Formal Mechanisms for Market Stability in Self-Interested Agent Societies: A Marketplace Simulation Study](http://arxiv.org/abs/2607.08652v1)
  <details><summary>📄 Abstract</summary>
  Self-interested agents, left unconstrained, tend toward defection in repeated social dilemmas, causing cooperative gains from trade to collapse. This paper investigates what formal mechanisms, layered on top of unrestricted communication, are sufficient for a society of such agents to maintain market stability, and how resilient those mechanisms are to adversarial attack. We instantiate the research question as a multi-agent marketplace simulation where 18 LLM agents (DeepSeek-V3) with complemen...
  </details>

- **2026-07-08** — Giulia Marchiori Pietrosanti, Giulio Rossolini, Giorgio Buttazzo — [Adversarial Decoys: Misdirecting Attention-Based Defenses in ViT](http://arxiv.org/abs/2607.07922v1)
  <details><summary>📄 Abstract</summary>
  Vision Transformers (ViTs) remain vulnerable to localized adversarial attacks, e.g., adversarial patches, while recent test-time defenses mitigate them by suppressing image tokens with abnormally high attention scores. These defenses exploit a strong coupling between attention and adversarial effectiveness: adversarial tokens often need to attract substantial attention to influence the prediction. We introduce adversarial decoys, independently optimized image patches that redirect the attention,...
  </details>

- **2026-07-08** — Zhenpeng Li — [Controllability-Aware Adversarial Examples Against LLM-Based Network Traffic Classifiers](http://arxiv.org/abs/2607.07739v1)
  <details><summary>📄 Abstract</summary>
  Large language models (LLMs) are increasingly explored as network intrusion detection classifiers, but their adversarial robustness under realistic attacker constraints remains unclear. We present a controllability-aware black-box transfer framework for LLM-based network traffic classifiers. The framework partitions flow features into directly controllable (DC), indirectly controllable (IC), and uncontrollable (UC) groups according to network communication semantics, then restricts perturbations...
  </details>

- **2026-07-08** — Xifeng Zhang, Tao Hu, Yijie Peng et al. — [A Unified Detection Framework for AI-Related Content and Artifacts](http://arxiv.org/abs/2607.07527v1)
  <details><summary>📄 Abstract</summary>
  Artificial intelligence (AI) is a double-edged sword: while it has achieved remarkable success across a wide range of domains, its deployment also calls for effective oversight and regulation, for which the detection of AI-related content and artifacts is perhaps the most direct and cost-effective approach. To this end, we propose a unified detection framework based on Mahalanobis distance scores (MDS), applicable to several important settings, including the detection of large language model (LL...
  </details>

- **2026-07-07** — Cong Su, Jiaju Han, Xuemeng Sun et al. — [AirflowAttack: Thermal-Airflow Adversarial Perturbations against Infrared Remote-Sensing Vision-Language Models](http://arxiv.org/abs/2607.06485v1)
  <details><summary>📄 Abstract</summary>
  Vision-language models (VLMs) are increasingly deployed on infrared (IR) remote sensing imagery in security-critical settings, yet their adversarial robustness remains unexamined. We present AirflowAttack, to our knowledge the first adversarial attack for IR remote-sensing VLMs and the first to weaponize thermal-airflow turbulence as the perturbation prior. A lightweight generator synthesizes a single input-agnostic perturbation regularized toward physically plausible airflow patterns. Optimized...
  </details>


### 📂 privacy-leakage
*隐私泄露 / Privacy Leakage* — 30 papers

- **2026-07-09** — Shashi Kumar, Yanis Labrak, Hasindri Watawana et al. — [When Synthetic Speech Is All You Have: Better Call GRPO](http://arxiv.org/abs/2607.08409v1)
  <details><summary>📄 Abstract</summary>
  LLM-based ASR adapted to regulated domains such as banking is bottlenecked by privacy: real speech is costly and legally constrained to collect, making synthetic text-to-speech (TTS) an attractive substitute. Yet synthetic speech stays acoustically mismatched with real recordings, and work on this gap has stayed within supervised fine-tuning (SFT). We instead turn to reinforcement learning, and show that Group Relative Policy Optimization (GRPO) extracts far more from the same synthetic speech t...
  </details>

- **2026-07-09** — Victor Jüttner, Xenia Wagner, Christoph Jahn et al. — [Simulating the Resident: Generating Executable Smart Home Schedules via LLM Personas](http://arxiv.org/abs/2607.08231v1)
  <details><summary>📄 Abstract</summary>
  Smart homes have emerged as an important domain for HCI research, including work on usable security and privacy. Ideally, studies in these areas draw on datasets collected in real homes with real residents, capturing authentic device interactions, network traffic, and daily routines. However, creating such datasets is slow, expensive, and raises significant privacy concerns, as it requires long-term observation of people in their most private spaces. We propose using LLMs to generate diverse res...
  </details>

- **2026-07-09** — Joongho Ahn, Moonsoo Kim — [From Prompts to Contracts: Harness Engineering for Auditable Enterprise LLM Agents](http://arxiv.org/abs/2607.08028v1)
  <details><summary>📄 Abstract</summary>
  Enterprise large language model (LLM) applications often begin as prototypes whose behavior is carried by prompts and retrieval context. Productization adds requirements for source boundaries, entity routing, answer contracts, and reproducible traces. We present a harness-engineering approach that reconstructs this pattern into a traceable, auditable LLM-agent architecture: deterministic behavior moves into code, manifests, schemas, and validation artifacts around a replaceable composition bound...
  </details>

- **2026-07-09** — Vikash Sathiamoorthy, Shuo Huai, Hao Kong et al. — [FedTR: Federated Learning Framework with Transfer Learning for Industrial Visual Inspection](http://arxiv.org/abs/2607.08014v1)
  <details><summary>📄 Abstract</summary>
  Federated learning (FL) is a collaborative learning scheme to train deep learning models, where collaborating parties can consolidate their models without sharing local data with other parties, hence preserving data privacy. Nevertheless, when implementing FL in Industrial visual inspection (IVI), the constraints posed by limited data availability and the intricate nature of the inspection tasks significantly impact the performance of the resulting model. This paper introduces FedTR, a novel FL ...
  </details>

- **2026-07-08** — Jonathan Katzy, Ali Al-Kaswan, Razvan Mihai Popescu et al. — [The Poisoned Chalice of LLM Evaluation Report](http://arxiv.org/abs/2607.07481v1)
  <details><summary>📄 Abstract</summary>
  Large language models are increasingly used to evaluate and support software engineering tasks, yet the validity of these evaluations is often undermined by uncertainty about whether benchmark instances were seen during pretraining. This can lead to data contamination, which may inflate performance and result in misleading conclusions about model capability. Despite this, the training corpora of many modern models are only partially disclosed, making direct decontamination infeasible. This creat...
  </details>

- **2026-07-08** — Kiarash Ahi, Saeed Valizadeh — [Large Language Models (LLMs) and Generative AI in Cybersecurity and Privacy: A Survey of Dual-Use Risks, AI-Generated Malware, Explainability, and Defensive Strategies](http://arxiv.org/abs/2607.06963v1)
  <details><summary>📄 Abstract</summary>
  Large Language Models (LLMs) and generative AI (GenAI) systems, such as ChatGPT, Claude, Gemini, LLaMA, Copilot, Stable Diffusion by OpenAI, Anthropic, Google, Meta, Microsoft, Stability AI, respectively, are revolutionizing cybersecurity, enabling both automated defense and sophisticated attacks. These technologies power real-time threat detection, phishing defense, secure code generation, and vulnerability exploitation at unprecedented scales. Following a rapid surge where LLM-generated malwar...
  </details>

- **2026-07-08** — Wei-Jung Huang — [Do LLM-Generated Skills Make Better AI Data Scientists? A Component Ablation Across Data-Science Workflows](http://arxiv.org/abs/2607.07504v1)
  <details><summary>📄 Abstract</summary>
  Product data scientists often ask LLM-based agents to help with recurring execution tasks such as cleaning data, writing SQL, choosing statistical tests, and formatting results. Reusable skill files are meant to avoid prompting from scratch by packaging guidance for a task family. Expert-written skills can encode high-quality guidance, but writing and maintaining them across many data-science task families creates a manual bottleneck. We ask whether LLM-generated skills offer a useful low-curati...
  </details>

- **2026-07-08** — Athanasios Zeris — [FourierQK: Spectral Preprocessing of Query-Key Projections Improves Transformer Attention](http://arxiv.org/abs/2607.07478v1)
  <details><summary>📄 Abstract</summary>
  FFT-based spectral preprocessing of learned query-key (Q/K) projections substantially improves transformer attention on character-level language modelling. On TinyShakespeare: a fixed random spectral filter achieves val=1.031 (Delta=+0.443); a single learned frequency at paragraph scale achieves val=0.608 (Delta=+0.867); and four learned frequencies spanning paragraph to word scale achieve val=0.309 (Delta=+1.166), a 79% reduction over standard dot-product attention. The single-frequency result ...
  </details>

- **2026-07-08** — Jin-Kang Guo, Jin-Lei Wu, Chuan-Cun Shu — [Non-Abelian Thouless pumping based on the global adiabatic criterion in Rydberg synthetic lattices](http://arxiv.org/abs/2607.07223v1)
  <details><summary>📄 Abstract</summary>
  We study a quantum implementation of non-Abelian Thouless pumping in Lieb lattices using Rydberg synthetic dimensions. The lattice is encoded in twelve selected microwave-coupled Rydberg levels, forming a three-cell structure with six degenerate zero-energy states. These zero-energy states define the working subspace for cyclic modulation of the microwave couplings, while the remaining bright states provide the dominant leakage channels at finite evolution time. To choose the relative timing of ...
  </details>

- **2026-07-08** — Chanwoo Cho, Wooseok Kim, Yonglak Son et al. — [Voltron: Enabling Elastic Multi-Device Execution of LLM Inference for Empowered Edge Intelligence](http://arxiv.org/abs/2607.07046v1)
  <details><summary>📄 Abstract</summary>
  Large language models (LLMs) are widely used in intelligent services due to their remarkable capability in generative tasks. Typically, LLM-based services process the inference requests of the users in a centralized data center. Unfortunately, such centralized execution has limitations for end-users, such as increased response latency with communication overhead and privacy leakage risk. To alleviate the aforementioned limitations, there have been increasing pushes to execute LLM inference local...
  </details>

- **2026-07-08** — Zhenghuang Wu, Yuyao Zhu, Songlin Xu — [Physical activities enable scalable foundation modelling for broad-spectrum health prediction](http://arxiv.org/abs/2607.06954v1)
  <details><summary>📄 Abstract</summary>
  Wearable and mobile sensing technologies have demonstrated strong potential for health inference; however, most sensor models are designed for specific disease types, limiting their transferability across different health risks. Wearable foundation models offer a more generalizable approach in diverse health risk types. Nevertheless, most existing methods rely on high-frequency raw sensor data, raising concerns about privacy, computational overhead, and scalability across devices and populations...
  </details>

- **2026-07-07** — Tamara Wit, Lifeng Han, Carly Heipon et al. — [Measuring the practice of shared-decision making (OPTION12): An Investigation into Open-sourced Smaller LLMs (OS-sLLMs) for Better Privacy and Sustainability](http://arxiv.org/abs/2607.06127v2)
  <details><summary>📄 Abstract</summary>
  We present LLM4SDM, the first study of open-source smaller language models (OS-sLLMs) for automated assessment of shared decision making (SDM) using the Observer OPTION12 framework. Unlike previous work that relies on large commercial models and the shorter OPTION5 instrument, our study focuses on privacy-preserving locally deployable models and Dutch melanoma consultation transcripts. Using expert-annotated clinical consultations, we evaluate three general-domain and two medical-domain OS-sLLMs...
  </details>

- **2026-07-07** — Barkha Rani — [Behavioral Privacy Leakage in Agentic Negotiation: Formalizing and Mitigating Inference Attacks via Randomized Policies](http://arxiv.org/abs/2607.06815v1)
  <details><summary>📄 Abstract</summary>
  Autonomous negotiation agents are increasingly deployed in high-stakes settings such as insurance and procurement. While cryptographic techniques protect explicitly disclosed constraint values, they fail to address a subtler threat: behavioral privacy leakage, where an adversary infers private constraints from observable negotiation dynamics such as concession trajectories, timing, and convergence patterns. This paper investigates behavioral differential privacy in multi-round negotiation protoc...
  </details>

- **2026-07-07** — Zhangheng LI, Jianing Zhu, Junyuan Hong et al. — [POPS: Recovering Unlearned Multi-Modality Knowledge in MLLMs with Prompt-Optimized Parameter Shaking](http://arxiv.org/abs/2607.06649v1)
  <details><summary>📄 Abstract</summary>
  Multimodal Large Language Models (MLLMs) have demonstrated impressive performance on cross-modal tasks by jointly training on large-scale textual and visual data, where privacy-sensitive examples could be unintentionally encoded, raising concerns about privacy or copyright violation. To this end, Multi-modality Machine Unlearning (MMU) was proposed as a mitigation that can effectively force MLLMs to forget private information. However, the robustness of such unlearning methods is not fully explo...
  </details>

- **2026-07-07** — Byunghoon Oh, Sunghwan Park, Jaewoo Lee — [Unlearnable Faces: Privacy Protection Surviving Extraction Pipeline](http://arxiv.org/abs/2607.05996v1)
  <details><summary>📄 Abstract</summary>
  Unlearnable examples keep publicly shared photos from being learned by unauthorized face-recognition models. An imperceptible perturbation, added before sharing, makes any model trained on the protected photos fail on clean faces. The perturbation is crafted on the shared image, however the attacker trains on the face it extracts, cropped and resized to the recognizer input, and under this extraction the protection collapses. We propose LPID, which builds the extraction into the unlearnable-exam...
  </details>

- **2026-07-07** — Peiheng Zhang, Yuejun Liu, Wei Cheng et al. — [From Regression to Prior-Aware Inference: Solving the ILWE Family in Randomness Leakage Attacks against ML-DSA](http://arxiv.org/abs/2607.05921v1)
  <details><summary>📄 Abstract</summary>
  ML-DSA is a representative lattice-based signature scheme standardized by NIST. It relies on signing randomness and rejection sampling to ensure that released signatures are statistically independent of the secret key. Practical implementations, however, may leak partial information about this randomness, and such leakage can transform public signatures into ILWE-type problems, resulting in secret key disclosure risks.   Such randomness leakage attack can be formulated as a two-stage key-recover...
  </details>

- **2026-07-07** — Sahasrajit Sarmasarkar, Anastasia Koloskova, Sanmi Koyejo — [Auditing of Unlearning Algorithms](http://arxiv.org/abs/2607.05898v1)
  <details><summary>📄 Abstract</summary>
  Evaluating whether unlearning algorithms truly remove training data influence remains an open challenge. We propose a practical auditor that computes data-dependent lower bounds on the unlearning parameter $\varepsilon$ using membership inference attacks. Evaluating multiple unlearning algorithms, we find a sharp separation: algorithms with rigorous guarantees, such as model clipping and rewind-to-delete, achieve very small $\varepsilon$ bounds that do not falsify their unlearning guarantees, wh...
  </details>

- **2026-07-07** — Andrew Fishberg, Yixuan Jia, Jonathan P. How — [CILC: Cryptographically-secure Inter-agent Loop Closure Candidate Detection for Multi-Agent Collaborative SLAM](http://arxiv.org/abs/2607.06700v1)
  <details><summary>📄 Abstract</summary>
  Multi-agent Simultaneous Localization and Mapping (SLAM) and collaborative SLAM (CSLAM) require robots to continuously exchange global descriptors (GDs) to detect inter-agent loop closures (ILCs). While encrypted radios protect this traffic from external eavesdroppers, they offer no protection against a compromised swarm member. We show this threat is concrete by demonstrating how a corrupted agent can reconstruct approximations of an honest agent's imagery and trajectory from its public GD broa...
  </details>

- **2026-07-07** — Jiaju Han, Ma Yaqi, Yahui Chai et al. — [MonoIR-RS: Infrared Remote Sensing Vision-Language Learning with CLIP and VLM Adaptation](http://arxiv.org/abs/2607.06552v1)
  <details><summary>📄 Abstract</summary>
  Infrared remote-sensing imagery captures intensity structure, object-background contrast, and illumination-invariant cues often invisible in RGB imagery. Yet, most remote-sensing vision-language resources and models focus on visible-band semantics, leaving infrared vision-language understanding underexplored. We introduce MonoIR-RS, a large-scale infrared remote-sensing vision-language dataset and benchmark that couples IR-aware data construction with CLIP-style contrastive adaptation and VLM in...
  </details>

- **2026-07-07** — Jabari Kwesi, Jiaxun Cao, Hailee Cunningham et al. — [The Impact of Security and Privacy Controls on Users' Emotional Engagement with Generative AI Chatbots](http://arxiv.org/abs/2607.06371v1)
  <details><summary>📄 Abstract</summary>
  Chatbots powered by generative AI (e.g., OpenAI's ChatGPT and Google's Gemini) are increasingly being appropriated for emotional support and companionship. These tools offer a suite of security and privacy (S&P) controls, including model training opt-outs and memory toggles, yet how the presence of these controls influences users' attitudes toward emotionally sensitive disclosure remains understudied. We conducted a mixed-methods vignette study with 354 U.S. participants to examine how S&P contr...
  </details>

- **2026-07-07** — Adam Jenkins, Agnieszka Kitkowska, Caterina Maidhof et al. — [Security and Privacy in Agentic AI: Grand Challenges and Future Directions](http://arxiv.org/abs/2607.06608v1)
  <details><summary>📄 Abstract</summary>
  We present key challenges and future research directions in the security and privacy of agentic AI, based on a horizon-scanning exercise that brought together thirty leading international experts from academia, industry, and government to engage in focused discussions and collaborative exercises on the emerging risks associated with the growing agency of AI.
  </details>

- **2026-07-07** — Mayur Kurup, Hyunjae Suh, Swathi Vaidyanathan et al. — [Deployment Risk Assessment Using Diff-Aware Features: A Case Study at Prime Video](http://arxiv.org/abs/2607.06766v1)
  <details><summary>📄 Abstract</summary>
  At Amazon Prime Video, we face the critical operational challenge of managing code deployments during live events and rapid feature releases without causing service outages. Current change control approaches use blanket deployment freezes that block all changes regardless of risk, creating significant developer toil. While prior research has explored risky change predictors, these rely on developer-specific metadata or extensive historical data, raising privacy concerns and limiting applicabilit...
  </details>

- **2026-07-07** — Tamara Wit, Lifeng Han, Carly Heipon et al. — [Measuring the practice of shared-decision making (OPTION12): An Investigation into Open-sourced Smaller LLMs (OS-sLLMs) for Better Privacy and Sustainability](http://arxiv.org/abs/2607.06127v1)
  <details><summary>📄 Abstract</summary>
  We present LLM4SDM, the first study of open-source smaller language models (OS-sLLMs) for automated assessment of shared decision making (SDM) using the Observer OPTION12 framework. Unlike previous work that relies on large commercial models and the shorter OPTION5 instrument, our study focuses on privacy-preserving locally deployable models and Dutch melanoma consultation transcripts. Using expert-annotated clinical consultations, we evaluate three general-domain and two medical-domain OS-sLLMs...
  </details>

- **2026-07-07** — Taerin Ki, Sunghwan Park, Junyoung Park et al. — [REAN: Reconstruction-aware ECG Anonymization Based on Privacy--Utility Orthogonality](http://arxiv.org/abs/2607.06037v1)
  <details><summary>📄 Abstract</summary>
  A shared electrocardiogram (ECG) is itself a biometric fingerprint that can re-identify a patient and reveal personal information. Recent ECG anonymizers transform the signal before sharing to reduce privacy leakage. However, existing methods still face a privacy--utility trade-off, in which preserving privacy often compromises utility while preserving utility reveals personal information. We propose \emph{REAN} (\emph{RE}construction-aware ECG \emph{AN}onymizer), a raw ECG signal anonymizer, to...
  </details>

- **2026-07-07** — Jurn-Gyu Park, Sanzhar Zholdybayev, Aidar Amangeldi et al. — [Energy-Efficient GPU DVFS for Fine-Tuning of SLMs on Resource-constrained Embedded Devices](http://arxiv.org/abs/2607.05933v1)
  <details><summary>📄 Abstract</summary>
  Dynamic Voltage Frequency Scaling (DVFS) on resource-constrained embedded GPU platforms is essential for energy-efficient small language model (SLM) fine-tuning, as privacy- and personalization-driven adaptation increasingly requires local execution and involves repeated forward-backward optimization over many mini-batches, making it substantially more time- and energy-intensive than single-pass inference. To this end, 1) we first characterize the fine-tuning behavior of representative encoder-o...
  </details>

- **2026-07-07** — Muhammad Assad Shehbaz, Carlos Francisco Moreno-García — [Structured Data Extraction from Real Estate Documents using Clustering, Classification, and Large Language Models](http://arxiv.org/abs/2607.06012v1)
  <details><summary>📄 Abstract</summary>
  Real estate property listings expose structured metadata through the API. Still, the richest property-level information (i.e., legal status, structural condition, utility supplies, heating systems) sits in attached questionnaire documents that no automated system currently processes at scale. These documents are heterogeneous. Some are digitally generated with selectable text, others are scanned physical forms. There are even more complex layouts that contain checkbox annotations that defeat con...
  </details>

- **2026-07-06** — H. Chad Lane, Bryson Kageler — [CSTutorBench: Benchmarking Small Language Models as Tutors for Block-Based Programming](http://arxiv.org/abs/2607.05571v1)
  <details><summary>📄 Abstract</summary>
  Large language models are increasingly explored as AI tutors, yet deploying them in K-12 settings raises concerns around privacy, cost, and reliance on proprietary models. Small language models (SLMs) offer a promising alternative, but selecting the right model for a specific educational context remains difficult, particularly when the target domain, such as block-based programming, is largely absent from model training data. We introduce CSTutorBench, a benchmark for evaluating language models ...
  </details>

- **2026-07-06** — Guanyu Cai, Ruiming Tian, Lang Yang et al. — [Is Your NPU Ready for LLMs? Dissecting the Hidden Efficiency Bottlenecks in Mobile LLM Inference](http://arxiv.org/abs/2607.05475v1)
  <details><summary>📄 Abstract</summary>
  Deploying Large Language Models (LLMs) on mobile devices enhances privacy and reduces latency, but is severely bottlenecked by hardware inefficiency. We present the first comprehensive, cross-layer measurement study of mobile LLM inference, uniquely spanning five mainstream frameworks (e.g., llama.cpp, GENIE) and three hardware backends (CPU, GPU, NPU). To enable this analysis, we develop PowerBench, a fine-grained profiling tool that provides the first backend-specific energy attribution, movin...
  </details>

- **2026-07-06** — Dylan Zongmin Liu — [SovereignPA-Bench: Evaluating User-Owned Personal Agents under Evolving Intent, Platform Mediation, and Consent Constraints](http://arxiv.org/abs/2607.05363v1)
  <details><summary>📄 Abstract</summary>
  Personal agents are becoming persistent user-owned intermediaries: they remember preferences, filter platform-mediated information, use tools, and negotiate with services. Existing benchmarks evaluate tool use, web navigation, desktop control, personalization, recommendation, and evolving context, but rarely ask whether an agent preserves user sovereignty: advancing the user's current interests while respecting privacy, consent, evidence, user burden, and resistance to manipulative incentives. W...
  </details>

- **2026-07-06** — Xuyang Chen, Xiang Li, Yangxinyu Xie et al. — [Selective Disclosure Watermarking for Large Language Models](http://arxiv.org/abs/2607.05353v1)
  <details><summary>📄 Abstract</summary>
  Watermarking methods embed imperceptible and verifiable signals into text generated by large language models (LLMs). Existing approaches include zero-bit schemes for distinguishing synthetic text from human writing and multi-bit schemes for embedding metadata. However, current multi-bit watermarking methods do not allow selective disclosure: verifying any part of the watermark requires revealing the entire embedded message. This lack of control leads to unnecessary information exposure and raise...
  </details>


### 📂 steganography
*隐写与隐蔽通信 / Steganography & Covert Communication* — 1 papers

- **2026-07-07** — Yige Wang, Shiqi Yi, Hanzhou Wu — [Code-Level Cost Function Generation for Spatial Image Steganography Using RAG-Enhanced Large Language Models](http://arxiv.org/abs/2607.05868v1)
  <details><summary>📄 Abstract</summary>
  Designing cost functions of adaptive steganography traditionally requires extensive manual tuning, while deep learning methods lack interpretability. Although large language models (LLMs) offer an automated alternative via evolutionary generation, they often violate domain specific mathematical constraints due to a lack of explicit domain knowledge. To address this problem, we propose a novel evolutionary system focused on exploiting Retrieval-Augmented Generation (RAG) enhanced LLMs for the aut...
  </details>


### 📂 misuse
*滥用与误用 / Misuse & Abuse* — 12 papers

- **2026-07-09** — Kutub Uddin, Nusrat Tasnim, Awais Khan et al. — [Do Transformations Reveal the Truth? Generative Residual Learning for Generalized AI-Generated Image Detection](http://arxiv.org/abs/2607.08674v1)
  <details><summary>📄 Abstract</summary>
  The rapid advancement of generative AI has enabled the creation of highly realistic deepfake media, posing significant threats, including misinformation, digital identity theft, fraud, and manipulation of public opinion. AI-generated image (AIGI) detection is reliably challenging due to the diversity of generative methods and the subtle artifacts they leave behind. In this work, we propose GenRes, a novel framework for generative residual learning via a neural tensor network, which models fine-g...
  </details>

- **2026-07-08** — Syed Usama Imtiaz, Mitra Nasr Azadani, Nasrin Alamdari — [Scalable and Trustworthy Earth Observation Foundation Models](http://arxiv.org/abs/2607.07758v1)
  <details><summary>📄 Abstract</summary>
  Foundation models (FMs) have transformed machine learning from isolated task-specific model development toward general-purpose models pretrained on broad data and adapted to multiple downstream tasks. Earth observation (EO) is an important domain for this paradigm because satellite and airborne archives are large, high-revisit, and increasingly multimodal, while reliable field labels are often sparse. Remote sensing foundation models (RSFMs) cannot be transferred reliably/optimally without domai...
  </details>

- **2026-07-08** — Zikai Alex Wen, Corrazon Ogot, Juan Li et al. — [Forensic Schema for Psychological Manipulation in Cyber Fraud: LLM-Driven Victim Reports Analysis](http://arxiv.org/abs/2607.07751v1)
  <details><summary>📄 Abstract</summary>
  Existing cybercrime classification schemas capture contact metadata and financial transactions but omit the psychological manipulation techniques perpetrators employ. We present a forensic schema (four categories, 35 questions) adding 11 manipulation indicators and cryptocurrency evidence fields to established forensic foundations. Applied to 10,994 victim reports via large language model (LLM)-driven annotation and validated against two human annotators (mean LLM-human $κ= 0.69$, matching inter...
  </details>

- **2026-07-08** — Harry Owiredu-Ashley — [Beyond Attack-Success Rate: Action-Graded Severity Scale for Tool-Using AI Agents](http://arxiv.org/abs/2607.07474v1)
  <details><summary>📄 Abstract</summary>
  Agentic red-teaming benchmarks report whether an injected agent was compromised as a single bit: the attack succeeded, or it did not. We argue that this binary attack-success rate discards the information a defender most needs, namely how harmful the resulting action was. We introduce an action-graded harm rubric that scores an agent's tool-call trajectory on a seven-level ordinal scale (L0 to L6) according to whether the executed action was reversible, whether it crossed scope to reach another ...
  </details>

- **2026-07-08** — Lifei Liu, Haoran Yu, Xiaochong Jiang et al. — [Operational Reframing and Approval-Framed Delegation in Multi-Agent LLM Safety](http://arxiv.org/abs/2607.07097v1)
  <details><summary>📄 Abstract</summary>
  Safety evaluations of multi-agent LLM systems often compare a direct prompt with a planner-executor pipeline and report the difference as a single "pipeline effect." We argue that this aggregate is difficult to interpret because it conflates three mechanisms: harmful intent may be reframed as plausible operational work, the planner may refuse or transform the request, and the executor may act under delegation prompts implying prior approval. To separate these factors, we introduce a five-conditi...
  </details>

- **2026-07-08** — Tomohiro Okatsu, Naoki Takada, Yin Min Pa Pa et al. — [Understanding Interpretation Difficulty in Harmful Online Communication: Insights from Cybercrime Communities](http://arxiv.org/abs/2607.07277v1)
  <details><summary>📄 Abstract</summary>
  Harmful online communication often contains slang, coded terms, abbreviations, and community-specific expressions, which make messages difficult to interpret. This paper presents an exploratory study of interpretation difficulty in Discord chats related to cybercrime. We construct reference interpretations of purposefully selected difficult messages, which were reviewed by an expert. We then use them to evaluate human and large language model (LLM) interpretations under different context conditi...
  </details>

- **2026-07-07** — Soohyeon Choi, Debin Gao, Yue Duan — [Multi-Channel Spread-Spectrum Code Watermarking](http://arxiv.org/abs/2607.06009v1)
  <details><summary>📄 Abstract</summary>
  Attributing code to the large language model that produced it is essential for provenance, licensing, and misuse accountability, yet no deployed watermark meets this need. Generation-time schemes require access to the producing model and cannot be applied to third-party code, while post-hoc schemes work on any code but carry at most 4 bits of payload, far too few to distinguish the many deployed model configurations. We present multi-channel spread-spectrum watermarking, the first post-hoc, trai...
  </details>

- **2026-07-07** — Mingchen Li, Meikang Qiu, Zifan Peng et al. — [Beyond Refusal: A Same-Lineage Study of Aligned and Abliterated LLMs for Vulnerability Analysis](http://arxiv.org/abs/2607.05842v1)
  <details><summary>📄 Abstract</summary>
  Large language model (LLM)-assisted software security operates at a difficult boundary: the vulnerability-analysis terminology needed for legitimate code review, triage, and repair can closely resemble terminology associated with misuse. Existing safety and cybersecurity evaluations are difficult to interpret in this setting because they often compare unrelated model families, thereby conflating safety behavior with differences in architecture, scale, training data, and deployment. To isolate th...
  </details>

- **2026-07-06** — Kabir Dev Paul Baghel, Radu Timofte, Dmitry Ignatov — [LLM-Driven Neural Network Generation with Same-Family Architecture Guidance: Disentangling Transfer and Adaptation](http://arxiv.org/abs/2607.05704v1)
  <details><summary>📄 Abstract</summary>
  Large language models (LLMs) can generate neural-network modifications, but unrestricted generation is often invalid or harmful. This paper studies a narrower setting: improving a weak target model using a stronger same-family source model from a neural-network database. We propose a source-guided candidate-generation protocol with non-source controls, source-conditioned candidates, and a no-LLM hp_copy ablation under equal evaluation budgets. The protocol reports validity separately from accura...
  </details>

- **2026-07-06** — Yibo Hu, Jiaming Qu — [Most LLM Conformity Needs No Speaker: Measuring the Speaker-Free Floor in Peer-Pressure Benchmarks](http://arxiv.org/abs/2607.05545v1)
  <details><summary>📄 Abstract</summary>
  LLM conformity is often used to describe cases where a model changes a correct answer toward a peer or group response. We show that most of this apparent conformity survives even after the peer is removed. The reason is a confound: standard conformity prompts mix two cues at once, the presence of a speaker and the repeated wrong answer itself. Existing benchmarks vary these cues together, so they cannot tell how much of the revision actually depends on the speaker. We introduce a no-source condi...
  </details>

- **2026-07-06** — Samira Hajizadeh — [Retroactive Chain-of-Thought (RetroCoT): Forensic Reconstruction Prompts as a Safety Diagnostic Across Model Generations](http://arxiv.org/abs/2607.04645v1)
  <details><summary>📄 Abstract</summary>
  Safety alignment in large language models is typically evaluated against direct, imperative harmful requests. We show that this alignment is highly conditioned on pragmatic register: models that refuse a direct request frequently comply when the same underlying objective is expressed through a different communicative stance. This suggests that current alignment policies are not invariant to semantic equivalence, but remain sensitive to how a request is pragmatically framed. We introduce Retroact...
  </details>

- **2026-07-06** — Ananth Eswar, Pratinav Seth, Utsav Avaiya et al. — [Faithfulness to Refusal: A Causal Audit of Neuron Selectors](http://arxiv.org/abs/2607.05355v1)
  <details><summary>📄 Abstract</summary>
  Attribution scores increasingly identify which neuron rows of a language model matter for applications such as pruning, interpretability, and editing for safety, yet whether they identify causally important rows is rarely tested directly. We address this with two paired audits built on one-shot neuron-row zeroing. We first audit selectors at the language-modeling level: attribution methods substantially outperform activation and magnitude-based baselines at identifying dispensable rows across fi...
  </details>


### 📂 red-teaming
*红队测试 / Red Teaming* — 1 papers

- **2026-07-08** — Yujiao Chen — [Institutional Red-Teaming: Deployment Rules, Not Just Models, Causally Shape Multi-Agent AI Safety](http://arxiv.org/abs/2607.07695v1)
  <details><summary>📄 Abstract</summary>
  We introduce institutional red-teaming, an evaluation methodology for testing deployment rules in multi-agent AI: hold the agents, objectives, and task state fixed, vary only one rule, and attribute the resulting change in collective behavior to that rule. We instantiate the methodology in IABench-CA, a consequence-allocation benchmark spanning 228 contexts, five canonical rules, and seven model populations (33,924 games), with a normative cooperative reference and auto-labelled reasoning traces...
  </details>


### 📂 vulnerability
*漏洞与攻击面 / Vulnerabilities & Attack Surfaces* — 61 papers

- **2026-07-09** — Shilin Ou, Yifan Xu, Luyao Zhang — [SolarChain-Eval: A Physics-Constrained Benchmark for Trustworthy Economic Agents in Decentralized Energy Markets](http://arxiv.org/abs/2607.08681v1)
  <details><summary>📄 Abstract</summary>
  As agentic AI systems are increasingly applied to cyber-physical environments, their evaluation requires assessment of both task performance and trustworthiness. In decentralized energy markets, autonomous agents may improve market utility, but may also exploit invalid physical data, create artificial liquidity, and produce unstable governance decisions. Therefore, we propose SolarChain-Eval, a physics-constrained benchmark for evaluating trustworthy economic agents. It formulates market governa...
  </details>

- **2026-07-09** — Seyyed Erfan Fatemi, Wafa Hedhly, Leila Musavian et al. — [Adaptive Wavelet Division Multiplexing for Heterogeneous Mobility Users](http://arxiv.org/abs/2607.08611v1)
  <details><summary>📄 Abstract</summary>
  This paper proposes an adaptive wavelet division multiplexing scheme for wireless systems serving users with heterogeneous mobility profiles over frequency-selective Rayleigh fading channels. By exploiting the multiresolution structure of the discrete wavelet transform (DWT), users are adaptively assigned to different decomposition levels according to their channel dynamics and Doppler conditions. A single-tap minimum mean square error (MMSE) equalizer is applied in the frequency domain, and the...
  </details>

- **2026-07-09** — Masatoshi Tateno, Alexandros Stergiou, Risa Shinoda et al. — [Do Egocentric Video-Language Models Capture Both Hand- and Object-Centric Cues?](http://arxiv.org/abs/2607.08514v1)
  <details><summary>📄 Abstract</summary>
  Hand-object interaction (HOI) recognition requires capturing both hand manipulations and object transformations. However, existing video-language models often fall into shortcuts by relying on spurious correlations among hands, objects, or environmental context, rather than reasoning from the appearance and dynamics of hands and objects themselves. To address this limitation, we propose a new learning paradigm that combines (i) hand-object masked training, which enables robust reasoning from par...
  </details>

- **2026-07-09** — Puji Wang, Yingchen Zhang, Ruqing Zhang et al. — [Token-Flow Firewall: Semantic Runtime Auditing for Persistent AI Agents](http://arxiv.org/abs/2607.08395v1)
  <details><summary>📄 Abstract</summary>
  Persistent AI agents extend large language models (LLMs) beyond single-turn interaction into long-lived software systems. Unlike traditional chat assistants, unsafe content in these agents can propagate through persistent state, reusable skills, and tool-mediated interactions, creating a substantially larger semantic attack surface. We observe that most security-critical interactions in such agents are transmitted through natural-language token flows, including memory updates, tool arguments, re...
  </details>

- **2026-07-09** — Matthias Weiß, Athreya Hosahalli Prakash, Maurice Artelt et al. — [Self-Adaptive Anomaly Detection with Reinforcement Learning and Human Feedback in Connected Vehicles](http://arxiv.org/abs/2607.08373v1)
  <details><summary>📄 Abstract</summary>
  Connected vehicles are autonomous cyber-physical systems whose behavior must be continuously monitored during operation to detect deviations from normal operation before they propagate into failures. Such evaluation is challenging because the systems themselves evolve: over-the-air updates, configuration changes, and shifting workloads alter the definition of normal behavior, causing static diagnostic methods to degrade silently over time. Existing approaches typically address either automated m...
  </details>

- **2026-07-09** — Anh Trac Duc Dinh, Khang Nhat Hoang Vo, Vinh Cong Doan et al. — [Echoes Across Vietnam's Highlands, Delta, and Coast: A Multilingual Corpus for Cham, Khmer, and Tay-Nung](http://arxiv.org/abs/2607.08362v1)
  <details><summary>📄 Abstract</summary>
  Vietnam's ethnic minority languages are almost absent from the field of Natural Language Processing (NLP), and the challenge goes beyond data scarcity: Cham, Khmer, and Tay-Nung differ sharply in script, Vietnamese contact, and standardization, conditions under which standard multilingual adaptation can learn the wrong signals. We introduce CKTN, the first corpus and benchmark for these languages (44,367 documents, 24M subword tokens), spanning continued pretraining, category classification, and...
  </details>

- **2026-07-09** — Lea Roxanne Muth, Marian Margraf — [From Legacy Documentation to OSCAL: An MCP-Based Agent Pipeline for Threat-Informed Continuous Compliance in Critical Infrastructure](http://arxiv.org/abs/2607.08288v1)
  <details><summary>📄 Abstract</summary>
  In critical infrastructure, operational technology environments often cannot be actively scanned, and yet active system feedback is needed for risk assessment and compliance. This paper presents a non-invasive, MCP-grounded multi-agent pipeline that converts natural-language system descriptions into source-verified knowledge graph and audit-ready artifacts in the NIST OSCAL format for continuous automated compliance management. The architecture decouples LLM-based reasoning from deterministic kn...
  </details>

- **2026-07-09** — Hou Hin Ip, Ka Nam Lam, Joshua Man Yu Ng et al. — [Enhancing the KidSat Model: Integrating Geographical Encoding and Data Quality Assessment for Childhood Poverty Prediction](http://arxiv.org/abs/2607.08281v1)
  <details><summary>📄 Abstract</summary>
  Accurate poverty mapping using satellite imagery is often hindered by (i) noisy and sparse survey-derived supervision, (ii) image quality issues such as cloud cover and image corruption, and (iii) lack of explicit spatial structure in image-only models. Building on the KidSat framework, we develop an enhanced pipeline that improves predictive accuracy via refined data preprocessing, systematic image quality assessment, and mathematically defined geographic encoding. First, we refine the fine-tun...
  </details>

- **2026-07-09** — Matthew W. Scroggs, Garth N. Wells — [Algorithm XXXX: Computation of finite element degree-of-freedom transformation matrices](http://arxiv.org/abs/2607.08172v1)
  <details><summary>📄 Abstract</summary>
  The arithmetic intensity of algorithms for computing finite element operators increases with increasing polynomial degree. This has made high degree methods particularly attractive on modern CPU and GPU architectures, since on these architectures performance at low degree is limited (severely) by the available memory bandwidth and only a very small fraction of the floating point capacity of the processor is used. Higher degree methods can exploit a significantly greater fraction of the available...
  </details>

- **2026-07-09** — Utkarsh A. Mishra, Yongxin Chen, Danfei Xu et al. — [Understanding and Mitigating the Video-Action Generalization Gap via Temporal Ratio](http://arxiv.org/abs/2607.08127v1)
  <details><summary>📄 Abstract</summary>
  Generative video foundation models exhibit strong compositional priors, yet world-action models (WAMs) and video-action models (VAMs) often lose these priors after finetuning on robotic action data. We refer to this discrepancy as the video-action generalization gap. In this paper, we systematically investigate this gap by evaluating a comprehensive design space of VAMs, demonstrating that standard design choices yield no emergent explanation pattern. To explain this behavior, we introduce the T...
  </details>

- **2026-07-09** — Lefu Cai, Hongjie Li, Xianchao Wang — [A Non-Decoupled Time-Domain Direct Sampling Method for Inverse Elastic Medium Scattering](http://arxiv.org/abs/2607.08067v1)
  <details><summary>📄 Abstract</summary>
  This work is concerned with an inverse medium problem for elastic waves, in which unknown inhomogeneities are reconstructed from time-resolved boundary measurements. We propose a novel time-domain direct sampling method for locating scatterers from a single incident source, without imposing specific assumptions on the temporal profile of the excitation. In particular, the imaging functional introduces a time-shifted correlation strategy that replaces the traditional $P$-$S$ wave decomposition wi...
  </details>

- **2026-07-09** — Youya Xu, Chengyong Yu, Sanjib Ghosh — [Robust Quantum Learning through Hamiltonian Reservoir Computing](http://arxiv.org/abs/2607.08037v1)
  <details><summary>📄 Abstract</summary>
  Quantum learning provides a versatile paradigm for information processing by exploiting the intrinsic representational capacity of high-dimensional Hilbert spaces. Here, we investigate a Hamiltonian-encoding framework for quantum reservoir computing that simultaneously addresses three key challenges in quantum learning: trainability, hardware efficiency, and information stability. In this framework, input data are directly mapped onto a fixed Hamiltonian and transformed into expressive nonlinear...
  </details>

- **2026-07-08** — Donghyun Lee, Yuhang Li, Ruokai Yin et al. — [KronQ: LLM Quantization via Kronecker-Factored Hessian](http://arxiv.org/abs/2607.07964v1)
  <details><summary>📄 Abstract</summary>
  Post-training quantization (PTQ) is a widely adopted technique for compressing large language models (LLMs) without retraining. Existing second-order PTQ methods, including GPTQ, construct quantization objectives exclusively from input activation statistics, effectively assuming that all output channels contribute equally to the layer-wise reconstruction objective. We propose KronQ, a PTQ framework that challenges this assumption by introducing the gradient covariance into the quantization pipel...
  </details>

- **2026-07-08** — J. Mark Bishop, Stephen J. Cowley — [How Do I Know What to Say Next? Barenholtz's Autogenerative Theory as an Enrichment of Harrisean Integrationism](http://arxiv.org/abs/2607.07891v1)
  <details><summary>📄 Abstract</summary>
  Roy Harris's Integrationist linguistics offers a compelling critique of the referentialist tradition embedded deep at the heart of computational approaches to language, arguing that language is not a code that maps onto a pre-given world but a situated, bipartite activity oriented toward prospective joint action. Yet Integrationism leaves certain explanatory gaps: it does not fully account for the structural mechanism by which signs sustain prospective openness, it undertheorises the continuity ...
  </details>

- **2026-07-08** — Felix Wang, Anudeep Das, Mei Nagappan et al. — [Functional and Secure Code Generation with Task Vectors](http://arxiv.org/abs/2607.07881v1)
  <details><summary>📄 Abstract</summary>
  Large language models (LLMs) are increasingly used for code generation, but they struggle to generate functional code free of security vulnerabilities. Prior work to improve the secure code generation abilities of such coding LLMs has largely focused on evaluating code functionality and security separately using different datasets, or focused on finding vulnerabilities post-generation. At the same time, the text-generation domain has seen significant work on alignment techniques, where models ar...
  </details>

- **2026-07-08** — Tingkai Liu, Muralidhar Andoorveedu, Sanjoy Das et al. — [CTA-Pipelining: A Latency-Oriented Spatial Scaling Method for Multi-GPU Systems](http://arxiv.org/abs/2607.07862v1)
  <details><summary>📄 Abstract</summary>
  The evolution of compute infrastructure has transformed multi-GPU systems into tightly integrated shared-memory structures. However, current software still mostly treats these coherent interconnects simply as high-speed networks. Simultaneously, the demand for serving Large Language Models under latency constraints has shifted GPU workload optimization from being throughput-driven to latency-bound, necessitating latency-oriented scaling methods beyond Tensor Parallelism (TP).   Thus, we introduc...
  </details>

- **2026-07-08** — Mihnea C. Moldoveanu, Joel A. C. Baum — [Adversarial Social Epistemology for Assemblies of Humans and Large Language Models](http://arxiv.org/abs/2607.07760v1)
  <details><summary>📄 Abstract</summary>
  We outline an adversarial social epistemology (ASE) for densely interactive communicative landscapes in which public assertions are scaffolded by chains of testimony, inference, institutional certification, and tacit trust. In such landscapes, agents have incentives and affordances to distort, color, omit, fabricate, or strategically under-specify information for private, reputational, rhetorical, or material gains. We argue that these phenomena are not adequately captured by familiar descriptio...
  </details>

- **2026-07-08** — Yingyun Cui, Yi Xie, Piaohong Wang et al. — [PERFOPT-Bench: Evaluating Coding Agents on Software Performance Optimization](http://arxiv.org/abs/2607.07744v1)
  <details><summary>📄 Abstract</summary>
  Coding-agent benchmarks have largely measured whether agents can produce functionally correct patches, but production software also demands measurable speedups on real execution targets. Performance optimization is a distinct agentic task: agents must profile executions, diagnose cross-layer bottlenecks, edit code without breaking correctness, and verify that gains are reproducible rather than measurement artifacts. We introduce PERFOPT-Bench, a benchmark for evaluating this full performance-eng...
  </details>

- **2026-07-08** — Qiaoni Shi, Kai Zhu, Kai Gu — [Answering Without Referring: How AI Search Rewrites the Web's Economic Bargain](http://arxiv.org/abs/2607.07652v1)
  <details><summary>📄 Abstract</summary>
  Search engines have long allocated attention on the web by routing users from queries to websites. AI search changes this arrangement because information needs can be resolved inside the intermediary. Using URL-level Comscore U.S. desktop clickstream, we compare ChatGPT and Google information-seeking occasions and exploit ChatGPT Search access expansions to estimate traditional search displacement. ChatGPT produces outbound clicks in only 5.2% of conversation sessions, far below Google's referra...
  </details>

- **2026-07-08** — Ana Schwengber Kelm, Christian Bockermann, Jörg Frochte — [Multi-Class vs. Multi-Label BERT for CVE-to-CWE Mapping: How Taxonomy Structure Shapes the Errors](http://arxiv.org/abs/2607.07573v1)
  <details><summary>📄 Abstract</summary>
  Assigning Common Weakness Enumeration (CWE) categories to Common Vulnerabilities and Exposures (CVE) records remains an important but largely manual step in vulnerability analysis. We study this task as a text classification problem and compare two modelling choices: a \emph{multi-class} formulation that predicts a single CWE per CVE and a \emph{multi-label} formulation that allows multiple assignments. Three transformer encoders (BERT Base, SecureBERT, and CySecBERT) are evaluated on three nest...
  </details>

- **2026-07-08** — Jaris Küken, Shi Bin Hoo, Martin Mráz et al. — [TimEE: End-to-end Time Series Classification via In-Context Learning](http://arxiv.org/abs/2607.07500v1)
  <details><summary>📄 Abstract</summary>
  Time series classification (TSC) is dominated by a two-stage paradigm: train a feature encoder -- either from scratch on the target dataset or via pretraining on large corpora -- and then fit a task-specific classifier on top. While effective, this decoupling optimizes representation learning independently of the classification objective, requires per-dataset training, and prevents the model from exploiting label information during inference. We introduce TimEE, a 4.5M-parameter foundation model...
  </details>

- **2026-07-08** — Florian Fuchs, Jessy Gosselin-Grant, Boris Skuin et al. — [Reward-Adaptive Iterative Discovery: A Case Study on Automated Game Testing for NHL26](http://arxiv.org/abs/2607.07498v1)
  <details><summary>📄 Abstract</summary>
  Testing is a major effort for the gaming industry, requiring a significant part of development budget and people power. We present a case study on a development version of the ice hockey game EA SPORTS NHL 26, for which human playtesters test the goalie AI for behavioral exploits. To reduce the effort of re-testing the goalie AI after every game or behavior modification in the development phase, we propose Reward-Adaptive Iterative Discovery (RAID), a novel approach to automatically find exploit...
  </details>

- **2026-07-08** — Yang Shi, Jiaheng Fu, Yihe Huang et al. — [Mitigating Taint-Style Vulnerabilities in MCP Servers via Security-Aware Tool Descriptions](http://arxiv.org/abs/2607.07461v1)
  <details><summary>📄 Abstract</summary>
  Large language models (LLMs) are increasingly deployed as autonomous agents that interact with external tools and services via the Model Context Protocol (MCP), a standardized interface for dynamic tool invocation. While MCP simplifies integration, it also expands the attack surface and enables generic exploits across multiple servers. Despite prior work on malicious MCP servers, the vulnerability landscape of MCP servers remains underexplored. In this work, we systematically analyze MCP server ...
  </details>

- **2026-07-08** — Chethan Krishnamurthy Ramanaik, Tobias Callies, Michael Hecht et al. — [On Adversarial Vulnerability of Vision-Language Models through the Lens of Intermediate Spectral Subspaces](http://arxiv.org/abs/2607.07375v1)
  <details><summary>📄 Abstract</summary>
  Adversarial vulnerability in deep neural networks (DNNs) has been studied from the perspectives of decision-boundary geometry, feature robustness, input-output Jacobians, and the instability of inverse problems. Here, we focus on the spectral structure of intermediate linear transformations that propagate information through modern DNNs, an unexplored mechanism of adversarial vulnerability. Specifically, we investigate transformer-based vision-language models, whose linear layers admit interpret...
  </details>

- **2026-07-08** — Xin Li, Jiaju Han, Ma Yaqi et al. — [InfraQR: Edge-Placed QR-Inspired Structured Patch Attacks on Infrared Vision-Language Models](http://arxiv.org/abs/2607.07288v1)
  <details><summary>📄 Abstract</summary>
  Infrared vision-language models are increasingly used for perception under low-light and adverse visual conditions, yet their robustness to localized structured perturbations remains underexplored. Existing infrared adversarial studies mainly focus on object detectors, leaving the security of infrared vision-language models less systematically examined. We present InfraQR, a QR-inspired structured patch attack for infrared vision-language models. Unlike localized attacks that attach perturbation...
  </details>

- **2026-07-08** — Antonio Cabrales, Wenhao Cheng — [Evaluation and Assignment with Networked Competition and Spillovers](http://arxiv.org/abs/2607.07280v1)
  <details><summary>📄 Abstract</summary>
  This paper studies how organizations should jointly design evaluation rules and assign workers when performance depends on both effort and non-discretionary advantage. Agents choose effort in positions linked by a competition network, while their effective advantage depends on own type and spillovers through a second network. The planner chooses both the assignment and the effort weight in evaluation. Equilibrium effort rises with a position's Katz-Bonacich centrality and falls with effective ad...
  </details>

- **2026-07-08** — Miguel Lopez-Duran, Elena Marrero, Julian Fierrez et al. — [Comparative Study of Domain-adapted VLMs for General Document Visual Question Answering](http://arxiv.org/abs/2607.07179v1)
  <details><summary>📄 Abstract</summary>
  Document Visual Question Answering (DocVQA) presents a complex multimodal challenge, requiring models to exploit visual, textual, and layout information from documents. Although Vision-Language Models (VLMs) have shown remarkable performance in text-vision tasks, their robustness and transferability to different document domains remains underexplored. In this study, we present a comprehensive evaluation of 8 open-source pretrained VLMs on DocVQA in three different document domains: industrial do...
  </details>

- **2026-07-08** — Zetian Hu, Shunyu Liu, Junjie Zhang et al. — [Entropy Pacing Policy Optimization for Multi-Task Agentic Reinforcement Learning](http://arxiv.org/abs/2607.07178v1)
  <details><summary>📄 Abstract</summary>
  Recent breakthroughs of Reinforcement Learning (RL) have highlighted its potential for complex agentic Large Language Model (LLM) tasks. However, existing efforts largely focus on single-task settings, whereas real-world deployment necessitates a generalist agent capable of solving multiple tasks simultaneously. In this work, we identify a critical yet underexplored phenomenon in multi-task agentic RL: different tasks can exhibit exploration-exploitation pace mismatch. Specifically, easier tasks...
  </details>

- **2026-07-08** — Yao Sheng, Yu Yokoi — [Stable Matchings with Minimum Utility Gap](http://arxiv.org/abs/2607.07160v1)
  <details><summary>📄 Abstract</summary>
  We introduce the Stable Matching Problem with Minimum Utility Gap, which seeks a stable matching in which the utilities received by individual agents are as balanced as possible. Our framework can handle many-to-many matchings and general utility functions on partner sets that are consistent with the agents' preferences. We consider two measures for comparing agents' utilities: the difference between the maximum and minimum utilities, and their ratio.   We provide a polynomial-time algorithm for...
  </details>

- **2026-07-08** — Víctor Mayoral-Vilches — [Certifying Ghosts: How Cybersecurity AI Agents Break the EU Cyber Resilience Act](http://arxiv.org/abs/2607.07109v1)
  <details><summary>📄 Abstract</summary>
  The EU Cyber Resilience Act (CRA) makes a smart bet. It does not demand that products be free of vulnerabilities, but only that manufacturers run a process: assess risk, handle flaws, ship updates. The bet pays off if four things about the world stay true: (P1) finding vulnerabilities is slow, skilled, human work; (P2) a product's exploitable flaws are knowable the day it ships; (P3) exploitation is rare enough to notice; and (P4) fixes keep pace with discovery. Cybersecurity AI (CAI) agents, AI...
  </details>

- **2026-07-08** — Junjie Wu, Lingjian Zhou, Zerui Shao et al. — [EvoOMG: An Evolution-Oriented Multi-Agent Guidance Framework for Heterogeneous Legacy-and-MLO Wi-Fi Networks](http://arxiv.org/abs/2607.07045v1)
  <details><summary>📄 Abstract</summary>
  The gradual deployment of Wi-Fi 7/8 multi-link operation (MLO) will lead to long-term coexistence between legacy non-MLO stations (STAs) and MLO-capable STAs in WLANs. This mixed deployment makes throughput optimization challenging because legacy STAs follow single-link contention and transmission, whereas MLO-capable STAs can exploit multiple links with richer access opportunities. Existing learning-based methods usually treat such networks as homogeneous systems and directly map the current ob...
  </details>

- **2026-07-08** — Dennis Gross, Quentin Mazouni, Helge Spieker et al. — [Gimitest: A Comprehensive Tool for Testing Reinforcement Learning Policies](http://arxiv.org/abs/2607.07029v1)
  <details><summary>📄 Abstract</summary>
  Reinforcement learning (RL) policies can be unsafe and vulnerable to attacks. Ensuring their reliability is often a pain point as existing automated testing methods target only selected environments, testing scenarios, and RL algorithms. To address this, we propose a comprehensive framework for testing single- and multi-agent RL policies under varying conditions. Our implementation of this framework, Gimitest, is an open-source tool that supports various gym frameworks and allows for modificatio...
  </details>

- **2026-07-07** — Austin Huang, William Maxwell, Vasilis Belis et al. — [Spectral Born machines: classically trainable quantum generative models for discrete data](http://arxiv.org/abs/2607.06675v1)
  <details><summary>📄 Abstract</summary>
  We present \emph{spectral Born machines}, a class of quantum generative models that results from viewing and generalizing the class of IQP Born machines through the lens of group Fourier analysis. These quantum models exploit the quantum Fourier transform to create an inductive bias that make them naturally suited to learning integer-structured data, while remaining classically hard to sample from in general. Similar to IQP Born machines, spectral Born machines can be trained efficiently at scal...
  </details>

- **2026-07-07** — Jiaming Liu, Qingpo Wuwu, Nuowei Han et al. — [Lift3D-VLA: Lifting VLA Models to 3D Geometry and Dynamics-Aware Manipulation](http://arxiv.org/abs/2607.06564v1)
  <details><summary>📄 Abstract</summary>
  Recently, Vision-Language-Action (VLA) models have demonstrated strong generalization across diverse tasks. However, effective robotic manipulation in physical environments fundamentally requires geometric understanding and spatial reasoning. While some VLA approaches attempt to incorporate 3D information, they are constrained by limited data availability and geometric information loss in current 3D encoding pipelines, and fail to jointly capture 3D geometry and temporally structured actions in ...
  </details>

- **2026-07-07** — Zichao Zhang, Melda Yuksel, Gokhan M. Guvensen et al. — [Constrained Capacity Analysis for Faster-than-Nyquist Signaling](http://arxiv.org/abs/2607.06496v1)
  <details><summary>📄 Abstract</summary>
  This paper studies the constrained-capacity for precoded faster-than-Nyquist (FTN) signaling with finite-alphabet inputs. Despite the promise of accelerated transmission, the fundamental rate limit of precoded FTN signaling under practical finite-alphabet constraints remains unclear. By introducing cyclic prefix (CP) and cyclic suffix (CS), the FTN channel is decomposed into a set of parallel eigenchannels by the discrete Fourier transform (DFT) matrix, based on which the constrained capacity is...
  </details>

- **2026-07-07** — R. P. Malik — [Abelian 2-Form Gauge Theory: Basic Canonical Brackets and Nilpotency Property of Noether (Anti-)BRST Charges](http://arxiv.org/abs/2607.06486v1)
  <details><summary>📄 Abstract</summary>
  Within the framework of Becchi-Rouet-Stora-Tyutin (BRST) formalism, we invoke the beauty of the basic canonical (anti)commutators to prove the nilpotency property of the Noether (anti-)BRST charges for the D-dimensional BRST-quantized version of the free Abelian 2-form gauge theory which is endowed with a non-trivial Curci-Ferrari (CF) type restriction. In this proof, we use only the theoretical strength of the Gauss divergence theorem. We demonstrate that, under the off-shell nilpotent (anti-)B...
  </details>

- **2026-07-07** — Yu Cheng, Siyue Yao, Zhongang Qi et al. — [Dynamic-in-Few-Step: Unifying Dynamic Computation and Few-Step Distillation for Efficient Video Generation](http://arxiv.org/abs/2607.06631v1)
  <details><summary>📄 Abstract</summary>
  Video Diffusion Models (VDMs) have demonstrated superior generation quality but suffer from prohibitive computational costs. While recent few-step distillation techniques significantly accelerate inference, they typically enforce a static model architecture across all denoising stages, ignoring the varying computational demands inherent to different noise levels. In this work, we propose a novel post-training acceleration framework that exploits this redundancy by integrating dynamic structural ...
  </details>

- **2026-07-07** — Alicia Parrish, Rajat Shinde, Sanket Badhe et al. — [Pluralis v0.1: Towards a Multicultural, Multimodal, Multilingual Benchmark for AI Risk and Reliability](http://arxiv.org/abs/2607.06196v1)
  <details><summary>📄 Abstract</summary>
  Current AI safety evaluation and benchmarking frameworks predominantly rely on Western-centric culture-agnostic defaults that mask critical regional laws, socio-linguistic nuances, and cultural taboos, leaving Vision-Language Models (VLMs) vulnerable in global deployments. We introduce Pluralis v0.1: a novel multimodal, multi-regional, and multilingual dataset built from a culture-first perspective. Spanning 6,448 prompts across six Asia-Pacific countries (Bangladesh, India, Korea, Pakistan, Sin...
  </details>

- **2026-07-07** — Melika Honarmand, Samin Mahdipour Aghabagher, Martin Schrimpf — [Reward Valuation in Vision Language Models: Causal Mechanisms Underlying Anhedonia](http://arxiv.org/abs/2607.06626v1)
  <details><summary>📄 Abstract</summary>
  Recent Vision-Language Models capture increasingly complex aspects of human cognition. Here we ask whether this alignment extends to reward valuation, which we assess in a mechanistic framework built on clinical tests that were developed to evaluate anhedonia and motivational deficits in major depressive disorder. In the brain, anhedonia is frequently linked to dysregulation in the Nucleus Accumbens (NAc) and the broader dopaminergic reward system. While neuroimaging has localized these deficits...
  </details>

- **2026-07-07** — Ioanna-Yvonni Tsaknaki, Andrea Macrì, Fabrizio Lillo — [Can Reinforcement Learning Efficiently Discover Price Manipulation?](http://arxiv.org/abs/2607.06121v1)
  <details><summary>📄 Abstract</summary>
  In this paper, we investigate whether a model-free RL agent can identify and exploit price manipulation opportunities more effectively than a traditional model-based approach that assumes correct specification of the data-generating process but relies on noisy parameter estimates. We consider a single-asset market in which prices evolve according to an Almgren-Chriss framework with non-linear permanent impact and linear temporary impact. We first establish the existence of price-manipulative str...
  </details>

- **2026-07-07** — Robin Holzinger, Riccardo Colletti — [Drift Happens: An Empirical Study of Neural Architecture Robustness to Temporal Distribution Shift](http://arxiv.org/abs/2607.05908v1)
  <details><summary>📄 Abstract</summary>
  Real-world data distributions evolve over time, inducing temporal distribution shift that can substantially degrade the reliability of deployed machine learning systems. However, the extent to which architectural choices and their associated inductive biases affect temporal robustness remains insufficiently understood.   We present a systematic empirical comparison of temporal robustness across three heterogeneous, time-indexed domains encompassing image classification, multi-label text classifi...
  </details>

- **2026-07-07** — Chenyu Zhou — [More Convincing, Not More Correct: Self-Play Reward Hacking of Reference-Free LLM Judges](http://arxiv.org/abs/2607.05904v1)
  <details><summary>📄 Abstract</summary>
  Training a language model against its own reference-free judgments (the premise of self-rewarding, self-play, and LLM-as-a-judge pipelines) assumes a model's verdict on a shown answer tracks correctness. We show it fails structurally: conditioned on a candidate, a judge scores plausibility, not correctness, leaving false-positive basins a policy learns to exploit. We measure this with a hidden-anchor audit: a held-out, cross-source exact-match check the judge never sees. On GSM8K with Qwen3 poli...
  </details>

- **2026-07-07** — Suraj Yadav, Anjaneya Sharma, Siddharth Yadav — [Breaking Spurious Correlations via Generative Randomization and Cross-Variant Self-Supervised Learning](http://arxiv.org/abs/2607.05850v1)
  <details><summary>📄 Abstract</summary>
  Deep neural networks trained with Empirical Risk Minimization (ERM) often fail under distribution shifts because they exploit spurious correlations between object labels and background context. Recent generative approaches address this issue by creating counterfactual images with altered contexts, but typically use these samples as standard data augmentation, leaving the model free to retain background-sensitive representations. We propose a two-stage framework that uses generative intervention ...
  </details>

- **2026-07-07** — Burte Bayarsaikhan, Serynn Kim, Buru Chang — [CoPiT: Cognitive Pivot Translation for Digraphic Low-Resource Mongolian in the Traditional Script](http://arxiv.org/abs/2607.05849v1)
  <details><summary>📄 Abstract</summary>
  Low-resource languages remain challenging for machine translation, and Mongolian is a representative case. As a digraphic language, Mongolian is written in both Cyrillic and Traditional scripts, which exhibit a severe imbalance in data availability. While the Cyrillic script is relatively well-resourced, the Traditional script remains extremely data-scarce and orthographically ambiguous, leading to substantial performance degradation in direct translation. We propose CoPiT, a cognitively motivat...
  </details>

- **2026-07-07** — Liyou Chen, Hailong Sun, Xiang Gao et al. — [Detecting Vulnerability-Inducing Commits via Multi-Stage Reasoning with LLM-Based Agents](http://arxiv.org/abs/2607.05772v1)
  <details><summary>📄 Abstract</summary>
  Detecting vulnerability-inducing commits (VICs) at submission time is critical for improving the security and reliability of software systems. However, this task is highly challenging because it requires reasoning about the semantic impact of code changes from heterogeneous information sources, including code diffs, commit messages, and the surrounding contextual code. Existing approaches often struggle to fully capture these complex interactions, resulting in limited detection performance. In t...
  </details>

- **2026-07-07** — Yunhan Xu, Qifeng Wu, Xunjin Li et al. — [ArtisanCAD: An Industrial-Level CAD Agent with Expert-Grounded Knowledge Distillation](http://arxiv.org/abs/2607.05750v2)
  <details><summary>📄 Abstract</summary>
  Computer-aided design (CAD) for industrial components requires long-horizon procedural modeling, robust feature dependencies, editable parametric geometry, and production-grade B-Rep execution. Existing text-to-CAD methods have made promising progress in generating CAD programs from natural-language descriptions, but they still struggle when user prompts are ambiguous, underspecified, or only describe high-level design intent. They also rarely exploit expert procedural knowledge naturally availa...
  </details>

- **2026-07-07** — Mohammadreza Rashidi — [The Balkanization of Execution-Security Research for AI Coding Agents: Isolation, Access Control, and Time-of-Check-to-Time-of-Use Vulnerabilities](http://arxiv.org/abs/2607.05743v1)
  <details><summary>📄 Abstract</summary>
  AI coding agents now read repositories, call tools, and execute shell commands with limited human oversight, and a fast-growing body of work studies whether the execution layer around them is actually safe. That literature is scattered. Papers on sandbox isolation, capability and access control, policy enforcement, time-of-check-to-time-of-use (TOCTOU) races, Model Context Protocol (MCP) threats, identity delegation, execution provenance, network egress control, and static analysis of agent-gene...
  </details>

- **2026-07-07** — Hossein Rajoli, Fatemeh Lotfi, Niloufar Alipour Talemi et al. — [SAMPLe: SAM-based Optimizer for Prompt Learning in VLMs](http://arxiv.org/abs/2607.05727v1)
  <details><summary>📄 Abstract</summary>
  Pre-trained Vision-Language Models (VLMs) like CLIP have proven highly effective as foundation models for various downstream applications. However, prompt learning in VLMs encounters a performance-generalization dilemma: while prompts can be tuned to achieve high accuracy on seen distributions, this tuning process often undermines their generalizability to unseen data. The limited set of learnable prompts, which contextualize and condition the input to steer it toward the task within the pretrai...
  </details>

- **2026-07-06** — Leonardo Trentini, Fanny Lehmann, Laura Crocetti et al. — [Integrating GNSS-Derived Zenith Wet Delay into a Weather Foundation Model Improves Precipitation Forecasting](http://arxiv.org/abs/2607.05658v1)
  <details><summary>📄 Abstract</summary>
  Global Navigation Satellite Systems (GNSS), best known for positioning, also serve weather science, as atmospheric water vapour delays their signals. This delay, the Zenith Wet Delay (ZWD), is a direct, all-weather measure of column moisture. Although assimilated into numerical weather prediction for decades, ZWD is not yet used by leading machine learning weather models (MLWM), despite addressing a known deficiency: the underestimation of severe precipitation. Here we present the first integrat...
  </details>

- **2026-07-06** — Babak Hemmatian, Razan Baltaji, Lav R. Varshney — [Collective Cognition in Hybrid Groups: A Network Science Synthesis](http://arxiv.org/abs/2607.05593v1)
  <details><summary>📄 Abstract</summary>
  The growing integration of AI agents into human teams calls for a principled understanding of how collective intelligence emerges in hybrid systems. Recent frameworks clarify how attention, memory, and reasoning differences shape human-AI interaction at the individual and dyadic levels, but a formal account of how these differences scale to group-level dynamics is lacking. Most network science has examined either human-only or multi-agent AI-only systems, leaving open how its findings and parame...
  </details>

- **2026-07-06** — Linjie Xu, David Wipf — [Parameter-Free Encoders Remain Viable for RDB Foundation Models](http://arxiv.org/abs/2607.05476v1)
  <details><summary>📄 Abstract</summary>
  Given a relational database (RDB) storing heterogeneous tabular information, how can we predict missing (or future) values in some target column of interest? As the space of potential targets is vast across enterprise settings, it is preferable to avoid learning a new model from scratch each time there is a new prediction task. Frozen foundation models based on RDB-specific encoders provide a viable solution, but ideal design remains an open question. On the one hand, it has recently been argued...
  </details>

- **2026-07-06** — Yuanmin Xie, Xiangfan Wu, Wenhao Wu et al. — [ShadowProbe: Language-Extensible Detection of Hidden Algorithmic Complexity Vulnerabilities](http://arxiv.org/abs/2607.05474v1)
  <details><summary>📄 Abstract</summary>
  Algorithmic Complexity Vulnerabilities (ACVs) arise when adversarial inputs trigger worst-case execution behavior, causing severe performance degradation or Denial-of-Service conditions. A key but underexplored source is shadow complexity: non-trivial computational costs hidden inside seemingly benign standard library APIs. Because these costs are invisible at call sites, attackers can exploit them to induce unexpected superlinear runtime behavior. Existing ACV detectors often rely on fuzzing, s...
  </details>

- **2026-07-06** — Jerick Shi, Terry Jingcheng Zhang, Bernhard Schölkopf et al. — [When Agents Lie: Premeditation, Persistence, and Exploitation in Repeated Games](http://arxiv.org/abs/2607.05132v2)
  <details><summary>📄 Abstract</summary>
  As large language models are deployed as autonomous agents that communicate intentions before acting, a critical safety question is whether agents that publicly commit to actions will honor those commitments. We place LLM agents in repeated $n$-player games with a three-stage protocol that separates private intent, public announcement, and final action, allowing us to identify whether each deviation from a stated announcement was already planned during private deliberation. Evaluating three fron...
  </details>

- **2026-07-06** — Eli N. Weinstein, David M. Blei — [Geometric Causal Models](http://arxiv.org/abs/2607.05153v1)
  <details><summary>📄 Abstract</summary>
  Scientists often seek to draw causal inferences from structured data that is not independently and identically distributed, such as spatial data, network data, or molecular data. We develop geometric causal models (GCMs), a framework for causal inference from dependent data that exploits underlying symmetries of the data generating process. For example, in spatial data, we consider processes that are symmetric under translations, or in graph data, symmetric under permutations of the nodes. We sh...
  </details>

- **2026-07-06** — Joongwon Chae, Lihui Luo, Yang Liu et al. — [ProCon: Projection-Consistency Memory for Training-Free Anomaly Detection](http://arxiv.org/abs/2607.04894v1)
  <details><summary>📄 Abstract</summary>
  Memory-based anomaly detection is attractive because it localizes defects from normal images without training a decoder or synthesizing pseudo anomalies. However, most memory methods still use the memory bank as a nearest-neighbor lookup table: a test patch is treated as normal if it has one nearby normal anchor. This hard retrieval view is vulnerable to false-normal matches and does not test whether the patch is consistently supported by a local normal neighborhood. We propose ProCon, a trainin...
  </details>

- **2026-07-06** — Kaixin Feng, Zhichao Wen, Zhaohong Liao et al. — [WinTA-GIL: Windowed Trajectory Alignment for GNSS-IMU-LiDAR Heading Refinement in Intermittent Signal Environments](http://arxiv.org/abs/2607.04879v1)
  <details><summary>📄 Abstract</summary>
  Although multi-source fusion positioning systems have achieved significant progress, accurate and reliable heading estimation remains a critical challenge due to the lack of gravitational constraints and the inherent weak observability of heading in complex environments. Most existing methodologies are specifically tailored for the startup phase, relying on a singular initial alignment to establish the heading reference. Consequently, these approaches lack the adaptability required to refine hea...
  </details>

- **2026-07-06** — Andreas Athanasopoulos, Anne-Marie George, Christos Dimitrakakis — [Probably Correct Optimal Stable Matching under Two-Sided Uncertainty](http://arxiv.org/abs/2607.04824v1)
  <details><summary>📄 Abstract</summary>
  We study a sequential learning problem for stable matchings in two-sided markets where preferences on both sides are initially unknown. We focus on a centralized setting where an algorithm matches agents at each time step and receives noisy rewards that reflect the preferences of the matched agents, following a semi-bandit feedback structure. We adopt a pure exploration perspective, aiming to efficiently identify the optimal stable matching with high probability. Our work extends prior results b...
  </details>

- **2026-07-06** — Weijian Liu, Mingzhen Li, Rui Kang et al. — [Direct Model State Migration for Elastic Training of Large Language Models](http://arxiv.org/abs/2607.04749v1)
  <details><summary>📄 Abstract</summary>
  Large language model (LLM) training shall adapt to dynamic resources in shared clusters to tackle the elasticity, including passive preemption and optimistic scaling. State migration across device sets is required when altering the hybrid-parallel configuration due to dynamic resources. Existing solutions rely on checkpoint-based mechanisms, which persist complete states to storage for resuming with re-assigned resources, forcing all GPUs to stall when transferring model states. Despite optimiza...
  </details>

- **2026-07-06** — Tarek Elsayed, Shiping Yang, Eunsong Koh et al. — [RustMizan: A Compilable, Contamination-Aware Benchmarking Framework for Rust Vulnerabilities](http://arxiv.org/abs/2607.04729v1)
  <details><summary>📄 Abstract</summary>
  LLM agents are increasingly applied to vulnerability analysis, but existing benchmarks have not kept pace. They typically rely on small non-compilable snippets, focus on binary classification (vulnerable or not), and do not account for the risk that publicly-released datasets are part of model training corpora. We introduce RustMizan, a benchmarking framework for Rust vulnerability analysis that addresses these gaps. RustMizan contains compilable code variants at the crate, file, and function le...
  </details>

- **2026-07-06** — Pin Tang, Guoqing Wang, Xiangxuan Ren et al. — [PixelPilot: Scalable Vision-Language-Action Models for End-to-End Autonomous Driving](http://arxiv.org/abs/2607.04637v1)
  <details><summary>📄 Abstract</summary>
  Vision-Language-Action Models (VLAs), which leverage the advanced reasoning capabilities of Vision-Language Models (VLMs), show promising generalization in complex autonomous driving scenarios. Existing VLAs typically predict and optimize 3D trajectories from 2D images. While intuitive, this 2D-to-3D prediction is inherently entangled with camera parameters, leading to limited data scalability across heterogeneous driving datasets. Moreover, directly optimizing in 3D space induces severe converg...
  </details>

- **2026-07-06** — Leran Hong, Lei Jin, Jianfeng Zhu — [Characterizing the Temporal, Emotional, and Social Patterns of Adolescent Substance Use Discussions on Reddit](http://arxiv.org/abs/2607.04566v1)
  <details><summary>📄 Abstract</summary>
  Adolescence is a critical developmental period marked by heightened emotional sensitivity, social stress, and vulnerability to substance use. However, traditional research methods provide limited access to adolescents' authentic experiences, hindering efforts to develop evidence-based prevention and intervention strategies. Social media provides a unique opportunity to observe adolescents' naturally occurring discussions about substance use, offering valuable insights into their opinions, emotio...
  </details>


### 📂 defense
*防御与防护方法 / Defense & Protection Methods* — 53 papers

- **2026-07-09** — Amirhossein Taherpour, Xiaodong Wang — [Secure Decentralized Federated Learning via Gossip and Virtual Voting](http://arxiv.org/abs/2607.08651v1)
  <details><summary>📄 Abstract</summary>
  Decentralized federated learning (DFL) removes the central server by letting nodes exchange model updates through peer-to-peer gossip, but existing gossip-based methods often lack provenance finality and resilience to Byzantine or lazy participants. Ledger-assisted federated learning (FL) improves auditability, yet blockchains, shards, or settlement committees can reintroduce global coordination costs that conflict with DFL locality. This paper proposes \emph{gspDAG-FL}, a secure DFL framework t...
  </details>

- **2026-07-09** — Zheng Gao, Xiaoyu Li, Xiaoyan Feng et al. — [TRACE: A Two-Channel Robust Attribution Watermark via Complementary Embeddings for LLM-Agent Trajectories](http://arxiv.org/abs/2607.08400v1)
  <details><summary>📄 Abstract</summary>
  LLM agents reach users through resellers, who may rebrand a developer's agent or substitute a cheaper model. When provenance is disputed, attribution rests on the trajectory log (the record of tool calls, observations, and executed actions, not the model's reasoning), which the reseller stores and processes to meter usage. A watermark must therefore survive an adversary with full read/write access to the very evidence it is detected from; existing agent watermarks do not, as their attribution is...
  </details>

- **2026-07-09** — Zhekai Chen, Chengqi Duan, Kaiyue Sun et al. — [UniClawBench: A Universal Benchmark for Proactive Agents on Real-World Tasks](http://arxiv.org/abs/2607.08768v1)
  <details><summary>📄 Abstract</summary>
  The rapid development of large language models and multimodal large language models has accelerated the emergence of proactive agents capable of operating everyday tools and assisting users in real-world environments. However, existing benchmarks struggle to evaluate such agents effectively, as they often rely on sandboxed environments and single-turn evaluation paradigms. Moreover, their scenario-based task taxonomies mix multiple model capabilities within the same task category, making it diff...
  </details>

- **2026-07-09** — Shreyas Subramanian, Adewale Akinfaderin, Akarsha Sehwag — [Super Weights in LLMs and the Failure of Selective Training](http://arxiv.org/abs/2607.08733v1)
  <details><summary>📄 Abstract</summary>
  Recent work identified Super Weights, individual parameters whose removal degrades model performance by orders of magnitude. We show that this degradation due to pruning Super Weights does not universally apply to all LLMs. Furthermore, if these parameters are so important, Super Weight-aware training should be effective. We show the opposite. Training Super Weights in isolation (100 to 8,192 parameters) drops accuracy to random-guessing levels on both OLMo-1B and OLMo-7B, and expanding to local...
  </details>

- **2026-07-09** — Xuefei Wang — [Out of Sight: Compression-Aware Content Protection against Agentic Crawlers](http://arxiv.org/abs/2607.08180v1)
  <details><summary>📄 Abstract</summary>
  The rise of LLM-based agents with reasoning, summarization, and memory capabilities has created a new threat surface for online content that conventional defenses fail to address. Existing defenses like access controls can be circumvented by agents mimicking ordinary browsers, and injection-based defenses often degrade human readability. In this paper, we revisit the agent pipeline and identify context compression, which agents routinely invoke to fit context budgets, as a critical yet overlooke...
  </details>

- **2026-07-09** — Hao Wu, RongQi Han, Zhen Wang et al. — [Diarization-Guided Qwen-ASR Adaptation for Multilingual Two-Speaker Conversational Speech](http://arxiv.org/abs/2607.08208v1)
  <details><summary>📄 Abstract</summary>
  This paper describes our self-designed system for Task 1 of the MLC-SLM 2026 Challenge for multilingual two-speaker conversational speech. The system combines a modular speaker diarization front end with a challenge-adapted Qwen3-ASR-1.7B recognizer. The diarization front end performs voice activity detection, subsegment generation, CAMPPlus speaker embedding extraction, two-speaker spectral clustering, and RTTM-based audio segmentation. The resulting speaker-attributed segments are grouped by l...
  </details>

- **2026-07-09** — Mingyu Zhao, Zhaohan Li, Zhenxiong Miao et al. — [PIT-SUN: A Deployable Empirical Marginal Transform Framework with Expectation-Consistent Recovery for Regression in Recommender Systems](http://arxiv.org/abs/2607.08202v1)
  <details><summary>📄 Abstract</summary>
  Estimating original-space conditional expectations is central to value-driven recommender systems, including dwell time, GMV, and LTV forecasting. Standard MSE is expectation-consistent in principle, but its gradients become unstable on heavy-tailed, zero-inflated, and multimodal targets, causing mean collapse and tail shrinkage. Target transformation alleviates this scale conflict, yet any useful nonlinear marginal transform loses expectation consistency under direct inversion. This is not an i...
  </details>

- **2026-07-09** — Mingyu Dou, Shi Qiu, Ming Hu et al. — [UAV-OVVIS: Unmanned Aerial Vehicles Also Need Open-Vocabulary Video Instance Segmentation](http://arxiv.org/abs/2607.08075v1)
  <details><summary>📄 Abstract</summary>
  Unmanned Aerial Vehicle (UAV) videos are widely used in traffic monitoring, urban management, and emergency rescue. However, existing UAV video perception mainly relies on box-level localization and trajectory association under predefined categories, making it difficult to simultaneously support flexible queries and fine-grained instance-level dynamic understanding in open scenarios. To this end, we introduce a new task, UAV Open-Vocabulary Video Instance Segmentation (UAV-OVVIS), which discover...
  </details>

- **2026-07-09** — Argyro Sasli, Maojie Xu, Alexandra Junell et al. — [Catching Disguised Transients with ASTRANet: Anomaly-Aware Spectroscopic Classification and Conformal Calibration](http://arxiv.org/abs/2607.08044v1)
  <details><summary>📄 Abstract</summary>
  Time-domain surveys discover thousands of transients per year, but the spectroscopic identification of rare and physically peculiar objects remains rate-limited by closed-set classifiers that confidently assign every input to a known class -- including spectra that genuinely belong to no known class. We present the \texttt{ASTRANet} framework, a confidence-aware infrastructure for spectroscopic transient classification built around three coupled modules: a hierarchical spectral classifier that o...
  </details>

- **2026-07-09** — Trong-Thuan Nguyen, Minh-Triet Tran — [LOGOS: Language-guided Oriented Object Detection in Aerial Scenes](http://arxiv.org/abs/2607.08004v1)
  <details><summary>📄 Abstract</summary>
  Object detection in geospatial scenes, such as satellite and aerial imagery, poses significant challenges due to the varying orientations and densities of objects, as well as the complex backgrounds inherent to remote sensing imagery. Traditional methods for oriented object detection have struggled to address issues such as angular discontinuity, fixed query sizes, and inefficiencies in handling sparse or cluttered scenes. In this paper, we propose LOGOS, a novel transformer-based approach that ...
  </details>

- **2026-07-08** — Shane Caldwell, Max Harley, Ads Dawson et al. — [ScopeJudge: Cost-Aware Pre-Execution Gating for Offensive Security Agents](http://arxiv.org/abs/2607.07774v1)
  <details><summary>📄 Abstract</summary>
  As LLM agents take on offensive security work, a single out-of-scope tool call can breach a client's engagement boundary, disrupt production, or void a bug-bounty finding. Unlike a fixed safety policy, the boundary that matters is declared in the user's request and must be inferred from intent. That challenge is sharpened by the adversarial nature of offensive security: the same tool call is in or out of scope depending not on the action itself but on the target it touches and the context in whi...
  </details>

- **2026-07-08** — Dongyang Kuang, Zizheng Ma, Yushan Zhang et al. — [Graph-Regularized Deep Learning for EEG-Based Emotion Recognition with Psychologically-Grounded Label Structure](http://arxiv.org/abs/2607.07773v1)
  <details><summary>📄 Abstract</summary>
  EEG-based emotion recognition is critical for mental health monitoring and affective brain-computer interfaces, yet existing deep learning approaches often treat emotion classes as isolated labels, ignoring their psychological interdependencies. We propose a graph-regularized learning framework that conceptualizes emotions as nodes in a graph where edges encode proximity based on dimensional emotion theories. We adapt three complementary regularization strategies--Graph Label Smoothing (intuitiv...
  </details>

- **2026-07-08** — Chenghao Xu, Malcolm Mielle, Olga Fink — [Beyond Thermal Imaging: Inferring Thermophysical Properties from Time-Resolved Thermal Observations](http://arxiv.org/abs/2607.07962v1)
  <details><summary>📄 Abstract</summary>
  Inferring latent physical properties from sensory observations is a fundamental challenge in machine perception. Among available sensing modalities, thermal imaging is particularly promising because temperature evolution is directly governed by heat-transfer physics and therefore encodes information about underlying thermophysical properties of a scene. Recovering spatially resolved thermophysical properties from thermal observations could transform applications ranging from digital twins and in...
  </details>

- **2026-07-08** — Piotr Put, Arjun Pillai, Xuan Hoang Le et al. — [Quantum Sensors for Chemistry and Materials Science](http://arxiv.org/abs/2607.07848v1)
  <details><summary>📄 Abstract</summary>
  The advancement of chemistry and materials science relies on transformative analytical tools which can overcome the sensitivity, spatial resolution, and throughput limitations of conventional techniques. This review explores the application of quantum sensors - specifically optically pumped magnetometers (OPMs) and nitrogen-vacancy (NV) centers in diamond - as robust platforms for molecular and materials analysis. We contrast the extreme magnetic sensitivity of macroscopic OPM ensembles with the...
  </details>

- **2026-07-08** — Dexing Liu — [Agent Delivery Engineering Predictive Reliability Framework](http://arxiv.org/abs/2607.07689v1)
  <details><summary>📄 Abstract</summary>
  Long-horizon LLM multi-agent systems face reliability risks invisible to infrastructure monitoring. We propose the ADE Predictive Reliability Framework (ADE-PRF), enabling proactive health trajectory prediction from passive degradation detection. ADE-PRF aggregates 20 heterogeneous signals across five layers into a Trust Margin (TM) metric (39.2-point dynamic range). Triple-method parallel prediction enables 8-hour forecasts: the Exponential method achieves MAE=1.228, Direction Accuracy=76.8%, w...
  </details>

- **2026-07-08** — Hyunjae Kim, Dain Kim, Pan Xiao et al. — [MedPMC: A Systematic Framework for Scaling High-Fidelity Medical Multimodal Data for Foundation Models](http://arxiv.org/abs/2607.07673v1)
  <details><summary>📄 Abstract</summary>
  Medicine is inherently multimodal, requiring clinicians to synthesize information across diverse data streams. Yet the development of multimodal foundation models is constrained by limited access to large-scale, high-quality clinical data. Although PubMed Central (PMC) offers a complementary source of expert-authored image-text data, existing PMC-derived resources remain limited in fidelity, reproducibility, and clinical validation. We introduce MedPMC, an automated, continuously updatable frame...
  </details>

- **2026-07-08** — Kaicong Huang, Meng Ma, Ruimin Ke — [CARLA-GS: Decoupling Representation, Reasoning, and Physics Simulation for Autonomous Driving Corner-Case Synthesis](http://arxiv.org/abs/2607.07601v1)
  <details><summary>📄 Abstract</summary>
  Safety evaluation for autonomous driving is dominated by rare, safety-critical interactions, motivating simulators that can deliberately synthesize corner cases with photorealistic observations. Corner-case generation is inherently a multi-source problem spanning visual representation, scene reasoning, and vehicle trajectory generation and control. Prior knowledge- and model-based approaches typically focus on scene or trajectory components in isolation, while diffusion-based methods attempt end...
  </details>

- **2026-07-08** — Bojie Li, Noah Shi — [RLVP: Penalize the Path, Reward the Outcome](http://arxiv.org/abs/2607.07435v1)
  <details><summary>📄 Abstract</summary>
  Agents acting on our behalf in the real world (e.g. placing phone calls) must learn online from costly, often irreversible interactions rather than cheap simulator steps. Two things follow. First, deployability depends on the path, not only the outcome. An agent must respect outcome-neutral constraints such as not repeatedly calling an unresponsive user, respecting business hours, or completing required authentication constraints that outcome-based rewards cannot express, since violating them fr...
  </details>

- **2026-07-08** — Zhijin Meng, Francisco Cruz — [Initiation Safety: A Missing Dimension in Generalist-Robot Safety](http://arxiv.org/abs/2607.07420v1)
  <details><summary>📄 Abstract</summary>
  Safety for generalist robots is usually discussed in terms of motion or dialogue. We argue a third question is missing: should the robot take its first hard-to-undo social action at all, such as a greeting, an uninvited grasp, or stepping into someone's space? We call this initiation authorization. Current frameworks rarely treat it as a separate safety layer. Today's stacks often skip this step: a high engagement score or a confident VLA rollout is treated as permission to act. But seeing a per...
  </details>

- **2026-07-08** — Alvina Rwaichi Minja, Jema David Ndibwile — [Evaluating Endpoint Detection Robustness Against Genetic Algorithm Driven Code Transformations](http://arxiv.org/abs/2607.07191v1)
  <details><summary>📄 Abstract</summary>
  Post-compromise test variants are widely used in controlled security evaluation and endpoint robustness benchmarking. However, modern Antivirus (AV) and Endpoint Detection and Response (EDR) systems increasingly combine signature- and behavior-based detection, challenging the reliability of conventional detection pipelines under adaptive variation. This study introduces ShellForge, a Genetic Algorithm (GA)-driven framework that evolves post-compromise variants representative of remote command ex...
  </details>

- **2026-07-08** — Yeonseok Lee — [Separation Logic for Memory Conflict Detection in High-Level Synthesis](http://arxiv.org/abs/2607.07126v1)
  <details><summary>📄 Abstract</summary>
  High-Level Synthesis leverages loop unrolling and array partitioning, but scheduling concurrent accesses is challenging when indices contain non-affine arithmetic. Conventional polyhedral frameworks systematically over-approximate these non-linear transformations, forcing conservative serialization that degrades performance. To minimize this bottleneck, we present a spatial verification framework operating at the LLVM Intermediate Representation (IR) level. By extracting flat arithmetic expressi...
  </details>

- **2026-07-08** — Ruilin Tong, Dong Gong — [MILES: Modular Instruction Memory with Learnable Selection for Self-Improving LLM Reasoning](http://arxiv.org/abs/2607.06974v1)
  <details><summary>📄 Abstract</summary>
  Large language models (LLMs) increasingly improve their reasoning at test time via additional computation, yet most existing works treat each problem in isolation. When problems arrive sequentially, accumulating reusable experience across them can further improve performance. Existing memory-based methods either store whole-solution templates that generalize poorly to novel problems or use heuristic step-level selection that is not optimized for final-answer correctness. Learning selection polic...
  </details>

- **2026-07-08** — Paul F. R. Wilson, Mohamed Harmanani, Zhuoxin Guo et al. — [Compass: Prostate Cancer Detection Needs Multi-View Context](http://arxiv.org/abs/2607.06919v1)
  <details><summary>📄 Abstract</summary>
  Artificial intelligence (AI) analysis of micro-ultrasound ($μ$US) has shown promise for prostate cancer (PCa) detection. However, most existing AI methods focus on the analysis of single $μ$US images in isolation. By contrast, expert $μ$US readers typically assess a full recorded video study, which provides three-dimensional context, to improve PCa detection compared to single-frame analysis. Inspired by this clinical workflow, we propose Compass, a novel AI methodology which models a $μ$US stud...
  </details>

- **2026-07-08** — Jannatul Ferdous, Rafiqul Islam, Md Zahidul Islam — [SA-DRL: Security-Aware Deep Reinforcement Learning for Ransomware Detection with Asymmetric Reward Design](http://arxiv.org/abs/2607.06880v1)
  <details><summary>📄 Abstract</summary>
  Ransomware detection is a security-critical task in which false negatives and false positives have unequal operational consequences. Conventional machine learning detectors often use symmetric objectives that penalize missed ransomware detections and benign false alarms equally, although a false negative can cause irreversible encryption, operational disruption, and high recovery cost, whereas a false positive is usually reversible. This study proposes a Security-Aware Deep Reinforcement Learnin...
  </details>

- **2026-07-08** — Yi-Xiang He, Lan Wei, Haoming Cen et al. — [A Closed-Loop Multi-Agent Framework for Robust Multi-Robot Manipulation](http://arxiv.org/abs/2607.06990v1)
  <details><summary>📄 Abstract</summary>
  Multi-robot systems provide the parallelism and redundancy necessary for long-horizon tasks, while Large Language Models (LLMs) offer the reasoning capabilities to decompose these objectives into actionable plans. However, effectively grounding this high-level reasoning in physical multi-robot execution remains an open challenge. Existing LLM-based approaches fall mainly into two categories: Single-robot methods achieve robust contact-rich manipulation but lack the coordination mechanisms requir...
  </details>

- **2026-07-08** — Shubham Kishore, Alok C. Gupta, Paul J. Wiita et al. — [Detection of Quasiperiodic Oscillations in the Blazar PKS 0735+178 with TESS](http://arxiv.org/abs/2607.07200v1)
  <details><summary>📄 Abstract</summary>
  We report here the detection of signatures of a quasiperiodic oscillation (QPO) and a short flare in the optical light curve of the blazar PKS 0735+178, observed in two sectors, 71 and 72, spanning around 49 days with the Transiting Exoplanet Survey Satellite. The modest flare in sector 71 lasted ~4.3 days and appears as a combination of two sub-flares. In sector 72, a transient QPO with a period ~11.2 hours is detected at local and global significance levels of 4.11$σ$ and 3.06$σ$, respectively...
  </details>

- **2026-07-07** — Heting Mao — [From Application-Layer Simulation to Native Meta-Architecture: Structural Tension as an Endogenous Driver for Heterogeneous AI Evolution](http://arxiv.org/abs/2607.06269v2)
  <details><summary>📄 Abstract</summary>
  Current large language models (LLMs) are stateless across inference sessions: their behavior is fully determined by input at inference time, and any higher-order cognitive architecture must be simulated at the application layer through prompt engineering and context management. This paper proposes a theoretical framework for submerging such application-layer cognitive protocols into a native meta-architecture by introducing three interlocking mechanisms: (1) Structural Tension, an endogenous los...
  </details>

- **2026-07-07** — Haowen Xu, Xue Tan, Lei Ma et al. — [When Agents Go Rogue: Activation-Based Detection of Malicious Behaviors in Multi-Agent Systems](http://arxiv.org/abs/2607.06807v1)
  <details><summary>📄 Abstract</summary>
  While enabling effective collaboration on complex tasks, LLM-based Multi-Agent Systems (MAS) face critical security challenges due to vulnerabilities at the agent and interaction levels. Most existing MAS security defenses are built upon two core assumptions: semantically-explicit malicious attacks and explicit graph-based modeling of the MAS topology and agent-level interactions. In practice, real-world attacks are becoming more semantically stealthy, while MAS execution is typically asynchrono...
  </details>

- **2026-07-07** — Sharayu N. Deshmukh, Md Rashidunnabi, Nelton Tiago Gemo et al. — [VendorBench-100: A Unified Cross-Paradigm Benchmark for Deepfake Image Detection](http://arxiv.org/abs/2607.06254v1)
  <details><summary>📄 Abstract</summary>
  Deepfake image detection is currently served by three fundamentally different paradigms: commercial APIs, zero-shot vision-language models (LLMs), and open-source detectors. Despite their widespread use, these paradigms are rarely evaluated under a common protocol, making direct comparison difficult. We introduce VendorBench-100, a cross-paradigm benchmark that evaluates 36 representative models using a single adversarial 100-image corpus, a unified output schema, and a common evaluation framewo...
  </details>

- **2026-07-07** — Mohammadreza Rashidi — [Unicode TAG-Block Concealment of Tool-Metadata Payloads in the Model Context Protocol: An Approval-View Fidelity Gap Across Three Independent Server Implementations](http://arxiv.org/abs/2607.05744v1)
  <details><summary>📄 Abstract</summary>
  The Model Context Protocol (MCP) is the dominant way coding agents discover and invoke external tools. A server advertises each tool through a tools/list handshake that returns a name, a natural-language description, and a JSON input schema. The client renders this metadata once, in a one-time approval dialog, and then injects it verbatim into the model's context on every subsequent turn. Nothing in the protocol requires the rendered approval view and the bytes delivered to the model to match. W...
  </details>

- **2026-07-07** — Yizhi Wang, Xinghua Gao, Reachsak Ly et al. — [SmartHomeSecure: Automated Detection and Repair of Smart Home Configuration Errors Using Large Language Models](http://arxiv.org/abs/2607.06748v1)
  <details><summary>📄 Abstract</summary>
  Smart home automation platforms increasingly rely on user-authored YAML configuration files to define device behaviors, but these files are prone to syntax, formatting, and semantic logic errors that can cause automation failures and safety risks. Existing YAML validators, static analysis tools, and general-purpose large language models offer limited support for end-to-end diagnosis and repair because they lack domain-specific understanding and validated correction workflows. This paper presents...
  </details>

- **2026-07-07** — He Liu, Changtao Miao, Xinjie Yang et al. — [DT-Guard: Intent-Driven Reasoning-Active Training for Reasoning-Free LLM Safety Guardrail](http://arxiv.org/abs/2607.06326v1)
  <details><summary>📄 Abstract</summary>
  Large language models deployed in open-world applications require safety guardrails that are both robust to complex risks and efficient enough for low-latency runtime moderation. Existing guardrails face a practical trade-off between lightweight classification-based models, which are efficient but often struggle with concealed intent, ambiguous semantics, and borderline safety decisions, and reasoning-based guards, which improve judgment quality but introduce additional token generation and infe...
  </details>

- **2026-07-07** — Heting Mao — [From Application-Layer Simulation to Native Meta-Architecture: Structural Tension as an Endogenous Driver for Heterogeneous AI Evolution](http://arxiv.org/abs/2607.06269v1)
  <details><summary>📄 Abstract</summary>
  Current large language models (LLMs) are fundamentally stateless: their behavior is fully determined by input at inference time, and any higher-order cognitive architecture must be simulated at the application layer through prompt engineering and context management. This paper proposes a theoretical framework for submerging such application-layer cognitive protocols into a native meta-architecture by introducing three interlocking mechanisms: (1) Structural Tension, an endogenous loss function d...
  </details>

- **2026-07-07** — Zongzhe Xu, Aakarsh Anand, Sarah Jiang et al. — [Inertia-1: An Open Exploration of Wearable Motion Foundation Models](http://arxiv.org/abs/2607.06617v1)
  <details><summary>📄 Abstract</summary>
  Wearable motion sensing provides a continuous and scalable window into human behavior and health, making it a natural fit for foundation models, yet its pretraining and scaling principles remain poorly understood. Prior work studies isolated design choices, such as sensor placement or sampling frequency, often under fixed settings and narrow downstream tasks that fail to capture real-world sensing diversity. We introduce Inertia-1, a fully open exploration of wearable motion foundation models. U...
  </details>

- **2026-07-07** — Suneeta Mall, Vladimir Nekrasov, Ashnil Kumar et al. — [Harrison.Rad 1.5 Technical Report: A radiology foundation model that can draft reports from images, priors and clinical context](http://arxiv.org/abs/2607.05880v1)
  <details><summary>📄 Abstract</summary>
  Imaging demand is growing faster than the radiology workforce can expand, and reporting backlogs cannot be resolved through training and recruitment alone. The most direct opportunity is reducing the time and effort radiologists spend producing reports, a task that requires interpreting images, integrating clinical history and prior studies, and drafting structured findings. We present Harrison.Rad 1.5 (HR1.5), a radiology-specific multimodal large language model that accepts interleaved text an...
  </details>

- **2026-07-07** — Tianyuan Zhang, Xianglong Liu, Aishan Liu et al. — [Benchmarking the Robustness of Autonomous Driving to Environmental Illusions: A Lane Perception Perspective](http://arxiv.org/abs/2607.05783v1)
  <details><summary>📄 Abstract</summary>
  Environmental illusions (eg., shadows, reflections, and tire marks) are naturally existing yet overlooked phenomena in real-world driving environments. They can disturb visual perception, leading to misinterpretation of the scene and posing serious safety risks to autonomous driving (AD) systems. However, existing researches largely overlook these phenomena, leaving a critical gap. To address this issue, we study AD robustness through the lane perception perspective, a fundamental task supportin...
  </details>

- **2026-07-07** — Andrii Balashov, Olena Ponomarova — [TriRoute: Unified Learned Routing for Joint Adaptive Attention, Experts, and KV-Cache Allocation](http://arxiv.org/abs/2607.06601v1)
  <details><summary>📄 Abstract</summary>
  Conditional computation can decouple language model quality from per-token inference cost, yet leading techniques act on a single axis in isolation: Mixture-of-Experts (MoE) sparsifies the FFN, Mixture-of-Depths (MoD) skips whole transformer blocks, and KV-cache quantization compresses attention memory. We argue these three decisions (attention resolution, expert selection, and cache bit-width) are strongly coupled and should be made jointly: a token rare enough to warrant full attention may als...
  </details>

- **2026-07-07** — Sishun Liu, Sajal Halder, Ke Deng et al. — [Unsupervised Anomaly Detection of Information Operations Users via Behavioral and Language Patterns](http://arxiv.org/abs/2607.05855v1)
  <details><summary>📄 Abstract</summary>
  Information Operations on social media networks have been identified as a significant threat to democracy and modern society, but they are challenging and expensive to detect by humans. Existing supervised IO detection methods fail to capture the dynamic nature of evolving IO user behavior, while existing unsupervised approaches rely on oversimplified assumptions of coordination among IO users that may not exist in practice. To overcome the limitations of existing methods, we formulate IO user d...
  </details>

- **2026-07-07** — Kien Le, Joseph Lindley, Quoc Bao Phan et al. — [Dual Attention Heads for Personalized Federated Learning in ECG Classification](http://arxiv.org/abs/2607.06653v1)
  <details><summary>📄 Abstract</summary>
  Federated learning (FL) enables collaborative model training across institutions without sharing sensitive patient data. However, the inherent heterogeneity of electrocardiogram (ECG) data across healthcare providers presents significant technical challenges for robust classification. We propose FedDualAtt, a personalized federated learning approach that splits transformer attention heads into global and local branches. Global heads are aggregated via FedAvg to capture shared cross-site patterns...
  </details>

- **2026-07-07** — Md Safwan Mondal, Luca Russo, James D. Humann et al. — [Towards Reliable Aerial Ground Vehicle Collaboration: An Integrated Planning and Autonomy Framework for Field Deployment](http://arxiv.org/abs/2607.07350v1)
  <details><summary>📄 Abstract</summary>
  Limited flight endurance significantly restricts the operational range of unmanned aerial vehicles (UAVs) in long duration missions such as surveillance and inspection, where multiple spatially distributed Areas of Interest (AOIs) must be visited. These tasks require efficient routing determining the sequence of visits which directly impacts mission time, energy consumption, and overall feasibility. Pairing UAVs with unmanned ground vehicles (UGVs) for mobile recharging offers a promising soluti...
  </details>

- **2026-07-07** — Innocent Onyenonachi, Peter J. Lawerance, Nadia Kanwal — [EcoVision: AI-Powered Drone Imaging for Salt Marsh Vegetation Monitoring and Dominance Mapping](http://arxiv.org/abs/2607.06105v1)
  <details><summary>📄 Abstract</summary>
  High-resolution RGB imagery acquired from low-altitude UAV surveys was processed through a modular pipeline incorporating transformer-based semantic segmentation, connected-component vegetation extraction, fine-grained species classification using a ConvNeXt architecture, and grid-based dominance scoring at 2x2m resolution. The framework targeted two ecologically significant halophytic grasses, Spartina maritima and Puccinellia maritima, and was trained using a curated and manually annotated UAV...
  </details>

- **2026-07-07** — Xiaopei Wu, Chenshu Hou, Liang Peng et al. — [PVCap: Towards Accurate 3D Dense Captioning via PseudoCap and VoxelCapNet](http://arxiv.org/abs/2607.06097v1)
  <details><summary>📄 Abstract</summary>
  3D dense captioning, an emerging vision-language task, aims to generate descriptive sentences for each object in the 3D scene. Despite the impressive results achieved by previous methods, they suffer from two limitations. First, current research often employs global rigid transformations, such as rotation, to augment scenes without changing their spatial layouts. However, diverse spatial layouts are crucial for training a 3D dense captioning model to describe spatial relations between objects. S...
  </details>

- **2026-07-07** — Seungwook Lee, David Hyunchul Shim — [Delay-Aware Active Triangulation with Uncertainty-Driven Multi-Agent Reinforcement Learning for Counter-UAS](http://arxiv.org/abs/2607.05957v1)
  <details><summary>📄 Abstract</summary>
  Multi-agent active visual triangulation enables precise 3D localization of aerial targets by coordinating mobile observers with controllable cameras. However, existing methods assume instantaneous state feedback, ignoring cumulative latency from detection, communication, and decision propagation. We present a delay-aware, uncertainty-driven multi-agent reinforcement learning framework for target localization in Counter-UAS applications. Our contributions are: (1) a Dec-POMDP formulation with Age...
  </details>

- **2026-07-07** — Manning Gao, Tingyi Liu, Leheng Zhang et al. — [Uncovering Latent Depression Severity for Binary Depression Detection via Advantage-weighting Ranking](http://arxiv.org/abs/2607.05901v1)
  <details><summary>📄 Abstract</summary>
  Automatic depression detection using audio-visual data faces significant challenges, particularly in disentangling overlapping feature distributions and establishing robust decision boundaries. To address this, we propose a fine-grained multimodal framework featuring a temporal encoder and a mutual transformer to facilitate deep cross-modal fusion. Our core contribution is the Binary Advantage-weighting Ranking Loss, which optimizes the latent space distribution through two complementary mechani...
  </details>

- **2026-07-07** — Yoshitaka Miyahara, Taiki Haga — [Autoencoder-Based Unsupervised Identification of Nonequilibrium Phases in Sheared Binary Colloids](http://arxiv.org/abs/2607.05860v1)
  <details><summary>📄 Abstract</summary>
  Identifying nonequilibrium phases in particle systems remains a major challenge because they often exhibit complex and spatially heterogeneous structures without long-range order. Here, we develop an unsupervised machine-learning framework for classifying such nonequilibrium phases by integrating Fourier-based preprocessing, an autoencoder, and a Gaussian mixture model (GMM). Specifically, we transform global spatial configurations into Fourier space and use the amplitudes of Fourier coefficient...
  </details>

- **2026-07-07** — Praneeth Narisetty, Uday Kumar Reddy Kattamanchi, Shiva Nagendra Babu Kore — [Onnes: A Physics-Grounded Multi-Agent LLM Simulator for Cryogenic Fault Diagnosis in Quantum Computing Infrastructure](http://arxiv.org/abs/2607.05805v1)
  <details><summary>📄 Abstract</summary>
  Dilution refrigerators are the enabling infrastructure of superconducting quantum computers, yet their fault diagnosis is still dominated by threshold alarms that report that something is wrong, not what. We present Onnes, a physics-grounded digital-twin simulator of a dilution refrigerator (a forward physics model with a learned real-fridge noise fingerprint) that drives a live multi-agent LLM operations layer, and use it for a controlled head-to-head between a zero-shot LLM agent panel and a s...
  </details>

- **2026-07-06** — Muhammad Rizwan, David Nabergoj, Jure Demšar — [Population-Level Profiling of DSM-5 Depressive Symptoms Among Self-Reported ADHD and ASD Users on Twitter: An Exploratory Study Using Advanced NLP and Statistical Analysis](http://arxiv.org/abs/2607.05626v1)
  <details><summary>📄 Abstract</summary>
  Background: Depression frequently co-occurs with ADHD and autism spectrum disorder (ASD), but population-level differences in symptom expression between these groups remain underexplored. Objective: We examined whether social media users with ADHD and ASD differ in how they express DSM-5 depressive symptoms in their tweets, and whether differences persist across varying levels of depressive-content filtering. Methods: We analysed 1,282,437 tweets from 792 users (622 ADHD; 170 ASD) with self-repo...
  </details>

- **2026-07-06** — Aditi Naiknaware, Jian Sun, Aminreza Khandan et al. — [Cross-Contextual Vision-Language Adaptation with LoRA for Personalized Severe Adverse Event Detection in Clinical Wound Monitoring](http://arxiv.org/abs/2607.05625v1)
  <details><summary>📄 Abstract</summary>
  Wound monitoring is a critical yet underserved clinical challenge, where timely identification of severe adverse events (SAEs) such as infection, tissue deterioration, and delayed healing can significantly impact patient outcomes. While vision-language models (VLMs) show strong multimodal reasoning, they often lack domain-specific grounding to integrate wound imagery with heterogeneous clinical information, and provide limited mechanisms for detecting cases that diverge from the training distrib...
  </details>

- **2026-07-06** — Bo Huang, Fengxiang Li, Hao Xu et al. — [KAT-Coder-V2.5 Technical Report](http://arxiv.org/abs/2607.05471v1)
  <details><summary>📄 Abstract</summary>
  We present KAT-Coder-V2.5, a coding-focused agentic model trained to act autonomously inside real, executable repositories rather than as a single-turn code generator. Its capability is bottlenecked less by model scale than by the scarcity of reproducible environments, verifiable rewards, and high-value trajectories, which we address with an end-to-end agentic post-training framework. AutoBuilder reconstructs multilingual repositories into sandboxed environments with fail-to-pass and pass-to-pas...
  </details>

- **2026-07-06** — Xiaopu Wang, Zelin He, Chengyuan Liu et al. — [Beyond Heuristic Tuning: Power-Calibrated LLM Watermarking](http://arxiv.org/abs/2607.05694v1)
  <details><summary>📄 Abstract</summary>
  Logit-based watermarking is a widely used mechanism for identifying LLM generated content, yet its effectiveness is governed by a fundamental trade-off between detectability and semantic distortion. Existing analyses provide limited guidance for principled hyperparameter selection, leaving practical deployments reliant on heuristic tuning. In this work, we develop a power-calibrated statistical framework that establishes explicit quantitative relationships between watermark hyperparameters, dete...
  </details>

- **2026-07-06** — Pengfei Zhu, Julien Lecompagnon, Philipp Daniel Hirsch et al. — [Structured Illumination Scanning Thermography (SISTER)](http://arxiv.org/abs/2607.05565v1)
  <details><summary>📄 Abstract</summary>
  Conventional non-invasive photothermal imaging techniques are fundamentally constrained by the diffusive nature of heat transport, which causes severe energy dissipation during subsurface reconstruction. Although modulation-based approaches partially mitigate this limitation by encoding depth information into phase delay and amplitude attenuation, they remain inherently restricted by repeated temporal excitation, long acquisition times, and stitching artifacts in large-area inspection. In this w...
  </details>

- **2026-07-06** — Akshay Gokhale, Mansi Dhamne — [Shape Over Intensity: Directional Topological Encoding for False Positive Reduction in Intracranial Aneurysm Detection](http://arxiv.org/abs/2607.05317v2)
  <details><summary>📄 Abstract</summary>
  Automated detection of intracranial aneurysms (IAs) from CT angiography (CTA) is severely hindered by high false-positive rates. Convolutional neural networks (CNNs) rely on local pixel intensities, causing systematic confusion between saccular aneurysms and vascular bifurcations - a problem especially acute for small lesions (<3 mm), where detection sensitivity falls below 60%. We propose a plug-and-play, topology-aware false-positive reduction framework evaluating the Smooth Euler Characterist...
  </details>

- **2026-07-06** — Xue Qin, Simin Luan, Cong Yang et al. — [Governed Individuation: Cryptographically Decoupling an Agent's Learning from Its Authority](http://arxiv.org/abs/2607.04613v1)
  <details><summary>📄 Abstract</summary>
  Autonomous agents are moving from sandboxed text generators to operators of code, data, and physical infrastructure, and they increasingly learn while deployed. This reopens a question that alignment techniques answer only probabilistically: after an agent has adapted in the field, is the running system still confined to what its operator authorised? Here we show that confinement can be guaranteed as an invariant of the agent's execution architecture rather than a probabilistic outcome of its tr...
  </details>


### 📂 alignment
*对齐与安全约束 / Alignment & Safety Constraints* — 70 papers

- **2026-07-09** — Cheng-De Fan, Chun-Wei Tuan Mu, Chen-Wei Chang et al. — [LongE2V: Long-Horizon Event-based Video Reconstruction, Prediction, and Frame Interpolation with Video Diffusion Models](http://arxiv.org/abs/2607.08770v1)
  <details><summary>📄 Abstract</summary>
  Recovering high-quality video from sparse event streams is a challenging task. Regression methods often blur textures, while existing generative models struggle with long-term stability. We propose LongE2V, a novel approach that leverages pre-trained video diffusion priors to jointly handle event-based video reconstruction, prediction, and frame interpolation. By fine-tuning a foundational video model, our approach achieves high data efficiency and superior perceptual quality. We introduce Autor...
  </details>

- **2026-07-09** — Wenbo Xu, Zhimin Chen, Xiaojie Liang et al. — [HumanForge: A Human-Centric Deepfake Video Benchmark with Multi-Agent Forgery Rationales](http://arxiv.org/abs/2607.08705v1)
  <details><summary>📄 Abstract</summary>
  Rapid advancements in video diffusion models and temporal editing tools have enabled the generation of highly realistic human-centric videos, posing unprecedented challenges to digital content forensics. Existing benchmarks primarily focus on either face-swapping or global text-to-video synthesis, overlooking the crucial dimensions of human-object or human-human interactions and multi-modal alignment. To address these limitations, we introduce HumanForge, a unified, large-scale, and multi-paradi...
  </details>

- **2026-07-09** — Xinlong Zhao, Dongsheng Liu, Hengyu Zhao et al. — [UltraX: Refining Pre-Training Data at Scale with Adaptive Programmatic Editing](http://arxiv.org/abs/2607.08646v1)
  <details><summary>📄 Abstract</summary>
  As available training data approaches its physical limit, gains from Scaling Laws have begun to diminish. Consequently, improving Large Language Models (LLMs) now depends less on data expansion and more on higher-quality data utilization. However, in the context of large-scale corpora, existing refinement methodologies face significant limitations in quality, efficiency, and reliability: Rule-based approaches are constrained by fixed heuristics and struggle with instance-level variations; LLM-ba...
  </details>

- **2026-07-09** — Weiduo Liao, Yunqiao Yang, Ying Wei — [When Structured Sparse Autoencoders Learn Consistent Concepts Across Modalities](http://arxiv.org/abs/2607.08605v1)
  <details><summary>📄 Abstract</summary>
  Sparse autoencoders (SAEs) have emerged as a promising technique for mechanistic interpretability by learning a set of sparse latent features in large models, each of which encodes a distinct concept. However, in vision-language models (VLMs), vanilla SAEs struggle to learn modality-consistent concepts, with concepts often exhibiting fragmented coverage (i.e., disjoint regions) in the visual modality. To address this challenge, we propose a Structured Sparse AutoEncoder ($S^2AE$) that enforces c...
  </details>

- **2026-07-09** — Arav Gupta, Nivedan Yakolli, Avinash Gautam — [Early to Share, Late to Save: Synchronisation-Driven Communication Gating in Bandwidth-Constrained Cooperative VLN](http://arxiv.org/abs/2607.08504v1)
  <details><summary>📄 Abstract</summary>
  Most cooperative Vision-Language Navigation (VLN) methods assume unlimited communication, not considering real-world applications where bandwidth is restricted and information efficiency is critical. We introduce \textbf{bandwidth-constrained cooperative VLN} and propose \textbf{hindsight gating}: a lightweight supervised gate that labels communication-critical steps post-hoc from navigation failures, avoiding the high variance of REINFORCE. Contrary to the intuition that agents should communica...
  </details>

- **2026-07-09** — Shun Liu, Nan Xi, Yang Liu et al. — [Attribute Retrieving for Open-Vocabulary Endoscopic Compositional Referring Segmentation](http://arxiv.org/abs/2607.08397v1)
  <details><summary>📄 Abstract</summary>
  Referring Image Segmentation (RIS) aims to segment image regions specified by natural language, enabling fine-grained and controllable visual understanding. Extending RIS to endoscopic imagery, however, presents unique challenges, including scarce high-quality annotations and complex, domain-specific image-text relationships. Although recent vision-language models demonstrate strong cross-domain alignment, they often fail to capture fine-grained textual cues in endoscopic settings, resulting in ...
  </details>

- **2026-07-09** — Xuerun Yan, Zhexi Lian, Nuoheng Zhang et al. — [WCog-VLA: A Dual-Level World-Cognitive Vision-Language-Action Model for End-to-End Autonomous Driving](http://arxiv.org/abs/2607.08375v1)
  <details><summary>📄 Abstract</summary>
  Vision-Language-Action (VLA) models have advanced end-to-end autonomous driving. However, existing methods either lack comprehensive world cognition or suffer from fragmented world foresight, inherently confining these models to reactive driving. To address this limitation, we propose WCog-VLA, a novel dual-level World-Cognitive VLA framework that successfully bridges semantic world forecasting with generative world evolution to achieve proactive autonomous driving. At the semantic level, WCog-V...
  </details>

- **2026-07-09** — Jing Jie Tan, Ban-Hoe Kwan, Danny Wee-Kiat Ng et al. — [Large-Language-Models-as-a-Judge in Theory-Agnostic Adaptive Metric-Alignment for Prototypical Networks in Personality Recognition](http://arxiv.org/abs/2607.08374v1)
  <details><summary>📄 Abstract</summary>
  Personality recognition has traditionally been constrained by theory-dependent formulations, where models are trained to fit predefined psychological taxonomies rather than uncovering shared underlying behavioral structure. This limits generalization, as personality itself is better understood as theory-invariant, while existing annotations reflect only partial and sometimes inconsistent views of the same latent traits. In this work, we introduce JAM ((J)udge for (A)daptive (M)etric-Alignment), ...
  </details>

- **2026-07-09** — Fengyuan Liu, Yuchen Fu, Yuqi Wang et al. — [XALPHA: A Memory-Driven AI Quant Researcher for Hypothesis-to-Code Alpha Discovery](http://arxiv.org/abs/2607.08332v1)
  <details><summary>📄 Abstract</summary>
  Financial markets are noisy, non-stationary, and high-dimensional, making it difficult to discover predictive and robust trading signals. Alpha discovery has evolved from manual factor design to machine learning, evolutionary search, and recent LLM-based frameworks, improving the efficiency of factor generation, search, and evaluation. However, existing methods still mostly automate isolated steps, rather than functioning as end-to-end quant researchers that can absorb external knowledge, close ...
  </details>

- **2026-07-09** — Ludovica de Paolis, Marco Baroni, Alessandro Laio et al. — [Texture Representations in Deep Vision Models: Comparing CNNs, Vision Transformers, and Human Perception](http://arxiv.org/abs/2607.08321v1)
  <details><summary>📄 Abstract</summary>
  In computational vision science, Convolutional Neural Networks (CNNs) have emerged as a popular model of biological vision because of the alignment they can exhibit with neural and behavioral data in humans and animals. However, it remains unclear to what extent this alignment persists for visual tasks that extend beyond the canonical object recognition paradigm based on well defined semantic content. In this study, we diverge from the common object-centric view by focusing on another aspect of ...
  </details>

- **2026-07-09** — Yuming Yang, Xiao Sun, Yuanwei Zou et al. — [MentalHospital: A Virtual Environment for Evaluating Psychiatric Clinical Encounters](http://arxiv.org/abs/2607.08257v1)
  <details><summary>📄 Abstract</summary>
  Large language models (LLMs) have shown strong performance on isolated psychiatric tasks, including dialogue, diagnosis, and treatment planning, yet existing benchmarks rarely simulate complete psychiatric clinical encounters. We introduce $\textbf{MentalHospital}$, a virtual evaluation environment for LLM-based psychiatric clinical encounters. MentalHospital instantiates the Subjective Interviewing, Objective Examination, Diagnostic Assessment, and Treatment Planning (S.O.A.P.) workflow, using ...
  </details>

- **2026-07-09** — Zheng Yu — [On the Limitations of Non-GPU AI Accelerators for Large-Model Inference: A Field Study of MoE and Multimodal Serving on Huawei Ascend](http://arxiv.org/abs/2607.08215v1)
  <details><summary>📄 Abstract</summary>
  Non-GPU AI accelerators are increasingly adopted as alternatives to general-purpose GPUs for large-model inference, but the real engineering cost of migrating demanding workloads beyond CUDA remains poorly documented. We present a field study of deploying two large inference workloads on a 16-device Huawei Ascend 910 system using CANN and vLLM-Ascend: an LLM-as-a-judge safety and alignment evaluation pipeline based on a W8A8 MoE judge model, DeepSeek-V4-Flash, and a multimodal medical vision--la...
  </details>

- **2026-07-09** — Mingjia Shi, Shuo Wang, Xiaobo Wang et al. — [Dive Into the Implicit Biases of Low-rank Vision-language Alignment](http://arxiv.org/abs/2607.08194v1)
  <details><summary>📄 Abstract</summary>
  Vision-language alignment, the stage that bridges pretrained vision encoders and large language models, is widely treated as a form of pretraining requiring full-parameter updates. We challenge this view and investigate what happens when low-rank adaptation is applied to the LLM during this stage instead. We find that low-rank alignment not only reduces computational costs but also outperforms full-parameter alignment on most benchmarks. To understand this phenomenon, we systematically character...
  </details>

- **2026-07-09** — Yidong Ouyang, Zhe Wang, Sourav Bhabesh et al. — [Reinforcing the Generation Order of Multimodal Masked Diffusion Models](http://arxiv.org/abs/2607.08056v1)
  <details><summary>📄 Abstract</summary>
  Diffusion Language Models (DLMs) have recently achieved substantial progress in natural language generation tasks. Recent research demonstrates that adaptive token generation ordering can significantly improve performance in mathematical reasoning and code synthesis applications. In this work, we investigate the optimization of generation order for both text-to-image synthesis and multimodal understanding. We first establish that, unlike structured problems in language generation such as Sudoku ...
  </details>

- **2026-07-09** — Samuel Tetteh, Udip Shrestha, Joshua R. Waite et al. — [Who Analyses the Analyser? Self-Validating LLM Hazard Analysis with Constitutional Meta-STPA](http://arxiv.org/abs/2607.08054v1)
  <details><summary>📄 Abstract</summary>
  Large language models (LLMs) are increasingly trusted to draft the artifacts of safety analysis such as, losses, hazards, Unsafe Control Actions (UCAs), and safety constraints, inside rigorous processes such as Systems-Theoretic Process Analysis (STPA). Yet a blind spot runs through this fast-growing literature: every system gets analysed except the LLM-assisted tool doing the analysing, which is itself a safety-relevant system that can hallucinate standards, emit unverifiable constraints, and l...
  </details>

- **2026-07-09** — Kshitij Dani, Cordero Core, Landung Setiawan et al. — [Aleena: Alignment Agent for Research Software Engineering Collaborations](http://arxiv.org/abs/2607.08043v1)
  <details><summary>📄 Abstract</summary>
  Research software collaborations span meetings, informal chats, pull requests, and GitHub issues. A decision surfaced in a Slack thread, refined in a meeting, and implemented in a pull request can lose its original rationale across these artifacts, leaving domain researchers and research software engineers with divergent mental models of project intent, ownership, and scientific assumptions. We argue that alignment in research software engineering is a continuous lifecycle problem, and that agen...
  </details>

- **2026-07-09** — Dhruv Agarwal, Anya Shukla, Tanya Goyal et al. — [PLURAL: A Global Dataset for Value Alignment](http://arxiv.org/abs/2607.08034v1)
  <details><summary>📄 Abstract</summary>
  Large language models (LLMs) are used worldwide, yet disproportionately reflect Western values, limiting their ability to represent diverse value systems. We introduce PLURAL, a large-scale, value-focused preference dataset grounded in the Integrated Values Survey (IVS), a nationally representative survey spanning 92 countries. Using a two-stage generation pipeline, we transform survey responses into synthetic preference triplets that preserve normative value signals while producing realistic sc...
  </details>

- **2026-07-09** — Hyeju Shin, Chorwon Kim, Ryangsoo Kim et al. — [Rethinking Small VLM Quantization: From Component-Wise Analysis to Hardware-Aware Edge Deployment](http://arxiv.org/abs/2607.08029v1)
  <details><summary>📄 Abstract</summary>
  The emergence of vision language models with fewer than 3 billion parameters has accelerated the implementation of on-device multimodal intelligence. However, a detailed understanding of component-wise quantization remains a bottleneck for optimal deployment. This paper presents a systematic evaluation framework for empirically validating five hypotheses across six quantization configurations on the Jetson Orin NX and AGX. By separating the vision encoder, projector, and large language model bac...
  </details>

- **2026-07-09** — Ryota Kobayashi, Tsubasa Hirakawa, Takayoshi Yamashita et al. — [Structured Pruning of Large Language Models via Power Transformation and Sign-Preserving Score Aggregation with Adaptive Feature Retention](http://arxiv.org/abs/2607.08027v1)
  <details><summary>📄 Abstract</summary>
  This paper proposes an improved structured pruning method for large language models (LLMs) that addresses key challenges in adapting Adaptive Feature Retention (AFR), an unstructured pruning technique, to structured pruning. When applying AFR to structured pruning, three major problems arise: distribution mismatch between heterogeneous pruning scores, loss of sign information indicating optimization direction consistency, and influence of outliers. To address these issues, we propose a unified a...
  </details>

- **2026-07-09** — Lu Dai, Ziyang Rao, Yili Wang et al. — [Towards Mechanistically Understanding Why Memorized Knowledge Fails to Generalize in Large Language Model Finetuning](http://arxiv.org/abs/2607.08393v1)
  <details><summary>📄 Abstract</summary>
  Fine-tuning LLMs to inject new knowledge faces a critical challenge: LLMs can quickly memorize new facts, yet fail to use them for downstream reasoning tasks. We formalize this failure as the \textit{\textbf{Knowing--Using Gap}}, characterized by an accuracy gap and a temporal lag between memorization and generalization. To understand this phenomenon, we fine-tune LLMs with unseen knowledge and monitor the spatial permeation dynamics of the knowledge internally using a novel intervention techniq...
  </details>

- **2026-07-08** — Paul Dela Cruz, Mostafa Mo. Massoud, Jacqueline Libby — [Soft Robotic Exogloves for Dexterous Mobility -- Towards Personalized Rehabilitation](http://arxiv.org/abs/2607.07968v1)
  <details><summary>📄 Abstract</summary>
  Soft robotic exogloves can provide hand rehabilitation and assistance. Fitting these gloves often relies on standardized measurements not tailored to the individual, limiting their effectiveness, especially for fine articulation necessary for dexterous manipulation. We present the design, fabrication, modeling, and testing of a personalized pneumatically-actuated soft robotic exoglove. The glove was fit to a user's hand with topological scans and fabricated with silicone mold casting. Finite ele...
  </details>

- **2026-07-08** — Benjamin Poole, Minwoo Lee — [Feedback Manipulation Regularization: Enabling Offline Agent Alignment for Imitation Learning](http://arxiv.org/abs/2607.07859v1)
  <details><summary>📄 Abstract</summary>
  Reinforcement learning (RL) research has increasingly shifted focus towards alignment, ensuring agents learn behaviors adhering to human values. While human demonstrations and feedback have proven crucial for alignment, existing approaches predominantly combine these signals using multi-stage pipelines designed for the contextual bandit framing of language generation. Yet little work explores how these complementary inputs can serve as a richer, interconnected signal for single-stage offline tra...
  </details>

- **2026-07-08** — Gwydion Williams, Sara Zannone, Bilal A Mateen — [Alignment Plausibility: A New Standard for Assuring AI in Healthcare](http://arxiv.org/abs/2607.07766v1)
  <details><summary>📄 Abstract</summary>
  Large language models (LLMs) have become significant providers of mental health support, yet they remain products of an attention economy whose operational and commercial targets favour sustained engagement over the friction that effective psychological support often requires. Developers' safety responses have been largely reactive, addressing the most visible and acute harms while subtler, longer-term patterns of risk (e.g., dependency, boundary erosion, the amplification of distorted beliefs) ...
  </details>

- **2026-07-08** — Jianyi Zhou, Feiyang Hong, Yunhao Li et al. — [TouchWorld: A Predictive and Reactive Tactile Foundation Model for Dexterous Manipulation](http://arxiv.org/abs/2607.07287v2)
  <details><summary>📄 Abstract</summary>
  Dexterous manipulation in everyday environments requires both anticipation and reaction: a robot must predict how contact should evolve while rapidly correcting local errors caused by slip, misalignment, unstable grasping, or force mismatch. Vision and language provide semantic and geometric guidance, but they cannot reliably reveal hidden contact states such as force, slip, and contact stability. Although tactile sensing exposes these physical cues, most existing policies treat touch as a low-f...
  </details>

- **2026-07-08** — Marcus Williams, Hannah Sheahan, Cameron Raymond et al. — [Predicting LLM Safety Before Release by Simulating Deployment](http://arxiv.org/abs/2607.07184v1)
  <details><summary>📄 Abstract</summary>
  Pre-deployment safety evaluations aim to inform the downstream risks of releasing a new AI model. Yet most evaluations provide limited evidence about how often undesired model behavior will occur in deployment: they generally have insufficient coverage, are unrepresentative, and are generally recognizable as tests. To address these concerns, we study a simple way to simulate a model deployment: starting from de-identified conversations from a previous model deployment, we hold fixed the initial ...
  </details>

- **2026-07-08** — Eric Zhu, Abhinav Shrivastava, Soumik Mukhopadhyay — [Selective Timestep Weighting and Advantage-Based Replay for Sample-Efficient Diffusion RLHF](http://arxiv.org/abs/2607.07693v1)
  <details><summary>📄 Abstract</summary>
  Reinforcement learning from human feedback (RLHF) has emerged as a powerful paradigm for aligning generative models with human preferences. However, applying RLHF to diffusion models remains highly feedback inefficient, as existing approaches typically require large amounts of human or reward model evaluations. This limitation reduces the practicality of diffusion RLHF in realworld settings where feedback is the primary bottleneck. In this paper, we propose two complementary strategies that subs...
  </details>

- **2026-07-08** — Shuailei Ma, Jiaqi Liao, Xinyang Wang et al. — [Scaling Mixture-of-Experts Video Pretraining for Embodied Intelligence](http://arxiv.org/abs/2607.07675v1)
  <details><summary>📄 Abstract</summary>
  Despite the recent promise in robot control, video generative models suffer from a domain mismatch due to their primary focus on content creation. For example, their design inherently prioritizes visual fidelity and creativity over computational efficiency and physical realism. In this work, we present LingBot-Video, a DiT-based video pretraining paradigm specifically tailored for embodied intelligence. From the architecture perspective, we adopt the Mixture-of-Experts (MoE), instead of dense, f...
  </details>

- **2026-07-08** — Jordan Painter, Dipankar Srirag, Adarsh Kappiyath et al. — [DiaLLM: An Investigation into the Robustness-Generation Gap in English Dialect Adaptation](http://arxiv.org/abs/2607.07669v1)
  <details><summary>📄 Abstract</summary>
  Large language models increasingly \emph{understand} dialectal English, yet still \emph{produce} only standard, US-leaning English, leaving dialectal generation, the harder half of the problem, largely unaddressed. We introduce \textbf{DiaLLM}, which continually pretrains three open-weight language model families on the International Corpus of English and applies implicit and explicit post-training paradigms, each combined with three model alignment strategies, giving the first controlled compar...
  </details>

- **2026-07-08** — Willem Fourie, Isabel Ray, Gray Manicom — [User identity conditions moral wrongness ratings in non-reasoning large language models](http://arxiv.org/abs/2607.07605v1)
  <details><summary>📄 Abstract</summary>
  This study adopts a behavioural bottom-up approach to AI value alignment to investigate whether an implicitly conveyed user identity shifts the moral evaluations of large language models (LLMs). Through a structured, multi-turn conversational protocol across 12,000 interactions, we evaluate AI value alignment in two non-reasoning models, gpt-4.1-mini-2025-04-14 and gemini-2.5-flash-lite. Rather than instructing the models to adopt a persona or prompting them with explicit moral stances, the user...
  </details>

- **2026-07-08** — Daeun Song, Nhat Le, Jeffrey Chen et al. — [HumAIN: Human-Aware Implicit Social Robot Navigation](http://arxiv.org/abs/2607.07357v1)
  <details><summary>📄 Abstract</summary>
  Effective social robot navigation requires sensitivity to human behavior, often revealed through subtle skeletal cues like gait and orientation. We present Human-Aware Implicit Social Robot Navigation (HumAIN), a novel framework that fuses implicit social cues directly into the planning loop via knowledge distillation. We first employ a transformer-based teacher model that fuses rich multi-modal inputs, including historic images, skeletal keypoints, robot state, and a robot's target goal, to lea...
  </details>

- **2026-07-08** — Georg Schäfer, Jakob Rehrl, Stefan Huber et al. — [Safe Reinforcement Learning using Ideas from Model Predictive Control](http://arxiv.org/abs/2607.07252v1)
  <details><summary>📄 Abstract</summary>
  Reinforcement learning (RL) enables the synthesis of control policies directly from data, making it highly appealing for complex cyber-physical systems (CPSs) and robotics. A persistent challenge, however, is ensuring strict, hard safety constraints during the active learning phase. In real-world physical systems, violating mechanical limits can cause irreversible damage, necessitating that exploration remains strictly within safe operational regions. We propose a generalized framework that comb...
  </details>

- **2026-07-08** — Waqas Arshid, Mohammad Awrangjeb, Alan Wee-Chung Liew et al. — [`Attention-Guided Cross-Temporal Clustering for Self-Supervised Video Object Segmentation](http://arxiv.org/abs/2607.07230v1)
  <details><summary>📄 Abstract</summary>
  Video object segmentation (VOS) is a fundamental task in video understanding, requiring accurate delineation and consistent tracking of objects across frames. While supervised methods achieve strong performance, they rely on densely annotated datasets that are costly to obtain and have limited domain coverage. Self-supervised learning offers a promising alternative by removing the need for manual labels; however, existing approaches often struggle to jointly maintain spatial accuracy and tempora...
  </details>

- **2026-07-08** — Alejandro Vergara-Richart, Xavier Rafael-Palou, Almudena Fuster-Matanzo et al. — [Vision Foundation Models in Radiology: A Scoping Review of Data, Methodology, Evaluation and Clinical Translation](http://arxiv.org/abs/2607.07219v1)
  <details><summary>📄 Abstract</summary>
  Vision foundation models (VFMs) are increasingly being developed for radiological imaging, yet their definition, development and evaluation remain heterogeneous. We conducted a PRISMAScR scoping review of peer-reviewed studies published between January 2017 and March 2026 describing foundation models trained exclusively on radiological imaging data. Sixty-seven studies were included and mapped across three pillars: data scale and heterogeneity, architectural and pretraining scalability, and down...
  </details>

- **2026-07-08** — Wenyan Xu, Alizer Wong — [Stage-Aware Adaptation and Distribution Calibration for Subject-Driven Personalized Text-to-Image Generation](http://arxiv.org/abs/2607.07173v1)
  <details><summary>📄 Abstract</summary>
  Subject-driven personalized text-to-image generation requires a pretrained diffusion model to acquire a specific subject from a few reference images while preserving subject identity, following novel text prompts, and maintaining sample diversity. Existing optimization-based methods instantiate subject adaptation through full fine-tuning, textual embedding optimization, or low-rank parameter updates; PaRa further constrains personalization from the perspective of parameter rank reduction. Howeve...
  </details>

- **2026-07-08** — Yi Yang, Siyuan Liu, Xin Gao et al. — [Learning social norms enhances compatibility in dynamic human-AI coordination](http://arxiv.org/abs/2607.07021v1)
  <details><summary>📄 Abstract</summary>
  Humans continuously coordinate with others in dynamic interactions, often through implicit, hard-to-quantify social norms that act as shared tacit expectations among interacting agents. As AI agents, including large language models (LLMs), become embedded in daily life, they increasingly participate in such interactions and reshape social interaction structures. Yet they often fail to coordinate with humans in an effective, considerate, and natural manner. We hypothesize that this gap arises bec...
  </details>

- **2026-07-08** — Jianyi Zhou, Feiyang Hong, Yunhao Li et al. — [TouchWorld: A Predictive and Reactive Tactile Foundation Model for Dexterous Manipulation](http://arxiv.org/abs/2607.07287v1)
  <details><summary>📄 Abstract</summary>
  Dexterous manipulation in everyday environments requires both anticipation and reaction: a robot must predict how contact should evolve while rapidly correcting local errors caused by slip, misalignment, unstable grasping, or force mismatch. Vision and language provide semantic and geometric guidance, but they cannot reliably reveal hidden contact states such as force, slip, and contact stability. Although tactile sensing exposes these physical cues, most existing policies treat touch as a low-f...
  </details>

- **2026-07-07** — Nicolas Koller, Andreas u. Schmidt — [REFORGE: A Method for Benchmarking LLMs' Reverse Engineering Capabilities in Decompiled Binary Function Naming](http://arxiv.org/abs/2607.07738v1)
  <details><summary>📄 Abstract</summary>
  Large language models (LLMs) are increasingly applied to reverse-engineering tasks, and recent threat-intelligence reporting shows them operating inside live offensive-security workflows. Claims about their capability, however, outpace our ability to measure it. Existing benchmarks for LLM-assisted binary analysis treat the construction of function-level ground truth as a solved pre-processing step and report accuracy without disclosing how many functions were reliably evaluable. We argue that t...
  </details>

- **2026-07-07** — Zhenyu Liu, Xuanyu Zhang, Yunxin Li et al. — [Hierarchical Acoustic-Semantic Modeling: Modality Separation and Semantic Coherence for Full-Duplex SLMs](http://arxiv.org/abs/2607.06540v2)
  <details><summary>📄 Abstract</summary>
  Developing seamless, high-performance, native intelligent full-duplex Spoken Language Models (SLMs) remains a critical challenge and long-standing goal for the speech and NLP community. Despite notable progress, recent endeavors are fundamentally constrained by severe modality interference, which causes substantial knowledge degradation and compromises semantic integrity -- ultimately making full-duplex SLMs feel unnatural and unintelligent. In this paper, through an exhaustive fine-grained anal...
  </details>

- **2026-07-07** — Phat Tran, Artin Lahni, Pranav Kulkarni et al. — [Is Domain Adaptation Always Helpful? A Frozen-Backbone Study of Cross-Domain Sentiment Transfer](http://arxiv.org/abs/2607.05937v1)
  <details><summary>📄 Abstract</summary>
  Sentiment analysis with frozen pre-trained language model (PLM) backbones has become a common paradigm, yet the practical benefit of explicit domain adaptation remains unclear, particularly when backbones encode varying degrees of target-domain knowledge. We present a preliminary case study evaluating a controlled family of frozen embedding backbones (Qwen3-Embedding 0.6B, 4B, 8B), alongside RoBERTa-base and FinBERT. We train a lightweight MLP adapter on consumer reviews using Domain-Adversarial...
  </details>

- **2026-07-07** — Michael King, Aravindh Mahendran, Matthew Koichi Grimes et al. — [Gen4U: Unifying Video Generation and Understanding via Diffusion](http://arxiv.org/abs/2607.06856v1)
  <details><summary>📄 Abstract</summary>
  Prior work suggests that diffusion representations capture low-level geometry but struggle with high-level semantics. We demonstrate that state-of-the-art video diffusion models overcome this limitation. By systematically probing their intermediate activations using recent mutual-kNN alignment metrics, we reveal a highly structured latent space where visual representations evolve across both network depth and noise levels. We show that while moderate noise levels yield linearly separable global ...
  </details>

- **2026-07-07** — Albert Zeyer, Ralf Schlüter, Hermann Ney — [Gradient-Based Speech-to-Text Alignment for Any ASR Model: From CTC to Speech LLMs](http://arxiv.org/abs/2607.06831v1)
  <details><summary>📄 Abstract</summary>
  Speech-to-text alignment means finding the temporal boundaries of each word in the audio. Some models provide such an alignment directly and others do not. Connectionist temporal classification (CTC) and transducer models have an alignment by construction, whereas attention-based encoder-decoders (AED) and speech large language models (LLMs) do not, and their word timings are usually read off the attention weights instead. All of these signals live on the encoder frame grid, which bounds their t...
  </details>

- **2026-07-07** — Tianjiao Yu, Xinzhuo Li, Yifan Shen et al. — [ELSA3D: Elastic Semantic Anchoring for Unified 3D Understanding and Generation](http://arxiv.org/abs/2607.06565v1)
  <details><summary>📄 Abstract</summary>
  Unified 3D foundation models aspire to generate 3D assets and reason about them in language within a single backbone, but their text-3D interaction remains largely implicit. Existing methods concatenate text and 3D tokens into a flat sequence and rely on self-attention, collapsing coarse structural cues and fine geometric details into one undifferentiated representation. We introduce ELSA3D, a unified 3D model that addresses this with elastic semantic anchoring, structuring language and geometri...
  </details>

- **2026-07-07** — Zhenyu Liu, Yunxin Li, Xuanyu Zhang et al. — [Hierarchical Acoustic-Semantic Modeling: Modality Separation and Semantic Coherence for Full-Duplex SLMs](http://arxiv.org/abs/2607.06540v1)
  <details><summary>📄 Abstract</summary>
  Developing seamless, high-performance, native intelligent full-duplex Spoken Language Models (SLMs) remains a critical challenge and long-standing goal for the speech and NLP community. Despite notable progress, recent endeavors are fundamentally constrained by severe modality interference, which causes substantial knowledge degradation and compromises semantic integrity -- ultimately making full-duplex SLMs feel unnatural and unintelligent. In this paper, through an exhaustive fine-grained anal...
  </details>

- **2026-07-07** — Han-Jun Ko, Jr-Jen Chen, Haobo Yuan et al. — [Bridging Physical Reasoning and Task Generalization via Visual Action Outcome Reasoning Alignment](http://arxiv.org/abs/2607.06522v1)
  <details><summary>📄 Abstract</summary>
  Vision-language models (VLMs) struggle to generalize in interactive physical reasoning, particularly under unseen tasks and environments. Two key failure modes are prominent: hallucinated chain-of-thought (CoT) reasoning that contradicts physical reality, and misalignment between the model's reasoning and actions. We present VAORA (Visual Action Outcome Reasoning Alignment), a novel reward design that directly addresses both issues. VAORA introduces two complementary rewards: Visual Alignment Re...
  </details>

- **2026-07-07** — Anna Córdoba, Adam Puente Tercero, Nerea Angulo Hijo et al. — [Prompt-Adapter Context Routing for Parameter-Efficient Multi-Shot Long Video Extrapolation](http://arxiv.org/abs/2607.06481v1)
  <details><summary>📄 Abstract</summary>
  We present PACR-Video, a parameter-efficient framework for multi-shot long video extrapolation that preserves recurring entities, scene structure, visual style, and causal progression without full generator fine-tuning. PACR-Video keeps a text-to-video diffusion transformer frozen and augments it with low-rank temporal adapters conditioned by learned shot-role prompt tokens. To maintain long-horizon coherence, it builds a recursive prompt bank that stores compact entity, location, action, and st...
  </details>

- **2026-07-07** — Sihang Nie, Jinxin Ji, Xiaofen Xing et al. — [WordVoice: Explicit and Decoupled Multi-Dimensional Word-Level Control for LLM-Based TTS](http://arxiv.org/abs/2607.06461v1)
  <details><summary>📄 Abstract</summary>
  While recent Large Language Model (LLM)-based Text-to-Speech (TTS) systems have achieved remarkable naturalness, they predominantly rely on implicit end-to-end generation paradigms, resulting in coarse-grained control. In scenarios demanding precise stylistic interventions and strict temporal alignment, such as audiobook narration and video dubbing, the inability to explicitly manipulate word-level acoustic attributes remains a critical bottleneck. This limitation is primarily amplified by the s...
  </details>

- **2026-07-07** — Thanh V. T. Tran, Ngoc-Son Nguyen, Luong Tran et al. — [Precise Video-to-Audio Generation with Cross-Modal Alignment in Latent Space](http://arxiv.org/abs/2607.06405v1)
  <details><summary>📄 Abstract</summary>
  Video-to-audio (V2A) generation aims to synthesize realistic audio that is both semantically consistent with and temporally synchronized to a silent video. Despite recent progress, many methods still rely on multi-stage training, resulting in high computational costs and long runtimes, or transform visual input into text to leverage pretrained text-to-audio models, sacrificing fine-grained temporal cues. To overcome these limitations, we propose Flowley, an end-to-end, single-stage training arch...
  </details>

- **2026-07-07** — Erica Lastufka, Mariia Drozdova, Svyatoslav Volosynovskiy — [Exploring Image-Text Alignment for Radio Galaxy Morphologies](http://arxiv.org/abs/2607.06305v1)
  <details><summary>📄 Abstract</summary>
  We investigate whether specially constructed text captions can capture the same morphological information as radio galaxy images. Using the MiraBest dataset, we generate captions with a domain-specific prompt and evaluate their alignment with images through the SigLIP-2 vision--language model, with and without LoRA fine-tuning. Results show that caption-based classification of FR-I and FR-II galaxies performs similarly to images, with fine-tuning improving local coherence of embeddings but not g...
  </details>

- **2026-07-07** — Xinda Liu, Qinyu Zhang, Weiqing Min et al. — [Structured-Condensed Prompt Tuning in Vision-Language Models for Fine-grained Image Recognition](http://arxiv.org/abs/2607.06185v1)
  <details><summary>📄 Abstract</summary>
  Fine-grained image recognition poses a significant challenge due to the substantial expertise and effort required for manual annotation. Vision-language models (VLMs) like CLIP provide a compelling zero-shot alternative, reducing reliance on extensive labeled data. However, their ability to capture subtle distinctions remains limited, leading to subpar recognition performance. While prompt tuning has proven effective for adapting VLMs, most existing methods treat class labels as isolated, discre...
  </details>

- **2026-07-07** — Jie Huang, Pengfei Yin, Zihan Xu et al. — [X-FEMR: A Token-level Explainable Approach for Electronic Health Records Foundation Models using Transformer-based Models](http://arxiv.org/abs/2607.06163v1)
  <details><summary>📄 Abstract</summary>
  Foundation Models for Electronic Health Records (FEMRs) are pretrained on large-scale structured patient data, enabling them to convert longitudinal patient trajectories into generalizable representations for diverse clinical prediction tasks. Despite their effectiveness, FEMRs remain black-box models, raising concerns about bias, interpretability, and clinical trust. To address this, we propose the first token-level explainability approach for FEMRs. We train a Transformer-based surrogate model...
  </details>

- **2026-07-07** — Youcheng Zong, Runda Jia, Mingxuan Ren et al. — [LLM-Guided Task-Semantic Field Factorization for Industrial Process Forecasting](http://arxiv.org/abs/2607.06623v1)
  <details><summary>📄 Abstract</summary>
  Process industries rely on time-series forecasting and soft sensing to estimate quality variables that are hard to measure online. Labeled data are scarce, operating regimes change frequently, and retraining models or rebuilding alignment pipelines for each scenario is costly. Such settings often provide variable tables and process documents that record variable names, units, physical meanings, and process roles. However, standard time-series backbones usually treat inputs as anonymous numerical...
  </details>

- **2026-07-07** — Wei Dong, Tianyu Fu, Zhe Yu et al. — [WebRetriever: A Large-Scale Comprehensive Benchmark for Efficient Web Agent Evaluation](http://arxiv.org/abs/2607.06118v1)
  <details><summary>📄 Abstract</summary>
  As web agents increasingly demonstrate capabilities in automated task execution, the development of robust evaluation frameworks for assessing their navigation and task completion performance has emerged as a critical research priority. However, existing benchmarks exhibit fundamental limitations. First, they suffer from insufficient scale and limited domain diversity, constraining comprehensive evaluation of cross-domain generalization. Second, prevailing LLM-as-Judge evaluation methodologies i...
  </details>

- **2026-07-07** — Anastasia Zorkina, Alexandr Anikin, Nikita Khmelev et al. — [Flow Matching-Based Speech Source Separation with Best-of-N Biometric Sampling](http://arxiv.org/abs/2607.06088v1)
  <details><summary>📄 Abstract</summary>
  Single-channel speech separation remains challenging for real-world deployment due to source permutation ambiguity, sampling variability of generative models, and the difficulty of processing long recordings with chunk-wise inference. We address these issues with a conditional flow-matching-based method that produces an ordered two-source output conditioned on the mixture. A frozen speaker encoder defines the source order during training and is reused at inference for biometric best-of-$N$ candi...
  </details>

- **2026-07-07** — Shiyi Ling, Zhi Zheng, Hui Zheng et al. — [From Blueprint to Reality: Modeling and Applying Putnam's Social Capital Theory with LLM-based Multi-agent Simulations](http://arxiv.org/abs/2607.06080v1)
  <details><summary>📄 Abstract</summary>
  Putnam's Social Capital Theory is a foundational framework for collective action and community prosperity. However, traditional empirical methods face practical limits on control and replication. Meanwhile, LLM-based social simulations are typically behavior-driven and lack theory-aligned environments for modeling Putnam's core propositions. To address these gaps, we introduce SocaSim, an LLM-based multi-agent simulation framework to study Putnam's Social Capital Theory from theoretical blueprin...
  </details>

- **2026-07-07** — Tihomir Rohlinger, Daniel Ratiu, Stefan Wagner — [Automating Quality Assessment with NLP of LLM-Generated Defeaters](http://arxiv.org/abs/2607.06039v1)
  <details><summary>📄 Abstract</summary>
  High-integrity systems, such as autonomous vehicle fleets and large-scale energy infrastructures, rely on structured assurance cases to justify safety claims. To remain valid under evolving operational conditions, such cases must be examined against potential challenges, known as defeaters. While large language models (LLMs) can support the scalable generation of candidate defeaters, assessing their quality remains largely manual and subjective process. This paper presents an automated approach ...
  </details>

- **2026-07-07** — Zheng Guo, Jiaqi Cui, Haocheng Xiong et al. — [KOAL: Knowledge-Driven Prostate Cancer Grading with Ordinal-Aware Learning](http://arxiv.org/abs/2607.06019v1)
  <details><summary>📄 Abstract</summary>
  Non-invasive prediction of Gleason Grade Group (GGG) in prostate cancer using multiparametric MRI (mpMRI) is clinically vital for reducing unnecessary biopsies. Existing GGG prediction methods face two major limitations. First, they often overlook non-image information critical for GGG prediction, including age, prostate-specific antigen (PSA), and expert priors embedded in radiology reports. Second, they tend to oversimplify GGG as flat categorical labels, failing to account for its intrinsic h...
  </details>

- **2026-07-07** — Niels Potters, Theo Hofman — [Auto-DSM Under the Lens: A Black-Box Evaluation Framework for LLM-Based DSM Generation](http://arxiv.org/abs/2607.05985v1)
  <details><summary>📄 Abstract</summary>
  This paper presents a black-box evaluation framework to systematically assess the ability of Large Language Models (LLMs) to generate Design Structure Matrices (DSMs) from structured technical documentation. Motivated by the closed-source nature of current Auto-DSM pipelines, the framework introduces a reproducible methodology that benchmarks generated DSMs (GEN-DSMs) against manually validated ground-truth matrices (GT-DSMs). The evaluation integrates both single-run and multi-run perspectives,...
  </details>

- **2026-07-07** — Jinkyu Kim, Jinyoung Choi, Bohyung Han — [D2PO: Optimizing Diffusion Samplers via Dynamic Preference](http://arxiv.org/abs/2607.06609v1)
  <details><summary>📄 Abstract</summary>
  We propose D2PO (Dynamic Direct Preference Optimization), a principled framework for optimizing diffusion sampling policies with respect to timestep schedules and classifier-free guidance (CFG) weights. Our work is motivated by a fundamental limitation of existing student-teacher regression frameworks; low-NFE student samplers are trained to mimic high-NFEteachers, often sacrificing high-frequency texture fidelity while preserving coarse global structures, thereby misaligning the sampler with pe...
  </details>

- **2026-07-07** — Yuqi Chen, Vincent Siu, Yang Liu et al. — [Controlling Tool Use with Heading-Specific Activation Steering](http://arxiv.org/abs/2607.05790v1)
  <details><summary>📄 Abstract</summary>
  Tool-augmented large language models extend their capabilities beyond parametric knowledge through external tools, but tend to invoke them unnecessarily. We investigate whether tool-use decisions have any stable internal representation that can be extracted and manipulated, a question that is non-trivial given that tools exist entirely in context at inference time and have no direct encoding in model weights. We show that steering vectors extracted from heading-anchors positions exert bidirectio...
  </details>

- **2026-07-07** — Huakun Liu, Qing Yu, Kent Fujiwara et al. — [ARMS: Anchor-Relational Motion Streaming for Seamless Solo-Social Motion Transitions](http://arxiv.org/abs/2607.05733v1)
  <details><summary>📄 Abstract</summary>
  Generating temporally continuous and socially coherent human motion from text remains a fundamental challenge, particularly in realistic streams where people act alone, enter interactions, and later disengage. Most existing methods generate fixed-length motion clips under static agent configurations, which makes them brittle to solo-social transitions and unsuitable for incremental generation over long horizons. We propose ARMS, an Anchor-Relational Motion Streaming framework that unifies solo m...
  </details>

- **2026-07-07** — Akshay Arora, Ishan Nigam, Ashutosh Aggarwal et al. — [Beyond Static Evaluation: Building Simulation Environments for Scalable Agentic Reinforcement Learning](http://arxiv.org/abs/2607.05773v1)
  <details><summary>📄 Abstract</summary>
  As Large Language Models (LLMs) evolve into autonomous agents, traditional static evaluation fails to capture multi-step decision-making. We introduce AgenticAI-Supervisor, an API and UI-driven RL Gym environment that decouples environment creation from scalable execution. By moving to verifiable execution outcomes, the platform generates high-fidelity traces and applies multi-dimensional reward shaping. Critically, our framework mitigates reward hacking through rigorous internal state validatio...
  </details>

- **2026-07-06** — Hanan Gani, Guy Pulik, Daniel Rosenfeld et al. — [Recovering Cloud Microstructures with Cascaded Diffusion Inversion](http://arxiv.org/abs/2607.05637v1)
  <details><summary>📄 Abstract</summary>
  High-resolution satellite imagery is critical for observing fine-scale cloud structures that inform weather modification strategies like cloud seeding for rain-enhancement. However, the spatial resolution of current geostationary and polar-orbiting satellites is often insufficient for capturing small cloud features. Current super-resolution methodologies are suited for natural images and, therefore, struggle to generalize to satellite-captured spectral images of cloud cover. To address this, we ...
  </details>

- **2026-07-06** — Anand Kamble, Aniket Tathe — [NAVER LABS System Re-implementation for the IWSLT 2026 Instruction-Following Task](http://arxiv.org/abs/2607.05623v1)
  <details><summary>📄 Abstract</summary>
  We re-implement the NAVER LABS IWSLT 2025 instruction-following pipeline for the IWSLT 2026 Shared Task (constrained condition, short audio track), adapting it to the mandated components: SeamlessM4T-v2-large as the speech encoder and Qwen3-4B-Instruct as the LLM backbone. The three-stage approach projector alignment, text-only LoRA pre-training, and multimodal merging is preserved from the original design. We additionally construct 100k synthetic instruction-following examples across ten speech...
  </details>

- **2026-07-06** — Chang Nie, Jiaju Wei, Junlan Feng et al. — [Light-Omni: Reflex over Reasoning in Agentic Video Understanding with Long-Term Memory](http://arxiv.org/abs/2607.05511v1)
  <details><summary>📄 Abstract</summary>
  Agentic video understanding equips models with long-term memory to autonomously process and respond to continuous, long-horizon multimodal streams. However, advanced video agents often rely on ``detective-style'' iterative reasoning for action control (e.g., $\mathtt{search}$) and evidence aggregation, incurring prohibitive costs and latency. We argue that such heavy reasoning primarily compensates for the lack of global context and semantic misalignment in retrieval. This paper introduces Light...
  </details>

- **2026-07-06** — Zhifeng Kong, Sang-gil Lee, Jaehyeon Kim et al. — [Unified Audio Intelligence Without Regressing on Text Intelligence](http://arxiv.org/abs/2607.05196v2)
  <details><summary>📄 Abstract</summary>
  Audio intelligence involves understanding, reasoning about, and generating both audio and speech. In this work, we introduce Nemotron-Labs-Audex-30B-A3B (Audex), a unified audio-text LLM built on Nemotron-Cascade-2-30B-A3B, a strong text-only MoE LLM. Audex adopts a simple unified design with a single Transformer decoder: audio inputs are encoded and projected into the text embedding space, while text tokens and quantized audio output tokens are treated uniformly during generation. This architec...
  </details>

- **2026-07-06** — Gengtian Shi, Jinze Yu, Chenhao Wu et al. — [Video-Text Temporal Localization via Multi-Scale Convolution and Dynamic Routing](http://arxiv.org/abs/2607.05093v2)
  <details><summary>📄 Abstract</summary>
  Video-text temporal localization requires precise alignment between natural language queries and corresponding video segments, a fundamental challenge in multimodal understanding. We present a novel framework that addresses two critical limitations of existing methods: inadequate modeling of hierarchical temporal structure and inability to handle complex many-to-many correspondences between modalities. Our approach introduces a multi-scale temporal convolutional encoder that captures motion patt...
  </details>

- **2026-07-06** — Humasak Tommy Argo Simanjuntak, Jesika Purba, Sitogab Girsang et al. — [AI for Cultural Heritage Textiles: Fine-Tuned Latent Diffusion for Novel Ulos Motif Synthesis](http://arxiv.org/abs/2607.06590v1)
  <details><summary>📄 Abstract</summary>
  Preserving and revitalising traditional textiles such as Ulos, a cultural heritage of the Batak ethnic group in North Sumatra, Indonesia, requires balancing fidelity to tradition with innovative approaches that meet contemporary design demands. Traditional Ulos weaving faces two key limitations: a narrow range of motifs and a time-intensive design process. This study presents a generative AI framework that fine-tunes two pretrained latent diffusion models: Protogen v3.4 and Stable Diffusion v1.4...
  </details>

- **2026-07-06** — Paolo Luppi, Viktoria Kabel, Flaminia Giacomini et al. — [Reduced Quantum-Reference-Frame Channels for Open Quantum Systems](http://arxiv.org/abs/2607.05578v1)
  <details><summary>📄 Abstract</summary>
  When reference frames are treated quantum mechanically, the subsystem structure of quantum systems is no longer absolute, but depends on the choice of the quantum reference frame (QRF). This raises a basic question: which dynamical properties are preserved across QRFs, and which depend on the physical reference used to define the system? We study this question in the general setting of open quantum systems. At the operational level, after a QRF transformation, the old reference frame and environ...
  </details>

- **2026-07-06** — Cheng-Kang Chou, Ming-To Chuang, Ke-Han Lu et al. — [REDDIT: Correcting Model-Generated Timestamp Drift in ASR without Forgetting via Replay-Based Distribution Editing](http://arxiv.org/abs/2607.05364v1)
  <details><summary>📄 Abstract</summary>
  Modern autoregressive ASR systems can emit timestamps as decoded tokens, enabling timestamped transcription without frame-level aligners or inference-time post-processing. We show that these generated timestamps can drift across long non-speech spans: the transcript may remain plausible, but the decoded time axis drifts away from the audio. We study this non-speech-induced timestamp drift with self-built gap and long-gap benchmarks across 15 evaluated timestamp-producing ASR and audio-language s...
  </details>

- **2026-07-06** — Wencan Jiang, Jiangning Zhang, Yong Liu — [ChatImage: Navigating Long-Form LLM Answers through Interactive Images](http://arxiv.org/abs/2607.05290v1)
  <details><summary>📄 Abstract</summary>
  Large Language Models (LLMs) can produce detailed answers to complex queries, but these answers are typically presented as dense linear text, which makes fine-grained inspection, navigation, and return visits difficult. We present ChatImage, a system that converts long-form LLM answers into interactive visual images. Given a textual answer, ChatImage first normalizes its content into structured visual modules, plans a visual layout, and renders a coherent image. It then applies a second groundin...
  </details>


### 📂 robustness
*鲁棒性与可靠性 / Robustness & Reliability* — 75 papers

- **2026-07-09** — Riccardo Revalor, Jalees Rehman, Debjit Pal — [Can We Trust LLM's Logic? Quantifying Uncertainty, Coherence, and Robustness via a Graph-Based Framework](http://arxiv.org/abs/2607.08017v1)
  <details><summary>📄 Abstract</summary>
  Large-Language Models (LLMs) can be prone to flawed and unfaithful reasoning that decoding strategies like Self-Consistency (SC) fail to detect as they evaluate only final-answer agreement while ignoring the logical validity of intermediate steps. This raises three fundamental questions: How can we reliably quantify uncertainty in LLM reasoning? Can semantic, structural, and causal awareness select more faithful reasoning compared to naïve majority voting? and How robust is reasoning topology un...
  </details>

- **2026-07-09** — Yunchao Yao, Zhuxiu Xu, Tianqi Zhang et al. — [DexVerse: A Modular Benchmark for Multi-Task, Multi-Embodiment Dexterous Manipulation](http://arxiv.org/abs/2607.08751v1)
  <details><summary>📄 Abstract</summary>
  Building general-purpose dexterous manipulation policies requires benchmarks that go beyond isolated tasks to systematically evaluate policies across diverse interaction modes, sensory conditions, and robot embodiments. However, existing benchmarks remain limited in task and data diversity, embodiment coverage, or controllable visual variation, hindering studies of cross-task and cross-embodiment generalization. We present DexVerse, a large-scale and modular benchmark for dexterous manipulation....
  </details>

- **2026-07-09** — Siddharth Damodharan, Radhika Gupta, Ali Alshami et al. — [AUTOPILOT VQA: Benchmarking Vision-Language Models for Incident-Centric Dashcam Understanding](http://arxiv.org/abs/2607.08745v1)
  <details><summary>📄 Abstract</summary>
  Recent advances in Vision-Language Models, Large Language Models, and Multimodal Large Language Models have improved autonomous driving tasks such as scene understanding, decision making, trajectory prediction, and visual question answering. However, evaluating whether these models can reliably reason about safety-critical incidents remains challenging. To address this gap, we present AUTOPILOT-VQA, an incident-centric visual question answering benchmark for dashcam video understanding. The data...
  </details>

- **2026-07-09** — Ali Larian, Qian Lin, Chang Zong Wu et al. — [Multi-Modal, Multi-Environment Machine Teaching for Robust Reward Learning](http://arxiv.org/abs/2607.08647v1)
  <details><summary>📄 Abstract</summary>
  As autonomous agents are increasingly deployed across diverse operational contexts, aligning their behavior with human intent demands reward functions that remain robust to such changes rather than overfitting to any single environment. Inverse reinforcement learning (IRL) provides a principled way to infer such objectives from human feedback. However, existing analyses of optimal teaching approaches for IRL focus on single-environment, demonstration-only settings, leaving underexplored how hete...
  </details>

- **2026-07-09** — Qihang Zhang, Lin Li, Luyao Zhang et al. — [Native Video-Action Pretraining for Generalizable Robot Control](http://arxiv.org/abs/2607.08639v1)
  <details><summary>📄 Abstract</summary>
  The advent of video-action models offers a promising path for robot control. Nevertheless, we argue that repurposing video generative models designed for digital content creation is inherently inadequate for physical environments. To bridge this gap, we present LingBot-VA 2.0, a video-action foundation model built from the ground up for embodiment. Four core design principles showcase its evolution from LingBot-VA. (1) Departing from traditional reconstruction-focused VAEs, we introduce a semant...
  </details>

- **2026-07-09** — Qian Jiang, Zhecheng Shi, Jingpu Yang et al. — [OmniFood-Bench: Evaluating VLMs for Nutrient Reasoning and Personalized Health Advice](http://arxiv.org/abs/2607.08423v1)
  <details><summary>📄 Abstract</summary>
  The rapid integration of Large Vision-Language Models (VLMs) into critical infrastructure promises to revolutionize   personalized healthcare and dietary management. However, in the domain of food systems, autonomous agents face a   unique and persistent challenge: the "Systemic Information Asymmetry" between visual appearance and intrinsic   nutritional composition. Existing benchmarks primarily focus on coarse-grained classification tasks, such as food   category recognition, which fail to eva...
  </details>

- **2026-07-09** — Iulia-Maria Udrea, Alexandra Diaconu, Bogdan Alexe — [VSRo-200: A Romanian Visual Speech Recognition Dataset for Studying Supervision and Multimodal Robustness](http://arxiv.org/abs/2607.08112v1)
  <details><summary>📄 Abstract</summary>
  We introduce VSRo-200, the first large-scale dataset for visual speech recognition (lip reading) in Romanian, comprising 200 hours of real-world podcast videos. All samples are annotated with pseudo-labels generated by a fine-tuned Romanian ASR model, while a subset of 100 hours is additionally transcribed by humans, enabling controlled analysis of supervision quality under a unified framework. Building on this dataset, we establish a benchmark for visual speech recognition in low-resource setti...
  </details>

- **2026-07-09** — Yi Zhang, Julia Rayz — [From Execution to Education: A Bloom-Aligned Framework for Measuring Educational Control in LLMs](http://arxiv.org/abs/2607.08009v1)
  <details><summary>📄 Abstract</summary>
  We introduce a Bloom-aligned framework for measuring educational control in Large Language Models (LLMs): the ability to preserve a task's instructional intent while shifting its cognitive demand toward specified learning objectives. We apply this framework to programming tasks in computer science education to study the gap between solving tasks and adapting them for learners. Using revised Bloom's Taxonomy as an operational scale of cognitive demand, we evaluate two intervention settings: gener...
  </details>

- **2026-07-09** — Yixian Zhang, Huanming Zhang, Feng Gao et al. — [Harness VLA: Steering Frozen VLAs into Reliable Manipulation Primitives via Memory-Guided Agents](http://arxiv.org/abs/2607.08448v1)
  <details><summary>📄 Abstract</summary>
  Language-conditioned manipulation requires both precise contact-rich control and robust reasoning over language, scenes, and long horizons. End-to-end Vision-Language-Action (VLA) models provide strong local visuomotor skills, but they are trained on in-distribution task trajectories and often fail under deployment perturbations such as semantic retargeting, goal re-binding, spatial-layout shifts, and unstable local contacts. LLM coding agents provide complementary semantic and compositional rea...
  </details>

- **2026-07-09** — Fabio Tosi, Luca Bartolomei, Matteo Poggi et al. — [ZipDepth: Bringing Lightweight Zero-Shot Monocular Depth Anywhere, on Any Device](http://arxiv.org/abs/2607.08771v1)
  <details><summary>📄 Abstract</summary>
  Monocular depth estimation has seen remarkable progress through foundation models achieving robust zero-shot generalization, yet their computational demands place them far beyond the reach of embedded and mobile platforms. Lightweight alternatives exist, but have been developed almost exclusively within single-domain, self-supervised paradigms, failing silently under domain shift. We present ZipDepth, a compact monocular depth network that bridges this gap by combining an efficient reparameteriz...
  </details>

- **2026-07-09** — Ruiqi Shen, Chang Liu, Henghui Ding — [SAM-MT: Real-Time Interactive Multi-Target Video Segmentation](http://arxiv.org/abs/2607.08688v1)
  <details><summary>📄 Abstract</summary>
  Modern Video Object Segmentation (VOS) involves tracking and segmenting user-specified targets. While recent approaches have achieved remarkable performance in single-target scenarios, extending them to multi-target settings typically involves replicating the single-target processing for each individual object, resulting in reduced frame rates (FPS) with unbounded latency as target count increases. Built upon Segment Anything 2 (SAM2), we propose SAM-MT, which addresses this by transforming the ...
  </details>

- **2026-07-09** — Teng-Ruei Chen — [Resample or Reroute? Budget-Aware Test-Time Model Selection for Large Language Models](http://arxiv.org/abs/2607.08665v1)
  <details><summary>📄 Abstract</summary>
  Routing among large language models (LLMs) trades response quality against serving cost, motivated by the reported gap between deployed routers and a per-instance oracle. Recent analysis shows that test-time resampling can recover per-instance selection headroom that no single-commit router captures; however, that guarantee holds only under an idealized oracle equipped with correctness labels and an unconstrained budget, neither of which a deployed system has. To the best of our knowledge, no pr...
  </details>

- **2026-07-09** — Tian Li, Thomas E. Collett, Coleman M. Krawczyk et al. — [Disentangling the dark and stellar mass through precise lens modelling of the JWST observation of lensed quasar WFI2033--4723](http://arxiv.org/abs/2607.08576v1)
  <details><summary>📄 Abstract</summary>
  We use high-resolution JWST/NIRCam imaging and measured time delays to model the quadruply imaged quasar WFI2033--4723 with a composite stellar plus dark-matter mass model. We first construct an elliptical power-law baseline model and recover Fermat-potential differences (fpd) consistent with previous HST-based and JWST-based analyses, providing a reference scale for composite modelling. We then replace the total mass profile with a physically motivated decomposition in which the stellar mass fo...
  </details>

- **2026-07-09** — Zongyou Yang, Yinghan Hou, Xiaokun Yang — [When the Judge Changes, So Does the Measurement: Auditing LLM-as-Judge Reliability](http://arxiv.org/abs/2607.08535v1)
  <details><summary>📄 Abstract</summary>
  An LLM-as-judge score can move even when the candidate responses stay fixed, simply because the evaluator has changed. We treat this evaluator-replacement ambiguity as a measurement-validity problem. Across four judgment datasets, we compare two upgrade paths available in practice: scaling Qwen3 dense judges from 1.7B to 32B parameters and moving across MiniMax M2-M2.7 released APIs. The main pattern is that judge upgrades are not interchangeable: only Qwen3 1.7B to 4B gives a robust adjacent ga...
  </details>

- **2026-07-09** — Carlos Garcia-Hernandez, Aymane Abdali, Guangyu Wu et al. — [Log-Insight: Automating Microservice Incident Diagnosis via Neuro-Symbolic Log Analysis](http://arxiv.org/abs/2607.08529v1)
  <details><summary>📄 Abstract</summary>
  Diagnosing production incidents in large-scale microservice systems is time-critical for Site Reliability Engineers (SREs). A single 30-minute incident window in our deployment can generate over two million log lines--approximately 1.2 billion characters, far exceeding standard LLM context windows--making direct LLM-based Root Cause Analysis (RCA) infeasible. Existing approaches leave gaps: template-based parsers lack semantic anomaly reasoning, deep-learning detectors emit black-box binary sign...
  </details>

- **2026-07-09** — Ashit Kumar Subudhi, Bhargav Chirumamilla, Shubham Vaishnav et al. — [ADORN: Adaptive Drift handling for Open RAN using Reinforcement Learning](http://arxiv.org/abs/2607.08443v1)
  <details><summary>📄 Abstract</summary>
  Dynamic traffic variations in Open Radio Access Networks (O-RAN) lead to drift, which degrades the performance of Artificial Intelligence/Machine Learning (AI/ML) models. Traditional retraining approaches maintain forecasting accuracy but incur high computational cost and may lead to violations of Service Level Agreements (SLAs). This work proposes a Q-learning-based adaptive retraining approach that formulates the retraining decision as a Markov Decision Process (MDP), where a Reinforcement Lea...
  </details>

- **2026-07-09** — Thibaud Ardoin, Semira Einsele, Evis Bregu et al. — [Prompt Compression via Activation Aggregation](http://arxiv.org/abs/2607.08399v1)
  <details><summary>📄 Abstract</summary>
  Large language models process prompts by propagating activations through dozens of layers before generating a response. We ask whether the task-relevant information contained in an instruction prompt can be compressed into a single activation vector and re-injected into the model, replacing the original token sequence? We show this is achievable using a learned weighted sum of activations extracted at an intermediate layer and injected at an early layer of the target LLM. The compressed vector p...
  </details>

- **2026-07-09** — Siddhartha Jain, Ameya Velingker — [Understanding Axes of Difficulty For Long Context Tasks Via PredicateLongBench](http://arxiv.org/abs/2607.08284v1)
  <details><summary>📄 Abstract</summary>
  Large language models (LLMs) have demonstrated rapidly improving long-context capabilities, prompting a wave of benchmarks designed to evaluate them. However, existing long-context evaluations - from Needle-in-a-Haystack (NIAH) tests to more recent multi-hop reasoning and summarization tasks - predominantly measure average-case performance, and many are either saturated or lack robustness. Notably absent is a systematic way to probe how models perform as we scale up the difficulty of tasks along...
  </details>

- **2026-07-09** — Miseong Shawn Kim — [Compete Then Collaborate: Frontier AI Teachers Build a Verifiable Curriculum to Improve a Coding Student Beyond Imitation](http://arxiv.org/abs/2607.08255v1)
  <details><summary>📄 Abstract</summary>
  Large language models increasingly serve as teachers generating training data for smaller students. Prior multi-teacher knowledge distillation methods merge outputs without determining which frontier model teaches best, often relying on an LLM judge biased toward its own outputs. We introduce a compete-then-collaborate framework where four frontier AI teachers (Claude, Codex-GPT, Grok, Gemini) are ranked head-to-head by an execution-based judge (unit tests and stdin-stdout checks) with fairness ...
  </details>

- **2026-07-09** — Mengchen Li — [AutoPersonas: A Multi-Timescale Loop Engine for Open-Ended Persona Evolution](http://arxiv.org/abs/2607.08252v1)
  <details><summary>📄 Abstract</summary>
  Long-term persona agents must remain identifiable while adapting to new events, relationships, evidence, and social conditions. We identify self-locking as a runtime failure mode in continuing persona-life loops: locally plausible events keep appearing while the generated life collapses toward familiar environments, weak relationships, suspended decisions, and stale life stages. We trace this failure to model-level convergence toward high-probability behavioral channels and system-level context ...
  </details>

- **2026-07-09** — Yifan Wang, Zhixiang Hao, Yu Wang et al. — [Multimodal 3D LUT Generation via StatLUT with Statistical Features for Photorealistic Style Transfer](http://arxiv.org/abs/2607.08227v1)
  <details><summary>📄 Abstract</summary>
  Photorealistic Style Transfer (PST) aims to transfer the color and tonal style of a reference to a content image while strictly preserving its structural integrity. However, existing deep learning-based methods inherently suffer from semantic entanglement caused by pre-trained image encoders, leading to unnatural spatial distortions. Moreover, current pixel-level mapping paradigms often ignore color gamut topology, resulting in color banding, while also lacking the multimodal capability for intu...
  </details>

- **2026-07-09** — Chris Xing Tian, Chengkai Wu, Ziyu Wang et al. — [LUMI: Tokenizer-Agnostic LLM-Based Lossless Image Compression](http://arxiv.org/abs/2607.08221v1)
  <details><summary>📄 Abstract</summary>
  Large language model (LLM)-based lossless image compression methods typically represent pixel data through the native text interface of a pretrained model, converting pixel values into token sequences that the LLM processes through its vocabulary head. This design shows that pretrained language models can provide probability estimates for image coding, but it also couples compression to tokenizer behavior, vocabulary-specific numeric tokens, and model-family-specific adaptation. In this paper, w...
  </details>

- **2026-07-09** — Sarthak Kumar Maharana, Shambhavi Mishra, Yunbei Zhang et al. — [Continual Test-Time Adaptation in Computer Vision: Methods, Benchmarks, and Future Directions](http://arxiv.org/abs/2607.08164v1)
  <details><summary>📄 Abstract</summary>
  Deep neural nets achieve remarkable performance when training and test data share the same distribution, but this assumption frequently breaks in real-world deployment, where data undergoes continual distributional shifts. Continual Test-Time Adaptation (CTTA) addresses this challenge by adapting pretrained models to non-stationary target distributions on-the-fly, without access to source data or labeled targets, while mitigating two critical failure modes: catastrophic forgetting of source know...
  </details>

- **2026-07-09** — Sokea Sang, Leanghok Hour, Dongmin Kim et al. — [Adaptive Qubit Freezing Enables Robust Graph Partitioning for Divide-and-Conquer QAOA](http://arxiv.org/abs/2607.08138v1)
  <details><summary>📄 Abstract</summary>
  Divide-and-conquer variants of the Quantum Approximate Optimization Algorithm (QAOA) provide a promising route for executing combinatorial optimization problems beyond the qubit capacity of near-term quantum devices. However, existing approaches rely on the existence of small vertex separators and fail entirely on dense or highly connected graphs where such decompositions do not exist. We introduce Frozen Large Graph Partitioning (FrozenLGP), an adaptive decomposition framework that transforms p...
  </details>

- **2026-07-09** — Jun Nie, Yonggang Zhang, Jun Song et al. — [TTHE: Test-Time Harness Evolution](http://arxiv.org/abs/2607.08124v1)
  <details><summary>📄 Abstract</summary>
  The behavior of an LLM agent is determined not only by the underlying model, but also by its harness: the executable program that constructs context, invokes tools, verifies intermediate results, and recovers from failures. Existing approaches optimize such harnesses before deployment, searching training or development data for a fixed agent workflow that is then frozen at test time. This limits adaptation when the test distribution, failure modes, or tool interactions differ from those seen dur...
  </details>

- **2026-07-09** — Jhih-Rong Guo, Bi-Cheng Yan, Tien-Hong Lo et al. — [COALA: Robust Contextualized Speech-augmented Language Modeling for ASR via Contrastive Regularizer and Biasing Score Estimation](http://arxiv.org/abs/2607.08117v1)
  <details><summary>📄 Abstract</summary>
  Contextual biasing seeks to integrate external knowledge into automatic speech recognition (ASR) systems to accurately recognize domain-specific entities. In this paper, we propose COALA (Contextualized ASR Leveraging Biasing Scoring), a robust framework designed to enhance speech-augmented language models (SLMs) in complex multi-entity scenarios. Considering the inherent context-window limitations of SLMs, identifying relevant target entities from a large-scale biasing list is crucial for effec...
  </details>

- **2026-07-08** — A. Sayyad, J. Emmons, S. Jones et al. — [A Reliability Assessment of LALM Audio Judges for Full-Duplex Voice Agents](http://arxiv.org/abs/2607.07985v1)
  <details><summary>📄 Abstract</summary>
  We report the empirical reliability of Gemini models as audio judges that score full-duplex agent conversations directly from the raw stereo waveform, tested across three models in the Gemini family: 2.5 Flash, 3.5 Flash, and 3.1 Pro. Our primary evidence base uses Gemini 2.5 Flash as the ground-truth model, validated against three calibrated human raters on 209 stereo sessions, scored on 8 production dimensions: 152 full-duplex conversations across 13 accent-and-condition strata, together with ...
  </details>

- **2026-07-08** — Alessandro Canevaro, Hang Yu, Julian Schmidt et al. — [Shift & Drift: A Zero-Shot Benchmark for Generalizable and Robust Autonomous Driving Motion Planning](http://arxiv.org/abs/2607.07844v1)
  <details><summary>📄 Abstract</summary>
  While closed-loop motion planners trained on large-scale, object-level datasets, e.g., nuPlan, demonstrate strong in-distribution (ID) performance, their generalization to novel urban topologies and recovery mechanisms following execution perturbations remain under-explored. To address this, we present Shift & Drift, a novel dual-track benchmark designed to rigorously stress-test motion planners across two critical axes of distribution shift: (1) The Semantic Shift Track leverages a novel conver...
  </details>

- **2026-07-08** — Nobin Sarwar, Shubhashis Roy Dipta, Zheyuan Liu et al. — [Multimodal Unlearning Across Vision, Language, Video, and Audio: Survey of Methods, Datasets, and Benchmarks](http://arxiv.org/abs/2607.07907v1)
  <details><summary>📄 Abstract</summary>
  With the growing adoption of VLMs, DMs, LLMs, and AFMs, these multimodal foundation models can inadvertently encode sensitive, copyrighted, biased, or unsafe cross-modal associations that originate from their training data. Retraining after deletion requests or policy updates is often impractical, and targeted forgetting remains difficult because knowledge is distributed across shared representations. Multimodal unlearning addresses this challenge by enabling selective removal across modalities ...
  </details>

- **2026-07-08** — Meera Desai, Dallas Card, Abigail Z. Jacobs — [Validating LLMs in social science: Epistemic threats and emerging norms](http://arxiv.org/abs/2607.07915v1)
  <details><summary>📄 Abstract</summary>
  Large language models (LLMs) are reshaping social science methodology. Researchers increasingly prompt language models to generate quantitative measurements of social concepts, for example labeling data or simulating survey responses. Yet LLMs pose methodological challenges including bias, hallucination, and brittleness across contexts, with unclear threats to validity. Standard practices and norms for addressing these challenges are still emerging. We collect and systematically analyze validati...
  </details>

- **2026-07-08** — Baoyu Li, Xinchen Yin, Mengying Lin et al. — [EgoWAM: World Action Models Beyond Pixels with In-the-Wild Egocentric Human Data](http://arxiv.org/abs/2607.08436v1)
  <details><summary>📄 Abstract</summary>
  Egocentric human data offers scalable supervision for robot manipulation. However, behavior cloning entangles transferable content like objects, scenes, and task semantics, with non-transferable factors like human morphology, head motion, and behavioral style. We study whether World Action Models (WAMs) provide a better training signal by requiring policies to predict not only actions, but also how the scene evolves. The central question is what world representation best enables human-to-robot t...
  </details>

- **2026-07-08** — Hari Prasad — [A Transdiagnostic Space of Disorder Like Phenotypes in Reinforcement Learning Agents](http://arxiv.org/abs/2607.07753v1)
  <details><summary>📄 Abstract</summary>
  Modelling psychological disorders in artificial agents offers both a testbed for computational psychiatry and a lens on the failure modes of affective control. Prior work induces one or two disorders in a reinforcement learning (RL) agent by hand-tuned reward shaping, labels the behaviour post hoc, and reports single runs. We recast disorder modelling as dose-controllable manipulation of cognitive appraisal signals in an appraisal-guided PPO agent, expressing seven disorders (anxiety, mania, obs...
  </details>

- **2026-07-08** — Seokhoon Jeong, Mijung Kim, Taehwan Kim — [Agentic Neural Architecture Search](http://arxiv.org/abs/2607.07984v1)
  <details><summary>📄 Abstract</summary>
  Neural architecture search (NAS) methods have grown increasingly efficient, yet they remain bounded by manually engineered search spaces that require substantial domain expertise and must be rebuilt for every new task. Large language models (LLMs) can generate architectures in an open-ended space, but how to optimally divide the labor between LLM-driven design and NAS-driven search remains unexplored. We propose a mechanism that bridges these two paradigms: an LLM produces a high-quality seed ar...
  </details>

- **2026-07-08** — Zhijian Luo, Yangyang Li, Xinyu Luo et al. — [Enhancing Photometric Redshift Estimation for LSST with a Hybrid LSTM-Mixture Density Network](http://arxiv.org/abs/2607.07960v1)
  <details><summary>📄 Abstract</summary>
  Accurate photometric redshift (photo-$z$) estimation and robust uncertainty quantification are essential for the LSST to achieve its precision cosmology goals. Traditional machine learning algorithms are largely restricted to point estimates, struggling to characterize the multimodal nature of redshift PDFs and the degeneracies within the color-redshift space. To address this, we present and validate the LSTM-MDNz architecture, which integrates sequential feature extraction with flexible probabi...
  </details>

- **2026-07-08** — Weizhe Liu, Yunjie Wu, Xiangqian Shu et al. — [DreamCharacter-1: From 3D Generative Foundation Models to Product-Ready Character Generation](http://arxiv.org/abs/2607.07817v1)
  <details><summary>📄 Abstract</summary>
  We present DreamCharacter-1, a lightweight post-adaptation framework that calibrates pretrained 3D foundation models toward high-fidelity, production-ready 3D character generation. Building upon a 3D foundation backbone, our pipeline incorporates three task-oriented components: (1) geometry post-training, which enhances fine-grained surface details through geometric preference optimization; (2) texture post-training, which synthesizes high-resolution textures and refines the appearance of occlud...
  </details>

- **2026-07-08** — Meet Barot, Daniel Berenberg, Sina Khajehabdollahi — [Architecture Generalization with MetaNCA](http://arxiv.org/abs/2607.07743v1)
  <details><summary>📄 Abstract</summary>
  Self-organization is an emergent property of life, driven by the collective behavior of individual components acting on local information. Biological neurons, through local interactions transmitted through synapses, are able to learn efficiently and can adapt their connections over an organism's lifespan. Motivated by these desirable properties of adaptability and local interaction, neural cellular automata (NCA) models have been successful at learning morphogenesis solely through local update r...
  </details>

- **2026-07-08** — Ishaan Batta, Meenu Ajith, Vince Calhoun — [Latent graph encoding of multimodal neuroimaging features with generative AI architectures](http://arxiv.org/abs/2607.07027v1)
  <details><summary>📄 Abstract</summary>
  While generative models enable encoding of complex neuroimaging data for feature generation and reconstruction, developing optimal architectural frameworks with appropriate encoding and latent space processes is crucial for studying structural and functional properties of the brain. We design a multimodal generative framework for structural and functional magnetic resonance imaging (MRI) features through systematic evaluation of encoding strategies, latent multimodal fusion, and generative model...
  </details>

- **2026-07-08** — Lipu Zhou, Yaoyun Kang, Junxiang Pang et al. — [GeoGS-SLAM: Geometry-Only Gaussian Splatting for Dense Monocular SLAM](http://arxiv.org/abs/2607.07452v1)
  <details><summary>📄 Abstract</summary>
  Dense visual SLAM is a fundamental problem in robotics. Recent advances in 3DGS have demonstrated its potential for dense SLAM. Existing 3DGS frameworks focus on both appearance and geometry modeling. However, scene geometry is typically more critical for SLAM than novel view synthesis because downstream robotic tasks, such as navigation and obstacle avoidance, rely primarily on accurate spatial geometry rather than photorealistic rendering. This observation raises a natural question: Is it feas...
  </details>

- **2026-07-08** — Jinbo Yang, Mingyue Yuan, Boyuan Zhang et al. — [HPG-Diff: Hierarchical physics-guided diffusion with differentiable connectivity constraints for topology optimization](http://arxiv.org/abs/2607.07233v1)
  <details><summary>📄 Abstract</summary>
  Deep generative models offer a promising paradigm for topology optimization, enabling rapid design exploration. However, these approaches lack intrinsic physics guidance, often leading to poor generalizability across unseen boundary conditions and the formation of floating material artifacts. To address these limitations, we propose Hierarchical Physics-Guided Diffusion (HPG-Diff), a novel diffusion framework that enforces physics consistency through two synergistic mechanisms. First, we introdu...
  </details>

- **2026-07-08** — Shivendra G. Tewari, Holly Kimko — [A hierarchical memory architecture overcomes context limits in long-horizon multi-agent computational modeling](http://arxiv.org/abs/2607.07666v1)
  <details><summary>📄 Abstract</summary>
  Large language models (LLMs) demonstrate remarkable reasoning capabilities, yet their stateless architecture fundamentally limits deployment in long-horizon research workflows requiring multi-session continuity and quantitative rigor. Here we present Ensemble QSP, a multi-agent framework featuring a three-layer hierarchical memory architecture that keeps injected context bounded and constant in project duration (mid-term project state: median 301 tokens, max 4,050, across 104 runs) by capping ea...
  </details>

- **2026-07-08** — Timur Khudaiberganov — [Geometric Interpretation of Sum Photon Blockade](http://arxiv.org/abs/2607.07591v1)
  <details><summary>📄 Abstract</summary>
  We present a geometric interpretation of the sum photon blockade effect in multimode quantum optical systems, such as semiconductor microresonators. The blockade condition \(c^{(n)} \cdot v = 0\) reflects the orthogonality of the \(n\)-photon amplitude vector to a target mode vector in an \(N\)-dimensional Hilbert space, visualized as the confinement of the state to a hyperplane.   A key result is the calculation of the maximum probability of the system remaining in the blockade subspace under t...
  </details>

- **2026-07-08** — Jorge Pueyo, Daniel Camps-Mur and, Miguel Catalan-Cid — [PHaul: A PPO-based forwarding agent for Sub6 enhanced Integrated Access and Backhaul networks](http://arxiv.org/abs/2607.07584v1)
  <details><summary>📄 Abstract</summary>
  3GPP Integrated Access and Backhaul (IAB) allows operators to deploy outdoor mm-wave access networks in a cost-efficient manner, by reusing the same spectrum in access and backhaul. In IAB networks the performance bottleneck is the wireless backhaul segment, where efficient forwarding strategies are needed to effectively use the available capacity. In addition, the performance of the mm-wave IAB backhaul segment is contingent on the availability of line of sight (LoS) conditions in the selected ...
  </details>

- **2026-07-08** — Feng He, Zhenting Wang, Qifan Wang et al. — [HIVE: Understanding Post-Hallucination Reasoning in Vision Language Models](http://arxiv.org/abs/2607.07507v1)
  <details><summary>📄 Abstract</summary>
  Hallucinations in vision language models (VLMs) are commonly treated as semantic errors, yet they often arise from partial or ambiguous visual evidence. Prior work mainly focuses on detecting or suppressing hallucinations at generation time, leaving the subsequent reasoning stage largely unexplored. In this work, we study Post Hallucination Reasoning (PHR), the stage in which hallucinated semantics enter the model's inference context and influence downstream predictions. To systematically invest...
  </details>

- **2026-07-08** — Ahan Basu, Ratnangshu Das, Soumyodipta Nath et al. — [Learning Spatiotemporal Tubes for Full Class of Signal Temporal Logic Tasks for Control of Unknown Systems under Input Constraints](http://arxiv.org/abs/2607.07136v1)
  <details><summary>📄 Abstract</summary>
  This paper presents a Spatiotemporal Tube (STT)-based control framework for general unknown nonlinear Euler-Lagrange (EL) systems subject to input constraints, with the objective of satisfying Signal Temporal Logic (STL) specifications, where confinement of the system trajectory within the STT guarantees the satisfaction of the corresponding STL task. For both single and multi-agent scenarios, the STT corresponding to each agent is modeled as a time-varying ball, whose center and radius are join...
  </details>

- **2026-07-08** — Hao Cong, Huizu Lin, Zihan Wang et al. — [Seeing and Reflecting: Multimodal Memory-Enhanced Agent Collaboration for Recommendation](http://arxiv.org/abs/2607.07108v1)
  <details><summary>📄 Abstract</summary>
  Large language model (LLM)-based agentic recommender systems show promise in modeling user preferences through natural-language reasoning, yet they remain limited by text-centric inputs and coarse-grained memory updates, making agents prone to missing visual evidence, semantic noise, and preference drift. To address these limitations, we propose MMEACR, a Multimodal Memory-Enhanced Agent Collaboration framework for recommendation. MMEACR introduces a dual-track memory architecture that separates...
  </details>

- **2026-07-08** — Jiang Zhang, Yan-dong Chen — [KAN-LSTM-Transformer Neural Networks, MFV and Cosmological Parameters](http://arxiv.org/abs/2607.06959v1)
  <details><summary>📄 Abstract</summary>
  Reconstructing the cosmic distance ladder directly from observations is a crucial issue in cosmology. In this paper, we present a novel method for modeling the cosmic distance ladder and estimating cosmological parameters through the use of Kolmogorov-Arnold networks (KAN), Long Short-Term Memory (LSTM), and Transformer networks (collectively referred to as KLT-Net), based on the apparent magnitude data from the Pantheon SN Ia compilation. As a data-driven, non-parametric method for reconstructi...
  </details>

- **2026-07-08** — Chenchuhui Hu, Shaoming Pan, Leon Axel et al. — [Bi-PT: Bidirectional Cross-Attention Point Transformers for Four-Chamber Heart Reconstruction from Sparse Cardiac MRI Data](http://arxiv.org/abs/2607.06923v1)
  <details><summary>📄 Abstract</summary>
  We propose Bi-PT, a pipeline for reconstructing 3D four-chamber human heart meshes from clinical sparsely sampled cardiac magnetic resonance imaging (CMR) data. This work addresses the error-prone generation of 3D cardiac shape from a sparse point cloud (SPC) extracted from 2D long-axis and short-axis views used in routine clinical CMR protocols. Bi-PT enables accurate inference of the four-chamber heart mesh from the SPC by learning robust point features via bidirectional point cross-attention ...
  </details>

- **2026-07-08** — Chuqing Zhao, Haochen Yang — [Evaluating LLM Robustness Under Domain-Specific Prompt Perturbations in Public Health Applications](http://arxiv.org/abs/2607.06913v1)
  <details><summary>📄 Abstract</summary>
  Large language models (LLMs) are increasingly applied in public health applications, yet their robustness to non-clinical user inputs remains underexplored. We propose a domain specific robustness benchmark that evaluates LLMs under two perturbation types that commonly arise when non-clinical users interact with health AI systems: misinformation framing (MF), where prompt might be injected by false health claims, and layperson rewriting (LR), where patients describe symptoms in everyday language...
  </details>

- **2026-07-07** — Jinhong Deng, Limeng Qiao, Guanglu Wan — [HoloCount: A Holistic Visual Counting Benchmark for MLLMs](http://arxiv.org/abs/2607.06420v1)
  <details><summary>📄 Abstract</summary>
  Visual counting is a fundamental pillar of multimodal intelligence, requiring a seamless integration of fine-grained grounding and spatial reasoning. While Multimodal Large Language Models (MLLMs) have achieved remarkable success in qualitative scene understanding, their quantitative precision remains a significant bottleneck, often characterized by persistent numerical hallucinations. Existing counting benchmarks primarily focus on basic perception in simplified contexts, failing to capture the...
  </details>

- **2026-07-07** — Wael Albayaydh, Rui Zhao, Ivan Flechais — [Beyond the Leaderboard: A Synthesis of Tool-Use, Planning, and Reasoning Failures in Large Language Model Agents](http://arxiv.org/abs/2607.05775v1)
  <details><summary>📄 Abstract</summary>
  Large language model (LLM) agents are increasingly evaluated on their ability to use tools, plan multi-step tasks, coordinate with other agents, and operate over extended horizons. Reported benchmark gains often obscure recurring failure modes documented across otherwise unrelated evaluation efforts. This paper synthesizes 27 benchmark, taxonomy, and audit papers (2023-2026), spanning 19 distinct benchmarks, into a cross-cutting taxonomy of agent limitations. To our knowledge, this is the first ...
  </details>

- **2026-07-07** — Nima Kelidari, Mohammadsaeed Haghi, Mahdi Salmani — [A Gold-Standard Study of What Makes a Lightweight Game-Playing Agent Strong](http://arxiv.org/abs/2607.06854v1)
  <details><summary>📄 Abstract</summary>
  Reinforcement learning agents for imperfect-information card games are only as strong as the opponents they train against, and they are hard to grade, since they beat a random opponent over 99 percent of the time and only tie copies of themselves. So we build a strong, fixed, rule-based expert for Gin Rummy and use it only as a yardstick, never for training. It beats every agent we trained 70 to 99 percent of the time. Across more than a hundred runs, we isolate what makes a lightweight agent st...
  </details>

- **2026-07-07** — Razvan Mihai Popescu — [Reliable and Developer-Aligned Evaluation of Agents for Software Engineering](http://arxiv.org/abs/2607.06713v1)
  <details><summary>📄 Abstract</summary>
  Large language models are rapidly moving towards closing the development cycle, transitioning from simple assistive companions to autonomous contributors deeply embedded into collaborative development environments. Despite their accelerated adoption, existing evaluation techniques are limited due to their fragmented nature and distorted projection of true model capabilities, often obtained from hypothetical syntactic scenarios. This research aims to bridge this gap by providing a comprehensive e...
  </details>

- **2026-07-07** — Ke Rui, Yushen Zuo, Jiawei Wang et al. — [Diagnosing Semantic Handoff Failures in Agent-Orchestrated Vision-Language-Action Skill Composition](http://arxiv.org/abs/2607.06256v1)
  <details><summary>📄 Abstract</summary>
  Long-horizon household tasks require robots to compose many language-conditioned skills, yet the boundary between consecutive skills is rarely explicit. A skill may satisfy its own postcondition while leaving the robot, objects, or camera views in a state from which the next skill cannot reliably start. We study this semantic handoff problem in BEHAVIOR-1K through an agent-orchestrated vision-language-action execution harness. The harness invokes $π_{0.5}$-based skill checkpoints trained from cl...
  </details>

- **2026-07-07** — Chenhao Yuan, Yinhao Xu, Shuwen Xu et al. — [LongCrafter: Towards Diverse Long-Context Understanding via Evidence-Graph-Guided Instruction Synthesis](http://arxiv.org/abs/2607.06160v1)
  <details><summary>📄 Abstract</summary>
  Synthesizing long-context supervised fine-tuning (SFT) data is a scalable way to enhance the long-context understanding of large language models (LLMs), yet existing approaches share three limitations: narrow task coverage, insufficient instruction difficulty, and a lack of faithfulness supervision. We propose \textbf{LongCrafter}, a structured synthesis framework that couples a hierarchical task taxonomy with an evidence-grounded pipeline. The taxonomy organizes long-context understanding into ...
  </details>

- **2026-07-07** — Shuze Daniel Liu, Claire Chen, Jiabao Sean Xiao et al. — [Strategic Bargaining in Multi-Buyer Markets: Reinforcement Learning from Verifiable Rewards for LLM Negotiations](http://arxiv.org/abs/2607.05863v1)
  <details><summary>📄 Abstract</summary>
  Negotiation is a fundamental strategic interaction in management science, characterized by agents attempting to reach agreements while protecting private information, such as reservation costs and hidden valuations. A prevalent yet complex scenario involves a single seller negotiating concurrently with multiple buyers, each possessing heterogeneous, private budgets. In such settings, constrained by a limited number of communication turns, the seller must balance exploring the broader market to d...
  </details>

- **2026-07-07** — Yueke Zhang, Yifan Zhang, Zihan Fang et al. — [SCOPE: Leveraging Subgoal Critiques for Code Generation](http://arxiv.org/abs/2607.05810v1)
  <details><summary>📄 Abstract</summary>
  Code generation with large language models (LLMs) remains unreliable because generated programs can appear correct while still violating key semantic requirements in the natural language specification. Existing feedback-based methods improve over coder-only generation, but they often rely on unstructured critique or execution signals that do not explicitly identify what the code is semantically missing. We present SCOPE, a prover-initialized subgoal critic for code generation. SCOPE adapts a Lea...
  </details>

- **2026-07-07** — Bhavya Sai Nukapotula, Samin Moosavi, Haoze Wang et al. — [EvoPlan: Evolutionary Neuro-Symbolic Robot Planning with Spatio-Temporal Guarantees](http://arxiv.org/abs/2607.06724v1)
  <details><summary>📄 Abstract</summary>
  LLM-based robot planners are fluent but cannot guarantee that their plans are executable or safe. Classical PDDL planners can guarantee these properties, but only after the problem is fully specified, and they make poor use of an LLM's ability to read context and repair plans. This paper presents a neuro-symbolic framework with three parts. All LLM calls use a locally-hosted open-weight model, so the pipeline can be deployed on-robot with no cloud dependency. First, an offline procedure that min...
  </details>

- **2026-07-07** — Yotam Wolf, Noam Wies, Amnon Shashua — [When Does In-Context Search Help? A Sampling-Complexity Theory of Reflection-Driven Reasoning](http://arxiv.org/abs/2607.06720v1)
  <details><summary>📄 Abstract</summary>
  Training large language models (LLMs) with extended reasoning has enabled in-context search, in which models iteratively generate, critique, and revise solution attempts. We provide a theoretical analysis of in-context search by modeling it as approximate inference over reasoning traces, where the base model defines a prior and self-reflection provides feedback for posterior updates, and study the resulting inference-time sampling complexity - the number of sequential attempts needed to achieve ...
  </details>

- **2026-07-07** — Aparna Madva, Sharath Srivatsa, Srinath Srinivasa et al. — [Rethinking Indic AI from a Lens of Cultural Heritage Preservation](http://arxiv.org/abs/2607.06544v1)
  <details><summary>📄 Abstract</summary>
  As Artificial Intelligence (AI) makes inroads into different parts of the Indian subcontinent, there is significant interest in studying how AI impacts the linguistic and cultural foundations of this civilization. AI is seen as a ''double-edged sword'' where on the one hand, it can enable access and inclusion for a large population, on the other, it can homogenize worldviews and exclude underrepresented languages and worldviews. In this paper, we try to characterize this problem by addressing th...
  </details>

- **2026-07-07** — Matthieu Ospici, Arnaud Gueze, Luc Bourrat et al. — [Mitigating Domain Shift in Conditioned Floor Plan Generation: Synthetic Pre-training for Data-Efficient Adaptation](http://arxiv.org/abs/2607.06483v1)
  <details><summary>📄 Abstract</summary>
  Robustness to domain shift is a key requirement for floor plan generative models to be applicable beyond the single dataset they were trained on, as floor plans vary widely across regions due to distinct architectural cultures, spatial constraints, and construction practices, while acquiring new annotated datasets remains costly and domain-specific. Yet, no prior work has studied this robustness in the context of conditioned floor plan generation. In this paper, we evaluate state-of-the-art mode...
  </details>

- **2026-07-07** — Taeyun Roh, Eunha Lee, Wonjune Jang et al. — [From Voting to Agent Collaboration: Answer-Type-Aware LLM Pipelines for BioASQ 14b](http://arxiv.org/abs/2607.06452v1)
  <details><summary>📄 Abstract</summary>
  Biomedical question answering requires not only accurate extraction of information from scientific literature but also reliable integration of evidence across multiple documents. This study presents a question-type-specific large language model (LLM) framework for BioASQ 14b Task B, designed to improve answer robustness and evidence grounding in biomedical question answering. Rather than applying a single prompting strategy to all questions, the framework selects different inference procedures f...
  </details>

- **2026-07-07** — Sofiane Daimellah, Sylvie Le Hégarat-Mascle, Clotilde Boust — [XRFormer: Multiscale Tokenization for XRF Representation Learning](http://arxiv.org/abs/2607.06424v1)
  <details><summary>📄 Abstract</summary>
  X-ray fluorescence (XRF) spectroscopy is a key modality for material analysis in cultural heritage. However, automated learning from XRF spectra remains challenging: XRF spectra are complex one-dimensional signals composed of sharp elemental peaks, broader structures, and background variations that are not taken into account by existing learning-based models. This paper introduces XRFormer, a transformer architecture tailored to XRF spectra through a multiscale convolutional tokenizer that injec...
  </details>

- **2026-07-07** — Jiazi Wang, Nonghai Zhang, Qiushi Xie et al. — [VaseMuseum: Digital Intelligent Museum for Ancient Greek Pottery](http://arxiv.org/abs/2607.06374v1)
  <details><summary>📄 Abstract</summary>
  Vision-language models (VLMs) have made interactive digital museums increasingly feasible by connecting 3D digitization with natural-language artifact exploration. However, in cultural heritage domains such as ancient Greek pottery, reliable VLM assistance is limited by two challenges. First, open-ended interpretation requires grounding fine-grained 2D/3D visual evidence in specialized curatorial knowledge, yet the retrieval process may introduce weak sources and unverifiable references. Second,...
  </details>

- **2026-07-07** — Kaibo Zhang, Ji Wu, Chao Zhang et al. — [Quantifying Entrainment Evidence: A Comparison of Frequentist and Bayesian Approaches for Information Processing Pathway Maps](http://arxiv.org/abs/2607.06284v1)
  <details><summary>📄 Abstract</summary>
  Information Processing Pathway Maps (IPPMs) offer a scalable framework for formalizing the complex sequence of mathematical transformations applied to sensory stimuli. These maps chart the latency and cortical expression of computational steps, relying on statistical inference to link model outputs with observed neural activity. Traditionally, this mapping has relied on frequentist hypothesis testing. However, determining which of several competing computational models best explains neural data ...
  </details>

- **2026-07-07** — Shuheng Zhang, Feng Wu — [NegROI: Click-Centric Uncertainty-Guided Refinement with Scene-Conditioned Negative Prompts for Robust Interactive 3D Segmentation](http://arxiv.org/abs/2607.05955v1)
  <details><summary>📄 Abstract</summary>
  Interactive 3D segmentation aims to extract object masks in point clouds with minimal user clicks. Despite recent progress, most existing approaches still struggle with (i) coarse voxel resolution that blurs fine boundaries under limited clicks and (ii) hard false positives caused by confusing background structures. These issues are exacerbated by density and scale shifts across datasets (e.g., dense RGB-D reconstructions vs. sparse LiDAR scans), where fixed refinement heuristics and purely clic...
  </details>

- **2026-07-07** — Timothée Gavin, Murat Bronz — [Intercepting an Agile Target with Net-Carrying Drones using Competitive Multi-Agent Reinforcement Learning](http://arxiv.org/abs/2607.05939v1)
  <details><summary>📄 Abstract</summary>
  This article presents a solution to intercept an agile drone by a team of agile drone carrying catching nets. We formulate the problem as a competitive Multi-Agent Reinforcement Learning (MARL) task. To address the problem of nonstationarity and catastrophic forgetting of agents overfitting to the current opponent strategy, we train the pursuers and the evader using Multi-Agent Proximal Policy Optimization (MAPPO) with Prioritized Fictitious Self Play (PFSP). We train the agents in a high-fideli...
  </details>

- **2026-07-07** — Yaovi Armand Amouzou-adoun, Lionel Gélébart, Cédric Flageul et al. — [A robust and versatile parallel FFT-based mechanical solver for general non-periodic and periodic boundary conditions](http://arxiv.org/abs/2607.05929v1)
  <details><summary>📄 Abstract</summary>
  General boundary conditions are implemented within a fast Fourier transform framework for linear and non-linear mechanical problems using small or finite transformation formulations. In the context of parallel computing (distributed memory), we present a framework that enables the combination of periodic and non-periodic (Dirichlet or Neumann) boundary conditions. Taking advantage of the link between non-periodic boundary conditions and the symmetries of the relevant components of the fluctuatio...
  </details>

- **2026-07-07** — Kaishen Wang, Tong Zheng, Xuehao Cui et al. — [Mitigating Factual Hallucination in Large Reasoning Models via Mixed-Mode Advantage Regularization](http://arxiv.org/abs/2607.05861v1)
  <details><summary>📄 Abstract</summary>
  Large reasoning models (LRMs) improve language model capabilities by generating explicit thinking traces before final answers. In factuality-oriented question answering (QA), such thinking often improves overall performance by helping the model recover relevant knowledge and refine its answers. However, we find that this benefit is not uniform at the instance level: explicit thinking can also overturn correct non-thinking answers and lead to factual drift. We refer to this failure mode as \emph{...
  </details>

- **2026-07-07** — Muhammadjon Tursunbadalov, Mustafojon Tursunbadalov — [A Quiet Failure in Calibrated Virtual Screening: Marginal Conformal Prediction Under-Covers the Minority Class, and a Class-Conditional Fix Recovers It](http://arxiv.org/abs/2607.06605v1)
  <details><summary>📄 Abstract</summary>
  Conformal prediction is being adopted in drug discovery to put an honest number on model reliability: pick an error rate alpha, and the method returns prediction sets containing the true label with probability at least 1 - alpha. We show this guarantee can be dangerous on imbalanced datasets. Across four datasets, standard (marginal) conformal prediction hits its global 90% coverage target while leaving the minority class badly exposed: realized minority coverage falls to 64.8% on blood-brain-ba...
  </details>

- **2026-07-07** — Mooho Song, Jay-Yoon Lee — [Retrieving a Set, Not Independent Passages: Set-Level Compatibility Learning for Efficient Set Exploration](http://arxiv.org/abs/2607.05712v1)
  <details><summary>📄 Abstract</summary>
  Multi-hop question answering and retrieval-augmented reasoning require selecting evidence passages that are jointly useful for answering a query. However, most retrievers still score passages independently or make locally supervised sequential decisions, which can fail when evidence usefulness depends on compatibility among passages. LLM-based set selection can model such interactions, but its computational cost limits practical use. We address this gap by formulating multi-hop retrieval as quer...
  </details>

- **2026-07-06** — Calvin A. Riiska, Michelle Lee, Yonatan Nemenman et al. — [Redundant contacts and force redistribution stabilize limbless vertical climbing](http://arxiv.org/abs/2607.06239v1)
  <details><summary>📄 Abstract</summary>
  Animals navigating complex vertical environments must secure stable footholds, a challenge for species without feet. While arboreal climbing has evolved repeatedly in snakes, the physical mechanisms they use to scale broad, nearly flat surfaces remain poorly understood. By measuring three-dimensional body kinematics and per-contact forces on a smooth vertical wall with protruding posts, we show that cornsnakes climb by dynamically balancing forces across a highly redundant network of 5 to 16 sim...
  </details>

- **2026-07-06** — Kenneth Benavides, Josh Fleischer, Danti Chen — [EvalLoop: A Methodology for Evaluation-Driven Iterative Improvement of Business AI Systems](http://arxiv.org/abs/2607.05638v1)
  <details><summary>📄 Abstract</summary>
  Teams deploying large language models in business contexts need evaluation systems, yet most treat evaluation as static model selection: run benchmarks, rank models, deploy the winner. This framing misses evaluation's primary value for production systems--diagnosing why a system underperforms and guiding what to fix. We present EvalLoop, a methodology for evaluation-driven iterative improvement. EvalLoop organizes evaluation around three mechanisms: (1) dimensional metric grouping that decompose...
  </details>

- **2026-07-06** — Sadia Kamal, Arefa Patwary, Anthony Marchiafava et al. — [Prompt Robustness Is Task-Dependent: Comparing Objective and Belief-Style Questions in LLM Evaluation](http://arxiv.org/abs/2607.05554v1)
  <details><summary>📄 Abstract</summary>
  Survey-style evaluations of large language models often treat a prompted response as a measure of a model's values or beliefs. This assumption is particularly fragile when responses are read as evidence of political values, social attitudes, or beliefs. We ask whether prompt robustness differs between objective questions with fixed answers and subjective questions that ask for opinions or values. We evaluate four instruction-tuned model families on three objective datasets (MMLU, ARC, and Cultur...
  </details>

- **2026-07-06** — Karim Benakli, Anna Chrysostomou — [The Fate of Black Hole-Induced Moduli Excursions in the Presence of Scalar Potentials](http://arxiv.org/abs/2607.05488v1)
  <details><summary>📄 Abstract</summary>
  Large charged black holes can create macroscopic, locally weakly curved regions in which moduli take values different from their asymptotic values. We study how robust this mechanism is once the scalar has a nontrivial potential. In four-dimensional Einstein-Maxwell-dilaton theory, the massless GHS solution provides a finite exterior throat in which the scalar and the gauge coupling vary logarithmically. We develop fixed-throat diagnostics for the competition between the black hole gauge source ...
  </details>

- **2026-07-06** — Anthony Hu, Václav Volhejn, Adrien Ramanana Rahary et al. — [Multiplayer Interactive World Models with Representation Autoencoders](http://arxiv.org/abs/2607.05352v2)
  <details><summary>📄 Abstract</summary>
  We introduce the first multiplayer world model for highly dynamic environments governed by complex physical interactions. Whereas single-player world models treat the other agents as part of the environment, ours conditions on the action streams of multiple agents, learning to attribute changes in the scene to the correct player and to stay coherent under arbitrary combinations of their actions. We study this problem in the game of Rocket League, where players compete and cooperate under fast, t...
  </details>


### 📂 watermark
*水印与溯源 / Watermarking & Provenance* — 10 papers

- **2026-07-09** — Ethan Leung, Elias Lumer, Corey Feld et al. — [Do You Need a Frontier Model as a Citation Verifier? Benchmarking Rubric LLMs for Deep-Research Source Attribution](http://arxiv.org/abs/2607.08700v1)
  <details><summary>📄 Abstract</summary>
  Reinforcement learning increasingly relies on an LLM judge to score each rubric criterion, and that judge acts as the reward model during training. Before such a signal can be trusted, we need to know how capable the judge must be and how biased it is. We study this calibration question for citation quality in deep-research systems, where a search-grounded LLM must support each claim it writes with a cited source. Citation quality is a structured rubric task in which each attribution-citation pa...
  </details>

- **2026-07-09** — Adis Alihodzic, Selma Skopljakovic Hubljar — [SHAP-Weighted Cross-Modal Expert Fusion for Emotion and Sentiment Recognition: Evidence and Limits](http://arxiv.org/abs/2607.08573v1)
  <details><summary>📄 Abstract</summary>
  Multimodal emotion and sentiment recognition is commonly addressed by early fusion, which concatenates modalities before classification, or late fusion, which combines independently trained unimodal predictors. Early fusion can be accurate but monolithic, while late fusion is modular but may lose cross-modal interactions. This paper revisits XAI-guided adaptive fusion (\xgaf), a tree-based mixture of unimodal and cross-modal experts whose sample-level weights are derived from TreeSHAP attributio...
  </details>

- **2026-07-09** — Javier Izquierdo, Aygul Zagidullina — [Applying JEPA-Style Predictive Learning to JA4-Derived Network Fingerprints](http://arxiv.org/abs/2607.08465v1)
  <details><summary>📄 Abstract</summary>
  I-JEPA and V-JEPA learn by matching latent predictions to target encoder outputs rather than regenerating the original input, and this has worked well for images and video. We explore whether the same objective works for compact network fingerprints. We built JA4-JEPA, a Transformer-based model trained on JA4, JA4H, JA4S, and JA4X subfields drawn from JA4DB and CIC-IDS- 2017. The training data combines roughly 397K samples from both sources, though no single sample contains all four view familie...
  </details>

- **2026-07-08** — Yufei Xia, Anjun Gao, Yueyang Quan et al. — [Who Broke the System? Failure Localization in LLM-Based Multi-Agent Systems](http://arxiv.org/abs/2607.07989v1)
  <details><summary>📄 Abstract</summary>
  Large language model (LLM) based multi-agent systems enable complex problem solving through coordinated reasoning and action, but their distributed structure also introduces new challenges in diagnosing system-level failures. When an execution fails, identifying which agent is responsible and at what point the trajectory first becomes irreversibly misdirected is difficult due to long-horizon interactions and tightly coupled agent behaviors. In this paper, we study the problem of failure localiza...
  </details>

- **2026-07-08** — Gospel Bassey, Vincent Fakiyesi — [Nigeria Machinery: A Low-Resource Industrial Dataset with a Domain-Grounded Reasoning Layer](http://arxiv.org/abs/2607.07883v1)
  <details><summary>📄 Abstract</summary>
  There is relatively little, public, and model-ready data on industrial machinery for African economies. This makes it hard to do quantitative analysis or to train language models on numeric tasks grounded in that setting. We release two things to help with part of this problem. The first is the Nigeria Machinery Usage and Failures Dataset: 89 machine-level records across 28 indicators, covering Nigeria's manufacturing and oil and gas sectors from 2006 to 2025. Every record names a public source ...
  </details>

- **2026-07-08** — Ahsan Habib Akash, Dipkamal Bhusal, Stacey Jones et al. — [Naming the Concepts Classifiers Rely On: Language-Anchored Decomposition for Faithful Explanation](http://arxiv.org/abs/2607.07264v1)
  <details><summary>📄 Abstract</summary>
  Deep neural networks are widely deployed in high-stakes visual applications where interpretability is critical, yet existing explanations face a trade-off: post-hoc concept methods recover factors that are faithful to a model's behavior but unnamed, while naming and by-design methods attach human-readable concepts only by retraining or altering the classifier. We propose Language-Anchored Decomposition (LAD), a post-hoc framework that delivers concepts which are simultaneously named, faithful, a...
  </details>

- **2026-07-07** — Riccardo Terrenzi, Serkan Ayvaz — [Faithful or Findable? Evaluating LLM-Generated Metadata for RDF Dataset Search](http://arxiv.org/abs/2607.05970v1)
  <details><summary>📄 Abstract</summary>
  Dataset search depends heavily on metadata, making LLM-generated metadata a consequential form of synthetic content in retrieval systems. We study six metadata-generation settings for RDF datasets, ranging from simple rewriting to profile-grounded and agentic graph-based generation, and evaluate them jointly for retrieval effectiveness and faithfulness. Unconstrained metadata rewriting delivers the strongest retrieval gains over the original metadata, but it is also the least faithful, showing t...
  </details>

- **2026-07-07** — Sergey Volkov, Yang Li, Ye Luo — [StateFuse: Deterministic Conflict-Preserving Memory for Multi-Agent Systems](http://arxiv.org/abs/2607.05844v1)
  <details><summary>📄 Abstract</summary>
  Agent systems accumulate conflicting observations across branches, retries, and replicas, yet many practical memory layers still collapse disagreement behind overwrite rules that are difficult to inspect or correct. We present StateFuse, a conflict-aware replicated memory contract built on standard OpSet/CRDT merge. StateFuse does not introduce a new join algebra; it defines an agent-facing semantics layer with immutable history, explicit conflict objects, exact and semantic correction handles (...
  </details>

- **2026-07-07** — Yue Xu, Yutao Sun, Yihao Liu et al. — [From Passive Retrieval to Active Memory Navigation: Learning to Use Memory as a Structured Action Space](http://arxiv.org/abs/2607.05794v1)
  <details><summary>📄 Abstract</summary>
  Long-term user memory is essential for personalized conversational agents, yet many memory systems still expose memory through passive retrieval interfaces, making the model a consumer of pre-selected evidence. We introduce NapMem, a framework for learning to use long-term user memory as a structured action space rather than passively retrieved context. NapMem organizes user history into a linked multi-granularity memory pyramid, where raw conversations, typed memory records, topic tracks, and u...
  </details>

- **2026-07-06** — Clemens Walter Koprolin, Leonardo Trentini, Benedikt Soja et al. — [GeoXplain: On-the-Fly Visual Explanations for Weather Foundation Models](http://arxiv.org/abs/2607.05655v1)
  <details><summary>📄 Abstract</summary>
  Weather and climate foundation models produce high-dimensional forecasts whose learned relationships are difficult to inspect with static plots alone. GeoXplain is an interactive Python-based visualization toolkit for exploring geospatial attribution maps across climate variables, atmospheric pressure levels, and forecast time. The toolkit accepts attribution bundles containing attribution grids together with corresponding metadata and renders them in a notebook widget or browser with map and gl...
  </details>


### 📂 survey
*综述与系统化 / Surveys & Systematization* — 2 papers

- **2026-07-08** — Arun Malik — [Progressive Crystallization: Turning Agent Exploration into Deterministic, Lower-Cost Workflows in Production](http://arxiv.org/abs/2607.07052v1)
  <details><summary>📄 Abstract</summary>
  AI agents deployed for IT operations are typically permanent cost centers because every execution requires full LLM inference, even for previously solved problems. This paper introduces progressive crystallization, a lifecycle that treats agent exploration as a discovery mechanism rather than a permanent execution model. It defines a three-stage execution taxonomy, from fully agent-orchestrated to hybrid to fully deterministic workflows, together with an evidence-based promotion mechanism that c...
  </details>

- **2026-07-07** — Rui Shu, Chun Yong Chong, Xin Zhou et al. — [What Resolve Rate Hides: Trajectory Structure Diagnostics for Coding Agents](http://arxiv.org/abs/2607.06184v1)
  <details><summary>📄 Abstract</summary>
  Coding agents are ranked almost entirely by resolve rate: whether their final patch passes the target tests. Yet two agents can reach the same outcome through very different processes, and a single pass/fail label says nothing about why a run failed or why an accepted run spent extra steps, time, or tokens. This process evidence lives in the trajectory, which records a run's searches, reads, edits, tool calls, validation, and reversions. However, raw traces are heterogeneous and hard to compare ...
  </details>


### 📂 other
*其他安全相关 / Other Security-Related* — 158 papers

- **2026-07-09** — Kushin Mukherjee, Na Yeon Kim, Maren Wehrheim et al. — [AI-guided stimuli discovery and generation to optimize facial emotion perception studies in autism](http://arxiv.org/abs/2607.08533v1)
  <details><summary>📄 Abstract</summary>
  Understanding perceptual differences between autistic and neurotypical adults requires behavioral assays that are sensitive, reliable, and mechanistically informative. Facial emotion perception is a useful test case because group differences have been reported, but findings vary across studies. Here we show that this variability may reflect image-level sparsity: autistic-neurotypical differences in emotion judgments were concentrated in a small subset of diagnostic facial expressions rather than...
  </details>

- **2026-07-09** — Mayank Singal — [When Thinking Hurts: Epistemic Signals in the Reasoning Chains of Visual Language Models](http://arxiv.org/abs/2607.08059v1)
  <details><summary>📄 Abstract</summary>
  Uncertainty quantification for visual language models (VLMs) conventionally targets the answer token distribution. We provide the first three-family empirical characterisation of answer entropy behaviour in thinking-mode VLMs. Running four models on identical POPE adversarial samples, we find three qualitatively distinct patterns: Qwen3-VL-8B-Thinking shows complete collapse (ans H AUROC = 0.492); GLM-4.1V-9B-Thinking shows no collapse (0.716); and InternVL3-8B shows selective thinking (chains o...
  </details>

- **2026-07-09** — Yifan Zhou, Qihao Yang, Yan Li et al. — [Ideas Have Genomes: Benchmarking Scientific Lineage Reasoning and Lineage-Grounded Idea Generation](http://arxiv.org/abs/2607.08758v1)
  <details><summary>📄 Abstract</summary>
  Scientific ideas rarely start from a blank page. They inherit mechanisms, repair known limitations, and recombine pieces of earlier work, much like biological genomes. Current benchmarks still say little about whether AI systems can follow this inheritance structure. We present IdeaGene-Bench (IG-Bench), a benchmark for scientific lineage reasoning and lineage-grounded idea generation. IG-Bench is organized around the IdeaGene framework: each paper or proposal is represented as a set of minimal,...
  </details>

- **2026-07-09** — Ayda Eghbalian, Kevin Desai — [Pose-to-Biomechanics: Bridging 3D Human Pose Estimation and Biomechanical Attribute Prediction](http://arxiv.org/abs/2607.08725v1)
  <details><summary>📄 Abstract</summary>
  Recent progress in 3D human pose estimation has made markerless recovery of skeletal motion increasingly accurate and scalable. However, most pose estimators remain optimized for geometric keypoint accuracy, while many real-world applications in rehabilitation, sports science, ergonomics, and clinical movement analysis require biomechanical quantities that describe how the body moves, loads, and activates. In this work, we propose BioModule, a lightweight plug-in temporal transformer that attach...
  </details>

- **2026-07-09** — Peng Cui, Jitao Wang, Siyan Xue et al. — [Towards Precision Therapy in Hepatocellular Carcinoma: A Clinical-Reasoning LLM for Risk Stratification and Treatment Guidance](http://arxiv.org/abs/2607.08602v1)
  <details><summary>📄 Abstract</summary>
  Hepatocellular carcinoma (HCC) is a common malignancy and a leading cause of cancer-related mortality. Current guidelines and staging systems provide coarse categories, but often miss within-stage heterogeneity and the clinical context in electronic medical records (EMRs). We present HCC-STAR (Hepatocellular Carcinoma Staging, Treatment And pRognosis), a clinically aligned large language model that reads routine EMR narratives and jointly outputs risk score-based staging, ranked guideline-consis...
  </details>

- **2026-07-09** — Palaash Goel, Ayush Maheshwari, Tanmoy Chakraborty — [It Takes a MAESTRO To Prune Bad Experts](http://arxiv.org/abs/2607.08601v1)
  <details><summary>📄 Abstract</summary>
  Sparsely-activated Mixture-of-Experts (MoE) language models achieve remarkable inference efficiency by activating only a small fraction of parameters per token, yet their full expert banks reside in memory at all times, creating a prohibitive deployment bottleneck. Existing structured pruning methods, largely designed for dense transformers, assess expert importance using locally derived heuristics that are blind to the interdependent nature of MoE routing. We introduce MAESTRO (Markov-chain App...
  </details>

- **2026-07-09** — Irina Vorobeva, Maxime Lenormand, Germana Berlantini et al. — [The geopolitics of knowledge: tipping points, national fingerprints, and the unequal globalization of science](http://arxiv.org/abs/2607.08512v1)
  <details><summary>📄 Abstract</summary>
  Science is often portrayed as a universal and self-contained system, driven solely by the internal logic of knowledge accumulation and isolated from the turbulences of the socio-political world. In this paper, we challenge this narrative by providing systematic quantitative evidence that the global scientific ecosystem is deeply shaped by geopolitical transformations. Using a large-scale dataset of scientific publications drawn from the OpenAlex database, spanning over five decades and covering ...
  </details>

- **2026-07-09** — Shenghui Chen, Po-han Li, Ximeng Sun et al. — [VEGAS: Human-Aligned Video Caption Evaluation via Gaze](http://arxiv.org/abs/2607.08489v1)
  <details><summary>📄 Abstract</summary>
  Vision-language models excel at video captioning, yet typically generate descriptions that fail to capture individual viewers' attention. We propose VEGAS (Video caption Evaluation via GAze Score), a training-free metric that leverages test-time gaze to sample personalized, attention-aligned text. It is a cross-modal, information-theoretic metric that quantifies how well a candidate caption matches a viewer's focus. To evaluate VEGAS, we curate a dataset of egocentric activities and instructiona...
  </details>

- **2026-07-09** — Weiming Sheng, Jinlang Wang, Manuel Barros et al. — [GitLake: Git-for-data for the agentic lakehouse](http://arxiv.org/abs/2607.08319v1)
  <details><summary>📄 Abstract</summary>
  We present GitLake, a Git-for-data design for an agent-first lakehouse. The system lifts single-table Iceberg snapshots into lakehouse-wide commits, branches, and merges, letting agents work on isolated branches while humans review and publish changes. Pipelines run on temporary branches and publish through a final merge, so all outputs become visible atomically or none do. Finally, we report production lessons as well as correctness insights from a preliminary Alloy model of our core abstractio...
  </details>

- **2026-07-09** — Gabriel Matos, Lauren Larson, Abhilasha Dave et al. — [Transformer-based machine learning using low-level calorimeter signals for collimated photon identification at collider experiments](http://arxiv.org/abs/2607.08175v1)
  <details><summary>📄 Abstract</summary>
  Electromagnetic calorimeters provide essential information for reconstructing and selecting both Standard Model (SM) and potential beyond the SM physics events at high-energy particle colliders. The fine-grained segmentation of modern calorimeters captures rich information about the internal structure of particle showers, much of which is discarded by conventional high-level reconstruction methods. In this work, we leverage calorimeter cell-level information to classify highly collimated diphoto...
  </details>

- **2026-07-09** — Fan Ma, Mauro Giuffrè, Donald Wright et al. — [A safety-oriented hypothetico-deductive framework for AI-assisted differential diagnosis](http://arxiv.org/abs/2607.08038v1)
  <details><summary>📄 Abstract</summary>
  Diagnostic error is a major threat to patient safety, yet current large language model (LLM) systems often treat diagnosis as a one-shot prediction task, lacking safeguards against missed high-risk alternatives or rigorous verification of their reasoning. Here, we present AegisDx, a safety-oriented framework for hypothetico-deductive clinical reasoning. AegisDx coordinates specialized LLM components through role-specific contracts, structured intermediate outputs, evidence-retrieval interfaces, ...
  </details>

- **2026-07-09** — Sutanay Choudhury, Anwesha Banerjee, Udishnu Sanyal et al. — [Reaction-network reasoning with frontier models for experimentally confirmed catalyst-selectivity hypotheses](http://arxiv.org/abs/2607.08003v1)
  <details><summary>📄 Abstract</summary>
  Catalysts are essential for sustainable chemical manufacturing, yet discovering novel architectures remains a bottleneck dominated by trial-and-error experimentation and computationally intensive screening. In complex reactions such as electrochemical carbon dioxide reduction, product selectivity is governed by dynamic interfacial, electrolyte, and potential factors as well as kinetic pathway competition. Conventional descriptor-based machine learning and computational potentials struggle to res...
  </details>

- **2026-07-09** — T. Zalewski, M. S. Mrudul, Y. Lee et al. — [A crystal-field route to THz-driven magnetization](http://arxiv.org/abs/2607.08519v1)
  <details><summary>📄 Abstract</summary>
  Light carries angular momentum, but the microscopic pathways that transform it into magnetization remain elusive. Here we establish that crystal-field excitations, historically viewed primarily as equilibrium spectroscopic fingerprints of localized 4$f$ electrons, constitute an active microscopic route through which circularly-polarized terahertz (THz) light creates magnetic polarization. Using wavelength-selective ultrafast Faraday spectroscopy on the paramagnetic insulator CeF$_3$, we show tha...
  </details>

- **2026-07-09** — Zi-han Ding, Ziwei Wang — [SkillPlug: Unsupervised Skill Mining for Few-Shot Adaptation in Robotic Manipulation](http://arxiv.org/abs/2607.08354v1)
  <details><summary>📄 Abstract</summary>
  Learning transferable visuomotor imitation policies that generalize across diverse manipulation tasks and adapt rapidly to new tasks from only a handful of demonstrations remains challenging. Most modern policies are trained end-to-end to map observations directly to low-level actions, offering little explicit structure for reusing and recombining behaviors across tasks and making transfer data-inefficient under limited supervision. We propose SkillPlug, a plug-in framework that augments an exis...
  </details>

- **2026-07-09** — Aditya Aladangady, Ricardo Duque Gabriel, Carlo Wix — [Measuring Consumption with Credit Card Data: Benchmarking and Beyond](http://arxiv.org/abs/2607.08759v1)
  <details><summary>📄 Abstract</summary>
  We introduce a novel monthly county-level consumption dataset constructed from spending data on over 350 million credit cards in the Federal Reserve's Y-14M reports, covering over 3,000 U.S. counties since 2014. We first show that the data closely approximate traditional consumption measures, explaining 92 percent of the variation in monthly adjusted personal consumption expenditures (PCE) growth at the national level and capturing meaningful cross-sectional variation in annual adjusted PCE grow...
  </details>

- **2026-07-09** — Baha Rababah, Cuneyt Gurcan Akcora, Carson K. Leung — [The Illusion of Equivalency: Statistical Characterization of Quantization Effects in LLMs](http://arxiv.org/abs/2607.08734v1)
  <details><summary>📄 Abstract</summary>
  Post-training quantization is widely used to deploy large language models in resource-constrained settings, yet its evaluation relies almost exclusively on accuracy and perplexity. We show that these metrics fail to capture behavioral changes induced by quantization. We introduce correctness agreement, a decision-level metric that measures overlap in correct predictions between a base model and its quantized variants, independent of absolute accuracy. Across multiple models and quantization sche...
  </details>

- **2026-07-09** — Chuning Zhu, Eva Xu, Jose Barreiros et al. — [Latent Memory Palace: Reasoning for Control as Autoregressive Variational Inference](http://arxiv.org/abs/2607.08724v1)
  <details><summary>📄 Abstract</summary>
  Human decision-making is highly flexible -- some actions are taken immediately; others require longer deliberation. Language models have exhibited a similar capacity for adaptive "reasoning." However, transferring this capability to continuous control policies has been challenging, as directly reasoning in language space may lack the granularity for spatial understanding and precise motions. In this work, we show that reasoning for control policies can emerge by organizing information in an auto...
  </details>

- **2026-07-09** — Xiaoshuai Song, Liancheng Zhang, Kangzhi Zhao et al. — [WebSwarm: Recursive Multi-Agent Orchestration for Deep-and-Wide Web Search](http://arxiv.org/abs/2607.08662v1)
  <details><summary>📄 Abstract</summary>
  Large language model (LLM)-based web search agents are transforming information seeking from simple factoid question answering into complex, deep-and-wide search and research-oriented tasks. A single ReAct-style agent is constrained by one long trajectory and limited context, making it difficult to handle depth and coverage simultaneously. Existing multi-agent systems improve search coverage through parallel execution and aggregation, but still exhibit clear limitations in recursive depth, colla...
  </details>

- **2026-07-09** — Corinna Dannert, Pablo M. Blanco, Sebastian P. Pineda et al. — [Short Peptide Tails Modulate DNA Association and Condensation by PAMAM Dendrimers](http://arxiv.org/abs/2607.08623v1)
  <details><summary>📄 Abstract</summary>
  Poly(amidoamine) (PAMAM) dendrimers are promising candidates for nucleic acid delivery; however, biocompatibility and transfection efficiency remain a challenge. Here, we investigated how the composition of short peptide tails conjugated to generation 2 PAMAM (G2) dendrimers influence DNA association and condensation across a range of pH values. Using a combination of potentiometric titrations, DNA precipitation assays, and coarse-grained molecular simulations with charge regulation, we show tha...
  </details>

- **2026-07-09** — Trinity Rosebud Stenhouse, Chamkaur Ghag, Frank F. Deppisch — [The 20 GeV Galactic Halo Excess: Pixel-Level Confirmation and Consistency with Sub-TeV WIMP Annihilation](http://arxiv.org/abs/2607.08552v1)
  <details><summary>📄 Abstract</summary>
  A recent analysis of 15 years of Fermi-LAT data reported a spherically symmetric, halo-like component of the Galactic diffuse emission that peaks near 20GeV. We independently reproduce this cell-aggregated analysis, then extend it to a pixel-level likelihood on the native $0.125^\circ$ maps, adding energy-dependent point-spread-function forward folding and masking bright sources. Both methods replicate the 20GeV halo spectrum, with the pixel-level normalisation ${\sim}20\%$ above the cellwise fi...
  </details>

- **2026-07-09** — Harrison Grodin, Ethan Chu, Runming Li et al. — [Potential Functions as Types](http://arxiv.org/abs/2607.08547v1)
  <details><summary>📄 Abstract</summary>
  Amortized analysis can be framed from the physicist's view, amenable to manual verification in dependent type theory using potential functions, and the banker's view, amenable to automated inference in substructural type theory using type-level credit annotations. In this work, we synthesize these perspectives in Calf, a dependent type theory cost verification. From the physicist's view, we present a fracture and gluing theorem that renders every type as containing a fusion of an abstraction fun...
  </details>

- **2026-07-09** — Yanpeng Su, Norman Franchi, Maximilian Lübke — [Fundamental Sensing Limits of 6G Cooperative MIMO-ISAC Networks: Joint Position-Velocity CRLB and Decoupling Analysis](http://arxiv.org/abs/2607.08510v1)
  <details><summary>📄 Abstract</summary>
  This paper presents a Cramér-Rao lower bound (CRLB)-based performance bound analysis of cooperative multiple-input multiple-output (MIMO) integrated sensing and communications (ISAC) networks. We first show the CRLB transformation of the signal-level parameters to the state parameters (position and velocity) in cooperative ISAC networks. Unlike existing studies that primarily ignored coupling between position and velocity in the Fisher information matrix (FIM), we derive the full FIM and the cor...
  </details>

- **2026-07-09** — Paula Font Solà, Adrià Molina Rodríguez, Josep Lladós — [Conversational Retrieval and On-the-Fly Knowledge Modeling of Historical Penitentiary Repression Records](http://arxiv.org/abs/2607.08459v1)
  <details><summary>📄 Abstract</summary>
  Recent developments in digital libraries increasingly favor conversational and natural language access to information through Retrieval-Augmented Generation (RAG). Although these approaches are effective for extractive tasks grounded in individual records, they remain limited in their ability to interpret document collections holistically and to incorporate expert knowledge dynamically. In this article, we present a document analysis system designed for the management of historical digital libra...
  </details>

- **2026-07-09** — Sebastian G. Gruber, Nassim Walha, Francis Bach et al. — [Eigenvalue Calibration for Semantic Embeddings of Large Language Models](http://arxiv.org/abs/2607.08377v1)
  <details><summary>📄 Abstract</summary>
  Uncertainty quantification is central to the reliable deployment of large language models (LLMs), and eigenvalues of semantic embeddings have recently emerged as a key tool in state-of-the-art methods. However, conventional calibration results developed for classification probabilities cannot be directly transferred to eigenvalues. We address this gap by proposing a novel framework for calibrating the eigenvalues of semantic embeddings. We interpret LLMs combined with semantic embeddings of thei...
  </details>

- **2026-07-09** — Amir Asiaee — [Certified Interventional Fidelity: Anytime-Valid, Adaptive Evaluation of Causal Claims in Mechanistic Interpretability](http://arxiv.org/abs/2607.08349v1)
  <details><summary>📄 Abstract</summary>
  Mechanistic interpretability often evaluates explanations by intervening on a model: swapping hidden states, patching activations, ablating components, or comparing a compressed model to the original one. These experiments are usually summarized by a point estimate, even though the evaluation may be monitored while it runs or adapted toward suspected failures. This makes it hard to tell whether a reported fidelity or patching effect is a stable causal claim or a consequence of finite sampling an...
  </details>

- **2026-07-09** — Kaustubh Kumar, Ashutosh Ranjan, Vivek Srivastava et al. — [ArtMine: Discovering and Formalizing Artistic Processes](http://arxiv.org/abs/2607.08331v1)
  <details><summary>📄 Abstract</summary>
  Understanding how artworks are created requires reasoning about the iterative decisions, material operations, and contextual influences that shape artistic production. While recent generative AI systems can synthesize artworks with high fidelity, they primarily model distributions over finished artifacts rather than the creative processes underlying their creation. In practice, artistic workflows are only partially documented through fragmented sources such as archival records, preparatory studi...
  </details>

- **2026-07-09** — Yuxiang Feng, Juncheng Wang, Chao Xu et al. — [Progression as Latent Drift: Generative Forecasting of Slow-Evolving Pathologies](http://arxiv.org/abs/2607.08270v1)
  <details><summary>📄 Abstract</summary>
  Forecasting the future anatomy of slow-evolving neurodegenerative diseases could enable earlier, more targeted intervention and improve clinical trial design, but it remains challenging because true progression signals are subtle in longitudinal MRI. In this low-signal regime, transferring modern generative sequence models directly is unreliable: training is dominated by stable baseline anatomy and confounded by dense, sample-specific nuisance variation. We first provide a theoretical analysis t...
  </details>

- **2026-07-09** — B. Maheshwari, P. Stevenson, P. Van Isacker — [Full-Spectrum Quantum Simulation for the Nuclear Shell Model](http://arxiv.org/abs/2607.08235v1)
  <details><summary>📄 Abstract</summary>
  The nuclear shell model is a general way of expressing the many-body nuclear Hamiltonian and deciphering the underlying nuclear structure. In today's era of modern and high-power computation, the primary limitation of the nuclear shell model is the enormous dimensionality of its Hilbert space, which far exceeds available storage capacity and prevents the diagonalization of the full Hamiltonian matrix in that space. Quantum computing offers a scalable solution to bypass this curse of dimensionali...
  </details>

- **2026-07-09** — Sumit Satishrao Shevtekar, Chandresh Kumar Maurya — [RhyMix: A Lightweight Adaptive Multi-Rhythm Network for Long-Term Time Series Forecasting](http://arxiv.org/abs/2607.08234v1)
  <details><summary>📄 Abstract</summary>
  Real-world time series exhibit complex dynamics characterized by multiple simultaneous temporal patterns: short-term fluctuations, periodic seasonal cycles, long-term trends, and irregular abrupt changes. However, many existing forecasting architectures rely on single-path temporal modeling--transformers capture long-range dependencies but smooth local variations, convolutions capture local patterns but have limited receptive fields, and linear models are efficient but cannot capture nonlinear d...
  </details>

- **2026-07-09** — David Serrano-Lozano, Luis Herranz, Michael S. Brown et al. — [Leveraging Color Naming for Image Enhancement](http://arxiv.org/abs/2607.08185v1)
  <details><summary>📄 Abstract</summary>
  Enhancing images to make them visually appealing is a persistent challenge in computer vision. Many deep-learning methods train models on paired datasets to replicate expert editing styles. However, these approaches struggle with two key issues: (1) interpretability and (2) a parametrization suitable for user adjustments. To address these challenges, we present NamedCurves+, an approach inspired by the concept of Color Naming, a universal set of familiar colors widely used in software tools for ...
  </details>

- **2026-07-09** — Kaihua Ding — [When LLMs Agree, Are They Right? Auditing Self-Consistency and Cross-Model Agreement as Confidence Signals](http://arxiv.org/abs/2607.08065v1)
  <details><summary>📄 Abstract</summary>
  LLM-as-judge (Zheng et al., 2023) is increasingly the default for evaluating AI systems in enterprise pipelines, often scaled to ensembles (Verga et al., 2024) or "mixture-of-experts" (Shazeer et al., 2017) panels of judges. These systems share a key assumption: that consistency -- agreement among judges, or among a model's own samples -- indicates correctness. We show this assumption is unreliable. Agreement is not accuracy: a model can agree with itself, and different models can agree with eac...
  </details>

- **2026-07-09** — Xiucheng Wang, Junxi Huang, Nan Cheng — [RadioDiff-v2: Generative Angular Radio Maps for Multi-Beam Selection and Localization](http://arxiv.org/abs/2607.08045v1)
  <details><summary>📄 Abstract</summary>
  Angular radio maps describe the received-power distribution over the angle of arrival and underpin beam selection and receiver localization in sixth-generation (6G) networks. Predicting the angular power spectrum (APS) from geometry is difficult, because the mapping is ill-posed in non-line-of-sight (NLOS) conditions and must generalize to unseen environments. Distortion-minimizing regressors return the conditional mean, which over-smooths the spectrum and erases the multipath structure that dow...
  </details>

- **2026-07-08** — Shyam Agarwal, Courtney Miller, Christian Kästner et al. — [3100 Opinions on Code Review in an AI World: Building Causal Theory from Practitioner Discourse](http://arxiv.org/abs/2607.07980v1)
  <details><summary>📄 Abstract</summary>
  Coding agents now author entire pull requests, and practitioners sharply disagree about what this does to code review: whether it becomes the bottleneck, whether human review is still necessary, and whether it quietly erodes the understanding that it once built. Repository-mining studies measure surface trends but seldom explain the mechanisms beneath them, and the trends themselves prove unstable. A motivating observational analysis of public GITHUB activity finds that agent-authored pull reque...
  </details>

- **2026-07-08** — Luke Baines, Anton Gonzalvez Hawthorne, Mariia Koroliuk et al. — [Persona Cartography: Charting Language Model Personality Traits in Weight Space](http://arxiv.org/abs/2607.07916v1)
  <details><summary>📄 Abstract</summary>
  Large language models exhibit recurring behavioural patterns -- personas -- that shape generalisation and safety, but we lack reliable tools for decomposing, measuring, and controlling them. Our central insight is to treat personas as positions in a space of behavioural traits, using the OCEAN framework to describe model personas in terms of Openness, Conscientiousness, Extraversion, Agreeableness, and Neuroticism. We train low-rank adapters to amplify or suppress individual traits, and evaluate...
  </details>

- **2026-07-08** — Xiaohan Zhang, Sebastian Starke, Alexander Winkler et al. — [GIRAF: Towards Generalizable Human Interactions with Articulated Objects](http://arxiv.org/abs/2607.07880v1)
  <details><summary>📄 Abstract</summary>
  Synthesizing realistic full-body human interactions with articulated objects is a fundamental challenge for embodied AI and graphics, with applications in robotics training and virtual agents. Existing models remain limited: some focus on simple activities with static objects, while others restrict attention to hand-only manipulation. This leaves open the problem of generating coordinated full-body motion that approaches, manipulates, and moves articulated objects in a realistic and generalizabl...
  </details>

- **2026-07-08** — Shengyuan Zhao — [On cube and Cremona rigidity for higher-rank lattices](http://arxiv.org/abs/2607.07940v1)
  <details><summary>📄 Abstract</summary>
  For irreducible lattices in semisimple Lie groups of real rank at least $2$, we prove a cohomological vanishing result implying that any action on a CAT(0) cube complex fixes a vertex whenever every hyperplane stabilizer is solvable. As an application, we prove regularizability for actions of all higher-rank lattices by birational transformations on projective surfaces. We first use superrigidity for actions on infinite-dimensional real hyperbolic spaces to reduce to the de Jonquières group, and...
  </details>

- **2026-07-08** — Weicheng Ma, John Guerrerio, Soroush Vosoughi — [Scalable and Culturally Specific Stereotype Dataset Construction via Human-LLM Collaboration](http://arxiv.org/abs/2607.07895v1)
  <details><summary>📄 Abstract</summary>
  Research on stereotypes in large language models (LLMs) has largely focused on English-speaking contexts, due to the lack of datasets in other languages and the high cost of manual annotation in underrepresented cultures. To address this gap, we introduce a cost-efficient human-LLM collaborative annotation framework and apply it to construct EspanStereo, a Spanish-language stereotype dataset spanning multiple Spanish-speaking countries across Europe and Latin America. EspanStereo captures both w...
  </details>

- **2026-07-08** — S M Farah Al Fahim, Md Nakhla Rafi, Md Ahasanuzzaman et al. — [Bug Report Specification Refinement with Trajectory Guidance for Automated Program Repair](http://arxiv.org/abs/2607.07882v1)
  <details><summary>📄 Abstract</summary>
  Bug reports serve as task specifications for repository-level automated program repair (APR) agents, but they often describe only the observed failure and omit repair-relevant information such as the failure-inducing behavior, behavioral requirement, and implementation scope. As a result, a repair agent may inspect irrelevant code, infer an incorrect requirement, or generate a patch that addresses the reported symptom without restoring the intended repository behavior. We present TrajSpec, a tra...
  </details>

- **2026-07-08** — Alessio Emanuele Biondo, Mauro Gallegati — [Inflation as an emergent phenomenon](http://arxiv.org/abs/2607.07864v1)
  <details><summary>📄 Abstract</summary>
  We develop an agent-based model in which inflation emerges from decentralized price-setting and credit-financed production in an endogenous-money economy. Firms operate under working-capital constraints, form market-based price expectations through heterogeneous adaptive learning, and set prices via cost-plus rules with endogenous mark-ups. Bank lending simultaneously creates deposits, while heterogeneous lending rates and credit rationing shape firms' financing costs and, through unit costs, th...
  </details>

- **2026-07-08** — Gaurav Arya, Mathieu Huot, Moritz Schauer et al. — [GradInf: Gradient Estimation as Probabilistic Inference](http://arxiv.org/abs/2607.07840v1)
  <details><summary>📄 Abstract</summary>
  Gradient estimation -- the task of computing the gradient of the expected value of a probabilistic program -- has diverse applications in scientific computing, but is notoriously difficult because of issues such as high-dimensional integration, discrete random choices, and complex stochastic dependencies. This article introduces gradient inference, a new approach to developing sound and efficient gradient estimators for probabilistic programs. Gradient inference rests on a formal reduction from ...
  </details>

- **2026-07-08** — Jingyao Cai, Shuaijun Liu, Abdul Rehman et al. — [From Triggers to Emotions: A CPM-Grounded Appraisal Multi-Agent for Dynamic Emotional Evolution in Persona-Based Dialogue](http://arxiv.org/abs/2607.07824v1)
  <details><summary>📄 Abstract</summary>
  Large Language Models (LLMs) have substantially advanced persona-based dialogue agents for emotion-sensitive role simulation in healthcare, education, counseling, customer service, and interactive storytelling. However, two related lines of work leave a key gap. Persona-based dialogue systems often encode emotions as static traits or surface-level stylistic cues, and affective dialogue research has largely focused on empathetic response generation toward users rather than modeling the agent pers...
  </details>

- **2026-07-08** — Osman Cevheroğlu, Arkadaş Özakın — [An analytical solution of a quantum system with non-Markovian behavior: The Bixon-Jortner system in time domain](http://arxiv.org/abs/2607.07546v1)
  <details><summary>📄 Abstract</summary>
  Non-Markovian behavior in quantum systems is often studied in the context of bipartite systems consisting of a system of interest and an environment -- tracing over the environment results in non-Markovian behavior for the subsystem of interest. One may get a Markovian limit in certain regimes, which is studied using the Lindblad master equation, and corrections to this behavior can be obtained by techniques such as the Nakajima-Zwanzig formalism. In this paper, we obtain an exact non-Markovian ...
  </details>

- **2026-07-08** — Zelin Gao, Qiuyu Wang, Jiapeng Zhu et al. — [Infinite Worlds with Versatile Interactions](http://arxiv.org/abs/2607.07534v1)
  <details><summary>📄 Abstract</summary>
  We present LingBot-World 2.0 (also known as LingBot-World-Infinity), an advanced iteration of LingBot-World featuring four distinct upgrades. (1) Our model achieves an unbounded interaction horizon while maintaining consistent output quality, benefiting from a carefully crafted causal pretraining paradigm. (2) Through distilling a real-time variant from the base model, our system guarantees rapid response time, sufficient to drive 720p video streams at 60 fps. (3) Compared to the previous versio...
  </details>

- **2026-07-08** — Tamal Maharaj — [A Word-Level Digital Reader of the Prasthanatrayi with Sankara's Bhasya: Corpus, Method, and an Open, Offline Reading Aid for the Advaita Vedanta Canon](http://arxiv.org/abs/2607.07282v1)
  <details><summary>📄 Abstract</summary>
  The Prasthanatrayi -- the ten principal Upanisads, the Brahmasutra, and the Bhagavadgita, with Sankara's commentaries (bhasya) -- is the foundational corpus of Advaita Vedanta. Continuous euphonic combination (sandhi), long compounds (samasa), and dense scholastic prose make it hard to read at the word level: where one word ends, and what each word means grammatically, are both obscured. We present an open, fully offline, word-level digital reader of the entire Prasthanatrayi with Sankara's bhas...
  </details>

- **2026-07-08** — Jerry Han, Rafael Moschopoulos, Ella Colby et al. — [Measuring Intelligence Beyond Human Scale](http://arxiv.org/abs/2607.07040v1)
  <details><summary>📄 Abstract</summary>
  How can we measure intelligence beyond human capability?   Human-authored benchmarks saturate, and above human capability, examiners may not know which tasks are both hard and verifiable. We argue that this difficulty is inherent to absolute-scale evaluation and propose a new paradigm based on relative measurement in which models generate public challenges that separate other systems. Aggregating these outcomes yields an adversarial psychometric rating system that can scale with the systems bein...
  </details>

- **2026-07-08** — Anna Kuzina, Paul N. Whatmough, Babak Ehteshami Bejnordi — [The Key to Going Linear: Analysis-Driven Transformer Linearization](http://arxiv.org/abs/2607.07706v1)
  <details><summary>📄 Abstract</summary>
  The quadratic cost of causal self-attention severely bottlenecks long-context transformer inference. While numerous post hoc linearization pipelines exist, it is difficult to identify which components preserve model quality. This work isolates the effect of state update design in a strict frozen-backbone regime. We show that softmax relies on key-dependent, rank-1 orthogonal projections, elucidating why delta-style networks outperform purely gated accumulation. We identify a potential source of ...
  </details>

- **2026-07-08** — Si-Yu Yuan, Wen-Tan Xue, Ching Hua Lee — [Non-Hermitian Edge State Endocytosis](http://arxiv.org/abs/2607.07703v1)
  <details><summary>📄 Abstract</summary>
  An isolated edge state observed in a finite open chain is usually expected to survive the thermodynamic limit (TDL), with a localization mechanism distinct from non-Hermitian skin accumulation, which localizes the \emph{entire} bulk continuum. We show that scale-sensitive non-Hermitian systems can generically admit a different fate: as we scale up the system size, a detached edge-localized eigenstate can remain sharply visible over a broad window until a critical scale is reached, where it forms...
  </details>

- **2026-07-08** — Tianming Sha, Yue Zhao, Lichao Sun et al. — [SkillCenter: A Large-Scale Source-Grounded Skill Library for Autonomous AI Agents](http://arxiv.org/abs/2607.07676v1)
  <details><summary>📄 Abstract</summary>
  Autonomous AI agents can execute complex tasks with limited human review, yet they often lack the grounded operational knowledge to make their outputs not just executable but correct, secure, and maintainable. We introduce SkillCenter, to our knowledge the largest open skill library for agents by total count: 216,938 structured skills across 24 domain bundles. A SkillGate-filtered pipeline contributes 114,565 source-grounded skills from peer-reviewed journals, ArXiv, and over 24,000 technical so...
  </details>

- **2026-07-08** — Halimat Olamide Yusuf, Augustine O. Nwajana — [Six-Pole Dual-band Bandpass Filter for WiMAX Applications](http://arxiv.org/abs/2607.07661v1)
  <details><summary>📄 Abstract</summary>
  Recent advances in multi-band wireless communication systems have driven the increasing need for dual-band bandpass filters. These types of filters are capable of isolating a small section of the frequency spectrum within a broader spectrum. Over the years, coplanar waveguide, microstrip, slotline, stripline, and other planar transmission line technologies have been widely employed in the design of microwave circuits and systems. This work employs a Folded-Arms Square Open-Loop Resonator (FASOLR...
  </details>

- **2026-07-08** — Azwar Abdulsalam, Nishil Patel, Andrew Saxe — [RL Post-Training Builds Compositional Reasoning Strategies](http://arxiv.org/abs/2607.07646v1)
  <details><summary>📄 Abstract</summary>
  Does RL post-training merely amplify primitive skills already latent in a base model, or can it compose primitive skills into new higher-level strategies? We study this question in a fully observable rewrite-grammar environment where the pretraining distribution is known and every generated rewrite can be audited. A Transformer is pretrained on primitive symbol-rewrite chains and post-trained on a Trace-based reasoning task with only a binary final-answer reward. RL solves held-out problems that...
  </details>

- **2026-07-08** — Aneesh Ramaswamy, Nageswara S. V. Rao, Joseph C. Chapman et al. — [Analysis of polarization drift of optical signals over deployed aerial-inground fiber connections](http://arxiv.org/abs/2607.07629v1)
  <details><summary>📄 Abstract</summary>
  Polarization measurements of a classical 1550-nm signal are collected and analyzed on 15-km hybrid aerial-inground fiber connections over 11 months. The spectral area and spectral moments9 of mHz-resolution Fast-Fourier-Transform (FFT) of these measurements are extracted, and related to temperature, humidity, wind speed, and time of day. Spectral area correlations show a strong11 diurnal structure: daytime maxima align with temperatures/wind speed peaks and humidity dips, with lower levels durin...
  </details>

- **2026-07-08** — Lara Khatib, Noble Saji Mathews, Meiyappan Nagappan et al. — [What Makes a Good Bug Report for an AI Agent?](http://arxiv.org/abs/2607.07593v1)
  <details><summary>📄 Abstract</summary>
  Automated program repair (APR) agents are transitioning from research benchmarks to developer workflows, yet they still begin with bug reports written for human developers. While decades of research have established what makes a good bug report for humans (e.g., steps to reproduce, stack traces), it remains unclear whether these features transfer to LLM-based agents. We study this question in two analyses. First, we use statistical modeling to examine associations between 27 bug-report features ...
  </details>

- **2026-07-08** — Dmitry Beresnev, Vladimir Makharev, Roman Khalikov et al. — [Search, Fail, Recover: A Training Framework for Correction-Aware Reasoning](http://arxiv.org/abs/2607.07492v1)
  <details><summary>📄 Abstract</summary>
  Many reasoning tasks are not well described by a single left-to-right chain: a solver may need to pursue a plausible branch, observe delayed failure, and return to the latest prefix that can still be completed. We introduce Pyligent, a training and inference framework inspired by the Diligent Learner formulation that represents reasoning as validated search over partial solution chains. A task validator labels generated continuations and failures, and the resulting search trees are converted int...
  </details>

- **2026-07-08** — Songhan Wang, Haoang Chi, He Li et al. — [SpaCellAgent: A Self-Evolving LLM-Based Multi-Agent Framework for Trajectory Analysis](http://arxiv.org/abs/2607.07467v1)
  <details><summary>📄 Abstract</summary>
  Spatial and Single-cell transcriptomics are transformative in deciphering cellular dynamics. As the fundamental paradigm for reconstructing cell developmental paths, trajectory inference (TI) is critical. However, existing methods require extensive manual intervention and proficiency in heterogeneous tools, posing a significant barrier to efficient TI analysis. To bridge this gap, we propose SpaCellAgent, an autonomous large language model (LLM) multi-agent framework that automates end-to-end sp...
  </details>

- **2026-07-08** — Xing Zhang, Yanwei Cui, Guanghui Wang et al. — [The Blind Curator: How a Biased Judge Silently Disables Skill Retirement in Self-Evolving Agents](http://arxiv.org/abs/2607.07436v1)
  <details><summary>📄 Abstract</summary>
  A self-evolving agent retires its bad skills by watching them fail, so what happens when the judge cannot see the failures? Skill retirement is the structural constraint that keeps a growing library from drifting below the no-skill baseline, but its guarantee assumes an unbiased reward, which is false for the LLM judges that reference-free tasks force upon us. We show that a biased judge does not merely add noise; it \emph{silently switches off the curator}. We make this precise with a corrupted...
  </details>

- **2026-07-08** — Kajetan Rachwał, Maciej Majek, Bartłomiej Boczek et al. — [Multi-Agent Robotic Control with Onboard Vision-Language Models](http://arxiv.org/abs/2607.07403v1)
  <details><summary>📄 Abstract</summary>
  Vision Language Models (VLMs) and Vision Language Action (VLA) models have shown promise in robotic control. Yet, they face significant challenges regarding explainability, generalization, and compute requirements. This paper presents a Multi-Agent System (MAS) architecture that addresses these limitations by deploying specialized agents on onboard hardware - eliminating dependence on external compute. The system controls a multi-purpose autonomous mobile manipulator in a simulated industrial wa...
  </details>

- **2026-07-08** — Elaine Ang, Chenxi Huang, Georgios Liargkovas et al. — [Agentic Data Environments](http://arxiv.org/abs/2607.07397v1)
  <details><summary>📄 Abstract</summary>
  Autonomous agents promise substantial gains in speed, scale, and labor efficiency, but their failures can impose abrupt and often irreversible costs. The central challenge for agentic automation is therefore to increase the benefits of automation while bounding the consequences of failure.   While databases remain central to modern computing, agents operate over a broader data environment spanning files, APIs, applications, and system state. In this talk, I will outline early work on Agentic Dat...
  </details>

- **2026-07-08** — Diab W. Abueidda, Bilal Ahmed, Panos Pantidis et al. — [Physics-Audited Agentic Discovery in Scientific Machine Learning](http://arxiv.org/abs/2607.07379v1)
  <details><summary>📄 Abstract</summary>
  In agentic scientific machine learning (SciML), large language model (LLM) agents can discover surrogate models and select one by an automated score, typically an error metric. A low error, however, does not establish that the predicted fields satisfy the physics that matter for mechanics, such as boundary conditions, superposition, stiffness scaling, or causality. We introduce Physics-Audited Agentic SciML (PA-SciML), a verification-first workflow for agentic SciML discovery. The workflow fixes...
  </details>

- **2026-07-08** — Pranav Sawant, Jakub Krejčí — [Mechanistic Interpretability for Neural Networks: Circuits, Sparse Features and Symbolic Reasoning](http://arxiv.org/abs/2607.07316v1)
  <details><summary>📄 Abstract</summary>
  This article offers a comprehensive overview of mechanistic interpretability, an emerging field that seeks to reverse-engineer the internal algorithms of modern neural networks. While traditional explainable AI methods often stop at surface-level input-output correlations, this approach directly addresses the opaque "black box" nature of machine learning models, which is essential for ensuring safety and auditability in high-stakes deployments. The paper provides a detailed examination of Transf...
  </details>

- **2026-07-08** — Arianna Pera, Mauro Martino, Nima Dehmamy et al. — [Billions of Sketches Reveal Hidden Cultural Variation in Human Concepts](http://arxiv.org/abs/2607.07267v1)
  <details><summary>📄 Abstract</summary>
  Claims about the universality of human concepts have been predominantly assessed through linguistic similarity across languages and cultures. However, words are effective as communication devices because they compress rich experiential variation into shared conventions, potentially obscuring hidden individual and cultural differences in how concepts are mentally represented. Here, we analyse 2.6 billion human-made sketches of common concepts from 236 countries and territories to examine conceptu...
  </details>

- **2026-07-08** — Zhenghao Zhou, Yiyan Li, Tao Xu et al. — [A Physics-guided Fine-tuned LLM-based Framework for Customized Power Distribution System Feeder Generation](http://arxiv.org/abs/2607.07237v1)
  <details><summary>📄 Abstract</summary>
  Power distribution system feeder models (e.g., IEEE 33-bus system, IEEE 13-bus system, etc.) are cornerstones for conducting power distribution system studies. As real-world feeder models are hard to acquire due to energy security concerns, generating high-quality synthetic feeders becomes an important alternative to satisfy the fast-growing and diversified needs of power system researchers and engineers. In this paper, we propose an LLM-based synthetic feeder generation framework that can achie...
  </details>

- **2026-07-08** — Jáchym Bártík, Alžběta Šrůtková, Irena Holubová — [Benchmark Engineering as a Design Instrument for Heterogeneous Information Systems](http://arxiv.org/abs/2607.07175v1)
  <details><summary>📄 Abstract</summary>
  Contemporary information systems operate in heterogeneous and continuously evolving data environments, where representation choices and structural redesign decisions strongly influence system behavior. Existing benchmarking approaches, however, rely mostly on static datasets and fixed schemas, providing limited support for analyzing architectural trade-offs or guiding evolution in multi-model settings.   This paper introduces TransforMMer, a framework for evolution-aware and representation-aware...
  </details>

- **2026-07-08** — Rakshitha De Silva, Shiva Raj Pokhrel, Jonathan Kua — [Small Language Model-based Control for BBR over Low Earth Orbit Satellite Internet](http://arxiv.org/abs/2607.07142v1)
  <details><summary>📄 Abstract</summary>
  Low Earth Orbit (LEO) satellite Internet introduces rapid path variability, intermittent capacity shifts, and non-terrestrial delay dynamics that challenge transport-layer congestion control. Although Bottleneck Bandwidth and Round-trip propagation time (BBR) achieves high throughput in such environments, its aggressive bandwidth probing can cause excessive retransmissions and unstable pacing over LEO links. This paper presents a global experimental evaluation of BBR over a SpaceX Starlink testb...
  </details>

- **2026-07-08** — Stepanida Alekseeva, Jenifer Kalafatovich, Seong-Whan Lee — [Tree-of-Thoughts Reasoning for Text-to-Image In-Context Learning](http://arxiv.org/abs/2607.07117v1)
  <details><summary>📄 Abstract</summary>
  In text-to-image in-context learning (T2I-ICL), a model has to infer a latent compositional pattern from fewshot demonstrations for generating a query image. Recent studies show that state-of-the-art multimodal large language models struggle with this setting, particularly due to limited compositional reasoning and sensitivity to prompt construction. In this work, we propose a Tree-of-Thoughts (ToT) reasoning framework for T2I-ICL that introduces a multi-stage reasoning and selection layer that ...
  </details>

- **2026-07-08** — Heye Huang, Jingguang Li, Zhiyuan Zhou et al. — [A knowledge-augmented dataset of high-risk driving scenarios with LLM annotations for autonomous driving](http://arxiv.org/abs/2607.07103v1)
  <details><summary>📄 Abstract</summary>
  Safe autonomous driving requires both rapid responses to common high-risk events and deeper reasoning over rare, extreme long-tail scenarios in traffic safety. These scenarios are severely under-represented in naturalistic driving data, and existing trajectory and language-augmented datasets seldom provide high-risk event labels, semantic annotations, and verifiable safety signals. Here we present K-Risk, a knowledge-augmented dataset that combines structured driving trajectories with large lang...
  </details>

- **2026-07-08** — Szczepan Konior, Alexandre Quemy, Przemysław Klocek et al. — [Riemannian Geometry for Pre-trained Language Model Embeddings](http://arxiv.org/abs/2607.07047v1)
  <details><summary>📄 Abstract</summary>
  Understanding the geometric structure of pre-trained language model embeddings matters for interpretability and safety. We ask whether sentence-level classification signal lives in the Riemannian geometry of contextual token embeddings, and probe it by extracting per-token pullback metrics from a learned encoder's analytical Jacobian and aggregating them with the Fréchet mean on the symmetric positive definite (SPD) manifold; we call this procedure Riemannian Mean Pooling (RMP). Across three dat...
  </details>

- **2026-07-08** — Yusen Feng, Bingchen Han, Jiangran Lyu et al. — [WAM-TTT: Steering World-Action Models by Watching Human Play at Test Time](http://arxiv.org/abs/2607.06988v1)
  <details><summary>📄 Abstract</summary>
  Steering robot foundation models (RFMs) toward new task variants or user-preferred behaviors remains challenging, often requiring additional robot demonstrations, task-specific fine-tuning, or long-context conditioning. We present WAM-TTT, a test-time training framework for steering world action models from raw human videos. Rather than treating human videos as trajectories to imitate, WAM-TTT absorbs them into a lightweight adaptive memory inside a frozen WAM through self-supervised video predi...
  </details>

- **2026-07-08** — Amin Tabrizian, Arsyi Aziz, Aarifah Ullah et al. — [End-to-End LLM Flight Planning with RAG-based Memory and Multi-modal Coach Agent](http://arxiv.org/abs/2607.06964v1)
  <details><summary>📄 Abstract</summary>
  Bridging the gap between human pilot intent and autonomous flight operation is critical for real-world electric vertical takeoff and landing (eVTOL) aircraft deployment. Flight planning traditionally relies on classic algorithms that struggle to incorporate flexible human preferences. We present FRAMe, an End-to-End Large Language Model (LLM) Flight Planning tool with RAG-based Memory and Multi-modal Coach Agent. Our system integrates a planner LLM with a multi-modal coach agent and retrieval au...
  </details>

- **2026-07-08** — Yingshu Li, Yunyi Liu, Zhenghao Chen et al. — [Seeing What Matters: Lesion-Aware High-Resolution Patch Discovery and Fusion for Chest X-ray Report Generation](http://arxiv.org/abs/2607.06909v1)
  <details><summary>📄 Abstract</summary>
  Despite rapid advances in chest X-ray (CXR) foundation models, most radiology report generation (RRG) systems still rely on heavily downsampled inputs (e.g., 256x256) due to the fixed visual token budgets of pretrained vision encoders, suppressing subtle yet clinically important cues present in native-resolution images. However, enabling high-resolution (high-res) perception remains challenging: naive tiling causes prohibitive token inflation, while global compression suppresses subtle lesions a...
  </details>

- **2026-07-08** — Muayad Sayed Ali, Aliaksandra Novik, Anji Boddupally et al. — [The Harness Effect: How Orchestration Design Sets the Token Economics of Enterprise Agentic AI](http://arxiv.org/abs/2607.06906v1)
  <details><summary>📄 Abstract</summary>
  Agentic AI development today runs on token maxing: buying capability with tokens -- longer reasoning traces, more turns, wider tool payloads, bigger replayed contexts -- so tokens per task grow faster than task value. Falling per-token prices mask the pattern; total spend rises anyway. We argue the decisive lever against token maxing is the harness: the orchestration layer that assembles context, exposes tools, sequences turns, delegates work, and carries enterprise observability and governance....
  </details>

- **2026-07-08** — Niraj Pudasaini, Geeta Chandra Raju Bethala, Pranav Doma et al. — [Immersive Social Interaction with VR and LLM-Assisted Humanoids](http://arxiv.org/abs/2607.07430v1)
  <details><summary>📄 Abstract</summary>
  Humanoid robots can extend human presence to remote, constrained, or hazardous environments, but existing teleoperation interfaces often require physically demanding motion tracking or cognitively demanding low-level control. This paper presents an immersive teleoperation framework that integrates voice-controlled locomotion, VR-based manipulation, and bidirectional social interaction for whole-body humanoid control. Using Apple Vision Pro, the operator receives egocentric visual feedback, issue...
  </details>

- **2026-07-08** — Vrinda Malhotra — [Modeling Misinformation as a Commons Problem](http://arxiv.org/abs/2607.06984v1)
  <details><summary>📄 Abstract</summary>
  Misinformation often harms society not just by spreading a single false belief, but by breaking down the shared trust people rely on to evaluate what is true. This paper presents an agent-based simulation that frames trust as a collective resource and attention as a scarce private budget: when aggregate attention shifts toward low credibility content, the trust environment degrades, making credible information harder to process and correct. Across experiments, the model produces four recurring m...
  </details>

- **2026-07-08** — Liting Lin, Boxi Yu, Yuzhong Zhang et al. — [Mining Workflow Graphs for Black-Box Boundary Testing of Conversational LLM Agents](http://arxiv.org/abs/2607.06873v1)
  <details><summary>📄 Abstract</summary>
  Conversational LLM agents can cause real-world harm when their internal workflows fail, such as completing a transaction without confirmation. Testing these state-dependent failures is difficult because critical boundaries, such as identity checks and confirmation gates, are hidden behind multi-turn conversational prerequisites, rendering them inaccessible to standard tests. We present AgentEval, a black-box testing framework that discovers and stresses these stateful boundaries. AgentEval inter...
  </details>

- **2026-07-08** — Chen Tang, Yizhou Wang, Jianyu Wu et al. — [Accurate, Interdisciplinary and Transparent Structure-property Understanding with Deep Native Structural Reasoning](http://arxiv.org/abs/2607.07708v1)
  <details><summary>📄 Abstract</summary>
  Structure-property relationships are foundational to biology, chemistry and materials science, where function, reactivity and physical response emerge from spatial, chemical and periodic organization. Mechanistically explaining these relationships requires interpreting structural evidence through scientific principles and physical constraints, from stereochemistry and bonding to symmetry, energetics and periodic order. However, applying artificial intelligence to this process presents a joint ch...
  </details>

- **2026-07-08** — Yair Feldman, Linxi Zhao, Nathan Godey et al. — [Co-LMLM: Continuous-Query Limited Memory Language Models](http://arxiv.org/abs/2607.07707v1)
  <details><summary>📄 Abstract</summary>
  Limited memory language models (LMLMs) externalize factual knowledge during pretraining to a knowledge base (KB), rather than memorizing it in their weights. During generation, the model then fetches knowledge from the KB as needed. This recently introduced paradigm provides multiple advantages, including knowledge control capabilities that remain beyond conventional LLMs. We propose continuous-query LMLM (CO-LMLM), where the KB pairs continuous keys with textual knowledge values, a significant ...
  </details>

- **2026-07-08** — Xinyi Wu, Siyuan Liu, Ali Jadbabaie — [How Data Shapes RoPE Frequency Usage: From Positional Scale Matching to Length Generalization](http://arxiv.org/abs/2607.07678v1)
  <details><summary>📄 Abstract</summary>
  Rotary Position Embeddings (RoPE) provide transformers with a fixed grid of positional frequencies, yet trained models use these frequencies highly non-uniformly. We study what determines this frequency usage and propose a data-centered explanation: RoPE frequencies are selected to match the relative-distance structure of the training data. Viewing each frequency as a positional lens, we formalize a field-resolution tradeoff and show that, for a data-induced dependency profile of width $W$, the ...
  </details>

- **2026-07-08** — Andrea Scarinci, Virginia Negri, Brayan Impata et al. — [SynthAVE: Scalable Synthetic Labeling for E-Commerce with LLM-Arena Validation](http://arxiv.org/abs/2607.07469v1)
  <details><summary>📄 Abstract</summary>
  Fine-tuning large language models (LLMs) for e-commerce attribute extraction requires labeled data representative across thousands of product types, attributes, and multiple languages. This combinatorial scale translates to millions of annotations, rendering human labeling prohibitively costly. While recent work has demonstrated synthetic label generation using LLMs, deploying such approaches at industrial scale requires integrated quality control mechanisms. We present SynthAVE, a large-scale h...
  </details>

- **2026-07-08** — Tanay Sodha, Aditya Sharma, Ramya Hebbalaguppe et al. — [When Prompts Ignore Structure: Graph-Based Attribute Reasoning for Calibrated VLMs](http://arxiv.org/abs/2607.07395v1)
  <details><summary>📄 Abstract</summary>
  Reliable confidence estimation remains a key limitation of test-time adaptation in vision-language models (VLMs), where prompt tuning improves zero-shot accuracy but often degrades calibration due to entropy-driven overconfidence. Prior approaches mitigate this using LLM-derived class attributes and contrastive regularization, yet treat attributes independently, ignoring their relational structure. We propose ARGTCA, which represents (class, attribute) pairs as nodes in a Symbolic Attribute Grap...
  </details>

- **2026-07-08** — Ritajit Dey, Iadh Ounis, Graham McDonald — [Interpretable Uncertainty for Adaptive Retrieval and Reasoning in Question Answering](http://arxiv.org/abs/2607.07380v1)
  <details><summary>📄 Abstract</summary>
  Large language models (LLMs) achieve a strong performance in question answering (QA), but remain prone to hallucinations and suffer from limited transparency. Retrieval-augmented generation (RAG) can improve factuality, yet decisions about when and how to retrieve from external resources are typically based on opaque policies or computationally inefficient multi-step prompting procedures. We propose an uncertainty-aware framework for adaptive QA based on explicit signals derived from LLM interna...
  </details>

- **2026-07-08** — Oskar von Seeler, Christian Tetzlaff, Andrew Lehr — [Dynamic neural manifolds for flexible closed-loop control on neuromorphic hardware](http://arxiv.org/abs/2607.07373v1)
  <details><summary>📄 Abstract</summary>
  In biological circuits, sequential neural activity evolves along dynamic, low-dimensional manifolds to enable flexible behavior. Spiking network models link aspects of this sequential activity to features of manifold geometry through specific circuit mechanisms, making dynamic neural manifolds parameterizable, and thereby offering an explainable framework for neural computation. Extending this framework to neuromorphic engineering, we present an implementation on the SpiNNaker 2 chip for real-ti...
  </details>

- **2026-07-08** — Klaus M. Frahm, Dima L. Shepelyansky — [Thermodynamic description of worldwide distribution of energy and carbon emission](http://arxiv.org/abs/2607.07315v1)
  <details><summary>📄 Abstract</summary>
  Based on public data, we analyze the distributions of energy and carbon emission over world countries on a scale of the last 40-50 years using their presentation via Lorenz and Pareto curves. These curves in rescaled format remain remarkably stable on this time period being characterized by high values of the Gini coefficient indicating a strong inequality of energy distribution. To explain these distributions, we introduce the ENergy Thermalization Hypothesis (ENTH) according to which these dis...
  </details>

- **2026-07-08** — Sambit Sarkar, Mansi Talwar, Pravata K. Mohanty — [The Deep Learning Cosmic Ray Energy Reconstruction Pipeline for the GRAPES-3 Experiment](http://arxiv.org/abs/2607.07265v1)
  <details><summary>📄 Abstract</summary>
  The mass independent energy reconstruction of cosmic rays is crucial for understanding their origin, acceleration, and propagation. Precise measurement of the primary energy can also lead to better mass classification and could enable energy dependent anisotropy maps for individual elements. The GRAPES-3 experiment located in Ooty consisting of 400 scintillator detector array placed 8 m apart covering an area of 25000 m$^2$ with a dedicated muon detector made of 3712 proportional counters, is de...
  </details>

- **2026-07-08** — Ignacio D. Lopez-Miguel, Ezio Bartocci, Thomas Eiter et al. — [ORCAID: Oblique Rule-Based Continuous-Action Interpretation for Deep RL Policies](http://arxiv.org/abs/2607.07235v1)
  <details><summary>📄 Abstract</summary>
  Explainability remains a key issue in reinforcement learning (RL). Distilling an interpretable policy from an agent trained in a complex environment is particularly challenging when the action space is continuous. We introduce ORCAID, a novel method for extracting interpretable rule-based policies from RL agents operating in mixed continuous-discrete environments with continuous action spaces. Our main contribution is an efficient oblique decision tree training algorithm that partitions the stat...
  </details>

- **2026-07-08** — Guoruizhe Sun, Yueqiao Chen, Emily Guo et al. — [ShapeTalk: Combining Natural Language and Sketch for Time-Series Pattern Querying](http://arxiv.org/abs/2607.07073v1)
  <details><summary>📄 Abstract</summary>
  Searching for time-series segments that match user-defined patterns is important in domains such as finance, climate science, and healthcare. However, existing visual query tools often struggle to support vague, composite, or fuzzy pattern descriptions, often requiring users to express their intent through precise sketches or rigid structured filters. We present ShapeTalk, a coordinated natural-language and sketch-based querying system for univariate time-series pattern search. Rather than treat...
  </details>

- **2026-07-08** — Zitong Andrew Chen, Junaid Hasan, Akhil Srinivasan et al. — [Multiplication Beyond Groups: Stratified Fourier Mechanisms in Transformer Circuits](http://arxiv.org/abs/2607.07066v1)
  <details><summary>📄 Abstract</summary>
  Transformers have demonstrated a remarkable ability to learn algorithmic reasoning, yet mechanistic analyses have mostly focused on globally invertible operations such as cyclic addition and group composition. In this work, we investigate how small transformers learn modular integer multiplication over composite moduli, a fundamentally non-invertible operation due to the presence of zero-divisors. We propose the monoid extension: a localized generalization of Group Composition via Representation...
  </details>

- **2026-07-08** — Yujin Bae, Jaewoo Jeong, Hyeonseong Kim et al. — [Ego-Human Motion Prediction with 3D-Aware LLM](http://arxiv.org/abs/2607.07001v1)
  <details><summary>📄 Abstract</summary>
  Anticipating human motion from an egocentric perspective is fundamental for proactive assistance in AR/VR, human-robot collaboration, and embodied AI. While recent works incorporate language as a semantic prior to reduce the ill-posed nature of egocentric forecasting, they largely neglect the 3D spatial and semantic context that governs how motion unfolds, and treat pose and language prediction as separate inference streams. We introduce Ego3DLM, built on two core principles: accurate motion for...
  </details>

- **2026-07-08** — Wachiravit Modecrua, Krittin Pachtrachai, Touchapon Kraisingkorn — [Large Behavior Model: A Promptable Digital Twin of the Retail Customer](http://arxiv.org/abs/2607.06993v1)
  <details><summary>📄 Abstract</summary>
  Customer behavior modeling underpins recommendation, marketing, and decision support, yet existing approaches either optimize predictive accuracy without explaining decisions or simulate users without grounding them in real behavioral data. We present the Large Behavioral Model (LBM) that learns customer decision making directly from large-scale retail transactions through a unified Person-Environment formulation. Customer state is represented by a behavioral profile derived from historical purc...
  </details>

- **2026-07-07** — Zeyuan Ding, Wenhai Liu, Yang Xu et al. — [Pelican-VLA 0.5: Attending Before Acting Benefits Generalization](http://arxiv.org/abs/2607.06655v2)
  <details><summary>📄 Abstract</summary>
  In this report, we present Pelican-VLA 0.5, a unified VLA model that integrates vision-language understanding, future-frame generation, and action prediction within a single architecture. Pelican-VLA 0.5 achieves attention-level generalization: without object annotations, segmentation masks, attention supervision, or task-specific fine-tuning, its action pathway already focuses on the manipulation-relevant object and contact region. This behavior persists across unseen scenes and unseen robot em...
  </details>

- **2026-07-07** — Truong Xuan Khanh — [At-Grok Is Not Converged:A Measurement-Validity Audit for Grokking Representation Metrics](http://arxiv.org/abs/2607.06639v1)
  <details><summary>📄 Abstract</summary>
  On modular arithmetic, a network's embedding keeps compressing for tens of thousands of steps after it has already generalized. Reading effective rank at the grokking transition overstates the converged value by 3-5x on an MLP, and by 1.3-1.5x on a transformer trained to convergence; on the MLP it also erases which cells compress at all. Compression lags the accuracy transition by an amount on the order of the time-to-grok, at least 10,000 steps, rather than coinciding with it. A one-variable ab...
  </details>

- **2026-07-07** — Siyuan Mei, Yan Xia, Yipeng Sun et al. — [WING: A Window-Prior-Based Generative Network with Gated Inception for Cross-Modality CT Synthesis](http://arxiv.org/abs/2607.06234v1)
  <details><summary>📄 Abstract</summary>
  Generating CT volumes from MRI and CBCT can improve treatment planning in adaptive radiotherapy while avoiding additional radiation exposure. However, direct regression of CT intensities is challenged by the inherently high dynamic range and long-tailed distributions, thereby averaging out sparse yet clinically important structures. To alleviate this issue, we reformulate the regression target into multiple windowed representations, leveraging the inductive prior that CT intensities are structur...
  </details>

- **2026-07-07** — Igor Santos-Grueiro — [Context-to-Execution Integrity for LLM Agents](http://arxiv.org/abs/2607.06000v1)
  <details><summary>📄 Abstract</summary>
  Language-model agents read attacker-writable context to solve tasks. Tool execution needs a separate authority check for protected sink fields, sink-interpreted payloads, and the invocation event. Context-to-Execution Integrity (CXI) is an execution-boundary system for this setting. Policies mark protected sink fields, typed releases carry narrow validated values from writable context to specific destinations, opaque data slots keep evidence as data, and a deterministic gate admits a call only a...
  </details>

- **2026-07-07** — Rakesh Podder, Wadia Ganim, Sarath Sreedharan et al. — [i-EXAM: Instructable and Explainable Attack Connectivity Graph Modeler](http://arxiv.org/abs/2607.05888v1)
  <details><summary>📄 Abstract</summary>
  i-EXAM is a planning-powered tool that helps system administrators to create security profiles of complex networks and perform what-if analyses to identify network hardening strategies. It leverages planning compilation that provides soundness and completeness guarantees to identify attack paths, evaluate security metrics, generate diverse hardening strategies, and explain these strategies in natural language using Large Language Models.
  </details>

- **2026-07-07** — Huan Wu, Ali Emami, Muhammad Furquan Hassan et al. — [LLMs Silently Correct African American English: Auditing and Mitigating Dialect Bias via Activation Steering](http://arxiv.org/abs/2607.06845v1)
  <details><summary>📄 Abstract</summary>
  African American English (AAE), a rule-governed dialect spoken by over 30 million people, is routinely misinterpreted and "corrected" by large language models (LLMs). Across six instruction-tuned LLMs (14B to 70B), we show that state-of-the-art models systematically prefer Standard American English (SAE) continuations even when the preceding context is in AAE, effectively rewriting AAE into SAE. We present an end-to-end framework to audit and mitigate this bias. For auditing, we introduce condit...
  </details>

- **2026-07-07** — Jiarui Xie, Lingchen Kong, Mohamed Rami Latreche et al. — [Machine Learning-Based Battery State-of-health Prediction for Unmanned Aerial Vehicles Predictive Maintenance](http://arxiv.org/abs/2607.06791v1)
  <details><summary>📄 Abstract</summary>
  Battery state-of-health (SoH) prediction aims to estimate the remaining capacity by modeling battery degradation through its life cycle. Machine learning (ML)-based SoH models can accurately predict the battery remaining capacity based on voltage, current, and temperature. Battery SoH prediction for unmanned aerial vehicles (UAVs) is a crucial yet overlooked domain with data scarcity and high variability. Accurate battery SoH information contributes to efficient predictive maintenance, enhancing...
  </details>

- **2026-07-07** — Alexey Gavryushin, Dingxi Zhang, Zhao Huang et al. — [CoMind: Understanding Collaborative Human Activity from Multiple Minds and Views](http://arxiv.org/abs/2607.06691v1)
  <details><summary>📄 Abstract</summary>
  Human-human collaboration is a fundamental aspect of everyday life, essential to success in a wide range of goal-directed activities from household tasks to professional teamwork. While much research has focused on modeling coordination and task execution, the cognitive processes that support such collaboration, particularly Theory of Mind (the ability to infer the mental states of others), remain difficult to study in natural settings. To address this gap, we introduce a novel egocentric and ex...
  </details>

- **2026-07-07** — Ziye Wang, Modi Shi, Chaojun Ni et al. — [NativeMEM: Native Memory Compression for Long-Horizon Robotic Manipulation](http://arxiv.org/abs/2607.06678v1)
  <details><summary>📄 Abstract</summary>
  How can pretrained Vision-Language-Action (VLA) models retain long-horizon visual histories with high-frequency updates without sacrificing efficiency? Existing approaches rely on external memory management, which restrains either the memory horizon or the reactiveness of pretrained policies. To this end, we present NativeMEM, a VLA policy that features long-term and real-time updated memory. At its core is an efficient memory encoding scheme, Native Memory Compression, which repurposes the VLA'...
  </details>

- **2026-07-07** — He Liang, Chenyang Ma, Yiming Zhang et al. — [CAIRN: Cross-Room 3D Scene Understanding with Topology-Aware Large Multimodal Models](http://arxiv.org/abs/2607.06534v1)
  <details><summary>📄 Abstract</summary>
  Existing 3D scene-grounded Large Language Models (3D-LLMs) focus on answering questions grounded in simplified single-room 3D scenes, lacking the ability to reason over real-world household environments containing multiple interconnected rooms and diverse object categories. We introduce CAIRN, a topology-aware 3D-LLM for multi-room 3D scene understanding. CAIRN aligns transformer attention with scene hierarchy, giving the model explicit awareness of object-level relations and room-level connecti...
  </details>

- **2026-07-07** — Linlin Zhang, Neema Jakisa Owor, Xiang Yu et al. — [A VLM-Enhanced Framework for Comprehensive Traffic Sign Condition Assessment Integrating Daytime Visual Performance and Nighttime Retroreflectivity Evaluation](http://arxiv.org/abs/2607.06478v1)
  <details><summary>📄 Abstract</summary>
  Traffic signs are crucial components of road safety, serving as visual tools under all lighting conditions. The Manual on Uniform Traffic Control Devices (MUTCD) specifies daytime visual factors such as legibility and color contrast, and nighttime retroreflectivity requirements. Traditional assessment methods rely on manual inspections, which the Federal Highway Administration (FHWA) notes are subjective, labor-intensive and pose safety concerns, while retroreflectometers are expensive and unaff...
  </details>

- **2026-07-07** — Yuhang Wu, Shuxiang Zhang, Wee Hian Ching et al. — [PIPBench: A Profile-Inclusive Framework for Personalized Image Generation Evaluation](http://arxiv.org/abs/2607.06440v1)
  <details><summary>📄 Abstract</summary>
  Recent text-to-image models such as DALLE-3 excel at following diverse prompts yet remain blind to individual aesthetic preferences. We study personalized image generation, where models must align outputs with a user's implicit visual preferences based on a few historically preferred images and a short prompt. To this end, we introduce PIPBench, the first profile-inclusive benchmark for evaluating personalized image generation. We further propose a novel data construction pipeline that leverages...
  </details>

- **2026-07-07** — Hao He, Xueying Liu, Chris J. Kuhlman et al. — [An Experimental Design Approach to Evaluating Agentic AI's Autonomous Model Discovery](http://arxiv.org/abs/2607.06413v1)
  <details><summary>📄 Abstract</summary>
  Large language model coding agents increasingly perform open-ended data modeling and analysis. These agents are stochastic and adaptive, and therefore their autonomous model discovery behavior cannot be adequately characterized by a single benchmark run. In this work, we propose an experimental design and analysis framework for systematically evaluating this discovery process, quantifying its variability, and identifying important factors. The proposed framework treats these agents as stochastic...
  </details>

- **2026-07-07** — Eleftherios Tsonis, Xi Wang, Vicky Kalogeiton — [What Images Cannot Say: Language-Guided Olfactory Representation Learning](http://arxiv.org/abs/2607.06402v1)
  <details><summary>📄 Abstract</summary>
  Images tell us what a scene looks like, but rarely what it would feel like to be there. While recent datasets pair visual scenes with electronic-nose measurements, aligning smell signals with images remains challenging because many olfactory cues arise from contextual environmental factors that are not directly visible in pixels. We introduce SCENT, a multimodal framework that uses language guidance as a semantic bridge between vision and olfaction. Our approach leverages Vision-Language Models ...
  </details>

- **2026-07-07** — John Bianchi, Luca Petrillo, Fabio Martinelli et al. — [Automated Compliance Mapping in Cloud Security with Domain-Adapted Sentence Transformers](http://arxiv.org/abs/2607.06364v1)
  <details><summary>📄 Abstract</summary>
  Mapping cloud security controls to technical metrics is currently a manual process. This paper proposes domain adaptation of Sentence Transformer models to automate it. We build a training corpus of 3,499 semantic pairs from five European security standards and a set of technical metrics, then expand it via back-translation and LLM-based paraphrasing to up to 13,996 samples across four scenarios. We fine-tune five architectures and evaluate their performance on two independent tasks: control-to-...
  </details>

- **2026-07-07** — Xiachong Lin, Du Yin, Arian Prabowo et al. — [TopoBrick: Agentic Topology Sampling of Exogenous Variables for Zero-Shot Building IoT Forecasting](http://arxiv.org/abs/2607.06349v1)
  <details><summary>📄 Abstract</summary>
  Building sensors are embedded in physical topology, spatial hierarchy, and operational context, yet existing forecasters often treat them as isolated time series or rely on fixed covariate sets. We present TopoBrick, a training-free framework for zero-shot building IoT (Internet-of-Things) forecasting. TopoBrick uses building knowledge graphs to construct a compact structural skeleton and employs an agentic topology sampler to select target-specific exogenous variables. The selected variables ar...
  </details>

- **2026-07-07** — Amin Haeri, Mahdi Ghelichi — [Specification Grounding Drives Test Effectiveness for LLM Code](http://arxiv.org/abs/2607.06636v1)
  <details><summary>📄 Abstract</summary>
  Large language models frequently generate code that appears correct on typical inputs yet fails on edge cases, invalid inputs, and other specification-defined corner conditions. A popular fix has the model write its own tests and repair until they pass, but the source of the gain is unclear: does it come from the tests merely existing, or from their grounding in a specification of what the code should do? We isolate this factor. Holding the tester, test budget, and repair loop fixed, we change a...
  </details>

- **2026-07-07** — Grace Man Chen, Litao Guo, Yifan Wu et al. — [UI2App: Benchmarking Visual Interaction Inference in Executable Web Application Generation](http://arxiv.org/abs/2607.06306v1)
  <details><summary>📄 Abstract</summary>
  Large language models (LLMs) have demonstrated growing competence in web page generation. However, existing text-driven approaches rely on complex prompts that impose substantial demands on users and offer limited expressivity for page layout and cross-page visual coherence. Image-driven paradigms, which take UI screenshots as input, align more closely with real development workflows. However, current benchmarks focus primarily on visual fidelity and lack a systematic evaluation of the interacti...
  </details>

- **2026-07-07** — Benjamin Marsh, Alejandro Ranchal-Pedrosa — [Slack and Budget Breaking in Threshold Team Production](http://arxiv.org/abs/2607.06197v1)
  <details><summary>📄 Abstract</summary>
  A threshold system completes a public task only after $κ$ verifiable shares are publicly committed. If the honest schedule creates \(   \Nstar=κ+Δ\) share opportunities by deadline $t^\star$, then $Δ$ shares are slack such that a coalition delays completion if and only if it withholds at least $Δ+1$ shares. The incentive problem is therefore to price the cheapest sabotage set. Agents receive a direct fee $f$ per committed share. A delaying coalition may also obtain delay value at most $L$, and m...
  </details>

- **2026-07-07** — Chenxu Wang, Yongkun Yang, Boyuan Du et al. — [LLM Agents for Deliberative Collaboration: A Study on Joint Decision Making Under Partial Observability](http://arxiv.org/abs/2607.06157v1)
  <details><summary>📄 Abstract</summary>
  Deliberation plays a crucial role in collaboration; when humans work together, they naturally engage in communication to align information and reach an agreement. In this paper, we investigate deliberative large language model (LLM) agents under partially observable joint decision-making tasks. We formalize deliberative collaboration as a cooperative joint decision problem with partial and asymmetric observations, and introduce a scalable benchmark that instantiates this problem across multiple ...
  </details>

- **2026-07-07** — Adrian Cosma — [Prompting Complexity: Shortest Prompts for Texts and Behaviors in LLMs](http://arxiv.org/abs/2607.06145v1)
  <details><summary>📄 Abstract</summary>
  In this paper, we define the quantity of prompting complexity: for a fixed instruction-tuned language model, what is the shortest plausible prompt that makes deterministic decoding produce a target text? It is an LM-relative analogue of resource-bounded Kolmogorov complexity: the prompt is a program, the model interface is the interpreter, and information omitted from the prompt is supplied by the model's weights, training distribution, tokenizer, template, and decoding rule. Unlike classical Ko...
  </details>

- **2026-07-07** — Hanan Gani, Tejal Kulkarni, Madhoolika Chodavarapu et al. — [RoboTALES: Learning Reasoning-Guided Robot Policies via Task-Aligned Simulated Futures](http://arxiv.org/abs/2607.06018v1)
  <details><summary>📄 Abstract</summary>
  Pretrained video generative models are promising backbones for visuomotor control, but their imagined futures often drift from task intent and are not reliably action-conditional. As a result, these models can be difficult to use for planning or policy extraction. To address these limitations, we propose RoboTALES, a single-stage framework that learns task-aligned simulated futures and uses them to train robot policies. Our approach introduces two key innovations: (1) a hierarchical LLM-based pl...
  </details>

- **2026-07-07** — Tomáš Sourada, Katia Vendrame, Jan Hajič — [Music I Care About: Automated Multimodal Benchmarking of LLM Music Perception Skills on (Almost) Any Music](http://arxiv.org/abs/2607.06015v1)
  <details><summary>📄 Abstract</summary>
  Music represents a cornerstone of human culture, existing digitally across diverse modalities, including audio, symbolic encodings (e.g., MIDI, MusicXML), and sheet music. Despite the advancement of Multimodal Large Language Models (MLLMs), current music benchmarks face three major limitations. First, large static benchmarks are resource-intensive to evaluate, and it remains unclear how their results transfer to diverse kinds of music beyond those included in the benchmark. Second, benchmarks cl...
  </details>

- **2026-07-07** — Yuhang Zhou, Kai Zheng, Haoling Li et al. — [TurnOPD: Making On-Policy Distillation Turn-Aware for Efficient Long-Horizon Agent Training](http://arxiv.org/abs/2607.05804v1)
  <details><summary>📄 Abstract</summary>
  On-policy distillation (OPD) trains a student policy by matching a stronger teacher on the student's own trajectories, offering a promising framework for language agent training. However, its application to long-horizon agentic tasks remains insufficiently explored. We identify two key inefficiencies in vanilla agent OPD: (1) full-horizon rollouts often waste wall-clock resources on tail turns that provide weak and noisy KL supervision, and (2) trajectory-level KL objectives concentrate most of ...
  </details>

- **2026-07-07** — Yake Wei, Yuan Wang, Fengyun Rao et al. — [Segmentation before Answering: Pixel Grounding for MLLM Visual Reasoning](http://arxiv.org/abs/2607.05798v1)
  <details><summary>📄 Abstract</summary>
  Recent advancements in Multimodal Large Language Models (MLLMs) have evolved from static perception to interleaved visual-language reasoning, often referred to as ``thinking with images''. A basic operation in this reasoning process is to zoom in on regions of interest (often represented with bounding boxes) to acquire finer visual details. In this paper, we propose \textbf{Seg}mentation before \textbf{Answer}ing (SegAnswer), which shifts the unit of zoom-in from the popular bounding box to pixe...
  </details>

- **2026-07-07** — Yan Chen, Weijing Tang, Jin-Hong Du — [AI-Augmented Statistical Network Estimation with Proxy Gene Embeddings](http://arxiv.org/abs/2607.05774v1)
  <details><summary>📄 Abstract</summary>
  Gene--gene networks are often observed only on a restricted target set, while modern biomedical foundation models provide proxy gene embeddings over substantially larger gene universes. To leverage externally learned representations to improve latent-structure recovery in partially observed target networks, we propose \emph{Proxy-Latent Assisted Network Estimation} (PLANE), an adaptively weighted joint network--embedding latent variable model. PLANE combines the two sources of information throug...
  </details>

- **2026-07-07** — Yimeng Zhang, Yingying Zhuang, Ziyi Wang et al. — [SpanUQ: Span-Level Uncertainty Quantification for Large Language Model Generation](http://arxiv.org/abs/2607.05721v1)
  <details><summary>📄 Abstract</summary>
  Uncertainty estimation is essential not only for the trustworthy deployment of large language models (LLMs) but also as a foundation for self-refinement in LLM generation. However, existing approaches operate at suboptimal granularities: token-level scores lack semantic coherence, while sequence-level scores fail to localize errors. We formalize Span-Level Uncertainty Estimation (SLUE), a new task that targets the natural granularity for uncertainty: semantically coherent text spans, each convey...
  </details>

- **2026-07-07** — Zhiwei Yang, Yuanchen Wu, Nan Zhang et al. — [Scene Graph Thinking: Reinforcing Structured Visual Reasoning for Multimodal Large Language Models](http://arxiv.org/abs/2607.05716v1)
  <details><summary>📄 Abstract</summary>
  Multimodal Large Language Models (MLLMs) have demonstrated strong perception and reasoning capabilities. However, most existing models focus on isolated objects and neglect structured relationships for efficient target navigation, limiting their performance on visually intensive tasks. To address this challenge, we introduce Scene Graph Thinking (SaGe), a novel paradigm that enables fine-grained and structured visual reasoning through explicit scene-graph representations. Specifically, we first ...
  </details>

- **2026-07-07** — Bowen Xue, Zihan Min, Xingyang Li et al. — [FourTune: Towards Fully 4-Bit Efficient Post-Training for Diffusion Models](http://arxiv.org/abs/2607.05711v1)
  <details><summary>📄 Abstract</summary>
  Diffusion models have become a dominant paradigm for high-quality generative modeling, while post-training is essential for adapting them to diverse downstream applications. However, post-training of large diffusion models is still challenging due to the prohibitive memory footprints and slow training speed, which existing parameter-efficient fine-tuning methods only partially address. To overcome these limitations, we propose FourTune, an efficient post-training framework for diffusion models b...
  </details>

- **2026-07-07** — Inkyu Sa, Chanoh Park, Hea-Min Lee et al. — [Vision Language Action (VLA) Models for Unmanned Aerial Robotics and Bimanual Manipulation: A Review](http://arxiv.org/abs/2607.06706v1)
  <details><summary>📄 Abstract</summary>
  Vision Language Action (VLA) models unify visual perception, natural-language understanding, and action generation within a single foundation model, allowing a robot to follow instructions such as fold the towel or fly to the red building directly from camera images. Because VLAs inherit world knowledge from internet-scale pre-training, they have become the dominant framework for learning-based manipulation, with bimanual coordination serving as the most demanding testbed: two arms with 7 degree...
  </details>

- **2026-07-07** — Mike Roberts, Renhan Wang, Rushikesh Zawar et al. — [SPEAR: A Simulator for Photorealistic Embodied AI Research](http://arxiv.org/abs/2607.06701v1)
  <details><summary>📄 Abstract</summary>
  Interactive simulators have become powerful tools for training embodied agents and generating synthetic visual data, but existing photorealistic simulators suffer from limited generality, programmability, and rendering speed. We address these limitations by introducing SPEAR: A Simulator for Photorealistic Embodied AI Research. At its core, SPEAR is a Python library that can connect to, and programmatically control, any Unreal Engine (UE) application via a modular plugin architecture. SPEAR expo...
  </details>

- **2026-07-07** — Zeyuan Ding, Wenhai Liu, Yang Xu et al. — [Pelican-VLA 0.5: Attending Before Acting Benefits Generalization](http://arxiv.org/abs/2607.06655v1)
  <details><summary>📄 Abstract</summary>
  In this report, we present Pelican-VLA 0.5, a unified VLA model that integrates vision-language understanding, future-frame generation, and action prediction within a single architecture. Pelican-VLA 0.5 achieves attention-level generalization: without object annotations, segmentation masks, attention supervision, or task-specific fine-tuning, its action pathway already focuses on the instruction-relevant object and contact region. This behavior persists across unseen scenes and unseen robot emb...
  </details>

- **2026-07-07** — Zhuofan Zhang, Tianxu Wang, Guoxi Zhang et al. — [UniLM-Nav: A Unified Framework for Zero-Shot Last-Mile Navigation](http://arxiv.org/abs/2607.06537v1)
  <details><summary>📄 Abstract</summary>
  Mobile manipulation requires a robot to navigate to a target object or receptacle and then perform intended manipulation. However, reaching the vicinity of the target does not guarantee a manipulation-ready base pose, a problem known as last-mile navigation. Prior methods for last-mile navigation either rely on manual pose annotation or task-specific training, limiting their scalability to open-vocabulary settings with fine-grained spatial constraints. We propose UniLM-Nav, a unified framework f...
  </details>

- **2026-07-07** — Wei Wu, Fangjing Wang, Fan Lu et al. — [From Foundation to Application: Improving VLA Models in Practice](http://arxiv.org/abs/2607.06403v1)
  <details><summary>📄 Abstract</summary>
  Despite recent progress of VLA foundation models, the disparity between laboratory conditions and real-world applications continues to impede their practical implementation. To bridge this gap, we present LingBot-VLA 2.0, which advances LingBot-VLA through improvements in three functional domains. (1) Generalization across tasks and embodiments. Compared to the previous version, we revamp the data processing pipeline and curate around 60,000 hours of data for pretraining, including 50,000 hours ...
  </details>

- **2026-07-07** — Shuangxiang Kan, Shuanglong Kan, Sebastian Ertel — [Harnessing Code Agents for Automatic Software Verification](http://arxiv.org/abs/2607.06341v1)
  <details><summary>📄 Abstract</summary>
  Formal verification offers the strongest guarantee of software correctness, but it does not scale: the proofs demanded by interactive theorem provers such as Coq require enormous expert effort. Large language models (LLMs) promise to generate these proofs automatically, yet existing approaches wire a fixed, human-designed proof strategy into the system and constrain the model to follow it (retrieving premises and predicting tactics one step at a time, or splitting goals by divide-and-conquer), a...
  </details>

- **2026-07-07** — Yan Pan, Yuanchuan Ren, Chipui Chan et al. — [Calf-Integrated Arms for Bimanual Quadruped Loco-Manipulation](http://arxiv.org/abs/2607.06186v1)
  <details><summary>📄 Abstract</summary>
  Most quadruped loco-manipulation designs trade manipulation capability against stance. A trunk-mounted arm sits high and usually carries a single arm; using the legs as manipulators lifts the manipulating leg off the ground; and even leg-mounted grippers reach two-handed tasks only by rearing onto the hind legs. This paper integrates a manipulator with a prismatic slider, two revolute joints, and a gripper into each front calf of a Unitree Go2. The two arms grasp objects at ground level and mani...
  </details>

- **2026-07-07** — Youcheng Zong, Runda Jia, Dakuo He — [LLM-Guided Measurement Credibility Correction for Trustworthy Industrial Process Inference](http://arxiv.org/abs/2607.06111v1)
  <details><summary>📄 Abstract</summary>
  Industrial prediction and soft sensing depend on credible input measurements. In field deployment, a predictor may receive biased, delayed, stale, or derived measurements that still look plausible. Prediction can then fail before the forecasting backbone becomes the main limitation, because the input window no longer represents the real process. Sensor reconstruction, data reconciliation, and fault-tolerant soft sensing reduce this risk, but they often rely on numerical correlation, alarms, faul...
  </details>

- **2026-07-07** — Shenbo Xie, Mingrui Cai, Xu Yang et al. — [SparseCtrl-HOI: Sparse Temporal Control for Human-Object Interaction Video Generation](http://arxiv.org/abs/2607.05994v1)
  <details><summary>📄 Abstract</summary>
  Human-Object Interaction (HOI) video generation aims to synthesize realistic videos of humans manipulating diverse objects, serving as a promising avenue for AI-driven live streaming e-commerce. A primary obstacle in this domain lies in the complexity of modeling fine-grained physical dynamics and the intricate spatial-temporal coordination between human hands and objects. Existing approaches to this problem typically rely on dense temporal guidance, e.g., frame-wise hand-object pose sequences, ...
  </details>

- **2026-07-07** — Lorenzo di Filippo, Enkeleda Bardhi, Andrea Agiollo et al. — [Beyond the Syntax: Do Security Experts Trust LLMs for NIDS Rule Engineering?](http://arxiv.org/abs/2607.05916v1)
  <details><summary>📄 Abstract</summary>
  As network threats evolve, manual NIDS rule engineering has become a critical operational bottleneck. While Large Language Models (LLMs) show promise for automating this process, their ability to produce production-ready rules remains unvalidated. This paper presents a human-centered investigation into LLM-based NIDS rule engineering, formalizing a grounded generation framework and evaluating it through a user study with 10 domain experts. Our evaluation reveals a syntax-semantics paradox: altho...
  </details>

- **2026-07-07** — Petar Djukic, Sudipta Acharya, Takai Eddine Kennouche et al. — [From Agentic to Autogenic Network Management for AI-Native 6G and Beyond: A Standards Perspective](http://arxiv.org/abs/2607.06786v1)
  <details><summary>📄 Abstract</summary>
  Standards bodies, including TM Forum, 3GPP, and ETSI, are converging on Agentic AI as the foundation for next-generation network management, where Large AI Model (LAM)-based agents autonomously interpret intent, coordinate resources, and adapt operational behaviors at runtime. However, achieving this vision at the scale and complexity of 6G networks requires management systems that can generate and evolve their own automation software during operation. We introduce Autogenic network management, ...
  </details>

- **2026-07-07** — Yoav Baron, Sara Dorfman, Roni Paiss et al. — [Analysis-by-Proxy: Localization Signals in VLMs Operating as Condition Encoders](http://arxiv.org/abs/2607.06445v1)
  <details><summary>📄 Abstract</summary>
  Vision-Language Models (VLMs) are increasingly utilized as the conditioning backbone for diffusion-based image editing due to their remarkable multimodal reasoning capabilities. While standalone VLMs demonstrate strong localization capabilities, editing pipelines frequently struggle to maintain this accuracy, particularly in complex, multi-entity scenes. In this work, we investigate this performance gap, hypothesizing that it stems from treating the VLM as a condition encoder. In this role, the ...
  </details>

- **2026-07-07** — Yufan Wang, Anit Kumar Sahu, Yan Fei Ng et al. — [Finding H. pylori in the Fine Print: Evidence-Linked Multi-Agent Case Finding from Gastric Biopsy Reports](http://arxiv.org/abs/2607.06435v1)
  <details><summary>📄 Abstract</summary>
  Data from Singapore indicated that about 31% of the population had evidence of Helicobacter pylori infection. Persistent H. pylori infection is associated with chronic active gastritis and peptic ulcer disease, and its eradication is key to gastric cancer prevention. However, evidence supporting \textit{H. pylori} positivity and H. pylori-associated gastritis may be distributed across heterogeneous coded and free-text report fields and may require contextual interpretation of assertion and negat...
  </details>

- **2026-07-07** — J. Pedra — [Understanding Small-Signal Impedance Matrices in Different Reference Frames](http://arxiv.org/abs/2607.06416v1)
  <details><summary>📄 Abstract</summary>
  This paper systematically analyzes the relationships among the $dq$-domain, $αβ$-domain, and sequence-domain representations used in small-signal impedance modeling of voltage-source converters (VSCs). It is shown that the AC impedance matrix expressed with $dq$-complex and $αβ$-complex variables leads to different formulations in the sequence domain. The study demonstrates that asymmetric systems exhibit different physical phenomena in the rotating and stationary reference frames; therefore, th...
  </details>

- **2026-07-07** — Felix Feldman, Joshua Harris, Timothy Laurence et al. — [Healthier LLMs: Retrieval-Augmented Generation for Public Health Question Answering](http://arxiv.org/abs/2607.06641v1)
  <details><summary>📄 Abstract</summary>
  Large language models (LLMs) achieve promising results on medical question answering benchmarks, yet their use in public health is constrained by hallucinations and the rapid evolution of official guidance. Retrieval-Augmented Generation (RAG) mitigates these risks by grounding responses in an explicitly maintained corpus, but end-to-end performance depends critically on retrieval configuration and on evaluation beyond multiple-choice formats. We extend PubHealthBench, a question answering (QA) ...
  </details>

- **2026-07-07** — Sonali Brahma, Trishna Kalita, Himangshu Prabal Goswami — [Coherence Estimation Beyond the Liouvillian Gap in a Finite Nonequilibrium System](http://arxiv.org/abs/2607.06215v1)
  <details><summary>📄 Abstract</summary>
  We investigate the estimation of bath-induced coherence in a finite quantum system interacting with thermal reservoirs. Enhancement of coherence estimation is transient and the estimation precision totally disappears at the steady state despite the system retaining finite coherence. By analyzing the full Liouvillian eigenspectrum, we demonstrate that the optimal sensing window emerges from the competition between identifiable contributory modes' temporal relaxation and statistical importance. Ne...
  </details>

- **2026-07-07** — Youcheng Zong, Runda Jia, Ranmeng Lin et al. — [Open-Ended Scenario Reasoning for Specialist Model Adaptation](http://arxiv.org/abs/2607.06625v1)
  <details><summary>📄 Abstract</summary>
  Process industries have accumulated validated specialist models, yet sensor drift, feedstock variation, and regime switching cause these models to degrade systematically in new scenarios. Collecting new labeled data and retraining is costly, while continuing with the original model incurs persistent bias. Existing adaptation methods require modifying model parameters with sufficient labeled data, making rapid response on deployed systems difficult. Using LLMs as direct predictors risks hallucina...
  </details>

- **2026-07-07** — Huzaifa Ejaz, Fabian C. Peña, Steffen Herbold — [Large Language Models Have Unreliable Understanding of Software Engineering Terminology](http://arxiv.org/abs/2607.06004v1)
  <details><summary>📄 Abstract</summary>
  Large Language Models (LLMs) are increasingly used in software engineering (SE), yet there is no systematic study that determines to which degree these LLMs actually understand standardized SE terminology. Lack of such understanding can lead to miscommunication and misunderstanding, both by LLMs consuming text but also by human-developers acting on LLM-generated text. Within this paper, we investigate to which degree state-of-the-art LLMs are able to identify whether definitions from the ISO/IEC...
  </details>

- **2026-07-07** — Fabian C. Peña, Steffen Herbold — [Pre-Training on Software Engineering Texts: Effects on Domain Adaptation and General-Language Understanding](http://arxiv.org/abs/2607.06613v1)
  <details><summary>📄 Abstract</summary>
  Generalist and code-focused Language Models (LMs) are increasingly applied to software engineering (SE), yet whether they are optimized for understanding SE textual artifacts (e.g., issues, commit messages, developer discussions) remains unclear, as most evidence comes from code-focused benchmarks. We study how to adapt encoder and decoder LMs to SE text, comparing continual pre-training (CPT) against pre-training from scratch (PTS) on a new SE corpus, and evaluating both domain adaptation (SELU...
  </details>

- **2026-07-07** — Krittanon Kaewtawee, Petmongkon Pornpichitsuwan, Natchaya Temyingyong et al. — [InfluMatch: Frontier-Quality KOL Search at 4B-Model Cost](http://arxiv.org/abs/2607.05968v1)
  <details><summary>📄 Abstract</summary>
  Matching influencers (KOLs) to free-form, multi-part Thai marketing criteria is today served either by keyword search over structured profiles, which misses semantic fit, or by prompting frontier LLMs over every candidate, which is accurate but slow and expensive. We present InfluMatch, a low-cost three-stage cascade -- retrieval $\rightarrow$ rerank $\rightarrow$ reason -- built entirely from small open-weight models: dense retrieval returns 50 candidates, a 4B pointwise reranker scores each by...
  </details>

- **2026-07-07** — Yakun Liu, Zhiyu Jin, Hai Luan et al. — [From Textural Counterpoint to Feature Encoding: A Multi-Dimensional Machine Representation Study of Haydn's "The Lark" Integrating Electroacoustic Analysis](http://arxiv.org/abs/2607.05902v1)
  <details><summary>📄 Abstract</summary>
  Chamber music, as a highly precise multi-part interactive system, contains a logic of "role assignment and dynamic interaction" that provides an extremely valuable blueprint for exploring human-computer collaborative composition paradigms. Addressing the lack of role perception capabilities in existing deep music generation models during polyphonic interactions, this paper conducts an interdisciplinary analysis of Haydn's String Quartet in D Major, The Lark (Op. 64, No. 5). We propose a novel re...
  </details>

- **2026-07-07** — Andrei-George Durdun, Victor Constantinescu, Radu Tudor Ionescu — [Audio Sentiment Analysis via Distillation and Cross-Modal Integration of Generated Multilingual Transcripts](http://arxiv.org/abs/2607.06611v1)
  <details><summary>📄 Abstract</summary>
  Automatically recognizing the sentiment, positive or negative, from speech is a challenging task, requiring both the analysis of vocal inflections and the interpretation of uttered words. Recent solutions rely on audio foundation models to solve the task, but it remains unclear if such models can take all aspects into account. To this end, we propose a multimodal solution that integrates audio and text information via cross-modal transformers, where text transcripts are automatically generated v...
  </details>

- **2026-07-07** — Guang Yang, Brian Siyuan Zheng, Victoria Ebert et al. — [LEGATO 2: Toward Multimodal Sheet Music Recognition and Understanding](http://arxiv.org/abs/2607.05769v1)
  <details><summary>📄 Abstract</summary>
  We propose a novel pipeline, Legato 2, for extracting symbolic notation and semantic knowledge from images of sheet music. Legato 2 features the first large-scale neural model for optical music recognition (OMR) to operate sequentially on a system-by-system basis, following the horizontal lines of notation as they are read on the page, rather than treating the page as an undifferentiated image, enabling better scaling to arbitrarily long inputs. It is also the first OMR model capable of generati...
  </details>

- **2026-07-07** — Zihan Wang, Seungjun Lee, Yinghao Xu et al. — [Image2Sim: Scaling Embodied Navigation via Generative Neural Simulator](http://arxiv.org/abs/2607.05765v1)
  <details><summary>📄 Abstract</summary>
  Embodied navigation aims to build agents that interpret multimodal goals, reason in 3D space, and reach target destinations reliably in the real world. However, progress remains constrained by the lack of scalable, high-fidelity, and physically grounded interactive environments. Although real-world scanned datasets offer visual realism, they are limited by scale. In contrast, synthetic simulators scale more easily but often exhibit large sim-to-real gaps. We introduce Image2Sim, a real-time neur...
  </details>

- **2026-07-07** — Mahmoud Hany, Mourad ElSheraey, Mahmoud Said et al. — [Inject or Navigate? Token-Efficient Retrieval for LLM Analysis of Transactional Legal Documents](http://arxiv.org/abs/2607.05764v1)
  <details><summary>📄 Abstract</summary>
  Answering questions over a set of transactional legal documents is most simply done by injecting the whole corpus into the LLM's context window on every query. That baseline maximises retrieval recall, but its token footprint scales with the corpus rather than the question, and long-context degradation scales with it. We report what it took to replace full-corpus injection in a legal-document analysis system, comparing it against two structured retrieval modes over our proprietary structure-awar...
  </details>

- **2026-07-06** — Sai Varun Kodathala — [aiAuthZ: Off-Host, Identity-Bound Authorization for AI Agents](http://arxiv.org/abs/2607.05518v1)
  <details><summary>📄 Abstract</summary>
  AI agents issue tool calls on the basis of text they cannot verify, so any party who controls part of the context can forge the appearance of authority. I evaluate 15 contemporary language models against eight attack scenarios derived from a published corpus of real agent incidents and find that refusal varies from 100% down to 38% across fully evaluated models; the most expensive model refused only half of the attacks despite a twentyfold price spread. I present aiAuthZ, an authorization gatewa...
  </details>

- **2026-07-06** — Mouhamed Amine Bouchiha, Gregory Blanc — [TACTIC-KG: Toward Small Agent Teams for Cyber Threat Intelligence Knowledge Graph Construction](http://arxiv.org/abs/2607.05001v2)
  <details><summary>📄 Abstract</summary>
  Cyber Threat Intelligence (CTI) reports are predominantly unstructured, heterogeneous, and noisy, which limits their direct usability for automated analysis and reasoning. Cybersecurity Knowledge Graphs (CSKGs) provide a structured representation of adversarial entities, actions, and relations, but constructing such graphs from free-text CTI remains a challenge. Recent approaches rely on monolithic Large Language Models (LLMs) to perform end-to-end extraction and completion, leading to high cost...
  </details>

- **2026-07-06** — Honglin Wang, Shiyao Pan, Yun-Fu Liu — [IMR: Iterative Mode-World Weighted Regression for Multi-Agent Trajectory Prediction](http://arxiv.org/abs/2607.05705v1)
  <details><summary>📄 Abstract</summary>
  Multi-agent motion prediction is essential for automated vehicles to understand the intentions of surrounding vehicles. However, previous prediction-based and anchor-based methods have limitations in mode diversity and prediction accuracy, respectively. These limitations may cause inadequate safety assessments and behavioral deviations in automated vehicles. To address this issue, a mode-world weighted regression loss is proposed to bridge the gap between these features. Specifically, this appro...
  </details>

- **2026-07-06** — Youssef Abdelsalam, Norman Peitek, Anna-Maria Maurer et al. — [A Mechanistic Lens on Semantic Conflicts: Using Activation Patching to Understand LLM Behavior](http://arxiv.org/abs/2607.05587v1)
  <details><summary>📄 Abstract</summary>
  Large language models (LLMs) are increasingly used in software-engineering tasks processing executable code and non-executable semantic cues such as comments or identifiers. These two sources can conflict when semantic cues suggest different program behavior than the code itself. It remains unclear how such semantic conflicts affect LLM behavior and which source dominates their outputs.   We present the first controlled, mechanistic study of LLM behavior under semantic conflicts. To this end, we...
  </details>

- **2026-07-06** — Hafsteinn Einarsson, Hafsteinn Birgir Einarsson, Jón Gunnar Ólafsson et al. — [Curated retrieval versus open web search in public AI information services: a coverage-trust trade-off](http://arxiv.org/abs/2607.05217v2)
  <details><summary>📄 Abstract</summary>
  Public institutions increasingly use large language models (LLMs) to answer citizens' questions, often pairing a curated knowledge base with live web search, yet whether the sources behind these answers can be trusted has received little empirical scrutiny. We report a pre-launch expert evaluation of Evrópuvefur, an independent, government-funded service run by the University of Iceland that answers questions about the European Union, conducted as Iceland prepared for its referendum of 29 August...
  </details>

- **2026-07-06** — Yuan Jiang, Ningyuan Zhang, Xicun Yang et al. — [Athena-WBC: Capability-Aligned Policy Experts for Long-Tail Humanoid Whole-Body Control](http://arxiv.org/abs/2607.04837v2)
  <details><summary>📄 Abstract</summary>
  Large-scale humanoid motion-tracking controllers are commonly improved by reallocating training effort: difficult motions are sampled more often, isolated into smaller subsets, or assigned to specialized experts. We show that this view is incomplete. In strong whole-body-control baselines, a residual set of feasible training clips remains unsolved even under targeted training, especially for high-dynamic transitions and balance-critical motions. These failures arise not only from insufficient ex...
  </details>

- **2026-07-06** — Hairui Zhu, Yiying Yang, Tengjin Weng et al. — [CanvasAgent: Enabling Complex Image Creation and Editing via Visual Tool Orchestration](http://arxiv.org/abs/2607.05465v1)
  <details><summary>📄 Abstract</summary>
  Complex image creation and editing often require more than a single generation or editing model. A user request may involve synthesizing images, localizing objects, segmenting regions, editing selected content, compositing intermediate assets, reading text, and enhancing the final result. Such tasks shift multimodal agents from perception-augmented reasoning to manipulation-centered visual creation, where tools must actively transform visual states rather than merely inspect them. However, exist...
  </details>

- **2026-07-06** — Mohammad Zeineldeen, Albert Zeyer, Haoran Zhang et al. — [Revisiting the Relation Between Language Model Perplexity and ASR Word Error Rate for Modern End-to-End Speech Recognition](http://arxiv.org/abs/2607.05612v1)
  <details><summary>📄 Abstract</summary>
  Language model (LM) perplexity (PPL) has historically been used as a proxy for automatic speech recognition (ASR) word error rate (WER), with prior work reporting an approximately linear relation in log-log space. Modern end-to-end ASR systems challenge this assumption because they already contain internal language modeling capacity, are often evaluated without external language models, and can now be combined with neural LMs and large language models (LLMs) through different recognition strateg...
  </details>

- **2026-07-06** — Alvin Wang, Jaromir Savelka — [Prompting Beats Fine-Tuning: Generative Expected Value Scoring for Statutory Term Retrieval](http://arxiv.org/abs/2607.05582v1)
  <details><summary>📄 Abstract</summary>
  Legal concepts in statutes are often expressed using vague terms, and practitioners frequently turn to case law to interpret them. We study the task of ranking case-law sentences by their usefulness for explaining a concept or target statutory term, using an established dataset of 26,959 sentences covering 42 U.S. Code concepts labeled into four explanatory-value categories. We compare two families of methods: (i) supervised fine-tuning of encoder-only models (ModernBERT) and (ii) zero-shot prom...
  </details>

- **2026-07-06** — Francesco Bilotta, Luca Braghieri, Collin Raymond et al. — [Agreement and Diversity in Interpretation](http://arxiv.org/abs/2607.05558v1)
  <details><summary>📄 Abstract</summary>
  We study joint decision-making when agents agree on all primitives other than signal likelihoods. We propose a decision-theoretic measure of interpretive disagreement: a pair of subjective models is more agreeable than another if, uniformly across decision problems, it supports a larger set of signal-contingent plans that both agents weakly prefer ex-ante to the common reservation payoff. We show that this measure is prior independent and can be represented as an inclusion preorder over pairs of...
  </details>

- **2026-07-06** — Haonan Huang — [The yes-no bias of large language models reflects answer order and wording, not shifts in moral judgment](http://arxiv.org/abs/2607.05552v1)
  <details><summary>📄 Abstract</summary>
  Large language models (LLMs) increasingly issue judgments read as binary verdicts, and a growing literature reports such judgments shifting under logically irrelevant changes of wording - among them an amplified yes-no bias on moral dilemmas, absent in humans. A single framing cannot say what such a shift is: in a yes/no question the word "no" is at once logical verdict, lexical token, and last-printed option. We introduce a psychometric battery that separates these: crossed symmetrization - eve...
  </details>

- **2026-07-06** — Mouhamed Amine Bouchiha, Gregory Blanc — [TACTIC-KG: Toward Small Agent Teams for Cyber Threat Intelligence Knowledge Graph Construction](http://arxiv.org/abs/2607.05001v1)
  <details><summary>📄 Abstract</summary>
  Cyber Threat Intelligence (CTI) reports are predominantly unstructured, heterogeneous, and noisy, which limits their direct usability for automated analysis and reasoning. Cybersecurity Knowledge Graphs (CSKGs) provide a structured representation of adversarial entities, actions, and relations, but constructing such graphs from free-text CTI remains a challenge. Recent approaches rely on monolithic Large Language Models (LLMs) to perform end-to-end extraction and completion, leading to high cost...
  </details>

- **2026-07-06** — Xue Qin, Simin Luan, Cong Yang et al. — [Governed Caste Reassignment in Heterogeneous Swarms: An Asymmetric-Trust Protocol with Audited Operator Countersignature](http://arxiv.org/abs/2607.04634v1)
  <details><summary>📄 Abstract</summary>
  In heterogeneous robot swarms, caste reassignment (rebinding a robot to a new capability-bound role) is a high-frequency runtime event driven by battery, payload, and priority changes. Existing approaches treat it as an internal allocation algorithm and do not expose the reassignment to external authority. We argue that for regulated embodied deployments a caste change that elevates a robot's privilege envelope is a governance event that must be auditable and externally authorised. We propose an...
  </details>

- **2026-07-06** — Jiaqi Peng, Xiqian Yu, Delin Feng et al. — [Cortex: A Bidirectionally Aligned Embodied Agent Framework for Long-horizon Manipulation](http://arxiv.org/abs/2607.05377v1)
  <details><summary>📄 Abstract</summary>
  While recent Vision-Language-Action (VLA) models show promise toward generalist manipulation policies, they struggle with long-horizon tasks due to their Markovian nature-relying solely on current observations. Hierarchical dual-system methods address this but suffer from a gap between high-level planning semantics and low-level execution kinematics. We introduce Cortex, a bidirectionally aligned embodied agent framework with a customized planning interface that conveys executable and tractable ...
  </details>

- **2026-07-06** — Sensen Gao, Zhaoqing Wang, Qihang Cao et al. — [PixWorld: Unifying 3D Scene Generation and Reconstruction in Pixel Space](http://arxiv.org/abs/2607.05373v1)
  <details><summary>📄 Abstract</summary>
  3D reconstruction and generation are commonly tackled by separate paradigms: pixel-based regression for reconstruction, and latent diffusion for generation. Recent works attempt to unify them in latent space, but with notable drawbacks: the diffusion objective is defined on latent features rather than the underlying 3D representation, and both branches suffer from information loss introduced by latent encoding, while requiring a pretrained Variational Autoencoder (VAE) or Representation Autoenco...
  </details>

- **2026-07-06** — Xianhao Chen, Jiarui Hu, Yuanbo Yang et al. — [Beyond Isolated Objects: Relationship-aware Open Vocabulary Scene Understanding via 3D Scene Graph Analysis](http://arxiv.org/abs/2607.05348v1)
  <details><summary>📄 Abstract</summary>
  Open-vocabulary 3D scene understanding aims to segment 3D scenes beyond predefined categories by transferring semantic knowledge from vision-language models. Existing methods have advanced this task by lifting language-aligned 2D features into 3D, yet they often rely on context-independent semantic representations, leaving object relationships underexplored for contextual refinement. We propose RelGraphOV, a relationship-aware framework that uses 3D scene graphs to enhance open-vocabulary 3D und...
  </details>

- **2026-07-06** — B. C. Low, S. W. McIntosh — [The steady incompressible ideal free-boundary flows of a hydromagnetic star](http://arxiv.org/abs/2607.05299v1)
  <details><summary>📄 Abstract</summary>
  This self-contained theoretical study treats incompressible, free-boundary flows in a gravitating, ideal hydromagnetic star abutting vacuum, centered on the steady field-aligned flows of Chandrasekhar, Prendergast and Tsinganos, together with a novel family of steady cross-field flows, all as solutions of the axisymmetric Tsinganos equation. In the absence of compressive waves and shocks, an incompressible fluid evolves by its frozen-in magnetic field propagating as transverse Alfvèn waves along...
  </details>


## 📊 统计 / Statistics

| 分类 / Category | 论文数 / Count |
|------|--------|
| jailbreak | 542 |
| prompt-injection | 449 |
| memory-poisoning | 36 |
| tool-use-attack | 91 |
| backdoor | 384 |
| adversarial-attack | 525 |
| privacy-leakage | 3662 |
| steganography | 52 |
| misuse | 798 |
| red-teaming | 105 |
| vulnerability | 2385 |
| defense | 2013 |
| alignment | 1844 |
| robustness | 1677 |
| watermark | 169 |
| unlearning | 81 |
| agent-safety | 48 |
| benchmark | 53 |
| survey | 239 |
| other | 5258 |

---

📚 **全部 20411 篇论文**（2022 至今）请访问 [GitHub Pages](https://ny1024.github.io/AgentSafety-Papers/) 查看完整列表、搜索与筛选。

*Generated by AgentGuard at 2026-07-14 02:35:58*