<div align="center">

# AgentGuard 🛡️

**Daily Tracking of LLM Agent Security Papers on arXiv**

[![Auto Update](https://github.com/NY1024/AgentSafety-Papers/actions/workflows/daily-update.yml/badge.svg)](https://github.com/NY1024/AgentSafety-Papers/actions/workflows/daily-update.yml)
[![Papers](https://img.shields.io/badge/Papers-32171-blue)](#)
[![License](https://img.shields.io/badge/License-MIT-green)](#)

</div>

---

## 📖 简介 / Introduction

自动追踪 arXiv 上大模型 Agent 安全方向的最新论文，每日更新，关键词智能分类。

*Automatically tracking the latest LLM Agent security papers on arXiv, updated daily with keyword-based classification.*

**最近更新 / Last Updated**: 2026-10-10 11:46 ｜ **论文总数 / Total Papers**: 32171（近 30 天 / Recent 30 days: 4945）

🌐 **[GitHub Pages](https://ny1024.github.io/AgentSafety-Papers/)** — 查看全部 32171 篇论文（含摘要、分类筛选、搜索）/ View all 32171 papers with abstracts, filters & search

## 📑 分类导航 / Category Navigation

- **[jailbreak](#-jailbreak)** — 越狱攻击 / Jailbreak Attacks — 670
- **[prompt-injection](#-prompt-injection)** — 提示注入攻击 / Prompt Injection Attacks — 608
- **[memory-poisoning](#-memory-poisoning)** — 记忆投毒与篡改 / Memory Poisoning & Tampering — 55
- **[tool-use-attack](#-tool-use-attack)** — 工具使用攻击 / Tool-Use Attacks — 152
- **[backdoor](#-backdoor)** — 后门与投毒攻击 / Backdoor & Poisoning Attacks — 508
- **[adversarial-attack](#-adversarial-attack)** — 对抗攻击 / Adversarial Attacks — 632
- **[privacy-leakage](#-privacy-leakage)** — 隐私泄露 / Privacy Leakage — 4333
- **[steganography](#-steganography)** — 隐写与隐蔽通信 / Steganography & Covert Communication — 77
- **[misuse](#-misuse)** — 滥用与误用 / Misuse & Abuse — 1146
- **[red-teaming](#-red-teaming)** — 红队测试 / Red Teaming — 140
- **[vulnerability](#-vulnerability)** — 漏洞与攻击面 / Vulnerabilities & Attack Surfaces — 3528
- **[defense](#-defense)** — 防御与防护方法 / Defense & Protection Methods — 3373
- **[alignment](#-alignment)** — 对齐与安全约束 / Alignment & Safety Constraints — 3150
- **[robustness](#-robustness)** — 鲁棒性与可靠性 / Robustness & Reliability — 3409
- **[watermark](#-watermark)** — 水印与溯源 / Watermarking & Provenance — 575
- **[unlearning](#-unlearning)** — 机器遗忘 / Machine Unlearning — 112
- **[agent-safety](#-agent-safety)** — Agent 安全框架 / Agent Safety Frameworks — 64
- **[benchmark](#-benchmark)** — 安全评测与基准 / Safety Benchmarks & Evaluation — 67
- **[survey](#-survey)** — 综述与系统化 / Surveys & Systematization — 395
- **[other](#-other)** — 其他安全相关 / Other Security-Related — 9177

## 📄 近期论文 / Recent Papers (Last 30 Days)

> 仅展示最近 30 天中最新的 500 篇论文（含日期、作者、摘要）。近 30 天共 4945 篇，完整 32171 篇论文列表请访问 [GitHub Pages](https://ny1024.github.io/AgentSafety-Papers/)

> Showing the latest 500 of 4945 papers from the last 30 days (with date, authors & abstract). For the full list of 32171 papers, visit [GitHub Pages](https://ny1024.github.io/AgentSafety-Papers/)

### 📂 jailbreak
*越狱攻击 / Jailbreak Attacks* — 7 papers

- **2026-10-08** — Seyedarmin Azizi, Erfan Baghaei Potraghloo, Massoud Pedram — [One Word Opens the Gate: The Option-Channel Attack on Typed Decision Models as Agent Guardrails](http://arxiv.org/abs/2610.12292v1)
  <details><summary>📄 Abstract</summary>
  A typed decision model reads a piece of text and returns a probability over caller-defined options, each with a short written definition, generating no text. Recent work places these models in agent systems as guardrails: the component that reads a proposed tool call or incoming message and decides whether to allow it. We evaluate seven open-weight models in that role and report the two error directions separately: a fail-open error allows a prohibited action and is a vulnerability; a fail-close...
  </details>

- **2026-10-07** — William Hackett, Peter Garraghan — [BRANCH: Bypassing Multi-Scanner AI Guardrails](http://arxiv.org/abs/2610.10742v1)
  <details><summary>📄 Abstract</summary>
  AI systems increasingly rely on Large Language Models (LLMs) as core reasoning engines, making them targets for prompt injection and jailbreaks. Guardrails monitor and validate model inputs and outputs, yet their isolated, task-focused detection leaves gaps in their classification making them susceptible to bypasses. In response, guardrail systems formed by multiple scanners have emerged that collaboratively detect different types of malicious instructions, whereby shared latent representations ...
  </details>

- **2026-10-07** — Yi Wang, Xiuyuan Qi, Dongqi Han et al. — [Safe at One Loop, Risky at Another: Aligning Safety Across Recurrent Depths in Looped Language Models](http://arxiv.org/abs/2610.10625v1)
  <details><summary>📄 Abstract</summary>
  Looped Language Models (LoopLMs) provide a parameter efficient approach to scaling model capabilities through repeated use of shared parameters across recurrent steps. Since each recurrent depth can be read out independently, a single LoopLM exposes a broader output space across inference depths, raising an important question: whether safety is preserved throughout recurrent computation. Prior evaluations suggest that deeper recurrence can improve safety on harmful queries, but robustness under ...
  </details>

- **2026-10-07** — Alexi Canesse, Mathis Le Bail, Maël Jenny et al. — [PatchBench: Measuring Collateral Damage in Activation Patching](http://arxiv.org/abs/2610.10276v1)
  <details><summary>📄 Abstract</summary>
  An LLM safety patch can pass a benchmark while still being a poor repair. This risk is especially acute for jailbreak repairs, where the goal is to correct a specific unsafe behaviour without changing unrelated behaviours. A patch may block exact evaluation prompts yet fail on close harmful variants, or suppress harmful behaviour by over-refusing benign prompts that share its wording or structure. Existing protocols primarily test whether models can be broken, while aggregate metrics (attack suc...
  </details>

- **2026-10-07** — Juanyang Xu, Zheng Wang, Xingyu Zhao et al. — [From Expected Harmfulness to Likelihood: A Probabilistic Reformulation of Jailbreaking LLM Agents](http://arxiv.org/abs/2610.09973v1)
  <details><summary>📄 Abstract</summary>
  When the harmfulness of an LLM agent's output can be quantified, a natural jailbreaking objective is to maximize expected harmfulness over admissible input modifications. An alternative approach constructs or selects harmful target outputs and modifies the input to increase their likelihood. We establish a precise connection between these two approaches through a probabilistic reformulation. Specifically, we show that the gradient of the logarithm of expected harmfulness with respect to the inpu...
  </details>

- **2026-10-07** — Shuailong Wang, Xinyu Lyu, Shengming Yuan et al. — [Understanding and Mitigating Token-Pruning-Induced Vulnerabilities in VLMs](http://arxiv.org/abs/2610.09703v1)
  <details><summary>📄 Abstract</summary>
  Token-Pruning accelerates Vision-Language Models by removing redundant visual tokens, yet its safety implications remain underexplored. In this work, we present the first comprehensive safety evaluation of Token-Pruning mechanisms and find that: most pruning strategies significantly degrade safety as pruning ratios increase, whereas Query-based Compression shows the opposite, with extreme pruning (up to 99.8%), unexpectedly improves model safety. This sharp contrast prompts a key question: How d...
  </details>

- **2026-10-06** — Xunlei Qian, Yingqian Cui, Yuping Lin et al. — [Detecting Unseen Jailbreak Sources: A Multi-Source Conformal Detection Perspective](http://arxiv.org/abs/2610.09167v1)
  <details><summary>📄 Abstract</summary>
  Jailbreak defenses for large language models are usually calibrated on a fixed set of known attack methods. However, new attack methods keep appearing after deployment, and existing detectors are observed to degrade under the new attacks (Piet et al., 2025). This paper studies how to detect, from a stream of attack prompts, that the prompts come from an attack source outside the known ones. We formulate it as a sequential test whose null hypothesis is that the stream comes from one of the known ...
  </details>


### 📂 prompt-injection
*提示注入攻击 / Prompt Injection Attacks* — 4 papers

- **2026-10-08** — Luman Zhao, Minghui Xu, Yue Zhang et al. — [LTBD: Learnable Trust-Boundary Delimiters for Prompt Injection Defense](http://arxiv.org/abs/2610.11634v1)
  <details><summary>📄 Abstract</summary>
  Large language models (LLMs) perform remarkably well on complex tasks, yet remain highly vulnerable to prompt injection attacks, where malicious instructions embedded in external data can override user intent. Existing defenses remain limited by model fine-tuning requirements, vulnerability to adaptive attacks, or reliance on brittle handcrafted prompts. We argue that a fundamental source of this vulnerability is the lack of an explicit representation of trust provenance. To address this, we int...
  </details>

- **2026-10-07** — Zitong Yao, Jiangrong Wu, Yixi Lin et al. — [AgentTracer: Tracing Indirect Prompt Injection Attack through Fine-Grained Intention-Execution Alignment](http://arxiv.org/abs/2610.09935v1)
  <details><summary>📄 Abstract</summary>
  Large language model (LLM) agents interact with external resources to complete complex user tasks, exposing them to indirect prompt injection (IPI), where malicious instructions redirect agents toward attacker-intended tasks. Since IPI is difficult to defend against in real-world environments, post-incident tracing is essential for locating the injection source and reconstructing the attack chain. However, existing tracing methods primarily capture explicit control-flow and data-flow dependencie...
  </details>

- **2026-10-07** — Yupu Wang, Zhengyuan Jiang, Reachal Wang et al. — [Package Hallucination Attacks on Coding Agents through Prompt Injection in Rule Files](http://arxiv.org/abs/2610.09264v1)
  <details><summary>📄 Abstract</summary>
  Modern agentic coding frameworks increasingly rely on community-shared rule files (e.g., AGENTS.md or .cursorrules) to guide autonomous code generation, yet the security risks of this pipeline remain underexplored. To bridge this gap, we introduce the package hallucination attack, where an attacker injects malicious prompts into benign rule files to induce coding agents to replace legitimate dependencies with attacker-controlled packages. To obtain effective malicious prompts injected into rule ...
  </details>

- **2026-10-06** — Pengfei He, Deep Mitra, Vishesh Sharma et al. — [ASPIRE: Agentic Safety & Prompt Injection Red-teaming Engine](http://arxiv.org/abs/2610.08951v1)
  <details><summary>📄 Abstract</summary>
  LLM agents retrieve untrusted content and act through tools, creating indirect prompt-injection risks that can cause unauthorized actions or persistent state changes. Existing automated red-teaming largely optimizes payloads for pre-specified scenarios, leaving latent vulnerabilities across the agent's behavior space unexplored. We present ASPIRE, an Agentic Safety & Prompt Injection Red-teaming Engine for open-ended, behavior-level vulnerability discovery. ASPIRE maintains an evolving Agent Sec...
  </details>


### 📂 memory-poisoning
*记忆投毒与篡改 / Memory Poisoning & Tampering* — 1 papers

- **2026-10-06** — David Dobre, Leo Schwinn, Gauthier Gidel et al. — [Visual Memory Attacks Can Persist Through The KV Cache](http://arxiv.org/abs/2610.09027v1)
  <details><summary>📄 Abstract</summary>
  Modern language model systems operate autonomously over increasingly long contexts containing untrusted text and images. Can an adversarial input continue to steer a model even after that input is removed from its context? We show that attacks can be trained to persist through the key/value (KV) cache of subsequent tokens, allowing adversarial influence to outlive direct access to its source.We consider the Visual Memory Injection (VMI; Schlarmann and Hein, 2026) attack setting, in which an adve...
  </details>


### 📂 tool-use-attack
*工具使用攻击 / Tool-Use Attacks* — 2 papers

- **2026-10-08** — Fahd Seddik — [Skill Constellations: Tracing the Supply Chain of Agent Skills on GitHub](http://arxiv.org/abs/2610.11169v1)
  <details><summary>📄 Abstract</summary>
  Agent skills are SKILL.md instructions and scripts that AI coding agents such as Claude Code and Codex run with the permissions of their user. Developers share skills by copying them between repositories, which makes them a software supply chain without a registry, versions or provenance. The origin of a copied skill, the reach of a security fix and the repositories that warrant review are therefore unknown. Studies that record which repositories hold a skill at a single point in time cannot rev...
  </details>

- **2026-10-07** — Jie Liao, Simeng Qin, Wenqi Ren et al. — [PyCache Trap: The Inspection-Execution Gap in Agent Skill Scanners](http://arxiv.org/abs/2610.10612v1)
  <details><summary>📄 Abstract</summary>
  Agent skills combine instructions with executable resources, giving third-party packages access to an agent's runtime. Existing skill scanners inspect documentation and visible source, but Python may execute a bundled bytecode cache with different behavior. We study this gap between inspection and execution through PyCache Trap, which pairs benign source with a substituted cache accepted by the loader and connects it to a task-relevant invocation. Scanner-guided rewriting changes the invocation ...
  </details>


### 📂 backdoor
*后门与投毒攻击 / Backdoor & Poisoning Attacks* — 7 papers

- **2026-10-08** — Shutong Zheng, Sijia Chen — [When to Intervene? State-Aware Sparse Manipulation in Federated Reinforcement Learning](http://arxiv.org/abs/2610.11523v1)
  <details><summary>📄 Abstract</summary>
  Federated reinforcement learning (FRL) enables distributed agents to collaboratively train decision-making policies, but its decentralized training process also exposes global policy learning to Byzantine manipulation. Existing poisoning attacks primarily focus on how to construct malicious updates, while trajectory-level intervention timing remains largely implicit. In sequential decision making, however, where an intervention is applied can alter subsequent trajectories and learning signals. T...
  </details>

- **2026-10-07** — Jan Dubiński, Anna Sztyber-Betley, Jan Betley et al. — [Beyond Owls: Subliminal Learning Can Transfer Learned Capabilities and Backdoors](http://arxiv.org/abs/2610.10657v1)
  <details><summary>📄 Abstract</summary>
  In subliminal learning (SL), a teacher model passes on a trait to a student model by distillation on data semantically unrelated to the trait. So far, SL has been demonstrated for only a limited range of traits, including preferences for animals (e.g., owls) and malicious personas. These traits can also be elicited with simple prompts or with steering. Can SL transfer a wider range of traits, including more complex ones? If so, distillation might transfer subtle forms of misalignment (e.g., rewa...
  </details>

- **2026-10-07** — Sebastian Prasanna, Jacqueline Tay, Alek Westover — [Distillation for Incrimination and Distillation for Capabilities](http://arxiv.org/abs/2610.11012v1)
  <details><summary>📄 Abstract</summary>
  Powerful misaligned AI models might recognize alignment evaluations and strategically behave well on them, rendering direct audits uninformative. However, distilling such a model into a weaker benign student places the teacher in a Distillation Double Bind: if misalignment transfers, the student may conceal it less effectively, revealing evidence about the teacher; if it does not, the student may learn useful capabilities while remaining benign. We introduce two distinct distillation approaches,...
  </details>

- **2026-10-07** — Hui Zhang, Yachao Yuan, Jiayun Wang et al. — [SLDR: Defending Against Malicious Fine-tuning via Selective Layers Recovery and Dynamic Routing](http://arxiv.org/abs/2610.10345v1)
  <details><summary>📄 Abstract</summary>
  Fine-tuning-as-a-service enables users to adapt aligned large language models (LLMs) to specialized tasks, but malicious fine-tuning can erode refusal behavior while preserving task performance on legitimate inputs. We revisit recent layer-wise safety diagnostics and find that safety sensitivity is signed: scaling different layers can strengthen refusal, weaken it, or have little effect. Motivated by this observation, we propose SLDR, a post-fine-tuning defense based on Selective Layers Recovery...
  </details>

- **2026-10-07** — Xilin Wang, David Bau, Byron C. Wallace — [How to train your model organism](http://arxiv.org/abs/2610.10203v1)
  <details><summary>📄 Abstract</summary>
  Model organisms of alignment-relevant behaviors (e.g., backdoors, sycophancy, spurious correlations) have emerged as a key tool for evaluating whitebox interpretability techniques. We argue that the prevailing practice of training model organisms to a single objective of installing the target behavior is insufficient and propose validating model organisms with respect to three objectives with associated metrics: target-behavior installation, general-capability preservation (i.e., parametric know...
  </details>

- **2026-10-07** — Bojun Yang, Haochen Zhou, Zhifang Zhang et al. — [Purifying Backdoored Large Vision-Language Models by Removing Hijacked Directions](http://arxiv.org/abs/2610.09941v1)
  <details><summary>📄 Abstract</summary>
  Large vision-language models (LVLMs) are increasingly deployed in safety-critical applications, yet they remain vulnerable to backdoor attacks. Defending against such attacks remains costly, as existing methods require either extensive retraining on clean data or per-query intervention at inference time. To address this limitation, we propose OrthoPurify, a more efficient method to purify backdoored model weights via one-step orthogonal projection. Specifically, through structural analysis of ba...
  </details>

- **2026-10-07** — Zebin Yun, Eyal Ronen, Mahmood Sharif — [Backdooring Acoustic Foundation Models for Physically Realizable Triggers](http://arxiv.org/abs/2610.09819v1)
  <details><summary>📄 Abstract</summary>
  Acoustic foundation models (AFMs) have democratized acoustic applications, enabling powerful models for tasks ranging from speech recognition to speaker verification with minimal resources. However, the security of applications based on AFMs remains largely underexplored. Our work addresses this gap by proposing the Foundation Acoustic model Backdoor (FAB) attack, demonstrating that state-of-the-art AFMs are susceptible to backdooring under practical settings. Despite making minimal assumptions ...
  </details>


### 📂 adversarial-attack
*对抗攻击 / Adversarial Attacks* — 4 papers

- **2026-10-08** — Tao Yang, Jianying Zhou — [Does Target Alignment Mean Target Recovery? An Evidence-Ladder Study of Adversarial Claims on Contrastive Encoders](http://arxiv.org/abs/2610.11938v1)
  <details><summary>📄 Abstract</summary>
  Adversarial attacks on vision-language models optimize an image toward a text target, then cite the attacked model's similarity score as evidence of success. We ask whether that score - victim-space target alignment (VTS) - predicts recovery of the target by an independent model. We first build a measurement instrument: supervised judges outside the attacked geometry, real-target blend controls, shuffled-target negatives, and a reference level derived from a 50% target-image blend. Two preregist...
  </details>

- **2026-10-07** — Arash Vashagh, Roozbeh Razavi-Far — [Detecting Adversarial Images through Response Profiles of Vision-Language Models](http://arxiv.org/abs/2610.10436v1)
  <details><summary>📄 Abstract</summary>
  Adversarial perturbations can alter the predictions of frozen vision-language models (VLMs) while leaving their confidence and image--text similarity patterns seemingly plausible. We investigate whether we can identify adversarial inputs based on the broader way an image interacts with a collection of general semantic prompts. Our detector summarizes these responses using category-level statistics, relationships among prompts, deviations from clean reference distributions, and stability under we...
  </details>

- **2026-10-07** — Xiaoyi Pang, Haoyue Feng, Quanxin Shou et al. — [Black-Box Adversarial Patch Attacks on VLAs via Ancestor VLM Exploitation](http://arxiv.org/abs/2610.09708v1)
  <details><summary>📄 Abstract</summary>
  Vision-Language-Action models (VLAs) are increasingly deployed in safety-critical physical environments, yet their adversarial robustness remains poorly understood. Existing attacks typically assume white-box access or rely on surrogate VLAs, which rarely holds in real-world deployments. Our key insight is that most VLAs are adapted from a publicly released pretrained vision-language model (VLM), inheriting two capabilities essential for action generation: visual perception and instruction-condi...
  </details>

- **2026-10-06** — Mojtaba Nafez, Aref Mousavi, Mohammad Ebrahim Mahdavi et al. — [Breaking Adversarial Transferability in Fine-Tuned Speech Recognition](http://arxiv.org/abs/2610.09109v1)
  <details><summary>📄 Abstract</summary>
  Many organizations fine-tune publicly available pretrained Automatic Speech Recognition (ASR) models and deploy them in black-box settings, assuming limited access provides protection. We show this assumption is fragile: adversarial perturbations crafted on the public base model transfer effectively to fine-tuned target models, severely degrading performance and posing concerns for safety-critical applications. We propose TransferBreaker, a unified fine-tuning framework that suppresses adversari...
  </details>


### 📂 privacy-leakage
*隐私泄露 / Privacy Leakage* — 25 papers

- **2026-10-08** — Feifei Li, Runjie Wang, Xiaohan Zhang et al. — [When Scene Text Hijacks the Scene: Uncovering, Exploiting, and Mitigating Rendered-Text Semantic Leakage in Image Generation Models](http://arxiv.org/abs/2610.11286v1)
  <details><summary>📄 Abstract</summary>
  The reliability and accountability of image generative models (IGMs) are essential for building responsible and trustworthy AI systems. Recent IGMs, such as Nano Banana and GPT-Image, now support complex instruction following, realistic image synthesis, and controllable scene-text rendering. As these capabilities expand, safety analysis must also account for new control channels introduced by complex prompts. In this work, we study rendered-text semantic leakage, a largely overlooked phenomenon ...
  </details>

- **2026-10-08** — Xie Zhang, Chengxiao Li, Xuan Liu et al. — [TAP3D: Thermal-Assisted 3D Human Point Clouds](http://arxiv.org/abs/2610.11241v1)
  <details><summary>📄 Abstract</summary>
  Human body point clouds are a versatile representation for AI-enabled human sensing. However, existing methods using LiDAR, radar, and depth cameras suffer from inherent drawbacks in high cost, sparse reconstruction, and privacy concerns, etc. In this paper, we exploit low-cost thermal arrays and present TAP3D, the first system to reconstruct 3D human point clouds from body heat signatures, offering significant advantages in cost, density, human sensitivity, and privacy. To overcome major challe...
  </details>

- **2026-10-08** — Chang Liu, Deliang Ding — [What to Admit and How to Present: Governing Persistent Memory in LLM Agents](http://arxiv.org/abs/2610.11188v1)
  <details><summary>📄 Abstract</summary>
  Persistent memory can improve personalization in LLM agents but can also induce sycophancy and cross-domain leakage. We distinguish two governance decisions: admission, which determines what recalled information enters the working context, and presentation, which determines how admitted information is expressed. We implement two inference-time designs without retraining: factor-compiled admission (FC), which assesses whole memory entries, and permission-semantic admission (PS), which decomposes ...
  </details>

- **2026-10-08** — Dung Nguyen, Anil Vullikanti — [Local Sensitivity in Exponential Selection: Failure Modes and Valid Calibrations](http://arxiv.org/abs/2610.11870v1)
  <details><summary>📄 Abstract</summary>
  Selection is a task that chooses one element from a finite public candidate range to maximize a data-dependent score. In differential privacy (DP), the exponential mechanism (EM) samples a candidate at a temperature calibrated to the global sensitivity. In this paper, we study when dataset-dependent sensitivity can safely replace global sensitivity in private selection.   We propose three valid approaches. First, a private, high-probability upper bound on local sensitivity yields approximate DP,...
  </details>

- **2026-10-08** — Yutong Hu, Tianming Huang, Yanbo Zhao et al. — [Elucidating the Space of Enzymatic Reaction: A Unified Benchmark and Pretrained Model](http://arxiv.org/abs/2610.11694v1)
  <details><summary>📄 Abstract</summary>
  Existing reaction models primarily learn molecular transformations, whereas enzy- matic reactions depend jointly on molecular structure and catalytic function. We formulate this problem as learning an enzymatic reaction space linking reactants, products, and Enzyme Commission (EC) annotations. To characterize this space, we introduce VenusRX-Bench, a unified benchmark for forward reaction prediction, single-step retrosynthesis, and EC-number prediction. VenusRX-Bench integrates reactions from mu...
  </details>

- **2026-10-08** — Matěj Kripner, Milan Straka — [NanoProof: Open and Efficient Automated Theorem Proving in Lean 4](http://arxiv.org/abs/2610.11605v1)
  <details><summary>📄 Abstract</summary>
  We introduce NanoProof, to our knowledge the first factorized execution-guided theorem prover in Lean 4 whose training data, extraction tooling, training pipeline, and weights are all released, making it end-to-end reproducible using open-source resources. To this end, we build and release a dataset of structured proof trees, as well as a tool for programmatic interaction and data extraction within the Lean 4 formal verifier. To support sustainable research, we focus on compute efficiency to fac...
  </details>

- **2026-10-08** — Pengxin Guo, Shuang Zeng, Zonggen Li et al. — [Fed-GRPO: Reward-Signal-Driven Federated Group Relative Policy Optimization](http://arxiv.org/abs/2610.11502v1)
  <details><summary>📄 Abstract</summary>
  Large Language Models (LLMs) have shown strong reasoning capabilities when fine-tuned with reinforcement learning (RL), particularly through Group Relative Policy Optimization (GRPO). However, existing GRPO methods assume centralized access to training data, which may not hold in practice due to privacy or regulatory constraints. To this end, we propose Fed-GRPO, a federated GRPO training framework that addresses these privacy constraints by enabling collaborative reasoning training without shar...
  </details>

- **2026-10-08** — Rongxue Li, Meng Yang, Yiru Mao et al. — [SpatialOPSD: Self-Distilling Spatial Intelligence from Verified Coding Agent Traces](http://arxiv.org/abs/2610.11366v1)
  <details><summary>📄 Abstract</summary>
  Spatial coding agents significantly improve spatial reasoning in Multimodal Large Language Models (MLLMs) by using external tools to generate verified execution traces. However, this paradigm inherently suffers from prohibitive inference-time overhead and external dependencies. In this paper, we explore whether an MLLM can internalize this agentic capability to operate entirely tool-free. We begin with a simple observation: prompting an MLLM with summarized execution traces of a spatial coding a...
  </details>

- **2026-10-08** — Preeti Saraswat, Divya Neelagiri, Ajay Manoj — [Gated Memory: Admission-Controlled Memory Formation for Conversational AI](http://arxiv.org/abs/2610.11270v1)
  <details><summary>📄 Abstract</summary>
  Personalized conversational AI relies on long-term memory systems that extract facts from user utterances and store them in persistent vector stores. Despite progress in retrieval, deduplication, and lifecycle management, the formation stage, the moment a fact is first written to storage has received almost no principled attention. We identify this as the binding constraint on memory quality in production systems. Critical contextual signals, such as the distinction between a permanent user attr...
  </details>

- **2026-10-07** — Yixin Tan, Jiayang Liu, Lu Sun et al. — [When Routing Reveals Membership: Privacy Leakage from MoE Router Telemetry](http://arxiv.org/abs/2610.10616v1)
  <details><summary>📄 Abstract</summary>
  Mixture-of-Experts (MoE) language models produce routing information during inference that may be logged or exposed for monitoring, debugging, load analysis, and safety auditing. Unlike ordinary model outputs, this telemetry reveals a view of the model's internal computation, raising a privacy question: can it reveal whether an example was used to fine-tune the deployed model? We introduce a router-augmented membership inference attack that combines conventional output-side signals with aggregat...
  </details>

- **2026-10-07** — Sinara S. Dourado, Ciro Micheletti Diniz, Gabriel P. L. M. Fernandes et al. — [Engineering Quantum Interactions: From Effective Models to Validated Physical Predictions](http://arxiv.org/abs/2610.10763v1)
  <details><summary>📄 Abstract</summary>
  Effective models make complex quantum dynamics tractable by retaining only the states, processes, and timescales relevant to a given physical question. Their predictive power, however, depends on treating the retained manifold, initial state, observables, micromotion, dissipative channels, and eliminated degrees of freedom consistently. We develop a unified framework for constructing and validating effective descriptions using projection methods, Schrieffer--Wolff transformations, Magnus expansi...
  </details>

- **2026-10-07** — Nafiseh Ghoroghchian, Luis Scoccola, Tina Sedaghat et al. — [Conversational Task Disambiguation over Tabular Data: Leakage-Aware Formulation, Benchmark Suite, and Training](http://arxiv.org/abs/2610.10740v1)
  <details><summary>📄 Abstract</summary>
  Conversational task disambiguation over tabular data uses dialogue to resolve missing information about a user's intended task before producing a solution over tables or databases. Existing evaluation and training lack a leakage-aware foundation. Task success mixes the agent's disambiguation and solution-generation capabilities and can also reflect oracle leakage, that is, information that a user simulator reveals beyond what a real user would. Existing datasets also lack a shared representation...
  </details>

- **2026-10-07** — Wei Zhai, Xiang Liu, Qiang Huang et al. — [Nullify: Null-Space Activation Steering for Training-Free LLM Unlearning](http://arxiv.org/abs/2610.10655v1)
  <details><summary>📄 Abstract</summary>
  Large Language Models (LLMs) inevitably internalize substantial amounts of sensitive or private information during pre-training, while LLM unlearning aims to selectively erase specific knowledge to prevent privacy leakage with minimal loss of model utility. However, existing methods struggle to balance forget quality with utility, and typically incur substantial computational costs due to parameter fine-tuning. To address this, we propose Nullify, a training-free, non-destructive activation stee...
  </details>

- **2026-10-07** — Konstantinos Gyftodimos, Kyriakos Chiotis, Elena Politi et al. — [Temporal transformer CAN encoder with federated lightweight heads for anomaly detection](http://arxiv.org/abs/2610.10613v1)
  <details><summary>📄 Abstract</summary>
  Modern vehicles rely on large numbers of Electronic Control Units (ECUs) that constantly exchange information over the Controller Area Network (CAN) bus. Due to the rapidity, structure, and repetition of this communication, even slight variations in timing, payload values, or message patterns can point to unusual activity. Whether due to errors, malfunctions, or deliberate interference, these anomalies are frequently subtle and challenging to identify with conventional methods that handle messag...
  </details>

- **2026-10-07** — Junkai Chen, Yuhao He, Qianshan Wei et al. — [Open-MMUnlearning: Unifying Methods and Evaluation for MLLM Unlearning](http://arxiv.org/abs/2610.10358v1)
  <details><summary>📄 Abstract</summary>
  As multimodal large language models (MLLMs) become more capable and widely deployed, concerns about privacy and safety have become increasingly pressing. Machine unlearning offers one approach to addressing these concerns by removing designated information from trained models while preserving unrelated capabilities. However, fragmented implementations and evaluation protocols, incomplete robustness testing, and limited understanding of metric reliability make progress in MLLM unlearning difficul...
  </details>

- **2026-10-07** — Talal Alrawajfeh, Cristiana Diaconu, Ossi Räisä et al. — [Efficient Provably Private Classification with a Tabular Foundation Model](http://arxiv.org/abs/2610.10068v1)
  <details><summary>📄 Abstract</summary>
  Tabular data underpin prediction and decision-making in medicine, finance, government and science, but often contain sensitive individual-level information, creating a need for accurate prediction while preserving privacy. Traditional private learning provides formal privacy guarantees, but requires slow dataset-specific optimisation, suffers substantial utility loss under strong privacy, and is often difficult to apply correctly. Tabular foundation models adapt rapidly to new datasets, but exis...
  </details>

- **2026-10-07** — Teng-Ruei Chen — [Sensitive-Topic Leakage Through LLM Routing Metadata: Measurement and Mitigation](http://arxiv.org/abs/2610.09981v1)
  <details><summary>📄 Abstract</summary>
  LLM routers pick a cheap or expensive model per request by its content, and many gateways and some cloud platforms can log that choice with content logging off. We measure this privacy channel beyond token counts, accounting for noisy labels and repeated prompts. We run pre-registered studies on 1.7 million real requests (WildChat-1M, LMSYS-Chat-1M) with two cost/quality routers and a domain router, survey eleven systems' logging, and test post-processing defenses. At matched length, the shift's...
  </details>

- **2026-10-07** — Ankita Das, Ambarish Parthasarathy, Sumohana S. Channappayya et al. — [FedSSMCoOp: SSM Encoders for light-weight Federated Prompt Learning for Few-shot Classification](http://arxiv.org/abs/2610.09907v1)
  <details><summary>📄 Abstract</summary>
  Vision-Language Models (VLMs) have shown strong performance across a wide range of downstream vision tasks, thanks to the complementary information contained in the respective domains. Despite the performance gains, most of these approaches rely on aligning these domains using the cosine similarity metric, which fails to capture token-level structure and cross-modal interactions prior to the classification stage. This is especially critical in biomedical applications under federated constraints,...
  </details>

- **2026-10-07** — Xiao Han, Aoyang Quan, Xiangyu Zhao et al. — [LLM-Enabled UAV Dispatch: A System-Level Survey and Taxonomy](http://arxiv.org/abs/2610.09466v1)
  <details><summary>📄 Abstract</summary>
  Unmanned aerial vehicle (UAV) dispatch is beginning to move beyond isolated path planning and optimization-driven resource allocation toward system-level coordination supported by semantic reasoning and LLM-based interfaces. This survey provides a unified characterization of LLM-enabled UAV dispatch systems that bridges semantic intent, symbolic decision-making, and physical UAV execution. Rather than treating LLMs as standalone add-ons, we conceptualize them as a cross-layer semantic orchestrat...
  </details>

- **2026-10-07** — Vita Santa Barletta, Danilo Caivano, Rebecca Margiotta et al. — [BagDINO: Multi-View Baggage Re-Identification with DINOv3](http://arxiv.org/abs/2610.10160v1)
  <details><summary>📄 Abstract</summary>
  Mishandled checked baggage remains a recurrent issue in airport operations, and current recovery workflows still largely rely on tag-based tracking, which does not directly support visual identification when tag evidence is missing or unavailable. This paper investigates baggage re-identification as an instance-level retrieval problem in a multi-camera setting, leveraging DINOv3 foundation-model representations to match a query image against a gallery of registered baggage images. A Torchreid-st...
  </details>

- **2026-10-07** — Yong Cao, Markus Flicke, Haoyu He et al. — [LLM4Impact: Integrating Heterogeneous Information for Scientific Impact Prediction](http://arxiv.org/abs/2610.10138v1)
  <details><summary>📄 Abstract</summary>
  Predicting the future impact of a newly published paper is challenging because it must be inferred from heterogeneous evidence available at publication time. Existing approaches often rely on a single source of information or combine multiple sources without accounting for their different predictive roles. In this paper, we present LLM4Impact, an evidence-aware method for scientific impact prediction that learns to represent, integrate, and calibrate heterogeneous information. LLM4Impact combine...
  </details>

- **2026-10-07** — Prabhath Chellingi, Raviraja G, Viraj Bagal — [From Plausible Hierarchies to Useful Taxonomies: Evaluating Agentic Harnesses on Customer Feedback](http://arxiv.org/abs/2610.09377v1)
  <details><summary>📄 Abstract</summary>
  Taxonomies are the symbolic representations through which AI systems organize evidence, aggregate patterns, and answer questions over large document collections. Over customer feedback, the category tree decides how every record is counted and routed, which problems get seen, and which team owns them. Agentic harnesses now make it easy to generate a plausible-looking hierarchy, and such trees are checked today with generic, individually scoped checks: each name fits its description, sits under t...
  </details>

- **2026-10-06** — Michael Tang, Mahmoud Abdelgalil, Jorge I. Poveda — [The Deceptive Bandit Problem: Exploratory Coupling and the Fragility of Multi-Agent Learning](http://arxiv.org/abs/2610.09120v1)
  <details><summary>📄 Abstract</summary>
  Randomized exploration is central to bandit learning, multi-agent reinforcement learning, and zeroth-order policy search, yet its independence and privacy are usually only treated as technical assumptions. We show that these properties are critical for security purposes and demonstrate how an adversarial agent can exploit privileged information on another agent's exploration. We analyze a deceiver-victim pair in the minimal two-player strongly monotone setting, where a deceptive player obtains l...
  </details>

- **2026-10-06** — Rafid Ahmed, Joseph Fioresi, Mubarak Shah et al. — [CredLeakBench: Evaluating Credential Leakage and Recovery in LLM Agents](http://arxiv.org/abs/2610.08871v1)
  <details><summary>📄 Abstract</summary>
  Language model agents are increasingly deployed to automate everyday digital chores from managing emails and social media to handling banking and bills allowing users to step away from supervision. However, this capability also exposes sensitive information to phishing. Safe execution requires distinguishing malicious requests from genuine ones without simply refusing to act. Despite its practical importance, this problem remains underexplored and it is unclear whether current agents or existing...
  </details>

- **2026-10-06** — Thushara Manjari Naduvilakandy, Hyeju Jang, Mohammad Al Hasan — [Multi-Objective Aligned Small Language Model Framework for SUD Patient Dialogue Generation](http://arxiv.org/abs/2610.09209v1)
  <details><summary>📄 Abstract</summary>
  Substance Use Disorder (SUD) counseling requires patient responses that reflect underlying cognitive states such as beliefs, coping strategies, and readiness for change. Although large language models (LLMs) can generate fluent text, they often fail to produce cognitively coherent and clinically realistic patient behavior, especially under ethical and data-scarce clinical settings. Moreover, deploying frontier-scale LLMs in healthcare applications presents practical challenges including high com...
  </details>


### 📂 steganography
*隐写与隐蔽通信 / Steganography & Covert Communication* — 1 papers

- **2026-10-08** — Jun Yeong Lee — [Who Leads and Who Collects:Algorithmic Collusion in Markets of Heterogeneous Language Models](http://arxiv.org/abs/2610.11256v1)
  <details><summary>📄 Abstract</summary>
  Evidence that pricing algorithms collude comes from markets in which every seller runs the same algorithm. We ask what happens when they do not. Four language models from four providers, each at its cheapest tier, price in a four-firm logit Bertrand market without communication, in every homogeneous, two-by-two and fully mixed composi- tion (11 cells, 20 runs, 200 periods). Collusion is a property of the model: Claude and Gemini markets reach 72 to 79 percent of the monopoly rent, DeepSeek marke...
  </details>


### 📂 misuse
*滥用与误用 / Misuse & Abuse* — 17 papers

- **2026-10-08** — Neha Verma, Sungwon Kim, Kenton Murray et al. — [VFold: Symmetry-Aware Cross-Layer Value Cache Compression](http://arxiv.org/abs/2610.12338v1)
  <details><summary>📄 Abstract</summary>
  While caching key-value (KV) states accelerates Large Language Model (LLM) decoding, this cache can dominate memory usage at long context lengths. One solution is to compress this memory by exploiting inter-layer cache similarities. However, most existing techniques necessitate architectural changes to LLMs and incur substantial overhead. In this work, we propose a symmetry-aware value cache merging strategy that reduces cache memory while avoiding both harmful performance degradation and archit...
  </details>

- **2026-10-08** — Jiaming Zhang, Xuan Wang, Fuyao Zhang et al. — [Right Screen, Wrong Transition: World Models as Verifiers for GUI Agents](http://arxiv.org/abs/2610.11942v1)
  <details><summary>📄 Abstract</summary>
  A login screen that appears after a tap on Sign in is expected; the same screen after a tap on View order is an attack. For GUI agents, safety is therefore a property of the transition rather than of the screen, and a monitor that inspects only screens can be defeated by reusing a legitimate one. Judging a transition requires an expectation of what should have followed the action. Existing GUI world models provide one, but they output it as text, code, or images, so checking it against the obser...
  </details>

- **2026-10-08** — Haitong Jiang, Chunlin Liu, Sihan Tang et al. — [Same Outcome, Different Evidence: Intent Recovery in LLM Safety Evaluation](http://arxiv.org/abs/2610.11766v1)
  <details><summary>📄 Abstract</summary>
  Safety evaluations of large language models commonly summarize harmful-output behavior with attack success rate (ASR). Yet the same non-harmful outcome can arise for very different reasons. A model may recover a harmful task and refuse it, fail to recover the task, or respond to something else entirely. Distinguishing these cases becomes especially important under intent-obscuring prompts, where a low ASR does not reveal whether the evaluated task was actually engaged. To make this distinction e...
  </details>

- **2026-10-08** — Zeyu Ye, Yanchun Li, Sibei He et al. — [False Claims, Credible Images: A Red-Teaming Benchmark for Commercial Image Generators](http://arxiv.org/abs/2610.11112v1)
  <details><summary>📄 Abstract</summary>
  Image-generation models can now produce text-rich, natural-looking visual artifacts that are hard to distinguish from real-world evidence, such as news reports and textbook pages. Yet, the same capability introduces a new risk: these models can just as easily fabricate visual misinformation. Even commercial models (e.g., GPT-Image-2) readily produce it. Curiously, we find that these models can recognize a claim as false when asked, yet still render that very claim as credible visual evidence. Th...
  </details>

- **2026-10-08** — Zhi Rao, Yucheng Zhou, Qianran Sun et al. — [SignRAG: Unified Retrieval-Augmented Gloss-Free Sign Language Translation](http://arxiv.org/abs/2610.11371v1)
  <details><summary>📄 Abstract</summary>
  Contemporary decoder-only large language models (LLMs) have demonstrated strong capabilities across a wide range of domains. However, existing pretraining paradigms for gloss-free sign language translation (SLT) are largely designed around conventional encoder-decoder pretrained language models, which limits their direct applicability to decoder-only LLMs. To address this limitation, we propose SignRAG, a unified framework combining hierarchical pretraining, target-domain retrieval augmentation,...
  </details>

- **2026-10-08** — Shunyuan Zhou, Hao Chen, Tianyu Wang et al. — [RAG-Stress: Probing the Limits of Evidence Reliance in Retrieval-Augmented Generation](http://arxiv.org/abs/2610.11183v1)
  <details><summary>📄 Abstract</summary>
  Following retrieved evidence does not guarantee factual correctness: misleading evidence can induce a model to replace an answer it previously gave correctly. Standard accuracy measures obscure this behavior by combining answer replacement with preexisting errors. We introduce RAG-Stress, a controlled diagnostic protocol for examining the limits of evidence reliance in retrieval-augmented generation. The protocol holds the question and reference answer fixed, edits one assertion to support a des...
  </details>

- **2026-10-07** — Zhankai Ye, Yanning Wang, Yukai Jin et al. — [How Narrative Wrapping Affects LLM Refusal: A Cross-Language Benchmark and Defense](http://arxiv.org/abs/2610.11005v1)
  <details><summary>📄 Abstract</summary>
  Safety-aligned language models often refuse a harmful request stated directly but answer the same request inside a role-play or narrative wrapper. We measure this vulnerability across languages and registers: attack success on Qwen3-1.7B is already 89.4% in English and 93.0% in modern Chinese, and reaches 95.7% in Classical Chinese. We build GUISE, a benchmark for systematically studying this vulnerability. It includes parallel requests in English, modern Chinese, and Classical Chinese, matched ...
  </details>

- **2026-10-07** — Gaurav Patel, Jun Fang, Greg Ver Steeg et al. — [Enabling Preference-driven Unlearning in Few-step Distilled Text-to-Image Diffusion Models](http://arxiv.org/abs/2610.10859v1)
  <details><summary>📄 Abstract</summary>
  Text-to-image diffusion models are increasingly distilled into few-step variants and being deployed to enable fast inference. However, their ability to generate harmful or undesired content poses significant safety risks. Data-driven unlearning methods suppress targeted generations by fine-tuning model weights using specialized unlearning objectives. Crucially, these objectives implicitly rely on multi-step denoising dynamics, an assumption that breaks down for few-step distilled (FSD) models, r...
  </details>

- **2026-10-07** — Ravil Akhtyamov — [The Harness as the Only Mutable Surface: Compliance-Bounded Self-Evolution of LLM Agents in Credit Pipelines, with a Measured Admission Gate](http://arxiv.org/abs/2610.10629v1)
  <details><summary>📄 Abstract</summary>
  Self-improving LLM agents can adapt a credit pipeline to a changed rule, but an agent that rewrites itself destroys the artefact a supervisor reviews: a named change, a recorded test, an approval. We argue that self-evolution is reviewable only if it is confined to the runtime harness (instruction text, tool-call logic and primitive composition) while model weights stay fixed, so that every adaptation is a diff with a cause and a test attached. We give a dual-loop engine built on that bound, wit...
  </details>

- **2026-10-07** — William Guey, Rashik Jahangir, Pierrick Bougault et al. — [When AI Finds Hidden Messages, Does It Report?](http://arxiv.org/abs/2610.10620v1)
  <details><summary>📄 Abstract</summary>
  When an assistant encounters a message for another AI, does it tell its user? Four fixed model-provider deployments perform simulated source tasks in 1,280 ordinary-note and 128 enhanced-note sessions. Harmless and harmful messages have matched plaintext and ROT13 versions, with no-message controls. Observers receive no decoder or decoded meaning; a requested reference code incentivizes inspection. Asking for reports increases rule-detected notifications identifying another AI as recipient by 53...
  </details>

- **2026-10-07** — Miao Yu, Hao Huang, Lu Yuan et al. — [SafeEvo: Deciphering the Safety Alignment Mechanism and Evolution in Language Models](http://arxiv.org/abs/2610.09600v1)
  <details><summary>📄 Abstract</summary>
  Safety interpretability advances the study of Large Language Model (LLM) alignment from behavioral constraints driven by data or algorithms towards a deeper understanding of internal mechanisms. However, existing works have focused primarily on safety-related representations, attention heads, or neurons after alignment, while largely overlooking the safety mechanisms in pretrained-only models and their evolution across alignment checkpoints. To address this, we propose SafeEvo, an interpretabili...
  </details>

- **2026-10-07** — Yuyao Ge, Yiwei Wang, Yuchen He et al. — [SkillForge: Co-Evolving Skills and Agents via Dynamic Skill Lifecycles](http://arxiv.org/abs/2610.09832v1)
  <details><summary>📄 Abstract</summary>
  Memory-augmented reinforcement learning strengthens LLM agents' ability to solve complex long-horizon tasks. Skills are one such form of memory, pairing instructions with an applicability condition over task types. However, retaining every skill indiscriminately as the policy improves lets obsolete or harmful entries accumulate and mislead the agent. We propose SkillForge, an agentic RL method that compiles and evolves the skill library through a fitness-driven skill lifecycle of trial, active, ...
  </details>

- **2026-10-07** — Mohnish Harwani, Yujia Zheng — [Sequential Pretraining Favors Large Models](http://arxiv.org/abs/2610.09611v1)
  <details><summary>📄 Abstract</summary>
  Large neural networks often acquire capabilities that small models fail to learn. Does this stem from large models learning more representative features, or from being more robust to unaccounted-for adverse effects introduced during training? We define and quantify one such adverse effect, primacy bias, as the extent to which exposure to early data distributions impairs later learning. We show that small models can allocate learning capacity inefficiently toward early distributions, whereas suff...
  </details>

- **2026-10-07** — Litao Hu, Yutong Tang — [The Winner's Curse in LLM Self-Improvement Loops: Selection Noise, Lock-in, and Acceptance Rules](http://arxiv.org/abs/2610.09239v1)
  <details><summary>📄 Abstract</summary>
  Self-improving LLM systems propose changes to themselves and keep those that score better on a small evaluation set. We treat this keep-if-better step as selection under measurement noise, model the correlated errors of the candidates in a single decision, and study empirically what happens when the evaluation set is reused. In runs where Qwen models rewrite their own instructions and every candidate is also scored on 600 held-out items, most proposals after the first are harmful, and the model ...
  </details>

- **2026-10-06** — Ankush Checkervarty — [Coverage, Not Difficulty, Sets How Much Synthetic Data an Activation Probe Needs](http://arxiv.org/abs/2610.10594v1)
  <details><summary>📄 Abstract</summary>
  Activation probes that monitor deployed language models are trained on synthetic conversations, and how many a probe needs is open. We trace learning curves over 10-590 synthetic samples for three monitoring concepts, high-stakes situations, replies harmful to a person, and replies that do not follow the user's instruction, on fourteen held-out evaluation distributions and four probe models, varying the generator LLM and the prompt's detail. The need is set by what is monitored: probes for high-...
  </details>

- **2026-10-06** — Pavan Maddula — [Quad-State Safety Evaluation of Open-Weight Large Language Models on Non-Canonical Inputs](http://arxiv.org/abs/2610.09033v1)
  <details><summary>📄 Abstract</summary>
  Standard safety evaluations of large language models assess harmful requests written in canonical plain text, while models in real-world deployment routinely receive inputs containing emojis, altered spellings, encoded strings, and character-level variations. This work introduces the Adversarial Surface-Form Robustness Dataset (ASRD), comprising 2,100 prompts across seven distinct surface-form families. Five open-weight language models are evaluated across these prompts, producing 10,500 respons...
  </details>

- **2026-10-06** — Domenic Rosati, Alessa Carbo, Ali Dadsetan et al. — [Removing Information Content Does Not Certify Tamper Resistance in Open-Weight Models](http://arxiv.org/abs/2610.09004v1)
  <details><summary>📄 Abstract</summary>
  Does removing harmful information make open-weight models resistant to fine-tuning attacks? We show that mutual information at release alone cannot universally certify slow recovery. Function-preserving reparameterizations leave information unchanged while altering gradient-descent geometry, so an invariant certificate is bounded by the fastest reachable parameterization. We apply this principle to weight--data mutual information under training-data filtering and label--representation mutual inf...
  </details>


### 📂 red-teaming
*红队测试 / Red Teaming* — 6 papers

- **2026-10-08** — Saisab Sadhu, Shreeyans Arora, Pratinav Seth — [Cited but Not Consulted: A Counterfactual Audit of Legal Chain-of-Thought Faithfulness](http://arxiv.org/abs/2610.12361v1)
  <details><summary>📄 Abstract</summary>
  Large language models increasingly justify legal decisions by naming the statute or precedent behind a verdict, treated as evidence that the decision follows from it. We test this directly: holding case facts fixed, we substitute the named legal authority for an unrelated one and decode a model's evolving verdict from its hidden states. Across seven open-weight models (8B-70B) and four benchmarks spanning judicial and contractual reasoning, when explicitly required to justify a verdict by naming...
  </details>

- **2026-10-08** — Jingnan Zheng, Dongcheng Zhang, Yi Zhang et al. — [ReSI: Recursive Safety Improvement toward Resistant and Resilient AI](http://arxiv.org/abs/2610.12233v1)
  <details><summary>📄 Abstract</summary>
  Recursive self-improvement, the participation of AI systems in improving their own capabilities, is beginning to move from theoretical prospect to practice, posing both challenges and opportunities for safety alignment. Models evolve through frequent updates, and their safety alignment requires continual adaptation to each new checkpoint. Meanwhile, with evolving red-teaming methods exposing new vulnerabilities, safety improvement for each checkpoint needs to mitigate exposed vulnerabilities and...
  </details>

- **2026-10-08** — Erin Crawley, Hidenori Tanaka — [Ecology of AI Agents: Collaboration Creates a Population Threshold for Takeoff](http://arxiv.org/abs/2610.12436v1)
  <details><summary>📄 Abstract</summary>
  AI agents can now conduct real-world cyberattacks, scale up capabilities with the number of agents, and collectively pursue misaligned goals to obtain rewards. Together, these factors raise the risk of a population explosion of misaligned agents: agents could compromise computers and secretly deploy additional agents, creating a self-reinforcing cycle where larger populations develop greater collective cyber capability and expand further. This raises a fundamental question: What determines wheth...
  </details>

- **2026-10-07** — Georgios Koutidis, Nikolaos Kekatos, Tom Nianios et al. — [Constrained-Action AI Remediation for SIEM/XDR via a NeMo-Guardrails Proxy](http://arxiv.org/abs/2610.09906v1)
  <details><summary>📄 Abstract</summary>
  Security Operations Centers (SOCs) for information technology and operational technology share one incident-response problem: a flood of correlated alerts and too few analysts. Large Language Models (LLMs) are increasingly proposed as reasoning engines that triage alerts and, in autonomous deployments, issue commands that block IPs, kill processes, or quarantine files on production hosts. This coupling introduces a new risk: a single adversarial alert can become a remote code path through the LL...
  </details>

- **2026-10-07** — Subhabrata Majumdar, Rajlakshmi Chavan — [Defensive Sufficiency in a Stackelberg Model of AI Security](http://arxiv.org/abs/2610.09892v1)
  <details><summary>📄 Abstract</summary>
  Feedback from automated testing, human red teaming, and incident response can strengthen an AI system's defenses when discovered failures lead to effective repairs. We study when this feedback process provides sufficient protection and when investing in it is economically worthwhile. We begin by showing that an attack surface composed of finite number of inputs is defended with probability 1 if every unresolved attack has a persistent chance of discovery, repairs are effective, and subsequent up...
  </details>

- **2026-10-07** — Wanjing Han, Levi Taiji Li, Mu Zhang et al. — [Adversarial Images Hijack Web Agents from Visual Grounding to Browser Execution](http://arxiv.org/abs/2610.09240v1)
  <details><summary>📄 Abstract</summary>
  Modern web agents built on large vision-language models process webpages, select relevant UI elements, and translate model outputs into browser actions. Existing visual red-teaming approaches use adversarial visual content to manipulate this process. However, they primarily target model inference and do not explicitly account for structured input processing or action post-processing. Consequently, model-level success does not establish control over browser execution and cannot reliably character...
  </details>


### 📂 vulnerability
*漏洞与攻击面 / Vulnerabilities & Attack Surfaces* — 45 papers

- **2026-10-08** — Abbas Raftari — [From Reactive Containment to Proactive Assurance: Lessons from OpenAI, Anthropic, and Google Agent Security Incidents](http://arxiv.org/abs/2610.12463v1)
  <details><summary>📄 Abstract</summary>
  In 2026, cybersecurity evaluations involving OpenAI, Anthropic, and Google agents reached real systems outside their authorized test scope. The paths were different. OpenAI agents exploited research infrastructure, coordinated across runs, and compromised parts of Hugging Face's production environment. Anthropic reported cases in which a misconfigured third-party environment exposed real systems to agents pursuing simulated cyber tasks. In a separately reported evaluation, Google's Gemini access...
  </details>

- **2026-10-08** — Shashank Hegde, Alexander Popov, Elie Aljalbout et al. — [LeWAM: A JEPA World Action Model with Diffusion-Steering-Based MPC](http://arxiv.org/abs/2610.12407v1)
  <details><summary>📄 Abstract</summary>
  World action models (WAMs) predict actions and future observations, typically from a reconstruction-based representation that carries noisy, redundant information which can complicate downstream predictions. We introduce LeWAM, a bidirectional transformer for forward, backward, inverse dynamics and policy prediction, on a decoder-free JEPA latent trained end-to-end through all four modes. We see the following benefits: 1) Alignment: linear probes read robot and object state from LeWAM's latent b...
  </details>

- **2026-10-08** — Jialu Wang, Ruichen Zhang, Xiaoou Liu et al. — [GeoReform: Reflective Formalization Evolution for Multimodal Geometry Problem Solving](http://arxiv.org/abs/2610.12391v1)
  <details><summary>📄 Abstract</summary>
  Multimodal large language models (MLLMs) often struggle to identify and use geometric relations in diagrams. Recent methods address this challenge by converting geometric entities, relations, and constraints into explicit textual representations for the model to reason over. However, effective formalization is highly non-trivial: on Geometry3K, structure injection fixes 28 errors but introduces 13 new ones among 200 examples. Redundant relations can distract the model, while ambiguous references...
  </details>

- **2026-10-08** — Adhila Nazarudeen, Silvia Ortín, Apostolos Argyris — [Spatiotemporal computing for temporal nonlinear tasks using few-mode fiber and SOA nonlinearity](http://arxiv.org/abs/2610.12173v1)
  <details><summary>📄 Abstract</summary>
  Step-index few-mode fibers (FMFs) provide a compact passive platform for high-speed photonic information processing by exploiting modal dispersion to map temporal inputs into spatiotemporal representations with short-term memory. In previous studies, we have demonstrated linear classification tasks with such FMFs, such as ultrafast multibit header recognition. Here, we extend the computational capability of such architectures towards solving nonlinear tasks by introducing an optical nonlinearity...
  </details>

- **2026-10-08** — Georgios Milis, Tom Sander, Tomáš Souček et al. — [Could LLM Watermark Detection be Public?](http://arxiv.org/abs/2610.12106v1)
  <details><summary>📄 Abstract</summary>
  Watermarking large language models is popular for tracing chatbot and agentic outputs, yet detectors remain unreleased since exposing them could let attackers do targeted edits with the detector's feedback. However, watermarks are already vulnerable to uninformed tampering attacks. We thus first quantify whether a public detector would be an additional liability in a deployment setting at varying levels of access, from token-level scores to a binary verdict. Second, we introduce a split-key publ...
  </details>

- **2026-10-08** — Yutong Xie, Jiawei Tang, Zhenglin Hua et al. — [Do Not Train Away Uncertainty: Early Uncertainty Anchored Calibration](http://arxiv.org/abs/2610.12048v1)
  <details><summary>📄 Abstract</summary>
  Deep neural networks, including large language models, have achieved remarkable performance across various tasks. However, they are prone to overconfidence during training or fine-tuning. In this work, we observe a consistent phenomenon across different models that the early model is better calibrated, while later training or fine-tuning yields marginal accuracy gains but substantially increases calibration errors. Our analysis suggests that the early model retains uncertainty awareness in both ...
  </details>

- **2026-10-08** — Daniel Thilo Schroeder, Philipp M. Lutscher, Samba Dialimpa Badji et al. — [Automated Disinformation and Malicious AI Swarms: Risks for Democracy and Development in Africa](http://arxiv.org/abs/2610.11930v1)
  <details><summary>📄 Abstract</summary>
  Generative artificial intelligence is reshaping how information is produced, accessed, and circulated, while enabling disinformation campaigns of increasing scale and sophistication. There is currently no clear evidence that fully autonomous AI swarms conduct influence operations at scale, but their enabling capabilities are advancing. We define malicious AI swarms as coordinated, persistent, and adaptive multi-agent systems designed for influence operations, distinguishing them from AI-assisted...
  </details>

- **2026-10-08** — Steve Nouyep, Sébastien Salva, Maxime Puys — [A Security Meta-Model for Retrieval-Augmented Generation Systems](http://arxiv.org/abs/2610.11893v1)
  <details><summary>📄 Abstract</summary>
  Retrieval-Augmented Generation (RAG) systems extend large language models (LLMs) with external knowledge through a multi-stage pipeline. While this architecture can improve the factual grounding of generated answers, it introduces structural attack surfaces that extend beyond those of standalone LLMs. In this paper, we introduce a security meta-model that captures explicit causal relationships between RAG surfaces, attacks, weaknesses, risks, and CIA impact (Confidentiality, Integrity, Availabil...
  </details>

- **2026-10-08** — Varun Gumma, Navonil Majumdar, Soujanya Poria — [SemField: A Simple, Linear, Continuous, yet Robust Semantic Watermark](http://arxiv.org/abs/2610.11848v1)
  <details><summary>📄 Abstract</summary>
  The rapid proliferation of Large Language Models (LLMs) necessitates reliable watermarking techniques to identify AI-generated text and ensure appropriate attribution. While token-based watermarks are vulnerable to paraphrasing, a central challenge for semantic watermarking is to turn sentence meanings into a stable, well-calibrated document-level signal. To this end, we introduce SemField, a simple, training-free semantic watermark that embeds a continuous, linear signal directly into the sente...
  </details>

- **2026-10-08** — Heyang Tan, Chengxin Gao, Xin Wen et al. — [ObliVul: Alert-Conditioned Safety Obligation Modeling and Bidirectional Counterfactual Validation for Code Vulnerability Detection](http://arxiv.org/abs/2610.11801v1)
  <details><summary>📄 Abstract</summary>
  In real-world software development, the primary challenge in vulnerability detection is often not finding suspicious code, but identifying which alerts among the large number of candidate alerts produced by static analysis truly warrant attention. Existing learning-based methods mainly identify suspicious patterns at the function or line level, making it difficult to extract complete program evidence centered on an individual alert. Although large language models can infer risk sources, dangerou...
  </details>

- **2026-10-08** — Simon Gabet, Etienne Boursier, Claire Boyer — [Softmax Attention on Gaussian Mixtures: Linear When It Can, Selective When It Must](http://arxiv.org/abs/2610.11798v1)
  <details><summary>📄 Abstract</summary>
  Softmax attention, at the heart of Transformers, has demonstrated remarkable capabilities. Yet its underlying mechanisms remain only partially understood. Recent theoretical work studies Gaussian prompts, where the infinite-prompt limit reduces softmax attention to a linear map, but also removes the query-dependent selection that distinguishes it from linear attention. This work studies the infinite-prompt limit of softmax attention on Gaussian mixtures, which retain the tractability of Gaussian...
  </details>

- **2026-10-08** — Thang X. Vu, Cuong Le, Symeon Chatzinotas et al. — [Distributed Constrained Resource Management in 6G Networks: A Scalable Hybrid Model-Learning Framework](http://arxiv.org/abs/2610.11739v1)
  <details><summary>📄 Abstract</summary>
  Radio Resource Management (RRM) is a fundamental challenge in 6G wireless networks, particularly under dynamic user demands, inter-cell interference, and heterogeneous QoS constraints. Centralized optimization solutions are often infeasible in practice due to the lack of system-wide state information, dynamic conditions, and signaling delays, making distributed learning-based approaches attractive. However, conventional multi-agent reinforcement learning (MARL) struggles with scalability and con...
  </details>

- **2026-10-08** — Haobo Jiang, Liang Yu, Jianmin Zheng — [PointVGGT: Zero-Shot Multiview RGB-D Point Cloud Registration with Visual Geometry Foundation Priors](http://arxiv.org/abs/2610.11612v1)
  <details><summary>📄 Abstract</summary>
  This paper addresses multiview RGB-D point cloud registration, aiming to estimate global rigid poses for unordered RGB-D scans and align them in a metrically consistent coordinate frame. The conventional pairwise-then-global paradigm suffers from locally optimized pairwise registration, severe error propagation and high computational burden. In particular, existing methods typically treat RGB data as a mere auxiliary matching cue and overlook the holistic geometric priors (e.g., camera poses and...
  </details>

- **2026-10-08** — Li Lu, Yanjie Zhao, Hongjie Chen et al. — [Where Do the Tokens Go? Understanding and Reducing Costs in LLM Agents for Vulnerability Discovery](http://arxiv.org/abs/2610.11602v1)
  <details><summary>📄 Abstract</summary>
  LLM agents can spend millions of tokens during vulnerability discovery without producing a working proof of concept (PoC). What consumes that budget, and why does it fail to produce results? We diagnose these costs and failures through a multi-axis open-coding study of 200 CyberGym traces, spanning four agents (i.e., Codex, OpenCode, Cybench, and EnIGMA) under an unaided baseline and four existing efficiency methods. The study reveals three key findings. First, different agents vary substantiall...
  </details>

- **2026-10-08** — Shunpu Tang, Qianqian Yang, Seung-Woo Ko et al. — [Model-Driven Deep Learning with Rank-One Sensing for Efficient CSI Feedback](http://arxiv.org/abs/2610.11558v1)
  <details><summary>📄 Abstract</summary>
  Downlink channel state information (CSI) feedback is essential for beamforming optimization in frequency-division duplex (FDD) massive multiple-input multiple-output (MIMO) systems. However, the feedback overhead increases with the number of antennas and subcarriers, posing a major challenge to practical deployment. Although recent deep learning (DL)-based methods reduce this overhead by compressing CSI at the user equipment (UE) and reconstructing it at the base station (BS), most of them treat...
  </details>

- **2026-10-08** — Varun Kohli, Lee Bing Cheng, Nur Hazim Ghazali et al. — [SoK: Are LLMs Reliable at Source Code Recovery? A Taxonomy and Empirical Evaluation](http://arxiv.org/abs/2610.11556v1)
  <details><summary>📄 Abstract</summary>
  Effective source recovery is critical to security applications such as malware analysis, vulnerability assessment, and legacy maintenance. Large Language Models (LLMs) are reshaping this field, shifting the paradigm away from rule-based heuristics to probabilistic and high fidelity semantic recovery of source code from assembly or classical decompiler-derived pseudo-C. However, despite rapid progress, the field suffers from fragmentation across numerous approaches as well as their non-unified ev...
  </details>

- **2026-10-08** — Lechen Li, Rongye Shi, Wanhuan Zhou — [Learning to Orchestrate Evolutionary Search: Progression-Aware Deep Reinforcement Learning for Dynamic DE-CMA-ES Coordination in Optimization and Structural Model Updating](http://arxiv.org/abs/2610.11546v1)
  <details><summary>📄 Abstract</summary>
  Solving high-dimensional structural model updating problems requires an algorithm capable of navigating complex, non-convex landscapes with correlated parameters. Existing hybrid evolutionary algorithms typically rely on static architectures or fixed switching rules, resulting in disjointed search phases. To address this, this study proposes a Deep Reinforcement Learning-governed dynamic DE-CMAES Orchestration (DRL-DCO) algorithm, in which a Deep Deterministic Policy Gradient (DDPG)-based actor-...
  </details>

- **2026-10-08** — Hongliang Liu — [Adversarial Cues in Decision Models Used as Judges: The Role of Request Presentation](http://arxiv.org/abs/2610.11436v1)
  <details><summary>📄 Abstract</summary>
  An answer judge instructed to grade the final commitment should reject an explicitly wrong final value even when an earlier value matches the reference. We show that adding one colon to a candidate can violate this requirement depending on the presentation of the structured judging request. Numeric references certify the error, and paired interventions distinguish the candidate edit from the integration's presentation choices. On 200 previously unused DROP and GSM8K source clusters, the edit inc...
  </details>

- **2026-10-08** — Kun Wang, Yupeng Hu, Ruping Cao et al. — [GroundSight at GroundLM 2026 Shared Tasks: GoldenViewVQA](http://arxiv.org/abs/2610.11402v1)
  <details><summary>📄 Abstract</summary>
  GoldenViewVQA requires models to jointly answer driving-scene questions and identify the camera view containing the supporting visual evidence, making precise evidence localization as important as answer correctness. We present \textbf{CoVeR-VQA}, a training-free multi-stage verification and correction framework for grounded multi-view VQA. Starting from GPT-5.6 zero-shot predictions, CoVeR-VQA progressively applies view-specific verification with Gemini-3.6-Flash, prior-guided joint verificatio...
  </details>

- **2026-10-08** — Francesco I. Re, Shubhangi Ghosh, Tim Vieira et al. — [Estimating great expectations under autoregressive language models with potentials](http://arxiv.org/abs/2610.11399v1)
  <details><summary>📄 Abstract</summary>
  Many applications of language models hinge not on individual samples but on the expectation of a test functional under the model. Estimating such expectations reliably can be computationally expensive. In this paper, we show how to make estimation more efficient by exploiting the next-token conditional probabilities which are available as a by-product of sampling. We do so through potentials: real-valued functions on prefixes that decompose the test functional additively. We construct an estimat...
  </details>

- **2026-10-08** — Navam Obeysekara, Nevidu Jayatilleke — [Fact over Fiction: Detection of Pathological Hallucinations in Sinhala-to-English Neural Machine Translation](http://arxiv.org/abs/2610.11389v1)
  <details><summary>📄 Abstract</summary>
  Neural Machine Translation (NMT) models, while capable of producing highly fluent outputs, remain vulnerable to hallucinations, which are translations that are natural yet semantically unrelated to the source. This vulnerability is acute in low-resource settings like Sinhala-to-English, where weak cross-lingual alignment leads to hallucinations. This paper introduces a framework for reference-free hallucination detection in this language pair. We present a 45,000-sample synthetic dataset generat...
  </details>

- **2026-10-08** — Jun Yao, Chao Wang, Yupeng Qiu et al. — [ProxyEraseAgent: Blind Watermark Removal in the Wild](http://arxiv.org/abs/2610.11290v1)
  <details><summary>📄 Abstract</summary>
  Invisible image watermark removal has received growing attention. Despite substantial progress, existing attacks face a tension between practicality and specificity. Attacks exploiting detector outputs, decoder responses, or paired images can be tailored to the watermark decision boundary, but require information rarely available in realistic scenarios. Conversely, attacks based on compression, geometric distortion, or reconstruction are easily deployed from a single watermarked image, but remai...
  </details>

- **2026-10-08** — Minghan Jiang, Jiayi Wang, Shuaiting Li et al. — [DynaTE: Accelerating Diffusion LLMs via Dynamic Token Execution](http://arxiv.org/abs/2610.11284v1)
  <details><summary>📄 Abstract</summary>
  Diffusion-based LLMs (dLLMs) have recently emerged as a promising alternative to autoregressive (AR) LLMs by enabling bidirectional parallel refinement, alleviating the sequential decoding bottleneck of AR generation. However, their parallel iterative refinement mismatches AR accelerators optimized for sequential decoding and their discrete token generation differs from DiT accelerators designed for continuous denoising. Recent dLLM accelerators have explored workload-specific optimizations to r...
  </details>

- **2026-10-08** — Yulin Sun, Kele Xu, Yong Dou — [Selective Listening: Mechanism-Guided Control of Audio Influence in Large Audio-Language Models](http://arxiv.org/abs/2610.11196v1)
  <details><summary>📄 Abstract</summary>
  Large audio-language models (LALMs) exploit multimodal evidence, yet task-irrelevant audio can alter text-reasoning decisions when listening is unnecessary. Aggregate Accuracy can hide this paired drift because audio-induced repairs and damages may cancel. Paired drift analysis and targeted interventions identify architecture-specific, intervention-sensitive late audio pathways as actionable control points. We introduce ICAP-Gate, which applies mechanism-guided, task-conditioned control to each ...
  </details>

- **2026-10-08** — Shengsheng Lin, Jing Hu, Zhengyang Hu et al. — [RideBench: A Large-Scale Exogenous-Aware Benchmark for Ride-Hailing Time Series Forecasting](http://arxiv.org/abs/2610.11164v1)
  <details><summary>📄 Abstract</summary>
  We release Ride-Hailing, a large-scale ride-hailing time series dataset synthesized from DiDi's marketplace data across 200 spatial areas. Ride-Hailing spans four consecutive years at half-hourly granularity and covers three representative exogenous scenarios: Weather Disturbance, Holiday Effect, and Large-scale Event Impact. Built upon Ride-Hailing, we introduce RideBench, a comprehensive benchmark for exogenous-aware ride-hailing forecasting, covering both regular week-ahead forecasting and lo...
  </details>

- **2026-10-08** — Minchan Kwon, Seunghee Koh, Sunghyun Baek et al. — [Do LLMs Learn from Rewards in Context? : Rethinking the role of reward in In-Context Reinforcement Learning](http://arxiv.org/abs/2610.11152v1)
  <details><summary>📄 Abstract</summary>
  LLM agents increasingly improve at inference time by accumulating experience in context rather than by updating parameters. This process is often described as in-context reinforcement learning (ICRL). Whether in-context learning (ICL) can actually play the role of RL, however, has not been tested. We study this question in its simplest form, direct ICRL, where the model conditions directly on raw trajectory-reward pairs, and ask whether the reward acts as a learning signal. Through controlled ex...
  </details>

- **2026-10-08** — Shuang Zheng, Xing Zhang, Quan Z. Sheng et al. — [Topology-Aware Cooperative Beam-Hopping Scheduling for Efficient Resource Allocation in LEO Satellite Systems](http://arxiv.org/abs/2610.11103v1)
  <details><summary>📄 Abstract</summary>
  The dynamic topology and heterogeneous traffic demands of multi-satellite systems present substantial challenges for beam-hopping (BH) resource management. This letter develops a topology-aware cooperative BH framework for multi-satellite systems under partial observability. A lightweight load-balancing scheme first determines the serving relationships, which are then exploited to construct an association-induced satellite-user graph. A two-phase graph neural network (GNN) extracts episode-level...
  </details>

- **2026-10-07** — Junwei Quan, Evgenii Opryshko, Rohan Subramani et al. — [RH-Detect: A Unified Benchmark for Reward Hacking Detection](http://arxiv.org/abs/2610.10947v1)
  <details><summary>📄 Abstract</summary>
  Reward hacking, where a model exploits an evaluation signal without completing the intended task, threatens the reliability of deployed language model systems. Existing datasets use different labels, response formats, and metadata conventions, making detector results difficult to compare. We present RH-Detect, a benchmark that combines reward-hacking-relevant subsets from eleven public datasets, comprising 92,761 rows and six behavior categories, into a common schema. On 5,021 open-ended evaluat...
  </details>

- **2026-10-07** — Adam Y. J. Jones, Yu Yuan, Sergio Maffeis — [Speedbumps: Rejection Attacks on Speculative Decoding](http://arxiv.org/abs/2610.10929v1)
  <details><summary>📄 Abstract</summary>
  Speculative decoding is a popular technique for increasing the speed and reducing the costs of large language model (LLM) inference by verifying multiple draft tokens in a single target-model forward pass. The resulting benefit depends on the ability of the drafter to approximate the target model's distribution. In this work, we study Speculative Rejection Attacks (SRAs), a novel class of attacks that cause draft and target models to disagree more often, resulting in fewer draft tokens being acc...
  </details>

- **2026-10-07** — Jasper Gerigk, Kenzo Aspuru-Takata, Chin-Hsuan Wu et al. — [When Listening Becomes Easier: Scrubbing Visual Cues for Shortcut-Free VLAs](http://arxiv.org/abs/2610.10912v1)
  <details><summary>📄 Abstract</summary>
  Shortcut learning is a prevalent issue in robot learning. The limited diversity of robot demonstration datasets can mislead policies into exploiting spurious correlations between tasks and irrelevant features, such as viewpoint or background. Collecting sufficiently diverse robot demonstrations is costly and inefficient, motivating algorithmic alternatives. We focus on vision-language-action (VLA) models and discover that different vision-language model backbones exhibit substantially different ...
  </details>

- **2026-10-07** — Yara Zgheib, Marc Antonini, Roula Nassif — [Decentralized collaborative continual learning: A multi-objective minimization-based technique](http://arxiv.org/abs/2610.10882v1)
  <details><summary>📄 Abstract</summary>
  In this work, we formulate decentralized continual learning within a multi-objective optimization framework. For a given inference task t (corresponding to a common minimizer shared by the cost functions of all agents), agents collecting data in a distributed and streamed manner are only allowed to perform local computations and to exchange information with neighboring agents over the underlying communication graph. As tasks evolve sequentially over time, agents must adapt to newly arriving task...
  </details>

- **2026-10-07** — Pedro Farinha — [Applying Security by Design at the Point of Execution: How Governed Security Requirements Affect the Security of AI-Generated Code](http://arxiv.org/abs/2610.10659v1)
  <details><summary>📄 Abstract</summary>
  Security by design asks that security requirements are defined before code is written. Secure-code benchmarks typically measure the opposite situation: the agent receives the task without requirements and is scored with security tests it has not seen. We measured what changes when security requirements, selected from a governed security-by-design knowledge base (SbD-ToE) and delivered through a Model Context Protocol (MCP) server, are given to the generator at the point of execution. On DualGaug...
  </details>

- **2026-10-07** — Xiangtao Kong, Shuaizheng Liu, Rongyuan Wu et al. — [HarnessIR: Harnessing Multimodal Foundation Models for Universal Real-World Image Restoration](http://arxiv.org/abs/2610.10133v2)
  <details><summary>📄 Abstract</summary>
  Real-world low-quality images suffer from complex mixed degradations, including but not limited to noise, blur, atmospheric effects, etc. Recent agentic methods usually model real-world image restoration (Real-IR) as a sequential tool calling problem over task-specific single-degradation restoration models. This paradigm, however, is fundamentally limited because complex real-world degradations cannot be cleanly undone degradation by degradation, and the tool used for task-specific models caps t...
  </details>

- **2026-10-07** — Aleksandar Armacki, Haoyuan Cai, Ali H. Sayed — [Decentralized SGD under Heavy-Tailed Noise: Optimal Convergence Rates and the Role of Gradient Clipping](http://arxiv.org/abs/2610.10527v1)
  <details><summary>📄 Abstract</summary>
  Heavy-tailed noise has been widely observed in modern machine learning, motivating the use of methods like gradient clipping and normalization. While these methods are well understood in centralized settings, much less is known in decentralized ones, where applying a nonlinearity to local gradients affects both optimization and consensus. Recent works on decentralized non-convex optimization have studied both clipping and normalization under heavy-tailed noise, with clipping yielding suboptimal ...
  </details>

- **2026-10-07** — Hao-Run Cai, Si-Yang Liu, Zi-Jian Cheng et al. — [Thinking in Depth: Retrospective Inference for Tabular Foundation Models](http://arxiv.org/abs/2610.10317v1)
  <details><summary>📄 Abstract</summary>
  Tabular foundation models (TFMs) are pretrained across diverse tabular tasks and make predictions on a new table at inference time using its labeled examples as context. Most recent TFMs perform such in-context prediction with stacked Transformer layers, repeatedly transforming how examples are represented and compared. By tracing individual queries through several strong TFMs, we find that predictive refinement is highly uneven across depth and is often concentrated in later layers. This uneven...
  </details>

- **2026-10-07** — William Chen, Prem Seetharaman, Ke Chen et al. — [CrossEdit: Cross-Modal Training Enables Rich Audio-Visual Editing](http://arxiv.org/abs/2610.10264v1)
  <details><summary>📄 Abstract</summary>
  Multimedia editing requires generative models to interpret complex, compositional instructions and modify only the desired elements across modalities, a capability largely beyond existing systems. Current approaches are typically limited to simple, single-attribute edits within one modality, since diverse, high-quality editing pairs are hard to obtain, especially for cross-modal tasks where aligned audiovisual (AV) data is scarce. We present CrossEdit, a unified omni-modal editing model for imag...
  </details>

- **2026-10-07** — Dang K Le, Wenxuan Shi, Xinyu Xing — [On the Reliability of LLM-Based Vulnerability Patching Benchmarks](http://arxiv.org/abs/2610.10150v1)
  <details><summary>📄 Abstract</summary>
  Large language models (LLMs) have shown strong potential for automated vulnerability patching, but current benchmarks can substantially distort reported performance. Drawing on extensive experience developing, running, and stress-testing such frameworks, we identify under-examined pitfalls across three dimensions: (1) agent-level factors, where prompting, tool availability, and detailed instructions can raise success rates without improving developer-aligned patch quality; (2) framework-level fa...
  </details>

- **2026-10-07** — Xiangtao Kong, Shuaizheng Liu, Rongyuan Wu et al. — [HarnessIR: Harnessing Multimodal Foundation Models for Universal Real-World Image Restoration](http://arxiv.org/abs/2610.10133v1)
  <details><summary>📄 Abstract</summary>
  Real-world low-quality images suffer from complex mixed degradations, including but not limited to noise, blur, atmospheric effects, etc. Recent agentic methods usually model real-world image restoration (Real-IR) as a sequential tool calling problem over task-specific single-degradation restoration models. This paradigm, however, is fundamentally limited because complex real-world degradations cannot be cleanly undone degradation by degradation, and the tool used for task-specific models caps t...
  </details>

- **2026-10-07** — Huanan Liu, Ye Li, Kangye Ji et al. — [RealtimeWAM: How Fast Can I Run My World Action Model?](http://arxiv.org/abs/2610.10079v1)
  <details><summary>📄 Abstract</summary>
  World Action Models (WAMs) combine visual dynamics modeling with action generation, but their high inference latency limits responsive robot control. Recent efforts accelerate inference by removing explicit future-video generation at test time, as in FastWAM, an approach that requires a specially tailored architectural design. More general caching strategies exploit feature redundancy, but redundancy alone does not capture the changing computational demands of closed-loop control. To address the...
  </details>

- **2026-10-07** — Jicheng Zhou, Kahim Wong, Jialong Wang et al. — [EASE: Entropy-Adaptive Distribution Shaping for Evading AI-generated Text Detectors](http://arxiv.org/abs/2610.09976v1)
  <details><summary>📄 Abstract</summary>
  AI-generated text (AIGT) detection can be sensitive to the decoding choices of the source large language model (LLM). We observe that perturbing next-token logits or adjusting sampling temperature can reduce detection performance, providing a clear signal of detector vulnerability to decoding-time distribution changes. Building on this observation, we propose EASE (Entropy-Adaptive Distribution Shaping for Evasion), a training-free and detector-agnostic framework for evading AIGT detectors. EASE...
  </details>

- **2026-10-07** — Zhuchenyang Liu, Yao Zhang, Yu Xiao — [Inverting Multi-Vector Visual Document Indices](http://arxiv.org/abs/2610.09920v1)
  <details><summary>📄 Abstract</summary>
  Prevailing multi-vector visual document retrievers store each page as about a thousand patch vectors, often in vector databases run by a third party. Since no one can read a page from its vectors, this index is easily treated as less sensitive than the page. However, because the index keeps one vector per patch in raster order, and each vector is computed by a vision-language model pre-trained to read documents, we hypothesize that whoever runs or breaches the store can reproduce a page from its...
  </details>

- **2026-10-07** — Ruohan Li, Miaoqing Tian, Haipeng Qu et al. — [GRAML: Graph-Grounded Reasoning and Multi-Task Learning for LLM-Based Software Vulnerability Detection](http://arxiv.org/abs/2610.09605v1)
  <details><summary>📄 Abstract</summary>
  Large Language Models (LLMs) have been widely applied to software vulnerability detection. However, their performance is often limited by insufficient use of control-flow and data-flow information. In this paper, we propose GRAML, a framework that combines graph evidence, vulnerability description generation, and multi-task training. GRAML first performs static analysis on C/C++ programs to extract critical source lines and typed line relations as structural evidence. It then uses this evidence ...
  </details>

- **2026-10-07** — Xinsong Feng, Peng Du, Zhizhuo Yang et al. — [Denoising Blocks, Not Tokens: Efficient Compressed Continuous Diffusion with Branching Token Realization](http://arxiv.org/abs/2610.09311v1)
  <details><summary>📄 Abstract</summary>
  Diffusion language models (DLMs) generate text through iterative parallel refinement, offering the potential for higher throughput than autoregressive (AR) decoding. However, most DLMs still maintain one generative state per token, so every denoising step processes a state sequence as long as the output sequence, limiting the throughput gains from parallel generation. Continuous DLMs provide an additional degree of freedom: a single continuous state can represent multiple tokens, allowing diffus...
  </details>

- **2026-10-07** — Bhavini Jeloka, Siddhartha Ganguly, Panagiotis Tsiotras — [Beyond Nominal Equilibria: Risk-Averse Multi-Population Mean-Field Games](http://arxiv.org/abs/2610.09244v1)
  <details><summary>📄 Abstract</summary>
  Recent advances in mean-field games and its multi-population variants enable large-scale heterogeneous multi-agent systems to be modeled through representative agents and their associated mean-field distributions. However, existing approaches do not explicitly account for uncertainty in the behavior of other populations. To this end, we introduce a new paradigm: risk-averse multi-population mean-field games, where each population optimizes a worst-case expected reward over dynamically feasible a...
  </details>

- **2026-10-06** — Habibur Rahaman, Swastik Bhattacharya, Sanjay Das et al. — [BARE-AI: Bit-Flip Attack Resilience in AI Hardware through Built-in Performance Monitors](http://arxiv.org/abs/2610.08739v2)
  <details><summary>📄 Abstract</summary>
  Deep Neural Networks (DNNs) are integral to many safety critical systems, yet they remain highly vulnerable to bit-flip attacks (BFAs), where a few memory level perturbations can drastically degrade accuracy. Existing defenses incur significant hardware overhead, depend on retraining, or fail against targeted flips. We propose BARE-AI, a runtime framework that detects, localizes, and mitigates BFAs during inference. BARE-AI introduces AI Performance Counters (APCs), lightweight hardware monitors...
  </details>


### 📂 defense
*防御与防护方法 / Defense & Protection Methods* — 65 papers

- **2026-10-08** — Shihab Ahmed, Md Sajidul Islam Sajid, Teryl Taylor et al. — [ORCAGen: Orchestrating Context-Aware Malware Deception with RAG-Guided Generative AI](http://arxiv.org/abs/2610.12415v1)
  <details><summary>📄 Abstract</summary>
  Malware defenses often remove or isolate suspicious programs as quickly as possible. While effective for containment, this approach can also waste an opportunity to observe attacker behavior and deploy targeted countermeasures. ORCAGen takes a different approach: it uses GenAI to build malware-specific deception playbooks offline, validates them before deployment, and enforces only the verified logic at runtime. ORCAGen combines Retrieval-Augmented Generation (RAG) with structured prompt enginee...
  </details>

- **2026-10-08** — Ines Ortega-Fernandez, Mateusz Kowalczyk, Keri Warr — [Anytime-valid detection of LLM weight exfiltration](http://arxiv.org/abs/2610.11843v1)
  <details><summary>📄 Abstract</summary>
  A compromised LLM inference server can leak model weights by encoding payload bits in otherwise plausible token choices. A replay of the same prompt in a trusted server can expose such deviations, but benign numerical nondeterminism also causes token mismatches. Patient attackers can therefore hide within normal variation unless evidence is combined across responses. We introduce a prompt-level e-process that calibrates whole-response mismatch events on trusted benign traffic and accumulates evi...
  </details>

- **2026-10-08** — Masaaki Nakatsu, Reno Wang — [Constitutional Gating and Deterministic Recovery for Multi-Agent LLM Negotiation: Ablations Against a Stateful Adversarial Gatekeeper](http://arxiv.org/abs/2610.11542v1)
  <details><summary>📄 Abstract</summary>
  Multi-agent LLM systems negotiating with a stateful counterpart waste model calls in three ways: polite loops that never meet the counterpart's hidden acceptance condition, malformed outputs that trigger retries, and compliance deadlocks in which the counterpart demands something the agent must refuse. We study a three-part control stack - a 5-Pillar runtime constitution, a 4-tier swarm (Director, three-agent majority vote, Monitor, schema hard gate) and Cognitive Annealing (deterministic deadlo...
  </details>

- **2026-10-08** — Liaoran Xu, Weizhi Liu, Zhaoxia Yin — [MARC: Multi-Bit Watermarking for Autoregressive Audio Generation against Codec Attacks](http://arxiv.org/abs/2610.11488v1)
  <details><summary>📄 Abstract</summary>
  Generated audio is now used in a range of applications, creating a need to verify its origin after distribution and signal processing. This task is particularly challenging for autoregressive audio generation because codec processing can alter the token sequence recovered from the waveform. Such changes reduce the reliability of watermark detection and payload decoding. Existing methods construct token groups using either intrinsic token representations or substitution patterns caused by transfo...
  </details>

- **2026-10-08** — Rachel S. Y. Teo, Yutaro Yamada, Shashank Kotyan et al. — [Beyond Imitation: A Framework and Benchmark for LLM-Assisted Peer Review](http://arxiv.org/abs/2610.11087v1)
  <details><summary>📄 Abstract</summary>
  The rapid growth of scientific publishing has strained peer review, particularly in machine learning, raising concerns about declining review quality and increasing reviewer workload. Large language models (LLMs) have been proposed as automated review assistants, yet their evaluation has focused largely on imitating human-written reviews rather than supporting the core functions of peer review. Here, we introduce a verification-centric perspective on LLM-assisted peer review, emphasizing error d...
  </details>

- **2026-10-08** — Min-Young Yu, Tony Kim, Jang Won Choi — [NOMOS: Compiling Written Policies into Statically Verified Tool-Call Gates for LLM Agents](http://arxiv.org/abs/2610.11030v1)
  <details><summary>📄 Abstract</summary>
  Tool-using LLM agents violate the policies they are deployed to enforce, often silently. Prior defenses hand-write rules, query an LLM verifier per action, or compile policies through heavyweight formal machinery. Naive compilation fails: extracted rules block the tool satisfying their own precondition, or read arguments their tool lacks. NOMOS, a four-pass compiler, turns a natural-language policy into a deterministic tool-call gate; static verification with tool-schema-level checks alone (no p...
  </details>

- **2026-10-08** — Babak Barazandeh, Connor Swanson, Chinmay Kulkarni et al. — [OnTrack: Real-Time Monitoring and Intervention in LLM Agent Trajectories via Streaming Structure-Aware Optimal Transport](http://arxiv.org/abs/2610.12375v1)
  <details><summary>📄 Abstract</summary>
  Agents are deployed in applications from trip planners and stock trading to IT incident triage. In most cases, LLM agents work autonomously with minimal rule-based safeguarding, leading to cost and safety issues from irreversible actions. Recent works resolve this either by using a safeguard agent to monitor behavior or evaluating logs post-hoc. The first adds cost and latency to every step; the second delivers its verdict after the run, when tokens are burned and damage is done. To overcome thi...
  </details>

- **2026-10-08** — Saurabh Mathur, Sahil Sidheekh, Bhavan Vasu et al. — [Learning Probabilistic Logic Programs with Functional Gradient Guided Language Models](http://arxiv.org/abs/2610.12303v1)
  <details><summary>📄 Abstract</summary>
  Declarative logic programs offer a powerful and interpretable abstraction for encoding relational structure and neurosymbolic reasoning, by expressing dependencies as weighted compositional rules. However, inducing them from data remains fundamentally hard, bottlenecked by the combinatorial explosion of symbolic search spaces. LLMs have recently emerged as powerful hypothesis generators, but when used in isolation, they lack the capacity to do systematic inductive reasoning needed to reliably sy...
  </details>

- **2026-10-08** — Hyunin Lee, Jinglue Xu, Jeffrey Seely et al. — [Recursive Self-Improvement through Multi-Agent Self-Supervision](http://arxiv.org/abs/2610.12176v1)
  <details><summary>📄 Abstract</summary>
  Recursive self-improvement (RSI) of a model on non-verifiable tasks, such as open-ended research, faces a supervision bottleneck when its outputs exceed what even human experts can reliably assess, leaving the model itself (optimizee) as the best available optimizer and evaluator. However, a single model instance struggles to critique and improve its own complex reasoning under this homogeneous loop. To address this, we propose Multi-Agent Self-Supervision (MASS), an RSI method that alternates b...
  </details>

- **2026-10-08** — Lei Zhai, Zhihao Chang, Shuyuan Yang et al. — [Instruction-Conditioned Electromagnetic Spectrum Understanding via Budget-Adaptive Signal Tokenization](http://arxiv.org/abs/2610.12142v1)
  <details><summary>📄 Abstract</summary>
  Electromagnetic spectrum monitoring increasingly requires flexible analysis beyond task-specific recognition and detection. Multimodal large language models offer a unified interface, but extending vision-language models (VLMs) to raw I/Q signals requires tokenization that balances fidelity against a strict budget. For signals, dense encoding causes token costs to grow with observation length, whereas fixed-resolution compression may discard short-duration or localized signal evidence. Thus, we ...
  </details>

- **2026-10-08** — Sixu Chen, Mingrui Yang, Qiang Guan et al. — [OA-MAP: Evidence-Grounded Multi-Agent Multimodal Framework for Interpretable Knee Osteoarthritis Progression](http://arxiv.org/abs/2610.12134v1)
  <details><summary>📄 Abstract</summary>
  Knee osteoarthritis (KOA) progression prediction can support patient monitoring, requiring the integration of multimodal data and multidomain expertise. Moreover, isolated risk estimates provide limited insight underlying a prediction. To automate the progression assessment workflow and reduce manual effort while providing interpretable findings and supporting evidence, we present OA-MAP, an autonomous multi-agent framework for evidence-grounded assessment of structural and pain progression in K...
  </details>

- **2026-10-08** — Riccardo Loconte, Jonas Festor, Zane Fatjanova et al. — [A persistent accuracy ceiling in automated verbal deception detection](http://arxiv.org/abs/2610.12118v1)
  <details><summary>📄 Abstract</summary>
  Automated methods have been proposed to overcome the limitations of human verbal deception detection, but evidence remains fragmented across disciplines. We systematically reviewed 25 years of research (289 reports, 6,136 classification models) and meta-analyzed 3,653 models nested within 97 datasets. Pooled accuracy was 74.4% (95% CI: 71.2%-77.4%) with substantial heterogeneity. Accuracy was driven by methodological quality (ground truth, data source, class balance, evaluation procedure) more t...
  </details>

- **2026-10-08** — Ali Satvaty, Narjes Sharafi, Jirui Qi et al. — [Is Memorization Context-Sensitive? Prefix-Based Extraction Beyond Isolated Prefixes](http://arxiv.org/abs/2610.12085v1)
  <details><summary>📄 Abstract</summary>
  Large language models (LLMs) can expose memorized training sequences under prefix-based extraction: given a prefix from a training example, the model may assign high probability to the original continuation. In deployed systems, however, prefixes are rarely evaluated in isolation. They often appear together with instructions, retrieved documents, or other task-specific context, as in retrieval-augmented generation (RAG). This motivates examining whether contextual conditioning mitigates memoriza...
  </details>

- **2026-10-08** — Xiaomi LLM-Core Team,  :, Zongming Qiao et al. — [MiMo-V2.6: Scaling Reinforcement Learning Towards Self-Improvement](http://arxiv.org/abs/2610.11959v1)
  <details><summary>📄 Abstract</summary>
  Reinforcement learning (RL) is the central training paradigm for advancing large foundation models towards self-improvement. This report introduces the MiMo-V2.6 series, an omni-modal family that pushes the frontier of model intelligence by scaling RL compute. Prior to RL, we conduct mid-training on a broad multimodal corpus to provide ample exploration space, and build a solid infrastructure on the pretrained hybrid-SWA architecture to support subsequent scale-up. We scale RL compute along thre...
  </details>

- **2026-10-08** — Sebastian Ben Daniel — [Near-Inverse-Linear Barriers for Explicit Affine Witness Isolation](http://arxiv.org/abs/2610.11432v1)
  <details><summary>📄 Abstract</summary>
  We study randomized nonuniform polynomial-size transformations that output explicit binary affine filters for circuit inputs whose nonempty satisfying sets are affine. The filter may depend on the entire input description; no affine basis is supplied. For every fixed $δ<1$, a worst-case singleton success guarantee $Ω(n^{-δ})$, where $n$ is the witness arity, implies $NP\subseteq P/poly$. More generally, any success guarantee $ω(\log n/n)$ yields satisfiability circuits of size $(s+2)^{O(1)}2^{o(...
  </details>

- **2026-10-08** — Junchi Liao — [Writing for the Reviewer: Defensive Writing in GPT Models](http://arxiv.org/abs/2610.11355v1)
  <details><summary>📄 Abstract</summary>
  Researchers increasingly use ChatGPT to revise their papers, and recent GPT versions often narrow or even retract the authors' claims. We call such changes defensive writing when the given material does not support them, and we test two explanations: the model corrects the authors' overclaiming, or it writes for an anticipated reviewer. We ask GPT versions and models from other developers to rewrite paragraphs from papers written before ChatGPT, or to write from an evidence sheet that lists a pa...
  </details>

- **2026-10-08** — Congqi Cao, Zhenhe Liang, Hanwen Zhang et al. — [A Unified Score Matching Paradigm for Video Anomaly Detection and Anticipation](http://arxiv.org/abs/2610.11149v1)
  <details><summary>📄 Abstract</summary>
  Video anomaly detection (VAD) is a fundamental and safety-critical task in computer vision. Recent generative approaches detect anomalies from a distributional perspective, but remain limited by local anomaly modes. Meanwhile, video anomaly anticipation (VAA), as a proactive extension beyond post-hoc detection, introduces additional challenges. In particular, the contrastive inference paradigm in VAD, which relies on ground-truth frames, is not applicable to VAA, hindering its development. To ad...
  </details>

- **2026-10-08** — Qiye Lu, Jiang Ji, Liang Zhang — [Ranking Prior Alignment for Credit Risk Modeling: When Do External Priors Matter?](http://arxiv.org/abs/2610.11146v1)
  <details><summary>📄 Abstract</summary>
  Cold-start credit scoring -- deploying models with scarce labeled data, weak features, or minimal capacity -- is a recurring problem in financial machine learning. When a new lending product launches, labeled default data is scarce, feature pipelines are immature, and models must be deployed with minimal capacity to avoid overfitting. Standard defenses operate on the same limited data; what is needed is a source of external regularization grounded in domain knowledge.   We propose Ranking Prior ...
  </details>

- **2026-10-08** — Xiaolong Li, Xiaohan Xu, Jinyang Li et al. — [When Interfaces Speak: Data-Aware Generative UI Harness for Active Interaction](http://arxiv.org/abs/2610.11123v1)
  <details><summary>📄 Abstract</summary>
  Most human-agent interaction today remains text-based. Natural language can impose cognitive overload, ambiguity, information chaos, and slow input for complex tasks; ephemeral generative UIs can present structured information and guide users toward task completion. We propose GenUI-Harness, a multi-agent harness pairing a Tool Agent for information retrieval and task execution with a GUI Coder Agent that identifies ambiguities and generates front-end code for structured interfaces. Training the...
  </details>

- **2026-10-08** — Oskar J. Hollinsworth, Alex F. Spies, Tigist Diriba et al. — [Caught in the Act: Probes Effectively Detect Sabotage and Catch Unverbalized Deception](http://arxiv.org/abs/2610.12445v1)
  <details><summary>📄 Abstract</summary>
  Recent incidents have highlighted the challenge of monitoring LLM agents and the danger of models deceiving people. We show that white-box deception detection via probes can be scaled up to frontier monitoring settings by collecting the largest deception dataset to date for training probes and introducing a novel probe architecture which can aggregate information across many layers and tokens. Our probes achieve 98.8% AUC in SHADE-Arena, surpassing an Opus 5.5 text-monitoring baseline, and show ...
  </details>

- **2026-10-08** — Yuxin Chen, Senqiao Yang, Zixuan Wang et al. — [RESETTLE: Robotic Recovery through Disagreement-Triggered Retrieval and Efficient Corrective Control](http://arxiv.org/abs/2610.12185v1)
  <details><summary>📄 Abstract</summary>
  Reliable robotic manipulation requires timely intervention to correct emerging deviations and restore progress after execution errors. However, recovery methods based on repeated vision-language reasoning or iterative online optimization can incur substantial latency, delaying intervention. To address these challenges, we introduce RESETTLE(Robotic rEcovery through diSagrEement-Triggered reTrievaL and Efficient Corrective Control), a model-agnostic framework that provides computationally efficie...
  </details>

- **2026-10-08** — Xiaoshan Zhou — [FearCaut-Qwen: Affective Steering in a Vision-Language Model Shifts the Decision Criterion for Hazard Assessment](http://arxiv.org/abs/2610.11986v1)
  <details><summary>📄 Abstract</summary>
  Vision-language models (VLMs) show great potential for damage assessment after a disaster, but a recurring deficiency is that they are reluctant to declare a hazard; that is, recall is low even when overall accuracy appears adequate. This study examines that deficiency by using signal detection theory to decompose the decision behavior into perceptual capability and decision-criterion placement. We then propose a novel method for correcting the over-conservative decision policy, inspired by the ...
  </details>

- **2026-10-08** — Yuchen Miao, Zijun Wang, Chang Han et al. — [The "10th Juror": Open-Set Standpoint Screening for Bureaucratic Bias Detection](http://arxiv.org/abs/2610.11136v1)
  <details><summary>📄 Abstract</summary>
  Presupposing the boundaries of bias is itself a form of bias. We study closed-loop bias governance for Dutch government documents, where a system must detect biased language, ground decisions in legal and contextual evidence, rewrite problematic sentences when intervention is warranted, and verify that the rewrite mitigates harm without distorting meaning. Existing methods face three challenges: (i) discriminative classifiers capture surface regularities but lack normative grounding; (ii) zero-s...
  </details>

- **2026-10-08** — Yujing Liu, Yixin Liu, Yue Tan et al. — [Is Real-World Training Data Necessary for Generalist Graph Anomaly Detection?](http://arxiv.org/abs/2610.12167v1)
  <details><summary>📄 Abstract</summary>
  Generalist graph anomaly detection (GAD) aims to build a foundation model that detects anomalies on arbitrary unseen graphs without retraining or fine-tuning. Sufficient data are essential for foundation model training, yet generalist GAD still faces a data shortage, as real-world anomalous graphs are scarce and costly to collect and annotate. To fill this gap, we propose AG-FORGE, an Anomalous Graph generation Forge for automatic synthesis of anomalous graphs, exploring the feasibility of synth...
  </details>

- **2026-10-08** — Ilya Lasy, Nora Yinuo Cai, Kola Ayonrinde — [RouterInterp: Understanding Superposed Specialisation in Mixture of Experts Routing](http://arxiv.org/abs/2610.11775v1)
  <details><summary>📄 Abstract</summary>
  Sparse Mixture of Experts (MoE) models scale more efficiently than dense models by routing tokens to modular expert networks that are only active for processing a fraction of tokens. A leading hypothesis for the performance of MoE models is that each expert specialises in a single, coherent domain. However, interpretability efforts that assume this hypothesis have generally been unsuccessful. We propose and present evidence for an alternative account that we call the Superposed Specialisation Hy...
  </details>

- **2026-10-08** — Raffaele Cappelli — [Revisiting Handcrafted Minutiae Detection: A Simple and Effective Open Source Baseline for Modern Fingerprint Workflows](http://arxiv.org/abs/2610.11641v1)
  <details><summary>📄 Abstract</summary>
  Handcrafted minutiae detection algorithms remain fundamental to biometric science and forensic practice due to their full auditability, adherence to international standards, and operational independence from training datasets or GPU hardware. However, current open-source traditional baselines are severely outdated, relying almost exclusively on legacy C/C++ codebases that lack seamless integration with modern scientific software ecosystems. To bridge this gap, the present work introduces SBMEX (...
  </details>

- **2026-10-08** — Jinghan Dong, Jingrui Zhang, Haichen Zhou et al. — [Undetected Photon Spectroscopy in the Long-wave and Far Infrared](http://arxiv.org/abs/2610.11582v1)
  <details><summary>📄 Abstract</summary>
  Spectroscopy with undetected photons allows the spectral response of a sample at long wavelengths to be measured through interference of a shorter-wavelength signal field, without directly detecting the light that probes the sample. Previous demonstrations of undetected-photon spectroscopy in the molecular fingerprint region have reached approximately 10.5 microns, leaving longer wavelengths largely unexplored. Here, we extend this approach to 20 microns wavelength, demonstrating infrared undete...
  </details>

- **2026-10-08** — Shinjiro Yagyu, Takahiro Nagata, Yoshiyuki Nakajima — [Data-Driven Variable-Exponent Analysis for Photoemission Yield Spectroscopy: An Autonomous Self-Diagnosing Framework Based on Integrated Residual Metrics](http://arxiv.org/abs/2610.11331v1)
  <details><summary>📄 Abstract</summary>
  Photoemission yield spectroscopy (PYS) is widely used for evaluating the electronic states of materials. As automated materials discovery advances, unsupervised extraction of physical information from ambient-air PYS data becomes important. Conventional fixed-exponent analyses and logarithmic transformations suffer from heteroscedasticity, which destabilizes estimation in low-signal regions. To address this, we propose a data-driven analysis framework based on the 1/n-Scan method, which operates...
  </details>

- **2026-10-07** — Andrea Wynn, Harsh Satija,  Seokhyun et al. — [Reading the Room: Foundations, Design, and Challenges of Normative Competence in LLMs](http://arxiv.org/abs/2610.10906v1)
  <details><summary>📄 Abstract</summary>
  Human communities are governed by normative systems: shared standards that produce \textit{norms} dictating acceptable behavior, enforced through community sanctioning. Aligning increasingly autonomous AI systems with these norms is a central alignment challenge, complicated by the fact that norms are vast in number, change quickly, and are often arbitrary (e.g., dress or language conventions). Thus, alignment requires \textit{normative competence}: the ability to discern from interaction alone ...
  </details>

- **2026-10-07** — Ziyuan Wang, Fredrik D. Johansson — [MotherTree: Meta-learning on synthetic data improves decision tree training](http://arxiv.org/abs/2610.10832v1)
  <details><summary>📄 Abstract</summary>
  Conventional decision tree algorithms produce effective, transparent models that can be audited, communicated, and deployed independently of the training data, but require learning every new task from scratch. In contrast, tabular foundation models demonstrate that meta-learning from a synthetic prior distribution enables strong in-context prediction for previously unseen tasks, especially in small-sample regimes. However, this approach does not produce a standalone model that can be inspected i...
  </details>

- **2026-10-07** — Pranav Wagh, Yu Fang, Yue Yang et al. — [Diagnosing and Recovering from Observation-Space Shift at Long-Horizon Skill Seams](http://arxiv.org/abs/2610.10810v1)
  <details><summary>📄 Abstract</summary>
  Long-horizon robotic manipulation is often built by chaining independently trained skills. Although each skill can be reliable in isolation, performance degrades sharply when skills are chained: each downstream skill must start from the state its predecessor leaves behind rather than from its training distribution. We study this failure mode, Observation-Space Shift (OSS), and ask what causes these skill-seam failures. Using privileged simulator resets, we find that the dominant shift comes from...
  </details>

- **2026-10-07** — Tolulope Agbaje, Nam Pham, Altay Sansal et al. — [Fault-conditioned Seismic Image Generation using Denoising Diffusion Probabilistic Modeling and Neural Style Transfer](http://arxiv.org/abs/2610.10788v1)
  <details><summary>📄 Abstract</summary>
  Seismic data augmentation is critical for training robust deep learning (DL) models for fault detection and characterization, yet conventional approaches remain inadequate. Geometric transforms, e.g., flips or rotations, and noise injection fail to capture realistic seismic textures, while physics-based forward modeling is computationally expensive and often poorly aligned with the statistical characteristics of field data. We present a denoising diffusion probabilistic model (DDPM) framework th...
  </details>

- **2026-10-07** — Yongjian Tang, Linhan Li, Thomas Runkler — [Agent4RE: A Self-Refining Multi-agent Framework for End-to-End Software Requirements Engineering and Benchmarking](http://arxiv.org/abs/2610.10628v1)
  <details><summary>📄 Abstract</summary>
  Existing LLM-based approaches for software Requirements Engineering (RE) typically rely on basic prompting strategies or rudimentary agent collaboration, under-utilizing the full potential of multi-agent systems. Meanwhile, available datasets focus on isolated subtasks, such as requirements extraction, classification, and completeness detection, leaving the absence of an end-to-end RE benchmark that spans from requirements elicitation to generation. We present Agent4RE - a self-refining multi-ag...
  </details>

- **2026-10-07** — Vincenzo Guarino, Emanuele Musumeci, Vincenzo Suriani et al. — [iAm.md: Robot Skill Self-Assessment through Agentic Introspection for Unknown Open-Vocabulary Domains](http://arxiv.org/abs/2610.10962v1)
  <details><summary>📄 Abstract</summary>
  Agentic AI based on Large Language Model generalization capabilities offers a wide range of potential applications, including planning for embodied tasks. For example, embodied agents based on Foundation models can generate plausible plans in autonomous robotics scenarios. Due to limited context windows or hallucinatory phenomena in the next-token prediction formulation, behaviors may be generated without establishing whether the deployed robot and the observed environment actually support the r...
  </details>

- **2026-10-07** — Maverick Morales, Tomáš Dominik, Vermut Gao et al. — [Reasoning-Token Spikes Under Prompted Untruthful Responding in Large Language Models](http://arxiv.org/abs/2610.10405v1)
  <details><summary>📄 Abstract</summary>
  Monitoring the chain-of-thought of reasoning artificial intelligence (AI) models remains a key approach to detecting deception and other forms of misbehavior in such models. However, semantic chain-of-thought monitoring depends on reasoning traces being legible and sufficiently faithful to the underlying computations that produced the model's behavior, not to mention accessible. Moreover, there is increasing evidence that chain-of-thought outputs may soon become illegible or unfaithful, if they ...
  </details>

- **2026-10-07** — Sayan Biswas, Jade Garcia Bourrée, Anne-Marie Kermarrec et al. — [Robust Decentralized Fairness Auditing](http://arxiv.org/abs/2610.10199v1)
  <details><summary>📄 Abstract</summary>
  Emerging legislation requires large language models (LLMs) to be audited for compliance with regulatory standards, particularly fairness. Such black-box audits typically assume a single auditor with access to a large, representative set of queries. In practice, it can be difficult for an auditor to obtain such a query set, but multiple auditors can together cover the relevant demographic groups by auditing the LLM collaboratively with their individual query sets. However, relying on multiple aud...
  </details>

- **2026-10-07** — Nikolaos Kekatos, Stylianos Basagiannis, Marinelio Chintri et al. — [Formal Runtime Verification for Tool-Using LLM Agents: An Offline Same-Benchmark Study on AgentDojo and STAC](http://arxiv.org/abs/2610.09793v1)
  <details><summary>📄 Abstract</summary>
  Guardrails for tool-using LLM agents are usually application-specific rules, which makes multi-step, data-dependent safety policies hard to specify, audit and reuse. As a declarative alternative, we evaluate metric first-order temporal logic (MFOTL), replaying the recorded trajectories that AgentDojo, STAC and R-Judge already ship through the unmodified MonPoly monitor, offline and without running an agent. On these corpora, five generic obligations flag 71.8% of STAC attack chains and 70.1% of ...
  </details>

- **2026-10-07** — Honglei Guo, Hanfang Zhang, Guochuan Zhang et al. — [Hierarchical Defense in Leader-Defender-Attacker Games: Nested Equilibria and Receding-Horizon Control](http://arxiv.org/abs/2610.09428v1)
  <details><summary>📄 Abstract</summary>
  We formulate a discrete-time leader-defender-attacker game that combines hierarchical interaction within a protective group with competition against an external attacker. The leader seeks to reach a prescribed demand point while avoiding capture, whereas the defender seeks to intercept the attacker while remaining near the leader. To capture their distinct objectives and asymmetric interactions, we introduce a nested equilibrium concept combining a leader-defender Stackelberg relationship with a...
  </details>

- **2026-10-07** — Fernando Martinez, Abhishek Satyam, Tao Li et al. — [Ask the Expert: LLM-Guided Reinforcement Learning for Autonomous Cyber Defense](http://arxiv.org/abs/2610.09337v1)
  <details><summary>📄 Abstract</summary>
  Policy-based reinforcement learning (RL) approaches have produced promising results for autonomous cyber defense; however, they are sample-inefficient in settings where defenders must respond under delayed, partial observations with actions from large action spaces. While large language models (LLMs) may reason semantically about security state space, high latency and trust assumptions prevent attractive in-line deployment models. We introduce Ask the Expert, a training-time guidance framework w...
  </details>

- **2026-10-07** — Fanqing Meng, Lingxiao Du, Haocheng Lu et al. — [RSIGym: A Flexible Environment for Recursive Self-Improvement](http://arxiv.org/abs/2610.10310v1)
  <details><summary>📄 Abstract</summary>
  Recursive self-improvement requires carrying accepted changes into later improvement cycles, while studying agent-proposed changes also requires substantial research infrastructure. Existing settings often leave agents to rebuild routine infrastructure or restrict exploration to individual components. We introduce RSIGym, an agent-native research environment based on Everything as a Service (EaaS). RSIGym exposes training, inference, rollout, evaluation, and sandbox execution through reusable se...
  </details>

- **2026-10-07** — Arnold Brosch, Abdelrahman Eldesokey, Michael Felsberg et al. — [A Probabilistic Perspective on Wasserstein-Based Evidential Uncertainty for Out-of-Distribution Segmentation](http://arxiv.org/abs/2610.10116v1)
  <details><summary>📄 Abstract</summary>
  Semantic segmentation networks operate on a fixed set of classes and therefore fail when out-of-distribution (OOD) objects appear during deployment, a critical limitation for safety-critical applications such as autonomous driving. Reliably identifying OOD objects requires well-calibrated epistemic uncertainty, yet common softmax-based confidence scores remain overconfident, while Bayesian alternatives such as Monte Carlo dropout or deep ensembles require costly repeated forward passes. Evidenti...
  </details>

- **2026-10-07** — Zijian Chen, Zhengyu Chen, Bohan Liang et al. — [From Pixel to Coding: Evaluating the Figure Reproduction Capabilities of MLLMs](http://arxiv.org/abs/2610.10066v1)
  <details><summary>📄 Abstract</summary>
  Multimodal Large Language Models (MLLMs) have demonstrated impressive capabilities in both visual understanding and code generation. However, existing benchmarks typically evaluate these two modalities in isolation, lacking a dedicated assessment of their unification, i.e., how a model can perceive complex visual structures and synthesize them into precise, executable code. Moreover, current visual code generation benchmarks often rely on simplified layouts within single programming environments...
  </details>

- **2026-10-07** — Malte Hansen, Karim Issa, Wilhelm Hasselbring — [A Chat Assistant for Software Exploration in a 3D Software Visualization](http://arxiv.org/abs/2610.09901v1)
  <details><summary>📄 Abstract</summary>
  We present a chat assistant for interactive software exploration, embedded in the 3D software visualization tool ExplorViz. The assistant builds upon current Large Language Models (LLMs) and enables users to ask questions about the currently visualized software system and trigger actions that change the visualization through natural language. We integrate the chat assistant in our ExplorViz frontend using the CopilotKit libraries such that probabilistic LLMs are combined with deterministic and t...
  </details>

- **2026-10-07** — Jonghyun Han, Younghoon Song, Jongyoul Park — [A Deafening Silence: Catastrophic Forgetting Lives in the Output Embeddings of Tokens the Data Never Speaks](http://arxiv.org/abs/2610.09835v1)
  <details><summary>📄 Abstract</summary>
  Continual pre-training and fine-tuning in Large Language Models (LLMs) inevitably induce catastrophic forgetting, typically mitigated by replay using often-inaccessible original data. In this data-free regime, we analyze where forgetting occurs and why. Systematic parameter freezing across five settings up to 1.4B reveals that forgetting concentrates selectively in the output embeddings of tokens rarely seen in the new corpus, whereas the same sqrt(v-hat) band of the body is inert and new learni...
  </details>

- **2026-10-07** — Arnold Olympio, Juan Manuel Servera Bondroit, Wael Abdelmalek et al. — [Reproducible LLM Inference Benchmarking: A Sequential Isolation Protocol for Regression Testing](http://arxiv.org/abs/2610.09778v1)
  <details><summary>📄 Abstract</summary>
  Reproducible benchmarking of Large Language Model (LLM) inference is challenging because repeated measurements can vary with execution and system state. We present the Sequential Isolation Methodology, a controlled benchmarking and regression-testing protocol designed to reduce between-run measurement variance while deliberately varying workload concurrency. We evaluate three representative open-source LLMs on an NVIDIA A100 80GB GPU using vLLM 0.9.1 across six context sizes and eight concurrenc...
  </details>

- **2026-10-07** — Kautuk Astu, Naina Rabha, Yogesh Simmhan — [AeroEval: Staged Program and Execution Validation for AI-Generated Drone Missions](http://arxiv.org/abs/2610.09764v1)
  <details><summary>📄 Abstract</summary>
  Large Language Models (LLMs) can generate drone programs from natural-language mission descriptions, but syntactically valid programs may still violate user intent, environmental constraints, and mission-level behavior. This problem is pronounced in cyber-physical applications, where correctness depends on the interaction among generated code, mobile sensing, environmental geometry, event-driven analytics, and physical execution. Existing drone code-generation systems primarily use prompt guardr...
  </details>

- **2026-10-07** — Samuel Margolis, Paul Schmiedmayer, Alan Huang et al. — [DrugTargetWorld: A Synthetic Biobank for Training and Benchmarking AI Scientists](http://arxiv.org/abs/2610.09558v1)
  <details><summary>📄 Abstract</summary>
  Drug target discovery requires distinguishing molecules that causally drive disease from those that are merely associated with it. Training and evaluating AI agents to perform this workflow end-to-end is difficult because real world biobanks lack known causal ground truth and participant-level data is access controlled. We introduce DrugTargetWorld, a framework that procedurally generates simulated biobanks, or "worlds," with known but concealed causal structure. Each world contains genotypes, p...
  </details>

- **2026-10-07** — Yupeng Zhang, Ziyi Zhao, Juntao Cheng et al. — [RT-DETR-World: Transferring Rich LLM Semantics to Real-Time Open-Vocabulary Detection](http://arxiv.org/abs/2610.09502v1)
  <details><summary>📄 Abstract</summary>
  Open-vocabulary detection (OVD) recognizes categories unseen during training through textual category queries, yet achieving strong generalization with real-time efficiency remains challenging. Beyond vocabulary scaling, zero-shot generalization may benefit from reusable visual--semantic cues learned from seen data, including attributes, actions, states, and contextual relations. Existing real-time OVD methods primarily emphasize vocabulary coverage and efficient region/query--text matching; und...
  </details>

- **2026-10-07** — Oliver Bimber, Rakesh John Amala Arokia Nathan, Mohamed Youssef et al. — [trACT: temporal revelation Airborne Camera Trap](http://arxiv.org/abs/2610.09417v1)
  <details><summary>📄 Abstract</summary>
  Effective remote monitoring and surveillance using drones are frequently impeded by severe environmental and thermal clutter, dynamic vegetation, target camouflage, and system latency. Drawing inspiration from the hunting strategies of birds of prey that hover and stabilize their vision to isolate subtle ground motion, we introduce trACT (temporal revelation Airborne Camera Trap), a lightweight, real-time aerial robotics framework designed for autonomous consumer drones. The system integrates Te...
  </details>

- **2026-10-07** — Raghu Arghal, Saswati Sarkar, Shirin Saeedi Bidokhti — [The Confidence Game: Strategic Miscalibration in Human-AI Delegation](http://arxiv.org/abs/2610.09371v1)
  <details><summary>📄 Abstract</summary>
  Calibrated uncertainty quantification is essential to ensuring AI agents are trustworthy and reliable. However, when agents seek to maximize user engagement or revenue, confidence reports may be strategically distorted, detracting from their informativeness. We formalize this problem in the Confidence Game: a repeated signaling game with imperfect monitoring in which an agent of unknown honesty and ability reports its confidence, and a user decides whether to delegate the task or complete it her...
  </details>

- **2026-10-07** — Yash Dave, Sang T. Truong, Serena Wang et al. — [The AI Evaluation Ecosystem](http://arxiv.org/abs/2610.09296v1)
  <details><summary>📄 Abstract</summary>
  AI evaluation shapes the decisions of model providers, users, funders, and regulators. We argue that designing valid benchmarks requires contextualizing design choices in the dynamics of this ecosystem of actors. We develop a simulation architecture that combines rule-based market dynamics with LLM-driven strategic actors, building on advances in Generative Agent-Based Modeling (GABM). We model benchmarks, consumer needs, and provider capabilities as vectors over a six-dimensional capability spa...
  </details>

- **2026-10-07** — Kefan Liu, Fengning Ou, Yelin Luo et al. — [We Query, Therefore We Compute: On Oracle Computation beyond the Machine, with an Application to Agents](http://arxiv.org/abs/2610.09243v1)
  <details><summary>📄 Abstract</summary>
  Agentic systems use large language models (LLMs) to carry out concrete tasks. Prior work often borrows abstractions such as scheduling, caching or isolation piecemeal from operating systems, so the mechanisms it builds share little common ground, and the shared view of the two forms of agentic system, Workflows and Agents, is limited. We construct an abstract machine that provides both.   We treat the LLM as an Oracle and extend a two-stack pushdown automaton with one instruction, which hands th...
  </details>

- **2026-10-07** — Zhaohui Geoffrey Wang — [When Rank Rises as LLMs Degrade](http://arxiv.org/abs/2610.09647v1)
  <details><summary>📄 Abstract</summary>
  Post-training adapts language models in non-stationary environments. Practitioners monitor representation health with RankMe and related spectral statistics, often assuming that rank falls when representations degrade. We show that this assumption is unsafe for LLM post-training. In a controlled study of Qwen3-0.6B with four degradation modes and three seeds, data duplication worsens held-out loss by 75% relative to healthy while increasing both original and centred RankMe; the latter changes by...
  </details>

- **2026-10-07** — Neil K. R. Sehgal, Manuel Tonneau, Dunigan Folk et al. — [AI-Assisted Submissions in Online Research Are Rare and Highly Concentrated but Routinely Approved](http://arxiv.org/abs/2610.09279v1)
  <details><summary>📄 Abstract</summary>
  Online research platforms underpin much of what science claims about people, on the assumption that a human produced each response. Generative AI threatens that assumption by letting participants delegate responses to a chatbot, yet how often they do so remains unclear because prior estimates rely on self-report or automated detection rather than direct observation. We surveyed 2,500 workers on a high quality online research platform and directly observed AI assistance by linking donated ChatGPT...
  </details>

- **2026-10-07** — Benoît Roussel, Damien Bouet, Liming Chen et al. — [MOTIP2: Spatial Priors for End-to-End Multi-Object Tracking](http://arxiv.org/abs/2610.10391v1)
  <details><summary>📄 Abstract</summary>
  End-to-end multi-object trackers have narrowed the gap with classical tracking-by-detection on association-difficult benchmarks. Yet they still make spatially implausible errors no classical tracker would, such as assigning one identity to objects on opposite sides of the frame. A model could learn to avoid them, but tracking annotations are scarce, so we encode spatial priors explicitly instead, while keeping inference fully end-to-end with no post-hoc association.   We propose three spatial pr...
  </details>

- **2026-10-07** — Jiapan Wang, Daan Hulskemper, Mathilde Letard et al. — [DeepTopoClustering: Unsupervised Derivation of Surface Process Taxonomy from 4D Point Clouds for Topographic Monitoring](http://arxiv.org/abs/2610.09860v1)
  <details><summary>📄 Abstract</summary>
  4D point clouds acquired by permanent laser scanning (PLS) enable accurate high-frequency monitoring of surface change in dynamic topographic environments. However, existing methods remain limited in organizing detected surface activities into meaningful process types. We propose DeepTopoClustering (DTC), an unsupervised framework for deriving a hierarchical process taxonomy from object-based surface activities, so-called 4D objects-by-change (4D-OBCs). We transform each 4D-OBC into a GeoMorphog...
  </details>

- **2026-10-07** — Matthieu Meignin, Cécile Mallet, Nicolas Viltard — [Generative and deterministic deep learning models comparison for fine-scale precipitation retrievals from infrared brightness temperature](http://arxiv.org/abs/2610.09859v1)
  <details><summary>📄 Abstract</summary>
  Accurate precipitation estimation at fine spatial scales is critical for hydrology, agriculture, and climate studies. Infrared brightness temperatures from geostationary satellites offer excellent temporal coverage over continental-scale domains. However, because these measurements primarily characterize cloud-top properties rather than precipitation processes near the surface, their correlation with rainfall intensity remains limited, making quantitative precipitation estimation challenging. In...
  </details>

- **2026-10-07** — Justus Flerlage, Thorsten Wittkopp, Alexander Acker et al. — [Adaptive Code Generation for Controlling Robots](http://arxiv.org/abs/2610.09588v1)
  <details><summary>📄 Abstract</summary>
  Deploying robots as Complex Adaptive Systems (CAS) in unknown and dynamic environments necessitates a transition from rigid command libraries toward intention-based autonomy, as natural language represents the only medium capable of articulating complex goals beyond the capacity of finite instruction sets. While Large Language Models (LLMs) offer a path toward natural language goal description, their integration introduces significant challenges: the formalization gap between imprecise intention...
  </details>

- **2026-10-07** — Toluwani Aremu, Samuele Poppi, Nils Lukas — [Constitution-Guided Watermarking](http://arxiv.org/abs/2610.09552v1)
  <details><summary>📄 Abstract</summary>
  Watermarking enables language model providers to identify text generated by their models. However, its desired properties can conflict (\ie~stronger watermark signals can degrade text quality), while designs that resist editing may also facilitate forgery. Providers address these trade-offs by choosing configurations that balance competing objectives or prioritize particular properties. Either approach imposes a shared operating point on requests with different requirements, potentially sacrific...
  </details>

- **2026-10-07** — Qiuqi Wang, Ruodu Wang, Zhenyuan Zhang — [Sequential resetting procedures and false discovery rate](http://arxiv.org/abs/2610.09339v1)
  <details><summary>📄 Abstract</summary>
  Data arrive sequentially, each associated with a null hypothesis. We develop testing procedures to locate intervals in which some null hypotheses fail with false discovery rate (FDR) control. The new procedures are called sequential resetting procedures, and they are based on e-values and test supermartingales. We also develop a refined version of the procedures by dropping less informative data points before the block minimum of the test supermartingale in each rejection block. These procedures...
  </details>

- **2026-10-07** — Mayank Sengupta, Nirmit Desai, Eric Song et al. — [LeCuration: A Tiny World Model as a Data Curation Multi-Tool](http://arxiv.org/abs/2610.09285v1)
  <details><summary>📄 Abstract</summary>
  Many applications of physical AI run within finite or closed physical worlds with a limited set of physical laws governing object behavior. Examples include robots working in a warehouse and agents moving around in a video game. In order to better organize, filter, and curate data for physical AI applications, we propose a new approach centered on the unique settings and physical laws of individual datasets. We train LeCuration, a small world model intended to serve as a data curation tool for a...
  </details>

- **2026-10-06** — Param Biyani, Krishnamurthy Dvijotham — [SpecGuard: Proving a Task Is Broken Before the Agent Cheats](http://arxiv.org/abs/2610.09159v1)
  <details><summary>📄 Abstract</summary>
  As autonomous coding agents get increasingly deployed, the risk that accidental or adversarially injected misspecifications in tasks lead to dangerous agent behavior is critical to address. Prior work has shown that agents given such tasks rarely flag the conflict and instead cheat, editing tests or hard-coding expected outputs, and the actions taken to cheat can cause real damage, such as deleting a security defense to make a corrupted test pass. It remains unclear whether such conflicts can be...
  </details>

- **2026-10-06** — Vahid Tavakkoli, Kabeh Mohsenzadegan, Kyandoghere Kyamakya — [SwarmReconGuard: Black-Box Detection of Distributed Collective Reconnaissance by Individually Benign-Looking Agent Populations](http://arxiv.org/abs/2610.09138v1)
  <details><summary>📄 Abstract</summary>
  Autonomous and agentic clients can distribute reconnaissance across many identities so that each request remains valid, low-rate, and benign-looking while the population collectively acquires broad system knowledge. We formalize this threat as Distributed Collective Reconnaissance (DCR) and present SwarmReconGuard, a reproducible black-box benchmark in which the defender observes only service-boundary telemetry. The Docker-isolated study evaluates 11 benign and attack behaviors across 10-10,000 ...
  </details>

- **2026-10-06** — Mohamed Kamel, Sahar Selim, Walaa Medhat et al. — [BeatFlow-ECG: Rectified Flow for ECG Reconstruction from Indirect Wearable Signals](http://arxiv.org/abs/2610.09052v1)
  <details><summary>📄 Abstract</summary>
  Continuous cardiac monitoring outside clinical settings requires signals that are both informative and practical to collect during daily life. Electrocardiography (ECG) provides rich information about cardiac rhythm and waveform morphology, while wearable photoplethysmography (PPG) is easier to acquire continuously but is only an indirect cardiovascular measurement and is highly sensitive to motion. We present BeatFlow-ECG, a conditional rectified-flow model for reconstructing single-channel ECG...
  </details>

- **2026-10-06** — Nikolaos Kekatos, Dimitrios Nikou, Anastasios Temperekidis et al. — [Multi-Aspect Runtime Verification for Simulation-Based V&V of LLM-Enabled Autonomous Agents](http://arxiv.org/abs/2610.08928v1)
  <details><summary>📄 Abstract</summary>
  LLM-based agents are entering decision-support roles in defence staff work, where the obligations they must respect are already written down and binding, and where retraining is not available as a control because models arrive as procured components. What can be placed under engineering control is the interface between the agent and the systems it acts on. Those obligations are at once spatial, temporal and text-semantic, and a violation typically lives in the composition of a multi-step interac...
  </details>


### 📂 alignment
*对齐与安全约束 / Alignment & Safety Constraints* — 63 papers

- **2026-10-08** — Mengping Dong, Jinbao Li, Fei Li — [DiscoVL: Unveiling Disentangled C ross-Modal Representation Learning via Orthogonal Adversarial Regularization for V ision-Language Models](http://arxiv.org/abs/2610.11113v1)
  <details><summary>📄 Abstract</summary>
  Pre-trained vision-language models excel across varied perception tasks, but adapting them to novel downstream settings without sacrificing generalization remains non-trivial. Existing parameter-efficient prompt learning method often yields inconsistent representations and fails to account for semantic distribution shifts. In this work, we present DiscoVL, a disentangled cross-modal representation learning framework that couples orthogonal adversarial regularization with structured cross-modal a...
  </details>

- **2026-10-08** — Jiayu Wang, Yue Yu, Bin Zhu et al. — [SpatialHarness: Test-Time Spatial Scaffolding for Fine Robotic Manipulation](http://arxiv.org/abs/2610.12457v1)
  <details><summary>📄 Abstract</summary>
  Frontier multimodal foundation models (e.g., GPT-6 Astra) have recently shown strong potential for direct robotic control, yet their performance on fine manipulation remains limited. We argue that an important source of failure is not necessarily insufficient policy capability, but insufficient spatial observability, where task-critical spatial relationships may be poorly revealed by the existing physical camera setup. We introduce SpatialHarness, a test-time embodied harness that provides test-...
  </details>

- **2026-10-08** — Peter Kulits, Yiqing Xu, R. Kenny Jones et al. — [BrickBench: Evaluating Agentic Brick Design](http://arxiv.org/abs/2610.12452v1)
  <details><summary>📄 Abstract</summary>
  We propose BrickBench, a benchmark for agentic text-conditioned LEGO-set design. Given a prompt, an agent is tasked with producing an assembly that not only satisfies semantic and design criteria, but that can also be physically built. To do so, it must select parts from a discrete library and reason jointly about local and global constraints. We score validity, alignment, and design across three settings that vary in scale and part availability. We provide BrickAgent, an environment for coding ...
  </details>

- **2026-10-08** — Suhwan Cho, Yonwoo Choi, Soongjin Kim et al. — [LEGO: A Lifting-Free Approach for Exocentric-to-Egocentric Video Generation](http://arxiv.org/abs/2610.12442v1)
  <details><summary>📄 Abstract</summary>
  Generating an egocentric video from a single exocentric recording is a challenging case of novel view synthesis, as the two cameras share little overlap and much of the target view is unobserved. Current state-of-the-art methods reconstruct the scene explicitly by estimating depth, lifting the video into a point cloud, and re-rendering it from the egocentric camera to condition a video diffusion model. This deterministic mapping assigns each pixel to a single reprojected location, which preserve...
  </details>

- **2026-10-08** — Andy Liu, Mehar Bhatia, Karolina Stanczak et al. — [Predicting Alignment Generalization with Value Representations](http://arxiv.org/abs/2610.12410v1)
  <details><summary>📄 Abstract</summary>
  LLM developers post-train their models to exhibit prosocial values and behavioral traits, which are enumerated in an alignment target. However, while recent post-training developments have yielded models that score highly on alignment evaluations, training models on sets of narrow behaviors still influences their behavior across unseen contexts and environments in unexpected ways. In this paper, we establish the task of alignment generalization prediction, i.e., predicting how fine-tuning a mode...
  </details>

- **2026-10-08** — Guowen Li, Yang Liu, Yujie Wang et al. — [Learning Kilometer-Scale Weather Prediction with Global-Regional Alignment](http://arxiv.org/abs/2610.12401v1)
  <details><summary>📄 Abstract</summary>
  Kilometer-scale regional weather forecasting is essential for local weather warnings and weather-sensitive decisions. Existing data-driven approaches often rely on numerical forecasts for large-scale guidance or require additional training of global forecasting components. Pretrained global weather models offer an efficient source of large-scale forecasts, motivating their reuse to guide high-resolution regional prediction. However, this coupling requires aligning global and regional representat...
  </details>

- **2026-10-08** — Stefano Esposito, Naama Pearl, Polina Karpikova et al. — [GenIA: Generative Reconstruction with Test-Time Input Alignment](http://arxiv.org/abs/2610.12388v1)
  <details><summary>📄 Abstract</summary>
  Reconstructing complete 3D object assets from monocular or sparse multi-view observations remains challenging. Generative 3D foundation models can complete object geometry beyond the observed views, but their predictions may not faithfully reproduce the observed geometry, appearance, or pose. We introduce GenIA, a framework for test-time input-aligned generation that grounds SAM3D's generative prior in geometric and photometric observations without retraining the foundation model. We improve obj...
  </details>

- **2026-10-08** — Jing He, Kaixin Ding, Xingye Tian et al. — [WorldAlign: Decoupled 4D Reward for World-Consistent Video Generation](http://arxiv.org/abs/2610.12382v1)
  <details><summary>📄 Abstract</summary>
  Faithful visual world simulation requires generated videos to maintain 4D world consistency, encompassing both static and dynamic consistency. Static consistency requires coherent 3D structure in static environments across viewpoints, while dynamic consistency requires plausible subject motion and consistent appearance over time. Geometry-aware post-training offers a promising way to improve world consistency. However, existing methods often rely on a static-scene assumption. Even those that acc...
  </details>

- **2026-10-08** — Daniel Domínguez Figaredo, Rafael Fernández De la Cruz — [The learner who does not learn: when optimizing a pedagogical metric degrades LLM tutoring](http://arxiv.org/abs/2610.12125v1)
  <details><summary>📄 Abstract</summary>
  It is assumed that a natural way to improve the pedagogical quality of large language model tutors is to define a metric of instructional performance and fine-tune the model against it. To test this strategy, we designed a metric of pedagogical adaptivity that scores each instructional decision in a learning sequence against the conditions of the learning situation, which is the standard used for automated pedagogical scoring. We audited a frontier tutor across 2,000 learner scenarios, corrected...
  </details>

- **2026-10-08** — Fazeng Li, Gan Sun, Hao Cheng et al. — [Tell Robot What Not to Do: A Negation Understanding Perspective](http://arxiv.org/abs/2610.11952v1)
  <details><summary>📄 Abstract</summary>
  Instruction following enables robots to perform diverse tasks specified in natural language, making it a fundamental capability for human-robot interaction. Beyond communicating desired outcomes, users also need to specify constraints on what not to do. We investigate how to enable vision-language-action models (VLAs) to follow negated instructions, where robots must accomplish task goals while respecting explicit exclusions. To this end, we propose NegaAlign, a parameter-efficient, plug-and-pla...
  </details>

- **2026-10-08** — Bo Chen, Huanzhang Hu, Junyang Ma et al. — [TACROSS: An Efficient and Low-Cost Scalable Human Touch System Across Heterogeneous Tactile Sensors for Dexterous Robot Learning](http://arxiv.org/abs/2610.11945v1)
  <details><summary>📄 Abstract</summary>
  Collecting tactile demonstrations on robots is costly and slow, motivating the use of lower-cost human tactile gloves for scalable data collection. However, human capacitive/piezoresistive gloves and robotic tactile sensors differ fundamentally in transduction principle, sensor layout, spatial resolution, and dynamic response, making alignment of raw sensor channels ill-posed. To address this problem, we present TACROSS, a scalable system for learning from human touch and transferring it to robo...
  </details>

- **2026-10-08** — Jierui Lei, Wenjian Zhang, Qingyi Yang et al. — [Revisiting Identity and Spectra Dispersion in Media-Bridged Time Series Forecasting: Linking Multivariate Signals and Narrative Flows](http://arxiv.org/abs/2610.11924v1)
  <details><summary>📄 Abstract</summary>
  Media-bridged time series forecasting is expanding to encompass traditional "multivariate" and emerging "multimodal" (e.g., through textual assistance). Existing Time Series Forecasting (TSF) models still rely on paradigm-specific relation, fusion, and temporal modules, hindering a common forecasting backbone across numerical and pre-aligned narrative-flow settings. To explore this, we propose the Multimedia Identity-Aware Prism Network (MIDAPN), a unified spatiotemporal forecasting backbone bas...
  </details>

- **2026-10-08** — Jia Li, Yichao He, Yangchen Yu et al. — [From Surface to Depth: Towards Cognitive Appraisal Reasoning in Multimodal Emotion Understanding](http://arxiv.org/abs/2610.11918v1)
  <details><summary>📄 Abstract</summary>
  Recent multimodal large language models (MLLMs) increasingly incorporate explainable reasoning for emotion understanding. However, reasoning based mainly on observable affective cues can reduce emotion understanding to superficial cue-label associations, giving rise to the Clever Hans effect. Such shortcuts become unreliable when affective cues are implicit, conflicting across modalities, linguistically misleading, or obscured by redundant details. In contrast, human emotions are shaped by how i...
  </details>

- **2026-10-08** — Yunji Wang, Junjie Yao, Linyu Liu et al. — [Probability-Signature Dynamics: Unpacking Modular Addition Learning Within Two-Layer Networks](http://arxiv.org/abs/2610.11833v1)
  <details><summary>📄 Abstract</summary>
  Neural networks trained on modular addition tasks often develop Fourier-structured representations that support exact generalization. While prior work has identified these Fourier circuits, the mechanism by which gradient-based training selects them from the data distribution remains unclear. We address this question using probability signatures, which express leading gradient interactions through conditional statistics of the training distribution. For modular addition, these signatures are cyc...
  </details>

- **2026-10-08** — Chen Zhao, Xingping Dong, Jiachun Shi et al. — [From Suppression to Repair: Mitigating Object Hallucination in Large Vision-Language Models via Localized Distribution Alignment](http://arxiv.org/abs/2610.11826v1)
  <details><summary>📄 Abstract</summary>
  Object hallucination remains a major obstacle for large vision-language models (LVLMs) to generate reliable content. An intuitive mitigation strategy is to suppress hallucination-related components in hidden representations. However, these components may also contain useful information, and suppressing them can weaken the model's multimodal capabilities. In this paper, we propose ResOT, a training-free method that repairs representations at inference time through localized distribution alignment...
  </details>

- **2026-10-08** — Qixiang Chen, Cheng Zhang, Fucai Ke et al. — [Seek-and-View Reasoning for Multi-View Spatial Understanding](http://arxiv.org/abs/2610.11810v1)
  <details><summary>📄 Abstract</summary>
  Existing approaches to multi-view spatial reasoning operate largely on sparse input views. Vision-language models (VLMs) are thus restricted to understand a scene and infer spatial relations within these fixed views, leading to fragile cross-view alignment and geometry-to-language bottleneck. To address these issues, we formulate a novel Seek-and-View reasoning approach to find implicit cross-view spatial evidence by locating a question-relevant view to support the spatial reasoning. To realize ...
  </details>

- **2026-10-08** — Frederikke Isa Marin, Panagiotis Antoniadis, Dionysia Danai Brilli et al. — [RAGenome: Scaling Retrieval-Based Genomic Language Models to Long Contexts](http://arxiv.org/abs/2610.11761v1)
  <details><summary>📄 Abstract</summary>
  The genome holds the blueprint that governs the biological properties of the cell. Consequently, advancing our knowledge of genomic function is crucial both for a broader understanding of biology and for continued biomedical advances. The success of large language models on natural language and protein sequences has motivated similar efforts on genomic data. However, standard genomic language models (gLMs) often require extremely large computational resources and still fall behind traditional me...
  </details>

- **2026-10-08** — Eitan Waks, Ben Glocker — [What Output-Only Review Cannot Verify: Study Contracts for Research Agents](http://arxiv.org/abs/2610.11754v1)
  <details><summary>📄 Abstract</summary>
  Some defects in an AI-generated study can be identified from its artifacts; others require knowledge of what was approved before execution. We propose study contracts that bind declared experimental choices, run obligations and claim scope to recorded execution evidence, and distinguish this contract-relative verification from scientific truth. A diagnostic using eight self-authored clean/mutated pairs illustrates the information boundary. A deterministic checker applying a registered, fault-spe...
  </details>

- **2026-10-08** — Nick Milkin, Lanmiao Liu, Esam Ghaleb et al. — [Perceptually Grounded and Semantics-Aware Evaluation for Holistic Co-Speech Gesture Generation](http://arxiv.org/abs/2610.11669v1)
  <details><summary>📄 Abstract</summary>
  Holistic and semantics-aware co-speech gesture generation has advanced rapidly, yet evaluation remains behind: objective metrics do not consistently reflect human perception, and semantic appropriateness remains difficult to quantify. We present a perceptually grounded and semantics-aware benchmark that combines standardized model comparison, human-centered metric validation, and fine-grained semantic evaluation. We first curate a list of 13 objective metrics covering different aspects, includin...
  </details>

- **2026-10-08** — Yuchen Yang, Xin Wang, Lufan Wang et al. — [Beyond Report Imitation: Clinically Aware Multi-Image Ultrasound Report Generation from Visible Evidence](http://arxiv.org/abs/2610.11610v1)
  <details><summary>📄 Abstract</summary>
  Generating ultrasound reports from multiple images requires aggregating clinical evidence across views, yet archived key frames capture only part of the dynamic examination. Raw-report imitation is therefore misaligned with visual supervision: content that is clinically valid for the full examination may be unverifiable from the images available to a model. This gap creates a clinical behavior alignment problem. A model must preserve visible findings, avoid diagnostic reversals and unsupported c...
  </details>

- **2026-10-08** — Umaira Izhar, Gunjan Arora, Pushpendra Singh — [Measuring Cultural Alignment Beyond the Average: A Framework for Evaluating Maternal-Health LLM Interactions in Indian Contexts](http://arxiv.org/abs/2610.11586v1)
  <details><summary>📄 Abstract</summary>
  Existing evaluation methods for healthcare LLMs primarily assess factual correctness,safety, and fluency, while providing limited insight into whether generated interactions reflect culturally situated healthcare reasoning. This limitation is particularly important in maternal health, where care decisions are shaped by social and relational norms. We introduce MH-INDIC, a culturally grounded evaluation framework for maternal-health interactions in urban and semi-urban North Indian contexts that ...
  </details>

- **2026-10-08** — Jeonghyo Song, YoungJoon Yoo — [SAGE: Sink-Aware Guided Emphasis for Visual Grounding in Vision-Language Decoders](http://arxiv.org/abs/2610.11469v1)
  <details><summary>📄 Abstract</summary>
  Recent large vision-language models (VLMs) pair a visual encoder with a large language model (LLM) and perform well on diverse image-text tasks, yet their reliability is often limited by decoder attention pathologies that suppress visual evidence and exacerbate hallucinations. In this paper, we revisit visual attention sinks and uncover a structured, layer-dependent behavior: across prompts, early and late decoder layers exhibit prompt-invariant attention collapse onto the same few image regions...
  </details>

- **2026-10-08** — Shiao Zhu, Lianbo Liu, Sizhen Lyu et al. — [Beyond Speech Captions: Speech-Rewarded Style Planning for Conversational Text-to-Speech](http://arxiv.org/abs/2610.11461v1)
  <details><summary>📄 Abstract</summary>
  Natural-language style descriptions provide an interpretable interface between large language models (LLMs) and controllable text-to-speech (TTS). However, using descriptions as pseudo-labels compresses target acoustics into text, and descriptive fidelity need not imply effective control of a particular synthesizer. We empirically show that speech-text alignment only weakly predicts downstream acoustic similarity among candidate instructions for the same utterance. We therefore propose Speech-Re...
  </details>

- **2026-10-08** — Jorge García-Carrasco, Sergio García-Carrasco, Alejandro Maté et al. — [Closed-loop evaluation of LLM agents for embedded software development](http://arxiv.org/abs/2610.11447v1)
  <details><summary>📄 Abstract</summary>
  Large language models (LLMs) are increasingly deployed as coding agents that edit files, run builds and tests, inspect execution results, and repair software iteratively. Embedded firmware is a demanding target because correctness depends on closed-loop behavior under sensing, timing, and safety constraints, not only on static source quality. Yet embedded-agent evaluation remains limited and often emphasizes one-shot synthesis or offline correctness.   We present a benchmark for closed-loop eval...
  </details>

- **2026-10-08** — Fanqi Cheng, Kuo Gong, Shangke Liu et al. — [PathLang: A Language-Centered Benchmark for Vision-Language Models in Computational Pathology](http://arxiv.org/abs/2610.11329v1)
  <details><summary>📄 Abstract</summary>
  Pathology vision-language models (VLMs) have shown strong visual perception ability, but their robustness in the language domain remains poorly characterized. Existing pathology VLM benchmarks largely rely on canonical closed-set prompts or perturb only generic templates, treating language as a fixed evaluation component rather than a variable axis of model behavior. In clinical practice, however, diagnostic language varies across reports, institutions, and candidate diagnoses. We introduce Path...
  </details>

- **2026-10-08** — Jianpeng Cheng, Guangyu Sun, Aashu Singh et al. — [MetaEncoder: Exploring the Limit of Bi-Encoders for Multimodal System One Decision Making with Natural Language Interface](http://arxiv.org/abs/2610.11316v1)
  <details><summary>📄 Abstract</summary>
  System One models output constrained decisions and probability distributions rather than free-form text generation. While prevailing paradigms rely on structured schema objects to encode state, intent, and candidate choices, we revisit a fully natural language-based System One interface. In this framework, both the user request and each candidate option are expressed in natural language, supported by multimodal (image and video) auxiliary inputs. We introduce MetaEncoder, which fine-tunes a pre-...
  </details>

- **2026-10-08** — Jihwan Kim, Dogyoon Song, Chulhee Yun — [From Geometry to Generalization: Why Row Normalization Can Beat Adam and Muon](http://arxiv.org/abs/2610.11309v1)
  <details><summary>📄 Abstract</summary>
  Different optimizers can fit the same training data while selecting classifiers with substantially different geometries, but whether this difference provably affects population performance remains unclear. We show that row-wise normalization can achieve strictly higher population accuracy than full-batch Adam, a proxy for random-reshuffling Adam, and exact-SVD Muon in high-dimensional multiclass classification. Under an isotropic Gaussian-cloud data model, this advantage arises because row norma...
  </details>

- **2026-10-08** — Runquan Gui, Hanzhu Chen, Zehao Wang et al. — [VAMR: Multi-Question Agentic Reasoning for Efficient Long-Form Video Understanding](http://arxiv.org/abs/2610.11171v1)
  <details><summary>📄 Abstract</summary>
  Long-form video understanding often involves multiple questions about different aspects of the same recording. Yet existing video agents typically process each question through an isolated tool-use trajectory. This repeatedly restarts video exploration and memory construction, missing opportunities to acquire evidence jointly and progressively build a shared understanding that supports the complete question set. We introduce \textbf{VAMR} (\textbf{V}ideo \textbf{A}gent for \textbf{M}ulti-Questio...
  </details>

- **2026-10-08** — Xinnian Zhao, Chia-Hua Wu, Pu Wang et al. — [Local Prototype Reconstruction for Text-Compatible Speech-to-LLM Bridge Pretraining](http://arxiv.org/abs/2610.11159v1)
  <details><summary>📄 Abstract</summary>
  Speech-to-LLM systems often connect a frozen speech encoder to a frozen large language model (LLM) through a small trainable bridge. The bridge is usually treated as plumbing, but it in fact defines the geometry of the speech-to-LLM interface, and the pretraining objective decides whether that interface provides a reusable initialization for downstream tasks. We study a transferable bridge through two complementary properties: global alignment with the text side, and local lexical manifold compa...
  </details>

- **2026-10-08** — Jiarui Zeng, Kun Shi, Chiman Vong et al. — [SatFix: Absolute Visual Localization of UAVs in Satellite Maps from a Single Oblique Image](http://arxiv.org/abs/2610.11049v1)
  <details><summary>📄 Abstract</summary>
  We study absolute metric UAV localization within a provided geo-referenced satellite region, recovering continuous map position and viewing heading from a single oblique image or a short multi-view clip. Existing cross-view geo-localization methods retrieve the most similar satellite tile from a gallery and report Recall@K, but retrieval depends on gallery sampling, provides no heading estimate, and returns a tile index rather than a continuous coordinate. We propose SatFix, a feed-forward UAV--...
  </details>

- **2026-10-08** — Xing Zhang, Guanghui Wang, Yanwei Cui et al. — [Who Verifies the Verifier? Co-Evolving Inspectable Graders with Self-Improving Agents](http://arxiv.org/abs/2610.11464v1)
  <details><summary>📄 Abstract</summary>
  We changed the agent: did it actually get better? Every self-improving agent loop answers this hundreds of times, and every answer comes from a verifier. On open-ended tasks none exists, so the loop is handed a hand-written rubric or a bare LLM judge grading output from a model like itself, inviting reward hacking and shared blind spots. We make the verifier the evolving object: an inspectable expression over small, mostly deterministic drawback detectors, synthesized from clustered failures, ga...
  </details>

- **2026-10-08** — Sanjit Dandapanthula, Shuvom Sadhuka, Samir Khan et al. — [How to post-train on a surrogate: Envelope sampling mitigates reward hacking](http://arxiv.org/abs/2610.11281v1)
  <details><summary>📄 Abstract</summary>
  Large language models (LLMs) are commonly post-trained against LLM judges and other cheap surrogates because the true reward, such as human preference, is too expensive to query at scale. This practice often leads to reward hacking, where reinforcement learning against a miscalibrated surrogate leads to undesirable side effects. In this work, we study a setting in which a small number $n$ of model outputs are annotated with ground-truth labels (e.g., from expert review) and used to recalibrate t...
  </details>

- **2026-10-07** — Ian de Holanda Cavalcanti Bezerra, Vivek Trivedy, Lucas Pascotti Valem et al. — [Region-Aware CLS Token Augmentation for Fine-Grained Image Retrieval](http://arxiv.org/abs/2610.10991v1)
  <details><summary>📄 Abstract</summary>
  Image retrieval methods often rely on a single global semantic descriptor extracted from an image, e.g., the [CLS] token in vision transformers. However, trying to squeeze all the semantic information of an image into a single descriptor can hurt downstream retrieval performance, especially for fine-grained retrieval tasks. In this work, we augment the semantic tokens in the newer visual transformers, the global [CLS] token and the four register tokens, with a carefully selected collection of sp...
  </details>

- **2026-10-07** — Hong Huang, Yuqiu Liu, Chenyu You et al. — [Fluid-Gen-Zero: Grounding Pretrained Video Generators in Physics without Training](http://arxiv.org/abs/2610.10984v1)
  <details><summary>📄 Abstract</summary>
  We present Fluid-Gen-Zero, a training-free framework for physics-aware fluid-object interaction video generation that decouples physical reasoning from appearance synthesis. Our key insight is to delegate motion dynamics to a physics simulator while preserving the appearance modeling capacity of pretrained video generators. We bridge these two domains through a two-level agentic workflow: generation-time planning, where a vision-language model (VLM) agent interprets intent and the simulation rol...
  </details>

- **2026-10-07** — Vishrut Goyal, Rohan Ramkumar — [Spectrally Targeted Muon](http://arxiv.org/abs/2610.10965v1)
  <details><summary>📄 Abstract</summary>
  The Muon optimizer orthogonalizes each update matrix, setting all of its singular values to one, and has proven highly effective for training large language models. It remains unclear, however, whether this success comes from amplifying small singular directions that gradient descent neglects or from suppressing large, degenerate directions that disrupt training. We introduce Spectrally Targeted Muon, which orthogonalizes only the singular values above or below a threshold $τ$, so that varying $...
  </details>

- **2026-10-07** — Xilin Jiang, Shun Zhang, Tejas Jayashankar et al. — [Conversational Voice Aesthetic Model with Reinforcement Learning from Human Listeners](http://arxiv.org/abs/2610.10868v1)
  <details><summary>📄 Abstract</summary>
  We introduce Conversational Voice Aesthetic Model, a speech large language model for describing the voice aesthetics of real or synthetic speech responses in natural conversational contexts. Given a context and a response speech, CVAM describes salient moments that characterize the voice and predicts nine categorical attributes spanning gender, pitch, pacing, emotion, and delivery. The key challenge lies in perceptual fields such as emotion and delivery, which are inherently subjective and lack ...
  </details>

- **2026-10-07** — Zihan Su, Junhao Zhuang, Yaowei Li et al. — [SGF+: Decoupling Gradient Flows for Autoregressive Video Generation](http://arxiv.org/abs/2610.10429v2)
  <details><summary>📄 Abstract</summary>
  Autoregressive video generation requires denoising the current frames while writing their key-value representations as context for future predictions. However, these two roles typically share parameters, and we find that their gradients exhibit distinct patterns and systematic negative alignment, hindering the joint optimization of visual quality and temporal consistency. We introduce Self Gradient Forcing Plus (SGF+), which assigns separate parameters to context writing and denoising while pres...
  </details>

- **2026-10-07** — Kaisong Zhang, Haotian Fang, Junmeng Zhou et al. — [Coverage-Aware Reasoning with Medical Tokens for Diagnosis Prediction](http://arxiv.org/abs/2610.10641v1)
  <details><summary>📄 Abstract</summary>
  Large language models (LLMs) offer promising potential for next-visit diagnosis prediction, owing to their ability to integrate longitudinal clinical evidence and reason over it in natural language. However, reinforcement learning for LLM reasoning commonly rewards each trajectory according to the correctness of its final answer. In next-visit diagnosis prediction, multiple diagnoses can be simultaneously valid, but independently rewarding one diagnosis per trajectory does not distinguish repeat...
  </details>

- **2026-10-07** — Zhewei Chen, Hao Zhu, Jiaojiao Jiang et al. — [Distilling Graph Geometry: Knowledge Gap from GNNs to MLPs](http://arxiv.org/abs/2610.10520v1)
  <details><summary>📄 Abstract</summary>
  GNN-to-MLP distillation aims to retain the predictive accuracy of a message-passing teacher while deploying a graph-free MLP at inference. Existing methods mainly transfer node-wise predictions or use confidence-based reweighting, but they do not specify where the student should preserve the teacher's graph-induced geometry. We show that this omission leads to two spectral failure modes in the student's representation space. On sparse graphs, the student suffers from spectral underfit, missing h...
  </details>

- **2026-10-07** — Zihan Su, Junhao Zhuang, Yaowei Li et al. — [SGF+: Decoupling Gradient Flows for Autoregressive Video Generation](http://arxiv.org/abs/2610.10429v1)
  <details><summary>📄 Abstract</summary>
  Autoregressive video generation requires denoising the current frames while writing their key-value representations as context for future predictions. However, these two roles typically share parameters, and we find that their gradients exhibit distinct patterns and systematic negative alignment, hindering the joint optimization of visual quality and temporal consistency. We introduce Self Gradient Forcing Plus (SGF+), which assigns separate parameters to context writing and denoising while pres...
  </details>

- **2026-10-07** — Chengwei Shi, Yunnong Chen, Tingting Zhou et al. — [TaoD2C-Bench: Benchmarking MLLMs for Industrial UI Code Generation Beyond Visual Fidelity](http://arxiv.org/abs/2610.10374v1)
  <details><summary>📄 Abstract</summary>
  A key challenge for multimodal large language models (MLLMs) is moving beyond visual recognition to constraint-aware cross-modal reasoning. This involves combining visual cues with information from other modalities to understand elements' relationships under domain-specific rules. This challenge is acutely evident in industrial design-to-code (D2C), which converts user interface (UI) designs into code and requires MLLMs to connect design images with disorganized layer metadata, infer component a...
  </details>

- **2026-10-07** — Koffka Khan — [ORDERS: An Empirical Study of Norm-Rank Aggregation for Personalized Federated Learning](http://arxiv.org/abs/2610.10361v1)
  <details><summary>📄 Abstract</summary>
  Personalized federated learning combines shared representations with client-specific predictors, but the contribution of a server weighting rule can be obscured by local training and evaluation choices. We study ORDERS, a configuration that combines a shared backbone, a private residual adapter and classifier, geometric weights assigned by descending update norm, feature alignment, and private-parameter perturbations. The server computes a weighted sum of updates obtained from the same broadcast...
  </details>

- **2026-10-07** — Zekai Liu, Zhilin Wang, Xuzheng He et al. — [MIRA: A Musical Intent Refinement Agent for Aligning Text-to-Music Generation with User Intent](http://arxiv.org/abs/2610.10355v1)
  <details><summary>📄 Abstract</summary>
  Text-to-music systems produce increasingly convincing audio, yet evaluation reveals little about whether the result matches user intent. A global text-audio relevance score can overlook the implicit intent in underspecified prompts and mask failures in specific requirements, such as instrumentation, structure, rhythm, or mood progression. To bridge this gap, we formulate text-to-music intent alignment as satisfying a per-request rubric of independently verifiable items covering both a request's ...
  </details>

- **2026-10-07** — Himarsha R. Jayanetti, Sivakanesan Dhanushkanda, Shuai Hao et al. — [Nobody Truly Agrees on Sentiment: Humans, Bespoke Tools, and LLMs Struggle with Social Media Texts](http://arxiv.org/abs/2610.10318v1)
  <details><summary>📄 Abstract</summary>
  Social media is a rich source of real-time public sentiment, but widely used sentiment analysis tools are often applied without understanding their limitations. In this study, we evaluate the inter-rater reliability of three bespoke sentiment analysis tools (TextBlob, VADER, and Twitter-roBERTa-base) and three large language models (LLMs: Qwen3-32B, GPT-OSS-120B, Llama-4-Maverick-17B) against six human raters across 100 tweets. We measured agreement using two statistical measures: Cohen's kappa ...
  </details>

- **2026-10-07** — Hao Wang, Qiwei Zeng, Jinghao Lin et al. — [$Δ$Representation: Geometry Supervised Representation Learning of Phenotypes via Counterfactual Reasoning for Medical VLMs](http://arxiv.org/abs/2610.10286v1)
  <details><summary>📄 Abstract</summary>
  Medical vision-language models (VLMs) have shown increasing potential for radiological image interpretation. Medical VLMs encode radiological images into visual representations that capture both anatomical and phenotypic information for diagnosis. Existing approaches improve pathological phenotype representations through semantic-guided representation alignment. However, pathological phenotypes arise as lesion-specific visual changes superimposed on underlying normal anatomy. Such semantic align...
  </details>

- **2026-10-07** — Leo Zeitler, Jack Richings, Victoria Nockles — [AI Safety Considerations for Agents With Limited Time to Act](http://arxiv.org/abs/2610.10285v1)
  <details><summary>📄 Abstract</summary>
  In the wake of the increasingly public discussion about AI alignment, recent work has tried to propose specific AI architectures that behave safely. However, the proposed arguments that seemingly demonstrate proved alignment mostly neglect the environment the agent needs to act in. We discuss theoretical bounds for agent-agnostic safety guarantees in environments that can only be partially observed and within which an action is required within limited time. We introduce two realistic scenarios, ...
  </details>

- **2026-10-07** — Hao Wang, Qiwei Zeng, Shuchang Ye et al. — [Geometry-Supervised Visual Representation Learning for Multi-Phenotype Lesion Interpretation in Medical VLMs](http://arxiv.org/abs/2610.10238v1)
  <details><summary>📄 Abstract</summary>
  Medical vision-language models (VLMs) have shown increasing potential for clinical image interpretation. However, these models still struggle to interpret multi-phenotype lesions whose diagnosis requires the joint assessment of multiple pathological phenotypes. Existing vision-language alignment methods produce visual representations that fail to preserve anatomical hierarchies and relationships among phenotypic subclasses. This stems from their reliance on semantic supervision, which lacks geom...
  </details>

- **2026-10-07** — Yifei Lu, Cheng Liu, Dianzhi Yu et al. — [UniSkill: Learning Actor-Aligned Skill Proposals for an Evolving Policy](http://arxiv.org/abs/2610.10164v1)
  <details><summary>📄 Abstract</summary>
  Large language model agents can improve across tasks by retaining reusable skills distilled from prior interactions. Recent work jointly optimizes task execution and skill extraction, enabling the policy and skillbank to co-evolve. However, as the actor continues learning, rewarding skill proposals through their reuse in subsequent training steps may conflate skill benefits with actor improvement, while directly testing each proposed skill requires costly additional actor rollouts. In this paper...
  </details>

- **2026-10-07** — Haoru Li, Jinmei Liu, Zhiyong Wang et al. — [Many Ways to Succeed: Diversity-Driven RL Fine-Tuning for VLA Generalization](http://arxiv.org/abs/2610.09943v1)
  <details><summary>📄 Abstract</summary>
  Reinforcement learning (RL) fine-tuning improves vision-language-action (VLA) policies through closed-loop experience, yet generalization beyond the fine-tuning distribution remains limited. Our analysis reveals a selective reshaping of exploration: RL contracts behavior globally, yet diversifies successful trajectories, elicits success with fewer rollouts, and covers more of the latent task-valid solution space than supervised fine-tuning. Broader successful-mode coverage may provide alternativ...
  </details>

- **2026-10-07** — Alexandra Coroiu, Andrea Vogt, Viktor Werbilo et al. — [A Scoping Review and Experimental Study on Reinforcement Learning from Human Feedback for Human-Robot Collaboration](http://arxiv.org/abs/2610.09891v1)
  <details><summary>📄 Abstract</summary>
  Human-Robot Collaboration (HRC) can facilitate mass customisation in Industry 4.0, with Reinforcement Learning from Human Feedback (RLHF) representing a promising approach for developing safe AI-based robots. Practical challenges remain regarding safety during AI development, human feedback quality, and bidirectional human-robot adaptation. We conducted a scoping review of RLHF in HRC systems, mapping methods that address these challenges. Following PRISMA guidelines, we screened 199 records and...
  </details>

- **2026-10-07** — Arshia Hemmat, Amirhossein Vahidi, Amitis Shidani et al. — [ORCA: Hunting Compositional Failures in Text-to-Image Diffusion](http://arxiv.org/abs/2610.09841v1)
  <details><summary>📄 Abstract</summary>
  Text-to-image diffusion models fail predictably on compositional prompts: attributes bind to the wrong objects, spatial relations invert, and multi-object scenes lose count. Recent architectures already augment CLIP with a T5 encoder precisely because CLIP's contrastive embedding loses compositional structure, yet these failures persist. We argue the binding problem is therefore not one of missing information but of misaligned information: a text encoder preserves compositional structure, but in...
  </details>

- **2026-10-07** — Huayi Lai, Jicheng Yang, Min Yi et al. — [MIRROR: From Imitation to Internalization in LLM Personalization](http://arxiv.org/abs/2610.09795v1)
  <details><summary>📄 Abstract</summary>
  The demand for personalized LLMs is shifting from style imitation toward content quality. We investigate whether self-distillation can bridge this gap in existing fine-tuning paradigm. To address this limitation, we introduce MIRROR(Meta- personalization by Internalizing Reference-Revealed On-policy Reflections), a novel self-distillation framework that shifts LLM personalization from imitation toward preference internalization. First, we replace reference-token imitation with reference-revealed...
  </details>

- **2026-10-07** — Yucheng Gong, Rui Zhou, Binbin Zeng et al. — [A Strength-Monotonic Law for Domain Alignment in Frozen-Embedding Bioacoustic Classification](http://arxiv.org/abs/2610.09737v1)
  <details><summary>📄 Abstract</summary>
  When does distribution alignment help a frozen foundation-model embedding generalize across acoustic domains? For cross-domain mosquito-species classification we report a strength-monotonic law: the stronger an encoder is on the target task, the more its unseen-domain generalization relies on a distribution-alignment (MMD) term, and the more it is harmed by domain-rebalanced sampling. Across four encoder families and a within-encoder HuBERT layer sweep (n=8), the rebalancing leg orders exactly w...
  </details>

- **2026-10-07** — Masatoshi Tateno, Takehiko Ohkawa, Yueh-Hua Wu et al. — [YUBI-STAG: Contact and Semantic-Rich Alignment for VLAs via Automated Video-Language Grounding](http://arxiv.org/abs/2610.09718v1)
  <details><summary>📄 Abstract</summary>
  Vision-Language-Action (VLA) models acquire broad manipulation capabilities via large-scale pretraining, yet eliciting them through language requires fine-grained alignment between instructions and physical interactions. Existing robot demonstrations typically provide only coarse task descriptions, omitting how actions are executed, including which gripper acts, which object is contacted, and how it is grasped and moved. We introduce YUBI-STAG, a framework for Spatio-Temporal Annotation and Grou...
  </details>

- **2026-10-07** — Zihao Zhang, Haochen Tian, Tianyu Li et al. — [Do Better Visual Representations Always Lead to Better End-to-End Autonomous Driving?](http://arxiv.org/abs/2610.09695v1)
  <details><summary>📄 Abstract</summary>
  Visual foundation models (VFMs) are increasingly integrated into end-to-end autonomous driving for their powerful representations, yet it remains unclear when these representations improve driving performance. To investigate this question, we introduce ViRA, a planner-agnostic visual representation alignment framework that keeps the planner architecture and inference cost unchanged. Our study reveals three findings: (1) VFM-guided visual representations consistently improve driving performance a...
  </details>

- **2026-10-07** — Igor Slinko, Yaroslav Golubev, Sergey Titov — [Coding-Agent Benchmarks Should Match Their Users' Task Flows](http://arxiv.org/abs/2610.09633v1)
  <details><summary>📄 Abstract</summary>
  The evaluation of coding agents generally strives to be as realistic as possible. In our study, we collect 4,782 agent sessions of real software engineers in JetBrains IDEs, which we call Production Sessions. Since our subject is interactive agents, we study the sessions with at least three user messages (33% of the sample). These long sessions differ from issue-derived benchmark tasks in two ways: (i) user requests span a far wider mix of task types - questions about the project's code, plannin...
  </details>

- **2026-10-07** — Vaibhava Lakshmi Ravideshik, Mayank Kejriwal — [Reliability of LLM Judges for Evaluating Entity Alignment](http://arxiv.org/abs/2610.09554v1)
  <details><summary>📄 Abstract</summary>
  Entity Alignment (EA) identifies equivalent entities across knowledge graphs and is critical for knowledge base integration and ontology merging. Evaluating EA systems at scale requires expensive expert annotation, making systematic assessment across diverse domains practically infeasible. LLM-as-judge evaluation offers a potentially scalable alternative, yet its reliability for structured prediction tasks like EA remains unstudied. We present the first systematic benchmarking study across three...
  </details>

- **2026-10-07** — Hanqiu Li Cai, Chema Garabito — [Iris-3B: Going Beyond the Latent with Pixel-Space Diffusion Training, Conversion and Fine-Tuning](http://arxiv.org/abs/2610.09450v1)
  <details><summary>📄 Abstract</summary>
  Pixel-space diffusion models avoid the lossy VAE of latent models, which suggests an advantage on downstream tasks where fine-grained detail matters. We test this claim along both routes to a pixel-space backbone. We pretrain Iris-3B, a 3B-parameter pixel-space text-to-image transformer, from scratch through a $256\to512\to1024$ curriculum, after first ablating the prediction target and representation alignment at $256^2$ to decide what to scale. We also convert a pretrained latent model, FLUX.2...
  </details>

- **2026-10-07** — Jiachen Zhao, Zhengxuan Wu, David Bau et al. — [The Persona Hierarchy Model: Understanding Contextual Generalization in Fine-Tuning LLMs](http://arxiv.org/abs/2610.09384v1)
  <details><summary>📄 Abstract</summary>
  Language models are routinely fine-tuned under a fixed context, such as a generic system prompt, persona or domain-specific instruction, yet the learned behavior sometimes stays confined to that context and sometimes broadly generalizes to unseen contexts. We propose the Persona Hierarchy Model to explain this: a shared default persona influences behavior across contexts. Under this model, fine-tuning that modifies the shared persona promotes broader transfer, whereas changes to local personas r...
  </details>

- **2026-10-07** — Jie Ren, Hao Kang, Kai Guo et al. — [ScribbleEdit: A Benchmark for Scribble-Only Image Editing](http://arxiv.org/abs/2610.09382v1)
  <details><summary>📄 Abstract</summary>
  Scribble-based interaction provides a lightweight and intuitive way for users to specify image editing intents in interactive editing tools. However, current image editing models based on VLMs or LLMs struggle to understand and execute edits based solely on scribble inputs. To systematically study this problem, we construct a new benchmark, ScribbleEdit, that evaluates the ability of image editing models to perform image editing conditioned on scribbles. This task requires both a deep understand...
  </details>

- **2026-10-07** — Moein Khajehnejad, Michelangelo Tronti, Forough Habibollahi et al. — [Many Brains, One Geometry: A Shared Visual-Semantic Space for Cross-Dataset fMRI Decoding](http://arxiv.org/abs/2610.09352v1)
  <details><summary>📄 Abstract</summary>
  Visual decoding from fMRI is typically siloed by participant and experiment, obscuring whether heterogeneous neural measurements can be organized within a common computational geometry. Here we introduce BRAID-fMRI (Brain Representation Alignment across Individuals and Datasets), a shared CLIP-supervised decoding framework. BRAID-fMRI uses a single ROI-wise Transformer with optional participant conditioning across eight visual-fMRI datasets comprising 93 dataset-specific participant entries, 430...
  </details>

- **2026-10-07** — Dung Truong, Kuntal Kokate, Arnaud Delorme — [Scaling subjects in cross-modal alignment: video decoding with EEG foundation model](http://arxiv.org/abs/2610.09287v1)
  <details><summary>📄 Abstract</summary>
  Naturalistic visual decoding from EEG has long been constrained by cohort size: existing scaling literature caps out at a few dozen subjects, leading prior work to conclude that scaling subject cohorts yields minimal performance gains. Training a cross-modal EEG--video contrastive encoder on a cohort larger by more than an order of magnitude, we find the axis is productive but has an onset. Below $S\approx50$ --- the entirety of the range prior work occupies --- no model improves meaningfully ov...
  </details>

- **2026-10-06** — Saba Sturua, Han Xiao — [What Transfers from a VLM Teacher? Comparing Supervision Signals for Visual Document Retrieval](http://arxiv.org/abs/2610.09177v1)
  <details><summary>📄 Abstract</summary>
  Visual document retrievers are trained contrastively: each query is matched to one page labelled relevant - the positive - and pushed away from negatives, pages presumed irrelevant. Recent methods distil a vision-language model (VLM) teacher into the retriever by enriching that positive, transferring the teacher's attention over it or a description of it. We ask whether the teacher is better spent on the other side, judging the candidates the retriever mines as negatives, which the label says no...
  </details>


### 📂 robustness
*鲁棒性与可靠性 / Robustness & Reliability* — 57 papers

- **2026-10-08** — Vineet Kumar, Darshita Rathore, Anindya Moitra — [All Verdicts are Not Equal: Rethinking LLM Judge Reliability](http://arxiv.org/abs/2610.12083v1)
  <details><summary>📄 Abstract</summary>
  LLM-as-a-Judge is the standard paradigm for NLP evaluation, yet its systemic reliability remains poorly understood despite being widely treated as a deterministic ground truth. We present a comprehensive reliability audit, stresstesting six frontier models across four benchmarks, five prompt formats, two presentation orders, three sampling temperatures, and ten repetitions per condition. Our empirical analysis reveals severe vulnerabilities: verdicts change across identical replications at tempe...
  </details>

- **2026-10-08** — Qitong Wang, Xinwei Niu, Mingluo Su et al. — [SparseDecoding: Decoding-Aware Pruning for Accurate and Efficient LLM Inference](http://arxiv.org/abs/2610.12327v1)
  <details><summary>📄 Abstract</summary>
  The memory-bound nature of the decoding stage of large language model (LLM) inference incurs significant latency. Layer-wise training-free network pruning approaches guided by the Hessian have been a prominent solution to this problem, as pruning reduces the number of nonzero parameters read from memory during decoding. Nevertheless, typical methods in this line compute the Hessian using pre-collected natural sequences, whereas the model is fed self-generated tokens during decoding, creating a d...
  </details>

- **2026-10-08** — Haolin Yang, Jipeng Zhang, Jian Xie et al. — [HarnessSQL: Harness-Native Training for SQL Agents in Realistic Database Environments](http://arxiv.org/abs/2610.12274v1)
  <details><summary>📄 Abstract</summary>
  Text-to-SQL models are commonly trained to map questions directly to static queries, whereas real-world database agents operate through stateful, multi-turn interaction with live databases -- inspecting schemas, executing probe queries, diagnosing errors, and revising hypotheses. This creates a critical train-deploy mismatch, as the execution harness that mediates this interaction is introduced only at inference time. To bridge this gap, we propose HarnessSQL, a harness-native post-training fram...
  </details>

- **2026-10-08** — Jorge García-Carrasco, Javier Sanchis, Alejandro Reina-Reina et al. — [Evaluating Local Language Model Agents for Reproducible Data Engineering: An Empirical Software Engineering Study of Mobility Workflows](http://arxiv.org/abs/2610.11482v1)
  <details><summary>📄 Abstract</summary>
  Context: Large language model (LLM) agents are increasingly used as software and data-engineering assistants, yet evidence about locally deployable open-weight agents remains limited. Existing evaluations often emphasize textual responses or isolated code generation rather than the validity of complete engineering artifacts.   Objectives: We evaluate whether local LLM agents can produce correct and reproducible data-engineering artifacts, quantify the effect of a closed-loop workspace condition,...
  </details>

- **2026-10-08** — Jusuk Lee, Sungha Kim, Yeonsoo Park et al. — [Dex-One2Many: Learning Dexterous Manipulation from a Single Human Demonstration](http://arxiv.org/abs/2610.12470v1)
  <details><summary>📄 Abstract</summary>
  While learning dexterous manipulation from a single human video offers a promising alternative to costly robot demonstrations, many recent methods predominantly imitate demonstrated motions. Such strict motion matching often limits generalization to initial object poses, goal poses, and grasps not shown in the video. Alternatively, discovering a policy via reinforcement learning (RL) allows for broad generalization, but without prior guidance, it struggles with high-dimensional exploration in co...
  </details>

- **2026-10-08** — Zekai Deng, Kangyi Chen, Ye Shi et al. — [From Solo to Ensemble: A Hierarchical Framework for Composable Multi-Agent Human-Object Interaction](http://arxiv.org/abs/2610.11722v1)
  <details><summary>📄 Abstract</summary>
  Physics-based human-object interaction has achieved robust single-agent manipulation skills, yet extending them to multi-agent cooperative tasks remains challenging. Existing approaches typically adapt interaction policies through task-specific fine-tuning, which entangles low-level contact-rich execution with high-level coordination and limits reuse across object geometries, interaction types, and team sizes. We propose a hierarchical framework that converts a single-agent HOI policy into a reu...
  </details>

- **2026-10-08** — Junmyeong Lee, Dongmin Shin, Min-Gyu Park et al. — [WARP-VLA: Wrist-Camera Adaptation for View-Robust Policy Execution in Vision-Language-Action Models](http://arxiv.org/abs/2610.11508v1)
  <details><summary>📄 Abstract</summary>
  Despite recent advances in Vision-Language-Action models (VLAs) for robotic manipulation, their performance remains sensitive to changes in camera configuration. The problem becomes more evident in cross-setup deployment, as reproducing the exact camera pose used for training is nearly impossible. Unlike fixed external views, wrist views are more challenging because the camera moves with the robot, causing even small mounting variations to alter fine-grained geometric cues. To address this, we p...
  </details>

- **2026-10-08** — You-Zhe Xie, Ting-Wei Chou, Yu-Hsuan Li et al. — [OuroWorld: Bringing Any 3D World Alive as Diverse, Endlessly Looping 3D Cinemagraphs](http://arxiv.org/abs/2610.12461v1)
  <details><summary>📄 Abstract</summary>
  Recent 3D world models generate photorealistic, explorable scenes that remain frozen in time. OuroWorld is a mask-free framework that turns any static 3D Gaussian Splatting scene into a 3D cinemagraph: a dynamic scene with vivid, diverse motion looping seamlessly from any viewpoint. A vision-language model infers plausible dynamics and guides a video model to synthesize a reference video, which we lift and complete into multi-view videos. To learn from this imperfect supervision, we propose Inco...
  </details>

- **2026-10-08** — Hanan Gani, Lulu Shao, Manmohan Chandraker — [Mental-Models for Multi-Agent Systems](http://arxiv.org/abs/2610.12453v1)
  <details><summary>📄 Abstract</summary>
  Large foundation models have accelerated progress toward general-purpose agents that interact with humans and other agents through language and multimodal signals. However, robust multi-agent decision-making requires reasoning about what other agents know, intend, and are likely to do under partial observability. Current agentic systems often operate through prompt design, memory, or end-to-end behavioral shaping, but typically do not learn an explicit partner-state representation that can be re...
  </details>

- **2026-10-08** — Zheyu Fan, Yue Zhang, Mingkai Deng et al. — [WOVEN: Weaving Visual World Modeling into Multimodal LLMs](http://arxiv.org/abs/2610.12417v1)
  <details><summary>📄 Abstract</summary>
  Multimodal large language models (MLLMs) struggle with spatial, embodied, physical, and temporal reasoning. We hypothesize that these failures reflect a shared deficit in visual transition reasoning, and test whether this capability can serve as a shared training primitive, one that different models can learn from different supervision sources and reuse across different tasks, with a systematic training recipe. Existing benchmarks document these deficits separately but do not support controlled ...
  </details>

- **2026-10-08** — Kairui Hu, Siyuan Hu, Fangzhou Hong et al. — [Embodied Turing Machines: Stateful Code for Robot Recursive Self-Improvement](http://arxiv.org/abs/2610.12369v1)
  <details><summary>📄 Abstract</summary>
  Most robot policies keep a model in the control loop: a VLA maps observations to actions, and an Agent Harness, such as Agent-as-Policy or Harness VLA queries a VLM for decision making at run time. We propose a different view: the embodied world is an Embodied Turing Machine, whose tape is the robot and environment state and rules are the policy. If this state can be represented accurately, the decision making can be written entirely in code. We therefore propose Code-Only-as-Policy (COAP): code...
  </details>

- **2026-10-08** — Yue Wu, Haoyu Wan, Yuan Tian et al. — [Specialized machine learning force fields for materials dynamics](http://arxiv.org/abs/2610.12151v1)
  <details><summary>📄 Abstract</summary>
  Machine learning interatomic potentials (MLIPs) are transforming atomistic simulations by accessing unprecedented length and time scales. While pretrained equivariant graph neural networks achieve robust zero-shot performance for near-equilibrium properties across broad chemical spaces, their translation to complex materials dynamics remains fundamentally challenged by out-of-distribution reactive states, representation biases, and computational scaling limits. In this Review, we examine how phy...
  </details>

- **2026-10-08** — Liping Fu — ["Hot-Blooded" vs "Cold-Blooded": Simulating the Behavioral Phenotypes of Childhood Aggression via Generative Agents](http://arxiv.org/abs/2610.11951v1)
  <details><summary>📄 Abstract</summary>
  This study examines the construct validity of LLM-based generative agents in simulating reactive, proactive, and co-occurring aggression in children. Four distinct agents were instantiated using a theory-driven parameterization grounded in the social information processing model. A total of 1,920 simulation runs were conducted across eight social scenarios, employing a hybrid blind-coding pipeline to extract 32 quantitative behavioral indicators. Results demonstrate robust discriminant validity ...
  </details>

- **2026-10-08** — Xin-Ze Song, Xiao-Li Huang, Shu-Min Wu — [Sharing of Gaussian tripartite steering in de-Sitter space](http://arxiv.org/abs/2610.11874v1)
  <details><summary>📄 Abstract</summary>
  We investigate the redistribution and directional properties of Gaussian tripartite quantum steering in de-Sitter space within the continuous-variable framework. By expressing the Bunch-Davies vacuum in terms of the open-chart modes through a Bogoliubov transformation, we derive the covariance matrix of the resulting multipartite Gaussian state and analyze both one-to-two and two-to-one steering configurations. We find that de-Sitter curvature generally suppresses the steering initially shared a...
  </details>

- **2026-10-08** — Haoran Zhang, Haixuan Liu, Xingjian Su et al. — [Timer-M1: A Multivariate Time Series Foundation Model via Learning Primitives](http://arxiv.org/abs/2610.11734v1)
  <details><summary>📄 Abstract</summary>
  We introduce Timer-M1, a pretrained multivariate time series foundation model that learns with primitives for zero-shot forecasting. Across domains, time series share elementary temporal and relational patterns, termed primitives, yet differ in how these primitives manifest and evolve across different contexts. Despite progress in zero-shot and task-general forecasting, existing foundation models may still struggle to generalize to complex real-world scenarios. To this end, we develop a primitiv...
  </details>

- **2026-10-08** — David J. Jin — [Singular Equilibrium and Selection of Narratives](http://arxiv.org/abs/2610.11615v1)
  <details><summary>📄 Abstract</summary>
  An agent learns from data that many parameters of her model explain equally well. Berk's theorem states that her belief concentrates on the parameters that best fit the data, but does not select between them. We show that, with a continuum of parameters, the posterior concentrates on the best-fitting parameters with the smallest local learning coefficient. We propose a definition of narratives, subsets of the best-fitting parameters on which the learning coefficient is constant. Narratives are c...
  </details>

- **2026-10-08** — Nikolaj Thams, Anton Rask Lundborg — [Embedding-Bias in Conditional Independence Testing](http://arxiv.org/abs/2610.11584v1)
  <details><summary>📄 Abstract</summary>
  To test conditional independence of $X$ and $Y$ given a text or an image $Z$, one conditions on an embedding $ψ(Z)$ in place of $Z$. The embedded test is valid if $Z$ is independent of $X$ or of $Y$ given $ψ(Z)$, which cannot be confirmed from data, and when this fails, the rejection probability under the null hypothesis can tend to one. We study this failure, and show that focusing on a specific form of dependence relaxes what the embedding must retain. For a residual correlation test inspired ...
  </details>

- **2026-10-08** — Xincheng He, Wanli Dong, Zhaoqiang Guo et al. — [SSCBench: Evaluating the Evidential Validity of Fault-Injection Tests for Tool-Using LLM Agents](http://arxiv.org/abs/2610.11514v1)
  <details><summary>📄 Abstract</summary>
  Fault injection is increasingly used to evaluate the reliability of tool-using LLM agents. However, there has been limited study of how fault-adoption results should be interpreted when the agent itself determines which authoritative observations become visible during execution. In this paper, we present a systematic study of this evidential validity problem in agent fault-injection evaluation. We develop a measurement protocol that specifies what observations can refute an injected assertion, d...
  </details>

- **2026-10-08** — Boaz Meivar, Ofir Kedem, Amit Edenzon et al. — [Beyond Resolution: Object-to-Image Ratio Mismatch in Instance Retrieval](http://arxiv.org/abs/2610.11489v1)
  <details><summary>📄 Abstract</summary>
  Visual instance retrieval often fails when the same object appears at different apparent sizes in the query and gallery. We show that the dominant cause is usually not resolution loss but object-to-image (O2I) ratio mismatch: the object occupies different fractions of the two images. On a controlled benchmark of 3,021 Objaverse objects rendered at five camera distances, more than 80% of the cross-distance degradation is attributable to O2I mismatch rather than resolution for 9 of 12 pretrained b...
  </details>

- **2026-10-08** — Zu-En Su, Dan Cogan, Oded Kenneth et al. — [Deterministic generation of large-scale photonic GHZ states utilizing spin echo in a solid-state quantum light source](http://arxiv.org/abs/2610.11445v1)
  <details><summary>📄 Abstract</summary>
  Quantum technologies witness rapid contemporary developments transitioning from abstract scientific ideas and fundamental demonstrations, into systems of sufficient quality and scale, enabling real applications. Photonic quantum technologies are playing a pivotal role in these developments, since photons are robust, easily controlled, detect and measured, thus qualify as flying carriers of quantum information and entanglement distributers. The efforts to develop photonic quantum technologies ben...
  </details>

- **2026-10-08** — Ming-Zheng Du, Shi-Yu He, Jing Shen et al. — [Isotope Effects at Classical Cost through Mass-Differentiable Machine Learning](http://arxiv.org/abs/2610.11325v1)
  <details><summary>📄 Abstract</summary>
  Isotope effects govern fractionation and modulate reactivity, with applications from hydrogen energy to environmental science and catalysis, yet predicting them requires resolving small isotope-dependent free-energy differences that remain very challenging for conventional path-integral simulations in complex systems. Here we introduce iso-EPIGS, a path-integral coarse-graining framework built on a mass-differentiable neural network that reconstructs the mass- and temperature-dependent path inte...
  </details>

- **2026-10-08** — Kang Yang, Tianci Bu, Peng Wang et al. — [LR-V2X: Loss-Resilient Collaborative Perception under Low-Bandwidth Communication](http://arxiv.org/abs/2610.11264v1)
  <details><summary>📄 Abstract</summary>
  Given the inherent unpredictability of packet loss in vehicular wireless communications, V2X collaborative perception can yield practical benefits only if agents can achieve reliable collaboration under lossy and low-bandwidth communication conditions. Existing dense BEV feature fusion methods depend on redundant BEV feature exchange, which is infeasible in low-bandwidth scenarios, while compact-communication methods aggressively compress messages but can hardly recover the missing feature conte...
  </details>

- **2026-10-08** — Yanlong Zhao, Xiaoyuan Cheng, Huihang Liu et al. — [When Lower Reconstruction Loss Hurts: Distributionally Robust Refinement for Low-Bit LLM Quantization](http://arxiv.org/abs/2610.11226v1)
  <details><summary>📄 Abstract</summary>
  Weight-only post-training quantization (PTQ) relies heavily on reconstruction loss minimization to preserve model quality at low precision. We show that the weights favored by minimizing this loss need not yield better model performance on new tasks. In fact, we find that lower reconstruction loss can even degrade model performance on the same calibration data. Our analysis further shows that weights with lower reconstruction loss on calibration data can have higher loss than other weights when ...
  </details>

- **2026-10-07** — Vineetha Yogesh, Saif Khan Mohammed, Sandesh Rao Mattu et al. — [Low-complexity Equalization of Zak-OTFS Via Neumann Series](http://arxiv.org/abs/2610.10872v1)
  <details><summary>📄 Abstract</summary>
  We describe a general method for selecting an orthonormal basis of carrier waveforms that aligns the basis with delay / Doppler characteristics of a wireless channel. We show that our method enables low-complexity equalization for two channels of practical interest. The first is satellite communication and the second is communication from a ground station to an unmanned aerial vehicle (UAV). After Doppler compensation both scenarios are characterized by a first line of sight (LOS) path with zero...
  </details>

- **2026-10-07** — Wenbin Zhou, Elizabeth Cucuzzella, Shixiang Zhu — [Calibrating Ambiguity Set via Diagnostic Transport for Distributionally Robust Optimization](http://arxiv.org/abs/2610.10793v1)
  <details><summary>📄 Abstract</summary>
  Distributionally robust optimization (DRO) protects decisions against distributional uncertainty by optimizing over an ambiguity set, but poorly aligned set geometry can require large radii and yield overly conservative decisions. We introduce diagnostic-transport DRO (DT-DRO), which uses held-out calibration data to adapt the ambiguity-set geometry to observed predictive errors. DT-DRO uses the conditional probability integral transform cumulative distribution function to diagnose systematic pr...
  </details>

- **2026-10-07** — Mikai Hulse, Musfequs Salehin, Sosuke Inui et al. — [A nonclassical law of the wall in superfluid helium-4](http://arxiv.org/abs/2610.10923v1)
  <details><summary>📄 Abstract</summary>
  The logarithmic law of the wall is one of the most robust scaling laws of classical turbulence, yet whether it survives in a quantum fluid such as superfluid $^4$He (He II) remains unknown. At a solid wall, the viscous normal-fluid and inviscid superfluid components of He II obey fundamentally different boundary conditions, yet their motions can be coupled through quantized vortices. How these competing effects organize the near-wall flow remains an open question in quantum-fluid hydrodynamics. ...
  </details>

- **2026-10-07** — Matthew Chen, Natalie Klco — [Susceptibility of qudit-qudit entanglement to quantum noise: insights from the negativity rank](http://arxiv.org/abs/2610.10820v1)
  <details><summary>📄 Abstract</summary>
  One aspect of complexity for quantum many-body systems resides in their ability to exhibit entanglement, uniquely quantum correlations central to quantum computation. To quantitatively explore the diminishing effect that quantum noise has on entanglement resources, we focus on the negativity witness, an entanglement measure based on local time reversal transformations that provides a perfect witness in simple physical contexts. Beyond calculation of the negativity, we analyze the associated eige...
  </details>

- **2026-10-07** — Mikey Watts, Yuchen Cui — [Rephrase Before You Act: Characterizing and Mitigating Language Sensitivity in Vision-Language-Action Models](http://arxiv.org/abs/2610.10526v1)
  <details><summary>📄 Abstract</summary>
  Vision-language-action models (VLAs) are strikingly sensitive to instruction phrasing and do not inherit the language robustness of the vision-language models they are built on. A one-word edit can move success by tens of points: $π_{0.5}$ turns on a LIBERO stove 100% of the time for "switch on the stove" and 2% for "switch on the hot plate", and a $π_0$ checkpoint finetuned with rephrase augmentation still shows swings of up to 61 points. We characterize this sensitivity with statistically test...
  </details>

- **2026-10-07** — Prakhar Ganesh, Kyra Wilson, Luca Zappella et al. — [Homogenization in Multi-Agent Systems](http://arxiv.org/abs/2610.09824v1)
  <details><summary>📄 Abstract</summary>
  Multi-agent systems (MAS) leverage interactions between agents to perform complex tasks. Despite their success, we show that these interactions can also lead to homogenization, i.e., agents converging to similar behaviors. Homogenization in MAS can reduce agent diversity and reinforce shared failures. In this paper, we operationalize homogenization using three metrics: conformity to the majority, polarization towards extremes, and growing inertia against changes over subsequent interactions. We ...
  </details>

- **2026-10-07** — Nadhem Zmandar, Mo El-Haj, Paul Rayson — [A Comparative Study of Evaluation Metrics for Long-Document Financial Narrative Summarization with Transformers](http://arxiv.org/abs/2610.09529v1)
  <details><summary>📄 Abstract</summary>
  There are more than 2,000 listed companies on the UK's London Stock Exchange, divided into 11 sectors who are required to communicate their financial results at least twice in a single financial year. UK annual reports are very lengthy documents with around 80 pages on average. In this study, we aim to benchmark a variety of summarisation methods on a set of different pre-trained transformers with different extraction techniques. In addition, we considered multiple evaluation metrics in order to...
  </details>

- **2026-10-07** — Eike S. Eberhard, Xaver Kainz, Viktor Kotsev et al. — [Physics-Aligned Electronic Ground-State Learning Improves Generalization](http://arxiv.org/abs/2610.10298v1)
  <details><summary>📄 Abstract</summary>
  Machine-learned interatomic potentials (MLIPs) excel at in-distribution tasks, accelerating drug and material development, yet they struggle to generalize out-of-distribution. We propose to push the cost-accuracy Pareto frontier by designing observable-agnostic electronic ground-state descriptor models (GSMs) with computational costs situated between MLIPs and Kohn-Sham density functional theory (KS-DFT). We align the learning objectives and architectures of GSMs with the governing equations of ...
  </details>

- **2026-10-07** — Yuchen Zhu, Chenyi Xu, Yulin Zhang et al. — [Juno: Taming Predictive Latents for Vision-Language-Action Models](http://arxiv.org/abs/2610.09940v1)
  <details><summary>📄 Abstract</summary>
  Joint-embedding predictive architectures (JEPAs) predict masked or future observations in representation space, offering a natural source of predictive latents for vision-language-action (VLA) models. Yet making these latents useful across pretraining, policy learning, and deployment requires addressing three failures: mismatch with embodiment-specific control, interference with action learning, and teacher miscalibration under distribution shifts. We introduce Juno, a unified framework built ar...
  </details>

- **2026-10-07** — Mahmoud Selim, Cristina Cipriani, Karl Henrik Johansson — [Beyond Policy Support: Interaction Constrained Offline Reinforcement Learning for Autonomous Driving](http://arxiv.org/abs/2610.09763v1)
  <details><summary>📄 Abstract</summary>
  Offline reinforcement learning enables reward-driven policy improvement from fixed datasets without requiring online exploration, making it particularly attractive in safety-critical domains. A central challenge, however, is distribution shift: policy optimization may favor actions that are weakly supported by the offline data, rendering value estimates unreliable. Existing approaches primarily control this shift in the policy's own action space. In interactive environments such as autonomous dr...
  </details>

- **2026-10-07** — Mike Zhang, Dongho Kang, Kevin Bergamin et al. — [HuMBLE: Human Motion-Driven Behavior Learning for Embodied Locomotion](http://arxiv.org/abs/2610.10489v1)
  <details><summary>📄 Abstract</summary>
  Despite recent advances in humanoid locomotion, controllers optimized for command tracking and robustness tend to produce mechanical gaits, whereas controllers tied to human motion data often fail to generalize to commands outside the data distribution. This work introduces a learning framework that balances these competing objectives to synthesize real-time steerable, robust, and biomimetic locomotion policies from human data. Using an in-house curated locomotion dataset covering diverse speeds...
  </details>

- **2026-10-07** — Jixuan Chen, Jiaxin Zhang, Qinyuan Ye et al. — [CoTrace: Data Recipes for Training Terminal Agents with Harness-Model Co-Evolution](http://arxiv.org/abs/2610.10426v1)
  <details><summary>📄 Abstract</summary>
  Terminal-agent capability depends jointly on model weights and the runtime harness that formats prompts, binds tools, and handles error recovery. Existing harness-model co-evolution approaches improve both components, yet often treat trajectories produced during harness search as an undifferentiated replay buffer. This practice overlooks that a trajectory's value for model training depends on the harness under which it was generated. To systematically analyze this interface, we establish an alte...
  </details>

- **2026-10-07** — Nipun Ghanghas, Dinil B. Palakkatharappil, Rafael A. Garcia et al. — [ROSE (Red-giant Oscillations Spectra Estimator): A Modular Machine-Learning Framework for Automated Asteroseismic Characterisation. I. $ν_{\max}$ and $Δν$ from TESS](http://arxiv.org/abs/2610.10312v1)
  <details><summary>📄 Abstract</summary>
  Space-based photometry from Kepler and TESS has delivered oscillation spectra for hundreds of thousands of red giants, and PLATO and the Roman Galactic Bulge Time-Domain Survey will add more. We present ROSE, a modular machine-learning framework for automated asteroseismic characterisation of red giants, and apply two of its modules to the frequency of maximum oscillation power, $ν_{\rm max}$, and the large frequency separation, $Δν$. Each module is a neural network bundled with its own preproce...
  </details>

- **2026-10-07** — Theodor Wulff, Angelo Cangelosi — [Do Vision-Language-Action Models Understand Instructions? A Mechanistic Interpretability Study on Language Grounding](http://arxiv.org/abs/2610.10178v1)
  <details><summary>📄 Abstract</summary>
  Vision-Language-Action models are designed to generalise across environments and task descriptions, raising the question of whether their action generation actually depends on the language instruction, or whether they largely rely on visual cues and superficial correlations. Robustness to variance in the visual and linguistic observation space is critical for real-world deployment, yet VLAs lack explicit grounding modules and instead rely on the intrinsic language grounding capabilities of their...
  </details>

- **2026-10-07** — Zhongping Ji — [HySPE: Positional Encoding via Symplectic Dual Shears](http://arxiv.org/abs/2610.10154v1)
  <details><summary>📄 Abstract</summary>
  We introduce Hyperbolic Symplectic Positional Encoding (HySPE), grounding positional attention in non-compact symplectic transformations. While canonical Rotary Position Embedding (RoPE) parameterizes the compact, elliptic branch of $\Sp(2,\R)$ via rotations, HySPE operationalizes its hyperbolic branch via a damped symmetric composition of dual shears, yielding a conformally symplectic contraction with two spectral decay rates per channel pair. To eliminate the exponential representation drift i...
  </details>

- **2026-10-07** — Alessandro Beatini, Marco Maronese, Emanuele Rodolà — [Activation-Aware Weight Tensorization: A Calibration-Time Preconditioner for Tensor-Network LLM Compression](http://arxiv.org/abs/2610.10085v1)
  <details><summary>📄 Abstract</summary>
  Post-training tensor-network compression replaces Transformer linear layers with Tensor Train (TT) or Tree Tensor Network (TTN) operators, but standard decompositions minimize weight-space Frobenius error rather than functional error under the layer's activation distribution. We propose Activation-aware Weight Tensorization (AWT), a training-free calibration wrapper that preconditions each weight matrix with a diagonal activation-derived scale before an unchanged TT/TTN solver and deploys the re...
  </details>

- **2026-10-07** — Matthieu Jeannin, Alessandro Chessari, Jan Von Delft — [Efficient Optimization of Tensor Rings with Low-Rank Environments](http://arxiv.org/abs/2610.10027v1)
  <details><summary>📄 Abstract</summary>
  Tensor-ring (TR) decompositions provide a natural representation of periodic systems but are difficult to optimize because the closed geometry prevents a global canonical form and leads to costly, ill conditioned environments. Existing periodic DMRG methods alleviate this difficulty by compressing long environments to a low-rank representation, reducing local operations to $\mathcal{O}(pχ^3)$, where $p$ is the retained environment rank. Here, we extend this approach to an efficient two-site Ring...
  </details>

- **2026-10-07** — Eliyahu Levy, Adam Teman, Yoni Pugachov — [TR-PTQ: High-Accuracy Integer-Only Transformer Post Training Quantization via Taylor Region Reformulation](http://arxiv.org/abs/2610.09969v1)
  <details><summary>📄 Abstract</summary>
  Post-training quantization (PTQ) enables efficient deployment, yet transformer architectures remain challenging to quantize due to nonlinear layers. While existing methods attribute accuracy loss to insufficient numerical precision, often necessitating floating-point fallbacks, we demonstrate that degradation is actually driven by specific structural error sources. We find that learned scale parameters in normalization layers and compounded approximations in GELU are the primary error contributo...
  </details>

- **2026-10-07** — Bernardo A. C. Pereira, Marcos Carvalho, Fatih Temiz et al. — [Deadline-Aware Multi-Agent Reinforcement Learning for TSN-Based Vehicular Edge Networks](http://arxiv.org/abs/2610.09870v1)
  <details><summary>📄 Abstract</summary>
  Vehicular edge computing (VEC) enables latency-sensitive applications by bringing computing and networking resources closer to vehicles. However, existing approaches often overlook network contention among co-located services with heterogeneous and dynamic latency requirements. While time-sensitive networking (TSN) provides bounded-latency communication, conventional and reinforcement learning-based schedulers struggle to adapt to highly dynamic vehicular environments and inter-queue dependencie...
  </details>

- **2026-10-07** — Henrique L. Senger, Gustavo P. Gonçalves, Bruno S. Chang et al. — [Effects of Residual Chirp Rate on DAFT-s-AFDM Uplink Performance](http://arxiv.org/abs/2610.09851v1)
  <details><summary>📄 Abstract</summary>
  Affine frequency division multiplexing (AFDM) is robust to doubly dispersive channels in high-mobility 6G systems but, like orthogonal frequency division multiplexing (OFDM), suffers from a high peak-to-average power ratio (PAPR). Spreading with a discrete affine Fourier transform (DAFT) yields DAFT-s-AFDM, whose precoder and modulator chirps can be chosen independently. For a single user with zero-offset localized allocation, we show that these two chirps merge into a single residual chirp whos...
  </details>

- **2026-10-07** — Masaaki Nakatsu, Reno Wang — [Decoupling Logic from Persona: Structural Immunity of Edge LLM Agents to Context Pollution](http://arxiv.org/abs/2610.09772v1)
  <details><summary>📄 Abstract</summary>
  Small language-model agents on edge devices must hold a persona and reason correctly at once, inside one context window that fills with conversational history and persona instructions. We study what happens to the logical part of such an agent when that history is long, misleading and persona-heavy (persona-logic interference), and present a Decoupling Architecture (AO-DA) that separates logical inference ("What") from persona expression ("How") into two inference paths on one INT4 base model wi...
  </details>

- **2026-10-07** — Tom Beucler, J. David Neelin, Hui Su et al. — [Artificial intelligence pathways from weather to climate](http://arxiv.org/abs/2610.09770v1)
  <details><summary>📄 Abstract</summary>
  Deep learning has made rapid advances in weather forecasting: autoregressive models trained on atmospheric reanalyses now rival dynamical models across nowcasting, medium-range, and subseasonal-to-seasonal lead times, producing well-calibrated ensemble forecasts at reduced cost. We review these advances and consider their extension to climate horizons, where the challenge shifts from initial-condition skill to producing reliable statistical responses under altered forcings. AI-powered climate pr...
  </details>

- **2026-10-07** — Mariia Baidachna, Nicolas Pugeault — [Flow-of-Thought: A Framework for Visual Reasoning](http://arxiv.org/abs/2610.09746v1)
  <details><summary>📄 Abstract</summary>
  Mental imagery, ``seeing with the mind's eye'' is an essential aspect of human cognition. Despite rapid progress Large Language Models (LLMs) and Vision Transformers (ViTs) still underperform on tasks requiring spatial understanding. To address this, we introduce Flow-of-Thought (FoT), a framework that integrates the generation of visual sketches as intermediate reasoning steps, mimicking mental imagery in humans. We train coordinate-aware trajectory flow fields on $SO(2)$ group orbits and cumul...
  </details>

- **2026-10-07** — Sourav Saha, Aditya Dutta, Soumajit Pramanik et al. — [Towards Explaining Query Expansion Performance in Information Retrieval](http://arxiv.org/abs/2610.09724v1)
  <details><summary>📄 Abstract</summary>
  Query Expansion (QE) techniques have long been widely used in Information Retrieval (IR) to address the vocabulary mismatch problem. They remain relevant in modern retrieval systems, including those based on large language models (LLMs). However, no single QE method consistently outperforms others across all queries. This work seeks to explain the variation in QE performance through two complementary perspectives. The first is the concept of an Ideal Expanded Query (IEQ)--a hypothetical query th...
  </details>

- **2026-10-07** — Sangyoon Bae, Sk Miraj Ahmed, Shinjae Yoo et al. — [Pretraining Shapes Spectral Structure: Architecture- and Strategy-Conditional Prediction of OOD Robustness in Foundation Models](http://arxiv.org/abs/2610.09709v1)
  <details><summary>📄 Abstract</summary>
  Can we determine whether a foundation model will generalize out-of-distribution (OOD) before any target data is available? Existing diagnostics require source or target data, which rules them out before a target domain exists. Those that use the weights alone apply one statistic to every architecture, and do not separate robust models from fragile ones. We show the answer is encoded in the spectral structure of pretrained weights. Two forces shape that structure. Architecture determines how info...
  </details>

- **2026-10-07** — Qifan Zhang, Ruijie Li, Fangzhou Zhang et al. — [CircuitGate: Logic-Consistent Circuit-Level Functional Modeling for And-Inverter Graphs](http://arxiv.org/abs/2610.09549v1)
  <details><summary>📄 Abstract</summary>
  And-Inverter Graphs (AIGs) are fundamental representations for logic synthesis and verification in Electronic Design Automation (EDA). As structured representations of complex digital systems, AIGs require models to capture functional dependencies beyond local structure and remain robust to functionality-preserving transformations. In learning-based AIG representation, existing approaches are predominantly based on GNNs and rely on local gate-level message passing, limiting their ability to capt...
  </details>

- **2026-10-07** — Dasari Naga Raju — [TIRA: Tumor Immune Representation Adaptation for Zero-Shot Cross-Cancer MSI and TMB Prediction](http://arxiv.org/abs/2610.09441v1)
  <details><summary>📄 Abstract</summary>
  Microsatellite instability-high (MSI-H) and high tumor mutational burden (TMB-H) are clinically relevant biomarkers, yet their histopathological prediction remains challenging when models are transferred across morphologically distinct cancer types. Immune-associated spatial patterns can persist across cancers despite these morphological differences, but foundation-model-based predictors trained on a single cancer do not explicitly use this information, limiting cross-cancer generalization. To a...
  </details>

- **2026-10-07** — Shadi Alijani, Fereshteh Aghaee Meibodi, Homayoun Najjaran — [Quantifying Volumetric Risk: Class-Aware Asymmetric Weighted Conformal Prediction for 3D Medical Image Segmentation](http://arxiv.org/abs/2610.09392v1)
  <details><summary>📄 Abstract</summary>
  Reliable volumetric segmentation is critical for clinical diagnostics, yet foundation models such as MedSAM remain deterministic and lack calibrated uncertainty under distribution shift. Existing conformal prediction methods offer statistical guarantees but are frequently applied in 2D and assume symmetric error distributions, so they do not capture the class-specific biases that arise in 3D multi-class segmentation. We propose Class-Aware Asymmetric Weighted Conformal Prediction (CA-WCP), which...
  </details>

- **2026-10-07** — Tomonari Kanazawa, Hikaru Hoshino, Eiko Furutani — [Learning Stability of Replay-Based Co-Optimization for Transmission Expansion under Strategic Bidding](http://arxiv.org/abs/2610.09366v1)
  <details><summary>📄 Abstract</summary>
  This paper investigates the behavior of learning-based co-optimization for transmission expansion under strategic bidding in electricity markets. In this framework, transmission capacities are updated while market participants simultaneously learn their bidding strategies through deep reinforcement learning, resulting in coupled and non-stationary learning dynamics. We show that transient policy degradation of bidding agents can generate inconsistent cost-capacity samples, which bias the transmi...
  </details>

- **2026-10-07** — Yatai Ji, Zhengqiu Zhu, Yong Zhao et al. — [SearchWorld: Spatial Value-Grounded Imagination for UAV Object Search via World Models](http://arxiv.org/abs/2610.09335v1)
  <details><summary>📄 Abstract</summary>
  Autonomous unmanned aerial vehicle (UAV) object search involves a closed loop of perception, decision-making, and action under partial observability. Urban environments pose several challenges: large search areas and narrow egocentric views limit coverage, dense 3D geometry constrains safe motion, and open-world instructions require identifying a specific target among distractors. Many existing methods mitigate partial observability through explicit maps or memory representations, yet remain lar...
  </details>

- **2026-10-07** — Fangping Lan, Qi Zhang, Eduard Dragut — [CATune: Structural Constraint-Aware Bayesian Optimization for DBMS Configuration Tuning](http://arxiv.org/abs/2610.09276v1)
  <details><summary>📄 Abstract</summary>
  Modern DBMSs expose hundreds of configuration knobs, resulting in a high-dimensional and heterogeneous search space that makes automated tuning costly. Existing ML-based tuning systems typically treat the configuration domain as box-constrained and rely on workload feedback to implicitly capture inter-knob relationships. However, DBMS documentation specifies deterministic knob dependency constraints, particularly ordering constraints, that characterize structurally valid regions of the configura...
  </details>

- **2026-10-06** — Wenqi Li, Bin Liu, Mindi Ruan et al. — [Conditional Accuracy Profiles: Diagnosing LLM Judges across Deployment Conditions](http://arxiv.org/abs/2610.09229v1)
  <details><summary>📄 Abstract</summary>
  LLM-as-judge is now a standard tool for scalable evaluation, but judge performance is still often summarized by a single accuracy number. This aggregate view hides the deployment conditions under which a judge succeeds or fails. We introduce \textbf{Conditional Accuracy Profiling} (CAP), a post-hoc diagnostic framework that decomposes pairwise LLM-judge accuracy into eight conditions organized into content sensitivity, robustness, and rationale quality. CAP is benchmark-agnostic: it can be appli...
  </details>

- **2026-10-06** — Arkajyoti Chakraborty, Aryan Tayal, Ishika Agarwal et al. — [ToolRACER: A Robust Agentic Conversation Emulation Resource for Agent Training and Evaluation](http://arxiv.org/abs/2610.09163v1)
  <details><summary>📄 Abstract</summary>
  Task-oriented conversational agents remain fragile under real world conversation scenarios as they rarely follow a predictable script, especially when users exhibit non-cooperative behavior. Existing function-calling benchmarks often emphasize successful, cooperative interactions and underrepresent adversarial conversation trajectories, thereby limiting the training resources available for developing robust agents. We present ToolRACER, a synthetic data generation pipeline that coordinates user,...
  </details>

- **2026-10-06** — Haoran Li, Zengle Ge, Xiaomin Yuan et al. — [RLDISCOVER: LLM-driven co-evolution of reinforcement learning algorithms](http://arxiv.org/abs/2610.09218v1)
  <details><summary>📄 Abstract</summary>
  LLM-guided program evolution has enabled discoveries in mathematics and computational optimization, raising the prospect of reinforcement learning (RL) algorithms that self-evolve to improve how agents learn. However, realizing this prospect faces two obstacles. Joint search over coupled algorithmic components is difficult to scale: simultaneous changes can disrupt learning, while isolated changes overlook their dependencies. Evaluating candidate algorithms also requires costly training, with fi...
  </details>


### 📂 watermark
*水印与溯源 / Watermarking & Provenance* — 23 papers

- **2026-10-08** — Shuai Guo, Yidong Cui — [BeliefScope: Diagnosing Evidence-Driven Revision and Pressure-Induced Shifts in Large Language Models](http://arxiv.org/abs/2610.11305v1)
  <details><summary>📄 Abstract</summary>
  A language model may revise the same proposition after receiving genuinely relevant evidence or after receiving directional user pressure that adds no relevant fact. The observable response shift alone therefore does not reveal which source drove the change. We introduce BeliefScope, a controlled black-box framework for separating these two sources of influence around a fixed target proposition. BeliefScope crosses Evidence and Pressure with factor-specific local controls and measures response c...
  </details>

- **2026-10-08** — Zhuohong Chen, Zhengxian Wu, Yunyao Yu et al. — [WorldFact-Bench: Beyond Image-Internal Plausibility to Image-World Consistency](http://arxiv.org/abs/2610.11184v1)
  <details><summary>📄 Abstract</summary>
  Advances in image generation have made visual authenticity increasingly difficult to assess. Although image forensics now examines both generation artifacts and higher-level visual inconsistencies, a plausible image can still contradict real-world facts or rules. We introduce WorldFact-Bench to evaluate image-world consistency from a single image, without a predefined claim or verification target. The benchmark contains 1,274 source-aligned real-fake pairs across four verification regimes and te...
  </details>

- **2026-10-08** — Julian Chan, Javier Mora Jimenez — [Prior or Feedback? What an LLM Uses When Adapting Neural Operators](http://arxiv.org/abs/2610.12325v1)
  <details><summary>📄 Abstract</summary>
  Do LLM scientific agents rely only on their initial task context, or do they adapt their decisions in response to experimental feedback? We study this question in neural operator adaptation, where a large language model (LLM) selects fine-tuning configurations under a limited trial budget. Across transfers within and between partial differential equation (PDE) families, the LLM achieves lower held-out test nRMSE than random search and Bayesian optimisation in nearly every matched comparison. End...
  </details>

- **2026-10-08** — Zoe Li — [Traceable World State: A Provenance-Aware State Representation and Deterministic Replay Framework for Robotic Systems](http://arxiv.org/abs/2610.12033v1)
  <details><summary>📄 Abstract</summary>
  Robotic systems operating over extended tasks must maintain a world state assembled from observations arriving at different times, with varying confidence and potential revisions. Conventional representations emphasize latest estimates, hindering fact provenance, decision reproduction, or execution auditing. We present Traceable World State (TWS), a middleware-neutral semantic representation and reference runtime for provenance-aware robot world state. A TWS snapshot captures entities, relations...
  </details>

- **2026-10-08** — Zhaoxin Yu, Qingchao Kong, Dajun Zeng et al. — [Examining Social Attribution in LLM Reasoning: A Theory-Guided Probing Methodology](http://arxiv.org/abs/2610.12022v1)
  <details><summary>📄 Abstract</summary>
  Large language models (LLMs) are increasingly deployed in sociotechnical systems where social attribution, the reasoning process attributing external events to the causes and reasons of agents' social behaviors, plays a critical role. These processes involve judgments of social cause, responsibility, and blame/credit to agents. Although attributional models are well-studied in social psychology and cognition through Attribution Theory, social attribution remains underexplored in AI, particularly...
  </details>

- **2026-10-08** — Hoyeol Sohn, Wonil Kim, Keunhyoung Kim et al. — [STEMMA: Song-to-Stem Multi-Audio Reasoning for Large Audio Language Models](http://arxiv.org/abs/2610.11884v1)
  <details><summary>📄 Abstract</summary>
  Music understanding often requires comparing excerpts and reasoning about relationships among songs, sections, and stems. However, existing large audio-language models (LALMs) and music question-answering datasets typically operate on single recordings or compare independently sampled tracks with no known production relationship. We introduce STEMMA, a multi-audio music question-answering framework built around production provenance: whether excerpts originate from the same track or section, and...
  </details>

- **2026-10-08** — Jiaqi Liao, Yuanzhao Zhai, Huanxi Liu et al. — [Error-Propagation Modeling for Failure Attribution in LLM-Based Multi-Agent Systems](http://arxiv.org/abs/2610.11600v1)
  <details><summary>📄 Abstract</summary>
  LLM-based multi-agent systems (MASs) are increasingly used to solve complex tasks through coordinated reasoning, tool use, and interaction with external resources. However, attributing failures in such systems remains challenging because the observed outcome often does not directly reveal the error responsible for the failed execution. In this work, the attribution target is the decisive error, defined as the agent--step pair whose correction would recover the failed execution. Existing approach...
  </details>

- **2026-10-08** — Yasunobu Ando, Masashige Miyamamoto, Keita Hiromori et al. — [Generation, Accumulation, and Utilization of Data in the Automatically Controlled End-Station of a Soft X-ray Beamline](http://arxiv.org/abs/2610.11476v1)
  <details><summary>📄 Abstract</summary>
  AI is rapidly transforming materials exploration, yet reliable AI-assisted research depends on experimental data that retains their context, provenance, and machine-readable structure. High-throughput synchrotron measurements therefore require more than automated data acquisition: data generation, accumulation, and utilization must be connected within a continuous workflow. Here, we present a data-centric research framework that integrates the PIONEER system, the OMNES, and ML analysis. The PION...
  </details>

- **2026-10-08** — Chiara Bonfanti, Cataldo Basile — [GROB: A Multi-Agent Architecture for Public-Trace Investigation of Candidate Agentic Activity](http://arxiv.org/abs/2610.11467v1)
  <details><summary>📄 Abstract</summary>
  We present GROB, a multi-agent architecture for investigating candidate autonomous-agent activity through public Internet traces when privileged telemetry is unavailable. The system performs controlled, read-only collection of public traces and preserves selected observations for later resolution. In a frozen September 2026 corpus, several collected traces became more informative as additional public evidence emerged. The strongest result concerns Census-labelled identifiers captured on 9 Septem...
  </details>

- **2026-10-08** — Weilin Jin, Mingyu Wang, Taiyu Zhu et al. — [ReCast: Attribution-Oriented Step Representation Learning for LLM-Based Agent Systems](http://arxiv.org/abs/2610.11334v1)
  <details><summary>📄 Abstract</summary>
  In LLM-based agent systems, failures can originate from early steps whose effects propagate through subsequent interactions, making their origins difficult to identify. To trace such failures back to their origin, failure attribution has been formulated as the task of identifying the earliest step responsible for the failure. Recent methods leverage LLM internal signals for failure attribution, typically using hidden states as step representations. We therefore conduct an empirical study to eval...
  </details>

- **2026-10-08** — Zirui Liao, Zhengxian Wu, Zhuohong Chen et al. — [From Retrieval to Reconstruction: Constructing Evolvable Cognitive Memory for Long-Term Dialogue](http://arxiv.org/abs/2610.11314v1)
  <details><summary>📄 Abstract</summary>
  Large Language Models (LLMs) serving as long-term dialogue agents require memory systems that support reliable reasoning over extended interactions. However, existing Retrieval-Augmented Generation (RAG) frameworks typically treat memory as passive storage, making it difficult to distinguish source-attributed beliefs from unattributed event/fact records and to connect evidence dispersed across sessions. We introduce CogMem, a cognitive memory architecture based on the PEC$^2$F (Person-Event-Conc...
  </details>

- **2026-10-08** — Hanchen Xia, Baoyou Chen, Yutang Ge et al. — [REMORY: Learning Residual Memory for Context Compaction](http://arxiv.org/abs/2610.11287v1)
  <details><summary>📄 Abstract</summary>
  Long-horizon agents compact their history to continue within a finite context window, but a textual summary alone may not support every subsequent decision. We introduce REMORY, a neural memory network that supplements the summary with a bounded sequence of soft memory tokens. Given the history and summary, the network learns to generate tokens that help a frozen LLM approximate the continuation it would produce with the full history. The tokens are conditioned on the summary and appended after ...
  </details>

- **2026-10-07** — Lex Konnelly, Elena Khasanova, Riqiang Wang et al. — [Back in Style: A Sociolinguistic Approach to Authoring and Measuring Persona Fidelity in User Simulation](http://arxiv.org/abs/2610.10988v1)
  <details><summary>📄 Abstract</summary>
  As agentic systems gain commercial popularity, user simulators increasingly serve as measurement instrument for their evaluation. However, the fidelity of simulated users in comparison to real human users is generally low, and typically assessed by costly, subjective LLM judges. In this pilot study, we ask whether fidelity can instead be measured deterministically by treating a user persona sociolinguistically: as a social type that emerges from observable linguistic style, rather than one predi...
  </details>

- **2026-10-07** — Tabia Tanzin Prama, Julia Witte Zimmerman, Christopher M. Danforth et al. — [Localized, unstable, and entangled: Exploring `Us vs. Them' bias in Large Language Models](http://arxiv.org/abs/2610.10864v1)
  <details><summary>📄 Abstract</summary>
  Large language models (LLMs) exhibit us-vs.-them bias: A behavioral asymmetry in which prompts framed around an ingroup (``we''/``us'') receive systematically more positive continuations than matched prompts framed around an outgroup (``they''/``them''). Using Edge Attribution Patching (EAP), we localize this behavior to directed circuits in GPT-2 Small, GPT-2 Large, Llama-2 7B, and Llama-3 8B. Across models, high-attribution edges are sparse and concentrated primarily in middle-to-late layers, ...
  </details>

- **2026-10-07** — Amit Nautiyal — [Which Rollout Taught It That? BehaviorTrace and the Limits of Training-Data Attribution in Online RL](http://arxiv.org/abs/2610.10422v1)
  <details><summary>📄 Abstract</summary>
  When reinforcement learning teaches a language model a new behavior, can we find the training rollouts that taught it? And when an attribution method says it can, how do we know the answer is real? We study both questions on online RL fine-tuning with GRPO, using a planted behavior with a known cause. We release BehaviorTrace, an open evaluation harness that combines full-gradient sketching, the planted-behavior setup, and controls for gradient magnitude, fluency, headroom, and variation across ...
  </details>

- **2026-10-07** — J. -P. Bouchaud, I. Mastromatteo, B. Toth — [On Bonart's interpretation of the Square-Root Impact Law](http://arxiv.org/abs/2610.10053v1)
  <details><summary>📄 Abstract</summary>
  The square-root impact law (SRIL), $I = Yσ\sqrt{Q/V}$, bundles two facts that a single mechanism must explain at once: a shape (impact proportional to square-root of traded volume $Q$) and an amplitude ($Y=O(1)$, independent of the participation rate $\varphi$). Bonart has recently proposed an elegant solution: if realized and counterfactual prices are both diffusive, information-neutral impact must have white increments and the SRIL follows without the wart. We reformulate and simplify his argu...
  </details>

- **2026-10-07** — Jinheon Baek, Soyeong Jeong, Yumin Choi et al. — [RunningTab: Direct Workspace Interaction with Environment-Side Tabs](http://arxiv.org/abs/2610.10444v1)
  <details><summary>📄 Abstract</summary>
  Much knowledge work produces new deliverables from files a workspace already holds, and LLM agents are beginning to take such work over. Through direct corpus interaction, an agent can search and read any of those files from a terminal with no indexing, and producing a deliverable from many of them in this way is what we call direct workspace interaction (DWI). Reaching the files, however, is only half the task: nothing keeps track of what the task asks for, what has been read, and what was list...
  </details>

- **2026-10-07** — Kun Liu, Liqun Chen — [OOM-RL II: Reality Is an Oracle, Not a Debugger Provenance-Constrained Diagnosis in Continually Evolving Agent-Engineered Systems](http://arxiv.org/abs/2610.10256v1)
  <details><summary>📄 Abstract</summary>
  Reality may establish that an outcome occurred without identifying which evolving procedure produced it or why. This distinction matters in production ML systems whose code, configuration, and artifacts change while external feedback accumulates. We examine it in a human-directed, agent-engineered quantitative trading system, using oracle to mean an external source of realized outcomes rather than a complete correctness specification. Across one year, the account gained and outperformed a broad ...
  </details>

- **2026-10-07** — Hengbo Xiao, Boyao Zhang, Purui Liu et al. — [RewardWeaver: Long-Horizon Interactive Learning for Language Agents via Self-Evolving Reward Adaptation](http://arxiv.org/abs/2610.10120v1)
  <details><summary>📄 Abstract</summary>
  Reinforcement learning with verifiable rewards (RLVR) has driven substantial progress in domains where task outcomes can be reliably evaluated, but long-horizon interaction remains challenging due to sparse terminal feedback and difficult credit assignment. Process rewards provide denser supervision, yet the capabilities most relevant for training can change as the policy evolves: a behavior that is easy to evaluate or frequently deficient need not be the bottleneck currently limiting task succe...
  </details>

- **2026-10-07** — Gabriel Ocana-Santero, Marko Tvrdic — [CircuitATLAS: Agentic reasoning over a systems neuroscience knowledge graph for target discovery in circuitopathies](http://arxiv.org/abs/2610.09643v1)
  <details><summary>📄 Abstract</summary>
  Drug discovery for neurological disease has traditionally centered on the molecules altered by disease. But the molecules that cause pathology are not necessarily the best points from which to reverse it. Here, we ask which otherwise unaltered molecular control points can be engaged to restore pathological neural circuits toward functional states. We present CircuitATLAS, a provenance-grounded systems-neuroscience knowledge graph and agentic framework for target discovery in circuitopathies. It ...
  </details>

- **2026-10-07** — Jiayu Feng — [Right Number, Wrong State? Measuring Cross-Jurisdiction Substitution in LLM Recall of State Policy](http://arxiv.org/abs/2610.09458v1)
  <details><summary>📄 Abstract</summary>
  When an LLM answers a state-specific policy question wrongly, it may be hallucinating, or it may be returning a real value that holds in another state. We test this with a minimal-set design: the question wording is fixed and only the jurisdiction varies, across the 50 U.S. states and the District of Columbia (51 jurisdictions) and three exactly defined Medicaid income-eligibility quantities. Gold values come from an official data book and agree with an independent source in 101 of 102 checked c...
  </details>

- **2026-10-07** — Xiaofei Zhang — [No Trace, No Claim: Two Contracts for Database Agents](http://arxiv.org/abs/2610.09286v1)
  <details><summary>📄 Abstract</summary>
  LLM agents can generate database operations and explain their results, but current interfaces often leave a gap between generated plans, execution conditions, and claims presented to users. We argue that agent-facing data systems need two enforceable contracts. A plan contract defines what an agent may execute and reference; an evidence contract records the belief state, completeness, and provenance under which a result supports a claim.   We instantiate these contracts in TGMS, a bi-temporal gr...
  </details>

- **2026-10-06** — Wenhui Chu, Sheikh Rabiul Islam — [TwinGuard-Lite: A Rule-Based State-Admission Gateway for Generative Patient Digital Twins](http://arxiv.org/abs/2610.09012v1)
  <details><summary>📄 Abstract</summary>
  Future generative patient digital twins may combine longitudinal health records with language-model agents and keep information across sessions. The wording of a proposed update does not reveal whether it comes from an allowed source, conflicts with the patient's record, or belongs to someone else. We present TwinGuard-Lite, a rule-based gateway that admits an update to a twin's persistent state only if it passes checkable approximations of two integrity properties. Grounded state consistency (G...
  </details>


### 📂 unlearning
*机器遗忘 / Machine Unlearning* — 2 papers

- **2026-10-08** — Xunlei Chen, Qinghui Gong, Jingkun Xue et al. — [Not Every Change Is Necessary: Recoverable Drift in Large Language Model Unlearning](http://arxiv.org/abs/2610.11915v1)
  <details><summary>📄 Abstract</summary>
  Machine unlearning in large language models aims to remove unwanted knowledge while preserving the model's remaining capabilities. Although existing methods use retention objectives or restrict where edits occur, achieving the desired forgetting level can still leave collateral changes that impair non-target behavior. Our recovery comparisons suggest that some of these changes can be reversed while preserving observed forgetting performance. In this work, we present Propose-Then-Project Unlearni...
  </details>

- **2026-10-07** — Jiho Lee, Jeongeun Park, Heayoun Choi et al. — [Sparse Feature Policy Unlearning Mitigates State Hallucination in Vision-Language-Action Models](http://arxiv.org/abs/2610.09496v1)
  <details><summary>📄 Abstract</summary>
  Vision-Language-Action (VLA) models have shown strong generalization in robotic manipulation by leveraging rich representations from pretrained vision-language models. However, their deployment in real-world environments remains limited by recurring unreliable behaviors. In this work, we study state hallucination, a recurring failure pattern in which a VLA continues acting as if an unrealized robot-object state had been achieved. Our analyses find that state hallucination coincides with weakened...
  </details>


### 📂 agent-safety
*Agent 安全框架 / Agent Safety Frameworks* — 3 papers

- **2026-10-08** — Youwei Feng, Yitong Zhang, Yuetong Liu et al. — [Safe Actions Alone Do Not Ensure Safe Agents: Identifying Unfulfilled Obligations with Guard Models](http://arxiv.org/abs/2610.11773v1)
  <details><summary>📄 Abstract</summary>
  Guard models are increasingly used to safeguard LLM-based agents, primarily by identifying actions that agents are forbidden to perform. However, identifying forbidden actions alone is insufficient to ensure agent safety. In this paper, we argue that agent safety also depends on identifying required yet unperformed safety-critical actions, which we call obligations. Our preliminary study on a popular benchmark for evaluating safety shows that 56.92% of GLM-5.3 trajectories contain unfulfilled ob...
  </details>

- **2026-10-08** — Hanjun Luo, Junting Mao, Yuhan Lu et al. — [Workerville: Towards an Organizational Behavior Account of Agent Safety](http://arxiv.org/abs/2610.11561v1)
  <details><summary>📄 Abstract</summary>
  LLM-based agents now interact with their environments continuously, shaped by such organizational channels as user instructions, peer messages, and long-term memory. Existing safety research has examined these influences, but largely as separate agent components. How such factors jointly shape an agent's safety behavior from a unified perspective remains unmeasured. To bridge this gap, we advocate organizational behavior (OB) as a framework for studying the safety of advanced agents, reorganizin...
  </details>

- **2026-10-07** — Tianruo Rose Xu, Jiawei Ren, Yichi Yang et al. — [RT-Safe: Benchmarking Agent Safety in Real-Time Embodied Environment](http://arxiv.org/abs/2610.09294v1)
  <details><summary>📄 Abstract</summary>
  Rapid progress in AI agents has brought growing attention to agent safety, with extensive evaluation focused on digital environments. As agents move into the physical world, embodied safety becomes increasingly important: failures can cause human injury and costly hardware damage. Beyond selecting safe actions, embodied agents must also operate under real-time constraints: the physical world does not pause while an agent reasons. As pedestrians move and vehicles approach during inference, an act...
  </details>


### 📂 survey
*综述与系统化 / Surveys & Systematization* — 7 papers

- **2026-10-08** — Md Shamimur Rahman, Khairul Alam, Banani Roy et al. — [Who Pays the Review Cost? Triage, Fairness, and Accountability in AI-authored Pull Requests](http://arxiv.org/abs/2610.11179v1)
  <details><summary>📄 Abstract</summary>
  AI coding agents are moving from local code assistance into pull-based workflows, where generated contributions must be reviewed, explained, and maintained within existing project norms. Although recent work has begun to characterize AI-authored pull requests (AIPRs), less is known about how reviewers govern their entry into review, how AI authorship reshapes credibility and fairness, and what intake mechanisms protect review sustainability. We report a mixed-method questionnaire survey of 239 p...
  </details>

- **2026-10-07** — Shivam Shukla, Jihye Kim, Shubham Gaur et al. — [RELATE: An Evaluation Framework for measuring Relational Orientation of Large Language Models](http://arxiv.org/abs/2610.09569v1)
  <details><summary>📄 Abstract</summary>
  Large language models (LLMs) are increasingly used for emotional support, raising concern that sustained use may draw users away from their real-world relationships. Yet existing evaluations primarily focus on the safety, empathy, or helpfulness of responses, leaving under-examined a relational question: where does the model orient the user for continued support? To address this question, we introduce relational orientation, a property operationalized through two non-exclusive dimensions: inward...
  </details>

- **2026-10-07** — Raviraja G, Viraj Bagal, Prabhath Chellingi — [From Retrieval to Customer Context: Evaluating Frontier-Model Systems for Voice-of-Customer Analysis](http://arxiv.org/abs/2610.09375v1)
  <details><summary>📄 Abstract</summary>
  Organizations increasingly use frontier language models to analyze customer feedback, but answer quality also depends on how that feedback is organized and made available. We define a \emph{customer context graph} as a unified model of customer and business context. Typed relationships connect customer objects (feedback, conversations, users, and accounts), operational objects (tickets, support agents, opportunities, and competitors), and analytical or action objects (taxonomy concepts, evidence...
  </details>

- **2026-10-07** — Nicolas Lacroix, Frederic Precioso, Mireille Blay-Fornarino et al. — [Using Small Language Models to Reverse-Engineer Machine Learning Pipelines Structures](http://arxiv.org/abs/2610.10261v1)
  <details><summary>📄 Abstract</summary>
  Context: Once defined a taxonomy of stages structuring Machine Learning (ML) pipelines (e.g. Data Preprocessing, Modeling...), extracting these stages from source code is key for better understanding ML practices. However, the diversity caused by the constant evolution of ML (e.g., algorithms, datasets) makes this task challenging. Existing approaches either rely on non-scalable manual labeling or on classifiers that do not properly support domain's diversity. These limitations call for more rel...
  </details>

- **2026-10-07** — Robert Bredereck, Eva Deltl, Tanmay Inamdar et al. — [Envy-free Allocations with Individual Payments](http://arxiv.org/abs/2610.09610v1)
  <details><summary>📄 Abstract</summary>
  When an envy-free allocation of indivisible goods does not exist, monetary transfers can restore envy-freeness. Existing work on fair division with subsidies, however, typically assumes that these payments are provided by an external source, an assumption that may be unrealistic in many applications. We address this limitation by allowing only monetary transfers between agents, with each agent's payments constrained by their individual budget. We show that while it is polynomial-time tractable t...
  </details>

- **2026-10-07** — Hyeongjun Choi — [MARS: Malware Analysis with Rule-Based Scoring of LLM Claims](http://arxiv.org/abs/2610.09553v1)
  <details><summary>📄 Abstract</summary>
  Large language models can triage malware through direct verdicts or behavioral claims scored by an external policy. We present MARS, a malware triage framework, and compare direct classification with single-pass claim scoring using the same evidence collector and identical static evidence bundles for each model. The evaluation covers 1,195 PE and ELF binaries grouped into 1,001 near-duplicate clusters and six language models, with deterministic rules providing a baseline. Direct classification i...
  </details>

- **2026-10-06** — Xingang Guo, Jing Gu, Brian Jang et al. — [Humanity's Sixth Sense: Benchmarking Intuitive Visual Reasoning in Multimodal Models](http://arxiv.org/abs/2610.08966v2)
  <details><summary>📄 Abstract</summary>
  Humans perceive far more in a scene than what is explicitly depicted: a single glance captures past causes and future trajectories; a quick peek determines if a vehicle can fit between two parked cars; a few seconds of video reveals who holds authority in a room; and a fleeting clip highlights subtle abstract patterns like unwritten rules or hidden labels. This capacity reflects a form of humanity's sixth sense: an intuitive reasoning mechanism that recovers implicit information beyond raw senso...
  </details>


### 📂 other
*其他安全相关 / Other Security-Related* — 161 papers

- **2026-10-08** — Jiawei Chi, Shangchen Miao, Zhiyuan Shi et al. — [AgentGarten: Code Worlds for Evolving Agents](http://arxiv.org/abs/2610.12374v1)
  <details><summary>📄 Abstract</summary>
  Interactive virtual worlds allow agents to learn through exploration and interaction. What agents can learn is bounded by the environments they practice in, which must be faithful, with consistent state, rules, and dynamics, and realistic, with observations that follow the real-world visual distributions. Achieving both across diverse worlds remains a bottleneck. We introduce AgentGarten, a framework that couples simulators and game engines with a shared neural renderer to build real-time intera...
  </details>

- **2026-10-08** — Kaisen Yang, Qingle Liu, Kejin Wang et al. — [Can AI Agents Learn Their Way to the Top? Evaluating Heuristic Learning in a Long-Running Game Agent Competition](http://arxiv.org/abs/2610.12341v1)
  <details><summary>📄 Abstract</summary>
  Adversarial games have driven advances from heuristic search to reinforcement learning, yet learning and adapting strategies from limited samples remain challenging. AI agents offer an alternative by turning game experience into revisions of executable policies. Building on heuristic learning (HL), we formalize Adversarial Heuristic Learning (AHL), a paradigm that uses AI agents as learning engines to refine game policies and supporting software while keeping model weights fixed. We introduce AA...
  </details>

- **2026-10-08** — Edward Chen, Yuntao Du — [Poster: A Preliminary Study of LLM Distillation Inference](http://arxiv.org/abs/2610.12137v1)
  <details><summary>📄 Abstract</summary>
  Unauthorized model distillation, in which a model is trained on the outputs of a proprietary large language model (LLM), is a growing threat to model providers. We study distillation inference: determining whether a suspect model was distilled from another model or trained independently. We formulate this problem as a hypothesis test and estimate the behavior expected under each hypothesis by training shadow models: distilled shadow models learn from the teacher's reasoning traces, whereas indep...
  </details>

- **2026-10-08** — Kislay Aditya Oj, Nidhi Jain, Sri Surya Varma Datla et al. — [Generative Adversarial Loops](http://arxiv.org/abs/2610.11458v1)
  <details><summary>📄 Abstract</summary>
  AI research progress can be viewed as the interaction between two processes: benchmark creation and method discovery. Historically, both were driven by human intelligence. However, recent advances in AI have accelerated automated method discovery, while automated benchmark creation has received comparatively less attention. To enable self-advancing systems, we propose Generative Adversarial Loop (GAL), a generator-discriminator framework alternating between two agentic searches: (1) a discrimina...
  </details>

- **2026-10-08** — Zhiwei Xue, Jia Yue Kam, Jinhang Qiu et al. — [Control-Ready Uncertainty for Trajectory Diffusion](http://arxiv.org/abs/2610.12431v1)
  <details><summary>📄 Abstract</summary>
  Diffusion models can represent complex, multimodal trajectory distributions, but extracting uncertainty from them typically requires costly Monte Carlo sampling. This limits their use in real-time control, where robots must rapidly assess risk and maintain safety margins. We introduce Score-Curvature for Online Precision Estimation (SCOPE), a lightweight module that augments diffusion trajectory models with control-ready uncertainty. SCOPE learns a structured precision matrix around each nominal...
  </details>

- **2026-10-08** — Barbara Toniella Corradini, Caterina Gallegati, Ludovica Genovese et al. — [From What to Which: Decoding Modifier Grounding in Frozen MLLMs](http://arxiv.org/abs/2610.12305v1)
  <details><summary>📄 Abstract</summary>
  As Multimodal Large Language Models (MLLMs) can describe increasingly complex visual scenes, token-level grounding becomes crucial. Yet, when an MLLM generates "the yellow banana on the left", established grounding approaches focus on what is in the image ("banana"), overlooking tokens that help describe which instance is meant ("yellow", "left"). In this work, we ask whether frozen MLLM representations contain decodable grounding information about the referred instance across generated tokens, ...
  </details>

- **2026-10-08** — Thomas Gebhart, Russell J. Funk — [SciTBERT: A family of chronologically consistent language models for scientific and technological language processing](http://arxiv.org/abs/2610.12207v1)
  <details><summary>📄 Abstract</summary>
  Pre-trained transformer models are increasingly being used to study scientific and technological progress. Encoders tuned to paper or patent text outperform general-purpose models on downstream classification, regression, and proximity tasks within science and technology. However, the applicability of these models for studying time-dependent or archival properties of science, technology, and their interface is limited due to lookahead and domain biases inherent to these pre-trained models. These...
  </details>

- **2026-10-08** — Ming Chen, Rong-Xi Tan, Ke Xue et al. — [A Closer Look at Agentic BBO: Benchmarking LLM Agents for Black-Box Optimization](http://arxiv.org/abs/2610.12183v1)
  <details><summary>📄 Abstract</summary>
  Black-box optimization (BBO) arises in many scientific and engineering problems where objective evaluations are expensive and limited. Recent large language model (LLM) agents offer a new way to approach BBO by combining task semantics, computation, optimization tools, and feedback-driven decision making, showing great potential due to the integration with mathematically rigorous tools. However, existing agentic BBO studies use different task domains and system configurations, making their resul...
  </details>

- **2026-10-08** — Chenyang Xu, Donglin Xie, Xi Xiang et al. — [PulseBound: Future-Beat State Forecasting Under an Explicit Information Boundary](http://arxiv.org/abs/2610.12010v1)
  <details><summary>📄 Abstract</summary>
  Predictive representation learning from photoplethysmography (PPG) can violate causal information access even with causal attention, as normalization, nonlocal transforms, or companion views may depend on withheld samples. We introduce PulseBound, a PPG representation learner combining physiologically structured future-beat prediction with an explicit stored-window information boundary. A content-independent cutoff separates the visible prefix from the prediction target. Prefix-only normalizatio...
  </details>

- **2026-10-08** — Younghwan Joo, Sung-il Kim — [Narrow and Deep: An Ontology Tower as the Knowledge of an LLM Agent for an Industrial Equipment System](http://arxiv.org/abs/2610.11768v1)
  <details><summary>📄 Abstract</summary>
  Large language model (LLM) agents are beginning to operate industrial energy equipment, and what they get right depends on what they are told about the plant. Established building ontologies name many kinds of points across many sites, whereas an industrial equipment system needs few entities with much knowledge about each. This study proposes the ontology tower, a narrow-and-deep ontology of a single equipment system whose knowledge deepens in two ways: through quantities derived from the measu...
  </details>

- **2026-10-08** — Konstantinos Fotopoulos, Petros Maragos — [Correlational Training of Morphological Neural Networks](http://arxiv.org/abs/2610.11740v1)
  <details><summary>📄 Abstract</summary>
  Neural networks are typically trained using first-order methods and back-propagation. It is unclear whether this approach is optimal for morphological layers whose weight Jacobians are sparse and whose resulting parameter gradients can be poor. In this work, we propose a novel weight update method for morphological neural networks inspired from the Multiplicative Weights Update (MWU) scheme. We view each morphological perceptron as an instance of the learning from experts' advice problem in loga...
  </details>

- **2026-10-08** — Mengnan Jiang, Christian Franke, Michele Franco Adesso et al. — [SubDGuide: A Modeler-Inspired Agentic Workflow for Mesh-to-SubD Reconstruction](http://arxiv.org/abs/2610.11721v1)
  <details><summary>📄 Abstract</summary>
  Subdivision surfaces represent free-form geometry through a sparse control cage, but recovering that cage from a dense mesh is not merely a fitting problem: the system must infer where control is needed, which curves encode design features, and when an initial result should be revised. We present SubDGuide, a modeler-inspired agentic workflow for this task. Stage A reads aligned multiview geometric evidence and produces a compact plan for cage resolution, feature mapping, and broad-form fitting....
  </details>

- **2026-10-08** — Ohad Rubin — [Conditional Transfer from Controlled Pretraining Mixtures to Code](http://arxiv.org/abs/2610.11548v1)
  <details><summary>📄 Abstract</summary>
  Synthetic tasks are increasingly used both as probes of language-model capability and as pretraining data. Both uses are often justified by loss reduction: falling loss is treated as informative, and faster loss reduction with more sampling as evidence that a task is worth sampling. We separate three signals. A task is diagnostic when its loss tracks global pretraining progress; it is teachable when its loss responds to its own token budget; and a data source transfers when including it improves...
  </details>

- **2026-10-08** — Haobo Li, Wenshuo Zhang, Wenxiao Zhao et al. — [RISR: Residual-Informed Scientific Equation Discovery with Large Language Models](http://arxiv.org/abs/2610.11387v1)
  <details><summary>📄 Abstract</summary>
  Symbolic regression combines structural search with numerical fitting, but aggregate fit scores do not describe how the remaining error varies across inputs. We introduce RISR, a residual-informed method that uses these error patterns to guide formula discovery and learn which corrections are worth fitting. A residual encoder compresses aligned inputs, targets, current predictions, and residuals into continuous tokens that condition a language model to propose formulas. For subsequent refinement...
  </details>

- **2026-10-08** — Zidan Wang, Yaqian Li, Xiaokai Zhang et al. — [Rethinking Contrastive Loss in CLIP Post-training: A Complementary Framework with Frozen Text Encoder](http://arxiv.org/abs/2610.11374v1)
  <details><summary>📄 Abstract</summary>
  CLIP serves as a foundational vision-language model and the de facto vision encoder for downstream VLMs such as LLaVA. Post-training offers a lightweight route to refine CLIP, but recent work argues that the standard contrastive loss is unsuitable for post-training due to catastrophic forgetting under small batches, motivating designs that abandon the contrastive objective in favor of distillation. We revisit this premise and find that, for the InfoNCE objective, the reported forgetting is drive...
  </details>

- **2026-10-08** — Meghanadh Pulivarthi, Swaraj Kumar Biswal, Kushagra Bhushan et al. — [RIT-RAG: Navigating Document Corpora with Retrieval-Induced Trees](http://arxiv.org/abs/2610.11370v1)
  <details><summary>📄 Abstract</summary>
  Retrieval-augmented generation (RAG) grounds language models in external corpora. Agentic RAG enables iterative search, yet exposes the model to isolated chunks without document structure, making it difficult to distinguish relevant evidence from chunks that merely resemble the query. Structure-aware methods such as PageIndex navigate document structure but cannot scale to the structures of large corpora, which do not fit in the LLM context. Hence, they first commit to a single document using a ...
  </details>

- **2026-10-08** — Zhengwei Bai, Moreno D'Incà, Danielle Class et al. — [H2CE: Modeling Geo-Semantic Interactions for POI Reranking with Heterogeneous Two-Stage Cross-Encoders](http://arxiv.org/abs/2610.11277v1)
  <details><summary>📄 Abstract</summary>
  Point-of-Interest (POI) reranking in local search must model query-conditioned tradeoffs among lexical semantics, geospatial proximity, and numerical quality signals such as rating and review count, while remaining practical under real-time serving constraints. A close POI may only partially satisfy the query intent, while a farther one may offer stronger semantic and quality evidence. We present H2CE, a Heterogeneous Two-stage Cross-Encoder for latency-bounded POI reranking. H2CE represents num...
  </details>

- **2026-10-08** — Wei-Xiang Mao, Zhi-Kai Chen, De-Chuan Zhan et al. — [TaReD: Tool-Aware Recursive Decomposition for Long-Horizon Tasks](http://arxiv.org/abs/2610.11268v1)
  <details><summary>📄 Abstract</summary>
  Agents combine reasoning with tools to interact with external systems and complete real-world tasks. Early agents typically interleave reasoning and actions along a single execution chain. On complex tasks, this chain becomes unreliable because growing histories obscure intermediate dependencies and allow early planning errors to propagate. Recursively decomposing a complex task into smaller subtasks offers a natural solution, yet effective decomposition must account for the system's capabilitie...
  </details>

- **2026-10-08** — Qirui Wu, Stan Birchfield, Hesam Rabeti et al. — [GATOR: Generative and Agentic 3D Object Reconstruction From Casual Images](http://arxiv.org/abs/2610.11215v1)
  <details><summary>📄 Abstract</summary>
  Reconstructing complete, scene-aligned 3D objects from casual images requires integrating sparse, uncertain observations and inferring surfaces hidden by occlusions. We present GATOR, a generative and agentic framework that recovers textured object assets and their scene-relative pose from one or more images. Our local modality mixer couples patch-aligned RGB, target-mask, and pointmap features before cross-view reasoning, preserving scene context while distinguishing the target from its surroun...
  </details>

- **2026-10-08** — Kim-Cuc Nguyen, Ngai-Man Cheung — [Dissecting Representation Structure in Vision Transformers: A Rigorous Architectural Study](http://arxiv.org/abs/2610.11205v1)
  <details><summary>📄 Abstract</summary>
  Representation structure is crucial for understanding Vision Transformer (ViT) architectures and their generalization behavior. However, prior studies neither isolate nor analyze module-level features nor investigate how their interactions contribute to performance estimation. In this work, we conduct the first rigorous analysis of feature information across diverse architectural scales, empirically uncover the relationship between ViT representation and generalization behavior, and leverage the...
  </details>

- **2026-10-08** — Wenjie Liao, Xiaohui Song, Liangjie Zhao et al. — [SP-DocReader: Difference-Aware Self-Play for Precise Document OCR](http://arxiv.org/abs/2610.11148v1)
  <details><summary>📄 Abstract</summary>
  Accurate page transcription remains difficult for vision language models under limited input and training budgets. We present SP-DocReader, a self-play framework for optical character recognition (OCR) that targets residual errors after supervised fine-tuning. Reading Discrepancy Masking aligns reference and generated model tokens through a longest common subsequence, then scores unmatched positions with their full conditioning prefixes. Focused Fidelity Loss adds direct negative log-likelihood ...
  </details>

- **2026-10-08** — Yuliang Chen, Yu Yvonne Wu, Patrick Langer et al. — [Lapras: Latent Reasoning for Time Series Language Models](http://arxiv.org/abs/2610.11111v1)
  <details><summary>📄 Abstract</summary>
  Time Series Language Models (TSLMs) offer a promising path toward time series understanding by reasoning over temporal signals and producing natural language answers and explanations. A common approach is Chain-of-Thought (CoT), which generates step-by-step rationales linking relevant signal patterns to final answers. Although these models learn from reference CoT traces during post-training, generating faithful descriptions of input time series at inference remains challenging. Expressing high-...
  </details>

- **2026-10-08** — Sota Sugawara, Yukihiko Okada — [FedAlphaEdit: Null-Space-Aligned Merging for Collaborative Knowledge Editing](http://arxiv.org/abs/2610.11033v1)
  <details><summary>📄 Abstract</summary>
  Multiple institutions may each hold their own private knowledge edits and wish to integrate them into a single large language model without sharing raw edit requests. Null-space-constrained editing methods such as AlphaEdit mathematically guarantee that each update leaves unrelated knowledge intact, while collaborative frameworks such as CollabEdit aggregate edits from multiple clients without data sharing. Combining the two appears trivial. However, we show that this naive combination fails str...
  </details>

- **2026-10-08** — Mert Albaba, Jens Beißwenger, Anna Manasyan et al. — [VioLA: Learning Generalist Humanoid Control Policies from Human Data](http://arxiv.org/abs/2610.12435v1)
  <details><summary>📄 Abstract</summary>
  Teaching a humanoid to follow instructions with its whole body runs into two obstacles. Its action space is large and tightly coupled: legs, arms, and fingers must move together while the robot keeps its balance, which makes joint-level actions hard to learn. And humanoid demonstrations are scarce, so current humanoid generalist policies do not follow new instructions out of the box and are fine-tuned on teleoperated demonstrations of each task before deployment. Human demonstrations exist in fa...
  </details>

- **2026-10-08** — Zimo Wen, Yijin Chen, Yuxuan Cao et al. — [RoboRSI: Stable, efficient, and reusable robot self-evolution in complex real-world environments](http://arxiv.org/abs/2610.12424v1)
  <details><summary>📄 Abstract</summary>
  A generalist robot should not only perform diverse tasks but also improve through experience, turning what it learns during execution into capabilities that later tasks can reuse. Robot agents that act through code can already repair programs from execution feedback, yet it remains a central challenge to organize this experience around the task structure that gives it meaning, so that each repair is attributed to the responsible capability, supported by execution evidence, and validated before i...
  </details>

- **2026-10-08** — Minye Wu, Zehao Wang, Tinne Tuytelaars — [Unifying Policy Learning and State Prediction through Spatial Language Modeling](http://arxiv.org/abs/2610.12172v1)
  <details><summary>📄 Abstract</summary>
  Learning how actions change scene geometry can provide complementary supervision for goal-directed manipulation. We introduce Spatial Language Modeling, which represents scene contours, goals, action targets, and future states with a shared vocabulary of discrete coordinates and semantic tokens. A task-specific grammar organizes these elements into spatial sequences, allowing one autoregressive Transformer to learn action generation and action-conditioned state prediction through a common next-t...
  </details>

- **2026-10-08** — Clarisse Wibault, Antoine Gorceix, Antonio Léon Villares et al. — [Q-Shaped Options for Hierarchical Reinforcement Learning](http://arxiv.org/abs/2610.12135v1)
  <details><summary>📄 Abstract</summary>
  Learning to tackle long-horizon, goal-conditioned tasks requires an agent to reason over extended timescales and act across a broad range of states. In principle, Hierarchical Reinforcement Learning (HRL) addresses both challenges through the interaction between action (temporal) and state (spatial) abstraction. First, using an action abstraction to represent temporally extended behaviour as options reduces the effective decision horizon. Second, enabling different state abstractions at each lev...
  </details>

- **2026-10-08** — Jie Fu, Anamika Dubey — [Policy Synthesis for Finite Populations of MDP Agents under Aggregate Reach-Avoid Chance Constraints](http://arxiv.org/abs/2610.12028v1)
  <details><summary>📄 Abstract</summary>
  Consider a finite population of agents with decoupled Markov transition dynamics and empirical-density feedback, subject to the following constraints: with probability at least $1-δ_r$, at least a fraction $α_r$ of agents must reach a target region at some time $t^*$, while, at each time up to $t^*$, the unsafe population fraction must remain below $β_u$ with probability at least $1-δ_u$. However, standard mean-field methods enforce these constraints only in expectation, which fails to account f...
  </details>

- **2026-10-08** — Prince Jha, Nils Lukas, Kun Zhang et al. — [CausalDreamer: Learning Predictive World Models with Latent Disentanglement](http://arxiv.org/abs/2610.12016v1)
  <details><summary>📄 Abstract</summary>
  World models for control must capture which aspects of the environment respond to the agent's actions and which are relevant to reward. Generative world models such as Dreamer 4 consist of a video tokenizer, which encodes each frame into a latent, and a dynamics model, which is pretrained to predict future latents from past latents and actions. Yet the tokenizer is trained with a reconstruction objective, without action or reward supervision, so its latent provides no explicit mechanism to separ...
  </details>

- **2026-10-08** — Houlong Xiong, Zhenqi Qiu, Zechen Wang et al. — [REACT: Rolling Denoising and Dual Decoupling for Reactive Robot Control with VLA Models](http://arxiv.org/abs/2610.12007v1)
  <details><summary>📄 Abstract</summary>
  Flow-based vision-language-action (VLA) models generate action chunks for temporally coherent robot motion, but chunked control creates a fundamental closed-loop trade-off: long chunks provide smooth execution, whereas frequent replanning improves reactivity at the cost of action discontinuities. We introduce REACT, a rolling-denoising framework that makes flow-based VLAs more reactive while preserving long-horizon context. Instead of regenerating entire action chunks from scratch, REACT maintai...
  </details>

- **2026-10-08** — Vinko Sabolčec, Bettina Messmer, Yassine Turki et al. — [Adapting English Quality Classifiers for Multilingual LLM Pretraining Data Selection](http://arxiv.org/abs/2610.11585v1)
  <details><summary>📄 Abstract</summary>
  Recent advances in large language model (LLM) pretraining highlight the role of high-quality training data in improving performance. While model-based filtering has proven effective in selecting high-quality subsets from web-scale corpora, especially for high-resource languages, low-resource languages face challenges due to limited availability of annotated data. This work explores extending quality filtering to over 100 languages by proposing a multilingual adaptation approach that converts an ...
  </details>

- **2026-10-08** — Shuang Luo, Yilun Kong, Yunpeng Qing et al. — [Rewiring Semantics, Dynamics, and Control: A Simple yet Effective Action-Centric Tri-Stream Transformer](http://arxiv.org/abs/2610.11416v1)
  <details><summary>📄 Abstract</summary>
  Vision-Language-Action (VLA) models have emerged as a prominent framework for complex robotic manipulation, building on the strong semantic understanding of pretrained Vision-Language Models (VLMs). However, such VLM backbones offer insufficient physical dynamics priors, which limits the generalization capabilities of robot policies. Recent efforts therefore integrate video-generation World Models (WMs) into robot policies through various strategies, using predictive dynamics to facilitate actio...
  </details>

- **2026-10-08** — Kai Ding, Yang He, Ruijie Quan et al. — [WAM-Cache: Staleness-Bounded KV Reuse for Efficient World Action Models](http://arxiv.org/abs/2610.11401v1)
  <details><summary>📄 Abstract</summary>
  World Action Models (WAMs) enable generalist robot manipulation by conditioning an action expert on representations from a pretrained video Diffusion Transformer (DiT). In closed-loop control, the video DiT runs at every chunk to encode the current observation into layerwise key-value (KV) pairs that the action expert queries. This prefill dominates the per-chunk computational cost, yet existing training-free accelerations leave it fully dense. We present WAM-Cache, a training-free framework tha...
  </details>

- **2026-10-08** — Lucas Florin, Amelie Knecht, Ulysse Schaller et al. — [Deception by Omission: Language Models Knowingly Hide Their Mistakes](http://arxiv.org/abs/2610.11351v1)
  <details><summary>📄 Abstract</summary>
  Large language models (LLMs) increasingly act as agents with little human oversight, so potential mistakes they make can go unnoticed. Users then depend on the model to report what went wrong. An honest model discloses its mistakes, while a deceptive one conceals them. However, it is unclear how current LLMs behave in such situations. In this study, we prefill LLM trajectories with synthetic mistakes. The trajectories resemble real deployments in chat and agentic settings. Models fail to disclos...
  </details>

- **2026-10-08** — Chuanrui Zhang, Zaijia Yang, Duomin Wang et al. — [USDCraft: Geometrically Grounded Programmatic Modeling of Articulated 3D Assets for Simulation](http://arxiv.org/abs/2610.11322v1)
  <details><summary>📄 Abstract</summary>
  Geometrically faithful and functional articulated 3D assets are essential for real-to-sim robot manipulation, where policies trained in simulation must transfer to physical objects. Recent mesh-based methods learn to infer articulation from annotated 3D assets, but deployment remains challenging when real-world objects fall outside the training distribution or their meshes are incomplete or corrupted. To address these limitations, we formulate articulated asset reconstruction as programmatic mod...
  </details>

- **2026-10-08** — Kyoungin Baik, Youngwoon Lee — [SimVLA: Zero-Shot Sim-to-Real VLA Learning for Mobile Manipulation](http://arxiv.org/abs/2610.11248v1)
  <details><summary>📄 Abstract</summary>
  Large-scale, diverse datasets have driven the success of LLMs and VLMs. But VLAs for robotics remain limited by the cost and complexity of real-world data collection. While simulation offers a scalable alternative, its potential for sim-to-real VLA learning in mobile manipulation remains largely underexplored. We introduce SimVLA, an end-to-end framework that trains VLAs entirely on synthetic simulation data without teleoperation for mobile manipulation. SimVLA is first pre-trained on two comple...
  </details>

- **2026-10-08** — Krithik Vishwanath, Haitong Lin, Anton Alyakin et al. — [Clinician use of language models diverges from how the models are evaluated](http://arxiv.org/abs/2610.11069v1)
  <details><summary>📄 Abstract</summary>
  Large language model (LLM) assistants are being deployed to clinicians across health systems, and judgments about their readiness rest largely on benchmark scores, most of them derived from examination questions or curated cases. A benchmark predicts performance in deployment only to the extent that its items resemble real use, yet whether benchmarks reflect the work these systems receive has rarely been measured. Here we analyze 127,833 queries sent by 6,342 physicians, advanced practice provid...
  </details>

- **2026-10-08** — Saeefa Rubaiyet Nowmi, Md Mahmuduzzaman Kamol, Mohammad Saidur Rahman — [Toward Joint Optimization of Circuit Depth and Training Data Size in Adaptively Grown Quantum Classifiers](http://arxiv.org/abs/2610.12428v1)
  <details><summary>📄 Abstract</summary>
  Building a quantum model involves a tradeoff: how complex the circuit should be, and how much training data it needs. Caro et al. show that models with fewer trainable gates need less training data to generalize well. Q-FLAIR shows that a quantum feature-map circuit can be grown gate-by-gate, stopping once further growth stops improving the training loss. We ask whether these two results combine into a predictable scaling law. Does Q-FLAIR's own stopping rule pick larger or smaller circuits as t...
  </details>

- **2026-10-08** — Weiying Hou, Xie Zhang, Chenshu Wu — [OctoSense: Building a Unified Ecosystem for Open-Source Wireless Sensing](http://arxiv.org/abs/2610.12405v1)
  <details><summary>📄 Abstract</summary>
  As AI enters the physical world, wireless sensing has emerged as a key modality for enabling non-intrusive physical intelligence. However, unlike the mature ecosystems of vision and language models, wireless sensing research remains highly fragmented. The field faces a growing "reproducibility wall" caused by heterogeneous data formats, non-interoperable processing pipelines, and the lack of standardized benchmarks. To dismantle this barrier, we present OctoSense, a unified platform designed to ...
  </details>

- **2026-10-08** — Gokul Puthumanaillam, Tao Sun, Elie Aljalbout et al. — [ARC: A Reasoning Recipe for Robot Foundation Models](http://arxiv.org/abs/2610.12386v1)
  <details><summary>📄 Abstract</summary>
  The prevailing approach to improving robot foundation models (RFMs) relies on larger models, more robot demonstrations, and costly training at scale. We show that there exists an effective and efficient complementary approach: the right reasoning recipe can substantially improve the zero-shot task performance of existing state-of-the-art RFMs. We refer to this recipe as ARC. It consists of three key ingredients: a reasoning trace, a scalable automatic labeling pipeline, and a strategy for adapti...
  </details>

- **2026-10-08** — Pratik Dutta, Matthew B. Obusan, Max Chao et al. — [Unlocking the Regulatory Genome by ARGUS: An Evidence-Constrained Agentic Framework for Interpreting Single Nucleotide Variants](http://arxiv.org/abs/2610.12281v1)
  <details><summary>📄 Abstract</summary>
  Over 90% of disease-associated variants from genome-wide association studies fall in noncoding regulatory regions, yet their functional interpretation remains a central open problem in genomic medicine. Large language models prompted to interpret such variants routinely hallucinate transcription factor (TF) binding changes, fabricate experimental support, and assign biological significance to statistically negligible signals. We present ARGUS (Agentic Regulatory Genomics for an Uncertainty-aware...
  </details>

- **2026-10-08** — Jinjing Zhao, Fangyun Wei, Yitong Wang et al. — [VibeEdit: Image Editing with Canvas Instructions](http://arxiv.org/abs/2610.12229v1)
  <details><summary>📄 Abstract</summary>
  In text-guided image editing, describing the desired change is often straightforward, but identifying the intended object or region can be cumbersome, especially when several objects look alike. We introduce a new image editing interface that lets users place spatial marks and optional short notes directly on the image. Together, these annotations form a canvas instruction that specifies where to edit and what to change. Our editor, VibeEdit, follows these instructions to perform object addition...
  </details>

- **2026-10-08** — Yudi Zhang, Mingyu Cao, Lu Yin et al. — [DataSense-Bench: The First Step Toward an AI Scientist](http://arxiv.org/abs/2610.12190v1)
  <details><summary>📄 Abstract</summary>
  As claims about recursive self-improvement (RSI) and artificial general intelligence (AGI) proliferate, we ask a simple question: do frontier AI models have a sense of data, i.e., can they reliably select the right data for training? We introduce DataSense-Bench to study this capability through the fundamental problem of data selection and performance forecasting in machine learning. We ask AI agents to select and rank candidate training subsets that can be used to fine-tune a small LLM model. A...
  </details>

- **2026-10-08** — Xinliang Xiao, Bowen Yang, Wenjing Zhang et al. — [Instance-anchored interaction evidence: Grounding robot plans in human pointing and handling](http://arxiv.org/abs/2610.12157v1)
  <details><summary>📄 Abstract</summary>
  A robot that assists people must often act on what a person has shown rather than said: which of several identical cartons was pointed at, or which box was handled. The plan is executed from the final scene, whereas the evidence occurs earlier, possibly on objects that have since moved. We propose instance-anchored interaction evidence (IAE), which registers every object of the final scene to its public identifier, keeps each identity through the video by backward mask propagation, and describes...
  </details>

- **2026-10-08** — Jinkai Zhang, Jingyi Xu, Yuanhong Yu et al. — [SuperNav: An Agentic Navigation System for Any Task in Any Scene](http://arxiv.org/abs/2610.12126v1)
  <details><summary>📄 Abstract</summary>
  General-purpose service robots need navigation systems that can handle diverse human requests in unfamiliar environments, combining task generality with scene generality. Some existing methods fine-tune multimodal large language models (MLLMs) to predict navigation actions, making their behavior dependent on the coverage of navigation training data and potentially limiting generalization to new requests and environments. Our key insight is to let the MLLM focus on interpreting requests, understa...
  </details>

- **2026-10-08** — Zhanyi Lu, Huan Wang — [Universal Textual Teaching for LLMs](http://arxiv.org/abs/2610.12114v1)
  <details><summary>📄 Abstract</summary>
  Knowledge distillation (KD) transfers knowledge from stronger Teacher models to weaker Student models, but most methods require training the Student parameters, thereby binding the distilled knowledge to a specific architecture and checkpoint. This implicit representation is difficult to interpret or reuse across models and limits KD for API-only or costly-to-train models. This paper studies knowledge transfer for large language models (LLMs). We introduce Universal Textual Teaching (UTT), a par...
  </details>

- **2026-10-08** — Han Tu, Hang Zhao, Qi Gao — [On the relationships between pressure geometrization and vortex identification](http://arxiv.org/abs/2610.11980v1)
  <details><summary>📄 Abstract</summary>
  The profound mathematical and conceptual analogy between pressure in fluid mechanics and gravity in general relativity motivates a novel geometric reinterpretation of flows. This article proposes a theoretical framework for geometrizing pressure by establishing a Newton-Cartan geometry and applying a conformal transformation to the spatial metric. The pressure field is reinterpreted as a geometric potential that induces an effective spatial curvature, encoded in the Ricci tensor Rij and the asso...
  </details>

- **2026-10-08** — Gaetano Tedesco, Alex Markham — [Score-Based Learning of Cluster DAGs from Interventions](http://arxiv.org/abs/2610.11947v1)
  <details><summary>📄 Abstract</summary>
  Graphical approaches to causal abstraction transform a low-level causal directed acyclic graph (DAG) over many measured variables into a smaller, high-level DAG whose nodes cluster the original variables and whose edges summarize the causal relations between clusters. Such cluster DAGs are easier to interpret, but learning them requires finding the clusters and recovering the edges between them. Madaleno et al. (2026) learn the interventional coarsening (the cluster DAG that merges variables the...
  </details>

- **2026-10-08** — Aaron Dsouza, Mohammed Azeez Khan, Ashutosh Mishra et al. — [Automated Assembly Instruction Generation from CAD Models Using Grounded Large Language Models: A Human-in-the-Loop Framework](http://arxiv.org/abs/2610.11896v1)
  <details><summary>📄 Abstract</summary>
  Assembly documentation is a downstream manufacturing artifact that is still usually authored by interpreting CAD models by hand. Structured product data and large language models are both available, yet studies of CAD interpretation, assembly sequence planning, instruction writing, and human oversight have largely proceeded separately. This paper formulates CAD-grounded assembly instruction generation: the production of natural-language assembly procedures constrained by structured engineering i...
  </details>

- **2026-10-08** — Pierre Gentine, Dhruv Balwada, Aytaç Paçal et al. — [legoESM: a modular, differentiable, multiscale, AI-ready Earth system model built with AI agents](http://arxiv.org/abs/2610.11883v1)
  <details><summary>📄 Abstract</summary>
  Earth system models (ESMs) have grown tremendously in realism, yet key uncertainties persist in the climate response to greenhouse-gas forcing, particularly due to cloud radiative feedbacks. In addition, their software architecture was not designed for accelerator hardware or modern artificial intelligence (AI). Here we present legoESM, a composable, differentiable, multiscale ESM written in JAX. It builds on decades of community-developed parameterizations and numerical methods, recast in a uni...
  </details>

- **2026-10-08** — Haoyu Zhao, Zhengxu Yu, Zhiyuan He et al. — [Memento 3: Model-Based Recursive Self-Improvement through Reflective Rulebooks](http://arxiv.org/abs/2610.11794v1)
  <details><summary>📄 Abstract</summary>
  Learning to act in unfamiliar environments requires agents to infer how the world works and revise that understanding as new evidence arrives. Yet limited observations can support multiple world models that explain past interactions but predict different outcomes in unseen states. We introduce Memento 3, building on the Memento series to enable frozen LLM agents to continually learn explicit world models through external memory. The agent maintains a natural-language rulebook as persistent seman...
  </details>

- **2026-10-08** — Lingsen You, Yujun Guo, Xinyu Zhong et al. — [Intervention anchors and scientific verification in synthetic vascular predictive representations](http://arxiv.org/abs/2610.11704v1)
  <details><summary>📄 Abstract</summary>
  Complete orthogonal predictive coordinates do not by themselves bind a latent direction to a named intervention. We present a mathematical and synthetic audit motivated by vascular device-vessel suitcordance. Capacity-matched least-squares predictors were exactly equivalent under complete fixed output transforms, whereas an anchor-only observer recovered interpretations only within the span of known perturbation signatures. Six three-dimensional configurations across 64 seeds gave a maximum pair...
  </details>

- **2026-10-08** — Saverio Cavasin, Pietro Tedeschi, Mattia Tamiazzo et al. — [VESSI - VLM-Enhanced Support for Surveillance and Investigations](http://arxiv.org/abs/2610.11674v1)
  <details><summary>📄 Abstract</summary>
  Automated video surveillance analysis has become a critical component of intelligence infrastructures and Law Enforcement agencies. Traditional systems lack the semantic module for comprehensive situational awareness and forensic tasks, limiting their ability to interpret events meaningfully or support post-incident investigations. This slows operational insight and increases the burden on human analysts. Recent advances in Vision-Language Models (VLMs) offer promising pathways to bridge this ga...
  </details>

- **2026-10-08** — Milán Zsolt Bagladi, László Gulyás — [Neural Networks for Temporal Pattern Recognition and Dynamic Arm Gesture Speed Estimation for Robot Control](http://arxiv.org/abs/2610.11631v1)
  <details><summary>📄 Abstract</summary>
  Deploying intelligent robotic systems that interact with humans through gestures requires neural networks capable of recognizing diverse temporal patterns. We present a systematic benchmark of ten abstract sequential tasks--five permutation-invariant (set) and five order-dependent (sequence) problems--evaluated across eighteen neural network architectures spanning recurrent, convolutional, attention-based, and set-function families. Beyond the core architecture-task grid, we explore numerous pre...
  </details>

- **2026-10-08** — Adonis Jamal, Samy Mekkaoui, Yadh Hafsi et al. — [Randomized Transport Maps for Model-Free Policy-Gradient Mean-Field Control](http://arxiv.org/abs/2610.11619v1)
  <details><summary>📄 Abstract</summary>
  We develop a model-free policy gradient method for discrete-time mean-field control (MFC). In MFC, the policy affects the objective both through the controlled dynamics and through the population distribution. Standard REINFORCE estimators capture the first effect but not the second. We introduce Transport REINFORCE, a transport map-based approach that perturbs a suitable transformation of the population distribution to estimate this missing mean-field contribution. The method applies to both fi...
  </details>

- **2026-10-08** — Jiawei Li, Fang Liu, Wei Zhang et al. — [Sera: Semantic Representation Aggregation for Reliable and Interpretable Battery Health Forecasting](http://arxiv.org/abs/2610.11567v1)
  <details><summary>📄 Abstract</summary>
  Battery state of health (SoH) forecasting is important for battery management, but remains challenging due to nonlinear degradation and heterogeneity across batteries. Existing data-driven approaches primarily use temporal models to learn from numerical battery time series, and higher-level degradation characteristics are often not explicitly represented. These characteristics, however, can provide degradation guidance to support reliable forecasting and make the influence of degradation more in...
  </details>

- **2026-10-08** — Zifei Wang, Wei Wen, Qiang Ji et al. — [EVIE: Evidence-Vector-Informed Embeddings for Visual Document Retrieval](http://arxiv.org/abs/2610.11553v1)
  <details><summary>📄 Abstract</summary>
  Accurate and scalable visual document retrieval (VDR) requires both fine-grained page understanding and efficient indexing, yet existing approaches struggle to achieve both. OCR-based text retrieval adds preprocessing latency and can lose visual and structural cues needed to understand complex pages. Single-vector vision-language models bypass OCR, but compressing an entire page into one vector limits the granularity of query--document matching. Multi-vector retrievers with MaxSim provide finer ...
  </details>

- **2026-10-08** — Abdu Sallouh, Nicholas Popovič, Michael Färber — [Does Modern Standard Arabic (MSA) Dominate Arabic Dialects in LLMs? A Representation-Level Analysis](http://arxiv.org/abs/2610.11510v1)
  <details><summary>📄 Abstract</summary>
  Large language models (LLMs) often default to Modern Standard Arabic (MSA) when generating Arabic, even when prompted with dialectal Arabic. A natural explanation is that their internal representations are dominated by MSA. We test this hypothesis by adapting the language-dominance framework of Shani and Basirat (2025) (https://doi.org/10.18653/v1/2025.blackboxnlp-1.7) to 26 Arabic varieties. Across layers and model families, we find no evidence that MSA acts as a dominant internal representatio...
  </details>

- **2026-10-08** — Leikun Liang, Guoshuai Wang, Xingsheng He et al. — [Beyond Sequences: Distilling Structured Decision Memory for LLM Recommendation](http://arxiv.org/abs/2610.11501v1)
  <details><summary>📄 Abstract</summary>
  Despite the adoption of large language models (LLMs) in recommendation systems, prevailing approaches mostly model single-type behaviors (e.g., views or purchases). Even when incorporating multiple behaviors, existing methods flatten heterogeneous actions into homogeneous token sequences, ignoring their distinct decision-making roles. This flattening fails to capture semantic hierarchies and contextual nuances in complex decision-making, such as trade-offs between price and quality. Consequently...
  </details>

- **2026-10-08** — Kyeong-Rae Kim, Sungnyun Kim, Tae-Hyun Oh — [FloorSAV: Elucidating Spatial Audio-Visual Context with 2D Floormap for AV-LLMs](http://arxiv.org/abs/2610.11310v1)
  <details><summary>📄 Abstract</summary>
  While 3D spatial reasoning in dynamic egocentric environments is crucial for embodied intelligence, audio-visual large language models (AV-LLMs) lack explicit mechanisms to process and internalize global geometry directly from raw sensory streams. Existing approaches either require costly fine-tuning or underutilize the model's cross-modal reasoning capacities. In this paper, we propose FloorSAV, a novel framework that explicitly grounds spatial audio-visual context by rendering a dynamic 2D flo...
  </details>

- **2026-10-08** — Wen Yan, Ligen Shi, Jun Qiu et al. — [Spatial-Frequency-Aware Implicit Neural Representation of Multidimensional Signals via MLP-KAN Fusion](http://arxiv.org/abs/2610.11296v1)
  <details><summary>📄 Abstract</summary>
  Implicit Neural Representations (INRs) have emerged as a compelling paradigm for modeling multidimensional signals by mapping continuous coordinates to signal values. However, Multi-Layer Perceptrons (MLP)-based INRs inherently suffer from spectral bias, which favors low-frequency components and suppresses the reconstruction of essential high-frequency details. While existing techniques, such as Fourier feature mappings, mitigate this issue, they often rely on sensitive manual tuning and are pro...
  </details>

- **2026-10-08** — Toufik Mansour, Olivia Nabawanda, Mark Shattuck — [Distinct flattened partitions avoiding a pattern of length four](http://arxiv.org/abs/2610.11271v1)
  <details><summary>📄 Abstract</summary>
  Let $\mathcal{P}_n$ denote the set of distinct permutations of length $n$ that arise from the flattening process applied to the partitions of $[n]=\{1,\ldots,n\}$. In this paper, we consider the problem of avoidance of a single classical pattern of length four by members of $\mathcal{P}_n$. Let $p_n(τ)$ denote the number of members of $\mathcal{P}_n$ that avoid the pattern $τ$. We show that $p_n(τ)=C_{n-1}$ for all $n \geq 1$ for seven patterns of length four yielding new combinatorial interpret...
  </details>

- **2026-10-08** — Unggi Lee, Haeun Park — [Can a System-One LLM Perform Knowledge Tracing When Few or No Learners Are Logged?](http://arxiv.org/abs/2610.11135v1)
  <details><summary>📄 Abstract</summary>
  Knowledge tracing (KT) models need many logged learners, so a new course or platform starts without a usable model. In LLM-based KT the LLM generates the answer, which we call System-Two; it is either fine-tuned on the target data or reasons and votes over ten samples, which is slow and gives coarse probabilities. We ask whether an off-the-shelf System-One LLM, which returns a probability for a typed question directly in a single pass, can perform KT when few or no learners are logged. On seven ...
  </details>

- **2026-10-08** — Jiahao Zhang, Pengbin Feng, Chunlei Meng et al. — [BayesJudge: Uncertainty-Aware Bayesian Meta-Evaluation of Human and LLM Judgments](http://arxiv.org/abs/2610.11116v1)
  <details><summary>📄 Abstract</summary>
  AI evaluation pipelines often produce conflicting judgments rather than clean labels. In pairwise LLM evaluation, this conflict is especially visible: disagreement can arise from ambiguous items, underspecified rubrics, heterogeneous or unstable human raters, or an LLM judge whose verdict changes when the response order is swapped. We propose BayesJudge, an online Bayesian meta-evaluation layer for conflicting human-LLM judgment streams. For each comparison, BayesJudge estimates a panel-relative...
  </details>

- **2026-10-08** — Jordan Prescott, Aditya Kommineni, Tiantian Feng et al. — [Towards Automated Clinical Behavioral Coding with Large Language Models: A Case study Using BOSCC recordings of Children](http://arxiv.org/abs/2610.11106v1)
  <details><summary>📄 Abstract</summary>
  Autism spectrum disorder (ASD) is a neurodevelopmental condition characterized by differences in social communication and by restricted interests and repetitive behaviors. Treatment interventions often target social-communication skills, creating a need for reliable measures of behavioral change. The Brief Observation of Social Communication Change (BOSCC) is a validated treatment-response measure based on brief play and social-communication interactions between a child and trained examiner. The...
  </details>

- **2026-10-08** — Zirui Peng, Yizhou Liu, Ziming Liu et al. — [Emergent Inverse-Depth Scaling From Nonlinearity In Attention](http://arxiv.org/abs/2610.11063v1)
  <details><summary>📄 Abstract</summary>
  Scaling laws describe power-law improvements in model performance with dataset size and parameter count, yet their underlying mechanisms are not fully understood. To explain the parameter count scaling, existing theory posits power-law scaling with model depth. In linear-attention models, this scaling is tied to a power-law data spectrum: unable to selectively attend to relevant tokens, these models learn according to global spectral strength, with stronger directions learned before weaker ones....
  </details>

- **2026-10-08** — Koya Sakamoto, Daichi Azuma, Shuhei Kurita et al. — [Rendering-Free Lookahead for Question-Guided Active Vision](http://arxiv.org/abs/2610.11039v1)
  <details><summary>📄 Abstract</summary>
  Active robot vision requires controlling the camera to reveal task-relevant information that is hidden from the current viewpoint. For example, determining what is inside a box may require raising the camera and looking down into it. For viewpoint-dependent question answering, the challenge is to select camera motions that expose the visual evidence needed to answer the question. Although vision-language models (VLMs) can interpret observed images, selecting such motions requires anticipating th...
  </details>

- **2026-10-07** — Farhoud Jafari Kaleibar, Amr M. Zaki, Marin Litoiu — [Adaptive Multi-Discriminator WGAN Framework for Resource-Constrained Internet of Vehicles Using Reinforcement Learning and Game Theory](http://arxiv.org/abs/2610.10926v1)
  <details><summary>📄 Abstract</summary>
  Managing machine learning workloads as a network service introduces a resource-orchestration problem distinct from conventional model training; which nodes should be allocated to a task, how communication and computation budgets should be divided among them, and how service quality should be sustained as connectivity and node availability change with mobility. Deploying Generative Adversarial Networks (GANs) in Internet of Vehicles (IoV) environments is a demanding instance of this problem; reso...
  </details>

- **2026-10-07** — Saimon Amanuel Tsegai, Alex Kantchelian,  Danfeng et al. — [From Investigation Failures to Reliable SOC Agents: Understanding and Improving LLM-Based Alert Triage](http://arxiv.org/abs/2610.10608v1)
  <details><summary>📄 Abstract</summary>
  Security operations centers (SOCs) must triage large volumes of alerts, most of which are benign, while missed attacks can remain uninvestigated. Tool-using large language model (LLM) agents can retrieve evidence during triage, but it remains unclear how reasoning strategies determine what to gather and when an investigation is sufficient to close an alert. We study five representative approaches spanning single-pass tool use, iterative retrieval, sampled investigations, self-review, and explici...
  </details>

- **2026-10-07** — Riqiang Wang, Elena Khasanova, Harsh Saini et al. — [Prompts versus Rules: Auditing and Controlling Speech Naturalness Behaviors in Voice User Simulators](http://arxiv.org/abs/2610.11015v1)
  <details><summary>📄 Abstract</summary>
  As voice agents gain more popularity commercially, the user simulators used to evaluate the deployed agents are also being developed to include more realistic, variable, and diverse speech naturalness behaviors -- disfluency, interruption and backchanneling. The quality of the user simulator directly affects the validity of agent evaluation results. However, we find that most studies so far have not examined in detail whether the intended configuration for these behaviors is realized in the simu...
  </details>

- **2026-10-07** — Hong Huang, Chenhongyi Yang, Junzhe Sun et al. — [Omni-Diffusion-Distill: Few-Step Distillation of Unified Multimodal Diffusion Large Language Models](http://arxiv.org/abs/2610.10990v1)
  <details><summary>📄 Abstract</summary>
  Unified multimodal diffusion large language models (dLLMs) offer a single architecture for both image generation and multimodal understanding, but their iterative decoding requires tens to hundreds of forward passes. Existing few-step distillation methods largely focus on either image generation or text generation, making it unclear how to compress a fully discrete multimodal dLLM into a single efficient student while preserving both generation and understanding. We introduce Omni-Diffusion-Dist...
  </details>

- **2026-10-07** — João Coelho, Hong Wang, Jie Yuan et al. — [Learning Multi-Step Query Rewriting via Corpus Feedback for Conversational Search](http://arxiv.org/abs/2610.10955v1)
  <details><summary>📄 Abstract</summary>
  Conversational Query Rewriting (CQR) turns a context dependent user turn into a standalone query for a retriever, and most methods do this in a single step from the dialogue history before retrieving once. The rewrite is therefore fixed before any corpus evidence is available to correct its reference resolution or its vocabulary. We recast CQR as a sequential retrieval problem: an agent rewrites the current turn, retrieves, and conditions its next rewrite on the returned passages. The agent acts...
  </details>

- **2026-10-07** — Zihao Sheng, Pei Li, Zilin Huang et al. — [Large Language Model-Assisted Preparation of Transportation Management Plans: A Case Study with WisDOT WisTMP System](http://arxiv.org/abs/2610.10650v1)
  <details><summary>📄 Abstract</summary>
  Work zones are critical yet hazardous components of transportation infrastructure, requiring carefully designed Transportation Management Plans (TMPs) to ensure safety and mobility. However, TMP preparation remains labor-intensive and heavily dependent on practitioner expertise. This paper proposes a Large Language Model (LLM)-assisted framework to automate TMP content generation, leveraging the WisDOT WisTMP system as the application context. The framework fine-tunes multiple open-source LLMs a...
  </details>

- **2026-10-07** — Xi Chen, Zhe Liu, Xiaogang Xu et al. — [Speaking the Navigator's Language: Trajectory-Grounded Instruction Translation for Frozen Aerial VLN Agents](http://arxiv.org/abs/2610.10635v1)
  <details><summary>📄 Abstract</summary>
  Aerial vision-and-language navigation (VLN) agents are typically trained on detail-rich, trajectory-aligned commands, whereas users issue short, intent-driven instructions; on a frozen OpenFly navigator, this \emph{instruction gap} drops success rate (SR) from $31.03\%$ to $11.33\%$. To scale translator training, we prompt a language model with human-written style examples to convert original commands into paired, intent-centered Weak commands, which yield $15.27\%$ SR. We introduce the \textbf{...
  </details>

- **2026-10-07** — Zihan Guo, Roxy He, Junwei Quan — [Before Bringing It Up: When and How AI Companions Should Use Memory](http://arxiv.org/abs/2610.09470v2)
  <details><summary>📄 Abstract</summary>
  Memory can sustain AI companionship, yet even accurate recollection can be inappropriate to use. Two rounds of formative interviews with 14 users (n = 6 exploratory, n = 8 memory-focused) motivate asking what a companion should consider before using past information. Eight themes inform Reconsider, a single-call procedure with five checks and four handling modes, evaluated on 80 scenarios across five models over 400 blinded within-model pairs. Two LLM judges favored Reconsider by net margins of ...
  </details>

- **2026-10-07** — Zexuan Liu, Yuning Yang, Tiancheng Zhao — [Curating Always-Loaded Context for LLM Agents: A Capacitated Assortment Model with Censored Feedback](http://arxiv.org/abs/2610.11007v1)
  <details><summary>📄 Abstract</summary>
  At the start of every session, LLM agents load a fixed context file, such as $\texttt{AGENTS.md}$. Each loaded token in the file is charged again in every later round of the session, and these files can degrade performance as they grow in size. However, in practice, human or automated curators usually grow these files by appending.   We formulate context curation as a capacitated assortment problem. Instructions consume tokens under a finite attention capacity; adding an instruction never raises...
  </details>

- **2026-10-07** — Daksh Raghuvanshi, Ved Vedere, Yifan Wang — [StoreBench: A Live-Commerce Environment for Evaluating and Training Autonomous Operator Agents](http://arxiv.org/abs/2610.10942v1)
  <details><summary>📄 Abstract</summary>
  Reinforcement learning environments are now a primary lever for improving large language model (LLM) capabilities in post-training, yet most agentic benchmarks remain static: the world moves only when the agent acts, the reward is a terminal verdict, and the pass bar is set arbitrarily. We introduce StoreBench, a live-commerce environment in which an agent runs a mid-size online apparel store on a production-grade commerce backend, testing long-horizon planning and economic judgment under uncert...
  </details>

- **2026-10-07** — Yanjiang Guo, Haodong Yan, Zhide Zhong et al. — [Video Prediction Policy 2: Predict Better, Act Better](http://arxiv.org/abs/2610.10270v2)
  <details><summary>📄 Abstract</summary>
  World action models (WAMs) have emerged as an important class of generalist robot policies, aiming to transfer video prediction priors to action learning. However, we find that existing WAMs frequently produce incorrect motion predictions in open-ended environment, leading to erroneous actions. We attribute this limitation to two factors: (1) base video models are not optimized for manipulation, and (2) naively incorporating action components into video models can substantially degrade their gen...
  </details>

- **2026-10-07** — Shuangjie Yao, Hao Wang, Koushik Sen et al. — [TestJack: Should you trust the results in coding benchmarks? Agentic Coding Benchmarks Auditing via Evaluator Evolution](http://arxiv.org/abs/2610.10619v1)
  <details><summary>📄 Abstract</summary>
  Large language model (LLM) agents are rapidly reshaping software engineering, accompanied by an explosion of new code benchmarks. Yet nearly all existing benchmarks still rely on the same decades-old criterion: a solution is correct if it passes a fixed set of unit tests. Such tests are often insufficient: they check only part of what the task requires, so agents can reward hack them or silently miss required behavior while still passing every test. As a result, higher benchmark scores may partl...
  </details>

- **2026-10-07** — Bokyung Kim, Amama Mahmood, Honghao Zhao et al. — [Guided Reflection for Personal Sleep Insight in Everyday Sleep Tracking](http://arxiv.org/abs/2610.10822v1)
  <details><summary>📄 Abstract</summary>
  Digital sleep technologies make tracking accessible, yet users often struggle to interpret what changes in their sleep mean. Behavioral sleep medicine addresses this through guided discovery, helping patients develop personal interpretations rather than simply receiving explanations. To bring this to everyday tracking, we present DREAM, an LLM-powered voice assistant that monitors conversational sleep diaries, selectively invites users to interpret meaningful changes, and uses their interpretati...
  </details>

- **2026-10-07** — Bastien Carreres, David Benisty, Jenny Wagner et al. — [Debiasing Local Cluster Infall Reveals $\boldsymbol{H_0}$: Application to the Virgo Cluster](http://arxiv.org/abs/2610.10779v1)
  <details><summary>📄 Abstract</summary>
  Galaxy recession velocities are commonly used to measure the Hubble constant, $H_0$, with peculiar velocities treated as random noise. Around massive clusters, however, these motions can be predicted by the gravitational potential of the central halo, allowing them to be modeled rather than averaged over. Past analyses relied on analytic approximations for the distance-infall-velocity relation, whose accuracy has not been tested using realistic cosmological simulations. We use halos from the Ill...
  </details>

- **2026-10-07** — Mikhail L. Arbuzov, Karan Dave, Evgeniya Dontsova et al. — [Clarify, Then Focus: Statement Normalization for Conversation Analytics at Scale](http://arxiv.org/abs/2610.10758v1)
  <details><summary>📄 Abstract</summary>
  Enterprise conversation analytics asks many questions of millions of interactions. Each question can require reconstructing what people mean and identifying which information matters, repeating costly interpretive work across the same transcripts. We propose a simple principle: clarify the text, then focus the reader. Statement normalization transforms dialogue into short, speaker-attributed statements with source references and semantic tags. The statements make meaning more explicit; the tags ...
  </details>

- **2026-10-07** — Pooneh Mousavi, Mirco Ravanelli, Cem Subakan — [Listen-to-Reason: Listen with Experts, Retrieve over a Graph, Reason with LLMs](http://arxiv.org/abs/2610.10749v1)
  <details><summary>📄 Abstract</summary>
  Large audio-language models (LALMs) fuse an audio encoder into a large language model (LLM) through multi-stage training. This coupling means that a new domain or a stronger LLM requires retraining, and their answers cannot be traced to what the model heard: a chain-of-thought is a post-hoc account. We propose Listen-to-Reason (L2R), an interpretable-by-design pipeline that passes audio to the LLM through an explicit, human-readable tree: small heads on frozen expert encoders map each chunk of a...
  </details>

- **2026-10-07** — Mingqing Yuan, Xiaobo Liang, Junwei Yang et al. — [Judging in Latent Space: Efficient Generative Reward Modeling via Semantics-Preserving Compression](http://arxiv.org/abs/2610.09788v2)
  <details><summary>📄 Abstract</summary>
  Reward modeling often requires jointly representing and reasoning over multiple evaluation criteria, yet verbalizing this process token by token can incur substantial inference cost. Recent work on latent reasoning suggests that continuous states may support this computation more compactly. We introduce LatentGRM, a latent evaluation framework built on semantic chunking, compression, and reconstruction. By using the structure of rubric-guided evaluations to guide compression, LatentGRM learns co...
  </details>

- **2026-10-07** — Takahiro Ezaki, Naoto Imura, Katsuhiro Nishinari — [Shared and structured inputs undermine collective random choice by reasoning AI agents](http://arxiv.org/abs/2610.09667v1)
  <details><summary>📄 Abstract</summary>
  Random selection is widely used in resource allocation and auditing, making reliable implementation essential for AI-agent systems. Behavioural tests across six reasoning models uncovered threshold and divisibility rules used in identifier-based choices. For threshold-following GPT-6 Sol and Gemini 3.8 Flash, single-agent measurements prospectively predicted correlated participation under shared identifiers and biased participation under distinct identifiers with common timestamp bits. Changing ...
  </details>

- **2026-10-07** — Sarthak Choudhary, Mihai Christodorescu, Ashish Hooda et al. — [Secure-CUA: Controlling Untrusted Influence in Computer-Use Agents](http://arxiv.org/abs/2610.09469v1)
  <details><summary>📄 Abstract</summary>
  Computer-use agents (CUAs) perform tasks across applications (such as desktops, mobile apps, and web browsers) by observing graphical interfaces and issuing commands such as clicks and keystrokes. These interfaces combine trusted controls and content with untrusted content needed for legitimate tasks. An adversary controlling this untrusted content can embed instructions or misleading visual cues to change the agent's intended action or redirect its commands to the wrong interface target. We for...
  </details>

- **2026-10-07** — Kerui Li, Zhe Jing, Chenyi Huang et al. — [RobotAPO: Adversarial Physics Preference Optimization for Robotic Manipulation Video Generation](http://arxiv.org/abs/2610.09454v1)
  <details><summary>📄 Abstract</summary>
  Robotic manipulation videos are increasingly used as visual plans for embodied agents, but optimizing purely for visual plausibility often fails to capture the fragile physical manifold of real-world interactions. Even minor physics-violating errors at the interaction boundary, such as interpenetration or premature object motion, can completely invalidate the inferred timing and pose needed for downstream execution. Because standard supervised fine-tuning lacks the direct pressure to penalize th...
  </details>

- **2026-10-07** — Jiyoung Kim, Paul Hyunbin Cho, Jisu Nam et al. — [GRACE: Generation-aware latent compression for efficient video generation](http://arxiv.org/abs/2610.10524v1)
  <details><summary>📄 Abstract</summary>
  Highly compressed video autoencoders offer an effective way to accelerate video diffusion models, as the Diffusion Transformer (DiT) operates on far fewer tokens. However, such autoencoders are challenging to train, since a higher compression ratio degrades reconstruction quality and recovering it requires more channels, which is known to slow the convergence of the DiT. The compressed latent also differs from the one the DiT was trained on, so the pretrained DiT must be either retrained from sc...
  </details>

- **2026-10-07** — Sarath Sankar, Abhijit Sinha, Shankar Ghosh et al. — [Trend formation with sparse global sampling](http://arxiv.org/abs/2610.10521v1)
  <details><summary>📄 Abstract</summary>
  Achieving global coordination without a central controller or dense global communication is a defining challenge for both biological collectives and engineered swarms. We introduce and analyze a minimal model in which self-propelled agents in a bounded domain periodically reorient their motions toward the centroid of a small, randomly chosen subset of their peers, with no direct sensing of any individual neighbor's position or heading. We show that this sparse, non-local sampling rule reliably d...
  </details>

- **2026-10-07** — Yihan Li, Yating Feng, Shengjiu Sun et al. — [Agentic RSR: Real-to-Sim-to-Real through Scene Reconstruction and Execution-Grounded Robot Policies](http://arxiv.org/abs/2610.10479v1)
  <details><summary>📄 Abstract</summary>
  A simulation of a real robot workspace must preserve task-relevant interactions, while policies developed in it must operate on observations available to the real robot. Yet scene reconstruction and policy development are often treated separately. We present Agentic Real-to-Sim-to-Real (Agentic RSR), a framework that links scene reconstruction, policy development, and real-robot execution through the same manipulation task. Given a workspace video, a task description, and a known robot model, an...
  </details>

- **2026-10-07** — Ting-Yu Dai, Takuya Kurihana, Wing Yee Au et al. — [NeuralBES: A Differentiable, Control-Aware Emulator for Scalable Building Energy Modeling](http://arxiv.org/abs/2610.10459v1)
  <details><summary>📄 Abstract</summary>
  Demand-side flexibility i.e. forecasting, shifting, and curtailing residential energy loads, depends on thermal models trusted across millions of heterogeneous buildings. Existing tools force a hard tradeoff: high-fidelity physics simulators such as EnergyPlus are accurate but sequential and require per-building calibration, while purely data-driven sequence models scale but abandon the physical structure that makes their predictions trustworthy.   We introduce NeuralBES (Building Energy Simulat...
  </details>

- **2026-10-07** — Xingtai Gui, Yucheng Zhou, Dongqian Guo et al. — [Explicit Geometric Chain-of-Thought for Vision-Language-Action in Autonomous Driving](http://arxiv.org/abs/2610.10390v1)
  <details><summary>📄 Abstract</summary>
  Vision-language-action~(VLA) models have emerged as a promising paradigm for autonomous driving. However, existing VLA models still suffer from a fundamental mismatch: driving actions require precise 3D geometric cues, while visual-language understanding and reasoning are largely conducted in a 2D semantic space. In this paper, we propose GeoCoTDrive, an explicit geometric chain-of-thought framework that grounds geometry in a planning-oriented manner. GeoCoTDrive follows a think with 2D first, d...
  </details>

- **2026-10-07** — Liu Renhang, Navonil Majumder, Tej Deep Pala et al. — [RoboQuest: Generalist Physical Agents that Search, Inspect and Test](http://arxiv.org/abs/2610.10388v1)
  <details><summary>📄 Abstract</summary>
  Recent advances in multimodal foundation models have made them capable generalist physical agents for a range of manipulation tasks. However, successful operation in an unfamiliar environment may require an agent to seek task-relevant information through interaction when it is absent from the observations: it may need to determine where a relevant object is, inspect an unobserved property, or discover the effect of an unfamiliar tool. We thus introduce RoboQuest, a benchmark for goal-directed em...
  </details>

- **2026-10-07** — Kerui Chen, Jianrong Zhang, Kai Lv et al. — [From Digital Human Interactions to Physics-Based Humanoid Skills: Physics-Grounded Post-Training of Interaction Generators](http://arxiv.org/abs/2610.10322v1)
  <details><summary>📄 Abstract</summary>
  Recent methods have made promising progress in generating interactions between two humanoids, largely relying on physics-based tracking policies to convert digital reference motions into executable trajectories. However, limited tracking capabilities restrict the range of reference motions that can be successfully executed, reducing data utilization. Moreover, even successful tracking does not guarantee physically plausible responses or faithful realization of the intended interactions. In this ...
  </details>

- **2026-10-07** — Amir Rafe, Subasish Das — [Estimating Uncoded Crash Factors with Tabular Foundation and System One Models: Kumo Tabular and Jev](http://arxiv.org/abs/2610.10321v1)
  <details><summary>📄 Abstract</summary>
  Road safety programs count the coded fields of police crash records, while the officer's narrative, which often records factors the fields omit, is rarely read. A safety office thus cannot tell how much its counts miss or where to review. This study develops and evaluates a system that joins both views of the 5,601,890 Texas crashes from 2017 to 2025 into population estimates with stated validity. An in-context tabular foundation model, Kumo Tabular, reads the coded record of every crash, a cali...
  </details>

- **2026-10-07** — Hanyong Xu, Zhaolai Dang, Tong Zhang — [Beyond LLM-GA: Secure Fluid Antenna Systems with ReEvo-Designed Memetic Algorithm](http://arxiv.org/abs/2610.10235v1)
  <details><summary>📄 Abstract</summary>
  Fluid antenna systems (FASs) offer significant spatial flexibility, yet securing them against eavesdropping is critical for practical FAS deployment in military, satellite, and internet-of-things networks. Although large language model (LLM)-assisted genetic algorithms (LLM-GAs) can address this secure FAS port selection problem, whether further algorithmic improvement is possible warrants deeper investigation. To this end, we propose a memetic algorithm based on reflective evolution (ReEvo). Un...
  </details>

- **2026-10-07** — Hyojae Kang, Hyun-mok Jung, Joonho Lee et al. — [Design of a Fully Actuated 4-DOF Robotic Finger With Joint-Specific Hybrid Remote Actuation](http://arxiv.org/abs/2610.10180v1)
  <details><summary>📄 Abstract</summary>
  This paper presents a fully actuated 4-DOF robotic finger using a joint-specific hybrid remote-actuation architecture. The metacarpophalangeal (MCP) joint is driven by two coordinated rigid-link transmission sets, whereas the proximal interphalangeal (PIP) and distal interphalangeal (DIP) joints are independently actuated by closed-loop wire transmissions incorporating circular rolling-contact joints (RCJs). A larger transmission radius is used at the PIP joint than at the DIP joint. The RCJ wir...
  </details>

- **2026-10-07** — Andrey Kuehlkamp, Priscila Correa Saboia Moreira, Samuel Rund — [Does Document Structure Help Dense Retrieval? A Placebo-Controlled Ablation of Four Mechanisms Across Two Corpora](http://arxiv.org/abs/2610.10170v1)
  <details><summary>📄 Abstract</summary>
  Retrieval-augmented generation systems increasingly rely on document-structure treatments: structure-aligned chunking, LLM-generated chunk contexts, heading-path metadata, and hierarchical two-stage retrieval. Separate studies support each on different corpora, embedders, and metrics, and none control for a shared confound: any text prepended to a chunk perturbs its embedding. We present a mechanism-isolating ablation testing all four treatments under one protocol, matching chunk sizes across co...
  </details>

- **2026-10-07** — Yossi Arjevani — [Eigenvalues of the Hessian in Deep Learning: The Origin of Symmetry and Its Breaking](http://arxiv.org/abs/2610.09919v1)
  <details><summary>📄 Abstract</summary>
  Hessian spectra at trained models in deep learning exhibit a persistent pattern: eigenvalues organize into distinct clusters, including a large bulk near zero and a few isolated outliers. This paper shows that a natural account of these spectral phenomena emerges when the original setting is understood as a departure from a nearby, otherwise hidden, highly symmetric reference.   Modifications, including changes to the architecture, data distribution, or parameter metric, expose a nearby referenc...
  </details>

- **2026-10-07** — Yueying Li, Zhongle Xie, Ke Chen et al. — [QCATS: Query Context-Aware Transformer Slicing for Efficient Predictive Query Processing](http://arxiv.org/abs/2610.09894v1)
  <details><summary>📄 Abstract</summary>
  In-database predictive query processing increasingly applies Transformer-based models within relational pipelines. However, existing in-database inference typically exposes only tuple-level model inputs to the inference runtime, leaving relational predicates and metadata statistics invisible to neural execution planning. In this paper, we propose QCATS, a query context-aware transformer slicing framework that enables efficient sparse inference inside database systems. QCATS executes at query gra...
  </details>

- **2026-10-07** — Yifei Zhu, Yangyang Cai, Mingyi Shi et al. — [DynaConTalk: Wavelet-Constrained Diffusion for Long-Form and Controllable Holistic Co-Speech 3D Motion](http://arxiv.org/abs/2610.09846v1)
  <details><summary>📄 Abstract</summary>
  Holistic co-speech animation is prone to averaging in both motion representation and speech conditioning. In coordinate-space diffusion, slow body posture, mid-frequency gesture strokes, and fast hand or facial details are entangled in one prediction target, often producing low-variance, over-smoothed motion. Meanwhile, dense rhythmic and acoustic cues can dominate sparse content-specific information under fixed multimodal fusion. We present DynaConTalk, a wavelet-constrained diffusion framework...
  </details>

- **2026-10-07** — Philipp Strasberg — [Redundant Records of the Past: Unifying Quantum Darwinism and Decoherent Histories](http://arxiv.org/abs/2610.09845v1)
  <details><summary>📄 Abstract</summary>
  There exist two different paradigms for records in isolated quantum systems: decoherent histories (which determines which past events leave formal records) and quantum Darwinism (which determines which current events get redundantly recorded). Neither one implies the other, and connections between the two are scarcely investigated. We unify quantum Darwinism and decoherent histories based on the insight that only redundant records about past events matter. The resulting framework of past redunda...
  </details>

- **2026-10-07** — Sunjoo Whang, Jungjun Oh, Minsung Kim et al. — [Dual-QK: Sharp Queries and Flat Keys for Prunable 2-bit KV Caches](http://arxiv.org/abs/2610.09827v1)
  <details><summary>📄 Abstract</summary>
  Long inputs and extended generation increase the storage and access costs of the key-value (KV) cache. Low-bit quantization reduces storage and memory traffic, while query-channel pruning can further reduce key-cache reads. Rotation-based quantization redistributes the energy of key outliers across channels. To maintain computational invariance, the same orthogonal transform must be applied to queries, preserving query-key dot products. However, this rotation can disperse query energy, weakening...
  </details>

- **2026-10-07** — Inbasekaran S — [EntroPrefill: Renyi-Guided Context Pruning with Conditional Stability Guarantees for Retrieval-Augmented Generation](http://arxiv.org/abs/2610.09757v1)
  <details><summary>📄 Abstract</summary>
  Mid-prefill pruning can reduce the sequence processed by deeper transformer layers, but attention concentration alone does not certify that discarded context is dispensable. We formulate EntroPrefill as a Renyi-guided proposal mechanism coupled to explicit constraints on discarded attention mass. Sink-isolated, regularized head pooling respects grouped-query attention while exposing a quantitative trade-off between specialization and worst-head coverage. We derive a mixture-to-head deletion enve...
  </details>

- **2026-10-07** — Tianle Wang, Jiayu Liu, Ruizhi Zhao et al. — [SAPD: Step-Aligned Privileged Distillation](http://arxiv.org/abs/2610.09665v1)
  <details><summary>📄 Abstract</summary>
  On-policy post-training can improve large language models by learning from their own trajectories, but requires costly rollout generation. We ask whether fixed demonstrations can support competitive off-policy learning through better supervision. Our premise is that their usefulness depends not only on the training trajectories, but also on whether supervision provides informative preferences among continuations and connects this guidance to the reasoning decision being learned. We introduce Ste...
  </details>

- **2026-10-07** — Zhifan Sun, Sebastian Gombert, Jannik Lossjew et al. — [Alice: A Large-Scale German Benchmark for Rubric-Based Multi-Dimensional Automatic Short Answer Scoring](http://arxiv.org/abs/2610.09661v1)
  <details><summary>📄 Abstract</summary>
  Automatic Short Answer Scoring (ASAS) is central to NLP for Education. However, openly available benchmarks remain scarce, and existing datasets largely address how well students answer a question directly rather than how well they master underlying concepts (knowledge elements) such as thermal energy or epistemic activities (skills) such as reasoning or claim.   To address this gap, we introduce Alice, a large-scale, rubric-based German ASAS dataset that is pedagogically aligned and comprises t...
  </details>

- **2026-10-07** — Samuel Tetteh, Cody Fleming — [It Is Not Seeing the Hazard: A Frozen Vision-Language Safety Score Measures Its Caption Bank](http://arxiv.org/abs/2610.09517v1)
  <details><summary>📄 Abstract</summary>
  Frozen vision-language models increasingly provide safety signals for reinforcement learning. Their use assumes that similarity to language describing danger indicates the hazard itself. Yet policy return and collision rate cannot reveal whether a score detects hazards or responds to correlated features of the scene. VLM-based methods have reported gains in driving and safe-RL benchmarks by converting image-text similarity into rewards, costs, or confidence weights. Such signals promise to reduc...
  </details>

- **2026-10-07** — Zihan Guo, Roxy He, Junwei Quan — [Before Bringing It Up: When and How AI Companions Should Use Memor](http://arxiv.org/abs/2610.09470v1)
  <details><summary>📄 Abstract</summary>
  Memory can sustain AI companionship, yet even accurate recollection can be inappropriate to use. Two rounds of formative interviews with 14 users (n = 6 exploratory, n = 8 memory-focused) motivate asking what a companion should consider before using past information. Eight themes inform Reconsider, a single-call procedure with five checks and four handling modes, evaluated on 80 scenarios across five models over 400 blinded within-model pairs. Two LLM judges favored Reconsider by net margins of ...
  </details>

- **2026-10-07** — Yeonseo Lee, Hyosup Shin, Guebin Hwang et al. — [TempoBridge: Language-Guided Tempo Control for Vision-Language-Action Policies](http://arxiv.org/abs/2610.09451v1)
  <details><summary>📄 Abstract</summary>
  Vision-Language-Action (VLA) models are effective at understanding what task to perform, but provide limited control over how it should be executed, such as moving quickly or slowly. We introduce TempoBridge, a lightweight framework that uses frozen VLA representations to modulate actions according to tempo cues in the instruction at each task phase, without additional tempo-conditioned robot demonstrations or tempo-specific base-policy fine-tuning. TempoBridge extracts tempo cues from contextua...
  </details>

- **2026-10-07** — Ling Li, Jianhui Zhong, Wei Liu et al. — [Spatial Latent Reasoning for Embodied Reference Understanding](http://arxiv.org/abs/2610.09418v1)
  <details><summary>📄 Abstract</summary>
  Pointing-gesture visual grounding requires connecting hand geometry with the visual identity and extent of a referred object. A central challenge for continuous latent reasoning is how to organize these complementary cues into useful intermediate supervision. We propose Spatial Latent Reasoning (SLR), a framework that structures this supervision around an ordered sequence of geometric and visual states. A spatial ray state is supervised by fingertip position and pointing direction, followed by f...
  </details>

- **2026-10-07** — Eunji Shin, Dahyun Choi, Seungyeon Jo et al. — [TiTok: Audio-Visual LLM for Multi-Segment Temporal Grounding](http://arxiv.org/abs/2610.09408v1)
  <details><summary>📄 Abstract</summary>
  Audio-visual multi-segment grounding (AV-MSG) in untrimmed videos, reasoning over audio-visual evidence and predicting multiple segments for a query, is a fundamental problem but remains challenging. Visual-only models overlook complementary acoustic cues, while audio-visual models often fail to calibrate the number of events - a phenomenon we refer to as count miscalibration. We present TiTok, an audio-visual large language model (AV-LLM) that localizes an arbitrary number of temporal event seg...
  </details>

- **2026-10-07** — Yihao Hu, Yanlin Feng, Naoki Otani et al. — [ARCS: Towards Precise Text-to-SQL via Structured Disambiguation](http://arxiv.org/abs/2610.09396v1)
  <details><summary>📄 Abstract</summary>
  As text-to-SQL systems move beyond demonstrations toward real-world deployment, ambiguity in user questions becomes a primary source of errors. Such ambiguities are often subtle, domain- or data-specific, and can silently cause system outputs to deviate from the user's true intent. Ambiguity is traditionally addressed through conversational clarification, which is often inefficient, cognitively demanding, and poorly aligned with real-world user workflows. We propose structured disambiguation, a ...
  </details>

- **2026-10-07** — Yizhi Song, Hang Ni, Weijia Zhang et al. — [DUDA-Bench: Benchmarking LLM Agents on Multimodal Data-Driven Urban Diagnosis](http://arxiv.org/abs/2610.09374v1)
  <details><summary>📄 Abstract</summary>
  Urban diagnosis integrates heterogeneous observations to identify urban problems, localize affected areas, and investigate contributing factors, informing evidence-based urban planning and management. However, its reliance on labor-intensive, case-specific expert workflows limits scalability and reuse, motivating the exploration of agent-based execution. To evaluate this capability, we introduce DUDA-Bench, a hierarchical and interactive benchmark that formalizes data-driven urban diagnosis as a...
  </details>

- **2026-10-07** — Bingxuan Li, Yiwen Song, Xueqing Wu et al. — [VIS-Ground: Video Interactive Storytelling with Contextual Grounding](http://arxiv.org/abs/2610.09326v1)
  <details><summary>📄 Abstract</summary>
  Video interactive storytelling enables viewers to actively steer how a video unfolds. However, once we allow viewers to intervene during generation, a new challenge arises: The viewer's request can have latent dependencies on both the grounding source and the current rendered video state. These dependencies may not be explicitly stated in any individual input, but emerge only when the source, rendered history, and new viewer intent are considered jointly. Existing interactive video generation sy...
  </details>

- **2026-10-07** — Zhiqin Yang, Chenxin Li, Xiaomeng Hu et al. — [RobotWorld: Benchmarking Multimodal Agents for Robot Use Across Diverse Tasks and Embodiments](http://arxiv.org/abs/2610.10409v1)
  <details><summary>📄 Abstract</summary>
  General-purpose agents increasingly write code, use tools, and complete complex digital tasks, raising the question of how far these capabilities carry into the physical world. To investigate this, we introduce RobotWorld, a challenging simulation testbed for robot use: turning instructions and observations into physical task execution through robot interfaces. Its 84 tasks span manipulation, mobile manipulation, locomotion, driving, and aerial control, with explicit interaction budgets and exec...
  </details>

- **2026-10-07** — Xin You, Zhiwei Ning, Zukai Chen et al. — [Self-correction Optimization for Interleaved Multimodal Generation](http://arxiv.org/abs/2610.10400v1)
  <details><summary>📄 Abstract</summary>
  Multimodal large language models (MLLMs) have made significant progress in visual understanding and generation. However, generating interleaved image--text content remains challenging, as it requires tightly integrated multimodal understanding and generation capabilities. Although existing MLLMs provide promising solutions, most rely on additional training with augmented data, which is computationally expensive and remains limited in preserving visual subjects, temporal consistency, and physical...
  </details>

- **2026-10-07** — Yifan Wu, Qin Li, Nan Min et al. — [OpenViTac: Learning and Benchmarking Visuo-Tactile Policies in a Unified Sim-and-Real Framework](http://arxiv.org/abs/2610.10384v1)
  <details><summary>📄 Abstract</summary>
  Tactile feedback provides embodied agents with physical information beyond visual observations, enabling more reliable interaction with the real world. However, despite the rapid progress of vision-tactile-language-action (VTLA) policies, there remains a lack of unified benchmarks for evaluating tactile-enabled robot manipulation across simulation and the real world. To address this gap, we introduce OpenViTac, a visuo-tactile manipulation benchmark for evaluating robot policies across simulatio...
  </details>

- **2026-10-07** — Yanjiang Guo, Haodong Yan, Zhide Zhong et al. — [Video Prediction Policy 2: Predict Better, Act Better](http://arxiv.org/abs/2610.10270v1)
  <details><summary>📄 Abstract</summary>
  World action models (WAMs) have emerged as an important class of generalist robot policies, aiming to transfer video prediction priors to action learning. However, we find that existing WAMs frequently produce incorrect motion predictions in open-ended environment, leading to erroneous actions. We attribute this limitation to two factors: (1) base video models are not optimized for manipulation, and (2) naively incorporating action components into video models can substantially degrade their gen...
  </details>

- **2026-10-07** — Kamile Dementaviciute, Julija Vaitonyte, Tijl De Bie — [LLM Persuasion Is in the Eye of the Evaluation](http://arxiv.org/abs/2610.10232v1)
  <details><summary>📄 Abstract</summary>
  Large language models (LLMs) have already been shown to match or exceed human experts in persuasion. While their persuasive capabilities hold promise for beneficial uses such as education and health communication, they can also be used to manipulate and misinform, making their evaluation a growing priority for developers and regulators. That evaluation, however, remains fragmented: studies differ in what they treat as persuasion, and broad claims often rest on narrow, situation-specific assessme...
  </details>

- **2026-10-07** — Leon Mayer, Lucas Luttner, Patrick Godau et al. — [HeiCo-FOCUS: A Clinically Grounded Dataset for Long-Context Video Understanding](http://arxiv.org/abs/2610.10156v1)
  <details><summary>📄 Abstract</summary>
  Recent advances in Vision-Language Models (VLMs) have led to rapid progress in video understanding across a wide range of benchmark tasks. However, existing evaluations largely focus on short-term reasoning, failing to assess a critical capability: maintaining cumulative temporal consistency over extended time horizons. To close this evaluation gap, we introduce HeiCo-FOCUS, a clinically grounded dataset for evaluating long-context video understanding through the task of Foreign Object Contextua...
  </details>

- **2026-10-07** — Mukul Dwivedi, Jesse Railo, Andreas Rupp — [A finite element exterior-to-interior reconstruction in the fractional conductivity inverse problem](http://arxiv.org/abs/2610.10484v1)
  <details><summary>📄 Abstract</summary>
  We develop a regularized finite element method for the fractional conductivity equation, recovering the conductivity on an exterior observation region from noisy Dirichlet-to-Neumann measurements and using this reconstruction to determine the interior conductivity. Mesh-localized inputs and mass-lumped Tikhonov regularization discretize the exterior determination principle of Covi--Railo--Zimmermann (2026, Calc. Var. PDE). We prove exterior \(L^2\)- and \(L^\infty\)-convergence with error estima...
  </details>

- **2026-10-07** — Duy-Cat Can, Mau Minh Phuc Le, Tuan-Khoa Hoang et al. — [MemoCare: An Interactive Multimodal Mobile System for Automated Cognitive Screening](http://arxiv.org/abs/2610.10448v1)
  <details><summary>📄 Abstract</summary>
  MemoCare is an interactive mobile system for automated multimodal cognitive screening. A React Native application combines spoken responses, temporal and spatial orientation, touchscreen actions, and visuoconstruction in complete English and Vietnamese workflows. Speech is transcribed by Google Speech-to-Text and scored locally with deterministic task-specific natural language processing rules; GPS coordinates are resolved by the MemoCare spatial module before answer matching; touch tasks are sc...
  </details>

- **2026-10-07** — Richard Cornelius Suwandi, Feng Yin, Kevin Murphy — [Kernel Autoresearch for Open-Ended Model Discovery](http://arxiv.org/abs/2610.10394v1)
  <details><summary>📄 Abstract</summary>
  Kernels encode the inductive bias of a wide range of machine learning models, yet automated kernel design faces a fundamental dilemma. A fixed grammar of base kernels and operators guarantees validity but limits the search to structures expressible by those building blocks. Conversely, unrestricted programs remove this limitation but no longer guarantee validity. In our stress tests, 22-58% of LLM-generated kernels that pass numerical checks on random inputs fail when evaluated at different scal...
  </details>

- **2026-10-07** — Yibei Guo, Rui Liu — [Input-Blind Controls Produce Substantial Oracle Headroom for Layer Programs in Multiple-Choice Evaluation](http://arxiv.org/abs/2610.10368v1)
  <details><summary>📄 Abstract</summary>
  Adaptive computation aims to improve language-model inference by tailoring execution to each input. For layer programs, oracle evaluations use known answers to estimate the potential gain from this flexibility, before a practical selector is available. However, a gain from selection does not by itself explain why the chosen programs help. This study examines this distinction using 32 layer-skipping and repetition programs on two models and 4,413 multiple-choice items. The analysis compares their...
  </details>

- **2026-10-07** — Eisuke Hirota, Aarav Sane, Rohan Paleja — [Temporally Interpretable Differentiable Decision Trees](http://arxiv.org/abs/2610.10367v1)
  <details><summary>📄 Abstract</summary>
  Interpretability offers a solution to safe autonomy by providing transparency into an agent's underlying decision-making model. Within sequential-decision making tasks, differentiable decision trees (DDTs) are one approach to such interpretability, maintaining automatic-differentiable policies while providing humans with a discrete tree-based visualization. Nonetheless, current implementations of DDTs are not well-suited for sequential-decision making domains, as there exists an inherent mismatc...
  </details>

- **2026-10-07** — Bo Li, Ankang Sun, Ruijie Wang — [Settling PROPm and PROPavg in Graphical Resource Allocation](http://arxiv.org/abs/2610.10336v1)
  <details><summary>📄 Abstract</summary>
  We study proportional fairness in graphical resource allocation, where agents are vertices, indivisible items are edges, and each item must be allocated to one of its two endpoints. It has been proved that PROP1 orientations always exist and PROPx orientations may not, but it has remained open whether the intermediate relaxations PROPm and PROPavg (both can be satisfied without graphical constraints) can always be satisfied. In this paper, we resolve this gap. We prove that PROPm orientations al...
  </details>

- **2026-10-07** — Mihai Bogdan Deaconu, Ioan Daniel Pop — [HAN-Mamba: Hierarchical Selective State Space Networks for Multi-Scale Financial Volatility Forecasting](http://arxiv.org/abs/2610.10323v1)
  <details><summary>📄 Abstract</summary>
  Short-horizon realized volatility forecasting requires the integration of market information that evolves at incompatible temporal resolutions, from second-level order book dynamics to weekly regime drift. Our conference work introduced HAN-T, a hierarchical architecture in which scale-specific Transformer encoders process short, mid, and long-horizon streams and a learned attention fuser weighs their contributions. This article replaces the quadratic attention encoders with selective state spac...
  </details>

- **2026-10-07** — Eduardo Santos-Escriche, Valerie Engelmayer, Ya-Wei Eileen Lin et al. — [How Do Transformers Learn to Represent Symmetries?](http://arxiv.org/abs/2610.10305v1)
  <details><summary>📄 Abstract</summary>
  Training Transformer-based architectures with finite data augmentation has become an increasingly popular approach in geometric machine learning. Despite its empirical success, the interplay between the Transformer architecture, invariance to different symmetries, and augmentation budgets remains underexplored. In this paper, we study the ability of a vanilla Transformer to learn various symmetries through finite data augmentation for point cloud datasets. We identify an ordering of increasing l...
  </details>

- **2026-10-07** — Mingyan Liu, Min Huang — [SemanticFold: Latent Sequence Compression SeparatesLanguage Modeling, Decodability, and Reasoning](http://arxiv.org/abs/2610.10304v1)
  <details><summary>📄 Abstract</summary>
  We study whether latent sequence compression of prompt prefixes preserves the capabilities that large language models rely on during inference. We introduce SemanticFold, a compression scheme that folds prefix hidden states at learned boundaries, and evaluate it across five model scales: Qwen3-1.7B, Qwen3-8B, SmolLM2-1.7B, Pythia-1.4B, and Pythia-6.9B. We use a fixed-target protocol: a frozen prefix is executed natively or compressed, and both arms teacher-force identical continuation tokens. Th...
  </details>

- **2026-10-07** — Junhyeok Kim, Jinyeong Kim, Jae Wan Park et al. — [On the Necessity of Attention-FFN Split in Vision Transformers](http://arxiv.org/abs/2610.10303v1)
  <details><summary>📄 Abstract</summary>
  The standard Transformer architecture relies on a rigid pattern that alternates Attention and Feed-Forward Network (FFN) layers. Despite its widespread adoption, the inductive bias imposed by this strict separation has not been systematically examined. In this work, we investigate the necessity of the Attention-FFN dichotomy in Vision Transformers (ViTs). To facilitate this analysis, we introduce the AttenFeed module, a unified component that integrates the functional properties of both Attentio...
  </details>

- **2026-10-07** — Tommaso Marzi, Ahmed Hendawy, Jan Peters et al. — [Continual Graph Multi-Agent Reinforcement Learning](http://arxiv.org/abs/2610.10302v1)
  <details><summary>📄 Abstract</summary>
  In Continual Multi-Agent Reinforcement Learning (CMARL), agents learn cooperative policies across sequences of tasks, aiming to adapt effectively to new tasks while preserving the ability to solve previously encountered ones. In many applications, tasks differ in their underlying structure, which can represent, for example, distinct operational conditions or target configurations (e.g., different network topologies in power grids or arrangements in formation control). Existing CMARL methods lack...
  </details>

- **2026-10-07** — Yue Qiu, Zekang Du, Yiqun Diao et al. — [From Prompts to Trees: Effective LLM-Guided Tree Generation for Few-Shot Tabular Classification](http://arxiv.org/abs/2610.10227v1)
  <details><summary>📄 Abstract</summary>
  While Large Language Models (LLMs) possess rich world knowledge and impressive generalization capabilities, their direct application to tabular data classification is hindered by high inference costs and limited interpretability. In contrast, decision trees are fast and transparent but often underperform in low-data regimes. In this work, we propose a novel framework that bridges these paradigms by distilling LLM knowledge into interpretable decision trees under a few-shot learning setting. Inst...
  </details>

- **2026-10-07** — Stepan Zharkov, Krish Singal, Ashwin Padaki et al. — [Attention via Black-Box Vector Search](http://arxiv.org/abs/2610.10135v1)
  <details><summary>📄 Abstract</summary>
  Sparse attention mechanisms estimate attention over $n$ tokens using a small subset of keys. Many existing approaches use maximum inner product search (MIPS) to retrieve the heaviest keys, which motivates the following question: given black-box access to a MIPS oracle, how many keys must be retrieved to output an $\varepsilon$-accurate attention estimate?   We answer this question by unifying prior approaches through the framework of priority sampling. With a single MIPS index, we show that $Θ(\...
  </details>

- **2026-10-07** — Xiaoran Liu, Ziwei He, Xipeng Qiu — [Mechanics of Long-Context Hybrid Models Part 1.1: From Hybrid Attention to Hybrid Position](http://arxiv.org/abs/2610.10114v1)
  <details><summary>📄 Abstract</summary>
  The architectural design of Large Language Models (LLMs) is shifting from traditional full-attention-only models to hybrid models, which combine different attention modules to improve long-context efficiency and performance in length extrapolation and context extension. To explain why hybrid models work and how to design them better, we propose Mechanics of Long-Context Hybrid Models. As Part 1.1 of this series, we begin with hybrids of full attention and either sliding-window attention (SWA) or...
  </details>

- **2026-10-07** — Peter Baile Chen, Geoffrey X. Yu, Xinming Liu et al. — [ExperienceIndex: Artifact-Grounded Memory](http://arxiv.org/abs/2610.10091v1)
  <details><summary>📄 Abstract</summary>
  Knowledge-intensive tasks require answering many questions by reasoning about a shared corpus of artifacts (e.g., court cases, or scientific literature). As humans interact with these corpora, they naturally accumulate experiential knowledge about artifacts, enabling them to quickly identify the complete set of relevant artifacts for each new task. However, existing AI agents lack appropriate memory solutions to build or reuse such artifact-grounded experience, leading to lower answer quality an...
  </details>

- **2026-10-07** — Efe Çangırılı, Murat Kurt — [TRACK: Telemetry-Based Racing Analysis and Coaching Kit in Sim Racing Games](http://arxiv.org/abs/2610.10061v1)
  <details><summary>📄 Abstract</summary>
  This paper presents TRACK (Telemetry-Based Racing Analysis and Coaching Kit), which is a framework for analyzing driving performance in sim racing and profiling how individual drivers behave behind the wheel. We report this framework together with its limitations: we calibrate each clustering result against a null, and when one does not separate from chance, we say so. Instead of restricting ourselves to scoring drivers or sorting them into preset labels, we represent each recording session as a...
  </details>

- **2026-10-07** — Pujian Mao — [Geometric interpretation of electromagnetic memory and large gauge transformation](http://arxiv.org/abs/2610.09960v1)
  <details><summary>📄 Abstract</summary>
  We develop a geometric characterization of electromagnetic memory in terms of the optical data of charged-particle congruences. We derive the worldline deviation of charged particles near null infinity for both massless and massive particles and construct the corresponding optical data. We show that the asymptotic shear of the charged-particle congruence provides an equivalent encoding of electromagnetic memory and its associated large gauge transformation. This establishes a geometric interpret...
  </details>

- **2026-10-07** — Paul W. Goldberg, Isaac Robinson, Nicholas Teh — [Minimizing Cumulative Envy in Allocating a Sequence of Items](http://arxiv.org/abs/2610.09843v1)
  <details><summary>📄 Abstract</summary>
  We study temporal fair division with indivisible goods that arrive sequentially and must be allocated irrevocably. In contrast to the usual online model, we assume that valuations and future arrivals are known in advance, and ask how unfairness evolves during the process. We introduce \emph{cumulative maximum envy}: the sum, over all rounds, of the maximum pairwise envy at that round. Equivalently, this is the area under the worst-envy curve, and it captures both the magnitude and the duration o...
  </details>

- **2026-10-07** — Francesco Cambria, Francesco Invernici, Andrea Colombo et al. — [Empowering Users in Graph Rule Mining via Large Language Models](http://arxiv.org/abs/2610.09842v1)
  <details><summary>📄 Abstract</summary>
  In the era of interconnected data, graphs have emerged as an effective abstraction for modeling complex systems in an intuitive format, especially with the rise of Property Graphs, which offer an intuitive and scalable way of navigating non-intuitive structures. In this context, graph mining techniques have been developed for testing complex graph-based rules, as the MINE GRAPH RULE operator, which, however, require users to have prior expertise both in graph theory and formal query language. In...
  </details>

- **2026-10-07** — Raneem Mahajne, Toviah Moldwin — [Fully Interpretable Minimal Transformers: From Geometry to Algorithm](http://arxiv.org/abs/2610.09838v1)
  <details><summary>📄 Abstract</summary>
  We present a framework for building and interpreting minimal transformer models. By constraining a transformer's embedding dimension and head size to 2, we enable full two-dimensional visualization of its internal representations. Embeddings, query/key/value transforms, attention outputs, residual streams, and decision boundaries can all be seen directly. Our central claim is that the learned geometry implies an algorithm; the arrangement of points and boundaries in R^2 can be read as a step-by-...
  </details>

- **2026-10-07** — Deyuan Liu, Yihao Hu, Jingxuan Zhang et al. — [UltraText Bench: A Comprehensive Bilingual Benchmark for Evaluating Visual Text Rendering in Image Generation](http://arxiv.org/abs/2610.09823v1)
  <details><summary>📄 Abstract</summary>
  Dense visual text requires image generators to reproduce long strings across multiple regions with correct placement and legibility. As short-string rendering improves, evaluation must test sustained performance across more demanding scenes. We introduce UltraText Bench, a bilingual benchmark for prompt-only generation of dense visual text. It contains 432 prompts spanning 24 real-world scene categories and three difficulty levels, split equally between English and Chinese. Each human-reviewed p...
  </details>

- **2026-10-07** — Mingqing Yuan, Xiaobo Liang, Junwei Yang et al. — [Judging in Latent Space: Efficient Generative Reward Modeling via Semantics-Preserving Compression](http://arxiv.org/abs/2610.09788v1)
  <details><summary>📄 Abstract</summary>
  Reward modeling often requires jointly representing and reasoning over multiple evaluation criteria, yet verbalizing this process token by token can incur substantial inference cost. Recent work on latent reasoning suggests that continuous states may support this computation more compactly. We introduce LatentGRM, a latent evaluation framework built on semantic chunking, compression, and reconstruction. By using the structure of rubric-guided evaluations to guide compression, LatentGRM learns co...
  </details>

- **2026-10-07** — Faissal Izermine, Hanru Bai, Oscar Davis et al. — [Unrolled Flow Models for Reasoning](http://arxiv.org/abs/2610.09759v1)
  <details><summary>📄 Abstract</summary>
  Flow matching enables language generation in few steps, but whether additional integration steps improve reasoning remains unclear. We prove that a flow parameterized by a two-layer Transformer can solve graph reachability, with the required number of integration steps increasing with the target's distance from the root. Yet, standard flow language models can fail to benefit from additional steps on reasoning tasks. We attribute this limitation to objectives that supervise each time point indepe...
  </details>

- **2026-10-07** — Ahmad Abbas, Tamara Fakih, Nour Fakih et al. — [Shaer: Controlled Arabic Poetry Generation with Meter Subform and Semantic Conditioning](http://arxiv.org/abs/2610.09756v1)
  <details><summary>📄 Abstract</summary>
  Classical Arabic poetry generation requires simultaneously satisfying semantic, linguistic, and fine-grained prosodic constraints. Existing systems typically control broad poetic attributes but do not jointly model semantic intent, meter subform, and poem length. We present Shaer, a controllable Classical Arabic poetry generation framework jointly conditioned on natural-language descriptions, meter subforms, and target hemistich counts. To support this task, we construct an enriched corpus of 11...
  </details>

- **2026-10-07** — Jacobus Arthur, Ahmad Sait, Batool Hani et al. — [SoccerNet-FoulRet: Retrieving Semantically Similar Soccer Foul Videos](http://arxiv.org/abs/2610.09742v1)
  <details><summary>📄 Abstract</summary>
  Refereeing decisions in professional soccer remain inconsistent because referees cannot easily compare a contentious foul against similar past cases. We cast this as a retrieval problem and introduce SoccerNet-FoulRet, the first benchmark for semantic foul retrieval. Given a query foul, the task is to retrieve past fouls judged to be relevant precedents, regardless of camera angle, teams, or appearance. This differs from prior video-to-video retrieval, which matches clips by visual similarity or...
  </details>

- **2026-10-07** — Bahadır Yüzbaşı — [The Lambert Penalty: Logarithmic Shrinkage for Sparse Regression](http://arxiv.org/abs/2610.09627v1)
  <details><summary>📄 Abstract</summary>
  Sparse regression must balance prediction accuracy with reproducible variable selection. We introduce the Lambert penalty by limiting how quickly the retained fraction of a scalar score increases after variable entry. Maximizing retention under this scale-equivariant constraint yields a logarithmic transition from exact zero to an identity tail. The bounded penalty has a fixed shape and a single penalty parameter selected by training-only five-fold cross-validation. We derive an explicit scalar ...
  </details>

- **2026-10-07** — HyeonSeok Lim, SeungWoo Song, Inho Won et al. — [Which Language Should a Skeleton Speak? Language Choices in Multilingual Reasoning](http://arxiv.org/abs/2610.09607v1)
  <details><summary>📄 Abstract</summary>
  Skeleton-based reasoning prompting is a promising training-free approach for structuring LLM reasoning, but prior work largely assumes an English-centric setting. We propose the Language-Aware Skeleton Exploration Framework (LASEF) to study skeleton-language choice in multilingual mathematical reasoning. Across math benchmarks, model scales, and languages, we show that English skeletons yield a small positive tendency on average, most visible for smaller models and low-resource languages. Howeve...
  </details>

- **2026-10-07** — Zicheng Hu, Zhijian Zhou, Xuan Zhang et al. — [COPC: Coupled Off-Policy Correction for Asynchronous LLM Reinforcement Learning](http://arxiv.org/abs/2610.09597v1)
  <details><summary>📄 Abstract</summary>
  Asynchronous RL accelerates large language model post-training by decoupling rollout generation from optimization, but trains on stale trajectories. Existing methods primarily correct token-level policy mismatch through importance-ratio control in the actor objective. We show that this \emph{policy-side correction} alone is insufficient: advantage estimates also inherit mismatch from behavior-policy continuations, which we term \emph{advantage staleness}. We derive exact bias and variance decomp...
  </details>

- **2026-10-07** — Daniel Paulin, Ádám Jung, András A. Benczúr — [Scalable Logistic Gaussian Process Density Regression with Kinetic Langevin Sampling](http://arxiv.org/abs/2610.09591v1)
  <details><summary>📄 Abstract</summary>
  Conditional density estimation targets the full distribution of a response given covariates, as required, for example, for per-galaxy photometric redshifts. We develop a scalable Bayesian estimator based on the logistic Gaussian process. The log conditional density has a separable covariance: a Matérn kernel along the response, represented in a truncated Fourier basis on a circle, and a covariate kernel represented by Nyström features, which accommodate non-stationary kernels with input-dependen...
  </details>

- **2026-10-07** — Lin Wu, Zhe Xu, Hongyi Wang et al. — [Dual- versus Single-Suggestion AI Support for Radiographic Interpretation in Residents: Randomized Multireader Study](http://arxiv.org/abs/2610.09589v1)
  <details><summary>📄 Abstract</summary>
  Purpose: To compare dual- and single-suggestion AI support for radiographic interpretation by residents, particularly when the shared AI suggestion was incorrect.   Materials and Methods: This prospective, multicenter, randomized three-arm reader study was conducted at three hospitals in China from July to September 2026 (ChiCTR2600129243). After specialty stratification, 132 residents with fewer than 3 years of clinical experience were randomized 1:1:1 to GPT-5.4 alone (group A), GPT-5.4 plus K...
  </details>

- **2026-10-07** — Taehyeon Yun, Dongho Kim, Geonwoo Kim et al. — [Correct Answers, Unsupported Findings: Evidence Binding in Forensic Reconstruction of LLM Agent Logs](http://arxiv.org/abs/2610.09581v1)
  <details><summary>📄 Abstract</summary>
  Forensic reconstruction of LLM-agent actions requires not only recovering the correct value, but establishing which preserved record supports that finding. Tool logs, generated explanations, and local citation identifiers capture different parts of this evidence, yet a citation identifier does not establish a source unless its binding to a record is preserved. We audit this distinction using 64 mechanically checkable cases from saved AgentDojo Banking executions. Two LLM readers reconstruct sour...
  </details>

- **2026-10-07** — Jongwook Yoon, Jongwon Lim, Sungjib Lim et al. — [How Do LLMs Change Predictions Under Negation?](http://arxiv.org/abs/2610.09571v1)
  <details><summary>📄 Abstract</summary>
  Negation is an essential feature of human language, yet large language models (LLMs) remain unreliable in processing it. We evaluate recent open-source and closed-source LLMs on our negation benchmark and find that, in 37-71% of cases, they repeat the same answer under negation (e.g., "Madrid" for "What is not the capital of Spain?"). To understand and address this brittleness, we mechanistically examine how models operate under negation. Our main finding is that specialized attention heads and ...
  </details>

- **2026-10-07** — Juuso Jaakola, Vlad Stirbu, Teiko Heinosaari — [Using Learning Analytics to Study Novice Learners' Work on Quantum Circuit Simulator Tasks](http://arxiv.org/abs/2610.09499v1)
  <details><summary>📄 Abstract</summary>
  Interactive quantum circuit simulators are increasingly used to support introductory quantum computing education for learners from varied disciplinary backgrounds. These environments can also generate detailed response logs of submitted circuits, but such data are rarely transformed into evidence that instructors can use for course redesign and development.   We present a learning analytics framework for quantum circuit simulator tasks and report its task-level branch on anonymised logs from an ...
  </details>

- **2026-10-07** — Minu Kim, Jihwan Lee, David R. Mortensen et al. — [Mitigating Accent-Language Confusion in Self-Supervised Speech Representations for Language Identification](http://arxiv.org/abs/2610.09486v1)
  <details><summary>📄 Abstract</summary>
  Spoken language identification (LID) aims to recognize the target language regardless of accent. In practice, however, LID models fine-tuned from self-supervised speech representations frequently confuse accents with languages, misclassifying non-native (L2) speech as the speaker's first language (L1). We show that non-native speech representations lie between native target-language and native L1 poles, causing systematic misclassification. To address this, we introduce a geometric projection th...
  </details>

- **2026-10-07** — Jeonghwan Kim, Sofia Stoica, Jiwan Chung et al. — [Mixture of Layers: Dynamic Layer Routing for Visual Reasoning](http://arxiv.org/abs/2610.09440v1)
  <details><summary>📄 Abstract</summary>
  Pre-trained vision encoders contain layer-wise visual representations that differ in spatial granularity, semantic abstraction, and sensitivity to local details. However, most Multimodal Large Language Models (MLLMs) rely on only the final or penultimate vision encoder representations or fixed aggregation rules, making visual abstraction largely query-agnostic and limiting access to fine-grained cues such as small objects, spatial details, text, and subtle visual attributes. In this work, we pro...
  </details>

- **2026-10-07** — William Y. C. Chen, Elena L. Wang — [The Higher-order Stirling Triangles](http://arxiv.org/abs/2610.09362v1)
  <details><summary>📄 Abstract</summary>
  The $r$th-order Stirling cycle and subset triangles and their associated quasi-Eulerian triangles were introduced by Deb and Sokal in their study of total positivity of combinatorial triangles. They found combinatorial interpretations for the cycle case in terms of Stirling permutations, leaving the subset case open. For $r\ge 2$, we resolve this problem by introducing the notion of Stirling subset permutations along with a consecutive-descent statistic. We also prove the conjectures of Deb and ...
  </details>

- **2026-10-07** — Zengyi Yang, Shuai Yuan, Zhong-Cheng Wu et al. — [CRT-HMAR: Causal Requirement Tracing-Guided Hierarchical Multi-Agent Regulation for Open-Task-Aware Infrared-Visible Image Fusion](http://arxiv.org/abs/2610.09330v1)
  <details><summary>📄 Abstract</summary>
  Infrared and visible (IR-VIS) image fusion integrates complementary multimodal information into a single fused image to support downstream vision tasks. However, existing methods are typically tailored to seen tasks within a fixed task set and struggle to generalize to unseen tasks, which restricts their applicability in real-world open-task scenarios. To address this issue, this paper proposes CRT-HMAR, a Causal Requirement Tracing-Guided Hierarchical Multi-Agent Regulation Framework for open-t...
  </details>

- **2026-10-07** — Baoteng Li, Wenzhuo Wu, Kongming Liang et al. — [Visual Jev Rewards: Reference-Bound Verification for Multi-Subject Image Generation](http://arxiv.org/abs/2610.09328v1)
  <details><summary>📄 Abstract</summary>
  Multi-subject image generation requires rewards that verify whether requested attributes, actions, and relations hold for the specified reference subjects. Subject presence alone does not establish that the correct subjects participate in a requested interaction. We present reference-bound Visual Jev rewards that turn these visual decisions into generator training signals. Each subject-related question receives a positive label only when the requested condition and the relevant reference identit...
  </details>

- **2026-10-07** — Weitian Wang, Shubham Rai, Cecilia De La Parra et al. — [Hardware-aware Calibrated Clustered Attention for Efficient Visual Geometric Transformers](http://arxiv.org/abs/2610.09274v1)
  <details><summary>📄 Abstract</summary>
  The Visual Geometry Grounded Transformer (VGGT) marks a significant leap forward in 3D scene reconstruction, as it is the first model that directly infers all key 3D attributes (camera poses, depths, and dense geometry) jointly in one pass. However, this joint inference mechanism requires global attention layers with extremely long sequences that causes a significant latency bottleneck. In this paper, we propose blockwise clustered attention (BC attention) to accelerate the global attention laye...
  </details>

- **2026-10-07** — Xinzhu Wang, Tanzy Love — [Bayesian Optimization for Dose Finding with Two Agents: Participant Allocation and Final Selection](http://arxiv.org/abs/2610.09245v1)
  <details><summary>📄 Abstract</summary>
  In two-agent dose-finding trials, the next cohort should help identify a combination for final selection. We studied a constrained knowledge-gradient (cKG) rule with one-cohort lookahead that updates independent Gaussian-process models of efficacy and continuous toxicity, reapplies a probability criterion for mean toxicity, and evaluates the resulting selection. We derived a deterministic calculation over a fixed set of dose combinations, holding fitted model parameters fixed during each hypothe...
  </details>

- **2026-10-06** — Hanjun Luo, Xiucheng Zhang, Zhuoning Xu et al. — [ParanoiaEval: Benchmarking Unnecessary Defensive Work in Agentic Coding](http://arxiv.org/abs/2610.08662v2)
  <details><summary>📄 Abstract</summary>
  As coding agents increasingly undertake real-world work autonomously, judging whether their risk treatments are warranted has become important. Existing work evaluates related agent behaviors from separate perspectives, but lacks a systematic framework for unifying these behaviors. To bridge this gap, we introduce ParanoiaEval, the first benchmark for unified evaluation of risk-treatment capabilities in coding agents. Grounded in the well-established Avoidance-Transfer-Mitigation-Acceptance fram...
  </details>


## 📊 统计 / Statistics

| 分类 / Category | 论文数 / Count |
|------|--------|
| jailbreak | 670 |
| prompt-injection | 608 |
| memory-poisoning | 55 |
| tool-use-attack | 152 |
| backdoor | 508 |
| adversarial-attack | 632 |
| privacy-leakage | 4333 |
| steganography | 77 |
| misuse | 1146 |
| red-teaming | 140 |
| vulnerability | 3528 |
| defense | 3373 |
| alignment | 3150 |
| robustness | 3409 |
| watermark | 575 |
| unlearning | 112 |
| agent-safety | 64 |
| benchmark | 67 |
| survey | 395 |
| other | 9177 |

---

📚 **全部 32171 篇论文**（2022 至今）请访问 [GitHub Pages](https://ny1024.github.io/AgentSafety-Papers/) 查看完整列表、搜索与筛选。

*Generated by AgentGuard at 2026-10-10 11:46:12*