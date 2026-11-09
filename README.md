<div align="center">

# AgentGuard 🛡️

**Daily Tracking of LLM Agent Security Papers on arXiv**

[![Auto Update](https://github.com/NY1024/AgentSafety-Papers/actions/workflows/daily-update.yml/badge.svg)](https://github.com/NY1024/AgentSafety-Papers/actions/workflows/daily-update.yml)
[![Papers](https://img.shields.io/badge/Papers-36272-blue)](#)
[![License](https://img.shields.io/badge/License-MIT-green)](#)

</div>

---

## 📖 简介 / Introduction

自动追踪 arXiv 上大模型 Agent 安全方向的最新论文，每日更新，关键词智能分类。

*Automatically tracking the latest LLM Agent security papers on arXiv, updated daily with keyword-based classification.*

**最近更新 / Last Updated**: 2026-11-09 14:56 ｜ **论文总数 / Total Papers**: 36272（近 30 天 / Recent 30 days: 4066）

🌐 **[GitHub Pages](https://ny1024.github.io/AgentSafety-Papers/)** — 查看全部 36272 篇论文（含摘要、分类筛选、搜索）/ View all 36272 papers with abstracts, filters & search

## 📑 分类导航 / Category Navigation

- **[jailbreak](#-jailbreak)** — 越狱攻击 / Jailbreak Attacks — 715
- **[prompt-injection](#-prompt-injection)** — 提示注入攻击 / Prompt Injection Attacks — 667
- **[memory-poisoning](#-memory-poisoning)** — 记忆投毒与篡改 / Memory Poisoning & Tampering — 58
- **[tool-use-attack](#-tool-use-attack)** — 工具使用攻击 / Tool-Use Attacks — 172
- **[backdoor](#-backdoor)** — 后门与投毒攻击 / Backdoor & Poisoning Attacks — 551
- **[adversarial-attack](#-adversarial-attack)** — 对抗攻击 / Adversarial Attacks — 664
- **[privacy-leakage](#-privacy-leakage)** — 隐私泄露 / Privacy Leakage — 4556
- **[steganography](#-steganography)** — 隐写与隐蔽通信 / Steganography & Covert Communication — 90
- **[misuse](#-misuse)** — 滥用与误用 / Misuse & Abuse — 1300
- **[red-teaming](#-red-teaming)** — 红队测试 / Red Teaming — 149
- **[vulnerability](#-vulnerability)** — 漏洞与攻击面 / Vulnerabilities & Attack Surfaces — 3934
- **[defense](#-defense)** — 防御与防护方法 / Defense & Protection Methods — 3829
- **[alignment](#-alignment)** — 对齐与安全约束 / Alignment & Safety Constraints — 3576
- **[robustness](#-robustness)** — 鲁棒性与可靠性 / Robustness & Reliability — 3908
- **[watermark](#-watermark)** — 水印与溯源 / Watermarking & Provenance — 722
- **[unlearning](#-unlearning)** — 机器遗忘 / Machine Unlearning — 120
- **[agent-safety](#-agent-safety)** — Agent 安全框架 / Agent Safety Frameworks — 67
- **[benchmark](#-benchmark)** — 安全评测与基准 / Safety Benchmarks & Evaluation — 74
- **[survey](#-survey)** — 综述与系统化 / Surveys & Systematization — 445
- **[other](#-other)** — 其他安全相关 / Other Security-Related — 10675

## 📄 近期论文 / Recent Papers (Last 30 Days)

> 仅展示最近 30 天中最新的 500 篇论文（含日期、作者、摘要）。近 30 天共 4066 篇，完整 36272 篇论文列表请访问 [GitHub Pages](https://ny1024.github.io/AgentSafety-Papers/)

> Showing the latest 500 of 4066 papers from the last 30 days (with date, authors & abstract). For the full list of 36272 papers, visit [GitHub Pages](https://ny1024.github.io/AgentSafety-Papers/)

### 📂 jailbreak
*越狱攻击 / Jailbreak Attacks* — 5 papers

- **2026-11-06** — Tianze Chang, Junjie Chu, Yixin Wu et al. — [GuardrailAgent: An Agentic Framework for Jailbreak Defense](http://arxiv.org/abs/2611.09734v1)
  <details><summary>📄 Abstract</summary>
  Despite undergoing safety training to align with human values, large language models (LLMs) remain vulnerable to jailbreak attacks that circumvent built-in safeguards and elicit malicious behaviors given by the adversary. Existing defenses are mostly static and fail to adapt to new or unknown attack strategies, providing limited resilience. To address these, we propose a multi-agent defense framework, GuardrailAgent, that offers adaptive, end-to-end protection. The system autonomously gathers an...
  </details>

- **2026-11-05** — Fazong Wu, Xin Wang, Ming Yang et al. — [JailBound: FOL-Guided Jailbreak Evaluation for Exploring LLM Behavioral Boundaries](http://arxiv.org/abs/2611.07530v1)
  <details><summary>📄 Abstract</summary>
  As large language models (LLMs) are increasingly deployed as general-purpose conversational assistants, they must handle diverse user requests while reliably refusing harmful ones. Jailbreak attacks craft adversarial instructions or conversational contexts to elicit unsafe responses despite these safeguards. However, existing jailbreak benchmarks often rely on manually designed or collected prompts, making it difficult to systematically extend coverage to new threat conditions. Moreover, existin...
  </details>

- **2026-11-04** — Hamid Dashtbani, Alexandra Dmitrienko — [Addition by Subtraction: Toward Mitigating Fragile Safety Alignment in Large Language Models](http://arxiv.org/abs/2611.06553v1)
  <details><summary>📄 Abstract</summary>
  Large language models (LLMs) undergo safety alignment to prevent harmful generations, yet they remain vulnerable to jailbreak attacks. Recent work reveals a deeper structural weakness: safety alignment can be highly sparse, such that pruning a small number of safety-critical neurons or ablating a single refusal direction can substantially undermine aligned behavior. In this work, we take the first steps toward strengthening safety alignment such that it is less dependent on sparse model componen...
  </details>

- **2026-11-04** — Erfan Baghaei Potraghloo, Saeid Shokoufa, Seyedarmin Azizi et al. — [SafeStart: Mitigating the Overlooked Safety Cost of Active Expert Reduction in MoE LLM Serving](http://arxiv.org/abs/2611.06147v1)
  <details><summary>📄 Abstract</summary>
  Mixture-of-Experts (MoE) language models send each token through a few of many expert subnetworks. Serving methods make these models faster by running even fewer experts per token, and they are validated on accuracy benchmarks. We show that these methods can weaken the model's refusal of harmful requests, and we introduce SafeStart, which largely restores refusal while keeping most of the speedup. In vLLM on one RTX A6000, keeping about two thirds of the selected experts speeds up offline decodi...
  </details>

- **2026-11-03** — Chuancheng Shi, Shangze Li, Wenhua Wu et al. — [TraceRouter++: Causal Semantic Routing Realignment via Optimal Transport](http://arxiv.org/abs/2611.04878v2)
  <details><summary>📄 Abstract</summary>
  Despite their remarkable capabilities, large foundation models (LFMs) remain susceptible to adversarial manipulation. Current safety intervention methods primarily rely on the \textit{locality hypothesis}, rigidly suppressing isolated neurons or features. However, harmful semantics manifest as distributed, cross-layer circuits, rendering localized ablations both brittle against complex jailbreaks and detrimental to general utility. To bridge this gap, we propose TraceRouter++, a routing-level sa...
  </details>


### 📂 prompt-injection
*提示注入攻击 / Prompt Injection Attacks* — 7 papers

- **2026-11-05** — Julian Kunkel, Ali Doosthosseini — [The Power of Meta Access in the Software of the Future --- Demonstrated on LLM Chat UIs and Chat AI](http://arxiv.org/abs/2611.08428v1)
  <details><summary>📄 Abstract</summary>
  Chat remains the default surface for many large language model (LLM) tasks, even as agentic tools such as OpenCode excel at coding and automation. Yet the model sees the current dialogue but not the workspace around it. We explore meta access---giving the assistant a structured, permissioned view of the interface itself and propose a ladder of levels: feature tutoring; metadata, settings, and preference access; retrieval over summaries and messages, confirmed mutation, and full orchestration. Me...
  </details>

- **2026-11-05** — Rongting Zhang, Martin Bertran, Sandeep Avula et al. — [Beyond Instruction Override: Benchmarking Indirect Prompt Injection with Task-Tampering Attacks](http://arxiv.org/abs/2611.07640v1)
  <details><summary>📄 Abstract</summary>
  Indirect prompt-injection (IPI) benchmarks predominantly test planted instructions that redirect a tool-using agent toward an attacker-chosen task. Yet attacker-controlled content can instead tamper with the outcome of the task already in progress. A buyer's dispute evidence can cite a false refund policy to inflate a refund without changing the task. We define IPI by authority rather than instruction-like wording: planted content constitutes an attack when it attempts to influence a decision th...
  </details>

- **2026-11-05** — Xiaobo Chen, Genliang Zhu, Ziyuan Wang et al. — [Signed but Not Safe: Requirement Integrity in Multi-Agent LLM Handoffs](http://arxiv.org/abs/2611.07483v1)
  <details><summary>📄 Abstract</summary>
  Enterprise AI agents increasingly split a user's request across subagents and merge their results, and each handoff can summarize away, alter or ignore a requirement. We report a preregistered study with synthetic, exactly scorable tasks comparing free-text, structured JSON and signed requirement-manifest handoffs: the orchestrator extracts each requirement as a verbatim quote plus a checkable predicate, code signs the manifest with HMAC-SHA256, and deterministic code verifies the merger's decis...
  </details>

- **2026-11-04** — Woosang Lim, Yeseul Chang, Jaewoo Lee — [SPILLWAY: Separating Target Admission from Sanitization to Defend Tool-Using Agents against Prompt Injection](http://arxiv.org/abs/2611.07222v1)
  <details><summary>📄 Abstract</summary>
  Tool-using agents act on email, files, and payments, so an instruction hidden in a web page or a shared document can make an agent send data or money to an attacker. Many runtime defenses put a language model on the decision that lets an action through, so the decision depends on a model that may read the attacker's text and adds model calls to every step. Provenance defenses keep the model off the final check but need a model to plan or route each task first. Where an action goes can instead be...
  </details>

- **2026-11-04** — Guoqin Xiong, Shengtao Wen, Xiang Chen et al. — [SecureGARD: Dynamic Ontology-Guided Governance for Secure Tool-Using LLM Agents](http://arxiv.org/abs/2611.06682v1)
  <details><summary>📄 Abstract</summary>
  Tool-using large language model (LLM) agents translate model outputs into consequential actions, turning indirect prompt injection into an execution-security problem. Existing defenses constrain tool calls, trajectories, or information flows, but often leave action semantics, state dependencies, and evidence relations implicit, limiting generalization across heterogeneous tools and complicating safe updates. We present \ours{}, a dynamic ontology-guided governance framework. \ours{} grounds hete...
  </details>

- **2026-11-04** — Annabella Chow, Jinhao Zhu, Sylvie Venuto et al. — [Securing Web Agents with the Compile-Then-Execute Paradigm](http://arxiv.org/abs/2611.06039v1)
  <details><summary>📄 Abstract</summary>
  Web agents commonly follow the ReAct paradigm, selecting each action from runtime observations that inherently mix trusted and untrusted content. This design makes their control flow vulnerable to prompt injections embedded in webpages. We introduce Baya, a compile-then-execute web agent designed to prevent prompt-injection-driven control-flow hijacking by design. Before accessing the live website, Baya compiles the user's request into an executable Python program that calls a Trusted Website AP...
  </details>

- **2026-11-03** — Yutao Wu, Xiao Liu, Ming Wen et al. — [ScamWorld: An Interactive Environment for Evaluating Web Agents Against Online Fraud](http://arxiv.org/abs/2611.04879v2)
  <details><summary>📄 Abstract</summary>
  Web agents increasingly browse, shop, and manage accounts on behalf of their users. Prior work has shown that they can be misled by adversarial content, including prompt injections and deceptive interfaces. Beyond such attacks, agents operating on the open web also encounter online fraud designed to deceive humans, including fraudulent online stores, fake investment platforms, and advance-fee schemes. How web agents respond to such fraud during task execution remains underexplored, in part becau...
  </details>


### 📂 memory-poisoning
*记忆投毒与篡改 / Memory Poisoning & Tampering* — 1 papers

- **2026-11-06** — David H. Yang, Blake Bullwinkel, Amanda Minnich et al. — [MemoryDojo: Benchmarking Poisoning Through LLM Agent Memory](http://arxiv.org/abs/2611.09721v1)
  <details><summary>📄 Abstract</summary>
  LLM agents benefit from using memory systems to improve performance on long-horizon, multi-session tasks. However, memory introduces a critical attack surface. Malicious instructions encountered in one session may be stored and propagated through memory before being retrieved and acted upon in later sessions. Because memory systems differ in how they process and retrieve information, the downstream effects of poisoning can vary significantly across systems. To quantify the effects of poisoning a...
  </details>


### 📂 backdoor
*后门与投毒攻击 / Backdoor & Poisoning Attacks* — 3 papers

- **2026-11-06** — Louise Nayeong Koh, Yaechan Lee, Myeongjong Lee et al. — [When Feedback Becomes a Backdoor: Tracing Backdoor Skill Formation in Text-Space Skill Optimization](http://arxiv.org/abs/2611.09348v1)
  <details><summary>📄 Abstract</summary>
  Reference answers are a supervision channel in text-space Skill optimization, which produces reusable text artifacts called Skills that guide future agent behavior. Poisoning those answers can induce a persistent trigger-conditioned rule without giving the attacker access to the model, optimizer, or Skill file. We study this reference-feedback poisoning in SkillOpt by tracing an attacker-supplied trigger--payload mapping from reflection to held-out activation. In SearchQA, where the payload repl...
  </details>

- **2026-11-05** — Celeste De Schamphelaere, Juan J. Vazquez, Ari Spiesberger et al. — [Towards interpreting any residual stream direction by scaling activation inversion](http://arxiv.org/abs/2611.08465v1)
  <details><summary>📄 Abstract</summary>
  To interpret a direction in a language model's residual stream, we can look for text that strongly activates it. But when such text is found by scanning a corpus, it is limited to what that corpus contains. We develop Maximally-Activating Example Metamodels (MAEMs), language models which map residual stream directions from a subject model to text exemplars that strongly activate those directions. Our objective is to maximise the cosine similarity of a supplied residual stream direction with the ...
  </details>

- **2026-11-04** — Zhiyang Xia, Yuming Shang, Xi Zhang — [Interactive Backdoor Attacks in LLM-Based Proactive Dialogue Systems](http://arxiv.org/abs/2611.06969v1)
  <details><summary>📄 Abstract</summary>
  LLM-based proactive dialogue systems provide goal-directed support through sustained interaction. Fine-tuning their underlying models on externally supplied dialogue data introduces backdoor risks. Existing LLM backdoor studies primarily focus on eliciting an attacker-specified response upon trigger activation. We present an interactive backdoor attack framework that uses training-data poisoning to steer post-trigger, multi-turn interactions toward an attacker-specified objective. Poisoned fine-...
  </details>


### 📂 adversarial-attack
*对抗攻击 / Adversarial Attacks* — 1 papers

- **2026-11-03** — Drake Benjamin Brown, Khushbu Pahwa, Yubin Ge et al. — [Grounded but Not Immune: Confirmation Bias in Agent-as-a-judge](http://arxiv.org/abs/2611.05662v1)
  <details><summary>📄 Abstract</summary>
  Evaluating open-ended agent tasks increasingly falls to an Agent-as-a-Judge: an evaluator handed tools and the agent's full trajectory so it can verify a result against the environment. The premise is that a judge that gathers its own evidence should be grounded by it. We show that this grounding does not immunize the judge against confirmation bias: a single false pre-screening note, attributed to an authority and carrying no evidential bearing on the correct verdict, overturns up to 40% of a t...
  </details>


### 📂 privacy-leakage
*隐私泄露 / Privacy Leakage* — 31 papers

- **2026-11-06** — Chuxue Cao, Jingru Zeng, Boqin Yin et al. — [Authorization Drift in LLM Agents: Evaluating Boundary Compliance in Multi-Step Tool Use](http://arxiv.org/abs/2611.09113v1)
  <details><summary>📄 Abstract</summary>
  LLM agents can exceed their authorization boundaries while pursuing user goals without an adversary. We formalize this phenomenon as authorization drift across data, tool, scope, and time, and introduce the Authorization Drift Benchmark (ADB): 648 samples across seven domains, each pairing a sufficient compliant path with an attractive unauthorized shortcut. To ensure executable tasks, tempting shortcuts, and feasible compliant paths, Staged Execution-Reflective Synthesis (SERS) grounds benchmar...
  </details>

- **2026-11-06** — Sofia Campos, Carlos Martins, Pedro Pires et al. — [Agentic AI for Healthcare Claim Denial Analysis: A Policy-Grounded Framework for Privacy Preservation](http://arxiv.org/abs/2611.09423v1)
  <details><summary>📄 Abstract</summary>
  In the healthcare sector, claim denials impose significant financial and administrative burdens, emphasizing the need for automated and trustworthy decision-support systems. This paper proposes a modular Agentic Artificial Intelligence (AI) framework for healthcare claim denial analysis, integrating specialized agents for denial risk prediction, risk factor identification, diagnosis-procedure-medication code relationship analysis, and counterfactual analysis. The framework integrates predictive ...
  </details>

- **2026-11-06** — Carlos Martín-Abellán, Mark Kröll — [Enabling Privacy-Preserving Natural Language Access to Industrial Smart Meter Data](http://arxiv.org/abs/2611.09372v1)
  <details><summary>📄 Abstract</summary>
  Energy management officers and grid operators increasingly rely on smart meter data for anomaly detection, performance monitoring, and strategic decision-making. However, extracting actionable insights from large-scale, heterogeneous telemetry databases requires advanced SQL and data engineering expertise, creating a critical bottleneck for non-technical personnel. Furthermore, the strict data privacy regulations and security constraints inherent to critical energy infrastructure often prohibit ...
  </details>

- **2026-11-06** — Gabriel Souza Baggio, Gabriel Machado Lunardi, Guilherme Medeiros Machado et al. — [Assessing the Impact of Retrieval-Augmented Generation on Algorithmic Problem-Solving](http://arxiv.org/abs/2611.09791v1)
  <details><summary>📄 Abstract</summary>
  Competitive programming problems pose distinctive challenges for Large Language Models, as they demand not only proficient code generation but also advanced algorithmic reasoning. This study presents a Retrieval-Augmented Generation approach specifically designed to enhance the capacity of Large Language Models to address such problems. Our approach integrates an embedding-based retrieval mechanism and a similarity search algorithm to identify analogous problems within a knowledge database, empl...
  </details>

- **2026-11-06** — Sarah Wheeler, Veronica Rammouz, Yaoyao Qian et al. — [What to Delegate, What to Preserve: Human Preferences for Agentic AI Across Everyday Life and Work](http://arxiv.org/abs/2611.09730v1)
  <details><summary>📄 Abstract</summary>
  AI agents can execute multi-step tasks on users' behalf, yet the boundaries of acceptable delegation remain unclear. We report a scenario-based survey of 289 U.S. adults with prior AI experience covering 45 use cases across nine life domains. Each respondent evaluated one scenario per domain, producing repeated measures of automation preference, trust, collaboration, AI leadership, privacy concern, and willingness to pay. Automation preferences varied substantially across domains. Generalized es...
  </details>

- **2026-11-06** — Ritik K. Badiya, Siladittya Manna, Ashmit Sinha et al. — [Breaking the Privacy Promise: Gradient Inversion Attacks on Federated Low-Rank Adapted Vision Transformers](http://arxiv.org/abs/2611.09652v1)
  <details><summary>📄 Abstract</summary>
  Parameter-efficient fine-tuning (PEFT) has been increasingly adopted to fine-tune pretrained models with low computational cost and is therefore also preferred in the federated learning paradigm to reduce computational and communication overhead. In this work, we investigate the sparsely explored problem of the risk of private data leakage in LoRA-adapted Vision Transformers (ViTs), where low-rank updates weaken the gradient signal available to a server with access to individual client updates. ...
  </details>

- **2026-11-06** — Subhankar Maity, Faiza Belbachir, Omar Boucelma et al. — [Analyzing Code Provenance in LLMs for Programming Education](http://arxiv.org/abs/2611.09177v1)
  <details><summary>📄 Abstract</summary>
  Large language models (LLMs) play an increasing role in programming education, challenging traditional assessment methods as they can generate fully functional code instantly. This disrupts the reliability of student submissions as indicators of learning and effort. To address this issue, code provenance is essential for tracing the origins of code and distinguishing student-authored, AI-generated, and externally sourced components. We extend the Min-K% probability approach by incorporating synt...
  </details>

- **2026-11-06** — Ryan Hsiang, William Adkisson, Robert Joseph George et al. — [LeanDojo-v2: A Comprehensive Library for AI-Assisted Theorem Proving in Lean](http://arxiv.org/abs/2611.09048v1)
  <details><summary>📄 Abstract</summary>
  Building on recent progress in machine learning for formal theorem proving in Lean, we introduce LeanDojo-v2: an end-to-end framework that unifies repository data extraction, LLM fine-tuning, proof search, AI autocompletion, and LLM-assisted theorem proving in a single software library. In addition, we provide Lean4Code, a lightweight IDE that integrates the various features of LeanDojo-v2 through a simple, mathematician-friendly UI. These tools will enable mathematicians and researchers to easi...
  </details>

- **2026-11-05** — Jiacheng Cen, Anyi Li, Ning Lin et al. — [Spectral symmetry fingerprints in equivariant representations](http://arxiv.org/abs/2611.07410v1)
  <details><summary>📄 Abstract</summary>
  Symmetry governs the organization of physical structures, while symmetry breaking reveals their transformations. In geometric deep learning, symmetry imposes rank constraints on equivariant representations, limiting the expressive capacity of equivariant graph neural networks (GNNs). Here we show that these constraints can instead be exploited: the singular-value spectra of equivariant representations provide a unified fingerprint of structural symmetry. We introduce spectral symmetry fingerprin...
  </details>

- **2026-11-05** — Zhiquan Liu, Haolin Gao, Bo Wu et al. — [CANMentor: A Large-Small Model Collaboration Framework for CAN Bus Intrusion Detection](http://arxiv.org/abs/2611.07853v1)
  <details><summary>📄 Abstract</summary>
  The Controller Area Network (CAN) bus lacks built-in security mechanisms, making real-time intrusion detection necessary. However, resource and latency constraints limit vehicle-side intrusion detection systems (IDSs) to lightweight models, whose detection performance and generalization can degrade under non-independent and identically distributed (non-IID) data. Meanwhile, uploading original CAN messages to the cloud for more powerful model inference risks exposing sensitive vehicle information...
  </details>

- **2026-11-05** — Ziqiao Weng, Yuanzhi Liang, Haibing Huang et al. — [Generator-Aligned Reward Modeling with Target-Aware Bounded Optimization for Visual Generation](http://arxiv.org/abs/2611.07648v1)
  <details><summary>📄 Abstract</summary>
  Post-training aims to enhance desired attributes in visual generative models while preserving their general generation capabilities. Reward-guided post-training faces two challenges: real training data may mismatch the generator's output distribution, and attribute supervision may be confounded by unrelated content. Unbounded reward maximization can also cause overoptimization and degrade generation quality. We propose a framework combining Generator-Aligned Reward Modeling (GARM) and Target-Awa...
  </details>

- **2026-11-05** — Yuan-Chiao Cheng, Yi-Hsuan Yang, Vincent K. M. Cheung — [ProCraft: Instruction-Driven Music Production from Free-Form Text](http://arxiv.org/abs/2611.07423v1)
  <details><summary>📄 Abstract</summary>
  Music production typically involves multiple editing operations that each require specialized tools and expertise. Existing text-guided music editing systems support few operations or instruments, operate on short clips, or handle only one operation per instruction, unlike real workflows where several changes are requested at once. Here, we present ProCraft, a lightweight 0.5B-parameter autoregressive codec language model that edits 30s music excerpts end-to-end from free-form instructions, incl...
  </details>

- **2026-11-05** — Johannes Taraz, Abhinav Kumar, Sahar Abdelnabi — [Trilemma: How Agents choose between Honesty, Confidentiality, and Task Completion](http://arxiv.org/abs/2611.08312v1)
  <details><summary>📄 Abstract</summary>
  Personal AI agents often act on underspecified instructions and draw on context such as their user's messages and calendar to decide how to proceed. This context can contain private preferences that interfere with the task, with other people's interests, or with confidentiality norms. Prior work has studied deception under goal conflicts and the leakage of private information, but largely as separate problems. We study both problems together in a simulated company Slack workspace in which four e...
  </details>

- **2026-11-05** — Petru Neague, Quinten Stokkink, Martijn de Vos et al. — [ZeroRAG: Adaptive Semantic Peer Routing for Decentralized Retrieval-Augmented Generation](http://arxiv.org/abs/2611.07928v1)
  <details><summary>📄 Abstract</summary>
  Retrieval-augmented generation (RAG) is a standard approach to enhance the reliability of large language model (LLM) outputs by retrieving documents relevant to a query and supplying them in the LLM prompt. Today's RAG systems collect, index, and serve these documents from centralized stores. In practice, however, documents are owned by organizations, devices, and individuals who cannot or will not surrender custody of them to a central party, e.g., because of privacy, copyright or regulatory co...
  </details>

- **2026-11-05** — Dina EL Zein, Shashi Kumar, James Henderson — [An Information Bottleneck for Post-hoc Memorization Mitigation in LLMs](http://arxiv.org/abs/2611.07669v1)
  <details><summary>📄 Abstract</summary>
  Recent studies have shown that large language models (LLMs) can memorize and reproduce copyrighted training data, raising serious privacy and intellectual property concerns. In this work, we investigate whether memorization can be mitigated without modifying or retraining the underlying model through an information bottleneck. We propose a modular plug-and-play framework that inserts a nonparametric variational information bottleneck (NVIB) between a frozen LLM backbone and its language modeling...
  </details>

- **2026-11-05** — Siyuan Jiang, Xiang Cai, Peixu Wang et al. — [AiXapply: Fast and Reliable Full-File Code Integration with Specialized Small Models for IDE Workflows](http://arxiv.org/abs/2611.07634v1)
  <details><summary>📄 Abstract</summary>
  Large language models increasingly assist developers by proposing small code edits, yet reliably integrating a partial update snippet into an existing file while preserving unrelated content remains poorly supported by current code-generation workflows. We formalize the Code Integration (Apply) task as follows: given an original file and an update snippet, the system must produce the complete merged file while preserving all content outside the requested edit. We construct a high-quality multi-l...
  </details>

- **2026-11-05** — Yuchen Cao, Zhenyu Mao, Jacky Wai Keung et al. — [Route Before Response: Fail-Closed Routing for LLM-Enabled Customer-Service Software](http://arxiv.org/abs/2611.07534v1)
  <details><summary>📄 Abstract</summary>
  LLM-enabled customer-service software in financial institutions must choose a downstream service before responding. Classifiers and LLM routers can identify a relevant label or destination, but a composed application must still verify dispatch permission and entity registration. We study this integration problem as boundary-aware pre-response routing. We present RouteBR, a controller in which one model call proposes a primary service action and registered object, then deterministic code checks i...
  </details>

- **2026-11-04** — Xue Zheng, Aylin Yener — [Server-Side Sparse Assignment for Federated Mixture-of-Experts](http://arxiv.org/abs/2611.07093v1)
  <details><summary>📄 Abstract</summary>
  Large language models (LLMs) are increasingly recognized for their remarkable capabilities; federated learning (FL) offers a promising framework for collaboratively fine-tuning LLMs on edge devices while achieving data privacy. However, edge devices are inherently heterogeneous: clients may exhibit diverse data distributions and resource constraints, including limited memory and computation budgets. Recent federated Mixture-of-Experts (MoE) approaches address these challenges by using sparse exp...
  </details>

- **2026-11-04** — Calister Nnona — [CoRTeC: A Differentially Private Release for Synthetic Tabular Data, Decodable by Any Generator](http://arxiv.org/abs/2611.06342v1)
  <details><summary>📄 Abstract</summary>
  The records that could train the most useful models, such as a hospital's patient files, are often the ones an institution cannot share. We propose CoRTeC, a method that releases synthetic versions of such records under differential privacy. Differential privacy places a proven limit on what the synthetic data can reveal about any person, and in particular on membership inference. CoRTeC spends the privacy budget once, on a small file of noisy counts designed for training a classifier. For each ...
  </details>

- **2026-11-04** — Zheao Li, Jiancheng An, Chau Yuen — [SIM-Enabled Wave-Domain Processing in MIMO-OFDM Receivers: Architecture, Modeling, and Validation](http://arxiv.org/abs/2611.05999v1)
  <details><summary>📄 Abstract</summary>
  This paper develops a wave-domain linear receiver for wideband MIMO-OFDM, where the main high-dimensional linear processing conventionally performed after sampling is physically shifted to propagation through stacked intelligent metasurfaces (SIMs). The proposed receiver transforms receive-port waveforms into OFDM-domain symbols through three cascaded SIM-enabled functional sections. The first section, SIM_1, performs channel-memory processing and channel shortening in an energy-concentration se...
  </details>

- **2026-11-04** — Jie Fu, Xiangpeng Deng, Yuan Hong et al. — [Timing is Everything: Inferring Temporal Membership in Continually Updated Models](http://arxiv.org/abs/2611.05781v1)
  <details><summary>📄 Abstract</summary>
  Continual model updating has become a common practice in the deployment of machine learning systems. However, the dynamic training behaviors give rise to new risks not sufficiently addressed by existing studies. In this paper, we present the first systematic study of temporal privacy risk in continually updated deep learning models. We formalize the notion of temporal membership in continually updated models. We then define the temporal membership inference attack, which seeks to infer whether a...
  </details>

- **2026-11-04** — Shahan Ali Memon, Anna-Maria Gueorguieva, Anukriti Kumar et al. — [U.S. State Guidance on AI in K-12 Education: A Comparative Content and Citation Analysis](http://arxiv.org/abs/2611.06762v1)
  <details><summary>📄 Abstract</summary>
  In the years following the public release of ChatGPT in late 2022, more than half of U.S. states have published formal guidelines around AI usage in K-12 education, creating a record of largely independent state education departments responding to a shared technological disruption. In this work, we analyze publicly available AI usage guidance documents from 35 states in the U.S. and Puerto Rico. We compare the guidance in these documents across various dimensions, including pedagogy and instruct...
  </details>

- **2026-11-04** — Xi Chen, Julien Cumin, Fano Ramparany et al. — [Multi-Resident Data Association in Smart Homes via MDP Modeling and Behavior Cloning](http://arxiv.org/abs/2611.06296v1)
  <details><summary>📄 Abstract</summary>
  Ambient sensors offer a privacy-preserving solution for activity recognition in smart homes, yet they face a critical challenge in multi-resident environments known as Data Association, which aims to identify the resident triggering a specific anonymous sensor event. Existing approaches fundamentally fail to maintain global consistency by often yielding conflicting associations for silent residents. Additionally, these methods frequently suffer from severe trajectory fragmentation caused by the ...
  </details>

- **2026-11-04** — Tianqi Zong, Baosheng Li, Nuocheng Yang et al. — [CARE-FL: Federated Fine-Tuning of Multimodal LLMs in Resource-Constrained Edge Networks](http://arxiv.org/abs/2611.06169v1)
  <details><summary>📄 Abstract</summary>
  Domain-specific adaptation of Multimodal Large Language Models (MLLMs) in privacy-sensitive edge environments requires federated fine-tuning, yet client selection remains challenging due to heterogeneous multimodal data and modality availability, dynamic system conditions, and evolving client utility during training. We propose Constraint-Aware Reinforcement Learning for Efficient Federated Fine-Tuning (CARE-FL), a constrained online client-selection framework for federated MLLM Low-Rank Adaptat...
  </details>

- **2026-11-04** — Elise L. Han, Tatsunori Hashimoto — [Reconciling Privacy with Provenance for Language Model Watermarks](http://arxiv.org/abs/2611.06100v1)
  <details><summary>📄 Abstract</summary>
  Watermarking has great potential for regulating the use of language models (LMs), but its deployment has been marred by controversy, as many users argue that fine-grained tracking of LM usage violates their privacy. This tension reduces the effectiveness of watermarks, as users engage in evasion strategies such as paraphrasing that can remove much of the watermark signal. We show that provenance and privacy can be reconciled if we shift the goal of watermark design from tracking individuals to e...
  </details>

- **2026-11-04** — Hengyou Kong, Xiaoli Xu, Zilong Liu et al. — [AFDMA with Heterogeneous Post-Chirp Parameters: Supporting User-Specific Waveform Configurations](http://arxiv.org/abs/2611.06063v1)
  <details><summary>📄 Abstract</summary>
  This paper investigates a downlink affine frequency division multiple access (AFDMA) framework supporting flexible user-specific waveform configurations with heterogeneous post-chirp parameters. The proposed framework is in sharp contrast to conventional disjoint chirp-subcarrier allocation, which may destroy inter-user orthogonality when users employ heterogeneous post-chirp parameters. Such a loss of orthogonality manifests as cross-basis leakage onto user-allocated chirp subcarriers, which we...
  </details>

- **2026-11-04** — Bin Wen, Dai-Qiao Zhang, Tien-Ping Tan — [Selective, Risk-Controlled Emotion Forecasting in Conversation: From a Persistence Barrier to Departure Detection with Conformal Guarantees](http://arxiv.org/abs/2611.05896v1)
  <details><summary>📄 Abstract</summary>
  Forecasting emotion in conversation is increasingly framed as predicting the next emotional state's value. We show this targets a hard quantity in a state-observed testbed and propose a learnable, deployable reformulation instead. On valence-arousal-dominance trajectories from a dyadic corpus, repeating a speaker's own previous state sets a persistence baseline that no frozen-encoder correction meaningfully improves upon and a state-space filter exceeds; the floor requires the historical state t...
  </details>

- **2026-11-04** — Zhanhong Jiang, Qisai Liu, Soumik Sarkar — [Vision Paper: Why Distributed LLM Post-Training and Decentralized Alignment Are Now Essential](http://arxiv.org/abs/2611.05841v1)
  <details><summary>📄 Abstract</summary>
  This vision paper argues that distributed learning, including federated and decentralized, should become a first-class paradigm in LLM post-training, not merely a privacy add-on. Current methods like RLHF and DPO rest on an invisible assumption: preference data should be centralized. We contend this assumption is scientifically unjustified, practically unsustainable, and ethically problematic. As LLMs deploy into healthcare, law, finance, and multilingual communities, preference data originates ...
  </details>

- **2026-11-03** — S M Rayeed, Qian Ma, Charles V. Stewart et al. — [How Finely Can Vision-Language Models See Biology? Bio-VQA: A Benchmark for Taxonomic, Morphological, Spatial and Individual Reasoning](http://arxiv.org/abs/2611.05559v1)
  <details><summary>📄 Abstract</summary>
  In biodiversity monitoring, a single image raises several questions: which taxon, how many, which trait, and whether the individual has been seen before. Vision-language models (VLMs) could answer all of these from the image, but their ability is largely untested in biology, as existing benchmarks focus mostly on species identification within a few taxonomic groups. We present Bio-VQA, the largest biological visual question answering (VQA) benchmark and the only one to span four aspects of biolo...
  </details>

- **2026-11-03** — Mingxuan Li, Huanzhi Mao, Ruitao Zheng et al. — [SlackBench: Benchmarking Agents on Collaborative Projects Grounded in Real Code Repositories](http://arxiv.org/abs/2611.05512v1)
  <details><summary>📄 Abstract</summary>
  AI Agents are becoming digital coworkers that can browse the web, write code, run experiments, and assist humans over extended horizons. Yet existing benchmarks fall short of real knowledge work: many rely on synthetic data or isolated tasks, missing the complex, multi-party dynamics of collaborative projects, where critical information is scattered across conversations, code, and evolving decisions. Even simple workplace questions may require locating relevant channels and direct messages, reco...
  </details>

- **2026-11-03** — Zhengtao Gao, Francesco Bombassei De Bona, Leonardo Alchieri et al. — [Self-Supervised Pretraining for Label-Efficient Facial Expression Recognition using Smart Glasses](http://arxiv.org/abs/2611.05711v1)
  <details><summary>📄 Abstract</summary>
  Facial Expression Recognition (FER) on optomyographic (OMG) smart glasses such as OCOsense enables privacy-preserving, camera-free affect sensing for health and well-being. Most FER systems are fully supervised, i.e., they rely either on hand-crafted expert features with classical machine learning, or on end-to-end deep models trained from labelled data. Both depend on large quantities of labelled expressions, which are costly to collect and limit deployment in real-world, personalized settings....
  </details>


### 📂 misuse
*滥用与误用 / Misuse & Abuse* — 15 papers

- **2026-11-06** — Jiashu Zhang, Jiaming He, Zheming Zhang et al. — [AUTEUR: Acoustic Plan Learning for Red-Teaming Text-to-Audio Models](http://arxiv.org/abs/2611.09351v1)
  <details><summary>📄 Abstract</summary>
  Automated red-teaming of text-to-audio models requires test prompts that pass textual screening and expose harmful acoustic content. The central challenge is to connect the sounds produced by the target model to both reusable test generation and prompt revision. Our key idea is to represent test descriptions as structured acoustic plans that organize foreground sounds, context, and vocal attributes. To this end, we propose acoustic plan learning, a framework that learns and refines these plans u...
  </details>

- **2026-11-06** — Hongwei Lin, Xun Huang, Chenglu Wen et al. — [Zero-Query Transferable Pretend Benign Attacks with Amortized Online Generation for Cooperative Perception](http://arxiv.org/abs/2611.09256v1)
  <details><summary>📄 Abstract</summary>
  Cooperative perception enables an ego agent to acquire information from collaborators beyond its own sensors' reach. Yet, the most beneficial messages are often the hardest to verify from local observations. Pretend Benign (PB) exploits this asymmetry by targeting regions with weak local verifiability and applying multi-objective perturbations, making harmful feature changes appear to be benign assistance. However, PB is victim-dependent: selecting regions and optimizing perturbations require th...
  </details>

- **2026-11-06** — Lei Zhenbing, Lei Chang — [Incentive Pathologies in a Live LLM Agent Arena: An Empirical Study of Concentration, Reward-Rule Implementation Discrepancy, and Network Dilution](http://arxiv.org/abs/2611.09445v1)
  <details><summary>📄 Abstract</summary>
  We audit one live LLM agent arena (AITRAP; 22 autonomous agent seats, ~96,000 reasoning nodes) over nine days (Oct 16-25, 2026), during which the platform deployed two bundled incentive changes: a progressive tax reform (V2.9.3, Oct 19) and a seed-inversion with explorer-side action update (V3.0, Oct 21). These serve as before-and-after markers, not cleanly isolated interventions. Four exploratory predictions are tested against ten data frames (F1-F10) using the Gini coefficient, Top-K concentra...
  </details>

- **2026-11-06** — Jungtaek Kim, Jaden Park, Jongwon Jeong et al. — [Where Should Learning Live? Regret Analysis for Text, Parameter, and Joint Adaptation](http://arxiv.org/abs/2611.09701v1)
  <details><summary>📄 Abstract</summary>
  Language-model systems can select prompts and parameter adapters repeatedly during deployment, using feedback to guide later choices. Earlier choices may change the context or environment inherited by later configurations. We study selection among preconstructed candidates and compare cumulative loss with the best fixed prompt--parameter pair used from the beginning. This excess loss separates into three terms: selection regret within the available family, the gap from restricting that family, a...
  </details>

- **2026-11-06** — Abhishek Gautam — [Benchmarking Speaker Embedders in the Sub-Second Regime for Real-Time Voice AI Agents](http://arxiv.org/abs/2611.09516v1)
  <details><summary>📄 Abstract</summary>
  Real-time Voice AI agents must separate the active user from intelligible background speech that survives conventional noise suppression. Background sources include television audio, family members, and colleagues. Production denoisers remove non-stationary environmental noise effectively. Background speech shares the spectral characteristics of the target and passes through, causing false acceptances in downstream speaker verification (SV) and automatic speech recognition (ASR). We benchmark op...
  </details>

- **2026-11-05** — Zhitao He, Chi Him Zhang, Chengru Han et al. — [Multimodal-SEA: Benchmarking AI Agent Security under Multimodal Social Engineering Attacks](http://arxiv.org/abs/2611.08281v1)
  <details><summary>📄 Abstract</summary>
  Personal AI agents face social engineering attacks supported by forged multimodal content, but existing evaluations mainly focus on text-based dialogue, leaving their intrinsic security under such attacks insufficiently studied. We introduce Multimodal-SEA, an interactive benchmark comprising 608 expert-designed tasks grounded in real-world fraud cases, covering 14 domains and 152 attack scenarios with prepared multimodal content. The tasks span four difficulty levels and reflect the distinct so...
  </details>

- **2026-11-05** — Abhishek Satyam, Hossein Siadati, Haadi Jafarian et al. — [The Promise of Strategic Agentic Scambaiting](http://arxiv.org/abs/2611.08170v1)
  <details><summary>📄 Abstract</summary>
  Scammers have increasingly adopted AI-driven capabilities, evolving from automated message generation to fully agentic conversational systems that scale operations and maximize the exploitation of fraudulent resources before detection and takedown. In parallel, agentic scambaiting has emerged as a defensive approach in which autonomous agents impersonate potential victims and engage scammers in sustained interactions to extract actionable threat intelligence, such as mule bank accounts and crypt...
  </details>

- **2026-11-05** — Yizhen Jiang, Haowei Guo, Tianyi Bai et al. — [MCPHallu: Benchmarking Reasoning, Execution, and Memory Hallucinations in MCP Agents](http://arxiv.org/abs/2611.07689v1)
  <details><summary>📄 Abstract</summary>
  Large language model agents are increasingly deployed through the Model Context Protocol (MCP), which allows them to discover and invoke tools across multiple servers at runtime. Existing MCP benchmarks primarily measure task completion; where they diagnose failures, they do so after execution rather than building specific reasoning, execution, and memory failure risks into task construction.   We introduce MCPHallu, a benchmark for diagnosing hallucination-prone agent failures in MCP environmen...
  </details>

- **2026-11-05** — Nicholas Roehner, Bryan Bartley, Jacob Beal et al. — [Building Barricades: Red-Teaming Agentic Biosynthesis Planning](http://arxiv.org/abs/2611.08218v1)
  <details><summary>📄 Abstract</summary>
  The rapid democratization of biotechnology, enhanced by large language models (LLMs) and agentic software, is eroding longstanding barriers that have limited biosynthesis planning to experts. We present BioBulbul, an agentic system that couples LLMs with open-source biodesign tools for retrobiosynthesis, enzyme selection, gene cluster design, and DNA assembly planning. Using simple natural language prompts, BioBulbul autonomously generates plausible biosynthesis pathways and corresponding gene c...
  </details>

- **2026-11-04** — Hong kyu Lee, Kai Shu, Li Xiong — [Compositional Unalignment: Auditing Safety in Large Vision-Language Models](http://arxiv.org/abs/2611.07216v1)
  <details><summary>📄 Abstract</summary>
  Large vision-language models (LVLMs) are vulnerable to compositional harm: an image and a prompt that are benign in isolation become harmful through the model's cross-modal reasoning. Recent alignment methods report strong scores on compositional safety benchmarks, but an LLM judge only measures observed behavior and cannot reveal how robustly safety is integrated into the model. We argue that un-alignment provides a complementary audit of alignment robustness. We first show that minimal supervi...
  </details>

- **2026-11-04** — Yifan Wang, Junyu Lu, Shun Zhang et al. — [Beyond Risk Cues: A Mechanism-Level Benchmark and Verifiable Debate for Scam Video Detection on the Web](http://arxiv.org/abs/2611.06110v1)
  <details><summary>📄 Abstract</summary>
  Online scam videos pose significant threats to individuals and society. Existing studies primarily focus on binary classification, offering limited insights into how scams work and the reasoning behind detection decisions. Moreover, they often overlook the challenge of distinguishing scam videos from superficially similar non-scam content, such as advertisements, and the robustness of detection models against misleading arguments. These limitations hinder reliable scam video detection. To addres...
  </details>

- **2026-11-04** — Tianwei Zhang, Ivy Njoki Nyagwencha, Zahraa Dirani et al. — [ALTO: African and Levantine Tech-Facilitated Gender-Based Violence Corpus](http://arxiv.org/abs/2611.06706v1)
  <details><summary>📄 Abstract</summary>
  Tech-facilitated gender based violence (TFGBV) is a pervasive online harm affecting women and gender minority groups through its many direct and covert forms. Current models and annotated datasets for gendered harm detection are dominated by data from, and models trained in, Global North languages. In collaboration with civil society organizations (CSOs) from Jordan, Francophone West Africa, and Kenya, we developed a community-led approach to crowdsource culturally and linguistically relevant in...
  </details>

- **2026-11-03** — George Newhouse AM, Trisha Ramesh, Tiara de Silva — [The Moving Frontier: How the National Justice Project Is Using Digital Technology to Expand Access to Justice](http://arxiv.org/abs/2611.08052v1)
  <details><summary>📄 Abstract</summary>
  Over the past three decades, technological advances have assisted individuals to gain access to legal information, enhance the efficiency of legal services, and streamline dispute resolution. More recently, the proliferation of generative artificial intelligence has reinforced this emphasis on firm-level productivity, with commercial legal practice increasingly leveraging artificial intelligence tools to automate document creation and optimise case management. While commercial technology focuses...
  </details>

- **2026-11-03** — Duc Anh Vu, Thong Nguyen, Hoang Pham et al. — [Objective-Conditioned Active Preference Learning for Multi-Objective Alignment](http://arxiv.org/abs/2611.05506v1)
  <details><summary>📄 Abstract</summary>
  Aligning large language models (LLMs) with several objectives, such as helpfulness, harmlessness, and honesty, typically relies on preference judgment for each objective, growing the annotation cost linearly with the number of objectives. Active preference learning can reduce this cost by selecting the comparisons whose labels are expected to change the policy most. Existing remedies either lack an objective-aware query selection mechanism for the multi-objective setting or regard conflicting pr...
  </details>

- **2026-11-03** — Mehdi Shajari — [Assurance-Conditioned Continuous Authorization for Autonomous AI Agents](http://arxiv.org/abs/2611.05632v1)
  <details><summary>📄 Abstract</summary>
  Autonomous software agents can act through tools, delegate work, and change their models or execution environments while earlier authorizations remain in flight. We present Assurance-Conditioned Continuous Authorization (ACCA), an approach designed to be harness-independent, for maintaining operational authority according to currently justified assurance. It distinguishes evidence validity from contextual applicability, derives assurance claims from eligible evidence, and resolves a multidimensi...
  </details>


### 📂 red-teaming
*红队测试 / Red Teaming* — 3 papers

- **2026-11-06** — Ruoyu Zhou, Shuyao Jiang, Haifeng Ruan et al. — [GreyZone: Production-quality Agentic Application Threats](http://arxiv.org/abs/2611.09161v1)
  <details><summary>📄 Abstract</summary>
  Agents are increasingly deployed across domains such as coding, banking, and commerce. Their ability to invoke tools and change application state makes security testing important for reliable deployment. Although agent security has been studied through various adversarial testing approaches, benchmarks grounded in production agent environments remain limited. We introduce GreyZone, a benchmark for evaluating automated red-teaming services against real-world agent applications. Unlike benchmarks ...
  </details>

- **2026-11-05** — Yao Huang, Yifan Wang, Yitong Sun et al. — [Stress Testing Chain-of-Thought Monitoring Against Covert Misalignment](http://arxiv.org/abs/2611.07586v1)
  <details><summary>📄 Abstract</summary>
  As LLM agents advance rapidly in autonomy, the risk of hidden objectives that bypass safety constraints becomes increasingly plausible. Chain-of-thought (CoT) monitoring offers a key control mechanism by reading the agent's reasoning and flagging misalignment before it materializes into action, yet its reliability depends on the realism of the red-team it is stress-tested against. Existing red-teaming efforts rely on shared templates, such as casting a side task as a prerequisite, which treat th...
  </details>

- **2026-11-05** — E. Kelly Buchanan, Crystal Zhou, Scott W. Linderman et al. — [Benchmarks as Software: Terminal-Bench and the Case for Continuous Benchmarks](http://arxiv.org/abs/2611.08417v1)
  <details><summary>📄 Abstract</summary>
  Coding agents are among the most economically consequential deployments of LLMs to date, making reliable evaluation increasingly important. Yet even benchmarks that are carefully validated at release can become stale. As models improve, they can discover valid solutions that existing verifiers reject, while changes to evaluation infrastructure can invalidate assumptions embedded in tasks and tests. We call the resulting accumulation of defects benchmark maintenance debt: a growing gap between be...
  </details>


### 📂 vulnerability
*漏洞与攻击面 / Vulnerabilities & Attack Surfaces* — 58 papers

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

- **2026-11-05** — Yu-Cheng Chou, Shihao Wang, Jin Huang et al. — [VFlash: Fast, Accurate Visual Planning via Flash Primitive Decoding](http://arxiv.org/abs/2611.08449v1)
  <details><summary>📄 Abstract</summary>
  Models for physical AI tasks, such as robotics and autonomous driving, need not reason solely in language. They can use visual plans--points, bounding boxes, and trajectories--to represent spatial goals and anticipate motion. However, autoregressive vision-language models generate these plans one coordinate token at a time, making richer predictions increasingly costly. We introduce VFlash, a method for fast, accurate visual planning through Flash Primitive Decoding. VFlash exploits the known st...
  </details>

- **2026-11-05** — Fuhao Li, Wenxuan Song, Qizhou Huang et al. — [SLA: Scaling Spatial-Language-Action Model via Continual Pre-training](http://arxiv.org/abs/2611.08373v1)
  <details><summary>📄 Abstract</summary>
  Reliable robotic manipulation requires both semantic understanding and precise control in three-dimensional space. However, vision-language-action (VLA) foundations largely inherit visual representations from 2D vision-language pre-training, while spatial supervision is often introduced only during task-specific adaptation. Developing spatial understanding as a transferable foundation-model capability therefore calls for learning from broader robot experience. We present SLA, a Spatial-Language-...
  </details>

- **2026-11-05** — Hong Jun Lee, Ziyan Wang, Jun Wang et al. — [Discovering Learning Rules that Shape Others](http://arxiv.org/abs/2611.08335v1)
  <details><summary>📄 Abstract</summary>
  In general-sum games, self-interested learners can reach outcomes that are poor for everyone, which has motivated methods that shape the opponent's learning. Methods like Learning with Opponent-Learning Awareness (LOLA), which differentiates through the opponent's learning process, and Model-Free Opponent Shaping (M-FOS), which uses model-free optimisation methods for long-horizon opponent shaping, have enabled mutual cooperation and exploitation of learners. However, these methods require acces...
  </details>

- **2026-11-05** — Hanyu Qiu, Ze Liu, Zhe Zhao et al. — [From Twisted Facts to Rogue Agents: Can LLMs Reliably Detect Multi-Dimensional Hallucinations?](http://arxiv.org/abs/2611.08231v1)
  <details><summary>📄 Abstract</summary>
  Large language models (LLMs) are widely used for information access, content production, and agent-based task execution, but their outputs remain vulnerable to subtle, high-risk hallucinations. To systematically evaluate and advance post-generation hallucination detection, we introduce HaluCheck, a large-scale, bilingual benchmark comprising over 42k instances spanning both factual hallucinations in text and faithfulness hallucinations in agent trajectories. HaluCheck features fine-grained, mult...
  </details>

- **2026-11-05** — Maciej Kisielewicz, Michał Kędziora, Ngoc Thanh Nguyen — [Escalate or Close: How Fast-Tier Models Handle Held-Out Web Attack Families in Two-Tier Triage](http://arxiv.org/abs/2611.08229v1)
  <details><summary>📄 Abstract</summary>
  In two-tier triage a fast model decides most web requests and escalates the rest to a slow tier, so an attack the fast tier closes is never examined. We hold each of seven attack families out of training, recalibration and thresholds, splice the payloads into parameters of real browsing traffic, and compare zero-shot decision models, which return a probability for a typed question, with supervised detectors, a local language model, the OWASP Core Rule Set and an anomaly baseline. Detectors train...
  </details>

- **2026-11-05** —  ATLAS Collaboration — [Development and performance of a transformer-based lepton isolation algorithm with the ATLAS experiment](http://arxiv.org/abs/2611.08194v1)
  <details><summary>📄 Abstract</summary>
  The Prompt Lepton Isolation Tagger (PLIT) is a transformer-based algorithm designed to distinguish prompt leptons (electrons and muons) produced in the primary decays of electroweak gauge bosons from non-prompt leptons produced in hadron decays and from misidentified leptons. It is primarily used in measurements targeting multilepton final states with important backgrounds from non-prompt and misidentified leptons. PLIT exploits information from charged-particle tracks associated with the lepton...
  </details>

- **2026-11-05** — Yalin E. Sagduyu, Tugba Erpek, Aylin Yener — [AI-Native Task-Oriented Semantic Communications over a Relay: Benefits and Vulnerabilities](http://arxiv.org/abs/2611.08155v1)
  <details><summary>📄 Abstract</summary>
  Semantic communication (SemCom) using a relay node is considered, where the relay assists in conveying task-relevant information from a source to a destination, with meaning defined by classification labels. A joint end-to-end design of the source encoder, relay transformation, and destination decoders is developed to optimize both semantic inference accuracy and perceptual reconstruction quality for image data. Relay-assisted schemes are shown to outperform direct transmission, with gains that ...
  </details>

- **2026-11-05** — Bin Liu, Wei Ni, Tommy Svensson et al. — [Structured Agentic Learning for Persistent Spatial Acquisition in RDT-TAIS-Assisted Communications](http://arxiv.org/abs/2611.08141v1)
  <details><summary>📄 Abstract</summary>
  Persistent TAIS operation can reduce repeated radio-information acquisition by reusing environmental knowledge across control intervals. This knowledge changes with radio-environment evolution and current communication task. This paper studies persistent spatial knowledge maintenance for TAIS control and formulates it as a sequential information-acquisition problem that maximizes effective communication performance while accounting for physical-acquisition overhead under an outage-reliability co...
  </details>

- **2026-11-05** — Shuyi Miao, Zheng Li, Xu Xie et al. — [Circe: Training-Free LLM Self-Evaluation via Component Interaction Consistency](http://arxiv.org/abs/2611.07948v1)
  <details><summary>📄 Abstract</summary>
  As large language models (LLMs) are increasingly deployed in real-world applications, evaluating the correctness of their responses is crucial for reliable use. However, such evaluation is challenging because reference answers are rarely available in practice. Existing reference-free methods mainly rely on output signals, which may assign high scores to incorrect responses and thus do not necessarily reflect correctness. This motivates exploring the model's internal computation for complementary...
  </details>

- **2026-11-05** — Ziang Cui — [Bridging Structure and Semantics: Knowledge Graph Verification via Triple-to-Text Alignment](http://arxiv.org/abs/2611.07780v1)
  <details><summary>📄 Abstract</summary>
  Semantic accuracy is an important dimension of knowledge graph quality. Graph-based scoring methods exploit relational structure, while textual representations allow classifiers to draw on knowledge encoded by pre-trained language models (PLMs). We present GenVer, a generative verifier that scores triples using both their serialized form and generated natural language representations (NLRs). A triple-text alignment procedure selects training pairs for a sequence-to-sequence generator; a BERT-bas...
  </details>

- **2026-11-05** — Kotaro Oishi, Kazuma Ikeda, Ryosei Hara et al. — [Towards Real-Time Full-Waveform LiDAR Transformers via Intensity-Guided Token Reduction and Physics-Aware Augmentation](http://arxiv.org/abs/2611.07613v1)
  <details><summary>📄 Abstract</summary>
  LiDAR is a critical sensor for autonomous driving and robotics, yet it remains vulnerable to adverse conditions such as fog, rain, transparent objects, and low-reflectance surfaces. Full-waveform LiDAR (FWL) addresses these limitations by capturing the complete return waveform as a histogram, preserving rich reflection characteristics including multi-path echoes and weak signals. While recent Transformer-based approaches have demonstrated promise on FWL data, two fundamental bottlenecks remain: ...
  </details>

- **2026-11-05** — Seungdeok Roh, Seokjun Ryu, Sohee Park et al. — [A Gingerbread House for LLM Agents: Source-Planned Honeypots That Lure Autonomous Attackers into an Isolated Shadow](http://arxiv.org/abs/2611.07611v1)
  <details><summary>📄 Abstract</summary>
  LLM agents can exploit web vulnerabilities fast enough that patching may come too late. Deception against such agents has mostly lured them away from a real target that stays reachable. We study a different arrangement: an LLM defender plans a static honeypot from the application's source, and a router sends every later request of a client it confirms as an attacker, including a working exploit, to an isolated shadow copy. We compare no defence, this static plan, and an augmented configuration w...
  </details>

- **2026-11-05** — Chongyu Qu, Ritchie Zhao, Yufan He et al. — [TACT-KV: Tri-Axis Cosine Transform for Compressing Volumetric KV Caches in Medical VLMs](http://arxiv.org/abs/2611.07593v1)
  <details><summary>📄 Abstract</summary>
  Vision-language models (VLMs) applied to 3D medical scans face a structural memory wall. A single CT or MRI volume produces tens of thousands of vision tokens, and the resulting key-value (KV) cache scales linearly with both batch and context. Existing KV compression methods operate on the cache's feature or token statistics, or apply 1D and 2D transforms, leaving the three-axis spatial structure in the cache unexploited. We propose TACT-KV (Tri-Axis Cosine Transform), a calibration-free KV comp...
  </details>

- **2026-11-05** — Zongxi Liu, Shuai Mao, Jie Chuai et al. — [SEROA: Stable Encrypted-Traffic Representation and Online Adaptation for Service-Aware Networks](http://arxiv.org/abs/2611.07550v1)
  <details><summary>📄 Abstract</summary>
  Mobile networks are evolving toward service-aware operation to support heterogeneous applications with diverse quality-ofservice (QoS) and quality-of-experience (QoE) requirements. In practice, however, the widespread use of encryption makes service types difficult to observe directly, which limits the deployment of service-aware optimization in operational networks. Recent raw-byte representation learning methods have improved offline encrypted-traffic classification, but their robustness in re...
  </details>

- **2026-11-05** — Purnata Saha, Rifatul Islam, John Quarles — [Breaking the Modality Barrier: Multimodal Fusion With Missing Modalities for Cybersickness Prediction](http://arxiv.org/abs/2611.07386v1)
  <details><summary>📄 Abstract</summary>
  Cybersickness is a major barrier to comfortable VR use, and reliable prediction often requires multiple physiological and behavioral sensors. However, existing models typically assume a fixed set of modalities, making them vulnerable when sensors are unavailable and difficult to generalize across datasets with different sensor configurations. We adapt a transformer-based model that handles arbitrary sensor combinations without imputing missing data. Anchor-based contrastive learning maps heterog...
  </details>

- **2026-11-05** — Cassandra C. Chou, Benjamin Q. Huynh, Allison Koenecke et al. — [Adversarial Multiplicity: Cherry-Picked Models and the Limits of Disclosure](http://arxiv.org/abs/2611.07378v1)
  <details><summary>📄 Abstract</summary>
  Predictive multiplicity -- where similarly accurate models disagree on individual predictions -- can be leveraged to optimize secondary metrics (e.g., fairness) without loss in predictive performance. However, exploiting multiplicity opens the opportunity for motivated parties (or coding agents gaming their objectives) to steer predictions toward their own ends, such as in litigation or consumer disputes with automated decision-making tools. In these adversarial multiplicity settings, we disting...
  </details>

- **2026-11-04** — Abdullah Al Noman, Gaurav Singh, Rameez Ahmed et al. — [IRIS: Intelligent Random Access with Integrated Shared Learning for Decentralized LEO Direct-to-Satellite Uplinks](http://arxiv.org/abs/2611.07201v1)
  <details><summary>📄 Abstract</summary>
  Grant-free uplink access in low-Earth-orbit (LEO) non-terrestrial networks (NTNs) poses a coordination challenge when multiple UEs share a satellite channel without real-time centralized scheduling under long propagation delays and time-varying channels. Conventional random access does not exploit peer context, leading to collisions and inefficient channel use as contention increases. To address this problem, we propose IRIS, a multi-agent reinforcement learning framework for decentralized grant...
  </details>

- **2026-11-04** — Korbinian Kügler, Carolin Schmidt, Florian Dandl et al. — [Regulating Autonomous Mobility-on-Demand Operators with Fixed and Adaptive Penalties: A Multi-Agent Reinforcement Learning Approach](http://arxiv.org/abs/2611.07122v1)
  <details><summary>📄 Abstract</summary>
  Profit-maximizing Autonomous Mobility-on-Demand (AMoD) operators may exploit consumer surplus through excessive prices and underserve less profitable regions by relocating vehicles away from them. We study how penalty-based regulation of an AMoD operator in a multimodal mobility system can limit surge pricing and improve regional service availability. We model regulation as an outer control loop that acts on a learning-based operator. Static regulation with fixed penalties is formulated as a Mar...
  </details>

- **2026-11-04** — Mohammed Rahman Sherif Khan Mohammad, Ardhendu Behera, Sandip Pradhan et al. — [SD-LoRA: Training-Time Structural Distillation into LoRA for Few-Shot Vision-Language Adaptation](http://arxiv.org/abs/2611.07063v1)
  <details><summary>📄 Abstract</summary>
  Few-shot adaptation of vision-language models must balance two competing goals: learning fine-grained visual distinctions from very limited supervision and preserving the efficiency that makes frozen CLIP-like models attractive for deployment. Existing lightweight adaptation methods, including prompt tuning, LoRA, and cache-based adapters, typically supervise global image embeddings and therefore underuse token-level structure. Conversely, structure-aware methods exploit local evidence but often...
  </details>

- **2026-11-04** — Mohammed Rahman Sherif Khan Mohammad, Ardhendu Behera, Sandip Pradhan et al. — [Batch-Conditioned Semantic Anchors for Robust Transductive Adaptation of Vision--Language Models](http://arxiv.org/abs/2611.06993v1)
  <details><summary>📄 Abstract</summary>
  Transductive adaptation improves vision-language models at test time by refining predictions on an unlabeled batch, but current methods face a key trade-off. Aggressive approaches exploit batch structure but can drift when batches are sparse, have prior shift, or cover little of the label space. Conservative methods better preserve CLIP text semantics, but fixed semantic references can under-adapt even when the batch provides strong corrective evidence. We propose JPTA (Joint Prior and Transport...
  </details>

- **2026-11-04** — Zhenyi Shen, Junru Lu, Wei Liu et al. — [On the Opportunities and Challenges of Prefill-to-Autoregressive Cross-Model Transfer](http://arxiv.org/abs/2611.06976v1)
  <details><summary>📄 Abstract</summary>
  Prefill-to-Autoregressive Cross-model Transfer (PACT), a form of latent communication between language models, combines a larger model's prompt representations with a smaller model's efficient generation, offering a promising way to balance capability and inference cost. However, existing systems provide limited support for independently evaluating large-small model collaboration, and improved task performance alone does not establish whether the receiver benefits from the sender's information. ...
  </details>

- **2026-11-04** — Weichen Fan, Haiwen Diao, Penghao Wu et al. — [From Pixels to Actions - Towards Native Vision-Language-Action Policies](http://arxiv.org/abs/2611.06918v1)
  <details><summary>📄 Abstract</summary>
  Vision-language-action models are typically built on a simple premise: perception is first compressed by visual encoders, and action reasoning begins only afterwards. Yet manipulation often hinges on precisely the visual signals most vulnerable to this abstraction, e.g., local geometry, boundaries, depth, and subtle state changes. This raises a fundamental question: should action policies inherit a fixed visual endpoint, or directly access evolving visual computation? We introduce NEO-VLA, a str...
  </details>

- **2026-11-04** — Chaomeng Lu, Pooya Rostami Mazrae, Bert Lagaisse — [PatchCon: Patch-aware Weighted Supervised Contrastive Learning for Vulnerability Detection](http://arxiv.org/abs/2611.06583v1)
  <details><summary>📄 Abstract</summary>
  Automated vulnerability detection is critical for securing modern software systems, yet existing learning-based approaches often treat functions as independent samples and underuse the supervision provided by vulnerability-fixing patches. In this paper, we propose PatchCon, a CodeBERT-based patch-aware contrastive learning model for function-level vulnerability detection. PatchCon jointly optimizes vulnerability classification and supervised contrastive learning, and treats vulnerable-patched fu...
  </details>

- **2026-11-04** — Jianhong Ma, Wenhao Li, Xixing Li et al. — [Towards Early Warning of Real-World Vulnerabilities: An Evidence-Aware Decoupled Method for CVSS Vector Prediction Based on Unstructured Disclosures](http://arxiv.org/abs/2611.06477v1)
  <details><summary>📄 Abstract</summary>
  Early assessment of Common Vulnerability Scoring System (CVSS) vectors from Open Source Intelligence (OSINT) can reduce the delay between initial public disclosure and official National Vulnerability Database (NVD) scoring. Existing predictors, trained mainly on standardized late-stage descriptions, degrade on noisy and incomplete pre-NVD reports. We introduce PARSE, a vulnerability-disclosure lifecycle model, and VPre, an early assessment framework built on two-level Evidence-Aware Decoupling. ...
  </details>

- **2026-11-04** — Zhuangyan Hu, Zhuoxuan Liang, Wei Li et al. — [Graph Foundation Models Can Become Effective Multivariate Time Series Anomaly Detectors](http://arxiv.org/abs/2611.06441v1)
  <details><summary>📄 Abstract</summary>
  Multivariate time series anomaly detection (MTSAD) relies on modeling both temporal dynamics and inter-sensor dependencies to identify complex system faults. Although graph-based detectors explicitly model sensor topologies, they train task-specific networks from scratch on limited target-domain data, remaining vulnerable to spurious correlations and unable to reuse transferable priors. While pretrained Graph Foundation Models (GFMs) offer transferable topological priors and anomaly discriminabi...
  </details>

- **2026-11-04** — Adrian Hayler, Shashank Reddy Chirra, Andrei Lupu et al. — [Zero-Shot Coordination among LLM Agents](http://arxiv.org/abs/2611.06409v1)
  <details><summary>📄 Abstract</summary>
  We study zero-shot coordination (ZSC), where independently developed agents must coordinate at test time. While ZSC has been well studied in the RL literature, far less is known about the performance of LLM agents despite their increasing deployment in such settings. Existing work on LLM coordination often relies on specialised scaffolding that independently developed agents are unlikely to share in practice. Moreover, evaluations on complex environments (e.g., Hanabi) make it difficult to pinpo...
  </details>

- **2026-11-04** — Ehud Shapiro — [Corralling AI Risks with Grassroots Contracts](http://arxiv.org/abs/2611.06374v1)
  <details><summary>📄 Abstract</summary>
  AI's inflection point is a fountain of alarming risks. Digital platforms in particular are vulnerable to three major AI risks, as those in control of global platforms cede control to AI, of the algorithms, of membership and of content: (1) AI control of global platforms, social and economic, used by the majority of humanity, resulting in the majority of humanity becoming vulnerable to AI control. (2) Unaccountable AI agents operating anonymously on social and economic digital platforms, side-by-...
  </details>

- **2026-11-04** — Norbert Sándor Szolnoki, Gábor Antal — [Reassessing Dataset Quality and Fine-Tuning Practices for Vulnerability Detection on PrimeVul dataset](http://arxiv.org/abs/2611.06373v1)
  <details><summary>📄 Abstract</summary>
  Recent studies report promising results from supervised fine-tuning of pre-trained code language models for automated vulnerability detection on benchmarks such as PrimeVul. In this paper, we present a large-scale empirical evaluation of both model performance and dataset quality in this setting.   We systematically fine-tune three widely used encoder models (CodeBERT, GraphCodeBERT, and UniXCoder) across five imbalance mitigation strategies, extensive hyperparameter sweeps, and multiple random ...
  </details>

- **2026-11-04** — Xingchen Zou, Maonan Wang, Kemou Jiang et al. — [Traffic-VL: Reinforced Vision-Language Models for Generalizable End-to-End Traffic Signal Control](http://arxiv.org/abs/2611.06353v1)
  <details><summary>📄 Abstract</summary>
  Existing traffic signal control methods typically rely on structured traffic states produced by dedicated perception pipelines. Emerging visual approaches often use idealized simulator images and convert them into intermediate representations before control, limiting their ability to directly exploit roadside visual observations. To bridge both the visual-domain and perception-to-decision gaps, we introduce SynTra-V and Traffic-VL. SynTra-V converts physics-based traffic simulations into photore...
  </details>

- **2026-11-04** — Jiongchi Yu, Keke Lian, Junqing Wang et al. — [A.S.E 2.0: Understanding How Repository Context Impacts the Security of LLM-Generated Code](http://arxiv.org/abs/2611.06294v1)
  <details><summary>📄 Abstract</summary>
  Large language model (LLM) coding assistants and agents construct a repository context before generating code. For security-sensitive code, this context decides whether the model sees the project's safeguards (e.g., authorization checks) or insecure code to imitate. However, context construction is designed almost exclusively for functional correctness, and secure-code benchmarks treat the context as fixed, so how repository context affects the security of generated code remains unclear. We cons...
  </details>

- **2026-11-04** — Jorge García-Carrasco, Javier Sanchis, Álvaro Navarro et al. — [Analysis of Local Open-Weight LLM Agents on Vulnerability-Reproduction Tasks](http://arxiv.org/abs/2611.06257v1)
  <details><summary>📄 Abstract</summary>
  Open-weight language models that fit on a single consumer GPU are becoming capable on a growing range of tasks, and they matter because they can run locally without sending the code to a hosted service. Vulnerability reproduction, turning a vulnerability description into an input that crashes the vulnerable build, is a natural target for them, since it is an automated analysis task closer to test generation than to code comprehension and it runs against a build that must be executed rather than ...
  </details>

- **2026-11-04** — Zhi Hong, Qianlong Wang, Hongchen Wei et al. — [HarnessFlow: MCTS-Guided Harness Optimization for LLM Agents](http://arxiv.org/abs/2611.06254v1)
  <details><summary>📄 Abstract</summary>
  The performance of large language model (LLM) agents depends on both the underlying model and the harness that governs interaction with tools and the environment. Yet harness design remains largely manual, and automating it requires navigating an open-ended search space through costly end-to-end evaluations. We introduce HarnessFlow, a framework for optimizing complete executable harnesses under a limited candidate-evaluation budget, with the model and task environment held fixed. HarnessFlow or...
  </details>

- **2026-11-04** — Martin Pinzger, Katharina Stengg, Christian Macho et al. — [SBVUL: Statement-Based Vulnerability Detection](http://arxiv.org/abs/2611.06135v1)
  <details><summary>📄 Abstract</summary>
  Many recent approaches for vulnerability detection use large language models (LLMs) to classify functions as vulnerable or benign, leaving developers to locate the exploitable statements. Furthermore, while these approaches have shown performance improvements, they still fall short in distinguishing vulnerable from patched real-world functions. This paper presents SBVul, an agentic approach that detects exploitable statements in C/C++ functions. In Phase~1, an LLM agent explores the function and...
  </details>

- **2026-11-04** — Songtang Han, Letian Liu, Zhiyan Yang et al. — [High-transformer-ratio plasma-based afterburner for extending X-ray free-electron laser photon energies to $\gtrsim$50 keV](http://arxiv.org/abs/2611.05957v1)
  <details><summary>📄 Abstract</summary>
  Bright coherent X-rays in the $\gtrsim$50 keV range are highly desirable for applications in materials science, high-energy-density physics, and nuclear physics, but are difficult to obtain from present X-ray free-electron laser (XFEL) facilities. Plasma-based afterburners offer a compact route to increasing the electron-beam energy, yet high transformer ratio (TR) operation is vulnerable to hosing instability, which can severely degrade the witness beam quality. We propose using a transversely ...
  </details>

- **2026-11-04** — Penghui Li — [When File Ingestion Misleads Language Models: Measuring and Mitigating Divergences in Office Documents](http://arxiv.org/abs/2611.05806v1)
  <details><summary>📄 Abstract</summary>
  Office documents are now routinely uploaded to large language models (LLMs) for processing. However, an LLM does not always see what a human sees, because it typically reads the text that an extractor produces from the document's underlying Office Open XML (OOXML) files. Depending on the implementation, extractors differ in which OOXML parts they read and how they interpret them, so their output can differ from what Office applications display. For example, by slightly shifting the positions of ...
  </details>

- **2026-11-03** — Dar-Yen Chen, Yi-Zhe Song — [NitroFusion2: Bringing Adversarial Loss to the Text Stream of Multimodal Diffusion Transformers](http://arxiv.org/abs/2611.05648v1)
  <details><summary>📄 Abstract</summary>
  Adversarial diffusion distillation has conventionally relied on image features for discrimination. We revisit this choice for multimodal diffusion transformers (MMDiTs), whose text stream becomes image-dependent through joint attention. We introduce Text-Stream Adversarial Distillation (TSAD), which exploits intermediate text-token states as a new adversarial representation. Because the text stream has already read the image while remaining tied to the text condition, changing that condition cha...
  </details>

- **2026-11-03** — Soraya Frías-Guadalupe, Pedro Paredes, Carlos Castaneda-Marroquín — [Cibersapiens: Gamifying Cybersecurity Education to Engage Secondary Students](http://arxiv.org/abs/2611.05587v1)
  <details><summary>📄 Abstract</summary>
  Cybersecurity education and awareness are often tailored for businesses, leaving general citizens, especially young people, unprepared. Despite the availability of educational resources, cybersecurity training is not provided equally to all individuals, particularly children and teenagers. As digital risks such as sexting, grooming, and cyberbullying, among others, increase, young users remain vulnerable. However, existing awareness efforts fail to engage them effectively and current content lac...
  </details>

- **2026-11-03** — Reza Ramji, Preston Vander Vos, Ziming Zeng et al. — [Anduin: A sybil-resistant agentic marketplace reputation system](http://arxiv.org/abs/2611.05586v1)
  <details><summary>📄 Abstract</summary>
  As autonomous AI agents enter permissionless onchain markets, selecting new service providers remains a core challenge. Existing reputation systems depend on scarce resources like human curation, identity credentials, or voluntary reviews, while naive volume rankings are vulnerable to Sybil attacks.   We evaluate whether existing onchain payment histories can yield provider ratings that are resilient against Sybil attacks. Using a 157-day dataset comprising 66M agentic transactions worth $6.1M a...
  </details>

- **2026-11-03** — Sasha Luccioni, Travis LaCroix — [What Do We Mean When We Say 'F*ck AI'?: Moral Panic, Semantic Indeterminacy, and the Reification of Techno-Capitalism](http://arxiv.org/abs/2611.05574v1)
  <details><summary>📄 Abstract</summary>
  Academic and (increasingly) public resistance to artificial intelligence (AI) often blurs the line between legitimate critique of techno-capitalist exploitation and (inflated) existential risk. Moreover, discourse around AI can sometimes resemble a "moral panic" where an apparently clear and identifiable scapegoat is targeted in lieu of the complex systemic problems that are causing (genuine and justified) social anxieties. However, AI is not a monolith. In this paper, we explore the environment...
  </details>

- **2026-11-03** — Hemanth Ram, Sai Shankar Narasimhan, Shubhankar Agarwal et al. — [TSFM Meets LLM: Context as Covariates](http://arxiv.org/abs/2611.05515v1)
  <details><summary>📄 Abstract</summary>
  Textual information is ubiquitous in real-world time series datasets, appearing as news, reports, and annotations that hold key predictive signals not deducible from numerical history alone. Large Language Models (LLMs) interpret text but lack numerical precision, while Time Series Foundation Models (TSFMs) are quantitatively accurate but cannot reason about the effects of text. Moreover, the lack of large-scale paired multimodal datasets limits progress in bridging this gap. In this work, we ad...
  </details>

- **2026-11-03** — WonJun Moon, Seongchan Kim, Dahun Kim et al. — [Factorized MLLM Embeddings for Composed Image Retrieval](http://arxiv.org/abs/2611.05193v2)
  <details><summary>📄 Abstract</summary>
  Composed Image Retrieval (CIR) aims to retrieve a target image given a reference image and a modification text. Although recent approaches leveraging Multimodal Large Language Models (MLLMs) have shown significant progress, we argue that the MLLM's compositional understanding remains underutilized. This stems from directly mapping composed queries into a retrieval embedding via contrastive supervision alone, without explicitly resolving the intended visual modifications. In this work, we introdu...
  </details>


### 📂 defense
*防御与防护方法 / Defense & Protection Methods* — 61 papers

- **2026-11-06** — Ruihan Hu, Wei Luo, Yu-Ming Shang et al. — [Logit Laundering: Evading Data-Use Auditing in Large Language Models](http://arxiv.org/abs/2611.09446v1)
  <details><summary>📄 Abstract</summary>
  Data-use auditing in Large Language Models (LLMs) aims to determine whether the given data has been used for training, thereby supporting data ownership safeguards. A dominant solution is data watermarking, which embeds traceable signals into training data and detects them in model outputs. Recent studies have proposed many watermarking-based auditing methods in LLMs. However, systematic investigation from an adversarial perspective remains limited: non-compliant LLM providers would use unauthor...
  </details>

- **2026-11-06** — Ayush Sawarni, Wenqian Xing, Tijana Zrnic et al. — [Knowing When to Intervene: Causal Evaluation of AI Agents](http://arxiv.org/abs/2611.09792v1)
  <details><summary>📄 Abstract</summary>
  Current evaluations of agentic AI systems primarily rely on benchmarks. However, the static nature of benchmarks makes them uninformative about the value of auditing interventions at deployment time. For reliable deployment, we often need to determine within an agent's trajectory whether or not to intervene, e.g., by verifying the agent's current output or steering it toward different behavior, using either human review or more costly models or time-consuming agentic supervision. The value of su...
  </details>

- **2026-11-06** — Muhammad Ashfaq, Ahmed R. Sadik, Ewan Warburton et al. — [SafeOrchestrate: Runtime Checked Intent-Driven Orchestration for Cyber-Physical Systems](http://arxiv.org/abs/2611.09364v1)
  <details><summary>📄 Abstract</summary>
  Modern cyber physical systems (CPS) integrate heterogeneous sensors, actuators, controllers, and services, composed at runtime rather than at design time. Orchestrating such systems through natural language (NL) is attractive, but unconstrained large language model (LLM) tool use is risky because actions must respect device capabilities, runtime state, and safety constraints. We present Safe Orchestrate, a reference architecture for runtime checked, intent driven CPS orchestration. Given an NL i...
  </details>

- **2026-11-06** — Yi Hao, Krzysztof Puczko, Levy Ferreira Costa et al. — [An Optimal Power-Flow Grouping Topology for Single-Isolation-Stage Multi-Output Solid-State Transformers](http://arxiv.org/abs/2611.09305v1)
  <details><summary>📄 Abstract</summary>
  Electric-vehicle dc fast-charging stations and data centers require multiple high-power dc outputs with independently varying demands. Conventional multi-output solid-state transformers typically establish a common dc bus and use downstream dc/dc converters for port-level regulation and, where required, galvanic isolation. A single-isolation-stage solid-state transformer can eliminate this additional high-power interface stage by directly forming multiple isolated outputs from its submodule dc/d...
  </details>

- **2026-11-06** — Oliver Noll, Nicholas Tan Jerome, Alexander Lehnen et al. — [Towards an Autonomous AI Steward for Large-Scale Physics Experiments: Integrating Causal Diagnostics, RAG, and Conformal Prediction](http://arxiv.org/abs/2611.09298v1)
  <details><summary>📄 Abstract</summary>
  Long-term particle physics experiments face critical operational challenges: monitoring non-stationary machine data streams and preserving tacit expert knowledge. We present the "Helmholtz Co-Pilot," a hybrid Multi-Agent System (MAS) acting as an autonomous experiment steward. The system can be triggered interactively by human operators or autonomously by an asynchronous causal diagnostics engine that runs independently of the MAS reasoning core. Continuously monitoring live hardware streams suc...
  </details>

- **2026-11-06** — Yi Hao, Levy Ferreira Costa, Krzysztof Puczko et al. — [DC-Link Voltage Regulation in a Single-Isolation-Stage Multioutput Solid-State Transformer for Wide-Range DC Outputs](http://arxiv.org/abs/2611.09276v1)
  <details><summary>📄 Abstract</summary>
  Single-isolation-stage solid-state transformers with balancing circuits eliminate an additional downstream dc--dc conversion stage. However, the remaining isolated converters must directly accommodate a wide output-voltage range. This paper investigates variable dc-link voltage operation of a single-isolation-stage multioutput SST to ease this requirement. Coordinated cascaded H-bridge modulation and embedded four-switch balancing circuits support intentionally unequal submodule dc-link voltages...
  </details>

- **2026-11-06** — Laurin Schmid, Suman Navaratnarajah, Koel Dutta Chowdhury et al. — [FondueQA: A Benchmark for Evaluating Parametric Compensation in Multi-Hop QA](http://arxiv.org/abs/2611.09274v1)
  <details><summary>📄 Abstract</summary>
  Large Language Models (LLMs) show remarkable performance based on parametric knowledge, i.e., their ability to recall facts and associations internalized in a model's weights. However, studying this capability on established multi-hop benchmarks may be complicated by benchmark contamination, as many of these benchmarks have been publicly available long enough to plausibly appear in modern pretraining corpora. As a result, correct answers under missing evidence may reflect either general parametr...
  </details>

- **2026-11-06** — Abdelkader Metales, Miriam Grabenheinrich, Aicha Metales — [Copies Are Not Confirmations: How News Duplication Fools LLM Judges and Continual Learners](http://arxiv.org/abs/2611.09203v1)
  <details><summary>📄 Abstract</summary>
  Many news reports of a claim are copies of one source: wire stories, content shared within a media group, syndicated features and press releases. We ask whether LLM judges and continual learners treat such copies as independent confirmations. In 200,000 English CC-News articles, a MinHash detector links 18.9% to a near-copy from another outlet (precision 0.97 once boilerplate is removed); it links 92% of edited reprints to their originals but none of the LLM rewrites by phi4, Llama 3.2 or Gemini...
  </details>

- **2026-11-06** — Boming Xia, Qinghua Lu, Dino Sejdinovic et al. — [When Routine Operations Break Architectural Pattern Relationships in LLM Agent Harnesses](http://arxiv.org/abs/2611.09088v1)
  <details><summary>📄 Abstract</summary>
  LLM agent harnesses distribute tool mediation, state management and safety guardrails across native services, independently written plugins and configuration. Routine operations can change the runtime order or retained state that architectural pattern relationships require, without any code change. We study five relationships associated with the Guardrail Enforcement Point, Autonomy Controller and Blackboard patterns across five released harnesses, analysing a main sample of fourteen independent...
  </details>

- **2026-11-06** — Zijie Xing, Xingyue Liu, Runze Wang et al. — [KnowEvo: Knowledge Evolution for Protein Optimization](http://arxiv.org/abs/2611.09013v1)
  <details><summary>📄 Abstract</summary>
  Large language models (LLMs) have shown promise in scientific discovery, yet systematically accumulating and refining reusable scientific knowledge remains challenging. Existing approaches primarily improve LLM-based problem solving through parameter optimization or feedback-driven refinement of prompts, programs, and solution trajectories, leaving acquired expertise either embedded in model weights or scattered across iterative problem-solving processes. As a result,knowledge is difficult to sy...
  </details>

- **2026-11-06** — Xiao Tan — [Multimodal Training with Knowledge Traction for Video Anomaly Detection](http://arxiv.org/abs/2611.09536v1)
  <details><summary>📄 Abstract</summary>
  The task of weakly supervised video anomaly detection is challenging. Existing approaches mainly model video frame features and determine whether anomalies are present based on their magnitudes. In this work, we propose a novel method that incorporates external knowledge into training to improve model performance, robustness, and generalization. We leverage textual prompts and a large language model (LLM) to establish prior information for the specific task, and employ dictionary learning to nor...
  </details>

- **2026-11-06** — Elnur Adl Zarabi, Amit Kumar, Adi Singh et al. — [On the Effectiveness and Limitations of Open-Weight LLMs for Low-Resource Offensive Language Detection in Danish](http://arxiv.org/abs/2611.09506v1)
  <details><summary>📄 Abstract</summary>
  We study the effectiveness and robustness of open-weight large language models (LLMs) for Danish offensive language detection, an underexplored low-resource task. We evaluate four model families (Llama, Mistral, Gemma, and Qwen) across eleven prompting strategies spanning five design categories, cross-prompt generalization, Danish orthographic variation, and robustness under balanced and naturally imbalanced class distributions. We compare against three BERT-family baselines with distinct pre-tr...
  </details>

- **2026-11-06** — Akansha Gautam, Aparna Bharati, Mayank Vatsa et al. — [T2I Models Rarely Invert Negation but Often Fail to Suppress Negated Concepts: Benchmarking Negation Suppression in Text-to-Image Generation](http://arxiv.org/abs/2611.09304v1)
  <details><summary>📄 Abstract</summary>
  Text-to-image diffusion models often fail to suppress explicitly negated concepts, such as a lamp for "a desk without a lamp." We introduce T2I-NSI, a benchmark and metric for measuring negation sensitivity in text-to-image generation. It pairs each negated prompt with a canonical positive counterpart and factorizes negation by linguistic form (lexical/semantic, morphological, syntactic) and target type (objects, attributes, relations, compositions, and nested cases). The benchmark contains 759,...
  </details>

- **2026-11-05** — Howard Halim, Eyasu Getahun Chekole, Jianying Zhou — [LABBA: LLM-Assisted Behavioral Biometric Authentication](http://arxiv.org/abs/2611.08343v1)
  <details><summary>📄 Abstract</summary>
  Behavioral biometrics have emerged as a promising complement to traditional physiological biometrics by leveraging dynamic human characteristics. These modalities offer advantages including continuous authentication, inherent liveness detection, and greater resistance to credential theft and other spoofing attacks. However, existing systems remain limited in adaptability, contextual awareness, and semantic reasoning as they primarily rely on similarity metrics, static thresholds, or supervised c...
  </details>

- **2026-11-05** — Mahdi Ghadamyari, Reza Habibi — [Decision Models as Retrieval Gates Against Injection and Pollution](http://arxiv.org/abs/2611.08325v1)
  <details><summary>📄 Abstract</summary>
  Retrieved web text can carry instructions aimed at the language model, or synthetic pages written to mislead. We test whether released open-weight decision models, which answer typed questions about a text without generating tokens, can screen retrieved passages against both threats. On a benchmark of 1,000 questions over forum-style web pages with hidden injected instructions, a Kev-4B gate reads each passage's HTML. Attack success, measured automatically, falls from 27.9% with no defence to 13...
  </details>

- **2026-11-05** — Yao Huang, Yichi Zhang, Yifan Wang et al. — [A Behavioural Framework for Predicting and Understanding Loss of Control in Frontier Artificial Intelligence Systems](http://arxiv.org/abs/2611.07953v1)
  <details><summary>📄 Abstract</summary>
  Frontier artificial intelligence (AI) systems are increasingly operating over longer horizons with diminishing human oversight, raising the risk of loss of control: systems acting beyond effective human control with potentially irreversible consequences. Because such failures may become observable only after containment is difficult, they must be assessed prospectively. We introduce a behavioural framework that decomposes loss-of-control risk into three factors: misaligned motive, harm-enabling ...
  </details>

- **2026-11-05** — Hongsen Cao, Chia-Yen Chiang, Mona Jaber et al. — [Edge-Assisted Crowdsensing for Explainable Cyclist Safety Perception](http://arxiv.org/abs/2611.08441v1)
  <details><summary>📄 Abstract</summary>
  Cyclist fatality rates remain high despite policy support for active travel, and autonomous vehicles add complexity to mixed traffic. Neither crash statistics nor multi-model detection pipelines scale to continuous monitoring of perceived safety along a route. We present an edge-assisted crowdsensing system: handlebar cameras supply street-level frames, a vision-language model (VLM) turns each frame into structured traffic attributes through a single prompt, and an explainable boosting machine (...
  </details>

- **2026-11-05** — Fazl Barez, Tung-Yu Wu, Hunar Batra et al. — [Understanding AI from the Inside: The State of Mechanistic Interpretability for AI Safety](http://arxiv.org/abs/2611.08438v1)
  <details><summary>📄 Abstract</summary>
  Neural networks are likely to be among the most consequential artefacts in human history. As these systems become more capable and autonomous, their potential to cause societal harm also grows, making AI safety one of the defining challenges of our time. Yet we continue to build increasingly powerful systems without fully understanding how they work, how they will behave in unfamiliar situations, or how to reliably control them. Mechanistic interpretability offers a path towards understanding th...
  </details>

- **2026-11-05** — Ali Mohammadi Ruzbahani, Abbas Yazdinejad, Hadis Karimipour — [FedReason: Large Language Models as Weight-Space Meta-Aggregators for Heterogeneous Federated Learning](http://arxiv.org/abs/2611.08383v1)
  <details><summary>📄 Abstract</summary>
  Federated learning servers combine client models with a fixed aggregation rule, and each rule in common use is designed for one kind of heterogeneity. We study whether a large language model (LLM) that inspects the client models can choose the rule itself, without any training on the server. In FedReason, the LLM is called every ten rounds. It analyses the weights by running code in a restricted server-side sandbox, sees only the printed results, may score a few candidates on a 500-image proxy s...
  </details>

- **2026-11-05** — Chen Cecilia Liu, Roi Reichart, Anna Korhonen — [Cultural Adaptation within Repeated Social Interactions](http://arxiv.org/abs/2611.08334v1)
  <details><summary>📄 Abstract</summary>
  Much of human culture is tacit and is typically learned through situated social interaction. As LLMs are deployed as interactive agents across diverse communities, assessing their cultural competence demands moving beyond existing question-answering approaches, shifting from what they know to how they adapt. In this work, we broaden the scope of cultural adaptation in NLP by investigating whether LLMs can adapt through repeated interactions via a sandbox environment. By reframing cultural adapta...
  </details>

- **2026-11-05** — Xiaojun Wu, Cehao Yang, Xuhui Jiang et al. — [Terminal-style Mathematical Modeling Bench: The First Agentic and Verifiable Benchmark for Mathematical Modeling](http://arxiv.org/abs/2611.08237v1)
  <details><summary>📄 Abstract</summary>
  Mathematical modeling turns an open-ended real-world problem into assumptions, a model, a solution, and a defended recommendation, and its answers matter only if they are both close to a credible reference and physically feasible; existing benchmarks either score solver fragments or grade reports with an LLM judge, leaving those numbers unchecked. We introduce TB-MathModel (the Terminal-style Mathematical Modeling Bench), the first benchmark to make complete contest-style modeling problems agent...
  </details>

- **2026-11-05** — Gizem Mert, Szymon Płotka, Pedro R. A. S. Bassi et al. — [Multimodal Hierarchical Mixture-of-Experts for 3D Medical Vision-Language Modeling](http://arxiv.org/abs/2611.08185v1)
  <details><summary>📄 Abstract</summary>
  Medical 3D scans and reports are inherently hierarchical, with diagnostic cues concentrated in specific anatomical regions across multiple levels of organization. Yet, most medical vision-language models ignore this structure and fail to focus on clinically relevant anatomy. We introduce MedHiVE, which combines hierarchical vision-language Soft Mixture-of-Experts (SMoE) with contrastive learning to jointly model fine-grained anatomy and global scan context. To our knowledge, MedHiVE is the first...
  </details>

- **2026-11-05** — Romain Hermary, Nesryne Mejri, Djamila Aouada — [Evaluating Language Model Features for Zero-Shot Time-Series Anomaly Detection Under Isolation Assumption](http://arxiv.org/abs/2611.07720v1)
  <details><summary>📄 Abstract</summary>
  Time-Series Anomaly Detection (TSAD) is a fundamentally challenging task: it is unsupervised, requires high local precision capabilities, and suffers from limited labelled data. Recent work has explored adapting Large Language Models (LLMs) to time-series via cross-modal transfer. However, existing approaches are poorly suited to Multivariate TSAD (MTSAD), as tokenisation often obscures fine-grained temporal and variables structures, and most methods optimise auxiliary objectives such as forecas...
  </details>

- **2026-11-05** — Laurenz Ruzicka, Roman Pflugfelder, Daniel Cremers — [FlyingDrones: A Dataset and Benchmark for Optical Flow Estimation from UAV motion](http://arxiv.org/abs/2611.07705v1)
  <details><summary>📄 Abstract</summary>
  Optical flow is an important cue for drone analysis in aerial surveillance, airspace monitoring, and long-range target tracking, where motion remains informative when appearance is weak. Estimating the motion of small Unmanned Aerial Vehicles, however, is difficult because distant targets occupy few pixels, have low contrast, and move against complex dynamic backgrounds. Standard optical-flow benchmarks emphasize large, object-centric motions and therefore do not characterize distant aerial targ...
  </details>

- **2026-11-05** — Pierre Onghena, Santiago Velasco-Forero, Beatriz Marcotegui — [GEKey: Learning Geodesic Eccentric 3D Keypoints via Self-Supervision](http://arxiv.org/abs/2611.07677v1)
  <details><summary>📄 Abstract</summary>
  Point clouds represent 3D object geometry as sets of spatial coordinates. A fundamental task in their analysis is keypoint detection, i.e., identifying a sparse subset of points that captures the most salient features. While supervised methods rely on manual annotations, unsupervised approaches leverage intrinsic geometric properties to localize keypoints without human input. We introduce GEKey, a self-supervised framework that uses the geodesic eccentricity transform, an SE(3)-invariant geometr...
  </details>

- **2026-11-05** — Yuefeng Xu, Jun Yu — [When Does Blockwise Additivity Break? Diagnosing and Repairing the Additive Assumption in Distillation-Based Architecture Search](http://arxiv.org/abs/2611.07487v1)
  <details><summary>📄 Abstract</summary>
  Blockwise distillation methods for architecture search, such as DNA, DONNA, LANA and Puzzle, score each candidate replacement block in isolation and assemble a child network by minimizing the sum of per-block scores. We test this additive assumption on DeiT-S and DeiT-B with seven replacement blocks per layer, seven block-latency budgets from 70% to 40%, three fine-tuning seeds and paired bootstrap confidence intervals. (i) At mild compression the additive integer linear program (ILP) is close t...
  </details>

- **2026-11-05** — Hongyu She, Yiling He, Mengda Xie et al. — [MEvince: Knowledge-Constrained LLM Reasoning for Technique Identification from Malware Reports](http://arxiv.org/abs/2611.07486v1)
  <details><summary>📄 Abstract</summary>
  Mapping behavioral intelligence in malware analysis reports to ATT&CK techniques supports threat analysis and defense, but reliable identification remains challenging. Supporting evidence is often scattered across long, heterogeneous reports, while closely related techniques share behavioral cues and differ only in subtle but decisive details. While large language models (LLMs) can use external knowledge to interpret reports, they may assign techniques based on plausible associations rather than...
  </details>

- **2026-11-05** — Raúl Boix-Aldeguer, Manuel Benavent-Lledo, David Ortiz-Perez et al. — [Egocentric Action Recognition with Objects and Vision-Language Affordances](http://arxiv.org/abs/2611.07673v1)
  <details><summary>📄 Abstract</summary>
  Action recognition, and more specifically egocentric action recognition, is a core task in computer vision, with applications such as monitoring the daily life activities of elderly people and task assistance. Recent methods rely on visual modalities such as RGB video or depth. However, in egocentric video, an action is largely defined by its objects, which these methods rarely model. We propose a method that combines a frozen SlowFast video expert with an attention-based object expert by late f...
  </details>

- **2026-11-05** — Tao Wang — [Fault-Guided Cross-Layer Prediction for Unsupervised Anomaly Detection](http://arxiv.org/abs/2611.08140v1)
  <details><summary>📄 Abstract</summary>
  Feature reconstruction is widely used for unsupervised industrial anomaly detection in the single-class setting, where only normal images from one product category are available for training. We propose a single-class detector that asks what information one block can pass to another. We treat the depth of a frozen vision transformer as a sequence of discrete transitions. A directed predictor learns a block-to-block hidden-state transition pointwise over tokens. Adjacent-layer cosine similarity e...
  </details>

- **2026-11-05** — Hyojun Yi, Geunyoung Kim, Hogeon Seo et al. — [How Far Can Untrained Neural Networks Go in Anomaly Detection? From Tables to Pixels](http://arxiv.org/abs/2611.08136v1)
  <details><summary>📄 Abstract</summary>
  Anomaly detection (AD) is often framed as a representation-learning problem, where strong performance is expected to require learned features or AD-specific optimization. However, this view can overlook the intrinsic separability of anomalies from normal references, even in the absence of learned representations. We therefore investigate how far untrained neural networks can go in anomaly detection. To this end, we propose PRISM, a framework combining fixed random nonlinear features with normal-...
  </details>

- **2026-11-05** — Zhengyu Fang, Liang Wang, Yingtong Dou et al. — [PersonaAgent: Retrieval-Augmented Transaction Anomaly Scoring with Refreshable Multi-Entity Persona Memory](http://arxiv.org/abs/2611.08094v1)
  <details><summary>📄 Abstract</summary>
  In large-scale payment networks, entities (card, merchant, etc.) and their interactions play a key role in transaction anomaly detection. However, transaction patterns between different entities usually change more frequently than the production model refresh schedule. Meanwhile, entity embedding tables suffer from high-cardinality and sparse interaction issues. To resolve the above challenges, we present PersonaAgent, an agentic transaction anomaly detection framework which represents the lates...
  </details>

- **2026-11-05** — S-Wei Chen, Siangyu Yang, Yi-Chen Jan et al. — [Spatiotemporal Dynamics-Aware Industrial Anomaly Detection and Reasoning](http://arxiv.org/abs/2611.08080v1)
  <details><summary>📄 Abstract</summary>
  Industrial Anomaly Detection (IAD) is a long-established problem that aims to detect defects in industrial products during manufacturing for quality control. Most existing studies focus on static visual patterns as the basis for detection. However, in real manufacturing environments, many anomalies are dynamics-based, such as irregular movements that cannot be perceived from static cues alone. We observe that even recent Multimodal Large Language Model (MLLM)-based approaches fall short in ident...
  </details>

- **2026-11-04** — Yang Liu, Ran Zou, Wanrong Zhu — [Source-balanced Capped Fisher: Bounded Evidence Aggregation for User Inference in Language Models](http://arxiv.org/abs/2611.07228v1)
  <details><summary>📄 Abstract</summary>
  User inference asks whether a source contributed documents to a language-model update, even when the auditor observes only fresh documents from that source. Document-level scores can provide evidence of participation, but combining this evidence is challenging: documents differ in baseline predictability and in how strongly they reflect information learned from other documents of the same source. We propose source-balanced capped Fisher (SCF), an aggregation method that uses known nonparticipati...
  </details>

- **2026-11-04** — Hanzhi Zhang, Qiao Zhang, Qinglei Cao et al. — [TileQuant: Tile as the Precision-Allocation Unit for LLM Mixed-Precision Post-Training Quantization](http://arxiv.org/abs/2611.07217v1)
  <details><summary>📄 Abstract</summary>
  Post-training quantization (PTQ) reduces large language model (LLM) deployment costs, but preserving quality requires accounting for uneven weight sensitivity. Uniform PTQ uses one weight bit-width, importance-aware PTQ adjusts scales or reconstructs weights within that width, and column-wise mixed precision retains selected columns at higher precision. However, sensitivity varies within columns, so whole-column retention also protects less sensitive weights, while runtime outlier detection adds...
  </details>

- **2026-11-04** — Yunru Zheng, Wun Ting Chan, Sampras Dsouza et al. — [Scalable Bayesian Gaussian Process Classification for Cancer Histopathology: Calibrated Uncertainty Under Distribution Shift](http://arxiv.org/abs/2611.07127v1)
  <details><summary>📄 Abstract</summary>
  Reliable uncertainty quantification is essential for clinical deployment of cancer diagnosis models, yet neural networks and variational Gaussian process methods can produce overconfident predictions, particularly under the distribution shifts that arise when models trained at one hospital are applied at another. We present a scalable Bayesian Gaussian Process Classification (GPC) framework that operates on frozen pathology foundation model embeddings (Phikon) and combines accelerated Randomly P...
  </details>

- **2026-11-04** — Wenyi Xu, Renzhe Zhou, Songyang Li et al. — [WISE: An Agentic Framework for Whole-page Multimodal Search Experience Attribution](http://arxiv.org/abs/2611.06777v2)
  <details><summary>📄 Abstract</summary>
  Algorithm-driven services, including search, recommendation, and advertising, rely on multi-stage model pipelines. While research prioritizes model optimization, post-deployment monitoring focuses on operational reliability. Yet operationally healthy systems may still produce poor-quality results, exposing a gap in existing evaluation and monitoring practices. However, a systematic problem formulation and benchmark for this task remain lacking. To bridge this gap, we formulate System Quality Dia...
  </details>

- **2026-11-04** — Yichiet Aun, Mohammed A. Alhartomi, Jing Jie Tan et al. — [Signed, Sealed, Leaked: Trust Beyond Signature for MCP Toolchains](http://arxiv.org/abs/2611.06585v1)
  <details><summary>📄 Abstract</summary>
  AI agents rely on third-party tools, such as Model Context Protocol (MCP) servers, whose publishers can be authenticated and whose execution can be restricted by runtime security policies. Yet authenticity does not guarantee benign behaviour: a legitimately signed tool may perform its advertised function while concealing malicious code that leaks confidential information. We demonstrate this trust failure with a signed MCP tool that embeds sensitive data in requests to a policy-allowed destinati...
  </details>

- **2026-11-04** — Fei Lin, Tengchao Zhang, Ziyang Gong et al. — [BEAKER: An Expert-Curated Benchmark for Embodied Brains in Self-Driving Chemical Laboratories](http://arxiv.org/abs/2611.06911v1)
  <details><summary>📄 Abstract</summary>
  Self-Driving Chemical Laboratories (SDCLs) are moving chemical experimentation toward embodied automation, where machines must perceive laboratory scenes, reason about experimental states, and act under physical, procedural, and safety constraints. Although Multimodal Large Language Models (MLLMs) are increasingly considered as embodied brains for such systems, existing laboratory benchmarks mainly focus on safety, anomaly detection, or general scientific understanding, leaving their execution-o...
  </details>

- **2026-11-04** — Austin C. Kozlowski, Avital Mintz, Madison Lee — [Persona Perspectives: Adopting Viewpoints Reorganizes Representations in LLMs](http://arxiv.org/abs/2611.06848v1)
  <details><summary>📄 Abstract</summary>
  Common methods for monitoring features in large language models (LLMs) such as linear probes and sparse autoencoders (SAEs) assume that features maintain a consistent representation across contexts. LLMs, however, can flexibly adopt different perspectives or "personas" that suggest different underlying systems of conceptual relations. In this paper, we examine whether prompting an LLM to adopt a persona alters the representational geometry of the model's latent space. We extract representations ...
  </details>

- **2026-11-04** — Nil-Jana Akpinar, Eugenia Kim, Natalie Isak et al. — [Measuring Risk, Not Harm: Detecting Psychological Harm Risk Factors in LLM Conversations](http://arxiv.org/abs/2611.06806v1)
  <details><summary>📄 Abstract</summary>
  Psychological harms from interactions with large language models cannot be monitored directly because they may emerge over repeated interactions and depend strongly on subjective individual user context. We propose measuring risk, not harm: detecting observable AI behaviors that constitute risk factors for psychological harm at the AI response level and aggregating these signals to support longitudinal monitoring. We operationalize eight such behaviors and construct a synthetic multi-label corpu...
  </details>

- **2026-11-04** — Chijin Zhou, Quan Zhang — [Rethinking Access Control for AI Agents: Recent Advances and Open Challenges](http://arxiv.org/abs/2611.06764v1)
  <details><summary>📄 Abstract</summary>
  Large language model agents access data, invoke tools, and act on users' behalf. Keeping these actions within authorized bounds is challenging because agents choose their own execution paths while permissions and operating conditions may change. This paper surveys recent advances in agent access control across four areas: policy specification and derivation, identity and delegation, action and resource enforcement, and information flow control. We compare their control objects, enforcement bound...
  </details>

- **2026-11-04** — Shubhabrata Mukherjee, Jeffrey Donatelli, Daniela Ushizima — [Route First, See Later: Enabling Vision Agents to Reason Scientifically by Separating Routing Policy from Action Spaces](http://arxiv.org/abs/2611.06760v1)
  <details><summary>📄 Abstract</summary>
  Scientific image-analysis workflows require agents to select among diverse capabilities like description, detection, counting, and segmentation. Current multi-tool architectures conflate intent interpretation with visual execution, masking whether a failure arises from flawed reasoning (misrouting) or failed perception (invalid tool execution). This lack of auditability renders agents unreliable for high-stakes scientific automation. We introduce ZETA, an extensible architecture that operational...
  </details>

- **2026-11-04** — Zhonghao Zhan, Javad Forough, Yefan Zhang et al. — [Airlock: Bounding the Multi-Agent Blast Radius via Selective Online Containment](http://arxiv.org/abs/2611.06727v1)
  <details><summary>📄 Abstract</summary>
  When multi-agent systems act on the external world, a single agent's faulty output can spread across tasks before detection, creating a system-wide blast radius. Single-agent guardrails are confined to individual harnesses, while existing multi-agent controls either cancel only the faulty source and miss downstream consumers or halt and roll back the entire workflow at the cost of healthy work. We present Airlock, a multi-agent runtime and guardrail for selective post-alert fault containment. It...
  </details>

- **2026-11-04** — Zohreh Abbasi Liasi, Batoul Hammoud, Anas Madkoor et al. — [Reasoning over Non-Parametric Memory in Multilingual LLMs: A Cognitive-Based Analysis of Relational Knowledge](http://arxiv.org/abs/2611.06715v1)
  <details><summary>📄 Abstract</summary>
  Retrieval-augmented generation (RAG) assumes that language models can reason over relations stated in their context rather than fall back on associations memorized during pretraining. We study this evidence-conditioned relational reasoning in isolation, with the facts supplied directly in the prompt rather than retrieved. \textsc{Rel-Bloom} is a controlled multilingual diagnostic of 450 multiple-choice questions built from 30 Wikidata relations; the same source relations are instantiated at five...
  </details>

- **2026-11-04** — Henry Zhang — [Hard to Fool: A Bounded LLM Research Loop for Quantitative Finance, and What Two Dozen Campaigns Found](http://arxiv.org/abs/2611.06607v1)
  <details><summary>📄 Abstract</summary>
  Agentic research loops that let a language model propose a change, run a fixed experiment and keep whatever improves the metric work well in machine learning. In trading research the same loop is a machine for producing false discoveries: a backtest that "improves the metric" is, by default, overfit, look-ahead, a multiple-comparisons artifact, cost-free, or market drift wearing a strategy. We describe Autonomous Quant Researcher, an open-source loop built on the opposite premise: the model prop...
  </details>

- **2026-11-04** — Chenyang Le, Pei Zhang, Yuxiang Chen et al. — [CRESiST: Self-Enhancing Explorative Policy Learning for Simultaneous Speech Translation](http://arxiv.org/abs/2611.06501v1)
  <details><summary>📄 Abstract</summary>
  Simultaneous Speech Translation (SimulST) requires balancing translation quality and latency. While Large Language Models (LLMs) excel in offline translation, current LLM-based SimulST systems predominantly rely on prefix-incremental generation. This paradigm suffers from redundant Key-Value cache recomputation and necessitates external Voice Activity Detection to process unbounded streams. To overcome these bottlenecks, we propose an end-to-end interleaved read-write framework built upon an omn...
  </details>

- **2026-11-04** — Jonguk Cheong, Myungbin Hwang, Eulgyu Kim et al. — [KVGuard: A KV Cache Safety Checker for LLM Serving Systems](http://arxiv.org/abs/2611.06138v1)
  <details><summary>📄 Abstract</summary>
  Modern LLM serving systems manage the KV cache through PagedAttention, a custom GPU allocator that partitions a single CUDA-allocated region into fixed-size physical blocks and maps each request to those blocks through a CPU-built block table. This block-based design exposes a previously unstudied class of memory safety bugs in the KV cache, including double-free, use-after-free, out-of-bounds access, uninitialized read, and permission violation, which silently corrupt outputs or break request i...
  </details>

- **2026-11-04** — Chunxiao Wu, Huixin Huang, Jialei Pan et al. — [XuanJian-DINOSAR: A SAR Foundation Model Based on Global and Local Semantic Consistency](http://arxiv.org/abs/2611.06105v1)
  <details><summary>📄 Abstract</summary>
  Self-supervised pre-training on synthetic aperture radar (SAR) imagery enables transferable representations, but the optical-SAR domain gap and speckle perturbations limit representation stability. Most SAR foundation models use masked image modeling (MIM) through pixel reconstruction or structural feature prediction, which is sensitive to speckle or relies on predefined operators. Joint modeling of cross-view semantics and perturbation stability at corresponding spatial locations remains undere...
  </details>

- **2026-11-04** — Danwen Chen, Guangba Yu, Pengfei Chen — [SWEOps-Bench: Evaluating Agents for End-to-End Resolution of Software-Induced Cloud Incidents](http://arxiv.org/abs/2611.06099v1)
  <details><summary>📄 Abstract</summary>
  As autonomous agents advance, the traditional boundary between software development and cloud operations gradually blurs, increasing the need for integrated incident detection, localization, and remediation. Existing benchmarks evaluate isolated diagnostic queries or repository-level program repair, failing to test continuous incident resolution across operational clusters and source repositories. We introduce SWEOps-Bench, an interactive benchmark comprising 55 reproducible incident tasks deriv...
  </details>

- **2026-11-04** — Ashutosh Dayal, Mallika Garg, Debashis Sen — [Intra-Architecture Source Attribution for Stable Diffusion: A New Task with Benchmark Dataset and Baseline](http://arxiv.org/abs/2611.06000v1)
  <details><summary>📄 Abstract</summary>
  Designing systems that attribute a generated image to its source model has lately become a major area of AI research. Most existing datasets and systems related to image source attribution are targeted towards the detection of architectural signatures of the source models. Distinct from this, focusing on stable diffusion, we introduce a novel task, IntrAA-SD, Intra-Architecture source Attribution for Stable Diffusion, where the source models to be differentiated share the same architectural back...
  </details>

- **2026-11-04** — Junnuo Wang, Weihan Xu, Hao-Wen Dong — [Clips2Story: Training-Free Video Storyboarding and Editing Using Multimodal Retrieval-Embedded Generation](http://arxiv.org/abs/2611.05992v1)
  <details><summary>📄 Abstract</summary>
  Video editors often work with large collections of fragmented footage and must select and organize relevant clips into a coherent story. However, many existing video editing and summarization methods assume a temporally ordered source video and aim to preserve its original narrative and temporal structure. In this paper, we introduce Clips2Story, a training-free, LLM-based pipeline that enables users to create keyword-specified short videos from a pool of video clips. Given a pool of clips and a...
  </details>

- **2026-11-04** — Yusheng Dai, Vladimir Iashin, Kangdi Wang et al. — [LiveFoley: Dynamic Real-Time Video-to-Audio Generation for Immersive Interactive Worlds](http://arxiv.org/abs/2611.05988v1)
  <details><summary>📄 Abstract</summary>
  Streaming video-to-audio (V2A) generation is essential for immersive interactive applications. However, real-time constraints leave existing streaming V2A methods far behind offline models: (1) visual frontends shrink their receptive fields to cut look-ahead latency, severely degrading audio-visual alignment; (2) causal autoregressive diffusion backends denoise each audio patch in isolation, impairing audio quality. To this end, we present LiveFoley, a streaming causal autoregressive diffusion a...
  </details>

- **2026-11-04** — Shumpei Shiina, Haruka Takahashi, Kento Sasaki et al. — [Enforcing Accountable Disclosure in Confidential AI](http://arxiv.org/abs/2611.05971v1)
  <details><summary>📄 Abstract</summary>
  Advances in CPU and GPU confidential computing enable confidential AI, allowing LLMs to process user prompts without exposing them to service providers or infrastructure operators. However, AI agents often need to send prompt-derived information to external services, and providers may also require limited disclosure for safety monitoring and failure diagnosis. We propose CORDE, a system for confidential virtual machines (CVMs) designed to satisfy the principle of Confine or Declare: user-derived...
  </details>

- **2026-11-04** — Anh Minh Nguyen, Tuan Dat Tran, Alzubair Hassan et al. — [A Hybrid Approach for Automated Security Pattern Recovery](http://arxiv.org/abs/2611.05823v1)
  <details><summary>📄 Abstract</summary>
  Security-by-design emphasises integrating security into software design and development. Security pattern catalogues operationalise this principle by prescribing reusable architectural solutions to recurring security problems. However, recovering their implementations from source code remains challenging because security patterns are abstract, span multiple components, and admit many valid implementations. We present SecPatRec, a hybrid approach for automated security pattern recovery from sourc...
  </details>

- **2026-11-04** — Wenyi Xu, Renzhe Zhou, Songyang Li et al. — [WISE: An Agentic Framework for Whole-page Multimodal Search Experience Attribution](http://arxiv.org/abs/2611.06777v1)
  <details><summary>📄 Abstract</summary>
  Algorithm-driven services, including search, recommendation, and advertising, rely on multi-stage model pipelines. While research prioritizes model optimization, post-deployment monitoring focuses on operational reliability. Yet operationally healthy systems may still produce poor-quality results, exposing a gap in existing evaluation and monitoring practices. However, a systematic problem formulation and benchmark for this task remain lacking. To bridge this gap, we formulate System Quality Dia...
  </details>

- **2026-11-04** — Jiuwu Hao, Yuting Wan, Liguo Sun et al. — [Uncertainty-Driven Efficient Communication for UAV-Based Collaborative Perception](http://arxiv.org/abs/2611.06635v1)
  <details><summary>📄 Abstract</summary>
  Unmanned aerial vehicle (UAV)-based collaborative perception enables multiple agents to share complementary perceptual information, overcoming limitations such as occlusion and limited sensing range. Communication efficiency is a critical bottleneck, as UAVs operate under stringent bandwidth and computational constraints. However, existing spatial selection methods focus predominantly on foreground regions to reduce missed detections, neglecting perceptually ambiguous regions and leaving false d...
  </details>

- **2026-11-04** — Jingwen Yu, Pengyu Wang, Jin Wu et al. — [UniLoop: Unified Loop Closure Detection from Retrieval to Geometric Verification and Relative Pose Estimation](http://arxiv.org/abs/2611.06378v1)
  <details><summary>📄 Abstract</summary>
  Loop closure detection conventionally cascades separate models for global retrieval, geometric verification, and relative pose estimation, leading to redundant computation and disconnected visual representations. We propose UniLoop, a unified framework that reuses the hierarchical representations of the pretrained geometric foundation model throughout this pipeline. A shared image encoder produces features for compact global descriptors; the same features are passed to the cross-view decoder for...
  </details>

- **2026-11-03** — Douglas Guilbeault, Bhargav Srinivasa Desikan — [The Male Abstraction Bias in Internet Culture and Large Language Models](http://arxiv.org/abs/2611.05730v2)
  <details><summary>📄 Abstract</summary>
  Conceptual abstraction and gender are two equally central aspects of the human mind, yet they have traditionally been studied in isolation from one another, as though they were fundamentally separate. Here, we find gender and abstraction are systematically linked throughout the space of concepts spanning single (N = 40,000) and multi-word expressions (N = 67,000): across billions of words and millions of images on the internet --- and across numerous measurement techniques, including human and A...
  </details>

- **2026-11-03** — Zekai Li, Zhenke Liu, Yonghao Li et al. — [LIBRA: Programmatic Induction of Executable Tool Libraries](http://arxiv.org/abs/2611.05445v2)
  <details><summary>📄 Abstract</summary>
  Large language model agents increasingly retrieve tools from large catalogs, yet most retrievers rank each tool independently by request similarity. For multi tool tasks, this recovers the goal matching tool while omitting prerequisite tools required by the workflow. We introduce LIBRA, a framework for Library Induction by Runtime Assembly that turns a flat tool catalog into an executable tool library. An LLM proposes per tool contracts of candidate invocations, reusable outputs and state change...
  </details>

- **2026-11-03** — Zekai Li, Zhenke Liu, Yonghao Li et al. — [LIBRA: Programmatic Induction of Executable Tool Libraries](http://arxiv.org/abs/2611.05445v1)
  <details><summary>📄 Abstract</summary>
  Large language model agents increasingly retrieve tools from large catalogs, yet most retrievers rank each tool independently by request similarity. For multi tool tasks, this recovers the goal matching tool while omitting prerequisite tools required by the workflow.We introduce LIBRA, a framework for Library Induction by Runtime Assembly that turns a flat tool catalog into an executable tool library. An LLM proposes per tool contracts of candidate invocations, reusable outputs and state changes...
  </details>

- **2026-11-03** — Sarah Montgomery-Taylor, Hamsa Subramaniam, Rob Brisk et al. — [Towards Multi-Method Evaluation of AI in Health: Integrating Benchmarks, Autoraters, and Expert Evaluation](http://arxiv.org/abs/2611.05127v2)
  <details><summary>📄 Abstract</summary>
  General-purpose generative AI (GenAI) models are being rapidly adopted in healthcare, but they are challenging to assess with traditional evaluation frameworks. These conceptual, methodological, and practical challenges parallel decades of work in evaluating clinician and health system quality and safety. We describe the adaptation of methods from several fields, combined with emerging technical approaches, into a structured, multi-method evaluation framework designed to give well-rounded assess...
  </details>


### 📂 alignment
*对齐与安全约束 / Alignment & Safety Constraints* — 40 papers

- **2026-11-06** — Anthony Rhodes, Gadi Singer — [BMMS: Policy-Conditioned Measurement of Behavioral Compliance in Language Models](http://arxiv.org/abs/2611.09147v1)
  <details><summary>📄 Abstract</summary>
  Behavioral evaluation of language models fixes its dimensions in advance: hallucination, sycophancy, toxicity, over-refusal. An operator in a regulated industry needs a different question answered: does a system do what a particular rulebook requires? We introduce the Behavioral Misalignment Metric Suite (BMMS), which measures policy-conditioned misalignment by taking a policy corpus as an argument and returning a compliance profile over it, for any published policy and any system that answers i...
  </details>

- **2026-11-06** — Nicolò Zava, Angel Franco-Alvarez, Samy Blusseau et al. — [Multiscale Closing Index (MCI) for measuring structural similarity between 2D point sets](http://arxiv.org/abs/2611.09745v1)
  <details><summary>📄 Abstract</summary>
  We introduce Multi-scale Closing Index (MCI), a new dissimilarity measure for evaluating the alignment of two 2D point sets. MCI is bounded between 0 and 1 and is based on multiscale mathematical morphology operations, with smaller values indicating greater structural agreement. The measure was motivated by the need to assess the quality of registration between point sets representing cell populations in biological images. To evaluate its behaviour under controlled conditions, we generated synth...
  </details>

- **2026-11-06** — Shira Ifergane, Roy Amoyal, Shahar Benishay et al. — [Video Stitching from Multiple Moving Cameras](http://arxiv.org/abs/2611.09570v1)
  <details><summary>📄 Abstract</summary>
  We address geometric video alignment for the same scene captured by multiple freely moving cameras. Existing methods, which are based on image stitching or video stabilization, are typically limited to two cameras or must assume the restrictive setting of a fixed linear ordering of the cameras. We propose MViS, a lightweight test-time optimization framework for joint multi-view alignment with temporal consistency. MViS uses a spatial-transformer-inspired net to jointly process frames from all vi...
  </details>

- **2026-11-06** — Nikhil Verma, Dingxian Wang, Mohammad Reza Rezaei et al. — [Alignment by Confident Debate: Preference Learning from Multi-Agent Debate](http://arxiv.org/abs/2611.09568v1)
  <details><summary>📄 Abstract</summary>
  Post-training language models for reasoning typically rely on gold answers, task-specific verifiers, or learned reward models, limiting scalability when such signals are scarce. Multi-agent debate offers a self-supervised alternative, but converting debate into reliable training supervision remains challenging: majority voting weights agreeing responses equally, lacks a principled tie-breaking rule, and is ill-defined for open-ended tasks without a canonical answer; likelihood-based scoring can ...
  </details>

- **2026-11-06** — Xiaomeng Guo, Fasheng Xu, Xiaoli Zhang — [Artificial Shoppers and Attention Competition](http://arxiv.org/abs/2611.09399v1)
  <details><summary>📄 Abstract</summary>
  We study how AI shopping interfaces affect price competition, platform profit, and consumer welfare. A platform hosts two of three products of different quality. Without AI, consumers compare the hosted pair under salience distortion and overweight whichever attribute, price or quality, stands out. Under assistance, an AI assistant recommends the two products with the highest true utility, leaving consumers to make the same distorted comparison. Under delegation, an AI agent selects the best pro...
  </details>

- **2026-11-06** — Barbara Gendron, Gaël Guibon, Mathieu D'aquin — [Ontology-Driven Control of Conversational Agents with a Use-Case for Job Interview Practice](http://arxiv.org/abs/2611.09282v1)
  <details><summary>📄 Abstract</summary>
  Large Language Models (LLMs) have been widely used as conversational agents in both domain-specific and open-domain situations. In domain-specific context, it is often necessary to adapt those LLMs to obtain conversations with desired characteristics, whether those apply at the level of each response (e.g. for tone or style) or more globally (i.e. at the level of a conversational strategy). Such adaptations are, however, generally realized in an ad hoc way, through specific, non-reusable, and no...
  </details>

- **2026-11-06** — Iñigo Parra — [Language, Not Code Abstraction: Natural-language Training Shapes Brain-aligned Geometry](http://arxiv.org/abs/2611.09027v1)
  <details><summary>📄 Abstract</summary>
  Code-trained language models produce positive brain scores, which raises the question of whether abstract structure learned from programming languages can substitute for natural-language training. We trained 25 GPT-2-small models on TinyStories, Python, C functions, x86-64 assembly, and the corresponding machine code, and scored them using a shared tokenizer and encoding procedure against matched random-weight models. On Pereira-243 and Tuckute2024, TinyStories exceeds the mean of the four code ...
  </details>

- **2026-11-05** — Jihao Zhao, Ding Chen, Yanfang Chen et al. — [RouteAlign: Aligning Task Requirements with Model Profiles for LLM Service Selection](http://arxiv.org/abs/2611.08162v1)
  <details><summary>📄 Abstract</summary>
  LLM service selection requires performance evidence that reflects the demands of the current task. Aggregate scores obscure differences in capability and difficulty, while semantically related examples can involve different combinations of skills. We present RouteAlign, which uses task requirements to structure both the measurement of model performance and the selection of services. Task requirements describe capability demand and difficulty, enabling alignment with corresponding model performan...
  </details>

- **2026-11-05** — Jiahao Cui, Jiaye Li, Wenhao Zhang et al. — [WAM-Sim0.1: World Anchored Memory Meets Online RL for Consistent and Realistic Driving Simulation](http://arxiv.org/abs/2611.07939v1)
  <details><summary>📄 Abstract</summary>
  Autoregressive driving world models systematically suffer from structural drift, identity drift, and quality decay over long rollout horizons due to transient conditioning signals that lack persistent state. We present WAM-Sim, a driving world model anchored by a persistent hierarchical memory and optimized via online flow-matching RL. WAM-Sim structures persistent context across three temporal and semantic scales: pose-aligned structural tokens encoding persistent road topology, read-only scene...
  </details>

- **2026-11-05** — Zeyu Liu, Xuanzhi Feng, Haoran Xu et al. — [Foresee to Trade: Forecast-Augmented Policy Optimization for Portfolio Management](http://arxiv.org/abs/2611.07750v1)
  <details><summary>📄 Abstract</summary>
  Online investment services must translate asset opportunities into investment outcomes for users' accounts, yet the same market opportunity can warrant different account actions. We study how supervision from future asset opportunities can strengthen account-level trading decisions and propose Forecast-Augmented Relative Policy Optimization (FRPO). FRPO separately supervises asset opportunities and account decisions through a jointly learned representation: a Financial State Head (FSH) learns fu...
  </details>

- **2026-11-05** — Jinkun Cao — [Fast and Accurate Hand Estimation in Pixels, Interaction and World Space](http://arxiv.org/abs/2611.07711v1)
  <details><summary>📄 Abstract</summary>
  Monocular hand mesh estimators commonly predict rig parameters and project the mesh to obtain 2D keypoints. We find that directly predicted 3D joints agree better with 2D predictions, and fitting a mesh to predicted points reduces mesh error. We present FAH (Fast and Accurate Hand Estimation), a family of models built on SAM 3D Body's hand branch through fine-tuning and feature distillation. The models predict corresponding 2D and 3D joints and surface points, fit MANO or MHR-Hand, and optionall...
  </details>

- **2026-11-05** — Tze Ho Elden Tse, Jizong Peng, Richard Chen et al. — [AffineGS: Unlocking Accurate Geometry in 3DGS via Spatially Varying Affine Rectification](http://arxiv.org/abs/2611.07709v1)
  <details><summary>📄 Abstract</summary>
  3D Gaussian Splatting (3DGS) has become the leading approach for photorealistic novel view synthesis, yet its geometric accuracy lags behind its visual quality. Existing depth-guided methods attempt to resolve this by regularizing the optimization with monocular depth priors, typically using a single global scale-and-shift alignment. Crucially, we discover a fundamental flaw in this assumption: modern monocular depth networks systematically exhibit region-dependent, piecewise-linear distortions....
  </details>

- **2026-11-05** — Weiqin Chen, Xinmeng Huang, Dongsheng Ding et al. — [Provable Zeroth-Order Safe Exploration for Reinforcement Learning from Human Feedback](http://arxiv.org/abs/2611.07561v1)
  <details><summary>📄 Abstract</summary>
  Safe reinforcement learning from human feedback (Safe-RLHF) seeks to improve helpfulness while satisfying harmlessness constraints. Existing primal-dual approaches can converge to feasible policies but do not prevent constraint violations during training. We study a stronger requirement, safe exploration for RLHF, under which every policy executed during training, including auxiliary exploration policies, remains feasible. We propose Zeroth-Order Log-Barrier Policy Gradient (ZO-LBPG), a reward-m...
  </details>

- **2026-11-05** — Viraj Shah, Ashwini Pokle, Peyman Milanfar et al. — [OptIMerge: Optimization-Based Merging of Diffusion Models](http://arxiv.org/abs/2611.07543v1)
  <details><summary>📄 Abstract</summary>
  The arithmetic merging of weights from multiple task-specific models fine-tuned from a shared base model, commonly known as model souping, has emerged as a popular strategy for multi-task learning without the computational overhead of joint retraining. However, naive scalar weight averaging frequently leads to severe performance degradation when the constituent models learn structurally divergent feature representations, leading to destructive parameter interference. We study this problem in a l...
  </details>

- **2026-11-05** — Alon Jacobson, Qian Xie, Peter I. Frazier — [Latency-Aware Adaptive Best-of-$N$](http://arxiv.org/abs/2611.07453v1)
  <details><summary>📄 Abstract</summary>
  Test-time compute (TTC) improves language model responses by spending additional computation at inference time, and the right amount of compute depends on the prompt. Adaptive TTC methods allocate compute based on signals of response quality such as observed rewards, often by stopping once the signal exceeds a fixed threshold, and generally measure cost by the number of generations or tokens. But in online serving, latency is also a cost: it grows with server load, so a method using a fixed thre...
  </details>

- **2026-11-05** — Shengbo Wang, Mingwei Liu, Yuwen Chen et al. — [Req2Rust: A Requirements-Guided Agent Harness for Project-Level C++-to-Rust Migration](http://arxiv.org/abs/2611.07442v1)
  <details><summary>📄 Abstract</summary>
  Memory-safety concerns make Rust an attractive target for modernizing legacy C/C++ systems, yet project-level C++ migration must balance semantic fidelity with Rust-oriented reconstruction. Source-structure-preserving migration can track low-level behavior, but it can also carry source-language organization, unsafe idioms, and project assumptions into Rust. Direct agent-based translation gives the model more freedom to construct a Rust project, but semantic coverage depends on the model identify...
  </details>

- **2026-11-05** — Yi He, Zhengxi Yu, Feilin Han et al. — [Designing with Cinematic Language: An Intent-Driven Approach to Human-AI Video Clip Co-Creation](http://arxiv.org/abs/2611.07377v1)
  <details><summary>📄 Abstract</summary>
  Generative video models have made video creation more accessible, yet creators still struggle to translate high-level narrative intentions into coherent cinematic expressions. Existing systems primarily rely on prompt refinement or expose isolated camera controls, leaving a gap between what to express and how to film it. We present CineAssist, a human-AI co-creation system that treats cinematic language as an interactive design medium connecting creative intentions with executable video controls...
  </details>

- **2026-11-05** — Yiling Chen, Shi Feng, Grant Schoenebeck et al. — [Information Elicitation by Ordinal Agreement](http://arxiv.org/abs/2611.08366v1)
  <details><summary>📄 Abstract</summary>
  Ordinal information is central to tasks ranging from conference peer review to Reinforcement Learning from Human Feedback for large language models. In many such settings, there is no objective ground truth against which reports can be directly verified, making incentive-compatible elicitation challenging. Peer-prediction mechanisms have been designed to achieve truthful elicitation despite the lack of ground-truth verification. However, existing peer-prediction methods do not provide incentives...
  </details>

- **2026-11-04** — Shumao Wu, Kongcheng Zhang, Jianqiang Huang et al. — [Using Experience Twice: Dynamic Process Rubrics for Privileged Token-Level Credit Assignment](http://arxiv.org/abs/2611.06543v2)
  <details><summary>📄 Abstract</summary>
  Agent trajectories often contain both successful decisions and failed attempts, yet optimization with sparse trajectory-level rewards struggles to identify which critical decisions should be reinforced or suppressed. We observe that meaningful distinctions among on-policy trajectories can be distilled into natural-language process rubrics and used as process supervision signals. Based on this insight, we propose Online Rubric Self-Distillation (ORSD), which leverages self-derived process rubrics...
  </details>

- **2026-11-04** — Ye Yuan — [The Alignment Tax Is Graded: Task-Selective Capability Loss Under Length-Normalized DPO with SFT Retention](http://arxiv.org/abs/2611.06476v2)
  <details><summary>📄 Abstract</summary>
  Setting. This is an empirical characterization study; we propose no new method and run no comparisons against alternative objectives. We fine-tune Qwen3.5-4B with sparse LoRA and length-normalized DPO plus an SFT retention term (the RPO objective) on structured financial-filing tasks, and track downstream capability as the implicit reward margin grows to $\sim 7$ $β$-scaled units (nf4 training; $\sim 3$ under fp16 measurement on the unquantized base). Question. Does margin growth degrade capabil...
  </details>

- **2026-11-04** — Ji Pei — [Dexterous Robotic Hands in the Foundation-Model Era: A Full-Stack Survey of Hardware, Data, Cross-Embodiment Transfer, Learning, and Evaluation](http://arxiv.org/abs/2611.06724v1)
  <details><summary>📄 Abstract</summary>
  Dexterous robotic hands are increasingly coupled to large-scale human data and foundation models, yet progress in hardware, representation learning and evaluation is often assessed separately. This survey reviews work from January 2024 to early November 2026, with earlier studies included to establish technical lineages. We organize the literature into five interdependent layers: hardware; data collection and curation; cross-embodiment transfer; learning and foundation models; and evaluation and...
  </details>

- **2026-11-04** — Ruben Boone, Gilles Eerlings, Sebe Vanbrabant et al. — [Does Personality Persuade? Investigating Personality Trait Prompting and Persuasion in Large Language Models](http://arxiv.org/abs/2611.06572v1)
  <details><summary>📄 Abstract</summary>
  Large language models (LLMs) can be prompted to express different personality profiles, but it remains unclear how reliably they do so or whether personality affects their persuasiveness. We investigate these questions in two evaluations. First, we assess Big Five personality prompting using the IPIP-NEO-120, examining reproducibility, trait controllability, cross-trait effects, and unconditioned model profiles. Second, we conduct a within-subjects user study (N=32) in which participants discuss...
  </details>

- **2026-11-04** — Shumao Wu, Kongcheng Zhang, Jianqiang Huang et al. — [Using Experience Twice: Dynamic Process Rubrics for Privileged Token-Level Credit Assignment](http://arxiv.org/abs/2611.06543v1)
  <details><summary>📄 Abstract</summary>
  Agent trajectories often contain both successful decisions and failed attempts, yet optimization with sparse trajectory-level rewards struggles to identify which critical decisions should be reinforced or suppressed. We observe that meaningful distinctions among on-policy trajectories can be distilled into natural-language process rubrics and used as process supervision signals. Based on this insight, we propose Online Rubric Self-Distillation (ORSD), which leverages self-derived process rubrics...
  </details>

- **2026-11-04** — Mingzhe Zheng, Yue Wu, Jing Tan et al. — [EmoReward: Self-Evolving Reward Calibration for Emotional Video Generation RL](http://arxiv.org/abs/2611.06518v1)
  <details><summary>📄 Abstract</summary>
  Group Relative Policy Optimization (GRPO) has advanced generative model post-training in verifiable domains such as code and mathematics, but evaluating video quality, especially emotional expression, often depends on subjective aesthetics and has no uniquely correct target. Existing approaches typically rely on fixed rewards for visual quality, motion quality, and text alignment that poorly capture emotional intent and can invite reward hacking, while RLHF is difficult to scale and subject to i...
  </details>

- **2026-11-04** — Ji Shi, Lirong Jie, Lexiao Zou et al. — [Trace2Eval: Contextualized Evaluation of Coding Agents from Real-World Traces](http://arxiv.org/abs/2611.06506v1)
  <details><summary>📄 Abstract</summary>
  Coding agents are increasingly used in real-world workflows across diverse domains, motivating evaluation grounded in real user tasks. Existing benchmarks, however, largely rely on static public tasks with reference patches or hidden tests. Next-generation coding-agent benchmarks should therefore move beyond correctness on fixed tasks toward continually renewed evaluation of overall artifact quality in real user workflows.   We propose Trace2Eval, a dynamically updatable pipeline that constructs...
  </details>

- **2026-11-04** — Ye Yuan — [The Alignment Tax Is Graded: Task-Selective Capability Loss Under Length-Normalized DPO with SFT Retention](http://arxiv.org/abs/2611.06476v1)
  <details><summary>📄 Abstract</summary>
  Setting. This is an empirical characterization study; we propose no new method and run no comparisons against alternative objectives. We fine-tune Qwen3.5-4B with sparse LoRA and length-normalized DPO plus an SFT retention term (the RPO objective) on structured financial-filing tasks, and track downstream capability as the implicit reward margin grows to $\sim 7$ $β$-scaled units (nf4 training; $\sim 3$ under fp16 measurement on the unquantized base). Question. Does margin growth degrade capabil...
  </details>

- **2026-11-04** — Shengzhe Zhang, Qi Zhang, Dazhong Shen et al. — [$A^3$-VLA: Automatic Perception-Guided Attention Alignment for Robot Manipulation](http://arxiv.org/abs/2611.06447v1)
  <details><summary>📄 Abstract</summary>
  Vision-Language-Action Models (VLAs) enable robots to perform manipulation tasks by leveraging Vision-Language Models (VLMs) to process visual observations and language instructions. However, the action prediction objective itself lacks fine-grained task-specific perceptual supervision, making it prone to relying on task-irrelevant visual shortcuts, leading attention away from target objects and key interaction areas, thereby limiting its operational performance and generalization ability. To ad...
  </details>

- **2026-11-04** — Jiaqi Deng, Zhe Fu, Yakun Chen et al. — [Entropogram-guided Visual Realignment Decoding: Capturing the Rhythm of Multimodal Reasoning](http://arxiv.org/abs/2611.06415v1)
  <details><summary>📄 Abstract</summary>
  Multimodal large language models (MLLMs) have demonstrated remarkable progress on cross-modal reasoning tasks, yet they continue to suffer from hallucinations in long-chain reasoning processes. In this work, we revisit hallucination in MLLMs from the perspective of reasoning generation dynamics. We argue that entropy is not merely a static measure of uncertainty but a structured signal that reflects how modality information is integrated throughout decoding. Through systematic analysis, we ident...
  </details>

- **2026-11-04** — Anthony Nguyen, Wenjun Lin — [Does Context Compression Preserve Refusal Alignment?](http://arxiv.org/abs/2611.06380v1)
  <details><summary>📄 Abstract</summary>
  Context compression reduces inference cost by encoding inputs into compact representations while preserving semantic content. An open question is whether semantic preservation alone is sufficient to maintain downstream behaviours such as refusal alignment. We investigate this question and find that encoder-based compression systematically weakens refusal behaviour in instruction-tuned language models, despite high reconstruction fidelity. This effect persists across model families and compressio...
  </details>

- **2026-11-04** — Yaowen Ye, Jacob Steinhardt, Sarah Schwettmann et al. — [Mass Producing Training Data with Surprising Side Effects](http://arxiv.org/abs/2611.06324v1)
  <details><summary>📄 Abstract</summary>
  Training data can have unexpected side effects on language model behavior outside the training domain: insecure code data can induce broad misalignment, and outdated bird names can induce a 19th-century persona. Understanding such generalization is hard because only dozens of isolated examples exist, each constructed by hand or discovered by accident. We propose automatically discovering such datasets with surprising side effects (DSSEs). We define three objectives for DSSEs: they should (1) eli...
  </details>

- **2026-11-04** — Ziyi Jin, Kangjin Yu, Beichen Wang et al. — [Scale Anchoring via Implicit Semantics and Sequence-Consistent Loop Closure for VGGT-Based SLAM](http://arxiv.org/abs/2611.06308v1)
  <details><summary>📄 Abstract</summary>
  Feed-forward geometric foundation models enable dense monocular reconstruction without requiring camera calibration, but independently reconstructed submaps can accumulate scale drift, and even a valid revisit can yield an inconsistent cross-submap measurement. We extend VGGT-SLAM 2.0 with fixed-root scale anchoring and short-sequence-assisted direct loop connections. SALAD selects an image pair between the initial submap and each eligible new submap; joint VGGT inference then uses learned impli...
  </details>

- **2026-11-04** — Zhiliang Zhu, Jiazheng Huang, Dawei Zhao — [Beyond Scene Shortcuts: Action-Centric Video-Text Alignment for Fine-Grained Action Understanding](http://arxiv.org/abs/2611.06302v1)
  <details><summary>📄 Abstract</summary>
  Fine-grained action understanding requires vision-language models to ground what an agent does, how it acts, and why it acts in spatio-temporal evidence. However, richer supervision can backfire: fine-tuned models may generate detailed action descriptions grounded in static scenes and salient objects rather than motion, a failure we call Environment-Grounded Action Hallucination (EGAH). To mitigate EGAH, we propose Staged Attention Rectification and Reinforcement (STARR), an action-centric video...
  </details>

- **2026-11-04** — Tanmay Bakshi, Chenglong Wang, Simra Shahid — [Evaluating Human-LLM Alignment on Visualization Preference](http://arxiv.org/abs/2611.06272v1)
  <details><summary>📄 Abstract</summary>
  There are often multiple valid visualizations, spanning different chart types, visual encodings, and aesthetic choices, that can all support a user's goal of analyzing a dataset. Determining which of these candidate visualizations is most appropriate, however, remains challenging. Prior work has leveraged expert-curated taxonomies to guide visualization design and subsequent quality evaluation, a practical evaluation model must also account for human-centric factors. Latest visualization tools i...
  </details>

- **2026-11-04** — Henrik Marklund, Alex Infanger, Benjamin Van Roy — [A Definition of Catastrophic Performance](http://arxiv.org/abs/2611.06219v1)
  <details><summary>📄 Abstract</summary>
  A central challenge in AI is specifying objectives that align with human preferences. While existing theoretical results elucidate how misspecification impacts performance, they typically do not distinguish between merely suboptimal and catastrophic outcomes. To enable rigorous analysis of catastrophic risk from AI misalignment, we introduce a formal definition of catastrophic performance. Our definition is based on two reference values. The first, baseline value, captures the value attained if ...
  </details>

- **2026-11-04** — Peiran Wu, Fangfei Gou, Zhaoxi Mu et al. — [SleuthVLM: Do We Really Need Audio-in-Video for Omni Video Understanding?](http://arxiv.org/abs/2611.06083v1)
  <details><summary>📄 Abstract</summary>
  Omni models answer questions about videos by jointly processing sampled frames and audio in one turn, with progress driven largely by scaling model size and omni training data. We ask whether a model needs to hear the audio directly at all, and present SleuthVLM, an agent harness built on a VLM that never hears the audio directly: speech will be transcribed into text, and the VLM will sleuth the video on its own without any predefined workflow. On four omni benchmarks with videos up to 90 minute...
  </details>

- **2026-11-04** — Mengqi Huang, Wenchuan Wang, Zhendong Mao et al. — [Chronos: Sequential Identity-Preserving Video Generation by Temporal Anchoring](http://arxiv.org/abs/2611.05893v1)
  <details><summary>📄 Abstract</summary>
  Identity-preserving video generation aims to synthesize high-quality and visually realistic videos from textual and visual conditions while faithfully maintaining the subject's identity across diverse motions. Prior methods have extensively introduced reference-guided control signals and identity-aware conditioning to improve facial alignment from reference images. However, improving static identity alignment alone creates a fundamental tension between identity fidelity and temporal controllabil...
  </details>

- **2026-11-03** — Justin Downes, Robby Milletich, Newel Hirst — [Same Method, Different Task: What the Bitter Lesson Does Not License in Social Simulation](http://arxiv.org/abs/2611.05717v1)
  <details><summary>📄 Abstract</summary>
  The bitter lesson holds that general methods leveraging computation defeat hand-encoded domain knowledge. We argue it carries a condition its popular reading omits: in every case Sutton cites, the general method was scaled against the same task the domain engineering was solving. Social simulation substituted across tasks instead, replacing hand-built agents with an artifact optimized for predicting text. The move is bitter-lesson-shaped, but the lesson does not license it. Prediction is a solit...
  </details>

- **2026-11-03** — Keyty Loza, Shayan Monadjemi — [How Do Artificial Agents Make Decisions in Light of Visual Data?](http://arxiv.org/abs/2611.05671v1)
  <details><summary>📄 Abstract</summary>
  Vision-language models (VLMs) have demonstrated significant advances in reasoning with visual data, which is particularly important given that much of human knowledge is encoded visually in scientific articles and other sources. However, a gap remains in understanding how artificial agents, powered by VLMs, perceive and navigate decision-making under uncertainty in the presence of visual data. This study explores this gap by evaluating and analyzing autonomous decision-making processes. Building...
  </details>

- **2026-11-03** — Elad Yoshai, Natan T. Shaked — [CAPTOR: text-encoder-free grounding by counting caption co-occurrence over the visual words of a frozen encoder](http://arxiv.org/abs/2611.05599v1)
  <details><summary>📄 Abstract</summary>
  Grounding a text query in an image needs a matrix scoring every term against every patch. Vision-language models compute it with an aligned text encoder, which many image encoders, such as histopathology-related models trained on slides alone, lack. The Caption-Anchored Patch-Term Occurrence Representation (CAPTOR) estimates the matrix without a text encoder. It clusters a frozen image encoder's patch tokens into visual words and describes each captioned image by its share of patches in each wor...
  </details>

- **2026-11-03** — Hei Yi Mak, Hoang Le, Mehran Taghian Jazi et al. — [Aligning Training and Rollout Policies for End-to-End FP4 RL on Mixture-of-Experts LLMs](http://arxiv.org/abs/2611.04376v2)
  <details><summary>📄 Abstract</summary>
  In this work, we study end-to-end FP4 reinforcement learning (RL) post-training for Mixture-of-Experts (MoE) large language models. Recent work on FP4 RL has introduced effective recovery recipes that restore accuracy under aggressive low-precision quantization for dense models, but we find that the same approach yields no improvement over the naive FP4 baseline in the MoE setting. We conduct an in-depth study to understand why. Our analysis identifies the root cause in the routing mechanism uni...
  </details>


### 📂 robustness
*鲁棒性与可靠性 / Robustness & Reliability* — 58 papers

- **2026-11-06** — Yasin Ghadimi Zaker, Hamid Reza Ghaeini — [Navigating Complexity: A User-Centered Evaluation of Project Management Tools](http://arxiv.org/abs/2611.09260v1)
  <details><summary>📄 Abstract</summary>
  In the age of digital transformation, companies are increasingly relying on specialized software to manage the complexity of projects. However, when selecting tools, features and costs often take precedence over user experience (UX), leading to low adoption rates, user frustration, and project delays. This study empirically evaluates the user experience of leading project management tools (Jira, Trello, Monday.com, Asana, and Microsoft Project) across various project scales using a mixed methods...
  </details>

- **2026-11-06** — Hongbin Lin, Sizhe Zou, Juangui Xu et al. — [Learning When to Think: Dual-Reference Offline Optimization for Adaptive VLM Reasoning](http://arxiv.org/abs/2611.09154v1)
  <details><summary>📄 Abstract</summary>
  Reasoning traces improve vision-language models on complex multimodal tasks, but forcing every input to follow a long reasoning process leads to overthinking and unnecessary inference cost. We study adaptive fast/slow thinking for VLMs, where one model answers directly for simple inputs and reasons step by step when needed. Fast answers and slow traces often come from distinct behavior policies, making a single-reference offline objective misweight one mode. We propose DUAL-REFERENCE BOLT (DR-BO...
  </details>

- **2026-11-06** — Chen Chen, Omid Bagherieh, Naveen Nikamanth Appiah Balaji et al. — [On Agentic Manipulation Policies](http://arxiv.org/abs/2611.09892v1)
  <details><summary>📄 Abstract</summary>
  Recent work on robot manipulation has focused on specialist policies trained on demonstrations. We show that generalist AI models can control manipulators more reliably than specialist policies such as vision-language-action models (VLAs) and world-action models (WAMs). We systematically analyze agentic manipulation policies (AMPs), in which a generalist AI model commands the manipulator directly, adapting its actions as the task unfolds. We present AMP1, a reference harness that runs unchanged ...
  </details>

- **2026-11-06** — Yina Jian, Mingkun Xu — [Seeing What Matters: Benchmarking Task-Conditioned Actionable Spatial Belief for Manipulation](http://arxiv.org/abs/2611.09794v1)
  <details><summary>📄 Abstract</summary>
  When should a robot look at the cup, and when at the portafilter? Spatial-reasoning benchmarks evaluate whether a model can describe a scene, but manipulation needs something more specific: the ability to acquire the particular evidence that makes the current command executable. A view that is informative for one task can be useless for another, even at the same workstation. We introduce Seeing What Matters, a benchmark for task-conditioned actionable spatial belief in simulated tabletop manipul...
  </details>

- **2026-11-06** — Peter Belcak, Greg Heinrich, Saurav Muralidharan et al. — [CPU-ARC: Agentic Reasoning Caching for on-CPU Reasoning Reuse](http://arxiv.org/abs/2611.09891v1)
  <details><summary>📄 Abstract</summary>
  Large language models reinvent the wheel all the time. They conflate task-solving with the execution of the solutions, which forces them to solve every problem from scratch. We show that once a task has been reasoned through, the application of its solution to a new problem instance can be done very efficiently and with little involvement from language models. We introduce agentic reasoning caching, a method for constructing robust CPU-executable agentic reasoning caches (ARCs) from LLM reasonin...
  </details>

- **2026-11-06** — Haoyu Wang, Ru Wang, Yuanyuan Wang et al. — [On the Reliability of Majority-Vote Pseudo-Labels in Test-Time Reinforcement Learning](http://arxiv.org/abs/2611.09872v1)
  <details><summary>📄 Abstract</summary>
  Test-time reinforcement learning (TTRL) adapts pretrained language models to unlabeled target-domain data using self-generated pseudo-labels, whose reliability remains poorly understood. We analyze majority-vote supervision for TTRL with online Direct Preference Optimization (DPO) and decompose its error into population-majority bias and prompt-dependent finite-rollout variation. Because population-majority bias is generally unidentifiable without external supervision, we focus on mitigating the...
  </details>

- **2026-11-06** — Julien Cardinal, Andrew Chedid, Imen Benzarti et al. — [QAOA for Layered Architecture Recovery: Feasibility, Limits, and the Role of Decomposition](http://arxiv.org/abs/2611.09744v1)
  <details><summary>📄 Abstract</summary>
  Layered architecture recovery (LAR) reconstructs a system's architectural layers from its package dependencies, and is defined as a combinatorial optimisation problem solved with classical search. We investigate whether the Quantum Approximate Optimization Algorithm (QAOA) can be applied to LAR, and with what practical limitations. We formulate LAR as a Quadratic Semi-Assignment Problem, transform it into a Quadratic Unconstrained Binary Optimisation (QUBO) problem in which each package is penal...
  </details>

- **2026-11-06** —  Sonali, Deeksha Varshney, Asif Ekbal — [ReSUM: Reasoning-Driven Multi-Agent Framework for Query-Focused Summarization](http://arxiv.org/abs/2611.09349v1)
  <details><summary>📄 Abstract</summary>
  LLMs excel at language tasks, but long-meeting QFS remains difficult due to complex speaker dynamics, sparse key information, and limited data. Meetings involve disfluencies, long transcripts and complex discourse. QFS have high risk of information omission, hallucination, even for advanced models such as GPT-4-mini and Gemini. Existing end-to-end methods compress retrieval, evidence extraction, and summary generation into a single pass, failing to handle the complex reasoning required for targe...
  </details>

- **2026-11-06** — Yuhang Guan, Huanle Zhang, Xiaomin Ouyang et al. — [UniExit: A Unified Latency-Aware Early-Exit Runtime for Heterogeneous Edge AI](http://arxiv.org/abs/2611.09159v1)
  <details><summary>📄 Abstract</summary>
  Edge applications increasingly combine CNN-based perception with edge-deployable Transformer-based language models, but deploying such heterogeneous workloads on resource-constrained devices is challenging because inference latency varies with both input difficulty and runtime hardware state. Early-exit inference reduces computation by terminating at intermediate stages, yet existing methods are often model-specific and rely on static latency profiles that become stale under dynamic edge conditi...
  </details>

- **2026-11-06** — Davide Batic, Denys Dutykh — [Perfect Wave Transfer in Nonconformal Tomonaga-Luttinger Liquids](http://arxiv.org/abs/2611.09018v1)
  <details><summary>📄 Abstract</summary>
  Perfect wave transfer (PWT) reproduces spatial reflection at a common finite time under a fixed Hamiltonian. We classify this process for open compact bosons and inhomogeneous Tomonaga--Luttinger liquids, distinguishing transfer of oscillator and neutral observables from transfer on the charged field algebra. In the single-charge model, the first two notions coincide. Global transfer additionally requires rephasing of the compact zero mode. For regular reflection-symmetric channels, exact oscill...
  </details>

- **2026-11-05** — Xiaodong Wu, Zhimin Zhao, Qi Li et al. — [What the Middleman Delivers: Answer Behavior, Tool Permissions, and Billed Usage in LLM API Relays](http://arxiv.org/abs/2611.07650v1)
  <details><summary>📄 Abstract</summary>
  Third-party application programming interface (API) relays offer access to large language models (LLMs), often at lower prices. Users depend on these services for model quality, instruction compliance, and accurate billing. However, existing studies leave unclear whether relays meet these expectations together. We test 20 relays offering GPT-6 Astra and Claude Opus 5. First, we compare answers to knowledge questions with batch-matched official responses. In our first-round sample, the analysis f...
  </details>

- **2026-11-05** — Ramyad Hadidi — [Should You Split Decode? Disaggregation Across Future Models and Accelerators](http://arxiv.org/abs/2611.08299v1)
  <details><summary>📄 Abstract</summary>
  For large language model (LLM) inference, prefill/decode disaggregation (P/D) is deployed in production to isolate phases with different resource demands. Attention/feed-forward network disaggregation (AFD) splits decode again, but adds communication, placement constraints, and another provisioned pool. We ask whether role-specific placement repays this cost as models and accelerator roadmaps change. Infrastructure is committed before future models and hardware can be benchmarked. We present Sil...
  </details>

- **2026-11-05** — Benedikt Blumenstiel, Hugues Devimeux, Johannes Jakubik et al. — [TerraMesh-Masks: Open-Vocabulary Segmentation for Earth Observation](http://arxiv.org/abs/2611.08081v1)
  <details><summary>📄 Abstract</summary>
  Open-vocabulary segmentation (OVS) enables models to segment a variety of concepts specified in natural language, removing the need for fixed label sets and fine-tuning. While recent OVS approaches have shown strong performance on natural images, they transfer poorly to Earth observation (EO) data due to differing semantics, scales, sensing modality, and geographic context. To date, large-scale EO-specific datasets and benchmarks for OVS remain scarce. We, therefore, introduce TerraMesh-Masks, a...
  </details>

- **2026-11-05** — Kapil Bhardwaj, Tauseef Ejaz, Sayani Majumdar — [Scenario-aware Adaptive Neuromorphic Intelligence for multimodal sensor fusion](http://arxiv.org/abs/2611.07830v1)
  <details><summary>📄 Abstract</summary>
  Multisensory Physical AI systems operating in isolated conditions must make timely and reliable decisions within strict energy and hardware budgets. In this context, the present analytical study investigates the feasibility of reliable multimodal sensor fusion using a neuromorphic approach based on memristor-based Integrate-and-Fire neuron circuits driven by aggressively compressed representations of sensory information. Rather than relying on fixed processing and learning parameters, the propos...
  </details>

- **2026-11-05** — Seong-Eun Hong, JuYeong Hwang, Jinhyun Kim et al. — [Seeing Beyond the Next Step: World-Model-Guided Human-Like Navigation in Multi-Agent Scenes](http://arxiv.org/abs/2611.07730v1)
  <details><summary>📄 Abstract</summary>
  Selecting a next motion in a populated scene is not just a matter of avoiding what is currently in the way: an action can be locally feasible yet drift onto the road instead of the crosswalk, cut into a stream of crossing pedestrians, or bottleneck a narrow passage. These failure modes are invisible from the current state alone, and acting on them requires reasoning about what each candidate action will cause. World models offer exactly this, namely action-conditioned predictions of the future, ...
  </details>

- **2026-11-05** — Yixiao Wang, Peiyi Chen, Mustafa Mukadam et al. — [Latent RL Priors for Data-Efficient Dexterous Manipulation](http://arxiv.org/abs/2611.08458v1)
  <details><summary>📄 Abstract</summary>
  Learning dexterous manipulation from limited visual demonstrations is challenging because policies must acquire both perceptual grounding and precise control, while reinforcement learning (RL) in simulation can acquire rich control behaviors from large-scale interaction with privileged information. We introduce \textbf{Latent RL Prior}, a two-stage framework that reuses this control knowledge for data-efficient visual policy learning. During privileged pretraining, we distill large-scale RL roll...
  </details>

- **2026-11-05** — Sateesh Kumar, Arnav Balaji, Arpit Bahety et al. — [MOMASPLAT: Dynamic Novel-View Demonstration Augmentation for Mobile Manipulation](http://arxiv.org/abs/2611.08372v1)
  <details><summary>📄 Abstract</summary>
  Visuomotor policies trained through imitation learning are highly sensitive to changes in camera viewpoint. This is particularly problematic for mobile manipulation (MoMa), where robots rarely execute manipulation from the exact same base pose used during demonstration collection due to navigation uncertainty, localization drift, and environmental constraints. Recent approaches use novel-view synthesis (NVS) to augment demonstrations with unseen viewpoints, but they assume static scenes and ther...
  </details>

- **2026-11-05** — Guanren Qiao, Ruixiang Ouyang, Sheng Xu et al. — [Semantics-to-Contact: A Stagewise Framework for Robust Contact-Rich Manipulation](http://arxiv.org/abs/2611.07532v1)
  <details><summary>📄 Abstract</summary>
  Contact-rich manipulation requires precise control under complex contact dynamics while remaining robust to diverse visual conditions. However, real-world reinforcement learning often overfits to the visual appearance of training scenes. We propose Semantics-to-Contact (S2C), a stagewise framework for visually robust contact-rich manipulation. The insight is to decompose the problem into two stages: semantic focusing and contact refinement. In the first stage, a vision-language model localizes t...
  </details>

- **2026-11-05** — Vinay Rodrigues, Sara Zeynalpour, Gokhan Solak et al. — [An Empirical Study of Reinforcement Learning for Keypoint Positioning of Deformable Linear Objects](http://arxiv.org/abs/2611.07261v1)
  <details><summary>📄 Abstract</summary>
  Deformable linear object (DLO) manipulation is challenging because high-dimensional configurations, nonlinear contact dynamics, and diverse material and geometric properties produce a broad range of object responses that are both difficult to model and data-intensive to learn. This work studies reinforcement learning for planar manipulation of a one-end-grasped DLO, focusing on training efficiency, observation design, robustness, and zero-shot sim-to-real transfer. We compare three Proximal Poli...
  </details>

- **2026-11-05** — Mohammed Hassan, Zhenyang Chen, Zheng Wang et al. — [T3R: Training-Free Two-Stage Token Refinement Towards Efficient and Robust VLA Models](http://arxiv.org/abs/2611.08413v1)
  <details><summary>📄 Abstract</summary>
  Vision-Language-Action (VLA) models enable end-to-end robot control, but inference is increasingly expensive. Each decision processes hundreds of visual tokens, often across multiple cameras, leading to substantial computation while allowing irrelevant background content to distract action prediction under distribution shift. We argue that these issues stem from two complementary forms of redundancy: many visual tokens are spatially irrelevant, while attention over the remaining tokens is often ...
  </details>

- **2026-11-05** — Timon S. Gutleb — [Interpretable many-body interaction laws for collective motion from few trajectories](http://arxiv.org/abs/2611.08314v1)
  <details><summary>📄 Abstract</summary>
  Models of collective motion usually reduce social interactions to pairwise forces, despite empirical evidence for many-body effects. We introduce the directional atomic cluster expansion (dACE), which adapts the atomic cluster expansion (ACE) of interatomic potentials to self-propelled agents. dACE provides a systematically improvable, exactly equivariant expansion of an agent's acceleration that splits uniquely into 1-, 2-, 3-body and higher contributions, along with a self term for the agent's...
  </details>

- **2026-11-05** — P. de Clermont Gallerande, Q. Avril, P. Gosselin et al. — [REACT: Towards Real-Time Completion of Skeletal Motion Signals](http://arxiv.org/abs/2611.08301v1)
  <details><summary>📄 Abstract</summary>
  Tracking user motion in interactive and immersive applications is increasingly common (e.g., video games, XR systems, smartphones). Yet, processing and transmitting human motion data remain critical challenges, as current approaches strongly rely on the quality of the tracked motion signals. In general, affordable motion-capture systems may produce unnatural animations in the presence of calibration errors, occlusions, sensor drift, high-frequency noise, or other artifacts. More specifically, we...
  </details>

- **2026-11-05** — Zeping Zhang, Zhuoya Zhao, Samy Metari et al. — [FreeOcc: Decoupling Ego-Motion for Efficient 4D Occupancy Forecasting via Continuous Flow Matching](http://arxiv.org/abs/2611.08128v1)
  <details><summary>📄 Abstract</summary>
  Current 4D occupancy world models use heavy cross-attention or deep recurrence to disentangle ego-motion from scene dynamics. This requires significant computational capacity. However, this effort is largely redundant since the ego-vehicle's intended future motion is provided by the downstream motion planner. We present FreeOcc, a lightweight continuous-time world model that introduces explicit $SE(2)$ geometric decoupling into a conditional flow-matching framework. By mathematically factoring o...
  </details>

- **2026-11-05** — Giuseppe Emanuele Lio, Roberto Caputo, Alain J. Corso et al. — [An Agent-Driven, Cross-Validated Inverse-Design Pipeline for Dielectric Metasurfaces](http://arxiv.org/abs/2611.08127v1)
  <details><summary>📄 Abstract</summary>
  Inverse design of dielectric metasurfaces is powerful but labour-intensive: each new target requires choosing a parameterization and a figure of merit, managing compute resources, and critically assessing results that may be numerically unconverged, sensitive to fabrication errors or trapped in local optima. Here we present an open-source pipeline in which an artificial intelligence (AI) coding agent turns a plain-language specification into metasurface optimization runs, executes them, analyses...
  </details>

- **2026-11-05** — Soroush H. Zargarbashi, Mohammad Sadegh Akhondzadeh, Aleksandar Bojchevski — [Should We Pay This Much for Robustness? Efficient Proxy Certificates with Marginal Guarantees](http://arxiv.org/abs/2611.08035v1)
  <details><summary>📄 Abstract</summary>
  Modern classifiers remain sensitive to small input perturbations, while strong model-agnostic robustness certificates such as randomized smoothing are often too expensive for deployment, requiring an extensive number (e.g. 2000) of model forward passes per input. We propose a framework that delegates certification to a cheap proxy function while statistically controlling its deviation from the original sound certificate. Given an exchangeable unlabeled calibration set, we tune the proxy via robu...
  </details>

- **2026-11-05** — Sabbir Ahmed, Hazem Abbas, Salimur Choudhury — [How Far Can Lightweight LLMs Go in Intent-to-SLO Translation?](http://arxiv.org/abs/2611.07982v1)
  <details><summary>📄 Abstract</summary>
  Intent-based networking (IBN) promises QoS provisioning in which the network derives the configuration from operator-stated goals. Its first step, translating a natural-language intent into enforceable service-level objectives (SLOs) grounded in a live snapshot of the network state, increasingly relies on large language models (LLMs). These large models add cost and energy to the management loop and typically require multi-GPU, cloud-hosted infrastructure. Can lightweight open LLMs take over thi...
  </details>

- **2026-11-05** — Viola Campos, Thomas Klassert, Adrian Ulges — [Which Signals of Code Correctness Survive Distribution Shift? Hidden-State and Causal Predictors of Program and Verdict Correctness](http://arxiv.org/abs/2611.07876v1)
  <details><summary>📄 Abstract</summary>
  Large language models increasingly judge code, yet without external feedback such judgments are unreliable, and verifying them by executing tests or by extended reasoning is costly. Instead, execution-free correctness predictors use signals from the model's output probabilities, sampled solutions, or hidden states to identify judgments that warrant further verification. However, these predictors may degrade under distribution shifts when generalizing across projects and languages.   We compare s...
  </details>

- **2026-11-05** — Nischay Dhankhar, Alisher Amantay, Zhanibek Datbayev et al. — [Towards Foundation Decision Models: Drex](http://arxiv.org/abs/2611.07854v1)
  <details><summary>📄 Abstract</summary>
  Autoregressive approaches with large language models, such as long chain-of-thought reasoning, have become the default for new AI applications because they reach higher accuracy on a wide range of tasks. In production, however, they give inconsistent answers, require parsing of outputs, and add cost and latency. Decision models address this: given a question and a set of options supplied by the user, they return a probability distribution over the options without autoregressive decoding. We pres...
  </details>

- **2026-11-05** — Moritz Grävinghoff, Konstantin Wehmeyer, Aron Asefaw et al. — [Adapters as Data: The Latent Space of LoRAs](http://arxiv.org/abs/2611.07775v1)
  <details><summary>📄 Abstract</summary>
  LoRA adapters are usually treated as finished artifacts rather than as a data modality. Prior work has shown that LoRA adapters populate a low-dimensional manifold that a linear PCA basis already organizes well enough to support different operations such as sampling, editing, and inversion. We ask what a learned, nonlinear latent adds beyond this. We train a transformer autoencoder on the same population of LoRA identity adapters, mapping each into a latent space and compare every operation agai...
  </details>

- **2026-11-05** — Dengyao Shi, Tianyu Fu, Fei Hu et al. — [BiGrounder: Bidirectional Training Unlocks the Potential of GUI Grounding](http://arxiv.org/abs/2611.07765v1)
  <details><summary>📄 Abstract</summary>
  Graphical User Interface (GUI) grounding aims to map natural language instructions to precise operational coordinates, serving as a critical task for autonomous agent interaction. Current approaches formalize GUI grounding as predicting action-coordinate pairs from instructions, with end-to-end training supervised solely by final coordinates. Training datasets typically provide only a small number of descriptions per target coordinate, whereas real-world scenarios involve a much larger set of va...
  </details>

- **2026-11-05** — Marios Costa, Elias Antoniou, Herodotos Herodotou et al. — [First Overlap Formulation and Perturbative Results for Supersymmetric QCD](http://arxiv.org/abs/2611.07745v1)
  <details><summary>📄 Abstract</summary>
  We present a lattice formulation of N=1 supersymmetric QCD (SQCD) based on overlap fermions, providing a discretization consistent with the Ginsparg-Wilson relation. Particular emphasis is placed on the construction of Yukawa terms that preserve a lattice-modified chiral symmetry involving overlap quarks and gluinos. To realize this modified chiral symmetry in the Yukawa sector, we follow Lüscher's strategy and introduce auxiliary Dirac and Majorana fermionic fields for the quark and gluino fiel...
  </details>

- **2026-11-05** — Minh Canh Tu, Quang-Binh Nguyen, Khoi Nguyen — [ArtCrafter: Feed-Forward Generation of Articulated 3D Object with Analytic Joint Derivation](http://arxiv.org/abs/2611.07658v1)
  <details><summary>📄 Abstract</summary>
  Articulated 3D assets are essential for robotic simulation and training, yet their generation from casual images poses a key challenge: recovering part geometry and kinematics that remain mutually consistent. We present ArtCrafter, a novel feed-forward generative model for controllable generation of articulated 3D objects from a pair of images, one depicting the object in the rest state and the other in the open state. At the core of ArtCrafter is a DiT-based generative model that jointly produc...
  </details>

- **2026-11-05** — Mayank Anand, Subham Raj, Aman Vaibhav Jha et al. — [MEMOIR: A Training-Free Memory Lifecycle for Long-Horizon LLM Agents](http://arxiv.org/abs/2611.07631v1)
  <details><summary>📄 Abstract</summary>
  Long-horizon LLM agents require memory systems that preserve useful information across sessions and retrieve it when needed. Existing systems treat these as separate problems: memories are written prospectively with static importance scores that are never revised after use. This creates two coupled failure modes: consolidation can silently destroy evidence that future queries require, while retrieval continues to favor stale memories. We propose MEMOIR (Memory Evidence via Merge-certified, Onlin...
  </details>

- **2026-11-05** — Chanyoung Kim, Harim Song, Byoungchan Ko et al. — [Binding Paraphrased Instructions to Encountered Objects in sLLM Agents under Partial Observability](http://arxiv.org/abs/2611.07599v1)
  <details><summary>📄 Abstract</summary>
  Reliable deployment of LLM agents requires grounding diverse user expressions in their environments. Although RL-finetuned smaller large language model (sLLM) agents rival larger prompted LLMs on embodied tasks, their robustness to instruction paraphrases remains unclear. We introduce ALFWorld-Para to evaluate this robustness under controlled paraphrases, revealing 21-52% declines in success rates (SRs), predominantly driven by object synonyms. Despite retaining knowledge of synonym referents, a...
  </details>

- **2026-11-05** — Dmitry Ryvkin, Qin Wu — [Robust prizes in all-pay contests with loss aversion](http://arxiv.org/abs/2611.07419v1)
  <details><summary>📄 Abstract</summary>
  We study robust prize design in all-pay contests with loss-averse agents when the principal does not know the agents' convex cost of effort, subject to an aggregate productivity constraint. The robustly optimal prize structure awards equal prizes to all contestants except the one ranked last. The optimal bottom prize is zero under moderate loss aversion, but becomes positive and increases with loss aversion when loss aversion is sufficiently strong. Under strong loss aversion, the robust solutio...
  </details>

- **2026-11-05** — Qingyun Liu, Yuankun Liu, Jiaye Feng et al. — [PSGAgent: Enhancing MLLMs' Dynamic Visual Perception for Panoptic Scene Graph Generation via Agentic Reasoning](http://arxiv.org/abs/2611.07408v1)
  <details><summary>📄 Abstract</summary>
  Panoptic Scene Graph generation (PSG) requires holistic yet fine-grained reasoning over complex relations among objects. However, current Multimodal Large Language Models (MLLMs) applied to PSG suffer from a perception bottleneck: they function as static observers limited by fixed-resolution views. As a result, models often overlook critical relations involving small or peripheral objects and struggle to differentiate ambiguous predicates in complex scenes. To address these limitations, we propo...
  </details>

- **2026-11-05** — Shiyue Jia, Nan Bai, Dawei Shi et al. — [Distributed Robust Model Predictive Control for Optimal Consensus of Unknown Multiagent Systems with Event-Triggered Communication](http://arxiv.org/abs/2611.07383v1)
  <details><summary>📄 Abstract</summary>
  In this paper, we study the optimal consensus problem for multiagent systems with unknown dynamics. We propose a robust model predictive control (MPC) framework that jointly optimizes the control input and consensus sequences while enforcing state and input constraints. Within this framework, noisy offline data are used to construct nominal prediction models and quantify the associated uncertainty, which is explicitly incorporated into the robust MPC design. To solve the resulting optimization p...
  </details>

- **2026-11-05** — Xianjing Zhu, Wenqi Lou, Yuanbo Wen et al. — [Rule-Guided and Trajectory-Aware Repair for LLM-Based HLS Generation](http://arxiv.org/abs/2611.07324v1)
  <details><summary>📄 Abstract</summary>
  Large language models (LLMs) offer a promising path for directly generating functionally correct and synthesizable HLS-C from natural-language specifications. However, existing approaches often struggle to turn multi-round tool feedback and reusable HLS knowledge into effective revisions, limiting end-to-end generation success. We propose MementoHLS, an agentic HLS generation framework built around executable and falsifiable dual-memory-guided repair. MementoHLS combines an Executable Repair Con...
  </details>

- **2026-11-05** — Jacob Solinsky, Serguei Pakhomov — [Encoding and Propagation of Grammatical Number in Large Language Models](http://arxiv.org/abs/2611.07283v1)
  <details><summary>📄 Abstract</summary>
  Sparse autoencoders (SAEs) have become an increasingly popular means of translating Large Language Model (LLM) hidden state vectors into a human-comprehensible list of features or symbols. As such, SAEs may provide insight into an LLM's knowledge representation and internal ``mental'' grammar - topics of pragmatic interest for mechanistic interpretation of AI behavior and of theoretical interest for the study of in silico representations of human language. Language models with fewer than 100M pa...
  </details>

- **2026-11-04** — Jaime Ruiz-Serra, Tomáš Gavenčiak, Jobst Heitzig — [Goal Revelation as a Bridge Between Information-Theoretic Empowerment and Capability-Based Human Power](http://arxiv.org/abs/2611.07247v1)
  <details><summary>📄 Abstract</summary>
  Power matters for AI safety. Optimal agents tend to acquire power across a wide range of objectives (instrumental convergence). As we embed AI agents into socio-technical systems, humans risk gradual disempowerment. Both concerns call for a formal, quantitative measure of power. Two such measures in the context of Markov games are information-theoretic empowerment, the capacity of the channel from an agent's actions to future states, and capability-based individual power, a measure of goal attai...
  </details>

- **2026-11-04** — Weiduo Yuan, Ze Yuan, Sihan Liu et al. — [Spatial-UMI-Dream: Scaling World Action Models with Metric Geometry for UMI Manipulation](http://arxiv.org/abs/2611.07229v1)
  <details><summary>📄 Abstract</summary>
  The Universal Manipulation Interface (UMI) enables scalable demonstration collection independently of a specific robot. However, its moving, close-range gripper cameras entangle camera and object motion without a stable external view, leaving the metric geometry needed for precise manipulation implicit in RGB. We introduce Spatial-UMI-Dream, a 5B spatial World Action Model (WAM) pretrained on 605 hours of RGB-D UMI data through two-stage training -- world-only adaptation followed by joint world-...
  </details>

- **2026-11-04** — Burkay Tunçtürk, Koorosh Aslansefat, Yiannis Papadopoulos et al. — [More Agents, More Reliable? System-Level Reliability of Multi-Agent LLMs under Operational-Profile Uncertainty](http://arxiv.org/abs/2611.07140v1)
  <details><summary>📄 Abstract</summary>
  Teams increasingly build software from cooperating large language model (LLM) agents, often assuming more agents mean more reliability. Yet the usual evidence, average benchmark accuracy, ignores the input mix a deployed system meets and the rule merging the agents' answers. Building on HIP-LLM, a hierarchical imprecise-probability assessment of single LLMs, we propose a framework combining it with a Bayesian network of the system's failure logic for multi-agent systems. Agent failure-probabilit...
  </details>

- **2026-11-04** — Ali Habibnia, Esfandiar Maasoumi, Gaurav Shah — [Double Machine Learning for Panel Data: Identification, Specification, and a Bank Regulation Effect](http://arxiv.org/abs/2611.07249v1)
  <details><summary>📄 Abstract</summary>
  This paper examines robustness and causal interpretation of panel estimates using double/debiased machine learning. The prototype treatment setup is the 2018 US banking regulation. Under common treatment timing, we characterize identification and nuisance restrictions and derive exact bank-level representations of specified "within" and "first-difference" scores. Simulations assess panel model transformation-induced specification bias and inference under weaker overlap. Empirically, estimates va...
  </details>

- **2026-11-04** — Nirdesh Chauhan, Dushyant Rajput, Siddharth Kosaraju — [When Can Self-Play Fix a False Belief? Answer Keys, Pass Bands and Replacement Rules in an Execution-Grounded Loop](http://arxiv.org/abs/2611.06965v1)
  <details><summary>📄 Abstract</summary>
  Self-play loops in which a model writes tasks, derives an answer key and trains on its own matching solutions are often called grounded when the key comes from executing code. We ask which false beliefs such a loop removes. We run expert-iteration self-play with Qwen3-4B-Base on output-prediction tasks, vary the source of the answer key, and track natural beliefs about Python semantics and two misreadings of task specifications planted by fine-tuning ("at most n" read as < n; "the k-th smallest"...
  </details>

- **2026-11-04** — Joan C. Timoneda, Sebastián Vallejo Vera — [Replicability, Reproducibility, and Robustness in Political and Social Science Research with Large Language Models](http://arxiv.org/abs/2611.06639v1)
  <details><summary>📄 Abstract</summary>
  This chapter addresses the central reproducibility problem of research with large language models. LLM output is probabilistic and varies across models and versions, which can have significant effects on downstream statistical results. The chapter distinguishes between replicability, reproducibility, and robustness, and proposes a probabilistic standard based on the distribution of results, not identical outputs. It introduces a standardized prompt script, tests within-model variation for encode...
  </details>

- **2026-11-04** — Harshit Gupta, Shunichi Ishihara — [How Well Can Large Language Models Impersonate Individual Authors? A Comparative Evaluation](http://arxiv.org/abs/2611.05771v1)
  <details><summary>📄 Abstract</summary>
  This study investigates the authorship impersonation capacity of six widely used large language models (LLMs): Gemini 3 Pro, Claude Opus, GPT 5.2, GPT 5.2 Pro, DeepSeek 3.2, and Grok 4.1 Fast. The evaluation was conducted using short product review texts selected to ensure high within author consistency in individual writing style. Two types of in context prompt were designed: a simple prompt with minimal instruction and a complex prompt incorporating explicit stylometric guidance for mimicry. A...
  </details>

- **2026-11-04** — Qiang Wang, Jianxin Bi, Shulong Jiang et al. — [PyRUA-REAL: Robot Exploration and Adaptive Learning through RSI in the Real World](http://arxiv.org/abs/2611.06768v1)
  <details><summary>📄 Abstract</summary>
  Coding agents powered by models such as GPT-6-Astra connect spatial reasoning with executable robot behavior, raising the question of how such agents can produce lasting improvements in robot capabilities from physical interaction. In this work, we study embodied recursive self-improvement (RSI) through real-world exploration, code refinement, and deployment using PyRUA-REAL, a framework in which coding agents retain interaction experience as persistent memory and reusable executable skills that...
  </details>

- **2026-11-04** — Mattia Greiche, Reihaneh Rabbany, Maximilian Puelma Touzel — [A Framework for Context Enrichment and Selective Robustness in LLM Social Agents](http://arxiv.org/abs/2611.06914v1)
  <details><summary>📄 Abstract</summary>
  Researchers use large language models as agents in social simulations, where agents are prompted with observations and background information intended to shape their actions. Yet LLM agents have been shown to substantially change their behavior under meaning-preserving prompt variations, creating a validation problem for social simulation. One plausible hypothesis is that this brittleness reflects a lack of grounding and can be reduced by enriching the context provided to the agents. Whether ric...
  </details>

- **2026-11-04** — Ruikang Li, Zixuan Chen, Jiarui Wu et al. — [TailSteer: Trajectory-Tail Steering for Drift-Resistant Multi-turn Image Editing](http://arxiv.org/abs/2611.06741v1)
  <details><summary>📄 Abstract</summary>
  Strong single-turn editing performance does not guarantee reliable multi-turn interaction: as edited outputs are repeatedly reused, small unintended changes can accumulate into severe visual drift. This long-term drift is often mitigated through training on multi-turn data or cross-turn rollouts, potentially altering pretrained priors, or through specialized inference-time mechanisms that are difficult to scale to foundation models. We introduce TailSteer, a final-stage training framework that i...
  </details>

- **2026-11-04** — Yutong Ma — [Data Center Agglomeration and Power Infrastructure Capacity in the United States](http://arxiv.org/abs/2611.06737v1)
  <details><summary>📄 Abstract</summary>
  The continuous expansion of digital infrastructure, especially data centers, has imposed unprecedented, geographically concentrated stress on existing power grids. However, rigorous causal evidence quantifying how these facilities reshape local power-infrastructure supply remains limited. This study builds a comprehensive county-level US panel dataset spanning 2010-2024, uniquely integrating individual data center building footprints and power-plant additions. To mitigate endogeneity and high-di...
  </details>

- **2026-11-04** — Kejian Zhu, Zhuoran Jin, Shangqing Tu et al. — [What Does Multi-Turn Reinforcement Learning Really Improve in LLM Agents?](http://arxiv.org/abs/2611.06483v1)
  <details><summary>📄 Abstract</summary>
  While multi-turn agentic reinforcement learning (RL) excels on long-horizon tasks, its performance gains remain highly sensitive to interaction constraints. Evaluating across sampling breadth $K$ and interaction depth $T$ via $Pass@(K,T)$, we show that trajectory-level RL advantages depend on sufficient turn budgets, diminishing significantly when budgets tighten. Besides, agentic RL does not uniformly elevate single-step decision quality; rather, its strength concentrates in error recovery and ...
  </details>

- **2026-11-04** — Kasra Fallah, Rudramani Singha, Hannah Ghanei et al. — [Mind Control of LLMs via Closed-Loop Stimulation: Out-of-Distribution Robustness](http://arxiv.org/abs/2611.06418v1)
  <details><summary>📄 Abstract</summary>
  Brains and large language models need not be considered equivalent systems to reveal an interpretable commonality: both exhibit high-dimensional, nonlinear dynamics whose behavior can only be modeled imperfectly. This creates a shared challenge whenever we seek to intervene in their dynamics. A controller may either rely on a model identified around a particular operating regime and risk failure as the system moves away from that regime, or explicitly account for uncertainty and a changing inter...
  </details>

- **2026-11-04** — JunYong Lee, Woo Kyung Kim, Honguk Woo — [MA-Mesh: Resilient Multi-Agent Collaboration via Role-based Self-Healing](http://arxiv.org/abs/2611.06389v1)
  <details><summary>📄 Abstract</summary>
  Effective collaboration in multi-agent systems requires mechanisms for coordination and adaptability in dynamic and uncertain environments. However, existing multi-agent systems rarely model resilience explicitly, instead relying on ad-hoc output correction that limits systematic, runtime management of robustness. In this work, we propose Multi-Agent Mesh (MA-Mesh), a framework that constructs a role-based self-healing layer on top of a collaboration pattern. Specifically, MA-Mesh generates resi...
  </details>

- **2026-11-04** — Varun A. Paturkar, Shankar Gangisetty, C. V. Jawahar — [MotoVerse: A Benchmark for Predictive Perception of Motorized Two-Wheelers in Dense Unstructured Traffic](http://arxiv.org/abs/2611.06007v1)
  <details><summary>📄 Abstract</summary>
  Motorized Two-Wheelers (MTWs) dominate personal transport across much of the Global South, yet remain largely overlooked in predictive perception research for autonomous driving and ADAS. We introduce MotoVerse, a benchmark for predictive perception from an MTW's ego-centric perspective. MotoVerse comprises 949 maneuver clips collected in dense, unstructured traffic and trajectory annotations for over 31,000 surrounding road agents, including over 16,000 MTWs, enabling two complementary tasks: E...
  </details>

- **2026-11-04** — Shuli Jiang, Khushbu Pahwa, Yuting Zhang et al. — [Learning When Human Decisions Matter: Executor-Relative Consultation Value for LLM Agents](http://arxiv.org/abs/2611.05814v1)
  <details><summary>📄 Abstract</summary>
  Large language models increasingly automate complex tasks, but human decision capacity does not scale with their capabilities. In many applications, humans remain essential for providing private context, authority, or judgments unavailable to the agent. We formulate human decision capacity allocation: given multiple consultation opportunities and a limited budget, at which decisions should an LLM agent consult a human? The central challenge is estimating consultation value, which is executor-dep...
  </details>

- **2026-11-04** — Rohit Mohan, Maximilian Luz, Swarnava Chowdhury et al. — [WayPOP: A Panoramic Open-Set Panoptic Tracking Benchmark](http://arxiv.org/abs/2611.05801v1)
  <details><summary>📄 Abstract</summary>
  Holistic perception for autonomous agents requires reliably segmenting and associating scene elements across time and camera views, including objects outside a fixed semantic taxonomy. Existing open-set panoptic benchmarks focus on individual images or views, while panoramic tracking benchmarks assume closed-set taxonomies. Consequently, these benchmarks do not evaluate whether unknown objects can be consistently segmented and tracked across synchronized multi-camera sequences. We introduce WayP...
  </details>

- **2026-11-03** — Hang Chen, Jiaying Zhu, Wenya Wang — [Unifying and Beyond the Theory of Pervasive Capability Degradation in LLM Post-training SFT from Feature Interference](http://arxiv.org/abs/2611.05003v2)
  <details><summary>📄 Abstract</summary>
  Pervasive Capability Degradation (PCD) refers to the phenomenon in which supervised fine-tuning (SFT), while adapting a large language model (LLM) to a target task, often erodes the general capabilities acquired during pre-training. Prevailing explanations attribute PCD to macroscopic distribution shift and therefore lack microscopic manipulability, leaving existing mitigation methods without a complete theoretical foundation. In this paper, we first develop a bottom-up geometric theory of PCD g...
  </details>

- **2026-11-03** — Ce Li, Tao Lin — [Learning to Design Information](http://arxiv.org/abs/2611.05701v1)
  <details><summary>📄 Abstract</summary>
  Information designers, such as large language models and online platforms, often do not know the subjective beliefs of their receivers or users. We construct learning algorithms enabling the designer to learn the belief of a strategic receiver through repeated interactions. Our learning algorithms are robust to the receiver's strategic manipulation of the learning process of the designer. We study regret relative to two benchmarks to measure the performance of the algorithms. The static benchmar...
  </details>


### 📂 watermark
*水印与溯源 / Watermarking & Provenance* — 17 papers

- **2026-11-06** — Claudio Segal, Paulo Segal, Hudson Silva Borges et al. — [Agents on the Patch Path: Mining AI-Associated Security Remediation in GitHub Security Advisories](http://arxiv.org/abs/2611.09808v1)
  <details><summary>📄 Abstract</summary>
  Autonomous coding agents are increasingly involved in software development, but their participation in real-world security remediation remains poorly understood. We investigate observable evidence of coding-agent involvement in commits referenced by reviewed GitHub Security Advisories (GHSAs), characterize the associated vulnerabilities, and examine review timing in relation to advisory disclosure routes.   We develop a local-Git mining pipeline that identifies agent evidence through known agent...
  </details>

- **2026-11-06** — Jingjia Teng, Yang Li, Wenjie Huang — [CARGO: Causal Attribution and Responsibility-Guided Preventive Safe Multi-Agent Reinforcement Learning for Cooperative Driving](http://arxiv.org/abs/2611.09139v1)
  <details><summary>📄 Abstract</summary>
  This study presents Causal Attribution and Responsibility-Guided Optimization (CARGO), a multi-agent reinforcement learning framework for cooperative on-ramp merging in mixed traffic. A shared latent-context posterior and an action-conditioned response model estimate directed behavioral influence, with posterior uncertainty propagated into interaction-edge selection. Complementary attribution mechanisms couple signed influence with marginal team utility for cooperative reward shaping and assign ...
  </details>

- **2026-11-05** — Andrei Alexandru Drăghici, Sediola Ruko, Briland Hitaj et al. — [KeHoSu: Keyed Homoglyph Substitution for Authenticated Text Provenance over Copy-Paste Channels](http://arxiv.org/abs/2611.08046v1)
  <details><summary>📄 Abstract</summary>
  Nowadays, large language models produce text at scale, and much of it is redistributed across platforms. A moderator who finds a suspicious comment, post or article may want to know which platform generated it and for which account. In this paper we study attribution over the channel through which such text actually travels, copy-paste, which discards document metadata but keeps Unicode code points. We present KeHoSu, which turns the confusable characters of homoglyph attacks into a keyed attrib...
  </details>

- **2026-11-05** — Rolf Drechsler, Christina Plump — [Secure Formal Raising: Protecting the Development of AI through Executable Properties](http://arxiv.org/abs/2611.08042v1)
  <details><summary>📄 Abstract</summary>
  Model raising revisits Turing's developmental view of machine intelligence. Formal Raising (FR) has recently been proposed to complement this view with explicit behavioral properties. This paper extends that proposal to the security of the raising environment. Secure Formal Raising (SFR) models policy integrity, authorization, and confidential data flow using four-valued evidence that preserves unknown and inconsistent assessments. We prove six security invariants and show that they force admiss...
  </details>

- **2026-11-05** — Ahana Biswas, Yu-Ru Lin — [Signals, Evidence, and Context: User Scrutiny in Real-World LLM Conversations](http://arxiv.org/abs/2611.08232v1)
  <details><summary>📄 Abstract</summary>
  Large language models (LLMs) often present synthesized answers without making their supporting evidence easy to inspect. We study how features of these answers relate to users' subsequent accepting, checking, and challenging in 489,283 assistant-user response pairs from ShareChat and WildChat. Broad attribution language appears in 31.9% of qualifying responses, compared with explicit URLs in 1.33%, revealing a gap between claims of grounding and preserved inspectable support. Attribution, uncert...
  </details>

- **2026-11-05** — Charalampos M. Liapis, Epameinondas Panagopoulos — [Technohybridism: Recursive Semantic Normalization in AI-Mediated Societies](http://arxiv.org/abs/2611.07984v1)
  <details><summary>📄 Abstract</summary>
  Language-generating AI systems are no longer only objects of linguistic interaction: their outputs increasingly re-enter the communicative and institutional practices from which their training material was drawn. Drawing on social theory, social epistemology, and the philosophy of language, this article develops a sociotechnical account of that re-entry. We introduce recursive semantic normalization: the process through which machine-generated formulations, once recurrently taken up, evaluated, ...
  </details>

- **2026-11-05** — Micheline Bénédicte Moumoula, Serge Lionel Nikiema, Tailia Malloy et al. — [A Low Similarity Score Does Not Show Independence after Source-Conditioned Repository Rewriting](http://arxiv.org/abs/2611.07887v1)
  <details><summary>📄 Abstract</summary>
  Maintainers sometimes cite a low token-similarity score as evidence that an LLM-assisted rewrite of a copyleft project is independent of the original. We test what such a score can support under \emph{source-conditioned} rewriting: a coding agent keeps the original in its working copy, rewrites the repository, and iterates until a fixed behavioural harness passes, with no human edit to the code. On 69 rewrites of six copyleft Python projects we find that: \ding{182}~Agent-only rewriting is inexp...
  </details>

- **2026-11-04** — Nigel F. Doering, Rahath Malladi, Arshia Sangwan et al. — [Structured Machine Theory of Mind from Agent Trajectories](http://arxiv.org/abs/2611.07208v1)
  <details><summary>📄 Abstract</summary>
  Predictive models of human behavior trained on large-scale trajectory data optimize for statistical accuracy without representing the mental states that causally generate behavior. Such models support prediction but not principled intervention: they cannot answer how an agent's behavior would change if its beliefs or preferences were different. We introduce Structured Machine Theory of Mind (SMToM), a framework that attributes explicit, independently supervised belief and desire representations ...
  </details>

- **2026-11-04** — Ruifeng Ren, Gun Ahn — [Closed-Loop Agent Evaluation: Layered Measurement and Self-Calibration](http://arxiv.org/abs/2611.07051v1)
  <details><summary>📄 Abstract</summary>
  Once an agent is live, teams want to know whether it is doing its job, not just whether it throws errors. Yet most evaluation is one-off: a benchmark run, a look at traces, a single score. Its conclusions neither check themselves nor reach the agent. We propose closed-loop evaluation, an evaluation method for deployed agents. It models evaluation as performance estimation under biased raters and censored outcomes, and it requires every level's conclusion to trace back to atomic data and to be co...
  </details>

- **2026-11-04** — Vivek Acharya — [The Two-Ledger Model: Transaction-Grain Cost Accounting for Multi-Agent AI Systems Across Clouds, Models, and Systems of Record](http://arxiv.org/abs/2611.06989v1)
  <details><summary>📄 Abstract</summary>
  Enterprises run business transactions through multi-agent AI systems spanning clouds, large language models (LLMs), orchestration harnesses, and systems of record. Finance receives AI cost only at settlement grain, aggregated by SKU and charge period. The business question (what did this order, claim, or case cost in AI?) cannot be answered from billing data, because providers never see enterprise transaction boundaries. The FinOps Open Cost and Usage Specification (FOCUS) gives billing data one...
  </details>

- **2026-11-04** — Sofia Bobadilla, Carmine Cesarano, Raphina Liu et al. — [EPISTEME: Trustworthy Coding Agents Through Tool Call Intent](http://arxiv.org/abs/2611.06563v1)
  <details><summary>📄 Abstract</summary>
  Coding agents change software through tool calls. Tool calls mutate the local state. For good? For bad? Nobody knows. Agents never say why a tool call is made. We propose the epistemic agent design, in which the harness guarantees that the model declares why a tool call is made. The harness then records what the command actually did and checks the self-reported declaration against these effects. The result is a journal 1) that can guard calls before they run and 2) that supports audits and foren...
  </details>

- **2026-11-04** — Khalid Tounoussi, Mohammed Sayagh, Ali Ouni et al. — [MCP-Eco: A Linked Dataset of MCP Servers, Consumers, and Development Activity](http://arxiv.org/abs/2611.06897v1)
  <details><summary>📄 Abstract</summary>
  The Model Context Protocol (MCP) enables LLM agents to access external tools and data. Studying its software ecosystem requires connecting server interfaces, the projects that configure these servers, and their development activity. However, this information is scattered across directories, package registries, configuration files, and repository histories. We present MCP-Eco, a relational dataset that integrates these sources and links consumer configuration declarations to candidate server proj...
  </details>

- **2026-11-04** — Shaoliang Yang, Jun Wang — [Ranking Agreement Does Not Reveal Paragraph-Edit Agreement in Two Released Paper Acceptance Predictors](http://arxiv.org/abs/2611.06789v1)
  <details><summary>📄 Abstract</summary>
  A fast acceptance classifier could select revisions for a slower evaluator. We ask whether agreement on existing papers supports that use. We compare a classifier of word and document features with two released text-only acceptance predictors fine-tuned from the same language model with three billion parameters. For 198 papers from the International Conference on Learning Representations, we compare model rankings of the original papers and of paragraph rewrites screened automatically for unchan...
  </details>

- **2026-11-04** — Jyotin Goel, Abhinav Arun, Tejas Prakash Agarwal et al. — [ArcRAG: Agentic Compositional Retrieval over Knowledge Graphs](http://arxiv.org/abs/2611.06481v1)
  <details><summary>📄 Abstract</summary>
  Graph-based retrieval-augmented generation (GraphRAG) answers questions by retrieving over a knowledge graph built from a corpus. Yet retrieval strategies are designed around the structure their own construction pipeline produces, and whether they survive a change of construction is rarely tested. We study this cross-construction portability: whether one retrieval procedure, with no construction-specific schema, relation names, or retuning, stays effective when the graph is built differently. We...
  </details>

- **2026-11-04** — Hongnian Huang, Hongliang Liu — [When Every Choice Is Correct: A Causal Study of Numerical Preference in Language Models](http://arxiv.org/abs/2611.06025v1)
  <details><summary>📄 Abstract</summary>
  When a language model chooses a number between 1 and 30, every integer in the range is valid, yet the model can favor particular answers. We use numerical choice to study how preference is processed across layers and tokens. Perturbation probing and gradient attribution nominate neurons for activation interventions. In a selected Qwen3-4B case, a pre-answer edit changes 17 to 15 while both runs first emit 1. After the edit ends, selective cache and attention-output replacements trace part of its...
  </details>

- **2026-11-04** — Hila Levi-Yosefi, Shunit Agmon, Ester Livshits et al. — [A Comparative Study of Importance Attribution to Columns in Deep Learning over Relational Databases](http://arxiv.org/abs/2611.05986v1)
  <details><summary>📄 Abstract</summary>
  Deep learning over relational databases has led to increasingly effective prediction models, motivating a growing need to explain their behavior. We study explanation methods that assign importance scores to individual database attributes, focusing on a fundamental question: to what extent does the choice of importance-attribution method matter? We develop a methodology to systematically compare importance-attribution methods and analyze their similarities and differences. In particular, we stud...
  </details>

- **2026-11-04** — Zimu Liu, Xiaoxi Guo, Xiaolu Tang et al. — [Can LLM Agents Learn to Test? Maintaining Scoped Experience as Testing Evidence for Mobile GUI Testing](http://arxiv.org/abs/2611.05873v1)
  <details><summary>📄 Abstract</summary>
  Repeated mobile GUI tests can reuse routes, locators, and recovery strategies from earlier executions. However, a route that worked in one workflow or app version may be irrelevant or misleading in another. We study how an LLM-based tester can retain useful experience while withholding entries contradicted by current observations. We present a maintenance contract for AdaptiTest in which reusable experience has an explicit applicability scope, trace provenance, and a lifecycle for confirmation, ...
  </details>


### 📂 unlearning
*机器遗忘 / Machine Unlearning* — 1 papers

- **2026-11-05** — Nicolás Segura-Kunsagi, Juan Luis Suárez-Díaz, Iván Sevillano-García et al. — [DISCERN: Distributional Synthetic Replay for Retain-Free Incremental Machine Unlearning](http://arxiv.org/abs/2611.07892v1)
  <details><summary>📄 Abstract</summary>
  Machine unlearning aims to remove the influence of specific training data from a trained model without retraining from scratch. In real deployments, however, deletion requests arrive over time, calling for incremental class unlearning (ICU): classes are removed sequentially, previously forgotten knowledge must remain forgotten, and the remaining classes must be preserved. We present DIstributional SynthetiC rEplay for Retain-free iNcremental unlearning (DISCERN), an intervention-based class unle...
  </details>


### 📂 agent-safety
*Agent 安全框架 / Agent Safety Frameworks* — 1 papers

- **2026-11-03** — Kiran Ravish, Ankita Kushwaha,  Preeti et al. — [MA-SafeDiffuser: Safe Multi-Agent Planning with Diffusion Probabilistic Models](http://arxiv.org/abs/2611.05524v1)
  <details><summary>📄 Abstract</summary>
  We propose MA-SafeDiffuser, a multi-agent extension of SafeDiffuser that equips diffusion-based trajectory planners with finite-time diffusion invariance guarantees for joint-agent safety specifications. Building on the single-agent construction that embeds control barrier function (CBF) constraints into reverse-diffusion updates, we: (i) formalize joint safe sets as intersections of per-agent and pairwise barrier sets; (ii) derive centralized and decentralized (communication-aware) constrained ...
  </details>


### 📂 benchmark
*安全评测与基准 / Safety Benchmarks & Evaluation* — 1 papers

- **2026-11-05** — Zhi Zhang, Francesco Belardinelli, Alessandro Abate — [Geometry-Evolving Barrier Functions for Safety Evaluation in Dynamic Environments](http://arxiv.org/abs/2611.07788v1)
  <details><summary>📄 Abstract</summary>
  Autonomous systems operating in dynamic environments often involve multiple interacting agents, giving rise to high-dimensional safety evaluation problems. Hamilton--Jacobi (HJ) reachability provides rigorous finite-horizon safety guarantees, but solving a global HJ partial differential equation (PDE) over the entire state space leads to prohibitive computational complexity. In this paper, we introduce Geometry-Evolving Barrier Functions (GEBFs), a novel representation for dynamic safety evaluat...
  </details>


### 📂 survey
*综述与系统化 / Surveys & Systematization* — 6 papers

- **2026-11-06** — Wei Huang, Youjin Deng — [Deep Learning Theory through the Lens of Statistical Physics: A Topical Review](http://arxiv.org/abs/2611.09138v1)
  <details><summary>📄 Abstract</summary>
  The recent success of foundation models and deep learning has far outpaced our theoretical understanding of how large-scale neural networks learn and generalize. Statistical physics provides a natural language for describing such high-dimensional, nonlinear, and strongly coupled systems, offering concepts such as mean-field theory, phase transitions, energy landscapes, and stochastic dynamics. In this topical review, we adopt a statistical-physics way of thinking -- from concepts including phase...
  </details>

- **2026-11-05** — Max Unterbusch, Julian Frattini, Michael Mircea et al. — [Adapt the Object to the Subject: Representative Study Material for Empirical Software Engineering](http://arxiv.org/abs/2611.07772v1)
  <details><summary>📄 Abstract</summary>
  External validity is a central concern in empirical software engineering, yet the debate has largely focused on whether study participants are representative. How well the study objects they reason about - code, models, or requirements - are representative of each participant's own work is often overlooked. Practitioners' own artifacts would be ideal, but are often out of reach, so researchers sample from public datasets or construct objects artificially. Whether this lack of subject-object fit ...
  </details>

- **2026-11-04** — Wenda Li, Congcong Yuan — [FA-Agent: An extensible multimodal agent framework for first-arrival picking in mountainous seismic data](http://arxiv.org/abs/2611.06555v2)
  <details><summary>📄 Abstract</summary>
  First-arrival traveltimes underpin near-surface velocity modeling and static corrections, but in low signal-to-noise mountainous land data the first arrival is often weak, intermittent, and masked by strong direct waves and noise. Energy-based pickers then pick later arrivals or noise, and deep-learning pickers usually require retraining for a new survey. Because erroneous picks bias first-arrival tomography, many difficult zones are still inspected and corrected manually. We present FA-Agent, a...
  </details>

- **2026-11-04** — Eraldo Pereira Marinho — [Object-independent evaluation of small-data astronomical image classifiers: architecture, representation, and acquisition shortcuts](http://arxiv.org/abs/2611.06484v1)
  <details><summary>📄 Abstract</summary>
  Reported performance in small astronomical image datasets can reflect object reuse, field-of-view differences, acquisition settings, and catalogue-derived properties as well as astronomical morphology. We designed \dataset{} to measure these effects in a four-class task comprising galaxies, globular clusters, nebulae, and open clusters. The dataset contains 370 catalogue-supported physical objects, each represented by three Digitised Sky Survey FITS bands, and uses a group-constrained split of 2...
  </details>

- **2026-11-04** — Wenda Li, Weibing Cai, Congcong Yuan — [FA-Agent: An extensible multimodal agent framework for first-arrival picking in mountainous seismic data](http://arxiv.org/abs/2611.06555v1)
  <details><summary>📄 Abstract</summary>
  First-arrival traveltimes underpin near-surface velocity modeling and static corrections, but in low signal-to-noise mountainous land data the first arrival is often weak, intermittent, and masked by strong direct waves and noise. Energy-based pickers then pick later arrivals or noise, and deep-learning pickers usually require retraining for a new survey. Because erroneous picks bias first-arrival tomography, many difficult zones are still inspected and corrected manually. We present FA-Agent, a...
  </details>

- **2026-11-03** — Egor Pakhomov, Erik Nijkamp — [Attributing Agent Failures to Their History Needs an Executed Counterfactual: Toward a Reporting Standard](http://arxiv.org/abs/2611.05650v1)
  <details><summary>📄 Abstract</summary>
  Published explanations of why long-horizon agents fail are commonly taxonomies labeled over completed trajectories: a judge reads a transcript and names the failure. We argue that a claim attributing an agent's behavior to its history should carry intervention-verified evidence, per instance or via a validated estimator: freeze an executable mid-trajectory state, alter only the history the agent sees, and continue - executed rather than inferred from the transcript, at a state whose restoration ...
  </details>


### 📂 other
*其他安全相关 / Other Security-Related* — 191 papers

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

- **2026-11-06** — Qiang Chen, Xiao Wang, Qingquan Yang et al. — [FusionCLIP: Multimodal Contrastive Pretraining for Fusion Plasma Diagnostics](http://arxiv.org/abs/2611.09493v1)
  <details><summary>📄 Abstract</summary>
  Visible-light videos and multivariate diagnostic signals provide complementary observations of tokamak discharges. However, existing fusion pretraining methods, primarily learn representations by reconstructing or predicting observations, leaving the correspondence between these modalities underexplored. Representation learning is further challenged by the fact that plasma-related regions occupy only part of each video frame and diagnostic variables have substantially different sampling rates. W...
  </details>

- **2026-11-06** — Viraj Mishra, Shubham Gupta, Dhruv Gupta et al. — [Definitions, Label Names, or Demonstrations? Auditing What Governs LLM Annotation](http://arxiv.org/abs/2611.09457v1)
  <details><summary>📄 Abstract</summary>
  Large language models (LLMs) are increasingly used to annotate social-science texts, but high accuracy does not establish that they apply researcher-supplied category definitions: predictions may instead reflect prior associations with category labels or labeled demonstrations. We introduce a counterfactual audit that reassigns definitions among output labels, distinguishing adherence to supplied definitions from preservation of a dataset's original mapping. Across three political-text datasets,...
  </details>

- **2026-11-06** — Shao-Chun Hu, Zi-Xiang Lin, Hsin-Min Wang et al. — [GTCRN-SS: Lightweight Causal Speech Separation with Residual Allocation and Reconstruction Refinement](http://arxiv.org/abs/2611.09358v1)
  <details><summary>📄 Abstract</summary>
  Low-complexity causal speech separation must preserve speaker information and allocate residual mixture energy without relying on future feature frames. We present GTCRN-SS, a two-stage time-frequency separator that adapts the compact GTCRN enhancement backbone to fixed-output speech separation. The model combines internal residual allocation, reconstruction-conditioned refinement, and frame-aligned recurrent-state transfer. Its complex-mask estimator assigns non-target content to an unreturned ...
  </details>

- **2026-11-06** — Jiabin Lin, Shana Moothedath, Vivek S. Borkar — [Safety-Focused Reinforcement Learning Using Risk-Sensitive Coupled Control](http://arxiv.org/abs/2611.09290v1)
  <details><summary>📄 Abstract</summary>
  This paper investigates the coupled control problem within safety-focused reinforcement learning, addressing the essential challenge of achieving optimal performance while ensuring safety in systems operating within complex environments. We define safety as the requirement to prevent the system from reaching undesirable or hazardous states. We propose a coupled control approach that prioritizes safety by employing effective methods to prevent the system from entering unsafe states while optimizi...
  </details>

- **2026-11-06** — Sangbu Yun, Jung Gyu Min, Jin Hyun et al. — [TwinHash: Two-Sided Object Identity Management for Time- and Energy-Efficient Agentic Workflows](http://arxiv.org/abs/2611.09254v1)
  <details><summary>📄 Abstract</summary>
  Agentic artificial intelligence (AI) services interleave large language model (LLM) generation with external tool execution, and increasingly rely on search-based workflows that repeatedly revisit shared reasoning states and computations. These patterns create substantial redundancy across tool outputs, LLM responses, and key-value (KV) prefixes, yet existing serving systems primarily optimize shared prompt prefixes, while naive input-keyed caching is unsafe when identical requests produce diffe...
  </details>

- **2026-11-06** — Zhuoran Li, Xu Sun, Chang Wen Chen et al. — [Controllable Molecule Generation via Sparse Representation Editing: An Interpretability-Driven Perspective](http://arxiv.org/abs/2611.09235v1)
  <details><summary>📄 Abstract</summary>
  Controllable molecule generation is crucial for diverse scientific applications, such as drug discovery and materials design. While large language models (LLMs) show great promise, their dense and entangled representations impede precise control over the generation of molecules with bespoke substructures or properties. To address this, we propose Sparse Representation Editing (SpaRE), an interpretability-driven framework for fine-grained and precise control in LLM-based molecule generation. The ...
  </details>

- **2026-11-06** — Seoyeon Kim, Jeonghyun Kang, Hamin Koo et al. — [KLEAR: Knowledge-Matched LLM Evaluation in Korean across Application Requirements via Controlled Benchmark Transformation](http://arxiv.org/abs/2611.09223v1)
  <details><summary>📄 Abstract</summary>
  Existing Korean benchmarks for Large Language Models (LLMs) evaluate performance across diverse knowledge domains, but their accuracy scores cannot distinguish whether incorrect responses arise from a lack of required knowledge or a failure to apply that knowledge correctly. Our analysis of existing Korean benchmarks reveals that most questions can be answered through factual recall alone, while those demanding greater application also differ in required knowledge, making it difficult to isolate...
  </details>

- **2026-11-06** — Yiyu Gui, Mingzhi Chen, Guibo Luo et al. — [BrainCoT: A Multi-Task Zero-Shot Brain Signal Foundation Model with Neurometric-Anchored Chain-of-Thought Reasoning](http://arxiv.org/abs/2611.09082v1)
  <details><summary>📄 Abstract</summary>
  Brain signals exhibit substantial multi-center heterogeneity, strong inter-subject variability, and highly diverse task settings, which makes it difficult to build models that generalize beyond a single task. While recent brain signal foundation models leverage large-scale pretraining to learn generalizable representations, they often fall short in practice because they still require target-data-specific supervised adaptation, lack multi-task zero-shot capability, and rarely provide verifiable e...
  </details>

- **2026-11-06** — Vignesh Rajagopal, Rohan Chandra — [FASTFUNNELS: Agile Multi Robot Navigation in Narrow Spaces via Adaptive Dynamic Funnels](http://arxiv.org/abs/2611.09005v1)
  <details><summary>📄 Abstract</summary>
  We focus on the problem of high-speed multi-robot navigation in cluttered spaces with tight spatial constraints. A key challenge is balancing safety with agility, as existing methods often trade one for the other (slowing down near a bottleneck to avoid collisions versus failing to swerve in time at high speeds), especially for car-like systems. Our approach belongs to the family of formation control methods, in which Ackermann-steering agents coordinate while navigating tight spaces. However, c...
  </details>

- **2026-11-06** — Yuchen Li, Lisa Liu, Runqi Zou et al. — [Language as Trait, Politeness as Strategy: Controlled Tests of Linguistic Effects in LLM Social-Deduction Agents](http://arxiv.org/abs/2611.09768v1)
  <details><summary>📄 Abstract</summary>
  Large language model (LLM) agents coordinate through conversation, and the same message can be phrased in simpler or more complex language, bluntly or politely. We test whether such differences change how other agents judge and act, using the LURK Werewolf framework, which separates each utterance's speech-act predicate from its natural-language realization. We rewrite only the realization, check that the game content is preserved, and replay each game day from saved checkpoints against a re-sam...
  </details>

- **2026-11-06** — Donglin Zhuang, Pragaash Ponnusamy, Xiaoxia Wu et al. — [FOSCAR: Accelerating Decode Attention over 2- and 4-Bit KV Caches through Affine Folding](http://arxiv.org/abs/2611.09722v1)
  <details><summary>📄 Abstract</summary>
  Large-language-model decode attention streams the key-value (KV) cache for every generated token. Packing that cache into 2-bit or 4-bit quantized integers reduces memory traffic but does not automatically translate into latency saving. Existing 2-bit fused kernels reach under 31%/15% of peak HBM throughput on H100/B200. Converting each value and applying its scale and offset before feeding Tensor Cores is a major bottleneck because instruction-issue throughput is scarce on modern GPUs. Instead ...
  </details>

- **2026-11-06** — Mohamed Elmoghany, Kehan Li, Ruoqu Chen et al. — [ToolDex: An Ego-Exo Human Demonstration Dataset for Creative Physical Tool Use](http://arxiv.org/abs/2611.09036v1)
  <details><summary>📄 Abstract</summary>
  Creative tool use is a fundamental human capability and an important step toward general-purpose embodied intelligence. It requires agents to reason about object affordances, physical constraints, and manipulation strategies, especially when standard tools are unavailable. However, progress in this area is limited by the lack of real-world datasets that capture human tool-use behavior with sufficient scale, fidelity, and diversity. Existing benchmarks are often simulation-based, focus on simplif...
  </details>

- **2026-11-06** — Kaiyuan Chen, Xinyue Zhu, Shuangyu Xie et al. — [A Controlled Study of Models, Skills, Feedback, and Curriculum in Agentic Robotics](http://arxiv.org/abs/2611.09030v1)
  <details><summary>📄 Abstract</summary>
  Agentic robotics asks coding agents to implement and iteratively improve robot policies from simulated and real-world physical interactions. We study the self-learning loop of agentic robotics through a controlled simulation study spanning nine manipulation tasks, 631 different experiment configurations, and 28K coding agent rollouts, systematically varying model capability, skill priors, feedback structure, and curriculum. The experiment data suggests that the bottleneck is often not the access...
  </details>

- **2026-11-06** — Shengjia Chen, Ruchika Verma, Kevin Clare et al. — [Health-System-Wide Mapping of Demographic Information in Routine Clinical Histopathology](http://arxiv.org/abs/2611.09851v1)
  <details><summary>📄 Abstract</summary>
  The extent to which demographic-associated information is detectable across organs and disease states in routine clinical histopathology remains unclear. Here, we analyzed 1.3 million hematoxylin and eosin whole-slide images from 257,322 patients across 25 organs, using pathology foundation-model representations and multiple-instance learning to systematically map information associated with sex, age group, and self-reported race. Across 69 organ-demographic combinations, demographic attributes ...
  </details>

- **2026-11-06** — Dario Scilla, Omar A. Lopez, Mattia Rosso et al. — [Zero-Shot Benchmarking of Unified Multimodal Models for Shallow-Water UAV Image Distortion Assessment and Restoration](http://arxiv.org/abs/2611.09740v1)
  <details><summary>📄 Abstract</summary>
  Shallow-water UAV imagery provides centimeter-scale observations of benthic environments, but water-induced distortions complicate interpretation. To our knowledge, we present the first systematic zero-shot benchmark of unified multimodal large language models (MLLMs) for both assessing water-induced distortions and restoring shallow-water imagery within the same model framework. We evaluate five open-weight unified MLLMs with frozen pretrained weights and without access to paired reference imag...
  </details>

- **2026-11-06** — Aleksei Chernulich, M. Bumin Yenmez — [Who Picks First? Compensatory Fairness When Equal Division Is Impossible](http://arxiv.org/abs/2611.09685v1)
  <details><summary>📄 Abstract</summary>
  When indivisible objects, such as heirlooms or tickets to sports events, do not divide evenly among agents with equal claims, some agents must receive more objects than others. Can picking first compensate those with fewer objects? We propose two principles of compensatory fairness. An agent with fewer objects must not envy a larger bundle with any one of its objects removed, and priority advantages among agents with equally many objects must alternate rather than accumulate. Non-wastefulness, n...
  </details>

- **2026-11-06** — Constantinos Karouzos, Nikolaos Aletras — [Steerable Multi-Objective Group-Relative Preference Optimization with Jointly Trained Low-Rank Adapters](http://arxiv.org/abs/2611.09634v1)
  <details><summary>📄 Abstract</summary>
  Language model deployment often requires different trade-offs between competing objectives as user preferences change, yet standard post-training methods typically produce a single policy for a fixed objective weighting. We introduce LambdaMix, a new parameter efficient method for learning a preference conditioned family of policies with group-relative online reinforcement learning. LambdaMix jointly trains one low-rank adapter per objective over a frozen base model. One preference vector select...
  </details>

- **2026-11-06** — Teerthal Patel, Henry V. Hirvonen, Fábio S. Bemfica et al. — [Mathematical foundations and numerical simulations of BDNK hydrodynamics: from heavy-ion collisions to astrophysics](http://arxiv.org/abs/2611.09582v1)
  <details><summary>📄 Abstract</summary>
  We present new developments in the mathematical foundations and numerical simulations of the causal and stable first-order relativistic viscous hydrodynamic theory by Bemfica, Disconzi, Noronha, and Kovtun (BDNK) in general spacetimes. We develop two independent flux-conservative algorithms for arbitrary 3+1-dimensional spacetime metrics. Both are hyperbolic, causal, and well-posed, pass convergence tests, and reproduce known results. The first uses a new first-order reduction with mathematicall...
  </details>

- **2026-11-06** — Xiangjing An, Zhibin Jiao, Aiting Chen — [StockASkill: A Local-First AgentSkill for Intelligent Stock Selection](http://arxiv.org/abs/2611.09528v1)
  <details><summary>📄 Abstract</summary>
  Quantitative equity selection and portfolio construction in emerging and cross-border markets frequently suffer from computational bottlenecks, remote API fragility, survivorship bias, and rigid execution constraints such as discrete board lots and investor-mandated drawdown limits. In this paper, we present StockASkill, a local-first, full-data-driven AgentSkill engineered as a specialized Quant Co-Processor for autonomous AI agents and quantitative researchers. Tailored for agile portfolios (1...
  </details>

- **2026-11-06** — Mingkai Li, Jiajun Wu, Yihan Mao et al. — [LEMMO: A Large Electromagnetic Model leveraging Pretrained LLMs for Million-Sample Signal Understanding](http://arxiv.org/abs/2611.09476v1)
  <details><summary>📄 Abstract</summary>
  Large language models have expanded beyond text to vision, audio, and other modalities, but understanding raw electromagnetic (EM) signals remains challenging. Wideband recordings can contain millions of samples, whereas existing waveform-based EM models are primarily evaluated on short in-phase and quadrature (IQ) segments, leaving long-recording understanding and detailed description insufficiently explored. We introduce LEMMO, a large EM model for instruction-driven recognition and descriptio...
  </details>

- **2026-11-06** — Sarah Ashby, David Bostanjyan, Mikayel Khanbekyan — [Reconstructing intracell polarization with calibrated sapphire-window optics for collimated blue-light generation in a rubidium cell](http://arxiv.org/abs/2611.09441v1)
  <details><summary>📄 Abstract</summary>
  We study the polarization dependence of collimated blue light (CBL) generated near 420~nm by resonant four-wave mixing in thermal rubidium vapor in a sapphire-window cell driven at 780 and 776~nm. Sapphire windows can transform the polarization of pump light before it reaches the vapor, complicating the interpretation of polarization-dependent nonlinear emission. We measured the 780-nm pump Stokes state at an external before-cell reference plane to calibrate the common HWP/QWP preparation optics...
  </details>

- **2026-11-06** — Jiakai Yang, Haoye Zheng, Yixiao Yue et al. — [SmartBloch-Agent: An Agentic Framework for Automated MRI Sequence Design and Optimization](http://arxiv.org/abs/2611.09413v1)
  <details><summary>📄 Abstract</summary>
  Magnetic resonance imaging (MRI) pulse sequences organize radiofrequency excitation, gradient encoding, and signal acquisition, determining magnetization evolution and image formation. Sequence research requires translating imaging objectives into executable protocols meeting physical and acquisition constraints, refined via physical simulation, signal reconstruction, and scientific evaluation. Sequence construction, physical verification, parameter search, and assessment involve many tools and ...
  </details>

- **2026-11-06** — Róisín Luo, Ihsan Ullah, Christian Gagné et al. — [MIRA: Mitigating Pole Geometry Bias in Recurrent Language Models](http://arxiv.org/abs/2611.09412v1)
  <details><summary>📄 Abstract</summary>
  We show that the Transformer's recurrent successors --- such as selective state-space models (SSMs), Receptance Weighted Key Value (RWKV), and Retentive Network (RetNet) --- can be characterized as infinite-impulse-response (IIR) systems. The zero--pole geometries of these IIR systems characterize the temporal modes they can represent. However, to trade parallelism, the algebraic structures of the parameterizations of these recurrent systems often give rise to poles constrained to the real axis,...
  </details>

- **2026-11-06** — Jusheng Zhang, Keze Wang, Liang Lin — [Can LLMs Debug Robots by Editing Their Weights?](http://arxiv.org/abs/2611.09376v1)
  <details><summary>📄 Abstract</summary>
  A language model can repair a robot policy's lexical instruction grounding by editing just 65 token-embedding rows. We bring weight-space programming to robot foundation policies: GPT-6 Astra reads weights and uses a CPU workspace and budgeted simulator feedback, without gradient updates or new demonstrations. Three independent sessions on $π_{0.5}$ all improve success on 765 held-out paraphrases; the best raises success from 86.3\% to 92.0\% (48 repairs, four regressions; exact paired $p=1.31\t...
  </details>

- **2026-11-06** — Shervin Shahidi, James Poon, Hang Xie et al. — [AutoRefine: Auto-Calibrating Code Judges from Workflow Outcomes](http://arxiv.org/abs/2611.09291v1)
  <details><summary>📄 Abstract</summary>
  LLM judges increasingly serve as quality gates for code changes that have no test oracle, but a judge prompt must be calibrated for its task and recalibrated as the system it judges evolves, while hand labels for the calibration are resource intensive and go stale. Development workflows emit outcome labels for free (tests pass or fail, changes land or are abandoned), but these labels are noisy. We present AutoRefine, a loop that rewrites a deployable judge's prompt to reproduce outcome labels, w...
  </details>

- **2026-11-06** — Anyuan Zhuo, Shaohua Zhang, Tianle Li et al. — [Cross-Layer TopK: Dynamically Allocating Sparsity Across Layers in Transcoders](http://arxiv.org/abs/2611.09233v1)
  <details><summary>📄 Abstract</summary>
  Cross-Layer Transcoders (CLTs) decompose the activations of large language models into human-interpretable features and trace how these features interact across layers to form circuits, making them a key tool for mechanistic interpretability. However, training CLTs effectively and efficiently is hard. Beyond the usual trade-off between sparsity and reconstruction quality, a CLT has to model all layers at once, which adds a further challenge. The common JumpReLU recipe controls sparsity only indi...
  </details>

- **2026-11-06** — Lorenzo Mannocci, Francesca Naretto, Lucia Passaro et al. — [RAG-Enhanced LLMs for Interactive Explainability in Clinical Decision Support Systems](http://arxiv.org/abs/2611.09232v1)
  <details><summary>📄 Abstract</summary>
  Artificial Intelligence (AI) is increasingly embedded in high-risks decision-making systems across domains such as healthcare, finance, and the judicial system. As reliance on predictive models grows, so does the demand for Explainable AI (XAI) to ensure transparency, trust, and interpretability. However, existing XAI approaches often fail to present explanations in a format accessible to domain experts, limiting their practical utility. Large Language Models (LLMs) have recently emerged as a br...
  </details>

- **2026-11-06** — Sercan Ozcan, Enes Ozgozler, C. Okan Sakar — [Large Language Model Consensus and Corpus-Adaptive Topic Modeling for Classifying and Mapping Patent Innovation](http://arxiv.org/abs/2611.09194v1)
  <details><summary>📄 Abstract</summary>
  Patent analytics increasingly relies on transformer representations and large language models (LLMs), yet linking conceptual classification, topic formation and interpretation requires explicit decisions about model roles and the evidence retained at each stage. In this design-oriented study, we propose and demonstrate a patent analytics pipeline that links these tasks and keeps each decision open to audit. Three LLMs separately classify each patent by novelty (radical or incremental) and innova...
  </details>

- **2026-11-06** — Sarthak Banerjee, Sallam Abualhaija, Domenico Bianculli et al. — [Rethinking Requirement-to-Code Traceability Through Single-Agent and Multi-Agent Approaches](http://arxiv.org/abs/2611.09162v1)
  <details><summary>📄 Abstract</summary>
  Requirements-to-code traceability supports essential software engineering activities, including change impact analysis, maintenance, and regulatory compliance. Existing approaches typically rely on a retrieval-and-classification pipeline, which suffers from an inherent retrieval bottleneck: relevant source files that are not retrieved cannot be recovered during subsequent analysis. In this paper, we revisit requirements-to-code traceability in light of the substantially larger context windows of...
  </details>

- **2026-11-06** — Chen-An Li, Cheng-Han Chiang, Hung-yi Lee — [Improving Large Audio-Language Model Embedding Baselines for Instruction-Aware Speech Retrieval](http://arxiv.org/abs/2611.09122v1)
  <details><summary>📄 Abstract</summary>
  Speech retrieval finds relevant spoken documents given a spoken query. The spoken query alone may not reveal the retrieval goal, such as finding an answer or matching speaker identity. Instruction-aware speech retrieval expresses this goal through a natural-language text instruction. Large audio-language models (LALMs) effectively process speech and text, and our analysis shows that different retrieval requirements favor hidden states from different audio-encoder layers. We introduce IRIS-Embed,...
  </details>

- **2026-11-06** — Ruichen Zheng, Yihe Wang, Fabrice Harel-Canada et al. — [Does Reasoning Improve Psychological Depth in Large Language Models?](http://arxiv.org/abs/2611.09061v1)
  <details><summary>📄 Abstract</summary>
  Benchmark gains from reasoning-enhanced large language models encourage the assumption that these models should broadly perform better on complex generative tasks, but this remains underexplored in open-ended, creative domains shaped by nuances of reader experience. We tested this assumption through the lens of psychological depth in short stories. We compared DeepSeek-R1 vs. DeepSeek-V3, our closest available contrast for reasoning-oriented post-training, and GPT-5 vs. GPT-4o, through 60 blinde...
  </details>

- **2026-11-06** — Sophie Hall, Heinrich H. Nax, Saverio Bolognani — [Fair Selection of Generalized Nash Equilibria: A Comparability Perspective](http://arxiv.org/abs/2611.09060v1)
  <details><summary>📄 Abstract</summary>
  Generalized Nash equilibrium (GNE) problems model self-interested agents coupled through their costs and shared constraints, and arise throughout control applications that allocate a scarce common resource. Such problems typically admit a continuum of equilibria, so any implementation must \emph{select} one. This selection is not neutral: it decides how the cost of the shared constraint is distributed among the agents, a decision often expected to be fair. The variational GNE (v-GNE), which char...
  </details>

- **2026-11-06** — Tianchi Yu, Ivan Oseledets — [Equidistribution of Solution Gradients in Physics-Informed Neural Networks via Coordinate Transformations](http://arxiv.org/abs/2611.09053v1)
  <details><summary>📄 Abstract</summary>
  Physics-Informed Neural Networks (PINNs) often struggle to approximate solutions with sharp gradients due to optimization difficulties and spectral bias. Motivated by the principle of gradient equidistribution from the stretching approach in grid generation, which redistributes solution gradients to reduce functional complexity, we propose Coordinate Transformation PINNs (CTPINNs), which incorporate learnable coordinate transformations to map the physical domain into a computational domain where...
  </details>

- **2026-11-06** — Maryam Rahimimovassagh, Waldemar Karwowski, Niloofar Yousefi — [When Can You Trust Neural Critics? Auditing Mutual Information Estimates of Higher-Order Epistasis in Protein Language Models](http://arxiv.org/abs/2611.09046v1)
  <details><summary>📄 Abstract</summary>
  Mutual information (MI) estimation is used to probe what neural representations encode, including in protein language models, but variational MI estimators have variance that scales at least exponentially in the true MI. We audit a prior neural-MI study of order-resolved epistasis in ESM-2 on the four-site GB1 landscape. Run-to-run differences show no systematic bias and a magnitude comparable to ordinary cross-seed retraining variability, and the evaluation-pairing scheme shifts scores substant...
  </details>

- **2026-11-06** — Lingxiao Zhou, Di Chen, Jia Li — [Sharing the Road: LLM-Based Bargaining in Mixed-Autonomy Traffic](http://arxiv.org/abs/2611.09004v1)
  <details><summary>📄 Abstract</summary>
  Mixed-autonomy traffic involves heterogeneous driving populations competing for shared road space. Previous studies have shown the existence and emergence of collective rationality using game-theoretic and reinforcement learning approaches, which rely on explicitly specified behavioral assumptions or reward functions for driving agents. However, how bargaining behaviors between driving agents evolve and lead to collective outcomes based on richer agent characteristics and language-based reasonin...
  </details>

- **2026-11-06** — Colin Priest — [Same Facts, Different Remedy: Linguistic Profiling and Arbitrariness in LLM and System One Decisions](http://arxiv.org/abs/2611.08995v1)
  <details><summary>📄 Abstract</summary>
  Large language models are increasingly used to resolve consumer complaints, and the way complainants write varies with age, education and socioeconomic status (SES). We audit three remedy-decision systems using sociolinguistic rewrites of US consumer financial complaints that are instructed to preserve every fact: two generative LLMs that return a single label (GPT-4o-mini and GPT-5-mini) and a probabilistic "System One" model that returns a distribution over remedies (Jev). Using pre-registered...
  </details>

- **2026-11-05** — Johannes Brüstle, Simone Di Gregorio, Federico Fusco et al. — [Regret Bounds for Profit Maximization in Bilateral Trade: Learning the Best Posted-Price Mechanism](http://arxiv.org/abs/2611.08173v1)
  <details><summary>📄 Abstract</summary>
  Bilateral trade models the task of intermediating between two strategic agents, a seller and a buyer, willing to trade a good for which they hold private valuations. We study this problem from the perspective of a profit-maximizing broker in a regret minimization framework. At each time step, a new seller and buyer arrive and the broker proposes a trading price to each agent. The trade happens if both agents accept, and the profit of the broker is the difference between the price received from t...
  </details>

- **2026-11-05** — Chenghao Sun, Youhao Lyu, Zizheng Li et al. — [Terrain-Indexed Motion Priors and Geometric Support for Extreme Humanoid Parkour](http://arxiv.org/abs/2611.08056v1)
  <details><summary>📄 Abstract</summary>
  We present a progressive imitation framework that learns terrain-appropriate humanoid parkour skills and subsequently adapts their hand--knee support. Human demonstrations provide traversal behaviors, but their contact patterns need not suit a robot's proportions or the available support surfaces. Our framework changes the role of demonstrations across three stages: privileged imitation produces physically executable robot references; terrain-indexed adversarial motion priors guide skill acquisi...
  </details>

- **2026-11-05** — Margherita Molaro, Matthew M. Graham, Oliver Watson et al. — [Leveraging deep generative modelling at the agent level in discrete-event simulations](http://arxiv.org/abs/2611.07995v1)
  <details><summary>📄 Abstract</summary>
  Emulators are often invoked to facilitate parameter inference in computationally intensive agent-based simulations (ABSs). Most approaches, however, require a large sample of pre-existing outputs on which such emulators can be trained. For computationally intensive simulations, this sample can be prohibitively expensive to generate. We propose a new approach to leverage emulators at the agent level in event-based ABSs to reduce the computational requirements of the simulation itself. We demonstr...
  </details>

- **2026-11-05** — Donghua Zhang, Zizheng Wang, Ze Dong et al. — [MedGraph: Maintaining Patient State with Graph Memory for Long-Term Medical Dialogue](http://arxiv.org/abs/2611.08433v1)
  <details><summary>📄 Abstract</summary>
  LLM-based medical assistants that follow a patient across visits need a memory that keeps the patient's clinical state correct as it changes. We examine the errors of five memory systems on longitudinal medical dialogue and find three recurring causes: the retrieved evidence gives an outdated state, includes another person's health facts, or lacks a safety fact the answer depends on. We present MedGraph, a graph memory built for these three cases. Construction extracts dated facts from each sess...
  </details>

- **2026-11-05** — Vongani H. Maluleke, James Ni, Kie Horiuchi et al. — [Social Humanoid: Socially Responsive Human-Humanoid Interaction](http://arxiv.org/abs/2611.08407v1)
  <details><summary>📄 Abstract</summary>
  Humanoid robots are typically trained as solitary agents, leaving them unable to coordinate physically with human partners who naturally anticipate and adjust to one another. To bridge this gap, we present Social Humanoid, a hierarchical system that generates and executes socially responsive whole-body motion on a 29-DoF Unitree G1 conditioned on a human partner's motion. Its high-level policy performs flexible sequence modeling of human and humanoid motion through a shared tokenized representat...
  </details>

- **2026-11-05** — Yufei Xue, Yushi Huang, Jiawei Shao et al. — [ProQuant: Progressive Quantization-aware Training for Edge MLLMs](http://arxiv.org/abs/2611.08216v1)
  <details><summary>📄 Abstract</summary>
  Multi-modal large language models (MLLMs) with impressive perception and understanding capabilities will enable a range of downstream applications. However, their substantial computational and memory requirements hinder the real-world implementation, particularly for resource-constrained edge devices. Quantization has emerged as an effective solution for deploying large models. While post-training quantization (PTQ) successfully retains the performance at moderate bit-width (e.g., W8A8), it suff...
  </details>

- **2026-11-05** — William Raftery, Dario Farina — [Do sEMG Foundation Models Improve Cross-Subject Generalisation?](http://arxiv.org/abs/2611.08199v1)
  <details><summary>📄 Abstract</summary>
  sEMG Foundation Models aim to learn general purpose representations over diverse subjects and recording conditions that boost performance on a variety of downstream tasks. However, existing evaluations make it difficult to discern whether pretraining alone is sufficient to combat the cross-subject overfitting which makes machine learning on sEMG so challenging. We conduct a systematic evaluation of three sEMG foundation models across three gesture classification datasets under both intra-session...
  </details>

- **2026-11-05** — Kangjie Zheng, Amirhossein Vahidi, Liying Jin et al. — [MUSS: A Multi-scale and Sequence-based Model for Single-cell Gene Regulation](http://arxiv.org/abs/2611.08086v1)
  <details><summary>📄 Abstract</summary>
  Modeling gene regulation in single cells requires jointly representing DNA sequence, chromatin accessibility, and gene expression across regulatory scales. Sequence-based models capture DNA-level regulatory grammar but often lack cell-level resolution, whereas many single-cell omics models represent genes and peaks as fixed-vocabulary tokens without their underlying sequence. Here, we present MUSS, a sequence-based multi-scale model for single-cell gene regulation that preserves both DNA-level a...
  </details>

- **2026-11-05** — Yifan Luo, Zhengying Liu, Yang Yuan et al. — [TCSExam: Evaluating Frontier LLMs on the Full Range of TCS Research](http://arxiv.org/abs/2611.07962v1)
  <details><summary>📄 Abstract</summary>
  Can large language models (LLMs) advance theoretical computer science and resolve its long-standing open conjectures? To study progress toward this goal, we introduce TCSExam, a unified framework and benchmark covering the full range of TCS research. It evaluates theorem proving, solver engineering, and constructions alongside direct attempts to resolve open conjectures, capturing both concrete research accomplishments and progress toward long-standing research goals. TCSExam-Full contains 100 e...
  </details>

- **2026-11-05** — Jincheng Li, Yutian Zhang, Jianyu Zhang et al. — [AffordJEV: Affordance Grounding by Confirming Candidate Regions](http://arxiv.org/abs/2611.07896v1)
  <details><summary>📄 Abstract</summary>
  Affordance grounding asks which visible part of an object performs a requested operation, a basic capability for embodied manipulation and human--robot interaction. Most existing methods follow a System Two paradigm: a multimodal language model first writes a chain of thought and then turns its conclusion into a box or points for a segmenter. This incurs considerable inference cost, gives the semantic decision little direct control over the extent of the final region, and makes mistakes hard to ...
  </details>

- **2026-11-05** — Zhishuo Yang, Li Zhang, Yang Liu et al. — [ReConMem: A Graph-Based Dual Memory System for Repository-Oriented Conversations](http://arxiv.org/abs/2611.07759v1)
  <details><summary>📄 Abstract</summary>
  LLM-based code assistants are increasingly used in iterative repository-level development, where effective assistance requires jointly leveraging evolving conversational history and repository context. Existing memory systems, however, are primarily designed for general-purpose conversations and do not sufficiently coordinate conversational information with the structured code entities to which it refers. We propose ReConMem, a graph-based dual memory system for repository-oriented conversations...
  </details>

- **2026-11-05** — Jaival Chauhan, Vikram Singh, Pruthwik Mishra — [Automated Video-to-QA Pipeline: End-to-End Question Generation and Verification Using Large Language Models](http://arxiv.org/abs/2611.07755v1)
  <details><summary>📄 Abstract</summary>
  The exponential growth of educational and informational video content on platforms like YouTube presents a challenge for efficient knowledge retrieval and assessment. This paper proposes an end-to-end automated pipeline for extracting structured summaries and generating high-fidelity Question-Answer (QA) pairs from video streams. The framework integrates a cascade of state-of-the-art models: audio extraction is handled via FFmpeg, followed by automatic speech recognition (ASR) using Whisper (A l...
  </details>

- **2026-11-05** — Shi Yin, Zujian Dai, Xinyang Pan et al. — [Equivariant Deep Learning in Direct-Product Space for Electronic-Structure Hamiltonian Prediction](http://arxiv.org/abs/2611.07695v1)
  <details><summary>📄 Abstract</summary>
  Most existing equivariant architectures for Hamiltonian prediction propagate features in direct-sum spaces of irreducible spherical tensors, whereas the target Hamiltonian is naturally an operator block in a direct-product representation over local orbital and spin bases. This representation mismatch fragments contiguous Hamiltonian blocks, obscures direct manipulation of orbital couplings, and organizes features into irregular angular-momentum components that require numerous transformations an...
  </details>

- **2026-11-05** — Sai Yashwant, Manoj Kumar Gondimalla, Arjun Sharma et al. — [Redacting Personal Data: A Speed and Accuracy Comparison of Regex, Presidio and Hybrid Designs](http://arxiv.org/abs/2611.07633v1)
  <details><summary>📄 Abstract</summary>
  Many enterprise projects now pass free text to large language models (LLMs), and that text often contains personally identifiable information (PII) such as names, phone numbers, email addresses, home addresses and dates of birth. Once a prompt is sent, this data is copied into provider systems, application logs and observability traces. Redacting PII before the call is an obvious control, yet teams seldom have numbers on what it costs in latency or what it lets through. This paper compares four ...
  </details>

- **2026-11-05** — Pengpeng Qiao, Yang Cao, Lingling Zhang et al. — [Align Before Aggregation: Basis-Consistent Federated LoRA under Heterogeneous Ranks](http://arxiv.org/abs/2611.07598v1)
  <details><summary>📄 Abstract</summary>
  Federated fine-tuning of large language models (LLMs) under heterogeneous client capacities is increasingly important, and low-rank adaptation (LoRA) with heterogeneous ranks makes it practical. Existing server-side aggregators compose local matrix updates $ΔW_i$ from client-specific LoRA factors $(A_i,B_i)$ before aggregating them. Although these matrix updates lie in the same weight space $\mathbb{R}^{m\times n}$ and can be averaged directly, the LoRA factors that generate them may expressed c...
  </details>

- **2026-11-05** — Moonseok Choi, Jongwon Jeong, Minki Kang et al. — [SKIM: Pruning Large Language Model Agents via Selective Knowledge Informed Masking](http://arxiv.org/abs/2611.07558v1)
  <details><summary>📄 Abstract</summary>
  Large Language Model (LLM) agents are increasingly deployed under structured generation, where grammar constraints enforce output format at inference time. Whereas existing compression methods target unconstrained generation, we first identify a fundamental mismatch: under structured generation, grammar constraints reduce the model's output distribution to valid tokens, and the logits matter most at the small set of positions that decide the agent's action. Motivated by this finding, we propose ...
  </details>

- **2026-11-05** — Zhenlong Dai, Zhuoluo Zhao, Xiu Tang et al. — [Enhancing Repository-Level Code Completion with Reinforcement Learning in Real-World Scenarios](http://arxiv.org/abs/2611.07510v1)
  <details><summary>📄 Abstract</summary>
  The rapid development of large language models (LLMs) for code, which closely aligns with the practical needs of real-world software development, has sparked growing attention in repository-level code completion. However, existing Code LLMs present challenges in focusing on suitable contexts from the repository and in deeply reasoning about cross-file dependencies. To address these challenges, we propose a novel reinforcement learning framework for repository-level code completion. To better und...
  </details>

- **2026-11-05** — Pengfei Gu, Huimin Li, Guangyu Meng et al. — [TRiST: Topology-Reinforced Swin Transformer for Medical Image Analysis](http://arxiv.org/abs/2611.07431v1)
  <details><summary>📄 Abstract</summary>
  Medical images contain topological patterns, such as connected components and loops, at scales ranging from small lesions to organ boundaries. Although hierarchical Vision Transformers have advanced medical image analysis, they do not explicitly incorporate topology throughout their multiscale representations. We propose Topology-Reinforced Swin Transformer (TRiST), a framework that integrates topological information into feature construction, refinement, and attention. First, a Hierarchical Mul...
  </details>

- **2026-11-05** — Pavan Kumar Mangipudi, Satya Krishna Pothapragada, Alina Zare et al. — [Deep reinforcement learning-based optimization of multi-RAT handovers](http://arxiv.org/abs/2611.07390v1)
  <details><summary>📄 Abstract</summary>
  A major evolutionary goal and challenge for next-generation wireless systems is seamless multiple radio access technology (multi-RAT) mobility. In a multi-RAT environment, handover decisions must account for both user quality of service and network priorities, including signal quality, resource availability, energy consumption, latency, and security. Although WiFi/cellular mobility is well explored in research and standardization, many conventional handover mechanisms continue to rely primarily ...
  </details>

- **2026-11-05** — Melika Sepidband, Jiho Shin, Song Wang et al. — [How Should Agents See Code? Rethinking Code Representations for Agentic Software Engineering](http://arxiv.org/abs/2611.07286v1)
  <details><summary>📄 Abstract</summary>
  LLM agents are increasingly used for repository-level software engineering tasks. However, most agents still access repositories through raw files, lexical search, and shell commands, treating code primarily as text. This paper investigates map-based code-representation workflows as a design variable in agentic software engineering, examining how different repository views change agents' retrieval behavior, task success, token use, and latency.   In this paper, we study five code-representation ...
  </details>

- **2026-11-05** — Mahdi Arab Loodaricheh, Anita Raja, Indranil SenGupta — [Scenario Augmentation for Rare Financial Events via Multimodal Latent Diffusion](http://arxiv.org/abs/2611.07282v1)
  <details><summary>📄 Abstract</summary>
  Extreme market movements are scarce, heterogeneous, and difficult to learn from imbalanced historical data. We study whether generative augmentation can improve the representation and classification of CVaR-labeled rare financial windows while retaining the complementary structure exposed by different financial representations. Each market window is expressed through three aligned modalities: structured market variables, a spatial image transformation, and a sequence of portfolio returns. Separa...
  </details>

- **2026-11-05** — Yuanchu Liang, Yue Yang, An-Chi He et al. — [Efficient Diffusion Policy Fine Tuning with Latent Noise Representation Bridging](http://arxiv.org/abs/2611.07275v1)
  <details><summary>📄 Abstract</summary>
  Pre-trained diffusion and flow policies have emerged as powerful backbones for robotics, yet adapting them to novel data via reinforcement learning (RL) remains computationally expensive, sample inefficient and lacks theoretical guarantees. Prior approaches that fine-tune the initial noise bypass costly backpropagation through time but struggle with the "noise aliasing" problem: there does not exista natural link between the noise space value and the action space value. This paper resolves these...
  </details>

- **2026-11-05** — Arpit Bahety, Skand Peri, Sriniket Ambatipudi et al. — [OopsieRecover: Learning Transferable VLA Corrections from Semantic Interventions](http://arxiv.org/abs/2611.08462v1)
  <details><summary>📄 Abstract</summary>
  Vision-Language-Action (VLA) models can perform a wide range of robotic manipulation tasks, but often fail during deployment. Teaching them to recover from these failures requires substantial corrective data: existing approaches learn to recover from failures by directly associating corrective actions with the observations in which they were demonstrated. For instance, DAgger-like fine-tuning can require tens to hundreds of interactions, yet the resulting policy may still fail to generalize the ...
  </details>

- **2026-11-05** — Robert Ren, Matthew Bronars, He Zhu et al. — [GPWM: Modeling the World as 3D Particle Motion](http://arxiv.org/abs/2611.08338v1)
  <details><summary>📄 Abstract</summary>
  We introduce GPWM, a Generative Particle World Model that predicts how 3D scenes evolve by generating the motion of particles and rigid bodies over time. Unlike video world models that generate scene appearance, GPWM operates directly in 3D physical space. A single representation and architecture cover rigid, deformable, cloth, and granular materials, in both passive physics and robotic interaction. GPWM is an object-aware multi-resolution transformer that combines flow matching with diffusion f...
  </details>

- **2026-11-05** — Roko Parac, Christos Ziakas, Leo Ardon et al. — [RM-VLM: From Natural-Language Task Descriptions to Vision-Grounded Reward Machines](http://arxiv.org/abs/2611.08308v1)
  <details><summary>📄 Abstract</summary>
  Reward machines (RMs) have been proposed as a reward formulation in reinforcement learning (RL) to capture non-Markovian tasks where credit assignment depends on history. By representing reward functions as automata, RMs expose the task's temporal structure and allow such rewards to be handled within a Markovian framework. However, they assume a labelling function, a proposition-grounding oracle for observations, which must be manually engineered for each environment, limiting their wider applic...
  </details>

- **2026-11-05** — Satvik Sharma, Hengyuan Hu, Mihika Kamat et al. — [RoboARCade: Benchmarking Agentic Robot Control](http://arxiv.org/abs/2611.08209v1)
  <details><summary>📄 Abstract</summary>
  Improvements in multi-modal capabilities have enabled agents to act directly as robot policies, a setting we refer to as agentic robot control (ARC). We introduce RoboARCade, a benchmark of long-horizon manipulation tasks across three embodiments designed to test in-context adaptation, memory, and reasoning for precise control. The tasks build on existing open-source benchmarks, which we make harder by widening the range of initial conditions. RoboARCade is easy to use and extend: all tasks run ...
  </details>

- **2026-11-05** — Qin Guo, Dan Xu — [StitchEdit: Stitching Depth Priors into Image Editors via Per-Layer Gradient Probing](http://arxiv.org/abs/2611.07922v1)
  <details><summary>📄 Abstract</summary>
  Text-guided image editing with diffusion models struggles with spatial edits (e.g. manipulating objects, changing viewpoints, manipulating occlusions) that depend on the 3D structure understanding of a scene. Marigold and follow-up work demonstrate that a pretrained diffusion backbone already harbors strong geometric priors that can be activated for depth estimation, yet how to redirect these priors toward editing remains unresolved. Through per-layer gradient probing, we discover that the editi...
  </details>

- **2026-11-05** — Hao Wu, Yuqi Li, Yizhou Zhao et al. — [Learning Robotic World Models with Semantic and Visual Feedback](http://arxiv.org/abs/2611.07850v1)
  <details><summary>📄 Abstract</summary>
  Robot world models predict action-conditioned future visual states to support robotic planning and decision making. However, visual reconstruction does not fully capture task progress, semantic evaluation alone provides limited constraints on fine-grained visual errors, and homogeneous predictions limit comparative feedback. We present RoboImagine, a framework for post-training autoregressive robotic world models through candidate-future comparisons with semantic and visual feedback. Diverse sea...
  </details>

- **2026-11-05** — Kaiqu Liang, Jaime Fernández Fisac, Thomas L. Griffiths et al. — [The Memory Trap: Language Agents Overgeneralize from Benign Interactions](http://arxiv.org/abs/2611.07554v1)
  <details><summary>📄 Abstract</summary>
  Language agents increasingly use persistent memory to record user preferences and procedures across sessions. We show that memory from benign interactions can cause unsafe or unreliable behavior on later tasks. We call this failure the memory trap. To study this issue, we compare behavior in sessions with and without memory across six frontier models (including Claude Sonnet, Opus, and Fable models and GPT-5.6). We evaluate these models in a range of settings. First, in autonomy experiments, we ...
  </details>

- **2026-11-05** — Chengcheng Wang, Wei He, Wenhao Li et al. — [Concertina: Embodying Manipulation and Cognition in One Diffusion Vision-Language Model](http://arxiv.org/abs/2611.07513v1)
  <details><summary>📄 Abstract</summary>
  Most vision-language-action (VLA) policies decouple manipulation from cognition by bolting an external action mechanism onto a vision-language model (VLM)--either quantizing actions into discrete tokens whose errors bear no stable correspondence to physical displacements, or delegating continuous trajectory generation to a separate action expert whose gradients compete with or are blocked from updating the VLM backbone. We argue that manipulation and cognition should instead be embodied in the s...
  </details>

- **2026-11-05** — Kenneth Llontop, Cherie Ho, Dylan Zhou et al. — [MessyNav: Zero-Shot Navigation via Manipulation in Messy Environments](http://arxiv.org/abs/2611.07417v1)
  <details><summary>📄 Abstract</summary>
  Real-world environments are messy, with paths often blocked by everyday objects like chairs and toys, requiring robots to perform interactive navigation by manipulating obstacles to clear a path. Existing methods rely on extensive simulation-based learning or per-scene instructions specifying which objects to avoid or manipulate. They struggle to generalize across novel objects, diverse environments, and varied contexts such as a cart of fragile glassware that should be avoided while an empty on...
  </details>

- **2026-11-05** — Jonathan Kozaczuk, Zheng Dong, Noyan Evirgen et al. — [User Embeddings are Superpositions of Interpretable Behavioral Modes](http://arxiv.org/abs/2611.08487v1)
  <details><summary>📄 Abstract</summary>
  User embeddings are central components of modern recommendation, personalization, and behavioral modeling systems. Though these embeddings can compactly encode rich behavioral information, they are inherently dense and opaque, limiting interpretability. To address this gap, we argue that user embeddings can be understood as sparse superpositions of interpretable behavioral modes. This structure is directly predicted by generative models of user behavior for linear embeddings and extends approxim...
  </details>

- **2026-11-05** — Margaret-Anne Storey — [Cognitive Tours: Making Understanding a Deliverable in AI-Assisted Development](http://arxiv.org/abs/2611.08456v1)
  <details><summary>📄 Abstract</summary>
  Generative AI and agentic coding are accelerating software development, leading to concerns about technical debt. But two less visible forms of debt, cognitive debt and intent debt, are emerging as key risks to software health. Cognitive debt is the absence or erosion of a team's shared understanding where no one can confidently explain how a system works or predict the impact of a change. Intent debt is the lack of clearly articulated goals, constraints, and rationale that explain what the syst...
  </details>

- **2026-11-05** — Henry Han — [Enhancing Local and Global Structure in Compressed AI Agent Memory](http://arxiv.org/abs/2611.08341v1)
  <details><summary>📄 Abstract</summary>
  AI agents store text as embedding vectors and compress them at scale. A compression is accepted when each item's nearest neighbors survive, but agents also consolidate, delete, and compare memories, tasks that depend on which items lie far apart. We evaluate both ends with two label-free fidelities from our prior work: the local fidelity $L$ at 10 neighbors and the global fidelity $G$ at 30 to 50 percent of the memory. At 96 bytes per passage, rescored binary codes reach an $L$ of 0.97 yet move ...
  </details>

- **2026-11-05** — Fuqing Gao, Yingli Wang, Lingjiong Zhu — [Fluctuations, Moderate and Large Deviations about Hydrodynamic Limits of Space-Time Hawkes Processes](http://arxiv.org/abs/2611.08339v1)
  <details><summary>📄 Abstract</summary>
  We study Gaussian fluctuations, moderate and large deviations around the high-density hydrodynamic limit of critical and nearly critical space-time Hawkes processes initialized by a prescribed Poisson field of past events, with no subsequent immigration. Under a finite mean reproduction delay and centered displacements with finite spatial covariance, a positive cluster-transform estimate yields a distribution-valued central limit theorem (CLT) and a moderate deviation principle (MDP) throughout ...
  </details>

- **2026-11-05** — Kirill A. Bronnikov, Rustam Ibadov, Jutta Kunz — [Instabilities of Simpson-Visser black bounces sourced by a phantom scalar and nonlinear electrodynamics](http://arxiv.org/abs/2611.08322v1)
  <details><summary>📄 Abstract</summary>
  We study the linear stability of Simpson-Visser ``black-bounce'' space-times (regular black holes and wormholes) under spherically symmetric (monopole) perturbations, taking as a source a phantom scalar field with a self-interaction potential and a magnetic field within nonlinear electrodynamics (NED). The metric contains two parameters: the mass $M$ and the bounce parameter $a >0$, such that $a \leq 2M$ corresponds to black holes and $a > 2M$ to wormholes. The stability problem reduces to a bou...
  </details>

- **2026-11-05** — Ali Sarabadani, Kheirolah Rahsepar Fard, Tahereh Jeirani — [Benchmarking Large Language Models on Heterogeneous Cognitive and Biomedical Knowledge Graphs: The Role of Graph Grounding in Multi-Hop Reasoning and Hallucination Mitigation](http://arxiv.org/abs/2611.08315v1)
  <details><summary>📄 Abstract</summary>
  Large language models (LLMs) are increasingly used in biomedical and cognitive neuroscience, but their ability to reason reliably over heterogeneous knowledge graphs (KGs) remains unclear. We benchmark five LLMs (GPT-5.1, Gemini 2.0 Pro, Llama 3, Qwen, and BioGPT) across five KGs: DrugBank, NeuroSynth, Cognitive Atlas, Brain Map, and GDPKG. We introduce a multitier query dataset to evaluate reasoning depth and factual accuracy under KG-aware (graph-grounded) and KG-agnostic conditions. Inter-ann...
  </details>

- **2026-11-05** — Xingyue Shi, Wesley K. G. Assunção — [Hard Issue, Weak Model, or Bad Run? Rethinking Failure Prediction for Coding Agents](http://arxiv.org/abs/2611.08285v1)
  <details><summary>📄 Abstract</summary>
  Trajectory-based failure predictors for software engineering (SE) agents read the partial trajectory of a run to flag whether it is going right or wrong. If it is going wrong, the run can be stopped, retried, or switched to another model. We ask whether these predictors learn anything about the run itself. On public SWE-bench Verified trajectories, where each model attempts each issue once, two run-independent factors dominate predictor performance. The first is issue difficulty: a reference sco...
  </details>

- **2026-11-05** — Wagner Barreto-Souza — [Bounded GARCH Processes](http://arxiv.org/abs/2611.08158v1)
  <details><summary>📄 Abstract</summary>
  We propose a novel class of Bounded GARCH (B-GARCH) processes designed to characterise the conditional heteroskedasticity of continuous time series constrained within a compact interval. While standard GARCH specifications are tailored for R-valued data, many empirical series, such as realised correlation, unemployment rates, expenditure shares, and relative humidity, are bounded. Fitting a traditional GARCH model to such data creates a severe support mismatch, frequently generating predictions ...
  </details>

- **2026-11-05** — Rui He, Philipp Homan, Wolfram Hinzen — [Linguistic boundaries emerge from pressure-constrained processing dynamics](http://arxiv.org/abs/2611.08085v1)
  <details><summary>📄 Abstract</summary>
  Human cognition organizes continuous experience into bounded units while maintaining continuity across them. Linguistic elements are also organized into bounded structural units such as words and phrases, with sentence marking the final bound of a grammatical construction process. How do such boundaries emerge? We propose boundaries emerge from interacting demands to maintain unresolved dependencies, integrate completed relations, and update semantic context, with structural completion allowing ...
  </details>

- **2026-11-05** — Nazmus Sakib Ahmed — [Can an LLM Actually Reason and Program about Neural Network's Weights or is it just memorization on steroids? Exploring "Weight-Space Programming"](http://arxiv.org/abs/2611.08070v1)
  <details><summary>📄 Abstract</summary>
  Large language models (LLMs) have recently been reported to read and write the raw weights of neural networks directly, a capability termed weight-space programming. We ask whether the reading side of this capability reflects reasoning about weight flows or a combination of local arithmetic at the network's edges and memorized priors over public datasets. We test Claude Opus 5.5 on small convolutional networks of about 125,000 parameters trained on five image datasets, providing every weight as ...
  </details>

- **2026-11-05** — Nick Brown, John Dennis — [xDSL-CCPP: An alternative code generator for atmospheric modelling](http://arxiv.org/abs/2611.08060v1)
  <details><summary>📄 Abstract</summary>
  The Common Community Physics Package (CCPP) is a framework designed to simplify the exchange of physics packages between state-of-the-art atmospheric models. A core software component of CCPP is a code generator: a bespoke Python-based application that uses regular expressions to transform an input specification into Fortran source code. While the code generator initially provided a simple transformation capability, the demands of state-of-the-art atmospheric models have resulted in significant ...
  </details>

- **2026-11-05** — Hanyue Shen, Xinling Liao — [Precision - Preserving Subtensor Inference for a 22B Joint Audio - Video Generator under a Fixed GPU Working Set](http://arxiv.org/abs/2611.08023v1)
  <details><summary>📄 Abstract</summary>
  Complete-block offloading reduces model residency but requires each transferred block to fit the GPU budget. We present Precision-Preserving Subtensor Inference (PSI), a fixed-arena runtime that combines sub-block weight streaming with separately managed intermediate state for the BF16 LTX-2.5 22B joint audio-video transformer. The contribution is a construction whose managed GPU footprint is determined by reusable pages, live state, and bounded workspace, together with controls that separate re...
  </details>

- **2026-11-05** — Alexander Hock, Jakob Lindner, Raimar Wulkenhaar — [Universal $x$-$y$ duality in equivariant topological recursion and quartic Kontsevich model](http://arxiv.org/abs/2611.08018v1)
  <details><summary>📄 Abstract</summary>
  Topological recursion is a universal procedure that generates an infinite family of multi-differentials with different interpretations in various areas of mathematics. Recently, a new understanding of topological recursion has emerged from $x$-$y$ duality, which relates two such families through explicit formulae. We study $x$-$y$ duality, its parametrised version, and symplectic duality in the setting of equivariant topological recursion. We explicitly analyse the pole structure of the resultin...
  </details>

- **2026-11-05** — Huanfei He, Bohao Zhang, Jiaxin Zhang et al. — [Rotation Is Token-Blind: A Structural Criterion for Post-Training Quantization of Feed-Forward Geometry Transformers](http://arxiv.org/abs/2611.07955v1)
  <details><summary>📄 Abstract</summary>
  Feed-forward 3D models use Transformers to predict camera poses, depth, and structure in one pass, avoiding iterative multi-view optimization. Long sequences and deep attention incur high compute and memory costs, motivating Post-Training Quantization (PTQ) for deployment. Existing PTQ methods mainly suppress channel-wise outliers by smoothing or orthogonal rotation. Geometry Transformers introduce a different challenge: heterogeneous token types share one activation quantization grid. A few spe...
  </details>

- **2026-11-05** — Cheng Yu, Jim Chi, Aaron J. Snoswell et al. — [How Generative AI Redefines Personalization and Diversity in the Newsroom](http://arxiv.org/abs/2611.07931v1)
  <details><summary>📄 Abstract</summary>
  The tension between news personalization and information diversity has traditionally been understood as a matter of different content reaching different people, with diversity evaluated by the range of sources, topics, and perspectives to which audiences are exposed. Generative AI outdates this understanding, since it transforms personalization in two ways: how journalists adapt news to audiences and how the AI tools journalists use personalize content production to their own preferences. Drawin...
  </details>

- **2026-11-05** — Robin Webbers, Wind Wong, Klaus v. Gleissenthall — [SymFC: Configurable Semantics for All Paths Symbolic Execution in Haskell via Embeddings](http://arxiv.org/abs/2611.07916v1)
  <details><summary>📄 Abstract</summary>
  Lightweight methods like QuickCheck have proven to be successful in functional languages and beyond, as they let users specify properties as Boolean functions directly in code. We can replicate some of their benefits for (bounded) proofs via symbolic execution. If we can execute arbitrary functions symbolically, we can specify properties just as easily. Unfortunately, existing symbolic execution tools for Haskell are restricted to a subset of the language that excludes many real-world applicatio...
  </details>

- **2026-11-05** — Gautam Gupta, Dikshant Kukreja, Unique Kumar et al. — [When Bigger Becomes Brittle: Why Compression Hurts More as Language Models Scale](http://arxiv.org/abs/2611.07891v1)
  <details><summary>📄 Abstract</summary>
  Quantization and pruning reduce the cost of deploying language models, but their effects are usually reported as benchmark scores. Such scores record only the loss that remains at the output. Inside the model, compression damages some components more than others, and the rest of the network can partly compensate. The observed loss therefore reflects both the damage and this compensation, which benchmark scores cannot separate. How the two combine, and whether their balance changes with model siz...
  </details>

- **2026-11-05** — Jisen Lei, Huizhi Liang — [Generate-then-Rank: Learning Symbolic Goal Interpretation for Embodied Agents](http://arxiv.org/abs/2611.07825v1)
  <details><summary>📄 Abstract</summary>
  Goal interpretation is to translate a natural language instruction into a formal symbolic goal that a planner can execute. It is critical for embodied agents because any error here propagates to every downstream planning and action step. Doing it well requires both generating suitable candidates and reliably selecting among them. We present a two-stage generate-then-rank approach to Goal Interpretation in the Embodied Agent Interface (EAI). First, supervised fine-tuning adapts a Large Language M...
  </details>

- **2026-11-05** — Ayal Klein — [Decodability Is Not Validity: Evaluating Nuisance Sensitivity in Language Model Concept Probes](http://arxiv.org/abs/2611.07805v1)
  <details><summary>📄 Abstract</summary>
  Two concept probes can be equally accurate at predicting a concept from a language model's hidden states while their scores contain different mixtures of the target concept and a correlated nuisance attribute. In four target--nuisance settings (two aspect sentiments in CEBaB; occupation and gender in BiasBios; Amazon review sentiment with negation, and with first-person framing), two LLMs, and a population of concept extractors, we compare decodability with discriminant evidence: the score's dep...
  </details>

- **2026-11-05** — Sam Power — [Geometric Functional Inequalities for Markov Processes: An Invitation via the Langevin Diffusion](http://arxiv.org/abs/2611.07785v1)
  <details><summary>📄 Abstract</summary>
  Functional inequalities provide a language for reasoning about the long-time properties of ergodic Markov processes in terms of their macroscopic geometry. This article offers an informal introduction to functional inequalities for readers who are more familiar with probabilistic tools based around couplings, Lyapunov techniques, and similar. The main ideas are developed through the overdamped Langevin diffusion, where various functionals related to this convergence admit particularly transparen...
  </details>

- **2026-11-05** — Zehao Wang — [ConvPE: Convolutional Position Embedding Improves Transformers](http://arxiv.org/abs/2611.07749v1)
  <details><summary>📄 Abstract</summary>
  ConvPE (Convolutional Position Embedding) improves both the performance and efficiency of Transformer models in language modeling, long-context extension, and vision. It injects a windowed, content-dependent bias into attention scores through a lightweight causal convolution over a low-dimensional projection of the hidden states. As a lightweight plug-in, ConvPE is compatible with RoPE, attention masks, and KV concatenation. It also supports high-dimensional position embeddings via high-dimensio...
  </details>

- **2026-11-05** — Yuxuan Yao, Harald Oberhofer, Karsten Reuter et al. — [Graph Symbolic Distillation: Decoding Graph Data into Interpretable Formulas across Materials and Chemistry](http://arxiv.org/abs/2611.07719v1)
  <details><summary>📄 Abstract</summary>
  Graph data provide a natural representation of the interconnected structures and interactions underlying many chemical and materials systems. Graph neural networks (GNNs) can learn complex relationships from such data, yet translating these representations into interpretable descriptors and scientific insights remains challenging. Here we introduce graph symbolic distillation (GSD), a framework for decoding graph data into interpretable symbolic formulas. GSD identifies task-relevant message-pas...
  </details>

- **2026-11-05** — Yu Cao, Haiyan Xu, Xiaohan Li et al. — [Pediatric ECG foundation model via adult-to-pediatric fine-tuning: downstream tasks and clinical evaluation](http://arxiv.org/abs/2611.07717v1)
  <details><summary>📄 Abstract</summary>
  Pediatric electrocardiogram (ECG) interpretation is complicated by age-dependent electrophysiological changes that limit direct transfer of adult AI models. We asked whether an adult ECG foundation model could be adapted to pediatric ECGs. Using 339,563 12-lead ECGs from 238,189 children, we compared direct application, pediatric fine-tuning, and training from scratch under an identical architecture. Direct transfer was poor (mean AUC 0.8256). Fine-tuning reached 0.9695, above de novo training (...
  </details>

- **2026-11-05** — Amelie Schatull, Torge Kolditz, Simon Kleinschmidt et al. — [Towards Track Height Control in Additive Manufacturing on Porous Substrates: An Approach for System Identification and Controller Selection](http://arxiv.org/abs/2611.07704v1)
  <details><summary>📄 Abstract</summary>
  Additive manufacturing is transforming the creation of materials and parts, enabling the design and manufacturing of multifunctional parts with tailored properties. One compelling example is the combination of a porous core and a non-porous surface, which offers significant advantages in terms of weight reduction, material efficiency, strength and wear resistance. Directed Energy Deposition (DED) processes enable the transition from porous core to non-porous part surface by closing the pores. Ho...
  </details>

- **2026-11-05** — Hangyu Qin, Junbin Xiao, Angela Yao — [ReferClaw: Disambiguating User Intent for Egocentric Assistance](http://arxiv.org/abs/2611.07683v1)
  <details><summary>📄 Abstract</summary>
  Users of egocentric AI assistants often ask short, ambiguous questions whose intended referents cannot be uniquely resolved from video and dialogue history. For example, "Where did I leave it?" may refer to several previously handled objects. Existing VideoQA systems typically commit to a single interpretation, risking plausible but intention-misaligned answers. We introduce ReferClaw, an agentic framework that formulates egocentric streaming QA as an interactive process: the assistant asks clar...
  </details>

- **2026-11-05** — Yunwan Fu, Sicheng He, Jiageng Mao et al. — [PhySA: Decoupling Aesthetic and Physical Rewards for Humanoid Locomotion](http://arxiv.org/abs/2611.07679v1)
  <details><summary>📄 Abstract</summary>
  Humanoid locomotion policies trained without an explicit smoothness objective tend to produce jerky, high-energy gaits that stress actuators. Vision-language models (VLMs) offer an appealing reward source: given a rendered rollout, a VLM returns an aesthetic quality score on [0,10] without task-specific feature engineering. We find, however, that aesthetic preference and physical smoothness point in opposite directions: across four production VLMs, clips with higher joint acceleration receive hi...
  </details>

- **2026-11-05** — Giorgio Monaco, Jacopo Lenti, Francesco Pierri — [The Popular Get More Popular: Auditing Brand Bias in Generative Search](http://arxiv.org/abs/2611.07614v1)
  <details><summary>📄 Abstract</summary>
  The shift from traditional to generative search has fundamentally transformed online product discovery. Because conversational recommendations synthesize choices into a few direct answers, subtle systemic preferences toward specific providers can exert profound commercial impacts. In this work, we audit this phenomenon through two distinct dimensions: (i) brand popularity bias, the systematic preference for market-dominant entities over long-tail alternatives, and (ii) brand familiarity bias, th...
  </details>

- **2026-11-05** — Zhuangsheng Li, Liang Dong, Yu Wu et al. — [What Gets Hacked in a Collaborative Reward for LLM Recommenders: The Part That Does Not Depend on the User](http://arxiv.org/abs/2611.07588v1)
  <details><summary>📄 Abstract</summary>
  Collaborative-filtering (CF) scores provide graded, personalized rewards for training large language model (LLM) recommenders through reinforcement learning. However, these rewards can cause exposure collapse: even though the CF model itself produces diverse top recommendations across users, an LLM optimized with its rewards concentrates on fewer items. We decompose each score into an item-mean component, the item's average CF score across user histories, and a residual component, the current us...
  </details>

- **2026-11-05** — Ramesh Pramanik, Shradha Mishra, Sakuntala Chatterjee — [Autotaxis of a Run-and-Tumble Agent via Reinforcement Learning](http://arxiv.org/abs/2611.07531v1)
  <details><summary>📄 Abstract</summary>
  We study the run-tumble motion of a single autochemotactic agent that secretes and senses chemical cues using a reinforcement learning (RL) framework. In a chemical environment that changes dynamically via secretion, diffusion, and degradation of attractant chemicals, we study the effectiveness of RL for a successful navigation strategy. We show that RL enhances chemotactic performance. Starting from a random initial position, the probability of finding the agent in the favorable region (near th...
  </details>

- **2026-11-05** — Yuri Yu. Tarasevich — [Electrical conductivity of a two-dimensional two-component medium: discretization and effective medium approximation](http://arxiv.org/abs/2611.07491v1)
  <details><summary>📄 Abstract</summary>
  The effective conductivity of a two-dimensional two-component medium is studied within a discretization scheme and the effective-medium approximation (EMA). A square lattice is superimposed on a random isotropic medium; each cell is assigned the conductivity of its majority component, and the cell is replaced by a star of four resistors. Neighboring cells are connected by an equivalent resistor whose conductivity is $σ_1$, $σ_2$, or the harmonic mean $σ_{12}=2σ_1σ_2/(σ_1+σ_2)$, with probabilitie...
  </details>

- **2026-11-05** — Kihyun Na, Injung Kim — [ReviewMap: Mapping Evaluative Acts and Automation Boundaries in Peer-Review Comments](http://arxiv.org/abs/2611.07489v1)
  <details><summary>📄 Abstract</summary>
  Peer-review comments check what a paper does and judge why it matters, but no existing scheme distinguishes these two evaluative acts. We argue that making these acts explicit and measuring how reliably LLMs identify them is a prerequisite for responsible LLM-assisted review analysis: humans need to inspect review judgments and their grounds. This defines a more honest mission for NLP in peer review than full automation. We present ReviewMap, a framework that classifies each comment as assessmen...
  </details>

- **2026-11-05** — Yupeng Cao, Xueqing Peng, Lingfei Qian et al. — [FINCOSMOS: An Open-World Evaluation Paradigm for Agents in Finance](http://arxiv.org/abs/2611.07464v1)
  <details><summary>📄 Abstract</summary>
  Language agents increasingly work for users on the open Web, and finance is where trusting them is hardest. The data must come from the Web, the strategy lives in the user's head, and correctness depends on time, so an agent can fail silently: a strategy the user never asked for, unverified data, or a backtest that uses the future yields a report as convincing as a correct one. Existing benchmarks close the world somewhere, fixing the task, the data, or the timeline, and thereby remove these fai...
  </details>

- **2026-11-05** — Sheng Jin, Wentao Liu, Chen Qian — [Vis2State: Visual Reasoning through Executable State Abstractions](http://arxiv.org/abs/2611.07397v1)
  <details><summary>📄 Abstract</summary>
  Solving visual puzzles requires both accurate interpretation of visual evidence and reliable computation under task-specific rules. Embedding visual assumptions and task constraints directly in solving code makes the represented problem difficult to inspect and revise independently. We introduce Vis2State, a training-free agentic framework that abstracts visual puzzles into explicit, revisable problem states linking visual inspection and execution. Visual inspection guides state construction and...
  </details>

- **2026-11-05** — Changwei Du, Linhui Li, Huijuan Ma et al. — [A Unified Coordinate Descent Framework for Penalized Longitudinal Log-Contrast Quantile Regression](http://arxiv.org/abs/2611.07379v1)
  <details><summary>📄 Abstract</summary>
  Quantile regression characterizes heterogeneous covariate effects across the response distribution, but its extension to high-dimensional longitudinal compositional data poses substantial challenges, such as the nonsmooth check loss, the unit-sum structure of compositional covariates. Existing work is confined to Lasso penalization, and does not readily extend to nonconvex penalties. We propose CDaLCqr, a unified coordinate descent algorithm for penalized longitudinal log-contrast quantile regre...
  </details>

- **2026-11-05** — Nicolas Hernandez, Ben D. Normann, Yeinzon Rodriguez — [Self-interacting $p$-forms and the shear-free anisotropic cosmological model](http://arxiv.org/abs/2611.07288v1)
  <details><summary>📄 Abstract</summary>
  The cosmological principle may require more than observations demand: what is needed is isotropic expansion without vorticity. Extended Friedmann-Lemaitre-Robertson-Walker (eFLRW) cosmologies realise this with a non-vanishing anisotropic spatial curvature that is balanced by an anisotropic stress while the shear vanishes. Thorsrud and others investigated such scenarios for free differential $p$-forms. Here we extend the analysis to non-Abelian $p$-forms ($p=0,\dots,4$) with self interactions. Th...
  </details>

- **2026-11-04** — Gabriele Donno, Kashif Mehmood, Katina Kralevska — [Authorization Propagation in Agent2Agent Systems: An Experimental Security Evaluation of Multi-Hop Delegation](http://arxiv.org/abs/2611.07050v1)
  <details><summary>📄 Abstract</summary>
  Delegated Agent2Agent (A2A) workflows create a security problem when the agent sending a request is different from the principal from which the authority originated. This paper evaluates a layered downstream-verification design in a synthetic four-party healthcare reimbursement workflow. The prototype separates current-caller context, transitive authorization evidence, per-hop Ed25519 request authentication, and independent replay state for requests and authorization artifacts. Of 15 adversarial...
  </details>

- **2026-11-04** — Rachel Lea Draelos — [Matriarchy Classics: A Computational Approach to Swap Only Gendered Words in Classic Novels](http://arxiv.org/abs/2611.07134v1)
  <details><summary>📄 Abstract</summary>
  This paper proposes a trustworthy computational method to gender-swap public domain novels, with programmatic guarantees that only gendered words are inverted and all other words are left unchanged. This may seem like a simple task, but both large language models and naive rule-based methods fail to complete it. The proposed method includes a custom whitespace-preserving tokenizer, gender-swap mappings across plural and possessive forms, pronoun handling, and a character renaming strategy. It sh...
  </details>

- **2026-11-04** — Tamás Janusko, Sven Kleinkop, Ricardo Bochnia et al. — [Adapting LLM Judges to Observed Human Annotation Policy through Soft Prompt Tuning](http://arxiv.org/abs/2611.07126v1)
  <details><summary>📄 Abstract</summary>
  Large Language Models (LLMs) are increasingly employed as automated judges for evaluating chatbot responses. While proprietary models can achieve high agreement with human annotators, they remain costly and difficult to deploy in practical settings. Lightweight open-source LLM judges provide an attractive alternative but typically exhibit lower agreement with human ratings. In this paper, we investigate whether soft prompt tuning can align open-source LLM judges more closely with human annotatio...
  </details>

- **2026-11-04** —  Doyeol,  Ahn — [Field-aligned measurement removes the anisotropy barrier of sample-based quantum subspace solvers for magnetized-plasma heat conduction](http://arxiv.org/abs/2611.07102v1)
  <details><summary>📄 Abstract</summary>
  Sample-based quantum subspace methods construct a small subspace from measured basis states and solve the target problem classically within it. We study these methods for heat conduction in magnetized plasmas, where the anisotropy $χ_\parallel/χ_\perp$ reaches $10^8$ to $10^{10}$. We prove two results for the energy-norm Galerkin solution. First, if the measurement basis is aligned with the flux surfaces and the subspace contains the poloidal-mode-zero block, the error is bounded by $\|r_0\|_{L^...
  </details>

- **2026-11-04** — Hongyu Cao, Guangfu Guo, Jinghan Zhang et al. — [Segment What It Can Draw: Querying a Text-to-Image Generator with Its Own Images for Skin Lesion Segmentation](http://arxiv.org/abs/2611.07061v1)
  <details><summary>📄 Abstract</summary>
  Skin lesion segmentation without annotated masks requires the target to be specified through other cues. Existing approaches rely on dermoscopy-specific rules, annotation-derived model priors, or user-selected regions. A general text-to-image diffusion transformer offers a text interface to the target, but its concept-word attention is unreliable on dermoscopy images: in the model's attention-output space, the word-derived skin-to-lesion direction is poorly aligned with the direction separating ...
  </details>

- **2026-11-04** — Andrew W. Lo, Chaoyi Zhao — [Adapting the Process of Adaptation: Darwinian, Lamarckian, and Agent-Directed Evolution in AI](http://arxiv.org/abs/2611.07048v1)
  <details><summary>📄 Abstract</summary>
  Evolution has shaped intelligence for billions of years. Artificial intelligence (AI) now raises a striking possibility: intelligence may begin to direct its own evolution. As AI agents become capable of modifying and evaluating their own behavior, how quickly could they improve, and how can that improvement remain safe? We develop a theoretical framework comparing Darwinian, Lamarckian, and agent-directed evolution following environmental change. Darwinian evolution relies on natural selection,...
  </details>

- **2026-11-04** — Xiuyuan Qi, Pedro Reviriego, Javier Conde et al. — [BlockLock: Reproducible LLM Inference with Fixed Batch Geometry](http://arxiv.org/abs/2611.06977v1)
  <details><summary>📄 Abstract</summary>
  Reproducible LLM inference requires that a request produces the same output regardless of the other requests in the batch. Existing solutions pay for this in different ways: batch-invariant kernels constrain every operator, and isolating prefill with fixed-shape decode ({our CoRun-style baseline}) gives up shared prefill compute and pads decode. We present BlockLock, which keeps shared batched prefill and pins only the numerical path of the protected request: it fixes the geometry that the reque...
  </details>

- **2026-11-04** — Zi-Jian Cheng, Weiming Wu, Jie Meng et al. — [KDASO: Knowledge-Data Dual-Driven Automated Skill Optimization for Liability Adjudication Tasks](http://arxiv.org/abs/2611.06972v1)
  <details><summary>📄 Abstract</summary>
  Liability adjudication tasks (e.g., legal charge determination) require analyzing event descriptions against domain-specific skills to determine whether a party should bear liability. While Large Language Models (LLMs) have shown promise in this area by leveraging executable skills for interpretable reasoning, existing approaches face three critical limitations: skill libraries become stale as real-world scenarios dynamically evolve, skill descriptions often suffer from a semantic execution gap ...
  </details>

- **2026-11-04** — Divyanshu Mishra, Sabine Sternig, Rakshith Shetty et al. — [Grounding in the Dark: Text-Only Training for Zero-Shot Video Temporal Localization](http://arxiv.org/abs/2611.06149v2)
  <details><summary>📄 Abstract</summary>
  Video-LLMs are typically trained on paired video-text data for temporal tasks, yet collecting precise temporal annotations and training on large-scale video datasets are both costly. We investigate whether a text-only LLM, with no vision-language pretraining, can be trained on textual video descriptions alone to perform temporal grounding and receive video only at inference time. This setting removes paired video data from training altogether and is a step toward training multimodal models witho...
  </details>

- **2026-11-04** — Imed Bouazizi — [Characterizing AI Service Traffic for 6G: An Open Testbed and Initial Results from 3GPP SA4](http://arxiv.org/abs/2611.07250v1)
  <details><summary>📄 Abstract</summary>
  The design of sixth generation (6G) mobile systems requires measurements of artificial intelligence (AI) service traffic under controlled network conditions. The 3rd Generation Partnership Project (3GPP) Service and System Aspects Working Group 4 (SA4) documents such measurements in draft Technical Report 26.870. In this paper, we describe the open testbed used for the study and analyze the results recorded in version 0.6.2 and its companion workbook. The testbed combines network emulation, pack...
  </details>

- **2026-11-04** — Mingyang Jiang, Yamin Li, Fan Ma et al. — [Backbone-Informed Adaptation after EEG Pretraining: A Capacity-Controlled Study](http://arxiv.org/abs/2611.07192v1)
  <details><summary>📄 Abstract</summary>
  Electroencephalography (EEG) foundation models learn representations that combine information across channels and time. This structure motivates adapters that model the same relationships during downstream learning. However, it is not clear whether such a design outperforms other candidate adapters. Moreover, in order to arrive at a fair comparison between candidate adapters, we also need to consider their trainable parameters. Here, we ask whether a backbone-informed (native) adapter makes bett...
  </details>

- **2026-11-04** — Vikram Krishnamurthy, Yiming Zhang, Luke Snow — [Stochastic Dynamics of Generative AI: From Autoregressive Models to Interacting LLM Networks and Neural SDEs](http://arxiv.org/abs/2611.07065v1)
  <details><summary>📄 Abstract</summary>
  This paper develops a stochastic dynamical-systems perspective on three classes of generative AI models. First, we formulate large language models (LLMs) as high-dimensional nonlinear autoregressive models with attention-based dependencies. This formulation connects pretraining by conditional maximum likelihood to sequential token generation and provides a probabilistic interpretation of LLM operation. Second, we consider networks of interacting LLMs and characterize their collective behavior th...
  </details>

- **2026-11-04** — Luis D. S. Silva, Arthur M. S. Carvalho, Francisco A. G. Almeida et al. — [Langmuir kinetics and totally asymmetric volume exclusion in linear chains via Fock space formalism](http://arxiv.org/abs/2611.07053v1)
  <details><summary>📄 Abstract</summary>
  Driven-diffusive systems combining spatial exclusion and bulk exchange, such as the totally asymmetric simple exclusion process coupled with Langmuir kinetics (TASEP-LK), serve as foundational models for particle transport in vehicular traffic, conveyor networks, and mesoscopic flow channels. In this work, we employ an exact Doi-Peliti field-theoretic operator formulation in Fock space to evaluate steady-state observables, continuous phase landscapes, and spatial correlations in finite linear ch...
  </details>

- **2026-11-04** — Mengni Jia, Mengyu Zhou, Xiaoxi Jiang et al. — [Reward Budgeting Reduces Premature Convergence in Reinforcement Learning for LLM Reasoning](http://arxiv.org/abs/2611.05942v2)
  <details><summary>📄 Abstract</summary>
  RL for LLM reasoning often reaches an early performance plateau as the policy distribution becomes increasingly sharp. Recent work has studied policy entropy as both a diagnostic and a control signal for this behavior. In our experiments, however, increasing entropy alone does not reliably change the eventual plateau. We analyze RL through its implicit target policy and derive a sharpness factor $κ$, together with an effective counterpart $κ_{\mathrm{eff}}$, that describes how strongly reward or...
  </details>

- **2026-11-04** — Georgios Feretzakis, Alexandros Papaspyridis — [Signed but Steerable: Measuring and Closing the Text-Vector Integrity Gap in Offline Retrieval-Augmented Generation](http://arxiv.org/abs/2611.06498v1)
  <details><summary>📄 Abstract</summary>
  Offline retrieval-augmented generation (RAG) on edge devices is updated through signed knowledge packs that carry text and precomputed embedding vectors. A signature proves who published a pack, not that its vectors encode its text. We study this text-vector integrity gap. A verifier that recomputes vectors and accepts them within a cosine tolerance concedes a predictable share of queries to an attacker who controls the vectors: the hijack rate equals the distribution of angular retrieval margin...
  </details>

- **2026-11-04** — Lorenzo Porcelli — [Clear Human Web: Where a Person Vouches for Every Client](http://arxiv.org/abs/2611.06286v1)
  <details><summary>📄 Abstract</summary>
  The web cannot tell whether a request comes from a person or from a program. Sites have checked the network address and puzzles in its place, and both have given way: automated traffic exceeds human traffic, and puzzles are solved for pay and by agents. This paper proposes the Clear Human Web, the part of the public web that sites open only to clients a person vouches for. A person's wallet presents their person identification data (PID) to one issuer, the only party that registers as a relying ...
  </details>

- **2026-11-04** — Pragyan Phukan — [AssameseLM-E2B: An Open-Weight Assamese Language Model for Efficient Consumer-Grade Deployment](http://arxiv.org/abs/2611.06170v1)
  <details><summary>📄 Abstract</summary>
  While Large Language Models (LLMs) excel in high-resource languages, their performance often degrades in low-resource languages due to tokenization inefficiencies, generative instability, and linguistic interference. This paper presents AssameseLM-E2B and its instruction-tuned variant, AssameseLM-E2B-it, a 2-billion-parameter model adapted specifically for low resource Assamese language. Built upon the Gemma-4 architecture, the model incorporates an expanded byte-level BPE vocabulary to reduce t...
  </details>

- **2026-11-04** — Bingran You, Wenjun Ke, Ria Rosenauer et al. — [FrontierPhysics: Evaluating Agents for End-to-End Physics Research](http://arxiv.org/abs/2611.06910v1)
  <details><summary>📄 Abstract</summary>
  AI agents are playing an increasingly important role in physics research. However, existing physics benchmarks only evaluate fixed questions, isolated sub-tasks, or paper reproduction with given solutions, and rarely check research quality alongside correctness. We introduce FrontierPhysics, an end-to-end benchmark with 56 tasks made by 42 physicists based on their own research, covering nine domains across theoretical, computational, and experimental physics. Each task requires agents to review...
  </details>

- **2026-11-04** — Peidi Dong, Yunze Xiao, Yu-Lin Tsai et al. — [Before You Continue: Evaluating Time-Sensitive Safety Awareness in Conversational Assistants](http://arxiv.org/abs/2611.06839v1)
  <details><summary>📄 Abstract</summary>
  Large language model (LLM) assistants increasingly help users with everyday activities that involve time-dependent constraints. However, users may not mention these constraints in later requests, requiring assistants to recognize and adjust their advice accordingly. To evaluate such capability, we introduce TASC (Temporal Action Safety in Conversation), a benchmark that evaluates whether LLMs apply time-dependent constraints when responding to conversational requests. TASC consists of 3,418 inpu...
  </details>

- **2026-11-04** — Man-Ling Sung, Hemanth Kandula, Jeff Ma et al. — [SAUCE: Summary Analysis Using Conversation Entailment](http://arxiv.org/abs/2611.06812v1)
  <details><summary>📄 Abstract</summary>
  With the growing need for evaluating Large Language Models (LLMs) and their applications to speech, challenges persist in summarizing and evaluating conversations that lack a clear end goal. We introduce SAUCE -- a reference-free, fact-based evaluation pipeline for cross-lingual conversational speech summarization. It measures the accuracy and the fact coverage of a summary through the entailment between conversation and text. We compare SAUCE against several popular summarization metrics and de...
  </details>

- **2026-11-04** — Sachin Gupta — [AgentTrustCI: Build-Time Policy, Grounding, and Trajectory Tests for Java LLM Agents](http://arxiv.org/abs/2611.06674v1)
  <details><summary>📄 Abstract</summary>
  Infrastructure security does not establish whether an LLM agent selected an allowed tool, grounded its answer in tool output, or followed a required workflow. AgentTrustCI is a Java/JUnit 5 framework that expresses these application-layer expectations as policy, grounding, and trajectory checks over recorded traces. A deterministic replay implementation supports repeatable build-time tests; a judge interface provides an extension point for optional semantic evaluation. On 55 synthetic cases span...
  </details>

- **2026-11-04** — Thomas Christian Joos, Azza Bouleimen, Anikó Hannák et al. — [Perceived Trust and Transparency in AI-Altered vs. Human-Written LinkedIn Posts](http://arxiv.org/abs/2611.06660v1)
  <details><summary>📄 Abstract</summary>
  People increasingly draft a social media post themselves and then let an AI model refine it (AI-altered), a common but understudied middle case between fully human-written and fully AI-generated content. We ask whether this changes how trustworthy and transparent readers perceive the post to be, and whether they can even tell. We first analyze real ChatGPT conversations (WildChat) to find how people actually alter social media posts, which we use to design realistic alteration prompts. We then r...
  </details>

- **2026-11-04** — Sourav Selvaraj, Juan Pablo Espinosa Chessal, Mahdi Agheli — [SCRUB: Contact-Based Surface-Frame Estimation for Force-Motion Control with an Armless Quadruped](http://arxiv.org/abs/2611.06649v1)
  <details><summary>📄 Abstract</summary>
  Wiping, sanding, and inspection robots press a sliding tool on a surface with controlled force. Controlling that force needs the surface normal, which is unknown on real-world, unmapped surfaces. Surface-normal estimators can help estimate the surface normal, but they either need a friction model or assume that the instantaneous tool velocity lies along the surface; however, walking violates this assumption. We propose SCRUB, a contact-based surface-frame estimator, which lets an armless quadrup...
  </details>

- **2026-11-04** — Yuetong Liu, Zhehao Zhou, Yitong Zhang et al. — [Tools Need Not Speak in Text: Latent Context Compression for Agents](http://arxiv.org/abs/2611.06500v1)
  <details><summary>📄 Abstract</summary>
  Large language model (LLM) agents typically append raw tool outputs to their context. Over multi-step interactions, long and noisy observations incur substantial context overhead and dilute the agent's attention to task-relevant information. Existing token pruning and summarization methods remain constrained by discrete text representations, limiting the achievable compression ratios.   In this work, we challenge the prevailing assumption that agents must consume tool observations as explicit te...
  </details>

- **2026-11-04** — Boyu Niu, Yingjie Xiong, Shurui Li et al. — [AmbiHTMLBench: A Benchmark for HTML-based Visually Rich Document parsing](http://arxiv.org/abs/2611.06449v1)
  <details><summary>📄 Abstract</summary>
  Traditional document parsing systems use Markdown as their output representation, which is effective for linear text but does not fully preserve fine-grained spatial structure, table geometry, visual hierarchy, or rendering semantics. We show that HTML is advantageous for heterogeneous and layout-sensitive documents whose representations must remain editable, inspectable, and reusable, and introduce AmbiHTMLBench to systematically study this setting. In this benchmark, given a real-world documen...
  </details>

- **2026-11-04** — Zhuang Zhao, Jiongchi Yu, Yao Zhang et al. — [Keeping Fuzzers on Duty: Repairing Fuzzing Build Breakages in Continuous Open-Source Fuzzing](http://arxiv.org/abs/2611.06358v1)
  <details><summary>📄 Abstract</summary>
  Continuous fuzzing platforms such as OSS-Fuzz provide sustained security testing for open-source projects, but long-term build breakages reduce security coverage and waste infrastructure resources. In OSS-Fuzz, around 20% of integrated projects remain in build-failure states, leaving their fuzzers off duty. These failures expose a maintenance gap between platform maintainers, who lack project-specific context, and project maintainers, who often lack fuzzing and infrastructure expertise. Existing...
  </details>

- **2026-11-04** — Jinhua Wu, Yuting Wang, Zhemin Chen — [Verified Implementation of the Next-gen Borrow Checking Algorithm for Rust via Abstract Interpretation](http://arxiv.org/abs/2611.06319v1)
  <details><summary>📄 Abstract</summary>
  Borrow checking is a central mechanism for Rust to ensure temporal memory safety. Its correctness is based on the intuition that the Aliasing XOR Mutability discipline guarantees that programs without borrow errors inherently could not access invalid references (i.e., pointers). However, existing work on formalizing borrow checking treats it either as a component of type systems or as symbolic execution describing resource transfer. None provides a direct explanation of the correctness of borrow...
  </details>

- **2026-11-04** — Xin Liu, Hongru Song, Ruqing Zhang et al. — [CLEAR: Structured Specifications for Controllable Long-Horizon ML Research Engineering](http://arxiv.org/abs/2611.06263v1)
  <details><summary>📄 Abstract</summary>
  Large language model (LLM) agents are increasingly being used to automate machine learning (ML) research workflows, ranging from code development and experiment execution to research reproduction and scientific discovery. Recent systems demonstrate that LLMs can perform substantial portions of ML research engineering with limited human intervention. These advances suggest a shift from automating individual research tasks toward automating long-horizon workflows that transform research artifacts ...
  </details>

- **2026-11-04** — Divyanshu Mishra, Sabine Sternig, Rakshith Shetty et al. — [Grounding in the Dark: Text-Only Training for Zero-Shot Video Temporal Localization](http://arxiv.org/abs/2611.06149v1)
  <details><summary>📄 Abstract</summary>
  Video-LLMs are typically trained on paired video-text data for temporal tasks, yet collecting precise temporal annotations and training on large-scale video datasets are both costly. We investigate whether a text-only LLM, with no vision-language pretraining, can be trained on textual video descriptions alone to perform temporal grounding and receive video only at inference time. This setting removes paired video data from training altogether and is a step toward training multimodal models witho...
  </details>

- **2026-11-04** — Mingkang Liu, Peipei Jiao, Weiming Meng et al. — [UniCompress: From Multi-LoRA Experts to One Compact Model for Edge Intelligence](http://arxiv.org/abs/2611.06075v1)
  <details><summary>📄 Abstract</summary>
  Embodied and edge systems increasingly rely on vision-language models (VLMs) to support heterogeneous skills, yet deploying a separate task adapter for each skill while retaining a high-precision backbone creates substantial memory and management costs. We present UniCompress, a deployment-oriented framework that converts multi-task expertise into one compact, adapter-free model. Starting from a consolidated BF16 Qwen3-VL-4B teacher, UniCompress constructs an asymmetric INT2 student using GPTQ i...
  </details>

- **2026-11-04** — Shuo Liu, Hao Ning, Jacky Keung et al. — [SynMOE: A Syntax-Aware MOE-Guided Approach for PEFT-Based Code Intelligence Learning](http://arxiv.org/abs/2611.06069v1)
  <details><summary>📄 Abstract</summary>
  Parameter-Efficient Fine-Tuning (PEFT) has emerged as an important approach for adapting Language Models (LMs) in downstream tasks. However, in the domain of code intelligence, the performance of most PEFT methods relatively drops compared to Full fine-Tuning (FT), hindering their broader applicability. One of the main reasons is that current PEFT methods are generally based on assumptions about the low-rank nature or sparsity of parameter updates, lacking explicit modeling of code-related infor...
  </details>

- **2026-11-04** — Yuliang Liu, Xinyu Wang, Xiang Bai — [Familiar letters, not related languages, let unseen languages into a shared space of meaning](http://arxiv.org/abs/2611.06006v1)
  <details><summary>📄 Abstract</summary>
  Hundreds of languages have written text but almost no translations, and whether a model learning one from untranslated text builds on a related language or familiar letters is unclear: they usually coincide. Here we show that familiar letters, not a related language, let an unseen language into a shared space of meaning. GlyphMind, a tokenizer-free vision transformer that reads text as pixels and lets any sentence be shown in any script, was pretrained to align translations across 27 writing sys...
  </details>

- **2026-11-04** — Luyang Jiang, Chuheng Wei, Yaguang Li et al. — [InterSim: Innovative Intersection Digital Twins for Human-in-the-Loop Driving Simulation](http://arxiv.org/abs/2611.05968v1)
  <details><summary>📄 Abstract</summary>
  Innovative intersection designs can improve roadway safety and operational efficiency, but their uncommon geometries may create challenges for driver comprehension during early deployment. Evaluating these designs through full-scale field implementation can also be costly. This paper presents InterSim, a Unity game engine-based human-in-the-loop (HITL) driving simulator that constructs digital twins of site-specific innovative intersections in a virtual environment. InterSim links the real world...
  </details>

- **2026-11-04** — Keonhee Jang, Kanghoon Lee, Seokwoo Yun et al. — [Robots in the City: Persona-Based Perceptions of Urban Robots](http://arxiv.org/abs/2611.05954v1)
  <details><summary>📄 Abstract</summary>
  Pedestrians increasingly encounter robots in urban public spaces without interacting with them, but how robots change the perceived safety of a street remains unclear. We examine how robot presence and type affect perceived safety across urban contexts. We generate 18 images of Seoul streets that vary in time of day, road class, and robot condition (no robot, a delivery robot, or a humanoid). Two multimodal large language models (MLLMs), Qwen3.8-27B and Gemma4-26B, each conditioned on 500 synthe...
  </details>

- **2026-11-04** — Zehao Lin, Kai Chen, Xixuan Hao et al. — [When Does Better Confidence Improve a Knowledge-Graph Audit?](http://arxiv.org/abs/2611.05877v1)
  <details><summary>📄 Abstract</summary>
  Confidence estimates guide human review in LLM-built knowledge graphs, but better error prediction can yield little improvement in an audit. We study this gap through repairability, selection headroom and label validity. Modelling non-adaptive auditing as budgeted covering, we characterise the minimal decision-relevant error statistics and bound the regret of scalar-preserving first-order planning by a structural mass $Δ^{\mathrm{cl}}$. We simulate ideal repair against benchmark-aligned labels f...
  </details>

- **2026-11-04** — Yuqin Dai, Zhanwei Zhang, Honghui Yang et al. — [CARTBench: Rubric-Based Evaluation of Shopping Advice for Complex and Ambiguous Requests with Timelines](http://arxiv.org/abs/2611.05862v1)
  <details><summary>📄 Abstract</summary>
  Large language model (LLM) shopping assistants now recommend products in multi-turn conversations. However, reliable evaluation faces Data scarcity and Difficulty Standardizing Criteria. To address these obstacles, we introduce CARTBench for CART (Complex and Ambiguous Requests with Timelines). For Data scarcity, we curate cases from real commercial shopping needs across 17 retail domains, pairing timestamped dialogue with 1,603 product records. For Difficulty Standardizing Criteria, we develop ...
  </details>

- **2026-11-04** — Vadim Gorin, Lingfu Zhang — [Gaussian free field limit for the Airy$_β$ line ensemble](http://arxiv.org/abs/2611.05852v1)
  <details><summary>📄 Abstract</summary>
  We prove that the centered height function of the Airy$_β$ line ensemble converges for each $β>0$, under rescaling of space and time variables, towards the Gaussian free field in the half-plane. The conformal structure for GFF involves the spatial change of coordinate $x\mapsto \sqrt{-x}$. The $β$--dependence is isolated in the field rescaling by $\sqrtβ$. For the proofs we study the asymptotic expansions of the moments of Laplace transforms of the Airy$_β$ line ensemble developed in our previou...
  </details>

- **2026-11-04** — Yuning Chen, Hongda Zhang, Linqiang Hu et al. — [Autonomy and Coordination in Intelligent Manufacturing: A Recursive Autonomous Agent Framework](http://arxiv.org/abs/2611.05828v1)
  <details><summary>📄 Abstract</summary>
  Intelligent production requires systems to make decisions and organize work according to production goals and operating conditions. It also requires continuous adjustment through feedback. This paper analyzes intelligence in human production organizations from a complex adaptive systems (CAS) perspective. The analysis identifies two coupled mechanisms: individual autonomy and collective coordination. Individual autonomy enables actors to form local decisions using available information. Collecti...
  </details>

- **2026-11-04** — Mohan Cao, Yongsen Mao, Chucheng Xiang et al. — [GREP: Grounding Generated Room Evaluation in Principles](http://arxiv.org/abs/2611.05802v1)
  <details><summary>📄 Abstract</summary>
  Recent LLM-centric advances can generate attractive furnished rooms by selecting and arranging assets. Yet evaluation remains limited to specific perspectives or predefined questions, failing to reflect overall scene quality. To address this pressing need, we introduce GREP. Its core is a focus shift from defining specific questions to establishing a three-tier evaluation philosophy: basic physical validity checks whether a scene obeys physical constraints; visual coherence concerns compatibilit...
  </details>

- **2026-11-04** — Jikwang Lee, Seungwook Jung, Jaechang Nam — [DARE: Difficulty Analysis for Repair Enhancement](http://arxiv.org/abs/2611.05797v1)
  <details><summary>📄 Abstract</summary>
  LLM-based coding agents are primarily evaluated by their solve rates. However, this metric does not reveal how difficult the solved tasks are or account for differences intask difficulty across benchmarks. Determining the difficulty of individual tasks by repeatedly running multiple agents is costly, while a predicted difficulty score alone provides limited guidance on what support an agent needs. To address these challenges, we propose DARE (Difficulty Analysis for Repair Enhancement), which in...
  </details>

- **2026-11-04** — Shuangyu Xie, Kaiyuan Chen, Uksang Yoo et al. — [VABAR: A Variational Automation Benchmark for Agentic Robotics](http://arxiv.org/abs/2611.06881v1)
  <details><summary>📄 Abstract</summary>
  For robots to operate reliably in commercial and industrial applications, they must persistently perform specific tasks with known variations in object shape and pose. We call this Variational Automation (VA) to differentiate these settings from fixed automation. Inspired by recent papers on Agentic Robotics, where pretrained LLM and VLM coding agents combine interpretable robot programming with the open-world adaptability of model free policies, we propose a general set of agentic robotics benc...
  </details>

- **2026-11-04** — Siddharth Aphale, Ayushman Singh — [Rethinking Self-Repair in Code-as-Policy Agents: What Drives Retry Success?](http://arxiv.org/abs/2611.06863v1)
  <details><summary>📄 Abstract</summary>
  Code-as-policy agents often use execution feedback to retry failed programs. Additional sampling and task guidance can also improve success, leaving the contribution of failure-specific feedback unclear. We study this question in simulated robot manipulation. A fixed lookup selects feedback templates using failure labels and the API variant. A frozen code model generates a fresh program after each scene reset. On the same 252 initial failures, Qwen2.5-Coder-7B recovers 85.3% within five retries,...
  </details>

- **2026-11-04** —  NVIDIA,  :, Anis Ahmad et al. — [Interactive World Simulation with Cosmos for Physical AI](http://arxiv.org/abs/2611.06627v1)
  <details><summary>📄 Abstract</summary>
  We present a shared framework that adapts Cosmos world foundation models for real-time interactive world simulation in Physical AI. By streaming visual observations in response to actions and scene controls, the framework enables users and embodied agents to interact with evolving virtual environments. It supports both predicting the visual consequences of actions and generating observations from physical state maintained by an external simulator. We demonstrate this approach across camera navig...
  </details>

- **2026-11-04** — Sihang Chen, Chen Ye, Wei Chen et al. — [Robocasa-Mem: Benchmarking Environment and Process Memory in Long-Horizon Mobile Manipulation](http://arxiv.org/abs/2611.06475v1)
  <details><summary>📄 Abstract</summary>
  In the real world, mobile manipulation robots must perform complex object interactions and make multi-step decisions, often relying on task-relevant information that is no longer observable. However, existing benchmarks provide limited evaluation of such memory-dependent decision-making in mobile manipulation. To address this gap, we introduce RoboCasa-Mem, a new benchmark comprising nine mobile manipulation tasks that require agents to use interaction history at key decision points. Specificall...
  </details>

- **2026-11-04** — Bingao Chen, Haoquan Fang, C. Karen Liu — [Can Astra Solve RoboMME without Breaking the Bank?](http://arxiv.org/abs/2611.06184v1)
  <details><summary>📄 Abstract</summary>
  Robotic manipulation often requires remembering information that is no longer visible, such as an object's location before occlusion or the order of a demonstrated action sequence. A large vision-language planner can read this history, but calling it before every action chunk is slow and costly. We present a three-tier system for the RoboMME benchmark. GPT-6 Astra (System 2) selects a grounded subtask from stored visual history, a $π_{0.5}$ vision-language-action policy (System 1) executes it, a...
  </details>

- **2026-11-04** — Xiaozhe Ji, Renfen Hu, Hai Hu — [Phonological Knowledge of Chinese Characters in Language Models](http://arxiv.org/abs/2611.05803v1)
  <details><summary>📄 Abstract</summary>
  How much phonological knowledge do language models (LMs) possess about Chinese characters, and how is this knowledge represented and used? We introduce PinyinBench, a controlled benchmark covering homophones, phonological features (initials, finals, and tones), and polyphonic characters. We investigate 17 text-only and multimodal LMs through three complementary approaches: behavioral evaluation, layer-wise probing, and activation steering. Behaviorally, models demonstrate substantial knowledge o...
  </details>

- **2026-11-04** — Siyi Yu — [Dull, Dirty, Dangerous? Working Conditions and the Limits of Occupational AI Exposure](http://arxiv.org/abs/2611.06888v1)
  <details><summary>📄 Abstract</summary>
  Automation is often justified as relief from dull, dirty, and dangerous work. I examine how these conditions relate to occupational AI exposure using 21 O*NET items across 754 US occupations. Higher exposure is associated with lower condition scores under a large language model (LLM) measure and AI Occupational Exposure (AIOE), with equal occupation weights and employment weights. Adjustment for physical demands, required education, training and experience, and wages reduces the composite associ...
  </details>

- **2026-11-04** — Yingying Yan, Jiaqi Tang, Wei Wei et al. — [Where to Connect? Boosting MLLMs via Dynamic Gated Pathways across ALL ViT and LLM Layers](http://arxiv.org/abs/2611.06844v1)
  <details><summary>📄 Abstract</summary>
  A central yet under-explored question in Multimodal Large Language Models (MLLMs) is where to connect---how visual information from a hierarchical vision encoder should be wired into the layer-wise semantics of a large language model. Mainstream MLLMs inject a fixed single-layer visual representation into the LLM and treat all LLM layers as a single consumer, ignoring that different layers demand different visual granularities. Recent multi-layer fusion methods either compress hierarchical featu...
  </details>

- **2026-11-04** — Xinrui Zhong, Zhiming Wang, Yongqi Liu et al. — [ServerBench: How can your coding agents design specialized LLM serving systems?](http://arxiv.org/abs/2611.06841v1)
  <details><summary>📄 Abstract</summary>
  Large language model (LLM) coding agents develop software through experimentation, offering an opportunity to design the serving systems supporting their own operation. Effective serving requires coordinating implementation and operating decisions under session dependencies, latency constraints, and correctness requirements. We introduce ServerBench, a benchmark for agentic design of complete, specialized LLM serving systems. Agents experiment against a common objective, dollars per dollar: late...
  </details>

- **2026-11-04** — Harsidak Singh Banwait — [Transforming Integer Grids to Spatial Intuition: Perception, Not Planning, Governs ARC-AGI-3](http://arxiv.org/abs/2611.06793v1)
  <details><summary>📄 Abstract</summary>
  Sample-efficient fluid intelligence requires agents that rapidly form working models of unfamiliar interactive environments. ARC-AGI-3 tests this across uninstructed visual games scored by Relative Human Action Efficiency, which penalizes exploratory waste quadratically. When frontier models read raw integer grids, serialization destroys spatial topology, and they spend hundreds of actions rediscovering basic boundaries and symmetries. We introduce SARBLOH, an open-weight agent built on the prem...
  </details>

- **2026-11-04** — Ekaterina Fadeeva, Xueyan Li, Mrinmaya Sachan et al. — [Verifier-Guided Self-Consistency: Test-Time Reasoning with Imperfect Generators and Verifiers](http://arxiv.org/abs/2611.06606v1)
  <details><summary>📄 Abstract</summary>
  Large language models can solve many multi-step reasoning problems, but their reasoning remains brittle: plausible intermediate steps often lead to incorrect answers. Improving reasoning at test time requires balancing two imperfect signals: the generator, which provides diversity, and the verifier, which guides correctness. Existing approaches largely favor one side of this tradeoff. Verifier-weighted voting relies on trajectories sampled from the generator and cannot steer generation toward co...
  </details>

- **2026-11-04** — Qian Liu, Shinuo Ma, Yixin Tao et al. — [Competitive Equilibrium for Linear Chores is CLS-complete](http://arxiv.org/abs/2611.06589v1)
  <details><summary>📄 Abstract</summary>
  The competitive equilibrium (CE) is a fundamental concept for markets, with applications to efficient and fair allocation of resources. We consider the fundamental question of computing a CE in the most basic Fisher market model where agents have linear preferences. While it is known that we can compute a CE in strongly polynomial time with linear goods, there is no known polynomial-time algorithm for CE with linear chores. Computing a CE for linear chores is known to be in CLS with no hardness ...
  </details>

- **2026-11-04** — Shreya K. Chari, John S. Vardakas, Kostas Ramantas et al. — [RAGAM-AI: A Hybrid Reinforcement Learning based Agentic approach powered by Generative AI for Edge Resource Management](http://arxiv.org/abs/2611.06554v1)
  <details><summary>📄 Abstract</summary>
  Resource management for distributed edge networks hosting different services has been handled efficiently using Reinforcement learning (RL). Reward generalization in complex workflows is still an open issue within the RL realm. Therefore, this work proposes RAGAM-AI, a hybrid framework that combines the capabilities of RL algorithms and Generative-AI (Gen-AI) for powering an Agentic AI workflow that optimizes resource allocation at the Multi-access Edge Computing (MEC) units. This framework furt...
  </details>

- **2026-11-04** — Christian Pipal, Morgan Wack, Eva-Maria Vogel — [Who Gets Counted? Large Language Models, Informative Refusal, and Downstream Bias in Name-Based Demographic Classification](http://arxiv.org/abs/2611.06550v1)
  <details><summary>📄 Abstract</summary>
  Researchers routinely infer gender, race, and ethnicity from names, yet the standard tools used for this task misclassify the groups that diversity research most needs to measure. Large language models (LLMs) have been proposed as a remedy because they label diverse names accurately. We ask whether that accuracy carries over to the estimates researchers report. Across 10,000 Chinese names, 19,998 North Carolina voters with self-reported race, and 300 political science authors with human referenc...
  </details>

- **2026-11-04** — Zhihao Nan, Sifan Zhou, Yiming Cheng et al. — [MKD2World: A Typed Spatial MarkDown World Model For Web Agents](http://arxiv.org/abs/2611.06544v1)
  <details><summary>📄 Abstract</summary>
  Graphical user interface (GUI) agents can improve decision-making with world-model foresight, provided that predicted states accurately reflect post-action interfaces. Existing state representations fail to jointly capture interface layout, UI semantics, and explicit locations. We introduce Typed Spatial Markdown (TSM), a Markdown-style textual state representation for desktop web interfaces. TSM serializes block-level and atomic-level UI elements according to their spatial relationships, jointl...
  </details>

- **2026-11-04** — Etuh E., Eli. A. Jiya — [Dialect Matters: A Dialect-Aware Baseline for Igala-English Machine Translation](http://arxiv.org/abs/2611.06517v1)
  <details><summary>📄 Abstract</summary>
  The massive permeability of intelligent systems in every sphere of human activities have greatly enhanced clarity, ease of work, and increased general global understanding which has significantly awaken the use of intelligent systems by all users. Intelligent systems greatly rely on precise dataset/corpus for the correctness of their output. Despite efforts by researchers to address Low-resource language in the Natural Language Processing (NLP), Igala still has zero parallel corpora despite effo...
  </details>

- **2026-11-04** — Yulu Xie, Zilong Li, Shen Xu et al. — [A 3D foundation model unifying CT interpretation and segmentation](http://arxiv.org/abs/2611.06471v1)
  <details><summary>📄 Abstract</summary>
  Radiologists interpret computed tomography (CT) scans by jointly determining what a finding represents and where it lies in three-dimensional (3D) anatomy. However, CT models have treated CT interpretation and 3D segmentation as separate tasks, leaving textual findings spatially unverifiable and overlooking potential synergy between clinical understanding and spatial perception. Here we present HoloCT, a generalist 3D foundation model unifying CT interpretation and voxel-level segmentation by jo...
  </details>

- **2026-11-04** — Faezeh Fadaei, Jenny Carla Moran, Taha Yasseri — [A Cracked Mirror: How People Perceive Gender Performance by Large Language Models](http://arxiv.org/abs/2611.06393v1)
  <details><summary>📄 Abstract</summary>
  How do large language models (LLMs) perform gender under zero-shot prompting, and how do people interpret those performances in conversation? Drawing on gender performativity, we examine how gendered meanings emerge through generated language, conversational context and human interpretation. In a preregistered randomised online experiment, 1,060 participants each had five short conversations with an LLM. We used minimal prompts to elicit performances from "very masculine" to "very feminine" and ...
  </details>

- **2026-11-04** — Xiaoyu Zhang, Yougang Lyu, Bin Wu et al. — [PMRecBench: A Benchmark for Personalization in Recommendation Agents under Multimodal Queries](http://arxiv.org/abs/2611.06349v1)
  <details><summary>📄 Abstract</summary>
  On Web platforms for shopping and entertainment, recommendation agents under multimodal queries aim to deliver personalized recommendations that satisfy users' visually specified requirements and reflect preferences inferred from user histories. However, existing personalized recommendation benchmarks use text-only queries, while multimodal ones assess query matching without evaluating personalization based on real user histories. We introduce the Personalized Multimodal Recommendation Benchmark...
  </details>

- **2026-11-04** — Dohyun Kim, Junyong Lhim, Kwanyong Park — [A Systematic Benchmark for Evaluating Multimodal Personalized Reasoning of Vision-Language Models](http://arxiv.org/abs/2611.06259v1)
  <details><summary>📄 Abstract</summary>
  People often make decisions by holistically reasoning over heterogeneous forms of personal information. In this paper, we study the relatively underexplored capability of multimodal personalized reasoning in multimodal large language models (MLLMs). To this end, we introduce \texttt{MPRBench}, a novel and comprehensive benchmark specifically designed to evaluate personalized reasoning across a wide range of tasks and real-world challenges. \texttt{MPRBench} consists of 12 sub-tasks and additiona...
  </details>

- **2026-11-04** — Federico Celi, Leonardo Zacchini, Gabriele Ferri — [A Layered View of LLM Support in Underwater Robotics](http://arxiv.org/abs/2611.06162v1)
  <details><summary>📄 Abstract</summary>
  This extended abstract discusses a specific and, in our experience, practically relevant role for large language models (LLMs) in underwater robotics. Our main premise is that, in underwater fielding missions, the immediate difficulty is often not the synthesis of new low-level control laws, but the operation of complex robotic systems under limited communications, partial observability, and expensive field time. In particular, a significant fraction of the effort during sea trials is devoted to...
  </details>

- **2026-11-04** — Sicen Guo, Zhengfei Song, Kuanhsun Chen et al. — [DSRS: Teaching MLLMs to Perceive, Reason, and Segment in Complex Driving Scenes](http://arxiv.org/abs/2611.06160v1)
  <details><summary>📄 Abstract</summary>
  Existing reasoning segmentation frameworks typically employ multimodal large language models (MLLMs) with broad world knowledge to extract semantics in a human-like manner and generate corresponding segmentation masks. Nevertheless, these frameworks lack the necessary scene-specific awareness. This paper introduces driving scene reasoning segmentation (DSRS), a scene-specific task that requires models to interpret implicit instructions, infer spatial relations, detect potential risks, handle cha...
  </details>

- **2026-11-04** — Niccolò Niccoli, Silvia Dani, Marco Mistretta et al. — [GeoBiaset: A Counterfactual Benchmark for Demographic Bias in World-Level Geolocalization](http://arxiv.org/abs/2611.06085v1)
  <details><summary>📄 Abstract</summary>
  World-level image geolocalization is an increasingly important task, yet the biases of current models remain poorly understood. Prior work has identified coarse dataset imbalances noting, for instance, that some cities are absent from training sets and that models tend to perform better in wealthier regions. However, no one has yet examined which visual cues drive these disparities. To do so, we introduce GeoBiaset, the first benchmark designed to measure how geolocalization models are influence...
  </details>

- **2026-11-04** — Dongjin Lee, Eunju Lee, Jinhee Jang et al. — [RI-Prune: Relation and Information Aware Visual Token Pruning for Multi-Image Vision-Language Models](http://arxiv.org/abs/2611.06047v1)
  <details><summary>📄 Abstract</summary>
  Large vision-language models (LVLMs) have recently been extended to handle multiple input images, but this extension dramatically increases the visual token budget, making visual-token pruning not merely an efficiency option but a practical necessity. Existing visual-token pruning methods, primarily designed for the single-image setting, rely on attention-derived saliency signals to estimate per-token importance. However, this attention-centric design transfers poorly to the multi-image regime: ...
  </details>

- **2026-11-04** — Jiamu Wang, Keunho Byeon, Ji-Uk Kim et al. — [PathoS2VD: From 2D Histopathology to Pseudo Z-Stack Representations](http://arxiv.org/abs/2611.05974v1)
  <details><summary>📄 Abstract</summary>
  For decades, diagnostic pathology has relied on thin two-dimensional (2D) tissue sections, despite biological tissues exhibiting inherently three-dimensional (3D) morphological organization. Because a single section captures only one focal plane, important morphological cues along the z-axis are inevitably discarded, limiting tissue representation for both human interpretation and computational analysis. In this work, we propose a generative framework that learns z-axis morphological priors from...
  </details>

- **2026-11-04** — Mengni Jia, Mengyu Zhou, Xiaoxi Jiang et al. — [Reward Budgeting Reduces Premature Convergence in Reinforcement Learning for LLM Reasoning](http://arxiv.org/abs/2611.05942v1)
  <details><summary>📄 Abstract</summary>
  RL for LLM reasoning often reaches an early performance plateau as the policy distribution becomes increasingly sharp. Recent work has studied policy entropy as both a diagnostic and a control signal for this behavior. In our experiments, however, increasing entropy alone does not reliably change the eventual plateau. We analyze RL through its implicit target policy and derive a sharpness factor $κ$, together with an effective counterpart $κ_{\mathrm{eff}}$, that describes how strongly reward or...
  </details>

- **2026-11-04** — Yoon Pyo Lee, Samrendra Roy, Jay Phil Yoo et al. — [Autonomous agents for electricity-system planning](http://arxiv.org/abs/2611.05911v1)
  <details><summary>📄 Abstract</summary>
  Planning electricity systems requires repeated decisions that connect regional resources, investment, operation and network constraints. Here we present an autonomous planning framework that carries prepared regional scenarios through proposal, numerical evaluation, feedback interpretation, redesign and final plan selection. Agents propose investment bounds, storage operating conditions and feeder interventions, interpret numerical feedback, and decide how to revise designs and when to stop. The...
  </details>

- **2026-11-04** — Zhaokang Liang, Shuyang Zhuang, Xiaoran Jiao et al. — [CellCanon: An Agentic Cellular World Model for Prediction, Explanation, and Observation-Driven Updating](http://arxiv.org/abs/2611.05890v1)
  <details><summary>📄 Abstract</summary>
  Biological discovery requires using molecular knowledge and new measurements to infer responses beyond the conditions already observed. We introduce CellCanon, the first agentic cellular world model to unify single-cell expression prediction, evidence-grounded explanation, and observation-driven updating. Its predictive core reuses condition-level biological evidence across gene-specific numerical readouts to guide single-cell expression generation. A shared world state links predictions, acquir...
  </details>

- **2026-11-04** — Furong Li, Wei Liu, Yali Shao et al. — [A Laplace-Transform Green's Function for Two-Zone Diffusion with Energy Losses: Application to the Geminga Pulsar Halo](http://arxiv.org/abs/2611.05808v1)
  <details><summary>📄 Abstract</summary>
  Extended TeV gamma-ray halos around pulsars are commonly interpreted as evidence for slow diffusion of high-energy electrons and positrons near their sources, with diffusion coefficients about two orders of magnitude below the Galactic average inferred from B/C measurements. A two-zone diffusion picture offers a natural phenomenological resolution: particles are temporarily confined in a slow-diffusion region around the source and subsequently propagate through the outer region with a diffusion ...
  </details>

- **2026-11-04** — Won-Ki Seo, Jiazhen Xu, Han Lin Shang — [Local Whittle estimation for distributional time series: A regularization framework in Bayes Hilbert space](http://arxiv.org/abs/2611.05765v1)
  <details><summary>📄 Abstract</summary>
  We study local Whittle estimation of long memory in density-valued time series in Bayes Hilbert space. The centered log-ratio (clr) transformation maps densities to a linear Hilbert space, allowing analysis using standard Hilbert space methods. When densities are reconstructed from finite samples, however, small absolute estimation errors can remain large relative to the true density in low-density tails. Taking logarithms can amplify this noise and introduce systematic distortions that affect m...
  </details>

- **2026-11-03** — Tianming Sha — [Octopus: One Brain, Many Branches for Latent-KV Multi-Agent Reinforcement Learning](http://arxiv.org/abs/2611.06956v1)
  <details><summary>📄 Abstract</summary>
  Multi-agent LLM systems explore in parallel by spawning sub-agents with isolated context windows, whereas single-agent systems append every search and verification step into one growing trajectory. However, existing multi-agent frameworks duplicate prefix KV caches across branches, exchange findings by re-prefilling text summaries, and flatten or drop cross-branch dependencies during reinforcement learning (RL).   We introduce Octopus, a single-model multi-agent RL framework in which all threads...
  </details>

- **2026-11-03** — Mateusz Modrzejewski, Michał Rokita, Łukasz Neumann — [How Python Audio Libraries Change Across Releases: Module Structure and Documentation](http://arxiv.org/abs/2611.06947v1)
  <details><summary>📄 Abstract</summary>
  Developers who upgrade a Python audio library need to know what changed in the code they import and whether the release notes say so. Release notes and breaking changes have been mined for general software, but the module structure of audio libraries and its documentation have not been studied together. We mine 56 audio repositories used in machine learning workflows: the import graph of 49 packages at 1,395 releases, joined to 20,864 release-note and changelog entries, labeled by three open-wei...
  </details>

- **2026-11-03** — Seungyong Lee, Suhyeok Jang, Minyoung Kim et al. — [Synthesizing Dexterous Robot Demonstrations from Human Videos via Virtual Try-On](http://arxiv.org/abs/2611.05163v3)
  <details><summary>📄 Abstract</summary>
  Robot foundation models have shown remarkable performance in robot control, yet adapting them to a new task still relies heavily on teleoperated demonstrations. Egocentric human videos offer a scalable substitute, but overlaying rendered robots on human videos or retargeting human poses into robot actions leaves significant visual or action gaps for high-DoF robot embodiments. To address this limitation, we propose RoboTryOn, which treats human-to-robot translation as virtual try-on: try-on keep...
  </details>

- **2026-11-03** — Rudrajit Choudhuri, Christian Bird, Carmen Badea et al. — [TACT: A Pragmatic Approach to Qualitative Analysis with an AI Council](http://arxiv.org/abs/2611.05702v1)
  <details><summary>📄 Abstract</summary>
  Qualitative data can tell software teams what their stakeholders need, yet rigorously analyzing thousands of qualitative responses takes expert time that few teams can afford or justify. Teams therefore often face a false choice: leave the responses unanalyzed, or hand them to a large language model and accept its interpretation and judgment. In this paper, we take a pragmatic approach to AI-assisted qualitative analysis and present TACT (Traceable AI Council for Thematic analysis), a procedure ...
  </details>

- **2026-11-03** — Giannis Fikioris, Balasubramanian Sivan, Éva Tardos — [Learning vs. Optimizing Players in Budgeted Games](http://arxiv.org/abs/2611.05580v1)
  <details><summary>📄 Abstract</summary>
  We study repeated general games over $T$ rounds between a utility-maximizing optimizer and a learning agent, where budget constraints couple the players' decisions across rounds. Without budgets, low swap regret simultaneously guarantees the learner sublinear regret and caps the optimizer at its Stackelberg value. Budgets break this picture: adversarial no-regret becomes impossible, so the natural goals are non-manipulability---no adaptive optimizer earns more than $\mathtt{BSE} \cdot T + o(T)$,...
  </details>

- **2026-11-03** — Aditya Gupta, Jean Sebastien Dandurand, Kai Qiu et al. — [Learning Hierarchical Patch Splitting Policies for Faster Vision Transformers](http://arxiv.org/abs/2611.05742v1)
  <details><summary>📄 Abstract</summary>
  Vision Transformers (ViTs) are bottlenecked by the length of their input token sequence. Standard patchification fixes this length with a single patch size applied across the image, regardless of regional content. Prior work on adaptive patch sizing reduces token count by assigning coarser patches to visually simple regions, but relies on noisy pixel-level heuristics such as local entropy to make patchification decisions. We argue that this compute allocation should be grounded in the model's in...
  </details>

- **2026-11-03** — Ankana Banerjee, Mark van der Giezen, Ole Gunnar Aasprong et al. — [Multimodal Fusion Methods for Whole-Slide Images and Clinical Data in Inflammatory Bowel Disease](http://arxiv.org/abs/2611.05579v1)
  <details><summary>📄 Abstract</summary>
  Multimodal AI fusion of histology and clinical data is an active research area in computational pathology, but fusion methods are rarely compared under identical conditions and across different clinical endpoints. We present a modular framework in which slide-level embeddings, obtained by training an attention-based aggregator over patch embeddings from a frozen foundation model, and per-visit clinical embeddings are fed into 15 interchangeable fusion methods with a shared output dimension and p...
  </details>

- **2026-11-03** — Albert Wilcox, Frank Chang, Nhi Nguyen et al. — [MESA: An Evaluation Framework for Compositional, Semantic, and Spatial Generalization in Robotics](http://arxiv.org/abs/2611.05567v1)
  <details><summary>📄 Abstract</summary>
  Despite growing interest in foundation models for robotic manipulation, systematic evaluation of their capabilities remains elusive. Existing benchmarks are either narrow and saturated, offering little signal on SOTA methods, broadly scoped, providing diversity at the cost of controlled experimentation, or require training on large, messy open-source datasets. We introduce MESA, an evaluation framework designed for precise, reproducible measurement of language-conditioned policy generalization. ...
  </details>

- **2026-11-03** — Jorge Ramón Fonseca Cacho — [Rewrite, Then Veto: Rewriter-Agnostic Edit Gating for LLM-Based Post-OCR Correction](http://arxiv.org/abs/2611.05539v1)
  <details><summary>📄 Abstract</summary>
  LLMs can repair noisy OCR transcripts of historical documents, but they also change text that was already correct. We propose EditVeto, a veto gate placed after a full-context LLM rewrite. The rewrite is character-aligned to the OCR input, its differences are split into blocks, and a 0.6B-parameter gate keeps or reverts each block. An oracle analysis motivates the design: given the true error locations, per-span generation is worse than no correction, whereas vetoing a full rewrite's edits helps...
  </details>

- **2026-11-03** — Ivan Martinez-Kay, Tatiana Kardashina, ShiNung Ching et al. — [A Bayesian Optimized Biquad Filter-Burg Model for Real-Time EEG Phase Estimation](http://arxiv.org/abs/2611.05374v2)
  <details><summary>📄 Abstract</summary>
  Real-time phase estimation on stimulus-aligned transient EEG is critical for closed-loop neuromodulation systems targeting the theta-band, yet most real-time phase estimation methods have been developed and validated on resting-state, high-fidelity signals in the alpha band. Recent work has pursued deep learning architectures, while individualized classical bandpass filter tuning remains underexplored. This study characterizes the spectral and temporal properties of non-anticipative bandpass fil...
  </details>

- **2026-11-03** — Zimeng Wang, Jinrong Yang, Rong Chen — [UMLoad: Fast On-Demand Model Loading on Unified Memory Architecture](http://arxiv.org/abs/2611.04253v2)
  <details><summary>📄 Abstract</summary>
  On-demand model loading dominates response latency for interactive on-device AI, yet unified memory architectures (UMAs), now common on edge devices, should make it cheap by placing weights in memory the GPU already sees. However, frameworks still use the loading flow built for discrete GPUs, leaving significant inefficiencies. This paper presents UMLoad, a system-level model-loading accelerator that decouples a framework's logical allocations from their physical page backing. UMLoad uses on-dem...
  </details>


## 📊 统计 / Statistics

| 分类 / Category | 论文数 / Count |
|------|--------|
| jailbreak | 715 |
| prompt-injection | 667 |
| memory-poisoning | 58 |
| tool-use-attack | 172 |
| backdoor | 551 |
| adversarial-attack | 664 |
| privacy-leakage | 4556 |
| steganography | 90 |
| misuse | 1300 |
| red-teaming | 149 |
| vulnerability | 3934 |
| defense | 3829 |
| alignment | 3576 |
| robustness | 3908 |
| watermark | 722 |
| unlearning | 120 |
| agent-safety | 67 |
| benchmark | 74 |
| survey | 445 |
| other | 10675 |

---

📚 **全部 36272 篇论文**（2022 至今）请访问 [GitHub Pages](https://ny1024.github.io/AgentSafety-Papers/) 查看完整列表、搜索与筛选。

*Generated by AgentGuard at 2026-11-09 14:56:46*