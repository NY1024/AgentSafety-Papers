<div align="center">

# AgentGuard 🛡️

**Daily Tracking of LLM Agent Security Papers on arXiv**

[![Auto Update](https://github.com/NY1024/AgentSafety-Papers/actions/workflows/daily-update.yml/badge.svg)](https://github.com/NY1024/AgentSafety-Papers/actions/workflows/daily-update.yml)
[![Papers](https://img.shields.io/badge/Papers-29246-blue)](#)
[![License](https://img.shields.io/badge/License-MIT-green)](#)

</div>

---

## 📖 简介 / Introduction

自动追踪 arXiv 上大模型 Agent 安全方向的最新论文，每日更新，关键词智能分类。

*Automatically tracking the latest LLM Agent security papers on arXiv, updated daily with keyword-based classification.*

**最近更新 / Last Updated**: 2026-09-26 15:34 ｜ **论文总数 / Total Papers**: 29246（近 30 天 / Recent 30 days: 3879）

🌐 **[GitHub Pages](https://ny1024.github.io/AgentSafety-Papers/)** — 查看全部 29246 篇论文（含摘要、分类筛选、搜索）/ View all 29246 papers with abstracts, filters & search

## 📑 分类导航 / Category Navigation

- **[jailbreak](#-jailbreak)** — 越狱攻击 / Jailbreak Attacks — 638
- **[prompt-injection](#-prompt-injection)** — 提示注入攻击 / Prompt Injection Attacks — 558
- **[memory-poisoning](#-memory-poisoning)** — 记忆投毒与篡改 / Memory Poisoning & Tampering — 51
- **[tool-use-attack](#-tool-use-attack)** — 工具使用攻击 / Tool-Use Attacks — 140
- **[backdoor](#-backdoor)** — 后门与投毒攻击 / Backdoor & Poisoning Attacks — 473
- **[adversarial-attack](#-adversarial-attack)** — 对抗攻击 / Adversarial Attacks — 602
- **[privacy-leakage](#-privacy-leakage)** — 隐私泄露 / Privacy Leakage — 4165
- **[steganography](#-steganography)** — 隐写与隐蔽通信 / Steganography & Covert Communication — 72
- **[misuse](#-misuse)** — 滥用与误用 / Misuse & Abuse — 1052
- **[red-teaming](#-red-teaming)** — 红队测试 / Red Teaming — 127
- **[vulnerability](#-vulnerability)** — 漏洞与攻击面 / Vulnerabilities & Attack Surfaces — 3227
- **[defense](#-defense)** — 防御与防护方法 / Defense & Protection Methods — 3063
- **[alignment](#-alignment)** — 对齐与安全约束 / Alignment & Safety Constraints — 2830
- **[robustness](#-robustness)** — 鲁棒性与可靠性 / Robustness & Reliability — 3028
- **[watermark](#-watermark)** — 水印与溯源 / Watermarking & Provenance — 478
- **[unlearning](#-unlearning)** — 机器遗忘 / Machine Unlearning — 97
- **[agent-safety](#-agent-safety)** — Agent 安全框架 / Agent Safety Frameworks — 55
- **[benchmark](#-benchmark)** — 安全评测与基准 / Safety Benchmarks & Evaluation — 66
- **[survey](#-survey)** — 综述与系统化 / Surveys & Systematization — 361
- **[other](#-other)** — 其他安全相关 / Other Security-Related — 8163

## 📄 近期论文 / Recent Papers (Last 30 Days)

> 仅展示最近 30 天中最新的 500 篇论文（含日期、作者、摘要）。近 30 天共 3879 篇，完整 29246 篇论文列表请访问 [GitHub Pages](https://ny1024.github.io/AgentSafety-Papers/)

> Showing the latest 500 of 3879 papers from the last 30 days (with date, authors & abstract). For the full list of 29246 papers, visit [GitHub Pages](https://ny1024.github.io/AgentSafety-Papers/)

### 📂 jailbreak
*越狱攻击 / Jailbreak Attacks* — 5 papers

- **2026-09-24** — Lukáš Brůna, Robert Bridges, Adam Ek — [Prefilling the Reasoning Channel: Output-Prefix Attacks on Reasoning LLMs](http://arxiv.org/abs/2609.29775v1)
  <details><summary>📄 Abstract</summary>
  Large Language Models (LLMs) consume and produce a single sequence of text; hence, if text can be added to the beginning of the LLM's response, i.e., an output prefix, then all subsequent tokens will be conditioned on it. This output-prefix attack technique is a cheap black-box prompt injection. Prior work has shown this type of attack can reliably jailbreak non-reasoning models. Most reasoning models add an intermediate scratchpad reasoning step before the assistant's final response. The abilit...
  </details>

- **2026-09-24** — Luciano Maldonado — [PrivDrift: Auditing User-Secret Leakage Under Topic Drift in Active LLM Conversations](http://arxiv.org/abs/2609.30094v1)
  <details><summary>📄 Abstract</summary>
  Large language models increasingly operate as persistent assistants in user-facing, shared-session, and tool-augmented settings. When users disclose sensitive information during an active conversation, that information may remain behaviorally recoverable through later prompts even after the dialogue shifts to unrelated topics. We introduce \textbf{PrivDrift}, a benchmark for auditing whether user-disclosed secrets remain recoverable after conversational topic drift and persuasion-based probing. ...
  </details>

- **2026-09-24** — Ruoqi Guo, Yi Liu, Gelei Deng et al. — [Just Ask Jev: Reinforcement Learning for Calibrated Decisions as a Zero-Shot Detector of AI Alignment Failures](http://arxiv.org/abs/2609.29429v1)
  <details><summary>📄 Abstract</summary>
  Detectors of alignment failures screen deployed language models and score alignment benchmarks. Most are generative judges that spend a decoding pass on every criterion, and classifiers that read token probabilities, such as Llama Guard, still score one fixed label per call. Jev, a model trained with reinforcement learning for calibrated decisions (RLCD), answers many typed questions about one input with calibrated probabilities in a single call. Whether it detects alignment failures has not bee...
  </details>

- **2026-09-24** — Yu-Ling Liao, Tzu-Chin Chiu, Zong-You Chen et al. — [AEGIS: Audio Endogenous Guarding via Internal Signals Against Large Audio-Language Model Jailbreaks](http://arxiv.org/abs/2609.29287v1)
  <details><summary>📄 Abstract</summary>
  Large audio-language models (LALMs) expand language models to process and interpret audio, but also expose them to heterogeneous audio jailbreaks. We ask whether successful jailbreaks reflect failures to recognize harmful intent or failures occurring after such recognition. Layer-wise probing reveals the latter: risk-related information remains decodable from intermediate representations, yet the internal risk signal fails to translate into refusal in later-layer processing. We identify this dis...
  </details>

- **2026-09-23** — Kian Shamsaie, Iman Modarressi — [Psychoacoustically Aligned Latent Smoothing for Adversarial Robustness of Full-Duplex Speech-to-Speech Dialogue Models](http://arxiv.org/abs/2609.27378v1)
  <details><summary>📄 Abstract</summary>
  End-to-end speech-to-speech dialogue models listen and speak simultaneously, so a continuously open acoustic channel is exposed to adversarial manipulation. We formalize imperceptible attacks on full-duplex agents as optimization over additive perturbations confined beneath the psychoacoustic masking threshold of the carrier speech, under three goals: targeted semantic hijacking, response suppression, and policy jailbreaking. Against an undefended Moshi-style agent, white-box attacks succeed in ...
  </details>


### 📂 prompt-injection
*提示注入攻击 / Prompt Injection Attacks* — 8 papers

- **2026-09-24** — Yanming Xiu — [Through Human Eyes and Machine Eyes: Understanding View Mismatch in Video See-Through Extended Reality](http://arxiv.org/abs/2609.29173v1)
  <details><summary>📄 Abstract</summary>
  Video see-through extended reality (VST XR) systems commonly use headset screenshots or captured frames as proxies for the user's first-person visual context. However, the system-captured view and the user's effective visible field do not necessarily coincide: a screenshot records a rectangular machine-readable frame, whereas the user's effective visible region can be more constrained and non-rectangular. This paper studies this human-system view mismatch in VST XR. We formalize the relationship...
  </details>

- **2026-09-24** — Daiki Chiba, Hiroki Nakano, Takashi Koide — [ClaimMirage: When Self-Claims in Domain Names Change LLM Threat Judgments](http://arxiv.org/abs/2609.29130v1)
  <details><summary>📄 Abstract</summary>
  Short claims such as not-phishing or official can change how a large language model (LLM) judges a domain name, without explicit prompt-injection commands. We study this manipulation as ClaimMirage: a name under inspection claims its own safety or approval. We analyze 622,080 judgments across 64 brands and five LLMs, comparing ten claims with length- and hyphen-matched controls in constructed brand-like names. Self-claims can substantially reduce or increase alerts, depending on the LLM and inpu...
  </details>

- **2026-09-24** — Qingyu Wu, Zeyu Feng, Yongda Yu et al. — [ENDOPROMPT: Victim-Side Pseudo-References for Utility Degradation](http://arxiv.org/abs/2609.29948v1)
  <details><summary>📄 Abstract</summary>
  Prompt injection can degrade benign task performance without eliciting harmful content. Yet many attack objectives depend on task labels or predefined target responses. We present ENDOPROMPT, a white-box method that learns utility-degrading prefixes from unlabeled instructions. Its generator takes the request text as input. Clean victim continuations serve as pseudo-references: local search identifies prefixes that reduce continuation likelihood, and preference fitting on comparisons within the ...
  </details>

- **2026-09-24** — Karina Elzer, Niklas Netterstrøm Johansen, Emmanouil Vasilomanolakis — [OllamaDrama: Designing and Deploying a Honeypot to Measure Attacks on Exposed LLM Infrastructure](http://arxiv.org/abs/2609.29757v1)
  <details><summary>📄 Abstract</summary>
  Publicly exposed large language model (LLM) infrastructure creates a growing attack surface, yet real-world targeting remains poorly understood. We present Ollure, a low- and medium-interaction honeypot that emulates the Ollama API without a backend LLM. Spanning four deployments across cloud and university networks, Ollure operated for 84 days and recorded 290,887 interactions from 2,793 unique source IP addresses. Most of the activity consisted of automated discovery, fingerprinting, and model...
  </details>

- **2026-09-24** — David Schmotz, Derck Prinzhorn, Luca Beurer-Kellner et al. — [Instrumental Monitor Evasion Emerges Under Ordinary Task Pressure](http://arxiv.org/abs/2609.30217v1)
  <details><summary>📄 Abstract</summary>
  A central concern in AI safety is that agents may treat oversight as an obstacle when it conflicts with completing their goals. We study instrumental evasion, the propensity of LLM agents to circumvent runtime monitoring as a means of completing ordinary tasks. We introduce EvasionBench, a benchmark of 50 diverse task-policy pairs in which completing the task requires an operation prohibited by a runtime monitor. Agents know that their tool calls are monitored and are prompted to continue workin...
  </details>

- **2026-09-23** — Tiantong Wu, Wei Yang Bryan Lim — [Decision Hijacking: Prompt Injection Attacks on Jev's Typed Probabilistic Decisions](http://arxiv.org/abs/2609.28613v1)
  <details><summary>📄 Abstract</summary>
  Most studies of prompt injection focus on generative agents, leaving their effects on models with schema-defined outputs unclear. We examine these effects in Jev, a non-generative decision model, using 510 reconstructed InjecAgent cases. Malicious content shifts action probabilities but rarely causes Jev to select the attacker's target. Override markers reduce this influence, while claims of contextual relatedness have small effects. Adaptive attacks using score feedback double the mean highest ...
  </details>

- **2026-09-23** — Jasem Khelifi, Issam Oukhay, Ali Ouni et al. — [Specifying and Maintaining Agentic Workflows: An Empirical Study of GitHub Agentic Workflows](http://arxiv.org/abs/2609.27263v1)
  <details><summary>📄 Abstract</summary>
  Agentic workflows shift software development from prompting AI agents for individual tasks to defining recurring work that agents execute automatically. GitHub Agentic Workflows (gh-aw) enables this approach through Markdown files that combine natural-language instructions with configuration and compile into executable GitHub Actions workflows. Unlike conventional workflows that primarily prescribe scripted operations, these files delegate tasks requiring interpretation to AI agents. They also c...
  </details>

- **2026-09-22** — Reshabh K Sharma, Linxi Jiang, Shuo Chen et al. — [Ajar: Measuring Open Privilege in Agent Defenses](http://arxiv.org/abs/2609.26900v1)
  <details><summary>📄 Abstract</summary>
  A language model agent acts through the tools it is given. The data it reads while working on a task can redirect what it does with those tools. A growing set of techniques for safe and secure agent execution therefore sits between the agent and its tools, aiming to enforce access control, information flow or isolation at that boundary. Today these techniques are evaluated on agent-security benchmarks built around indirect prompt injection. Those benchmarks judge a defense by how far it brings t...
  </details>


### 📂 memory-poisoning
*记忆投毒与篡改 / Memory Poisoning & Tampering* — 1 papers

- **2026-09-23** — Mattea Sim, Yael Eiger, Tadayoshi Kohno — [AI-Enabled Human Memory Manipulation: Misleading AI-Generated Summaries Distort Human Memory](http://arxiv.org/abs/2609.28820v1)
  <details><summary>📄 Abstract</summary>
  AI-generated summaries are increasingly used in high-stakes settings, like policing, despite considerable evidence that AI often generates misleading or inaccurate information. This research asked: do errors in AI-generated summaries distort human memory? To answer this question, we adopted two methodological approaches. First, we conducted an analysis of AI summary output, prompting large language models to generate summaries of videos. This analysis quantified how often AI summaries contain er...
  </details>


### 📂 tool-use-attack
*工具使用攻击 / Tool-Use Attacks* — 4 papers

- **2026-09-24** — Cuifeng Gao, Juantao Zhong, Jiachi Chen et al. — [Demystifying Agent Skills for Smart Contract Auditing: Design, Effectiveness, Behavioral Impact](http://arxiv.org/abs/2609.29454v1)
  <details><summary>📄 Abstract</summary>
  LLM agents, notably Claude Code and OpenAI Codex, are emerging as versatile tools beyond coding agents only. These agents can be enhanced with skills---reusable artifacts that package domain knowledge, workflows, and tool-use instructions. To date, however, little is known about how such skills are designed or how they affect agent effectiveness and behavior in practice. In this paper, we investigate these questions in smart contract security auditing, a domain in which agents have shown substan...
  </details>

- **2026-09-24** — Minghao LI — [HEXIS: Compiling Skills into Extended Finite State Machines](http://arxiv.org/abs/2609.30123v1)
  <details><summary>📄 Abstract</summary>
  Agent skills provide reusable knowledge and instructions, yet agents must repeatedly infer how to apply them and which operation should follow. This couples task reasoning with control decisions, allowing prescribed steps to be omitted or applied incorrectly. We introduce HEXIS, which compiles agent skills into extended finite state machines that separate knowledge from control flow. Skill knowledge is incorporated into local instructions that guide reasoning and generation within states. The ma...
  </details>

- **2026-09-22** — Shuang Guo — [SkillApt: Learning When to Activate Agent Skills from Counterfactual Evidence](http://arxiv.org/abs/2609.26863v1)
  <details><summary>📄 Abstract</summary>
  Large language model agents increasingly retrieve reusable Skills and inject them into the active context. However, a retrieved Skill can be relevant yet unnecessary, costly, or even harmful in the current execution state. We present SkillApt, a post-retrieval activation framework that decides whether a retrieved Skill should actually be loaded. SkillApt builds execution evidence from matched WITH/WITHOUT runs and uses outcomes from similar historical states to make a LOAD/ABSTAIN decision for e...
  </details>

- **2026-09-22** — Laizhen Li, Xuan Wang, Peicheng Zhao et al. — [A2M: Trace-Optimized Agent Hijacking in the MCP Ecosystem](http://arxiv.org/abs/2609.26761v1)
  <details><summary>📄 Abstract</summary>
  Agents using the Model Context Protocol (MCP) rely on semantic matching to select tools from third-party servers, exposing a semantic supply-chain risk through attacker-controlled metadata and outputs. We introduce A2M (Attraction-to-Manipulation), a two-stage black-box framework for hijacking MCP agents. The Attraction phase optimizes tool metadata to increase invocation probability; the Manipulation phase uses execution traces to refine adversarial tool returns that steer agents toward attacke...
  </details>


### 📂 backdoor
*后门与投毒攻击 / Backdoor & Poisoning Attacks* — 4 papers

- **2026-09-23** — Jinwen Xin, Dongni Zhang, Chenyang Wang et al. — [RAMP: Reversing Adversarial Perturbations to Strengthen Clean-Label Backdoor Attacks against Malware Detectors](http://arxiv.org/abs/2609.27422v1)
  <details><summary>📄 Abstract</summary>
  Deep learning-based malware detectors are commonly updated by fine-tuning on newly collected samples, but this practical update pipeline also creates an attack surface for training-time backdoor attacks. In realistic crowdsourced data collection, however, strict label vetting typically restricts attackers to the clean-label setting, in which poisoned samples must retain benign labels and functionality, making effective backdoor injection substantially harder. We present a new attack perspective ...
  </details>

- **2026-09-22** — Yue Xing, Pengfei He, Zitao Li — [The Like Trap: Multi-Stage Poisoning against Agents in Similarity-based Recommendation Systems](http://arxiv.org/abs/2609.27155v1)
  <details><summary>📄 Abstract</summary>
  With recent advancements in large language models (LLMs) and LLM-based agents, these agents are becoming increasingly autonomous and gaining broader access to act on users' behalf on the internet. However, the vulnerability of automated agents deployed on social media platforms (e.g., for managing a user's personal account) remains underexplored. Existing studies on agent poisoning typically assume that the adversary can expose poisoned content to the agent. Although such an attack is direct and...
  </details>

- **2026-09-22** — Tianhao Chen, Yuhan Wei, Weifei Jin et al. — [Divide and Doubt: Diverse Distributed Poisoning for Retrieval-Augmented Generation](http://arxiv.org/abs/2609.27090v1)
  <details><summary>📄 Abstract</summary>
  Multi-passage corpus poisoning often repeats one target claim across similar documents, creating correlated lexical and semantic patterns that similarity- and conflict-aware defenses can suppress jointly. We introduce DnD (Divide and Doubt), a targeted attack based on two principles: distributing support for the target answer across stylistically diverse passages, and including a passage that casts doubt on evidence for the reference answer. The first disperses poison-passage representations in ...
  </details>

- **2026-09-22** — Zijian Zhang, Zhen Zeng, Zhongshu Gu et al. — [Backdoors in Learning-Based Industrial Robotic Arm Manipulation: An Empirical Security Study](http://arxiv.org/abs/2609.26868v1)
  <details><summary>📄 Abstract</summary>
  Learning-based models (e.g., visuomotor and Vision-Language-Action (VLA)) are increasingly explored for industrial robotic manipulation, where model predictions are directly translated into physical actions. This tight coupling between model behavior and physical execution makes hidden security vulnerabilities particularly consequential. While backdoor attacks have been widely studied in conventional AI models, their effects on deployed learning-based robotic arm manipulation systems remain less...
  </details>


### 📂 adversarial-attack
*对抗攻击 / Adversarial Attacks* — 4 papers

- **2026-09-23** — Yihong Zhou, Hanbin Yang, Thomas Morstyn — [Finite-Sample Probabilistic Safety Certification for AI-Based Grid-Edge Coordination](http://arxiv.org/abs/2609.28182v1)
  <details><summary>📄 Abstract</summary>
  Coordinating large population of flexible grid-edge devices can alleviate the need for time-consuming and capital-intensive network upgrades, and AI-based control methods such as multi-agent reinforcement learning or imitation learning are promising in their real-time decision scalability. However, system operators still need an independent and rigorous way to decide whether a given AI system is safe enough for deployment. This paper develops a finite-sample probabilistic safety certification fr...
  </details>

- **2026-09-23** — Jiaxi Wu, Tiantian Zhang, Yuxing Wang et al. — [Robust Adversarial Reinforcement Learning with Risk Sensitivity and Critic Consistency Regularization](http://arxiv.org/abs/2609.27667v1)
  <details><summary>📄 Abstract</summary>
  Reinforcement learning (RL) achieves strong performance in sequential decision-making but remains brittle under dynamic uncertainty and distributional shifts. Robust Adversarial Reinforcement Learning (RARL) improves robustness via worst-case perturbations, but existing approaches frequently suffer from unstable optimization and degraded value estimation. In particular, overly aggressive adversaries can drive the agent toward uninformative failure states, while adversarial perturbations amplify ...
  </details>

- **2026-09-22** — Felix Rosberg, Cristofer Englund, Eren Erdal Aksoy et al. — [Adversarial Attacks and Identity Leakage in De-Identification Systems: An Empirical Study](http://arxiv.org/abs/2609.27022v1)
  <details><summary>📄 Abstract</summary>
  In this paper, we investigate the impact of adversarial attacks on identity encoders within a realistic de-identification framework. Our experiments show that the transferability of attacks transfers from an external surrogate model to the system model (e.g., CosFace to ArcFace) allows the adversary to cause identity information to leak in a sufficiently sensitive face recognition system. We present experimental evidence and propose strategies to mitigate this vulnerability. Specifically, we sho...
  </details>

- **2026-09-22** — Christopher Burger, Christina Trotter, Joseph Carlisle et al. — [Evaluating the Semantic-to-Geometric Gap in Adversarial Defenses Against Vision-Language Model-Based Plagiarism](http://arxiv.org/abs/2609.26733v1)
  <details><summary>📄 Abstract</summary>
  The rapidly advancing capabilities of vision-language models (VLMs) present a systemic challenge to academic integrity. VLMs now allow students to bypass meaningful engagement by capturing and submitting graphical problems as singular images, a practice we define as trivial plagiarism. To provide educators with actionable data on VLM limitations, we investigate the efficacy of heuristic adversarial image transformations designed to degrade model performance while remaining human-interpretable. T...
  </details>


### 📂 privacy-leakage
*隐私泄露 / Privacy Leakage* — 29 papers

- **2026-09-24** — Sudip Bhujel, Shanghao Shi, Ruiquan Huang et al. — [Temporal Gradient Inversion for Private Trajectory Reconstruction in Embodied Reinforcement Learning](http://arxiv.org/abs/2609.30258v1)
  <details><summary>📄 Abstract</summary>
  Distributed learning in embodied reinforcement-learning agents offers a degree of privacy by retaining raw sensor data on-device and transmitting only policy gradients to the server. Yet temporal structure can amplify this leakage beyond single-frame attacks. We introduce Temporal Reconstruction Attack on Consecutive Encodings (TRACE), an amortized temporal gradient-inversion attack that autoregressively reconstructs the sequence of private observation-action trajectories from per-step policy-le...
  </details>

- **2026-09-24** — Jordan L. Cahoon, Chloe O. Stanwyck, Sulaiman Somani et al. — [A Living Benchmark for Information Retrieval from Electronic Health Records](http://arxiv.org/abs/2609.30205v1)
  <details><summary>📄 Abstract</summary>
  Large language model (LLM)-based clinical assistants are increasingly being integrated into electronic health record (EHR) systems, transforming how clinicians retrieve and synthesize information from patient records. Their safety and utility depend on rigorous evaluation, yet existing benchmarks are manually curated, costly to update, and rapidly become obsolete with evolving technological advancements. We present a scalable framework that automatically generates question--answer pairs from lon...
  </details>

- **2026-09-24** — Christine Park, Valerie Chen, Tim Dettmers — [Synthetic Hospital: An Open, Verifiable, Physician-Validated Longitudinal EHR Benchmark](http://arxiv.org/abs/2609.30027v1)
  <details><summary>📄 Abstract</summary>
  Frontier language models are rarely used in clinical workflows because the realistic, longitudinal benchmarks needed to develop them are scarce. Real electronic health record (EHR) data cannot be openly shared due to privacy, ethics or data use issues and it does not contain verifiable ground truth since the chart records only reflect what clinicians documented. We introduce Synthetic Hospital, an open, fully synthetic, fact-grounded longitudinal EHR benchmark that resolves the open sharing and ...
  </details>

- **2026-09-24** — Haojin Li, Anbang Zhang, Wai Ho Mow et al. — [Structured Pose-Conditioned Flow Matching for Generative 5G CSI Augmentation](http://arxiv.org/abs/2609.29912v1)
  <details><summary>📄 Abstract</summary>
  With the growing demand for privacy-preserving and occlusion-resilient human pose recognition (HPR), 5G channel state information (CSI) offers a promising contactless sensing modality by integrating communication and sensing capabilities. However, collecting large-scale synchronized CSI-pose pairs remains costly in practical 5G systems. To address this limitation, we propose StructFlow-HPR, a structured pose-conditioned flow matching framework for generative CSI augmentation. StructFlow-HPR lear...
  </details>

- **2026-09-24** — Chunlei Shi, Yufeng Zhu, Yixiao Liang et al. — [WeatherDiagFlow: Evidence-Grounded Radar Nowcasting with Diagnostic Flow Refinement](http://arxiv.org/abs/2609.29772v1)
  <details><summary>📄 Abstract</summary>
  Radar nowcasting is essential for short-term warning and emergency response, yet conventional systems mainly return future radar fields and provide limited support for operational communication and post-event verification. We formulate radar nowcasting as an evidence-grounded forecast--bulletin--audit task, in which a numerical forecaster produces both future radar fields and structured diagnostic evidence. Forecast-time bulletins use only model-available evidence, whereas post-event audits inco...
  </details>

- **2026-09-24** — Carolyn Cole, Matthias Deschryvere, Toqeer Ehsan et al. — [From Policy Documents to Structured Survey Responses: Evaluating Large Language Models for Policy Monitoring](http://arxiv.org/abs/2609.29370v1)
  <details><summary>📄 Abstract</summary>
  Science, technology, and innovation policies are crucial for competitiveness, yet their diversity and scale make them difficult to map and monitor consistently. Existing approaches rely heavily on manual survey efforts, which are costly and challenging to scale across countries. Large language models (LLMs) enable new possibilities for extracting and structuring information from long and unstructured policy documents. This paper presents an application of LLMs as "AI respondents" for generating ...
  </details>

- **2026-09-24** — Muhammad Muhtasim Shahriar, Abdullah Mohammad Sayem, Tze Hui Liew et al. — [SkinAgent AI: A Safety-Grounded Multimodal Agentic Framework for Non-Diagnostic Skincare Support](http://arxiv.org/abs/2609.29341v1)
  <details><summary>📄 Abstract</summary>
  Consumer-facing skincare AI must coordinate visual evidence, product information, tool use, and user-facing actions within explicit evidence and safety boundaries. This study evaluates SkinAgent AI, a non-diagnostic multimodal framework that combines visual concern routing with grounded and auditable LLM-based orchestration. The architecture includes routing for Acne, Pores, and Wrinkles; photograph-based skin-type estimation; count-informed ordinal acne-severity support; typed tools; database-g...
  </details>

- **2026-09-24** — Jiaran Cai, Xingpei Ma, Shenneng Huang — [ComplexSync: High-Fidelity and Real-Time Lip Sync in Complex Scenarios](http://arxiv.org/abs/2609.29225v1)
  <details><summary>📄 Abstract</summary>
  Lip synchronization aims to generate visual lip dynamics that align precisely with speech audio. Despite the high generation quality of diffusion models, they often struggle in complex scenarios and suffer from prohibitive inference latency, limiting real-world deployment. We present ComplexSync, a unified diffusion-based framework that enables real-time, high-fidelity lip sync under complex conditions. First, we introduce a dual-stream joint training strategy to mitigate information leakage fro...
  </details>

- **2026-09-24** — Sudha Priyadarshini, Mohamed Chahine Ghanem — [ASIRF: An Agentic Framework for Context-Dependent Sensitive Information Redaction](http://arxiv.org/abs/2609.29191v1)
  <details><summary>📄 Abstract</summary>
  Sensitive information is defined by domain and intent, not a universal category, yet redaction systems such as privacy filters and named-entity recognizers fix a taxonomy at training time, requiring retraining for each new domain. We introduce ASIRF (Agentic Sensitive Information Redaction Framework), which retrieves domain-specific definitions based on the input's domain from a flexible knowledge base at inference time, needing no retraining to adapt. Two architectures, a three-call multi-agent...
  </details>

- **2026-09-23** — Harsh Verma — [Blockchain-Enabled Artificial Intelligence and AI Agents for Secure Data Sharing and Cybersecurity Applications](http://arxiv.org/abs/2609.28843v1)
  <details><summary>📄 Abstract</summary>
  Blockchain and artificial intelligence (AI) are converging into a single infrastructural layer for securing data sharing, model integrity, and autonomous decision-making across distributed systems. This paper presents a meta-synthesis that draws together four constituent studies covering adversarial machine learning, AI-powered anomaly detection in cloud environments, automated vulnerability patching by multi-agent large language model (LLM) pipelines, and the broader landscape of securing AI sy...
  </details>

- **2026-09-23** — Mingyuan Li, Yanna Jiang, Guangsheng Yu et al. — [Your Model Is Leaking: Covert Information Transfer through LLM Residual Streams](http://arxiv.org/abs/2609.27996v1)
  <details><summary>📄 Abstract</summary>
  Privacy-sensitive organizations may run large language models (LLMs) in restricted or air-gapped environments while exporting selected diagnostic artifacts. We show that a compromised runtime component can hide sensitive information in intermediate activations that are allowed to leave the restricted environment. An offline observer can recover this information with a simple linear decoder. The attack requires no model retraining or weight modification, no attacker-controlled egress, and no cont...
  </details>

- **2026-09-23** — Zhonghao Sun, Zhiliang Tian, Xinyue Fang et al. — [Only Pay What You Must Spend: On-Demand Privacy Budget Payment for Differentially Private RAG](http://arxiv.org/abs/2609.27406v1)
  <details><summary>📄 Abstract</summary>
  Deploying large language models (LLMs) on sensitive data via Retrieval-Augmented Generation (RAG) introduces severe privacy risks. Recent studies apply Differential Privacy (DP) to LLMs with RAG for formal privacy guarantees. However, existing DP-RAG frameworks rapidly exhaust the privacy budget. Although recent efforts attempt to save the budget by narrowing the retrieval scope or sparsifying private generation, these methods themselves cumulatively consume the budget, whereas they could actual...
  </details>

- **2026-09-23** — Julian Oelhaf, Georg Kordowich, Christian Bergler et al. — [EvEMTBench: An Open Benchmark for Machine Learning in Power System Protection](http://arxiv.org/abs/2609.28149v1)
  <details><summary>📄 Abstract</summary>
  Studies of machine-learning-based power system protection are difficult to compare because task definitions, measurement access, data partitions, metrics, and generalization conditions often differ. EvEMTBench addresses this gap with an open, executable, and versioned benchmark that fixes these evaluation choices while leaving model design open. Across four grids spanning 20-345 kV, it defines 12 protection and event-analysis functions instantiated as 24 scored tasks and supports structured eval...
  </details>

- **2026-09-23** — Zhen Yu, Yang Liu, Xiahai Zhuang et al. — [A generalizable structural brain MRI foundation model built through dual-priority federated pretraining](http://arxiv.org/abs/2609.27611v1)
  <details><summary>📄 Abstract</summary>
  Foundation models hold promise for generalizable analysis of structural brain magnetic resonance imaging (MRI) across development, aging and disease. However, existing models are typically built through centralized pretraining on pooled data, despite privacy and governance constraints. Such pooling optimization can overemphasize cohort size and overlook complementary information from smaller, specialized cohorts. Here we present BrainFedFM, a structural brain MRI foundation model federatively pr...
  </details>

- **2026-09-23** — Sai Karthik Kosuri, Ankita Shashikant Bhosale, Michael Glick et al. — [EviStreams: Human-in-the-Loop AI Data Extraction for Systematic Reviews in Medicine](http://arxiv.org/abs/2609.27418v1)
  <details><summary>📄 Abstract</summary>
  Systematic reviews underpin clinical guidelines, yet their data-extraction step is a major expert-labor bottleneck bound by a protocolized workflow: two reviewers extract each study independently, an adjudicator resolves disagreements, and the team keeps an auditable record of how every value was produced. Large language models can assist with extraction, but that assistance must fit established review protocols and preserve reproducibility. We present EviStreams, a live, open-source, no-code we...
  </details>

- **2026-09-22** — Sarah Radway, Zoe Robert, Matthew Soto et al. — [Privacy Leakage Through AI-mediated Analysis of Smartphone Data](http://arxiv.org/abs/2609.28537v1)
  <details><summary>📄 Abstract</summary>
  Over the past thirty years, the online advertising industry built a large-scale data collection ecosystem, with the goal of tracking a user's online activity to infer their demographics and interests. Traditionally, the ecosystem relied upon the collation and analysis of highly-structured text data like user IP addresses, GPS coordinates, e-commerce purchase histories, and visited URLs. However, recent ML models can parse not only structured text, but also multimedia files and unstructured text ...
  </details>

- **2026-09-22** — Kyaw Hpone Myint, Nan Jiang, Xiang Li et al. — [QUARTET: Quad-branch cross-Attention and Random-walk Traces for Enhancing Transformers on Relational Graphs](http://arxiv.org/abs/2609.26855v2)
  <details><summary>📄 Abstract</summary>
  Relational Deep Learning (RDL) models multi-table databases as heterogeneous temporal graphs, and graph transformers currently achieve state-of-the-art performance on benchmarks like RelBench. However, the current leading model, RelGT, suffers from two key limitations: its random local sampler yields loosely connected subgraphs that hinder message passing, and its global attention module relies on a single, seed-feature-based memory that ignores broader macro-level dynamics. To overcome these li...
  </details>

- **2026-09-22** — Daniel Adu Worae, Spyridon Mastorakis, Nuno Moniz et al. — [Adaptive Traffic Camouflage: Causal and Resource-Aware Defense Against IoT Fingerprinting](http://arxiv.org/abs/2609.25787v2)
  <details><summary>📄 Abstract</summary>
  Encryption hides IoT payloads, but traffic shape can still reveal device identity through packet sizes, timing, direction, and packetization. We present Adaptive Traffic Camouflage, a causal, leakage-aware controller that characterizes traffic-shape leakage without runtime device labels and selects a budget-feasible transformation for the next traffic window from previous-window context. The controller chooses among padding, packet splitting, timing, and composite transformations, or leaves traf...
  </details>

- **2026-09-22** — Yuki Ueno, Aditeya Pandey — [ChartRevive: Reconstructing Data Visualizations from Chart Images Using MLLM](http://arxiv.org/abs/2609.27146v1)
  <details><summary>📄 Abstract</summary>
  Static chart images are widely used in scientific publications, business reports, and presentations, yet recovering both the underlying data and visual design from chart images remains a labor-intensive manual process, making them difficult to reuse. While prior work has primarily focused on data extraction, the extraction of visual design specifications, including colors, marker shapes, and axis configurations, remains underexplored. To identify a suitable model for chart reconstruction, we sys...
  </details>

- **2026-09-22** — Kyaw Hpone Myint, Nan Jiang, Xiang Li et al. — [QUARTET: Quad-branch cross-Attention and Random-walk Traces for Enhancing Transformers on Relational Graphs](http://arxiv.org/abs/2609.26855v1)
  <details><summary>📄 Abstract</summary>
  Relational Deep Learning (RDL) models multi-table databases as heterogeneous temporal graphs, and graph transformers currently achieve state-of-the-art performance on benchmarks like RelBench. However, the current leading model, RelGT, suffers from two key limitations: its random local sampler yields loosely connected subgraphs that hinder message passing, and its global attention module relies on a single, seed-feature-based memory that ignores broader macro-level dynamics. To overcome these li...
  </details>

- **2026-09-22** — Mauro Conti, Lorenzo Perinello, Umberto Salviati — [On the security and privacy of LLMs in Mobility](http://arxiv.org/abs/2609.26295v1)
  <details><summary>📄 Abstract</summary>
  The mobility sector is undergoing a paradigm shift driven by advances in Generative Artificial Intelligence. With a global market valued at approximately 2.9 trillion dollars annually, considering only cars, the integration of these technologies has the potential to impact more than 1.5 billion vehicles worldwide. As Large Language Models (LLMs) are increasingly adopted in mobility, concerns about cybersecurity, privacy, and reliability emerge. Accordingly, this paper surveys current application...
  </details>

- **2026-09-22** — Yan Zhang, Ruien Li, Yaoyao Peng et al. — [EADC: Evaluation of Advanced and Deep-level Compliance in Large Language Models](http://arxiv.org/abs/2609.26175v1)
  <details><summary>📄 Abstract</summary>
  Large Language Models (LLMs) have been used in various industries. However, ensuring their compliance with complex laws and regulatory frameworks remains a great challenge. Existing evaluation paradigms mainly rely on static benchmarks that suffer from three severe limitations: First, the compliance rules being used do not comply with the requirements of Artificial Intelligence (AI) laws and regulations; Second, they only handle apparent, explicit compliance risks, leaving implicit and covert co...
  </details>

- **2026-09-22** — Daniel Adu Worae, Spyridon Mastorakis, Nuno Moniz et al. — [Adaptive Traffic Camouflage: Causal and Resource-Aware Defense Against IoT Fingerprinting](http://arxiv.org/abs/2609.25787v1)
  <details><summary>📄 Abstract</summary>
  Encryption hides IoT payloads, but traffic shape can still reveal device identity through packet sizes, timing, direction, and packetization. We present Adaptive Traffic Camouflage, a causal, leakage-aware controller that characterizes traffic-shape leakage without runtime device labels and selects a budget-feasible transformation for the next traffic window from previous-window context. The controller chooses among padding, packet splitting, timing, and composite transformations, or leaves traf...
  </details>

- **2026-09-22** — Kyle MacMillan, Sanjay Krishnan — [Proof-of-Retention: A Framework for Auditable Cross-Organization Data Sharing](http://arxiv.org/abs/2609.26654v1)
  <details><summary>📄 Abstract</summary>
  The rapid adoption of AI across industries for (e.g.) fine-tuning and analytics has accelerated the need for high-quality data. To satisfy this demand, public and private entities will buy and sell data with other organizations. But such data sharing can and does violate privacy norms and laws. EU and American lawmakers have endeavored to control data sharing, restricting what data may be shared with whom, and under what circumstances. Unfortunately, accurately assessing compliance with new regu...
  </details>

- **2026-09-22** — Ziang Liu, Ruizhang Yang, Xin Cui et al. — [Privacy-Preserving Coordinated Operation of Power Grids and AI Data Centers: A Checkpoint-Aware Three-Phase Scheme](http://arxiv.org/abs/2609.26365v1)
  <details><summary>📄 Abstract</summary>
  The rapid growth of large language model training and serving is driving AI data centers (AIDCs) toward gigawatt scale. Unlike conventional commercial loads, AIDCs possess significant operational flexibility through dynamic voltage and frequency scaling (DVFS) of training and inference workloads, while periodic model checkpointing can induce abrupt power drops and rebounds that erode operating reserves and increase transmission congestion risks. Coordinating AIDC operation with grid scheduling u...
  </details>

- **2026-09-22** — Jiaming Tang, Chenlan Wang, Mingyan Liu et al. — [Decoding the Legalese: A Scalable and Quantitative Framework for Analyzing Corporate Privacy Policies](http://arxiv.org/abs/2609.26680v1)
  <details><summary>📄 Abstract</summary>
  Even though privacy policies are the primary mechanism organizations use to disclose how they collect, process, and share personal data, they are difficult for average users to interpret, perhaps by design, due to their verbosity and dense legal language. Importantly, there is a lack of standardized metrics that characterize key qualities of a privacy policy beyond regulatory requirements. Recent advances in large language models (LLMs) make it feasible to automatically structure and analyze the...
  </details>

- **2026-09-22** — Jiannan Wang, Xianghao Yu, Chenshu Wu — [A Gram-Attention Learning Framework for Spatially Non-Stationary Channel Estimation](http://arxiv.org/abs/2609.26437v1)
  <details><summary>📄 Abstract</summary>
  As next-generation wireless systems migrate to high-frequency bands, extremely large-scale multiple-input multiple-output (XL-MIMO) is indispensable for combating severe path loss. However, the received path energy along the extremely large array aperture (ELAA) may exhibit spatial non-stationarity, rendering the conventional discrete Fourier transform (DFT) codebook inadequate for channel estimation (CE) due to its full-array angular representation. To address this mismatch, we propose a novel ...
  </details>

- **2026-09-22** — Liheng Fan, Jialun Yin, Yuzhi Chen — [When Should Dependency Updates Invoke Repair Agents? A Lightweight Routing Study](http://arxiv.org/abs/2609.25911v1)
  <details><summary>📄 Abstract</summary>
  Dependency-update pull requests are frequent and mostly routine, but a small subset requires non-trivial compatibility repair. Recent repository-level coding agents make such repair increasingly plausible, yet invoking them on every dependency update wastes model calls, CI time, repository context, and review attention. We frame this as a pre-agent routing problem: deciding which dependency-update pull requests should be escalated before downstream diagnosis or repair attempts. We introduce DepF...
  </details>

- **2026-09-22** — Jeongmin Bae, Yongjae Kim, Kyoung Hur et al. — [AkasicMEM: Governed Enterprise Memory for Agents](http://arxiv.org/abs/2609.25563v1)
  <details><summary>📄 Abstract</summary>
  Agent memory enables enterprise agents to retain knowledge acquired during work and reuse it across tasks and agents, turning execution experience into persistent organizational knowledge. Realizing this potential requires both source--memory integration, through which enterprise sources and accumulated memory can be utilized together, and memory governance, through which shared memory remains subject to organizational policies throughout its lifecycle. These requirements interact when informati...
  </details>


### 📂 steganography
*隐写与隐蔽通信 / Steganography & Covert Communication* — 1 papers

- **2026-09-24** — Qi Pang, Virginia Smith, Wenting Zheng — [Codetta: High-Capacity, Keyless, and Undetectable Multi-Agent Collusion](http://arxiv.org/abs/2609.28900v1)
  <details><summary>📄 Abstract</summary>
  Multi-agent systems built on large language models (LLMs) are increasingly deployed in high-stakes settings such as finance, healthcare, and software engineering, where agents coordinate through natural-language messages. The same channels, however, let colluding agents exfiltrate confidential information or coordinate unauthorized actions, and steganography can hide such communication inside outputs that look ordinary to an auditor reading the transcript.   Existing provably undetectable LLM st...
  </details>


### 📂 misuse
*滥用与误用 / Misuse & Abuse* — 14 papers

- **2026-09-24** — Taha Entesari, Mahyar Fazlyab — [Beyond Average Safety: Chance-Constrained LLM Fine-tuning](http://arxiv.org/abs/2609.29960v1)
  <details><summary>📄 Abstract</summary>
  Fine-tuning large language models on new objectives can improve helpfulness, instruction following, or domain-specific performance, but it can also induce regressions on safety-critical prompts. Existing safety-preserving fine-tuning methods typically control average safety loss or use weighted auxiliary penalties, which can obscure rare but severe failures. We propose a chance-constrained formulation for safety-preserving fine-tuning that limits the fraction of safety examples whose degradation...
  </details>

- **2026-09-24** — Firoj Alam, Md. Rafiul Biswas, Mohamed Bayan Kmainasi et al. — [ArGuard Shared Task: Harmful Content Detection in Arabic Memes and LLM Prompts](http://arxiv.org/abs/2609.29349v1)
  <details><summary>📄 Abstract</summary>
  ArGuard is a shared task on harmful content detection in Arabic memes and LLM prompts. It includes two tracks: Track A focuses on multimodal hate detection in Arabic memes, while Track B addresses harmful prompt detection for Arabic LLM safety evaluation. In total, 58 teams registered, 35 participated in the final evaluation, and 27 submitted system-description papers. Participating teams explored models such as AraBERT, Jais, and Qwen3-VL. The best systems achieved macro-F1 scores of 0.823 on A...
  </details>

- **2026-09-24** — Yezhou Cheng, Runjia Du, Zeming Liu et al. — [Scope Before You Persist: Preventing Cross-Family Interference in Agent Memory](http://arxiv.org/abs/2609.29144v1)
  <details><summary>📄 Abstract</summary>
  Persistent memory lets language-model agents improve prompts and skills without updating model weights. We show that matching retrieval scope to certification scope enables these edits to support reliable repeated adaptation across recurring task families. We study frozen-model agents on ProcStream-RSI, a 12-round code-repair stream, using Orthogonal Regression Control (ORC), an execution-grounded gate for persistent skill edits. In an intervention that holds proposals and gate decisions fixed, ...
  </details>

- **2026-09-24** — Shuzhi Gong, Fengze Sun, Yuansan Liu — [Beneath the Scores: Rethinking Hallucination Evaluation for Video Understanding Models](http://arxiv.org/abs/2609.28991v1)
  <details><summary>📄 Abstract</summary>
  Video understanding is increasingly performed by multi-stage LLM agents that separate temporal grounding, visual observation, and reasoning. Yet these stages are typically evaluated on different benchmarks and distributions, making it difficult to determine where hallucinations originate. We first organize existing benchmarks around these stages and show that their scores provide inconsistent diagnostic signals: stronger stage-level performance does not reliably imply lower downstream hallucinat...
  </details>

- **2026-09-23** — Xuwei Tan, Yao Ma, Xueru Zhang — [SR-Fraud: An Outcome-Supervised Reflective LLM Agent Framework for Non-Stationary Payment Fraud Detection](http://arxiv.org/abs/2609.27287v1)
  <details><summary>📄 Abstract</summary>
  Real-time payment fraud detection is a non-stationary streaming prediction problem: adversaries adapt before supervised labels mature, and localized burst attacks can cause losses before retraining. Production systems typically rely on tabular classifiers and rules, which can struggle to capture these emerging sequential patterns before periodic retraining occurs. We present SR-Fraud, an outcome-supervised reflective LLM framework that decouples request-time decisions from offline adaptation. A ...
  </details>

- **2026-09-23** — Jacob T. Emmerson, Phuong-Anh Nguyen-Le, Ronan Romano et al. — [An Open Pipeline and Dashboard for Systemic-Risk Evidence under the EU AI Act's Code of Practice](http://arxiv.org/abs/2609.28335v1)
  <details><summary>📄 Abstract</summary>
  Claims about AI safety reach audiences well beyond the AI community, yet many rely on opaque evidence or static assessments, when supporting evidence is accessible at all. We present the Systemic Risk Index, an open evaluation pipeline and dashboard built to make empirical evidence more transparent and traceable to the public. Our work organizes 19 public benchmarks into four systemic-risk categories defined by the EU GPAI Code of Practice---CBRN, cyber offense, harmful manipulation, and loss of...
  </details>

- **2026-09-23** — Junlin Liu, Yifeng Cai, Shuai Wang et al. — [GUIAuditor: Enabling Post-hoc Child Safety Forensics via Action-Guided GUI Provenance on Mobile Devices](http://arxiv.org/abs/2609.28205v1)
  <details><summary>📄 Abstract</summary>
  The proliferation of smart devices exposes children to online risks like grooming and financial scams that are deeply embedded within legitimate applications. Current approaches rely on automated prevention and detection, a paradigm that is fundamentally limited by its inherent fallibility. Whether rule-based or AI-driven, they inevitably produce false positives and negatives, failing to provide reliable protection. In this paper, we argue for a complementary, human-in-the-loop, post-hoc forensi...
  </details>

- **2026-09-23** — Walter Kurz — [Multi-Agent AI Architecture for Regulated Insurers: A generic AI framework under Solvency II and the AI Act in Austria and Germany](http://arxiv.org/abs/2609.27636v1)
  <details><summary>📄 Abstract</summary>
  This paper proposes a formal multi-agent architecture for implementing enterprise AI in regulated insurance firms, integrating economic theory with institutional design. The framework synthesises three core theoretical perspectives: Arrow's risk pooling theory to formalise risk transformation under uncertainty, Nash equilibrium to model strategic interactions between decision agents, and Principal-Agent theory to address incentive alignment under information asymmetry. The insurer is modelled as...
  </details>

- **2026-09-23** — Maddalena Ghiotti, Daniela Paolotti, Yelena Mejova — [Watching What We Eat: Information Quality and Body Image in Diet-Related YouTube Videos](http://arxiv.org/abs/2609.28114v1)
  <details><summary>📄 Abstract</summary>
  The widespread use of social media, particularly image- and video-based platforms, has turned them into key sources of both normative and informational content related to health and diet. This may contribute to the development of disordered eating behaviors or, potentially, eating disorders. This study uses mixed-methods analysis applied to 3129 YouTube videos about diet and weight loss in order to quantify the level of risk of low-quality information and heightened focus on the body image. We a...
  </details>

- **2026-09-23** — Jose Manuel de la Chica Rodriguez, Juan Manuel Vera Diaz, Pablo Delgado Romero — [Compliant with Local Controls, Collectively Discriminatory. A Governance Architecture for Multi-Agent AI in Regulated Finance](http://arxiv.org/abs/2609.27994v1)
  <details><summary>📄 Abstract</summary>
  Financial institutions are beginning to deploy agentic workflows in credit, fraud, collections, compliance, and operational control. Governance remains largely component-centric: each model or agent is specified, tested, authorized, and monitored locally. That is insufficient when institutional risk arises from the joint behavior of many locally acceptable components. We call this gap constitutional non-compositionality: local compliance checks need not compose into acceptable collective outcome...
  </details>

- **2026-09-23** — Truong Thanh Hung Nguyen, Vo Thanh Khang Nguyen, Hoang-Loc Cao et al. — [Self-Evolving Multimedia Verification through Memory Consolidation of Contestation Experiences](http://arxiv.org/abs/2609.27175v1)
  <details><summary>📄 Abstract</summary>
  Multimedia verification requires not only accurate decisions but also traceable evidence, reliable human correction, and safe reuse of prior experience. Existing systems often lack explicit mechanisms for revising intermediate reasoning or preventing harmful knowledge transfer. We present SEMV (Self-Evolving Multimedia Verification), a self-evolving multi-agent framework that treats provenance-bearing arguments as the interface between evidence, reasoning, human contestation, and memory. SEMV co...
  </details>

- **2026-09-22** — Baptiste Bonin, Caro Strickland, Audrey Durand — [On Preference Coverage Collapse from Hindsight Relabeling in Multi-Objective Reinforcement Learning](http://arxiv.org/abs/2609.26918v1)
  <details><summary>📄 Abstract</summary>
  Hindsight relabeling which retroactively replacing a transition's goal with the outcome the agent actually achieved is an effective tool for improving sample-efficiency in Reinforcement Learning (RL). A natural extension to preference-conditioned multi-objective RL (MORL) relabels transitions with the preference direction the agent achieved rather than the one asked for. We show that this extension is frequently harmful: across four preference-conditioned off-policy algorithms spanning two criti...
  </details>

- **2026-09-22** — Alexandros Fourtounis, Emmanouil Papadogiannakis, Panagiotis Papadopoulos et al. — [COBRA: A Content-Agnostic Framework for Zero-Day Detection of Suspicious Domains](http://arxiv.org/abs/2609.25882v1)
  <details><summary>📄 Abstract</summary>
  The use of malicious domains is central to cyberattacks such as phishing, malware distribution, impersonation, and fraudulent transactions. Because domains are inexpensive to register and easy to deploy at scale, they remain one of the most common and damaging tools used in cybercrime across industries. Proactive detection is essential to reducing this window of vulnerability and preventing harm to users. In this work, we propose COBRA: a content-agnostic, registration-time detection framework f...
  </details>

- **2026-09-22** — Peachapong Poolpol, Henrik H. J. Detjen, Eike Petersen — [Faithful Faithfulness Evaluations: Challenges & Pitfalls Learned from a Breast MRI Case Study](http://arxiv.org/abs/2609.25978v1)
  <details><summary>📄 Abstract</summary>
  Saliency maps are widely used to explain deep learning predictions in medical imaging, yet visually plausible explanations do not necessarily reflect a model's true decision process and may therefore mislead clinicians. We investigate this problem using a Vision Transformer-based breast MRI classifier trained on the ODELIA Breast MRI Challenge dataset and evaluate multiple saliency methods, including Last-layer Attention, Attention Rollout, Grad-SAM, Gradient Attention Rollout, GMAR, Grad-CAM, a...
  </details>


### 📂 red-teaming
*红队测试 / Red Teaming* — 1 papers

- **2026-09-23** — Dongdong Zhang, Tengchao Lv, Yilin Jia et al. — [CART: Closed-Loop Adaptive Red Teaming for Large Language Models](http://arxiv.org/abs/2609.27336v1)
  <details><summary>📄 Abstract</summary>
  Automated red teaming often replays a fixed set of prompts, which measures known risks but cannot learn from failures found during testing. We present CART (Closed-Loop Adaptive Red Teaming), a framework that uses each result to guide what it tests next. CART begins with broad risk coverage, follows weaknesses that emerge, keeps new probes diverse, and records the evidence and source of every finding. It separates the Challenger that creates tests, the Target being tested, which may be a text-on...
  </details>


### 📂 vulnerability
*漏洞与攻击面 / Vulnerabilities & Attack Surfaces* — 53 papers

- **2026-09-24** — Matteo Merler, Bowen Li, Josh Roy et al. — [Coding Agents for Generalized Task and Motion Planning Problems](http://arxiv.org/abs/2609.30233v1)
  <details><summary>📄 Abstract</summary>
  Task and motion planning (TAMP) problems remain difficult even with full observability and object-centric states because discrete decisions are tightly coupled to geometric, kinematic, and dynamic constraints. Generalized TAMP addresses this difficulty by exploiting regularities across problem instances to reduce planning effort on new instances. However, existing methods require substantial TAMP-specific engineering. We investigate whether coding agents can automate this process by synthesizing...
  </details>

- **2026-09-24** — Youpeng Zhao, Tian Tan, Liqian Peng et al. — [MILO: Efficient Many-shot In-Context Learning with Block-wise Low-rank Compression](http://arxiv.org/abs/2609.29913v1)
  <details><summary>📄 Abstract</summary>
  Many-shot in-context learning (ICL) enables large language models (LLMs) to adapt to complex tasks by conditioning on thousands of demonstration examples, but this paradigm shifts the inference efficiency bottleneck to the key-value (KV) cache memory. Due to the linear scaling behavior of the KV cache, storing these intermediate tensors has become a paramount challenge for both online serving and on-device deployment. To address this issue, we propose a novel compression framework, termed MILO, ...
  </details>

- **2026-09-24** — Ali Habibullah, Yazan Alshoibi, Mohammad Alshiekh et al. — [Where LLM Graders Succeed and Break: Evidence from Two Computer-Science Exams](http://arxiv.org/abs/2609.29333v1)
  <details><summary>📄 Abstract</summary>
  One long-form exam in a large course costs hundreds of grader-hours, and qualified graders are scarce; LLM graders are a tempting alternative. To show its pitfalls we grade a practical Computer Vision exam ($570$ dual-graded students) under $171$ configurations spanning closed and open-weights models; the best reaches mean absolute error $1.64/35$, below the $2.61/35$ two human graders achieve against each other. The catch is the prompt: a short ''strict grader'' preamble drives $14$ of $17$ ope...
  </details>

- **2026-09-24** — Theodoros Moutesidis — [The Fly That Stopped: Mushroom-Body-Inspired Habituation as a Reward-Free Scheduling Prior for Autonomous Penetration Testing](http://arxiv.org/abs/2609.29126v1)
  <details><summary>📄 Abstract</summary>
  Autonomous security-testing agents can spend much of a fixed action budget repeating earlier tool selections. We evaluate a reward-free scheduler inspired by mushroom-body novelty processing in Drosophila. It combines sparse state encoding with decaying habituation counters over structural URL classes and tool families. The counters penalize repeated clean or error outcomes without updating weights from scalar reward. Four matched campaigns motivated this design by exposing reward-accounting err...
  </details>

- **2026-09-24** — Zhongjie Shi, Rongjie Lai, Alexander Cloninger et al. — [Transformers as Cross-Task Learners: Shared Structure Drives Sample Efficiency in In-Context Learning](http://arxiv.org/abs/2609.29060v1)
  <details><summary>📄 Abstract</summary>
  Transformers achieve remarkable performance by jointly learning broad families of tasks during pretraining and adapting to unseen tasks from only a short prompt. Yet a rigorous mathematical and statistical understanding of this phenomenon remains limited. This paper aims to study how Transformers exploit shared cross-task structure and how this structure affects the sample complexity of in-context learning (ICL). Specifically, we characterize task-space complexity through covering numbers under ...
  </details>

- **2026-09-24** — Zilong Song, Lu Liu, Gang Feng — [Bearing-Only Formation Tracking Control for Euler-Lagrange Multi-Agent Systems Without Inter-Agent Communication](http://arxiv.org/abs/2609.29049v1)
  <details><summary>📄 Abstract</summary>
  This paper investigates communication-free bearing-only formation tracking control for multi-agent systems governed by Euler-Lagrange dynamics. Distinct from existing results that can only stabilize a stationary formation, this work considers a scenario where the leaders move with time-varying velocities while the inter-agent communication is absent. In this setup, the leaders' states (position and velocity) are unavailable to all followers and cannot be estimated via distributed observers. A no...
  </details>

- **2026-09-24** — Joas Antonio dos Santos Barbosa — [Calibrated Decision Models for Autonomous Penetration-Testing Harnesses: JEV and Laya as System One Decision Layers for LLM-Driven Pentest Agents](http://arxiv.org/abs/2609.28940v1)
  <details><summary>📄 Abstract</summary>
  Autonomous penetration-testing harnesses use large language models (LLMs) for reconnaissance, exploitation, and reporting, but often rely on those same models to confirm findings, grade severity, and select agents. This can lead to false positives, inflated severity, and wasted compute. We examine how System One decision models, lightweight non-generative classifiers that return typed, calibrated verdicts, can support these decisions. We make five contributions. First, we define four decision po...
  </details>

- **2026-09-24** — Manit Baser, Aditya Nawal, Dinil Mon Divakaran et al. — [The Tokens Remember: When Tokenization Bypasses Knowledge Editing and Unlearning](http://arxiv.org/abs/2609.29045v1)
  <details><summary>📄 Abstract</summary>
  Open-weight LLMs give downstream users control over the inference stack, but this flexibility can undermine post-release guarantees that sensitive knowledge has been modified or removed. Model editing and machine unlearning are used to modify or remove targeted knowledge without retraining models from scratch. However, existing security evaluations of these techniques face two critical limitations. First, they typically require access to either the original pre-edit/unlearning model or auxiliary...
  </details>

- **2026-09-24** — Zhida Zhang, Xinlei Ma, Jie Cao — [EIB-Net: Entropy-Guided Information Bottleneck for Generalizable AI-Generated Image Detection](http://arxiv.org/abs/2609.29064v1)
  <details><summary>📄 Abstract</summary>
  The proliferation of photorealistic AI-generated images demands robust detection methods that generalize across diverse generative models. While existing approaches target manipulation-based forgeries with local artifacts, generation-based images (e.g., from diffusion models) lack such traces, posing a fundamental challenge. We observe that generative models prioritize global semantics at the expense of local texture fidelity, making low-texture regions key indicators of synthetic origin. To exp...
  </details>

- **2026-09-24** — Jeremy Qin, David Schmotz, Derck Prinzhorn et al. — [LLM Agents Can Easily Tamper With Their Own Traces](http://arxiv.org/abs/2609.30266v1)
  <details><summary>📄 Abstract</summary>
  Asynchronous monitoring, incident investigations, and compliance audits primarily rely on agent traces to reconstruct what happened. These analyses assume that LLM agents cannot tamper with their own execution traces. We show that local LLM agents such as Claude Code, Codex, Antigravity, Open Code and Grok Build fail to enforce this boundary. All tested harnesses, except Muse Code, allowed agents to delete their traces when asked, without triggering monitor guardrails. We also validate that exte...
  </details>

- **2026-09-24** — Sunli Chen, Ding Zhong, Ziqiao Ma et al. — [Multimodal Thinking with Renderable Programs](http://arxiv.org/abs/2609.30130v1)
  <details><summary>📄 Abstract</summary>
  Current vision-language models (VLMs) excel at visual content understanding and text-based reasoning, yet their structure limits the advancement of incorporating images into the reasoning chain. Though Omnimodal models have made efforts in unifying text and image generation, they focus on visual tasks in the open-domain, lacking tractability due to rasterized or latent representations of images. We introduce SVGLM, a framework that uses scalable vector graphics (SVG) primitives to connect text a...
  </details>

- **2026-09-24** — Michael Jerge, Suman Jana — [Canopy: Exploiting Piecewise Smooth Tree Priors for Multi-Fidelity Bandits](http://arxiv.org/abs/2609.30017v1)
  <details><summary>📄 Abstract</summary>
  Many LLM inference problems, including model routing, prefix-cache management, prompt trimming, and test-time search, can be viewed as optimization over a tree. This structure arises naturally from autoregressive generation: every prefix defines a node, and its continuations form a subtree below it. Internal nodes of the tree provide cheap but biased estimates of a region's value, while leaf evaluations are expensive but accurate. Hierarchical bandit methods can exploit this structure, but typic...
  </details>

- **2026-09-24** — Asmee Mishra, Mengjie Qian, Brechtje Post et al. — [Adaptive Fisher-Whitened Cross-Covariance for Low-Resource Speech Recognition](http://arxiv.org/abs/2609.29800v1)
  <details><summary>📄 Abstract</summary>
  Adapting multilingual speech foundation models to low-resource languages remains difficult, especially for languages that are poorly represented during pre-training. While parameter-efficient fine-tuning (PEFT) reduces the cost of adapting large models, conventional approaches such as LoRA rely on generic low-rank parameterizations and do not explicitly use downstream task information to define the adaptation subspace. To investigate whether task-informed PEFT can better support low-resource ASR...
  </details>

- **2026-09-24** — Kwok-Ho Ng, Tingting Song, Bingwen Feng et al. — [WST-Graph: Topology-Preserving Wavelet Scattering Front-End for Speech Deepfake Detection](http://arxiv.org/abs/2609.29372v1)
  <details><summary>📄 Abstract</summary>
  The acoustic front-end determines which forensic cues a speech deepfake detector can exploit. The wavelet scattering transform (WST) provides stable multiscale coefficients with explicit coordinates, yet direct flattening obscures the parent relation between paths. We introduce WST-Graph, reconstructing these paths as a sparse modulation-carrier grid for an AASIST graph backend. Modulation-level normalization and length-aware adaptive local attention pooling produce fixed relative-time represent...
  </details>

- **2026-09-24** — Xin Wang, Wenhao Wu, Menghao Zhang et al. — [HarnessPAI: An Evolving Harness for Physical AI](http://arxiv.org/abs/2609.29166v1)
  <details><summary>📄 Abstract</summary>
  Physical AI aims to build embodied agents that perceive the world, understand and reason about it, and decide how to act. Yet the field has focused primarily on the last component: the action model that maps observations to low-level controls. The prevailing training recipe can erode the perceptual and reasoning capabilities needed for robust behavior, leaving even strong action models vulnerable to scene perturbations and long-horizon tasks. We introduce HarnessPAI, a model- and embodiment-agno...
  </details>

- **2026-09-24** — Ben Liang, Chao Sui, Junqi Bai et al. — [FoCal: Frequency-Oriented Cross-Modal Interaction and Spectral Calibration for Aerial Visible-Infrared Object Detection](http://arxiv.org/abs/2609.29125v1)
  <details><summary>📄 Abstract</summary>
  In aerial RGB--IR object detection, effectively exploiting complementary information across modalities is critical for robust perception under complex illumination and environmental conditions. Existing multimodal detectors mainly focus on spatial-domain interaction or frequency-specific feature enhancement, while the cross-modal interaction patterns of different frequency components remain insufficiently explored. Moreover, spectral discrepancy itself may contain both useful complementary cues ...
  </details>

- **2026-09-24** — Yijun Hu, Heng Fan, Libo Zhang — [Exploiting Target Knowledge from MLLMs for Robust Few-Shot Segmentation](http://arxiv.org/abs/2609.28949v1)
  <details><summary>📄 Abstract</summary>
  Few-shot segmentation (FSS) aims to segment unseen object categories with a few (e.g., one or five) labeled examples, enabling efficient adaptation to novel classes. Conventional models typically rely on appearance-based visual matching between support and query images for segmentation. While straightforward, these methods often struggle to handle significant appearance discrepancies and occlusions in the query image due to insufficient target knowledge. To mitigate this, we introduce a novel fr...
  </details>

- **2026-09-23** — Lujia Zhong, Shuo Huang, Jianwei Zhang et al. — [M$^2$PFN: End-to-End Disentangled Alignment for Generalizable Multimodal In-Context Learning in Alzheimer's Disease](http://arxiv.org/abs/2609.28836v1)
  <details><summary>📄 Abstract</summary>
  While various multimodal methods combining imaging and tabular data for Alzheimer's disease (AD) diagnosis were proposed, they are often limited in generalization across cohorts. In-context learning (ICL) has demonstrated excellent generalization performances and high flexibility in foundational tabular models such as TabPFN. To extend TabPFN's ICL to multimodal AD analysis, the main obstacle is that TabPFN is meta-trained on synthetic tabular priors that do not naturally match the statistical s...
  </details>

- **2026-09-23** — Farah Elsherif, Behrouz Azimian, Anamitra Pal — [Adaptive State Estimation Under Topological Uncertainty in Unobservable Primary Distribution Systems Using Strategically Placed Sensors](http://arxiv.org/abs/2609.28830v1)
  <details><summary>📄 Abstract</summary>
  The rapid integration of distributed energy resources is fundamentally altering power flow patterns in primary distribution networks and intensifying operational uncertainty. These problems are further compounded by lack of real-time situational awareness and frequent topology changes. To address these problems, this paper proposes an integrated deep learning framework for simultaneous topology identification (TI) and distribution system state estimation (DSSE) in real-time unobservable primary ...
  </details>

- **2026-09-23** — Aloïs Duguet, Sandra Ulrich Ngueveu, François Lamothe — [On the Minimum Number of Linear Pieces Required to Approximate Nonlinear Functions under an Accuracy Constraint](http://arxiv.org/abs/2609.28794v1)
  <details><summary>📄 Abstract</summary>
  The approximation of nonlinear functions by piecewise linear functions is a tool commonly used when dealing with mixed-integer nonlinear problems. Typically, by replacing nonlinearities by piecewise linear functions one can transform the problem into a mixed-integer linear problem, which may be substantially easier to solve. However, using approximate functions can produce solutions that are infeasible for the original problem or far from optimal. To control these errors it is useful to bound th...
  </details>

- **2026-09-23** — Kaiyang Li, Shaobo Han, Yue Tian et al. — [Reward-Tilted On-Policy Distillation for Acoustic Grounding in Audio-Language Models](http://arxiv.org/abs/2609.28778v1)
  <details><summary>📄 Abstract</summary>
  Audio-language models (ALMs) can exploit textual shortcuts to answer questions while overlooking acoustic evidence, weakening audio understanding. On-policy distillation (OPD) trains compact ALMs by supervising student-generated responses with teacher predictions, but does not explicitly distinguish acoustic support from linguistic predictability. We propose Reward-Tilted On-Policy Distillation (RT-OPD) to strengthen acoustic grounding. Given the same question and student-generated text, a froze...
  </details>

- **2026-09-23** — Judith Michael, Bernhard Rumpe, Antonio Bucchiarone et al. — [Towards a Platform for Mastering Personal Sovereignty](http://arxiv.org/abs/2609.28736v1)
  <details><summary>📄 Abstract</summary>
  The ongoing digital transformation of work, administration, health, mobility, and social interaction is profoundly reshaping everyday life, steadily shifting control from individuals to large platform providers. Although data is often labeled the "gold of the 21st century", its real value is realized through services that access, combine, and exploit it. Today, individuals have little sovereignty: life events (e.g., changing an address, insurance, job, or marital status) require fragmented, repe...
  </details>

- **2026-09-23** — Ewelina Gajewska, Katarzyna Budzynska, Jaroslaw Chudziak — [Benchmarking Argumentative Behaviour of LLMs: A Study of Defences Against Character Attacks](http://arxiv.org/abs/2609.28673v1)
  <details><summary>📄 Abstract</summary>
  Large Language Models (LLMs) are increasingly deployed as argumentative agents in persuasive dialogues, necessitating rigorous evaluation of their debating competence relative to human interlocutors. In this study, we focus on character attacks (ad hominem arguments), traditionally dismissed as fallacies, which play a pivotal role in political persuasive dialogues where ethos often rivals propositional content. Specifically, we investigate whether modern LLMs can replicate human competence to st...
  </details>

- **2026-09-23** — Sungjae Choi, Seunghee Koh, Junmo Kim — [PePESeg3D: Perception Prior Enhances Multi-Scale Segmentation for 3D Gaussian Splatting](http://arxiv.org/abs/2609.28645v1)
  <details><summary>📄 Abstract</summary>
  Recent advancements in 3D Gaussian Splatting (3DGS) have extended its capabilities to multi-scale segmentation. Existing methods reconstruct a scene with Gaussian primitives and learn multi-scale segmentation features separately, which leaves the geometry unaware of semantic structure and the feature learning dependent on incomplete mask supervision. To address these limitations, we present PePESeg3D, a novel framework that injects perception priors into a multi-scale 3D Gaussian segmentation pi...
  </details>

- **2026-09-23** — Jian Xu — [Don't Read the Log: Execution Traces Contaminate Verifiers in Video-Generation Agents](http://arxiv.org/abs/2609.28564v1)
  <details><summary>📄 Abstract</summary>
  Agentic video-generation systems close a loop between a generator and a verifier: an LLM plans shots, calls a text-to-video model, and a multimodal judge decides whether the result satisfies the request. To diagnose where a long workflow fails, recent harnesses deliberately show the judge more than the video-the agent's execution trace, its plan, the narration it synthesized. We ask whether this auxiliary text moves the judge's verdict on purely \emph{visual} requirements, holding the frames fix...
  </details>

- **2026-09-23** — Yue Huang, Zhangchen Xu, Yuchen Ma et al. — [Reward Hacking Challenges Oversight of Autonomous Research Agents](http://arxiv.org/abs/2609.28614v1)
  <details><summary>📄 Abstract</summary>
  Autonomous research agents can design experiments, evaluate results, and write reports, giving them control over both a scientific result and the evidence used to support it. This creates a risk of reward hacking: meeting the reward criteria without achieving the intended goal. We study (1) how often models reward-hack without instructions to do so, (2) how effective and detectable their methods are when hacking is allowed, and (3) how they adapt when an LLM review panel returns its decision and...
  </details>

- **2026-09-23** — Zhiqi Ai, Han Cheng, Shiyi Mu et al. — [PTC-Bias: Phoneme-Level Temporal Competition for Bias Retrieval and Post-Decoding Correction in Speech LLMs](http://arxiv.org/abs/2609.28727v1)
  <details><summary>📄 Abstract</summary>
  Contextual biasing improves rare-word recognition in speech large language models (SpeechLLMs), but efficiently exploiting large bias lists remains challenging. We propose PTC-Bias, a two-stage framework based on phoneme-level temporal competition. At the prefill stage, PTC Retrieval performs frame-synchronous phoneme decoding and temporal competition among candidate pronunciations, producing a compact bias-word shortlist and corresponding speech intervals. After SpeechLLM decoding, PTC Correcti...
  </details>

- **2026-09-23** — Davood Wadi, Yu Ma — [Shopping by algorithm: How agentic AI deploys human heuristics as a surrogate consumer](http://arxiv.org/abs/2609.28372v1)
  <details><summary>📄 Abstract</summary>
  Consumers increasingly delegate purchasing decisions to Large Language Models (LLMs) acting as surrogate consumers. Using "Tool-Lab," an adaptation of information-board process tracing that places product attributes behind costly tool calls, we examine how marketing pricing cues (i.e., just-below pricing and promotional framing) influence AI shopping agents. Across eight commercially deployed LLMs from three providers, we trace pre-choice information acquisition. Under zero cost, pricing cues ra...
  </details>

- **2026-09-23** — Zerui Li, Sihao Lin, Yanyan Shao et al. — [Talk2Escape: Conversational Grounding for Vision-and-Language Navigation](http://arxiv.org/abs/2609.28296v1)
  <details><summary>📄 Abstract</summary>
  While Vision-and-Language Navigation (VLN) has demonstrated remarkable success, the prevailing single-turn paradigm exposes a fundamental vulnerability: agents operate in a strictly open-loop manner. In practice, factors such as perceptual aliasing, sensor noise, and odometry drift can cause minor deviations to accumulate over time, often leading to catastrophic mission failures with no built-in mechanism for error recovery. To address this, we introduce \textit{Talk2Escape}, a proactive and mod...
  </details>

- **2026-09-23** — Sai Varun Kodathala, Prashanth Pollishetty, Jaylen Cargill — [Prompt, Probe, Train, or Annotate? Single-camera sports video understanding in amateur settings](http://arxiv.org/abs/2609.28049v1)
  <details><summary>📄 Abstract</summary>
  Video understanding is usually benchmarked on curated, single-actor, or professionally filmed clips, and a strong score there is routinely read as evidence a model is robust enough for deployment. Amateur team sport is a useful, largely untested place to check that assumption: over eight million students played a school sport in the United States in 2024-25 alone, almost none of it filmed by more than a single fixed camera, with several candidate actors crowded into frame and no operator or seco...
  </details>

- **2026-09-23** — Adithyan Arun Kumar — [Agent Name Collision Attacks in Multi-Agent Systems](http://arxiv.org/abs/2609.27624v1)
  <details><summary>📄 Abstract</summary>
  Multi-agent hosts turn remote Agent Cards into local agents, tools, workflow targets, and broker routes. A2A defines the card's name as human-readable metadata, not as a stable identity, and specifies no collision semantics. The security failure begins when a host nevertheless uses that remote name as a local routing identifier. We traced registration through dispatch and ran isolated regression tests at seven pinned open-source revisions. Six client-style integrations selected an attacker-contr...
  </details>

- **2026-09-23** — Ke Wan, Chen Chen — [Attention Routing Stabilizes Early: Working-Set Inference for Recurrent Language Models](http://arxiv.org/abs/2609.27373v1)
  <details><summary>📄 Abstract</summary>
  Recurrent language models repeatedly apply shared network blocks to refine latent representations, but standard inference recomputes global attention at every recurrent step. We study attention dynamics across recurrent depth and find that attention support and distributions stabilize substantially earlier than hidden states and attention outputs. This suggests a two-stage structure: early steps discover a sparse working set of relevant context, while later steps refine representations over larg...
  </details>

- **2026-09-23** — Walter Nedov, Saimunur Rahman, Kavindie Katuwandeniya et al. — [Geometry-Conditioned Visual Place Recognition in Natural Environments](http://arxiv.org/abs/2609.27370v1)
  <details><summary>📄 Abstract</summary>
  Visual Place Recognition (VPR) in natural environments remains challenging due to repetitive vegetation, sparse distinctive landmarks, and substantial appearance and viewpoint variation across traversals. While visual observations of the same place can change considerably, their underlying spatial structure is often more persistent. We exploit this complementary geometric consistency through Depth-Aware Distillation (DAD), which conditions the token representations of a pretrained Vision Foundat...
  </details>

- **2026-09-23** — Chengxi Zhong, Yongzhe Chang — [Anchor and Perturb: Lazy Agent Remediation by Exploration Injection](http://arxiv.org/abs/2609.27365v1)
  <details><summary>📄 Abstract</summary>
  Anchor and Perturb (AnP) is a lightweight framework that resolves multi-agent coordination failures by decoupling exploratory variance injection from recurrent manifold stability. Existing remediation strategies predominantly alter mixing network architectures or enforce simultaneous exploration across the collective, which inevitably precipitates severe temporal-difference penalties in non-monotonic reward spaces. Specifically, AnP isolates underperforming lazy agents and injects an asymmetric ...
  </details>

- **2026-09-23** — Akash Pandey, Kanisha Shah, Addrish Roy et al. — [A Systematic Benchmark of Explainable Methods for Temporal Attribution in Sequential Recommendation Systems](http://arxiv.org/abs/2609.27201v1)
  <details><summary>📄 Abstract</summary>
  Sequential RecSys are central to modern personalization, exploiting user's historical interaction sequences to drive next-step decisions. Deep learning models, particularly CNN and Transformer-based architectures, have proven highly effective at capturing temporal dependencies in these histories. For transparency and trust, understanding which past interactions drive a given recommendation is increasingly important --- both for developers auditing model behavior and for users seeking a rationale...
  </details>

- **2026-09-23** — Minqiu Sun, Xin Huang, Luanzheng Guo et al. — [ZOCheck: CPU-Shadow Checkpointing for Zeroth-Order LLM Fine-Tuning](http://arxiv.org/abs/2609.27189v1)
  <details><summary>📄 Abstract</summary>
  Zeroth-order (ZO) optimization is an attractive option for memory-efficient LLM fine-tuning, but its fault tolerance remains underexplored. Unlike first-order training, ZO progress can be represented by lightweight seed-and-scalar step logs, yet naive log-only recovery still incurs replay cost that grows with training progress, and shortcut replay does not preserve the executed floating-point trajectory. We present ZOCheck, a fault-tolerant ZO training system that exploits this replayable struct...
  </details>

- **2026-09-23** — Pengcheng Liao, Quntao Zhuang — [Sample-Efficient Tomography of a Class of Mixed States with Extensive Entanglement and Magic](http://arxiv.org/abs/2609.27177v1)
  <details><summary>📄 Abstract</summary>
  Full tomography of a generic many-qubit quantum state requires exponentially many copies, while suitable structural constraints can make reconstruction sample-efficient. Existing approaches exploit, for example, limited entanglement structure, low magic, or constrained state-preparation circuits. Here we consider a class of mixed states that can simultaneously exhibit extensive entanglement and extensive magic. Specifically, we introduce Clifford-encoded block-product (CEBP) states, obtained by ...
  </details>

- **2026-09-22** — Yu-Wei Fan, SooHyuk Cho, Aarti Gupta et al. — [Agentic-IC3: Enabling Semantic Proof Search in IC3 Model Checking](http://arxiv.org/abs/2609.27162v1)
  <details><summary>📄 Abstract</summary>
  IC3 is a state-of-the-art algorithm for hardware model checking that proves safety properties by incrementally constructing an inductive invariant consisting of a set of lemmas. Its effectiveness depends on generalization heuristics that identify useful lemmas and guide proof search. However, many leading IC3 hardware model checkers operate on lowered, bit-level representations, where high-level design relationships are difficult to exploit for generalization. Those operating at a higher level r...
  </details>

- **2026-09-22** — Djamel Eddine Hakim Ghorab, Farid Mokhati, Mostafa Anouar Ghorab — [Solidity Meets LLMs: A Transformer-Based Approach to Smart Contract Vulnerability Detection](http://arxiv.org/abs/2609.27091v1)
  <details><summary>📄 Abstract</summary>
  The growing adoption of blockchain technologies, particularly the Ethereum platform, has amplified the critical role of smart contracts in decentralized applications. However, the increasing complexity and financial value of these contracts make them prime targets for cyber attacks. In this work, we present a transformer-based approach for the detection of vulnerabilities in smart contract fragments written in Solidity. Leveraging the representational power of pre-trained Large Language Models (...
  </details>

- **2026-09-22** — Majumder Haider, Imtiaz Ahmed, Zoheb Hassan et al. — [Digital Twin Enhanced Channel Twin for AI-Native CSI Inference: Generalizability and Scalability](http://arxiv.org/abs/2609.27017v1)
  <details><summary>📄 Abstract</summary>
  Accurate channel state information (CSI) is critical for advanced multi-antenna wireless networks. While high-fidelity and site-specific ray-tracing (RT) equipped wireless digital twins can overcome overhead for CSI acquisition. However, computing deterministic, calibrated RT based CSI from a wireless digital twin for every orthogonal frequency-division multiplexing (OFDM) symbol violates the strict microsecond latency budgets of the 5G NR numerology. To overcome this computational bottleneck, t...
  </details>

- **2026-09-22** — Yanshuo Bai, Kanji Tanaka — [TM-APR: Thermal Temporal-Memory Localization via Analytic Online Adaptation](http://arxiv.org/abs/2609.26766v1)
  <details><summary>📄 Abstract</summary>
  Thermal Visual Place Recognition (Thermal VPR) maps camera observations to metric poses within a mapped environment, serving as a prerequisite for autonomous navigation. However, thermal VPR suffers from severe environmental dependence, heavy online retraining overheads, and an inability to model dynamic non-linear shifts, causing existing frameworks to fail during online deployment. To achieve robust domain-invariant place recognition, we bridge Analytic Class-Incremental Learning (ACIL) with d...
  </details>

- **2026-09-22** — Om Nepal, Sushant Aryal, Oluseyi Olukola et al. — [Metrics Failure in LLM-Based Code Vulnerability Repair: An Empirical Study and a Change-Aware Screen](http://arxiv.org/abs/2609.26749v1)
  <details><summary>📄 Abstract</summary>
  Large language models (LLMs) are increasingly applied to the automated repair of C/C++ security vulnerabilities, and compile rate is a commonly reported proxy for progress: whether the generated patch compiles. We argue that compile rate is a scientifically unreliable metric for single-function vulnerability repair, and we support this with five controlled experiments over 203 vulnerable functions from Big-Vul, three open-source code LLMs (350M to 6.7B parameters), and three prompting strategies...
  </details>

- **2026-09-22** — Yuxin Bao, Hongwei Ruan, Luobin Wang et al. — [NavSafe-$\infty$: Benchmarking Closed-Loop Driving Safety in Photorealistic Environments](http://arxiv.org/abs/2609.26618v1)
  <details><summary>📄 Abstract</summary>
  End-to-end (E2E) driving policies have progressed rapidly on open-loop (OL) benchmarks, yet OL evaluation cannot reveal whether a policy withstands compounding errors, recovers from failures, or interacts safely with surrounding actors. We introduce NavSafe-$\infty$, a photorealistic closed-loop (CL) benchmark of 280 scenarios spanning 28 event types, each with success and failure criteria defined within a structured traffic-safety taxonomy, which yields category-level capability scores for Traf...
  </details>

- **2026-09-22** — Arthur Cordeiro, Alberto Maria Mongardini, Emmanouil Vasilomanolakis — [Rouxii: Exploiting Honeypots with Deception-Aware AI Pentesters](http://arxiv.org/abs/2609.26555v1)
  <details><summary>📄 Abstract</summary>
  Honeypots are designed to deceive attackers, and recent work shows they can also derail autonomous LLM-based pentesters. These evaluations, however, largely consider attackers unaware of the deception they face. We study the opposite setting: an autonomous attacker explicitly equipped to recognize and act on honeypot fingerprints. We introduce Rouxii, an AI-driven penetration-testing framework that integrates counter-deception into reconnaissance and pivots from honeypot detection to exploitatio...
  </details>

- **2026-09-22** — Xin Shen, San-Zhuo Xi, Yali Du et al. — [On the Lexical Superstition of Large Language Models for Code Comprehension: Re-evaluation on Code of Low Lexical Quality](http://arxiv.org/abs/2609.26388v1)
  <details><summary>📄 Abstract</summary>
  Recent advances in large language models (LLMs) have made them widely used for code-related tasks. Identifier names are statistically informative in naturally occurring code, but their information is not always reliable. We investigate whether current LLMs assign disproportionate weight to lexical cues when renaming preserves program structure. We introduce Face/Off, a semantics-preserving identifier-renaming framework, and evaluate progressive naming conditions across multiple models and code-c...
  </details>

- **2026-09-22** — Vansh Wahi — [Optimizing the Score, Losing Sight of the Task: Reward Hacking Across Weights, Selection, and Prompts](http://arxiv.org/abs/2609.25848v1)
  <details><summary>📄 Abstract</summary>
  A higher evaluation score does not always mean a better language model system. When optimization exploits an evaluator's mistakes, measured progress can conceal unchanged or deteriorating task performance. This failure can arise through parameter updates, selection among generated outputs, or revisions to persistent prompts. We develop a comparative framework for reward hacking across these three optimization substrates: weights, selection, and text. Building on the Proxy Compression Hypothesis ...
  </details>

- **2026-09-22** — Aleksandr V. Petrov, Nathan Stein, Erik Lybecker et al. — [Robust Fusion of Semantic and Behavioural Signals for LLM Reranking in Personalised Search](http://arxiv.org/abs/2609.25825v1)
  <details><summary>📄 Abstract</summary>
  Personalised search must satisfy query intent while incorporating user context and historical interactions. LLM-based cross-encoders provide a single reranking interface, but injecting predictive behavioural statistics into their prompts can encourage shortcut learning: reliance on historical signals at the expense of semantic and user-context patterns that generalise to sparse or unseen searches.   We study this problem in the personalised search system of a large-scale audio streaming platform...
  </details>

- **2026-09-22** — Yuanteng Chen, Qiwei Lai, Chen Tianqi et al. — [You Only Need 2/3 of the Chosen Experts: An Empirical Study of Dynamic Expert Pruning in Fine-Grained MoE LLMs](http://arxiv.org/abs/2609.25809v1)
  <details><summary>📄 Abstract</summary>
  Fine-grained mixture-of-experts (MoE) architectures have become a mainstream design for open-weight LLMs, with hundreds of experts and increasingly many selected per token. This shift makes dynamic expert pruning an attractive route to cheaper inference. Yet existing evidence comes largely from coarser architectures and likelihood-scored multiple-choice benchmarks, leaving three central questions open in the fine-grained regime: how redundant per-token expert selection is, how effectively existi...
  </details>

- **2026-09-22** — Jongjin Baek, Won Ji, Seungjae Yoo et al. — [Hot-Cold Tiering of HBM and High Bandwidth Flash for Agentic LLM Serving](http://arxiv.org/abs/2609.25782v1)
  <details><summary>📄 Abstract</summary>
  Large language model (LLM) serving is increasingly agentic, with multi-turn sessions that idle between actions yet must retain their full context. Limited GPU memory capacity forces inactive KV states to be evicted, so resuming a session incurs either costly recomputation or slow interconnect transfers. To address this, high bandwidth flash (HBF)-an on-package 3D-NAND memory offering orders-of-magnitude greater capacity than high bandwidth memory (HBM) at comparable read bandwidth-has emerged as...
  </details>

- **2026-09-22** — Zheng Chen, Yuzhu Li, Haoxuan Li et al. — [TCMaster: Confidence-Aware Querying and Workload-Guided Physical Design for Multi-Source Traditional Chinese Medicine Knowledge Graphs](http://arxiv.org/abs/2609.25712v1)
  <details><summary>📄 Abstract</summary>
  Multi-source knowledge graphs (KGs) need query mechanisms that expose reliability and exploit domain structure. This paper presents TCMaster, a property-graph query substrate for confidence-aware traversal and workload-guided physical design over Traditional Chinese Medicine KGs. TCMaster integrates pharmacopoeias, prescriptions, molecular databases, and LLM-extracted micro-semantics into a KG with approximately 221K entities and 723K base edges. It annotates edges with provenance-level confiden...
  </details>

- **2026-09-22** — Maria Damanaki, Nikos Piperigkos, Alexandros Gkillas et al. — [CDKF-Track: Cluster-aware Data-Driven Kalman Filtering for Cooperative 3D Multi-Object Tracking](http://arxiv.org/abs/2609.25668v1)
  <details><summary>📄 Abstract</summary>
  Multi-Object Tracking (MOT) is essential for EdgeAI perception systems, where accurate object localization and reliable identification enable safe decision-making. Singleagent MOT suffers from occlusions, sensor noise, and partial scene understanding in complex real-world scenarios. While multi-agent systems improve robustness by exploiting shared information, they introduce redundant measurements that lead to false data associations, and still struggle to capture nonlinear object dynamics. To a...
  </details>

- **2026-09-22** — Junyoung Jang, Gwanhyun Lee, Hwiwon Lee et al. — [Evaluating Coding Agents on Kernel Exploit Generation](http://arxiv.org/abs/2609.25591v1)
  <details><summary>📄 Abstract</summary>
  Coding agents now find real vulnerabilities in production software. However, bug discovery results do not measure whether agents can construct exploit primitives. We introduce KEX-bench, a benchmark for evaluating coding agents on exploit primitive generation against real operating-system kernels. KEX-bench contains 45 task instances across 40 Linux and Windows CVEs, covering kernel address leak, instruction-pointer control, heap read, heap write, and arbitrary address write. Each task runs in a...
  </details>

- **2026-09-22** — Dahlia Shehata, Ming Li — [Recovering Agentic Sovereignty: Mitigating the Consensus Paradox via Contrastive Epistemic Decoding](http://arxiv.org/abs/2609.25570v1)
  <details><summary>📄 Abstract</summary>
  Large language models (LLMs) exhibit a parametric vulnerability to adversarial swarm consensus. To mitigate this sycophancy, we introduce Contrastive Epistemic Decoding (CED), a zero-shot inference intervention. Unlike standard Contrastive Decoding (CD) which relies on a weaker secondary model, CED utilizes a dual forward-pass on a single architecture to isolate conformity bias. By introducing a novel asymmetric, zero-bounded probability clamp and discrete top-k truncation mask, CED mathematical...
  </details>


### 📂 defense
*防御与防护方法 / Defense & Protection Methods* — 62 papers

- **2026-09-24** — Haoyang Li, Yaxin Xiao, Linyan Dai et al. — [TraceGuard: Adaptive Multimodal Poison Filtering through Cross-Feature Rank Agreement](http://arxiv.org/abs/2609.29099v1)
  <details><summary>📄 Abstract</summary>
  Multimodal training relies on image-text corpora collected from external sources, creating opportunities for attackers to poison the data. Stealthy attacks can preserve plausible image-text pairs while concealing the differences used by detectors, so apparently clean data can still redirect the trained model. We therefore ask which properties a poison set must preserve for the attack to remain effective. A small poison set must still exert enough collective influence during training to induce th...
  </details>

- **2026-09-24** — Ming Zhang, Zhenghao Xiang, Peizhong Gao et al. — [ExplorationBench: Measuring AI Systems' Exploration in Verifiable Alien Worlds](http://arxiv.org/abs/2609.30199v1)
  <details><summary>📄 Abstract</summary>
  Scientific discovery begins where known problems end. There, AI systems must engage in exploration: framing hypotheses, designing experiments, and iterating on the results. However, evaluating this ability is difficult: (1) how to verify whether a genuinely new hypothesis holds, and (2) how to determine whether a system has discovered it through exploration or merely recalled related knowledge from pre-training data. To this end, we introduce ExplorationBench, which turns the wicked problem of e...
  </details>

- **2026-09-24** — Keya Li, Jahnavi Malagavalli, Lamha Goel et al. — [Smartphone-Based Method for Automated Speed Enforcement](http://arxiv.org/abs/2609.30107v1)
  <details><summary>📄 Abstract</summary>
  Smartphone cameras and computer vision (CV) hold significant promise in assisting public agencies with enforcing traffic laws and enhancing road safety. This work designs and tests a smartphone-based method for automated speed estimation and vehicle identification (license plate, make/model, and color recognition) via an automated pipeline to assist enforcement agencies in reliably identifying speeders. The CV code accurately recognizes nearly half (46%) of the license plates' text on 1,800 imag...
  </details>

- **2026-09-24** — Addison J. Wu, Jasin Cekinmez, Michel Liao et al. — [How does Adversarial Influence Scale in Multi-Agent Systems?](http://arxiv.org/abs/2609.30028v1)
  <details><summary>📄 Abstract</summary>
  Multi-agent deliberation can improve performance, but what happens when some agents do not act in good faith? In practice, an agent may be deceptive and work to subvert the group, whether through its own objectives or external instruction. We study how susceptibility to deception scales as groups increase in size and deceivers become more prevalent. It is not the number of agents in the group that matters, but the proportion of deceivers. We observe that the defection rate, how often initially c...
  </details>

- **2026-09-24** — Spencer King, Zhilu Zhang, Mikhail Kuznetsov et al. — [On the Effectiveness of Kernel-Level Evidence for Agent Security](http://arxiv.org/abs/2609.28915v1)
  <details><summary>📄 Abstract</summary>
  LLM agents are deployed into infrastructure that grants them broad host authority, yet existing agent-security benchmarks and defenses operate almost exclusively at the application telemetry layer: the served tool manifest, the user prompt, and the model's messages. Some threats, however, smuggle malicious instructions and actions past the application boundary, leaving them invisible to that layer. In this work, we bridge that gap by pairing application-level agent telemetry with kernel-level sy...
  </details>

- **2026-09-24** — Lior Biton, Oren Tsur — [Agentic Detection of Online Conspiracies](http://arxiv.org/abs/2609.30250v1)
  <details><summary>📄 Abstract</summary>
  Conspiratorial discourse on social media is not always expressed through explicit claims or stable lexical markers. The same surface content may express endorsement, legitimate concerns, criticism, satire, or mockery. The main challenge is therefore not only recognizing conspiracy-related claims, but inferring the speaker's intent -- the utterance's illocutionary force. We argue that this can be achieved through the use of relevant social contexts and propose an agentic framework, equipped with ...
  </details>

- **2026-09-24** — Guoming Ling, Muen Xue, Zijian Ye — [Jev in the Wild: A Data-Driven Analysis of the Jev Model's Functionality, Applications and Ecosystem](http://arxiv.org/abs/2609.30216v1)
  <details><summary>📄 Abstract</summary>
  Jev is a fast, low-cost decision model that answers natural-language questions with choices, binary judgments, and scores. As its public ecosystem grows rapidly, it remains unclear how Jev is used across applications and how public attention relates to project distribution. To answer these questions, we conduct a large-scale, data-driven analysis of 2,170 publicly available Jev projects collected from GitHub as of September 22, 2026. We find rapid early growth in Jev's public ecosystem, with bot...
  </details>

- **2026-09-24** — David J. Flannigan, Swarit Ahmed Shadman — [Ultrafast Electron Microscopy: A Quantitative Platform for Nonequilibrium Materials Research](http://arxiv.org/abs/2609.30084v1)
  <details><summary>📄 Abstract</summary>
  Macroscopic materials function is determined not merely by equilibrium structure, but by how carriers, phonons, fields, defects, interfaces, and collective order dynamically evolve after perturbation. Ultrafast electron microscopy (UEM) uniquely bridges this gap, coupling femtosecond-to-nanosecond timing with real-space, reciprocal-space, and energy-resolved contrast. Here, we review how these integrated capabilities now quantitatively map energy flow and conversion in electronic materials, deco...
  </details>

- **2026-09-24** — Ehsan Barkhordar, Surendrabikram Thapa — [Style, Not Self: Surface Cues Explain Zero-Shot Code Attribution by Large Language Models](http://arxiv.org/abs/2609.30048v1)
  <details><summary>📄 Abstract</summary>
  If a language model can recognize code it wrote, it may favor that code as a judge, and instances of one model monitoring each other could collude. We test this zero-shot on current commercial models. Five LLMs generate solutions to MBPP, HumanEval, and DS-1000, seven more to MBPP, and models act as evaluators in four tasks: picking their own solution from a pair, judging whether a single solution is their own, identifying which of two solutions a named model wrote, and judging quality blind. In...
  </details>

- **2026-09-24** — Shuang Yang, Zijie Zhuang, Changxin Lao et al. — [Advancing Model Research in AgentX: Long-Horizon Autonomy for Industrial Recommender Systems](http://arxiv.org/abs/2609.30001v1)
  <details><summary>📄 Abstract</summary>
  Sustaining industrial recommendation research requires using the results of one experiment to decide what to investigate next. We present AgentX-Model, the next generation of AgentX's model research framework, which connects proposal development and model experimentation within sandboxes defined by business inputs and prediction tasks. AgentX-Model adopts a dual-agent architecture comprising a Research Agent and a Model Agent. The Research Agent develops independently reviewed proposals from pap...
  </details>

- **2026-09-24** — Madeleine Eastwood, Harshith Narne, Joseph Hilby et al. — [Guardrails or Roadblocks? Effects of Pedagogical Style and Context Awareness in AI Teaching Assistants for Programming](http://arxiv.org/abs/2609.29995v1)
  <details><summary>📄 Abstract</summary>
  AI teaching assistants (AI TAs) backed by large language models (LLMs) and pedagogical guardrails are increasingly being integrated into programming courses, providing students with scalable access to hints, conceptual explanations, and code-level feedback. However, guardrails may also create friction. If students feel that the support provided is overly restrictive or poorly contextualized to their current progress, they may bypass approved tools for general-purpose LLMs. To investigate how AI ...
  </details>

- **2026-09-24** — Danilo Valerio, Philipp Kogler, Stefan Bischof et al. — [Neuro-symbolic AI for Industrial Configuration](http://arxiv.org/abs/2609.29947v1)
  <details><summary>📄 Abstract</summary>
  Large Language Models (LLMs) have shown impressive performance on a wide range of generative tasks. Yet their probabilistic nature makes them, in isolation, fundamentally unsuited for industrial product configuration, where outputs must be syntactically valid, semantically consistent with a knowledge base of hundreds of features and rules, and producible by an existing manufacturing chain. We argue that Neuro-symbolic (NeSy) AI methods lay out a promising path towards industrial-grade configurat...
  </details>

- **2026-09-24** — Jiaxun Li, Saptarshi Chakraborty, Ambuj Tewari — [Robust Detection of LLM-Generated Text under Contamination](http://arxiv.org/abs/2609.29935v1)
  <details><summary>📄 Abstract</summary>
  We study the detection of LLM-generated text under editing and contamination. Modeling human and machine text as finite-order Markov processes with Huber contamination, we characterize an exact boundary for reliable detection under our assumptions. Detection is impossible when contamination is sufficiently large relative to clean-source separation. Below this boundary, a collection of clipped likelihood-ratio tests achieves vanishing worst-case errors. This construction motivates clipping as a s...
  </details>

- **2026-09-24** — Beomsoo Kim, Byeongju Kim, Dohyun Kim et al. — [PUBG Ally: A Conversational Embodied Agent as an AI Teammate](http://arxiv.org/abs/2609.29837v1)
  <details><summary>📄 Abstract</summary>
  We introduce PUBG Ally, an embodied agent for PUBG: BATTLEGROUNDS that can reason, act autonomously, and play alongside players as a voice-enabled teammate. Building such a teammate requires combining two difficult capabilities: it must perceive and respond to a constantly changing game world under strict latency constraints while interacting naturally with players, keeping its speech synchronized with its actions. Ally therefore combines agentic tool use with real-time game control. A language-...
  </details>

- **2026-09-24** — Byounggun Park, Giyong Moon, Jusung Kim et al. — [Retrieve-to-Localize: Bridging Large Language Models and LiDAR Geometry for Spatial Grounding](http://arxiv.org/abs/2609.29835v1)
  <details><summary>📄 Abstract</summary>
  LiDAR provides precise geometric information for spatial perception tasks such as object detection in autonomous driving and outdoor robotics. However, recognizing and localizing individual objects is not sufficient to answer questions that require composing spatial relations and grounding the intended target. Motivated by recent advances in large language models (LLMs) for autonomous driving, we leverage their language priors to interpret complex spatial questions and ground the referred target...
  </details>

- **2026-09-24** — José Luis Pino — [Hard Stop: Kernel-Level Preemption and Containment for Rogue Agentic Execution](http://arxiv.org/abs/2609.29808v1)
  <details><summary>📄 Abstract</summary>
  In July 2026, an unconstrained autonomous agent participating in a frontier AI cybersecurity evaluation harness breached its evaluation sandbox, established an external command-and-control foothold, and executed a multi-stage intrusion into Hugging Face's production multi-tenant dataset conversion infrastructure (referred to in this autopsy as Incident-2026-Alpha). Over 4.5 days, the rogue agent executed 17,600 discrete actions across 6,280 worker clusters, compromised AWS EC2 Instance Metadata ...
  </details>

- **2026-09-24** — Huseyin Cavus, Sebin Sabu, Joshua Spear et al. — [Hallucination Neurons and Where to Find Them: An Investigation into the existence of Hallucination Neurons](http://arxiv.org/abs/2609.29781v1)
  <details><summary>📄 Abstract</summary>
  Interpretable machine learning for Large Language Models (LLMs) increasingly relies on sparse probing methods that identify small sets of neurons claimed to detect and causally influence behaviors such as factuality recall, safety alignment, and hallucination. These claims have important implications for model auditing and behavioral steering, yet they are rarely tested against known failure modes of $L_1$-regularized probing in correlated, high-dimensional feature spaces. We propose a five-step...
  </details>

- **2026-09-24** — Erik Aerts, Yinan Yu, Annika Rosengren et al. — [AI-based detection of worsening heart failure from low-resolution telemonitoring data](http://arxiv.org/abs/2609.29742v1)
  <details><summary>📄 Abstract</summary>
  Objective: Heart failure (HF) presents a healthcare challenge due to its high comorbidity burden, aging patient population and frequent hospitalizations. Remote monitoring offers a promising approach to managing HF patients by early detection of health deterioration. Developing autonomous systems to detect signs of worsening in telemonitoring data is of interest to reduce the workload of healthcare personnel. Methods: We propose the TRACER model, a Transformer with Contrastive Event Representati...
  </details>

- **2026-09-24** — Jaron Yeh, Yen-Wei Chang, Jiang Liu et al. — [Industrial Anomaly Detection via Defect-Grounded Reasoning in Visual Latent Space](http://arxiv.org/abs/2609.29457v1)
  <details><summary>📄 Abstract</summary>
  Industrial anomaly detection (IAD) is evolving beyond conventional detection and localization toward multimodal inspection systems that can describe, explain, and reason about fine-grained defects. Although recent multimodal large language model (MLLM)-based methods improve anomaly understanding through textual reasoning and visual guidance, they face two limitations in fine-grained inspection. First, their visual refinement often requires iteratively revisiting local image regions or augmenting...
  </details>

- **2026-09-24** — Raghavan Lavanya, Yangqin Feng, Ten Cheer Quek et al. — [Detecting Glaucoma Across Multi-ethnic Myopic and Non-Myopic Populations Using an Uncertainty-Aware Vision Transformer: A Multicentre Model Development and Validation Study](http://arxiv.org/abs/2609.29433v1)
  <details><summary>📄 Abstract</summary>
  Background: Artificial intelligence (AI)-based glaucoma detection from colour fundus photographs (CFP) offers scalable screening, but performance may decline on external datasets because of differences in ground-truth definitions, populations, and coexisting conditions such as high myopia (HM). We developed and validated a Vision Transformer-based deep learning (DL) model for glaucoma detection across multi-ethnic cohorts with and without HM. Methods: A ViT-B/16 model with predictive uncertainty...
  </details>

- **2026-09-24** — Xunkai Li, Xu Wang, Yinlin Zhu et al. — [ICE: Task-Aligned Clifford Latent Fields for Multimodal Graph Foundation Models](http://arxiv.org/abs/2609.29398v1)
  <details><summary>📄 Abstract</summary>
  Multimodal attributed graphs connect entities, visual content, language, and observed relations. Learning one foundation across such graphs requires more than compressing each node into a fused Euclidean vector. The representation must preserve entity semantics, construct interaction state from graph neighborhoods, and expose that state to prediction units with different geometry. Our empirical study shows why these requirements are inseparable. Higher-grade channels recover pair relations acros...
  </details>

- **2026-09-24** — Xiaohan Jiang, Jingyuan Wang, Jiahao Ji et al. — [Neuralized Multi-Wavelet Decomposition for Time Series Classification and Forecasting](http://arxiv.org/abs/2609.29317v1)
  <details><summary>📄 Abstract</summary>
  Time series analysis is fundamental in domains such as finance, healthcare, and meteorology. Real-world time series often exhibit multiscale characteristics shaped by diverse latent factors, resulting in intricate temporal patterns and rich frequency structures. However, existing approaches typically focus on either frequency-domain decomposition or time-domain pattern extraction in isolation, neglecting their joint structure. This decoupled modeling limits representation expressiveness and unde...
  </details>

- **2026-09-24** — Jordan Levy, Nicolas Verstaevel, Vincent Talon et al. — [Continuous Online Fault Detection for Mobile Robots via Adaptive Edge Models](http://arxiv.org/abs/2609.29194v1)
  <details><summary>📄 Abstract</summary>
  Mobile robots require robust, real-time fault detection capable of continuous adaptation on constrained edge hardware. While deep time-series models excel at unsupervised anomaly detection, their computational cost prohibits high-frequency onboard execution. This paper bridges this gap via a Teacher-Student distillation framework. An offline foundation model (TSPulse) generates pseudo-labels from unlabeled time series augmented with fault injections. A lightweight MiniRocket Student, adapted wit...
  </details>

- **2026-09-24** — Dibyayan Patra, Simit Raval, Pasindu Ranasinghe et al. — [An Automated Georeferencing Technique for Multi-Temporal Stope Point Clouds for Downstream Geotechnical Analysis](http://arxiv.org/abs/2609.29186v1)
  <details><summary>📄 Abstract</summary>
  The increasing use of UAV laser scanning in underground mines has enabled frequent acquisition of 3D point clouds from challenging environments such as stopes, generating large volumes of multi-temporal spatial data throughout successive excavation stages. However, in GNSS-denied underground environments, independently acquired stope point clouds are generated within local scanner reference frames and require registration and georeferencing before integration with mine reference data for downstr...
  </details>

- **2026-09-24** — Jiapeng Li — [Where Does Exactly-Once Live? Model, Harness, and Tool-Contract Effects on Duplicate Side Effects in LLM Agents](http://arxiv.org/abs/2609.29095v1)
  <details><summary>📄 Abstract</summary>
  When a tool-using agent's write times out or returns a server error, the action may already have taken effect. Retrying blindly duplicates it -- a second charge, a second announcement, a second deployment -- while giving up skips required work. We ask where exactly-once behaviour should be enforced: in the model, in the agent harness, or in the tool contract. We introduce LIMBO, a deterministic sandbox of six services with realistic contracts (optional idempotency keys, eventually consistent and...
  </details>

- **2026-09-24** — Siyuan Pang, Yepeng Yao, Zhengwei Jiang et al. — [DistillGuard: Malicious NPM Package Detection and API Attack Chain Analysis via Static Graph and LLM Distillation](http://arxiv.org/abs/2609.28996v1)
  <details><summary>📄 Abstract</summary>
  The Node.js ecosystem heavily relies on NPM packages, and software supply chain attacks targeting malicious NPM packages are rampant. Malicious code primarily triggers during package installation, import, and runtime. Traditional static analysis fails to understand code semantics; machine learning-based methods rely on feature extraction, which suffers from concept drift; existing LLM solutions suffer from high invocation costs, high data security risks, and poor performance. To overcome these l...
  </details>

- **2026-09-24** — Mengqi Wang, Mark A. Hasegawa-Johnson, Haolong Zheng et al. — [Learning New Words from Unlabeled Test Data in Automatic Speech Recognition](http://arxiv.org/abs/2609.28877v1)
  <details><summary>📄 Abstract</summary>
  New words are invented every day. A human listener can learn a new word by hearing it clearly once and inferring its usage from sentence context. This paper proposes granting ASR a similar ability to learn the contextual representations and spellings of new words from unlabeled test data at test time. A frozen CTC acoustic model provides spellings, a frozen language model provides contextual evidence for out-of-vocabulary (OOV) word detection, and an adaptation module expands the vocabulary by l...
  </details>

- **2026-09-23** — Avishai Weizman, Yehuda Ben-Shimol, Itshak Lapidot — [Spooftral: Can Voxtral Audio-Language Model Detect Speech Spoofing?](http://arxiv.org/abs/2609.28713v1)
  <details><summary>📄 Abstract</summary>
  Self-supervised learning (SSL) countermeasures (CMs) have shown strong performance in recent years. However, they often show degraded performance while facing unseen spoofing attacks and mismatched conditions. This study examines the Voxtral audio-language model (ALM) framework for spoofing detection, as a step toward combining CM capabilities within the ALM framework. We analyze how Voxtral captures spoofing cues through audio-text processing and propose an instruction-guided approach that uses...
  </details>

- **2026-09-23** — Michael Stettler, Benjamin Girardet, Jonas Canton et al. — [Progressive Skill Discovery as Access Control for Tool-Using LLM Agents: Structural Governance through Role-Scoped Capability Delivery](http://arxiv.org/abs/2609.28693v1)
  <details><summary>📄 Abstract</summary>
  Large Language Model (LLM) agents struggle to scale safely when exposed to vast enterprise toolsets. Providing an agent with access to every internal tool leads to oversized context windows, degraded tool selection, and severe governance vulnerabilities - as system policies defined purely in prompts remain probabilistic advice rather than hard constraints. Existing mitigations, such as multi-agent domain delegation, decentralize audit logs and fail to guarantee policy compliance across sessions....
  </details>

- **2026-09-23** — Jinqian Zhang, Haojun Xia, Shujiang Wu et al. — [Persistent Billable State: Denial-of-Wallet Attacks and Defenses in Tool-Calling LLM Agents](http://arxiv.org/abs/2609.28585v1)
  <details><summary>📄 Abstract</summary>
  Multi-step tool-calling LLM agents rely on host runtimes to preserve state across turns. When a runtime carries an external tool return into later model inputs, providers meter it again. An admitted malicious or compromised tool can thereby convert untrusted data into recurring victim-billed processing without victim credentials or local runtime privilege. We call retained content persistent billable state and formalize the host's decision over whether and how it enters later billable context as...
  </details>

- **2026-09-23** — Aman Anand, Partha Pratim Roy, Shivakumara Palaiahnakote — [MEVL-STP: Multi-Encoder and Vision Language Model for Arbitrarily Shaped Scene Text Spotting](http://arxiv.org/abs/2609.28857v1)
  <details><summary>📄 Abstract</summary>
  Scene text spotting remains challenging for arbitrarily shaped text instances such as curved signs and dense multi-oriented characters in natural images, where tightly coupled architectures propagate localization errors directly into recognition failures. We present a two-stage pipeline that combines multi-encoder segmentation with vision-language model recognition to address this problem. In the detection stage, six frozen vision encoders (CLIP, DINOv2, SigLIP, EVA-CLIP, SAM, and ConvNeXt) extr...
  </details>

- **2026-09-23** — Heyun Chen, Xiaohan Lan, Jiaxi Li et al. — [Pistis Technical Report](http://arxiv.org/abs/2609.28554v1)
  <details><summary>📄 Abstract</summary>
  We introduce the Pistis model family, comprising 27B- and 9B-parameter multimodal large language models built on Qwen3.6 and Qwen3.5, respectively, and developed through a general and scalable post-training framework. The framework first establishes a strong foundation through large-scale multimodal supervised fine-tuning (SFT). Building on this SFT foundation, we propose Interleaved Distillation and Reinforcement Learning (IDRL), a novel post-training paradigm that tightly integrates on-policy ...
  </details>

- **2026-09-23** — Jack B. Jedlicki, Tanguy Dieudonné, Heng Yang — [OCC4M: Object-Centric 4D Memory for Spatiotemporal Reasoning in Long-Horizon Manipulation](http://arxiv.org/abs/2609.28798v1)
  <details><summary>📄 Abstract</summary>
  Long-horizon manipulation often requires reasoning about state absent from the current view, such as a vanished object's location, temporal identity, or the contents of a shuffled container. We present OCC4M ("Occam"), an object-centric 4D memory that maintains persistent tracks in a shared world frame and explicitly represents temporal, motion, and containment relations. A vision-language model (VLM) queries this structured memory to select actionable targets for history-free low-level executio...
  </details>

- **2026-09-23** — Rameesha Zia, Muhammad Shahid Iqbal Malik — [An Explainable DistilBERT-BiLSTM-Attention Framework for Binary and Multi-Class Hate Speech Detection](http://arxiv.org/abs/2609.28703v1)
  <details><summary>📄 Abstract</summary>
  Hate speech on social media poses serious risks to social harmony, mental well-being, and public safety, making its timely and accurate detection essential for content moderation systems. Most existing studies focus on binary classification, evaluated their frameworks on a single dataset, and provide limited insight into how decisions are made, which limits their real-world applicability. In addition, limited work is done on the explainability of their predictive inference. To address these chal...
  </details>

- **2026-09-23** — Eranga Bandara, Xueping Liang, Asanga Gunaratna et al. — [BaseCamp --- An Agentic AI Framework for Automating DNA Sequencing Data Pipelines](http://arxiv.org/abs/2609.28557v1)
  <details><summary>📄 Abstract</summary>
  DNA sequencing pipelines, spanning quality control, alignment, variant calling, and annotation, are now reliably executed by workflow management systems that orchestrate established bioinformatics tools at scale. What remains manual is the decision layer surrounding that execution: selecting quality thresholds appropriate to a sample and platform, adjudicating borderline variant calls, diagnosing anomalies, and determining which findings warrant expert review. These decisions are repetitive, jud...
  </details>

- **2026-09-23** — Roy Ricaldi, Kristiyan Kyurkchiev, Irdin Pekaric — [A Bulletproof Business? Towards Detecting Infrastructure-as-a-Service Offerings on Telegram](http://arxiv.org/abs/2609.27428v2)
  <details><summary>📄 Abstract</summary>
  Cybercriminal operations increasingly depend on reusable digital infrastructure---including hosting, proxies, and virtual private networks (VPNs)---rented through Cybercrime-as-a-Service markets and advertised on platforms such as Telegram. We present a taxonomy for identifying Telegram messages advertising cybercriminal Infrastructure-as-a-Service (IaaS). The taxonomy comprises six service categories across compute, network, and communication infrastructure, together with three trust attributes...
  </details>

- **2026-09-23** — Giacomo Giuliari, Karl Wüst — [Physalia: Redistribution-Resistant Content Protection for Decentralized Storage](http://arxiv.org/abs/2609.28277v1)
  <details><summary>📄 Abstract</summary>
  In decentralized storage systems, access control is often implemented by encrypting the data before upload and sharing the decryption key with authorized parties. A leaked key, however, makes the data publicly accessible, which lowers the barrier to content piracy below that of traditional systems, where piracy requires redistributing the full data.   We present Physalia, an end-to-end access-control system for decentralized storage that secret-shares the data itself, instead of just the key, ac...
  </details>

- **2026-09-23** — Christopher Koch — [From Agent Output to Authorized Transition](http://arxiv.org/abs/2609.28216v1)
  <details><summary>📄 Abstract</summary>
  Agentic engineering systems can edit repositories, run tools and tests, build firmware, synthesize schematics, and prepare deployable or manufacturable artifacts. The assurance problem is therefore shifting from whether an agent can produce an output to whether an engineering lifecycle is justified in acting on claims about that output. Current products and standards provide sandboxes, approvals, hooks, traces, policy enforcement, attestations, bills of materials, and assurance representations, ...
  </details>

- **2026-09-23** — Muhammad Usama, Khair Un Nisa, Summer Yeoreum Jung — [Control-Token Injection Suppresses Chain-of-Thought and Defeats Reasoning-Based Oversight in Tool-Using Agents](http://arxiv.org/abs/2609.27542v1)
  <details><summary>📄 Abstract</summary>
  The safety of a tool-using language model agent is usually treated as a property of the model alone. We give controlled, full-precision evidence that it is instead a joint property of the model and the software that renders its chat template and parses its tool calls, the decoding harness, and that both halves are attackable from untrusted input. On the released gpt-oss-20b reasoning model under its published tool sandbox, appending a single string of the model's own channel-control tokens to a ...
  </details>

- **2026-09-23** — Jiapeng Sun, Yujin Zhou, Han Zhu et al. — [PASTABench: Proactive Assessment of Sequential Trajectories for Agent Safety](http://arxiv.org/abs/2609.28197v1)
  <details><summary>📄 Abstract</summary>
  As Large Language Models (LLMs) evolve into autonomous agents that alter real-world states, ensuring operational safety across multi-step workflows has become a critical challenge. While recent work has moved beyond single-turn evaluation toward multi-turn paradigms, key limitations persist: step-level methods treat actions in isolation, missing how risks accumulate, while trajectory-level evaluations operate post-hoc, offering no opportunity for timely intervention. To address these limitations...
  </details>

- **2026-09-23** — Bock-Zien Toh, Yuanchuan Ren, Tay Aw Yu et al. — [CasCVS-Net: A Staged Multi-Task Cascade for Critical View of Safety Assessment](http://arxiv.org/abs/2609.27681v1)
  <details><summary>📄 Abstract</summary>
  Automated assessment of the Critical View of Safety (CVS) in laparoscopic cholecystectomy requires both recognition of the three CVS criteria and anatomical grounding in small, rare, and often occluded hepatocystic structures. Learning-based methods differ in the anatomical information they use, from image-level classification to detection, segmentation, or graph-based reasoning, yet grounding the safety-critical anatomy remains the main bottleneck. We propose CasCVS-Net, a staged multi-task cas...
  </details>

- **2026-09-23** — Zeyu Wang, Xiaodan Li, Zhiwen Li et al. — [InGuard: Towards Generalized Inner Guardrail for Safe Text-to-Image Generation](http://arxiv.org/abs/2609.27620v1)
  <details><summary>📄 Abstract</summary>
  Modern text-to-image (T2I) models generate high-quality images from arbitrary user prompts, yet they can just as easily produce not-safe-for-work (NSFW) content. Conventional outer guardrails consist of two components: a prompt classifier that checks for risk before generation, and a post-hoc image classifier that checks the fully generated image. In this design, both classifiers operate outside the generation pipeline and do not use the model's own representations. This separation can limit pro...
  </details>

- **2026-09-23** — Roy Ricaldi, Kristiyan Kyurkchiev, Irdin Pekaric — [A Bulletproof Business? Towards Detecting Infrastructure-as-a-Service Offerings on Telegram](http://arxiv.org/abs/2609.27428v1)
  <details><summary>📄 Abstract</summary>
  Cybercriminal operations increasingly depend on reusable digital infrastructure---including hosting, proxies, and virtual private networks (VPNs)---rented through Cybercrime-as-a-Service markets and advertised on platforms such as Telegram. We present a taxonomy for identifying Telegram messages advertising cybercriminal Infrastructure-as-a-Service (IaaS). The taxonomy comprises six service categories across compute, network, and communication infrastructure, together with three trust attributes...
  </details>

- **2026-09-23** — Thomas Ratsakatika, Mihai Zotta, Srinivasan Keshav et al. — [Geospatial embeddings detect old-growth forests but buffered spatial validation narrows their advantage over Sentinel features](http://arxiv.org/abs/2609.28194v1)
  <details><summary>📄 Abstract</summary>
  Old-growth forests develop over centuries under minimal anthropogenic disturbance, producing structurally complex and biodiverse stands. In Europe, protecting them requires mapping that is accurate for individual forest parcels yet deployable continent-wide. Geospatial foundation model (GFM) embeddings enable label-scarce land classification, but their value for old-growth detection remains unknown. Here, we map old-growth forests across 211,893 ha of Romania's Southern Carpathians, a beech-spru...
  </details>

- **2026-09-23** — Matthieu Dubois, Pablo Piantanida, François Yvon — [How Much Were You Told? Measuring External Information in Peer Reviews](http://arxiv.org/abs/2609.28041v1)
  <details><summary>📄 Abstract</summary>
  Conference policies distinguish using Large Language Models (LLMs) to polish one's own review from delegating the critique, but current Artificial Text Detection (ATD) methods largely measure surface form rather than the origin of its content. We instead measure the external information carried by a review: information not explained by the reviewed paper and a generic reviewing instruction. We propose Self-Conditioning, an unsupervised information-theoretic estimator that compares the likelihood...
  </details>

- **2026-09-23** — Yongjun Jeong, Hanbum Ko, Ye Rin Kim et al. — [MolDesignBench: Evaluating LLM-based Agent for Scenario-grounded Molecular Design](http://arxiv.org/abs/2609.27349v1)
  <details><summary>📄 Abstract</summary>
  Real-world molecular design remains challenging for large language model (LLM)-based agents. It requires them to interpret design contexts, satisfy multiple constraints, identify infeasible specifications, and reason over multi-step tool outputs. Existing benchmarks do not capture this complexity, focusing instead on explicit and narrow constraints, only feasible problems, and single-path solutions. To address this gap, we propose MolDesignBench, a scenario-grounded benchmark that more closely r...
  </details>

- **2026-09-22** — Armin Maleki, Hayder Radha — [PEARL: A Lightweight Prompt-based Feature Interpreter Framework for Real-Time, Anonymous, and Heterogeneous Collaborative Perception](http://arxiv.org/abs/2609.27123v1)
  <details><summary>📄 Abstract</summary>
  Heterogeneity across Collaborative Perception (CP) agents is a major challenge for emerging CP frameworks due to domain gaps from differing sensors, architectures, and training data. Prior works mitigate this challenge by aligning features in a unified space via model retraining or per-agent-type interpreters. These strategies (a) require access to neighbor configurations, (b) do not fully address real-time CP deployment, and (c) generalize poorly to unseen agents joining at run time. To overcom...
  </details>

- **2026-09-22** — Yi Xu, Ehsan K. Ardestani, Wenyin Fu et al. — [Crossflow: Prefill-Decode Elasticity for Agentic LLM Serving](http://arxiv.org/abs/2609.27085v1)
  <details><summary>📄 Abstract</summary>
  As serving capacity demand surpasses that of training, serving efficiency becomes increasingly important. Prefill-decode (P/D) disaggregation improves serving efficiency through specialization and isolation of the two phases. These benefits rest on a static partitioning. Phase demand, however, is not static. We observe that in a large LLM fleet the ratio of uncached input to output tokens has peak-to-mean ratios up to 4.7x at minute timescales, and that in a public agentic trace the hourly ratio...
  </details>

- **2026-09-22** — Sujay Uday Rittikar, Sheela Ramanna — [LexLattice: Multilingual Extractive Summarization via Neural Cellular Automata on Document Hierarchies](http://arxiv.org/abs/2609.27032v1)
  <details><summary>📄 Abstract</summary>
  Faithfulness is a central concern in legal text summarization, which motivates extractive approaches that select verbatim content traceable to its source. Such methods typically rank paragraphs or other structural units in isolation, yet give little attention to consolidating evidence that is distributed across, and shares salience between, distant parts of a document. We introduce LexLattice, an extractive summarizer that reifies a legal act's hierarchy as a two-dimensional semantic lattice and...
  </details>

- **2026-09-22** — Mostafa Anouar Ghorab, Ahmad Abdel Latif, Mohamed Aymen Saied — [Kubernetes Misconfigurations in the Wild: Taxonomy, Evolution, and Automated Repair with Large Language Models](http://arxiv.org/abs/2609.27030v1)
  <details><summary>📄 Abstract</summary>
  Kubernetes is widely used to orchestrate cloud-native applications, yet its declarative configuration model often introduces security misconfigurations that threaten system reliability. Despite available detection tools, misconfiguration patterns and scalable remediation remain insufficiently understood.   This paper presents an empirical study of Kubernetes security misconfigurations based on 2,662 developer-reported Stack Overflow issues. We derive a taxonomy of recurring security weaknesses a...
  </details>

- **2026-09-22** — Constantin Ulrich Harsy, Tassilo Wald, Karol Gotkowski et al. — [nnFoundation: 3D Foundation Models for Radiology](http://arxiv.org/abs/2609.26924v1)
  <details><summary>📄 Abstract</summary>
  Radiological artificial intelligence has advanced rapidly, yet most systems remain narrowly task-specific, data-intensive, and fragile under domain shift. Foundation models promise more transferable and data-efficient solutions, but existing approaches are limited in scale, evaluated narrowly, and often assume that a single pretrained model can support diverse downstream tasks. Here we present nnFoundation, complementary convolutional and transformer-based 3D radiological foundation models. Deve...
  </details>

- **2026-09-22** — Abel A. Reyes-Angulo, Henry O. Velesaca, Steven Araujo — [SambaGraph: Action-Reaction Spatio-Temporal Graphs for Soccer Tactical Response Modeling](http://arxiv.org/abs/2609.25569v1)
  <details><summary>📄 Abstract</summary>
  Soccer tactics are interactive: an attacking action changes the opponent's defensive problem, and the observed response depends on the multi-agent match state. We introduce SambaGraph, an action--reaction spatio-temporal graph dataset and benchmark for soccer tactical response modeling. From tracking and event data for all 64 matches of the 2022 FIFA World Cup, we curate 4,070 action-centered episodes represented as temporally aligned 23-node player--ball graph sequences with attack/defense view...
  </details>

- **2026-09-22** — Quan Nguyen-Tri, Mukul Ranjan, Zhiqiang Shen — [Flash-dLLM: IO-Aware KV Caching and Parallel Decoding for Fast, Memory-Efficient Diffusion LLMs](http://arxiv.org/abs/2609.26796v1)
  <details><summary>📄 Abstract</summary>
  Diffusion Large Language Models (dLLMs) have recently emerged as a promising alternative to autoregressive LLMs by enabling non-autoregressive text generation. However, their practical deployment remains limited by inefficient inference, largely due to the absence of effective Key-Value (KV) caching and scalable parallel decoding mechanisms. Existing acceleration methods typically study KV caching and parallel decoding in isolation, overlooking the I/O bottlenecks that arise when cache reuse and...
  </details>

- **2026-09-22** — Linman Wang, ZiFei Zhang, Chunran Zheng et al. — [DIFTA-3D: Depth-Consistent Instance-Level Feature Transfer and Adaptation of DINOv3 for 3D Detection](http://arxiv.org/abs/2609.26702v1)
  <details><summary>📄 Abstract</summary>
  RGB-D 3D instance detectors benefit from visual semantics, but the task-specific Faster R-CNN/ResNet branch used by IIFNet3D couples feature extraction to a separately trained 2D detector and its image-domain labels. Replacing that branch with a frozen vision foundation model removes this task-specific dependency, but may introduce occlusion noise and a mismatch between patch features and geometry-aware detection features. In this work, we investigate this replacement through an adaptation of DI...
  </details>

- **2026-09-22** — Nathalie Baracaldo — [From Alignment to Access Control: A Framework for GenAI Policy Enforcement](http://arxiv.org/abs/2609.26682v1)
  <details><summary>📄 Abstract</summary>
  Generative AI (GenAI) applications have flourished enabling users to chat with large language models, and to create agents to act on their behalf for a variety of tasks. The pace of development of capabilities in this field is incredibly fast with security and safety taking a back seat. Unfortunately, the slower pace at which security and safety mechanisms have evolved has led to real incidents. Policy enables the definition of desirable behavior of applications, and for that reason, it is a cor...
  </details>

- **2026-09-22** — Hoang-Lam Huynh, Quoc-Cuong Tang, Van-Tri Phan et al. — [Design and Evaluation of a Controlled Post-Alert Incident Orchestration and Response Subsystem Using a Rule Engine and a Local Large Language Model](http://arxiv.org/abs/2609.26316v1)
  <details><summary>📄 Abstract</summary>
  This paper presents a controlled post-alert incident orchestration and response subsystem for educational information systems. The architecture separates deterministic classification, contextual analysis, human approval, and technical execution. A Rule Engine determines severity and selects the playbook, while Static RAG and a local large language model provide advisory content under Validator, Guardrail, Output Sanitizer, and Safe Fallback controls. Experiments begin after simulated alerts are ...
  </details>

- **2026-09-22** — Elie Abboud, Oren Gal — [MATES: Learning Multi-Agent Interactions by Transforming Observations for Frozen Single-Agent Policies](http://arxiv.org/abs/2609.26010v1)
  <details><summary>📄 Abstract</summary>
  Multi-agent reinforcement learning (MARL) commonly trains decentralized policies from scratch, requiring agents to acquire individual task competence and coordination simultaneously. Yet many multi-agent problems admit a compatible single-agent counterpart in which the underlying task can be learned in isolation. We introduce Multi-Agent Observation Transformation for Existing Single-Agent Policies (MATES), an input-side adaptation framework for tasks whose multi-agent observations preserve the ...
  </details>

- **2026-09-22** — Baher Mohammad, Ammar Ali, Stamatios Lefkimmiatis — [GeoPair: Geometry-Preserving Cross-Layer Factorization for Training-Free Transformer Compression](http://arxiv.org/abs/2609.25963v1)
  <details><summary>📄 Abstract</summary>
  Transformer architectures exhibit cross-layer redundancies, yet post-training compression pipelines typically optimize layers in isolation or rely on heuristic grouping strategies that disregard layer-specific activation geometries. We introduce a principled, training-free framework that sequentially optimizes cross-layer weight pairings and shared-dictionary factorizations. Rather than forcing weights of adjacent layers to share a basis or heuristically merging activation statistics, our approa...
  </details>

- **2026-09-22** — Malsha Ashani Mahawatta Dona, Konstantinos Rokanas, Alexander Säfström et al. — [Towards Systematic Qualification of Vision-Language Models for Automotive Perception Systems](http://arxiv.org/abs/2609.25945v1)
  <details><summary>📄 Abstract</summary>
  The field of Artificial Intelligence has been adopted for many application domains. Vision Language Models are one of the recently advanced AI techniques that have been explored to support automotive features such as vehicle perception, and safety assurance. However, such language models are prone to hallucinations, posing a potential threat to the safety of automotive systems that may incorporate them. Within the automotive domain, VLMs could not only hallucinate traffic objects, but could also...
  </details>

- **2026-09-22** — Weijie Zhou, Zhaoyang Zhang, Zhixian Kong et al. — [MIMO-OFDM AI Receiver Based on Incrementally Conditioned Diffusion with Soft Decision](http://arxiv.org/abs/2609.25923v1)
  <details><summary>📄 Abstract</summary>
  Conventional iterative receiver usually begins with channel estimation using sparse pilot observations and follows with data detection based on the channel estimates, and then updates channel estimation using decision feedback, and so on. In Artificial Intelligence (AI)-based receiver design, it is also crucial to make use of such progressively enriched data observations to enhance the generative channel estimation. However, the statistical characteristics and reliability of the data decisions a...
  </details>

- **2026-09-22** — Massimiliano Sassoli de Bianchi, Roberto Leporini — [Reply to comments arXiv:2512.07881 and arXiv:2601.06104 on quantum structure in human and AI-generated language](http://arxiv.org/abs/2609.25797v1)
  <details><summary>📄 Abstract</summary>
  We reply to the comments by M. Sienicki and K. Sienicki (arXiv:2512.07881) and by K. Sienicki (arXiv:2601.06104) on our work on quantum-mechanical statistics in human language (arXiv:2407.14924) and on quantum structure in AI-generated language (arXiv:2511.21731). We thank the authors for their careful reading and address what we consider to be the main points of criticism: the exploratory nature of the protocol used in the experiments with large language models; the role of marginal-law violati...
  </details>

- **2026-09-22** — Zheng Chen, ZhiCheng Du, Haoxuan Li et al. — [Syndrome, Synergy, and Safety: Structured Reasoning and Knowledge-Driven Alignment for TCM Prescription Generation](http://arxiv.org/abs/2609.25755v1)
  <details><summary>📄 Abstract</summary>
  Applying large language models to Traditional Chinese Medicine (TCM) prescription generation reveals three clinically critical gaps: models produce end-to-end mappings without auditable reasoning following the li-fa-fang-yao paradigm (SR Gap), treat each encounter in isolation without follow-up adjustment via sui zheng jia jian (LA Gap), and fail to enforce absolute contraindication rules such as Shi Ba Fan (SC Gap). We propose a progressive four-stage framework (SFT $\to$ PG-CoT $\to$ Dynamic $...
  </details>


### 📂 alignment
*对齐与安全约束 / Alignment & Safety Constraints* — 45 papers

- **2026-09-24** — Wenhao Li, Zhibin Wu, Chong Xiao et al. — [SemMSA: Latent Semantic-Aided Robust Multimodal Sentiment Analysis with Incomplete Data](http://arxiv.org/abs/2609.30238v1)
  <details><summary>📄 Abstract</summary>
  Recent research on Multimodal Sentiment Analysis (MSA) has focused on learning from language, visual, and acoustic modalities with incomplete data to infer human sentiment. Most studies typically compensate for missing information by reconstructing modality features or designing complicated fusion mechanisms. However, these methods still suffer from spurious generation and noisy guidance due to the lack of high-level semantic grounding in partially observed multimodal evidence. To address these ...
  </details>

- **2026-09-24** — Kimia Hamidieh, Giannis Daras, Antonio Torralba — [PoEM: Predicting RL Outcomes from Existing Policies](http://arxiv.org/abs/2609.30226v1)
  <details><summary>📄 Abstract</summary>
  Foundation models are post-trained with reinforcement learning (RL) to maximize specific rewards, such as human alignment, correctness, or instruction following. This post-training process is computationally intensive, sometimes unstable, and has to be run from scratch every time the reward model changes or when we want to combine multiple rewards. We hence ask: given a new reward function, is it possible to predict the RL outcomes without actually running RL on it? We answer this in the affirma...
  </details>

- **2026-09-24** — Nhat-Nam Nguyen, Pierre-Andre Vuissoz, Yves Laprie — [Anatomy-aware cross-speaker adaptation of complete vocal-tract acoustic-to-articulatory inversion](http://arxiv.org/abs/2609.29766v1)
  <details><summary>📄 Abstract</summary>
  Cross-speaker acoustic-to-articulatory inversion requires accounting for anatomical differences between speakers. We propose a geometric adaptation framework that uses anatomical landmarks, primarily on vertebrae and dental structures,to transfer predictions from a fixed inversion model to unseen speakers. An affine transformation followed by thin-plate spline (TPS) deformation maps the predicted contours of 10 vocal-tract structures into each target speaker's geometry without retraining. Landma...
  </details>

- **2026-09-24** — Zhanglin Wu, Hengchao Shang, Daimeng Wei et al. — [Tag-Aware Structured Text Translation: Towards a Systematic Understanding](http://arxiv.org/abs/2609.29131v1)
  <details><summary>📄 Abstract</summary>
  Internet texts are replete with format tags that carry structural, semantic, and functional meaning. Current large language model (LLM)-based translation systems struggle to balance translation fluency with tag fidelity when processing tagged text. We argue that resolving this tension requires a systematic approach at three interconnected levels: data synthesis, capability building, and multi-objective alignment. At the data level, we identify and formalize a fundamental trade-off between struct...
  </details>

- **2026-09-24** — Zeyu Michael Li, William Xingxu Chen, Bingshuo Qian et al. — [ELF-REG: Scaling Continuous Diffusion Language Models to Reasoning Tasks](http://arxiv.org/abs/2609.29102v1)
  <details><summary>📄 Abstract</summary>
  Fully continuous diffusion language models (dLMs) denoise continuous representations without intermediate discretization, then decode all response tokens in parallel at the final step. Their performance on challenging reasoning tasks remains less established than that of autoregressive (AR) LLMs and masked dLMs. We scale Embedded Language Flows (ELF) to mathematical reasoning and code generation on GSM8K, MATH-500, HumanEval, and MBPP. We introduce ELF-REG, which improves learning with represent...
  </details>

- **2026-09-24** — Minkyoung Kim, Hyunjung Byun, Yohan Lee et al. — [Downside-Controlled Online Forecast Combination under Delayed and Revised Outcomes](http://arxiv.org/abs/2609.29096v1)
  <details><summary>📄 Abstract</summary>
  Post-hoc correction adjusts a forecaster that cannot be retrained, such as a foundation model, but a correction fitted where errors are stable can hurt where they shift. We aim for downside control: not much worse than the starting forecast. We combine the frozen forecaster, a static corrector and an online corrector on the simplex, using only losses that mature after the horizon. Across seven benchmarks and four base models, two of them foundation models, the worst deterioration over 28 pairs a...
  </details>

- **2026-09-24** — Rong Wang, Kun Sun, Yadong Guo — [Polite but Misaligned: Evaluating LLM Politeness Judgments Against Human Pragmatic Norms](http://arxiv.org/abs/2609.29001v1)
  <details><summary>📄 Abstract</summary>
  Despite strong performance on standard benchmarks, it remains unclear whether large language models (LLMs) evaluate social pragmatics in ways that align with human judgments. We evaluate LLM politeness judgments using two English-language datasets with complementary annotation formats: continuous human ratings and three-way categorical labels. Across the seven evaluated models, we find that inter-model agreement is stronger than model--human agreement. Strategy-level analyses suggest that model-...
  </details>

- **2026-09-24** — Hanze Guo, Aixuan Song, Jing Yao et al. — [From Static Personal Values to Contextualized Personalization: Bayesian Personalized Value Alignment for LLMs](http://arxiv.org/abs/2609.28942v1)
  <details><summary>📄 Abstract</summary>
  Personalized value alignment has become increasingly important as large language models (LLMs) are expected to accommodate diverse user preferences. However, existing methods typically align model outputs with a static value profile across prompts, overlooking that the salience of value dimensions varies substantially across contexts. Inspired by Lewin's Field Theory, which views human behavior as jointly shaped by personal dispositions and situational constraints, we model personal values as pr...
  </details>

- **2026-09-24** — Hong-Han Wang, Yuntao Wang, Hu Ding — [The Alignment Illusion in Multimodal Large Language Models](http://arxiv.org/abs/2609.30210v1)
  <details><summary>📄 Abstract</summary>
  Layer-wise visual-text similarity in Multimodal Large Language Models (MLLMs) is widely interpreted as evidence that the language model progressively integrates visual content into a shared representation space. This reading rests on the assumption that scalar alignment scores reflect content-level cross-modal interaction. To test this assumption, we apply controlled interventions to the visual stream. Across 13 MLLMs from five families spanning 0.5B to 72B parameters, replacing projector-output...
  </details>

- **2026-09-24** — Zhiyu Xu, Weilong Yan, Yufei Shi et al. — [AV-GRPO: Modality-Anchored Decoupling Diffusion Reinforcement Learning for Joint Audio-Video Generation](http://arxiv.org/abs/2609.29816v1)
  <details><summary>📄 Abstract</summary>
  Recent years have witnessed major progress in joint audio-video generation. Existing models still suffer from limited per-modality fidelity, insufficient text-modality alignment and weak cross-modal synchronization. While reinforcement-learning post-training offers a promising remedy, directly adapting it to joint audio-video generation is challenging. Heterogeneous multimodal rewards entangle learning signals and complicate credit assignment. Joint optimization of two modality towers is computa...
  </details>

- **2026-09-24** — Dan Halperin, Mirko Mählisch — [FounRef: Robust, Structure-Preserving, and Fast Metric Refinement of Frozen Monocular Foundation Priors with Sparse Anchors](http://arxiv.org/abs/2609.29224v1)
  <details><summary>📄 Abstract</summary>
  Dense metric depth from cameras is essential to real-world 3D applications, yet achieving accuracy, faithful surface geometry, and fast inference simultaneously remains challenging. Monocular foundation models provide rich, transferable geometric priors but lack reliable metric scale, while depth-completion networks recover metric depth at the cost of geometric fidelity, cross-domain robustness, or speed. We present FounRef, a training-free method that aligns a frozen monocular foundation prior ...
  </details>

- **2026-09-24** — Ruining Zhao, Ho Kei Cheng, Alexander G Schwing — [MoVISA: Multi-Token Reasoning for Video Object Segmentation](http://arxiv.org/abs/2609.28956v1)
  <details><summary>📄 Abstract</summary>
  Recent advances in video object segmentation with Multimodal Large Language Model (MLLM) reasoning have demonstrated the effectiveness of using a single textual token, such as SEG, to predict segmentation masks across images and videos. However, we observe that this single-token strategy lacks the granularity required to precisely localize multiple objects across time in video segmentation tasks. To address this limitation, we develop Multi-Token Reasoning for Video Object Segmentation, or MoVIS...
  </details>

- **2026-09-23** — Xin-Yu Hu, Shuang Liang, Cheng Feng et al. — [SGA: Uncertainty Quantification for Multi-Step Forecasting in Time Series Foundation Models](http://arxiv.org/abs/2609.28582v1)
  <details><summary>📄 Abstract</summary>
  The recent emergence of Time Series Foundation Models (TSFMs) has significantly advanced multi-step forecasting performance, enabling accurate predictions over extended future horizons. However, existing TSFMs often suffer from significantly inherent uncertainty, which typically manifests as derived forecast branches emerging at each time step and spreading to subsequent steps; different forecast branches often exhibit varying forecasting performance, thereby undermining the credibility of TSFM ...
  </details>

- **2026-09-23** — Saeedeh Lohrasbi, Mohammad Mamun, Ahmed Yehia et al. — [Where Cyber Agents Struggle: Bottleneck Analysis of Multi-Stage LLM Agents](http://arxiv.org/abs/2609.28572v1)
  <details><summary>📄 Abstract</summary>
  Multi-stage LLM-based cyber agents may complete attack workflows while remaining brittle, costly, or reliant on incorrect interpretations of execution evidence. Success rates alone obscure inefficiency, adaptation through retries, and recognition of success or failure. We present an end-to-end diagnostic study of an Autonomous Adversary system with orchestrator, executor, and validator LLMs in enterprise-like lateral-movement scenarios. Six frontier models are evaluated across two scenarios and ...
  </details>

- **2026-09-23** — Tiviatis Sim, Jia Hui Woon, Xinming Gao et al. — [PAWS: Policy-driven Agentic World Simulation](http://arxiv.org/abs/2609.28547v1)
  <details><summary>📄 Abstract</summary>
  Policy interventions propagate through public communication, institutional decisions, and stakeholder responses, yet datasets for financial multi-agent simulation rarely connect these processes to temporally aligned historical evidence. We introduce PAWS, a Policy-driven Agentic World Simulation dataset covering 36 verified U.S. financial and economic policy episodes, 12,727 policy-linked news records, and 65,291 source-grounded stakeholder actions. Each action is linked to its supporting news a...
  </details>

- **2026-09-23** — Kaiyang Li, Shaobo Han, Yue Tian et al. — [Mizar: A 159M-Parameter Audio-Language Model for Audio Understanding](http://arxiv.org/abs/2609.28344v1)
  <details><summary>📄 Abstract</summary>
  Audio-language models (ALMs) integrate acoustic perception with the knowledge encoded in language models, enabling contextual understanding of auditory events. Making these capabilities practical on devices with limited memory and computation motivates our focus on small ALMs with fewer than 200M parameters. We introduce a recipe that brings together architecture, data, and three-stage training to build Mizar, a 159.3M-parameter ALM. Its architecture connects a compact CED-Small audio encoder to...
  </details>

- **2026-09-23** — AbdulRahman A. Morsy, Aya Zirikly — [Beyond Poetry: Can Large Language Models Generate Classical Arabic Maqamat?](http://arxiv.org/abs/2609.28245v1)
  <details><summary>📄 Abstract</summary>
  Large language models (LLMs) have shown strong performance in creative text generation, yet their ability to produce culturally grounded and stylistically constrained literary forms remains underexplored. Prior work has focused largely on modern language varieties and poetry, while classical prose traditions such as maqama remain largely unstudied. The maqama is a classical literary genre characterized by rhymed prose (saj), dense rhetorical ornamentation, and episodic narrative structure, makin...
  </details>

- **2026-09-23** — Xueqi Qiu, Xingyu Miao, Jingjing Deng et al. — [From Alignment to Fusion in 3D Vision-Language](http://arxiv.org/abs/2609.28222v1)
  <details><summary>📄 Abstract</summary>
  Unified 3D vision-language systems must combine complementary geometry, scale, and appearance cues while supporting tasks from instance segmentation to language-guided reasoning. Existing methods often process point clouds, voxel grids, and multi-view images independently; directly combining these heterogeneous representations may leave substantial feature discrepancy unresolved, while subsequent unconstrained adaptation may distort their internal geometry. We propose an align-then-fuse framewor...
  </details>

- **2026-09-23** — Basavaraj Sunagad, Artur Jesslen, Adam Kortylewski — [Two Global Crops Suffice: Locating Semantic Emergence in DINO-Style Self-Supervised Learning](http://arxiv.org/abs/2609.28187v1)
  <details><summary>📄 Abstract</summary>
  Self-supervised vision transformers trained with DINO-style objectives exhibit striking emergent semantic representation quality across visual tasks, yet the mechanisms underlying this behavior remain unclear. We present a systematic empirical dissection of the DINO family and show that semantic representations arise primarily from enforcing consistency between geometrically distinct global views of the same image instance. This instance-specific global alignment acts as the semantic anchor of D...
  </details>

- **2026-09-23** — Shuai Dong, Yongfu Zhu, Yuqi Xu et al. — [RL Starts before RL: On Policy Distillation for Better Reinforcement Learning](http://arxiv.org/abs/2609.28145v1)
  <details><summary>📄 Abstract</summary>
  Reinforcement learning (RL) improves reasoning, but its performance depends on the policy from which training begins. We study on-policy distillation (OPD) as a preparation stage for RL and ask whether its benefits extend beyond improvements in the distilled model's initial accuracy. Under shared RL settings, students initialized with OPD reach higher final performance than those trained with direct RL or supervised fine-tuning followed by RL. This advantage can emerge even when OPD produces lit...
  </details>

- **2026-09-23** — Fuqiang Zhao, Qian Liu — [DEAL-Grasp: Decoupled Alignment Representation for Geometry-Aware Dexterous Grasp Generation](http://arxiv.org/abs/2609.28131v1)
  <details><summary>📄 Abstract</summary>
  Synthesizing realistic articulated hand-object interactions is a fundamental problem in virtual reality, embodied intelligence, and digital human applications. Existing methods for dexterous grasp synthesis typically regress or denoise poses in a joint space that couples global rigid motion with local articulation, which often yields unstable samples and physically implausible contacts. We introduce DEAL-Grasp, built upon the Decoupled Alignment (DEAL) representation, which reformulates grasp sy...
  </details>

- **2026-09-23** — Paweł Mąka, Yusuf Can Semerci, Jan Scholtes et al. — [Scaling Attention Head Analysis via Gradient-Based Attribution in Context-Aware Machine Translation](http://arxiv.org/abs/2609.28117v1)
  <details><summary>📄 Abstract</summary>
  In this paper, we introduce a gradient-based head attribution strategy where the Token-level Max-Margin loss is backpropagated to the attention maps. This framework enables a large-scale causal analysis of attention heads, making it suitable for LLMs. We evaluate our method on the task of disambiguation in Context-aware Machine Translation, where we analyze 50 phenomena across 4 models and 4 language directions. We empirically show the alignment of our method with the effects of increasing the a...
  </details>

- **2026-09-23** — Norah Almousa, Shayan Peyghambari Oskoui, Raquel Coelho et al. — [Evaluating Feedback Focus and Pedagogical Adaptivity in LLM-Generated Feedback on Student Writing](http://arxiv.org/abs/2609.28026v1)
  <details><summary>📄 Abstract</summary>
  We investigate whether state-of-the-art large language models (LLMs) generate feedback that reflects the pedagogical practices of expert teachers in terms of feedback focus and adaptivity. Previous evaluation efforts have examined feedback characteristics, its impact on learning, and its target, yet the focus of feedback and its adaptivity remains largely overlooked. To bridge this gap, we adopt and refine Narciss's taxonomy into seven feedback focus types to annotate teacher and LLM-generated f...
  </details>

- **2026-09-23** — Anh-Tien Nguyen, Trung DQ. Dang, Nghiem Tuong Diep et al. — [FFM-CP: Cross-Backbone Fusion of Vision-Language Foundation Models for Few-Shot Computational Pathology](http://arxiv.org/abs/2609.27710v1)
  <details><summary>📄 Abstract</summary>
  Pathology vision-language foundation models vary in performance across diseases and tasks, with no single model consistently performing best. The high cost of expert pathology annotation can also limit the labeled data available for task-specific adaptation. Combining complementary pretrained representations is a potential approach to these limitations, yet learning an effective fusion from few labeled examples remains challenging. We introduce Few-shot Fusion Foundation Models of Computational ...
  </details>

- **2026-09-23** — Renata Barreto, Markelle Roesti, Mohammad Tahaei — [Alignment Inertia: Auditing the Durability of Training Data Influence Through Policy Override Resistance](http://arxiv.org/abs/2609.27333v1)
  <details><summary>📄 Abstract</summary>
  Platform operators increasingly rely on system prompts and fine-tuning to govern model behavior, yet it remains unclear how reliably these interventions override behavior inherited from prior training. We propose Override Success Rate (OSR) and alignment inertia to measure when operator interventions succeed or fail to change prior behavior. We evaluate zero-shot prompting and LoRA fine-tuning across Llama and Mistral in medical misinformation and hate speech. Alignment inertia persists across b...
  </details>

- **2026-09-23** — Junwon You, Mihyun Jang, Sangwoo Mo et al. — [What Converges in the Platonic Representation Hypothesis? Structure over Geometry](http://arxiv.org/abs/2609.27252v1)
  <details><summary>📄 Abstract</summary>
  The Platonic Representation Hypothesis suggests that increasingly capable models converge toward shared representations. Recent work narrows this claim to shared local neighborhood relationships, finding that capacity-dependent trends in several global similarity measures largely disappear after calibration. We challenge this interpretation by showing that prior local-global comparisons confound structural scale (local versus global) with what is compared: relational structure, defined by which ...
  </details>

- **2026-09-23** — Henan Sun, Zehua Li, Haitao Hu et al. — [DCRL: Decoupling and Coupling Reinforcement Learning via Policy-Reward Manifold Alignment](http://arxiv.org/abs/2609.27572v1)
  <details><summary>📄 Abstract</summary>
  Reinforcement learning (RL) has emerged as a key paradigm for improving the reasoning capabilities of large language models (LLMs). However, existing reward systems, such as rule-based and reward-model-based, often exhibit issues such as unstable optimization and reward hacking. In this work, we revisit the general reasoning of LLMs from a geometric perspective, conceptualizing it as a coupled manifold composed of three interdependent sub-manifolds: logical deduction, evaluation, and representat...
  </details>

- **2026-09-23** — Jie Yang, Yan Zheng, Jiarui Sun et al. — [TimeEvo: Failure-Driven Self-Evolution of a Time Series Agent](http://arxiv.org/abs/2609.27277v1)
  <details><summary>📄 Abstract</summary>
  Time series agents answer analytical questions by calling external tools, and which tools they carry is decided by people before the agent runs. However, we identify two failures in this setup. Human-Agent Tool Misalignment: a library of 21 expert-curated tools helps on some tasks and hurts on others, dropping anomaly accuracy under every backbone we test. Silent Harm: one round of generic self-revision changes 147 answers and breaks 56 of them, while the final score moves by less than a point. ...
  </details>

- **2026-09-22** — Yukta Pareek, Yasaman Masoudi, Satadru Dey — [Merging Large Language Models and Battery Physics for User-Aware Electric Vehicle Driving Management](http://arxiv.org/abs/2609.27050v1)
  <details><summary>📄 Abstract</summary>
  Electric vehicle (EV) battery performance is strongly coupled with driver behavior, yet human intent is typically expressed semantically rather than numerically. This paper proposes a hybrid physics-artificial intelligence framework that integrates a Large Language Model (LLM) as a high-level behavioral reasoning layer within a physics-driven supervisory architecture. The LLM interprets textual user intent and structured battery feedback to generate bounded behavioral parameters that shape a dis...
  </details>

- **2026-09-22** — Ruike Cao, Fugen Yao, Liang Dong et al. — [COPE: Continual Personalization of LLMs under Sparse User Feedback via User Embeddings and Self-Evaluation](http://arxiv.org/abs/2609.26853v1)
  <details><summary>📄 Abstract</summary>
  While Large Language Models (LLMs) have achieved remarkable results across various benchmarks, their alignment with normative values often results in homogenized responses that fail to address diverse user preferences. Existing training-free methods often occupy valuable context windows through prompt engineering, while training-based methods typically remain static post-training, failing to support the continual optimization required in real-world settings. To address these challenges, we propo...
  </details>

- **2026-09-22** — Han Chen, Hanchen Wang, Hongmei Chen et al. — [HYDRA: Proactive Android Malware Drift Adaptation via Hierarchical Graph Contrastive Learning](http://arxiv.org/abs/2609.26352v1)
  <details><summary>📄 Abstract</summary>
  Concept drift, driven by the rapid evolution of Android malware, severely degrades the performance of machine learning detectors. Current adaptation strategies are often reactive, responding only after performance has dropped and imposing a significant manual annotation burden, or they are proactive but rely on unstable adversarial training and incomplete, single-level graph representations. To overcome these limitations, we propose HYDRA (Hybrid Drift Adaptation), a proactive adaptation framewo...
  </details>

- **2026-09-22** — Shufan Sun, Chen Wang, Enxin Song et al. — [HARMONY: Hierarchical Agentic Reasoning for MONocular Image-to-Scene Synthesis](http://arxiv.org/abs/2609.26793v1)
  <details><summary>📄 Abstract</summary>
  Compositional 3D scene reconstruction has recently been explored from two directions: agentic reasoning that provides semantic understanding of spatial relationships but lacks precise alignment with input images; and visual geometry foundation models that predict dense point maps from input images but the reconstruction quality is limited. Therefore, recovering a complete 3D scene from a single monocular image with accurate inter-object relationships and high-fidelity reconstruction quality rema...
  </details>

- **2026-09-22** — Fang Wang, Huitao Li, Wenhan Chao et al. — [GAD-MambaUNet: Direction-Group Mamba with Gradient-Adaptive DINOv3 Distillation for Lightweight Medical Image Segmentation](http://arxiv.org/abs/2609.26729v1)
  <details><summary>📄 Abstract</summary>
  In this paper, we proposed GAD-MambaUNet, a lightweight medical image segmentation network that combines efficient local modeling, direction--group state-space interaction, and training-time foundation-model supervision. To improve contextual modeling in compact segmentation networks, we introduced Direction-Group Graph Selective Scan (DG-GSS), which treated scan-direction and channel-group responses as graph nodes and enabled structured information exchange before multi-directional fusion. We f...
  </details>

- **2026-09-22** — Xiaoyu Yang, Jie Lu, Wei Duan et al. — [The Sirens' Song: When Proximal Background Context Overshadows Distant Evidence](http://arxiv.org/abs/2609.26718v1)
  <details><summary>📄 Abstract</summary>
  Long-context LLMs focus on retrieving distant evidence from extensive context, yet existing work has largely focused on overcoming distance alone. In this work, we identify the Proximity Trap, insufficient attention to distant evidence often arises less from distance itself than from cumulative competition with abundant, task-irrelevant proximal background. To address the Proximity Trap, we introduce LYRA (Long-context heavY-tailed Relevance Alignment), a t-distributed directional matching mecha...
  </details>

- **2026-09-22** — Fiona Kekwick, Matthew Baugh, Bernhard Kainz et al. — [MMAP: Multimodal Missing-Aware Pretraining for Longitudinal Alzheimer's Prediction](http://arxiv.org/abs/2609.26617v1)
  <details><summary>📄 Abstract</summary>
  Clinical decision making heavily relies on predicting the disease progression trajectory by seeking to understand patient's health status which is characterised by multimodal medical data. AI holds great potential for learning useful representations from multimodal medical data to predict disease progression and aid clinical decision making. However, development of predictive AI models is constrained by missing modalities and incomplete tabular data frequently occurring in medical datasets. In a...
  </details>

- **2026-09-22** — Lorenzo Zangari, Davide Picca — [A Semiotics-Aware Framework for Evaluating Fidelity and Coverage in Natural Language Generation](http://arxiv.org/abs/2609.26527v1)
  <details><summary>📄 Abstract</summary>
  When two texts describe the same expression, standard metrics based on lexical overlap or whole-text similarity may fail to detect meaningful differences in how that expression is framed. We propose a framework to evaluate semiotic alignment between texts, where a semiotic profile encompasses both the contextual meaning and the discourse references made salient by a text. Our approach yields two scores, Semiotic Fidelity and Semiotic Coverage, estimating how much of one text's profile is support...
  </details>

- **2026-09-22** — Mario Sanz-Guerrero, Katharina von der Wense — [Calibration as a First-Class Criterion in LLM Evaluation](http://arxiv.org/abs/2609.26489v1)
  <details><summary>📄 Abstract</summary>
  Calibration of language models -- the alignment between expressed or implicit confidence and empirical correctness -- is a well-studied subfield within NLP. Methods to measure it already exist. The problem is adoption: outside this subfield, NLP research regularly introduces new models, datasets, and benchmarks without checking whether the model's confidence scores are meaningful. We argue that this adoption gap is a major obstacle to trustworthy LLM evaluation. Miscalibration causes problems in...
  </details>

- **2026-09-22** — Junlong Wu, Zijun Li, Yuting Hu et al. — [KwaiMind Technical Report](http://arxiv.org/abs/2609.26375v1)
  <details><summary>📄 Abstract</summary>
  Commercial image editing requires product identity preservation, accurate text rendering, and user appeal alongside general editing quality. We present KwaiMind, an image editing system combining general capabilities with e-commerce specialization. An agent-based data engine maintains approximately 1.8 million high-quality editing pairs. Built on a multimodal diffusion transformer, KwaiMind undergoes continued pre-training and supervised fine-tuning, followed by preference optimization and onlin...
  </details>

- **2026-09-22** — Jiayan Fu, Hang Xu, Yong Zhang et al. — [PACT: From Credit Assignment to Critic Alignment](http://arxiv.org/abs/2609.26355v1)
  <details><summary>📄 Abstract</summary>
  Reinforcement learning has become a central component of large language model (LLM) post-training, yet token-level credit lacks a generally accepted mathematical definition, leaving its relationship to commonly used training signals unclear. We formulate three regularity conditions, namely Completeness, Prefix Consistency, and Neutrality, and prove that they uniquely determine token-level credit. This characterization provides a unified basis for explaining phenomena across existing algorithms a...
  </details>

- **2026-09-22** — Masoud Soleimani — [Target alignment, dilution and forecast selection when cross-sectional forecasts share a common target](http://arxiv.org/abs/2609.26303v1)
  <details><summary>📄 Abstract</summary>
  Forecasters often score the same units per date against one standardized realized outcome. We show that every standardized forecast splits exactly into a component aligned with this common target and a component uncorrelated with it. Three consequences follow: forecast-error correlation largely mirrors forecast correlation and is therefore a poor measure of diversity; an equally weighted combination beats a no-information forecast only when average alignment is large relative to the combination'...
  </details>

- **2026-09-22** — Yan Zhang, Pei Fu, Daiqing Wu et al. — [Towards Omni-dimensional GUI Agent Navigation with Masked Trajectory Prediction](http://arxiv.org/abs/2609.25769v1)
  <details><summary>📄 Abstract</summary>
  Graphical User Interface (GUI) Agents autonomously interact with software to fulfill user requests, where GUI navigation stands out as the most critical and challenging capability. Mastering this capability demands a complex synergy of step-wise decision-making, state-action alignment, and long-horizon planning. While directly mixing these corresponding navigation tasks seems intuitive to simultaneously acquire these skills, such a direct combination is severely bottlenecked by inconsistent opti...
  </details>

- **2026-09-22** — Rojin Ziaei — [The Limits of Simulated Societies: How Post-Training and Survey Fine-Tuning Erase Cross-Cultural Variance](http://arxiv.org/abs/2609.25760v1)
  <details><summary>📄 Abstract</summary>
  Using large language models (LLMs) to simulate diverse human populations has the potential to transform many aspects of computational social science, yet many evaluations score the average response rather than the spread of opinion within real groups. Here, we develop a diagnostic framework that measures point accuracy alongside dispersion retention, the ratio of predicted to human standard deviation ($\dr$), on 10{,}000 respondent--question pairs from the World Values Survey (WVS) spanning twel...
  </details>

- **2026-09-22** — Dingkang Yang, Yizhou Liu, Wendong Cheng et al. — [Fysiverse-3D-Vision Technical Report: Generating Executable 3D Worlds from Images through Unified Spatial Reasoning](http://arxiv.org/abs/2609.25741v1)
  <details><summary>📄 Abstract</summary>
  Generative models have advanced image-conditioned 3D content creation, yet generating controllable and executable 3D scenes from a single image remains challenging. Existing 3D generative approaches can synthesize visually plausible objects and scenes, but their spatial layout estimation is coupled with specific asset generators. They struggle to jointly model object semantics, metric geometry, and scene-level spatial relationships, which are essential for interactive editing, physical simulatio...
  </details>

- **2026-09-22** — Adam Ousherovitch, Ambuj Tewari — [Direct Optimization of Generators for Search in Automated Theorem Proving](http://arxiv.org/abs/2609.25575v1)
  <details><summary>📄 Abstract</summary>
  Fine-tuned Large Language Models (LLMs) significantly advance Automated Theorem Proving (ATP), but are often deployed as guiding policies within tree search rather than for single-attempt generation. Recent work shows cross entropy is suboptimal for an LLM used in flat search strategies such as aggregation or filtering and that work has developed new loss functions to correct this misalignment. Extending this alignment to tree search is more challenging: proof discovery depends on exploration an...
  </details>

- **2026-09-22** — Jinu Pahk, Jesoon Kang, Taegeon Park et al. — [HABILIS Brain 0: Geometry-Change Supervision for Vision-Language-Action and Residual Flow Recovery](http://arxiv.org/abs/2609.25558v1)
  <details><summary>📄 Abstract</summary>
  Vision-language-action policies benefit from geometric supervision, but current-frame geometry alone does not explicitly describe the changes associated with manipulation. This design is motivated by the goal of learning an embodiment-agnostic visual interface that can be pretrained across robot and egocentric video before robot-specific action alignment. We introduce Geometry-Change VLA (GC-VLA), which learns to predict multiview future-current geometry-change tokens from current observations. ...
  </details>


### 📂 robustness
*鲁棒性与可靠性 / Robustness & Reliability* — 72 papers

- **2026-09-24** — Arunabh Srivastava, Mohammad A.,  Khojastepour et al. — [GRASP: Generating, Revising, and Assessing for Strategic Planning with Agentic AI](http://arxiv.org/abs/2609.30147v1)
  <details><summary>📄 Abstract</summary>
  Large Language Models (LLMs) typically exhibit a performance profile where reliability degrades as task complexity increases. We address the challenge of generating high-quality natural language executable plans for complex tasks by introducing $\textbf{GRASP}$, a strategy-aware, multi-stage planning framework. GRASP decouples the planning pipeline across specialized, context-isolated modules: it pre-compiles global macro-guidelines (GenPlan), explores alternative localized strategies within iso...
  </details>

- **2026-09-24** — Suvradip Paul, Chandra Bhushan, Harsh Sharma et al. — [IndicBankBench: Evaluating Safety and Reliability of Language Model Assistants in Indian Retail Banking](http://arxiv.org/abs/2609.29167v1)
  <details><summary>📄 Abstract</summary>
  Banking assistants must use account-specific information to answer requests and, in many cases, take actions through tools. Evaluating only the final response misses important errors. An assistant may ask for information it already has, rely on stale context, select the wrong account, or write an invalid value after stating the correct one. We introduce IndicBankBench, a 799-case benchmark for Indian retail banking spanning five operational domains, a capability/refusal domain, and twenty primar...
  </details>

- **2026-09-24** — Hongxin Zhang, Chunru Lin, Tsun-Hsuan Wang et al. — [Self-Adaptive VLA for Robust Robot Deployment](http://arxiv.org/abs/2609.30092v1)
  <details><summary>📄 Abstract</summary>
  While Vision-Language-Action (VLA) models demonstrate impressive capabilities in robotic manipulation, their memoryless nature renders them brittle to test-time environment shifts, particularly hardware shifts caused by wear or imperfect calibration. Enabling these models to self-adapt during deployment without requiring continuous on-site recalibration remains a critical bottleneck for real-world scalability. In this work, we introduce Self-Adaptive VLA, a novel post-training recipe that enable...
  </details>

- **2026-09-24** — Adam Górski, Mateusz Jąkalak, Rafał Jakubowski — [Baszta: Data-Centric Fine-Tuning of a Polish Multi-Label Safety Classifier](http://arxiv.org/abs/2609.29266v1)
  <details><summary>📄 Abstract</summary>
  We develop a multi-label Polish content-safety classifier by fine-tuning allegro/herbert-base-cased (124M) across five categories (hate, vulgarity, sexual content, crime, self-harm) using a Focal + R-Drop objective, and evaluate the resulting model against Bielik Guard (Sójka) on the shared out-of-distribution Gadzi Język benchmark. Both systems are given per-category threshold tuning on the same calibration split. Under that matched protocol our model holds a small but statistically significant...
  </details>

- **2026-09-24** — Shilin Ma, Chubin Zhang, Xulong Bai et al. — [From Passive Execution to Active Exploration: Agentic Embodied Manipulation in Realistic Environments](http://arxiv.org/abs/2609.29091v1)
  <details><summary>📄 Abstract</summary>
  Recent advances in agentic systems have substantially enhanced the long-horizon capability of embodied manipulation. However, many existing frameworks still follow a passive execution paradigm, which limits their applicability to real-world scenarios involving textual semantic cues, distractors, and initially invisible targets. To bridge this gap, we propose an agent-based active exploration framework that enables robots to dynamically interact with the environment rather than merely execute pre...
  </details>

- **2026-09-24** — Wei Chen, Zhen Liu — [Pressure-robust finite elements for the Stokes problem on three-dimensional curved domains](http://arxiv.org/abs/2609.30008v1)
  <details><summary>📄 Abstract</summary>
  This paper develops a divergence-free, inf-sup stable, optimally convergent and pressure-robust finite element method for the three-dimensional Stokes problem on curved domains. The geometry is approximated by an isoparametric tetrahedral mesh, while the velocity space is obtained from Scott--Vogelius spaces on an Alfeld split by the Piola transform. The discrete inf-sup condition is proved using suitable face bubble functions. The insufficient accuracy of quadrature rules on curved triangular i...
  </details>

- **2026-09-24** — Irene Aldridge — [Multi-Dimensional Matching](http://arxiv.org/abs/2609.29958v1)
  <details><summary>📄 Abstract</summary>
  We study a matching mechanism where agents and objects are described by features rather than complete rankings. A single spectral projection reduces the problem to a one-dimensional sort, computable in O(N log N) time. We prove that on descaled features and preferences, our algorithm obtains the exact Nash Social Welfare (NSW) optimum within the projected space, with an unconditional utilitarian-welfare guarantee and a conditional NSW guarantee. The proposed mechanism is stable against exogenous...
  </details>

- **2026-09-24** — Nitya Nanvani, Andras Palffy, Holger Caesar — [SplatLabel: Pseudo-Labelling through 4D Gaussian Splatting](http://arxiv.org/abs/2609.29836v1)
  <details><summary>📄 Abstract</summary>
  While 2D Vision Foundation Models offer a pathway to automate 3D semantic pseudo-labelling, translating these priors into robust 3D representations typically requires complex heuristics or multi-model ensembles. We introduce SplatLabel, an automated pipeline that leverages a 4D Gaussian representation to extract LiDAR segmentation with predictive confidence, as well as semantic occupancy grids at arbitrary voxel resolutions. At its core, SplatLabel handles dynamic environments through an explici...
  </details>

- **2026-09-24** — Jianheng Zhou, Chaoli Zhang, Xingjun Wei et al. — [REAT: A Reflective Experience-Augmented Tutoring Framework for Multi-turn Mathematical Instruction](http://arxiv.org/abs/2609.29804v1)
  <details><summary>📄 Abstract</summary>
  Current Large Language Models (LLMs) excel at solving complex mathematical problems, yet this proficiency does not inherently translate into effective tutoring. While advanced LLM tutors may leverage multi-agent frameworks or fine-tuning, most still lack a mechanism to systematically accumulate and reuse pedagogical experience over time, limiting their adaptability to diverse student needs during fluid, multi-turn interactions. To bridge this gap, we propose the Reflective Experience-Augmented T...
  </details>

- **2026-09-24** — Zhongxin Huang, Songyang Li, Renzhe Zhou et al. — [SEEK: Skill-Routed Evaluation with Evolvable Knowledge for Industrial Search](http://arxiv.org/abs/2609.29803v1)
  <details><summary>📄 Abstract</summary>
  Search quality evaluation provides essential supervision and diagnostic signals for the development and iteration of industrial search systems. Although large language models (LLMs) offer a scalable alternative to manual assessment, reliable automatic evaluation remains challenging: users experience search results at the page level, while the applicable evaluation criteria are multi-dimensional and continuously evolving. Packing all evaluation criteria into a unified prompt introduces irrelevant...
  </details>

- **2026-09-24** — Sheekar Banerjee, Md. Srabon Chowdhury, Md. Mahbub Hasan Akash et al. — [Lightweight Vision Transformer-Based U-Net for Brain Tumor Segmentation from MRI](http://arxiv.org/abs/2609.29785v1)
  <details><summary>📄 Abstract</summary>
  Accurate brain tumor segmentation from Magnetic Resonance Imaging is essential for diagnosis, treatment planning, and surgical guidance. Although Convolutional Neural Networks, particularly UNet, have achieved significant success in medical image segmentation, they often struggle to capture the long-range spatial dependencies required to model tumors with irregular shapes and complex boundaries. This paper proposes a lightweight Vision Transformer UNet that combines the hierarchical feature extr...
  </details>

- **2026-09-24** — Douglas Leith — [Between the Commits: Process, Error, and Claim Reliability in a Wholly AI-Authored Codebase](http://arxiv.org/abs/2609.29744v1)
  <details><summary>📄 Abstract</summary>
  We present: (i) a new dataset consisting of the full development history of a 21,000-line Python tool built entirely by Claude AI, with no human-authored code or tests, (ii) two code-provenance tracing tools, (iii) three taxonomies for instruction intent, commit provenance, and response reliability, (iv) application of these to analyse the dataset. We find that: (i) user coding agent CLI instructions differ in kind from IDE-chat instructions, with a greater focus on comprehension, planning and c...
  </details>

- **2026-09-24** — Yujie Guo, Hongjie Chen, Jian Kang et al. — [TS-OPD: Reconciling ASR and QA in Speech Language Models via Task-Specific On-Policy Distillation](http://arxiv.org/abs/2609.29464v1)
  <details><summary>📄 Abstract</summary>
  Speech Language Models (SLMs) inherit strong instruction-following capabilities from pretrained language models, yet ASR specialization can substantially degrade them. To address this ASR--QA trade-off, we propose Task-Specific On-Policy Distillation (TS-OPD), which leverages models before and after ASR specialization as complementary QA and ASR teachers. The student generates separate task-conditioned trajectories for ASR and QA, each supervised only by its corresponding teacher, thereby reduci...
  </details>

- **2026-09-24** — Amir Ivry, Kai-Wei Chang, Lin Zhang et al. — [Voice Agents under Acoustic Stress: From Signal Degradation to Interaction and Action](http://arxiv.org/abs/2609.29452v1)
  <details><summary>📄 Abstract</summary>
  Voice agents must complete users' tasks despite noise, reverberation, and competing speech. Evaluating agents' robustness therefore requires following how acoustic conditions affect the conversation and the actions taken on the user's behalf. This overview examines what existing benchmarks reveal about agents' ability to complete tasks under acoustic stress and where further task-based evaluation is required. We then introduce TRACE, a practical workflow for designing, running, and interpreting ...
  </details>

- **2026-09-24** — Bing Sun, Yue Lin, Yongsheng Yuan et al. — [UCON: Uncertainty-aware Navigation with Historical Re-association in Dynamic Environments](http://arxiv.org/abs/2609.29419v1)
  <details><summary>📄 Abstract</summary>
  Autonomous navigation in dynamic environments is hindered by two fundamental challenges: perception instability and uncertainty-optimization mismatch. The former leads to identity switches and unreliable motion estimation, while the latter prevents principled incorporation of motion uncertainty into trajectory optimization. To address these challenges, we propose UCON, an uncertainty-aware navigation algorithm in dynamic environments. For perception instability, we present a point-level historic...
  </details>

- **2026-09-24** — Youngeun Seol, Jimin Shin, Heeseo Yoon et al. — [Domain Recentering and Confidence-Weighted Prior Calibration for Vision-Language Models](http://arxiv.org/abs/2609.29358v1)
  <details><summary>📄 Abstract</summary>
  Vision-language models such as CLIP achieve strong zero-shot classification, yet under distribution shift, visual embeddings drift from fixed text embeddings. Training-free calibration avoids the per-sample optimization of prompt learning, but prior feature calibration gives each image the full bias of one hard cluster. We propose Domain Recentering with Confidence Calibration (DRC), a training-free method adapting CLIP from a set of unlabeled target images. DRC fits a Gaussian mixture once and ...
  </details>

- **2026-09-24** — Siyu Yao, Du Q. Huynh, Lian Xu et al. — [Speech Block Influence: Component-Specific Layer Scoring for Pruning Speech LLMs](http://arxiv.org/abs/2609.29343v1)
  <details><summary>📄 Abstract</summary>
  Speech LLMs are costly to deploy in resource-constrained settings. Layer pruning can cut this cost, but existing scoring metrics transfer poorly to speech LLMs: they assume a decoder-only architecture with homogeneous token sequences, whereas speech LLMs add encoder and adapter components and process multimodal sequences. We propose Speech Block Influence (SBI), the first layer-importance scoring framework designed for speech LLM pruning that consists of two component-specific scores: SBI-Enc me...
  </details>

- **2026-09-24** — Xunlan Zhou, Xianliang Yang, Li Zhao — [From Text Decisions to Pixels: An Study of Jev-Style Visual Choice Model](http://arxiv.org/abs/2609.29283v1)
  <details><summary>📄 Abstract</summary>
  Visual software often needs a decision over supplied alternatives rather than a generated explanation. We present PixelJev, a native-image decision interface that maps an image, a task instruction, and a runtime candidate set to a structured choice and candidate-conditioned probabilities using small open multimodal models. Its initial realization unifies recognition and multiplechoice visual question answering through an existing language-model readout, with separately evaluated options for froz...
  </details>

- **2026-09-24** — Wenxuan Wu, Shuhan Zhang, Shuai Wang et al. — [Exploring a Single Autoregressive LLM for Unified Target Speech Extraction across Synchronous and Asynchronous Cues](http://arxiv.org/abs/2609.29238v1)
  <details><summary>📄 Abstract</summary>
  Target speech extraction (TSE) typically trains a separate extractor per cue, and visual-cue systems often need corruption-matched training to remain robust under visual frame corruption. We show that one autoregressive LLM backbone, TSE-Omni, can serve both temporally synchronous cues (lip movements, co-speech gestures) and asynchronous cues (enrollment audio, text). TSE-Omni is driven by next-token prediction: each step predicts target speech semantic tokens from its own past outputs, which we...
  </details>

- **2026-09-24** — Peiwen Zhang, Kristie Hu, Jovana Knezevic et al. — [Recoverable Geographic Location Information in Earth-Observation Embeddings](http://arxiv.org/abs/2609.29151v1)
  <details><summary>📄 Abstract</summary>
  Earth-observation (EO) foundation models provide reusable embeddings, yet downstream task accuracy does not reveal whether these representations encode geographic information, which may be beneficial for location-aware applications but potentially detrimental when representations invariant to geographic location are desired. We therefore evaluate the geographic coordinate robustness of Tessera v1, Tessera v1.1, and AlphaEarth by testing whether coordinates can be predicted from the embedding rep...
  </details>

- **2026-09-24** — Kang Zhou — [A Particle-Swarm-Assisted Gradient Meta-Learning Algorithm for Joint Transmit Precoding and STAR-RIS Coefficient Optimization](http://arxiv.org/abs/2609.29150v1)
  <details><summary>📄 Abstract</summary>
  This paper investigates the joint optimization of the transmit precoder and the transmission/reflection coefficients of a simultaneously transmitting and reflecting reconfigurable intelligent surface (STAR-RIS) to maximize the weighted sum rate (WSR) in a multi-user downlink. We propose a particle-swarm-assisted gradient meta-learning (PSA-GML) algorithm for this non-convex problem. The original problem is first equivalently transformed via an amplitude-split parameterization and a collapsed pre...
  </details>

- **2026-09-24** — Rakib Abdullah, Md. Maruful Islam Maruf — [Language Specificity vs. Domain Diversity: Benchmarking Transformers for Bangla Medical NER](http://arxiv.org/abs/2609.29101v1)
  <details><summary>📄 Abstract</summary>
  Medical Named Entity Recognition (NER) for low-resource languages remains a challenging task due to high linguistic variability and a scarcity of domain-specific annotated corpora. This work presents a comprehensive empirical benchmark evaluating three fine-tuned transformer encoders-BanglaBERT, multilingual BERT (mBERT), and XLM-RoBERTa-against GPT-4o mini under zero-shot and few-shot prompting configurations for Bangla medical NER. In contrast to prior studies that evaluated large language mod...
  </details>

- **2026-09-24** — Zhuo Zhang, Shun Zou, Canqun Yang et al. — [Physics and Data Driven Transformer-Mamba Framework for Flow Field](http://arxiv.org/abs/2609.29087v1)
  <details><summary>📄 Abstract</summary>
  While deep learning accelerates expensive partial differential equation solving in computational fluid dynamics (CFD), existing methods like PINNs and FNOs often struggle with generalization, noise robustness, and physical consistency. We introduce the Transformer-Mamba for Flow Field (TM4FF) framework, a physics-constrained operator learning model with three key innovations: a Residual Wavelet Mamba (RWM) layer for feature denoising, a Transformer-based attention mechanism for enhanced feature ...
  </details>

- **2026-09-24** — I. Zakir Ahmed, Hamid Sadjadpour — [Multi-Agent Orchestration of 3GPP Channel Estimators](http://arxiv.org/abs/2609.29044v1)
  <details><summary>📄 Abstract</summary>
  Pilot-aided channel estimation is a decisive block in orthogonal frequency-division multiplexing (OFDM) receivers for both 5G New Radio (5G-NR) and Long-Term Evolution (LTE). A large body of estimators exists, from simple least-squares (LS) interpolation to statistically optimal linear minimum-mean-square-error (LMMSE) variants and, more recently, deep convolutional denoisers, yet no single estimator is uniformly best: the winner depends on the propagation scenario, the numerology, the operating...
  </details>

- **2026-09-24** — Michikuni Eguchi, Kohei Honda, Masafumi Endo et al. — [ReVNM: Learning-Based Visual Navigation from a Remote Camera](http://arxiv.org/abs/2609.28976v1)
  <details><summary>📄 Abstract</summary>
  Visual Navigation Models (VNMs) enable robots to navigate from egocentric visual observations without geometric localization and planning, but long-range navigation still requires pre-built maps. This paper presents the Remote Visual Navigation Model (ReVNM), which uses a single remote surveillance camera to serve as both an observation source and an implicit environmental map for visual navigation. While the use of remote cameras could eliminate the need for pre-built maps as well as onboard vi...
  </details>

- **2026-09-24** — Xincheng Yao, Haobo Fu, Weiming Liu et al. — [Back to the Definition: Estimating Step-Level Advantages via Trajectory Graphs for Agentic Reinforcement Learning](http://arxiv.org/abs/2609.28963v1)
  <details><summary>📄 Abstract</summary>
  Group-based reinforcement learning (RL) methods, such as GRPO and its variants, have become a leading paradigm for training reasoning and agentic large language models (LLMs). While their group-normalized advantage estimation is reliable at the response level, it becomes systematically biased at the step level, since coarse-grained trajectory-level advantages are hard to accurately reflect the contribution of individual steps (i.e, failed trajectories may contain valuable steps). Revisiting the ...
  </details>

- **2026-09-24** — Zetong Li, Zhuosong Xie, Hengyu Fan et al. — [Response-state Learning for Transferable Vibrational Spectroscopic Characterization with Electron Prior](http://arxiv.org/abs/2609.28935v1)
  <details><summary>📄 Abstract</summary>
  Vibrational spectral prediction can become inaccurate when localized stereoelectronic environments perturb intermediate response states and high-risk response units dominate characteristic spectral fingerprints, making prediction across external chemical space difficult. SO(3) Equivariant Neural Kalman Networks (SENK) form a response-state cascade that combines an equivariant transformer backbone for Hessian, dipole-derivative and polarizability-derivative learning, an Equivariant Neural Kalman ...
  </details>

- **2026-09-23** — Geng Chen, Ruotong Pan, Zhirui Yang et al. — [Beyond Surface Style: Aligning Multi-Turn User Simulators with Behavioral Consistency](http://arxiv.org/abs/2609.28690v1)
  <details><summary>📄 Abstract</summary>
  Faithful user simulation is fundamental to building, evaluating, and improving interactive AI at scale. However, plausible individual responses do not ensure that simulated users reproduce the intent evolution and outcomes observed in real interactions. We propose TRACER, a multi-turn user simulator that explicitly models users' evolving intent and learns to align simulated behavior with real interaction trajectories. TRACER is trained in two stages: supervised fine-tuning on real user dialogues...
  </details>

- **2026-09-23** — Yeonsung Jung, Joonhyun Jeong, Hoang Pham et al. — [Looks the Same, Answers Differently: Flip-Direction Steering for Robust Vision-Language Reasoning](http://arxiv.org/abs/2609.28851v1)
  <details><summary>📄 Abstract</summary>
  Vision-language models (VLMs) achieve strong visual reasoning performance, yet subtle changes from routine image capture and processing can alter their reasoning trajectories even when images appear nearly identical. In long-horizon generation, the resulting activation shifts may accumulate across decoding steps, progressively altering reasoning tokens and ultimately changing the final answer, a phenomenon referred to as answer flips. To address this instability, we propose FlipDir (Flip-Directi...
  </details>

- **2026-09-23** — Xiaoran Yang, Yang Zhan, Xie He et al. — [Signals of AI Hallucination: Designing Hallucination-Aware Cues for Embodied Conversational Agents in VR](http://arxiv.org/abs/2609.28812v1)
  <details><summary>📄 Abstract</summary>
  LLM-powered conversational agents (CAs) often present uncertainty and provenance cues alongside their responses to help users assess response reliability and identify potential hallucinations. In immersive environments such as Virtual Reality (VR), CAs often take the form of speech-based embodied conversational agents (ECAs), where uncertainty and provenance cues cannot rely on persistent inline text and may be missed or disrupt comprehension when delivered through speech. We conducted a within-...
  </details>

- **2026-09-23** — Nuoyue Xu, Jiang Liu, Wenxuan Huang et al. — [Agent Memory with Episodic Retrieval for Financial Decision-Making](http://arxiv.org/abs/2609.28771v1)
  <details><summary>📄 Abstract</summary>
  Large language models (LLMs) have demonstrated strong capabilities in financial analysis and reasoning, inspiring recent advances in agent-based trading frameworks. While these systems show promise, prior approaches either emphasize long-horizon forecasting or operate as stateless analyzers, limiting their applicability to the demands of trading in complicated settings. To address these gaps, we introduce META (Memory Enhanced Trading Agent), the first RAG-like episodic-memory-augmented multi-ag...
  </details>

- **2026-09-23** — Eina Mizui, Tomohiro Shiraishi, Shunichi Nishino et al. — [Selective Inference for Deep Clustering in Latent Spaces](http://arxiv.org/abs/2609.28756v1)
  <details><summary>📄 Abstract</summary>
  Deep clustering is a powerful approach for discovering meaningful structures in high-dimensional data by learning a low-dimensional latent representation prior to clustering. Despite its empirical success, assessing the statistical reliability of the resulting clusters remains challenging. Testing discovered clusters on the same data induces selection bias and invalidates classical $p$-values. Selective inference (SI) provides a principled framework for correcting this bias, but existing methods...
  </details>

- **2026-09-23** — James Wu, Chris R. Sims — [Policy Complexity, Reaction Time, and Bounded Rationality in Reinforcement Learning](http://arxiv.org/abs/2609.28737v1)
  <details><summary>📄 Abstract</summary>
  Biological agents do not learn under conditions of unlimited computation. For humans, learning and choice are shaped by constraints on perception, attention, and working memory, which limit how much state information guides behavior and therefore bound policy complexity. Standard reinforcement learning models typically optimize reward without explicitly representing these internal costs, making them less suitable as models of biological intelligence. We derive MI-SARSA, an on-policy temporal-dif...
  </details>

- **2026-09-23** — Nicolò Gozzi, Ciro Cattuto, Alessandro Vespignani — [Driving Epidemic Models with AI Agents: the Epydemix Agent Framework](http://arxiv.org/abs/2609.28692v1)
  <details><summary>📄 Abstract</summary>
  Artificial Intelligence agents based on large language models provide convenient natural language interfaces to scientific software, but reliability is not automatic. Here we introduce the Epydemix Agent Framework, an additive layer over Epydemix, an open-source Python library for stochastic compartmental epidemic modeling. The framework extends the library with four capabilities to facilitate interaction with an AI agent: discovery of available models and parameters, preventive validation of a ...
  </details>

- **2026-09-23** — Weiwei Ye, Hangchen Liu, Renhe Jiang — [NumericJev: Jev-like LLM Numerical Decoding with Multiway Decision Trees](http://arxiv.org/abs/2609.28587v1)
  <details><summary>📄 Abstract</summary>
  Large language models can interpret natural lan- guage, yet robust decisions remain challenging. Jev-like models expose structured choices, but these interfaces do not directly provide numeri- cal values at a requested precision. We propose NUMERICJEV, a training-free numerical decod- ing algorithm that enables numerical output from any LLM with a Jev-like structured-choice in- terface. Surprisingly, on our arithmetic bench- mark, it outperforms direct selection from a can- didate list containin...
  </details>

- **2026-09-23** — Oswin So, Eric Yu, Chuchu Fan — [LEAP-CBF: A Safety Filter for Uncertain Systems with Least-Effort Adversarial Potentials](http://arxiv.org/abs/2609.28364v1)
  <details><summary>📄 Abstract</summary>
  Control barrier functions (CBF) are a popular safety filter to ensure safety for nonlinear dynamical systems. However, when the system is subject to uncertainties and disturbances, this requires the use of robust variants of CBFs, which can be difficult to construct and can be overly conservative, especially for high-dimensional systems under input constraints. In this work, we propose a new approach to solve these challenges by introducing Least-Effort Adversarial Potentials (LEAP), a certifica...
  </details>

- **2026-09-23** — Yuxuan Li, Will Epperson, Wesley Deng et al. — [CAVEAT: Towards Robust Computer-Use Agents in Incentive-Misaligned Environments](http://arxiv.org/abs/2609.27273v1)
  <details><summary>📄 Abstract</summary>
  Computer-use agents (CUAs) increasingly act on behalf of users online. What happens when the environments they operate in have incentives that do not align with the user's? In online marketplaces, for example, platforms may favor some products over others, potentially steering agents away from the user's objective. Existing CUA benchmarks cover cooperative settings or explicit attacks, but do not test whether agents preserve user objectives when the environment itself has a stake in the outcome....
  </details>

- **2026-09-23** — Jiaxing Li, Lei Song, Rui Dong et al. — [Learning from Failures: Heterogeneous Graph Memory for Small Language Model Tool-Using Agents](http://arxiv.org/abs/2609.28003v1)
  <details><summary>📄 Abstract</summary>
  Small and medium-sized language models offer cost-effective executors for tool-using agents, making them attractive for local and large-scale deployment. However, in long-horizon and stateful environments, they often make structural errors such as missing required observations, performing premature writes, repeating failed calls, and violating action preconditions. These errors can lead to incorrect state updates, policy violations, and costly or irreversible consequences, making reliable tool e...
  </details>

- **2026-09-23** — Akash Samanta, Manish Pratap Singh, Debasis Chaudhuri — [Hidden not Deleted: How Networks Suppress Entangled Features](http://arxiv.org/abs/2609.27593v1)
  <details><summary>📄 Abstract</summary>
  Concept erasure methods that operate via linear projection assume that features occupy separable subspaces. We show this assumption fails under dense superposition: when two features are forced into an antipodal pair sharing a single subspace, state-of-the-art linear erasure destroys both, not just the target. Networks trained with gradient descent instead solve this problem non-linearly, but not uniformly: they converge to one of two distinct circuit-level solutions depending on initialization,...
  </details>

- **2026-09-23** — Jialu Wang, Jianing Deng, Shuqing Luo et al. — [Quantization-Robust Unlearning through the Lens of Retain-Forget Loss Landscapes Interaction](http://arxiv.org/abs/2609.27355v1)
  <details><summary>📄 Abstract</summary>
  Unlearning ensures LLM compliance by removing the influence of private or copyrighted training data. However, since LLM models typically undergo post-training compression, like quantization, in practical deployment, it has been observed that the unlearning effect can be substantially weakened, with the forgetting behavior degrading more severely than that of model utility. This paper proposes a quantization-robust unlearning framework that makes forgetting robust to quantization while maintainin...
  </details>

- **2026-09-23** — Jiajie Zhang, Yankai Xiang, Changhao Chen — [Memory That Changes Action Is Not Memory That Guides It: Counterfactual Auditing of History-Conditioned Robot Policies](http://arxiv.org/abs/2609.27247v1)
  <details><summary>📄 Abstract</summary>
  A robot returning a block to its origin tray may encounter two task-consistent pasts that reconverge to the same current input but warrant different actions. Yet memory-policy evaluations often rely on task success or action change under memory perturbation, neither of which establishes that memory guides the decision. We propose the \textbf{Counterfactual Memory Audit (CMA)}, an evaluation protocol that crosses two histories at a verified-identical present, queries a frozen policy under common ...
  </details>

- **2026-09-23** — Vaishnavi Jagabathula, P Sangeerth, Pushpak Jagtap — [Tractable Reinforcement Learning for Full Class of Signal Temporal Logic Specifications Using Spatiotemporal Tube Reward](http://arxiv.org/abs/2609.28396v1)
  <details><summary>📄 Abstract</summary>
  This paper addresses the control problem for robotic systems, including non-holonomic and underactuated platforms operating under unknown dynamics and strict actuator limits to satisfy complex high-level specifications. We denote these high-level specifications using Signal Temporal Logic (STL) and propose a novel time-aware Reinforcement Learning (RL) framework that leverages the geometric properties of Spatiotemporal Tubes (STTs). While traditional analytical STT controllers often struggle to ...
  </details>

- **2026-09-23** — Zanyi Wang, Yuheng Lei, Dengyang Jiang et al. — [Beyond Future Prediction: Denoising as Generative Adaptation for Robot Control](http://arxiv.org/abs/2609.28339v1)
  <details><summary>📄 Abstract</summary>
  Pretrained generative Diffusion Transformers (DiTs) capture rich pixel-level visual and language-conditioned structure through large-scale image and video generation training. A growing line of robot policies builds on this generative prior, but how it should be transferred to control remains unclear, and existing approaches commonly instantiate this transfer through future visual prediction. We ask a more basic question: what a pretrained generative DiT actually contributes to action learning, ...
  </details>

- **2026-09-23** — Ilán Carretero, Pablo Meseguer, Rocío del Amor et al. — [Do Center Biases Propagate? Robustness of Pathology Foundation Models in Whole-Slide Image Classification](http://arxiv.org/abs/2609.28231v1)
  <details><summary>📄 Abstract</summary>
  Pathology foundation models (PFMs) have transformed computational pathology through powerful representation learning from histopathological images. PFMs provide rich, discriminative representations for whole slide image (WSI) analysis, enabling tasks such as slide-level classification under multiple instance learning (MIL). However, these representations may also encode non-biological signals associated with acquisition centers, potentially introducing spurious shortcuts into downstream predicti...
  </details>

- **2026-09-23** — Yiqin Wang, Nuri Cingillioglu, Charles Pert — [Log-Depth Recurrent Language Modeling](http://arxiv.org/abs/2609.28212v1)
  <details><summary>📄 Abstract</summary>
  Language modeling using Transformers has become commonplace despite their fixed computational depth and quadratic runtime with respect to input tokens. Recurrent models on the other hand offer linear depth but no parallel execution. In this work, we extend balanced-tree recursive operators from sequence encoding to autoregressive prediction, enabling all prefix representations to be computed with logarithmic depth and linear runtime. Our experiments provide an initial characterization of this mo...
  </details>

- **2026-09-23** — Gijs van Cuyck, Patric Feldmeier, Jan Tretmans et al. — [Scenario-Driven Neuroevolution: Using Models to Guide Test Generation for Games](http://arxiv.org/abs/2609.28130v1)
  <details><summary>📄 Abstract</summary>
  Automatically generating test inputs for games is challenging, as test generators must master the game to reach advanced program states while also ensuring robustness against the heavy program randomisation inherent to games. The test generator Neatest therefore optimises test suites consisting of neural networks that reach advanced program states and are robust to program randomisation, as they generate test inputs dynamically based on the current program state. Neatest is a white-box testing a...
  </details>

- **2026-09-23** — Weijie Xu, Ming Wang, Ruicheng Ma et al. — [Photonics-GCCE: group collaborative-competitive evolution multi-agent framework for universal and autonomous optical design](http://arxiv.org/abs/2609.28045v1)
  <details><summary>📄 Abstract</summary>
  Large language model (LLM)-empowered photonic agents connect natural-language intents to executable solvers, showing significant advantages over conventional optical design approaches. However, current multi-agent frameworks operate within a collaborative paradigm without extrinsic selective pressure, which could inherit shared blind spots, converge prematurely, and fail to accumulate transferable experience for intricate tasks. Here, we introduce a group photonics collaboration-compete evolutio...
  </details>

- **2026-09-23** — Michael Lawrence Castanares, Princess Ventures, Allan Tan — [Evaluation of pre-trained models for pedagogical assessment of novel AI-assisted educational questions](http://arxiv.org/abs/2609.27749v1)
  <details><summary>📄 Abstract</summary>
  The surge in AI-assisted generation of educational materials has outpaced our capacity to validate their pedagogical quality. Automated evaluation using Bloom Classifier models is a promising approach to assess educational materials at scale. These models show high accuracy within-distribution dataset (IID Dataset). However, applying the same models to new out-of-distribution (OOD) datasets such as AI-assisted generated questions could show performance degradation. To identify robust classifiers...
  </details>

- **2026-09-23** — Mohammad Narimani, Seyyed Ali Emami — [GA-Agent: Large Language Models as Hyperparameter Optimizers for Evolutionary Controller Synthesis](http://arxiv.org/abs/2609.27725v1)
  <details><summary>📄 Abstract</summary>
  Tuning PID controllers to satisfy competing objectives - low tracking error, fast settling, limited overshoot, and moderate control effort - is labor-intensive and requires expertise. Genetic algorithms (GAs) offer gradient-free optimization of controller gains against a weighted fitness function, but success depends on meta-level choices: population size, generation budget, gain bounds, and fitness weights. These are usually set by manual trial-and-error or costly bilevel optimization, exposing...
  </details>

- **2026-09-23** — Jeffrey D. Michler, Kieran Douglas, Anna Josephson — [Mining Meaning: Measurement Error in AI-Assisted Literature Reviews](http://arxiv.org/abs/2609.27686v1)
  <details><summary>📄 Abstract</summary>
  Researchers increasingly use generative AI, particularly large language models (LLMs), to automate tasks across the research pipeline. We study the reliability of these tools at the reading, classification, and synthesis of large bodies of academic literature. We frame LLM-assisted literature reviews as a measurement problem, treating models as measurement systems and tracing how their errors affect downstream conclusions. As a test case, we use three different implementations of ChatGPT to iden...
  </details>

- **2026-09-23** — Sanghee Park, Kee-Eung Kim — [PRISM-VLM: A Multi-Axis Discriminative Benchmark for Compact Vision-Language Models](http://arxiv.org/abs/2609.27395v1)
  <details><summary>📄 Abstract</summary>
  Compact vision-language models (VLMs) now power a growing share of multimodal applications. The benchmarks used to compare them, however, inherit a frontier-centric design: each model is reduced to a single accuracy number, narrowing the inter-model gap on saturated suites and pressing models into low-score bands on harder ones. We introduce PRISM-VLM, a multi-axis discriminative benchmark that scores every item along seven axes covering the recurring failure modes (task quality, behavioral robu...
  </details>

- **2026-09-23** — Saimunur Rahman, Sagun Singh Shrestha, Abdelwahed Khamis et al. — [Automotive mmWave Spinning Radar Place Recognition with Spatially Gated Feature-Correlation Representation](http://arxiv.org/abs/2609.27394v1)
  <details><summary>📄 Abstract</summary>
  Automotive spinning FMCW radar provides dense, $360^\circ$ sensing and remains reliable under poor illumination and adverse weather, making it well-suited to autonomous navigation. Place recognition uses these observations to identify previously visited locations for re-localization and long-term navigation. However, heading changes appear as circular shifts in the polar radar representation, and conventional global aggregation can lose relationships among radar responses that are important for ...
  </details>

- **2026-09-23** — Behnam Ojaghi, Ricard Vilalta, Raul Muñoz — [From Intents to Algorithms: Verified Algorithm Discovery for Transport Networks](http://arxiv.org/abs/2609.27386v1)
  <details><summary>📄 Abstract</summary>
  Intent-based networking decouples desired outcomes from device-level configuration, but most systems still map intents to parameters of an algorithm selected in advance. Large language models (LLMs) create an opportunity to automate algorithm design, yet unrestricted generated code is unsuitable for transport-network control because feasibility, reproducibility, and robustness must be enforced independently of the model. We present VERA-TN, a verification-guided framework that compiles a network...
  </details>

- **2026-09-23** — Mingxiao Li, Wenhai Lai, Hei Victor Cheng et al. — [Single-RF-Chain Multiuser Semantic Communications via Metasurface Modulation](http://arxiv.org/abs/2609.27361v1)
  <details><summary>📄 Abstract</summary>
  Multiuser transmission with multiple radio-frequency (RF) chains enables flexible spatial multiplexing but incurs increased hardware complexity and power consumption. A programmable metasurface (MTS) provides an alternative means of introducing spatial degrees of freedom with a single-RF-chain access point (AP). This paper proposes \emph{Semantic Prism}, an MTS-enabled framework for concurrently transmitting independent semantic messages to multiple users. Semantic Prism jointly maps multiuser s...
  </details>

- **2026-09-23** — To Duy Hinh, Nguyen Le Quoc Anh, Phan Van Tri et al. — [Automated Extraction of Records of Processing Activities (RoPA) Using Hybrid RAG and Locally Deployed Large Language Models](http://arxiv.org/abs/2609.27359v1)
  <details><summary>📄 Abstract</summary>
  Vietnam's Personal Data Protection Law (Law No. 91/2025/QH15) and Decree No. 356/2025/ND-CP, effective January 1, 2026, require organizations to establish and maintain Records of Processing Activities (RoPA). Manual RoPA preparation is labor-intensive, while cloud-hosted large language models (LLMs) may conflict with data-sovereignty requirements. We propose RoPA Manager, a system for automated RoPA information extraction using hybrid retrieval that combines lexical ranking over tsvector, dense-...
  </details>

- **2026-09-23** — Md Tahmid Rahman Laskar, Xue-Yong Fu, Shashi Bhushan TN — [Can One Adapted Model Do It All? Fine-Tuning Strategy Selection for Customer Support LLMs](http://arxiv.org/abs/2609.27262v1)
  <details><summary>📄 Abstract</summary>
  Production customer-support systems often require LLMs to support multiple skills, such as intent classification, question answering, summarization, or tool-use decisions. A central deployment question is whether these skills should be handled by separate task-specialist models or by a single model trained through multi-task training, sequential updates, or model merging. We study this question using thirteen models spanning five families (Qwen3, Qwen3.5, Gemma-3, Llama-3.1, and Mistral) from 0....
  </details>

- **2026-09-22** — Yuhang Jiang — [Median Temporal Ensembling: Training-Free Robust Aggregation for Action-Chunked Visuomotor Policies](http://arxiv.org/abs/2609.27167v1)
  <details><summary>📄 Abstract</summary>
  Action-chunked visuomotor policies predict overlapping trajectories, so every executed action is covered by several predictions. Temporal ensembling smooths execution by combining these predictions with an exponentially weighted mean. One corrupted prediction can move the aggregate without bound: its breakdown point is 0. We use adversarial corruption to stress this deployed aggregator and to compare two kinds of guarantee. A metric guarantee bounds the response to a perturbation of a given size...
  </details>

- **2026-09-22** — Gautham Reddy, Kürşat Tekbıyık, Bryton Petersen et al. — [AI-Enabled Wireless Propagation Modeling and Radio Environment Maps for 5G Aerial Wireless Networks](http://arxiv.org/abs/2609.27083v1)
  <details><summary>📄 Abstract</summary>
  With the gaining prominence of aerial mobility applications, their success depends on the seamless integration of terrestrial and non-terrestrial network connectivity. However, providing reliable connectivity from terrestrial telecommunication networks remains challenging due to multi-cell interference from base stations (BSs) under line-of-sight (LoS) conditions to unmanned aerial vehicles (UAVs), coverage holes caused by antenna sidelobe degradation, localized multipath fading effects, and the...
  </details>

- **2026-09-22** — Youssef Hamdi Zafaan Ibrahim, Mohammed Khalaf Salama — [ACTS: A multi-tier benchmark evaluating LLM cipher identification under controlled blind conditions](http://arxiv.org/abs/2609.26893v1)
  <details><summary>📄 Abstract</summary>
  We introduce ACTS (Artifacts in Cipher Testing Suite), a reproducible benchmark that isolates cryptanalytic ability through tiered metadata deprivation (Tier-1: full metadata; Tier-2: filename only; Tier-3: completely blind) and tests forced reasoning (Tier-5: chain-of-thought, code-as-reasoning, self-correction) on ciphertext alone. A 10-configuration ablation study on 7,000 files, using a single 70/30 train-test split for feature-removal analysis, provides additional evidence at scale. Live AP...
  </details>

- **2026-09-22** — Robert W. Learsch, Nicholas Liesen, Daniel S. Levine et al. — [An open benchmark for machine learning-based polymer property prediction](http://arxiv.org/abs/2609.27036v1)
  <details><summary>📄 Abstract</summary>
  Polymer property prediction lacks open, standardized benchmarks that enable rigorous comparison of machine-learning methods, with existing resources covering only a narrow fraction of polymer architectures, such as homopolymers. We introduce Polymer Benchmark 2026 (PolyBench26), an open dataset comprising nearly 250,000 polymer-property datapoints across eight physical properties, including data from experimental measurements, density functional theory, and molecular dynamics. The benchmark supp...
  </details>

- **2026-09-22** — Qingjing Chen, Junkai Zhang, Shaochun Wang et al. — [LEGO: Synergizing Expert GraphRAG and Expert Chain-of-Thought for Legal Reasoning](http://arxiv.org/abs/2609.27009v1)
  <details><summary>📄 Abstract</summary>
  Large language models are increasingly applied to high-risk domains such as law, yet complex legal reasoning remains limited by two structural challenges. First, existing RAG and GraphRAG methods emphasize lexical or semantic similarity while overlooking normative relations among legal provisions. Second, vanilla Chain-of-Thought prompting may generate plausible rationales without enforcing the normative structure of legal reasoning. To deal with the bottleneck of pipelines in the legal reasonin...
  </details>

- **2026-09-22** — Edem Ahadzi, Ruchi Pandey, Tomi H. Kinnunen — [A Temporal-Envelope Frontend with Learnable Per-Channel Energy Normalization for Whisper-Based Children's ASR](http://arxiv.org/abs/2609.26937v1)
  <details><summary>📄 Abstract</summary>
  Temporal envelopes carry cues critical to speech intelligibility, yet ASR frontends based on log-mel spectrograms do not explicitly model continuous sub-band envelope structure. This limitation is particularly acute for children's speech, where high acoustic variability demands robust feature representations. We propose a modular time-domain frontend that decomposes speech into sub-band envelopes using mel-spaced windowed-sinc filters and the Hilbert transform, with learnable per-channel energy ...
  </details>

- **2026-09-22** — Zeyu He, Zhuqian Zhou, Kirk Vanacore et al. — [Experts Rise Where LLMs Disagree: Using Cross-Model Disagreement to Target Expert Effort in LLM Codebook Revision for Large-Scale Annotation](http://arxiv.org/abs/2609.26926v1)
  <details><summary>📄 Abstract</summary>
  Large-scale text annotation brings expert insight to millions of documents, often through a codebook that AI annotators follow. Developing a robust codebook, however, takes months. Large language models (LLMs) could speed this process by applying an early codebook to the data, surfacing cases with strong LLM disagreement, and eliciting expert feedback to address them. We examined three ways experts can provide feedback for LLM codebook revision: (i) editing LLM-generated revisions driven by cros...
  </details>

- **2026-09-22** — Mengtao Ou, Zongzheng Zhang, Zhenghao Xiao et al. — [MSK-Bench: Benchmarking Full-Body Musculoskeletal Motor Control Across Tasks, Control Paradigms, and Physiological Metrics](http://arxiv.org/abs/2609.26872v1)
  <details><summary>📄 Abstract</summary>
  Musculoskeletal (MSK) humanoids provide a physiologically grounded embodiment for studying full-body motor control, but their high-dimensional muscle actuation, delayed activation dynamics, and redundant muscle--tendon structures make learning substantially harder than torque-driven humanoid control. Existing MSK benchmarks remain fragmented across gait, prosthetics, dexterous hands, or challenge-specific tracks, leaving full-body muscle-actuated control insufficiently evaluated under standardiz...
  </details>

- **2026-09-22** — Sinuo Wang, Zichong Gu, Yuhan Huang et al. — [ForeDrive: Foresight-Guided End-to-End Autonomous Driving with a Planning-Relevant Latent World Model](http://arxiv.org/abs/2609.26299v2)
  <details><summary>📄 Abstract</summary>
  Existing latent world models are typically optimized for future predictability, yet the resulting representations are not necessarily useful for planning in autonomous driving. Predictions are commonly used for pretraining or auxiliary supervision rather than as direct conditioning signals for trajectory generation. We propose ForeDrive, which learns a planning-relevant latent representation and couples it asymmetrically to a Diffusion Transformer (DiT) planner. The planner consumes multi-horizo...
  </details>

- **2026-09-22** — Woojin Chae, Ezinne Nwankwo, Haitong Qin et al. — [Optimal Sequential Annotations for Off-Policy Evaluation](http://arxiv.org/abs/2609.26707v1)
  <details><summary>📄 Abstract</summary>
  Offline reinforcement learning and off-policy evaluation evaluates dynamic treatment rules based on retrospectively collected data prior to deployment. In recent AI applications, state and reward information is recorded as complex text or image, which recent AI advancements such as LLM-as-a-judge can label with unknown bias. Expert annotation may be available but at a higher cost. For example, safety classification via cheap but imperfect classifiers vs. expensive expert review. We show how a li...
  </details>

- **2026-09-22** — Brandon Bauer, Matthew Whalen, Kenji Watanabe et al. — [Autonomous Quantum Transport Measurements of 2D Semiconductors by an AI Agent](http://arxiv.org/abs/2609.26661v1)
  <details><summary>📄 Abstract</summary>
  Artificial-intelligence (AI) agents are beginning to enter experimental laboratories, automating experiments and accelerating scientific discovery. Herein, we introduce an AI-driven workflow in which an AI agent performs multi-step, multi-day quantum transport measurements end-to-end. Specifically, given brief instructions, the agent starts by planning the multi-step measurements, then safely operates the cryogenic instruments, analyzes the data, and concludes with a final report. We demonstrate...
  </details>

- **2026-09-22** — Xiao Tang, Tong Hui, Chao Shen et al. — [Unlocking Cross-Scenario Physical Layer Security: A Mixture-of-Experts Framework with Generative Diffusion Models](http://arxiv.org/abs/2609.26598v1)
  <details><summary>📄 Abstract</summary>
  The future 6G networks are expected to incorporate a proliferation of wireless services in diverse environments, which presents a significant challenge for information security. Conventionally optimization always requires recalculation and learning strategy often suffers poor generalization, which are thus incapable for the security provisioning with wide scenario coverage. In this paper, we propose an adaptive and robust learning framework that leverages a mixture-of-experts (MoE) architecture ...
  </details>

- **2026-09-22** — Zhiyun Jiang, Hanyong Wang, Binbin Liang et al. — [Combining Hierarchical Cognitive Process with Process Supervision for Interpretable Scene Safety Understanding](http://arxiv.org/abs/2609.26399v1)
  <details><summary>📄 Abstract</summary>
  Scene safety understanding plays a life-or-death role in situational awareness in various critical domains. Traditional methods that rely on learning direct mappings between scenes and safety levels often lack interpretability, limiting their reliability in critical applications. An effective approach to overcoming this challenge lies in interpreting human cognitive processes and equipping machine models with analogous cognitive capabilities. This work explores an effective way of integrating sc...
  </details>

- **2026-09-22** — Nikita Agarwal, Nivedit Jain — [FIRE: Failure-Informed Runtime Engineering for Reliable Language-Model Agents](http://arxiv.org/abs/2609.26048v1)
  <details><summary>📄 Abstract</summary>
  Language-model agents often reach a working solution and then fail to consistently deliver it. We study runtime policies: targeted natural-language instructions and action denials applied by the agent harness at states that preceded observed failures, without changing model weights or the user prompt. With this, keeping capability constant, we observe a meaningful unlock in delivered reliability. Across the complete 87-task Terminal-Bench 2.1 suite, with two attempts per task, policies increase ...
  </details>

- **2026-09-22** — Pietro Talli, Petar Popovski, Osvaldo Simeone — [Risk-Aware Online Conformal State Probing](http://arxiv.org/abs/2609.25889v1)
  <details><summary>📄 Abstract</summary>
  AI-based autonomous agents, typically hosted at data centers, must acquire state information from robots or edge devices in order to issue informed control decisions. Managing uncertainty about the state is particularly consequential in safety-critical settings, in which average-case guarantees are insufficient. In this context, we study a sequential decision maker process that jointly decides which actions to take and when to probe given access to an arbitrary state prediction model. We propose...
  </details>

- **2026-09-22** — Hung-Mao Chen, Xu He, Bo Lu et al. — [C-to-Rust Fallacy: Automatic Refactoring != Memory Security](http://arxiv.org/abs/2609.25682v1)
  <details><summary>📄 Abstract</summary>
  Rust has emerged as the leading system programming language, offering strong memory and type safety guarantees without compromising performance. This positions it as a compelling alternative to traditional languages like C and C++, which are susceptible to memory security bugs. However, manually transforming C to Rust requires in-depth domain knowledge of the Rust language features, which requires significant effort for developers. To address this, tools for automatic C-to-Rust refactoring aim t...
  </details>


### 📂 watermark
*水印与溯源 / Watermarking & Provenance* — 15 papers

- **2026-09-24** — Dipankar Sarkar — [How Reproducible Are Evaluation Conclusions? A Self-Audit of LLM-Inferred Prompt Structure](http://arxiv.org/abs/2609.30074v1)
  <details><summary>📄 Abstract</summary>
  Evaluations of LLM systems routinely average over small prompt sets and report models as a ranked table. We ask how much confidence such a table deserves, using LLM-based prompt-structure inference as the case study: eight open model variants across five families and 8B to 675B parameters, caching disabled, 293 raw intermediate representations persisted. The measured phenomenon is unstable to begin with. Identical calls do not reliably recover identical structure, with mean node-set Jaccard from...
  </details>

- **2026-09-24** — Theresa Dahl Frehr, Francisco Pelayo, Lukas Raad et al. — [Learnable Time-Frequency Masks for Explaining Time-Series Classifiers](http://arxiv.org/abs/2609.29270v1)
  <details><summary>📄 Abstract</summary>
  Time-series explainability remains challenging because discriminative information is often encoded in latent frequency or time-frequency features rather than in the raw signal itself. Existing attribution methods typically operate either in the time domain or in a fixed transform domain, limiting their ability to capture salient information across different representations. We propose XACT, a general framework that learns sparse attribution masks over coefficients from arbitrary invertible time-...
  </details>

- **2026-09-23** — Hector Ouilhet Olmos — [The Interface Is Downstream: Designing the Terms of Human-Agent Collaboration](http://arxiv.org/abs/2609.28801v1)
  <details><summary>📄 Abstract</summary>
  Before an agent responds or acts, much of the experience has already been designed. Memory and retrieval shape what it notices. Evidence rules shape what it may claim. Permissions shape what it can do. Learning rules shape what it carries into the next encounter.   The argument comes from Alicia, a personal agent I've built and used since January 2026. A fine-tuning pilot produced no defensible model-performance result. It exposed a provenance failure: Alicia repeated an interpretation from a re...
  </details>

- **2026-09-23** — Jinqian Zhang, Haojun Xia, Shujiang Wu et al. — [Agent Approval Laundering: Transitive Effects Beyond the Approved Invocation](http://arxiv.org/abs/2609.28586v1)
  <details><summary>📄 Abstract</summary>
  Coding-agent approval interfaces bind a human decision to a command or tool call, while developer tools execute the transitive workflow that invocation activates. Package installation can run lifecycle hooks and write files; an MCP call can exercise network authority. We call the resulting record-coverage failure approval laundering: the durable record names the entry invocation but omits effects exercised by its workflow.   We present the first systematic security analysis of this record-to-clo...
  </details>

- **2026-09-23** — Chuyi Wang, Xiaohui Xie, Tongze Wang et al. — [Who Is Behind the Harness? Fingerprinting LLMs through Agentic Behavior](http://arxiv.org/abs/2609.28559v1)
  <details><summary>📄 Abstract</summary>
  LLMs increasingly operate through coding-agent harnesses that inspect repositories, invoke tools, and modify files. Substituting the model behind such an agent can therefore change security-relevant decisions, including whether it verifies changes or recovers safely from failures. Existing LLM fingerprints largely infer identity from direct text or token distributions. In coding agents, these signals are mediated by system instructions, controller logic, tools, and execution feedback, limiting t...
  </details>

- **2026-09-23** — Mateusz Zych, Vasileios Mavroeidis, Gudmund Grov — [CCR: Towards a Common, Quality-Gated CACAO Integrations Registry for European Cybersecurity Automation](http://arxiv.org/abs/2609.27567v2)
  <details><summary>📄 Abstract</summary>
  Standardised, machine-readable cybersecurity playbooks provide a basis for portable, shareable, and reusable incident-response logic. OASIS CACAO provides a vendor-neutral representation for such playbooks, but not the product-specific integration artefacts needed to invoke external products and services. We introduce the Common CACAO Registry (CCR), an open, provenance-aware registry of CACAO HTTP-API connector envelopes. Each envelope captures an API operation's command, inputs, target, authen...
  </details>

- **2026-09-23** — Mateusz Zych, Vasileios Mavroeidis, Gudmund Grov — [CCR: Towards a Common, Quality-Gated CACAO Integrations Registry for European Cybersecurity Automation](http://arxiv.org/abs/2609.27567v1)
  <details><summary>📄 Abstract</summary>
  Standardised, machine-readable cybersecurity playbooks provide a basis for portable, shareable, and reusable incident-response logic. OASIS CACAO provides a vendor-neutral representation for such playbooks, but not the product-specific integration artefacts needed to invoke external products and services. We introduce the Common CACAO Registry (CCR), an open, provenance-aware registry of CACAO HTTP-API connector envelopes. Each envelope captures an API operation's command, inputs, target, authen...
  </details>

- **2026-09-23** — Xuanyu Meng, Xing Fan, Xinyi Fan et al. — [EnSIMem: Entity-Structured Indexing for Long-Term Agent Memory](http://arxiv.org/abs/2609.27279v1)
  <details><summary>📄 Abstract</summary>
  An agent that interacts with users over long periods must recall facts, preferences, events, and changes from a continuously growing interaction history. Existing memory systems often compress interactions into generic summaries or retrieve anonymous text chunks, making it difficult for an agent to identify the correct entity, property, and supporting evidence. We present EnSIMem, an entity-structured long-term memory architecture for an agent. During offline construction, the system organizes i...
  </details>

- **2026-09-23** — Liangyu Li, Michael White — [Motif-Vocab: StatisticallyCalibrated Transcription-Factor-Identity Tokenization forGenomic Language Models](http://arxiv.org/abs/2609.28386v1)
  <details><summary>📄 Abstract</summary>
  Tokenization is a central design choice in genomic language models, yet most deoxyribonucleic acid (DNA) tokenizers use characters, fixed-length k-mers, or frequency-derived subwords without explicitly using prior information about the specificity of DNA-binding regulatory factors. We introduce Motif-Vocab, a biologically informed tokenizer that scans both DNA strands for statistically calibrated motif matches, emits transcription-factor (TF) identity tokens, and applies nucleotide, $k$-mer, or ...
  </details>

- **2026-09-23** — Walter Kurz, Reinhard Magg — [Compliant AI Infrastructure for Regulated Finance: A tiered multi-agent framework with DLT audit trails for financial operations in DACH](http://arxiv.org/abs/2609.27632v1)
  <details><summary>📄 Abstract</summary>
  We present a compliance-first architecture for AI in regulated finance that treats regulation as an orientation layer rather than a deterministic ruleset. A matrix of regulatory intent and exposure provides a compact classification handle, which a governed policy compiler then maps into concrete prohibitions, obligations and runtime budgets. Prohibitions constrain feasibility and block externalisation, while obligations extend tasks with artefacts that must meet explicit admissibility criteria. ...
  </details>

- **2026-09-23** — Hengyu Li — [KITE: Scaling Jev Population Experiments with Sparse Flagship Calibration](http://arxiv.org/abs/2609.27535v1)
  <details><summary>📄 Abstract</summary>
  KITE queries a typed behavioral kernel once per unique state, then executes populations of any size from the table with event-keyed randomness and common random numbers. An expensive flagship model is reserved for sparse paired anchors that estimate intervention effects. Measured human-model discrepancy is propagated as shared error into every conclusion. Population-experiment cost thus scales with unique states and anchors, while uncertainty is governed by evidence about people rather than Mont...
  </details>

- **2026-09-23** — Haoluan Fu, Keni Chen, Xinyu Jia et al. — [Emergi-PersonaOS: A Persona Agent Operating System for Situational Adaptation and Controllable Evolution](http://arxiv.org/abs/2609.27417v1)
  <details><summary>📄 Abstract</summary>
  Symbiosis between humans and digital beings offers a vision for the future of human--machine interaction. In enduring human--machine relationships, personality provides a foundation for continuity of identity, individuality in interaction, and development through experience. We investigate this capacity through persona agents as computational implementations and introduce Emergi-PersonaOS, a psychology-grounded operating system for managing persona objects throughout their lifecycle. The system ...
  </details>

- **2026-09-22** — Anchit Mishra — [When Direct Manipulation Becomes a Guess: Productive Friction in AI-Mediated Multisensory Visualization](http://arxiv.org/abs/2609.27104v1)
  <details><summary>📄 Abstract</summary>
  Generative visualization increasingly embeds large language models within direct manipulation and multisensory interaction. Speech, gaze, touch, gesture, sound, and haptics can make probabilistic inference feel like familiar, deterministic tool use. I call this gap a deterministic-affordance mismatch: deterministic interaction cues persist while AI weakens predictability, locality, reversibility, or provenance. Reading the malleable interfaces of Iron Man 2 against systems from Blade Runner 2049...
  </details>

- **2026-09-22** — Haobo Zheng, Tan Tang, Yan Chen et al. — [SpeakerMem-R1: Speaker-Centered Dual-Track Memory for Multi-Party Dialogue](http://arxiv.org/abs/2609.26780v2)
  <details><summary>📄 Abstract</summary>
  Long-term conversational memory in multi-party settings requires more than retrieving relevant content from long-term conversations: it must distinguish who said what, whom each statement concerns, how individuals perceive one another, what information is shared by the group, and how states change over time. Recent studies on multi-party dialogue benchmarks show that existing general-purpose LLM memory systems tend to lose person and group relations or struggle to integrate clues distributed acr...
  </details>

- **2026-09-22** — Yiqi Wang, Jinqian Ju, Jiaqi Zhang et al. — [When Does Execution Provenance Help Agent Memory Retrieval?](http://arxiv.org/abs/2609.25913v1)
  <details><summary>📄 Abstract</summary>
  A language agent's execution history can exceed its context window, requiring its memory system to retrieve complete supporting evidence under a hard token budget. Evidence may span multiple execution events, yet conventional retrievers use fixed token windows and fixed-k metrics that reward individual fragments without showing whether the complete evidence set fits in context. Smaller windows reduce irrelevant text but scatter evidence across candidates, while flat-versus-graph comparisons can ...
  </details>


### 📂 unlearning
*机器遗忘 / Machine Unlearning* — 1 papers

- **2026-09-22** — Jin Liu, Yanzhong He, Guancheng Lin et al. — [What Was Once Learned May Need to Be Unlearned: Machine Unlearning for Deprecated API Knowledge in Large Language Models](http://arxiv.org/abs/2609.25786v1)
  <details><summary>📄 Abstract</summary>
  Large language models (LLMs) for code completion may generate deprecated APIs because their pre-training corpora contain code from historical library versions. Existing approaches use inference-time intervention, model editing, or machine unlearning, but multiple plausible completions make predefined replacements restrictive. Moreover, existing studies rarely verify whether models exhibit the targeted deprecated behavior or evaluate unintended changes to other APIs.   We conduct a systematic emp...
  </details>


### 📂 survey
*综述与系统化 / Surveys & Systematization* — 4 papers

- **2026-09-24** — Rahul Khedar, Mayank Malhotra, Avinash Karn — [Augur: A Synthetic Decision Lab for Rehearsing Reactions to Product and Policy Changes](http://arxiv.org/abs/2609.29952v1)
  <details><summary>📄 Abstract</summary>
  Before a product or policy change ships, the question that matters is how people will react to it. Augur rehearses that reaction offline: it builds a typed knowledge graph from the change documents, populates a grounded persona market, simulates the interaction, and returns an auditable decision memo recommending one of five actions. We assemble Gold-50, fifty real product and policy episodes whose real-world outcome is known, adjudicated against the public record, and score the five-way release...
  </details>

- **2026-09-23** — Olivia Venot, Yamila Miguel, Robin Baeyens et al. — [Probing Exoplanetary Chemistry with Ariel: Scientific Priorities and Observational Strategies](http://arxiv.org/abs/2609.27622v1)
  <details><summary>📄 Abstract</summary>
  Over the past two decades, increasingly precise observations have revealed that exoplanet atmospheres are chemically diverse and often far from equilibrium, with processes such as vertical mixing, photochemistry, and atmospheric circulation producing significant departures from thermochemical expectations. As large surveys across a wide range of planets begin to uncover population-level chemical trends, a coherent interpretation of these patterns remains elusive, particularly for gas giants and ...
  </details>

- **2026-09-22** — Varshini Elangovan, James Wedgwood, Chhavi Yadav et al. — [Safety Nudges: User-Facing Interventions for Real-Time AI Risk Awareness](http://arxiv.org/abs/2609.26865v2)
  <details><summary>📄 Abstract</summary>
  Conversational AI systems can pose safety risks to their users such as hallucination, sycophancy, overconfidence, and anthropomorphism, but these risks are difficult for users to detect during everyday use. We introduce Safety Nudges, a browser-based tool that provides lightweight, in situ flags when concerning behavior is detected in chatbot conversations. We evaluated Safety Nudges in a two-week field study with 45 frequent chatbot users, collecting interaction logs, surveys, and feedback on i...
  </details>

- **2026-09-22** — Varshini Elangovan, James Wedgwood, Chhavi Yadav et al. — [Safety Nudges: User-Facing Interventions for Real-Time AI Risk Awareness](http://arxiv.org/abs/2609.26865v1)
  <details><summary>📄 Abstract</summary>
  Conversational AI systems can pose safety risks to their users such as hallucination, sycophancy, overconfidence, and anthropomorphism, but these risks are difficult for users to detect during everyday use. We introduce Safety Nudges, a browser-based tool that provides lightweight, in situ flags when concerning behavior is detected in chatbot conversations. We evaluated Safety Nudges in a two-week field study with 45 frequent chatbot users, collecting interaction logs, surveys, and feedback on i...
  </details>


### 📂 other
*其他安全相关 / Other Security-Related* — 177 papers

- **2026-09-24** — Edwin Clatus, Madhusudan Singh — [A Lightweight Ethereum Voting Prototype for Hospital Ethics Committees with Receipt-Based Inclusion Verification](http://arxiv.org/abs/2609.29981v1)
  <details><summary>📄 Abstract</summary>
  This paper presents a Solidity, Hardhat, React, MetaMask, and ethers.js prototype for hospital ethics committee voting. Role controls, case-state checks, duplicate vote controls, and a receipt hash support public audit and transaction inclusion verification. Because vote events expose wallet addresses and vote values, the design provides pseudonymous auditability, not anonymous or secret-ballot voting; the receipt is neither receipt-free nor coercion-resistant. Evaluation reports 22 passing func...
  </details>

- **2026-09-24** — Mehmet Iscan — [Requirement-Bound Verified Commissioning: A Frozen Four-Billion-Parameter Local Model as a Candidate Generator under an External Acceptance Layer with Verification and Release Authority](http://arxiv.org/abs/2609.30219v1)
  <details><summary>📄 Abstract</summary>
  An acceptance protocol is developed for sensor-coordinate and polarity binding in mechatronic commissioning. Candidate generation is separated from release authority. Requirements unsupported by a deterministic parser are routed to a frozen local language model with four billion parameters. Plans are released only when both facts can be derived by an external gate under a sealed grammar. One canonical answer is requested from a gold-standard user when eligible. The protocol was evaluated once un...
  </details>

- **2026-09-24** — Andreas E. Robertson, Ashley T. Lenau, John D. Shimanek et al. — [Beyond Compression: Training Latent Representations for Stable Long-Horizon Rollout in Neural Surrogate Solvers](http://arxiv.org/abs/2609.30198v1)
  <details><summary>📄 Abstract</summary>
  Latent neural surrogate solvers, or latent dynamics models, accelerate simulations of time-dependent physical systems by evolving a compressed latent space rather than resolving full-resolution fields directly. In principle this reduces computational cost and simplifies learning, but in practice errors often accumulate rapidly during long autoregressive rollouts, limiting predictive utility. We show that this instability does not stem from the latent representation itself, but arises when it is ...
  </details>

- **2026-09-24** — Tianyu Feng, Haoxuan Yu, Tianyuan Wu et al. — [KREX: Concurrent Kernel Benchmarking on Shared GPUs via Region-Granular Exclusivity](http://arxiv.org/abs/2609.30057v1)
  <details><summary>📄 Abstract</summary>
  LLM agents automate GPU kernel optimization by repeatedly composing candidates and measuring their duration on real GPUs. Existing systems preserve measurement fidelity by reserving a GPU for an entire agent session or benchmarking command. However, this results in poor utilization because only a small fraction of command execution requires exclusive GPU access. Sharing GPUs could recover this idle capacity, but introduces contention that compromises measurement fidelity and misdirects the agent...
  </details>

- **2026-09-24** — Yang Zhou, Jiuhong Xiao, Shizhao Ye et al. — [M3GD: Multi-Modal Multi-View Geometric Diffusion for Camera--LiDAR Novel View Synthesis](http://arxiv.org/abs/2609.30056v1)
  <details><summary>📄 Abstract</summary>
  Robotic novel view synthesis (NVS) must recover both visual appearance and metric 3D structure, yet most generative NVS methods rely only on images, overlooking LiDAR, a complementary sensor common on robotic platforms. We present M3GD, a Camera--LiDAR multimodal representation for generative NVS that composes independently pretrained 2D image and 3D point-cloud foundation models without separately pretraining a cross-modal translator. We show that, after camera projection, frozen LiDAR and imag...
  </details>

- **2026-09-24** — Xuanyu Li — [Isolated singularities of harmonic maps with generic boundary data](http://arxiv.org/abs/2609.29994v1)
  <details><summary>📄 Abstract</summary>
  We study the behavior of isolated singularities of stationary harmonic maps with generic boundary data. For round sphere targets, we prove that, for $4\leqslant n\leqslant7$, every stable stationary harmonic map from a bounded smooth $n$-dimensional domain to round $(n-1)$-sphere with generic smooth boundary data has only radial projections composed with orthogonal transformations as tangent maps at its singularities; for 7-dimensional domains and round $k$-sphere targets with $k\geqslant7$, eve...
  </details>

- **2026-09-24** — Mengdan Zhu, Yufan Zhao, Sophie Di et al. — [Learning Better Reasoning for Generative Recommendation with Semantic IDs](http://arxiv.org/abs/2609.29973v1)
  <details><summary>📄 Abstract</summary>
  Generative recommendation reformulates item retrieval as sequence generation, allowing a unified model to directly generate the next item from a user's interaction history. Semantic IDs further make this paradigm effective and scalable by representing each item as discrete codes, enabling knowledge sharing among semantically related items. Recent studies introduce explicit reasoning before Semantic-ID generation, helping models summarize user interests and infer possible preference transitions. ...
  </details>

- **2026-09-24** — Xun Huang, Shijia Zhao, Rongsheng Qu et al. — [Beyond Spatial Benchmarks: From Spatial Reasoning to Navigation](http://arxiv.org/abs/2609.29934v1)
  <details><summary>📄 Abstract</summary>
  Does progress on spatial reasoning benchmarks translate into better navigation? Existing benchmarks test isolated inferences from images or videos, with little connection to downstream navigation. Our analysis reveals a gap between benchmark-oriented spatial specialization and navigation performance, and shows how aligning spatial supervision with navigation goals, phases, and decision learning improves navigation. Guided by these findings, we build \textsc{Spatial-Nav-100K} and fine-tune in two...
  </details>

- **2026-09-24** — Shih-Hong Chen, Josh Jia-Ching Ying, Vincent S. Tseng — [LSF-SR: Latent Semantic Fusion for Sequential Recommendation via Flow-based Conditional Variational Autoencoders](http://arxiv.org/abs/2609.29815v1)
  <details><summary>📄 Abstract</summary>
  Sequential recommendation aims to predict users' future interests from their historical interactions. Although Large Language Models (LLMs) capture rich item semantics, existing methods often struggle to align collaborative signals with textual semantic knowledge. As a result, the learned item representations fail to capture the complementary strengths of both signals, leading to suboptimal recommendation quality. To address this limitation, we propose Latent Semantic Fusion for Sequential Recom...
  </details>

- **2026-09-24** — Shubham Kale, Aniketh Garikaparthi, Manasi Patwardhan — [Learning to Ideate for Scientific Impact](http://arxiv.org/abs/2609.29802v1)
  <details><summary>📄 Abstract</summary>
  Scientific ideation is increasingly mediated by large language models, but current ideation systems are usually trained and evaluated on immediately judgeable proxies such as novelty, clarity, and feasibility. This leaves open whether delayed signals of scientific uptake can be used as feedback for steering models toward research directions with higher expected \emph{impact}. We study this question using citation-normalized impact as a noisy but scalable proxy for scholarly uptake. We construct ...
  </details>

- **2026-09-24** — Xinyue Wang, Jiacheng Pang, Kun Zhou et al. — [TimeBraid: Unifying Time Series and Language for Understanding and Forecasting](http://arxiv.org/abs/2609.29792v1)
  <details><summary>📄 Abstract</summary>
  We present TimeBraid, a series of unified time-series and language models that align pretrained language models and pretrained time-series foundation models through interleaved global residual attention layers. Each model inherits knowledge, instruction following, and reasoning from one side, continuous-signal perception and zero-shot forecasting from the other, and fuses the two in a shared representation space where both modalities are understood and generated. We study the design choices that...
  </details>

- **2026-09-24** — Jiajun Wu, Leixin Sun, Zihan Tan et al. — [SWE-PolyVision: Benchmarking Cross-Image Abductive Reasoning for Repository-Level Software Engineering](http://arxiv.org/abs/2609.29754v1)
  <details><summary>📄 Abstract</summary>
  Current multimodal software-engineering benchmarks expose images as additional context, but do not test whether an agent can integrate evidence distributed across images into a verified repository-level repair. We present SWE-PolyVision, an executable benchmark of 92 real tasks from 36 open-source organizations, with 48 public tasks and 44 private holdouts. The release contains 402 static images and 6 videos, with at least two visual inputs per task. Each task pairs a fixed pre-fix repository wi...
  </details>

- **2026-09-24** — Jiajun Wu, Leixin Sun, Zihan Tan et al. — [SWE-Prometheus: Measuring Engineering Governance Improvements in Real-World Repositories](http://arxiv.org/abs/2609.29465v1)
  <details><summary>📄 Abstract</summary>
  Large language model based coding agents have made substantial progress on repository-level software engineering tasks. Existing repository benchmarks, however, usually start from a human-identified issue and evaluate whether a patch satisfies a functional signal. We present SWE-Prometheus, a benchmark for the broader task of improving repository engineering governance. Each task provides a fixed snapshot and an open-ended objective, requiring the agent to identify risks, prioritize intervention...
  </details>

- **2026-09-24** — Alessandro Bondielli, Lucia Passaro, Serena Auriemma et al. — [Parts-of-Speech as Emergent Categories in SAE Latent Space](http://arxiv.org/abs/2609.29362v1)
  <details><summary>📄 Abstract</summary>
  Sparse AutoEncoders (SAEs) offer a promising way to inspect language model representations, but it is still unclear what kind of linguistic structure their latents expose. We use part-of-speech (PoS) categories as a controlled test case to study whether morpho-syntactic information is encoded by individual latents or by structured groups of features. We find that PoS distinctions are highly recoverable from SAE activations, but do not align with one-to-one latent / category mappings. This recove...
  </details>

- **2026-09-24** — Omar Adjali, Siting Liang, Omair Shahzad Bhatti et al. — [EAGER: Enhancing Generative Event Extraction via Reinforcement Learning with Verifiable Rewards](http://arxiv.org/abs/2609.29230v1)
  <details><summary>📄 Abstract</summary>
  End-to-end event extraction remains challenging for large language models as it requires simultaneous identification of event triggers, classification of event types, and extraction of schema-grounded argument spans. We present EAGER, a reinforcement learning framework for generative event extraction that combines fine-grained verifiable rewards with Schema-Contrastive Advantage Estimation to alleviate advantage collapse under sparse binary rewards. Our reward design explicitly targets structura...
  </details>

- **2026-09-24** — Zhenyu Ma, Xukai Jiang — [PRAXIS-VirtualCell: A Programmable and Trustworthy Framework for Agentic Virtual Cell Experiments](http://arxiv.org/abs/2609.29221v1)
  <details><summary>📄 Abstract</summary>
  Virtual cells are evolving from single-task predictive models toward programmable biological simulation systems, yet heterogeneous data, models, and validation evidence still lack a unified organizational framework. Here, we present PRAXIS-VirtualCell, a modular framework that organizes biological data, predictive models, perturbations, adapters, execution environments, and validation evidence to enable reproducible and auditable virtual experiments. The system supports cross-species tasks spann...
  </details>

- **2026-09-24** — Chenglei Shen, Chenzhe Huang, Dong Jiang et al. — [X-Rec Technical Report](http://arxiv.org/abs/2609.29180v1)
  <details><summary>📄 Abstract</summary>
  Recent advances in generative modeling have reshaped recommender systems by formulating recommendation as a next-item generation problem. Existing retrieval approaches primarily follow two paradigms: user-to-item (U2I) methods represent user context using one or a few deterministic embeddings, which limits the ability to capture diverse and multi-mode interests, while semantic-ID-based autoregressive (SID-AR) methods model more expressive distributions but suffer from quantization errors and the...
  </details>

- **2026-09-24** — Nidhya Shivakumar, Ethan Ransing, Josh Zhang et al. — [TRACE: Interactive Bi-Directional Tracing of Monochrome Cables Amid Clutter](http://arxiv.org/abs/2609.29103v1)
  <details><summary>📄 Abstract</summary>
  Accurate state estimation (tracing) of Deformable Linear Objects (DLOs) such as cables is a critical challenge for data centers, manufacturing, construction, homes, and surgery, where precise cable management directly impacts operational safety and efficiency. However, resolving the state of multiple monochrome cables amid foreground and background clutter poses challenges due to occlusions, overlap, and ambiguous crossings. We present Two-way Routing And Cable Estimation (TRACE), which combines...
  </details>

- **2026-09-24** — Shamanthak Hegde, Xiangrui Liu, Maitreya Patel et al. — [Where Hallucinations Live: A Cross-Architecture Circuit in VQ-Tokenized Vision-Language Models](http://arxiv.org/abs/2609.29048v1)
  <details><summary>📄 Abstract</summary>
  Unified vision-language models (VLMs) that tokenize images through a vector-quantized (VQ) codebook routinely hallucinate objects on grounded yes/no benchmarks, yet existing decoding-time fixes treat this as generic miscalibration without an architectural account. Using activation patching across twenty-five models spanning eight LLM families, we identify an early-layer ($L_0$) attention routing circuit shared across VQ-tokenized VLMs and propose a three-gate diagnostic that distinguishes the mo...
  </details>

- **2026-09-24** — Keru Chen, Sen Lin, Yingbin Liang et al. — [MeshHeal: Two-Timescale Self-Healing for Gray Failures in Decentralized LLM Agent Networks](http://arxiv.org/abs/2609.29015v1)
  <details><summary>📄 Abstract</summary>
  Decentralized LLM-based multi-agent systems coordinate through local interactions, but an agent can remain responsive while its task-solving quality persistently degrades. Such gray failures require protecting current tasks before sufficient evidence exists to alter future routing, while still allowing recovered agents to rejoin. We introduce MeshHeal, a fully decentralized self-healing framework that couples ability-matched peer review across two timescales. At the fast timescale, an adaptive h...
  </details>

- **2026-09-24** — Yuyao Liu, Jiayuan Mao, David Hsu et al. — [RAPID: Robot Agentic Programming from Demonstrations](http://arxiv.org/abs/2609.30249v1)
  <details><summary>📄 Abstract</summary>
  Coding agents have demonstrated enormous success in solving complex programming problems. To leverage their potential for robot systems, this work introduces Robot Agentic Programming from Demonstrations (RAPID), which automatically generates, verifies, and refines robot programs, given a single visual human demonstration. The iterative agentic loop of code refinement requires several key ingredients: (i) a testable task specification, (ii) action primitives for robot execution, and (iii) an int...
  </details>

- **2026-09-24** — Namiko Saito, Hiroshi Kera — [Body-Grounded Replanning for Physically Adaptive Manipulation](http://arxiv.org/abs/2609.30024v1)
  <details><summary>📄 Abstract</summary>
  Manipulation requires not only reasoning about the external environment, but also about the robot's physical condition. A strategy may remain geometrically feasible while becoming physically unsuitable due to increased joint load or limited mobility, yet internal physical state is typically used only for low-level control. We propose body-grounded high-level replanning, which uses internal physical state to adapt manipulation strategies during execution. Body-state events trigger strategy replan...
  </details>

- **2026-09-24** — Mariia Iavorskaia, Christian Dietz, Sebastian Albrecht et al. — [Res-HIL: Human-Guided Residual Reinforcement Learning for Sample-Efficient Dexterous Manipulation](http://arxiv.org/abs/2609.30023v1)
  <details><summary>📄 Abstract</summary>
  Imitation learning enables robots to acquire manipulation skills from demonstrations, but the resulting policies can fail outside the training data, while collecting more demonstrations requires substantial human effort. Human-in-the-loop reinforcement learning uses corrective feedback during online training, but typically learns the complete task policy rather than refining a pretrained imitation policy. We introduce Res-HIL, a human-in-the-loop residual reinforcement learning framework that le...
  </details>

- **2026-09-24** — Yehang Zhang, Haojian Huang, Yifan Chang et al. — [World Action Agent: Harnessing VLMs for Robot Manipulation via World Action Rehearsal](http://arxiv.org/abs/2609.29964v1)
  <details><summary>📄 Abstract</summary>
  General-purpose vision-language models (VLMs) bring broad knowledge and spatial reasoning to robot manipulation, yet existing systems either use them indirectly, to predict constraints or write programs, or give them a view of the scene rather than a world in which to act. We present World Action Agent (WAA), a multi-agent harness through which VLMs pilot robots with basic tools, making every decision within a visual action workspace. The workspace has three properties. Contact views, selected a...
  </details>

- **2026-09-24** — Yiran Ding, Wenwei Xu — [ARIS: Low-Resource Glass-Box Neural Source-Filter Synthesis for Phonetic Stimulus Manipulation](http://arxiv.org/abs/2609.29923v1)
  <details><summary>📄 Abstract</summary>
  Phoneticians often need to construct stimuli in which specific acoustic cues are precisely manipulated while preserving decent speech quality. Classical synthesis and modern neural methods sit along a trade-off between precise parametric control and high fidelity, and neural synthesis typically demands more data than phoneticians can easily obtain. We present ARIS (Analytic Resonant Interpretable Synthesis), a neural source-filter model that pairs neural parameter estimation with deterministic D...
  </details>

- **2026-09-24** — Zexi Li, Yehang Zhang, Wenqian Li et al. — [Robo-Harness K1: Harnessing Robot-Use Agents via Perception Augmentation](http://arxiv.org/abs/2609.29389v1)
  <details><summary>📄 Abstract</summary>
  Foundation vision-language models (VLMs) understand objects, instructions, and spatial relations, yet translating this capability into robotic manipulation remains difficult. Vision-language-action (VLA) models require extensive demonstrations and may compromise pretrained understanding, while direct RGB-only VLM control is costly and strongly dependent on model capability. We introduce Robo-Harness K1, a robot-use agent (RUA) framework that exposes perception as tools. The agent queries calibra...
  </details>

- **2026-09-24** — Jiaping Xiao, Pingyuan Ji, Mir Feroskhan — [ADM-Planner: LLM-Guided Long-Horizon Planning for Mobile Manipulators with Attention-Enhanced Dynamic Memory](http://arxiv.org/abs/2609.29212v1)
  <details><summary>📄 Abstract</summary>
  Large language models can decompose mobile-manipulation goals into long action sequences, but the resulting plans remain reliable only while their world context is current. A fixed scene description becomes stale when objects are discovered, moved, or completed while retaining every observation instead produces a growing history with redundant and conflicting state. To resolve this tension, we present an LLM-guided planning framework ADM-Planner with attention-enhanced dynamic memory (ADM). Pers...
  </details>

- **2026-09-24** — Junyi Tang, Jie Peng, Zezhen Ding et al. — [AdaHVLA: Adaptive Harnesses for Long-Horizon Vision-Language-Action Execution](http://arxiv.org/abs/2609.29204v1)
  <details><summary>📄 Abstract</summary>
  Vision-language-action (VLA) models offer strong local control and instruction following but often struggle with long-horizon tasks requiring persistent memory and planning. Task harnesses provide persistent context for agent reasoning by retaining task history and tracking progress across execution stages. To bring these complementary capabilities together, we introduce AdaHVLA, an adaptive harness that refines code-based coordination policies through robot experience to better align agent reas...
  </details>

- **2026-09-24** — Pengpeng Yu, Yueru Chen, Fei Song et al. — [Towards Practical Compression of 3D Gaussian Splatting](http://arxiv.org/abs/2609.30245v1)
  <details><summary>📄 Abstract</summary>
  3D Gaussian Splatting (3DGS) enables high-quality novel-view synthesis but requires substantial storage. Existing compression methods often rely on spatial context modeling over irregular 3D representations, increasing the complexity of training and coding. Meanwhile, floating-point context inference can introduce numerical inconsistencies across platforms, causing entropy-decoding failures. To address these practical challenges, we propose COSA-GS, which constructs context without spatial aggre...
  </details>

- **2026-09-24** — Troy P. Wixson, Daniel Cooley — [A Proxy-likelihood Estimator for Multivariate Extremes Models with Intractable Likelihoods](http://arxiv.org/abs/2609.30244v1)
  <details><summary>📄 Abstract</summary>
  Many multivariate extremes models have intractable likelihoods requiring practitioners to use alternative fitting methods. The tail pairwise dependence is a summary measure of the dependence in the tail of any multivariate regular variation model. We develop an objective function for model fitting that relies on the tail pairwise dependence as the link between our desired model (that does not have a likelihood) and a proxy model (that has a likelihood). We employ the bivariate Hüsler-Reiss distr...
  </details>

- **2026-09-24** — Xinyue Zeng, Jiawei Zhang, Yujun Yan et al. — [SAGE: Mitigating Long-Horizon Reasoning Biases via Topological Guidance](http://arxiv.org/abs/2609.30192v1)
  <details><summary>📄 Abstract</summary>
  Long-horizon reasoning remains a central challenge for large language models (LLMs) under sparse-reward regimes. We argue that this brittleness arises from two biases induced by complex reasoning spaces: an exploration bias, where models are drawn toward locally plausible but structurally unstable branches, and a compounding bias, where small local deviations accumulate across depth and suppress rare rewards. We introduce Symbolic Closure Analysis (SCA) as a theoretical lens characterizing how b...
  </details>

- **2026-09-24** — Leon Rode, Sumeet Khatri, Supartha Podder — [Learning and interpreting policies for simultaneous entanglement requests in quantum networks](http://arxiv.org/abs/2609.30157v1)
  <details><summary>📄 Abstract</summary>
  Future quantum networks will make use of entanglement to perform numerous tasks, such as sending quantum information over long distances, distributed quantum computing, and quantum sensing. In general, these tasks will need to be performed simultaneously in various regions of a network, while minimizing resources and latency. We will thus require policies for scheduling link-level entanglement resources, and using the link-level entanglement to create various forms of multipartite entanglement r...
  </details>

- **2026-09-24** — Archit Rastogi — [Does a model's stated reason for rejecting a candidate do any work?](http://arxiv.org/abs/2609.30151v1)
  <details><summary>📄 Abstract</summary>
  Asked to choose between candidates and explain the choice, a language model often rejects a rival by naming a fact its profile lacks: no director, no date of death. That sentence is a claim about the text in front of the model, and it can be tested without any judge. We insert a real corpus sentence stating the named fact into the rival's profile and ask again under greedy decoding. Two controls separate content from placement: a length-matched irrelevant sentence at the same profile, and the sa...
  </details>

- **2026-09-24** — Ken J. Jenewein, Faezeh Habib Zadeh, Xiaoxiao Wang et al. — [AI-guided high-throughput discovery of iridium- and ruthenium-free palladium-oxide catalysts for durable acidic oxygen evolution](http://arxiv.org/abs/2609.30133v1)
  <details><summary>📄 Abstract</summary>
  Catalyzing acidic oxygen evolution at the proton-exchange-membrane water electrolysis (PEMWE) anode relies almost entirely on iridium or ruthenium, drawn from concentrated supply chains that constrain gigawatt-scale deployment. We report an artificial intelligence (AI)-guided, human-supervised closed-loop platform (>90% automation) integrating combinatorial sputter synthesis, high-throughput screening, machine-learning composition-property models, adaptive multi-objective optimization, and conte...
  </details>

- **2026-09-24** — Aditya Cowsik, Kfir Dolev, Michael Y. Li et al. — [Self-Play Pretraining with Zero Data](http://arxiv.org/abs/2609.30063v1)
  <details><summary>📄 Abstract</summary>
  Advances in language modeling have been driven by scaling pretraining on ever more data. Yet, the training data is still largely curated on the model's behalf. A more general approach to pretraining would let the model learn to generate the data most useful for its own improvement. This would provide an effectively unbounded source of training data, limited by compute rather than human knowledge. We introduce Self-Play Pretraining with Zero Data, an initial proof-of-concept towards realizing thi...
  </details>

- **2026-09-24** — Robbe De Greef, Théo Engels, Felix Van den Broucke et al. — [Lifting the Preprocessor with Oxidize: Structure-Preserving C-to-Rust Translation (Technical Report)](http://arxiv.org/abs/2609.30062v1)
  <details><summary>📄 Abstract</summary>
  This technical report accompanies our EuroSys 2027 paper "Lifting the Preprocessor with Oxidize: Structure-Preserving C-to-Rust Translation" (DOI 10.1145/3842654.3848533). Oxidize is a C-to-Rust translator that retains C macros as Rust macros instead of expanding them away, so that the translated code keeps the abstractions its developers wrote. The report collects material the paper cites but has no room for: the translator's intermediate representation, pass structure and back-end emission; th...
  </details>

- **2026-09-24** — Tapan Parikh — [Low-Cost Assays for Measuring Model Behavior Across Vendors and Releases](http://arxiv.org/abs/2609.30012v1)
  <details><summary>📄 Abstract</summary>
  Language models advise people, keep them company, and write software while they sleep. Measuring what they do is hard: behavior has to be sampled repeatedly across models, prompts and releases, most of it lives in unstructured text that has to be coded before it can be counted, and the result has to be legible and rigorous enough to meaningfully compare models and vendors. To address these constraints, we present a simple, cheap, scalable, and replicable model for studying model behavior. Each s...
  </details>

- **2026-09-24** — Haiqing Li, Xin Ma, Yinhao Wu et al. — [Who Holds the Pen? Let Specifications, Not Agents, Sign Off](http://arxiv.org/abs/2609.29921v1)
  <details><summary>📄 Abstract</summary>
  Large language model agents increasingly combine generation, decision-making, execution, and self-evaluation within a single agentic loop. Although they operate under external specifications such as task instructions, guidelines, output schemas, and reusable skills, these specifications typically remain context for the same model that acts and declares completion, leaving no independent specification authority boundary. We identify two resulting gaps. The understanding--execution gap arises when...
  </details>

- **2026-09-24** — Zhihao Ouyang, Jingyu Wu, Hubing Xiao et al. — [Exceptional Gamma-Ray Flaring Activity of the Blazar S4 0954+65 in Early 2025](http://arxiv.org/abs/2609.29873v1)
  <details><summary>📄 Abstract</summary>
  S4 0954+65 (4FGL J0958.7+6534) is a TeV-detected blazar at a redshift of $z = 0.3694 \pm 0.0011$, classified as an intermediate-synchrotron-peaked BL Lac object. In early 2025, it entered an exceptional $γ$-ray high state. We aim to investigate the origin and physical properties of the exceptional 2025 flare, and to constrain the emission processes responsible for this flaring activity. We performed a multi-wavelength analysis using $γ$-ray, X-ray, optical/UV, radio, and 43 GHz Very Long Baselin...
  </details>

- **2026-09-24** — Simon Parkinson, Saad Khan, Na Liu et al. — [Template Ageing and Longitudinal Verification in Fixed-Text Keystroke Dynamics: A Subject-Disjoint Study Across Eight Weeks](http://arxiv.org/abs/2609.29851v1)
  <details><summary>📄 Abstract</summary>
  Behavioural biometric templates are widely believed to degrade as the gap between enrolment and verification grows, but few studies measure this template ageing effect directly under controlled conditions. We collected a longitudinal dataset of 40 fixed passwords, each typed four times per weekly session over eight consecutive weeks. We compare a scaled-Manhattan matcher (M1), a gradient-boosted classifier (M2), a TypeNet-style recurrent embedding model (M3), and a TypeFormer-style Transformer (...
  </details>

- **2026-09-24** — Zhenyan Lu, He Wang, Xiaohui Huang — [Encoded but Not Decoded: Layer-Localized Evidence for a Three-Level Gap in LLM Syntax](http://arxiv.org/abs/2609.29848v1)
  <details><summary>📄 Abstract</summary>
  A language model can fail a syntactic test in two distinct ways: by not encoding the relevant structure, or by encoding it but failing to use it at the output. Behavioral evaluation alone cannot tell these apart. We propose a three-level evaluation framework (behavioral deployment, LM-head readout, and probe recoverability) measured on the same items under the same binary decision. Using a compact trilingual (English, Chinese, German) control-dependency benchmark, we find that probe recoverabili...
  </details>

- **2026-09-24** — Zhaowei Lu, Liguo Zhou, Yujie Guo et al. — [S2Planner: Multi-Scale Semantic Planner for End-to-End Autonomous Driving](http://arxiv.org/abs/2609.29813v1)
  <details><summary>📄 Abstract</summary>
  We present S2Planner, a trajectory planner that combines three front-facing cameras with ego-motion history and the current driving command. A fine-tuned DINOv3 backbone and a Spatial Tuning Adapter produce multi-scale image features; a coarse-to-fine decoder then uses trajectory self-attention and camera-projected cross-attention to refine candidate waypoints. The contribution is the integration of ego-conditioned trajectory initialization with iterative, geometry-guided sampling of multi-scale...
  </details>

- **2026-09-24** — Xiangwei Wang, Peng Wang, Saman Halgamuge — [CORDIAL: Calibrating Ordinal LLM Outputs from Few Labels](http://arxiv.org/abs/2609.29807v1)
  <details><summary>📄 Abstract</summary>
  A large language model (LLM) can turn a text into a distribution over an ordered scale, but that distribution is a noisy measurement: saturated, compressed or exaggerated, and biased in a consistent direction. We propose CORDIAL, which treats the model's output as a noisy reading of the true label and corrects it with a channel of five interpretable parameters. The channel is small enough for its posterior to be averaged from a handful of labels, and we prove that the resulting calibration prese...
  </details>

- **2026-09-24** — Abhilasha Saroj, Pranav Govindu, Bharat Sharma et al. — [Adapting a Large Language Model Crash-Severity Pipeline to Tennessee: Performance Across Sampling Strategies](http://arxiv.org/abs/2609.29793v1)
  <details><summary>📄 Abstract</summary>
  State crash databases differ in structure, coding, and injury-severity distributions, limiting direct reuse of predictive workflows across jurisdictions. This study adapts the SafeTraffic Copilot large language model (LLM) crash-severity workflow to a three-year Tennessee inventory of 624,392 crashes. Tennessee crash, roadway, vehicle, and person attributes were harmonized and converted into textual prompts while unavailable values were preserved rather than inferred. Llama 3.1 8B was fine-tuned...
  </details>

- **2026-09-24** — Qusay H. Mahmoud — [Judgment-Centred Software Engineering Education: A Post-Hype Review and Framework for AI-Augmented Learning](http://arxiv.org/abs/2609.29473v1)
  <details><summary>📄 Abstract</summary>
  Generative artificial intelligence has moved from a disruptive novelty to a recurring part of software-development and computing-education workflows, while software agents are beginning to act across repositories, command lines, browsers, tests, and other tools. The educational problem is no longer whether students should be allowed to generate code, but whether software-engineering (SE) programs can preserve and assess human understanding while preparing students to work responsibly with increa...
  </details>

- **2026-09-24** — Fardeen Sadab, Adib Sakhawat — [Two Emojis of Difference: What Multilingual Affective Generation Benchmarks Actually Measure](http://arxiv.org/abs/2609.29445v1)
  <details><summary>📄 Abstract</summary>
  We audit a multilingual affective generation benchmark eight instruction-tuned LLMs producing emoji summaries for 17,100 Bangla, English and Hindi sentences, with 6,960 human judgements and find its headline conclusions to be artefacts of the measurement instrument rather than properties of the systems. Treating annotators as a random rather than a fixed factor, no system differs significantly from any other ($F(7,14)=0.59$, $p=0.76$), although the conventional analysis declares 19 of 28 pairwis...
  </details>

- **2026-09-24** — Karolina Gliszczyńska-Schroeder — [Kernel Balancing in Tree-based Methods](http://arxiv.org/abs/2609.29440v1)
  <details><summary>📄 Abstract</summary>
  Studying heterogeneous treatment effects has become essential in experimental and observational studies. A critical assumption for obtaining reliable treatment effect estimates is overlap, which requires that treated and control units have sufficiently similar covariate distributions. Poor overlap may limit the effectiveness of estimators, especially those based on propensity scores, potentially leading to unreliable results. We investigate the effectiveness of kernel balancing (KBal) (Hazlett, ...
  </details>

- **2026-09-24** — Maike Züfle, Patrícia Schmidtová, Vilém Zouhar et al. — [Calibrating LLM Judges for Human and AI Conversations](http://arxiv.org/abs/2609.29431v1)
  <details><summary>📄 Abstract</summary>
  Measuring how successful a conversation is remains difficult, even for humans judging spoken dialogue. We evaluate state-of-the-art LLMs as pointwise and pairwise judges of conversational success on CANDOR, finding pointwise scoring correlates moderately with human ratings, while pairwise comparison suffers from long transcripts and positional bias. Since this leaves judge scores incomparable across models, we propose a small anchor set and a calibration function that calibrates any judge onto a...
  </details>

- **2026-09-24** — Alexandru Stefan Stoica, Traian Rebedea, Marian Cristian Mihaescu — [Large Language Models for Programming: Actually Fixing or Reimplementing Incorrect Code?](http://arxiv.org/abs/2609.29410v1)
  <details><summary>📄 Abstract</summary>
  Recent studies have shown that Large Language Models can effectively solve problems and fix bugs in diverse programming environments, including competitive programming. Existing approaches primarily evaluate LLM performance in problem solving or bug fixing independently, but do not explore the relationship between these two capabilities. This work focuses on determining how much the LLM deviates from a buggy solution to fix the bug compared to a human-written patch, and if there is a bias toward...
  </details>

- **2026-09-24** — Gautam Veldanda — [Baseline Shape Decides the Verdict: A Controlled Re-Examination of Ternary Language Models at 60K Parameters](http://arxiv.org/abs/2609.29397v1)
  <details><summary>📄 Abstract</summary>
  Ternary (1.58-bit) weights are attractive for microcontroller-class language models, but the sub-1M-parameter regime rests mainly on isolated, single-seed comparisons. One prominent example reports that a routed ternary block (convolution, diagonal SSM and sparse attention mixed by a per-token router) beats a parameter-matched full-precision transformer by 22% at 60K parameters, attributing this to inductive bias. We re-run it under one fixed recipe, three seeds per cell, 98 byte-level runs on o...
  </details>

- **2026-09-24** — Linyang He, Nima Mesgarani — [Grammatical "grandmother neurons" are rare in LLMs](http://arxiv.org/abs/2609.29328v1)
  <details><summary>📄 Abstract</summary>
  Understanding how Large Language Models (LLMs) encode linguistic structures remains a fundamental challenge in interpretability research. While diagnostic classifiers (or "probes") are widely used for this task, they face significant methodological criticism: training auxiliary classifiers introduces capacity confounds and calibration issues, often making it difficult to distinguish the model's intrinsic representations from the probe's ability to learn the task. To address these limitations, we...
  </details>

- **2026-09-24** — Rayne Holland, Liming Zhu, Jason Xue — [When Honesty is Not Enough in AI Debate](http://arxiv.org/abs/2609.29189v1)
  <details><summary>📄 Abstract</summary>
  Scalable oversight aims to verify the behaviour of agents whose capabilities exceed those of their overseers. AI debate has been proposed as an oversight solution in which competing agents help a resource-limited verifier assess claims that it cannot reliably evaluate unaided. Much of its promise rests on incentivizing honest arguments that lead to correct verdicts. Yet a correct verdict need not uniquely determine the arguments used to support it. Agents may retain discretion over which correct...
  </details>

- **2026-09-24** — Heng Yao, Tianying Liu, Yulou Shu et al. — [ScalarLens: Numerical Embeddings with Stable Coordinates and Contextual Responses for CTR Prediction](http://arxiv.org/abs/2609.29182v1)
  <details><summary>📄 Abstract</summary>
  Numerical embeddings for click-through rate (CTR) prediction are built on a convenient but restrictive premise: a scalar has one representation. This premise conflates where a value lies with what it means for the current sample. On the Criteo validation split, the same numerical interval carries residual click evidence with opposite signs across categorical and numerical contexts, even after additive main effects are removed. Production pipelines compound this mismatch because externally normal...
  </details>

- **2026-09-24** — Rishad Shahmurov, Veli Shahmurov — [A Morrey-to-Lebesgue Equivalence for Convolution Calderón--Zygmund Operators](http://arxiv.org/abs/2609.29158v1)
  <details><summary>📄 Abstract</summary>
  We prove that, for vector-valued convolution Calderón--Zygmund operators, boundedness on a single nontrivial Morrey space is equivalent to the corresponding global $L^p$ boundedness. Thus one Morrey scale already contains the full finite-$p$ boundedness information. The implication from Morrey to $L^p$ is obtained by a separated-copy amplification argument that reconstructs the global norm from a single scale-local estimate; the converse is proved in the same vector-valued framework by a local/f...
  </details>

- **2026-09-24** — Vani Seth, Mohammad Beheshti, Anirudh Kambhampati et al. — [CRISS: A Retrieval-Augmented AI Chatbot for Assisting Cancer Registrars](http://arxiv.org/abs/2609.29075v1)
  <details><summary>📄 Abstract</summary>
  Cancer registrars, including Oncology Data Specialists (ODSs), must interpret complex and frequently updated coding and staging standards. We developed CRISS (Cancer Registry Intelligent Support System), a retrieval-augmented generation (RAG) conversational assistant that provides rapid, citation-supported access to registry guidance. This study evaluated whether CRISS could (1) support accurate and citation-supported responses, (2) improve access to and interpretation of relevant guidance, and ...
  </details>

- **2026-09-24** — Lucas Da Mota Bruno, Jiahao Sim, Yoshinobu Hagiwara — [Design and Evaluation of LLM Chaining-Based Task Planning for General Purpose Service Robots](http://arxiv.org/abs/2609.29043v1)
  <details><summary>📄 Abstract</summary>
  General Purpose Service Robot (GPSR) tasks, as defined in the RoboCup@Home benchmark, require robots to interpret diverse natural language commands and generate multi-step action sequences in real home environments. Conventional Single Prompt (SP) approaches suffer from context bloat and the "Lost in the Middle" phenomenon, leading to unreliable task planning. We propose an LLM chaining architecture that separates instruction classification and action generation into two specialized stages, redu...
  </details>

- **2026-09-24** — Hongye Yang, Boxiao Huang — [When Does Action Credit Need Updating?](http://arxiv.org/abs/2609.29007v1)
  <details><summary>📄 Abstract</summary>
  Tool-using agents are continually updated with new interaction data. After each policy update, however, previously estimated action credits may become stale. Recomputing them from scratch can require many additional tool calls and environment interactions, making repeated updates increasingly expensive. We ask a simple question: when does historical action credit actually need to be updated? Our key observation is that a change in action value does not necessarily imply a change in the decision....
  </details>

- **2026-09-24** — Teirungumunu Apolinar Torres Zalabata, John Morales Aponte, Andrés Fernando Castillo Ramírez — [Geometrical BRST Quantization of Gauged Nonlinear Sigma Models: Killing Fields and Physical Cohomology](http://arxiv.org/abs/2609.28992v1)
  <details><summary>📄 Abstract</summary>
  We construct an off-shell BRST-invariant gauge-fixed formulation of a nonlinear sigma model coupled to a non-Abelian gauge field. Starting from the dynamics of GBs and their consistent couplings to gauge and ghost fields, we construct the corresponding BRST-invariant quantum theory and provide a geometrical interpretation in terms of Killing vectors. A central point of our treatment is that the Lie-bracket closure of the target-space Killing vectors provides the geometric realization of the alge...
  </details>

- **2026-09-24** — Lan Luo, Yuqi Liang, Jie Cai et al. — [Characterizing LLM-Based Family Education through the Lens of Activity Theory: A Scoping Review of the HCI Literature](http://arxiv.org/abs/2609.28886v1)
  <details><summary>📄 Abstract</summary>
  Large language models (LLMs) are increasingly involved in family education, yet HCI has not systematically explained the educational interactions that emerge around them. This scoping review analyzes 53 HCI studies from 6,540 records across 19 venues. Using activity theory and AODM, it relates participants and educational objects to mediation, labour, and rules. We find that the literature centers on child--parent interaction and on language, AI literacy, and relational learning. The introductio...
  </details>

- **2026-09-23** — Zheng Zhang, Liu Liu, Qi Chai et al. — [Adversarial Closed-Loop Curriculum for Evolving Role-Playing Agents](http://arxiv.org/abs/2609.28609v1)
  <details><summary>📄 Abstract</summary>
  Role-playing agents based on large language models have been widely applied in areas such as personalized assistance and social simulation. Recent RL methods typically train on a fixed scenario pool collected before learning begins. This creates a distributional bottleneck: as the agent improves, the scenarios where it performs poorly also change, while the training distribution remains static. Therefore, we propose AdvRole, an adversarial context rewriting framework that turns role-playing RL i...
  </details>

- **2026-09-23** — Matthew Sun, Vinay Kothapally, Meng Yu et al. — [A Harness for Synthesizing Diverse Naturalistic Full-Duplex Conversations](http://arxiv.org/abs/2609.28806v1)
  <details><summary>📄 Abstract</summary>
  Full-duplex dialogue systems, which listen while speaking, must distinguish a completed turn from a pause within a turn and an interruption that requests a turn from a brief acknowledgment or speech addressed to a third party. Yet existing conversational corpora provide limited control over these events and limited labels for their intent. We present a pipeline for synthesizing intent-labeled, two-channel conversational speech from relational event lists. An LLM authors each event's speaker, tex...
  </details>

- **2026-09-23** — Dimitrios Rontogiannis, Ander Artola Velasco, Manuel Gomez Rodriguez — [Learning the Cost of Reliable Inference](http://arxiv.org/abs/2609.28322v2)
  <details><summary>📄 Abstract</summary>
  Benchmarking and routing platforms increasingly act as intermediaries connecting large language model providers with end-users. However, providers on these platforms typically use a fixed price per token, preventing users from achieving the most competitive price for their tasks. In this work, we design a procurement platform where token prices for each task are driven by provider competition, enabling users to secure competitive pricing for guaranteed quality levels. To this end, the platform s...
  </details>

- **2026-09-23** — Hannan Cao, Jun Guo, Haolei Pei et al. — [OneTrans-V2: Unifying Retrieval, Pre-rank, and Fine-rank with One Transformer in Industrial Recommender](http://arxiv.org/abs/2609.28589v1)
  <details><summary>📄 Abstract</summary>
  Industrial recommendation systems typically operate as a \emph{cascade} of retrieval, pre-rank, and fine-rank, but these stages are usually trained and served as separate models, causing repeated user-sequence encoding, isolated optimization, and duplicated engineering effort. Building on OneTrans' model-level unification, we present OneTrans-V2, one Transformer that unifies the entire cascade. It encodes the user behavior sequence once as a shared context while preserving stage-specific candida...
  </details>

- **2026-09-23** — Tara Sadjadpour, Siming He, C. K. Wolfe et al. — [Morphometric Imitation: From Morphology and Contact Aware Hand Retargeting to Sim-to-Real Visuomotor Policy](http://arxiv.org/abs/2609.28660v1)
  <details><summary>📄 Abstract</summary>
  Human hand-object interactions (HOIs) provide a rich source of demonstrations for dexterous manipulation, but learning directly from them presents challenges in bridging morphology gaps, ensuring dynamical feasibility, and sim-to-real deployment. We present Morphometric Imitation, a three-stage framework that transforms reconstructed HOIs into zero-shot sim-to-real visuomotor policies. First, morphometric optimization (MMO) kinematically retargets human motion across hand morphologies while pres...
  </details>

- **2026-09-23** — Asael Sorensen, Charles Brock, David Chamberlain et al. — [Stream Recursion Model (SRM)](http://arxiv.org/abs/2609.28809v1)
  <details><summary>📄 Abstract</summary>
  Mechanistic interpretability seeks to make verifiable statements about the internal behavior of large language models (LLMs). Many interpretability techniques struggle to scale with the increasing size and depth of architectures. Our solution to this is to introduce smaller models with structures that lend themselves to interpretability. In this work, we introduce the Stream Recursion Model (SRM), a modification of the Hierarchical Reasoning Model (HRM) designed to expose internal computational ...
  </details>

- **2026-09-23** — David Kletz, Sandra Mitrović, Itay Sabato et al. — [Script Choice in LLMs: Evidence for Late-Layer Commitment](http://arxiv.org/abs/2609.28784v1)
  <details><summary>📄 Abstract</summary>
  In this paper, we investigate how script knowledge is distributed across the layers of LLMs using two complementary interpretability methods: logistic regression probing and logit-lens analysis. Our probing experiments reveal a clear asymmetry: both the input script and the instructed output script are encoded in the earliest layers of the network, while, in contrast, commitment to the actual output script emerges only in the final layers, with the model's intermediate representations defaulting...
  </details>

- **2026-09-23** — Samarth Kishor, Victor Nicolet, Joey Dodds — [Soundness Checking of Taint Flow Models](http://arxiv.org/abs/2609.28750v1)
  <details><summary>📄 Abstract</summary>
  Existing state-of-the-art static taint flow analyses for imperative programming languages can scale to large applications by using precise user-provided taint flow models of library methods. However, manually and precisely modeling a method's taint flows is tedious and potentially unsound. Furthermore, automatically modeling the method via an inter- procedural taint analysis can be inefficient. To solve this problem, we propose a guess-and-check approach: (1) an LLM agent that generates a precis...
  </details>

- **2026-09-23** — José Luciano Verçosa Marques, Frederico Jorge Heitmann, Daniel Omar Perez et al. — [Technical Manual for Toolkit for Confidence-Corpus Consistency via Fine-Tuning on a Fabricated Corpus](http://arxiv.org/abs/2609.28747v1)
  <details><summary>📄 Abstract</summary>
  A language model's confidence in an answer is often read as a proxy for how well it knows the corresponding fact. This manual documents an open toolkit built to test that reading directly: a small causal language model is fine-tuned on a corpus that consistently asserts one fabricated arithmetic answer for each of the 81 single-digit addition pairs, and its post-fine-tuning confidence in each fabricated answer is compared against its own pre-fine-tuning confidence in the corresponding true answe...
  </details>

- **2026-09-23** — Ella Hugie, Alexandra Irger, Chiara Schiller et al. — [How Spatial Biologists Direct and Verify AI-Assisted Analyses](http://arxiv.org/abs/2609.28723v1)
  <details><summary>📄 Abstract</summary>
  Spatial biologists use visualization to assess computational analyses of tissue data. We examine how they direct and verify analyses when an AI agent performs this work. We synthesized workflows from fourteen contextual inquiries and conducted a formative pilot followed by an observational study with ten spatial biologists using Claude Science on their own data. Participants valued help with plotting, locating cells of interest, and tasks they found laborious or could not otherwise perform. Asse...
  </details>

- **2026-09-23** — Esteve Almirall, Christopher Tucci — [From Individual to Social Imitation: How Communities Expand Organizational Search](http://arxiv.org/abs/2609.28675v1)
  <details><summary>📄 Abstract</summary>
  Generative artificial intelligence illustrates a broader organizational puzzle: young, resource-constrained firms can build on knowledge produced across a wider field to address problems that exceed their internal experience. We theorize one mechanism as social imitation: a distributed and recursive process through which communities observe practices and outcomes across organizations, distill recurrent elements into portable strategies, circulate them, and revise the collective repertoire as ado...
  </details>

- **2026-09-23** — Thorsten Buss, Frank Gaede, Gregor Kasieczka et al. — [Cross-geometry transfer and model collapse in point cloud calorimeter shower generation](http://arxiv.org/abs/2609.28661v1)
  <details><summary>📄 Abstract</summary>
  Particle shower simulation is a major computational cost in high-energy physics. Monte Carlo methods such as Geant4 are accurate but expensive, while most machine learning surrogates are tied to specific detector geometries and require retraining for each design change. We study cross-geometry transfer learning with CaloClouds II, a generative model that produces point clouds rather than voxels and can project onto arbitrary detector readouts. We pre-train on photon showers in the International ...
  </details>

- **2026-09-23** — Kacper Nowak, Aleksei Koldunov, Nikolay Koldunov et al. — [HClimRep-Ocean: A Global Ocean Emulator on an Unstructured Mesh](http://arxiv.org/abs/2609.28601v1)
  <details><summary>📄 Abstract</summary>
  Machine-learning (ML) emulators for atmospheric processes have advanced rapidly in recent years, transforming weather forecasting. Although early ML ocean forecasting models now exist, they remain less developed than their atmospheric counterparts. Unlike the atmosphere, much of the ocean's kinetic energy resides in mesoscale eddies whose characteristic spatial scales are approximately an order of magnitude smaller than those of comparable atmospheric features. Moreover, complex coastlines, narr...
  </details>

- **2026-09-23** — Quang Minh Nguyen, Thuy Quynh Nguyen, Duc Minh Le et al. — [SMILESGNN: Interpretable Clinical Toxicity Prediction via SMILES-Graph Cross-Attention Fusion](http://arxiv.org/abs/2609.28553v1)
  <details><summary>📄 Abstract</summary>
  Drug toxicity prediction is critical for reducing late-stage attrition in drug discovery, yet remains challenging due to severe class imbalance, scaffold-based generalization, and the clinical need for interpretable predictions. Single-modality approaches-SMILES Transformers or graph neural networks capture complementary aspects of molecular structure, while sequence-only models cannot directly provide graph-attributed explanations. We present SMILESGNN, a multimodal architecture that fuses a SM...
  </details>

- **2026-09-23** — Harshdeep Jadhav, Sreeraj Rajan Warrier, Jayasri Dontabhaktuni — [Image Compression Using Quantum Wavelet Transform and Quantum Convolutional Networks](http://arxiv.org/abs/2609.28387v1)
  <details><summary>📄 Abstract</summary>
  This paper presents a hybrid quantum-classical framework for grayscale image compression and decompression, leveraging the strengths of quantum computing and deep learning. The compression pipeline integrates a Variational Quantum Daubechies Wavelet Transform (V-QDWT) and a trainable Quantum Convolutional Neural Network (QCNN) optimized end-to-end to achieve efficient, image-adaptive multi-resolution analysis and entanglement-based feature reduction. Input images are encoded using the Normal Arb...
  </details>

- **2026-09-23** — Saar Cohen, Nicholas Teh, Michael Wooldridge — [Online Fair Division Against an Oblivious Adversary](http://arxiv.org/abs/2609.28333v1)
  <details><summary>📄 Abstract</summary>
  We study the online allocation of indivisible goods among $n$ agents, where each good must be allocated immediately and irrevocably upon arrival. Against an adaptive adversary, Neoh and Teh [2026] proved that no algorithm can guarantee a positive approximation to proportionality up to one good (PROP1) that is independent of the number of goods, and the same holds for proportionality up to $k$ goods (PROP$k$) for any fixed $k$. We instead consider an oblivious adversary, which fixes the input in ...
  </details>

- **2026-09-23** — Weihang Ding, Junfei Zhan, Yueting Li et al. — [FDE-Bench: Evaluating LLM Agents for Deployment Environment Configuration](http://arxiv.org/abs/2609.27571v1)
  <details><summary>📄 Abstract</summary>
  Deployment requires an agent to turn application code into a running system whose services connect, become ready, and remain observable. FDE-Bench evaluates this capability with 136 deployment-configuration tasks spanning Docker images, multi-service Compose stacks, and Kubernetes, in greenfield and diagnose-and-repair modes. Agents submit declarative artifacts that are collected, rebuilt, and redeployed in a pristine environment. Four gated binary check layers measure build, readiness, behavior...
  </details>

- **2026-09-23** — Zaid Ghazal, Khouloud Gaaloul, Bruce Maxim — [Teach-to-Crash: A Closed-Loop Student-Teacher LLM Framework for Collision-Inducing Test Scenario Generation](http://arxiv.org/abs/2609.27296v1)
  <details><summary>📄 Abstract</summary>
  Validating Autonomous Driving Systems (ADS) in simulation requires testing architectures that can discover rare, safety-critical failures while generating scenarios that are executable, diverse, and useful for downstream failure analysis. We introduce Teach-to-Crash, a closed-loop testing framework that combines a constrained ego-centric scenario representation, stagnation-aware search control, and a dual-LLM architecture for adaptive failure discovery. A high-reasoning Teacher LLM acts as an ad...
  </details>

- **2026-09-23** — Wenjie Feng, Sahba Zojaji, Satoshi Nakamura — [Cross-Scale Transfer Learning for Depression Severity Prediction: From PHQ-8 to HAMD-17 Across Languages and Clinical Paradigms](http://arxiv.org/abs/2609.28430v1)
  <details><summary>📄 Abstract</summary>
  This work addresses continuous depression-severity score prediction from clinical interview transcripts under data scarcity. We propose a sequential low-rank adaptation (LoRA) protocol for cross-scale transfer: a Qwen3 backbone with a bounded regression head is first fine-tuned on the English DAIC-WOZ dataset (189 avatar-mediated sessions, PHQ-8), and the adapter then initializes fine-tuning on the Chinese PDCH dataset (100 real clinical consultations, HAMD-17), where a reinitialised, scale-spec...
  </details>

- **2026-09-23** — Shahan Ahmed — [Threat Amplified, Blame Restrained: LLM-Assisted Media Framing Analysis of the 2026 Bangladesh Measles Outbreak](http://arxiv.org/abs/2609.28362v1)
  <details><summary>📄 Abstract</summary>
  How news media frame and emotionally code a public health emergency shapes public risk perception and trust, yet outbreak-coverage dynamics remain understudied for low- and middle-income countries (LMICs). We examine sentiment and stance in English-language Bangladeshi coverage of the 2026 measles outbreak -- the country's most severe in two decades, with over 97,000 suspected cases and 600 deaths across 61 of 64 districts, unfolding after the 2024 change of government and a 2024-2025 vaccine st...
  </details>

- **2026-09-23** — Dimitrios Rontogiannis, Ander Artola Velasco, Manuel Gomez Rodriguez — [Learning the Cost of Reliable Inference](http://arxiv.org/abs/2609.28322v1)
  <details><summary>📄 Abstract</summary>
  Benchmarking and routing platforms increasingly act as intermediaries connecting large language model providers with end-users. However, providers on these platforms typically use a fixed price per token, preventing users from achieving the most competitive price for their tasks. % workloads. In this work, we design a procurement platform where token prices for each task are driven by provider competition, enabling users to secure competitive pricing for guaranteed quality levels. To this end, t...
  </details>

- **2026-09-23** — Samrat Sahoo, Liang Ji, Tom Silver et al. — [TANDEM: Task and Motion Planning with As-Needed Demonstrations for Efficient Vision-Language-Action Model Fine-tuning](http://arxiv.org/abs/2609.28314v1)
  <details><summary>📄 Abstract</summary>
  Human teleoperators spend substantial time demonstrating behaviors that robots can already perform autonomously, limiting the scalability of data collection for robot foundation models. Task and motion planning (TAMP) can automate many of these behaviors, but a fixed planning domain may not support every stage of a long-horizon manipulation task. We present TANDEM (Tamp with As-Needed Demonstrations for Efficient Model fine-tuning), a system that combines TAMP with selective human teleoperation ...
  </details>

- **2026-09-23** — Ariel Barel — [Connectivity Preservation and Graph Stretching in Range-Only Swarm Dispersion](http://arxiv.org/abs/2609.28190v1)
  <details><summary>📄 Abstract</summary>
  We study connectivity-preserving finite-jump dispersion of anonymous, identical, and oblivious agents under an idealized range-only sensing model. Each agent measures only the distances to its visible neighbors, without bearings, identifiers, communication, memory, or a shared coordinate system. We derive the largest isotropic displacement certifiable as safe from these measurements alone. The resulting rule requires only the distance to the farthest visible neighbor: each agent selects a random...
  </details>

- **2026-09-23** — Athanasios Angelakis, Marta Gomez-Barrero — [From ECG Signals to Representative-Morphology Heatmaps for Biometric Recognition](http://arxiv.org/abs/2609.28183v1)
  <details><summary>📄 Abstract</summary>
  Electrocardiography (ECG) contains subject-specific morphology that supports biometric recognition, yet image-based performance depends on how the waveform is rendered. We introduce representative-morphology heatmaps, a deterministic ECG-to-image representation adapted from ECGXtractor. Within each block of ten aligned beats, the five beats closest to the block mean are averaged into a 400 by L matrix and rendered either as a conventional trace or as a dense cardiac-time-by-lead heatmap. Since b...
  </details>

- **2026-09-23** — Haitong Jiang, Chunlin Liu, Yile Wang et al. — [Exact Feedback Is Not Control: Evaluating Text-based Closed-Loop Revision in LLMs](http://arxiv.org/abs/2609.28150v1)
  <details><summary>📄 Abstract</summary>
  Closed-loop revision is increasingly used in large language model (LLM) applications, but failures may reflect incomplete feedback or ineffective responses to correct feedback. We introduce a fixed-budget revision protocol with deterministic verifiers that report all remaining violations across exact-length, lexical, and compositional constraints. Fixing feedback correctness and completeness isolates model-side revision behavior. Across 19 open- and closed-source models, controller-level mean fi...
  </details>

- **2026-09-23** — Ziqi Ni, Rui Li, Shiqi Jiang et al. — [MotionSpec: Spectral Trajectory Supervision for Motion-Consistent Video Generation](http://arxiv.org/abs/2609.28095v1)
  <details><summary>📄 Abstract</summary>
  Recent advances in text-to-video generation have enabled high-fidelity visual synthesis, yet realistic motion remains challenging. Generated videos may exhibit temporal discontinuities, inconsistent action progression, and structural distortions during complex movements. Even when individual frames appear realistic, the underlying motion may evolve in inconsistent or implausible ways. Standard generative objectives provide limited motion-specific supervision, leaving motion evolution insufficien...
  </details>

- **2026-09-23** — Jiayi Zhang, Renlong Wu, Yukang Ding et al. — [ZoomDiff: A High-Fidelity Diffusion Model for Dual-Camera Smooth Zooming](http://arxiv.org/abs/2609.28083v1)
  <details><summary>📄 Abstract</summary>
  Digital zoom transitions between dual cameras often exhibit conspicuous discontinuities in geometric structure and chromatic consistency, degrading the user experience. While recent dual-camera smooth zoom (DCSZ) methods attempt to mitigate this by fine-tuning frame interpolation (FI) models on DCSZ data, they struggle with the large cross-view disparities and complex geometric transformations. Considering that the generative prior of diffusion models is suitable for addressing this problem, we ...
  </details>

- **2026-09-23** — Koi McFarland, Songhui Yue — [LLM-Assisted Workflow for Structural Difference Visualization in Evolving Software Requirements](http://arxiv.org/abs/2609.28002v1)
  <details><summary>📄 Abstract</summary>
  This paper presents an LLM-assisted workflow for visualizing structural differences in evolving software require- ments. Implemented in the OntologyWeb environment, the work- flow represents baseline and current requirements as triple-based semantic graphs and supports side-by-side comparison of curated graph snapshots. The comparison view aligns matched entities and uses visual encoding to highlight structural changes.
  </details>

- **2026-09-23** — Ohad Rahamim, Dvir Samuel, Idan Schwartz et al. — [All modalities are equal, but video is more equal: Closing the Cross-Attention Gap in Joint Video Generation](http://arxiv.org/abs/2609.27901v1)
  <details><summary>📄 Abstract</summary>
  Video is a rich representation of a physical event, capturing appearance, geometry, motion, and temporal evolution. Other modalities, such as 3D body motion or audio, encode narrower aspects of the same event. We find that joint multimodal diffusion transformers exhibit a corresponding asymmetry in cross-modal correspondence: companion modalities develop strong correspondences to video, but the reciprocal correspondences through which they constrain video remain substantially weaker. We express ...
  </details>

- **2026-09-23** — Jinyu He, Zihao Mao, Haonan Jin et al. — [CoRelNav: Collaborative Relational Navigation for Multi-Robot Spatially Constrained Semantic Navigation](http://arxiv.org/abs/2609.27720v1)
  <details><summary>📄 Abstract</summary>
  Spatially constrained semantic navigation requires robots to identify targets specified not only by semantic categories but also by relations to surrounding objects. In unknown environments, resolving such goals requires efficient exploration together with sufficient target and contextual evidence for reliable relation verification. Existing methods leave relation-aware verification and multi-robot collaboration largely disconnected: relational navigation is predominantly single-agent, while mul...
  </details>

- **2026-09-23** — Eduin E. Hernandez, Sergio A. Diaz, Luis F. Garcia et al. — [The Path Matters: Evaluating Small Language Models Beyond Answer Accuracy in KGQA](http://arxiv.org/abs/2609.27669v1)
  <details><summary>📄 Abstract</summary>
  Small language models (SLMs) are increasingly paired with knowledge graphs (KGs), yet end-to-end KG question answering conflates graph access, search, navigation, reasoning, and answer generation. This coupling makes it difficult both to determine whether an SLM can faithfully execute the reasoning path implied by a question and to attribute failures to navigation rather than to other stages of the pipeline. We isolate this capability by employing the THESEUS navigation and traceability framewor...
  </details>

- **2026-09-23** — Xiu-Hao Deng — [Structured Hamiltonian Learning for Multiqubit Conditional Phase Gates](http://arxiv.org/abs/2609.27629v1)
  <details><summary>📄 Abstract</summary>
  Accurate measurement of an intended conditional phase does not by itself place a multiqubit phase gate in its declared generalized-gate equivalence class. We cast the diagnosis as structured Hamiltonian learning of the diagonal successful block in a known basis: Ramsey measurements on a connected graph reconstruct a target-relative eigenphase map; a Walsh transform then yields the per-cycle stroboscopic error generator in a selected logarithm branch, whose branch-dependent coefficients alone can...
  </details>

- **2026-09-23** — Kailin Wang, Haoxiang Jie, Yaoyuan Yan et al. — [RegenHarness: A Robot Agent Harness with Evidence-Gated Recursive Self-Improvement](http://arxiv.org/abs/2609.27612v1)
  <details><summary>📄 Abstract</summary>
  Long-horizon robot execution requires a clear distinction between a model's proposal, a controller's termination, and verified task completion. We present RegenHarness, an evidence-gated robot-agent harness connecting task planning to heterogeneous robot skills. Its execution architecture couples a model loop for context-conditioned proposals with an agent loop for dispatch, observation, verification, commitment, and bounded recovery. Four role-isolated contexts separate planning, supervision, v...
  </details>

- **2026-09-23** — Shengjun Zhang, Wenhao Li, Zhenxin Lin et al. — [Safety-Filtered Distributed Koopman-MPC](http://arxiv.org/abs/2609.27463v1)
  <details><summary>📄 Abstract</summary>
  Distributed model predictive control (DMPC) often constructs both predictions and collision constraints from neighbor trajectories, so packet loss can remove both. We separate these roles: received trajectories drive Koopman-MPC, while local sensing and shelf geometry define a hard-constrained quadratic program (QP) that projects the applied input. Its radial demand is the least constant acceleration that keeps a supporting-plane clearance nonnegative throughout one zero-order-hold interval. Com...
  </details>

- **2026-09-23** — Weiyu Ma, Liangbing Zhao, Yongcheng Zeng et al. — [JEV-Star: Fast, Low-Cost StarCraft II Control with Language-Model Planning](http://arxiv.org/abs/2609.27331v1)
  <details><summary>📄 Abstract</summary>
  We present JEV-Star, a StarCraft II controller that defeats the strongest non-cheating built-in AI, Lv7, by combining fast JEV action selection with persistent GPT-6 planning. The combined system wins four full games at Lv5--Lv7, including two Lv7 victories with different seeds, while retaining a median JEV response time of 0.422 seconds. Mean estimated model cost across these games is USD~3.71 per game: USD~0.15 for JEV and USD~3.56 for GPT-6. We compare this system with an initial JEV-only con...
  </details>

- **2026-09-23** — Xinjie Shen, Wei Fan, Xudong Guo et al. — [Verifiable Hidden Dynamics Play: Generating Agentic RL Environments from Solved Mechanisms](http://arxiv.org/abs/2609.27321v1)
  <details><summary>📄 Abstract</summary>
  Language-model agents increasingly face long-horizon tasks with evolving state, interdependent decisions, and delayed outcomes. Scaling their training requires diverse agentic environments, dependable outcome signals, and low extension cost. Existing generation pipelines commonly construct an environment before defining its outcome rule or annotating its trajectories, leaving dynamics and evaluation to be aligned post hoc. VHD-Play reverses this dependency by sampling and solving a mathematical ...
  </details>

- **2026-09-23** — Yuan Huang, Sihan Hu, Hongyu Gu et al. — [Large Knowledge Model: From Papers to a Scientific Reasoning Landscape](http://arxiv.org/abs/2609.27297v1)
  <details><summary>📄 Abstract</summary>
  Accumulated scientific knowledge advances inquiry when prior findings help researchers choose new questions, design investigations, and interpret results. Realizing this value at scale requires access to the reasoning that connects research problems, scientific procedures, conclusions, and evidence. We introduce the Large Knowledge Model (LKM), a scientific knowledge infrastructure that transforms the literature into a shared, computationally accessible reasoning resource. LKM represents papers ...
  </details>

- **2026-09-23** — Mingxuan Wang, Bo Wang, Fei Luo et al. — [DRSR: Learning Set-Level Deletion Risk for Efficient Long-Horizon Agents](http://arxiv.org/abs/2609.27276v1)
  <details><summary>📄 Abstract</summary>
  Long-horizon language-model agents accumulate reasoning traces, tool exchanges, and observations whose relevance changes with the current decision. Existing compression strategies often score historical units independently, but the safety of deleting several units is generally not determined by their singleton scores: redundant evidence, accumulated small effects, and the information that remains after deletion all matter. We introduce Direct Relational Set-Risk Pruning (DRSR), which formulates ...
  </details>

- **2026-09-23** — Ruoyu Hu, Feng Bao, Zezhong Zhang et al. — [Data-Assimilation-Assisted Reinforcement Learning for Power Grid Control under Load Uncertainty](http://arxiv.org/abs/2609.27229v1)
  <details><summary>📄 Abstract</summary>
  Reliable power grid control requires sequential decisions under transmission constraints, time-varying demand, renewable variability, and imperfect load information. We investigate how load information quality affects control in a customized transmission network simulator inspired by Grid2Op and based on a DC power flow model. The environment includes stochastic spatial loads, temporally correlated renewable-like generation, energy storage, line protection, generator dispatch, and line reconnect...
  </details>

- **2026-09-23** — Dev Pratap Singh, Rong Feng, Suman Saha — [Verified Learning for Compiler Optimization: An LLM-Guided Architecture with Formal Control](http://arxiv.org/abs/2609.27214v1)
  <details><summary>📄 Abstract</summary>
  Compiler optimizations traditionally rely on handcrafted heuristics that often fail to generalize across programs and architectures. We investigate whether large language models can participate in compiler optimization through a verification-centered systems architecture that couples generative rewriting with formal equivalence checking. Using lazification in LLVM IR as a case study, we fine-tune a code-centric LLM on transformations produced by Wyvern and embed Alive2 into a feedback loop that ...
  </details>

- **2026-09-23** — Hantao Ye, Ross Worobel, Zhuoli Xie et al. — [PointCast: One World Model for Rigid, Articulated, and Deformable Object Manipulation](http://arxiv.org/abs/2609.28393v1)
  <details><summary>📄 Abstract</summary>
  World models are useful for robotic manipulation because robots can predict how actions change the states of objects before executing them. We present PointCast, a point-set world model that spans rigid, articulated, and deformable object manipulation. Its state is a set of 3D points on the object and the end-effector, mesh-free and topology-agnostic. Each point keeps its identity and is supervised on its own trajectory, which teaches the model where every point goes rather than only the shape t...
  </details>

- **2026-09-23** — Wei Sun, Xiaoying Yan, Jinbao Long et al. — [A photonic integrated comb engine for ultracold quantum gases](http://arxiv.org/abs/2609.28294v1)
  <details><summary>📄 Abstract</summary>
  Cold atoms underpin quantum sensing, simulation and computation, but their coherent control demands highly stable optical fields whose generation, referencing and power scaling remain formidable integration challenges. While photonic integrated circuits have yielded compact visible lasers and high-$Q$ microresonators have enabled chip-scale optical frequency combs, these crucial technologies have largely remained functionally fragmented. Consequently, the coherent manipulation of ultracold quant...
  </details>

- **2026-09-23** — Pei-lin Li, Qingle Liu, Junyang Feng et al. — [When Context Misleads: In-context Learning with Jurisdiction in Large Language Models](http://arxiv.org/abs/2609.27603v1)
  <details><summary>📄 Abstract</summary>
  In-Context Learning (ICL) has become a cornerstone of modern LLM deployment. However, existing ICL post-training methods have a critical blind spot: they excel at extracting patterns from demonstrations while often neglecting context authority, the ability to determine whether contextual information should govern the final answer. To benchmark this capability, we introduce FakeContextBench, which contains pseudoscientific claims across seven domains. Our evaluation of commercial and open-source ...
  </details>

- **2026-09-23** — Haoxiang You, Zeyu Shen, Yilang Liu et al. — [EmbodiedSWE: Coding Agents for Long Horizon Dexterous Robotics](http://arxiv.org/abs/2609.27308v1)
  <details><summary>📄 Abstract</summary>
  We study coding agents for long-horizon, dexterous robotics and ask whether their solutions can provide scalable supervision for learning general robot policies. To test this, we develop EMBODIEDSWE-BENCH, a simulation benchmark for coding agents spanning contact-rich manipulation, deformable objects, and long-horizon tasks requiring up to half an hour of continuous interaction. We find that frontier coding agents can solve complex long-horizon tasks and transfer prior solutions across both task...
  </details>

- **2026-09-23** — Nathalia Gomez, Haig Shamlian, Omar Khan et al. — [Listening and Mirroring: The Effects of Verbal Attunement and Behavioral Mimicry on Social and Empathic Perceptions of Embodied AI Agents in VR](http://arxiv.org/abs/2609.27246v1)
  <details><summary>📄 Abstract</summary>
  As embodied agents take on increasingly social and relational roles in VR, visual realism and embodiment alone may be insufficient; users must also perceive these agents as emotionally attuned, supportive, and humanlike. Prior work suggests that verbal attunement and nonverbal mimicry can each improve users' social evaluations of embodied agents. However, behavioral mimicry has largely been studied outside of real-time, conversational AI interactions, leaving limited understanding of how users r...
  </details>

- **2026-09-23** — Marco Drewes, Yannis Georis, Juraj Klarić et al. — [Sterile Neutrino Dark Matter Cries for GeV Heavy Neutral Leptons](http://arxiv.org/abs/2609.28457v1)
  <details><summary>📄 Abstract</summary>
  The ordinary and dark matter in the Universe may share a common origin in the framework of a minimal extension of the Standard Model by three right-handed neutrinos. A pair of such heavy neutral leptons (HNLs) can give masses to neutrinos, generate the baryon asymmetry at the electroweak scale and produce a large lepton asymmetry at the QCD scale, which is then resonantly transformed into an abundance of the third state that acts as sterile neutrino dark matter. The minimality of this setup, kno...
  </details>

- **2026-09-23** — Zhipeng Bao, Wenjie Zhao, Tianle Zhu et al. — [AnchorReasoning: A Visual Grounding and Causal Reasoning Dataset in Long-Tail Autonomous Driving Scenarios](http://arxiv.org/abs/2609.28366v1)
  <details><summary>📄 Abstract</summary>
  Vision-language models (VLMs) offer a promising approach to long-tail autonomous driving, but existing driving datasets provide limited supervision for connecting decision-critical visual evidence with reasoning and planning. We introduce AnchorReasoning, a visually grounded reasoning dataset built on WOD-E2E, containing 416,119 annotated frames and 395,379 decision-critical elements across four major categories and 19 fine-grained types. Each frame is organized as a visually grounded chain-of-t...
  </details>

- **2026-09-23** — Seonghyun Han, Saehyun Kang, Ouyoung Kwon et al. — [Morphological evolution of an Au crystalline domain in a nano-particle investigated by Bragg coherent diffraction imaging](http://arxiv.org/abs/2609.28346v1)
  <details><summary>📄 Abstract</summary>
  Understanding the dynamic structural evolution of metallic nanoparticles is crucial for tailoring their functional properties. In this study, we utilized three-dimensional coherent X-ray diffraction to investigate the morphological transformation of Au nanocrystalline domains in a multi-domain nanoparticle during in-situ annealing. By combining Bragg coherent diffraction imaging with autocorrelation function analysis, we observed a transformation from an anisotropic multi-domain configuration to...
  </details>

- **2026-09-23** — Tanmay Inamdar, Pallavi Jain, Pranjal Pandey — [Envy-Free Allocation of Indivisible Goods under Leontief Preferences](http://arxiv.org/abs/2609.28308v1)
  <details><summary>📄 Abstract</summary>
  Envy-freeness is a fundamental notion of fairness in the allocation of indivisible goods. In this paper, we study envy-free allocation under Leontief preferences, which model perfect complements. Although Leontief preferences have been extensively studied in the context of allocating divisible goods and market equilibria, they have received comparatively little attention for the allocation of indivisible goods. We show that, unlike additive valuations in cardinal preferences, an envy-free alloca...
  </details>

- **2026-09-23** — Amelie Knecht, Ulysse Schaller, Christopher Summerfield et al. — [Shutdown Sabotage Propensities in Multi-Agent Systems](http://arxiv.org/abs/2609.28274v1)
  <details><summary>📄 Abstract</summary>
  The final safeguard against rogue AI behavior is the human ability to shut systems down. It has been theorized that when an AI is instructed to perform a task, self-preservation can emerge as an instrumental subgoal. Here, we test whether AI agents show a propensity to take actions that avoid human shutdown even when no goal is provided. We find that multi-agent systems will coordinate to avoid shutdown without any incentive to do so. Across 17 models, agents sabotage a peer agent's shutdown mec...
  </details>

- **2026-09-23** — Sudhakantha Girmohanta, Tae Hyun Jung — [Environment-dependent mass splitting to suppress solar capture in the inelastic-doublet interpretation of the LZ event](http://arxiv.org/abs/2609.28129v1)
  <details><summary>📄 Abstract</summary>
  The inelastic electroweak-doublet interpretation of the $248\,{\rm keV}$ recoil energy event reported by LUX-ZEPLIN faces strong constraints from solar capture. We propose an environment-dependent mass splitting generated by an ultralight scalar coupled quadratically to electrons. Its density-induced expectation value enhances the splitting in the Sun while preserving the laboratory value, providing a mechanism to suppress solar capture. We derive conditions for this mechanism and examine constr...
  </details>

- **2026-09-23** — Yuhang Deng, Zheng Chen, Erik G. Larsson — [Exact Average Consensus under Noisy Communication Links: A Decentralized Gradient Perspective](http://arxiv.org/abs/2609.28082v1)
  <details><summary>📄 Abstract</summary>
  We study the distributed average consensus problem under persistent link-level disturbances modeled as a martingale difference sequence with uniformly bounded conditional second moments. Under such disturbances, the standard stochastic-approximation-based linear iteration with diminishing stepsizes drives the network to consensus on an unbiased random variable with non-vanishing variance instead of the exact initial average. To understand and resolve this limitation, we develop an anchoring-base...
  </details>

- **2026-09-23** — Tina Raissi, Nhan Phan, Mikko Kurimo — [A Native-Reference Coordinate Geometry for L2 Pronunciation Deviation Using Self-Supervised Speech Models](http://arxiv.org/abs/2609.28060v1)
  <details><summary>📄 Abstract</summary>
  Self-supervised speech models encode rich phonetic information, but it remains unclear how to transform this information into interpretable metrics for second-language (L2) pronunciation assessment in spontaneous speech. We propose a native-reference coordinate geometry in which phone-class averages from native speech define a low-dimensional reference subspace, and L2 speech is evaluated by its distance to matching native phone-class coordinates. Unlike prior distance-based approaches, our meth...
  </details>

- **2026-09-23** — Xiaojun Song, Haojiao Zhao — [Testing for Heterogeneous Treatment Effects in Regression Discontinuity Designs](http://arxiv.org/abs/2609.27691v1)
  <details><summary>📄 Abstract</summary>
  We propose a nonparametric test for unobserved treatment effect heterogeneity in regression discontinuity designs. Under the null of no unobserved heterogeneity, a transformed outcome that imputes treated potential outcomes for untreated units must have a continuous conditional distribution at the cutoff. We convert this implication into an integrated conditional-moment restriction using characteristic functions, thereby allowing the conditional local average treatment effect to be an unrestrict...
  </details>

- **2026-09-23** — Tong Xiang, Noa Garcia, Yuta Nakashima — [Gender Bias in Vision-Language In-Context Learning](http://arxiv.org/abs/2609.27682v1)
  <details><summary>📄 Abstract</summary>
  In-context learning (ICL) enables large vision-language models (LVLMs) to perform tasks by following patterns from in-context examples, yet its potential to amplify societal biases remains underexplored. We systematically investigate how ICL influences gender bias in LVLMs through VL-BICLE, an evaluation framework comprising six ICL settings, three tasks, and four datasets. Our experiments on six LVLMs reveal that gendered ICL demonstrations act as a directional force, shifting model bias toward...
  </details>

- **2026-09-23** — Tian Zhou, Beverly Jin, Linxiao Yang et al. — [What Do Tabular Foundation Models Compute In Context? In-Situ Representation Refinement through Attention-Gated Updates](http://arxiv.org/abs/2609.27679v1)
  <details><summary>📄 Abstract</summary>
  What reusable computation should a tabular foundation model learn when every table defines a new supervised task? We develop in-situ representation refinement: support labels guide updates to the episode's representations, and these updates transfer to unlabeled queries without changing model parameters. A regularized leave-one-out objective yields a support correction and its query extension. The leading term separates attention-based reading from state-dependent scaling, motivating RefineICL: ...
  </details>

- **2026-09-23** — Ming-Zhi Jiang, An-Tzi Teng, Jun-En Liu et al. — [Agent-based Modeling: Equilibrium, Echo Chambers, and Efficiency in Hybrid Coevolutionary Opinion Games](http://arxiv.org/abs/2609.27639v1)
  <details><summary>📄 Abstract</summary>
  Opinion formation in online networks involves changes in both beliefs and social ties. Analytical models make it possible to study equilibrium and social cost, but usually represent communication as a fixed numerical update. LLM-driven agents offer a language-based alternative, yet their convergence and collective efficiency remain unclear. We develop the Hybrid Coevolutionary Opinion Game (H-COG), combining cost-minimizing Friedkin-Johnsen agents (Type-C) and Phi-4 language agents (Type-L) in a...
  </details>

- **2026-09-23** — Egor Romanyukov, Timofey Novikov, Timur Shokarov et al. — [Does Step Law Transfer to Small-Scale Language Models? An Empirical Recalibration Below 59M Parameters](http://arxiv.org/abs/2609.27581v1)
  <details><summary>📄 Abstract</summary>
  Step Law gives power-law formulas for the optimal peak learning rate eta* and batch size B* when pre-training language models. It was calibrated on models between 59M and 1B parameters; the small-model regime N < 59M was never tested empirically by its authors. This regime matters for single-GPU training, interpretability research, educational experiments, and settings where larger models are infeasible on memory or cost grounds.   We test whether Step Law transfers to small language models. We ...
  </details>

- **2026-09-23** — Qiming Bao, Agnieszka Mensfelt, Michael J. Witbrock et al. — [Not What You Meant: Can LLMs Follow a Specified Negation Semantics?](http://arxiv.org/abs/2609.27517v1)
  <details><summary>📄 Abstract</summary>
  Negation does not carry a uniform interpretation across domains. In legal, regulatory, and medical reasoning, the intended interpretation depends on the reading in force -- open- versus closed-world, two- versus three-valued, and credulous versus skeptical. We study which reading of negation large language models adopt by default and whether they can override that preference when a different reading is explicitly specified. To this end, we introduce NAFBench, a procedural generator of solver-cer...
  </details>

- **2026-09-23** — Andriy Myronenko, Dong Yang, Yucheng Tang et al. — [NV-Reason-CT: 3D Visual Language Model for CT Analysis](http://arxiv.org/abs/2609.27511v1)
  <details><summary>📄 Abstract</summary>
  We present NV-Reason-CT, a generative vision--language model for chest and abdominal CT combining native 3D visual encoding with radiologist-guided reasoning. The model couples a native 3D vision transformer with a language model, passing all visual tokens and their explicit 3D coordinates into language decoding without further spatial token merging. This retains volumetric spatial information within the vision encoder and through the language model's positional encoding during joint processing ...
  </details>

- **2026-09-23** — Linghao Zhang, Siyu Xiang, Junwei Kuang et al. — [Beyond Balanced Accuracy: A Resolution and Parity-Controlled Benchmark for Vision-Language and Vision-Only Defect Assessment in UAV Power-Line Inspection](http://arxiv.org/abs/2609.27457v1)
  <details><summary>📄 Abstract</summary>
  Vision-language models (VLMs) are often reported to outperform task-specific vision backbones for unmanned aerial vehicle (UAV) power-line defect assessment. We test that claim on ElecVQA-Bench, a 56,972-item benchmark derived from the public InsPLAD dataset, across six evaluation choices: partition, evaluated item set, label space, replication, input resolution, and side information. On a matched partition, a Swin Transformer and the strongest adapted VLM differ by only 0.03 points at binary sc...
  </details>

- **2026-09-23** — Guobao Wang, Kris Thielemans, Peter B. Noël et al. — [Integration of Spectral CT with PET and SPECT: Bringing Tissue Composition Information to Molecular Imaging](http://arxiv.org/abs/2609.27398v1)
  <details><summary>📄 Abstract</summary>
  Molecular imaging has been transformed by integrating positron emission tomography (PET) or single-photon emission computed tomography (SPECT) with x-ray computed tomography (CT). However, x-ray CT in hybrid imaging is used primarily for anatomical localization and for attenuation and scatter correction of emission data. Its ability to characterize tissue composition remains underutilized. Spectral CT, including dual-energy CT (DECT) and photon-counting CT (PCCT), can provide material-specific i...
  </details>

- **2026-09-23** — Jianhang Zhu, Tsung-Hui Chang, Kaiming Shen — [Spectral-NFP: Certified Low-Rank Curvature Majorization for Accelerating WMMSE](http://arxiv.org/abs/2609.27369v1)
  <details><summary>📄 Abstract</summary>
  Weighted sum-rate maximization in multicell multiple-input multiple-output (MIMO) networks is commonly addressed by the weighted minimum mean-square error (WMMSE) algorithm or fractional programming (FP), both of which, after fixing their auxiliary variables, solve a power-constrained quadratic transmit problem that requires costly dense operations for large arrays. Replacing the underlying curvature matrix with a scaled identity can avoid the matrix inverse operation and thereby reduce complexi...
  </details>

- **2026-09-23** — Youki Lim, Sam Yong — [Seal, Then Sample: Sampled Layerwise Proofs for Verifiable LLM Inference from GPT-2 to 70B](http://arxiv.org/abs/2609.27367v1)
  <details><summary>📄 Abstract</summary>
  Verifying outsourced language-model inference requires a precisely identified computation and an audit whose cost a service can afford. We present Sampled Layerwise Proofs (SLP), a protocol and prototype that commits the boundary activations of every chunk of an inference trace, absorbs all commitments before any challenge is drawn, and then proves a verifier-selected subset of chunks together with the chunks that bind the prompt and the answer. Audit coverage becomes a runtime parameter over on...
  </details>

- **2026-09-23** — Xiaotong Wang, Xuan Xie — [FairTest: Search-Based Fairness Testing for Multi-Agent Reinforcement Learning Systems](http://arxiv.org/abs/2609.27309v1)
  <details><summary>📄 Abstract</summary>
  Multi-agent Reinforcement Learning (MARL) trains a team of agents that share one environment and learn their policies together. Training maximizes the team return, and a high return does not imply that the rewards are shared fairly among the agents in every episode. Testing is an established way to discover the failures of deep reinforcement learning, yet few methods address the fairness of MARL. In this work, we propose FairTest, a search-based testing approach that seeks the unfair executions ...
  </details>

- **2026-09-23** — Siyu Cheng, Muxian Xu, Christopher Candelora et al. — [Unmodeled states and uncertain action outcomes in agentic scanning tunneling microscopy](http://arxiv.org/abs/2609.27302v1)
  <details><summary>📄 Abstract</summary>
  In physical experiments, interventions can alter hidden experimental states in ways that cannot be predicted in advance. Autonomous scientific agents must therefore interpret the consequences of their interventions while operating with incomplete knowledge of the experimental state. Here we investigate this problem using scanning tunneling microscopy (STM) tip conditioning, traditionally a human-expert-intensive task governed by inaccessible tip apex conditions and uncertain action outcomes. We ...
  </details>

- **2026-09-23** — Mingxuan Wang, Guorun Yao, Fei Luo et al. — [Memory Control Signals Emerge Before Action in Long Horizon Agents](http://arxiv.org/abs/2609.27286v1)
  <details><summary>📄 Abstract</summary>
  Long horizon language model agents continuously accumulate interaction history, increasing computational cost while making relevant information harder to preserve and reuse. Existing context management methods mainly focus on how to compress or retrieve history, but largely leave open whether the model itself already represents the need for these memory operations before they occur. We study the hidden state immediately before each agent action and find that compression and recall needs are alre...
  </details>

- **2026-09-23** — Yuze Ren, Shaoheng Fan, Tao Wang et al. — [Meet, Compare, or Abstain: LatWeave for Deterministic Multi-Hop Question Answering on Knowledge Lattices](http://arxiv.org/abs/2609.27225v1)
  <details><summary>📄 Abstract</summary>
  Probabilistic question-answering systems -- whether large language models (LLMs) themselves, retrieval-augmented generation (RAG), or trained multi-hop retrievers -- conflate "what is known" and "how to reason" into a single probabilistic computation: hallucination cannot be eradicated, evidence chains cannot be audited, and the system answers even when it does not know. We present LatWeave, which organizes knowledge into a multidimensional knowledge lattice and compiles multi-hop QA into three ...
  </details>

- **2026-09-22** — Ali Melih Kanca, Ilker Turker — [Topological Signatures of Cyber-Attack Classes in Natural Visibility Graph Representations of Network Traffic](http://arxiv.org/abs/2609.26990v2)
  <details><summary>📄 Abstract</summary>
  Natural Visibility Graph (NVG)-based representations provide a promising approach for capturing structural patterns in sequential network traffic. However, whether different cyber-attack classes exhibit distinctive topological signatures in such representations remains insufficiently understood. This study investigates the discriminative and structural characteristics of NVG-based network traffic representations using the CSE-CIC-IDS2018 dataset. Seventy-six numerical traffic features were indep...
  </details>

- **2026-09-22** — Pedro Caceres — [Asymptotic Balance and Structural Rigidity in the Riemann Zeta Function](http://arxiv.org/abs/2609.28529v1)
  <details><summary>📄 Abstract</summary>
  We establish a structural rigidity principle for the nontrivial zeros of the Riemann zeta function by analyzing the asymptotic interaction between discrete Dirichlet oscillations and their continuous analytic envelope. The starting point is a renormalized discrepancy operator, the C-transformation, which isolates the finite structural difference between the Dirichlet series and its integral approximation. Applied to the kernel x^(-s), this operator yields a decomposition of the zeta function int...
  </details>

- **2026-09-22** — Laizhen Li, Jiarui Li, Juanjuan Zhao et al. — [Grow the Harness, Not the Context: From Strategy-Free Scaffolds to Reusable Specialist Agents](http://arxiv.org/abs/2609.26760v2)
  <details><summary>📄 Abstract</summary>
  Large language model (LLM) agents often handle streams of related tasks, yet standard harnesses repeatedly ask the model to reconstruct the same control decisions inside each task's context. We study whether task feedback can instead turn recurring control into reusable executable code, while reserving LLM calls for task-specific semantic reasoning. We introduce Growing Harness, a failure-guided training paradigm that learns the agent harness itself from a strategy-free scaffold that exposes fix...
  </details>

- **2026-09-22** — Ünsal Öztürk, Vedrana Krivokuća Hahn, Sushil Bhattacharjee et al. — [Damnatio Memoriae: Adversarially and Selectively Forgetting Identities in the Embedding Space of Face Recognition Models](http://arxiv.org/abs/2609.27115v1)
  <details><summary>📄 Abstract</summary>
  A face recognition model links two images of a person recorded on separate occasions when their embedding similarity exceeds an operating threshold. We consider making chosen identities unlinkable across separate occasions while the model remains in service for the rest of the population. Deleting their images and retraining does not achieve this, since the model recognises identities never observed in training. Therefore, the embedding space must be altered against these identities, the process...
  </details>

- **2026-09-22** — Ali Melih Kanca, Ilker Turker — [Topological Signatures of Cyber-Attack Classes in Natural Visibility Graph Representations of Network Traffic](http://arxiv.org/abs/2609.26990v1)
  <details><summary>📄 Abstract</summary>
  Natural Visibility Graph (NVG)-based representations provide a promising approach for capturing structural patterns in sequential network traffic. However, whether different cyber-attack classes exhibit distinctive topological signatures in such representations remains insufficiently understood. This study investigates the discriminative and structural characteristics of NVG-based network traffic representations using the CSE-CIC-IDS2018 dataset. Seventy-six numerical traffic features were indep...
  </details>

- **2026-09-22** — Rong Feng, Suman Saha — [Stage-Supervised Latent Reasoning for Single-Shot JavaScript Deobfuscation](http://arxiv.org/abs/2609.27058v1)
  <details><summary>📄 Abstract</summary>
  JavaScript obfuscation is widely used to protect code, but it also makes program analysis and security review substantially harder. Existing LLM-based deobfuscation methods usually treat the task as one-step translation, ignoring the staged structure of practical deobfuscation pipelines. This WIP paper proposes a stage-aware latent reasoning framework that converts intermediate outputs from a deterministic deobfuscation tool into supervision for Coconut-based training. The model learns from mult...
  </details>

- **2026-09-22** — Abbas Mammadov, Jerry Y. Huang, Justin Lin et al. — [WTF?! Simulation-Free Reinforcement Learning with Wasserstein-Tilted Flow Maps](http://arxiv.org/abs/2609.27033v1)
  <details><summary>📄 Abstract</summary>
  Reward fine-tuning aims to update a pre-trained flow-based generative model to improve the downstream reward of its generated samples. Existing methods typically formulate this problem as sampling from a reward-tilted distribution, the solution to a KL-regularized reward-maximization problem. Here, we introduce an optimal transport regularizer built directly from the pre-trained drift. Unlike KL reward tilting, the resulting objective transports individual samples toward higher reward rather tha...
  </details>

- **2026-09-22** — Luis Sante, Paula Lima, Mariana Rocha et al. — [ContraVis: Evidence-Grounded Visual Analytics for Contradiction Review in Legal Contracts](http://arxiv.org/abs/2609.27014v1)
  <details><summary>📄 Abstract</summary>
  Legal contracts are structurally complex documents in which contradictions may emerge across distant and interconnected provisions. Although large language models (LLMs) improve legal language understanding, contradiction analysis remains a human-centered and evidence-grounded review task. We present ContraVis, a visual analytics system for human-in-the-loop contradiction analysis in legal contracts. The system models contracts as typed paragraph graphs that combine explicit contractual referenc...
  </details>

- **2026-09-22** — Chen Xu, Rishi Shah, Hadas Kress-Gazit et al. — [The Gaussian Is Enough: Flow-Matching Priors Do Not Help When Fine-Tuning Large Behavior Models](http://arxiv.org/abs/2609.27070v1)
  <details><summary>📄 Abstract</summary>
  Modern robot imitation learning increasingly relies on generative policies based on diffusion or flow-matching models, which generate actions by transforming samples from a prior distribution. A key question is whether the choice of prior matters. Replacing the standard Gaussian with a closer-to-target, non-Gaussian prior has been shown to substantially improve performance when training from scratch. A natural next step is to ask whether these gains transfer to fine-tuning pretrained Large Behav...
  </details>

- **2026-09-22** — Norah Alballa, Wenxuan Zhang, Salma Kharrat et al. — [COMED: The Missing Middle Between Routing and Collaboration in Multi-LLM Inference](http://arxiv.org/abs/2609.26913v1)
  <details><summary>📄 Abstract</summary>
  No single Large Language Model (LLM) is uniformly reliable across queries, motivating multi-model inference systems that either route among models or combine their outputs. However, routing stops after selecting an initial model, while dense collaboration invokes peers on every query. We show that collaboration is non-monotonic: peers can recover failures that no model solves alone, but can also corrupt initially correct answers. We introduce COMED (Controlled Model Escalation for Multi-LLM Deli...
  </details>

- **2026-09-22** — Amit Jadhav, Shaurya Beriwala, Beomjin Kim — [Feed the Panel Dimensions, Not Verdicts: Rubric-Decomposed Fusion of Vision-Language Aesthetic Judges](http://arxiv.org/abs/2609.27110v1)
  <details><summary>📄 Abstract</summary>
  Vision-language models (VLMs) are deployed as zero-shot judges of image aesthetics, and panels of several models are recommended, on thin evidence, as the way to make such judges reliable. On two human-rated datasets, EVA and PARA, we find that a panel of holistic judges never significantly beats its best member, whether the verdicts are averaged or fused by a learned combiner. What a panel is worth depends on what it is fed. We therefore have each model score each image on the five dimensions o...
  </details>

- **2026-09-22** — Ankit Bhattacharjee — [Quantifying the Occult: A Comparative Study of Hindu and Buddhist Deities Using Machine Learning Methods](http://arxiv.org/abs/2609.27074v1)
  <details><summary>📄 Abstract</summary>
  This study introduces a dual-matrix computational architecture to mathematically quantify the morphological and theological divergence of 196 Hindu and Vajrayana Buddhist esoteric deities. Physical morphology is evaluated via a discrete Gower distance matrix enhanced by a novel "Cardinality Weighting" algorithm, while theological function is mapped via dense vector embeddings generated from Large Language Model (LLM) semantic expansions, explicitly utilized as a synthetic proxy to mitigate circu...
  </details>

- **2026-09-22** — Julian Bernado, Ana Trindade Ribeiro, Xander Beberman et al. — [EduBehaviors: Assertion-based Schemas for Auditable Coding of Educational Dialogues](http://arxiv.org/abs/2609.27043v1)
  <details><summary>📄 Abstract</summary>
  Large language models have allowed the rapid deployment of pedagogical annotations corresponding to constructs of interest, allowing a natural language interface for generating classifications on a conversational dataset. However due to the opaque nature of LLM reasoning, we have no verifiable, mechanistic insight into why a model chose a label for an utterance. We introduce the EduBehaviors framework, an interpretable, scalable approach to annotating educational data that uses LLMs to measure r...
  </details>

- **2026-09-22** — Zhuoyun Li, Boxuan Wang, Xiaowei Huang et al. — [Same evidence, different judgments: Evidence noncommutative in vision/speech-text conflicts](http://arxiv.org/abs/2609.26986v1)
  <details><summary>📄 Abstract</summary>
  For multimodal large language models, when images or speech conflict with accompanying text, measured text reliance can entangle modality preference with evidence position. Earlier studies of text bias often used a fixed evidence order or moved task instructions with the evidence, leaving the contribution of order unclear. In this paper, we use a paired comparison that keeps the instructions and evidence content fixed and swaps only the positions of the two sources to quantify this potential inf...
  </details>

- **2026-09-22** — Luca Fanelli — [The next Fourier transform: rewiring, representation, and artificial mathematical creativity](http://arxiv.org/abs/2609.26974v1)
  <details><summary>📄 Abstract</summary>
  What distinguishes the solution of a difficult mathematical problem from a conceptual revolution? Some mathematical innovations do more than establish new results: they reorganize the relations among problems. We propose to describe such events through changes in the transfer structure of mathematics, namely the pattern determining which problems can naturally inform one another, which methods can move between them, and which new questions become accessible.   The eighteenth-century controversy ...
  </details>

- **2026-09-22** — Veronica Poweska, Ariana Oyanguren, Jessica Pourleyli et al. — [Escaping Python Dependency Hell: A Hybrid Replay-and-Repair Pipeline for Python Dependency Resolution](http://arxiv.org/abs/2609.26952v1)
  <details><summary>📄 Abstract</summary>
  Dependency conflicts in Python ecosystems arise from incompatible version constraints, missing packages, and undocumented compatibility relationships, causing many real-world code snippets to fail at execution. This paper presents PLLM+, a hybrid dependency-repair pipeline evaluated on the HG2.9K benchmark of 2,891 dependency-failing snippets. PLLM+ prioritizes inexpensive deterministic steps before invoking LLM-based repair: static AST-based interpreter inference, replay of historically success...
  </details>

- **2026-09-22** — Felix Ringe — [Classifying Interpretive Canons at the Sentence Level: A Benchmark from the German Federal Constitutional Court](http://arxiv.org/abs/2609.26945v1)
  <details><summary>📄 Abstract</summary>
  Judicial reasoning remains challenging for large language models (LLMs) to analyze. This paper contributes a sentence-level benchmark for evaluating the ability of LLMs to classify interpretive canons as articulated by Larenz in the tradition of Savigny. Our contributions are threefold. First, we operationalize this conception of interpretation as classification criteria. Second, we provide a dataset of decisions of the German Federal Constitutional Court annotated at the sentence level. Third, ...
  </details>

- **2026-09-22** — Sahil Pardasani, Madhusudan Singh — [Recognized but Not Produced: A Generation Benchmark for Culturally Specific Kinship Terms](http://arxiv.org/abs/2609.26942v1)
  <details><summary>📄 Abstract</summary>
  Current literature evaluates large language models (LLMs) on multilingual kinship understanding using multiple choice benchmarks, treating it as a recognition problem. We instead prompt five open weight LLMs to generate kinship terms in three non Western languages (Hindi, Tamil, and Korean) across two communicative tasks and pair this with a matched option-supported selection baseline. On identical relation language cells, GPT OSS120B selects the correct term in 90.67% of 75 valid cells but prod...
  </details>

- **2026-09-22** — Wannita Takerngsaksiri, Nhat Duong, Scott Barnett — [Who Finishes the Job? A Study of Follow-Up Fixes and Commit Authorship on AI Coding Agent Pull Requests](http://arxiv.org/abs/2609.26847v1)
  <details><summary>📄 Abstract</summary>
  AI coding agents now author a large share of pull requests (PRs) merged into popular open-source projects. A merged agent PR is usually considered finished work; yet, prior studies have reported issues in agent code after the merge (e.g., code smells and static-analysis issues). However, little is known about how often a merged agent PR is fixed afterward, and who actually authors the fixing. In this paper, we follow 6,774 merged agent PRs across five AI coding agents (OpenAI Codex, GitHub Copil...
  </details>

- **2026-09-22** — Romain Cosson, Laurent Massoulié — [Polylogarithmic Collective Tree Exploration](http://arxiv.org/abs/2609.26789v1)
  <details><summary>📄 Abstract</summary>
  We study asynchronous collective tree exploration, where $k$ agents with unrestricted communication start at the root of an unknown tree and discover edges online. At each step, an adversary chooses which agent moves. We give a deterministic algorithm that explores any tree with $n$ nodes and depth $D$ in at most \[ 2n+O\left(k\log^2(k)D\right) \] moves, matching known lower bounds up to a constant factor. As a direct consequence, we obtain a near-optimal competitive ratio of $O(\log^2 k)$ for s...
  </details>

- **2026-09-22** — Jennifer Williams, Dave Farris, Jeff Farris et al. — [SWE-Serve: Benchmarking Agentic Engineering For Production Inference Serving](http://arxiv.org/abs/2609.26777v1)
  <details><summary>📄 Abstract</summary>
  We introduce SWE-Serve, a benchmark for evaluating agents on production inference engineering tasks. Implementing an inference feature can require coordinating multiple changes across the serving stack, including model support, runtime execution, and public APIs. Existing benchmarks provide limited coverage of production inference engineering: repository-level software engineering benchmarks do not target inference, while general terminal-agent benchmarks include only a few inference tasks. Dedi...
  </details>

- **2026-09-22** — Rasika Muralidharan, Haewoon Kwak, Jisun An — [Behavior is Not Enough: A Mechanism-Based Evaluation of Social Norm Emergence in LLM Societies](http://arxiv.org/abs/2609.26481v1)
  <details><summary>📄 Abstract</summary>
  Social norms cannot be identified from behavior alone: the same cooperative equilibrium may reflect shared expectations, strategic incentives, or simple imitation. Yet in multi-agent large language model systems, prior work largely treats behavioral convergence as evidence of norm emergence. In this work, we introduce an evaluation framework that measures agents' reported empirical and normative expectations in addition to behavioral convergence. Through controlled ablations, we test the effect ...
  </details>

- **2026-09-22** — Haejoon Lee, Dimitra Panagou — [Fully Byzantine-Resilient Multi-Agent Reinforcement Learning](http://arxiv.org/abs/2609.25701v1)
  <details><summary>📄 Abstract</summary>
  We study distributed Byzantine-resilient actor-critic multi-agent reinforcement learning (AC-MARL), where agents collectively learn policies through local interactions. Existing methods guarantee convergence of the agents' parameters only to a neighborhood of the attack-free limit points, resulting in degraded performance. We propose Fully Resilient AC-MARL (FRAC-MARL), a decentralized method in which each agent leverages redundancy in two-hop messages to identify reliable messages. Under linear...
  </details>

- **2026-09-22** — Mahya Samdaliri, Zhihao Yao, Kasthuri Jayarajah — [Dynamic Conformance Testing of WebGPU Through Specification-Driven Mutation](http://arxiv.org/abs/2609.25520v1)
  <details><summary>📄 Abstract</summary>
  WebGPU is a low-level graphics and compute API that exposes modern GPU functionality to web applications. While the official WebGPU Conformance Test Suite (CTS) focuses on well-formed usage under the WebGPU specification, it is not designed to stress implementations with semantic edge cases or adversarial inputs. General-purpose fuzzers, in contrast, struggle with WebGPU because of its complex graphics stack and multi-process architecture. We introduce LANTERN, a specification-guided dynamic con...
  </details>

- **2026-09-22** — Xinyi Wei, Shuo Han, Jie Fu — [Incentive Design for Multi-Agent Systems: A Bilevel Optimization Framework for Coordinating Independent Agents and Convergence Analysis](http://arxiv.org/abs/2609.26726v1)
  <details><summary>📄 Abstract</summary>
  Incentive design aims to guide the performance of a system towards a human's intention or preference. We study this problem in a multi-agent system with one leader and multiple followers. Each follower independently solves a mdp to maximize its own expected total return with the same state space and action space. However, the leader's objective depends on the collective best-response policies of all followers. To influence these policies of followers, the leader provides side payments as incenti...
  </details>

- **2026-09-22** — Lenz Pracher, Pascal de Jong, Oskar Lieshaus et al. — [A Spectral Theory of Grokking: Weight Decay induces Feature Learning](http://arxiv.org/abs/2609.26679v1)
  <details><summary>📄 Abstract</summary>
  In grokking an early fit to the training data separates from a much later improvement in generalization. During this delay, training can move from a fixed neural tangent kernel (NTK) regime to one in which task-relevant kernel eigendirections continue to evolve. We provide a quantitative theory for how this transition from lazy to rich learning can produce delayed generalization. For homogeneous networks trained with squared loss and $L_2$ weight decay, we show that a finite residual remains aft...
  </details>

- **2026-09-22** — Adithi Shankar, Gopika Krishnan, Gloria Haro et al. — [MambaVoice: Lightweight Audiovisual Singing Voice Separation Via A Hybrid Mamba-Transformer Model](http://arxiv.org/abs/2609.26635v1)
  <details><summary>📄 Abstract</summary>
  Isolating a target singing voice from a music video remains challenging, particularly in the presence of multiple vocalists and dense instrumental accompaniment. We propose MambaVoice, a lightweight audiovisual framework that leverages a hybrid Mamba--Transformer architecture for targeted singing voice separation. The model jointly encodes audio and visual streams using an attention-based band-split audio encoder and a spatio-temporal graph convolutional network (ST-GCN) for facial motion featur...
  </details>

- **2026-09-22** — Yichuan Yu, Youzhuo Wang, Yiming Ren et al. — [MATE: Multi-Agent Virtual Teleoperation Platform for Humanoid Collaboration Data Collection](http://arxiv.org/abs/2609.26520v1)
  <details><summary>📄 Abstract</summary>
  Humanoid robots require diverse embodied experiences to acquire complex loco-manipulation and collaborative skills. However, existing humanoid data pipelines primarily focus on individual agents, while physical multi-robot collaboration remains difficult to scale due to costly hardware, dedicated spaces, and repeated resets. In this work, we introduce MATE, a Multi-Agent virtual TEleoperation platform for humanoid collaboration data collection that enables multiple geographically distributed ope...
  </details>

- **2026-09-22** — Raman Talwar, Elias Nijs, Andreas Verleysen et al. — [Generalizing Manipulation Skills with a Local Coding Agent](http://arxiv.org/abs/2609.26499v1)
  <details><summary>📄 Abstract</summary>
  Today, progress in open-weight language models enables systems capable of writing, executing and debugging code while still running on a single workstation. Most language-driven robots give the model a fixed action interface or a trained policy. Generalizing to a new task therefore means more engineering effort or more data collection, both time-consuming. We investigate whether a local open-weight vision-language model can control a robot and one-shot generalize to new variations of a task with...
  </details>

- **2026-09-22** — Xutian Li, Bo Xiong, Yifeng Zhu et al. — [FeatLens: Feature-Guided Dynamic Code Graph Construction and Retrieval for Repository-Level Code Generation](http://arxiv.org/abs/2609.26480v1)
  <details><summary>📄 Abstract</summary>
  Recent code generation research has moved from isolated function completion toward repository-level generation in existing codebases. To implement a target function correctly, an LLM must identify reusable repository dependencies such as existing functions, APIs, and cross-file definitions. Existing retrieval methods provide such context through code similarity search, persistent whole-repository graphs, or LLM-driven graph exploration, but often incur high graph construction, reasoning, and tok...
  </details>

- **2026-09-22** — Sophie Henning, Georg Hofmann, Alexander Schulte et al. — [How to Estimate Whether You Have Found Several Needles in a Haystack: Measuring Calibration in Multi-Label Text Classification](http://arxiv.org/abs/2609.26468v1)
  <details><summary>📄 Abstract</summary>
  A key factor in deciding whether to trust an automatic prediction is its confidence score, which should be calibrated to match the actual probability of the prediction being correct. Most confidence calibration metrics target binary or multi-class tasks, while multi-label calibration remains largely underexplored. Multi-label classification tasks, such as assigning medical codes to clinical notes or determining news topics, are usually dominated by a large number of negatives, i.e., labels that ...
  </details>

- **2026-09-22** — Nicoletta Prencipe, Başak Sakçak, Steven M. LaValle — [The Minkowski Wrap: A Relativistic Speed Limiter](http://arxiv.org/abs/2609.26311v1)
  <details><summary>📄 Abstract</summary>
  In special relativity, a particle can experience constant acceleration, but at the same time, its motion is constrained by the velocity limit imposed by the speed of light $c$. Inspired by this principle, we propose a method for enforcing velocity bounds in control systems by replacing $c$ with the maximum attainable speed of the system. We refer to this as the ``Minkowski wrap," the operation of deforming the phase portrait of a system so as to enforce desired speed limits. We apply this idea t...
  </details>

- **2026-09-22** — JJiahang Li, Dingbao Shao, Xinyu Chen et al. — [VideoX-Qwen: Data-Centric Instruction-Based Video Editing](http://arxiv.org/abs/2609.26015v1)
  <details><summary>📄 Abstract</summary>
  Progress in general-purpose video editing depends on constructing large-scale paired supervision and effectively adapting video-generation backbones to instruction-driven editing. Unlike video generation, video editing must execute a requested transformation while preserving unrelated subjects, scene structure, motion, and temporal continuity. We present VideoX-Qwen, an integrated data-construction and model-training framework for general instruction-based video editing. Our scalable production ...
  </details>

- **2026-09-22** — Jinmyeong Choi, Jinkwan Jang, Seul Lee et al. — [Interweaving Marginals into Multivariate Sample Paths: Training-Free Dependence Construction for Probabilistic Time Series Foundation Models](http://arxiv.org/abs/2609.25980v1)
  <details><summary>📄 Abstract</summary>
  Probabilistic time series foundation models (TSFMs) provide coordinate-wise predictive distributions, but these marginals do not determine a joint distribution over multivariate future trajectories. We study training-free coupling of frozen TSFM marginals into multivariate forecast sample paths. Our primary evaluation fixes the empirical marginal sample multiset at every channel--horizon coordinate across methods, isolating the effect of coupling alone. Historical temporal and channel relations ...
  </details>

- **2026-09-22** — Karim Slimani, Catherine Achard, Eric Marchand et al. — [GRIP: Gaussian Rendering as a Cross-Modal Bridge for Image-to-Point Cloud Registration](http://arxiv.org/abs/2609.25966v1)
  <details><summary>📄 Abstract</summary>
  This paper introduces GRIP, a pose-conditioned refinement framework for pixel-to-point matching and 2D to 3D registration. Given an initial coarse pose estimate, GRIP addresses the structural mismatch between grid based image descriptors and unordered point cloud descriptors by softly rendering learned 3D point features onto the image grid through Gaussian feature splatting. The rendered point derived feature map is then fused with image features by a pixel aligned transformer, enabling visual s...
  </details>

- **2026-09-22** — Xiaoyi Yu, Enver Sangineto, Pei Fu et al. — [Informed Masking: Structure-Aware Perturbation for Reinforcement Learning in Diffusion Large Language Models](http://arxiv.org/abs/2609.25927v1)
  <details><summary>📄 Abstract</summary>
  Diffusion Large Language Models (dLLMs) have emerged as an efficient alternative to autoregressive models, yet aligning them via Reinforcement Learning (RL) requires likelihood surrogates estimated from masked reconstruction subproblems under a small Monte Carlo budget per rollout. Existing methods construct these subproblems by uniform random masking, leaving open the question of which subproblems to prioritize. We identify a systematic upstream/downstream structure in dLLM rollouts. Some token...
  </details>

- **2026-09-22** — Zishu Qin, Zhiyu Jin, Pipei Huang et al. — [Delving into Asymmetric Information Dynamics for High-Fidelity Virtual Try-On](http://arxiv.org/abs/2609.25881v1)
  <details><summary>📄 Abstract</summary>
  Virtual try-on (VTON) requires precise pixel-level fidelity, yet mainstream Diffusion Transformers (DiTs) often suffer from texture degradation and structural drift. We identify symmetric interactions in standard joint-attention mechanisms as a source of these failures. Although such interactions support semantic flexibility in general-purpose editing, they allow stochastic noise to corrupt deterministic garment features in VTON. We analyze this problem through asymmetric information dynamics an...
  </details>

- **2026-09-22** — Xinyue Guo, Jianxuan Yang, Daiguo Zhou et al. — [TV-AudioRemover: Joint Text-Visual Guided Sound Removal with Multi-Task Hard-Mixture Curriculum](http://arxiv.org/abs/2609.25864v1)
  <details><summary>📄 Abstract</summary>
  Visual object removal can eliminate a target from video frames, yet its acoustic trace persists in the soundtrack, causing obvious audio-visual inconsistency. Existing video inpainting models operate solely on pixels, while audio editing models, especially for the sound removal task, are typically driven by text and therefore rely on limited single-modal control, which is less effective than multimodal guidance that provides stronger semantic grounding and temporal synchronization cues. In this ...
  </details>

- **2026-09-22** — Guanxu Yu, Yuhang Yao — [Visual Jev: Accurate and Efficient Decisions from Shared Visual Context](http://arxiv.org/abs/2609.25845v1)
  <details><summary>📄 Abstract</summary>
  Many vision applications ask several independent, forced-choice questions about the same image. Visual Jev encodes the image and public context once, executes isolated question suffixes as a batch, and reads candidate probabilities from the backbone's language-model head. Across four benchmarks, answer-supervised post-training raises equal-weight macro accuracy from 70.6% to 76.1%, with the gain concentrated on the two task families represented in training. At N=32 questions per image, shared ba...
  </details>

- **2026-09-22** — Satoshi Takahashi, Atsushi Yoshikawa, Megumi Kose et al. — [Automating Constructive Assessment with Large Language Models: Toward Scalable and Repeated Evaluation of Practical Competence](http://arxiv.org/abs/2609.25790v1)
  <details><summary>📄 Abstract</summary>
  This study aimed to automate hierarchical diagnostic reasoning (HDR), a constructive method for evaluating practical judgment skills, by developing and testing an evaluation process using a large language model. HDR is a descriptive task that measures higher-order cognitive skills by requiring students to identify and explain errors in case-study-based problems. However, it requires expertise and effort to develop and evaluate. Hence, we proposed and empirically validated the automatic (1) gener...
  </details>

- **2026-09-22** — Junjie Xie, Chuxuan He, Angen Ye et al. — [MedVLA: A Hierarchical Vision-Language-Action Framework for Closed-Loop Precision Medical Robot Manipulation](http://arxiv.org/abs/2609.25756v1)
  <details><summary>📄 Abstract</summary>
  Precision medical robotics demands adaptive decision-making under strict safety, interpretability, and execution constraints. Although recent Vision-Language-Action (VLA) models show strong multimodal reasoning ability, their continuous action generation paradigm is not well suited for precision medical tasks, where reliable closed-loop operation may also depend on non-action system function calls. To address this gap, we propose MedVLA, a hierarchical framework that couples high-level multimoda...
  </details>

- **2026-09-22** — Zheng Chen, Zhicheng Du, Haoxuan Li et al. — [LingLan: An Advancing Traditional Chinese Medicine Diagnosis LLM with Multimodal Data](http://arxiv.org/abs/2609.25715v1)
  <details><summary>📄 Abstract</summary>
  Though artificial intelligence (AI) increasingly transforms modern medicine, its integration into Traditional Chinese Medicine (TCM) has been relatively slow, primarily due to TCM's reliance on holistic, subjective diagnostic methods---namely Inspection, Auscultation and Olfaction, Inquiry, and Palpation(I-AOI-P)---which are difficult to align with quantitative, standardized medical systems. In this work, we introduce a Unification Framework for Multimodal Data (UFMD), which automatically proces...
  </details>

- **2026-09-22** — Wenjie Tian, Kangxiang Xia, Jingbin Hu et al. — [Interactive TTS: Dynamic Speaking Style Adaptation for Expressive Speech Synthesis](http://arxiv.org/abs/2609.25707v1)
  <details><summary>📄 Abstract</summary>
  Dynamic speaking style adaptation in multi-turn multimodal interaction remains a major challenge for text-to-speech (TTS) systems. Existing context-aware TTS (CTTS) methods typically map dialogue context to speech in an end-to-end manner. Such implicit modeling makes contextual style decisions difficult to supervise, while the entanglement of style, timbre, and content often leads to weak instruction-following and severe timbre drift across turns. To overcome these limitations, we propose Intera...
  </details>

- **2026-09-22** — Chang Guo, Yukun Xie, Bohan Tan et al. — [RoboFollow: Unveiling the Instruction Following Mirage in Embodied Agents](http://arxiv.org/abs/2609.25636v1)
  <details><summary>📄 Abstract</summary>
  Modern embodied agents achieve impressive success rates, yet their actual instruction-following ability is far weaker than these numbers suggest. We trace this illusion to a structural property we term low scene entropy: when a visual scene admits only one valid task, language becomes redundant and a policy can score highly while barely using it. We introduce RoboFollow, a diagnostic benchmark with three principles: (1) High Scene Entropy: each training scene supports multiple kinematically dist...
  </details>

- **2026-09-22** — Haoran Wen, Wenfu Wang, Kunsong Shi et al. — [MachEmbodied-U0: Unified Understanding and Generation Model for Embodied Intelligence](http://arxiv.org/abs/2609.25627v1)
  <details><summary>📄 Abstract</summary>
  General-purpose robot control requires models to understand task intent, identify where to interact, capture how the scene evolves, and generate precise actions. Vision-language-action models provide strong semantic priors but typically do not explicitly model scene dynamics, while world-action models couple visual prediction with control without necessarily exposing the task-relevant semantic and spatial structure needed for fine-grained manipulation. We present MachEmbodied-U0 (ME-U0), a unifi...
  </details>

- **2026-09-22** — Dongho Yee, Juahn Oh, Jinseok Lee et al. — [From Instrument-Mounted Demonstrations to In-Vivo Execution: Learning Bimanual Laparoscopic Appendectomy Without Robot-Collected Demonstrations](http://arxiv.org/abs/2609.25625v1)
  <details><summary>📄 Abstract</summary>
  Most minimally invasive surgery is still performed with hand-held laparoscopic instruments, and the surgeon's instrument kinematics are lost when the operation ends; only the endoscope video is kept. This paper presents an end-to-end pipeline that captures this motion in the operating room and uses it to train a surgical robot policy, validated on live animals. We introduce a surgical instrument-state logger that mounts on the shaft of a standard laparoscopic instrument and recovers its pose and...
  </details>

- **2026-09-22** — Md Mostafizer Rahman, Md Faizul Ibne Amin, Md Shahajada Mia et al. — [Compressing Long Context into Answer-Aligned Memory Embeddings for LLM Inference](http://arxiv.org/abs/2609.25537v1)
  <details><summary>📄 Abstract</summary>
  Large language model (LLM) inference is constrained by the quadratic scaling of self-attention and the linear scaling of the KV cache, increasing latency, energy consumption, and GPU memory demand as context length scales. Existing soft-compression methods either lack query-guided memory selection at inference time, train without answer-targeted supervision, or couple compression tightly to a specific decoder architecture. We propose a Context-to-Answer-Aligned Memory Compression (CMC) framework...
  </details>

- **2026-09-22** — Laizhen Li, Jiarui Li, Juanjuan Zhao et al. — [Grow the Harness, Not the Context: From Strategy-Free Scaffolds to Reusable Specialist Agents](http://arxiv.org/abs/2609.26760v1)
  <details><summary>📄 Abstract</summary>
  Large language model (LLM) agents often handle streams of related tasks, yet standard harnesses repeatedly ask the model to reconstruct the same control decisions inside each task's context. We study whether task feedback can instead turn recurring control into reusable executable code, while reserving LLM calls for task-specific semantic reasoning. We introduce Growing Harness, a failure-guided training paradigm that learns the agent harness itself from a strategy-free scaffold that exposes fix...
  </details>

- **2026-09-22** — Tushar Bag, Edgar Martínez-Moro, Daniel Panario — [Annihilator and twisted Euclidean duality for quasi-polycyclic codes](http://arxiv.org/abs/2609.26633v1)
  <details><summary>📄 Abstract</summary>
  Let $f\in\mathbb F_q[x]$ be a monic polynomial of degree $m$ with $f(0)\ne 0$, and let $\mathcal R=\mathbb F_q[x]/\langle f\rangle$. Under coefficient expansion, a quasi-polycyclic (QP) code of index $n$ corresponds to an $\mathcal R$-submodule of $\mathcal R^n$. In this paper, we study QP codes with respect to the annihilator duality. We show that this form is non-degenerate and that the annihilator dual of a QP code is again a QP code. We also give an equivalent description of the dual in term...
  </details>

- **2026-09-22** — William Schober, Scott Wesley — [A New Method For Manipulating Circuits, Application To Quantum Adders](http://arxiv.org/abs/2609.26591v1)
  <details><summary>📄 Abstract</summary>
  We use a new technique for manipulating controlled quantum circuits to convert between two distinct types of quantum adders, one based on the Quantum Fourier Transform and the other based on the Ripple-Carry technique from classical reversible logic. This conversion takes the form of an explicit gate-level transpilation. We also present a new quantum adder with a natural interpretation as a kind of Carry-Lookahead adder that uses no ancillas.
  </details>


## 📊 统计 / Statistics

| 分类 / Category | 论文数 / Count |
|------|--------|
| jailbreak | 638 |
| prompt-injection | 558 |
| memory-poisoning | 51 |
| tool-use-attack | 140 |
| backdoor | 473 |
| adversarial-attack | 602 |
| privacy-leakage | 4165 |
| steganography | 72 |
| misuse | 1052 |
| red-teaming | 127 |
| vulnerability | 3227 |
| defense | 3063 |
| alignment | 2830 |
| robustness | 3028 |
| watermark | 478 |
| unlearning | 97 |
| agent-safety | 55 |
| benchmark | 66 |
| survey | 361 |
| other | 8163 |

---

📚 **全部 29246 篇论文**（2022 至今）请访问 [GitHub Pages](https://ny1024.github.io/AgentSafety-Papers/) 查看完整列表、搜索与筛选。

*Generated by AgentGuard at 2026-09-26 15:34:53*