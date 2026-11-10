<div align="center">

# AgentGuard 🛡️

**Daily Tracking of LLM Agent Security Papers on arXiv**

[![Auto Update](https://github.com/NY1024/AgentSafety-Papers/actions/workflows/daily-update.yml/badge.svg)](https://github.com/NY1024/AgentSafety-Papers/actions/workflows/daily-update.yml)
[![Papers](https://img.shields.io/badge/Papers-36534-blue)](#)
[![License](https://img.shields.io/badge/License-MIT-green)](#)

</div>

---

## 📖 简介 / Introduction

自动追踪 arXiv 上大模型 Agent 安全方向的最新论文，每日更新，关键词智能分类。

*Automatically tracking the latest LLM Agent security papers on arXiv, updated daily with keyword-based classification.*

**最近更新 / Last Updated**: 2026-11-10 22:44 ｜ **论文总数 / Total Papers**: 36534（近 30 天 / Recent 30 days: 4328）

🌐 **[GitHub Pages](https://ny1024.github.io/AgentSafety-Papers/)** — 查看全部 36534 篇论文（含摘要、分类筛选、搜索）/ View all 36534 papers with abstracts, filters & search

## 📑 分类导航 / Category Navigation

- **[jailbreak](#-jailbreak)** — 越狱攻击 / Jailbreak Attacks — 716
- **[prompt-injection](#-prompt-injection)** — 提示注入攻击 / Prompt Injection Attacks — 677
- **[memory-poisoning](#-memory-poisoning)** — 记忆投毒与篡改 / Memory Poisoning & Tampering — 58
- **[tool-use-attack](#-tool-use-attack)** — 工具使用攻击 / Tool-Use Attacks — 174
- **[backdoor](#-backdoor)** — 后门与投毒攻击 / Backdoor & Poisoning Attacks — 555
- **[adversarial-attack](#-adversarial-attack)** — 对抗攻击 / Adversarial Attacks — 666
- **[privacy-leakage](#-privacy-leakage)** — 隐私泄露 / Privacy Leakage — 4566
- **[steganography](#-steganography)** — 隐写与隐蔽通信 / Steganography & Covert Communication — 90
- **[misuse](#-misuse)** — 滥用与误用 / Misuse & Abuse — 1304
- **[red-teaming](#-red-teaming)** — 红队测试 / Red Teaming — 149
- **[vulnerability](#-vulnerability)** — 漏洞与攻击面 / Vulnerabilities & Attack Surfaces — 3959
- **[defense](#-defense)** — 防御与防护方法 / Defense & Protection Methods — 3856
- **[alignment](#-alignment)** — 对齐与安全约束 / Alignment & Safety Constraints — 3611
- **[robustness](#-robustness)** — 鲁棒性与可靠性 / Robustness & Reliability — 3940
- **[watermark](#-watermark)** — 水印与溯源 / Watermarking & Provenance — 732
- **[unlearning](#-unlearning)** — 机器遗忘 / Machine Unlearning — 120
- **[agent-safety](#-agent-safety)** — Agent 安全框架 / Agent Safety Frameworks — 67
- **[benchmark](#-benchmark)** — 安全评测与基准 / Safety Benchmarks & Evaluation — 74
- **[survey](#-survey)** — 综述与系统化 / Surveys & Systematization — 446
- **[other](#-other)** — 其他安全相关 / Other Security-Related — 10774

## 📄 近期论文 / Recent Papers (Last 30 Days)

> 仅展示最近 30 天中最新的 500 篇论文（含日期、作者、摘要）。近 30 天共 4328 篇，完整 36534 篇论文列表请访问 [GitHub Pages](https://ny1024.github.io/AgentSafety-Papers/)

> Showing the latest 500 of 4328 papers from the last 30 days (with date, authors & abstract). For the full list of 36534 papers, visit [GitHub Pages](https://ny1024.github.io/AgentSafety-Papers/)

### 📂 jailbreak
*越狱攻击 / Jailbreak Attacks* — 3 papers

- **2026-11-08** — Mohammad Tehabsim, Basil Al-Housani, Nour Alhussien et al. — [Beyond AUROC: Deployment-Aware Evaluation of Model-Internal Jailbreak Detectors](http://arxiv.org/abs/2611.11067v1)
  <details><summary>📄 Abstract</summary>
  Large language models (LLMs) are increasingly deployed in user-facing systems, where jailbreak attacks can bypass safety controls and induce harmful and policy-violating outputs. Recent model-internal detectors use hidden representations, gradients, or internal signals to identify such prompts, but their practical security value depends critically on behavior at low false-positive operating points rather than on area under the receiver operating characteristic curve (AUROC) alone.   We study two...
  </details>

- **2026-11-06** — Tianze Chang, Junjie Chu, Yixin Wu et al. — [GuardrailAgent: An Agentic Framework for Jailbreak Defense](http://arxiv.org/abs/2611.09734v1)
  <details><summary>📄 Abstract</summary>
  Despite undergoing safety training to align with human values, large language models (LLMs) remain vulnerable to jailbreak attacks that circumvent built-in safeguards and elicit malicious behaviors given by the adversary. Existing defenses are mostly static and fail to adapt to new or unknown attack strategies, providing limited resilience. To address these, we propose a multi-agent defense framework, GuardrailAgent, that offers adaptive, end-to-end protection. The system autonomously gathers an...
  </details>

- **2026-11-05** — Fazong Wu, Xin Wang, Ming Yang et al. — [JailBound: FOL-Guided Jailbreak Evaluation for Exploring LLM Behavioral Boundaries](http://arxiv.org/abs/2611.07530v1)
  <details><summary>📄 Abstract</summary>
  As large language models (LLMs) are increasingly deployed as general-purpose conversational assistants, they must handle diverse user requests while reliably refusing harmful ones. Jailbreak attacks craft adversarial instructions or conversational contexts to elicit unsafe responses despite these safeguards. However, existing jailbreak benchmarks often rely on manually designed or collected prompts, making it difficult to systematically extend coverage to new threat conditions. Moreover, existin...
  </details>


### 📂 prompt-injection
*提示注入攻击 / Prompt Injection Attacks* — 13 papers

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


### 📂 memory-poisoning
*记忆投毒与篡改 / Memory Poisoning & Tampering* — 1 papers

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

- **2026-11-05** — Celeste De Schamphelaere, Juan J. Vazquez, Ari Spiesberger et al. — [Towards interpreting any residual stream direction by scaling activation inversion](http://arxiv.org/abs/2611.08465v1)
  <details><summary>📄 Abstract</summary>
  To interpret a direction in a language model's residual stream, we can look for text that strongly activates it. But when such text is found by scanning a corpus, it is limited to what that corpus contains. We develop Maximally-Activating Example Metamodels (MAEMs), language models which map residual stream directions from a subject model to text exemplars that strongly activate those directions. Our objective is to maximise the cosine similarity of a supplied residual stream direction with the ...
  </details>


### 📂 adversarial-attack
*对抗攻击 / Adversarial Attacks* — 2 papers

- **2026-11-09** — Melih Coşğun, Mehmet Emre Gürsoy, Alptekin Küpçü et al. — [SNAPRAG: Cost-Efficient Knowledge Extraction Attack on RAG Systems via Adversarial Perturbations](http://arxiv.org/abs/2611.12241v1)
  <details><summary>📄 Abstract</summary>
  Retrieval-Augmented Generation (RAG) systems improve Large Language Model (LLM) responses by incorporating information from external knowledge bases. However, recent studies have shown that attackers can extract substantial portions of private knowledge bases from RAG systems through repeated querying. Yet, state-of-the-art extraction attacks either rely heavily on external LLMs to generate adversarial queries or require a large number of queries. In this paper, we propose SNAPRAG, a novel and c...
  </details>

- **2026-11-08** — Yibo Miao, Yichuan Cao, Xiao-Shan Gao et al. — [Chatter Attack: Resource Consumption Attack for Large Language Models](http://arxiv.org/abs/2611.11261v1)
  <details><summary>📄 Abstract</summary>
  LLMs are powerful but incur substantial inference cost, which can be exploited by malicious users to induce overly long outputs, increasing latency and operational expense. Prior resource consumption attacks either coerce repetition or suppress the end-of-sequence token by lowering its logit value. However, with autoregressive, sampling-based generation, the search space grows exponentially with length and small deviations or unstable trajectories can derail optimization, limiting attack effecti...
  </details>


### 📂 privacy-leakage
*隐私泄露 / Privacy Leakage* — 27 papers

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


### 📂 misuse
*滥用与误用 / Misuse & Abuse* — 13 papers

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


### 📂 defense
*防御与防护方法 / Defense & Protection Methods* — 59 papers

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


### 📂 alignment
*对齐与安全约束 / Alignment & Safety Constraints* — 53 papers

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


### 📂 robustness
*鲁棒性与可靠性 / Robustness & Reliability* — 56 papers

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


### 📂 watermark
*水印与溯源 / Watermarking & Provenance* — 15 papers

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


### 📂 unlearning
*机器遗忘 / Machine Unlearning* — 1 papers

- **2026-11-05** — Nicolás Segura-Kunsagi, Juan Luis Suárez-Díaz, Iván Sevillano-García et al. — [DISCERN: Distributional Synthetic Replay for Retain-Free Incremental Machine Unlearning](http://arxiv.org/abs/2611.07892v1)
  <details><summary>📄 Abstract</summary>
  Machine unlearning aims to remove the influence of specific training data from a trained model without retraining from scratch. In real deployments, however, deletion requests arrive over time, calling for incremental class unlearning (ICU): classes are removed sequentially, previously forgotten knowledge must remain forgotten, and the remaining classes must be preserved. We present DIstributional SynthetiC rEplay for Retain-free iNcremental unlearning (DISCERN), an intervention-based class unle...
  </details>


### 📂 benchmark
*安全评测与基准 / Safety Benchmarks & Evaluation* — 1 papers

- **2026-11-05** — Zhi Zhang, Francesco Belardinelli, Alessandro Abate — [Geometry-Evolving Barrier Functions for Safety Evaluation in Dynamic Environments](http://arxiv.org/abs/2611.07788v1)
  <details><summary>📄 Abstract</summary>
  Autonomous systems operating in dynamic environments often involve multiple interacting agents, giving rise to high-dimensional safety evaluation problems. Hamilton--Jacobi (HJ) reachability provides rigorous finite-horizon safety guarantees, but solving a global HJ partial differential equation (PDE) over the entire state space leads to prohibitive computational complexity. In this paper, we introduce Geometry-Evolving Barrier Functions (GEBFs), a novel representation for dynamic safety evaluat...
  </details>


### 📂 survey
*综述与系统化 / Surveys & Systematization* — 3 papers

- **2026-11-09** — Jeremy Canale, Fabien Soulis — [Detecting Shadow AI: Unsanctioned LLM Agents on Enterprise Endpoints: A Taxonomy, an Open Detector and a Controlled Evaluation](http://arxiv.org/abs/2611.12377v1)
  <details><summary>📄 Abstract</summary>
  Shadow IT, the use of technology that the IT organisation has not approved, is a long-standing governance problem. We argue that autonomous AI agents can make it grow much faster: agents make building tools nearly free, act with their user's privileges, and leave behind scripts, automations and MCP servers that are themselves unsanctioned. A simple compounding model shows that, under its assumptions, shadow IT grows exponentially once agentic artifacts reproduce faster than the organisation reti...
  </details>

- **2026-11-06** — Wei Huang, Youjin Deng — [Deep Learning Theory through the Lens of Statistical Physics: A Topical Review](http://arxiv.org/abs/2611.09138v1)
  <details><summary>📄 Abstract</summary>
  The recent success of foundation models and deep learning has far outpaced our theoretical understanding of how large-scale neural networks learn and generalize. Statistical physics provides a natural language for describing such high-dimensional, nonlinear, and strongly coupled systems, offering concepts such as mean-field theory, phase transitions, energy landscapes, and stochastic dynamics. In this topical review, we adopt a statistical-physics way of thinking -- from concepts including phase...
  </details>

- **2026-11-05** — Max Unterbusch, Julian Frattini, Michael Mircea et al. — [Adapt the Object to the Subject: Representative Study Material for Empirical Software Engineering](http://arxiv.org/abs/2611.07772v1)
  <details><summary>📄 Abstract</summary>
  External validity is a central concern in empirical software engineering, yet the debate has largely focused on whether study participants are representative. How well the study objects they reason about - code, models, or requirements - are representative of each participant's own work is often overlooked. Practitioners' own artifacts would be ideal, but are often out of reach, so researchers sample from public datasets or construct objects artificially. Whether this lack of subject-object fit ...
  </details>


### 📂 other
*其他安全相关 / Other Security-Related* — 184 papers

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


## 📊 统计 / Statistics

| 分类 / Category | 论文数 / Count |
|------|--------|
| jailbreak | 716 |
| prompt-injection | 677 |
| memory-poisoning | 58 |
| tool-use-attack | 174 |
| backdoor | 555 |
| adversarial-attack | 666 |
| privacy-leakage | 4566 |
| steganography | 90 |
| misuse | 1304 |
| red-teaming | 149 |
| vulnerability | 3959 |
| defense | 3856 |
| alignment | 3611 |
| robustness | 3940 |
| watermark | 732 |
| unlearning | 120 |
| agent-safety | 67 |
| benchmark | 74 |
| survey | 446 |
| other | 10774 |

---

📚 **全部 36534 篇论文**（2022 至今）请访问 [GitHub Pages](https://ny1024.github.io/AgentSafety-Papers/) 查看完整列表、搜索与筛选。

*Generated by AgentGuard at 2026-11-10 22:44:48*