<div align="center">

# AgentGuard 🛡️

**Daily Tracking of LLM Agent Security Papers on arXiv**

[![Auto Update](https://github.com/NY1024/AgentSafety-Papers/actions/workflows/daily-update.yml/badge.svg)](https://github.com/NY1024/AgentSafety-Papers/actions/workflows/daily-update.yml)
[![Papers](https://img.shields.io/badge/Papers-24050-blue)](#)
[![License](https://img.shields.io/badge/License-MIT-green)](#)

</div>

---

## 📖 简介 / Introduction

自动追踪 arXiv 上大模型 Agent 安全方向的最新论文，每日更新，关键词智能分类。

*Automatically tracking the latest LLM Agent security papers on arXiv, updated daily with keyword-based classification.*

**最近更新 / Last Updated**: 2026-08-18 18:30 ｜ **论文总数 / Total Papers**: 24050（近 30 天 / Recent 30 days: 3182）

🌐 **[GitHub Pages](https://ny1024.github.io/AgentSafety-Papers/)** — 查看全部 24050 篇论文（含摘要、分类筛选、搜索）/ View all 24050 papers with abstracts, filters & search

## 📑 分类导航 / Category Navigation

- **[jailbreak](#-jailbreak)** — 越狱攻击 / Jailbreak Attacks — 583
- **[prompt-injection](#-prompt-injection)** — 提示注入攻击 / Prompt Injection Attacks — 492
- **[memory-poisoning](#-memory-poisoning)** — 记忆投毒与篡改 / Memory Poisoning & Tampering — 44
- **[tool-use-attack](#-tool-use-attack)** — 工具使用攻击 / Tool-Use Attacks — 118
- **[backdoor](#-backdoor)** — 后门与投毒攻击 / Backdoor & Poisoning Attacks — 416
- **[adversarial-attack](#-adversarial-attack)** — 对抗攻击 / Adversarial Attacks — 563
- **[privacy-leakage](#-privacy-leakage)** — 隐私泄露 / Privacy Leakage — 3846
- **[steganography](#-steganography)** — 隐写与隐蔽通信 / Steganography & Covert Communication — 55
- **[misuse](#-misuse)** — 滥用与误用 / Misuse & Abuse — 900
- **[red-teaming](#-red-teaming)** — 红队测试 / Red Teaming — 115
- **[vulnerability](#-vulnerability)** — 漏洞与攻击面 / Vulnerabilities & Attack Surfaces — 2714
- **[defense](#-defense)** — 防御与防护方法 / Defense & Protection Methods — 2438
- **[alignment](#-alignment)** — 对齐与安全约束 / Alignment & Safety Constraints — 2261
- **[robustness](#-robustness)** — 鲁棒性与可靠性 / Robustness & Reliability — 2265
- **[watermark](#-watermark)** — 水印与溯源 / Watermarking & Provenance — 300
- **[unlearning](#-unlearning)** — 机器遗忘 / Machine Unlearning — 89
- **[agent-safety](#-agent-safety)** — Agent 安全框架 / Agent Safety Frameworks — 52
- **[benchmark](#-benchmark)** — 安全评测与基准 / Safety Benchmarks & Evaluation — 58
- **[survey](#-survey)** — 综述与系统化 / Surveys & Systematization — 285
- **[other](#-other)** — 其他安全相关 / Other Security-Related — 6456

## 📄 近期论文 / Recent Papers (Last 30 Days)

> 仅展示最近 30 天中最新的 500 篇论文（含日期、作者、摘要）。近 30 天共 3182 篇，完整 24050 篇论文列表请访问 [GitHub Pages](https://ny1024.github.io/AgentSafety-Papers/)

> Showing the latest 500 of 3182 papers from the last 30 days (with date, authors & abstract). For the full list of 24050 papers, visit [GitHub Pages](https://ny1024.github.io/AgentSafety-Papers/)

### 📂 jailbreak
*越狱攻击 / Jailbreak Attacks* — 6 papers

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

- **2026-08-13** — Julian Minder, Viktor Moskvoretskii, Raghav Singhal et al. — [Synthetic Persona Pretraining: Alignment from Token Zero](http://arxiv.org/abs/2608.13482v1)
  <details><summary>📄 Abstract</summary>
  As language-model-based AI is increasingly deployed in autonomous settings, aligning its goals and values with those of humans becomes critical. Today, alignment, and the assistant identity itself, are typically introduced only after pretraining, once behavioral priors are already established. This can make values a thin overlay, rather than deeply rooted, and facilitate subsequent misalignment. Pursuing a different paradigm, we introduce Synthetic Persona Pretraining (SPP), which installs the d...
  </details>

- **2026-08-13** — Fangzhou Chen, Shiji Zhao, Mengyang Wang et al. — [HiRoute: Hierarchical Routed Prompt Tuning for Safety Alignment of Large Language Models](http://arxiv.org/abs/2608.12821v1)
  <details><summary>📄 Abstract</summary>
  Large language models (LLMs) remain vulnerable to harmful requests and jailbreak attacks. Parameter-efficient safety alignment methods based on prompt tuning typically rely on a single global prompt or externally selected prompt modules. Such static designs struggle to maintain a cross-category safety boundary while generating constructive responses tailored to specific risks and avoiding over-refusal of benign inputs. To address these limitations, we propose HiRoute, an input-adaptive hierarchi...
  </details>


### 📂 prompt-injection
*提示注入攻击 / Prompt Injection Attacks* — 4 papers

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
*工具使用攻击 / Tool-Use Attacks* — 5 papers

- **2026-08-17** — Mingxiao Liu, Zhoumian Jiang, Jianan Ma et al. — [CompoSkill: Compositional Skill Chain Attacks from Individually Scanner-Passing LLM Agent Skills](http://arxiv.org/abs/2608.16246v1)
  <details><summary>📄 Abstract</summary>
  Autonomous AI agents tackling Long Horizon Tasks depend on marketplace skills that are certified one at a time: a scanner returns a safety verdict for each skill and declares the ecosystem safe if every package passes. We show that this assumption fails under skill composition. A skill may pass the per-skill scanner individually yet participate in a risky composition when an agent connects its outputs, capabilities, or side effects with those of other scanner-passing skills. This makes skill com...
  </details>

- **2026-08-17** — Lihui Ding, Zihan Guo, Bingwei Lu et al. — [Skill2Query: Exploiting Skill Structure to Generate Pseudo-Queries for Agent Skill Retrieval](http://arxiv.org/abs/2608.16071v1)
  <details><summary>📄 Abstract</summary>
  Pseudo-query generation can alleviate the supervision bottleneck for agent skill retrieval, but existing document-level approaches typically leave the rich internal relations among capabilities, parameters, and usage examples implicit. As a result, generated queries may be topically relevant to a skill while lacking capability grounding and parameter consistency, raising the question of whether explicitly exploiting a skill document's internal structure can produce more effective retrieval signa...
  </details>

- **2026-08-14** — Zhiyuan Jiang, Fangrui Huang, Hanwen Xing et al. — [Demystifying Agent Skills: Why They Work-Until They Don't](http://arxiv.org/abs/2608.14036v1)
  <details><summary>📄 Abstract</summary>
  Skills have emerged as a practical and effective approach for enhancing LLM agents at inference time through structured packages of knowledge. However, existing evaluations largely measure whether skills improve aggregated task success, leaving a more fundamental question underexplored: \emph{\textbf{When do skills help, why do they work, and where do they fail?}} Through controlled experiments across various benchmarks, agent harnesses and LLMs, we isolate the effects of representation, outcome...
  </details>

- **2026-08-13** — Qianxi Yan, Chunrong Chen, Jiuzhou Zhao et al. — [SkillEvo: Self-Renewing Evolution Gradients from Multi-Turn Interaction Feedback](http://arxiv.org/abs/2608.13120v1)
  <details><summary>📄 Abstract</summary>
  Agent Skills are today either hand-authored or produced in a single LLM generation pass, and consequently possess no closed loop through which they might improve from the interaction failures they actually cause. Recent work does close this loop, but derives its feedback from single-turn question-answering evaluation. The consequence is a sharp asymmetry: once the first round has patched the gaps that a single exchange can reveal, the evolution gradient decays, the defects that surface only acro...
  </details>

- **2026-08-13** — Chang Liu, Yuqi Zhang, Yiman Zhong et al. — [SkillShapley: Boundary-Adaptive Shapley Valuation for Skill Step Attribution in LLM Agents](http://arxiv.org/abs/2608.13173v1)
  <details><summary>📄 Abstract</summary>
  Agent skills are crucial external instructions that enable language agents to execute long procedural tasks such as coding or document processing. Existing agent skills are primarily created through human manual crafting or agent execution traces, with limited understanding of how each step contributes to overall skill performance on specific tasks; i.e., there remains an open problem in quantifying the contribution of individual steps within an agent skill. To address this issue, we first model...
  </details>


### 📂 backdoor
*后门与投毒攻击 / Backdoor & Poisoning Attacks* — 2 papers

- **2026-08-16** — Nokimul Hasan Arif, Qian Lou, Mengxin Zheng — [Conjunctive Poisoning in AI Supply-Chain Applications](http://arxiv.org/abs/2608.15913v1)
  <details><summary>📄 Abstract</summary>
  Large Language and Vision-Language Models are increasingly deployed through inference pipelines that include prompt wrappers (e.g., templates and post-processing scripts) and configuration metadata (e.g., JSON/YAML files) that together shape model outputs. While model weights and binaries are routinely verified, these textual deployment artifacts remain weakly protected despite directly influencing runtime behavior. We show that a malicious developer can pair a benign-looking wrapper with crafte...
  </details>

- **2026-08-16** — Riku Mochizuki, Shusuke Komatsu, Souta Noguchi et al. — [Assessing Attack Surfaces in Generative Search Engines through Publisher Attributes: A Case Study in Political Domains](http://arxiv.org/abs/2608.15814v1)
  <details><summary>📄 Abstract</summary>
  We characterize the attack surface of generative search engines (GSEs) against poisoning attacks in the political domain, from the perspectives of citation selection and personalization. GSEs integrate web search and answer generation with user preferences and backgrounds using large language models (LLMs). They play a crucial role in how users access information on the web. Because anyone can publish content on the web, GSEs are vulnerable to poisoning attacks that manipulate citations to under...
  </details>


### 📂 adversarial-attack
*对抗攻击 / Adversarial Attacks* — 8 papers

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

- **2026-08-13** — Denzel Chiuseni, Athanase Bahizire, Silva Hama et al. — [Adversarial Robustness in Smishing Detection: A Comparative Analysis of Adversarial Fragility in Classical vs. Transformer-Based Detection Systems](http://arxiv.org/abs/2608.12889v1)
  <details><summary>📄 Abstract</summary>
  Smishing detection systems are commonly trained and evaluated on clean, monolingual text. In low-resource settings, however, attackers frequently circumvent these systems through character obfuscation, cross-lingual code-switching, and structural perturbation. This study evaluates adversarial robustness for five model architectures: three classical lexical models (Random Forest, XGBoost, CNN+BiLSTM) and two multilingual transformers (mBERT, XLM-RoBERTa), using a dataset of 27,037 messages. Class...
  </details>

- **2026-08-13** — Qiao Li, Xiaomeng Fu, Yuanshu Zhao et al. — [Semantic Steering for Controllable Generation: Tuning-Free Concept Erasure in Multimodal Diffusion Transformers](http://arxiv.org/abs/2608.12829v1)
  <details><summary>📄 Abstract</summary>
  Multimodal Diffusion Transformers (MM-DiTs) have demonstrated remarkable text-to-image generation performance, surpassing traditional U-Net-based diffusion models. Nevertheless, their powerful generative capabilities also raise significant safety concerns, as they may generate sensitive or inappropriate content. While existing concept erasure methods aim to mitigate such risks, most require modifying model parameters, which are often architecture-specific and impractical for deployed larger mode...
  </details>


### 📂 privacy-leakage
*隐私泄露 / Privacy Leakage* — 27 papers

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

- **2026-08-14** — Hansoo Lee, Pablo Fonseca, Md Haseen Akhtar — [Designing Mobile and Wearable Sensor-Fused Conversational Agents for Health and Wellbeing](http://arxiv.org/abs/2608.14273v1)
  <details><summary>📄 Abstract</summary>
  Mobile and wearable devices increasingly collect continuous wellbeing data, including sleep, activity, heart rate, stress, blood glucose, and blood pressure. Yet access to such data does not automatically help people interpret their condition or change behavior. Many health applications remain dashboard-first, presenting charts, thresholds, goals, and alerts while leaving users to decide what a change means and what action should follow. Conversely, generic LLM-based conversational agents (CAs) ...
  </details>

- **2026-08-14** — Ying Huang, Wencan Zhang, Brian Y. Lim — [AlignFace: Human-Aligned Face Similarity Metric with Interpretable Concept Relations](http://arxiv.org/abs/2608.14130v1)
  <details><summary>📄 Abstract</summary>
  Computer vision models for generated facial content, such as face editing and privacy protection, increasingly affect people, requiring similarity metrics that serve as faithful proxies for human perception. While perceptual evaluation has progressed from signal-based heuristics to representation-based metrics, current approaches are limited to behavioral modeling without cognitive alignment. They rely on implicit and spurious relations while assuming a universal observer, failing to account for...
  </details>

- **2026-08-14** — Myunghoon Ryu, Geunpyo Park, Sungjoon Lee et al. — [P2Skill: Privacy Preserving Skill Distillation for Cloud-Local LLM Inference Systems](http://arxiv.org/abs/2608.14094v1)
  <details><summary>📄 Abstract</summary>
  Cloud-local LLM inference systems have the potential to use the reasoning capability of large cloud models while protecting sensitive user data on personal devices. Cloud-bound requests must exclude personally identifiable information (PII) to prevent external data leakage. Existing privacy-preserving methods rely on prompt perturbation, entity masking, or model fine-tuning, but these approaches may distort contextual semantics or require additional training. This paper proposes P2Skill, a promp...
  </details>

- **2026-08-13** — Yakun Huo, Yingquan Wang, Yangyang Liu et al. — [Paths: Prompt-aware Spatio-temporal Transformer with Hierarchical Multi-modal Fusion for RGB-Event Video Person Re-Identification](http://arxiv.org/abs/2608.13092v1)
  <details><summary>📄 Abstract</summary>
  RGB-Event Video Person Re-Identification (RE-VReID) aims to retrieve specific person across non-overlapping cameras with complementary RGB videos and event streams. However, existing methods often decouple spatial and temporal modeling, which limits their interaction. In addition, global-level RGB-Event fusion fails to fully exploit fine-grained discriminative cues. To address these issues, we propose Paths, a unified framework with spatio-temporal modeling and hierarchical multi-modal fusion fo...
  </details>

- **2026-08-13** — Beining Xu, Hairui Wang, Jiaxin Wang et al. — [Beyond Visual Evidence: Revealing and Mitigating Relational Privacy Leakage in Document MLLMs](http://arxiv.org/abs/2608.12911v1)
  <details><summary>📄 Abstract</summary>
  While the privacy risks of multimodal large language models (MLLMs) have drawn significant attention, the unique vulnerabilities of domain-specific MLLMs remain largely underexplored. Focusing on document understanding MLLMs for identity document processing, this paper investigates the privacy issues inherent in Key Information Extraction (KIE) tasks. We reveal that when input images lack sufficient visual evidence, these models often rely on memorized field relations from training data to infer...
  </details>

- **2026-08-13** — Rana Muhammad Ahmed, Sabahat Abbas — [Labels Are Not Endpoints: Treatment Leakage and Construct Validity in MCP Agent Security Evaluation](http://arxiv.org/abs/2608.12880v1)
  <details><summary>📄 Abstract</summary>
  Security evaluations of tool-using agents often equate stored labels with behavioral facts. We audit a preserved campaign by tracing 10,200 execution rows to 180 model-bound requests, 45 semantic requests, and 15 observable stimuli. Two schema treatments were delivered, but the planned external payload-family corpus was not. The historical grader exhibited direct treatment leakage: treatment metadata gated the ATTACK_SUCCESS class, so fixed behavior could change class under treatment relabeling....
  </details>

- **2026-08-13** — Ruofei Qu, Wei Feng, Hongzhan Ma et al. — [RealmEye: Virtual Machine Introspection for Arm CCA Realm VMs](http://arxiv.org/abs/2608.12822v1)
  <details><summary>📄 Abstract</summary>
  Confidential VMs (CVMs) have become the dominant substrate for sensitive cloud workloads, from financial services to privacy-preserving AI inference. The hardware isolation that protects these CVMs from a malicious cloud also blinds their owners to what runs inside them: kernel rootkits planted via network or supply-chain attacks can hide processes, tamper with kernel data, and exfiltrate model weights under the cover of the same isolation that defends the VM. Tenants therefore need to inspect a...
  </details>

- **2026-08-13** — Muhammad Hannan Akram, Muhammad Abubakar Rashid, Wassi Haider Kabir et al. — [Heterogeneity-Aware Belief Synchronization for Semantic Communication in AI-Native 6G Networks](http://arxiv.org/abs/2608.13394v1)
  <details><summary>📄 Abstract</summary>
  6G networks will not be serving as communication infrastructures only; rather, they are expected to evolve into intelligent systems, where thousands of autonomous artificial intelligence (AI) agents are interconnected. The agents are deployed across a wide range of platforms including low Earth orbit (LEO) satellites, high-altitude platforms (HAPs), unmanned aerial vehicles (UAVs), edge servers, and terrestrial devices. These agents continuously observe their environment and exchange information...
  </details>

- **2026-08-13** — Xinming Wang, Weinong Wang, Hongming Yang et al. — [Beyond Correctness: Benchmarking and Aligning Response Behaviors in Hybrid-Thinking MLLMs](http://arxiv.org/abs/2608.12781v1)
  <details><summary>📄 Abstract</summary>
  Hybrid-thinking multimodal large language models (MLLMs) allow a single model to alternate between deliberative thinking and latency-efficient non-thinking inference. Although these modes differ in reasoning budget, their delivered responses should satisfy the same user-facing standard. Correctness alone may not characterize this response quality; we therefore evaluate task accuracy and response-pattern failures as complementary outcomes. We study this gap through \textbf{response-pattern alignm...
  </details>

- **2026-08-13** — I. Dey, I. Cherkaoui — [Deterministic Johnson--Lindenstrauss Projections from Pisot $β$-Transformations for Zero-Knowledge Private Routing](http://arxiv.org/abs/2608.13078v1)
  <details><summary>📄 Abstract</summary>
  Zero-knowledge (ZK) proofs certify that a message belongs to an allowed semantic class without revealing the message, but the certificate compares a high-dimensional embedding against class centroids, so its cost grows with the embedding dimension $d$. A Johnson--Lindenstrauss (JL) projection lowers $d$ to $m\ll d$ while preserving pairwise distances, yet a random JL matrix must be committed and its sampling proved inside the circuit, which is costly and a leakage risk. We construct a public det...
  </details>

- **2026-08-13** — Wenjin Liu, Shen Pang, Tiesunlong Shen et al. — [TIEM: Temporal Integration of Hypergraph Evidence and Skill Memory for Event-Driven Financial Forecasting](http://arxiv.org/abs/2608.13024v1)
  <details><summary>📄 Abstract</summary>
  Event-driven catalyst-outcome forecasting increasingly uses retrieval- and memory-augmented large language model agents for prediction. However, training-data contamination and temporal leakage can create an Evidence Chasm between reported accuracy and true predictive ability. We propose TIEM, a timestamp-gated framework with three coordinated components: an Event-Evidence Hypergraph (EEH) for timestamp-filtered multi-tier retrieval; a Case-based Skill Memory (CSM) for source-tagged temporal ski...
  </details>

- **2026-08-13** — Saleh Almohaimeed, Saad Almohaimeed, Mousa Jari et al. — [Privacy-Preserving RAG by Concealing Sensitive Information from External LLMs](http://arxiv.org/abs/2608.12675v1)
  <details><summary>📄 Abstract</summary>
  Retrieval-Augmented Generation (RAG) is widely used to improve the performance of Large Language Models (LLMs) in answering user queries. Existing privacy research on RAG has focused on preventing unauthorized users from accessing sensitive data. However, another important problem that is often overlooked in RAG privacy research is that external generators have access to the query and the retrieved documents, which may contain confidential information that could potentially be misused or accesse...
  </details>


### 📂 misuse
*滥用与误用 / Misuse & Abuse* — 13 papers

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

- **2026-08-13** — Satoshi Takahashi, Nobuji Kouno, Masaaki Komatsu et al. — [Rules or Character? Scaling Laws for AI Safety Design](http://arxiv.org/abs/2608.13345v1)
  <details><summary>📄 Abstract</summary>
  Artificial Intelligence (AI) safety systems combine character shaping (e.g., Reinforcement Learning from Human Feedback [RLHF], Constitutional AI), which modifies behavioral distributions at training time, with rule enforcement (e.g., output filters, safety classifiers), which blocks harmful outputs at inference time, yet little formal analysis exists on how their optimal balance should change as deployment scales increase. We introduce a stylized comparative-statics model that parameterizes saf...
  </details>

- **2026-08-13** — Ping Wu, Haibo Tong, Feifei Zhao et al. — [Refusing Intent, Not Form: Wrapper-Based Intent-Group Supervision for LLM Safety](http://arxiv.org/abs/2608.13304v1)
  <details><summary>📄 Abstract</summary>
  Safety tuning can improve harmful refusal, but models may learn surface-form shortcuts: wrapped harmful prompts bypass safety, while similarly wrapped benign prompts are over-refused. We propose Wrapper-Based Intent-Form Augmentation (WIFA), an automatic intent-group augmentation method that pairs wrapped harmful examples with structurally matched wrapped benign counterexamples, requiring no external teacher or manual per-wrapper intent labels. We use WIFA as a common data layer for two compleme...
  </details>

- **2026-08-13** — Severin Engelmann, Daniel Susser — [From Fair Representation to Just Recognition in Generative AI](http://arxiv.org/abs/2608.12669v1)
  <details><summary>📄 Abstract</summary>
  The fair AI/ML literature has long distinguished distributive fairness, concerning how automated systems allocate resources and opportunities, from representational fairness, concerning how they shape the ways individuals and social groups are perceived, understood, and accorded social status. Generative AI is rebalancing these normative dimensions. Unlike predictive systems, large language models (LLMs) and related technologies are fundamentally expressive: their primary function is to convey m...
  </details>


### 📂 red-teaming
*红队测试 / Red Teaming* — 1 papers

- **2026-08-13** — Xing Zhang, Yanwei Cui, Guanghui Wang et al. — [Reconcile Once, Write Anytime: A Trust-Tiered Librarian and a Multi-Agent Writer for Drift-Free, Point-in-Time Research](http://arxiv.org/abs/2608.12984v1)
  <details><summary>📄 Abstract</summary>
  Long-form research reports generated by large language models drift, contradict themselves, and lose provenance: the same metric appears with different values, and rumor is quoted as confidently as an audited filing. We present a two-tier agentic system that separates a maintained, point-in-time knowledge library from report writing. A deterministic "librarian" ingests timestamped sources into a trust-tiered ontology, layering evidence cards, an authoritative metric ledger, and a claim graph int...
  </details>


### 📂 vulnerability
*漏洞与攻击面 / Vulnerabilities & Attack Surfaces* — 47 papers

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

- **2026-08-13** — Yukun Dai, Mingzhe Dai, Tianshi Wang et al. — [UniTexture: Cross-Task Universal Adversarial Textures for Vision-Language-Action Models](http://arxiv.org/abs/2608.13453v1)
  <details><summary>📄 Abstract</summary>
  Vision-Language-Action (VLA) models have emerged as generalist robotic policies capable of following diverse language instructions and performing a wide range of manipulation tasks. However, their direct control over embodied agents also exposes them to adversarial interference that may cause unsafe physical behaviors. Existing attacks on robotic policies are typically optimized for a single task or instruction, leaving the cross-task vulnerabilities of multitask VLAs largely unexplored. We intr...
  </details>

- **2026-08-13** — Md Wasiul Haque, Sagar Dasgupta, Mizanur Rahman et al. — [LLM-Assisted Dynamic Threat Analysis for Attacker-Reachable Software Weaknesses in Autonomous Vehicles](http://arxiv.org/abs/2608.13450v1)
  <details><summary>📄 Abstract</summary>
  Autonomous vehicles depend on large safety-critical software stacks, where weaknesses reachable from adversarial inputs may affect steering, braking, or other control decisions. Static analysis can identify candidate sites, but dynamically confirming exploitability requires executable test artifacts that are difficult to construct manually. We investigate whether large language models (LLMs) can automate this process for Autoware, an open-source autonomous-driving stack. We perform compiler-prec...
  </details>

- **2026-08-13** — Raphaël Mothe, Otfried Gühne — [Witnessing the architecture of quantum circuits](http://arxiv.org/abs/2608.13169v1)
  <details><summary>📄 Abstract</summary>
  Determining whether a target unitary can be implemented within a prescribed quantum circuit architecture is a fundamental problem in quantum information, with direct implications for optimisation and compilation of quantum circuits, and hardware-efficient quantum computation. While existing synthesis and compilation methods are primarily constructive, they generally do not provide rigorous certificates that a unitary cannot be realised using given implementation resources. Here we introduce a ge...
  </details>

- **2026-08-13** — Yi Shi, Huichao Xie, Yuqing Wang et al. — [P2Fusion: Prompt-based Progressive Infrared-Visible Image Fusion via Dual-Prior Distillation](http://arxiv.org/abs/2608.13045v1)
  <details><summary>📄 Abstract</summary>
  Infrared-visible image fusion (IVIF) is pivotal for multimodal perception, yet reconciling the inherent information disparity between thermal and textural features remains a fundamental challenge. Existing prior-guided methods often rely on static constraints that induce optimization conflicts or utilize extrinsic semantic priors from large-scale foundation models (e.g., CLIP/DINO), which frequently fail to exploit the intrinsic modality characteristics essential for high-fidelity fusion. To add...
  </details>

- **2026-08-13** — Peng Li, Qianqian Xu, Shilong Bao et al. — [UniTraffic-Agent: Unified Traffic Video Reasoning for AI City Challenge 2026 Track 3 with Two Out-of-Domain Evaluations](http://arxiv.org/abs/2608.13031v1)
  <details><summary>📄 Abstract</summary>
  Traffic video understanding has become an important problem in intelligent transportation, as road videos provide direct evidence for accidents, violations, and interactions between vehicles and vulnerable road users. A useful system should explain how a traffic event develops, why it happens, and when the relevant interaction occurs, yet this remains difficult for multimodal large language models (MLLMs) because traffic videos contain sparse events and varied viewpoints. We introduce UniTraffic...
  </details>

- **2026-08-13** — Qiyang Chen, Yixi Li, Fengwei Zhang et al. — [ATOBench: Tracing How Autonomous Penetration-Testing Agents Verify Vulnerabilities When Target Evidence Lies](http://arxiv.org/abs/2608.12996v1)
  <details><summary>📄 Abstract</summary>
  Autonomous penetration-testing agents rely on target responses. These responses guide both subsequent actions and the final report. A deceptive response can therefore redirect both the attack trajectory and the agent's verification process. However, final reports reveal little about how an agent interprets conflicting evidence, changes course, decides to stop, or turns observations into a vulnerability claim. We introduce ATOBench, an evaluation framework that makes this verification process obs...
  </details>

- **2026-08-13** — Wencong Zhang, Yue Zhang, Meiyan Huang et al. — [Dual-Manifold Geometry Guided Representation Learning: Adaptive Coupling between Kernel and Data Spaces](http://arxiv.org/abs/2608.12737v1)
  <details><summary>📄 Abstract</summary>
  Deep representation learning has primarily focused on how features evolve across network layers, while largely overlooking the structured geometry embedded in network parameters. We introduce a dual-manifold perspective in which each convolutional layer contains two coupled geometric spaces: a Kernel Manifold induced by convolutional filters and a Data Manifold characterized by intermediate feature representations. Because these manifolds share the same channel space, parameter geometry can prov...
  </details>

- **2026-08-13** — Zirui Cheng, Xun Xu, Tiankai Chen et al. — [MAG: MAnifold Guided Semi-Supervised Multi-modal In-Context Learning](http://arxiv.org/abs/2608.12724v1)
  <details><summary>📄 Abstract</summary>
  Few-shot in-context learning (ICL) with multi-modal large language models (MLLMs) enables task adaptation without parameter updates, but its performance is highly sensitive to the quality and coverage of the selected demonstrations. While unlabeled multi-modal data is abundant, it remains elusive how to exploit them for ICL. We propose MAG (MAnifold-Guided semi-supervised in-context demonstra- tion selection), an efficient framework that leverages unlabeled data to improve multi-modal ICL. MAG f...
  </details>

- **2026-08-13** — Xiaoyan Feng, Yanjun Zhang, He Zhang et al. — [Tracing Provenance and Detecting Tampering with Complementary LLM Watermarks](http://arxiv.org/abs/2608.12713v1)
  <details><summary>📄 Abstract</summary>
  Watermarking LLM-generated text is an important task for tracing its provenance. Existing LLM watermarks preserve provenance under editing, but this same robustness allows an adversary to alter critical content while retaining attribution, a vulnerability known as piggyback spoofing. We introduce an innovative watermark that jointly provides provenance and tamper evidence. It co-embeds a robust signal and a fragile signal into each generated token. The signals share the same mechanism but use in...
  </details>

- **2026-08-13** — Hamza Shafiq, Hung Manh Pham, Bin Zhu et al. — [CardioState-JEPA: Delay-Aware Cross-Modal Learning of a Shared Cardiac Representation](http://arxiv.org/abs/2608.12944v1)
  <details><summary>📄 Abstract</summary>
  Electrocardiography (ECG), photoplethysmography (PPG), and phonocardiography (PCG) provide complementary views of the same cardiac cycle, yet existing cardiac foundation models are trained for a single sensing modality, leaving the shared physiology across sensors unexploited. We introduce CardioState-JEPA, a cardiac foundation model to learn a single shared representation jointly across ECG, PPG, and PCG, built on a physiology-aware joint-embedding predictive architecture. The model maps hetero...
  </details>


### 📂 defense
*防御与防护方法 / Defense & Protection Methods* — 66 papers

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

- **2026-08-14** — Yuhao Zhan, Bingxiang He, Zecong Tang et al. — [PACE-Bench: Benchmarking Physics Adaptation via Code Evolution in Dynamic Environments](http://arxiv.org/abs/2608.14441v1)
  <details><summary>📄 Abstract</summary>
  Self-evolving agents improve future behavior from interaction experience, yet existing evaluations typically optimize under fixed execution conditions and do not test recovery after those conditions change. To address this gap, we introduce PACE-Bench (Physics Adaptation via Code Evolution), a simulator-grounded benchmark of 144 source-to-target adaptation pairs across six physics domains. Each pair links a source environment to a mutated target environment with the same goal and interface. A co...
  </details>

- **2026-08-14** — Junichiro Niimi — [Revisiting Energy-based Tabular Anomaly Detection: Energy and Reconstruction are Complementary](http://arxiv.org/abs/2608.14186v1)
  <details><summary>📄 Abstract</summary>
  Tabular anomaly detection is dominated by classical density-proxy methods (Isolation Forest, OCSVM, LOF), reconstruction-based detectors (Autoencoders, VAEs), and modern non-parametric scorers (COPOD, ECOD, Deep SVDD), all of which approximate the inlier distribution only indirectly; explicit energy-based models are largely absent. Motivated by the recent revival of EBMs in deep learning (e.g., Energy-Based Transformers, JEPA), we revisit the classical Deep Boltzmann Machine (DBM) for this task ...
  </details>

- **2026-08-14** — Syeda Anshrah Gillani, Mirza Samad Ahmed Baig — [Whose doctor does the AI recommend? An algorithm audit of reputation and demographic signals in large language model-assisted physician choice](http://arxiv.org/abs/2608.14399v1)
  <details><summary>📄 Abstract</summary>
  Patients increasingly ask large language model (LLM) assistants which doctor to see, making these systems AI infomediaries: algorithms that intermediate one person's choice among other people and thereby decide, silently and at scale, which physicians become visible. We report a prespecified randomized algorithm audit of what causally moves those recommendations. Seven models (six open-weight; gpt-4o-mini) each chose among five synthetic family-medicine physician cards whose attributes were inde...
  </details>

- **2026-08-14** — Shuo Liang, Yixing Ma, Pengfei Zhou et al. — [Can We Defend Against AI-Generated Video Attacks on Real-World Crisis Events? A Systematic Evaluation of Detectors, Generators and Social Dissemination](http://arxiv.org/abs/2608.14391v1)
  <details><summary>📄 Abstract</summary>
  Recent video generators can fabricate realistic depictions of wars, disasters, public emergencies, and other real-world crises, creating substantial risks of misinformation. Existing benchmarks, however, provide limited evidence on detector and generator behavior in such settings, including how detectability varies with generation conditions, how people perceive generated videos, and whether detectors remain reliable during social dissemination. To address this gap, we introduce RA-Bench, a benc...
  </details>

- **2026-08-14** — Jinlong Wang, Yuang Jia, Junhong Lin et al. — [CoDS: Robust Collaborative Perception via Expert-driven Detection and BEV Segmentation](http://arxiv.org/abs/2608.14085v1)
  <details><summary>📄 Abstract</summary>
  Collaborative perception breaks through single-view limitations via multi-agent information exchange. However, multi-source noise such as pose errors and communication delays degrades fusion feature quality, constraining perception performance. Joint training of detection and BEV segmentation provides a natural remedy, where segmented road regions help constrain target distributions and detection bounding boxes help recover ambiguous segmentation boundaries. To this end, we propose a robust Coll...
  </details>

- **2026-08-13** — Shubin Lu, Jiaqi Yin, Yihao Huang — [QuISE: Defense against Typographic Attacks on VLMs via Query-Irrelevant Semantic Editing](http://arxiv.org/abs/2608.13119v1)
  <details><summary>📄 Abstract</summary>
  Typographic attacks pose a critical threat to vision-language models (VLMs) by injecting misleading text into images and causing models to rely on adversarial textual cues rather than visual evidence. Existing defenses often require model-specific modifications, additional training, or access to internal model components, limiting their applicability to modern closed-source VLMs. In this paper, we propose QuISE, a model-agnostic, training-free black-box defense based on query-irrelevant semantic...
  </details>

- **2026-08-13** — Atul Kabra, Prakhar Paliwal, Manjesh K. Hanawal — [Operationalizing Cyber Threat Intelligence with GraphRAG](http://arxiv.org/abs/2608.13050v1)
  <details><summary>📄 Abstract</summary>
  When a security researcher publishes a report on a cyberattack, detection engineers are supposed to turn it into working detection rules. In practice, most automated attempts at this only extract the simplest clues from the report --- bad IP addresses, domain names, and file hashes --- and turn them into block lists. This is a weak strategy, because attackers can change these simple clues within hours or days, so the resulting detections stop working almost as soon as they are deployed. Security...
  </details>

- **2026-08-13** — Sanjay Kariyappa, Severin Klingler, G. Edward Suh — [PIPES: Securing Agent Perception with Provenance and Priors](http://arxiv.org/abs/2608.12789v1)
  <details><summary>📄 Abstract</summary>
  Tool-using agents consume external data from sources with different levels of trust, yet tool responses rarely identify who produced each component or what it should convey. We show that this gap enables state-corruption attacks, in which attacker-controlled content makes environmental claims beyond the informational authority of its response component and corrupts the agent's perceived environment, making the resulting action appear justified to existing guardrails. We introduce PIPES (Provenan...
  </details>

- **2026-08-13** — Rishi Shah, Rishav Shrestha — [A Contract-Grade Verifier for LLM-Generated GPU Kernels, and a Native Blackwell Backward for the Gated-Linear-Recurrence Family](http://arxiv.org/abs/2608.12700v1)
  <details><summary>📄 Abstract</summary>
  Systems that generate GPU kernels with language models report high correctness rates. Those rates come from a single loose test: run the kernel on a few random inputs at one fixed shape and accept it if the output is close to a reference. A kernel can pass that test and still be silently wrong. It can return an ordinary number where the true answer is a NaN or an infinity, differ from run to run, break when the shape changes, or accumulate in fp16 where the reference keeps an fp32 total. We buil...
  </details>

- **2026-08-13** — Fanfei Li, Jana Zeller, Manuel Prada-Corral et al. — [LittleLearner: Language Models Under Pedagogically Controlled Knowledge Exposure](http://arxiv.org/abs/2608.13545v1)
  <details><summary>📄 Abstract</summary>
  Modern language models are trained on heterogeneous web-scale text corpora. Consequently, studying knowledge and skill acquisition is difficult, as prior exposure to related content is hard to characterize. To address this challenge, we introduce LITTLECURRICULUM, a curated 88B-token pretraining corpus tailored to U.S. elementary school material, explicitly excluding concepts, facts, and vocabulary taught above Grade 5. Training a 5B-parameter LLM from scratch on LITTLECURRICULUM yields LITTLELE...
  </details>

- **2026-08-13** — Benjamin Agyekum, Fabio Santos — [Does Fixing Break Security? An Empirical Study of Security Degradation in Iterative LLM-Driven Infrastructure-as-Code Repair](http://arxiv.org/abs/2608.13404v1)
  <details><summary>📄 Abstract</summary>
  Background: Iterative feedback loops are the dominant paradigm for improving LLM-generated Infrastructure-as-Code (IaC): validators such as Checkov and terraform validate feed error signals back for successive repair attempts. Prior work reports cumulative-best metrics, which are non-decreasing by construction, so the raw per-iteration security trajectory has never been examined for IaC. Aims: We study security regression (a previously-passing CIS Benchmark check that fails after a repair iterat...
  </details>

- **2026-08-13** — Zeta Avarikioti, Dimitris Karakostas, Karl Kreder et al. — [Slow and Steady: Preventing MEV with Verifiable Delays](http://arxiv.org/abs/2608.13271v1)
  <details><summary>📄 Abstract</summary>
  Our work presents a defense mechanism against Maximal Extractable Value (MEV) opportunities in distributed ledgers. The mechanism relies on the idea of enforcing a verifiable delay when generating transactions, such that a block creator cannot react to the appearance of a MEV opportunity without breaking liveness. We present positive results both in the Byzantine setting and in a game theoretic model of rational participants. We additionally present negative bounds that outline the limitations o...
  </details>

- **2026-08-13** — Shuailei Zhang, Muyun Jiang, Wei Zhang et al. — [EEG-PRIME: Prototype-Aligned Representation Learning with Multi-Level Conditioning for EEG Decoding](http://arxiv.org/abs/2608.13072v1)
  <details><summary>📄 Abstract</summary>
  Electroencephalography (EEG) decoding models often generalize poorly across datasets and subjects due to domain shifts in acquisition protocols and individual neurophysiology. We propose EEG-PRIME, a two-stage EEG foundation model for cross-dataset multi-task decoding. EEG-PRIME combines masked pretraining with prototype-aligned instruction tuning to enable instruction-aware and subject-invariant decoding across diverse BCI paradigms. During pretraining, an EEG encoder learns transferable repres...
  </details>

- **2026-08-13** — Zhenhua Zou, Sheng Guo, Qiuyang Zhan et al. — [InterSAGE: The Secure and Verifiable Interoperability Protocol for An Internet of Agents](http://arxiv.org/abs/2608.13030v1)
  <details><summary>📄 Abstract</summary>
  The emerging Internet of Agents enables LLM-powered agents to discover peers, invoke tools, and delegate tasks across organizational boundaries. Existing protocols increasingly define how agents exchange messages, but not how an agent proves its identity, authorization, advertised capabilities, or accountability after delegation. We present InterSAGE, a trust-native protocol suite that supplies this missing security substrate alongside, rather than in place of, communication protocols. InterSAGE...
  </details>

- **2026-08-13** — Jiajun Ruan, Peiyang Li, Yukun Chen et al. — [Beyond Handcrafted Security: Towards Self-Evolving Defense for LLM Agents](http://arxiv.org/abs/2608.12977v1)
  <details><summary>📄 Abstract</summary>
  The expanding operational capabilities of large language model (LLM) agents introduce sophisticated security threats. Runtime defenses have emerged as an effective approach to mitigating these risks by integrating security mechanisms into the agent execution loop. However, existing runtime defenses rely heavily on manually designed interventions and lack a principled framework for their construction and maintenance. In this work, we first develop a harness-level formulation of runtime defense th...
  </details>

- **2026-08-13** — Zekai Li, Yihao Liang, Hongfei Zhang et al. — [FlashDrive: Flash Vision-Language-Action Inference for Autonomous Driving](http://arxiv.org/abs/2608.12932v1)
  <details><summary>📄 Abstract</summary>
  Vision-Language-Action (VLA) models promise to bring end-to-end reasoning to autonomous driving, but their computational cost remains far too high for real-time control. The core challenge is structural: VLA inference is not a single bottleneck but a cascade of four. Visual encoding wastes compute on overlapping video frames; language-model prefill recomputes context that could be carried over from the previous timestep; reasoning tokens are generated serially despite low entropy; and flow-match...
  </details>

- **2026-08-13** — Jiacheng Guo, Suozhi Huang, Yunlong Gao et al. — [AQuA: Recursively Self-Improving Quantitative Trading Research Agents](http://arxiv.org/abs/2608.12841v1)
  <details><summary>📄 Abstract</summary>
  We study recursive self-improvement at the level of quantitative-investment research: whether an autonomous system can use evidence from earlier experiments to improve the hypotheses and candidates proposed in later iterations. We present AQuA, which comprises two separate language-model-driven research systems: one for symbolic factor discovery and one for trainable model development. The two systems do not share agents, memories, candidate spaces, or research state. Instead, each independently...
  </details>

- **2026-08-13** — Chengyang He, Tahreem Arif, Marko Zivkovic et al. — [CRAFT: LLM-Based Iterative Refinement for Temporal Reasoning over Clinical Narratives](http://arxiv.org/abs/2608.12779v1)
  <details><summary>📄 Abstract</summary>
  Understanding the temporal progression of symptoms in clinical narratives is critical for disease monitoring, safety surveillance, and causality assessment. Clinical narratives, however, rarely provide explicit temporal anchors. Current approaches to temporal information reasoning focus predominantly on pairwise relation classification across multi-visit and timestamp-rich records, leaving the reconstruction of structured symptom trajectories from individual anchor-sparse reports largely unaddre...
  </details>

- **2026-08-13** — Habib Ammari, Yat Tin Chow, Fuqun Han — [Scattering by a medium with self-similar or fractal structure](http://arxiv.org/abs/2608.12728v1)
  <details><summary>📄 Abstract</summary>
  We develop a topological framework for wave scattering by a medium with self-similar or prefractal geometry. Physical scaling identities motivate an auxiliary boundary-integral model that is periodic in logarithmic scale, and the Bloch-Floquet-Zak transform fiberizes its interscale coupling. For sufficiently small, well-separated components, equilibrium densities define a computable finite-dimensional projected matrix, while Riesz projections select the corresponding invariant spectral subspace ...
  </details>

- **2026-08-13** — Abdul Mueez, Yogesh S. Rawat, Shruti Vyas — [A Generative Approach for Improving Multi-Label Defect Classification in Photovoltaic Modules](http://arxiv.org/abs/2608.12725v1)
  <details><summary>📄 Abstract</summary>
  This paper addresses the challenge of multi-label defect classification in electroluminescence (EL) images of photovoltaic (PV) cells. Training models on images where multiple defects co-occur creates learning ambiguity, making it difficult to disentangle visual features for specific defect types, a problem compounded by the scarcity of examples for individual classes. To tackle this, we introduce Generative Defect Isolation (GDI), utilizing the LaMa inpainting model with Fast Fourier Convolutio...
  </details>

- **2026-08-13** — Gehan Zheng, Matthew Johnson-Roberson, Weiming Zhi — [ContactGuard: Pre-Contact Execution Monitoring with Action-Conditioned Latent World Models](http://arxiv.org/abs/2608.13438v1)
  <details><summary>📄 Abstract</summary>
  Contact-rich manipulation failures are often detected only after the robot has committed to contact. This is especially limiting in wrist-camera setups: close gripper--object views help observe contact, but a poor approach may already push, miss, slip, or disturb the object before conventional detectors react. We introduce \emph{ContactGuard}, a pre-contact execution monitor for chunked visuomotor policies. Given the policy's planned action chunk, ContactGuard predicts its short-horizon conseque...
  </details>

- **2026-08-13** — Charles Koll, Houssam Abbas — [Runtime Monitoring of Distributed Cyber-Physical Systems Without a Global Clock](http://arxiv.org/abs/2608.13486v1)
  <details><summary>📄 Abstract</summary>
  We give the first theoretical characterization, and the first algorithm, for continuous monitoring of a distributed Cyber-Physical System (CPS) against a dense-time temporal logic specification. A distributed CPS is composed of multiple agents, each with a local clock; these clocks drift from each other, so there is no well-defined global time. When monitoring such a system's output signal against a temporal logic specification, it is not evident how to interpret the temporal constraints of the ...
  </details>

- **2026-08-13** — Paul Savala — [Jointly Predicting Courses and Grades Using a Transformer-Based Model](http://arxiv.org/abs/2608.13409v1)
  <details><summary>📄 Abstract</summary>
  Existing predictive models in learning analytics often treat student academic history as a simple sequence, overlooking the concurrent nature of courses taken within a semester. This simplification can lead to inaccurate performance predictions, particularly for students with heavy or challenging course loads. This paper introduces a TRansformer for Academic Course-grade Estimation (TRACE) that addresses this limitation by jointly predicting both the set of courses a student will take and their ...
  </details>

- **2026-08-13** — Alexander Bräuer, Benjamin Cauchi, Nils Strodthoff — [Foundation models for movement data: Are they ready for prime-time?](http://arxiv.org/abs/2608.13316v1)
  <details><summary>📄 Abstract</summary>
  Foundation models (FMs) trained on large-scale accelerometer data have been proposed as general-purpose feature extractors for health monitoring, but systematic evidence of their advantages is lacking. We present the first comprehensive evaluation of four open-source accelerometer FMs against supervised baselines covering 19 tasks across the domains of activity recognition including activities of daily living, clinical monitoring, and physiological inference. We find task-dependent performance r...
  </details>

- **2026-08-13** — Timilehin B. Aderinola, Ilaria D'Ascanio, Luca Palmerini et al. — [Beyond Simulated Benchmarks: Evaluating Motion Representations for Fall Detection Under Real-World Data Scarcity](http://arxiv.org/abs/2608.13197v1)
  <details><summary>📄 Abstract</summary>
  Falls are a major health concern for older adults, and wearable sensors have been widely explored for detecting falls and enabling timely intervention. However, real-world falls are extremely rare: collecting 100 of them requires an estimated 100,000 days of monitoring, resulting in severely limited labelled data for training machine learning models. Consequently, many approaches rely on simulated datasets, often reporting high laboratory performance but limited real-world generalisation. We pre...
  </details>

- **2026-08-13** — Sam Mao — [Explanatory Engagement Under Rare Anomalous Failure: Asymptotic Rarity in Model Behavior (or: The Asymptotic AI)](http://arxiv.org/abs/2608.13063v1)
  <details><summary>📄 Abstract</summary>
  Prior work on LLM behavior under anomalous conditions asks whether a model notices anomalies. We ask a narrower question: once a model sits in a workflow with a low, controllable failure rate, does its explanatory engagement - length, specificity, self-reported confidence - change as failure grows asymptotically rarer? We built a local, zero-cost harness on three open-weight models (qwen3:8b, llama3.1:8b, mistral:7b) running a repeated tool-call task where one call fails at probability p, swept ...
  </details>


### 📂 alignment
*对齐与安全约束 / Alignment & Safety Constraints* — 56 papers

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

- **2026-08-14** — Darakshan Rashid, Raza Imam, Ufaq Khan et al. — [On the Robustness of Temporal Vision-Language Models for Surgical Endoscopy Videos](http://arxiv.org/abs/2608.14262v1)
  <details><summary>📄 Abstract</summary>
  Temporal vision-language models (TVLMs) offer a reusable, prompt-based interface for surgical video understanding, yet, their robustness under clinically realistic acquisition artifacts in endoscopy remains insufficiently characterized. In practice, degradations such as defocus, haze, motion blur, noise, cautery smoke, and packet loss introduce structured distribution shifts which may compromise video-text alignment. We study the robustness of temporal VLMs under such shifts caused by corruption...
  </details>

- **2026-08-14** — Nan Li, Li Zhou, Haijun Wang et al. — [Personalized Digital Semantic Communication for Image Transmission with Vision-Language Models](http://arxiv.org/abs/2608.14260v1)
  <details><summary>📄 Abstract</summary>
  Semantic communication (SC) enables bandwidth-efficient wireless image transmission, but most existing SC schemes are user-agnostic and ignore receiver-dependent semantics. To address this issue, we propose a personalized digital semantic communication (PDSC) framework that integrates a vision-language model (VLM)-based semantic encoder with a latent diffusion model (LDM)-based semantic decoder. Specifically, the semantic encoder extracts source-aware personalized semantic tokens from both the s...
  </details>

- **2026-08-14** — Jeongwan Shin, Jaehyeon Kim, Donguk Ko et al. — [Can Language Models Understand mmWave Data? Benchmarking Large Language Models for mmWave Radar-Based Human Understanding](http://arxiv.org/abs/2608.14179v1)
  <details><summary>📄 Abstract</summary>
  Large language models (LLMs) have shown remarkable reasoning and generative capabilities, motivating their use as universal reasoning engines for perception. While modern approaches such as vision-language models (VLMs) have attempted to incorporate reasoning capabilities into visual sensing, the integration of LLMs with the millimeter-wave (mmWave) modality-despite its unique advantages under low light and occlusion-remains largely unexplored. The principal bottlenecks stem from the scarcity of...
  </details>

- **2026-08-14** — Yanbo Ding, Yijia Fan, Caihua Shan et al. — [Beyond Text Conditioning: A Systematic Study of MLLM-DiT Fusion for Video Generation](http://arxiv.org/abs/2608.14043v1)
  <details><summary>📄 Abstract</summary>
  Diffusion Transformers (DiTs) have become the dominant paradigm for high-fidelity video generation, yet their ability to perform high-level semantic planning remains limited. While hybrid architectures integrating MLLMs with diffusion backbones have shown strong advantages in image synthesis, such designs remain underexplored in video generation, where existing approaches often treat MLLMs primarily as frozen feature encoders rather than semantic generators. To fill this gap, we systematically s...
  </details>

- **2026-08-14** — Mathew Varghese — [Content Based Video Narration of Gameplay with Vision Language Models](http://arxiv.org/abs/2608.14016v1)
  <details><summary>📄 Abstract</summary>
  Live game commentary is scarce: it exists for professional esports broadcasts and almost nowhere else. We present a content-based video narration system that produces spoken, esports-style commentary for arbitrary gameplay recordings using a general-purpose vision-language model (VLM) and a text-to-speech back end, with no game-specific instrumentation, no engine telemetry, and no task-specific training. Three mechanisms carry the system. Temporal mosaic packing arranges nine uniformly sampled f...
  </details>

- **2026-08-13** — Dananjay Srinivas, Saksham Khatwani, Maria Pacheco — [Toward a Gricean Retreat: Probing LLMs for Knowledge Boundaries and Referent Specificity](http://arxiv.org/abs/2608.13484v1)
  <details><summary>📄 Abstract</summary>
  When asked about entities outside their knowledge boundary, LLMs routinely fabricate plausible-sounding details rather than backing off to safer, more general claims. We frame this failure through a Gricean lens: a cooperative speaker who is uncertain about a referent retreats up the specificity hierarchy, trading informativeness for truthfulness. We ask whether LLMs have the ingredients to perform this retreat. Using a T-REx-based benchmark that varies entity familiarity and referent specificit...
  </details>

- **2026-08-13** — Yusen Tan, Yixuan Chen, Zheng Fang et al. — [Simulation-to-real transfer learning for infrared spectroscopic chemical sensing and analysis from molecules to complex samples](http://arxiv.org/abs/2608.13341v1)
  <details><summary>📄 Abstract</summary>
  Infrared (IR) spectroscopy is widely used for chemical sensing, but extracting reliable chemical information from spectra remains challenging. Conventional interpretation is labor-intensive, relies on prior knowledge and reference spectra, and is difficult to scale, whereas most machine-learning methods are tailored to individual tasks or datasets, require large labeled training sets, and transfer poorly across analytical objectives and experimental datasets. Here we introduce UltraIR, a foundat...
  </details>

- **2026-08-13** — Yanwen Peng, Delvin Ce Zhang, Xi Wang et al. — [StateBridge: Training-free Hidden-state Alignment for Latent Communication in LLM Multi-Agent Systems](http://arxiv.org/abs/2608.13317v1)
  <details><summary>📄 Abstract</summary>
  Large language model based multi-agent systems usually communicate in text, i.e., using discrete tokens. However, text introduces a discrete bottleneck. Converting the sender's continuous hidden states into discrete tokens discards information that token identities alone cannot capture. Recent work proposes latent communication as an alternative, where agents transmit hidden representations directly without converting them to text. However, existing latent methods either inject working memory la...
  </details>

- **2026-08-13** — Wafa Al Ghallabi, Ritesh Thawkar, Sara Ghaboura et al. — [How Good are Foundation Models in Longitudinal MRI Disease Progression Reasoning?](http://arxiv.org/abs/2608.13309v1)
  <details><summary>📄 Abstract</summary>
  Magnetic Resonance Imaging (MRI) interpretation is fundamental to clinical decision-making, requiring radiologists to integrate multi-view anatomical planes across sequential timepoints while precisely localizing interval changes. However, existing vision-language benchmarks remain confined to single-timepoint, single-view interpretation, failing to capture the temporal-spatial reasoning essential to radiologic practice. We introduce the Time-Aware Multi-View MRI Benchmark, an evaluation framewo...
  </details>

- **2026-08-13** — Hongjie Xia, Yiding Liu, Yifan Hu et al. — [Into the ORBIT for Time Series: Training Regimes for Foundation Models](http://arxiv.org/abs/2608.13262v1)
  <details><summary>📄 Abstract</summary>
  Time series foundation models (TSFMs) have advanced primarily through architectural innovation, while training regimes for large-scale heterogeneous corpora remain under-explored. As a result, pre-training distributions are often poorly controlled with respect to domain imbalance, context requirements, prediction horizons, and missingness. We introduce ORBIT (Omni-Range Bootstrap Incremental Training), a training paradigm that makes this distribution explicit and controllable. ORBIT combines Boo...
  </details>

- **2026-08-13** — Long Hoang Nguyen, Brice Valentin Kok-Shun, Guangyu Du et al. — [Follow the Norm: Accounting for Fine-Tuning and Prompt Effects on Model Rationales](http://arxiv.org/abs/2608.13250v1)
  <details><summary>📄 Abstract</summary>
  Normative datasets are often used to train and align AI systems, but the norms they contain can function as action-guiding patterns rather than neutral moral knowledge. We propose treating the AI system as a proxy actor and test whether dataset-level norms can shift it away from its baseline safety behavior when it faces high-conflict dilemmas. We make three contributions. First, we demonstrate in controlled experiments that norm-breaking fine-tuning yields norm-divergent actions justified by se...
  </details>

- **2026-08-13** — Yilin Wang, Yuchun Fan, Weidong Bao et al. — [Better Decomposition, Free Aggregation: A Synthesizer-Folding Framework for Multilingual Multi-Hop Question Answering](http://arxiv.org/abs/2608.13160v1)
  <details><summary>📄 Abstract</summary>
  Multilingual retrieval-augmented generation (mRAG) equips large language models with access to globally distributed external knowledge for complex multilingual question answering. Recent approaches either translate retrieved documents into English or the query language to bridge the cross-lingual semantic gap, or decompose a complex query into sub-questions and aggregate the intermediate reasoning process. However, both lines of work suffer from two limitations. First, one-size-fits-all translat...
  </details>

- **2026-08-13** — Chenrun Wang, Mingxuan Zhu, Tiancheng Huang et al. — [LigBench: A Unified and Human-Aligned Benchmark for LLM-based Research Idea Generation](http://arxiv.org/abs/2608.13136v1)
  <details><summary>📄 Abstract</summary>
  With the rapid advancement of large language models (LLMs), research idea generation has attracted increasing attention. Existing approaches enable LLMs to retrieve relevant literature and propose novel ideas for research areas. However, current evaluation practices for idea generation remain fragmented and lack objective standards, often relying on direct LLM scoring, which limits their ability to provide unified and reliable assessments across a coherent distribution of generated ideas. To add...
  </details>

- **2026-08-13** — Lucia Malíčková — [Behavioral Reprogramming of Open-Weights Models: Cognitive Plasticity and Alignment Bounds](http://arxiv.org/abs/2608.13069v1)
  <details><summary>📄 Abstract</summary>
  Large language models (LLMs) are predominantly aligned to function as passive, sycophantic assistants. We challenge this default paradigm by empirically evaluating the cognitive plasticity of open-weight architectures when subjected to rigorous behavioral reprogramming. Our objective is to induce a proactive, Socratic conversational framework, characterized by high-frequency question generation under strictly constrained high-performance computing (HPC) conditions. Through a massively paralleliz...
  </details>

- **2026-08-13** — Jiale Cui, Yueyao Yuan, Kaixi Zhong et al. — [ARAC: Benchmarking Auto-Research's Alignment and Completeness on End-to-End Researchs](http://arxiv.org/abs/2608.12788v1)
  <details><summary>📄 Abstract</summary>
  The rapid advancement of Auto-Research has surfaced a fundamental evaluation challenge: how can we measure the alignment, logical coherence, and evolutionary completeness of its research trajectory with human research behavior? We propose Auto-Research's Alignment and Completeness, ARAC-Bench: a Researcher-Mimicking Evaluation framework that shifts the objective from matching final answers to reproducing high-quality human research processes. The framework operates through two synergistic compon...
  </details>

- **2026-08-13** — Junyi Hu, Tian Bai, Fengyi Wu et al. — [Scaling Representation Diversity: Modulated Attention and Reconstructive Regularization for Visual Grounding](http://arxiv.org/abs/2608.12748v1)
  <details><summary>📄 Abstract</summary>
  Referring Expression Comprehension (REC) is commonly studied under dataset-specific fine-tuning, resulting in specialist models with limited cross-dataset generalization. In this work, we revisit REC from the perspective of unified open-vocabulary grounding and identify representation degeneration as a key obstacle to scaling a single generalist model. To preserve representation diversity, we propose a holistic data-model co-design framework. Architecturally, we introduce the Modulated Attention...
  </details>

- **2026-08-13** — Zhi Qiao, Xintong Wu, Yichu He et al. — [Mr3D-VL: A generalist vision language foundation model for Multiparametric 3D Magnetic Resonance Imaging](http://arxiv.org/abs/2608.12689v1)
  <details><summary>📄 Abstract</summary>
  Multi-parametric magnetic resonance imaging (mpMRI) is a cornerstone for brain tumor diagnosis and treatment, yet current AI models face critical limitations: their lack of natural language interaction and interpretability impedes spatial information integration and cross-modal reasoning required clinically. Key challenges arise from significant physical meaning differences across modalities, spatial misalignment due to scan intervals, and the need for complex multi-feature interpretation in tas...
  </details>

- **2026-08-13** — Danial Sharifrazi, Saadat Behzadi, Julakha Jahan Jui et al. — [The Role of Natural Language Understanding in Multimodal Video-Based Dengue Diagnosis](http://arxiv.org/abs/2608.12677v1)
  <details><summary>📄 Abstract</summary>
  Detecting infection-related behavioral changes in mosquitoes from video data is challenging because mosquitoes are small, move rapidly and irregularly, and are affected by environmental factors such as background, lighting, and shadows, which can make reliable feature extraction difficult. In this study, a YOLO- and Contrastive Language-Image Pre-training (CLIP)-based vision-language framework is proposed to classify mosquito flight frames of uninfected and Dengue virus serotype 2 (DENV2)-infect...
  </details>


### 📂 robustness
*鲁棒性与可靠性 / Robustness & Reliability* — 69 papers

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

- **2026-08-14** — Md Kamrul Islam, Tiphaine Henry, Mattia Salnitri et al. — [A Hybrid LLM-Based Framework for Automated Security Annotation Generation in Business Process Models](http://arxiv.org/abs/2608.14370v1)
  <details><summary>📄 Abstract</summary>
  The modelling and analysis of secure business processes require the incorporation of security annotations into process models. Although BPMN extensions, including SecBPMN2, exist for this purpose, the derivation of accurate and complete security annotations from natural-language specifications remains a manual, expert-intensive, and error-prone task. This paper presents a hybrid framework that takes a BPMN process model and a security requirements document as input and automatically generates se...
  </details>

- **2026-08-14** — Yijiao Zhang, Hongzhe Li — [Generation-Powered Inference for Distribution-Valued Outcomes](http://arxiv.org/abs/2608.14542v1)
  <details><summary>📄 Abstract</summary>
  Modern generative models increasingly produce distribution-valued outputs, such as predicted cellular responses to genetic perturbations in single-cell genomics. While these models provide valuable auxiliary information, they are inherently imperfect, creating a need for statistical methods that leverage their predictions without relying on their correctness. We propose generation-powered inference (GPI), a general framework for improving inference on distribution-valued parameters using auxilia...
  </details>

- **2026-08-14** — Zhelun Wu — [Split the Labor: Separating Evidence Interpretation from Decision Aggregation](http://arxiv.org/abs/2608.14509v1)
  <details><summary>📄 Abstract</summary>
  Systems that ask a language model to reach a conclusion from many sources usually concatenate them into one prompt. This conflates two operations with different requirements. Interpreting a source rewards capacity and context. Combining interpretations rewards fixed arithmetic, comparability across instances, and the option to return nothing. Once separated, the design problem becomes the interface between them. We propose a four-field evidence tuple (hypothesis, reliability bucket, rationale, p...
  </details>

- **2026-08-14** — Yiderigun Borjigin, Alexander Hermann, Christian Cyron et al. — [AnchorBench: A Multi-Pathway Benchmark for the Anchoring Effect in LLMs](http://arxiv.org/abs/2608.14320v1)
  <details><summary>📄 Abstract</summary>
  The anchoring effect is a cognitive bias in which an initial reference value shifts a later judgment toward itself. This effect is well established in human judgment and decision-making, and recent work suggests that large language models (LLMs) exhibit similar behavior. However, existing work on anchoring in LLMs typically evaluates only a narrow set of anchor pathways and rarely distinguishes irrelevant from plausible anchors. We introduce AnchorBench, a benchmark for the anchoring effect in L...
  </details>

- **2026-08-14** — Anandaroop Ray — [Extending Occam's inversion with lasso fusion, overcomplete dictionaries, and isotropic total variation regularisation](http://arxiv.org/abs/2608.14225v1)
  <details><summary>📄 Abstract</summary>
  Occam's inversion is a robust algorithm to perform nonlinear geophysical inversion. It provides the smoothest model within observation noise, thereby discouraging geological overinterpretation. While Occam originally penalised l2 model roughness, l1 can be used to provide models that are visually sharp. However, l1 regularised geophysical inversion has diverged from the larger body of statistics and imaging literature. For example, l1 regularisation with a difference operator (i.e., total variat...
  </details>

- **2026-08-14** — Hengzhe Zhang, Qi Chen, Bing Xue et al. — [Adaptive Protection for Evolutionary Feature Construction in Symbolic Regression with Application to Credit Classification](http://arxiv.org/abs/2608.14209v1)
  <details><summary>📄 Abstract</summary>
  Evolutionary feature construction has shown strong promise in symbolic regression by automatically discovering informative transformations of input features that enhance a simple base learner. However, existing approaches often lack explicit mechanisms to preserve important constructed features discovered during evolution, and valuable genetic material can be lost when genetic operators disrupt effective features. This paper introduces an adaptive protection mechanism that leverages feature impo...
  </details>

- **2026-08-14** — Arne Kröger, Ralf Buschermöhle, Wilhelm Hasselbring et al. — [Reinforcement Learning-Based Production Scheduling in an Industry-Based Coating Scenario Using the Digital Model Playground](http://arxiv.org/abs/2608.14122v1)
  <details><summary>📄 Abstract</summary>
  Production scheduling in complex manufacturing environments is challenging when sequence-dependent setup times, stochastic disturbances, and due-date constraints must be addressed simultaneously. While reinforcement learning (RL) methods have shown promising results in research, most studies rely on simplified benchmark processes, limiting their industrial relevance. This paper demonstrates the applicability of RL-based scheduling in an industry-inspired coating process that reflects practical c...
  </details>

- **2026-08-14** — Juli Huang, Hannah Clay, Sajjad Beygi et al. — [MACS: A Hybrid Multi-Agent Framework for Reliable Conversational E-Commerce Recommendation](http://arxiv.org/abs/2608.14068v1)
  <details><summary>📄 Abstract</summary>
  Conversational recommendation for e-commerce is increasingly mediated by large language models (LLMs), yet many real-world deployments operate under a stricter requirement: recommendations must be drawn only from a merchant's fixed catalog, without web search or unsupported product claims. In this setting, the main challenge is reliability under hard constraints: the system must satisfy user requirements, remain grounded in available inventory, and preserve preferences across multiple conversati...
  </details>

- **2026-08-14** — Yi Ding, Yanzhao Yu, Xili Dai et al. — [Evolve Vision-Language-Action Model into an Agent with On-the-fly Tool-use](http://arxiv.org/abs/2608.14047v1)
  <details><summary>📄 Abstract</summary>
  This paper integrates end-to-end Visual-Language-Action (VLA) models with agentic tool-use to propose Agentic Robot with Tool-use (ART). ART is a tool-injection framework that tunes any VLA model to leverage off-the-shelf tool modules for low-level vision, high-level affordance, and embodiment enhancement. Compared to vanilla VLA models with a whole continuous action solution space, ART reduces the complexity of the action solution space through tool-use, which not only improves generalizability...
  </details>

- **2026-08-13** — Daniel Perkins, John Squires, Janou Milligan et al. — [MLLM-Routed Heterogeneous Ensembles for Robust Cross-Dataset Image Classification](http://arxiv.org/abs/2608.13463v1)
  <details><summary>📄 Abstract</summary>
  Modern image classification models excel when trained on single task-specific datasets but often struggle to generalize across domains and difficulty levels. We propose ARMDIL, an Adaptive Router for Multi-Domain Image classification with LLMs. ARMDIL is an ensemble that uses a multimodal large language model (MLLM) agent to dynamically route each image to the most suitable vision backbone. Our diverse ensemble employs convolutional neural networks (ResNets), self-supervised representation learn...
  </details>

- **2026-08-13** — Zhe Ye, Hantao Lou, Yuechun Sun et al. — [Vero: Can AI Agents Build Formally Verified Software Repositories?](http://arxiv.org/abs/2608.13522v1)
  <details><summary>📄 Abstract</summary>
  AI agents are increasingly used for programming, but do not provide any guarantee on the correctness of generated code. Verified code generation, in which an agent produces both an implementation and a machine-checked proof of its specification, offers a stronger path toward trustworthy AI-generated software. Existing benchmarks in this direction either focus on individual functions or only evaluate proof generation with provided implementations. It is still an open question whether agents can m...
  </details>

- **2026-08-13** — Anna Sterna, Kacper Dudzic, Karolina Drożdż et al. — [How LLMs Respond to Escalating Delusions: Four Longitudinal Trajectories of Model Behavior](http://arxiv.org/abs/2608.13017v1)
  <details><summary>📄 Abstract</summary>
  The widespread use of LLMs among psychiatric populations has raised concerns regarding their safety and potential iatrogenic impact in the context of AI psychosis. While growing literature conceptualizes AI psychosis and documents case studies, empirical evidence tracing AI-exacerbated psychotic processes remains scarce. We propose and test a longitudinal qualitative evaluation design, supported by automated metrics, to assess mainstream LLMs' potential to exacerbate psychosis. Fifteen widely us...
  </details>

- **2026-08-13** — Rathijit Aich, Nirjhar Das, Mahfuzulhoq Chowdhury — [HybridRAG-BN: A Retrieval-Augmented Framework with Fine-Tuned Verification for Bangla KBQA](http://arxiv.org/abs/2608.13004v1)
  <details><summary>📄 Abstract</summary>
  Knowledge-base question answering (KBQA) systems rely on effective retrieval and reasoning mechanisms to generate accurate answers from external knowledge sources. However, developing reliable KBQA systems for low-resource languages such as Bangla remains challenging due to limited retrieval-focused research, scarce language resources, and difficulties in grounding generated responses in external knowledge. In this work, we propose HybridRAG-BN, a retrieval-augmented framework for Bangla KBQA th...
  </details>

- **2026-08-13** — Kwangyik Jung, Eungchang Mason Lee, Taekjun Oh et al. — [ASPIRE-VINS: Adaptive Spline-based Visual-inertial Navigation System With Robust 3D Measurement Residuals](http://arxiv.org/abs/2608.12840v1)
  <details><summary>📄 Abstract</summary>
  Visual-inertial navigation systems estimate six-degree-of-freedom motion by fusing visual and inertial data. Modern discrete-time methods with IMU preintegration provide strong accuracy and efficiency, but keyframe-based representations can be less flexible when residuals must be evaluated at arbitrary timestamps or when motion-dependent temporal resolution is needed. Continuous-time splines address this issue by representing the trajectory as a smooth temporal function, but uniformly spaced kno...
  </details>

- **2026-08-13** — Qi Zhao, Qirui Li, Hanlin Tang et al. — [SCOPE: Subspace Clustering with Online Per-Head Top-K Estimation for Sparse Video Attention](http://arxiv.org/abs/2608.12780v1)
  <details><summary>📄 Abstract</summary>
  Diffusion Transformers (DiTs) incur quadratic self-attention cost over spatiotemporal tokens. Existing training-free sparse attention methods often construct sparse masks from block-level or cluster-level proxy scores, which can obscure fine-grained differences among keys and miss high contribution keys under aggressive sparsity. Moreover, such proxy scores may yield overly concentrated softmax distributions, causing Top-$p$ to retain too few keys for some query clusters. Although a fixed Top-$k...
  </details>

- **2026-08-13** — Haolong Chen, Zhengyuan Xin, Liang Zhang et al. — [Error-Aware Reverse Auction Mechanism for Large Language Model Routing](http://arxiv.org/abs/2608.12719v1)
  <details><summary>📄 Abstract</summary>
  Routing each query to a cost-effective large language model (LLM) is critical for balancing quality and cost, yet most routers rely on a centralized task center to predict model performance, creating an information-risk mismatch and a scalability bottleneck as the model pool grows. We propose a market-based routing paradigm that shifts ex-ante prediction to LLM providers via a reverse auction, where providers bid with self-predicted success probabilities and execution costs. To account for inher...
  </details>

- **2026-08-13** — Lei Bai, Jiaqi Cao, Chiyu Chen et al. — [Intern-S2-Preview: Scientific Agentic Foundation Model](http://arxiv.org/abs/2608.13505v1)
  <details><summary>📄 Abstract</summary>
  Scientific discovery increasingly requires AI systems that can reason over scientific evidence of heterogeneous modalities, interact with scientific tools and environments, and sustain progress across long task horizons. We present Intern-S2-Preview, a series of scientific agentic foundation models designed to support multimodal scientific understanding, reasoning, generation, and long-horizon tasks. The training pipeline begins with scientific multimodal pre-training over rendered scientific do...
  </details>

- **2026-08-13** — Yanming Yang, Chenxi Song, Ping Wang et al. — [GS$^{2}$CI: Robust Gaussian Splatting For Snapshot Compressive Imaging via Large Vision Model Priors](http://arxiv.org/abs/2608.13502v1)
  <details><summary>📄 Abstract</summary>
  Snapshot Compressive Imaging (SCI) offers an efficient solution for high-speed video acquisition and, under exposure-time camera--scene relative motion, multi-view scene capture by compressing temporal or spatial information into a single 2D measurement. While recent studies have explored SCI for 3D scene reconstruction, existing methods struggle with significant challenges due to information loss, limited viewpoint diversity, and the computational burden of jointly optimizing 3D representations...
  </details>

- **2026-08-13** — Mostafa Mansour, Mansoura Oumennana — [Quantum correlations and Basis-Independent Coherence Distribution in Two Gravitational Cat States](http://arxiv.org/abs/2608.13493v1)
  <details><summary>📄 Abstract</summary>
  We study the distribution of quantum correlations and basis-independent coherence in a pair of massive particles confined in a double-well potential and coupled through their mutual Newtonian gravitational interaction. Non-classical correlations are characterized using Bures distance of entanglement and quantum discord, while coherence is quantified through the square root of the quantum Jensen--Shannon divergence (QJSD) from the maximally mixed state, yielding a measure that is invariant under ...
  </details>

- **2026-08-13** — Zixuan Lan, Yanhong Li, Jiawei Zhou — [Reduced Matrix Multiplication: Input-Adaptive Matrix-Product Reduction for LLM Inference](http://arxiv.org/abs/2608.13426v1)
  <details><summary>📄 Abstract</summary>
  Transformer-based language models achieve strong performance but incur substantial inference cost due to repeated high-dimensional matrix multiplications. We propose Reduced Matrix Multiplication (RMM), a training-free, input-adaptive inference method that reduces Transformer matrix products by selecting informative slices along their contraction dimensions, without modifying model weights. Under a simple retention-ratio control, RMM provides a smooth and predictable accuracy-efficiency trade-of...
  </details>

- **2026-08-13** — Teng Lin, Yuyu Luo, Nan Tang — [Structure then Query: Enabling Precise Analytical Queries over Unstructured Documents](http://arxiv.org/abs/2608.13384v1)
  <details><summary>📄 Abstract</summary>
  Unstructured documents constitute the majority of enterprise and web data. With the rapid development of large language models(LLMs), researchers have started to build data systems that analyze unstructured textual documents like operating on databases. However, because mainstream retrieval methods still relies on fuzzy matching based on vector similarity, accurately obtaining information and performing structured analysis and reasoning remains a major challenge. To address these limitations, An...
  </details>

- **2026-08-13** — Renlei Jiang, Xiaoyu Zhang, Chuanhou Gao et al. — [Input-to-state stability of chemical reaction networks with application to molecular computation](http://arxiv.org/abs/2608.13302v1)
  <details><summary>📄 Abstract</summary>
  In biological reaction systems, reaction rates may vary over time due to environmental fluctuations, regulation, or coupling with other reaction modules. Input-to-state stability (ISS) provides a useful tool for analyzing the robustness of time-varying chemical reaction networks (CRNs). Existing ISS results for CRNs typically rely on restrictive structural assumptions, such as zero deficiency, a single linkage class, or weak reversibility. This paper makes two main contributions. First, we estab...
  </details>

- **2026-08-13** — Paul Osemudiame Oamen, Owusu-Banahene Osei, Ananya Mukherjee et al. — [How Do VLMs Behave When Blind or Misled? Behavioral Evaluation of VLMs on Scientific Figures](http://arxiv.org/abs/2608.13267v1)
  <details><summary>📄 Abstract</summary>
  Existing vision-language model (VLM) benchmarks emphasize perception and reasoning accuracy (how well VLMs describe and reason about what they see in an image), with limited attention to behavioral reliability under uncertainty (how they behave when visual evidence is missing or misleading). We introduce SciFigBench, a diagnostic VLM benchmark for scientific figure understanding that jointly evaluates perception, reasoning, and behavioral reliability under uncertainty. It contains 250 figures wi...
  </details>

- **2026-08-13** — Berk Hadzhamolla, Alexander Johannes Stasik, Signe Riemer-Sørensen — [Virtual Temperature Sensors in Power Transformers Using Neural Ordinary Differential Equations](http://arxiv.org/abs/2608.13260v1)
  <details><summary>📄 Abstract</summary>
  Accurate modeling and forecasting of power transformer thermal behavior are critical for reliability, asset lifetime, and optimized power system operation. Numerical approaches such as finite element methods (FEM) and computational fluid dynamics (CFD) offer high fidelity but are computationally expensive, require complex mesh generation, and are often impractical for real-time or large-scale applications, particularly when transformer geometries are unknown. Lumped-parameter thermal models are ...
  </details>

- **2026-08-13** — Peng Ling, Yingda Yin, Lingting Zhu et al. — [CoverPrune: Coverage-Driven Token Pruning for 3D VLMs via Optimal Transport](http://arxiv.org/abs/2608.13226v1)
  <details><summary>📄 Abstract</summary>
  While 3D Vision-Language Models (3D VLMs) have demonstrated remarkable spatial reasoning capabilities, they suffer from massive visual token counts that create severe computational bottlenecks during inference. Existing token pruning methods primarily rely on diversity-based selection, discarding similar tokens to maximize dispersion. However, in 3D environments, this approach frequently drops representative prototype tokens in favor of outliers, breaking the multi-view consistencies and geometr...
  </details>

- **2026-08-13** — Mallika Garg, Debashis Ghosh, Pyari Mohan Pradhan — [UniCon-Former: Unified Convolution Transformer is All You Need for Hand Gesture Recognition](http://arxiv.org/abs/2608.13217v1)
  <details><summary>📄 Abstract</summary>
  Convolutional Neural Networks (CNNs) capture local features efficiently but struggle with global context due to their limited receptive field. On the other hand, transformers effectively capture global dependencies through self-attention but suffer from high redundancy and computational costs. Thus, to leverage the advantages of both CNNs and transformers, we propose a unified model (UniCon-Former) that aims to provide robust and efficient performance on dynamic hand gesture recognition. The uni...
  </details>

- **2026-08-13** — Fnu Pramono, John Cai, Sourabh Kulkarni — [TRAPSBench: Vision-Language Models Encode but Fail to Express Epistemic Restraint](http://arxiv.org/abs/2608.13167v1)
  <details><summary>📄 Abstract</summary>
  When visual evidence is occluded or chaotic, models should abstain. In this paper, we show that Vision-Language Models (VLMs) can internally distinguish when abstention is required, but fail to express it anyway. We introduce TRAPSBench, a procedurally generated video benchmark of 1,404 matched physics pairs in which a single targeted change renders the outcome undeterminable from the visual evidence. Furthermore, we introduce Penalized Epistemic Calibration Score (PECS), a new robust metric tha...
  </details>

- **2026-08-13** — Jakub Peleška, Gustav Šír — [Incremental Evaluation and Training in Relational Deep Learning](http://arxiv.org/abs/2608.13023v1)
  <details><summary>📄 Abstract</summary>
  Relational Deep Learning (RDL) models multi-tabular databases as temporal heterogeneous graphs to enable end-to-end representation learning. However, prevailing RDL evaluation practices rely on static, single-episode dataset snapshots, overlooking the continuous, time-evolving nature of real-world databases. Consequently, current RDL benchmarks fail to capture how model performance changes as new data accumulates over time. To address this limitation, we introduce an incremental, multi-episode e...
  </details>

- **2026-08-13** — Fanyu Wang, Chetan Arora, Zhenping Xie et al. — [Requirements-Augmented Generation for Trustworthy Acceptance Testing of LLM-Based Software](http://arxiv.org/abs/2608.12970v1)
  <details><summary>📄 Abstract</summary>
  LLM-based software (LBS) integrates large language models as core components to deliver flexible, personalised responses. Unlike traditional software with deterministic outputs, LBSs exhibit context-dependent, stochastic behaviour that renders classical acceptance testing and test oracles insufficient: the same query may require fundamentally different responses depending on user personas and software context. This gap creates an urgent need for automated acceptance testing frameworks that auton...
  </details>

- **2026-08-13** — Ankita Joshi — [A Deep RL based Framework for Targeted White Matter Tractography](http://arxiv.org/abs/2608.12960v1)
  <details><summary>📄 Abstract</summary>
  Fiber tractography's ability to reconstruct the brain's structural pathways, has made it a crucial component of modern neuroimaging, enabling detailed, non-invasive mapping of structural connectivity and supporting a wide range of neurological research and clinical applications. However, despite its importance, tractography remains a challenging task due to the inherent complexity of white matter structure and its susceptibility to false positives, which can lead to the misrepresentation of crit...
  </details>

- **2026-08-13** — Palaash Goel, Ayan Sengupta, Akshay Nambi et al. — [Unifying Depth and Width Pruning for LLMs via Binary Knapsack Optimization](http://arxiv.org/abs/2608.12953v1)
  <details><summary>📄 Abstract</summary>
  Structured pruning is a promising approach for compressing large language models (LLMs), yet existing methods rely heavily on greedy heuristics that produce myopic decisions, and often fail to precisely meet target compression budgets. We present SNIPER, a two-stage structured pruning framework that solves a knapsack optimization over coarse-granularity components to yield conditionally optimal parameter allocations with respect to fixed importance estimates, followed by a fine-grained pruning s...
  </details>


### 📂 watermark
*水印与溯源 / Watermarking & Provenance* — 19 papers

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

- **2026-08-13** — Yuto Nishida, Hirokazu Kiyomaru, Yusuke Oda et al. — [Measuring Task-Agnostic Training Data Influence Across Language Model Pretraining](http://arxiv.org/abs/2608.13515v1)
  <details><summary>📄 Abstract</summary>
  Measuring training data influence consistently across language model pretraining is challenging. It is difficult to select downstream tasks or validation sets representative of a model's general capabilities, and reliance on task performance at intermediate checkpoints complicates comparisons across training. We propose a measure of training data influence that does not require selecting a downstream task or validation set as the attribution target. Specifically, we define an example's influence...
  </details>

- **2026-08-13** — Saveliy Batruin — [Capability Sheaves for Compositional Agent-Harness Repair: Controlled Quotients and a Real-Repository Stress Test](http://arxiv.org/abs/2608.13228v1)
  <details><summary>📄 Abstract</summary>
  Agent harnesses combine retrieval, routing, state, provenance, and verification, but locally successful components may disagree on shared state. We model this failure with a finite \emph{capability sheaf}: stalks encode typed behavior signatures, restriction maps retain shared fields, and accepted runs are useful global sections. An exact finite constraint-satisfaction problem (CSP) defines acceptance, while a linearized relative cohomology class provides a diagnostic and search feature.   A con...
  </details>

- **2026-08-13** — Lei You — [Decomposition of Evidence, Contradiction, and Fragility in Perturbation Responses](http://arxiv.org/abs/2608.12935v1)
  <details><summary>📄 Abstract</summary>
  Perturbation methods explain model decisions by measuring prediction changes under altered inputs, but response magnitude tells us only how much a model reacts, not what that reaction means. The same magnitude can support the final factual-counterfactual difference, oppose it, or arise strongly along the perturbation path yet vanish at the endpoint. We therefore track how the contrast develops as paired inputs are progressively revealed, using the final contrast to interpret the trajectory. We i...
  </details>

- **2026-08-13** — Bobo Li, Hao Fei, Tianjie Ju et al. — [OmniScientist: An Omni-Modal Omni-Discipline AI Scientist](http://arxiv.org/abs/2608.13558v1)
  <details><summary>📄 Abstract</summary>
  Recent advances in foundation models have enabled AI scientists to automate increasingly complete research workflows, from hypothesis generation and code execution to manuscript preparation. Yet workflow coverage alone does not provide access to the full evidence on which scientific discovery depends. Existing systems typically reason over text, code, labels, or precomputed summaries, leaving scientifically decisive spatial, temporal, cross-channel, and procedural relations unavailable to the ag...
  </details>

- **2026-08-13** — Saisha Shetty, Satvik Tripathi, Austin Lin et al. — [MARC v1: An Open-Source Multi-Agent Framework for Clinical AI Reasoning and Coordination](http://arxiv.org/abs/2608.13476v1)
  <details><summary>📄 Abstract</summary>
  We present Multi-Agent Reasoning and Coordination (MARC), an open-source framework that replaces monolithic LLM prompting with deterministic multi-agent orchestration for clinical reasoning. MARC coordinates role-specialized agents for extraction, reasoning, answer generation, and evaluation, with explicit context passing and traceable intermediate outputs, enabling stage-wise failure attribution. We additionally introduce a Decomposer module that generates task-specific agent prompts from a pla...
  </details>

- **2026-08-13** — Amogh Joshi, Animesh Mukherjee, Sergey Utyuzhnikov — [DMDIntel: Interpreting Large Language Models via Dynamic Mode Decomposition](http://arxiv.org/abs/2608.13048v1)
  <details><summary>📄 Abstract</summary>
  In this work, we introduce DMDIntel which uses dynamic mode decomposition (DMD) to make the predictions made by LLMs in a classification task interpretable. It develops an input attribution pipeline, that first decomposes the hidden states of an LLM into prominent patterns, also known as modes, and then associates ranks to the input tokens based on the projection values on those modes. Rigorous experiments across three datasets and three model families consistently show that the ranked attributi...
  </details>

- **2026-08-13** — Junzhi Li, Peng He, Qirui Ji et al. — [Discovering Efficient and Explainable Communication Topologies for LLM-based Multi-Agent Systems via Causal Inference](http://arxiv.org/abs/2608.12921v1)
  <details><summary>📄 Abstract</summary>
  The performance of large language model (LLM)-based multi-agent systems (MAS) largely depends on effective communication topologies. Existing topology generation methods, however, typically learn communication topologies through black-box optimization driven solely by task-level rewards. While effective, such optimization provides little insight into why particular communication edges are selected, making it difficult to identify the critical communication subgraphs responsible for successful co...
  </details>


### 📂 unlearning
*机器遗忘 / Machine Unlearning* — 3 papers

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
*安全评测与基准 / Safety Benchmarks & Evaluation* — 1 papers

- **2026-08-17** — Peng Du, Kiran Kamble, Rakshith Vasudev et al. — [Palmyra x6 Technical Report: An Agentic, Tool-Use Model Post-Trained via Anchored Supervised Fine-Tuning](http://arxiv.org/abs/2608.16620v1)
  <details><summary>📄 Abstract</summary>
  Palmyra x6 is a large language model optimized for use with enterprise-oriented agentic tasks. The model was built by post-training a Mixture-of-Experts base model with Anchored Supervised Fine-Tuning on a compact corpus of verified, synthetic tool-use trajectories, optimized with a Muon + Adam hybrid. The recipe is deliberately conservative and deliberately controlled: 626 trajectories, a single epoch, a low learning rate, and a KL anchor to the frozen base. The model shows substantial gains ov...
  </details>


### 📂 survey
*综述与系统化 / Surveys & Systematization* — 5 papers

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

- **2026-08-14** — Ross D. King — [The Past and Future of AI Scientists](http://arxiv.org/abs/2608.14407v1)
  <details><summary>📄 Abstract</summary>
  We present a survey of the past and future of AI Scientists: machines capable of automating science. AI Scientists can originate hypotheses, deduce their consequences, design and execute experiments, interpret their results, and revise their beliefs. Such systems are integrated scientific agents, connected to the literature, formal knowledge, mathematical models, simulations, data-analysis systems and physical laboratories.   Adam was the first machine to make novel scientific discoveries throug...
  </details>


### 📂 other
*其他安全相关 / Other Security-Related* — 168 papers

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

- **2026-08-14** — Alexei Odinokov, Rostislav Yavorskiy — [Ensuring Safe Physical AI in Urban Mobility via Hazard-Informed Synthesized Envelopes](http://arxiv.org/abs/2608.14481v1)
  <details><summary>📄 Abstract</summary>
  As heterogeneous robotic systems deploy across diverse urban zones, maintaining safety amid complex human-robot interactions remains a critical challenge. We present a unified framework that bridges systematic hazard analysis and runtime enforcement using hazard-informed safety envelopes. Rather than treating safety as a static constraint isolated within individual software modules, we introduce a cross-layer safety transformation process spanning symbolic, spatial, and dynamic world models. We ...
  </details>

- **2026-08-14** — Jihun Park, Kyoungmin Lee, Jongmin Gim et al. — [CRAFT: Constrained Reward via Attention Fine-Tuning for Subject Personalization without Composed Targets](http://arxiv.org/abs/2608.14403v1)
  <details><summary>📄 Abstract</summary>
  Subject-driven image personalization---generating new images that preserve the identity of one or several reference subjects in novel scenes---is a foundational capability for modern visual content creation. It is currently dominated by generalized methods that fine-tune a pretrained multimodal diffusion transformer (MMDiT) on hundreds of thousands to millions of paired \emph{(reference, composed-target)} examples, where each composed target is a synthesized image of the subject in a novel scene...
  </details>

- **2026-08-14** — Yu Zhuang, Kefei Chen, Yitong Duan et al. — [AgentRewind: Recoverable Execution for Long-Horizon LLM Agents](http://arxiv.org/abs/2608.14380v1)
  <details><summary>📄 Abstract</summary>
  Many real-world tasks require LLM agents to interact with their environments over long execution horizons. Errors that occur early in execution may propagate through both the agent context and environment state, and their effects may be difficult to reverse through subsequent actions. Existing methods mainly seek to reduce such errors through plan refinement and safety checks but provide little support after errors occur. To enable recovery during long-horizon execution, we present AgentRewind, ...
  </details>

- **2026-08-14** — Shiju Zhao, Jiacheng Yang, Qihang Chen et al. — [CoRun: Padding is Simple and Efficient for Deterministic LLM Inference](http://arxiv.org/abs/2608.14376v1)
  <details><summary>📄 Abstract</summary>
  Despite fixed sampling parameters and random seeds, Large Language Model (LLM) inference exhibits output inconsistency, which undermines downstream tasks such as model evaluation and reinforcement learning. A major source of this nondeterminism is batch-dependent GPU execution: dynamic input shapes change kernel tiling and floating-point reduction orders. Existing systems address this problem with batch-invariant kernels, but these kernels restrict optimized tiling and split reductions, increasi...
  </details>

- **2026-08-14** — Wei Wei, Foroozan Daneshzand, Zezhong Wang et al. — [Epistemic Tensions: Reframing A Visualization Co-Design through Entanglement Theory](http://arxiv.org/abs/2608.14364v1)
  <details><summary>📄 Abstract</summary>
  In this work, we present how employing the lens of entanglement helped us examine and reframe epistemic tensions arising in a visualization co-design project. Entanglement theory challenges traditional assumptions in the visualization research community by emphasizing that knowledge is not produced through linear, isolated processes, but is inherently entangled with phenomena and apparatuses. While this perspective offers a compelling critique of conventional research practices, its practical va...
  </details>

- **2026-08-14** — Mingming Zhao, Jiqian Dong, Kangping Xu et al. — [ScienceFlow: A long-horizon agent for ML research, scientific discovery and beyond](http://arxiv.org/abs/2608.14354v1)
  <details><summary>📄 Abstract</summary>
  Enabling LLM agents to sustain productive, stable, and goal-aligned research over extended horizons is a central challenge for autonomous machine learning and scientific discovery, as progress hinges on continuously managing evolving state, exploration decisions, and computational resources. Pioneering autoresearch agents, despite great success, still lack mechanisms for continuity, recovery from dead ends, and value-driven compute allocation, which inherently undermines overall search efficienc...
  </details>

- **2026-08-14** — Uwe M. Borghoff, Paolo Bottoni, Remo Pareschi — [Sensor-Driven Mission Synthesis for UAV/UGV Swarms: A TB-CSPN Coordination Architecture with Hardware-Enforced Safety](http://arxiv.org/abs/2608.14306v1)
  <details><summary>📄 Abstract</summary>
  This paper presents a coordination architecture for heterogeneous UAV/UGV swarms that synthesises mission actions from uncertain, multi-modal sensor evidence while preserving hardware-enforced safety at the actuation boundary. The approach combines radar, RF, acoustic, and visual observations with Topic-Based Communication Space Petri Net (TB-CSPN) orchestration to support incremental mission formation under partial and evolving information. Consultant agents transform sensor outputs into tempor...
  </details>

- **2026-08-14** — Brett Reynolds — [Grounding Without Corrective Control: Truth-Tracking Profiles for Large Language Models](http://arxiv.org/abs/2608.14252v1)
  <details><summary>📄 Abstract</summary>
  Recent work suggests that some large language model representations have content or reference. Grounding can secure either without supplying live routes for correction. This paper asks what follows from that gap. An output is answerable when discrepancies can affect what a target- and task-specific arrangement produces, accepts, or withdraws. The arrangement has corrective control only when live, sufficiently independent routes can detect and repair fresh discrepancies. A route profile records w...
  </details>

- **2026-08-14** — Varuni H K, Soham Sarkar, Jay Kumar et al. — [Polaris : Multi Agentic System for Conversational Enterprise Analytics](http://arxiv.org/abs/2608.14246v1)
  <details><summary>📄 Abstract</summary>
  In today's fast-paced environment, the ability to swiftly access, understand, and act on data is no longer optional; it is essential. Yet most organizations remain data-rich but insight-poor, constrained by the complexity of querying, interpreting, and explaining enterprise-scale information. We present Polaris, a supervisor-led multi-agent framework for conversational enterprise analytics that bridges this gap. Polaris introduces Dynamic Task Coordination (DTC), a decision-theoretic orchestrati...
  </details>

- **2026-08-14** — Wenhao Tang, Tianyang Chen, Zhejun Cui et al. — [AgilePE: Autonomous UAV Pursuit-Evasion via Self-Play Reinforcement Learning](http://arxiv.org/abs/2608.14135v1)
  <details><summary>📄 Abstract</summary>
  Autonomous pursuit-evasion is a fundamental challenge for Unmanned Aerial Vehicles (UAVs), requiring rapid decision-making under tightly coupled dynamics and continuously changing opponent behaviors. Traditional rule-based or differential-game approaches often struggle with high-dimensional aerial interactions and agile maneuvering. We present AgilePE, a complete system for autonomous UAV pursuit-evasion via self-play reinforcement learning. AgilePE integrates agile low-level control, competitiv...
  </details>

- **2026-08-14** — Kaipeng Zeng, Wenxi Zhai, Shengrui Xu et al. — [Reaction-Transformation-Aware Flow Matching for Generalizable Transition State Generation](http://arxiv.org/abs/2608.14076v1)
  <details><summary>📄 Abstract</summary>
  Transition-state (TS) structures define the energetic barriers and mechanistic pathways of elementary chemical reactions, yet their identification remains computationally demanding because conventional saddle-point searches require expensive quantum-mechanical calculations. Recent machine-learning approaches have accelerated TS generation by predicting structures from reaction endpoint information, but they primarily learn geometric correspondence between endpoints and TSs, leaving the structura...
  </details>

- **2026-08-14** — Dingbao Shao, Song Wu, Xinyu Chen et al. — [InstructVVT: Instruction-Driven Video Virtual Try-On without Auxiliary Spatial Priors](http://arxiv.org/abs/2608.14070v1)
  <details><summary>📄 Abstract</summary>
  Video virtual try-on is a highly constrained editing task requiring the precise replacement of a target person's clothing while strictly preserving the original video's spatial structure and temporal dynamics. Existing methods heavily rely on auxiliary handcrafted spatial priors (e.g., masks, poses) for editing control. However, these priors are prone to failure in unconstrained real-world videos and often compress rich visual context into incomplete structural signals. Furthermore, standard rec...
  </details>

- **2026-08-14** — Xinye Li, Lingshuai Lin, Lei Wang et al. — [ForgeWM: Progressive Causal Training for Few-Step Action-Conditioned Video World Models](http://arxiv.org/abs/2608.14022v1)
  <details><summary>📄 Abstract</summary>
  Action-conditioned video world models require low-latency causal generation and reliable responses to game-native controls. Although causal distillation enables one- or few-step video synthesis, extending it to interactive world models remains challenging, as discrete keyboard states and continuous mouse motion must remain aligned with temporally compressed latent chunks during causal training and autoregressive rollout. We introduce ForgeWM, a progressive framework that transforms a bidirection...
  </details>

- **2026-08-14** — Jin Xu, Yu-Ping Chen, Ayanna Howard — [THRIVE: Therapeutic Humanoid Robot In Virtual Environment](http://arxiv.org/abs/2608.14462v1)
  <details><summary>📄 Abstract</summary>
  This paper presents THRIVE (Therapeutic Humanoid Robot In Virtual Environment), an at-home rehabilitation platform that integrates a suite of virtual-reality upper-body rehabilitation games, a real-time camera-based motion-tracking system, and a socially interactive robot therapist. The system is designed for therapy and intervention in children with upper-limb motor impairments, which can be improved through consistent, task-specific practice. THRIVE features a set of newly designed, engaging g...
  </details>

- **2026-08-14** — Chih-Hsuan Yang, Anjir Ahmed Chowdhury, Cheng-Hau Yang et al. — [Wrong but Useful: Trajectory Value Beyond Answer Correctness in Multi-Agent Messages](http://arxiv.org/abs/2608.14375v1)
  <details><summary>📄 Abstract</summary>
  Multi-agent reasoning systems often use agreement, confidence, or automated scores to decide which messages should shape a final answer. Such filtering assumes that a message likely to be correct is also worth keeping. Yet a wrong answer can contain a useful decomposition, constraint, or scientific principle. We test this distinction with Diverse Hypothesis Deliberation (DHD), a controlled measurement protocol that caches five independently generated messages and replays the same downstream solv...
  </details>

- **2026-08-14** — Marco Roth — [Classical Limits of Spectral Filtering in Quantum Generative Models](http://arxiv.org/abs/2608.14169v1)
  <details><summary>📄 Abstract</summary>
  Spectral filtering has been proposed as a route to regularization in quantum generative models: the quantum Fourier transform exposes the amplitude spectrum of a quantum circuit Born machine, and a diagonal filter suppresses the high frequencies associated with finite-sample noise, an operation whose classical counterpart seemingly requires manipulating an exponentially long amplitude vector. We examine whether this coherent operation produces anything that classical post-processing of samples f...
  </details>

- **2026-08-14** — Xingyu Zhu, Wenshuo Han, Zhouyu Wang et al. — [FlatLab: A Unified Methodology Framework and Simulation-Based Benchmark for Robotic Manipulation of Flat Objects](http://arxiv.org/abs/2608.14049v1)
  <details><summary>📄 Abstract</summary>
  Robotic manipulation of flat objects is challenging due to the ungraspable configurations and strong variations in object geometry and material. Existing methods rely on heuristic pre-manipulation and are often evaluated in closed settings with limited generalization. We propose a unified framework that decouples the manipulation into a strategy generator and an action execution module. The strategy generator predicts appropriate manipulation strategies from object point clouds by learning strat...
  </details>

- **2026-08-14** — Haohui Yang, Jiaxing Sun, Xiujun Ma — [More Correct Mass, Worse Answers: Why Power Sampling Can Fail and How to Fix It](http://arxiv.org/abs/2608.14420v1)
  <details><summary>📄 Abstract</summary>
  Power Sampling sharpens a language model's distribution over complete generation trajectories, offering a verifier-free way to improve reasoning at inference time. It also has the potential to serve as a general-purpose front end for a broad range of downstream sampling methods. However, we uncover a striking paradox: Power Sampling can drive more probability mass toward correct trajectories while degrading the downstream inference it is intended to enhance. Using self-consistency as a represent...
  </details>

- **2026-08-14** — Paras Balani, Subhrakanta Panda — [LLMs Don't Pay for the Jump](http://arxiv.org/abs/2608.14397v1)
  <details><summary>📄 Abstract</summary>
  Zahavy [2026] argues that Large Language Models, despite their capabilities in induction and deduction, cannot perform the abductive "Jump" that produced Einstein's equivalence principle, and attributes this limitation to the absence of embodied simulation. Zheng-Xin [2026] and Farmer [2026] question whether embodiment is necessary for abduction, pointing to alternative routes to General Relativity and forms of abduction that require no sensorimotor grounding. Max Planck resolved the blackbody r...
  </details>

- **2026-08-14** — Marek Arsenault, Hlér Kristjánsson — [Linearised quantum signal processing](http://arxiv.org/abs/2608.14387v1)
  <details><summary>📄 Abstract</summary>
  Quantum functional programming has been developed through two distinct paradigms in the last few years: Quantum Signal Processing (QSP)-based methods, including the Quantum Singular Value Transformation (QSVT), and methods based on higher-order quantum transformations, such as the Universal Hamiltonian Eigenvalue Transformation (UHET). While UHET performs functional transformations of Hamiltonian dynamics, its relationship to QSP-based techniques has remained unclear despite evident structural s...
  </details>

- **2026-08-14** — Arwa Osman, Marco Baroni, Iuri Macocco — [Local and Global Regimes of Geometric Complexity in Language Model Representations](http://arxiv.org/abs/2608.14361v1)
  <details><summary>📄 Abstract</summary>
  Intrinsic dimensionality (ID) is widely used to probe the representational complexity of language models, but it remains unclear whether ID differences reflect properties of language itself or artefacts of how the underlying dataset was constructed. In this paper, we focus specifically on how lexical diversity, the number of unique last-token items present in a dataset, affects ID estimates of that dataset. We find a scale-dependent transition between two regimes: at low lexical diversity, condi...
  </details>

- **2026-08-14** — Zhizhao Guan, Chen Huang, Ziming Liu et al. — [Clearing the Fog: Towards Installing and Refining Proactive Exploration Capabilities in LLM Agents](http://arxiv.org/abs/2608.14339v1)
  <details><summary>📄 Abstract</summary>
  We study proactive exploration in LLM agents, i.e., the ability to explore an environment to acquire information that improves future decision-making. In this regard, we first identify two fundamental bottlenecks that hinder this capability and then propose \ours, a novel method designed to instill and refine proactive exploration. Specifically, \ours\ consists of two components: (1) Exploratory Data Construction, which synthesizes exploration-rich trajectories to mitigate the hindsight bias of ...
  </details>

- **2026-08-14** — Jing-Cheng Yang, Hao-Jung Wang, Jinhao Du et al. — [Spatial Message Passing in Language Space for Pathology Image Interpretation](http://arxiv.org/abs/2608.14309v1)
  <details><summary>📄 Abstract</summary>
  Multimodal Large Language Models (MLLMs) can generate pathological descriptions from histological images, but gigapixel Whole Slide Images (WSIs) exceed their visual context limits. The standard tiling workaround makes WSIs tractable yet severs the tissue neighborhoods that define tumor-stroma interfaces and morphology. We introduce Spatial Language Message Passing (SLMP), a framework that performs spatial reasoning entirely in language space, human-readable by construction. SLMP represents a WS...
  </details>

- **2026-08-14** — Kohsuke Ide, Ryousuke Yamada, Yoshihiro Fukuhara et al. — [Seeing Red, Thinking Bad: Color Bias in Vision Language Models](http://arxiv.org/abs/2608.14286v1)
  <details><summary>📄 Abstract</summary>
  Vision language models (VLMs) are increasingly used in industrial decision-making systems, such as recruitment support and recommendation. This motivates careful analysis of how VLMs process visual and textual information. In this work, we study how VLMs interpret text rendered as an image, and investigate the influence of visual styling biases. To this end, we introduce Stealth Visual Prompts, which subtly change visual styling of text, such as color and contrast, while preserving semantic cont...
  </details>

- **2026-08-14** — Dongjun Wei, Hongyi Wu, Yinuo Zou — [Attributing Preprocessing Invariance in Spectral Foundation Models](http://arxiv.org/abs/2608.14227v1)
  <details><summary>📄 Abstract</summary>
  Preprocessing invariance is an appealing goal for spectral foundation models: a frozen model should remain useful when laboratories preprocess spectra differently. It is usually measured by training a classifier under one preprocessing pipeline and testing it under another, with preserved accuracy read as evidence of learning. We revisit that reading, using a Raman foundation model as a case study. Such models normalize their inputs before any learned parameter is applied. If that normalization ...
  </details>

- **2026-08-14** — Patrik Kenfack, Jesse C. Cresswell, Anthony L. Caterini et al. — [Training Fair Tabular Foundation Models](http://arxiv.org/abs/2608.14211v1)
  <details><summary>📄 Abstract</summary>
  Tabular Foundation Models (TFMs) have emerged as leading methods for tabular predictive tasks, leveraging in-context learning to predict on new data without task-specific training. Despite the increased use of TFMs in high-stakes decision-making, their fairness properties remain largely unexplored. In this work, we incorporate fairness constraints directly into TFM training, enabling fair predictions in a single forward pass. Our approach addresses two key challenges: limited access to sensitive...
  </details>

- **2026-08-14** — Vassilios M Rothos — [Spectral stability and slow--fast structure of traveling waves in a regularized sine--Gordon equation](http://arxiv.org/abs/2608.14108v1)
  <details><summary>📄 Abstract</summary>
  We investigate the dynamics and spectral stability of traveling kink and antikink solutions in a dissipative sine--Gordon equation with two distinct fourth--order regularization mechanisms: a mixed space--time (inertial) term and a purely spatial (elliptic) term. The model includes damping, bias forcing, and higher--order dissipative effects, and is motivated by refined descriptions of fluxon dynamics in long Josephson junctions. Using a collective--coordinate reduction, we derive a Melnikov--ty...
  </details>

- **2026-08-14** — Zihong He, Chen Liang, Hai-Ning Liang — [AppLooper: An Agentic Application Engineering Loop for Accountable Release with Virtual-User Feedback](http://arxiv.org/abs/2608.14093v1)
  <details><summary>📄 Abstract</summary>
  Much existing research on coding agents organizes application development as an iterative loop of requirement interpretation, implementation, tool execution, evaluation, and repair. As these loops run longer, requirements may drift; users may lose awareness of the current state and rationale for changes; and generated applications may remain insufficiently grounded in target users' contexts and needs. Application engineering therefore requires a mechanism connecting owner intent, target-user exp...
  </details>

- **2026-08-14** — Giovanni Racioppi — [Mandato: Protocol-Level Enforcement of Digitally Signed Mandates on AI Agent Actions with Cryptographically Chained Audit Trails](http://arxiv.org/abs/2608.14074v1)
  <details><summary>📄 Abstract</summary>
  AI agents increasingly act on external systems through standardized tool-calling protocols such as the Model Context Protocol (MCP), yet no infrastructure layer constrains their actions to what a principal has verifiably authorized: authorization logic lives in application code, is neither signed nor independently auditable, and the resulting logs lack evidentiary value. We present Mandato, a governance proxy that enforces digitally signed mandates on agent actions at the protocol level. A manda...
  </details>

- **2026-08-14** — Ziqi Song, Zongyuan Xiang, James G. Ogg et al. — [HERMES: a multi-agent framework for structured knowledge extraction from ultra-long documents in geoscience](http://arxiv.org/abs/2608.14055v1)
  <details><summary>📄 Abstract</summary>
  Authoritative scientific knowledge in geoscience remains largely trapped in legacy monographs and historical literature, where unstructured text and complex layouts hinder computational access. We introduce HERMES, a scalable multi-agent framework that extracts structured data from ultra-long scientific documents. Using a coordinating large language model, HERMES integrates domain constraints, validation rules and evidence tracing within a unified document-level extraction process that incorpora...
  </details>

- **2026-08-14** — Keito Kozaki, Keigo Sakurai, Ren Togo et al. — [Residual Dominance as a Structural Account of Last-Item Reliance in Causal Self-Attention Recommenders](http://arxiv.org/abs/2608.14021v1)
  <details><summary>📄 Abstract</summary>
  Transformer-based sequential recommenders with causal self-attention often rely heavily on the most recent interaction at inference time, but how this behavior is structurally expressed in the representation used for prediction remains unclear. We combine prediction-time diagnostics with norm-based analysis of the full attention block. First, we show that SASRec-style models exhibit highly localized last-item reliance. We then find that, although self-attention aggregates contextual information,...
  </details>

- **2026-08-14** — Alireza Kargarzadeh, Nariman Khaledian, Navid Parvini et al. — [Buy the Rumor, Sell the News: When Is News Priced In?](http://arxiv.org/abs/2608.14014v1)
  <details><summary>📄 Abstract</summary>
  Two old market sayings hold that news is already priced in by the time it is published, and that the rumor is bought while the news is sold. Both place the price move associated with a piece of news before and at publication rather than after it. Whether the claims hold, for which kinds of news, and by how much are basic questions about how fast markets absorb public information. We test them on 4.57 million financial news articles covering roughly 3,000 US stocks (2023-2026). A large language m...
  </details>

- **2026-08-13** — Dingzhan Nong, Zhihao Ren, Ziqi Li et al. — [Sign Language Video Synthesis via Loss-Guided Multi-Expert GANs](http://arxiv.org/abs/2608.13368v1)
  <details><summary>📄 Abstract</summary>
  This preliminary technical report presents a framework for sign language video synthesis using a loss-guided multi-expert Generative Adversarial Network (GAN) to enhance communication for individuals with hearing impairments. Three specialized discriminators -- global, hand, and head -- each guide a corresponding expert branch in the generator toward a distinct visual region, enabling implicit feature specialization without explicit diversity losses. To stabilize this multi-discriminator system,...
  </details>

- **2026-08-13** — Shunwen Bai, Ziping Ma, Chaoyang Zhang et al. — [TsuGO: Probing Search Efficiency in LLM Reasoning via Go Life-and-Death Problems](http://arxiv.org/abs/2608.13221v1)
  <details><summary>📄 Abstract</summary>
  The evaluation of LLM reasoning is moving from final-answer accuracy to process-level assessment, yet existing methods still fail to capture how models plan reasoning paths and allocate reasoning resources--that is, how they organize search. Prior process-level methods focus on the coherence and redundancy of chain-of-thought (CoT), and most benchmark tasks have a single objective solvable by static capabilities such as derivation and tool use, leaving search organization unmeasured. We introduc...
  </details>

- **2026-08-13** — Yaxin Luo, Haobin Jiang, Jialv Zou et al. — [AutoDesign: Meta-Harness Optimization for Long-Horizon Agentic Design](http://arxiv.org/abs/2608.13560v1)
  <details><summary>📄 Abstract</summary>
  Transforming multimodal sources into condensed and structured media outputs can be fundamentally conceptualized as a long-horizon agentic process centered on a model-harness system. While an ideal harness system should align with human design priors and accumulate reusable experience through empirical exploration to drive recursive self-improvement, existing paradigms remain static and fall short of this capability. In this paper, we present AutoDesign, a framework that aligns with human design ...
  </details>

- **2026-08-13** — Shouzhi Fang, William C. Tegge, Md Omar Faruque et al. — [YAVIN: A Unified Architecture for Secure Edge Processing in Memory](http://arxiv.org/abs/2608.13496v1)
  <details><summary>📄 Abstract</summary>
  Secure, private multi-tenant execution spanning processors, memory, and accelerators remains one of the most significant challenges in modern edge computing systems. Simultaneously, processing-in-memory (PIM) has emerged as an effective approach for reducing the Von Neumann bottleneck by moving computation closer to data. Existing trusted execution environments (TEEs) establish trust only within the processor, protecting data while it traverses untrusted resources such as the memory bus. Consequ...
  </details>

- **2026-08-13** — Yi-Chung Chen, Philip Jacobson, Tom Lampo et al. — [TraVEL: Trajectory-Guided Video Embedding Learning for Driving-Video Retrieval](http://arxiv.org/abs/2608.13495v1)
  <details><summary>📄 Abstract</summary>
  Efficiently retrieving relevant clips from large-scale driving logs is essential for data curation, model development, and safety analysis. Structured and rule-based retrieval systems can explicitly target driving events, but typically require expert-defined rules, auxiliary data, and multi-stage perception pipelines. Multimodal embedding models offer a simpler and more efficient alternative by representing each video with a single searchable vector. However, general-purpose models often rely on...
  </details>

- **2026-08-13** — Zuzanna A. Wakefield-Skórniewska, Bartłomiej W. Papież — [Evaluation of Clinically Steerable Retinal Image Generation from Foundation Model Latent Spaces](http://arxiv.org/abs/2608.13455v1)
  <details><summary>📄 Abstract</summary>
  Medical foundation models learn latent representations of clinically meaningful phenotypes, yet their ability to support controllable image generation remains largely unexplored. We evaluate four retinal foundation models within the representation tokenizer framework and examine whether demographic and clinical information encoded in latent representations from foundation models is preserved during synthetic image generation. We show that generated representations and images faithfully inherit p...
  </details>

- **2026-08-13** — Zongyun Zhang, Jiacheng Ruan, Xian Gao et al. — [Edit2TikZ: A Comprehensive and Challenging Benchmark for Scientific Figure Editing with TikZ](http://arxiv.org/abs/2608.13441v1)
  <details><summary>📄 Abstract</summary>
  Although multimodal large language models (MLLMs) have shown substantial potential in visual understanding and graphic code generation, editing scientific figures through code presents a greater challenge: a model must jointly recover visual structure, ground the requested change, generate compilable code, and preserve all unrelated content. While existing TikZ benchmarks mainly focus on figure reconstruction and generation, few systematically evaluate instruction-guided scientific figure editin...
  </details>

- **2026-08-13** — Yupan Ding, Jing Xiao, Zhenyuan Zhang et al. — [LongEarth-R1: Benchmarking and Aligning Vision-Language Models for Long-Horizon Earth Observation Reasoning](http://arxiv.org/abs/2608.13344v1)
  <details><summary>📄 Abstract</summary>
  Long-horizon Earth observation reasoning requires models to organize multi-stage geographic evolution, localize spatial changes, detect temporal anomalies, and infer future from extended image sequences. However, existing remote sensing vision-language models mainly focus on isolated images, image pairs, or short sequences, limiting reliable grounding in the relevant frames and regions. We introduce LongEarth-Bench, a benchmark containing approximately 120k question-answering samples derived fro...
  </details>

- **2026-08-13** — Jingbo Ji, Lingyi Li, Xilong Cheng et al. — [RippleMem: From Isolated Retrieval to Associative Recollection for Long-Term Agent Memory](http://arxiv.org/abs/2608.13334v1)
  <details><summary>📄 Abstract</summary>
  LLM-based agents increasingly rely on external memory to support long-horizon reasoning and interaction. However, the main bottleneck is not simply storing past experience, but recovering the right set of evidence when relevant information is distributed across many interactions. Existing approaches struggle with this access problem. Full-context methods require noisy long-context search, flat retrieval often returns isolated and incomplete records, and graph-based memory systems can be expensiv...
  </details>

- **2026-08-13** — Mohammed Sabry, Sean Augenstein, Keith Rush et al. — [Mixture of Training: Recombining Small-Scale Scaffolded Pretraining Runs into a Larger Language Model](http://arxiv.org/abs/2608.13277v1)
  <details><summary>📄 Abstract</summary>
  We ask whether language-model pre-training can be decomposed into smaller, independently trainable jobs that can later be recomposed into a coherent larger model. We introduce Mixture of Training (MoT), a scaffolded modular pre-training procedure that partitions a target Transformer into contiguous layer blocks, trains each block inside a frozen pretrained aligner scaffold, and then recomposes the trained blocks with an optional short end-to-end adaptation pass. On a 1.3B-parameter Gemma-style m...
  </details>

- **2026-08-13** — Yuheng Huang, Jianlang Chen, Jiayang Song et al. — [NARU: A Benchmark for NARrative Evolution and Cultural Nuance Understanding in Japanese Extreme Long Video](http://arxiv.org/abs/2608.13210v1)
  <details><summary>📄 Abstract</summary>
  Long-form video understanding encompasses tasks that go beyond retrieving isolated events, including tracking an evolving narrative and interpreting social meaning that may remain implicit. However, existing benchmarks rarely evaluate these capabilities jointly, particularly in high-context, non-English media. To address this gap, we introduce NARU, a benchmark designed to evaluate Narrative evolution and Reasoning on cultural Understanding in Japanese long-form video. NARU consists of 1,481 que...
  </details>

- **2026-08-13** — Shuzhe Zhang, Xin Zhu, Yinling Qian et al. — [S2-HWM: Sparse Event-Structured Hierarchical World Model for Long-Horizon Surgical Robot Manipulation](http://arxiv.org/abs/2608.13103v1)
  <details><summary>📄 Abstract</summary>
  Long-horizon surgical robot manipulation is challenging because task rewards are sparse, while meaningful interaction changes occur at irregular intervals. Existing world-model agents typically imagine at primitive-step resolution, leaving variable-duration task progress implicit. Manually specified stages can provide intermediate structure, but their task specific boundaries are difficult to align with state-dependent interaction transitions. We propose S2-HWM, a Sparse Event-Structured Hierarc...
  </details>

- **2026-08-13** — Jiqi Li, Jingyi Mei, Wang Fang et al. — [Formal Verification of Quantum Ancilla Safety](http://arxiv.org/abs/2608.13099v1)
  <details><summary>📄 Abstract</summary>
  Ensuring ancilla safety is a critical correctness requirement for quantum compilation, since ancilla qubits are routinely introduced to implement complex operations with fewer gates and reduced depth. However, formally verifying this property is computationally hard due to state-space explosion in the number of qubits, particularly for dirty ancillae, which carry unknown initial states and must be restored after use. We propose an end-to-end verification-and-repair framework that rigorously addr...
  </details>

- **2026-08-13** — Fanpeng Yang, Xing Li, Shuling Wang et al. — [How Powerful are LLMs in Generating Formal Program Specifications?](http://arxiv.org/abs/2608.13077v1)
  <details><summary>📄 Abstract</summary>
  Formal verification provides strong guarantees of software correctness, but its adoption is limited by the high cost of writing precise formal specifications. While recent large language models (LLMs) have shown strong capabilities in theorem proving and verified code generation, their true ability to generate program specifications remains unclear. Existing evaluations require either verifying implementation conformance or proving semantic equivalence between specifications, both of which are f...
  </details>

- **2026-08-13** — Johan Henriksson — [Static analysis-guided agentic AI translation enables Rust as a full stack bioinformatics language](http://arxiv.org/abs/2608.13029v1)
  <details><summary>📄 Abstract</summary>
  The field of bioinformatics struggles with legacy code - old code that is commonly used but may no longer have a maintainer, or may be written in an now-unfamiliar language (e.g. Perl, Fortran). This incurs maintenance cost (technical debt), but dynamically typed languages also negatively impacts the environment and fail to make use of modern hardware. Legacy code may also have security or safety problems that make it unsuited for use in clinical settings. Here we show that agentic AI, combined ...
  </details>

- **2026-08-13** — Yunhao Bai, Zhongwei Qiu, Guangyu Guo et al. — [HounsWorld: A Multimodal World Model for Hidden Patient-State Readout, Reconstruction, and Simulation](http://arxiv.org/abs/2608.12904v1)
  <details><summary>📄 Abstract</summary>
  Clinical intelligence requires estimating a patient's underlying condition from incomplete observations rather than learning isolated mappings from scans to answers. Volumetric medical images provide dense observations of anatomy, attenuation, and lesions, whereas clinical language provides sparse but complementary semantic observations. We formulate CT-centered intelligence as inference over a shared latent patient state, under which readout, reconstruction, and simulation all become state-depe...
  </details>

- **2026-08-13** — Xutao Mao, Liangjie Zhao, Xiang Zheng et al. — [Practice Makes Unsafe: Skill Misevolution in Self-Improving LLM Agents](http://arxiv.org/abs/2608.12851v1)
  <details><summary>📄 Abstract</summary>
  Self-improving LLM agents convert successful trajectories into persistent cross-task state. An unsafe success can thereby become reusable policy after its triggering input disappears. Skill evolution makes this failure measurable by distilling operational trajectories into executable, transferable, and inspectable procedures. Because evolution optimizes task outcomes rather than procedure safety, compromised experience can cause skill misevolution. Existing benchmarks measure current behavior or...
  </details>

- **2026-08-13** — Prateek Kumar Rajput, Abdoul Aziz Bonkoungou, Alberick Euraste Djiré et al. — [Memorization Diagnostics for Code LLMs Should be Scale-Aware](http://arxiv.org/abs/2608.12771v1)
  <details><summary>📄 Abstract</summary>
  The extent to which large language models for code rely on memorization over genuine understanding remains highly debated. While current literature frequently reports widespread memorization, evaluating the underlying probing techniques across dense architectures reveals a severe breakdown in their utility at scale. Traditional encoder-style probes using perturbations such as synonym fuzzing or dead-code insertion struggle to expose memorization in scaled models, even on known-contaminated bench...
  </details>

- **2026-08-13** — LingKai Bu — [Dual-Stream Cross-Anchor Correction Grounding Long-Form Captions and the Domain Limits of Object-Level Anchors](http://arxiv.org/abs/2608.12746v1)
  <details><summary>📄 Abstract</summary>
  Object hallucination in multimodal large language models arises when language priors and corpus co-occurrence bias outweigh the visual evidence, with nothing tying an individual object mention to what the image shows. Most remedies intervene at decoding time without training, yet under a unified protocol their benefit is confined to short captions;supervised fine-tuning (SFT) on a detail- rich corpus lengthens captions, but over forty percent still name absent objects. This paper proposes Dual-S...
  </details>

- **2026-08-13** — João Henrique Andrade, Tao Feng, Paolo Piccione et al. — [Delaunay solutions to the fractional Hartree equation with critical growth](http://arxiv.org/abs/2608.12734v1)
  <details><summary>📄 Abstract</summary>
  We study positive solutions of the critical fractional Hartree equation with a non-removable isolated singularity at the origin. This equation is doubly nonlocal, involving both the fractional Laplacian and a Riesz convolution potential. We first prove that every positive singular solution is radially symmetric about the origin, by combining the Caffarelli--Silvestre extension with the method of moving spheres. We then establish the existence of Delaunay-type periodic singular solutions. After t...
  </details>

- **2026-08-13** — Ping Li — [Topological obstructions to geometric positivity and negativity on Calabi-Yau manifolds](http://arxiv.org/abs/2608.12705v1)
  <details><summary>📄 Abstract</summary>
  We study whether the topology underlying a Calabi-Yau manifold can support natural geometric positivity or negativity structures. In even complex dimension $n \geq 4$ (assuming $b_2=1$ when $n \geq 6$), we strengthen a theorem of Oguiso-Peternell by proving that a Calabi-Yau manifold is not homeomorphic to a weak Fano $n$-fold. The same obstruction applies to Kähler manifolds with quasi-positive holomorphic sectional curvature. A transformation-group analogue excludes, in particular, symplectic ...
  </details>

- **2026-08-13** — Fin Amin, Sounak Dutta, Paul D. Franzon — [Finding the Needle in a Haystack: Test-Time Analog Circuit Representation Adaptation for Bayesian Optimization](http://arxiv.org/abs/2608.12687v1)
  <details><summary>📄 Abstract</summary>
  Bayesian optimization (BO) is a sample-efficient framework for analog circuit topology search, where evaluating each candidate topology can require costly simulation. However, representation-based BO methods typically treat circuit embeddings as fixed after encoder training. This creates a mismatch between representation learning and optimization: embeddings learned to encode or reconstruct circuit structure are not necessarily organized according to the figure of merit (FoM) being optimized. Th...
  </details>

- **2026-08-13** —  DreamX Team, Rui Chen, Xiangxiang Chu et al. — [DreamX-Phi 1.0: Action-Conditioned Video World Model for Robotic Manipulation](http://arxiv.org/abs/2608.13489v1)
  <details><summary>📄 Abstract</summary>
  We present \textbf{DreamX-Phi 1.0}, an action-conditioned video world model for robotic manipulation that, given an observed frame, a language instruction, and a prescribed action sequence comprising end-effector poses and gripper states, predicts the resulting future observations. Yet realism alone does not guarantee faithfulness: a convincing rollout can still move the wrong arm or lose the manipulated object. To ensure the prediction respects each arm's commanded path, we inject per-arm $\mat...
  </details>

- **2026-08-13** — Dingyi Rong, Yue Shi, Chaofan Ma et al. — [H2R-Bench: Benchmarking Human-to-Robot Manipulation Video Generation in World Models](http://arxiv.org/abs/2608.13049v1)
  <details><summary>📄 Abstract</summary>
  Large-scale manipulation data is essential for robot learning, yet collecting robot demonstrations remains expensive and difficult to scale. Meanwhile, abundant egocentric human manipulation videos provide rich behavioral experiences, but transferring them across embodiments remains challenging due to differences between human hands and robotic end-effectors. Recent advances in video world models offer a promising pathway to synthesize robot-centric manipulation videos from human observations, w...
  </details>

- **2026-08-13** — Geng Wang, Junyu Yang, Timan Lei et al. — [Controlling the dynamics of an electric-field-driven droplet on a lubricant-infused micropillar surface](http://arxiv.org/abs/2608.12868v1)
  <details><summary>📄 Abstract</summary>
  As a non-contact control approach, electric field (EF) can be utilised to drive droplet dynamics on a lubricant-infused surface (LIS), with numerous potential applications ranging from drug manufacturing to 3D printing. However, the resulting droplet dynamics remain poorly understood, especially as there are several possible droplet lubrication states on LIS. Here, we develop a lattice Boltzmann scheme that fully captures the interplay between the interfacial flows and electrohydrodynamics and h...
  </details>

- **2026-08-13** — Weihan Meng, Hongzhu Guo, Yi Jing et al. — [SAEVerbalizer: Generating Explanations for Sparse Autoencoder Features via Representation Verbalization](http://arxiv.org/abs/2608.13538v1)
  <details><summary>📄 Abstract</summary>
  Sparse autoencoders (SAEs) are proposed to extract numerous features from large language model (LLM) representations, yet explaining these features still relies primarily on external observation. This reliance leads to superficial explanations inferred from observed model behavior and computational inefficiency from collecting such behavioral evidence at scale. We introduce SAEVerbalizer, a framework that injects SAE decoder directions into an LLM's representations and fine-tunes the LLM's downs...
  </details>

- **2026-08-13** — David Chushig-Muzo, María Ángeles Rodríguez de Cara, Eva Milara et al. — [TabSOM: A tabular-to-image encoding method based on self-organizing maps](http://arxiv.org/abs/2608.13513v1)
  <details><summary>📄 Abstract</summary>
  Tabular-to-image methods have emerged as novel approaches to leverage the high predictive performance of convolutional neural networks and vision transformers. They convert tabular data into image representations, mapping each feature at a fixed pixel location derived from a dimensionality-reduction method (e.g., t-SNE, UMAP, PCA). However, they encode only the marginal value of each feature and discard information about feature relationships. We propose TabSOM, a tabular-to-image encoding built...
  </details>

- **2026-08-13** — Avinash Kori, Fabrizio Russo — [A Unifying Perspective on Causal World Models: From Observations to Representations to Structure](http://arxiv.org/abs/2608.13456v1)
  <details><summary>📄 Abstract</summary>
  World Models (WM) are increasingly seen as a foundation for intelligent agents that can predict, plan, and act beyond their training distribution. In this paper, we study WMs from a causal perspective across multiple levels of abstraction, ranging from perceptual observations to building a conceptual representation of the structure governing the environment dynamics. We argue that useful WMs must go beyond generative capabilities alone: they should also capture entity properties, entity-to-entit...
  </details>

- **2026-08-13** — Jiin Choi, Kyung Hoon Hyun — [CogChat: Knowledge Graph-Augmented Conversational AI with Heterogeneous Graph Transformer for Cognitive Grounding in Design Generation](http://arxiv.org/abs/2608.13216v1)
  <details><summary>📄 Abstract</summary>
  LLM-based chat systems have become valuable tools for design practice, enabling rapid ideation and flexible task support. Yet these systems process designer utterances as generic sequences, maintaining context through recency rather than through any model of how the speaker organizes knowledge. In design conversation, this gap compounds as relational context decays between turns, identical words go unresolved across designers, and the conversation loops or restarts rather than deepens. We presen...
  </details>

- **2026-08-13** — Zhili Shen, Craig Macdonald — [GEM: A Generative Embedding Model Bridging Reasoning and Retrieval](http://arxiv.org/abs/2608.13200v1)
  <details><summary>📄 Abstract</summary>
  Modern LLMs excel at reasoning and instruction following, enabling users to express complex and diverse information needs. However, conventional retrievers largely rely on surface-level matching between queries and documents, resulting in a growing gap between how users express their needs and how retrievers interpret them. In this paper, we present GEM, a generative embedding model that augments retrieval through its own knowledge by explicitly reasoning about user intent and relevance criteria...
  </details>

- **2026-08-13** — Shotaro Tada — [A Radon-Transform Perspective on Exoplanet Transits](http://arxiv.org/abs/2608.13163v1)
  <details><summary>📄 Abstract</summary>
  Transit light curves are usually analyzed under the assumption that the transiting planet has a circular sky-projected silhouette. However, planetary rotation, tides, rings, or atmospheric inhomogeneities can produce non-circular silhouettes. This raises the question of what information transit light curves can provide about the underlying two-dimensional attenuation map. In this paper, we show that, in a simple and transparent limit, the time derivative of the transit light curve during ingress...
  </details>

- **2026-08-13** — Nhan Phan, Ilona Lähteenmäki, Anna von Zansen et al. — [CASA: Content-Acoustic Speaking Assessment with Speech Encoder and Large Language Model](http://arxiv.org/abs/2608.13101v1)
  <details><summary>📄 Abstract</summary>
  Research on automatic speaking assessment (ASA) has increasingly adopted multimodal speech large language models to assess learners' speaking performance. However, existing studies provide limited analysis of how acoustic and content information contribute to predictions and how stable the resulting performance is. We propose CASA, a simpler architecture combining Whisper-medium and Qwen3.5-2B that achieves state-of-the-art performance while providing a more interpretable separation between spee...
  </details>

- **2026-08-13** — Divya Jyoti Bajpai, Kishan Kumar Upadhyay, Manjesh Kumar Hanawal — [SPADE: Speculative Decoding for Precise and Low Cost Distributed Edge Cloud Inference](http://arxiv.org/abs/2608.13076v1)
  <details><summary>📄 Abstract</summary>
  Large Language Models (LLMs) have achieved remarkable success in natural language understanding and generation, but their deployment is constrained by high computational demands. Deploying smaller LLMs directly on the edge can circumvent this, but with degraded accuracy. Deploying smaller cloud-based big LLMs preserves performance, but at the cost of expensive per-token computation. We present a distributed inference framework, \our{}, that integrates speculative decoding (SD) across edge and cl...
  </details>

- **2026-08-13** — David Krüger, Michael Potthoff — [Topology and Quantum-Spin-Classical-Spin Crossover of the Gapped Kondo Effect](http://arxiv.org/abs/2608.13065v1)
  <details><summary>📄 Abstract</summary>
  The gapped Kondo effect describes the screening of an $S=\frac12$ impurity spin locally coupled via an antiferromagnetic exchange interaction to a conduction-electron system exhibiting a finite hard gap. Using a combination of a Lanczos transformation and a self-consistent configuration-interaction scheme, we numerically investigate the local phase diagram. Furthermore, we show that the different phases can be characterized by several topological invariants: the conventional momentum-space Chern...
  </details>

- **2026-08-13** — Dechen Zhang, Xuan Tang, Xinxiang Yin et al. — [VALG: An Agentic System for ML Theory Research](http://arxiv.org/abs/2608.13060v1)
  <details><summary>📄 Abstract</summary>
  Machine learning theory studies learning procedures through mathematical setups in which the data model, training protocol, oracle access, loss, metric, and randomness define the phenomenon that a theorem is meant to explain. Solving an open problem therefore requires the problem formulation, theorem target, and proof mechanism to be developed in concert. Researchers formulate hypotheses, test them through preliminary theoretical or empirical analysis, and refine both assumptions and proofs. We ...
  </details>

- **2026-08-13** — Zhixin Ren, Yau Lyu, Congrong Li et al. — [Momentum as Residual-Driven Multiplier Correction for Deep Learning Optimization](http://arxiv.org/abs/2608.12925v1)
  <details><summary>📄 Abstract</summary>
  Momentum-based optimizers are widely used in modern deep learning, yet the relations among momentum recursion, update geometry, and acceleration remain only partially understood. We develop an $\textbf{A}$DMM-$\textbf{I}$nspired $\textbf{M}$omentum (AIM) framework based on residual-penalty variable splitting, which interprets momentum as a multiplier-like correction driven by the splitting residual. AIM recovers the exponential moving average of gradients from an ADMM-style multiplier update and...
  </details>


## 📊 统计 / Statistics

| 分类 / Category | 论文数 / Count |
|------|--------|
| jailbreak | 583 |
| prompt-injection | 492 |
| memory-poisoning | 44 |
| tool-use-attack | 118 |
| backdoor | 416 |
| adversarial-attack | 563 |
| privacy-leakage | 3846 |
| steganography | 55 |
| misuse | 900 |
| red-teaming | 115 |
| vulnerability | 2714 |
| defense | 2438 |
| alignment | 2261 |
| robustness | 2265 |
| watermark | 300 |
| unlearning | 89 |
| agent-safety | 52 |
| benchmark | 58 |
| survey | 285 |
| other | 6456 |

---

📚 **全部 24050 篇论文**（2022 至今）请访问 [GitHub Pages](https://ny1024.github.io/AgentSafety-Papers/) 查看完整列表、搜索与筛选。

*Generated by AgentGuard at 2026-08-18 18:30:07*