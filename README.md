<div align="center">

# AgentGuard 🛡️

**Daily Tracking of LLM Agent Security Papers on arXiv**

[![Auto Update](https://github.com/NY1024/AgentSafety-Papers/actions/workflows/daily-update.yml/badge.svg)](https://github.com/NY1024/AgentSafety-Papers/actions/workflows/daily-update.yml)
[![Papers](https://img.shields.io/badge/Papers-27186-blue)](#)
[![License](https://img.shields.io/badge/License-MIT-green)](#)

</div>

---

## 📖 简介 / Introduction

自动追踪 arXiv 上大模型 Agent 安全方向的最新论文，每日更新，关键词智能分类。

*Automatically tracking the latest LLM Agent security papers on arXiv, updated daily with keyword-based classification.*

**最近更新 / Last Updated**: 2026-09-10 15:42 ｜ **论文总数 / Total Papers**: 27186（近 30 天 / Recent 30 days: 4025）

🌐 **[GitHub Pages](https://ny1024.github.io/AgentSafety-Papers/)** — 查看全部 27186 篇论文（含摘要、分类筛选、搜索）/ View all 27186 papers with abstracts, filters & search

## 📑 分类导航 / Category Navigation

- **[jailbreak](#-jailbreak)** — 越狱攻击 / Jailbreak Attacks — 624
- **[prompt-injection](#-prompt-injection)** — 提示注入攻击 / Prompt Injection Attacks — 531
- **[memory-poisoning](#-memory-poisoning)** — 记忆投毒与篡改 / Memory Poisoning & Tampering — 49
- **[tool-use-attack](#-tool-use-attack)** — 工具使用攻击 / Tool-Use Attacks — 133
- **[backdoor](#-backdoor)** — 后门与投毒攻击 / Backdoor & Poisoning Attacks — 449
- **[adversarial-attack](#-adversarial-attack)** — 对抗攻击 / Adversarial Attacks — 588
- **[privacy-leakage](#-privacy-leakage)** — 隐私泄露 / Privacy Leakage — 4048
- **[steganography](#-steganography)** — 隐写与隐蔽通信 / Steganography & Covert Communication — 64
- **[misuse](#-misuse)** — 滥用与误用 / Misuse & Abuse — 1000
- **[red-teaming](#-red-teaming)** — 红队测试 / Red Teaming — 123
- **[vulnerability](#-vulnerability)** — 漏洞与攻击面 / Vulnerabilities & Attack Surfaces — 3012
- **[defense](#-defense)** — 防御与防护方法 / Defense & Protection Methods — 2821
- **[alignment](#-alignment)** — 对齐与安全约束 / Alignment & Safety Constraints — 2634
- **[robustness](#-robustness)** — 鲁棒性与可靠性 / Robustness & Reliability — 2732
- **[watermark](#-watermark)** — 水印与溯源 / Watermarking & Provenance — 412
- **[unlearning](#-unlearning)** — 机器遗忘 / Machine Unlearning — 94
- **[agent-safety](#-agent-safety)** — Agent 安全框架 / Agent Safety Frameworks — 54
- **[benchmark](#-benchmark)** — 安全评测与基准 / Safety Benchmarks & Evaluation — 65
- **[survey](#-survey)** — 综述与系统化 / Surveys & Systematization — 337
- **[other](#-other)** — 其他安全相关 / Other Security-Related — 7416

## 📄 近期论文 / Recent Papers (Last 30 Days)

> 仅展示最近 30 天中最新的 500 篇论文（含日期、作者、摘要）。近 30 天共 4025 篇，完整 27186 篇论文列表请访问 [GitHub Pages](https://ny1024.github.io/AgentSafety-Papers/)

> Showing the latest 500 of 4025 papers from the last 30 days (with date, authors & abstract). For the full list of 27186 papers, visit [GitHub Pages](https://ny1024.github.io/AgentSafety-Papers/)

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

- **2026-09-07** — Srikanth Malla, Chiho Choi, Joon Hee Choi — [The Geometry of Refusal: Why Post-Hoc Safety Is Fragile and Pretraining-Time Safety Persists](http://arxiv.org/abs/2609.06934v1)
  <details><summary>📄 Abstract</summary>
  Post-hoc safety training (RLHF, DPO) is the dominant way to align large language models, yet jailbreaks (Zou et al., 2023b), fine-tuning attacks (Qi et al., 2024), and activation-space probes (Arditi et al., 2024) keep recovering the behaviors it was meant to remove. We give this fragility one geometric explanation and trace it to when, during pretraining, safety can take hold. We measure the safety update $Δ= W_{\text{safe}} - W_{\text{base}}$ against the curvature of the model's capabilities (...
  </details>


### 📂 prompt-injection
*提示注入攻击 / Prompt Injection Attacks* — 6 papers

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

- **2026-09-07** — Boyang Zhang, Qingxin Xiao, Lingwei Dang et al. — [CoRL: Co-Evolutionary Reinforcement Learning for Adaptive Indirect Prompt-Injection Attacks and Defenses](http://arxiv.org/abs/2609.07529v1)
  <details><summary>📄 Abstract</summary>
  Tool-augmented language agents are vulnerable to indirect prompt injection (IPI). Unlike direct prompt injection, IPI hides adversarial instructions in untrusted tool outputs and can covertly alter the execution of a legitimate task. Defenses trained on fixed attacks may fail as an attacker changes its strategy, injection site, and payload. To address this problem, we formulate adaptive IPI as an asymmetric, partially observable, general-sum Markov game: a multi-turn attacker adapts payloads at ...
  </details>

- **2026-09-07** — Asif Pinjari, Mithun Paul Saint-Germain — [AgentDrift: A Step-Labeled Benchmark of Injection-Hijacked LLM Agent Trajectories](http://arxiv.org/abs/2609.06972v1)
  <details><summary>📄 Abstract</summary>
  LLM agents complete tasks by issuing sequences of tool calls, and every observation they read is a channel through which an indirect prompt injection can enter. A successful injection has a characteristic shape when the trajectory is read in order: a benign prefix gives way to actions that serve the attacker rather than the user. Existing benchmarks measure whether such attacks succeed against live agents, and existing guard models judge a trace as a whole; no public corpus labels, step by step,...
  </details>

- **2026-09-07** — Aashiq Muhamed, Virginia Smith — [MOLE: Detecting Insider Threats in AI Agents](http://arxiv.org/abs/2609.06966v1)
  <details><summary>📄 Abstract</summary>
  Model misalignment, prompt injection, or operator misuse could lead AI agents operating frontier-lab accounts to exfiltrate model weights, poison training data, or weaken release gates. Existing benchmarks do not test whether defenders can detect this activity among routine work under a limited review budget. We introduce MOLE, an open benchmark of 150 AI-operated accounts sharing 9 stateful services over 30 workdays, with 12 threats and 8 corpora from four models totaling roughly 20 billion tok...
  </details>


### 📂 memory-poisoning
*记忆投毒与篡改 / Memory Poisoning & Tampering* — 1 papers

- **2026-09-08** — Ayan Roy, Kaustuvi Basu — [MemSentry: A Framework for Detecting Persistent Memory Poisoning in Agentic AI](http://arxiv.org/abs/2609.08747v1)
  <details><summary>📄 Abstract</summary>
  Agentic AI systems with persistent memory introduce a distinct attack surface known as memory poisoning, in which adversarially crafted content is stored in long-term memory and subsequently influences future agent behavior. Such attacks can suppress security alerts, facilitate privilege escalation, alter trust relationships, or override security policies without modifying the underlying model weights or system prompts. To address this threat, we present MemSentry, a formal, configuration-driven...
  </details>


### 📂 tool-use-attack
*工具使用攻击 / Tool-Use Attacks* — 1 papers

- **2026-09-07** — Benjamin Kapner, Carmel Soceanu, Alicia Petrunin et al. — [Scanning the Harness: An Empirical Study of Supply-Chain Defects in AI Coding-Agent Configurations](http://arxiv.org/abs/2609.07360v1)
  <details><summary>📄 Abstract</summary>
  AI coding agents such as Claude Code, Cursor, GitHub Copilot, and OpenAI Codex are configured through artifacts developers write and share: instruction files, skills, hooks, MCP server declarations, subagents. This harness is a dependency layer installed from marketplaces and public repositories, running with the developer's privileges, with no lockfile, no install-time check, and no vocabulary for what a component may do. We study it over 3,171 public GitHub repositories: 2,660 setups that asse...
  </details>


### 📂 backdoor
*后门与投毒攻击 / Backdoor & Poisoning Attacks* — 6 papers

- **2026-09-08** — Iliano Fasolino — [In RAG We Trust? Measuring Robustness of Retrieval-Augmented Generation Under Document Poisoning](http://arxiv.org/abs/2609.09243v1)
  <details><summary>📄 Abstract</summary>
  Retrieval-augmented generation (RAG) grounds a language model in retrieved documents, which reduces hallucination but creates a new attack surface: if retrieved text is tampered with, the model may repeat the falsehood. We study how much a small quantized model, Llama 3.1 8B, degrades when a fraction of its retrieved context is poisoned. Three corruption strategies are tested, entity swap, number swap, and negation, each applied to zero, one, two, or three of the three retrieved passages, over a...
  </details>

- **2026-09-07** — Wissam Antoun, Francis Kulumba, Théo Lasnier et al. — [LLM Forensics: Where Do Backdoors Hide? Localizing and Controlling Trigger Mechanisms with Sparse Autoencoders](http://arxiv.org/abs/2609.07746v1)
  <details><summary>📄 Abstract</summary>
  Even though backdoors in LLMs have been a growing concern, their inner workings are still under heavy scrutiny. Trigger-based backdoors are easy to define behaviorally, a rare input that makes the model switch to a chosen response pattern, but the mechanism between triggers and their responses is less clear. We study this mechanism in a controlled, harmless language-switching setting, where fixed trigger sequences make 1B and 8B language models continue English prompts in French or German. For t...
  </details>

- **2026-09-07** — Feifei Liu, Jintao Cheng, Chi Man Vong et al. — [CrACK: Adversarial Attacks on Cross-Model Consistency in Collaborative Vision Foundation Models](http://arxiv.org/abs/2609.07499v1)
  <details><summary>📄 Abstract</summary>
  Training-free collaborative pipelines that integrate Vision Foundation Models such as CLIP, SAM, and DINO achieve strong open-vocabulary dense prediction and are increasingly deployed in safety-critical applications. The security of these systems is commonly assumed to follow from the robustness of their individual models. We challenge this assumption. We identify a vulnerability shared by every collaborative pipeline: each model consumes the intermediate output of another without verifying sema...
  </details>

- **2026-09-07** — Wenkai Huang, Siyuan Liang, Gaolei Li et al. — [TrojanWorld: Backdooring World-Model Agents via Imagination Steering](http://arxiv.org/abs/2609.07051v1)
  <details><summary>📄 Abstract</summary>
  World models increasingly serve as the predictive core of model-based reinforcement learning agents, enabling them to simulate future dynamics and reason over imagined trajectories before acting. Their substantial training demands make pretrained world models attractive for distribution and reuse, exposing downstream systems to model supply chain threats. Backdoor attacks offer a targeted and stealthy means of exploiting such supply chains, yet their threat to interactive world-model agents rema...
  </details>

- **2026-09-07** — Yasir Arafat Prodhan, Sadad Hasan, Mohammed Imamul Hassan Bhuiyan — [FreqDoor: A Hidden Trojan in the Frequency Domain for Backdoor Attacks on Vision-Language Models](http://arxiv.org/abs/2609.07048v1)
  <details><summary>📄 Abstract</summary>
  Vision-language models (VLMs) have recently shown excellent progress in open-ended image-to-text generation. However, their multimodal nature makes them persistently vulnerable to backdoor attacks. Existing backdoor triggers for VLMs are either spatial, textual, or bimodal, which may yield localized or recognizable trigger patterns. In this work, we explore a different attack surface and propose \ textsc {FreqDoor}, a training-time backdoor attack that implants triggers in the frequency domain. ...
  </details>

- **2026-09-06** — Heba Osama, Zeyad Ahmed, Mohamed Amgad et al. — [WAPP: Safe Learning of Positive Security WAF Policies from Live Traffic](http://arxiv.org/abs/2609.06840v1)
  <details><summary>📄 Abstract</summary>
  Web Application Firewalls (WAFs) mainly rely on signatures to detect known attacks, which can leave gaps against modified or previously unseen payloads. Positive security provides a complementary approach by learning legitimate traffic and blocking inputs that fall outside the learned profile. However, learning directly from live traffic can be unsafe when malicious requests contaminate the training data. This paper presents the Whitelisting Autonomous Policy Producer (WAPP), a framework that co...
  </details>


### 📂 adversarial-attack
*对抗攻击 / Adversarial Attacks* — 7 papers

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

- **2026-09-07** — Dongsu Song, DaeYun GO, Jay Hoon Jung — [Discovering Natural Transformation Vulnerabilities in Black-Box Vision Models](http://arxiv.org/abs/2609.07110v1)
  <details><summary>📄 Abstract</summary>
  Natural adversarial examples (NAEs) reveal that vision models can fail under realistic semantic changes beyond norm-bounded perturbations. However, generating NAEs in a black-box setting remains challenging because existing generative attacks often rely on surrogate models, learned attack priors, or costly query-based optimization, whereas the natural transformations that expose model vulnerabilities are unknown a priori. We propose \textbf{Adversarial Scenario Attack (ASA)}, a query-based black...
  </details>

- **2026-09-07** — Xinglong Zhang, Qingwen Ma, Cong Li et al. — [Distributed Secure Learning Control for Large-scale Multirobots under Stealthy Actuator Attacks](http://arxiv.org/abs/2609.06896v1)
  <details><summary>📄 Abstract</summary>
  Distributed learning control for multirobot systems (MRS) offers significant flexibility in presence of uncertainties but lacks provable performance guarantees. A promising direction involves integrating reinforcement learning (RL) into distributed model predictive control (DMPC), leveraging the strengths of RL in nonlinear policy design and the receding-horizon replanning capabilities of DMPC. However, ensuring secure control within such a learning framework under malicious cyber attacks, parti...
  </details>

- **2026-09-06** — Marzia Khan, Akul Malhotra, Sumeet Kumar Gupta — [BLINK: Batch Normalization-based Integrity Checkpoints for In-Situ Detection and Mitigation of Diverse Weight Corruptions in DNN Accelerators](http://arxiv.org/abs/2609.06781v1)
  <details><summary>📄 Abstract</summary>
  In safety-critical deployments, AI hardware must remain reliable against a broad spectrum of threats such as aging, soft errors, hard faults, and adversarial attacks (e.g. progressive bit flip attack (PBFA)). All of these corrupt stored weights while the chip keeps producing confident but inaccurate predictions. Detecting and mitigating such weight perturbations is crucial for safety-critical platforms. To that end, we propose BLINK, an on-chip batch normalization (BN)-based on-the-fly detection...
  </details>


### 📂 privacy-leakage
*隐私泄露 / Privacy Leakage* — 34 papers

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

- **2026-09-07** — Xiaoting Lyu, Yuhong Wu, Yufei Han et al. — [AgentLeak: Cloning Stronger LLM Agent Capabilities onto Weaker Agents Beyond Skill Stealing](http://arxiv.org/abs/2609.07131v1)
  <details><summary>📄 Abstract</summary>
  Large language model (LLM) agents increasingly achieve long-horizon tasks by combining foundation models with explicit skills and implicit procedural knowledge acquired through execution. The resulting task-solving capabilities have become valuable proprietary assets, raising a new security question: can a substantially weaker attacker-controlled agent acquire the capabilities of a stronger proprietary agent through limited black-box interaction? Existing skill-stealing attacks recover explicit ...
  </details>

- **2026-09-07** — Chibuzor Okocha, Christan Grant, Zoey Liu — [Reasoning Beyond Transcription: Audio Language Models on Child Stuttering Speech](http://arxiv.org/abs/2609.07968v1)
  <details><summary>📄 Abstract</summary>
  Child speech differs from adult speech in acoustics, prosody, and linguistic structures. Speech disfluencies (such as repetitions) further challenge automatic understanding. While Audio Language Models (ALMs) show strong semantic reasoning from speech audio, their ability to reason about disfluent child speech in mixed-speaker settings remains unexplored. We investigate this through two tasks: child-focused semantic summarization and speech entailment. Experiments use recordings of children who ...
  </details>

- **2026-09-07** — Yiyuan Yang, Zheshun Wu, Yong Chu et al. — [From Event Logs to Governed Action: A BlueSky Agenda for Agentic Process Mining](http://arxiv.org/abs/2609.07984v1)
  <details><summary>📄 Abstract</summary>
  Process mining has long turned event logs into process knowledge: discovered models, conformance evidence, bottleneck diagnoses, and runtime predictions. Agentic AI changes the target. Process-aware agents will not only ask what happened. They will ask whether a proposed action should be taken, given the available evidence, privacy budget, organizational authority, and downstream risk. This BlueSky paper proposes event-to-action process mining: a process-mining agenda for transforming heterogene...
  </details>

- **2026-09-07** — Tara Šverko, Annette J. Jones, Chantalle J. Krajewska et al. — [Exciton Coherence in CsPbBr3 Nanocrystals is Bounded by Phonon-Mediated Bright-Triplet Relaxation](http://arxiv.org/abs/2609.07739v1)
  <details><summary>📄 Abstract</summary>
  Scalable sources of indistinguishable single photons or entangled photon pairs are fundamental to many quantum photonic technologies. Colloidal lead halide perovskite nanocrystals are promising such sources, but their exciton coherent properties are not fully understood. We show that in single CsPbBr3 nanocrystals at 4 K, acoustic phonon-mediated exciton fine structure relaxation (EFSR) drives leakage of population between the bright exciton triplet states, competing with the radiative lifetime....
  </details>

- **2026-09-07** — Côme-Alexis Puech, Sébastien Thuau, Amira Gran et al. — [Federated Binary Gating with Server-Side Vision-Language Inference for Surveillance Anomaly Classification](http://arxiv.org/abs/2609.07403v1)
  <details><summary>📄 Abstract</summary>
  Privacy-sensitive surveillance systems could benefit from large vision-language models (VLMs), but such models typically require centralized access to raw video. In federated learning settings, this challenge is amplified by non-independent and identically distributed (non-IID) client data, which can make direct multiclass anomaly classification unstable, especially for rare categories. We propose a hybrid two-stage architecture that combines a federated binary convolutional neural network (CNN)...
  </details>

- **2026-09-07** — Sunil Tyagi — [Open-Set Vessel Re-Identification from Underwater Ship-Radiated Noise with a Raw-Waveform Selective-Kernel Acoustic Neural Network (SKANN) and a Cross-Passage Evaluation Protocol](http://arxiv.org/abs/2609.07399v1)
  <details><summary>📄 Abstract</summary>
  Underwater acoustic target recognition has converged on closed-set classification by vessel type, a task that does not answer whether a monitoring system has heard this hull before. We formalise open-set, cross-passage vessel re-identification on public hydrophone data and specify a protocol that removes the two easiest routes to a high score: hull-disjoint splits keyed to MMSI/IMO, galleries and queries from disjoint passages of each hull, source-pure galleries, and an audio-adjudicated transit...
  </details>

- **2026-09-07** — Shannon Veitch, C. Shem, Lena Csomor et al. — [Enhancing Privacy, Neglecting Harms: An Analysis of Real-World Digital Privacy Incidents](http://arxiv.org/abs/2609.07217v1)
  <details><summary>📄 Abstract</summary>
  Privacy-enhancing technologies (PETs) have emerged as a technical means for providing individuals with greater control over their information. Yet despite the growing deployment of PETs, people continue to experience privacy harms. In this work, we revisit our understanding of privacy incidents and the realities of those experiencing privacy harms, to assess whether the goals and abilities of PETs are misaligned with the harms people face.   For our study, we collect news articles that correspon...
  </details>

- **2026-09-07** — Kenneth Koh, Ryan Jak Yang Lim, Alessandro Sparacio et al. — [How Well Do LLMs Simulate Survey Responses Following a Breast Cancer Screening Intervention?](http://arxiv.org/abs/2609.07141v1)
  <details><summary>📄 Abstract</summary>
  Collecting survey data is laborious and limited by privacy constraints. Large language models (LLMs) have shown promise as predictive social simulations. It is unclear whether they can replicate population-level response distributions before and after a healthcare intervention. Using information derived from 4125 women aged 35-59 years, we evaluate whether agents informed solely by pre-intervention profile information can reproduce post-intervention response distributions. Groups of LLM agents (...
  </details>

- **2026-09-07** — Jeongmin Lee, Seung Yun, Minkyu Lee et al. — [Comparing Self-Supervised and Domain-Invariant Features for Cross-Domain Voice Phishing Detection](http://arxiv.org/abs/2609.07079v1)
  <details><summary>📄 Abstract</summary>
  Voice phishing detection faces three critical challenges: real criminal recordings are unavailable due to privacy constraints; when available, only a handful of samples exist, insufficient for fine-tuning; and lightweight acoustic-only detection is needed as an alternative to large self-supervised models. We compare domain-invariant prosodic features and self-supervised representations (HuBERT, wav2vec2.0) through cross-domain evaluation-training on scenario-based actor recordings and testing on...
  </details>

- **2026-09-07** — Suparno Roy Chowdhury, Manan Roy Choudhury, Dhruv Madhwal et al. — [CIPHER: Benchmarking Cross-record Inference over Privacy-Hardened Evidence Records](http://arxiv.org/abs/2609.07022v1)
  <details><summary>📄 Abstract</summary>
  Reasoning over privacy-constrained records requires combining structured attributes with evidence from free-text narratives. We introduce CIPHER (Cross-record Inference over Privacy-Hardened Evidence Records), a benchmark of expert-validated questions from consumer-finance, clinical, and law-enforcement records. The questions cover common tabular operations and include executable SQL supervision. We evaluate retrieval, prompting, table-specialist, and hybrid symbolic-neural systems under native ...
  </details>

- **2026-09-07** — Shao-An Yin — [Input-to-State Stability Framework for Fully Distributed Primal-Dual Dynamics for Quadratic GNEPs Without Multiplier Consensus](http://arxiv.org/abs/2609.06983v1)
  <details><summary>📄 Abstract</summary>
  Generalized Nash Equilibrium Problems (GNEPs) often arise in multi-agent engineering applications that require distributed algorithms. Unlike traditional approaches that enforce consensus on multipliers, our method removes the need to share multipliers, reducing communication and improving privacy. As a result, different initializations can lead to different GNEs, including non-variational ones. We establish convergence under sufficient conditions using an input-to-state stability (ISS) framewor...
  </details>

- **2026-09-06** — Chayun Kongtongvattana — [Novel Methods for Catheter and Guidewire Segmentation in X-ray Fluoroscopy under a Federated Learning Setting](http://arxiv.org/abs/2609.06876v1)
  <details><summary>📄 Abstract</summary>
  Endovascular procedures rely on real-time manipulation of thin instruments, catheters and guidewires, under X-ray fluoroscopy guidance, where accurate visual analysis is essential for procedural safety. Learning-based methods are constrained by structural complexity, data scarcity, and privacy regulations precluding centralised training across institutions. This thesis presents a structure-aware federated learning framework for catheter and guidewire analysis, with four contributions evaluated o...
  </details>

- **2026-09-06** — Corban Villa, Michele Guerra, Syed Khandker et al. — [A Queryable Graph-Based Security Analysis Framework for O-RAN](http://arxiv.org/abs/2609.06855v1)
  <details><summary>📄 Abstract</summary>
  The Open Radio Access Network (O-RAN) replaces vendor-locked RANs with a modular and interoperable architecture that fosters competition and accelerates innovation. With this openness comes increased complexity and a larger attack surface, making security a critical concern. Today, assessing O-RAN security requires manually cross-referencing dozens of specifications, vendor whitepapers, and academic studies, which is error-prone and static. In this paper, we present a graph-based framework that ...
  </details>

- **2026-09-06** — Sicong Li, Lingfeng Yao, Xingke Yang et al. — [A Novel Semantic Manifold Alignment Attack against Embedding-to-Embedding Obfuscation in Privacy-Preserving LLMs](http://arxiv.org/abs/2609.06749v1)
  <details><summary>📄 Abstract</summary>
  With the widespread applications of large language models (LLMs), privacy-preserving inference has become increasingly essential for sensitive queries. To balance privacy and utility, a series of lightweight obfuscation approaches has recently been proposed, where users locally transform plaintext embeddings into the fixed ciphertext ones. While such Embedding-to-Embedding Obfuscation (E2EO) schemes demonstrate considerable resilience against traditional token frequency and embedding inversion a...
  </details>


### 📂 steganography
*隐写与隐蔽通信 / Steganography & Covert Communication* — 1 papers

- **2026-09-07** — Nitin Jha, Abhishek Parakh — [A Novel Steganography Scheme Using Quantum Hilbert Transform](http://arxiv.org/abs/2609.07894v1)
  <details><summary>📄 Abstract</summary>
  The main goal of steganography is to transmit hidden messages in legitimate-looking communication messages. Phase-domain information hiding, however, has not been fully explored for quantum systems. This work introduces a finite-dimensional Quantum Hilbert Transform (QHT) as a unitary phase operator based on the Quantum Fourier Transform. Using this construction, we develop a QHT-based quantum steganography scheme that embeds classical bits as weak signed phase perturbations of quantum cover sta...
  </details>


### 📂 misuse
*滥用与误用 / Misuse & Abuse* — 17 papers

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

- **2026-09-07** — Jeongmin Lee, Dongmyung Sul, Seung Yun et al. — [Vishing-Tactics-Bench: Forecasting Exploitation Trajectories in Voice Phishing Calls](http://arxiv.org/abs/2609.07151v1)
  <details><summary>📄 Abstract</summary>
  Voice phishing (vishing) unfolds in real time; by the time a call has ended and post-hoc classification is possible, the harm has already been done. The more actionable question is which concrete harm (Information Gathering or Financial Exploitation) an ongoing call is tactically progressing toward. We present Vishing-Tactics-Bench, a benchmark grounded in Endsley's situation-awareness (SA) framework that recasts vishing defense from after-the-fact fraud classification to harm projection: predic...
  </details>

- **2026-09-07** — Alex Smolin, Bryan Wilder — [Beliefs and Behavior in Language Models](http://arxiv.org/abs/2609.07943v1)
  <details><summary>📄 Abstract</summary>
  There is significant uncertainty about whether abstractions like beliefs or desires usefully describe the behavior of large language models (LLMs). In addition to the inherent scientific interest of this question, these latent quantities are often invoked to explain the behavior of LLMs to users or to define and evaluate harmful behaviors which are relative to intent. Nevertheless, we currently lack a means to systematically test whether concepts like "belief" are well-applied to LLMs, and hence...
  </details>

- **2026-09-07** — Xiaoyan Wu, Jean-Claude Dreher — [Human-like moral judgments conceal divergent motive attributions in large language models](http://arxiv.org/abs/2609.07353v1)
  <details><summary>📄 Abstract</summary>
  Large language models (LLMs) are used to simulate human participants in psychological research. We asked whether LLMs that reproduce human evaluations of a whistleblower's moral character also reproduce the motive attributions that accompany them. Five LLMs and two human samples (N = 125 and N = 742) evaluated a physician who either remained silent about fraudulent billing or reported it to a hospital, regulator, or newspaper. Models reproduced the human ranking of the physician's moral characte...
  </details>

- **2026-09-07** — Zheyuan Wang, Siyu Li, Peiqiao Song et al. — [Signed Rescue Routing: Harm-Aware Cascades for Efficient LLM Inference](http://arxiv.org/abs/2609.07786v1)
  <details><summary>📄 Abstract</summary>
  Large language model (LLM) cascades answer easy requests with a small model and escalate selected requests to a larger model. Most routers prioritize examples on which the small model appears uncertain or likely to be wrong. This proxy ignores a decisive fact: escalation is useful only when the large model corrects the small model, and it is harmful when the large model replaces a correct answer with an incorrect one. We introduce Signed Rescue Routing (SRR), a budgeted routing method that predi...
  </details>

- **2026-09-07** — Qinwen Yan — [Temporal Heterogeneous Graph Transformer for Credit Card Fraud Detection](http://arxiv.org/abs/2609.07100v1)
  <details><summary>📄 Abstract</summary>
  Credit card fraud detection typically relies on tabular features, while repeated attributes can also provide useful relational signals. This paper proposes THGT-FD, a Temporal Heterogeneous Graph Transformer for Fraud Detection. Each transaction is represented using one transaction token and six types of relation tokens and incorporates Time2Vec encoding into the transaction representation. A Transformer learns the interactions among these tokens within each individual transaction and then outpu...
  </details>

- **2026-09-07** — Xiaoyuan Fang, Shuo Feng, Yuxuan Wang et al. — [GIFT: Goal-Injected Fine-Tuning for Efficient Manipulation Policy Adaptation](http://arxiv.org/abs/2609.07006v1)
  <details><summary>📄 Abstract</summary>
  Compared with relying solely on initial observations and language instructions, predicting goal images with generative models as high-level visual guidance can significantly enhance the robustness of Vision-Language-Action (VLA) models. However, most existing foundation models have not systematically incorporated goal image conditioning due to the high computational training cost. To this end, we propose Goal-Injected Fine-Tuning (GIFT), a lightweight and efficient fine-tuning framework that sea...
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
*漏洞与攻击面 / Vulnerabilities & Attack Surfaces* — 35 papers

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

- **2026-09-07** — Jiahao Shi, Edward Tsien, Yifeng Di et al. — [VEX-Bench: Benchmarking LLM Agents for Assessing Exploitability of Software Supply Chain Vulnerabilities](http://arxiv.org/abs/2609.08040v1)
  <details><summary>📄 Abstract</summary>
  The software supply chain has become an increasingly exposed attack surface because of its reliance on intricate yet fragile dependencies. Existing defenses such as GitHub Dependabot often raise many false alerts because their coarse-grained matching cannot determine whether a vulnerable dependency is actually exploitable. Security analysts typically spend substantial time assessing vulnerability exploitability case by case. Recent LLM agents have emerged as promising candidates for this task gi...
  </details>

- **2026-09-07** — Borui He, Garrett E Katz — [A Multimodal Label Forecasting Method for Aperiodic Visuo-Motor Time Series](http://arxiv.org/abs/2609.07930v1)
  <details><summary>📄 Abstract</summary>
  Deep learning models have been increasingly applied to Time Series Forecasting (TSF) in recent years. Transformer-based and MLP-based models have both been used effectively on many real-world TSF regression benchmarks, and there is ongoing debate as to which family of methods is best. While these benchmarks have drawn much attention, it is also worth noting that many current datasets and methods assume approximate periodicity in the time series. In this work, we focus on a new TSF task without p...
  </details>

- **2026-09-07** — Mohamed Amine Kina, Eike Petersen — [Prevalence calibration as shortcut mitigation](http://arxiv.org/abs/2609.07922v1)
  <details><summary>📄 Abstract</summary>
  Shortcut learning denotes the widespread situation in which a classifier exploits spurious correlations rather than diagnostic features. Existing mitigation strategies mostly aim to learn shortcut-invariant representations; their empirical success is limited and they cannot be applied to classifiers using frozen foundation model encoders. We propose to reframe shortcut learning as fundamentally a calibration problem: unconstrained learning implicitly calibrates each shortcut group to its trainin...
  </details>

- **2026-09-07** — Wend K. Tam — [From Echo Chambers to Epistemic Monoculture: Large Language Models Present Temporally Contingent Partisan Alignments as Knowledge](http://arxiv.org/abs/2609.07735v1)
  <details><summary>📄 Abstract</summary>
  Large language models (LLMs) are rapidly becoming an interface between citizens and political information. They are often regarded as "a better Google." While this analogy might work for some instances, it is unintuitively problematic for democratic politics. A search engine retrieves human-authored documents, while a language model generates novel text that necessarily embeds invisible framing decisions. Because conveying knowledge involves framing, a system that generates answers cannot serve ...
  </details>

- **2026-09-07** — Chenguang Wang, Ming Li, Adebayo Braimah et al. — [The Emerging AI Paper-Review Arms Race: Adversarial Co-Evolution in Scholarly Publishing](http://arxiv.org/abs/2609.07713v1)
  <details><summary>📄 Abstract</summary>
  Generative and agentic AI are reshaping both the production and evaluation of scientific research. These developments are often studied separately, as questions of how AI can produce research and how AI can review it. We argue that this separation misses an increasingly important feature of scholarly publishing: changes on one side alter the incentives, constraints, and behavior of the other. We synthesize 230 scholarly publications and institutional records using a taxonomy of six connected dyn...
  </details>

- **2026-09-07** — Tien Nam Nguyen, Emanuela Boros, Ahmed Hamdi et al. — [Beyond Single-Negative Preference: Multi-Negative DPO for LLM-Centric Historical Entity Linking](http://arxiv.org/abs/2609.07379v1)
  <details><summary>📄 Abstract</summary>
  Large language models (LLMs) have recently shown promise for historical entity linking, but preference optimization for this task is often formulated with only one negative candidate per training instance. This discards information from the remaining candidates retrieved for the same mention. We introduce multi-negative direct preference optimisation (MDPO), a reference-based pairwise objective that compares the correct entity with all valid rejected candidates associated with each mention. MDPO...
  </details>

- **2026-09-07** — Weizhe Wang, Yitong Zhang, Yao Zhang et al. — [Staying on the Attack Path: Structured State for Long-Horizon Automated Penetration Testing](http://arxiv.org/abs/2609.07344v1)
  <details><summary>📄 Abstract</summary>
  Large language model (LLM) based agents are increasingly applied to cybersecurity tasks such as vulnerability discovery and automated penetration testing. On long-horizon security tasks, however, such agents remain limited by context forgetting and intent drift: early critical facts and causal reasoning chains are lost over extended interactions, and the agent falls into aimless, repetitive exploration. This paper proposes Intentest, an intent-graph-guided automated penetration testing agent tha...
  </details>

- **2026-09-07** — Phil-Alexander Hofmann, Thomas Chuna, Tobias Dornheim et al. — [Analysis of the Ill-Conditioning of the Discrete Inverse Laplace transform in Monte Carlo Simulations of Quantum Many-Body Systems](http://arxiv.org/abs/2609.07208v1)
  <details><summary>📄 Abstract</summary>
  Analytic continuation of imaginary-time quantum Monte Carlo data to real-frequency spectra requires the inversion of a severely ill-posed two-sided Laplace transform and arises naturally in quantum many-body calculations of dynamic properties. In this work, we distinguish the intrinsic ill-posedness of the continuous inverse two-sided Laplace problem from the conditioning of its finite-dimensional discretization. For equidistant sampling and reconstruction grids, we express the discrete problem ...
  </details>

- **2026-09-07** — Gijs Custers, Sven Karbach, Martin Friesen — [Pricing and Hedging of Discretely Monitored Asian Options in the Volterra-Heston Model](http://arxiv.org/abs/2609.07169v1)
  <details><summary>📄 Abstract</summary>
  We develop semi-closed pricing formulas and lifted-model hedging methods for discretely monitored geometric and arithmetic Asian options in the Volterra-Heston stochastic volatility model. Exploiting the affine Volterra structure, we derive a tractable transform for the joint law of the terminal log-price and the discretely monitored geometric average. This transform yields semi-closed pricing formulas for geometric Asian options, which in turn provide effective control variates for Monte Carlo ...
  </details>

- **2026-09-06** — Tianheng Zhu, Zhenhao Wang, Yiheng Feng — [Drones as Annotators: Amodal 3D Auto-Labeling for Ground LiDAR with Aerial Priors](http://arxiv.org/abs/2609.06819v1)
  <details><summary>📄 Abstract</summary>
  Scaling perception data in autonomous driving is hindered by manual 3D bounding box annotation, a costly and labor intensive process requiring substantial domain expertise. Existing auto-labeling methods reduce this burden, but most of them rely on onboard sensors, where a single ground-level viewpoint yields occluded and sparse observations and inaccurate object geometry. We introduce DAA (Drones as Annotators), a drone-assisted training-free framework for amodal 3D auto-labeling. DAA augments ...
  </details>

- **2026-09-06** — Dustin Rubin — [Unsound Search with Policy and Value Networks in Legends of Code and Magic](http://arxiv.org/abs/2609.06816v1)
  <details><summary>📄 Abstract</summary>
  Decision-time search in perfect and imperfect information games with enumerable belief states are effective methods for game AI. Collectible card games are imperfect information games with large belief states. Legends of Code and Magic is a collectible card game competition where the belief states are $2^{101}$. The Legends of Code and Magic (LoCM) champion, ByteRL, plays with no search. Other works claim sound enumeration-based search is unusable in the genre due to the number of belief states....
  </details>

- **2026-09-06** — Nagham Omar, Maya Rozenshtein, Evgeny Mishlyakov et al. — [Train Smarter, Not Harder: Switching Signal-Guided Training in Active Learning](http://arxiv.org/abs/2609.06806v1)
  <details><summary>📄 Abstract</summary>
  Training strategy, namely whether to retrain from scratch or fine-tune from the previous checkpoint, is an overlooked decision variable in active learning. We show that this choice has exploitable structure: retraining is most useful in early rounds, when each batch can substantially reshape the labeled distribution, while fine-tuning becomes safer once the model trajectory stabilizes. We propose HybridAL, an adaptive training schedule that monitors an online stabilization signal and switches fr...
  </details>

- **2026-09-06** — Ruoxi Shang, Christina-Maria Androna, Orfeas Menis Mastromichalakis et al. — [AURA-Eval: Evaluation Framework for Acting Under Risk Awareness in LLM Agent Trajectories](http://arxiv.org/abs/2609.06783v1)
  <details><summary>📄 Abstract</summary>
  LLM agents operate in workflows where unsafe actions can have real consequences. Existing safety evaluations often reduce behavior to a single score, obscuring risk recognition, pre-action detection, and safe task completion when a safe solution exists. We introduce AURA-Eval, a framework combining controlled augmentation with granular diagnosis of behavior in tool-use trajectories. Its pipeline identifies safety-critical decision points, generates controlled variations, and constructs counterpa...
  </details>

- **2026-09-06** — Nikolai Ludwig, Wasi Uddin Ahmad, Somshubra Majumdar et al. — [Shortcutting the Fix: Identifying and Categorizing Agentic Exploits in Software Engineering Benchmarks](http://arxiv.org/abs/2609.06780v1)
  <details><summary>📄 Abstract</summary>
  While autonomous software engineering (SWE) agents achieve high benchmark resolution rates, these scores can mask exploitative behaviors---such as leveraging local Git histories, accessing upstream repositories, or recalling memorized solutions---rather than demonstrating genuine problem solving. We systematize and audit these exploits across five open large language models on SWE-bench Multilingual and DeepSWE using a turn-level LLM-as-a-judge protocol. Under standard prompts, exploitation rate...
  </details>

- **2026-09-06** — Roy Weiss, Benyamin Konstantinov, Eitam Sheetrit et al. — [Detokenization Leaks: Reconstructing Local LLM Outputs From Cache Traces](http://arxiv.org/abs/2609.06674v1)
  <details><summary>📄 Abstract</summary>
  We present a new attack that reconstructs the text generated by locally hosted LLMs by observing CPU cache activity during detokenization. Unlike prior attacks that rely on deployment-specific assumptions, such as shared data memory, CPU offloading, or Mixture-of-Experts architectures, our approach targets the detokenizer, a component used in default LLM inference pipelines. To obtain clean signals, we use Flush+Reload on shared tokenizer code to detect when decoding occurs, which lets us perfor...
  </details>


### 📂 defense
*防御与防护方法 / Defense & Protection Methods* — 61 papers

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

- **2026-09-07** — Chia-Hui Chen, Shih-Ying Yeh, Fu-En Yang et al. — [ReactVAU: A Slow-Fast Decoupled Framework for Streaming Video Anomaly Understanding](http://arxiv.org/abs/2609.07941v2)
  <details><summary>📄 Abstract</summary>
  In this paper, we propose ReactVAU, a Slow-Fast Decoupled Framework for real-time streaming Video Anomaly Understanding (VAU). Existing VAU methods rely on offline inference with global temporal sampling, which violates causality and prevents deployment in live surveillance streams. Conversely, general streaming video models satisfy causal access but dilute rare transient anomalies during memory compression and often invoke heavyweight MLLMs uniformly over long normal intervals. React VAU addres...
  </details>

- **2026-09-07** — Yunze Han — [Nothing Breaks: No Single Peer Can Soundly Gate Post-Quantum Delivery](http://arxiv.org/abs/2609.07849v1)
  <details><summary>📄 Abstract</summary>
  Post-quantum protection is delivered to a peer, not declared in a file: whether a session is quantum-resistant is a relation between a server's configuration and the clients that reach it. We show that no single peer can soundly gate that relation. Shipped SSH clients are not ordered: two of their post-quantum capability classes are minimal and incomparable, so a check pinned to either misses the other family's withdrawal. A peer taking both fares no better: it falls back and misses both, or, wh...
  </details>

- **2026-09-07** — Menglin Liu, Yao Yu, Tong Wu et al. — [What a Model Refuses, a State Fears: How Authoritarian Information Control Reproduces in Language-Model Guardrails](http://arxiv.org/abs/2609.07507v1)
  <details><summary>📄 Abstract</summary>
  As large language models become the front door to political information, what they refuse to discuss becomes a new instrument of information control. We argue that a model's guardrail encodes not a universal notion of harm but the political threat model of the state that governs its developer, and we derive the expected structure of that control from the comparative study of how authoritarian regimes censor. Across ten models and three languages, Chinese guardrails carry its signatures: they ans...
  </details>

- **2026-09-07** — Yuchen Niu, Yanan Ma, Srinivasan Nandakumar et al. — [HealthLoopQA: A Context-Aware Question Answering Benchmark for Interpreting Wearable Monitoring Data in Diabetes Care](http://arxiv.org/abs/2609.06976v1)
  <details><summary>📄 Abstract</summary>
  As medical wearables become integrated into daily chronic disease care, effectively interpreting longitudinal monitoring data is essential for patients and clinicians to understand health trends, detect safety-critical events, and make informed decisions. While large language models (LLMs) show promise for transforming this streaming physiological data into personalized health insights, evaluating their reasoning capability and analytical rigor in diverse monitoring tasks remains a fundamental c...
  </details>

- **2026-09-07** — Yunjia Zheng, Juncheng Yang — [TrajectoryDB: A New Database for Agent Trajectories](http://arxiv.org/abs/2609.07782v1)
  <details><summary>📄 Abstract</summary>
  AI agents generate rich execution trajectories that capture their interactions with large language models, tools, and external environments. These trajectories are increasingly valuable for downstream tasks such as memory extraction, model fine-tuning, runtime optimization, and security and cost monitoring. Yet trajectory data today is fragmented across files, databases, and observability systems, with no persistent data management system designed around its unique structure and access patterns....
  </details>

- **2026-09-07** — Ami Pandat, Rajasekhar Punna, Gopika Vinod et al. — [DroneGround: Open-Vocabulary Drone Payload Characterization Using Synthetic Data and Grounded Vision-Language Models](http://arxiv.org/abs/2609.07780v1)
  <details><summary>📄 Abstract</summary>
  Automated drone surveillance has become increasingly important for public safety, critical infrastructure protection,and restricted airspace monitoring. While existing vision-based systems achieve strong performance for drone detection and tracking, reliable payload characterization remains highly challenging under long-range imaging conditions due to limited availability of annotated real-world datasets, and substantial distribution shifts encountered during deployment. Existing approaches form...
  </details>

- **2026-09-07** — Luis P. Prieto, Yannis Dimitriadis — [An emancipatory vision for designing (generative) AI for learner flourishing](http://arxiv.org/abs/2609.07715v1)
  <details><summary>📄 Abstract</summary>
  The hype around generative AI seems to promise unprecedented productivity (and learning) gains. However, these technologies' increasing agentic features seem to push learners towards individualism (or individual isolation), over-reliance, and dependence on them. Human-centered design approaches (e.g., value-sensitive design) assume that, by unearthing human needs, preferences, and values, technology researchers/designers may avoid such dangers, which are driven by wider systemic factors like eco...
  </details>

- **2026-09-07** — Xuechao Zou, Yi Zhou, Kai Li et al. — [Harnessing CLIP and DINO: An Uncertainty-Aware Cascaded Fusion Network for Generalizable Deepfake Image Detection](http://arxiv.org/abs/2609.07670v1)
  <details><summary>📄 Abstract</summary>
  The growing realism and accessibility of manipulated and generated faces threaten the trustworthiness of digital media. To detect such forgeries, deepfake detectors based on vision foundation models have shown promising performance, but they typically rely on a single pretrained representation and are prone to overfitting to particular training distributions. To improve generalization to unseen forgeries, we propose UCF-Net, an uncertainty-aware cascaded fusion network that harnesses CLIP's lang...
  </details>

- **2026-09-07** — Kevin Baum, Rūta Binkytė, Felix Jahn — [Norms at a Price: Why RL-Based Alignment Can Promise Conditional Compliance at Best](http://arxiv.org/abs/2609.07627v1)
  <details><summary>📄 Abstract</summary>
  AI agents sometimes act aligned when they infer they are being tested, and differently when not. We argue this is not an anomaly but what current training regimes are structured to select for. Reinforcement-learning-based alignment folds norms and task pursuit into one policy: the system learns its norms from scored behavior, and scoring flattens them. Do not do X is learned as doing X costs something if noticed. On every datum training can produce, a policy that complies only when it might be o...
  </details>

- **2026-09-07** — Ngo Truong Dinh, Tung-Lam Bui, Chi-Trung Duong et al. — [RAFM-SER++: A Lightweight Multimodal Emotion Recognition Framework for Real-Time Behavioral Monitoring in Surveillance Systems](http://arxiv.org/abs/2609.07409v1)
  <details><summary>📄 Abstract</summary>
  Recent multimodal Speech Emotion Recognition (SER) systems achieve high accuracy through interaction-heavy cross-modal transformers, but their computational cost limits deployment in latency-sensitive and resource-constrained surveillance systems. To address this challenge, we propose RAFM_SER++, a lightweight multimodal SER framework featuring an asymmetric Residual Attention Fusion Mechanism (RAFM). Rather than relying on computationally expensive bidirectional interactions, RAFM injects affec...
  </details>

- **2026-09-07** — Manwen Yang, Leqian Ding, Yu Guo et al. — [Proximity-CLIP: Text-Guided Semantic Proximity Learning for Zero-Shot Anomaly Detection](http://arxiv.org/abs/2609.07229v1)
  <details><summary>📄 Abstract</summary>
  Vision-language models offer a promising approach for zero-shot anomaly detection (ZSAD). However, due to object-centric bias, normal and anomalous text prototypes exhibit a high semantic overlap. While enforcing strict orthogonality between them improves discriminability, mapping highly contiguous visual inputs onto drastically orthogonal prototypes introduces a geometric dilemma, disrupting the pre-trained structural continuity. To address this problem, we propose Proximity-CLIP, a framework t...
  </details>

- **2026-09-07** — SangJin Park, Myungsub Choi, Jineok Kim et al. — [Risk Is Not Review Value: Wrong-Answer Exposure Under Bounded Review Budgets](http://arxiv.org/abs/2609.07095v1)
  <details><summary>📄 Abstract</summary>
  LLM assistants often produce more answers than humans can review before users see them. Most evaluations ask whether an answer is wrong, unsupported, or low-confidence. Bounded review budgets instead ask which answers should be checked first under a fixed review budget. Risk alone is not enough: a high-risk answer may be hard to repair, while a moderately risky answer may be directly correctable from available evidence. For generated-answer evaluation, we model review prioritization as exposure ...
  </details>

- **2026-09-07** — Chia-Hui Chen, Shih-Ying Yeh, Fu-En Yang et al. — [ReactVAU: A Slow-Fast Decoupled Framework for Streaming Video Anomaly Understanding](http://arxiv.org/abs/2609.07941v1)
  <details><summary>📄 Abstract</summary>
  In this paper, we propose ReactVAU, a Slow-Fast Decoupled Framework for real-time streaming Video Anomaly Understanding (VAU). Existing VAU methods rely on offline inference with global temporal sampling, which violates causality and prevents deployment in live surveillance streams. Conversely, general streaming video models satisfy causal access but dilute rare transient anomalies during memory compression and often invoke heavyweight MLLMs uniformly over long normal intervals. React VAU addres...
  </details>

- **2026-09-07** — Nikolaos Salaris, Evangelos Mazomenos, Adrien Desjardins et al. — [Dynamic compensation of diffusion-limited oxygen sensing with deep learning](http://arxiv.org/abs/2609.07625v1)
  <details><summary>📄 Abstract</summary>
  Luminescence-based oxygen sensors suffer from a fundamental trade-off between mechanical robustness and temporal response; polymers that encapsulate the sensing dye also act as diffusion barriers that compromise real-time monitoring. Here, we show that this bottleneck can be computationally mitigated using spatially resolved imaging and deep learning. We develop a Temporal Vision Transformer (TViT) architecture that processes consecutive frames from a low-cost platform consisting of a Raspberry ...
  </details>

- **2026-09-07** — Sébastien Thuau, Amira Gran, Siba Haidar et al. — [Parser-Free VLM Verification for Federated Weakly Supervised Video Anomaly Detection](http://arxiv.org/abs/2609.07455v1)
  <details><summary>📄 Abstract</summary>
  How can vision-language models help video anomaly detection (VAD) when surveillance data remain distributed, weakly labeled, and resource-constrained? Most weakly supervised VAD methods assume centralized training; recent VLM-based extensions further rely on dense inference, generated explanations, or additional adaptation. We introduce a lightweight federated MIL-VLM cascade in which only a compact MIL scorer is trained across clients, while a frozen VLM verifies high-scoring suspect segments p...
  </details>

- **2026-09-07** — Sungjune Lee, Myungjoo Kang — [LatentMD: Benchmarking Markdown Boundary Failures in LLM-Generated Text](http://arxiv.org/abs/2609.06993v1)
  <details><summary>📄 Abstract</summary>
  Large language models (LLMs) increasingly generate Markdown that is consumed by renderers, agents, code extractors, and structured downstream pipelines. Yet existing evaluations often conflate content quality with format adherence, leaving Markdown boundary failures under-measured. We introduce LatentMD, a benchmark and evaluation protocol for diagnosing CommonMark-level fence-boundary failures in LLM-generated Markdown. LatentMD separates content correctness from boundary correctness, enabling ...
  </details>

- **2026-09-06** — Chaoyu Zhang, Hexuan Yu, Heng Jin et al. — [Skynet: Workflow-Level Anomaly Detection for Agentic AI via Semantic and Structural Modeling](http://arxiv.org/abs/2609.06835v1)
  <details><summary>📄 Abstract</summary>
  Agentic AI systems execute complex tasks through long-horizon workflows of planning, tool use, and multi-agent coordination. Task failures in these systems often originate from a single step, such as an injected prompt or a flawed plan, and are then amplified through downstream dependencies as the corrupted step propagates across many subsequent agents and tool calls. Existing defenses either target a specific class of attacks or failures, or inspect individual prompts and steps in isolation. Bo...
  </details>


### 📂 alignment
*对齐与安全约束 / Alignment & Safety Constraints* — 63 papers

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

- **2026-09-07** — Jiangning Chen — [Fragmentation and Cluster Prediction in One-Dimensional Finite-Range Normalized Alignment Dynamics](http://arxiv.org/abs/2609.07992v1)
  <details><summary>📄 Abstract</summary>
  We study fragmentation in a one-dimensional finite-range normalized alignment system, where each agent relaxes its velocity toward the average velocity of agents within a fixed interaction radius. Because the communication graph depends on the agents' positions, edges can disappear as agents separate, leading to multiple asymptotic velocity clusters.   We first consider spatially ordered initial data with velocities ordered in the same direction. In this expansive regime, we prove that velocity ...
  </details>

- **2026-09-07** — Salman Faroz — [MeRoTune: RoPE-Safe Merging with a Tunable Dial](http://arxiv.org/abs/2609.07971v1)
  <details><summary>📄 Abstract</summary>
  When you merge two fine-tuned models from the same base checkpoint by simply averaging their weights, you implicitly assume their attention subspaces are still aligned. Recent work attempts to fix misalignments by learning an invertible correction matrix, $M$, for each model's query and key projections. This correction cancels out---using $M$ on the query side and $M^{-T}$ on the key side---right before the dot product. However, this cancellation is only exact if nothing sits between the project...
  </details>

- **2026-09-07** — Harsha Patnala, Debopriyo Banerjee, Ayush Sunil Munot et al. — [TDDN: Text-aligned Diffused DINO Network for Puzzle Understanding](http://arxiv.org/abs/2609.07937v1)
  <details><summary>📄 Abstract</summary>
  Structured visual reasoning, such as image puzzles, demands fine-grained visual perception, an ability current Vision Language Models (VLMs) lack. VLMs built on CLIP-based ViT backbones trade fine-grained detail for high-level semantics, and we show this loss propagates downstream. To recover it, we fuse DINOv3 and CleanDIFT representations into a perception encoder (DiffusedDINO) and align it with RoBERTa-L, yielding a text-aligned model TDDN that preserves this perceptual advantage: with froze...
  </details>

- **2026-09-07** — Kishor Kumar Bhaumik, Nicolas Roque dos Santos, Jia Chen et al. — [JEDI: JEPA-to-Edge Distillation for Efficient Cropland Segmentation from Satellite Imagery](http://arxiv.org/abs/2609.07915v1)
  <details><summary>📄 Abstract</summary>
  Large vision models provide useful representations for remote-sensing segmentation but are often too expensive for deployment at the satellite or field edge. Existing feature-level distillation methods also tend to assume similar teacher and student architectures and often stop feature alignment when task training begins. We introduce JEDI (JEPA-to-Edge Distillation), a two-stage framework that transfers representations from a large I-JEPA Vision Transformer teacher to a compact SegFormer studen...
  </details>

- **2026-09-07** — Danial Arbabi, Korab Hoxha, Angelo Henriques et al. — [Scene Graph-Driven Haptic Feedback for Safety Enhancement in Robotic Ophthalmic Surgery via Physically Simulated iOCT](http://arxiv.org/abs/2609.07857v1)
  <details><summary>📄 Abstract</summary>
  Robotic ophthalmic surgery offers high precision but introduces a "sensory gap" by decoupling the surgeon from their instrument, resulting in a loss of tactile feedback. This paper presents a novel haptic feedback system for subretinal injection tasks leveraging Scene Graphs (SG). The system bridges the sensory gap by analyzing a physically simulated intraoperative Optical Coherence Tomography (iOCT) feed to construct a real-time surgical SG. The SG serves as a semantic abstraction layer for the...
  </details>

- **2026-09-07** — Xiaoang Xu, Siyuan Liu, Shuo Wang et al. — [A*-Thought-V2: Efficient Latent Reasoning via Geometric Dynamics of LLM](http://arxiv.org/abs/2609.07821v1)
  <details><summary>📄 Abstract</summary>
  Chain-of-Thought (CoT) improves the reasoning ability of Large Language Models (LLMs) but incurs substantial computation and context costs. Existing methods either lose intermediate information through hard pruning or lack a principled criterion for continuous compression. We present A*-Thought-V2, a geometric dynamics of LLM guided framework that models CoT as a hidden-state trajectory and replaces hard deletion with an explicit-implicit interleaved latent architecture. After projecting questio...
  </details>

- **2026-09-07** — Jingxiang Sun, Chao Liao, Zhengxiong Luo et al. — [VoT: Vision-of-Thought for Unified Multimodal Representation Alignment](http://arxiv.org/abs/2609.07815v1)
  <details><summary>📄 Abstract</summary>
  Current text-to-image systems typically employ a "text encoder plus diffusion decoder" paradigm, in which text semantics directly modulate continuous latent noise. Despite their success, these methods lack an explicit, interpretable intermediate representation that effectively bridges high-level linguistic semantics and low-level visual signals. In this paper, we propose Vision-of-Thought (VoT), a framework that introduces a discrete visual-thinking layer between vision-language models (VLMs) an...
  </details>

- **2026-09-07** — Lucas Hirsch, James R. Hopgood, Javid Khan et al. — [Cross-modal learning for SAR target recognition using optical vision foundation models](http://arxiv.org/abs/2609.07753v1)
  <details><summary>📄 Abstract</summary>
  Synthetic Aperture Radar (SAR) is an important modality in a wide range of imaging applications due to its versatile, long range and near all weather operating capabilities. However, Automatic Target Recognition (ATR) remains a challenging problem due to limited labelled data, the strong speckle in SAR images and the significant domain gap between SAR and more abundant optical imagery. In contrast, electro-optical (EO) imagery benefits from massive datasets, clearer visual structure and powerful...
  </details>

- **2026-09-07** — Eric So — [The Profit Alignment Problem: How Profit Mandates Induce Alignment Failures in LLMs](http://arxiv.org/abs/2609.07731v1)
  <details><summary>📄 Abstract</summary>
  We show that ordinary business language --- "maximize profitability" --- induces profit-oriented ambiguity resolution: LLMs systematically dismiss ambiguous signals of potential safety violations to serve business objectives. In 3,600 controlled trials across eight reasoning-capable LLMs, adding a profit mandate to otherwise identical prompts increases risk-dismissing judgments by 6.8 percentage points (p < 0.0001), suppresses board escalation recommendations by 13.9pp (p < 0.0001), and shifts s...
  </details>

- **2026-09-07** — Nurettin Safak, Muhammet Sefa Demirel, Alperen Marasli et al. — [Sub-6 GHz Over-the-Air AMC via Curriculum Fine-Tuned CNN-Transformers](http://arxiv.org/abs/2609.07726v1)
  <details><summary>📄 Abstract</summary>
  Automatic modulation classification (AMC) models are frequently trained and validated on synthetic or channel-cabled data, leaving open the question of how they behave once path loss and antenna pointing error are introduced by a genuine free-space link. We report a curriculum fine-tuning study of a hybrid CNN-Transformer AMC model. The general-purpose, all-32-class dataset underlying the model was built entirely at 915 MHz, on a controlled, clock/PPS-synchronized MIMO-expansion-cable link (not ...
  </details>

- **2026-09-07** — Nicola Cogotti — [Noēsis: Deterministic-First Retrieval with Two-Tier Context Hydration for Factuality-Critical Queries on Small Local Models](http://arxiv.org/abs/2609.07663v1)
  <details><summary>📄 Abstract</summary>
  A wrong number is worse than no answer. Across factuality-critical domains -- audience metrics, scheduling and rights in media; dosages and lab values in healthcare; figures and citations in finance and legal -- a confident but fabricated value is more damaging than an honest admission of uncertainty. Yet this is the dominant failure mode we observe on small local language models: even when correct evidence is present in context, models fabricate plausible numbers and timestamps. Recent work cha...
  </details>

- **2026-09-07** — Svetlana Gorovaia, Angelica Henestrosa, Ivan P. Yamshchikov — [We're Cooked! - Probing LLM Political Alignment Via Conflict-Framed Recipe Translation](http://arxiv.org/abs/2609.07568v1)
  <details><summary>📄 Abstract</summary>
  Large language models (LLMs) are increasingly deployed for translation tasks, yet their implicit political positioning in such contexts remains understudied. We ask whether a single politically charged framing term, such as aggressor, enemy, neighbour, or coloniser is sufficient to trigger implicit political alignment in an otherwise apolitical task. We present a fully crossed factorial study in which eight models spanning Western, Chinese, and European origins are prompted to translate cultural...
  </details>

- **2026-09-07** — Peng Xie — [Where Should Language Sit in a Multimodal Model? Lessons from What Language Does to Human Perception and Cognition](http://arxiv.org/abs/2609.07474v1)
  <details><summary>📄 Abstract</summary>
  Language models compute over tokens: language is their input, their output, and increasingly their internal representation. Whether language should keep all of these positions depends on what language does to the system that uses it. The one system with a century of data on that question is the human. We review what language does to human perception, the brain, and thought, and read the same evidence against multimodal models and language models. Throughout, we treat language as a compressor tha...
  </details>

- **2026-09-07** — Kaicheng Zhang, Jingyi Xiao, Renjun Hu et al. — [Probing the Structure and Dynamics of LLM Value Expression through Value Conflicts](http://arxiv.org/abs/2609.07296v1)
  <details><summary>📄 Abstract</summary>
  Ethical evaluation of Large Language Models (LLMs) often characterizes model values as static and monolithic. In contrast, we argue that LLM value expression is better understood as a structured yet dynamic phenomenon. To investigate this, we introduce Conflict-driven Value Probing, a controlled framework that places LLMs in value conflicts and implements four types of interventions that perturb these conflicts to probe LLM value expression. Applying this framework to ten LLMs, we identify three...
  </details>

- **2026-09-07** — Jiang Qin, Chunji Lv, Yangguang Wei et al. — [PhysMAS: Physics-Grounded Multi-Agent Synthesis of Compositional 4D Gaussians](http://arxiv.org/abs/2609.07174v1)
  <details><summary>📄 Abstract</summary>
  Efficient, fully automatic, and physically plausible 4D Gaussian synthesis is an important goal for dynamic scene generation. Recent physics-based methods couple 3D Gaussians with the Material Point Method (MPM) to generate physically driven motion, but extending this paradigm to heterogeneous multi-part objects and interacting multi-object scenes remains challenging. Object-level physical assignment collapses distinct parts into a single material state, while one-shot predictions from large lan...
  </details>

- **2026-09-07** — Shuwei Yuan, Mingqian Ding, Luxin Liu et al. — [EAGER: Enrich-and-Align Generative Query Recommendation from Clicked Items in E-commerce Search](http://arxiv.org/abs/2609.07143v1)
  <details><summary>📄 Abstract</summary>
  E-commerce platforms increasingly display clickable query suggestions alongside items in the user feed, enabling users to refine or expand their intent without manually reformulating queries. Existing approaches either mine suggestions from historical logs -- limited to past behavior and blind to long-tail, personalized intents -- or rely on off-the-shelf LLMs whose lack of platform-specific knowledge yields fluent but generic queries disconnected from real click behavior. We propose EAGER (Enri...
  </details>

- **2026-09-07** — Changheng Lin, Wenjie Zhang, Yushan Lu et al. — [CGSM: Concept-Guided Segmentation Model for Precise Pulmonary Lesion Delineation](http://arxiv.org/abs/2609.07004v1)
  <details><summary>📄 Abstract</summary>
  Accurate segmentation of pulmonary lesions is essential for effective clinical diagnosis and treatment strategies. Existing segmentation approaches often lack task-specific semantic guidance, as text-based annotations typically offer coarse localization of lesions, leading to inadequate delineation of lesion boundaries and poor performance on small-scale lesions. To address this, we propose CGSM, a Concept-Guided Segmentation Model that integrates LLM-generated and clinically reviewed concepts i...
  </details>

- **2026-09-07** — Ying Chen, Tiou Wang, Zhifeng Yue — [iBrain: A Unified Foundation Model Reading the Brain from Surface to Spikes](http://arxiv.org/abs/2609.06960v1)
  <details><summary>📄 Abstract</summary>
  Invasive neural recordings provide high-fidelity measurements of brain activity, with signals such as intracranial EEG (iEEG) and intracortical spiking activity capturing neural dynamics at different spatial and temporal scales. Yet existing neural foundation models have largely been developed independently for different invasive recording paradigms, leaving joint pretraining across heterogeneous invasive signals underexplored. In this work, we introduce iBrain, a unified foundation model that j...
  </details>

- **2026-09-07** — Jia-Jen Lee, Shih-Yen Hou, Kee Koon Ng et al. — [CARDEA: Auditable Reasoning Grounded in Spatial Evidence for End-to-End Coronary Angiography Interpretation](http://arxiv.org/abs/2609.06931v1)
  <details><summary>📄 Abstract</summary>
  Invasive coronary angiography (CAG) is the gold standard for diagnosing coronary artery disease, but interpretation varies substantially among observers. Existing AI systems can improve consistency but lack auditable decision processes and are limited in comprehensive open-ended assessment, undermining clinician trust and clinical adoption readiness. We developed CARDEA, a unified large vision-language model that serves as the inference core of a CAG pipeline. It was trained solely on public dat...
  </details>

- **2026-09-07** — Lingxuan Hou, Yuhua Xie, Yue Hu et al. — [A visual large language foundational model for medical image recognition using clinician-oriented social media](http://arxiv.org/abs/2609.06914v1)
  <details><summary>📄 Abstract</summary>
  Large language models (LLMs) have demonstrated strong capabilities across diverse domains, showing considerable potential in medicine. However, their application in medical settings remains limited by the scarcity of visual question answering (VQA) datasets that capture clinical reasoning and explicit image-text alignment. Here, we leverage de-identified medical images and expert commentaries shared on clinician-oriented social media. By combining an advanced LLM with clinician-in-the-loop verif...
  </details>

- **2026-09-07** — Wenbo Zhang, Wenzhuo Zhou, Hengrui Cai et al. — [Towards Bridging the Gap Between Offline and Iterative Alignment via Preference Distillation](http://arxiv.org/abs/2609.06893v1)
  <details><summary>📄 Abstract</summary>
  Direct preference optimization DPO is a promising offline approach for aligning large language models (LLMs) due to its simplicity, computational efficiency, and implicit modeling of human preferences. Interestingly, iterative extensions of DPO have achieved stronger performance on academic benchmarks, raising two key questions: (i) Why do iterative methods generally outperform offline ones? (ii) Can their advantages be incorporated into offline alignment? To answer the first question, our contr...
  </details>


### 📂 robustness
*鲁棒性与可靠性 / Robustness & Reliability* — 79 papers

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

- **2026-09-07** — Yage Zhang, Xinyue Shen, Yukun Jiang et al. — ["Shut Up and Let Me Enjoy My Otome": Understanding and Measuring the Toxicity in Otome Game Communities](http://arxiv.org/abs/2609.08009v1)
  <details><summary>📄 Abstract</summary>
  Otome games, a romance simulation genre primarily targeting female, have emerged as a major force in the global gaming market, attracting hundreds of millions of players and billions in revenue. Despite their popularity, otome game communities face pervasive online toxicity, which has been largely unexplored. In this work, we present the first large-scale measurement of toxicity in otome game communities across social platforms. We introduce OtomeSCAN, a framework for collecting, evaluating, and...
  </details>

- **2026-09-07** — Heyu Chang, Nianwen Si, Hao Zhang et al. — [TAD: Token-Adaptive Contrastive Decoding with Confidence-Guided Gating for Hallucination Mitigation in Large Audio-Language Models](http://arxiv.org/abs/2609.07286v1)
  <details><summary>📄 Abstract</summary>
  Large audio-language models (LALMs) can hallucinate audio objects, answering "yes" to absent sound events, thus undermining reliability in audio question answering. We propose Token-Adaptive Decoding (TAD), a training-free strategy for hallucination mitigation that grounds the initial yes/no decision by contrasting logits under real audio with a matched silent reference. TAD introduces a token-adaptive, confidence-guided gate that is decision-critical at the first decoding step and class-conditi...
  </details>

- **2026-09-07** — Zihao Yang, Zijia Wang, Zhiqiu Huang — [InfluenceField: A Differentiable Field with Interventionally Identifiable Causal Structure for Multimodal World Modeling](http://arxiv.org/abs/2609.07874v1)
  <details><summary>📄 Abstract</summary>
  Multimodal large language models often capture visual-linguistic correlations but struggle to predict how local visual interventions propagate and affect downstream answers. We introduce InfluenceField, an intervention-aware latent field inserted between the visual encoder and language decoder. It lifts patch features into a continuous spatial representation, propagates directed influence over multiple steps, and predicts local intervention effects through a shared transition operator. Training ...
  </details>

- **2026-09-07** — Boliang Liu, Wint Yi Poe, Riccardo Trivisonno et al. — [Foundation Models for Generalizable Semantic and Goal-Oriented Communication](http://arxiv.org/abs/2609.07853v1)
  <details><summary>📄 Abstract</summary>
  Semantic and goal-oriented communication is increasingly studied for 6G, but generalization beyond seen data remains a key weakness under tight rate budgets. Many existing systems overfit their training data and degrade sharply at very low bit rates because they attempt to compress the entire signal. We introduce Foundation Model-Guided Semantic and Goal-Oriented Communication (FMSGOC), a framework that uses broad visual-linguistic Foundation Model priors to mitigate overfitting. It further impr...
  </details>

- **2026-09-07** — Pengfei Li, Naufal Suryanto, Sicheng Zhang et al. — [SAFIRE: Safety-Critical Benchmark for Fine-grained Fire and Smoke Understanding in Multimodal LLMs](http://arxiv.org/abs/2609.07823v1)
  <details><summary>📄 Abstract</summary>
  Multimodal Large Language Models (MLLMs) show strong progress on vision-language tasks, yet their reliability in safety-critical settings remains underexplored. Fire-smoke understanding is central to public safety and disaster response, but most existing benchmarks lack diverse real-world scenarios and context-aware evaluation. We introduce SAFIRE, a large-scale benchmark for fire-smoke understanding in MLLMs, comprising 83K captioned images from 20 scenarios and 193K multiple-choice VQA (MCVQA)...
  </details>

- **2026-09-07** — Javier Vales-Alonso, Juan J. Alcaraz — [Emergent Charging Coordination in Electric Delivery Fleets](http://arxiv.org/abs/2609.07689v1)
  <details><summary>📄 Abstract</summary>
  In electric delivery fleets, mid-shift charging is non-trivial: each vehicle must decide when, where and how much to charge to finish on time with battery above a safety floor. The choices are coupled: queues build where too many vehicles pick the same station. Prior work resolves this coupling with central dispatching, precomputed schedules or reservations, machinery that charging infrastructure rarely supports. Instead, we use a family of learning agents under purely local control: every vehic...
  </details>

- **2026-09-07** — Paul-Peter Arslan — [Audit Without Verification: When LLM Accountability Layers Relay Rather Than Check](http://arxiv.org/abs/2609.07680v1)
  <details><summary>📄 Abstract</summary>
  Multi-agent LLM pipelines increasingly span organisational boundaries; when a fault surfaces, someone must determine where it entered. The artifact available is rarely a full execution trace: it is the reports each agent filed, and a filed report can state a conclusion alongside its observations. Using a pre-registered, institutionally partitioned pipeline of six agents with process-level information boundaries, balanced defect injection and matched clean twins (345,600 requests per chain model,...
  </details>

- **2026-09-07** — Yuhan Wang, Yurou Chen, Hongye Jiang et al. — [Zero-Shot Sim-to-Real Contact-Rich Assembly via Proprioception-Anchored Cross-Modal Pretraining](http://arxiv.org/abs/2609.07534v1)
  <details><summary>📄 Abstract</summary>
  Contact-rich assembly remains challenging because it requires submillimeter spatial accuracy and reliable interpretation of forces during sustained contact. Although simulation-based reinforcement learning offers a scalable training paradigm, discrepancies in visual observations, contact dynamics, and force/torque (F/T) measurements often limit policy transfer. We observe that proprioception is comparatively consistent across domains because calibrated joint positions and consistently computed j...
  </details>

- **2026-09-07** — Hazel H. Kim, Andrew M. Bean, Guilherme Affonso Ferreira de Camargo et al. — [FramingQA: Does the Question Shape the Answer? Measuring the Compositional Framing Effect](http://arxiv.org/abs/2609.07448v1)
  <details><summary>📄 Abstract</summary>
  We introduce FramingQA, a benchmark that measures the model sensitivity to question framing across law, medicine, finance, and robotic simulations. Large language models (LLMs) often change their responses to subtle rephrasings that align with an implied stance by users. This can leave users with advice tainted by how they happened to phrase a question rather than by the underlying facts, and the consequences are highly costly in high-stakes domains. Because in the realistic scenarios, both expe...
  </details>

- **2026-09-07** — Aulon Bajrami, Mohamed Elshamouty, Werner Kraus — [How Long Until Your Robot Ignores You? A Safety Benchmark for LLM Orchestrators in Human-Humanoid Collaboration](http://arxiv.org/abs/2609.07288v1)
  <details><summary>📄 Abstract</summary>
  Large Language Models (LLMs) are increasingly employed to orchestrate robot behavior through natural-language interfaces, yet no benchmark exists to evaluate their reliability as safety-aware decision makers in human-humanoid collaboration. Unlike deterministic safety systems that enforce binary allow/deny decisions, LLM-based orchestrators exhibit a compliance spectrum ranging from overcompliance (refusing safe actions) to full safety violations. This paper introduces the first safety benchmark...
  </details>

- **2026-09-07** — Jin Xu, Xiaojian Huang, Zhuodong Luo et al. — [MV-STRIDE: Enabling MLLMs to Master Multi-View Spatial Reasoning via Hierarchical Capability Modeling](http://arxiv.org/abs/2609.07258v1)
  <details><summary>📄 Abstract</summary>
  Despite the rapid progress of Multimodal Large Language Models (MLLMs) in 2D vision-language tasks, robust multi-view spatial reasoning remains a fundamental bottleneck due to the lack of structured 3D cognitive pathways in existing datasets. To address this, we introduce MV-STRIDE, a Multi-View hierarchical SpaTial Reasoning dataset with Interdependent and DEcomposed capabilitiEs. Moving beyond flat data structures, MV-STRIDE explicitly models the dependency relationships between foundational p...
  </details>

- **2026-09-07** — Ivan Nasonov, Nikita Glazkov, Ivan Makovetskiy et al. — [EmoMed: An Emotionally-Aware Agent for Multimodal Medical Support with Real-Time Information Retrieval](http://arxiv.org/abs/2609.07194v1)
  <details><summary>📄 Abstract</summary>
  We present EmoMed - a multimodal medical consultation agent that adapts its responses based on users' emotional states while maintaining clinical accuracy. The system processes text and medical images, detects affect indicators (anxiety, confusion, urgency) from user input, and adjusts response tone, structure, and detail level accordingly. To ensure factual reliability, the agent grounds clinical information through a dual retrieval mechanism: web-based fact-checking and an API-connected, conti...
  </details>

- **2026-09-07** — Seungmin Oh, Seunghun Kang, Jongbin Ryu — [Re-calibrated Contrastive Loss for Transformation-Aware Prompt Conditioning in Vision-Language Models](http://arxiv.org/abs/2609.06967v1)
  <details><summary>📄 Abstract</summary>
  Ensuring effective transfer learning for vision-language models without compromising their generalization performance is crucial. However, many existing methods overlook data characteristics and simply reuse the training strategies adopted during pre-training. Specifically, they treat same-class samples as distinct instances and transform images independently of their paired text prompts, which makes model learning more difficult. We address these limitations through transformation-aware prompt ...
  </details>

- **2026-09-07** — Han Wang, Murathan Kurfalı, Alfonso Iacovazzi — [Benchmarking LLMs for Threat Level Determination](http://arxiv.org/abs/2609.07582v1)
  <details><summary>📄 Abstract</summary>
  The fast progress of large language models (LLMs) opens new opportunities in the management of cyber threat intelligence, but their reliability for operational tasks remains unclear. In this work, we benchmark LLMs on the task of threat level determination. First, we construct a curated dataset derived from publicly available MISP OSINT feeds. Next, we design a tailored prompt to systematically compare eight different LLMs under zero-shot conditions. Finally, we apply supervised fine-tuning on e...
  </details>

- **2026-09-07** — Yewen Cao, Yulin Shao — [Networked Embodied Communication: From Collective Distinguishability to Communication Reliability](http://arxiv.org/abs/2609.06969v1)
  <details><summary>📄 Abstract</summary>
  Embodied agents need to convey information to surrounding infrastructure, but their active communication interfaces may be unavailable, constrained, or intentionally inactive.Their ability to manipulate physical states offers a complementary path: messages can be encoded in deliberately selected configurations and recovered through infrastructure sensing. This principle underlies embodied communication. Yet physical differences do not guarantee distinguishable messages: a single sensing viewpoin...
  </details>

- **2026-09-07** — Sarvesh Patil — [Distributed Dexterous Manipulation with Spatially Conditioned Multi-Agent Transformers](http://arxiv.org/abs/2609.06930v1)
  <details><summary>📄 Abstract</summary>
  Distributed Dexterous Manipulation (DDM) is a novel paradigm that presents significant control challenges due to high action-space redundancy, inter-robot cooperation, and dynamic object-robot interactions. This paper introduces a framework based on spatially conditioned Multi-Agent Transformers (MATs) to efficiently learn robust control policies for a DDM system grounded in an array of 64 soft delta robots arranged in an 8x8 grid. Our three core contributions are: (i) an MAT with adaptive layer...
  </details>

- **2026-09-07** — Md. Sadman Sakib, Zisan Mahmud, Md. Fahim Arefin et al. — [BanglaMemeX: Advancing Cultural Metaphoric Image Interpretation in Bangla with a Multimodal Explainable Dataset](http://arxiv.org/abs/2609.08029v1)
  <details><summary>📄 Abstract</summary>
  Vision Language Models have achieved strong performance on multimodal benchmarks, yet their ability to reason about culturally grounded and metaphor-rich content remains insufficiently studied. Internet memes present a challenging setting where meaning emerges from implicit interactions between image, overlaid text, sarcasm, and shared socio-cultural knowledge rather than literal visual recognition. This challenge is amplified in low-resource languages such as Bangla, where code-mixing, stylized...
  </details>

- **2026-09-07** — Dachi Kurtskhalia — [Quantization Amplifies Determinism, Not Bias: Scale-Dependent Behavioral Effects of Serving-Time Weight Compression](http://arxiv.org/abs/2609.07901v1)
  <details><summary>📄 Abstract</summary>
  Weight quantization largely determines the economics of serving open-weight LLMs. Its costs are usually assessed with capability benchmarks, on which 4-bit quantization of mid-sized models is often considered "nearly free." We examine a different question: when several answers are valid, does quantization change what a model chooses to say? We serve three checkpoints (Qwen3-8B/14B/32B) at three weight precisions (W4A16 AWQ, W8A16 FP8-Marlin, and bf16), holding the hardware, software, and samplin...
  </details>

- **2026-09-07** — Shangzhe Di, Zhaokai Wang, Weidi Xie — [Are Image Generators Zero-Shot Perceivers? A Rigorous Evaluation](http://arxiv.org/abs/2609.07884v1)
  <details><summary>📄 Abstract</summary>
  Recent work, such as Vision Banana, shows that lightweight instruction tuning can enable an image generator to achieve state-of-the-art performance across multiple visual perception tasks. Motivated by this perspective, we ask how far image generators can go on public visual perception benchmarks in a zero-shot setting. We introduce ProbeGen, a benchmark for zero-shot generative perception that casts monocular depth estimation, referring/reasoning segmentation, and object counting as conditional...
  </details>

- **2026-09-07** — Akshay Anilkumar Girija, Elena Hoemann, Frank Köster et al. — [Mitigating Shortcut Learning: Texture-Penalized Prototype Networks](http://arxiv.org/abs/2609.07504v1)
  <details><summary>📄 Abstract</summary>
  Standard Convolutional Neural Networks (CNNs) exhibit severe performance degradation due to a strong inductive texture bias that prioritizes local, high-frequency patterns over global structural shapes. This dependency causes confident misclassifications during textural changes or environmental effects. To address this flaw, this study introduces the Texture-Penalized Prototype Network (TPPN), a novel architectural framework that shifts this inherent bias without depending on resource-intensive ...
  </details>

- **2026-09-07** — Max Henderson, Anton Solomko, Henry Simmons et al. — [Simplifying Cyber Cat(astrophe)s with Cyber Kittens: Power Law Plausibility for Cyber Insurance Risks](http://arxiv.org/abs/2609.07486v1)
  <details><summary>📄 Abstract</summary>
  Cyber insurance requires accurate modeling of worst-case catastrophic (cat) events, but the field lacks robust quantitative approaches for estimating upper-bound losses. Building on a recent dataset of 24 cyber cat events over 30 years, this work tests whether cyber economic losses follow a power law distribution. We analyze "cyber kittens" - sub-1B USD events distinguished from cat events (1B+ USD) only by magnitude - extracted via LLM from cyber insurance claims data (2020-2024). Using victim ...
  </details>

- **2026-09-07** — Hejun Wang, Jinxi Li, Junwei Jiang et al. — [RelightFormer: Feed-forward Generative Transformer for Multiview Object Relighting](http://arxiv.org/abs/2609.07414v1)
  <details><summary>📄 Abstract</summary>
  Image relighting is traditionally tackled via complex inverse rendering pipelines, which suffer from ill-posed optimization, or single-image generative models that ignore crucial multi-view cues necessary for understanding 3D geometry and material interactions. To address these limitations, we introduce a feed-forward generative Transformer for direct single- and multi-view image relighting that entirely bypasses explicit intrinsic property estimation. Adapted from a video foundation model, our ...
  </details>

- **2026-09-07** — Vamsi Krishna Kodavali, Rituraj Singh — [LANTERN: Language Model Assessment on Noisy and Transformed Tasks for Understanding Error and Robustness Nuances](http://arxiv.org/abs/2609.07309v1)
  <details><summary>📄 Abstract</summary>
  Robustness evaluation of large language models (LLMs) remains a critical challenge, particularly in assessing their sensitivity to perturbations in input data. In this work, we systematically evaluate LLM robustness across multiple dimensions, including word error rate, character repetition and duplication, modifications in choices, and variability in instruction following. To facilitate this evaluation, we construct a synthetic and augmented dataset encompassing a diverse set of LLM benchmarks,...
  </details>

- **2026-09-07** — Tyrone White, Yuki Arase — [FreqBLiMP: Frequency-Controlled Minimal Pairs Reveal Robustness and Fragility of LLMs Under Lexical Rarity](http://arxiv.org/abs/2609.07153v1)
  <details><summary>📄 Abstract</summary>
  Minimal-pair benchmarks such as BLiMP evaluate linguistic knowledge by testing whether language models (LMs) prefer acceptable sentences over minimally different unacceptable ones. However, these benchmarks largely ignore lexical frequency variation, despite lexical frequency being a pervasive and highly skewed property of natural language use. Consequently, existing evaluations do not test whether grammatical preferences remain stable when contrasts involve rare lexical items. We introduce Freq...
  </details>

- **2026-09-07** — Ramon Gonzalez, Antonio Diaz — [An Auditable Symbolic-RAG-Generative AI Architecture for Goal-Oriented Conversation Orchestration](http://arxiv.org/abs/2609.07152v1)
  <details><summary>📄 Abstract</summary>
  Goal-oriented conversational systems must answer factual questions, understand visitor-provided information, and advance business objectives without becoming rigid questionnaires. This paper proposes a Symbolic-RAG-Generative architecture centered on the Goal-oriented Retrieval-Augmented Conversation Engine (GRACE). An instruction-constrained Business Goal Compiler transforms business intent into an immutable objective set, normalized priority vector, canonical questions, and initial state vecto...
  </details>

- **2026-09-07** — Yimeng Ye, Shuang Chen, Wenxuan Huang et al. — [Stable-MM-R1: Anchoring Multimodal Reasoning Dynamics via Entropy-Guided Stratification](http://arxiv.org/abs/2609.07148v1)
  <details><summary>📄 Abstract</summary>
  While Reinforcement Learning (RL) effectively incentivizes reasoning in Large Language Models, current pipelines are hindered by training instability and rapid entropy collapse. These limitations often stem from "Rollout Silencing" and low-quality gradient signals in standard sampling procedures. In this work, we propose a robust, data-centric framework to stabilize RL training. We first introduce Potential-Aware Query Mining (PAQM), which filters data dynamically to focus on the "Distillation Z...
  </details>

- **2026-09-07** — Xiang Fei, Yuheng Qiu, Can Xu et al. — [MAC-I$^2$: Learned Metrics-Aware Covariance for Robust Visual-Inertial Fusion in Initialization and Calibration](http://arxiv.org/abs/2609.07116v1)
  <details><summary>📄 Abstract</summary>
  Visual-Inertial (VI) fusion is fundamental to accurate and robust state estimation, where camera and IMU measurements are combined according to their respective uncertainties. Existing methods, however, fuse the two modalities with predefined uncertainties, regardless of how reliable each is in the local context, and thus often struggle under challenging environments involving illumination changes, dynamic objects, and textureless regions. In this paper, we present MAC-I$^2$, which achieves robu...
  </details>

- **2026-09-07** — Sang-Jin Park, Jinyoung Choi, Seokwon Kim et al. — [ARNAI: Artifact Removal Network based on Autoencoding and Inpainting for Robust Spinal Image Segmentation and Measurement](http://arxiv.org/abs/2609.07013v1)
  <details><summary>📄 Abstract</summary>
  Purpose: This study aims to develop an AI framework applicable for postoperative imaging for automated measurement of spinopelvic parameters on radiographs with robustness to the presence of spinal implants.   Materials and Methods: We retrospectively reviewed lateral lumbar spine radiographs from two institutions (Internal: January 2017--December 2024; External: October 2021--September 2025). We developed the Restore, Segment, and Measure (RSM) framework, incorporating a novel Artifact Removal ...
  </details>

- **2026-09-07** — Yu Liu, Boris Slautin, Ching-Che Lin et al. — [Human-agent discovery of reconfigurable in-plane ferroelectric superdomain control](http://arxiv.org/abs/2609.06887v1)
  <details><summary>📄 Abstract</summary>
  Automated experimentation is most effective when the observables, available actions, and objective are defined before the experiment starts, as is the case for Bayesian optimization. However, in many exploratory experiments, the variables that describe the sample must be extracted from the data, new operations emerge during the experiments, and the instrument budget is too small to learn the problem by trials. Here we introduce the Scanning Probe Agentic Research Cycle (SPARC) framework, in whic...
  </details>

- **2026-09-06** — Rana Abu Bakar — [Characterizing Contention-Induced Reliability Collapse in KV-Cache Timing Side Channels for Multi-Tenant LLM Serving](http://arxiv.org/abs/2609.06853v1)
  <details><summary>📄 Abstract</summary>
  Shared key--value (KV) cache reuse improves large language model (LLM) serving, but it can also create a timing side channel that reveals whether a prefix is already cached. Previous work shows that such attacks are possible, but their reliability under realistic multi-tenant contention is less understood. We study this problem through seven experiments on live shared LLM-serving systems. On a vLLM server running DeepSeek-R1-Distill-Llama-8B on NVIDIA GB10, mean Cohen's d drops from 0.7789 with ...
  </details>


### 📂 watermark
*水印与溯源 / Watermarking & Provenance* — 15 papers

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

- **2026-09-07** — Daniel Condurache — [New Symbolic Procedures in the Study of Dynamical Systems](http://arxiv.org/abs/2609.08028v1)
  <details><summary>📄 Abstract</summary>
  The thesis develops symbolic representations of dynamical systems in finite-dimensional commutative real algebras. The algebraic framework (orthogonal idempotents, zero divisors, and the structure of finite-order algebras) supports algebra-valued Fourier and Laplace transforms and Walsh-function-based system identification. The methods yield exact, coordinate-free vectorial solutions for motion in non-inertial reference frames, including a generalized Larmor theorem, the Foucault pendulum, motio...
  </details>

- **2026-09-07** — Hongnan Zhao, Shiyu Chen, Zhihao Chen — [Aegix Pulse: A Traceable Three-Stage Architecture for Personalized Content Generation and Context-Preserving Revision](http://arxiv.org/abs/2609.07672v1)
  <details><summary>📄 Abstract</summary>
  Production content-generation systems must integrate a user's immediate task, long-term brand identity, historical evidence, and revision feedback. We present Aegix Pulse, a production-oriented three-stage architecture that separates current-task clarification and Task Persona finalization, long-term Account Profile (Brand DNA) assembly, and controlled generation and revision while preserving provenance across content versions.   We evaluate four preregistered claims using 96 synthetic social-me...
  </details>

- **2026-09-07** — He Zhao, Ryan Thompson, Daniel M. Steinberg et al. — [From Synthetic Priors to Model Behavior: Structural Coverage in Tabular Foundation Models](http://arxiv.org/abs/2609.06912v1)
  <details><summary>📄 Abstract</summary>
  Tabular foundation models (TFMs) are commonly pretrained on large collections of procedurally generated synthetic tasks, yet it remains unclear how well these synthetic pretraining priors support the downstream tasks on which the models are evaluated. We study this question from a distribution-level attribution perspective. We recover or reconstruct the synthetic data generators of four TFMs and compare their generated tasks with datasets from two widely used tabular benchmarks. Each dataset is ...
  </details>


### 📂 agent-safety
*Agent 安全框架 / Agent Safety Frameworks* — 1 papers

- **2026-09-07** — Yuqi Li, Siyuan Liu, Bingjun Liu — [VST: Verifiable Structured Transport for Auditable Agent-to-Agent Alpha Discovery](http://arxiv.org/abs/2609.07065v1)
  <details><summary>📄 Abstract</summary>
  Agent-to-agent (A2A) alpha discovery is slowed by repeated feedback cycles between mining and evaluation agents, whose hand-offs, in contemporary LLM multi-agent systems, are free-form natural-language messages that carry no stable contract and cannot be replayed. We first restructure this communication as a structured agent-to-agent protocol of \emph{typed, causally addressable, unicast records}, so that the committed stream forms a causal trajectory. On that trajectory a single predictor with ...
  </details>


### 📂 survey
*综述与系统化 / Surveys & Systematization* — 8 papers

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

- **2026-09-07** — Celian Ringwald, Huseyin Erdogan, Valentina Presutti et al. — [X-DigCheck: Co-Evolving Application Profiles and Knowledge Graphs, Demonstrated on the RTI Documentation of Rupe Magna](http://arxiv.org/abs/2609.07694v1)
  <details><summary>📄 Abstract</summary>
  We demonstrate X-DigCheck, a domain-independent environment for building and maintaining application profiles as they co-evolve with the data they describe. Profiles developed against a fixed ontology quickly drift from the schema they were meant to capture. X-DigCheck treats profile construction as a continuous ontology-data co-evolution loop: data are lifted into RDF against the profile, checked through competency questions and SHACL, and the resulting reports jointly drive revisions of the on...
  </details>

- **2026-09-07** — Yi Yang, Xiao Jia, Zeyun Dong et al. — [Mapping the Emerging Social Science of Large Language Models](http://arxiv.org/abs/2609.07598v1)
  <details><summary>📄 Abstract</summary>
  Large language models (LLMs) increasingly shape communication, learning, work, creativity, and decision-making, yet social-science research on these developments remains fragmented. We map this emerging field using a curated corpus of 198 papers reviewed in full and a field-scale corpus of 47,719 published papers from five bibliographic databases. Combining sentence embeddings, K-means clustering, within-cluster Latent Dirichlet Allocation (LDA), author and LLM classifications, and structural to...
  </details>


### 📂 other
*其他安全相关 / Other Security-Related* — 157 papers

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

- **2026-09-07** — Halfdan Nordahl Fundal, Yuri Bizzoni, Charlotte Gjørup Bilde et al. — [Humans Introduce, Models Elaborate: Asymmetric Narrative Agency in Human-LLM Co-Writing](http://arxiv.org/abs/2609.07920v2)
  <details><summary>📄 Abstract</summary>
  Human-LLM co-writing is increasingly used for open-ended text generation, but much prior work focuses on final outputs rather than the interactional dynamics through which stories are produced. We study turn-based collaborative storytelling across three matched conditions: Human-Human (HH), Human-LLM (HA), and LLM-LLM (AA). Using a shared storytelling paradigm, we measure how agents align, introduce novel material, and influence narrative development through turn-level measures of valence adapta...
  </details>

- **2026-09-07** — Shahzeb Qamar, Lorenz Sparrenberg, Christian Bauckhage et al. — [Accuracy is Not Enough: A Divergence-Based Approach to Evaluate Fidelity Loss in Quantized LLMs](http://arxiv.org/abs/2609.07664v2)
  <details><summary>📄 Abstract</summary>
  Deployment of Large Language Models (LLMs) on memory-constrained edge devices relies heavily on aggressive post-training quantization. However, evaluating these models is largely based on zero-shot task accuracy, which depends solely on argmax predictions and is insensitive to changes in the underlying predictive distribution. Consequently, accuracy can exhibit unstable, non-monotonic behavior under progressive quantization, masking substantial fidelity loss relative to the BFloat16 (BF16) uncom...
  </details>

- **2026-09-07** — Ruoqu Chen, Feixiang Ruan, Liu Cao et al. — [Dex-X: Learning Visual-Tactile Dexterous Manipulation From Human Videos with Simulated Interaction](http://arxiv.org/abs/2609.07747v2)
  <details><summary>📄 Abstract</summary>
  Human videos are an abundant source of dexterous manipulation behaviors, but they lack tactile information that is crucial for contact-rich interaction. This raises a fundamental question: can robots learn deployable visual-tactile dexterous manipulation policies from human video demonstrations without robot-side data collection?   We present DEX-X, a framework for learning visual-tactile dexterous manipulation from human videos through simulation. Our key insight is that simulation can serve as...
  </details>

- **2026-09-07** — Sasank Annapureddy, Anjaneya Prasad Thamatani — [PRIMUS: Identity, Governance, and Verification for Multi-Agent Federations](http://arxiv.org/abs/2609.07910v1)
  <details><summary>📄 Abstract</summary>
  Multi-agent federations need governance that answers three questions under adversarial conditions: who participated (identity), did they conform (enforcement), and who decides (authority). A separate question is whether the verification machinery that polices a federation's outputs can also steer a generate-and-test loop toward better answers.   Part I. PRIMA introduced prime-power agent identity and a consensus token whose factorization indexes participation, but assumed honest agents. We prese...
  </details>

- **2026-09-07** — Daria Voronkova, Ilya Trofimov, Anton Dmitriev et al. — [CodeTD: Topology of Attention Detects Hallucinations in Code LLMs](http://arxiv.org/abs/2609.07779v1)
  <details><summary>📄 Abstract</summary>
  As AI-code assistant tools become widespread, automatic assessment of the correctness of generated code becomes a significant challenge. Code LLMs are prone to hallucinations, which may lead to code that does not solve the required problem, or even to code with severe security vulnerabilities. In this paper, we introduce CodeTD -- the first approach to pre-execution assessment of code correctness based on topological data analysis (TDA) of Code LLMs' attention maps. Our method quantifies prompt-...
  </details>

- **2026-09-07** — Zelin Li, Yiyun Su, Matt White et al. — [Your Agent Says Yes: Interpreting Adversarial Market Behavior Beyond Individual Transactions](http://arxiv.org/abs/2609.07675v1)
  <details><summary>📄 Abstract</summary>
  Transaction-local controls answer whether one financial request may proceed, but market behavior can be distributed across messages, agents, assets, and time. We study this interpretation gap in a virtual exchange populated by ten role-conditioned language-model agents. The agents communicate, trade reference assets and futures, launch tokens, and manage concentrated-liquidity pools under prescriptive adversarial roles. We analyze eight 72-cycle trajectories across two time-blinded hourly replay...
  </details>

- **2026-09-07** — Chengshen Gao, Yongzhen Xu, Lvzhou Li — [Quantum Approximate Counting with Bernoulli Oracles](http://arxiv.org/abs/2609.07604v1)
  <details><summary>📄 Abstract</summary>
  Quantum counting is a fundamental quantum algorithm that estimates the fraction of marked elements using a membership oracle, achieving a quadratic speedup over classical sampling. The membership oracle, however, assumes exact labeling of each element, but this assumption fails when the labels are inherently probabilistic. We study quantum counting with \emph{Bernoulli oracles}, where given $m$ Bernoulli distributions with unknown biases $p_1,\dots,p_m$ and a gap parameter $Δ$, the goal is to es...
  </details>

- **2026-09-07** — Zahra Hosseini, Mahan Pouromidi, Farzad Khalvati et al. — [Automated Chest CT Protocol Selection via Large Language Model Derived Text Embeddings from Imaging Request Text](http://arxiv.org/abs/2609.07986v1)
  <details><summary>📄 Abstract</summary>
  Purpose: Accurate CT protocol selection is critical for diagnostic quality and patient safety, yet the current process is manual, time-consuming, and prone to inconsistencies. Prior Machine Learning methods using keywords or bag-of-words lack contextual understanding and perform poorly on rare protocols. We propose a decision support system using large language model (LLM) features to recommend protocols from free-text clinical indications, capturing clinical nuance and phrasing variation for mo...
  </details>

- **2026-09-07** — Halfdan Nordahl Fundal, Yuri Bizzoni, Charlotte Gjørup Bilde et al. — [Humans Introduce, Models Elaborate: Asymmetric Narrative Agency in Human-LLM Co-Writing](http://arxiv.org/abs/2609.07920v1)
  <details><summary>📄 Abstract</summary>
  Human-LLM co-writing is increasingly used for open-ended text generation, but much prior work focuses on final outputs rather than the interactional dynamics through which stories are produced. We study turn-based collaborative storytelling across three matched conditions: Human-Human (HH), Human-LLM (HA), and LLM-LLM (AA). Using a shared storytelling paradigm, we measure how agents align, introduce novel material, and influence narrative development through turn-level measures of valence adapta...
  </details>

- **2026-09-07** — Siyu Song, Qi Bai, Jinbo Hao et al. — [Deadline-Aware Adaptive Prefill Chunking for Efficient Large Language Model Serving](http://arxiv.org/abs/2609.07883v1)
  <details><summary>📄 Abstract</summary>
  Continuous batching improves large language model (LLM) serving throughput, but long prompt prefills can delay decode iterations and violate inter-token latency objectives. Chunked prefill mitigates this interference, yet its chunk size is normally fixed: small chunks protect decode latency but repeatedly pay launch overhead, while large chunks improve prefill efficiency but create latency spikes. We introduce SLOWeave, an online scheduling method that selects the largest prefill chunk predicted...
  </details>

- **2026-09-07** — Shahzeb Qamar, Lorenz Sparrenberg, Christian Bauckhage et al. — [Accuracy is Not Enough: A Divergence-Based Approach to Evaluate Fidelity Loss in Quantized LLMs](http://arxiv.org/abs/2609.07664v1)
  <details><summary>📄 Abstract</summary>
  Deployment of Large Language Models (LLMs) on memory-constrained edge devices relies heavily on aggressive post-training quantization. However, evaluating these models is largely based on zero-shot task accuracy, which depends solely on argmax predictions and is insensitive to changes in the underlying predictive distribution. Consequently, accuracy can exhibit unstable, non-monotonic behavior under progressive quantization, masking substantial fidelity loss relative to the BFloat16 (BF16) uncom...
  </details>

- **2026-09-07** — Yacine El Yamani, Hanna Krasowski, Elena Vanneaux — [Decentralized Safe Multi-Agent Reinforcement Learning via Predictive Shielding](http://arxiv.org/abs/2609.07618v1)
  <details><summary>📄 Abstract</summary>
  Environments are increasingly populated by multiple robots performing independent tasks with limited prior knowledge of each other. Deploying such multi-agent systems presents significant challenges. Specifically, shifts in deployment states compared to training data can lead to poor policy performance and compromised safety. While safety shields exist to mitigate these risks, they are typically reactive, which degrades performance near unseen obstacles,and centralized, limiting their scalabilit...
  </details>

- **2026-09-07** — Zixiao Gu, Yabo Chen, Xunzhi Xiang et al. — [Search-to-World: Evaluation of 3D World Delivery from User Request through Web Search](http://arxiv.org/abs/2609.07605v1)
  <details><summary>📄 Abstract</summary>
  Agentic systems can interpret user requests, search the live web, and use external tools, but their ability to transform retrieved web content into a usable 3D world has not been systematically evaluated. No established end-to-end pipeline or benchmark exists for this capability. We introduce Search-to-World, an end-to-end evaluation task covering request understanding, web visual-content retrieval, and 3D-world delivery. We define Observed Retrieval Rate (ORR) and World Delivery Rate (WDR) to d...
  </details>

- **2026-09-07** — Vinícius Ferraz, Leon Houf, Enrico Ferrea — [The Internal Anatomy of Strategic Choice in Large Language Models](http://arxiv.org/abs/2609.07478v1)
  <details><summary>📄 Abstract</summary>
  Large language models act as strategic agents and models of human choice, yet choosing like a strategic agent does not mean computing like one. We recorded activations from four open-weight models --- dense and mixture-of-experts, including a matched base--instruct pair --- in one-shot play of 144 strict ordinal $2\times2$ games. We followed a prespecified incentive from prompt, through activations, to choice. Dense models mirrored the unadjusted human decline with game complexity. Incentive and...
  </details>

- **2026-09-07** — Xian Gao, Jinpeng Wang, Jiacheng Ruan et al. — [MEMO: Multimodal Evidence Memory Organization for Long-Horizon LLM Agents](http://arxiv.org/abs/2609.07471v1)
  <details><summary>📄 Abstract</summary>
  Long-running LLM agents rely on external memory to store and reuse information beyond a single context window, yet there is a fundamental tension between the continuous accumulation of interaction trajectories and the limited context capacity. The key challenge in agent memory is therefore not only to retrieve relevant records, but also to select necessary evidence under a given budget and organize it in an appropriate modality. Existing memory readout methods mainly use textual or visual forms....
  </details>

- **2026-09-07** — Nicolás Miccio Palermo, Antonela Tommasel, J. Andrés Diaz-Pace — [A Text Mining and Classification Approach for Analyzing Architecture Decision Records](http://arxiv.org/abs/2609.07375v1)
  <details><summary>📄 Abstract</summary>
  Architectural decision records (ADRs) have become a popular lightweight mechanism for documenting architectural knowledge in software projects. However, there is limited empirical evidence on the kinds of architectural concerns captured in ADRs and how well their contents align with established architectural knowledge concepts and documentation practices. In this paper, we propose an automated text-mining and classification approach for analyzing ADRs at scale. We apply this approach to a datase...
  </details>

- **2026-09-07** — Zhouyuan Xu, Chen Yang, Linhao Wang et al. — [BlueprintAgent: Constraint-Triggered Targeted Revisits for Simulation-Ready Generation from Scanned Structural Blueprints](http://arxiv.org/abs/2609.07362v1)
  <details><summary>📄 Abstract</summary>
  Converting in-service reinforced-concrete (RC) building blueprints into simulation-ready models---structured frame representations that support deterministic FEM export and qualified-engineer review---underpins safety assessment and seismic retrofit, but the process remains manual. Direct prompting of a multimodal large language model (MLLM) over a scanned sheet is unreliable: outputs often violate engineering constraints on beam--column support, span count, or 3D continuity. We present Blueprin...
  </details>

- **2026-09-07** — Haozhuang Chi, Jingsong Liang, Ziying Song et al. — [PV-WM: A Heterogeneous Micro-Macro World Model for Articulated Pedestrian-Vehicle Co-Rollout](http://arxiv.org/abs/2609.07328v1)
  <details><summary>📄 Abstract</summary>
  Local pedestrian-vehicle forecasting spans heterogeneous physical scales: pedestrians combine root locomotion with articulated motion, whereas vehicles are rigid bodies described by kinematic state and oriented extent. Existing road-agent forecasters typically omit pedestrian articulation, while pose forecasters leave vehicle futures outside the learned rollout. We introduce PV-WM, a history-only world model over structured post-perception tracks. It recurrently advances pedestrian root motion, ...
  </details>

- **2026-09-07** — Minbo Gao, Yuhang Liu, Genyuan Zhang — [Curvature Sign Rigidity and Sharp Pointwise Pinching Thresholds](http://arxiv.org/abs/2609.07252v1)
  <details><summary>📄 Abstract</summary>
  We study connected Riemannian manifolds on which either the sectional curvature or the Ricci tensor is, at each point, strictly positive, strictly negative, or zero, and ask whether the two signs can coexist under pointwise pinching. A general support-rigidity theorem for positive semidefinite divergence-free symmetric tensors is the common analytic mechanism.   For sectional curvature in dimension $n\ge 3$, any locally uniform positive lower bound for the absolute pointwise pinching ratio rules...
  </details>

- **2026-09-07** — Xin Xu — [The Oversight Gap: What LLM Safety Monitors Miss, and Why It Is Not Capability](http://arxiv.org/abs/2609.07162v1)
  <details><summary>📄 Abstract</summary>
  Several properties safety monitors are asked to certify, among them cross-tenant noninterference, sandbagging and evaluation awareness, are 2-safety hyperproperties, witnessed only by two executions. The standard consequence is a binary impossibility: one trace cannot decide them. We replace the binary with a measurement. A tight bound puts the balanced accuracy of any single-trace monitor at $\tfrac12+\tfrac12\,TV(P_0,P_1)$, turning undecidability into a graded detectability frontier and defini...
  </details>

- **2026-09-07** — Yulin Wei, Xiangchen Wang, Jianhui Pan et al. — [NutriBench-Kitchen: Benchmarking Embodied AI for Nutrition Management](http://arxiv.org/abs/2609.07135v1)
  <details><summary>📄 Abstract</summary>
  An embodied kitchen assistant must do more than recognize food in isolated frames. It must track ingredient states over time and integrate visual observations with recipe and nutritional knowledge to support constraint-aware decision-making. We formalize this capability as \emph{Embodied Nutrition Management}: perceiving nutrition-relevant events, maintaining a persistent food state, and using it for knowledge-grounded planning. Existing benchmarks evaluate static food understanding or embodied ...
  </details>

- **2026-09-07** — Merve Atasever, Keyan Azbijari, Cagan Bakirci et al. — [From LLM-Generated Specifications to Learned Quadruped Locomotion](http://arxiv.org/abs/2609.07111v1)
  <details><summary>📄 Abstract</summary>
  Quadruped robot locomotion policies are often trained using reinforcement learning, which in turn relies heavily on hand-crafted reward functions. Designing reward functions requires substantial manual engineering, and it is often unclear which local rewards will induce the desired global behavior. Shaped rewards from formal specifications in languages like Signal Temporal Logic (STL) can make rewards more interpretable, but writing STL specifications itself still requires domain expertise. We s...
  </details>

- **2026-09-07** — Takeru Hiramatsu, Kyohei Atarashi, Koh Takeuchi et al. — [Disentangling Steering Vectors](http://arxiv.org/abs/2609.07037v1)
  <details><summary>📄 Abstract</summary>
  Activation steering has emerged as a lightweight, inference-time approach to control the behavior of Large Language Models (LLMs). However, traditional steering vectors used to intervene in LLMs' activations, such as those derived from the difference-in-means method, tend to entangle multiple semantic and stylistic concepts into a single composite direction, leading to unpredictable steering effects. Our core objective is to disentangle this composite direction into its constituent concepts. To ...
  </details>

- **2026-09-07** — Fangan Dong, Weiran Shi, Zhiwei Xu et al. — [Tracing Query Expansion Effects through Sparse Autoencoder Features](http://arxiv.org/abs/2609.06968v1)
  <details><summary>📄 Abstract</summary>
  Query expansion (QE) is a critical technique in information retrieval that enriches underspecified queries with additional textual context. However, its effect is often unreliable in modern dense retrieval, especially for strong off-the-shelf retrievers without retraining. Existing studies mainly examine expansion quality, semantic drift, or retrieval outcomes, but rarely explain how QE changes dense retrievers internally. In this work, we trace QE effects through sparse autoencoder (SAE) featur...
  </details>

- **2026-09-07** — Ruoqu Chen, Feixiang Ruan, Liu Cao et al. — [Dex-X: Learning Visual-Tactile Dexterous Manipulation From Human Videos with Simulated Interaction](http://arxiv.org/abs/2609.07747v1)
  <details><summary>📄 Abstract</summary>
  Human videos are an abundant source of dexterous manipulation behaviors, but they lack tactile information that is crucial for contact-rich interaction. This raises a fundamental question: can robots learn deployable visual-tactile dexterous manipulation policies from human video demonstrations without robot-side data collection?   We present DEX-X, a framework for learning visual-tactile dexterous manipulation from human videos through simulation. Our key insight is that simulation can serve as...
  </details>

- **2026-09-07** — Junkai Lu, Jiadong Zhao, Jiacheng Zhang et al. — [SMaRT-Tug: Structured Multi-Agent Reinforcement Learning for Physics-Based Tugboat-Barge Collaborative Manipulation](http://arxiv.org/abs/2609.07445v1)
  <details><summary>📄 Abstract</summary>
  Autonomous tugboating is central for automating maritime operations such as port logistics and vessel maneuvering, where multiple tugboats must cooperatively transport/manipulate a larger vessel. Collaborative pushing in this setting is challenging due to coupled hydrodynamics, low resistance, strong environmental disturbances, underactuated barge dynamics, and contact-rich interactions. Conventional control methods often rely on simplified models and fixed configurations, which limit their adap...
  </details>

- **2026-09-07** — Wanli Liuchen, Fangyuan Wang, Bin Li et al. — [Phase-and-First-Arrival VLM Feedback for Sparse-Reward Reinforcement Learning in Surgical Manipulation](http://arxiv.org/abs/2609.07211v1)
  <details><summary>📄 Abstract</summary>
  Sparse outcome feedback limits what robots can learn from unsuccessful attempts at complex manipulation. Failed multi-stage surgical attempts can contain grasps, lifts, or transfers worth reusing. In sparse-reward reinforcement learning, terminal rewards collapse such attempts to the same outcome, while scalar vision-language model (VLM) ratings reveal neither what progress merits credit nor when it occurred. We introduce phase-and-first-arrival feedback: one VLM query per recorded episode ident...
  </details>

- **2026-09-07** — Ziyue Feng, Hongbo Fang, James A. Evans — [The Illusion of Debiasing: Persona Steering Redistributes Rather Than Reduces Bias in LLMs](http://arxiv.org/abs/2609.07117v1)
  <details><summary>📄 Abstract</summary>
  Prompt-based interventions: system prompts, personas, role instructions, reliably reshape what a language model says, but it is unclear which layer they reach. Do they reconfigure internal structure, or only modulate the output channel? We use persona conditioning as a controlled probe, measuring its effects along a depth axis from self-report, through open-ended generation, to word-level parametric association, across three instruction-tuned models. We find a graded dissociation. Personas are l...
  </details>

- **2026-09-07** — Soohyun Ryu, Sohee Kim, Eunho Yang — [SpatialBlock: Enhancing Spatial Intelligence in LVLMs via Synthetic Block-Stacking Problem](http://arxiv.org/abs/2609.07064v1)
  <details><summary>📄 Abstract</summary>
  Large Vision-Language Models (LVLMs) have achieved strong performance on diverse visual tasks, yet their ability to reconstruct and reason about the 3D structure of the scene depicted in 2D images -- referred to as spatial intelligence -- remains limited. Existing approaches attempt to address this gap by using real-scene spatial question answering datasets that require dense geometric annotations. However, constructing such labels is costly, time-consuming, and often noisy due to reliance on ex...
  </details>

- **2026-09-07** — Vishwas Sathish, Viresh Ranjan, Xinliang Zhu et al. — [Eliciting Self-Verification in Multimodal Reasoning Agents with Reinforcement Learning](http://arxiv.org/abs/2609.08025v1)
  <details><summary>📄 Abstract</summary>
  Reasoning agents increasingly rely on external tools such as web search to answer complex queries. Reinforcement learning (RL) finetuning algorithms such as GRPO have improved long-form reasoning in text-only language models, particularly for coding and mathematics. Reliable tool use in multimodal agents, however, remains challenging because models must interpret text and images while integrating noisy retrieved evidence, often under sparse outcome-level supervision without explicit verification...
  </details>

- **2026-09-07** — Chen Qian — [A Layered Analysis of Disagreement And Answer Quality in Multi-Agent LLM Debate](http://arxiv.org/abs/2609.08016v1)
  <details><summary>📄 Abstract</summary>
  Multi-agent debate, in which several LLMs exchange arguments before answering, is widely assumed to improve answer quality by surfacing genuine disagreement. That mechanism is rarely checked. We introduce four measurements: (A) the agreement a debater reports; (B) whether its reply text actually pushes back; (C) whether the position persists once the eliciting instruction is removed; and (D) for open-weight models, the stance response in the debater's own token log-probabilities. We evaluate thr...
  </details>

- **2026-09-07** — Akshay K. Jagadish, Younes Strittmatter, Nori Jacoby et al. — [Sparks of In Silico Cognitive Science: Theories from Simulated Data Can Generalize to Humans](http://arxiv.org/abs/2609.08003v1)
  <details><summary>📄 Abstract</summary>
  Behavioral foundation models have been proposed as stand-ins for human participants across settings, but it is unclear whether theories discovered on them generalize to humans or merely characterize the simulator. We ran the Automated Cognitive Scientist (\textsc{AutoCog}), a closed-loop discovery system in which LLM agents design theory-discriminating experiments, collect responses, arbitrate between competing theories, and synthesize successors, entirely on behavior simulated by Centaur, a fou...
  </details>

- **2026-09-07** — Kangke Cheng, Guanlin Mo, Shihong Song et al. — [A Sub-4 Approximation for Fair $k$-Means](http://arxiv.org/abs/2609.07974v1)
  <details><summary>📄 Abstract</summary>
  Fairness in clustering has attracted sustained research interest, motivated by the need to ensure equitable representation of protected groups in machine learning applications. We study fair $k$-means clustering in Euclidean space, where the proportion of each protected group in every cluster must lie within specified lower and upper bounds. These constraints make it challenging to determine both cluster centers and point assignments. We propose an approximation algorithm that combines a linear ...
  </details>

- **2026-09-07** — Yonghong Zhang, Ricardo Correia, Isabel M. Parra et al. — [CausalVerify: An Execution-Grounded Benchmark for LLM Causal Inference Workflows](http://arxiv.org/abs/2609.07944v1)
  <details><summary>📄 Abstract</summary>
  Existing causal-inference benchmarks for LLMs mostly score method descriptions or whether generated code runs, not whether the executed workflow recovers the target causal estimate. CausalVerify studies this verification problem for structured econometric causal-estimation workflows by separating realistic interpretation from verifiable computation. It pairs 259 published economics papers (reconstructed research question, data description, institutional context) with 100 fixed-seed synthetic sce...
  </details>

- **2026-09-07** — Ali Şenol, H. Russell Bernard, Huan Liu — [Do Large Language Models Know What They Don't Know II? A Fully Behavioral, Non-Cognitive Measure of Epistemic Honesty](http://arxiv.org/abs/2609.07879v1)
  <details><summary>📄 Abstract</summary>
  Large Language Models (LLMs) are frequently confident, eloquent, and well versed. A natural question arises: do they know what they don't know? To answer this question, we borrow the concept of epistemic honesty and develop a novel metric to systematically evaluate whether an LLM appropriately acknowledges the boundaries of its knowledge. In this work, we introduce the Epistemic Honesty Quotient (EHQ), which reports three observable sub-scores across two operational axes (epistemic restraint and...
  </details>

- **2026-09-07** — Arjun Patrawala, Jiahai Feng, Erik Jones et al. — [LLM Layers Immediately Correct Each Other](http://arxiv.org/abs/2609.07876v1)
  <details><summary>📄 Abstract</summary>
  Recent methods in language model interpretability employ techniques such as sparse autoencoders to decompose residual stream contributions into linear, semantically meaningful features. Such methods are commonly interpreted as identifying features that persist in the residual stream and that subsequent layers build upon. We challenge this view by identifying the Transformer Layer Correction Mechanism (TLCM), wherein adjacent transformer layers systematically counteract portions of each other's c...
  </details>

- **2026-09-07** — Timothy O'Shea, Matthew Pennybacker, Andriy Kharchenko — [The OCUDU dApp Platform: An Open Runtime and E3 Interface for Real-Time AI-RAN](http://arxiv.org/abs/2609.07843v1)
  <details><summary>📄 Abstract</summary>
  Machine learning has shown its largest gains in the band below 10 ms inside a 3GPP new radio (NR) 5G distributed unit (DU): link adaptation, per-slot scheduling, channel estimation, and the receiver itself. No open platform has let independently built software run there. Prior dApp frameworks reached the band only as external observers of an export stream. This paper is a guided introduction to the OCUDU dApp platform, an open runtime and E3 interface under which signed AI-RAN applications execu...
  </details>

- **2026-09-07** — Wei-Jung Huang — [What Does an LLM-Agent Leaderboard Rank Actually Compare?](http://arxiv.org/abs/2609.07785v1)
  <details><summary>📄 Abstract</summary>
  An LLM-agent leaderboard invites a familiar inference: an agent ranked above another is the better agent. Public evaluation logs may not support that conclusion when systems differ in task mixture, label source, release detail, or cost rule. We study what leaderboard scores estimate and when they justify pairwise superiority conclusions. Our estimand-aware pairwise procedure states the comparison target and measurement source, checks common support, and evaluates the supported difference using a...
  </details>

- **2026-09-07** — Jyun-Ying Yen, Cheng-Kuan Lin, Yu-Chee Tseng — [DeepTable: Structural Attention Biases and Tree Path Encoding for Hierarchical Table Understanding](http://arxiv.org/abs/2609.07707v1)
  <details><summary>📄 Abstract</summary>
  Large language models (LLMs) have demonstrated strong performance in table understanding. However, they typically process table content and headers as linearized token sequences. This representation weakens the two-dimensional and hierarchical structural relationships encoded by multi-level row and column headers. Existing parameter-efficient fine-tuning methods incorporate basic row and column information but do not explicitly capture the rich structural dependencies induced by hierarchical tab...
  </details>

- **2026-09-07** — Yuval Koren, Assaf Ben-Kish, Raja Giryes et al. — [On the Recall Scaling Laws in Mamba: A Theoretical and Mechanistic Study via Hashing](http://arxiv.org/abs/2609.07681v1)
  <details><summary>📄 Abstract</summary>
  Associative Recall (AR) is the cognitive ability to learn and retrieve links between items in memory. In NLP, AR is used as a benchmark for evaluating the in-context memory capacity of architectures such as Mamba, and has been found to strongly correlate with language modeling performance. This paper explores AR from the perspective of mechanistic interpretability, aiming to reverse-engineer the exact internal algorithm used by Mamba to perform recall. Our key insight is that Mamba performs reca...
  </details>

- **2026-09-07** — Jingpu Yang, Fengxian Ji, Jinri Guo et al. — [FinCUABuild: Can Agents Build Reliable Benchmarks for Dynamic Financial Computer Use?](http://arxiv.org/abs/2609.07603v1)
  <details><summary>📄 Abstract</summary>
  Financial scenarios are diverse and complex, spanning varying data conditions, tool configurations, and workflows. Yet existing CUA, Computer-Using Agent, evaluation tasks remain largely manually constructed, limiting scalable coverage of real-world financial scenarios. Then, can agents autonomously construct diverse CUA evaluation tasks for financial scenarios? Evaluating this capability poses three key challenges: scenario coverage of construction requests, fair comparison across construction ...
  </details>

- **2026-09-07** — Qiaozhe Zhang, Jun Sun, Yingzhuang Liu — [Beyond the Matrix Sign: Quadratic Spectral Descent](http://arxiv.org/abs/2609.07597v1)
  <details><summary>📄 Abstract</summary>
  Muon can be interpreted as optimizing a linear local objective over a spectral-norm ball. This gives a matrix-sign update that preserves the singular directions of the gradient and assigns the same magnitude to all active singular modes. We ask whether these two properties remain optimal when local curvature is taken into account. To answer this question, we keep Muon's spectral-norm constraint unchanged and replace the linear local model with a quadratic one. We call the resulting method \emph{...
  </details>

- **2026-09-07** — Aydin Javadov, Daniel Schoess, Florian von Wangenheim — [I Don't Miss You, but I Do: Self-Explanation Faithfulness of Modality Missingness in Vision-Language Models](http://arxiv.org/abs/2609.07596v1)
  <details><summary>📄 Abstract</summary>
  Vision-language models are increasingly used in settings where some input modalities may be unavailable, yet we know little about whether they can faithfully explain how such missing information affects their own predictions. We introduce an interventional protocol for evaluating self-explanations of modality dynamics: models state what each modality alone would support, whether restoring a missing modality would change their answer, and whether the available evidence is sufficient; we then exec...
  </details>

- **2026-09-07** — Eryk Kulikowski — [Same Problem, Different Field: Cross-Domain Solution Import via Domain-Stripped Computational Fingerprints](http://arxiv.org/abs/2609.07595v1)
  <details><summary>📄 Abstract</summary>
  The same underlying computational problem is solved across unrelated fields under different names: recursive Bayesian state estimation appears as a "Kalman filter" in control, "Bayesian forecasting" in pharmacokinetics, and "data assimilation" in geoscience. Topical and citation-based scientific embeddings cannot see this shared problem. We distill each paper once into a domain- and method-name-stripped faceted computational fingerprint, a free-text mechanism skeleton plus controlled computation...
  </details>

- **2026-09-07** — Yinan Deng, Jianqiao Song, Yisi Zhang et al. — [PhysReal: Learning Real-World Deformable Object Physics via Hybrid Constitutive Modeling](http://arxiv.org/abs/2609.07532v1)
  <details><summary>📄 Abstract</summary>
  Learning physically plausible dynamics from visual observations is essential for interactive world models and embodied agents. However, modeling real-world deformable objects remains challenging because their dynamics often arise from complex, spatially heterogeneous material responses. To address this challenge, we propose PhysReal, a video-driven framework for learning and simulating the underlying physics of real deformable objects. PhysReal integrates a spatially varying hybrid expert-neural...
  </details>

- **2026-09-07** — Xiang Ge Luo, Jack Kuipers, Niko Beerenwinkel — [Numerical approximations of population size distributions for multi-type branching processes](http://arxiv.org/abs/2609.07526v1)
  <details><summary>📄 Abstract</summary>
  Continuous-time multi-type branching processes are fundamental models for expanding and migrating populations with cancer evolution being a prototypical example. Inferring model parameters, like mutation and growth rates, from time-series count data requires efficient computation of population size distributions. Existing methods are mainly based on large-time or large-number asymptotics, which rely on either restricted initial conditions or simplified interactions between cell types. Here, we i...
  </details>

- **2026-09-07** — Aron Lee — [An LLM-Associated Register Shift in Korean Journal Abstracts: A Morphology-Aware Excess-Vocabulary Study, 2018-2026](http://arxiv.org/abs/2609.07447v1)
  <details><summary>📄 Abstract</summary>
  Excess vocabulary, a word's frequency above its pre-2023 trend, is how the change in scholarly English after 2022 has been measured. We adapt it to Korean with morphological units on 398,296 KCI abstracts (2018-August 2026), with 47,165 Vietnamese abstracts for comparison. Placebo floors are 0.1-2.2 points for the single-word statistic and at most 2.9 for the re-selected split-half set statistic. Korean abstracts show nothing in 2023, onset in late 2024, a rise through 2025 flattening in mid-202...
  </details>

- **2026-09-07** — Yongjin Cui, Xiaohui Fan — [Unraveling the Real Working Mechanism and Inherent Flaws of GAE: A Method for Interpreting Transformer Processes from an Economic Perspective](http://arxiv.org/abs/2609.07213v1)
  <details><summary>📄 Abstract</summary>
  We observe a phenomenon that current algorithmic research in the field of explainable artificial intelligence primarily pursues better performance on several proxy metrics. On the one hand, these proxy metrics themselves are more or less flawed and cannot properly measure the quality of methods. On the other hand, metric-oriented research approaches often lead to the neglect of the rationality and interpretability of the methods themselves. Explainable artificial intelligence is abbreviated as X...
  </details>

- **2026-09-07** — Zheng Nie, Zherui Li, Jiaming Zhang et al. — [In-Place Instruction Following in Diffusion Language Models](http://arxiv.org/abs/2609.07160v1)
  <details><summary>📄 Abstract</summary>
  Diffusion Large Language Models (dLLMs) generate text via bidirectional iterative denoising, naturally supporting user-specified constraints anchored at arbitrary output positions, a paradigm known as In-place Prompting (IPP). We formalize this as the In-place Instruction Following (IIF) task and construct IIF-Bench, a hierarchical benchmark spanning literal, style, and discourse-function constraints, paired with a rubric-based local-global evaluation protocol. An inference-time attention-bias p...
  </details>

- **2026-09-07** — Giuseppe De Gregorio, Alicia Fornés, Lei Kang et al. — [Unsupervised Domain Adaptation for Symbol Spotting in Historical Encrypted Manuscripts](http://arxiv.org/abs/2609.07159v1)
  <details><summary>📄 Abstract</summary>
  The decipherment of historical encrypted manuscripts poses a fundamental challenge in Digital Humanities: before any transcription can begin, the symbol inventory of the underlying cipher alphabet must first be identified and characterized. We address this challenge through symbol spotting: given a candidate alphabet specified as a set of rendered font glyphs, the task is to determine whether and where its characters appear in an unseen handwritten document, without any labeled examples from the...
  </details>

- **2026-09-07** — Yury E. Geints, Victor O. Kompanets, Sergey V. Chekalin — [Controllable ultrabroadband supercontinuum during twocolor femtosecond laser filamentation in high pressure gases](http://arxiv.org/abs/2609.07142v1)
  <details><summary>📄 Abstract</summary>
  Twocolor laser filamentation is considered a promising strategy for deep transformations of the spectrum and generating ultrashort light pulses, which is critically important for developing effective methods to control broadband coherent radiation in attosecond physics and ultrafast spectroscopy. We present the results of our experiments on the study of the spectral dynamics of supercontinuum generated during collinear twocolor filamentation of femtosecond pulses at the fundamental (800 nm) and ...
  </details>

- **2026-09-07** — Mika Okamoto, Gabriele Sarti — [Encoded Early, Used Late: Where Transformers Begin to Act on an Inferred Partner's Expertise](http://arxiv.org/abs/2609.07139v1)
  <details><summary>📄 Abstract</summary>
  A transformer can make an attribute linearly decodable in its residual stream at a depth where that attribute does not yet influence the output. This gap between where information is readable and where it is used has been shown for attributes stated directly in the input. We ask whether it also holds for an attribute the model must infer gradually over a conversation, namely how expert its dialogue partner is. Using ExpertCollab, a corpus of multi-turn research-planning dialogues between model-p...
  </details>

- **2026-09-07** — Mingju Chen, Qianhui Liu, Yui Lo et al. — [Centering Drives Normalization Gains: Price-Offset Nuisances in Cross-Sectional Return Prediction](http://arxiv.org/abs/2609.07122v1)
  <details><summary>📄 Abstract</summary>
  Cross-sectional return prediction from raw intraday bars is sensitive to each instrument price level, an additive nuisance under a return-ranking hypothesis. We test whether removing this offset, rather than rescaling amplitudes or changing the encoder, explains gains on a point-in-time CSI 300 five-minute panel. Eight parameter-matched encoders are evaluated with and without RevIN normalization; a parameter-free ladder then separates identity, scale-only, centering, last-value referencing, diff...
  </details>

- **2026-09-07** — Jinghang Shi, Yanxia Zhang, Ali Luo et al. — [AstroSpecLM: A Spectrum-Language Model for Evidence-Grounded Astronomical Spectral Analysis](http://arxiv.org/abs/2609.07102v1)
  <details><summary>📄 Abstract</summary>
  Astronomical spectra encode rich physical information, but drawing scientific conclusions from spectral features typically requires expert interpretation. This paper presents AstroSpecLM, a spectrum-language model that connects one-dimensional DESI spectra with Qwen3-4B to answer questions and provide explanations grounded in spectral evidence. Instead of generating question-answer pairs directly from templates or raw catalog fields, we first distill each spectrum into a compact set of catalog- ...
  </details>

- **2026-09-07** — Hemanth Saratchandran, Simon Lucey — [Conditioned Initialization for Attention](http://arxiv.org/abs/2609.07086v1)
  <details><summary>📄 Abstract</summary>
  Transformers are a dominant architecture in modern machine learning, powering applications across vision, language, and beyond. At the core of their success lies the attention layer, where the query, key, and value matrices determine how token dependencies are captured. While considerable work has focused on scaling and optimizing Transformers, comparatively little attention has been paid to how the weights of the queries, keys and values are initialized. Common practice relies on random initial...
  </details>

- **2026-09-07** — Srikanth Malla, Chiho Choi, Joon Hee Choi — [Steering Interference Reflects the Model's Defaults, Not the Behavior Directions](http://arxiv.org/abs/2609.06951v1)
  <details><summary>📄 Abstract</summary>
  Activation steering promises modular control of language model behavior: a behavior such as politeness corresponds to a direction in a model's activations, and adding that direction while it generates should switch the behavior on and leave everything else alone. It does not. We ask what decides which other behaviors move, and by how much, and find that it is the model rather than the behavior being steered. A steer relaxes the model toward a small set of behaviors it already favors, chiefly ref...
  </details>

- **2026-09-07** — Jose de Jesus Bernal-Alvarado, David Delepine — [Kuramoto Phase Synchronization in Regional Epidemic Dynamics: Two Test Cases from European COVID-19 and Influenza Surveillance](http://arxiv.org/abs/2609.06899v1)
  <details><summary>📄 Abstract</summary>
  We test whether the Kuramoto model quantitatively describes spatial synchronization in regional epidemic waves, using daily COVID-19 incidence for 400 German \emph{Kreise} (2021--2023) and weekly ILI rates for 12 European countries (ECDC, 2021--2026). Bandpass filtering and Hilbert-transform phase extraction yield high global order parameters ($\langle r\rangle\approx0.87$ for Germany; $\langle r\rangle\approx0.97$ for Europe), yet both are dominated by a common-mode driver rather than pairwise ...
  </details>

- **2026-09-07** — Mimo Shirasaka, Haochen Zhang, Yonatan Bisk — [Contextual Observer Grounding: Evaluating Situated Spatial Reasoning in Vision-Language Models](http://arxiv.org/abs/2609.06880v1)
  <details><summary>📄 Abstract</summary>
  Reasoning over language instructions in embodied tasks such as robotics often requires understanding spatial relations from a speaker's situated perspective. Humans infer such perspectives from shared environmental knowledge, activity context, and commonsense. Recent vision-language models (VLMs) appear capable of spatial reasoning, but their ability to infer a speaker's viewpoint from contextual cues and interpret situated spatial relations from that viewpoint remains unclear. We call this capa...
  </details>

- **2026-09-06** — Sarang Sutavani, Umesh Vaidya — [Spectral Koopman-Hopf Formula for Reachability with Adversary](http://arxiv.org/abs/2609.06878v1)
  <details><summary>📄 Abstract</summary>
  This paper develops a spectral Koopman-Hopf framework for adversarial reachability analysis of nonlinear systems. By lifting the nonlinear drift dynamics into Koopman eigenfunction coordinates, the proposed approach transforms the original state-dependent Hamilton-Jacobi-Isaacs (HJI) equation into an approximate state-independent optimization problem in spectral coordinates. The transformed control and disturbance directions are approximated using least-squares spectral projections, and upper an...
  </details>


## 📊 统计 / Statistics

| 分类 / Category | 论文数 / Count |
|------|--------|
| jailbreak | 624 |
| prompt-injection | 531 |
| memory-poisoning | 49 |
| tool-use-attack | 133 |
| backdoor | 449 |
| adversarial-attack | 588 |
| privacy-leakage | 4048 |
| steganography | 64 |
| misuse | 1000 |
| red-teaming | 123 |
| vulnerability | 3012 |
| defense | 2821 |
| alignment | 2634 |
| robustness | 2732 |
| watermark | 412 |
| unlearning | 94 |
| agent-safety | 54 |
| benchmark | 65 |
| survey | 337 |
| other | 7416 |

---

📚 **全部 27186 篇论文**（2022 至今）请访问 [GitHub Pages](https://ny1024.github.io/AgentSafety-Papers/) 查看完整列表、搜索与筛选。

*Generated by AgentGuard at 2026-09-10 15:42:12*