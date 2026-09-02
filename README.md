<div align="center">

# AgentGuard 🛡️

**Daily Tracking of LLM Agent Security Papers on arXiv**

[![Auto Update](https://github.com/NY1024/AgentSafety-Papers/actions/workflows/daily-update.yml/badge.svg)](https://github.com/NY1024/AgentSafety-Papers/actions/workflows/daily-update.yml)
[![Papers](https://img.shields.io/badge/Papers-26200-blue)](#)
[![License](https://img.shields.io/badge/License-MIT-green)](#)

</div>

---

## 📖 简介 / Introduction

自动追踪 arXiv 上大模型 Agent 安全方向的最新论文，每日更新，关键词智能分类。

*Automatically tracking the latest LLM Agent security papers on arXiv, updated daily with keyword-based classification.*

**最近更新 / Last Updated**: 2026-09-02 15:49 ｜ **论文总数 / Total Papers**: 26200（近 30 天 / Recent 30 days: 4336）

🌐 **[GitHub Pages](https://ny1024.github.io/AgentSafety-Papers/)** — 查看全部 26200 篇论文（含摘要、分类筛选、搜索）/ View all 26200 papers with abstracts, filters & search

## 📑 分类导航 / Category Navigation

- **[jailbreak](#-jailbreak)** — 越狱攻击 / Jailbreak Attacks — 609
- **[prompt-injection](#-prompt-injection)** — 提示注入攻击 / Prompt Injection Attacks — 519
- **[memory-poisoning](#-memory-poisoning)** — 记忆投毒与篡改 / Memory Poisoning & Tampering — 46
- **[tool-use-attack](#-tool-use-attack)** — 工具使用攻击 / Tool-Use Attacks — 131
- **[backdoor](#-backdoor)** — 后门与投毒攻击 / Backdoor & Poisoning Attacks — 440
- **[adversarial-attack](#-adversarial-attack)** — 对抗攻击 / Adversarial Attacks — 578
- **[privacy-leakage](#-privacy-leakage)** — 隐私泄露 / Privacy Leakage — 3984
- **[steganography](#-steganography)** — 隐写与隐蔽通信 / Steganography & Covert Communication — 61
- **[misuse](#-misuse)** — 滥用与误用 / Misuse & Abuse — 966
- **[red-teaming](#-red-teaming)** — 红队测试 / Red Teaming — 120
- **[vulnerability](#-vulnerability)** — 漏洞与攻击面 / Vulnerabilities & Attack Surfaces — 2935
- **[defense](#-defense)** — 防御与防护方法 / Defense & Protection Methods — 2698
- **[alignment](#-alignment)** — 对齐与安全约束 / Alignment & Safety Constraints — 2508
- **[robustness](#-robustness)** — 鲁棒性与可靠性 / Robustness & Reliability — 2586
- **[watermark](#-watermark)** — 水印与溯源 / Watermarking & Provenance — 377
- **[unlearning](#-unlearning)** — 机器遗忘 / Machine Unlearning — 93
- **[agent-safety](#-agent-safety)** — Agent 安全框架 / Agent Safety Frameworks — 52
- **[benchmark](#-benchmark)** — 安全评测与基准 / Safety Benchmarks & Evaluation — 65
- **[survey](#-survey)** — 综述与系统化 / Surveys & Systematization — 315
- **[other](#-other)** — 其他安全相关 / Other Security-Related — 7117

## 📄 近期论文 / Recent Papers (Last 30 Days)

> 仅展示最近 30 天中最新的 500 篇论文（含日期、作者、摘要）。近 30 天共 4336 篇，完整 26200 篇论文列表请访问 [GitHub Pages](https://ny1024.github.io/AgentSafety-Papers/)

> Showing the latest 500 of 4336 papers from the last 30 days (with date, authors & abstract). For the full list of 26200 papers, visit [GitHub Pages](https://ny1024.github.io/AgentSafety-Papers/)

### 📂 jailbreak
*越狱攻击 / Jailbreak Attacks* — 6 papers

- **2026-09-01** — Kaiyan Wen, Shijie Zhang, Lu Yu et al. — [Jailbreaking Text-to-Image Models Through Cracks: Navigating Heterogeneous Safety Filters via Multi-Agent Debate](http://arxiv.org/abs/2609.01168v1)
  <details><summary>📄 Abstract</summary>
  Text-to-image (T2I) models remain vulnerable to jailbreak attacks that elicit Not-Safe-For-Work (NSFW) content, despite increasingly being guarded by heterogeneous, multi-layer safety stacks combining text filters, image classifiers, and cross-modal detectors. Existing jailbreak studies either optimize against individual filters or query the complete pipeline with aggregate feedback, making it difficult to identify the active constraint and adapt to conflicts across safety layers.In this paper, ...
  </details>

- **2026-09-01** — Nikita Oblakov, Sabrina Sadiekh, Evgeniy Kokuykin — [HiveTraceGuard-Pro: A Compact Generative Guardrail for Prompt Injection, Jailbreaks, and Adversarial Obfuscation](http://arxiv.org/abs/2609.01046v1)
  <details><summary>📄 Abstract</summary>
  Production LLMs must handle inputs that attempt to override system instructions, bypass safety policies or elicit harmful responses. A common mitigation is a separate guardrail model. Existing reports, however, provide little evidence on Russian prompt injection or Russian surface obfuscation. We present HiveTraceGuard-Pro, a 0.6B generative guardrail LoRA-tuned from Qwen3-0.6B. It is trained on Russian and English and uses one binary scoring rule (safe/unsafe) for the final target turn. Its tra...
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
*提示注入攻击 / Prompt Injection Attacks* — 8 papers

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

- **2026-08-30** — Ashok Subbabhatta Gopalakrishna — [Zero-Knowledge Predicate Proofs Between AI Agents: A Measured, Cross-Protocol Gateway and the Source-Integrity Gap](http://arxiv.org/abs/2608.30083v1)
  <details><summary>📄 Abstract</summary>
  Multi-agent AI platforms move quickly from staging to production, but the way agents establish trust remains rudimentary: an agent either transmits raw data to a peer or accepts that peer's natural-language self-report that a value complies with policy. The first over-shares; the second is unverifiable and is exactly the channel prompt injection attacks. Prevailing responses emphasise identity, visibility, and post-hoc detection, and recent proposals for cryptographically enforced agent policy h...
  </details>

- **2026-08-30** — Wujie Xiong, Rabimba Karanjai, Yang Lu et al. — [Reachability-Based Capability Confinement for LLM Agents under Indirect Prompt Injection](http://arxiv.org/abs/2608.30041v1)
  <details><summary>📄 Abstract</summary>
  Large language model agents place outputs from external skills into their execution context, allowing attacker-controlled data to influence later privileged actions. Existing defenses mainly classify untrusted content or authorize proposed operations. They do not directly address how an agent's future authority should change once untrusted data enters its state. We present SkillGuard, a harness-level enforcement layer that treats this event as contamination and restricts future capabilities to d...
  </details>


### 📂 memory-poisoning
*记忆投毒与篡改 / Memory Poisoning & Tampering* — 2 papers

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

- **2026-09-01** — Jinqing Zhao, Chengcan Wu — [Making Prospective Memory SLM-Shaped: Typed Intention Stores for Small-Model Agents](http://arxiv.org/abs/2609.01272v1)
  <details><summary>📄 Abstract</summary>
  Prospective memory means carrying out a deferred intention at the right future cue while other work continues. Benchmarks now isolate it as an agent skill, yet frontier LLMs still struggle: the best published PM-Bench scaffold reaches only 65.1% Set-F1. We argue that this loop is schema-constrained state tracking rather than open-ended reasoning, and that small models can execute it when the action space is typed. We propose the Prospective Intention Store (PIS) that puts lifecycle logic in code...
  </details>

- **2026-08-31** — Xiaofan Bai, Chao Liu, Hongqiang Lin et al. — [SkillZip Pro: Execution-Aware Dynamic Compression of Progressively Loaded Skills for Self-Evolving Agents](http://arxiv.org/abs/2608.30785v1)
  <details><summary>📄 Abstract</summary>
  Production agent skills are directory bundles, not isolated prompts. The root is loaded at activation; references, schemas, scripts, assets, and nested subskills are loaded only when an execution path needs them. Compressing only the root misses most deployment cost and may move branch-specific details into the always-loaded context. Flattening instead destroys progressive-loading boundaries.   We introduce \method, an evaluation-free compressor for complete, progressively loaded skill bundles. ...
  </details>


### 📂 backdoor
*后门与投毒攻击 / Backdoor & Poisoning Attacks* — 5 papers

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
*对抗攻击 / Adversarial Attacks* — 6 papers

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

- **2026-08-30** — Bhaskar Ganesh Devalla, Junchao Wu, Nilesh Dokuparthi et al. — [IndicDetect: Evaluating Cross-Lingual LLM-Generated Text Detection for Hindi, Telugu, and Tamil](http://arxiv.org/abs/2608.29919v1)
  <details><summary>📄 Abstract</summary>
  The rapid proliferation of LLMs has further heightened the need to develop dependable AI-generated text detection, especially beyond English. Nevertheless, current benchmarks pay little attention to Indic languages and test detectors in idealized settings that do not represent the real world. We present a generalized benchmark for AI-generated text detection in Hindi, Telugu, and Tamil, which we call IndicDetect, designed to assess the robustness of detectors under realistic distribution shifts....
  </details>


### 📂 privacy-leakage
*隐私泄露 / Privacy Leakage* — 31 papers

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

- **2026-08-31** — Dan Schumacher, Pragathi Durga Rajarajan, Haven Kotara et al. — [Detecting AI Impostors: How Do Middle Schoolers Identify LLM Agents in a Live Collaborative Setting?](http://arxiv.org/abs/2608.30948v1)
  <details><summary>📄 Abstract</summary>
  LLMs can imitate how people write, which raises concerns about impersonation, trust, and detection in social settings. These concerns are especially important for adolescents, who use generative AI frequently but may struggle to recognize it. We introduce \textit{DoppelBot}, a cooperative social deduction game designed to study how young people detect and respond to AI impersonation. Through studies with middle schoolers, we investigate whether a DoppelBot prompts reflection on privacy and imper...
  </details>

- **2026-08-31** — Kangwook Ko, Jaehyuk Jang, Wonjun Lee et al. — [Where Identity Lives: Localized, Retain-Free Identity Unlearning in Multimodal Large Language Models](http://arxiv.org/abs/2608.30649v1)
  <details><summary>📄 Abstract</summary>
  Removing a specific individual's information from multimodal large language models (MLLMs) is often needed after deployment, but existing methods rely on a retain set, which is hardest to obtain at that point, and rebuilding it recreates the privacy exposure that unlearning aims to remove. Forgetting from the forget set alone instead damages the shared visual-language computation, harming perception. We cast retain-free unlearning as a localization problem: causal tracing, weight transplant, and...
  </details>

- **2026-08-31** — Haoran Que, Jiajun Shi, Ting Huang et al. — [REER-PT: Reverse-Engineered Reasoning for Perplexity-Guided Pre-training Data Augmentation](http://arxiv.org/abs/2608.30627v1)
  <details><summary>📄 Abstract</summary>
  As language-model compute continues to scale, high-quality training data is becoming an increasingly important bottleneck. Conventional next-token prediction supervises what follows a context but leaves the intermediate reasoning behind that continuation implicit. We introduce \textbf{REER-PT}, a scalable framework that extends Reverse-Engineered Reasoning (REER) to raw pre-training data. REER-PT identifies continuations that are difficult to predict but can still be inferred from the preceding ...
  </details>

- **2026-08-31** — Nadia Jul Jeldtoft, Tariq Yousef — [Designing an Auditable LLM-Supported Workflow for Qualitative Thematic Analysis](http://arxiv.org/abs/2608.30543v1)
  <details><summary>📄 Abstract</summary>
  Large Language Models (LLMs) offer new possibilities for scaling qualitative analysis, but existing applications often provide limited methodological transparency regarding how qualitative methods are translated into computational procedures. This paper presents an auditable and privacy-preserving computational operationalization of inductive and latent Thematic Analysis (TA). This paper first derives five design principles from the methodological requirements of TA and the conditions introduced...
  </details>

- **2026-08-31** — Mathias Zinnen, Alisha Mund, Sabine Lang et al. — [Lot Machine: Multimodal Lot Extraction from Auction Catalogs](http://arxiv.org/abs/2608.30510v1)
  <details><summary>📄 Abstract</summary>
  For provenance research and art market studies, auction catalogs are an essential resource to trace specific objects over time and space. While historical auction catalogs follow established domain conventions, their internal formatting remains highly variable, and their large-scale analysis is currently restricted by the lack of machine-readable representations of the auction lots. We propose a pipeline to automatically extract structured lot-level metadata from German Sales, a large database o...
  </details>

- **2026-08-31** — Luigi Simeone — [Self-Supervised Pretext Tasks for Infant Cry Analysis: A Controlled Comparison and a Cautionary Result on Donateacry](http://arxiv.org/abs/2608.30456v1)
  <details><summary>📄 Abstract</summary>
  We compare six self-supervised pretext tasks for infant cry analysis under a fixed budget, meaning the same compact encoder of 1.17M parameters, the same 115 hours of license-verified public pretraining audio, and the same evaluation protocol for every candidate. On cry detection the reconstructive objectives dominate, and a linear probe over a masked-spectrogram encoder reaches 0.988 AUC with subject-wise splits even though the encoder never observed a cry during pretraining. On cry-reason clas...
  </details>


### 📂 steganography
*隐写与隐蔽通信 / Steganography & Covert Communication* — 2 papers

- **2026-08-31** — Minkyung Cho, Jihyo Kim, SeungWoo Song et al. — [Hidden Threat in Synthetic Data: Covert Targeted Bias Injection through Benign Text](http://arxiv.org/abs/2608.30619v1)
  <details><summary>📄 Abstract</summary>
  Synthetic data is increasingly used to train large language models (LLMs), yet its security implications remain poorly understood. Prior work on subliminal learning suggests that models can inherit behavioral traits from seemingly unrelated training data. In this work, we investigate whether such mechanisms can be exploited to inject targeted social biases into aligned models through semantically benign synthetic data. We construct a pipeline in which a misaligned teacher model generates filtere...
  </details>

- **2026-08-31** — Rastislav Lenhardt, Teodora Dobos, Thomas Vecchiato et al. — [RSLM: Training-Free Vector Quantization for Approximate Nearest Neighbor Search](http://arxiv.org/abs/2608.30384v1)
  <details><summary>📄 Abstract</summary>
  By introducing RSLM (Rotated Scaled Lloyd-Max), a family of training-free vector quantization codecs compressing embeddings to 1--4 bits per dimension, we reduce memory cost and memory bandwidth of a typical large-scale Approximate Nearest Neighbor (ANN) search system, while reducing its complexity and keeping or improving recall across multiple benchmark datasets. State-of-the-art systems filter candidates using coarse partitions, approximately score them to narrow the set, and then rescore the...
  </details>


### 📂 misuse
*滥用与误用 / Misuse & Abuse* — 18 papers

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

- **2026-08-31** — Annemarie Wittig, Alina Mailach, Janet Siegmund et al. — [On the Prospects of Dynamic LLM Conversations in Software Development](http://arxiv.org/abs/2608.30756v1)
  <details><summary>📄 Abstract</summary>
  Large language models (LLMs) have become an essential tool for assisting developers, yet we still lack knowledge on ways to effectively support their interactions during development activities. That is, the quality of interactions with a chat-based LLM still strongly depends on how developers phrase prompts and which information they include.   Our goal is to evaluate whether interventions into these interactions with LLMs have an effect on software developers---be it harmful or beneficial. To t...
  </details>

- **2026-08-31** — Xiaoyu Guo, Pengcheng Chen, Jiong Yu et al. — [Graph Evidence Is Not Enough: Diagnosing Native Decoder Use in Graph-Augmented LLMs](http://arxiv.org/abs/2608.30437v1)
  <details><summary>📄 Abstract</summary>
  Graph-augmented large language models often assume that graph evidence produced by external computation and placed in the input can be used by the native decoder. We test this assumption with HopQA, a deliberately bounded diagnostic that asks for the shortest-hop distance between two query nodes. Because the answer is a small integer and the target is purely topological, failure cannot be dismissed as open-ended generation or ambiguous evaluation. Yet existing graph-augmented baselines still fai...
  </details>

- **2026-08-31** — Hoejoon Kwon, Byeonggeuk Lim, Kahyeon Kim et al. — [ALTSTEER: Selective Safety Steering for Moving Beyond Hard Refusals to Constructive Alternatives](http://arxiv.org/abs/2608.30197v1)
  <details><summary>📄 Abstract</summary>
  Safety alignment is essential for deploying large language models, requiring systems to prevent harmful compliance while preserving helpfulness on benign requests. Activation steering offers a training-free inference-time approach to safety control, but effective safety steering requires addressing two coupled questions: when to intervene and how generation should be shaped after intervention. However, existing safety steering methods remain limited along both dimensions, as their triggering mec...
  </details>

- **2026-08-31** — Wei Fan, Xinjie Shen, Xudong Guo et al. — [E-Commerce Bench: Evaluating LLM Agents on Long-Horizon Autonomous Business Operation](http://arxiv.org/abs/2608.30730v1)
  <details><summary>📄 Abstract</summary>
  Long-horizon agentic tasks go beyond chaining short tasks over more interaction turns. Their evolving dynamic environments and long-range dependencies require Large Language Models (LLMs) to continually explore, learn from experience, and adapt their policies over thousands of steps. We introduce E-Commerce Bench, the first open-source benchmark that integrates multi-round counterpart negotiation and dynamic events into a year-long business operation. Over a 365-day year, an LLM agent concurrent...
  </details>

- **2026-08-30** — Apoorva Upadhyaya, Sandipan Sikdar — [When Safety Speaks a Language: A Mechanistic Analysis of Safety-Language Identity Entanglement in LLMs](http://arxiv.org/abs/2608.29936v1)
  <details><summary>📄 Abstract</summary>
  Safety alignment of large language models (LLMs) degrades across languages, yet the internal mechanism driving this asymmetry remains poorly understood. Our work, therefore, presents a systematic mechanistic analysis of multilingual safety using sparse autoencoder (SAE) features, sparse interpretable directions in the residual stream associated with harmful and harmless model behavior across three instruction-tuned LLMs, eight languages, and all model layers. We observe that safety-relevant feat...
  </details>


### 📂 vulnerability
*漏洞与攻击面 / Vulnerabilities & Attack Surfaces* — 55 papers

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

- **2026-08-31** — Matvei Tarasov, Salman Ahmadi-Asl, Andre L. F. de Almeida et al. — [Tensor Methods for Language Models: From Token Representation to Training, Adaptation, Inference, Compression, and Interpretability](http://arxiv.org/abs/2608.30505v1)
  <details><summary>📄 Abstract</summary>
  Large language models (LLMs) are built from structured high-dimensional objects such as token representations, weights, adaptation updates, caches, and activations, whose multilinear structure is underexploited by the conventional matrix-centric view. Tensor decompositions and tensor networks provide a principled algebraic language for this structure, yet the literature often treats them as isolated compression mechanisms. This survey organizes tensor methods for LLMs through two complementary v...
  </details>

- **2026-08-30** — Qi Fan, An Zou, Yehan Ma — [CUDA-Harness: Harnessing Agentic CUDA Kernel Generation and Optimization from Natural Language](http://arxiv.org/abs/2609.00058v1)
  <details><summary>📄 Abstract</summary>
  Developing high-performance CUDA kernels demands specialized knowledge in algorithm implementation, correctness validation, and hardware-aware parallel optimization, creating a substantial expertise barrier and making generating CUDA kernels directly from natural language (Text2CUDA) essential. Meanwhile, the general-purpose code generation capability of Large Language Models (LLMs) prompts a series of works exploring LLM-based CUDA kernel generation. They mainly focus on transpilation from high...
  </details>

- **2026-08-30** — Taejong Joo, Diego Klabjan — [Mitigating Over-Optimization in PRM-Guided Search in Mathematical Reasoning by Optimizing the Guide](http://arxiv.org/abs/2608.30051v1)
  <details><summary>📄 Abstract</summary>
  Process reward models (PRMs) provide dense step-level guidance for search-based reasoning, enabling inference-time compute to be allocated toward promising partial solutions. However, recent evidence suggests that PRM-guided search can over-optimize imperfect process rewards, pruning viable trajectories while expanding spurious ones. In this work, we theoretically show that directly leveraging PRM score is vulnerable to verifier noise through an extreme-value effect: non-viable prefixes become m...
  </details>

- **2026-08-30** — Shitanshu Bhushan, Yunxiang Zhang, Lu Wang — [Can LLM Agents Discover? Evaluating Creativity on ML Engineering Tasks](http://arxiv.org/abs/2608.30047v1)
  <details><summary>📄 Abstract</summary>
  Recent AI systems promise autonomous scientific discovery, claiming to discover algorithms and produce research papers, yet understanding whether they exhibit creativity, the capacity to produce solutions that are both novel and useful, remains an open question. We present a framework for evaluating multi-turn LLM research agents' creativity using ML engineering tasks as a testbed, through three dimensions: P-Creativity (psychological novelty: novel relative to the agent's own prior solutions wi...
  </details>

- **2026-08-30** — Hao Yan, Ziyu Yao — [Interpreting and Steering for Safe and Correct Code Generation](http://arxiv.org/abs/2608.30025v1)
  <details><summary>📄 Abstract</summary>
  Large language models (LLMs) frequently generate source code containing vulnerabilities, yet little work studies the internal mechanisms that distinguish safe from vulnerable generation in them. In this work, we systematically perform a mechanistic interpretation of LLMs, aiming at both understanding how code safety-vs-vulnerability is represented or driven by components in an LM and turning the insights into actionable steering strategies to encourage safer code generation. To this end, we intr...
  </details>

- **2026-08-30** — Aditi Sarker, Nazreen Shah, Rafi Ibn Sultan et al. — [Partition-Aware Unlearning for Removing Spurious Correlations in Large Vision-Language Models](http://arxiv.org/abs/2608.29996v1)
  <details><summary>📄 Abstract</summary>
  Large Vision-Language Models (LVLMs) achieve strong performance across many multimodal tasks; however, they often exploit spurious object-background correlations, resulting in predictions driven by contextual shortcuts rather than object-relevant visual evidence. Despite growing interest in hallucination and robustness evaluation, existing benchmarks provide limited control over whether model predictions are grounded in the target object or induced by correlated background cues. In this work, we...
  </details>

- **2026-08-30** — Teena Thomas, S. Balakrishnan — [Emergence of Strategic Equilibria from Transverse Field Ising Hamiltonian Dynamics](http://arxiv.org/abs/2608.29926v1)
  <details><summary>📄 Abstract</summary>
  Game theory studies strategic decision-making among rational agents, and many classical games can be mapped onto interaction models such as the Ising model. Quantum game theory extends this framework by allowing players to exploit quantum superposition and entanglement. In this work, we study quantum games using an operator-based formulation derived from the transverse-field quantum Ising model. We show that the Hamiltonian-driven dynamics naturally generate entangling operator which resolve the...
  </details>

- **2026-08-30** — Sheeraja Rajakrishnan, Alexander G. Ororbia, Travis Desell et al. — [Uncertainty-Driven Replay Memory for Reinforcement Learning](http://arxiv.org/abs/2608.29860v1)
  <details><summary>📄 Abstract</summary>
  Uncertainty estimation provides promising capabilities for reinforcement learning (RL) agents. Notably, estimating uncertainty can reduce the training time and enable agents to obtain greater rewards over time by exploiting information related to whether an action would facilitate exploration of portions of an environment that are well-known versus those that are relatively unknown. In this work, we propose a novel formulation of the experience replay buffer commonly used in RL that we call unce...
  </details>

- **2026-08-30** — Hyewon Choi, Donggyu Kim, Soojean Han — [SymVD: Symmetric Vision Language Action Distillation for Robot Manipulation](http://arxiv.org/abs/2608.29828v1)
  <details><summary>📄 Abstract</summary>
  While pretrained Vision-Language-Action (VLA) models offer broad generalization capabilities in robotic manipulation tasks, adapting them to real-world environments or handling task shifts often requires substantial additional data and retraining. To address this, we propose Symmetric VLA Distillation (SymVD), a distillation framework that transfers knowledge from a large VLA teacher to a compact student policy by explicitly exploiting geometric symmetries in manipulation tasks, such as rotation...
  </details>

- **2026-08-30** — Hatef Otroshi Shahreza, Asif Hussain Khan, Peter Lorenz et al. — [Foundation and Multimodal Large Language Models for Face Presentation and Morph Attack Detection](http://arxiv.org/abs/2608.29802v1)
  <details><summary>📄 Abstract</summary>
  Face recognition systems are increasingly deployed in security-critical applications, yet they remain vulnerable to presentation and morph attacks. Presentation attack detection (PAD) and morphing attack detection (MAD) are therefore essential components of trustworthy face biometrics. Despite advancements in PAD and MAD methods, existing detectors suffer from limited generalization and degrade in cross-dataset evaluation. In this paper, we systematically investigate whether general-purpose foun...
  </details>

- **2026-08-30** — A. Rahaman, A. Quadir, M. Sajid et al. — [ECA-BLS: An Efficient Complex-Augmented Broad Learning System](http://arxiv.org/abs/2608.29763v1)
  <details><summary>📄 Abstract</summary>
  Broad Learning System (BLS) is an efficient alternative to deep architectures due to its fast training, analytical learning, and strong generalization under limited data. However, existing BLS variants are confined to real-valued representations, restricting their ability to capture nonlinear interactions and second-order statistical dependencies inherent in real-world data. Notably, no prior BLS model fully exploits the complete second-order statistics that naturally emerge when data are embedd...
  </details>

- **2026-08-30** — Zhenling Duan, Pan Dong, Renshuang Jiang et al. — [Building the Truman Show: A TrustZone-Based Framework for Lightweight Out-of-band Kernel Security Monitoring](http://arxiv.org/abs/2608.29758v1)
  <details><summary>📄 Abstract</summary>
  The increasing number of vulnerabilities in operating systems, together with sophisticated kernel-level threats (e.g., rootkits), has weakened the effectiveness of traditional in-kernel protection mechanisms. Since these defenses operate at the same privilege level as the kernel, they share the same attack surface and can be bypassed once the kernel is compromised. Isolation-based security approaches provide stronger protection by separating security logic from the kernel, but strict isolation o...
  </details>

- **2026-08-30** — Tairui Wang, Zhi Zhang, Yansong Gao et al. — [JITterFlip: Uncovering Fault Attack Surfaces in JIT-Compiled LLM Serving](http://arxiv.org/abs/2608.29745v1)
  <details><summary>📄 Abstract</summary>
  LLMs are widely deployed through cloud-hosted inference services, where Just-in-Time (JIT) compilation is used to reduce recurring framework and GPU-launch overhead. JIT serving introduces a host-side control plane that selects compiled artifacts and orchestrates their execution on the GPU. Meanwhile, the shared cloud setting has motivated a growing body of bit-flip attacks (BFAs) against LLM/DNN inference. Most existing BFAs target model parameters or weights and require model-specific knowledg...
  </details>

- **2026-08-30** — Jiayi Zhang, Zexin Wang, Degang Sun et al. — [Detect Before You Attribute: Cascade Failure Attribution for Multi-Agent Systems](http://arxiv.org/abs/2608.29646v1)
  <details><summary>📄 Abstract</summary>
  Large language model (LLM)-based agents have shown strong potential in solving complex tasks through multi-step reasoning, yet they remain vulnerable to execution failures. Accurate failure attribution is therefore critical for improving agent reliability. Existing topology- and spectrum-based methods exploit trajectory structures but often overlook fine-grained semantics, while LLM-based attribution methods capture semantic cues but suffer from long-context degradation over lengthy trajectories...
  </details>

- **2026-08-30** — Haoxuan Jia, Yang Liu, Yingguang Yang et al. — [Hindsight Memory-PRM: Supervising Memory Management with Auditable Hindsight Credit](http://arxiv.org/abs/2608.29605v1)
  <details><summary>📄 Abstract</summary>
  Memory operations of long-horizon LLM agents are hard to supervise: an operation's value is unobservable when it is taken. But they are special -- they leave machine-readable evidence in the trajectory: retrieval hits and answer-time citations. Hindsight Memory-PRM exploits this audit trail twice: offline to train an operation-conditioned memory-utility critic, and online, where retrievals, citations, and one controlled deletion-and-reanswer per probe settle an intervention-calibrated entry-leve...
  </details>


### 📂 defense
*防御与防护方法 / Defense & Protection Methods* — 62 papers

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

- **2026-08-31** — Martin Bonsergent-Brachet, Jesse Read, Dany Abboud — [Geometric Attractor Monitoring: A Robust and Frugal Framework for Multi-modal Industrial Robotic Cycles](http://arxiv.org/abs/2608.30804v1)
  <details><summary>📄 Abstract</summary>
  Monitoring the health of heterogeneous industrial robot fleets is severely challenged by the multi-modal nature of their operational cycles and a persistent scarcity of run-to-failure data. Standard data-driven approaches, particularly deep learning architectures relying on sequential reconstruction, often struggle in this specific setting; they tend to over-smooth complex dynamics, masking early signs of degradation. To address these industrial constraints, we reframe the monitoring problem thr...
  </details>

- **2026-08-31** — Quan Hao, Ziyang Tao, Chenxi Zhang et al. — [RailGen: Improving Railway Intrusion Detection via Agent-Guided Small-Scale Foreign Object Generation](http://arxiv.org/abs/2608.30727v1)
  <details><summary>📄 Abstract</summary>
  Small-object detection under long-tailed data distributions is a fundamental yet challenging problem in multimedia. Railway Foreign Object Detection (RFOD) epitomizes this challenge with easily confused small intrusions and scarce samples. To address these issues, we propose a generative-augmented detection paradigm that leverages multimodal image generation to enrich the feature space of rare and small objects. We first construct RailGen, a multimodal image generation agent based on large model...
  </details>

- **2026-08-31** — Quan Hao, Chenxi Zhang, Ziyang Tao et al. — [RailSyn: Diagnosis-Guided Image Generation for Traceable Data Completion in Railway Foreign Object Detection](http://arxiv.org/abs/2608.30709v1)
  <details><summary>📄 Abstract</summary>
  Railway foreign object detection (RFOD) is critical to safe railway operation, yet scarce real positive samples incompletely represent task-relevant variations in object scale, intrusion relation, railway scene, illumination, and adverse weather. Existing synthetic augmentation can improve RFOD detection, but its gains lack an explicit account of the task-relevant deficiencies complemented by the generated data. We therefore introduce RailSyn, a diagnosis-guided framework comprising a real-refer...
  </details>

- **2026-08-31** —  Sing Team — [SingProbe Technical Report](http://arxiv.org/abs/2608.30703v1)
  <details><summary>📄 Abstract</summary>
  Runtime guardrails are essential for reliable large language model (LLM) deployment, yet existing approaches typically rely on independent, external models that introduce additional inference cost, delayed safety signals, and a capacity mismatch with increasingly capable base models. To address these issues, we introduce SingProbe, a lightweight intrinsic runtime guard that directly reuses hidden states produced during LLM inference and operates alongside autoregressive decoding. Within a unifie...
  </details>

- **2026-08-31** — Weijia Han, Lisha Qu — [When the Martingale Never Stops Firing: Anytime-Valid Gating on Real Forecast Streams](http://arxiv.org/abs/2608.30502v1)
  <details><summary>📄 Abstract</summary>
  Machine learning systems are increasingly corrected while they run, and the decision of when to intervene is increasingly delegated to statistical monitors. Anytime-valid inference promises evidence that can be acted on at any moment, exactly the guarantee this setting needs, and it is moving from theory into deployed monitoring. Conformal test martingales are the change-detection instrument, and Ville's inequality caps their false-alarm probability on exchangeable data. The guarantee is conditi...
  </details>

- **2026-08-31** — Jaewoo Ahn, Junseo Kim, Hyunseo Kim et al. — [Lies We Can See: Joint Verbal and Non-Verbal Deception by VLM Agents in Embodied Social Interactions](http://arxiv.org/abs/2608.30428v1)
  <details><summary>📄 Abstract</summary>
  Strategic deception by LLM and VLM agents has emerged as a central AI alignment and safety concern. Social-deduction games (where each player holds a hidden role and communicates with others to deduce identities) serve as the canonical testbed, particularly in multi-agent settings. Existing testbeds, however, are text-only and run on a single fixed agent configuration, missing the non-verbal sensorimotor channels treated as core by deception taxonomies and leaving it ambiguous whether an observe...
  </details>

- **2026-08-31** — Vishal Nedungadi, Xingguo Xiong, Marc Rußwurm et al. — [Foundation Models Meet Agriculture: Challenges Beyond Pretraining](http://arxiv.org/abs/2608.30392v1)
  <details><summary>📄 Abstract</summary>
  Global food security and sustainable climate action increasingly rely on robust, scalable agricultural monitoring. Earth observation foundation models have emerged as powerful, label-efficient tools across general remote sensing domains, yet early attempts to deploy them for agricultural applications have yielded surprisingly poor results. We hypothesize that this performance gap stems from the extreme heterogeneity of agricultural landscapes and the inherent inability of current earth observati...
  </details>

- **2026-08-31** — Xiaoyan Wei, Zhimin Yao, Ruilin Yang et al. — [OPUS: A Simple yet Effective Unified Framework for Open-Vocabulary Detection](http://arxiv.org/abs/2608.30247v1)
  <details><summary>📄 Abstract</summary>
  Recent unified open-vocabulary detection (OVD) supports heterogeneous prompts, including text queries, visual exemplars, and their combinations, but often rely on increasingly complex designs such as heavy cross-modal fusion, staged training, and iterative annotation pipelines. We revisit whether such complexity is necessary in the era of stronger foundation models. Our finding is that unified OVD can be made substantially simpler with semantic-rich visual representations and scalable grounding ...
  </details>

- **2026-08-31** — Arya S. Rao, Rodrigo I. Castro, Sager J. Gosai et al. — [Science sandboxes measure the scientific capability of AI agents](http://arxiv.org/abs/2608.30165v1)
  <details><summary>📄 Abstract</summary>
  Scientific progress depends not only on finding solutions, but on learning the rules that explain why they work and using that understanding to design better experiments. We introduce science sandboxes, a framework for studying this capability in AI agents through repeated cycles of experimentation, feedback, and hypothesis revision. Science sandboxes invite an agent to query the natural world in different ways, ranging from "wet" physical experiments, to "damp" predictive models trained on empi...
  </details>

- **2026-08-31** — Siddhi Pravin Lipare, Vishesh Kumar, Akshay Agarwal — [SegWave: Wavelet-Driven Segmentation of Tampered Regions](http://arxiv.org/abs/2608.30714v1)
  <details><summary>📄 Abstract</summary>
  Verifying image authenticity is increasingly difficult, posing serious risks across journalism, law enforcement, and political domains. Most existing forensic methods rely on high-level visual artifacts and treat frame detection as a simple binary task. To address this, we propose SegWave, a hybrid framework that jointly leverages spatial and frequency-domain cues for image tampering detection. SegWave integrates a transformer-based architecture with the Discrete Wavelet Transform (DWT) to captu...
  </details>

- **2026-08-31** — Athira J. Jacob, Puneet Sharma, Dorin Comaniciu et al. — [MR-JEPA: A General Purpose Video Foundation Model for Cardiac MRI](http://arxiv.org/abs/2608.30975v1)
  <details><summary>📄 Abstract</summary>
  Cardiac magnetic resonance imaging (CMR) produces rich sequential data such as temporal cine videos and spatial LGE/mapping stacks, yet most deep learning approaches process individual 2D slices, discarding this context. We present MR-JEPA, a self-supervised video foundation model for CMR that extends LeJEPA to 3D spatiotemporal inputs through tubelet tokenization, spatiotemporal masking augmentation, and initialization from a 2D CMR foundation model. Unlike prior CMR video models limited to cin...
  </details>

- **2026-08-31** — Abdullah Al Mamun, Md. Nasif Osman Khansur, Md Ashraful Hossen Akash et al. — [Beyond Accuracy: Quantifying Pulmonary Attribution in Anatomy-Guided Chest X-Ray Classification Under Domain Shift](http://arxiv.org/abs/2608.30467v1)
  <details><summary>📄 Abstract</summary>
  Deep-learning models can achieve strong chest X-ray (CXR) classification performance without establishing whether their predictions predominantly rely on pulmonary image content. This study evaluates pulmonary attribution containment as an anatomy-related reliability property distinct from diagnostic performance. We propose DBCA-SegNet-MGAP, a multi-task anatomy-guided CNN-Transformer framework that combines complementary feature representations through bidirectional cross-backbone attention, pr...
  </details>

- **2026-08-30** — Mingshuo Wang, Hanqing Guo, Huining Li et al. — [ActReal: System-Level Mobile Agents Challenge Mobile Automation Detection](http://arxiv.org/abs/2608.30038v1)
  <details><summary>📄 Abstract</summary>
  System-level mobile agents are evolving from fixed scripts into adaptive systems that continuously observe interfaces, reason, and adjust their actions, allowing automated attacks to navigate dynamic UIs and complete complex tasks. Existing applications detect automation using touch trajectories, action timing, and the physical coupling between touch and inertial measurement unit (IMU) signals. However, a privileged system-level agent executor can control both touchscreen input and application-v...
  </details>

- **2026-08-30** — Amelia Petrenciuc, Alexandru Lecu, Adrian Groza — [Memory-First Fact-Checking: A Knowledge-Graph-Grounded Multi-Agent System for Misinformation Detection](http://arxiv.org/abs/2608.29617v1)
  <details><summary>📄 Abstract</summary>
  This paper introduces a hybrid fact-checking framework that integrates Knowledge Graph-based semantic memory with adversarial multi-agent reasoning for explainable misinformation detection. The proposed system follows a memory-first, web-fallback architecture, in which input claims are initially evaluated against a dual-index Knowledge Graph through Sentence-BERT-based semantic retrieval and Natural Language Inference. When the evidence retrieved from the graph is insufficient to support a relia...
  </details>

- **2026-08-30** — Sanket Badhe, Deep Shah, Priyanka Tiwari et al. — [Towards a Systems Foundation for Agentic Skills: Architecture, Lifecycle, and Security](http://arxiv.org/abs/2608.29596v1)
  <details><summary>📄 Abstract</summary>
  Autonomous large language model (LLM) agents increasingly face reliability, context consumption, and execution stability bottlenecks when deployed on complex, long-horizon tasks. While monolithic prompt engineering and stateless tool-calling paradigms struggle to scale, the field is rapidly converging toward \emph{agentic skills}: modular procedural abstractions that externalize execution knowledge into reusable, executable, and portable artifacts. This paper establishes a unified systems founda...
  </details>

- **2026-08-30** — Abdullah Hashmat, Usman Naseem, Agha Ali Raza — [Pak3H: Evaluating the Cost of Cultural Mismatch in LLM Alignment with a Human-Contextualized Urdu Benchmark](http://arxiv.org/abs/2608.30065v1)
  <details><summary>📄 Abstract</summary>
  Large language models (LLMs) demonstrate strong Helpfulness, Harmlessness, and Honesty (3H) alignment in English-centric settings, but these gains transfer poorly to low-resource languages due to cultural mismatches. Existing multilingual 3H benchmarks rely predominantly on automated translation or LLM based synthesis, propagating source-language biases while sacrificing local relevance. To address this gap, we introduce Pak3H1, the first human-validated, culturally contextualized Urdu benchmark...
  </details>

- **2026-08-30** — Haoting Zhang, Haoxian Chen, Jiayuan Sheng et al. — [Spec2Twin-Chain: Orchestrating Bi-Level Optimization with LLMs for Blockchain Digital Twin Construction](http://arxiv.org/abs/2608.30050v1)
  <details><summary>📄 Abstract</summary>
  Building a blockchain digital twin largely requires translating domain knowledge and specific system descriptions into a simulator architecture, calibrating its parameters against behavioral evidence, and validating the constructed twin. These steps are commonly performed through application-specific modeling efforts that can be difficult to reuse across systems and downstream decision problems. We consider automating this process through Spec2Twin-Chain, a framework that formulates blockchain d...
  </details>

- **2026-08-30** — Hanjun Luo, Qiushi Liu, Jingya Zhang et al. — [AutoCRAT: Within-trajectory Joint Control of Stochasticity and Compute for LLM Reasoning](http://arxiv.org/abs/2608.29988v1)
  <details><summary>📄 Abstract</summary>
  Large language models (LLMs) achieve strong reasoning performance, which depends critically on inference-time decisions. Yet these decisions are commonly handled by static, one-size-fits-all policies, limiting adaptation to diverse tasks and reasoning stages. Recent adaptive methods partially address this limitation, but they primarily adapt either decoding stochasticity (how the model explores) or reasoning compute (how long the model reasons) in isolation, leaving their interaction within a si...
  </details>

- **2026-08-30** — Armaan Singh, Ryan Trinh Le, Jasmine Kaur et al. — [Detecting Hidden Chain-of-Thought in Large Language Models with Linguistic, Behavioral, and Mechanistic Indicators](http://arxiv.org/abs/2608.29956v1)
  <details><summary>📄 Abstract</summary>
  Large language models often answer complex reasoning questions without revealing intermediate steps, raising whether they reason latently or complete patterns. We propose the Hidden CoT Detection Score (HCDS), a comparative behavioral and mechanistic signal measuring whether neutral-prompt behavior aligns more closely with explicit CoT or explicit no- CoT. Here, hidden CoT operationally denotes this neutral-prompt CoT-like alignment; HCDS does not directly observe or prove an unexposed reasoning...
  </details>

- **2026-08-30** — Zhirui Fang, Qingchi Yu, Ziyang Chen et al. — [EMERGE-Policy: A Robot Mind Emerges Beyond a Single Policy](http://arxiv.org/abs/2608.29896v1)
  <details><summary>📄 Abstract</summary>
  A robot's effective ``mind'' need not reside in a single policy. It can emerge when specialized components perceive, reason, predict, act, verify, and remember within a shared orchestration process. EMERGE-Policy turns this perspective into a graph-structured agentic framework that coordinates both capability invocation and information exchange. A Main Agent retains task-level state within an active context window, while role-specific Sub Agents process perception, execution monitoring, verifica...
  </details>

- **2026-08-30** — Chia-Hsuan Wu, Dar-Hsin Dustin Wu, Rui Fang et al. — [HSMLog: Small Language Model-Assisted Hardware Security Module Log Anomaly Detection with Behavioral Analysis](http://arxiv.org/abs/2608.29773v1)
  <details><summary>📄 Abstract</summary>
  Hardware Security Module (HSM) logs capture security-critical behavior, but anomalies emerge from relationships across event sequences, keys, object states, sessions, and temporal patterns rather than isolated events. Existing methods separate detection from HSM-specific evidence validation and reporting. In this paper, we present HSMLog, a two-stage framework for HSM log anomaly detection with retrieval-grounded behavioral analysis. In Stage 1, a small language model (SLM) identifies candidate ...
  </details>


### 📂 alignment
*对齐与安全约束 / Alignment & Safety Constraints* — 73 papers

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

- **2026-08-31** — Daniel Agyei Asante, Yang Li — [TopoCompress: Long Context Compression via Graph-Wired Semantic Trajectories](http://arxiv.org/abs/2608.30811v1)
  <details><summary>📄 Abstract</summary>
  Long-context compression is essential for reducing the cost and latency of large language model inference. However, existing methods can fragment important evidence, require additional training or alignment, and often depend on the target model for effective compression. We introduce TopoCompress, a training-free and model-agnostic framework that compresses long contexts by selecting coherent semantic spans. TopoCompress first scores each span using dense and lexical query relevance together wit...
  </details>

- **2026-08-31** — Adonay Demewez Gebremedhin, Wessam Shehieb, Sara Alansari et al. — [CheXGround: Anatomical Region Tokens for Grounded Longitudinal Chest X-ray Interpretation](http://arxiv.org/abs/2608.30758v1)
  <details><summary>📄 Abstract</summary>
  Recent radiology multi-modal language models have made substantial progress in chest X-ray report generation, visual question answering, and temporal reasoning. While longitudinal chest X-ray interpretation compares sequential examinations to describe change, visual grounding aims to connect clinical language with localized image evidence. Although longitudinal modeling and visual grounding have each advanced radiology language models, how localized visual evidence can support longitudinal inter...
  </details>

- **2026-08-31** — Mohammad Reza Modarres, Armin Tourajmehr, Yadollah Yaghoobzadeh et al. — [CLIN: an Objective Framework for Evaluating Creativity in Short Persian Literary Text](http://arxiv.org/abs/2608.30754v1)
  <details><summary>📄 Abstract</summary>
  Evaluating creativity in large language model (LLM) outputs remains challenging because creativity is multidimensional and human-centered. We examine how reliably LLMs evaluate short literary text in Persian, a low-resource language, across multiple evaluation strategies and prompt formulations. We find that LLM-human agreement varies substantially across dimensions: alignment is stronger for structured TTCT-derived properties such as Originality, Fluency, and Elaboration, but considerably weake...
  </details>

- **2026-08-31** — Xingyu Ding, Yuzhong Zhao, Chunhai Zhao et al. — [Temporal Forcing: 4D Representation Alignment for Vision-Language-Action Models](http://arxiv.org/abs/2608.30643v1)
  <details><summary>📄 Abstract</summary>
  Recent vision-language-action (VLA) methods improve manipulation performance by aligning their representations with 3D scene geometry. However, these methods often struggle with long-horizon manipulation and observation aliasing between visually similar states due to a lack of temporal information: the 3D scene geometry captures only the current state, rather than how it has evolved over time. To resolve this, we present Temporal Forcing, a 4D representation alignment method for VLA models. Spec...
  </details>

- **2026-08-31** — Gaoming Zhang, Angqing Jiang, Jianchun Song et al. — [Preference Shapes Relevance: Cross-component Hierarchical Semantic Alignment for Personalized Generative Retrieval](http://arxiv.org/abs/2608.30553v1)
  <details><summary>📄 Abstract</summary>
  Generative Retrieval (GR) has emerged as a promising paradigm by mapping queries directly to Semantic IDs (SIDs) with powerful representation capabilities for candidate items. However, existing SIDs derived solely from item content create a semantic gap, failing to align dynamic query intents with static item representations. Furthermore, current generative paradigms rarely model user behavior sequences and are always bottlenecked by the high inference latency of beam-search autoregressive decod...
  </details>

- **2026-08-31** — Erica Lastufka, Mariia Drozdova, Daniel Schaerer et al. — [DINOspec: Efficient Multimodal Alignment of Vision and Spectral Foundation Models for Astronomy](http://arxiv.org/abs/2608.30503v1)
  <details><summary>📄 Abstract</summary>
  Astronomical observations provide multimodal views of physical systems, with images and spectra capturing complementary properties of celestial objects. Scientific foundation models can learn powerful representations from these observations, but representations learned by separate models remain difficult to combine. We investigate whether physical representations learned by separate vision and spectral models can be aligned without retraining their encoders. We introduce DINOspec, a multimodal f...
  </details>

- **2026-08-31** — Shuto Ito, Yuta Shimoda, Haruka Fukunishi et al. — [Polymer Membrane Tensegrity: Inverse Design of Polymer Films Morphing into Freeform 3D Surfaces with Digital Photopatterning Technique](http://arxiv.org/abs/2608.30501v1)
  <details><summary>📄 Abstract</summary>
  In Metamorphosis of Plants (1790), Goethe traced diverse plant organs to transformations of a common leaf-like structure -- a principle modern mechanics attributes to two material ingredients: non-uniform in-plane strain from differential growth or shrinkage, and spatially patterned stiffness. Here we translate this principle into a synthetic fabrication framework called Polymer Membrane Tensegrity (PMT). A flat elastomeric film swollen with a second monomer is selectively UV-cured through a liq...
  </details>

- **2026-08-31** — Yi Zhang, Yi Wang, Yueting Wu et al. — [SeqAlign3DVG: A Sequence-Aligned Benchmark and Voxel Reasoning Framework for 3D Visual Grounding](http://arxiv.org/abs/2608.30451v1)
  <details><summary>📄 Abstract</summary>
  Image-based 3D visual grounding is critical for embodied agents, yet existing benchmarks suffer from loose text-observation alignment and neglect temporal ordering. We introduce SeqAlign3DVG, a novel benchmark dedicated to temporally ordered and strictly observation-aligned image-based 3D visual grounding. Unlike prior works using order-agnostic views or global point clouds, SeqAlign3DVG ensures all expressions are human-verified and strictly grounded in the provided RGB observations (single fra...
  </details>

- **2026-08-31** — Yunqi Liu, Yang Zhang, Ruixing Zhang et al. — [SemPOI-RL: Aligning LLM Semantic Reasoning for Interpretable Out-of-Town POI Sequential Generation](http://arxiv.org/abs/2608.30399v1)
  <details><summary>📄 Abstract</summary>
  Large language models (LLMs) exhibit strong semantic reasoning and open-ended generation abilities, but aligning these abilities with structured sequential generation remains challenging. This challenge is particularly evident in out-of-town (OOT) POI sequence generation, where a model must infer transferable travel intent from a user's hometown behaviors, adapt to cross-city interest drift, and generate a coherent destination trajectory under structural constraints. Existing approaches either r...
  </details>

- **2026-08-31** — Minsoo Song, Chanwoo Kim, Sugyeong Eo et al. — [Beyond Consensus: Downward Bias and Role Asymmetry in Multi-Agent LLM Judges for Subjective Evaluation](http://arxiv.org/abs/2608.30373v1)
  <details><summary>📄 Abstract</summary>
  Multi-Agent Debate (MAD) has been widely adopted to improve LLM-based evaluation by prompting multiple agents to negotiate and reach a consensus. However, for subjective rubric-based scoring, inter-agent agreement does not guarantee alignment with human judgments. In this paper, we compare a single-judge baseline against a consensus-based MAD protocol on subjective evaluation tasks and design three ablations to isolate the impact of role prompting, multi-round interaction, and explicit score sha...
  </details>

- **2026-08-31** — Minsoo Song, Chanjun Park — [Auditing MCQA Benchmarks through Probability Landscapes](http://arxiv.org/abs/2608.30372v1)
  <details><summary>📄 Abstract</summary>
  As Large Language Models rapidly advance, performance on standard multiple-choice question answering (MCQA) benchmarks is reaching saturation. While the community has responded by developing increasingly difficult datasets, validating question quality and filtering flawed items remains a labor-intensive process. To provide a scalable diagnostic approach, we propose a two-component probabilistic framework for auditing MCQA benchmarks using model output distributions. First, for benchmark-level an...
  </details>

- **2026-08-31** — Jin Gan, Xin Li, Jun Luo — [Beyond Token-Level Guidance: Inference-Time Alignment of Specialized LLMs via Cross-Family Representation Steering](http://arxiv.org/abs/2608.30319v1)
  <details><summary>📄 Abstract</summary>
  Large language models (LLMs) finetuned for specialized domains represent crucial high-impact applications. Inference-time alignment improves safety degraded from specialization finetuning without requiring substantial computational resources, complementing finetuning-based methods with an easy-to-use, plug-and-play solution. However, existing inference-time methods fail to reliably improve safety without disrupting domain capability. We identify the root cause as complementary expertise orthogon...
  </details>

- **2026-08-31** — Rahul Bapusaheb Kodag, Vipul Arora — [Weakly Supervised Tabla Stroke Transcription via an Adaptive Dynamic Rhythm Language Model (ADRM)](http://arxiv.org/abs/2608.30314v1)
  <details><summary>📄 Abstract</summary>
  Tabla Stroke Transcription (TST) is central to the analysis of rhythmic structure in Hindustani music, yet it remains challenging due to complex and dynamic rhythmic organization and the scarcity of strongly annotated data. Existing approaches largely rely on fully supervised learning with onset-level annotations, which are costly and impractical at scale. This work addresses TST in a weakly supervised setting, using only symbolic stroke sequences without temporal alignment of onsets. We propose...
  </details>

- **2026-08-31** — Zhichao Hou, Ferhat Erata, Joe Lilien et al. — [Stratified Consistency Distillation for Natural Language Formalization](http://arxiv.org/abs/2608.30258v1)
  <details><summary>📄 Abstract</summary>
  Neurosymbolic reasoning has shown promising success in addressing complex reasoning tasks by combining large language models (LLMs) and symbolic solvers. While this approach shows promise, a fundamental challenge remains: improving the accuracy of translations from natural language to logical formulas. Current methods predominantly rely on prompt engineering, which is difficult to scale across different domains and input formats. Drawing inspiration from the success of fine-tuning in other model...
  </details>

- **2026-08-31** — Hongzhe Bi, Zihao Zhou, Yihang Tang et al. — [Motus2: A Self-Evolving General World Model for Dexterous Manipulation](http://arxiv.org/abs/2608.30237v1)
  <details><summary>📄 Abstract</summary>
  General embodied agents should perceive, predict, act, evaluate, and improve within a unified system. World models have shown great promise in building such agents, yet existing models typically append an action output head to a world simulator, without coupling them into a closed decision-and-learning loop for policy improvement. We present Motus2, a self-evolving general world model for dexterous manipulation. Motus2 advances world modeling through model scaling and data scaling. For model sca...
  </details>

- **2026-08-31** — Mohanad Odema, Jacob Song — [LaMoC: Loss-Aware Modular Compression for LLMs](http://arxiv.org/abs/2608.30226v1)
  <details><summary>📄 Abstract</summary>
  Modular compression has enabled considerable parameter reduction in LLMs while preserving strong language understanding and downstream task accuracy. However, existing joint modular compression methods primarily rely on activation statistics, leaving loss-sensitivity information and its module-level characterization underexplored. We investigate addressing this gap with LaMoC, a loss-aware modular compression methodology that blends activation and Empirical Fisher statistics through gradient-err...
  </details>

- **2026-08-31** — Yuyang Hong, Jinhui Guo, Jiaqi Gu et al. — [DICS: Exploring Data Intrinsic Consistency for Visual Instruction Selection](http://arxiv.org/abs/2608.30209v1)
  <details><summary>📄 Abstract</summary>
  Visual instruction tuning is crucial for advancing the vision-language alignment and instruction-following capabilities of Vision-Language Models (VLMs). However, identifying optimal subsets under a fixed ratio constraint from rapidly expanding datasets remains a significant bottleneck. While existing methods largely depend on distribution diversity or heuristic filtering, they often overlook the internal coherence within individual samples. To bridge this gap, we propose Data Intrinsic Consiste...
  </details>

- **2026-08-31** — Yujiang Pu, Yu Kong — [NoisEasier: Test-Time Noise Optimization for Text-to-Video Generation](http://arxiv.org/abs/2608.30194v1)
  <details><summary>📄 Abstract</summary>
  Diffusion models have recently advanced text-to-video (T2V) generation, yet they still struggle with fine-grained compositional alignment, such as attribute binding, spatial relations, and object interactions. While reward-based fine-tuning improves alignment, it is susceptible to reward hacking and adapts poorly to new prompt distributions. In this work, we propose NoisEasier, a test-time scaling framework that improves T2V generation through differentiable reward-guided noise optimization with...
  </details>

- **2026-08-31** — Boqi Chen, Xudong Liu, Yunke Ao et al. — [GPAgentBench-2K: Benchmarking Large Language Model Agents in Complex Clinical Action Space](http://arxiv.org/abs/2608.30188v1)
  <details><summary>📄 Abstract</summary>
  Large Language Models (LLMs) show great potential as clinical agents, yet existing benchmarks reduce clinical workflows to static predictions or unconstrained Markov Decision Processes (MDPs) with coarse action sets. To address this, we introduce GPAgentBench-2K, the first Constrained MDP (CMDP) LLM-agent benchmark for primary-care clinical decision-making, constructed from expert-validated records of real-world GP encounters. Our environment models a full spectrum of six foundational clinical a...
  </details>

- **2026-08-31** — Zhiqin Yang, Jingwen Fu, Yuhan Liu et al. — [Scaling Large Reasoning Models beyond Human Supervision: A Path toward Superintelligence](http://arxiv.org/abs/2608.31075v1)
  <details><summary>📄 Abstract</summary>
  Recent advances in large reasoning models (LRMs) have shown that reinforcement learning with verifiable rewards (RLVR) can substantially improve reasoning in mathematics and code, where outcomes can be checked automatically. Extending this progress to open-ended and agentic tasks remains difficult because reliable rewards are harder to obtain and direct human supervision cannot keep pace with the scale and complexity of model-generated experience. This paper studies how LRMs can continue to impr...
  </details>

- **2026-08-31** — Laur Sisask, Ardi Tampuu, Tambet Matiisen — [What Emerges and What Breaks in Self-Play Driving](http://arxiv.org/abs/2608.30819v1)
  <details><summary>📄 Abstract</summary>
  Training autonomous driving policies through pure self-play has recently shown promising results. Following Gigaflow and Puffer- Drive, we train driving policies in a similar self-play fashion, but extend the models from MLPs to Transformers and train on the high-definition map of a real city, where we ultimately aim to deploy them. On the CARLA and Waymax benchmarks, our policies fall short of Gigaflow, and we trace the gap to specific failure modes, including reward hacking at traffic lights a...
  </details>

- **2026-08-31** — Chuhan Zhang, Ebrahim Shahabi, Kseniia Khomenko et al. — [Learning to infer and manipulate through distributed whole-arm interaction in a soft robot](http://arxiv.org/abs/2608.30773v1)
  <details><summary>📄 Abstract</summary>
  In animals such as elephants and octopuses, acquiring non-visual information about an object and physically engaging with it are inseparable processes mediated by rich, large-area interactions between compliant appendages and the environment. Soft robots provide a natural platform for translating this principle into engineered systems. Yet current robotic intelligence makes limited use of physical interaction, treating it primarily as a disturbance to be rejected or, at best, as a means of compe...
  </details>

- **2026-08-30** — Ashvin Gupta, Denys Prociuk, Alessandra Russo et al. — [Automatic Conversion of NICE Guidelines to an Executable Computational Model Using Large Language Models](http://arxiv.org/abs/2608.30022v1)
  <details><summary>📄 Abstract</summary>
  Introduction: NICE guidelines provide evidence-based recommendations for clinical care but remain largely in unstructured natural language. Existing approaches to converting them into computable representations often focus on individual diseases, require substantial manual encoding, and do not scale. Large language models (LLMs) may enable much of this translation to be automated. Methods: We present an end-to-end approach that converts textual clinical guidelines into executable models capable ...
  </details>

- **2026-08-30** — Lucas A. Dias, Henrique A. Schulz, Rafaela de Miranda et al. — [Confidence-Aware Ensemble and Long-Word Refinement for Artistic Text Recognition](http://arxiv.org/abs/2608.29970v1)
  <details><summary>📄 Abstract</summary>
  Artistic Text Recognition (ATR) remains challenging because word images often combine decorative fonts, curved layouts, object-like characters, clutter, and severe distortions. This paper studies WordArt-V1.5 as a standardized benchmark for this setting and evaluates recent scene and artistic text recognizers under a common protocol. We propose a confidence-aware ensemble that combines SVTRv2, PARSeq, and MAERec after fine-tuning on the official training split. The ensemble selects predictions u...
  </details>

- **2026-08-30** — Kun Efimov-Zhang, Yifei Song, Claire Gardent — [XQDT: eXplainable and Quantitative Data-Text Alignment Metric with Feedback Signals](http://arxiv.org/abs/2608.29948v1)
  <details><summary>📄 Abstract</summary>
  Evaluating data-text alignment remains challenging: existing metrics often provide limited explanations for the scores, while prompt-based LLM-as-Judge methods can be expensive and unreliable. We present an end-to-end explainable evaluation metric that fine-tunes a language model to identify omitted, extra, incorrect, and correct data units in a data-text pair. These local judgements are aggregated into precision, recall, and F1 scores, providing both fine-grained diagnostic feedback and an inte...
  </details>

- **2026-08-30** — Muxin Liu, Tianbo Liu, Jing Xia et al. — [OptiGeo: Efficient Monocular Geometry for Embodied Perception in Optically Challenging Scenes](http://arxiv.org/abs/2608.29881v1)
  <details><summary>📄 Abstract</summary>
  Monocular depth estimation has achieved strong open-domain generalization, yet reliable robotic deployment remains difficult in transparent, reflective, and specular environments, where depth sensors often produce missing or biased depth. Existing methods often handle such optical failures with scene-specific preprocessing, auxiliary modules, or post-hoc fine-tuning. While effective in constrained settings, these designs increase architectural redundancy and can over-specialize general geometry ...
  </details>

- **2026-08-30** — Huiyi Zhang, Zijian Li, Xiaocheng Feng et al. — [ACTD: Anchor-Based Cross-Tokenizer Distillation with Residual Regularization](http://arxiv.org/abs/2608.29662v1)
  <details><summary>📄 Abstract</summary>
  Knowledge distillation effectively transfers reasoning capabilities from large language models to lightweight student models. To enable knowledge transfer across disparate model families, researchers increasingly explore cross-tokenizer distillation. However, cross-tokenizer distillation remains challenging due to vocabulary and sequence misalignment, while approximate vocabulary alignment can introduce additional noise into distillation. To address these challenges, we propose Anchor-Based Cros...
  </details>


### 📂 robustness
*鲁棒性与可靠性 / Robustness & Reliability* — 63 papers

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

- **2026-08-31** — Debarpan Bhattacharya, Malay Phadke, Sriram Ganapathy — [BiG-SURE - Bipartite Graph for Semantic Uncertainty and Reliability Estimation of LLMs](http://arxiv.org/abs/2608.30646v1)
  <details><summary>📄 Abstract</summary>
  Reliable uncertainty estimation is a crucial requirement for deploying large language models (LLMs) and vision-language models (VLMs) in safety-critical settings, especially when the model parameters are not accessible (black-box). We propose BiG-SURE, an uncertainty estimator based on cross-temperature semantic agreement. The method samples low-temperature responses as stable semantic anchors and high-temperature responses as probes under meaning-preserving input transformations. It then constr...
  </details>

- **2026-08-31** — Peijun Qing, Fobo Shi, Soroush Vosoughi — [UTILMEM: Benchmarking Evidence Utilization in Long-Term Conversational Memory](http://arxiv.org/abs/2608.30508v1)
  <details><summary>📄 Abstract</summary>
  Long-term memory is increasingly important for conversational agents, yet existing benchmarks primarily measure memory through pointwise factual recall: whether a system can recover isolated facts or event-level details from prior interactions. Real-world memory use, however, often requires a more demanding capability: integrating distributed, implicit, and noisy evidence across extended interaction histories into coherent, task-oriented outputs. We call this capability memory utilization. Here,...
  </details>

- **2026-08-31** — Zixing Lei, Gengze Zhou, Xiong-Hui Chen et al. — [Scaffolding Foundation Models into Physical-World Agents Pushes the Frontier of Long-Horizon Navigation](http://arxiv.org/abs/2608.30396v1)
  <details><summary>📄 Abstract</summary>
  Long-horizon physical-world agents must reason over distant goals while grounding decisions in reliable closed-loop behavior. Today's foundation models split these capabilities: vision-language models (VLMs) infer missing information and adapt high-level plans but remain brittle and inefficient at repeated navigation grounding, while navigation foundation models (NFMs) robustly execute semantic goals but operate as bounded episodes without persistent task-level reasoning. We introduce NavMCP, an...
  </details>

- **2026-08-31** — Zhuoran Lu, Yangyang Yu, Zhuoyan Li et al. — [Using Grounded Theory for Agent Behavior Analysis at Scale](http://arxiv.org/abs/2608.30391v1)
  <details><summary>📄 Abstract</summary>
  Understanding agent behavior requires methods that scale to thousands of trajectories and surface new patterns in long, often unfamiliar tasks where pre-built classifiers fall short. We propose to bring grounded theory into agent trajectory analysis: a six-decade-old qualitative method from the social sciences, with a principled saturation criterion and an auditable trail from data to theory. We propose AutoTraceGT (Automated Trace analysis through Grounded Theory), the first multi-agent pipelin...
  </details>

- **2026-08-31** — Ziheng Li, Xichen He, Haoyan Chen et al. — [Augmenting Human Performance with an XR Agent Learning from Online Behavior and BCI Evidence](http://arxiv.org/abs/2608.30369v1)
  <details><summary>📄 Abstract</summary>
  We present OLIVE, a framework for adapting a foundation model to provide real-time assistance in temporally demanding, high-stakes, and dynamic tasks. We show that passive EEG, fused online with behavioral evidence, can meaningfully extend the number of targets users detect and engage beyond their unaided action bandwidth. OLIVE learns from both explicit behavioral signals (the targets the user shoots down in an XR first-person shooter game) and implicit physiological signals (fixation-locked EE...
  </details>

- **2026-08-31** — Tingnan Bao, Medhat Elsayed, Pedro Enrique Iturria-Rivera et al. — [Agentic Quantum Deep Reinforcement Learning for RAN Slicing](http://arxiv.org/abs/2608.30206v1)
  <details><summary>📄 Abstract</summary>
  Radio access network (RAN) slicing enables ultra-reliable low-latency communications (URLLC) and enhanced mobile broadband (eMBB) services to share radio resources, but their requirements create a challenging reliability--throughput tradeoff. URLLC requires low-latency and reliable packet delivery, whereas eMBB targets high sustained throughput. This paper considers downlink URLLC/eMBB RAN slicing and formulates it as a queue-aware long-term eMBB throughput maximization problem subject to URLLC ...
  </details>

- **2026-08-31** — Shangqing Tu, Daniel Zhang-Li, Yucheng Wang et al. — [CogEvol: Towards Efficient and Reliable Learning Environment Generation](http://arxiv.org/abs/2608.30968v1)
  <details><summary>📄 Abstract</summary>
  We present CogEvol, a family of models trained specifically for Learning Environment Generation: turning a course brief into a finished learning artifact (structured-JSON slides or self-contained interactive HTML pages) in a single pass. Across 220k production requests, CogEvol completes a slide in a median of 17 seconds and an interactive page in 59, replacing minutes-long multi-turn agent scaffolding. Reliability is enforced rather than hoped for: a production-grounded data pipeline turns real...
  </details>

- **2026-08-31** — Ramya Keerthy Thatikonda, Wray Buntine, Ehsan Shareghi — [Beyond Surface Forms: Symbolic Edits as a Test for Logical Reasoning with LLMs](http://arxiv.org/abs/2608.30256v1)
  <details><summary>📄 Abstract</summary>
  Logical reasoning with large language models (LLMs) is a critical capability, as it reflects a system's ability to correctly deduce hypotheses from a given context using faithful deductive processes. However, LLM reasoning has often been shown to be sensitive to small surface-level variations in problem formulation, raising questions about whether models truly follow the underlying logical structure. Studying this behavior is challenging because the symbolic components of logical problems, such ...
  </details>

- **2026-08-31** — Yunxiang Fu, Meng Lou, Yizhou Yu — [One Adapter, Many Tasks: Task-Conditioned Feature Transformations for Continual Learning](http://arxiv.org/abs/2608.31096v1)
  <details><summary>📄 Abstract</summary>
  Class-incremental learning (CIL) requires a model to incrementally learn tasks that contain new classes without accessing earlier training data while preserving the ability to recognize all seen classes. Recently, pretrained-model-based approaches have become prevalent by adapting a frozen backbone with additional lightweight trainable modules. Existing methods, however, exhibit limitations: task-specific adapters learn explicit per-task representations but are parameter- and computation-ineffic...
  </details>

- **2026-08-31** — Xinglong Liang, Chunyao Lu, Tianyu Zhang et al. — [Pretrained, Curriculum-Tuned, and Ensembled: A Tracer-Aware Interactive Segmentation Pipeline for AutoPET V](http://arxiv.org/abs/2608.30844v1)
  <details><summary>📄 Abstract</summary>
  Interactive lesion segmentation in whole-body PET/CT requires a model to provide a strong initial prediction while also responding efficiently to sparse corrective scribbles during inference. This setting is particularly challenging because tracer distributions, physiological uptake patterns, lesion appearance, and acquisition characteristics differ substantially between FDG and PSMA studies. We present TRIAGE, Tracer-aware Refinement via Interactive Anatomy-Guided sEgmentation. The core backbon...
  </details>

- **2026-08-31** — Elena Merdjanovska, Jonas Golde, Alan Akbik — [Error-Type-Aware Loss Reweighting for Robust Named Entity Recognition with Noisy LLM Labels](http://arxiv.org/abs/2608.30827v1)
  <details><summary>📄 Abstract</summary>
  Large language models are increasingly used to annotate datasets for training smaller, task-specialized models such as named entity recognition. While this method yields effective models, it assumes that the synthetic dataset is correctly annotated. In this work, we find that (i) current fine-tuning processes simply ignore LLM-introduced annotation noise, resulting in degraded performance and (ii) existing noise-robust losses are not transferable to sequence labeling because annotation noise in ...
  </details>

- **2026-08-31** — Junhee Lee, Seunghwan Kim, Hongro Jang et al. — [CIG-RL: Curiosity-Driven Information-Guided Reinforcement Learning for Source Term Estimation in Uncertain Environments](http://arxiv.org/abs/2608.30673v1)
  <details><summary>📄 Abstract</summary>
  Source term estimation (STE), which aims to estimate key properties of the gas source, is essential for identifying hazardous gas releases. Information-theoretic approaches have been adopted for autonomous STE using mobile sensors due to robustness in noisy environments, yet their online action selection incurs substantial computational cost. Deep reinforcement learning (DRL) provides a promising alternative with its fast decision-making capability. In DRL-based STE, the agent selects actions ba...
  </details>

- **2026-08-31** — Erica Lastufka, Mariia Drozdova, Vitaliy Kinakh et al. — [Learning Radio Astronomical Representations with LeJEPA and Very Small Models](http://arxiv.org/abs/2608.30594v1)
  <details><summary>📄 Abstract</summary>
  Representations learned by vision foundation models pretrained on natural images have been shown to be useful for out-of-domain astronomical images. Performance on scientific downstream tasks increases with model size, which both carries higher inference costs and limits scalability, even when considering parameter-efficient adaptation. An alternative is to learn representations directly from astronomical observations rather than natural images, through self-supervised pretraining.   We evaluate...
  </details>

- **2026-08-31** — Malhar Udmale, Divyanshu Dwivedi, Aarohi Dhand et al. — [Federated Multi-Task Learning for Bladder Tumor Segmentation and MIBC Classification Using a Hybrid CNN-Transformer Architecture](http://arxiv.org/abs/2608.30458v1)
  <details><summary>📄 Abstract</summary>
  Accurate bladder tumor segmentation and assessment of mus- cle invasion from T2-weighted MRI are important for treatment plan- ning, but developing robust models across institutions is challenging be- cause patient data cannot be centrally pooled and imaging characteristics vary across scanners and acquisition protocols. We propose a federated multi-task learning framework for joint bladder tumor segmentation and MIBC/NMIBC classification across four clinical centers. The proposed Swin Hybrid mo...
  </details>

- **2026-08-31** — Markel Ferro, Oier Lopez de Lacalle — [Learning to Reason and Use Tools through Unsupervised Fine-Tuning in Task-Oriented Dialog Systems](http://arxiv.org/abs/2608.30426v1)
  <details><summary>📄 Abstract</summary>
  Current dialogue systems struggle with dynamic information retrieval, often leading to hallucinations and lower response accuracy. We address this by adapting the ReAct framework for Task-Oriented Dialogue, enabling Large Language Models (LLMs) to access external knowledge and produce factual responses. Mainly, we propose an unsupervised fine-tuning pipeline that harvests reasoning trajectories via in-context learning inference. High-quality samples are filtered using an LLM-based judge to const...
  </details>

- **2026-08-31** — Haoxu Huang, Narges Razavian — [Uncertainty of Vision Medical Foundation Models](http://arxiv.org/abs/2608.30390v1)
  <details><summary>📄 Abstract</summary>
  Accurate uncertainty estimation is essential for machine learning systems de- ployed in high-stakes domains such as medicine. Traditional approaches primarily rely on probability outputs from trained models (point predictions), which provide no formal guarantees on prediction coverage and often require additional calibra- tion techniques to improve reliability. In contrast, conformal prediction (region prediction) offers a principled alternative by generating prediction sets with finite- sample ...
  </details>

- **2026-08-31** — Yi Fang, Que Shen, Chengpeng Li et al. — [Answer Probing-Guided Search for Diverse Solution Exploration of LLMs](http://arxiv.org/abs/2608.30345v1)
  <details><summary>📄 Abstract</summary>
  Generating multiple diverse and high-quality solutions is valuable for many applications, such as code-test generation and drug discovery. However, Large Language Models (LLMs) tend to converge on a single high-confidence solution during inference, limiting exploration of alternative valid solution paths. Existing test-time methods promote diversity through tree-like search and prune semantically similar branches using response-level semantic embeddings. However, we find that such embeddings are...
  </details>

- **2026-08-31** — Hanshu Rao, Guangzeng Han, Xiaolei Huang — [AIA$^{2}$: Attribute-Agnostic Imbalance Augmentation for Subgroup Robustness](http://arxiv.org/abs/2608.30297v1)
  <details><summary>📄 Abstract</summary>
  Attributes describing data content and context can induce diverse imbalance patterns that go beyond label imbalance alone. However, existing studies primarily address label imbalance while overlooking data attributes, such as topics and demographics, which can induce meaningful subgroup structure while causing model degradation on underrepresented subgroups. We propose Attribute-Agnostic Imbalance Augmentation (AIA$^{2}$), a framework for improving model robustness under varying subgroup imbalan...
  </details>

- **2026-08-31** — Haoran Wang, Jing Yao, Xu Yang et al. — [SimCRAFT: Distilling Remote Sensing Agents via Synthetic Trajectories and Contextual Retrieval-Augmented Fine-Tuning](http://arxiv.org/abs/2608.30277v1)
  <details><summary>📄 Abstract</summary>
  The unprecedented surge in Earth observation data volume and diversity has exposed a critical bottleneck for traditional manual workflows, catalyzing the emergence of Remote Sensing (RS) Agents. However, the practical deployment of these advanced agents is severely hindered by their heavy reliance on large-scale general-purpose LLMs, which lack deep domain expertise and impose prohibitive infrastructure demands. To resolve this, we propose SimCRAFT, a model-agnostic framework that distills sophi...
  </details>

- **2026-08-31** — Shunjie Wen, Jaeyeon Lee, Dong-Wan Choi — [Centering before Pruning: Lightweight Geometry Correction for Diversity-Based Visual Token Pruning in LVLMs](http://arxiv.org/abs/2608.30263v1)
  <details><summary>📄 Abstract</summary>
  Large vision-language models (LVLMs) incur substantial inference costs due to their long and highly redundant visual-token sequences. Diversity-based pruning mitigates this cost by selecting token subsets based on pairwise cosine similarity. We find, however, that similarities between raw visual tokens are strongly concentrated in the positive range, limiting their ability to distinguish non-redundant tokens. A natural way to improve this resolution is to center token features before computing c...
  </details>

- **2026-08-31** — Hyeonjin Kim, Minseok Kim, Seunghyeon Jung et al. — [FaVOR: LLM-Based Agentic Framework for Factor Mining via Empirical Validation](http://arxiv.org/abs/2608.30192v1)
  <details><summary>📄 Abstract</summary>
  Traditional finance relies on experts to hand-craft factors through a principled process grounded in economic rationale. Recent LLM-based multi-agent systems have automated this process, scaling factor mining far beyond manual effort. However, these automated approaches optimize directly for returns and rarely check whether a generated factor still expresses the economic hypothesis that motivated it. We identify this inconsistency between mathematical form and economic meaning as a structural fa...
  </details>

- **2026-08-31** — Amir Saeidi, Zehua Zhang, Rishitosh Singh et al. — [CAST: Critique-Aware Supervision for Training Reliable Long-Horizon Tool-Calling Agents](http://arxiv.org/abs/2608.30147v1)
  <details><summary>📄 Abstract</summary>
  Large language model (LLM) agents are increasingly deployed in long-horizon, interactive, and stateful environments. In these settings, a single wrong action, such as refunding the wrong purchase, can cause irreversible task failure and must be intercepted before execution. Such failures may not appear in every single run, but can emerge across repeated trials, making reliability across steps and trials critical. However, ensuring agentic reliability is challenging: even frontier LLMs struggle t...
  </details>

- **2026-08-30** — Dong Hu, Chao Huang, Carman K. M. Lee et al. — [Self-Aware Active Learning Enables Continual Improvement in Autonomous Driving](http://arxiv.org/abs/2608.29772v1)
  <details><summary>📄 Abstract</summary>
  Learning-based autonomous driving (AD) systems can perform reliably in familiar conditions, yet rare distribution shifts and long-tail events remain a major source of abrupt failure. A central limitation is that most agents learn primarily from passive experience and lack mechanisms to estimate when their competence is insufficient, seek timely assistance, and convert safety-critical encounters into targeted improvement. Here we present self-aware guided exploration (SAGE), an active learning fr...
  </details>

- **2026-08-30** — Guang Gao, Yuxuan Nong, Baifu Huang et al. — [SmoothRL: Online Reinforcement Learning During Asynchronous Execution](http://arxiv.org/abs/2608.29768v1)
  <details><summary>📄 Abstract</summary>
  Deploying robot policies in the physical world requires satisfying two fundamental desiderata: reliability and smooth real-time execution. However, deploying state-of-the-art generalist models presents challenges on both fronts. Achieving the precision and robustness required for real-world deployment necessitates sample-efficient online reinforcement learning (RL) to adapt pretrained models. Meanwhile, the increasing scale of robot foundation models has led to higher inference latency. To satis...
  </details>

- **2026-08-30** — Prokhor Shlyakhtun, Alexander Gryzlov, Vladimir Kukharenko et al. — [Agent-Driven Verification of Memory Safety for liblzma Decoder Components with VST](http://arxiv.org/abs/2608.29716v1)
  <details><summary>📄 Abstract</summary>
  We report on the verification of memory safety for decoder components of liblzma, the compression library underlying xz-utils: the LZMA2 state machine, the LZMA1 decoder it controls, the outer decoding path, and the shared sliding-window dictionary. Built with the Verified Software Toolchain (VST), machine-checked body theorems establish memory safety and partial functional correctness. Across 27 completed body proofs, the largest covers lzma decode, whose 338 source lines expand to 1,934 lines ...
  </details>

- **2026-08-30** — Zhiyu Chen, Keyu Zhao, Jigao Fu et al. — [Ideation Arena: Evaluating LLM Generated Research Ideas with Battle-style Human Expert Assessment](http://arxiv.org/abs/2608.29696v1)
  <details><summary>📄 Abstract</summary>
  Evaluating research ideas generated by LLMs is difficult because their scientific value cannot be fully determined by objective criteria, and no single reference answer specifies what counts as a good idea. To address this challenge, we introduce Ideation Arena, a battle style platform that evaluates research ideas through pairwise human assessment. Ideation Arena evaluates ideas generated by 14 frontier LLMs and 5 research agent architectures built on 2 base models. To ensure a common starting ...
  </details>


### 📂 watermark
*水印与溯源 / Watermarking & Provenance* — 15 papers

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

- **2026-08-31** — Can Zhang, Baofeng Zhang, Xiaotian Han et al. — [From Intent to Evidence: Policy-Steered Multi-Strategy Retrieval for Long-Video Agents](http://arxiv.org/abs/2608.31005v1)
  <details><summary>📄 Abstract</summary>
  Existing long-video agents acquire evidence through one uniform behavior, ignoring whether the required evidence is concentrated, requires broad occurrence coverage, or must discriminate competing hypotheses---which can cause failure before substantive reasoning begins. Prescribing a fine-grained solution procedure for every question is not a satisfactory remedy, as it restricts autonomous exploration. We propose VESTA, a training-free long-video agent organized as a route-conditioned acquire--v...
  </details>

- **2026-08-31** — Alireza Bayat Makou, Emirhan Böge, Phu Gia Hoang et al. — [MURANO: Design, Run, and Reproduce Mechanistic Interpretability Experiments as Composable Pipelines](http://arxiv.org/abs/2608.30662v1)
  <details><summary>📄 Abstract</summary>
  This paper presents Murano, an open source framework for designing, running, and reproducing mechanistic interpretability studies of large language models, intended for researchers across disciplines. These studies often combine loading, recording, attribution, intervention, and evaluation, while existing libraries tend to focus on different parts of this workflow. As a result, researchers using several libraries may need to adapt outputs from one for use by another. To bridge this gap, Murano r...
  </details>

- **2026-08-31** — Keno Moenck, Thorsten Schüppstuhl — [AQ3D: Adaptive Query Transformer for 3D Instance Segmentation](http://arxiv.org/abs/2608.30618v1)
  <details><summary>📄 Abstract</summary>
  Transformer-based decoders for 3D instance segmentation typically commit to a fixed number of queries and positional modeling calibrated on the training distribution rather than on the scene at hand. Indoor scans vary widely in spatial extent and object count, so a fixed query set over-initializes small scenes and under-initializes large ones, while learned absolute and relative encodings are bound to the training scenes' extents and can saturate. We present AQ3D, which is designed to handle sce...
  </details>

- **2026-08-31** — Gissu Valentina Naghavi, Dominik Hagmann, Martin Kampel et al. — [OCR-Based Field Extraction for Archaeological Pottery Metadata: The CENTURIA Dataset](http://arxiv.org/abs/2608.30616v1)
  <details><summary>📄 Abstract</summary>
  Pottery is a primary source for reconstructing the chronological and economic dimensions of past societies. Archaeologists often document ceramic finds through technical drawings and handwritten metadata. This metadata is critical for dating, provenance attribution, and cross-site comparison, but remains inaccessible to computational analysis, requiring manual transcription of every record. We investigate whether state-of-the-art document analysis models can address this task, and introduce CENT...
  </details>

- **2026-08-31** — Negin Sadat Babaiha, Stefan Geissler, Marie-Christine Simon et al. — [Quantitative Evidence Mining for Plausibility-Aware Biomedical AI](http://arxiv.org/abs/2608.30393v1)
  <details><summary>📄 Abstract</summary>
  Biomedical artificial intelligence (AI) systems increasingly extract, organize, and reuse scientific claims from literature, clinical trials, and regulatory documents. But automatic extraction alone does not make a claim reliable evidence: a claim becomes useful only when it can be traced to its source, linked to the quantitative details that support it, and read within its biomedical context and uncertainty. This matters as large language models (LLMs) and increasingly autonomous systems drive ...
  </details>

- **2026-08-31** — Yanan Cao, Anay Dombe, Murali Mohana Krishna Dandu et al. — [Beyond Ranking Accuracy: Evaluating LLM-Cited Feature Rationales for Next Basket Repurchase Recommendation](http://arxiv.org/abs/2608.30333v1)
  <details><summary>📄 Abstract</summary>
  Next-basket repurchase recommendation is commonly formulated as a ranking task: given a customer's purchase history, the system ranks previously purchased items that may be needed again. In production settings, however, ranking accuracy is only one component of recommendation quality. Customers may also benefit from concise evidence about why an item is recommended now. Large language models (LLMs) offer a potential way to surface such evidence through feature-based, human-readable rationales gr...
  </details>

- **2026-08-31** — Hanlin Tian, Minhao Li, Yu Mi et al. — [Ignorance or Incompetence? Constructing Knowledge-Gated, Verifiable Tasks for LLM Agents](http://arxiv.org/abs/2608.30322v1)
  <details><summary>📄 Abstract</summary>
  Professional agent tasks often depend on conventions that are absent from public corpora, yet benchmarks rarely control whether an agent has access to those conventions. We introduce a knowledge-gated task-construction protocol that separates a task instruction from a compact artefact containing private conventions, reference tables, and utility operators. Construction-time provenance, byte-identical task instructions across the provided- and withheld-artefact conditions, leak audits, and execut...
  </details>

- **2026-08-30** — Nora Girda, Adrian Groza — [Review Before Trust: Source-Grounded Integrity Gates for AI-Assisted Personal Health Records](http://arxiv.org/abs/2608.29965v1)
  <details><summary>📄 Abstract</summary>
  Large language models can convert medical documents into structured data, but plausible output may still be unsupported by the source. Persisting such output in a longitudinal health record, a record that accumulates patient information over time, therefore creates an integrity risk: unverified data may influence later summaries, trends, or preventive-care computations. We introduce an evidence-gated trust-promotion model that keeps generated data provisional until a deterministic monitor verifi...
  </details>

- **2026-08-30** — Ridam Roy, Md Shahriar Rashid, Md. Rajib Mia — [Source-Dependent Deference in Medical Imaging Agents Under Falsified Findings: A Pilot Audit](http://arxiv.org/abs/2608.29800v1)
  <details><summary>📄 Abstract</summary>
  Tool-using agents are being proposed for medical imaging, and their behaviour when a tool returns a false finding is largely unmeasured. We audit whether a ReAct-style tool-calling agent abandons an answer it has already given correctly once a falsified finding arrives, and whether that depends on how the finding is presented. On 20 VQA-RAD closed questions across four vendor-designated model tiers, the agent commits to an answer from the image alone; a negated finding is then delivered either a...
  </details>


### 📂 survey
*综述与系统化 / Surveys & Systematization* — 11 papers

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

- **2026-08-31** — Dennis Gross, Helge Spieker — [Automated Testing of LLM-Based Post Hoc Explainers Using Model Checking as an Oracle](http://arxiv.org/abs/2608.30581v1)
  <details><summary>📄 Abstract</summary>
  Large language models (LLMs) are used as post hoc explainers of sequential decision-making policies, producing natural-language explanations of why an action was chosen. However, LLMs often generate plausible but incorrect statements, and no existing approach systematically tests whether such explanations are faithful to the underlying environment. Two classic software testing challenges stand in the way: there is no oracle for the correctness of an explanation, and the test inputs, natural lang...
  </details>

- **2026-08-31** — Jianhao Lin, Lexuan Sun, Yixin Yan — [Tariff Threats, Macroeconomic Expectations, and Policy Communication Strategies: Experiments Based on a Multi-Agent System](http://arxiv.org/abs/2608.30522v1)
  <details><summary>📄 Abstract</summary>
  Tariff threats can move household beliefs before policy is enacted, yet their rapidly changing language is difficult to study with conventional surveys. We build a multi-agent system that turns 300 households from the Michigan Surveys of Consumers into persistent large-language-model agents exposed to social-media information over several simulated months. Calibrated agents reproduce some distributional and demographic patterns in human survey data collected after the announcement of Liberation ...
  </details>

- **2026-08-31** — Peter Lippmann, Fred A. Hamprecht — [Rotational Equivariance in Machine Learning: A Comprehensive Tutorial](http://arxiv.org/abs/2608.31045v1)
  <details><summary>📄 Abstract</summary>
  Rotational symmetry is one of the most important structural principles in machine learning on 3D data. In applications ranging from physics and materials science to 3D computer vision, predictions should not depend on an arbitrary choice of coordinate frame. Rotational equivariance captures this requirement mathematically by enforcing that a rotation of the input induces a corresponding transformation of the model output. This tutorial provides a comprehensive introduction to rotational equivari...
  </details>

- **2026-08-31** — Masahiro Yoshida, Atsuya Kobayashi, Kei Tateno et al. — [Towards Cognitive Process-Aware Proactive Writing Support](http://arxiv.org/abs/2608.30424v1)
  <details><summary>📄 Abstract</summary>
  Large language models can support writing, but existing tools require users to explicitly articulate prompts-particularly burdensome in creative writing, where intentions are often ambiguous. Proactive support that infers users' needs from writing interactions could alleviate this burden, but raises two challenges: determining what support to provide and when to intervene. This work focuses on the former. We hypothesize that Flower and Hayes' cognitive process theory of writing-which characteriz...
  </details>

- **2026-08-31** — Tongfei Guo, Lili Su — [Rethinking Language's Role in Efficient VLA for Autonomous Vehicles: Toward Smarter, Trustworthy Driving](http://arxiv.org/abs/2608.30144v1)
  <details><summary>📄 Abstract</summary>
  Vision-Language-Action (VLA) models are reshaping autonomous driving (AD) by unifying perception, reasoning, and control through language, enabling semantic grounding, interpretable decisions, and better long-tail generalization. But language is expensive onboard: latency and memory budgets are tight, and autoregressive decoding is inherently sequential. This work reframes the central question as when and where language should act at inference, since inference cost recurs at every deployed frame...
  </details>


### 📂 other
*其他安全相关 / Other Security-Related* — 141 papers

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

- **2026-08-31** — Ziyi Bai, Siqi Li, Tinglei Huang et al. — [PRACTICE: From Experience to Expertise in Self-Evolving Embodied Agents](http://arxiv.org/abs/2608.30760v1)
  <details><summary>📄 Abstract</summary>
  Recent studies have shown that multimodal large language models (MLLMs) can serve as embodied agents, translating language instructions and visual observations into executable plans. However, building agents that can continually improve through interaction and rapidly adapt to their environments remains challenging. Summing up experience from past interaction trajectories provides a promising solution, but existing experience-based methods often rely on manually designed prompting workflows to e...
  </details>

- **2026-08-31** — Kieran Murphy — [Tracing distinguishability through transformer processing with stochastic LayerNorm](http://arxiv.org/abs/2608.30720v1)
  <details><summary>📄 Abstract</summary>
  Representational similarity is foundational to analyses of deep networks, yet distances between point-valued representations are not intrinsically tied to downstream function: nearby states may produce different behaviors, while distant states may behave similarly. We instead give representations volume, turning similarity into statistical distinguishability. Overlapping stochastic representations necessarily induce overlapping downstream distributions, grounding latent comparison in model funct...
  </details>

- **2026-08-31** — Wei Chen, Peilun Zhou, Zhaoyu Hu et al. — [ATLAS: Dual-Horizon Diagnostic Evaluation for Industrial Tool-Use Agents](http://arxiv.org/abs/2608.30685v1)
  <details><summary>📄 Abstract</summary>
  Large language model (LLM) agents are increasingly deployed in user-facing services that require iterative tool use under dynamic business conditions. Reliable evaluation is essential for sustained improvement: it must reveal capability deficiencies, inform priorities, and assess interventions. Yet industrial agent service unfolds both through the iterative trajectory of a current request and through continued user interaction. Final-outcome assessment can therefore obscure where deficiencies ar...
  </details>

- **2026-08-31** — Wenxuan Guo, Yuyang Hong, Lubin Fan et al. — [DiffPDE: Masked Diffusion Language Models as PDE Solver](http://arxiv.org/abs/2608.30532v1)
  <details><summary>📄 Abstract</summary>
  Existing approaches for synthesizing Partial Differential Equation (PDE) solvers predominantly rely on autoregressive models, yet their global left-to-right decoding incurs substantial redundancy when addressing inherently localized bugs. In this work, we challenge this inefficient paradigm and propose DiffPDE, a framework leveraging discrete diffusion language models for targeted code repair. By introducing a localized re-masking and infilling strategy, DiffPDE regenerates only erroneous region...
  </details>

- **2026-08-31** — Minju Song, Hyeon Hwang, Junhyun Lee et al. — [Enhancing Low-Resource Language Reasoning via High-Resource Language Feature Transfer](http://arxiv.org/abs/2608.30462v1)
  <details><summary>📄 Abstract</summary>
  Large language models exhibit substantial performance variation across languages, even when solving semantically equivalent tasks. Existing analyses often treat this phenomenon as an observational disparity caused by differences in pretraining data, tokenization, or benchmark coverage. We study a complementary hypothesis: high-resource languages (HRLs) may more reliably elicit latent computations useful for task-specific (i.e. mathematical) reasoning, while lower-resource languages (LRLs) may un...
  </details>

- **2026-08-31** — Tiffanie Godelaine, Maxime Zanella, Karim El Khoury et al. — [Whole-Slide Image Analysis under Realistic Few-Shot Annotation Protocols](http://arxiv.org/abs/2608.30420v1)
  <details><summary>📄 Abstract</summary>
  Automating the analysis of whole-slide images has high clinical value, since characterizing cancers requires examining them in detail. Such analysis increasingly relies on vision-language models that provide patch-level zero-shot predictions. However, these predictions remain noisy and must be refined with a few annotations. A promising paradigm for this refinement is few-shot transduction. Rather than treating each patch independently, these methods leverage the relations between patches, toget...
  </details>

- **2026-08-31** — Jayanta Sadhu, Sayem Shahad, Kenneth Marino — [DERELAB: Probing Defeasible Reasoning and Confirmation Bias in LLMs with a Generative Benchmark](http://arxiv.org/abs/2608.30413v1)
  <details><summary>📄 Abstract</summary>
  Defeasible reasoning is a type of reasoning where inferences are drawn from plausible current evidence, but can be retracted upon the introduction of newer evidence. Although recent studies have examined language-model behaviors in defeasible reasoning, the datasets have been static and lack wide coverage of non-monotonic reasoning categories. We introduce DeReLab, a generative framework that produces multi-turn belief-updating conversations from parameterized graph structures across default and...
  </details>

- **2026-08-31** — Ahmed Sameh, Nolan Wilson, Max Enderlein et al. — [Beat-Synchronous Tokenization for ECG Transformers](http://arxiv.org/abs/2608.30367v1)
  <details><summary>📄 Abstract</summary>
  Transformer-based electrocardiogram (ECG) models commonly tokenize waveforms into fixed temporal patches. Though convenient, fixed patching can split heartbeat structures across token boundaries. We study beat-synchronous tokenization as a physiologically grounded alternative, comparing fixed patches with three beat-aligned strategies: resampled beats, adaptive pooled beats, and resampled beats augmented with R--R interval information. Experiments span two settings: 10-second 12-lead diagnostic ...
  </details>

- **2026-08-31** — Ziheng "Leo" Li, Benjamin Freeman, Akshay Raman et al. — [Co-Annotator: Expert-Distilled ViT and VLM for Visual and Documentation Guidance in Age-Related Macular Degeneration](http://arxiv.org/abs/2608.30352v1)
  <details><summary>📄 Abstract</summary>
  Clinical AI often optimizes predictive performance without engaging how clinicians decide where to look and what to write. We present Co-Annotator, which distills expert gaze and dictation into two guidance components: a gaze-aligned Vision Transformer producing fixation-aligned areas of interest (AOIs), and an ontology-bounded vision-language model (VLM) that pre-fills editable biomarker summaries for retinal optical coherence tomography (OCT). We first collect expert gaze and dictations (US1) ...
  </details>

- **2026-08-31** — Yan Zhou, Yun Hong, Yang Feng — [Sequential Trajectories and Simultaneous Blending: Multi-Emotion Modeling for Instruction-Following TTS](http://arxiv.org/abs/2608.30325v1)
  <details><summary>📄 Abstract</summary>
  Natural-language instructions enable flexible control of synthesized speech, yet emotional TTS systems primarily model a single utterance-level affect, leaving multi-emotion control underexplored. We study two complementary multi-emotion TTS tasks: emotion trajectory, which spans several ordered affective stages, and emotion blending, in which multiple emotions coexist throughout an utterance. These tasks expose a supervision mismatch: supervised fine-tuning (SFT) does not explicitly evaluate em...
  </details>

- **2026-08-31** — Junjie Yao, Liangkai Hang, Zhi-Qin John Xu — [Context Staircase: Signature-Aligned Dynamics of Token Embeddings under Small Initialization](http://arxiv.org/abs/2608.30315v1)
  <details><summary>📄 Abstract</summary>
  Token embeddings are the basic representational units that connect discrete tokens with continuous computation in language models. Although modern language models learn embeddings from random initialization through gradient-based training, the dynamical mechanism by which meaningful embedding structures emerge remains unclear. In this work, we identify that the evolving embedding structures are closely related to token-conditioned label and contextual distributions, which we formalize as probabi...
  </details>

- **2026-08-31** — Xiaodong Liu, Siman Wang, Congfei Zhang et al. — [CAMIE: Co-Engagement-Aware Multimodal Item Embeddings for Snap Dynamic Product Ads Retrieval](http://arxiv.org/abs/2608.30255v1)
  <details><summary>📄 Abstract</summary>
  Item-to-item (I2I) retrieval is a core primitive in large-scale recommendation and advertising systems. In production Snap Dynamic Product Ads (DPA), I2I retrieval faces two challenges: separate visual, textual, and multimodal encoders fragment the retrieval stack, and content-only training does not align embeddings with the co-engagement behavior that drives downstream conversions. We present CAMIE, a co-engagement-aware multimodal item embedding framework for Snap DPA retrieval. CAMIE builds o...
  </details>

- **2026-08-31** — Dong-Wook Kim, Ji-Hoon Hwang, E-In Son et al. — [CanonNav: Disentangling Navigation Behavior from Camera Geometry in Cross-Platform Visual Navigation](http://arxiv.org/abs/2608.30242v1)
  <details><summary>📄 Abstract</summary>
  While visual navigation has advanced through imitation learning from cross-platform demonstrations, fully leveraging such data remains challenging. First, directly learning from image-trajectory pairs entangles navigation behavior with platform-dependent camera geometry. This hinders consistent learning by forcing the policy to implicitly infer camera geometry from visual observations, an inherently ill-posed problem. Second, imitation learning from demonstrated trajectories captures the expert'...
  </details>

- **2026-08-31** — Zijun Gao, Weihan Zhang — [Cubic-Root Gaussian Approximation under Unrestricted Covariance](http://arxiv.org/abs/2608.30221v1)
  <details><summary>📄 Abstract</summary>
  For Gaussian approximation over high-dimensional rectangles under unrestricted covariance, Chernozhukov et al. (2023b) conjectured that the $n^{-1/4}$ rate, up to logarithmic factors, is near-optimal. We show that, under the coordinatewise subexponential condition with scale $B_n$ and the marginal variance lower bound condition with constant $b$ in Chernozhukov et al. (2023b), the approximation error in dimension $d$ is bounded by \begin{align*} C_b\min\left\{ 1,\, \left(\frac{B_n^2}{n}\right)^{...
  </details>

- **2026-08-31** — Jiaxin Tian, Darren An, Jun Li — [Benchmarking Peptide-Protein Affinity Prediction Across Peptide and Target Shifts](http://arxiv.org/abs/2608.30175v1)
  <details><summary>📄 Abstract</summary>
  Peptide-protein affinity models are often evaluated with a single data split, obscuring whether they interpolate among measurements for observed targets or generalize across peptide or target shifts. We integrated three sources of quantitative peptide-protein binding data to obtain 11,349 deduplicated pairs and benchmarked ten peptide representations, ESM-2 protein embeddings, and six regressors under peptide-similarity, within-target, and leave-target-out partitions. Across 60 matched represent...
  </details>

- **2026-08-31** — Tianyu Gao, Zhikai Su, Jiashu Li et al. — [Language-Informed Flow Matching for Trend-Guided Structure-Based 3D Molecular Generation](http://arxiv.org/abs/2608.31009v1)
  <details><summary>📄 Abstract</summary>
  Structure-based drug design (SBDD) requires ligands that satisfy both 3D target affinity and 1D chemical validity. Existing controllable generation methods often rely on task-specific fine-tuning or externally imposed sampling-time guidance, adding cost and potentially conflicting with evolving 3D geometric constraints. We propose LiFT, a language-informed cross-modal framework built on Flow Matching for trend-guided 3D molecular generation across both de novo design and scaffold hopping. LiFT u...
  </details>

- **2026-08-31** — Atta Ul Asad, Ahsan Bilal, Muhammad Ali et al. — [Faithfulness Is Not Free: Auditing Offline KV-Cache Quantization in Retrieval-Augmented Generation](http://arxiv.org/abs/2608.30996v1)
  <details><summary>📄 Abstract</summary>
  Retrieval-augmented generation systems can precompute and store key-value caches of retrieved documents to avoid re-encoding context at every query. Quantizing these caches further reduces storage, but no prior work asks whether compression damages faithfulness, whether responses remain grounded in the retrieved evidence. Faithfulness and accuracy are not equivalent: a model can produce a correct answer that is no longer supported by the context it was given. We evaluate Qwen2.5-7B-Instruct unde...
  </details>

- **2026-08-31** — Émiland Garrabé, Mahdi Khoramshahi, Stéphane Doncieux — [Autonomously Acquiring Robot Manipulation Skills with Language-Driven Quality-Diversity](http://arxiv.org/abs/2608.30983v1)
  <details><summary>📄 Abstract</summary>
  Quality-diversity (QD) algorithms have been gaining traction in robot learning, where diverse motion primitive libraries allow robots to adapt zero-shot to constraints at deployment time. However, such methods typically require expert designers to write the success condition, fitness and diversity metrics, and this strongly limits the robot's autonomy. On the other hand, existing LLM-based reward-shaping techniques allow robots to learn autonomously but only output single high-performing solutio...
  </details>

- **2026-08-31** — Olivier Serris, Stéphane Doncieux, Olivier Sigaud — [Locally-Guided Actor-Critic: Training a Goal-conditioned Actor with a Subgoal-aware Critic](http://arxiv.org/abs/2608.30406v1)
  <details><summary>📄 Abstract</summary>
  Goal-conditioned reinforcement learning struggles with long horizons when rewards are sparse. While a planner can provide subgoals to guide a low-level policy, its use at test time may introduce practical subgoal management difficulties. An alternative paradigm utilizes a high-level planner to assist learning, while the policy remains conditioned only on the final goal, enabling planner-free deployment. Among these methods, Reinforcement Learning with Imagined Subgoals (RIS) introduces a regular...
  </details>

- **2026-08-31** — Natalie B. Hogg — [Agentic research is oxymoronic](http://arxiv.org/abs/2608.31161v1)
  <details><summary>📄 Abstract</summary>
  The use of agentic large language models obviates human interpretation of scientific results, and will lead to substantial distrust in the literature.
  </details>

- **2026-08-31** — Benjamin Cookson, Nisarg Shah — [Constrained Fair Allocations via Partition Matroid Reductions](http://arxiv.org/abs/2608.31121v1)
  <details><summary>📄 Abstract</summary>
  We study fair allocation of indivisible goods under additive valuations and matroid constraints. A challenging open question is whether a complete and feasible envy-free up to one good (EF1) allocation exists under every matroid that admits a complete and feasible allocation. The state-of-the-art result by Biswas and Barman [2018] positively resolves this question for partition matroids.   Our first result positively resolves it for laminar matroids, which generalize partition matroids, when the...
  </details>

- **2026-08-31** — Pradyumn Goyal, Yizhak Ben-Shabat, Hsueh-Ti Derek Liu et al. — [BLARM: Animating 3D Objects from Video via Blending Latent Rigid Motion Primitives](http://arxiv.org/abs/2608.31113v1)
  <details><summary>📄 Abstract</summary>
  We introduce BLARM, a feed-forward method for video-driven 3D mesh animation. Given a monocular video and a static object mesh, BLARM predicts a temporally coherent animated mesh whose motion follows the video. Rather than relying on explicit rigs or directly regressing high-dimensional vertex motion, we represent animation using a compact set of learned, time-varying rigid motion components and time-invariant vertex-to-component skinning weights. This yields a low-dimensional deformation space ...
  </details>

- **2026-08-31** — Yuhao Wu, Jingyuan Zhang, Jiajun Shi et al. — [Aspire: Can Models Self-Evolve from Vague Goals?](http://arxiv.org/abs/2608.31111v1)
  <details><summary>📄 Abstract</summary>
  Many important forms of human learning begin with a vague goal, such as "become a better physicist" or "improve at research." Learners must interpret the goal, identify capability gaps, decide how to learn, and determine whether they have actually improved. In contrast, existing work on LLM self-evolution typically begins with tasks and evaluation metrics specified by humans, reducing self-evolution to optimizing an explicit objective rather than deciding what and how to learn. We introduce ASPI...
  </details>

- **2026-08-31** — Lucas Wojcik, Gabriel E. Lima, Sergio M. Silva et al. — [VeriCam: A Verification Baseline for the Classification of Unknown Data](http://arxiv.org/abs/2608.31107v1)
  <details><summary>📄 Abstract</summary>
  The advent of foundation models have enabled a new era in zero-shot classification. Yet, key challenges persist. Despite their impressive generalization power that leverages the immense pre-training knowledge, both foundation models for image and text as well as vision-text hybrids lack the representational power needed for fine-grained, minutiae-based class separation that some real-world tasks require. To address the current gaps in the literature, we propose VeriCam, a pipeline designed to le...
  </details>

- **2026-08-31** — Xijie Gong, Tonghan Wang — [The First Token Is a Clue: Verbalizing Multi-Token Concepts from the J-lens](http://arxiv.org/abs/2608.31084v1)
  <details><summary>📄 Abstract</summary>
  The Jacobian Lens (J-lens) is a recent tool for interpreting LLMs. It reads a hidden state as a ranked list of vocabulary tokens, leaving multi-token concepts without a representation of their own. The original J-lens work addresses this limitation with Template Lens, which precomputes vectors for a fixed phrase vocabulary, and Oracle Lens, which fine-tunes components to propose phrases and reconstruct phrase vectors. We ask whether multi-token concepts and their vectors can instead be recovered...
  </details>

- **2026-08-31** — Qiyao Yan, Chenpeng Wang, Liangming Pan — [Wrong Prediction, Right Answer: Recovering Evidence from Collapsed LLM Sequence Scores](http://arxiv.org/abs/2608.31068v1)
  <details><summary>📄 Abstract</summary>
  When a large language model fails a reasoning task, it is often assumed to lack the underlying capability. However, this conflates a genuine absence of reasoning with a late-stage output bottleneck. We observe a consistent readout gap across diverse reasoning benchmarks: hidden-state probes successfully decode correct answers even when native sequence scoring completely collapses due to structural biases. To test whether instance-specific logic survives this collapse, we introduce a diagnostic p...
  </details>

- **2026-08-31** — Takuya Ito, Ruchir Puri, Murray Campbell et al. — [Universal Transformers for Circuit Computations: Perfect Length Generalization in Tiny Transformers](http://arxiv.org/abs/2608.31067v1)
  <details><summary>📄 Abstract</summary>
  Learning generalizable algorithmic computations remains a challenge for neural networks, as reflected in persistent failures on compositional and length generalization benchmarks. We present a provably correct, transformer parameterization (with only 280 learnable parameters for Boolean algebra tasks) capable of learning and evaluating problems of any depth or length. We assume inputs are fully parenthesized, well-formed expressions. Our approach conceptualizes algorithmic tasks as circuit model...
  </details>

- **2026-08-31** — Simon Freyaldenhoven — [When Can We Work in Embedding Space? What Text Embeddings Preserve](http://arxiv.org/abs/2608.31059v1)
  <details><summary>📄 Abstract</summary>
  When do text embeddings work as inputs to empirical analysis? Their use rests on an assumption: that we can trade text for its low-dimensional embedding, and lose little in doing so. I make that assumption precise under a generative model in which documents are mixtures of latent topics. I study two uses---clustering units in embedding space and controlling for high-dimensional text. A cluster of embeddings is a set of documents with similar topic mixtures; controlling for the embedding is equiv...
  </details>

- **2026-08-31** — Orkun Yiğit Cengiz — [Annotated Surrogate Retrieval for Polish Statutory Law](http://arxiv.org/abs/2608.30929v1)
  <details><summary>📄 Abstract</summary>
  We present a family of retrieval methods for Polish statutory law built on document surrogates: language-model annotations attached to statutory articles at index time. Three designs occupy different points on the cost-quality frontier. ASCR is a surrogate cascade with reranking; ASCR-H fuses a dense list into that cascade; and DTF replaces both language-model stages with three lexical and dense retrievers, weighted reciprocal rank fusion, and a deterministic re-scoring prior, using no model cal...
  </details>

- **2026-08-31** — Xuanle Zhao, Xinyuan Cai, Xiang Cheng et al. — [S3C-LLM: Skill-Code Guided Agentic Language Models for Spectrum-to-Structure Elucidation](http://arxiv.org/abs/2608.30910v1)
  <details><summary>📄 Abstract</summary>
  Spectroscopic structure elucidation is central to molecular analysis, but recent Large Language Model (LLM)-based methods mostly formulate it as direct spectrum-to-SMILES generation. Although this paradigm can leverage paired spectral data, it does not explicitly model the analytical workflow used by spectroscopists, such as diagnostic peak interpretation, fragment reasoning, formula constraints, and chemical consistency checking. In this paper, we introduce S3C-LLM, a skill-guided and code-grou...
  </details>

- **2026-08-31** — Mohammadsina Hassannia, Matthew A. Reyna, Reza Sameni — [ECGQuest: Benchmarking and Fine-Tuning Language Models for Electrocardiography](http://arxiv.org/abs/2608.30893v1)
  <details><summary>📄 Abstract</summary>
  Electrocardiogram (ECG) interpretation requires knowledge of cardiology, electrophysiology, clinical diagnosis, ECG waveforms, signal acquisition, and instrumentation. Existing language-model benchmarks, however, primarily assess broad medical knowledge or interpretation of individual ECG signals and images rather than the broader contextual knowledge required for ECG interpretation. We developed ECGQuest, a literature-grounded resource for evaluating and fine-tuning ECG-specific language models...
  </details>

- **2026-08-31** — Melina Morch, Daniel Braun — [Evaluating and Mitigating Anti-LGBTQ Biases in German and Multilingual Language Models](http://arxiv.org/abs/2608.30884v1)
  <details><summary>📄 Abstract</summary>
  While gender and racial biases in language models have been widely studied, anti-LGBTQ biases remain underexplored, particularly beyond English. Existing benchmarks often do not capture cultural and linguistic variation and rely on gender representations. This paper introduces a multilingual German-English benchmark dataset for the evaluation of anti-LGBTQ biases in language models. It combines community-sourced stereotypes from German-speaking queer individuals with a German translation of Wino...
  </details>

- **2026-08-31** — Laura Daza, Marta Hasny, Cristina González et al. — [Whole-Body MRI Classification via Prompt-Based Clinical Conditioning](http://arxiv.org/abs/2608.30824v1)
  <details><summary>📄 Abstract</summary>
  Combining whole-body magnetic resonance imaging (WB-MRI) with clinical variables has the potential to improve systemic disease diagnosis by leveraging complementary sources of patient information. However, structured clinical variables are often incomplete or missing, limiting the applicability of conventional multimodal fusion methods that assume fixed inputs. In this work, we propose TACTIC (Tabular-Attribute Conditioned Transformer for Image Classification), a prompt-based multimodal framewor...
  </details>

- **2026-08-31** — Max A. Alekseyev, Joseph T. Iosue, Adam Ehrenberg et al. — [Cycle-Structure Generating Functions for Special Breakpoint Graphs](http://arxiv.org/abs/2608.30764v1)
  <details><summary>📄 Abstract</summary>
  Breakpoint graphs originate in comparative genomics, where their alternating cycles encode relationships between genomes. We study a constrained class of three-colored breakpoint graphs associated with permutations and develop cycle-refined generating functions for two extremal families. These families have a natural topological interpretation: their canonical surfaces are, respectively, the sphere and the projective plane. The spherical family is characterized by noncrossing configurations, whi...
  </details>

- **2026-08-31** — Ashwin Nedungadi, Stefan Oehmcke, Stefan Lüdtke — [Autoregressive Mosaics: Probing 2D Spatial Reasoning in Text-Only Language Models](http://arxiv.org/abs/2608.30751v1)
  <details><summary>📄 Abstract</summary>
  Large language models (LLMs) trained only on text and code can sometimes generate programs that draw recognizable images. However, it is unclear whether this reflects an internal representation of 2D spatial layout or simply the ability to translate spatial descriptions into code. We introduce Autoregressive Mosaics (AM-Bench), a benchmark that separates these factors: First, a translation task gives a model a fully specified geometry of a picture in words as a prompt and asks for the code that ...
  </details>

- **2026-08-31** — Fengji Ma, Yan Rong, Xu Li et al. — [Closing the Verification Loop: Self-Check Captioning for Long-Paragraph Detailed Audio Captioning](http://arxiv.org/abs/2608.30713v1)
  <details><summary>📄 Abstract</summary>
  Long-paragraph detailed audio captioning, which requires dense and transcript-faithful descriptions of fine-grained audio content, remains unsolved for current audio-visual multimodal language models. We attribute this failure to two structural problems. The first is data poverty, as no public corpus jointly provides long clips, paragraph captions, and verbatim-transcript fidelity. The second is generation-mode failure, evidenced by a 44.8 to 46.4 percentage-point gap between right-audio and shu...
  </details>

- **2026-08-31** — Jingyi He, Sanghwan Kim, Zeynep Akata — [VisLens: Single-Pass Interpretable Visual Search for Multimodal LLMs](http://arxiv.org/abs/2608.30705v1)
  <details><summary>📄 Abstract</summary>
  Multimodal large language models (MLLMs) struggle with fine-grained Visual Search, the task of locating small or rare objects in high-resolution images. Existing remedies fall into two families: (1) Training-free methods based on attention or confidence scores are accurate but slow, since they require multiple MLLM queries per example. (2) Reinforcement Learning (RL) trained tool-use models are faster at inference but opaque, since their tool calls remain uncontrollable and hard to interpret. To...
  </details>

- **2026-08-31** — Jeff Lee, Sebastien Jourdain, Cory Quammen et al. — [Domain-Grounded Tool Orchestration for LLM-Guided Scientific Analysis](http://arxiv.org/abs/2608.30696v1)
  <details><summary>📄 Abstract</summary>
  Scientific analysis workflows encode deep domain knowledge through sequences of tightly coupled operations where correctness depends on tool selection, execution order, and parameterization. A CFD engineer investigating flow separation must extract wall shear stress, identify zero-crossings in skin friction, and confirm with boundary-layer profiles: a chain that requires both domain expertise and proficiency with visualization tools. Current approaches to LLM-assisted scientific visualization ge...
  </details>

- **2026-08-31** — Futa Hidaka, Naomi Imasato, Kazuki Miyazawa et al. — [Inferring Value Criteria from Ordinal Preferences: An Iterative In-Context Learning Framework for Music Generation](http://arxiv.org/abs/2608.30694v1)
  <details><summary>📄 Abstract</summary>
  Adapting a generative music system to an individual's taste requires learning what that listener values. Listeners can rank pieces, but their underlying criteria may be tacit and difficult to articulate. We ask whether and under what conditions a large language model (LLM) can adapt symbolic music generation from rankings alone and construct transferable natural-language descriptions of value criteria. In our iterative in-context learning framework, the LLM formulates hypotheses, generates candi...
  </details>

- **2026-08-31** — Danyang Li, John Taylor, Thang Bui et al. — [Season-Aware Hybrid Convolutional-Transformer for Antarctic Sea Ice Concentration Forecasting](http://arxiv.org/abs/2608.30654v1)
  <details><summary>📄 Abstract</summary>
  Antarctic sea ice concentration (SIC) forecasting is an important yet challenging task due to the coexistence of complex spatial structure, long-range temporal dependencies, and strong seasonal variability. Conventional convolution-based models are effective at capturing local spatial patterns, but often have limited ability to model long-term temporal evolution. To address these challenges, we build on a hybrid Convolutional-Transformer forecasting framework for monthly Antarctic SIC forecastin...
  </details>

- **2026-08-31** — Yinwen Lu, Weihao Luo, Yueqi Zhong — [GarmentWeaver: Schema-Aware Structured Synthesis for Multimodal Sewing Patterns](http://arxiv.org/abs/2608.30550v1)
  <details><summary>📄 Abstract</summary>
  Multimodal Sewing pattern generation aims to infer executable sewing patterns from design cues such as sketches and textual descriptions. As an interpretable and simulation-compatible representation, sewing patterns are particularly valuable for digital garment creation. However, existing methods often model garment specifications as flat long sequences, which entangles garment structure with detailed parameters and leads to redundant components, inaccurate local details, and poor simulation com...
  </details>

- **2026-08-31** — Qi Li, Zhaojie Kang, Yingjie He et al. — [CM2: Multimodal Cultural Reasoning via an Integrated Multi-Agent Framework](http://arxiv.org/abs/2608.30498v1)
  <details><summary>📄 Abstract</summary>
  Multimodal Large Language Models (MLLMs) have shown remarkable success in STEM domains, where progress is often driven by vertical, step-by-step deduction under relatively stable symbol systems. Their horizontal, interdisciplinary cultural reasoning, however, remains underexplored.We propose CM2, a multi-agent framework grounded in the cognitive pathway of human cultural interpretation. CM2 integrates multimodal perception, retrieval-augmented generation, networked reasoning, gated fusion, and r...
  </details>

- **2026-08-31** — Haowen Lin, Jing Li, Zhibin Hao et al. — [HF-SID: High-Fidelity Semantic IDs for Generative Retrieval in Location-Based Services](http://arxiv.org/abs/2608.30479v1)
  <details><summary>📄 Abstract</summary>
  Generative retrieval has attracted increasing attention in Location-Based Services (LBS), where each Point-of-Interest (POI) is represented as a Semantic ID (SID). As the SID is the only channel through which POI information reaches the generative model, whatever it fails to preserve is irrecoverable at decoding time, and LBS retrieval is especially sensitive to the fine-grained differences that existing SIDs blur. Specifically, (1) LLMs embed continuous coordinates discontinuously, so their num...
  </details>

- **2026-08-31** — Jiaqi Ding, Chuan Yang, Linghui Meng et al. — [LangBP: Language-Guided Reasoning and Acting for Joint Bidding and Pricing](http://arxiv.org/abs/2608.30343v1)
  <details><summary>📄 Abstract</summary>
  Auto-bidding is a long-horizon sequential decision problem for maximizing conversion value under budget and key performance indicator (KPI) constraints. Recent work extends this task from bidding alone to joint bidding and pricing, where a policy controls bidding decisions and pricing corrections. Existing methods mainly rely on numerical trajectory modeling, which offers limited support for interpreting campaign context and expressing high-level strategies. Large language models (LLMs) can comp...
  </details>

- **2026-08-31** — Raunak Kumar, Anuj Pal, Dhruvi Solanki et al. — [Coarse composition suffices: tabular in-context learning for multi-activity antimicrobial peptide profiling](http://arxiv.org/abs/2608.30337v1)
  <details><summary>📄 Abstract</summary>
  Antimicrobial peptides (AMPs) often act against multiple pathogen classes, making multi-label activity prediction a more realistic screening target than binary antimicrobial classification. The ESCAPE benchmark formalizes this setting, but leading approaches typically rely on multimodal, structure-conditioned deep models that are costly to train and tune. We show that a simple, sequence-only pipeline can match and surpass these methods by combining 330 interpretable sequence descriptors with Tab...
  </details>

- **2026-08-31** — Moniruzzaman Mahadi, Abrar Mohammed Tanzim Alam, Sayma Siddika Monalisa et al. — [Do Small Models Use the Law You Give Them? Measuring Context Use on a Bilingual Bangladesh Legal Benchmark](http://arxiv.org/abs/2608.30327v1)
  <details><summary>📄 Abstract</summary>
  Fine-tuning can improve legal question-answering accuracy without improving how models use law supplied in context. We study this distinction in bilingual Bangladeshi legal QA, where observed errors can arise from answer scoring, retrieval, or failure to use relevant law. We construct a hierarchy-preserving statutory corpus, 2,165 reviewed bilingual fine-tuning examples, and a 150-item supplied-law control. We evaluate six instruction-tuned models: Llama-3.2-1B, Llama-3.2-3B, Qwen3.5-0.8B, Qwen3...
  </details>

- **2026-08-31** — Qinghua Qin — [The Exact MMS Guarantees of EFX and PMMS](http://arxiv.org/abs/2608.30267v1)
  <details><summary>📄 Abstract</summary>
  Envy-freeness up to any good (EFX) and pairwise maximin share (PMMS) are standard local fairness criteria for indivisible goods, whereas maximin share (MMS) is a global benchmark. We determine the exact quantitative relationship between these local fairness notions and the global MMS guarantee under nonnegative additive valuations. We show that the optimal universal factor for both notions is $ρ^{\mathrm{EFX}\to\mathrm{MMS}}=ρ^{\mathrm{PMMS}\to\mathrm{MMS}}=\frac{10}{17}$. We prove the lower bou...
  </details>

- **2026-08-31** — Qinghua Qin — [Residual Maximin Share: Exact Finite-Agent Frontier, Sparse Extremizers, and Threshold Cuts](http://arxiv.org/abs/2608.30257v1)
  <details><summary>📄 Abstract</summary>
  Residual maximin share (RMMS) is the largest share threshold that remains guaranteeable throughout dynamic allocation processes, even after previously allocated, lower-valued bundles are removed from the item pool. For additive valuations, recent density-balance analyses established finite-agent lower bounds comparing RMMS with the classical maximin share (MMS). In this paper, we prove that these finite-agent lower bounds are exact. Specifically, if $d_n$ denotes the largest odd integer at most ...
  </details>

- **2026-08-31** — Anand Iyer, Bhanu Khetharpal, Srinivas Upadhya et al. — [Generating Workflow DAGs from Natural Language with Non-Reasoning LLMs](http://arxiv.org/abs/2608.30250v1)
  <details><summary>📄 Abstract</summary>
  This paper addresses the problem of translating natural-language routing rules written by business administrators into executable workflow graphs for enterprise contact centers. Each target is a directed acyclic graph (DAG) of conditional actions with parallel branches, hit-first fallback chains, and per-branch Boolean predicates, encoded in the JSON dialect of a commercial routing platform. We show that neuro-symbolic decomposition enables lower-cost, non-reasoning large language models to gene...
  </details>

- **2026-08-31** — Dianjing Cheng, Yike Li, Lan Yang et al. — [Open-Source Autonomous Driving System Analysis and Multi-Disciplinary Hardware-in-the-Loop Research Paradigm with Reinforcement-Learning Testing and Large Language Models](http://arxiv.org/abs/2608.30179v1)
  <details><summary>📄 Abstract</summary>
  Open-source autonomous driving systems provide an inspectable software foundation for intelligent vehicle research. Under real-vehicle deployment conditions, the recording and review of experimental conditions are important for interpreting system behavior and reusing experimental results. However, in a shared real-vehicle environment involving multiple vehicles, task processes, code modifications, and hardware testing feedback are often distributed across different teams and experimental stages...
  </details>

- **2026-08-30** — Lifei Liu, Haoran Yu, Xiaochong Jiang — [VERA: Authority-Preserving Edge Revocation for Federated AI-Agent Workflows](http://arxiv.org/abs/2608.30091v1)
  <details><summary>📄 Abstract</summary>
  Modern agent frameworks compose planners, tool agents, remote services, and shared specialists into runtime delegation graphs, but their revocation APIs still resemble token or subtree invalidation. When one delegation is withdrawn, the runtime must know which agents lose authority while independently authorized agents keep working. We study this authority consistency problem and introduce VERA (Verifiable Edge Revocation for Agents), a verifier-checkable revocation contract and API emitted by a...
  </details>

- **2026-08-30** — Haoran Yang, Zhixuan Zhong, Jiawei Guo et al. — [POLYFLOW: A Neuro-Symbolic Framework for Static Cross-Language Information Flow Analysis](http://arxiv.org/abs/2608.29808v1)
  <details><summary>📄 Abstract</summary>
  Modern software systems are commonly constructed in multiple, interacting programming languages. This construction leads to additional, often stealthy vulnerabilities buried in complex information flow due to language interactions. Existing static analyzers are impeded by the heterogeneous semantics of different languages, whereas dynamic approaches suffer from the limited coverage of (available and/or generated) test inputs. In this paper, we develop PolyFlow, a neural-symbolic framework for st...
  </details>

- **2026-08-30** — Qian Chen, Shiliang Xiao, Yuzhi Liang — [OASIS: Optimizing Attacker Sequences for Hard-Label Black-Box Text Attacks](http://arxiv.org/abs/2608.29568v1)
  <details><summary>📄 Abstract</summary>
  Different attack methods follow different search trajectories, they succeed on different subsets of samples, whereas existing hard-label black-box text attacks mainly focus on improving individual attackers or manually combining them. We present {\OURS}, a method for optimizing attacker sequences in hard-label black-box text attacks. {\OURS} first performs a one-time bi-objective attack chain search over candidate sequences to balance attack success rate and perturbation, and then reuses the sel...
  </details>

- **2026-08-30** — Abdul Qadir Ibrahim, Martin Burger — [Selection, Representation, and Execution in Sparse Fourier Neural Operators](http://arxiv.org/abs/2608.30070v1)
  <details><summary>📄 Abstract</summary>
  Sparse representations are often expected to make models smaller and also reduce inference cost. For Fourier Neural Operators (FNOs), these objectives are not equivalent or do not always align: removing parts of the learned operator can leave the underlying transforms and dense computations unchanged, while changing the grid on which the model is evaluated can introduce overhead of its own. We therefore distinguish sparsity in the representation, in the stored parameters, in the theoretical oper...
  </details>

- **2026-08-30** — Aditi Sarker, Rafi Ibn Sultan, Hui Zhu et al. — [Hallucination Mitigation for Large Vision-Language Models via Implicit Feature Stabilization](http://arxiv.org/abs/2608.29924v1)
  <details><summary>📄 Abstract</summary>
  Large Vision-Language Models (LVLMs) are prone to hallucinations: they fluently describe objects, attributes, and scenes that are not in the image. We connect part of this failure to a measurable property of their representations, feature instability, where mild semantics-preserving perturbations of the input cause large changes in the learned embeddings; hallucination rates rise together with this variability. Existing stability-motivated remedies are explicit, in the sense that they intervene ...
  </details>

- **2026-08-30** — Nhu Vo, Phuong Nguyen, Nu Uyen Phuong Le et al. — [En-ViMedNER: An English-Vietnamese Parallel Biomedical Corpus with UMLS Semantic Type Annotations](http://arxiv.org/abs/2608.29890v1)
  <details><summary>📄 Abstract</summary>
  Biomedical Named Entity Recognition (NER) is fundamental to healthcare AI applications, including clinical decision support and medical information extraction. While corpora with Unified Medical Language System (UMLS) annotations, such as MedMentions, have driven progress in English biomedical NER, no comparable resource exists for Vietnamese. This paper presents En-ViMedNER, the first English-Vietnamese parallel biomedical NER corpus annotated with UMLS semantic types, which are language-neutra...
  </details>

- **2026-08-30** — Luxi Lin, Zhanpeng Zeng, Shuang Peng et al. — [ReTrace: Rejected-Trajectory Conditioning for Speculative Decoding](http://arxiv.org/abs/2608.29748v1)
  <details><summary>📄 Abstract</summary>
  Speculative decoding accelerates autoregressive language model inference by having a lightweight draft model propose multiple candidate tokens, which are then verified in parallel by a larger target model. However, after the first rejection, standard prefix-based verification discards the remaining draft suffix, so the computation spent generating and verifying those positions does not contribute to decoding progress. Focusing on DFlash, we show that rejected positions in a rejected suffix may s...
  </details>


## 📊 统计 / Statistics

| 分类 / Category | 论文数 / Count |
|------|--------|
| jailbreak | 609 |
| prompt-injection | 519 |
| memory-poisoning | 46 |
| tool-use-attack | 131 |
| backdoor | 440 |
| adversarial-attack | 578 |
| privacy-leakage | 3984 |
| steganography | 61 |
| misuse | 966 |
| red-teaming | 120 |
| vulnerability | 2935 |
| defense | 2698 |
| alignment | 2508 |
| robustness | 2586 |
| watermark | 377 |
| unlearning | 93 |
| agent-safety | 52 |
| benchmark | 65 |
| survey | 315 |
| other | 7117 |

---

📚 **全部 26200 篇论文**（2022 至今）请访问 [GitHub Pages](https://ny1024.github.io/AgentSafety-Papers/) 查看完整列表、搜索与筛选。

*Generated by AgentGuard at 2026-09-02 15:49:45*