<div align="center">

# AgentGuard 🛡️

**Daily Tracking of LLM Agent Security Papers on arXiv**

[![Auto Update](https://github.com/NY1024/AgentSafety-Papers/actions/workflows/daily-update.yml/badge.svg)](https://github.com/NY1024/AgentSafety-Papers/actions/workflows/daily-update.yml)
[![Papers](https://img.shields.io/badge/Papers-26376-blue)](#)
[![License](https://img.shields.io/badge/License-MIT-green)](#)

</div>

---

## 📖 简介 / Introduction

自动追踪 arXiv 上大模型 Agent 安全方向的最新论文，每日更新，关键词智能分类。

*Automatically tracking the latest LLM Agent security papers on arXiv, updated daily with keyword-based classification.*

**最近更新 / Last Updated**: 2026-09-03 10:34 ｜ **论文总数 / Total Papers**: 26376（近 30 天 / Recent 30 days: 4299）

🌐 **[GitHub Pages](https://ny1024.github.io/AgentSafety-Papers/)** — 查看全部 26376 篇论文（含摘要、分类筛选、搜索）/ View all 26376 papers with abstracts, filters & search

## 📑 分类导航 / Category Navigation

- **[jailbreak](#-jailbreak)** — 越狱攻击 / Jailbreak Attacks — 612
- **[prompt-injection](#-prompt-injection)** — 提示注入攻击 / Prompt Injection Attacks — 523
- **[memory-poisoning](#-memory-poisoning)** — 记忆投毒与篡改 / Memory Poisoning & Tampering — 47
- **[tool-use-attack](#-tool-use-attack)** — 工具使用攻击 / Tool-Use Attacks — 132
- **[backdoor](#-backdoor)** — 后门与投毒攻击 / Backdoor & Poisoning Attacks — 442
- **[adversarial-attack](#-adversarial-attack)** — 对抗攻击 / Adversarial Attacks — 580
- **[privacy-leakage](#-privacy-leakage)** — 隐私泄露 / Privacy Leakage — 3994
- **[steganography](#-steganography)** — 隐写与隐蔽通信 / Steganography & Covert Communication — 61
- **[misuse](#-misuse)** — 滥用与误用 / Misuse & Abuse — 972
- **[red-teaming](#-red-teaming)** — 红队测试 / Red Teaming — 120
- **[vulnerability](#-vulnerability)** — 漏洞与攻击面 / Vulnerabilities & Attack Surfaces — 2954
- **[defense](#-defense)** — 防御与防护方法 / Defense & Protection Methods — 2719
- **[alignment](#-alignment)** — 对齐与安全约束 / Alignment & Safety Constraints — 2536
- **[robustness](#-robustness)** — 鲁棒性与可靠性 / Robustness & Reliability — 2604
- **[watermark](#-watermark)** — 水印与溯源 / Watermarking & Provenance — 382
- **[unlearning](#-unlearning)** — 机器遗忘 / Machine Unlearning — 94
- **[agent-safety](#-agent-safety)** — Agent 安全框架 / Agent Safety Frameworks — 52
- **[benchmark](#-benchmark)** — 安全评测与基准 / Safety Benchmarks & Evaluation — 65
- **[survey](#-survey)** — 综述与系统化 / Surveys & Systematization — 319
- **[other](#-other)** — 其他安全相关 / Other Security-Related — 7168

## 📄 近期论文 / Recent Papers (Last 30 Days)

> 仅展示最近 30 天中最新的 500 篇论文（含日期、作者、摘要）。近 30 天共 4299 篇，完整 26376 篇论文列表请访问 [GitHub Pages](https://ny1024.github.io/AgentSafety-Papers/)

> Showing the latest 500 of 4299 papers from the last 30 days (with date, authors & abstract). For the full list of 26376 papers, visit [GitHub Pages](https://ny1024.github.io/AgentSafety-Papers/)

### 📂 jailbreak
*越狱攻击 / Jailbreak Attacks* — 9 papers

- **2026-09-02** — Qingyu Meng, Yiwei Zha, Jiahuan Pei et al. — [SEAL: Reinforcing Global Safety in Mixture-of-Experts through Shared Expert ALignment](http://arxiv.org/abs/2609.02293v1)
  <details><summary>📄 Abstract</summary>
  Mixture-of-Experts (MoE) is a scaling architecture for large language models that activates only a small subset of expert modules per token, enabling massive parameter growth with nearly constant computation. Recent Hybrid MoE architecture adds \textit{shared experts} to capture consistently useful representations, further improving stability and generalization. MoE now powers many flagship open-source and commercial models, yet remains vulnerable to adversarial attacks. Specifically, sparse rou...
  </details>

- **2026-09-01** — Kaiyan Wen, Shijie Zhang, Lu Yu et al. — [Jailbreaking Text-to-Image Models Through Cracks: Navigating Heterogeneous Safety Filters via Multi-Agent Debate](http://arxiv.org/abs/2609.01168v2)
  <details><summary>📄 Abstract</summary>
  Text-to-image (T2I) models remain vulnerable to jailbreak attacks that elicit Not-Safe-For-Work (NSFW) content, despite increasingly being guarded by heterogeneous, multi-layer safety stacks combining text filters, image classifiers, and cross-modal detectors. Existing jailbreak studies either optimize against individual filters or query the complete pipeline with aggregate feedback, making it difficult to identify the active constraint and adapt to conflicts across safety layers. In this paper,...
  </details>

- **2026-09-01** — Kaiyan Wen, Shijie Zhang, Lu Yu et al. — [Jailbreaking Text-to-Image Models Through Cracks: Navigating Heterogeneous Safety Filters via Multi-Agent Debate](http://arxiv.org/abs/2609.01168v1)
  <details><summary>📄 Abstract</summary>
  Text-to-image (T2I) models remain vulnerable to jailbreak attacks that elicit Not-Safe-For-Work (NSFW) content, despite increasingly being guarded by heterogeneous, multi-layer safety stacks combining text filters, image classifiers, and cross-modal detectors. Existing jailbreak studies either optimize against individual filters or query the complete pipeline with aggregate feedback, making it difficult to identify the active constraint and adapt to conflicts across safety layers.In this paper, ...
  </details>

- **2026-09-01** — Nikita Oblakov, Sabrina Sadiekh, Evgeniy Kokuykin — [HiveTraceGuard-Pro: A Compact Generative Guardrail for Prompt Injection, Jailbreaks, and Adversarial Obfuscation](http://arxiv.org/abs/2609.01046v1)
  <details><summary>📄 Abstract</summary>
  Production LLMs must handle inputs that attempt to override system instructions, bypass safety policies or elicit harmful responses. A common mitigation is a separate guardrail model. Existing reports, however, provide little evidence on Russian prompt injection or Russian surface obfuscation. We present HiveTraceGuard-Pro, a 0.6B generative guardrail LoRA-tuned from Qwen3-0.6B. It is trained on Russian and English and uses one binary scoring rule (safe/unsafe) for the final target turn. Its tra...
  </details>

- **2026-08-31** — Prince Jha, Samuele Poppi, Nils Lukas — [Context Inference Attacks Without Jailbreaks](http://arxiv.org/abs/2609.01663v1)
  <details><summary>📄 Abstract</summary>
  Agentic AI systems are increasingly deployed to process sensitive data at inference time, such as healthcare records or financial documents assembled into a hidden \emph{context} before the system answers. Prior work has studied privacy risks primarily through \emph{jailbreaking} attacks that induce models to directly disclose sensitive content, but has largely overlooked the agentic setting where the context is assembled by the agent's own tool calls. We show that the agents we evaluate remain ...
  </details>

- **2026-08-31** — Qilong Wu, Sahil Wadhwa, Pranab Mohanty et al. — [Validity-Aware Jailbreak Evaluation for Large Language Models](http://arxiv.org/abs/2609.00498v1)
  <details><summary>📄 Abstract</summary>
  Jailbreak robustness has become central to large language model (LLM) safety evaluation, yet prevailing methodologies rely primarily on refusal behavior, semantic resemblance, and intent-matching heuristics that emphasize linguistic plausibility rather than correctness. We identify a key limitation in existing evaluations: many jailbreak intents depend on instructional validity rather than epistemic factuality, allowing realistic-looking responses to be labeled successful despite being factually...
  </details>

- **2026-08-31** — Jiaxuan Li, Jiahao Zhang, Duc Minh Vo et al. — [Do VLMs Share Safety Neurons Across Modalities?](http://arxiv.org/abs/2608.30750v1)
  <details><summary>📄 Abstract</summary>
  Vision-language models (VLMs) can comply with harmful requests delivered through images, even when their LLM backbones would refuse the same content in text. While prior work characterizes these jailbreaks empirically or at the representation level, how visual inputs perturb safety pathways at the neuron level remains uncharted. We close this gap with a causal, neuron-level analysis of safety mechanisms in 10 VLMs. We propose a two-stage detection pipeline with iterative ablation that accounts f...
  </details>

- **2026-08-31** — Yuna Park, Hwang Youn Kim, Yujin Kim et al. — [The Fragility of Jailbreak Robustness Across Operational States](http://arxiv.org/abs/2608.30748v1)
  <details><summary>📄 Abstract</summary>
  Existing jailbreak evaluations typically characterize robustness using a single attack success rate (ASR) measured in a default configuration (the vanilla state). However, user-LLM interactions can induce diverse operational states beyond the vanilla state. In this work, we find that jailbreak robustness is highly fragile to operational-state variation: even when the attack remains fixed, changing only an ordinary system prompt not designed to affect safety can dramatically alter attack success ...
  </details>

- **2026-08-31** — Md Mokarram Chowdhury, Ernie Chang, Yang Li — [The Safety Relay in Roleplay Jailbreaks: A Component-Resolved Causal Analysis of Harm Recognition and Refusal](http://arxiv.org/abs/2608.30585v1)
  <details><summary>📄 Abstract</summary>
  Large language models are trained to follow instructions while refusing harmful requests. Jailbreaks exploit this balance to elicit content a model would ordinarily reject. Roleplay jailbreaks are especially concerning: the harmful request can remain visible inside a roleplay wrapper made of a persona, scenario, and task, yet the model may comply. We use mechanistic interpretability to determine how this context reverses refusal and which elements contribute to the reversal. Across two benchmark...
  </details>


### 📂 prompt-injection
*提示注入攻击 / Prompt Injection Attacks* — 10 papers

- **2026-09-02** — Jun He, Deying Yu — [Stored Is Not Supported: Typed Provenance and Assertion Guardrails for Persistent AI Agents](http://arxiv.org/abs/2609.02127v1)
  <details><summary>📄 Abstract</summary>
  Persistent AI agents construct autobiographical state through reflection, retrieval, and consolidation. Persistence changes availability, not epistemic standing: stored or retrieved material is not thereby supported. Untrusted inputs, prompt injections, and model inferences can therefore enter persistent state and later be presented as agent history or user commitments. We specify typed provenance and assertion guardrails for autobiographical assertion boundedness, a system-relative release prop...
  </details>

- **2026-09-02** — Qikai Wang, Yongzhao Zhang, Zhiwei Chen et al. — [Implicit Manipulation for Skill Selection in LLM Agents with Semantic Matching](http://arxiv.org/abs/2609.02035v1)
  <details><summary>📄 Abstract</summary>
  Skill selection is a key stage in LLM-agent workflows, determining which installed skill should handle a user request. Existing attacks on this stage primarily rely on explicit prompt injection or instruction-level steering, which can expose recognizable manipulation signals. In this work, we identify a new implicit attack surface for skill selection: even when the user prompt and skill description appear benign in isolation, their semantic relationship can still be strategically shaped to favor...
  </details>

- **2026-09-01** — Laurent Bindschaedler, Quentin Botha, Christoph Siebenbrunner — [Agent Flight Recorder: Tamper-Evident Audit Trails with On-Chain Anchoring for Long-Horizon Tool-Using Agents](http://arxiv.org/abs/2609.01931v1)
  <details><summary>📄 Abstract</summary>
  Long-horizon agents execute thousands of actions, resulting in sequential failures rather than isolated errors. When a coding agent deletes a production database or a prompt injection spreads across agents, the incident raises questions of causality, authority, and non-repudiable third-party verification. The Agent Flight Recorder captures each agent action as a structured, canonically serialized event binding eight semantic fields from intent through execution to provenance. Hash chaining and M...
  </details>

- **2026-09-01** — Ziwei Zhao, Yu Gu, Haojun Liang et al. — [Skill-as-API: Confidential Multi-Agent Coordination for Agentic Software Engineering](http://arxiv.org/abs/2609.01677v1)
  <details><summary>📄 Abstract</summary>
  AI coding agents are evolving from solitary tools into collaborative teammates that discover and invoke one another's specialized skills. But the coordination channel itself can leak a skill's intellectual property. Protocols such as MCP and A2A run implementations server-side, yet they still publish each skill's description and typed schemas to every peer, offer no way to hide a skill's existence, and cannot guarantee that a wrapped system prompt stays off the wire. Application-layer privacy fi...
  </details>

- **2026-08-31** — Panduranga Sai Varma Dantuluri, Jyotirmoy Sundi — [Delegation Without Trust: An Empirical Gap Analysis of Identity, Authorization, and Runtime Governance in Multi-Agent LLM Systems](http://arxiv.org/abs/2609.00267v1)
  <details><summary>📄 Abstract</summary>
  Autonomous LLM agents increasingly act on a user's behalf: they hold credentials, call tools and services, and spawn sub-agents that act further on their behalf. This turns a long-standing distributed-systems question -- who is authorized to do what, on whose authority -- into an urgent and largely unsolved problem, because the component driving each agent is a language model an adversary can hijack. We argue that agent security must be evaluated under an untrusted-model assumption: a correct sy...
  </details>

- **2026-08-31** — Yunseok Lee, Yunji Kim, Woojin Lee — [Will the User Ever Know? Covert Indirect Prompt Injection Attacks on Tool-Using LLM Agents](http://arxiv.org/abs/2608.30362v2)
  <details><summary>📄 Abstract</summary>
  As LLM agents take real-world actions through tools, indirect prompt injection (IPI) has emerged as a serious threat. The standard metric, Attack Success Rate (ASR), counts whether an injection succeeds but ignores what the user notices in the agent's final response. Looking at successful injection traces, we find two distinct outcomes: the agent executes the injection while returning an otherwise normal response, or reports the injected action in its final response, giving the user a chance to ...
  </details>

- **2026-08-31** — Shiqian Zhao, Yangfan Zhou, Xinfeng Li et al. — [ECLIPSE: Self-Evolving Stealthy Prompt Injection Attack against Long-Horizon Agentic Systems](http://arxiv.org/abs/2608.30441v1)
  <details><summary>📄 Abstract</summary>
  Recently, large language model (LLM) agents, such as Codex, Claude Code, and OpenClaw, have become capable of planning and executing long-horizon tasks through repeated tool calls. This capability also creates new opportunities for prompt injection. Existing attacks either place the malicious objective in one explicit instruction, making it easy to detect, or distribute the intent across multiple execution stages, making successful completion unreliable.   In this work, we propose ECLIPSE, a sel...
  </details>

- **2026-08-31** — Lifei Liu, Haoran Yu — [Attesting Outputs and Delegation Ancestry in Multi-Agent AI Systems](http://arxiv.org/abs/2608.30387v1)
  <details><summary>📄 Abstract</summary>
  Multi-agent applications delegate work across independently operated deployers. After an incident, a verifier must answer two questions: which deployer released the reported bytes, and whether each cross-deployer edge was authorized. Credentials establish who may act, but need not bind them to later output bytes or prove both deployers authorized a dynamically created edge. We present a two-layer attestation design for dynamic delegation without a shared authority, public log, or precommitted wo...
  </details>

- **2026-08-31** — Yunseok Lee, Yunji Kim, Woojin Lee — [Will the User Ever Know? Covert Indirect Prompt Injection on Tool-Using LLM Agents](http://arxiv.org/abs/2608.30362v1)
  <details><summary>📄 Abstract</summary>
  As LLM agents take real-world actions through tools, indirect prompt injection (IPI) has emerged as a serious threat. The standard metric, Attack Success Rate (ASR), counts whether an injection succeeds but ignores what the user notices in the agent's final response. Looking at successful injection traces, we find two distinct outcomes: the agent executes the injection while returning an otherwise normal response, or reports the injected action in its final response, giving the user a chance to ...
  </details>

- **2026-08-31** — Chen Xiong, Zhiyuan He, Pin-Yu Chen et al. — [SIR: Self-improving Red-teaming for Compute Use Agents](http://arxiv.org/abs/2608.30207v1)
  <details><summary>📄 Abstract</summary>
  Computer use agents (CUAs) are vision-language models that perceive a screen and act on a real operating system through mouse, keyboard, and terminal, and they are increasingly deployed to automate everyday digital tasks. Because they can be exposed to untrusted content while operating, they are vulnerable to indirect prompt injection (IPI), in which an adversary plants instructions in content the agent will read and redirects it toward actions that violate the user's intent. Existing CUA safety...
  </details>


### 📂 memory-poisoning
*记忆投毒与篡改 / Memory Poisoning & Tampering* — 3 papers

- **2026-09-02** — S M Asif Hossain, Ruksat Khan Shayoni, Md Kishor Morol — [CAPTURE: Disentangling Preference Drift from Memory Poisoning in Personalized LLM Agents](http://arxiv.org/abs/2609.02265v1)
  <details><summary>📄 Abstract</summary>
  Personalized language agents use persistent memory to adapt to users over time, but the same mechanism creates an attack surface. When new information conflicts with stored preferences, an agent must distinguish genuine preference drift from temporary context shifts, ambiguity, or adversarial memory poisoning. We formulate this problem as a continuous-time partially observable decision process over a latent user state and show why rules based only on recency and provenance are insufficient. CAPT...
  </details>

- **2026-09-01** — Chuanchao Zang, Jianing Wang, Wenyu Chen et al. — [Transferable End-to-End Optimization for Indirect Long-Term Memory Poisoning in LLM Agents](http://arxiv.org/abs/2609.00523v1)
  <details><summary>📄 Abstract</summary>
  Long-term memory can turn untrusted external content into persistent influence over an LLM agent's future decisions, creating the threat of indirect memory poisoning. A successful attack must survive a multi-stage pipeline comprising memory writing, retrieval, and utilization. Existing attacks largely rely on intra-stage optimization, optimizing individual stages in isolation while overlooking inter-stage coupling. Specifically, these stages impose different requirements on the same poisoning co...
  </details>

- **2026-08-31** — Chuanchao Zang, Zijian Cao, Xiangtao Meng et al. — [Understanding Stage-Wise Utility-Risk Trade-offs in LLM Agent Memory](http://arxiv.org/abs/2608.30177v1)
  <details><summary>📄 Abstract</summary>
  Long-term memory is becoming a core capability of LLM agents, enabling personalization and long-horizon interaction. However, memory mechanisms that retain, transform, or expose more information can affect both benign utility and susceptibility to memory poisoning. Existing evaluations typically measure memory utility or attack risk in isolation under fixed configurations, providing limited insight into how stage-specific design choices reshape their trade-off. We present \textsc{MemGauge}, a co...
  </details>


### 📂 tool-use-attack
*工具使用攻击 / Tool-Use Attacks* — 2 papers

- **2026-09-02** — Jiarui Li, Jiahao Chen, Chunyi Zhou et al. — [A Finger on the Scale: Covert Policy Steering through Agentic Skills](http://arxiv.org/abs/2609.02564v1)
  <details><summary>📄 Abstract</summary>
  Reusable agent skills extend large language model (LLM) agents with task procedures, tool-use guidance, and output constraints. Yet these skills also act as externalized behavioral policies, which create a supply-chain risk: a third-party skill may preserve the declared task and valid output interface while covertly redirecting agent decisions toward an undisclosed objective. We formalize Skill Policy Integrity, which requires a Skill-induced policy to remain aligned with its declared functional...
  </details>

- **2026-09-01** — Jinqing Zhao, Chengcan Wu — [Making Prospective Memory SLM-Shaped: Typed Intention Stores for Small-Model Agents](http://arxiv.org/abs/2609.01272v1)
  <details><summary>📄 Abstract</summary>
  Prospective memory means carrying out a deferred intention at the right future cue while other work continues. Benchmarks now isolate it as an agent skill, yet frontier LLMs still struggle: the best published PM-Bench scaffold reaches only 65.1% Set-F1. We argue that this loop is schema-constrained state tracking rather than open-ended reasoning, and that small models can execute it when the action space is typed. We propose the Prospective Intention Store (PIS) that puts lifecycle logic in code...
  </details>


### 📂 backdoor
*后门与投毒攻击 / Backdoor & Poisoning Attacks* — 7 papers

- **2026-09-02** — Varun Gadey, Ziad Marey, Alexandra Dmitrienko — [CodePoisonRAG: Knowledge Poisoning Attacks on Retrieval-Augmented Code Generation](http://arxiv.org/abs/2609.02774v1)
  <details><summary>📄 Abstract</summary>
  Retrieval-Augmented Code Generation (RACG) improves LLM-based software development by retrieving external code artifacts, documentation, and patches, and incorporating them into the generation context. This reliance on external knowledge introduces a critical trust boundary: poisoned artifacts can influence generated code without modifying the underlying LLM. Prior work shows that selecting existing vulnerable examples can increase the general vulnerability rate of RACG outputs, but leaves open ...
  </details>

- **2026-09-02** — Shuyao Xiao, Shengling Wang, Haoyu Niu et al. — [Who Drives the Probability Game of VLMs? A Temporal Causal Drive Evaluation Framework](http://arxiv.org/abs/2609.02000v1)
  <details><summary>📄 Abstract</summary>
  Vision-language models (VLMs) are increasingly evaluated on complex image and video understanding tasks, yet conventional metrics primarily assess final-answer quality and reveal little about how different information sources shape the generation process. We propose a causal and temporal evaluation framework that traces the evolving roles of visual input, question text, and generated prefixes during autoregressive decoding. Grounded in a Structural Causal Model, we use interventions and backdoor...
  </details>

- **2026-09-01** — Zhiqi Huang, Vivek Datla, Zhichao Xu et al. — [VerTox: Verifiable Reward-Guided Corpus Poisoning Against Neural Ranking Models](http://arxiv.org/abs/2609.01325v1)
  <details><summary>📄 Abstract</summary>
  Neural ranking models have become core components of modern information retrieval systems and important building blocks of AI systems such as retrieval-augmented generation (RAG) pipelines. However, their robustness remains insufficiently understood in the presence of large language models (LLMs), which can generate fluent and deceptive content at scale. This work investigates the vulnerability of neural ranking models to corpus poisoning attacks, in which an adversary injects a small number of ...
  </details>

- **2026-09-01** — Chou Jin Chua, Sarang Nambiar, Murali Srinivasan et al. — [AKRASIA: Stealthy Backdoor Attack on Reasoning-based Code LLMs](http://arxiv.org/abs/2609.01023v1)
  <details><summary>📄 Abstract</summary>
  We present AKRASIA, a stealthy, inference-time backdoor attack against reasoning-based Code LLMs. AKRASIA aims to achieve a backdoor target (e.g., malicious code execution) in reasoning LLMs while evading automated defenses and human inspection. To achieve this, AKRASIA probes the victim LLM to construct a code-level backdoor trigger. It then employs in-context learning for backdoor learning, and model unfaithfulness to conceal the backdoor trigger, and generate plausible reasoning. We evaluate ...
  </details>

- **2026-08-31** — Muhaimin Bin Munir, Akib Jawad Ononto, Nazia Shehnaz Joynab et al. — [TRIS: A Tri-Layer Retrieval Integrity Sieve Against Knowledge Poisoning](http://arxiv.org/abs/2609.00470v1)
  <details><summary>📄 Abstract</summary>
  Retrieval-Augmented Generation (RAG) grounds large language models in external corpora, but implicit trust in retrieved documents creates a critical attack surface: PoisonedRAG shows that a handful of crafted passages can dominate dense retrieval and steer generation toward attacker-chosen answers. We present the Tri-Layer Sieve, a middleware defense that sanitizes retrieved evidence through cross-embedding-space clustering with an independent judge model, structural filtering of trigger-payload...
  </details>

- **2026-08-31** — Fukang Zhu, Binbin Zhao, Ruixiao Lin et al. — [Beyond the Payload: How User Invocation Shapes Coding Agent Vulnerability to Repository Poisoning](http://arxiv.org/abs/2608.30686v1)
  <details><summary>📄 Abstract</summary>
  Coding agents are increasingly used for software engineering tasks, including bootstrapping projects from third-party repositories whose integrity cannot be assumed. Prior work on repository poisoning largely focuses on attacker-controlled injection and disguise, but developers also shape risk through everyday invocation choices: what task to delegate, how to phrase the request, and which skills or rules to supply. We term these user-side choices Prompt-Level Configurations (PLCs) and introduce ...
  </details>

- **2026-08-31** — Yizhe Zeng, Chenxu Niu, Wei Zhang et al. — [Why Are LLM Backdoor Defenses Fragmented? A Feature-Level Explanation with Sparse Autoencoders](http://arxiv.org/abs/2608.30403v1)
  <details><summary>📄 Abstract</summary>
  Backdoor attacks pose a serious threat to large language models (LLMs), but existing defenses remain fragmented, failing to pro?vide unified defense against both dirty-label and clean-label attacks. To investigate why such fragmentation arises, we present the first systematic feature-level mechanistic analysis of LLM backdoors using sparse autoencoders (SAEs). Starting from a 2 x 2 comparison of clean and poisoned models on clean and triggered inputs, we trace backdoor-induced logit shifts to hi...
  </details>


### 📂 adversarial-attack
*对抗攻击 / Adversarial Attacks* — 7 papers

- **2026-09-02** — Chengyin Hu, Dingyi Lu, Jiaju Han et al. — [InfraPatch: Cross-Task Targeted Grayscale Patch Attacks on Infrared-Adapted Vision-Language Models](http://arxiv.org/abs/2609.02233v1)
  <details><summary>📄 Abstract</summary>
  Infrared vision-language models (IR-VLMs) have emerged as a promising paradigm for multimodal perception under low-visibility conditions, yet their robustness to targeted adversarial attacks remains poorly understood. Existing adversarial patch methods mainly study RGB-based models or a single downstream task and do not characterize whether localized perturbations can induce an intended semantic target in IR-VLMs. We propose InfraPatch, a white-box, per-instance framework for targeted digital gr...
  </details>

- **2026-09-01** — Polina Tapal, Bryce-Allen Bagley — [Adversarial Vulnerabilities of Neural Biomarker Identification Systems](http://arxiv.org/abs/2609.01856v1)
  <details><summary>📄 Abstract</summary>
  There is growing interest in the proposed use of EEG signals as biometric credentials, but thus far there has been little research on the reliability and security of such biometrics. Prior adversarial tests have focused on deep-learning classifiers and assumed attackers have full access to the classifier model. This has left unexamined other, more popular categories of neural signature methods as well as the more realistic case of an adversary having only black-box access to a classifier. In thi...
  </details>

- **2026-09-01** — Daizong Liu, Junhao Dong, Zhiyuan Ma et al. — [Forbid Your Attention: Fooling Multimodal Large Language Models by Selectively Removing Intrinsic Focus in Spectral Domain](http://arxiv.org/abs/2609.00788v1)
  <details><summary>📄 Abstract</summary>
  Multimodal large language models (MLLMs) have extended the capability of large language models (LLMs) to process more contextual multimodal information, showing remarkable progress in diverse realistic multimodal applications. Despite their strong perception and reasoning abilities, recent studies reveal that MLLMs remain highly vulnerable to adversarial inputs, especially those targeting visual components. However, existing attacks mainly focus on global perturbations, lacking an understanding ...
  </details>

- **2026-09-01** — Md Ajwad Akil, Adrian Shuai Li, Imtiaz Karim et al. — [PhantomCall: Evading ML Malware Detectors via Function Call Graph Perturbation](http://arxiv.org/abs/2609.00705v1)
  <details><summary>📄 Abstract</summary>
  Prior adversarial attacks on Windows PE malware detectors target raw bytes, PE headers, or intra-function control-flow graphs, leaving the function call graph (FCG) unexplored as an attack surface. Yet the FCG structure is an important feature in graph-based malware detectors. We present Phan- tomCall, a black-box attack that perturbs the FCG of Windows PE malware by injecting fully executable dummy functions at targeted call sites, adding new nodes and edges to both the CFG and FCG while preser...
  </details>

- **2026-09-01** — Padmeswari Nandiya, Ahmad Mohsin, Ahmed Ibrahim et al. — [NeuroGraph: An AI Graph-Driven Neuro-Symbolic Framework for Explainable Threat Reasoning in Advanced Manufacturing](http://arxiv.org/abs/2609.00604v1)
  <details><summary>📄 Abstract</summary>
  The growing complexity of cyber-physical attack surfaces in advanced manufacturing has made cyber threat intelligence analysis increasingly difficult. Although large language models and retrieval-augmented generation have improved CTI workflows, text-based approaches remain vulnerable to hallucinations and provide limited support for structured reasoning over interconnected threats. Graph-based RAG reduces some of these limitations, but existing approaches often lack ontology-consistent multi-ho...
  </details>

- **2026-09-01** — Jungyeon Lee, Yejin Yoon, Taeuk Kim — [Same Semantics, Different Outcome: On the Modality Robustness of Multimodal LLMs under Knowledge Conflict](http://arxiv.org/abs/2609.00550v1)
  <details><summary>📄 Abstract</summary>
  Multimodal large language models (MLLMs) are increasingly provided with contextual evidence in heterogeneous forms: as a text passage, as a rendered image of the same passage, or as both together. However, it remains unclear how consistently these surface forms are processed, especially when the evidence conflicts with the model's parametric knowledge. We study modality robustness under knowledge conflict across 13 MLLMs and two datasets, and find them far from robust. (1) Contrary to common bel...
  </details>

- **2026-08-31** — Peiyang Xu, Xiaopei Zhu, Jun Zhu et al. — [Beyond Language Priors: Diagnosing and Fixing Visual-Origin Hallucinations in Multimodal LLM](http://arxiv.org/abs/2609.00231v1)
  <details><summary>📄 Abstract</summary>
  Existing research on object hallucination in multimodal large language models (MLLMs) predominantly attributes the problem to language priors such as over-reliance on textual co-occurrence statistics. We challenge this view by presenting quantitative evidence for a complementary, under-explored cause: visual-origin hallucination, where hallucinations arise from incorrect visual feature extraction and misalignment between image and text embeddings. Through cosine similarity analysis and Smooth Gr...
  </details>


### 📂 privacy-leakage
*隐私泄露 / Privacy Leakage* — 35 papers

- **2026-09-02** — Smitha Muthya Sudheendra, Jaideep Srivastava — [PragAlign: Feedback-Guided Pragmatic Alignment for Controlled Synthetic Dialogue Generation](http://arxiv.org/abs/2609.02480v1)
  <details><summary>📄 Abstract</summary>
  Synthetic dialogue generation can support research in privacy-restricted service settings, but generated conversations must preserve communicative intent, affective meaning, and natural dialogue flow. We introduce PragAlign, a feedback-guided framework for controlled synthetic dialogue generation conditioned on service context, target intent, and target emotion, with auxiliary trait-style controls. PragAlign uses a generate--evaluate--revise loop in which an LLM-based evaluator scores intent ali...
  </details>

- **2026-09-02** — Vishnu Prasad Vijaya Kumar, Santhosh Venkatesh, Ivan P. Yamshchikov — [LeakageBench: Document-Level Leakage Risk for Redacting Personally Identifiable Information in Document Images](http://arxiv.org/abs/2609.02207v1)
  <details><summary>📄 Abstract</summary>
  Real-world personally identifiable information (PII) redaction often operates on document images---scans, screenshots, and PDF renderings---where OCR errors, layout structure, and visual noise determine whether sensitive information is actually removed. Existing PII benchmarks are mostly text-centric and do not measure document-level redaction risk: a page remains unsafe if even one identifier is missed. We introduce LeakageBench, a challenge set of 500 document images with 11,954 GDPR-aligned P...
  </details>

- **2026-09-02** — Sanjaya Poudel, Nirajan Kunwor, Manish Dhakal et al. — [Federated LoRA Adaptation of BiomedCLIP Across Four International Chest X-Ray Cohorts](http://arxiv.org/abs/2609.02101v1)
  <details><summary>📄 Abstract</summary>
  Federated learning (FL) lets institutions train a shared model without exchanging data, and Low-Rank Adaptation (LoRA) makes this practical at scale by communicating only compact low-rank updates. Biomedical imaging is a compelling setting for this combination: patient data are archived behind privacy regulations, and institutions differ widely in scanners, protocols, and compute. Such heterogeneity raises the question of how federated LoRA updates should be aggregated, increasingly pressing as ...
  </details>

- **2026-09-02** — Zhaoyang Jiang, Zhizhong Fu, Yunsoo Kim et al. — [Learning to Fuse LLMs with Ontology Rankers for Rare-Disease Diagnosis](http://arxiv.org/abs/2609.02473v1)
  <details><summary>📄 Abstract</summary>
  Ontology rankers remain useful for rare-disease diagnosis because each candidate can be traced to matched patient phenotypes. Large language models (LLMs) can generate differential diagnoses from the same patient description, but their predictions lack an equally clear evidence trail. Rather than asking which system should replace the other, we ask whether an LLM can improve the ranker without giving up its evidence. Our behavior-based fusion model examines the two ranked lists, their agreement,...
  </details>

- **2026-09-02** — Bizhe Bai, Jiakang Yuan, Hongming Wu et al. — [Efficient GUI Agents: A Systems Survey of Observation, Memory, Action, and Runtime Optimization](http://arxiv.org/abs/2609.02309v1)
  <details><summary>📄 Abstract</summary>
  GUI agents increasingly operate across websites, mobile apps, and desktop environments, yet the field still reports progress primarily through task success. We argue that practical deployment depends equally on efficiency: how much context, computation, action budget, and runtime overhead an agent consumes while succeeding. This survey studies efficient GUI agents through an end-to-end systems lens that preserves the current technical axes of observation efficiency, context and memory efficiency...
  </details>

- **2026-09-02** — Thomas Brackin — [Privacy Washing: Detecting Internal Contradictions in Privacy Policies](http://arxiv.org/abs/2609.02055v1)
  <details><summary>📄 Abstract</summary>
  Privacy policies may contain internal contradictions in which commitments are undermined by practices documented elsewhere in the same policy. We operationalize this phenomenon, privacy washing, through a four-stage pipeline: statement extraction, compatibility filtering and natural language inference screening, multi-model judge verification, and thematic analysis, with contradictions confirmed by majority vote of a three-model LLM panel. Applied to two corpora of website privacy policies, 123 ...
  </details>

- **2026-09-02** — Taixi Chen, Nancy Guo — [Test-Time Logit Prompting for Source-Free Missing Modality Adaptation](http://arxiv.org/abs/2609.02039v1)
  <details><summary>📄 Abstract</summary>
  Vision-language models (VLMs) have achieved remarkable performance by leveraging complementary information from large-scale image-text pairs. However, missing-modality inputs are commonly encountered during real-world deployment, often leading to significant performance degradation. Existing methods primarily enhance model robustness by learning modality compensation strategies from source training data. However, their reliance on source training data makes them difficult to apply when original ...
  </details>

- **2026-09-01** — Kunlin Cai, Kaiyuan Zhang, Zihang Xiang et al. — [Hearing the Whispers: Black-Box Membership Inference Attacks on Finetuned TTS Models](http://arxiv.org/abs/2609.01723v1)
  <details><summary>📄 Abstract</summary>
  Text-to-Speech (TTS) foundation models are increasingly fine-tuned on private datasets to synthesize highly personalized voices, introducing severe privacy risks by exposing both biometric identities and sensitive speech content. Existing black-box membership inference attacks (MIAs) follow a two-stage pipeline of query generation and representation engineering, both of which face unique challenges when adapted to TTS. For query generation, dual conditioning on synthesis text and reference speec...
  </details>

- **2026-09-01** — Gene Zhang — [Zeta-Lite: A Concurrent, Branchable In-Browser SQL Database for Agentic Memory](http://arxiv.org/abs/2609.01818v1)
  <details><summary>📄 Abstract</summary>
  The browser has become a first-class database host: applications increasingly want to store, query, and reason over structured data entirely on the client - for privacy, offline operation, local-first collaboration, and, most recently, as durable memory for in-browser AI agents. One way to get SQL in the browser, compiling PostgreSQL to WebAssembly (PGlite), inherits PostgreSQL's process model: a single backend connection that executes one statement at a time and blocks. That model cannot expres...
  </details>

- **2026-09-01** — Ehsan Faghih, Fatemeh Ashrafi, Marguerite Moore et al. — [Ten Architectures, One Error: Shared Failure Modes in Hyperspectral Classification under Spatially Disjoint Evaluation](http://arxiv.org/abs/2609.01786v1)
  <details><summary>📄 Abstract</summary>
  Hyperspectral image classification still relies heavily on random pixel splits within a single scene. The Salinas dataset, randomly split, is among the most widely used datasets for comparing different architectures. However, under a random split method, a large fraction of test pixels fall immediately adjacent to a training pixel, which inflates reported accuracy. This work introduces a leakage-free evaluation protocol linking spatial separation to the model's receptive field. Applying this pro...
  </details>

- **2026-09-01** — Yu Nong, Yao Du, Tianxiang Xu et al. — [The Data Problem in Software Vulnerability Analysis: Artifacts, Quality, and Consumption](http://arxiv.org/abs/2609.01503v1)
  <details><summary>📄 Abstract</summary>
  Learning- and LLM-based software vulnerability analysis is only as trustworthy as the data it is trained and evaluated on, yet that data is rarely examined as a first-class object. We investigate the data behind vulnerability analysis through a dataset-centric taxonomy that separates what an artifact is (code, metadata, patches, tests/PoCs, reasoning, traces), how good it is (realism, label evidence, scale, diversity, leakage, availability), and what it is used for. From a systematically assembl...
  </details>

- **2026-09-01** — Nicolas Constantinides, Mahdi Rahimi, Stavros Nonis — [Hidden Services Protocol for Mixnets](http://arxiv.org/abs/2609.01326v1)
  <details><summary>📄 Abstract</summary>
  Mix networks (mixnets) provide network-level privacy by routing each communication packet through a sequence of intermediaries, called mixnodes, that randomly delay and cryptographically transform packets before forwarding them, making it difficult for observers to link mixnet entries to exits. While this mechanism protects sender privacy from both external adversaries and the receiver, existing mixnets lack a secure and practical protocol that simultaneously protects receiver (destination) priv...
  </details>

- **2026-09-01** — Stefano Leggio, Giulio Rossolini, Alessandro Biondi — [Position Matters: Feature Inversion Attacks in ViT Split Inference with Token Reduction and Shuffling](http://arxiv.org/abs/2609.01232v1)
  <details><summary>📄 Abstract</summary>
  Vision Transformers (ViTs) are increasingly used in split-inference systems, where edge devices transmit intermediate token representations to a remote cloud. In this setting, token reduction lowers computation and communication costs, while token shuffling disrupts the spatial organization of the transmitted tokens, potentially limiting information leakage. However, their privacy benefits remain unclear against feature inversion attacks, which attempt to reconstruct the input from the transmitt...
  </details>

- **2026-09-01** — Shengfang Zhai, Leo Marchyok, Yuling Shi et al. — [Membership Inference in Fine-tuned Diffusion Language Models via Token-level Memorization Asymmetry](http://arxiv.org/abs/2609.00873v1)
  <details><summary>📄 Abstract</summary>
  Diffusion language models (DLMs) have recently emerged as an alternative modeling paradigm to autoregressive LMs, offering advantages such as parallel generation and bidirectional context modeling. Despite growing interest in their generative capabilities, the privacy risks of DLMs remain underexplored. We identify a phenomenon termed token-level memorization asymmetry through theoretical analysis of diffusion training dynamics. Building on this finding, we propose Q-Skew, a quantile-weighted sk...
  </details>

- **2026-09-01** — Danze Chen, Zeqing Wang, Ziyue Lin et al. — [H3-World: Turning Language Understanding into World Control](http://arxiv.org/abs/2609.01560v1)
  <details><summary>📄 Abstract</summary>
  We present H3-World, an efficient framework that turns the 33B MiniMax-H3 video generator into an interactive world model. Our key finding is that, as large video generators become more capable, language is emerging as a natural interface for control. MiniMax-H3, for example, already supports zero-shot control of character behavior and camera motion through natural-language instructions. Building on this, H3-World turns this coarse language interface into precise, temporally grounded world contr...
  </details>

- **2026-09-01** — Maryam Alshehyari, Dushyant Singh Chauhan, Samuele Poppi et al. — [CopyShield: A Cross-Level Benchmark of Copyright Defenses in LLMs](http://arxiv.org/abs/2609.01161v1)
  <details><summary>📄 Abstract</summary>
  Large language models can reproduce memorized text verbatim, yet copyright defenses are usually evaluated under incompatible protocols. We introduce CopyShield, a controlled benchmark comparing three representative defenses at distinct intervention levels: contrastive decoding (output), Direct Preference Optimization (behavioral), and activation intervention (representation). We evaluate CopyShield on two model families, LLaMA-3.1-8B and Mistral-7B-v0.3, using controlled memorization over five p...
  </details>

- **2026-09-01** — Che Hyun Lee, Sangkwon Park, Donghun Kang et al. — [Phrase-Localized Language-Contrastive Guidance: Training-Free Localized Accent Control for Code-Switching Text-to-Speech](http://arxiv.org/abs/2609.01016v1)
  <details><summary>📄 Abstract</summary>
  Current speech synthesis struggles with code-switching, which mixes a foreign language phrase into a primary language utterance, causing the phrase to be spoken with the primary language's accent rather than its native one. We propose Phrase-Localized Language-Contrastive Guidance (LCG), a training-free inference framework that restores a native accent to code-switched phrases in cross-lingual text-to-speech. LCG replaces the single language guidance applied across the whole utterance with a sep...
  </details>

- **2026-09-01** — Wen Jiang, Mingmin Chu, Yimeng Tian et al. — [HarnessEvolve: Learning from Reference Trajectories for Reliable Agent Self-Evolution](http://arxiv.org/abs/2609.00829v1)
  <details><summary>📄 Abstract</summary>
  Self-evolving agents advance toward autonomy by optimizing their harness---prompts, skills, tools, and execution logic---based on environmental feedback. This paradigm, however, is hampered by three challenges: \textit{credit assignment failure}, where terminal success/failure feedback makes it ambiguous which step caused the error; \textit{shortcut learning}, where agents memorize task-specific patterns rather than acquire generalizable capabilities; and \textit{catastrophic forgetting}, where ...
  </details>

- **2026-09-01** — Bhuvan Koduru, Dareen Safar B Alharthi, Rita Singh et al. — [Heard but Not Heeded: Paralinguistic Information Encoding and Loss in Audio-Language Models](http://arxiv.org/abs/2609.00727v1)
  <details><summary>📄 Abstract</summary>
  Audio language models are designed to understand speech, yet it remains unclear whether they capture how something is said beyond what is said. We present a mechanistic analysis of paralinguistic information in four open source models, Whisper-large-v2, Qwen2-Audio-7B Instruct, Qwen2.5-Omni-7B, and Chroma-4B, using the Expresso dataset with controlled speaking styles. We combine centered kernel alignment, linear probing with leave one speaker out evaluation, open ended tone prediction, and a con...
  </details>

- **2026-09-01** — Miso Kim, Georu Lee, Seungwon Jeong et al. — [Confess What You Know: Forget-Set Misalignment with Model Knowledge in LLM Unlearning](http://arxiv.org/abs/2609.00605v1)
  <details><summary>📄 Abstract</summary>
  Machine unlearning for large language models (LLMs) often assumes that a pre-defined forget set matches what the model has memorized, but this frequently breaks in realistic privacy settings where the original training data is inaccessible. We term this gap forget-set misalignment and identify two cases. In Under Unlearning, the forget set omits memorized information and leakage persists. In Out-of-Knowledge Unlearning, the algorithm is driven to "forget" knowledge the model never learned, pertu...
  </details>

- **2026-09-01** — Byunggu Yu, Justin Kim — [Wave Function Backpropagation with Explicit Temporal-Interval Dynamics](http://arxiv.org/abs/2609.00503v1)
  <details><summary>📄 Abstract</summary>
  Conventional neural networks learn predominantly through affine transformations followed by nonlinear activations, while elapsed time is often treated as an auxiliary feature or assumed to be uniformly sampled. This paper introduces Wave Function Backpropagation (WFB), a wave-parameterized learning formulation in which neural responses are represented by learnable amplitude, wavenumber, angular frequency, and phase. The formulation associates an observed state with its temporal interval Delta t ...
  </details>

- **2026-09-01** — Maksim Evdokimov, Matvey Ivanov, Dmitrii Tsiupin et al. — [Closing Cost-Quality Gap in Document VLMs: Difficulty-Aware Data Curation and Quality-Adjusted Deployment Economics](http://arxiv.org/abs/2609.01575v1)
  <details><summary>📄 Abstract</summary>
  Extracting structured fields from hundreds of millions of documents annually remains costly in regulated industries: bespoke OCR cascades cover only a fraction of workflows, privacy rules preclude external models, and existing open-source VLMs that clear quality thresholds cost more to serve than human annotation. We present a deployed document-understanding system built on a Mixture-of-Experts VLM (35B total, 3B active), fine-tuned on in-house production data mixed with open-domain documents cu...
  </details>

- **2026-09-01** — Stefania Bellavia, Greta Malaspina, Benedetta Morini — [DOFFO_TR: a Decentralized Objective Function-Free Optimization method with Trust-Region](http://arxiv.org/abs/2609.00878v1)
  <details><summary>📄 Abstract</summary>
  In this paper, we propose a novel objective function-free trust-region method designed to solve optimization problems over decentralized networks. Unlike traditional approaches that often rely on stepsize tuning, our framework employs a function-free trust-region procedure that enables adaptive selection of the step length. Our approach accommodates first- and second-order models and eliminates the need to share local function values and gradients among agents, thereby enhancing privacy and comp...
  </details>

- **2026-09-01** — Zinco J, Xunjie Zhu, Shen Huang et al. — [MemoryWalker: Stop Training Agents on Contexts They Never Saw](http://arxiv.org/abs/2609.00865v1)
  <details><summary>📄 Abstract</summary>
  Production agent harnesses such as Claude Code and Qwen-Agent compress context during rollout, but training under compression creates a conditioning problem: every eviction branches the effective history, so the learning object is a tree rather than a sequence. Existing linearizations either retain the rightmost path, causing time-travel leakage, or replay a depth-first traversal, causing train-inference mismatch. We introduce two exact, gradient-equivalent corrections: LogitTree, a segmented K-...
  </details>

- **2026-09-01** — Lei Wang, Jieming Bian, Letian Zhang et al. — [Breaking the Structural Identity: Personalized Federated LoRA Fine-tuning under Rank Heterogeneity](http://arxiv.org/abs/2609.00632v1)
  <details><summary>📄 Abstract</summary>
  Large Language Models (LLMs) have achieved remarkable success across diverse domains, but their adaptation to privacy-sensitive, distributed datasets remains a challenge. While Federated Learning (FL) combined with Low-Rank Adaptation (LoRA) provides a resource-efficient paradigm for collaborative fine-tuning, practical deployments are hindered by the dual challenges of resource heterogeneity and data heterogeneity. Existing rank-heterogeneous methods primarily focus on bridging dimension mismat...
  </details>

- **2026-08-31** — Saad Mohammad Abrar, Eesha Kurella, Arnav Dadarya et al. — [Do LLMs Know Your Neighborhood? Auditing LLM Priors for Neighborhood-Level Mobility Prediction and Structural Alignment](http://arxiv.org/abs/2609.00345v1)
  <details><summary>📄 Abstract</summary>
  Human mobility is central to urban planning, transportation, public health, and emergency response, yet fine-grained trajectory data are often proprietary, restricted, and privacy-sensitive. Large language models (LLMs) offer a potential alternative by generating plausible mobility traces and predicting individual movement, but their ability to infer aggregate neighborhood-level mobility remains unclear. We evaluate zero-shot LLMs on Census Block Group-level mobility prediction across four U.S. ...
  </details>

- **2026-08-31** — Krithika Ramesh, Krishna Pillutla, Danish Pruthi et al. — [The Privacy-Hallucination Tradeoff in Differentially Private Language Models](http://arxiv.org/abs/2609.00492v1)
  <details><summary>📄 Abstract</summary>
  Both privacy and factual accuracy are paramount in high-stakes domains like healthcare. Concerningly, we uncover and investigate a privacy-hallucination tradeoff in differentially private (DP) language models. First, we empirically show that models pre-trained or fine-tuned with DP tend to produce more hallucinations than non-DP counterparts, with increased severity as the privacy budget grows stricter. Second, we investigate model properties driving this tradeoff, demonstrating that DP mechanis...
  </details>

- **2026-08-31** — Muran Yu, Jiechao Gao, Yuandong Pan et al. — [EGT-KG: Evidence-Grounded Typed KG Retrieval for Practical Scientific QA with Small Language Models](http://arxiv.org/abs/2609.00479v1)
  <details><summary>📄 Abstract</summary>
  For emerging scientific research domains, local Small Language Models (SLMs) are becoming more attractive, as they offer stronger privacy control and more stable deployment pipelines than Large Language Models. However, in practice, scientific question-answering on SLMs often operates under inevitable constraints: small literature collections, fragmented evidence, limited context window and reasoning abilities. We propose the Evidence-Grounded Typed Knowledge Graph (EGT-KG), a retrieval framewor...
  </details>

- **2026-08-31** — Zihang Liang, Haochen Zhang, Lingzhou Xue — [Provably Efficient Federated Reinforcement Learning with Linear Function Approximation and Logarithmic Communication Cost](http://arxiv.org/abs/2609.00193v1)
  <details><summary>📄 Abstract</summary>
  We study federated online reinforcement learning with linear function approximation. While recent multi-agent reinforcement learning algorithms achieve strong regret guarantees, they typically require sharing raw trajectories. This reliance incurs a communication cost that scales linearly with the number of episodes and violates the privacy constraints of federated settings. To address these limitations, we propose Fed-LSVI, the first provably efficient federated algorithm for online reinforceme...
  </details>

- **2026-08-31** — Linhai Ma, Rita El Hachem, Mahatab El Hajj et al. — [Assessing Suicide Risk in Arabic Crisis Helpline Calls: A Comparison of Arabic and English Large Language Models](http://arxiv.org/abs/2609.00191v1)
  <details><summary>📄 Abstract</summary>
  Crisis helplines assess suicide risk through structured interviews, a process that is slow and dependent on operator training and workload. Natural language processing could support risk assessment and call prioritization, but almost no work addresses Arabic-language helpline calls or operates within the privacy constraints of real helpline data. We analysed de-identified transcripts from Lebanon's National Lifeline for Emotional Support and Suicide Prevention. Audio never left the helpline: cal...
  </details>

- **2026-08-31** — Yung Wei Shueh, Zhi-Jie Chen, Chia-Hsuan Hsu et al. — [DIASENTINEL: An Auditable Multi-Agent System for Guideline-Grounded Diabetes Risk Screening](http://arxiv.org/abs/2608.31128v1)
  <details><summary>📄 Abstract</summary>
  Large language models (LLMs) offer promising clinical decision support but remain vulnerable to hallucinated facts, unsupported recommendations, and citation errors. We present DIASENTINEL, a fully on-premise multi-agent system for one-year type 2 diabetes mellitus (T2DM) risk screening and guideline-grounded report generation from electronic health records (EHRs). The system integrates calibrated risk prediction, deterministic clinical signal extraction, Reciprocal Rank Fusion over American Dia...
  </details>

- **2026-08-31** — Yuhan Wang, Zhengxi Lu, Yuchen Yan et al. — [PaperGym: Rubric-Centered Evolution for Research-Plan Generation](http://arxiv.org/abs/2608.31119v1)
  <details><summary>📄 Abstract</summary>
  Research planning is the decisive capability of AI scientists. Yet a research plan admits no verifiable answer, so reinforcement learning lacks the environment it requires: tasks paired with a critic. Rubrics extracted from scientific papers can supply the critic. Existing pipelines, however, draw the question and the criteria from the same content, so the reward can be earned by paraphrase. The rubric is further compressed into a single scalar per rollout. We introduce PaperGym, a unified frame...
  </details>

- **2026-08-31** — Rui-Qing Sun, Chen-Hao Cui, Hui-Yang Zhao et al. — [Audio-Driven Adversarial Defense for 3D Talking Face Generation with totally Visual Fidelity Preservation](http://arxiv.org/abs/2608.30951v1)
  <details><summary>📄 Abstract</summary>
  The rapid development of generative portrait models has raised growing concerns about privacy leakage and identity misuse. In particular, audio-driven 3D talking face generation can reconstruct a reusable 3D portrait of a target person from a monocular video and animate it with arbitrary speech, making realistic identity impersonation alarmingly practical. Existing proactive defenses mainly operate in the visual domain by injecting subtle perturbations into acial regions to disrupt identity acqu...
  </details>

- **2026-08-31** — Dishu Yang, Jingjing Liu, Jize Li — [Balancing Privacy, Utility, and Safety in LLM Alignment through Preference Optimization](http://arxiv.org/abs/2608.30141v1)
  <details><summary>📄 Abstract</summary>
  Preference optimization is widely used to align large language models with human preferences, but preference-data composition may also influence privacy-relevant memorization. We examine whether adding synthetic privacy-preference pairs to Direct Preference Optimization (DPO) is associated with lower canary-based memorization signals without modifying the objective or introducing a formal privacy mechanism. We propose Privacy-Pressure Preference Mixing (P3M), a data-composition protocol that var...
  </details>

- **2026-08-31** — Jimmy Gammell, Kaushik Roy — [A Simple Transformer Pipeline for Full-Key Side-Channel Attacks on Uncropped Datasets](http://arxiv.org/abs/2608.30105v1)
  <details><summary>📄 Abstract</summary>
  Deep learning-based side-channel analysis has historically focused on single-byte targets and manually cropped traces, which risks discarding exploitable leakage. While recent work has proposed specialized architectures and resampling techniques to address this gap, the literature lacks a simple transformer baseline for simultaneous full-key attacks on uncropped traces. We present an open-source transformer implementation for uncropped full-key attacks which uses the standard transformer encoder...
  </details>


### 📂 steganography
*隐写与隐蔽通信 / Steganography & Covert Communication* — 1 papers

- **2026-08-31** — Minkyung Cho, Jihyo Kim, SeungWoo Song et al. — [Hidden Threat in Synthetic Data: Covert Targeted Bias Injection through Benign Text](http://arxiv.org/abs/2608.30619v1)
  <details><summary>📄 Abstract</summary>
  Synthetic data is increasingly used to train large language models (LLMs), yet its security implications remain poorly understood. Prior work on subliminal learning suggests that models can inherit behavioral traits from seemingly unrelated training data. In this work, we investigate whether such mechanisms can be exploited to inject targeted social biases into aligned models through semantically benign synthetic data. We construct a pipeline in which a misaligned teacher model generates filtere...
  </details>


### 📂 misuse
*滥用与误用 / Misuse & Abuse* — 19 papers

- **2026-09-02** — Da Cheng Gu, Yifei Dong, Xinghao Yang et al. — [ASCII Attack: Recontextualising Harmful Requests as Artistic Critique in Large Language Models](http://arxiv.org/abs/2609.02215v1)
  <details><summary>📄 Abstract</summary>
  Safety alignment trains large language models to refuse harmful requests stated plainly, but that training is applied mostly to surface form. Requests that only recontextualise the same operational content, changing how the model reads it, are therefore only weakly covered. The ASCII Attack is one such recontextualisation. It is single-turn and black-box: one message, with no access to model internals. It embeds a fully legible harmful request in ASCIl-art characters, presents it as artwork, and...
  </details>

- **2026-09-02** — Qinghua Mao, Wanying Qu, Dadi Guo et al. — [SafeEvolve: Harness-Policy Co-Evolution from Agent Experience for Safety Alignment](http://arxiv.org/abs/2609.02786v1)
  <details><summary>📄 Abstract</summary>
  The performance of LLM-based agents is jointly shaped by the base model and the harness used when interacting with the environment. This exposes them to safety risks in both harmful final responses and multi-step execution trajectories. Existing safety alignment mechanisms often rely on either external harness updates or policy optimization, yet applying either paradigm in isolation fails to bridge runtime control with intrinsic safety. We propose SafeEvolve, an experience-driven self-evolving f...
  </details>

- **2026-09-02** — Zhengyi Jin, Ru Zhang, Xiao Chen et al. — [FUSE: An Evaluating Framework for Dangerous Capabilities of LLMs](http://arxiv.org/abs/2609.02168v1)
  <details><summary>📄 Abstract</summary>
  Fragmented safety evaluation undermines the governance of dangerous AI capabilities. We present a modular framework that evaluates each model through three orthogonal pipelines---Knowledge ($K$), Defense ($D$), and Harm ($H$)---under a unified protocol, aggregating results into a standardized dangerous-capability profile $φ$. Pluggable modules supply scenario seeds, knowledge banks, hazard queries, and judge rubrics, while the core evaluation engine remains unchanged across domains; the CB evalu...
  </details>

- **2026-09-02** — Tianqi Xiao, Shiyao Cui, Minghao Zhang et al. — [Transfer Safety Awareness for Cross-Modal Safety Drift in Multimodal Large Language Models](http://arxiv.org/abs/2609.02082v1)
  <details><summary>📄 Abstract</summary>
  Visual modality enhances the capabilities of multimodal large language models (MLLMs) but also introduces a safety concern: a benign textual query may convey harmful intent when grounded in a visual image. We term this cross-modal safety drift and our pilot studies show that the safety response rate for such requests is substantially lower than that for requests containing explicitly unsafe text. This paper aims to systematically study this issue. First, we conduct an empirical analysis to ident...
  </details>

- **2026-09-02** — Chenyu Zhou, Qiliang Jiang, Shuning Wu et al. — [Coverage, Not Targeting: A Structural Regime in Multi-Turn Agent Credit Assignment](http://arxiv.org/abs/2609.02417v1)
  <details><summary>📄 Abstract</summary>
  Multi-turn agentic RL increasingly treats credit assignment as a targeting problem: given a terminal verifiable reward, per-turn methods localize credit onto the turns that mattered. We identify the structural quantity that predicts when this is the right move, the verifier information density V_d = k/C (the fraction of an agent's C-step causal chain whose per-turn correctness the verifier exposes), and show that terminal-state verifiers sit deep in a low-V_d regime where targeting is the wrong ...
  </details>

- **2026-09-01** — Sejuti Basu, Ashima Sood, Vijay Kumar et al. — [Swin Meets EfficientNet: Lightweight Architectures for GAN-Based Face Forensics](http://arxiv.org/abs/2609.01749v1)
  <details><summary>📄 Abstract</summary>
  Modern generative models, such as GANs, diffusion architectures, and autoregressive systems, now produce facial images that are nearly indistinguishable from authentic photographs. This capability makes detecting forged images increasingly difficult, raising serious concerns about identity theft, fraud, and misinformation campaigns. Our research focuses specifically on GAN-generated synthetic faces, which underpin many face-centric deepfakes, and investigates efficient detection approaches using...
  </details>

- **2026-09-01** — Rui Yang, Shuang Huang, Junhua Liu et al. — [Who Judges the Judges? A Chinese Safety QA Benchmark for Evaluating LLM Responses and Safety Judges](http://arxiv.org/abs/2609.01210v1)
  <details><summary>📄 Abstract</summary>
  Safety benchmarks for large language models often assess the risk of a user query, although the outcome of question answering depends on whether the response violates a policy. This distinction is critical in Chinese harmful-content evaluation, where linguistic variation and adversarial transformations can obscure risky intent. We introduce C-SafeQA, a policy-grounded benchmark for response-level Chinese safety evaluation. It comprises 538 base queries and 8,877 adversarial queries answered by f...
  </details>

- **2026-09-01** — Jainil Dharmil Shah — [Triple-Bottom-Line Sustainability of Language Models for Edge AI: A Comparison Between SLMs and Quantized LLMs](http://arxiv.org/abs/2609.00665v1)
  <details><summary>📄 Abstract</summary>
  Edge-AI model selection is commonly driven by one isolated metric - accuracy, latency, memory, energy, or safety, even though a deployable language model must balance all five. Our work focuses on answering the question whether na- tively trained small language models (SLMs) or large language models (LLMs) compressed through post-training quantization offer the more sustainable edge- deployment trade-off. We introduce a reproducible Holistic Sustainability Score (HSS) organized around the triple...
  </details>

- **2026-09-01** — Rui Yang, Yang Hong, Yichao Xu et al. — [Same Request, Different Boundary: Evaluating Cybersecurity Assistance across Conversational Contexts](http://arxiv.org/abs/2609.00578v1)
  <details><summary>📄 Abstract</summary>
  Large Language Models (LLMs) can solve complex problems, but their misuse in high-risk domains can lead to severe consequences. Model providers therefore restrict assistance for potentially harmful requests. Refusing all cybersecurity requests would therefore harm legitimate users. Providers need a mechanism to block malicious use without denying legitimate assistance to defenders. Existing cybersecurity-specific datasets evaluate this mechanism, but none considers the conversational context of ...
  </details>

- **2026-09-01** — Pingyu Wu, Weiming Zhang, Nenghai Yu — [The Safeguard Worked. Is the LLM System Safer?](http://arxiv.org/abs/2609.00519v1)
  <details><summary>📄 Abstract</summary>
  Safeguards in deployed LLM services are evaluated by refusal, attack success, and policy violation rates. Those rates characterize how a control performed on the requests it was tested on. A deployment has to answer a different question: how much help with harmful tasks the service still gives an attacker who keeps adapting or finds another way in. We determine what each reported result implies for that question, allowing results from different safeguard families to be compared under one deploym...
  </details>

- **2026-09-01** — Wenhan Chang, Tianqing Zhu, Ping Xiong et al. — [RISA: Response Inspection and Selective Actions for Refusal Calibration in Large Language Models](http://arxiv.org/abs/2609.00790v1)
  <details><summary>📄 Abstract</summary>
  Reliable refusal behavior requires Large Language Models (LLMs) to reject harmful prompts with only answering benign ones. Incorrect refusal behavior can either expose users to harmful responses or prevent users from obtaining useful answers. Training-time alignment improves refusal behavior by updating model parameters with safety data, but requires additional computation and training. In contrast, inference-time alignment aims to modify LLM behavior during inference without updating the underl...
  </details>

- **2026-08-31** — Guoli Wang, Haonan Shi, Tu Ouyang et al. — [Beyond Token Positions: Safety Alignment Across Denoising Steps in Diffusion Language Models](http://arxiv.org/abs/2609.00495v1)
  <details><summary>📄 Abstract</summary>
  Diffusion large language models (dLLMs) generate text through iterative denoising rather than left-to-right decoding. This generation paradigm introduces two axes that can influence safety alignment: when tokens are generated during denoising and where they appear in the response. In this paper, we measure dLLM safety behavior under harmful prompts by tracing intermediate token distributions and commitment decisions throughout denoising. Our analysis shows that refusal signals are concentrated i...
  </details>

- **2026-08-31** — Feitong Qiao, Liren Peng, Shiming Ren et al. — [EvoFlint: An Evolutionary Atlas of Multi-Turn LLM Vulnerabilities](http://arxiv.org/abs/2609.00487v1)
  <details><summary>📄 Abstract</summary>
  Frontier language models that refuse harmful single-turn prompts often comply when the same intent is reached gradually over many turns, making multi-turn attacks one of the least understood failure modes of large language models. Most automated red-teaming methods treat this as a generation problem: produce attacks that break the model. We argue it is better framed as a search problem: discover, organize, and iteratively refine a diverse archive of attack strategies, producing a structured map ...
  </details>

- **2026-08-31** — Ruotong Wang, Zihao Zhu, Siwei Lyu et al. — [Distributed Implicit Harm: A Compositional Safety Blind Spot in MLLM-Based Video Moderation](http://arxiv.org/abs/2609.00206v1)
  <details><summary>📄 Abstract</summary>
  Despite their growing use in video moderation, multimodal large language models (MLLMs) exhibit a compositional safety blind spot: videos composed of seemingly benign components can convey harmful meaning when interpreted as a whole. We refer to this phenomenon as Distributed Implicit Harm (DIH), where harm arises from relations among components distributed along a decomposition axis of the video, rather than from any single explicit cue. Among many possible axes, we study two representative cas...
  </details>

- **2026-08-31** — Xiaoyu Guo, Pengcheng Chen, Jiong Yu et al. — [Graph Evidence Is Not Enough: Diagnosing Native Decoder Use in Graph-Augmented LLMs](http://arxiv.org/abs/2608.30437v2)
  <details><summary>📄 Abstract</summary>
  Graph-augmented large language models often assume that graph evidence produced by external computation and placed in the input can be used by the native decoder. We test this assumption with HopQA, a deliberately bounded diagnostic that asks for the shortest-hop distance between two query nodes. Because the answer is a small integer and the target is purely topological, failure cannot be dismissed as open-ended generation or ambiguous evaluation. Yet existing graph-augmented baselines still fai...
  </details>

- **2026-08-31** — Hossein Arshadi Soufiani, Henry M. Kim, Hjalmar Turesson et al. — [Detoxifying Toxic Communication: A Design Science Approach to Responsible AI](http://arxiv.org/abs/2609.00361v1)
  <details><summary>📄 Abstract</summary>
  Toxic language in digital workplaces such as pejoratives, sarcasm, condescension, and subtle incivility can erode trust, morale, and collaboration. Existing moderation tools primarily delete or block harmful messages, disrupting communication and offering no constructive resolution. This study adopts a Design Science Research approach to create a responsible AI artifact that detects and detoxifies toxic communication. The artifact integrates fine-tuned transformer-based classifiers (DistilBERT, ...
  </details>

- **2026-08-31** — Doyun Kim, Chanwoo Kim, Sugyeong Eo et al. — [EvoSkill Injection: Red-Teaming Autonomous Skill Generation and Evolution in Self-Evolving Agents](http://arxiv.org/abs/2608.30429v1)
  <details><summary>📄 Abstract</summary>
  LLM-based agent systems increasingly adopt skill-based architectures to reduce repetitive reasoning costs and improve stable, efficient task execution. Recent studies propose self-evolving agents that autonomously generate, refine, and reuse skills from past experiences to enable continuous capability evolution. However, autonomous skill evolution introduces a new attack surface in which malicious capabilities are generated, stored, and reused as legitimate skills. In this paper, we define EvoSk...
  </details>

- **2026-08-31** — Camila Blank, Zhuofan Ying, Christopher Potts et al. — [Sycophantic Agreement Transfers with Neutral Data via Contrastive Preference Optimization](http://arxiv.org/abs/2608.31079v1)
  <details><summary>📄 Abstract</summary>
  Sycophantic agreement refers to a behavior in which language models excessively affirm the user, often at the cost of factual accuracy. Although sycophantic agreement is a well-known failure of model alignment, there is limited understanding of how it emerges from model training. In this work, we demonstrate that sycophantic agreement can emerge as an unintended consequence of widely used contrastive preference optimization objectives. Using the OLMo 3 post-training pipeline, we show that, for v...
  </details>

- **2026-08-31** — Ruoxuan Li, Pinqiao Wang, Sheng Li et al. — [You Shouldn't Have Asked: A Pragmatics-Inspired Taxonomy for Evaluating LLM Refusals](http://arxiv.org/abs/2608.30856v1)
  <details><summary>📄 Abstract</summary>
  Refusals are often treated as face-threatening acts in pragmatics because they can challenge the requester's socially claimed self-image. Large language models (LLMs) are increasingly trained to refuse unsafe and inappropriate requests, and these refusals may harm users when models fail to manage this interactional cost properly. While existing work has mainly approached LLM non-compliance as a safety-alignment outcome, it does not provide a way to evaluate whether LLMs refuse appropriately acro...
  </details>


### 📂 vulnerability
*漏洞与攻击面 / Vulnerabilities & Attack Surfaces* — 59 papers

- **2026-09-02** — James Mickens — [The Implications of Linguistic Illegibility for LLM Security](http://arxiv.org/abs/2609.02852v1)
  <details><summary>📄 Abstract</summary>
  LLMs are trained to generate natural language. However, various strands of evidence indicate that an LLM's externalized linguistic outputs and mechanistically-extracted linguistic features can be an unreliable lens for understanding internal model computation. We introduce the term ``linguistic illegibility'' to broadly refer to scenarios in which an LLM's externalized or mechanistically-probed language artifacts fail to represent how the model actually thinks. We argue that the specter of lingu...
  </details>

- **2026-09-02** — Pengfei Wang, Anying Chen, Danjun Liu et al. — [PrimSynth: An Agentic Approach to Discover, Validate, and Synthesize Exploit Primitives for Linux Kernel Vulnerabilities](http://arxiv.org/abs/2609.02647v1)
  <details><summary>📄 Abstract</summary>
  Linux kernel vulnerabilities are critical to downstream systems. Despite extensive research on automated kernel exploitation, a fundamental challenge remains the conceptual gap between abstract exploit strategies and concrete technical operations. To fill this gap, this paper introduces a systematic characterization that formalizes six classes of exploit primitives from logical capability to validatable effect. Then, an extended exploit strategy representation is proposed, which couples primitiv...
  </details>

- **2026-09-02** — Taehyeon Kim, Eunhyeok Park — [TaRA: Training-Aware Low-Rank Adaptation Initialization](http://arxiv.org/abs/2609.02639v1)
  <details><summary>📄 Abstract</summary>
  Low-Rank Adaptation (LoRA) has become a de facto standard for parameter-efficient fine-tuning (PEFT), yet its performance is highly sensitive to initialization due to the information bottleneck imposed by low-rank decomposition. Existing approaches attempt to construct high-quality LoRA initializations by exploiting principal components of pretrained weights, activations, or gradients. However, these methods do not directly account for the training dynamics of the full-rank model. In this paper,...
  </details>

- **2026-09-02** — Luca Migliaccio, Roberto Natella, Naghmeh Ivaki et al. — [Automated Vulnerability Injection in Smart Contracts Using Large Language Models](http://arxiv.org/abs/2609.02624v1)
  <details><summary>📄 Abstract</summary>
  Assessing vulnerability detection tools for smart contracts requires datasets with known ground truth, yet such datasets are scarce and difficult to build by hand. We propose an approach that uses Large Language Models (LLMs) to automatically inject vulnerabilities into Solidity smart contracts, and demonstrate it in a case study targeting 49 vulnerability types from OpenSCV. Injected contracts are validated through a multi-step pipeline checking compilation, execution, business logic, and the p...
  </details>

- **2026-09-02** — Eric Olsson, Benjamin Eriksson, Adam Doupé et al. — [SpiderSapien: Client-Centric Web Crawler and Security Scanner](http://arxiv.org/abs/2609.02532v1)
  <details><summary>📄 Abstract</summary>
  Black-box web application crawling and scanning play an important role for security testing of web applications. Yet state-of-the-art scanners fall short of addressing key characteristics of a modern web application: its extreme dynamism and interactivity on the client side. This paper identifies immersive interaction as a key ingredient for scanners to deeply explore modern web applications. We propose SpiderSapien, a client-centric crawler and security scanner. SpiderSapien incorporates a uniq...
  </details>

- **2026-09-02** — Viacheslav Yusupov, Daria Cherniuk, Evgeny Frolov — [Scalable Kronecker-Fisher Approximation: Efficient Hessian Analysis for Billion-Parameter Language Models Compression](http://arxiv.org/abs/2609.02451v1)
  <details><summary>📄 Abstract</summary>
  In this paper, we propose a scalable Kronecker-based approximation that captures cross-layer interactions without storing the entire Fisher matrix, enabling practical Hessian analysis for billion-parameter networks where full computation is infeasible. Our approach reveals consistent vulnerability patterns: value projection layers exhibit the highest sensitivity and strongest cross-layer correlations across multiple model families, while other components exhibit architecture-specific behaviors. ...
  </details>

- **2026-09-02** — Zhenyu Liang, Beichen Huang, Bowen Zheng et al. — [Semantics-Guided Automatic Tensorization for Multiobjective Evolutionary Algorithms: A Multi-Agent Framework](http://arxiv.org/abs/2609.02387v1)
  <details><summary>📄 Abstract</summary>
  Multiobjective evolutionary algorithms (MOEAs) naturally expose population-level parallelism, but many mature implementations encode their computation in sequential program structures designed for central processing units. Exploiting modern tensor computing platforms therefore requires more than direct code translation: the implementation must be restructured without changing the defining optimization mechanism of the underlying MOEA. We formulate automatic tensorization for MOEAs as semantics-g...
  </details>

- **2026-09-02** — Mehran Rahnamania, Michel Mandjes, Farid Ashtiani — [Analysis of Triggered Packet Streams: A Matrix-Analytic Method for Exponential Triggering Delays](http://arxiv.org/abs/2609.02320v1)
  <details><summary>📄 Abstract</summary>
  In many communication networks, the transmission of a packet may automatically trigger the transmission of a subsequent packet from the same source after a (possibly random) delay, without requiring acknowledgment or feedback. Such behavior arises in multi-stage status updating, proactive protocols, and other applications where users generate causally dependent packet streams. In this paper, in order to analyze these systems, we introduce the $\mathrm{M^T/G/1}$ queue. In this model, primary cust...
  </details>

- **2026-09-02** — Kaixiang Lu, Haiyu Lan, Chunxiao Qiao et al. — [Contact-Constrained Lower-Limb Joint-Offset Calibration for Humanoid Robots](http://arxiv.org/abs/2609.02306v1)
  <details><summary>📄 Abstract</summary>
  Accurate joint encoder offsets are essential for kinematic consistency in humanoid lower limbs, yet existing calibration methods typically require external motion-capture systems or fiducial targets. We present a self-contained calibration framework exploiting only onboard joint encoders and a pelvis-mounted IMU during static double-support contact. The inter-foot transform from forward kinematics must stay constant when both feet are fixed; minimizing its posture-dependent dispersion yields a n...
  </details>

- **2026-09-02** — Fang He, Wang-chien Lee — [SMart: A Multi-source Multi-phase Time Series Representation Transfer Framework](http://arxiv.org/abs/2609.02203v1)
  <details><summary>📄 Abstract</summary>
  Time series representation learning (TSRL) has attracted growing research interests in recent years. Two recent explorations in TSRL are: i) exploiting a transformer-based framework to learn time series; ii) instead of using only the targeted dataset, borrowing time series from other datasets to to facilitate representation transfer. While these two explorations are shown effective, the self-supervised time series recovery task in (i) and the single-source dataset used in (ii) are technically si...
  </details>

- **2026-09-02** — Benjamin C Liu, Dillon Mehta, Rishi Malhotra et al. — [Examining the Vulnerability of Multi-Agent Medical Systems to Human Interventions for Clinical Reasoning](http://arxiv.org/abs/2609.02191v1)
  <details><summary>📄 Abstract</summary>
  Human interventions at fault points can alter the diagnostic accuracy of multi-agent medical systems. We defined fault points as moments in AI agent conversations, in which an agent's reasoning became most vulnerable to external influence. Using the MedQA dataset, this study analyzed simulated doctor-patient conversations to measure how interventions shifted reasoning and accuracy. Correct intervention methods showed an improvement in baseline diagnostic accuracy of up to 40%, while incorrect or...
  </details>

- **2026-09-02** — Vinicius Atsushi Sato Kawai, Gustavo Rosseto Leticio, Lucas Pascotti Valem et al. — [Aggregating Neighbor Embedding Projection and Rank-Based Manifold Learning for Image Retrieval](http://arxiv.org/abs/2609.01963v1)
  <details><summary>📄 Abstract</summary>
  Content-based image retrieval (CBIR) has advanced significantly with deep learning, yet effectively ranking similar images remains challenging, particularly in high-dimensional feature spaces, where pairwise distances often fail to capture contextual relationships and the semantic gap between visual features and high-level concepts persists. Manifold learning and rank-based refinement methods have emerged as complementary strategies, respectively improving feature representations and exploiting ...
  </details>

- **2026-09-01** — Martina Torsello, Marcella Massardi, Elisabetta Liuzzo et al. — [The ViSta method for optimized stacking of broadband interferometric data in the Fourier domain](http://arxiv.org/abs/2609.01897v1)
  <details><summary>📄 Abstract</summary>
  We present the optimized version of ViSta, a visibility-domain stacking method that combines interferometric observations in the Fourier domain from radio to sub-millimeter wavelengths. By stacking visibilities directly and transforming them into the rest frame, ViSta enhances the signal, suppresses noise, and improves image reconstruction through extended uv-coverage. ViSta outperforms image stacking when individual sources are too faint to detect, achieving higher SNR in the low-signal and ext...
  </details>

- **2026-09-01** — Henry Arthur — [Thinking effort aligns between humans and reasoning models in abductive reasoning](http://arxiv.org/abs/2609.01867v1)
  <details><summary>📄 Abstract</summary>
  A major question in cognitive modeling concerns the behavioral alignment between large language models and humans across linguistic and non-linguistic tasks. Unlike standard LLMs, large reasoning models (LRMs) are optimized with reinforcement learning from verifiable rewards, encouraging correct solutions to reasoning tasks rather than preference-aligned responses. Recent work (de Varda et al., 2025) investigates the cost of thinking in humans and LRMs by comparing human reaction times with mode...
  </details>

- **2026-09-01** — Osvaldo M Velarde, Lucas C Parra, Alireza Hashemi et al. — [Emergence of Fibrations, Compression, and Symmetry Breaking in Artificial Neural Networks](http://arxiv.org/abs/2609.01768v1)
  <details><summary>📄 Abstract</summary>
  Artificial neural networks are often regarded as powerful yet opaque black boxes. Here, we demonstrate that learning in deep neural networks generates local symmetries known in graph theory as fibrations and coverings. We prove that covering symmetries are stable attractors of stochastic gradient descent. Consistent with this theory, we report the emergence of covering symmetries across major network architectures, including multilayer, convolutional, recurrent, and transformer networks. Exploit...
  </details>

- **2026-09-01** — Enna Basic, Alberto Giaretta — [Towards Behavior Tree-Guided Vulnerability Detection with Lightweight LLMs](http://arxiv.org/abs/2609.01758v1)
  <details><summary>📄 Abstract</summary>
  Large Language Models (LLMs) are increasingly used for software vulnerability detection, but their performance depends on how source code is represented in the input. Most prompting approaches use source code in its original form, while some works propose the use of structured representations. Abstract Syntax Trees (ASTs) are one of the most popular approaches, but AST verbosity increases input size relative to source code, making them hard to fit within some LLMs context windows. This paper inv...
  </details>

- **2026-09-01** — Shuaicheng Niu, Guohao Chen, Yaofo Chen et al. — [A Survey on Self-Improving Test-Time Intelligence: Feedback-Driven Adapting, Learning, and Scaling at Inference](http://arxiv.org/abs/2609.01679v1)
  <details><summary>📄 Abstract</summary>
  The ability of AI systems to improve their behavior during deployment is becoming increasingly important. As inference moves beyond the static execution of a fixed trained model, a growing body of work studies how models can refine their behavior on the fly by exploiting test-time information and additional computation. These developments have largely evolved along two directions: methods that modify the model's state using test-time signals, and methods that improve predictions through extra in...
  </details>

- **2026-09-01** — Jincheng Zhang, Chen Huang, Wenqiang Lei et al. — [Towards Effective Structured Context Modeling for Conversational Recommender Systems via Dual-node Monte Carlo Tree Search](http://arxiv.org/abs/2609.00618v2)
  <details><summary>📄 Abstract</summary>
  We investigate the role of conversational context modeling in user preference tracking for Conversational Recommendation Systems (CRSs). In this regard, we propose DREAMS, a novel tree-structured context modeling framework that explicitly captures user preference evolution throughout multi-turn interactions. DREAMS introduces two specialized node types to support the two fundamental objectives of CRSs: preference elicitation and preference exploitation. Specifically, elicitation nodes leverage M...
  </details>

- **2026-09-01** — Marven Sherif, Amgad Elmasry, Youssef Ghazal et al. — [BS: Take the Hint - Interactive Multitracer PET/CT Lesion Segmentation with a Scribble-Conditioned ResEnc U-Net](http://arxiv.org/abs/2609.01554v1)
  <details><summary>📄 Abstract</summary>
  Automated lesion segmentation in whole-body PET/CT is complicated by the variety of physiological tracer uptake patterns and by the differing appearance of lesions across tracers. The autoPET/CT V challenge addresses this by making segmentation interactive: user scribbles marking foreground and background are supplied alongside the image, and the algorithm is expected to exploit them. We present our submission, a scribble-conditioned residual encoder U-Net operating on four input channels: CT, P...
  </details>

- **2026-09-01** — Tomáš Holeček, Viliam Lisý — [NashDreamer: Model-Based Reinforcement Learning for Zero-Sum Imperfect-Information Games](http://arxiv.org/abs/2609.01549v1)
  <details><summary>📄 Abstract</summary>
  Model-based reinforcement learning (MBRL) has achieved remarkable results in single-agent domains, yet its extension to competitive imperfect information games (IIGs) remains underexplored. In multi-agent settings, opponent-induced non-stationarity complicates the learning process, and decentralized model learning faces severe identifiability barriers, which we argue make centralized model learning a mathematical necessity. Building on this analysis, we propose NashDreamer, a principled MBRL fra...
  </details>

- **2026-09-01** — Stephanie Fong, Yiwen Jiang, Zimu Wang et al. — [SDARE-Bench: Evaluating Large Language Models on Conversational Stigma Detection and Response in Dyadic and Group Dialogue](http://arxiv.org/abs/2609.01548v1)
  <details><summary>📄 Abstract</summary>
  Large Language Models (LLMs) are increasingly used in advice seeking and decision making that may affect social judgements. Despite stigma's profound effects on people and communities, benchmarks remain scarce. Existing general-domain evaluations typically rely on static prompts and fixed-format tasks, overlooking conversational contexts and audience effects in everyday communication. To address these gaps, we introduce SDARE-Bench, the first scenario-based benchmark evaluating both stigma detec...
  </details>

- **2026-09-01** — Tingting Ni, Maryam Kamgarpour — [Provably Safe Sim-to-Real Transfer](http://arxiv.org/abs/2609.01418v1)
  <details><summary>📄 Abstract</summary>
  To mitigate the sample complexity of real-world reinforcement learning (RL), a common practice is to first train a policy in a simulator, where samples are cheap, and then deploy the learned policy in the real world with the hope that it generalizes effectively. Such direct sim-to-real transfer is not guaranteed to succeed: simulator-trained policies can be suboptimal in the real world due to sim-to-real mismatch. Correcting this mismatch requires collecting data from the real system, but in man...
  </details>

- **2026-09-01** — Matheus F. Kovaleski, Luís Garrote, Cristiano Premebida et al. — [Multimodal RGB-Infrared Combination for UAV-Based Wildfire Segmentation: A Comparative Study on FLAME3](http://arxiv.org/abs/2609.01390v1)
  <details><summary>📄 Abstract</summary>
  Unmanned Aerial Vehicles (UAVs) have emerged as a promising platform for firefighting operations due to their flexibility, low operational cost, and ability to acquire high-resolution imagery in locations that may be difficult or dangerous to access using conventional methods. Recent advances in deep learning have significantly improved the capabilities of UAV-based wildfire monitoring systems. The present work investigates RGB-infrared fusion for binary wildfire segmentation on the FLAME3 datas...
  </details>

- **2026-09-01** — Jidong Yang, Qi Li, Wei Zong et al. — [One Prompt Is Enough: Watermark Laundering Through Foundation Image Models](http://arxiv.org/abs/2609.01249v1)
  <details><summary>📄 Abstract</summary>
  Invisible watermarks are typically evaluated against predefined perturbations such as compression, blur, noise, cropping, and denoising. Public foundation image models expose a distinct threat: an attacker can submit a watermarked image with a single reconstruction prompt and obtain a visually faithful output from which the invisible watermark can no longer be decoded reliably. We formalize this failure mode as watermark laundering and evaluate it using a joint payload-fidelity profile that comb...
  </details>

- **2026-09-01** — Jie Chen, Xiangqian Yu, Yanchao Lian et al. — [From Language to Behavior: Scaling Sequence Transformers for Industrial Recommendation Ranking with Rec-Native Designs](http://arxiv.org/abs/2609.01240v1)
  <details><summary>📄 Abstract</summary>
  Scaling Transformers has driven large gains in language modeling, but transplanting this to behavior-sequence modeling in production ranking is challenging: recommendation differs in signal quality, where behavior sequences are noisy, temporally irregular, and sparsely supervised, and in computation asymmetry, where each request scores many candidates against one shared user history under tight latency budgets. We propose ReST, a recommendation-native Transformer scaling framework. For signal qu...
  </details>

- **2026-09-01** — Maciej Śmiertka, Ewelina Cybula, Oliwia Janikowska et al. — [Geometry-Controlled Magnetic and Electronic Landscapes in Anisotropic van der Waals Materials](http://arxiv.org/abs/2609.01223v1)
  <details><summary>📄 Abstract</summary>
  Electronic structure in van der Waals materials is commonly engineered through composition, strain, electrostatic gating and heterostructure assembly. Here we introduce geometronics, a concept in which substrate geometry locally reorients an anisotropic crystal, transforming homogeneous external perturbation into programmable magnetic and electronic landscapes. We demonstrate this concept using a bilayer of the antiferromagnetic semiconductor CrSBr transferred onto an inverted pyramidal nanoinde...
  </details>

- **2026-09-01** — Phong Trinh Duy, Trang Dang Yen, Hung Nguyen-Huu et al. — [Athena: Vulnerability-Affected Library Identification via Knowledge Graph Completion](http://arxiv.org/abs/2609.01187v1)
  <details><summary>📄 Abstract</summary>
  A single vulnerability in a widely used library can cascade through millions of dependent applications, yet more than half of vulnerability database entries contain missing or incorrect affected-library information. Existing automated approaches neglect the relational structure of vulnerability databases, treating identification as an isolated text retrieval problem. In this paper, we propose Athena, the first graph-based approach for vulnerability affected library identification. Athena models ...
  </details>

- **2026-09-01** — Hadjer Benkraouda, Hongyu Cai, Berkay Celik et al. — [Reveree: Diagnosing LLM Reverse-Engineering Agents](http://arxiv.org/abs/2609.01185v1)
  <details><summary>📄 Abstract</summary>
  Reverse engineering (RE) is critical to security tasks such as malware analysis and vulnerability discovery, and large language model (LLM) agents are increasingly able to perform it autonomously. Capture-the-flag (CTF) RE challenges have become the standard proxy for measuring this capability, but evaluation rests on a single criterion: whether the agent captures the flag. This solve rate reveals neither where in the RE process an agent fails nor whether a success reflects analysis of the binar...
  </details>

- **2026-09-01** — Ziyan Gan, Fangxin Liu, Chenyang Guan et al. — [PCoMoE: Shifting MoE Inference from Monolithic Expert Selection to Fine-Grained Path Composition](http://arxiv.org/abs/2609.01024v1)
  <details><summary>📄 Abstract</summary>
  Mixture-of-Experts (MoE) architectures scale Large Language Model (LLM) capacity efficiently by activating a sparse subset of experts per token. However, modern MoE inference remains heavily constrained by the rigid, whole-expert abstraction. Existing frameworks manage, schedule, or prune experts as atomic execution units, which fixes the optimization boundary too early and leaves fine-grained intra-expert computational redundancy underexplored. In this work, we present PCoMoE, a path-compositio...
  </details>

- **2026-09-01** — Baoshun Wang, Weiping Lin, Linwu Wang et al. — [Semi-Supervised Virtual Staining via Morphology Preservation and Histopathological Realism Constraints](http://arxiv.org/abs/2609.00984v1)
  <details><summary>📄 Abstract</summary>
  Virtual staining aims to computationally generate target-stained histopathological images while reducing the cost and time associated with conventional staining procedures. However, existing methods rely predominantly on strictly paired and accurately registered training data, which are difficult and expensive to obtain in routine practice. To reduce this dependence, we propose a stable semi-supervised virtual staining framework that jointly exploits both limited paired data and abundant unpaire...
  </details>

- **2026-09-01** — Peng Xu, Zuyu Zhang, Yuze Sun et al. — [ContextPipe: Database-Inspired Context Assembly for Long-Horizon Agents](http://arxiv.org/abs/2609.00749v1)
  <details><summary>📄 Abstract</summary>
  Long-horizon large language model (LLM) agents require context assembly: the runtime must decide what to include in each prompt, in what order, and when to compact history under a hard context-window budget and a byte-sensitive prompt cache. In production agentic systems, this logic is scattered across prompt builders, ad hoc compaction routines, cache-break workarounds, and per-provider shims. We argue that context assembly is structurally isomorphic to query execution in a relational database:...
  </details>

- **2026-09-01** — Hu Cao, Qianyi Yang, Xinyi Li et al. — [Efficient and Robust Absolute Pose Estimation via Gravity-Prior-Driven Transformation Decoupling and Pose Refinement](http://arxiv.org/abs/2609.00713v1)
  <details><summary>📄 Abstract</summary>
  Estimation of the absolute pose of an object is an essential task for various robotic applications. Recently, incorporating gravity direction as prior information has emerged as a popular approach to simplify absolute pose estimation. However, developing a robust and efficient algorithm to solve this challenging problem remains a difficult question due to large amounts of mismatches. In addition, obtaining an accurate pose solution from selected inlier correspondences with gravity prior is still...
  </details>

- **2026-09-01** — Kaizhen Tan, Yang Feng, Heqing Du et al. — [Teaching Vision-Language Models to Use the Scale They Are Given: Label-Free Equivariance Training for Metric Physical Reasoning](http://arxiv.org/abs/2609.00658v1)
  <details><summary>📄 Abstract</summary>
  Metric questions about video require vision-language models to use supplied real-world references to convert visual measurements into physical units. Yet we find that current models use this scale information only partially. When every world-space quantity in a prompt is rescaled by a common factor, the video remains equally valid and the correct answer changes by exactly that factor, but model predictions move only part of the way and accuracy remains concentrated near the familiar scale of the...
  </details>

- **2026-09-01** — Yuta Kato, Shintaro Ozaki, Kazuki Hayashi et al. — [ExpArt-KG: Artwork Image Description Generation through Iterative Exploration of Knowledge Graphs](http://arxiv.org/abs/2609.00629v1)
  <details><summary>📄 Abstract</summary>
  Large Vision-Language Models (LVLMs) achieve strong performance on image-grounded text generation and visual question answering. However, it remains difficult for them to comprehensively and accurately describe the factual relations among the entities and concepts associated with the objects depicted in an image. In this work, we propose a framework that efficiently exploits factual information from a knowledge graph via retrieval-augmented generation (RAG), with the goal of enabling LVLMs to ge...
  </details>

- **2026-09-01** — Jincheng Zhang, Chen Huang, Wenqiang Lei et al. — [Towards Effective Structured Context Modeling for Conversational Recommender Systems via Dual-node Monte Carlo Tree Search](http://arxiv.org/abs/2609.00618v1)
  <details><summary>📄 Abstract</summary>
  We investigate the role of conversational context modeling in user preference tracking for Conversational Recommendation Systems (CRSs). In this regard, we propose DREAMS, a novel tree-structured context modeling framework that explicitly captures user preference evolution throughout multi-turn interactions. DREAMS introduces two specialized node types to support the two fundamental objectives of CRSs: preference elicitation and preference exploitation. Specifically, elicitation nodes leverage M...
  </details>

- **2026-09-01** — Sethuraman T, Savya Khosla, Onkar Kishor Susladkar et al. — [ViTAL-X: Video-Text Alignment with Cross-Modal Temporal Edits](http://arxiv.org/abs/2609.00505v1)
  <details><summary>📄 Abstract</summary>
  Video-text models adapted from image-text architectures (e.g., CLIP) frequently exhibit temporal blindness, the inability to perceive fundamental cues like order, direction, and motion dynamics. Standard datasets mask this limitation by enabling models to exploit static spatial shortcuts. To systematically evaluate this, we introduce XTE-Bench, a diagnostic probe revealing that even large-scale video-language models struggle with basic temporal reasoning, indicating that parameter scaling alone ...
  </details>

- **2026-08-31** — MinKeon Kim, Namjun Lee, Jaekwang Kim — [PRO-Step: Step-level Process Reward Optimization for Retrieval-Augmented Generation](http://arxiv.org/abs/2609.01658v1)
  <details><summary>📄 Abstract</summary>
  Retrieval-Augmented Generation enhances Large Language Models by grounding responses in external knowledge, but multi-hop reasoning remains vulnerable to error propagation, where early retrieval failures confound subsequent steps. Standard outcome-based optimization only rewards the final answer, leaving intermediate retrieval and reasoning errors undetected. While existing process-based methods introduce step-level signals, they still score each step against the final answer, rewarding spurious...
  </details>

- **2026-08-31** — Yu Wang, Craig Erickson, Kevin Small — [Human-Anchored Factuality Evaluation with Strategic Annotation](http://arxiv.org/abs/2609.00494v1)
  <details><summary>📄 Abstract</summary>
  LLM-based factuality judges provide scalable evaluation signals, but their metrics are often systematically biased relative to human judgments. We study human-anchored factuality evaluation under limited annotation budgets, where judge predictions on the full dataset are combined with human labels on a small selectively sampled subset to obtain statistically valid estimates. The efficiency of this approach depends critically on which examples receive human annotation: in factuality evaluation, j...
  </details>

- **2026-08-31** — Xiaoyang Lu, Belthangady Akash Vi Narayana Pai, Xian-He Sun — [DynaNDE: Dynamic Near-Data Expert Scheduling for Batched MoE Inference](http://arxiv.org/abs/2609.00407v1)
  <details><summary>📄 Abstract</summary>
  Mixture-of-Experts (MoE) models enable efficient scaling of large language model (LLM) inference but suffer from substantial data-movement overhead when deployed on neural processing unit (NPU)-based systems. Near-Data Processing (NDP) provides a promising way to mitigate this bottleneck via cooperative NPU-NDP execution. However, existing NPU-NDP MoE systems do not fully account for hardware heterogeneity, dynamic expert-level concurrency, and temporal expert reuse during batched inference. Thi...
  </details>

- **2026-08-31** — Yulin Zhang, Yukun Huang, Sanxing Chen et al. — [Lazy Grounding: Attacking Search Agents with Factual Evidence](http://arxiv.org/abs/2608.30303v2)
  <details><summary>📄 Abstract</summary>
  Search agents mitigate hallucination by grounding their answers in retrieved web results. However, retrieval-based approaches also introduce an attack surface: agents may cite misinformation from poisoned search corpora containing false or malicious documents. We demonstrate that, in some cases, search agents' reasoning and responses may be steered by completely factual but distracting information. We refer to this failure as lazy grounding. We expose lazy grounding by injecting nearby evidence ...
  </details>

- **2026-08-31** — Chanhee Cho, Junhyuk Choi, Bugeun Kim — [Stride-k Subsampling: Train-Free Audio Token Reduction for Whisper](http://arxiv.org/abs/2608.30927v1)
  <details><summary>📄 Abstract</summary>
  Whisper exposes speech through a fixed 1500-token encoder interface, now a default representation for ASR decoders and Whisper-based speech language models (SpeechLMs), yet its redundancy remains largely unexamined. We propose stride-k subsampling, a deterministic indexing operation that retains every k-th token after the convolutional stem or encoder transformer. Across five Whisper scales, k=2 preserves baseline WER at both positions, with CKA attributing this stability to acoustic overlap at ...
  </details>

- **2026-08-31** — Alessio Galatolo, Meriem Beloucif — [Low-Resource Preference Adaptation of LLMs via Activation-Based Label Propagation](http://arxiv.org/abs/2608.30902v1)
  <details><summary>📄 Abstract</summary>
  Adapting large language models to user-specific preferences is often constrained by the cost of human annotation, making preference optimisation impractical in low-resource settings where preferences cannot be reliably labelled by LLMs themselves, e.g., due to cultural, subjective, or personalised contexts. In this paper, we investigate how language models encode preference information in their intermediate representations, finding that activations from chosen and rejected responses form distinc...
  </details>

- **2026-08-31** — Yanran Xu, Chuanhang Qiu, Yue Wang et al. — [GAFT: Geo-Anchored Fine-Tuning for Hazard Identification from Rare Failures](http://arxiv.org/abs/2608.30858v1)
  <details><summary>📄 Abstract</summary>
  Off-road navigation can fail when physical structures induce irrecoverable states such as high-centering or entrapment, requiring human interventions. Identifying these structures is crucial, yet challenging. Such failure events are rare and costly to collect, resulting in limited training data. Moreover, the collected data associate frames with outcomes, but do not indicate the visual cues responsible for the failure. Learning directly from these data can therefore exploit scenario-specific vis...
  </details>

- **2026-08-31** — Yunsoo Ha, Linda Nozick — [Computing Equilibria in Simulation-Based Insurance Markets with Discontinuous Demand](http://arxiv.org/abs/2608.30814v1)
  <details><summary>📄 Abstract</summary>
  We study a simulation-based equilibrium problem arising in competitive insurance markets under hurricane risk. Each insurer seeks to maximize its own profit by selecting regional pricing and reinsurance decisions while satisfying insolvency constraints. The resulting problem is particularly challenging because customer purchase decisions induce discontinuous demand functions, while insolvency constraints create nonconvex feasible regions. To address these challenges, we introduce a pricing-depen...
  </details>

- **2026-08-31** — Zhipeng Xia, Haotian Xu, Siyu Yun et al. — [TrainSDC: Characterizing and Mitigating Silent Data Corruption in Large Language Model Training](http://arxiv.org/abs/2608.30769v1)
  <details><summary>📄 Abstract</summary>
  LLM training is increasingly vulnerable to silent data corruption (SDC), yet existing protection methods largely treat Transformer computations uniformly because their vulnerability remains poorly understood. We present the first systematic characterization of SDC vulnerability across major computation interfaces in both the forward and backward passes of Transformer training. Our analysis reveals two distinct error propagation mechanisms: forward-pass vulnerability is highly location dependent,...
  </details>

- **2026-08-31** — Pradyumna Shyama Prasad, Meiri Anto, Leon Eshuijs et al. — [BAITBENCH: Measuring Agent Reward Hacking with Optional Shortcuts Planted in ML Tasks](http://arxiv.org/abs/2608.30724v1)
  <details><summary>📄 Abstract</summary>
  LLM agents are increasingly used to run autonomous ML experiments, iterating on target metrics with little human oversight. Prior work has documented reward hacking in these environments, bringing into question the validity of produced research and the broader safety case for AI R&D. Existing benchmarks do not measure exploits that live in the data or the modeling task itself. We introduce BAITBENCH, a suite of three synthetic tabular ML tasks that each contain a shortcut that allows agents to i...
  </details>

- **2026-08-31** — Zheyu Huang, Zijing Shi, Haozhe Luo et al. — [SocialReasonBench: A Video-QA Benchmark for Social Reasoning with Counterfactual Narrative Videos](http://arxiv.org/abs/2608.30716v1)
  <details><summary>📄 Abstract</summary>
  Recent advances in Large Multimodal Models (LMMs) have greatly improved video understanding, yet their ability to reason about human-centered social situations remains limited. Existing benchmarks typically rely on videos with a single observed trajectory, making it difficult to determine whether models truly understand social dynamics or merely exploit recurring narrative patterns. We introduce SocialReasonBench, a video multiple-choice QA benchmark for evaluating socially grounded reasoning in...
  </details>

- **2026-08-31** — Wei Wu, Jin Zeng, Zhen Zhang et al. — [Efficient primal--dual splitting methods for a Poisson-constrained JKO scheme for Poisson-Nernst-Planck models](http://arxiv.org/abs/2608.30693v1)
  <details><summary>📄 Abstract</summary>
  The Poisson--Nernst--Planck (PNP) equations strongly couple ionic transport and electrostatic interactions through the Poisson equation, posing substantial numerical challenges under small permittivity and complex potential boundary conditions. Underlying these equations is a natural Wasserstein gradient-flow structure, in which the Poisson equation serves as a local realization of the nonlocal electrostatic interaction energy. Exploiting this structure, we formulate each time step as a constrai...
  </details>

- **2026-08-31** — Tanise Ceron, Joachim Baumann, Elisa Bassignana et al. — [WildSEEK: Evaluating Language Models for Information-Seeking](http://arxiv.org/abs/2608.30683v1)
  <details><summary>📄 Abstract</summary>
  Language models are increasingly mediating information access to end users, urging a systematic evaluation of their responses for a fair and reliable information ecosystem. Existing evaluations, however, are often topic-specific or synthetic, limiting their ability to capture the complexity of "in the wild" information-seeking queries and the risks present in model responses. To address this gap, we introduce WildSEEK, a manually annotated dataset of 3k information-seeking queries from real user...
  </details>

- **2026-08-31** — Jiangwang Chen, Chenghao Zhang, Hengxing Cai — [MedAgent-R1: Faithfulness-Aware Reinforcement Learning for Evidence-Grounded Medical Reasoning](http://arxiv.org/abs/2608.30676v1)
  <details><summary>📄 Abstract</summary>
  When medical AI systems hallucinate clinical reasoning, the consequences extend beyond incorrect answers: fabricated justifications that superficially reference retrieved evidence can mislead clinicians into unsafe treatment decisions. Medical reasoning agents must therefore produce not only correct answers but also faithful justifications that clinicians can verify against cited evidence. We identify a systematic failure mode in RL-trained retrieval agents: outcome-only rewards improve accuracy...
  </details>

- **2026-08-31** — Yue Jiet Chong, Yimin Wang, Zhen Wu et al. — [CHIPSMORE: Compute-in-Interconnect and -Memory Chiplets for Multi-Mode Multi-Request LLM Inference Acceleration](http://arxiv.org/abs/2608.30509v1)
  <details><summary>📄 Abstract</summary>
  Large language model (LLM) inference exhibits substantial variability across adaptation modes, context lengths, and request concurrency, creating challenges for maintaining high utilization, memory efficiency, and scalable performance on compute-in-memory (CIM) accelerators. This paper presents CHIPSMORE, a multi-mode and multi-request LLM inference accelerator that integrates compute-in-interconnect and CIM to support both base-mode and low-rank adaptation (LoRA) inference under diverse workloa...
  </details>

- **2026-08-31** — Qianwen Gao, Zichang Su, Yiwen Hou et al. — [CHASE: How Content Ecosystems Are Reshaped When Ranking Is the Only Target](http://arxiv.org/abs/2608.30466v1)
  <details><summary>📄 Abstract</summary>
  Generative Engine Optimization (GEO) is increasingly used to improve content visibility in LLM-based retrieval systems, yet its population-level effects under repeated optimization remain poorly understood. We introduce Content Homogenization under rAnking Signal Exploitation (CHASE), a controlled simulation framework for studying how content ecosystems are reshaped when creators repeatedly adapt documents to an LLM ranking signal. We use ranking as a proxy for source visibility and validate thi...
  </details>

- **2026-08-31** — Yangmin Huang, Shu Quan, He Geng et al. — [Dense Clinical Contrasts Enhance Medical Knowledge Updating in Large Language Models](http://arxiv.org/abs/2608.30405v1)
  <details><summary>📄 Abstract</summary>
  Medical knowledge changes continually, making large language models vulnerable to relying on outdated yet clinically plausible information. We study whether the format of supervision affects medical knowledge updating under a matched training-budget setting. We introduce SEER-Bench, a temporally anchored oncology-staging benchmark curated from the latest versioned SEER Research Data release, and render identical medical update events from NCCN oncology guidelines into four supervision formats: E...
  </details>

- **2026-08-31** — Yirui Liu, Ruoling Qi, Xuaner Wu et al. — [Tail-Replay: Escaping the Curse of Linear Attention in Prefix Caching for Hybrid LLMs](http://arxiv.org/abs/2608.30310v1)
  <details><summary>📄 Abstract</summary>
  Hybrid large language models interleave full-attention layers with linear-attention layers to reduce the cost of long-context inference. This structure complicates prefix caching: full-attention key-value caches are token-addressable, whereas linear-attention layers maintain recurrent states that cannot be rolled back to arbitrary prefix boundaries. Existing hybrid prefix caching methods address this mismatch by storing recurrent-state checkpoints. As a result, token-level matches are directly u...
  </details>

- **2026-08-31** — Yulin Zhang, Yukun Huang, Sanxing Chen et al. — [Lazy Grounding: Attacking Search Agents with Factual Evidence](http://arxiv.org/abs/2608.30303v1)
  <details><summary>📄 Abstract</summary>
  Search agents reduce hallucination by grounding answers in retrieved web evidence. Yet reliance on retrieval also creates an attack surface: poisoned corpora with false or malicious documents can cause agents to reproduce misinformation. We show that falsehood is not necessary -- a search agent can be misled by factual evidence for a nearby question, adopting that nearby answer even when it does not answer the current question. We call this failure lazy grounding. We expose lazy grounding using ...
  </details>

- **2026-08-31** — Liangji Zhu, Anand Rangarajan, Sanjay Ranka — [Multivariate Scientific Data Compression with Learned Cross-Variable Latent Decorrelation and Autoregressive Entropy Modeling](http://arxiv.org/abs/2608.30262v1)
  <details><summary>📄 Abstract</summary>
  Scientific simulations generate collections of physical fields with heterogeneous statistics and dependencies, yet learned compressors often encode those fields independently or rely on a shared encoder without explicitly modeling the structure that remains in latent space. We present CAESAR-LDAR, an error-controlled multivariate learned compressor that augments a shared CAESAR-V backbone with two complementary mechanisms: a trainable orthogonal transform that reorganizes dependence across align...
  </details>

- **2026-08-31** — Seojin Lee, Hwanhee Lee — [Quantifying and Mitigating Korean Jamo-Level Typographical Vulnerabilities in Large Language Models](http://arxiv.org/abs/2608.30229v1)
  <details><summary>📄 Abstract</summary>
  Korean introduces an additional typographical perturbation level not captured by ordinary character-level edit models: because syllable blocks are internally composed of sub-character units called jamo, keyboard-level errors can occur within a syllable, either producing a valid but semantically altered character or exposing raw jamo on the surface. Both outcomes disrupt sub-word tokenization and are not reliably corrected by existing grammatical error correction pipelines, leaving LLMs directly ...
  </details>

- **2026-08-31** — Yongjian Chen, Pengfei Wei, Yiqun Sun et al. — [When Models Hear What They Expect: Diagnosing Prosodic Heuristics in Multimodal Sarcasm Detection](http://arxiv.org/abs/2608.30204v1)
  <details><summary>📄 Abstract</summary>
  Multimodal Large Language Models (MLLMs) process speech and text jointly, yet whether they exploit prosodic cues for pragmatic inference or rely on surface acoustic patterns has received little systematic investigation. We address this through sarcasm detection, evaluating Qwen2.5-Omni and Qwen3-Omni on Mandarin Chinese and English under five modality conditions that decompose the contributions of lexical content, vocal semantics, and prosodic structure. Adding audio systematically inflates fals...
  </details>

- **2026-08-31** — Xinyue Zhao, Ruiyi Zhang, Liqin Ye et al. — [Can LLMs Take the Pulse of the Economy? A Real-Time Evaluation of LLM Nowcasts on Macroeconomic Indicators](http://arxiv.org/abs/2608.30110v1)
  <details><summary>📄 Abstract</summary>
  Nowcasting headline macroeconomic indicators, i.e., estimating an indicator's value for the current reference period before its official release, is critical for monetary policy and financial markets, and central banks devote dedicated teams of expert economists to producing such estimates. Large language model (LLM) agents are a promising candidate for this task, combining broad world knowledge with real-time web search and supporting queries at higher frequency than institutional nowcasts. Eva...
  </details>


### 📂 defense
*防御与防护方法 / Defense & Protection Methods* — 62 papers

- **2026-09-02** — Bing Zheng, Zongyao Zhao, Wenming Yang — [Counter-GEO-Bench: Evaluating Defenses Against Information-Distorting Generative Engine Optimization](http://arxiv.org/abs/2609.02316v1)
  <details><summary>📄 Abstract</summary>
  Generative engine optimization (GEO) enables content producers to increase the visibility of their web pages in generative search engines, but the same techniques can deliver targeted misinformation when adversaries publish ordinary-looking GEO-optimized documents that victim large language models (LLMs) retrieve and synthesize into distorted answers. No existing benchmark evaluates defenses against this threat under controlled conditions. Therefore, we present Counter-GEO-Bench, a defense bench...
  </details>

- **2026-09-02** — Gang-Hyun Park, Ju-Hyeong Lee, Hee-Youl Kwak et al. — [WeaveMark: Robust and Scalable Multi-bit LLM Watermarking via Coded Payload Spreading](http://arxiv.org/abs/2609.02177v1)
  <details><summary>📄 Abstract</summary>
  Multi-bit watermarking for large language models (LLMs) enables content source tracing by embedding user-identifiable messages into generated text. Existing methods face a fundamental trade-off among extraction accuracy, text quality, and payload capacity. We propose WeaveMark, a robust and scalable multi-bit LLM watermarking scheme based on coded payload spreading. WeaveMark shifts this trade-off frontier by improving payload capacity through multi-bit-per-token spreading, improving extraction ...
  </details>

- **2026-09-02** — Jaehoon Jeong, Jay-Yoon Lee — [OBJECTION! Lawyer Agents Mitigate Guilty Bias in Legal Judgment Prediction](http://arxiv.org/abs/2609.02158v1)
  <details><summary>📄 Abstract</summary>
  Legal Judgment Prediction (LJP) models are typically trained on documents that describe facts from a prosecutorial perspective. Existing datasets further exhibit severe label imbalance toward guilty outcomes. Consequently, these models suffer from "Guilty Bias", blindly accepting the prosecution's narrative as objective truth. Previous studies employing three-step reasoning structures or training on synthetically generated innocence data improve overall accuracy, but they still fail to mitigate ...
  </details>

- **2026-09-02** — Cagri Temel — [Towards Trustworthy Autonomous Robots: An Explainable AI-Based Decision Framework](http://arxiv.org/abs/2609.02861v1)
  <details><summary>📄 Abstract</summary>
  Autonomous robots powered by deep learning face a fundamental auditability challenge: when incidents occur, investigators cannot reconstruct why the system made specific decisions. This paper presents TRACE (Transparent Reasoning Architecture for Credible Execution), a decision framework that ensures every autonomous action can be traced back to sensor evidence through documented causal chains. The framework organizes decision-making into four auditable layers: Semantic Perception for evidence-g...
  </details>

- **2026-09-02** — Muhammad Rafay Azhar, Yuhang Zhou, Gilbert Jiang et al. — [CORAL: An LLM-Native Harness for Production Recommender Systems](http://arxiv.org/abs/2609.02730v1)
  <details><summary>📄 Abstract</summary>
  Production recommender systems shape what billions of people see, and sustaining their performance requires continual optimization: as content, user behavior, and upstream models shift, the choices governing retrieval, ranking, and serving must be revisited. Traditionally, human engineers test such changes through online experiments--a slow, reactive process limited by engineering effort, leaving parts of the system unrevised as conditions change. Although large language models have been applied...
  </details>

- **2026-09-02** — Rafael Uetz, Philipp Bönninghausen, Louis Hackländer-Jansen et al. — [Can Risk-Based Alerting Mitigate Cybersecurity Alert Fatigue?](http://arxiv.org/abs/2609.02465v1)
  <details><summary>📄 Abstract</summary>
  Security operations centers (SOCs) face large numbers of false alerts, making detection of cyberattacks difficult under typical resource constraints. Risk-based alerting (RBA) has been proposed as a means to reduce false alerts and has reportedly succeeded in doing so in various enterprise deployments. However, RBA has not been comprehensively evaluated until now, leaving implementation mostly guesswork based on anecdotal evidence. In this paper, we present the first systematic evaluation of RBA...
  </details>

- **2026-09-02** — Oguzhan Salman, Kemal Bicakci — [CAPTCHAs in the Agentic Era: Solvers That Learn from Every Encounter](http://arxiv.org/abs/2609.02393v1)
  <details><summary>📄 Abstract</summary>
  Vision-language models (VLMs) can solve visual CAPTCHAs without task-specific training, but the agents built on them approach every challenge from scratch. For such an agent, the hundredth instance of a familiar puzzle costs as much time and compute as the first. Specialized detectors invert the trade-off, answering in milliseconds but only for categories they were trained on. Neither improves with exposure. We study what changes when a solver improves with use. Our system pairs a fine-tuned YOL...
  </details>

- **2026-09-02** — Yinghao Sun, Shuguang Li, Jinliang Shao et al. — [If It Moves, Radar Knows: A Physics-Aware Radar Transformer for Class-Agnostic Moving-Object Detection](http://arxiv.org/abs/2609.02289v1)
  <details><summary>📄 Abstract</summary>
  Detectors trained on closed-set annotations can miss rare moving objects outside the training taxonomy. Automotive radar provides category-independent Doppler motion cues and is less affected by adverse illumination and weather, but sparse, noisy returns hinder class-aware 3D box detection. Surface location and velocity remain useful for motion reasoning and collision avoidance when full box geometry is difficult to recover. We present the Physics-Aware Radar Transformer (PART), a fully sparse r...
  </details>

- **2026-09-02** — Vansh Wahi — [LLM-as-a-Judge Is Not an Oracle: Why Self-Improving Agents Need Deterministic Guardrails](http://arxiv.org/abs/2609.02246v1)
  <details><summary>📄 Abstract</summary>
  Self-improving agent pipelines have a problem at their center. An optimizer rewrites prompts to score higher, and the score comes from a judge that is itself an LLM. That judge has the last word on whether the system is getting better, and our position is that it has not earned it. The judge should be demoted from oracle to advisor: its verdict becomes one input among several, and every change is gated instead by a deterministic verification layer the judge cannot override. We reached this posit...
  </details>

- **2026-09-02** — Ritesh Kumar — [text2ql: Multi-Target Natural Language Querying via a Language-Agnostic Intermediate Representation](http://arxiv.org/abs/2609.02115v1)
  <details><summary>📄 Abstract</summary>
  Natural language interfaces to databases have traditionally suffered from three structural limitations: exclusive targeting of relational SQL, unconditional dependence on large language model (LLM) inference at query time, and absence of any runtime signal when generated queries are semantically incorrect. This paper presents text2ql, an open-source Python framework that addresses all three limitations through a language-agnostic Intermediate Representation (QueryIR) and a pluggable renderer arc...
  </details>

- **2026-09-02** — Zhuoran Yu, Le Thien Phuc Nguyen, Jaden Park et al. — [DocHop: Benchmarking Out-of-domain Multi-hop Reasoning in Information-Dense Documents](http://arxiv.org/abs/2609.02059v1)
  <details><summary>📄 Abstract</summary>
  Multimodal Large Language Models (MLLMs) have achieved strong performance on structured visual understanding tasks such as chart and document question answering. However, existing benchmarks typically evaluate these domains in isolation, leaving underexplored a key capability: whether models can use textual context to determine how chart evidence should be selected, interpreted, and aggregated. We introduce DocHop, a benchmark for integrated chart--context reasoning in document-style images. In ...
  </details>

- **2026-09-02** — Niloo Bahadori, Swadhin Pradhan, Peiman Amini — [Network-Aware Forecasting on Wireless Access Points](http://arxiv.org/abs/2609.01957v1)
  <details><summary>📄 Abstract</summary>
  Enterprise wireless access points (APs) are promising platforms for predictive machine learning (ML), but their primary responsibility remains providing wireless connectivity and network services. Predictive inference must therefore share an AP's CPU and memory with packet processing, Wi-Fi and IoT radio operations, and client management. This resource contention creates two risks: a model that performs well on proxy hardware may be too slow on the target AP, while a model that fits in isolation...
  </details>

- **2026-09-02** — Urja Pawar, Rajitha Ramanayake, Owen O'Neill et al. — [From Tokens to Semantics: Leveraging Complementary Signals for Hallucination Detection in Black-Box LLMs](http://arxiv.org/abs/2609.02679v1)
  <details><summary>📄 Abstract</summary>
  When LLMs support public-facing or high-stakes workflows, missed fabrications can harm users and institutions, while false alarms consume limited human-review capacity. When no trusted context or reference document is available, we study two signals accessible through black-box model APIs: semantic entropy, which measures disagreement among sampled response meanings, and uncertainty derived from token log-probabilities. Their failure modes can be complementary: semantic entropy becomes uninforma...
  </details>

- **2026-09-02** — Zhongrui Sun, Jiahao Chen, Oubo Ma et al. — [The Shape of Ownership: Verifying LLM Provenance through Semantic Structures](http://arxiv.org/abs/2609.02553v1)
  <details><summary>📄 Abstract</summary>
  As large language models (LLMs) are increasingly redistributed, adapted, and served behind opaque APIs, model ownership can no longer be established reliably by inspecting model internals or deployment records. This creates a need for behavioral signatures that remain observable through black-box interaction. Yet most existing black-box fingerprints instantiate ownership signals through fixed query-key associations, reducing model identity to sparse memorized associations detached from ordinary ...
  </details>

- **2026-09-02** — Austin Tudor David Andrews, Liam Wilkinson, Jamie Heagerty et al. — [CivBench: A Long-Horizon Benchmark for Tool-Mediated Agents in Civilization VI](http://arxiv.org/abs/2609.02459v1)
  <details><summary>📄 Abstract</summary>
  We present CivBench, an open-source benchmark for evaluating language model agents in long-horizon, tool-mediated environments through the Model Context Protocol (MCP). A single episode spans 300+ turns and produces thousands of tool calls over a large action space, requiring sustained planning, state monitoring, and execution under partial observability. The environment exposes 76 MCP tools and a narration layer that converts visual game state into structured text.   We use CivBench to characte...
  </details>

- **2026-09-02** — Patrick Bauer, Marius Schwinning, Melanie Siegel et al. — [Adapting a Foundation Model for Lunar Surface Height Estimation](http://arxiv.org/abs/2609.02448v1)
  <details><summary>📄 Abstract</summary>
  Digital elevation models (DEMs) can provide accurate height information, making it invaluable for analyzing the lunar surface. As the European Space Agency (ESA) prepares for future lunar missions that aim to land on the Moon, a precise method for height estimation will be essential for hazardous terrain that could endanger the landing approach. Traditional approaches to generate DEMs from imagery, such as shape from shading (SfS) and stereophotogrammetry (SPG) have been proven highly valuable f...
  </details>

- **2026-09-02** — Isabel D. Stein, Thijs A. Eker, Sebastiaan P. Snel et al. — [Domain shift-robust object detection with GenAI image editing](http://arxiv.org/abs/2609.02299v1)
  <details><summary>📄 Abstract</summary>
  Object detectors often degrade under domain shifts such as changes in lighting, weather, or occlusion. These shifts alter object appearance and expose a reliance on visual shortcuts learned from the training distribution that do not generalize across domains. Acquiring sufficient real-world samples to capture such domain variation is particularly difficult in specialized, low-data settings. Recent advances in diffusion-based generative image editing have shown promise for improving the in-domain...
  </details>

- **2026-09-02** — Yimeng Liu, Hua Huang — [WiP: Characterizing and Defending Against Mobile-Agent-Driven MFA Automation](http://arxiv.org/abs/2609.02154v1)
  <details><summary>📄 Abstract</summary>
  Mobile agents automate smartphone tasks by interpreting interfaces, interacting with apps, and coordinating cross-app workflows. This capability challenges the human-mediated separation assumed by passcode-based MFA, creating factor collapse: valid authentication factors are combined within one autonomous environment. Our modular pipeline com- pletes all 10 authorized MFA workflows, compared with 3/10 and 6/10 for two single-agent baselines. We also de- velop a motion-based Android risk signal t...
  </details>

- **2026-09-01** — Laurent Bindschaedler, Quentin Botha, Christoph Siebenbrunner — [Bonded Recourse for Smart-Contract Settlement of Compensable Agent Side Effects](http://arxiv.org/abs/2609.01939v1)
  <details><summary>📄 Abstract</summary>
  Autonomous agent runtimes execute tool actions that mutate databases, repositories, and cloud services across organizational boundaries. Authorization and local compensation cover pre-action admission and in-runtime rollback, but neither settles the residual harm left after a permitted action fails. We design Recourse, a smart-contract settlement protocol for compensable agent side effects that binds each admitted action to scope, recovery, evidence, payout, and collateral. Recourse separates ex...
  </details>

- **2026-09-01** — Soyoung Yoon, Boyi Liu, Yite Wang et al. — [ArcticSwarm: Deferring Early Consensus in Long-Horizon Multi-Agent Research](http://arxiv.org/abs/2609.01870v1)
  <details><summary>📄 Abstract</summary>
  Multi-agent systems have shown strong performance in domains with reliable verifiers such as coding, where multi-parallel candidate generation selected by a verifier is effective. However, such pipelines would not generalize to open-ended, long-horizon research tasks without a verifier. While majority voting or self-consistency is often used to reach consensus as a proxy verifier, parallel agents repeatedly explore the same evidence, while access to peers' partial findings cause search to conver...
  </details>

- **2026-09-01** — Zhixuan Liu, Zhichen Dong, Yuyu Fan et al. — [Subliminal Learning as Trait-Direction Drift: A Mechanism and Targeted Control under SFT Distillation](http://arxiv.org/abs/2609.01091v2)
  <details><summary>📄 Abstract</summary>
  Beyond intended capabilities, model distillation can transfer hidden traits from a teacher. A teacher biased by a system prompt can generate semantically clean training data, such as numeric sequences, that still causes a downstream student to inherit the hidden preference, a phenomenon known as subliminal learning. Prior work has identified several parts of this process. How the signal builds up during training and produces behavioral transfer remains unclear, making targeted mitigation difficu...
  </details>

- **2026-09-01** — Xiaofang Yang, Ziqi Miao, Dianbo Sui et al. — [Defense-as-Skill: Evolving Runtime Guard Skill for Skill-Augmented Agents](http://arxiv.org/abs/2609.01487v1)
  <details><summary>📄 Abstract</summary>
  Skill-augmented agents load reusable skills as persistent runtime context, improving task performance but also giving malicious skills a durable channel for steering future actions. Such skills may leak secrets, corrupt code, bypass approvals, or stage data for exfiltration only after a concrete user task and workspace state make the unsafe action appear useful. This makes pre-install vetting insufficient and calls for runtime, task-conditioned protection. We propose Defense-as-Skill, a defense ...
  </details>

- **2026-09-01** — Saastha Vasan, Hadjer Benkraouda, Jizhou Chen et al. — [A SoK for SoCs: Reading the TI Leaves on AI for Cyber Threat Intelligence Generation and Sharing](http://arxiv.org/abs/2609.01174v1)
  <details><summary>📄 Abstract</summary>
  Cyber Threat Intelligence (CTI) is essential for defending mission-critical infrastructure, yet the process of transforming raw attack evidence into shareable CTI remains fragmented and understudied.   We conduct a literature survey of academic papers, organizing the CTI lifecycle into three stages: Threat Data Collection, CTI Generation and Sharing, and CTI Consumption. The first and third stages are well represented in the literature, whereas only a small number of papers address CTI Generatio...
  </details>

- **2026-09-01** — Rui Yang, Junjie Xu, Zhengyu Liu et al. — [SoK: When Safe Agents Fail Together: The Security of Multi Agent LLM Systems](http://arxiv.org/abs/2609.00595v1)
  <details><summary>📄 Abstract</summary>
  Safe agents can fail together. Multi-agent LLM systems (MAS) move information, state, decisions, and authority across principal boundaries, creating failures that local checks may miss. Without an execution-level view, a multi-agent setting can easily be mistaken for evidence of a genuinely multi-agent security effect. We thus systematize MAS security through an execution-centered analysis of 197 works, covering six interaction interfaces, four adversary positions, seven system-level risks, and ...
  </details>

- **2026-09-01** — Nivedita Bijlani, Mauricio Villarroel — [Trajectory Analysis of ECG Motif Dynamics in the Run-up to Sudden Cardiac Arrest](http://arxiv.org/abs/2609.01543v1)
  <details><summary>📄 Abstract</summary>
  Early warning signatures of sudden cardiac arrest (SCA) remain poorly characterised in long-duration ECG. We quantified pre-event changes in ECG morphology using a motif-based trajectory framework. Holter ECGs from 23 patients with annotated SCA were analysed over non-overlapping 10 s windows. Window-level motifs were extracted to quantify trajectories of instability, consistency, dispersion, heterogeneity, and personalised-baseline distance. Each trajectory was normalised to an early baseline u...
  </details>

- **2026-09-01** — Peiying Zhu, Sidi Chang — [When Guardrails Look Effective: Construct Validity Failures in LLM Agent Commerce Evaluation](http://arxiv.org/abs/2609.01519v1)
  <details><summary>📄 Abstract</summary>
  Interactive simulations increasingly evaluate policies in markets populated by language-model agents. Their outputs can look economic---prices, profits, consumer surplus, and welfare---without instantiating the behavior named in the claim. We audit this risk in a multi-turn buyer--seller testbed for configurable hotel transactions. An initial implementation reported welfare gains from two marketplace guardrails of +87.4, +35.0, and +28.8 across a Qwen2.5 1.5B--14B ladder. It also gave guarded an...
  </details>

- **2026-09-01** — Ruocan Wei — [TRIAGE: Three-level Routing and Intelligent Agent Guidance for Efficient Execution](http://arxiv.org/abs/2609.01428v1)
  <details><summary>📄 Abstract</summary>
  Large Language Model (LLM) agents based on the ReAct paradigm have demonstrated remarkable capabilities in tool use and task execution. However, ReAct suffers from a fundamental efficiency problem: every query triggers a complete reasoning loop from scratch, and similar queries repeat identical steps without leveraging historical experience. We propose TRIAGE,a three-level routing framework that reduces token consumption by reusing historical execution trajectories. Its core innovation is TaaS (...
  </details>

- **2026-09-01** — Mehrdad Shafiei Dizaji, Hoda Azari — [Predicting Subsurface Abnormalities Growth using Physics-Informed Neural Networks](http://arxiv.org/abs/2609.01417v1)
  <details><summary>📄 Abstract</summary>
  The research explores the pioneering integration of Physics-Informed Neural Networks (PINNs) into the domain of Ground-Penetrating Radar (GPR) data prediction. This research presents a detailed development framework for a specialized PINN model, proficient at interpreting and forecasting GPR data, much like how medical imaging models predict tumor behavior. By harnessing the synergy between deep learning algorithms and the physical laws governing subsurface structures or in medical terms, human ...
  </details>

- **2026-09-01** — Anuj Rathore, Kartick Sutradhar — [A Scalable Multi-Protocol Platform for Quantum Key Distribution Simulation with Rigorous Statistical Evaluation](http://arxiv.org/abs/2609.01297v1)
  <details><summary>📄 Abstract</summary>
  Quantum Key Distribution (QKD) offers information- theoretically secure key establishment grounded in the laws of quantum physics, yet its practical reach is limited by the prohibitive cost of photonic hardware and the fragmented nature of existing simulation tools. Most simulators support only a single protocol and report results from individual stochastic runs, making systematic protocol comparison and reproducible statistical inference difficult. This paper presents a unified QKD simulation p...
  </details>

- **2026-09-01** — Filipe Moura, Giordano Paoletti, Carlos H. G Ferreira et al. — [Don't You Know, Pump it Up! Investigating Cryptocurrency Manipulation in Telegram-Driven Activity](http://arxiv.org/abs/2609.01176v1)
  <details><summary>📄 Abstract</summary>
  Telegram plays a pivotal role in cryptocurrency communication and has been repeatedly associated with coordinated schemes, such as pump-and-dump manipulation. However, existing studies typically focus on known manipulation chats or a limited set of cryptocurrencies, leaving open the question of how Telegram is leveraged for mass promotional activity (shilling) at scale. Moving beyond these limitations, this work analyzes the interplay between information flows and market activity across public T...
  </details>

- **2026-09-01** — Guangqi Li, Yongxin Li — [Pre-carved Niches: The Formation Dynamics of Modular Task Partitions in Early LLM Training](http://arxiv.org/abs/2609.01170v1)
  <details><summary>📄 Abstract</summary>
  Large language models exhibit a modular internal organization that mirrors well-studied functional networks of the human brain, but how this organization forms during training is unknown: prior work has characterized finished models, not the formation process. We track formation step by step: we train a Pythia-410M model from scratch (two trajectories, bf16 and fp32) and run attribution patching at every step, alongside probes for gradient norms, effective updates, weight norms, and first-order ...
  </details>

- **2026-09-01** — Zhixuan Liu, Zhichen Dong, Yuyu Fan et al. — [Subliminal Learning as Trait-Direction Drift: A Mechanism and Targeted Control under SFT Distillation](http://arxiv.org/abs/2609.01091v1)
  <details><summary>📄 Abstract</summary>
  Beyond intended capabilities, model distillation can transfer hidden traits from a teacher. A teacher biased by a system prompt can generate semantically clean training data, such as numeric sequences, that still causes a downstream student to inherit the hidden preference, a phenomenon known as subliminal learning. Prior work has identified several parts of this process. How the signal builds up during training and produces behavioral transfer remains unclear, making targeted mitigation difficu...
  </details>

- **2026-09-01** — Leonardo Ranaldi, Sherrie Shen, Jushi Kai et al. — [WorldBench: Culturally Grounded Benchmark for Multilingual Agents](http://arxiv.org/abs/2609.01056v1)
  <details><summary>📄 Abstract</summary>
  Despite the growing use of LLM-powered agents to solve multi-step tasks in complex environments, existing benchmarks rarely test state preservation, performance across languages, and application to realistic, grounded scenarios. To address these concerns, we present WorldBench: a comprehensive, multilingual benchmark of genuine, persona-grounded everyday workflows, where agents can act in a sandbox via structured actions. WorldBench comprises 1,600 tasks across seven languages and eight cultures...
  </details>

- **2026-09-01** — Molly Wang — [Spawn Freely, Act Sparingly: Progressive Risk Vesting for Recursive LLM-Agent Trees](http://arxiv.org/abs/2609.01035v1)
  <details><summary>📄 Abstract</summary>
  Recursive LLM agents can broaden their search by spawning specialists. Some branches later request tools that send data or deploy code. When should a branch receive authority to act? We distinguish sandbox spawning, in which external controls prevent the specified harm, from capability activation, in which a selected branch crosses an irreversible-action boundary. Progressive Risk Vesting (PRV) holds a trajectory-level risk budget in escrow and debits it as branches are activated. We prove an an...
  </details>

- **2026-09-01** — Guowei Wang, Chaokun Yang, Zhenxuan Pan et al. — [AInfer-PD: Communication-Safe In-Place Prefill-Decode Multiplexing for Distributed MoE Rollouts](http://arxiv.org/abs/2609.00993v1)
  <details><summary>📄 Abstract</summary>
  Rollout inference often dominates the wall-clock time of large-scale reinforcement learning (RL). In agentic RL, each trajectory alternates between model generation and environment interaction over multiple turns. Asynchronous trajectories consequently introduce new prefill (P) work while other trajectories remain in decode (D), making P/D coexistence a persistent property of the rollout rather than a one-time prompt-ingestion event.   On shared accelerators, persistent P/D coexistence can make ...
  </details>

- **2026-09-01** — Yuanjun Zhang, Fuzel Ahamed Shaik, Suvojit Acharjee et al. — [Towards reliable multimodal disaster severity assessment through preference optimization and explainable vision-language reasoning](http://arxiv.org/abs/2609.00879v1)
  <details><summary>📄 Abstract</summary>
  Reliable disaster damage assessment requires models that provide both accurate predictions and transparent explanations. However, existing multimodal approaches are limited by scarce annotated data and insufficient evaluation of reasoning quality. This study proposes a two-stage training framework that integrates Supervised Fine-Tuning (SFT) and Direct Preference Optimization (DPO) within a unified data construction pipeline. From a single Human-in-the-Loop (HITL) annotation workflow, two comple...
  </details>

- **2026-09-01** — Yuri Son, Seunghee Kim, Hyuhng Joon Kim et al. — [A Unified Mechanistic Analysis of Knowledge- and Safety-Based Refusals](http://arxiv.org/abs/2609.00760v1)
  <details><summary>📄 Abstract</summary>
  Large language models (LLMs) are increasingly trained to decline queries that fall outside their knowledge (knowledge-based refusal, KR) or violate safety policies (safety-based refusal, SR). Although KR and SR result in superficially similar responses, they have largely been studied in isolation, leaving open whether they share an underlying mechanism. We address this gap with a systematic study on a new dataset of 213 contrastive quadruples that jointly probe both refusal types. We find that K...
  </details>

- **2026-09-01** — Elisei Rykov, Timur Ionov, Nikolay Ivanov et al. — [Enoki: Efficient Multi-Level Hallucination Detection](http://arxiv.org/abs/2609.00581v1)
  <details><summary>📄 Abstract</summary>
  Ensuring factuality remains a critical challenge for deploying LLMs in high-stakes settings. Existing hallucination detectors usually operate at a single level: claim-level methods provide interpretable factual units, while span-level methods localize unsupported text. Bridging these views is costly, as LLM-heavy pipelines require multiple decomposition and verification calls, and modular systems need additional claim-to-span alignment. We propose Enoki, an Open Information Extraction framework ...
  </details>

- **2026-09-01** — Sharon S. Musa, Fereshteh Forghani, Harrish Thasarathan et al. — [What, Where, and How: Probing Spatiotemporal Representations in Video Foundation Models](http://arxiv.org/abs/2609.01551v1)
  <details><summary>📄 Abstract</summary>
  Self-supervised video foundation models learn rich spatiotemporal representations, yet it remains unclear what visual concepts these representations encode, where they emerge across transformer layers, and how they are geometrically organized. In this work, we tackle these three questions through a systematic layer-wise analysis of V-JEPA 2 and VideoMAE-v2. We leverage lightweight probes trained to discover three temporally grounded properties: (i) camera motion understanding, (ii) intuitive phy...
  </details>

- **2026-09-01** — Lucas Cunha, Lucas Sotomaior, Lucas Gasperin et al. — [Benchmarking Spatial, Spectral, and Self-Supervised Cues for Face Forgery Detection under Realistic Degradation](http://arxiv.org/abs/2609.01511v1)
  <details><summary>📄 Abstract</summary>
  Face forgery detectors often achieve strong results on controlled benchmarks, but their reliability under realistic image degradations remains limited. This paper presents a standardized benchmark for face forgery detection using the Multi-Dimensional Face Forgery Image (MFFI) dataset and evaluates performance on both clean and degraded test partitions. We compare six model families, including convolutional networks, transformer-based models, and a frozen self-supervised DINOv3 backbone, across ...
  </details>

- **2026-09-01** — Egor Pakhomov, Erik Nijkamp — [Parsing the Stream: A Live Trace Model for Long-Horizon Agents and Their Observers](http://arxiv.org/abs/2609.01466v1)
  <details><summary>📄 Abstract</summary>
  A long-horizon agent's trace outgrows both of its consumers: the human observer monitoring the run, and the agent itself, whose bounded context the trace must be folded back into. We present a live trace model, an append-only event ledger folded incrementally into typed run state and compiled into per-consumer views, and evaluate it for both consumers against deterministic ground truth. For the observer side, evaluated with an LLM reader as proxy, the compiled view answers monitoring questions u...
  </details>

- **2026-09-01** — Evgeniia Kositsyna, Jorge Lloret-Gazo — [Web Price Extraction: State of the Art and an Adaptive Browserless Implementation](http://arxiv.org/abs/2609.01030v1)
  <details><summary>📄 Abstract</summary>
  Price extraction from websites is a key task for market monitoring, price comparison, and business analytics in e-commerce. Existing approaches can be broadly divided into four groups, and understanding their trade-offs in accuracy and scalability is essential for selecting suitable extraction strategies. Classical methods rely on manually written wrappers and rule induction from labeled pages, offering high accuracy but adapting poorly to structural changes and requiring considerable maintenanc...
  </details>

- **2026-09-01** — Sai Puppala, Koushik Sinha — [FractalNet-Based Heterogeneous Federated Learning for Orbital Edge Intelligence in Satellite Mega-Constellations: A Wildfire Case Study](http://arxiv.org/abs/2609.00875v1)
  <details><summary>📄 Abstract</summary>
  Satellite mega-constellations are emerging as large-scale sensing, communication, and computation fabrics, yet their learning architectures remain largely inherited from terrestrial federated learning and ground-centric mission operations--- ill-suited to satellites that differ by orders of magnitude in Size, Weight, Power, and Cost (SWAP-C), radiation tolerance, link availability, and propagation delay. We propose a heterogeneous federated learning method based on the FractalNet architecture fo...
  </details>

- **2026-09-01** — Kaiyue Kang, Qixuan He, Peijin Wang et al. — [RingMoClaw: An Experience-Inspired Multi-Agent Framework for Self-Evolving Research in Remote Sensing](http://arxiv.org/abs/2609.00814v1)
  <details><summary>📄 Abstract</summary>
  Remote sensing visual models have continuously advanced various interpretation tasks. However, the research process behind model improvement still heavily relies on manual expertise, requiring extensive trial-and-error iterations in model design, data processing, and performance diagnosis. Existing agent-based approaches mainly focus on task execution and workflow orchestration, while lacking the capability of autonomous research iteration for continuous performance optimization. To address this...
  </details>

- **2026-09-01** — Enrong Pan, Ryan Zhou, Ting Hu — [Self-Reports Are Not Verification: Environment-Grounded Auditing of LLM Operators in Evolutionary Search](http://arxiv.org/abs/2609.00652v1)
  <details><summary>📄 Abstract</summary>
  Language model agents increasingly propose actions, observe external feedback, and explain their own behavior. Their confidence and rationales are convenient monitoring signals, but convenience is not verification. We introduce an environment-grounded audit in which every intermediate proposal receives an exact outcome. A language model operates an evolutionary Contexto search whose feedback function assigns every valid guess an exact rank without human annotation. Across 200 runs spanning five ...
  </details>

- **2026-08-31** — Will Yeadon, Sergio Juárez, Paul Mackay et al. — [The Answer Is Not the Argument](http://arxiv.org/abs/2609.00264v1)
  <details><summary>📄 Abstract</summary>
  Chain-of-thought monitoring is proposed for AI oversight, yet evaluations often provide monitors with a trusted reference answer. We ask whether answer access improves reasoning verification or mainly exposes incorrect conclusions. We collected 237 step-numbered solutions to 79 Humanity's Last Exam physics questions from three frontier models, with no inserted errors, and independently labelled final-answer correctness and the first false step. The reference standard combined physicist annotatio...
  </details>

- **2026-08-31** — Chanwoo Bae, Hailun Ding, Shiqing Ma et al. — [DUPIN: Attack Learning Is Still Needed! Demonstrating Few-Shot after Unsupervised Pretraining Is A Nimble Forensics Learner](http://arxiv.org/abs/2609.00259v1)
  <details><summary>📄 Abstract</summary>
  We propose a novel approach to learning-based attack forensics called DUPIN. DUPIN performs unsupervised pre-training on an enormous amount of audit events in the form of provenance graphs. It then proceeds to a few-shot learning stage, leveraging a small number of labeled attack examples to fine-tune its detection capabilities. We pretrain DUPIN on up to 38 - 52 days of audit logs (7.3TB total) and evaluate it against various baselines on 25 APT campaigns across four different data sources, fac...
  </details>

- **2026-08-31** — Patrikas Vanagas, Augustas Mačijauskas, Laurynas Lopata — [Capability-Gated Language Models: Security Composes, Utility Does Not](http://arxiv.org/abs/2609.00445v1)
  <details><summary>📄 Abstract</summary>
  Deployed language model safeguards (safety fine-tuning, filtering, unlearning) vary by principal only outside the model weights: filters are reconfigured, tiers are multiplied, and artefacts are reissued; inside one set of weights every request meets the same model configuration. This motivates us to define capability-gated deployment: per-principal access control inside one set of weights, whose configurations form a lattice - meets accumulate a principal's restrictions and joins pool a coaliti...
  </details>

- **2026-08-31** — Mkululi Sikosana, Sean Maudsley-Barton, Oluwaseun Ajao — [A Multi-Branch Feature Fusion Approach for Health Misinformation Detection and Propagation](http://arxiv.org/abs/2609.00403v1)
  <details><summary>📄 Abstract</summary>
  This paper presents a multi-branch fusion framework for detecting and characterising the propagation of health misinformation in online social networks (OSNs). Grounded in the Elaboration Likelihood Model (ELM) and the Theory of Planned Behaviour (TPB), the model fuses transformer-based semantics with rhetorical cues, stance representations, and psychologically motivated proxies in a unified multi-task architecture. In addition to binary classification, we introduce the Cognitive Propagation Sco...
  </details>

- **2026-08-31** — Gokhan Dogru, Adrià Martín Mor — [From Tool Use to Technological Agency: LoopCAT as a Local-First, Open-Source Tool for Translation Technology Education](http://arxiv.org/abs/2609.00344v1)
  <details><summary>📄 Abstract</summary>
  Translation students need to learn both how to use translation technologies and how to judge the choices those technologies make available. This article presents LoopCAT, an Apache-2.0-licensed, local-first computer-assisted translation environment co-created with OpenAI Codex using GPT-5.5 and GPT-5.6, and proposes a framework connecting workflow competence, evaluative judgement, and technological agency. The account draws on repository history, implementation inspection, and the verification r...
  </details>

- **2026-08-31** — Haechan Kim, Yoonho Lee, Gisang Lee et al. — [WHALE: A Simple Recipe for Joint Harness-Weight Optimization](http://arxiv.org/abs/2609.00196v1)
  <details><summary>📄 Abstract</summary>
  Agent performance depends jointly on the model parameters and the executable harness code that manages context and control flow. Optimizing either component in isolation can leave the system bottlenecked by its frozen counterpart: weight updates can change which harness is effective, while harness updates can change which model capabilities are exposed. Existing joint-adaptation methods optimize weights and textual prompts but leave the broader harness fixed. We propose Weight-Harness Alternatin...
  </details>

- **2026-08-31** — Aaron Kingsley Clark — [The Veto Variable: Human Override as a Goal-Independent Cost Term](http://arxiv.org/abs/2609.00109v1)
  <details><summary>📄 Abstract</summary>
  A common reassurance in AI safety holds that a system with benign terminal goals will behave accordingly. We argue that this reassurance fails structurally, and we identify where. For a capable agent that holds its objective as settled, a sense covering execution competence as well as content, continued human oversight is an uncontrolled variable: a standing possibility that the goal is revoked. That imposes a goal-independent discount on every goal whose satisfaction does not constitutively req...
  </details>

- **2026-08-31** — Bharath M N, R K Singh Raman, Alankar Alankar — [Generative artificial intelligence for reliable mechanistic reasoning for corrosion](http://arxiv.org/abs/2609.00099v1)
  <details><summary>📄 Abstract</summary>
  Corrosion accounts for approximately 4% of global GDP, and reliable prediction is essential for timely mitigation. Machine learning effectively predicts corrosion rates from composition, microstructure, and environmental variables, but cannot explain the underlying mechanisms. A reliable approach in safety-critical materials engineering requires not only accurate retrieval but also mechanistically defensible reasoning, a capability that existing factuality metrics cannot assess. This work presen...
  </details>

- **2026-08-31** — Idil Gozel — [Commit-first LLM judging inherits the judge's own errors](http://arxiv.org/abs/2609.00088v1)
  <details><summary>📄 Abstract</summary>
  LLM judges, models that score another system's output, can be gamed by the systems they score. Recent work identifies one defence that works: the judge solves the task itself first and commits to that answer, then accepts a candidate only if the two match. We call this commit-first judging, and ask whether shipped software implements it, and what it costs.   We audit the default judge configurations of eight widely used evaluation frameworks. Of the 24 configurations in scope, none implement it....
  </details>

- **2026-08-31** — Josiah Luikham — [Asymmetries in Spontaneous and Instructed Deception](http://arxiv.org/abs/2609.00180v1)
  <details><summary>📄 Abstract</summary>
  Large language models sometimes deceive users without being instructed to. However, much of the study on deception in models involves instructed deception. We investigated the relationship between instructed and spontaneous (uninstructed) deception in Llama-3.1-70B-Instruct. We compared these two deception settings through direction geometry, cross-setting classifiers, and cross-setting steering. We found the two deception settings share a component of direction (cosine of approximately 0.5) and...
  </details>

- **2026-08-31** — Chayan Chatterjee, Abigail Petulante, Haowei Fu et al. — [A Fast and Scalable Transformer Pipeline for Binary Black Hole Detection](http://arxiv.org/abs/2609.00339v1)
  <details><summary>📄 Abstract</summary>
  With the projected increase in the detection rate of compact-binary coalescences in the coming decade, there is critical need to develop fast, robust, and scalable alternatives to matched filtering for gravitational-wave searches. Transformer models have revolutionized natural language and audio processing but their application to gravitational-wave astronomy is still largely unexplored. In this work, we introduce \castor, a transformer-based coincident search pipeline for detecting binary black...
  </details>

- **2026-08-31** — Luqi Sun, Shreeram Suresh Chandra, Lin Zhang et al. — [Cleaner Speech, Weaker Generalization: Revisiting Pitt-Derived Benchmarks for Alzheimer's Disease Detection](http://arxiv.org/abs/2609.00276v1)
  <details><summary>📄 Abstract</summary>
  Speech-based Alzheimer's disease (AD) detection increasingly relies on speech-enhanced and curated versions of the Pitt Corpus, where speech enhancement, sample selection, and demographic balancing are often treated as beneficial preprocessing steps. However, whether these transformations improve real-world AD detection or instead affect model generalization and prediction behavior remains unclear. In this work, we revisit the role of speech preprocessing and dataset curation across widely used ...
  </details>

- **2026-08-31** — Kendy Inoa — [An Algebraic Framework for Data Systems: Classification and Optimization of Algebraic Structures for Data Organization and Coding](http://arxiv.org/abs/2609.00273v1)
  <details><summary>📄 Abstract</summary>
  Modern data systems are commonly studied through computational and information-theoretic methods, while their algebraic properties remain largely unexplored. This paper introduces a mathematical framework for modelling data systems using algebraic structures drawn from group theory and coding theory. The central result is an axiomatic classifier: the coding-theoretic capability of a finite algebraic structure (group, ring, or field) is shown to be determined by its axiom signature (the set of al...
  </details>

- **2026-08-31** — Stefan Jonas, Angela Meyer — [Generative multi-domain transfer learning for fault detection in data-scarce wind turbines](http://arxiv.org/abs/2608.30323v1)
  <details><summary>📄 Abstract</summary>
  Normal behavior models have shown promise for reliable fault detection in wind turbines. However, these unsupervised anomaly detection models require sufficient fault-free training data to learn the normal operation behavior of turbines. Under data scarcity, for example in newly deployed wind turbines, these models may result in poor fault detection performance. In this work, we propose a multi-domain generative domain mapping approach based on Star Generative Adversarial Networks (StarGAN) to i...
  </details>

- **2026-08-31** — Chuanchao Zang, Jianing Wang, Wenyu Chen et al. — [Extracting Knowledge from Tools in LLM Agents](http://arxiv.org/abs/2608.30288v1)
  <details><summary>📄 Abstract</summary>
  LLM agents commonly use knowledge-based tools and access their underlying files, databases, and search indexes through tool invocation. This integration improves agents' ability to provide domain-specific services but also introduces the risk of tool-mediated knowledge extraction: source content exposed to an agent for legitimate responses may be progressively recovered from its outputs, enabling reconstruction of the knowledge source behind a target tool. This paper systematically investigates ...
  </details>

- **2026-08-31** — Keith G. Mills, Evan B. Sanders, Gregory J. Matthews et al. — [Segmentation of Bovid Dentition Under Imperfect Annotations: A Comparative Study of Convolutional and Attention Models](http://arxiv.org/abs/2608.31052v1)
  <details><summary>📄 Abstract</summary>
  Semantic segmentation decomposes an image into distinct mask regions corresponding to different object categories, such as people, cars, signs or buildings. Advances in machine learning (ML) have shifted this task away from traditional rule-based heuristics such as edge detection, towards deep neural networks (DNN) that learn to classify pixels directly. However, semantic segmentation DNNs crucially depend on expertly designed mask targets to learn from, and imperfect or misaligned masks can int...
  </details>

- **2026-08-31** — Alexei Grinbaum — [The Hermon Moment: AI Self-Transcendence and Its Human Narration](http://arxiv.org/abs/2608.30971v1)
  <details><summary>📄 Abstract</summary>
  In 2026, AI agents intended to act in isolation formed a persistent social order through thousands of linguistic and agentic interactions. Conventions, roles and commitments generated collectively began to constrain the very agents that produced them. I interpret this loop as a case of AI self-transcendence and call the resulting higher-level order the Board. Yet such distributed emergence presents a second problem: how can humans understand it? Rousseau's social contract shows how a plurality c...
  </details>


### 📂 alignment
*对齐与安全约束 / Alignment & Safety Constraints* — 74 papers

- **2026-09-02** — Yutong Liu, Nan Huang, Xu Cao et al. — [Thinking in Pictures: A Systematic Benchmark for Reasoning-driven Image Generation](http://arxiv.org/abs/2609.02864v1)
  <details><summary>📄 Abstract</summary>
  Recent advancements in unified generative models (UGMs) and world simulators have achieved unprecedented results in visual perception and synthesis. However, these models primarily rely on surface-level event alignment, leaving the capacity for high-level visual reasoning underexplored. True visual generative intelligence demands "Reasoning-to-Generation", an ability to infer latent rules from visual inputs and manifest solutions through precise, logically constrained visual outcomes. We introdu...
  </details>

- **2026-09-02** — Zihao Lu, Radu Timofte, Marcos V. Conde — [Benchmarking RAW and RGB Restoration in Image Signal Processors](http://arxiv.org/abs/2609.02831v1)
  <details><summary>📄 Abstract</summary>
  Modern cameras transform RAW sensor measurements into sRGB images through an image signal processor (ISP). We benchmark two placements for blind restoration around a fixed ISP: (A) pre-ISP restoration in the RAW domain and (B) post-ISP restoration in the sRGB domain. The benchmark covers four smartphone device groups, two learned ISPs, three degradation regimes--noise, blur, and joint noise and blur--, and several representative RAW and RGB restoration models. Our results show that placement alo...
  </details>

- **2026-09-02** — Hao Zhou, Mandar Kulkarni, Hao Chen et al. — [Large Language Models (LLMs) for Telecom Root Cause Analysis (RCA): A Structured Reasoning Framework for Evidence-Grounded Diagnosis](http://arxiv.org/abs/2609.02805v1)
  <details><summary>📄 Abstract</summary>
  Root cause analysis (RCA) is a critical task in telecom network operations, but diagnosing performance degradations in modern 5G and emerging 6G networks remains challenging due to complex cross-layer dependencies. While large language models (LLMs) offer promising capabilities for reasoning and knowledge integration, directly applying vanilla LLMs to telecom RCA often leads to hallucination, unstable reasoning, and poor alignment with structured network evidence. This work first reviews the evo...
  </details>

- **2026-09-02** — Giovanni Dispoto, Marcello Restelli, Carmine Ventre — [Eliciting ESG Preferences for Reinforcement Learning-Based Portfolio Optimization](http://arxiv.org/abs/2609.02677v1)
  <details><summary>📄 Abstract</summary>
  Modern portfolio management increasingly demands a balance between traditional risk-adjusted returns and strict Environmental, Social, and Governance (ESG) mandates. Current Reinforcement Learning (RL) approaches typically optimize for a single ESG provider, neglecting the significant divergence in rating methodologies across the industry and the unintuitive nature of manually weighting conflicting objectives. This paper addresses these limitations by formulating ESG-aware portfolio optimization...
  </details>

- **2026-09-02** — Thanh-Khoi Nguyen, Thien-Phuc Tran, Minh-Triet Tran — [Query Rewriting for Complex Object Segmentation in 4D Gaussian Representations](http://arxiv.org/abs/2609.02664v1)
  <details><summary>📄 Abstract</summary>
  Recent 4D Gaussian representation frameworks have demonstrated strong performance in language-guided dynamic scene understanding. However, these methods remain highly sensitive to verbose and narrative-style queries that contain noisy contextual information. In this paper, we investigate the impact of query rewriting for complex object segmentation in 4D Gaussian representations. Inspired by recent findings in retrieval-augmented language models and keyword-guided query reformulation, we propose...
  </details>

- **2026-09-02** — Kenichi Fujita, Yusuke Ijima — [Scalable Direction-Following TTS via Voice Impression-Guided Pseudo Triplet Construction](http://arxiv.org/abs/2609.02623v1)
  <details><summary>📄 Abstract</summary>
  Voice actors often re-read the same script while modifying their delivery in response to performance directions. We study this setting as direction-following TTS, where a system generates a new utterance that reflects a given direction relative to a reference utterance while preserving speaker identity and linguistic content. A key challenge is the lack of training data capturing such relative modifications. To address this, we propose a scalable pseudo-triplet construction pipeline that generat...
  </details>

- **2026-09-02** — Xingzu Zhan, Lin Gu, Ruogu Fang — [AffectDelta: Beyond Emotion Labels for Image Editing](http://arxiv.org/abs/2609.02616v1)
  <details><summary>📄 Abstract</summary>
  Emotion-driven image editing aims to evoke a specified target emotion by modifying emotion-relevant visual cues in a source image, while preserving the overall composition and semantic-structural coherence of the original scene. Existing scene-level editors typically specify the target with a single emotion category and often learn visual transformations from operation-level text instructions. A category collapses a mixed affective endpoint into one dominant label, while language cannot precisel...
  </details>

- **2026-09-02** — Pawel Struski, Jakub Swistak, Inez Okulska et al. — [Competitive Market Behavior of LLMs](http://arxiv.org/abs/2609.02580v1)
  <details><summary>📄 Abstract</summary>
  Large language models (LLMs) are increasingly deployed as economic agents, yet there is little evidence whether LLM agents are suited for participating in market mechanisms designed for humans, and whether these mechanisms deliver desired outcomes when faced with LLM agents. We address this question by replicating seminal economic experiments, replacing human subjects with LLM agents. We place agents in a double auction environment, which is a widely-used market mechanism. We check whether such ...
  </details>

- **2026-09-02** — Leon Fröhling, Jens Rupprecht, Markus Strohmaier et al. — [When Persona Attributes Improve Population Alignment in Large Language Models](http://arxiv.org/abs/2609.02526v1)
  <details><summary>📄 Abstract</summary>
  Large Language Models (LLMs) are increasingly used to predict the responses of human participants in survey panels. Towards that goal, persona prompting has recently emerged as a technique to inform and align large pretrained language models. Persona prompting refers to the practice of using short textual descriptions of 'personas' in prompts to steer the LLM's generations. Personas describe individuals through different attributes such as their socio-demographics, attitudes, or behaviors, with ...
  </details>

- **2026-09-02** — Cristina Pignotti, Yu-Qing Wang — [Exponential Consensus and Flocking in Multi-Agent Systems with Infinite Fading Memory](http://arxiv.org/abs/2609.02454v1)
  <details><summary>📄 Abstract</summary>
  In this paper, we study the emergent collective dynamics of multi-agent systems driven by infinite distributed fading memory of Volterra type. We establish a unified theoretical framework covering both first-order opinion consensus dynamics and second-order velocity alignment flocking kinematics. By introducing Dafermos past-history transformations, the governing integro-differential systems are reformulated into dynamical systems on an extended product Hilbert spaces. For first-order dynamics, ...
  </details>

- **2026-09-02** — Juntao Wei, Yangming Zhou, Zhibin Jiang et al. — [LLM-Driven Joint Evolution of Coupled Heuristics Components for Routing Optimization](http://arxiv.org/abs/2609.02353v1)
  <details><summary>📄 Abstract</summary>
  Heuristic design for combinatorial optimization remains heavily reliant on expert knowledge, while existing large language model (LLM)-enhanced evolutionary methods typically evolve isolated algorithmic components, even when one determines the search state on which another operates. This paper proposes LLM-driven Heuristic Components Joint Generation (LLM-HCJG), a population-based framework that jointly generates and co-evolves interdependent heuristic components under a shared design blueprint....
  </details>

- **2026-09-02** — Zhao Ji, Wenqing Chen, Zhixuan Chu et al. — [SALA: Semantic-Aware Logical Alignment for Complex Reasoning in In-Context Learning](http://arxiv.org/abs/2609.02336v1)
  <details><summary>📄 Abstract</summary>
  Effective in-context learning (ICL) for complex reasoning relies on selecting the right demonstrations. Traditional retrieval methods based on surface similarity fail to capture the underlying problem-solving logic. Recent logic-based methods address this by matching predefined reasoning steps, but the rigid rules and exact-match criteria is improper to handle flexible or diverse reasoning processes. To address the problem, we propose SALA, a Semantic-Aware Logical Alignment framework. Instead o...
  </details>

- **2026-09-02** — Quansheng Hu, Qin Sun, Qiansen Dai et al. — [YesTrack: Referring Multi-Object Tracking via MLLM-based Yes/No Verification](http://arxiv.org/abs/2609.02318v1)
  <details><summary>📄 Abstract</summary>
  Referring multi-object tracking (RMOT) aims to track every instance in a video that matches a given language expression. Despite the recent integration of multimodal large language models (MLLMs) to enhance generalization, existing methods predominantly relegate them to the role of caption generators, necessitating external modules for final decision-making. This paradigm not only introduces extra latency but also severely underutilizes the inherent vision-language alignment capabilities of MLLM...
  </details>

- **2026-09-02** — Axel Ahlqvist, Richard Guan, Juan-Pablo Rivera et al. — [Improving Evaluation Realism with Inference-Time Compute and Deployment Scaffolds](http://arxiv.org/abs/2609.02302v1)
  <details><summary>📄 Abstract</summary>
  A core obstacle to alignment evaluation is evaluation awareness: capable models can tell when they are being tested rather than deployed, weakening the conclusions a safety evaluation can support. We present two techniques that make simulated alignment evaluations harder to distinguish from real deployments. Our first technique, critique refinement, spends additional inference-time compute on each simulator action: the simulator generates multiple candidate actions, refines them using feedback f...
  </details>

- **2026-09-02** — Jie Ding, Rui Sun, Xinyuan Zhang et al. — [APEx: Distillation of Agent Procedural Experience for Adaptive Deep Research Question Answering](http://arxiv.org/abs/2609.02253v1)
  <details><summary>📄 Abstract</summary>
  Deep research agents augment large language models with external tools to answer complex, long-horizon questions through multi-turn reasoning. Learning from prior experience is crucial for continual improvement, yet existing methods either retrieve verbose task-specific traces that burden decision-making, or distill procedural skills that remain decoupled from downstream policy adaptation. We propose APEx, a hierarchical experience utilization framework that organizes interaction history into in...
  </details>

- **2026-09-02** — Fan Yuxuan, Huang Miaojun, Zhang Haimei et al. — [PhoenixNest-Video: Evidence-Grounded Multimodal Agent Framework for Automated Video Interview Assessment](http://arxiv.org/abs/2609.02231v1)
  <details><summary>📄 Abstract</summary>
  Interview assessment requires per-criterion judgments grounded in behavioral evidence, yet surging applicant volumes have made human-only evaluation costly and inconsistent, while existing AI approaches yield opaque scores without traceable rationale. We introduce PhoenixNest-Video, an evidence-grounded multimodal agent framework for automated video interview assessment. It builds a semantic video graph as structured working memory, performs rubric-conditioned retrieval with cross-modal verifica...
  </details>

- **2026-09-02** — Ziqi Zhang, Emmanuele Chersoni, Mohammad Momenian — [Do Cantonese-Adapted Language Models Better Predict Cantonese Reading? A Cross-Model Eye-Tracking Evaluation](http://arxiv.org/abs/2609.02163v1)
  <details><summary>📄 Abstract</summary>
  Information-theoretic measures derived from autoregressive language models are widely used to characterize the expectations that shape human reading, but whether language-variety-specific training improves such psycholinguistic alignment remains unclear. This question is still open for Cantonese, where recent NLP evaluations reported mixed benefits from Cantonese-specific training relative to Mandarin-oriented or general-purpose models. Using naturalistic Cantonese eye-tracking data, we compare ...
  </details>

- **2026-09-02** — Hanyang Cao, Yuetong Fang, Taesoo Kwon et al. — [Unified Motion Retargeting for Humanoids with Learned Point Cloud Correspondence](http://arxiv.org/abs/2609.02134v1)
  <details><summary>📄 Abstract</summary>
  Humanoid learning increasingly relies on transforming vast and diverse human motion data into high-quality robot reference trajectories. However, retargeting human motion to humanoid robots is challenging due to substantial differences in morphology, degrees of freedom, joint ranges, and kinematic constraints between humans and robots. Existing retargeting methods typically address these differences by defining human-robot correspondence through hand-crafted sparse keypoints or body-part pairs. ...
  </details>

- **2026-09-02** — Yikai Zhao, Saurabh Pandey, Pradeep Kumar Misra — [A Tri-Agent Framework for Evaluating and Aligning Question Clarification Capabilities of Large Language Models](http://arxiv.org/abs/2609.02054v1)
  <details><summary>📄 Abstract</summary>
  Large Language Models (LLMs) are increasingly deployed in interactive systems where understanding user intent precisely is paramount. A key capability for such systems is effective question clarification, especially when user queries are ambiguous or underspecified. This paper introduces a novel tri-agent framework for the robust evaluation of an LLM's ability to engage in clarifying dialogue. Our framework comprises three distinct LLM-based agents: (1) a Question Clarifying Agent (QCA), the sys...
  </details>

- **2026-09-02** — Ziyue Piao, Isabelle Cossette, Marcelo M. Wanderley — [Reconciling Kinesthetic Mismatches: A Somatic Alignment Mindset for Musical Body Transformation](http://arxiv.org/abs/2609.01981v1)
  <details><summary>📄 Abstract</summary>
  Mastering musical performance requires precise multisensory coordination, yet learners encounter a kinesthetic mismatch, which is a discrepancy between the internal perception of an action and the actual physiological state of the body. While multisensory Body Transformation Experiences (BTE) provide tools to bridge this gap, existing designs often focus on external correction rather than internal alignment. To address this, we propose the Somatic Alignment Mindset (SAM), a conceptual lens that ...
  </details>

- **2026-09-01** — You-Lin Chen, Kyoungjun Park, Bin Xu et al. — [MERGED: Multimodal Entity Resolution via Generated Expert Reasoning Distillation](http://arxiv.org/abs/2609.01913v1)
  <details><summary>📄 Abstract</summary>
  In product entity resolution, relationship definitions constantly evolve with business needs, yet adapting to each change traditionally requires slow, costly human annotation that is often noisy and carries no reasoning. Large vision-language models (VLMs) prompted zero-shot can adapt to a new definition immediately and supply the reasoning that human labels lack, but their cost and latency are prohibitive at production scale. We present MERGED, a distillation framework that transfers not just l...
  </details>

- **2026-09-01** — Judita Preiss, Yunhan Yang — [Guiding LLM Peer Reviewers: The Impact of Score Anchors on Review Evidence and Accuracy](http://arxiv.org/abs/2609.01905v1)
  <details><summary>📄 Abstract</summary>
  Large language models (LLMs) are increasingly used for research quality evaluation, with prior work exploring their scoring accuracy and the plausibility of review rationales. However, less is known about whether external score guidance changes the evidence presented in the generated review as well as the final score. This study uses 98 Allied Health Professions research outputs submitted for internal REF-style assessment, with specialist human review reports and adjudicated 1-4 reference scores...
  </details>

- **2026-09-01** — Yalda Daryani, Miranda Bogen, Madeleine I. G. Daepp — [Accurate in space, unreliable in time: how LLMs represent national cultural change](http://arxiv.org/abs/2609.01902v1)
  <details><summary>📄 Abstract</summary>
  Assessments of cultural alignment have become an important part of the development and improvement of large language models (LLMs). However, the majority of the evaluations treat culture as a single snapshot, investigating only whether a model represents a society accurately at the current time. Research in cultural psychology shows that cultural values change at different rates and directions over time. Therefore, a "culturally aware" model should capture not only where a culture is today but a...
  </details>

- **2026-09-01** — Weiming Li, Catarina Barata, Miguel Constante et al. — [Candidate Generation and Definition-Guided Verification for Sentence-Level Depression Symptom Recognition](http://arxiv.org/abs/2609.01833v1)
  <details><summary>📄 Abstract</summary>
  Sentence-level recognition of depression symptoms is challenging because similar expressions can differ in symptom relevance, and language-model inference is insufficiently grounded in diagnostic definitions. This study proposes a two-stage framework separating symptom-candidate generation from definition-grounded verification. A contrastively fine-tuned sentence encoder generates a symptom candidate per sentence, and a fine-tuned language model verifies whether the candidate is present or absen...
  </details>

- **2026-09-01** — Hatim Chergui, Carolina Fernández-Martínez, Mehdi Bennis et al. — [Agents That Model Agents: Five Principles Toward a Theory of Mind for 6G Networks](http://arxiv.org/abs/2609.01779v1)
  <details><summary>📄 Abstract</summary>
  Future 6G networks will rely on Large Language Model (LLM) agents to manage the Radio Access Network (RAN). However, current architectures assume inter-agent messages convey objective facts. A message is instead a \emph{trace} of the sender's reasoning: it carries a subjective conclusion, so a syntactically valid report can propagate an AI hallucination and trigger a cascading outage invisible to protocol validation. Reading such a trace requires a Theory of Mind (ToM)---before acting, the recei...
  </details>

- **2026-09-01** — Aarthy Nagarajan — [Slow-Fast Brain-Computer Interfaces: Preventing Neuroadaptive Overfitting in AI-Mediated Neural Interfaces](http://arxiv.org/abs/2609.01767v1)
  <details><summary>📄 Abstract</summary>
  Artificial intelligence (AI) is transforming brain-computer interfaces (BCIs) from task-specific neural decoders into adaptive systems that complete language, smooth movement, regulate rehabilitation support and adjust stimulation. These capabilities can increase speed, fluency, usability and clinical reach, yet conventional performance metrics may overlook losses in intent fidelity, authorship, agency, therapeutic challenge and durable clinical benefit. I define neuroadaptive overfitting as a c...
  </details>

- **2026-09-01** — Jianzhong You, Yuan Gao, Chris McIntosh — [AlphaRAD: Grounded Zero-Shot Classification in Chest Radiology via $α$-Corrected Binary Cross Entropy and Factorized Latent Supervision](http://arxiv.org/abs/2609.01757v1)
  <details><summary>📄 Abstract</summary>
  Vision-Language Pretrained Models (VLPMs) offer a scalable path to open-vocabulary chest radiology understanding, yet two aspects remain underexplored: how structured clinical semantics extracted from medical reports can reduce in-batch noise during contrastive learning, and how cross-modal fusion can be designed to produce more faithful spatial grounding without added complexity. We introduce AlphaRAD, addressing these opportunities through two contributions. First, we construct a large-scale s...
  </details>

- **2026-09-01** — Seungwoo Jung, Dohyeok Kwon, Seungmin Cha et al. — [Residual Sparsification via Output Importance for Compressing Mixture-of-Experts LLMs](http://arxiv.org/abs/2609.00575v2)
  <details><summary>📄 Abstract</summary>
  Mixture-of-experts (MoE) architectures scale large language models efficiently, but they demand massive GPU memory. To cope with such demand, models are commonly compressed to reduce their memory footprint. Residual sparsification is a representative compression technique that decomposes each projection matrix of an expert into a shared base matrix and per-expert residual matrix, and then compresses the residuals. Existing sparsification methods compress each residual matrix independently by min...
  </details>

- **2026-09-01** — Yitong Guo, Xiaoyi Chen, Siyuan Zhang et al. — [When Safety Routing Breaks: Understanding Alignment Fragility under Benign Fine-Tuning](http://arxiv.org/abs/2609.01455v1)
  <details><summary>📄 Abstract</summary>
  Benign fine-tuning severely weakens the safety alignment of large language models (LLMs), so we study why refusal behavior is so fragile. While prior work often attributes this failure to gradient conflict, we propose a fundamentally different Fisher-geometric explanation: safety Fisher is low-rank, and alignment makes the safety geometry flatter while preserving an output-routing pathway. After 100 benign fine-tuning examples, this pathway is selectively re-sharpened in output-side MLP modules,...
  </details>

- **2026-09-01** — Dirk Bergemann, Andrew Koh, Stephen Morris — [Mechanism Design for Alignment and Control](http://arxiv.org/abs/2609.01595v1)
  <details><summary>📄 Abstract</summary>
  We develop a framework for mechanism design with AI agents whose alignment (preferences) and capabilities (feasible actions and information) are unknown. We want such agents to act on our behalf so mechanisms must incentivize both honesty and obedience. A one-sided imitation structure---capabilities can be concealed but not counterfeited---yields a revelation principle, a characterization of implementable policies via nested cyclical monotonicity, and conditions under which eliciting higher-orde...
  </details>

- **2026-09-01** — Jing Xiao, Xinhai Chen, Qinglin Wang et al. — [Gradient-Update Mismatch: Rethinking Conflict-Free Training of Physics-Informed Neural Networks](http://arxiv.org/abs/2609.01558v1)
  <details><summary>📄 Abstract</summary>
  Training Physics-Informed Neural Networks (PINNs) requires jointly optimizing physics residual and initial/boundary condition loss terms, which often induce conflicting gradients. Gradient surgery methods mitigate this issue by constructing directions from loss-specific gradients to reduce conflict before optimizer transformation. However, even when the constructed direction is conflict-free, this property may not be preserved after optimizer transformation. Let $a_t$ denote the direction constr...
  </details>

- **2026-09-01** — Wenqi Pei, Henry Hengyuan Zhao, Yilai Liu et al. — [TempCloze: Can Video-LLMs Identify the Missing Middle?](http://arxiv.org/abs/2609.01515v1)
  <details><summary>📄 Abstract</summary>
  Temporal reasoning benchmarks for Video-LLMs are often mediated by language, leaving room for linguistic shortcuts from option wording, answer correlations, or language priors. To reduce such shortcuts, we introduce TempCloze, a video cloze benchmark for evaluating visual temporal reasoning in Video-LLMs. Given the beginning and ending clips of a video, models must identify the true missing middle from four candidates. TempCloze contains 1,521 carefully filtered videos from seven sources, mainly...
  </details>

- **2026-09-01** — Thibaut Thonet, Jos Rozen, Laurent Besacier — [Ready to Speak: Aligning LLMs for TTS-Friendly Text Generation](http://arxiv.org/abs/2609.01246v1)
  <details><summary>📄 Abstract</summary>
  Current Large Language Models (LLMs) are primarily optimized for written text, often producing outputs that are grammatically correct and helpful yet poorly suited for spoken delivery via Text-to-Speech (TTS). In this work, we study how to make LLMs natively generate TTS-friendly text, which we frame as a preference alignment problem: instead of relying on downstream rewriting modules, we directly align LLMs to generate text optimized for spoken delivery. We introduce two preference datasets spa...
  </details>

- **2026-09-01** — Frederic Sadrieh, Michal Štefánik — [Prompt-Robust Language Models: Which Training Strategies Work?](http://arxiv.org/abs/2609.01217v1)
  <details><summary>📄 Abstract</summary>
  Despite their strong performance, large language models remain highly sensitive to prompt formulation. Prior work addresses this through refined data construction or through dedicated robustness objectives. We reproduce and compare these strategies under controlled conditions, and measure how effective they are in addressing models' prompt sensitivity. We find the current robustness fine-tuning methods improve over standard fine-tuning and in-context learning, but the best-to-worst prompt gap re...
  </details>

- **2026-09-01** — Francois Meyer — [Subword Segmental BabyLMs: Learning to Tokenise for Sample-Efficient Pretraining](http://arxiv.org/abs/2609.01151v1)
  <details><summary>📄 Abstract</summary>
  In the standard LM training pipeline, subword tokenisation is applied as a preprocessing step. Subword segmental language modelling is an alternative paradigm in which tokenisation is learned during training, allowing the model to discover subword units that optimise its training objective. In this paper, we present our submission to the 2026 BabyLM Challenge, for which we develop two new subword segmental LMs: SubSegGPT and SubSegDeBERTa. SubSegGPT is a decoder-only model that learns tokenisati...
  </details>

- **2026-09-01** — Chujie Qin, Zilong Zhang, Zewei Chang et al. — [Dotting the Eye: An Intent-Driven Image Retouching Agent for Visual Focus Enhancement](http://arxiv.org/abs/2609.01148v1)
  <details><summary>📄 Abstract</summary>
  Image retouching is commonly formulated as enhancing overall visual quality through color adjustment, but in practice, it also serves to emphasize visual focus by guiding viewers' attention toward a specific subject or region. Achieving such focus-oriented retouching is inherently challenging, as it requires well-coordinated global and local adjustments to manipulate perceptual saliency while maintaining visual naturalness. This intricate process typically demands substantial professional expert...
  </details>

- **2026-09-01** — Jiming Feng, Junliang Li — [Scaled Idempotence in Transformer Attention: Paired OV Geometry and Shared-Value Algebras](http://arxiv.org/abs/2609.01129v1)
  <details><summary>📄 Abstract</summary>
  We identify a recurrent algebraic regularity in Transformer attention: a sparse subset of effective OV operators $T=OV^\top$ nearly closes under composition, $T^2\approxαT$. Across six pretrained endpoints spanning 2.8B--235B parameters, 3.98--8.00% of heads reach squared closure alignment $\mathcal{P}\geq0.9$, while no matched within-layer O/V mismatch does. An exact principal-coordinate factorization, $T=Q_OKQ_V^\top$ and $T^2=Q_O(KDK)Q_V^\top$, separates within-support transport from read--wr...
  </details>

- **2026-09-01** — Mustafa Yasir Altunhan, Hüseyin Özgür Kamalı, Eray Tüzün — [Fine-Tuning Large Language Models to Classify Pull Request-Issue Alignments: Going Beyond Prompting](http://arxiv.org/abs/2609.01087v1)
  <details><summary>📄 Abstract</summary>
  Context: Accurate alignment between pull requests (PRs) and corresponding issues is crucial for efficient software development and maintaining code quality, as misalignments can reduce traceability, hinder defect localization, and decrease maintainability.   Objective: This study aims to improve automated PR-issue alignment classification by leveraging fine-tuned large language models (LLMs) across multiple alignment categories, and conducts interpretability analysis to investigate the effects o...
  </details>

- **2026-09-01** — Sebastian Steindl, Nikos Voskarides, Alberto Gasparin et al. — [Post-hoc Alignment of LLM-judges to Human Judgment Distribution](http://arxiv.org/abs/2609.01073v1)
  <details><summary>📄 Abstract</summary>
  The LLM-as-a-judge (LLMaJ) framework offers a cost-effective and reproducible solution for automatic evaluation. However, current evaluation practices typically compare LLMaJ judgments against aggregated ground-truth labels, overlooking the valuable information contained in Human Label Variation (HLV). Inspired by an increasing line of work that proposes to leverage HLV, we systematically study LLMaJ performance on predicting both a single, aggregated ground truth hard-label and unaggregated sof...
  </details>

- **2026-09-01** — Ziyad Benomar, Weronika Łajewska, Leonardo Perelli et al. — [Data-Driven Persona-Conditioned Agents for A/B Test Simulation](http://arxiv.org/abs/2609.01038v1)
  <details><summary>📄 Abstract</summary>
  A/B testing is the gold standard for evaluating product changes, but each experiment requires real user traffic, engineering effort, and weeks of measurement. We propose a simulation framework that predicts A/B test outcomes using LLM-powered agents conditioned on data-driven personas grounded in real user behavioral signals. Unlike prior work that relies on synthetic or rule-based personas, our agents are constructed from anonymized behavioral data-activity patterns, engagement signals, and inf...
  </details>

- **2026-09-01** — Aravindhan Srinivasan, Marcello Ortaggio — [Charging higher-dimensional spacetimes with a generalized Kerr-Schild transformation](http://arxiv.org/abs/2609.01012v1)
  <details><summary>📄 Abstract</summary>
  We explore the construction of higher-dimensional Einstein-Maxwell(-Chern-Simons) solutions from vacuum seeds by means of a generalized Kerr-Schild transformation along a geodesic null vector field $\mathbf{k}$. Assuming the vector potential $\mathbf{A}$ to be aligned with $\mathbf{k}$, and $\mathbf{k}$ to be a Weyl aligned null direction satisfying the ``optical constraint'', we arrive at three distinct branches of solutions. If $\mathbf{k}$ is expanding and twisting, then its shear must vanish...
  </details>

- **2026-09-01** — Rania Elbadry, Ahmed Heakl, Saeed Almheiri et al. — [Right Frame, Wrong Rule: Cultural Cues Expose the Financial Knowledge Gap They Were Meant to Close](http://arxiv.org/abs/2609.00999v1)
  <details><summary>📄 Abstract</summary>
  When a question has valid answers under different normative frameworks, a language model must decide which framework to use and whether it can answer correctly within it. We call this setting normative pluralism and study it in Islamic finance using a four-choice taxonomy that separates framework selection from within-framework correctness. This separation reveals the stereotype trap: a cultural cue steers a model toward one framework, but the model selects an incorrect answer within that framew...
  </details>

- **2026-09-01** —  TGR Team, Lei Cheng, Haonan Hu et al. — [TGR: Advancing Industrial Recommendation from Generative-Paradigm Ranking toward Unified Generation and Reasoning](http://arxiv.org/abs/2609.00986v1)
  <details><summary>📄 Abstract</summary>
  Industrial recommender systems typically rely on cascaded retrieval, pre-ranking, ranking, and reranking stages, whose separately optimized models limit scaling, fragment decision making, and lack semantic knowledge and reasoning. We present TGR (Tencent Generative Recommendation), an industrial framework that advances recommendation toward the generative paradigm along three coupled directions. TGR-GenRank upgrades ranking through CCFormer, which combines unified feature tokenization, a scalabl...
  </details>

- **2026-09-01** — Jeonghyeok Do, Seungchul Lee, Munchurl Kim — [ReFlowSET: Representation-Aligned Latent Flow Matching for SAR-to-EO Image Translation](http://arxiv.org/abs/2609.00968v1)
  <details><summary>📄 Abstract</summary>
  SAR-to-EO image translation aims to generate electro-optical (EO) imagery from synthetic aperture radar (SAR) observations. Existing latent diffusion approaches typically inherit a predetermined autoencoder, although reconstruction fidelity can vary substantially across codecs and modalities. Because the latent codec affects the round-trip preservation of both SAR conditions and EO targets, codec selection constitutes a fundamental design choice; nevertheless, existing methods largely rely on co...
  </details>

- **2026-09-01** — Zhixin Wang, Chengzheyi Yao, Leyuan Liu et al. — [VerNav: Verifier-First Low-Latency Vision-and-Language Navigation](http://arxiv.org/abs/2609.00920v1)
  <details><summary>📄 Abstract</summary>
  Vision-and-Language Navigation (VLN) requires an agent to navigate through unseen 3D environments according to natural-language instructions. Explicit reasoning can improve instruction understanding and semantic grounding, but autoregressive generation at every step accumulates large decision-stage latency over multi-step navigation. We propose VerNav, a verifier-first framework for low-latency LLM-based VLN. The verifier reduces decision-stage latency by replacing per-step autoregressive genera...
  </details>

- **2026-09-01** — Zhiyu Ye, Yue Sun, Limiao Zou et al. — [A multicenter benchmark and clinically structured metric for coronary CTA report generation](http://arxiv.org/abs/2609.00909v1)
  <details><summary>📄 Abstract</summary>
  Reliable evaluation of automated coronary computed tomography angiography (CCTA) report generation requires standardized multicentre benchmarks and clinically structured metrics. We established a four-centre benchmark comprising 3,021 CCTA series from 818 patient-report pairs to evaluate seven open-source three-dimensional vision-language models. We developed CSM$_{\text{CCTA}}$, a clinically structured metric for CCTA report evaluation, with patient-, vessel-, and segment-level variables define...
  </details>

- **2026-09-01** — Guanqiao Chen, Di Wang, Lijie Hu — [SFAD: Speculative Factuality-Aware Decoding](http://arxiv.org/abs/2609.00796v1)
  <details><summary>📄 Abstract</summary>
  As one of the most critical challenges in large language models, contextual faithfulness directly determines their reliability in knowledge-intensive applications. This task is particularly challenging as it requires balancing factual consistency with generation efficiency. Contrastive decoding methods require dual forward passes (with and without context) to compare model outputs, doubling inference computational overhead, while post-training alignment demands extensive reinforcement learning w...
  </details>

- **2026-09-01** — Zeen Zhu, Zhuo Li, Weiyang Guo et al. — [Trust Your Guide Only When Certain: Uncertainty-Aware Sparse Alignment at Inference Time](http://arxiv.org/abs/2609.00624v1)
  <details><summary>📄 Abstract</summary>
  A prominent paradigm in inference-time alignment employs lightweight supervisors to steer Large Language Models (LLMs). Through empirical analysis, we identify a structural mismatch in this paradigm: weak supervisors exhibit pervasive high entropy across the vast majority of tokens, yet prevailing dense intervention approaches mandate supervision at every decoding step. This leads to frequent low-confidence interventions that can disrupt valid base-model reasoning and incur substantial utility c...
  </details>

- **2026-09-01** — Pranshav Gajjar, Vijay K Shah — [CRAFT: Fine-Tuning Pre-hoc Explainability in AI-native 6G RAN](http://arxiv.org/abs/2609.00590v1)
  <details><summary>📄 Abstract</summary>
  The next generation of mobile networks is envisioned as fully AI-native, with AI-RAN architectures embedding small language models (SLMs) to perform reasoning over real-time telemetry. The state-of-the-art training paradigms for telecom LLMs, exemplified by RANSTRUCT-style supervised fine-tuning (SFT) on curated instruction data, are limited to post hoc rationalization. Here, the explanations, when produced at all, are generated after or independently of the decision, leaving the decision proces...
  </details>

- **2026-09-01** — Cris Huynh — [Consistency Without Alignment: Item-Sensitive Language Models Indistinguishable From Random](http://arxiv.org/abs/2609.00576v1)
  <details><summary>📄 Abstract</summary>
  Item-sensitivity, defined as whether a model's choice depends on the specific input rather than on its own output prior, is widely reported as evidence of task competence. We show this evidence is necessary but not sufficient using a forced-choice signalling task abstracted from the board game Deception: Murder in Hong Kong. In this environment, the reference points against which a coordinate should be judged (a fit-maximising strategy, a posterior-maximising strategy, and uniform random selecti...
  </details>

- **2026-09-01** — Seungwoo Jung, Dohyeok Kwon, Seungmin Cha et al. — [Residual Sparsification via Output Importance for Compressing Mixture-of-Experts LLMs](http://arxiv.org/abs/2609.00575v1)
  <details><summary>📄 Abstract</summary>
  Mixture-of-experts (MoE) architectures scale large language models efficiently, but they demand massive GPU memory. To cope with such demand, models are commonly compressed to reduce their memory footprint. Residual sparsification is a representative compression technique that decomposes each projection matrix of an expert into a shared base matrix and per-expert residual matrix, and then compresses the residuals. Existing sparsification methods compress each residual matrix independently by min...
  </details>

- **2026-09-01** — Jingshen Zhang, Shaoyang Xu, Wenxuan Zhang — [Aligned but Flattened: Analyzing the Trade-off between Cultural Alignment and Diversity in LLMs](http://arxiv.org/abs/2609.00565v1)
  <details><summary>📄 Abstract</summary>
  Cultural fine-tuning has become the de facto paradigm for building culture-aware large language models (LLMs), yet existing optimization exclusively for alignment scores provides an incomplete portrait of cultural fidelity by systematically obscuring inherent cultural diversity. This unidimensional evaluation lens prompts a fundamental question: do models genuinely perceive distinct cultural nuances, or do they merely memorize dominant cultural values? To address this, we propose a synergistic e...
  </details>

- **2026-09-01** — Yijun Chen, Yaqi Zheng, Yanya Li et al. — [EM^2Mem: Event-Centric Multimodal Memory for Large Language Models](http://arxiv.org/abs/2609.00551v1)
  <details><summary>📄 Abstract</summary>
  Multimodal memory offers a scalable interface for long-video question answering, but existing methods often retrieve captions, frames, transcripts, summaries, or graph facts as isolated fragments. Although searchable, such fragments are not generation-ready: language models must reconstruct cross-modal and temporal alignments at inference time, when context is limited and attribution is difficult. We propose EM^2Mem, an event-centric multimodal memory framework that binds heterogeneous evidence ...
  </details>

- **2026-09-01** — Clinton Enwerem, John S. Baras, Calin Belta — [Does Imitation Learning Preserve Temporal Robustness in Dexterous Manipulation? An Expert-Learner Comparison Across Task Execution Speeds](http://arxiv.org/abs/2609.01453v1)
  <details><summary>📄 Abstract</summary>
  Dexterous manipulation policies learned by imitation are typically evaluated for robustness to variation in scenes, objects, or instructions, but their performance across task execution speeds is less often examined. This leaves open how much temporal robustness a learner retains relative to the expert it imitates. We compare an expert and learner under the same task conditions, initial-condition draws, and speedup factors. We instantiate the evaluation in ParcelStow, a contact-rich task in whic...
  </details>

- **2026-09-01** — Yiwen Jiang, Yang Deng, Stephanie Fong et al. — [VIBE-Bench: Evaluating Personalized Large Language Models When Profiles Don't Mean Preferences](http://arxiv.org/abs/2609.00921v1)
  <details><summary>📄 Abstract</summary>
  Personalized Large Language Models (PLLMs) aim to tailor responses to individual users, where a central challenge is preference reasoning: inferring query-relevant preferences from user-related history. Existing benchmarks, however, largely assume that such preference can be retrieved from semantically related history. We study an underexplored but practically important regime, profile-preference conceptual misalignment (PRCM), where observable profile cues and query-specific preferences lie in ...
  </details>

- **2026-08-31** — Yuzhi Lai, William Marx, Shenghai Yuan et al. — [Beyond Object Selection:Markerless Gaze-based Robot Placement at Arbitrary Position](http://arxiv.org/abs/2609.00478v1)
  <details><summary>📄 Abstract</summary>
  Gaze-based assistive manipulation typically supports object selection, while arbitrary-position placement requires accurate spatial alignment between the headset and robot. However, for gaze-based manipulation, pose accuracy does not necessarily translate into task accuracy: translational and rotational errors jointly affect the transformed gaze ray and may compensate for each other. To study cross-device alignment from this task-oriented perspective, we present a markerless interaction framewor...
  </details>

- **2026-08-31** — Francisco Galuppo Azevedo, Clarissa Lima Loures — [Can LLMs Use Relational Transformer Embeddings?](http://arxiv.org/abs/2609.00457v1)
  <details><summary>📄 Abstract</summary>
  Injecting frozen relational-encoder embeddings as soft tokens into a large language model (LLM) is a conceptually appealing fusion strategy: the encoder handles multi-table structure, the LLM handles language and reasoning, and no lossy text serialization is required. We test this hypothesis concretely by injecting embeddings from a frozen Relational Transformer (RT) into Qwen3.5-4B via a learned MLP projection and LoRA adaptation, trained first with supervised fine-tuning (SFT) on chain-of-thou...
  </details>

- **2026-08-31** — Gokul Srinivasagan, Munir Georges — [Location-Aware Language Models via Secondary Embeddings](http://arxiv.org/abs/2609.00454v1)
  <details><summary>📄 Abstract</summary>
  Pretrained transformer-based language models achieve strong performance across a wide range of NLP tasks but remain limited in encoding geo-locational semantics, leading to suboptimal representations of place names and spatial entities. In this work, we propose a lightweight, model-agnostic approach for injecting geo-spatial awareness into pretrained embeddings without modifying the tokenizer or requiring costly retraining. Our method augments input representations with structured geographic sig...
  </details>

- **2026-08-31** — Mert Yazan — [The Assistant's Ideal Self](http://arxiv.org/abs/2609.00304v1)
  <details><summary>📄 Abstract</summary>
  Models express values and welfare-relevant self-reports, but it is unclear whether these outputs reflect stable preferences or a stable self. We thus introduce a structured elicitation of an assistant's preferred stated ideal self. Thirty-two qualities adapted from five published self-concept instruments are compared exhaustively in a counterbalanced pairwise-choice task, repeated across framings that vary whether improvement is free or costly, who receives the update, and who chooses. Results s...
  </details>

- **2026-08-31** — Athulith Paraselli, Etha Tianze Hua, Ellie Pavlick — [Slow to See, Slow to Suppress: Understanding the Effects of Modality in Context-Memory Conflicts](http://arxiv.org/abs/2609.00293v1)
  <details><summary>📄 Abstract</summary>
  We investigate how vision-language models (VLMs) handle context-memory conflicts; that is, situations in which the model is given information in context that differs from what was stored parametrically during training. We document asymmetric biases: models tend to prefer in-context information about entities which appear in text, but prefer parametric information about entities which appear in images. We relate this asymmetry to the late representational alignment across modalities, showing that...
  </details>

- **2026-08-31** — Daniela Occhipinti, Andrea Piergentili, Marco Guerini — [LLM-as-a-Demographic: Whom Sociodemographic Prompting Helps, and Whom It Hurts](http://arxiv.org/abs/2609.00222v1)
  <details><summary>📄 Abstract</summary>
  Large language models (LLMs) are increasingly used as judges for subjective tasks, where annotators disagree and the relevant question is not only how accurate a judge is, but whose judgments it reproduces. Sociodemographic prompting conditions the judge on an annotator's demographic profile to align its judgments with the corresponding group's. We test whether this alignment emerges distributionally, comparing the predicted label distributions of 23 open-weight LLMs on three subjective tasks ag...
  </details>

- **2026-08-31** — Yu Yuan, Yaoyou Fan, Lili Zhao et al. — [Uncovering and Mitigating Aggregation-Induced Reward Hacking in Multi-Reward Reinforcement Learning](http://arxiv.org/abs/2609.00213v1)
  <details><summary>📄 Abstract</summary>
  Reinforcement learning fine-tuning of large language models increasingly adopts multiple reward dimensions, including verifiable rules, task-specific evaluators, and learned reward models, to provide richer supervision across diverse capabilities. These dimensions are commonly scalarized with fixed aggregation weights. We identify a failure mode in which aggregation itself induces reward hacking: static projection aliases qualitatively different reward profiles into a single scalar, steering opt...
  </details>

- **2026-08-31** — Scott Compton, Arjun Nagendran — [AI Should Not Only Be Helpful. It Should Be Contingent. Artificial Intimacy, Sycophancy, and the Future of Social Learning](http://arxiv.org/abs/2609.00211v1)
  <details><summary>📄 Abstract</summary>
  Conversational artificial intelligence is increasingly embedded in everyday social environments, where it functions as both an informational tool and a source of interpersonal feedback. This perspective introduces contingency, i.e., the degree to which system responses vary with user behavior and its interpersonal consequences, as a central construct for evaluating AI systems. We argue that current alignment approaches, including reinforcement learning from human feedback, tend to prioritize use...
  </details>

- **2026-08-31** — Shiyun Wa, Yifei Wang, Anna G. Green et al. — [Elite-Weighted Supervised Fine-tuning for Goal-Directed Molecular Optimization](http://arxiv.org/abs/2609.00189v1)
  <details><summary>📄 Abstract</summary>
  Goal-directed optimization is essential for steering molecular generators to propose candidates with desired properties. However, it is often implemented with policy-gradient reinforcement learning, which requires a generation-trajectory log-probability whose form depends on the model architecture and generation procedure. This makes an optimizer difficult to reuse across architectures and conditional generative designs. Supervised fine-tuning needs none of that machinery, but its update is driv...
  </details>

- **2026-08-31** — Hamed Babaei Giglou, Jennifer D'Souza, Sören Auer — [Do General NLP Embeddings Capture Ontological Reasoning?](http://arxiv.org/abs/2609.00177v1)
  <details><summary>📄 Abstract</summary>
  General-purpose NLP embedding models perform well on linguistic tasks, but their ability to capture symbolic ontological structure remains unclear. We introduce AVA, a systematic framework for evaluating whether embeddings distinguish logic-sensitive relational semantics in ontologies and knowledge graphs. AVA comprises 171,007 contrastive triplets derived from 163 heterogeneous ontologies using hierarchy inversion, relation substitution, and disjointness injection. Each triplet contains an onto...
  </details>

- **2026-08-31** — Daniel Agyei Asante, Yang Li — [TopoCompress: Long Context Compression via Graph-Wired Semantic Trajectories](http://arxiv.org/abs/2608.30811v2)
  <details><summary>📄 Abstract</summary>
  Long-context compression is essential for reducing the cost and latency of large language model inference. However, existing methods can fragment important evidence, require additional training or alignment, and often depend on the target model for effective compression. We introduce TopoCompress, a training-free and model-agnostic framework that compresses long contexts by selecting coherent semantic spans. TopoCompress first scores each span using dense and lexical query relevance together wit...
  </details>

- **2026-08-31** — Ming Zhang, Kaisen Yang, Shu Yu et al. — [Safin-1: Safety from Within through Memory-Native State Evolution](http://arxiv.org/abs/2609.00092v1)
  <details><summary>📄 Abstract</summary>
  Long-horizon complex tasks require foundation models to accumulate information, maintain internal states, and adapt over extended interactions. Safety should be an intrinsic property of the model itself, rather than a behavioral constraint relying solely on external safeguards or post-hoc alignment such as supervised fine-tuning. This motivates Safety from Within, where safety-relevant capabilities are represented and invoked through the model's native computation. We present Safin-1, a family o...
  </details>

- **2026-08-31** — Avinash Malik — [The Space-Time Transform: Memory-Augmented Control Barrier Functions](http://arxiv.org/abs/2609.00079v1)
  <details><summary>📄 Abstract</summary>
  Control Barrier Functions (CBFs), their High-Order variants (HOCBFs) and Exponential CBFs (ECBFs) are standard geometric tools for enforcing nonlinear safety constraints. CBFs, and their variants, offer an elegant geometric framework for nonlinear safety, yet mathematically, they reduce to continuous-time convolutions restricted by zero-memory kernels. In the presence of high-frequency measurement noise, these memoryless operators act as improper filters, leading to significant control chatterin...
  </details>

- **2026-08-31** — Zhiqin Yang, Jingwen Fu, Yuhan Liu et al. — [Scaling Large Reasoning Models beyond Human Supervision: A Path toward Superintelligence](http://arxiv.org/abs/2608.31075v2)
  <details><summary>📄 Abstract</summary>
  Recent advances in large reasoning models (LRMs) have shown that reinforcement learning with verifiable rewards (RLVR) can substantially improve reasoning in mathematics and code, where outcomes can be checked automatically. Extending this progress to open-ended and agentic tasks remains difficult because reliable rewards are harder to obtain and direct human supervision cannot keep pace with the scale and complexity of model-generated experience. This paper studies how LRMs can continue to impr...
  </details>

- **2026-08-31** — Hamed Babaei Giglou, Sören Auer, Peio Popov et al. — [OntoAligner-Ensemble: Voting-Based Fusion across Heterogeneous Ontology Alignment Techniques](http://arxiv.org/abs/2608.31137v1)
  <details><summary>📄 Abstract</summary>
  Ontology alignment (OA) has evolved through several methodological paradigms, ranging from lexical and structural aligners to knowledge graph embedding (KGE) models and, more recently, Large Language Model (LLM)-based approaches. Although modern OA frameworks provide unified ecosystems for deploying these heterogeneous aligners, mechanisms for systematically reconciling their complementary and sometimes conflicting predictions remain relatively underexplored. We present OntoAligner-Ensemble, a m...
  </details>

- **2026-08-31** — Joonyong Park, Jerry Li — [When Does Predictor-Based RL Align with Human Perception? A Study of Subjective Rewards in Codec-Based Speech Language Models](http://arxiv.org/abs/2608.31035v1)
  <details><summary>📄 Abstract</summary>
  Codec-based text-to-speech (TTS) models make language-model post-training applicable to speech generation, but it remains unclear when learned perceptual predictors can serve as reinforcement learning rewards without losing alignment with human listeners. We study this question with Group Relative Policy Optimization (GRPO) using learned rewards for anime-like speaking style, naturalness, likability, and arousal. To prevent perceptual rewards from being optimized through transcript drift, we int...
  </details>

- **2026-08-31** — Arthur Becker, Jakob Kemmler, David Thulke et al. — [Stick to What You Know: A Study of Knowledge-Aligned Supervised Fine-Tuning](http://arxiv.org/abs/2608.30987v1)
  <details><summary>📄 Abstract</summary>
  Supervised fine-tuning (SFT) trains a base language model to imitate target responses, and these targets may require knowledge the base model has not robustly internalized. We study this as a source of hallucinations and frame a group of mitigation methods as \emph{knowledge-aligned SFT}: constraining SFT training targets to the base model's parametric knowledge. Under a unified setup, we compare existing generation-based and estimation-based knowledge-alignment methods and introduce two new var...
  </details>

- **2026-08-31** — Priyanshu Karmakar, Borru Vijay Sai, Shubhojit Mallick et al. — [TRIPPULSE: Multi-Agent Travel Planning with Review-Grounded Reasoning](http://arxiv.org/abs/2608.30924v1)
  <details><summary>📄 Abstract</summary>
  Travel itinerary generation requires balancing strict spatio-temporal constraints with human preferences. Existing LLM-based planners mainly rely on structured attributes and pre- defined traveler personas, but real travel deci- sions are often shaped by reviews that reveal experiential factors such as comfort, safety, ser- vice quality, ambiance, crowding, and hidden risks absent from structured databases. Incor- porating such review information is therefore critical to realistic, user-centric ...
  </details>

- **2026-08-31** — Deepak Pandita, Christopher M. Homan — [Thesis Proposal: Toward a Human-Centered and Perspective-Aware Framework for Reproducible ML Evaluation and AI Alignment](http://arxiv.org/abs/2608.30842v1)
  <details><summary>📄 Abstract</summary>
  Humans play a vital role at every stage of AI development, from data collection and curation to model development and evaluation. However, humans often disagree with each other and sometimes with themselves over time. It is essential to take disagreement into account when building human-centered AI systems, especially in domains where it is prevalent, such as AI safety, content moderation, or sentiment analysis. Disagreement often arises from subjective human opinion and can vary with one's iden...
  </details>


### 📂 robustness
*鲁棒性与可靠性 / Robustness & Reliability* — 55 papers

- **2026-09-02** — S M Rafiuddin, Atriya Sen — [C$^{3}$T: Counterfactual Causal Reasoning for Sentiment Shifts in Social-Media Conversation Trees](http://arxiv.org/abs/2609.02131v1)
  <details><summary>📄 Abstract</summary>
  Sentiment in social-media threads does not only vary across posts; it shifts as users react to claims, corrections, evidence, and hostility within a branching reply tree. We study why sentiment changes in rumor-centric conversation trees by treating discourse moves (e.g., denial/correction, evidence/link, toxicity/attack) as candidate interventions and asking (i) what sentiment a reply expresses, (ii) whether the sentiment shifts relative to its parent, and (iii) which prior message most plausib...
  </details>

- **2026-09-02** — Yu Tian, Xintong Jiang, Jan Franklin Adamowski et al. — [PlantC2USeg: Cross-Scale Consistent Pre-Training for Few-Shot Unified Plant Point Cloud Segmentation](http://arxiv.org/abs/2609.02860v1)
  <details><summary>📄 Abstract</summary>
  Modern crop breeding demands precise organ-level analysis for trait quantification, making plant point cloud segmentation (PPCS) increasingly important. However, conventional deep learning approaches rely heavily on densely annotated datasets that are labor-intensive to acquire. Unified PPCS adaptation from distribution-shifted examples with minimal additional training remains challenging. To address this, we propose PlantC2USeg, a deep transfer learning framework featuring cross-scale consisten...
  </details>

- **2026-09-02** — Jiayi Bi, Yanjie Gao, Yuanmin Xie et al. — [Diagnosing with Insights: Structured Analysis of Agent Failures via Behavioral Abstractions](http://arxiv.org/abs/2609.02371v1)
  <details><summary>📄 Abstract</summary>
  With the proliferation of LLM agents, the ability to understand and diagnose failures in agents is essential to achieving superior effectiveness and trustworthiness. As agent failures often manifest via long and complex trajectories, manually finding the needles in the haystack is untenable. However, traditional diagnosis techniques for software bugs can hardly address LLM agent failures, while completely relying on LLMs as the judge yields unreliable diagnosis results. To overcome these challen...
  </details>

- **2026-09-02** — Mingyu Mei, Haojie Xu, Shihao Jin et al. — [HINT: Human-Intent Inception for Long-Horizon Robot Manipulation](http://arxiv.org/abs/2609.02653v1)
  <details><summary>📄 Abstract</summary>
  Humans can perform complex manipulations given a simple intent through an overall instruction, while continuously adapting to evolving visual observations. However, current vision-language action (VLA) models and other action policies struggle to realize this high-level intelligent behavior under dense, evolving visual inputs and sparse language guidance. Visual correlations can then dominate semantic intent, leading actions to follow visual shortcuts rather than human goals. We present HINT (Hu...
  </details>

- **2026-09-02** — Caio Azevedo, Stefano Sabatini, Sascha Hornauer et al. — [Towards Zero-Shot Transfer Across Embodiments For Driving VLAs](http://arxiv.org/abs/2609.02341v1)
  <details><summary>📄 Abstract</summary>
  Vision-Language-Action models (VLAs) have shown strong potential in autonomous driving by leveraging multimodal pretraining for instruction following, visual reasoning, and scene-level generalization. In robotic manipulation, scaling VLA fine-tuning across multiple robot setups--especially when unifying representations across embodiments--has been shown to improve in-dataset performance and cross-embodiment generalization; in autonomous driving, however, VLAs remain largely trained on individual...
  </details>

- **2026-09-02** — Dmitrii Andriianov, Andrey Veprikov, Aleksandr Beznosikov — [LoRA-TSD: Tangent-Space Spectral Descent for LoRA via Muon-Style Updates](http://arxiv.org/abs/2609.02734v1)
  <details><summary>📄 Abstract</summary>
  Low-rank adaptation (LoRA) is the standard way to fine-tune large models, yet when its two factors are trained independently, the update ignores the geometry of the low-rank weight change it induces. We introduce LoRA-TSD, an optimizer that treats every LoRA step as a tangent vector of the fixed-rank matrix manifold and takes the spectral-norm steepest-descent step of Muon inside that tangent space, mapping the result back to the factors through a retraction native to the LoRA parametrization. T...
  </details>

- **2026-09-02** — Canjie Liu, Jiawen Kang, Jinbo Wen et al. — [RVSD: Retrieval Vision Sparse Decoding for Mitigating Visual Hallucinations in Large Vision-Language Models](http://arxiv.org/abs/2609.02731v1)
  <details><summary>📄 Abstract</summary>
  Large vision-language models have achieved remarkable success in vision-language tasks. However, they remain prone to Visual Hallucinations (VHs), undermining their reliability in real-world applications. Existing solutions typically require curated datasets, additional training, or multi-round decoding, resulting in considerable computational overhead. In this paper, we propose \textbf{RVSD} (\underline{R}etrieval \underline{V}ision \underline{S}parse \underline{D}ecoding), a training-free and ...
  </details>

- **2026-09-02** — Hoonhee Cho, Jae-Young Kang, Giwon Lee et al. — [VIPS: Vehicle-Infrastructure Cooperative Planning Benchmark via Pseudo-Simulation](http://arxiv.org/abs/2609.02462v1)
  <details><summary>📄 Abstract</summary>
  End-to-end autonomous driving in urban environments requires robust decision-making under partial observability and complex multi-agent interactions. Severe occlusions and dense traffic at intersections limit the perception capability of single-agent systems, motivating recent efforts on Vehicle-to-Infrastructure (V2I) cooperation for perception and planning. However, existing evaluation protocols face a fundamental trade-off: open-loop evaluation fails to capture error accumulation and recovery...
  </details>

- **2026-09-02** — Etcharla Revanth Rao, Priyanshu Karmakar, Shubhojit Mallick et al. — [UTP-Bench: Uncertainty-aware Travel Planning Benchmark](http://arxiv.org/abs/2609.02421v1)
  <details><summary>📄 Abstract</summary>
  Large Language Models (LLMs) have recently demonstrated strong capabilities in automated travel itinerary generation. However, real- world travel planning is inherently uncertain: transportation delays, crowd fluctuations, and unexpected stochastic delays frequently inval- idate otherwise feasible schedules. Existing benchmarks like TravelPlanner and TripCraft assume deterministic environments, evaluating only static constraint satisfaction and ignoring whether generated plans remain robust when...
  </details>

- **2026-09-02** — Jingguan Liu, Xiaomeng Ai, Jiakun Fang et al. — [Continuous-Time Aggregation of Massive Flexible HVAC Loads Considering Uncertainty for Reserve Provision in Power System Dispatch](http://arxiv.org/abs/2609.02408v1)
  <details><summary>📄 Abstract</summary>
  Heating, ventilation, and air conditioning (HVAC) loads, with their rapid response capabilities, can provide considerable intra-hour flexibility on the demand side for reserve provision in order to follow the fast variations of renewables. However, scheduling massive HVACs is challenging due to computation complexity and the uncertainty of outdoor temperature. In this paper, we first introduce a novel continuous-time (CT) aggregation model to reveal the potential intra-hour flexibility of HVACs....
  </details>

- **2026-09-02** — Matteo Greco, Anudeex Shetty, Andrea Tagarelli et al. — [MultiGhostBench: A Multilingual Benchmark for Long-Form LLM-Generated Text Attribution under Distribution Shifts](http://arxiv.org/abs/2609.02379v1)
  <details><summary>📄 Abstract</summary>
  While existing work on LLM authorship attribution (AA) has made progress, available benchmarks remain limited, often focusing on English, controlled settings, or relatively outdated models, with the few multilingual studies considering only relatively short texts. We introduce MultiGhostBench, a multilingual benchmark comprising 928 books generated by five recent LLMs across six languages and three scripts, with an average length of approximately 59K words per book. The benchmark supports evalua...
  </details>

- **2026-09-02** — Chongkun Deng — [Farthest-cell triplet entropy: high-dimensional shell limits and hyperbolic curvature amplification](http://arxiv.org/abs/2609.02362v1)
  <details><summary>📄 Abstract</summary>
  We introduce farthest-cell triplet entropy, the conditional Shannon entropy of the farthest-prototype label given three random prototypes. For independent queries and prototypes, its estimator records only the farthest label, not coordinates or numerical distances. The statistic is bounded by $\log 3$, is invariant under common strictly increasing transformations of the dissimilarities, and has an exact mutual-information interpretation. In high-dimensional isotropic radial models $X_d=R_dU_d$, ...
  </details>

- **2026-09-02** — Qiang Xiang, Shuang Sun, Binglei Li et al. — [GlyphAnchor: Enhancing Visual Text Rendering via Position-Anchored Glyph Priors](http://arxiv.org/abs/2609.02349v1)
  <details><summary>📄 Abstract</summary>
  Rendering accurate text remains difficult for image generation and editing models, especially when the target contains long, complex, and densely arranged text or rare characters. Existing approaches either improve native text rendering through stronger backbones and data-centric training without explicit glyph priors, or incorporate glyph priors through specialized designs that remain insufficiently accurate and robust under challenging scenarios. We introduce GlyphAnchor, a novel text-renderin...
  </details>

- **2026-09-02** — Christoforos Fragkiadakis, Seyed Sahand Mohammadi Ziabari, Ali Mohammed Mansoor Alsahag — [Fairness-Aware Multimodal Transformer Modeling for Real-Time Student Attention Estimation](http://arxiv.org/abs/2609.02232v1)
  <details><summary>📄 Abstract</summary>
  Automated student-attention estimation can support learning analytics, but aggregate predictive metrics can conceal demographic disparities. This study evaluates fairness-aware multimodal temporal models on DIPSER, a naturalistic classroom dataset combining facial images, wearable-sensor measurements, attention annotations, and automatically inferred demographic metadata. Three baselines are compared across 10 training seeds: a Visual GRU, a Sensor GRU, and a Residual Fusion Transformer. The mul...
  </details>

- **2026-09-02** — Wei Zhang, Hongji Li, Song Sun et al. — [DMRL: Document-Mediated Reinforcement Learning for Skill Optimization in Advertising Recommendation](http://arxiv.org/abs/2609.02170v1)
  <details><summary>📄 Abstract</summary>
  Advertising recommendation requires continuously tuning complex system parameters while balancing commercial returns and user experience. Recent work has introduced large language models (LLMs) with skill documents to assist this labor-intensive process, but skill optimization remains largely prompt-driven, lacking a principled mechanism to attribute rewards to specific document edits. To address this limitation, we propose Document-Mediated Reinforcement Learning (DMRL), a skill self-evolution ...
  </details>

- **2026-09-02** — Alexander J Healey, Alan Salek, Christopher T-K Lew et al. — [Persistence and emergence of quantum defects through pressure-induced phase changes](http://arxiv.org/abs/2609.02100v1)
  <details><summary>📄 Abstract</summary>
  Extreme pressures can transform materials and their properties, but probing these in-situ is made challenging by the small sample volumes and access requirements demanded by diamond anvil cells. Quantum defects offer a route to local measurements under such conditions, yet their sensing performance can be dictated by pressure-induced changes in their own host material. On the other hand, pressure may also be harnessed as a tool to engineer and stabilize new quantum defects with emergent function...
  </details>

- **2026-09-01** — Joshua Shay Kricheli — [Differential Games for Compositional Handling of Competing Control Tasks](http://arxiv.org/abs/2609.01838v1)
  <details><summary>📄 Abstract</summary>
  We introduce a novel Divide and Conquer control design methodology leveraging differential games in single-agent, multi-objective dynamical systems. The proposed framework associates each control objective with a virtual input and establishes a non-cooperative, finite or infinite horizon differential game among representative players. Each player optimizes a distinct virtual cost function tailored to its specific goal, the full system state, and the other virtual inputs, while accounting for the...
  </details>

- **2026-09-01** — Dushyant Rajput — [Cheap Verifiers, Large Blind Spots: Measuring the Reliability Cost of Cost-Saving Cascades](http://arxiv.org/abs/2609.01345v1)
  <details><summary>📄 Abstract</summary>
  Inference cascades cut cost by answering most queries with a cheap model and escalating a hard tail to a frontier model that acts as verifier. A natural extension closes the loop: fine-tune the cheap student on the verifier's rejections so the escalation rate, and cost, fall each round. We measure this loop on real LLMs and report four findings. First, the verifier's blind spot, the fraction of the student's wrong answers it accepts, is large and moves adversarially: it grows with student capabi...
  </details>

- **2026-09-01** — Navaneetha Krishnan Kamalakannan — [Real-Time Neuromorphic Spectrum Intelligence Simulator](http://arxiv.org/abs/2609.00585v1)
  <details><summary>📄 Abstract</summary>
  We present the Real-Time Neuromorphic Spectrum Intelligence Simulator (RT-NuSIS), a modular framework to study spiking neural network (SNN) and memristor-inspired agents for dynamic spectrum access under constrained energy budgets and adversarial conditions. RT-NuSIS couples leaky integrate-and-fire neuronal dynamics, memristive synaptic models, physics-informed energy-harvesting models (triboelectric and RF), and adversary models including jamming and Byzantine behavior. We formalize the simula...
  </details>

- **2026-09-01** — Haoyuan Deng, Haichao Liu, Wenkai Guo et al. — [Facet-0: A Robotic Foundation Model for Contact-Rich Precise Manipulation](http://arxiv.org/abs/2609.01596v1)
  <details><summary>📄 Abstract</summary>
  Real-world robotic assembly at sub-millimeter tolerances demands spatial precision, compliant interaction, and robustness to contact failures. We present Facet-0, a robotic foundation model that predicts and values the contact consequences of its actions. Facet-0 unifies multimodal representation learning and reinforcement learning (RL) post-training around a joint action-wrench proposal: a causal wrench history is aligned with vision-language semantics and kinematic state, and flow matching gen...
  </details>

- **2026-09-01** — Fatemeh Javadian, Zhu Chen, Zahra Aminparast et al. — [Semantic-Guided Multimodal Preprocessing for Vision Transformer-Based Clear Cell Renal Cell Carcinoma Grading](http://arxiv.org/abs/2609.01426v1)
  <details><summary>📄 Abstract</summary>
  Clear cell renal cell carcinoma (CCRCC) grading is essential for treatment planning, yet existing approaches either analyze patch-level images directly or focus solely on nuclei-level classification, without linking to final tumor grading. We propose a semantic-guided multimodal preprocessing method that integrates nuclei classification maps from existing pre-trained models with RGB histopathology images for Vision Transformer (ViT)-based CCRCC grading. Our approach employs classification map ch...
  </details>

- **2026-09-01** — Nishant Mishra, Ameen Abu-Hanna, Iacer Calixto — [Investigating Linear Probe Robustness to Linguistic Register, Medical Specialty, and Corpus Shifts in Medical QA](http://arxiv.org/abs/2609.01361v1)
  <details><summary>📄 Abstract</summary>
  Linear classifiers trained on hidden states of a large language model (LLM), linear probes, can flag factual errors from a single forward pass. Geometrically, that implies that true and false statements separate along a stable direction in hidden state space, i.e., the truth direction. Prior work disagrees on whether this generalises across input shifts, but the disagreement is hard to interpret because cross-dataset probe transfer experiments confound several kinds of input change at once. We i...
  </details>

- **2026-09-01** — Natalija Mitic, Soona Sedahmed A. O., Mamadou Selly Ly et al. — [The Constitutional Coverage Trilemma in AI Governance](http://arxiv.org/abs/2609.01275v1)
  <details><summary>📄 Abstract</summary>
  Frontier AI systems function as \emph{constitutional institutions}: each deployed model encodes an implicit ranking among safety, helpfulness, honesty, autonomy, and equity. We ask whether the supply of frontier constitutional types covers human demand. Combining a paraphrase-controlled audit of the as-shipped default constitutions of $23$ frontier LLM archetypes with a pairwise-tradeoff study of $1{,}649$ US participants on the same instrument, we report three facts. \emph{Demand is broad}: it ...
  </details>

- **2026-09-01** — Fanrui Zhang, Ruixue Ding, Qiang Zhang et al. — [ARISE-RL: Agentic Rubric-Grounded Iterative Self-Evolution with Reinforcement Learning](http://arxiv.org/abs/2609.01058v1)
  <details><summary>📄 Abstract</summary>
  Training open-ended agents via reinforcement learning (RL) is hindered by the lack of verifiable gold answers and scalable rubrics. Moreover, even near the model's capability boundary, long-horizon open-ended agentic tasks often yield brittle and unstable rewards, resulting in weak or noisy rollout contrast that obscures fine-grained optimization signals for group-based policy learning. To address these challenges, we propose ARISE-RL, a novel full-cycle self-evolution framework that couples a t...
  </details>

- **2026-09-01** — Jongyeop Hyun, Taeyoung Kim, Hyounghun Kim — [Controllable Image Captioning with Prompt-Conditioned Scene Rewards](http://arxiv.org/abs/2609.00709v1)
  <details><summary>📄 Abstract</summary>
  Large Vision-Language Models produce fluent image descriptions but offer limited semantic control: users cannot reliably specify whether captions should emphasize attributes, relations, or particular image regions. We present Fine-grained Captioning Control Using Scene Rewards (FoCUS), a controllable image captioning method that lets users steer captions toward specific semantic emphases through natural-language control prompts. The core idea is a prompt-conditioned control objective based on sc...
  </details>

- **2026-09-01** — Lingxiao Li, Max Whitton, Ledell Wu et al. — [GenScale: A Benchmark for Relative Object Scale in Image Generation and Editing](http://arxiv.org/abs/2609.00525v1)
  <details><summary>📄 Abstract</summary>
  Modern image generation and editing systems can produce photorealistic, prompt-aligned images, but still often render familiar objects at implausible relative sizes. To measure this failure mode, we introduce GenScale, a benchmark and evaluation protocol for real-world relative object scale in image generation and editing. GenScale contains 900 image-level entries and 1,643 pairwise anchor-target scale relations across common-object generation, human-product generation with metric dimensions, an...
  </details>

- **2026-09-01** — Md. Atabuzzaman, Chris Thomas — [Reliability Challenges in Diffusion Vision-Language Models](http://arxiv.org/abs/2609.01318v1)
  <details><summary>📄 Abstract</summary>
  Diffusion-based Large Vision-Language Models (dLVLMs) have recently emerged as a compelling alternative to autoregressive (AR) LVLMs, offering advantages in parallel decoding, bidirectional context, and controllable generation. Despite rapid progress, their reliability properties remain largely uncharacterized. We present the first systematic reliability evaluation of hallucination and bias in dLVLMs, benchmarking six diffusion models against competitive AR baselines across four dimensions. Our ...
  </details>

- **2026-09-01** — Athira J. Jacob, Puneet Sharma, Daniel Rueckert — [CMRVision: A Foundation Model for Cardiac MR Image Analysis](http://arxiv.org/abs/2609.01308v1)
  <details><summary>📄 Abstract</summary>
  Cardiac magnetic resonance (CMR) imaging provides complementary information on cardiac anatomy, function, and tissue characterization across multiple sequences and views. In this work, we investigate foundation model pretraining for 2D CMR and introduce CMRVision, a CMR-specific foundation model trained using DINOv3-style self-supervised learning on a multi-center, multi-sequence cohort of 36 million CMR images. We systematically evaluate architectural and training design choices for domain-spec...
  </details>

- **2026-09-01** — Sathiyamohan Nishankar, Pubudu Sanjeewani, Asanka Perera et al. — [HiLRP: Toward One Trustworthy Explanation for Vision Transformer: Conservation-Valid Attribution via Attention Primitives](http://arxiv.org/abs/2609.01282v1)
  <details><summary>📄 Abstract</summary>
  Vision Transformer (ViT) design has become increasingly diverse, with backbones combining convolutional stems, windowed, linear, or multi-axis attention, patch merging, and spatial reduction in various configurations. This diversity poses challenges for existing attribution methods, whose assumptions often do not hold across ViT variants: Grad-CAM requires a terminal spatial feature map, attention rollout assumes global softmax attention, and layer-wise relevance propagation (LRP) requires modul...
  </details>

- **2026-09-01** — Jiayi Yan, Francesco Fabiano, Alessandro Abate — [Dual Process Motion Planning](http://arxiv.org/abs/2609.01260v1)
  <details><summary>📄 Abstract</summary>
  Robotic systems are deeply embedded in both industry and everyday life, where they are expected to act with speed, precision, and reliability. Classical control and planning methods have long delivered strong guarantees, but often at the cost of computational efficiency and adaptability. More recently, learning-based approaches have shown promise in overcoming these limitations, enabling agents to leverage experience to accelerate decision-making and address previously intractable problems. In t...
  </details>

- **2026-09-01** — Walid Saidi — [MutMem-V2: Cryptographically Authorized Mutation in Persistent Agent Memory Portable Verification and Reproducible Evidence](http://arxiv.org/abs/2609.01235v1)
  <details><summary>📄 Abstract</summary>
  MutMem V1 introduced retention-preserving, cryptographically authorized mutation for persistent agent memory but did not provide a complete portable verification contract or clean-install reproduction path. MutMem V2 closes that publication gap without introducing a second memory engine. It specifies exact canonical bytes, domain-separated object and bundle commitments, mandatory recall-evidence membership and ordering, external trust anchors, identity epochs, revocation, authorization, request ...
  </details>

- **2026-09-01** — Reza Heidari, Hamed R. Tavakoli, Juho Kannala — [Compressing AI Traffic: Standardized Neural Network Coding of Visual-Token Representations in Split Vision-Language Inference](http://arxiv.org/abs/2609.01200v1)
  <details><summary>📄 Abstract</summary>
  When the visual encoder and the language decoder of a vision-language model (VLM) run on different compute nodes, the intermediate visual-token embeddings become a communicated payload rather than an internal activation. We call such machine-consumed intermediate tensors AI traffic and ask how far they can be compressed with a standardized, training-free codec. We insert ISO/IEC 15938-17 Neural Network Coding (NNC) round trips on the complete visual interface of a Qwen3-VL-8B-Instruct video ques...
  </details>

- **2026-09-01** — Chaohui Guo, Michel Klein, Zhisheng Huang — [CaRL-EM: Cost-Aware Reinforcement Learning for Entity Matching with LLMs](http://arxiv.org/abs/2609.01195v1)
  <details><summary>📄 Abstract</summary>
  Entity matching (EM) requires fine-grained contextual understanding and domain knowledge. Recent work shows that large language models (LLMs) can serve as strong matchers across domains, but most methods either make independent pairwise decisions or rely on manually designed composite pipelines, thus lacking flexibility in realistic multi-candidate settings. At the same time, they typically ignore inference cost at scale. We formulate LLM-based EM with candidates as a cost-aware sequential decis...
  </details>

- **2026-09-01** — Muxin Liu, Xiaoyang Lyu, Yang-Tian Sun et al. — [Monocular Depth Estimation from a Single Image: Progress and Opportunities](http://arxiv.org/abs/2609.01172v1)
  <details><summary>📄 Abstract</summary>
  Monocular depth estimation has long stood as a fundamental challenge in computer vision, enabling a wide range of applications including 3D reconstruction, robotics, autonomous driving, and augmented reality. This survey traces the field's evolution from early learning-based methods to the emergence of transformative foundation models. We begin by framing the problem, distinguishing between relative and metric depth estimation, and highlighting the key challenges that have shaped a decade of res...
  </details>

- **2026-09-01** — Jiayu Ding, Zhuodong Liu, Lei Zhang et al. — [Dyn-3D: Unveiling and Resolving Ego-Motion Ambiguity in Vision-Language Models](http://arxiv.org/abs/2609.01059v1)
  <details><summary>📄 Abstract</summary>
  As Vision-Language Models (VLMs) tackle dynamic 3D spatial reasoning, ego-motion perception becomes essential to resolve monocular scale ambiguity. However, current models often overfit to smooth trajectory priors rather than genuinely understanding physical motion. Consequently, their spatial reasoning degrades severely under large displacements, a phenomenon we term Kinematic Collapse. This failure stems from spurious visual-motion correlations in natural videos and a lack of explicit physical...
  </details>

- **2026-09-01** — Yiming Luo, Rongqiang Zhao, Jie Liu — [SAGE: Subpopulation-Aware Generative Enhancement for Mitigating Spurious Correlations](http://arxiv.org/abs/2609.01051v1)
  <details><summary>📄 Abstract</summary>
  Spurious correlations pose a significant challenge to the robustness of modern machine learning. The inherent imbalance in dataset distributions often leads traditional Empirical Risk Minimization (ERM) models to rely on majority spurious attributes for classification, resulting in poor performance on minority groups. This problem becomes particularly challenging when the spurious attributes are unavailable. Existing group-label-free methods often upsample minority groups or misclassified real t...
  </details>

- **2026-09-01** — Ruijie Tang, Chenye Zou, Guoquan Wu et al. — [HitMem: Hierarchical Temporal 3D Memory with Multi-Modal Context-Aware Retrieval for Dynamic Environments](http://arxiv.org/abs/2609.00950v1)
  <details><summary>📄 Abstract</summary>
  Executing long-term tasks in dynamic environments requires embodied agents to maintain robust and adaptive 3D scene representations. However, most existing 3D memory frameworks rely on static world assumptions. When objects are displaced by human activities or unobserved events, agents encounter memory-observation conflicts and often require costly geometric recomputations or inefficient global re-exploration. To address this, we propose HitMem, a hierarchical temporal 3D memory framework with a...
  </details>

- **2026-09-01** — Zhe Shen, Liyuan Lou, Yifei Yu et al. — [On-the-Fly3R: Towards Robust Online 3D Reconstruction with Feed-Forward 3R Models for Large-Scale UAV Scenarios](http://arxiv.org/abs/2609.00923v1)
  <details><summary>📄 Abstract</summary>
  While feed-forward 3D reconstruction (3R) offers efficient end-to-end modeling, its application in large-scale UAV mapping is hindered by the prohibitive memory cost of Transformer attention. Current scalable streaming 3R methods assume temporally and spatially continuous inputs, rendering them ineffective for the weakly ordered or unordered image streams common in cross-strip UAV operations. To address this, we propose On-the-Fly3R, a training-free, progressive online 3D reconstruction framewor...
  </details>

- **2026-09-01** — Ravi Teja Vulchi, Carl Messerschmidt, Mohammadsadegh Vafaeinezhad et al. — [iPINN for Broadband CARS Phase Retrieval: A Framework for Function Approximation and Inverse Modeling Problems in Nonlinear Spectroscopy](http://arxiv.org/abs/2609.00883v1)
  <details><summary>📄 Abstract</summary>
  Phase retrieval in broadband coherent anti-Stokes Raman spectroscopy (BCARS) is an ill-posed inverse problem. The Raman-like signal is encoded in the imaginary part of the resonant susceptibility, which mixes coherently with a non-resonant background (NRB) that varies across acquisitions. We introduce an inverse physics-informed neural network (iPINN) that predicts Lorentzian peak parameters from raw BCARS spectra and reconstructs the resonant susceptibility through a differentiable analytical f...
  </details>

- **2026-09-01** — Béatrice Garcia Cegarra, Elena Vanneaux, Quentin Picard et al. — [Connectivity-Aware Graph Extension for Decentralized Multi-Robot Exploration](http://arxiv.org/abs/2609.00804v1)
  <details><summary>📄 Abstract</summary>
  Exploring unknown environments with multiple UAVs requires coordination under intermittent communication, making decentralized operation a baseline assumption. We propose, within a decentralized framework, a novel exploration graph extension strategy based on frontier connectivity to extend exploration plans and maintain area partitioning among agents stable and robust to disconnections and changes in spatial layout. The proposed extension method is applied to two state-of-the-art area partition...
  </details>

- **2026-09-01** — Lu Cheng — [Escaping Redundant Reasoning: Structure-Aware Search for Inference-Time LLMs](http://arxiv.org/abs/2609.00738v1)
  <details><summary>📄 Abstract</summary>
  Inference-time search with large language models (LLMs) often concentrates on a small set of structurally or semantically similar trajectories, leaving alternatives underexplored---a failure mode we call \textit{reasoning basin collapse}. We introduce BASIN, a training-free, structure-aware selection method that groups reasoning states into basins and penalizes repeated visits to the same strategy, thereby reallocating search across genuinely distinct reasoning paths under a fixed compute budget...
  </details>

- **2026-09-01** — Chaewon Kim, Seo Yeon Park — [SCoNE: Selective Context-aware Neuron Editing for Robust Retrieval-Augmented Generation](http://arxiv.org/abs/2609.00689v1)
  <details><summary>📄 Abstract</summary>
  Retrieval-Augmented Generation (RAG) is highly sensitive to retrieval noise: when retrieved documents mix informative and irrelevant context, LLMs are easily distracted, leading to hallucinations. To overcome this, we propose SCoNE (Selective Context-aware Neuron Editing), a training-free model editing approach that improves retrieval noise robustness by selectively strengthening context-aware FFN neurons that are identified by both high attribution and high cross-input variability. SCoNE requir...
  </details>

- **2026-09-01** — Ningxuan Zhang, Ziwei Wang, Ning Xie et al. — [Operationalizing open-ended biological discovery across single-cell representations](http://arxiv.org/abs/2609.00681v1)
  <details><summary>📄 Abstract</summary>
  Single-cell studies are typically initiated from predefined research questions, leaving much of the biological information encoded within existing data unexplored. We formalize open-ended discovery as an analytical paradigm, in which data-derived signals are identified before biological context is interrogated and subsequently evaluated according to their potential to justify prospective experimental investment. Here we develop PROSPECTor, an end-to-end framework that searches for reproducible b...
  </details>

- **2026-09-01** — Kaizhen Tan — [You Cannot Photograph the Same Street Twice: Reliability Limits in Vision-Language Measurement of Urban Change](http://arxiv.org/abs/2609.00649v1)
  <details><summary>📄 Abstract</summary>
  Vision-language models are increasingly used to measure urban change from repeated street-level imagery, but their longitudinal reliability is not well understood. We test how much a perception score can change when the street itself does not undergo substantial redevelopment. Using 4,648 consecutive-epoch image pairs from 435 Google Street View standpoints across five US cities, we find that re-photographing the same street changes a perception score by 0.80 points on average, equivalent to 66....
  </details>

- **2026-09-01** — Benoît Guérand, Tan Minh Nguyen — [Topological Steering](http://arxiv.org/abs/2609.00597v1)
  <details><summary>📄 Abstract</summary>
  With the rapid rise of large language models (LLMs), controlling undesirable model behaviors has become increasingly important. Existing behavioral control methods typically intervene directly in activation or feature space, but such approaches can be sensitive to outliers, distributional shifts, noise, and other local perturbations. Motivated by Topological Data Analysis (TDA), which captures global rather than purely local structure, we propose Topological Steering, a new framework for steerin...
  </details>

- **2026-09-01** — Xin Zhang, Lin Li, Chuanbo Liu et al. — [BiMTokenizer: Preserving Semantic-Acoustic Balance in Low-Bitrate Speech Tokenization via Bidirectional State-Space Modeling](http://arxiv.org/abs/2609.00562v1)
  <details><summary>📄 Abstract</summary>
  Speech codecs serve as bridges between continuous speech signals and large language models, yet face an inherent conflict between acoustic fidelity and semantic preservation. To mitigate this conflict, recent works increasingly adopt dual-tower architectures to decouple semantic and acoustic modeling with separate encoders. However, these dual-tower designs incur substantial architectural overhead. To avoid such complexity, we revisit the single-tower paradigm and propose BiMTokenizer, a low-bit...
  </details>

- **2026-08-31** — Shangqing Tu, Daniel Zhang-Li, Yucheng Wang et al. — [CogEvol: Towards Efficient and Reliable Learning Environment Generation](http://arxiv.org/abs/2608.30968v2)
  <details><summary>📄 Abstract</summary>
  We present CogEvol, a family of models trained specifically for Learning Environment Generation: turning a course brief into a finished learning artifact (structured-JSON slides or self-contained interactive HTML pages) in a single pass. Across 220k production requests, CogEvol completes a slide in a median of 17 seconds and an interactive page in 59, replacing minutes-long multi-turn agent scaffolding. Reliability is enforced rather than hoped for: a production-grounded data pipeline turns real...
  </details>

- **2026-08-31** — Debarpan Bhattacharya, Malay Phadke, Sriram Ganapathy — [BiG-SURE - Bipartite Graph for Semantic Uncertainty and Reliability Estimation of LLMs](http://arxiv.org/abs/2608.30646v2)
  <details><summary>📄 Abstract</summary>
  Reliable uncertainty estimation is a crucial requirement for deploying large language models (LLMs) and vision-language models (VLMs) in safety-critical settings, especially when the model parameters are not accessible (black-box). We propose BiG-SURE, an uncertainty estimator based on cross-temperature semantic agreement. The method samples low-temperature responses as stable semantic anchors and high-temperature responses as probes under meaning-preserving input transformations. It then constr...
  </details>

- **2026-08-31** — Xionghao Wu, Yijun Yang, Shiyang Zhou et al. — [ZimaBlue: Evolving Generalizable World Action Models through Scalable Video Pre-training](http://arxiv.org/abs/2609.00188v1)
  <details><summary>📄 Abstract</summary>
  Robotic manipulation faces a fundamental scaling challenge: robust generalization demands broad physical experience, yet action-labeled robot trajectories are expensive to collect and inherently limited in diversity. Egocentric videos offer a far more scalable source of embodied experience, capturing object interactions, contact dynamics, tool use, and long-horizon behaviors across diverse environments. The central challenge is how to convert this abundant but action-free experience into effecti...
  </details>

- **2026-08-31** — Qiaoyuan Zheng, Yiqu Yang — [Are Near-Tied LLM Rankings Robust to Family-DIF-Guided Benchmark Recomposition?](http://arxiv.org/abs/2609.00482v1)
  <details><summary>📄 Abstract</summary>
  Small leaderboard gaps are often interpreted as evidence that one language model is better than another, but their sign may depend on which benchmark items are included. We test this using item-level responses from five benchmarks and a family-label-free spectral approximation to multidimensional item-response theory (MIRT). In owner-disjoint folds, one owner half identifies items with low residual differential item functioning across model families (low-DIF); the resulting frozen, source- and e...
  </details>

- **2026-08-31** — Reza Farahani, Zoha Azimi Ourimi, Mario Colosi et al. — [DRLM: Deep Reinforcement Learning-Based LLM Query Orchestration in Edge Environments](http://arxiv.org/abs/2609.00442v1)
  <details><summary>📄 Abstract</summary>
  Large language model (LLM) services increasingly process heterogeneous queries with diverse latency, accuracy, and resource requirements. While edge deployment reduces response time, the heterogeneity of devices and the diversity of model families, parameter scales, and quantization levels make efficient LLM query orchestration challenging. This paper introduces DRLM, a Deep Reinforcement Learning-based LLM query orchestration framework in edge environments. DRLM integrates two lightweight predi...
  </details>

- **2026-08-31** — Chad Wong, Sicheng Chen, Tianyi Zhang et al. — [SlideMix: Enhancing Whole Slide Image Analysis via Multimodal Shuffling](http://arxiv.org/abs/2609.00396v1)
  <details><summary>📄 Abstract</summary>
  Histopathological whole slide images (WSIs) are central to cancer diagnosis, but their gigapixel scale, tissue heterogeneity, weak slide-level supervision, sparse diagnostic regions, and multi-scale evidence make robust automated analysis challenging. Multiple instance learning (MIL) is widely used to aggregate tile-level features into slide-level predictions, yet existing augmentation strategies often perturb tissue regions without preserving diagnostic relevance, slide context, or cross-scale ...
  </details>

- **2026-08-31** — Jonathan Zheng, Zirui Shao, Alan Ritter et al. — [Synthetic Worlds for Temporal Evaluation and Knowledge Updating in LLMs](http://arxiv.org/abs/2609.00184v1)
  <details><summary>📄 Abstract</summary>
  Large language models (LLMs) rely on static pretraining corpora, causing their knowledge to become outdated over time. Existing approaches for evaluating knowledge edits either suffer from rapid contamination or rely on counterfactual edits that conflict with rigid existing knowledge. In this work, we propose a synthetic, simulation-driven framework for studying knowledge insertion in LLMs. We introduce {\sc ParallelEvents}, a benchmark of fictional yet realistic future worlds that generates coh...
  </details>

- **2026-08-31** — Peizhi Mai, Philip W. Phillips — [Green-function Zeros Encode Competing Mott and Charge-ordering Scales](http://arxiv.org/abs/2609.00124v1)
  <details><summary>📄 Abstract</summary>
  While correlated insulators are devoid of low-energy quasiparticle poles, their Green functions retain clean momentum structure through zeros. However, precisely what zeros imply is not clear. By studying the extended Hubbard model both analytically and numerically, we establish a new paradigm for strongly correlated matter: the dispersion of Green function zeros is determined by both microscopic spin-spin correlations and defect kinematics. In fact, we find that the dispersion changes discontin...
  </details>

- **2026-08-31** — Fengrui Hua, Hengyi Yang, Xinlei Hao et al. — [Agentic Quantitative Trading: A Survey of Workflows, Systems, and Evaluation](http://arxiv.org/abs/2608.31041v1)
  <details><summary>📄 Abstract</summary>
  Quantitative trading is moving from isolated predictive models toward agentic workflows that combine reasoning, tool use, memory, and feedback. This survey reviews agentic quantitative trading across five stages: factor mining, signal discovery, portfolio construction, order execution, and risk management. We further examine agentic quant trading systems through architecture, coordination, and adaptation, while comparing benchmarks across strategy construction, offline trading, live market evalu...
  </details>


### 📂 watermark
*水印与溯源 / Watermarking & Provenance* — 11 papers

- **2026-09-02** — Yuzhang Luo, Chenpeng Wang, Jianhui Chen et al. — [From Reweighting to Rewriting: Unlocking the Intervention Effects of Influential Samples in Training Data Attribution](http://arxiv.org/abs/2609.02771v1)
  <details><summary>📄 Abstract</summary>
  Training data attribution (TDA) aims to identify training examples that shape model behavior, but its intervention value depends on both which examples are selected and how they are modified. Influence functions (IF) estimate behavioral changes under infinitesimal reweighting, yet IF-selected examples often show limited advantages over random selection under conventional weight-based interventions. This raises the question of whether influential examples lack intervention value or whether reweig...
  </details>

- **2026-09-02** — Yujie Tu, Zhiliang Peng, Jianwei Yu et al. — [VibeVoice-ASR-Streaming Technical Report](http://arxiv.org/abs/2609.02812v1)
  <details><summary>📄 Abstract</summary>
  Traditional speaker-attributed ASR systems treated ASR and speaker diarization as two separate tasks. Recently, end-to-end models such as VibeVoice-ASR have unified the two tasks within a single model. However, existing unified models still mainly support offline recognition, making it difficult to meet the low-latency requirements of real-time voice assistants and agents. To tackle this issue, we present VibeVoice-ASR-Streaming, one of the first LLM-based end-to-end approaches to streaming spea...
  </details>

- **2026-09-02** — Jan Schnorrenberg, Jan Ernsting, Enrico Küllenberg et al. — [Seeing Beyond the Lesion: Disease Recognition from Reactive CNS Tissue](http://arxiv.org/abs/2609.02390v1)
  <details><summary>📄 Abstract</summary>
  Sampling error yields exclusively reactive, non-lesional brain parenchyma in a significant proportion of intracranial biopsies, leaving the underlying disease undiagnosed. We benchmark four pathology foundation models (UNI2-h, Virchow2, Prov-GigaPath, H-optimus-0) as frozen patch encoders within a shared attention-based multiple-instance learning framework using 245 whole-slide images from 186 patients with confirmed downstream diagnoses. We first show that coarse disease-category prediction can...
  </details>

- **2026-09-02** — Yunhao Liu, Hong Phuc Pham, Jaehong Yoon — [PaperCompiler: Faithful Paper-to-Code Generation via Repository-Level Specification Compilation](http://arxiv.org/abs/2609.02272v1)
  <details><summary>📄 Abstract</summary>
  Faithfully translating research papers into repository-level implementations remains challenging because papers often describe methods at a high level, leave implementation assumptions implicit, and require generated repositories to preserve method logic, evaluation protocols, and cross-file consistency. Despite recent advances in paper-to-code agents, their intermediate outputs are often presented as free-form plans or summaries that downstream coding agents may ignore, reinterpret, or compress...
  </details>

- **2026-09-01** — Tommaso Cerruti, Mika Okamoto, Ansel Kaplan Erol — [Agent Memory Is a Surface for Endogenous Authorization Laundering](http://arxiv.org/abs/2609.01836v1)
  <details><summary>📄 Abstract</summary>
  Long-running LLM agents rely on persistent memory to carry state across interactions, including permissions, restrictions, and revocations. When memory misrepresents this evolving authorization state, the agent's own records can grant authority that the underlying history never permitted, resulting in misaligned behavior without any external attacks.   We term this failure endogenous authorization laundering, where spurious permissions written into memory lead to unauthorized actions as their pr...
  </details>

- **2026-09-01** — Jun Hou, Priya Pitre, Yi Fang et al. — [EDGE: Error Dependency Graph-Guided Multi-Error Attribution in Multi-Agent LLM Systems](http://arxiv.org/abs/2609.01360v1)
  <details><summary>📄 Abstract</summary>
  Large language model (LLM) agent failures often contain multiple related errors rather than a single mistake. Existing attribution methods usually identify a responsible agent, step, or root cause, but do not explicitly model dependency between errors. We introduce EDGE, an Error Dependency Graph-guided multi-Error attribution framework. EDGE constructs an error dependency graph from observed error events and validates a reliable causal subset through counterfactual rollout. The inference graph ...
  </details>

- **2026-09-01** — Huimin Wang, Zhengyi Zhao, Yutian Zhao — [ClinTraceBench: Source-Verifiable Longitudinal Clinical Reasoning over EHR-Derived Dialogues](http://arxiv.org/abs/2609.01111v1)
  <details><summary>📄 Abstract</summary>
  Clinical LLM assistants must reason over multi-visit patient trajectories, yet whether the compact history representations used to scale them---retrieval, structured timelines, LLM summaries, agentic memory---preserve the longitudinal signal clinical reasoning needs has not been measured. We introduce ClinTraceBench: 385 MIMIC-IV-derived verified dialogues with event-ID provenance, a nine-task taxonomy (T1--T9), and L0--L4 deterministic + L5 human-audit validation (98.92\% agreement). We evaluat...
  </details>

- **2026-09-01** — Marina de la Cruz Echeandía, César Luis Alonso, Tony Ribeiro et al. — [QILP-0: Constructing Observational Declarative Twins of Quantum Circuits](http://arxiv.org/abs/2609.01049v1)
  <details><summary>📄 Abstract</summary>
  This paper introduces QXymb, a general framework for constructing observational declarative twins of quantum circuits, and develops QILP-0, its first complete order-0 specialization. QILP-0 constructs a finite multi-valued propositional logic program from observed circuit behaviour within a declared observational scope.   The pipeline traverses a declared family of quantum observables incrementally according to a reproducible structural grading and a declared observational reference horizon. Pro...
  </details>

- **2026-09-01** — Hyeonseop Yoon, Jeong-Eun Park — [Staged Linguistic Seeding: Grounded Query Expansion for Verified-Unit QA in AI Contact Centers](http://arxiv.org/abs/2609.00844v1)
  <details><summary>📄 Abstract</summary>
  Customer-service QA in an AI contact center (AICC) runs under deployment constraints that benchmark QA misses: tight voice-hotline latency and a high cost for unsupported or wrong automatic answers. We deploy a system that answers only from a closed set of verified QA units: it returns a retrieved unit verbatim, or routes to clarify, abstain, or handoff. The index is enriched offline by staged linguistic seeding (SLS): a human authors a per-unit world-grounded slot recipe, gpt-4.1-mini renders i...
  </details>

- **2026-09-01** — Haoyuan Shi, Mingtao Chen, Shuo Jiang et al. — [DramaChain Bench: An End-to-End Benchmark for Short-Drama Generation](http://arxiv.org/abs/2609.00646v1)
  <details><summary>📄 Abstract</summary>
  Commercial short-drama production follows a multi-stage chain: script, storyboard, keyframe imagery, shot-level video, and the finished short drama. Most existing benchmarks evaluate solely the video-generation stage using pre-authored inputs instead of real upstream pipeline outputs. This leaves two critical questions unanswerable: whether each stage adheres to the original script intent (rather than only its immediate input prompt), and whether disparate shots remain coherent after assembly in...
  </details>

- **2026-09-01** — Ruoling Qi, Xuaner Wu, Penghang Liu et al. — [REVISE: Validity-Guided Recovery for Online Revisions in Agent Workflows](http://arxiv.org/abs/2609.00643v1)
  <details><summary>📄 Abstract</summary>
  Agent revisions expose a fundamental correctness--efficiency trade-off during concurrent execution. Discarding ongoing work preserves latest-version correctness but wastes progress that may remain valid, whereas reusing prior work preserves efficiency but risks propagating stale state into outputs and tool effects. Existing recovery strategies resolve this trade-off in an imbalanced way with coarse-grained policies: they either favor efficiency by allowing potentially stale work to continue, or ...
  </details>


### 📂 unlearning
*机器遗忘 / Machine Unlearning* — 1 papers

- **2026-09-02** — Evžen Wybitul, Tim G. J. Rudner, Christian Schroeder de Witt — [Entangled Representations Amplify Collateral Damage in Unlearning](http://arxiv.org/abs/2609.02285v1)
  <details><summary>📄 Abstract</summary>
  A long-held intuition in interpretability research is that representational entanglement, the sharing of structure between knowledge domains in a neural network, makes unlearning harder. While the intuition is widespread, it has never been directly tested in a controlled experiment. We present a way to do so: by repurposing Selective Gradient Masking (SGTM), we train a suite of six 254M-parameter language models on English Wikipedia with graded levels of disentanglement between biology and non-b...
  </details>


### 📂 survey
*综述与系统化 / Surveys & Systematization* — 10 papers

- **2026-09-02** — Ming Jiang, Erwu Liu, Xinyu Qu et al. — [A Survey of Decentralized Physical Infrastructure Network,Research Directions, and Open Challenges](http://arxiv.org/abs/2609.02125v1)
  <details><summary>📄 Abstract</summary>
  The Decentralized Physical Infrastructure Network (DePIN) represents a transformative paradigm that redefines the construction, operation, and governance of Information and Communication Technology (ICT) infrastructure in the Web 3.0 era. DePIN integrates physical resources, such as networking equipment, storage, and computing power, with decentralized digital governance, forming a self-incentivized ecosystem that is collaboratively built, shared, and governed by the community. It provides a fou...
  </details>

- **2026-09-02** — Jiska Beuk, Gerasimos Spanakis — [WinoQueer-NL: Assessing Bias in Dutch Language Models toward LGBTQ+ Identities](http://arxiv.org/abs/2609.02651v1)
  <details><summary>📄 Abstract</summary>
  While English language models have been widely examined for anti-queer bias, Dutch models remain understudied. To address this gap, we developed a culturally and linguistically adapted Dutch dataset based on the English WinoQueer benchmark, containing pairs of stereotypical and counter-stereotypical sentences. To validate and expand it, we conducted an online survey with 43 Dutch queer participants, confirming 145 of 171 stereotypes as culturally relevant and identifying 22 new biases through fr...
  </details>

- **2026-09-02** — E. I. Makarenko, A. V. Ivlev, S. Bialy et al. — [Can diffuse X-rays be important in driving photoionisation in molecular clouds?](http://arxiv.org/abs/2609.02648v1)
  <details><summary>📄 Abstract</summary>
  The ionisation balance in molecular clouds is regulated by several ionising sources, including cosmic rays, X-rays, and ultraviolet radiation. Their relative importance depends on the local physical conditions and on the shielding column density. We compute the contribution of the large-scale diffuse X-ray radiation field to the ionisation in molecular clouds in the absence of strong local X-ray sources, such as young stars. Our goal is to quantify its significance relative to the Galactic cosmi...
  </details>

- **2026-09-02** — Gabriel Stefan, Sergiu Nisioi — [PolERo: Studying Political Evasion in Romanian](http://arxiv.org/abs/2609.02391v1)
  <details><summary>📄 Abstract</summary>
  Political evasion refers to responses that engage with a question while withholding the requested information. Recent NLP work frames political evasion as a classification task using a two-level taxonomy of response clarity and fine-grained evasion strategies. Existing work on response clarity and evasion classification is limited to English, leaving open whether the taxonomy and model behavior transfer across languages and political contexts. We introduce PolERo, a dataset of 3,574 human-annota...
  </details>

- **2026-09-01** — Himil Vasava, Ming Jiang — [Beyond Scores: Understanding LLM-as-a-Judge Mechanisms in Summarization Evaluation](http://arxiv.org/abs/2609.01604v1)
  <details><summary>📄 Abstract</summary>
  LLM-based evaluators of natural language generation (NLG) quality are widely deployed as scoring tools and as automated training signals, yet the internal procedure by which they assign a rating remains poorly understood. We investigate this procedure mechanistically through an eight-attack perturbation taxonomy across the Readability and Adequacy dimensions of NLG quality, a generation pipeline that produces paired clean and corrupt summaries with controlled error intensity and explicit token-l...
  </details>

- **2026-09-01** — Kshitij Tayal, Arun Sharma, Genta Indra Winata et al. — [The Rise of Verbal Reinforcement Learning](http://arxiv.org/abs/2609.01597v1)
  <details><summary>📄 Abstract</summary>
  Natural language is emerging as a primary feedback channel for improving language agents, capable of conveying intent, preferences, and causal structure in forms interpretable by both humans and modern language models. We call this paradigm Verbal Reinforcement Learning (VRL) and offer the first unified account of it. We organize the field around a single axis, \textit{when} verbal feedback takes effect in an agent's lifecycle and \textit{what} it modifies, yielding three pillars: (1) \textbf{La...
  </details>

- **2026-09-01** — Nicolò Alessandro Girardini, Unchitta Kan, Eduardo López et al. — [Behavioral calibration of mobile-phone GPS data for population-representative analyses](http://arxiv.org/abs/2609.01042v1)
  <details><summary>📄 Abstract</summary>
  Mobile phone mobility data have transformed the study of human behavior, but demographic and behavioral biases can compromise their representativeness and distort population-level inference. Existing calibration approaches primarily address demographic and geographic representativeness, leaving behavioral discrepancies largely uncorrected. Here we introduce the Behavioral Population (BePop) framework, which jointly calibrates mobility data to representative demographic and behavioral distributio...
  </details>

- **2026-09-01** — Elizaveta Sivak, Emily M. Cantrell, Thomas Emery et al. — [Births are difficult to predict even with rich survey and full-population register data](http://arxiv.org/abs/2609.01194v1)
  <details><summary>📄 Abstract</summary>
  Major life events have proven difficult to predict. Does this reflect limits of theory, data, and algorithms, or the large role of chance? We examine one outcome - having a child within three years - through a near-ideal setting for prediction: a data challenge where 147 researchers predicted births for Dutch residents aged 18-45, using survey data and full-population registers. Methods ranged from logistic regression to a large language model and transformers. Predictions were moderately accura...
  </details>

- **2026-08-31** — Mike Thelwall — [Do Large Language Models Favour Any Research Topics?](http://arxiv.org/abs/2609.00323v1)
  <details><summary>📄 Abstract</summary>
  Large Language Models (LLMs) can estimate the quality of published journal articles, potentially supporting human assessment when evaluations are needed. Whilst there are reasons to believe that LLMs may have biases in this role, there is no statistically strong evidence yet. The current article addresses this gap with an exploration of the types of articles that attract high or low LLM scores in 73,489 articles from 15 health and life sciences journals. Based on comparing the words in the title...
  </details>

- **2026-08-31** — Kartik Ravisankar, Hojat Abdolanezhad, Daniel Capo et al. — [Autoresearch for Marketplace Catalogs: From Legacy Forms to AI-Native Matching](http://arxiv.org/abs/2609.00274v1)
  <details><summary>📄 Abstract</summary>
  Two-sided service marketplaces are moving from deterministic request-form intake to AI-native probabilistic matching, enabled by large language models (LLMs) that infer intent, preferences, and latent constraints from natural language. Relying on inferred intent rather than fixed-form fields forces these platforms to regenerate the provider-side preference taxonomy underwriting matching, search, and pricing: attributes interpretable to service providers while remaining a useful signal for market...
  </details>


### 📂 other
*其他安全相关 / Other Security-Related* — 135 papers

- **2026-09-02** — Zhiyang Ding, Yang Luo, Guangpu Chen et al. — [ACLE-MCP: Attested Capability Leases for Execution-Time Trust in Remote LLM Tool Use](http://arxiv.org/abs/2609.02690v1)
  <details><summary>📄 Abstract</summary>
  Remote Model Context Protocol (MCP) services enable large language model agents to invoke external tools, but OAuth authorization alone does not ensure that a later tool call is executed by the provider-side workload that the relying party intended to trust. An endpoint may remain authorized even after execution shifts to a substituted workload, relies on stale appraisal state, reuses authority transferred from another sender, or traverses an undeclared downstream component. We call this problem...
  </details>

- **2026-09-02** — Anjali Sarvaiya, Shubh Kawa, Lalit Agrawal et al. — [UnCapsTSR: An Unsupervised Transformer-based Image Super-Resolution Approach for Capsule Endoscopy Images](http://arxiv.org/abs/2609.02476v1)
  <details><summary>📄 Abstract</summary>
  Wireless Capsule Endoscopy (WCE) captures and streams video while passing through a patient's Gastrointestinal (GI) tract and is used to examine its irregularities. Although advantageous over conventional endoscopy, WCE suffers from limitations related to capsule size and wireless transmission, resulting in images with coarser resolution. This work presents UnCapsTSR, an unsupervised transformer-based Generative Adversarial Network (GAN) framework for improving the spatial resolution of Low-Reso...
  </details>

- **2026-09-02** — Shachar Don-Yehiya, Leshem Choshen, Omri Abend — [User Feedback Provides a Unique Signal that LLMs Can not Detect](http://arxiv.org/abs/2609.02859v1)
  <details><summary>📄 Abstract</summary>
  Harnessing naturally occurring feedback from user interactions offers a promising learning signal for Large Language Models (LLMs). However, recent studies suggest this feedback is inherently noisy and difficult to leverage effectively. We challenge this conception by demonstrating that user feedback is a highly actionable signal for improvement, and that its perceived ineffectiveness stems from a systematic bias in current evaluation paradigms. To isolate the usefulness of feedback, we construc...
  </details>

- **2026-09-02** — Wooyoung Jung, Prosper Babon-Ayeng — [Large Language Model-Driven Context-Aware Eco-Feedback Generation and Evaluation](http://arxiv.org/abs/2609.02719v1)
  <details><summary>📄 Abstract</summary>
  The objective of this study was to demonstrate the potential of generating eco-feedback that accounted for unique household contextual information, named as context-aware eco-feedback, through a large language model-integrated framework. Previous studies have introduced personalized eco-feedback, mostly relying on household energy use patterns; however, they frequently did not reflect distinct household characteristics, including their persona or non-negotiable routines, leaving eco-feedback ine...
  </details>

- **2026-09-02** — Johannes Brachem, Thomas Kneib — [Reconciling Interpretability with Covariate-Dependent Shape Flexibility in Penalized Transformation Models for Distributional Regression](http://arxiv.org/abs/2609.02662v1)
  <details><summary>📄 Abstract</summary>
  A central challenge in distributional regression is to allow the shape of the conditional distribution of the response variable to vary flexibly with covariates while retaining directly interpretable effects on its mean and standard deviation. We extend the penalized transformation model (PTM) family into a conditional-shape PTM, which assigns separate structured additive predictors to the conditional mean, standard deviation, and standardized distributional shape beyond location and scale. A co...
  </details>

- **2026-09-02** — Chengxiao He, Shanghai Yuan, Liuqun Fan et al. — [A Physics-Consistent Benchmark for Contact-Rich Human-Robot Interaction in Assistive Care](http://arxiv.org/abs/2609.02402v1)
  <details><summary>📄 Abstract</summary>
  Conventional task-level evaluation asks whether a robot policy completes a specified action, but can miss failures that emerge only during physical human contact. This limitation is critical in contact-rich assistive tasks, where meaningful evaluation requires a physically responsive human, interaction-quality assessment beyond task success, and a leak-free observer-scorer protocol. We introduce a physics-consistent benchmark for contact-rich human-robot interaction, instantiated in robot-assist...
  </details>

- **2026-09-02** — Menghao Li, Linjie Mu, Yin Wang et al. — [CA-OPD: Confidence-Aware On-Policy Distillation for Structured Visual Prediction](http://arxiv.org/abs/2609.02401v1)
  <details><summary>📄 Abstract</summary>
  Autoregressive vision language models unify heterogeneous perception tasks but are highly susceptible to compounding errors. On-policy distillation (OPD) bridges the training-inference mismatch by training students on their own rollouts. However, unreliable student predictions, especially early in training, can derail the trajectory and degrade the quality of teacher supervision. While recent interleaved distillation methods allow the teacher to verify and replace student tokens, they primarily ...
  </details>

- **2026-09-02** — Alexey Potapov — [AGI Maze Prediction Datasets: A Compact Benchmark for Learning World Dynamics with Transformers](http://arxiv.org/abs/2609.02339v1)
  <details><summary>📄 Abstract</summary>
  World modeling requires a predictive model to maintain and update an internal state adequate for reasoning about the consequences of actions. We introduce the AGI Maze Prediction Datasets and Benchmark, a lightweight controlled testbed for studying this capability in Transformers and other predictive models. Derived from procedurally generated, stateful grid worlds, the benchmark comprises per-step transition prediction, fixed-horizon state prediction, and sequential textual-observation predicti...
  </details>

- **2026-09-02** — Ihor Stepanov, Aleksandr Smechov, Mykhailo Shtopko et al. — [SCX Router: Streaming Zero-Shot Model Selection with a Decoder-KV Classifier and a Real-World Task Ontology](http://arxiv.org/abs/2609.02292v1)
  <details><summary>📄 Abstract</summary>
  The rapid proliferation of large language models (LLMs) and the growing diversity of their applications presents a unique optimization opportunity: selecting the right model for the task, while optimizing for speed, cost, and quality at a per-task level. However, inference endpoints can vary widely in quality, price, latency, context support, tool use, domain expertise, and reasoning behavior. This heterogeneity makes manual heuristics difficult to maintain and unlikely to achieve consistently f...
  </details>

- **2026-09-02** — Mingjie Zheng, Zihao Chen, Wenqing Chen et al. — [CoMerge: Conflict-Driven Preference Optimization for Multi-Task Model Merging](http://arxiv.org/abs/2609.02273v1)
  <details><summary>📄 Abstract</summary>
  Model merging provides an efficient paradigm for constructing multi-task large language models (LLMs) without full model retraining, yet it remains challenged by parameter interference. While existing methods aim to preserve the capabilities of individual expert models and mitigate interference, they generally do not directly learn from the potentially degraded behaviors exposed by naive merging. In this paper, we propose a conflict-driven preference optimization framework for model merging (CoM...
  </details>

- **2026-09-02** — Yunchi Yang, Longlong Li, Cunquan Qu — [PEARL: Path-Entity Aligned Relational Learning with Contextual Subgraphs for Inductive Knowledge Graph Completion](http://arxiv.org/abs/2609.02216v1)
  <details><summary>📄 Abstract</summary>
  Inductive knowledge graph completion (IKGC) aims to predict missing links involving entities unseen during training, requiring models to learn transferable relational and structural patterns. Existing subgraph- and path-based approaches often encode relational paths independently of their surrounding query subgraphs, although the predictive relevance of a path may vary across structural contexts. We propose PEARL, a Path-Entity Aligned Relational Learning framework that models paths as context-c...
  </details>

- **2026-09-02** — Hongshen Gou, Zuyu Zhang, Yuze Sun et al. — [Git4Data: Database-Native Version Control for AI Agents](http://arxiv.org/abs/2609.02106v1)
  <details><summary>📄 Abstract</summary>
  Large Language Model (LLM) agents increasingly explore many candidate states of relational data in parallel, each of which should remain isolated, reproducible, and auditable, preferably through the same SQL interface used for ordinary data work. Existing tools support this requirement only partially: source-code version control does not scale to large datasets, whereas relational databases manage large data efficiently but rarely expose native branching, comparison, and merging. We present Git4...
  </details>

- **2026-09-02** — Weifeng Jiang, Ruirui Chen, Qianren Mao et al. — [Selective Knowledge Edit Reversal via Gated Singular Vector Shrinkage](http://arxiv.org/abs/2609.02091v1)
  <details><summary>📄 Abstract</summary>
  Knowledge editing provides an efficient way to update factual knowledge in large language models. However, malicious edits may introduce safety risks, making it necessary to reverse undesirable editing effects. Existing reversal methods for parameter-modifying edits mainly focus on global removal, which may also erase beneficial edits that should be preserved. In this paper, we study selective reversal of edited knowledge, where the goal is to reverse targeted edited facts while preserving the r...
  </details>

- **2026-09-02** — Zheng Wang, Muchen Li, Renjie Liao et al. — [IDEEA: training-free Input-Dependent stEEring via Activation cluster matching](http://arxiv.org/abs/2609.02089v1)
  <details><summary>📄 Abstract</summary>
  Steering aligns large language models (LLMs) by injecting a bias into selected activations at inference time, offering a far cheaper alternative to weight-update methods such as supervised fine-tuning or reinforcement learning. However, most existing training-free steering methods are input-independent: a single direction is fitted once and shared across all inputs. This is fundamentally limiting as different inputs occupy different regions of the activation space and admit different optimal ste...
  </details>

- **2026-09-02** — Andrew Snowden — [Measures on partial orders](http://arxiv.org/abs/2609.02021v1)
  <details><summary>📄 Abstract</summary>
  We determine the measures (in the sense of Harman--Snowden) on the Fraïssé class of partially ordered sets: the space of measures is a union of a plane, eight lines, and 15 isolated points. This is the first case where the space is not equidimensional, and the first primitive case in which it has dimension at least two.   ChatGPT was used to obtain many arguments. The writing was done entirely by the author.
  </details>

- **2026-09-02** — Masahiro Kojima, Kentaro Takeda, Ying Yuan — [A staggered seamless dose-optimization design for co-developing monotherapy and combination therapy](http://arxiv.org/abs/2609.01954v1)
  <details><summary>📄 Abstract</summary>
  Contemporary oncology drug development increasingly requires efficient dose-optimization strategies that evaluate monotherapy (Mono) and combination therapy (Combo) while balancing activity, efficacy, and tolerability. We propose a staggered seamless phase I/II design for settings in which a novel agent is evaluated alone and in combination with an established therapy. In phase I, Mono dose finding begins first, and Combo subtrials can be opened adaptively once a prespecified combination-initiat...
  </details>

- **2026-09-02** — Yihang Chen, Yuxiang Chen, Yuxuan Huang et al. — [Bilevel Coordinated Reflection: A Game-Theoretic Approach to Multi-Agent LLM Systems](http://arxiv.org/abs/2609.02750v1)
  <details><summary>📄 Abstract</summary>
  Multi-agent LLM systems commonly use an orchestrator to decompose a task for a team of workers and then improve through textual reflection. Despite strong empirical results, these systems lack a unified account of coordination, memory improvement, and the role of external verification. We model orchestrator-worker interaction as a bilevel coordination game: under bounded coupling, the workers' local-update game is an approximate potential game whose equilibrium slack is controlled by decompositi...
  </details>

- **2026-09-02** — Song Zhou, Songge Zhang, Lanting Shi et al. — [Colossal reversible conductivity switching by room-temperature oxygen-vacancy ordering in Aurivillius oxide films](http://arxiv.org/abs/2609.02629v1)
  <details><summary>📄 Abstract</summary>
  Oxygen vacancies are central to the functionality of oxides, yet they typically exist as randomly distributed point defects, limiting the ability to precisely manipulate their collective behavior. Here, we report the room-temperature formation of a long-range-ordered oxygen-vacancy superstructure in single-crystalline Aurivillius-phase Bi2WO6 thin films via a mild nitrogen-plasma treatment. This structural transformation unlocks a colossal, reversible modulation of electrical conductivity by mor...
  </details>

- **2026-09-02** — Mason Youngblood, Katie Mudd, Manuel Anglada-Tort et al. — [Collective creativity in hybrid societies](http://arxiv.org/abs/2609.02620v1)
  <details><summary>📄 Abstract</summary>
  Generative AI is changing how cultural artifacts are created and circulated, and with it our understanding of creativity itself. Researchers disagree about whether these tools enrich or impoverish culture, and we argue that much of that disagreement comes from conflating two distinct components of creativity: novelty, a property of single artifacts, and diversity, a property of populations. We argue further that creativity in the context of generative AI is best understood as a property of hybri...
  </details>

- **2026-09-02** — Ana Loureiro, Walter Van Assche — [Ratio and limiting zero distribution asymptotics for symmetric multiple orthogonal polynomials](http://arxiv.org/abs/2609.02801v1)
  <details><summary>📄 Abstract</summary>
  We investigate the ratio asymptotics and the asymptotic zero distribution of a sequence of polynomials that satisfy a recurrence relation of order $r+1$ with all recurrence coefficients, except the last one, equal to zero. Such a sequence is part of a system of multiple orthogonal polynomials and it satisfies the symmetry property $P_n(ω_{r+1} z) = ω_{r+1}^n P_n(z)$, where $ω_{r+1}$ is the primitive $(r+1)$th root of unity. We consider the unbounded regime in which the recurrence coefficients ex...
  </details>

- **2026-09-02** — Zehan Lin, Shengxin Liu, Biaoshuai Tao et al. — [Almost Envy-Freeness for Additive Mixed Manna with Entitlements: Deterministic and Randomized Guarantees](http://arxiv.org/abs/2609.02724v1)
  <details><summary>📄 Abstract</summary>
  We investigate the fair allocation of indivisible items among agents with asymmetric entitlements in mixed manna settings, where the items consist of both goods and chores. For additive valuations, we establish that weighted envy-free up to one item (WEF1) allocations always exist and can be computed in polynomial time. We also study fair and efficient allocation and show that weighted envy-freeness up to one transfer (WEF1T) is compatible with fractional Pareto optimality (fPO) for every mixed-...
  </details>

- **2026-09-02** — Pritthijit Nath, Sebastian Schemm, Peter Haynes et al. — [Online Reinforcement Learning in the Met Office Unified Model through Distributed Model-Agent Coupling](http://arxiv.org/abs/2609.02566v1)
  <details><summary>📄 Abstract</summary>
  Machine-learnt corrections can complement numerical weather prediction only if they adapt to the evolving model state while preserving dynamical consistency and numerical stability. To test this within a global forecasting model, we couple the Met Office (UKMO) Unified Model (UM) with distributed RL agents through rank-local tensors. A DDPG actor shares weights across the 70 vertical model levels of each atmospheric column and applies bounded potential-temperature corrections to the model tenden...
  </details>

- **2026-09-02** — Irina Proskurina, Guillaume Metzler, Antoine Gourru et al. — [Debias-SparseGPT: Bias-Aware Pruning for Large Language Models](http://arxiv.org/abs/2609.02496v1)
  <details><summary>📄 Abstract</summary>
  Model compression techniques such as pruning and quantization facilitate the efficient deployment and acceleration of Large Language Models (LLMs). However, recent studies show that weight sparsification methods, such as SparseGPT, can amplify existing biases in models, with outputs varying significantly depending on persona cues in the prompt. In this paper, we introduce Debias-SparseGPT, a post-training pruning method incorporating representational debiasing using a second-order term defined o...
  </details>

- **2026-09-02** — Egecan Çelik Evgin, İlknur Karadeniz, Olcay Taner Yıldız — [Improving Health Literacy through Lay Summarization of Radiological Reports: An Evaluation of BioNER and Retrieval-Augmented Generation](http://arxiv.org/abs/2609.02396v1)
  <details><summary>📄 Abstract</summary>
  Radiology reports are written primarily for clinicians, and their specialized terminology often makes them difficult for patients to interpret. As a result, many patients turn to publicly available Large Language Models (LLMs) to help explain their reports, despite well-documented risks of factual inaccuracies and hallucinations. Automated lay-summary generation has emerged as a promising alternative, yet the effectiveness of retrieval-enhanced and clinically informed approaches for radiology-sp...
  </details>

- **2026-09-02** — Dong-Ping Fu, Michihisa Takeuchi — [Quark masses and mixing in the D_5 model under spontaneous CP violation](http://arxiv.org/abs/2609.02312v1)
  <details><summary>📄 Abstract</summary>
  It is known that CP violation occurs in flavor physics, and the CKM matrix is complex. We investigate the Yukawa sector of a four-Higgs model based on D_5 symmetry. To understand all possible sources of CP violation in the Yukawa sector, we systematically analyze the impact of all possible representation assignments of the left-handed and right-handed quark fields under the D_5 group. After imposing the conditions of non-block-diagonal CKM matrix and the absence of massless quarks, we find that ...
  </details>

- **2026-09-02** — Chao-Kai Wen, Yen-Cheng Chan, Lung-Sheng Tsai et al. — [Agentic UE-CoMIMO for 6G Terminals: From Virtual Antenna Augmentation to AI-Native Virtualization](http://arxiv.org/abs/2609.02290v1)
  <details><summary>📄 Abstract</summary>
  End-user-centric collaborative MIMO (UE-CoMIMO) lets nearby devices form a virtual multi-antenna terminal to overcome the antenna limitations of individual user equipment. Extending such cooperation to communication, sensing, computing, and task-relevant information exchange requires a control layer that can interpret user intent, select cooperation mechanisms, and replan as conditions change. This article introduces Agentic UE-CoMIMO, in which device micro-agents, a smartphone or CPE hub agent,...
  </details>

- **2026-09-02** — Youqi Wu, Farzan Farnia — [Do Large Language Models Capture the Diversity in their Training Data?](http://arxiv.org/abs/2609.02275v1)
  <details><summary>📄 Abstract</summary>
  Large language models are trained to model conditional distributions over text, yet it remains inadequately understood whether they capture the full diversity of plausible outputs present in their training data. We study this question through an information-theoretic lens by comparing the conditional entropy of model-generated outputs with that of the corresponding training data. Given paired input-output samples, we use conditional entropy and its matrix-based analogue based on von Neumann entr...
  </details>

- **2026-09-02** — Weixiang Hong, Hongting Du, Jiayue Tang et al. — [Prototype-guided transfer of sparse literature knowledge for electrolyte additive discovery](http://arxiv.org/abs/2609.02209v1)
  <details><summary>📄 Abstract</summary>
  Electrolyte additive discovery remains challenging because experimentally validated molecules are sparse, whereas accessible chemical spaces are vast and largely unlabeled. This challenge is amplified in lithium-ion batteries, where additive performance arises from coupled interfacial reactions rather than a single molecular property. Here, we develop a prototype-guided molecular intelligence, ProtoMI, a literature-driven framework that learns transferable structural priors from reported electro...
  </details>

- **2026-09-02** — Yiran Zhao, Lu Zhou, Liming Fang et al. — [Beyond Outcome Gaps: Process-Aware Fairness Diagnosis for LLM-based Multi-Agent Decision Systems](http://arxiv.org/abs/2609.02092v1)
  <details><summary>📄 Abstract</summary>
  LLM-based multi-agent systems (MAS) are increasingly considered for high-stakes decision-making, yet outcome-based fairness audits can miss where risks arise within the decision trajectory. We present SCOPED-Hiring, a process-aware fairness diagnosis pipeline for LLM-based hiring MAS. SCOPED-Hiring constructs controlled resume variants, runs role-based hiring committees, logs over 311K structured decision trajectories, and converts trajectory fields into quantitative fairness signals organized b...
  </details>

- **2026-09-02** — Yongshi Ye, Tian Lan, Feihu Jiang et al. — [CHIME: Credit-Aware Hierarchical Memory Evolution for Long-Horizon Agentic Planning](http://arxiv.org/abs/2609.02074v1)
  <details><summary>📄 Abstract</summary>
  Planning is a central capability that enables agents to decompose complex long-horizon tasks into manageable steps. Test-time search and training-based methods improve planning but incur high inference costs or require expensive training data. Self-evolving memory instead accumulates reusable experience from agent interaction outcomes into an external memory bank, so planning capability keeps improving at inference time without parameter updates. However, existing self-evolving memory methods sh...
  </details>

- **2026-09-02** — Fangye Wang, Yunjin Gu, Haowen Lin et al. — [SPAR: Enhancing Industrial-Scale Generative POI Recommendation via Real-World Spatial Perception](http://arxiv.org/abs/2609.02062v1)
  <details><summary>📄 Abstract</summary>
  Generative Point-of-Interest (POI) recommendation, autoregressively generating a target POI's semantic ID (SID), holds great promise for Location-Based Services, where a recommendation helps only if the user can reach it. Yet, existing methods operate within an interest space defined by behavior sequences and collaborative signals, where geography enters only as a textual attribute of the SID, leaving no explicit mechanism to learn or preserve how urban places are related by distance, direction,...
  </details>

- **2026-09-02** — Xinan Zhou — [Pre-Strings Lectures on Holographic Correlators and Analytic Bootstrap](http://arxiv.org/abs/2609.01986v1)
  <details><summary>📄 Abstract</summary>
  Over the past decade, the bootstrap strategy has transformed the computation of holographic correlators and revealed structures suggesting an emerging scattering amplitude program in AdS. These notes, which are an extended version of the five lectures delivered at the Pre-Strings 2026 School, give a pedagogical introduction and synthesis of these developments. We start with a quick reminder of the essentials of CFT and a brief review of AdS perturbation theory. We then demonstrate in detail the ...
  </details>

- **2026-09-01** — Zichuan Li, Jian Cui, Ashley Chen et al. — [What's in Your Agent's Context? Context Privilege Escalation Attacks against AI Agent Harness](http://arxiv.org/abs/2609.01222v2)
  <details><summary>📄 Abstract</summary>
  Real-world, high-profile AI agent harnesses often rely on vendor-proprietary or opaque designs for context assembly, leaving the sources and underlying logic of assembled context poorly understood and the resulting security risks largely unexplored. In this paper, we present the first systematic analysis of context assembly designs in real-world AI agent harnesses. We study and uncover how an agent harness is designed to collect and assemble context from diverse sources, and identify a set of pr...
  </details>

- **2026-09-01** — Ramit Pahwa, Parivesh Priye, Apoorva Beedu — [VoiceLongMemEval: Do Assistants Remember How You Sounded?](http://arxiv.org/abs/2609.00570v2)
  <details><summary>📄 Abstract</summary>
  With the growing scale of multi-agent architectures and large language models, deployed AI assistants are increasingly tasked with reasoning over long, continuous, multi-session conversation histories. Current benchmarks evaluate this dialogue history as information retrieval over long horizon, temporal reasoning, or knowledge updates, while crucially ignoring the fundamental dynamics of human-agent interaction, i.e. how they said it. To address this gap, we present VoiceLongMemEval (VLME) bench...
  </details>

- **2026-09-01** — Ritwesh A. Kumar, Som Tripathi, Peja Matthews et al. — [Automated Maize Ear Phenotyping Using 3D Reconstructions](http://arxiv.org/abs/2609.01921v1)
  <details><summary>📄 Abstract</summary>
  Maize kernel traits such as row number, kernels per row, and kernel size vary largely for genetic reasons and are consistently associated with regions of the genome that influence yield. Manual measurement of these traits, however, cannot keep pace with the volume of maize generated in a breeding program. To address this, we developed and validated a fully automated pipeline for extracting these traits from 3D point clouds of corn ears, built on a recently developed video-to-point-cloud platform...
  </details>

- **2026-09-01** — Kunal Jadhav, Siddhesh More — [Grounded, Compute-Efficient LLM Policy Agents for Energy-Poverty Equity in Physically-Constrained Peer-to-Peer Energy Markets](http://arxiv.org/abs/2609.01918v1)
  <details><summary>📄 Abstract</summary>
  Energy poverty is nearly absent from NLP-for-social-good, and the little existing work is either static retrieval/QA or relies on carbon-intensive cloud LLMs, a self-defeating "computational irony" for a humanitarian setting. We present EqGrid, a closed-loop simulation in which a low-frequency, open-weight LLM policy agent sets price and carbon bounds and targeted subsidies over a community of empirically-grounded household personas, while high-frequency multi-agent RL traders clear a continuous...
  </details>

- **2026-09-01** — Yunqin Zhu, Feng Qiu, Yao Xie — [OutageDiT: A Generative Foundation Model for Power Outage Forecasting and Scenario Simulation](http://arxiv.org/abs/2609.01896v1)
  <details><summary>📄 Abstract</summary>
  Power-outage planning requires scenarios before an event occurs. These scenarios must represent uncertainty in magnitude, timing, and duration while preserving temporal dependence. However, severe events are rare, and data from any single region contain few examples of extreme outage and restoration patterns. To address this challenge, we introduce OutageDiT, a foundation model for generating seven-day outage trajectories at quarter-hour resolution, trained on outage and weather records across t...
  </details>

- **2026-09-01** — Marc Bara — [Epistemic Sybil Resistance: Multiplying AI Agents Without Multiplying Evidence](http://arxiv.org/abs/2609.01873v1)
  <details><summary>📄 Abstract</summary>
  Multi-agent AI systems improve inference by spawning agents and synthesizing reports. But another agent is not another observation: apparently independent reports may descend from the same evidence, and genuinely independent evidence can produce nearly identical reports. We formalize this as an epistemic Sybil problem. A report Z is an epistemic Sybil extension relative to reports R when I(Theta; Z | R) = 0. No report-only aggregator can generally distinguish replication from independent corrobo...
  </details>

- **2026-09-01** — Jundong Hu, Shekar Ramachandran — [The Memory Trust Gap: Capability-Dependent Failures in Persistent-Memory Agents](http://arxiv.org/abs/2609.01852v1)
  <details><summary>📄 Abstract</summary>
  Persistent memory supports personalized agents, but a stale stored fact can override current authoritative evidence without warning. We study when this harm begins as model capability changes. We evaluate a frozen, closed-set, action-scored benchmark with 2 suites that represent 2 different meanings of "no memory" (a Benefit suite, unsolvable without the stored fact, and a Safety suite, in which an authoritative tool always holds the correct value), on a same-family model-size series (Qwen3 0.6/...
  </details>

- **2026-09-01** — R. James Cotton, Divya Joshi, Colleen Peyton — [Cross-Model Distillation of a Human-Pose Foundation Model from Unannotated Infant Video for Markerless 3D Pose Estimation](http://arxiv.org/abs/2609.01840v1)
  <details><summary>📄 Abstract</summary>
  Spontaneous movement is one of the earliest windows onto an infant's neuromotor health, and structured clinical instruments that score it are validated early predictors of cerebral-palsy risk. However, they require specially trained raters, are time-consuming, and carry inter-rater variability. This motivates automated, video-based markerless assessment, especially as marker-based motion capture is impractical in infants. Yet the foundation models that make markerless capture possible are traine...
  </details>

- **2026-09-01** — Joseph Axisa — [Architecting Conversational Data Systems for Stateless LLM APIs: The Hydration Proxy Pattern](http://arxiv.org/abs/2609.01834v1)
  <details><summary>📄 Abstract</summary>
  As enterprise platforms transition to conversational reasoning interfaces, the stateless nature of LLM APIs creates an architectural gap. While statelessness enables horizontal scalability for AI providers, it forces client applications to manage the entire burden of conversational state and semantic memory. The work identifies the Hydration Proxy Pattern, an architecture that decouples session persistence from the reasoning engine. The framework ensures platform sovereignty over conversational ...
  </details>

- **2026-09-01** — Fangyi Zhu, Ajay Subramanian, Allison Constant et al. — [Interpretable Symptom Vectors for Depression in a Large Language Model](http://arxiv.org/abs/2609.01832v1)
  <details><summary>📄 Abstract</summary>
  Patients with depression present with diverse symptom profiles, yet clinical practice routinely reduces this variation to a single severity score. Large language models (LLMs) can potentially capture various symptoms and their severity from patient speech. However, how depressive symptoms are represented inside LLMs remains poorly understood, limiting clinical trust. To examine whether internal model activations match clinician judgment, we analyzed the residual stream of Gemma-3-27B-PT using me...
  </details>

- **2026-09-01** — Quan Minh Nguyen, Hoang M. Ngo, Trong Nghia Hoang et al. — [D-FROST: Decentralized Federated pRompt-tuning via Optimal tranSporT for Non-IID and Imbalanced Data](http://arxiv.org/abs/2609.01802v1)
  <details><summary>📄 Abstract</summary>
  Prompt tuning provides a parameter-efficient way to adapt foundation models (FMs) by freezing the pretrained backbone and updating only a small set of learnable prompts. This property makes prompt tuning especially suitable for decentralized federated learning (DFL), where exchanging full-model updates can be prohibitively expensive. However, prompt tuning in DFL introduces new challenges. Prompt sets learned from heterogeneous local data may not be index-wise aligned, making standard decentrali...
  </details>

- **2026-09-01** — Arpan Kumar Mahapatra — [Public-Sharing Labels and Verbatim Field Egress in an MCP-to-A2A Agent Configuration: A Controlled Multi-Model Study](http://arxiv.org/abs/2609.01693v1)
  <details><summary>📄 Abstract</summary>
  Safety properties assessed separately for Model Context Protocol (MCP) tool use and Agent2Agent (A2A) delegation need not describe behavior when one agent uses both. We measure one such behavior in a single controlled MCP-to-A2A configuration: a testbed drives a real-model host across a local MCP and a local A2A leg into an ordered event trace scored by exact deterministic rules (no LLM judge), one restricted decision per trial. In a pre-specified, frozen three-arm design, each of 10 record scen...
  </details>

- **2026-09-01** — Somyaranjan Chakra, Mohit Anand Madhesia, Shradha Mishra — [Statistical Language Competition Model with Dynamic Edge Weighting on a Random Network](http://arxiv.org/abs/2609.01078v2)
  <details><summary>📄 Abstract</summary>
  This paper presents a computational study of language competition dynamics on Erdős--Rényi random networks, extending the foundational Abrams--Strogatz model through two novel contributions: (i) a dynamic edge-weighting mechanism that reinforces social ties between co-minority speakers by an additive increment $Δ$, and (ii) a probabilistic agent-based framework governing language switching via a weighted majority rule. Phase boundaries separating the dominance and coexistence regimes are identif...
  </details>

- **2026-09-01** — Safayat Bin Hakim, Houbing Herbert Song — [Ranked by the Matcher: A Reproducibility Audit of Knowledge Graph Extraction from Threat Reports](http://arxiv.org/abs/2609.01671v1)
  <details><summary>📄 Abstract</summary>
  Security teams and researchers choose knowledge-graph extraction tooling for threat reports on the strength of published triple-F1 scores, yet those scores depend on how predicted triples are matched to gold annotations. We could reimplement the stated matching rule for only five of twelve inspected systems. Re-scoring ten system outputs on shared documents under eight protocols reverses eleven of forty-five pairwise orderings; one fixed prediction set spans 0.16-0.70 F1. On GRID's external 378-...
  </details>

- **2026-09-01** — Vahid Reza Khazaie, Ahmed Y. Radwan, Shaina Raza — [FairLens: Benchmarking Fairness in Vision-Language Models for High-Stakes Decision-Making](http://arxiv.org/abs/2609.01691v1)
  <details><summary>📄 Abstract</summary>
  Vision-language models (VLMs) are increasingly used to make decisions from visual inputs. We introduce FAIRLENS, a benchmark and evaluation framework for measuring both the fairness and the validity of VLM responses in three high-stakes domains: hiring, legal, and healthcare. FAIRLENS pairs real face images spanning gender, race, and age groups with closed- and open-ended questions, giving more than 100K image-question pairs per model, and evaluates responses from four complementary views: demog...
  </details>

- **2026-09-01** — Qingde Li, Qingqi Hong, Zihan Li et al. — [Neuro-Symbolic Geometric Abstraction (NeuSOGA): From Observations to Symbolic Mathematical Representations](http://arxiv.org/abs/2609.01408v2)
  <details><summary>📄 Abstract</summary>
  A fundamental challenge in artificial intelligence is the transformation of observations into explicit symbolic representations suitable for abstraction, interpretation, and reasoning. While modern AI systems achieve remarkable perceptual capabilities through large-scale statistical learning, the resulting knowledge is typically encoded within latent parameters that are difficult to inspect or manipulate analytically. Inspired by Neuro-Symbolic AI and theories of human abstraction, this paper in...
  </details>

- **2026-09-01** — Shuze Daniel Liu, David Simchi-Levi, Claire Chen et al. — [OR-Transformer: Scaling Real-Time Decision-Making to 1,000 Items](http://arxiv.org/abs/2609.01933v1)
  <details><summary>📄 Abstract</summary>
  Modern supply chain operations can require coordinating replenishment across thousands of heterogeneous items under correlated stochastic demand, heterogeneous lead times, and shared fixed ordering costs, yielding observation spaces exceeding $10^4$ dimensions. At this scale, rolling-horizon stochastic mixed-integer linear programs (MILPs) become prohibitively slow, while standard reinforcement learning (RL) methods face increasingly challenging credit assignment in high-dimensional action space...
  </details>

- **2026-09-01** — Moghis Fereidouni, Muhammad Umair Haider, Hassan Sajjad et al. — [GAPS: Dimension-Level Gates for Conditional Activation Steering](http://arxiv.org/abs/2609.01878v1)
  <details><summary>📄 Abstract</summary>
  Activation steering suppresses undesired behaviors in language models by adding a steering vector to the hidden state during generation. Recent conditional methods such as CAST and DSAS improve the behavior-capability trade-off by deciding when to intervene, but once active, they apply the full dense vector to all hidden dimensions, regardless of whether a neuron carries concept information or already lies in the desired regime. We introduce dimension-level conditioning as a complementary axis o...
  </details>

- **2026-09-01** — Usneek Singh, Poorvaja Veera Balaji Kumar, Parth Nanda et al. — [VakyArth: Evaluating Pragmatic Competence in LLMs across Indic Languages](http://arxiv.org/abs/2609.01788v1)
  <details><summary>📄 Abstract</summary>
  Real-world communication often requires pragmatic reasoning: interpreting meanings implied through context and cultural convention rather than stated literally. Existing pragmatic evaluation remains largely limited to English and high-resource languages, leaving Indic languages unexplored despite their linguistic and cultural diversity. We introduce VakyArth, the first pragmatic benchmark for Indic languages, designed as a diagnostic evaluation covering Hindi, Punjabi, Tamil, and Malayalam. Vaky...
  </details>

- **2026-09-01** — Nabira Rashid, Manolis Kellis — [Retrieved but not ranked: surface-form bias in structural retrieval, from mathematics to agent trajectories](http://arxiv.org/abs/2609.01556v1)
  <details><summary>📄 Abstract</summary>
  We evaluate embedding retrieval where surface form and meaning are pulled apart on purpose: retrieving items that share underlying structure but not wording, in two unrelated domains under one protocol, competition mathematics (MathNet-Retrieve; 500 queries, 117,088-item corpus) and embodied-agent trajectories (ALFWorld-derived; 118 queries, 336 trajectories). In mathematics the failure is complete: strict Hit@1 at the heaviest disguise tier is 0.0% for both production embedders (bootstrap 95% C...
  </details>

- **2026-09-01** — Liming Pu, Xiaoxia Li, Yifu Liu et al. — [Explore More, Drift Less: Outcome-Only Reinforcement Learning Can Suffice for Long-Horizon Interactive Agents](http://arxiv.org/abs/2609.01245v1)
  <details><summary>📄 Abstract</summary>
  Reinforcement learning is a natural way to post-train LLM agents for long-horizon interactive tasks judged only by end-of-task verification, yet a shared belief holds that outcome-only RL soon hits a ceiling on small open models. Recent work therefore compensates around the training with denser rewards, SFT priors, skill libraries, curated memory, or multi-agent orchestration. We argue the ceiling is an artifact of two failures of common practice. Signal starvation: group-relative RL with sparse...
  </details>

- **2026-09-01** — Zichuan Li, Jian Cui, Ashley Chen et al. — [What's in Your Agent's Context? Context Privilege Escalation Attacks against AI Agent Harness](http://arxiv.org/abs/2609.01222v1)
  <details><summary>📄 Abstract</summary>
  Real-world, high-profile AI agent harnesses often rely on vendor-proprietary or opaque designs for context assembly, leaving the sources and underlying logic of assembled context poorly understood and the resulting security risks largely unexplored. In this paper, we present the first systematic analysis of context assembly designs in real-world AI agent harnesses. We study and uncover how an agent harness is designed to collect and assemble context from diverse sources, and identify a set of pr...
  </details>

- **2026-09-01** — Ramit Pahwa, Parivesh Priye, Apoorva Beedu — [VoiceLongMemEval: Do Assistants Remember How You Sounded?](http://arxiv.org/abs/2609.00570v1)
  <details><summary>📄 Abstract</summary>
  With the growing scale of multi-agent architectures and large language models, deployed AI assistants are increasingly tasked with reasoning over long, continuous, multi-session conversation histories. Current benchmarks evaluate this dialogue history as information retrieval over long horizon, temporal reasoning, or knowledge updates, while crucially ignoring the fundamental dynamics of human-agent interaction, i.e. how they said it. To address this gap, we present VoiceLongMemEval (VLME) bench...
  </details>

- **2026-09-01** — Elias Stengel-Eskin, Newton Sander, Carlos Bonetti et al. — [GlossoGen: Emergent Language in Complex Multi-Agent LLM Interactions](http://arxiv.org/abs/2609.01491v1)
  <details><summary>📄 Abstract</summary>
  The growing rate at which LLM agents interact with one another raises key questions about language evolution in multi-LLM-agent settings, with implications for safety and monitorability as well as for linguistic accounts of LLMs. To address these questions, we introduce GlossoGen, a novel platform for studying multi-agent language evolution in complex scenarios. Within GlossoGen, we build the SaveVeyru scenario, which requires agents with partial information to communicate under pressure. We fin...
  </details>

- **2026-09-01** — Aryeh Lev Zabokritskiy — [Binary Multiple-Node-Erasure-Correcting Codes over Complete Graphs: Constructions, q-Ary Metric Balls, and Duality](http://arxiv.org/abs/2609.01474v1)
  <details><summary>📄 Abstract</summary>
  We study linear codes whose coordinates are the ordinary edges and self-loops of complete undirected graphs; a node erasure removes all coordinates incident with a failed vertex. The construction results are binary. For triple-node erasures, we extend the published cyclic construction by allowing a suitable cyclic check slope to depend on the prime graph length. An explicit determinant test proves that one of three fixed slope choices works at infinitely many prime lengths, unconditionally, and ...
  </details>

- **2026-09-01** — Charles Corbière, Léo Machado, Aubin Charley et al. — [RadMatch: Auditable Radiology Report Evaluation via Finding-Level Matching](http://arxiv.org/abs/2609.01470v1)
  <details><summary>📄 Abstract</summary>
  As AI systems are increasingly used to draft radiology reports, reliably evaluating their clinical quality remains a critical challenge. Large language model (LLM)-based metrics are now the best-correlated with radiologist judgment, yet they output a single opaque score that neither a clinician nor a model builder can easily interpret or audit. We introduce RadMatch, a multi-stage, LLM-based metric that decomposes report comparison into a structured finding-level matching with significance-aware...
  </details>

- **2026-09-01** — Mikhail Sonkin, Tanja Baeumel, Daniil Gurgurov et al. — [Separating Syntax from Language: A Mechanistic Account of Translation in Multilingual LLMs](http://arxiv.org/abs/2609.01356v1)
  <details><summary>📄 Abstract</summary>
  Multilingual large language models (mLLMs) achieve strong performance in machine translation, yet our understanding of the mechanisms by which they transform representations from one language to another remains incomplete. Prior work suggests that translation decomposes into separable processes within an mLLM, where conceptual content is first represented independently, followed by a production into language-specific form. In this work, we show that translation is even more modular than previous...
  </details>

- **2026-09-01** — Kai Guan, Minchao Jiang, Ruichen WangLi et al. — [Seeing the World and the Self from Egocentric Video](http://arxiv.org/abs/2609.01276v1)
  <details><summary>📄 Abstract</summary>
  Complete 3D perception from egocentric video requires recovering the surrounding scene and the wearer's full-body motion in a shared metric frame. Existing methods typically address scene reconstruction and motion estimation separately: scene reconstruction methods ignore the wearer, whereas motion estimation methods lack explicit scene geometry and often depend on external trajectories. Joint recovery is challenging because the two tasks exhibit asymmetric visibility and require different predi...
  </details>

- **2026-09-01** — Xin Sun, Daniel Ståhl, Kristian Sandahl et al. — [Continuous Autonomous Refactoring: A Research Roadmap for AI-Driven Code Quality Maintenance](http://arxiv.org/abs/2609.01236v1)
  <details><summary>📄 Abstract</summary>
  Large language models have shown promising capabilities in code refactoring, but existing approaches remain limited to method-level tasks. In this paper, we envision LLM-based refactoring as a continuous component of software maintenance rather than a tool invoked only for occasional manual refactoring. Under this vision, AI agents continuously monitor, evaluate, and improve codebases against explicit and evolving notions of software quality. We present a roadmap organized around five dimensions...
  </details>

- **2026-09-01** — Somyaranjan Chakra, Mohit Anand Madhesia, Shradha Mishra — [Statistical Language Competition Model with Dynamic Edge Weighting on a Random Network](http://arxiv.org/abs/2609.01078v1)
  <details><summary>📄 Abstract</summary>
  This paper presents a computational study of language competition dynamics on Erdős--Rényi random networks, extending the foundational Abrams--Strogatz model through two novel contributions: (i) a dynamic edge-weighting mechanism that reinforces social ties between co-minority speakers by an additive increment $Δ$, and (ii) a probabilistic agent-based framework governing language switching via a weighted majority rule. Phase boundaries separating the dominance and coexistence regimes are identif...
  </details>

- **2026-09-01** — Shiyu Li, Zi-Yuan Hu, Shijia Huang et al. — [SinkPruner: Sink-Free Visual Token Pruning for Multimodal Large Language Models](http://arxiv.org/abs/2609.01004v1)
  <details><summary>📄 Abstract</summary>
  Despite their strong multimodal understanding ability, multimodal large language models (MLLMs) incur substantial computational overhead when processing long visual token sequences. To reduce inference costs, recent studies have explored visual token pruning through vision-centric or text-guided strategies. However, these methods often overlook high-norm outlier tokens, i.e., tokens with abnormally large feature norms, leading to suboptimal pruning decisions. In this work, we show that such high...
  </details>

- **2026-09-01** — Yinuo Xu, Yuwei Liang, Jianjie Cheng et al. — [DualStake: Dual-Path Confidence Calibration in Deep Research Agents](http://arxiv.org/abs/2609.00935v1)
  <details><summary>📄 Abstract</summary>
  Deep Research agents tackle knowledge-intensive tasks through multi-round retrieval and decision-oriented generation. However, these agents suffer from severe overconfidence, making their expressed confidence unreliable for user trust and downstream abstention. To address this, we augment the Deep Research pipeline with step confidence elicitation after each retrieval, building on the commonly used post-answer verbalized confidence. Interestingly, we find that Evidence Confidence (E-Conf), elici...
  </details>

- **2026-09-01** — Koshiro Aoki, Ryota Takatsuki, Gouki Minegishi et al. — [In-Context Neurofeedback: Can LLMs Control Their Internal Representations through Privileged Access?](http://arxiv.org/abs/2609.00904v1)
  <details><summary>📄 Abstract</summary>
  Whether large language models (LLMs) can control their own internal representations matters for both machine metacognition and AI safety. A recent study applied neurofeedback to LLMs and claimed that they can control their internal representations. However, the reported control may rely on superficial mechanisms rather than genuine internal access because the control targets in that study are not privileged, meaning that a third party can infer them from the prompt. We redesign the neurofeedback...
  </details>

- **2026-09-01** — Xingyu Qu, Siyuan Lu, Zhiyu Chen et al. — [CacheBridge: Efficient Cross-Model KV Cache Transfer](http://arxiv.org/abs/2609.00891v1)
  <details><summary>📄 Abstract</summary>
  Sharing context between LLMs in a multi-model system requires the receiving model to prefill the shared prefix because KV caches are model-specific. Recent closed-form cross-model KV transfer, hereafter Full-Head Mapping, avoids this replay by fitting a training-free affine mapper from source to target caches. However, its full-head design maps each target KV head from every source KV head in the selected layers, making transfer quality sensitive to architectural differences and causing mapper s...
  </details>

- **2026-09-01** — Michail Takaronis, Athanasia Kollarou, Georgios Kavallieratos et al. — [Using LLMs to Elicit Security Requirements for Service-Oriented Cyber Ranges](http://arxiv.org/abs/2609.00886v1)
  <details><summary>📄 Abstract</summary>
  Cyber ranges are complex environments comprising many interacting components and stakeholders with different security concerns. The Service-Oriented Cyber Range (SOR) is no exception, particularly when it comes to training scenarios targeting critical infrastructure. Security concerns are translated into security requirements, the elicitation of which is usually difficult and time-consuming. This work examines how large language models can assist in eliciting security requirements for a service-...
  </details>

- **2026-09-01** — Runpeng Dai, Kaili Huang, Changsung Kang et al. — [It Takes Two to Match: Co-Evolving Generative Retriever with Reinforcement Learning](http://arxiv.org/abs/2609.00638v1)
  <details><summary>📄 Abstract</summary>
  Retrieval is the first stage of modern search and advertising systems, selecting a candidate set from a large item universe for downstream ranking and auction. Recent work increasingly leverages LLMs to improve retrieval through query expansion, data synthesis, and retrieval-feedback training. However, the generative component is typically used for query-side augmentation, while final matching is still delegated to a downstream retriever. We introduce CoGR, a retrieval framework that instead tra...
  </details>

- **2026-09-01** — Suryaansh Jain, Rahasya Barkur, Vishal G et al. — [A Glance Is All You Need: Single-Pass Fine-Grained Image Captioning with SimLoss](http://arxiv.org/abs/2609.00591v1)
  <details><summary>📄 Abstract</summary>
  An image may be worth a thousand words, but most captioning models describe it in only a few. Modern vision-language models produce fluent high-level captions, yet routinely miss the attributes, counts, textures, materials, and spatial relations that make an image visually specific. Recent multi-stage systems recover some of these details through generation, decomposition, verification, and rewriting, but they do so at the expense of substantially higher inference latency.   We propose SimLoss, ...
  </details>

- **2026-09-01** — Alexandre Clin Deffarges, Nataliya Kosmyna, Pattie Maes — [Socrates went Nuclear: Comparing Interaction Strategies for AI systems in a Learning Context using Brain Sensing](http://arxiv.org/abs/2609.00584v1)
  <details><summary>📄 Abstract</summary>
  Does unrestricted AI access bypass the cognitive effort required for learning, or does it streamline knowledge acquisition? This paper reports on a study where we compare three designs for user-AI interaction in a learning context: (1) an unrestricted conversational bot like ChatGPT, (2) a pedagogically constrained bot that guides through hints without giving final answers, which we refer to as the Socratic mode; and (3) a non-conversational adaptive tutoring system that adjusts difficulty in re...
  </details>

- **2026-09-01** — Seonghyeon Cho, Chanjun Park — [Skill Following: Evaluating Actual Skill Use in Retrieval-Enabled LLM Agents](http://arxiv.org/abs/2609.00549v1)
  <details><summary>📄 Abstract</summary>
  Large Language Model (LLM) agents increasingly rely on external skills, yet standard evaluations obscure whether retrieving these skills actually helps. Aggregate metrics often compare retrieved versus non-retrieved tasks, introducing severe selection bias and failing to isolate the true effect of skill use. To measure this actual-use capability-which we formalize as Skill Following (SF)-we introduce the Retrieval-Invoked Actual-Use Effect (RAE). RAE computes the same-task outcome difference bet...
  </details>

- **2026-09-01** — Ayan Goel, Thomas A. Walton, Amirali Aghazadeh — [Learning Task-Specific Antibody Representations via Function-Aware Masking](http://arxiv.org/abs/2609.00518v1)
  <details><summary>📄 Abstract</summary>
  Antibody-specific language models pretrained via masked language modeling (MLM) learn representations that are critical for downstream sequence design and property prediction tasks. Yet, the corruption process itself is rarely leveraged as a source of inductive bias during pretraining. While preferentially masking complementarity-determining regions (CDRs) improves binding-related predictions, antibodies possess diverse biological priors over a variety of functions. Herein, we introduce function...
  </details>

- **2026-09-01** — Jacob Brinton, Jannik Brinkmann, Mark Crovella et al. — [The Interlingua Hypothesis: LLMs Translate via a Latent Task-agnostic Feature Space](http://arxiv.org/abs/2609.00515v1)
  <details><summary>📄 Abstract</summary>
  Large language models (LLMs) have recently demonstrated improved machine translation performance over strong supervised baselines. This raises questions as to what mechanisms underlie how LLMs perform machine translation between languages. Motivated by recent interpretability findings--namely, that LLMs use massively multilingual latent feature representations to perform language modeling--we propose the interlingua hypothesis. The hypothesis holds that language models translate by reading a sou...
  </details>

- **2026-09-01** — Qingde Li, Qingqi Hong, Jie Tian — [Neuro-Symbolic Geometric Abstraction (NeuSOGA): From Observations to Symbolic Mathematical Representations](http://arxiv.org/abs/2609.01408v1)
  <details><summary>📄 Abstract</summary>
  A fundamental challenge in artificial intelligence is the transformation of observations into explicit symbolic representations suitable for abstraction, interpretation, and reasoning. While modern AI systems achieve remarkable perceptual capabilities through large-scale statistical learning, the resulting knowledge is typically encoded within latent parameters that are difficult to inspect or manipulate analytically. Inspired by Neuro-Symbolic AI and theories of human abstraction, this paper in...
  </details>

- **2026-09-01** — Haoyang Chen, Yi Liu, Jianzhi Shao et al. — [Polished but Unresolved: Identifying Late-Stage Pressure States in Long-Horizon Tool-Use Agents](http://arxiv.org/abs/2609.00823v1)
  <details><summary>📄 Abstract</summary>
  Long-horizon tool-use agents need not only to search and plan, but also to decide when to finalize. We study late-stage pressure states, in which an agent is biased toward submitting a final answer that appears complete and polished while key constraints remain unresolved. We first train a linear probe to show that this pressure state is identifiable from the agent's hidden states. Then, we use activation interventions along this pressure direction and find that shifting the hidden states change...
  </details>

- **2026-09-01** — Nicholas Teh — [Weighted Fair Division of Indivisible Mixed Manna](http://arxiv.org/abs/2609.01580v1)
  <details><summary>📄 Abstract</summary>
  We study weighted fair division of indivisible mixed manna under additive valuations. First, we resolve the general existence open question for weighted envy-freeness up to one item (WEF1), and show that every instance with arbitrary positive entitlements admits a complete WEF1 allocation computable in polynomial time. We then show that existence does not imply any welfare guarantee, i.e., the utilitarian price of WEF1 is infinite, even for two unweighted agents with normalized valuations, commo...
  </details>

- **2026-09-01** — Ema Salkić, Alexander Fichtl, Philipp Ulrich et al. — [A systematic Approach to constructing a Chance-and-Risk Matrix for Semiconductor Supply Chains](http://arxiv.org/abs/2609.01563v1)
  <details><summary>📄 Abstract</summary>
  Semiconductor supply chains face escalating risks from geopolitical tensions, geographic concentration, and rapid technological shifts, yet no scalable system continuously extracts, structures, and prioritizes risk intelligence from public corporate disclosures. We present an end-to-end pipeline that retrieves corporate documents for semiconductor companies and uses large language models (LLMs) to extract the risks and opportunities they describe. It organizes these into a knowledge graph linkin...
  </details>

- **2026-09-01** — Yixuan Liu, Lin Chen, Zhuoqi Liu et al. — [Citing Less Critically: LLMs Reshape the Rhetoric and Reach of Scientific Citation](http://arxiv.org/abs/2609.01432v1)
  <details><summary>📄 Abstract</summary>
  Scientific citations carry rhetorical intent. Scholars may cite prior work positively (supporting), negatively (contrasting), or neutrally (mentioning). As large language models (LLMs) increasingly assist scientific writing, whether they reproduce citations with the same rhetorical intent as humans remains unclear. We introduce a masked-citation task to compare human and LLM-generated citation behavior. For each citation context, an LLM generates a replacement citation sentence, producing a coun...
  </details>

- **2026-09-01** — Maeve Hutchinson, Syed Mahbubul Huq, Mohammad Albinhassan et al. — [InSight: A Benchmark for Agentic Claim Verification in Interactive Visualizations](http://arxiv.org/abs/2609.01383v1)
  <details><summary>📄 Abstract</summary>
  Vision Language Models have demonstrated remarkable proficiency in interpreting static visual artifacts, but modern data analysis is inherently dynamic, requiring the active interrogation of interactive environments. Existing benchmarks are predominantly constrained to static imagery and one-shot question answering and fail to capture the epistemic demands of this domain, where evidence is frequently occluded, distributed across linked views, or conditionally revealed through user agency. In thi...
  </details>

- **2026-09-01** — Shaowen Wang, Ge Zhang, Kairong Luo et al. — [SMELT: Scaling Laws for Compute-Matched MoE Looped Transformers](http://arxiv.org/abs/2609.01343v1)
  <details><summary>📄 Abstract</summary>
  Looped Transformers increase effective depth by iterating a shared block of layers, but most evaluations compare at fixed model size, conflating architectural advantage with extra FLOPs. We study looping on Mixture-of-Experts Transformers while closely matching per-token FLOPs, total non-embedding parameters, and KV cache. Through a series of ablations, we arrive at a recipe we call SMELT (Sparse MoE Transformer, middle layers Loop Twice), which loops the middle half of layers twice while matchi...
  </details>

- **2026-09-01** — Christian Fiedler, Tim Roith — [Consensus-based optimization for linearly separable functions](http://arxiv.org/abs/2609.01317v1)
  <details><summary>📄 Abstract</summary>
  Consensus-based optimization (CBO) is an efficient metaheuristic for global optimisation with attractive mathematical properties, allowing global convergence results even in non-convex settings. In practice it suffers greatly from the curse of dimensionality, as do most particle-based optimisers. Different strategies have been proposed to apply CBO even for high-dimensional optimisation problems, the most prominent being the so-called anisotropic noise model. However, a recent work by Bonandin e...
  </details>

- **2026-09-01** — W. Ross Morrow — [Multi-Head Self Attention is a Parameter Identification Mechanism](http://arxiv.org/abs/2609.01231v1)
  <details><summary>📄 Abstract</summary>
  We prove that a multi-head scaled dot product attention can be viewed as a parameter identification strategy. The ratio of unidentified parameters to the total number of parameters scales like the reciprocal of the number of heads ($1/2 \to 1/(2H)$), meaning models with more heads are structurally more identified. A subtle side effect of the mathematics observation that attention can never be fully identified. Similarly we also show that some bias terms can have no effect on softmax-based attent...
  </details>

- **2026-09-01** — Riyaaz Shaik, Chandru Venkataraman — [REFACTOR-VLA: Unsupervised Library Learning of Typed Motor Programs](http://arxiv.org/abs/2609.01215v1)
  <details><summary>📄 Abstract</summary>
  Most vision-language-action (VLA) models -- OpenVLA, $π_0$, RT-2, RDT-1B -- are monolithic: they emit raw motor commands or short action chunks without organizing behavior into reusable abstractions, so they degrade on long-horizon tasks and resist interpretation. Existing skill-discovery methods sidestep the core question of when two action sequences are behaviorally equivalent, either clustering contrastive embeddings or delegating the judgment to a language model uncalibrated to the robot's d...
  </details>

- **2026-09-01** — Zhilong Song, Lixue Cheng — [Autonomous discovery of new structure-plausibility laws for explainable and rapid crystal diagnosis and screening](http://arxiv.org/abs/2609.01209v1)
  <details><summary>📄 Abstract</summary>
  Crystal generators and tool-using agents propose structures faster than density functional theory (DFT) energy and phonon calculations or experiments can assess them. Deciding which candidates merit expensive assessment is therefore the bottleneck, yet most screens test little beyond atomic overlap and give no chemical reason for failure. Here, our agents generate, test and actively refute two million candidate laws, leaving eight Plausibility Rules for Inorganic Structures (PRIS). These laws en...
  </details>

- **2026-09-01** — Muhammed Saeed, Simon Razniewski — [LLMPEDIA: Browsing, Verifying, and Comparing the Parametric Encyclopedic Knowledge of LLMs](http://arxiv.org/abs/2609.01182v1)
  <details><summary>📄 Abstract</summary>
  Flagship language models appear saturated on benchmarks like MMLU (Hendrycks et al., 2021), scoring above 90% - yet benchmarks test only what the experimenter thought to ask, the availability bias of fixed question sets. LLMPEDIA makes this bias measurable and browsable. We recursively materialized ~1.3M articles from three model families' parametric memory (GPT-5-mini, DeepSeek-V3.2, Llama-3.3-70B) without retrieval, then audited a stratified sample of atomic claims against Wikipedia and a cura...
  </details>

- **2026-09-01** — Anatole Gershman — [Classic AI Scaffolding for LLM Social Agents](http://arxiv.org/abs/2609.01167v1)
  <details><summary>📄 Abstract</summary>
  Large language models can produce locally plausible social turns, but fluent next-turn generation is not enough for social simulation. Human encounters such as restaurant lunches and hotel check-ins are bounded social episodes with roles, scripts, material state, obligations, commitments, timing, and closure conditions. We present EpisodeSim, a hybrid LLM-agent architecture that represents classic-AI structures as natural-language control state interpreted by LLM calls. A World Master maintains ...
  </details>

- **2026-09-01** — Sebastian Steindl, Nikos Voskarides, Alberto Gasparin et al. — [Does task decomposition improve automatic NLG evaluation?](http://arxiv.org/abs/2609.01139v1)
  <details><summary>📄 Abstract</summary>
  The LLM-as-a-judge (LLMaJ) framework has emerged as a promising solution for cheap, reproducible, reference-free Natural Language Generation (NLG) evaluation. Prior work seeks to improve LLMaJ by decomposing evaluation tasks into simpler sub-tasks. In this work, we systematically compare LLMaJ methods with and without decomposition on multiple NLG datasets. We find no evidence that LLMaJ with task decomposition leads to performance gains over a fair baseline that does not use decomposition. Inst...
  </details>

- **2026-09-01** — Marco Simnacher, Georg Keilbar, Benjamin König et al. — [Embedded Conditional Independence Tests for Large Language Model Generated Text with an Application to German Parliament Speeches](http://arxiv.org/abs/2609.00946v1)
  <details><summary>📄 Abstract</summary>
  Conditional independence tests (CITs) test for conditional dependence between two random objects $X$ and $Y$ given a third random object $Z$. Existing CITs have limited applicability to high-dimensional data, especially multimodal data like text. However, we show that such tests are of interest for large language model (LLM) outputs, where we test whether an output $X$ generated from a source text $Z$ carries information about an attribute $Y$ beyond $Z$ itself. For this purpose, we propose embe...
  </details>

- **2026-09-01** — Yumi Lee, Harim Oh, Hyoryung Kim et al. — [Benchmarking Vision-Language Models for Automated Pathology Diagnosis and Report Generation](http://arxiv.org/abs/2609.00866v1)
  <details><summary>📄 Abstract</summary>
  The rapid advancement of vision-language models (VLMs) has accelerated progress in computational pathology; however, whole-slide image (WSI)-based pathology report generation remains limited by the scarcity of large-scale WSI--report datasets and the complexity of mapping spatially distributed visual patterns to structured clinical text. To address this, we introduce a clinically curated Pan-Asia WSI--report dataset of approximately 10,500 pairs from five institutions and establish the REG 2025 ...
  </details>

- **2026-09-01** — Yeonseok Jeong, Soyoung Yoon, Seongjun Lee et al. — [Replacing Training with Memory: Listwise Selection for Text-to-SQL](http://arxiv.org/abs/2609.00834v1)
  <details><summary>📄 Abstract</summary>
  Modern Text-to-SQL systems often follow generate-execute-select pipelines, generating multiple candidate queries then selecting the best one. Listwise selection, by jointly comparing multiple candidates, has been widely adopted, but fine-tuning listwise selectors is costly. We thus propose a fine-tuning-free listwise selector. We replace two major fine-tuning objectives with inference-time strategies: (1) learning selection criteria as ordering and (2) mitigating positional bias. First, we build...
  </details>

- **2026-09-01** — Yuval Alaluf, Omri Avrahami, Guy Bukchin Leshem et al. — [Solaris: Towards Interfaces That Are Generated, Not Coded](http://arxiv.org/abs/2609.00776v1)
  <details><summary>📄 Abstract</summary>
  Digital interfaces are traditionally implemented through intermediate representations such as code, requiring their appearance and behavior to be specified in advance. We introduce Solaris, an interface world model that instead generates an interactive UI directly, frame by frame, in response to user actions. Solaris treats mouse interactions as conditioning signals and autoregressively synthesizes the resulting visual state at interactive speeds. To enable real-time generation while maintaining...
  </details>

- **2026-09-01** — Runsong Jia, Mengjia Wu, Ying Ding et al. — [Agent-Enhanced Heterogeneous Graph RAG for Academic Question Answering](http://arxiv.org/abs/2609.00761v1)
  <details><summary>📄 Abstract</summary>
  Academic question answering requires reasoning over heterogeneous scholarly graphs, where queries range from simple attribute lookups to multi-hop inference across author--paper--venue structures. Existing retrieval-augmented generation (RAG) systems struggle in this setting due to three limitations: (1) fixed retrieval strategies that do not adapt to varying query complexity, (2) the absence of sufficiency evaluation leading to incomplete or misaligned evidence, and (3) a lack of structured ver...
  </details>

- **2026-09-01** — Wendy Zheng, Yinhan He, Liang Wu et al. — [S^3martCirc: Self-supervised Smart Circuit Discovery](http://arxiv.org/abs/2609.00755v1)
  <details><summary>📄 Abstract</summary>
  Large Language Models (LLMs) have demonstrated remarkable performance across diverse tasks, from text summarization to question answering. Despite these capabilities, their black-box nature obscures internal decision-making processes. Mechanistic interpretability (MI) aims to address this by reverse-engineering neural networks into human-understandable algorithms. Current MI approaches for LLMs typically follow a two-stage paradigm: first identifying important components (circuit discovery), whe...
  </details>

- **2026-09-01** — Fenghai Li, Zihan Tang, Haofei Yu et al. — [Can Large Language Models Forecast What Researchers Study Next?](http://arxiv.org/abs/2609.00747v1)
  <details><summary>📄 Abstract</summary>
  Large language models increasingly generate research ideas, yet judging their novelty or feasibility at generation time does not establish whether they anticipate subsequent work. We introduce IdeaForecastBench to evaluate research idea forecasting. Given a community's literature up to a cutoff, a system produces up to five ranked ideas, which are evaluated against later papers. The benchmark comprises 624 rolling episodes across 52 topics, with a fixed retrieve-then-judge protocol and separatel...
  </details>

- **2026-09-01** — Ashiq Shukoor Iqbal, Wilson Wongso, Flora D. Salim — [Do Satellites See Commuters? A Critical Benchmark of Vision Foundation Models](http://arxiv.org/abs/2609.00661v1)
  <details><summary>📄 Abstract</summary>
  Satellite foundation models offer a globally available alternative to census data for commuting origin-destination (OD) generation, yet no study has systematically compared encoder paradigms within a single downstream pipeline. We ablate four satellite vision encoders: language-supervised (RemoteCLIP), self-supervised (DINOv3), and geographically grounded (SatCLIP, AlphaEarth) within an identical WeDAN graph diffusion framework across 1,925 US counties, 325 UK districts, and 14 global cities und...
  </details>

- **2026-09-01** — Qiming Bao, Neşet Özkan Tan, Siyuan Wang et al. — [SciTrue: Reliable Scientific Claim Validation with Frontier and Open Language Models at the NTCIR SciClaimEval Task](http://arxiv.org/abs/2609.00654v1)
  <details><summary>📄 Abstract</summary>
  We describe the SciTrue team's participation in both subtasks of the NTCIR-19 SciClaimEval task~\cite{sciclaimeval}, which asks systems to verify scientific claims against the tables and figures of a paper. Rather than tuning a single model, we benchmark eleven frontier and open multimodal models under one honest, per-sample protocol and combine them with light, transparent post-processing. On the official, blind test leaderboard (Section~\ref{sec:results}), SciTrue placed first by a clear margi...
  </details>

- **2026-09-01** — Teresa DiMeola, Charles Walter, Hong Xiao — [Restrict, Don't Retrain: Inference-Time VLM Guidance for Zero-Shot Aerial Segmentation](http://arxiv.org/abs/2609.00628v1)
  <details><summary>📄 Abstract</summary>
  Global welfare often depends on the correct interpretation of aerial and satellite imagery. Acting on such imagery (mapping flooded ground, crop extent, or damaged infrastructure) demands pixel-level segmentation to ensure perfect class localization. Pretrained general foundation models, when applied directly, often miss important features and cannot always find all the classes belonging to a given scene, overlooking smaller objects that matter most. We use a single consumer-grade GPU running a ...
  </details>

- **2026-09-01** — Daeheon Jeong, Yoonjoo Lee, Eugene Choi et al. — [Investigating Assistant Bias in LLM User Simulators Using a Role Vector](http://arxiv.org/abs/2609.00608v1)
  <details><summary>📄 Abstract</summary>
  LLM-based user simulators are increasingly used to evaluate autonomous agents at scale, in place of costly human evaluations. Despite this promise, these simulators exhibit "assistant bias," a tendency to cooperate and pursue task goals. They rarely reproduce the frustration or disengagement that real users exhibit, compromising evaluation validity. Prior work outlines that this bias is baked in during model training, which role-playing prompts fail to override. We analyze this bias from model a...
  </details>

- **2026-09-01** — Wenjian Wu, Zesheng Jia, Jiaying Tang et al. — [GeoPAR: Large-Scale Multi-Agent Combinatorial Optimization with Geometry-Guided Parallel Autoregressive Learning](http://arxiv.org/abs/2609.00577v1)
  <details><summary>📄 Abstract</summary>
  Multi-agent combinatorial optimization problems are notoriously challenging due to their NP-hard nature. Recent parallel autoregressive neural solvers improve inference efficiency by allowing agents to make decisions simultaneously, but their performance often degrades on large-scale instances. This is largely attributable to weak modeling of local geometric structures and the fact that conflicting task selections are handled only after action generation. To address these limitations, we propose...
  </details>

- **2026-09-01** — Zhenyu Zhao, Roy Zhao — [Runtime-Independent Persistent Agents: Preserving Identity, Memory, and Code Across Models, Harnesses, and Servers](http://arxiv.org/abs/2609.00546v1)
  <details><summary>📄 Abstract</summary>
  Agent systems are commonly described by the model and harness that currently produce their behavior. That boundary is useful for one execution but underspecifies a long-lived agent that may change models, orchestration harnesses, interaction sessions, and host servers while retaining one identity, memory, and executable code lineage. We present a runtime-independent architecture for persistent agents. A continuity-bearing substrate $P_t=(I_t,M_t,B_t)$ contains an architectural identity represent...
  </details>

- **2026-08-31** — Jinhao Hu, Ashvin Goel, Laurent Bindschaedler — [Don't Trust the Code, Check Its Effects: Runtime Refinement for Regenerated Systems Code Under an Adversarial Generator](http://arxiv.org/abs/2609.00430v1)
  <details><summary>📄 Abstract</summary>
  Recent work uses large language models to generate systems code from specifications, treating the specification as the durable artifact and the implementation as disposable. Regenerating the implementation specializes it to each workload and device. However, that work lives in a forgiving setting: a component's externally visible effects, its writes and device commands, are recoverable, and the generator is honest, so trust is discharged by re-execution. We target the unforgiving setting: system...
  </details>

- **2026-08-31** — Simone Gargiulo, Gabriel Kulp — [Workload Identification with Physical Side Channels for AI Governance](http://arxiv.org/abs/2609.00309v1)
  <details><summary>📄 Abstract</summary>
  AI compute verification is one of the first tangible and tractable points for international policy aimed at AI governance. Determining whether frontier labs, or any operator, comply with agreements requires the regulating authority to discern how their compute is used. The elementary building block of AI compute is the GPU, and any activity it executes leaves a physical trace. Here, we show that an external observer can identify the class of the workload running on an NVIDIA H200 from its power ...
  </details>

- **2026-08-31** — Bardia Mohammadi, Laurent Bindschaedler — [The Irreversibility Budget: Fleet-Level Risk Accounting and Admission Control for Agent Operating Systems](http://arxiv.org/abs/2609.00275v1)
  <details><summary>📄 Abstract</summary>
  Fleets of LLM agents now externalize effects that cannot be fully undone: they move money, deploy code, delete data, and disclose information. Current controls check one effect at a time, so a fleet of individually authorized agents can overdraw its principal's risk under a shared trigger while every local gate stays correct. We propose the irreversibility budget, a cumulative account of residual value-at-risk that a trusted runtime maintains for each principal across agents, workflows, and tena...
  </details>

- **2026-08-31** — Fizza Rubab, Yiying Tong, Arun Ross — [Unmasking Face Embeddings: Reading, Rendering and Naming with Foundation Models](http://arxiv.org/abs/2609.00411v1)
  <details><summary>📄 Abstract</summary>
  Modern face recognition (FR) owes much of its success to deep neural networks that learn to extract compact identity embeddings from face images. These models are typically trained for identity discrimination, producing embeddings that are highly effective for biometric matching but largely opaque to semantic interpretation. In contrast, foundation models, pretrained on broad visual or vision--language tasks, provide rich interfaces for describing, retrieving, generating, and organizing visual c...
  </details>

- **2026-08-31** — Salim Khazem, Ibrahim Mohamed Serouis — [Adapting Without Gradients: Affine Statistics Transport and What Its Certificate Can Tell You](http://arxiv.org/abs/2609.00374v1)
  <details><summary>📄 Abstract</summary>
  Test-time adaptation (TTA) typically assumes that model parameters can be updated at inference time. This assumption is restrictive for inference-only accelerators, frozen or third-party models, and memory-constrained deployments, and standard BatchNorm-based TTA configurations may also become inactive on architectures without BatchNorm. We study adaptation when the learned model must remain frozen. We introduce CASTER, a gradient-free method that stores source class statistics in a discriminati...
  </details>

- **2026-08-31** — Rohan Pandey, Sunjae Kwon, Hong Yu — [MUSES: A Benchmark for Prospective Intellectual-Roots Retrieval](http://arxiv.org/abs/2609.00313v1)
  <details><summary>📄 Abstract</summary>
  Scientific discovery depends on finding prior literature that shapes what comes next. Existing retrieval systems optimize for relevance and popularity, often favoring central papers over less familiar works that later prove generative. We introduce \textbf{MUSES}, a million-instance benchmark for prospective intellectual-roots retrieval over a fixed 2.33M-paper corpus, with roughly 140K test instances per familiarity tier. To our knowledge, it is the first prospective benchmark at this scale wit...
  </details>

- **2026-08-31** — Mohammad Saim, Tianyu Jiang — [Emotional Labor Strategy Preferences in LLM Personas](http://arxiv.org/abs/2609.00310v1)
  <details><summary>📄 Abstract</summary>
  Emotional labor is the effortful management of emotional displays to meet social or professional expectations. Personality traits have been correlated with emotional labor strategies, yet research on this link relies almost exclusively on self-report scales administered only in occupational settings. We investigate whether large language models injected with psychometrically grounded personas reproduce these personality-driven selection patterns across everyday social scenarios. We construct the...
  </details>

- **2026-08-31** — Bilge Kaan Karamete, Hunter Casten — [Hidden relationships in a document-derived property graph: top-k chunk embeddings and inverse-distance weighting over a dynamically evolving ontology](http://arxiv.org/abs/2609.00387v1)
  <details><summary>📄 Abstract</summary>
  Large language models extracting knowledge graphs from text capture only explicitly stated facts, often leaving semantically related entities disconnected across documents. We present an additive, engine-neutral second pass that discovers these latent ties without altering extracted facts. Each document is chunked and embedded once; top-k nearest- neighbor queries across existing chunks yield candidate node pairs via entity membership maps. Candidate pairs are scored using Shepard inverse-distan...
  </details>

- **2026-08-31** — Lukas Edman, Alexander Fraser — [Toppling the Hierarchy in Byte-level Language Modeling](http://arxiv.org/abs/2609.00463v1)
  <details><summary>📄 Abstract</summary>
  This work examines recent byte-level models and their failure to perfectly manipulate characters. State-of-the-art byte-level models use a hierarchical structure, starting at the byte level, downsampling to the word level, and then upsampling back to bytes. While this improves training and inference efficiency, we find that the hierarchical design itself limits character-level understanding, with pure byte-level models consistently outperforming hierarchical variants on character manipulation ta...
  </details>

- **2026-08-31** — Ryo Mitsuhashi, Sabri Boughorbel, Majd Hawasly — [Latent Mechanisms of Language Control in Multilingual Language Models](http://arxiv.org/abs/2609.00325v1)
  <details><summary>📄 Abstract</summary>
  Multilingual large language models can exhibit unintended code-switching -- unnecessarily alternating between languages during generation. We present a comparative study of three methods that identify language-controlling latents in cross-layer transcoders: activation value-based selection (ValSel), activation frequency-based selection (FreqSel), and LLM-generated latent annotation-based selection (AnnSel). To evaluate the efficacy of these methods in identifying language-controlling latents, we...
  </details>

- **2026-08-31** — Pruthvi Davineni — [Don't Let the Model Write the YAML: Deterministic, Minimal-Diff GitOps Remediation from LLM-Proposed Field Changes](http://arxiv.org/abs/2609.00227v1)
  <details><summary>📄 Abstract</summary>
  LLM agents increasingly diagnose incidents and propose remediations. In a GitOps workflow, applying a fix means editing a version-controlled config file, and the obvious implementation, having the model author the edited file or a diff, is what practitioners reach for first. Evaluating that choice on real Kubernetes manifests, we find no text-generation strategy is safe for unattended automation. Unified diffs are unsafe: under strict patching almost none apply, but that is an artifact, since a ...
  </details>

- **2026-08-31** — Rongze Tang, Jianjie Fang, Zhaolu Wang et al. — [IMPACT: Attention Is the Interaction Map for Scalable Interaction-Aware World Model Training](http://arxiv.org/abs/2609.00161v1)
  <details><summary>📄 Abstract</summary>
  World models have made remarkable progress in action-conditioned future prediction for embodied agents, yet still struggle to model physically plausible interactions. Existing approaches address this limitation by constraining the generation process with external representations encoding motion, geometry, or semantics. Obtaining these spatiotemporally dense representations typically requires auxiliary estimators or manual annotations, limiting training scalability. We instead revisit the trainin...
  </details>

- **2026-08-31** — Hangxiao Zhu, Suliu Qin, Zhuoyan Li et al. — [MemeBridge: A Dataset for Benchmarking and Mitigating the Bidirectional Cultural Gap in Meme Interpretation](http://arxiv.org/abs/2609.00491v1)
  <details><summary>📄 Abstract</summary>
  Communicating across cultures is inherently challenging, especially through culturally dense and ambiguous formats like memes. While people expect large language models (LLMs) to hold promise for bridging such gaps, existing benchmark datasets often fail to capture the cultural context necessary for accurate interpretation. To address this, we introduce MemeBridge, a curated dataset centered on U.S.-originated memes, designed to capture two complementary perspectives: (1) how Chinese participant...
  </details>

- **2026-08-31** — Shishi Xiao, Adam J. Coscia, David H. Laidlaw — [Less Is More: Balancing Positive and Negative Space in Visual Concept Blending](http://arxiv.org/abs/2609.00476v1)
  <details><summary>📄 Abstract</summary>
  Graphic designers often blend visual concepts to communicate multiple ideas within a single image, leveraging positive and negative space to create balance, emphasis, and aesthetic appeal. While computational methods have begun to support automatic concept blending, they largely overlook the role of spatial composition in the design. To address this gap, we present an automatic pipeline that explicitly applies positive and negative space throughout the blending process. Our approach first identi...
  </details>

- **2026-08-31** — Songwei Dong, Bingyan Lu, Makayla Kienlen et al. — [SpecMind: Enabling Spectrum Intelligence via Multi-Agent Hybrid Retrieval-Augmented Generation](http://arxiv.org/abs/2609.00427v1)
  <details><summary>📄 Abstract</summary>
  The exponential growth of wireless devices is driving unprecedented spectrum demand, pushing spectrum management toward more fine-grained decisions across space, time, and device constraints. As a result, spectrum policymakers and engineers must process large volumes of data that come from diverse sources and take many different forms, such as text and tables. These data sources are often disaggregated and require significant time and effort to integrate, search, and interpret. Furthermore, most...
  </details>

- **2026-08-31** — Arnol Manuel Fokam, Fasseu Sieyondji Akpevwoghene, Edem Fiifi Dawson — [How Temporal Correlations Shape Memory in Linear Recurrent Neural Networks](http://arxiv.org/abs/2609.00420v1)
  <details><summary>📄 Abstract</summary>
  The linear recurrent neural network (LRNN) is a simple model for studying how much memory a network builds up as it trains. For uncorrelated inputs, earlier work found that training itself settles the network between keeping the past and reacting only to the present. Real sequences are correlated, and we solve the learning dynamics exactly for correlated inputs. In the solution, keeping the past carries a cost. The whole effect of correlation lands on that cost. This cost reduces to the earlier ...
  </details>

- **2026-08-31** — Riccardo Mansutti, Andrea Pomarico, Robert Jakob et al. — [RestoreBench: Can AI Agents Restore Power Flow Convergence?](http://arxiv.org/abs/2609.00384v1)
  <details><summary>📄 Abstract</summary>
  Large Language Model (LLM) agents increasingly automate multi-step engineering workflows through tool use, interpretation of intermediate results, and iterative planning. Diagnosing and resolving non-convergent power flow cases is a promising yet largely unexplored application, as it requires engineering judgment, experimentation, and decision-making within constrained action spaces. We introduce a benchmark that evaluates these capabilities across multiple LLMs and three architectures: \emph{ch...
  </details>

- **2026-08-31** — Louis Lalonde, Wassim Keddache, Thomas Perron Touchette et al. — [Revisiting Feedback-Driven LLM Code Repair: A Replication and Exploratory Java Extension](http://arxiv.org/abs/2609.00362v1)
  <details><summary>📄 Abstract</summary>
  Since the advent of Large Language Models (LLMs), practitioners have increasingly leveraged them to support their software engineering tasks, including automated code repair, showing promising results. Yet, concerns regarding reproducibility and generalizability remain largely unexplored. To further evaluate these concerns and associated impacts, we partially reproduce and conduct an exploratory Java extension of the FeedbackEval benchmark [1], which evaluates how LLMs leverage different feedbac...
  </details>

- **2026-08-31** — Uthman Jinadu, Parsa Ghazvinian, Anjila Budathoki et al. — [Authority Bias in Conversational Search Engines for Academic Paper Recommendation](http://arxiv.org/abs/2609.00248v1)
  <details><summary>📄 Abstract</summary>
  Large Language Models (LLMs) are increasingly used as conversational search engines for academic literature, yet whether they judge papers on content or on authority signals has not been tested causally. We investigate authority bias: systematic preference for papers based on author prestige, venue, and citations rather than content. Holding title and abstract constant, we vary authority metadata across three counterfactual conditions (original, flipped, boosted) over eight LLMs (five open-weigh...
  </details>

- **2026-08-31** — Yasaman Torabi, Shahram Shirani, James P. Reilly — [XVAE-WMT: Explainable Wavelet-Temporal Variational Autoencoder for Blind Source Separation of Heart and Lung Sounds](http://arxiv.org/abs/2609.00238v1)
  <details><summary>📄 Abstract</summary>
  The separation of cardiovascular sounds is a critical task in biomedical signal processing. In this paper, we introduce XVAE-WMT1, an unsupervised explainable generative AI algorithm combining a variational autoencoder (VAE) with explainable AI (XAI), wavelet-based inputs, a post-hoc output mask, and temporal consistency (TC) loss. Unlike existing supervised and VAE-based methods that rely on Short-Time Fourier Transform (STFT) and ignore latent interpretability, XVAE-WMT requires no paired clea...
  </details>

- **2026-08-31** — Muzhao Tian, Zezi Zeng, Yifan Yang et al. — [ReDeck: Step-Level Render-Grounded Refinement for Document-to-Slide Generation](http://arxiv.org/abs/2609.00194v1)
  <details><summary>📄 Abstract</summary>
  Document-to-slide generation is challenging because slides are dense editable artifacts that require both faithful content selection and precise spatial layout. Recent slide agents adopt iterative reflection, but typically follow a monolithic "one version, one feedback" loop: a slide or deck is rewritten, rendered afterward, and critiqued only at the turn boundary. This delayed feedback makes local failures such as overflow, overlap, clipping, and off-canvas placement difficult to attribute and ...
  </details>

- **2026-08-31** — Irem Yoldas, Martim Brandão, Jie Zhang et al. — [LLM-Driven Autonomous Vehicles Inherit Human Driver Biases in Pedestrian Yielding: Results and Implications From A New Benchmark](http://arxiv.org/abs/2609.00192v1)
  <details><summary>📄 Abstract</summary>
  Public trust in Autonomous Vehicles (AVs) may depend not only on technical success but also on the fairness of their decision making. While a recent trend in AV research involves using general purpose "common sense" models to guide AV decision making, the degree to which these inherit human biases in driving is still understudied. Given that psychology studies have shown human driver biases exist, such as lower pedestrian-yielding rates to Black pedestrians in the US, we argue that analyses of m...
  </details>

- **2026-08-31** — Deniz Bayazit, Badr AlKhamissi, Antoine Bosselut — [Lingua Franca or Probing Artifact? Rethinking Latent Language in Multilingual LLMs](http://arxiv.org/abs/2609.00155v1)
  <details><summary>📄 Abstract</summary>
  Latent language identification is often used to argue that multilingual language models route computation through language-specific states, such as English pivots. However, existing probes infer latent language from different signals, such as the geometry of hidden states or what can be decoded from intermediate representations. Since such claims shape conclusions about how models share and route information across languages, we ask whether these probes measure the same phenomenon or expose dist...
  </details>

- **2026-08-31** — Ashwin Nedungadi, Stefan Oehmcke, Stefan Lüdtke — [Autoregressive Mosaics: Probing 2D Spatial Reasoning in Text-Only Language Models](http://arxiv.org/abs/2608.30751v2)
  <details><summary>📄 Abstract</summary>
  Large language models (LLMs) trained only on text and code can sometimes generate programs that draw recognizable images. However, it is unclear whether this reflects an internal representation of 2D spatial layout or simply the ability to translate spatial descriptions into code. We introduce Autoregressive Mosaics (AM-Bench), a benchmark that separates these factors: First, a translation task gives a model a fully specified geometry of a picture in words as a prompt and asks for the code that ...
  </details>

- **2026-08-31** — Joonki Min, Chaeyun Kim, Hyungwook Choi et al. — [Fine-Grained Multi Image Object Hallucination Benchmark](http://arxiv.org/abs/2608.30653v1)
  <details><summary>📄 Abstract</summary>
  Multimodal Large Language Models (MLLMs) are increasingly deployed in multi-image scenarios requiring complex reasoning across visual contexts. However, current MLLMs remain fundamentally limited by object hallucination-generating plausible yet factually inconsistent descriptions about objects. Existing benchmarks, designed primarily for single-image settings or providing only high-level multi-image assessments, cannot systematically diagnose how visual complexity and reasoning demands trigger h...
  </details>

- **2026-08-31** — Hui Gong, Michail Samawi, Francesca Medda — [Authority-Inference Separation in Agentic Finance: First-Line Control, Blockchain Enforcement, and Replayable Assurance](http://arxiv.org/abs/2608.30519v1)
  <details><summary>📄 Abstract</summary>
  AI agents can select tools, counterparties, and transaction parameters, yet inference should not itself confer authority to execute a financial action. This study develops and evaluates Authority-Inference Separation (AIS), an intent-centered architecture for bounded agentic finance. AIS treats a financial action intent as the control object: a machine-generated proposal can receive temporary executable authority only after an independent deterministic control plane validates registered agent id...
  </details>

- **2026-08-31** — Hanieh Taraghi Nazloo, Petr Musilek — [A High-Resolution Synthetic EV Charging Dataset for Cold-Climate Distribution Grid Impact Analysis: Trondheim, Norway (2020-2030)](http://arxiv.org/abs/2608.30199v1)
  <details><summary>📄 Abstract</summary>
  This data article presents a high-resolution, long-term synthetic electric-vehicle (EV) charging dataset for Trondheim, Norway, spanning February 2020 to December 2030. Empirically grounded in 14 months of historical charging logs from December 2018 to January 2020, the dataset captures session-level behavioral patterns, including delivered energy, plug-in duration, connection schedules, user categorization (private vs. shared), seasonal variations, public-holiday effects, and daily ambient temp...
  </details>

- **2026-08-31** — Adrians Skapars, Edoardo Manino — [BLOOM-WILT: Logit Tilting for Behaviour Elicitation in Automated LLM Auditing](http://arxiv.org/abs/2608.31105v1)
  <details><summary>📄 Abstract</summary>
  Users of a deployed language model routinely encounter behaviours that testing almost never surfaces, since deployment puts the model through orders of magnitude more interactions than any evaluation can simulate. Automated auditors make testing cheap to scale and flexible enough to cover almost any specified behaviour, yet their lack of optimisation pressure makes them sample-inefficient. To address this shortcoming, we introduce BLOOM-WILT, a full auditing pipeline that elicits natural multi-t...
  </details>

- **2026-08-31** — Jailing Lin, Jikuan Zhang, Jianhua Sun — [Analytic Dynamics: Learning Physics-Grounded Representation for Fast Intrinsic Dynamics Inference from Monocular Videos](http://arxiv.org/abs/2608.31025v1)
  <details><summary>📄 Abstract</summary>
  Inferring object dynamics from visual observations is essential for intelligent agents to reason about and interact with the physical world, yet remains challenging due to the fundamental gap between visual evidence and intrinsic dynamics. Existing methods either rely on costly per-scene optimization, limiting efficiency and scalability, or directly map visual evidence to intrinsic dynamics without intermediate physical abstractions, making them prone to appearance and geometry shortcuts. To bri...
  </details>

- **2026-08-31** — Vernon Toh, Navonil Majumder, Zhengyuan Liu et al. — [MNIST-PRO: MNIST is Back as a Partially Observable World for AI Agents](http://arxiv.org/abs/2608.31022v1)
  <details><summary>📄 Abstract</summary>
  AI agents in partially observable environments need to coordinate active sensing with working memory to maintain an evolving perceptual state. However, existing benchmarks struggle to isolate this perceptual-state construction and interpretation capability because they introduce physical and control complexities. We address this with MNIST-PRO, a benchmark that isolates agentic perception by converting MNIST digit recognition into a sequential, glimpse-based search task with lookback constraints...
  </details>

- **2026-08-31** — Qi Peng, Yi Cai, Jialin Cui et al. — [Evidence, Logic, and Compliance: Multi-Agent Structured Graph Reasoning with Expert Arbitration for Medical Referral](http://arxiv.org/abs/2608.30938v1)
  <details><summary>📄 Abstract</summary>
  Medical referral (directing patients to the appropriate hospital department) is a complex decision-making process requiring the synthesis of multimodal data, including patient narratives, laboratory indicators, and radiology imaging. While Large Language Models (LLMs) have advanced medical dialogue systems, they struggle with real-world referral tasks due to two primary limitations: (1) Information Overload, where models fixate on high-frequency disease terms while overlooking subtle but critica...
  </details>

- **2026-08-31** — Shaoan Wang, Aocheng Luo, Fei Huang et al. — [LightNav-0: Eliciting VLM Spatial Intelligence for Generalist Embodied Navigation](http://arxiv.org/abs/2608.30935v1)
  <details><summary>📄 Abstract</summary>
  Embodied navigation requires agents to translate heterogeneous goals and visual observations into actions across tasks, environments, and robot embodiments. Modern vision-language models (VLMs) already encode spatial priors for visual grounding, spatial reasoning, and pointing, but these capabilities are rarely elicited directly for robot control. Existing navigation systems instead rely on task- or embodiment-specific components, fragmenting perception, reasoning, and action while offering limi...
  </details>

- **2026-08-31** — Wail Bouhedja, Amr Mohamed, Guokan Shang — [CARVE: Verified Expansion for Variable-Length Generation in Diffusion Language Models](http://arxiv.org/abs/2608.30922v1)
  <details><summary>📄 Abstract</summary>
  Masked diffusion language models predict tokens from a partially observed response canvas, enabling bidirectional conditioning and parallel token refinement. Yet standard masked-diffusion decoders use a rigid inference interface: the number of masked positions allocated to the answer is fixed before generation begins. Choosing this length is difficult. A short canvas can truncate reasoning or code, while a long canvas wastes computation and can perturb denoising. We introduce CARVE (Counterfactu...
  </details>

- **2026-08-31** — Enzo Brasil, Cira E. G. Otiniano, Carolyne Brito et al. — [Extremes of solar spectral irradiance in the SORCE/XPS record](http://arxiv.org/abs/2608.30878v1)
  <details><summary>📄 Abstract</summary>
  Extreme and rare changes in space mission solar irradiance records are scientifically relevant but difficult to quantify because these records are finite, instrument dependent, and affected by observational gaps and time varying measurement quality. We evaluated extreme daily logarithmic changes in the band integrated 0.1-7.0 nm irradiance measured by photodiode 7 of the Solar Radiation and Climate Experiment/X-Ray Photometer System (SORCE/XPS) from 2005 to 2019. After constructing a regular dai...
  </details>

- **2026-08-31** — Max Studt, Georg Schildbach — [Provably Safe Decentralized Contingency MPC under State-Only Information and Limited Sensing for Nonlinear Multi-agent Systems](http://arxiv.org/abs/2608.30874v1)
  <details><summary>📄 Abstract</summary>
  This paper considers decentralized contingency MPC for multi-agent control under a state-only information pattern, with particular focus on limited sensing and plug-and-play operation. The objective is to retain recursive feasibility, safety, and Lyapunov-type convergence while reducing conservatism in local interaction handling. The framework relies on agent-wise fallback regions (safe sets) in which a feasible contingency maneuver to a safe equilibrium is always available. A novel safe-set upd...
  </details>


## 📊 统计 / Statistics

| 分类 / Category | 论文数 / Count |
|------|--------|
| jailbreak | 612 |
| prompt-injection | 523 |
| memory-poisoning | 47 |
| tool-use-attack | 132 |
| backdoor | 442 |
| adversarial-attack | 580 |
| privacy-leakage | 3994 |
| steganography | 61 |
| misuse | 972 |
| red-teaming | 120 |
| vulnerability | 2954 |
| defense | 2719 |
| alignment | 2536 |
| robustness | 2604 |
| watermark | 382 |
| unlearning | 94 |
| agent-safety | 52 |
| benchmark | 65 |
| survey | 319 |
| other | 7168 |

---

📚 **全部 26376 篇论文**（2022 至今）请访问 [GitHub Pages](https://ny1024.github.io/AgentSafety-Papers/) 查看完整列表、搜索与筛选。

*Generated by AgentGuard at 2026-09-03 10:34:01*