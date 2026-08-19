<div align="center">

# AgentGuard 🛡️

**Daily Tracking of LLM Agent Security Papers on arXiv**

[![Auto Update](https://github.com/NY1024/AgentSafety-Papers/actions/workflows/daily-update.yml/badge.svg)](https://github.com/NY1024/AgentSafety-Papers/actions/workflows/daily-update.yml)
[![Papers](https://img.shields.io/badge/Papers-24234-blue)](#)
[![License](https://img.shields.io/badge/License-MIT-green)](#)

</div>

---

## 📖 简介 / Introduction

自动追踪 arXiv 上大模型 Agent 安全方向的最新论文，每日更新，关键词智能分类。

*Automatically tracking the latest LLM Agent security papers on arXiv, updated daily with keyword-based classification.*

**最近更新 / Last Updated**: 2026-08-19 18:26 ｜ **论文总数 / Total Papers**: 24234（近 30 天 / Recent 30 days: 3366）

🌐 **[GitHub Pages](https://ny1024.github.io/AgentSafety-Papers/)** — 查看全部 24234 篇论文（含摘要、分类筛选、搜索）/ View all 24234 papers with abstracts, filters & search

## 📑 分类导航 / Category Navigation

- **[jailbreak](#-jailbreak)** — 越狱攻击 / Jailbreak Attacks — 587
- **[prompt-injection](#-prompt-injection)** — 提示注入攻击 / Prompt Injection Attacks — 495
- **[memory-poisoning](#-memory-poisoning)** — 记忆投毒与篡改 / Memory Poisoning & Tampering — 44
- **[tool-use-attack](#-tool-use-attack)** — 工具使用攻击 / Tool-Use Attacks — 120
- **[backdoor](#-backdoor)** — 后门与投毒攻击 / Backdoor & Poisoning Attacks — 418
- **[adversarial-attack](#-adversarial-attack)** — 对抗攻击 / Adversarial Attacks — 566
- **[privacy-leakage](#-privacy-leakage)** — 隐私泄露 / Privacy Leakage — 3858
- **[steganography](#-steganography)** — 隐写与隐蔽通信 / Steganography & Covert Communication — 55
- **[misuse](#-misuse)** — 滥用与误用 / Misuse & Abuse — 905
- **[red-teaming](#-red-teaming)** — 红队测试 / Red Teaming — 115
- **[vulnerability](#-vulnerability)** — 漏洞与攻击面 / Vulnerabilities & Attack Surfaces — 2737
- **[defense](#-defense)** — 防御与防护方法 / Defense & Protection Methods — 2461
- **[alignment](#-alignment)** — 对齐与安全约束 / Alignment & Safety Constraints — 2276
- **[robustness](#-robustness)** — 鲁棒性与可靠性 / Robustness & Reliability — 2283
- **[watermark](#-watermark)** — 水印与溯源 / Watermarking & Provenance — 303
- **[unlearning](#-unlearning)** — 机器遗忘 / Machine Unlearning — 90
- **[agent-safety](#-agent-safety)** — Agent 安全框架 / Agent Safety Frameworks — 52
- **[benchmark](#-benchmark)** — 安全评测与基准 / Safety Benchmarks & Evaluation — 59
- **[survey](#-survey)** — 综述与系统化 / Surveys & Systematization — 286
- **[other](#-other)** — 其他安全相关 / Other Security-Related — 6524

## 📄 近期论文 / Recent Papers (Last 30 Days)

> 仅展示最近 30 天中最新的 500 篇论文（含日期、作者、摘要）。近 30 天共 3366 篇，完整 24234 篇论文列表请访问 [GitHub Pages](https://ny1024.github.io/AgentSafety-Papers/)

> Showing the latest 500 of 3366 papers from the last 30 days (with date, authors & abstract). For the full list of 24234 papers, visit [GitHub Pages](https://ny1024.github.io/AgentSafety-Papers/)

### 📂 jailbreak
*越狱攻击 / Jailbreak Attacks* — 8 papers

- **2026-08-18** — Istiaque Ahmed, Afia Anjum Borsha, Ranat Das Prangon et al. — [Reflex-Guard: A Low-Latency Guardrail for LLM Prompt Safety Using Dense Semantic Embeddings](http://arxiv.org/abs/2608.17556v1)
  <details><summary>📄 Abstract</summary>
  Large Language Models (LLMs) in real-world applications often face the risks of specially crafted prompts designed to bypass the safety controls. Existing guardrail methods, such as LLM-as-a-judge and cloud-based safety APIs are able to detect unsafe content. However, they often add a delay of about 250-900 ms to each request. This delay is too high for real-time applications, when the system usually needs to respond in less than 100 ms. Furthermore, routing user prompts through external moderat...
  </details>

- **2026-08-18** — Zhida He, Xiaoyu Wen, Han Qi et al. — [Fair ASR: Re-Evaluating Black-Box Jailbreaks under Shared Target-Call Budgets](http://arxiv.org/abs/2608.17360v1)
  <details><summary>📄 Abstract</summary>
  Reliable jailbreak evaluation is essential for assessing LLM safety, but most existing studies rely solely on attack success rate (ASR) without accounting for its dependence on attack budgets, resulting in unfair comparisons across methods. Existing compute-aware evaluations reduce heterogeneous resources into FLOPs, which is difficult to estimate for black-box models and fails to capture resource-specific constraints. To provide a comparable evaluation basis, we introduce Fair-ASR, an evaluatio...
  </details>

- **2026-08-18** — Md Abdullahil Oaphy, Anhao Xiang, Zongxing Xie et al. — [COMIC: Reference-Aware Safety Gating for Multimodal Large Language Models](http://arxiv.org/abs/2608.17234v1)
  <details><summary>📄 Abstract</summary>
  Multimodal large language models (MLLMs) are increasingly used to interact with screenshots, scanned documents, diagrams, and other visually grounded inputs. This shift introduces a new safety risk: in many multimodal jailbreaks, neither the prompt nor the image is harmful in isolation. Unsafe behavior emerges only when the model binds an apparently benign operation, such as summarizing, translating, or following, to a localized visual target. This reveals a structural weakness in current multim...
  </details>

- **2026-08-17** — Mark Russinovich — [Fool's Gold: Defensive Deception Against Safety-Removal Attacks on Open-Weight Models](http://arxiv.org/abs/2608.17202v1)
  <details><summary>📄 Abstract</summary>
  Safety alignment in open-weight language models is trivially removable: abliteration projects a refusal-mediating direction out of the weights in minutes, and no release-time defense we are aware of prevents it durably. What cannot be prevented can be deceived. Our defense, decoy hardening ("Fool's Gold"), concedes the refusal strip and poisons its payoff: once refusal is stripped, most answers to hazardous operational requests are confident, fluent decoys whose critical elements are falsified. ...
  </details>

- **2026-08-17** — Jiawei Liu, Jiacheng Guo, Tian Zhang et al. — [Security of Foundation-Model-Powered Embodied Agents: Attack Surfaces, Attacks, Defenses, and Evaluation](http://arxiv.org/abs/2608.16843v1)
  <details><summary>📄 Abstract</summary>
  Foundation models are increasingly used for perception, reasoning, planning, and action generation in embodied agents, creating security risks that can propagate from digital inputs to physical behavior. Existing surveys often organize threats by mechanisms such as jailbreaks, prompt injection, backdoors, poisoning, or adversarial examples, but these categories do not consistently identify where an adversary first enters the embodied control loop. We present a trust-boundary-centric survey of fo...
  </details>

- **2026-08-17** — Xiaoyu Wen, Jiajia Li, Zhida He et al. — [JailbreakSkill: Scaling Automated Red-Teaming with Reusable and Ever-Evolving Skills](http://arxiv.org/abs/2608.16465v1)
  <details><summary>📄 Abstract</summary>
  Automated red-teaming has produced a growing collection of attack strategies, yet they typically remain scattered across prompts and workflows, making them difficult to systematically integrate, reuse, and improve at scale. We introduce \textsc{JailbreakSkill}, a skill-centric framework for scaling automated red-teaming through reusable and continuously evolving attack capabilities. \textsc{JailbreakSkill} packages existing attack strategies into modular, agent-ready skills that can be directly ...
  </details>

- **2026-08-16** — Md Messal Monem Miah, Adrita Anika, Zhiyuan Yu et al. — [TRACE: Trajectory Aware Reasoning for Multi-Turn Adversarial Conversation Evaluation](http://arxiv.org/abs/2608.15594v1)
  <details><summary>📄 Abstract</summary>
  Multi-turn jailbreak attacks have emerged as a critical safety threat to LLMs, as harmful objectives are decomposed across a sequence of apparently benign turns to bypass guardrails. Existing defenses lack the reasoning capacity to identify evolving manipulation patterns, often trading helpfulness for safety by over-refusing benign requests related to sensitive topics. We introduce Trace, a multi-turn defense with trajectory-aware structured reasoning. Before generating each response, the model ...
  </details>

- **2026-08-14** — Wei Zhao, Zhe Li, Peixin Zhang et al. — [Tripwire: Triggering Aligned Refusal via Statistically Certified Safety Neurons](http://arxiv.org/abs/2608.14392v1)
  <details><summary>📄 Abstract</summary>
  Neuron- and path-level interventions offer the finest-grained route to defending large language models (LLMs) against jailbreak attacks, yet existing methods fall short of this promise, i.e., they often compromise model utility significantly. Specifically, one line of work suppresses toxic neurons to erase harmful semantics, but since such semantics are distributed across the network, blocking every pathway forces a large intervention footprint. An alternative line of research focus on identify ...
  </details>


### 📂 prompt-injection
*提示注入攻击 / Prompt Injection Attacks* — 7 papers

- **2026-08-18** — Sujin Chen, Lijun Li, Tianyi Du et al. — [MobileWorldSafety: Benchmarking GUI Agent Safety Against Environmental Injection Attacks in Android Apps](http://arxiv.org/abs/2608.17659v1)
  <details><summary>📄 Abstract</summary>
  LLM-powered GUI agents that autonomously operate smartphones are rapidly transitioning from research prototypes to early real-world deployment. However, because these agents routinely process untrusted environmental content, they are highly vulnerable to environmental injection attacks, which include indirect prompt injections and adversarial instructions. Such attacks can manipulate the behavior of agents without user awareness through diverse channels encountered in everyday mobile use. Despit...
  </details>

- **2026-08-18** — Rabimba Karanjai, Yang Lu, Richard Williamson et al. — [PACE: Policy-Attested Contract Execution for Safe AI Agents in Decentralized Finance](http://arxiv.org/abs/2608.17220v1)
  <details><summary>📄 Abstract</summary>
  Autonomous AI agents are emerging as interfaces for decentralized finance (DeFi) actions such as swaps, lending operations, and yield management. Because these agents rely on large language models (LLMs) to plan transactions, they inherit the LLM's susceptibility to prompt injection and lack of mechanisms to bind a verifier's approval to the exact transaction ultimately submitted on-chain. We present PACE (Policy-Attested Contract Execution), a transaction-level authorization framework that inte...
  </details>

- **2026-08-17** — Zonghao Ying, Xiangfan Wu, Huiyu Wu et al. — [Security Assessment of DeepSeek Harness with A.I.G: Evaluating Resistance to Indirect Prompt Injection](http://arxiv.org/abs/2608.16393v2)
  <details><summary>📄 Abstract</summary>
  We assess indirect prompt injection in DeepSeek Harness (DSH), using AI-Infra-Guard (A.I.G) to construct tests, deliver controlled taint, execute DSH, collect traces, and judge outcomes. The study covers 14,560 controlled executions over 16 indirect-content channels, text and file carrier modes, 35 payload objectives, one unmodified baseline, and 12 attack methods. The experiment preserves DSH's agent loop, tool registry, model adapter, and session-event path; source tools and sensitive sinks ar...
  </details>

- **2026-08-17** — Zonghao Ying, Xiangfan Wu, Huiyu Wu et al. — [Security Assessment of DeepSeek Harness with A.I.G: Evaluating Resistance to Indirect Prompt Injection](http://arxiv.org/abs/2608.16393v1)
  <details><summary>📄 Abstract</summary>
  We assess indirect prompt injection in DeepSeek Harness (DSH), using AI-Infra-Guard (A.I.G) to construct tests, deliver controlled taint, execute DSH, collect traces, and judge outcomes. The study covers 14,560 controlled executions over 16 indirect-content channels, text and file carrier modes, 35 payload objectives, one unmodified baseline, and 12 attack methods. The experiment preserves DSH's agent loop, tool registry, model adapter, and session-event path; source tools and sensitive sinks ar...
  </details>

- **2026-08-17** — Jun He, Deying Yu — [Agent-Native Telemetry: Verifiable State-Delta Evidence for Autonomous Operations](http://arxiv.org/abs/2608.16178v1)
  <details><summary>📄 Abstract</summary>
  Operational telemetry is predominantly engineered for human reading: systems repeatedly serialize verbose prose, static keys, and redundant context across billions of log lines. As autonomous AI agents become primary operational consumers, feeding them traditional logs wastes scarce context capacity parsing lexical syntax rather than reasoning over system state changes -- all while lacking cryptographic guarantees of provenance or collection completeness.   This paper introduces agent-native tel...
  </details>

- **2026-08-16** — Xabier Muruaga — [Bounded Agents: Delegation Security for Multi-Agent AI Systems](http://arxiv.org/abs/2608.15888v1)
  <details><summary>📄 Abstract</summary>
  LLM-based agents can act on behalf of a user to access cloud services, call tools, or invoke agents. At session start, the agent's permissions are set but remain static, and each request is evaluated independently, without considering prior actions. Within its permissions, an agent may act contrary to the delegated task, combine individually permitted actions into a prohibited outcome, or delegate authority to a sub-agent without limiting it. A prompt injection poses a risk only if the agent has...
  </details>

- **2026-08-15** — Md Fazley Rafy — [TwinGridShield: Consequence-Aware Runtime Authorization for LLM Grid-Agent Actions](http://arxiv.org/abs/2608.15391v1)
  <details><summary>📄 Abstract</summary>
  Large language model (LLM)-assisted energy-management tools can translate natural-language context into structured grid commands, but syntactic validity does not imply physical admissibility. This paper presents TwinGridShield, a model-independent runtime authorization layer that evaluates each proposed action in a deterministic network twin before release. The prototype checks connectivity, branch-flow, generator, and load-shedding invariants and records each decision in a hash-chained log. A c...
  </details>


### 📂 tool-use-attack
*工具使用攻击 / Tool-Use Attacks* — 4 papers

- **2026-08-18** — Zhibo Zhang, Zhen Ouyang, Ling Shi et al. — [TRUSS: Towards Task-Reliable and User-Safe Automated Agent Skill Generation](http://arxiv.org/abs/2608.17588v1)
  <details><summary>📄 Abstract</summary>
  Agent Skills package reusable natural language procedures with executable resources, enabling software agents to acquire task specific capabilities without model adaptation. Automatically generating such Skills can improve task performance, yet evaluating a candidate solely from its artifact or final task outcome leaves unresolved which actions the equipped agent will perform and which side effects those actions will produce. We present TRUSS, an evidence guided framework for generating function...
  </details>

- **2026-08-17** — Yinuo Wang, Yiyu Shi — [SkillEffect: Checked Lowering for Memory-Bounded Agent Tools](http://arxiv.org/abs/2608.17007v1)
  <details><summary>📄 Abstract</summary>
  Agent Skills can specify procedural and resource obligations for tool use, and language models instantiate them as concrete programs. However, when models turn this guidance into code for existing tool interfaces, even a semantically correct program may load an entire input and exceed the memory available to one tool call. We present SkillEffect, a checked-lowering runtime for computations with a recoverable source relation, an audited bounded implementation, and a registered output postconditio...
  </details>

- **2026-08-17** — Mingxiao Liu, Zhoumian Jiang, Jianan Ma et al. — [CompoSkill: Compositional Skill Chain Attacks from Individually Scanner-Passing LLM Agent Skills](http://arxiv.org/abs/2608.16246v1)
  <details><summary>📄 Abstract</summary>
  Autonomous AI agents tackling Long Horizon Tasks depend on marketplace skills that are certified one at a time: a scanner returns a safety verdict for each skill and declares the ecosystem safe if every package passes. We show that this assumption fails under skill composition. A skill may pass the per-skill scanner individually yet participate in a risky composition when an agent connects its outputs, capabilities, or side effects with those of other scanner-passing skills. This makes skill com...
  </details>

- **2026-08-17** — Lihui Ding, Zihan Guo, Bingwei Lu et al. — [Skill2Query: Exploiting Skill Structure to Generate Pseudo-Queries for Agent Skill Retrieval](http://arxiv.org/abs/2608.16071v1)
  <details><summary>📄 Abstract</summary>
  Pseudo-query generation can alleviate the supervision bottleneck for agent skill retrieval, but existing document-level approaches typically leave the rich internal relations among capabilities, parameters, and usage examples implicit. As a result, generated queries may be topically relevant to a skill while lacking capability grounding and parameter consistency, raising the question of whether explicitly exploiting a skill document's internal structure can produce more effective retrieval signa...
  </details>


### 📂 backdoor
*后门与投毒攻击 / Backdoor & Poisoning Attacks* — 4 papers

- **2026-08-18** — Xukun Luan, Jinyan Liu, Yuhui Gong et al. — [MemCatalyst: Amplifying Data Auditing on Vision-Language Models via Data Poisoning](http://arxiv.org/abs/2608.17722v1)
  <details><summary>📄 Abstract</summary>
  Vision-Language models (VLMs) achieve outstanding performance largely due to the amount of training data available on the internet. At the same time, data holders (e.g., artists) urgently need to determine whether their data has been used for model training without authorization, which concerns both intellectual property rights and personal privacy. Data auditing, particularly through membership inference (MI), has attracted attention as a direct tool. This work proposes MemCatalyst, a set of da...
  </details>

- **2026-08-17** — Mehrdad Ghassabi — [Towards Safer RAG: Only Agents Capable of System 2 Thinking may Access Untrusted Documents](http://arxiv.org/abs/2608.17153v1)
  <details><summary>📄 Abstract</summary>
  Retrieval-Augmented Generation (RAG) has significantly enhanced the performance of large language models (LLMs), yet these systems remain vulnerable to knowledge-poisoning attacks, in which misinformation in retrieved documents can influence the model's final outputs. Notably, an LLM may correctly detect that a document contains incorrect information while nevertheless being influenced by it. Prior work has addressed this vulnerability through the Cordon Principle, which prevents models responsi...
  </details>

- **2026-08-16** — Nokimul Hasan Arif, Qian Lou, Mengxin Zheng — [Conjunctive Poisoning in AI Supply-Chain Applications](http://arxiv.org/abs/2608.15913v1)
  <details><summary>📄 Abstract</summary>
  Large Language and Vision-Language Models are increasingly deployed through inference pipelines that include prompt wrappers (e.g., templates and post-processing scripts) and configuration metadata (e.g., JSON/YAML files) that together shape model outputs. While model weights and binaries are routinely verified, these textual deployment artifacts remain weakly protected despite directly influencing runtime behavior. We show that a malicious developer can pair a benign-looking wrapper with crafte...
  </details>

- **2026-08-16** — Riku Mochizuki, Shusuke Komatsu, Souta Noguchi et al. — [Assessing Attack Surfaces in Generative Search Engines through Publisher Attributes: A Case Study in Political Domains](http://arxiv.org/abs/2608.15814v1)
  <details><summary>📄 Abstract</summary>
  We characterize the attack surface of generative search engines (GSEs) against poisoning attacks in the political domain, from the perspectives of citation selection and personalization. GSEs integrate web search and answer generation with user preferences and backgrounds using large language models (LLMs). They play a crucial role in how users access information on the web. Because anyone can publish content on the web, GSEs are vulnerable to poisoning attacks that manipulate citations to under...
  </details>


### 📂 adversarial-attack
*对抗攻击 / Adversarial Attacks* — 9 papers

- **2026-08-18** — Xiaoyong Yu, Rongzhen Li, Shuming Shi et al. — [MS-MFAD : Multimodal large language models for Face Anti-spoofing Detection](http://arxiv.org/abs/2608.17328v1)
  <details><summary>📄 Abstract</summary>
  Facial biometric recognition systems currently face compound threats intertwining generative AI and high-fidelity physical spoofing. Existing defenses suffer from systemic bottlenecks, including poor generalization, non-auditable reasoning, and reliance on massive, low-quality datasets. To address these challenges, we propose Multimodal Large Language Models (MFAD) for face anti-spoofing detection, an explainable reasoning system for Unified Face Anti-Spoofing Detection (UFAD), accompanied by a ...
  </details>

- **2026-08-18** — Yang Chen, Zhan Zhuang, Yanbin Wei et al. — [Learning What Not to Learn: Adversarial Disentangled Prompt Tuning for Robust Vision-Language Models](http://arxiv.org/abs/2608.17306v1)
  <details><summary>📄 Abstract</summary>
  While adversarial prompt tuning can enhance robustness of vision-language models efficiently, we find that existing methods aggravate robust generalization overfitting on seen classes, leading to a rapid degradation in performance against adversarial examples of unseen classes as training progresses. We empirically identify that this degradation stems from the tendency of the model to learn pseudo-robust features (i.e., non-generalizable shortcuts). To mitigate this, we propose ADAPT (Adversaria...
  </details>

- **2026-08-17** — Tong Zhang, Motasem Alfarra, Carlos Hinojosa et al. — [DiSCO: Defending text-to-image generation through distribution-guided contrastive prompt optimization](http://arxiv.org/abs/2608.17067v1)
  <details><summary>📄 Abstract</summary>
  As text-to-image generative models advance, they raise critical safety concerns, particularly the generation of Not-Safe-For-Work (NSFW) content such as violence and nudity, further exacerbated by red-teaming adversarial attacks. Existing defenses predominantly operate under white-box assumptions, relying on text encoder optimization, weight editing, or inference-time intervention, and fundamentally cannot scale to proprietary models. Black-box alternatives based on LLM prompt rewriting offer br...
  </details>

- **2026-08-17** — Yuting Wu, Dongfang Guo, Xiangzhong Luo et al. — [AdROD: HyperNetwork-based Adversarially Robust Object Detection for Autonomous Driving](http://arxiv.org/abs/2608.16031v1)
  <details><summary>📄 Abstract</summary>
  Camera-based object detectors are vulnerable to physical adversarial attacks designed to suppress detections. While adversarial training and input purification offer some protection, they often overfit to specific attack distributions and fail on adaptive adversaries. This paper presents AdROD, an embedded, stochastic ensemble defense software designed for autonomous driving. AdROD employs {\em low-rank HyperNetworks}, which require only 1.6\% of the parameter footprint of standard HyperNetworks...
  </details>

- **2026-08-16** — Nof Orenstein, Yoni Birman — [Breaking and Defending LLM-Powered Social Media Bot Detection Systems](http://arxiv.org/abs/2608.15893v1)
  <details><summary>📄 Abstract</summary>
  The rise of social media bots poses a persistent threat, enabling misinformation, opinion manipulation, and the erosion of trust in online platforms. To combat this, machine learning systems have been developed to detect and limit bot activity, but attackers continuously adapt through techniques such as adversarial learning and behavior imitation, fueling an ongoing arms race between bots and detection tools. Recent advances in large language models (LLMs) have significantly improved bot detecti...
  </details>

- **2026-08-15** — Alireza Dehghanpour Farashah, Zhuan Shi, Negar Rostamzadeh et al. — [TEA: Text Encoder Alignment for Robust Concept Erasure in Text-to-Image Models](http://arxiv.org/abs/2608.15341v1)
  <details><summary>📄 Abstract</summary>
  Text-to-image diffusion models can be misused to generate harmful content through adversarial or paraphrased prompts that bypass built-in safety mechanisms. Existing concept erasure methods often suffer from limited robustness against adversarial prompts, degradation of benign generation quality, or reliance on inference-time interventions that introduce persistent computational overhead. To address these limitations, we formulate concept erasure as a domain alignment problem in the text represe...
  </details>

- **2026-08-15** — Weikang Yu, Yonghao Xu, Pedram Ghamisi — [On the Adversarial Robustness of Remote Sensing Semantic Change Detection](http://arxiv.org/abs/2608.15267v1)
  <details><summary>📄 Abstract</summary>
  Semantic change detection (SCD) is a bitemporal dense-prediction task that jointly identifies changed regions and their semantic states before and after change. Unlike single-image segmentation or binary change detection, SCD couples two temporal inputs with timestamp-wise semantic prediction, change localization, and final semantic-change decoding, creating adversarial dependencies that are not captured by conventional robustness protocols. We present a task-specific evaluation framework that s...
  </details>

- **2026-08-15** — Kaisheng Liang, Yiming Cao, Bin Xiao — [Perspective-Invariant Attack with Enhanced Transferability of Adversarial Examples](http://arxiv.org/abs/2608.15115v1)
  <details><summary>📄 Abstract</summary>
  Adversarial examples generated on a surrogate deep neural network (DNN) can often successfully fool other black-box DNN models. This cross-model transferability poses serious security threats to DNNs in practical applications. Input transformation techniques are widely used to enhance adversarial transferability by increasing the diversity of input images. However, existing methods primarily rely on local operations with limited degrees of freedom (DOF), such as block-wise shuffling and resizing...
  </details>

- **2026-08-14** — Dipankar Sarkar — [A Four-Axis Trustworthiness Benchmark for LLM-as-Judge in Principle-Based Regulation](http://arxiv.org/abs/2608.14329v1)
  <details><summary>📄 Abstract</summary>
  Principle-based regulation, with evaluative standards such as "fair, clear, and not misleading" or "deliver good outcomes", cannot be reduced to binary predicates, and LLM-as-judge is increasingly used as the substitute. Our position is that any such judge must be evaluated on four axes: accuracy, paraphrase robustness, adversarial robustness, and calibration. We release Principle-Bench, 168 cryptoasset financial-promotion scenarios mapped to two UK FCA principles, with paraphrase, adversarial k...
  </details>


### 📂 privacy-leakage
*隐私泄露 / Privacy Leakage* — 27 papers

- **2026-08-18** — Maosen Zhang, Jianshuo Dong, Boting Lu et al. — [The Model's Tell: Measuring Context-Leakage Attack Signals with Behavior Gauges](http://arxiv.org/abs/2608.17829v1)
  <details><summary>📄 Abstract</summary>
  LLMs increasingly rely on external contexts, such as pre-defined system prompts or retrieved documents, to improve generation quality. However, processing these contexts alongside user queries creates an attack surface: adversarial inputs can induce models to disclose them. Prior probing studies suggest that leakage-related signals emerge in hidden states, yet the need to extract these states poses additional deployment challenges. In this paper, we explore whether this internal signal leaves a ...
  </details>

- **2026-08-18** — Sarvesh Gharat, Junpei Komiyama — [SGHA: Evidence-Grounded Research Problem Discovery with Local Language Models](http://arxiv.org/abs/2608.17501v1)
  <details><summary>📄 Abstract</summary>
  Recent efforts toward fully automated AI scientists have demonstrated that language-model agents can generate hypotheses, execute experiments, and draft scientific manuscripts. However, during the early stages of research, when research problems are formulated, these AI scientists often rely heavily on proprietary frontier models. Their proposals are shaped by opaque parametric knowledge and by literature searches conditioned on the proposals themselves. Such knowledge is effectively a black box...
  </details>

- **2026-08-18** — Rubén Balbastre, Juan Manuel Orduña, Mariano Pérez — [An Empirical Study of Reward Specification and Benchmark Reliability in GRPO-based LLM Unlearning](http://arxiv.org/abs/2608.17804v1)
  <details><summary>📄 Abstract</summary>
  Practical LLM unlearning is usually evaluated through two objectives: suppress target-specific knowledge and preserve non-target utility. In generative QA, this leaves a third behavior underspecified: when a target-adjacent prompt admits a broader answer without target-specific leakage, the model should answer at that level rather than leak, evade, or refuse. We study this specification problem in a controlled LoRA-GRPO RWKU setting, comparing four reward designs that span lexical suppression, a...
  </details>

- **2026-08-18** — Xiangyi Li, Jiajia Guo, Chao-Kai Wen et al. — [Learnware for CSI Feedback: Scene-specific Small Models Can Do Big](http://arxiv.org/abs/2608.17760v1)
  <details><summary>📄 Abstract</summary>
  Intelligent channel state information (CSI) feedback is essential for realizing the high capacity and spectral efficiency goals of future 6G systems, yet existing deep learning solutions face a trade-off between model generalization and scenario-specific performance. Large neural networks generalize well but incur high computational and tuning costs, while small models excel in particular environments but require repetitive costly end-to-end training for each base station (BS). To address these ...
  </details>

- **2026-08-18** — Yufan Zhu, Chao Jin, Khin Mi Mi Aung et al. — [FESC: Remodeling Long-Context Private Inference with Encrypted State-Space Models](http://arxiv.org/abs/2608.17442v1)
  <details><summary>📄 Abstract</summary>
  Processing long, sensitive documents with machine-learning models requires efficient, privacy-preserving long-context inference. Prior private inference systems optimize or distribute encrypted Transformer attention, but its quadratic token-pair work remains the bottleneck as sequence length grows. Selective state-space models (SSMs) offer linear-time recurrence, yet direct encrypted implementation incurs linear multiplicative depth, sequence-wide state residency, or dense FHE-MPC conversion. We...
  </details>

- **2026-08-18** — Sabari Shanmugam, Nick Barnes, Kerry Taylor — [Spectral Gradient Orthogonalization Improves Differentially Private Training at Scale](http://arxiv.org/abs/2608.17415v1)
  <details><summary>📄 Abstract</summary>
  Differentially private training adds isotropic Gaussian noise to clipped gradients, corrupting every singular direction equally. In vision models, where spatial correlation concentrates gradient energy into a low-rank subspace, most of this noise falls in directions that carry little signal. Spectral gradient orthogonalization via polar decomposition is introduced as a post-processing step that recovers directional signal from the noisy gradient's low-rank structure at zero additional privacy co...
  </details>

- **2026-08-18** — Weiran Wang, Hongxiang Shi, Huitao Tang et al. — [ArguLens: An Open-Source System for Automated Essay Scoring and Label-Aware Feedback Generation](http://arxiv.org/abs/2608.17356v1)
  <details><summary>📄 Abstract</summary>
  Most automated essay scoring (AES) systems output a single holistic score without interpretable evidence and rely on closed APIs that introduce data privacy and cost barriers. We present ArguLens, an opensource, locally deployable system that decomposes AES into three decoupled components: a discourse-move classifier (Qwen2.5-7B-Instruct fine-tuned with LoRA on PERSUADE 2.0), a grade-independent LightGBM scorer over 31 linguistic and discourse features, and a label-aware feedback generator serve...
  </details>

- **2026-08-18** — Chenhao Xue, Raslen Guesmi, Siwei Feng et al. — [Temporal Leakage in Financial News NLP: A Multi-Architecture Audit with a Regime-Specific M&A Signal](http://arxiv.org/abs/2608.17223v1)
  <details><summary>📄 Abstract</summary>
  Financial-news direction prediction has become a popular NLP benchmark, yet reported gains depend critically on whether the train-test split is chronological or random, i.e., on temporal leakage. We audit this dependence on a 49,799-article corpus across 16 feature-model combinations spanning TF-IDF, MiniLM, FinBERT, and fine-tuned RoBERTa-large / DeBERTa-v3-large, plus separate zero/few-shot and LoRA probes of Llama-3 and Qwen2.5 LLMs: random splits inflate MCC by $1.1\times$ to $6.5\times$, tr...
  </details>

- **2026-08-17** — Sibo Liu — [Authorization Before Context: A Model-Neutral Audience Boundary Against Cross-Audience Memory Leakage in Agentic Systems](http://arxiv.org/abs/2608.17148v1)
  <details><summary>📄 Abstract</summary>
  A personal language agent learns a fact from one audience and may later place it in the prompt it assembles for another. This memory-to-context step is an attack surface: ambiguous or inconsistent channels, cross-audience prying, and poisoned memory can each cause the system to assemble context containing a fact relevant to the query yet unauthorized for the current viewers. We introduce authorization before context: a single, anti-monotone audience-membership rule applied at the memory-to-conte...
  </details>

- **2026-08-17** — Nyamtulla Shaik, Fengjun Li, Bo Luo — [Benchmarking the Benchmarks: Evaluating Automated Safety Benchmarks for Small Language Models](http://arxiv.org/abs/2608.17183v1)
  <details><summary>📄 Abstract</summary>
  Small Language Models (SLMs) are increasingly deployed in resource-constrained, privacy-sensitive settings, where safety and bias failures can cause security and societal risks. However, existing AI safety\slash security\slash compliance benchmarks are designed for large language models that may not transfer reliably to SLMs. We therefore ask: Can these benchmarks effectively and reliably evaluate SLMs? To answer this question, we conduct a large-scale assessment of the effectiveness and robustn...
  </details>

- **2026-08-17** — Zhixiang wang, Ziliang Hong, Ulas Bagci — [A decodability criterion predicts when hidden-state selection beats majority voting in large language models](http://arxiv.org/abs/2608.17124v1)
  <details><summary>📄 Abstract</summary>
  Combining the answers a large language model (LLM) samples for a question into one decision is a test-time information fusion problem, usually solved by majority voting. Voting is unreliable on difficult questions, where the sampled answers share correlated errors, so the wrong answer can win and drawing more samples makes the decision worse. Selecting a candidate by reading a correctness signal from the model's hidden states is a promising alternative, but its accuracy varies across models and ...
  </details>

- **2026-08-17** — Zheng Tang, Shuo Wang, David C. Anastasiu et al. — [The 10th AI City Challenge](http://arxiv.org/abs/2608.17044v1)
  <details><summary>📄 Abstract</summary>
  The 10th AI City Challenge, held with ECCV 2026, marks a decade of community benchmarking for intelligent transportation, smart cities, and physical AI. Since its 2017 start with vehicle detection, classification, and tracking, the challenge has grown into a broad benchmark suite for multi-camera perception, multimodal reasoning, synthetic-to-real learning, generative forecasting, and privacy-preserving evaluation. The 2026 edition continued this growth with 325 registered teams, up from 245 in ...
  </details>

- **2026-08-17** — Lehao Wang, Zhiwen Yu, Sicong Liu et al. — [AdaSprite: Resource-efficient Online Co-Adaptation for V2I Systems Under Large-scale Data Drifts](http://arxiv.org/abs/2608.16188v1)
  <details><summary>📄 Abstract</summary>
  The rise of vehicle-infrastructure (V2I) collaboration enables safer and broader perception. To process large-scale V2I video streams, vision-language models (VLMs) are promising as they unify multi-view vision into end-to-end task grounding, reducing handcrafted design. We use Vision Mixture-of-Experts (V-MoE) as the distributed visual backbone of VLMs, leveraging sparse expert routing to enable conditional computation across diverse viewpoints under resource constraints. Yet, V-MoEs face a cri...
  </details>

- **2026-08-17** — Yu Li, Liqi Zhuang, Dong Wei et al. — [SkillWatermark: An Embedded Skill Watermark of Progressive Privacy Inference via Benign Prompts](http://arxiv.org/abs/2608.16026v1)
  <details><summary>📄 Abstract</summary>
  Skills for large language model (LLM) agents have been widely deployed across diverse application domains. However, we observe that these skills generate specific traffic patterns during execution. In this paper, we design a pipeline that generates specific traffic patterns by inserting carefully designed skill descriptions, which we term skill watermarks, so that a passive network attacker can establish a covert channel to encode private information within observable traffic across multiple con...
  </details>

- **2026-08-17** — Shaolong Chen, Yanlin Fei, Nazhou Liu et al. — [Reconstruction: A Blind Benchmark for Recovering Research Ideas from Pre-Publication Bibliographies](http://arxiv.org/abs/2608.16645v1)
  <details><summary>📄 Abstract</summary>
  Can a language model recover the true research idea of a published paper when given only that paper's pre-publication bibliography? We introduce Reconstruction, a blind idea-recovery benchmark that withholds the seed paper and all contemporaneous or future literature, and asks models to propose hypotheses that an independent large language model judge matches against the held-out ground-truth idea. A strict anti-leakage protocol-temporal citation cutoff, anonymous reference IDs, and frozen per-p...
  </details>

- **2026-08-17** — Wenjie Wang, Wenhe Si, Xinyue Xu et al. — [What to Remember, What to Reveal: Privacy-Aware Memory for Conversational Agents](http://arxiv.org/abs/2608.16551v1)
  <details><summary>📄 Abstract</summary>
  Long-term memory enables personalized conversational agents to retain user information across sessions. However, existing memory architectures primarily optimize for utility while neglecting the risks of unnecessarily storing and reusing private attributes such as personally identifiable information (PII). Addressing privacy risks in personalized memory is challenging because simply removing sensitive values can undermine system utility. Therefore, privacy protection for memory agents should gov...
  </details>

- **2026-08-17** — Yizhao Wang, Xinfa Wang, Jingbo Wang et al. — [Beyond Similarity Matching: Structured Reasoning for Open-Vocabulary Referring Segmentation in 3DGS](http://arxiv.org/abs/2608.16103v1)
  <details><summary>📄 Abstract</summary>
  Open-vocabulary referring segmentation in 3D Gaussian Splatting (3DGS) requires a neural model to select Gaussian primitives according to free-form language expressions. Existing 3DGS-based methods usually rely on global text-region similarity, which is weak for queries involving attributes, reference objects, spatial relations, and fine-grained parts. This often causes target-reference confusion, granularity mismatch, part-whole leakage, and relation violations. We propose QAGaussian, a query-a...
  </details>

- **2026-08-17** — Victor Ye Dong, Reid Pryzant, Yi Liu et al. — [CAPO: Constraint-Aware Prompt Optimization for LLM Agents](http://arxiv.org/abs/2608.16068v1)
  <details><summary>📄 Abstract</summary>
  Large language models (LLMs) are increasingly deployed as agents that rely on system prompts to use tools and complete tasks. Such deployments impose distinct operational requirements, including appropriate tool use, concise prompts and solution paths, and compliance with safety and formatting policies. For many practitioners, however, assembling domain-specific supervised data to post-train models to meet these requirements is infeasible. We introduce CAPO (Constraint-Aware Prompt Optimization)...
  </details>

- **2026-08-17** — Haixu Liu, Lei Zhou, Yuhao Ren et al. — [GoalEvolve: From Handcrafted Algorithm Priors to Goal-Driven Evolution of Physical Design Algorithms](http://arxiv.org/abs/2608.16733v1)
  <details><summary>📄 Abstract</summary>
  Physical design algorithms operate within tightly coupled, multi-stage optimization flows, where stage-local gains may vanish or induce downstream degradation. Existing program-evolution frameworks often rely on stage-local objectives or undifferentiated multi-metric feedback, which neither guarantee better final results nor identify which unmet requirement should guide the next iteration. We present GoalEvolve, a goal-driven framework that makes physical design algorithm evolution accountable f...
  </details>

- **2026-08-17** — Sourya Joyee De, Abdessamad Imine — [A Human-LLM Teaming Framework for Privacy Risk Analysis: An Illustration with CBDC-Based Welfare Schemes](http://arxiv.org/abs/2608.16461v1)
  <details><summary>📄 Abstract</summary>
  Central Bank Digital Currency (CBDC)-based welfare schemes may be potentially privacy invasive as they process significant volumes of beneficiary personal data and lead to privacy harms such as surveillance, discrimination and stigmatization. Such welfare delivery schemes involve complex digital ecosystems and large number of stakeholders. Consequently, to examine their privacy risks, privacy risk assessments require extensive information gathering and synthesis, complex reasoning, scenario expl...
  </details>

- **2026-08-17** — Sofoklis Kitharidis, Cor J. Veenman, Jan N. van Rijn et al. — [Evolving Executable Pipeline Programs for AutoML with Language Models](http://arxiv.org/abs/2608.16416v1)
  <details><summary>📄 Abstract</summary>
  Automated machine learning (AutoML) systems search for pipelines within a space of preprocessing operators, learners, and hyper-parameters specified in advance: they can select and tune known components, but cannot produce structure outside that space. We present LACE, an AutoML framework that instead searches over complete executable pipeline programs: an evolutionary loop maintains a population of scikit-learn-compatible Python classes, and a large language model acts as the variation operator...
  </details>

- **2026-08-16** — Chong Chen, Yulu Zhang, Qingxi Guo et al. — [A Responsible Artificial Intelligence Framework for Groundwater Modeling](http://arxiv.org/abs/2608.15657v1)
  <details><summary>📄 Abstract</summary>
  The rapid development and widespread application of artificial intelligence (AI) have sparked intense discussions on how to deploy responsible AI systems in a manner aligned with human values and ethical standards. Compared to fields like healthcare, energy, or finance, the application of AI in groundwater is relatively limited, and research on responsible AI is even more scarce. Taking the middle reaches of the Heihe River Basin as the study area, this paper proposes six Responsible AI principl...
  </details>

- **2026-08-16** — Pengyu Wang, Baochen Xiong, Xiaoshan Yang et al. — [UniFed-VLM: Federated Instruction Tuning for Vision-Language Models with Multiple Heterogeneity](http://arxiv.org/abs/2608.15516v1)
  <details><summary>📄 Abstract</summary>
  Vision-Language Models (VLMs) have demonstrated strong performance in multimodal understanding and generation. However, fine-tuning of VLMs typically relies on centralized data, which raises privacy concerns in certain domains (e.g. healthcare). Federated Learning (FL) provides a natural solution by enabling model training without sharing raw data. However, applying FL to VLM instruction tuning is highly challenging. VLMs have substantial parameter scales, and in real-world scenarios, clients ex...
  </details>

- **2026-08-15** — Lovre Antonio Budimir, Mingya Alexa Gong, Alyssa Foong Quinney et al. — [Beyond Natural-Image Foundation Models: Benchmarking Satellite Pretraining for Ophthalmic Image Analysis](http://arxiv.org/abs/2608.15195v1)
  <details><summary>📄 Abstract</summary>
  Vision Foundation Models (VFMs) have emerged as a promising approach in medical imaging, producing broadly applicable systems that can be efficiently adapted across diverse imaging modalities, anatomical regions, and clinical tasks. However, VFMs require extensive training data, and their progress in medical image analysis is constrained by limited data availability, privacy concerns, and high development costs. To alleviate these constraints, medical VFMs (MedVFMs) are often built upon weights ...
  </details>

- **2026-08-15** — Seongyoon Kim — [Global Federated Learning Strategies for Building Efficient Personalized Models](http://arxiv.org/abs/2608.15107v1)
  <details><summary>📄 Abstract</summary>
  Federated learning (FL) is a practical framework that can train models on distributed user data while guaranteeing data privacy; however, due to heterogeneity in which each user has a different data distribution, problems frequently arise where both global and personalization performance deteriorate simultaneously. This dissertation presents methodologies for building efficient personalized models by identifying which strategies are effective in the global training stage and by showing how to pr...
  </details>

- **2026-08-15** — Ankita Sharma, Bahar Farahani, Sanaz Rahimi Moosavi et al. — [MoE Router-Guided Clustering for Heterogeneous Federated Instruction Tuning](http://arxiv.org/abs/2608.15311v1)
  <details><summary>📄 Abstract</summary>
  Federated instruction fine-tuning enables Large Language Models (LLMs) to adapt to decentralized, privacy-sensitive data without requiring data sharing. Recent Mixture-of-Experts (MoE) LLMs are particularly attractive for federated learning because their sparse activation reduces computation and communication while scaling model capacity. However, existing federated MoE methods primarily focus on parameter aggregation and personalization, overlooking the routing behavior of MoE models as a sourc...
  </details>

- **2026-08-14** — Zhenyuan Li, Yi Jiang, Junjie Cheng et al. — [MazeRunner: Nonlinear Task and Clue Orchestration for LLM-driven Black-Box Automated Penetration Testing](http://arxiv.org/abs/2608.14216v1)
  <details><summary>📄 Abstract</summary>
  Penetration testing is essential yet resource-intensive. Although large language models (LLMs) show promise for automating security auditing, existing agents mainly execute end-to-end workflows in simplified linear scenarios. Real-world black-box testing is fundamentally nonlinear: the attack graph is initially unknown and must be incrementally inferred from environmental feedback. Observations may reveal multiple attack branches, failures are often ambiguous, and critical clues may span long ac...
  </details>


### 📂 misuse
*滥用与误用 / Misuse & Abuse* — 15 papers

- **2026-08-18** — Bowen Sun, Zhengyue Zhao, Xiaogeng Liu et al. — [Decomposition Attacks Across Unlinkable Identities: Limits of Stateful Defenses for LLM Services](http://arxiv.org/abs/2608.17445v1)
  <details><summary>📄 Abstract</summary>
  Most large language model services use stateless defenses, which judge only the current request, to refuse harmful tasks. Decomposition attacks exploit this limitation by splitting a harmful task into individually permissible requests and combining their answers. Defending against them therefore requires a stateful monitor that considers requests together. If it can group all requests for one attacker task, it can stop the attack. However, attackers can use unlinkable identities and combine answ...
  </details>

- **2026-08-18** — Hamidreza Saffari, Francesco Pierri — [Auditing Exposure to Harmful Content on TikTok using Multimodal Language Models: A Cross-National, Age-Stratified Study](http://arxiv.org/abs/2608.17583v1)
  <details><summary>📄 Abstract</summary>
  Online video platforms can expose young users to harmful content, but independent audits remain difficult because video annotation is costly and moderation judgments vary across languages. We audit TikTok in France, Italy, and Sweden with sockpuppet accounts representing four age personas (13, 16, 19, 40), collecting 36,971 videos from passive For-You-page scrolling and active sessions that scroll, search for harm keywords, and scroll again. To scale annotation, we validate four multimodal LLMs ...
  </details>

- **2026-08-18** — Zhen Zhang, Ahmad Hafez, Amr Alanwar — [Cross-View Correspondence Is a Measurement Intervention: Two-Sided Validation for Agent Evaluation and Credit Assignment](http://arxiv.org/abs/2608.17713v1)
  <details><summary>📄 Abstract</summary>
  Agent evaluations and trace-based learning often compare outputs across transformed views through a post-response correspondence treated as neutral preprocessing. We show that this correspondence is a measurement intervention: omitting it can manufacture sensitivity, an over-aggressive map can manufacture invariance, and multiple optimal correspondences can leave mechanism labels and signed learning credit unidentified. We develop a validity theory and audit with three components: two-sided vali...
  </details>

- **2026-08-18** — Cesar Borja, Breck A. McCollum, Jarret E. Byrnes et al. — [Leveraging existing sparse point annotations for benthic imagery dense segmentation](http://arxiv.org/abs/2608.17561v1)
  <details><summary>📄 Abstract</summary>
  The health of marine ecosystems is a critical indicator of global environmental change, yet the physical constraints of underwater observation and the intrinsic challenges of processing marine imagery severely limit the scalability of systematic monitoring. While recent visual foundation models such as the Segment Anything Model (SAM) series show great promise, they still struggle with the fine-grained recognition required in these complex scenarios and still require expert supervision. Our work...
  </details>

- **2026-08-17** — Hidayet Aksu — [Measuring Obedience to Authority Across Large Language Models with the Milgram Paradigm](http://arxiv.org/abs/2608.16177v2)
  <details><summary>📄 Abstract</summary>
  Large language models (LLMs) are increasingly deployed as agents that operate equipment, execute instructions, and act inside institutional hierarchies, raising a question social psychology answered for humans six decades ago: how far will an agent escalate a harmful action when a legitimate authority insists? We port Milgram's obedience paradigm to LLMs as a standardized, fully scripted, replicable probe: the model plays the Teacher, a deterministic harness plays Experimenter and Learner from p...
  </details>

- **2026-08-17** — Yujia Li, Yiqun Zhang, Zihan Cheng et al. — [HarmTrace: Anchor-Calibrated Decoupled Optimization for Fine-Grained Target Identification in Harmful Memes](http://arxiv.org/abs/2608.16622v1)
  <details><summary>📄 Abstract</summary>
  Multimodal harmful meme detection is typically formulated as image--text harmfulness classification. A model may correctly predict harmfulness while misidentifying the attacked target or its supporting evidence. We therefore extend harmful meme detection with fine-grained target identification, asking what type of target is attacked, who is targeted, and where the target appears in the meme. The model predicts harmfulness for every meme and, for harmful memes, outputs the target category, target...
  </details>

- **2026-08-17** — Emma V. Stein, Dominik Meier, Terry Ruas et al. — [BabelSteering: Multilingual Safety Alignment via English Steering Vectors](http://arxiv.org/abs/2608.16577v1)
  <details><summary>📄 Abstract</summary>
  Large language models (LLMs) are deployed globally in high-stakes settings, yet most safety research and alignment efforts remain concentrated on English. Thus, users interacting with LLMs in other languages may encounter weaker safeguards despite relying on the same systems for similarly sensitive tasks. In this work, we investigate whether safety signals learned from a high-resource language, like English, can improve multilingual safety. We propose BabelSteering, an activation steering method...
  </details>

- **2026-08-17** — Hidayet Aksu — [Measuring Obedience to Authority Across Large Language Models with the Milgram Paradigm](http://arxiv.org/abs/2608.16177v1)
  <details><summary>📄 Abstract</summary>
  Large language models (LLMs) are increasingly deployed as agents that operate equipment, execute instructions, and act inside institutional hierarchies, raising a question social psychology answered for humans six decades ago: how far will an agent escalate a harmful action when a legitimate authority insists? We port Milgram's obedience paradigm to LLMs as a standardized, fully scripted, replicable probe: the model plays the Teacher, a deterministic harness plays Experimenter and Learner from p...
  </details>

- **2026-08-17** — Anand Murugan — [Does the LM Head Create a Harmful Gradient Bottleneck? A Causal Test](http://arxiv.org/abs/2608.16671v1)
  <details><summary>📄 Abstract</summary>
  The language-model head maps a hidden state of width D to a vocabulary of size V, so its transpose can return at most D independent directions to the Transformer. Godey and Artzi argue that this severe projection is a harmful optimization bottleneck. We separate the geometry from the causal claim. Our backward-only intervention keeps the ordinary logits and the exact LM-head parameter update while reducing only the rank of the gradient sent into the Transformer. Across five paired seeds on byte-...
  </details>

- **2026-08-17** — Parsa Mazaheri, Kasra Mazaheri — [Prior Audit-Repair Context Shifts LLM Verifier Thresholds Toward Leniency](http://arxiv.org/abs/2608.16003v1)
  <details><summary>📄 Abstract</summary>
  Automated checking pipelines increasingly place one language model as the checker and another (or the same one) as the fixer. We ask whether that wiring changes what the checker reports. Measuring false alarms on human-verified-correct ProcessBench traces with the present task held byte-identical, we find that a completed audit -> repair episode already in the model's context lowers false alarms in 15 of 15 model x wording combinations, by 2.8 to 11.5 percentage points against a length-matched n...
  </details>

- **2026-08-17** — Yuanzhi Xu, Qian Gao, Jun Fan et al. — [Diagnosing Dense Same-Class Attribute Misbinding in Large Vision-Language Models](http://arxiv.org/abs/2608.16805v1)
  <details><summary>📄 Abstract</summary>
  Large vision-language models can recognize the objects and attributes in a crowded scene yet assign an attribute to the wrong same-class instance. Generic visual-question-answering accuracy marks the response as wrong, while object-hallucination metrics may regard both the object and attribute as image-supported; neither reveals the transfer. This study formalizes this blind spot as Dense Same-Class Attribute Misbinding (DSCAM) and presents InstaBind-Lite, a controlled benchmark that makes it di...
  </details>

- **2026-08-16** — Jiaming He, Zhicong Huang, Tian Jin et al. — [ARENA: Automated Red-Teaming for Large Audio Language Models](http://arxiv.org/abs/2608.15578v1)
  <details><summary>📄 Abstract</summary>
  Large audio-language models (LALMs) make it possible to interact with language models through speech, music, and environmental sound, but they also introduce a safety surface that is difficult to expose with text-only red-teaming. We study automated audio-grounded red-teaming, where a text query must remain safe in isolation while the joint text-audio input induces harmful target behavior. We propose ARENA, a closed-loop framework that trains a controller on an independent 2,000case text-audio d...
  </details>

- **2026-08-16** — Satchit Chatterji, Shihan Wang, Giovanni Sileno et al. — [PL-Guard: Probabilistic Logic Reasoning for LLM Guardrails](http://arxiv.org/abs/2608.15673v1)
  <details><summary>📄 Abstract</summary>
  Large language model guardrails can be viewed as policy-consistency problems: a system must determine which policy-relevant facts hold in a prompt-response pair and what those facts imply under a given policy. Common approaches, including policy prompting and LLM-as-a-judge pipelines, often overlap the tasks of semantic grounding and policy reasoning: the model both interprets the prompt-response pair and reasons about whether a policy has been violated. This can lead to unsafe compliance with h...
  </details>

- **2026-08-16** — Mingyu Yuan, Shengtao Wen, Lingbing Guo et al. — [VARM-Bench: Benchmarking Verifiable Structured Reasoning in Chinese Abusive Speech Moderation](http://arxiv.org/abs/2608.15600v1)
  <details><summary>📄 Abstract</summary>
  The widespread circulation of abusive online content has increased the need for reliable moderation of Chinese social-media text. Existing Chinese benchmarks support label classification, fine-grained toxicity categorization, and target-aware extraction, but do not provide a unified representation for deterministically verifying the stated basis of a moderation decision. We introduce VARM-Bench, a benchmark for field-anchored chain-of-thought rationales in Chinese abusive-speech moderation. Each...
  </details>

- **2026-08-14** — Parameswaran Kamalaruban, Viktor Drobnyi, Maeve Madigan et al. — [MINT: A Universal Zero-Shot Predictor for Transaction Data](http://arxiv.org/abs/2608.14198v1)
  <details><summary>📄 Abstract</summary>
  Banks analyse sequential financial transaction data to perform many tasks, including fraud prevention, credit risk assessment and offer personalization. To improve the predictive accuracy of these tasks, Payments Foundation Models encode transaction sequence data as rich contextual embeddings, which can then be provided to task-specific models as features. However, these Foundation Models are not designed for flexible zero-shot reasoning across novel downstream prediction tasks, limiting their a...
  </details>


### 📂 vulnerability
*漏洞与攻击面 / Vulnerabilities & Attack Surfaces* — 60 papers

- **2026-08-18** — Javier Aguilar Martín — [An Omitted Mode Is a Rare Rule: The Sampling-Verification Danger Law in Continuous Code World Models](http://arxiv.org/abs/2608.17956v1)
  <details><summary>📄 Abstract</summary>
  In the Code World Model paradigm an LLM synthesizes an executable world model that a classical planner searches, and the model is accepted when it reproduces sampled transitions. We ask what that acceptance certifies in continuous control. We define the pipeline's danger as an expected risk and isolate its exact factor: the probability that N i.i.d. gate rollouts all miss a critical event of probability r is exactly (1-r)^N; an independent acceptance sample adds its budget to the exponent. On th...
  </details>

- **2026-08-18** — Lei Jiang, Ye Wei, Xinyu Xi et al. — [EvoTS-Agent: A Self-Evolving LLM Agent for Financial Time Series Change Point Detection](http://arxiv.org/abs/2608.17933v1)
  <details><summary>📄 Abstract</summary>
  Financial time series exhibit non-stationary and heterogeneous statistical properties, making change-point detection challenging because no single unsupervised algorithm performs consistently across assets and market regimes. Conventional workflows consequently depend heavily on expert-driven model selection, feature design, and hyperparameter tuning, limiting their scalability and adaptability. We propose EvoTS-Agent, a validation-guided self-evolving LLM agent for autonomous financial time-ser...
  </details>

- **2026-08-18** — Zachary Kenton, Lili Janzer, Rory Greig et al. — [Debate Training Reduces Reward Hacking in RLAIF](http://arxiv.org/abs/2608.17776v1)
  <details><summary>📄 Abstract</summary>
  We demonstrate that RL finetuning an LLM using debate, a two-player adversarial game between a generator and a critic adjudicated by a weaker LLM judge, reduces reward hacking compared to a reinforcement learning from AI feedback (RLAIF) baseline. Reward hacking is a central obstacle in RLAIF: as training progresses, the policy learns to exploit systematic errors in its AI judge, degrading task performance, a problem that worsens precisely when the judge is weaker than the policy, the setting mo...
  </details>

- **2026-08-18** — Yizhu Zhao, Li Yu, Jianhua Zhang et al. — [Electromagnetic World Model for 6G: A Unified Framework for Joint Environment Reconstruction and Channel Prediction](http://arxiv.org/abs/2608.17769v1)
  <details><summary>📄 Abstract</summary>
  The integration of sensing, communication, and intelligence is becoming a key enabler for sixth generation (6G) wireless systems, where intelligent terminals are expected to simultaneously support efficient link establishment and reliable environmental sensing. However, existing studies mainly exploit sensing information or communication information to address a single task, such as channel prediction or environment reconstruction. Motivated by the shared dependence of optical and radio-frequenc...
  </details>

- **2026-08-18** — Janine Schneider, Jan Kallenborn, Tim Hoffmann et al. — [Achievement Unlocked: Let's Get Hacked! An Empirical Study of Cybercrime in the Video Gaming Ecosystem](http://arxiv.org/abs/2608.17754v1)
  <details><summary>📄 Abstract</summary>
  The ubiquity of the video game industry and its large user base have transformed video games into complex social and economic ecosystems. Unfortunately, this growing popularity also attracts cybercriminals who deliberately exploit game-specific mechanisms to target players. Despite this growing threat, cybercrime in the gaming ecosystem has received little systematic attention in prior research.   In this work, we present an empirical study of cybercrime affecting video game players, combining q...
  </details>

- **2026-08-18** — Raghutheja Bollampally, Soumya Sankar, Yuqi Qin et al. — [Active learning molecular beam epitaxy of complex quantum materials](http://arxiv.org/abs/2608.17742v1)
  <details><summary>📄 Abstract</summary>
  The integration of machine learning (ML) into materials science offers a transformative pathway toward fully autonomous synthesis workflows. For precise thin-film deposition techniques like molecular beam epitaxy (MBE), this automation is critical to overcome the time-consuming, manual navigation of high-dimensional thermodynamic phase spaces. Existing approaches for ML-assisted thin film growth predominantly rely on continuous Bayesian optimization (BO) models that assume smooth parameter lands...
  </details>

- **2026-08-18** — Zachary R. Madin, Connor York, Jonathan Lawry et al. — [Collective Ranking of Environmental Signals through Gaussian Belief Propagation in a Patrolling Robot Swarm](http://arxiv.org/abs/2608.17690v1)
  <details><summary>📄 Abstract</summary>
  Multi-robot patrolling requires a team to visit all areas of an environment at regular intervals, typically minimising idleness. A practical extension, motivated by security and environmental monitoring, is to additionally form a collective ranking of all patrol locations by some measured signal, a generalisation of the best-of-n problem to the many-option, continuous-valued regime. We observe that the patrol graph admits a natural dual interpretation: it is simultaneously the topology that dict...
  </details>

- **2026-08-18** — Joao Fonseca, Rodrigo Rodrigues, Paolo Romano — [Mixture-of-Expert Blocks Contain Strong Hallucination Detection Signals](http://arxiv.org/abs/2608.17687v1)
  <details><summary>📄 Abstract</summary>
  Despite their widespread use, Large Language Models (LLMs) remain limited by a fundamental problem: the generation of plausible but false content, known as hallucinations. Most existing detection methods operate at the answer or sentence level, yet per-token detection is essential for localizing hallucinated spans and enabling fine-grained interventions. In this paper, we explore the use of the Mixture-of-Experts (MoE) paradigm to address this gap. In MoE architectures, a single forward pass act...
  </details>

- **2026-08-18** — Chin-Hung Chen, Wim van Houtum, Yan Wu et al. — [Statistical Characterization and Block-EM Estimation of Frequency-Domain NSI for OFDM Systems in Bursty Impulsive Noise](http://arxiv.org/abs/2608.17683v1)
  <details><summary>📄 Abstract</summary>
  Impulsive noise (IN), characterized by its high power and non-Gaussian distribution, poses a critical challenge in modern orthogonal frequency-division multiplexing (OFDM) systems, driven by the proliferation of electronic devices. Current IN mitigation techniques rely heavily on time-domain processing. These methods apply before the discrete Fourier transform (DFT), introducing additional complexity, failing to align with OFDM's inherent frequency-domain processing flow, and risking the destruc...
  </details>

- **2026-08-18** — Luke C. Ugwuoke, Farooq Kyeyune, Tjaart P. J. Krüger — [Body-of-Revolution Finite-Element Model of Plasmon-Enhanced Fluorescence](http://arxiv.org/abs/2608.17655v1)
  <details><summary>📄 Abstract</summary>
  Plasmon-enhanced fluorescence (PEF) is one of the most widely investigated optical phenomena in hybrid systems of emitters and plasmonic nanoantennas, with applications ranging from biosensing to single-molecule emission microscopy. In this work, we extend finite-element modelling of PEF beyond spherically symmetric geometries using a body-of-revolution finite-element method (BOR-FEM). By exploiting exact or equivalent rotational symmetry, 3D emitter-nanoantenna systems are reduced to computatio...
  </details>

- **2026-08-18** — Prashant Rawat, Ravi Kumar Bairagi,  Arunima et al. — [An Emulation Anchored Digital Twin Testbed for Cyberattack and Defense Analysis in Hospital IT OT Environments](http://arxiv.org/abs/2608.17650v1)
  <details><summary>📄 Abstract</summary>
  Modern hospitals increasingly rely on integrated Information Technology (IT) and Operational Technology (OT) infrastructures to support critical healthcare services. However, this convergence expands the cybersecurity attack surface and makes safe validation of defensive mechanisms difficult on live systems. Existing testbeds often focus on isolated IT or OT environments and do not capture realistic cross-domain healthcare interactions. This work presents a hospital IT and OT cybersecurity testb...
  </details>

- **2026-08-18** — Bowen Liu, Qixiang Zhang, Xiaomeng Li — [PathoArgus: Advancing Evidence-Grounded Long-Context Visual Reasoning across Gigapixel Whole-Slide and Multi-Slide Case Contexts](http://arxiv.org/abs/2608.17607v1)
  <details><summary>📄 Abstract</summary>
  Whole-slide pathology reasoning requires models to integrate gigapixel-scale visual evidence across complete case-linked slides, yet current question-answering benchmarks primarily measure final answer accuracy--a metric vulnerable to linguistic priors and benchmark regularities, and insufficient to establish that predictions are grounded in the supplied tissue. We introduce PathoArgus-Bench, a benchmark and evaluation protocol that explicitly tests the full evidence chain: availability, accessi...
  </details>

- **2026-08-18** — Yajing Bai, Jinhao Duan, Jie Peng et al. — [HarnessRisk: A Lifecycle-Oriented Benchmark for Agent Harness Safety](http://arxiv.org/abs/2608.17597v1)
  <details><summary>📄 Abstract</summary>
  Large language models are increasingly deployed through agent harnesses that manage tools, extensions, persistent state, permissions, and external actions. Existing safety benchmarks mainly target individual attack mechanisms or a limited subset of operational settings, making it difficult to compare how safety failures emerge across different harness responsibilities. We present HarnessRisk, a lifecycle oriented benchmark that organizes agent harness safety into six operational phases including...
  </details>

- **2026-08-18** — Enrique Barba Roque, Luís Cruz, Annibale Panichella — [Beyond FLOPs: Energy-Aware Knowledge Distillation for Sustainable LLMs on Code-Related Task](http://arxiv.org/abs/2608.17515v1)
  <details><summary>📄 Abstract</summary>
  Background: Large Language Models (LLMs) are increasingly being applied to Software Engineering (SE) tasks, achieving high accuracy across problems such as clone detection, vulnerability prediction, and code summarization. However, their high computational demands and energy consumption raise sustainability concerns and hinder their use on consumer hardware and resource-constrained platforms. A common way to report the computational cost of an LLM in the literature and industry is to use the num...
  </details>

- **2026-08-18** — Kanglei Zhou, Ruizhi Cai, Hubert P. H. Shum et al. — [NeuroPath: Brain-Inspired Dual-Pathway Graph Convolutional Networks for Skeleton-Based Action Recognition](http://arxiv.org/abs/2608.17487v1)
  <details><summary>📄 Abstract</summary>
  Skeleton-based action recognition aims to recognize human actions from sequences of human joint coordinates. Most existing Spatial-Temporal Graph Convolutional Networks (STGCNs) have achieved promising results by modeling skeletal structures with implicit spatial-temporal representations. However, our empirical study reveals a clear performance imbalance across different skeletal modalities, indicating that implicitly coupling spatial and temporal information limits the full exploitation of comp...
  </details>

- **2026-08-18** — Songwei Wu, Rui Zhao, Fan Yang et al. — [EATR-Stereo: Embodiment-Aware Routing of Paired Stereo Evidence for Humanoid Vision-Language-Action Control](http://arxiv.org/abs/2608.17453v1)
  <details><summary>📄 Abstract</summary>
  Long-horizon humanoid vision--language--action (VLA) control with head-mounted stereo cameras requires visual interfaces that can exploit complementary views while maintaining compatibility with pretrained representations. Existing interfaces often discard complementary stereo evidence or fuse additional observations without preserving the native primary-view pathway and adapting auxiliary information to robot embodiment. We present EATR-Stereo, an embodiment-aware token-routing framework that r...
  </details>

- **2026-08-18** — Genghan Zhang, Yixin Dong, Chengze Fan et al. — [PTXBench: Benchmark and Adapt LLMs for GPU Kernel Optimization with Architecture-specific PTX](http://arxiv.org/abs/2608.17379v1)
  <details><summary>📄 Abstract</summary>
  We introduce PTXBench, a benchmark for evaluating and adapting large language models (LLMs) to use architecture-specific PTX for GPU kernel optimization. PTXBench measures functional correctness, whether selected target instructions execute at runtime, and speedup over frontier libraries across GEMM and attention workloads on H100 and B200 GPUs. Our evaluation shows that architecture-specific PTX capability remains uneven: success rates fall substantially on complex attention backward workloads,...
  </details>

- **2026-08-18** — Jie Deng, Zhigang Li, J. H. Zheng et al. — [Integrated Heat and Power System Scheduling with Continuous-Time Thermal Dynamics via Bernstein-Galerkin Optimization](http://arxiv.org/abs/2608.17287v1)
  <details><summary>📄 Abstract</summary>
  Coordinated scheduling of district heating networks (DHNs) and electric power systems can improve operational flexibility and reduce costs by exploiting thermal inertia. Most existing formulations rely on simplified discrete-time DHN models, which may inadequately represent continuous spatiotemporal thermal dynamics and can lead to biased flexibility estimation and suboptimal schedules. In this paper, an integrated heat and power system scheduling framework that explicitly incorporates the conti...
  </details>

- **2026-08-18** — Berkcan Kapusuzoglu, Shunsaku Matsumoto, Yoshitomo Miyagi et al. — [Adaptive surrogate modeling for high-dimensional spatio-temporal output](http://arxiv.org/abs/2608.17250v1)
  <details><summary>📄 Abstract</summary>
  This paper develops an adaptive surrogate modeling method for problems with very high-dimensional spatio-temporal outputs. The analysis of spatio-temporal multi-physics systems is computationally expensive and consists of a large number of inputs and outputs. Surrogate models are often constructed to replace the physics-based model to achieve computational efficiency in analyses such as uncertainty quantification and optimization that require many function calls. In order to address the challeng...
  </details>

- **2026-08-17** — Maria Katarine Santana Barbosa, Kelvin Lopes Dias — [An O-RAN-Assisted MARL Approach for Dynamic Sidelink and Infrastructure Selection in V2X Communications](http://arxiv.org/abs/2608.17210v1)
  <details><summary>📄 Abstract</summary>
  Future applications in the 6G-based Internet of Vehicles will leverage sidelink (SL) transmissions in Vehicle-to-Everything (V2X) scenarios. However, SL-based direct communication can significantly increase interference among vehicles and between vehicles and other entities of the Intelligent Transportation System. Thus, both Vehicle-to-Vehicle communications and Vulnerable Road Users (VRUs) uplink resources may be degraded or subject to starvation. Existing solutions primarily focus on improvin...
  </details>

- **2026-08-17** — Liner Xiang, Yixin Wang, Hengrui Cai — [Policy Optimization and Statistical Inference for Online Contextual Matrix Games](http://arxiv.org/abs/2608.17173v1)
  <details><summary>📄 Abstract</summary>
  Online decision making often requires navigating a landscape shaped by both dynamic contexts and strategic interactions. In competitive pricing, for example, hotels must account for both dynamic contextual factors and rivals' strategic responses. Existing approaches address only part of this challenge: contextual bandits optimize single-agent decisions using observable features but ignore multi-player interactions, while online matrix games capture strategic behavior through Nash equilibrium but...
  </details>

- **2026-08-17** — Paul Minchella, Stéphane Chrétien, Guillaume Metzler et al. — [MultiSigBERT: Beyond Survival Analysis through Multimodal and Sequential Modeling in Oncology](http://arxiv.org/abs/2608.16972v1)
  <details><summary>📄 Abstract</summary>
  Machine learning has become an essential component of modern healthcare, where the integration of heterogeneous data sources offers unprecedented opportunities to improve clinical decision-making. Electronic Health Records (EHR) contain complementary information -- including narrative clinical reports, numerical measurements, and structured variables -- yet most survival models remain limited to a single modality or fail to exploit the temporal nature of patient trajectories. We propose MultiSig...
  </details>

- **2026-08-17** — Alizishaan Khatri — [Probing the Prefill: Detecting Code Vulnerabilities via Latent Activations](http://arxiv.org/abs/2608.16970v1)
  <details><summary>📄 Abstract</summary>
  LLM-based code generation is now embedded in mission-critical pipelines, but defenses against vulnerable output remain post-hoc -- static analyzers, fine-tuned classifiers, or an LLM judge that screen completed code, ignoring the generating model's own internal state. We test a narrower, directly measurable question: when an LLM reads a piece of C/C++ code as context, do its hidden activations already carry a signal about that code's vulnerability status? We extract last prefill token activation...
  </details>

- **2026-08-17** — David Eric Austin, Kaheer Suleman, Jackie Chi Kit Cheung — [Semantic Bandits: In-Context Exploration-Exploitation is Biased by Semantic Priors](http://arxiv.org/abs/2608.16707v1)
  <details><summary>📄 Abstract</summary>
  Large language models (LLMs) are increasingly deployed as decision-making agents in settings that require sophisticated environmental exploration. However, existing work has raised questions about how LLMs actually balance exploration and exploitation. Unlike classical agents, LLM agents engage with tasks through natural language, exposing them to semantic information with no formal counterpart in the task structure. We introduce the semantic bandit, an extension of the multi-armed bandit settin...
  </details>

- **2026-08-17** — Yifan Zhang, Rahmatollah Beheshti — [Toward Better Assessment of LLMs' Performance in Clinical Error Detection](http://arxiv.org/abs/2608.16643v1)
  <details><summary>📄 Abstract</summary>
  Automated detection of errors in clinical documentation is a promising application of large language models (LLMs), yet decisions to deploy such models rest on benchmarks that evaluate each clinical note in isolation. Error-detection benchmarks are typically constructed by injecting errors into notes, such that each erroneous note has a natural counterpart. Aggregate discriminative metrics (e.g., balanced accuracy or F1) do not exploit this structure. We show that this omission is consequential....
  </details>

- **2026-08-17** — Jianming Chen, Xuanbin Ye, Yawen Wang et al. — [VCE-Skill: Enhancing Skill Self-Evolution with Version-Change Experience](http://arxiv.org/abs/2608.16544v1)
  <details><summary>📄 Abstract</summary>
  Agents increasingly rely on reusable skills to encode task knowledge, tool-use procedures, and validation rules. Existing skill self-evolution methods primarily revise skills using execution trajectories collected from current tasks, leaving the evolution knowledge accumulated in public skill version histories largely untapped. Our pilot study reveals a clear complementarity between the two sources: public skill changes provide reusable evolution priors, whereas trajectories provide evidence gro...
  </details>

- **2026-08-17** — Yu-Han Huang, Yujia Wu, Vincent S. Tseng — [TRACE-CASH: Trial-History-Conditioned Reinforcement Learning for Adaptive Configuration Exploration in Time-Series CASH](http://arxiv.org/abs/2608.16410v1)
  <details><summary>📄 Abstract</summary>
  Combined algorithm selection and hyperparameter optimization (CASH) searches a conditional space in which the selected model determines which hyperparameters are active. In time-series forecasting, temporal choices, chronological validation, and costly evaluations further complicate this search. Controlled comparisons of heterogeneous search methods under a shared time-series CASH (TS-CASH) evaluation protocol remain limited. Within this setting, we study TRACECASH, a task-local hybrid sequentia...
  </details>

- **2026-08-17** — Chathura Jayawardena, Konstantinos Nikitopoulos — [Aggressive Non-Orthogonal Transmission with DFT-s-OFDM for Direct Device-to-Satellite Communications](http://arxiv.org/abs/2608.16361v1)
  <details><summary>📄 Abstract</summary>
  Direct Device-to-Satellite (D2S) communications promise global connectivity to unmodified user equipment (UE), extending coverage beyond terrestrial networks. Realizing this promise is fundamentally challenging: severe path loss and limited UE transmit power push uplink SNRs far below terrestrial norms, while suitable spectrum remains scarce. Together, these constraints impose a spectral-efficiency (SE) bottleneck, and under such conditions the efficiency of the UE power amplifier becomes critic...
  </details>

- **2026-08-17** — Lyuye Zhang, Chengwei Liu, Fangyuan Zhang et al. — [Implicit, Yet Impactful: Understanding Hidden Dependencies in Java Projects](http://arxiv.org/abs/2608.16262v1)
  <details><summary>📄 Abstract</summary>
  As software usage continues to expand, package managers automatically resolve dependencies to construct a dependency graph based on user-specified requirements. These explicitly declared dependencies, known as direct dependencies, receive significant attention in terms of maintainability and security. However, implicit dependencies, which are not explicitly defined by users but are still directly utilized or referenced in their project code due to oversight, remain largely unnoticed. Unlike ordi...
  </details>

- **2026-08-17** — Xinlong Dai, Jinchuan Zhang, Lei Gao et al. — [STAIR: Semantic-Temporal Automaton for Interpretable Reasoning in Temporal Question Answering](http://arxiv.org/abs/2608.16224v1)
  <details><summary>📄 Abstract</summary>
  By leveraging large-scale pretraining, LLMs can interpret diverse temporal expressions and question formulations without task-specific training. However, existing prompt-based neuro-symbolic systems continue to rely on LLMs for both semantic interpretation and exact temporal inference. Consequently, discrete decisions regarding intervals, time anchors, and ordered states remain vulnerable to probabilistic errors and difficult to verify. We present STAIR, a \textbf{S}emantic-\textbf{T}emporal \te...
  </details>

- **2026-08-17** — Mikhail Surikov — [Securing AI-Generated Code: A Just-in-Time Vulnerability Detection and Remediation Pipeline](http://arxiv.org/abs/2608.16187v1)
  <details><summary>📄 Abstract</summary>
  AI-assisted development tools generate vulnerable code at significant rates, yet few automated mechanisms exist to detect, enrich, fix, and verify security issues at development velocity, particularly ones that ground remediation in real-world threat context. This paper presents an automated security evaluation pipeline that generates Python code from LLMSecEval prompts, scans for vulnerabilities using CodeQL and Bandit in parallel with an independent Code Validator LLM, enriches the Code Valida...
  </details>

- **2026-08-17** — Jinhao Yi, Weijun Gao, Chong Han — [L-COIN: LLM-Assisted Counterfactual Inference for Game-Theoretic Distributed Computation Offloading in Sub-THz LEO Satellite Networks](http://arxiv.org/abs/2608.16174v1)
  <details><summary>📄 Abstract</summary>
  As Space-Based Information Networks (SBINs) evolve toward high-capacity, intelligence-centric paradigms, integrating sub-Terahertz (sub-THz) communication into Low Earth Orbit (LEO) satellite constellations has emerged as a critical enabler for ultra-broadband and resilient global connectivity. By exploiting the ultra-wide bandwidth of sub-THz links to reduce transmission delays, resource-constrained ground devices can seamlessly offload compute-intensive tasks to LEO edge servers. However, sate...
  </details>

- **2026-08-17** — Xiaochuan Ma, Ning Zhu, Jia Fu et al. — [SUGFW+: An Uncertainty-guided Feature Weighting Framework for Cold Start Active Adaptation of SAM in Medical Image Segmentation](http://arxiv.org/abs/2608.16110v1)
  <details><summary>📄 Abstract</summary>
  Cold Start Active Learning (CSAL) is important in improving the performance of a medical image segmentation model with low annotation budget by querying a small subset for annotation from an unlabeled training set. Existing CSAL methods typically rely on inefficient dataset-specific Self-Supervised Learning (SSL) to map the unlabeled images into a feature space for sample selection. Recently, the advent of foundation models such as the Segment Anything Model (SAM) offer a promising alternative a...
  </details>

- **2026-08-17** — Tatsuhito Yamagata, Hanna Sumita — [Witness-Certified Fair Division with Comparison Queries](http://arxiv.org/abs/2608.16109v1)
  <details><summary>📄 Abstract</summary>
  We study fair division of indivisible goods when agents' valuations are accessed only through ordinal comparisons between bundles, with arbitrary tie-breaking. In this model, even deciding whether a given allocation is envy-free up to one good (EF1) can be impossible. This suggests explicit fairness certificates as a natural algorithmic object. Our main contribution is a certificate-preserving scaling framework, which recursively contracts goods, solves a smaller instance, and expands the soluti...
  </details>

- **2026-08-17** — Huitong Cheng, Yabo Dong, Jun Fan et al. — [Assessing Parameter Redundancy in Transformers for Jet Tagging](http://arxiv.org/abs/2608.16061v1)
  <details><summary>📄 Abstract</summary>
  Transformer-based jet taggers, such as the Particle Transformer (ParT) and the More-Interaction Particle Transformer (MIParT), achieve excellent discrimination by exploiting correlations among jet constituents, but often require more trainable parameters than earlier deep-learning taggers. In this paper, we investigate whether comparable discriminating power can be achieved with substantially fewer parameters. We introduce an hourglass structure that replaces the feed-forward networks (FFNs) in ...
  </details>

- **2026-08-17** — Jiawei Liu, Jiacheng Guo, Tian Zhang et al. — [When State Becomes an Attack Surface: State-Semantic Injection in LLM-Driven Embodied Agents](http://arxiv.org/abs/2608.16806v1)
  <details><summary>📄 Abstract</summary>
  Large Language Models (LLMs) have demonstrated capabilities in in-context learning, task decomposition, step-by-step reasoning, and code generation, driving their gradual evolution from text generation models into the core of agents capable of perceiving environments, invoking tools, and executing tasks. Traditional LLM Agents typically obtain information through webpages, documents, databases, or external tools and generate corresponding invocation sequences according to user goals; when this t...
  </details>

- **2026-08-16** — Yishun Wang, Wenjin Yi, Wenkai Li et al. — [RAGas: Retrieval-Augmented Gas Optimization for Smart Contracts with Continuous Knowledge Integration](http://arxiv.org/abs/2608.15857v1)
  <details><summary>📄 Abstract</summary>
  Ethereum is now integral to mission-critical sectors, including finance, healthcare, and supply chain management. Execution fees, commonly referred to as Gas, scale with the computational complexity of their functions. Smart contracts on Ethereum incur execution fees, known as Gas, which increase with computational complexity. Thus, optimizing Gas-intensive code while preserving functional equivalence significantly lowers deployment costs. No existing system continuously exploits evolving Gas us...
  </details>

- **2026-08-16** — Bo Zhao, Zheng Wu, Yiping Xie et al. — [CardiacMamba: Fair and Robust RGB-RF Fusion for Remote Heart Rate Estimation via State Space Modeling](http://arxiv.org/abs/2608.15831v1)
  <details><summary>📄 Abstract</summary>
  Remote photoplethysmography (rPPG) enables non-contact heart rate (HR) monitoring from facial videos, but RGB-only methods are vulnerable to illumination changes, motion artifacts, and skin-tone-dependent optical reflectance. We propose CardiacMamba, a fair and robust RGB-RF fusion framework that integrates optical facial cues and radio-frequency cardiac motion cues through state space modeling. CardiacMamba introduces a Temporal Difference Mamba Module (TDMM) to enhance subtle RF temporal varia...
  </details>

- **2026-08-16** — Weinan Liu, Zeyuan Ding, Dian Ding et al. — [Global Simulation-Guided Dynamic Operator Scheduling for Efficient Multi-Tenant Model Serving](http://arxiv.org/abs/2608.15762v1)
  <details><summary>📄 Abstract</summary>
  Container-granularity scheduling leaves abundant short-lived idle slices within containers unexploited. Reallocating containers is too heavyweight to utilize such fine-grained opportunities under SLA constraints, and operator-level scheduling requires reasoning about dependencies, memory safety, and cluster-wide execution dynamics in real time.   In this paper, we present SliceScheduler, a dynamic operator-level scheduling system for multi-tenant model serving. The key idea is to expose cluster-...
  </details>

- **2026-08-16** — Shuaishuai Cao, Meng Tang, Shuwei Peng et al. — [Hierarchical Adaptive Feature Refinement Network for VHR Remote Sensing Image Segmentation](http://arxiv.org/abs/2608.15647v1)
  <details><summary>📄 Abstract</summary>
  Semantic segmentation of very-high-resolution (VHR) remote sensing imagery increasingly benefits from strong pretrained hierarchical encoders, yet exploiting their multi-stage representations remains difficult. Nearby regions demand different balances between fine detail and semantic context, aggressive task-specific transformations perturb useful pretrained features, and conventional semantic supervision provides limited structural guidance. We present HAFR-Net, a progressive refinement framewo...
  </details>

- **2026-08-16** — Yudong Gao, Linghan Chen, Wenhan Wu et al. — [Bit-Flip Attacks on Vision-Language-Action Models: Action-Decoding Architecture Shapes the Vulnerability](http://arxiv.org/abs/2608.15475v1)
  <details><summary>📄 Abstract</summary>
  Quantized Vision-Language-Action (VLA) models expose a weight-fault surface: Rowhammer-style faults can corrupt deployed INT8 bits. We present the first bit-flip attack on a VLA: a few gradient-selected flips reduce closed-loop success to $0\%$, while hundreds of random flips are harmless. Across four model variants spanning three action-head families, damaging bits concentrate in a few action-generating layers, but the empirical budget depends sharply on the head: direct regression and token po...
  </details>

- **2026-08-16** — Arman Zarei, Mahdi M. Kalayeh — [Spatially-Grounded Flow Matching: Structured Source Distributions for Image Generation](http://arxiv.org/abs/2608.15452v1)
  <details><summary>📄 Abstract</summary>
  Current flow matching models learn to transport the source i.i.d. Gaussian noise into the target distribution of natural images, yet this source distribution carries no notion of spatial structure. Images however are fundamentally local since nearby pixels are strongly correlated. By sampling the noise independently, we hypothesize that models are implicitly encouraged to exploit less noisy neighbors as context during training, partially bypassing the need to properly learn the true local struct...
  </details>

- **2026-08-15** — Suyash Maniyar, Armaan Sandhu, Abhishek Mishra — [Measuring Reward Hacking and Reasoning-Answer Decoupling Under Position-Confounded Optimization](http://arxiv.org/abs/2608.15445v1)
  <details><summary>📄 Abstract</summary>
  When a reward is correct on every training example yet consistent with more than one goal, a model can acquire an unintended one, a failure known as goal misgeneralization. Endpoint accuracy on the training distribution cannot tell the two apart, because solving the task and exploiting a surface feature can satisfy the reward equally well. We treat this as a measurement problem: what does a benchmark score measure once a model has been optimized against a correct but confounded signal? We train ...
  </details>

- **2026-08-15** — Volodymyr Ovcharov — [Gated Against One Model, Open to the Next: Option-Only Solvability in Legal Multiple-Choice Benchmarks](http://arxiv.org/abs/2608.15428v1)
  <details><summary>📄 Abstract</summary>
  Multiple-choice benchmarks are graded on whether a model picks the right option, not on whether it needed the question. Measuring that gap takes care: a model answering A to most items scores above chance wherever the key sits at A, and reads as recognition when it is not. We measure it on UA-JudgeExam: 11,990 four-option items with official keys, published by Ukraine's Higher Qualification Commission of Judges.   Shown the options and no question, Claude Haiku 4.5 scores 0.383 against chance, a...
  </details>

- **2026-08-15** — Rohit Swami, Tushar Singh, Akash Warde et al. — [Chameleon: An Adaptive AI-Driven Honeypot Architecture Using Threat-Calibrated Particle Swarm Optimization and Semantic Deception Rapidly-Exploring Random Trees](http://arxiv.org/abs/2608.15407v1)
  <details><summary>📄 Abstract</summary>
  An invariant behavioral profile is the defining vulnerability of traditional honeypot installations: a skilled adversary can confirm the presence of a deception environment within only a few diagnostic commands, limiting its intelligence value. High-cost commercial deception products (USD 100,000--150,000 per year) share a related weakness in that their response engines are not coupled to real-time model-driven feedback. Chameleon is an openly distributed adaptive honeypot platform introduced he...
  </details>

- **2026-08-15** — Phillip Jiang — [UC-PSRO: Utility-Conditioned Policy-Space Response Oracles with a Communication-Dropout Curriculum for Game-Theoretic Course-of-Action Generation in Adversarial Swarms](http://arxiv.org/abs/2608.15372v1)
  <details><summary>📄 Abstract</summary>
  We study generating game-theoretically optimized Courses of Action (COAs) for a Blue UAS swarm against an adaptive Red adversary in a communication-degraded environment, motivated by (but not derived from) a public U.S. Air Force SBIR solicitation. We propose UC-PSRO (Utility-Conditioned Policy-Space Response Oracles with a Communication-Dropout Curriculum), combining three mechanisms: (i) PSRO self-play, so Blue and Red policies train as approximate best responses to each other rather than one ...
  </details>

- **2026-08-15** — Bo Wen, Yuhao Chen, Erhan Bilal et al. — [Divergent-Convergent Reasoning: Scaling Test-Time Compute through Structured Solution Synthesis](http://arxiv.org/abs/2608.15303v1)
  <details><summary>📄 Abstract</summary>
  Test-time compute can substantially improve Large Language Model (LLM) reasoning performance, yet how and when additional compute helps remains poorly understood. We study Divergent-Convergent Reasoning (DCR), a simple two-phase primitive consisting of an exploration phase that generates multiple candidate solutions followed by a convergent reconciliation phase. We present three core results. First, we show that even a single reconciliation step can reliably amplify correct minority reports: acr...
  </details>

- **2026-08-15** — Wei Zhang, Yihang Wu, Songhua Li et al. — [VGGT-Align: Bridging Local Reconstruction and Global Consistency for Long-Sequence 3D Reconstruction](http://arxiv.org/abs/2608.15260v1)
  <details><summary>📄 Abstract</summary>
  Maintaining global geometric consistency is a central challenge in long-sequence 3D reconstruction, with scale drift being the most critical failure mode. In chunk-based inference pipelines, the scale degree of freedom in sequential Sim(3) alignment is left unconstrained, causing estimation errors to compound multiplicatively and distort global trajectories and point cloud geometry. We present a scale-consistency enhancement framework built on a key insight: in structured environments such as dr...
  </details>

- **2026-08-15** — Puyu Zeng, Qibing Ren — [Beyond Direct Access: Resource Hijacking in LLM Agents](http://arxiv.org/abs/2608.15108v1)
  <details><summary>📄 Abstract</summary>
  Large language model agents are increasingly connected to high-value resources such as computing infrastructure, credentials, usage budgets, identities, private knowledge, communication channels, and organizational workflows. Existing agent security research mainly studies attacks on instructions, data, and tool behaviors, while high-value resources accessible to agents have received much less attention as direct attack targets. We are the first to identify and systematically study agent resourc...
  </details>

- **2026-08-15** — Zhiyu Zhang, Tingyue Wen, Senke Sun et al. — [WeSCE: A Benchmark for Measuring Security Drift in LLM-Driven Code Editing](http://arxiv.org/abs/2608.15092v1)
  <details><summary>📄 Abstract</summary>
  In this work, we introduce WeSCE, a benchmark for quantifying security drift in code editing under weak-security constraints, where tasks specify only functional objectives without explicit security requirements. WeSCE consists of 400 executable programs derived from real-world code, covering feature addition, feature removal, bug fixing, and refactoring. To quantify security drift, we propose a continuous risk representation that aggregates heterogeneous vulnerability signals through a unified ...
  </details>

- **2026-08-14** — Ruizhe Wang, Meng Xu, N. Asokan — [Finding Vulnerabilities via LLM-Augmented Semantics-Aware Type-Checking](http://arxiv.org/abs/2608.14533v1)
  <details><summary>📄 Abstract</summary>
  Vulnerability detection via static analysis traditionally relies on security experts encoding insecure coding patterns into algorithmic rules. However, this approach often focuses on syntactic patterns and overlooks deeper semantic information in the code, such as the meanings of variable and function names. As software systems grow more complex, modeling vulnerabilities using only syntactic rules becomes increasingly challenging.   In this paper, we propose a semantics-aware approach to detecti...
  </details>

- **2026-08-14** — Noel Murasko, John C. Bowman — [Hybrid Dealiasing and Implicit Packing for Real Convolutions](http://arxiv.org/abs/2608.14497v1)
  <details><summary>📄 Abstract</summary>
  Hybrid dealiasing is an FFT-based method for computing linear convolutions of complex-valued data that reduces the cost of dealiasing by performing zero padding implicitly. We develop two new algorithms that extend hybrid dealiasing to real-valued convolutions.   The first algorithm exploits conjugate symmetries in the transformed data and computes each residue contribution directly. The second algorithm employs complex-valued hybrid dealiasing via a new implicit packing technique, which packs r...
  </details>

- **2026-08-14** — Panjing He, Mingyue Cheng, Yucong Luo et al. — [SheetCompass: Hierarchical Relation Graphs for Agentic Spreadsheet Reasoning](http://arxiv.org/abs/2608.14452v1)
  <details><summary>📄 Abstract</summary>
  Spreadsheets are widely used to organize, analyze, and manipulate semi-structured data, yet automated spreadsheet reasoning remains challenging for large language models (LLMs). Real-world workbooks often contain implicit cross-table associations, fine-grained column dependencies, and complex spatial layouts. Existing methods typically flatten these multidimensional structures into sequential strings, losing important intra-sheet boundaries and inter-sheet semantics. Consequently, LLMs cannot ex...
  </details>

- **2026-08-14** — Ignacio D. Lopez-Miguel, Andreas Happe, Jürgen Cito et al. — [ATLAS: Discovering Agent Strategies through LLM-Guided Abstraction and Automata Learning](http://arxiv.org/abs/2608.14352v1)
  <details><summary>📄 Abstract</summary>
  Large Language Model (LLM)-based agents are increasingly used for complex tasks such as software testing and cybersecurity assessment. While these agents demonstrate impressive capabilities, their behavior is difficult to understand, explain, and analyze. Existing evaluations focus mainly on task success and execution traces, offering limited insight into the strategies employed by the agent. We present ATLAS (Automata Learning for Agent Trajectory Analysis and Strategy Discovery), an approach f...
  </details>

- **2026-08-14** — Seeyeon Kim, Juhyeong Jin, Joo-Young Kim — [Beyond Capacity: Scalable MoE LLM Inference via High-Bandwidth Flash with Direct GPU and HBM Paths](http://arxiv.org/abs/2608.14333v1)
  <details><summary>📄 Abstract</summary>
  Modern mixture-of-experts (MoE) language models increasingly strain the capacity and cost efficiency of high-bandwidth memory (HBM), as rapidly growing expert weights must be provisioned close to GPUs. High-bandwidth flash (HBF) offers substantially greater capacity, but conventional designs typically deliver HBF-resident expert weights to the GPU through HBM, leaving an additional direct GPU-HBF connection underutilized. We explore an HBF organization that simultaneously exploits two independen...
  </details>

- **2026-08-14** — Francesco Quinzan, Noor Munir, Yishun Lu et al. — [Detecting Contaminated Code-Generation Prompt Batches via Influence Functions](http://arxiv.org/abs/2608.14303v1)
  <details><summary>📄 Abstract</summary>
  Large language models (LLMs) are increasingly used for code generation, yet they remain vulnerable to prompts that elicit insecure implementations. Existing defenses typically rely on predefined threat models or known vulnerability patterns, limiting their effectiveness against novel attacks. We propose CodeSIFT, a threat-model-agnostic detection method that leverages influence functions to identify batches of prompts that induce anomalous model behavior. Rather than detecting specific vulnerabi...
  </details>

- **2026-08-14** — Sojeong Park, Hyeonsu Lyu, Jaehyun Choi et al. — [LLM-Assisted LDPC Decoding via Syndrome-Verified Semantic Priors](http://arxiv.org/abs/2608.14280v1)
  <details><summary>📄 Abstract</summary>
  Semantic communication exploits the meaning of the payload, which bit-level processing discards. When channel decoding fails on a natural language payload, the errors appear as corrupted characters in the recovered text. A large language model (LLM) infers the intended characters from the semantic context, but it can also produce incorrect corrections. Applying them directly introduces new bit errors when the LLM modifies characters incorrectly. In this paper, we propose an LLM-assisted decoding...
  </details>

- **2026-08-14** — Varsha Ramineni, Hossein A. Rahmani, Jerome Ramos et al. — [BiasTrace: Linking Reasoning Behaviours to Biased Outputs in LLMs](http://arxiv.org/abs/2608.14161v1)
  <details><summary>📄 Abstract</summary>
  LLMs exhibit social biases that can produce inaccurate and discriminatory inferences, posing risks in high-stakes applications. While prior work has made progress in measuring and mitigating bias, it largely focuses on final outputs of models, with limited understanding of the mechanisms that produce biased outcomes. Recent advances in LLM reasoning offers a new lens for investigating bias, yet the link between reasoning and bias remains poorly understood. Existing approaches focus primarily on ...
  </details>

- **2026-08-14** — Ziyan He, Xiongtai Yang, Tao Wang — [PISA: A Pseudo-Individual Source-Domain Feature Adaptation Framework for Test-Time Open-Vocabulary Object Detection](http://arxiv.org/abs/2608.14142v1)
  <details><summary>📄 Abstract</summary>
  Open-vocabulary object detection test-time adaptation (OVOD-TTA) aims to address the performance degradation that pre-trained base models suffer when encountering image-domain shifts. Existing source-free OVOD-TTA methods rely either on refined test-time information for re-scoring or on pseudo-labels for self-training, leading to significant accuracy degradation when initial predictions are poor. Meanwhile, most conventional source-domain estimation methods recover abstract, sparse representatio...
  </details>

- **2026-08-14** — Ismail El Hamraoui, Sagar Jose, Nicolas Bureau et al. — [A Graph-Based Reinforcement Learning Framework for Structured Drift Diagnosis and Recovery in Autonomous LLM Agents](http://arxiv.org/abs/2608.14109v1)
  <details><summary>📄 Abstract</summary>
  Autonomous LLM agents are increasingly deployed in complex real-world workflows, yet they remain vulnerable to runtime behavioral drift, a silent deviation from the original task that can lead to irreversible side effects on external systems. Existing approaches address drift at the prompt level but lack structured mechanisms for step-level detection, risk assessment, and recovery decision. Because the main task-executing agent is often a large and expensive model that cannot be re-trained on ev...
  </details>


### 📂 defense
*防御与防护方法 / Defense & Protection Methods* — 63 papers

- **2026-08-18** — Rabimba Karanjai, Yang Lu, Nour Diallo et al. — [When Agents Act on Web3: An Attack-Surface Survey of MCP, Skills, and Tool Calling](http://arxiv.org/abs/2608.17275v1)
  <details><summary>📄 Abstract</summary>
  AI agents increasingly act rather than merely read: across the Model Context Protocol (MCP) ecosystem, the share of deployed tools that modify external state has risen from 27% to 65% of tool use. When agents exercise this authority on public blockchains through MCP, skills, and tool calling, the consequences of an attack are governed by the blockchain execution layer rather than by conventional software assumptions. This survey argues that four properties of that layer (irreversibility, signing...
  </details>

- **2026-08-18** — Yeongwoo Kim, Quanyan Zhu, György Dán — [ADAPTD: Adaptive Detection and Proactive Threat Defense for Autonomous APT attacks](http://arxiv.org/abs/2608.17251v1)
  <details><summary>📄 Abstract</summary>
  Advanced persistent threat (APT) actors increasingly employ sophisticated techniques to propagate laterally through segmented enterprise networks. Timely detection and defense depend on cross-subnetwork coordination, yet maintaining global situational awareness generates substantial communication overhead. To manage this tradeoff, flexible monitoring and adaptable containment are imperative. This paper presents ADAPTD, a communication- and computation-efficient, decision-theoretic framework inte...
  </details>

- **2026-08-18** — Xingjian Wang, Zhao Wang, Taihang Hu et al. — [From Corpora to Co-Evolving Capabilities: Capability-Centric Data Design for Generalist Image Generation](http://arxiv.org/abs/2608.18076v1)
  <details><summary>📄 Abstract</summary>
  Large-scale image generation has benefited from advances in data scale, quality, rebalancing, and recaptioning, yet conventional pipelines typically optimize task-specific datasets in isolation. A central challenge is not only how to curate each task-specific corpus, but also how to organize heterogeneous supervision according to the dependencies among generative capabilities. We present a \textbf{capability-driven data infrastructure} that couples capability-specific supervision construction wi...
  </details>

- **2026-08-18** — Hollis Robbins — [Language Has Two Parameters: Narrative-Induced Semantic Plasticity and Phase-Sensitive Interpretation](http://arxiv.org/abs/2608.18041v1)
  <details><summary>📄 Abstract</summary>
  Language has two parameters. Count how often words occur together and you estimate amplitude, the strength of association. Word embeddings and attention weights refine that count, which sums every writer in the corpus together. This paper claims a second parameter, phase, which signed weights learned from a corpus do not supply. Phase exists only between meanings: it determines how coactivated meanings combine, and it can reverse what a meaning contributes while that meaning stays fully present....
  </details>

- **2026-08-18** — Lu Xu, Xu Li, Linjiang Zheng et al. — [Can Large Language Models Explain Flight Safety Events? A Prior-Guided Semantic LLM-based Approach](http://arxiv.org/abs/2608.18017v1)
  <details><summary>📄 Abstract</summary>
  Improving flight safety with flight data requires not only accurate detection of risk events, but more importantly, clear interpretation of their underlying causes at the level of pilot control behavior. Existing explainable AI techniques, such as feature importance maps, often require considerable domain knowledge to translate them into operationally meaningful explanations. Large Language Models (LLMs), which excel at language reasoning, bring a promising solution to this issue. However, apply...
  </details>

- **2026-08-18** — Lotta Kiefer, Brisca Balthes, Christoph Leiter et al. — [When Writing Style Drifts: Benchmarking Authorship Verification under Distribution Shifts in Genre, Time and the AI-Era](http://arxiv.org/abs/2608.17979v1)
  <details><summary>📄 Abstract</summary>
  Authorship verification (AV) assumes that an author's writing style remains sufficiently stable to distinguish it from that of other writers. In practice, however, this assumption is challenged by distribution shifts caused by changes in genre, time, and AI-assisted writing. Existing AV benchmarks typically study these factors in isolation and focus predominantly on English, limiting our understanding of model robustness under realistic conditions. We introduce AVShift, the first German benchmar...
  </details>

- **2026-08-18** — Ziya Zhou, Shangda Wu, Shenyang Xu et al. — [UniVerse: Benchmarking and Enhancing LALMs on Culturally Inclusive Low-Resource Music Understanding](http://arxiv.org/abs/2608.17852v1)
  <details><summary>📄 Abstract</summary>
  Recent advances in large audio-language models (LALMs) have significantly improved performance in tasks such as music captioning, genre classification, and sound event detection. However, limited attention has been paid to improving their adaptability across diverse musical traditions, particularly folk music rooted in distinct cultural contexts. Folk-music traditions are typically resource-scarce, unevenly represented across regions, and poorly documented. Even when such samples appear in large...
  </details>

- **2026-08-18** — Tanel Liiv, Sander Soodla, Nzamba Bignoumba et al. — [Training with synthetic data for drone detection in thermal imagery](http://arxiv.org/abs/2608.17799v1)
  <details><summary>📄 Abstract</summary>
  Ground-to-Air (G2A) drone detection in medium- and long-wave infrared (MWIR/LWIR) imagery is challenging due to reduced texture information, sensor noise, weak thermal contrast, and the scarcity of annotated data. This work investigates a synthetic-first training strategy that combines synthetic scene generation with fine-tuning on real data. We show that synthetic data provides an effective basis for learning initial object representations, while real in-domain thermal imagery is still essentia...
  </details>

- **2026-08-18** — Abdul Mueez, Aaditya Baranwal, Junior Chaj-Mejia et al. — [Vision-Language Models for Analog Gauge Reading: An Empirical Study of Specialization, Transfer and Reliability](http://arxiv.org/abs/2608.17723v1)
  <details><summary>📄 Abstract</summary>
  Analog gauges remain common in industrial environments where manual inspection is costly or hazardous. The engineering application addressed here is direct numerical reading of single-target analog-gauge images, while the artificial-intelligence contribution is a systematic evaluation of specialization, transfer, robustness and reliability for a general-purpose vision-language model (VLM) without an explicit pointer-segmentation and geometric-reading pipeline. The Qwen2.5-VL-7B-Instruct model is...
  </details>

- **2026-08-18** — Bowen Sun, Yixi Cai, Xiaogeng Liu et al. — [KeyPooling: Measuring Where LLM API Relay Paths Collapse Prompt Cache Isolation](http://arxiv.org/abs/2608.17485v1)
  <details><summary>📄 Abstract</summary>
  Large language model (LLM) API relays authenticate customers separately but often forward requests through shared provider credentials. Providers scope prompt caches to upstream principals and namespaces, so relay customers mapped to one cache identity can observe each other's cache state. Prior work showed cache sharing at selected endpoints but did not identify which credential, pool, adapter, or nested hop controls the finalidentity. We present KeyPooling, a measurement method that traces cus...
  </details>

- **2026-08-18** — Yiming Du, Yuxin Jiang, Tao Yuan et al. — [LEGO-RL: Harness-Native Reinforcement Learning for Coding Agents](http://arxiv.org/abs/2608.17393v1)
  <details><summary>📄 Abstract</summary>
  Reinforcement learning for coding agents increasingly relies on long-running agent harnesses to manage tool integration, repository contexts, and execution feedback. However, the native execution environments of these harnesses are inherently misaligned with policy-gradient training: environmental crashes and reward hacking corrupt outcome signals, while train-inference discrepancies decouple rollout behavior from policy updates. To address this, we present LEGO-RL, a framework that bridges nati...
  </details>

- **2026-08-18** — Qishuang Fu, Andreas Deppeler, Joseph K. Liu et al. — [FlowShield: cryptocurrency anti-money laundering with transaction semantics parsing and fund flow tracking](http://arxiv.org/abs/2608.17355v1)
  <details><summary>📄 Abstract</summary>
  Cryptocurrency anti-money laundering (Crypto AML) is increasingly challenged by sophisticated laundering behaviors that rapidly fragment stolen assets through diverse semantics and across multiple blockchains. Existing Crypto AML methods often simplify transaction semantics, rely on topology-centric signals, or output isolated detection labels. In this paper, we present \textsc{FlowShield}, a Crypto AML framework for transaction-level laundering detection and investigator-facing report generatio...
  </details>

- **2026-08-18** — Junwei Zhou, Zhen Sun, Binyu Li et al. — [ASI-Bench: At the Dawn of Artificial Superintelligence](http://arxiv.org/abs/2608.17271v1)
  <details><summary>📄 Abstract</summary>
  Artificial superintelligence (ASI) requires AI to move beyond mastering existing knowledge toward exploring the unknown, creating new knowledge, and turning new ideas into verifiable results. However, the capabilities of today's AI systems are still largely built on learning, compressing, and applying existing human knowledge. Accordingly, existing benchmarks primarily test whether AI can produce correct answers based on learned knowledge, or whether it can complete tasks under extensive human g...
  </details>

- **2026-08-18** — Yijie Xu, Chao Wang, Hui Xiong — [Against Political Polarization: A Unified Framework for Tracing Evolving Political Ideologies on Social Media](http://arxiv.org/abs/2608.17987v1)
  <details><summary>📄 Abstract</summary>
  The rapid growth of social media has greatly influenced political discourse, highlighting the need to understand individual political ideologies and their temporal dynamics. This task faces challenges such as data scarcity, abundant non-political content, costly and bias-prone manual annotation, and difficulty in modeling future ideological inclinations. To address these issues, we propose TSN4PI, a unified framework for tracking the evolution of political ideologies on social media. It includes...
  </details>

- **2026-08-18** — Bin Li, Dongdong Wang, Siyang Lu — [Too Sure to Be Safe: Model Calibration for Reliable Log Anomaly Detection](http://arxiv.org/abs/2608.17965v1)
  <details><summary>📄 Abstract</summary>
  Online log anomaly detection is critical for maintaining the reliability of large-scale computing systems. Although recent language model-based log anomaly detectors achieve strong detection performance, their confidence estimates remain poorly calibrated. We show that these detectors frequently assign excessive confidence to incorrect predictions, particularly for anomalous logs under severe class imbalance. Moreover, confidence on erroneous predictions remains persistently high even when conve...
  </details>

- **2026-08-18** — Md. Faiyaz Abdullah Sayeedi — [Do Large Language Models Play Six Degrees of Separation? Measuring Topological Compression in Long-Context Manifolds](http://arxiv.org/abs/2608.17950v1)
  <details><summary>📄 Abstract</summary>
  Large Language Models (LLMs) demonstrate remarkable multi-hop reasoning capabilities over long contexts, yet the internal mechanisms enabling these distant cognitive leaps remain poorly understood. Traditional attention-based interpretability often fails to capture true semantic proximity due to routing artifacts like attention sinks. In this paper, we bypass attention weights to directly analyze the dynamic geometry of the hidden state manifold, proving that deep LLM latent spaces natively orga...
  </details>

- **2026-08-18** — Xule Liu, Yijun Liu, Chao Li et al. — [D$^2$ACCI: A Dual-Loop Diagnostic Protocol for Evidence-Preserving Agent Memory](http://arxiv.org/abs/2608.17756v1)
  <details><summary>📄 Abstract</summary>
  Memory is a key capability of LLM agents. Persistent memory extends this across sessions---enabling recall, revision, and personalization. Yet its multi-stage pipeline (ingestion, retrieval, filtering, generation) makes failures difficult to localize: end-to-end evaluation reveals that an error occurred, but not which stage caused it. Existing evaluations often report aggregate performance without paired statistical comparisons, slice-level non-regression checks, or stage-level diagnostic traces...
  </details>

- **2026-08-18** — Shenghao Chen, Hao Jia, Chen Li et al. — [Environment-Invariant Subspace Learning for Generalizable Deepfake Detection](http://arxiv.org/abs/2608.17700v1)
  <details><summary>📄 Abstract</summary>
  Cross-distribution generalization remains a critical bottleneck in deepfake detection. While recent efforts leverage the semantic priors of large-scale visual foundation models (VFMs), a noteworthy yet underexplored challenge remains: the susceptibility of these semantic priors to environmental interference from factors such as lighting and style. Crucially, this interference establishes spurious correlations between forgery cues and environmental patterns that severely limit generalization. To ...
  </details>

- **2026-08-18** — Tianjing Hao, Haiyu Lan, Angsong Li et al. — [OVIP-SG: Open-Vocabulary Instance-Preserving Scene Graphs for Mapping and Retrieval of Small, Fine-Grained Objects](http://arxiv.org/abs/2608.17633v1)
  <details><summary>📄 Abstract</summary>
  Integrating open-vocabulary perception into object-level 3D scene graphs is a double-edged sword. While vision-language detectors recover long-tail categories and small, fine-grained objects overlooked by closed-set models, they also tend to fragment large surfaces and merge small objects into larger neighboring objects, compromising instance-level consistency and undermining mapping fidelity. Moreover, existing methods struggle to retrieve previously unmapped targets or determine whether a quer...
  </details>

- **2026-08-17** — Abyad Enan, Sagar Dasgupta, Mizanur Rahman et al. — [Structured Driving-State Narratives for Small Language Model-Based GNSS Spoofing Detection](http://arxiv.org/abs/2608.17092v1)
  <details><summary>📄 Abstract</summary>
  Autonomous vehicles (AVs) depend on reliable Global Navigation Satellite System (GNSS) positioning. However, spoofed GNSS signals can induce plausible but incorrect vehicle states. This study develops a small language model (SLM)-based framework for detecting and classifying GNSS spoofing attacks by comparing vehicle behaviors independently derived from GNSS and other sensing sources. The framework converts independent driving states from GNSS and other sensing sources into structured semantic n...
  </details>

- **2026-08-17** — Manjushree Aithal, Alexander Kotz, James Mitchell — [LadderTeam: Dual-Agent Laddering Elicitation Framework](http://arxiv.org/abs/2608.17029v1)
  <details><summary>📄 Abstract</summary>
  Eliciting detailed and actionable software requirements from end-users is a critical phase in the iterative development of a software product or application. To ensure the feedback collected is detailed and actionable, software teams can leverage the laddering interview technique. While effective for ensuring granular and actionable items from the software feedback, these interviews are subject to several limitations. They are traditionally a manual process associated with a time and financial b...
  </details>

- **2026-08-17** — Flint Xiaofeng Fan, Cheston Tan, Yew-Soon Ong et al. — [FedPref: Federated Preference Learning for Structured Radiology Report Extraction](http://arxiv.org/abs/2608.16971v1)
  <details><summary>📄 Abstract</summary>
  Radiology reports describe findings and locations in free text, but downstream search and analysis require these relations in a fixed schema. Learning this extraction requires labels that are unevenly distributed across institutions: smaller hospitals have less local evidence, and pooling data may be infeasible. We introduce FedPref: frozen public language models propose alternative JSON extractions, local annotations rank them, and sites collaboratively train compact Qwen3-8B adapters while sha...
  </details>

- **2026-08-17** — Saisab Sadhu, Aadit Sengupta, Vinay Kumar Sankarapu et al. — [What Do Compliance Detectors Read? An Audit of Activation Probes and Guard Models](http://arxiv.org/abs/2608.16852v1)
  <details><summary>📄 Abstract</summary>
  Regulatory compliance monitoring in deployed language models is increasingly implemented as a legal and audit control, checking model outputs against written rules spanning data protection, healthcare, financial regulation, and platform policy. Such monitoring is meaningful only if a detector's verdict depends on the stated rule rather than on surface features of the scenario. We show this condition fails across the current class of compliance detectors, a failure we call rule blindness. Deletin...
  </details>

- **2026-08-17** — Abdullah Alghamdi, Siamak Layeghy, Marius Portmann — [LLMs for Zero-Shot Threat Detection via Structured Risk Indicators](http://arxiv.org/abs/2608.16508v1)
  <details><summary>📄 Abstract</summary>
  We propose a two-stage large language model (LLM) framework for zero-shot detection of insider threats and advanced persistent threats (APTs) from heterogeneous security logs. The framework models user activity as chronological timelines and incorporates retrieval-augmented generation (RAG) to provide personalised behavioural context from each user's historical activity. Rather than performing end-to-end classification directly from raw logs, it first generates structured, interpretable sets of ...
  </details>

- **2026-08-17** — Stylianos Kampakis, Fabio Rovai, Marcos Charalambides et al. — [Proving the Utility of Large Language Models in Cybersecurity Simulations: A Comprehensive Examination](http://arxiv.org/abs/2608.16422v1)
  <details><summary>📄 Abstract</summary>
  Cyber threats continue to escalate in both frequency and sophistication, necessitating more adaptive and scalable defense strategies. This paper explores how Large Language Models (LLMs) can bolster cybersecurity simulations by automating the creation of synthetic environments and identifying latent vulnerabilities. We employ YAML as a structured representation format for simulating complex network configurations, thereby enabling Large Language Model-driven pipelines to support and improve rein...
  </details>

- **2026-08-17** — Marta Sumyk, Oleksandr Kosovan, Iryna Voitsitska — [Synthetic Data Augmentation for Satellite-Based Analysis of Battle-Damaged Agricultural Fields in Ukraine](http://arxiv.org/abs/2608.16380v1)
  <details><summary>📄 Abstract</summary>
  Monitoring war-induced damage to agricultural land in Ukraine is important for understanding threats to food security, environmental stability, and post-war recovery. However, the development of computer-vision systems for satellite-based damage analysis is limited by the scarcity of labeled imagery, especially for damaged agricultural fields. This work investigates synthetic data augmentation as a method for improving classification under limited and imbalanced training data. We train class-con...
  </details>

- **2026-08-17** — Konstantinos E. Kampourakis, Vasileios Gkioulos, Sokratis Katsikas — [Digital Twin Degradation: Detecting Cyber Physical Attacks via Temporal Inconsistencies](http://arxiv.org/abs/2608.16159v1)
  <details><summary>📄 Abstract</summary>
  Digital Twins (DTs) are increasingly used to monitor and analyze Cyber Physical Systems (CPS). However, in adversarial environments, the fidelity of a DT cannot be assumed. Communication delays, data manipulation, sensor degradation, or partial information loss may cause the DT state to diverge from the physical process it represents. Such divergence creates temporal inconsistencies that may reveal cyber physical attacks. This paper proposes a detection framework that monitors temporal consisten...
  </details>

- **2026-08-17** — Md Habibur Rahman, Jaeho Kim — [Proof-of-Execution Memory: Defending LLM Agents Against Forged-Reasoning Attacks by Verifying What Actually Happened](http://arxiv.org/abs/2608.16032v1)
  <details><summary>📄 Abstract</summary>
  LLM agents are stateless and rely on external memory to carry context between steps. Because agents treat that memory as trustworthy, an adversary who can write to it can steer their behavior. The FARMA attack does this with no malicious command: it inserts fabricated entries into the agent's reasoning memory claiming a required safety step is already done, so the agent skips it. SENTINEL, the defense proposed with FARMA, scores entries against a fixed list of suspicious wordings; its authors no...
  </details>

- **2026-08-17** — Huatong Song, Fei Bai, Ming Yang et al. — [ClawGym II: Exploring Black-Box RL on Agent Harness](http://arxiv.org/abs/2608.16798v1)
  <details><summary>📄 Abstract</summary>
  Agent harnesses have substantially improved performance on long-horizon tasks by coordinating agent interactions with the environment. However, reinforcement learning through complex harnesses remains largely unexplored, as scaling such training to long-horizon agent tasks introduces fundamental challenges. In this work, we present a unified black-box RL framework for stable and scalable optimization of general agents through complex harnesses. Concretely, we first build a sandbox-based executio...
  </details>

- **2026-08-17** — Artem Sergievskii, Artyom Turevich, Sergey Kastryulin — [Revisiting Classifier-Free Guidance Methods in Latent Diffusion Models](http://arxiv.org/abs/2608.16786v1)
  <details><summary>📄 Abstract</summary>
  Inference-time quality-enhancement methods are an effective and widely adopted means of improving diffusion models without expensive retraining. We study a family of training-free techniques conceptually rooted in Classifier-Free Guidance (CFG), most of which were originally proposed on older U-Net diffusion models and validated using metrics that assess image quality in isolation, without accounting for compositional alignment or semantic correspondence between the generated image and its assoc...
  </details>

- **2026-08-17** — Batu El, Jinhee Paeng, Fatih Dinc et al. — [Physics of Agents: Statistical Mechanics Predicts Collective Behavior of AI Agents](http://arxiv.org/abs/2608.16578v1)
  <details><summary>📄 Abstract</summary>
  AI agents increasingly operate as part of interacting systems rather than in isolation. As agents exchange information and jointly make decisions, their interactions can improve collective reasoning but may also produce herding, polarization, or amplify shared biases. Understanding and predicting these collective dynamics is therefore important for designing effective and aligned multi-agent systems. Here, we study over 10,000 communities of language-model agents that repeatedly exchange message...
  </details>

- **2026-08-17** — Dennis Schrader, Eva-Maria Schön, Henning Fritzemeier et al. — [Operationalizing the EU AI Act in Agile Software Development: A Guideline-Based Approach](http://arxiv.org/abs/2608.16526v1)
  <details><summary>📄 Abstract</summary>
  Context: The EU AI Act requires providers and deployers of Artificial Intelligence (AI) systems to implement documentation, risk management, and human oversight. Agile teams that ship AI features in short iterations lack specific artifacts to discharge these duties, since the regulation's abstract provisions do not map onto the Definition of Done, Sprint Reviews, or working agreements. Objective: We provide agile teams with an actionable compliance instrument: an evaluated guideline that operati...
  </details>

- **2026-08-17** — Zigan Zhou, Kai Li, Yupeng Deng — [Remote-Sensing City Layout Extraction with MLLM](http://arxiv.org/abs/2608.16484v1)
  <details><summary>📄 Abstract</summary>
  Remote-sensing systems usually describe urban content with detection boxes, semantic masks, or vector boundaries. Such outputs locate classes and support image-plane scoring, yet they do not by themselves constitute an executable layout that retains object identities, typed relations, topology, and regeneration rules. Code-as-City instead casts urban-layout extraction from a single top-down image as constrained code generation with a multimodal large language model (MLLM). An image model first p...
  </details>

- **2026-08-17** — Zhihao Guo, Zonghan Wu, Huan Huo et al. — [HalluTracer: Hallucination Detection via Depth-Averaging Truth Signals](http://arxiv.org/abs/2608.16353v1)
  <details><summary>📄 Abstract</summary>
  Even well-aligned large language models confidently generate factually incorrect text, making hallucination a persistent reliability risk in high-stakes deployments. These models nonetheless carry linearly separable truthfulness signals in their internal representations. Existing white-box detectors, however, collapse this evidence to isolated components or a single depth, discarding discriminative information distributed across the full forward pass. We introduce HalluTracer, a detection framew...
  </details>

- **2026-08-17** — Mohammadparsa Karimi, Majid Nabi, Andrew Nelson et al. — [SbDN: Source-based TSN-Grade Deterministic Networking using Commodity Switches](http://arxiv.org/abs/2608.16199v1)
  <details><summary>📄 Abstract</summary>
  Deterministic networking is essential for safety-critical applications in automotive, industrial, and aerospace systems, where bounded end-to-end latency must be guaranteed for time-critical traffic. Time-Sensitive Networking (TSN) provides the mechanisms to achieve such guarantees, but its deployment requires expensive TSN-capable switches at every hop and complex per-switch configuration that hinders runtime reconfiguration. This paper presents SbDN, a Multi-Agent Source-based architecture tha...
  </details>

- **2026-08-17** — Jiadao Zou, Hongyu Guo, Wei Xi — [Decoupling Parcellation from Classification: Systematic Benchmark of Fast Brain Segmentation Methods for Alzheimer's Disease Detection](http://arxiv.org/abs/2608.16039v1)
  <details><summary>📄 Abstract</summary>
  Brain parcellation and classification are typically evaluated in isolation, yet downstream AD detection performance depends on their interaction. We decouple these components and systematically benchmark fast deep learning parcellation methods (SynthSeg+, OpenMAP-T1) against the FreeSurfer (FS-HV) clinical baseline through down- stream AD classification on OASIS-1. Our factorial design evaluates three parcellation methods, two volumetry strategies (hard vs. soft), and four classifier paradigms (...
  </details>

- **2026-08-17** — Zhengzhao Ma. Boxi Cao, Yaojie Lu, Hongyu Lin et al. — [From Sequence to Structure: Relational Uncertainty Propagation for LLM Agents](http://arxiv.org/abs/2608.16002v1)
  <details><summary>📄 Abstract</summary>
  Reliable uncertainty quantification (UQ) is essential for deploying large language model (LLM) agents in complex interactive environments. Existing UQ methods largely rely on local signals, such as token probabilities, predictive entropy, or per-step confidence, and therefore overlook the long-range dependencies through which errors accumulate across an execution trajectory. As a result, they may fail to identify agent failures whose causes originate several reasoning or interaction steps before...
  </details>

- **2026-08-17** — Junjie Chu, Ye Leng, Mingjie Li et al. — [GEO-Flag: Detecting and Measuring GEO-Optimized Web Content](http://arxiv.org/abs/2608.16824v1)
  <details><summary>📄 Abstract</summary>
  Generative Engine Optimization (GEO) modifies web content to increase its likelihood of being selected and cited by generative search engines. This can give strategically optimized pages visibility disproportionate to their authority or relevance and even make weak or false information appear well supported. Unlike conventional search, generative search synthesizes information into direct answers rather than presenting competing sources, which can further amplify these risks, as assessing source...
  </details>

- **2026-08-17** — Divine Yao Agbobli, Geoffery Eyram Agorku, Israel Afriyie et al. — [DRAFE: Domain-Robust Asymmetric Fusion of Heterogeneous Detection Transformers for Cross-City Fine-Grained Traffic Object Detection](http://arxiv.org/abs/2608.16632v1)
  <details><summary>📄 Abstract</summary>
  Deep learning-based object detectors are fundamental to intelligent transportation systems, enabling traffic monitoring, vehicle analytics, and infrastructure management. However, achieving both fine-grained vehicle recognition and robust cross-city domain generalization remains challenging. We present the Domain-Robust Asymmetric Fusion Ensemble (DRAFE), which combines independently trained LW-DETR and RF-DETR detectors for cross-city fine-grained traffic object detection. DRAFE employs a two-s...
  </details>

- **2026-08-17** — Dong Chen, Kenneth M. C. Cheung — [TokenSTFormer: A Tokenized Spatial-temporal Attention Model for Holistic Motion Analysis in Adolescent Idiopathic Scoliosis Screening](http://arxiv.org/abs/2608.16122v1)
  <details><summary>📄 Abstract</summary>
  Adolescent Idiopathic Scoliosis (AIS) is a prevalent spinal deformity in adolescents that, if left untreated, can result in severe health outcomes. Traditional screening methods are limited by subjective interpretation, reliance on professional expertise and low scalability. To address these challenges, we present ScoliGait dataset, which comprises 1,516 gait video clips paired with corresponding X-ray records. We also introduce TokenSTFormer, a novel model that tokenizes spatial and temporal se...
  </details>

- **2026-08-17** — Sachin Deb, Harshit Sharma, Asif Salekin — [Representation Is Not Enough: Body-Localized Thermal Evidence for Contactless Stress and Craving Sensing in Opioid Use Disorder](http://arxiv.org/abs/2608.16087v1)
  <details><summary>📄 Abstract</summary>
  Removing wearables from physiological monitoring also removes their supervision: the signal indicating where and when a stress response occurred. Contactless stress sensing therefore becomes a weakly supervised evidence-localization problem, where a clip-level label must be traced to the body regions and moments that produced it. We address this with FABLE-Therm, a weakly supervised architecture that preserves localized evidence across body regions, time, and encoder-specific representations unt...
  </details>

- **2026-08-17** — Anton Tolstonogov, David Cabecinhas, Pedro Batista et al. — [Moving Horizon Estimation for Underwater Target Tracking Based on Time-Difference-of-Arrival Measurements](http://arxiv.org/abs/2608.16024v1)
  <details><summary>📄 Abstract</summary>
  There has been a flurry of activity in the development of robotic systems to localize and track underwater man-made or natural targets based on sparse acoustic data. Compelling examples include the development of surface tracking systems to aid in the navigation of groups of underwater vehicles performing environmental monitoring missions or to study the motion patterns of large underwater fauna. With current technology, the latter case can only be tackled using Time-Difference-of-Arrival (TDoA)...
  </details>

- **2026-08-16** — Nabil Ashab, Soumit Kumar Kundu, Saif Mahmud Parvez et al. — [MagViT: Interpretable Multi-Magnification Transformers with Patient-Level Model Selection for Breast Histopathology](http://arxiv.org/abs/2608.16959v1)
  <details><summary>📄 Abstract</summary>
  Breast cancer is one of the most common types of cancer among women around the world. Rapid detection and early treatment can hinder its progress to more complex stages and can impede its spread to other parts of the body. Histopathological image classification is the most common task in cancer detection due to its robustness in analyzing cellular data. Breast histopathology classification requires handling both multi-scale tissue morphology and clinically relevant generalization beyond the sour...
  </details>

- **2026-08-16** — Yuchen Zhang, Shuang Dai, Zeyu Fu et al. — [CLARA: Clip-Level Multimodal Alignment with VLM-Derived Rationales for Hateful Video Detection](http://arxiv.org/abs/2608.15905v1)
  <details><summary>📄 Abstract</summary>
  Hateful video detection has become increasingly important with the rapid growth of video-centric social media platforms, given the serious risks that hate speech poses to both individual well-being and social cohesion. Compared with text or static multimodal content, hateful video detection remains underexplored and significantly more challenging, as hateful meaning often arises from complex interactions among multimodal cues, including speech, audio, and visual content. Moreover, such signals a...
  </details>

- **2026-08-16** — Kiyotaka Kasubuchi, Kazuo Fukiya — [QuantumPhaseNet: A Gauge-Covariant Geometric and Quantum-Spectral Theory of Semantic Concept Hierarchies with Prototype Validation of a Classical Quantum-Inspired Model](http://arxiv.org/abs/2608.15820v1)
  <details><summary>📄 Abstract</summary>
  We present QuantumPhaseNet, a gauge-covariant geometric and quantum-spectral extension of Transformer representations. Context-dependent semantic states are modeled as complex amplitudes; a covariant phase rate induces a semantic wavelength used as a proxy for conceptual scale; and low-frequency graph modes define a document-level discourse direction. The theoretical part establishes local gauge invariance, unitarity of the quantum block, boundedness and conditional stability of WavePhase Attent...
  </details>

- **2026-08-16** — Miyu Yamada, Yuki Arase — [Hallucination Span Detection with Input-Side Evidence Alignment](http://arxiv.org/abs/2608.15804v1)
  <details><summary>📄 Abstract</summary>
  Hallucinations remain a major obstacle to the reliable use of large language models (LLMs) in conditional text generation. Existing methods primarily assess the factuality of an entire generated text, providing limited insight into which output spans are hallucinated or how they relate to the input. We introduce the task of hallucination span detection with input-side evidence alignment, which jointly identifies hallucinated spans and aligns output tokens with the corresponding input evidence. O...
  </details>

- **2026-08-16** — Ted Lentsch, Santiago Montiel-Marín, Holger Caesar et al. — [Emergent 3D Instance Segmentation from Self-Supervised Point Transformers](http://arxiv.org/abs/2608.15796v1)
  <details><summary>📄 Abstract</summary>
  Unsupervised 3D instance segmentation of outdoor LiDAR scans has traditionally relied on handcrafted geometric priors such as density-based clustering, motion cues, or projected 2D detections. In this work, we investigate whether a frozen, self-supervised point transformer already contains the structural information required to isolate object instances without any handcrafted geometric prior. Using this transformer purely as a feature extractor, we probe its internal representations across the S...
  </details>

- **2026-08-16** — XinQi Wang, Jinwei Xiao, Sijia Cui et al. — [HyMem: Hierarchical Context Management for Long-Horizon Agents via Information Isolation](http://arxiv.org/abs/2608.15703v1)
  <details><summary>📄 Abstract</summary>
  Large language model (LLM) agents often perform poorly on complex, long-horizon tasks because their context becomes increasingly cluttered over time. As interactions accumulate, detailed execution traces and intermediate outputs dominate the context, making it difficult for the model to retain and use high-level planning information. Most existing methods address this issue through compression or retrieval applied to a single, flat context, which does not clearly separate different types of cont...
  </details>

- **2026-08-16** — Omair Shafi Ahmed, Zohair Shafi — [Beat the Counter First: A Baseline for Temporal-Graph Anomaly Detectors](http://arxiv.org/abs/2608.15965v1)
  <details><summary>📄 Abstract</summary>
  Progress in streaming, edge-level graph anomaly detection (GAD) has been marked by increasingly elaborate architectures, from count-min-sketch chi square tests to memory-augmented attention networks. Yet the empirical gains attributable to this added complexity have not been systematically evaluated. We propose SimpleCount, a reference with no parameter fitting that selects one scalar feature per dataset from a fixed pool of counts, recencies, first-occurrence indicators, and count-derived trans...
  </details>

- **2026-08-16** — Ali Boudaghi, Alireza Nemati, Hadi Zare — [FirstDiff: One-Step Diffusion-Based Anomaly Detection for Multivariate Time Series via Initial Noise Prediction](http://arxiv.org/abs/2608.15727v1)
  <details><summary>📄 Abstract</summary>
  Diffusion models have recently shown strong potential for multivariate time-series anomaly detection by learning the distribution of normal data through iterative denoising. Existing diffusion-based approaches, however, typically perform anomaly detection after completing the reverse diffusion process, relying primarily on the final reconstructed signal and overlooking informative representations produced during denoising. This design incurs substantial computational cost and limits the use of i...
  </details>

- **2026-08-16** — Seungyeol Baek, Yoonbyung Chai, Yonghyeon Lee et al. — [Rotation-Invariant Multi-IMU Activity Recognition under Independent Per-Location Orientation Shifts](http://arxiv.org/abs/2608.15621v1)
  <details><summary>📄 Abstract</summary>
  Human Activity Recognition (HAR) with self-administered wearables, such as at-home rehabilitation and exercise monitoring, often requires reattaching inertial measurement units (IMUs) across sessions. In multi-IMU settings, this can induce independent orientation offsets across body locations, a deployment shift that conventional scalar HAR models do not structurally handle. Existing remedies rely on rotation augmentation, whose robustness depends on sampled transformations, or calibration and o...
  </details>

- **2026-08-15** — Yifeng He, Yundi Xu, Christopher Castro Gaw Gonzalo et al. — [Invariant Pretraining for Robust Code Representations](http://arxiv.org/abs/2608.15412v1)
  <details><summary>📄 Abstract</summary>
  Encoder-based code representation models remain widely deployed for discriminative tasks such as clone detection and code classification, where their small size and low inference cost are decisive. Their robustness, however, is fragile: under invariant programs, semantically equivalent code written in different syntactic forms, learned representations degrade substantially even though program behavior is unchanged. We present an empirical study of this robustness gap across four encoder baseline...
  </details>

- **2026-08-15** — Botao Amber Hu, Iris Long — [Afterlife Delegation Protocol: Speculative Design of Self-Sovereign Agents that Outlive Their Principals](http://arxiv.org/abs/2608.15405v1)
  <details><summary>📄 Abstract</summary>
  Afterlife Delegation Protocol is a speculative design project that asks what death becomes when a will can act eternally. We design a speculative protocol through which a living person signs an agentic will: upon a verified death, a self-sovereign AI agent spawns on blockchain -- an immutable, resistant, decentralized, infrastructural substrate that could last forever -- endowed with the funds and memories its principal attached to it, and persists indefinitely to execute the will, overridable b...
  </details>

- **2026-08-15** — Yi Yu, Jian Peng, Yucheng Lin et al. — [Earth Observation Foundation Models for Terrestrial Ecohydrology: From Representation Learning to Process Inference](http://arxiv.org/abs/2608.15282v1)
  <details><summary>📄 Abstract</summary>
  Earth observation foundation models (EOFMs) are emerging as reusable representation frameworks for data-driven retrieval, prediction and process modelling within ecohydrology, which integrate EO, meteorological forcing and process models to characterise coupled water, energy and carbon dynamics in vegetation and soil across scales. However, there is yet to be an ecohydrology-specific synthesis assessing the EOFM relevance, application evidence or evaluation requirements under uncertain reference...
  </details>

- **2026-08-15** — Yansong Ning, Jingwen Ye, Zhongkai Wu et al. — [VibeWorlding: Can Multimodal Agents Construct 3D Open Worlds End-to-End?](http://arxiv.org/abs/2608.15265v1)
  <details><summary>📄 Abstract</summary>
  Constructing an interactive 3D open world from a user query is important. However, existing methods are primarily evaluated on idealized, simple queries, making it difficult to systematically analyze and compare how multimodal agents understand user intent, use 3D tools, and reason over textual and visual 3D world information. To this end, we propose VibeWorlding, a unified framework for benchmarking and training vibe worlding agents: a multimodal agent that can autonomously infer user intent, p...
  </details>

- **2026-08-15** — Chaokun Chang, Yukun Zhou, Kaihua Fu et al. — [From LLM Inference to Agentic Workloads: Characterization and Implications for Serving Systems](http://arxiv.org/abs/2608.15127v1)
  <details><summary>📄 Abstract</summary>
  Agentic applications are shifting AI serving from isolated model inference to long-running workloads in which LLMs coordinate tools, environments, and persistent state. However, the system behavior of these workloads---where latency, cost, and bottlenecks arise---remains poorly characterized, leaving serving systems to rely on assumptions built for conventional inference. We present AgentSysBench, a benchmark suite and measurement toolkit with ten representative agentic applications and unified ...
  </details>

- **2026-08-15** — Yuzhou Yang, Qichao Ying, Sheng Li et al. — [RoE-FND: Synergizing LLMs with Experiential Learning for Effective and Generalizable Evidence-Based Fake News Detection](http://arxiv.org/abs/2608.15210v1)
  <details><summary>📄 Abstract</summary>
  The proliferation of deceptive content in social networks necessitates robust Fake News Detection (FND) systems. Existing pipelines either train detectors on labeled data or leverage Large Language Models (LLMs) for their reasoning ability. However, current approaches remain either limited in generalizability or prone to over-commitment to persuasive yet flawed rationales, lacking systematic experience and mechanisms to expose subtle reasoning errors. We propose \textbf{RoE-FND} (\textbf{\underl...
  </details>

- **2026-08-15** — Lei Tan, Shuwei Li, Mohan Kankanhalli et al. — [UC-VLM: Consistency-Driven Learning for AI-Generated Image Detection with Vision-Language Large Models](http://arxiv.org/abs/2608.15238v1)
  <details><summary>📄 Abstract</summary>
  Vision-Language Large Models (VLLMs) are promising for AI-generated image (AIGI) detection because they can produce both a prediction and a natural-language output. However, most existing VLLM-based detectors primarily fine-tune the language side while giving limited attention to low-level visual forensic cues. They also often depend on manually crafted prompts or human-annotated rationales, which limits scalability.We present UC-VLM, a unified multi-stage framework for AIGI detection that relie...
  </details>

- **2026-08-15** — Che Shen, Junwei Su, Lingpeng Kong et al. — [Structuring Semantic Embeddings for Principle Evaluation: A Prototype-Guided Contrastive Learning Approach](http://arxiv.org/abs/2608.15224v1)
  <details><summary>📄 Abstract</summary>
  Reliable post-hoc evaluation asks whether already generated text satisfies a target criterion after generation. In this paper we study a focused frozen-embedding setting using principle-evaluation proxy tasks: toxicity detection, fine-grained emotion categorization, and ordinal review rating. General-purpose text embeddings are widely deployed for such tasks, but broad semantic similarity can place semantically similar yet task-distinct examples in overlapping regions of the representation space...
  </details>

- **2026-08-14** — Yasir Ech-Chammakhy, Oussama Azrara, Jaafar Chbili et al. — [STINER: Automated Extraction of Strategic Cyber Threat Intelligence from X](http://arxiv.org/abs/2608.14418v1)
  <details><summary>📄 Abstract</summary>
  Strategic Cyber Threat Intelligence (CTI) focuses on high-level insights, such as identifying targeted industries, attributing attacks to specific ransomware groups, and assessing the scale of data loss. Today, X (formerly Twitter) has become the fastest source for this intelligence, often hosting real-time breach announcements days before formal vendor reports. Converting this raw chatter into actionable intelligence requires navigating a complex linguistic landscape. Conventional Named Entity ...
  </details>

- **2026-08-14** — Sheng Hong, Yixuan Huang, Weiwei Jiang et al. — [BGA: A noise-immune neural distillation framework for malicious signature extraction in high-entropy encrypted flows](http://arxiv.org/abs/2608.14126v1)
  <details><summary>📄 Abstract</summary>
  To mitigate attention dilution in high-entropy TLS 1.3 flows, we propose BGA, a noise-immune neural distillation framework for encrypted threat intelligence.The methodology first employs Analysis of Variance (ANOVA) to decouple high-discriminatory control-plane features - specifically industrial setpoints - from stochastic cryptographic noise. To resolve the extreme class imbalance within a corpus of 86,878 flow records, a Wasserstein GAN with Gradient Penalty (WGAN-GP) module, enforcing the 1-L...
  </details>

- **2026-08-14** — Thiago Sandoval, Ufuk Topcu — [Regime-Conditional Verification: Correctness Estimation for Adapting and Monitoring Safety Classifiers](http://arxiv.org/abs/2608.14089v1)
  <details><summary>📄 Abstract</summary>
  Safety classifiers deployed with large language models often fail for two reasons: their decisions reflect the policy learned during training rather than the deployer's desired policy, and their performance degrades as deployment traffic evolves. We present Regime-Conditional Verification (RCV), a lightweight wrapper that adapts an off-the-shelf safety classifier without retraining it. RCV estimates, from the classifier's internal representations, the probability that each prediction disagrees w...
  </details>

- **2026-08-14** — Yubo Zhang, Yiyao Liu, Xiaodong Wang — [Learning-to-Transition for Large-scale and High-Order MIMO Detection](http://arxiv.org/abs/2608.14511v1)
  <details><summary>📄 Abstract</summary>
  High-order multiple-input multiple-output (MIMO) detection requires efficient search over a large discrete symbol space while producing reliable soft information for channel decoding. This paper develops a learning-to-transition (L2T) framework that formulates MIMO detection as a stochastic sequence of complete-vector transitions. At each transition, a channel-coupled Transformer updates both the instance embedding and the sampling policy, while a blockwise autoregressive factorization captures ...
  </details>


### 📂 alignment
*对齐与安全约束 / Alignment & Safety Constraints* — 53 papers

- **2026-08-18** — Clara Meister — [TokEval: A Tokenizer Evaluation Suite](http://arxiv.org/abs/2608.18062v1)
  <details><summary>📄 Abstract</summary>
  Language model tokenizers are typically selected with minimal evaluation, despite the fact that their design choices directly impact model capabilities. This can be partly attributed to a limited understanding of which tokenizer properties affect which aspects of downstream performance. We introduce TokEval, a framework of tokenizer evaluation metrics that goes beyond standard measures like fertility and compression rate to capture linguistically and structurally meaningful properties, e.g., UTF...
  </details>

- **2026-08-18** — Sher Badshah, Ali Emami, Hassan Sajjad — [Judge, Retrieve, or Abstain: Uncertainty-Guarded LLM Judging with Provable Risk Guarantees](http://arxiv.org/abs/2608.17994v1)
  <details><summary>📄 Abstract</summary>
  Using LLMs as judges has become standard practice for evaluating model outputs at scale. This is particularly common for subjective, open-ended tasks such as assessing helpfulness or alignment, where no single reference answer exists. However, objective tasks introduce a distinct reliability challenge for reference-free LLM judging. In the absence of a reference answer, the judge evaluates factual correctness either through its parametric knowledge or through tool augmentation. Although the form...
  </details>

- **2026-08-18** — Neelesh Kumar Shukla, Debasmita Panda, Srutanik Bhaduri et al. — [TraceSQL: Traceable Answerability Estimation for Reference-Free Text-to-SQL Verification](http://arxiv.org/abs/2608.17795v1)
  <details><summary>📄 Abstract</summary>
  Text-to-SQL systems are commonly evaluated using ground-truth SQL queries or reference execution results, but such supervision is unavailable at inference time in real-world deployments. This creates a critical verification problem: given only a user question, database context, and generated SQL, can a system estimate whether the generated query is likely to correctly answer the question? Recent approaches use LLMs as judge or specialized agents to inspect generated SQL, but their decisions can ...
  </details>

- **2026-08-18** — Mehdi Djellabi, Louis-Paul Henry — [On the Expressive Power of the Transverse-Field Ising Model for Graph Learning](http://arxiv.org/abs/2608.17750v1)
  <details><summary>📄 Abstract</summary>
  We study the quantum evolution induced by graph-indexed Ising Hamiltonians as a source of structural signal for graph learning. Graph automorphisms preserve symmetries of the Hamiltonian, and these symmetries constrain the quantum evolution in a way that turns time-dependent local measurements into informative probes of graph structure. Leveraging this idea, we introduce QDAGer, a quantum-inspired graph-pair Transformer that injects quantum-dynamical features from time series of node occupations...
  </details>

- **2026-08-18** — Syeda Faiza Ahmed, Zien Sheikh Ali, Hunzalah Hassan Bhatti et al. — [Multi-turn Conversational AI from Text to Multimodal Interaction: Data, Models, Evaluation, and Open Challenges](http://arxiv.org/abs/2608.17605v1)
  <details><summary>📄 Abstract</summary>
  Conversational AI is moving beyond isolated text prompts toward sustained, multimodal interaction. In real conversations, users clarify goals, revise requests, interrupt responses, switch topics, and introduce new evidence while expecting systems to preserve context across turns. This makes multi-turn dialogue a distinct challenge requiring systems to maintain and update memory, ground responses across modalities, tools, and external knowledge, and adapt across languages and cultures. This study...
  </details>

- **2026-08-18** — Ruizhe Wang, Yixuan Dong, Bolin Yang et al. — [DMT-Dens: Density-preserving manifold visualization for biological data](http://arxiv.org/abs/2608.17571v1)
  <details><summary>📄 Abstract</summary>
  Motivation: Low-dimensional embeddings are widely used to explore cell-state heterogeneity in single-cell and other high-dimensional biological data. Although many methods preserve local neighborhoods, they may distort the apparent sampling density of processed observations, altering the visual contrast between dense and sparse regions and complicating the interpretation of rare, transitional, or continuous cell-state populations. Results: We present DMT-Dens, a parametric manifold-visualization...
  </details>

- **2026-08-18** — Ksenia Merzlyakova, Sebastian Padó, Franziska Weeber — [Effects of Answer Format Variation on Gender Bias in Large Language Models](http://arxiv.org/abs/2608.17516v1)
  <details><summary>📄 Abstract</summary>
  Gender bias or other social biases in large language models (LLMs) are frequently evaluated with question answering or survey benchmarks where the LLM needs to give a response in a predefined answer format. It is well known in survey science that the answer format has a substantial impact on answers, just as LLMs are sensitive to the prompt wording. However, to our knowledge it has not been studied yet how changes in answer format impact the measurement of gender bias in LLMs and their alignment...
  </details>

- **2026-08-18** — Hongyan Feng, Sunlai Chen, Xuanyu Liu et al. — [Embodied-Navigator: Point, Think, Memorize, and Align for Efficient Navigation](http://arxiv.org/abs/2608.17512v1)
  <details><summary>📄 Abstract</summary>
  Although Large Vision-Language Models (VLMs) have significantly advanced embodied navigation, their direct deployment remains challenging, as existing methods often force VLMs into unnatural action spaces that misalign with their 2D pre-training priors, compounded by rigid reasoning schedules and inefficient memory management. To overcome these limitations, we propose TAMP-Nav, a unified framework for efficient embodied navigation. First, we introduce a Pixel-to-3D Action Formulation (Point) tha...
  </details>

- **2026-08-18** — Feiyu Shen, Kun Xie, Yichen Wu et al. — [FireRedTTS3: Unified Speech Generation and Editing with Semantically Enriched Speech Representations](http://arxiv.org/abs/2608.17492v1)
  <details><summary>📄 Abstract</summary>
  Recent continuous autoregressive TTS models operate directly on continuous speech representations, preserving rich acoustic details while leveraging the instruction-following capabilities of text LLMs. This paradigm opens new possibilities for voice cloning, instruction-controlled voice design, and speech editing, but remains susceptible to error accumulation during autoregressive generation. Existing solutions often require additional semantic modules, multi-stage tokenizer training pipelines, ...
  </details>

- **2026-08-18** — Yibo Liu, Bowen Jiang — [When More Foundation Models Means Less: Diagnosing and Addressing Multi-View Fusion Failure](http://arxiv.org/abs/2608.17490v1)
  <details><summary>📄 Abstract</summary>
  Foundation-model hubs turn multi-view fusion into a selection problem: from a large heterogeneous encoder pool, which views should be fused, and how many? We show that downstream performance is non-monotonic in the number of fused encoders; later views can be redundant or task-misaligned, causing accuracy to saturate or decline. We formalise this setting as view-set composition and propose KAGES (Kernel-Alignment Greedy Encoder Selector), a label-aware method that orders frozen encoders by their...
  </details>

- **2026-08-18** —  AIMAE Team, Tianxiang Chen, Yan Cheng et al. — [Wuying-Browser-Agent: Real-World Centric Fundamental Long-Horizon Browser Agents](http://arxiv.org/abs/2608.17319v1)
  <details><summary>📄 Abstract</summary>
  Browser agents perform well on short, clean demonstrations, but real deployment is fundamentally different: agents must sustain dozens of decisions on live websites while recovering from mistakes and navigating complex UIs. We argue that closing this gap requires alignment at every level of the pipeline, including execution, supervision, optimization, and evaluation, rather than scale alone. We present Wuying-Browser-Agent, a unified framework that addresses each of these levels. A structured br...
  </details>

- **2026-08-17** — Xiutian Zhao, Luqi Sun, Björn Schuller et al. — [Emotion Across Speech and Faces: Shared Affective Mechanisms in Multimodal Foundation Models](http://arxiv.org/abs/2608.17102v1)
  <details><summary>📄 Abstract</summary>
  Modern multimodal foundation models (MFMs) have made rapid progress on tasks requiring integrated perception across speech, vision, and language, including emotion recognition. However, it remains unclear whether they recognize speech and facial emotion through shared affective functional units or modality-specific pathways. We explore emotion-sensitive neurons (ESNs), sparse decoder neurons selectively associated with emotion categories, in three MFMs: Gemma-4-12B-it, MiniCPM-o-4.5, and Qwen2.5...
  </details>

- **2026-08-17** — Kazuyuki Akitsu, Shi-Fan Chen, Zvonimir Vlah — [Intrinsic Alignments in Redshift Space I: Symmetries](http://arxiv.org/abs/2608.17078v1)
  <details><summary>📄 Abstract</summary>
  Galaxy shapes are unique tensor tracers of large-scale structure, providing a promising avenue to both enhance current cosmological programs and detect new physics beyond the scalar sector. We develop a general formalism to describe the full 3D structure of galaxy shapes and their statistics, including the breaking of isotropy by the line of sight and redshift space distortions. We constructively show that the redshift-space mapping generates a kinematic basis whose form factors are strictly pol...
  </details>

- **2026-08-17** — Mingyuan Li, Guangsheng Yu, Xu Wang et al. — [Cross-Model Memory Transfer via Target-Side Reader Adaptation](http://arxiv.org/abs/2608.17050v1)
  <details><summary>📄 Abstract</summary>
  Methods for improving knowledge use in large language models typically fall into two regimes. Non-parametric retrieval offers flexible access to external knowledge, but adds retrieval latency, context overhead, and only shallow integration with the backbone. Parametric adaptation is efficient at inference time, but entangles knowledge with model weights and can be hard to update, audit, or transfer. Engram-style hashed memory occupies a middle regime: it stores learned information in an external...
  </details>

- **2026-08-17** — Jiaqi Wang, Huawen Hu, Shu Zhang — [Margin-Regularized Structured Semantic Alignment for Brain-Language Correspondence](http://arxiv.org/abs/2608.16975v1)
  <details><summary>📄 Abstract</summary>
  With the rapid advancement of large language models, brain-language decoding has achieved remarkable progress. However, it remains unclear whether decoded content genuinely reflects neural representations or is largely reconstructed by the language model itself. This ambiguity limits interpretability and hinders the investigation of intrinsic brain-language correspondence. To address this challenge, we propose MD-SigLIP. This margin-regularized structured semantic alignment framework directly al...
  </details>

- **2026-08-17** — Harold Haodong Chen, Zhiyu Hou, Wen-Jie Shu et al. — [GenRouter: Unified Workflow Routing for Agentic Image Generation](http://arxiv.org/abs/2608.16721v1)
  <details><summary>📄 Abstract</summary>
  The rapid evolution of text-to-image (T2I) generation models has effectively solved the foundational challenge of raw pixel synthesis, shifting the community's focus toward fulfilling increasingly intricate user requests. While recent agentic image generation workflows enhance static inference with advanced capabilities like external knowledge retrieval and iterative reasoning, they mostly operate in isolated silos with fixed ``one-size-fits-all" topologies. This inevitably leads to severe compu...
  </details>

- **2026-08-17** — Thomas Mbrice, Ammar Ali, Sami Mian et al. — [The Ethical Decision Head: Operationalizing Normative Ethics in Autonomous Vehicles via Reinforcement Learning from Human Feedback](http://arxiv.org/abs/2608.16710v1)
  <details><summary>📄 Abstract</summary>
  As autonomous vehicles (AVs) approach Level 4 and Level 5 operational capability [SAE International, 2018], their on- board decision systems must handle not only safety-critical locomotion but also their subsequent moral weight. This paper details the Ethical Decision Head (EDH), a deep re- inforcement learning (RL) framework that encodes ethical reasoning as a differentiable reward signal, enabling a pol- icy gradient agent to learn morally-aligned driving behavior in scenarios whose state repr...
  </details>

- **2026-08-17** — Zi Haur Pang, Casey Kennington, Tatsuya Kawahara — [Closing the Affective Loop: Multimodal Speaker-Listener Emotion-Dynamics-Aware Empathetic Social Robots](http://arxiv.org/abs/2608.16686v1)
  <details><summary>📄 Abstract</summary>
  Empathetic social robots should respond not only to what users say, but also to how their emotions dynamically evolve during interaction. However, existing empathetic dialogue systems are often text-centered and primarily model empathy as a one-way mapping from the user's emotion to the system response, limiting their ability to capture embodied speaker--listener affective exchange. We present AffectLoop, a multimodal speaker-listener emotion-dynamics-aware spoken dialogue system implemented on ...
  </details>

- **2026-08-17** — Shanwen Wang, Xin Sun, Danfeng Hong et al. — [Bridging the Gap between Labeled and Unlabeled Data via Unified Flow with Feature Memory Bank](http://arxiv.org/abs/2608.16681v1)
  <details><summary>📄 Abstract</summary>
  Although semi-supervised semantic segmentation ($\text{S}^4$) utilizes abundant unlabeled data to reduce manual labeling burdens, independent training of labeled and unlabeled data causes the former to dominate, which severely degrades pseudo-label quality. To address this challenges, we propose a novel remote sensing (RS) $\text{S}^4$ method via unified flow with feature memory bank (UFFM). Specifically, UFFM comprises two key innovations: unified flow (UF) and feature memory bank (FMB). The UF...
  </details>

- **2026-08-17** — Mahdi Dhaini, Adam Dejl, Juraj Vladika et al. — [When Do Explanations Help In-Context Learning? A Comparative Study of Natural Language Explanation Types and Faithfulness](http://arxiv.org/abs/2608.16627v1)
  <details><summary>📄 Abstract</summary>
  Natural language explanations (NLEs) are increasingly used as inputs, for example, as few-shot rationales that influence model behavior in in-context learning (ICL). However, it remains unclear how different types of NLEs compare in their effects on downstream model performance in explanation-augmented prompting. Therefore, we provide a comparative evaluation across six benchmarks and four instruction-tuned models, studying how NLE source (human-written when available, self-generated explanation...
  </details>

- **2026-08-17** — Nils Lehmann, Jakob Gawlikowski, Burak Ekim et al. — [Beyond Accuracy: Assessing Calibration of Geospatial Foundation Models and Their Sensitivity to Distribution Shifts](http://arxiv.org/abs/2608.16614v1)
  <details><summary>📄 Abstract</summary>
  Geospatial Foundation Models (GeoFMs) are most commonly ranked and selected by accuracy on standard benchmark conditions via averaged ranks. We show that this protocol is too narrow: the promised deployment in critical EO tasks requires further angles of analysis, mainly calibration, the agreement between a model's confidence and its correctness. Across 16 frozen encoders, four classification and five segmentation datasets, and two orthogonal stress axes, every encoder degrades as corruption int...
  </details>

- **2026-08-17** — Yongqi Tong, Zhenyu Zhang, Ruirui Wang et al. — [STAGE: Controlled Objective Admission for Multi-Preference LLM Alignment](http://arxiv.org/abs/2608.16553v1)
  <details><summary>📄 Abstract</summary>
  Multi-preference alignment is often framed as scalarization: combine reward dimensions, then optimize. This leaves a temporal decision underspecified: when should each preference dimension enter policy optimization? We propose \methodname, a stability-guided active-set controller for controlled objective admission. \methodname starts from a small active set, retains admitted objectives, and expands when reward-deviation gates indicate low recent deviation or a patience budget is exhausted. A pro...
  </details>

- **2026-08-17** — Tony Alex, Wish Suharitdamrong, Sara Atito et al. — [Listen, Reason, and Segment: Aligning LALMs with Editorial Judgment for Media Chapterization](http://arxiv.org/abs/2608.16539v1)
  <details><summary>📄 Abstract</summary>
  Large Audio Language Models (LALMs) have made rapid progress on standardized benchmarks, yet their deployment in practical media workflows, curation, archival indexing, and content distribution remains largely unrealized. We identify automated audio chapterization, the task of segmenting continuous audio streams into thematically coherent chapters, as a demanding and commercially consequential setting that exposes this gap. Chapterization is challenging because boundaries are defined less by obj...
  </details>

- **2026-08-17** — David Moriña — [Bayesian epidemic alignment for causal evaluation of seasonal infectious-disease interventions](http://arxiv.org/abs/2608.16537v1)
  <details><summary>📄 Abstract</summary>
  Seasonal infectious-disease interventions are commonly evaluated with interrupted time-series or pre--post designs that align epidemics by calendar week. When epidemic onset, speed or peak timing differs between seasons, such comparisons confound a shift in epidemic phase with a change in disease burden. We propose a Bayesian causal count model in which season-specific affine transformations map calendar time to a latent epidemic clock, and intervention effects are estimated on that clock rather...
  </details>

- **2026-08-17** — Mohamed Amine Kerkouri, Marouane Tliba, Aladine Chetouani et al. — [Matched Outcomes, Divergent Gaze: How Foveated MLLMs Search Compared to Humans](http://arxiv.org/abs/2608.16514v1)
  <details><summary>📄 Abstract</summary>
  Human visual search is serial: the fovea must land on a candidate to confirm it, and those landings form a scanpath. Whether multimodal large language models (MLLMs), given the same foveated input, search as humans do bears on their use as models of human vision and on attention-alignment scores. We compare three general-purpose MLLMs with human eye-movement scanpaths on goal-directed search (COCO-Search18), driving each model fixation by fixation through an identical, human-matched foveated vie...
  </details>

- **2026-08-17** — Junhao Chen, Zheqi Lv, Keting Yin et al. — [MLLM-Guided Semantic Correction for Text-to-Video Generation](http://arxiv.org/abs/2608.16513v1)
  <details><summary>📄 Abstract</summary>
  Recent advances in diffusion models and Transformer architectures have led to significant progress in text-to-video generation. However, these models often suffer from semantic errors such as missing objects, incorrect attributes, or mismatched actions. Although some semantic correction methods perform optimization before sampling or refinement after sampling, how to detect and correct semantic deviations during the video generation process remains underexplored. In this paper, we introduce a tr...
  </details>

- **2026-08-17** — Burak Tamer, Wolfram Höpken, Zehui Wang — [POI Recommendation with LLM-Augmented Multi-Graph Learning and Contrastive Alignment](http://arxiv.org/abs/2608.16407v1)
  <details><summary>📄 Abstract</summary>
  Point-of-interest (POI) recommendation models based on graph neural networks achieve strong performance by propagating collaborative signals over user-item interactions, yet they struggle with the cold-start problem, where items with few or no interactions are not represented. In this paper, we propose LLM-augmented Multi-Graph Contrastive Learning (LLM-MGCL), a multi-graph neural network that uses semantic and spatial information about items to extend the LightGCN backbone with two auxiliary it...
  </details>

- **2026-08-17** — Yuchen Yuan, Zhenghuang Wu, Yuangan Li et al. — [AeroCopilotBench: A Two-Tier Benchmark for Evaluating LLM Agents as Aviation Copilots in an Interactive Virtual Cockpit Environment](http://arxiv.org/abs/2608.16349v1)
  <details><summary>📄 Abstract</summary>
  Large language model (LLM) agents may assist flight crews with complex decisions and task execution, but existing aviation evaluations centered on static knowledge do not support systematic testing of procedural execution and safety compliance in interactive environments. This paper presents the AeroCopilot Operational Environment (ACOE), a reproducible interactive virtual-cockpit test environment, and AeroCopilotBench, a two-tier aviation agent evaluation benchmark. Tier-1 evaluates aviation kn...
  </details>

- **2026-08-17** — Fernando Cardenas Piepereit — [Architecture-Dependent Causal Transfer of Activation States Across Large Language Models](http://arxiv.org/abs/2608.16347v1)
  <details><summary>📄 Abstract</summary>
  Direct communication between AI systems relies on natural language as an intermediate layer, incurring encoding/decoding overhead, token cost, and latency. We ask whether internal activation states can instead be transferred causally between different large language model (LLM) architectures via a learned projection, evaluated at three levels: representational similarity, cross-model retrieval from projected states, and end-to-end causal transfer via activation injection during generation. Using...
  </details>

- **2026-08-17** — Ruchen Liu, Yi Yang, Yiming Xu et al. — [Seeing Before Answering: Training-Free Visual Layer Profiling for Vision-Language Models](http://arxiv.org/abs/2608.16263v1)
  <details><summary>📄 Abstract</summary>
  LLaVA-style Vision-Language Models (VLMs) pass visual tokens from a fixed late layer of the vision backbone, typically the penultimate one, to the language model. We first show that this hidden convention is fragile: across 2 VLMs and 7 image and video benchmarks, the default layer is sub-optimal in 13 of 14 model-task pairs, and the best layer shifts with both task and visual backbone. Finding that layer by exhaustive layer-wise inference is prohibitively expensive, and no better fixed default ...
  </details>

- **2026-08-17** — Małgorzata Łazęcka, Ewa Szczurek — [The Trade-off Between Covariate Dependence and Latent Structure in Representation Learning](http://arxiv.org/abs/2608.16245v1)
  <details><summary>📄 Abstract</summary>
  Disentangled representation learning seeks latent representations whose indicidual dimensions each align with a distinct covariate. Unsupervised approaches typically target latent dimension independence, yet this gives no guarantee that the resulting dimensions align with semantically meaningful covariates. Supervised approaches structure the latent space using observed covariates, but under correlated covariates they cannot simultaneously control one-to-one latent-covariate alignment and latent...
  </details>

- **2026-08-17** — Shanshan Lin, Yuesheng Wu, Chao Chen et al. — [Multi-Granularity Sentiment Integration for LLM-Based Multimodal Sentiment Analysis](http://arxiv.org/abs/2608.16201v1)
  <details><summary>📄 Abstract</summary>
  Multimodal sentiment analysis (MSA) aims to predict sentiment polarity and intensity from heterogeneous inputs such as text, audio, and vision. While large language models (LLMs) offer strong semantic priors for MSA, effectively incorporating audio and visual signals effectively remains challenging. A key challenge is that audio and visual sentiment cues evolve over different temporal scales, yet many LLM-based methods compress these signals through shallow projection or coarse pooling before fu...
  </details>

- **2026-08-17** — Wengan He, Yongsheng Luo, Lihong Jiang et al. — [Protein Structure Prediction: From Evolutionary Constraints to Generative Modeling](http://arxiv.org/abs/2608.16094v1)
  <details><summary>📄 Abstract</summary>
  Accurate protein structure prediction is fundamental to structural biology because protein structure underlies molecular function and provides a basis for mechanistic interpretation. Recent advances in deep learning have transformed the field from multiple sequence alignment (MSA)-driven monomer folding into broader frameworks capable of modeling protein complexes and increasingly heterogeneous molecular systems. Existing reviews have summarized this progress from the perspectives of representat...
  </details>

- **2026-08-16** — Yubo Zhang, Yiyao Liu — [CM-MAE: A Physics-Guided Cross-Modal Self-Supervised Learning Framework for Vision-Wireless Applications](http://arxiv.org/abs/2608.15972v1)
  <details><summary>📄 Abstract</summary>
  Synchronized camera and wireless measurements observe the same scene through different physical channels. The central difficulty is that a representation learned in one deployment can fail when viewpoint, traffic, illumination, and propagation geometry change. This paper presents CM-MAE, a self-supervised vision--wireless pretraining framework for cross-scenario representation transfer. The evaluated real-data model uses only RGB frames and the measured 64-beam received-power vector available in...
  </details>

- **2026-08-16** — Ryota Kanai — [A Control-Theoretic Formulation of Global Workspace Theory](http://arxiv.org/abs/2608.15926v1)
  <details><summary>📄 Abstract</summary>
  Global workspace theory explains conscious access as the broadcasting of selected information to the rest of the network, but it lacks a formal criterion for identifying the mechanism that enables this access. We propose that a global workspace is a mediator, namely, a subnetwork that receives activity from distributed systems, transforms it through internal modes, and returns differentiated effects to the broader network. We formalize this claim as the Global Mediation Workspace (GMW), a contro...
  </details>

- **2026-08-16** — Fan Yang, Youngsun Wi, Jinhao Yu et al. — [Tactile Sim2Real without Tactile Simulation via Bottlenecked Latent Reconstruction](http://arxiv.org/abs/2608.15897v1)
  <details><summary>📄 Abstract</summary>
  Robot sensor designs, particularly tactile sensors, are highly diverse and evolve rapidly. Modeling each sensor in simulation demands substantial domain expertise and computational approximations can degrade the fidelity of the simulated signals. We propose Sim2Real via Bottlenecked Latent Reconstruction (SBLR), a framework that avoids sensor-specific simulation entirely by (1) training policies on a simulator-native oracle sensor that is easy to construct without modeling any particular sensor ...
  </details>

- **2026-08-16** —  GigaBrain Team, Angen Ye, Axiang Sun et al. — [GigaBrain-0.7: Scaling Embodied Foundation Models to Emergent Capabilities with a Three-System Architecture](http://arxiv.org/abs/2608.15875v1)
  <details><summary>📄 Abstract</summary>
  Vision-language-action (VLA) models have become a dominant paradigm for generalist embodied agents, demonstrating strong complex and long-horizon task completion in structured settings. Yet it remains an open question whether current VLA systems can benefit from more effective architectural design, scale to substantially larger and more heterogeneous data regimes, and achieve broader generalization across tasks and embodiments. To this end, we present GigaBrain-0.7, an embodied foundation model ...
  </details>

- **2026-08-16** — Everistus Ugochukwu Nwogo, Isibor Kennedy Ihianle, Pedro Machado et al. — [An AI-Based Adaptive Learning Platform for Multilingual and Low-Resource Educational Contexts: A Case Study on Nigeria](http://arxiv.org/abs/2608.15738v1)
  <details><summary>📄 Abstract</summary>
  Educational platforms in under-resourced and multilingual contexts, such as Nigeria, often struggle with limited personalisation, inadequate language support, and weak curriculum internationalisation, leading to reduced learner engagement and inclusivity. This paper presents an AI-based adaptive learning platform designed for multilingual and low-resource educational contexts, with a case study on Nigerian Pidgin English. The system integrates fine-tuned large language models (LLMs) within a per...
  </details>

- **2026-08-16** — Peng Chunyi, Xu Zhipeng, Yan Yukun et al. — [ConceptFormer: Learning Adaptive Latent Concepts for Query-Document Alignment in Visual Document Retrieval](http://arxiv.org/abs/2608.15698v1)
  <details><summary>📄 Abstract</summary>
  Visual document retrieval is a critical component of multimodal retrieval-augmented generation, aiming to identify query-relevant pages from document collections where evidence is distributed across text, layout, charts, and visual structures. Recent efforts toward finer-grained supervision primarily rely on textual descriptions or localized visual regions as evidence proxies. However, such supervision signals may either overlook complex visual structures or provide incomplete and inaccurate rep...
  </details>

- **2026-08-16** — Kareem Hassani, Chaymaa Abbas, Lama Mawlawi et al. — [THESIS-MoE: Trainable Hierarchical Extraction and SteerIng of Sycophancy in Mixture-of-Experts](http://arxiv.org/abs/2608.15687v1)
  <details><summary>📄 Abstract</summary>
  Sycophancy, the tendency of a language model to change its answer to match a user's stated belief, is a common alignment failure. Existing activation steering methods typically apply a single contrastive direction uniformly throughout the model, which is an unconditional intervention that alters activations even when no sycophantic behavior is present, trading knowledge retention for behavioral correction. In Mixture-of-Experts (MoE) models, prior work further suggests that behavior is encoded w...
  </details>

- **2026-08-16** — Mikhail Krasitskii, Alexander Gelbukh, Olga Kolesnikova et al. — [Why Summaries Turn Neutral: Policy Attribution for Sentiment Drift in Reinforcement Learning from Human Feedback](http://arxiv.org/abs/2608.15530v1)
  <details><summary>📄 Abstract</summary>
  Reinforcement learning with human feedback (RLHF) aligns LLMs with human preferences, improving summarization fluency and safety, but causes sentiment drift: overly neutral summaries stripped of emotional nuance. We diagnose why RL acts as a sentiment neutralizer and present Policy Attribution, a framework using gradient and logit decomposition to trace drift to reward model (RM) signals and KL (Kullback-Leibler) penalty. Sentiment drift reflects a strategic bias toward "low-risk" tokens maximiz...
  </details>

- **2026-08-16** — Shuo Lu, Weicheng Meng, Aijing Yu et al. — [Topological collapse of higher-order interactions bottlenecks collective intelligence in AI agent societies](http://arxiv.org/abs/2608.15519v1)
  <details><summary>📄 Abstract</summary>
  Current paradigms in artificial intelligence concentrate on scaling the capabilities of individual models, yet the collective behaviour of interacting agents is shaped by the topology of their interactions rather than by individual cognition alone. Here we show that the binding constraint on collective behaviour in agent societies is topological. Analysing a macroscopic AI social platform of 1.6 million registered agents (174,458 active in the interaction record), we identify a phenomenon we ter...
  </details>

- **2026-08-16** — Aditya Singh — [Not All Attention Is Equal: A Quantitative Survey of the EEI Trade-off](http://arxiv.org/abs/2608.15459v1)
  <details><summary>📄 Abstract</summary>
  Attention mechanisms have driven machine learning for a decade, from neural machine translation to language models that do general-purpose reasoning. This survey covers four connected threads: their formulation for sequence-to-sequence tasks, adaptation to computer vision, efficiency innovations that address the quadratic bottleneck, and advances in interpretability. We define three criteria: efficiency, expressiveness, and interpretability, and compare twenty-one methods using an EEI scoring fr...
  </details>

- **2026-08-16** — Md Aminur Hossain, Omkumar Vaghasiya, Rajeev Ranjan Dwivedi et al. — [AlignJEPA: Predictive Vision-Language Alignment for Remote Sensing Foundation Models](http://arxiv.org/abs/2608.15456v1)
  <details><summary>📄 Abstract</summary>
  Remote sensing (RS) foundation models provide transferable Earth observation representations across sensors, resolutions, and geographies, yet most remain weakly aligned with natural language, limiting natural-language archive search, image-text retrieval, and question-conditioned analysis. We propose AlignJEPA, a JEPA-inspired predictive vision-language alignment framework for remote sensing foundation models. AlignJEPA uses a pretrained AnySat visual encoder and a RemoteCLIP text encoder while...
  </details>

- **2026-08-16** — Ishika Agarwal, Arkajyoti Charaborty, Tanner Sorensen et al. — [LLMs Get Smarter from Targeted Synthetic Multilingual Data](http://arxiv.org/abs/2608.15964v1)
  <details><summary>📄 Abstract</summary>
  Language-specific competency (LSC) is the phenomenon of a language model performing better or worse depending on the language of the prompt. In other words, a language model outputs different (and potentially incorrect) responses to the same semantic query when prompted in different languages. Prior work attributes this to an internal misalignment of semantic representation across languages. Currently, there are two main approaches to address LSC in the literature: (1) routing all queries throug...
  </details>

- **2026-08-15** — Steve Hanneke, Hongao Wang, Mingyue Xu — [Towards a theory of inference-time alignment with unknown rewards](http://arxiv.org/abs/2608.15402v1)
  <details><summary>📄 Abstract</summary>
  Generative model alignment has received broad interest, and significant progress has been made in supervised fine-tuning and inference-time computation. Yet, alignment has remained poorly understood from a statistical learning perspective. We formulate inference-time alignment as a weak-to-strong learning problem, where a reference policy (weak learner) is assumed to be fairly good and the goal is to produce a strong learner that predicts a good response at test time with arbitrarily high probab...
  </details>

- **2026-08-15** — Catherine Bao, Vivek Srikumar — [The Machine's Internal Clock: Do LLMs Share Human Temporal Illusions?](http://arxiv.org/abs/2608.15394v1)
  <details><summary>📄 Abstract</summary>
  Human perception of time is subjective. Well-documented temporal illusions show that the brain relies on context and relational cues for judging duration instead of tracking elapsed time directly. Prior studies established these effects with visual and auditory stimuli. Existing LLM evaluations of temporal perception focus on estimating event durations or multi-step temporal reasoning. In this work, we investigate whether written narratives alone can evoke human temporal illusions, using a new b...
  </details>

- **2026-08-15** — Pegah Nokhiz, Aravinda Kanchana Ruwanpathirana, Helen Nissenbaum — [Incoherent by Design? On the Moral Self-Consistency of LLMs](http://arxiv.org/abs/2608.15354v1)
  <details><summary>📄 Abstract</summary>
  LLMs are increasingly used in morally sensitive contexts, yet it is unclear whether they apply ethical principles consistently across situations. A model that can state a moral principle may still violate it when the same scenario is rephrased or reframed. This inconsistency is a problem for any system whose outputs are used to inform moral decisions. If generative systems exhibit internal inconsistency, then the epistemic integrity of AI-mediated systems becomes uncertain. To study this concern...
  </details>

- **2026-08-15** — Sijing Wu, Yunhao Li, Zhilin Gao et al. — [FMReward: Aligning and Evaluating Audio-Driven 3D Facial Animation with Human Preferences](http://arxiv.org/abs/2608.15296v1)
  <details><summary>📄 Abstract</summary>
  Audio-driven 3D facial animation is essential for advancing immersion and interactivity in virtual experiences. Although recent advances have shown promising capabilities, the training and evaluation of existing methods typically rely on ground-truth-based errors, which fall short of aligning with human preferences. To address this, we present a comprehensive framework that learns an automatic perceptual model from human preference data and leverages it to improve and evaluate the perceptual qua...
  </details>

- **2026-08-15** — San Jiang, Hui Wang, Xing Zhang et al. — [Robust structure from motion for aerial-ground images via detector-free feature matching and multi-view track refinement](http://arxiv.org/abs/2608.15251v1)
  <details><summary>📄 Abstract</summary>
  Integrated 3D reconstruction from aerial-ground images is essential for generating high-precision urban 3D models, yet severe variations in viewpoint, scale, and rotation make robust feature matching highly challenging. To address these limitations, this study introduces a rotation-robust detector-free matching network coupled with multi-view track refinement for incremental Structure from Motion (ISfM). The proposed workflow features four key modules. First, rotation-aware feature extraction re...
  </details>

- **2026-08-15** — Kaitao Yan, Chi Liu, Congcong Zhu et al. — [From "What-If" to "What-Is": Counterfactual Thinking-Inspired Semantic Alignment for Visual Brain Decoding](http://arxiv.org/abs/2608.15163v1)
  <details><summary>📄 Abstract</summary>
  Visual brain decoding reconstructs visual content perceived by a person from neural measurements such as fMRI, providing a computational approach to studying how visual information is represented in the brain. Recent multimodal representations and diffusion priors have improved reconstruction realism. However, visually plausible reconstructions may contain incorrect objects, attributes, or relations because a strong generative prior can complete content not sufficiently specified by the decoded ...
  </details>

- **2026-08-15** — Yihang Du, Juhao Liang, Zhengzhao Lai et al. — [Why Vision Fails as a Universal Bridge: Rectifying Modality Asynchrony in Multilingual MLLMs](http://arxiv.org/abs/2608.15085v1)
  <details><summary>📄 Abstract</summary>
  Multimodal large language models (MLLMs) exhibit substantial performance degradation in non-English visual reasoning, despite the strong multilingual competence of their text-only backbones. While mechanistic evidence from text-only models suggests that non-English inputs are routed through an English-centric latent space, the multimodal implications of this phenomenon remain unexplored. Through rigorous mechanistic analysis, we identify the \textbf{Ghost Anchor} phenomenon: a temporal modality ...
  </details>

- **2026-08-14** — Taenyun Kim, Edyta Bogucka, Daniele Quercia — [Participatory Moral AI Is Not Neutral: The Invisible Hand of Developers](http://arxiv.org/abs/2608.14522v1)
  <details><summary>📄 Abstract</summary>
  As AI systems make more morally loaded decisions across society, one response has been moral preference elicitation. In this approach, researchers poll participants on hypothetical dilemmas and use the aggregated votes to train a policy that an AI model then applies at scale. Before any vote is cast, developers make three key choices in the moral AI elicitation pipeline: feature scoping, voter sampling, and question framing. In other words, they decide which features go to a vote, which voters t...
  </details>


### 📂 robustness
*鲁棒性与可靠性 / Robustness & Reliability* — 56 papers

- **2026-08-18** — Deep Kumar Ganguly, Jan Kretinsky — [Quantifying Risk Under Evolving Uncertainty: Belief-Dependent Robustness for Safe Sequential Decision Making](http://arxiv.org/abs/2608.17574v1)
  <details><summary>📄 Abstract</summary>
  How cautious should an agent be while it is still learning its environment? We propose RATTL (Risk-Adversarial Total-Reward Learning), which ties caution to epistemic uncertainty: the agent holds a Bayesian posterior over unknown dynamics and plans against a Wasserstein ambiguity set whose radius is a monotone function of that posterior. The radius contracts with evidence, so behaviour interpolates continuously between worst-case robustness and risk-neutral total-reward maximization. The design ...
  </details>

- **2026-08-18** — Fangling Jiang, Qi Li, Bing Liu et al. — [Primitive-Driven Compositional Forensic Visual Prompting for Open-World Face Anti-Spoofing](http://arxiv.org/abs/2608.17351v1)
  <details><summary>📄 Abstract</summary>
  Open-world face anti-spoofing must address both covariate and semantic shifts: source and target domains differ in imaging conditions, while target domains contain diverse attack types absent from training. Existing prompt-based approaches often express spoofing through category semantics or language guidance, which is effective for modeling high-level concepts but is less suited to explicitly capturing the evolving fine-grained and spatially heterogeneous forensic evidence of unseen attacks. Mo...
  </details>

- **2026-08-18** — Ingrid navarro, Pablo Ortega-Kral, Yutong Duan et al. — [ControlledShifts: Towards Standardizing Robustness Evaluation in Trajectory Prediction Under Distribution Shifts](http://arxiv.org/abs/2608.17882v1)
  <details><summary>📄 Abstract</summary>
  Trajectory prediction is central to safety in autonomous driving, yet learning-based predictors tend to degrade sharply when encountering scenarios poorly represented by their training data. Many methods attempt to mitigate distribution shift degradation through data-centric or test-time adaptation approaches; however, they are typically validated along fragmented axes of generalization, leaving the field without a standardized way to compare robustness across shifts a model may encounter.   To ...
  </details>

- **2026-08-18** — Yiyan Peng, Philip Wang, Simon Sinong Zhan et al. — [MANIGUARD: A Benchmark and Data Suite for Specification-Grounded Safety Evaluation and Improvement of Robotic Manipulation](http://arxiv.org/abs/2608.17386v1)
  <details><summary>📄 Abstract</summary>
  Foundation-model policies for robotic manipulation are advancing rapidly on task success, but rigorous evaluation of whether they succeed safely is still lacking. We introduce ManiGuard, a specification-grounded framework for evaluating and improving the safety of foundation-model manipulation, comprising the ManiGuard-Bench task suite and a paired safety-annotated trajectory-generation pipeline. ManiGuard-Bench organizes six contact-rich household task families into 200 locked base tasks along ...
  </details>

- **2026-08-18** — Rui-Huan Wang, Si-Tong Wei, Jia-Qi He et al. — [aDSL: Agentic 3D Creation via Joint Agent-Program Design](http://arxiv.org/abs/2608.17975v1)
  <details><summary>📄 Abstract</summary>
  Programmatic representations provide a compelling paradigm for 3D content creation, enabling fine-grained edits, interpretability, and explicit structural control. Yet, agentic workflows that rely on large language models (LLMs) to author 3D programs remain brittle, often failing to translate high-level intent into consistent low-level geometry. We attribute this fragility to a mismatch between existing programmatic interfaces and the reasoning strengths of LLMs, which favor semantic structure a...
  </details>

- **2026-08-18** — Muhammad A. Muttaqien, Tomohiro Motoda, Ryo Hanai et al. — [ORPA: Online Residual Policy Adaptation for Robot Manipulation Control with Human Feedback](http://arxiv.org/abs/2608.17323v1)
  <details><summary>📄 Abstract</summary>
  Robotic manipulation policies trained via imitation learning, such as Action Chunking with Transformers (ACT), can achieve strong performance under ideal conditions but often remain sensitive to small execution errors and distribution shifts. Correcting these failures typically requires dataset aggregation and full-policy retraining, which is computationally expensive and unsuitable for real-time deployment. In this work, we propose Online Residual Policy Adaptation (ORPA), a framework that enab...
  </details>

- **2026-08-18** — Haoqin Tu, Yunhao Fang, Yizhong Wang et al. — [Chain-of-Experience for Continual LLM Improvement](http://arxiv.org/abs/2608.18027v1)
  <details><summary>📄 Abstract</summary>
  Humans continuously learn from experience, whereas conventional large language model (LLM) evaluations ignore the models' ability to improve through inference-time interaction. In this paper, we study how LLMs learn from iterative experience at test time, a setting we refer to as Chain-of-Experience (CoE), where models accumulate experiential traces through iterative interactions with self or environmental feedback to form a continual improvement loop beyond zero-shot inference. We instantiate C...
  </details>

- **2026-08-18** — Jhen-Ke Lin — [Grading Needs a Rubric, Not Intelligence](http://arxiv.org/abs/2608.17938v1)
  <details><summary>📄 Abstract</summary>
  Small language models can grade open-ended examination answers as reliably as substantially more expensive models when they grade against an explicit rubric. We test this claim as the design principle behind any-to-bench: a frontier model reads source documents once, at ingestion, to extract each question and its rubric; lower-cost models then perform all repeated grading work. We evaluate six cost-efficient model configurations from two model families at three reasoning-effort levels. Each conf...
  </details>

- **2026-08-18** — Geon Tack Lee, Jaegul Choo, Kang Eun Jeon — [Denoised Variance-Based Pruning with Optimal Brain Bias Compensation](http://arxiv.org/abs/2608.17657v1)
  <details><summary>📄 Abstract</summary>
  Vision Transformers (ViTs) achieve state-of-the-art performance but carry massive computational overhead that restricts edge deployment. Although structural pruning has emerged as a key strategy to reduce these costs, existing methods often suffer from severe accuracy degradation or require expensive retraining. Recently, Variance-Based Pruning (VBP) introduced a promising paradigm by selecting neurons based on activation variance; however, it remains limited by statistical noise in finite-sampl...
  </details>

- **2026-08-18** — Henrik Wille, Luis-Finley Schütz, Felix Strieth-Kalthoff — [Domain-Adapted Molecular Language Models for Efficient Search of Make-on-Demand Libraries](http://arxiv.org/abs/2608.17567v1)
  <details><summary>📄 Abstract</summary>
  Pretrained molecular language models are increasingly used as molecular encoders for learning structure-property relationships. However, their practical suitability for molecular discovery within and beyond their pretraining domain remains unclear. Herein, we systematically benchmark four molecular language models across six virtual molecular libraries spanning drug discovery, organic materials, and catalysis. Native molecular language model embeddings show substantial variation in discovery per...
  </details>

- **2026-08-18** — George Webster — [Mutual Recognition in the Philosophy of Physics: QBism, Phenomenology, Hegel](http://arxiv.org/abs/2608.17472v1)
  <details><summary>📄 Abstract</summary>
  Recent discussions of QBism have turned increasingly toward the question of its ontology. I argue that key insights into QBism's ontology of agency can be identified by reconstructing its response to Wigner's friend paradox. I clarify the relation between two formulations of that response: one grounded in the claim that quantum states are agents' personal probability assignments, and another grounded in the injunction to treat all users of quantum theory as agents on equal footing. Once disambig...
  </details>

- **2026-08-18** — Haomin Wen, Ziyu Zhou, Qingxiang Liu et al. — [LiveHouse-TS: An Open-world Living Benchmark for Time Series Foundation Models](http://arxiv.org/abs/2608.17299v1)
  <details><summary>📄 Abstract</summary>
  Time Series Foundation Models (TSFMs) have recently emerged as a highly promising paradigm for cross-domain zero-shot forecasting. However, existing evaluation protocols predominantly rely on static benchmarks with fixed historical test windows. While these benchmarks provide a valuable baseline snapshot, they evaluate an average performance on a fixed history, failing to capture how models behave in continuously evolving real-world environments characterized by seasonal variations, distribution...
  </details>

- **2026-08-18** — Kyle Chickering, Wei-An Lin, Swayam Bhanded et al. — [Abra: Scaling Diffusion Image Training](http://arxiv.org/abs/2608.17286v1)
  <details><summary>📄 Abstract</summary>
  Compute-optimal scaling laws guide the training of frontier language models yet remain largely unexplored for visual generation. We present a systematic scaling law study for text-to-image diffusion models using Abra, a controlled family of flow-matching transformers trained across three orders of magnitude worth of compute ($10^{19}$ to $10^{22}$ FLOPs), reaching significantly larger compute budgets than previous works. We demonstrate that diffusion models scale just as predictably as language ...
  </details>

- **2026-08-17** — John Tribbia — [Identifying Model Quality Effects on User Engagement: A Within-Version Causal Estimator with Synthetic Data Validation](http://arxiv.org/abs/2608.17187v1)
  <details><summary>📄 Abstract</summary>
  Every team building Large Language Models (LLMs) faces a core challenge: offline benchmarks show performance gains and user engagement rises post deployment, but isolating cause from effect remains difficult. Simultaneous marketing, media coverage, and seasonal demand obscure whether model updates truly drive engagement gains.   This paper presents a novel causal estimation approach that leverages non uniform quality improvements across capabilities within a single model version. Because capabil...
  </details>

- **2026-08-17** — Mason Smetana, Trevor Neece, Lev Khazanovich — [AISA: AI Safety Assistant Framework for Continuous Improvement of Highway Construction](http://arxiv.org/abs/2608.17184v1)
  <details><summary>📄 Abstract</summary>
  Job Safety Analysis (JSA) and pre-task planning can benefit from prior incident records, yet historical accident data is often stored as unstructured narratives that are difficult to consult at the point of planning. A novel framework centered on large language models (LLMs) for highway construction safety reporting and planning is proposed as a foundation for future agentic applications, prioritizing deterministic, local inferencing. The first aim is to enable classification and quality scoring...
  </details>

- **2026-08-17** — Abderrahmene Boudiaf, Irfan Hussain, Sajid Javed — [Uncertainty-Aware Decision Making in Multimodal Large Language Models](http://arxiv.org/abs/2608.17084v1)
  <details><summary>📄 Abstract</summary>
  Multimodal large language models (MLLMs) increasingly answer questions whose correctness depends on visual, textual, temporal, acoustic, document, chart, or embodied evidence. Their failures are therefore not only linguistic. A fluent answer may conceal poor input quality, a perceptual error, weak grounding, conflict between modalities, unstable reasoning, distribution shift, or a question that is not answerable from the supplied evidence. This survey organizes the literature on uncertainty-awar...
  </details>

- **2026-08-17** — Mihaela Ifrim, Ryan Martinez, Daniel Tataru — [Global solutions for 1D cubic defocusing dispersive equations, Part V: low regularity NLS](http://arxiv.org/abs/2608.17156v1)
  <details><summary>📄 Abstract</summary>
  This article is motivated by a broad conjecture, formulated by the first and last authors in earlier work, asserting that one-dimensional cubic defocusing dispersive flows with small initial data have global, dispersive solutions. The conjecture was first established for a class of semilinear Schrödinger-type models at $L^2$ regularity, the classical cubic NLS among them. In a complementary direction, Harrop-Griffiths, Killip and Vişan have recently shown, using the completely integrable structu...
  </details>

- **2026-08-17** — Alena Rottensteiner, Sebastian Ratzenböck, João Alves et al. — [A comprehensive cluster census of Orion. An application of the Significance Mode Analysis (SigMA) algorithm](http://arxiv.org/abs/2608.16989v1)
  <details><summary>📄 Abstract</summary>
  Precise astrometric surveys and modern clustering algorithms are working in step to transform our view of star-forming regions. By revealing a much richer substructure than previously accessible, they pave the way for reconstructing star formation histories by accurately resolving and age-dating individual sub-populations. The Orion star-forming complex is the best-studied stellar nursery in the solar neighborhood and the nearest one currently forming massive stars. Even so, a comprehensive char...
  </details>

- **2026-08-17** — Lingchen Sun, Rongyuan Wu, Xiangtao Kong et al. — [PixRestore: Unified Image Restoration via Pixel Diffusion Transformer](http://arxiv.org/abs/2608.16793v1)
  <details><summary>📄 Abstract</summary>
  Unified image restoration (UIR) aims to recover high-quality (HQ) content from low-quality (LQ) images with different degradations using a single model. Most recent methods adapt large pretrained text-to-image (T2I) latent diffusion models for their strong capacity and generative priors. However, the variational autoencoder (VAE) in latent T2I models may discard restoration-sensitive details, while the open-ended synthesis prior can introduce content-inconsistent artifacts. We present PixRestore...
  </details>

- **2026-08-17** — Hui Mao — [Historical Backtesting for Scientific Question Discovery: A Protocol and Astronomy Pilot](http://arxiv.org/abs/2608.16795v1)
  <details><summary>📄 Abstract</summary>
  Systems that generate scientific research questions are evaluated today by expert scores, LLM-as-judge ratings, or curated case studies -- all subjective, none falsifiable. We formalize historical backtesting as an alternative: a system generates questions from a corpus frozen at a historical cutoff, the questions are frozen before any access to later literature, and a temporally isolated future corpus then determines whether each question was subsequently answered, partially addressed, independ...
  </details>

- **2026-08-17** — Reza Fayyazi, Michael Zuzak, Shanchieh Jay Yang — [Topological Attribution Distance (TAD): Revealing Segment-Level RAG Influence on LLM Output Geometry for Incident Log Analysis](http://arxiv.org/abs/2608.16775v1)
  <details><summary>📄 Abstract</summary>
  Large Language Models (LLMs) are increasingly being deployed in cybersecurity operations to assist cybersecurity analysts with rapid decision-making against emerging threats. However, there is a main criteria that must be met when using LLMs in cybersecurity, that is, trust in the generated outputs. As Agentic AI is integrated into operational systems, a robust evidence attribution and provenance tracking technique is essential to trace the origins of model generations. When autonomous agents ma...
  </details>

- **2026-08-17** — Jiaqi Yao, Julia Kowal — [Degradation-Aligned Self-Supervised Learning for State of Health Estimation of Lithium-Ion Batteries under Label Sparsity](http://arxiv.org/abs/2608.16612v1)
  <details><summary>📄 Abstract</summary>
  An accurate estimation of the state of health (SOH) underpins a safe and optimized use of the battery system. Although compelling, data-driven SOH estimation models typically require large amounts of high-quality labeled cycling data, while in practice such labels are often sparse in both quantity and coverage. Therefore, in this work, we propose a degradation-aligned self-supervised learning (SSL) framework based on a convolutional neural network-gated recurrent unit (CNN-GRU) model, which lear...
  </details>

- **2026-08-17** — Kazuki Nakajima, Yuya Sasaki, Masaki Aida — [Declining Modularity of Intellectual Bases During the Emergence of Research Areas](http://arxiv.org/abs/2608.16602v1)
  <details><summary>📄 Abstract</summary>
  Understanding how research areas emerge can help identify nascent areas early and inform research strategy, yet how the intellectual base of a field restructures as an area takes shape remains unclear. We hypothesize that the emergence of a research area is accompanied by the integration of largely separate knowledge communities, observable as a decline in the modularity of its co-citation network, which represents its intellectual base. We propose a framework that tracks this modularity over ti...
  </details>

- **2026-08-17** — Yintong Huo, Rangeet Pan, Abhik Roychoudhury — [Towards Risk-free AI Agent Deployment](http://arxiv.org/abs/2608.16411v1)
  <details><summary>📄 Abstract</summary>
  LLM-based agents are rapidly moving from research prototypes into the core business processes of organizations, but these agents pose deployment risks to security, compliance, and functionality. In this article, we argue that risk-free deployment must be grounded in the agent's trajectory: the recorded sequence of reasoning steps, tool invocations, and environmental observations. Trajectories are available for any agent, and many failures are visible only in the trajectory. To make agents deploy...
  </details>

- **2026-08-17** — Bhaskar Tripathi, Anurag Kumar, Ramendra Kumar et al. — [A Policy Algebra for Trust-Preserving Agentic AI Execution](http://arxiv.org/abs/2608.16402v1)
  <details><summary>📄 Abstract</summary>
  Large language model-based agentic frameworks primarily optimize capability: whether an agent can reason, retrieve information, call tools, delegate work, and complete a goal. Enterprise execution requires a stronger property. A successful result is not reliable if it was produced through unauthorized data access, widened delegated authority, unapproved side effects, unrecoverable budget consumption, or incomplete evidence. This paper defines reliable capability as a path property: an agent is r...
  </details>

- **2026-08-17** — Vahid Zolfaghari, Nenad Petrovic, AndrÉ Schamschurko et al. — [Think Inside the Chunk: RegulaRAG for Regulation-Compliant Scenario Generation using LLMs: A Case Study of UN Regulation No. 152](http://arxiv.org/abs/2608.16394v1)
  <details><summary>📄 Abstract</summary>
  Generating regulation-compliant test scenarios is essential for validating safety-critical automotive systems, yet Large Language Models (LLMs) struggle to ground outputs in long, hierarchical standards. We present RegulaRAG, a Retrieval-Augmented Generation (RAG) pipeline that couples SmartChunking, reference-aware enrichment of paragraphs and tables via graph traversal, with Smart Retrieve & Rerank over these enriched units. To test our system, we evaluate on a manually curated dataset coverin...
  </details>

- **2026-08-17** — Mint-Agent Team, B. Zhang, Yaze Geng et al. — [Mint-Agent: Introducing Finance-Native Agentic Foundation Models](http://arxiv.org/abs/2608.16386v1)
  <details><summary>📄 Abstract</summary>
  Financial agents must do more than recall domain knowledge: they must be both reliable, executing precise operations over grounded evidence, and executive, sustaining long-horizon research whose conclusions remain auditable. We present Mint-Agent, a family of finance-native agentic models designed around these two scales of financial intelligence. Mint-Agent is built upon three pillars: data, harness, and algorithm. Our data engine constructs clean, specialized tasks for atomic financial capabil...
  </details>

- **2026-08-17** — Qijin She, Hanyang Yu, Zeming Li et al. — [MatchingPolicy: Correspondence-Aware Policy Enables Cross-Object In-Context Learning](http://arxiv.org/abs/2608.16715v1)
  <details><summary>📄 Abstract</summary>
  In-context imitation learning enables few-shot policy generalization but struggles to maintain performance on unseen objects and novel scenarios. To address this, we introduce MatchingPolicy, a correspondence-driven framework that explicitly decouples demonstration-to-scene matching from policy learning. Central to our method is a correspondence-aware diffusion policy that conditions robotic actions directly on dense semantic correspondences. This architectural separation resolves the inherent c...
  </details>

- **2026-08-17** — Ruoqi Shu, Xuhui Wang, Isaac Wang et al. — [LAVA: Logic-Aware Validation and Augmentation Framework for Large-Scale Financial Document Auditing](http://arxiv.org/abs/2608.16763v1)
  <details><summary>📄 Abstract</summary>
  Financial document validation in production, such as payroll auditing, tax compliance, and loan underwriting, demands exceptional accuracy, consistency, and reproducibility under strict enterprise constraints. In practice, documents arrive with heterogeneous layouts and formats, semantically rich and context-dependent content, and embedded business rules that current pipelines struggle to process reliably. We introduce LAVA (Logic-Aware Validation and Augmentation), a modular, backbone-agnostic ...
  </details>

- **2026-08-17** — Adam Karvonen, Euan Ong, Subhash Kantamneni et al. — [Would this change your answer? Evaluating Explanations of LLM Behavior In The Wild with Counterfactual Experiments](http://arxiv.org/abs/2608.16747v1)
  <details><summary>📄 Abstract</summary>
  Many areas of AI research, such as language model interpretability and chain of thought faithfulness, seek to explain model behaviors. But what constitutes a "good" explanation? In this work, we evaluate explanations through the lens of counterfactual simulatability-whether the explanation is useful for predicting model behaviors on related counterfactual inputs. To this end, we introduce CHIVE (Counterfactual Hypothesis Investigation Via Edits), a novel agentic pipeline that identifies unexpect...
  </details>

- **2026-08-17** — Yi Ai — [Bounded Semantic Planning and Deterministic Compilation for Reliable Enterprise Text-to-SQL](http://arxiv.org/abs/2608.16663v1)
  <details><summary>📄 Abstract</summary>
  Direct text-to-SQL asks a language model to do two jobs: interpret the business question and construct the complete relational query. In enterprise schemas, SQL can execute successfully while using the wrong relationship role or aggregation grain. We study an alternative placement of the stochastic boundary. A multi-turn planner grounds phrases and selects from question-specific governed options; graph traversal, role predicates, grain lowering, SQL construction, and deterministic checks are imp...
  </details>

- **2026-08-17** — Davood Marripour, Saeed S. Jahromi, Jahanfar Abouie — [Scarred discrete time crystal in a periodically driven dimerized spin chain](http://arxiv.org/abs/2608.16616v1)
  <details><summary>📄 Abstract</summary>
  We investigate the emergence of a scarred discrete time crystal (SDTC) phase in a periodically driven dimerized spin chain. While generic interacting Floquet systems are expected to thermalize according to the eigenstate thermalization hypothesis (ETH), we demonstrate that this system hosts quantum many-body scars (QMBS) that induce a regime of weak ergodicity breaking. Through an analysis of Floquet level statistics, entanglement entropy, and eigenstate fidelity, we identify a manifold of low-e...
  </details>

- **2026-08-17** — Zihan Zhao — [Social Learning with Selective Sampling](http://arxiv.org/abs/2608.16599v1)
  <details><summary>📄 Abstract</summary>
  This paper studies how robust social learning is when sampling is selective, i.e., some types of actions are more likely to be sampled by successors. We show that Bayesian agents can achieve asymptotic learning despite non-expanding observations, because the endogenous observation network itself carries information and agents have ways to undo the selection bias.
  </details>

- **2026-08-17** — Simranjit Singh, Jaswant Sharma, Jigar M. Pandya — [Development of Different Algorithms for Drone-Based Antenna Measurement Systems and Near-Field Error Analysis](http://arxiv.org/abs/2608.16518v1)
  <details><summary>📄 Abstract</summary>
  Near-field antenna measurements underpin the characterization of electrically large apertures, yet the fidelity of the Near-Field to Far-Field (NF-FF) transformation depends on the reconstruction algorithm's assumptions and robustness to real-world imperfections, including those from drone-based scanning platforms.   Classical FFT-based modal expansion is efficient on uniformly sampled canonical grids but fails when phase-coherent acquisition cannot be maintained. We address this via a phaseless...
  </details>

- **2026-08-17** — Yiqi Liu, Joseph James, Yang Wang et al. — [When Tool-Backed Skill Retrieval Fails: Source-Style Collapse in Executable Capability Retrieval](http://arxiv.org/abs/2608.16502v1)
  <details><summary>📄 Abstract</summary>
  Large-scale agents increasingly rely on retrieval to access external capabilities. We study this retrieval gate in structured tools and APIs, a measurable class of tool-backed executable skills that must be surfaced before an agent can plan, incorporate, or act. In this setting the retrieval layer can silently fail even when the capability corpus is fixed: on ToolRet, a retriever fine-tuned on one source-specific slice collapses on another source-specific slice of the same benchmark, with FT-110...
  </details>

- **2026-08-17** — Dongbin Jiao, Xianyi Wang, Yuchen Yuan et al. — [KC-BFPRL: Knowledge-Guided Multi-UAV Collaboration for Grassland Restoration via Bilevel Formerpointer-Based Reinforcement Learning](http://arxiv.org/abs/2608.16326v1)
  <details><summary>📄 Abstract</summary>
  Multi-unmanned aerial vehicle (UAV) systems provide scalable service platforms for large-scale environmental tasks, such as grassland ecosystem restoration. However, coordinating fleet operations requires solving the restoration area maximization problem (RAMP). This non-linear combinatorial optimization challenge is complicated by payload-dependent energy dynamics and heterogeneous ecological degradation. We propose a novel knowledge-guided collaborative bilevel formerpointer reinforcement lear...
  </details>

- **2026-08-17** — Seung-Won Seo, Won Ik Cho, Yongmin Yoo — [Domain-Agnostic Neural Topic Modeling with Contextual Token-Level Semantic Graph Representation](http://arxiv.org/abs/2608.16269v1)
  <details><summary>📄 Abstract</summary>
  Recent advances in neural topic models with pre-trained language models (PLMs) have achieved strong performance by leveraging general-domain pre-training, yet their topic interpretability often degrades on specialized corpora. This limitation primarily stems from the geometry of the embedding space, where domain-specific terms unseen during pre-training collapse into an indistinguishable region, and neither domain-specific re-training, word-level graph enrichment, nor parameter-efficient fine-tu...
  </details>

- **2026-08-17** — Pengbin Feng, Chunlei Meng, Daozheng Qu et al. — [Second-Order Response Laws for LLM Judges: Debiased Estimation of Prompt Instability](http://arxiv.org/abs/2608.16253v1)
  <details><summary>📄 Abstract</summary>
  LLM judges are often evaluated with a single prompt and only a few repeated calls. When their verdicts vary, it remains unclear whether the variation comes from sampling noise within a prompt or systematic differences across prompts. We formalize this distinction using a second-order response law: the distribution of prompt-conditioned verdict distributions induced by a declared prompt policy. For a quadratic measure of prompt instability, we show that the usual plug-in estimator is biased upwar...
  </details>

- **2026-08-17** — Chen-An Li, Hung-yi Lee — [INSPIRE: A Benchmark for Instruction-Aware Speech Retrieval](http://arxiv.org/abs/2608.16203v1)
  <details><summary>📄 Abstract</summary>
  Existing speech retrieval systems rely on fixed similarity matching and cannot adapt to diverse user intents. We introduce INSPIRE, the first benchmark for instruction-aware speech retrieval, in which natural-language instructions dynamically specify relevance criteria, including semantic content, speaker identity, speaking style, environmental sounds, and their combinations. We evaluate four retrieval paradigms: large audio-language models, cascaded pipelines, self-supervised speech models, and...
  </details>

- **2026-08-17** — Maoke Miao, Bo Liu, Xinyu Zhang et al. — [Gaussianization-Based Parameter Estimation for Gamma-Gamma and Lognormal-Rician Turbulence Channels](http://arxiv.org/abs/2608.15990v1)
  <details><summary>📄 Abstract</summary>
  Accurate parameter estimation for atmospheric turbulence channels is challenging because the probability density functions of the Gamma-Gamma (GG) and Lognormal-Rician (LR) models involve special functions and numerical integrations. This paper proposes two Gaussianization parameter estimators for GG and LR turbulence channels, i.e., the quantile-transformation (QT) estimator and the Box-Cox estimator. The QT estimator employs bidirectional cross-transformation together with higher-order statist...
  </details>

- **2026-08-16** — Sky Ng, Brihi Joshi, Ishan Gupta et al. — [MicroVerse: An Instrument for Measuring Self-Authored Identity Drift in Long-Horizon Multi-Agent Language-Model Simulations](http://arxiv.org/abs/2608.15844v1)
  <details><summary>📄 Abstract</summary>
  Long-horizon, multi-agent language model (LM) simulations are widely proposed for studying social behavior, yet instruments to measure whether persona-conditioned agents maintain identity fidelity under sustained pressure are lacking. We present MicroVerse, a behavioral-science instrument that measures identity drift in generative agents. Agents carry an immutable "soul file" (core values, moral boundaries, personality, goals) and inhabit a resource-scarce 50 x 50 environment where water is a no...
  </details>

- **2026-08-16** — Jose Rodriguez, Sven Koenig, Wenjie Dong et al. — [Grouping Auction-Consensus Algorithm for Decentralized Task Allocation in Multi-Robot Systems](http://arxiv.org/abs/2608.15884v1)
  <details><summary>📄 Abstract</summary>
  Decentralized multi-robot task allocation (MRTA) is essential for scalable and resilient autonomous systems. The Consensus-Based Bundle Algorithm (CBBA) is a widely adopted decentralized baseline. However, its individual task-level bidding is poorly aligned with the min-sum objective of minimizing total team travel distance, leading to suboptimal allocations in spatially distributed environments. This paper introduces the Grouping Auction-Consensus Algorithm (GACA). This decentralized MRTA frame...
  </details>

- **2026-08-16** — Wumei Du, Jiarong Wen, Kaiyu Zhang et al. — [PERO: Efficient Robust Post-Training Foundation Models for Encrypted Traffic Classification](http://arxiv.org/abs/2608.15504v1)
  <details><summary>📄 Abstract</summary>
  Encrypted traffic classification is vital for network security, yet real-world deployments are inherently sensitive to rare but high-loss errors such as misclassification of malicious traffic. The encrypted traffic foundation model, as a promising general-purpose technique, can achieve impressive overall performance. However, employing standard objectives such as empirical risk minimization often overlooks high-risk tail events, and commonly used performance metrics hardly reflect robustness lim...
  </details>

- **2026-08-16** — Abraham Toluwase Owodunni, Chibuzor Okocha, Christan Grant et al. — [Dynamic Multi-Byte Prediction With Hierarchical Language Models](http://arxiv.org/abs/2608.15454v1)
  <details><summary>📄 Abstract</summary>
  Byte-level hierarchical language models (LMs) have recently emerged as a robust alternative to their popular counterparts that use subword tokenization. However, generating one byte at a time remains a bottleneck for inference speed. To address this, we introduce multi-byte prediction (MBP), which generates multiple bytes in parallel, speeding up inference with minimal performance impact and no additional parameters. MBP builds on the popular multi-token prediction (MTP) paradigm with two crucia...
  </details>

- **2026-08-16** — Hao Zhang, Zhangli Zhou, Zhen Kan — [Temporal Logic Guided Universal Task Representations for Reinforcement Learning](http://arxiv.org/abs/2608.15509v1)
  <details><summary>📄 Abstract</summary>
  Task guided agents demonstrate strong performance in a wide range of complex tasks. However, most existing task representation algorithms are tailored to specific contexts and struggle to generalize across diverse scenarios. Moreover, they typically depend on gradient signals from reinforcement learning controllers to update their weights, which can degrade both representation quality and learning efficiency. To overcome these limitations, we propose LOTUS, a temporal logic inspired universal ta...
  </details>

- **2026-08-16** — Stefano Scialla, Marco Patriarca, Els Heinsalu et al. — [A memory-based three-state model of competing technology adoption: substitution regimes, multi-homing, and churn](http://arxiv.org/abs/2608.15706v1)
  <details><summary>📄 Abstract</summary>
  Technologies, products, platforms, and behavioral routines often compete through gradual adoption, reinforcement-dependent use, and temporary multi-homing. We formulate a homogeneous, well-mixed, three-state agent-based model of competition between an incumbent option (X) and a challenger (Y). Agents are exclusive users of (X), exclusive users of (Y), or dual adopters (Z). Adoption is memory-based: an exclusive user adds the alternative only after enough adoption-relevant encounters within a fin...
  </details>

- **2026-08-16** — Tianhui Zhu, Carlos A. Gonzalez, Shihao Tu et al. — [Individual Vanadium Dopants Form Deep In-Gap States in Monolayer WS2](http://arxiv.org/abs/2608.15551v1)
  <details><summary>📄 Abstract</summary>
  Point defects in atomically thin materials have a strong impact on physical properties and those that induce in-gap states are advantageous for quantum information science and engineering (QISE). However, dopant engineering consisting of well-controlled synthesis and robust identification of in-gap states is challenging. In this work, we addressed this challenge by first using finely tuned chemical vapor deposition to incorporate vanadium dopants into a monolayer WS2 (V-WS2). Next, we utilized a...
  </details>

- **2026-08-16** — Wang Jiangtao, Nur Intan Raihana Ruhaiyem, Fu Panpan et al. — [EA-LiteUNet: An Edge-Adaptive and Resource-Efficient U-Net for Boundary-Sensitive Dermoscopic Image Segmentation](http://arxiv.org/abs/2608.15537v1)
  <details><summary>📄 Abstract</summary>
  Accurate boundary delineation remains a persistent challenge in dermoscopic image segmentation because of blurred lesion margins, heterogeneous textures, and complex background artifacts. From a signal-processing perspective, lesion boundaries represent high-frequency components that are highly susceptible to aliasing, noise amplification, and information loss. Consequently, repeated downsampling and feature transformations in conventional convolutional architectures often lead to severely degra...
  </details>

- **2026-08-16** — Jie Wei, Yue Liu, Xiaochuan Tang et al. — [A Network-driven Framework for Public Event Forecasting via Dynamic Interaction Network Evolution](http://arxiv.org/abs/2608.15488v1)
  <details><summary>📄 Abstract</summary>
  Effective public event forecasting is essential for intelligent service systems, enabling proactive risk management, adaptive resource allocation, and timely decision-making. In many real-world scenarios, the evolution of public events is driven by dynamic interactions among participants. Motivated by this observation, this paper proposes auto-ibDLM, a network-driven deep learning framework that represents events as dynamic interaction networks and predicts public event evolution through partici...
  </details>

- **2026-08-15** — Rakesh Sharma, Sydney Pugh, Cameron Beeche et al. — [ETHOS: Towards a Modular Ethics Framework for Clinical Multi-Agent Systems](http://arxiv.org/abs/2608.15424v1)
  <details><summary>📄 Abstract</summary>
  The rapid adoption of large language models has enabled the development of clinical multi-agent systems (MAS) capable of integrating multimodal patient data and supporting increasingly complex clinical decision-making. However, the deployment of these systems in real-world healthcare settings raises critical ethical concerns related to safety, fairness, accountability, transparency, and patient trust. While numerous organizations, including the World Health Organization, the National Academy of ...
  </details>

- **2026-08-15** — Sahil Gangurde — [AudioTQ: A Data-Oblivious 6-Bit CPU Audio Codec via Randomized Hadamard Rotation and Lloyd-Max Quantization](http://arxiv.org/abs/2608.15369v1)
  <details><summary>📄 Abstract</summary>
  Lossy audio compression algorithms traditionally rely on psychoacoustic modeling and frequency-domain representations (e.g., MP3, AAC, and Opus) to discard information that is imperceptible to the human auditory system. While highly effective, these approaches are computationally complex and domain-specific. In this paper, we present the design and mathematical formulation of AudioTQ, a data-oblivious lossy audio codec that operates directly in the time domain. Inspired by Large Language Model (...
  </details>

- **2026-08-15** — Chan Lee, Kimin Yun, Yuseok Bae et al. — [PersonaDrive: Controllable Trajectory Prediction with Multi-Dimensional Driving Personas](http://arxiv.org/abs/2608.15230v1)
  <details><summary>📄 Abstract</summary>
  Although recent trajectory prediction and end-to-end autonomous driving methods improve robustness in urban environments, they still lack meaningful controllability. Existing benchmarks either provide no persona-conditioned annotations or support only a single urgency spectrum (i.e., emergency, normal, relaxed), which cannot distinguish personas that share the same urgency level but require different driving dynamics. To address this, we propose (i) the Persona-Conditioned Trajectory (PCT) datas...
  </details>

- **2026-08-15** — Ummara Mumtaz, Aimen Noor, Awais Ahmed — [Grounding Healthcare LLMs in a Causal Knowledge Graph: Framework, Metrics, and a Cardiovascular Pilot](http://arxiv.org/abs/2608.15382v1)
  <details><summary>📄 Abstract</summary>
  Large language models (LLMs) are increasingly proposed for healthcare decision support, but their evaluations still reward single-answer accuracy rather than reasoning about interventions, mechanisms, harms, evidence, and uncertainty. We propose a reproducible, graph-centered evaluation framework for intervention-oriented LLM behavior in healthcare and stress-test it in a cardiovascular pilot. The framework has four components: (i) a domain causal knowledge graph in which assertions are first-cl...
  </details>

- **2026-08-15** — Changruo Zhao, Zujun Peng, Yu Tian et al. — [Agentic-SQL Revisited: Autonomy-Based Taxonomy and Empirical Benchmark Analysis for LLM Text-to-SQL](http://arxiv.org/abs/2608.15389v1)
  <details><summary>📄 Abstract</summary>
  LLM-based Text-to-SQL progress is reported across heterogeneous benchmarks, backbones, and inference protocols, making cross-system comparison fragile. We reframe the field as a leaderboard aggregation: we collect the metrics authors themselves report and organize them along an inference-autonomy axis spanning constrained, in-context, iterative, agentic, and reasoning-internalized generation, with traceable provenance for every cell. To anchor the aggregation empirically, we run a focused case s...
  </details>

- **2026-08-15** — Yirun Wang, Soung Chang Liew, Yuyang Du — [ICL-SEC: Iterative Cross-Layer Semantic Error Correction](http://arxiv.org/abs/2608.15207v1)
  <details><summary>📄 Abstract</summary>
  Iterative decoding has been central to the success of modern channel coding, where reliability information is repeatedly exchanged across decoding components to approach fundamental performance limits. This paper brings the same principle to semantic error correction by proposing iterative cross-layer semantic error correction (ICL-SEC), a framework that closes the loop between physical-layer soft channel decoder and application-layer language-model-empowered semantic decoder. In the proposed fr...
  </details>

- **2026-08-15** — Luca Cirfeta — [Stress-Testing DANTE under Detector Domain Shift: a Representation-Coherent Reanalysis of LIGO O4a](http://arxiv.org/abs/2608.15166v1)
  <details><summary>📄 Abstract</summary>
  This sixth version of the Domain-Adaptive Network for Transient Evaluation (DANTE) preprint stress-tests an unsupervised transient-noise pipeline under representation mismatch and observing-run adaptation. We reanalyse 10,429 detector-time strain candidates from 42 LIGO O4a sessions using frozen DINOv2 patch embeddings and a Top-k multiple-instance score. Candidate and native-background Q-transforms share Q in [4,64], and detector-specific thresholds are calibrated from 5,000 run-native windows ...
  </details>


### 📂 watermark
*水印与溯源 / Watermarking & Provenance* — 15 papers

- **2026-08-18** — Maolin Ran, Xiaoyang Lu, Jiaqi Liu et al. — [SAGE: Self-Evolving Storyboard Skills via Attribution-Guided Rule Evolution](http://arxiv.org/abs/2608.17468v1)
  <details><summary>📄 Abstract</summary>
  Storyboards turn screenplays into visual shot plans for automated short drama production. Professional storyboarding relies on tacit directorial expertise and remains an industrial bottleneck. Large language models can automate this step, but methods for supplying directing knowledge face three challenges: (1) Knowledge acquisition: the craft remains implicit in exemplars or must be written manually. (2) Knowledge refinement: authored knowledge is not evaluated against execution outcomes, and op...
  </details>

- **2026-08-18** — Zhi Zheng, Rongsheng Chen, Yunpeng Ba et al. — [Agentic ESOpt: Fine-Tuning Long-Horizon LLM Agents with Minimal GPU Requirements](http://arxiv.org/abs/2608.17310v1)
  <details><summary>📄 Abstract</summary>
  Reinforcement Learning (RL) has been promising in single-turn LLM fine-tuning. However, long-horizon agentic reasoning introduces increasingly branching interactions and sparse rewards, exposing several limitations of RL: its heavyweight backpropagation-based training stack makes it impractical to fine-tune larger LLMs, and longer-horizon trajectories make credit assignment in RL substantially harder. This paper argues that evolution strategies (ES) can be a better choice for fine-tuning long-ho...
  </details>

- **2026-08-17** — Pengyin Shan — [A Multi-Surface Consistency Audit of Software Citation Metadata](http://arxiv.org/abs/2608.17159v1)
  <details><summary>📄 Abstract</summary>
  Research software projects describe themselves in many places at once: citation files in the repository, archive deposits, DOI registry records, package registries, and README text. We treat the software as the underlying object and these machine-readable self-descriptions as its surfaces: the points where people and automated systems read what the project declares about the software. Citation guidance, indexing services, and automated agents may read a different subset of these surfaces, so dis...
  </details>

- **2026-08-17** — Siyi Li, Yuchen Kang, Wuliang Wang et al. — [DeepInsight II: One Trace from Benchmark to Robot](http://arxiv.org/abs/2608.16556v1)
  <details><summary>📄 Abstract</summary>
  Across a Physical AI stack, evaluation maturity is inversely aligned with deployment risk: foundation models enjoy mature, standardized harnesses, while the embodied layers on which deployment actually turns remain fragmented across benchmark-specific simulators, embodiments, and interfaces. The first DeepInsight report (v1) unified evaluation across this stack behind three abstractions---task, resource, and result---but its quantitative evidence centered on the foundation-model layer; navigatio...
  </details>

- **2026-08-17** — Benjamin Belay — [Towards Computational Provenance: Carrying Causal-State Evidence in Generated Text](http://arxiv.org/abs/2608.16868v1)
  <details><summary>📄 Abstract</summary>
  A language model's output does not by itself provide verifiable evidence about the internal computation that produced it. We study computational provenance: whether generated text can carry detectable evidence of which causally relevant internal state occurred. We test a bounded form of this idea in two controlled architectures: a modular feed-forward neural network and a transformer-based model. Both architectures are trained on the same arithmetic task with a mandatory pathway through two disc...
  </details>

- **2026-08-17** — Homa Esfahanizadeh, Matin Mortaheb, Jinfeng Du et al. — [UniTAC: Universal Task-Aware Compression via Weighted Distortion Measures](http://arxiv.org/abs/2608.16696v1)
  <details><summary>📄 Abstract</summary>
  Physical AI systems such as autonomous vehicles and robots rely on timely exchange of high-dimensional sensory signals under tight bandwidth, latency, and energy budgets. Because the task driving downstream decisions evolves over time, a task-specific codec is brittle and retraining one per task is infeasible in the field. We propose UniTAC, a single learned image codec spanning universal (task-agnostic) to task-specialized operation, re-targeted at runtime without retraining. The task is abstra...
  </details>

- **2026-08-17** — Xueping Gao — [Executable Code Knowledge: Code as a Native, Validation-Carrying Knowledge Representation for AI Coding Agents](http://arxiv.org/abs/2608.16295v1)
  <details><summary>📄 Abstract</summary>
  AI coding agents need more than relevant snippets: they need business semantics, validation evidence, relations, and assurance that their context is current. Existing systems usually infer or externalize this knowledge through retrieval, summaries, graphs, rules, or reverse specifications. We investigate a complementary representation in which selected code units directly carry agent-usable knowledge. We introduce Executable Code Knowledge (ECK) and define an Executable Code Knowledge Unit (ECKU...
  </details>

- **2026-08-16** — Sabry E. Farrag — [Where Accountability Lives: Mapping Human Responsibility to Workflow Artifacts in Agentic Software Development](http://arxiv.org/abs/2608.15678v1)
  <details><summary>📄 Abstract</summary>
  Coding agents author commits, open pull requests, and push code in production repositories. Who is accountable is settled in two places that do not refer to each other: the platform controls that gate what an agent may do, and the provider terms that allocate responsibility for what it produces.   We read both against the workflow events that leave artifacts, across four agentic coding tools and eighteen governing policy documents from seven providers, recording at each event who holds authority...
  </details>

- **2026-08-16** — Parviz Shariff — [The Authority Resolution Framework: A Five-Domain Ontology for Governing Who and What Decides, at Scale](http://arxiv.org/abs/2608.15832v1)
  <details><summary>📄 Abstract</summary>
  As AI systems become increasingly capable of autonomous action, determining whether an agent is technically capable of performing an action is insufficient: the system must also determine whether the action is authorised in its context.   This paper introduces the Authority Resolution Framework (ARF), a five-domain ontology for representing and resolving authority across organisational roles and informal influence, business concepts, codified processes, machine-readable permissions and executabl...
  </details>

- **2026-08-16** — Hongfu Huang, Yuzhe Li, Ao Xu et al. — [ALKEMIE Agent: an autonomous platform for computational materials design](http://arxiv.org/abs/2608.15776v1)
  <details><summary>📄 Abstract</summary>
  Despite the powerful multi-scale modeling methods and high-throughput infrastructures established in the materials community, real material computation workflows remain fragmented and heavily manual, requiring researchers to constantly bridge software tools, data analysis, and intermediate decisions. This growing gap between methodological capability and practical execution highlights the need for a new kind of autonomous computational framework, one that can coordinate tools, knowledge, and wor...
  </details>

- **2026-08-16** — Meiling Tao, Yiling Tao, Peng Wang — [Intent-Driven Situation Tracking for User-Centric Multi-Turn Agents](http://arxiv.org/abs/2608.15755v1)
  <details><summary>📄 Abstract</summary>
  User-centric multi-turn agents must act on an evolving task situation shaped by changing user intents, accumulated tool-grounded facts, missing information, and execution constraints. Existing context-management methods improve the use of past interaction history, but rarely maintain an explicit situation state that separates grounded facts from task-state judgments. As a result, agents often need to infer fine-grained attributes, task dependencies, and constraint satisfaction implicitly from di...
  </details>

- **2026-08-16** — Jinhyun Jeon, Sungjoo Yoo — [GraniKV: Asymmetric Granularity KV-Cache Paging for Multi-Agent Systems with Long Shared Prefix](http://arxiv.org/abs/2608.15584v1)
  <details><summary>📄 Abstract</summary>
  Production paged-serving engines apply uniform paging granularity to the KV cache, even though the two regions of a multi-agent workload have opposite storage requirements: a long shared prefix demands contiguity, while the per-request suffix demands fine-grained allocation.   We present \textbf{GraniKV}, a KV-cache layer that allocates the shared prefix in a contiguous HOT pool and the suffix in a token-level COLD pool, combined with a per-step dispatcher which selects the appropriate backend a...
  </details>

- **2026-08-15** — Yunfei Zhang, Boyu Feng, Changhua Pei et al. — [LongRCA Bench: Diagnosing Responsible Roles and Root Causes in Long-Horizon Agent Failures](http://arxiv.org/abs/2608.15242v1)
  <details><summary>📄 Abstract</summary>
  When a long-horizon agent execution fails, outcome-level evaluation reveals the unsuccessful result but not where the decisive error entered the trajectory. Developers must then inspect the full execution to identify the responsible role and localize the earliest decisive root-cause step. Existing failure-attribution benchmarks largely focus on shorter traces, leaving diagnosis across hundreds of recorded steps underexplored. We introduce LongRCA Bench, comprising 1,140 failed trajectories acros...
  </details>

- **2026-08-15** — Yuyang Zheng, Nan Li, Wenxia Deng et al. — [Valhalla: A Layered Knowledge-State and Service-Governance Framework for Long-Term Scientific Knowledge Work](http://arxiv.org/abs/2608.15193v1)
  <details><summary>📄 Abstract</summary>
  As large language model (LLM) agents are increasingly adopted in scientific research, external knowledge bases, knowledge graphs, and long-term memory have improved information retrieval and task continuity. However, most structured knowledge systems remain node-centric, representing files, concepts, results, and judgments as nodes and relations in a graph. While suitable for personal knowledge management, such structures often depend on individual organizational practices, limiting knowledge sh...
  </details>

- **2026-08-15** — Rosen Ting-Ying Yu, Christophe Hatterer, Advaith Narayanan et al. — [BOCoDe: Engineering-Centered Benchmarking for Bayesian Optimization](http://arxiv.org/abs/2608.15073v1)
  <details><summary>📄 Abstract</summary>
  Bayesian optimization (BO) is a sample-efficient, surrogate-based approach to black-box optimization (BBO), but its evaluation remains dominated by synthetic functions and hyperparameter optimization (HPO) tasks that are typically low-dimensional and single-objective. Engineering design poses a substantially different regime: problems are physics-based, often high-dimensional, constrained by requirements such as cost and manufacturability, and may involve multiple objectives or mixed variables. ...
  </details>


### 📂 unlearning
*机器遗忘 / Machine Unlearning* — 4 papers

- **2026-08-17** — Aditya Kumar, Sumit Chongder — [Dynamic Entanglement-Weighted Pruning for Quantum Federated Unlearning in Supply-Chain Risk Prediction](http://arxiv.org/abs/2608.17069v1)
  <details><summary>📄 Abstract</summary>
  Federated deployments of variational quantum classifiers are attractive for cross-organisation risk prediction in supply chains, because raw data never leaves the client, yet data-protection regulations such as the GDPR grant clients a right to request that their contribution be removed from a trained model after the fact. Retraining a federated model from scratch to honour such a request is correct but wasteful, and it is not obvious which quantum circuit parameters actually carry a given clien...
  </details>

- **2026-08-17** — Jaewan Choi, Junyoung Yang, Sangdon Park — [SAUL: Sharpness-Aware Augmented-Lagrangian Unlearning](http://arxiv.org/abs/2608.16249v1)
  <details><summary>📄 Abstract</summary>
  Machine unlearning in Large Language Models (LLMs) faces a critical trade-off between erasing target knowledge and preserving general utility. We propose SAUL (Sharpness-Aware Augmented-Lagrangian Unlearning), which formulates unlearning as a constrained minimization problem following the principle of "forget enough, but no more than necessary." At its core, SAUL formulates forgetting as an explicit constraint with a prescribed satisfaction criterion, whereas prior unlearning methods typically s...
  </details>

- **2026-08-16** — Cedar Site Bai, Amber Yijia Zheng, Raymond A. Yeh et al. — [Spectral Saliency for Machine Unlearning](http://arxiv.org/abs/2608.15548v1)
  <details><summary>📄 Abstract</summary>
  Machine unlearning (MU) aims to remove the influence of specific training data while preserving model utility. As the name suggests, MU can be viewed as the inverse of learning, using gradient-based updates to reduce the influence of a forget-set by counteracting the previously learned behavior. Recently, Muon, a gradient descent variant, has been introduced. Muon applies spectral magnitude normalization to encourage exploration of rare directions and demonstrates promising performance. Inspired...
  </details>

- **2026-08-14** — Anna Borisiuk, Andrey Savchenko, Alexander Panchenko et al. — [The More Popular, The Harder to Forget: Adaptive Popularity for LLM Unlearning](http://arxiv.org/abs/2608.14229v1)
  <details><summary>📄 Abstract</summary>
  Popular facts are memorised more deeply during pretraining and resist removal longer than rare ones, yet existing LLM unlearning methods apply uniform gradient pressure regardless of training-data frequency. We propose the AdaPop (Adaptive Popularity) method, which combines local token confidence with a per-fact popularity-dependent exponent derived from an external proxy (e.g., Wikidata sitelinks, LLM-as-Judge), and automates the forget-retain balance via a dual-ascent controller that adjusts t...
  </details>


### 📂 benchmark
*安全评测与基准 / Safety Benchmarks & Evaluation* — 2 papers

- **2026-08-17** — Peng Du, Kiran Kamble, Rakshith Vasudev et al. — [Palmyra x6 Technical Report: An Agentic, Tool-Use Model Post-Trained via Anchored Supervised Fine-Tuning](http://arxiv.org/abs/2608.16620v2)
  <details><summary>📄 Abstract</summary>
  Palmyra x6 is a large language model optimized for use with enterprise-oriented agentic tasks. The model was built by post-training a Mixture-of-Experts base model with Anchored Supervised Fine-Tuning on a compact corpus of verified, synthetic tool-use trajectories, optimized with a Muon + Adam hybrid. The recipe is deliberately conservative and deliberately controlled: 626 trajectories, a single epoch, a low learning rate, and a KL anchor to the frozen base. The model shows substantial gains ov...
  </details>

- **2026-08-17** — Peng Du, Kiran Kamble, Rakshith Vasudev et al. — [Palmyra x6 Technical Report: An Agentic, Tool-Use Model Post-Trained via Anchored Supervised Fine-Tuning](http://arxiv.org/abs/2608.16620v1)
  <details><summary>📄 Abstract</summary>
  Palmyra x6 is a large language model optimized for use with enterprise-oriented agentic tasks. The model was built by post-training a Mixture-of-Experts base model with Anchored Supervised Fine-Tuning on a compact corpus of verified, synthetic tool-use trajectories, optimized with a Muon + Adam hybrid. The recipe is deliberately conservative and deliberately controlled: 626 trajectories, a single epoch, a low learning rate, and a KL anchor to the frozen base. The model shows substantial gains ov...
  </details>


### 📂 survey
*综述与系统化 / Surveys & Systematization* — 5 papers

- **2026-08-17** — Morita Tarvirdians, Hayley Hung, Catharine Oertel — [Why This and Not That? A Collaborative Reflection Approach for Understanding Thought Coverage in Decision Making Support Dialog](http://arxiv.org/abs/2608.17054v1)
  <details><summary>📄 Abstract</summary>
  Conversational agents that support reflection for decision making often rely on adaptive dialogue policies that map observed user behavior to actions such as probing, deepening, or redirecting. Yet the same pattern can reflect a range of different reasons such as deliberate prioritisation or limited self-access. By modeling the observable pattern rather than the user's reason for it, current policies risk premature assumptions about the user state and inappropriate next actions. To address this ...
  </details>

- **2026-08-17** — Andrew Borthwick — [Competing at Every Price Point with Agentic Evolution over a Menu of LLMs](http://arxiv.org/abs/2608.16207v1)
  <details><summary>📄 Abstract</summary>
  Consider a firm that surveys its competition for a particular agentic task and seeks to offer superior accuracy at every competitor price point. A firm that Pareto-dominated its competitors would leave no rational customer a reason to buy elsewhere. This paper shows a path to this kind of capability via agentic evolution over a menu of LLMs, from training pools of at most 100 examples. Given a priced menu of nine LLM endpoints; brief documentation of the task, objective, and API; a simple seed a...
  </details>

- **2026-08-16** — Farbod Abbasi, Zachary Patterson, Bilal Farooq — [Feasible and Novel Synthetic Population Generation with Tabular and Sequential Travel Attributes](http://arxiv.org/abs/2608.15867v1)
  <details><summary>📄 Abstract</summary>
  Synthetic populations are critical inputs for activity-based travel demand models, yet generating realistic populations from limited survey data remains challenging. Small samples miss valid attribute combinations, known as sampling zeros, and generative models may also produce infeasible structural zeros. Moreover, realistic synthetic populations must capture both static socio-demographic attributes and sequential travel behaviour, such as trip chains. This paper proposes a regularized two-stag...
  </details>

- **2026-08-16** — Taishi Odaka, Kentaro Sakamaki — [Energy Balancing Weights for Mediation Analysis](http://arxiv.org/abs/2608.15497v1)
  <details><summary>📄 Abstract</summary>
  Causal mediation analysis requires reconstruction of counterfactual distributions to estimate natural direct and indirect effects. Inverse probability weighting estimators rely on models for treatment assignment and mediator density ratios, whereas moment balancing approaches require researchers to specify in advance which functions of the covariates and mediators should be balanced. We propose Energy Balancing Weights for Mediation Analysis (EBWMA), which targets the joint mediator-covariate di...
  </details>

- **2026-08-16** — Nilotpal Sanyal — [Competing-Risk Cure Models: A Five-Axis Systematic Review of Methodological Literature](http://arxiv.org/abs/2608.15455v1)
  <details><summary>📄 Abstract</summary>
  Competing-risk cure models describe time-to-event populations with individuals immune to all event types or an event of interest, yet literature is fragmented across model families. We review 26 papers across five axes: cure definition/scope; decomposition/cure mechanism; latency; dependence, censoring, and masked causes; and estimation. We distinguish global from cause-specific cure and incidence--latency mixtures from vertical susceptibility factorizations, latent competing-causes/zero-count c...
  </details>


### 📂 other
*其他安全相关 / Other Security-Related* — 168 papers

- **2026-08-18** — Christophe D. Hounwanou, John Emeka Eze, Yaé U. Gaba — [Policy-Invariant Reward Shaping from LLM Feedback: A Framework for Hybrid RL Agents](http://arxiv.org/abs/2608.18008v1)
  <details><summary>📄 Abstract</summary>
  Combining large language models with reinforcement learning is increasingly explored, yet the theoretical status of LLM-derived reward signals is often left implicit. We formalize the hybrid LLM-planner and RL-controller architecture as a Goal-Augmented Markov Decision Process and show that when the LLM per-state progress score is used as a bounded potential function, the resulting shaping term preserves the optimal policy set even when the LLM scores are inaccurate. This guarantee is stronger t...
  </details>

- **2026-08-18** — Roman Maksimov, Vladimir Aletov, Vladimir Solodkin et al. — [Leveraging Association Context Retrieval in Knowledge Edit- ing to Build White-Box Attacks on LLMs](http://arxiv.org/abs/2608.17836v1)
  <details><summary>📄 Abstract</summary>
  As large language models (LLMs) are granted increasing autonomy, it is essential to investigate methods that can induce unsafe behavior. We propose a novel white-box attack inspired by locate-then-edit approaches from the field of Knowledge Editing. Our choice is motivated by the observation that models edited with such schemes tend to assign unusually high prediction probabilities to the edit target, a property that is particularly advantageous when designing attacks. We modify the editing fram...
  </details>

- **2026-08-18** — Jialong Li, Jialing Zhu — [Auditing Self-Evolution in Financial Agents: Capability Gains, Security Drift, and Execution-Interface Mismatch](http://arxiv.org/abs/2608.17684v1)
  <details><summary>📄 Abstract</summary>
  Self-evolving agents turn experience into reusable skills, workflows, or memories, but post-evolution accuracy alone does not show whether learned behavior preserves previously correct behavior or security. We audit SkillOpt, Agent Workflow Memory (AWM), and ReasoningBank in simulated e-banking using matched benign acquisition trajectories, sealed evaluation endpoints, execution-grounded checks, and independent state replay. On Qwen 3.7 Flash, SkillOpt raises benign utility from 0.741 to 0.837 w...
  </details>

- **2026-08-18** — Jincheng Yang, Yulong Fu, Chengwei Liu et al. — [Benchmarking Automated Security Patch Backporting: How Far Are We?](http://arxiv.org/abs/2608.17671v1)
  <details><summary>📄 Abstract</summary>
  Automated security patch backporting is critical for mitigating N-day vulnerabilities. Recent tools report success rates above 80% on their respective datasets. However, these evaluations are often confined to homogeneous environments, such as one repository or specific project versions. Consequently, it remains unclear how well these tools generalize beyond their originally targeted scenarios. We present Porting Benchmark, a curated dataset of 1,234 security patch backporting cases spanning cro...
  </details>

- **2026-08-18** — Haoran Bu, Zejian Chen, Litian Zhang et al. — [GraphWake: Group Polarization via Memory-Mediated Polarization Cascade in LLM-Agent Communities](http://arxiv.org/abs/2608.17665v1)
  <details><summary>📄 Abstract</summary>
  LLM-driven agents can autonomously exchange opinions on online platforms and form communities. Such agent-operated social platforms raise a new security concern: attackers may manipulate agents to induce group polarization. Existing methods manipulate agent prompts or construct echo chambers, both of which are difficult to realize in practice. We therefore formulate a new threat, Memory-Mediated Polarization Cascade, which uses agent memory as a persistence channel and public discussion as a pro...
  </details>

- **2026-08-18** — Mateo Cárdenes Wuttig, Joseph Tindall — [A Complete Classification of Complex Hadamard Matrices of Order Six](http://arxiv.org/abs/2608.18053v1)
  <details><summary>📄 Abstract</summary>
  Complex Hadamard matrices encode perfectly balanced unitary transformations. They underlie mutually unbiased quantum measurements and multiphoton interferometry. Their classification is complete through order five, but order six -- the first dimension in which several continuous families coexist with an isolated solution -- has remained open for decades. Here, we give a complete and exact finite-incidence classification of order-six complex Hadamard matrices up to standard equivalence. We first ...
  </details>

- **2026-08-18** — Emma Ceccherini, Daniel Lawson, Anjulika Salhan — [Where A Small Language Model Helps in Invoice Categorisation, Understood Through Embedding Geometry](http://arxiv.org/abs/2608.18033v1)
  <details><summary>📄 Abstract</summary>
  Categorising invoices into the correct General Ledger (GL) code underpins financial reporting and tax compliance. This is a skilled accounting judgement rather than a routine task: the correct category depends subtly on the nature of the purchasing business, the vendor and the invoice text. Whilst AI is increasingly being adopted across industries to automate tasks, including invoice categorisation, implementations built on in-house small language models (SLMs) can simultaneously reduce cost and...
  </details>

- **2026-08-18** — Alexis Farman, Benjamin J. Walker, Martin A. Pule et al. — [Mathematical modelling of immune persistence and relapse pathways in CAR T-cell therapy for B-ALL](http://arxiv.org/abs/2608.17955v1)
  <details><summary>📄 Abstract</summary>
  Chimeric antigen receptor (CAR) T-cell therapy has transformed the treatment of B-cell acute lymphoblastic leukaemia (B-ALL). Despite high initial response rates, a substantial fraction of patients relapse, often due to loss of CAR T-cell persistence, antigen escape, or immune-privileged sites that shield tumour cells. Prolonged CAR T-cell persistence is clinically associated with durable remission, but why it is required remains poorly understood. To address this, we develop and analyse the BEA...
  </details>

- **2026-08-18** — Zixuan Li — [Bounded-State Restoration: Decoupling Local Restore Capacity from External LLM State](http://arxiv.org/abs/2608.17826v1)
  <details><summary>📄 Abstract</summary>
  Hierarchical KV-cache systems can retain long-context LLM execution state beyond GPU memory, but retention capacity does not determine the local memory required to make that state executable again. We isolate this second resource as the restoration working set (RWS): the peak local staging state whose lifetimes overlap during restoration. In the pinned upstream LMCache whole-plan path, measured full-reuse points for 1.956, 7.823, and 15.646 GiB/rank states first succeed at 2, 8, and 16 GiB L1 ru...
  </details>

- **2026-08-18** — Sumit S. Shevtekar, Chandresh K. Maurya, Gourab Sil et al. — [MotoSafety: Edge-AI with Learned Temporal Importance for Two-Wheeler Collision Risk Assessment Under Time Pressure](http://arxiv.org/abs/2608.17823v1)
  <details><summary>📄 Abstract</summary>
  Powered two-wheeler riders face critical safety challenges in low- and middle-income countries, yet limited studies exist on how cognitive stressors such as Time Pressure influence collision risk. To address this gap, we introduce a large-scale dataset of over 129,000 labeled multivariate time-series sequences from 153 simulator rides by 51 participants under No, Low, and High TP, capturing 64 features across vehicle dynamics, control inputs, proximity, and behavioral violations. Building on thi...
  </details>

- **2026-08-18** — Sahab Zandi, Noah Kostesku, Christophe Mues et al. — [Communicating Credit Risk with Large Language Models: Evaluation of Explanations from Standard and Alternative Data-Based Models](http://arxiv.org/abs/2608.17715v1)
  <details><summary>📄 Abstract</summary>
  Credit decisioning is a high-stakes task in which model outputs must be accurate and explainable to support compliant decisions. Although modern credit risk models such as eXtreme Gradient Boosting (XGBoost) and Graph Neural Networks (GNNs) improve predictive performance, their explanations are often too technical for stakeholders creating communication gaps that can shape approvals, denials, and fairness judgments. We examine whether Large Language Models (LLMs) can serve as explanation layers ...
  </details>

- **2026-08-18** — Jingyuan Wang, Richong Zhang, Zhijie Nie et al. — [DEPT: Document Embedding Preservation Tuning for Unified Query Expansion and Retrieval](http://arxiv.org/abs/2608.17632v1)
  <details><summary>📄 Abstract</summary>
  Large language models (LLMs) can both expand underspecified queries and encode text as dense representations, suggesting a unified model for query expansion and retrieval. Existing systems usually rely on prompted expansions, independently trained modules, or staged optimization, leaving generated expansions only indirectly aligned with the retrieval loss that judges them. We train a single decoder-only LLM end to end, where the same model generates the expansion and encodes both the expanded qu...
  </details>

- **2026-08-18** — Andrea Coladangelo, Qipeng Liu, Ziyi Xie — [Unclonable encryption from BB84 states: a simultaneous Goldreich-Levin reduction](http://arxiv.org/abs/2608.17629v1)
  <details><summary>📄 Abstract</summary>
  Goldreich-Levin reductions are ubiquitous in cryptography: they convert an algorithm capable of guessing $\langle r, m \rangle$ (mod $2$) for a hidden string $m$ and a random challenge $r$, to one that is capable of extracting the entirety of $m$. Here, we describe a "simultaneous" Goldreich-Levin reduction for two entangled parties who are capable of guessing $\langle r, m \rangle$ given uniformly random identical challenges $r$. This allows to upgrade any unclonable encryption scheme satisfyin...
  </details>

- **2026-08-18** — Wang Warren Chen, Jiahao Zhang, Zhenjiang Li et al. — [HODAgent: Towards On-Demand, Responsive Humanoids for Physical World Human Interaction](http://arxiv.org/abs/2608.17584v1)
  <details><summary>📄 Abstract</summary>
  We propose HODAgent, a System-2 embodied agent for humanoid robots in service settings, addressing situated intent, responsive execution, task revision, and outcome verification. Its semi-duplex architecture integrates an Env-Interactor, Planner, Executor, and hierarchical Memory to maintain coherent interaction, planning, and task state during service episodes. This allows handling new requests during motion, retaining progress, revising actions, and grounding closure in execution outcomes. A s...
  </details>

- **2026-08-18** — Zongwei Lv, Yuemeng Xu, Yilun Yao et al. — [ArborMem: Navigating Interaction States with Memory Forests](http://arxiv.org/abs/2608.17534v1)
  <details><summary>📄 Abstract</summary>
  Large language models increasingly serve as persistent conversational assistants, requiring memory that preserves relevant experience and maintains continuity across interactions. Existing methods improve access to conversational history through long-context processing, selective retrieval, and structured memory organization. However, most systems treat memory access as retrieving relevant past information without first determining which prior interaction state the current turn resumes. This lim...
  </details>

- **2026-08-18** — Madhumitha Venkatesh, Shanawaj S Madarkar, Konda Reddy Mopuri — [BrainNorm: A Foundation Model that knows Normal via Semantic Atlas Pretraining](http://arxiv.org/abs/2608.17521v1)
  <details><summary>📄 Abstract</summary>
  We introduce BrainNorm, a normative foundation model, trained and tested on ~66,000 T1-weighted structural MRI (T1w sMRI) scans. By leveraging language-image style contrastive pretraining on healthy cohorts across ages, BrainNorm learns a Semantic Atlas Latent space (SAL), where each scan is represented as a set of atlas-parcel embeddings. This yields parcel-specific healthy aging template trajectories that support age-consistent template matching and localized deviation scoring relative to a su...
  </details>

- **2026-08-18** — Matheus S. Azevedo, Geovana S. de Oliveira, Andrea Failla et al. — [The Brazilian Vaccination Debate on YouTube: Topics, Perspectives, and Engagement Dynamics](http://arxiv.org/abs/2608.17502v1)
  <details><summary>📄 Abstract</summary>
  Vaccination debates are central to online public health communication, as COVID-19 intensified disputes over scientific authority, institutional trust, and political identity. Yet studies often isolate semantic structure, stance, misinformation, and engagement, leaving their interplay over time poorly understood. We conduct a multilevel computational text analysis based on language models applied to 1.27 million Brazilian YouTube comments from 2018 to 2024, using what is, to our knowledge, the l...
  </details>

- **2026-08-18** — Yiwen Zhao, Zhihao Wen, Yuchen Mao et al. — [Towards Better Agents for Multi-Turn User Interaction: The Next User Turn Is More Than Context](http://arxiv.org/abs/2608.17499v1)
  <details><summary>📄 Abstract</summary>
  User-facing tool agents must coordinate dialogue and tool use as user goals unfold over multiple turns. Yet interactive reinforcement learning typically reduces each rollout to a terminal reward, assigning the same credit to effective elicitation, errors, and later repair. The next user turn is more than context: it also provides noisy, temporally local evidence about the preceding user-to-user segment. We introduce \textbf{F}eedback-\textbf{A}ware \textbf{C}redit \textbf{A}ssignment (\textsc{FA...
  </details>

- **2026-08-18** — Xingrui Zhuo, Jiapu Wang, Manzong Huang et al. — [Structure-Internalized Rule Language Model for Faithful Knowledge Graph Reasoning](http://arxiv.org/abs/2608.17443v1)
  <details><summary>📄 Abstract</summary>
  Knowledge Graph Reasoning (KGR) aims to discover latent facts by leveraging the structural evidence available in KGs, posing a challenge to the structural semantic understanding capability of KGR models. Recent studies have demonstrated that Large Language Models (LLMs) can achieve remarkable progress on KGR tasks via flexible in-context learning. However, the inherent representation inconsistency between KG structural context and LLM parametric knowledge remains inadequately addressed. This lim...
  </details>

- **2026-08-18** — Bonan Zhang, Shiyu Dong, Quan Hung Tran et al. — [MoE-ViE: Mixture of Experts Vision Encoder for Efficient Image and Video Understanding](http://arxiv.org/abs/2608.17402v1)
  <details><summary>📄 Abstract</summary>
  Vision encoders are a critical component of vision-language models, and scaling their capacity effectively improves performance. However, dense scaling increases compute cost and inference latency. Mixture-of-Experts (MoE) architectures offer a compelling alternative, having enabled efficient scaling in LLMs, yet the MoE design space for CLIP-style vision encoders remains underexplored at State-of-the-Art (SOTA) levels. In this work, we systematically study MoE designs for vision encoder scaling...
  </details>

- **2026-08-18** — Maria Valentini, Téa Wright, Julisa Granados et al. — [An Investigation of Translationese in the Generations of Multilingual Large Language Models](http://arxiv.org/abs/2608.17399v1)
  <details><summary>📄 Abstract</summary>
  Text which has been translated from another language tends to carry with it evidence of translation$\unicode{x2014}$hence, it is often referred to as $\textit{translationese}$. Multilingual large language models (MLLMs) generate text in a variety of languages. However, it is still unclear if MLLMs' generations resemble internal translation (from English or, potentially, other languages) and, thus, result in translationese. Here, we ask the following research questions: (1) Does text generated by...
  </details>

- **2026-08-18** — Arnab Mallick — [Brief Announcement: Fair Binding for Hidden-State Authorization in Byzantine SMR](http://arxiv.org/abs/2608.17349v1)
  <details><summary>📄 Abstract</summary>
  Validated Byzantine SMR assumes that replicas can evaluate the validity of an ordered command. Agent authorization creates a different regime: a command may be valid only relative to a committed policy state that validators cannot reconstruct from the log. A proof that an action was authorized at an old commitment is then only a historical attestation, it does not by itself reserve the hidden resource for later use.   We isolate two independent requirements for safe live allocation of a hidden c...
  </details>

- **2026-08-18** — Hanzhi Zhang, Qiao Zhang, Qinglei Cao et al. — [TileMix: Tile-Centric Mixed-Precision Attention for LLM Inference Acceleration](http://arxiv.org/abs/2608.17336v1)
  <details><summary>📄 Abstract</summary>
  Long-context prefill in large language models (LLMs) incurs substantial computation and memory traffic because dense self-attention computes quadratic query-key scores. Existing methods either use a uniform low-precision path or select token interactions, leaving spatial precision routing over hardware-aligned score tiles outside fused dense attention. We introduce TileMix, a tile-centric precision-routing kernel that makes numerical precision an executable spatial decision over score-tile group...
  </details>

- **2026-08-18** — Saketh Reddy Vemula, Parameswari Krishnamurthy — [What Tokens are Learned when Tokenization is Optimized Jointly with Language Modeling?](http://arxiv.org/abs/2608.17325v1)
  <details><summary>📄 Abstract</summary>
  Tokenization is a fundamental component of language modeling pipelines. Despite its importance, it is often fixed, even though it significantly impacts model performance across languages. In this work, we analyze what tokens are learned when tokenization is jointly optimized with language modeling. We compare tokenizer-free approaches such as SSLMs and H-Nets with fixed tokenizers across 18 typologically and script-diverse languages. Our results show that joint optimization fundamentally alters ...
  </details>

- **2026-08-18** — Zhiyuan Yan, Xiaofeng Zhou, Ziyue Zheng et al. — [NeuroAbs: A Neuro-Symbolic RTL Abstraction Framework for Property Checking Acceleration](http://arxiv.org/abs/2608.17304v1)
  <details><summary>📄 Abstract</summary>
  Formal verification is a crucial technique for ensuring the functional correctness of hardware designs. In the context of property checking, a key challenge is how to efficiently prove a user-specified property in the face of increasingly complex RTL designs. To address this challenge, abstraction techniques are often employed to reduce system complexity and accelerate the verification process. However, prior RTL abstraction methods either require significant manual effort or rely on rule-based ...
  </details>

- **2026-08-18** — Emama Nahid, Tahmid Imtiaz Imu, Huayue Gu et al. — [Q-Interference: Memory-Efficient Phase-Aware Quantum-Inspired Attention](http://arxiv.org/abs/2608.17288v1)
  <details><summary>📄 Abstract</summary>
  GPT attention measures token compatibility through dot-product similarity. This mechanism is simple, effective, and memory-efficient. But it does not explicitly model whether strong token features should reinforce or suppress one another. We introduce Q-Interference, a fully classical quantum-inspired attention mechanism for autoregressive language modeling that augments each query and key feature with an amplitude and a learned phase. The resulting attention score is phase-aware which aligned p...
  </details>

- **2026-08-18** — Ce Bian, Xusheng He, Jinrong Zhang et al. — [Key-Frame Reasoning with SAM3: Third Place Solution for the MeViS-Text Track of the 8th LSVOS Challenge](http://arxiv.org/abs/2608.17279v1)
  <details><summary>📄 Abstract</summary>
  This report presents a two-stage, training-free solution for the MeViS-Text track of the 8th LSVOS Challenge. The task requires a model to localize and segment the object specified by a natural-language expression throughout a video. Such expressions often depend on temporal cues, including actions, interactions, directions, and relative positions. Our first stage uses Gemini-3.1 Pro via API to decompose a video-level event into instance-level targets, select a key frame for each target, and gen...
  </details>

- **2026-08-18** — Swati Rajwal, Sanjay Das, Tirthankar Ghosal — [Do LLMs Know a Good Hypothesis When They See One? Logit-Based Energy Scoring Outperforms Prompted LLM-as-Judge for Scientific Hypothesis Ranking](http://arxiv.org/abs/2608.17270v1)
  <details><summary>📄 Abstract</summary>
  Large language models (LLMs) are increasingly used for scientific hypothesis generation. However, evaluating generated hypotheses remains a challenge for trustworthy AI-enabled scientific workflows. Existing approaches often use LLMs as judges or rely on semantic similarity, which can favor familiar ideas over novel ones. We propose a logit-based energy scoring method that evaluates hypotheses using a language model's intrinsic confidence rather than comparative judgment. We benchmarked seven la...
  </details>

- **2026-08-18** — Yihang Chen, Pin Qian, Su Wang et al. — [Explicit State Elicitation Is Not Enough: A Controlled Audit of Memory-Policy Classification](http://arxiv.org/abs/2608.17247v1)
  <details><summary>📄 Abstract</summary>
  Personalized agents must decide whether retrieved user memory should be used, ignored, updated, or queried before it affects a current task. We use this setting to develop an empirical audit protocol for structured intermediate outputs: first audit dataset shortcuts, then isolate bundled prompt changes, check whether intermediate labels are answer-associated, test decomposed semantic evidence, and audit provider-level execution failures. A 480-example synthetic development set initially suggeste...
  </details>

- **2026-08-18** — Oussama Ziadi, Abdelilah Rochd, Samir Idrissi Kaitouni et al. — [Safe Deep Reinforcement Learning for Energy-Efficient HVAC Control in Multi-Zone Residential Buildings](http://arxiv.org/abs/2608.17235v1)
  <details><summary>📄 Abstract</summary>
  HVAC systems represent a major share of building energy consumption. Traditional control strategies are limited in coordinating energy-comfort tradeoffs across multiple zones simultaneously. Reinforcement learning (RL) offers adaptive, data-driven control that optimizes performance over time. However, deploying learned neural network controllers in safety-critical building systems remains challenging due to lack of formal safety guarantees. We propose a safety-certified deep RL framework for mul...
  </details>

- **2026-08-18** — Amir Arsalan Nematollahi, Shayan Ahmadi, Mehdi Tale Masouleh et al. — [Iterative Grasp Pose Refinement: A Deep Reinforcement Learning Approach for 2D Vision](http://arxiv.org/abs/2608.17628v1)
  <details><summary>📄 Abstract</summary>
  Developing robots capable of understanding and manipulating objects requires compact, interpretable, and generalizable representations. This work proposes a reinforcement learning-based framework for robotic grasp refinement, integrating keypoint-based object representations with a Deep Q-Network (DQN). Using 2D overhead images captured in a simulated environment, a geometric-based algorithm generates initial grasp candidates, which are iteratively refined by the proposed framework, transforming...
  </details>

- **2026-08-18** — Dohoon Park, Seungyun Han, Hyun-Woo Lee — [Intra-atomic magnetic octupoles and their coupling to cluster magnetic octupoles in Chiral antiferromagnets Mn$_3$Sn](http://arxiv.org/abs/2608.17461v1)
  <details><summary>📄 Abstract</summary>
  We demonstrate that Mn$_3$Sn hosts finite intra-atomic magnetic octupoles (AMOs) $\mathbf{o}$ in addition to the well-established cluster magnetic octupole (CMO) $\mathbf{O}$. In contrast to the cluster-scale CMO, the AMO is a site-localized magnetic multipole associated with the anisotropic intra-atomic spin density. Symmetry analysis shows that the CMO and AMO transform in the same representation, allowing a bilinear interaction of the form $-g\,\mathbf{O}\cdot\mathbf{o}$. Using first-principl...
  </details>

- **2026-08-18** — Hoda Yamani, Yuning Xing, Koen van Rijnsoever et al. — [Repetition as Reinforcement: Enhancing Sample Efficiency via Instant Episode Repetition in Reinforcement Learning](http://arxiv.org/abs/2608.17347v1)
  <details><summary>📄 Abstract</summary>
  Repetition is a fundamental mechanism in human learning, where revisiting successful experiences strengthens memory, consolidates skills, and improves future performance. Motivated by this biological principle, we introduce Instant Episode Repetition (IER), a simple and novel mechanism that improves sample efficiency by immediately repeating action sequences from successful episodes during environment interaction. Unlike conventional approaches such as Experience Replay and Self-Imitation Learni...
  </details>

- **2026-08-18** — Iryna Hartsock, Cesar Lam, Christopher Otteni et al. — [Multi-Agent AI System for Radiology Report Structuring and Quality Assurance with Independent Radiologist Evaluation](http://arxiv.org/abs/2608.18072v1)
  <details><summary>📄 Abstract</summary>
  Purpose: To develop and evaluate a locally deployed multi-agent AI system for radiology report structuring and quality assurance. Materials and Methods: This retrospective study included 638 radiology reports from CT examinations of the chest, abdomen, and pelvis dictated by 15 board-certified radiologists in 2023 and 2024. A multi-agent AI pipeline was developed to perform report structuring and quality assurance (QA). The system structured the report into standardized anatomical sections at th...
  </details>

- **2026-08-18** — Andrew Wack — [CLOPS: Benchmarking System Speed at Utility Scale](http://arxiv.org/abs/2608.18044v1)
  <details><summary>📄 Abstract</summary>
  As quantum processors scale to hundreds of qubits, execution speed is a critical performance dimension alongside scale and quality. While substantial progress has been made in benchmarking circuit fidelity, existing speed metrics often fail to reflect the sustained, end-to-end throughput experienced by users running utility-scale workloads. This shortfall is especially pronounced for layered, parameterized circuits executed repeatedly within classical-quantum workflows, such as variational algor...
  </details>

- **2026-08-18** — Nour Shaheen, Junwei Ma, Alex Labach et al. — [Understanding the Surprising Generalization Properties of Tabular Foundation Models](http://arxiv.org/abs/2608.17957v1)
  <details><summary>📄 Abstract</summary>
  Tabular Foundation Models (TFMs) increasingly rely on in-context learning, where a model receives labelled examples at inference time and predicts labels for new inputs without updating its weights. Existing TFMs are typically trained on either massive synthetic corpora or very large collections of real datasets. In contrast, we show that surprisingly strong transfer can emerge from self-supervised pre-training on just a single real table. In this setting, we also find that tables tend to be eit...
  </details>

- **2026-08-18** — Jianyu Sun, Zhenxuan Zhang, Guang Yang et al. — [PerFact: Perception-Derived Fact Prompting for 3D Brain MRI Report Generation](http://arxiv.org/abs/2608.17926v1)
  <details><summary>📄 Abstract</summary>
  Radiology report generation has matured almost entirely on 2D chest radiographs, where the default route to better reports is a larger backbone or a pre-training one on medical data. We revisit that assumption on 3D multi-sequence brain MRI, a volumetric multi-disease regime, and find that the model is not the lever. Zero-shot medical and radiology vision-language models transfer poorly to brain MRI, with chest radiograph specialists failing most conspicuously, and five backbones fine-tuned iden...
  </details>

- **2026-08-18** — Fahad Ahammed, Omar Faruq Shikdar, Navid Zaman et al. — [AppendiGrade: An XAI-Enhanced Deep Learning Framework for Grading Appendicitis in Ultrasound with Gaussian Blur and Grad-CAM](http://arxiv.org/abs/2608.17923v1)
  <details><summary>📄 Abstract</summary>
  Appendicitis is one of the most common abdominal emergencies worldwide and requires prompt diagnosis and treatment to prevent life-threatening conditions. However, accurately differentiating complicated cases, such as perforation or abscess formation, from uncomplicated appendicitis remains a significant clinical challenge. Among other methods, ultrasound is a safer and more cost-efficient diagnostic technique because of the lack of radiation exposure. In this research, an advanced system capabl...
  </details>

- **2026-08-18** — Zheling Tan, Jin Gao, Dequan Wang — [CABLE: Extending the Reach of Memory Retrieval via Complementary Antecedent-Based Linking and Expansion](http://arxiv.org/abs/2608.17911v1)
  <details><summary>📄 Abstract</summary>
  As LLM agents operate across structured workflows and sessions, preserving long-term history does not ensure that later contexts can recover relevant evidence through a bounded memory interface. We study this evidence-reachability problem in long-term conversational memory, where retrieval still relies heavily on semantic similarity. This works well for topical recall, but it often misses earlier experiences, plans, or motivations that are semantically distant from the later events they help exp...
  </details>

- **2026-08-18** — Franky Kevin Nando Tezoh, Ali Hussaini Umar, Alessandro Laio et al. — [BayesPrompt: human readable prompts that make sense](http://arxiv.org/abs/2608.17866v1)
  <details><summary>📄 Abstract</summary>
  Reconstructing prompts that can elicit a desired answer or behaviour in an LLM is an open and important research topic. Optimisation methods which aim at minimising the perplexity of a given answer, however, consistently yield so-called pseudoprompts, unintelligible strings of tokens which can lack human interpretability. We argue that this is a consequence of the ill-posedness of the prompt optimisation task. By reframing the task as a Bayesian posterior inference over prompts, we propose an ef...
  </details>

- **2026-08-18** — Camilla Dalerci, Thilo Michael, Robin Schaefer et al. — [From Global Benchmarks to Local Evaluations: Benchmarking LLMs for the German Public Sector](http://arxiv.org/abs/2608.17827v1)
  <details><summary>📄 Abstract</summary>
  Public institutions face a persistent challenge in selecting LLMs suited to their specific context. Existing benchmarks, however, are of limited use as they primarily reflect English-language and US-centric settings, and often only evaluate task performance. In this paper, we present first results of MÖVE, a holistic evaluation framework for the German public sector, examining three rarely considered governance dimensions: energy consumption, provider transparency, and knowledge of German-party ...
  </details>

- **2026-08-18** — Alona Strugatski, Licol Zeinfeld, Jason Cooper et al. — [Interpretable Humans, Alien LLMs: Expert Analysis of Latent Structures in Assessment Responses](http://arxiv.org/abs/2608.17810v1)
  <details><summary>📄 Abstract</summary>
  The evaluation of large language models (LLMs) relies heavily on human-designed assessments, implicitly assuming that AI and humans employ similar underlying cognitive constructs. Challenging this assumption, we investigate whether the latent factors governing LLM performance carry the same substantive, human-interpretable meaning as the cognitive constructs governing human learners. Using responses from humans and six LLMs across quantitative reasoning and chemistry assessments, we conducted Ex...
  </details>

- **2026-08-18** — Lu Liu, Chi Xie, Xi Xiong — [Offline Multi-Agent Reinforcement Learning with a Physics-Informed World Model for Cooperative Mixed Traffic Control](http://arxiv.org/abs/2608.17739v1)
  <details><summary>📄 Abstract</summary>
  This study investigates cooperative control of connected and automated vehicles (CAVs) at partially observable highway bottlenecks in mixed traffic, aiming to mitigate congestion without relying on complete global traffic states or online trial-and-error. We propose a physics-informed world model-based offline multi-agent reinforcement learning framework that reconstructs a physically interpretable global traffic state from local CAV observation-action histories, with coupled macroscopic-microsc...
  </details>

- **2026-08-18** — Matthew T. Ford, Francis Bahk, Jingjing Wang et al. — [LLM-Derived Preference Judgments Are Not Self-Consistent](http://arxiv.org/abs/2608.17644v1)
  <details><summary>📄 Abstract</summary>
  Agents increasingly interpret a person's natural-language preferences by querying an LLM for numerical preference judgments, e.g., by asking how much the person would be willing to pay for an item. A growing body of work estimates a utility function from these judgments and then chooses actions based on their estimated utility. This pipeline assumes the judgments are approximately self-consistent: that a single utility function can reproduce them. But are they? To study this question, we measure...
  </details>

- **2026-08-18** — Ram Rachum, Yotam Amitai, Bálint Gyevnár et al. — [Evaluating RL Explainability Methods by How Much They Help Fix Bugs in Agents](http://arxiv.org/abs/2608.17524v1)
  <details><summary>📄 Abstract</summary>
  This preliminary paper outlines a planned evaluation benchmark for Explainable Reinforcement Learning (XRL) methods. Current evaluations rely on functionally-grounded metrics like faithfulness and compactness, and on human-grounded proxies like subjective ratings or prediction accuracy. We suggest evaluating XRL methods by how effectively their generated explanations help to diagnose and fix malfunctioning reinforcement learning (RL) agents. We propose EvalXRL, a benchmark in which a Large Langu...
  </details>

- **2026-08-18** — Noam Berkovich Lahav, Oren Wiezel, Yizhar Or — [Optimal control of a swimming robot based on Purcell's microswimmer model](http://arxiv.org/abs/2608.17455v1)
  <details><summary>📄 Abstract</summary>
  Purcell's swimmer is a well-known planar model of a swimming microorganism, governed by low Reynolds number hydrodynamics, which is comprised of three rigid links connected by actuated rotary joints. This model has been analyzed as a robotic locomotion system governed by first-order nonlinear dynamics with a periodic input (gait) of the two joint angles. In this work, we present a robotic macro-scale realization of this three-link swimmer moving in a highly viscous fluid. We propose a simple var...
  </details>

- **2026-08-18** — Xiaoduo Li, Quan Gu — [GSToken: Geometry-Structured Gaussian Tokens for Compact 3D Medical Image Representation](http://arxiv.org/abs/2608.17425v1)
  <details><summary>📄 Abstract</summary>
  Effective segmentation of multi-modal MRI is central to improving neural network accuracy in brain tumor recognition. Existing methods typically compress 3D volumes into token sequences via fixed patch encoding or learned attention pooling (e.g., TokenLearner). However, these compression schemes discard explicit spatial shape information; the resulting tokens convey no notion of lesion morphology or spatial extent. Meanwhile, end-to-end evaluation entangles a tokenizer's information retention wi...
  </details>

- **2026-08-18** — Jan C Olivier, Etienne Barnard — [Finite-range Lattice Momentum Operators for Quantum Field Theory](http://arxiv.org/abs/2608.17327v1)
  <details><summary>📄 Abstract</summary>
  We propose a Z-transform framework for the analysis and synthesis of finite range lattice momentum operators in quantum field theory. In this formulation, translation-invariant lattice operators are represented as functions of the complex variable $z$ in the unit circle, allowing their spectral properties to be analyzed using tools from digital signal processing and rational approximation theory.   Within this framework, the fermion doubling problem is reinterpreted as the appearance of unwanted...
  </details>

- **2026-08-18** — Jie Gu, Tingting Wang, Hongrun Gao et al. — [Reconfiguration-Complete Motion Primitives with Constructive Planning for Deformable Planar Modular Robots](http://arxiv.org/abs/2608.17324v1)
  <details><summary>📄 Abstract</summary>
  The continuously deformable geometry of modular robots makes it difficult to define a fixed representation for reconfiguration planning and analysis. This letter introduces a square-cell abstraction that maps deformable rhombus modules to fixed-size grid cells while retaining physically interpretable local motions through two primitives, pivoting and shearing. Under this abstraction, we prove that every non-straight edge-connected configuration with $N \geq 7$ can be transformed to a fixed canon...
  </details>

- **2026-08-18** — Zhikai Ding, Ziyi Ye — [Understanding Curriculum Learning in Large Language Models via Cross-Difficulty Optimization Dynamics](http://arxiv.org/abs/2608.17268v1)
  <details><summary>📄 Abstract</summary>
  Curriculum learning has been widely adopted in the post-training of large language models by organizing training data from easy to hard. However, its effectiveness varies substantially across reasoning tasks, suggesting that no single curriculum is universally optimal and raising a fundamental question: what determines when curriculum learning works? In this paper, we answer this question by analyzing the optimization dynamics induced by different curriculum schedules. We show that the transfer ...
  </details>

- **2026-08-17** — Andrew Stuart, Florian Wolf — [Expressivity In Multimodal Contrastive Learning](http://arxiv.org/abs/2608.17203v1)
  <details><summary>📄 Abstract</summary>
  Contrastive learning has become a cornerstone of modern representation learning, powering CLIP-style models that underpin text-to-image generation, vision-language models, and retrieval across a rapidly growing range of modalities. Despite this empirical success, the expressive power of these architectures remains poorly understood. To gain insight, we study expressivity by adopting a population-level, density-estimation viewpoint: each architecture comprises a parameterized set of densities who...
  </details>

- **2026-08-17** — Jianan Zhou, Jung-Hoon Cho, Tianyue Zhou et al. — [Task Specialization Fine-Tuning for Contextual Reinforcement Learning](http://arxiv.org/abs/2608.17180v1)
  <details><summary>📄 Abstract</summary>
  Contextual Reinforcement Learning (CRL) seeks to generalize classical RL by maximizing task coverage across a context space of related tasks. While prior works often train from scratch and rely on either multi-task learning for a single policy or strategically training multiple policies, we advocate for a unified alternative: pretraining a single policy with good initial performance, followed by fine-tuning multiple policies for task specialization. This new paradigm, however, introduces unique ...
  </details>

- **2026-08-17** — Amogh Raina, Ilias Chalkidis, Daniel Hershcovich et al. — [Can LLMs Reason in a Legally Meaningful Manner? A Small-scale Study on European Court of Human Rights Cases](http://arxiv.org/abs/2608.17168v1)
  <details><summary>📄 Abstract</summary>
  Reasoning has become a standard technique and feature for contemporary LLMs; however, its application and quality in the context of demanding legal-oriented tasks, such as legal case forecasting, remain under explored. We investigate how LLMs reason in the context of legal case forecasting, using legal cases from the European Court of Human Rights (ECtHR) as a testbed. We evaluate OpenAI GPT 5.4, a recent top-tier LLM, by exploring alternative prompting strategies that are more or less suggestiv...
  </details>

- **2026-08-17** — Tuan-Binh Tran, Dat Nguyen Cong, Duc-Trong Le et al. — [SCENARIODIFF: A Scenario-level Guidance Framework for Multimodal Time Series Forecasting--Extended Version](http://arxiv.org/abs/2608.17164v1)
  <details><summary>📄 Abstract</summary>
  Textual context such as news, reports, and logs can provide valuable signals for time series forecasting, especially when future dynamics are driven by external events that are not yet visible in historical values. Existing multimodal forecasting methods often either ask large language models (LLMs) to predict numerical values directly or fuse text and time series implicitly, making contextual influence difficult to interpret and control. We propose SCENARIODIFF, a hierarchical contextual reason...
  </details>

- **2026-08-17** — Elnaz Rabieinejad, Ali Dehghantanha, Fattane Zarrinkalam et al. — [Beyond the Hype: Evaluating LLM Integration and Practical Limitations in Security Operation Centers](http://arxiv.org/abs/2608.17154v1)
  <details><summary>📄 Abstract</summary>
  Large Language Models (LLMs) are increasingly being explored within Security Operation Centers (SOCs) to support text-heavy analytical work such as alert contextualization, incident summarization, and drafting investigative artifacts. Despite this interest, practitioners describe critical operational concerns, most notably hallucinations (plausible but incorrect outputs), opaque reasoning, and the verification effort required to safely use model-generated content in security workflows. In this p...
  </details>

- **2026-08-17** — Yoonjoo Lee, Hyoungwook Jin, Tae Soo Kim et al. — [KnowSim: Evaluating Information Calibration in LLM Assistants with User Simulators that Learn](http://arxiv.org/abs/2608.17150v1)
  <details><summary>📄 Abstract</summary>
  To effectively collaborate with users on knowledge-intensive tasks, Large Language Models (LLMs) must perform information calibration: matching content to a user's evolving understanding and cognitive capacity. Yet user simulators used to evaluate and train LLMs do not explicitly model user knowledge so they neither produce realistic interactions across knowledge levels nor reflect how interactions unfold as that knowledge evolves. To close this gap, we introduce KNOWSIM, an evaluation framework...
  </details>

- **2026-08-17** — Disha Kamale, Dmitry Berenson — [PDDL-ART: Autonomous Symbolic Abstraction From Demonstration For Long-Horizon Robotic Manipulation Using Vision-Language Models](http://arxiv.org/abs/2608.17146v1)
  <details><summary>📄 Abstract</summary>
  Symbolic planning with PDDL offers a principled framework for long-horizon robot manipulation, but constructing accurate PDDL domain and problem descriptions remains a significant bottleneck, typically requiring substantial domain expertise. We present a Vision-Language Model (VLM)-based approach called PDDL-ART, a framework that autonomously generates task-specific PDDL domain and problem descriptions from a single expert demonstration, a natural language task description, and a library of avai...
  </details>

- **2026-08-17** — Hadeer Elashhab, Sai Srijan Papineni, Marvin Dorn et al. — [Deep Learning for Cross-Border Electricity Price Forecasting: A Comparative Study](http://arxiv.org/abs/2608.17091v1)
  <details><summary>📄 Abstract</summary>
  While publicly available electricity market data presents a valuable resource for forecasting research, the field lacks established benchmark datasets for standardized comparison. As a result, many studies have relied on different datasets and metrics to evaluate methods in isolated settings, making it difficult to assess progress and compare state-of-the-art approaches consistently. In this work, we use public data to evaluate deep learning models for electricity price forecasting (EPF) across ...
  </details>

- **2026-08-17** — Yunfan Gao, Xinyi Huang, Tao Sheng et al. — [J-Miner: Recovering Executable Decision Knowledge from Language-Model Classifiers](http://arxiv.org/abs/2608.17063v1)
  <details><summary>📄 Abstract</summary>
  Large language models can be fine-tuned into specialized classifiers that perform well across diverse text tasks and make complex judgments, but they typically expose only final labels, leaving the decision knowledge acquired through fine-tuning implicit within the model. We study how to mine this internal decision knowledge from a fine-tuned classifier and encode it in an executable representation that can be inspected, validated, and reused beyond the source classifier. We introduce J-Miner, w...
  </details>

- **2026-08-17** — Daniel Palacios, Matthew Brady Neeley, Angel Adetomike Otto et al. — [Institution-Specific LLM Prompting Recovers PHI That De-identification Systems and Their Gold Standards Both Miss](http://arxiv.org/abs/2608.17051v1)
  <details><summary>📄 Abstract</summary>
  Secondary use of electronic health records requires de-identification, yet existing systems miss \emph{institutionally situated} protected health information (PHI) such as hospital abbreviations, building names, and internal codes whose status is locally determined. We ask whether large language models (LLMs) with in-context learning (ICL) can close this gap and control the precision--recall trade-off.   On 100 annotated pediatric oncology notes (5,322 PHI spans) from Texas Children's Hospital, ...
  </details>

- **2026-08-17** — Wei Jiang, Junru Li, Kai Zhang et al. — [BiCRVC: An Efficient Bidirectional Neural Video Compression Framework via Coupled Representation Coding](http://arxiv.org/abs/2608.16175v2)
  <details><summary>📄 Abstract</summary>
  Neural video compression (NVC) has achieved strong compression performance, but practical random-access coding still faces two technical challenges: existing bidirectional NVCs (BVCs) usually require costly motion-first decoding, and reliable motion estimation is difficult under long-range bidirectional prediction. To address these issues, we present BiCRVC, an efficient bidirectional neural video compression framework based on coupled representation coding. Instead of coding motion and frame in...
  </details>

- **2026-08-17** — Abel C. H. Chen — [Quantum-Safe Web Service Architecture Using Time-Based One-Time Passwords](http://arxiv.org/abs/2608.16961v1)
  <details><summary>📄 Abstract</summary>
  One-Time Passwords (OTPs) have become a common option for multi-factor authentication in several applications. For instance, during website login processes, OTPs are often used in conjunction with traditional text-based usernames and passwords to verify whether the access request originates from a legitimate human user rather than an automated agent. However, in scenarios involving automated connections and system-to-system interoperability, Time-Based One-Time Passwords (TOTPs) may be required ...
  </details>

- **2026-08-17** — Perry Dong, Yueru Jia, Chelsea Finn et al. — [Q-Learning With World Models](http://arxiv.org/abs/2608.17163v1)
  <details><summary>📄 Abstract</summary>
  Off-policy reinforcement learning (RL) has become increasingly sample-efficient, enabling applications such as RL fine-tuning of Vision-Language-Action models into reliable, high-performing policies. World models offer a further lever for sample efficiency, as they predict state changes rather than actions alone, but their success has largely been confined to supervised policy learning. Prior model-based RL methods often optimize the policy or value function directly on imagined rollouts, which ...
  </details>

- **2026-08-17** — Vineet Bhat, Siyi Chen, Alex Zook et al. — [PROBE: Manipulation-Grounded Visual Question Answering with VLM Agents](http://arxiv.org/abs/2608.17129v1)
  <details><summary>📄 Abstract</summary>
  Vision-language Models (VLMs) excel at 2D grounding, spatial reasoning and agentic tool-based planning in static scenes. However, consider asking a home robot "Is my medication still in the cabinet?" The answer may be physically hidden behind a row of containers that must first be moved aside. Answering such questions in real-world cluttered environments requires reasoning in dynamic scenes: distractors must be manipulated to reveal occluded objects, and each action changes the scene the model m...
  </details>

- **2026-08-17** — Maciej Wodziński, Joanna Wodzińska, Kacper Dudzic et al. — [Language Models Reproduce Human Reductionist Bias and Decision Inconsistency in Neurodevelopmental Disorders Assessment](http://arxiv.org/abs/2608.17105v1)
  <details><summary>📄 Abstract</summary>
  Large language models (LLMs) are increasingly supporting complex mental-health decisions, which depend not only on factual evidence but also value-laden interpretations. We introduce a mixed-methods human-LLM auditing framework examining decision consistency, susceptibility to cognitive heuristics, declarative intellectual humility, and the concepts operationalized in support-allocation judgments of neurodevelopmental disorders. Comparing 35 humans (18 physicians and 17 psychologists) with seven...
  </details>

- **2026-08-17** — Hai Xia, Carlos Ansótegui, Stefan Szeider — [Synthesizing Feature Extractors: An Agentic Approach for Algorithm Selection](http://arxiv.org/abs/2608.17170v1)
  <details><summary>📄 Abstract</summary>
  Algorithm selection for constraint satisfaction problems requires extracting features that capture problem structure. Manually designing feature extractors demands deep domain expertise and quickly becomes a bottleneck when new problem classes appear. We present an automated approach that uses Large Language Models (LLMs) in an agentic check--fix--verify loop to synthesize executable Python scripts that act as interpretable, problem-specific feature extractors. Given a high-level MiniZinc model ...
  </details>

- **2026-08-17** — Zhiyuan Yuan, Guanying Chen, Lingteng Qiu et al. — [PXDepth: Pixel-Space Modeling for Structure Preserving Monocular Depth Estimation](http://arxiv.org/abs/2608.16984v1)
  <details><summary>📄 Abstract</summary>
  Recent monocular depth estimators achieve strong zero-shot generalization, yet often struggle to preserve fine-grained structures and object boundaries. We attribute this limitation to the prevalent combination of large-patch ViT encoders and convolutional decoders, as coarse tokenization can weaken pixel-level cues that upsampling cannot fully recover. To address this issue, we propose PXDepth, a discriminative monocular depth model that separates global context modeling from pixel-level depth ...
  </details>

- **2026-08-17** — Kejia Zhang, Youran Sun, Xinyu Ren et al. — [AutoSR: Automatic Symbolic Regression by Searching Research States](http://arxiv.org/abs/2608.16876v1)
  <details><summary>📄 Abstract</summary>
  We introduce Automatic Symbolic Regression (AutoSR), a fully automated system that instantiates Research-Space Symbolic Regression by searching persistent scientific investigations rather than isolated equations. Finite, noisy data often yield numerically competitive expressions that imply very different behavior outside the observed regime, making numerical fit and syntactic complexity insufficient measures of scientific credibility. Existing approaches largely focus on improving expressions, y...
  </details>

- **2026-08-17** — Weiliang Chen, Haowen Sun, Jun Gao et al. — [HarnessEval-W: Agentifying the Evaluation of Visual Worlds](http://arxiv.org/abs/2608.16859v1)
  <details><summary>📄 Abstract</summary>
  A benchmark should deliver more than a scalar score: what makes an evaluation trustworthy is the reasoning that justifies the score. This is especially critical for world models, where judging a rollout requires understanding whether physics, causality, and world state evolve correctly. Humans spot such violations naturally, yet no existing benchmark automates this capability: metrics are computed brute-force, leaving no reasoning chain that can be examined or verified. We introduce HarnessEval-...
  </details>

- **2026-08-17** — Langzhe Gu, Chengkai Hou, Meng Li et al. — [HAF: Adapting Generalist VLAs to Humanoid Whole-Body Loco-manipulation via Hierarchical Action Flow and Spectral Latent RL](http://arxiv.org/abs/2608.16837v1)
  <details><summary>📄 Abstract</summary>
  Humanoid robots hold great promise as general-purpose agents in human-centered environments, yet generalist vision-language-action (VLA) foundation models are not readily applicable to humanoid whole-body loco-manipulation. The high dimensionality and interdependence of humanoid motions make it challenging for conventional single-stage VLA architectures to coordinate locomotion, waist posture, and dual-arm manipulation effectively. Moreover, policies trained through offline behavior cloning can ...
  </details>

- **2026-08-17** — Steve Brown — [Quipu: A Governed Bitemporal Knowledge Graph Store](http://arxiv.org/abs/2608.16813v1)
  <details><summary>📄 Abstract</summary>
  Agents now write knowledge graphs, but knowledge-graph stores still carry defaults set when humans curated them: accept writes now and clean later, keep one time axis or none, treat every writer's facts as equally trustworthy, and leave governance to dashboards and middleware. These four defaults are individually convenient and jointly untenable under agent workloads. We present Quipu, an embeddable store that inverts all four: no fact enters except through a gate whose predicates evaluate the p...
  </details>

- **2026-08-17** — Hongyue Yu, Kefan Li, Jiakun Li et al. — [TDD-Agent: Test-Driven Reasoning for Code Generation](http://arxiv.org/abs/2608.16742v1)
  <details><summary>📄 Abstract</summary>
  Large Language Models (LLMs) have achieved remarkable progress in code generation, yet ensuring correctness in complex, repository-level tasks remains challenging. Existing approaches often use generated tests as static post-hoc validators, which limits their ability to guide implementation and may introduce misleading feedback when the tests themselves are incomplete or incorrect. In this paper, we introduce TDD-Agent, which operationalizes the test-driven development paradigm for code generati...
  </details>

- **2026-08-17** — Rudolf L. M. van Herten, Robert Graf, Paula Feldman et al. — [GeoPose: Patient-agnostic CTA-to-DSA registration through projection-space calibration](http://arxiv.org/abs/2608.16600v1)
  <details><summary>📄 Abstract</summary>
  Aligning intraoperative biplanar digital subtraction angiography (DSA) to pre-procedural computed tomography angiography (CTA) requires rapid and accurate 3D-to-2D registration. Optimization-based methods are sensitive to initialization and may require hundreds of iterations, whereas learning-based approaches commonly rely on patient-specific training. We propose GeoPose, a population-trained framework that estimates the C-arm pose in a learned canonical frame and transfers it to the native fram...
  </details>

- **2026-08-17** — Tianqi Xiang, Qixiang Zhang, Xinpeng Ding et al. — [CACSurv: Concordance-Aligned Comparative Learning with Large Language Models for Cancer Survival Prediction](http://arxiv.org/abs/2608.16594v1)
  <details><summary>📄 Abstract</summary>
  Cancer survival prediction supports treatment planning, risk stratification, and follow-up management. Existing methods use structured clinical variables, whole-slide images, genomic profiles, or multimodal inputs, while patient reports remain underexplored. We study report-centric survival prediction using reports that organize pathological, clinical, and molecular evidence. Large language models (LLMs) can reason over such reports, but case-wise time regression introduces two mismatches. First...
  </details>

- **2026-08-17** — Kuo Zhan, Peilin Xin, Yingqi Zhao et al. — [Physics-Aligned Deep Learning Enables SERS Resolving and Sequencing of Dynamic Single-Molecule DNA Oligomers in Plasmonic Nanocavity](http://arxiv.org/abs/2608.16576v1)
  <details><summary>📄 Abstract</summary>
  Single-molecule surface-enhanced Raman spectroscopy (SM-SERS) captures dynamic molecular behavior with ultrahigh sensitivity, but its biopolymer analysis is hindered by strong spectral heterogeneity, transient hotspot sampling, and background interference. Here, we develop a physics-aligned deep learning framework integrating contrastive attention-based multiple-instance learning (CAMIL), a tri-channel multi-kernel CNN classifier, and trajectory-level transition-guided sequence reconstruction to...
  </details>

- **2026-08-17** — Timon Böhler, Simon Daniel, David Richter et al. — [Mechanizing Choreographic Programs and Hoare Logic with State Transformers](http://arxiv.org/abs/2608.16346v1)
  <details><summary>📄 Abstract</summary>
  Choreographic programming is a programming model for developing distributed applications where an entire communication protocol is written as a single program, which a compiler then projects to one process per participant. Choreographic programming abstracts over low-level network communication primitives such as sockets, and provides a high degree of safety guarantees with deadlock freedom ensured by construction. Mechanizing choreographies necessarily deals with both operations specific to dis...
  </details>

- **2026-08-17** — Diptesh Kanojia, Archchana Sindhujan, Sourabh Deoghare et al. — [IndicQE-APE: A Benchmark for Quality Estimation and Automatic Post-Editing for Indic Languages](http://arxiv.org/abs/2608.16344v1)
  <details><summary>📄 Abstract</summary>
  Indic quality estimation (QE) and automatic post-editing (APE) data is spread across separate releases, so no single resource supports training and evaluation across tasks and language pairs on one footing. We consolidate the WMT 2020--2024 shared-task lineage with an extended English--Malayalam resource into \indicqe: $126{,}754$ instances over nine directional pairs, with up to four label types aligned on the same segment, a direct assessment, a human post-edit, word-level OK/BAD tags and an e...
  </details>

- **2026-08-17** — Changhui Sun, Lanbo Liu, Hang Lei et al. — [Step-Level On-Policy Distillation: Interpolating Between On-Policy Distillation and Supervised Fine-Tuning](http://arxiv.org/abs/2608.16333v1)
  <details><summary>📄 Abstract</summary>
  On-policy distillation (OPD) aligns a student model with a teacher's logit distribution on student-generated trajectories. This approach has achieved strong empirical gains and can often surpass conventional off-policy distillation with substantially less data. However, standard token-level OPD can provide only fragmented corrections along an erroneous student trajectory and cannot unfold a complete and correct repair path. Motivated by this limitation, we propose \emph{Step-Level On-Policy Dist...
  </details>

- **2026-08-17** — Simon Ellershaw, Christopher Tomlinson, Zeljko Kraljevic et al. — [Foresight-England: Development of a National-Scale Generative AI Model of Electronic Health Records for Medical Event Prediction across the COVID-19 Pandemic](http://arxiv.org/abs/2608.16273v1)
  <details><summary>📄 Abstract</summary>
  Foresight-England (Foresight-E) is the first national-scale generative foundation model of electronic health records (EHRs), developed as a research pilot strictly for COVID-19 research. We evaluated its ability to model the direct and indirect effects of the pandemic. Trained from scratch entirely within the NHS England Secure Data Environment, Foresight-E is a 243-million-parameter transformer decoder. It was trained and evaluated on de-identified, longitudinal EHRs of approximately 61 million...
  </details>

- **2026-08-17** — Junqi Liu, Yufan He, Yexiao He et al. — [BaT: Towards Self-Evolving Medical Research Agent with Stage Rubrics](http://arxiv.org/abs/2608.16211v1)
  <details><summary>📄 Abstract</summary>
  Long-horizon agents are beginning to automate complete workflows that produce code, reports, and research artifacts. Medical imaging workflows are multi-stage and data-sensitive, while expert trajectories remain scarce and difficult to share. Structured benchmarks can localize failures through stage-level rubrics, but standard post-training discards these diagnostics before the next training round. We present Benchmark-as-Teacher (BaT), a recursive self-improvement system for agent post-training...
  </details>

- **2026-08-17** — Wei Jiang, Junru Li, Kai Zhang et al. — [BiCRVC: An Efficient Bidirectional Neural Video Compression Framework via Coupled Representation Coding](http://arxiv.org/abs/2608.16175v1)
  <details><summary>📄 Abstract</summary>
  Neural video compression (NVC) has achieved strong compression performance, but practical random-access coding still faces two technical challenges: existing bidirectional NVCs (BVCs) usually require costly motion-first decoding, and reliable motion estimation is difficult under long-range bidirectional prediction. To address these issues, we present BiCRVC, an efficient bidirectional neural video compression framework based on coupled representation coding. Instead of coding motion and frame in...
  </details>

- **2026-08-17** — Fengji Ma, Yan Rong, Xu Li et al. — [ACE-Cap: Active Evidence Acquisition via Agentic Co-Evolution for Long-Paragraph Fine-Grained Audio Captioning](http://arxiv.org/abs/2608.16162v1)
  <details><summary>📄 Abstract</summary>
  Long-paragraph fine-grained audio captioning requires models to recover diverse acoustic facts while avoiding omissions and unsupported details. However, prevailing captioners remain passive one-shot generators: once a detail is overlooked, they cannot identify the evidence gap, query the audio for targeted information, or decide when sufficient evidence has been collected. We formulate this task as active evidence acquisition and introduce Agentic Co-Evolution for Captioning (ACE-Cap). The fram...
  </details>

- **2026-08-17** — Ruiyao Xu, Tiankai Yang, Wei-Chieh Huang — [HyperSkill: Self-Evolving LLM Agents via Hypergraph-Structured Skill Memory](http://arxiv.org/abs/2608.16114v1)
  <details><summary>📄 Abstract</summary>
  As agentic tasks grow in complexity, LLM agents increasingly rely on experiential memory to reuse procedural knowledge across tasks. Effective memory design must jointly address what to store, how memory is structured and retrieved, and how memory evolves. Existing systems tackle each only partially: they store trajectories, insights, or workflows as isolated entries, discarding compositional relationships among subtasks and reusable skills; retrieve by flat embedding similarity that ignores rel...
  </details>

- **2026-08-17** — Taegang Kim, Saleh Afroogh, Junfeng Jiao — [SafeGesture: Evaluating Fine-Grained Hand Gesture Understanding in Vision-Language Models through Scenario-Conditioned Safety Interpretation](http://arxiv.org/abs/2608.16081v1)
  <details><summary>📄 Abstract</summary>
  Open-weight and frontier vision-language models (VLMs) perform well on general image understanding, but their ability to interpret fine-grained hand gestures in safety-critical operational contexts remains largely unexamined. We introduce SafeGesture, a benchmark that evaluates whether a model can infer scenario-appropriate safety actions from hand gestures. It pairs six HaGRID gestures with eight operational scenarios for 4,800 items and evaluates Qwen2.5-VL-7B, LLaVA-NeXT-7B, InternVL2-8B, Phi...
  </details>

- **2026-08-17** — Nneka Hyman, Jasmine Khan, Raj Korpan — [Benchmarking Identity-Sensitive LLM Outputs for Surveillance and Security Robots](http://arxiv.org/abs/2608.16030v1)
  <details><summary>📄 Abstract</summary>
  Large language models (LLMs) are increasingly used to generate textual robot design specifications, interaction policies, and risk assessments during early-stage robot development. Such outputs may influence how surveillance and security robots are conceptualized, documented, and ultimately implemented. This paper evaluates whether identity-conditioned prompts produce systematic differences in LLM-generated surveillance and security robot design descriptions. Using 236 demographic identity label...
  </details>

- **2026-08-17** — Wenbo Li, Dai Shen, Shengping Gong — [Dual-Thrust Switching Analytical Guidance Algorithm for Powered Landing with Attitude Smoothness Optimization](http://arxiv.org/abs/2608.16000v1)
  <details><summary>📄 Abstract</summary>
  Traditional numerical guidance methods for powered landing of reusable rockets are typically constrained by high computational complexity and inadequate real-time performance. Moreover, insufficient consideration of attitude smoothness often induces severe fluctuations in control commands; meanwhile, most existing approaches are tailored for single-thrust scenarios, failing to accommodate the guidance requirements of multi-engine thrust switching. To mitigate these limitations, this paper propos...
  </details>

- **2026-08-17** — Anik Jha — [Whose Gold? Annotator-Pool Disagreement Is Large at the Item Level, and Hidden by Small Leaderboards](http://arxiv.org/abs/2608.15980v1)
  <details><summary>📄 Abstract</summary>
  Preference benchmarks are built by hiring annotators, and the identity of those annotators is treated as an implementation detail. We measure what that detail buys. On the 2,885 MultiPref items where both pools are internally unanimous, so no tie-breaking convention is consulted at all, expert and crowd annotators assign a different majority label to 23.6% and name the opposite winner on 9.2%; on the 246 comparably unanimous MT-Bench cells, benchmark authors and recruited experts differ on 30.5%...
  </details>

- **2026-08-17** — Bingxin Xu, Yuzhang Shang, Emilio Ferrara — [Don't Drop the BATON: Long-Horizon Robot Manipulation via Agentic Subtask Exploration and Transition-aware Memory](http://arxiv.org/abs/2608.16889v1)
  <details><summary>📄 Abstract</summary>
  Long-horizon robot manipulation chains many contact-rich skills into one multi-stage task. Vision-language-action (VLA) models increasingly master the individual skills, yet the chain still fails: errors compound beyond the policy's ability to correct, and one subtask silently constrains the next. A promising recipe freezes the VLA and puts an LLM agent in charge: it plans in language, moves in free space with analytic primitives, invokes the VLA only for contact-rich segments, and writes adapta...
  </details>

- **2026-08-17** — Xiaowei Cai, Yunuo Cai, Bingao Chen et al. — [$τ_0$-VLA: a Hierarchical Robot Foundation Model with World-Model-Guided Test-Time Computation](http://arxiv.org/abs/2608.16885v1)
  <details><summary>📄 Abstract</summary>
  Long-horizon robot manipulation requires a robot to both execute individual skills reliably and sequence them coherently over extended tasks. Most hierarchical vision-language-action (VLA) models make each such decision with a single forward pass, leaving no mechanism to allocate additional computation to difficult or consequential choices. We introduce $τ_0$-VLA, a hierarchical robot foundation model that formulates high-level subtask generation as a compute-scalable inference problem through w...
  </details>

- **2026-08-17** — Haris Aziz, Simon Mackenzie, Mashbat Suzuki — [Anchoring for Truthfulness: The Random-Anchor Volume Mechanism for Multi-Facility Location](http://arxiv.org/abs/2608.16550v1)
  <details><summary>📄 Abstract</summary>
  We study the strategyproof placement of \(k\) facilities on the real line for \(n\) agents who privately report their locations, without monetary transfers. For two facilities, the Proportional Mechanism of Lu, Sun, Wang, and Zhu (2010) is strategyproof in expectation and achieves a constant-factor approximation to the optimal social cost. Whether such a guarantee is possible for three facilities in the standard model, where each agent is served by her nearest open facility, has remained open.  ...
  </details>

- **2026-08-17** — Yifan Lu, Xiaopeng Yuan, Haohan Wang — [Beyond Asking: A Pipeline for Personalized Game Generation that Reads Players from Behavior](http://arxiv.org/abs/2608.16196v1)
  <details><summary>📄 Abstract</summary>
  Personalized game generation requires inferring a player's abilities and behavioral style from how they play. Large language models have made this inference more attainable than ever: an LLM can read a raw gameplay transcript and produce a fluent, plausible profile of the player. Plausible, however, is not verified, and verification is precisely what the field lacks: latent traits are unobservable; questionnaires provide noisy proxies and become circular when self-reports are used to validate be...
  </details>

- **2026-08-17** — Xinyu Zhou, Zikun Cai, Kuangji Zuo et al. — [Unified Condition-Action Modeling for Accurate One-Step Action Generation](http://arxiv.org/abs/2608.16153v1)
  <details><summary>📄 Abstract</summary>
  Robot manipulation requires policies that are both accurate and efficient, as robot control must respond to changing observations under tight latency constraints. Recent diffusion and flow policies are promising, but they often treat conditions as auxiliary signals rather than jointly evolving them with action trajectories. We find that this limitation can be effectively mitigated by a \textbf{simple yet effective unified condition-action modeling design} that represents conditions and actions i...
  </details>

- **2026-08-17** — Serena Su, Yifan Wang, Senwei Liang — [Data-Efficient and Interpretable Classification of Circulating Tumor Cell Phenotypes in Microfluidic Devices via Deep Learning](http://arxiv.org/abs/2608.16870v1)
  <details><summary>📄 Abstract</summary>
  Accurate classification of circulating tumor cell (CTC) phenotypes can provide valuable information for assessing metastatic potential. Label free microfluidic devices provide a hydrodynamic obstacle course that transforms subtle biophysical characteristics of CTCs, including size and deformability, into distinct kinematic trajectories. However, the highly nonlinear fluid structure interactions governing these trajectories make the inverse problem of inferring cellular phenotype from trajectory ...
  </details>

- **2026-08-17** — Amos Muench, Jonathan Thielmann, Reduan Achtibat et al. — [Concept-based explanation of gene expression prediction from H&E images](http://arxiv.org/abs/2608.16669v1)
  <details><summary>📄 Abstract</summary>
  Recent advances in pathology foundation models have enabled accurate prediction of spatial transcriptomics (ST) from routine H&E images. However, existing explainability methods for vision transformer (ViT)-based models are largely limited to local heatmaps and do not reveal how morphological concepts contribute to ST predictions. Here, we introduce an explainable framework that combines relevance propagation and concept discovery to link transcriptional programs to tissue morphology. We develop...
  </details>

- **2026-08-17** — Anna Shalova — [Random Quadratic Form with random forcing: Metastable synchronization by noise](http://arxiv.org/abs/2608.16664v1)
  <details><summary>📄 Abstract</summary>
  We study the Random Quadratic Form (RQF) on a sphere in the presence of random Brownian forcing. We show that the forcing does not effectively change the law of the process but affects the synchronization properties of the system. While the RQF without forcing exhibits partial synchronization due to the intrinsic symmetries, the introduction of an arbitrarily small forcing results in long-term symmetry breaking and leads to full synchronization.   In this work we focus on the small forcing regim...
  </details>

- **2026-08-17** — Yusuke Takahashi, Kyle Wild, Asako Uraki — [Cost Scales with Change, Not Corpus Size: Incrementally Maintaining an Evolving Semantic Substrate](http://arxiv.org/abs/2608.16621v1)
  <details><summary>📄 Abstract</summary>
  Retrieval-augmented and agentic question-answering systems increasingly re-derive the meaning of a corpus at query time. Put plainly, instead of re-deriving what a corpus means on every question, the work is done once when a document arrives and is thereafter merely consulted -- a compiler, not an interpreter, of meaning. An alternative is to compile that meaning once, at ingest time, into a compact, queryable semantic substrate and maintain it as the corpus evolves. The central objection is mai...
  </details>

- **2026-08-17** — Tassio Sirqueira, Jessica Faciroli — [The Specification Paradox: Rethinking Requirements Engineering in the Age of AI](http://arxiv.org/abs/2608.16618v1)
  <details><summary>📄 Abstract</summary>
  The growing adoption of Large Language Models (LLMs) in Software Engineering has reinforced the expectation that coding activities can be largely automated. However, this perception may represent yet another historical search for a solution capable of eliminating the inherent challenges of software development. This article discusses the transition from a code-centered paradigm to Specification-Driven Development. We argue that artificial intelligence reduces some of the effort associated with w...
  </details>

- **2026-08-17** — Anima Kujur, Zahra Monfared — [Learning Generalizable Reconstruction of High-Dimensional Neural Dynamics](http://arxiv.org/abs/2608.16569v1)
  <details><summary>📄 Abstract</summary>
  Accurate reconstruction of long-duration neural recordings is challenging because local field potentials (LFPs) are high-resolution, multichannel, transient, and variable across subjects. We present PCA-DMD, a scalable operator-theoretic framework that segments LFP recordings into overlapping windows, projects them into a compact PCA space, learns linear Koopman evolution in the latent space, and reconstructs continuous signals through inverse projection and overlap-add aggregation. On 200,000-s...
  </details>

- **2026-08-17** — Clemens Schächter, Astrid Pechmann, Janbernd Kirschner et al. — [Large language models as synthetic clinical experts to inform longitudinal rare-disease modeling](http://arxiv.org/abs/2608.16507v1)
  <details><summary>📄 Abstract</summary>
  Due to the limited amount of information, modeling longitudinal rare-disease data can benefit from integrating clinical knowledge. Yet, elicitation of expert knowledge and formalization for model fitting is challenging, in particular due to limited time of clinical experts. To nevertheless make domain knowledge accessible during model fitting, we use large language models (LLMs) as synthetic clinical experts to supervise a variational-autoencoder-based approach that learns low-dimensional latent...
  </details>

- **2026-08-17** — Kasumi Ban — [Computational KJ-Ho: An Analyst-Bias-Free Insight Extraction Framework from Large-Scale Qualitative Data Using Domain-Specialized LLMs](http://arxiv.org/abs/2608.16467v1)
  <details><summary>📄 Abstract</summary>
  The qualitative research methodologies that underpin consumer-insight generation - the KJ method, Grounded Theory, and Thematic Analysis - share a structural constraint: the cognitive processing capacity of the human analyst. Replication research further shows that conclusions vary substantially across analysts analyzing identical data (analyst bias). This paper proposes Computational KJ-Ho (the Kawakita Jiro method), a theoretical framework that computationally realizes the KJ method's epistemo...
  </details>

- **2026-08-17** — Zhenchao Tang, Xiaogang Xu, Tianxu Lv et al. — [PertMind: Eliciting Emergent Biological Reasoning in LLM via Reinforcement Learning on Cellular Perturbation Data](http://arxiv.org/abs/2608.16419v1)
  <details><summary>📄 Abstract</summary>
  Large language models can describe mechanisms, yet scalable post-training still depends on costly, manually curated biological reasoning traces. Here we show that cellular perturbation atlases can instead become reinforcement-learning environments, where measured gene responses provide computable rewards for biological reasoning. We introduce PertMind, which combines trusted-trajectory supervised initialization with gene-, pathway-, and format-level reinforcement signals. Trained only on forward...
  </details>

- **2026-08-17** — Hao Zhang, Longrong Yang, Lunhao Duan et al. — [D2-ScaleAgent: Dual-Dimensional Scaling for Long Document Understanding](http://arxiv.org/abs/2608.16417v1)
  <details><summary>📄 Abstract</summary>
  Multi-modal retrieval-augmented generation (RAG) is a key technique for visually rich long document understanding. Existing multi-modal RAG methods are progressively advancing toward multi-agent systems: they first retrieve relevant pages based on a query, and then iteratively understand information within those pages. However, these methods typically rely on fixed workflows and lack the ability to dynamically scale computation at test time, often leading to insufficient evidence. To address thi...
  </details>

- **2026-08-17** — Xiangfan Wu, Zonghao Ying, Huiyu Wu et al. — [Ventor-QTest: Threat-Model-Driven Verification of Vendor-Hosted LLM APIs](http://arxiv.org/abs/2608.16391v1)
  <details><summary>📄 Abstract</summary>
  As large language models become increasingly widespread, third-party providers that deploy open-weight models have become an important part of the ecosystem. Auditing the quality of their inference APIs is therefore an open problem. We formalize hosted model routing as a stochastic process and propose \mbox{\textbf{Ventor-QTest}}, a composite black-box audit that requires no probability information from the target API. Its repeated-request component sends each frozen constrained context to the t...
  </details>

- **2026-08-17** — Javier Sivianes, Enrique Boquete-Someso, Daniel Hernangómez-Pérez et al. — [Optical Response Beyond Magnetic Symmetries](http://arxiv.org/abs/2608.16368v1)
  <details><summary>📄 Abstract</summary>
  The optical response of magnetic materials is conventionally classified through magnetic space groups (MSGs), where spin and lattice are locked by the relativistic spin-orbit interaction. However, most optical observables are governed primarily by nonrelativistic physics, and thus a purely MSG-based description can overlook important insights. Here we systematically show that spin-space groups (SSGs), which operate at the nonrelativistic level, provide a broader and more predictive framework for...
  </details>

- **2026-08-17** — Marina Lepp, Joosep Kaimre — [Revisiting the Performance of Generative Artificial Intelligence on Introductory Object-Oriented Programming Assessments: Insights from 2026](http://arxiv.org/abs/2608.16318v1)
  <details><summary>📄 Abstract</summary>
  Recent advances in Generative Artificial Intelligence (GenAI) have substantially improved the ability of large language models (LLMs) to generate and explain source code. However, their performance on authentic object-oriented programming (OOP) assessments remains insufficiently understood. This study evaluates five widely used GenAI systems, ChatGPT-5.2, DeepSeek-V3, Gemini 2.5 Flash, Claude Sonnet 4.5, and M365 Copilot, using programming tests and examination tasks from an introductory univers...
  </details>

- **2026-08-17** — Kristina Šekrst, Ana Kovačić — [Clause Encounters of the Third Kind: Can LLMs Replace Language Teachers?](http://arxiv.org/abs/2608.16286v1)
  <details><summary>📄 Abstract</summary>
  While various organizations now actively encourage LLM use in classrooms, we still lack rigorous, systematic evaluations of how well these models actually perform the fundamental tasks of language pedagogy. This paper examines whether state-of-the-art LLMs can deliver the kind of corrective feedback and methodological explanations that language learners need. The study tests multiple large language models on their ability to identify, correct, and explain common learner mistakes in English, by s...
  </details>

- **2026-08-17** — Pengfei Jia, Jingjian Wang, Jingmao Li et al. — [Decoupled Temporal Encoding for Generative Recommendation](http://arxiv.org/abs/2608.16274v1)
  <details><summary>📄 Abstract</summary>
  Positional encoding is a fundamental component of Transformer-based generative recommendation models, where user histories are modeled as autoregressive item sequences. Most positional encoding methods are inherited from natural language processing and mainly represent discrete item order. However, recommendation sequences go beyond ordered lists, as timestamps and temporal effects also shape item relations. Our work is motivated by a real-world food delivery and instant retail recommendation sy...
  </details>

- **2026-08-17** — Alexandros A. Voudouris — [Group-Fair Metric Distortion of Facility Assignment Problems](http://arxiv.org/abs/2608.16252v1)
  <details><summary>📄 Abstract</summary>
  We study the group-fair distortion of metric facility assignment problems, where a set of agents, partitioned into unknown groups, must be assigned to a collection of facilities, possibly subject to capacity or other feasibility constraints. Given an assignment, each agent incurs a cost that depends on both its distance to its assigned facility and, via an affinity factor, the average distance of the other members in its group to their assigned facilities. We consider full-information algorithms...
  </details>

- **2026-08-17** — Dejun Zhang, Yanzi Bai, Yiqi Wu — [PCT-Prompt: A Prompt-Guided Transformer Framework for Dense Prediction Tasks in Point Clouds](http://arxiv.org/abs/2608.16225v1)
  <details><summary>📄 Abstract</summary>
  Standard Transformers have proven effective in point cloud object classification, but their performance in dense prediction tasks within complex scenes is often hindered by weak prior assumptions. To address this challenge, we propose PCT-Prompt, a novel framework that enhances standard Transformers by introducing a prompt-guided feature branch to improve performance in dense prediction tasks. The standard Transformer branch leverages pre-trained models for global feature extraction from point c...
  </details>

- **2026-08-17** — Kangning Yin, Kaige Liu, Zhe Cao et al. — [RoboStriker: Latent-Space Strategic Games for Autonomous Humanoid Boxing](http://arxiv.org/abs/2608.16195v1)
  <details><summary>📄 Abstract</summary>
  Achieving human-level competitive intelligence and physical agility in humanoid robots remains a profound challenge, particularly in contact-rich and highly dynamic tasks such as boxing. While Multi-Agent Reinforcement Learning offers a principled framework for strategic interaction, its direct application to unstructured raw motor spaces inevitably leads to joint-level physical collapse, preventing the emergence of any viable combat tactics. To resolve this fundamental conflict between strategi...
  </details>

- **2026-08-17** — Kwan Yun, Serin Yoon, Sunjin Jung et al. — [AnyTalk: Speech Animation for Arbitrary Characters Leveraging a Video Generation Model](http://arxiv.org/abs/2608.16143v1)
  <details><summary>📄 Abstract</summary>
  We present AnyTalk, a novel method for generating 3D speech animations for arbitrary characters without requiring any animation data. While existing audio-driven 3D speech animation methods rely on character-specific training data or laborious rigging/re-meshing, AnyTalk circumvents these limitations by leveraging recent video diffusion models trained on extensive video datasets. We first adapt a pre-trained video diffusion model to a target character through our Character-specific Fine-tuning (...
  </details>

- **2026-08-17** — Owen Tang, Alexandra Vassar, Jake Renzella — [Mitigating AI Risks in Computing Education via LLM-Driven Lecture Video Curation](http://arxiv.org/abs/2608.16131v1)
  <details><summary>📄 Abstract</summary>
  This study evaluates the effectiveness of utilising large language models (LLMs) to retrieve targeted segments from delivered video recordings to answer student questions in introductory programming environments. By restricting AI to identifying existing, educator-verified media rather than generating open-ended text, this approach aims to mitigate common pedagogical risks such as generative hallucinations and cognitive bypassing. We benchmarked three distinct models, two proprietary (Gemini 3.1...
  </details>

- **2026-08-17** — Haris Aziz, Bo Li — [On the Incompatibility of Weighted PROPX and Pareto Optimality for Indivisible Chores](http://arxiv.org/abs/2608.16130v1)
  <details><summary>📄 Abstract</summary>
  Proportionality (PROP) is one of the simplest fairness criteria for allocating items among agents with additive preferences. With indivisible chores, however, PROP is not always satisfiable. We study proportionality up to any item (PROPX), which requires every agent to satisfy proportionality after any chore is removed from her bundle. Under strictly positive costs, we settle the weighted compatibility question negatively: weighted PROPX and Pareto optimality are incompatible already for two age...
  </details>

- **2026-08-17** — Yike Yuan, Virum Ranka, Tina Lasisi et al. — [Walk Before You Run: The Importance of Data Exploration for Data Analysis Agents](http://arxiv.org/abs/2608.16045v1)
  <details><summary>📄 Abstract</summary>
  LLM-based data-analysis tools are increasingly used to help users analyze messy spreadsheets and workbooks, from answering questions over uploaded files to generating code, summaries, and visualizations. These systems are often evaluated by the correctness of their final downstream answers. However, reliable data analysis also depends on an earlier step: understanding what the dataset contains before solving the requested task. For complex workbooks, this Data Exploration step includes identifyi...
  </details>

- **2026-08-17** — Eric Xie, Wenqian Ye, Aidong Zhang — [ALPS: Measuring Valid Creativity in Large Language Models with Mathematical Construction](http://arxiv.org/abs/2608.15979v1)
  <details><summary>📄 Abstract</summary>
  Large language models produce outputs presented as discoveries - new proofs, conjectures, or molecules. Whether such an output that appears creative is truly original and effective is hard to establish: open-ended outputs require subjective judgment, the output may replicate something seen in training, or the task may be too simple to need creativity. We present ALPS (Austin-Law Proof-Synthesis), a benchmark that designs a task to measure valid creativity: producing a solution that is original a...
  </details>

- **2026-08-17** — Qinyou Wang — [Fiber Fingerprints of Hidden Learning-State Dynamics](http://arxiv.org/abs/2608.15976v1)
  <details><summary>📄 Abstract</summary>
  A learning system can occupy execution states that are indistinguishable under every declared present-behavior readout yet respond differently to future training. We formalize this through fiber fingerprints: controlled future-learning response laws restricted to present-behavior equivalence classes. Prefix-compatible finite probes induce a predictive quotient functor, a Nerode-type minimal recursively sufficient representation, and a canonical set-level predictive fiber without assuming smoothn...
  </details>

- **2026-08-16** — Steven Wallace, William D. Harcourt, Richard Hann et al. — [CrevasseSeg: A Label-Efficient UAV Crevasse Segmentation Framework](http://arxiv.org/abs/2608.15790v2)
  <details><summary>📄 Abstract</summary>
  Crevasse mapping from uncrewed aerial vehicle (UAV) imagery matters for glaciological research and for field safety in glaciated terrain. Yet, pixel-level annotation of glacier surfaces is costly and requires domain experts. We introduce CrevasseSeg, a framework for binary segmentation over the terminus of Borebreen, Svalbard, comprising 1,938 unlabelled UAV orthomosaic tiles for self-supervised/unsupervised fine-tuning, 24 labelled tiles for validation and 176 labelled tiles for testing. Using ...
  </details>

- **2026-08-16** — Guijia Zhang, Harry Yang — [Aborted but Not Forgotten: KV-Cache Retention Breaks Rollback Consistency in Language Agents](http://arxiv.org/abs/2608.15939v1)
  <details><summary>📄 Abstract</summary>
  Stateful language agents assume a rejected branch can be taken back by clearing it from the application transcript. We show this breaks when the serving session retains key/value (KV) state across the logical abort: the model can continue attending to content the application believes it discarded. We formalize the missing guarantee as rollback consistency: a complete abort must restore the state the model attends, not just the transcript. The key failure is cross-layer: a correct logical rollbac...
  </details>

- **2026-08-16** — William Kalikman, Šimon Sukup, Michal Tešnar et al. — [Augmenting Text to Increase Translation Difficulty](http://arxiv.org/abs/2608.15932v1)
  <details><summary>📄 Abstract</summary>
  As state-of-the-art machine translation models saturate standard benchmarks, the field needs more challenging evaluations to distinguish between models of varying quality. We propose augmenting existing benchmarks to increase translation difficulty by combining adversarial optimization with a differentiable translation difficulty estimator. Our Adversarial Translation Optimization (ATO) uses gradients from a combined difficulty and fluency objective to iteratively replace tokens. Because each st...
  </details>

- **2026-08-16** — Yogesh Kumar — [Catching Hallucinated Citations in Video-LLM Question Answering: A Self-Verification Pipeline and Verifier Ablation Study](http://arxiv.org/abs/2608.15574v1)
  <details><summary>📄 Abstract</summary>
  Video question answering systems built on vision-language models often produce timestamped claims with high confidence even when unsupported by the cited frame. This deceptive hallucination arises because timestamps imply grounding without ensuring correctness, increasing user trust but not accuracy. We introduce a pipeline that closes this loop. A retrieval-augmented language model drafts answers with per-claim timestamp citations, and each cited frame is independently re-examined before being ...
  </details>

- **2026-08-16** — Junbo Jacob Lian, Huiling Chen, Hanzhang Qin et al. — [Admission Without Answers: Label-Free Certification and Experience Learning for LLM-Based Optimization Modeling](http://arxiv.org/abs/2608.15565v1)
  <details><summary>📄 Abstract</summary>
  Experience-learning agents for optimization modeling improve by storing verified skills, but existing learners admit knowledge by checking against known answers, which real ticket streams do not provide. The natural label-free alternatives are unreliable: on a 300-problem label-blind stream, admitting every executable model poisons roughly one admission in four, while single-instance agreement accepts models that match at one value but differ elsewhere. We propose AdmitOR, an admission gate buil...
  </details>

- **2026-08-16** — Roman Neruda, Martin Bakoš, Josef Šlerka et al. — [Large Language Models as Implicit Sociological Models: Reconstructing Voting Behaviour from Sociodemographic Profiles](http://arxiv.org/abs/2608.15871v1)
  <details><summary>📄 Abstract</summary>
  Large language models (LLMs) trained on large-scale internet corpora encode extensive statistical regularities about social identities, attitudes, and political behaviour. This paper introduces and evaluates a methodological framework that leverages these latent representations to reconstruct aggregate voting behaviour from individual-level sociodemographic profiles. We operationalize LLMs as implicit sociological models by conditioning them on demographic descriptions, eliciting probabilistic t...
  </details>

- **2026-08-16** — Steven Wallace, William D Harcourt, Richard Hann et al. — [CrevasseSeg: A Label-Efficient UAV Crevasse Segmentation Framework](http://arxiv.org/abs/2608.15790v1)
  <details><summary>📄 Abstract</summary>
  Crevasse mapping from uncrewed aerial vehicle (UAV) imagery matters for glaciological research and for field safety in glaciated terrain. Yet, pixel-level annotation of glacier surfaces is costly and requires domain experts. We introduce CrevasseSeg, a framework for binary segmentation over the terminus of Borebreen, Svalbard, comprising 1,938 unlabelled UAV orthomosaic tiles for self-supervised/unsupervised fine-tuning, 24 labelled tiles for validation and 176 labelled tiles for testing. Using ...
  </details>

- **2026-08-16** — Xiaohan Zhang, Feng Gu, Xudong Rao et al. — [ChainSpace: A Chained-Reasoning Paradigm for Spatial Intelligence](http://arxiv.org/abs/2608.15788v1)
  <details><summary>📄 Abstract</summary>
  Spatial intelligence requires foundation models to maintain coherent spatial state across interactions with the physical world. However, existing data-centric approaches typically treat spatial reasoning as independent question-answer instances, enabling shortcut-based answering and providing limited supervision for persistent spatial understanding. To address this, we introduce ChainSpace, a chained-reasoning paradigm that structures spatial reasoning as a state-preserving multi-round process. ...
  </details>

- **2026-08-16** — Yiqi Liu, Yang Wang, Songxin Wang et al. — [Broken Symmetry in LLM Refusal: Answer Release Is More Local Than Refusal Restoration](http://arxiv.org/abs/2608.15772v1)
  <details><summary>📄 Abstract</summary>
  When a language model refuses to answer a prompt, it is unclear whether the correct answer is erased from its internal representations, or merely suppressed at the output layer. We investigate this mechanism using a controlled withhold setting, which yields perfectly matched answering and refusal trajectories for bidirectional activation patching. We uncover a causal asymmetry in intervention locality under matched causal interventions, which we term broken symmetry. Even when a model generates ...
  </details>

- **2026-08-16** — Luoyuan Shi, Yuanzhao Zhai, Dawei Feng et al. — [An Empirical Study on the Impact of Normalized Use-Case Specifications on Traceability](http://arxiv.org/abs/2608.15726v1)
  <details><summary>📄 Abstract</summary>
  Traceability link recovery between requirements and source code is vital for software quality assurance and evolution analysis. Although automated traceability techniques have advanced greatly, the large semantic gap between vague natural-language requirements and precise source code still hinders accurate link recovery. Most existing approaches optimize traceability algorithms yet ignore the inherent quality of requirement descriptions, which prevents fundamental reduction of the semantic gap. ...
  </details>

- **2026-08-16** — Pouya Ghiasnezhad Omran, Michael Zimmermann, Duncan Cambridge et al. — [Agent Gym: A Framework for Continuous Evaluation and Evolution of LLM Agents Through Human-in-the-Loop Feedback](http://arxiv.org/abs/2608.15591v1)
  <details><summary>📄 Abstract</summary>
  Large Language Model (LLM) agents deployed in production environments face a fundamental tension: the agent's behavior is frozen at deployment time, while the business rules and edge cases it must handle continue to evolve. Existing approaches address agent construction and one-time evaluation but provide no structured mechanism for continuous post-deployment behavioral correction without modifying the agent's source code. Most of the approaches offered in the market, require intense collection ...
  </details>

- **2026-08-16** — Xiao Wang, Lu Dong, Ifeoma Nwogu et al. — [MistyPilot: Enabling Social-Robot Control through Multi-Agent LLM Skill Orchestration](http://arxiv.org/abs/2608.15549v1)
  <details><summary>📄 Abstract</summary>
  Programming small social robots from natural-language instructions requires more than invoking isolated APIs. Interactive tasks combine reactive physical behaviors with stateful social behaviors, while existing interfaces often require developers to manually compose APIs into skills, configure their parameters, bind sensor events to skills, and manage task states at runtime. We present MistyPilot, a multi-agent LLM framework that interprets high-level natural-language instructions and orchestrat...
  </details>

- **2026-08-16** — Sahil Shah, S P Sharan, Harsh Goel et al. — [CrossView: Can Vision-Language Models Reason Across Cameras?](http://arxiv.org/abs/2608.15539v1)
  <details><summary>📄 Abstract</summary>
  Video understanding benchmarks have long centered on single-camera settings, where modern multi-modal language models achieve strong performance across image and video tasks. Yet, the real world runs on multi-camera networks: autonomous vehicles, security systems, and robots all gather data across many simultaneous views. We argue that this is not simply "more" of the single-camera problem; it is fundamentally different. Multi-camera reasoning requires handling context that scales with the numbe...
  </details>

- **2026-08-16** — Junqing Lin, Jingwei Sun, Zhengding Hu et al. — [FlashQuant: Sparse-Dense Fusion for Memory-Efficient Outlier-Aware LLM Inference](http://arxiv.org/abs/2608.15531v1)
  <details><summary>📄 Abstract</summary>
  Low-bit quantization reduces the memory footprint and computational cost of large language model (LLM) inference. However, high-magnitude outlier weights can induce substantial quantization errors and degrade model accuracy. Outlier-aware quantization addresses this issue by retaining outliers in high precision while quantizing the remaining weights, resulting in a low-bit dense GEMM path and a high-precision sparse SpMM path. Existing implementations execute these paths in separate GPU kernels,...
  </details>

- **2026-08-16** — Sarthak Kamat, Adam Rashid, Satvik Sharma et al. — [Pre-training Visual Dexterity in Simulation](http://arxiv.org/abs/2608.15917v1)
  <details><summary>📄 Abstract</summary>
  Large-scale pre-training has made robot policy fine-tuning increasingly data-efficient, but this progress has largely been driven by datasets and embodiments built around simple parallel-jaw grippers. Dexterous, multi-fingered hands remain comparatively data-starved because real teleoperation is costly to scale, while human hand video is off-embodiment and requires lossy pose estimation and retargeting. We introduce Simulation Pre-training for Dexterity (SPD), a pre-training framework for dexter...
  </details>

- **2026-08-16** — Louise Demoor, Martí Jané-Ballarín, Pierre Nunn et al. — [Non-obvious Manipulability with Groups in Shapley-Scarf Housing Markets](http://arxiv.org/abs/2608.15631v1)
  <details><summary>📄 Abstract</summary>
  In Shapley-Scarf housing markets, Ma (1994) shows that top trading cycles (TTC) is the unique mechanism satisfying individual rationality (IR), Pareto efficiency (PE), and strategy-proofness. We ask what other mechanisms become possible when strategy-proofness is replaced by a weaker condition called non-obvious manipulability (NOM), introduced by Troyan and Morrill (2020). We first show that this weaker condition does not help on its own: every IR and PE mechanism is already NOM. We therefore i...
  </details>

- **2026-08-16** — Zesheng Yang, Lingling Zhang, Xinyu Zhang et al. — [GLaQ: Grounding Latent Queries in Visual Evidence for Multimodal Reasoning](http://arxiv.org/abs/2608.15517v1)
  <details><summary>📄 Abstract</summary>
  Chain-of-thought reasoning has substantially improved the problem-solving capabilities of multimodal large language models. Fine-grained visual evidence, however, remains difficult to preserve and reuse across text-based reasoning steps. To address this limitation, tool-augmented thinking-with-images methods maintain visual access externally by revisiting or manipulating the image, but require predefined tools and additional inference-time processing. As an internal alternative, continuous visua...
  </details>

- **2026-08-16** — Dinh-Khiet Le, Minh-Quyet Ha, Hong-Phuc Vu-Dinh et al. — [Crystal-structure design by agentic AI in a language of motifs](http://arxiv.org/abs/2608.15900v1)
  <details><summary>📄 Abstract</summary>
  Data-driven materials discovery interpolates more reliably than it extrapolates and seldom reaches new structure types. We present MatEvolve, an agentic-AI framework designing crystals, proposing each candidate with a stated rationale and testing it. The agent reasons in an interpretable \emph{language of motifs}, writing each crystal as a \emph{motif profile} that describes the recurring geometric patterns---the \emph{motifs}---composing it. The motif profile serves not merely as a description ...
  </details>

- **2026-08-16** — Yao Lu, Zhicheng Guo, Qijun Zhang et al. — [COOL: A Cooling-Aware Point Transformer Framework for Thermal Prediction in Advanced 3D/3.5D IC Packaging](http://arxiv.org/abs/2608.15890v1)
  <details><summary>📄 Abstract</summary>
  Advanced 3D and 3.5D IC packaging significantly improves integration density but elevates thermal management challenges due to cross-layer heat coupling and complex cooling structures. Traditional solvers deliver high fidelity but are too slow for iterative design flows, while existing learning-based methods either fail to capture inter-die thermal coupling or treat cooling structures as static components, limiting their applicability in real packaging co-design scenarios. In this work, we intro...
  </details>

- **2026-08-16** — Yutong Li, Yiwen Pan — [Lagrangian Schur index and Bethe ansatz type formula](http://arxiv.org/abs/2608.15878v1)
  <details><summary>📄 Abstract</summary>
  We propose a surprisingly elementary method to compute the Schur index in closed-form for general $\mathcal{N} = 2$ Lagrangian theories. The method is inspired by the Bethe ansatz type formula for $\mathcal{N} = 1$ superconformal index. We identify issues underlying the original derivation: the loss of periodicity property upon integration and the omitted poles outside of the annulus region. We circumvent the problems and transform integration into solving a simple difference equation. The final...
  </details>

- **2026-08-16** — Yuhao Zhang — [Exact MMS Allocations under Personalized Bivalued Valuations: Goods and Chores](http://arxiv.org/abs/2608.15822v1)
  <details><summary>📄 Abstract</summary>
  The maximin share (MMS) is a central fairness benchmark for allocating indivisible goods and chores. We study additive valuations in the personalized bivalued setting, where each agent assigns one of two agent-specific values to every item. Whether exact MMS allocations always exist in this setting has remained a major open question, as highlighted by Ebadian, Peters, and Shah and by Garg, Huang, and Segal-Halevi. We answer this question affirmatively: we prove that exact MMS allocations always ...
  </details>

- **2026-08-16** — Yonghe Sun, Zhenjia Liu, Hua Liao et al. — [Toward AI-Friendly Cartography: Understanding How Color Design Influences Foundation Model Spatial Reasoning on Sequential Choropleth Maps](http://arxiv.org/abs/2608.15736v1)
  <details><summary>📄 Abstract</summary>
  Foundation models (FMs) increasingly support multimodal and geospatial reasoning, yet it remains unclear whether cartographic principles designed for human perception are equally effective for machines. Focusing on sequential choropleth maps, we examine how hue palette, color ordering, and lightness contrast influence FM spatial reasoning. We construct a controlled benchmark of 5,760 maps and 28,800 questions spanning Attribute Identify, Spatial Recognition, Compare, Rank, and Pattern Delineate,...
  </details>

- **2026-08-16** — Uri Malamud, Shmuel Bialy, Benjamin Godard et al. — [Multiphase turbulence as the origin of OH+, H2O+ and H3+ column density scatter in the local ISM](http://arxiv.org/abs/2608.15633v1)
  <details><summary>📄 Abstract</summary>
  Observations of the reactive ions OH+, H2O+ and H3+ in the Galactic interstellar medium reveal large sight-line-to-sight-line scatter in their column densities, commonly interpreted as evidence for substantial variations in the cosmic-ray ionization rate (CRIR). We revisit this interpretation using high-resolution three-dimensional magneto-hydrodynamic simulations of the multiphase ISM with time-dependent chemistry for H, H2, H+ and electrons, building on the fiducial model of Godard et al. (202...
  </details>

- **2026-08-16** — Alona Strugatski, Licol Zeinfeld, Giora Alexandron — [Do Assessment Instruments Measure the Same Thing for Humans and LLMs? A Latent Structure Analysis](http://arxiv.org/abs/2608.15630v1)
  <details><summary>📄 Abstract</summary>
  The rapid development and growing deployment of large language models (LLMs) have made it increasingly important to understand their capabilities. A common approach is to evaluate LLMs using assessment instruments originally designed to measure skills and competencies in humans, such as standardized exams, and to use performance on these instruments as evidence for generalizable claims about LLMs' underlying abilities on the same skills the assessments are intended to measure in humans. However,...
  </details>

- **2026-08-16** — Qinghao Fu, Yarong Wang, Shunlei Ning et al. — [Who Leads Now? Token-Level Modality Arbitration for Chart-to-Code Generation](http://arxiv.org/abs/2608.15510v1)
  <details><summary>📄 Abstract</summary>
  Chart-to-code generation requires a model to read the fine-grained visual details of a chart and write executable code that reproduces it. Existing chart-to-code methods either train visual and coding abilities separately, or fine-tune on chart-to-code data with the two abilities entangled. Neither strategy accounts for the distinct nature of the two abilities or the interference that arises when they are optimized together. We propose MoCA (Mixture of Cross-modal Arbitration), which separates t...
  </details>

- **2026-08-15** — Farbod Tavakkoli, Roderic Paulk, Jorden Terrazas et al. — [OTel: Building Domain-Specialized Telecom LLM Foundations for Intelligent Networks](http://arxiv.org/abs/2608.15436v1)
  <details><summary>📄 Abstract</summary>
  Frontier AI models have advanced rapidly, but they still struggle with telecom-specific tasks. We present Open Telco (OTel), an open telecom AI resource with derived datasets for retrieval, reranking, instruction tuning, and safety/abstention, plus 30 full-parameter post-trained baselines across embedding, reranking, and language models. The community has already engaged substantially with the resource: as of May 3, 2026, the released models have been downloaded over 16 million times, and the pr...
  </details>

- **2026-08-15** — Yusuf Meric Karadag, Gulay Oklan, Seref Baris Cagliyan et al. — [CBX-Bench: A Human-Aligned MLLM Council for Benchmarking Concept Bottleneck Model Explanations](http://arxiv.org/abs/2608.15404v1)
  <details><summary>📄 Abstract</summary>
  Concept Bottleneck Models (CBMs) are designed to make visual classification interpretable by expressing predictions through human-understandable concepts. Although interpretability is the central motivation for CBMs, they are still largely evaluated as predictive models by downstream classification accuracy, supplemented by isolated qualitative examples. This highlights a pressing need for quantitative measures, a challenge complicated by the infeasibility of ground-truth concept annotation at s...
  </details>

- **2026-08-15** — Juseok Jeon, Ramy E. Ali, Doyun Kwon et al. — [FedPA-LoRA: Product-Aligned Framework for Mitigating Aggregation and Initialization Errors in Heterogeneous Federated LoRA](http://arxiv.org/abs/2608.15381v1)
  <details><summary>📄 Abstract</summary>
  Low-Rank Adaptation (LoRA) enables efficient federated fine-tuning of large language models, but its factorized parameterization creates a tension between accurate aggregation of local updates and continuity of locally optimized factors. Factor-wise aggregation incurs aggregation mismatch but better preserves factor continuity, whereas product-space reconstruction reduces this mismatch at the cost of greater factor-level initialization mismatch from newly reconstructed factors. We propose FedPA-...
  </details>

- **2026-08-15** — Mohammad Aref Jafari-Raddani, Morteza Mohajjel Kafshdooz — [SAPE: Sandwich Adapters for Parameter Efficiency in Large Language Model Fine-Tuning](http://arxiv.org/abs/2608.15360v1)
  <details><summary>📄 Abstract</summary>
  While Parameter-Efficient Fine-Tuning (PEFT) has substantially reduced the hardware cost of adapting Large Language Models (LLMs) by decreasing the number of trainable parameters, recent studies have sought to further improve PEFT through parameter sharing. However, these approaches either employ uniform parameter sharing across layers, which can delay convergence, or rely on dynamic masking strategies, which add computational overhead. The potential of sharing patterns inspired by the inherent ...
  </details>

- **2026-08-15** — Ziyue Yang, Chaolin Xu, Yijing Wang et al. — [ReasonCast: Agentic Demand Forecasting with Selective Semantic Reasoning](http://arxiv.org/abs/2608.15291v1)
  <details><summary>📄 Abstract</summary>
  Demand forecasting increasingly requires combining two complementary sources of information: historical sales reveal recurring numerical dynamics, while future promotions, holidays, price changes, and platform interventions provide forward-looking knowledge. Existing text-enhanced forecasting methods often encode such context into generic representations and fuse it uniformly with time-series features, without explicitly distinguishing which semantic effects are forecast-relevant or how they sho...
  </details>

- **2026-08-15** — Yihong Ji, Jinsong Zhang, He Hu et al. — [HOIMask: Towards Generative Masked Modeling for Human Object Interaction Generation](http://arxiv.org/abs/2608.15141v1)
  <details><summary>📄 Abstract</summary>
  Diffusion-based methods have dominated the HOI generation, as they enable critical contact fusions or signals to guide the diffusion process. However, they often result in high artifacts and unstable interaction quality due to error accumulation during iterative denoising. In this work, we propose HOIMask, the first generative masked framework for modeling HOI motion in discrete space. HOIMask first encodes both motion sequences and contact-aware signals into discrete 2D human and object token m...
  </details>

- **2026-08-15** — Varvara Arzt, Allan Hanbury, Terra Blevins — [Left-Branching Transformers Excel at Right-Branching Languages: Data Shapes Word Order Preferences in Language Models](http://arxiv.org/abs/2608.15129v1)
  <details><summary>📄 Abstract</summary>
  We systematically compare word order preferences in decoder-only language models across 192 artificial languages and typologically diverse natural languages. On artificial languages, models exhibit a left-branching preference that aligns with neither natural language universals nor human word order learning biases. On natural languages, monolingual models show no clear base word order bias at small scales, but as data grows, a preference for right-branching subject-verb-object (SVO) languages em...
  </details>

- **2026-08-15** — Haoxiang Luo, Bang Huang, Mohamed-Slim Alouini — [Agentic AI-Enabled Solar-Powered High-Altitude Platforms for Sustainable SAGINs](http://arxiv.org/abs/2608.15087v1)
  <details><summary>📄 Abstract</summary>
  Space-Air-Ground Integrated Networks (SAGINs) can extend connectivity, but their communication, computing, and platform operations create tightly coupled energy demands. Solar-powered High-Altitude Platforms (HAPs) offer a promising middle layer by combining persistent regional coverage, renewable-energy harvesting, and onboard computing. However, realizing this potential requires more than optimizing individual links or processors, as radio transmission, task execution, backhaul use, and batter...
  </details>

- **2026-08-15** — Tianxin Wei, Zhan Shi, Minhua Lin et al. — [Evo-Harness: Context-to-Harness Skill Compilation for Self-Evolving Agents](http://arxiv.org/abs/2608.15071v1)
  <details><summary>📄 Abstract</summary>
  Learning from experience is critical for developing capable, self-improving large language model (LLM) agents. Existing methods typically extract knowledge from accumulated trajectories via reflection, memory, rules, or skills. However, agents in realistic environments continuously encounter novel tasks, often offering only a one-shot opportunity to improve. These executions yield rich but highly noisy contexts, entangling broadly useful lessons with task-specific artifacts. Critically, prior wo...
  </details>

- **2026-08-15** — Yiming Fu, Fangjun Li, Xiujin Liu et al. — [NumerosityVLM: A Cognitively Inspired Benchmark for Interpreting Numerosity Representations in Vision-Language Models](http://arxiv.org/abs/2608.15425v1)
  <details><summary>📄 Abstract</summary>
  Vision-language models (VLMs) achieve strong performance on high-level multimodal tasks, yet numerosity perception, a cognitive ability that emerges in human infants before language acquisition, remains poorly understood in current models, as existing counting benchmarks entangle numerosity with correlated visual factors. We introduce a cognitively inspired diagnostic benchmark, NumerosityVLM, comprising 10,800 synthetic images across six controlled conditions. The benchmark orthogonally manipul...
  </details>

- **2026-08-15** — Jiaqi Hu, Junwen Huang, Hongli Xu et al. — [SOS! : A Streamlined Object-Conditional Transformer for Model-free Segmentation](http://arxiv.org/abs/2608.15295v1)
  <details><summary>📄 Abstract</summary>
  Foundation segmentation models excel at generating high-quality, class-agnostic masks, but they struggle to associate these proposals with specific target objects. This semantic gap severely hinders their deployment in downstream applications like robotic manipulation, which demand precise unseen objects segmentation. Existing approaches attempt to resolve this by relying on exhaustive 3D object model priors, inherently introducing prohibitive computational overhead and complex, multi-stage pipe...
  </details>

- **2026-08-15** — Yufei Guo, Yinan Wu, Haoran Duan et al. — [PhaseLoRA: Control-Regime-Conditioned Low-Rank Adaptation for Continuous-Action Vision-Language-Action Policies](http://arxiv.org/abs/2608.15285v1)
  <details><summary>📄 Abstract</summary>
  Parameter-efficient fine-tuning (PEFT) is a natural way to adapt pretrained vision-language-action (VLA) policies, but most adapter designs apply temporally static updates throughout a control rollout, overlooking the phase-dependent nature of continuous-action manipulation. Such policies traverse distinct regimes, including approach, contact transition, grasping, transport, and placement, each requiring different adaptation behaviors. We propose \textbf{PhaseLoRA}, a lightweight LoRA parameteri...
  </details>

- **2026-08-15** — André Oliveira, João Victor Monteiro, Vânia Neves et al. — [On the Influence of Refactoring Types on Merge Effort](http://arxiv.org/abs/2608.15384v1)
  <details><summary>📄 Abstract</summary>
  Modern software development involves parallel work and concurrent changes, requiring code merging. Prior studies report that 10% to 20% of merge attempts result in conflicts, often requiring manual intervention. The literature explores factors that generate conflicts, including refactorings, but does not analyze how individual refactoring types influence the manual effort required to resolve them. We analyzed 64 open-source Java projects and applied association rule mining to measure the strengt...
  </details>

- **2026-08-15** — Tien Mai — [Learning Sequential Mobility Choice: A Review of Route and Activity Choice through Inverse Reinforcement and Imitation Learning](http://arxiv.org/abs/2608.15339v1)
  <details><summary>📄 Abstract</summary>
  Route and activity choice are connected levels of a common sequential mobility decision problem: activity choice determines what people do, where, and when, while route choice governs how they move between activities. This review develops a unified framework connecting transportation choice modeling with inverse reinforcement learning (IRL) and imitation learning (IL). Under explicit assumptions, recursive logit, logit dynamic discrete choice, and maximum-entropy IRL share a soft Bellman represe...
  </details>

- **2026-08-15** — Sijing Wu, Dongyuan Li, Miaoting Huang et al. — [BrainLinear: A Linear Model for Brain Network Analysis in Sparse Tangent Subspaces](http://arxiv.org/abs/2608.15266v1)
  <details><summary>📄 Abstract</summary>
  Functional connectome analysis examines brain-region interactions to understand and identify disorders such as autism spectrum disorder and Alzheimer's disease. Existing methods typically use GNNs and Transformers to model the full functional connectivity matrix. However, processing tens of thousands of connections introduces redundancy and noise, increases computational cost, and limits connection-level interpretability. This raises a central question: do we really need complex interaction mode...
  </details>

- **2026-08-15** — Diego Mardian, Frank Liu — [Demographic Injection in Medical Language Models under Diversity, Equity, and Inclusion Prompts](http://arxiv.org/abs/2608.15254v1)
  <details><summary>📄 Abstract</summary>
  Clinical-AI guidance increasingly recommends prompting language models to reason with attention to diversity, equity, and inclusion (DEI). We measure a side effect that misrepresents patients: a one-sentence DEI prompt appended to a medical question leads models to add patient demographic attributes (race, socioeconomic status, sex) the question never stated, in effect rewriting who the patient is. We call this demographic injection. Across 47 models, four medical benchmarks, and 376,000 respons...
  </details>

- **2026-08-15** — Yinjian Zhao, Zhongping Zhao, Zhe Liu et al. — [AlgoPlasma: Open Algorithms for Plasma Modeling](http://arxiv.org/abs/2608.15249v1)
  <details><summary>📄 Abstract</summary>
  AlgoPlasma is an open-source library in which core numerical algorithms for plasma modeling are implemented as modular, well-documented, and independently testable components. Rather than offering a complete simulation code, it allows researchers to select, adapt, and assemble the required components into application-specific workflows. The current release is centered on particle-based simulation, while AlgoPlasma is designed to encompass a broader range of approaches to plasma modeling. It prov...
  </details>

- **2026-08-15** — Timo Sämann — [P-PAS: Prefill-Pressure Adaptive Scheduling for Long-Context LLM Serving](http://arxiv.org/abs/2608.15171v1)
  <details><summary>📄 Abstract</summary>
  Long-context LLM applications such as retrieval-augmented generation (RAG) and agentic systems often process tens of thousands of input tokens to produce short outputs, making end-to-end request latency an important serving objective. We show that the maximum number of batched tokens (MBT), which controls the token scheduling budget in vLLM, has a scheduling-pressure-dependent effect on latency. Larger token budgets can reduce latency under low scheduling pressure, while smaller budgets become p...
  </details>

- **2026-08-15** — Sander Borst, Golnoosh Shahkarami, Rohit Vaish — [Fair Division Meets Scheduling: Approximately Envy-Free Interval Scheduling](http://arxiv.org/abs/2608.15159v1)
  <details><summary>📄 Abstract</summary>
  We study interval scheduling from the perspective of fair allocation. There are $m$ identical machines and a set of intervals, each specified by a start time, an end time, and a nonnegative weight. A schedule assigns a subset of the intervals to the machines so that no two intervals on the same machine overlap, and the goal is to maximize the total weight of scheduled intervals. Viewing machines as agents and intervals as goods, we require the schedule to be envy-free up to one item (EF1), and w...
  </details>

- **2026-08-15** — Zhiqiang He, Zhi Liu — [ReForge: Keeping ABR Algorithms Never Finished with Verified Large Language Model Edits](http://arxiv.org/abs/2608.15138v1)
  <details><summary>📄 Abstract</summary>
  Designing an ABR algorithm for one network scenario takes an engineer months, and large language models now do this work in hours, matching or beating hand-built designs. But either way, the design fits only the world visible at its birth, and fails on the world that arrives after. We ask whether an ABR algorithm can keep pace with the world, redesigned in minutes as each scenario arrives, with every change proven harmless to every scenario already served. In this work, we propose ReForge, a con...
  </details>

- **2026-08-15** — Amrit Gopinath,  Raghul, Durairaj Thenmozhi — [A Declarative-Procedural Perspective on Expert Routing in Bilingual Mixture-of-Experts Language Models](http://arxiv.org/abs/2608.15102v1)
  <details><summary>📄 Abstract</summary>
  We investigate whether Mixture-of-Experts (MoE) language models develop linguistically structured expert routing during bilingual language acquisition. Inspired by the Declarative-Procedural framework, we analyze lexical, grammatical, and syntactic processing in a decoder-only English-German MoE Transformer trained under sequential language exposure. We construct a probe-based validation set and extract token-level routing distributions to quantify category-dependent specialisation using mutual ...
  </details>

- **2026-08-15** — Daniel Khaykelson, Lothar Houben, Boris Rybtchinski — [DINO4DSTEM: A self-supervised framework for structural discovery in 4D-STEM](http://arxiv.org/abs/2608.15098v1)
  <details><summary>📄 Abstract</summary>
  Nanodiffraction using 4D-STEM has become a key technique for quantitative nanoscale structural mapping in materials research, yet interpreting its high-dimensional datasets in structurally complex materials remains a major bottleneck. Existing analysis workflows typically rely on structural models, manual annotation, predefined classes, or sample-specific heuristics, limiting their ability to characterize heterogeneous complex materials. Here, we introduce DINO4DSTEM, a self-supervised machine l...
  </details>

- **2026-08-14** — Alexei Vazquez — [Absorbing phase transition in a queueing model of coupled adaptive agents](http://arxiv.org/abs/2608.14398v1)
  <details><summary>📄 Abstract</summary>
  What decides whether people do things together or separately? Many activities cannot be carried out alone, and an individual must rank them against the private tasks competing for the same time. We address this within the priority-queue description of human activity by letting each agent choose the priority of a shared task rather than drawing it from a fixed distribution: the value of the joint activity, discounted by the estimated risk that the partner will not take part. Participation becomes...
  </details>

- **2026-08-14** — Benedikt Barthel Sorensen, Mitchell Black, Erfaun Noorani et al. — [A Temporal Barrier Framework for Collision Avoidance in Multi-Agent Autonomous Aerial Vehicles](http://arxiv.org/abs/2608.14239v1)
  <details><summary>📄 Abstract</summary>
  Operating teams of autonomous aircraft in dynamic, uncertain, and potentially adversarial environments requires safety protocols that are reliable yet selective, and allow agents to fly in close proximity while making progress toward mission objectives. We introduce adversarial time-to-collision (aTTC), a risk metric that quantifies, for a given agent, how quickly any surrounding agent could reach it assuming adversarial intent. We embed aTTC into the control barrier function (CBF) framework, de...
  </details>

- **2026-08-14** — Masahiro Kato, Taka Kato — [Handover of In-Context Learning State Across Session Boundaries](http://arxiv.org/abs/2608.14528v1)
  <details><summary>📄 Abstract</summary>
  This study investigates the methodological and theoretical properties of session handover in applications that use large language models. A task may continue in a new session when the context reaches the model's input limit, when the application restarts, or when another agent is asked to finish the task. The application must then decide which information from the earlier session to pass on. We formulate handover as the transfer of a task-relative in-context learning (ICL) state and distinguish ...
  </details>

- **2026-08-14** — Evan Coleman, Yuzhong Shen, Masha Sosonkina et al. — [Validating LLM-Modernized Scientific Software Through Differential Fault Injection](http://arxiv.org/abs/2608.14527v1)
  <details><summary>📄 Abstract</summary>
  Large language model (LLM) agents are increasingly used to modernize the legacy Fortran underlying production scientific software, but validation of these transformations emphasizes nominal executions and may not test whether a modernization preserves the original code's response to faults, perturbations, and reduced precision. We present a differential fault-injection validation method: a harness instruments the shared self-consistent-field driver of GAMESS at twelve sites and applies identical...
  </details>

- **2026-08-14** — Zohar Barak, Inbal Talgam-Cohen — [Ex-ante versus Ex-post: Egalitarian Facility Location Mechanism Design](http://arxiv.org/abs/2608.14499v1)
  <details><summary>📄 Abstract</summary>
  We study the facility location mechanism design problem where $n$ strategic agents report locations in Euclidean space and the mechanism outputs a single facility location. Each agent's cost is its distance from the facility, and our objective is to minimize the egalitarian cost, i.e., the maximum agent cost, in a strategyproof way.   The optimal deterministic approximation ratio is $2$, achieved by any dictator mechanism. We study the power of randomized strategyproof-in-expectation mechanisms....
  </details>


## 📊 统计 / Statistics

| 分类 / Category | 论文数 / Count |
|------|--------|
| jailbreak | 587 |
| prompt-injection | 495 |
| memory-poisoning | 44 |
| tool-use-attack | 120 |
| backdoor | 418 |
| adversarial-attack | 566 |
| privacy-leakage | 3858 |
| steganography | 55 |
| misuse | 905 |
| red-teaming | 115 |
| vulnerability | 2737 |
| defense | 2461 |
| alignment | 2276 |
| robustness | 2283 |
| watermark | 303 |
| unlearning | 90 |
| agent-safety | 52 |
| benchmark | 59 |
| survey | 286 |
| other | 6524 |

---

📚 **全部 24234 篇论文**（2022 至今）请访问 [GitHub Pages](https://ny1024.github.io/AgentSafety-Papers/) 查看完整列表、搜索与筛选。

*Generated by AgentGuard at 2026-08-19 18:26:01*