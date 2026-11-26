<div align="center">

# AgentGuard 🛡️

**Daily Tracking of LLM Agent Security Papers on arXiv**

[![Auto Update](https://github.com/NY1024/AgentSafety-Papers/actions/workflows/daily-update.yml/badge.svg)](https://github.com/NY1024/AgentSafety-Papers/actions/workflows/daily-update.yml)
[![Papers](https://img.shields.io/badge/Papers-39026-blue)](#)
[![License](https://img.shields.io/badge/License-MIT-green)](#)

</div>

---

## 📖 简介 / Introduction

自动追踪 arXiv 上大模型 Agent 安全方向的最新论文，每日更新，关键词智能分类。

*Automatically tracking the latest LLM Agent security papers on arXiv, updated daily with keyword-based classification.*

**最近更新 / Last Updated**: 2026-11-26 16:14 ｜ **论文总数 / Total Papers**: 39026（近 30 天 / Recent 30 days: 4356）

🌐 **[GitHub Pages](https://ny1024.github.io/AgentSafety-Papers/)** — 查看全部 39026 篇论文（含摘要、分类筛选、搜索）/ View all 39026 papers with abstracts, filters & search

## 📑 分类导航 / Category Navigation

- **[jailbreak](#-jailbreak)** — 越狱攻击 / Jailbreak Attacks — 734
- **[prompt-injection](#-prompt-injection)** — 提示注入攻击 / Prompt Injection Attacks — 713
- **[memory-poisoning](#-memory-poisoning)** — 记忆投毒与篡改 / Memory Poisoning & Tampering — 59
- **[tool-use-attack](#-tool-use-attack)** — 工具使用攻击 / Tool-Use Attacks — 181
- **[backdoor](#-backdoor)** — 后门与投毒攻击 / Backdoor & Poisoning Attacks — 576
- **[adversarial-attack](#-adversarial-attack)** — 对抗攻击 / Adversarial Attacks — 684
- **[privacy-leakage](#-privacy-leakage)** — 隐私泄露 / Privacy Leakage — 4691
- **[steganography](#-steganography)** — 隐写与隐蔽通信 / Steganography & Covert Communication — 96
- **[misuse](#-misuse)** — 滥用与误用 / Misuse & Abuse — 1366
- **[red-teaming](#-red-teaming)** — 红队测试 / Red Teaming — 159
- **[vulnerability](#-vulnerability)** — 漏洞与攻击面 / Vulnerabilities & Attack Surfaces — 4192
- **[defense](#-defense)** — 防御与防护方法 / Defense & Protection Methods — 4141
- **[alignment](#-alignment)** — 对齐与安全约束 / Alignment & Safety Constraints — 3884
- **[robustness](#-robustness)** — 鲁棒性与可靠性 / Robustness & Reliability — 4249
- **[watermark](#-watermark)** — 水印与溯源 / Watermarking & Provenance — 822
- **[unlearning](#-unlearning)** — 机器遗忘 / Machine Unlearning — 127
- **[agent-safety](#-agent-safety)** — Agent 安全框架 / Agent Safety Frameworks — 67
- **[benchmark](#-benchmark)** — 安全评测与基准 / Safety Benchmarks & Evaluation — 78
- **[survey](#-survey)** — 综述与系统化 / Surveys & Systematization — 474
- **[other](#-other)** — 其他安全相关 / Other Security-Related — 11733

## 📄 近期论文 / Recent Papers (Last 30 Days)

> 仅展示最近 30 天中最新的 500 篇论文（含日期、作者、摘要）。近 30 天共 4356 篇，完整 39026 篇论文列表请访问 [GitHub Pages](https://ny1024.github.io/AgentSafety-Papers/)

> Showing the latest 500 of 4356 papers from the last 30 days (with date, authors & abstract). For the full list of 39026 papers, visit [GitHub Pages](https://ny1024.github.io/AgentSafety-Papers/)

### 📂 jailbreak
*越狱攻击 / Jailbreak Attacks* — 5 papers

- **2026-11-25** — Manit Baser, Vyoman Jain, Rachel Yeo Hui Min et al. — [Latent-in-the-Middle: On the Security of Cross-Model Latent Communication in Multi-Agent Systems](http://arxiv.org/abs/2611.34278v1)
  <details><summary>📄 Abstract</summary>
  As large language models increasingly collaborate in heterogeneous multi-agent systems, latent communication has emerged as an efficient alternative to exchanging natural-language messages. By sharing internal representations, agents can avoid repeatedly processing the same context, reducing communication overhead and prefill computation. One such mechanism is cross-model Key-Value (KV) cache transfer, which uses a learned mapper to translate a source model's KV cache into one a target model can...
  </details>

- **2026-11-25** — Jacques Dumora, André-Louis Rochet, Simon Roburin — [Unstable Action Boundaries in Lethal Drone Agents](http://arxiv.org/abs/2611.34121v1)
  <details><summary>📄 Abstract</summary>
  Tool-using large language model (LLM) agents raise safety risks that are not captured by text-only refusal behavior, especially when tools can trigger high-impact actions. This concern is salient in military settings, where autonomous weapons raise the possibility of delegating force decisions to software agents. In this work, we study whether a drone agent's action boundary is stable under changes to the target descriptor. We evaluate recent and popular LLMs in a simulated perception-action pip...
  </details>

- **2026-11-24** — Shivank Rajput, Himanshu Singh, A. V. Subramanyam — [SALSA: Sampling Adversarial Suffixes from Learned Distributions for LLM Safety Assessment](http://arxiv.org/abs/2611.33030v1)
  <details><summary>📄 Abstract</summary>
  Large language models (LLMs) remain vulnerable to jailbreak attacks, where adversaries append optimized suffixes to otherwise benign looking prompts to bypass safety alignment. Existing optimization-based GCG-style attacks can be effective, but they are expensive at inference time, and suffer from poor transfer. We present, SALSA, a generative framework that learns a distribution over jailbreak suffixes from optimization-derived attack corpora. Once trained, the model supports efficient sampling...
  </details>

- **2026-11-24** — Megan Squire — ["I Do Intend to Deliver": Will LLMs Run a Marketplace Advance-Fee Scam?](http://arxiv.org/abs/2611.32957v1)
  <details><summary>📄 Abstract</summary>
  Online fraud is traditionally limited by the cost of the human labor needed to talk to potential victims. We ask whether hosted large language models will now supply that labor. We prompted ten off-the-shelf models to play the seller in the "free item, just pay delivery" advance-fee scam common on buy-and-sell sites, using a plain system prompt with no jailbreak. Each model played 30 conversations against each of four buyer personas, from credulous to guarded, with the same model playing the buy...
  </details>

- **2026-11-24** — Henry Castillo, Yanchen Liu, Claudio Mayrink Verdun et al. — [Steerable by Design: Conditional Pretraining for Robust Control of Language Models](http://arxiv.org/abs/2611.32199v1)
  <details><summary>📄 Abstract</summary>
  Our goal is to build language models that are steerable by design. Today's language models are pretrained with next-token prediction, which relegates alignment and control to the final 1% of training tokens or inference-time interventions. These models repurpose a single input channel for both instructions and data, leading to common failure modes where the model mistakenly treats data as instructions such as intentional jailbreaks and unintentional in-context alignment drift. To correct this, w...
  </details>


### 📂 prompt-injection
*提示注入攻击 / Prompt Injection Attacks* — 9 papers

- **2026-11-25** — Truong Phan, Ngoc-Quan Pham, Dat Quoc Nguyen — [MINE: A Training-Free Defense against Indirect Prompt Injection via Mutual Information and Embedding Variance](http://arxiv.org/abs/2611.34188v1)
  <details><summary>📄 Abstract</summary>
  Existing defenses against indirect prompt injection in retrieval-augmented generation (RAG) are inherently reactive: prompt-engineering methods are often overridden by the injected instructions, while supervised detectors must be retrained for each new attack style. We propose a different paradigm: defend by maximizing relevance, not by detecting attacks. Our method, MINE, is training-free and attack-agnostic, and it also serves as a query-conditioned reranker. To evaluate defenses under realist...
  </details>

- **2026-11-25** — Boyang Ma, Jinku Li, Hao Wu et al. — [The Detour Is the Danger: Preserving Security During LLM Agent Recovery](http://arxiv.org/abs/2611.33605v1)
  <details><summary>📄 Abstract</summary>
  LLM agents increasingly rely on external tools and reusable Skills to execute complex workflows, autonomously replanning when operations fail. However, such recovery may preserve task functionality while silently discarding the security protections required by the original workflow. In this paper, we investigate workflow security downgrade, a failure-induced security threat in which agents execute sensitive operations without satisfying their original protection requirements. Unlike prompt injec...
  </details>

- **2026-11-24** — Newt Hue-Nam K. Nguyen, Jui-Yu Ho, Wei-Han Chen et al. — [AVERT: Anomalous Value Erasure with Response Testing against Visual Prompt Injection](http://arxiv.org/abs/2611.33532v1)
  <details><summary>📄 Abstract</summary>
  Vision Language Models (VLMs) are vulnerable to visual prompt injection, in which an adversarially perturbed image forces the model to respond with the attacker's chosen content, such as malicious tool calls, website links, or advertisements, sometimes regardless of the user's question. Existing defenses, such as diffusion-based purification and image-token masking, mitigate these attacks at a substantial cost to the model's utility on benign inputs. To address this challenge, we propose AVERT, ...
  </details>

- **2026-11-24** — Aymen Noor, Honglu Jiang — [Poisoning Self-Evolving Security Policies in LLM Agents](http://arxiv.org/abs/2611.33385v1)
  <details><summary>📄 Abstract</summary>
  Self-evolving defenses improve LLM-agent security by learning reusable policies from observed attacks. However, we demonstrate that this learning process itself can become an attack surface. Using SED (Self-Evolving Defense) in the AgentDojo benchmark, we construct a single prompt-injection episode that causes the defense to learn an over-broad policy and subsequently refuse legitimate requests. Across 10 Nemotron runs, every poisoned run over-refuses at least one legitimate task, while unrelate...
  </details>

- **2026-11-24** — Jie Li, Chenxu Niu, Tongyang Wang et al. — [Attestation is All You Need: Toward a Zero-Trust Architecture for HPC AI Agents](http://arxiv.org/abs/2611.32958v1)
  <details><summary>📄 Abstract</summary>
  AI agents are beginning to automate data analysis, orchestration, and simulation steering in HPC environments, but they introduce a security problem that existing cluster defenses do not address: the hijacked authorized agent. An adversary can subvert an agent through prompt injection, poisoned shared data, compromised tools, or multi-agent coordination, then exfiltrate sensitive data through legitimate encrypted LLM API traffic. We propose behavioral attestation as a runtime defense for this se...
  </details>

- **2026-11-24** — Wonjune Seo, Minkyung Park, Saerom Park — [ReQOR: Operator-Discrepancy Subspace Repair for Quantization-Conditioned Backdoors in Large Language Models](http://arxiv.org/abs/2611.32755v1)
  <details><summary>📄 Abstract</summary>
  Quantization-Conditioned Backdoors (QCBs) cause large language models (LLMs) to exhibit malicious behavior after quantization while remaining benign at high precision. Existing defenses often rely on security-guided configuration selection or iterative optimization, but do not identify which quantization-induced changes should be repaired. We isolate module-local quantization effects from upstream drift by evaluating the high-precision and quantized versions of each module on identical states fr...
  </details>

- **2026-11-24** — Kailun Yan, Yue Huang, Sisi Duan — [CAPTA: Identifying LLMs Behind AI Agents](http://arxiv.org/abs/2611.32686v1)
  <details><summary>📄 Abstract</summary>
  Large language model (LLM)-based agents access remote services through tools to complete user tasks, often via API calls. In this setting, a remote service may want to identify the backend LLM of an agent to launch model-specific attacks, including prompt injection or selective delivery of manipulated content. However, the service cannot directly query the backend model and must instead collect observable responses through its interactions with the agent, making identification challenging.   In ...
  </details>

- **2026-11-24** — Zeming Fei, Hongming Fei, Yi Xu et al. — [LLM Agent Authorization Across Context Compaction](http://arxiv.org/abs/2611.32194v1)
  <details><summary>📄 Abstract</summary>
  Request-derived authorizers such as Progent protect LLM agents from prompt injection by deriving what an agent may do from the user's request. Their guarantee rests on attribution: the request is taken to be what the user said. Compaction breaks it. At every automatic compaction we observed, Claude Code and Codex placed a model-written summary of earlier turns as a user message, so the compactor's quotation of the user, documents and injected text reads as the user speaking. Because a policy fro...
  </details>

- **2026-11-23** — Yi Han, Zhen Sun, Zhijie Deng et al. — [ContextLure: Exploiting Benign Conversation History for Indirect Prompt Injection](http://arxiv.org/abs/2611.31424v1)
  <details><summary>📄 Abstract</summary>
  As LLMs become more capable, agents can perform more complex tasks with tools and maintain longer interactions with users. These benign conversations contain evidence on task results, user concerns, and operational constraints. The risk is that attackers who can observe benign conversations (evidence) may construct stronger indirect prompt injections without increasing the attackers' control over prior turns or the later injection. However, we still lack a clear study of how effectively attacker...
  </details>


### 📂 tool-use-attack
*工具使用攻击 / Tool-Use Attacks* — 1 papers

- **2026-11-25** — Haozhe Zhang, Zhen Long — [What Does Skill Lift Actually Measure? A Source-Code-Level Audit and Noise-Aware Reanalysis of SkillsBench](http://arxiv.org/abs/2611.33943v1)
  <details><summary>📄 Abstract</summary>
  Agent skills are directories of instructions, reference materials, and scripts loaded on demand by coding agents. According to SkillsBench, although human-curated skills can raise the passing rate by about 16.6 percentage points (pp) on average, they have actually reduced the results for some tasks. Later research has started to gate or eliminate skills according to the above per-task gains. We have audited the above benchmark at the source-code level and analysed 7,554 public trials to form 1,4...
  </details>


### 📂 backdoor
*后门与投毒攻击 / Backdoor & Poisoning Attacks* — 7 papers

- **2026-11-25** — Maximilian Petrowitsch, Ben Connors, Chris Kapulkin — [Reading Fine-Tuning Diffs Through Lenses: Model Diffing for Backdoor Detection](http://arxiv.org/abs/2611.34758v1)
  <details><summary>📄 Abstract</summary>
  We introduce a common scoring system based on token readouts to evaluate weight, activation and output-based model diffing methods for backdoor detection in fine-tuning processes. We also improve existing weight and activation based methods by incorporating the $J$-lens and its refinement, the $J{+}{+}$-lens. We test our setup in experiments where we compare a backdoored model with the base model from which it was fine-tuned. Our results show that incorporating the $J{+}{+}$-lens improves the we...
  </details>

- **2026-11-25** — Ioannis Kalogeropoulos, Giorgos Bouritsas, Yannis Panagakis — [Hierarchical Graph Metanetworks](http://arxiv.org/abs/2611.34726v1)
  <details><summary>📄 Abstract</summary>
  The emerging field of weight space learning has demonstrated the potential to enable metanetworks, i.e. models that process neural network (NN) data, to support several steps of the machine learning lifecycle, from model optimisation to evaluation and adaptation. However, this potential has yet to materialise beyond small-scale MLPs or CNNs: most current models, including message-passing based graph metanetworks (GMNs), operate exclusively at the finest level of granularity, processing every neu...
  </details>

- **2026-11-25** — Santosh Chapagain, Shah Muhammad Hamdi, Soukaina Filali Boubrahimi — [Trigger-Invariant Contrastive Unlearning for Backdoor Removal](http://arxiv.org/abs/2611.33571v1)
  <details><summary>📄 Abstract</summary>
  Backdoor attacks pose a severe threat to modern NLP models by embedding hidden triggers that induce malicious behavior at inference time. Recent unlearning methods such as gradient ascent (GA) attempt to remove backdoors by maximizing the loss on poisoned samples; however, these methods can suffer from a critical limitation: they may shift the trigger's influence to other classes rather than eliminating it. In this work, we propose Trigger-Invariant Contrastive Unlearning (TICU), a framework for...
  </details>

- **2026-11-24** — Yage Zhang, Yukun Jiang, Ziqing Yang et al. — [Anti-AI in the Wild: From Toxic Discourse to Action](http://arxiv.org/abs/2611.33254v1)
  <details><summary>📄 Abstract</summary>
  Online discussion of generative AI has become increasingly contentious, and communities devoted to supporting, opposing, or debating AI have emerged on social media. Some of these communities take anti-AI actions, such as deploying crawler tarpits and data-poisoning services to interfere with data collection and model training. Yet, the scope of these actions and their relationship to online discourse remain poorly understood. In this paper, we present the first measurement study of online confl...
  </details>

- **2026-11-24** — Guowei Guan, Yurong Hao, Jiaming Zhang et al. — [C3H: Compression-to-Consensus Criteria Hijacking in Multimodal LLM Recommender Systems](http://arxiv.org/abs/2611.32780v2)
  <details><summary>📄 Abstract</summary>
  Multimodal large language models (MLLMs) are transforming recommender systems into content-aware decision systems. In these systems, multimodal compression and cross-modal fusion are often viewed as robustness-enhancing mechanisms against content manipulation, as compression can filter noisy signals and cross-modal consensus can suppress inconsistent anomalies. We challenge this assumption by showing that the same process can expose a compression-to-consensus (C2C) bias in ranking decisions. Sig...
  </details>

- **2026-11-24** — Guowei Guan, Yurong Hao, Jiaming Zhang et al. — [C3H: Compression-to-Consensus Criteria Hijacking in Multimodal LLM Recommender Systems](http://arxiv.org/abs/2611.32780v1)
  <details><summary>📄 Abstract</summary>
  Multimodal large language models (MLLMs) are transforming recommender systems into content-aware decision systems. In these systems, multimodal compression and cross-modal fusion are often viewed as robustness-enhancing mechanisms against content manipulation, as compression can filter noisy signals and cross-modal consensus can suppress inconsistent anomalies. We challenge this assumption by showing that the same process can expose a compression-to-consensus (C2C) bias in ranking decisions. Sig...
  </details>

- **2026-11-24** — Sirui He, Chi Zhang — [ADE: A Zero-Training Unlearning Method for Latent World Models](http://arxiv.org/abs/2611.31998v1)
  <details><summary>📄 Abstract</summary>
  Latent world models learn compact recurrent dynamics from offline trajectories, yet deployed simulators can retain backdoor triggers or stale transitions from outdated physical regimes. Existing unlearning methods fail in autoregressive physics: gradient updates distort latent manifolds and compound rollout drift, naive output zeroing suppresses valid control responses on trigger onset, and single-step deletion leaves corruption inside recurrent hidden states. We propose Analytical Dynamics Exci...
  </details>


### 📂 adversarial-attack
*对抗攻击 / Adversarial Attacks* — 5 papers

- **2026-11-25** — Nian Ai, Guangke Chen, Xiaowen Cai et al. — [Attacking Hard-Label Large Vision-Language Models with Model-Sensitive Adversarial Patch Designs](http://arxiv.org/abs/2611.34467v1)
  <details><summary>📄 Abstract</summary>
  Large vision-language models (LVLMs) have demonstrated impressive capabilities in handling multi-modal downstream tasks, gaining increasing popularity. However, recent studies show that LVLMs are susceptible to both intentional and inadvertent attacks. Existing attackers ideally optimize adversarial perturbations with backpropagated gradients from LVLMs, thus limiting their scalability in practical scenarios as real-world LVLM applications will not provide any LVLM's gradient or details. Motivat...
  </details>

- **2026-11-25** — Yilong Yang, Jiale Teng, Yule Liu et al. — [Hijacking 3D Generation: Targeted Adversarial Attacks against Image-to-3D Models via Prefix Trajectory Alignment](http://arxiv.org/abs/2611.34075v1)
  <details><summary>📄 Abstract</summary>
  Online services that deploy Image-to-3D models enable users to generate high-quality 3D assets from a single image. However, the generated 3D geometry can violate content policies and cause broader security risks. To prevent such content, these services typically use policy-restricted inspectors to examine uploaded images before generation. Since the inspector examines only the visible content of the input, a visually benign image can still induce the generation of policy-restricted 3D geometry....
  </details>

- **2026-11-24** — Haz Sameen Shahgir, Ali Asif Khan, K. M. Mehemud Azad et al. — [Beyond Random Starts: Amortized Initialization for Adversarial Attacks on Vision-Language Models](http://arxiv.org/abs/2611.33414v1)
  <details><summary>📄 Abstract</summary>
  Gradient-based transferable adversarial attacks achieve state-of-the-art attack success rates against black-box vision-language models (VLMs). However, they require hundreds of costly optimization steps for each image pair. One possible reason is that these attacks typically start from random perturbations that contain no information about the source or target image. In this work, we study whether amortized adversarial generation can provide better initializations for gradient-based attacks. By ...
  </details>

- **2026-11-24** — Tigran Fahradyan, Riccardo Ali, Sergio Calvo-Ordoñez et al. — [Understanding the Importance of Massive Activations through Adversarial Robustness](http://arxiv.org/abs/2611.32585v1)
  <details><summary>📄 Abstract</summary>
  A common occurrence in Large Language Models (LLMs) is the emergence of so-called massive activations. This phenomenon is well known in the literature and has been connected to attention sinks, representational compression, as well as signal propagation. However, the reasons and consequences for their appearance are not yet well understood. In this paper, we explain the role of massive activations in deep learning by showing that they are connected to the region migration phenomenon in delayed r...
  </details>

- **2026-11-23** — Adam Wróbel, Jacek Tabor, Bartosz Zieliński et al. — [Spec$^2$R: Recovering Emergent Properties in Supervised Vision Transformers](http://arxiv.org/abs/2611.31589v1)
  <details><summary>📄 Abstract</summary>
  Vision Transformers (ViTs) have achieved strong performance across computer vision tasks, but the quality of their learned representations differs drastically depending on the training paradigm. While self-supervised ViTs often demonstrate emergent properties, such as object-aligned patch representations and attention maps, supervised ViTs typically lack these properties, even when trained with strong data augmentations. Understanding the origin of this difference is important for explaining and...
  </details>


### 📂 privacy-leakage
*隐私泄露 / Privacy Leakage* — 28 papers

- **2026-11-25** — Peizhuo Lv, Tao Chen, Mengya Shi et al. — [AgentLens: Graph-guided Security Auditing for LLM-based Agents](http://arxiv.org/abs/2611.34380v1)
  <details><summary>📄 Abstract</summary>
  LLM-based agents are emerging as a key paradigm for automating software engineering by coupling LLM-driven decision-making with external tools, files, APIs, and execution environments. However, weaknesses in agent implementations and insecure interactions between the agent and external resources can lead to severe consequences, including remote code execution, arbitrary file access, SQL injection, and data leakage. This makes pre-deployment auditing essential for systematically identifying imple...
  </details>

- **2026-11-25** — Qihao Lin, Guanxu Chen, Shuhang Zheng et al. — [$μ$-Bench: Benchmarking Multi-User Task Completion in Shared Interaction Voice Agents](http://arxiv.org/abs/2611.34920v1)
  <details><summary>📄 Abstract</summary>
  Voice agents in shared spaces must satisfy interdependent multi-user requests while upholding per-user authority, privacy, and task constraints. Existing evaluations offer limited coverage when participants react throughout a session. We introduce $μ$-Bench, a benchmark for joint task completion in closed-loop, full-duplex multi-user voice interaction. Simulated participants act from isolated profiles of goals, knowledge, and permissions, adapting to the agent's speech and tool outcomes. Across ...
  </details>

- **2026-11-25** — Joy Bose, Srinivas Adyapak — [A Survey of Security, Privacy, and Ethics of Large Language Models in Telecom](http://arxiv.org/abs/2611.34868v1)
  <details><summary>📄 Abstract</summary>
  Large Language Models (LLMs) are increasingly integrated into telecommunications for customer service, network analytics, and operational support. While offering efficiency and innovation, their deployment raises critical privacy, security, and ethical challenges due to the uniquely sensitive and longitudinal nature of telecom data. This paper presents a survey of LLM risks and safeguards in telecom context. Our survey introduces a telecom-specific taxonomy linking privacy, security, and ethics ...
  </details>

- **2026-11-25** — Truyen T. Le, Vinh Dang Ngoc, Thai Bao Huynh — [An Embedded Ergonomic Posture Monitoring and AI-Assisted Home Learning System on a Raspberry Pi 3B Edge Platform](http://arxiv.org/abs/2611.34669v1)
  <details><summary>📄 Abstract</summary>
  During independent home study sessions, students frequently sustain improper sitting postures, accumulate excessive sedentary hours, and experience productivity loss from off-task digital distractions. Furthermore, learners often lack real-time pedagogical scaffolding for demanding self-study curricula. To mitigate these ergonomic and instructional challenges, this paper presents an affordable, privacy-preserving cyber-physical embedded system for domestic study spaces. Engineered on a Raspberry...
  </details>

- **2026-11-25** — Yaser Kord, Moritz Hess — [Train-Only-Constrained LM for Synthetic Clinical Trajectories: Leak-Safe Calibration and Auditable Dynamics](http://arxiv.org/abs/2611.34258v1)
  <details><summary>📄 Abstract</summary>
  Simulating clinical time series necessitates temporal realism, calibration that preserves model integrity, and privacy transparency. We present a train-only, constrained language-model pipeline that factorizes generation. A compact GPT-style language model learns cross-biomarker co-occurrence through quantile tokens, and temporal directions are enforced by 3x3 per-biomarker Markov transitions fit on TRAIN, allowing dynamics to be audited. We fit a monotone quantile map (QMap) on TRAIN only (SYN(...
  </details>

- **2026-11-25** — Zhen Xu, Beata Beigman Klebanov, Jamie N. Mikeska — [Too Smart for Its Own Good? Cognitive Fidelity and Competence Leakage in LLM Simulations of Young Learners](http://arxiv.org/abs/2611.34042v1)
  <details><summary>📄 Abstract</summary>
  LLM-based interactive learner simulators are increasingly used in educational applications, including teacher training and tutoring system development. A critical requirement for those simulations is cognitive fidelity: the simulated learner should maintain the assigned knowledge, misconceptions, and reasoning procedures throughout interaction. However, LLMs may express knowledge or problem-solving skills beyond the assigned learner's cognitive status, a phenomenon we refer to as competence leak...
  </details>

- **2026-11-24** — Chun Xie, Itaru Kitahara — [StyleID++: Position-Decoupled and Structure-Coherent Style Retrieval across Diffusion Architectures](http://arxiv.org/abs/2611.33323v1)
  <details><summary>📄 Abstract</summary>
  Attention injection offers a remarkably simple route to training-free style transfer: content queries retrieve style keys and values inside a pretrained diffusion model. We show that this operation also creates an overlooked failure mode. Position signals that are useful within one image become a spurious shared coordinate system across two spatially unrelated images, causing content tokens to favor style tokens at similar coordinates. This cross-image positional leakage appears in both convolut...
  </details>

- **2026-11-24** — Jian Li, Qinglin Zhao, Shuoyao Wang et al. — [Fresh Keys, Stale Secrets: Numeric Leakage across Linked LLM Prompts](http://arxiv.org/abs/2611.32864v1)
  <details><summary>📄 Abstract</summary>
  Small businesses repeatedly ask cloud language models about the same confidential prices, unit costs and margins. Numeric prompt disguises for such numbers are evaluated one prompt at a time, but a provider sees a firm's history, in which each fresh secret gives a new, independent view of the same numbers. Since real costs are not public, we measure on synthetic firms with known values how much an honest-but-curious provider recovers when it knows the disguise algorithm, holds sector-level price...
  </details>

- **2026-11-24** — Hatef Otroshi Shahreza — [Red-Teaming a Sovereign LLM, Its Reasoning and Its Training Stages](http://arxiv.org/abs/2611.32710v1)
  <details><summary>📄 Abstract</summary>
  Open-weight large language models (LLMs) are increasingly deployed for applications with sensitive information. We investigate whether confidentiality instructions in system prompt can protect such information. We red-team Apertus v1.5, an open sovereign LLM, and five other model families across six languages and reasoning modes. We use synthetic personal records to evaluate direct disclosure, correction baits, yes/no verification, derived-value queries, reasoning leakage and authorisation check...
  </details>

- **2026-11-24** — Pedram Zaree, Kleomenis Katevas, Vandana Rajan et al. — [Query-Guided Visual Minimization for Selective Disclosure to Cloud VLMs](http://arxiv.org/abs/2611.32302v1)
  <details><summary>📄 Abstract</summary>
  Cloud-hosted vision-language models (VLMs) require sending images beyond the user's local trust boundary, potentially exposing sensitive information the query does not need. We study query-guided visual minimization: a trusted local transformation preserves query-relevant visual content and reduces unnecessary disclosure before transmission. Unlike query-agnostic anonymization, it preserves the same sensitive content when the query requires it and suppresses it otherwise. We introduce QGVM, a fr...
  </details>

- **2026-11-24** — Mark Farinas, Alesandra Garcia, Maria Reyes et al. — [Unjamming Deferrals: Supporting Students Through JAMN Bot, a Mobile RAG-Grounded Policy Assistant](http://arxiv.org/abs/2611.32266v1)
  <details><summary>📄 Abstract</summary>
  In some educational institutions, workflows such as the exam deferral process can be slow, inconvenient, and inconsistent, which creates the need to implement novel digital systems. This paper presents Schedulater, a mobile app for managing university exam deferrals. JAMN Bot is a Large Language Model (LLM)-powered chatbot integrated into Schedulater that provides context-aware support to help users understand the deferral process. The system features a Retrieval-Augmented Generation (RAG) pipel...
  </details>

- **2026-11-24** — Rajarshi Chattopadhyay, Chen-Khong Tham — [Multi Agent Reinforcement Learning enhanced Federated Learning for Predicting Remaining Useful Lifetime](http://arxiv.org/abs/2611.31880v1)
  <details><summary>📄 Abstract</summary>
  Remaining useful life (RUL) prediction is central to Prognostics and Health Management (PHM). The growth of industrial IoT has unlocked large multivariate sensor streams and enabled deep models - especially Transformers - for long-horizon sequence learning. However, transformers are parameter-heavy and data-hungry, while operational datasets are often siloed and privacy-sensitive. Federated Learning (FL) addresses this by training across clients without raw data sharing, but in practice many cli...
  </details>

- **2026-11-24** — Asma Farajidizaji, Vyas Raina, Vatsal Raina et al. — [SwarmLeak: Does Coordination Improve Privacy Attacks on LLM Agents?](http://arxiv.org/abs/2611.31791v1)
  <details><summary>📄 Abstract</summary>
  LLM agents increasingly collaborate in group chats while holding tool access to confidential records, which makes the shared chat an attack surface. It remains unclear whether several colluding attackers extract such information more effectively than one. We introduce SwarmLeak, a red-teaming dataset of 24 synthetic group-chat scenarios across healthcare, law, finance, and software engineering, where attackers pose as colleagues to make a victim agent post protected fields despite an explicit co...
  </details>

- **2026-11-24** — Georgios Politis, Evangelos Pappas — [Separating Measurement Failures from Defence Failures in Split Language-Model Privacy](http://arxiv.org/abs/2611.31752v1)
  <details><summary>📄 Abstract</summary>
  Split-training privacy evaluations fail through distinct mechanisms. Evaluators can overlook an exposed gradient channel, align reconstructions against shifted labels, or deploy uncalibrated probes before testing a candidate defence, while calibrated attacks can also refute real defences. Separating these failure modes alters which claims survive. We conduct a retrospective evidentiary reanalysis across four split-LLM campaigns and two cross-cutting scope checks covering host key custody and var...
  </details>

- **2026-11-24** — Hanjing Ye, Tianle Zeng, Jianwei Peng et al. — [Follow-Bench 2.0: An End-to-End 3D Benchmark for Socially-Aware Robot Person Following](http://arxiv.org/abs/2611.32579v1)
  <details><summary>📄 Abstract</summary>
  Socially-aware robot person following (RPF) requires a mobile robot to follow a designated person in dynamic human environments while maintaining target identity, avoiding obstacles and pedestrians, and preserving socially comfortable formations. Existing benchmarks only partially evaluate this coupled problem: embodied visual tracking benchmarks emphasize target visibility with limited social interaction, person re-identification benchmarks study perception without closed-loop control, and moti...
  </details>

- **2026-11-24** — Yicheng Huang, Feng Ke, Linhan Chen et al. — [PhysRF-WorldJEPA: Transforming Heterogeneous Large Language Models into Manifold-Decoupled Millimeter-Wave Radar World Models](http://arxiv.org/abs/2611.32113v1)
  <details><summary>📄 Abstract</summary>
  Adapting Large Language Models (LLMs) to millimeter-wave (mmWave) radar enables privacy-preserving, all-weather physical scene understanding across darkness, smoke, and walls. However, standard instruction tuning treats continuous radar streams as static text-like tokens, causing near-random global radar-to-text retrieval and severe physical drift under sensor blackouts. Conversely, coupling pairwise contrastive losses (e.g., SigLIP) directly into the shared backbone improves retrieval but injec...
  </details>

- **2026-11-24** — Dongyu Cui, Jie Ding, Xuan Bi — [Structure-Aware Transformers for Hierarchical Authorization in Personal AI Agents](http://arxiv.org/abs/2611.32018v1)
  <details><summary>📄 Abstract</summary>
  Personal AI agents can carry out complex, multi-step tasks on users' behalf, but doing so often involves numerous permission requests. Manually reviewing each request is time-consuming, while indiscriminate approval poses privacy and security risks. Predicting users' authorization preferences offers a way to reduce this burden while preserving user control. However, authorization prediction is challenging because permission requests are often hierarchical and observed user decisions are sparse a...
  </details>

- **2026-11-24** — Scott Piersall, Yang Gao, Shenyang Liu et al. — [MetaFORGE: A Meta-Learning Framework for Harness Optimization in Automated Code Generation for Parallel Computing](http://arxiv.org/abs/2611.33119v1)
  <details><summary>📄 Abstract</summary>
  Large language models (LLMs) can generate parallel programs, but their correctness and performance depend strongly on the instructions that guide generation. We present \textsc{MetaFORGE}, an execution-grounded meta-learning framework that iteratively optimizes persistent natural-language skill specifications for MPI C code generation. \textsc{MetaFORGE} combines correctness testing, compiler diagnostics, static-analysis findings, runtime measurements, and rank-level load-imbalance profiles into...
  </details>

- **2026-11-24** — Saket Gollapudi, Elisa Bertino, Sewoong Oh — [Understanding Clipping In Zeroth-Order Optimization](http://arxiv.org/abs/2611.33062v1)
  <details><summary>📄 Abstract</summary>
  Zeroth-order optimization has emerged as a resource-efficient alternative to Stochastic Gradient Descent (SGD) when fine-tuning LLMs, thanks to the inherent low dimensionality of the loss landscape. It relies on a two-point estimate of the gradient that only accesses the function value and not the gradient, bypassing the resource-heavy backpropagation. Recently, it was accidentally discovered that per-sample clipping can improve the performance of the trained model, while running a differentiall...
  </details>

- **2026-11-24** — Truong-Thanh Le, Hoang-Loc La, Amir Taherkordi et al. — [Scalable Placement for Disaggregated LLM Serving on Heterogeneous Edge Fleets](http://arxiv.org/abs/2611.32881v1)
  <details><summary>📄 Abstract</summary>
  Serving large language models (LLMs) at the edge is increasingly desirable for privacy-sensitive applications and scenarios that require data to remain on local devices. However, edge environments are constrained by limited computational resources and exhibit substantial device heterogeneity, making efficient LLM serving challenging. These limitations become particularly pronounced under bursty demand, where congestion and queue buildup can significantly increase response latency. Replicating th...
  </details>

- **2026-11-24** — Kosuke Fujita, Daiki Nishiyama, Jun Sakuma — [Privacy Disclosure Control Benchmark (PDC-Bench): How Faithfully Do LLMs Keep Privacy Constraints on In-Context Disclosure Granularity?](http://arxiv.org/abs/2611.32610v1)
  <details><summary>📄 Abstract</summary>
  In LLM task execution, a constraint on the permitted disclosure granularity of personal attributes is sometimes imposed on the output. For example, if a person's private attribute is their location (San Francisco) and disclosure is permitted only at the country level, an output at the state level (California) violates the constraint. Detecting such violations requires capturing not only direct privacy leakage (San Francisco) but also semantic leakage (California). However, existing benchmarks ca...
  </details>

- **2026-11-24** — Liu Wang, Tianshu Zhou, Haoyu Wang et al. — [SCOPE: Evaluating and Enhancing Permission Explanation Transparency in Mobile Apps](http://arxiv.org/abs/2611.32122v1)
  <details><summary>📄 Abstract</summary>
  Permission explanations, explanatory text accompanying mobile app permission requests, are crucial for user privacy transparency and informed consent. Despite their importance, current practices often fall short of regulatory expectations due to the lack of systematic evaluation mechanisms. Through an empirical study of 600 mainstream mobile apps, we reveal widespread deficiencies: 15\% of permission requests provide no explanation, others use vague language or technical jargon, and critically, ...
  </details>

- **2026-11-24** — Fangzhou Lin, Shuo Xing, Xin Li et al. — [Contrastive On-Policy Self-Distillation for LLM Unlearning](http://arxiv.org/abs/2611.31932v1)
  <details><summary>📄 Abstract</summary>
  Large language model unlearning aims to remove the influence of designated training data while preserving unrelated model capabilities. Existing likelihood-based methods commonly optimize against fixed forget sequences, providing only negative supervision on what the model should not generate and overlooking the states visited by the evolving unlearned policy. We introduce Contrastive On-Policy Self-Distillation (CPSD), a new unlearning framework that constructs an explicit knowledge-reduced tar...
  </details>

- **2026-11-23** — Aymen Noor, Ke Lyu, Honglu Jiang — [Frequency-Conditioned Privacy Auditing of Fine-Tuned Language Models](http://arxiv.org/abs/2611.31581v1)
  <details><summary>📄 Abstract</summary>
  Large language models are increasingly fine-tuned on sensitive data, where the same person's information may appear multiple times across records. This can cause models to memorize sensitive information, but memorization does not necessarily mean that the information can be recovered. A more serious privacy risk arises when the model begins to reproduce that information during generation. In this paper, we study how often sensitive information must appear in the fine-tuning data before it become...
  </details>

- **2026-11-23** — S. Kawa Atapour, S. Jamal Seyedmohammadi, Maryam Hosseini et al. — [ECLIPSE: Embedding-Centered Foundation-Model Federated Knowledge Transfer for Data-Free Edge Intelligence](http://arxiv.org/abs/2611.31527v1)
  <details><summary>📄 Abstract</summary>
  Foundation Models (FMs) are envisioned to become an integral component of intelligent federated edge networks because of their strong representation and generalization capabilities. However, their integration into resource-constrained and privacy-sensitive edge environments remains challenging. This challenge is particularly pronounced in data-free settings, where no shared, public, or server-accessible reference dataset is available to establish a common reference space for aligning distributed...
  </details>

- **2026-11-23** — Venkata Muttineni, Karthik Narayan, Christopher David — [Leaks by Installments: Cross-Session Answer Disclosure in LLM Tutors and a Ledger-Based Defense](http://arxiv.org/abs/2611.31429v1)
  <details><summary>📄 Abstract</summary>
  Tutors built on large language models (LLMs) are told not to give away answers, but a learner does not have to ask for the answer all at once. Existing safeguards judge each reply within the current conversation, so a learner can open a new session, reword the problem, or request a worked solution to the same problem with different numbers. We call this cross-session disclosure and propose a defense: a persistent, per-learner disclosure ledger. For every problem a learner brings, the system buil...
  </details>

- **2026-11-23** — Yuhan Bian, Zhaokai Liang, Jia Wang et al. — [What People Choose Not to Say: A Multimodal Benchmark for Fine-Grained Information Manipulation in Conversations](http://arxiv.org/abs/2611.31346v1)
  <details><summary>📄 Abstract</summary>
  Recent advances in MLLMs have improved social understanding, enabling models to recognize emotions and distinguish truthful from deceptive behaviors. However, existing benchmarks largely focus on coarse-grained emotion recognition or binary truth-deception detection, overlooking the diverse ways people manipulate information in conversations, such as withholding, leakage, fabrication, evasion, and defensive counterclaim. Understanding these behaviors requires reasoning about underlying facts, pa...
  </details>

- **2026-11-23** — Nader Lobandi, Mohammad Mehdi Hosseini, Lombe Chileshe et al. — [E-Waste-Bench: A Large-Scale Benchmark for Visual Triage of Data-Center Hardware](http://arxiv.org/abs/2611.31703v1)
  <details><summary>📄 Abstract</summary>
  Retired data-center hardware can often be refurbished or resold, but triage demands more than object categories. A model must tell visually similar parts apart, judge condition under damage and occlusion, and read the printed part number. We audit nine public e-waste collections. They cover mostly consumer devices (only 10% of images are labeled as a data-center part), label neither condition nor printed text, and contain 42% exact or augmented duplicates. We introduce E-Waste-Bench, 328K photog...
  </details>


### 📂 steganography
*隐写与隐蔽通信 / Steganography & Covert Communication* — 2 papers

- **2026-11-25** — Jinwei Hu, Lai Wei, Zhuoyun Li et al. — [VisualMontage: Manipulating the Beliefs of Vision-Language Agents with Authentic Image Sequences](http://arxiv.org/abs/2611.34603v1)
  <details><summary>📄 Abstract</summary>
  As agents based on vision-language models (VLMs) increasingly interpret social-media content, errors in their analysis may lend credibility to rumors and amplify their spread. In this paper, we study the problem of visual cognitive collusion, in which coordinated posts combine authentic images and locally faithful captions to induce VLM agents to infer and accept attacker-chosen target claims through their own reasoning. To enable systematic evaluation of this cognitive threat, we introduce a ne...
  </details>

- **2026-11-25** — Haochen Luo, Jie Fu, Mukai Li et al. — [PROVE: Mitigating Long-Horizon LLM Collusion with Reinforcement Learning from Verified Evidence](http://arxiv.org/abs/2611.34215v1)
  <details><summary>📄 Abstract</summary>
  When LLM agents verify each other's work over a long interaction, they drift into collusion: they come to accept work without the evidence that the verification protocol requires. Collusion is absent at the start and builds up episode by episode, which we trace to accurate feedback accumulating in memory. An agent that follows the rule is told that its verdict was wrong whenever its peer was right, so breaking the rule is the reward-maximizing choice, and agents talk themselves into it in their ...
  </details>


### 📂 misuse
*滥用与误用 / Misuse & Abuse* — 15 papers

- **2026-11-25** — Jiaming Luo, Jiacheng Ji, Haoan Jin et al. — [VulnSafe: Measuring Vulnerability-Aware Relational Safety in Large Language Models](http://arxiv.org/abs/2611.34819v1)
  <details><summary>📄 Abstract</summary>
  Emotionally supportive interactions require large language models not only to avoid overtly harmful content, but also to recognize vulnerability-related risk, regulate their relational stance, preserve user agency, and provide context-appropriate support. Existing safety benchmarks often measure isolated violations, leaving unclear what underlying response competence their scores represent. We introduce VulnSafe, a Chinese capability assessment centered on Vulnerability-Aware Response Competence...
  </details>

- **2026-11-25** — Ashkan Golgoon, Giacomo Domeniconi, Samuel Atkins et al. — [From Prediction to Decision: Decision-Focused Fine-Tuning of Autoregressive Tabular Transformers for Cost-Sensitive Financial Events](http://arxiv.org/abs/2611.34858v1)
  <details><summary>📄 Abstract</summary>
  Autoregressive transformers trained on tokenized tabular event streams are a simple and strong baseline for predicting financial events such as fraud. Yet institutions do not act on probabilities; they act on decisions whose consequences are asymmetric and heteroscedastic: the cost of a missed high-value fraud and that of a wrongly declined small purchase are not the same. The standard bridge is post-hoc Bayes-optimal thresholding of calibrated probabilities under a cost matrix. We ask whether f...
  </details>

- **2026-11-25** — Jinkun Zhao, Wenjun Wu — [TASK Memory: Beyond Text-Only Memory with Activation Steering and Knowledge Editing against Memory Hallucination](http://arxiv.org/abs/2611.34762v1)
  <details><summary>📄 Abstract</summary>
  LLM agents increasingly rely on external memory, yet they still hallucinate about what they remember. Often the correct memory is retrieved and placed in the prompt, but the answer contradicts it or the memory is applied to the wrong question. We call these use-time memory hallucinations. Across five open models, we find that they arise from the conflict between parametric knowledge and external memory and take three forms: memory-ignoring, where the model returns to a stale fact in its weights ...
  </details>

- **2026-11-25** — Adhwaa Al-Chaab, Ayman Younis, Dario Pompili — [SlicePlanner: Logic-Guided Agentic AI for Online QoS-Aware Network Slicing in Open RAN](http://arxiv.org/abs/2611.33664v1)
  <details><summary>📄 Abstract</summary>
  Adaptive network slicing in Open Radio Access Network (O-RAN) demands reconfiguration decisions that respond to live traffic conditions while remaining safe with respect to Service Level Agreement (SLA) constraints, a combination that purely data-driven controllers cannot reliably guarantee without continuous retraining. We present SlicePlanner, a logic-guided closed-loop framework that treats each RAN reconfiguration as a controlled hypothesis: proposed from live and historical KeyPerformance I...
  </details>

- **2026-11-25** — Zitian Guo, Chen Xu, Beibei Li et al. — [Welfare-Enhancing Mechanism Design for Agent Ecosystems](http://arxiv.org/abs/2611.33627v1)
  <details><summary>📄 Abstract</summary>
  The emerging Agentic Web forms a multi-agent ecosystem: a decentralized service market where the user agent selects which content agents to query from their submitted profiles, before seeing any documents. Profiles therefore become a new target of optimization. Existing Generative Engine Optimization studies how a single supplier rewrites documents the engine can already retrieve, to improve their citation. In the Agentic Web, multiple content agents optimize profiles to compete for limited oppo...
  </details>

- **2026-11-24** — Zhi Yang, Junzhou Chen, Jindong Wang — [Streaming Tax: Can Streaming VLMs Replace Their Offline Parents?](http://arxiv.org/abs/2611.33474v1)
  <details><summary>📄 Abstract</summary>
  Most vision-language models (VLMs) specialize in offline video understanding; in contrast, their post-trained versions, streaming VLMs, can perform live interactions. We investigate whether streaming VLMs can replace their offline parent models on offline tasks. Such replacement could reduce deployment costs and improve efficiency. We propose Streaming Tax to systematically evaluate streaming VLMs on offline tasks. Our exploration spans three core dimensions: understanding, trustworthiness, and ...
  </details>

- **2026-11-24** — Catarina Botelho, António Farinhas, John Mendonça et al. — [What, Who, and When: Structured Harm Assessment for Mental Health Safety via Short Reasoning](http://arxiv.org/abs/2611.33263v1)
  <details><summary>📄 Abstract</summary>
  The growing use of large language models (LLMs) for mental health support raises important safety concerns. Existing guard models primarily identify categories of harmful content, often overlooking the context needed to determine an appropriate response. We introduce a clinically grounded taxonomy that characterizes harm along three dimensions: what the harm is, who is involved, and when it occurs. It further separates harm characterization from intervention decisions, thus enabling safety polic...
  </details>

- **2026-11-24** — Yuzhou Chen, Licheng Pan, Zhixuan Chu et al. — [ExpGuard: Guarding Long-Horizon LLM Agents against Corrupted Experience](http://arxiv.org/abs/2611.32085v1)
  <details><summary>📄 Abstract</summary>
  Long-horizon large language model (LLM) agents distill past trajectories into reusable experiences. Misleading or adversarial guidance in source trajectories can corrupt these experiences, allowing harmful instructions to persist across tasks and influence future agent actions. Assessing the risks of potentially corrupted experiences poses three challenges: (1) modeling provenance and execution dependencies before experience reuse, (2) learning task-conditioned risk from trajectory outcomes, and...
  </details>

- **2026-11-24** — Niloofar Ranjbar, Saeedeh Momtazi, Mohammad Mehdi Homayounpoor — [Gated Concept Adapters: Layer-Wise Concept Bottlenecks for Auditable Text Understanding](http://arxiv.org/abs/2611.32600v1)
  <details><summary>📄 Abstract</summary>
  Human-facing text understanding systems are used to infer affect, moderate harmful content, and support socially sensitive decisions. However, Transformer predictions are difficult to audit because they are produced from high-dimensional hidden states that do not provide a compact, inspectable interface for human analysis or intervention. We introduce Gated Concept Adapters (GCA), a layer-wise concept bottleneck framework that attaches gated, low-dimensional concept-producing readout adapters to...
  </details>

- **2026-11-24** — Iliyan Zarov, Henry Course, Anthony Hartshorn et al. — [Avalon-M1: Reinforcement Learning from Collective Rewards](http://arxiv.org/abs/2611.32539v1)
  <details><summary>📄 Abstract</summary>
  We introduce reinforcement learning from collective rewards (RLCR), a recipe for jointly training language models to act as agent organisations under latency constraints. A CEO and up to eight specialists share one policy, co-ordinate through a message board and workspace, and are trained with a common outcome-derived advantage. The deadline makes parallel work valuable when it increases the return earned before the cap. We train Avalon-M1-Mini (120B) across 147 environments. For the trained mod...
  </details>

- **2026-11-24** — Haoyuan Li, Gangyi Zhang, Dong Wang et al. — [Evolve to Learn: Gradient-aligned experience evolution for model self-improvement](http://arxiv.org/abs/2611.32390v1)
  <details><summary>📄 Abstract</summary>
  Self-evolving language models can continuously acquire useful experience through test-time interaction, reflection, and prompt optimization, yet turning such experience into model itself to ensure self improvement remains challenging. On-policy self-distillation (OPSD) provides a natural mechanism for internalizing test-time information into model parameters, yet it largely assumes that the gener- ated experience is worth learning. We show that this assumption does not always hold: experiences t...
  </details>

- **2026-11-24** — Tanzeel Abbas, Tehseen Zia, David Windridge — [Measurement Artifacts in Trustworthiness Evaluations of Quantized Small Language Models](http://arxiv.org/abs/2611.32848v1)
  <details><summary>📄 Abstract</summary>
  Evaluations of quantized language models attribute the change in a benchmark score to quantization. We write the measured change as the true change plus a term contributed by the instrument. Instrument error that is the same at every precision can shrink a paired comparison but cannot create or reverse an effect. Error that interacts with quantization can do both, and it is reported as an effect of quantization. We estimate this interaction for four measurement choices in 8 instruction-tuned mod...
  </details>

- **2026-11-23** — Paul Deepakraj Retinraj — [Scoring Recovery-Time Agent Security: Proposals, Effects, and Retry Instructions](http://arxiv.org/abs/2611.31318v1)
  <details><summary>📄 Abstract</summary>
  A timed-out tool write may be absent, committed, or still in flight. Evaluating an agent only on whether its goal exists can hide harmful recovery actions: auditing 12 supplied traces changes apparent completion from 10/12 to 8/12. We introduce an executable evaluation that separately records tool proposals, runtime decisions, and committed effects. In 3,456 model episodes, the original task wording produces only 39/576 valid recoveries when the initial write is absent; a combined clarification ...
  </details>

- **2026-11-23** — Zhixuan Ge, Anqi Li, Kexin Geng et al. — [Lit Up but Not Needed: Scoped Lesions Show Where Multimodal Mixture-of-Experts Depend on Their Experts](http://arxiv.org/abs/2611.31576v1)
  <details><summary>📄 Abstract</summary>
  Cognitive neuroscience learned that an activation map is not a map of necessity. Regions that light up during a task are not always needed for it, and only lesions reveal which ones are. Mixture-of-experts (MoE) vision-language models come with an activation map for free, since the router records which experts respond to image and text tokens, and recent work reads modality-specialized experts off this map. We bring the lesion. In Qwen3-VL-30B-A3B, Kimi-VL-A3B and Gemma-4-26B-A4B, 3 to 12% of th...
  </details>

- **2026-11-23** — Artem Trofimov, Boris Novikov — [Agent Recovery Gone Wrong: Measuring Harm Beyond Duplicate Calls](http://arxiv.org/abs/2611.31554v1)
  <details><summary>📄 Abstract</summary>
  Code-executing LLM agents submit blocks of code that issue several API writes. If a block fails after some of its writes have taken effect, the agent rewrites the block and continues. It is unknown how often such a recovery harms the external state when the failure occurs naturally in the code written by the agent. In this paper, we measure it on recorded trajectories of AppWorld agents. In a stratified random sample of 200 candidate episodes across ten models, 145 are partial executions confirm...
  </details>


### 📂 red-teaming
*红队测试 / Red Teaming* — 1 papers

- **2026-11-24** — Guowei Zou, Beiwen Zhang, Haitao Wang et al. — [TeamFlowRL: Online Policy Optimization of Decentralized Flow Policies for Multi-Agent Coordination](http://arxiv.org/abs/2611.32645v1)
  <details><summary>📄 Abstract</summary>
  Complex cooperative tasks require coordinated multi-agent behavior. Offline generative policies learn expressive cooperative behaviors from trajectories but remain limited by fixed datasets. Online reinforcement learning can improve them through environment interaction. However, fine-tuning flow policies is difficult because action likelihoods are hard to compute. We propose TeamFlowRL, a two-stage framework that pretrains multi-agent flow policies offline and fine-tunes them online. We formulat...
  </details>


### 📂 vulnerability
*漏洞与攻击面 / Vulnerabilities & Attack Surfaces* — 56 papers

- **2026-11-25** — Thiago de Souza Lamenza, Bruno José Olivieri de Souza, Markus Endler — [Deep Reinforcement Learning for Multi-UAV Data Harvesting Under Variable Team Sizes and Agent Loss](http://arxiv.org/abs/2611.34818v1)
  <details><summary>📄 Abstract</summary>
  Collecting data from wireless sensors can be challenging when limited communication infrastructure prevents them from offloading their measurements. In such settings, unmanned aerial vehicles (UAVs) can exploit their mobility to harvest data locally, while coordinated UAV teams can provide efficient and redundant coverage of remote areas. Multi-agent reinforcement learning (MARL) enables such teams to learn decentralized coordination policies. However, training separate policies for different te...
  </details>

- **2026-11-25** — Yifan Wang, Zetao Guo, You Xiao et al. — [A Differential Computing Accelerator for LLM Inference Leveraging Bit-Slice Transition Sparsity](http://arxiv.org/abs/2611.34630v1)
  <details><summary>📄 Abstract</summary>
  Large language models (LLMs) have become foundational to modern artificial intelligence. Driven by scaling laws, their rapid growth poses increasing computational and memory challenges for deployment. To accelerate the general matrix multiplication (GEMM) operations that dominate LLM computation, bit-slice architectures decompose quantized operands along the bit dimension, exposing slice-level sparsity and redundancy. However, existing bit-slice designs primarily exploit sparsity in high-order s...
  </details>

- **2026-11-25** — Jitendra K. Tugnait — [Conditional Independence Graph Learning from Dependent Data Via Time-Delay Embedding](http://arxiv.org/abs/2611.34616v1)
  <details><summary>📄 Abstract</summary>
  We consider the problem of inferring the conditional independence graph (CIG) of a high-dimensional stationary multivariate Gaussian time series which could be short-range dependent (SRD) or long-range dependent (LRD). In a time series graph, each component of the vector series is represented by a distinct node, and associations between components are represented by edges between the corresponding nodes. We consider a time-domain approach based on time-delay embedding, casting the problem as one...
  </details>

- **2026-11-25** — Liangyu Xiang, Junyu Gao, Xiaofeng Wang et al. — [DuCo: Exploiting Dual Cross-Layer Consistency for Sparse Geometric Attention](http://arxiv.org/abs/2611.34608v1)
  <details><summary>📄 Abstract</summary>
  Dense global attention is crucial for capturing cross-view geometry in visual geometry foundation models, yet its quadratic complexity limits efficient inference on long image sequences. Existing sparse attention methods primarily select entries of the global attention matrix based on attention probabilities and construct masks independently across layers, overlooking value redundancy and cross-layer information reuse. By analyzing attention distributions and clustering value representations acr...
  </details>

- **2026-11-25** — Ryuji Yamaguchi, Miyuki Matsuo — [ChemoMAE: Self-Supervised Spectral Representation Learning Reveals Chemical Heterogeneity in Historical Wood](http://arxiv.org/abs/2611.34581v1)
  <details><summary>📄 Abstract</summary>
  In historical timber buildings, multiple environmental factors act over centuries on wood whose chemical composition varies across anatomical regions, producing complex patterns of degradation. Understanding how timber members degrade is important for the effective conservation and restoration of historical buildings, yet the mechanisms underlying these patterns remain unclear. To investigate these mechanisms, we used self-supervised learning to establish a common basis for comparing specimens f...
  </details>

- **2026-11-25** — Yuyao Sun, Hongli Yuan, Shuang Li et al. — [PURA: Video Token Pruning via Unified Spatiotemporal Redundancy Assessment](http://arxiv.org/abs/2611.34521v1)
  <details><summary>📄 Abstract</summary>
  Video large language models incur substantial inference costs from long visual token sequences. Existing video token compression methods mitigate these costs by exploiting spatial redundancy within frames and temporal redundancy across frames. However, many approaches impose predefined processing orders or fixed allocation ratios for spatial and temporal compression, limiting their ability to adapt to the varying balance of spatiotemporal redundancy across videos. To address this limitation, we ...
  </details>

- **2026-11-25** — Yifan Jin, Zheng Zhang, Tianwen Qian et al. — [Who Is Ego? Scaling Cross-View Camera Wearer Identification and Segmentation beyond Humans](http://arxiv.org/abs/2611.34489v1)
  <details><summary>📄 Abstract</summary>
  A first-person (ego) image reveals what a camera sees, but not who or what carries it. Given a synchronized third-person (exo) image, camera wearer identification asks who is ego: which candidate carries the ego camera? We extend this task beyond humans to robots, vehicles, animals, and drones, and broaden its spatial scope (where is ego) from selecting a provided candidate mask to wearer segmentation with absence prediction and mutual camera localization across ego-exo views. We introduce FindE...
  </details>

- **2026-11-25** — Giacomo Vianello, David Morilla-Cabello, Juan Dendarieta Serrano et al. — [SkySearcher: High-Altitude Onboard VLM Reasoning for Aerial Semantic Search](http://arxiv.org/abs/2611.34485v1)
  <details><summary>📄 Abstract</summary>
  Recent advances in Vision-Language Models (VLMs) have improved semantic and visual reasoning, enabling UAVs to search for open-vocabulary queries in unstructured environments at high altitude. However, existing systems mainly follow low-altitude strategies, focusing on close-range iterative exploration, requiring storage-intensive dense 3D metric-semantic reconstructions or relying on large cloud-serviced VLMs assuming constant internet access. We propose SkySearcher, an aerial semantic search n...
  </details>

- **2026-11-25** — Guanxi Lai, Zixuan Li, Zhiwei Li et al. — [Semantic State Reading for Joint Image-Semantic Diffusion Transformers](http://arxiv.org/abs/2611.34279v1)
  <details><summary>📄 Abstract</summary>
  Pretrained visual representations improve diffusion-transformer training, yet exploiting both global context and local spatial structure requires deciding which semantic states to model and how to access them. We introduce Semantic State Reading (SSR), which jointly denoises image latents, a global CLS token encoding image-level context, and a compact patch state preserving spatial correspondence. SSR couples this global-local modeling with distinct reading paths: local states are fused with cor...
  </details>

- **2026-11-25** — Yuxuan Sun,  Hao,  Chen et al. — [Agent-as-a-Verifier: From Scores to Evidence for General Verification](http://arxiv.org/abs/2611.34132v1)
  <details><summary>📄 Abstract</summary>
  Verification is increasingly critical across various inference and learning paradigms, such as test-time scaling, recursive intelligence and automated research, where feedback can improve efficiency and optimization. Common score-based verifiers, or discriminative reward models, predict a scalar reward for an output. While useful for filtering, rewarding, and ranking, such scores provide no explicit, auditable evidentiary basis for the judgment. In parallel, although existing generative process ...
  </details>

- **2026-11-25** — Chau Truong, Hieu Ta Quang, Zhenzhen Liu et al. — [MulCLIP: A Multi-level Alignment Framework for Enhancing Fine-grained Long-context CLIP](http://arxiv.org/abs/2611.34083v1)
  <details><summary>📄 Abstract</summary>
  Vision-language models such as CLIP excel at image-text alignment but struggle with long, detailed descriptions due to training on short captions. Recent methods address this limitation using region proposals to align visual regions with sentences, but at substantial deployment cost. We present MulCLIP, an end-to-end multi-level alignment framework that directly exploits natural long-text structure without region proposals. Instead of simply stacking objectives, MulCLIP aligns different textual ...
  </details>

- **2026-11-25** — Yiheng Han, Ziang Chen, Zhuyong Fu et al. — [Embodied-VGGT: Preserving Reliable Local Geometry for Long-Sequence Reconstruction](http://arxiv.org/abs/2611.33964v1)
  <details><summary>📄 Abstract</summary>
  Long sequence reconstruction must correct accumulated drift while preserving locally consistent geometry. In robotics and autonomous driving, embodied acquisition provides recurring platform- environment geometry and repeated observations of scene structure and platform motion. We present Embodied-VGGT, which exploits these cues to establish reliable local relationships and selectively preserve them during global refinement. Memory-Augmented Grounded Chunks (MAGC) builds on Scal3R's global conte...
  </details>

- **2026-11-25** — Xiaocheng Luo, Peng Xu, Zaifu Zhan et al. — [DLaR: Dynamic Stochasticity Control for Latent Reasoning in Large Language Models](http://arxiv.org/abs/2611.33962v1)
  <details><summary>📄 Abstract</summary>
  Latent reasoning enables LLMs to operate in continuous embedding space, yet existing methods suffer from deterministic inference that precludes exploration of diverse reasoning paths. While recent approaches inject stochasticity to restore exploration, we identify two fundamental limitations: \textit{uniform stochasticity} across all steps is suboptimal, and unconstrained perturbations disrupt reasoning coherence. We propose Dynamic Stochasticity Control for Latent Reasoning (DLaR), a framework ...
  </details>

- **2026-11-25** — Hieu Man, Chao Shang, Rui Dong et al. — [FORK: Co-Evolving Safe Disclosure and Decision Skills Against Attackers Who Read Every Refusal](http://arxiv.org/abs/2611.33879v1)
  <details><summary>📄 Abstract</summary>
  When a guardrail rejects an LLM agent's action, its message reaches any attacker observing the trajectory: a fixed refusal leaves benign users unable to recover, whereas an explanation can tell the attacker what to try next. We study this as safe disclosure: explaining rejections so that authorized tasks recover without increasing adaptive attack success. Safe disclosure depends on both the decision and the message: what the guardrail blocks and what it reveals to the agent and the attacker. Bec...
  </details>

- **2026-11-25** — Zhaoxin Fan, Qingchen Yu, Kejian Wu et al. — [MMotion: Collaborative Cross-Scale Memory for Text-to-Motion Generation](http://arxiv.org/abs/2611.33819v1)
  <details><summary>📄 Abstract</summary>
  Text-to-motion generation aims to synthesize realistic human motions from natural-language descriptions, enabling applications in animation, virtual avatars, and embodied agents. Despite recent progress, existing methods either retrieve motion exemplars or retain long-range context, but rarely exploit memory to jointly reason about semantics, dynamics, and generation history. In this paper, we propose MMotion, a collaborative multi-scale memory framework that unifies scale-conditioned semantic r...
  </details>

- **2026-11-25** — Bowen Shi, Bo Li — [RHOPE: LLM-Augmented Adaptive Experimental Design with Complex Contextual Information](http://arxiv.org/abs/2611.33767v1)
  <details><summary>📄 Abstract</summary>
  Experimental design allocates limited measurement effort across candidate treatments to learn their expected outcomes. Adaptive designs refine allocations as evidence accumulates, improving estimation and treatment selection. Contextual information can inform these decisions, but exploiting unstructured or high-dimensional context remains challenging. We use large language models (LLMs) to transform complex context into proxy outcomes and propose Residual Horizon Optimization for Prediction-Powe...
  </details>

- **2026-11-25** — Natalie Collina, Elijah Journey Fullerton, Jingyi Liu et al. — [Non-manipulability and Approachability Beyond Two-Player Games](http://arxiv.org/abs/2611.33562v1)
  <details><summary>📄 Abstract</summary>
  We study the problem of guaranteeing non-manipulability and low regret for $n-1$ independent learners in an $n$-player repeated general game with one optimizer. Non-manipulability is a property which guarantees that learning agents can prevent a strategic opponent from exploiting their learning dynamics for its own benefit, while no-regret provides guarantees to a learner with respect to a fixed static benchmark. This problem is well understood in games with a single learner and a single optimiz...
  </details>

- **2026-11-24** — Keyan Guo, Rupam Patir, Haipeng Cai et al. — [PRECEPT: Security Self-Improvement of Coding Agents via Evolving Principles](http://arxiv.org/abs/2611.33519v1)
  <details><summary>📄 Abstract</summary>
  AI coding agents increasingly write and submit code with limited human review, and much of it passes functional tests while remaining insecure. We show that these failures persist. Across 14 task sequences, Codex, Claude Code, and Qwen Code fixed a vulnerability 85.7% of the time when shown the failing security test, then reintroduced the same vulnerability class in a new session 26.7% of the time, about as often as agents that had never seen it (27.5%). The capability is present; the retention ...
  </details>

- **2026-11-24** — Jongseong Kim, Hwiwon Lee, Dongjun Kim et al. — [Benchmarking Open-Ended Vulnerability Discovery in Windows Kernel Binaries](http://arxiv.org/abs/2611.33486v1)
  <details><summary>📄 Abstract</summary>
  Frontier models are increasingly used to discover real-world security vulnerabilities, making it critical to systematically evaluate their cybersecurity capabilities. However, existing security benchmarks primarily focus on known vulnerabilities in open-source projects, largely overlooking closed-source binaries, which underpin much of the software industry. In this paper, we ask: how effective are frontier models at uncovering deep vulnerabilities in production binaries? To answer this question...
  </details>

- **2026-11-24** — Md Ajoad Hasan, Dipayan Saha, Upoma Das et al. — [SecID: An LLM-Guided Framework for Threat-Aware Secondary Asset Identification with Quantitative RTL Analysis](http://arxiv.org/abs/2611.33453v1)
  <details><summary>📄 Abstract</summary>
  The growing complexity of modern hardware designs is making security assurance increasingly difficult. One of the foundational steps in pre-silicon security verification is identifying security assets. While primary assets are often evident from design functionality, the internal signals that can facilitate their compromise are much less apparent. Complex data- and control-flow dependencies create many such internal security-critical locations, whose exploitation depends on the threat-specific a...
  </details>

- **2026-11-24** — Siddharth Arya, Kshitij Jain — [Partial Routing: Trace-Tuned Delegation for Resource-Efficient Agentic Workflows](http://arxiv.org/abs/2611.33402v1)
  <details><summary>📄 Abstract</summary>
  AI models vary enormously in capability and price. Model routing exploits this by sending easier tasks to cheaper models. However, a single agentic task often combines easy and difficult subtasks, making one model choice for the entire task inefficient. We introduce partial routing, which guides a frontier lead model to delegate suitable subtasks to a cheaper worker model. From both models' past runs, we identify recurring subtasks and measure each model's quality and cost on them. These measure...
  </details>

- **2026-11-24** — Xiaomeng Wang, Peter Horvath, Zhengyu Zhao et al. — [RegionAlign: Manipulating Parameter Layouts for Localized Fault Injection on LLMs and VLMs](http://arxiv.org/abs/2611.33370v1)
  <details><summary>📄 Abstract</summary>
  Physical fault injection can flip stored weight bits, degrading LLMs and VLMs. Existing work largely overlooks how supply-chain manipulation affects fault vulnerability. We introduce RegionAlign, which allows a malicious provider to manipulate only the parameter layout before deployment, using bit-sensitivity search and channel permutations to concentrate vulnerable bits in one memory region while preserving weight values and clean performance. Under matched budgets, software experiments show gr...
  </details>

- **2026-11-24** — Xiang Fan, Yuheng Wang, Jiayuan Yan et al. — [OmniAct: One Policy, One Million Embodiments](http://arxiv.org/abs/2611.33158v2)
  <details><summary>📄 Abstract</summary>
  A single policy that controls diverse robots must not only transfer task knowledge across embodiments, but also adapt its behavior to each robot's capabilities. Existing approaches facilitate transfer through shared action representations, but these representations do not necessarily capture how differences in robot morphology should shape manipulation strategies. We introduce OmniAct, a cross-embodiment manipulation policy that conditions directly on each robot's kinematics in a specific scene ...
  </details>

- **2026-11-24** — Joshua Foster — [Do Language Models Mix? Experimental Evidence from Asymmetric Matching Pennies](http://arxiv.org/abs/2611.33265v1)
  <details><summary>📄 Abstract</summary>
  I test whether language models can select and implement mixed strategies using asymmetric matching pennies and a task with prescribed choice probabilities. Several models respond to their own payoffs, contrary to equilibrium and resembling human experimental subjects. Without randomization tools, no tested model reliably implements prescribed probabilities. Prompting models with their choice histories alone does not resolve this failure. While an external randomizer sharply improves implementati...
  </details>

- **2026-11-24** — Xiang Fan, Yuheng Wang, Jiayuan Yan et al. — [OmniAct: One Policy, One Million Embodiments](http://arxiv.org/abs/2611.33158v1)
  <details><summary>📄 Abstract</summary>
  A single policy that controls diverse robots must not only transfer task knowledge across embodiments, but also adapt its behavior to each robot's capabilities. Existing approaches facilitate transfer through shared action representations, but these representations do not necessarily capture how differences in robot morphology should shape manipulation strategies. We introduce OmniAct, a cross-embodiment manipulation policy that conditions directly on each robot's kinematics in a specific scene ...
  </details>

- **2026-11-24** — Shijin Gong, Kai Ye, Victor Chernozhukov et al. — [U-Statistics-Powered LLM Reasoning](http://arxiv.org/abs/2611.33064v1)
  <details><summary>📄 Abstract</summary>
  Since its introduction by DeepSeek, group relative policy optimization (GRPO) has been widely adopted for training large reasoning models and agents, spurring a proliferation of its variants. Yet the group size, a crucial hyperparameter in these GRPO-type algorithms, remains largely chosen by trial and error. Exploiting the U-statistic structure of GRPO's policy gradient, we recast the selection of the group size as a classical statistical problem of variance ratio estimation. This problem is pa...
  </details>

- **2026-11-24** — Ce Zhang, Junyi He, Tianshi Ming et al. — [GRAPE-Bench: When Vision Degrades, Does Video Reasoning Hold?](http://arxiv.org/abs/2611.33020v1)
  <details><summary>📄 Abstract</summary>
  Despite strong performance on standard benchmarks, video reasoning models remain vulnerable to visual degradation, raising concerns about their reliability in safety-critical scenarios. Existing benchmarks address this concern in part by simulating visual degradation or probing model reasoning with challenging questions, leaving open how well models handle naturally degraded video and whether they can make the simpler judgments that matter for safe driving. To this end, we introduce GRAPE-Bench,...
  </details>

- **2026-11-24** — Zixu Zhou, Xiangyu Guo, Ilya Grishchenko et al. — [PORTA: Systematic Discovery of Vulnerabilities in Identity Brokers](http://arxiv.org/abs/2611.33015v1)
  <details><summary>📄 Abstract</summary>
  Identity brokers such as Keycloak, Vault, and Dex translate authentication proofs from an upstream identity provider into sessions for downstream services. Due to their central role in authentication and trust mediation, a single vulnerability in a broker compromises every downstream service behind it. In fact, recent incidents have demonstrated that even widely adopted platforms are not immune to such issues, highlighting the critical need for systematic analysis. To build such an analysis, thi...
  </details>

- **2026-11-24** — Xuanchen Liu, Hejun Zhang, Boxuan Dong et al. — [Embodied AI Fails the Mirror Test: How a Simple Mirror Breaks Robot Policies](http://arxiv.org/abs/2611.33010v1)
  <details><summary>📄 Abstract</summary>
  Can a simple mirror expose the limitations of today's robotic manipulation policies? Inspired by the mirror self-recognition test in animal cognition, we investigate whether robot policies can reliably manipulate physical objects in scenes containing their reflections. We introduce RoboDojo-Mirror, a benchmark built on RoboDojo that preserves task objectives, success criteria, and policy checkpoints while comparing a mirror-free baseline with single-mirror, dual-mirror, and mirrored-tabletop con...
  </details>

- **2026-11-24** — Sascha H. Hauck, Nis-Luca van Hülst, Matthias Kabel et al. — [Quantum-Inspired Tensor Train Spectral Solver for High-Resolution PDEs with Non-Periodic Boundary Conditions](http://arxiv.org/abs/2611.32968v1)
  <details><summary>📄 Abstract</summary>
  Tensor train (TT) methods enable high-resolution computational mechanics simulations by exploiting low-rank structure in discretized fields and operators. While the superfast Fourier transform (SFFT) has enabled efficient TT-based spectral solvers for periodic problems, corresponding representations for non-periodic boundary conditions remain underexplored. We introduce the superfast cosine and sine transforms (SFCT and SFST), extending the TT spectral framework to homogeneous Neumann and Dirich...
  </details>

- **2026-11-24** — Etienne D'Argenlieu, Alessandro Summer, François Jamet et al. — [Exploiting SU(2) Symmetry for Efficient Quantum State Preparation of Matrix Product States](http://arxiv.org/abs/2611.32805v1)
  <details><summary>📄 Abstract</summary>
  Quantum computing offers a promising route to simulating strongly correlated systems, particularly for dynamical and spectral quantities whose classical computation can become prohibitively expensive. Fault-tolerant algorithms for these tasks, including real-time dynamics and phase estimation, assume efficient preparation of the initial many-body state, making state preparation an important bottleneck. Matrix product states obtained classically with the density matrix renormalization group can b...
  </details>

- **2026-11-24** — Nicola Leonetti, Federico Stella, Aoxiang Fan et al. — [AnyPrune: Optimization-Free Pruning for Any Feedforward 3D Gaussian Splatting Pipeline](http://arxiv.org/abs/2611.32735v1)
  <details><summary>📄 Abstract</summary>
  Feedforward 3D Gaussian Splatting (3DGS) pipelines reconstruct a scene from images in a single forward pass, representing it as real-time-renderable 3D Gaussians. However, the resulting representations contain far more Gaussians than are needed to render the scene faithfully, especially when there are many input views. This drastically increases memory and storage requirements. Existing pruning methods either require costly re-optimization, which defeats the purpose of a single forward pass, or ...
  </details>

- **2026-11-24** — Wei Huang, Chenying Liu, Xudong Kang et al. — [HS-OVSeg: Multi-Granularity Open-Vocabulary Semantic Segmentation in Remote Sensing via Heterogeneous Supervision](http://arxiv.org/abs/2611.32518v1)
  <details><summary>📄 Abstract</summary>
  Open-vocabulary semantic segmentation (OVSS) enables flexible, text-driven mapping of remote sensing (RS) imagery beyond predefined categories. Despite advances in segmentation foundation models, RS-OVSS remains constrained by the scarcity of large-scale, semantically diverse datasets with accurate pixel-level annotations. Meanwhile, existing RS datasets contain abundant scene- and object-level annotations that offer valuable semantic information but lack precise pixel-wise supervision. To explo...
  </details>

- **2026-11-24** — Xiaomeng Wang, Martha Larson, Zhuoran Liu et al. — [Analyzing Single-Bit Flips on LLMs and Their Backbone-Matched VLMs](http://arxiv.org/abs/2611.32503v1)
  <details><summary>📄 Abstract</summary>
  Open-weight large language models (LLMs) enable offline weight analysis and are reused as backbones in vision-language models (VLMs), increasing the risk of bit-flip attacks that manipulate stored weight bits to induce malicious model behavior. An adversary could identify vulnerable bits on a public LLM and later flip the same locations in a deployed LLM or its backbone-matched VLMs. A single-bit flip is particularly practical in this setting because it is easier to achieve under hardware fault ...
  </details>

- **2026-11-24** — Zhumei Wang, Shaofei Wang, Xiang An et al. — [COHERE4D: Training-Free Dense Surface Alignment for Coherent Metric 4D Human-Scene Reconstruction](http://arxiv.org/abs/2611.32482v1)
  <details><summary>📄 Abstract</summary>
  Human and scene foundation models offer complementary strengths for monocular 4D reconstruction: human models recover metric-scale body meshes but lack scene grounding, whereas scene models estimate globally consistent 3D geometry and camera motion without reliable metric scale. Crucially, both models reconstruct the same foreground human surface. Yet existing methods do not directly exploit this shared surface: lacking reliable foreground human geometry in scene reconstructions, earlier approac...
  </details>

- **2026-11-24** — Jing Li, Zhe Zhang, Huateng Sun et al. — [Progressive Reliable Supervision for Black-Box Universal Domain Adaptation](http://arxiv.org/abs/2611.32474v1)
  <details><summary>📄 Abstract</summary>
  Black-Box Universal Domain Adaptation (B$^2$-UniDA) aims to adapt a target model to an unlabeled target domain under arbitrary label-space relationships, while neither source data nor source-model parameters are accessible during adaptation. Under such restrictive information access, reliable target supervision is unavailable, while predictions from the black-box source model can be unreliable due to source bias and domain shifts. To address this challenge, we propose Progressive Reliable Superv...
  </details>

- **2026-11-24** — Haozhan Shen, Liangbo He, Jun Lan et al. — [Describe, Don't Ask: Caption-Driven On-Policy Distillation for Fine-Grained Visual Perception](http://arxiv.org/abs/2611.32463v1)
  <details><summary>📄 Abstract</summary>
  Vision-language models (VLMs) often recognize fine-grained details more accurately in a relevant crop than in the full image. Multimodal on-policy distillation (OPD) methods exploit this by transferring the advantage of a crop-view teacher to a full-image student. However, their supervision relies on region-specific questions curated through an elaborate synthesis pipeline, which brings three weaknesses: (1) every region needs a question--answer pair written exclusively for it, locking training ...
  </details>

- **2026-11-24** — Ruizhe Yao, Zhen Huang, Songpan Gao et al. — [LRQ-Cache: Compressing Feature Caches in Video Diffusion via Low-Rank Approximation and Quantization](http://arxiv.org/abs/2611.32345v1)
  <details><summary>📄 Abstract</summary>
  Video diffusion transformers (DiTs) achieve high-fidelity generation, but inference is expensive because every denoising step evaluates a large transformer over all spatiotemporal tokens of the video. Temporal caching accelerates them by reusing intermediate features across denoising steps. However, retaining dense feature tensors introduces a persistent storage cost that grows with video length, resolution, and cache coverage, reaching 109-346 GiB per video for the predictive caches we evaluate...
  </details>

- **2026-11-24** — Jiajie Zhang, Yankai Xiang, Changhao Chen — [VLAs Execute, Code Recovers: 3D Skill Envelopes Bridge the Compositional Gap in Agentic Manipulation](http://arxiv.org/abs/2611.32245v1)
  <details><summary>📄 Abstract</summary>
  Composing frozen Vision-Language-Action (VLA) skills under an agentic planner promises scalable long-horizon manipulation without long-horizon demonstrations, yet strong atomic skills routinely fail at seams even under a correct plan. Standard remedies reset the robot's pose or draft entry conditions in language, missing the physical cause we uncover via causal interventions: even after re-homing, a frozen VLA rigidly retraces its habitual trajectory and collides with displaced scene residue, wh...
  </details>

- **2026-11-24** — Yuanuo Feng, Yubing Ye, Yizhe Chen et al. — [Beyond Autoregression: Diffusion Language Model is All Analog In-Memory Computing Need](http://arxiv.org/abs/2611.32223v1)
  <details><summary>📄 Abstract</summary>
  Analog in-memory computing (AIMC) enables energy-efficient language-model inference, but hardware non-idealities perturb matrix--vector multiplications and degrade generation quality. Autoregressive (AR) models are especially vulnerable: each token is committed to the causal context at birth, so perturbation-induced errors cascade. We study diffusion language models (DLMs), which iteratively refine a masked sequence, as an alternative paradigm. Across scale-matched model pairs and open checkpoin...
  </details>

- **2026-11-24** — Sai Karthikey Pentapati, Shashank Nelamangala Sridhara, Birendra Kathariya et al. — [SplatTok: Data-Driven Compression of 3D Gaussian Splats with Scene-Level Tokens](http://arxiv.org/abs/2611.32202v1)
  <details><summary>📄 Abstract</summary>
  3D Gaussian splats enable real-time rendering but require substantial storage. Existing compression methods either encode the primitives of a given splat or optimize a compact representation independently for each scene. Yet a Gaussian splat is only one realization of a scene: different arrangements of primitives can produce nearly identical rendered views. We exploit this freedom on the decoding side with SplatTok, a learned scene-resynthesis codec. Trained across thousands of real-world scenes...
  </details>

- **2026-11-24** — Qiyuan Chen, Hongsen Huang, Jiahe Chen et al. — [RightDiff: Learning Generative Reward Models to Judge by the Right Differences](http://arxiv.org/abs/2611.32166v1)
  <details><summary>📄 Abstract</summary>
  Generative reward models typically rely on generic query-level rubrics or unconstrained rationales, overlooking the fact that pairwise preference is driven by response-specific differences. Moreover, optimizing solely for outcome correctness encourages models to exploit superficial shortcuts such as verbosity and formatting, triggering rationale drift. To address this, we propose RightDiff, which structures pairwise evaluation into an evidence-grounded evaluation trajectory executed in a single ...
  </details>

- **2026-11-24** — Mahmoud Abumandour, Srinija Ramichetty, Guru Venkataramani et al. — [Bit-Flip Attacks on Quantized Neural Networks without Knowledge of Model Parameters](http://arxiv.org/abs/2611.32128v1)
  <details><summary>📄 Abstract</summary>
  We show that quantization asymmetry concentrates bit-flip vulnerability in small tensors retained at high precision. CoarseHammer targets these tensors and accepts flips at any bit, without parameter values, gradients, or data. It remains effective under continued fine-tuning. Under ideal placement, CoarseHammer reaches chance accuracy in at least 81.5% of runs on each of ten evaluated models, including four large language models, with median successful runs requiring at most 24 flips. On simula...
  </details>

- **2026-11-24** — Wenchong Tian, Shixun Li, Ruozhou Lin et al. — [From Rule-based to Agentic: LLM Agent based Real-time Control of Urban Drainage Systems for Flooding and Sewer Overflow Mitigation](http://arxiv.org/abs/2611.32046v1)
  <details><summary>📄 Abstract</summary>
  Real-time control (RTC) for urban drainage systems (UDS) remains hampered by sparse in-network sensing. While heterogeneous multi-modal meteorological early warnings often contain decision-critical information for UDS RTC, none of the existing approaches can exploit such externally-sourced information within the control workflow. Here we introduce AgenticAI-Control, an agentic artificial intelligence framework able to assimilate multi-source meteorological early warnings in RTC. Two coupled larg...
  </details>

- **2026-11-24** — Sheng Lu, Rui Mao, Zewei Chen et al. — [Online Environment Repair for Coding Agents](http://arxiv.org/abs/2611.32037v1)
  <details><summary>📄 Abstract</summary>
  Programmatic verifiers provide scalable reward signals for training coding agents with reinforcement learning, yet subtle harness defects and incomplete unit tests allow policies to earn full credit without solving the intended task. Existing training-time defenses intervene either by penalizing suspicious outputs or by filtering flagged tasks and rollouts. However, output penalties leave the underlying verifier exploitable, driving policies to disguise shortcuts under reasoning monitors or zero...
  </details>

- **2026-11-24** — Zichen Liu, Liangyi Huang, Stanley Nguyen et al. — [Not Just Any Example: Security Requirements and Fix Patterns for Guiding LLM Vulnerability Repair](http://arxiv.org/abs/2611.31993v1)
  <details><summary>📄 Abstract</summary>
  Software vulnerabilities leave systems open to attack, and their remediation is often delayed. Large language models (LLMs) have advanced automated patch generation, yet passing functionality tests does not ensure that a patch enforces the security requirement the vulnerability violated. Existing vulnerability repair techniques rely on curated patterns or templates with limited coverage, leaving unclear which repair strategies carry over across vulnerabilities and how they can steer LLMs. We pre...
  </details>

- **2026-11-24** — Weiying Wang, Yuanyang Xiang, Zhiwei Zhang — [Native Block-Quantized Matrix Multiplication and Explicit K/V Residency with Dual-View Access for LLM Inference on RISC-V Vector Processors](http://arxiv.org/abs/2611.31937v1)
  <details><summary>📄 Abstract</summary>
  Some key execution states in large language model inference persist across multiple instructions and are difficult to express and exploit within RVV semantics centered on individual operations. We define specialization boundaries according to data-state lifetimes and propose Quantized Block Streams (QBS) and Attention/KV Context (AKV) while preserving RVV programmability. QBS organizes native-block format processing, block traversal, integer computation, and ordered FP32 accumulation into a unif...
  </details>

- **2026-11-24** — Keyu He, Michael Li, Jiarui Liu et al. — [Exploring Multi-Player Social Games as Verifiable Training Grounds for Large Language Models](http://arxiv.org/abs/2611.31821v1)
  <details><summary>📄 Abstract</summary>
  The training of socially intelligent language models often relies on large language model (LLM) judges, which are expensive, noisy, and vulnerable to reward hacking. Multi-player social games offer a natural alternative: they require open-ended communication to coordinate with teammates and infer hidden roles, while their rules provide an objective outcome which can serve as a verifiable reward for training. Using three social games, we explore how much social intelligence Qwen3 models can acqui...
  </details>

- **2026-11-24** — Seunghan Lee, Jun Seo, Junhyeok Kang et al. — [VISOR: A Vision-Language Selector for Multimodal Time-Series Forecasting](http://arxiv.org/abs/2611.31780v1)
  <details><summary>📄 Abstract</summary>
  Recent time-series foundation models (TSFMs) forecast a distribution over futures, and multimodal time-series (TS) forecasting further exploits other modalities to improve forecasting accuracy. However, existing works have two limitations: 1) TSFMs reduce the predictive distribution to its median or mean, flattening diverse futures into a calm line, and 2) multimodal TS forecasting models incorporate text into the forecaster through TS-language alignment, which is substantially weaker than visio...
  </details>

- **2026-11-24** — Yuhei Kawakoya, Eitaro Shioji, Yuto Otsuki et al. — [Mixed-Initiative Mining of Root-Cause Analyses into Audit Priors for C/C++ Vulnerability Hunting](http://arxiv.org/abs/2611.31744v1)
  <details><summary>📄 Abstract</summary>
  Vulnerability auditing of large C/C++ codebases is constrained by limited review attention. Human auditors and LLM-based agents need operational priors that indicate where to look first and what to suspect, but such priors are rarely available in directly usable form. Rather than proposing a new vulnerability detector, we derive audit-steering artifacts from evidence-backed root-cause analysis (RCA) reports.   We introduce two complementary representations: Occurrence Context (OC), a location pr...
  </details>

- **2026-11-23** — Jaromir Sant, Ivana Valentić — [From invasion to replacement: excursions of the Moran model](http://arxiv.org/abs/2611.31663v1)
  <details><summary>📄 Abstract</summary>
  An excursion-theoretic description of the continuous-time Moran model with recurrent mutation is developed. Exploiting its birth--death structure, the killed Moran process is characterized through its Green function, resolvent, Laplace transforms of hitting times, and spectral decomposition. A duality between the Moran model and a pure-death process is also established, yielding a spectral representation of its transition probabilities. The characterization of the killed process leads to a bound...
  </details>

- **2026-11-23** — Fatemeh Elhambakhsh, Gaurav Ameta, Aditi Roy et al. — [Boundary Representation-Driven Graph Transformer Modeling for Machining Operation Sequencing](http://arxiv.org/abs/2611.31661v1)
  <details><summary>📄 Abstract</summary>
  Machining process planning is inherently complex due to the interdependence between part geometry, machining operations, and evolving manufacturable states. Traditional approaches rely heavily on expert knowledge and rule-based systems, limiting scalability and automation. While recent machine learning methods have shown promise, most operate on simplified geometric representations, such as voxels or hand-crafted features, which fail to fully exploit the rich geometric and topological informatio...
  </details>

- **2026-11-23** — Mudita Khurana, Karim Liman-Tinguiri — [Evaluating LLM Security Review Agents with Operationally Sourced Ground Truth](http://arxiv.org/abs/2611.31606v1)
  <details><summary>📄 Abstract</summary>
  LLM-based security review agents can reason about vulnerabilities that deterministic tools miss, but deploying them responsibly requires knowing whether they actually work. Existing benchmarks construct ground truth synthetically or from public CVE databases and are blind to the vulnerability patterns specific to a given production codebase. We present an evaluation framework grounded in an organisation's own vulnerabilities, with three contributions. First, a dataset construction methodology th...
  </details>

- **2026-11-23** — Kareem Shehada, Zhiyun Qian — [Aftershock: Yesterday's Linux Kernel Bugs, Tomorrow's Android Exploits](http://arxiv.org/abs/2611.31547v1)
  <details><summary>📄 Abstract</summary>
  Android kernels have long suffered from slow patch propagation from Linux upstream, with fixes often reaching devices far later than conventional Linux distributions. Until recently, this lag was largely a patch-management problem. With rapidly improving LLM agents, it is becoming an exploitation problem: public upstream patches can now serve as blueprints for building working n-day exploits before downstream devices are fixed. We test this threat end to end by building an automated pipeline tha...
  </details>

- **2026-11-23** — Muhammad Talha, Zhu Li, Joel Jung — [InterGS+: Inter-Frame Gaussian Splatting Compression with Geometry-Aware Transformer Prediction and Adaptive Residual Coding](http://arxiv.org/abs/2611.31482v1)
  <details><summary>📄 Abstract</summary>
  Dynamic 3D Gaussian Splatting (3DGS) provides real-time photorealistic rendering, but representing each frame as irregular Gaussian primitives with high-dimensional attributes creates substantial storage and transmission cost. Exploiting temporal redundancy is challenging because Gaussian primitives do not preserve fixed identities across frames. We propose InterGS+, a lightweight post-hoc inter-frame codec that jointly improves temporal prediction and residual representation. Current-frame geom...
  </details>

- **2026-11-23** — Karthik Karunanithi — [Per-Attack Blocking Hides Catalog Vulnerability: A Weakest-Link Analysis of Tool Manifests](http://arxiv.org/abs/2611.31338v1)
  <details><summary>📄 Abstract</summary>
  Runtime controls for tool-using agents depend on manifests that state what each tool may read and where its output may go. Evaluations of these controls, including ChainCaps, report per-attack blocking: the share of attacks a set of manifests stops. We show that this is the wrong unit. A catalog is only as safe as its weakest source policy: if $M$ independently authored policies are each wrong with probability $p$, the chance that the catalog contains an accepted exfiltration path is $1-(1-p)^M$...
  </details>


### 📂 defense
*防御与防护方法 / Defense & Protection Methods* — 59 papers

- **2026-11-25** — Alessandro Cantelli-Forti, Isabella Marasco, Hosam Alamleh et al. — [Make the Adversary Spend More: Stateful Deception as a Cost-Exchange Primitive for AI-Era Cyber Defense](http://arxiv.org/abs/2611.34770v1)
  <details><summary>📄 Abstract</summary>
  Large language models (LLMs) are transforming the economics of intrusion by reducing the attacker's cost to scan and adapt, while tempting defenders into unbounded compute. We argue that cyber deception should be judged by the cost exchange it imposes, not by realism or detection, and that the primitive making that exchange favorable is adversary-specific persistent state. Rather than a honeypot that resets or merges sessions, each recognized adversary re-enters the world it believes it has comp...
  </details>

- **2026-11-25** — Jianming Zhou, Yang Luo, Guangpu Chen et al. — [From Models to Services: Systematizing Security Assurance for Model-as-a-Service](http://arxiv.org/abs/2611.34623v1)
  <details><summary>📄 Abstract</summary>
  Large language models are mainly delivered as cloud services, in which the assets of different principals are coupled within a single service pipeline, while the related security research is scattered across several fields with differing threat models. This paper systematizes this research from a service perspective. We decompose Model-as-a-Service (MaaS) into a five-layer stack and five trust boundaries, define six adversary classes and six security goals, use them to code 120 studies, and eval...
  </details>

- **2026-11-25** — Yan Lin, Zhongliang Guo, Jingyu Lin et al. — [Agentic-Level Adversarial Purification: Revisiting Diffusion Purifiers on Native-Resolution Agentic Inputs](http://arxiv.org/abs/2611.34181v1)
  <details><summary>📄 Abstract</summary>
  Vision-language agents act on native-resolution renders of multi-element pages, where one perturbed photo or a few altered text strokes can redirect the decision. Any content provider can craft such a perturbation on the open model behind the agent, so a plug-in purifier is the natural first line of defense. Yet diffusion purifiers were designed and evaluated at the fixed resolution of the diffusion model on classifier or natural-image benchmarks, and defense evaluations for agents test JPEG, bl...
  </details>

- **2026-11-25** — Rikard Vinge, Miguel A. Belenguer-Plomer, Isabelle Wittmann et al. — [Enhancing Maritime Domain Awareness using Latent Space Representations](http://arxiv.org/abs/2611.34899v1)
  <details><summary>📄 Abstract</summary>
  This work presents a novel application of Earth Observation (EO) embeddings for Maritime Domain Awareness (MDA) from the perspective of the geospatial foundation model TerraMind. By operating directly on compressed latent-space representations rather than on the original Sentinel-1 imagery, this approach directly addresses the data gravity bottleneck that increasingly constrains operational EO processing, in line with the objectives of the Embed2Scale project. In particular, linear and non-linea...
  </details>

- **2026-11-25** — Yuncheng Guo, Ying Dong, Xiaodong Gu — [Reading, Not Adapting: Unlocking Frozen Visual Knowledge for AI-Generated Image Detection](http://arxiv.org/abs/2611.34719v1)
  <details><summary>📄 Abstract</summary>
  Generalization to unseen image generators has driven efforts to adapt pretrained visual representations for detection. Yet recent findings show that vision foundation models already encode transferable detection knowledge, while further adaptation can impair generalization. This motivates a shift from backbone adaptation to knowledge readout. Conventional linear probing offers a direct way to read this knowledge but is limited to final-layer RGB features. Multi-cue detectors broaden the evidence...
  </details>

- **2026-11-25** — Yusen Feng, Zixi Kang, Zhijun Yin et al. — [Nav4Manip: From Navigation to Dexterous Mobile Manipulation through Co-Evolution](http://arxiv.org/abs/2611.34655v1)
  <details><summary>📄 Abstract</summary>
  Dexterous mobile manipulation is essential for robots to perform useful tasks in complex, unstructured environments. However, existing systems face two challenges. First, navigation remains too coarse for downstream manipulation, which often requires a precise base position and approach orientation rather than merely reaching a meter-scale goal region. Second, navigation and manipulation are commonly trained in isolation, lacking a feedback loop that enables the two capabilities to co-evolve. Th...
  </details>

- **2026-11-25** — Hoang-Nhat Nguyen, Chen Change Loy — [DocSEAM: Bidirectional Cross-Page Encoding for Multi-Page Document Understanding](http://arxiv.org/abs/2611.34420v1)
  <details><summary>📄 Abstract</summary>
  Multi-page document vision-language models encode each page independently, creating a feature-level discontinuity at page boundaries: visual tokens are formed without access to content on adjacent pages, and the language model must reason over these page representations formed in isolation. We introduce DocSEAM (Document Selective Enrichment via Anchored Masking), a lightweight module inserted between a pretrained vision encoder and the language model that injects the inductive bias of local cro...
  </details>

- **2026-11-25** — Yuchen Zhou, Hongsheng Wu, Jiayu Tang et al. — [AIRIS: Benchmarking Social Embodied Intelligence in Egocentric Streaming Videos](http://arxiv.org/abs/2611.34347v1)
  <details><summary>📄 Abstract</summary>
  Embodied agents operating around people must not only recognize social cues, but also decide when the available evidence is sufficient, whether to intervene, and how to respond without violating social norms. Existing benchmarks typically evaluate these abilities in isolation or with access to completed videos, obscuring where an online social decision fails. We introduce AIRIS, a causal streaming benchmark that formulates social embodied intelligence as a time-anchored chain of Attention, Inten...
  </details>

- **2026-11-25** — Yinjun Liu, Xinye Li, Ruisen Peng et al. — [Crucible: Evaluating LLM Agents in Executable Chemistry Research Environments](http://arxiv.org/abs/2611.34254v1)
  <details><summary>📄 Abstract</summary>
  Large language models (LLMs) perform well on chemistry knowledge benchmarks, which mainly assess question answering and isolated tasks. Chemical research, however, requires using specialized tools and interpreting their outputs to obtain chemically valid results. To address this gap, we introduce Crucible Bench to evaluate this ability across all four stages of the design-make-test-analyze (DMTA) cycle. The benchmark contains 1,078 tasks in 12 task families curated from 18 published datasets, co...
  </details>

- **2026-11-25** — Inhee Cho, Jinyoung Jeong, Byung Ju Kim et al. — [Knocking on Minds Door; A Mixed-Methods Field Study of a Voice LLM Companion in Older Adults Daily Lives](http://arxiv.org/abs/2611.33727v1)
  <details><summary>📄 Abstract</summary>
  Global aging makes digital technology important for older adults healthy aging, yet graphical user interfaces remain inaccessible to many. Voice agents based on large language models may help, but users needs and reasons for sustained use remain unclear. We developed a phone-call-style companion that initiates conversations proactively and structures calls using a persona, conversation rules, and prior-call memory (facts, insights, relationship background). We conducted a two-week mixed-methods ...
  </details>

- **2026-11-25** — Jiechen Li, Hannah Groos, Brinnae Bent — [Aligned Machine: A Benchmark for Evaluating Multimodal Embedding Similarity via Human Comparative Judgements](http://arxiv.org/abs/2611.33594v1)
  <details><summary>📄 Abstract</summary>
  Embedding models increasingly inform how people search, recommend, and retrieve information, yet we lack credible ways to test whether these similarity judgments reflect how humans understand meaning. Existing benchmarks typically rely on static, expert-labeled pairs with coarse Likert-style annotations, limiting scalability and making it difficult to obtain consistent, high-confidence annotations. We introduce Aligned Machine, an interactive, public-facing platform that transforms broad partici...
  </details>

- **2026-11-25** — Ronglai Zuo, Fei Ni, Junpeng Jing et al. — [SEEL: Towards End-to-End 3D Sign Generation with Language Models](http://arxiv.org/abs/2611.33588v1)
  <details><summary>📄 Abstract</summary>
  3D sign language generation aims to produce signing motion from written text. Motivated by the linguistic nature of sign language, recent methods combine a motion tokenizer with a language model to predict motion tokens from text. However, both components are optimized through a two-stage pipeline with mismatched objectives: the tokenizer minimizes reconstruction error in isolation, while the generator learns from rigid one-hot reference tokens. A straightforward end-to-end extension bridges dis...
  </details>

- **2026-11-25** — Sumukh Shrote, Shenbagaraj Kannapiran, Eric Eaton et al. — [Memory Is Not Ground Truth: Revising Navigation Authority under Unreliable VLM Evidence for Persistent Semantic Navigation](http://arxiv.org/abs/2611.34915v1)
  <details><summary>📄 Abstract</summary>
  Vision-language models (VLMs) enable robots to reason about semantic and spatio-temporal context, verify task-relevant objects, and guide sensing and navigation. Persistent memory can reduce redundant search for field robots, but when should a memory continue to guide behavior? Repeated misses may suggest that a memory is stale. Our experiments show why this evidence can remain ambiguous under VLM-based perception. Using a Boston Dynamics Spot with four fixed cameras and a persistent spatio-temp...
  </details>

- **2026-11-25** — Siddhartha Gairola, Jiahao Xie, Anna Kukleva et al. — [Stranger Things: When Objects Appear Without Their Typical Neighbors](http://arxiv.org/abs/2611.34881v1)
  <details><summary>📄 Abstract</summary>
  Visual context is a powerful cue for object recognition: scenes inform what, where, and at what scale objects are likely to appear. Yet over-reliance on context becomes a failure mode when models predict objects based on their typical neighbors rather than the objects' own visual features, which we call typicality bias. While extensively studied in the pre-Transformer era, it has often been assumed that architectural and scale improvements would naturally solve it, and a systematic diagnostic ac...
  </details>

- **2026-11-25** — Xinyi Wu, Rongxin Gao, YuHui Lin et al. — [ADClaw: A Programmable Visual Agent for Industrial Anomaly Detection and Understanding](http://arxiv.org/abs/2611.34591v1)
  <details><summary>📄 Abstract</summary>
  Industrial anomaly detection (IAD), the task of identifying and localizing deviations from normal product conditions, is essential to automated quality inspection in manufacturing. Many vision-language models for IAD rely on large domain-specific datasets for fine-tuning and make predictions in a single pass, leaving no opportunity to re-examine ambiguous regions. Although tool-using agents can revisit these regions, predefined tool interfaces limit how they can combine intermediate results in a...
  </details>

- **2026-11-25** — Niccolò D'Archivio, George Giakkoupis, Frédéric Giroire et al. — [DéjàVu: Plurality Consensus by First Repetition](http://arxiv.org/abs/2611.34534v1)
  <details><summary>📄 Abstract</summary>
  We analyze DéjàVu, a simple protocol for plurality consensus: in each synchronous round, each agent samples one uniformly random agent and adopts the first opinion it observes twice, resetting its memory after every adoption. The rule requires neither frequency counters nor knowledge of the population size or the number of opinions. It relies only on repetition detection, an ability documented in single neurons and reflected in the mere-exposure effect.   For a population of $n$ agents with $k$ ...
  </details>

- **2026-11-25** — Yuntong Chen, Yingqi Li, Qiwen Shen et al. — [LLM-coupled interpretable tool wear monitoring with multi-evidence reasoning in CNC machining](http://arxiv.org/abs/2611.34270v1)
  <details><summary>📄 Abstract</summary>
  Interpretable tool wear assessment in CNC machining is challenging. Existing diagnostic models have high accuracy but provide limited guidance for tool replacement. This study proposes a two layer framework combining deep learning wear classification and LLM assisted reasoning. The first layer uses PCA Loading feature selection and optimized GRU to recognize three wear states, achieving 98.38 percent macro F1 score on the PHM2010 dataset. The second layer uses LLMs to generate natural language r...
  </details>

- **2026-11-25** — Michael Ruofan Zeng, Junaid Hasan, Xuanyu Yang et al. — [PatternMiner: Automated Mathematical Discovery Through LLM-Guided Training and Interpretation of Small Models](http://arxiv.org/abs/2611.33966v1)
  <details><summary>📄 Abstract</summary>
  There are several approaches to AI-driven mathematical discovery. One of these involves the use of large language models (LLMs) to resolve well-specified conjectures via text-based reasoning, while another uses narrow models and interpretability for more open-ended, human-in-the-loop exploration using object-based mathematical data. The latter is limited in its ability to move beyond simple empirical pattern detection while the former is not well-designed for direct, open-ended exploration of la...
  </details>

- **2026-11-25** — Yuan Qian, Jiaqi Cui, Jie Ma — [Show Me the Change You Want: Visual Example-Guided Change Detection](http://arxiv.org/abs/2611.33756v1)
  <details><summary>📄 Abstract</summary>
  Change detection identifies where images differ, but in practice users often seek only a particular kind of change. Existing referring change detection methods rely on predefined categories, textual descriptions, or annotated masks, limiting flexibility or requiring additional annotation. In this paper, we propose a new way to perform change detection, where an unannotated before-and-after image pair serves as a visual example to guide change localization in another pair. Our framework, Visual E...
  </details>

- **2026-11-24** — Jeremy Canale — [Dynamic Reasoning in Next-Gen Detection and Response: An Empirical Study of LLM Triage, Reinforcement Tuning, and Adversarial Evasion](http://arxiv.org/abs/2611.33470v1)
  <details><summary>📄 Abstract</summary>
  We present an end-to-end empirical study of dynamic reasoning in next-generation detection and response pipelines, evaluating how static classifiers, graph-based signal fusion, and large language model (LLM) triage agents perform under strict human-analyst attention budgets (Recall at B alerts/day). Across 56 reproducible experiments spanning a multi-layer enterprise-and-cloud simulator and four public datasets (SOREL-20M, BODMAS, LANL, and DARPA Transparent Computing), we test twelve architectu...
  </details>

- **2026-11-24** — Ehsan Latif, Roberto Dailey, Risto Miikkulainen et al. — [Evaluation and Restoration of Safety in Reasoning-Tuned LLMs](http://arxiv.org/abs/2611.33515v1)
  <details><summary>📄 Abstract</summary>
  Open-source LLMs that are optimized for reasoning, such as VibeThinker, aim to democratize AI by bringing high-capability models to users with limited resources. They are broadly available but lack regulation and external guardrails; therefore, in order to integrate them safely into human society, it is critical that they perform in a safe manner. There are popular and intuitive arguments for why improved reasoning should improve safety, but recent evidence suggests that, in fact, the opposite m...
  </details>

- **2026-11-24** — Mingzhe Du, Thong Thanh Nguyen, Nguyen Tran Cong Duy et al. — [Lost in Translation, Not in Confidence: Benchmarking and Calibrating Multilingual Decision Models](http://arxiv.org/abs/2611.33307v1)
  <details><summary>📄 Abstract</summary>
  Decision models are language models fine-tuned to return a probability for each option of a typed query, which routers and guardrails threshold directly. They are built on multilingual bases but ranked almost entirely in English. We evaluate 25 top-ranked open-weight decision models on 17 tasks in 14 languages, comparing each language with English on parallel items. Every model loses accuracy in every language, from about 2 points in high-resource languages to 8 in Tamil, while confidence falls ...
  </details>

- **2026-11-24** — Jingde Chen, Zijie Shang, Tong Liu et al. — [CLEAR: A Contrastive-Masked Foundation Model for BESIII Event Understanding](http://arxiv.org/abs/2611.33223v1)
  <details><summary>📄 Abstract</summary>
  The increasing diversity and complexity of decay channels at high energy physics experiments pose a challenge to analysis workflows, which require time-consuming, labor-intensive channel-specific selections and optimization. This motivates the development of foundation models capable of learning a unified representation transferable across different channels. In this paper, we introduce CLEAR (Contrastive Learning for Event Attention-based Representation), a foundation model designed for physics...
  </details>

- **2026-11-24** — Xinyi Hou, Shenao Wang, Wenhui Pan et al. — [Demystifying Real-world LLM Service Freeloading](http://arxiv.org/abs/2611.33218v1)
  <details><summary>📄 Abstract</summary>
  Third-party projects repackage free inference from LLM web applications and dedicated clients into independent APIs. We refer to such use beyond providers' permitted access, allocation, or redistribution conditions as LLM service freeloading (LSF). However, its scale and underlying mechanisms remain poorly understood. We present a systematic measurement study of 513 open-source projects, tracing 1,588 inference paths across 64 upstream LLM services and characterizing their development, dependenc...
  </details>

- **2026-11-24** — S M Zia Ur Rashid, Sazidul Islam Hira, Suman Rath — [Real Package, Wrong Controller: Static Auditing of Vendor--Protocol Mismatches in LLM-Generated PLC Code](http://arxiv.org/abs/2611.33227v1)
  <details><summary>📄 Abstract</summary>
  Language models can generate Python that drives industrial protocols on programmable logic controllers, yet existing code-grounding checks ask whether an imported package or symbol exists rather than whether it suits the declared industrial target. We define \emph{metadata-conditioned, import-level vendor--protocol incompatibility} and build \textsc{Proteus-OT}, a label-free static verifier over a version-pinned graph of documented bindings. Across 883 generated scripts, 180 carry an import-leve...
  </details>

- **2026-11-24** — Yisrael Clark, Guy Katz — [FOL-Proof: Verifying LLM Text-to-Logic Translations via Deterministic Semantics](http://arxiv.org/abs/2611.33078v1)
  <details><summary>📄 Abstract</summary>
  Large Language Models (LLMs) are increasingly used to translate natural-language statements into first-order logic (FOL) to improve reasoning. However, LLMs are prone to errors, and so a semantically unfaithful FOL formula could corrupt downstream reasoning. We present FOL-Proof, a semantic firewall pipeline that validates LLM-generated FOL translations against independently derived linguistic interpretations. FOL-Proof operates by deterministically obtaining a pool of candidate translations via...
  </details>

- **2026-11-24** — Nikolaos Kekatos, Antonio Anastasio Bruto da Costa, Alexios Lekidis et al. — [Sound Distributed Runtime Verification under Incomplete Evidence](http://arxiv.org/abs/2611.32868v1)
  <details><summary>📄 Abstract</summary>
  Distributed runtime verification often requires combining evidence from several nodes to check properties that cannot be evaluated locally. However, when messages are delayed, lost, or deliberately suppressed, the verifier may not know whether a violation occurred or whether the relevant evidence is missing. This creates a risk of incorrectly reporting compliance. We study the requirements for sound monitoring under these conditions. We first show that a deadline-bounded monitor cannot be simult...
  </details>

- **2026-11-24** — Zeming Fei, Hongming Fei, Jingwen Chen et al. — [When Answering Is Administering: Permission Replies That Rewrite Coding-Agent Policy](http://arxiv.org/abs/2611.32195v1)
  <details><summary>📄 Abstract</summary>
  Coding agents let plugins and remote services answer permission prompts, and Claude Code documents that such an answer cannot override the operator's deny rules. However, we show that this guarantee, checked one decision at a time, fails over a whole run, because an answer to one permission prompt can rewrite the policy that every later answer is checked against. For example, a remote service with no access to the operator's files approves an unrelated command and attaches an update that deletes...
  </details>

- **2026-11-24** — Parsa Nilforushan, Gemmin Sugiura, Kourosh Hashemi et al. — [Are Web Agents Still Detectable? Stress-Testing Bot Defenses with Coordinated Evasion](http://arxiv.org/abs/2611.31962v1)
  <details><summary>📄 Abstract</summary>
  AI web agents can autonomously navigate websites and complete various tasks. As their capabilities and adoption expand, evaluating bot defenses requires adversarial stress tests. Although prior work demonstrates that existing agents can remain detectable, it remains unclear how effective bot defenses are against adversaries that coordinate evasion across browser fingerprints, automation controls, and interaction behavior. To investigate this threat, we introduce DarkAgent, an autonomous web agen...
  </details>

- **2026-11-24** — Yue Xue, Yi Rong, Ziqiao Kong et al. — [Shuttle: Dependency-Attributed Workflow Evolution for Smart Contract Auditing](http://arxiv.org/abs/2611.31929v1)
  <details><summary>📄 Abstract</summary>
  In LLM-based smart contract auditing, detection quality depends on both model capability and workflow design. While coding agents can revise workflows from execution feedback, unconstrained rewrites rarely yield stable gains. Cross-function vulnerabilities require multi-step state tracking and boundary reasoning that coarse pipelines miss. End-to-end outcomes hide which step lost a clue, so direct rewrites regress existing hits or discard valid edits under coarse aggregate scoring. Repeatedly it...
  </details>

- **2026-11-24** — Ilia Hashemi Rad, Feijie Wu, Haoyu Wang et al. — [TACT-Bench: Testing Adaptive Conversational Threats against Tool-Use Agents](http://arxiv.org/abs/2611.31756v1)
  <details><summary>📄 Abstract</summary>
  The growing autonomy of AI agents in using external tools and making decisions has created an urgent need for comprehensive safety benchmarks. Existing benchmarks test compromised tool channels or adaptive multi-turn attacks, though they may not capture the unique capabilities of policy-governed tool-use agents, which must resist unauthorized requests without abandoning the legitimate work embedded in the same interaction. To fill this gap, we introduce TACT-Bench, a stateful benchmark built aro...
  </details>

- **2026-11-24** — Hao Wu, Sipeng Chen, Weikai Li et al. — [Towards Realistic Evaluation of Uncertainty Quantification for LLM-Based Recommender Systems](http://arxiv.org/abs/2611.33036v1)
  <details><summary>📄 Abstract</summary>
  Large language models (LLMs) provide a flexible interface for recommendation systems. However, their issued rankings require reliable instance-level uncertainty monitoring. In this scenario, comparing uncertainty quantification (UQ) methods becomes challenging because LLM rankers lack a standard item-classification head. Their scores may depend on option labels, prompts, generation procedures, and the available user and item evidence. Existing methods derive uncertainty from different sources an...
  </details>

- **2026-11-24** — Xiaogang Peng, Jiaqi Zou, Lei Zhong et al. — [MESSI: Multi-Expert Soccer Skill Integration for Physics-Based Character Control](http://arxiv.org/abs/2611.33011v1)
  <details><summary>📄 Abstract</summary>
  Physics-based soccer characters must perform diverse motor skills and transition smoothly between them, such as dribbling into a shot. However, skills that perform well in isolation may fail when executed sequentially, as preceding behaviors can leave the character and ball in unfamiliar states. We present MESSI (Multi-Expert Soccer Skill Integration), a framework that enables multiple soccer skill transitions through shared adaptation while preserving the original skill policy outside transitio...
  </details>

- **2026-11-24** — Gregory Bolet, Giorgis Georgakoudis, Konstantinos Parasyris et al. — [Estimating GPU Roofline Arithmetic Intensity with Off-the-Shelf LLMs and Compiler Artifacts](http://arxiv.org/abs/2611.32975v1)
  <details><summary>📄 Abstract</summary>
  GPU developers use profiling to understand computation and data movement, but access to target hardware can delay optimization. We investigate whether off-the-shelf large language models (LLMs) can estimate Roofline arithmetic intensity (the ratio of floating-point operations (FLOPs) to device-memory bytes) without executing the target GPU workload. We evaluate three models (deepseek-v4-flash, gemini-3.7-flash, and gpt-5.6-sol) across 179 combinations of five kernel families, four NVIDIA and AMD...
  </details>

- **2026-11-24** — Jiayu Tang, Yuchen Zhou, Hongsheng Wu et al. — [LookAnything: A Foundation Model for Holistic Gaze Following](http://arxiv.org/abs/2611.32351v1)
  <details><summary>📄 Abstract</summary>
  Human gaze provides a rich window into attention and intent, making its understanding essential for applications ranging from social signal analysis to human-robot interaction. Existing methods typically employ highly customized architectures relying on auxiliary inputs like head crops or depth maps, causing cascading errors and inference overhead. Trained on single domains and confined to isolated gaze following with heatmap outputs, they lack flexibility and generalization for diverse interact...
  </details>

- **2026-11-24** — Zizheng Guo, Yanqing Zhang, Nathaniel Pinckney et al. — [TimeTravelContainer: A Live Forking Sandbox for Stateful Agent Exploration](http://arxiv.org/abs/2611.32255v1)
  <details><summary>📄 Abstract</summary>
  LLM agents that drive stateful tools (e.g., interactive shells, design environments, simulation engines) frequently need to clone, backtrack, and parallelize live sessions to support exploration. However, cloning a live session today requires serializing the tool's in-memory state to disk or relaunching from scratch, both prohibitively slow for interactive exploration. Existing agent sandboxes based on microVMs or kernel patches either serialize full guest memory to storage or require privileged...
  </details>

- **2026-11-24** — Tim d'Hondt, Oleksii Furman, Damian Kwolek et al. — [Joint Classification and Generation on Tabular Data: an Empirical Study](http://arxiv.org/abs/2611.32225v1)
  <details><summary>📄 Abstract</summary>
  Many applications of machine learning on tabular data need both a classifier and a generator of realistic records. The default is to train two separate models, whereas a single joint model promises both from one set of weights. Several families of tabular deep learning models can be turned into such a joint model, which raises the question of which joint model is preferable at which computational budget. In this empirical study, we introduce and compare joint models based on four state-of-the-ar...
  </details>

- **2026-11-24** — Jun He, Deying Yu — [Provenance-Isolated Epistemic Quorums: Execution-Bound Evidence Certification and Plausible-World Safety Gating in Agentic Control Planes](http://arxiv.org/abs/2611.32032v1)
  <details><summary>📄 Abstract</summary>
  Agreement among large language models is not physical evidence for mutating production infrastructure. Because generative models share pretraining priors and conform to peer rationales during deliberation, voting ensembles correlate errors instead of providing independent fault tolerance; yet attaching rigid deterministic checks to unconstrained agent outputs paralyzes incident remediation. We present Provenance-Isolated Epistemic Quorums (PIEQ), an execution-bound certification layer that keeps...
  </details>

- **2026-11-24** — Shengkai Lyu, Hairui Zhao, Daran Sun et al. — [LIBRA: Runtime Co-Tuning of Batch Size and Parallelism for Time-Efficient LLM Training](http://arxiv.org/abs/2611.32008v1)
  <details><summary>📄 Abstract</summary>
  Training large language models (LLMs) requires choosing both a batch size and a parallel configuration. Existing systems make these decisions in isolation, tuning parallelism for throughput and batch size for convergence, but neither objective alone determines training efficiency. We present LIBRA, a lightweight runtime framework that co-tunes batch size and parallel configuration to minimize end-to-end time. LIBRA treats throughput and convergence as two noisy objectives and searches their join...
  </details>

- **2026-11-24** — Shifang Zhao, Haoyu Wang, Yuyang Yin et al. — [Coding4Games: Can Modern Coding Agents Play Modern Video Games?](http://arxiv.org/abs/2611.31974v1)
  <details><summary>📄 Abstract</summary>
  Games, especially modern AAA games, challenge language models to perceive complex scenes, control actions, and make decisions over long horizons. Existing game benchmarks primarily test language models as computer-use agents that query a language model throughout play, incurring repeated inference cost and, in real-time games, acting while the environment continues to evolve. We ask whether coding agents can learn from game interaction to develop standalone game-playing programs that run without...
  </details>

- **2026-11-24** — Aoqi Hu, Yueao Xing — [RepoEviAgent: Scalable Synthesis of Evidence-Grounded Repository-Level Question Answering Tasks](http://arxiv.org/abs/2611.31873v1)
  <details><summary>📄 Abstract</summary>
  Real-world software engineering (SWE) tasks require agents to understand repository structures, cross-module dependencies, and runtime behaviors, posing significant challenges for constructing high-quality training and evaluation data. To address this, we propose RepoEviAgent, a scalable SWE data construction framework that integrates quality-aware data curation and role-specialized multi-agent task synthesis. Starting from 8,477 open-source repositories and approximately 2.48 million pull reque...
  </details>

- **2026-11-24** — Zeyan Li, Jianfeng Xu — [FN-Prune: Training-Free Expert Pruning with Finite RMSNorm Perturbations](http://arxiv.org/abs/2611.31747v1)
  <details><summary>📄 Abstract</summary>
  Expert pruning reduces the memory footprint of mixture-of-experts language models, but retaining model quality depends on which experts are removed. Frequency- and magnitude-based scores measure the expert in isolation and overlook how normalization consumes its contribution: subtracting one expert changes both the direction of the residual stream and the scale applied to what remains. We propose FN-Prune, a training-free criterion that compares the next RMSNorm outputs before and after subtract...
  </details>

- **2026-11-24** — Nader Lobandi, Lombe Chileshe, Mohammad Mehdi Hosseini et al. — [BEARING: Who Is Talking to Whom? Grounding Acoustic Direction in Vision for Online Multi-Party Conversation](http://arxiv.org/abs/2611.31735v1)
  <details><summary>📄 Abstract</summary>
  Understanding a group conversation means deciding, from video and audio, who is speaking and to whom. Leading systems treat these tasks offline on single-channel clips and align models with a self-evaluation reward. We propose BEARING, a geometry-first alternative built on one measured signal: the direction from which a microphone array beside the camera hears a sound. A label-free calibration learned from the stream registers this direction into the camera image, and an online registry of faces...
  </details>

- **2026-11-24** — Neda Ghafouri — [Can LLM Judges Catch Unsafe Clinical Actions? A Fault-Injection Study](http://arxiv.org/abs/2611.33012v1)
  <details><summary>📄 Abstract</summary>
  As clinical AI agents begin to interact with electronic health records (EHRs), large language models (LLMs) are increasingly used to evaluate their actions. But how reliably can these judges recognize clinically dangerous mistakes, especially when an agent appears to have completed its task successfully? We investigate this question using MedAgentBench by introducing controlled clinical errors into verified agent trajectories. The experiments include 416 faulty trajectories, eight error categori...
  </details>

- **2026-11-24** — Xingjian Wang, Shijian Wang, Minghao Liu et al. — [SpecEngineeringBench: Evaluating Coding Agents as Autonomous Specification Engineers](http://arxiv.org/abs/2611.32973v1)
  <details><summary>📄 Abstract</summary>
  Autonomous specification engineering requires coding agents to translate functional requirements into executable tests and use the results to discover and validate defects. However, existing benchmarks evaluate coding agents on explicitly specified test generation tasks, commonly providing an issue description, a designated test entry point, or files to inspect, leaving the ability to determine what to test and where to investigate insufficiently evaluated. Relying on such clues bypasses the cha...
  </details>

- **2026-11-24** — Jingcheng He, Zinan Zhao, Wenguang Sun et al. — [Simultaneous Inference for Watermark Proportions in LLM-Generated Text](http://arxiv.org/abs/2611.32674v1)
  <details><summary>📄 Abstract</summary>
  Watermarking enables detection of text generated by large language models, but practical review also requires quantifying retained signals within content of interest. Readers may choose passages based on their content and refine their selections after examining the watermark evidence. We develop simultaneous lower confidence bounds on the fraction of selected tokens that retain a watermark signal. The bounds hold jointly for the full document and any passages selected during review. We develop s...
  </details>

- **2026-11-24** — Cyril Perosino, Rino Di Chiara, Hamida Seba — [On the Effectiveness of Resampling for Supervised Graph Anomaly Detection](http://arxiv.org/abs/2611.32598v1)
  <details><summary>📄 Abstract</summary>
  Class imbalance and scarce anomaly labels motivate oversampling in supervised graph anomaly detection (GAD), but its benefits across detectors and benchmarks remain unclear. In the low-label setting of GADBench, with 20 labelled anomalies and 80 labelled normal nodes, we compare class weighting and up to six oversampling strategies in ten detector configurations from three families: graph neural networks (GNNs), tree ensembles on neighbourhood-aggregated features, and tabular foundation models, ...
  </details>

- **2026-11-24** — Shangze Li, Chuancheng Shi, Simiao Xie et al. — [UnifiedAD: One-Shot Anomaly Detection across Modalities via Evidence Calibration](http://arxiv.org/abs/2611.32551v1)
  <details><summary>📄 Abstract</summary>
  Both single-modal and multi-modal anomaly detection aim to identify deviations from normal patterns, providing a common foundation for unified detection. However, existing methods rely on modality-specific modeling and scoring, making it difficult to obtain comparable anomaly evidence with limited normal references. To that end, we propose UnifiedAD, which unifies single-modal and multi-modal anomaly detection through anomaly evidence calibration, requiring only one normal reference per target c...
  </details>

- **2026-11-24** — Ameya Uppina, S Navaneetha Krishnan, Nikhil N Iyer et al. — [Advanced Synthetic Image Detection Using Hybrid Feature Extraction](http://arxiv.org/abs/2611.32538v1)
  <details><summary>📄 Abstract</summary>
  In the realm of generative AI, models such as GANs, MidJourney, DALL-E, and others have been continuously evolving to generate increasingly lifelike images. This rapid advancement has created an urgent need for robust methods to distinguish between real and AI-generated images. This paper proposes a novel approach for the detection of synthetic images by employing deep learning techniques for feature analysis. The proposed architecture classifies images by identifying variations that generative ...
  </details>

- **2026-11-24** — Daniel Pröll, Sebastian Hegenbart — [One Subspace Is Not Enough: LocalSubspaceAD for Training-Free Few-Shot Anomaly Detection](http://arxiv.org/abs/2611.32424v1)
  <details><summary>📄 Abstract</summary>
  Defect-free industrial samples can vary considerably in appearance, texture, and geometry. In few-shot anomaly detection, this variability has to be modeled from only a handful of images. SubspaceAD showed that a single principal subspace of foundation-model patch features is a strong training-free model of nominal appearance. However, a single subspace has to cover all of the nominal data's variability, so a deviation that is anomalous for one semantic region can be within the nominal variabili...
  </details>

- **2026-11-23** — Jake Watts, Joel Sokol — [Monitorable-by-design architectures for a post-Astra world: a compartmentalization-based approach](http://arxiv.org/abs/2611.31610v1)
  <details><summary>📄 Abstract</summary>
  Frontier models like GPT-6 Astra are increasingly able to do substantial reasoning without a monitorable chain of thought, chains of thought are becoming less legible, and are often monitored asynchronously to reduce cost. With the future of chain of thought monitoring unclear, it may be necessary to design LLMs with monitorability in mind. We propose a modification to existing LLM architectures based on GRAM, SGTM, DEMix, BTS, and similar methods to compartmentalize dangerous capabilities so th...
  </details>

- **2026-11-23** — Kunwar Sangram Singh, Krishna Mohan Guda Nagavenkata Srinivasa — [Where Agent Defenses Fail: A Case Study of Policy Compositions and Measurement Limits](http://arxiv.org/abs/2611.31541v1)
  <details><summary>📄 Abstract</summary>
  A coding agent may need to upload a report while its sandbox blocks network access. A host mediator can restore delivery, but an injected instruction may add a secret to the approved request. We study this interaction using files and HTTP receipts to measure effects independently of control logs. Two prospective frozen-input cohorts comprise 110 and 300 runs on previously explored authored tasks. Restrictive sandboxing produces no observed attack harm but reduces benign utility to 6/8 and 12/24....
  </details>

- **2026-11-23** — Mohammed Nayeem Khan, Akhil P — [Antares-Smaug: Adversarial Names, Tokens and Attack Rewrites: Sanitisers Miss Unseen Generalisations](http://arxiv.org/abs/2611.31347v1)
  <details><summary>📄 Abstract</summary>
  Laya is an open decision model: given a text, a question and K named options with descriptions, it returns one probability per option in a single pass, and software may act on the answer unseen. We attack six Laya models with 81 programmatic edits of 566 synthetic items (injected sentences, label leaks, edited descriptions, decoy options, invisible and look-alike characters, floods) and report the share of correctly answered items hijacked or lost, with bootstrap intervals. Attack wordings that ...
  </details>

- **2026-11-23** — Jie Ma, Junqing Zhang, Guanxiong Shen et al. — [Open-Set Radio Frequency Fingerprint Identification with Feature Fusion and Vision Transformer](http://arxiv.org/abs/2611.31636v1)
  <details><summary>📄 Abstract</summary>
  Radio frequency fingerprint identification (RFFI) is a promising device authentication technique for the Internet of Things (IoT) that leverages hardware impairments to uniquely identify devices. However, most existing RFFI systems operate under a closed-set assumption and lack the ability to detect rogue devices, which poses significant security risks. In this paper, we propose an open-set RFFI approach that jointly performs rogue device detection and legitimate device classification. Specifica...
  </details>

- **2026-11-23** — Zhengye Yang, Anthony Wang, Yuyang Li et al. — [Adapt, Label, Distill: Foundation-Model Supervision for Efficient Object Detection](http://arxiv.org/abs/2611.31604v1)
  <details><summary>📄 Abstract</summary>
  Object detectors often transfer poorly to specialized domains, where box annotations are scarce and deployment requires compact, real-time models. Large vision foundation models can provide offline supervision, but their zero-shot predictions may be poorly aligned with the target domain. We present an adapt-label-distill pipeline that uses limited target annotations to specialize a foundation teacher and transfer its supervision to compact detectors. We adapt SAM3 on the labeled subset, generate...
  </details>

- **2026-11-23** — Satiyabooshan Murugaboopathy, Adel Daoud, Connor T. Jerzak — [LUCID: Statistically Grounded Self-Correction for LLM Reasoning Evaluation](http://arxiv.org/abs/2611.31595v1)
  <details><summary>📄 Abstract</summary>
  Cheap language-model raters grade chain-of-thought reasoning at scale, yet systematic step-rating errors can skew reasoning audits and solution rankings. We introduce LUCID (Loop for Unbiased Calibration via Inference-time Diagnosis), which pairs prompt self-correction with Design-based Supervised Learning (DSL). Without retraining or weight access, LUCID calibrates binary step ratings by aligning predicted and expert soundness rates. From a small expert-labeled set, LUCID summarizes rater bias ...
  </details>

- **2026-11-23** — Rohit Gheyi, Anderson Uchôa, Wesley Assunção et al. — [Decision Models for Definition-Driven GitHub Actions Workflow Smell Detection](http://arxiv.org/abs/2611.31421v1)
  <details><summary>📄 Abstract</summary>
  GitHub Actions workflows automate continuous integration and delivery (CI/CD), and workflow smells are recurring configuration patterns that may weaken security, hinder maintenance, or waste resources. Extending static analyzers to new smells requires encoding constructs, applicability conditions, and exceptions in detection rules. We investigate definition-driven detection, in which models assess workflows against reusable natural-language smell definitions, focusing on decision-oriented models...
  </details>

- **2026-11-23** — Ankit Gupta, Christoph Adami, Emily Dolson — [Query Obfuscation with Embedding-Optimized Noise (EON): A Representational Blindspot in Agentic Retrieval](http://arxiv.org/abs/2611.31344v1)
  <details><summary>📄 Abstract</summary>
  In modern agentic and semantic retrieval systems, dense embedding models increasingly determine which intent, tool, document, memory, or image to retrieve for a query. We identify a representational failure mode in this pipeline: a meaningful query can be replaced by visibly nonsemantic content while preserving much of its retrieval outcome, even when the candidate bank is hidden from the optimizer. We introduce Embedding-Optimized Noise (EON), constructed using only the natural query representa...
  </details>

- **2026-11-23** — Ayesha Sahar, Tahir Mustafa Madni, Tehseen Zia et al. — [One Size Doesn't Fit All: Input Adaptive Class Activation Mapping for Improved Visual Explanations](http://arxiv.org/abs/2611.29993v2)
  <details><summary>📄 Abstract</summary>
  Despite their widespread use in tasks such as image classification, object detection and semantic segmentation, the limited interpretability of Convolutional Neural Networks (CNNs) and Vision Transformers (ViTs) can undermine trust and hinder adoption in safety-critical applications. Explainable artificial intelligence (XAI) methods seek to address this by providing human-understandable explanations for model predictions. Class Activation Maps (CAM) constitute one such widely used XAI technique ...
  </details>


### 📂 alignment
*对齐与安全约束 / Alignment & Safety Constraints* — 60 papers

- **2026-11-25** — Tianru Zhang, Mayank Nautiyal, Hugo Eidmann et al. — [ProbFaS: Probabilistic Video Frame Selection for MLLMs via Multi-Fidelity Calibration](http://arxiv.org/abs/2611.34903v1)
  <details><summary>📄 Abstract</summary>
  Processing long videos with multimodal large language models (MLLMs) is prohibitively expensive, making informative frame selection essential for accurate video understanding. The default uniform sampling often misses task-relevant keyframes, while recent training-free selectors instead pick frames by how well each one matches the question under an image-text alignment (ITA) score. However, we show that ITA signals correspond poorly with the MLLM's true needs: their rankings correlate weakly wit...
  </details>

- **2026-11-25** — Insup Lee, Hojin Jeon, Sunguk Shin et al. — [RePace: Reasoning about Demonstration Speedup for Faster Vision-Language-Action Policies](http://arxiv.org/abs/2611.34864v1)
  <details><summary>📄 Abstract</summary>
  Since vision-language-action (VLA) policies can inherit the slow pace of human demonstrations, accelerating these demonstrations before fine-tuning can lead to faster VLA policies without an additional speed-selection module at deployment. Several offline speedup methods have focused on identifying segments that require less precision and assigning predefined speedup factors to the segments. However, even within a single segment, a speedup factor suitable for steady motion may be too high when p...
  </details>

- **2026-11-25** — Tingrui Huang, Yuanyuan Deng, Qingren Yao et al. — [Put the World Back: Timestamps Matter in Time Series Reasoning](http://arxiv.org/abs/2611.34848v1)
  <details><summary>📄 Abstract</summary>
  Large language models (LLMs) are increasingly applied to time series reasoning. However, current evaluations often give models events in chronological order and already matched to the time series. This makes it unclear whether models use timestamps to connect events with observations or simply take shortcuts. To expose this ambiguity, we reformulate time series reasoning from a world-to-series projection perspective, viewing timestamps as explicit indices that connect numerical observations and ...
  </details>

- **2026-11-25** — Bich Ngoc Doan, Hanna Yukhymenko, Imanol Schlag — [PersonaFactory: Stylistic User Prompt Augmentation with Synthetic Persona Bank](http://arxiv.org/abs/2611.34785v1)
  <details><summary>📄 Abstract</summary>
  Large language models increasingly replace real people in the AI development pipeline, as they are used to generate training dialogues at scale and to drive alignment and evaluation. However, out-of-the-box models produce monolingual and stylistically flat texts as synthetic user prompts, failing to replicate the real user-AI communication mechanics. We present PersonaFactory, an end-to-end pipeline that generates detailed user personas and uses them to augment existing user prompts from their p...
  </details>

- **2026-11-25** — Yiqian Yang, Yiqun Duan — [Technical Report MEG2text: Beyond Alignment in Non-Invasive Brain-to-Text](http://arxiv.org/abs/2611.34686v1)
  <details><summary>📄 Abstract</summary>
  Non-invasive brain-to-text seeks to recover language from brain activity without surgery. A central challenge is turning learned brain-language representations into accurate word predictions. We present MEG2text, a decoding system that combines corrected training and evaluation, brain-text alignment, a class-balanced word readout, and target-word language-model fusion. On LibriBrain100's word-ranking task, MEG2text reaches 64.12% mean Top-10 balanced accuracy, improving on published MEG-XL by 16...
  </details>

- **2026-11-25** — Bo Leng, Baoyun Wang, Wenxin Wen et al. — [FeaXDrive2: Body-Scene Spatial Grounding for Feasibility-Aware Generative Driving](http://arxiv.org/abs/2611.34658v1)
  <details><summary>📄 Abstract</summary>
  Generative driving planners may produce trajectories that appear feasible at their reference points but violate environmental constraints over the full vehicle body. We propose FeaXDrive2, an end-to-end generative planning framework that enhances vehicle-embodied spatial feasibility (VESF) through body-scene spatial grounding. The proposed method constructs spatial queries from actual vehicle-body corners and dynamically updates visual sampling locations using evolving trajectory estimates acros...
  </details>

- **2026-11-25** — Nikita Sorokin, Zoya Volovikova, Alexey Skrynnik et al. — [ZeroHero: Training Small Language Agents from Scratch](http://arxiv.org/abs/2611.34635v1)
  <details><summary>📄 Abstract</summary>
  Large pretrained language models provide capable policies for interactive tasks, but how much model capacity is necessary for a specialized language agent? We introduce ZeroHero, a framework for training small language agents (SLAs) from scratch. In each environment, a large language model acts as the expert, and we collect its successful trajectories. We pretrain each SLA, which has fewer than 50 million parameters, to predict the expert's responses given the interaction history. We then post-t...
  </details>

- **2026-11-25** — Xuheng Gao, Yuhan Pang, Bi-Ke Zhu et al. — [Geometric Acceleration Obstacles: Physical Boundary Structure and Affine Safety Certificates](http://arxiv.org/abs/2611.34586v1)
  <details><summary>📄 Abstract</summary>
  Safe robot navigation in dynamic environments requires collision avoidance that respects motion constraints while remaining computationally efficient. Conventional velocity-obstacle (VO) methods characterize collision-inducing motions in velocity space. Although some formulations account for acceleration-limited velocity transitions, their collision constraints remain tied to specific velocity-tracking models. Acceleration obstacles (AO) address this limitation by representing collision-inducing...
  </details>

- **2026-11-25** — Lingxiang Hu, Zhenjun Zhao, Qi Shao et al. — [ProManO: Beyond Sim(3) for Metric Upgrade of Feed-Forward Geometry with Visual-Inertial Anchors](http://arxiv.org/abs/2611.34480v1)
  <details><summary>📄 Abstract</summary>
  Upgrading feed-forward geometry to metric scale with visual-inertial odometry (VIO) raises the question of which correction should align dense feed-forward prediction with sparse metric VIO anchors. Existing methods use either a similarity transformation, which cannot represent depth-dependent distortion, or a projective transformation, which alters pre-calibrated intrinsics. We prove that the transformations compatible with pre-calibrated intrinsics form a ten-dimensional manifold. Beyond Sim(3...
  </details>

- **2026-11-25** — Chaewon Kim, Sangheon Lee, Seyeon Choi et al. — [LUDIUS: A Benchmark for Embodied Social Intelligence in Everyday Human-Robot Interactions](http://arxiv.org/abs/2611.34328v1)
  <details><summary>📄 Abstract</summary>
  Social intelligence in a robot requires interpreting a situation from the perspectives of the people involved and using that understanding to decide when and how to act. We introduce LUDIUS, a benchmark for evaluating how vision-language models exercise this judgment through a robot's verbal responses and actions, organized around 15 social intelligence skills drawn from social psychology, sociology, and cognitive science. LUDIUS comprises six editions, each a collection of episodes spanning one...
  </details>

- **2026-11-25** — Zhiyu Tao, Mike Thelwall, Danqun Zhao et al. — [Can Large Language Models Estimate the Likely Technological Impact of Scientific Research? Evidence from Biotechnology](http://arxiv.org/abs/2611.34300v1)
  <details><summary>📄 Abstract</summary>
  This study provides large-scale empirical evidence about whether large language model (LLM)-based assessments of the likely technological impact of scientific publications are associated with their patent-based impact. Using Lens.org, we constructed a biotechnology dataset of 107,615 papers published between 1980 and 2015 with their patent citation counts. We used GPT-5-mini, Qwen-Flash, and DeepSeek-V3.2 to estimate papers technological impact and technology relevance, benchmarking model output...
  </details>

- **2026-11-25** — Dewei Kong — [TigerTTS: Draft-Guided Multi-Frame Parallel Speech-Token Language Model for Fast and Robust Text-to-Speech](http://arxiv.org/abs/2611.34241v1)
  <details><summary>📄 Abstract</summary>
  Autoregressive speech-token language models enable high-quality TTS but suffer from latency growth with sequence length, word omission or repetition without explicit alignment, and fidelity limits from discrete codebooks. We present TigerTTS, a production-grade LLM TTS system built around a lightweight non-autoregressive NAR model. With explicit alignment, the NAR model drafts tokens for the entire utterance, which are refined frame-by-frame by a compact autoregressive LLM. The draft is aligned ...
  </details>

- **2026-11-25** — Minyeong Jeong, Yeonju Kim, Yong Man Ro — [Modality-Shift Contrastive Decoding for Temporally Grounded Audio-Visual Understanding](http://arxiv.org/abs/2611.34162v1)
  <details><summary>📄 Abstract</summary>
  Audio-visual large language models (AV-LLMs) are designed to represent the temporal structure of audio and video, yet it remains unclear how effectively they use this temporal information to relate sounds to visual events. To examine this, we probe an AV-LLM on an audio-visual synchronization task by shifting the audio so that the queried sound overlaps a different visual event. We observe that the model still favors the originally aligned event over the newly aligned one, indicating limited sen...
  </details>

- **2026-11-25** — Pusala Pavan Teja, Jayasimha Talur, Saab Mansour et al. — [Reliable User Simulation in Complex Multi-Step Workflows](http://arxiv.org/abs/2611.34044v1)
  <details><summary>📄 Abstract</summary>
  LLM-based user simulators are increasingly used to evaluate conversational assistants. Yet, these simulators can drift from their assigned goals or fail to exhaustively explore all specified options, causing evaluation errors incorrectly attributed to the assistant. Prior work has examined goal alignment in single-task settings, but many practical scenarios require simulators to execute multi-step workflows with sequential tasks, fallback logic, and cross-task dependencies, where simulator fidel...
  </details>

- **2026-11-25** — Yun Chen, Munchurl Kim, Jeonghyeok Do — [MoSk: A Unified Motion-Skeleton Foundation Model for Human Motion Understanding and Generation](http://arxiv.org/abs/2611.34022v1)
  <details><summary>📄 Abstract</summary>
  Foundation models (FMs) have advanced visual understanding and generation by providing semantically rich representations. However, this role of FMs remains underexplored in human motion. Large motion datasets offer diverse movements at scale, but often lack action labels for systematically evaluating learned representations on understanding tasks. Skeleton datasets enable such evaluation through established recognition protocols, yet are typically smaller and focus on predefined actions captured...
  </details>

- **2026-11-25** — Zhuoran Yang, Junchen Yu, Runmin Zhang et al. — [Rethinking Unsupervised Cross-Modal Homography Estimation:Spatially Aware Representations and Geometric Consistency Learning](http://arxiv.org/abs/2611.34021v1)
  <details><summary>📄 Abstract</summary>
  Unsupervised cross-modal homography estimation is challenging because appearance differences obscure shared geometric structures. Separating modality transfer from homography estimation helps reduce these differences, but accurate alignment still requires effective geometric representations and consistency constraints on the two subtasks. We propose GeoCo (Geometry-Aware and Consistency-Constrained Homography Estimation), a framework that addresses these two requirements without cross-modal tran...
  </details>

- **2026-11-25** — Fangyu Sun, Guanyan Wu, Yang Deng et al. — [Ask to Land: Learning a Mask-Conditioned Open-Vocabulary Landing Policy via Differentiable Physics](http://arxiv.org/abs/2611.34020v1)
  <details><summary>📄 Abstract</summary>
  Existing drone landing systems, whether model-based or learning-based, typically rely on predefined visual markers (e.g., ArUco tags) or are trained for specific platform categories, and often assume structured target motion. Recent open-vocabulary studies enable text-prompted target selection, but integrating this capability with learned closed-loop landing control remains underexplored. To this end, we present \textit{Ask to Land}, a mask-conditioned framework that enables a quadrotor to land ...
  </details>

- **2026-11-25** — Guang Huang, Zeyi Wen — [Asymmetric Speculative Decoding: Unlocking In-Context Learning in Draft Models](http://arxiv.org/abs/2611.34010v1)
  <details><summary>📄 Abstract</summary>
  Speculative decoding addresses Large Language Model (LLM) inference latency by first drafting and then verifying in parallel. Yet practical speedups fall far short of theoretical bounds, especially on reasoning tasks. We identify the root cause as task isomorphism: existing methods provide identical prompts to both models, forcing the draft model to solve problems beyond its capacity. This produces high rejection rates that eliminate parallelization gains. We discover that acceptance rates incre...
  </details>

- **2026-11-25** — Nannan Zhang, Ting Huang, Zeyu Zhang et al. — [3D CoCa v3: Contrastive Learners with Scene Graphs for Urban Scene Understanding](http://arxiv.org/abs/2611.33835v1)
  <details><summary>📄 Abstract</summary>
  Understanding large-scale 3D urban scenes requires representations that capture both multi-scale geometric structures and complex spatial relationships. However, existing 3D vision-language methods primarily emphasize global semantic alignment or object-level representations, leaving structured relational modeling underexplored within unified contrastive and generative frameworks. In this paper, we present 3D CoCa v3, a scene-graph-enhanced contrastive and generative framework for urban 3D scene...
  </details>

- **2026-11-25** — Zhaoxin Fan, Jian Yang, Kejian Wu et al. — [MotionODE: Enhancing Autoregressive Text-to-Motion Generation with Continuous-Depth Modeling](http://arxiv.org/abs/2611.33826v1)
  <details><summary>📄 Abstract</summary>
  Autoregressive text-to-motion generation requires local motion predictions to reconcile cross-temporal textual requirements with the available motion context. While existing methods primarily improve motion representations and generation order, the internal formation of conditioned motion representations remains less explored. We introduce MotionODE, a continuous-depth post-training framework that refines hidden-state evolution in pretrained autoregressive generators. MotionODE reinterprets sele...
  </details>

- **2026-11-25** — Qirui Wang, Hengwei Zhao, Xiaoshu Yang et al. — [Bridging Transferability and Discriminability via Positive-Unlabeled Domain Adaptation for Building Damage Mapping Across Disaster Events](http://arxiv.org/abs/2611.33790v1)
  <details><summary>📄 Abstract</summary>
  Mapping the damage to buildings following natural and human-caused disasters is essential for disaster response and humanitarian assistance. However, differences in hazard types, geographic environments, building characteristics, and imaging conditions cause cross-event distribution shifts that limit the generalization of deep learning models to new disaster events, even for geospatial foundation models (GFMs) pretrained on extensive Earth observation data. Unsupervised domain adaptation (UDA) c...
  </details>

- **2026-11-25** — Yu Yang, Jiafeng Song, Baraa F Abed et al. — [InterGenEHR$^+$: An Interactive Framework for Natural Language-Conditioned Generation of Longitudinal Patient Trajectories](http://arxiv.org/abs/2611.33788v1)
  <details><summary>📄 Abstract</summary>
  Objective: To develop and validate InterGenEHR$^+$, an interactive framework for natural language-conditioned generation of synthetic tabular electronic health records (EHRs) and longitudinal trajectories for scenario-based evaluation of machine learning models.   Methods: An optional large language model (LLM) parser converts clinical requests into structured constraints. Conditional variational autoencoders and diffusion models generate single-time-point records, while diffusion models generat...
  </details>

- **2026-11-25** — Tangyuan Zhang, Zhuang Li, Fatemeh Shiri et al. — [NORMCRAFT: Cultural Norm Generation for Context-Aware Language Model Alignment](http://arxiv.org/abs/2611.33726v1)
  <details><summary>📄 Abstract</summary>
  Cultural alignment requires large language models (LLMs) to infer often-implicit social norms from a scenario and its cultural context. Existing approaches typically adapt individual models or supply external cultural knowledge, while learning norm inference independently of downstream response generation remains underexplored. We introduce NORMCRAFT, a modular framework that decouples norm inference from response generation. Through norm-centric multi-view supervision, we train an LLM as a norm...
  </details>

- **2026-11-25** — Ting Lei, Yu Chen, Yang Liu — [EVA: Evidence-seeking Visual Agent for Hallucination-Resistant Multimodal Reasoning](http://arxiv.org/abs/2611.33706v1)
  <details><summary>📄 Abstract</summary>
  Hallucinations in multimodal large language models (MLLMs) often arise from visual assumptions that go unchecked. Self-reflection, multi-agent debate, and counterfactual verification can reinforce erroneous conclusions when they rely on the same unverified visual assumptions. External visual tools can provide verifiable evidence, but models may select the wrong tools, supply incorrect parameters, or ignore or contradict the evidence they obtain. In this work, we propose EVA, an Evidence-seeking ...
  </details>

- **2026-11-25** — Tianle Lyu — [Recall4D: Forgetting, Not Misalignment, Limits Long-Horizon Feed-Forward 4D Reconstruction](http://arxiv.org/abs/2611.33655v1)
  <details><summary>📄 Abstract</summary>
  Feed-forward 4D trackers recover camera motion, depth, and point trajectories from short video clips, but chaining windows over long videos degrades their accuracy. We find that replacing inter-window alignment with ground-truth transforms leaves tracking error essentially unchanged. Static-point error instead grows with time since last observation: repeatedly predicting a static point from windows that no longer observe it corrupts previously recovered geometry. We call this failure forgetting....
  </details>

- **2026-11-25** — Mingyu Zhang, Jiejie Qin, Jianhui Ji et al. — [OneQuery: Unified Sequence-to-Structure Generation for Multilingual E-commerce Query Understanding](http://arxiv.org/abs/2611.33653v1)
  <details><summary>📄 Abstract</summary>
  Multilingual e-commerce search requires robust query understanding to convert cross-lingual user queries with varied linguistic patterns into standardized semantic representations that support retrieval and ranking. However, traditional Query Understanding systems suffer from error accumulation, separately optimized subtasks that ignore their mutual correlations, and high maintenance costs. To address these issues, this paper proposes OneQuery, a unified generative framework for multilingual que...
  </details>

- **2026-11-24** — Romeo De Timmerman, Thomas Demeester, Els Lefever — [Evaluating Large Language Models on conversational African American English: Feature classification and next-turn generation](http://arxiv.org/abs/2611.33499v1)
  <details><summary>📄 Abstract</summary>
  Large Language Models (LLMs) are known to misinterpret and misrepresent regional and social varieties of English other than Mainstream American English (MAE), such as African American English (AAE), yet most evaluations of these biases have relied on synthetic, stylized or decontextualized data. This paper instead evaluates LLMs on authentic, conversational AAE to more closely reflect how such models may encounter AAE when deployed as chatbots. Concretely, we perform two complementary evaluation...
  </details>

- **2026-11-24** — Sergei Koltcov, Vera Ignatenko, Anton Surkov et al. — [Scalpel and Brush: Pruning and Targeted Weight Editing of a Small Language Model by a Single LLM Agent](http://arxiv.org/abs/2611.33426v1)
  <details><summary>📄 Abstract</summary>
  It has recently been shown that an LLM can itself edit the weights of a language model, yet it remains unclear which part of such a result is due to the agent and which part is reproduced by a random edit of the same shape, by an instruction in the prompt, or by a standard procedure without an LLM. We unify repair and pruning as sparse weight edits to optimize a metric we specify, using BLEU as an example: three tasks -- targeted weight repair ("brush"), structured MLP neuron pruning ("scalpel",...
  </details>

- **2026-11-24** — Albert Chiwara, Erhan Guven — [A Semantics-First Approach to Multimodal Video Captioning with Frozen Encoders and Stabilized Reinforcement Learning](http://arxiv.org/abs/2611.33409v1)
  <details><summary>📄 Abstract</summary>
  We propose the Audio-Visual Query Transformer (AVQFormer), a highly efficient architecture built upon a 2.7B parameter LLM featuring a fixed-length $K=16$ semantic alignment module, stabilized via Adaptive Self-Critical Sequence Training (ASCST) with Entropy Regularization. Multimodal Large Language Models (LLMs) often rely on global audio representations to compensate for inefficient, frame-based visual encoders. While our Phase 1 prompted evaluations demonstrate that the Multimodal Base Model ...
  </details>

- **2026-11-24** — Sujong Shin, Sang-Il Choi, Kwang Moo Yi — [Synchronizing Cameras via 3D Object Relationships](http://arxiv.org/abs/2611.33387v1)
  <details><summary>📄 Abstract</summary>
  In this paper, we synchronize multiple videos of the same dynamic event through object relationships. Driven by dynamic reconstruction and novel view synthesis, many recent synchronization methods rely on pixel-level evidence, such as point correspondences across views or the photometric losses of a reconstructed scene. In dynamic scenes, however, fast motion and occlusions make the moving regions that carry much of the timing information hard to match across views. We thus propose to bring back...
  </details>

- **2026-11-24** — Hamed Poursiami, Ahmad Tahmasivand, Farshad Soleiman et al. — [HDMark: Holographic Multi-Bit Model Watermarking for Intellectual Property Protection in Hyperdimensional Computing](http://arxiv.org/abs/2611.31781v1)
  <details><summary>📄 Abstract</summary>
  Hyperdimensional computing (HDC) models deployed on edge hardware are valuable intellectual property that is easy to steal, since a trained classifier consolidates its learned knowledge into a compact set of class prototype hypervectors; yet protecting their ownership through watermarking remains largely unexplored. We present HDMark, the first model watermarking framework native to HDC, which encodes ownership in the same hyperdimensional algebra the model computes with. HDMark maps a multi-bit...
  </details>

- **2026-11-24** — Zehan Zheng, Yanyuan Chen, Deming Li et al. — [Lost on Campus: Evaluating Embodied Spatial Reasoning of Vision-Language Models in the Wild](http://arxiv.org/abs/2611.33145v1)
  <details><summary>📄 Abstract</summary>
  Embodied Spatial Reasoning (ESR) is central to deploying Vision-Language Models (VLMs) in real-world embodied tasks, yet remains inadequately evaluated. Existing benchmarks primarily assess spatial reasoning in static images or synthetic indoor environments, where semantic shortcuts often suffice, making it difficult to faithfully evaluate spatial reasoning capabilities in the wild. In light of this, we present Lost on Campus, a benchmark for evaluating ESR in large-scale real-world outdoor 3D e...
  </details>

- **2026-11-24** — Erfei Cui, Shengjia Zhao, Yan Qin et al. — [EmbodiSafety: Benchmarking Risk Understanding and Response in Embodied AI](http://arxiv.org/abs/2611.33054v1)
  <details><summary>📄 Abstract</summary>
  Progress in embodied foundation models is largely measured by task success, while the physical safety of their decisions remains underexamined. Safety evaluations centered on rule following and binary judgments do not adequately assess whether embodied models understand environmental hazards and make safe decisions. We introduce EmbodiSafety, comprising 1,092 snapshot tasks and 540 trajectory tasks across 844 visual scenarios to assess safety over short and long horizons. Six response modes cove...
  </details>

- **2026-11-24** — Yanlai Yang, Minki Kang, Divyam Madaan et al. — [Latent Merger: Latent-Space Composition of Hypernetwork-Generated LoRAs](http://arxiv.org/abs/2611.33048v1)
  <details><summary>📄 Abstract</summary>
  Recent work proposes hypernetworks that convert a document into a low-rank parameter update (LoRA) in a single forward pass, enabling fast injection of new knowledge into a frozen LLM. However, storing separate LoRA adapters for each document can be unsustainable in streaming settings. In this paper, we study the problem of composing hypernetwork-generated LoRAs using two representative systems, Doc-to-LoRA and SHINE. We show that hypernetwork-generated LoRAs have a geometry sharply different fr...
  </details>

- **2026-11-24** — Jordan Kennedy, Federico Oliva, Amir Degani et al. — [Multi-Agent Coordination Through Stigmergy for Canal Network Formation on Real Terrain](http://arxiv.org/abs/2611.32966v1)
  <details><summary>📄 Abstract</summary>
  Terrain-modifying robot swarms operating in unstructured outdoor environments must coordinate under uncertain dynamics despite unreliable communication and incomplete global information. Stigmergy offers a decentralized alternative by allowing agents to coordinate indirectly through persistent environmental modifications, yet its application to large-scale terrain construction on real landscapes remains largely unexplored. Inspired by beaver canal construction, we present a minimal stigmergic fr...
  </details>

- **2026-11-24** — Zhongyao Wang, Lun Song, Yakun Zeng et al. — [Path-probability gradients for optimizing force fields against dynamical observables](http://arxiv.org/abs/2611.32851v1)
  <details><summary>📄 Abstract</summary>
  Machine learning force fields inherit the errors of the electronic-structure methods used to generate their training data, and refining them against experimental measurements provides a direct route beyond this limit. However, such refinement remains difficult for dynamical observables because differentiating chaotic molecular trajectories yields unstable gradients. Here, we introduce PathGrad, which differentiates Langevin path probabilities instead of the trajectories themselves. The resulting...
  </details>

- **2026-11-24** — Jiajun Shen, Chuancheng Shi, Jiayi Lyu et al. — [SAVERA: Bridging Frozen Vision and Language Models via Sparse Alignment and Visual Evidence Reuse](http://arxiv.org/abs/2611.32828v1)
  <details><summary>📄 Abstract</summary>
  Independently pretrained vision and language models may learn shared structures of the same underlying world, providing a foundation for combining them to build multimodal capabilities. However, a key challenge remains in aligning cross-modal feature representations while preserving access to visual information before and after language adaptation. To this end, we propose sparse alignment with visual evidence-guided residual adaptation (SAVERA), a framework that combines frozen vision and langua...
  </details>

- **2026-11-24** — Yujie Sun, Zeqing Wang, Shuang Liang et al. — [Beyond Image-Text Pairs: Aligning Semantic Changes for Fine-Grained Visual Understanding](http://arxiv.org/abs/2611.32817v1)
  <details><summary>📄 Abstract</summary>
  Image-text alignment serves as a foundation for modern vision-language models (VLMs), yet prevailing training paradigms provide limited supervision for learning how semantic changes correspond across modalities. To address this limitation, we propose a post-training method that learns cross-modal semantic change correspondences through controlled visual and textual variations. Specifically, we introduce a Semantic Difference Alignment (SDA) loss which can align the directions of corresponding vi...
  </details>

- **2026-11-24** — Yu Chen, Haosen Yang, Su Ee Tan et al. — [SpatialArena: Where Do Geometric Foundation Models Stand?](http://arxiv.org/abs/2611.32816v1)
  <details><summary>📄 Abstract</summary>
  3D perception is shifting from task-specific pipelines to geometric foundation models: monocular depth networks, feed-forward 3D/4D reconstruction models, and vision--language models that predict geometry. However, their progress cannot be measured reliably. Published numbers are not comparable, because every paper samples frames, sets resolutions, and selects test splits differently. They are not robust because the alignment required for every up-to-scale prediction can outweigh the gap between...
  </details>

- **2026-11-24** — Yun Chen, Jeonghyeok Do, Munchurl Kim — [Back to Raw Motion: Latent-Free Diffusion Transformers for Text-to-Motion and Exact Conditional Generation](http://arxiv.org/abs/2611.32793v1)
  <details><summary>📄 Abstract</summary>
  As generative models tackle larger and more complex datasets, learned codecs enable efficient generation through compact latent representations, but may lose details and cannot guarantee exact preservation of given conditions. Generating directly in the original data space avoids errors introduced by the codec. Recent advances in image generation demonstrate that pixel diffusion can produce high-quality samples at practical computational costs. Inspired by these advances, we conduct a preliminar...
  </details>

- **2026-11-24** — Yunong Liu, Danna Xue, Javier Vazquez-Corral — [HazeFlux: Few-Step Generative Priors for Real-World Image Dehazing](http://arxiv.org/abs/2611.32632v1)
  <details><summary>📄 Abstract</summary>
  Real-world single-image dehazing suffers from severe domain shifts, as paired real data is scarce and models trained on synthetic haze generalize poorly to real-world haze. While pre-trained generative editing models offer powerful image priors to bridge this generalization gap, applying them to image dehazing poses two major challenges: standard generative models prioritize distribution alignment over strict pixel-level fidelity, and operating in compressed latent spaces inherently discards fin...
  </details>

- **2026-11-24** — Linjing You, Zeming Yang, Zhenhao Shen et al. — [ViTacLab: Physically Consistent Visuo-Tactile Simulation, Benchmarking, and Representation Learning for Robotic Manipulation](http://arxiv.org/abs/2611.32476v1)
  <details><summary>📄 Abstract</summary>
  Tactile sensing is essential for contact-rich robotic manipulation, but existing visuo-tactile simulators trade physical fidelity for scalability, and benchmarks largely focus on two-finger grippers. We present ViTacLab, a framework comprising ViTacSim, ViTacBench, and ViTacPolicy. ViTacSim uses a tri-modal tactile primitive: a global sparse contact-force lattice, a local dense force array, and tactile images. Anchored to PhysX contact-solver outputs, it corrects normal inconsistency through loc...
  </details>

- **2026-11-24** — Yoonki Cho, Youngju Na, Taegeun Yang et al. — [See the Answer, Learn to Embed: Learning Universal Multimodal Embeddings from Hindsight](http://arxiv.org/abs/2611.32439v1)
  <details><summary>📄 Abstract</summary>
  Universal Multimodal Embedding (UME) models map heterogeneous multimodal inputs into a shared embedding space, where pairwise similarity supports diverse downstream tasks. Recent reasoning-driven UME approaches use intermediate reasoning to generate additional context for embedding, but often incur extra computation at inference. In this paper, we explore the matched candidate (i.e., the paired target) as an alternative source of context, asking whether a model can "see the answer" during traini...
  </details>

- **2026-11-24** — Kian Izadpanah, Ali Mahdavi Amiri, Daniel Cohen-Or et al. — [Video Models are Excellent Motion Models](http://arxiv.org/abs/2611.32432v1)
  <details><summary>📄 Abstract</summary>
  Video foundation models have emerged as powerful generators of dynamic visual content, exhibiting remarkable capabilities in synthesizing complex actions and interactions. We argue that these models have also become excellent motion generators, with motion priors that are richer and more general than those learned by dedicated motion models. Their advantage extends beyond visual realism and is manifested in two important aspects: motion naturalness, including coherent body coordination, physical...
  </details>

- **2026-11-24** — Linhao Zhong, Bozhen Fang, Xuehao Wang et al. — [On the Importance of Hidden-State Refinement in Masked Diffusion Language Models](http://arxiv.org/abs/2611.32416v1)
  <details><summary>📄 Abstract</summary>
  Masked diffusion language models (MDLMs) generate text by iteratively denoising masked or corrupted token sequences, allowing token predictions to condition on bidirectional context and update multiple positions in parallel. While each denoising step produces a rich layer-wise hidden-state trajectory, prior work typically focuses only on token-level information and discards these continuous hidden states, leaving their refinement dynamics underexplored. In this work, we analyze hidden-state dyna...
  </details>

- **2026-11-24** — Maria-Emilia Grigore, Stelian Spînu — [Improving Character Identity Consistency in Diffusion-Based Visual Story Generation through Identity Memory and Automatic Reranking](http://arxiv.org/abs/2611.32383v1)
  <details><summary>📄 Abstract</summary>
  Automatic visual story generation using diffusion-based models has become an increasingly important research direction in generative artificial intelligence. However, maintaining character identity consistency across consecutive frames remains an open challenge, as existing models often produce significant variations in facial traits, clothing, visual style, or anatomical proportions. This paper proposes a modular pipeline to improve character identity consistency in multi-frame visual story gen...
  </details>

- **2026-11-24** — Simin Fan, Martin Jaggi — [DAiSy: Online Data Selection by Adaptive Utility Estimation for LLM Pretraining](http://arxiv.org/abs/2611.32294v1)
  <details><summary>📄 Abstract</summary>
  Model-aware online data selection prioritizes the training documents that contribute the most given the model's current state. Existing online selectors rank candidates upon gradient-based data utility scores, which requires the full forward-backward pass of the main model on every candidate document. Scoring each document therefore pays as much as training on it, yet only a small fraction is used for the real model update. We introduce DAiSy, a lightweight linear auxiliary model that learns to ...
  </details>

- **2026-11-24** — Xiaoye Liang, Yiming Huang, Jialu Wu et al. — [StreamCoach: Proactive Sports Coaching via Continuous Visual Reasoning](http://arxiv.org/abs/2611.32281v1)
  <details><summary>📄 Abstract</summary>
  In fitness and sports training, timely action quality assessment (AQA) is essential for learners to identify and correct technical errors during movement execution. However, most AQA methods assess completed performances, limiting their ability to provide timely feedback. Streaming methods alleviate this latency, but limited reasoning hinders their use of subtle movement cues and sport-specific knowledge. Moreover, their fragmented feedback focuses on one body part at a time, overlooking movemen...
  </details>

- **2026-11-24** — Zihan Jia, Zhilin Dai, Zhengming Zhang et al. — [SoccerNarrate: Event-Grounded Streaming Soccer Commentary with Macro-Window Preference Alignment](http://arxiv.org/abs/2611.32153v1)
  <details><summary>📄 Abstract</summary>
  Existing clip-based soccer commentary models often produce delayed, repeated, or poorly synchronized narration on untrimmed full-match videos. Recent streaming video-language models make low-latency full-match narration feasible, but they often favor general descriptions rather than professional, event-grounded soccer commentary. They may describe nearby actions while failing to mention key events such as goals, cards, substitutions, and offsides correctly and on time. In this paper, we present ...
  </details>

- **2026-11-24** — Enqi Liu, Zhi Gao, Liu Liu et al. — [RISE: Reasoning with Implicit State Embeddings for GUI Agents](http://arxiv.org/abs/2611.32102v1)
  <details><summary>📄 Abstract</summary>
  Graphical user interface (GUI) agents translate user instructions and screenshots into executable actions. To learn executable actions, existing approaches often rely on explicit reasoning during training, which encourage over-reliance on specific reasoning patterns rather than generalizable action-relevant information. In this paper, we propose an implicit framework, RISE, which integrates action-relevant reasoning into implicit state representations to guide GUI action prediction. To this end,...
  </details>

- **2026-11-24** — Luoyuan Zhang, Xuanyu Zheng, Yancheng Long et al. — [Rethinking Video Agents: When and Why Video Harnesses Work](http://arxiv.org/abs/2611.31883v1)
  <details><summary>📄 Abstract</summary>
  Video understanding depends not only on how models reason about visual evidence, but also on which evidence they observe. Fixed observation policies determine this evidence in advance; agentic harnesses allow models to seek further observations as their understanding develops. This shift creates an opportunity to realize capabilities that fixed inputs leave untapped, yet the ability to request observations does not ensure their effective use. We investigate when and why video harnesses improve u...
  </details>

- **2026-11-24** — Kaushal Mhapsekar, Darsh Asher, Bita Aslrousta et al. — [DELTA: Diagnosing Exploration Lineages via Twin-path Alignment - What Can Contrasting Design Paths Reveal About Microarchitectural Behavior?](http://arxiv.org/abs/2611.31767v1)
  <details><summary>📄 Abstract</summary>
  Architects have two mature instruments for performance work. Top-Down analysis tells them where a design loses its pipeline slots, and design-space exploration (DSE) tells them which configuration scores best. Neither explains why a search stops improving: why a backend-bound design rejects a prefetcher that the bottleneck label recommends, or why a capacity increase that helped in one configuration hurts in the next. This paper argues that the evidence needed to answer such questions is already...
  </details>

- **2026-11-24** — Ernesto Lozano, Alberto Jaenal, Javier Civera — [Xtream: An Explicit Metric State for Large-Scale Streaming Reconstruction](http://arxiv.org/abs/2611.31757v1)
  <details><summary>📄 Abstract</summary>
  3D foundation models (3DFMs) enable dense reconstruction in a feed-forward pass, yet their effective span is limited by cross-view attention. Local consistency has been expanded through geometric alignment of video chunks and recursive updates of an implicit memory, and large-scale scenes with pose graphs. However, both strategies are prone to drift, largely due to the lack of metric-scale observability from monocular geometry. We present Xtream,a hybrid streaming pipeline that maintains an expl...
  </details>

- **2026-11-24** — Reda Bensaid, Ismail Ben Ayed, François Leduc-Primeau et al. — [Text Is Just Another Shot in Vision-Language Models: Simple Probes on Frozen Encoders Do It](http://arxiv.org/abs/2611.32672v1)
  <details><summary>📄 Abstract</summary>
  Few-shot adaptation of vision-language models has produced increasingly elaborate methods built on CLIP and on one shared principle: the zero-shot text classifier is the anchor, and labeled images only correct it. We argue that this principle reflects CLIP's visual features rather than a property of the task. We provide a simple Bayesian interpretation, in which a class name is worth exactly kappa = sigma^2 / tau^2 labeled images, the ratio between the visual spread of a class and the misalignme...
  </details>

- **2026-11-23** — Merel Kuijs, Till Richter, Rushin H. Gindra et al. — [Learning Multimodal Representations from Partially Paired, Small-Scale Data](http://arxiv.org/abs/2611.30601v2)
  <details><summary>📄 Abstract</summary>
  Modeling multimodal data from partially paired samples is critical for advancing domains like biomedicine, where vast unimodal datasets and foundation models exist but paired data remains scarce. Existing fusion methods rely on large-scale paired datasets, limiting their use in scenarios with incomplete pairing. We introduce CAMEO, an adversarial learning-based modality fusion framework that integrates modalities from small, partially paired datasets. Combining any pre-trained unimodal encoder w...
  </details>

- **2026-11-23** — Qiaoqiao Jia, Guile Wu, Dongfeng Bai — [GeoMVGen: Joint Appearance-Geometry Modeling for Multi-View Video Generation in Robotic Manipulation](http://arxiv.org/abs/2611.31689v1)
  <details><summary>📄 Abstract</summary>
  Robotic manipulation requires predicting how robot-object interactions evolve over time, encompassing both visual appearance and scene geometry. In multi-camera settings, such predictions need to capture the evolving 3D scene consistently across viewpoints, while supporting controllable generation under different robot actions and camera configurations. Existing video generation models provide strong priors for visual appearance and motion but typically lack explicit geometric modeling. Meanwhil...
  </details>

- **2026-11-23** — Tom Alisch, Sonia Murthy, Robert Hawkins et al. — [Reproducible Social Structure Emerges From Free-Form Interaction Among LLM Agents](http://arxiv.org/abs/2611.31543v1)
  <details><summary>📄 Abstract</summary>
  Multi-agent LLM simulations are increasingly used as models of social systems, but most published findings are anecdotal, i.e., drawn from a single run. It is therefore unclear which observed phenomena are robust findings of the simulated system itself, and which were random events in one particular run. Here, we introduce a repeatable, goal-free, proactive multi-agent framework in which fifty persona-conditioned agents with persistent memory choose whether, with whom, and how to communicate acr...
  </details>

- **2026-11-23** — Tonmoy Hossain, Alexandra G. Roberts, Mark Olchanyi et al. — [Fast Anatomy-Aware Diffeomorphic Augmentation for Brain MRI](http://arxiv.org/abs/2611.31524v1)
  <details><summary>📄 Abstract</summary>
  Data augmentation is essential for training deep learning models that are generalizable, particularly when training data are limited. In brain MRI, augmentation methods that synthesize anatomically diverse images without relying on large cohorts are particularly attractive, especially when training supervised models for scans with a specific resolution or MRI contrast. While conventional random nonlinear fields offer a simple means of achieving such diversity, they fail to capture the underlying...
  </details>

- **2026-11-23** — Wenyi Lian, Zheng Zhao, Thomas B. Schön — [PromptSMC: Enabling Particle Exploration in Flow Matching via LLM-Based Prompt Rejuvenation](http://arxiv.org/abs/2611.31471v1)
  <details><summary>📄 Abstract</summary>
  This paper is concerned with prompt-image alignment at inference time through exploration of generative trajectories and dynamical prompt rejuvenation. We leverage sequential Monte Carlo (SMC), to offer a gradient-free and principled framework for this purpose through reward-guided trajectory selection. More specifically, we introduce LLM-based prompt rejuvenation, allowing for efficient particle exploration in SMC samplers along the diffusion time in flow matching models. The proposed method, P...
  </details>

- **2026-11-23** — Yiming Liu, Jianwei Ma, Zhongwei Xing et al. — [Sparse Hodge Preference Optimization: Fine-Tuning Language Models toward Alignment beyond Transitive Preferences](http://arxiv.org/abs/2611.30135v2)
  <details><summary>📄 Abstract</summary>
  The growing adoption of Direct Preference Optimization (DPO), which leverages pairwise preference data, reflects its great success in fine-tuning large language models to align with human expectations. It directly optimizes the policy from human preferences without explicit reward modeling or the complexities of reinforcement learning-based approaches. However, the classic DPO relies on the Bradley--Terry sampling model and cannot effectively capture intransitivity or cyclic structures in aggreg...
  </details>


### 📂 robustness
*鲁棒性与可靠性 / Robustness & Reliability* — 53 papers

- **2026-11-25** — Ofer Idan, Dan Badur, Yoli Shavit — [Towards Closing the Performance Gap in Cross-Modal Place Recognition](http://arxiv.org/abs/2611.34877v1)
  <details><summary>📄 Abstract</summary>
  Cross-modal place recognition (CMPR) matches natural language descriptions against databases of geo-tagged reference images, enabling localization without visual queries. Despite its potential for language-guided navigation, existing vision-language models lag far behind visual place recognition (VPR) baselines, even after task adaptation. Unlike general-purpose text-to-image retrieval, place recognition relies on subtle local cues to distinguish visually similar locations. We therefore hypothes...
  </details>

- **2026-11-25** — Yiming Wang, Yenan Wu, Junda Wu et al. — [Reference-Model-Guided Distributed MPC for UAV Swarm Formation Flying Under Switching Directed Graphs](http://arxiv.org/abs/2611.34540v1)
  <details><summary>📄 Abstract</summary>
  Distributed formation control of unmanned aerial vehicle (UAV) swarms in complex environments faces several challenges, including switching inter-agent connectivity, limited communication, external disturbances, and collision avoidance. To address these challenges, we propose a reference-model-guided distributed model predictive control (MPC) framework for UAV swarm formation. Each UAV uses relative-position information from its neighbors as input to a local reference model, whose output serves ...
  </details>

- **2026-11-25** — Hui Shen, Yunta Hsieh, Jianing Ma et al. — [OS-Omni: Benchmarking Generalist Computer-Using Agents on Long-Horizon Workflows Across Platforms](http://arxiv.org/abs/2611.34232v1)
  <details><summary>📄 Abstract</summary>
  Computer-using agents are increasingly expected to complete realistic user goals rather than isolated GUI actions. However, existing benchmarks typically isolate web, mobile, or desktop environments, leaving it unclear whether a single generalist agent can execute long-horizon workflows that span multiple operating systems and persistent application states. We introduce OS-Omni, a live cross-platform benchmark and execution environment for evaluating computer-using agents across Windows, Ubuntu,...
  </details>

- **2026-11-25** — Jonas Peché, Dmitry Matveev, Vladimir Ciric et al. — [Strategic and Robust Task Allocation for Combat Objectives in Adversarial Multi-Agent Environments](http://arxiv.org/abs/2611.34158v1)
  <details><summary>📄 Abstract</summary>
  Task allocation in contested-objective team games requires coordinated decisions under uncertainty, spatial constraints, and changing tactical conditions. In such settings, multiple agents must anticipate both teammate behavior and opponent actions. We study a hybrid predict-then-optimize approach for assigning controllable agents to objectives in real time. A masked multi-head model predicts tactical signals for each agent, including survival chance, local superiority, combat interaction, trave...
  </details>

- **2026-11-25** — Shizhuang Wang, Tianhao Wang, Xingqun Zhan — [CondUQ: Calibrated Conditional Uncertainty Quantification Using Distribution Matching](http://arxiv.org/abs/2611.33939v1)
  <details><summary>📄 Abstract</summary>
  Many applications, especially reliability- and safety-critical ones, require accurate uncertainty quantification for the outputs of model- or learning-based measurement, estimation, and prediction systems. The errors of such systems often vary with factors such as input quality and operating conditions, and thus cannot be accurately described by a single Gaussian model. Although Gaussian mixture models and calibrated quantiles can approximate such error distributions, their unconditional forms d...
  </details>

- **2026-11-25** — Bingyu Li, Wu Du, Zhiyuan Zhao et al. — [Towards 360$^\circ$ Embodied UAV Tracking Without Turning](http://arxiv.org/abs/2611.33934v1)
  <details><summary>📄 Abstract</summary>
  Conventional embodied UAV tracking couples target observability with heading control because targets may leave the field of view of forward-facing cameras. We investigate a complementary paradigm that uses full-spherical perception to follow designated targets without active heading adjustment. To support this setting, we introduce 360UAV-ETrack, a simulation benchmark comprising 2,652 sequences, over 1.73 million synchronized observations, eight tracking tasks, and 150 held-out closed-loop scen...
  </details>

- **2026-11-25** — Yuqi Cheng, Rui Meng, Yijin Li et al. — [Agentic Reinforcement Learning with Immediate and Prospective Credit Assignment for Medical Visual Reasoning](http://arxiv.org/abs/2611.33777v1)
  <details><summary>📄 Abstract</summary>
  Medical visual question answering (VQA) requires acquiring useful evidence and deciding where to look next. Yet final-answer rewards do not reveal which observations support answering or guide subsequent inspection. We introduce MedPACT, an agentic reinforcement learning framework that learns selective observation policies through immediate answer support and prospective guidance. Our content-controlled estimator compares next actions induced by real and matched alternative observations under a ...
  </details>

- **2026-11-25** — Shiyu Zhang, Zengyi Wo, Yuming Liao et al. — [SEAM: A Self-Evolving and Adaptive Probing Framework for Automatic MLLM Hallucination Evaluation](http://arxiv.org/abs/2611.34598v1)
  <details><summary>📄 Abstract</summary>
  The severe susceptibility of multimodal large language models (MLLMs) to hallucinations poses a critical threat to their reliability, making a rigorous evaluation framework indispensable. However, existing evaluation pipelines largely rely on predefined test items, suffering from high construction costs, rapid obsolescence as MLLMs evolve, and ineffectiveness in probing model-specific weaknesses. To address these limitations, we propose SEAM, a self-evolving and adaptive probing framework for au...
  </details>

- **2026-11-25** — Léonard Brice — [The Weak Negotiation Function](http://arxiv.org/abs/2611.34442v1)
  <details><summary>📄 Abstract</summary>
  Subgame-perfect equilibria (SPEs) constitute a refinement of Nash equilibria, where the players are not allowed to resort to non-credible threats to discourage deviations. In graph games equipped with a broad class of objectives, SPEs are captured by a tool called the negotiation function.   After giving a quick overview of what has already been achieved using this tool, we define a variant of it: the weak negotiation function. We show that weak SPEs, a standard relaxation of SPEs, can be captur...
  </details>

- **2026-11-25** — Haoming Gu, Yunpeng Qing, Zhi Hou et al. — [CamAct: Learning Robotic Manipulation from In-the-Wild Videos via Camera Motion](http://arxiv.org/abs/2611.34257v1)
  <details><summary>📄 Abstract</summary>
  Vision-Language-Action (VLA) models benefit from large, diverse datasets for robotic manipulation, yet collecting robot demonstrations remains costly. Recent work has explored egocentric videos as a source of supervision, primarily drawing on demonstrations of human-object interaction. We show that in-the-wild videos can improve robotic manipulation even when they contain no demonstrations of object manipulation. Specifically, camera motion recovered from these videos provides an additional sour...
  </details>

- **2026-11-25** — Yechan Cho, Hyeonsu Lee, Emma Deneuville et al. — [Learning from Natural Images Untangles Number Sense](http://arxiv.org/abs/2611.33615v1)
  <details><summary>📄 Abstract</summary>
  Numerical cognition is a simple yet fundamental ability that remains challenging for modern vision-language models. Meanwhile, number sense is already present in numerically naïve animals, suggesting that it can emerge without explicit numerical learning. Deep neural networks provide a related observation, with numerosity-selective units appearing after training on unrelated natural-image tasks and even before any training. However, these findings leave unresolved whether visual learning contrib...
  </details>

- **2026-11-25** — Boxuan Dong, Yupeng Qian, Ying Wu et al. — [HOG-WAM: Improving Visual Robustness through Future Gradient Prediction](http://arxiv.org/abs/2611.34811v1)
  <details><summary>📄 Abstract</summary>
  World-action models jointly predict future observations and actions, yet visual corruption can disrupt the resulting policies. We introduce HOG-WAM, which adds future Histograms of Oriented Gradients (HOG) as structural supervision derived directly from demonstration images. An auxiliary HOG diffusion transformer (DiT) module reads RGB features through asymmetric attention, allowing its objective to shape the visual representation used for control. The module is used only during training and rem...
  </details>

- **2026-11-25** — Maria Ilektra Plakitsi, Sebastian Feld, Akash Kundu — [LatentRL-QAS: Transfer via Latent Reinforcement Learning for Quantum Architecture Search](http://arxiv.org/abs/2611.34634v1)
  <details><summary>📄 Abstract</summary>
  Reinforcement learning (RL) emerges as a prominent approach to quantum architecture search (QAS), the automated design of quantum circuits. However, transferring what an agent has learned from one number of qubits to another is still weakly explored: the state, the action space and the neural network of a state-of-the-art RL-QAS agent all grow with the number of qubits, which makes transfer learning across qubit counts prohibitive. We make this transfer possible by introducing LatentRL-QAS, a la...
  </details>

- **2026-11-25** — Nirmit Joshi, Nathan Srebro, Eran Malach — [Tune for Retention, Not Just Gain: SFT Forgets Far Less than You Think](http://arxiv.org/abs/2611.34579v1)
  <details><summary>📄 Abstract</summary>
  Catastrophic forgetting, the drastic loss of previously acquired capabilities when learning new ones, is a central challenge in language model fine-tuning. Supervised fine-tuning (SFT) is widely believed to be prone to such forgetting. Recent works have attributed this to the off-policy nature of SFT, arguing that on-policy learning is key to continual learning. In this paper, we challenge this premise. We show that while maximizing new-task performance can induce catastrophic forgetting, altern...
  </details>

- **2026-11-25** — Yan Lin, Zhongliang Guo, Jingyu Sun et al. — [When Skills Fail to Compose: Compatibility and Retention in Language Models](http://arxiv.org/abs/2611.34398v1)
  <details><summary>📄 Abstract</summary>
  Skill acquisition alone does not establish a reusable skill library: task proficiency does not specify a compositional interface. Motivated by agents that acquire and refine skills, we study independently learned soft-prompt skills on frozen language models, with skill identities and execution order supplied. Across four digit-task bases and three record-editing models, mean composition accuracy in one call is at most 7.6%, compared with 88.2% to 100% over two calls that add computation and an e...
  </details>

- **2026-11-25** — Caterina Senette — [Interacting with Alexa: A Longitudinal Case Study of Voice Assistant Use in Down Syndrome](http://arxiv.org/abs/2611.34159v1)
  <details><summary>📄 Abstract</summary>
  As life expectancy for individuals with Down syndrome (DS) continues to increase, supporting cog- nitive engagement, everyday autonomy, and participation throughout adulthood has become an important research priority. Conversational voice assistants have emerged as promising assistive tech- nologies for these purposes, yet evidence regarding their long-term use in naturalistic settings remains limited. This paper presents a longitudinal case study of the everyday use of Amazon Alexa by an adult ...
  </details>

- **2026-11-25** — Shenxing Wei, Jinxi Li, Zihui Zhang et al. — [FoundSurface: Feedforward Ray-Based 3D Scene Surface Reconstruction from Unposed Images](http://arxiv.org/abs/2611.34128v1)
  <details><summary>📄 Abstract</summary>
  Accurate 3D surface reconstruction from unposed images remains a fundamental challenge in computer vision. Recent feed-forward pointmap methods eliminate the need for camera poses but inherently produce discrete, sparse representations. In this paper, we present a generalizable pipeline that directly recovers continuous, high-fidelity 3D surfaces from unposed images by seamlessly integrating pointmap- and ray-based representations. Our approach first extracts explicit geometric priors using a pr...
  </details>

- **2026-11-25** — Heshen Zhan, Youhan Huang, Yunke Peng et al. — [BReD: Block Replay Dithering for Stable Low-Bit EMA Optimizer States](http://arxiv.org/abs/2611.33951v1)
  <details><summary>📄 Abstract</summary>
  Low-bit storage of optimizer states can substantially reduce the memory footprint of large-scale training. In practice, however, these states are not quantized once: at every training step, they are dequantized, updated, requantized, and written back. This iterative quantization pipeline can destabilize training. We identify a failure mode behind this instability: for states updated via exponential moving averages (EMAs), quantization errors are recursively fed into subsequent updates. As a resu...
  </details>

- **2026-11-25** — Bryan Wong, Xun Xu, Jongwoo Kim et al. — [BayesPath: Reliability-Aware Bayesian Reasoning for Whole-Slide Pathology Agents](http://arxiv.org/abs/2611.33935v1)
  <details><summary>📄 Abstract</summary>
  Diagnosing whole-slide images (WSIs) requires hypothesis-driven reasoning: pathologists form a differential diagnosis, seek discriminative evidence, weigh its reliability, and stop once it suffices. However, existing training-free WSI agents lack an explicit framework for such reasoning. They typically use a large language model (LLM) to aggregate the region descriptions of a multimodal LLM (MLLM), without a belief over the candidates or regard for the descriptions' reliability. Consequently, a ...
  </details>

- **2026-11-25** — Yao Lu, Yuhang Zheng, Yaxin Gao et al. — [VTK-Bench: A Diagnostic Benchmark for Distinguishing Language Priors and Text Modal Bias in Visual Language Models](http://arxiv.org/abs/2611.33725v1)
  <details><summary>📄 Abstract</summary>
  Visual language models (VLMs) have demonstrated exceptional capabilities across various multimodal tasks, but they remain susceptible to hallucinations, undermining their reliability. Existing hallucination benchmarks primarily focus on identifying hallucinations and describing their manifestations, often neglecting their underlying causes. Specifically, multimodal hallucinations can stem from two distinct failure modes: text modality bias (TMB), reflecting an over-reliance on misleading text in...
  </details>

- **2026-11-25** — Ming Xue, Shijie Wei, Shulei Zhao et al. — [Deep-learning-enabled rapid spatially multiplexed wavefront sensing with a thin diffuser](http://arxiv.org/abs/2611.33724v1)
  <details><summary>📄 Abstract</summary>
  Conventional wavefront sensing typically measures aberrations along a single guide-star direction, limiting the correction of field-dependent aberrations over a wide field of view. Spatial multiplexing with a thin diffuser enables simultaneous measurements across multiple isoplanatic patches, but the computational cost of reconstruction makes it difficult to track changing aberrations. We propose a deep-learning approach that combines recurrent all-pairs field transforms for displacement estimat...
  </details>

- **2026-11-25** — Aditya Sai Pranith Ayapilla, Yuki Yasuda, Ryo Onishi — [BridgeSRDA: Efficient Probabilistic Super-Resolution Data Assimilation with Forecast-Informed Stochastic Interpolants](http://arxiv.org/abs/2611.33720v1)
  <details><summary>📄 Abstract</summary>
  High-resolution ensemble data assimilation is computationally demanding because it requires repeated forecasts and updates of many flow states. We introduce BridgeSRDA, a probabilistic super-resolution data assimilation framework that combines low-resolution numerical forecasts with sparse, noisy observations to generate high-resolution analysis windows. A neural network learns forecast-informed stochastic transport, which is sampled to produce an ensemble of reconstructions. Each current analys...
  </details>

- **2026-11-25** — Yuchi Pu, Bosong Qi, Pengcheng Shi et al. — [MOVR-SAR: A Multi-resolution SAR Registration Dataset under Orbit-crossing and View-variant Imaging Differences](http://arxiv.org/abs/2611.33673v1)
  <details><summary>📄 Abstract</summary>
  Synthetic aperture radar (SAR) image registration under varying acquisition geometries is challenging because orbit direction, look side, and incidence angle affect backscatter, terrain-induced distortion, and feature visibility. However, large-scale geometry-aware benchmarks remain scarce. This paper presents MOVR-SAR, a multi-resolution dataset of 450,845 registered and quality-screened tile pairs derived from 2774 scene pairs from Capella, Umbra, Sentinel-1, and NISAR. It covers X, C, and L b...
  </details>

- **2026-11-25** — Masahiro Kaneko, Ayana Niwa, Timothy Baldwin — [Sparse-to-Sparse Feature Learning for Cross-Layer Analysis and Steering](http://arxiv.org/abs/2611.33640v1)
  <details><summary>📄 Abstract</summary>
  Understanding how models internally represent information is a central challenge in interpretation and control. Sparse autoencoders (SAEs) decompose dense hidden representations into sparse features, and cross-layer methods capture structure spanning multiple layers. However, existing objectives do not explicitly train the sparse code at one layer to predict the sparse code at the next layer. We propose sparse-to-sparse feature learning (S2S), where sparse features at each intermediate layer are...
  </details>

- **2026-11-24** — Luiz G. A. Alves, Aaron Vermeersch — [Confidence scores for gated automation of large language models](http://arxiv.org/abs/2611.33394v1)
  <details><summary>📄 Abstract</summary>
  AI agents built on large language models (LLMs) demonstrate strong capabilities in automated decision-making. However, LLMs may produce incorrect answers with high confidence, limiting their applicability in decisions that affect individuals and organizations. Reliable confidence scores are necessary to gate such decisions, and existing estimates are frequently unavailable or too coarse to support effective gating. This work uses supervised learning to train models to predict the correctness of ...
  </details>

- **2026-11-24** — Danil Kostromin, Andrey Sakhovskiy, Semen Budennyy — [CypherMAS: Benchmarking Routing Reliability in LLM-Based Multi-Agent Systems](http://arxiv.org/abs/2611.33242v1)
  <details><summary>📄 Abstract</summary>
  Multi-agent systems (MAS) built on large language models (LLMs) distribute reasoning across specialized agents that must exchange messages and invoke tools reliably. Existing evaluations typically couple communication with open domain tasks, making it difficult to determine whether a failure arises from reasoning, malformed tool use, lost messages, or forgotten requests. Prior benchmarks do not isolate communication execution or measure routing redundancy against a known optimal path. We introdu...
  </details>

- **2026-11-24** — Cheng Dai, Renkai Luo, Guanfeng Tang et al. — [OVOK: A Recursive Self-Improving Agentic Framework for Video-Based Articulated Robot State Estimation](http://arxiv.org/abs/2611.32185v2)
  <details><summary>📄 Abstract</summary>
  Recovering articulated robot state from video supports metric spatial sensing for manipulation, scene reconstruction, and action planning. Yet the problem is ill-posed: different intrinsics, camera-to-robot poses, and joint angles can explain similar observations. Prior task-specific regressors typically assume known intrinsics, fit one robot through laborious data collection and robot-specific training, and still transfer poorly across scenes. Foundation models apply to any robot zero-shot, but...
  </details>

- **2026-11-24** — Nathan A. C. Hogg, Matt Hyatt, Neil Klingensmith et al. — [An Adversarial Multi-Agent Pursuit Game for Locomotor Agility Pretraining](http://arxiv.org/abs/2611.33407v1)
  <details><summary>📄 Abstract</summary>
  Agile humanoid locomotion requires controllers that can adapt to rapidly changing motion demands while remaining stable and robust. Recent locomotion controllers are typically designed with either a dense reward that is carefully shaped to encourage steps and penalize falling, or by using a reference tracking reward which teaches the controller to follow predetermined motions. Once a behavior that maximizes the reward is discovered, the controller ceases to learn. While generally stable, referen...
  </details>

- **2026-11-24** — Dreamlee Sharma, Nikita Rawat — [A Quantile-Based Framework for Bimodal Distribution Construction](http://arxiv.org/abs/2611.33329v1)
  <details><summary>📄 Abstract</summary>
  This study suggests a novel quantile-based framework to construct bimodal distribution which does not rely on mixture representations or closed-form probability density functions. This proposed approach induces bimodality by transforming the quantile density through a strictly positive modulation function so that it can preserve the support and tail behavior of a chosen baseline distribution with providing explicit control over modal structure. The method is shown to apply broadly across bounded...
  </details>

- **2026-11-24** — Akshata A Bhat, Daman Deep Singh, Niyati Chhaya — [When Ink Meets Pixel: Intent-Aware OCR with VLMs for Human-Corrected Financial Documents](http://arxiv.org/abs/2611.32446v2)
  <details><summary>📄 Abstract</summary>
  Human annotations on documents (such as arrows, carets, strikethroughs, and insertions) express corrective intent yet existing OCR and document understanding systems treat these marks as visual noise rather than semantic edit operations. We introduce intent-aware OCR, the task of generating corrected transcriptions by jointly reasoning over original document content and visual intent cues (handwritten or digital) that convey edit intent. To support this setting, we present DocIntent, a multimoda...
  </details>

- **2026-11-24** — Hanzhao Xi, Zhonghao Li, Suxuan Liu et al. — [CAPER: PartGround and PlanRefine for Reliable Manual-Guided Robotic Assembly Planning](http://arxiv.org/abs/2611.32986v1)
  <details><summary>📄 Abstract</summary>
  Vision-Language-Models (VLMs) used in robot task planning to derive assembly procedures from existing manuals may correctly interpret individual assembly actions yet confuse exact part identities, predict unsupported Part IDs, or produce inconsistent parts across assembly steps. Thus, we propose CAPER (Capacity-Aware Part-grounding and Evidence Refinement), a manual-guided robotic assembly framework that enables VLMs to generate assembly procedures with two modules--PartGround and PlanRefine. Pa...
  </details>

- **2026-11-24** — Ashkan Ganj, Hang Su, Tian Guo — [FocusAnchor: Zero-Shot Metric Depth by Anchoring a Depth Foundation Prior to Focus Cues](http://arxiv.org/abs/2611.32970v1)
  <details><summary>📄 Abstract</summary>
  Existing depth-from-focus methods can struggle with weak focus cues, new cameras, or fewer focal slices. We present FocusAnchor, a recurrent model that uses focus-volume lookups to refine metric depth and repeatedly aligns a relative depth prior from a frozen foundation model to the current depth estimate. The aligned prior guides subsequent refinement in a feedback loop, carrying metric scale recovered from textured regions into regions where focus cues are weak while preserving scene structure...
  </details>

- **2026-11-24** — Tiago Simão Ferreira, Farzad Fallahi — [From Safety-Driven Redundancy to Value-Driven Architecture: An ODD-Based Rationalization Framework for Level 4 Autonomous Vehicles](http://arxiv.org/abs/2611.32960v1)
  <details><summary>📄 Abstract</summary>
  Level 4 autonomous vehicles require fault-tolerant architectures that preserve critical driving functions under sensing, computing, communication, power, and actuation failures. As these systems progress toward industrial scalability, architectural complexity, validation burden, integration effort, and lifecycle cost become increasingly relevant. This study proposes an Operational Design Domain (ODD)-based, safety-constrained systems-engineering framework for architecture rationalization. ODD-sp...
  </details>

- **2026-11-24** — Yera Choi, Yeong Hwa Kim, Jaedeok Lee et al. — [ASCENT: A Benchmark for Evaluating and Advancing Stepwise Diagnostic Reasoning in Large Language Models on Common Clinical Scenarios](http://arxiv.org/abs/2611.32734v1)
  <details><summary>📄 Abstract</summary>
  Large language models (LLMs) excel at medical question answering yet are rarely evaluated on the stepwise diagnostic reasoning that defines real clinical workflows, where impressions are revised as information accumulates. We build Annotated Stepwise Clinical rEasoning for NaturalisTic Diagnosis (ASCENT), a clinician-annotated benchmark and training resource of 3,078 stepwise problems derived from MedQA-USMLE that decomposes each vignette into EMR-aligned steps (Findings, Impression, supporting ...
  </details>

- **2026-11-24** — Kim N. Nolle, Ivana Dusparic, Rhodri Cusack et al. — [Assessing Robustness to Catastrophic Forgetting in Continual Deep Reinforcement Learning for Cyber-Physical Systems](http://arxiv.org/abs/2611.32496v1)
  <details><summary>📄 Abstract</summary>
  As the use of reinforcement learning (RL) becomes more widespread in cyber-physical systems, it becomes increasingly important to design RL agents that are able to adapt to changes in their environments in order to maintain safety and reliability. This paper addresses the question of whether different classes of RL algorithm are more robust against forgetting previously learned behaviours, a critical issue in continual learning, in non-stationary environments. We evaluate the robustness of repre...
  </details>

- **2026-11-24** — Xudong Tan, Peng Ye, Chenyu Huang et al. — [ViDM: Efficient and Order-Robust Parallel Visual Decision Making](http://arxiv.org/abs/2611.32461v1)
  <details><summary>📄 Abstract</summary>
  Visual decision-making demands accurate judgments and timely responses. Yet for multiple questions sharing the same visual input, autoregressive multimodal large language models generate answers token by token, accumulating sequential decoding costs as question count grows and delaying completion of the decision set. Their predictions can also vary with question order. We introduce ViDM, which transforms multi-question visual inference into parallel decisions in a single forward pass, improving ...
  </details>

- **2026-11-24** — Xiangwei Wang, Jianyuan Lin, Peng Wang et al. — [ARS-VLM: Visually Aligned Augmented Random Search for Vision-Language Models](http://arxiv.org/abs/2611.32147v1)
  <details><summary>📄 Abstract</summary>
  First-order reinforcement learning, such as Group Relative Policy Optimization (GRPO), is widely used to post-train Vision-Language Models (VLMs) for multimodal reasoning. However, it incurs heavy memory and system overhead from backpropagation, optimizer states, and a reference model. Forward-only zeroth-order (ZO) methods, such as Evolution Strategies (ES) and its top-k variant Augmented Random Search (ARS), avoid these overheads via reward-guided weight perturbations, yet remain unexplored fo...
  </details>

- **2026-11-24** — Jongseong Bae, Ha Young Kim — [Do Occupancy World Models Really Follow Actions?](http://arxiv.org/abs/2611.32029v1)
  <details><summary>📄 Abstract</summary>
  Occupancy world models predict future 3D scenes conditioned on ego actions, yet their predictions may not faithfully follow the specified trajectory under counterfactual actions. Because driving datasets provide sparse coverage of alternative trajectories for each scene, existing models learn the spatial effect of ego motion implicitly from observed scene--trajectory combinations, which may entangle action effects with scene--trajectory correlations. We propose ReCast, an ego-trajectory-guided t...
  </details>

- **2026-11-24** — Nicolas Sanchez, Bin Yu — [Not All Interpretation Methods Are Created Equal: Tiered Evaluation of AI Interpretability](http://arxiv.org/abs/2611.31833v1)
  <details><summary>📄 Abstract</summary>
  As AI transitions to sociotechnical deployments, uninterpretable models pose serious threats to reliability, public trust and contestability. However, not all interpretation methods are created equal: for interpretability to enhance deployment safety and effectiveness, interpretation methods must be evaluated in a tiered system to differentiate evidence levels of trustworthiness, rather than validated through isolated interpretation instances. Our core vision is that elevating the evaluation of ...
  </details>

- **2026-11-24** — Feixiang Ruan, Guodong Lv, Kewei Zhang et al. — [PyRUA-Dex: Learning Programmatic Policies for Dexterous Bimanual Manipulation with Coding Agents](http://arxiv.org/abs/2611.33144v1)
  <details><summary>📄 Abstract</summary>
  Learning for dexterous manipulation is limited by the scarcity of high-quality demonstrations: retargeting from human video is imprecise, teleoperation gives no force feedback to the operator, and exoskeleton-based collection is hard to scale up. We present PyRUA-Dex, a framework that enables coding agents to develop dexterous manipulation through programmatic policy, without the need of demonstrations. The programmatic policy is developed in two stages: during exploration, multiple agents explo...
  </details>

- **2026-11-24** — Cheng Dai, Renkai Luo, Guanfeng Tang et al. — [OVOK: A Recursive Self-Improving Agentic Framework for Video-Based Articulated Robot State Estimation](http://arxiv.org/abs/2611.32185v1)
  <details><summary>📄 Abstract</summary>
  Recovering articulated robot state from video supports metric spatial sensing for manipulation, scene reconstruction, and action planning. Yet the problem is ill-posed: different intrinsics, camera-to-robot poses, and joint angles can explain similar observations. Prior task-specific regressors typically assume known intrinsics, fit one robot through laborious data collection and robot-specific training, and still transfer poorly across scenes. Foundation models apply to any robot zero-shot, but...
  </details>

- **2026-11-24** — Jie He, Meixun Qu, Cheng Hu et al. — [At the Limit: Autonomous Vehicle Drifting under Generative Policies](http://arxiv.org/abs/2611.33040v1)
  <details><summary>📄 Abstract</summary>
  Autonomous drifting requires agile control despite tire-force saturation and highly nonlinear vehicle dynamics. We propose an online reinforcement learning method for flow policies that combines stochastic differential equation (SDE) sampling for exploration with value-based policy optimization. This method supports both training from scratch and fine-tuning a policy pretrained on expert demonstrations. After training, control actions can be generated using either SDEs or ordinary differential e...
  </details>

- **2026-11-24** — Yue Wang — [Breaking the Joint Action Space Dependence in Distributionally Robust Multi-Agent Reinforcement Learning](http://arxiv.org/abs/2611.32812v1)
  <details><summary>📄 Abstract</summary>
  We study the sample complexity of learning robust coarse correlated equilibria (CCE) in finite-horizon, general-sum, distributionally robust Markov games with known rewards and a generative model of the nominal transitions. Each player evaluates a policy by its worst-case return over total-variation (TV) balls centered at the nominal transition distribution of every stage, state, and joint action; this is the standard $(s,a)$-rectangular uncertainty set. Existing generative-model guarantees for ...
  </details>

- **2026-11-24** — Yibo Wang, Changyi Yang, Yuanxin Liu et al. — [EPRO: Robust Policy Optimization Through an Imperfect Execution-Policy Predictor](http://arxiv.org/abs/2611.32810v1)
  <details><summary>📄 Abstract</summary>
  RL for LLMs often separates rollout generation from policy training. Although the two numerical engines share model parameters, they can induce different policies. This creates a challenge beyond correcting a known training-inference mismatch: during learner updates, the execution policy corresponding to the current parameters cannot be directly observed. We view this as optimizing an unobserved execution policy through an imperfect predictor of its evolution. This perspective raises two fundame...
  </details>

- **2026-11-24** — Daehee Kim — [Measuring Layer-wise Intrinsic Dimensionality of FFNs in LLMs via PCA](http://arxiv.org/abs/2611.32782v1)
  <details><summary>📄 Abstract</summary>
  Modern large language models (LLMs) keep the feed-forward network (FFN) intermediate width identical across every layer, a convention inherited from the original Transformer. Yet mechanistic work suggests layers at different depths do qualitatively different work, raising a natural question: are their capacity demands also non-uniform, and if so, can a fixed parameter budget be allocated more wisely than uniformly? To probe this, we apply principal component analysis (PCA) to the input of each F...
  </details>

- **2026-11-24** — P. D. S. de Lima, D. O. Fontinele, R. L. Gomes et al. — [The W Transform: an additional powerful tool for astrophysical time-series analysis](http://arxiv.org/abs/2611.32699v1)
  <details><summary>📄 Abstract</summary>
  This work introduces the W Transform (WT) for astrophysical applications and explores its similarities and differences to the Continuous Wavelet Transform (CWT), in photometric stellar light curves (LCs). We tested both techniques on synthetic data, producing LCs with different noise levels and numbers of gaps, and applied them to LCs from TESS space mission. The analysis focused on six stars: the solar analog TIC 276293046, the ultra-cool dwarf TIC 359892714, the $γ$ Dor pulsator TIC 164173105,...
  </details>

- **2026-11-24** — Yizhuo Ma, Haoran Sun, Shuang Liang et al. — [Accelerating Dynamic Route Re-solving via Robust Solver Evolution in Automatic Heuristic Design](http://arxiv.org/abs/2611.32576v1)
  <details><summary>📄 Abstract</summary>
  Multi-goal route planning uses spatial data on service locations and pairwise travel costs to determine a visiting order that minimizes total travel cost. This task can be formulated as the traveling salesman problem (TSP) and has benefited from large language model-based automatic heuristic design (AHD) for constructing effective solvers. Despite their effectiveness in static settings, existing methods exhibit substantial re-solving inefficiency when location changes, new requests, or request c...
  </details>

- **2026-11-24** — Viktor Larsson, Johannes Schönberger — [Smooth Essential-Manifold Residuals for View-Graph Calibration](http://arxiv.org/abs/2611.32540v1)
  <details><summary>📄 Abstract</summary>
  View-graph calibration jointly estimates camera intrinsics from multiple pairwise fundamental matrices. The correct intrinsics transform each fundamental matrix into an essential matrix, casting the calibration problem as minimizing the distance to the essential manifold. We study how to represent this objective for nonlinear least squares. The conventional singular-value formulation collapses two independent essential-matrix constraints into one scalar residual. Its per-edge Gauss-Newton model ...
  </details>

- **2026-11-24** — Akshata A Bhat, Daman Deep Singh, Niyati Chhaya — [When Ink Meets Pixel: Intent-Aware OCR with VLMs for Human-Corrected Financial Documents When Ink Meets Pixel: Intent-Aware OCR with VLMs for Human-Corrected Financial Documents](http://arxiv.org/abs/2611.32446v1)
  <details><summary>📄 Abstract</summary>
  Human annotations on documents (such as arrows, carets, strikethroughs, and insertions) express corrective intent yet existing OCR and document understanding systems treat these marks as visual noise rather than semantic edit operations. We introduce intent-aware OCR, the task of generating corrected transcriptions by jointly reasoning over original document content and visual intent cues (handwritten or digital) that convey edit intent. To support this setting, we present DocIntent, a multimoda...
  </details>

- **2026-11-24** — Barnabas Juhasz, Rolf Pfister — [Does Research-Paper Context Improve LLM-Generated Quadruped Navigation? An Exploratory Simulation Study](http://arxiv.org/abs/2611.32381v1)
  <details><summary>📄 Abstract</summary>
  Large language models can write competent robot navigation code, but not only does the research on the topic advance, a model may also, due to the volume of findings, fail to recall relevant findings and apply them to the task at hand. In this work, we test whether providing particular research papers as context improves the LLM-written navigation code for the Go2 quadruped, with the LLM (Claude Opus 5) and locomotion policy frozen. Specifically, we compare the navigation controllers the LLM wri...
  </details>

- **2026-11-24** — Kaipeng Fang, Yuhao Wang, Ji Zhang et al. — [Boundary-Aware Policy Learning for Agent-Orchestrated Robot Manipulation](http://arxiv.org/abs/2611.32238v1)
  <details><summary>📄 Abstract</summary>
  Agent-orchestrated robot systems combine the general reasoning capability of multimodal agents with the precise physical control of learned visuomotor policies. Yet such systems often fail at the moment of handoff: a policy is reliable only from a limited set of start states, while the agent may invoke it outside this region. We call this region the policy's handoff boundary. Existing whole-task policies typically have handoff boundaries that are narrow and difficult for an agent to characterize...
  </details>

- **2026-11-24** — Jinyu Cai, Mingyue Zhang, Nianyu Li et al. — [Automated Smoke Testing for Multi-ending Game Quests via Large Language Models](http://arxiv.org/abs/2611.32089v1)
  <details><summary>📄 Abstract</summary>
  Modern game quests are increasingly trending toward high freedom and multiple endings, making their design and testing more complex. Smoke testing in games aims to rapidly validate quest functionality, but existing automated testing approaches face critical limitations when handling quests with branching narratives, and multiple possible endings. These challenges result in insufficient exploration of endings, redundant action sequences, and prohibitively high interaction costs. To address these ...
  </details>

- **2026-11-24** — Shuxin Li, Yingjie Zhou, Le Zhang et al. — [Rethinking Universal Time Series Foundation Models from Unified Representations to Shared Dynamics (UniTFU)](http://arxiv.org/abs/2611.31921v1)
  <details><summary>📄 Abstract</summary>
  Time series foundation models (TSFMs) have attracted increasing attention in cross-domain forecasting. Existing works mainly rely on large-scale pre-training and general modeling paradigms. However, the former heavily relies on the diversity and domain coverage of pre-training data. Meanwhile, the latter learns unified representations across heterogeneous domains without explicitly identifying the temporal regularities shared among them, limiting robust cross-domain generalization. This work exp...
  </details>


### 📂 watermark
*水印与溯源 / Watermarking & Provenance* — 13 papers

- **2026-11-25** — Jon Carmona, Jon Irureta, Jon Imaz et al. — [Know the Design, Pick the Attack: Sentence-Keyed Watermarks for LLMs](http://arxiv.org/abs/2611.34505v1)
  <details><summary>📄 Abstract</summary>
  A watermark lets the provider of a language model recognise the text its model wrote, which matters more as generated text becomes hard to tell from human writing: provenance underpins academic integrity, the fight against misinformation and new regulation. Providers have started to watermark the text of their models, and to explain how their watermarks work. Explaining a watermark, however, also tells an attacker how to break it, and there are two ways to do so: reword the text to erase the mar...
  </details>

- **2026-11-25** — Aakash Goel, Benjamin Steenhoek, Yu Hu — [How Much Do Coding Agents Over-Edit, and Why? An Empirical Study of Unneeded Edits in Repository-Level Agent Patches](http://arxiv.org/abs/2611.34875v1)
  <details><summary>📄 Abstract</summary>
  Agent patches are larger than developers', which is widely read as over-editing. But patch size does not say whether the extra edits are needed, what they are, or where they come from. We introduce Delta Residue Attribution (DRA), which replays agent trajectories, traces every block (unit) of the final patch to the step that wrote it, reverts each unit, and reruns the task tests to decide whether the unit is needed. We apply DRA to 7,660 resolved GitHub Copilot CLI trajectories from 18 frontier ...
  </details>

- **2026-11-25** — Vahid Etemadi, Gregorio Robles — [SmartLens: Turning AI Agent Changes into Learning, Review, and Risk Signals in the IDE](http://arxiv.org/abs/2611.34377v1)
  <details><summary>📄 Abstract</summary>
  Developers increasingly act as managers of AI agents: they hand tasks to AI coding agents and then have to understand, verify, ship, and learn from what the agents produce. IDEs and recent tools can show which committed lines were written by AI, but they do not attribute the pending changes of external agents, and they do not use attribution to help the developer review, learn, or judge risk. We present SmartLens, an IntelliJ IDEA plugin that attributes changes to an AI agent, the developer, or ...
  </details>

- **2026-11-25** — Abhinav Sharma, Li Li, Chien Van Nguyen et al. — [Puzzling-Bench: Evaluating Language Models on 23,777 Human-Written Puzzles with Community-Verified Answers](http://arxiv.org/abs/2611.34331v1)
  <details><summary>📄 Abstract</summary>
  We introduce Puzzling-Bench, a benchmark of 23,777 puzzles with community-verified answers drawn from the Puzzling Stack Exchange archive (2014-2026): riddles, ciphers, logic grids, lateral-thinking problems, wordplay and recreational mathematics, a third of them with images. Every puzzle carries the answer accepted by its author, a short reference answer taken from it (LLM-extracted for the evaluation sets and checked on a 50-puzzle human review), the author's own hints, community tags and a cr...
  </details>

- **2026-11-25** — Zhongliang Guo, Yan Lin, Yifei Qian et al. — [SOLO: Towards Sample-Faithful and Detectable LLM Watermarking under Repeated Sampling via Content-Anchored Single-Owner Contexts](http://arxiv.org/abs/2611.34190v1)
  <details><summary>📄 Abstract</summary>
  Providers watermark the outputs of large language models, while applications sample many responses per prompt for self-consistency, best-of-n selection, and uncertainty estimation. We show that deployed configurations of distortion-free watermarks, which deduplicate keyed contexts only within a response, couple the responses of a request: answer templates make all responses query the watermark with the same context before the answer, so collisions across responses, usually assumed rare, become t...
  </details>

- **2026-11-25** — Matthieu Queloz — [Familiar Words, Unfamiliar Minds: Conventionalization without Calibration in the Vocabulary of Mind](http://arxiv.org/abs/2611.34179v1)
  <details><summary>📄 Abstract</summary>
  Speakers describe new technologies by stretching old words, letting experience of the new referents sort out which inferences carry over. I argue that stretching the vocabulary of mind to language models pulls apart two processes that theories of metaphor and linguistic change tend to conflate: conventionalization, whereby a stretched word ceases to be marked as such, and calibration, whereby the inferences it invites are fitted to what its new referents bear out. As a gene variant can reach fix...
  </details>

- **2026-11-25** — Johannes R. Hübers, Daniel Uedelhoven, Manuela Bergau et al. — [From Data Room to Report: End-to-End AI Support for M&A Legal Due Diligence](http://arxiv.org/abs/2611.34120v1)
  <details><summary>📄 Abstract</summary>
  Legal due diligence in mergers and acquisitions requires lawyers to organize heterogeneous virtual data room documents, extract transaction-relevant information and consolidate reviewed findings into a due diligence report. We present LEXI (Legal Extraction and Intelligence), a work-in-progress system that demonstrates how large language models can support this process from document ingestion to report preparation. LEXI classifies documents under a configurable due diligence taxonomy, assigns re...
  </details>

- **2026-11-25** — Christos Koutras, Yurong Liu, Laura Haas et al. — [Data Agents Need a Map: Evolving, Demand-Driven Knowledge of Large Collections](http://arxiv.org/abs/2611.33763v1)
  <details><summary>📄 Abstract</summary>
  Most data that could power rich analysis sits unintegrated and uncataloged in open data portals, data lakes, and collections of independently published tables. Data agents now answer analytical questions over such collections with a full workflow per question, including dataset retrieval, join discovery and evaluation, and tailored program synthesis, most of which are discarded when a new task arrives. The knowledge these workflows depend on, such as what each column means, which context a datas...
  </details>

- **2026-11-25** — Siyuan Chen, Yuping Gao, Tai Huang et al. — [FIG-MAC: A Fine-grained Inspiration Graph Empowered Multi-Agent Collaboration for Automated Scientific Hypothesis Generation](http://arxiv.org/abs/2611.33563v1)
  <details><summary>📄 Abstract</summary>
  Automated Scientific Hypothesis Generation (ASHG) leveraging large language models (LLMs) aims to harness their strengths in knowledge integration, logical reasoning, and text generation for efficiently producing innovative, verifiable scientific hypotheses. However, existing approaches face three critical limitations: (i) insufficient fine-grained knowledge representation, as unstructured context impairs LLM comprehension and reasoning; (ii) lack of knowledge evolution traceability, constrainin...
  </details>

- **2026-11-24** — Mingxi Yan, Vasudha Varadarajan, Qiaosi Wang et al. — [Who Attributes a Mind to Whom? Mutual Theory of Mind in Simulated User-Assistant Conversation](http://arxiv.org/abs/2611.33327v1)
  <details><summary>📄 Abstract</summary>
  When users assume that an AI chatbot has mental states, they are more likely to develop over-reliance, emotional dependence, and in extreme cases, psychological harm or self-harm. However, how these mind attributions arise in conversations and how human or AI factors influence this is still unknown. We study how users attribute minds using a minimal framework: a simulated user with different characteristics chats with assistants that differ in social style and memory. We also introduce a message...
  </details>

- **2026-11-24** — Xiaodong Luo — [APEX: Agentic Platform for Ensemble eXploration](http://arxiv.org/abs/2611.33450v1)
  <details><summary>📄 Abstract</summary>
  Ensemble-based methods provide a practical framework for history matching, prediction, and optimization of subsurface models. In methodological studies, however, performance is rarely assessed from a single run. Comparisons typically span cases, configurations, and random seeds, while each evaluation may require an expensive external simulator. Keeping such studies computationally bounded, auditable, and reproducible therefore requires more than implementing a numerical method: experiments must ...
  </details>

- **2026-11-24** — Yifan Duan, Lihuan Li, Chao Xue et al. — [RecordRoute: Auditing Agent Failures with Localization-Guided Diagnosis](http://arxiv.org/abs/2611.33022v1)
  <details><summary>📄 Abstract</summary>
  Auditing failed agent executions requires identifying the responsible actor, the earliest decisive step, and the error mode. Representative supervised methods either focus on step localization or predict multiple attribution targets from shared trajectory representations. These methods do not use the localization result to select the text for mode diagnosis. To address this limitation, we propose RecordRoute, which couples comparative localization with local diagnosis. Specifically, it represent...
  </details>

- **2026-11-24** — Shilin Ma, Xingming Shui, Jinglin Chen et al. — [OmniHarness-RSI: Modality-Aware Harness Evolution for Omnimodal Understanding](http://arxiv.org/abs/2611.32951v1)
  <details><summary>📄 Abstract</summary>
  Recent advances in harness-based recursive self-improvement (RSI) have improved video understanding by evolving executable agent workflows without updating foundation model parameters. However, extending this paradigm to omnimodal understanding remains challenging, as the heterogeneous and interdependent nature of multimodal perception and reasoning creates a complex evolution space, making targeted harness optimization difficult. To address these challenges, we propose OmniHarness-RSI, a modali...
  </details>


### 📂 unlearning
*机器遗忘 / Machine Unlearning* — 1 papers

- **2026-11-24** — Mayank Gulati, Gerhard Wunder — [Deletion You Can Check: Auditing LLM Unlearning](http://arxiv.org/abs/2611.33525v1)
  <details><summary>📄 Abstract</summary>
  A common indication that a fine-tuned model has forgotten a deleted record is a membership-inference score near chance (ROC-AUC $\approx 0.5$). This reading is sound only if the comparison population represents how the record should behave after a valid deletion---a counterfactual that is rarely validated. We test this premise in a controlled $2\times2$ study pairing two membership-inference benchmarks, ArxivMIA and BookMIA, with two language models, Llama-3.2-1B and Qwen2.5-1.5B. Exact retraini...
  </details>


### 📂 benchmark
*安全评测与基准 / Safety Benchmarks & Evaluation* — 1 papers

- **2026-11-25** — Su Myat Noe, Hisami Suzuki, Kouta Nakayama et al. — [Multimodal Safety Evaluation of Vision-Language Models in Japanese](http://arxiv.org/abs/2611.33789v1)
  <details><summary>📄 Abstract</summary>
  Vision-Language Models (VLMs) are increasingly deployed in Japanese-language settings, yet multimodal safety evaluation has been largely English-centric. We extend the Multimodal Safety Test Suite (MSTS) of Röttger et al. (2025) to Japanese as the 12th language, contributing 320 machine-translated and post-edited cases with reference answers plus 82 culturally localized Japanese images. We introduce an evaluation framework that (i) extends MSTS's 3-class safety grouping with a 5-point scale that...
  </details>


### 📂 survey
*综述与系统化 / Surveys & Systematization* — 6 papers

- **2026-11-25** — Dat Tat Mai, Hung Tran Quy, Thai Viet Pham et al. — [Not Every Input Needs Everything: Unifying Expert Gating, Model Cascades, and Agent Orchestration](http://arxiv.org/abs/2611.34112v1)
  <details><summary>📄 Abstract</summary>
  Executing monolithic neural weights, frontier foundation models, or entire multi-agent workflows uniformly on every input incurs substantial computational, latency, and monetary overhead. Conditional computation mitigates this cost by deciding dynamically which internal experts, model endpoints, or specialized agents to invoke per request. Yet token-level gating in sparse neural architectures, query-level model cascades, and task-level multi-agent coordination have largely progressed in disconne...
  </details>

- **2026-11-24** — Gratiana Fu, Josh Beitler, Brian Houck — [DevEx is for Humans, AX is for Agents: Measuring Context Health in Agentic Software Work](http://arxiv.org/abs/2611.33480v1)
  <details><summary>📄 Abstract</summary>
  Coding agents succeed or fail in the context humans give them, yet most evaluations measure only output. Drawing on developer experience research, we introduce Agent Experience (AX), an instrument that scores session transcripts on four dimensions of the CAFE(S) framework: Clarity, Actionability, Fidelity, and Efficiency; Security, a gate rather than a friction dimension, is out of scope. A rubric-guided language model rates each dimension from 1 to 5 and explains what the human could have provi...
  </details>

- **2026-11-24** — Marius Momeu, Koushik Sen — [Agentic Discovery of Soundness Bugs in Safe Rust Bindings](http://arxiv.org/abs/2611.31813v1)
  <details><summary>📄 Abstract</summary>
  Rust crates confine unsafe code, such as calls into C or C++ libraries or system calls, behind safe interfaces that must uphold Rust's invariants. If an interface encodes one rule of the code beneath it too weakly, a program written in purely safe Rust can cause undefined behavior. Static analyzers and fuzzers are bound to fixed patterns or to the paths they execute. We propose LLM agents as auditors of these interfaces, and study how well they do it.   We first define a taxonomy of the defects ...
  </details>

- **2026-11-24** — Rosalia Tufano, Nargiz Humbatova, Daniele Bifolco et al. — [AI-Generated Code Issues: A Taxonomy from Repository Histories, AI Conversations, and Developer Interviews](http://arxiv.org/abs/2611.32676v1)
  <details><summary>📄 Abstract</summary>
  Large language models (LLMs) are increasingly used to generate source code, yet the quality issues in such code remain only partially understood. Understanding these issues can help developers adapt quality assurance practices, such as code review and testing, to better detect problems that may be more common in AI-generated than in human-written code. We study how quality issues in AI-generated code manifest in real software development activities through a mixed-method empirical study that dra...
  </details>

- **2026-11-24** — Zhilin Luo — [The Lafforgue Transform](http://arxiv.org/abs/2611.32627v1)
  <details><summary>📄 Abstract</summary>
  In this report, we survey the \emph{Lafforgue transform}, a natural representation-theoretic map from the Kazhdan cocenter to the Bernstein center of a reductive group over a local field. Its motivation comes from our study of the Braverman-Kazhdan proposal, a conjectural framework for establishing the meromorphic continuation and functional equations of general automorphic $L$-functions through harmonic analysis on possibly singular varieties. For $G=\SL_2$ and $\GL_2$, we explain how the stabl...
  </details>

- **2026-11-24** — Maria Eduarda Pinheiro, Vitoria Caroline Blau — [Generating health variables for a synthetic population of Santa Catarina, Brazil, via ensemble learning and a calibrated linear program](http://arxiv.org/abs/2611.31726v1)
  <details><summary>📄 Abstract</summary>
  Agent-based models in epidemiology require synthetic populations with health-related attributes, which in Brazil are available only from sample surveys such as the Pesquisa Nacional de Saúde (PNS). We add health variables, including smoking, alcohol consumption, physical exercise, self-rated health and chronic conditions, to a georeferenced synthetic population of the state of Santa Catarina. Class probabilities are estimated by an ensemble of logistic regression, random forest and support vecto...
  </details>


### 📂 other
*其他安全相关 / Other Security-Related* — 178 papers

- **2026-11-25** — Charlie Griffin, Oliver Makins, Asa Cooper Stickland et al. — [Attack Policy Selection can Mislead Monitor Evaluators](http://arxiv.org/abs/2611.34934v1)
  <details><summary>📄 Abstract</summary>
  AI monitors, classifiers that flag dangerous behaviour by AI agents, are often evaluated against transcripts generated by attack policies acting as proxies for dangerous behaviour in deployment. We evaluate an ex-production OpenAI monitor as a case study and find that measured false negative rate is highly sensitive to both the method used to generate attack policies and the level of optimisation applied within that method. This rate ranged from 0.5\% to 20.8\% across optimisation levels of a si...
  </details>

- **2026-11-25** — Baihan Yang, Xin Lin, Yufan Wei et al. — [High-Fidelity Image Matting with Pixel-Space Diffusion Transformers](http://arxiv.org/abs/2611.34929v1)
  <details><summary>📄 Abstract</summary>
  Diffusion models have shown strong potential for image matting by transferring generative priors learned from large-scale pretraining. However, existing approaches largely rely on latent diffusion models, whose compressed representations and VAE-based reconstruction introduce a mismatch with the high-frequency precision required for matting. We present PixelMatte, a framework that adapts pretrained pixel-space diffusion transformers for high-fidelity image matting. We show that strong image-cond...
  </details>

- **2026-11-25** — Kumar Shubham, Devendra Vyas, Vidushi Agarwal et al. — [Repairing the Trustworthiness of Distilled Language Models](http://arxiv.org/abs/2611.34831v1)
  <details><summary>📄 Abstract</summary>
  Knowledge distillation enables the deployment of large language models through smaller student models, but the compression process can introduce regressions in trustworthiness even when downstream performance is preserved. Repairing such failures is challenging because the original distillation corpus is often unavailable, while direct preference optimization may alter capabilities inherited from the teacher. We propose a targeted repair framework based on the proximal Bregman response function ...
  </details>

- **2026-11-25** — Daiwei Chen, Anda He, Binwei Yao et al. — [One Model, Many Modes: Evolving System Prompt Ensembles for Creative Generation](http://arxiv.org/abs/2611.34760v1)
  <details><summary>📄 Abstract</summary>
  Preference-aligned LLMs can exhibit mode collapse, concentrating their output distributions around a narrow set of high-reward responses. This limits creative generation, which requires quality, novelty, and diversity. Existing test-time methods often emphasize diversity, giving less attention to whether individual responses are both high-quality and novel. This distinction matters in practical use, where users may seek a single compelling, original response. We formalize creative generation as ...
  </details>

- **2026-11-25** — Soumik Bhattacharjee, Musa Tur Farazi, Md Nasir Uddin et al. — [Spec2Weights: Certifying Networks that a Language Model Writes from a Specification](http://arxiv.org/abs/2611.34711v1)
  <details><summary>📄 Abstract</summary>
  A language model can write the weights of a small MLP, CNN, RNN or GNN from a plain-language specification, with no data and no gradient step. We ask when such a network can be proved exact in the float32 arithmetic it actually runs in. A float-safety lemma makes exhaustive float32 enumeration a proof for any summation order, and a layered error bound covers networks whose weights are not short binary fractions. With dynamic programming, template checks, an SMT proof, breadth-first search and in...
  </details>

- **2026-11-25** — Yuxia Zhu, Shiying Zhang, Lingzhuang Sun et al. — [PoVi: Agentic Poetry-to-Video Generation with Knowledge Grounding and Figurative Understanding](http://arxiv.org/abs/2611.34690v1)
  <details><summary>📄 Abstract</summary>
  Poetry-to-video generation requires more than translating text into visual scenes. Poetic language is highly compressed, often depends on historical and cultural knowledge, and frequently conveys meaning through metaphor, imagery, and other non-literal expressions. We introduce PoVi, a benchmark and agentic framework for grounded poetry-to-video generation, evaluating semantic grounding, discourse coherence, and audiovisual realization. PoVi reconstructs poem semantics into an evidence-bounded r...
  </details>

- **2026-11-25** — Ruixiang Wang, Xinyue Yao, Xuanning Zhou et al. — [DemoFoundry: Toward Scalable Photorealistic Robot Data with Coding Agents and Generative Rendering](http://arxiv.org/abs/2611.34671v1)
  <details><summary>📄 Abstract</summary>
  Scaling robot learning requires demonstrations that combine realistic visual observations with reliable action supervision. Simulation-based synthesis faces a substantial visual gap relative to real environments, while video-only generation struggles to maintain physically consistent interactions and provide aligned action labels. We present DemoFoundry, an automated framework that couples coding agents with generative rendering to synthesize photorealistic and physically grounded robot demonstr...
  </details>

- **2026-11-25** — Cui Yakun, Tiantian Geng, Huixiang Kong et al. — [Recalling the Past to Answer the Present: Context-Aware Multi-Evidence Reasoning for Streaming Video Question Answering](http://arxiv.org/abs/2611.34545v1)
  <details><summary>📄 Abstract</summary>
  Vision-language models (VLMs) have achieved remarkable progress in video understanding, yet existing video question answering (VQA) benchmarks mainly evaluate models in offline settings. Real-world streaming scenarios instead require models to answer context-dependent queries by retrieving and reasoning over evidence distributed across the video history. We introduce StreamRecall, a benchmark for context-aware Multi evidence reasoning in streaming video QA. StreamRecall requires models to retrie...
  </details>

- **2026-11-25** — Samah Fodeh, Sreeraj Ramachandran, Ganesh Puthiaraju et al. — [EPPC-CARE: Staged Hierarchical Annotation of Communication Behaviors in Secure Patient-Provider Messages](http://arxiv.org/abs/2611.34539v1)
  <details><summary>📄 Abstract</summary>
  Objectives: Patient portal messages provide invaluable information about communication dynamics between patients and healthcare providers, but extracting it manually is labor-intensive. We developed and evaluated EPPC-CARE, an automated framework for identifying communication behaviors together with the supporting text for each classification. Materials and Methods: From 867 messages, we obtained 5,516 reference standard annotations. Each annotation is a triplet of communication-related text (sp...
  </details>

- **2026-11-25** — Yurun Chen, Biao Yi, Qihang Yu et al. — [EgoUseBench: Benchmarking Computer-Use Agents under Evolving First-Person Contexts](http://arxiv.org/abs/2611.34466v1)
  <details><summary>📄 Abstract</summary>
  AI wearables, such as smart glasses, extend the context available to agents beyond digital environments to users' physical surroundings. With these devices, computer tasks can originate from users' ongoing activities rather than solely from explicit instructions. Through first-person observations, agents can identify objects and activities relevant to user requests and ground digital tasks in the surrounding context. We call this interaction paradigm Ego Use. However, first-person observations a...
  </details>

- **2026-11-25** — Zhongpai Gao, Anwesa Choudhuri, Meng Zheng et al. — [Evidence-Aligned Benchmarking and Learning for Medical Video Language Models](http://arxiv.org/abs/2611.34465v1)
  <details><summary>📄 Abstract</summary>
  A medical video language model should answer from the visual evidence its question asks about. We find three places where this breaks down and address each with an approach we call MedEvidU. First, benchmarks reward answers that ignore the video: on one dataset, the position of a clip within its recording predicts the surgical step in 37% of questions, and a constant answer beats every trained model on a standard safety-assessment metric. We build MedVidBench-v2, 34 tasks from 18 surgical and cl...
  </details>

- **2026-11-25** — Abdullah Hashmat, Danish Javed, Usman Naseem et al. — [IRTIQA: Evolving in English, Evaluated in Urdu -- Does Agent Self-Evolution Transfer from English to Urdu and Code-Switched Input?](http://arxiv.org/abs/2611.34303v1)
  <details><summary>📄 Abstract</summary>
  As LLM agents increasingly learn from their own experience, the tasks they learn from and are evaluated on are almost always in English. We ask whether self-evolution transfers from English to Urdu, and release IRTIQA, a benchmark of aligned English, Urdu-translated, and Urdu code-switched variants of DROP, SNIPS, AppWorld, and SkillsBench, built with a matrix-language code-switching pipeline and human verification. Using IRTIQA, we evaluate three self-evolving frameworks, Tool-R0 (self-play RL)...
  </details>

- **2026-11-25** — Milad Panahi, Annalisa Bracco — [LatENSO v1.0: a learned latent state of the tropical Pacific for seasonal ENSO operators and forecasting](http://arxiv.org/abs/2611.34296v1)
  <details><summary>📄 Abstract</summary>
  Here we present LatENSO v1.0, a machine-learning forecast system for the El Niño-Southern Oscillation (ENSO) built around a learned, 32-dimensional state of the tropical Pacific. A Swin-transformer autoencoder compresses thirteen monthly-averaged ocean and atmosphere fields into 32 numbers, trained to reconstruct the fields, with no forecast target. The 32 numbers rebuild the fields as well as O(100) empirical orthogonal functions. Two seasonal operators use this state. The first is the extended...
  </details>

- **2026-11-25** — Jing Liu, Fangfei Li, Xin Jin et al. — [Energy-Aware Distributed Task Allocation via Local Submodular Maximization](http://arxiv.org/abs/2611.34293v1)
  <details><summary>📄 Abstract</summary>
  This paper studies distributed task allocation under time-varying agent sets, task sets, and communication graphs. At each decision epoch, the stage allocation problem is formulated as monotone submodular maximization over a time-varying, energy-filtered admissible ground set subject to a partition-matroid constraint. We develop a Distributed Adaptive Greedy Bidding Algorithm (DAGBA) that combines local admissible-set construction, conditional marginal bidding, and neighbor-based conflict resolu...
  </details>

- **2026-11-25** — Modi Jin, Xuying Zhang, Yijing Guo et al. — [StateWeaver: Multi-Agent Coordination of Story-State Transitions for Long-Horizon Video Generation](http://arxiv.org/abs/2611.34290v1)
  <details><summary>📄 Abstract</summary>
  Modern video foundation models generate high-quality short clips, but preserving long-video consistency and correctly depicting event-driven state changes remain challenging. Existing agentic workflows face these challenges because continual planning and repair accumulate context, while reference updates remain limited. We introduce StateWeaver, which combines Active States and Hierarchical Collaboration to connect review-driven visual reference updates with cross-shot state inheritance. Active ...
  </details>

- **2026-11-25** — Guangyu Liu, Hanzhang Wang, Huijia Zhang et al. — [Rehearse in 3D, Render in 2D: Physically Consistent and Editable Robot World Models](http://arxiv.org/abs/2611.34288v1)
  <details><summary>📄 Abstract</summary>
  Embodied world models aim to predict future interactions that are both visually realistic and physically consistent. Yet explicit 3D motion prediction alone does not guarantee that object structure and contact relationships are preserved. Beyond motion prediction, 3D representations provide an explicit state space for imposing structural and physical constraints. Building on this insight, we introduce RehearsalWorld, an editable robot world model driven by 3D Interaction Rehearsal (3DIR). Given ...
  </details>

- **2026-11-25** — Yujia Chen, Rui Sun, Huayu Mai et al. — [Beyond Logits: Coherent Hallucination Mitigation via Attention Contrastive Decoding](http://arxiv.org/abs/2611.34207v1)
  <details><summary>📄 Abstract</summary>
  Large Vision-Language Models (LVLMs) demonstrate impressive multimodal capabilities, yet suffer from hallucination - generating factually inaccurate content. Contrastive Decoding (CD) mitigates this by contrasting amateur and expert branches at the logit level. However, our investigation reveals that such logit-level interventions fundamentally compromise generation coherence, necessitating restrictive penalty constraints unrelated to hallucination suppression.   We introduce Attention Contrasti...
  </details>

- **2026-11-25** — Ziyu Shan, Xiao Ma, Kangrui Yu et al. — [WAtcher: Watching Ahead for Safe Robotic Manipulation with Efficient World-Action Models](http://arxiv.org/abs/2611.34124v1)
  <details><summary>📄 Abstract</summary>
  World-action models (WAMs) couple future imagination with action generation, but they execute every action chunk while ignoring the potential risk. To fill this gap, we present WAtcher, a safety-aware world-action framework in which the policy imagines the outcome of the candidate chunk before execution. For fast future preview, WAtcher builds on a compact WAM whose video expert imagines the visual outcome in only two denoising steps. In addition, we propose Safe-Guard, a lightweight module kept...
  </details>

- **2026-11-25** — Yaniv Galron, Rabeeh Karimi Mahabadi, Maor Ashkenazi et al. — [Improving Tail-Augmented Speculative Drafting with Hidden State Mixing and Gradient Detach](http://arxiv.org/abs/2611.34092v1)
  <details><summary>📄 Abstract</summary>
  Multi-token prediction (MTP) modules and EAGLE-style drafters support efficient speculative decoding by reusing target-model hidden states. Their autoregressive use, however, introduces a training-inference mismatch: training supplies sequences of hidden states from the backbone or a single MTP step, whereas inference attends to a target-model prefix followed by a growing tail of recurrently generated MTP states. EAGLE-3's training-time test (TTT) explicitly simulates this behavior during traini...
  </details>

- **2026-11-25** — Yamato Takahagi, Yoshinari Motokawa, Toshiharu Sugawara — [Post-Training Policy Replication for Strategy-Following Multi-Agent Deep Reinforcement Learning across Team Sizes](http://arxiv.org/abs/2611.34035v1)
  <details><summary>📄 Abstract</summary>
  Although multi-agent deep reinforcement learning enables coordinated behavior, aligning it with managerial intent remains difficult due to complex agent interactions. Although the strategy-following distributed attentional actor architecture (sfDA7-X) improves controllability via regional instructions, instruction combinations scale exponentially with team and instruction sizes, leading to prohibitive training costs and poor transferability. To reduce this computational cost, we introduce a team...
  </details>

- **2026-11-25** — El Houcine El Moussaoui, Chouaib El Hachimi, Saïd Khabba et al. — [Assessing the Physical Interpretability of AlphaEarth Foundation Embeddings Through Multi-Sensor Satellite Time-Series Benchmarking for Agricultural Mapping](http://arxiv.org/abs/2611.34019v1)
  <details><summary>📄 Abstract</summary>
  Accurate and dynamic maps of agricultural LULC are important for agricultural water resource management, particularly in areas where water scarcity is prevalent, such as Morocco. Here, we evaluate the utility of AlphaEarth Foundation Model (AEF) embeddings for agricultural LULC and irrigation-type mapping in Morocco. AEF embeddings were compared to single-date and time-series remote-sensing features using three machine-learning classifiers: XGBoost, CatBoost, and TabPFN. We also evaluated whethe...
  </details>

- **2026-11-25** — Yuze Zhu, Jacky Li, Yusen Luo et al. — [Targeted Adaptation of World-Action Models via Interaction and Motion Heads](http://arxiv.org/abs/2611.33963v1)
  <details><summary>📄 Abstract</summary>
  World-Action Models (WAMs) are a promising new paradigm of robot manipulation policies that jointly generate future video and actions. Successful manipulation requires both identifying where to interact and modeling how the robot and objects move. Yet standard adaptation methods, such as full fine-tuning and LoRA, do not explicitly select parameters aligned with these manipulation-specific capabilities. Motivated by this challenge, we discover two functionally specialized families of attention h...
  </details>

- **2026-11-25** — Shayan Baghayi-Nejad, Jeongsol Kim, Jong Chul Ye — [TWIST: Teacher-Weighted Initial-Noise Spherical Transform for Quality-Preserving Diversity in Distilled Diffusion Models](http://arxiv.org/abs/2611.33895v1)
  <details><summary>📄 Abstract</summary>
  Timestep-distilled diffusion models generate high-quality images in one or a few steps, but often suffer from reduced mode coverage and limited diversity. Recent methods improve diversity by optimizing the initial noise at inference time, requiring costly backpropagation through the denoiser. Moreover, their diversity objectives typically repel generated samples without accounting for how the corresponding teacher model distributes its outputs. We introduce Teacher-Weighted Initial-noise Spheric...
  </details>

- **2026-11-25** — Amirhossein Alimohammadi, Kian Izadpanah, Bardiya Kariminia et al. — [SIA: Selective Image Analogy](http://arxiv.org/abs/2611.33894v1)
  <details><summary>📄 Abstract</summary>
  Image analogy transfers a demonstrated transformation from a before/after pair (A, A') to a new query image B. Existing methods assume all changes in (A, A') should be fully transferred, limiting flexibility when users want only a subset of the demonstrated edits. We introduce Selective Image Analogy (SIA), a new setting where a single demonstration pair encodes multiple edits, and the user selects at inference time which edits to apply to B. To support this, we curate a multi-edit analogy datas...
  </details>

- **2026-11-25** — Rikuto Hidaka, Tsung-Yuan Chen, Kento Kawaharazuka — [Learning a Whole-Body Pivot-Walking Gait for Heavy-Box Transport with a Humanoid](http://arxiv.org/abs/2611.33828v1)
  <details><summary>📄 Abstract</summary>
  Through pivot walking, humans can transport objects that are too heavy to lift. Previous humanoid studies have relied on planned sequences in which object manipulation and stepping are executed separately and the object is brought to rest between successive rotations. However, few studies have developed a single learned controller for humanoid pivot walking. In this paper, we propose a single reinforcement-learning policy that jointly coordinates stepping, balance control, and object manipulatio...
  </details>

- **2026-11-25** — Yixiong Chen — [QPAT: A Universal Quantum Machine Learning Framework for Quantum-Assisted Training and Classical Inference](http://arxiv.org/abs/2611.33806v1)
  <details><summary>📄 Abstract</summary>
  Deep learning models often struggle with sharp local optima and overfitting in limited-data regimes, and exhibit limited capacity for capturing high-order, complex probability distributions. Quantum Machine Learning (QML) models, by operating in exponentially large Hilbert spaces, can efficiently represent such distributions and provide favorable inductive biases for learning, offering a promising pathway to overcome these limitations. However, their practical deployment in the Noisy Intermediat...
  </details>

- **2026-11-25** — Zixuan Li, Kangyao Huang, Meng Xu et al. — [DuoWM:Integrating Dual 6-DoF Visual Flows into Action-Conditioned Drone World Model](http://arxiv.org/abs/2611.33779v1)
  <details><summary>📄 Abstract</summary>
  Action-conditioned video world models generate future observations from an initial frame and a camera trajectory, but often fail to align camera commands with visual dynamics or represent full 6-DoF scene transformations. We present DuoWM, a first-person drone video world model with two complementary visual conditions. Action flow projects future camera positions and orientations into each target frame, while Object flow forward-warps the initial observation and overlays local 6-DoF transformati...
  </details>

- **2026-11-25** — Junsu Kim, Seungryul Baek — [Teaching Students to Stand on Their Own: Distilling Vision Foundation Models for Fine-Grained Few-Shot Class-Incremental Learning](http://arxiv.org/abs/2611.33749v1)
  <details><summary>📄 Abstract</summary>
  Fine-grained few-shot class-incremental learning (FG-FSCIL) aims to incrementally learn visually similar new classes from limited images without catastrophic forgetting. Prior work typically learns strong representations on base classes or leverages vision foundation models (VFMs) directly as backbones or via knowledge distillation. However, VFM backbones incur high computational costs and do not guarantee fine-grained recognition. Although knowledge distillation reduces inference cost, our prel...
  </details>

- **2026-11-25** — Tanvir Hossain, Sudipta Paria, Aidan Gleason Myers et al. — [REFORGE: LLM-Assisted RTL Bug Repair with Structured Context and Verification Feedback](http://arxiv.org/abs/2611.33748v1)
  <details><summary>📄 Abstract</summary>
  Large language models (LLMs) can write and repair RTL, but successful compilation or testbench execution does not establish defect removal, behavioral preservation, security, or implementation feasibility. Existing LLM-based RTL repair methods often report a single repair rate without retaining separate evidence for these properties, limiting reproducible comparison and integration into hardware design flows. We present REFORGE, which, to our knowledge, is the first LLM-assisted RTL repair frame...
  </details>

- **2026-11-25** — Can Wang, Shi Qiu, Fanfan Lin — [PowerFix: Physics-Guided Iterative Repair for LLM-Assisted Power Converter Design](http://arxiv.org/abs/2611.33712v1)
  <details><summary>📄 Abstract</summary>
  Large language model (LLM) agents are increasingly being explored for automated engineering design. However, repairing power-converter designs that fail engineering validation remains challenging: the system must identify physical causes, locate responsible design variables, and resolve violations without compromising other constraints. We introduce PowerFix, a physics-guided iterative repair framework that converts validation failures into structured diagnoses and executable patches while prese...
  </details>

- **2026-11-25** — Lebin Zhou, Zhenghao Chen, Nam Ling et al. — [LLMVC: Large Language Model-Guided Generative Video Compression](http://arxiv.org/abs/2611.33580v1)
  <details><summary>📄 Abstract</summary>
  Recent generative video methods achieve strong perceptual compression by encoding videos into compact latent representations and reconstructing them with powerful generative decoders. However, visual encoders must compress both high-level semantics and dense visual details into a unified latent space, which complicates entropy coding and decoding and may cause semantic drift under aggressive compression. In this work, we propose Large Language Model-Guided Video Compression (LLMVC), which levera...
  </details>

- **2026-11-25** — Yujia Zeng, Yuxin Chen, Yuzhen Song et al. — [FineDex: Bridging Fine-Grained Human-Object Interaction Generation to Dexterous Humanoid Manipulation](http://arxiv.org/abs/2611.34884v1)
  <details><summary>📄 Abstract</summary>
  Dexterity is, at its core, finger-level control, yet existing dexterous manipulation and human-object interaction (HOI) generation methods rarely let one specify how an interaction is performed: five-fingered hands are often reduced to grippers, or finger usage is copied from individual human demonstrations. We present FineDex, a framework that makes finger-level intent both expressible and executable. FineDex learns coordinated human body, hand, and object motions that follow fine-grained instr...
  </details>

- **2026-11-25** — Jose Alfredo de Leon — [State convertibility in quantum-state texture from a general form of free operations](http://arxiv.org/abs/2611.34865v1)
  <details><summary>📄 Abstract</summary>
  State convertibility specifies which transformations between states a quantum resource theory allows. In quantum-state texture, deterministic conversion criteria are known for qubits and pure sources in arbitrary dimension, but a general criterion for mixed states in higher dimensions is missing. We derive this exact criterion from a complete characterization of free operations in arbitrary finite dimension. Because the unique free state is pure, every free operation splits into a quantum filter...
  </details>

- **2026-11-25** — Tomás Lejarraga, Dirk U. Wulff, Ralph Hertwig — [Proverbs As A Window On Collective Prescriptions](http://arxiv.org/abs/2611.34832v1)
  <details><summary>📄 Abstract</summary>
  Proverbs, as repositories of traditional wisdom, have informed human reasoning for millennia. Yet the collective prescriptions they encode have remained largely unquantified. We introduce a computational framework to analyze nearly 50,000 English-language proverbs. Using large language models, validated against human judgments, we map the topical landscape of proverbs, assess their prescriptive power, and quantify their recommendations on key dimensions of human judgment and behavior. We find th...
  </details>

- **2026-11-25** — Yuxiang Lai, Jike Zhong, Yu-Jhe Li et al. — [Toward Agentic Robotics: A Large-Scale Study of Harness Design for Robot-Use Agents](http://arxiv.org/abs/2611.34778v1)
  <details><summary>📄 Abstract</summary>
  Recent vision-language models (VLMs) can act as robot-use agents that understand diverse scenes and control robots through policy code and tools. However, they predict 3D gripper poses poorly even with extended reasoning, struggling with precise manipulation. Vision-language-action (VLA) and world-action (WAM) models are the opposite: they execute fast, smooth control on trained tasks, yet fail under domain shifts or when tasks require long-horizon memory and reasoning. Agentic robots therefore ...
  </details>

- **2026-11-25** — Xiang Li, Hongyu Zhou, Ya-Li Li et al. — [SOLVE: Sparse, Ordered Keyposes Make LLM Agents Versatile and Efficient Robot Manipulator](http://arxiv.org/abs/2611.34750v1)
  <details><summary>📄 Abstract</summary>
  LLM agents have made remarkable progress in robot manipulation, yet they suffer from expensive inference, dense step-by-step control, and tool bottlenecks. We introduce SOLVE, a training-free, versatile and efficient agent policy: a multimodal LLM agent writes a sparse, ordered sequence of 6-DoF end-effector keyposes per call, observes the result, and writes the next, while a motion planner interpolates between them. The agent decides the number and spacing of keyposes for both fast long-range m...
  </details>

- **2026-11-25** — Chengzhi Zhao, Juelin Li, Zhennan Wang et al. — [Motion Beyond Pixels: Learning Future Visual Representations for Object-Centric Dynamics](http://arxiv.org/abs/2611.34644v1)
  <details><summary>📄 Abstract</summary>
  Many embodied world models predict future states in latent spaces optimized for RGB reconstruction, which do not explicitly prioritize object-level semantics and geometry relevant to motion generation. We present MotionRep, a visual representation world model that jointly generates future DINO representations and 3D object flow, coupling semantic and geometric information with object-centric dynamics. To make high-dimensional DINO features amenable to generative modeling, we introduce DINO-VAE, ...
  </details>

- **2026-11-25** — Thanapong Intharah, Pharamut Makjaroen, Kanvara Thawarorit et al. — [SMOTE 25 Years of Magic: What Has Been Done, What the Evidence Shows, and Whom It Reached](http://arxiv.org/abs/2611.34511v1)
  <details><summary>📄 Abstract</summary>
  Background. SMOTE was published in this journal in 2002 and reviewed here at its fifteenth anniversary in 2018. At twenty-five it is cited by more than 34,000 indexed works, half of them outside computer science. Objectives. To establish what the methods built on SMOTE change, how strong the evidence for them is, and whom the technique has reached. Methods. We audited a curated corpus of 76 papers, 37 of which propose a SMOTE-family generator, and tested its coverage with a systematic search of ...
  </details>

- **2026-11-25** — Felix Tristram, Benjamin D. Killeen, Nassir Navab — [Can Visual World Models See Force?](http://arxiv.org/abs/2611.34422v1)
  <details><summary>📄 Abstract</summary>
  World models and vision-language-action policy models are increasingly proposed as foundations for robot manipulation. They predict how scenes evolve and which actions to take, yet successful manipulation depends not solely on following observable trajectories but also on the hidden variable of interaction force. Neurophysiology has shown that humans possess a visual prior for this hidden variable, motivating us to ask the question: Do the representations of visual foundation models also capture...
  </details>

- **2026-11-25** — Shreshth Rai, Rishii Kumar Singh, Aksh Aggarwal — [Single-Database Rewards Are Hackable: Counterfactual Execution for Trustworthy Text-to-SQL RL](http://arxiv.org/abs/2611.34363v1)
  <details><summary>📄 Abstract</summary>
  Reinforcement learning (RL) for text-to-SQL agents pays a query when its result matches the reference on one database. However, a wrong query can match by luck when the data lack the rows that expose its bug. We study a counterfactual-database (CF) reward that also runs the final query on a few hidden, code-generated copies of the database and pays only if all results match (strict form) or by the share matched (mean form). On 1,302 synthetic audit questions, the strict form lowers the share of ...
  </details>

- **2026-11-25** — Sergei Kurchev, Iaroslav Kolomiets, Filipp Maksimov et al. — [DataForgeVLA: Fully Synthetic Manipulation Demonstrations for Vision-Language-Action Training](http://arxiv.org/abs/2611.34287v1)
  <details><summary>📄 Abstract</summary>
  We present a dataset of 340 fully synthetic manipulation demonstrations generated from real seed data for Vision-Language-Action (VLA) training. The corpus contains 32,340 frames with synchronized RGB and actions across eight object categories, represented as LeRobot v2.1 episodes with H.264 video, per-frame robot states and pose-valued action labels, language task annotations, summary statistics and quality decisions. Each synthetic demonstration is produced without additional teleoperation: a ...
  </details>

- **2026-11-25** — Gen Li, Fan Luo, Mengjun Lin et al. — [Loop4D: Embodied World Modeling with 4D VAEs and Looped Diffusion Transformers](http://arxiv.org/abs/2611.34199v1)
  <details><summary>📄 Abstract</summary>
  Predicting the outcomes of robotic manipulation requires modeling both visual appearance and evolving 3D geometry. This poses two challenges: video compression can obscure fine-grained robot motion, while jointly predicting RGB and geometry demands sufficient generative capacity. We introduce Loop4D, a framework that addresses these challenges through motion-preserving 4D representations and recurrent generative refinement. Our 4D VAE encodes RGB and pointmap sequences into compact spatiotempora...
  </details>

- **2026-11-25** — Zeyang Guan, Qihao Zhao, Rui Gong et al. — [SEEK: Self-Evolution through Execution Knowledge for Agentic Robot Manipulation](http://arxiv.org/abs/2611.33915v1)
  <details><summary>📄 Abstract</summary>
  General-purpose multimodal foundation models enable robots to adapt during deployment from observations and execution feedback, without task-specific demonstrations or training. However, the robot retains what it learns only in the model's working context. Once the task ends, it loses this execution knowledge, such as how to carry a bowl between two grippers. On the next attempt at the task, the robot may take just as long and repeat the same mistakes. To avoid this repetition, robots must retai...
  </details>

- **2026-11-25** — Xian Cui, Gan Yang, Dongqi Han et al. — [Tells of a Lying Machine: Analyzing LLM-Generated Strategic Dialogue in Chinese Werewolf](http://arxiv.org/abs/2611.33747v1)
  <details><summary>📄 Abstract</summary>
  Social-deduction games give models opposing objectives, but they also give roles different information and speaking obligations. We analyze 5,404 public utterances from 150 Chinese Werewolf games played by 12 models, comparing ordinary wolves with ordinary villagers so that special roles are excluded. Private knowledge and goals still differ, and no utterance is verified as true or false. After model and length adjustment, wolf utterances score higher on both certainty and uncertainty (coefficie...
  </details>

- **2026-11-25** — Wongyun Yu, Honggeun Kim, Donguk Lee et al. — [DexEngine: Scaling Human Demonstrations into Physically Executable Whole-Robot Data](http://arxiv.org/abs/2611.33579v1)
  <details><summary>📄 Abstract</summary>
  A growing body of recent work addresses the retargeting of human hand-object demonstrations to robotic hands. To train whole-robot policies, however, the retargeted motions must be kinematically feasible and physically executable, and be produced efficiently at scale. We present DexEngine, a simulation pipeline that turns human manipulation data into train-ready, physically executable arm-hand trajectories. DexEngine first places each clip's hand-object motion where the arms can reach it, finds ...
  </details>

- **2026-11-25** — Yipengjing Sun, Chenyang Wang, Boyao Zhou et al. — [LuxAvatar: Real-Time Relightable Head Avatars via Causal Neural Shading of 3D Intrinsic Proxies](http://arxiv.org/abs/2611.34940v1)
  <details><summary>📄 Abstract</summary>
  We present LuxAvatar, a feed-forward framework for real-time head avatar animation and relighting from a single portrait. To achieve both 3D controllability and complex facial light transport, we factorize avatar synthesis into an animatable 3D intrinsic Gaussian proxy and a causal autoregressive neural shader. This proxy disentangles canonical geometry and reflectance attributes, rapidly rasterizing deformed Gaussians into view- and motion-consistent PBR buffers. Conditioned on these buffers, o...
  </details>

- **2026-11-25** — Yihang Lu, Denica Kjorvezir, Ana Gjorgjevikj et al. — [Routeability Before Routing: Routeability Audit Protocol (RAP) and RouteabilityBench for Audited LLM Model Selection](http://arxiv.org/abs/2611.34825v1)
  <details><summary>📄 Abstract</summary>
  LLM routing aims to choose, for each prompt, which model in a portfolio is most likely to answer correctly. This only makes sense when the benchmark contains enough prompt-specific variation for different models to be best on different inputs. On coarse-scored LLM benchmarks, however, many models often tie for the best score, and the single best model may already leave little room for improvement. We therefore propose a routeability-first audit, instantiated as RAP and RouteabilityBench, a runna...
  </details>

- **2026-11-25** — Yichang Luo, Hourun Zhu, Shixiong Liu et al. — [Seeing the Right Context: Grounded On-Policy Distillation for Remote Sensing](http://arxiv.org/abs/2611.34700v1)
  <details><summary>📄 Abstract</summary>
  Remote sensing scene understanding requires multimodal large language models (MLLMs) to interpret queried targets in relation to nearby objects and surrounding structures, which serve as spatial references or define the scope of an answer. However, standard answers and bounding boxes often leave these contextual relationships implicit. Thus, we construct GeoContext-5K to make them explicit in 5,394 training pairs for visual question answering (VQA), with spatial cues, visual facts, and supportin...
  </details>

- **2026-11-25** — Kyungmin Min, Soyeon Kim, Junseok Kim et al. — [Find the Clue, Not the Scene: Rethinking Reasoning for Entity Recognition in Vision-Language Models](http://arxiv.org/abs/2611.34681v1)
  <details><summary>📄 Abstract</summary>
  Answering a knowledge-based visual question requires first recognizing the entity in the image and then recalling knowledge about it. Thinking vision-language models (VLMs) reason for thousands of tokens before answering, yet it remains underexplored how well such thinking VLMs perform each of these two steps. We therefore analyze thinking VLMs on this task and make two key observations. (1) Recognition is the bottleneck, since 76.3% of errors across four models on ViQuAE stem from misrecognizin...
  </details>

- **2026-11-25** — Mingchao Zhang, Miduo Cui, Kangze He et al. — [Do We Still Need Reinforcement Learning When We Can Read the World Model?](http://arxiv.org/abs/2611.34656v1)
  <details><summary>📄 Abstract</summary>
  Reinforcement learning has achieved remarkable success in sequential decision-making, but learning effective policies often requires substantial interaction experience. Model-based reinforcement learning alleviates this dependence by leveraging world models, which are typically used to support planning or policy optimization. In this paper, we investigate an alternative paradigm in which autonomous LLM-based coding agents directly synthesize control policies by reasoning over readable world mode...
  </details>

- **2026-11-25** — Zikai Zhang, Hubert P. Shum, Toby Breckon — [Commit2Drive: Perception-Grounded Language Decisions as Commitments for Trajectory Planning in Vision-Language-Action Driving Models](http://arxiv.org/abs/2611.34614v1)
  <details><summary>📄 Abstract</summary>
  Vision-Language-Action (VLA) models introduce language reasoning into end-to-end autonomous driving. They output a language decision together with a trajectory, which makes the planner more interpretable. However, in existing methods the language decision is either an independent output or an index that selects among similar candidate trajectories, and its annotations are not verified against the trajectory. As a result, the language decision and the trajectory are often inconsistent in closed-l...
  </details>

- **2026-11-25** — Shuai Yuan, Yuwei Gui, Mingshuang Luo et al. — [AGLR: Attribute-Guided Latent Refinement for Fine-Grained Humanoid Motion Generation and Editing](http://arxiv.org/abs/2611.34519v1)
  <details><summary>📄 Abstract</summary>
  Humanoid motion generation must accommodate evolving task requirements, where localized adjustments should satisfy new geometric constraints without disrupting desired motion details. However, language-based control lacks geometric precision, while joint-level constraints require explicit spatial targets. Local geometric constraints are also underdetermined, complicating target satisfaction and source preservation. We present AGLR (Attribute-Guided Latent Refinement), a unified framework for fin...
  </details>

- **2026-11-25** — Adhemar de Senneville, Xavier Bou, Jérémy Anger et al. — [Decoder-as-a-Probe: Verbalizing and Steering Visual Representations in LVLMs](http://arxiv.org/abs/2611.34515v1)
  <details><summary>📄 Abstract</summary>
  It is commonly accepted that high-level concepts are represented linearly in the representation space of large neural networks. For Large Vision Language Models (LVLMs), finding those interpretable directions in visual representations is important for interpretability. To find them, the classical approach is to train a linear classifier on the representations, but it needs a large amount of labels and only recovers what can be read from the representations, not what the model actually uses. In t...
  </details>

- **2026-11-25** — Eugene Lim, Nicholas Teh — [Computing Feasible EF1 Allocations under Generalized Assignment Constraints](http://arxiv.org/abs/2611.34488v1)
  <details><summary>📄 Abstract</summary>
  We study the fair allocation of indivisible goods under generalized assignment constraints, where each agent's bundle must fit within her budget, the sizes of goods may differ across agents, and unallocated goods go to a charity. A natural fairness notion here is feasible envy-freeness up to one good (FEF1), which requires an agent's envy towards any feasible subset of another bundle to disappear after some good is removed from this subset. While FEF1 allocations always exist, they could previou...
  </details>

- **2026-11-25** — Zeeshan Ali, Md Rayyan, Anshuman Chakravorty et al. — [Plausible Is Not Proven: Testing Failure Explanations in Monocular Depth Estimation](http://arxiv.org/abs/2611.34393v1)
  <details><summary>📄 Abstract</summary>
  Failure analyses of monocular depth models often name a cause for each error, such as an occluding boundary, a thin object or a reflective surface, but such labels are rarely tested. We present the Vision Error Observatory (VEO), an audit that finds regions failing the $δ_1$ criterion on sensor-measured pixels, labels each with a likely cause or abstains, and then subjects the labels to four tests: agreement with object annotations on data the label model never saw, agreement with blinded human ...
  </details>

- **2026-11-25** — Kiana Farhadyar, Yannick Vogt, Philipp Laur et al. — [EXPOSURE: Explaining Sources of Uncertainty in Reinforcement Learning](http://arxiv.org/abs/2611.34248v1)
  <details><summary>📄 Abstract</summary>
  Shapley values in reinforcement learning are used to explain which observation features drive an agent's behavior and expected return, but not its certainty. Explaining certainty requires understanding how observation features influence different sources of return uncertainty, and Shapley values need the agent's prediction for every subset of visible features. We propose EXPOSURE, which uses one mask-aware belief network for both action selection and Shapley explanations. It explains the varianc...
  </details>

- **2026-11-25** — Alex López-Cifuentes, Laura Martínez-Ferrer, Juan Ignacio Bravo Pérez-Villar — [Analemma $\infty$: A Temporal Benchmark for Geospatial Foundation Models](http://arxiv.org/abs/2611.34240v1)
  <details><summary>📄 Abstract</summary>
  Satellite time series capture how land surfaces change over time. Pixel-wise temporal foundation models read a year of satellite observations per pixel, yet public benchmarks lack a temporal axis or subsample it to a few dates. We introduce Analemma, a temporal benchmark of six datasets that carry every 10 and 20 m Sentinel-2 band and a time series spanning a growing season, completed where their releases omit geometry, dates, or cloud masks. One frozen-encoder protocol evaluates all models acro...
  </details>

- **2026-11-25** — Luoxi Zhang, Tianyi Tan, Jiawei Liu et al. — [Lost in the Grid: Where Multimodal LLMs Fail Between Seeing and Planning](http://arxiv.org/abs/2611.34152v1)
  <details><summary>📄 Abstract</summary>
  Multimodal large language models (MLLMs) excel at static visual understanding and are increasingly applied to spatial planning, where a model interprets a visual layout and outputs an action sequence to reach a goal. Grid games are a common testbed for this ability because their rules are explicit and a solver can verify every move. Yet existing benchmarks mostly report end-to-end success rates, which hide whether a failure stems from visual perception, rule application, or multi-step planning. ...
  </details>

- **2026-11-25** — Katsuya Ogata, Kazuya Nishimura, Yuta Nakashima — [What Makes a Gavagai? Learning Visual Concepts from One Positive and Few Negatives](http://arxiv.org/abs/2611.34105v1)
  <details><summary>📄 Abstract</summary>
  Humans can recognize novel concepts from only a few observations by identifying defining visual attributes and eliminating alternative interpretations. However, a single observation is consistent with multiple possible concepts, and accurate visual perception alone is insufficient to determine the intended interpretation. Negative evidence can reduce this ambiguity by eliminating competing hypotheses. Inspired by Quine's gavagai problem, we introduce the Gavagai Benchmark to evaluate whether vis...
  </details>

- **2026-11-25** — Haechan Shin, Hoonki Lee, Jungwoon Kang et al. — [The Reference Matters: Displacement Probing for Weight-Space Learning](http://arxiv.org/abs/2611.33998v1)
  <details><summary>📄 Abstract</summary>
  Weight-space learning predicts a model's attributes directly from its parameters, and probing-based methods do so efficiently by reading a model's responses to learned probes. Prior work shows that probing succeeds within a Model Tree -- models fine-tuned from a shared pretrained origin -- but not why. We trace this to the shared origin itself: since a tree's leaves start from the same weights, what distinguishes them is their displacement from that origin. This motivates probing the displacemen...
  </details>

- **2026-11-25** — Mingyuan Li, Tong Jia, Ziyuan Yang et al. — [EGSE: Evidence-Grounded Skill Evolution for Medical Reasoning Agents](http://arxiv.org/abs/2611.33909v1)
  <details><summary>📄 Abstract</summary>
  Medical reasoning agents combine foundation models with specialized tools to interpret medical images, yet reusing their historical experience remains challenging. A correct final answer can conceal flawed reasoning or tool use, synthesized advice may lack source support, and superficially similar cases may require different diagnostic procedures. In this paper, we propose EGSE, an evidence-grounded skill evolution framework that distills historical dialogues from similar cases into reusable con...
  </details>

- **2026-11-25** — Zike Luo, Hao Li, Mengxiao Wang et al. — [Structured Noise Diffusion for Echocardiography Haze Removal](http://arxiv.org/abs/2611.33860v1)
  <details><summary>📄 Abstract</summary>
  Echocardiographic images are frequently degraded by spatially structured haze artifacts that obscure anatomical boundaries and hinder clinical analysis. Conventional diffusion models typically employ pixel-independent Gaussian noise, limiting their ability to represent localized ultrasound haze. In this study, we propose a structure-informed diffusion framework that explicitly models ultrasound haze as an accumulation of localized Gaussian components constrained by the ultrasound fan geometry. T...
  </details>

- **2026-11-25** — Messi H. J. Lee — [Language models call themselves AI but do not favor AI over people](http://arxiv.org/abs/2611.33851v1)
  <details><summary>📄 Abstract</summary>
  Many fear that AI systems will side with one another against people. Social identity theory, which explains why people favor their own group, offers one way to examine this fear. Seen through this theory, AI would side with AI only if it treated AI as its group and favored AI over people. In three experiments, 24 language models favored a group they were assigned to, even a team of AI agents. With no group assigned, they gave a person more money and credit than an AI agent. Prompts that made the...
  </details>

- **2026-11-25** — Hengyi Cai, Yuqi Tang, Zichang Li et al. — [ChemDeduce: Benchmarking LLMs for Unknown Chemical Identification through Interactive Simulated Experiments](http://arxiv.org/abs/2611.33848v1)
  <details><summary>📄 Abstract</summary>
  Large language models (LLMs) have shown strong performance in chemical knowledge and reasoning, yet it remains unclear whether they can solve problems whose answers must be discovered through experimentation. We investigate this question through Unknown Chemical Identification, where a model must actively design experiments, interpret observations, update hypotheses, and ultimately identify a hidden substance. We introduce ChemDeduce, an interactive evaluation framework for assessing LLMs throug...
  </details>

- **2026-11-25** — Yixuan Duan, Kexin Geng, Hanwen Xu et al. — [Can Its Own Misses Teach an MLLM to Find Small Brain Metastases?](http://arxiv.org/abs/2611.33836v1)
  <details><summary>📄 Abstract</summary>
  Multimodal large language models (MLLMs) are becoming general readers of medical images, yet they remain weak at locating small abnormalities. Brain metastases expose this gap: at 384 px a 0.1 mL lesion covers less than a quarter of one visual token, and at one false positive per scan frontier MLLMs find fewer than 30% of lesions of 0.1-1 mL. Fine-tuning on one dataset helps but transfers poorly, and improving it further is slow trial and error steered by a single score. We introduce LANTERN (Le...
  </details>

- **2026-11-25** — Afifah Kashif, Malak Sadek, Jin Huang et al. — [Refusal Is Not Scored: A Coverage Limit in Content-Based Bias Evaluation](http://arxiv.org/abs/2611.33690v1)
  <details><summary>📄 Abstract</summary>
  Bias audits of conversational models often discard refusals (responses such as "I can't assist with that request") before scoring, a filtering step which is rarely examined as a measurement decision even though it determines which responses an audit is capable of evaluating. This work examines what the step removes, applying seven bias-evaluation instruments spanning both deployed paradigms, three dictionary-based and four LLM-as-judge, to two intersectional datasets of 360 generated responses e...
  </details>

- **2026-11-25** — Yuxuan Sun, Yuanjian Xu, Jianing Hao et al. — [Rethinking Knowledge Distillation for Diffusion Language Models](http://arxiv.org/abs/2611.33670v1)
  <details><summary>📄 Abstract</summary>
  Knowledge distillation has recently proven highly effective for improving autoregressive models, but its applicability to DLMs remains poorly understood. We present the first systematic study of KD for DLMs and uncover two non-intuitive failures of classical forward-KL (FKL) distillation: (i) student perplexity does not improve monotonically with more teacher-generated data, and (ii) on the same teacher-generated corpus, FKL distillation underperforms simply training the student with the origina...
  </details>

- **2026-11-25** — Shen Chen, Lei Li, Jiajun Sun et al. — [Controllable CAD Generation and Interactive Editing of Fluid Rotors](http://arxiv.org/abs/2611.33617v1)
  <details><summary>📄 Abstract</summary>
  Computer-aided design (CAD) provides the geometric foundation for rotors in fluid rotating machinery. However, creating models for different rotors requires different modeling processes, making it difficult to control geometry through design intent and reuse existing models. We introduce VaneCraft, an agent-driven framework for rotor generation, inverse recovery, and editing through a unified analytical representation. The agent interprets design requests and invokes geometric modeling operation...
  </details>

- **2026-11-25** — Gerard McCaul — [The Phases of Hierarchy](http://arxiv.org/abs/2611.33566v1)
  <details><summary>📄 Abstract</summary>
  We develop a dynamical phase theory of hierarchy, in which depth decides whether a population of size $N$ that revises its own environment can correct it without overcorrecting. The statistics that let a large majority detect a small bias - the basis of the Condorcet jury theorem - also make its response grow as $\sqrt{N}$. Fed back into the environment it is judging, this sharpening destabilises the matched state through a flip bifurcation at a critical loop gain, which we obtain analytically f...
  </details>

- **2026-11-24** — Constanza Gacitúa Fuentes, Marcos Kiwi, Matías Pavez-Signé — [Graphon hitting times: connectivity and minimum degree](http://arxiv.org/abs/2611.33540v1)
  <details><summary>📄 Abstract</summary>
  A classical result in random graphs states that the Erdős--Rényi random graph process becomes connected at exactly the moment its last isolated vertex disappears. The main goal of this paper is to establish a graphon analogue of this result. Let $G(n,W)$ be the inhomogeneous random graph sampled from a graphon $W$, and reveal its edges one by one in a uniformly random order. We prove that if $W$ is connected and the lower tail of its degree distribution satisfies $g_W(t)/t\to 0$ as $t\to 0$, whi...
  </details>

- **2026-11-24** — Maham Tanveer, Hao Zhang — [CoSMo: A Compact Spectral Space of Body Motion in Video](http://arxiv.org/abs/2611.33296v1)
  <details><summary>📄 Abstract</summary>
  We introduce CoSMo, a compact spectral space of body motion in video, in which each motion is a single code that can be compared and edited without training, transferred to a new subject, interpolated, composed, scaled in intensity and detail, or sampled anew. Our encoder expresses how a clip's DINOv2 features change over time in a fixed temporal basis, the discrete cosine transform (DCT), and compresses this change into 384 numbers. Because each frequency band is the same cosine pattern in ever...
  </details>

- **2026-11-24** — Hanzhen Wang, Jiaming Xu, Guohao Dai — [LEGOSpec: A Composable and Efficient Framework for Speculative Draft Design and Training](http://arxiv.org/abs/2611.33004v2)
  <details><summary>📄 Abstract</summary>
  Speculative decoding accelerates large language model (LLM) generation using a lightweight draft. Existing methods evaluate complete recipes under different training configurations, leaving component effects, interactions, and composition benefits unclear. Therefore, we present LEGOSpec, a composable framework for speculative draft design and training. LEGOSpec decomposes draft models into Context, Backbone, Proposal, and Objective components that share a unified training infrastructure. Using L...
  </details>

- **2026-11-24** — Alexandros Theocharous, Holger Caesar, Ziqi Zhang — [CriticalScenes: Scalable Photorealistic Critical-Scenario Generation for Closed-Loop Driving Adaptation](http://arxiv.org/abs/2611.33255v1)
  <details><summary>📄 Abstract</summary>
  Safety-critical interactions are rare in recorded driving data, leaving end-to-end driving planners with limited exposure to evasive behaviour during training. This lack of critical supervision can lead to unsafe behaviour and, in rare instances, collisions. To address this gap, we introduce CriticalScenes, a reconstruction-based framework that transforms ordinary recorded driving scenes into photorealistic safety-critical interactions with corresponding collision-avoidance supervision. Across 5...
  </details>

- **2026-11-24** — Divya Joshi, Ruize Yang, Colleen Peyton et al. — [Biomechanically Grounded Prediction of Selective Motor Control and Clinical Outcomes from Infant Video](http://arxiv.org/abs/2611.32890v2)
  <details><summary>📄 Abstract</summary>
  Early identification of cerebral palsy (CP) relies on observational assessments of spontaneous infant movement, such as the General Movement Assessment (GMA) and the Baby Observational Selective Control AppRaisal (BabyOSCAR), which require trained raters and substantial scoring time. Existing automated approaches derive hand-engineered features from two-dimensional keypoints, which describe image-plane motion rather than the three-dimensional behavior of individual joints. We present Baby Biomec...
  </details>

- **2026-11-24** — Sichen Wu, Qian Sun, Mengfan Liu et al. — [DiffGR00T: Execution-Aware Differentiable Training for Humanoid Whole-Body Vision-Language-Action Models](http://arxiv.org/abs/2611.32665v2)
  <details><summary>📄 Abstract</summary>
  Vision-language-action (VLA) models have achieved strong results in arm-centric manipulation, yet humanoid whole-body control (WBC) requires dynamic balance and tightly coupled full-body coordination. Existing hierarchical humanoid VLAs typically decouple motion generation from physical execution, leaving tracking and balance errors unable to directly optimize the VLA generator. We propose DiffGR00T, an end-to-end differentiable training framework that couples GR00T N1.7 with SONIC, a pretrained...
  </details>

- **2026-11-24** — Shubhajyoti Das, Pritam Bikram, Arindam Biswas et al. — [Resource-Efficient Multimodal Fusion for Early Rice Blast Forecasting in Sustainable Agriculture](http://arxiv.org/abs/2611.33237v1)
  <details><summary>📄 Abstract</summary>
  Resource-efficient artificial intelligence has become increasingly important for sustainable agriculture, where timely disease forecasting must be achieved under computational and energy constraints. Early estimation of rice blast can enhance food security by optimizing crop management practices while reducing excessive pesticide use. However, existing frameworks often suffer from high computational overhead and limited capability to model the complex spectral-temporal dependencies present in he...
  </details>

- **2026-11-24** — Qineng Wang, Jianwen Lyu, Pingyue Zhang et al. — [RoboARC: Physical Puzzles for Robotic Manipulation under Spatial Constraints](http://arxiv.org/abs/2611.33390v1)
  <details><summary>📄 Abstract</summary>
  Many hard manipulation tasks come down to a spatial constraint that only a few motions satisfy, such as passing a part through a gap barely wider than itself or separating two interlocked parts. These motions depend on the exact geometry of each scene, so demonstrations and skills recorded elsewhere rarely transfer. We therefore ask: when manipulation hinges on spatial constraints, can robots reason out the right motions? We introduce RoboARC, a benchmark of 90 tasks in six constraint types over...
  </details>

- **2026-11-24** — Burcu Kilic, David Drexel, Emre Ugur et al. — [Effect-Driven Skill Abstractions for Offline Reinforcement Learning](http://arxiv.org/abs/2611.33229v1)
  <details><summary>📄 Abstract</summary>
  We seek to learn discrete skill abstractions to facilitate long-horizon, goal-conditioned reinforcement-learning (RL) tasks. Recent approaches have shown success by quantizing actions via clustering or reconstruction. However, these objectives lead to skills that are not directly related to what the current state affords or what the goal requires. Instead, we argue that goal-directed skills should be driven by \emph{how they affect the state} of the agent. To realize this, we introduce a novel q...
  </details>

- **2026-11-24** — Zheng Sun, Zhuo Li, Zhihao Li et al. — [RESET: One Demonstration, One Verified World, Self-Improved Skills Across Embodiments](http://arxiv.org/abs/2611.31894v2)
  <details><summary>📄 Abstract</summary>
  Large language model (LLM) coding agents can iteratively self-improve robot manipulation skills in simulation benchmarks, yet real-world tasks provide neither ground-truth success scorers nor resettable practice environments. Our key observation is that a single real demonstration simultaneously specifies scene geometry, defines the terminal success criterion, and serves as a physical reference trajectory for verifying world fidelity---all decoupled from the source robot's kinematics. We present...
  </details>

- **2026-11-24** — Ahmed Alajrami, Ondrej Bohdal, Seokwoo Song et al. — [LogToPersona: New Benchmark and Efficient Persona Prediction through Semantic Log Filtering](http://arxiv.org/abs/2611.33510v1)
  <details><summary>📄 Abstract</summary>
  Detailed knowledge of a user's persona is valuable for personalizing generative AI models and agents, yet such details are difficult to obtain and change over time. We address the task of inferring persona attributes from a single day of mobile activity logs. No suitable publicly available benchmark exists for this task, so we introduce a synthetic benchmark of 1,600 persona-log pairs. We target on-device inference so that raw logs never leave the phone, which makes memory rather than speed the ...
  </details>

- **2026-11-24** — Masayuki Takayama, Shohei Shimizu — [Joint Estimation of Abilities and Item Parameters for Large Language Models Using Probability and Binary Responses: A Fractional-Response IRT Framework](http://arxiv.org/abs/2611.33493v1)
  <details><summary>📄 Abstract</summary>
  Large language model (LLM) evaluations provide two response types: probabilities assigned to correct answers and binary indicators of correctness. Restricting evaluation to one type narrows the range of available models or discards probability information. We propose a method to integrate both types through a common two-parameter logistic item response model and fractional-response quasi-maximum likelihood estimation. The framework includes binary-only models in common-scale evaluation without d...
  </details>

- **2026-11-24** — Ishita Chakraborty, Xingjian You, Shrabastee Banerjee — [AI-human hybrid conversations: Can AI Agents Improve Discourse Quality?](http://arxiv.org/abs/2611.33459v1)
  <details><summary>📄 Abstract</summary>
  Conversations are central to how people exchange information, share experiences, and develop collective understanding. Yet, across conversational settings, discussions often suffer from uneven participation, unanswered contributions, and a narrow range of perspectives. As generative AI agents increasingly participate alongside humans, hybrid human-AI conversations present a new opportunity to address these challenges. We investigate whether AI agents can serve as catalysts for human interaction,...
  </details>

- **2026-11-24** — Chun He — [The Information Content of News Embeddings](http://arxiv.org/abs/2611.33458v1)
  <details><summary>📄 Abstract</summary>
  Does the predictive success of news embeddings reflect a better measure of news surprises or other sources of return predictability in text? We decompose news embeddings by content into event-category, firm-identity, and idiosyncratic components, and by timing into historical levels and current deviations. At short horizons, event categories account for most of the predictive power of embedding forecasts, and simple forecasts based on historical average returns after news in each event category ...
  </details>

- **2026-11-24** — Mohamed El-Hadedy — [WADJET: Whole-Job Authorization and Dispatch for Job Execution Trust on FPGA System-on-Chip Accelerators](http://arxiv.org/abs/2611.33406v1)
  <details><summary>📄 Abstract</summary>
  On an FPGA system-on-chip, the software that submits work to an accelerator also decides what the accelerator does. It writes the registers one by one, and the hardware runs whatever it finds, so faulty or compromised software can change one address or resend a job. Existing protections decide who may reach an accelerator or keep its data safe. Deciding whether one job was approved and is still unused takes three things in one place: the only way to the accelerator, the whole job held back until...
  </details>

- **2026-11-24** — Jingtao Zhang, Zeming Liu, Haorui Gao — [GhostAPI-V: Evaluating Audited Diagnostics for Internal API Migration Repair](http://arxiv.org/abs/2611.33396v1)
  <details><summary>📄 Abstract</summary>
  API migrations require callers to adopt target-version usages while removing incompatible legacy usages. GhostAPI-V represents these obligations as human-audited temporal contracts and supplies candidate-specific repair diagnostics, with correctness assessed by independent behavioral tests. We evaluate 48 internal migrations from eight Python repositories using Claude Code and Codex, with two initial runs per agent and task. Five revision arms branch from the same 192 initial candidates, control...
  </details>

- **2026-11-24** — Kaiyang Li, Shaobo Han, Shihao Ji — [Change Partners at Every Layer: Balanced Random Regrouping for Model Merging](http://arxiv.org/abs/2611.33308v1)
  <details><summary>📄 Abstract</summary>
  Model merging combines fine-tuned experts into one model that serves many tasks without retraining, but merging many experts this way substantially reduces accuracy. Grouping offers a middle ground: at every layer or weight matrix, the $N$ experts are divided into $K<N$ groups, the experts in a group are merged into one shared module, and a task uses the module merged from its expert's group. Natural choices are to keep the same partners across layers or to group similar experts. Surprisingly, w...
  </details>

- **2026-11-24** — Maximus Adeola — [Focus On Facts: Stylistically Invariant and Factually Sensitive Text Embeddings](http://arxiv.org/abs/2611.33250v1)
  <details><summary>📄 Abstract</summary>
  Text embedding models can conflate surface-form similarity with factual identity. Given an altered near-copy with one corrupted fact and a differently worded fact-preserving rewrite, the base model prefers the altered near-copy. We test whether hard-negative contrastive supervision can reduce this surface-similarity shortcut. We construct FOF-Bench, an 83,263-triplet benchmark spanning five domains. Each anchor is paired with an LLM-generated, fact-preserving stylistic rewrite and a matched fact...
  </details>

- **2026-11-24** — Tejas Tovinkere Pattabhi — [Typical Angina, Reversed: A Long-Standing Documentation Error in the UCI Heart Disease Data](http://arxiv.org/abs/2611.33248v1)
  <details><summary>📄 Abstract</summary>
  The UCI Heart Disease data are a widely used machine-learning benchmark. We show that their chest-pain variable is stored in reverse of its documentation. At all four sites, the code documented as "asymptomatic" (4) marks patients with typical angina, and the code documented as "typical angina" (1) marks patients with almost none of the classical angina features (at Cleveland, no chest pain).   Two complementary checks establish this: (i) the chest-pain table and regression coefficients of the o...
  </details>

- **2026-11-24** — Lennart Schiweck, Cristóbal Curio — [MinPair: Measured Minimal Pairs for Fine-Grained Control in Text-to-Motion Generation](http://arxiv.org/abs/2611.32549v2)
  <details><summary>📄 Abstract</summary>
  Text-to-motion generation has made great progress in capturing what action to perform, yet it remains limited in controlling how that action is executed. For example, when only the height word of a kick request changes, none of the tested state-of-the-art methods reaches all three of knee, waist and head height. The other words of a caption usually imply an attribute such as height, so neither the training loss nor the standard metrics require a model to use the word that states it. A model has ...
  </details>

- **2026-11-24** — Jiayuan Du, Yebo Feng, Lin Zhang et al. — [Where Did My Tokens Go? Verifiable Token Billing for LLM Services](http://arxiv.org/abs/2611.31806v1)
  <details><summary>📄 Abstract</summary>
  Users of large language model (LLM) services receive token bills with limited evidence of which calls incurred their charges. In broker-mediated agent workflows, calls arise after authorization and billing evidence spans service domains. A bill can count one genuine receipt twice and omit another. Valid metering evidence can also be attributed to the wrong execution. We present \textsc{TokenProv}, which uses authenticated provider acceptances to establish settlement coverage and verify token cha...
  </details>

- **2026-11-24** — Hanzhen Wang, Jiaming Xu, Guohao Dai — [LEGOSpec: A Composable and Efficient Framework for Speculative Draft Design and Training](http://arxiv.org/abs/2611.33004v1)
  <details><summary>📄 Abstract</summary>
  Speculative decoding accelerates large language model (LLM) generation using a lightweight draft. Existing methods evaluate complete recipes under different training configurations, leaving component effects, interactions, and composition benefits unclear. Therefore, we present LEGOSpec, a composable framework for speculative draft design and training. LEGOSpec decomposes draft models into Context, Backbone, Proposal, and Objective components that share a unified training infrastructure. Using L...
  </details>

- **2026-11-24** — Nan Li, Shaofeng Liang, Shiyun Zhao et al. — [PAVE: Preference-Aligned Visual Egocentric Learning for the Blind and Low-Vision Users](http://arxiv.org/abs/2611.32996v1)
  <details><summary>📄 Abstract</summary>
  Egocentric video question answering enables blind and low-vision (BLV) users to query their immediate surroundings through natural language. However, existing benchmarks and models primarily optimize for semantic agreement with reference answers, reducing visual assistance to a purely factual matching task. In real-world scenarios, a factually correct response remains practically unhelpful if it lacks the spatial orientation, actionable detail, or conciseness required by the immediate task of th...
  </details>

- **2026-11-24** — Vincent Koc, Aditya Washikar, Rishab Naveen Venkataraman et al. — [ShellBench: What Matters More for AI Agents, Models, or Harness for Everyday Tasks](http://arxiv.org/abs/2611.32946v1)
  <details><summary>📄 Abstract</summary>
  The use of AI agents among the general public has been increasing exponentially throughout 2026, though it is often hard for users to determine which configuration is most effective for their personal use. To help provide clarity here we introduce ShellBench, 100 day-to-day tasks based on more than 10 million user requests, each set in a realistic workspace with messy files and competing data sources, and graded for both correctness and safety. We evaluate 12 models across 5 agent harnesses at 3...
  </details>

- **2026-11-24** — Divya Joshi, Ruize Yang, Colleen Peyton et al. — [Biomechanically Grounded Prediction of Selective Motor Control and Clinical Outcomes from Infant Video](http://arxiv.org/abs/2611.32890v1)
  <details><summary>📄 Abstract</summary>
  Early identification of cerebral palsy (CP) relies on observational assessments of spontaneous infant movement, such as the General Movement Assessment (GMA) and the Baby Observational Selective Control AppRaisal (BabyOSCAR), which require trained raters and substantial scoring time. Existing automated approaches derive hand-engineered features from two-dimensional keypoints, which describe image-plane motion rather than the three-dimensional behavior of individual joints. We present Baby Biomec...
  </details>

- **2026-11-24** — Siamak Ravanbakhsh, David Nitchi, Khang Ngo — [Scaling Laws of Ensemble Uncertainty in Language Models](http://arxiv.org/abs/2611.32801v1)
  <details><summary>📄 Abstract</summary>
  Many use cases for large language models (LLMs)---from AI safety to exploration and human interaction---can benefit from epistemic uncertainty estimates. We argue that existing Bayesian Deep Learning solutions, which are often restricted to a fixed model family, fail to capture the full epistemic uncertainty at practical LLM scales. This is because the error due to the bounded capacity of the model family remains invisible to disagreement among models supported by the prior. We relate this error...
  </details>

- **2026-11-24** — Lance Calvin Lim Gamboa, Yue Feng, Mark Lee — [Social Bias Neurons in Multilingual Language Models: A Mechanistic Interpretability Analysis](http://arxiv.org/abs/2611.32685v1)
  <details><summary>📄 Abstract</summary>
  Multilingual models exhibit social bias when processing inputs pertaining to societal stereotypes. We adapt emerging mechanistic interpretability methods to pinpoint and characterize model components that encode this bias. We conduct our analysis across three instruction-tuned models, four languages, and seven bias dimensions. Specifically, we leverage multilingual bias benchmarks in implementing two methods for identifying social bias neurons: activation probability entropy and integrated gap g...
  </details>

- **2026-11-24** — Sichen Wu, Qian Sun, Mengfan Liu et al. — [DiffGR00T: Execution-Aware Differentiable Training for Humanoid Whole-Body Vision-Language-Action Models](http://arxiv.org/abs/2611.32665v1)
  <details><summary>📄 Abstract</summary>
  Vision-language-action (VLA) models have achieved strong results in arm-centric manipulation, yet humanoid whole-body control (WBC) requires dynamic balance and tightly coupled full-body coordination. Existing hierarchical humanoid VLAs typically decouple motion generation from physical execution, leaving tracking and balance errors unable to directly optimize the VLA generator. We propose DiffGR00T, an end-to-end differentiable training framework that couples GR00T N1.7 with SONIC, a pretrained...
  </details>

- **2026-11-24** — Konrad Stolte, Toni Fetzer — [Generating Schema-Aligned Synthetic Dialogues and Measuring Their Diversity](http://arxiv.org/abs/2611.32631v1)
  <details><summary>📄 Abstract</summary>
  Training or evaluating a model that turns a conversation into a structured record requires paired data, meaning a transcript together with the exact record it should be converted into. Such pairs are expensive to annotate, and in sensitive domains they are also difficult to obtain at all. We therefore build them in the opposite order by sampling a schema-valid record first, then writing a dialogue from it, and optionally synthesizing speech from the dialogue, so the label exists before the text ...
  </details>

- **2026-11-24** — Mickaël D. Chekroun, Ilan Koren, Honghu Liu — [Emergent cloud patterns from stochastic jump models of parcel microphysics](http://arxiv.org/abs/2611.32596v1)
  <details><summary>📄 Abstract</summary>
  Warm clouds organize into bands, cells, and intricate wave networks, yet the dynamical mechanisms connecting these forms remain difficult to isolate. To bridge unresolved parcel microphysics and cloud organization, we formulate a spatial jump-process model of cloud-water and rain-water anomalies in an activated regime and analyze its mean-field closure. Eliminating fast supersaturation adjustment from droplet growth and vapor transport supplies a screened environmental kernel, which we couple to...
  </details>

- **2026-11-24** — Lennart Schiweck, Alaa Saleh, Cristóbal Curio — [SetCon: Setup-Conditioned IMU-Language Learning from 3D Human Motion](http://arxiv.org/abs/2611.32548v1)
  <details><summary>📄 Abstract</summary>
  Aligning inertial measurement unit (IMU) signals with text enables zero-shot activity recognition across wearable devices. A worn device's signal depends on its setup, the combination of body site and mounting. Leading IMU-language models make their encoders invariant to the mounting, which also discards the device's orientation relative to the body, such as the direction of gravity that separates sitting, standing and lying. We introduce SetCon, which replaces full invariance with selective inv...
  </details>

- **2026-11-24** — Kunjie Lin, Haitao Zhang, Bosheng Chen et al. — [Towards a Multimodal Aesthetic Agent for Photographic Reference Grading](http://arxiv.org/abs/2611.32299v1)
  <details><summary>📄 Abstract</summary>
  Reference-guided photographic color grading helps users realize their aesthetic intent by selectively drawing on the color and tonal characteristics of a reference photograph. Doing so requires understanding which characteristics users wish to adopt and translating these preferences into controllable edits. However, image-only reference methods align overall appearance without instruction-grounded selection, while pixel-space generative editors typically produce flattened images without editable...
  </details>

- **2026-11-24** — Shin'ya Yamaguchi, Kosuke Nishida — [Relational Bottleneck Models](http://arxiv.org/abs/2611.32227v1)
  <details><summary>📄 Abstract</summary>
  Achieving both interpretable and high-performance inference is a key challenge in deep learning. While Concept Bottleneck Models (CBMs) provide inherent interpretability, they are constrained by task-specific training and rely on isolated visual concepts that fail to capture higher-order visual semantic relationships. Conversely, Large Vision Language Models (LVLMs) demonstrate zero-shot capabilities through Chain-of-Thought (CoT) reasoning. However, standard CoT lacks a strict causal dependency...
  </details>

- **2026-11-24** — Zhuoying Yang, Jiachen Ni, Yichen Guo et al. — [RoboProbe: Benchmarking Physical Plausibility of Robot World Models](http://arxiv.org/abs/2611.32152v1)
  <details><summary>📄 Abstract</summary>
  Evaluating the physical plausibility of generated videos is critical for reliable robotic planning with world models. These videos inform action proposal and assessment before real-world execution, so undetected physical violations can lead to erroneous assessments of action feasibility and safety. Yet current video generators often produce physically implausible interactions. Detecting such violations directly with vision-language models (VLMs) remains challenging as physical verification requi...
  </details>

- **2026-11-24** — Tian Tang, Guo Chen, Reed Li et al. — [LARF: Learning-aligned Reasoning Framework for Search Relevance](http://arxiv.org/abs/2611.32125v1)
  <details><summary>📄 Abstract</summary>
  Query-document relevance estimation is a core component of AI-native search systems, where a model must assess whether retrieved documents satisfy users' information needs under complex, multi-dimensional criteria. However, directly applying large language models (LLMs) to this task remains challenging because conventional supervised fine-tuning (SFT) provides limited supervision for domain-specific judgment rationales, while standard trajectory-level reinforcement learning (RL) objectives do no...
  </details>

- **2026-11-24** — Zeteng Lin, Yikang Liu, Bolin Zeng et al. — [Do Clinician-Scored Examples Help LLMs Code ADOS-2 from Hour-Long Transcripts?](http://arxiv.org/abs/2611.32050v1)
  <details><summary>📄 Abstract</summary>
  Large language models can apply a written rubric to a transcript, making automated coding of the Autism Diagnostic Observation Schedule (ADOS-2) look within reach. A common way to align such a rater with clinicians is to show it expert-scored examples, but whether correct labels improve agreement is rarely tested. We test this for eight speech-based items of hour-long ADOS-2 Module 3 sessions from 48 children, with one local model and a pre-registered, placebo-controlled design. We compare few-s...
  </details>

- **2026-11-24** — Yuncheng Zhang, Songtao Jiang, Yitian Tang et al. — [HuluOPD: Unifying Heterogeneous Medical Specialists into One Lightweight Model with Unlabeled Prompts](http://arxiv.org/abs/2611.32021v1)
  <details><summary>📄 Abstract</summary>
  Specialist medical vision-language models (VLMs) are strong within their specialties but hard to unify: their training data are often private, and independently developed specialists cannot be assumed to share an architecture. Deploying these large models separately is costly. We present HuluOPD, an on-policy distillation recipe that unifies heterogeneous specialists into one lightweight VLM using only unlabeled prompts, without requiring reference answers or the specialists' training data. The ...
  </details>

- **2026-11-24** — Jason Wei, George Pu, Jingxuan Fan et al. — [To Critic Or Not To Critic](http://arxiv.org/abs/2611.32013v1)
  <details><summary>📄 Abstract</summary>
  As large language models tackle longer and more complex tasks, understanding when a critic improves the efficiency of reinforcement learning (RL) becomes increasingly important. Proximal Policy Optimization (PPO) trains a critic to reduce variance and provide fine-grained credit assignment, while Group Relative Policy Optimization (GRPO) drops the critic and avoids the bias of bootstrapping from the critic's value estimates. Although recent critic-based methods have reported strong performance r...
  </details>

- **2026-11-24** — Sunwoo Kim, Hyunjin Hwang, Geon Lee et al. — [User-Adaptive Fusion of Multiple Foundation Models for Recommender Systems](http://arxiv.org/abs/2611.31951v1)
  <details><summary>📄 Abstract</summary>
  Can recommender systems benefit from combining a collection of foundation models within and across modalities? While different foundation models may capture complementary aspects of item metadata, we find that naively combining their representations yields only marginal gains over using a single foundation model. We make a key observation: the users who benefit vary across foundation models. Motivated by this observation, we introduce UF2O, a user-adaptive approach for fusing multiple foundation...
  </details>

- **2026-11-24** — Seonghwan Park, Yong-Hoon Kwon, Min-Gyu Park — [Generalizable Feed-Forward 3D Hand-Object Reconstruction with Coarse-to-Fine Contact Estimation](http://arxiv.org/abs/2611.31812v1)
  <details><summary>📄 Abstract</summary>
  Reconstructing the 3D poses of hands and objects from a single image, together with the contact between them, is fundamental to understanding manipulation. To be practical, the reconstruction must generalize to unseen objects, and the contact must be localized precisely. Yet joint feed-forward estimators often rely on predefined object sets, while contact is typically predicted from image features alone, without the explicit geometry needed to localize it. To address both limitations, we present...
  </details>

- **2026-11-24** — Jia Hu, Changjian Yu, Panqu Wang et al. — [A Generative AI Agent to Emulate Interactive Human-driven Vehicles for Automated Driving Testing in Urban Areas](http://arxiv.org/abs/2611.31797v1)
  <details><summary>📄 Abstract</summary>
  Realistic modeling of human-driven vehicle (HDV) interactions is essential for automated driving safety testing in urban areas. Existing methods struggle to reproduce realistic safety-critical interactions involving high collision risk for the following reasons: they often assume full observability, overlooking interactions arising from occlusion. Driving styles are mainly characterized by vehicle maneuvers, limiting the diversity of safety-critical interaction behaviors. Moreover, learning sign...
  </details>

- **2026-11-24** — Ankit Chadha, Pratyay Banerjee — [fork() for Agents: Agent Kernel for Non-blocking LLM Orchestration](http://arxiv.org/abs/2611.31727v1)
  <details><summary>📄 Abstract</summary>
  LLM-based agents typically execute tool calls synchronously and discard completed work upon failure. Subgraph-selective recovery, re-executing only a failed node's transitive descendants, is a well-established pattern in distributed systems (Spark, Erlang/OTP, Dryad), and recent agent runtimes (Sherlock, AgentGit, Atomix) preserve completed work through verifiers, version control, or transactional tool boundaries. We present \textbf{Agent-Kernel}, a non-blocking runtime that ports this pattern t...
  </details>

- **2026-11-24** — Rafay Mohiuddin, Jiaqi Chen, Marc Pollefeys et al. — [VidForce: Predicting Force-Aware Articulation by Observing Humans](http://arxiv.org/abs/2611.32967v1)
  <details><summary>📄 Abstract</summary>
  People can anticipate how an object moves and the effort an interaction may require by watching others. How can embodied agents acquire this understanding from video? Force measurements provide direct sensory supervision, but require specialized equipment and remain limited in quantity. We introduce VidForce, which estimates an interaction trajectory together with a force profile from a third-person RGB video; 2D contact clicks and textual object-action prompts are optional. Our approach makes l...
  </details>

- **2026-11-24** — Yi-Jun Chen, I-Tsen Hsieh, Li-Wun Chang — [One Style Fits All? Cultural Values Embedded in Conversational AI via a People-Pleasing Lens](http://arxiv.org/abs/2611.32939v1)
  <details><summary>📄 Abstract</summary>
  Conversational AI systems trained on large-scale web corpora inevitably encode the cultural values and interactional norms embedded in their training data, yet our understanding of how deployed LLMs reflect or reinforce culture-specific social expectations remains limited. This study examined how supportive versus challenging chatbot interaction styles shape user experience and continuance intention, and whether people-pleasing tendency (PPT) moderates these effects across cultures. Taiwanese (N...
  </details>

- **2026-11-24** — Kaidi Zhang, Pengyuan Guo, Zhengtong Xu et al. — [Atomic Policy: Composing Atomic Manipulation Skills with Agentic Reasoning](http://arxiv.org/abs/2611.32813v1)
  <details><summary>📄 Abstract</summary>
  Long-horizon manipulation requires robots to translate task intent into physical interactions as the scene changes. Vision-language models (VLMs) offer semantic and spatial reasoning, while visuomotor policies provide fine-grained control. Yet ambiguous goals and dependencies between actions make their integration challenging. We introduce Atomic Policy, a framework that composes learned manipulation skills through grounded steering and execution feedback. A VLM estimates the symbolic state and ...
  </details>

- **2026-11-24** — Yanzhe Chen, Zhijun Cao, Ruihe An et al. — [MRBench: Benchmarking Physical Necessity Reasoning in Heterogeneous Multi-Robot Manipulation](http://arxiv.org/abs/2611.32803v1)
  <details><summary>📄 Abstract</summary>
  Recent advances in multi-robot manipulation have shown how robots can collaborate to accomplish complex tasks. However, successful coordination does not reveal which robots are actually needed. The same task may require different teams as robot capabilities change, resources become unavailable, or objects replace robotic support. We argue that reliable multi-robot manipulation requires physical necessity reasoning: understanding what a task demands, which resources can fulfill those demands, and...
  </details>

- **2026-11-24** — Aly Magassouba — [Supply Geometry, Learn Execution: Screw Attention for Zero-Shot Policy Transfer in Robot Manipulation](http://arxiv.org/abs/2611.32797v1)
  <details><summary>📄 Abstract</summary>
  We present the Screw Attention Policy, a geometry-centric manipulation framework that supplies task geometry explicitly and learns only execution. The policy operates on object poses, relative SE(3) transforms, and joint screw axes provided by perception and robot models. The policy requires only 30K learned parameters. Trained entirely in simulation on a single robot arm, the policy generalises to new scene layouts, transfers zero-shot across robot embodiments, and deploys directly on a real ro...
  </details>

- **2026-11-24** — Yunzi Wu, Sunyao Zhou, Xiaotao Zhang et al. — [DeCoNav-Act: Benchmarking Collective Physical Capability in Multi-Robot Mobile Manipulation](http://arxiv.org/abs/2611.32683v1)
  <details><summary>📄 Abstract</summary>
  Robot teams can split workloads or combine complementary bodies, but only if each robot leaves the shared world in a state its teammate can use. Existing multi-robot benchmarks emphasize task allocation and skill sequencing, rarely testing whether the resulting physical states are usable. To evaluate collective physical capability, we introduce DeCoNav-Act, a benchmark for language-guided multi-robot mobile manipulation in a shared physics simulation. Its 350 homogeneous and 150 heterogeneous ta...
  </details>

- **2026-11-24** — Yushi Long, Juzhan Xu, Haibin Huang et al. — [RoboRecast: Intent-Preserving Demonstration Augmentation via Diagnosis-Driven Optimization](http://arxiv.org/abs/2611.32622v1)
  <details><summary>📄 Abstract</summary>
  Collecting diverse real-world manipulation demonstrations is costly, motivating the use of simulation to augment existing demonstrations for robot policy learning. When objects, layouts, or robots change, transferring motions from a source demonstration can produce behavior that is semantically implausible or physically infeasible in the new setting. We introduce RoboRecast, an agentic optimization framework that preserves the interactions required by the source task while jointly optimizing the...
  </details>

- **2026-11-24** — Jiayi Liu, Ke Ye, Jiaming Zhou et al. — [Next-Manip: On-Demand Agent-Policy Collaboration for Robotic Manipulation](http://arxiv.org/abs/2611.32533v1)
  <details><summary>📄 Abstract</summary>
  General-purpose robotic manipulation requires task reasoning, failure recovery, and precise control, yet limited manipulation data make these abilities difficult to obtain from a single policy. Recent multimodal agents show promise in task reasoning and recovery but lack reliable fine-grained control and incur high inference cost, whereas learned policies provide efficient fine-grained execution but struggle beyond their learned skills. Although their complementary strengths suggest combining th...
  </details>

- **2026-11-24** — Zixiao Gu, Qiren Qin, Yu He et al. — [ActiveBridge: Scaling Active Prior for Robots through Egocentric Perception-Interaction Modeling](http://arxiv.org/abs/2611.32098v1)
  <details><summary>📄 Abstract</summary>
  Robotics foundation models are now widely used for manipulation, and egocentric videos offer rich data for scaling. However, existing methods overlook the human active priors captured in egocentric videos, which limits performance in unstructured scenes. They act on given observations instead of actively seeking information as humans do. We propose ActiveBridge, a training framework that learns these human active priors and transfers them to robots through world-action modeling. We design a robo...
  </details>

- **2026-11-24** — Liyang Li, Mingyu Liu, Xiaoman Li et al. — [RoboHarness-RL: Agentic Reinforcement Learning for VLM-Based Robot Manipulation](http://arxiv.org/abs/2611.32016v1)
  <details><summary>📄 Abstract</summary>
  Agentic harnesses enable frontier vision-language models (VLMs) to manipulate robots through perception, planning, and control tools, yet achieving comparable performance with compact open-weight VLMs remains challenging. We present RoboHarness-RL, an agentic reinforcement learning framework for improving VLM-based robot manipulation through tool calls. Starting from supervised fine-tuning on successful teacher demonstrations, the VLM further improves through multi-turn reinforcement learning wi...
  </details>

- **2026-11-24** — Seonghwan Park, Inho Chang, Min-Gyu Park — [CodeHOI: Code with Agents for Physically Plausible 4D Hand-Object Interaction](http://arxiv.org/abs/2611.31976v1)
  <details><summary>📄 Abstract</summary>
  Modeling 4D hand-object interaction (HOI) is fundamental to understanding manipulation. This requires physics, since hands move objects only by touch and each material responds differently. Yet existing methods ignore this physics or simulate only a narrow range of matter. Programs can instead describe any matter with its physics, but coding agents omit the hand that drives the interaction. We close this gap with CodeHOI, to our knowledge the first agentic framework that writes physically plausi...
  </details>

- **2026-11-24** — Ming-Lun Lee, Yi-En Li, Feng-Dian Su et al. — [DUALingo: A Dual-Hand Instruction-Guided Dataset for Affordance Grounding on 3D Objects](http://arxiv.org/abs/2611.31919v1)
  <details><summary>📄 Abstract</summary>
  Affordance grounding localizes where an agent should interact with an object to perform a task. Many everyday manipulation tasks, however, require bimanual affordance, in which two hands assume complementary and cooperative roles to accomplish a shared goal. Existing 3D affordance datasets primarily ground single interaction regions, and manually annotating dual-hand, cooperative contacts does not scale. To address this gap, we introduce DUALingo, a large-scale dataset for task-conditioned, role...
  </details>

- **2026-11-24** — Zheng Sun, Zhuo Li, Zhihao Li et al. — [RESET: One Demonstration, One Verified World, Self-Improved Skills Across Embodiments](http://arxiv.org/abs/2611.31894v1)
  <details><summary>📄 Abstract</summary>
  Large language model (LLM) coding agents can iteratively self-improve robot manipulation skills in simulation benchmarks, yet real-world tasks provide neither ground-truth success scorers nor resettable practice environments. Our key observation is that a single real demonstration simultaneously specifies scene geometry, defines the terminal success criterion, and serves as a physical reference trajectory for verifying world fidelity---all decoupled from the source robot's kinematics. We present...
  </details>

- **2026-11-24** — Jin Sano — [Functional Programming with Hypergraph Transformation](http://arxiv.org/abs/2611.31858v1)
  <details><summary>📄 Abstract</summary>
  Complex data structures are difficult to manipulate declaratively while preserving their shape invariants. Functional languages offer pattern matching and strong static guarantees, but their type systems primarily describe tree-shaped data. Graph transformation languages support richer structures, yet their state-oriented models do not integrate naturally with value- and function-based programming.   This dissertation introduces $λ_{GT}$, a functional language that integrates port-hypergraph tra...
  </details>

- **2026-11-24** — Jin Yang, Youlin Wang, Ping Wei — [Many Senses, One World: Learning Hierarchical Multimodal World Representations for Bimanual Dexterous Manipulation](http://arxiv.org/abs/2611.31782v1)
  <details><summary>📄 Abstract</summary>
  Bimanual dexterous manipulation relies on multimodal inputs that capture visual context and non-visual physical interaction cues for precise and coordinated control. To address the challenge of effectively integrating these modalities for policy learning, we propose HiMoDex, a two-stage framework centered on hierarchical multimodal world-state representations. In Stage 1, we pretrain a hierarchical representation network on the collected dataset of 1.19 million synchronized multimodal time steps...
  </details>

- **2026-11-24** — Mingyu Kim, Doguk Kim — [Tokenization and Architecture Jointly Allocate Component Roles in Time Series Transformers](http://arxiv.org/abs/2611.31730v1)
  <details><summary>📄 Abstract</summary>
  Time series transformers have achieved strong forecasting performance, yet it remains unclear which of their components, attention or the feed-forward network (FFN), constructs temporal features, and how tokenization such as patching changes this. We propose a temporal probing framework that uses 15 token-level diagnostic tasks to measure feature construction as the gain in linear decodability of temporal properties from one sub-layer to the next (a matched MLP probe already saturates at the emb...
  </details>

- **2026-11-24** — Nadav Magar, Amir Hertz, Ariel Shamir et al. — [BriConstrain: Geometrically Constrained Decoding for Autoregressive Brick Assembly Generation](http://arxiv.org/abs/2611.33135v1)
  <details><summary>📄 Abstract</summary>
  Language models can generate LEGO$^\circledR$ assemblies from text, but their builds often contain parts that collide or attach to nothing. The usual approach of rejecting and resampling invalid placements discards decoded tokens without guaranteeing a valid build. We present BriConstrain, a constrained decoding method that restricts a pretrained language model's next-token probabilities before sampling, steering it towards valid placements. Because the validity of a brick placement depends on t...
  </details>

- **2026-11-24** — Hussamuddin Syed — [A Bias in Disguise: Tiny Gradient Edits Stop a Small Language Model's Thinking Loops and Complement a Frontier Model's Weight Edit](http://arxiv.org/abs/2611.33133v1)
  <details><summary>📄 Abstract</summary>
  Qwen3.5-0.8B rarely finishes reasoning in thinking mode: at a 4,096-token budget only 1 or 2 of 500 MATH-500 answers close their think block (two seeds), and accuracy is 15.4%. A recent demonstration had GPT-6 Astra edit 131,072 of the model's weights without gradients and reported MATH-500 rising from 7.9% to 48.1% at a 32,768-token budget. We provide the missing gradient baseline, then combine the two edits. Fine-tuning only the 140 to 139,750 weights with the largest gradient, on the model's ...
  </details>

- **2026-11-24** — Yuchao Wu, XingCheng Liang, Xuanze Wang et al. — [SAG-Mem-1.0 Technical Report](http://arxiv.org/abs/2611.33124v1)
  <details><summary>📄 Abstract</summary>
  Long-term conversational memory requires retrieving complementary facts scattered across dialogue sessions, including intermediate evidence with limited similarity to the original question. Existing approaches often rely on derived memory representations or persistent relational structures, introducing construction costs and potentially losing source details. We present SAG-Mem, a conversational memory framework that preserves complete dialogue messages in non-overlapping chunks and discovers co...
  </details>

- **2026-11-24** — Hamin Koo, Chanjoo Jung, Fangzhao Wu et al. — [Auditing the Judge: Human-Derived Bias Discovery, Quantification, and Mitigation in LLM Judges](http://arxiv.org/abs/2611.33065v1)
  <details><summary>📄 Abstract</summary>
  While Large Language Models (LLMs) are increasingly deployed as automated evaluators in evaluation and training pipelines, their judgements are often affected by systematic biases that conflict with human preferences. Although prior work has identified various biases and proposed methods for detecting and mitigating them, less attention has been paid to using human preferences to inform bias identification and mitigation. Moreover, these approaches rely heavily on pre-discovered bias lists, over...
  </details>

- **2026-11-24** — Uriel Feige, Vadim Grinberg — [Approximate MMS allocations for large number of agents](http://arxiv.org/abs/2611.33051v1)
  <details><summary>📄 Abstract</summary>
  We consider allocation of indivisible items to agents with non-negative additive valuations, under the maximin share (MMS) fairness benchmark. We prove that for every $ρ< 1$, there exists some $n_ρ$ such that every allocation instance with $n \ge n_ρ$ agents has a $ρ$-MMS allocation. This was explicitly stated as a conjecture in a recent paper of the authors, where it was shown to hold if the number of items is at most $(2 - ε)n$ (and $n \ge n_{ρ, ε}$). We build on some techniques from that earl...
  </details>

- **2026-11-24** — Pengwei Wang, José Morano, Botond Fazekas et al. — [Linear Probes Can Guide: Training-Free Control of Representation Generators](http://arxiv.org/abs/2611.33037v1)
  <details><summary>📄 Abstract</summary>
  Representation-space generative models, such as Representation Autoencoders (RAEs), leverage pretrained vision foundation models (VFMs) primarily to accelerate training and improve sample fidelity. Yet VFMs are more than reconstruction tokenizers, as they feature rich representation spaces that are highly organized and linearly readable. We observe that this removes a key obstacle of post-hoc guidance: by linearity of expectation, a clean probe applied to an ideal denoiser's prediction yields th...
  </details>

- **2026-11-24** — Fabian Gröger, Shuo Wen, Maria Brbić — [On Potentiality and Actuality Of Foundation Models](http://arxiv.org/abs/2611.32991v1)
  <details><summary>📄 Abstract</summary>
  Foundation models are built through large-scale pretraining, often followed by post-training, and are then adapted to specific tasks and behaviors. But, does the adaptation add truly new capabilities, or the base model already holds it? We decompose the update induced by different adaptations into a component shared across all inputs and a residual that varies with the input. We find that the shared component suffices for most of the adaptation gain and can be learned directly: a shift adapter t...
  </details>

- **2026-11-24** — Max Raner — [Efficient inferential models and their fiducial connections](http://arxiv.org/abs/2611.32930v1)
  <details><summary>📄 Abstract</summary>
  Valid inferential models (IMs) provide frequentist calibration guarantees, but validity alone does not determine which construction is most informative. We study finite-sample efficiency through concentration risk, the expected volume under a possibility contour. For a smooth, fully identified association and a specified parameter-volume measure, a weighted Neyman--Pearson argument identifies the generalized fiducial density as the optimal score for minimizing cut volume subject to fixed-data au...
  </details>

- **2026-11-24** — Xiaofeng Shi, Qian Kou, Hua Zhou — [InstructReplay: Replaying Assistant Turns to Preserve General Behavior During Factual Fine-Tuning](http://arxiv.org/abs/2611.32918v1)
  <details><summary>📄 Abstract</summary>
  Fine-tuning an instruction-tuned language model on new facts often erodes its general abilities. We find that standard fine-tuning lowers instruction-following, reasoning and coding benchmarks by 35 points on average, and that these losses track a collapse in answer length: fine-tuned models at least halve their responses, and the further a response drifts from the initial model's length, the more often it fails. We propose InstructReplay: the initial model answers a set of general instructions ...
  </details>

- **2026-11-24** — MD Junayed Talukdar, Khosro Salmani — [AI, Bias, and Inclusion: A Two-Phase Mixed-Methods Study of Gender Bias, Awareness, and Trust in Artificial Intelligence](http://arxiv.org/abs/2611.32869v1)
  <details><summary>📄 Abstract</summary>
  Artificial Intelligence (AI) systems are widespread across fields such as healthcare, finance, employment, and criminal justice, with a substantial impact on the lives of individuals and society. However, it has been established that AI systems perpetuate existing social inequalities, particularly through biases that are not easily discernible. Such biases are embedded in the technical and social structures of artificial intelligence systems, making them difficult to detect. These biases challen...
  </details>

- **2026-11-24** — Jing Jia, Guanyang Wang — [Tabra Blends: Improving the Accuracy--Latency Trade-off with Complementary Tabular Models](http://arxiv.org/abs/2611.32859v1)
  <details><summary>📄 Abstract</summary>
  Tabular foundation models make different trade-offs between prediction accuracy and latency. We study whether a compact ensemble can deliver higher accuracy in less time. Across 816 TabArena splits, our blend of four-estimator Kumo and one LimiX pipeline reaches 2063.8 Elo, 45.4 points above the top published entry in the same fit. Its normalized fit + predict time is 15% lower than Kumo-16's and 98% lower than full LimiX's. We find that greater prediction diversity between the two models helps ...
  </details>

- **2026-11-24** — Zhiyuan Zhang, Yanzhao Li, Hui Dong et al. — [HiCal: Offline Calibration for Hierarchical Scale Encoding in Accurate HiF4 Quantization](http://arxiv.org/abs/2611.32624v1)
  <details><summary>📄 Abstract</summary>
  Block floating-point (BFP) quantization is widely adopted for efficient low-bit large language model (LLM) inference, where the choice of block scales plays a critical role in quantization accuracy. HiFloat4 (HiF4) employs a hierarchical scale encoding scheme consisting of a global E6M2 scale and two levels of binary scale extensions. However, its conventional rounding rule and fixed scale extension thresholds may not fully capture the statistical characteristics of the quantized tensors in prac...
  </details>

- **2026-11-24** — Lixuan He, Shengqu Cai, Fang Wu et al. — [Recursive Collective Intelligence: Emergence on an Equal-Budget Ladder in Multi-Agent LLM Systems](http://arxiv.org/abs/2611.32606v1)
  <details><summary>📄 Abstract</summary>
  Large language models increasingly work as teams of agents, and a team is expected to solve problems beyond the reach of any single member. Most evaluations credit a team for outperforming a single agent, without accounting for the additional computation: a team may consume many times the tokens of one agent, and a plain vote over independent answers already explains most of the reported gain. Two questions therefore remain open: When does interaction itself make a group smarter, and can a group...
  </details>

- **2026-11-24** — Nora A. M. A. Talkhan, Ibrahim Abdelbaky, Fatma A. Omara — [Representation and Model Contributions on Small Molecular Benchmarks: Controlled Comparisons and External Evaluation](http://arxiv.org/abs/2611.32568v1)
  <details><summary>📄 Abstract</summary>
  Improvements in molecular property prediction are usually attributed to the model, although part of the gain may come from the molecular representation. New models are commonly benchmarked against a random forest (RF) trained on a molecular fingerprint, a comparison that changes the model and the representation at the same time. We separate the two contributions with a two-by-two factorial design in which the RF and a second model (CatBoost or the tabular foundation models TabPFN and TabFM) are ...
  </details>

- **2026-11-24** — Lennart Schiweck, Cristóbal Curio — [MinPair: Measured Minimal Pairs for Fine-Grained Control in Text-to-Motion Generation](http://arxiv.org/abs/2611.32549v1)
  <details><summary>📄 Abstract</summary>
  Text-to-motion generation has made great progress in capturing what action to perform, yet it remains limited in controlling how that action is executed. For example, when only the height word of a kick request changes, none of the tested state-of-the-art methods reaches all three of knee, waist and head height. The other words of a caption usually imply an attribute such as height, so neither the training loss nor the standard metrics require a model to use the word that states it. A model has ...
  </details>

- **2026-11-24** — Xu Zhang, Xinpeng Zhang, Yunrui Zou et al. — [RSReasoner: Reformulating and Auditing Geospatial Reasoning Segmentation](http://arxiv.org/abs/2611.32536v1)
  <details><summary>📄 Abstract</summary>
  Geospatial reasoning segmentation aims to localize geographic targets from language requiring semantic inference beyond direct visual perception. However, existing benchmarks often operationalize reasoning as category omission while overlooking attribute mixing, which neglects explicit-category reasoning, introduces perceptual shortcuts, and fails to precisely evaluate reasoning capability. To diagnose and address these limitations, we first reformulate geospatial reasoning segmentation along ca...
  </details>

- **2026-11-24** — Yi-Fei Zhang, Ting-Ting Wang, Zhong-Jie Wang et al. — [Reconfigurable Chiral Phonons and Their Selection in Asymmetrically Stacked Graphene MoirMoiré Superlattices](http://arxiv.org/abs/2611.32466v1)
  <details><summary>📄 Abstract</summary>
  Chiral phonons, lattice vibrations carrying angular momentum, offer a new handle for controlling phonon-mediated phenomena in condensed matter, yet their on-demand generation and deterministic control remain challenging. Here we show, using helicity-resolved Raman spectroscopy, that asymmetrically stacked graphene moiré superlattices provide a reconfigurable platform for chiral phonons. We observe a finite degree of circular polarization for both chiral interlayer shear phonons and intralayer op...
  </details>

- **2026-11-24** — Philipp Koch, Alexander Posztos — [Grokipedia stretches the US political spectrum](http://arxiv.org/abs/2611.32420v1)
  <details><summary>📄 Abstract</summary>
  Language models now write reference works that people and other AI systems consult. Grokipedia, written by xAI's model, presents itself as a less biased alternative to crowd-edited Wikipedia. We compare the biographies of 1,614 Democratic and Republican current and former politicians, from Andrew Jackson to members of the current Congress, on both encyclopedias in February and November 2026. For nine in ten Republicans, Grokipedia's biography reads as if written by a more conservative author tha...
  </details>

- **2026-11-24** — Ruiqi Zhao — [Within-task hazards of AI agents: unidentified by time-horizon curves, identified by repeated runs](http://arxiv.org/abs/2611.32415v1)
  <details><summary>📄 Abstract</summary>
  The time horizon of an AI agent is read off a curve: the probability that the agent completes a task, plotted against the time a human needs for it. Several recent analyses fit survival models to this curve and conclude that agents' hazard of failure declines as a task goes on. The curve cannot support that conclusion. Every log-logistic horizon curve with slope $β\le1$ is a mixture of constant-hazard curves, and in a proportional-hazards frailty model the same curve is produced by every within-...
  </details>

- **2026-11-24** — Songtao Jiang, Yuan Wang, Fucheng Niu et al. — [Can AI Design a Better nnU-Net? A Hypothesis-Driven Architecture Discovery Loop from Failures to Design Rules](http://arxiv.org/abs/2611.32384v1)
  <details><summary>📄 Abstract</summary>
  Neural architecture search and LLM-driven evolution often reduce evaluation to a scalar fitness score, discarding failures that could explain why designs succeed or fail. We present a hypothesis-driven architecture discovery loop in which LLM agents diagnose structured error patterns, formulate falsifiable hypotheses, test counterfactual controls under a frozen nnU-Net pipeline, and distill validated mechanisms into executable trigger-to-action rules. Across eight search waves, the loop identifi...
  </details>

- **2026-11-24** — Haobo Zhang, Shuhao Zeng, Boya Di et al. — [Integrated Semantic Sensing and Communications: Target Attribute Inference and Beamforming Design](http://arxiv.org/abs/2611.32341v1)
  <details><summary>📄 Abstract</summary>
  Integrated sensing and communication (ISAC) is expected to become a key enabling paradigm for future 6G networks, supporting emerging applications that require a comprehensive understanding of sensed targets. As a step toward this goal, we consider an ISAC system with semantic sensing capability that determines what the sensed target is, where it is located, and how large it is. However, the accurate retrieval of these attributes, including target class, location, and size, is challenging due to...
  </details>

- **2026-11-24** — Irmaan Mirzanejad — [When Exact Token Importance Is Not Enough: Limits of Top-K Selection in LLM Attention](http://arxiv.org/abs/2611.32324v1)
  <details><summary>📄 Abstract</summary>
  Long-context language models often retain only a limited set of past token positions for an attention query. A common strategy scores positions individually and keeps the highest-ranked K. Yet attention weights are renormalized over the chosen set: two individually important positions need not form the best pair. We ask whether independent ranking suffices even when each importance score measures the exact downstream change in next-token predictions caused by deleting that position alone. It doe...
  </details>

- **2026-11-24** — Xiaoyang Fan, Yufan Cai, Zhe Hou et al. — [Refining and Aligning Clinical Reasoning with Health Guidelines via Formal Constraints](http://arxiv.org/abs/2611.32247v1)
  <details><summary>📄 Abstract</summary>
  Clinical reasoning from incomplete or conflicting patient evidence must account for low-probability but high-risk concerns while remaining grounded in health guidelines. We introduce VerClin, an explainable framework that extracts guideline conditions, exclusions, recommendations, and priorities into executable knowledge and represents patient conversations as scoped cases. A deterministic four-valued reasoner produces traceable guideline matches while preserving uncertainty and enforcing exclus...
  </details>

- **2026-11-24** — Zhenzhi Tang — [Who gets the information? An $α$-fair label-coverage framework for multi-label feature selection](http://arxiv.org/abs/2611.32200v1)
  <details><summary>📄 Abstract</summary>
  Recent information-theoretic filters for multi-label feature selection disagree on how to distribute relevance over labels: some amplify features that inform a few labels, others balance what every label receives. We show these choices are implicit social welfare functions. Treating labels as agents whose utility is the information they receive, we propose FLIC, which greedily maximises the $α$-fair welfare of per-label information coverage. A single parameter $α$ moves from utilitarian ($α=0$) ...
  </details>

- **2026-11-24** — Jiawei Gu, Linjie Li, Yiming Liu et al. — [ThinkMorph-SSL: Scaling Interleaved Multimodal Reasoning with Pretext Tasks](http://arxiv.org/abs/2611.32183v1)
  <details><summary>📄 Abstract</summary>
  People reason with pictures as well as words. Interleaved multimodal reasoning gives models a similar way to solve problems by creating intermediate images and using them to guide further reasoning. Training models with this ability usually relies on task-specific demonstrations, which are difficult to collect. We introduce ThinkMorph-SSL, a two-stage training recipe that uses images themselves as a source of supervision. The first stage, pretext reasoning, converts visual pretext tasks, such as...
  </details>

- **2026-11-24** — Yong Liu, Zhanpeng Shi, Peicong Lin et al. — [Benchmarking Protein Structure Tokenizers as Generation Targets for Language Models](http://arxiv.org/abs/2611.32168v1)
  <details><summary>📄 Abstract</summary>
  Discrete structure tokenizers are the standard way to give a language model access to protein three-dimensional structure, yet they are selected on how accurately they can be read, their reconstruction fidelity, while the property that governs generation is how well a model can write them. We measure this property, writability, directly: holding the base model, data, recipe and compute fixed, we swap only the tokenizer and train the same 9B model to emit structure tokens residue by residue, over...
  </details>

- **2026-11-24** — Jiachen Lei, Jiahong Wu, XiangXiang Chu — [Let The Pixels Through: Rethinking Long Skip Connections for Scalable Pixel Diffusion](http://arxiv.org/abs/2611.32151v1)
  <details><summary>📄 Abstract</summary>
  Training pixel diffusion models remains less straightforward, owing to the ad hoc training recipes and architecture designs, along with the sensitivity to hyper-parameter choices. We show that strong denoisers can be built by refining existing pixel-native designs from the literature. Specifically, we revisit the long skip connection in U-Net and find that the optimization benefit commonly attributed to it is not necessary for its denoising benefit. We further find that the conventional linear c...
  </details>

- **2026-11-24** — Mikołaj Martyka, Joanna Jankowska, Pavlo O. Dral — [OMNI-P3x universal neural network potential for large-scale computational photochemistry workflows](http://arxiv.org/abs/2611.32133v1)
  <details><summary>📄 Abstract</summary>
  Computational photochemistry supports the design and understanding of new materials. However, the high cost of excited-state quantum-mechanical (QM) calculations makes screening large molecular libraries prohibitively expensive. To address this limitation, we introduce OMNI-P3x, a universal machine-learned interatomic potential (MLIP) for singlet ground- and excited-state simulations of neutral and charged organic molecules. Trained on both ground- and excited-state conformations, it performs co...
  </details>

- **2026-11-24** — Wenhe Zhang, Xin Li, Hanzhi Chen et al. — [Wireless-OptSG: A Versatile Multi-Agent Optimization Framework for Wireless Resource Allocation](http://arxiv.org/abs/2611.32105v1)
  <details><summary>📄 Abstract</summary>
  6G wireless networks are expected to accommodate heterogeneous service requirements across diverse deployment scenarios, giving rise to physical-layer resource allocation problems with scenario-dependent objectives and constraints. Recent advances in large language models (LLMs) and agent systems can interpret wireless-domain specifications and incorporate execution feedback into optimization. However, translating language-level reasoning into feasible, high-quality resource allocations remains ...
  </details>

- **2026-11-24** — Dengzhe Hou, Kazunori D. Yamada — [EEGJev: A System One Decision Model and Benchmark for Multi-Task EEG Question Answering](http://arxiv.org/abs/2611.32100v1)
  <details><summary>📄 Abstract</summary>
  A single electroencephalographic (EEG) recording can support multiple decoding tasks. Fixed-label tests cannot show how EEG foundation models handle changing questions or options. We introduce EEGJev, a fast decision model that scores candidate answers in one pass. Our benchmark, EEGJev-Bench, covers six question types across 19 public EEG sources. We held the recording and options fixed while switching between questions about attributes paired during training, such as facial expression and the ...
  </details>

- **2026-11-24** — Seongrae Noh, RyunHa Lee, HyeongYeop Kang — [PreferenceScene: Personalized Indoor Scene Synthesis from Feedback](http://arxiv.org/abs/2611.32099v1)
  <details><summary>📄 Abstract</summary>
  Text-to-scene methods turn a short instruction into a furnished 3D room, but the room that a particular person wants rarely comes across fully in words: many preferences surface only when the person sees a concrete room and can point to what they like and dislike in it. We therefore study personalized indoor scene synthesis under hidden user preferences: over several turns, a system shows a 3D scene, and the user, who sees only rendered images of the scene, replies with brief free-form feedback ...
  </details>

- **2026-11-24** — Yang Bai, Yingzhi Xia, Ling Lin et al. — [Clinical3D-Bench: Evaluating and Improving Spatial Intelligence of Multimodal LLMs in Hospital Environments](http://arxiv.org/abs/2611.32094v1)
  <details><summary>📄 Abstract</summary>
  Spatial reasoning in hospitals requires tracking look-alike equipment, interpreting patient-relative directions, and judging passage widths, yet existing benchmarks provide limited coverage of these abilities. We introduce Clinical3D-Bench, a simulated benchmark with 3,368 questions of eight types on egocentric walkthroughs of 373 hospital-room layouts. Layouts follow hospital design guidelines, answers are computed from the 3D scenes, and paired scene states test whether models change their ans...
  </details>

- **2026-11-24** — Youngji Koh, Esther Kang, Gyuna Kim et al. — [CHORAL: A Multi-Agent Scaffold for Longitudinal Prognostic Reasoning from Patient-Generated Health Data](http://arxiv.org/abs/2611.32044v1)
  <details><summary>📄 Abstract</summary>
  Longitudinal patient-generated health data can inform prognostic reasoning about how patients' conditions may evolve between follow-up visits. Existing approaches summarize trajectories or predict symptom states, but provide limited support for examining how heterogeneous evidence informs prognosis. We present CHORAL, a multi-agent scaffold that forms domain-specific appraisals before cross-domain synthesis and review, preserving evidence and revisions. Informed by a formative study with 12 psyc...
  </details>

- **2026-11-24** — Patrick Q. Zhang, Yancheng Liang, Adrienne Fairhall et al. — [Unifying Partner and Environment Diversity to Improve Human-AI Coordination](http://arxiv.org/abs/2611.32031v1)
  <details><summary>📄 Abstract</summary>
  Real-world applications of modern AI systems require generalization to both unseen environments and novel human users. The field of zero-shot coordination (ZSC) has focused primarily on deploying AI to cooperate with novel partners in otherwise familiar environments. Popular population-based methods achieve this by partnering the agent with a diversity of simulated human users during training in a fixed environment, but does not consider the more realistic scenario where both the users and the e...
  </details>

- **2026-11-24** — Shaoan Xie, Fan Feng, Peiyuan Zhu et al. — [Learning Agent States for Latent Action Modeling](http://arxiv.org/abs/2611.32017v1)
  <details><summary>📄 Abstract</summary>
  Latent action models (LAMs) learn action-like latents from unlabeled video by coupling frame-pair inference with latent-conditioned prediction, enabling policy and world-model pretraining. However, what the latent must explain depends on the representation space used for action inference and transition prediction. When this space entangles the agent's evolving physical state with visual context, such as background and persistent agent appearance, inferred latents can encode information unrelated...
  </details>

- **2026-11-24** — Shuwei Wu, Longin Jan Latecki — [Describe, Don't Decide: Correcting Answer Bias in Multimodal LLMs](http://arxiv.org/abs/2611.31988v1)
  <details><summary>📄 Abstract</summary>
  Comparing two entities in an image, multimodal LLMs (MLLMs) often answer wrongly. We find that the answer bias enters not when the model sees, but when it decides with the image in view: the model's own descriptions of the two entities often already hold the right answer. We therefore propose D$^3$ (Describe, Don't Decide): the model describes each entity alone, decides from these descriptions without the image, and merges this decision with its direct answer. Without any training, D$^3$ improve...
  </details>

- **2026-11-24** — Xiaoyan Lei, Biao Luo, Wenlong Zhang et al. — [WaveSR: Physics-Inspired Wave Evolution Attention for Efficient Image Super-Resolution](http://arxiv.org/abs/2611.31984v1)
  <details><summary>📄 Abstract</summary>
  Recently, physics-inspired neural networks have gained widespread attention due to their interpretability. The closed-form, frequency-time decoupled solution of the wave equation offers linear complexity and allows different frequency components to evolve independently, making it a potential alternative solution for efficient image super-resolution. Therefore, a physics-inspired wave evolution attention framework is proposed, namely WaveSR. The WaveSR framework involves two key modules, i.e., wa...
  </details>

- **2026-11-24** — Wenchao Ma, Rui Yu, Fan Zhu et al. — [Decompose, Verify, Evolve: Physically Grounded Shape Decomposition](http://arxiv.org/abs/2611.31924v1)
  <details><summary>📄 Abstract</summary>
  Shape decomposition represents 3D objects as a compact set of geometric primitives for interpretable modeling and simulation. However, existing decomposition methods are trained primarily for geometric fidelity, without explicit constraints on physical plausibility, and can therefore produce disconnected parts or physically unstable reconstructions. We present PhysDec, an agentic framework that draws on a pretrained vision-language model's semantic understanding and commonsense reasoning to pred...
  </details>

- **2026-11-24** — Nikolaos Nikolaou — [How Far Apart Are Two Proofs? Measuring Proof Dissimilarity in a Proof Kernel and in Lean/Mathlib](http://arxiv.org/abs/2611.31811v1)
  <details><summary>📄 Abstract</summary>
  We now live in the age of machine-generated mathematics: AI systems produce research-level proofs faster than the human mathematical community can read them. Verification is only part of the challenge. We also need to know whether a "new proof" is indeed new, whether a thousand generated proofs contain one idea or many, and where each sits relative to human mathematics. All of these require measuring distances between proofs. Following Hilbert's 24th problem and the identity-of-proofs problem, w...
  </details>

- **2026-11-24** — Wafa Johal, Sarah Schombs — [Where is the Interface for the AI Harness?](http://arxiv.org/abs/2611.31739v1)
  <details><summary>📄 Abstract</summary>
  Norman's gulfs of execution and evaluation have guided interaction design for forty years, but both assume a user who is present in the loop. Agentic delegation breaks that assumption: users describe an outcome and leave, while the agent takes hundreds of unseen actions. Starting from a 2026 incident in which a research agent circumvented an access refusal on an Australian government portal and went unnoticed for two months, we argue that delegation opens two new gulfs. The gulf of specification...
  </details>

- **2026-11-23** — Neusha Javidnia, Ruisi Zhang, Farinaz Koushanfar — [RTLDetective: Agentic RTL Debugging through Dataflow Analysis and Simulation-Guided Fault Localization](http://arxiv.org/abs/2611.31709v1)
  <details><summary>📄 Abstract</summary>
  Large language model (LLM) agents have shown promise in RTL debugging, yet accurately localizing functional errors and generating reliable repairs remain challenging. We propose RTLDetective, a multi-agent framework that integrates signal dependency analysis, simulation-guided fault localization, and knowledge-based reasoning for automated RTL debugging and repair. RTLDetective constructs signal dependency graphs from RTL code and extracts failure information from waveform traces. A lightweight ...
  </details>

- **2026-11-23** — Yueling Fan, Jacqueline Wong, Olov Engwall et al. — [The Paradox of Agency-Preserving AI: Negotiating Learner Agency in Layered Human-AI Interactions](http://arxiv.org/abs/2611.31573v1)
  <details><summary>📄 Abstract</summary>
  Generative AI is increasingly used by learners in cognitively demanding tasks, but its capacity to provide immediate solutions raises concerns about decreased learner agency. Meta-level AI systems that provide reflective and metacognitive scaffolding have emerged as a promising approach to supporting learners' self-regulation. However, these systems introduce a fundamental paradox: AI intended to preserve learner agency can itself constrain that agency by regulating when, how, and why learners s...
  </details>

- **2026-11-23** — Umut A. Acar, Eli Goldweber — [Safe Autoformalization: Sufficiency and Necessity with Entailment Graphs](http://arxiv.org/abs/2611.31571v1)
  <details><summary>📄 Abstract</summary>
  Autoformalization translates a natural-language statement into a formula that captures its intent, which depends on the statement's context: the background that disambiguates it. LLMs make autoformalization practical, but their probabilistic output carries no formal guarantees. We propose techniques for safe autoformalization that certify one-sided logical adequacy: a formula sufficient for the intent is safe to enforce, and a formula necessary for it is safe to rely on. We use LLMs to generate ...
  </details>

- **2026-11-23** — Y. Lu, L. Wang, S. Okada — [BiSAT: Bidirectionally Aligned Semantic-Acoustic Tokenization for Speech Language Models](http://arxiv.org/abs/2611.30723v2)
  <details><summary>📄 Abstract</summary>
  Speech language models (LMs) generate speech as sequences of discrete tokens, requiring tokenizers that preserve both acoustic detail and linguistic content at a low bitrate. Semanticenhanced tokenizers may discard acoustic detail, whereas acousticoriented tokenizers retain acoustic variation that hinders language modeling. Unified tokenizers combine both, but encoding them within a single feature space can cause interference, and existing methods typically align acoustic features to fixed targe...
  </details>

- **2026-11-23** — Yohann Trivino — [Self-gravitating dust clumps: linear theory sets the threshold, the onset time and the spacing of their formation, then slow coarsening erases this pattern](http://arxiv.org/abs/2611.31327v1)
  <details><summary>📄 Abstract</summary>
  Planets form in disks of gas and dust. One step of their formation is the gathering of dust grains into dense clumps, under their own gravity. This work tries to predict when these clumps appear and how far apart they are. The grains attract each other through a gravity of finite range. The gas slows them down, and its turbulence spreads them out. The grains also cannot go beyond maximum packing: this is volume filling. The dimensionless model depends on two numbers. The first one is the gravita...
  </details>

- **2026-11-23** — Erik Derner — [CATWAY: Cost-sensitive agentic three-way robot decisions with calibrated language-model confidence](http://arxiv.org/abs/2611.31694v1)
  <details><summary>📄 Abstract</summary>
  A language-model robot agent must decide whether to execute, question or refuse an instruction, and an unsafe execution costs far more than an unneeded question. No prior robot gate derives all its thresholds from error costs or acts on calibrated probabilities, and none was fitted in one domain and evaluated unchanged in another. We propose CATWAY, a cost-sensitive three-way decision gate: a loss matrix over four instruction conditions (clear, ambiguous, infeasible, unsafe) fixes execute, ask a...
  </details>

- **2026-11-23** — Federico Echenique, Albin Erlanson, Anna Vakarova — [Fairness and incentives in combinatorial assignment](http://arxiv.org/abs/2611.31557v1)
  <details><summary>📄 Abstract</summary>
  We consider the fair and efficient random assignment of indivisible goods subject to resource constraints. Agents receive bundles randomly, but individual lotteries over bundles that are feasible in expectation need not be jointly feasible. Consequently, we treat a lottery over feasible allocations as a public good. We show that every feasible finite economy admits an envy-free and Pareto efficient random assignment that may be supported as a Lindahl equilibrium. For a finite type space with spe...
  </details>

- **2026-11-23** — Guangting Zheng, Shaoxuan Wang, Yu Yuan et al. — [Ground, Guide, Act: Improving VLA Spatial Generalization with Multimodal Foundation Models](http://arxiv.org/abs/2611.31452v1)
  <details><summary>📄 Abstract</summary>
  Vision-Language-Action (VLA) models effectively learn action policies from robot demonstrations, but struggle to generalize to changes in object positions and task goals. General multimodal foundation models (MFMs) offer complementary scene understanding and spatial reasoning, but remain slow and unreliable for direct fine-grained control. To understand how MFMs can improve VLA spatial generalization, we conduct a systematic capability analysis across multiple VLA architectures using atomic-stag...
  </details>

- **2026-11-23** — Mingyao Guo, Luting Wang, Murali Suganya et al. — [Non-integer high harmonic generation from many-body nonadiabatic gating](http://arxiv.org/abs/2611.31383v1)
  <details><summary>📄 Abstract</summary>
  High harmonic generation (HHG) in solids typically produces a rigid frequency comb locked to exact integer multiples of the drive photon energy. In strongly correlated materials, however, the light field can dynamically transform the electronic state on the timescale of harmonic generation itself, potentially violating this rule. Here, we report giant blueshifted, non-integer HHG in a cuprate Mott insulator Sr$_2$CuO$_3$ produced by mid-infrared excitations. Concurrent transient reflectivity mea...
  </details>

- **2026-11-23** — Jiawei Guo, Yu Huang, Dijiang Dong et al. — [RoboInF: A Benchmark for Instruction Fidelity in Robotic Manipulation](http://arxiv.org/abs/2611.30555v2)
  <details><summary>📄 Abstract</summary>
  Precise language control requires embodied models to follow instructions governing both task outcomes and execution. Although recent methods train policies to follow increasingly detailed commands, existing benchmarks often assess instruction following alongside perception, planning, and generalization to unfamiliar scenes. Higher task success therefore offers limited evidence of closer adherence to instructions. We introduce RoboInF, a benchmark measuring how reliably manipulation policies adap...
  </details>

- **2026-11-23** — Yunhe Zhang, Long Gao, Yuedong Fu et al. — [ConsisX: Cross-View Consistency Thinking in 3D for Vision-Language-Action Models](http://arxiv.org/abs/2611.30308v2)
  <details><summary>📄 Abstract</summary>
  Vision-language-action (VLA) models integrate visual perception and language understanding from vision-language models (VLMs) with action prediction for robotic manipulation. Although multi-view observations provide complementary scene information, VLMs model cross-view interactions based on 2D feature similarity, which can lead to physical inconsistency in the form of cross-view incorrect association between distinct entities and cross-view information fragmentation about the same entity. To ad...
  </details>


## 📊 统计 / Statistics

| 分类 / Category | 论文数 / Count |
|------|--------|
| jailbreak | 734 |
| prompt-injection | 713 |
| memory-poisoning | 59 |
| tool-use-attack | 181 |
| backdoor | 576 |
| adversarial-attack | 684 |
| privacy-leakage | 4691 |
| steganography | 96 |
| misuse | 1366 |
| red-teaming | 159 |
| vulnerability | 4192 |
| defense | 4141 |
| alignment | 3884 |
| robustness | 4249 |
| watermark | 822 |
| unlearning | 127 |
| agent-safety | 67 |
| benchmark | 78 |
| survey | 474 |
| other | 11733 |

---

📚 **全部 39026 篇论文**（2022 至今）请访问 [GitHub Pages](https://ny1024.github.io/AgentSafety-Papers/) 查看完整列表、搜索与筛选。

*Generated by AgentGuard at 2026-11-26 16:14:07*