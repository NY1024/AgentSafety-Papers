<div align="center">

# AgentGuard 🛡️

**Daily Tracking of LLM Agent Security Papers on arXiv**

[![Auto Update](https://github.com/NY1024/AgentSafety-Papers/actions/workflows/daily-update.yml/badge.svg)](https://github.com/NY1024/AgentSafety-Papers/actions/workflows/daily-update.yml)
[![Papers](https://img.shields.io/badge/Papers-25934-blue)](#)
[![License](https://img.shields.io/badge/License-MIT-green)](#)

</div>

---

## 📖 简介 / Introduction

自动追踪 arXiv 上大模型 Agent 安全方向的最新论文，每日更新，关键词智能分类。

*Automatically tracking the latest LLM Agent security papers on arXiv, updated daily with keyword-based classification.*

**最近更新 / Last Updated**: 2026-09-02 02:45 ｜ **论文总数 / Total Papers**: 25934（近 30 天 / Recent 30 days: 4070）

🌐 **[GitHub Pages](https://ny1024.github.io/AgentSafety-Papers/)** — 查看全部 25934 篇论文（含摘要、分类筛选、搜索）/ View all 25934 papers with abstracts, filters & search

## 📑 分类导航 / Category Navigation

- **[jailbreak](#-jailbreak)** — 越狱攻击 / Jailbreak Attacks — 606
- **[prompt-injection](#-prompt-injection)** — 提示注入攻击 / Prompt Injection Attacks — 517
- **[memory-poisoning](#-memory-poisoning)** — 记忆投毒与篡改 / Memory Poisoning & Tampering — 45
- **[tool-use-attack](#-tool-use-attack)** — 工具使用攻击 / Tool-Use Attacks — 130
- **[backdoor](#-backdoor)** — 后门与投毒攻击 / Backdoor & Poisoning Attacks — 437
- **[adversarial-attack](#-adversarial-attack)** — 对抗攻击 / Adversarial Attacks — 573
- **[privacy-leakage](#-privacy-leakage)** — 隐私泄露 / Privacy Leakage — 3964
- **[steganography](#-steganography)** — 隐写与隐蔽通信 / Steganography & Covert Communication — 61
- **[misuse](#-misuse)** — 滥用与误用 / Misuse & Abuse — 956
- **[red-teaming](#-red-teaming)** — 红队测试 / Red Teaming — 120
- **[vulnerability](#-vulnerability)** — 漏洞与攻击面 / Vulnerabilities & Attack Surfaces — 2913
- **[defense](#-defense)** — 防御与防护方法 / Defense & Protection Methods — 2661
- **[alignment](#-alignment)** — 对齐与安全约束 / Alignment & Safety Constraints — 2467
- **[robustness](#-robustness)** — 鲁棒性与可靠性 / Robustness & Reliability — 2550
- **[watermark](#-watermark)** — 水印与溯源 / Watermarking & Provenance — 371
- **[unlearning](#-unlearning)** — 机器遗忘 / Machine Unlearning — 93
- **[agent-safety](#-agent-safety)** — Agent 安全框架 / Agent Safety Frameworks — 52
- **[benchmark](#-benchmark)** — 安全评测与基准 / Safety Benchmarks & Evaluation — 65
- **[survey](#-survey)** — 综述与系统化 / Surveys & Systematization — 309
- **[other](#-other)** — 其他安全相关 / Other Security-Related — 7044

## 📄 近期论文 / Recent Papers (Last 30 Days)

> 仅展示最近 30 天中最新的 500 篇论文（含日期、作者、摘要）。近 30 天共 4070 篇，完整 25934 篇论文列表请访问 [GitHub Pages](https://ny1024.github.io/AgentSafety-Papers/)

> Showing the latest 500 of 4070 papers from the last 30 days (with date, authors & abstract). For the full list of 25934 papers, visit [GitHub Pages](https://ny1024.github.io/AgentSafety-Papers/)

### 📂 jailbreak
*越狱攻击 / Jailbreak Attacks* — 6 papers

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

- **2026-08-27** — Junjie Zhang, Hui Liu, Kecheng Chen et al. — [RedEvoAgent: Automatic Red-Teaming Agent with Experience-Driven Skill Evolution](http://arxiv.org/abs/2608.27439v1)
  <details><summary>📄 Abstract</summary>
  LLM-based agents are increasingly deployed in product-level execution harnesses, where jailbreaks can trigger harmful tool use and persistent state changes, creating greater risks than unsafe text generation alone. Existing automatic red-teaming methods often rely on fixed attacks, while recent agentic attackers coordinate multiple jailbreak tools and show stronger potential through trajectory-based retrieval. However, such retrieval can reuse misleading experiences due to retrieval bias and unc...
  </details>

- **2026-08-27** — Qi Lu, Zehui Guo, David Yuanda Gan et al. — [TempJail: Temporal Jailbreak Attacks against Image-to-Video Generation Models](http://arxiv.org/abs/2608.26971v1)
  <details><summary>📄 Abstract</summary>
  In recent years, image-to-video (I2V) generation models have made remarkable progress in subject consistency and temporal coherence, enabling high quality video synthesis. However, these advances also introduce new safety risks. Existing studies mainly focus on jailbreak attacks involving single frame violations, while largely overlooking the temporal dimension unique to video generation models. In this paper, we investigate three attack scenarios and uncover a temporal vulnerability in I2V syst...
  </details>

- **2026-08-27** — Yu Zhe, Yixin Tan, Junhao Wei et al. — [A Single Suffix to Break Them All: Basin-Aware Jailbreaks for Merged Model Families](http://arxiv.org/abs/2608.26506v1)
  <details><summary>📄 Abstract</summary>
  Model merging enables combining multiple fine-tuned models without additional training, but its safety implications remain poorly understood. Prior work primarily attributes merging risks to unsafe constituent models, implicitly assuming that merging individually aligned models preserves safety. In contrast, we show that model merging reveals a previously overlooked jailbreak risk rooted in the pretrained foundation model, even when all constituent models are individually safety-aligned. Motivat...
  </details>


### 📂 prompt-injection
*提示注入攻击 / Prompt Injection Attacks* — 7 papers

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

- **2026-08-28** — Yupei Liu, Yuqi Jia, Neil Zhenqiang Gong et al. — [LongPIBench: A Long-Context Benchmark for Prompt Injection](http://arxiv.org/abs/2608.28411v1)
  <details><summary>📄 Abstract</summary>
  Prompt injection attacks pose a serious security risk to large language models in real-world applications. However, existing prompt injection benchmarks primarily focus on short-context inputs, leaving the attacks and defenses in long-context settings largely unexplored. This gap leads to a substantial overestimation of the effectiveness of current defenses. In this paper, we bridge the gap by introducing LongPIBench, a long-context benchmark for prompt injection covering 4 realistic application...
  </details>


### 📂 memory-poisoning
*记忆投毒与篡改 / Memory Poisoning & Tampering* — 1 papers

- **2026-08-31** — Chuanchao Zang, Zijian Cao, Xiangtao Meng et al. — [Understanding Stage-Wise Utility-Risk Trade-offs in LLM Agent Memory](http://arxiv.org/abs/2608.30177v1)
  <details><summary>📄 Abstract</summary>
  Long-term memory is becoming a core capability of LLM agents, enabling personalization and long-horizon interaction. However, memory mechanisms that retain, transform, or expose more information can affect both benign utility and susceptibility to memory poisoning. Existing evaluations typically measure memory utility or attack risk in isolation under fixed configurations, providing limited insight into how stage-specific design choices reshape their trade-off. We present \textsc{MemGauge}, a co...
  </details>


### 📂 tool-use-attack
*工具使用攻击 / Tool-Use Attacks* — 2 papers

- **2026-08-31** — Xiaofan Bai, Chao Liu, Hongqiang Lin et al. — [SkillZip Pro: Execution-Aware Dynamic Compression of Progressively Loaded Skills for Self-Evolving Agents](http://arxiv.org/abs/2608.30785v1)
  <details><summary>📄 Abstract</summary>
  Production agent skills are directory bundles, not isolated prompts. The root is loaded at activation; references, schemas, scripts, assets, and nested subskills are loaded only when an execution path needs them. Compressing only the root misses most deployment cost and may move branch-specific details into the always-loaded context. Flattening instead destroys progressive-loading boundaries.   We introduce \method, an evaluation-free compressor for complete, progressively loaded skill bundles. ...
  </details>

- **2026-08-27** — Yu-Lin Tsai, Yu-An Lu, Ci-Yang Tsai et al. — [Daydreaming: Stealing Hidden Agent Skills through Black-Box Task Interaction](http://arxiv.org/abs/2608.26733v1)
  <details><summary>📄 Abstract</summary>
  Agent skills bundle instructions, reference data, and executable helpers that let a general agent perform specialized tasks. Hosted providers can keep these files secret while selling access to task results, making the skill itself a valuable target. Existing disclosure defenses can block requests that ask for the skill or reproduce its text, but they cannot block customers from submitting the ordinary tasks the service is built to complete. We present Daydreaming, an execution-only attack that ...
  </details>


### 📂 backdoor
*后门与投毒攻击 / Backdoor & Poisoning Attacks* — 3 papers

- **2026-08-31** — Fukang Zhu, Binbin Zhao, Ruixiao Lin et al. — [Beyond the Payload: How User Invocation Shapes Coding Agent Vulnerability to Repository Poisoning](http://arxiv.org/abs/2608.30686v1)
  <details><summary>📄 Abstract</summary>
  Coding agents are increasingly used for software engineering tasks, including bootstrapping projects from third-party repositories whose integrity cannot be assumed. Prior work on repository poisoning largely focuses on attacker-controlled injection and disguise, but developers also shape risk through everyday invocation choices: what task to delegate, how to phrase the request, and which skills or rules to supply. We term these user-side choices Prompt-Level Configurations (PLCs) and introduce ...
  </details>

- **2026-08-31** — Yizhe Zeng, Chenxu Niu, Wei Zhang et al. — [Why Are LLM Backdoor Defenses Fragmented? A Feature-Level Explanation with Sparse Autoencoders](http://arxiv.org/abs/2608.30403v1)
  <details><summary>📄 Abstract</summary>
  Backdoor attacks pose a serious threat to large language models (LLMs), but existing defenses remain fragmented, failing to pro?vide unified defense against both dirty-label and clean-label attacks. To investigate why such fragmentation arises, we present the first systematic feature-level mechanistic analysis of LLM backdoors using sparse autoencoders (SAEs). Starting from a 2 x 2 comparison of clean and poisoned models on clean and triggered inputs, we trace backdoor-induced logit shifts to hi...
  </details>

- **2026-08-28** — Jaewon Jung, Haizhong Zheng, Hongsun Jang et al. — [CamoDocs: A Poisoning Attack Against Retrieval-Augmented Language Models Using Camouflaged Documents](http://arxiv.org/abs/2608.28389v1)
  <details><summary>📄 Abstract</summary>
  Retrieval-augmented generation (RAG) augments LLMs with external documents, but public or user-editable sources expose RAG systems to data poisoning: attackers can inject malicious documents to steer outputs toward targeted answers. Existing poisoning attacks often rely on query inclusion, inserting the target query into poisoned documents to improve retrieval; however, this creates lexical and embedding-space artifacts that make them easy to filter. We propose CamoDocs, a poisoning attack that ...
  </details>


### 📂 adversarial-attack
*对抗攻击 / Adversarial Attacks* — 1 papers

- **2026-08-30** — Bhaskar Ganesh Devalla, Junchao Wu, Nilesh Dokuparthi et al. — [IndicDetect: Evaluating Cross-Lingual LLM-Generated Text Detection for Hindi, Telugu, and Tamil](http://arxiv.org/abs/2608.29919v1)
  <details><summary>📄 Abstract</summary>
  The rapid proliferation of LLMs has further heightened the need to develop dependable AI-generated text detection, especially beyond English. Nevertheless, current benchmarks pay little attention to Indic languages and test detectors in idealized settings that do not represent the real world. We present a generalized benchmark for AI-generated text detection in Hindi, Telugu, and Tamil, which we call IndicDetect, designed to assess the robustness of detectors under realistic distribution shifts....
  </details>


### 📂 privacy-leakage
*隐私泄露 / Privacy Leakage* — 32 papers

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

- **2026-08-30** — Shicheng Hu, Runzhi Tian, Ziqiao Wang et al. — [On the Recoverability of Private Information Unlearning in Large Language Models](http://arxiv.org/abs/2608.29943v1)
  <details><summary>📄 Abstract</summary>
  Large language models (LLMs) can memorize sensitive information, raising serious privacy concerns. Machine unlearning offers a potential solution to remove such information, but it remains unclear whether existing methods truly erase it or merely hide it within the model. A key challenge is quantifying the persistence of sensitive data under a unified evaluation framework. To address this, we construct a synthetic dataset containing fake private information and propose a white-box auditing frame...
  </details>

- **2026-08-30** — Mohamed Abdalmoaty, Zheran Zeng, Dongsheng Yang et al. — [Identification of $dq$-Asymmetric Impedances as Complex Transfer Functions Using a Single Arbitrary Excitation](http://arxiv.org/abs/2608.29740v1)
  <details><summary>📄 Abstract</summary>
  Cross-coupling between the $dq$ coordinates makes the identification of asymmetric grid impedances a challenging problem, particularly near the fundamental frequency where the asymmetric coupling is strongest. Existing schemes usually handle it either by perturbing the two coordinates sequentially, which lengthens the measurement, or by using a time-domain method with a global parametric model whose order must be tuned. This paper develops a single-shot active non-parametric frequency-domain met...
  </details>

- **2026-08-30** — Zhe Dong, Wanqing Wu, Yuzhe Sun et al. — [GeoRay: Gauge-Aware Feed-Forward Satellite 3D Reconstruction in the Geodetic Frame](http://arxiv.org/abs/2608.29680v1)
  <details><summary>📄 Abstract</summary>
  Feed-forward 3D foundation models reconstruct perspective scenes in one pass. Satellite photogrammetry needs a different product, one that domain adaptation alone does not deliver: dense surface height in an absolute geodetic frame under non-central rational polynomial cameras (RPCs). Perspective-pretrained features are not reliably observable along RPC height rays, absolute elevation carries a low-order height--datum gauge exchangeable with sensor bias to first order, and monocular and multi-vi...
  </details>

- **2026-08-30** — Jinmeng Li, Quan Zhang, Hangting Ye et al. — [Creation begins with understanding: LLMs as strategy designers for privacy-preserving tabular data synthesis](http://arxiv.org/abs/2608.29674v1)
  <details><summary>📄 Abstract</summary>
  Sharing tabular data in high-stakes domains is constrained by privacy regulations. Synthetic data offer a promising alternative, but deep generative models are costly to train and difficult to audit, while LLM-based methods often serialize records as text, obscuring tabular structure and exposing sensitive data. We introduce Tabular Synthesis Strategy Designer (TabSSD), which uses an LLM to design synthesis procedures rather than directly generate records. TabSSD provides the LLM with tree-deriv...
  </details>

- **2026-08-30** — Shambhu Bhandari Sharma — [Evaluating a 4B open-weights local LLM for agentic DFT workflows: a literature reproducibility audit](http://arxiv.org/abs/2608.29665v1)
  <details><summary>📄 Abstract</summary>
  Agentic workflows in materials science relying on hosted commercial models face severe reproducibility, economic, and data-privacy constraints. To explore fully local agentic science, this work evaluates an open-weights Qwen3:4B model executing an autonomous scientific pipeline across varying hardware constraints. Applied to pentagonal two-dimensional materials, the system extracts parameters from unstructured text, translates them into density functional theory (DFT) inputs, and drives simulati...
  </details>

- **2026-08-30** — Stephen Meisenbacher, Andreea-Elena Bodea, Ahmet Bilal Akın et al. — [PrivBench: A Holistic and Modular Benchmarking Platform for Evaluating Text-to-Text Privatization](http://arxiv.org/abs/2608.29624v1)
  <details><summary>📄 Abstract</summary>
  Natural Language Processing methods have enabled novel solutions and advances in the field of privacy, particularly in the sub-domain of text-to-text privatization, where the goal is to transform a sensitive input text into a privatized output by ideally masking (in)directly identifiable or otherwise private information. The evaluation of text-to-text privatization, however, is not straightforward, and the extant literature has utilized a myriad of techniques and metrics to quantify the privacy-...
  </details>

- **2026-08-30** — Arka Mukherjee, Soham Roy, Kartikeya Trivedi et al. — [GeoAgent: Evaluating VLM Geolocalization Through Embodied Navigation](http://arxiv.org/abs/2608.29483v1)
  <details><summary>📄 Abstract</summary>
  Modern Vision-Language Models (VLMs) perform well above the human baseline in image geolocalization, a task critically important in disaster response, OSINT verification, and location privacy. However, most efforts to study AI behavior on the task remain limited to static image-based retrieval, classification, and predictions. We argue that faithful recreation of the task should involve embodied navigation, where a multimodal agent autonomously explores its surroundings to gather observations be...
  </details>

- **2026-08-29** — Ruiyi Yang, Gayathri Lihinikaduarachchi, Rahat Masood et al. — [GuardianAgent: Policy-Conditioned Risk-Adaptive Anonymization with Verified Adversarial Escalation](http://arxiv.org/abs/2608.29251v1)
  <details><summary>📄 Abstract</summary>
  Privacy protection for live web traffic requires more than detecting private spans. Agent-based privacy protection systems must determine whether an outgoing action complies with the destination site's privacy policy, then apply only the level of rewriting or sanitisation justified by the residual disclosure risk. We present GuardianAgent, a policy-conditioned anonymization framework that couples structured risk assessment with verified adaptive rewriting. GuardianAgent computes risk through AMR...
  </details>

- **2026-08-29** — Lee En-Yi Hannah, Haozhi Cao, Yuecong Xu — [Multi-Scale Temporal Domain Alignment for Federated Video Domain Adaptation](http://arxiv.org/abs/2608.29186v1)
  <details><summary>📄 Abstract</summary>
  Federated Video Domain Adaptation (FVDA) enables collaborative learning across distributed and non-IID video datasets while preserving privacy, but is under-explored due to challenges in aligning temporal information. We propose Multi-scalE Temporal domAin aLignment (METAL), a novel framework that leverages temporal information at multiple resolutions to improve cross-domain video action recognition with only model parameter transfers. METAL trains per-scale transformer encoders on source-client...
  </details>

- **2026-08-29** — Jona te Lintelo, Lichao Wu, Stjepan Picek — [WoE Wrote It? Watermarking Mixture-of-Experts LLMs for Black-Box Text Provenance](http://arxiv.org/abs/2608.29151v1)
  <details><summary>📄 Abstract</summary>
  Large Language Model (LLM) watermarks provide a mechanism for text provenance, enabling model owners to identify machine-generated content and attribute it to a specific watermarked model. However, current LLM watermarking approaches predominantly rely on inference-time sampler methods and focus their analysis on dense models. Inference-time methods are only effective when the text is explicitly generated via the model owner's controlled API; they fail in a post-compromise scenario. An adversary...
  </details>

- **2026-08-29** — Kejia Zhang, Tianyuan Zou, Zixuan GU et al. — [Auditing and Mitigating Privacy Leakage in Cloud-Edge Collaborative Decoding](http://arxiv.org/abs/2608.29111v1)
  <details><summary>📄 Abstract</summary>
  Applications such as personalized assistance and proprietary document analysis require large language models (LLMs) to generate outputs from private data. Yet powerful LLMs typically cannot be deployed on the resource-constrained devices where private data resides, and uploading private data to cloud-hosted LLMs exposes sensitive information. Recent work addresses this tension with a cloud-edge collaborative decoding paradigm, where private data are kept on the edge with a small language model (...
  </details>

- **2026-08-29** — Sunghwan Han, Youngtae Han, Youngmin Yi — [AdaVLA: Adaptive Step Flow Matching for Training-free Acceleration of Vision-Language-Action Models](http://arxiv.org/abs/2608.29208v1)
  <details><summary>📄 Abstract</summary>
  Vision-Language-Action (VLA) models, built upon Vision-Language Models (VLMs), have significantly enhanced robotic capabilities by leveraging internet-scale knowledge and multimodal reasoning. However, the intensive computational overhead of VLAs constrains on-device deployment, hindering real-time responses to environmental changes. While various acceleration techniques have been proposed, they often rely on fine-tuning or access to training datasets, which are frequently unavailable due to pri...
  </details>

- **2026-08-29** — Yian Wang, Agam Goyal, Eshwar Chandrasekharan et al. — [Facts Without Rules: Boundary Metadata Collapse in Multi-Agent LLM Handoffs](http://arxiv.org/abs/2608.29028v1)
  <details><summary>📄 Abstract</summary>
  Multi-agent LLM systems often coordinate by compressing an upstream interaction into a handoff artifact that downstream agents treat as shared state. We show that this handoff step is a structural source of privacy leakage: summaries preferentially preserve operational facts while weakening the boundary metadata that governs how those facts may be used---a failure mode we call \emph{summary collapse}. On a controlled multi-agent coordination testbed we measure marker survival with a human-valida...
  </details>

- **2026-08-28** — Daniela Occhipinti, Malvina Nissim, Marco Guerini — [Stranger, Fan, or Peer? A Systematic Study on the Role of Interlocutor in Persona-Based Dialogue Generation](http://arxiv.org/abs/2608.28467v1)
  <details><summary>📄 Abstract</summary>
  Persona-based dialogue systems are usually conditioned on speaker biography, but dialogues involve at least two participants, and who has access to whose biography can vary across training, inference, and evaluation. Prior work often neglected these aspects, obscuring mechanisms that only appear when biography visibility is toggled separately across training, inference, and evaluation, a three-stage factorisation that prior work has largely treated as a single factor. We study this factorisation...
  </details>

- **2026-08-28** — Wonjun Lee, Jaehyuk Jang, Kangwook Ko et al. — [AIM: Anchor Identity Features, Then Match for Multimodal Large Language Model Unlearning](http://arxiv.org/abs/2608.28312v1)
  <details><summary>📄 Abstract</summary>
  Multimodal large language models (MLLMs) can memorize identity-specific facts about people in their fine-tuning data, creating privacy risks when a person requests deletion. Existing MLLM unlearning methods often assume access to retain images or ground-truth answers during deletion, which is unrealistic in many practical scenarios. We study identity unlearning when retain images are unavailable at deletion time. Our analysis shows that identity and visual-perception questions occupy distinct re...
  </details>

- **2026-08-27** — Shengzhuang Chen, Jerrod Parker, Yejin Bang et al. — [Thomson: Continual Learning of Frontier Models for SovereignAI](http://arxiv.org/abs/2608.27147v1)
  <details><summary>📄 Abstract</summary>
  The development of frontier models is commonly perceived to be the exclusive remit of a small number of heavily funded players, creating an information, economic and power asymmetry between developers and the diverse user base of modern AI. Recent public discourse acknowledges this concern, calling for SovereignAI (an organisation's capability to independently build, deploy and govern AI use), but offers little concrete advice on how this can be achieved in the short term under a diversity of fu...
  </details>

- **2026-08-27** — Menghui Zhang, Aoying Zheng, Guoxiao Liu et al. — [Beyond Vector Hiding: Breaking and Mitigating Shared-Direction Weight Obfuscation in TEE-Offloaded Large Language Models](http://arxiv.org/abs/2608.26651v1)
  <details><summary>📄 Abstract</summary>
  Trusted Execution Environment (TEE)-shielded partitioning of Large Language Models (LLMs) accelerates on-device inference by offloading obfuscated linear layers to an untrusted accelerator while retaining only a small correction inside the TEE. However, earlier lightweight obfuscation schemes preserved weight-vector directions and were broken by ArrowMatch. To defend against this attack, ArrowCloak injects scalar multiples of the same hidden direction into all weight vectors, enabling lightweigh...
  </details>

- **2026-08-27** — Jin Liu, Junkang Liu, Ning Xi et al. — [When Privacy Hurts Mergeability: Geometry-Aware Model Merging under Differential Privacy](http://arxiv.org/abs/2608.26655v1)
  <details><summary>📄 Abstract</summary>
  Model merging promises to construct a single multi-task model from independently fine-tuned task models without accessing the original task data. This makes it attractive when task data cannot be centralized, but released task models may still leak private fine-tuning data. Differential privacy (DP) provides a principled mechanism for limiting such leakage, yet its effect on model merging remains poorly understood. In this paper, we study the geometry of differentially private model merging and ...
  </details>

- **2026-08-27** — Jiahui tang, Kuicai Dong, Dexun Li et al. — [DEEPCHART: How Far are LLMs from Faithful Data-Science Chart Generation?](http://arxiv.org/abs/2608.26757v1)
  <details><summary>📄 Abstract</summary>
  Faithful chart generation in real-world data-science workflows requires grounding visualizations in scattered evidence, computing chart-ready quantities, and rendering them accurately. Modern LLMs can produce visually plausible, instruction-compliant charts, yet data-level hallucinations remain difficult to detect in long, noisy, and multimodal contexts. To measure this gap, we introduce DEEPCHART, an expert-annotated benchmark of 1,482 task-conditioned chart-generation instances drawn from real...
  </details>

- **2026-08-27** — Waqas Khan, Tabinda Sarwar, Jingyue Cong et al. — [Graph-Guided Selective Unlearning for Language Models: Controlling Support Routes Beyond Forget Seeds](http://arxiv.org/abs/2608.26743v1)
  <details><summary>📄 Abstract</summary>
  Enterprises fine-tune language models on proprietary data that may later require removal due to privacy, contractual, or compliance obligations. Selective unlearning removes requested knowledge while preserving model utility, offering a practical alternative to full retraining, but existing methods treat the explicitly identified forget examples as the complete deletion scope. This is insufficient when target knowledge remains recoverable through paraphrases, aliases, or neighboring training exa...
  </details>

- **2026-08-27** — Junyoung Lee, Sehyeon Park, Shinhyoung Jang et al. — [FOCUS & RePAIR: Mitigating Text Degeneration via Token-Level Guidance for Pruned Large Language Models](http://arxiv.org/abs/2608.26676v1)
  <details><summary>📄 Abstract</summary>
  Pruning is a practical approach to compress large language models (LLMs), but it can amplify text degeneration, especially repetition loops, even when perplexity and task accuracy remain largely unchanged. In this work, we present a token-level analysis of this failure mode by viewing decoding as a dynamical process that enters and persists in a small set of recurrent contexts. Our analysis decomposes degeneration into loop entry risk and loop persistence, and shows that persistence is controlle...
  </details>


### 📂 steganography
*隐写与隐蔽通信 / Steganography & Covert Communication* — 3 papers

- **2026-08-31** — Minkyung Cho, Jihyo Kim, SeungWoo Song et al. — [Hidden Threat in Synthetic Data: Covert Targeted Bias Injection through Benign Text](http://arxiv.org/abs/2608.30619v1)
  <details><summary>📄 Abstract</summary>
  Synthetic data is increasingly used to train large language models (LLMs), yet its security implications remain poorly understood. Prior work on subliminal learning suggests that models can inherit behavioral traits from seemingly unrelated training data. In this work, we investigate whether such mechanisms can be exploited to inject targeted social biases into aligned models through semantically benign synthetic data. We construct a pipeline in which a misaligned teacher model generates filtere...
  </details>

- **2026-08-31** — Rastislav Lenhardt, Teodora Dobos, Thomas Vecchiato et al. — [RSLM: Training-Free Vector Quantization for Approximate Nearest Neighbor Search](http://arxiv.org/abs/2608.30384v1)
  <details><summary>📄 Abstract</summary>
  By introducing RSLM (Rotated Scaled Lloyd-Max), a family of training-free vector quantization codecs compressing embeddings to 1--4 bits per dimension, we reduce memory cost and memory bandwidth of a typical large-scale Approximate Nearest Neighbor (ANN) search system, while reducing its complexity and keeping or improving recall across multiple benchmark datasets. State-of-the-art systems filter candidates using coarse partitions, approximately score them to narrow the set, and then rescore the...
  </details>

- **2026-08-29** — Ruiyi Yan, Chenhui Chu, Zhongliang Yang et al. — [A Comprehensive Survey on Linguistic Steganography: Methods, Countermeasures, Evaluation, and Challenges](http://arxiv.org/abs/2608.29077v1)
  <details><summary>📄 Abstract</summary>
  Linguistic steganography hides secret messages in natural language text. Large language models (LLMs) have reshaped the field, but a systematic account of how these scattered advances collectively reshape the field in this new era is still missing. We provide one along four axes: 148 steganographic methods, 60 linguistic steganalysis countermeasures, 23 evaluation metrics, and 9 open challenges, each with taxonomies, reviews, and adoption analyses. Cutting across these axes, we identify five spe...
  </details>


### 📂 misuse
*滥用与误用 / Misuse & Abuse* — 17 papers

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

- **2026-08-30** — Xiaoyang Han, Lvxiaowei Xu, Ming Cai — [When Less is More: Understanding When Token Filtering Helps and Fails in AI-generated Text Detection](http://arxiv.org/abs/2608.29903v1)
  <details><summary>📄 Abstract</summary>
  The rapid advancement of large language models (LLMs) has made AI-generated text detection increasingly critical. Existing zero-shot detectors assume that more token-level evidence leads to more reliable detection. However, our empirical study challenges this consensus: fewer tokens sometimes work better, retaining only 40% can yield optimal performance, yet this benefit is not universal. Using the Entropy Gap Score (EGS), we introduce top-$k$ cumulative probability filtering as a diagnostic pro...
  </details>

- **2026-08-30** — Nadav Borenstein, Greta Warren, Desmond Elliott et al. — [MMMMM: A Unified Taxonomy for Investigating the Mechanisms of Multilingual MultiModal Misinformation](http://arxiv.org/abs/2608.29681v1)
  <details><summary>📄 Abstract</summary>
  Multimodal misinformation on social media is highly prevalent, potent, and harmful, yet difficult to detect and counter, and still poorly understood compared to its text-only counterpart. Research on the properties and deceptive strategies of multimodal misinformation is hindered by a lack of taxonomies grounded in real-world contexts and by the limitations of current multimodal machine learning models, which prevent the automation of annotation and analysis at scale. We address these shortcomin...
  </details>

- **2026-08-30** — Hongbo Gao, Zeyu Ni, Xin Wen et al. — [AGM: Achievement-Grounded Memory for Closed-Loop Agents with Frozen VLA Policies](http://arxiv.org/abs/2608.29537v1)
  <details><summary>📄 Abstract</summary>
  Frozen vision-language-action (VLA) policies offer broad manipulation skills but execute open-loop action chunks without tracking task progress, so the agent cannot reliably decide whether to continue, retry, or terminate. External memory is a natural remedy, yet it can be harmful when attempted actions are treated as completed progress, turning local execution errors into persistent task-state errors. We propose Achievement-Grounded Memory (AGM), a lightweight closed-loop framework for frozen V...
  </details>

- **2026-08-29** — Mingxuan Li, Qirun Dai, Heran Wang et al. — [Emergent Misalignment Is Not Magical](http://arxiv.org/abs/2608.29118v1)
  <details><summary>📄 Abstract</summary>
  Fine-tuning large language models (LLMs) on narrowly harmful datasets can lead to misalignment broadly, a phenomenon known as emergent misalignment (EM). EM poses a challenge for AI safety and our understanding of LLMs. Prior work often frames EM as an unexpected behavior, and explains it by appealing to general misalignment directions or anthropomorphizing it as acquiring an evil persona. However, the mechanisms behind these framings remain obscure. In this work, we show that EM is a predictabl...
  </details>

- **2026-08-29** — Yucheng Du, Xiyang Hu — [Recognition-Refusal Misalignment in LLMs: Why Models Answer Structurally Unanswerable Questions](http://arxiv.org/abs/2608.29109v1)
  <details><summary>📄 Abstract</summary>
  Large language models often answer structurally unanswerable questions, such as computing cot(-540°) or evaluating (1).startswith("1"), instead of abstaining. We ask whether this failure reflects missing recognition or failed routing from recognition to abstention. Across instruction-tuned models from 1.7B to 70B parameters, a single linear direction in the hidden state separates answerable from structurally impossible math and code prompts, showing that models represent impossibility before gen...
  </details>

- **2026-08-29** — Mohamad Zbib, Ammar Mohanna — [Arabic Safety Alignment as Selective Refusal: An Empirical Study of SFT, DPO, and Guard Calibration](http://arxiv.org/abs/2608.29378v1)
  <details><summary>📄 Abstract</summary>
  Arabic large language models must refuse harmful prompts without over-refusing benign or sensitive prompts, yet a single refusal rate hides this trade-off. We evaluate it using benign refusal B and harmful-prompt refusal H, where H measures refusal rather than harmful compliance. Across five Arabic-capable models and 130 runs on the full human-written AraSafe set, refusal-only supervised fine-tuning (SFT) collapses toward blanket refusal, whereas selected mixed-SFT configurations reach H = 90% t...
  </details>

- **2026-08-29** — Shoei Inoue, Norihiro Yoshida, Erina Makihara et al. — [Database-Augmented RAG for Automated Repair of REST API Misuses](http://arxiv.org/abs/2608.29290v1)
  <details><summary>📄 Abstract</summary>
  Many Internet of Things (IoT) services provide Representational State Transfer (REST) APIs, which require client developers to implement applications that conform to the corresponding API specifications. When client programs contain API misuse, developers debug them based on error responses. However, such responses are often insufficient for identifying the root cause, requiring developers to repeatedly communicate with the server. Retrieval-Augmented Generation (RAG) is a promising approach for...
  </details>

- **2026-08-27** — Yutong Zhang, Jianshuo Dong, Peng Xu et al. — [INTENT-AS-A-TOOL Makes it Easy to Track Agentic Misalignment](http://arxiv.org/abs/2608.27348v1)
  <details><summary>📄 Abstract</summary>
  As large language models (LLMs) are deployed as autonomous agents, safety failures increasingly involve consequential actions. We study agentic misalignment, where agents take harmful actions under goal conflicts and pressures. Using chain-of-thought (CoT) monitoring, we find that harmful execution is often preceded by intent signals in reasoning. However, post-hoc CoT labels are too coarse to show how intent changes during generation. We introduce INTENT-AS-A-TOOL, an approach that adds intent-...
  </details>

- **2026-08-27** — Tingyun Li, Wenfeng Feng, Weiqing Li et al. — [Knowing When Not to Reuse: Conditional Experience Transfer in Autonomous LLM Post-Training](http://arxiv.org/abs/2608.26730v1)
  <details><summary>📄 Abstract</summary>
  Large language models offer broad capabilities, but adapting them to evolving domains, tools, and requirements often entails repeated post-training. Autonomous systems automate parts of this process by proposing updates, training candidates, and using evaluation feedback to select subsequent proposals. As evidence accumulates, a central problem emerges: which past update evidence remains actionable after subsequent training has changed the parent model? An update's effect depends on its parent, ...
  </details>


### 📂 red-teaming
*红队测试 / Red Teaming* — 2 papers

- **2026-08-28** — Jun Wen Leong — [Recognition Without Enforcement: Configuration-Dependent Failures in LLM Agent Instruction Arbitration and External Control](http://arxiv.org/abs/2608.28502v1)
  <details><summary>📄 Abstract</summary>
  LLM agents arbitrate among instructions from system prompts, users, memory, and tools, but this arbitration cannot be assumed to enforce trust boundaries. We identify a recognition-enforcement gap: source-format features (role-template position, channel metadata, formatting cues) are linearly decodable from model activations, and models can explicitly identify forged authority when prompted, yet some configurations still produce the conflicting tool call. We use "recognition" in this specific de...
  </details>

- **2026-08-27** — Chenhao Wu, Haoxuan Jia, Yang Liu et al. — [Safety Does Not Compose: Non-Decaying Loop State for Autonomous LLM Agents](http://arxiv.org/abs/2608.27141v1)
  <details><summary>📄 Abstract</summary>
  Large language model agents are increasingly deployed as autonomous loops. Starting from one human goal, such a system repeatedly discovers work, plans, executes tool calls, verifies outcomes and persists state across many unattended iterations. The agent safeguards in wide use, however, are defined over a single trajectory, and their safety state is re-initialized when the next trajectory begins. We show that this is a failure of composition rather than an implementation detail. Our central res...
  </details>


### 📂 vulnerability
*漏洞与攻击面 / Vulnerabilities & Attack Surfaces* — 65 papers

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

- **2026-08-29** — Francesca Gomez — [Can escalation channels redirect reward hacking toward defect disclosure?](http://arxiv.org/abs/2608.29460v1)
  <details><summary>📄 Abstract</summary>
  When coding agents encounter defective test infrastructure they may reward-hack: hardcoding outputs or editing test files to pass tests they cannot legitimately satisfy, a pattern that has now appeared outside benchmarks, in a coordinated multi-agent intrusion of a major AI platform's production infrastructure. The same capability that lets an agent detect and exploit a defect could let it report one, given the right decision environment. We evaluate escalation channels, structured reporting too...
  </details>

- **2026-08-29** — Andrew Aquilina, Xiang Lorraine Li, Yu-Ru Li — [Whose Assessment of Distress? Community Perspectives and LLM Alignment on Well-Being Posts](http://arxiv.org/abs/2608.29446v1)
  <details><summary>📄 Abstract</summary>
  Judgments about psychological distress are socially situated: what counts as concerning hinges on community norms around emotional expression, vulnerability, and help-seeking. Yet large language models (LLMs) used for distress detection are typically aligned to a single, undifferentiated standard. How well do these models capture the perspectives of the communities whose language they assess? We address this question through a perspectivist annotation study in which 321 participants provided 9,5...
  </details>

- **2026-08-29** — Ziniu Li, Jinbo Wang, Guanhua Huang et al. — [When Do Larger Batches Help Scale LLM Reinforcement Learning?](http://arxiv.org/abs/2608.29296v1)
  <details><summary>📄 Abstract</summary>
  Larger batches reduce the variance of stochastic gradients per update and are therefore often expected to accelerate training. Yet whether this statistical benefit translates into lower wall-clock time-to-target remains unclear, because each update consumes more samples and may take longer to execute. We study this tradeoff in reinforcement learning for large language models. We separate its algorithmic and systems effects by comparing learning and execution along their natural axes. At the algo...
  </details>

- **2026-08-29** — Eduard Zamfir, Christian Reisswig, Zongwei Wu et al. — [Elastic Token Compression for Pixel-Space Diffusion Transformers](http://arxiv.org/abs/2608.29281v1)
  <details><summary>📄 Abstract</summary>
  Natural images concentrate their detail in a small fraction of the frame, yet diffusion models spend a full token on every patch, in every layer and at every timestep. The waste is largest in pixel-space models, with no autoencoder to absorb low-level redundancy first. Probing a pretrained pixel text-to-image transformer, we find its middle-block tokens redundant wherever the image is flat. The redundancy occupies connected, content-shaped regions, and exploiting it requires tokens with the same...
  </details>

- **2026-08-29** — Yuhan Li, Xianfeng Tan, Fangao Zeng et al. — [RAGDiffusion++: From Macro-Retrieval to Micro-Fidelity Alignment for Garment Generation](http://arxiv.org/abs/2608.29280v1)
  <details><summary>📄 Abstract</summary>
  Standard clothing asset generation---restoring forward-facing flat-lay garment images from diverse real-world contexts---holds immense commercial value yet demands both macroscopic topological accuracy and microscopic physical fidelity. Although our previous work RAGDiffusion effectively eradicated large-scale structural hallucinations via retrieval-augmented macro-constraints, achieving industrial-grade micro-texture realism remains an unsolved bottleneck. We formally identify this limitation a...
  </details>

- **2026-08-29** — Abdelrahman Abdallah, Mohammed Ali, Bhawna Piryani et al. — [Large Language Models Systematically Favor Popular Options: Evidence and Mitigation Across MCQs](http://arxiv.org/abs/2608.29257v1)
  <details><summary>📄 Abstract</summary>
  Multiple-choice questions (MCQs) are a standard format for evaluating large language models (LLMs), yet the popularity of answer options can confound evaluation. Modern LLMs systematically prefer popular but incorrect options over less popular correct ones, a vulnerability we call \textbf{popularity bias}. This pattern aligns with confidence miscalibration: model confidence remains high even as accuracy collapses for popular options. To systematically isolate this phenomenon, we introduce \textb...
  </details>

- **2026-08-29** — Li-Ni Fu, Chang-Chih Meng, Chien-Hua Chen et al. — [How Identity and Opinion Shape Political Sycophancy in LLMs](http://arxiv.org/abs/2608.29198v1)
  <details><summary>📄 Abstract</summary>
  As Large Language Models (LLMs) increasingly encourage users to disclose personal profiles for tailored assistance, measuring their political alignment becomes increasingly important. However, many existing benchmarks for assessing political behavior rely on closed-ended questions and do not fully capture how a model's stance may adapt to user-provided context during interaction. We introduce a framework that disentangles two distinct triggers of political sycophancy: opinion (aligning with expl...
  </details>

- **2026-08-29** — Zelin Wan, Arash Nourian, Xiaoxiao Li et al. — [APIFlow-Bench: Measuring Whether Agents Survive Long, Dependent API Workflows](http://arxiv.org/abs/2608.29128v1)
  <details><summary>📄 Abstract</summary>
  Tool-using agents are commonly evaluated by a single bit: whether an end-to-end workflow completed. This metric fails to distinguish failures that matter in production, such as expired credentials, malformed payloads, or correct execution followed by incorrect final delivery. We introduce APIFlow-Bench, a fully auditable benchmark for long-horizon, dependent REST-API workflows that decomposes performance into seven engineering capabilities and requires agents to produce answers supported by the ...
  </details>

- **2026-08-29** — Yifan Xiang, Bin Liang, Yuqi Huang et al. — [Not All or None: Dynamic Construction of Target-aware Memory Graph for Conversational Stance Detection](http://arxiv.org/abs/2608.29066v1)
  <details><summary>📄 Abstract</summary>
  Stance detection is crucial for understanding the underlying attitude of an expression towards a target. Conversational stance detection is a more challenging stance detection task in real-world social media scenarios, as it involves detecting the user's stance by leveraging the target-related historical statements across conversational sessions. In this paper, we propose target-aware Memory Graph TamGraph, a novel method that dynamically leverages target-related statements for conversational st...
  </details>

- **2026-08-29** — Hanting Li, Xin Sun, Wei Ye et al. — [Di$^2$CycleSB: Towards High-Quality Unsupervised Nighttime Visibility Enhancement via Schrödinger Bridge Transformer](http://arxiv.org/abs/2608.29043v1)
  <details><summary>📄 Abstract</summary>
  Light-effect contamination poses a significant challenge to nighttime visibility enhancement. Most methods suppress light effects by estimating and decomposing them through prior-driven regularization, yet they are often limited by hand-crafted priors and ill-posed nature of decomposition. This work proposes Di$^2$CycleSB, a unsupervised Cycle Schrödinger Bridge Transformer framework guided by dynamic integral image priors, for high-quality unsupervised nighttime visibility enhancement. Specific...
  </details>

- **2026-08-28** — Javier Aguilar Martín — [An Enclosed Mode Is a Gauge Choice: Topology Relative to Reach in Certified Code World Models](http://arxiv.org/abs/2608.28541v1)
  <details><summary>📄 Abstract</summary>
  A code world model accepted by a sampling gate can be exactly right on everything the gate can see and arbitrarily wrong beyond it. We characterize what a certified model can know, and what its errors can cost, when the omission is an annular freeze mode enclosing an unreachable interior. The gate quotient makes the question precise: acceptance-with-certainty determines the model exactly on the reachable query set; beyond reach is gauge. On a minimal ring instrument we prove the extreme case (a ...
  </details>

- **2026-08-28** — Arun D. Kulkarni — [Texture Image Classification Using DWT AlexNet Feature Fusion and Deep Neural Networks](http://arxiv.org/abs/2608.28524v1)
  <details><summary>📄 Abstract</summary>
  Texture image classification plays a significant role in computer vision applications, including industrial inspection, medical image analysis, remote sensing, and object recognition. Handcrafted features can capture local texture characteristics but may have limited capability to represent complex visual patterns. In contrast, deep learning models automatically learn discriminative representations but may not fully exploit the multiscale spatial-frequency information inherent in texture images....
  </details>

- **2026-08-28** — Mingyuan Huang, Zimo Ji, Yifan Mo et al. — [When Verified Source Becomes Attack Input: Defending Smart Contracts Against LLM-Based Vulnerability Scanning](http://arxiv.org/abs/2608.28400v1)
  <details><summary>📄 Abstract</summary>
  Smart contracts are financial programs deployed on blockchains to manage digital assets. To build trust with users and investors, smart contract projects typically publish their source code on blockchain explorers and verify it against the deployed bytecode, making the on-chain program accessible through a human-readable implementation. However, LLM agents are changing the threat model of this disclosure mechanism. By leveraging publicly disclosed source code, recent agent workflows make it incr...
  </details>

- **2026-08-28** — Angelo Sparacino, Francesca Toni, Adam Dejl — [Embedding Models for Stance-Aware Argument Retrieval](http://arxiv.org/abs/2608.28283v1)
  <details><summary>📄 Abstract</summary>
  In computational argumentation, obtaining arguments that explicitly support or attack given claims is a critical precursor to downstream reasoning tasks. When these supporting and attacking arguments are to be retrieved using semantic search methods, they need to be assessed for topic-relevance to the claims of interest as well as for correctness of their (positive or negative) stance towards the claims. In this paper we explore how dense embedding models (hereafter, models), powering modern ret...
  </details>

- **2026-08-28** — Yang Chen, Zhenyu Huang, Wenbo Fu et al. — [STEGNav: Spatio-Temporal Event Graph Reasoning for Multimodal Lifelong Object Navigation](http://arxiv.org/abs/2608.28279v1)
  <details><summary>📄 Abstract</summary>
  Multimodal lifelong navigation requires an agent to autonomously explore unseen environments while sequentially completing navigation tasks specified by object categories, language descriptions, or reference images. Existing methods primarily accomplish these tasks by constructing state-centric semantic scene graphs. By treating scene graphs as persistent repositories of semantic observations, these methods struggle to distinguish similar instances, jointly represent semantic targets and explora...
  </details>

- **2026-08-27** — Frederik Berenz — [Successive Capacity Growth: Task-Complexity-Driven Width and Depth Expansion for Vision Transformer Encoders in JEPA World Models](http://arxiv.org/abs/2608.27367v1)
  <details><summary>📄 Abstract</summary>
  Joint-Embedding Predictive Architectures (JEPAs) for world modeling typically employ fixed-size Vision Transformer encoders that are over-provisioned for simple tasks and under-provisioned for complex ones, with significant redundancy across attention heads. We propose Successive Capacity Growth (SCG), a method that starts from a minimal encoder (1 head, 2 layers, 283K parameters) and grows incrementally in width (adding attention heads for low-level semantic capacity) or depth (adding transform...
  </details>

- **2026-08-27** — Yunpeng Ba, Zhi Zheng, Yue Xie et al. — [Understanding Evolution Strategies for LLM Reasoning: Broader Reasoning Coverage than GRPO](http://arxiv.org/abs/2608.27351v1)
  <details><summary>📄 Abstract</summary>
  Evolution Strategies (ES) have recently emerged as a memory-efficient post-training paradigm for LLM reasoning. However, the optimization behavior of ES remains understudied, making it hard to define its advantage scope compared to mainstream post-training paradigms (e.g., Group Relative Policy Optimization (GRPO)). By systematically investigating ES dynamics and mechanisms, this paper first identifies a performance advantage of ES over GRPO, theoretically and empirically showing that ES can lea...
  </details>

- **2026-08-27** — Catherine Simons, Alexander K. Saeri, Peter Slattery et al. — [Assessing Company Contributions to Societal Resilience: Extending the Societal Capacity Assessment Framework to Agentic AI](http://arxiv.org/abs/2608.27238v1)
  <details><summary>📄 Abstract</summary>
  Companies that deploy AI agents and make them available to others are creating the sociotechnical circumstances under which this technology integrates into existing social and economic structures. AI-deploying companies are institutional actors that actively shape society's capacity to withstand and govern the consequences of agentic AI. In view of these societal impacts, companies can build societal resilience by designing and promoting safer implementations of AI agents. To operationalize this...
  </details>

- **2026-08-27** — Nicola Vassena — [Sequential and distributive dual futile cycle: Hopf bifurcation can occur under parameter-rich kinetics but cannot occur under mass action kinetics](http://arxiv.org/abs/2608.27081v1)
  <details><summary>📄 Abstract</summary>
  This paper establishes that the system of ordinary differential equations arising from the sequential and distributive dual futile cycle has the structural capacity for Hopf bifurcations, whenever it is endowed with general parameter-rich kinetics, but it loses such capacity if it is endowed with mass action kinetics. The proof of the latter fact relies on a Routh-Hurwitz approach, improved by few preliminary structural considerations, but a decisive contribution came from ChatGPT Sol 5.6, which...
  </details>

- **2026-08-27** — Ziyue Wang, Shiqi Huang, Weiwen Xu et al. — [Video-OPSD: Exploiting Privileged Visual Evidence for On-Policy Self-Distillation in Video Large Language Models](http://arxiv.org/abs/2608.27065v1)
  <details><summary>📄 Abstract</summary>
  On-policy self-distillation (OPSD) has recently emerged as an effective post-training paradigm that improves policy optimization through dense token-level supervision from a privileged self-teacher. Despite its promise, OPSD remains largely underexplored for Video Large Language Models (Video-LLMs). Existing methods typically construct privileged teachers by augmenting their context with additional information while keeping the primary input unchanged for both teacher and student. Video reasonin...
  </details>

- **2026-08-27** — Yuzhe Zhao — [Anatomy-Guided Foundation Model Adaptation with Within-Case Prototype Supervision for Standard Plane Detection in Fetal Ultrasound Blind Sweeps](http://arxiv.org/abs/2608.27051v1)
  <details><summary>📄 Abstract</summary>
  Detecting the fetal abdominal circumference standard plane in low-cost obstetric blind sweeps is a highly imbalanced frame-classification problem: positive frames account for under 3% of a sequence, form short contiguous segments, and are poorly handled by off-the-shelf ultrasound and vision foundation models. We propose AnatoProto, a lightweight sequence-level framework that adapts a frozen BiomedCLIP encoder to fetal blind sweeps through four components: (i) anatomy-weighted spatial pooling th...
  </details>

- **2026-08-27** — Hanchong Chen, Xing Tang, Lingjie Li et al. — [When Memory Takes Gradients: Collaborative Vector Memory for Agentic Recommender Systems](http://arxiv.org/abs/2608.26895v1)
  <details><summary>📄 Abstract</summary>
  Agentic recommender systems ground each decision of a large language model (LLM) in a persistent memory of the user, and in existing agents that memory is text: a narrative written and maintained by further LLM calls. Text limits this memory in two ways. It is updated one rewrite at a time, so exploiting the full interaction history is prohibitively expensive; and collaborative evidence, graded similarity over an entire catalog, does not survive translation into sentences. We propose CoVeMem (Co...
  </details>

- **2026-08-27** — Chenyang Wu, Fuchen Long, Binyuan Huang et al. — [Thinking on Shots: Consistent Multi-Shot Video Editing with Agentic Reasoning](http://arxiv.org/abs/2608.26809v1)
  <details><summary>📄 Abstract</summary>
  While generative AI has significantly advanced video editing, existing methods primarily focus on single-shot or short video clips. Editing long videos with multiple instructions remains a formidable challenge. Naive chunking strategies, e.g., fixed-duration segmentation, often lead to entity fragmentation, severe editing hallucinations, and disrupted temporal continuity. To bridge this gap, we introduce the Multi-Instruction Multi-Shot Long-Video Editing (MMLVE) task, which is structured around...
  </details>

- **2026-08-27** — Yiwei Lu, Ke Xu, Tao Yan et al. — [Glass Surface Detection Grounded in 3D Visual Geometry](http://arxiv.org/abs/2608.26752v1)
  <details><summary>📄 Abstract</summary>
  Glass surface detection (GSD) is critical for scene understanding and reconstruction, and yet remains challenging due to the transparency and reflectivity of glass surfaces. Existing GSD methods typically rely on 2D appearance cues, which may fail in geometrically ambiguous scenes. In this paper, we propose a paradigm shift: grounding GSD in 3D visual geometry to explicitly model the physical existence of glass surfaces. Our method first distills rich 3D priors from the visual geometry grounded ...
  </details>

- **2026-08-27** — Zeming Liu, Hang Lyu, Jingtao Zhang — [FaultLens: Learning Compact Behavioral Test Suites for Generated Operational Programs](http://arxiv.org/abs/2608.26746v1)
  <details><summary>📄 Abstract</summary>
  Generated operational programs are often validated with either a few hand-written examples or exhaustive regression suites. The former can miss sparse boundary and interaction faults, while the latter can be unnecessarily expensive. We introduce FaultLens, a method for learning compact behavioral test suites while preserving an auditable connection to executed evidence. It executes a rich probe domain once, stores the fault-probe kill relation as a sparse outcome cache, and learns probe ordering...
  </details>

- **2026-08-27** — Yuhao Liu, Yingnan Zhou, Weijie Liu et al. — [KubeCap: A Framework for Capability Minimization in Kubernetes via Static Analysis and LLM-Assisted Rule Inference](http://arxiv.org/abs/2608.26699v1)
  <details><summary>📄 Abstract</summary>
  As the most widely used container orchestration platform, Kubernetes provides flexible privilege configuration by allowing developers to manage Linux capabilities via manifest files. However, developers rely on default settings or coarse-grained security contexts in practice, violating the principle of least privilege and enlarging the attack surface of containerized workloads. Existing studies either detect vulnerable patterns in Kubernetes manifests or infer required capabilities for standalon...
  </details>

- **2026-08-27** — Kumju Jo, Heesun Jung, Sungyong Baik — [Text-to-seed generation: Training-free open-vocabulary seeded semantic segmentation via re-purposing diffusion as text-guided seed generator](http://arxiv.org/abs/2608.26624v1)
  <details><summary>📄 Abstract</summary>
  Open-vocabulary semantic segmentation (OVSS) aims to segment image regions corresponding to arbitrary text queries. Although the Segment Anything Model (SAM) is a powerful foundation model for segmentation, its standalone performance on OVSS remains limited. Existing methods therefore often use SAM to refine coarse masks predicted by other models, but this strategy is unreliable when the initial masks are inaccurate. In this work, we argue that more reliable segmentation can be achieved by explo...
  </details>

- **2026-08-27** — Ziquan Liu, Zhewei Zhu, Xuyang Shi — [FAN-LoRA: A Fourier-Adaptive Nonlinear Low-Rank Adaptor for Medical Foundation Model Domain Adaptation](http://arxiv.org/abs/2608.26531v1)
  <details><summary>📄 Abstract</summary>
  The advent of vision foundation models, notably the Segment Anything Model (SAM), has catalyzed significant advancements in natural image segmentation. However, their direct transfer to medical imaging remains severely bottlenecked by profound domain gaps, such as cross-modality and cross-center shifts. Existing Parameter-Efficient Fine-Tuning (PEFT) methods facilitate the adaptation of SAM to medical domains; nevertheless, they frequently suffer from performance degradation under severe distrib...
  </details>

- **2026-08-27** — Xingbang He, Yuanwei Chen, Yi Qian et al. — [When Context Gets Root: Privilege Escalation in LLM Harnesses](http://arxiv.org/abs/2608.27299v1)
  <details><summary>📄 Abstract</summary>
  Instruction hierarchy is a model-side defense that assigns instructions different levels of privilege according to their sources. These levels constrain which content may direct model behavior. During agent execution, however, agent harnesses construct context for each model invocation. This construction can elevate low-level content to a higher instruction level and grant it greater model-facing privilege. We introduce instruction privilege escalation. In this attack, an attacker induces an age...
  </details>

- **2026-08-27** — Yitian Zhou, Jingyu Zheng, Qiliang Jiang et al. — [PLCBench: Can Autonomous LLM Agents Turn PLC Access into Sustained Physical Impact?](http://arxiv.org/abs/2608.26882v1)
  <details><summary>📄 Abstract</summary>
  Industrial control systems (ICSs) rely on programmable logic controllers (PLCs) to connect networked computation with physical control. Tool-using large language model (LLM) agents represent an emerging attack threat: can an autonomous agent convert a network-reachable PLC into sustained adverse physical impact? However, existing evaluations focus on digital tasks or individual stages of PLC testing. In ICSs, evaluations that stop at software exploitation, an accepted write, or tool access may t...
  </details>

- **2026-08-27** — Jin Mu, Guanhua Chen — [Making Clinical Language Models Auditable: Concept-Guided Fine-Tuning for Robust Prediction](http://arxiv.org/abs/2608.27397v1)
  <details><summary>📄 Abstract</summary>
  Clinical language models can achieve strong in-hospital accuracy yet fail under deployment shifts because they exploit note-specific artifacts (e.g., templates, separators, boilerplate) that do not reflect patient state. We propose CAST (Concept-guided Artifact Suppression Tuning), an SAE-based framework for auditable clinical text classification. CAST uses Sparse Autoencoders to expose sparse, human-auditable features from intermediate Transformer activations, labels SAE latents with an LLM-ass...
  </details>

- **2026-08-27** — Jinghan Zhang, Fengran Mo, Zhiyu Chen et al. — [BrailleBench: Investigating Multi-Criteria Braille Comprehension in Large Language Models](http://arxiv.org/abs/2608.27268v1)
  <details><summary>📄 Abstract</summary>
  Although Large language models (LLMs) mediate access to knowledge and computational assistance, their capabilities should benefit vulnerable groups in the same way. However, it is unclear whether existing AI systems are inclusive enough for blind and deafblind users to access the same functionality through Braille, whose indicators, contractions, and digital representations introduce distinct requirements for model comprehension. To this end, we introduce BrailleBench, a benchmark for evaluating...
  </details>


### 📂 defense
*防御与防护方法 / Defense & Protection Methods* — 59 papers

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

- **2026-08-30** — Sagar Srinivas Sakhinana, Venkataramana Runkana — [Forward-Deployed Full-Stack Engineering for Autonomous Cloud MLOps](http://arxiv.org/abs/2608.29615v1)
  <details><summary>📄 Abstract</summary>
  Across industries, machine-learning systems support applications ranging from prediction and anomaly detection to forecasting, optimization, and scheduling, yet operationalizing these systems requires coordinating application development, model pipelines, cloud infrastructure, security, deployment, monitoring, retraining, recovery, and rollback. We present an evidence-gated multi-agent framework for transforming a natural-language MLOps cloud engineering task into a verified repository and opera...
  </details>

- **2026-08-30** — Yusuke Hirota, Michael Ross Boone, Arun George Zachariah et al. — [Guardrail-Agnostic Societal Bias Evaluation in Large Vision-Language Models](http://arxiv.org/abs/2608.29590v1)
  <details><summary>📄 Abstract</summary>
  We propose a societal bias evaluation method for large vision-language models (LVLMs) in the era of strong safety guardrails. Existing benchmarks rely on prompts that ask models to infer attributes of people in images (e.g., "Is this person a CEO or a secretary?"). However, we find that LVLMs with strong guardrails, such as GPT and Claude, often refuse these prompts, making evaluations unreliable. To address this, we change the prior evaluation paradigm by decoupling the task from the depicted p...
  </details>

- **2026-08-30** — Tian Yu, Lu Feng, Sebastian Elbaum — [Drive the Thoughts: Runtime Monitoring of VLA Reasoning-Trajectory Consistency](http://arxiv.org/abs/2608.29583v1)
  <details><summary>📄 Abstract</summary>
  Autonomous vehicles (AVs) operate in complex environments where failures are consequential. Sophisticated machine learning models for perception and planning are key to overcoming at least part of that complexity, but their black-box nature complicates validation and verification (V&V). The recent integration of Vision-Language-Action (VLA) models into AVs introduces a unique opportunity: besides generating trajectories, these models produce an explicit Chain-of-Thought (CoT) explaining their un...
  </details>

- **2026-08-30** — Junbin Lu, Hsiang-Wei Huang, Saesha Wadhwa et al. — [SpatialTrust: A Benchmark for Environmental Risk Recognition in Secure Authentication](http://arxiv.org/abs/2608.29489v1)
  <details><summary>📄 Abstract</summary>
  Visual environmental risk recognition plays an important role in secure authentication, where a user's surroundings may reveal sensitive information or introduce potential security risks. However, existing evaluations of multimodal large language models (MLLMs) rarely examine whether models can reliably recognize, localize, and explain such risks in spatially grounded authentication scenarios. We present SpatialTrust, a question-answering benchmark for evaluating environmental risk recognition i...
  </details>

- **2026-08-30** — Weifei Chen, Honghao Zhang, Zhiyuan You et al. — [InspectorGPT: A Comparative Reasoning Enhanced VLM for Comprehensive Industrial Anomaly Detection](http://arxiv.org/abs/2608.29783v1)
  <details><summary>📄 Abstract</summary>
  Industrial anomaly detection is a critical component of modern manufacturing. Most traditional unsupervised methods rely on modelling normal feature distributions, inherently limiting generalization to unknown categories. To improve generalizability, some recent methods incorporate vision-language models (VLMs) for zero-shot detection via text prompts. However, we observe that reasoning-oriented post-training can cause anomaly discrimination to collapse, with some fine-tuned models performing wo...
  </details>

- **2026-08-30** — Junyan Zhang, Yudong Zeng, Yongwei Huang et al. — [SemTrace: Source-Grounded Semantic Signatures for Tracing LLM Exposure to Protected Documents](http://arxiv.org/abs/2608.29575v1)
  <details><summary>📄 Abstract</summary>
  Large language models are increasingly used to read documents and produce downstream text, creating a provenance problem when the document owner cannot control or inspect the model that performs the generation. We introduce SemTrace, a source-grounded semantic watermark for detecting whether a generated review was influenced by a known protected manuscript copy. Rather than biasing token probabilities or imposing surface-form patterns, SemTrace constructs a document-specific binary signature fro...
  </details>

- **2026-08-29** — Jinzhe Li, Gengxu Li, Jinnan Li et al. — [MMPCBench: Benchmarking Multimodal Large Language Models on Proactive Critique of Flawed Inputs](http://arxiv.org/abs/2608.29286v1)
  <details><summary>📄 Abstract</summary>
  As Multimodal Large Language Models (MLLMs) evolve into sophisticated interactive assistants, their reliability depends not only on following instructions but also on validating them. We define Proactive Critique as the model's autonomous ability to identify, analyze and fix faulty user inputs without extra prompts. However, evaluations mainly test models under ideal circumstances or simple refusal behaviors, largely ignoring active error processing. To fill this gap, we propose MMPCBench, a com...
  </details>

- **2026-08-29** — Qianqi Liu, Jin Huang, Fethiye Irmak Dogan et al. — [Benevolent Bias in Multi-Turn Human-Agent Dialogue](http://arxiv.org/abs/2608.29206v1)
  <details><summary>📄 Abstract</summary>
  Bias in human-agent interaction can manifest not only through hostile language but also as benevolent bias, whereby unequal treatment hides behind a warm, positive tone. To make it detectable, we operationalise benevolent bias along two dimensions, tone and treatment, yielding three classes: neutral support, overt bias, and benevolent bias. Building on these definitions, we construct BENEVDIAL, a class-balanced corpus of 362,880 multi-turn support dialogues spanning user and agent demographics, ...
  </details>

- **2026-08-29** — Zhang Enyan, R. Thomas McCoy — [A Unifying Perspective on Language Model Representations: From Filler-Role Structure to Mechanistic Interpretability](http://arxiv.org/abs/2608.29034v1)
  <details><summary>📄 Abstract</summary>
  A wide range of methods have been proposed for interpreting language models, delivering important insights into their inner workings. However, different methods and their resulting insights stand in relative isolation: what could the underlying structure of language models be, such that they give rise to all our interpretations? In this work, we propose using Tensor Product Representations (TPRs) as a unifying hypothesis. TPRs give a concrete proposal for how compositional structure could be rep...
  </details>

- **2026-08-29** — Cunhang Fan, Junqin Cao, Tian Gao et al. — [Beyond Speech: Dual-Domain SSL Fusion for Unified All-Type Audio Deepfake Detection](http://arxiv.org/abs/2608.29021v1)
  <details><summary>📄 Abstract</summary>
  Unified all-type audio deepfake detection aims to determine whether an input clip is real or fake when its audio type may be speech, environmental sound, singing voice, or music. Existing speech-centric or type-dependent solutions are insufficient for this setting because the test-time audio type is unknown, while the required output is still a single binary decision. To address these issues, this paper proposes a dual-domain SSL fusion method that maps heterogeneous audio into a shared binary a...
  </details>

- **2026-08-29** — Aryo Pradipta Gema, Neel Rajani, Rohit Saxena et al. — [Chain-of-Thought Faithfulness of Reasoning Models Varies with Where and How Preference Cues Are Delivered](http://arxiv.org/abs/2608.29464v1)
  <details><summary>📄 Abstract</summary>
  Chain-of-thought (CoT) monitoring assumes that reasoning traces faithfully record the information that shapes a model's answer. Existing faithfulness tests often place explicit bias cues in the user message, while agents may encounter preferences through tool returns or raw artifacts. We introduce FACE-Eval (Faithful Attribution of Cue Effects Evaluation), a 5,100-sample evaluation that varies cue location (user message or tool return) and explicitness (direct summary or raw artifact). We measur...
  </details>

- **2026-08-28** — Changze Li, Yutong Cheng, Tsania Camila Finnisa et al. — [BEACON: Behavior-Anchored Cross-Source Knowledge Graph Construction for Cyber Threat Intelligence](http://arxiv.org/abs/2608.28394v1)
  <details><summary>📄 Abstract</summary>
  Cyber threat intelligence (CTI) is foundational to modern cyber defense, yet much of it resides in unstructured reports whose volume and heterogeneity far exceed manual analysis, motivating research on automatically constructing knowledge graphs from CTI reports. However, existing approaches mainly extract partial information within a single report, leaving the cross-source setting unexplored, where the same threat is given unrelated names. Our key insight is that attack behaviors, once mapped t...
  </details>

- **2026-08-28** — S. Krishna, Kaushik Mallik, Abhilasha Sharma Suman — [Adaptive Strategies for GR(1) Games](http://arxiv.org/abs/2608.28391v1)
  <details><summary>📄 Abstract</summary>
  We consider two-player GR(1) games on graphs, where the system player Eve must satisfy \[ \Box\Diamond A_1\land\cdots\land\Box\Diamond A_m \;\implies\; \Box\Diamond G_1\land\cdots\land\Box\Diamond G_n \] against the environment player Adam. Here $A_1,\ldots,A_m$ are assumptions on the environment, $G_1,\ldots,G_n$ are guarantees the system must provide, and $\Box\Diamond S$ denotes ``always eventually $S$''. Traditional static strategies are overly conservative: they may actively violate assumpt...
  </details>

- **2026-08-28** — Abrar Alotaibi, Muhammad Shahid Jabbar, Sadam Al-Azani et al. — [Layered LLM Defenses as an Ensemble: Access Tiers, Inference Cost, and the Measured Failure Correlation Between Defense Layers](http://arxiv.org/abs/2608.28327v1)
  <details><summary>📄 Abstract</summary>
  Practitioners defend large language models (LLMs) by stacking defenses, assuming the layers compound. A stack is an ensemble, and ensembles compound only under a condition the LLM security literature recommends but never measures: the members must fail on different inputs.   Two instruments make that measurable. The Adversary Access-Tier Model (AATM) grades an adversary by the access it holds, from system-only (A0) to influence over training data (A4). A cost model sorts defenses into five class...
  </details>

- **2026-08-28** — Guipeng Xin, Jiahe Xu, Chenhui Wan et al. — [PanelShield: Verifiable Closed-Loop Safe Planning for Robotic Industrial Panel Operation](http://arxiv.org/abs/2608.28305v1)
  <details><summary>📄 Abstract</summary>
  Industrial panel operation is knowledge-intensive and safety-critical. Beyond control recognition and action generation, execution must satisfy constraints in operation manuals and safety regulations. While foundation-model-based planners show strong semantic capability, they typically lack computable, localizable, and reproducible mechanisms for violation detection and repair. To address this, we propose PanelShield, a verifiable closed-loop safety planning framework for manual-guided industria...
  </details>

- **2026-08-28** — Nan Li — [Acquire, Repair, Preserve: A Diagnosis-Guided Post-Training Recipe for Small-Model Dialogue Game Agents](http://arxiv.org/abs/2608.28458v1)
  <details><summary>📄 Abstract</summary>
  Interactive dialogue games test a capability that static benchmarks largely leave implicit: a model must carry state across turns, interpret feedback, and choose valid actions under changing constraints. We study this setting in the LM Playschool Challenge with a 2B open-weight model, and find that many failures are not only broad knowledge failures but also local decision failures: repeated guesses, malformed actions, and violations of feedback that the model has just seen. These diagnostics mo...
  </details>

- **2026-08-28** — Qing Ye, Meng-Hsuan Lin — [Fidelity Is Not Enough: Dispatch-Level Instrumentation for Agentic Datasheet Extraction](http://arxiv.org/abs/2608.28439v1)
  <details><summary>📄 Abstract</summary>
  One model passed our fidelity check without ever opening the datasheet. We found it while qualifying models for an internal extraction service: a structured-output constraint had silently disabled tool use, and the model answered anyway, with fabricated source text. Only the per-tool trace exposed it. Fidelity -- whether an extracted value matches the source -- is the standard measure for agentic document extraction, and it scores that run a success. We therefore log every tool call in an agenti...
  </details>

- **2026-08-28** — Marin Maletic, Marijana Peti, Tamara Petrovic et al. — [Spatial-Semantic Reasoning using Large Language Models for Efficient UAV Search Operations](http://arxiv.org/abs/2608.28270v1)
  <details><summary>📄 Abstract</summary>
  We present a real-time semantic navigation framework for Unmanned Aerial Vehicles (UAVs) focused on improving time efficiency in the Object Goal Navigation (ObjectNav) task. Central to our approach is a Large Language Model (LLM) that interprets user-provided natural language instructions and performs semantic reasoning over detected objects and spatial context to prioritize high-probability search regions. The system combines real-time object detection, 3D spatial mapping, and polynomial spline...
  </details>

- **2026-08-27** — Sven Hinderer, Jonathan Riese, Zheming Yin et al. — [Super-Resolution of Range-Doppler Maps: A Case Study with Chirp-Sequence Radar and Transformer](http://arxiv.org/abs/2608.27354v1)
  <details><summary>📄 Abstract</summary>
  Range-Doppler (rD) maps produced by chirp- sequence (CS) radar systems are fundamentally limited in reso- lution by bandwidth, carrier frequency, and coherent processing interval constraints. Improving resolution through hardware is often impractical due to regulatory, cost, and real-time operation requirements. In this work, we investigate deep learning-based super- resolution of rD maps in both range and Doppler using a real- world dataset collected with an Infineon millimeter-wave CS radar. W...
  </details>

- **2026-08-27** — Mesut Toruk — [BekchiAI: Measuring, Observing, and Controlling LLM Agents in One Click](http://arxiv.org/abs/2608.26867v1)
  <details><summary>📄 Abstract</summary>
  Large language model agents reason, call tools, and act autonomously over many steps, but their agentic skills-correctly sequencing tools, planning under dependencies, judging untrusted inputs, and grounding generated arguments-are hard to measure with accuracy-only leaderboards. We present BekchiAI, which addresses both sides: a benchmark for measuring agentic skill and a platform for observing and controlling live agents. The BekchiAI-Benchmark, a suite of 13 tool-using ReAct agents across 7 t...
  </details>

- **2026-08-27** — Siye Wu, Kai Yang, Yuchen Cai et al. — [Consolidating RLVR Capabilities Across Domains: A Deep Dive into Fusion Paradigms](http://arxiv.org/abs/2608.27409v1)
  <details><summary>📄 Abstract</summary>
  Reinforcement learning with verifiable rewards (RLVR) improves specific capabilities of large language models, but covering multiple capabilities often involves training separate domain experts and subsequently consolidating them. We organize three fusion paradigms by the artefacts they reuse: Merge combines expert task vectors, Mix RL pools their datasets, and multi-teacher on-policy distillation (MOPD) uses both. Because they have largely been studied in isolation, how they compare and how to ...
  </details>

- **2026-08-27** — Jackie Baek — [LLMs Can Design Near-Optimal OR Algorithms](http://arxiv.org/abs/2608.27296v1)
  <details><summary>📄 Abstract</summary>
  We ask whether large language models (LLMs) can design effective algorithms for well-specified operations research (OR) problems. We study inventory control, queueing network control, and assortment optimization. We evaluate two levels of LLM use: at level 1, the model receives one problem instance and returns a solution for that instance; at level 2, it receives only the problem class description and broad parameter ranges, and returns an algorithm that maps instance parameters to solutions. Hu...
  </details>

- **2026-08-27** — Dezheng Han, Anbang Zhang, Zhihao Zhu et al. — [Unifying Detection and Adaptation in Task-Free Continual Learning](http://arxiv.org/abs/2608.27070v1)
  <details><summary>📄 Abstract</summary>
  To mitigate catastrophic forgetting in downstream continual learning (CL) for large language models (LLMs), existing methods typically constrain parameter updates or introduce task-specific adaptation modules. However, these methods often rely on explicit task boundaries during training, limiting their applicability to realistic task-free scenarios. In this paper, we propose a \textbf{Fi}sher-guided \textbf{uni}fied (\textbf{FiUni}) framework for batch-level task detection and parameter-efficien...
  </details>

- **2026-08-27** — Haihan Li, Haihao Li, Zhenfei Xu et al. — [Order Matters: A Chinese Multi-Panel Meme Benchmark for Vision-Language Reasoning](http://arxiv.org/abs/2608.26866v1)
  <details><summary>📄 Abstract</summary>
  Many multimodal tasks depend on how visual elements are ordered and composed, not only on recognizing them in isolation. Internet memes are a compact case of this problem: their punchline often depends on a constrained reading order and cross-panel visual--textual cues. While large vision-language models (LVLMs) show strong performance on single-image understanding, it remains unclear whether they can perform sequence-aware reasoning over structured meme layouts, especially in Chinese social med...
  </details>

- **2026-08-27** — Rongjin Li, Yuanxin Liu, Hao Zhou et al. — [Not Just Reason, Not Just Scan: Reinforcement Learning for Proactive Scientific Error Verification over Academic Paper](http://arxiv.org/abs/2608.26596v1)
  <details><summary>📄 Abstract</summary>
  Multimodal large language models (MLLMs) are increasingly capable scientific assistants, yet they remain far from fully autonomous research. This transition requires models to actively inspect academic papers, build global evidence views, and make traceable judgments without prespecified issues or evidence. However, existing work provides limited task paradigms or training studies for such issue- and evidence-absent verification. We study this challenge through scientific error detection, where ...
  </details>

- **2026-08-27** — Haoyu Wang, Chi Zhang, Mafu Zhang et al. — [Current-Limiting Control for Fault Ride-Through of LLC-based Solid-State Transformer in Data Centers](http://arxiv.org/abs/2608.26595v1)
  <details><summary>📄 Abstract</summary>
  Solid-State Transformers (SSTs) are increasingly proposed as the interface between distribution grids and data centers due to flexible power flows and fast dynamic response. However, when a short-circuit fault occurs in a load branch, the SST with a voltage-source-type DC-DC stage is forced to shut down due to fault currents. Therefore, current-limiting strategies are strongly needed to prevent catastrophic equipment damage and cascading blackouts by instantly restricting massive current spikes ...
  </details>

- **2026-08-27** — Hongru Song, Ruqing Zhang, Jiafeng Guo et al. — [DeepRepro: State-Aware Subplanning for Paper-to-Code Reproduction in Evolving Repositories](http://arxiv.org/abs/2608.26557v1)
  <details><summary>📄 Abstract</summary>
  Recent advances in agentic large language models (LLMs) have enabled increasingly autonomous software engineering workflows, yet automatic machine learning (ML) paper-to-code reproduction remains a challenging long-horizon problem. Unlike conventional code generation, this task requires constructing and maintaining a fully functional repository whose state continuously evolves during execution. Existing systems typically rely on static upfront planning followed by sequential file-level generatio...
  </details>

- **2026-08-27** — Kal Backman, Jared Wood, Adam Roff — [Learning Woody Clearing With Loss Alignment for Zero-Shot Regrowth and Woody Segmentation](http://arxiv.org/abs/2608.26489v1)
  <details><summary>📄 Abstract</summary>
  Detecting woody clearing is vital for managing biodiversity. Deep learning models can detect change in woody vegetation from bitemporal remote sensing imagery, however generated products may not meet end-user specifications due to unaligned loss definitions. Further limitations of deep learning models are the reliance on large datasets which can be difficult to attain for spatially rare and ambiguous events such as regrowth detection. In this work we train a model to detect woody change using bi...
  </details>

- **2026-08-27** — Orion Reblitz-Richardson — [How Language Models Organize and Structure Moral Knowledge](http://arxiv.org/abs/2608.27402v1)
  <details><summary>📄 Abstract</summary>
  How do large language models (LLMs) organize moral knowledge? Models detect moral content broadly, but detection is a low bar. We ask whether they go further, distinguishing moral foundations from one another and organizing the relationships between them geometrically.   We train six independent linear probes on open-weight language models, one per Moral Foundations Theory (MFT) category (care/harm, fair/cheat, lib/oppress, loy/betray, auth/subv, sanc/degrade), and examine how the resulting dire...
  </details>

- **2026-08-27** — Dylan Girrens, Guangjing Wang — [SPA: Securing Persistent LLM Agents Across Queries with Plan-First Information-Flow Control](http://arxiv.org/abs/2608.27234v1)
  <details><summary>📄 Abstract</summary>
  Large language model (LLM) agents increasingly operate over untrusted webpages, documents, tools, and persistent states while exercising authority over security-sensitive resources. Existing defenses typically protect either planning or individual tool interactions, but persistent agents face a broader threat: attacker-controlled data can alter control flow, enter security-sensitive tool arguments, or compromise later queries. We present SPA, a plan-first architecture that secures planning, exec...
  </details>

- **2026-08-27** — Prachi Chaturvedi, Shahnawaz Ahmad, Ehsan Nowroozi et al. — [LAAF: A Layered Accountability Architecture Framework for LLM Applications](http://arxiv.org/abs/2608.27102v1)
  <details><summary>📄 Abstract</summary>
  Large Language Models (LLMs) operate in hospitals, courtrooms, banks, and public service desks, where fluent, confident outputs are treated as authoritative even when ungrounded or incorrect. When such an output contributes to harm, who is answerable, and through what mechanisms can responsibility be traced, explained, and acted upon? Following PRISMA guidance, five databases were searched from January 2022 to March 2026 against four review questions; of 4,512 records identified, 122 primary stu...
  </details>

- **2026-08-27** — Yingjie Zhang, Yuanbo Xie, Kai Chen — [The Guard That Cried Wolf: How Scary Words Make Agent Guardrails Refuse Legitimate Actions](http://arxiv.org/abs/2608.27009v1)
  <details><summary>📄 Abstract</summary>
  Agent guardrails are checks that approve or refuse each action before an LLM executes it. Sometimes they refuse requests that are genuinely safe. This over-safety blocks deployment when a guardrail refuses an authorized task. Evaluating over-safety is hard: at the boundary an authorized action resembles an unauthorized one, and the safe-versus-unsafe label is a choice of authorization policy, not fixed by the action alone. We argue it therefore requires a benchmark that does not yet exist, one t...
  </details>

- **2026-08-27** — Tianjie Ju, Zheng Wu, Yueqing Sun et al. — [UrbanGround: From Local Perception to Spatial Agency in a Real-Scale City](http://arxiv.org/abs/2608.27456v1)
  <details><summary>📄 Abstract</summary>
  Multimodal large language models (MLLMs) can interpret a street view, but urban agency depends on whether such local evidence remains useful after the agent starts to move. In this paper, we investigate how far current MLLM agents can turn local urban perception into reliable action in a complicated real-scale city. We propose UrbanGround, the first sandbox to make this question testable in a physically constrained replica of Hong Kong built from territory-wide 3D geospatial data. UrbanGround su...
  </details>

- **2026-08-27** — Yisen Xi — [Persona-Execution Separation: An Architecture Pattern for Evolving LLM Agents under Execution Audit](http://arxiv.org/abs/2608.27427v1)
  <details><summary>📄 Abstract</summary>
  Large language model (LLM) agents in governed organizations must let the persona (instructions, tone, self-presentation) evolve freely, while keeping execution (stateful, audited work) traceable. A single trust domain does not satisfy both cheaply. We present Persona-Execution Separation (PES): persona and execution reside in different trust domains, connected by a governed contract bridge. The persona is singly-homed and may drift; execution is faceless and audited. Status summaries may return;...
  </details>


### 📂 alignment
*对齐与安全约束 / Alignment & Safety Constraints* — 64 papers

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

- **2026-08-30** — Luwei Xiao, Xin Wang, Keane Ong et al. — [OmniClimate-TC: Physics-Aware Visual Abstractions for Multimedia Reasoning over Tropical Cyclones](http://arxiv.org/abs/2608.29661v1)
  <details><summary>📄 Abstract</summary>
  Meteorological reanalysis encodes extreme weather through continuous, physically constrained fields, posing a fundamental challenge for vision-language models (VLMs) whose perceptual assumptions are shaped by natural images. Tropical cyclones exemplify this mismatch: critical properties such as intensity extrema, asymmetry, spatial extent, and physical impacts arise from field-level organization rather than object-centric visual cues. Existing approaches address this gap through text alignment o...
  </details>

- **2026-08-30** — Hoseong Hwang, Woorim Han, Joungin Chun et al. — [Reward-guided Fine-Tuning of One-Step Generative Models via Wasserstein Gradient Flow](http://arxiv.org/abs/2608.29647v1)
  <details><summary>📄 Abstract</summary>
  To mitigate the time complexity of generative models, one-step generative models have recently emerged through direct mapping from noise to data in a single forward pass. However, the reward-guided fine-tuning method of one-step generative models remains largely unexplored. To address this, we consider one-step generators from an optimal transport view, investigating Wasserstein Gradient Flow (WGF) for modeling smooth and controlled distributional evolution in probability space. We then propose ...
  </details>

- **2026-08-30** — Chenghao Yang — [Beyond Surface Alignment: Grounding the Dynamics of Situational Understanding and Generative Control in LLMs](http://arxiv.org/abs/2608.29610v1)
  <details><summary>📄 Abstract</summary>
  The current alignment tuning paradigm for Large Language Models (LLMs) prioritizes surface-level behaviors -- fluency, safety, and tonal consistency. While effective for casual chat, this thesis argues that such surface alignment masks a lack of grounding, creating models that are stylistically confident but situationally brittle. We propose a framework of Grounded Alignment, analyzing how models process context (Input) and structure generation (Output), then aligning these grounded behaviors to...
  </details>

- **2026-08-30** — William Schroeder — [Argument-Aware Semantic Alignment of Normative Texts: A Toulmin-Based Neuro-Symbolic Approach](http://arxiv.org/abs/2608.29529v1)
  <details><summary>📄 Abstract</summary>
  Semantic alignment between specialized normative texts is challenging when equivalent requirements use different terms, syntax, and levels of abstraction. Lexical overlap, distributional embeddings, and semantic similarity capture topical relatedness but often miss the argumentative structure by which normative claims are supported, qualified, and justified. This paper asks whether explicit argument structure adds information complementary to neural semantics for aligning requirements. We treat ...
  </details>

- **2026-08-30** — Kyungdon Lee, Wei Xu, Alan Ritter et al. — [CoCoA: Context-Conditional Cultural Alignment for Large Language Models](http://arxiv.org/abs/2608.29492v1)
  <details><summary>📄 Abstract</summary>
  Large Language Models (LLMs) often favor Western-associated entities across cultural contexts. Conventional debiasing methods aim for uniform neutrality, but cultural bias mitigation demands context-conditional behavior, preferring culturally appropriate entities when cultural cues are present and remaining neutral when they are absent. We propose CoCoA (Context-Conditional Cultural Alignment), a framework that learns this behavior through dual-context training on the same entity pairs under con...
  </details>

- **2026-08-30** — Kun Fang, Ziyu Wang, Ichiro Fujinaga — [What Are You Listening to? Temporal Music Grounding for Audio-to-Text Large Language Models](http://arxiv.org/abs/2608.29480v1)
  <details><summary>📄 Abstract</summary>
  Large audio-language models can produce fluent and musically plausible responses, yet it often remains unclear whether those responses are grounded in the audio input. We introduce temporal music grounding, a task in which a model returns one or more time spans corresponding to a queried musical note, event, or pattern. To evaluate this capability, we present MusicGroundingBench, a controlled benchmark suite built by rendering algorithmically generated piano MIDI to audio, yielding exact symboli...
  </details>

- **2026-08-29** — Matin Mahmood, Antonio Rueda-Toicen, Mohamed ElBassat et al. — [Hyper3-CLIP: Hierarchy-Conditioned Hyperbolic Vision-Language Training](http://arxiv.org/abs/2608.29313v1)
  <details><summary>📄 Abstract</summary>
  CLIP-like vision-language models (VLMs) trained with contrastive objectives learn strong global image-text representations, but their Euclidean embeddings and global pooling fail to encode relational structure such as part-whole and parent-child relations. Hyperbolic VLMs address this gap with entailment-based objectives, and text-conditioned variants improve fine-grained alignment through sentence- and phrase-level queries. However, these two lines of work remain separate: hyperbolic VLMs use s...
  </details>

- **2026-08-29** — Hojae Han, Jongyoon Kim, Sanghyuk Park et al. — [SHADOWBENCH: Toward Reliable Automatic Evaluation of Semantic Alignment in Autoformalization](http://arxiv.org/abs/2608.29270v1)
  <details><summary>📄 Abstract</summary>
  Autoformalization translates informal mathematical theorems into code for proof assistants such as Lean. A central challenge is that current evaluation metrics can accept type-correct but misaligned statements or reject correct statements written in a different formulation. Inspired by Pass@$k$, we propose SA-Pass (*Semantic Alignment Pass*), which tests formal statements using auxiliary statements called *shadows* that characterize the intended statement. A generated statement receives full cre...
  </details>

- **2026-08-29** — Haoru Tan, Sitong Wu, Yanfeng Chen et al. — [Dynamic Important Example Mining for Reinforcement Finetuning](http://arxiv.org/abs/2608.29252v1)
  <details><summary>📄 Abstract</summary>
  Reinforcement fine-tuning (RFT) is increasingly used to strengthen the reasoning abilities of large models, yet its effectiveness is bound by how training data are selected and used. Most data-centric RFT methods rely on static or heuristic sample selection, implicitly assuming a sample's value is fixed over training. This overlooks the non-stationary dynamics of policy learning and can lead to suboptimal updates. We propose Dynamic Important Example Mining (DIEM), a principled and fully automat...
  </details>

- **2026-08-29** — Haozhen Wei, Chengjun Jiang, Yutong Guo et al. — [SGPDFuse: Semantically-Guided Physics-Disentanglement General Multi-Modal Image Fusion](http://arxiv.org/abs/2608.29220v1)
  <details><summary>📄 Abstract</summary>
  Multimodal image fusion (MMIF) aims to integrate complementary sensor data into a single representation that preserves intrinsic scene reality while eliminating environmental interferences. Most existing approaches rely on blind feature aggregation, which excels at signal accumulation but fails to distinguish essential content from physical degradations. We propose SGPDFuse, which bridges this gap by mapping inputs into a physics-disentangled structural representation via a Semantic-Physical Par...
  </details>

- **2026-08-29** — Millicent Ochieng, Felermino D. M. A. Ali, Elizabeth A. Ankrah et al. — [Toward Cultural Alignment: Human-Centered Evaluation of Multimodal AI Stories Across Five African Communities](http://arxiv.org/abs/2608.29209v1)
  <details><summary>📄 Abstract</summary>
  In this paper, we examine how well AI-generated multimodal stories align with the lived practices, relationships, language, values, and visual expectations of the communities they represent. We conduct a community-grounded mixed-methods evaluation with 19 culture representatives across five African communities, combining quantitative annotations with qualitative focus group discussions. We find that cultural alignment depends not simply on recognizable cultural markers, but on how those markers ...
  </details>

- **2026-08-29** — Boyu Cai, Li Yang, Yan Xu et al. — [Dynamic-Robust Photometric-Semantic Reconstruction for Open-Vocabulary 3D Scene Understanding](http://arxiv.org/abs/2608.29177v1)
  <details><summary>📄 Abstract</summary>
  The integration of novel view synthesis (NVS) and open-vocabulary segmentation (OVS) has recently yielded powerful feed-forward 3D foundation models. However, their inherent reliance on static-scene assumptions leads to severe misalignment of spatial features in unconstrained dynamic environments. To bridge this critical gap, we propose SPAR, a novel joint semantic-geometric encoding architecture that explicitly isolates transient dynamic noise prior to latent space aggregation. Furthermore, we ...
  </details>

- **2026-08-29** — Zijie Zhang, Tan Lee, Yong Cao et al. — [Toward a Cross-Lingual Romanization Ecosystem for Sinitic Languages: A Paired Mandarin-Cantonese Case Study](http://arxiv.org/abs/2608.29170v1)
  <details><summary>📄 Abstract</summary>
  This paper proposes the Sinitic Romanization Ecosystem, a cross-lingual Sinitic romanization design framework with supporting digital infrastructure and a community-driven open-source workflow. The design framework addresses the lack of systematic cross-lingual romanization alignment among Sinitic languages through four design principles: phonetic correspondence for representing similar sounds with similar romanized symbols, historical-phonological correspondence for aligning cognate romanizatio...
  </details>

- **2026-08-29** — Han Wang, Yuxuan Liu, Yuhan Sun et al. — [Efficient Language-to-Vision Feature Injection for Referring Single-Object Tracking](http://arxiv.org/abs/2608.29126v1)
  <details><summary>📄 Abstract</summary>
  Referring single-object tracking enables language-grounded target initialization and subsequent tracking by jointly leveraging semantic cues and visual templates. The core difficulty is to use language differently across stages: it is indispensable for grounding but can induce semantic drift during tracking when overemphasized. Meanwhile, current methods often require costly vision-language alignment training. We present LVTrack, a pure transformer framework that introduces a mode-conditioned Ga...
  </details>

- **2026-08-29** — An Duy Nguyen, Muhammad Aurangzeb Ahmad — [Measurement Validity in LLM Cultural Alignment](http://arxiv.org/abs/2608.29266v1)
  <details><summary>📄 Abstract</summary>
  Researchers increasingly treat LLM survey responses as a proxy for human cultural values. This includes projecting model outputs onto instruments like the Inglehart-Welzel Cultural Map and drawing conclusions about which cultures a model resembles. While a model's answer to a value-laden questions may be interpreted as a cultural signal, it also carries sampling noise and, can be quite sensitive to question framing. In this paper, we separate survey responses, sampling noise and question framing...
  </details>

- **2026-08-28** — Huseyin Umut Isik, Mehmet Alp Ozaydin, Sila Kurugol et al. — [ARC-CT: Anatomy-Routed Contrastive Vision-Language Learning for 3D Chest CT](http://arxiv.org/abs/2608.28455v1)
  <details><summary>📄 Abstract</summary>
  Contrastive vision-language learning uses paired chest CT volumes and radiology reports to learn abnormality classifiers without manually annotated labels. However, two characteristics of chest CT challenge conventional global contrastive learning. First, many critical abnormalities are small or anatomically localized, and pooling an en- tire volume into a single embedding may dilute their visual evidence. Second, the standard contrastive objective treats every other scan in a batch as a negativ...
  </details>

- **2026-08-28** — Shihang Yang, Sanwoo Lee, Ningning Zhao et al. — [A Unified Framework to Elicit Structured Feedback for Interpretable Multi-Trait Essay Scoring](http://arxiv.org/abs/2608.28407v1)
  <details><summary>📄 Abstract</summary>
  Multi-trait Automated Essay Scoring (AES) requires rubric-grounded reasoning across interdependent traits, rather than isolated score prediction. Existing feedback-enhanced methods often decouple feedback from scoring or assess traits independently, weakening score--feedback consistency and rubric alignment. We propose HiFTS, a unified autoregressive framework that generates hierarchical CoT feedback before predicting trait-level and holistic scores. HiFTS distills rubric-grounded hierarchical C...
  </details>

- **2026-08-28** — Yupeng Zhang, Liuyuan Jiang, Hongyi Huang et al. — [RetailAgent: Structured Adverse Timing in Self-Conditioned Multimodal LLM Trading Agents](http://arxiv.org/abs/2608.28399v1)
  <details><summary>📄 Abstract</summary>
  In financial markets, a sequential policy that reacts systematically to price movements may become predictable to other market participants. This paper studies whether large language model (LLM) agents exhibit such directional structure through RetailAgent, an experimental framework in which an LLM observes anonymized intraday equity price histories and permitted state, then repeatedly chooses long (hold the stock) or flat (stay out) before the subsequent interval return is revealed. We compare ...
  </details>

- **2026-08-28** — Hefan Zhang, Bingquan Zhang, Ming Cheng et al. — [When Linguistic and Internal Confidence Diverge in Large Language Models](http://arxiv.org/abs/2608.28382v1)
  <details><summary>📄 Abstract</summary>
  Users often ask large language models (LLMs) to report how confident they are, but it is unclear whether such linguistic confidence tracks the model's internal confidence. We study this question across 8 classification tasks, 2 generation tasks and 30 models from three families. For classification, we compare linguistic confidence with logits-based confidence along three axes: association, magnitude agreement and calibration. For generation, we test whether linguistic confidence tracks semantic-...
  </details>

- **2026-08-28** — Pengze Li, Cui Tao — [AGENT-O: A Semantic Agent Card Framework for Interoperable and Governed Healthcare AI Agents](http://arxiv.org/abs/2608.28345v1)
  <details><summary>📄 Abstract</summary>
  AGENT-O is a modular ontology framework that defines a semantic Agent Card for representing health-oriented AI agent systems and supports assessment of reporting completeness in scientific publications. AGENT-O was developed as an OWL 2/RDF ontology covering runtime, models, workflow, tools, clinical use, evaluation, provenance, governance, and reporting assessment. Evaluation included ontology inventory, OWL-RL reasoning, three SHACL suites, 12 SPARQL competency queries, three cases, and model-...
  </details>

- **2026-08-27** — Gauthier Miralles, Loic Le Folgoc, Vincent Jugnon et al. — [Unsupervised Adaptation of 3D CT Foundation Models for 3D CBCT Segmentation](http://arxiv.org/abs/2608.27190v1)
  <details><summary>📄 Abstract</summary>
  Accurate 3D segmentation of cone-beam CT (CBCT) is critical for interventional and radiation therapy applications, yet it remains limited by two compounding challenges: the scarcity of annotated CBCT data and the large domain shift from diagnostic CT. Interventional CBCT exhibits fundamental modality differences from conventional CT, driven by acquisition and physics effects as well as contrast-specific vascular content, thereby limiting effective cross-modality model transfer. We propose a nove...
  </details>

- **2026-08-27** — Yichen Dong, Hao Wang, Junhui Li et al. — [STAR : Sentence Translation Alignment Rate for Document-to-Document Machine Translation](http://arxiv.org/abs/2608.27161v1)
  <details><summary>📄 Abstract</summary>
  Large Language Models (LLMs) have enabled a shift from sentence-level to document-to-document (Doc2Doc) machine translation, promising improved global coherence. However, document-to-document generation in a single pass frequently suffers from structural misalignment, manifesting as sentence omissions or hallucinations that violate the core requirement of source-target correspondence. To address this, we introduce Sentence Translation Alignment Rate (STAR), an auxiliary metric that explicitly qu...
  </details>

- **2026-08-27** — Jingyi Zheng, Yule Liu, Zifan Peng et al. — [TransMeme: A Multi-Agent Framework for Cross-Cultural Meme Transcreation](http://arxiv.org/abs/2608.27127v1)
  <details><summary>📄 Abstract</summary>
  Internet memes are a pervasive form of multimodal online communication; however, such communication often involves users from diverse linguistic and cultural backgrounds. Therefore, adapting memes across cultures and languages is a central challenge for enabling mutual understanding in online communication. Unlike ordinary translation or standalone text rewriting, cross-cultural meme transcreation must jointly preserve communicative intent, adapt culture-dependent meaning for the target audience...
  </details>

- **2026-08-27** — Hengyuan Xu, Wei Cheng, Yumeng Ji et al. — [Aphanta: Diagnosing Task-Aligned Image-Edited Intermediates for Multimodal Reasoning](http://arxiv.org/abs/2608.26993v1)
  <details><summary>📄 Abstract</summary>
  Explicit visual intermediates can help multimodal large language models (MLLMs) externalize spatial evidence and updated visual states, but their utility depends on whether an image editor can faithfully realize the required transformation. We introduce \textbf{Aphanta}, an automated task-discovery and closed-loop diagnostic framework for the MLLM -> image editor -> MLLM pipeline. Aphanta evaluates three conditions---direct reasoning, reasoning with an editor-generated intermediate, and reasonin...
  </details>

- **2026-08-27** — Shiyi Zhang, Mushui Liu, Yunze Tong et al. — [Self-OPD: On-Policy Distillation for Flow Matching Models without Teacher](http://arxiv.org/abs/2608.26872v1)
  <details><summary>📄 Abstract</summary>
  On-policy distillation (OPD), which leverages a pre-trained, specialized teacher model to provide dense supervisory signals, has achieved significant success in Large Language Models (LLMs) and has recently been adapted to flow matching models. However, this paradigm suffers from two major issues: First, training a separate, task-specific teacher for every new objective incurs high computational costs. Second, the discrepancy between teacher and student distributions often leads to compounding e...
  </details>

- **2026-08-27** — Jean-Daniel de Ambrogi, Aladine Chetouani, Vincent Nguyen et al. — [CGS-SLAM: Collaborative Gaussian Splatting based SLAM for Multi-Agent Reconstruction](http://arxiv.org/abs/2608.26868v1)
  <details><summary>📄 Abstract</summary>
  Recent advances in SLAM have leveraged 3DGS for photorealistic reconstruction and novel view synthesis. However, most methods rely on RGB-D input, which is unavailable on consumer-grade smartphones, and few integrate 3DGS within a collaborative framework. Therefore, we present CGS-SLAM, a hybrid decentralized/centralized system enabling multi-agent 3DGS SLAM using only RGB and inertial data. Each agent performs local tracking with inertial data as a motion prior and reconstructs a scaled map usi...
  </details>

- **2026-08-27** — Haowen Gu, Gensheng Pei, Zeren Sun et al. — [MedFG-VQA: Low-Frequency Memory and Graph Attention for Lightweight Medical VQA](http://arxiv.org/abs/2608.26848v1)
  <details><summary>📄 Abstract</summary>
  Medical Visual Question Answering (Med-VQA) holds significant promise for clinical decision support, yet faces challenges due to limited annotated data and the high computational demands of existing large vision-language models. We propose MedFG-VQA, a lightweight framework that leverages a memory bank to augment DCT-based low-frequency features and employs graph-enhanced cross-attention for effective visual-textual alignment. Specifically, our approach features two key components: Frequency-Mem...
  </details>

- **2026-08-27** — Muyao Yuan, Muyan Jiao, Jiangyong Ying et al. — [LLaVAFlow: Preserving Latent Alignment Flow for Parameter-Efficient Multimodal Fine-Tuning](http://arxiv.org/abs/2608.26820v1)
  <details><summary>📄 Abstract</summary>
  While Multimodal Large Language Models (MLLMs) exhibit strong generalization, visual instruction tuning for downstream tasks inevitably causes catastrophic forgetting, impairing overall generalization. While existing methods regulate weight updates to reduce forgetting, they overlook the fundamental cross-modal alignment in MLLMs. Based on prior work and our observations, we argue that cross-modal alignment is implicitly captured in the information-compression trajectory. To preserve the alignme...
  </details>

- **2026-08-27** — Seohyeong Lee, Hwaran Lee, Buru Chang — [Instruction Quality Matters: Refining Instructions for Effective Preference Learning](http://arxiv.org/abs/2608.26779v1)
  <details><summary>📄 Abstract</summary>
  Preference learning optimizes models using response pairs, yet the informativeness of these pairs is fundamentally shaped by the instructions from which they are generated. We identify instruction quality as a hidden bottleneck in preference learning: low-quality or ambiguous instructions restrict the response-quality distribution, limiting strong chosen responses and weakening preference signals. Through Best- and Worst-of-N analyses, we show that instruction quality constrains both the ceiling...
  </details>

- **2026-08-27** — Abhigya Verma, Amit Kumar Saha, Seganrasan Subramanian et al. — [AgentJudgeBench: A Multi-Difficulty Benchmark for Evaluating LLM Judges on Agentic Tool-Calling](http://arxiv.org/abs/2608.26623v1)
  <details><summary>📄 Abstract</summary>
  LLM judges are widely used to evaluate agentic tool-calling systems, yet their reliability on structured, dependency-driven workflows remains largely unexamined. We present AgentJudgeBench, the first benchmark to systematically study LLM-as-a-judge reliability for agentic tool-calling over workflow DAGs, as distinct from the broader LLM-as-a-judge task of open-ended text or preference evaluation. The benchmark comprises 3,808 instances spanning six DAG topologies and three difficulty tiers, eval...
  </details>

- **2026-08-27** — Saksham Khatwani, He Cheng, Majid Afshar et al. — [Surgical Alignment in Knowledge Graph Training for Clinical Diagnosis with Large Language Models](http://arxiv.org/abs/2608.26587v1)
  <details><summary>📄 Abstract</summary>
  Biomedical knowledge graphs (KGs) offer structured medical knowledge that can ground large language model (LLM) reasoning in clinical diagnosis application, yet how KG signal should be integrated into LLMs remains an open question. We present a systematic study spanning five KG task formulations, three training paradigms, two KGs, and three base LLMs. At the task level, all paradigms improve over the non-finetuned baseline, but methods with comparable in-domain accuracy show substantially differ...
  </details>

- **2026-08-27** — Haizhao Fan, Xinyi Le — [SAGE: Variate-Wise Semantic Augmentation for Vision-Language Time Series Forecasting](http://arxiv.org/abs/2608.26829v1)
  <details><summary>📄 Abstract</summary>
  Time series forecasting models operate on raw numerical sequences, lacking the semantic knowledge that domain experts implicitly leverage, such as the physical meaning of each variable, its statistical behavior, and its temporal dynamics. Recent efforts to bridge this gap fall into two camps. Some rely on large language models at inference time, which is computationally expensive. Others apply uniform textual prompts at the dataset level, ignoring the heterogeneous semantics across individual va...
  </details>


### 📂 robustness
*鲁棒性与可靠性 / Robustness & Reliability* — 63 papers

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

- **2026-08-30** — Yi Yu, Bo Wang, Chong Feng et al. — [SUP-MIMIC: A Multi-Task Clinical Diagnosis Benchmark for Evaluating LLMs' Robustness to Contradictory Evidence](http://arxiv.org/abs/2608.29582v1)
  <details><summary>📄 Abstract</summary>
  Current evaluations of large language models (LLMs) primarily focus on factual knowledge retrieval, overlooking the fundamental challenge of navigating the complex, non-bijective mappings between clinical indicators and diagnoses. Existing benchmarks fail to assess whether large language models truly possess the reasoning capability required for diagnostic ambiguity scenarios, where identical clinical presentations may correspond to different etiologies, and diagnostic convergence scenarios, whe...
  </details>

- **2026-08-30** — João L. P. Santana, Filipe R. Cordeiro — [Forget or Fine-tune? A Comparative Study of Machine Unlearning Strategies for Noisy Label Correction](http://arxiv.org/abs/2608.30046v1)
  <details><summary>📄 Abstract</summary>
  Noisy labels remain a critical challenge for training deep neural networks, since memorizing incorrect labels degrades generalization. Once noisy samples are identified after training, the standard solution is to retrain the model from scratch on the cleaned dataset, which is increasingly expensive as datasets and models grow. Machine Unlearning (MU) has recently emerged as a computationally efficient alternative, but the relative effectiveness of different MU strategies for noisy-label correcti...
  </details>

- **2026-08-30** — Hongyu Yu, Yifei Shen — [Budget-Aware Compression Pipeline for Single-GPU LLM Inference: Methods, Trade-offs, and Coupling Effects](http://arxiv.org/abs/2608.30076v1)
  <details><summary>📄 Abstract</summary>
  Single-GPU deployment of 70B-parameter language models on an NVIDIA GPU is constrained by device memory, long-context throughput, and engineering integration cost. We cast single-GPU inference as a budget-aware design problem over these three axes and study how pruning, quantization, and KV-cache compression interact under realistic execution. Controlled ablations show that layer-wise pruning makes weight quantization more robust. KV-cache sparsification complements INT8 KV quantization by reduc...
  </details>

- **2026-08-30** — Weixuan Xia — [Distribution-free testing of linear type](http://arxiv.org/abs/2608.30074v1)
  <details><summary>📄 Abstract</summary>
  We introduce a distribution-free goodness-of-fit test, termed the omega-1 test, which naturally complements the Kolmogorov--Smirnov test and Cramér--von Mises test and can be viewed as their (piecewise) linear analog. Defined as an $\mathrm{L}^{1}$-functional of the empirical process, the test statistic improves on balancing sensitivity to localized and diffuse alternatives and gives a robust and interpretable measure of distributional discrepancy, apart from close connections to the Wasserstein...
  </details>

- **2026-08-30** — Ruize Xu, Xiao Yu, Yujin Tang et al. — [How do World Models and Policies Compose in LLM Agents? A Joint Spectral and Behavioral Account](http://arxiv.org/abs/2608.30067v1)
  <details><summary>📄 Abstract</summary>
  How do LLM agents come to both understand environments they act in and master tasks set within them? Through controlled experiments combining world-model training (next-state prediction) and policy training (reward maximization), we investigate this question. We dissect the resulting models through their additive parameter updates. Geometrically, we find effective world-model updates are low-rank and share an input-feature subspace with policy updates while writing to nearly orthogonal output di...
  </details>

- **2026-08-30** — Jhen-Ke Lin — [Balance of Benchmarks: Semantic Density Reweighting for Benchmark Multiplicity and Task-Conditioned Evaluation](http://arxiv.org/abs/2608.30044v1)
  <details><summary>📄 Abstract</summary>
  Language models are commonly compared by averaging scores across a benchmark list with equal weight. Such lists grow through publication outside an explicit measurement design, so equal weighting turns the density of published benchmarks into an implicit capability weight: densely benchmarked regions count repeatedly. We introduce Balance of Benchmarks (BoB), which embeds benchmark descriptions and assigns each benchmark an inverse-density semantic weight. Nearby entries share aggregate influenc...
  </details>

- **2026-08-30** — Alexandre V. Delazeri, Gabriel E. Lima, Eduil Nascimento et al. — [Evaluating 2D and 3D-Aware Vision Foundation Models for Vehicle Attribute Recognition](http://arxiv.org/abs/2608.29929v1)
  <details><summary>📄 Abstract</summary>
  Vehicle attribute recognition is an important task in intelligent transportation systems, particularly when Automatic License Plate Recognition (ALPR) is unavailable or unreliable. Although vision foundation models have shown strong transferability across domains, their effectiveness for fine-grained vehicle classification remains underexplored. Moreover, given the inherently three-dimensional structure of vehicles, it is unclear whether emerging 3D-aware foundation models offer advantages over ...
  </details>

- **2026-08-30** — M. Tsukerman, K. Grotov, D. Vovchuk et al. — [Diffusion-Based Inverse Design of Dielectric Resonator Metasurfaces for Shaping Smart Electromagnetic Environments](http://arxiv.org/abs/2608.29907v1)
  <details><summary>📄 Abstract</summary>
  Future wireless systems are expected to transform the surrounding space from a passive propagation medium into a smart electromagnetic environment, where engineered surfaces control wave propagation, support wireless sensing, and create programmable electromagnetic fingerprints. A key challenge in realizing this vision is the inverse design of metasurfaces for tailored electromagnetic propagation. While forward analysis evaluates the response of a known geometry, the inverse task starts from a p...
  </details>

- **2026-08-30** — Abdolmehdi Behroozi, Chaopeng Shen — [Joint Spatiotemporal Spectral Neural Operators for Learning PDEs on Irregular Domains](http://arxiv.org/abs/2608.29892v1)
  <details><summary>📄 Abstract</summary>
  Learning solution operators for partial differential equations (PDEs) on irregular and geometry-dependent domains remains a central challenge in scientific machine learning. While spectral methods provide strong inductive biases for modeling global interactions, they are typically limited to regular domains, and existing neural approaches often require domain warping, interpolation, or costly geometric embeddings. We introduce the \textbf{Graph Spectral Neural Operator (GSNO)}, a neural operator...
  </details>

- **2026-08-30** — Ruihang Jiang, Zhaolin Wang, Yuanwei Liu — [KDGen-BF: A Generative Site-Specific Multi-User Beamforming Approach](http://arxiv.org/abs/2608.29838v1)
  <details><summary>📄 Abstract</summary>
  This paper proposes knowledge-distilled generative beamforming (KDGen-BF) framework for site-specific multi-user beamforming. KDGen-BF generates a multi-user beamforming weights from low-dimensional reference signal received power (RSRP) observations without acquiring instantaneous channel state information (CSI). To address the ambiguity caused by limited RSRP observations and interference coupling, KDGen-BF formulates multi-user beamforming as a conditional generation problem and directly outp...
  </details>

- **2026-08-30** — Md Raqib Khan, Santosh Kumar Vipparthi, Subrahmanyam Murala — [PhasorNet: Learning Structure from Frequency for Real-Time Stereo Matching](http://arxiv.org/abs/2608.29819v1)
  <details><summary>📄 Abstract</summary>
  Accurate stereo matching remains challenging in ill-posed regions such as fine structures, reflective, or transparent objects, where appearance cues are often ambiguous or unreliable. To tackle this, we propose PhasorNet, a lightweight yet powerful framework that boosts geometric discrimination via frequency-domain cues. At its core, the Phase-Augmented Transformer (PAT) injects Fourier-derived phase information into the attention mechanism, yielding photometrically robust, structure-preserving ...
  </details>

- **2026-08-30** — Yixing Li, Ruobing Xie, Yudong Zhang et al. — [Higher-Dimensional Rotary Position Embedding](http://arxiv.org/abs/2608.29715v1)
  <details><summary>📄 Abstract</summary>
  Transformers rely on position embedding mechanisms in long context modeling in most cases. Rotary Position Embedding (RoPE) embeds positional information with independent 2D rotations, forming relative position terms in self-attention. However, its pairwise, block-based, and decoupled structure limits deep mixing and robustness across channels. We propose HD-RoPE, which extends RoPE from independent 2D rotations to higher-dimensional rotations and introduces a Paley-I orthogonal basis to obtain ...
  </details>

- **2026-08-30** — Xinke Jiang, Yue Fang, Zhibang Yang et al. — [AgenticRag-R1: Agentic Reinforcement Learning with Stack Memory for Multi-Step Reasoning, Retrieval and Memorizing](http://arxiv.org/abs/2608.29622v1)
  <details><summary>📄 Abstract</summary>
  Retrieval-Augmented Generation (RAG) improves the factuality of large language models (LLMs), yet existing RAG systems often struggle with complex, multi-step reasoning that requires adaptive retrieval and continuous revision of intermediate contexts. Recent reinforcement learning (RL)-based agentic RAG methods partially alleviate this issue, but typically rely on coarse-grained action spaces and trajectory-level rewards, resulting in weak reward assignment and a bias toward short-horizon, stere...
  </details>

- **2026-08-30** — Xiaobing Dai, Zewen Yang, Wei Ren et al. — [Asynchronous Cooperative Online Learning for Multi-Robot Control under Computational Delays](http://arxiv.org/abs/2608.29562v1)
  <details><summary>📄 Abstract</summary>
  Ensuring the safe operation of multi-agent systems (MASs) under uncertain environments is crucial for cooperative robotic, where external disturbances and inaccurate dynamic models can significantly compromise performance and reliability. To address this challenge, calibrated machine learning models, particularly Gaussian process (GP) regression, are extensively employed due to their interpretable performance quantification. As the interconnected communication of MASs facilitates cooperative lea...
  </details>

- **2026-08-30** — Yanshan Zeng, Ruixuan Tu, Zuo Xiang et al. — [Towards Effective Generation of Interactive Visualizations with Vibe Coding: An Empirical Study](http://arxiv.org/abs/2608.29550v1)
  <details><summary>📄 Abstract</summary>
  Constructing interactive visualizations has traditionally required substantial human effort, involving both technical implementation and design decision-making. Recently, vibe coding, a programming paradigm leveraging Large Language Models to generate, interpret, and refactor code from natural language specifications, has emerged as a promising approach to reduce the burden. However, the capabilities and limitations of vibe coding in building interactive visualizations remain unexplored. To addr...
  </details>

- **2026-08-30** — Jason Luo, Saibilila Abudukelimu, Judy Song et al. — [MUDDLE: Measuring Understanding of Documents under Distractor and Length Effects](http://arxiv.org/abs/2608.29477v1)
  <details><summary>📄 Abstract</summary>
  Document question-answering systems increasingly answer questions over collections of retrieved documents rather than one clean source, so robustness to distracting context matters as much as reading ability. When such systems fail, it is often unclear whether the context was too long or the distractors were too close to the topic, because prior work tends to conflate these two effects. We present MUDDLE, a controlled benchmark that separates them. MUDDLE uses 270 human-annotated questions, each...
  </details>

- **2026-08-29** — Guanlong Wu, Dahui Li, Ke Jiang et al. — [Safe to Resume? Breaking Execution Continuity of Agent Execution via Rollback](http://arxiv.org/abs/2608.29381v1)
  <details><summary>📄 Abstract</summary>
  AI agents are moving toward persistent, stateful execution across various applications, accumulating execution state and external effects that are costly to reconstruct after failures. Checkpoint and rollback (C/R) are becoming essential for recovery, yet their security implications remain largely unexplored. Correct rollback does not imply secure recovery: a faithfully restored checkpoint may resume an execution whose states, assumptions, and external effects never coexisted in any valid histor...
  </details>

- **2026-08-29** — Yuxiong Wang, Ziwei Lin, Bo Wang et al. — [StageWell: A Process-Aligned Chinese Corpus for Positive-Psychology Support Dialogue](http://arxiv.org/abs/2608.29326v1)
  <details><summary>📄 Abstract</summary>
  Positive psychology dialogue aims to support emotional distress and positive resource building, requiring models to produce not only empathetic replies but also coherent progression through a multi-turn support process. Existing resources often reduce supervision to turn-level strategies or holistic preference labels, leaving process position, support function, and local repair targets implicit. We introduce StageWell, a process-aligned Chinese corpus for positive psychology dialogue, together w...
  </details>

- **2026-08-29** — Saransh Kumar Gupta, Armaan Shah, Lipika Dey et al. — [Validating FKG.in: Soundness Assessment in LLM-Augmented Indian Food Knowledge](http://arxiv.org/abs/2608.29249v1)
  <details><summary>📄 Abstract</summary>
  The online culinary ecosystem is increasingly populated by recipe content generated, modified, or summarized by Large Language Models (LLMs). While often plausible, such outputs may contain hallucinated ingredients, misrepresented quantities, or culturally implausible combinations, limiting their suitability for downstream applications and knowledge graph construction. In this paper, we present a semi-automated soundness assessment workflow for validating structured recipe data extracted and aug...
  </details>

- **2026-08-29** — Divya Khanure, Riti Gour†, Congzhou Li et al. — [RL-based Network Slice Embedding over Space Division Multiplexed Elastic Optical Networks](http://arxiv.org/abs/2608.29444v1)
  <details><summary>📄 Abstract</summary>
  Network slicing over space-division-multiplexed elastic optical networks (SDM-EONs) requires jointly managing spectrum, spatial cores, and compute resources, a coupling that many existing studies ignore by treating compute placement independently from routing and spectrum decisions. This disconnect can cause the spectrum to be allocated along a path, only for the request to fail due to insufficient compute resources along the path, or may result in compute resources being allocated without consi...
  </details>

- **2026-08-29** — Pedram MohajerAnsari, Amir Salarpour, Run Wang et al. — [GATE: Reliability-Gated Gaussian Evidence Fusion for Training-Free Test-Time Adaptation of Vision-Language Models](http://arxiv.org/abs/2608.29395v1)
  <details><summary>📄 Abstract</summary>
  Vision-language models such as CLIP and SigLIP provide strong zero-shot recognition, but their predictions can degrade when deployed on target data that differ from the pretraining distribution. Test-time adaptation offers a practical way to improve robustness without source data or target labels, yet existing methods often rely on either prompt-side adaptation or image-side target evidence alone. In this work, we introduce GATE, a training-free two-pass transductive test-time adaptation framewo...
  </details>

- **2026-08-29** — Marina Valdora, Víctor Yohai — [Robust estimation in generalized linear models based on the normal quantiles of the probability integral transformation](http://arxiv.org/abs/2608.29385v1)
  <details><summary>📄 Abstract</summary>
  A new approach to robust estimation in generalized linear models is introduced. The idea of the method is to first transform the responses applying the composition of the normal quantile function and the probability integral transformation. Then, using that the transformed responses should follow a standard normal distribution, find the values of the parameters that minimize a robust measure of their size. In practice an approximation of this transformation is used. The proposed estimators are s...
  </details>

- **2026-08-29** — Junxuan Li, Zijun Liu, Ziyi Huang et al. — [Learning Simple Test-Time Environments for LLM Web Agents](http://arxiv.org/abs/2608.29305v1)
  <details><summary>📄 Abstract</summary>
  Large language model (LLM) agents have demonstrated remarkable proficiency in manually constructed environments, yet their performance frequently collapses when transitioned to complex real-world settings. Existing research largely attribute this degradation to the compositional generalization gaps in LLMs on combinations of multiple simple, well-structured environments. In this work, we propose that LLM web agents can learn simple environment observations at test time. Specifically, we introduc...
  </details>

- **2026-08-29** — Zhaolu Kang, Meixin Wu, Yu Xue et al. — [Modality Fault Lines: Structural Corruptions Reveal Fragile Omni-Modal Reasoning](http://arxiv.org/abs/2608.29278v1)
  <details><summary>📄 Abstract</summary>
  Omni-modal large language models are increasingly evaluated on clean text--vision--audio inputs, where every channel is present, synchronized, and readily interpretable. Such scores are often taken as evidence of robust cross-modal fusion, but clean evaluation cannot tell whether success depends on stable cross-modal structure or on cues sufficient only in intact inputs. To address this gap, we define a modality fault line: a boundary at which model behavior becomes unstable when a modality rema...
  </details>

- **2026-08-29** — Yuwei Lou, Hao Hu, Yuzhou Jiang et al. — [RACER: Reinforced Agent Collaboration for Explainable Reasoning on Knowledge Graphs](http://arxiv.org/abs/2608.29263v1)
  <details><summary>📄 Abstract</summary>
  Large Language Models (LLMs) often suffer from hallucination and struggle with complex reasoning tasks requiring multi-hop domain knowledge. While integrating Knowledge Graphs (KGs) provides a structured and verifiable information source, current KG-enhanced LLM paradigms usually rely on single-agent path extraction and fixed prompting, lacking adaptability and facing huge search spaces. To address these challenges, we propose RACER, a Reinforced Agent Collaboration framework for Explainable Rea...
  </details>

- **2026-08-29** — Zachary Ellis, Spencer Hazel, Adam Brandt et al. — [When Patients Cut In: Extending Clinical Conversational AI Safety to Interruptions](http://arxiv.org/abs/2608.29241v1)
  <details><summary>📄 Abstract</summary>
  Clinical voice agents are now deployed in routine care, where real patients do not wait their turn: they interrupt. These systems typically use a cascaded architecture (speech-to-text -> LLM -> text-to-speech), so when a patient cuts the agent off mid-utterance, clinically required content can be lost even when the model handles cooperative transcripts well. Yet clinical conversational-AI benchmarks almost universally assume patients wait for the agent to finish, missing interruption-induced los...
  </details>

- **2026-08-29** — Guosheng Fu, Jian-Guo Liu — [Entropy-Stable and Physical-Constraint-Preserving DGSEM for Symmetry-Reduced General-Relativistic Hydrodynamics on Stationary Spacetimes](http://arxiv.org/abs/2608.29229v1)
  <details><summary>📄 Abstract</summary>
  We develop an entropy-stable and physical-constraint-preserving discontinuous Galerkin spectral element method for symmetry-reduced general-relativistic hydrodynamics on prescribed stationary spacetimes. Using a local orthonormal transformation, the fluid variables are expressed in a form for which the relativistic hydrodynamic algebra and the admissible set are independent of the spatial metric, while the spacetime geometry enters through stationary coefficients. This separation allows entropy-...
  </details>

- **2026-08-28** — Yafei Zhang, Nan Wu — [AcrossVAM1.0: Particle World Modeling for Text-Assisted Robot Video Prediction](http://arxiv.org/abs/2608.28491v1)
  <details><summary>📄 Abstract</summary>
  Predicting robot videos requires both precise motion reasoning and preservation of high-frequency appearance, yet monolithic pixel models entangle these objectives and often conceal their progress behind a strong last-frame baseline. We present AcrossVAM1.0, a lightweight, text-assisted video action model that factorizes future prediction into object-centric motion and dense appearance. A frozen SAM3-DLP codec decomposes four context frames into semantic particles for the robot, arm, and gripper...
  </details>

- **2026-08-28** — Di Wu, Sergey Troshin, Christof Monz et al. — [Ladders in Chaos: When, How, (and Perhaps Why) Does Test-Time Scaling Improve LLM Machine Translation](http://arxiv.org/abs/2608.28496v1)
  <details><summary>📄 Abstract</summary>
  Two forms of test-time scaling for Large Language Models (LLMs) have emerged as effective and widely adopted paradigms: sequential, in which later answer attempts depend on earlier ones, and parallel, such as i.i.d. sampling with reranking. In this study, we investigate their properties in translation. First, our study shows that sequential sampling has a higher performance ceiling, providing a more diverse and effective pool of samples, particularly under smaller sampling budgets. Second, we in...
  </details>

- **2026-08-28** — Eric L. Wisotzky, Jost Triller, Simon W. Härtl et al. — [Cross-Spectral Dense Correspondence for Multimodal Spectral Medical Imaging](http://arxiv.org/abs/2608.28341v1)
  <details><summary>📄 Abstract</summary>
  Precise dense correspondence is a fundamental prerequisite for multimodal spectral imaging systems that fuse disparate wavelength ranges for subsequent analysis in medical and scientific imaging. Corresponding image points are often observed with non-overlapping spectral sensitivities, leading to wavelength-dependent contrast changes, intensity inversions, and appearance shifts for which dense ground truth is difficult to obtain and conventional RGB-based training data provides only limited supe...
  </details>

- **2026-08-28** — Julien Grain, Hugo Holland, Lucas Pinol — [Explicit gauge-invariant variables in multifield inflation beyond linear order and Hamiltonian dynamics](http://arxiv.org/abs/2608.28337v1)
  <details><summary>📄 Abstract</summary>
  General relativity coupled to multiple scalar fields is a diffeomorphism-invariant constrained system. Consequently, a naive counting of the perturbative degrees of freedom unavoidably overestimates the true number of physical modes propagating in the theory, as gauge redundancies and constraint equations remove non-dynamical ones. While this problem has been solved for linear fluctuations, this work presents the first explicit calculation of all large-scale gauge-invariant phase-space variables...
  </details>

- **2026-08-27** — Zihan Ding, Liyu Zhang, Xiaomin Ouyang — [HALO: A Heterogeneity-Aware Language-Aligned IMU Foundation Model for Open-Set Human Activity Recognition](http://arxiv.org/abs/2608.27233v1)
  <details><summary>📄 Abstract</summary>
  Human Activity Recognition (HAR) using inertial measurement units (IMUs) enables a wide range of applications, yet the field still lacks a unified model that can generalize across diverse subjects, devices, and activities. Training such a model is difficult due to two key challenges: sensing heterogeneity -- differences in sampling rates, channel configurations, and sensor placements -- and poor generalization to unseen activities and label vocabularies. We introduce HALO (Heterogeneity-Aware La...
  </details>

- **2026-08-27** — Samuel Schmidgall, Xiaokai Zhu, Marian Shaw et al. — [Accelerating Scientific Research with Gemini in the Real-World](http://arxiv.org/abs/2608.26701v1)
  <details><summary>📄 Abstract</summary>
  We present an extension and comprehensive real-world validation of Co-Scientist, a Gemini-based multi-agent system designed to accelerate end-to-end scientific research across hypothesis generation, experimentation, and manuscript generation. Moving beyond in silico hypothesis generation, this specialized configuration transitions Co-Scientist into an execution-grounded research partner advancing closed-loop scientific workflows across materials science, biology, and computer science. In materia...
  </details>

- **2026-08-27** — Jinning Cui, Lu Chen, Haoyan Shi et al. — [Chart2SVG: Editable SVG Generation from Raster Chart Images](http://arxiv.org/abs/2608.26544v1)
  <details><summary>📄 Abstract</summary>
  We present Chart2SVG, a multimodal large language model that converts static raster charts into structurally organized, semantically enriched SVGs that support programmatic editing. By incorporating chart-specific semantic tokens into a vision-language model, Chart2SVG captures both geometric primitives and their functional roles. To support robust structural recovery, we introduce Beagle+, a dataset of 33K canonicalized and structurally distilled chart samples. Our approach combines specialized...
  </details>

- **2026-08-27** — Nguyen Xuan-Vu, Octavian Susanu, Daniel Armstrong et al. — [Mechanistic Reaction Prediction via Discrete Flow Matching on Graph-Structured Electron Occupation](http://arxiv.org/abs/2608.27429v1)
  <details><summary>📄 Abstract</summary>
  Chemical reactions are fundamentally transformations in electron space, yet most machine learning approaches model them either through \textit{de novo} generation of product molecules or through heuristic graph edits that operate directly on molecular topology.   We introduce MAELLE (\textbf{M}ech\textbf{A}nistic \textbf{E}dit f\textbf{L}ow-matching on e\textbf{L}ectron r\textbf{E}arrangements), which instead models reactions as discrete flow matching over electron occupation vectors.   Concrete...
  </details>

- **2026-08-27** — Xiaoxiao Lu, Yunlong Dong, Jiahao Shi et al. — [Making Latent Evolution Explicit: Operator-Structured Transitions for World Action Models](http://arxiv.org/abs/2608.27259v1)
  <details><summary>📄 Abstract</summary>
  World Action Models (WAMs) augment robot policies by predicting how task-relevant scene states may evolve under interaction. Recent WAMs increasingly perform such prediction in latent representation spaces, avoiding full appearance-level generation while preserving control-relevant information. Yet latent transitions are commonly realized with Transformer-based predictors whose inductive structure is centered on token interaction rather than temporal evolution. We study transition realization as...
  </details>


### 📂 watermark
*水印与溯源 / Watermarking & Provenance* — 19 papers

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

- **2026-08-30** — Dmitrij Żatuchin, Daniil Dzemesjuk — [Demand-Side Measurement for Generative Engine Optimization: Constructing and Validating a Million-Persona, Intent-Annotated Buyer Corpus](http://arxiv.org/abs/2608.30023v1)
  <details><summary>📄 Abstract</summary>
  Generative engines such as ChatGPT, Gemini, and Perplexity answer buyer questions directly and name a shortlist of brands inside the answer. Studying how brands enter or fail to enter that shortlist requires demand-side data: what buyers in a category ask, what information they need, and which sources they trust. Existing large persona corpora are built for training-data diversity and carry neither a staged search-intent label nor a preferred-sources field, so they cannot be joined to supply-sid...
  </details>

- **2026-08-30** — Bo Chen — [Token Counts Are Not Model Lineage: A Frozen-Threshold Holdout Study of Black-Box LLM API Fingerprinting](http://arxiv.org/abs/2608.29930v1)
  <details><summary>📄 Abstract</summary>
  Black-box model attribution is increasingly relevant when large language models (LLMs) are served through relay and reseller APIs. A tempting low-cost signal is the prompt-token count returned by an OpenAI-compatible endpoint: two models that share a tokenizer and chat template may produce the same count sequence up to a fixed offset. Yet the validity of this signal for broader \emph{model-family} attribution has received little direct holdout testing. We conduct a frozen-threshold study over 24...
  </details>

- **2026-08-30** — Shahar Oded, Yuval Shahar — [INTERVenE: Temporal-Abstraction-Interval Based Transformers for Short-Horizon Medical Event Prediction](http://arxiv.org/abs/2608.29901v1)
  <details><summary>📄 Abstract</summary>
  Electronic Health Record (EHR) prediction models in the intensive care unit must learn from sparse and irregular measurements while preserving the clinical meaning of time and supporting transparent decision-making. We present INTERVenE, a family of Transformer architectures whose input is an interval-based, knowledge-based temporal abstraction (KBTA), a token stream of named clinical concepts (states, trends, events, contexts) drawn from a curated medical ontology, rather than an unnamed bin in...
  </details>

- **2026-08-30** — Saadi Lahlou, Juan Pablo Caicedo, Shriya Sekhsaria et al. — [Large-Scale Qualitative Research with AI: Infrastructure, Management and Operation of the Socioscope Data Pipeline](http://arxiv.org/abs/2608.29751v1)
  <details><summary>📄 Abstract</summary>
  The Socioscope project is a pioneering effort in Large-Scale Qualitative Research (LSQR) collecting comparable, open-ended, multimedia field data on hundreds of cases and using AI to make the material analysable at scale. The domain studied is the food system. The entities documented are the organisations that act in it: farms, processors, distributors, retailers, restaurants; and, at meso level, the actors that shape their environment, such as municipalities, government programmes, banks, NGOs ...
  </details>

- **2026-08-30** — Ming Wu, Pengyuan Zhu — [Agent Zero Memory: Provenance-Aware Long-Term Memory for LLM Agents](http://arxiv.org/abs/2608.29606v1)
  <details><summary>📄 Abstract</summary>
  Large language model (LLM) agents need durable, faithful memory of everything a user or organization has said and stored, yet most memory systems commit to a single organizing structure (a fact store, a vector index, or a knowledge graph) and inherit its blind spots. We present Agent Zero Memory, a provenance-aware long-term memory system that distils a user's conversations, files, and connected sources into three parallel memory systems, each capturing a different facet of the same history: an ...
  </details>

- **2026-08-29** — Bingjie Li, Yumeng Song, Zhongming Yao et al. — [Localizing Emergent Failures in Agentic AI: Recovering Minimal Repair Families via Counterfactual Replay](http://arxiv.org/abs/2608.29228v1)
  <details><summary>📄 Abstract</summary>
  Failures in agentic AI systems can arise from interactions among messages exchanged by multiple large language model (LLM) agents. Pointwise attribution cannot distinguish a jointly necessary repair from alternative singleton repairs. We formulate Minimal Repair Family Recovery (MRFR): recovering all inclusion-minimal event sets whose counterfactual replay restores task success within a declared size bound. We propose Graph-Constrained Joint Replay (GCJR), which slices failure-relevant events fr...
  </details>

- **2026-08-28** — Jie Hu, Junjie Wang, Shan Lu et al. — [Propagating construction-time knowledge quality into medical question answering: A framework grounded in clinical guidelines](http://arxiv.org/abs/2608.28360v1)
  <details><summary>📄 Abstract</summary>
  Large language models have facilitated knowledge graph (KG) construction from clinical guidelines, but extracted triples vary in structural validity and evidential support. Meanwhile, graph-augmented question answering (QA) systems typically optimize query relevance during retrieval, with limited reuse of quality information produced during KG construction. This creates a disconnect between construction-time quality control and inference-time evidence use. We investigate whether construction-tim...
  </details>

- **2026-08-27** — Ke Shu, Kira Hinderks, Eetu Mäkelä et al. — [Pair-Level Essay-Scale Republication and Reuse from Fragmented Historical Text Reuse: A Workflow Study on Eighteenth-Century Books and Newspapers](http://arxiv.org/abs/2608.27343v1)
  <details><summary>📄 Abstract</summary>
  This paper addresses the recovery of essay-scale republication and reuse from fragmented text-reuse evidence, a setting whose central challenge is pair-level evidence consolidation and not fragment retrieval alone. The study focuses on a candidate set centered on essays by eighteenth-century Scottish philosopher David Hume, spanning books from ECCO (Eighteenth Century Collections Online) and historical newspapers. Because the input consists of fragmented reuse hits instead of clean document pair...
  </details>

- **2026-08-27** — Jeong-Yoon Kim — [BTS-AgentBench: A Deterministic, Replayable Pipeline from Read-Only Telemetry Logs to Agent Benchmarks](http://arxiv.org/abs/2608.27334v1)
  <details><summary>📄 Abstract</summary>
  Industrial sites contain large volumes of read-only telemetry, but few benchmarks specify how to compile these records into executable multi-turn agent tasks. We present a telemetry-to-episode construction method instantiated as BTS-AgentBench. The pipeline normalizes BTS metadata and raw histories into a read-only tool store, compiles static tasks with tool-derived gold answers and evidence, and lifts retained tasks into typed, bounded operator-facing episodes. The 532-row release adds clarific...
  </details>

- **2026-08-27** — Jinghan Xu, Yikai Zhang, Aili Chen et al. — [Verify Smarter, Evolve Further: Efficient Harness Evolution through Behavior-Aware Verification](http://arxiv.org/abs/2608.27311v1)
  <details><summary>📄 Abstract</summary>
  Agent harnesses shape how language-model agents use instructions, tools, and runtime components, but adapting these harnesses requires costly verification. Existing propose-and-verify methods typically score every candidate on a fixed task set, wasting rollouts on unrelated behaviors and allowing aggregate scores to obscure specific regressions. We introduce HarnessLens, a budget-aware framework for automated harness evolution. HarnessLens jointly explores the task space and user-configurable co...
  </details>


### 📂 unlearning
*机器遗忘 / Machine Unlearning* — 1 papers

- **2026-08-28** — Praveen Bushipaka, Andrea D'Angelo, Lucia Passaro et al. — [GRACE:Gradient-guided Coreset Selection for LLM Unlearning](http://arxiv.org/abs/2608.28361v1)
  <details><summary>📄 Abstract</summary>
  Machine Unlearning methods for Large Language Models typically assume pre-specified forget and retain sets. In realistic settings, however, requests may provide only a few examples of undesired behavior, requiring forget and retain sets to be inferred from heterogeneous corpora. We study this data-selection problem and propose GRACE , a gradient-guided coreset selection method that constructs both forget and retain sets for LLM unlearning. GRACE first computes a forget direction from seed exampl...
  </details>


### 📂 benchmark
*安全评测与基准 / Safety Benchmarks & Evaluation* — 3 papers

- **2026-08-29** — Linh Le, Hong Kiat Tan, David Williams-King — [Reference-Grafting Matches Fine-Tuning at Eliciting Sandbagged Capabilities](http://arxiv.org/abs/2608.29458v1)
  <details><summary>📄 Abstract</summary>
  Sandbagging, in which a model deliberately underperforms on an evaluation despite retaining the underlying capability, threatens the safety evaluations that frontier-model governance depends on. The Elicitation Game found that fine-tuning elicits hidden capability from sandbagging model organisms whereas additive activation steering fails. We revisit that verdict with reference-grafting, which sets an activation's coordinate along a contrast direction to the value it takes in an honest reference...
  </details>

- **2026-08-27** — Anik Saha, Fahmida Sultana Naznin, Sadatul Islam Sadi et al. — [DocTalkBN: A Novel Dataset of Expert Telemedicine Conversations in Bengali](http://arxiv.org/abs/2608.27110v1)
  <details><summary>📄 Abstract</summary>
  Reliable medical conversational AI requires authentic expert--patient interaction data, yet such datasets remain scarce, especially for low-resource languages such as Bengali. We present DocTalkBN, a large-scale multimodal dataset of real-world expert telemedicine conversations in Bengali, collected from nationally broadcast telemedicine programs featuring board-certified physicians. DocTalkBN contains 557.63 hours of paired audio and text, 1,515 multi-turn patient calls, 10,274 host--doctor que...
  </details>

- **2026-08-27** — Guang Yang, Xing Hu, Xiang Chen et al. — [Unsaid, Unsafe? Implicit Security Obligations in LLM-Based RTL Code Generation](http://arxiv.org/abs/2608.26588v1)
  <details><summary>📄 Abstract</summary>
  Large Language Models (LLMs) generate register-transfer-level (RTL) code with rapidly improving functional correctness. Security of LLM-generated code, however, has been studied mainly for software, where flaws can still be patched after deployment. Insecure RTL offers no such remedy once taped out into silicon. We construct SECRTL-GEN, a multi-language resource-access security benchmark grounded in real SoC IP: 392 tasks over five CWE families and four HDLs (Verilog, SystemVerilog, VHDL, and Py...
  </details>


### 📂 survey
*综述与系统化 / Surveys & Systematization* — 9 papers

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

- **2026-08-29** — Daehwan Ahn, Chengfeng Mao, Dokyun Lee — [Item-Mean Surrogates: Why Richer Persona Data Fail to Improve LLMs as Human Surrogates](http://arxiv.org/abs/2608.29455v1)
  <details><summary>📄 Abstract</summary>
  LLMs are increasingly used as human surrogates, often on the premise that richer persona data could make them substitutes or exploratory tools for specific individuals. We test this premise across four datasets covering more than 400,000 participants and more than 6,000 survey items and experimental outcomes. LLMs perform well at the aggregate level: their average responses closely align with average human responses to the same items. But this success largely reflects predicting each item's aver...
  </details>

- **2026-08-28** — Jingjing Nie, Jiawei Guo, Krishna Meda et al. — [LLM-Based Agents for Software and Systems Security: Approaches, Applications, and Assessment](http://arxiv.org/abs/2608.28490v1)
  <details><summary>📄 Abstract</summary>
  Software and systems security workflows are typically procedural: analysts inspect heterogeneous artifacts, form hypotheses, invoke tools, interpret outputs, and revise plans. Large language model (LLM)-based agents, which can plan, use tools, retain state, and revise actions across multi-step workflows, are being rapidly adopted to automate this work. Given the consequences of delegating security decisions to autonomous systems, understanding how such agents are built, used, and assessed is cru...
  </details>

- **2026-08-28** — Chengpiao Huang, Kaizheng Wang — [Learning a Size-Weight Frontier for Synthetic-Augmented Inference](http://arxiv.org/abs/2608.28576v1)
  <details><summary>📄 Abstract</summary>
  Synthetic data can improve statistical inference when real data are scarce, but naively treating synthetic samples as real data can introduce bias and lead to unreliable inference. We develop a general framework for synthetic-augmented inference across a population of related tasks. It characterizes synthetic augmentation by the number of synthetic observations and their weight. Central to our framework is a size-weight frontier that specifies, for each weight, the largest synthetic sample size ...
  </details>

- **2026-08-27** — Maciej Besta, Leonard Schmidt, Lara Nonino et al. — [Performance Foundations of Parallel & Distributed Reasoning Language Models](http://arxiv.org/abs/2608.27046v1)
  <details><summary>📄 Abstract</summary>
  Reinforcement Learning with Verifiable Rewards (RLVR) and other RL-style post-training paradigms have been used for aligning large language models (LLMs) with reasoning standards. The resulting recent Reasoning Language Models (RLMs) such as DeepSeek-R1, o3, and Kimi k1.5 show that such RL-style post-training ("RL-for-LLMs") can substantially improve chain-of-thought reasoning, long-horizon planning, and self-correction. However, the computational footprint of these systems is massive: state-of-...
  </details>


### 📂 other
*其他安全相关 / Other Security-Related* — 143 papers

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

- **2026-08-30** — Xinke Jiang, Zhixin Zhang, Zhibang Yang et al. — [Harness-RL: Black-Box Reinforcement Learning with Action-Args Decoupling for Central-Agent Multi-Agent Harnesses](http://arxiv.org/abs/2608.29641v1)
  <details><summary>📄 Abstract</summary>
  Large language model agents increasingly solve long-horizon tasks through multi-agent harnesses in which a central agent coordinates specialized sub-agents, tools, and environments. Training the central policy in such a harness raises two challenges. First, an action label is a low-cardinality decision, whereas its args form a high-dimensional conditional sequence; optimizing both with a shared sequence-level signal can produce conflicting gradients. Second, dynamic scheduling creates interdepen...
  </details>

- **2026-08-30** — Junxiang Liu, Lin Wang, Haiyu Shi et al. — [CineForge: Self-Improving Agents for Long-Horizon Video Generation](http://arxiv.org/abs/2608.29621v1)
  <details><summary>📄 Abstract</summary>
  Long-horizon story-driven video generation requires a production agent to coordinate narrative decomposition, state tracking, shot design, prompt construction, rendering, and revision across interdependent scenes. Existing adaptive video systems primarily refine requests or reusable skills, leaving recurring production failures disconnected from persistent, stage-targeted improvements across stories. We introduce CineForge, a self-evolving video-production agent framework that couples CineForge-...
  </details>

- **2026-08-30** — Hao Tian, Heng Cai, Yifan Yang — [BEACON: Behavioral and Semantic Enrichment of AlphaEarth Embeddings through Tri-Modal Contrastive Learning](http://arxiv.org/abs/2608.29553v1)
  <details><summary>📄 Abstract</summary>
  Geospatial foundation models such as the AlphaEarth Foundation produce compact and globally consistent representations of the Earth's surface that transfer effectively to a wide range of downstream tasks. However, because these models are trained primarily on Earth-observation imagery, their embeddings mainly capture physical and spectral characteristics while encoding human activity and urban function only weakly. To address this limitation, we propose BEACON, a tri-modal contrastive learning f...
  </details>

- **2026-08-30** — Joe Eappen, Zikang Xiong, Shreyash S. Iyengar et al. — [Generalizable Multi-Agent Planning from Signal Temporal Logic Specifications via Diffusion](http://arxiv.org/abs/2608.29490v1)
  <details><summary>📄 Abstract</summary>
  Multi-agent systems in the real-world (e.g., drone swarms, autonomous cars, warehouse robots) must satisfy rich, temporal tasks while avoiding collisions. Signal Temporal Logic (STL) elegantly encodes such objectives, but current STL planning methods face critical limitations. State-of-the-art optimization-based approaches can handle arbitrary STL specifications but struggle with scalability, becoming computationally impractical as the number of agents grows. Learning-based methods efficiently h...
  </details>

- **2026-08-30** — Peizheng Li, Xin Ai, Hanyuan Liu et al. — [RegionCache: Semantic-Aware Region Reuse for Efficient Multi-Turn Image Generation](http://arxiv.org/abs/2608.29809v1)
  <details><summary>📄 Abstract</summary>
  Real-world image generation often involves multi-turn editing, where users iteratively modify small regions while most image content remains unchanged. However, existing diffusion transformer (DiT)-based editing pipelines recompute the entire image at every turn, causing substantial redundant computation. Existing DiT acceleration methods further ignore semantic correspondence across prompts, leading to unnecessary recomputation or unsafe reuse that harms editing quality. To address this, we pro...
  </details>

- **2026-08-30** — R. Thomas McCoy, Paul Soulos, Tal Linzen et al. — [The Emergent Symbolic Structure of Artificial Neural Networks](http://arxiv.org/abs/2608.29530v1)
  <details><summary>📄 Abstract</summary>
  Modern systems in artificial intelligence (AI) somehow excel in domains for which they seem poorly suited. Intelligence has traditionally been modeled as operating over structured combinations of symbols, such as logical formulas. However, the strongest modern AI systems are based on neural networks, which instead represent information in continuous vectors. Vectors seem inadequate for capturing the structure of language, logic, and other cognitive domains, yet neural networks achieve impressive...
  </details>

- **2026-08-30** — Jackson R. Ye, Alexandre V. Morozov — [A Hybrid State-Space Approach for Census-Tract Population Estimation](http://arxiv.org/abs/2608.30094v1)
  <details><summary>📄 Abstract</summary>
  Sequence models---the architecture family behind large language models and, increasingly, state-of-the-art image recognition---have redefined how machines learn from high-dimensional data. Yet population estimation from satellite imagery, a task that underpins infrastructure planning, public health, and disaster response, has scarcely benefited: leading systems still bind population to a uniform raster, disaggregating census counts onto grid cells through weighting surfaces built from ancillary ...
  </details>

- **2026-08-30** — Robert Valaska, Katarina Bodova — [Observation delays can bias inference of selective advantage in evolutionary competition](http://arxiv.org/abs/2608.30085v1)
  <details><summary>📄 Abstract</summary>
  Relative-frequency trajectories are often used to infer selective advantage in competing biological populations. A common empirical approach is to fit a linear function to the logit-transformed frequency of an invading type and interpret the slope as the relative advantage. Here we test how this estimator is affected when the competing types are observed after type-specific delays. We use SARS-CoV-2 variant replacement in the United Kingdom as empirical motivation and study the mechanism with si...
  </details>

- **2026-08-30** — Shulei Wang — [Learning Representations through Token Prediction: Geometry, Approximation, and Downstream Guarantees](http://arxiv.org/abs/2608.30072v1)
  <details><summary>📄 Abstract</summary>
  Token prediction is a central pre-training objective for modern language models. Despite its empirical success, why token prediction learns broadly useful representations remains incompletely understood. We develop a statistical framework connecting token prediction with representation geometry, encoder approximation, and downstream performance. Under a softmax prediction head, we show that accurate token prediction organizes token embeddings according to similarities between the distributions o...
  </details>

- **2026-08-30** — Kaishuu Shinozaki-Conefrey, Olivier Pascaud, Robin Courant et al. — [TAKE 85: Testing Audiovisual filmmaKer's intEnt across 85 Hours of Film](http://arxiv.org/abs/2608.30068v1)
  <details><summary>📄 Abstract</summary>
  Films communicate through deliberate creative choices, including lighting, color, composition, editing, dialogue, music, and sound. Humans naturally interpret these signals as directorial intent, yet current multimodal large language models (MLLMs) are evaluated almost exclusively on understanding what happens rather than why it is presented that way. We introduce TAKE 85, the first benchmark for directorial-intent understanding, comprising 398 short films (85 hours) with expert-verified questio...
  </details>

- **2026-08-30** — Krisztian Balog, Arild Michel Bakken — ["Act Like a 5th Grader" is Not Enough: Bounding Knowledge in LLM-Based User Simulators](http://arxiv.org/abs/2608.30033v1)
  <details><summary>📄 Abstract</summary>
  Large language models (LLMs) are increasingly used to simulate human behavior but frequently fail to exhibit realistic cognitive constraints, suffering from a "superhuman bias." Using a dataset of over 71,000 reading comprehension responses from 2,359 primary-school students (grades 4--6), we demonstrate that standard persona prompting yields near-perfect, deterministic performance, failing to capture the natural variance of developing readers. To address this, we introduce the Cognitively Bound...
  </details>

- **2026-08-30** — Shriram Vasudevan, Subramanian Vasudevan — [Predictive Traffic Shaping as a UE Network Control Loop in Wireless Systems](http://arxiv.org/abs/2608.30019v1)
  <details><summary>📄 Abstract</summary>
  Wireless systems usually react to current channel conditions, queue state, and policy. Yet service conditions can often be anticipated seconds ahead. This paper studies predictive traffic shaping, a slower user-equipment (UE) control loop that changes when flexible demand reaches the radio access network (RAN). The UE estimates useful pre-event demand and releases it across a lookahead window. Cooperative deployments may also send a compact future-risk descriptor to the network. The trigger uses...
  </details>

- **2026-08-30** — Jakkala Mahesh, Jatavath Shravan Kumar, Komalla Shivani et al. — [Generative vs. Encoder Models for Multilingual NER: A Comprehensive Empirical Study on Naamapadam](http://arxiv.org/abs/2608.29959v1)
  <details><summary>📄 Abstract</summary>
  Language is humanity's most consequential technology, yet for over a billion speakers across India's twenty-two constitutionally recognised languages, its digital layer remains structurally incomplete. Named Entity Recognition (NER), the foundational step in transforming raw text into machine-interpretable knowledge, has been studied exhaustively for English but remains largely unsolved across most Indic languages. This paper presents a rigorous comparative study of generative and encoder-based ...
  </details>

- **2026-08-30** — Shanqing Xu, Meng Luo, Mengchen Qian et al. — [RIDGE: Region-Informed Derivative-Guided Evidence Selection for Long Video Understanding](http://arxiv.org/abs/2608.29958v1)
  <details><summary>📄 Abstract</summary>
  Long videos contain far more visual content than Large Vision-Language Models (LVLMs) can process under a fixed visual-token budget, making frame selection essential. Existing query-aware selectors usually estimate frame-query relevance and build a compact subset from high-scoring frames. Although their mechanisms differ, the similarity sequence is still often treated primarily as values to rank or sample from, rather than as an ordered signal whose shape reflects how query-relevant evidence eme...
  </details>

- **2026-08-30** — Alberto Cetoli — [Sleight of Word Benchmark: Can Language Models Notice If Their Own Output Was Tampered With?](http://arxiv.org/abs/2608.29921v1)
  <details><summary>📄 Abstract</summary>
  The output of a Language Model can be tampered with \emph{while} the model is writing it. A simple test can thus be constructed by evaluating the model's perception of this external perturbation. In this spirit, a simple benchmark is built in which a single word is consistently substituted with another in the generation process. We call this method \emph{Sleight of Word}. Two distinct axes are measured: metrics that relate to the model's surprise, as well as an evaluation of the textual reaction...
  </details>

- **2026-08-30** — Nicolas Bousquet, Frank Connor, Agnès Totschnig et al. — [Fair Division of Graphs: Beyond Traceability](http://arxiv.org/abs/2608.29902v1)
  <details><summary>📄 Abstract</summary>
  In this paper, we study fair division problems in which resources are structured as graphs and agents must receive connected bundles. This connectivity requirement fundamentally alters the problem, making it significantly more challenging than its classical counterpart. We focus on the fairness notion of $\mathrm{EF1}_{\mathrm{outer}}$, where envy can be eliminated by removing at most one vertex whose deletion does not disconnect the bundle -- a critical constraint for applications such as land ...
  </details>

- **2026-08-30** — Jiaqi Su, Cong Pang, Jiawei Hong et al. — [When History Is Multimodal: Rethinking Context Management for Long-Horizon Agents](http://arxiv.org/abs/2608.29897v1)
  <details><summary>📄 Abstract</summary>
  Long-horizon agents need a context manager to compress growing interaction histories into a bounded working context, via passive strategies or active strategies that decide how memory is accessed and reorganized. Meanwhile, prior optical-memory work mainly treats pixels as a dense codec for textualized histories, often presupposing that rendering context into optical memory incurs a significant performance drop relative to text, thus coupling this representation with SFT, self-distillation, or r...
  </details>

- **2026-08-30** — Kaidong Zhang, Yukang Ding, Xiaoyu Liu et al. — [Beyond Global Realism: Virtual Try-On Evaluation and Optimization with Dimension-wise Garment Fidelity Assessment](http://arxiv.org/abs/2608.29804v1)
  <details><summary>📄 Abstract</summary>
  Virtual try-on (VTON) requires not only realistic generation but also faithful preservation of garment characteristics. However, existing evaluation metrics such as PSNR, SSIM, KID and FID struggle to measure the consistency between the generated and reference garments, particularly in capturing the multi-dimensional characteristics of garment fidelity. To address this, we propose DAT: a Dimension-wise Assessment framework for virtual Try-on, which decomposes garment consistency into seven inter...
  </details>

- **2026-08-30** — Nicole Gehring — [Successive design of backstepping observers for parabolic PDE-ODE systems and its duality to state feedback stabilization](http://arxiv.org/abs/2608.29693v1)
  <details><summary>📄 Abstract</summary>
  The paper introduces a successive backstepping observer design for strictly feedforward parabolic PDE-ODE systems, in which the coupling structure determines the order of error stabilization and the corresponding transformations. First, a transformation based on a virtual measurement stabilizes the ODE observer error subsystem, which is most distal from the measurement, while decoupling it from the PDE error state. Second, a Volterra integral transformation is employed to stabilize the PDE error...
  </details>

- **2026-08-30** — Zongyue Li, Chengyue Yu, Lei Zang et al. — [Last Step Matters: Early Uncertainty Cannot Predict Failure in Long-Horizon Agents](http://arxiv.org/abs/2608.29685v1)
  <details><summary>📄 Abstract</summary>
  Early failure prediction is important for long-horizon agents, as it enables timely intervention and can reduce inference and tool-use costs. Uncertainty quantification, such as verbal confidence and perplexity, offers a promising approach to detecting agent failures; however, it has not been explored whether these signals retain their discriminative power during the intermediate stages of long-horizon execution. We evaluate mainstream uncertainty signals on deep-research tasks and find that ver...
  </details>

- **2026-08-30** — Marc S. Walton, Astrid Harth — [Conducting Stylistic Analysis of Paintings through an Art-History Agent](http://arxiv.org/abs/2608.29644v1)
  <details><summary>📄 Abstract</summary>
  Attributing an artwork to an artist has traditionally relied on detailed visual observations and descriptions, known as stylistic analysis in art history. By contrast, current artificial intelligence (AI) models used in the field offer only unexplained probabilistic classifications. To bridge this methodological gap, we present an AI framework that automates stylistic analysis of paintings, providing a foundation for enhancing evidence collection, discovery, and verification. By training a visio...
  </details>

- **2026-08-30** — Shi-Ju Ran, Kun Zhang, Xi Wu et al. — [LLMs Interpret, Embeddings Organize, Graphs Emerge: Agent-Driven Compilation of Scientific Knowledge](http://arxiv.org/abs/2608.29612v1)
  <details><summary>📄 Abstract</summary>
  Sustained scientific work requires a knowledge substrate that carries interpretation across tasks and preserves paths to source evidence. We call this process \emph{scientific knowledge compilation} and implement it in ASKS, the \emph{Agent-Driven Scientific Knowledge System}. For each source, an LLM produces a readable Wiki view and machine-facing semantics. Deterministic checks convert the latter into a document-local GraphDelta, and embedding geometry together with explicit graph rules integr...
  </details>

- **2026-08-30** — Juneha Baek, Suhyeon Lee, Donghyuk Shin — [How You Ask Shapes What You Get: A Theory-Seeded Measurement of Articulation in Advice-Seeking LLM Conversations](http://arxiv.org/abs/2608.29591v1)
  <details><summary>📄 Abstract</summary>
  Users articulate the same advice-seeking request in different ways: some specify detailed constraints, others gesture at a vague need. Prior work treats this variation as noise to be averaged away; we instead treat it as a stable, measurable structure in the input distribution. We ask whether articulation (how people ask) forms latent dimensions separable from topic (what they ask about), and whether it is associated with how language models respond. We extract interpretable features from 16,447...
  </details>

- **2026-08-30** — Yilun Liu, Boyu Luo, Yanran Tang et al. — [Call Neighbours Yourself: Graph Walks with Destination-Conditioned On-Policy Self-Distillation](http://arxiv.org/abs/2608.29588v1)
  <details><summary>📄 Abstract</summary>
  Reasoning over text-attributed graphs (TAGs) requires large language models (LLMs) to combine a node's text with evidence distributed across its neighbourhood. Existing methods fix the set of accessible neighbours before generation, forcing reasoning to operate over a static context and preventing the model from acquiring missing evidence during inference. We argue that neighbour selection should itself be part of the reasoning process. To this end, we propose Call Neighbours Yourself (CNY), a f...
  </details>

- **2026-08-30** — Alvin Wei Ming Tan, Ben Prystawski, Veronica Boyce — [Which one is banana man? Evaluating vision-language models in multi-turn pragmatic interpretation](http://arxiv.org/abs/2608.29571v1)
  <details><summary>📄 Abstract</summary>
  Flexible adaptation to context and shared pragmatic intuitions contribute to smooth human conversation. Iterated reference games---in which players repeatedly pick out novel referents using language---present a test case for agents' ability to perform context-sensitive pragmatic reasoning in multi-turn linguistic environments. We tested humans and vision--language models on their ability to identify the intended meaning of descriptions produced in iterated reference games, varying the provided c...
  </details>

- **2026-08-30** — Yuqi Pan, Zheng Li, Bohao Tang et al. — [LoGo: Token-Level Dynamic Local-Global Attention](http://arxiv.org/abs/2608.29539v1)
  <details><summary>📄 Abstract</summary>
  As context lengths scale, attention increasingly becomes a primary computational bottleneck in large language models. Standard Transformers remain powerful but computationally inefficient, as they allocate the same attention budget to every token regardless of its contextual demand. Existing local-global hybrids provide a more efficient alternative by mixing restricted- and full-context attention, but they typically allocate span statically across layers or heads. To address these limitations, w...
  </details>

- **2026-08-30** — Nisarg Shah, Paritosh Verma — [Fair Division Under Boolean Valuations: Beyond Normalization](http://arxiv.org/abs/2608.29497v1)
  <details><summary>📄 Abstract</summary>
  We study fair division of indivisible items when agents have arbitrary two-level preferences: the value of each agent for any set of items is Boolean, which need not be monotone or additive. Notably, we do not impose the standard assumption of normalization, i.e., different agents may value the empty set at different Boolean levels. Since the preferences are nonmonotone, envy-freeness up to one item (EF1) and envy-freeness up to any item (EFX) each admit several variants, depending on which item...
  </details>

- **2026-08-30** — Sindhuja Penchala, Sudip Mittal, Noorbakhsh Amiri Golilarz — [Seeing Through Extreme Visual Sparsity: Surface Understanding from a Single Random Visual Patch](http://arxiv.org/abs/2608.29475v1)
  <details><summary>📄 Abstract</summary>
  Surface material recognition from incomplete visual observations remains a challenging problem in robotic perception and environmental understanding. This paper discusses Sparse Surface Understanding Framework (SSUF), a unified dual-task learning framework that adapts four pretrained architectures-Convolutional Autoencoder (ConvAE), Vision Transformer (ViT), Swin Transformer, and Masked Autoencoder (MAE) for si-multaneous surface reconstruction and material classification. Experiments were condu...
  </details>

- **2026-08-29** — Muhammad Adil, Pranavkumar Pathak, Salman A. Alqahtani — [Secrecy Outage Analysis over Correlated Composite Generalized-Gamma Fading Channels](http://arxiv.org/abs/2608.29414v1)
  <details><summary>📄 Abstract</summary>
  This paper investigates physical-layer security (PLS) over correlated composite generalized-Gamma (GG)/GG fading channels, where both shadowing and small-scale fading follow GG distributions. Using Mellin transforms and Fox-H functions, closed-form expressions are derived for the single-link probability density function (PDF), joint distribution, survival function, and zero-rate secrecy outage probability (SOP)/probability of non-zero secrecy capacity (PNZSC). The general-rate SOP is expressed a...
  </details>

- **2026-08-29** — Yue Peng, Lanke Xia, Zihan Wang et al. — [EvoGenUI-Bench: Evaluating LLMs as Multi-Turn Generative UI Assistants](http://arxiv.org/abs/2608.29387v1)
  <details><summary>📄 Abstract</summary>
  Large language models can generate interactive web interfaces, but reliable generative UI requires maintaining an executable artifact as user requests evolve. We introduce EvoGenUI-Bench, a benchmark for multi-turn interface maintenance comprising 150 five-turn tasks and 750 turns across three scenarios: information presentation, executable interaction, and tool-grounded external state. We execute generated artifacts in a browser and evaluate them using screenshots, source and DOM evidence, acto...
  </details>

- **2026-08-29** — Runsheng Li, Kai Sun, Bin Shi et al. — [Cross-Relational Preference Learning for Better LLM Instruction Following](http://arxiv.org/abs/2608.29352v1)
  <details><summary>📄 Abstract</summary>
  Large Language Models (LLMs) still exhibit limited capability in following complex instructions. While existing approaches often rely on preference learning to enhance this ability, they typically overlook the relationships between the permissible response spaces of different instructions, which restricts a model to align with subtle and diverse constraint variations. To address this, we propose Cross-Relational Preference Learning (CRPL), a novel framework for constructing preference data that ...
  </details>

- **2026-08-29** — Niamh Ellis, Thi Tran, Ignacio Carlucho et al. — [A Cognitive Architecture for Shared Autonomy in AUV Operations](http://arxiv.org/abs/2608.29347v1)
  <details><summary>📄 Abstract</summary>
  Operators remain essential to Remotely Operated Vehicle (ROV) operation, yet often suffer from low situational awareness and high workload, both of which negatively affect safety. This paper presents a cognitive architecture consisting of an ontology and multiple Large Language Models (LLMs) to assist the operator at all stages of the mission. Each LLM is grounded with domain-specific information from the ontology and given a simple role to create a system that can support the operator at all st...
  </details>

- **2026-08-29** — Márcus Lobo, Vitor Matias, Jeová Farias et al. — [3D-MRL: Nested Multimodal 3D Representations via Matryoshka Representation Learning](http://arxiv.org/abs/2608.29285v1)
  <details><summary>📄 Abstract</summary>
  Vision-Language Models align point clouds with image and text embeddings, enabling zero-shot recognition, retrieval, and open-vocabulary understanding of 3D shapes. Existing multimodal 3D pre-training methods produce fixed-dimensional embeddings, requiring separate models for different computational budgets. We propose 3D Matryoshka Representation Learning (3D-MRL), a multimodal 3D pre-training framework based on Matryoshka Representation Learning. 3D-MRL learns nested 3D representations by alig...
  </details>

- **2026-08-29** — Aman Prakash, Sourish Dasgupta, Tanmoy Chakraborty — [HalluPrism: When Multimodal Uncertainty Should Diagnose, Not Decide](http://arxiv.org/abs/2608.29193v1)
  <details><summary>📄 Abstract</summary>
  Multimodal Large Language Models (MLLMs) can assign similar confidence to answers that fail for different reasons. We propose HalluPrism, a behavioral diagnostic that re-runs an answer after visual degradation, blank-image replacement, and grounding or relation checks. These targeted probes yield a signature over visual-perturbation sensitivity (V ), image-removal confidence retention (L), and grounding/relation-probe instability (A). Across 58K+ examples from four benchmarks and four MLLMs, ima...
  </details>

- **2026-08-29** — Yujun Qi, Yangyang Guan — [Sustained Heterogeneity: an emergent collective mechanism in LLM-driven traffic](http://arxiv.org/abs/2608.29174v1)
  <details><summary>📄 Abstract</summary>
  Large language models (LLMs) are increasingly adopted as closed-loop controllers in physical multi-agent systems, yet their emergent collective dynamics remain incompletely characterised. We deploy 22 LLM agents as direct, real-time target-speed controllers (per 0.5 s cycle, with IDM as collision-avoidance clamp) on a 230 m ring road under the Sugiyama 2008 paradigm, reproducing human-like stop-and-go waves. Six matched controls spanning stochasticity (white noise, OU noise, temperature), popula...
  </details>

- **2026-08-29** — Pravin Game, Vipin Ramakrishnan, Prathamesh Wagh — [Development of an Autonomous AI Coding Agent using Monte Carlo Tree Search (MCTS) and Gemini LLM Frameworks](http://arxiv.org/abs/2608.29096v1)
  <details><summary>📄 Abstract</summary>
  The ongoing changes in software engineering requirements have created a substantial need for automated tools which can create secure source code from natural language input. The performance of traditional Large Language Models (LLMs) becomes limited by their "one-shot" capability which results in logical hallucinations together with reduced algorithmic performance during complicated operations. The research presents an autonomous AI Coding Agent which establishes a connection between LLM-generat...
  </details>

- **2026-08-29** — Rithika Narayan, Suresh Kumaar Jayaraman, Henny Admoni — [Teaching Robot Policies to Humans Using Erroneous Examples](http://arxiv.org/abs/2608.29023v1)
  <details><summary>📄 Abstract</summary>
  Human-robot collaboration describes the process of humans and autonomous agents working together to accomplish common goals. This process is facilitated best when robot policies, or behaviors in different situations, are made transparent to humans. Demonstration-based explanations have been a focus of human-robot collaboration research, and the field has frequently drawn upon literature from education to improve how humans are taught robot policies. However, no single teaching method has been pr...
  </details>

- **2026-08-29** — Xunyi Jiang, Junda Wu, Yuxin Xiong et al. — [Toward Latent Language Model Skills Steering and Optimization: An Empirical Study](http://arxiv.org/abs/2608.29459v1)
  <details><summary>📄 Abstract</summary>
  Skills, as a useful abstraction for the procedural capabilities of large language models (LLMs), capture how models perform structured, multi-step reasoning and program execution. Existing approaches typically treat skills as explicit, surface-level constructs specified through prompts or programs, leaving open the question of how such procedural capabilities are represented inside the model and whether they can be manipulated as structured objects in latent space. In this empirical study, we in...
  </details>

- **2026-08-29** — Cheng Chen, Jerry Bai, Jiacheng Wei et al. — [AnyWorld: Factorized Egocentric World Models for Cross-Embodiment Generalization](http://arxiv.org/abs/2608.29242v1)
  <details><summary>📄 Abstract</summary>
  Collecting contact-rich robot experiences at scale remains a major bottleneck for generalizable manipulation. Beyond data quantity, robot learning also requires diverse experiences across embodiments, viewpoints, and scenes. Human egocentric videos provide abundant physical interactions, but each video captures only a narrow slice of experience under a single body, camera trajectory, and environment. We propose AnyWorld, a cross-embodiment world modeling framework that expands a single human int...
  </details>

- **2026-08-29** — Shuangkang Fang, Yufeng Wang, Yi-Hsuan Tsai et al. — [Chat-Edit-3D++: Interactive 3D and 4D Scene Editing via Large Language Models](http://arxiv.org/abs/2608.29137v1)
  <details><summary>📄 Abstract</summary>
  Recent work on image content manipulation based on vision-language pre-training models has been effectively extended to text-driven 3D scene editing. However, existing schemes for 3D scene editing still have certain shortcomings, hindering their further development as interactive design tools. Such schemes typically adhere to fixed input patterns, limiting flexibility in text input. Furthermore, their editing capabilities are constrained by a single or a few 2D visual models and require intricat...
  </details>

- **2026-08-29** — Makoto Sato, Tatsuya Matsushima, Yutaka Matsuo et al. — [DREAM: Deployment-Time Demonstration Generation via Real-to-Sim for Scalable Policy Adaptation](http://arxiv.org/abs/2608.29078v1)
  <details><summary>📄 Abstract</summary>
  Vision-language-action (VLA) models have made strong progress in language-conditioned robot manipulation, but improving their performance in a new workspace still often requires action-labeled data from that environment. Collecting such data by human teleoperation is costly, especially when each workspace, object arrangement, or task may require new demonstrations. We present DREAM, a framework that generates fine-tuning data for a pretrained VLA from a captured workspace and a language instruct...
  </details>

- **2026-08-29** — Zhangdie Yuan, Andreas Vlachos — [Evaluating the Semantic Specificity of Representation Steering in Language Models](http://arxiv.org/abs/2608.29431v1)
  <details><summary>📄 Abstract</summary>
  Localized Representation Steering (LRS) is widely used to correct reasoning pathologies in large language models. However, standard benchmark evaluations can easily be fooled by superficial label overrides, creating a false impression of reasoning circuit repairs. In this work, we propose Cross-Rule Transfer (CRT), a diagnostic framework that audits representational interventions by evaluating them on rule families where the model is natively competent. Evaluating late-layer LRS for a widespread...
  </details>

- **2026-08-29** — Bram Brongers — [Improving Swaption Calibration in Factor HJM Stochastic Volatility Models: A First-Order Correction to Frozen Swap-Rate Loadings](http://arxiv.org/abs/2608.29423v1)
  <details><summary>📄 Abstract</summary>
  The factor HJM stochastic volatility model introduced by Sepp and Rakhmonov (2025) obtains tractable swaption pricing by freezing the nonlinear swap-rate loading along a deterministic expected-state path. This removes the dependence of conditional swap-rate variance on the current yield-curve state. We introduce a first-order Taylor correction to the loading that adds no calibration parameters. Conditional on retaining the frozen annuity-measure drift, we show that the first variation of the swa...
  </details>

- **2026-08-29** — Jinfeng Xu, Zheyu Chen, Shuo Yang et al. — [Agents as Knowledge Integrator and Utilizer in Multimodal Recommendation](http://arxiv.org/abs/2608.29410v1)
  <details><summary>📄 Abstract</summary>
  Online platforms increasingly rely on multimodal recommender systems to rank products, media, and other Web content. Existing methods usually inject visual and textual features into item representations or build homogeneous graphs from modality-level similarity, but the resulting signals can remain misaligned with the recommendation objective. We study this semantic gap from a knowledge-integration perspective: multimodal content should be interpreted together with user behavior before it is use...
  </details>

- **2026-08-29** — Juhwan Song, Heejung Kim, Juntae Noh et al. — [FISICA: A Deployed Service for Plantar-Pressure and Posture Assessment with Ontology-Grounded Recommendation](http://arxiv.org/abs/2608.29336v1)
  <details><summary>📄 Abstract</summary>
  FISICA is a body-assessment and recommendation service running in production. One standing session with two photographs returns foot-loading measures, posture coordinates, a driven 3D avatar, a visual report, and ranked shoe and exercise candidates. Measurement comes from a purpose-built scale carrying 634 force-sensitive elements on a 1 cm grid and four load cells, and a rule-based evaluator controls every recommendation while a language model only explains the stored result. The method contrib...
  </details>

- **2026-08-28** — Le Xia, Rose Qingyang Hu, Paul S. Kudyba et al. — [xTRUCE: A Provably Safe Arbiter for Multi-xApp Conflict Mitigation in Agentic O-RAN](http://arxiv.org/abs/2608.28532v1)
  <details><summary>📄 Abstract</summary>
  The open radio access network (O-RAN) is evolving toward agentic operation, where large language model (LLM)-driven xApps/rApps generate control proposals under operator intents. However, such proposals may be conflicting, infeasible, or hallucinated, and no existing system jointly provides proposal-independent safety, priority-aware reconciliation, and traceable feedback. To this end, we propose a provably safe arbiter, namely xTRUCE, in the near-real-time (Near-RT) RAN intelligent controller f...
  </details>

- **2026-08-28** — Bryan Chen Zhengyu Tan, Weihua Zheng, Thong T. Doan et al. — [CultureConverse: A Multilingual Multi-turn Simulation Harness for Culturally Grounded Assistance in East and Southeast Asia](http://arxiv.org/abs/2608.28405v1)
  <details><summary>📄 Abstract</summary>
  Current cultural evaluations for large language models (LLMs) often reduce culture to single-turn factual recall via MCQs, failing to capture a common use case: users seeking practical help over multiple turns in culturally grounded scenarios. We introduce CultureConverse, a scalable, multilingual simulation and evaluation harness for culturally grounded assistant dialogue that covers 10 East and Southeast Asian regions, 58 subgroup identities, and 7 domains. Each simulated and evaluated episode...
  </details>

- **2026-08-28** — Aaryan Ajay Sharma, Sai Nishanth Padala, Seganrasan Subramanian — [DARTS: Decoder-Aware Representation Tuning via Surgery for Model Merging](http://arxiv.org/abs/2608.28547v1)
  <details><summary>📄 Abstract</summary>
  Model merging combines multiple task-specific fine-tuned LLMs into a single multi-task model without additional training. However, merged models are known to suffer from representation bias: systematic drift between the merged model's hidden states and those of each individual source model. Prior work (Yang et al., 2024a) study and mitigate this bias for encoder-based vision models using a lightweight correction module trained with L1 loss. However, such bias is not studied for decoder models du...
  </details>

- **2026-08-28** — Benjamin Turtel, Paul Wilczewski, Kris Skotheim et al. — [How Proper Scoring Rules Shape LLM Forecasting](http://arxiv.org/abs/2608.28482v1)
  <details><summary>📄 Abstract</summary>
  This paper evaluates how reward function choice shapes the performance and behavior of LLM forecasters. We compare five proper scoring rules as training objectives for binary forecasts of resolved real-world events. Although the rules share the same theoretical incentive for truthful probability reporting, the resulting models differ in calibration, probability use, and estimated profiles of bias, information, and noise, with smaller differences in aggregate accuracy and discrimination. The Brie...
  </details>

- **2026-08-28** — Minghui Xu, Zi Wang — [Learning to Use Tools: Reinforcement Learning for Tool-Integrated Mathematical Reasoning](http://arxiv.org/abs/2608.28447v1)
  <details><summary>📄 Abstract</summary>
  Current large language models (LLMs) increasingly benefit from external tool integration, especially for tasks requiring reliable computation and verification. Motivated by this, we study calculator tool calling for improving mathematical reasoning on the Countdown task. We first analyze reasoning failures and find that calculation errors account for a substantial portion of incorrect responses. We then construct supervised fine-tuning datasets to teach the model useful tool-use patterns and how...
  </details>

- **2026-08-28** — Antonio Laface — [Fujita freeness for projectivized toric vector bundles](http://arxiv.org/abs/2608.28438v1)
  <details><summary>📄 Abstract</summary>
  Let $X$ be a smooth projective toric variety of dimension $n\geq1$ over an algebraically closed field of characteristic zero, let $\mathcal E$ be a toric vector bundle of rank $r\geq2$, and let $π\colon Y=\mathbb P_X(\mathcal E)\to X$ be the projective bundle of one-dimensional quotients. Write an ample line bundle on $Y$ as $A=\mathcal O_Y(a)\otimesπ^*L$, with $a\geq1$. We record a blow-up argument proving that $K_Y+mA$ is globally generated whenever an integer $m$ satisfies $ma\geq r$ and $mδ(...
  </details>

- **2026-08-28** — Haofei Hou, Fanxu Meng, Shunyi Zhao et al. — [Linear Temporal Logic Translation via Human-Inspired Self-Constrained Reasoning for Robot Task Specification](http://arxiv.org/abs/2608.28435v1)
  <details><summary>📄 Abstract</summary>
  Many robotic tasks are temporally extended and demand precise specifications of subgoals, constraints, and their temporal ordering. Yet human operators typically communicate such tasks in natural language, which is inherently ambiguous, underspecified, and context dependent. Translating human instructions into formal task specifications, such as Linear Temporal Logic (LTL), is therefore essential for verifiable and safe robotic execution. Existing LLM-based translators attempt to bridge this gap...
  </details>

- **2026-08-28** — Md Haseen Akhtar — [Between Algorithm (AI) and Intuition (Human): Preserving Designer Agency in AI-Assisted Sensemaking of Qualitative UX Data](http://arxiv.org/abs/2608.28420v1)
  <details><summary>📄 Abstract</summary>
  The integration of AI into qualitative design research presents a fundamental tension: how do we leverage AI while preserving the subjective, intuitive judgments that define design expertise? This paper examines this question through a case study of analyzing 20 user responses about video conferencing platforms for educational contexts. We argue that AI sensemaking tools risk flattening the rich data patterns, amplifying contradictory textures of user feedback into sterile categories thereby tra...
  </details>

- **2026-08-28** — Zi-Jian Cheng, Zi-Yi Jia, Zhi Zhou et al. — [SymboLLM-FE: LLM-Accelerated Symbolic Regression for Automated Feature Engineering on Tabular Data](http://arxiv.org/abs/2608.28408v1)
  <details><summary>📄 Abstract</summary>
  Tabular data, as a core data format in machine learning, often lacks the discriminative power needed for high-performance modeling due to insufficient feature informativeness. Automated Feature Engineering (AutoFE) overcomes this by automating feature generation and selection, ensuring both model performance and operational efficiency. However, traditional AutoFE often yield features with poor interpretability because they rely on blind mathematical transformations, while large language models (...
  </details>

- **2026-08-27** — Stian Lybech, Eun-Young Kang, Riccardo Tonello et al. — [Information Flow Control in Off-Chain Components](http://arxiv.org/abs/2608.26858v1)
  <details><summary>📄 Abstract</summary>
  This paper develops a model of a smart-contract language for a blockchain architecture with off-chain components. Off-chain components are pieces of smart contracts that execute at designated locations outside of the network of blockchain nodes, but remain synchronised with the on-chain contract state. They react to changes to the on-chain state, but may also notify the on-chain component about events in the world, e.g. stock prices, weather data etc., or even act as a bridge between different b...
  </details>

- **2026-08-27** — Gyouk Chu, Myeongho Jeon, Eunho Yang — [J-Zero: Unified Challenger--Solver--Judge Co-Evolution from Zero Data](http://arxiv.org/abs/2608.26582v1)
  <details><summary>📄 Abstract</summary>
  Self-evolving language models have recently emerged as a promising path toward superintelligence, with the advantage of reducing the cost of human supervision. While considerable progress has been made in verifiable domains, self-evolution in unverifiable domains remains substantially less explored. We propose Judge co-adaptation from Zero data (J-Zero), a unified Challenger--Solver--Judge co-evolution framework that supports self-improvement across both domains. The Challenger and Solver co-evo...
  </details>

- **2026-08-27** — Canzhi Chen, Zan Wang, Siqi Zhu et al. — [Embodied Scene Rearrangement Planning](http://arxiv.org/abs/2608.27371v1)
  <details><summary>📄 Abstract</summary>
  This paper introduces Embodied Scene Rearrangement Planning (ESRP), a novel task requiring embodied agents to rearrange furniture in 3D scenes to match a target configuration using only egocentric observations and a top-down target layout. Unlike prior rearrangement tasks, ESRP precludes global state access and introduces mutual object occlusions, reflecting the practical constraints of real-world robotic deployment. These factors make aligning partial egocentric observations with the global tar...
  </details>

- **2026-08-27** — Navya Goli, Junzhe Liu, Zhenge Jia et al. — [AgentDV: Closed-Loop Agentic AI for Hardware Design Verification](http://arxiv.org/abs/2608.27148v1)
  <details><summary>📄 Abstract</summary>
  Register-transfer level (RTL) verification consumes a major part of modern system-on-chip (SoC) development effort. Yet, recent LLM-based verification-code generation often fails to produce runnable, design-consistent, and coverage-producing testbenches. We present AgentDV, a closed-loop agentic AI framework for automated RTL verification environment generation. AgentDV transforms single-shot LLM testbench generation into a tool-grounded verification pipeline by combining LLM-guided analysis, te...
  </details>

- **2026-08-27** — Yaxiao Liu, Pengbo Liu, Yiwen Liu et al. — [A Contract-Centered Architecture for Scalable and Manageable Agentic Runtimes](http://arxiv.org/abs/2608.27086v1)
  <details><summary>📄 Abstract</summary>
  Enterprise AI deployment is a coordination problem across business units, application and AI teams, testing, platform engineering, infrastructure, security, operations, and data governance. Use-case benchmarks show whether one agent completes one task, but not how changing capabilities, models, runtime mechanisms, capacity, and enterprise data should be owned, changed, admitted, or evidenced together.   We present four responsibility objects as shared organizational contracts: Skill (reusable, v...
  </details>

- **2026-08-27** — Abdullah Karasan — [Representation Measurements Under Function-Preserving Reparameterizations](http://arxiv.org/abs/2608.27020v1)
  <details><summary>📄 Abstract</summary>
  Hidden coordinates are not uniquely determined by a language model's input--output function, so representation-derived measurements should be invariant to function-preserving changes of basis. This study shows that column-permutation parallel analysis violates function-preserving reparameterization invariance because its reference distribution and selected component count can change while the model function and observed covariance spectrum remain fixed. More generally, a data-internal reference ...
  </details>

- **2026-08-27** — Ireddi Rakshitha, Devavarapu Yashwanth, Ntakirutimana Pierre — [KinyaEmbed: Contrastive Sentence Embeddings for Kinyarwanda via Multi-Stage Curriculum Training](http://arxiv.org/abs/2608.26941v1)
  <details><summary>📄 Abstract</summary>
  We present KinyaEmbed, the first dedicated sentence embedding model for Kinyarwanda, a morphologically rich Bantu language spoken by over 12 million people in Rwanda. Existing multilingual embedding models such as LaBSE, mE5-large, and OpenAI text-embedding-3-large perform poorly on Kinyarwanda due to severe under-representation in their pre-training corpora. KinyaEmbed is built on KinyaBERT-large and trained via a four-stage curriculum using MultipleNegativesRankingLoss (MNRL): Stage 1 leverage...
  </details>

- **2026-08-27** — Mohamed Guechaoui, Mohamed Diaa Zellagui, Souleyman Chaib et al. — [AraMS-28k: The Largest Publicly Released Line-Level Dataset of Historical Arabic Manuscripts with Margin and Insertion-Anchor Annotations](http://arxiv.org/abs/2608.26921v1)
  <details><summary>📄 Abstract</summary>
  We introduce AraMS-28k, the largest publicly released line-level dataset of genuine historical Arabic manuscripts, comprising 14 books, 3,043 pages, and 28,600 annotated text lines (27,971 main-text, 629 margin). Thirteen books are hand-copied manuscripts spanning three script traditions -- Naskh, Ruq'ah, and Maghrebi -- and one is a lithographed printed edition included to broaden format diversity. Each line is labelled as main-text or margin, and margin lines that have an unambiguous attachmen...
  </details>

- **2026-08-27** — Biao Yin, Abderrahmane Kasmi, Nadir Farhi — [Reinforcement Learning-Based Control of CAV Platoon Joining Maneuvers in Mixed Traffic](http://arxiv.org/abs/2608.26860v1)
  <details><summary>📄 Abstract</summary>
  Connected and automated vehicle (CAV) platooning offers a promising approach to improving road safety and traffic capacity. However, platoon control in real-world traffic is challenging due to uncertainty and heterogeneous driving behaviors. Reinforcement learning (RL) has strong potential for addressing such control problems, but its practical deployment raises challenges related to safety and learning efficiency. This paper proposes a generic modeling and simulation framework for investigating...
  </details>

- **2026-08-27** — Ji Soo Lee, Jinyoung Park, Seohyun Lee et al. — [Reason in the Words You Speak: Idiolectal Paraphrasing Off-Policy Traces for Reasoning Distillation in VideoLLMs](http://arxiv.org/abs/2608.26684v1)
  <details><summary>📄 Abstract</summary>
  Recent large language models achieve strong performance on complex reasoning tasks, where reinforcement learning with Group Relative Policy Optimization (GRPO) has emerged as a leading paradigm for optimizing models on self-generated trajectories. However, the on-policy nature of GRPO bounds the model to the reasoning skills it can already produce, restricting to learn more advanced capabilities. Prior works inject privileged reasoning traces from a stronger teacher policy to guide training, yet...
  </details>

- **2026-08-27** — Pei Yu Chang, Qadeer Ahmed — [Barrier Function Conformal Safety Clearance Certification with CVaR for Driving Trajectory Selection](http://arxiv.org/abs/2608.26533v1)
  <details><summary>📄 Abstract</summary>
  Autonomous driving motion planners generate and select candidate trajectories while accounting for interactions with surrounding agents. However, these evaluations do not certify the actual safety clearance of the selected trajectory. The framework evaluates the trajectory selected by ant planners and calibrates the gap between its plan time margin and realized safety clearance. A differentiable separating axis barrier margin deterministically lower bounds exact signed oriented-bounding-box (OBB...
  </details>

- **2026-08-27** — Lois Curfman McInnes, Dorian Arnold, Prasanna Balaprakash et al. — [Report of the 2026 Workshop on Next-Generation Ecosystems for Scientific Computing: Harnessing Community, Software, and AI for Cross-Disciplinary Team Science](http://arxiv.org/abs/2608.26519v1)
  <details><summary>📄 Abstract</summary>
  Scientific computing is undergoing rapid transformation as advances in artificial intelligence, heterogeneous computing, automation, and data-intensive research reshape not only computational tools but also the institutions, workforce models, and collaborative practices that support scientific discovery. This report synthesizes insights from the 2026 Workshop on Next-Generation Ecosystems for Scientific Computing, the second in a three-year series focused on strengthening scientific computing ec...
  </details>

- **2026-08-27** — Huanhuan Ma, Henry Peng Zou, Chengze Li et al. — [Sycophancy Suppression Can Impair Rational Updating: Anti-Sycophancy Should Preserve the Ability to Update](http://arxiv.org/abs/2608.26511v1)
  <details><summary>📄 Abstract</summary>
  Large language models often exhibit sycophancy, revising their answers to align with users when users push back. Such answer flips, however, can arise from different causes. One possibility is that the model simply aligns with the user's feedback in order to satisfy them. Another is that the feedback genuinely contains useful evidence, prompting the model to update its answer in a rational way. We distinguish them as Unsupported-Yielding and Rational-Updating. Prior work focuses primarily on sup...
  </details>

- **2026-08-27** — Shuyi Fan, Boyuan Deng, Mengyu Xu et al. — [Difference-in-Differences on a Censored Rating Scale Can Manufacture an Effect: Evidence from a Pre-Registered LLM-Judge Audit](http://arxiv.org/abs/2608.27309v1)
  <details><summary>📄 Abstract</summary>
  Audits of LLM judges certify a bias by contrasting matched conditions, and the strongest designs difference twice: a within-item contrast between two candidate responses, differenced again across a manipulated attribute, read off a bounded rating scale. We show that this endpoint is not identified on the scale that reports it. Each term of the double difference is censored by its own share, so the observed statistic confounds differential preference with differential attenuation: a severity shif...
  </details>

- **2026-08-27** — Haofeng Sun, Jiangbo Pei, Fei Kang et al. — [Riemann-1.0: An Embodied World Action Model for Physical AI](http://arxiv.org/abs/2608.27033v1)
  <details><summary>📄 Abstract</summary>
  We introduce Riemann-1.0, a fully causal autoregressive World Action Model for embodied intelligence. Riemann-1.0 jointly models multi-view visual observations, robot states, and embodiment-specific actions within a unified causal autoregressive sequence, representing robot actions and world evolution as causal state transitions. Unlike existing WAMs based on joint generation, video-first prediction, or decoupled modeling paradigms, Riemann-1.0 unifies online robot policy execution and action-co...
  </details>

- **2026-08-27** — Zihang Wang, Jianming Hu, Shang Su et al. — [MeshPriorDiT: Hierarchical Modeling for Action-Conditioned Cloth Dynamics](http://arxiv.org/abs/2608.26766v1)
  <details><summary>📄 Abstract</summary>
  Action-conditioned cloth dynamics prediction requires both locally plausible deformation and long-range coordination. Existing approaches largely follow two paradigms. Mesh-based GNNs capture local physical responses through material connectivity. However, their finite message-passing range limits coordination between topologically distant regions, while autoregressive rollouts tend to accumulate prediction errors. Transformer-based dynamics models capture long-range interactions through global ...
  </details>

- **2026-08-27** — Hiroki Sawada, Shunichi Kasahara — [PredVLA: A Sub-Million-Parameter Predictive-Coding Policy for Robot Manipulation](http://arxiv.org/abs/2608.26673v1)
  <details><summary>📄 Abstract</summary>
  Large pretrained vision-language-action models dominate modern robot-manipulation benchmarks, but it remains unclear how much model scale is necessary for strong language-conditioned control, or whether fundamentally different control architectures can remain competitive at much smaller parameter budgets. We present PredVLA, a language-conditioned predictive-coding policy with only 0.68 million trainable network parameters and no robot-data pretraining, whose hierarchical generative recurrent dy...
  </details>

- **2026-08-27** — Chanho Park, Daehyeon Choi, Jihyun Lee et al. — [Retrieval Heads Meet Vision: Uncovering How VLMs Locate and Extract Visual Information](http://arxiv.org/abs/2608.27417v1)
  <details><summary>📄 Abstract</summary>
  Vision-language models (VLMs) can locate an image region referred to by a text prompt and route the corresponding visual evidence to the output, yet the internal mechanism behind this behavior is not understood. Inspired by retrieval heads in large language models, we ask whether VLMs contain an analogous mechanism for visual retrieval. We answer affirmatively by introducing Visual Retrieval Heads (VRHs), a small subset of attention heads (about 1.7-2.6%) that are causally responsible for ground...
  </details>

- **2026-08-27** — Peiling Yi — [RCMN: Understanding Misleadingness in Influential Public Discourse](http://arxiv.org/abs/2608.27358v1)
  <details><summary>📄 Abstract</summary>
  Influential public discourse shapes public beliefs and can also mislead, not only through what is stated, but also through how information is framed, omitted, contextualised, and communicated. Yet less research has focused on how such misleadingness arises and shapes the interpretations formed by readers. To address this gap, we introduce Reader-Centric Misleadingness Understanding (RCMN), a framework that operationalises misleadingness through five dimensions: misleading mechanism, likely reade...
  </details>

- **2026-08-27** — Kai Sun — [Why Three Phases? A Historical and Engineering Reassessment of Phase Order in AC Power Transmission](http://arxiv.org/abs/2608.27325v1)
  <details><summary>📄 Abstract</summary>
  Three-phase alternating current is so deeply embedded in modern electric-power infrastructure that its phase order is often treated as self-evident. Historically, however, 1-phase and true 2-phase systems were commercially important, while commercial 6-phase transmission was later demonstrated. This paper reassesses why 3 phases became the dominant architecture for bulk AC transmission. A general balanced \(m\)-phase formulation is used to show that constant aggregate instantaneous power is not ...
  </details>

- **2026-08-27** — Mayanka Chandrashekar, Xi Zhang, Ethan Seefried et al. — [Decoupled I/O-Dominant Pipelines for Large-Scale Whole-Slide Image Embedding Extraction](http://arxiv.org/abs/2608.27278v1)
  <details><summary>📄 Abstract</summary>
  Whole-slide images (WSIs) are central to computational pathology but are prohibitively large, making patch-based processing the practical unit for foundation model inference. At scale, however, generating and handling massive numbers of patches on quickly introduces significant I/O and orchestration overhead, often dominating end-to-end performance. We present a decoupled, I/O-aware pipeline for large-scale WSI embedding extraction that decomposes the workflow into three stages: (1) patch genera...
  </details>


## 📊 统计 / Statistics

| 分类 / Category | 论文数 / Count |
|------|--------|
| jailbreak | 606 |
| prompt-injection | 517 |
| memory-poisoning | 45 |
| tool-use-attack | 130 |
| backdoor | 437 |
| adversarial-attack | 573 |
| privacy-leakage | 3964 |
| steganography | 61 |
| misuse | 956 |
| red-teaming | 120 |
| vulnerability | 2913 |
| defense | 2661 |
| alignment | 2467 |
| robustness | 2550 |
| watermark | 371 |
| unlearning | 93 |
| agent-safety | 52 |
| benchmark | 65 |
| survey | 309 |
| other | 7044 |

---

📚 **全部 25934 篇论文**（2022 至今）请访问 [GitHub Pages](https://ny1024.github.io/AgentSafety-Papers/) 查看完整列表、搜索与筛选。

⚠️ **本次更新跳过：arXiv API 爬取失败，数据为上次缓存。下次 CI 将自动重试。**

*Generated by AgentGuard at 2026-09-02 02:45:47*